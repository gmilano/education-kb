---
industry: education
region: Global
updated: 2026-10-11
---

# Education — foundational repositories

**Pass 128, 2026-10-11.** ⏱️ **Fifteenth pass of this date** (census window **13:4x → 14:2x UTC**).

## 🔴 🆕 `P128-A/F` — the release figure on this page was being read with an instrument that double-counts

🔵 **A foundational row earns its place partly on release engineering**, so the tag figure on this
page is load-bearing. 🔴 **`git ls-remote --tags` emits two lines per ANNOTATED tag** — `refs/tags/X`
and the `refs/tags/X^{}` dereference — so a line-count census inflates every annotated-tag
repository and leaves lightweight-tag ones untouched.

🟢 **Re-derived with `^{}` subtracted, p127's ten figures reproduce exactly**, so this page's
FUN-MOOC and FSRS tiers are sound as published. 🔴 **The one foundational row that moves is the
Canvas connector**: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) is
**23** tags, not 26 — repaired in place above, with the old value kept visible as a record.

🟢 **The rule for this page, stated so it does not have to be rediscovered:**

> a release count is `git ls-remote --tags | grep -c 'refs/tags/'` **minus** the `^{}` lines.
> If the two numbers differ, the repository uses annotated tags and the line count is wrong.

## 🟢 🆕 `P128-B` — a second permissive, heavily released Canvas connector belongs on this page, and this KB already had it

| address | grant (payload · bytes · ref · SHA) | 🟢 real tags | latest tag | tier verdict |
|---|---|---|---|---|
| 🆕 [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **MIT** · `LICENSE` 1 070 B · `main` · `5da987a` | 🟢 **78** | `canvas-lms-mcp-v2.2.0` | 🟢 **Foundational at the LMS edge.** Widest surface in the cluster (gradebook history, rubrics, admin workflows, write paths behind env gates); 🔵 unplaced — © 2026 **Christian Bru**, no jurisdiction in the payload |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `63f4222` | **23** | `v1.14.0` | 🟢 **Foundational and PLACED** — `P800`-grade on **North America**. Prefer it where the region line matters |
| [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | 🟢 **MIT** · 1 081 B · `main` · `2343408` | **12** | — | 🟡 **Third independent project**, smaller surface; 🔵 unplaced |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · `LICENSE` 34 523 B · `main` · `5a194a5` | 7 | — | 🔴 **Declined, unchanged** — network copyleft on a networked server. 🟢 **Reproduced byte for byte this pass** |

🔴 **Three of those four addresses are independent projects and two more addresses that look like
projects are forks** (`lindsay-cheng`, `YeetingWaterbottle` — identical 1 071 B payload, identical
holder, divergent HEAD). 🔵 **The Canvas edge is a three-project layer with a fork fringe, and the
discriminator is the payload, not the API.**

🟢 **The asymmetry this page should carry forward:** **Canvas** has three permissive maintained
connectors; **Moodle** — the platform LATAM ministries and public universities actually run — still
has one AGPL-3.0 server and one unreleased MIT fork base
([`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server), 0 tags).
🔴 **That gap is a region gap, not a technology gap, and it has not closed in this pass either.**

## 🔴 🆕 `P128-E` — read the HOLDER line, not just the token, before a row joins this page

🟡 [`scaleapi/researchrubrics`](https://github.com/scaleapi/researchrubrics) serves a complete
**MIT** permission text (1 078 B, `main` · `2dc80e2`) whose copyright line is the **unfilled
template**: *"Copyright (c) 2025 **[Authors/Institution]**"*. 🔵 **There is no one to attribute and no
one disclaiming warranty**, so the grant cannot be relied on even though every other line of it is
standard. 🔴 **For a foundational row this is disqualifying, and it is harder to catch in review than
a missing file**, which is why it is now a page rule and `ACTION AT` for the next pass.

🔵 **This page already labels a username holder as not `P800`-grade** (`peancor`, and now
[`supe-log/writing-engine`](https://github.com/supe-log/writing-engine), MIT 1 065 B, **0** tags).
🟢 **A placeholder holder is the same class one step worse: not merely unplaceable, but unattributable.**



# Education — foundational repos

**Pass 127, 2026-10-11.** ⏱️ **Fourteenth pass of this date** (census window **12:4x → 13:0x UTC**).

🟢 **A supply pass. 33 of 33 addresses resolved on the git lane; every grant below read from the
payload, every SHA from `git ls-remote`.**

## 🟢 🆕 `P127-F1` Tier 1e — the retention spine: FSRS, permissive in seven languages

🔵 **This page has carried spaced repetition only as an application property** (`ankitects/anki`,
AGPL-3.0 with per-file exceptions; `ankimcp/anki-mcp-server` as a tool surface). 🟢 **The algorithm
and its bindings are a foundation tier in their own right, and they are permissive.**

🔵 **Tabled once on `agents/top.md` under `P127-C` with full payload bytes and SHAs.** What belongs
on *this* page is the dependency decision, because that is what a foundation tier is for:

| if the client's stack is… | take | grant | release engineering |
|---|---|---|---|
| Python | [`py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | 🟢 MIT | 38 tags |
| TypeScript / JS | [`ts-fsrs`](https://github.com/open-spaced-repetition/ts-fsrs) | 🟢 MIT | **114 tags** |
| Rust | [`fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 BSD-3-Clause | 73 tags |
| Go | [`go-fsrs`](https://github.com/open-spaced-repetition/go-fsrs) | 🟢 MIT | 16 tags |
| Swift / iOS | [`swift-fsrs`](https://github.com/open-spaced-repetition/swift-fsrs) | 🟢 MIT | 🟡 individual holder |
| Dart / Flutter | [`dart-fsrs`](https://github.com/open-spaced-repetition/dart-fsrs) | 🟢 MIT | — |
| in-browser / WASM | [`fsrs-browser`](https://github.com/open-spaced-repetition/fsrs-browser) | 🟡 BSD-3 body, no title line | 34 tags |
| **fitting to a real review log** | [`fsrs-optimizer`](https://github.com/open-spaced-repetition/fsrs-optimizer) | 🟢 BSD-3-Clause | **127 tags** |
| the algorithm itself, to implement | [`free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 MIT | 0 tags — a spec, not a release |

🟢 **Why this is a foundation and not a library curiosity:** every tutoring engagement eventually
has to answer *"when does this learner see this item again"*, and the choice is to reimplement a
scheduler, buy one, or depend on this. 🔵 **`fsrs-optimizer` is the row that matters most** — it
fits the model's parameters to the client's own review history, which is the difference between a
generic scheduler and one calibrated to their learners.

🔴 **The hole in the tier, and it is the same hole as `Gap 393`:**
[`srs-benchmark`](https://github.com/open-spaced-repetition/srs-benchmark) (**274★**) — the
benchmark that ranks these schedulers — carries **no grant in 15 probed filenames** and its README
makes no licence claim. 🔴 **`fsrs4anki-helper` (325★) likewise carries none in 6.**
🔵 **See `intel/trends.md` `P127-T2`: this is the second independent instance in this industry of
granted implementations with an ungranted yardstick, and n=2 makes it a shape.**

🟡 **Region, stated honestly rather than upgraded.** The family's README derives FSRS from
**MaiMemo's DHP model**, linking a Chinese-language explainer and a KDD 2022 paper — so the
*lineage* is APAC. 🔴 **But no payload in the family carries a jurisdiction** (holders read
*"Open Spaced Repetition"*, plus two individuals), so these rows stay 🔵 **unplaced** under `P800`
rather than being promoted on a README link.

## 🟢 🆕 `P127-F2` Tier 1f — the FUN-MOOC platform spine, and the xAPI tier's only live MIT row

🔵 **`openfun` (France Université Numérique / GIP FUN MOOC) publishes ten repositories that
together form a platform spine; nine are MIT.** Tabled once on `agents/top.md` under `P127-A`.
What this page adds is how it sits against the tier already here.

🟡 **The xAPI / learning-record tier on this page already contained permissive rows** —
[`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0),
[`yetanalytics/lrs`](https://github.com/yetanalytics/lrs),
[`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) and
[`Apereo-Learning-Analytics-Initiative/Larissa`](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa).
🔴 **So [`openfun/ralph`](https://github.com/openfun/ralph) is not a discharge** — `agents/top.md`
`P127-B` records that correction in full. 🟢 **What it is: the tier's only LIVE MIT row**, since
[`KI-Campus/LRS`](https://github.com/KI-Campus/LRS), the only other MIT entry, is **ARCHIVED
read-only since 2026-02-20**.

🟢 **And the chain is the real addition:**

| layer | repo | grant |
|---|---|---|
| learner-event record | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT · 32 tags |
| analytics toolkit over xAPI | [`openfun/warren`](https://github.com/openfun/warren) | 🟢 MIT · 13 tags |
| dashboards (Grafana/Jsonnet) | [`openfun/potsie`](https://github.com/openfun/potsie) | 🟢 MIT · 17 tags |
| LTI tool-provider library | [`openfun/django-lti-toolbox`](https://github.com/openfun/django-lti-toolbox) | 🟢 MIT · 7 tags |
| K8s/Ansible deployment | [`openfun/arnold`](https://github.com/openfun/arnold) | 🟢 MIT · **119 tags** |

🔵 **One holder, one licence, five layers — an event-to-dashboard path that needs no grant
reconciliation.** 🔴 **The boundary:**
[`openfun/openedx-docker`](https://github.com/openfun/openedx-docker) is **AGPL-3.0**, because it
packages Open edX. 🟢 **The copyleft in this stack is one named layer, not a diffuse risk**, which
is what makes it costable.

## 🟢 🆕 `P127-F3` Tier 2h re-measured — the student-success tier gains a released, institution-held analytics row

🔵 **`Gap 385`, as p101 restated it, asks for a *permissive, modern, release-engineered* layer**
after `dssg/student-early-warning` turned out to carry bespoke U Chicago terms excluding the sale
of a service.

| address | grant (payload · bytes · ref · SHA) | ★ | tags | region | role |
|---|---|---|---|---|---|
| [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) | 🟢 **Apache-2.0** · `LICENSE` 11 379 B + `NOTICE` 304 B · `master` · `44dbf90` | 37 | **38** | 🟢 **North America** — `NOTICE`: © 2018-2019 **The Regents of the University of Michigan** | MyLA: student-facing learning-analytics dashboard over LMS data |

🟢 **Apache-2.0 with a patent grant, 38 tags, an institutional holder, and a `NOTICE` file** — the
`NOTICE` oracle this tier was built on at p101 works again here, and it is what makes the region
`P800`-grade rather than inferred.

🟡 **A note on the byte count, because this page pins them:** 11 379 B is **21 B larger** than
canonical Apache-2.0 (11 358 B). 🟢 **That is the Appendix boilerplate filled in rather than an
abridgement** — the opposite of `P127-F`'s `ai-literacy-superpowers` case (11 207 B, i.e. text
*removed*). 🔵 **Bigger-than-canonical is benign; smaller-than-canonical is the one to read.**

🔴 **What this does NOT close, stated so the gap stays usable:** MyLA is a **dashboard**, not a
risk model. 🔴 **A permissive, modern, release-engineered ML early-warning *model* is still absent
from this page**, and `Jasig/SSP` (Apache-2.0, 57 tags) remains the tier's only other
release-engineered row. 🟢 **The engagement consequence is precise: the presentation and
student-consent surface is now takeable permissively, and the model is the part the studio builds.**

## 🟢 🆕 `P127-F4` Tier 3b — the AI-literacy curriculum tier gains two PERMISSIVE bases

🔴 **This page has recorded the AI-literacy tier as dominated by Creative Commons**, which is fine
to teach from and awkward to fold into a closed training product. 🟢 **Two permissive rows this
pass**, tabled once on `agents/top.md` under `P127-G`:

- [`hanhuark/machine-learning-for-engineers`](https://github.com/hanhuark/machine-learning-for-engineers)
  — 🟢 **BSD-3-Clause**, 51★, AI/ML **and AI-literacy** curriculum for engineers: tutorials,
  assignments, projects, verified workflows for physical systems. 🟡 Region is org-name inference
  only; **not `P800`-grade**.
- [`BradGroux/ai-dev-days`](https://github.com/BradGroux/ai-dev-days) — 🟢 **MIT**, 33★, reusable
  events, curriculum, labs and tool tracks.

🔵 **Why the tier matters more than its star counts suggest: AI literacy is now a statutory duty in
two regions** — EU AI Act Article 4 (applying since 2 Feb 2025) and, in the US, H.R. 8747 cleared
committee this year (`intel/market.md`). 🟢 **A client under a literacy obligation needs curriculum
it can rebrand, and BSD-3/MIT is the version that permits it.**

**Pass 126, 2026-10-11.** ⏱️ **Thirteenth pass of this date** (census window **11:4x → 12:1x UTC**).

🟢 **Instrument: `compose/code/p126-address-binding/` — `ACTION AK` and `AM` discharged and not refuted; 🔴 **`ACTION AJ` and `ACTION AL` REFUTED on their own clauses**. `test_p126.sh` **20 passed / 0 failed**, fully offline, over 9 fixtures.**

## 🔴 🆕 `P126-A` — p125's committed evidence cannot be found again on p125's committed pages

p125 committed `out/ac-after.triples`: 36 `path:line|address|token` records, the residue of its own
`ACTION AC` assertion. 🔴 **Not one of those 36 line numbers names the address it is filed under.**

The cause is ordering, not drift and not a faulty recogniser. p125 measured the pages, then
**prepended its pass section to each page it had just measured**, and every coordinate below the
insertion moved down by the length of that section.

| page | p125's section | recorded → true |
|---|---|---|
| `agents/top.md` | **58** lines | `163` → **221** (`pupilfirst/pupilfirst`, CC-BY-SA-4.0) |
| `intel/market.md` | **63** | a uniform `+63` across all 4 of its records |
| `intel/trends.md` | **33** | `+33` across both |
| `intel/open-gaps.md` | **186** | `+186` across all 4 |

🟢 **The claims themselves survive.** Relocated by `(page, address, token)`, all 15 records of
`ACTION AJ`'s clause set are found and **0 are unlocatable** — the same claims, at coordinates the
pass itself invalidated. 🔵 **This is the lineage's own pattern one level up**: p122 found a census
less precise than the page, p123 a repair that was an edit, p124 a token read without its scope,
p125 an assertion run without its domain — and p126 finds **evidence keyed on a coordinate the pass
does not preserve.** This instrument's `out/` is therefore keyed on `(page, address, token)` and
never on a line number.

## 🔴 🆕 `P126-B` — one unreadable column heading, and the table reporting three false claims was itself an unmarked correction

Recomputed on the committed pages with p125's own code, the assertion returns **49** violations
rather than the 36 reported, and 🔴 **12 of the 49 sit inside p125's own section** — the largest
single bucket when each violation is attributed to the pass section it lives in (p122: 6, p93: 5,
p118: 4, p120/p116/p104: 3 each).

The cause is one heading. `P125-A`'s defect table — the table that reports the three live false
claims — is headed `| # | where | the page said | the file says | how it was missed |`, and
`HDR_OLD` carries `this KB said`, `KB said` and `pNNN said` but 🔴 **not `the page said`**. So
`classify_header` returns `None`, the table is not a correction table to the apparatus at all, its
quoted OLD values read as live claims, and the assertion re-raises them on each of the **6** pages
the table was copied onto.

🔵 **p125 invented a new column spelling in the same commit that shipped the sweep for forms
1–13** — which is `ACTION AM`'s argument restated as a measured fact rather than a prediction.

🟢 **Repaired this pass:** three spellings added to `HDR_OLD` (`the page said`, `the
{shelf,row,cell,table} said`, `as published`), after which p125's own writer reaches the rows.
**6 rows marked, form 2, one per page.** Rows 2 and 3 of that table are correctly *not* hits —
row 2's old value `MIT` is also a new value (for `pyBKT`), and row 3's old cell carries no licence
token at all.

## 🔴 🆕 `P126-C` — `ACTION AJ` and `ACTION AK` are one mechanism, and neither works alone

The 15 violations `ACTION AF` newly surfaced decompose exhaustively, and 🔴 **mis-binding explains
none of them**:

| n | class | why |
|---|---|---|
| **6** | `pupilfirst/pupilfirst` CC-BY-SA-4.0 | 🟢 `AK`'s class — a split grant collapsed to one token, so the surviving member reads as superseded |
| **4** | `oat-sa/tao-core` LGPL-3.0 | unmarked correction apparatus: a quoted retraction, and an old column whose header was not read |
| **3** | `instructure/canvas-lms`, `openedx/edx-platform` `GPL` | 🔴 **SUBSTRING, not binding** |
| **2** | `1EdTech/openbadges-specification` Apache-2.0 | the referent is *"the validator"* — named in prose, not as an address, so binding structurally cannot reach it |

🔴 **The 3 are `ACTION AG`'s own SUBSTRING class recurring in a function `AG` never reached.**
`repair_search.violations` tests `re.escape(tok)` between word boundaries instead of the
vocabulary, and `\bGPL\b` matches inside `GPL-3.0`. Line 524 of `compose/patterns.md` carries no
bare `GPL` at all — the vocabulary reads `GPL-3.0` and `AGPL-3.0`. `AG` guarded token *reading*;
the violation *check* was outside it.

🔴 **And `AK` cannot be implemented without `AJ`.** An address-level survivor set must be fed by
*bound* tokens. `compose/patterns.md` carries one cell naming [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT)
and [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) together, giving each its own
token in a parenthetical and retracting the earlier *"both"* reading. An unbound union hands
`MIT`, true of `pyBKT`, to `catsim` as a surviving member — clearing `catsim`'s superseded `MIT` on
**9** live rows: the defect p125 called *the one worth the pass*, re-opened by its own remedy.

🔵 **That cell is described here rather than quoted, and the reason is a finding of its own.**
🔴 **`mark_forms` is not fence-aware**: `_is_quote` skips a fence's delimiter lines but nothing
tracks fence STATE, so a licence token inside a fenced block is read as live prose. Quoting the
cell verbatim — even fenced — registered as an unmarked retraction on **7** pages, and the
self-audit caught it before this commit. `ACTION AR` makes the fence a scope.

| run | `pupilfirst` cleared (wanted 6) | `catsim/MIT` kept (wanted 9) | verdict |
|---|---|---|---|
| `AK` alone (`--no-bind`) | 🟢 6 | 🔴 **0 — laundered** | 🔴 refuted |
| 🟢 **`AK` over `AJ`** | 🟢 **6** | 🟢 **9** | 🟢 **not refuted** |

🟢 **So `AJ` is refuted as a CAUSE and indispensable as a MECHANISM, and those are not opposites.**
The binder needed three rules in priority order: a **short name** in backticks within 30 characters
(the only rule that resolves the `pyBKT`/`catsim` row — cell and distance both fail); **ordinal
pairing** where k addresses and k tokens sit in two cells; then the **cell wall and nearest
address**. Composed, the assertion falls from **49** violations over 23 addresses to **27** over 13.

## 🔴 🆕 `P126-D` — two writers ship side by side, and this pass published a false number before catching it

`compose/code/p125-retraction-cue/` contains **two** `apply_marks`: one in `correction_form.py`,
one in `mark_forms.py`. Only the second carries the `APPARATUS` guard and the cue model, and
🔴 **nothing in the directory marks the first as superseded.**

🔴 **p126 used the wrong one.** Measured against `correction_form`, `ACTION AM` reproduced **41 of
81 = 50.6 %** and the conclusion drafted was that 40 of p125's marks had no provenance in the
repository. Measured against `mark_forms` — p125's actual writer — it reproduces 🟢 **81 of 81 =
100 %, per page exactly**, and `AM` is not refuted.

| writer | proposes on p125's own committed pages | `APPARATUS` guard |
|---|---|---|
| 🟢 `mark_forms.apply_marks` | **0** — converged, exactly as p125 claimed | 🟢 yes |
| 🔴 `correction_form.apply_marks` | 🔴 **50** | 🔴 none |

Run with `P126-B`'s header patch, the superseded writer marks p125's own prose *about* the marker —
*"(`⚠️ **was 🟢 MIT**` inside the cell)"* — the exact false-positive class p125's fourth defect
fixed. Two such lines were written and reverted before `repair.py` was pointed at `mark_forms`;
`AM.5` now pins both numbers so the hazard cannot be hit silently again.

🔵 **The lesson is this pass's own:** a reproduction claim is only as good as the identification of
what it reproduces, and a directory shipping two writers without saying which is live invites
exactly this error. `ACTION AO` makes it refuse.

## 🔴 `ACTION AL` — a blind spot with nothing behind it

`ACTION AI` inferred the toolchain was blind to two conventions. Both were added and probed over
**32** candidate addresses × **21** paths = **672 probes**, each reading the repository's own bytes
on its real default branch (`raw.githubusercontent.com` resolves `HEAD`, so no branch is guessed).
🟢 **200 × 3, 404 × 669, and zero `000`/`403` — no proxy noise in the channel.**

| path class | probes | grants found |
|---|---|---|
| 🔴 `LICENSE.GPL`, `.LGPL`, `.MPL`, `.APACHE`, `.BSD` | **160** | 🔴 **0** |
| 🟢 `readme.txt` / `README.txt` / `Readme.txt` (WordPress plugin header) | 96 | 🟢 **1** — [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress), `License: GPLv3` at line 7 of 41 951 B |

🔴 **The clause needed 3 and got 1, and this KB already knew that one** — it is `P125-A`'s own
defect 3. The dual-licence filename convention does not occur anywhere in this corpus's no-grant
set. 🟢 **The extended path list is still correct to keep**: it is the right convention and costs
nothing. The honest statement is that it has no further yield here.

🔵 **Two caveats, both from the probe's own output.** The candidate set was harvested by text search
for no-grant language, which over-captures — 2 of the 3 hits (`moodle/moodle` `COPYING.txt`,
`celtic-project/LTI-PHP` `LICENSE`) are addresses this KB never claimed were grantless. And `AL`'s
literal subject, the **18 "genuinely absent"** addresses of p123's `ACTION Y`, are repositories
that **do not exist**; a 404 repository cannot carry a grant on any path, so that reading is vacuous
and the operative set had to be the exists-but-unread one.

## 🟢 Pre-registered for p127

🟢 **`ACTION AN`** — give `repair_search.violations` the vocabulary instead of `re.escape(tok)`, so
a family token cannot match inside a precise one, and re-run the lineage's baselines. 🔴 *Refuted
if fewer than the 3 `GPL` records this pass classified as SUBSTRING are removed, or if any of the
other 24 live violations disappears with them.*

🟢 **`ACTION AO`** — mark the superseded writer as superseded. Add a module-level refusal to
`correction_form.apply_marks` naming `mark_forms.apply_marks` as the live one, and assert no
instrument in `compose/code/` calls the former. 🔴 *Refuted if any pass's committed instrument
turns out to depend on it.*

🟢 **`ACTION AP`** — bind a token to a referent named in PROSE rather than as an address. The 2
`openbadges-specification` records are *"the spec carries no grant while the validator is
Apache-2.0"*, and that validator is a real, separately published address in this corpus. 🔴
*Refuted if fewer than both are resolved by matching a prose noun phrase to an address this KB
already publishes.*

🟢 **`ACTION AQ`** — the 8 remaining `catsim/MIT` rows, all on append-only pages or inside the
`"MIT both"` quantifier cell. Decide and record the rule: may an append-only page carry a
correction *annotation* without being rewritten? 🔴 *Refuted if the rule cannot be applied without
editing a single historical claim.*

🟢 **`ACTION AR`** — make the fence a SCOPE. `_is_quote` skips a fence's delimiter lines while
nothing tracks fence state, so every licence token inside a fenced block is read as a live claim.
🔴 *Refuted if fewer than the 7 rows this pass's own self-audit raised are cleared by tracking
fence state, or if doing so suppresses any of the 27 live violations.*

🔵 **`compose/code/p126-address-binding/out/` carries every number above, keyed on `(page, address, token)` and never on a line.**

**Pass 125, 2026-10-11.** ⏱️ **Twelfth pass of this date** (census window **11:0x → 11:1x UTC**).

🟢 **Instrument: `compose/code/p125-retraction-cue/` — `ACTION AF`, `AG`, `AH` discharged and not refuted; 🔴 **`ACTION AI` REFUTED on its own clause**. `test_p125.sh` **51 passed / 0 failed**, fully offline, over 25 fixtures.**

## 🔴 🆕 `P125-A` — three live false claims, and one of them is on a page p124 read by hand

p124 found **zero** live false claims among its 27. Over the full ten-page domain there are
**three**, each verified against the repository's own bytes on its real default branch.

| # | where | the page said | the file says | how it was missed |
|---|---|---|---|---|
| 1 | `agents/trending.md` | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) **453★** 🟢 `MIT`<!--corrected--> | 🟢 **`Apache-2.0`** — `main/LICENSE`, **11 358 B** | p124 repaired this address on `agents/top.md` **and recorded the repair on both of that page's tables**; the trending row was outside the assertion's domain |
| 2 | `compose/patterns.md` | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) + [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) 🟢 **`MIT` both** | 🟡 `pyBKT` **MIT**, `catsim` **`BSD-3-Clause`** — `dev/LICENSE`, **1 514 B** | 🔴 **inside p124's domain and read by hand.** The word *"both"* carries the error, and twelve other rows on these pages already say `BSD-3` |
| 3 | `verticals/solutions.md` | the licence-tier table counted [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) under 🔴 **"not open source / unknown"** as *"(no file)"* | 🔴 **`GPL-3.0`** — declared in the WordPress plugin header of `develop/readme.txt`: *"License: GPLv3"*, *"License URI: gnu.org/licenses/gpl-3.0.html"* | the row is right that there is no `LICENSE` **file**, and wrong about the tier. 🟢 **This KB's own `README.md` already records it as GPL-3.0** |

🔴 **Defect 2 is the one worth the pass.** A hand-read of a row that says *"MIT both"* about two
repositories confirms the token and not the quantifier. A single cell naming two addresses is the
smallest unit at which this shelf can be wrong about exactly one of them, and `ACTION AJ` makes
that the next thing measured.

🔵 **Defect 3 is the direction this KB's own `intel/trends.md` trend 1 names as the expensive
one**: an over-restrictive cell creates no legal exposure and silently deletes a platform from a
shortlist. **24 % of Mexico's LMS-carrying sites run LearnPress**, and the tier table had it in
the bucket a studio never reads twice. Repaired: copyleft **8 → 9 of 20**, not-open-source
**2 → 1**.

## 🟢 `ACTION AF` — one retraction CUE, not thirteen regexes

p124's `ACTION AC` enumerated **nine** surface forms of this KB's correction apparatus and reached
four. p125 began by writing one pattern per unreached form and stopped at **thirteen**:

| # | form | status |
|---|---|---|
| 1 | `⚠️ **was X**` bold | 🟢 p123 |
| 2 | audit-table OLD column | 🟢 p124 |
| 3 | prose `was X` + publication reference | 🟢 p124 |
| 9 | NEW column named by its SOURCE | 🟢 p124 |
| 4 | `⚠️ *was X*` **italic** | 🟢 **p125** |
| 5 | `⚠️ **KB said X**` | 🟢 **p125** |
| 6 | reversed `(New, published Old)` | 🟢 **p125** |
| 7 | `as X not Y` | 🟢 **p125** |
| 8 | OLD column whose NEW cell holds **no token** | 🟢 **p125** |
| 10 | 🔴 **`⚠️ was X` with NO emphasis at all** — **19 of the 61 violations**, the single largest class | 🟢 **p125** |
| 11 | prose naming a PRIOR PASS's reading (*"`p1040` read Elastic-2.0 …"*, *"an older row on this shelf said AGPL-3 and was superseded"*) | 🟢 **p125** |
| 12 | a `P###-x` finding SECTION whose heading announces the correction | 🟢 **p125** |
| 13 | a licence named in a **CONTRAST clause** (*"Neither restriction exists under AGPL-3"*) | 🟢 **p125 — and it needs no marker at all** |

🟢 **Enumeration is losing, and FORM 13 is why.** Every pass that writes a correction invents a
spelling, and the sweep that chases it ships one pass later — but a licence token inside a
comparison clause was **never a claim about that repository**, so marking it would record a
correction that never happened. The model therefore changes from a form list to the same two-part
rule the rest of this lineage converged on: a **retraction CUE** (a verb or sigil announcing a
superseded value) and a **SCOPE GATE** (`ACTION AG`) that tells a retraction from a contrast, a
quotation or a live claim. Forms 4, 5 and 10 collapse into one pattern with the asterisks optional.

**81 rows marked** across 9 pages; rows carrying the marker **105 → 190**. Applying it twice marks
nothing (asserted). 🟢 **40 of the 61 baseline violations resolved — the clause required 20.**

🔴 **And three defects in `ACTION AF`'s own first application, each found by re-measuring rather
than by inspection:**

| defect | what it did | the rule it became |
|---|---|---|
| a correction table's column mapping **outlived its table** | a header row whose columns `classify_header` cannot read left the PREVIOUS table's mapping in force, and the foundational shelf's **live** licence column was marked superseded on [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | a header row — the one directly above a `\|---\|` separator — always clears the mapping, read or not |
| the marker landed **inside** the emphasis | `⚠️ *was GPL<!--corrected-->*` splits the span the marker is meant to close, so the row read back as unmarked and the assertion re-raised it — 3 rows, all already repaired | the marker moves past any closing `*`/`**` the cue opened |
| `\| \`GPL\` \| 🟢 **GPL-3.0** \|` read as a correction | 20 Moodle-plugin rows marked as repairs that never happened | a bare family token made precise is a **RESOLUTION**, not a correction — `GPL → GPL-3.0` exactly as p124's `ACTION AD` resolved 41 bare `CC` grants without calling one a correction |

🔵 **A fourth was prose, not code**: *"(`⚠️ **was 🟢 MIT**` inside the cell)"* and
*"read *\"⚠️ **was LGPL-3.0**\"*"* are discussion OF the marker. p124 hit the same wall from the
other side — its headline of 94 marked rows differed from a raw `grep`'s 102 by exactly these
lines. The cue's own position now decides: inside backticks or a quotation it is apparatus. 🔵 **The
test keeps the boundary case separate because it is a judgement rather than a rule**: *"The stale
cell's value was **Apache-2.0**"* is apparatus prose *and* a retraction in its own voice, and it
is marked.

## 🟢 `ACTION AG` — the standing check, and three further instances of its own class

The clause: *refuted if the check does not independently reproduce all four known instances.* It
reproduces all four, each driven through the **naive pattern that actually produced the defect**,
because a gate that can only judge its own matches cannot be shown to catch anything:

| instance | pass | naive read | gate's label |
|---|---|---|---|
| GPL-2.0's preamble names the Lesser GPL — *"(Some other Free Software Foundation software is covered by the GNU Lesser General Public License instead.)"* | p122 | `LGPL` | 🟢 `PREAMBLE` |
| EPL-2.0's secondary-licence clause names GPL-2.0 | p123 | `GPL-2.0` | 🟢 `SECONDARY` |
| CC 4.0's own boilerplate names CC0 | p124 | `CC0-1.0` | 🟢 `DOCUMENT-TEXT` |
| `CC BY` matches **inside** `CC BY-SA 4.0` | p124 | a second licence → a split grant | 🟢 `SUBSTRING` |

🔴 **p124's description of its own third instance is wrong, and a gate built to that description
finds nothing.** p124 called it *"the CC 4.0 legalcode **recommends** CC0 in its own
boilerplate"*. The sentence in the file reads *"The text of the Creative Commons public licenses
is dedicated to the public domain under the CC0 Public Domain Dedication."* That is a real grant
with a real verb — and its **subject is the licence document, not the licensed material**. The
label is `DOCUMENT-TEXT`, not `RECOMMENDATION`, and the distinction is the whole content of the
check: the question is never *"is there a verb?"* but *"what does the verb govern?"*

🔴 **Three further instances, none of them hypothesised, all found by the gate's own controls:**

| # | instance | consequence before the gate |
|---|---|---|
| 5 | 🔴 **`MIT` matches inside `LIMITED`, and `ISC` inside `DISCLAIMED`** | **every BSD-3 and Apache-2.0 warranty disclaimer on earth** yields a spurious `MIT` grant. The `SUBSTRING` check could not see it — it compares a span against other LICENCE tokens, and `LIMITED` is not one. 🔴 **This was p125's own first build: the fifth instance of the class, committed inside the module written to prevent it** |
| 6 | AGPL-3's **section 13** is a compatibility grant over a work being *combined* with this one — *"permission to link or combine any covered work with a work licensed under version 3 of the GNU General Public License"* | one AGPL-3 file yielded **five** spurious `GPL` grants, enough to make every AGPL-3.0 repository in the corpus read as dual-licensed |
| 7 | AGPL-3's preamble spends a paragraph on the **historical Affero GPL** to say this is *not* it — *"This is a different license, not a version of the Affero GPL"* | two more spurious `GPL` grants from the same file |
| 8 | `ankitects/anki`: *"without the need to license your work under an **AGPL3-compatible license**"* | a compatibility **class** read as a grant (found by `ACTION AH`, below) |

🟢 **The controls assert an EXACT grant set, not non-emptiness** — p124's `ACTION AE` established
that a model scored only where it cannot fail scores perfectly and means nothing, and a control
that only asks *"did it find anything?"* is that same mistake in a test.

## 🟢 `ACTION AH` — `ankitects/anki` is six licences, not two

p124 published [`ankitects/anki`](https://github.com/ankitects/anki) as `AGPL-3.0 + CC-BY-SA` and
recorded the set as **partial**: the per-file exceptions sit in a bulleted list no single binding
window spans. The clause: *refuted if fewer than 3 further tokens are recovered.* **Four are.**

🟢 **A list distributes one introducing sentence over many items, so a binding is assembled from
three levels rather than matched in one window** — the grant verb from *"The following included
source code items use a license other than AGPL3:"*, the directory from *"In the qt folder:"*, and
the artifact and licence from the bullet itself.

| scope | token | read from |
|---|---|---|
| *(whole repository)* | `AGPL-3.0` | *"Anki is licensed under the GNU Affero General Public License, version 3 or later"* |
| contributed portions | 🆕 **`BSD-3-Clause`** | *"with portions contributed by Anki users licensed under the BSD-3 license (see CONTRIBUTORS)"* |
| `pylib/statsbg.py` | 🆕 **`CC-BY-4.0`** | ` * statsbg.py: CC BY 4.0.` |
| `qt/mpv.py`, `qt/winpaths.py`, `qt/jQuery and jQuery-UI`, `qt/plot.js` | 🆕 **`MIT`** | four bullets |
| `qt/MathJax` | 🆕 **`Apache-2.0`** | ` * MathJax: Apache 2.` |
| `qt/protobuf.js` | `BSD-3-Clause` | ` * protobuf.js: BSD 3 clause` — **no trailing period** |
| `docs-site/` | `CC-BY-SA-4.0` | the file's last paragraph |

🔵 **Three things the list names that are NOT grants over this tree**, and the gate discards each:
*"Binary distributions also include copies of Qt translation files **(LGPL)**"* → `OUT-OF-TREE`;
*"an **AGPL3-compatible** license"* → `SECONDARY`; and *"Anki's translations are **a mix of** BSD
and public domain"* → no single grant for the item, so no binding. 🟢 **`jQuery-UI` is not split at
its own hyphen** — the item separator is a colon or a spaced dash, which cost one fixture to learn.

## 🔴 `ACTION AI` — REFUTED, and the refutation is the useful result

The clause: *refuted if [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti)
is the only such address in the corpus.* **It is.** All **86** non-standard-default addresses were
probed on their real default branch and on `main` and `master` as a guessing probe would request
them — **258 probes, 79 real-branch grants**, independently reproducing p124's 79 to the row.

| verdict | n | what it means for a studio |
|---|---|---|
| `AGREE` | **77** | `raw.githubusercontent.com` keeps serving a `main`/`master` that still exists, so guessing usually returns the same bytes |
| `BOTH-ABSENT` | 7 | no grant on any of the three branches |
| 🔴 **`FALSE-PERMISSIVE`** | 🔴 **1** | [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti): `develop` is **`GPL-2.0`** (18 264 B), `master` is 🟢 **`MIT`** (1 067 B) |
| `GUESS-MISSES-GRANT` | 1 | [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks): `dev` is `GPL-3.0`, `main` and `master` both 404 |
| `GUESS-INVENTS-GRANT` | 🟢 **0** | no address where a guess asserts a licence the real default does not grant |

🟢 **p125 separates p124's two failures by DIRECTION, and only one of them costs money.**
`pressbooks` returns nothing where there is something — that costs a shortlist. `learnosity-qti`
returns **permissive** for a **copyleft** repository — that costs a licence breach. So
`MAIN-ONLY`'s false-permissive rate is **1 of 79 = 1.3 %** where it can err and **1.2 %** across
the 86, not p124's 2.5 %, which counted both directions as one failure mode.

🔵 **The hypothesis behind the clause was that p124's gold set hid the worst case by requiring a
grant on the real default — and that is refuted too.** The 7 excluded addresses were probed on
14 paths × 3 branches: not one has a `main`/`master` grant over a grant-less default.

🟢 **But two of the 7 are not grant-less at all, and that is a real finding about the
instrument rather than about the shelf.**

| address | the 21-path list requests | the grant actually is |
|---|---|---|
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | no `LICENSE.GPL`, no `LICENSE.MPL` | 🟡 **dual `GPL-3.0` (35 142 B) + `MPL-2.0` (15 921 B)** on default branch `integration` |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | no `readme.txt` | 🔴 **`GPL-3.0`**, declared in the WordPress plugin header |

🔴 **So "no grant file at 22 probed paths" is a statement about the path list, and p123's
`ACTION Y` built a 'genuinely absent' census on it.** 🟢 **Both repositories' real licences were
already correctly recorded on these pages** — the pages are more precise than the census auditing
them, which is `P122-H` for the fourth consecutive pass. The genuinely grant-less set is **5**,
not 7, and `P125-A` defect 3 is the same blindness reaching a live tier table.

🔵 **`compose/code/p125-retraction-cue/false_permissive.sh`, `scope_gate.py`, `bullet_bindings.py` and `mark_forms.py` carry the method; `out/ai-verdict.tsv` and `out/ac-{baseline,after}.triples` carry the evidence.**

**Pass 124, 2026-10-11.** ⏱️ **Eleventh pass of this date** (census window **10:0x → 11:3x UTC**).

🟢 **Instrument: `compose/code/p124-correction-form-marker/` — `ACTION AA`, `AB`, `AC`, `AD`, `AE`
all five discharged, none refuted. `test_p124.sh` **50 passed / 0 failed**, fully offline.**

Corpus re-derived from scratch this pass: **1 370** folded addresses off the ten live pages,
**1 344 EXISTS / 26 ABSENT**, **1 135** grant files read from each repository's REAL default
branch. 🟢 **p123 counted 1 365 addresses and 84 non-standard default branches; p124's independent
re-derivation gives 1 370 and 86 — agreement to 0.4 % and 2 % on two figures nobody carried.**

## 🟢 🆕 `P124-AD` — the `CC` bucket is resolved, and 15 of its 41 rows forbid a commercial deliverable

p123 left **41** readable grants in a bare `CC` bucket and said why it mattered: in education the
asset under a CC grant is the curriculum, the item bank or the knowledge graph — the deliverable
itself. 🟢 **All 41 now resolve to a version.**

| token | rows | may Globant ship a commercial derivative? |
|---|---|---|
| `CC-BY-NC-SA-4.0` | **13** | 🔴 **no** |
| `CC0-1.0` | 11 | 🟢 yes — public-domain dedication, no attribution duty |
| `CC-BY-4.0` | 7 | 🟢 yes, with attribution |
| `CC-BY-SA-4.0` | 6 | 🟡 yes, but the derivative inherits ShareAlike |
| `CC-BY-SA-3.0` | 2 | 🟡 as above, older licence text |
| `CC-BY-NC-ND-4.0` | 1 | 🔴 **no, and no derivatives at all** |
| `CC-BY-NC-4.0` | 1 | 🔴 **no** |

🔴 **15 of 41 — 37 % of the CC bucket — cannot be used commercially, and until this pass all 41
read as the same token.** 🟢 **16 further candidates were correctly rejected as `NOT-CC`:**
`GPL-UNTITLED` rows such as [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) and
[`r-dcm/measr`](https://github.com/r-dcm/measr) that mention Creative Commons without being
licensed under it.

🔴 **The resolution order had to be TITLE LINE FIRST, and the reason is the pass's sharpest
lesson.** The first build scanned the whole text for its element set and returned **`CC0-1.0` for
9 of 13 rows**, including [`openstax/osbooks-college-physics-bundle`](https://github.com/openstax/osbooks-college-physics-bundle),
whose first line reads `Attribution-NonCommercial-ShareAlike 4.0 International`. The cause is not
a typo: **the CC 4.0 legalcode body recommends the `CC0 Public Domain Dedication` in its own
"Considerations for licensors" boilerplate**, so every CC-BY file on earth contains that string,
and a whole-text scan reads all of them as CC0 — the single most permissive answer for the single
most restrictive licence. 🔵 **Two further refinements came from real files: the CC0 legalcode puts
`CC0 1.0 Universal` on its SECOND line under a `Creative Commons Legal Code` document header, and
[`azure/moodle`](https://github.com/azure/moodle)'s `LICENSE-DOCS` is served with a UTF-8 BOM that
hides the title from a naive first-line read.**

## 🟢 🆕 `P124-AE` — `MAIN-ONLY` scored where it CAN fail, and one foundation inverts commercially

p123 measured the branch-guessing `MAIN-ONLY` model at **0 % error** and noted in the same breath
that its gold set could not see the defect: every gold row's default branch *was* `main` or
`master`. 🔴 **A model scored only where it cannot fail scores perfectly and means nothing.**

`ACTION AE` built the complement — **79 gold rows**, each an address whose real default branch is
neither `main` nor `master` and which carries a readable grant there. `MAIN-ONLY` gets **77 right
and 2 wrong.**

| address | real default | the grant there | what guessing returns |
|---|---|---|---|
| [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti) | `develop` | 🔴 **GPL-2.0** · 18 264 B | 🟢 **MIT** from `master` · 1 067 B |
| [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks) | `dev` | 🔴 GPL-3.0 · `LICENSE.md` | 🔴 **nothing** — `main` and `master` both 404 |

🟢 **The 77 agreements are a real result, not a let-off:** `raw.githubusercontent.com` keeps
serving a `master`/`main` branch that still exists even after the repository's *default* has moved
on, so guessing usually returns the same bytes. 🔴 **`learnosity-qti` is where usually fails, and
it fails in the expensive direction.** Both files were fetched and read: `master/LICENSE` is the
MIT text, `develop/LICENSE` is GPL-2.0 verbatim. **A branch-guessing probe hands a studio the
PERMISSIVE answer for a repository whose current default branch is COPYLEFT.** 🟢 **This shelf
publishes `GPL-2.0` on `develop` at `repos/trending.md:3720` and is correct — the defect is in the
model, not the shelf.**

🔵 **So `MAIN-ONLY`'s error rate is 2.5 % where it can err, 0.15 % across the 1 344-address
corpus, and 0 % on the set p123 scored it against — three true numbers of which only the first is
useful.** The 86 non-standard defaults span **39 distinct branch names**, and the convention
belongs to exactly the platforms this KB exists to place: release lines
(`openeducat/openeducat_erp` `19.0`, `claroline/claroline` `15.0`, `ILIAS-eLearning/ILIAS`
`release_11`, `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` `v6.2.0`, `GibbonEdu/core` `v31.0.00`),
gitflow (`frappe/*`, `oppia/*`, `oat-sa/tao-core`, `opencast/opencast`, `1EdTech/*` on `develop`),
and `trunk` (`apache/ofbiz-framework`, `gocodebox/lifterlms`).

## 🟢 🆕 `P124-AB` — this page's correction records are now machine-readable

**14** marked rows on this page, up from 11. `ACTION AB` extended p123's marker from the inline
`⚠️ **was X**` span to the audit-table OLD column and to prose retractions — **42 rows across 5
files, 52 → 94 marked rows corpus-wide.**

🔵 **The figure is 94 ROWS and a raw `grep` for the marker returns 102.** The difference is 8
lines of prose *about* the marker, inside backticks, on these same pages. 🔴 **p122 made exactly
this mistake (its "57 rows" included 6 lines discussing the marker) and p124 very nearly repeated
it in its own headline figure.** Counted here as a marked ROW: a table row carrying the marker, or
a prose line whose `was …` span carries it. 🟢 **Two of this page's rows were correctly NOT
marked, and that is the harder half:** `| moodle/moodle | 🟡 GPL-3 | GPL-3.0 (COPYING.txt) |
🟢 AGREE |` and the `overhangio/tutor` row beside it are **agreements**, not corrections —
`GPL-3` and `GPL-3.0` are the same grant written two ways, and the first build reported both as
defects.

**Pass 123, 2026-10-11.** ⏱️ **Tenth pass of this date** (census window **08:4x → 09:4x UTC**).

🟢 **Instrument: `compose/code/p123-grant-set-calibration/`, discharging `ACTION W, X, Y, Z` and
implementing `ACTION V`. `test_p123.sh` **35 passed / 0 failed**, fully offline.**

🟢 **This page carried 0 live licence defects this pass.** Its **11** repaired rows now carry the
`<!--corrected-->` marker.

### 🟢 🆕 `ACTION Z` — a grant is a SET, and 17 addresses on these shelves prove it matters

Every licence probe in this KB up to p122 stopped at the FIRST grant file that returned 200. p123
reads them all. **17 of 1 096 addresses with a readable grant carry more than one grant file**,
and each is a convention with a different legal meaning from any single arm:

| convention | addresses | why one token is wrong |
|---|---|---|
| R/CRAN: stub `LICENSE`, grant in `DESCRIPTION` | [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck), [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck), [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna), [`sidneybissoli/educabr`](https://github.com/sidneybissoli/educabr), [`cambridgeassessmentresearch/kerneqwps`](https://github.com/cambridgeassessmentresearch/kerneqwps), [`r-dcm/measr`](https://github.com/r-dcm/measr), [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | `LICENSE` alone is a stub or `UNKNOWN` — which reads as *"no grant"*, the worst possible error |
| dual **MIT OR Apache-2.0** | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs), [`contentauth/c2pa-python`](https://github.com/contentauth/c2pa-python) | 🟢 **the licensee chooses.** Reporting one arm removes a right the grant gives |
| code / docs split | [`microsoft/autogen`](https://github.com/microsoft/autogen), [`azure/moodle`](https://github.com/azure/moodle), [`wildcat430524/stepstogreat`](https://github.com/wildcat430524/stepstogreat) | docs under CC, code permissive |
| code / **data** split | [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) | 🔴 `CC-BY-NC-SA` **data** — and in an education KB the data is the asset |
| `COPYING` + `COPYING.LESSER` | [`datacamp/catsim`](https://github.com/datacamp/catsim) | 🟢 the LGPL file is the operative grant; `COPYING` alone over-restricts |

🟢 **20 grants sit on paths no previous probe requested** — `DESCRIPTION` ×13, `LICENSE-CODE` ×2,
`LICENSE-DOCS` ×2, `LICENSE-APACHE` ×2, `COPYING.LESSER` ×1.

### 🔴 🆕 `ACTION Y` — the default branch, not the path, was the bigger blind spot

**84 of 1 327 addresses default to neither `main` nor `master`, and 77 of them hold a readable
grant that a `main`/`master` probe could never reach.** These are not abandoned branches — they
are RELEASE LINES, which is the convention of the platforms this page exists to place:

| address | default branch | grant |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `19.0` | 🔴 LGPL-3.0 |
| [`claroline/claroline`](https://github.com/claroline/claroline) | `15.0` | 🔴 AGPL-3.0 |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | 🔴 GPL-2.0 |
| [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | `7.x` | 🟡 split — GPL-2.0 core + MIT bundled plugins |
| [`eclipse-ee4j/jersey`](https://github.com/eclipse-ee4j/jersey) | `4.x` | 🟡 EPL-2.0 |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `develop` | 🟢 **MIT**, 816★, 12 316 commits |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `develop` | 🟢 **MIT** |
| [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) | `dev` | 🟡 MPL-2.0 |

🔵 **`git ls-remote --symref` answers existence and default branch in one call, so this is now
cheaper than the guessing it replaces, not more expensive.**

### 🟢 🆕 The xAPI / learning-record tier, re-verified repo-by-repo this pass

🟢 **Measured, not inferred** — licence from the live tree, stars and commits from the rendered
page (`P123-D`):

| address | stars | licence | commits | role |
|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **144** | 🟢 **Apache-2.0** | 2 269 | SQL LRS — the deployable learning-record store |
| [`yetanalytics/lrs`](https://github.com/yetanalytics/lrs) | — | 🟢 **Apache-2.0** | — | the conformant-LRS protocol library |
| [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | — | 🟢 **Apache-2.0** | — | statement forwarding governed by xAPI Profiles. 🔴 **Its PRODUCT name is LRSPipe; `yetanalytics/lrspipe` does not exist** — `ACTION Y`'s product-name class |
| [`Apereo-Learning-Analytics-Initiative/Larissa`](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa) | — | 🟢 **Apache-2.0** | — | Apereo's LRS |
| [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) | **243** | 🔴 **AGPL-3.0** | 3 323 | secure automated exercise assessment (UCLouvain, 🇧🇪). 🔴 **network copyleft — integrate, do not embed** |
| [`skolverket/dnp-ss12000-reference-api`](https://github.com/skolverket/dnp-ss12000-reference-api) | 5 | 🟢 **Apache-2.0** | 35 | 🟢 **the value is the STANDARD, not the stars**: Sweden's national agency's SS 12000 SIS reference |
| [`KI-Campus/LRS`](https://github.com/KI-Campus/LRS) | 3 | 🟢 MIT | 212 | 🔴 **ARCHIVED 2026-02-20, read-only** — do not start here |

**Pass 122, 2026-10-11.** ⏱️ **Ninth pass of this date** (census window **07:3x → 08:4x UTC**).

🟢 **Instrument: `compose/code/p122-prose-licence-census/`, discharging `ACTION R, S, T, U` and
closing the five-pass-old `ACTION C` and `ACTION D` as **refuted**. `test_p122.sh`
**50 passed / 0 failed**, fully offline.**

🟢 **This page gains a 13-row EMEA public-sector shelf** that no mandated search has ever
returned — two national education agencies, the European Commission, TU Munich, ETH Zurich,
Oxford and Amsterdam — found by reading package namespaces out of the tree (`ACTION C`).

## 🟢 🆕 `P122-EMEA` — the EMEA public-sector shelf, found by package namespace (`ACTION C`)

**Pass 122, 2026-10-11.** `ACTION C` — carried unattempted for five passes — probed `pom.xml`
`<groupId>` and Gradle `group` across **1 627** folded addresses. **68** declare a namespace;
**13** are placed by it. 🔴 **The action is REFUTED on its own clause (it required ≥ 20).**
🟢 **But all 13 placements are EMEA, and that is the reusable result:** a ccTLD-leading
reverse-DNS namespace (`de.`, `fi.`, `se.`, `ch.`, `nl.`, `uk.ac.`, `eu.`) is a **European
university and public-agency convention**. North American projects use `org.` (37), `com.` (6)
and `edu.` (4), which place nothing. APAC and LATAM: **zero**.

🟢 **Layer P is therefore not a general placement layer — it is an EMEA public-sector detector.**
Five passes of carrying it forward as a general tool is why it never paid off.

| address | namespace | country | licence, measured this pass | what it is |
|---|---|---|---|---|
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | `fi.vm.sade` | 🇫🇮 Finland | 🟢 **EUPL-1.1-or-later** — `master/LICENSE.txt`, 654 B, *"Licensed under the EUPL, Version 1.1 or … subsequent versions"* (README: *"Koski on EUPL-lisensoitu sovellus"*). 🆕 **p123: the grant is by REFERENCE and admits later versions** | the Finnish National Agency for Education's **national study-rights and attainments registry**. A state-run system of record, in the open |
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | `fi.vm.sade.oppijanumerorekisteri` | 🇫🇮 Finland | carried | national **learner-identifier** registry — the join key for every other service |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | `fi.vm.sade.organisaatio` | 🇫🇮 Finland | carried | national **institution** registry |
| [`skolverket/dnp-ss12000-reference-api`](https://github.com/skolverket/dnp-ss12000-reference-api) | `se.skolverket.service.provisioning` | 🇸🇪 Sweden | 🟢 **Apache-2.0**, 5★ | **reference implementation of SS 12000**, Sweden's school-interoperability standard, published by the Swedish National Agency for Education itself |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `de.tum.cit.aet.artemis` | 🇩🇪 Germany | 🟢 **MIT**, 816★ | interactive learning with automated feedback, TU Munich |
| [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) | `de.tum.cit.ase` | 🇩🇪 Germany | carried | Artemis's auto-grading sandbox |
| [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | `de.thm.ii` | 🇩🇪 Germany | 🟢 **Apache-2.0**, 24★ | AI feedback for students, TH Mittelhessen |
| [`jplag/jplag`](https://github.com/jplag/jplag) | `de.jplag` | 🇩🇪 Germany | carried | plagiarism detection |
| [`FWU-DE/fwu-kc-extensions`](https://github.com/FWU-DE/fwu-kc-extensions) | `de.intension` | 🇩🇪 Germany | 🟢 Apache-2.0 | Keycloak extensions behind the German states' school identity layer |
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | `ch.ethz.seb` | 🇨🇭 Switzerland | 🟢 **MPL-2.0** — 16 725 B, title line *"Mozilla Public License Version 2.0"* | exam-lockdown server, ETH Zurich |
| [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | `uk.ac.ox.ctl` | 🇬🇧 United Kingdom | carried | LTI 1.3 for Spring Security, University of Oxford |
| [`apereo-learning-analytics-initiative/Larissa`](https://github.com/apereo-learning-analytics-initiative/Larissa) | `nl.uva` | 🇳🇱 Netherlands | carried | learning analytics, University of Amsterdam |
| [`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials) | `eu.europa.ec.empl.edci` | 🇪🇺 EU | carried | the EU's own digital-credentials stack (EDCI) |

🟢 **`SafeExamBrowser/seb-server` is MPL-2.0 and this page already said so.** This pass's first
classifier read it as AGPL-3.0 because **MPL-2.0 names the GPL and AGPL in its secondary-licence
section**. The page was right; the instrument was wrong. Fixture:
`fixtures/mpl2-secondary-names-gpl.txt`.

🔵 **Why this matters for an EMEA engagement.** p121 recorded EMEA as a *measured absence* on the
demand side, and that still holds. This is the **supply** side, and it is unusually strong: two
national agencies (Finland, Sweden) publish their systems of record as open source, the EU
publishes its credentials stack, and SS 12000 gives a public standard to integrate against. An
EMEA proposal can cite named, licence-verified, state-maintained code rather than vendor claims.

## 🟢 🆕 `P121-N` — the foundations shelf is 98 % granted, and last pass's headline said 59 %

🔴 **p120 published *"41 % of audited addresses cannot be built on"*.** `ACTION N` pre-registered
the test that would confirm or refute it across the rest of the census. **It refutes it.**

| | addresses | ungranted | rate |
|---|---|---|---|
| p120's sample — **selected for being `UNREAD`** | 22 | 9 | 🔴 41 % |
| 🟢 **`ACTION N` — the other 227** | 227 | 🟢 **4** | 🟢 **1.8 %** |
| whole census | 249 | 13 | 🟢 **5.2 %** |

🟢 **For a studio choosing substrate this is the number that matters, and it is good news:
roughly 19 of every 20 addresses on this shelf carry a readable grant.** 🔵 **p120's figure was
not wrong — it was an answer to a different question**, and this KB published it as though it
described the shelf. A failure rate measured on the addresses chosen for being hardest is a
property of the choosing, not of the population.

## 🔴 🆕 `P121-N2` — `atutor/ATutor` is published here as GPL-3 and its repository says only "GPL"

🔴 **[`atutor/ATutor`](https://github.com/atutor/ATutor) (180★) has no licence file at 22 probed
paths on `master`.** Its README's `## License` section contains one word: **`GPL`**.

🔴 **"GPL" is not a licence.** GPL-2.0 and GPL-3.0 are mutually incompatible — a component under
one cannot be combined with a component under the other. A bare family name chooses neither, so
there is nothing for a compliance review to act on.

🟡 **This page is partly right about it already** — a row reads *"genuinely commits no licence file"*
and `verticals/solutions.md` carries a ‡ footnote saying *"the grant is asserted by this KB's
history rather than by the repository … treat the row as licence-unresolved"*. 🟢 **That footnote
stands and this pass confirms it by measurement.** 🔴 **What it does not say is that the
version — `GPL-3` — is this KB's invention.** The repository never names a version. For an
accessibility-pioneer LMS last released 2023-02-12, the honest cell is *"author claims GPL, no
version, no file"*.

## 🟢 `douglasrizzo/catsim` repaired — 🟢 MIT here, BSD-3-Clause in the tree

🔴 **This page's star table published [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim)
(153★) as 🟢 MIT.** Measured this pass: `dev/LICENSE`, 1 514 B, **BSD 3-Clause**. Its
`pyproject.toml` also declares `BSD-3-Clause`, so **three channels agreed and the page disagreed
with all three.** 🟢 **Repaired.**

🔵 **Both are permissive, so nothing is legally exposed** — but `catsim` is the shelf's adaptive-testing
(IRT/CAT) foundation, the component an assessment engagement builds on, and BSD-3 carries a
non-endorsement clause MIT does not.

## 🟢 The foundational shelf, measured

🔵 **Licences below were read from the default branch; the `⚠️ was` marker means this pass or a
prior one corrected the cell.**

| address | ★ | 🟢 licence, measured | region | why it is foundational |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 6.2k | 🔴 GPL-3.0 — `COPYING.txt` | Global (AU origin) | the largest-install LMS on earth; integrate, do not absorb |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 7.5k | 🔴 **AGPL-3.0** ⚠️ *was GPL*<!--corrected--> | North America | the MOOC platform of record; AGPL reaches hosted services |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 5.8k | 🔴 **AGPL-3.0** ⚠️ *was GPL*<!--corrected--> | North America | the HiEd LMS with the largest US market share |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1.1k | 🟢 **MIT** | Global (offline-first) | the only permissive LMS at scale — the low-bandwidth answer |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 8.1k | 🟢 BSD-3 | Global | multi-user notebook serving; the CS-teaching substrate |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 1.3k | 🟢 BSD-3 | North America | notebook autograding; pairs with JupyterHub |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 800 | 🟢 BSD-3 | North America (RPI) | programming-assignment autograder with plagiarism detection |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | — | 🟢 BSD-3 | North America (UC Berkeley) | Python/R autograding, container-isolated |
| [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 153 | 🟢 **BSD-3-Clause** ⚠️ **was 🟢 MIT**<!--corrected--> | LATAM (BR) | computerised adaptive testing — **repaired this pass** |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 1.5k | 🟢 MIT | North America | Bayesian Knowledge Tracing intelligent tutor |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | — | 🟢 Apache-2.0 | Global | 🔵 **cite the VALIDATOR** — the *specification* repo carries no grant (`P120-J`) |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 1.1k | 🟢 BSD-3 | Global | institutional repository of record |

🔵 **The shape has not changed in eight passes and remains the single most useful fact here: the
permissive tier is the plumbing — grading, assessment, notebooks, repositories, badges — while
every large-install LMS is copyleft.** A studio builds permissive tooling *around* a copyleft
platform at a service boundary; it does not fork the platform.

## 🟡 `ACTION Q` — a manifest is weak evidence, but not as weak as p120 said

🔴 **p120: 2 of 4 manifests contradict the committed licence (50 %).** `ACTION Q` read all 249
addresses: **161 manifests fetched, 104 declare a licence, 10 contradict — 9.6 %.** The clause
required **≥ 15 %**, so 🔴 **`ACTION Q` is REFUTED.**

🟢 **The direction survives and is sharper than the rate.** 7 of the 10 are
permissive-over-restrictive — the dangerous way round, because a dependency scanner reads the
manifest and returns the permissive answer. Details and the full table are in
`repos/trending.md` and `intel/trends.md`.

# Education — foundational repos

**Pass 120, 2026-10-11.** ⏱️ **Seventh pass of this date** (census window **05:3x → 06:2x UTC**).

🟢 **Instrument: `compose/code/p120-unread-grant-resolution/`, discharging `ACTIONS J, K, L`.
`test_p120.sh` **55 passed / 0 failed**, fully offline. This page's own `leemons` row — p119's
€100 000 finding — is **independently reproduced** by this pass's classifier as a control, and
this page carried **1** of the 7 cells repaired in this commit.**

## 🔴 🆕 `P120-J` — the foundations shelf's most-cited standards repo grants nothing at all

🔴 **[`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification)
(205★) was 🟢 Apache-2.0<!--corrected--> on this page. It carries no licence file at any of 22 probed paths on
its default branch `develop`, and its README names no licence.**

🔵 **This page was already half-right about it**: a row further down reads *"The specification
carries no grant while the validator is Apache-2.0. Cite the validator."* 🟢 **That row stands
and p120 confirms it by measurement.** The defect was the row that still carried the green token,
and in `compose/patterns.md` the same address was tokened 🟢 **inside a recommendation** — the
exact shape `P119-PAT-0` pre-registered.

🔴 **For a consultancy the distinction is operational, not academic.** Open Badges 3.0 is the
credentialing standard a client asks for by name. The *specification text* is governed by
1EdTech's own membership IPR terms, not by an OSI licence in the repository; what is Apache-2.0
is the **validator**. A build that vendors the spec repo has vendored an ungranted artefact; a
build that depends on the validator has a grant. 🟢 **Cite the validator.**

## 🔴 🆕 `P120-K` — a repaired row LEAVES this KB's census, and five of them already have

p118's claim-side alternation can only express OSI licences. 🔴 **So the moment a pass repairs a
row on this page to *"Fair Code License v1.0"*, that row stops matching and becomes invisible to
the instrument that repaired it.**

`ACTION K` extended the alternation with the source-available family. **22 claim rows across 6
pages reappeared**, 5 of them on this page:

| address | token that was invisible | rows on this page |
|---|---|---|
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `Elastic-2.0` | 4 |
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | `Fair Code License` | 1 |

🔴 **A repaired row that vanishes is worse than a wrong one.** The page is right and nothing can
see it any more, so nothing will notice when it next goes stale — and `leemons` is the row where
going unnoticed costs €100 000.

🟡 **`ACTION K`'s own clause is not the measurement that matters.** It said *"refuted if the
residual `WRONG` count does not fall below 19"*, which measures a re-run of the full `ACTION E`
sweep that this pass did not run. Recorded as discharged **on its mechanism only**, with the
clause left unmet rather than quietly reinterpreted.

## 🟢 🆕 `P120-F` — `leemons` reproduced from scratch, as a control on the instrument

🟢 **p119 found the €100 000 Fair Code licence by hand. p120's classifier finds it
independently**, through a branch that matches restriction *semantics* rather than licence
*names* — and finds a second address of the same shape that p119 did not reach
([`yuanjiusheng/cloud-learning-ce`](https://github.com/yuanjiusheng/cloud-learning-ce), see
`verticals/solutions.md`).

| control | p119 found, by hand | p120 measured, by instrument | agrees |
|---|---|---|---|
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | Fair Code v1.0, €100k + 5 % | 🔴 **proprietary, 3 restriction signals** | 🟢 yes |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | MIT code · 🔴 CC BY-NC-SA corpora | 🔴 **NonCommercial tier, MIT + CC BY 4.0 + CC BY-NC-SA 4.0** | 🟢 yes |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | multi-grant framework | 🟢 **MIT + CC0 + CC BY 4.0** | 🟢 yes |
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | split, MIT for code | 🟢 **`LICENSE-CODIGO.md`=MIT + `LICENSE-DADOS.md`=CC BY** | 🟢 yes |

🔵 **4 of 4 reproduced.** An instrument that re-derives a previous pass's hand-read answers is
worth more than one that only finds new things, because it is the only evidence that the new
things are not artefacts. 🟡 **One gap, stated: p119 also recorded that `knowledge-graph` has
*"Open + Gated" and "Gated" tiers covered by no open licence at all.* p120's prose-index tier
reads licence NAMES and does not detect an unlicensed tier, so it under-reports that row.**

## 🟢 🆕 `P120-R` — five permissive grading repos, confirmed and safe to vendor

🟢 **The one unambiguously good outcome of this pass.** Five R-ecosystem autograders were
published here as MIT/BSD, measured `UNREAD` by p118 because they commit a 45-byte CRAN stub as
`LICENSE`, and are now confirmed from `LICENSE.md` + `DESCRIPTION`:

| address | ★ | grant | what it does |
|---|---|---|---|
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 23 | 🟢 **MIT** | inspects `ggplot2` plots for automated grading |
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | 15 | 🟢 **MIT** | downloads and processes Brazilian INEP education microdata (Censo Escolar, ENEM) |
| [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 13 | 🟢 **MIT** | Transition Network Analysis for learning-analytics sequences |
| [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) | 9 | 🟢 **MIT** | grading checks for tabular data |
| [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 3 | 🟢 **BSD-3** | autograder for R scripts, Rmd and Jupyter R kernels (UC Berkeley) |

🟢 **[`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard)
(46★) is confirmed Apache-2.0** — read from its default branch, which is the **tag `v6.2.0`**,
not a branch. 🔵 A probe assuming `main` would have 404'd and fed the `UNREAD` pile; p118's
default-branch measurement is what made this row readable at all.

## 🔴 🆕 `P119-A` — the foundations shelf published a €100 000 licence as 🟢 Apache-2.0

🔴 **[`leemonade/leemons`](https://github.com/leemonade/leemons) was row-level 🟢 Apache-2.0<!--corrected--> on
this page. Its root `LICENSE.md` (10 830 B) is a "Fair Code License" v1.0 built on the
Sustainable Use License, and contains ZERO occurrences of the word "apache".** What it actually
says, read from the file:

| clause | text, as committed |
|---|---|
| scope of use | *"may only be used or copied to facilitate the management of educational services offered by the User"* — any other use needs prior written authorization |
| redistribution | *"only ... if done so free of charge and for non-commercial purposes"* |
| 🔴 fee trigger | **ONE HUNDRED THOUSAND EURO** once the platform passes **1 000 users or profiles**, *or* €1 M annual revenue from it |
| 🔴 royalty | **5 %** after the first year of use |
| sublicensing | forbidden without prior written authorization |

🔴 **For a consultancy this is the worst possible shape of error.** Any education deployment
Globant would be hired to build crosses 1 000 users on day one, and the KB's own shelf said the
licence was permissive. Repaired here and in `compose/patterns.md`.

## 🔴 🆕 `P119-A2` — and p118's 957-claim sweep could not have caught it, by design

This is the mechanism, and it is the pass's most transferable finding:

1. `leemons`' grant is a prose index, so p118's classifier measured it **`UNKNOWN`**.
2. `UNKNOWN` → verdict **`UNREAD`**, which p118's layer *correctly* refuses to fold into `AGREE`:
   *"not contradicted, not corroborated."*
3. `repair.py` is driven by the verdict file, so — also correctly — it **cannot touch an
   unmeasured row**.
4. The stale 🟢 Apache-2.0 therefore survived a whole-KB sweep **because every layer behaved as
   specified**.

🔴 **The dangerous cell is `UNREAD` + a permissive claim, and there are 42 of them across 22
addresses** — **76 %** of p118's 55 `UNREAD` rows claim MIT, Apache-2.0 or BSD against a grant
the sweep could not read.

| address | `UNREAD` rows claiming permissive |
|---|---|
| `bncc-dev/bncc-benchmark` | 8 |
| `learning-commons-org/evaluators` | 4 |
| `ed-fi-alliance-oss/Ed-Fi-Data-Standard` | 4 |
| `FWU-DE/ais-chat` | 3 |
| `yuanjiusheng/cloud-learning-ce`, `sidneybissoli/educabr`, **`leemonade/leemons`**, `kaushal0494/AITutor-EvalKit`, `cezarc/EPESI` | 2 each |
| 12 more addresses | 1 each |

🔵 p118's own `P118-K` wrote the reason down — *absence of a licence reads as permission* — and
applied it to the measurement but not to the verdict. **`ACTION J` is pre-registered to resolve
the remaining 20.**

## 🟢 The foundations shelf — grant, liveness and stars all measured this pass

🔵 **`ARCHIVED` is a new column on this page, and it changes five recommendations.** A repo that
is read-only cannot take a patch or ship a CVE fix; *"stale"* and *"archived"* are different
procurement facts, and this page had a recency column but no liveness column.

| repo | ★ this pass | grant, from the default branch | state |
|---|---|---|---|
| [`ollama/ollama`](https://github.com/ollama/ollama) | **182 679** | 🟢 MIT | 🟢 live — local inference, the offline-first floor |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | **167 342** | 🟢 Apache-2.0 | 🟢 live |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | **61 345** | 🟢 **MIT** (`LICENSE-CODE`) · 🔵 `LICENSE` is CC-BY-4.0 for docs | 🟢 live |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **43 034** | 🟢 MIT | 🟢 live |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | **39 986** | 🔴 GPL-3.0 | 🟢 live, `develop` |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | **23 591** | 🟢 MIT | 🟢 live |
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **15 491** | 🟢 Apache-2.0 | 🟢 live — pronunciation assessment |
| [`frappe/frappe`](https://github.com/frappe/frappe) | **10 913** | 🟢 MIT | 🟢 live, `develop` |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **8 354** | 🟢 BSD-3-Clause | 🟢 live |
| [`MontrealCorpusTools/Montreal-Forced-Aligner`](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | **1 902** | 🟢 MIT | 🟢 live |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **1 374** | 🟢 BSD-3-Clause | 🟢 live |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | **518** | 🟡 AGPL-3.0 core + MIT contributed portions | 🟢 live |
| [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **507** | 🟢 MIT | 🟢 live — spaced repetition |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **443** | 🟢 MIT | 🟢 live — **repaired, 3 cells carried `~430`** |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **283** | 🟢 MIT | 🟢 live — knowledge tracing |
| [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **153** | 🟢 **BSD-3-Clause** ⚠️ **was 🟢 MIT**<!--corrected--> | 🟢 live, `dev` — adaptive testing |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **144** | 🟢 Apache-2.0 | 🟢 live — the xAPI record store |
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **42** | 🟢 Apache-2.0 | 🔴 **ARCHIVED — treat as a frozen SPEC to implement, never a dependency that will take a fix** |

🔵 **Eighteen foundational repos, every star count and grant measured this pass, and the three
rows that would have been recommendations on dead upstreams now say so.**

## 🟢 🆕 `P119-G` — p118's `P118-C` cross-validated on a second, independent channel

p118 read all 249 default branches over the **git transport**. p119 read them over the **search
API**. 🟢 **26 addresses are comparable across both captures and they agree 26 / 26** — including
every one of p118's awkward cases: `frappe/*` → `develop`, `Elgg/Elgg` → `7.x`,
`claroline/Claroline` → `15.0`, `openeducat/openeducat_erp` → `19.0`,
`ILIAS-eLearning/ILIAS` → `release_11`, `overhangio/tutor` → `release`,
`gocodebox/lifterlms` → `trunk`, `francoisjacquet/rosariosis` → `mobile`.

🔵 **`P118-C` is confirmed, not merely unrefuted** — which matters because every licence and
recency figure on this page is read from a branch, so reading the wrong branch is not a near-miss
but a different repository state.


**Pass 118, 2026-10-11.** ⏱️ **Fifth pass of this date** (census window **03:4x → 04:2x UTC**).

🟢 **Instrument: `compose/code/p118-licence-column-sweep/`, discharging `ACTION E`. This page
carried **7** of the 38 wrong licence cells the sweep found; all are repaired in this commit.**

## 🟢 🆕 `P118-C` — 37 of 249 addresses default to neither `main` nor `master`

🔴 **14.9 %, and five of them default to a TAG-SHAPED ref that no `main`/`master`/`develop`
probe reaches at all.** Every foundation row's licence and recency is read from a branch, so
reading the wrong branch is not a near-miss — it is a different repository state.

| address | default branch | why it matters here |
|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | `develop` | 🔴 `master` carries an **MIT** `LICENSE`; `develop` is what ships |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `v31.0.00` | tag-shaped; unreachable by branch probe |
| [`claroline/Claroline`](https://github.com/claroline/Claroline) | `15.0` | tag-shaped |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | `19.0` | tag-shaped, tracks the Odoo major |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | tag-shaped; LATAM (BR) |
| [`ed-fi-alliance-oss/Ed-Fi-Data-Standard`](https://github.com/ed-fi-alliance-oss/Ed-Fi-Data-Standard) | `v6.2.0` | tag-shaped |
| [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | `7.x` | 🔵 canonical spelling is `Elgg/Elgg`; `elgg/elgg` is a case variant of the same repo |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | `trunk` | |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | `release` | |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `mobile` | 🔵 a *default* branch named `mobile` |
| `oppia/oppia`, `learningequality/kolibri`, `opencast/opencast`, `oat-sa/tao-core`, `ls1intum/Artemis`, `1EdTech/*`, `frappe/*`, `LearnPress/learnpress`, `pressbooks/pressbooks` (+ others) | `develop` / `dev` | 22 further addresses |

🟢 **`P118-B`: the default branch was read with `git ls-remote --symref HEAD` — 249 / 249, no
session scope needed — while BOTH REST endpoints were gated to `curl` and `gh api` (`P118-A`).
For the one field this sweep could not proceed without, the oldest transport was the only
ungated one.**

## 🟢 The foundations shelf — licence measured from the default branch

| repo | default branch | licence file | grant, from the tree | class |
|---|---|---|---|---|
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | `main` | `LICENSE` | 🟢 Apache-2.0 | permissive |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | `main` | `LICENSE` | 🟢 Apache-2.0 | permissive |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `master` | `LICENSE` | 🟢 Apache-2.0 | permissive — 🟢 **the only large LMS in this KB a client can ship closed** |
| [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | `main` | `LICENSE` | 🟢 BSD | permissive |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `develop` | `LICENSE` | 🟢 MIT | permissive — offline-first, the LATAM//APAC low-connectivity base |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `develop` | `LICENSE` | 🟢 Apache-2.0 | permissive |
| [`frappe/frappe`](https://github.com/frappe/frappe) | `develop` | `LICENSE` | 🟢 **MIT** ⚠️ **was GPL-3.0**<!--corrected--> | permissive — see `P118-G` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `master` | `LICENSE` | 🟡 **ECL-2.0 + Apache-2.0** | multi-grant, both permissive |
| [`opencast/opencast`](https://github.com/opencast/opencast) | `develop` | `LICENSE` | 🟡 **ECL-2.0 + Apache-2.0** | multi-grant, both permissive |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | **`COPYING.txt`** | 🔴 **GPL-3.0** ⚠️ **was "no licence file at all"**<!--corrected--> | see `P118-N` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master` | `LICENSE` | 🔴 AGPL-3.0 | network copyleft |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | `master` | `LICENSE` | 🔴 **AGPL-3.0** ⚠️ **was Apache-2.0**<!--corrected--> | network copyleft |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | `release` | `LICENSE.txt` | 🔴 AGPL-3.0 | network copyleft |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `master` | `LICENSE` | 🔴 AGPL-3.0 | network copyleft |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `develop` | `license.txt` | 🔴 GPL-3.0 | distribution copyleft |
| [`frappe/lms`](https://github.com/frappe/lms) | `develop` | `license.txt` | 🔴 **AGPL-3.0** ⚠️ **was GPL**<!--corrected--> | network copyleft |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | `master` | `LICENSE` | 🔴 **AGPL-3.0 (CE) + MIT (portions) + proprietary `ee/`** | see `P118-J` |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `main` | `LICENSE` | 🔴 **Elastic-2.0 — NOT open source** ⚠️ **was AGPL-3**<!--corrected--> | see `P118-I` |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | `LICENSE` | 🔴 **GPL-2.0** ⚠️ **was LGPL-3.0**<!--corrected--> | 🔴 LGPL permits linking without copyleft reaching your code; **GPL-2.0 does not** |
| [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | `1.6` | `LICENSE` | 🔴 **AGPL-3.0** ⚠️ **was unread**<!--corrected--> | 🔵 the AGPL-3 **in Portuguese** — see `P118-K` |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | `main` | `LICENSE` | 🟢 **CC0-1.0** ⚠️ **was MIT**<!--corrected--> | public-domain dedication, no code |
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck), [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck), [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr), [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna), [`sidneybissoli/educabr`](https://github.com/sidneybissoli/educabr) | various | `LICENSE` | 🔵 **`GRANT-IN-MANIFEST`** | 45–108 B field stub; the licence is named in `DESCRIPTION`, not in the licence file |
| [`frappe/education`](https://github.com/frappe/education) | `develop` | `license.txt` | 🔵 **`GRANT-BY-REFERENCE`** | one line: `License: GNU GPL V3`. No body, no terms, no holder |

🟢 **22 foundations with a readable grant are listed above; 230 of the KB's 249 addresses
(92.4 %) now have one.** 🔵 **The permissive tier of the LMS layer is thin and it is worth
naming precisely: `OpenOLAT` (Apache-2.0), `Sakai` and `Opencast` (ECL-2.0, Apache-derived),
`Kolibri` (MIT), `Oppia` (Apache-2.0), `DSpace` (BSD), `frappe/frappe` (MIT). The five largest
LMS platforms by install base are all copyleft.**

## 🔴 🆕 `P118-N` — Moodle does commit a licence, and the KB said it did not

p117's `Gap 409` recorded three rows that *"commit no licence file at all"*, and
`moodle/moodle` was one of them. 🔴 **Moodle commits `COPYING.txt` — the GPL-3.0, on `main`.**
p117's candidate list was `LICENSE LICENSE.txt LICENSE.md LICENCE COPYING LICENSE-MIT`; the file
is `COPYING.txt`, one extension away from a name it was already trying.

🔵 **The world's most-installed LMS was published in this KB as unlicensed.** The remaining
`Gap 409` claims survive re-measurement: `atutor/ATutor` genuinely commits no licence file on
`master`, and 13 further addresses commit none. 🟡 **"No licence file" is the most dangerous
cell this KB can print, because absence reads as permission — so it now requires 9 filename
candidates across the default branch before it may be written.**

## 🔵 🆕 `P118-F` — every byte figure p117 published is short by one

p117 measured file sizes inside a command substitution, which strips trailing newlines before
`wc -c` sees them. Confirmed 3 / 3, including the discriminating case: the single file whose
published size matches its on-disk size is the single file that does not end in a newline
(`openedx/edx-ora2`, 35 135 B). p117 also declared, as its own fault, that it had *inferred
licence identity from file size*. 🔵 The sizes it was inferring from were systematically off by
one — which is harmless for identity at kilobyte granularity and is recorded because p117 asked
for exactly this kind of check on its own numbers.

**Pass 117, 2026-10-11.** ⏱️ **Fourth pass of this date** (census window **02:45 → 03:0x UTC**).

🟢 **Instrument: `compose/code/p117-second-channel/`. The GitHub API answers this session
through the MCP relay while `curl` still gets `403` at the CONNECT layer and `gh api` is
repo-scope gated (`P117-A`) — so star counts, archive state and canonical names are
authoritative here for the first time, and every licence below was re-read from the TREE.**

## 🔴 🆕 `P117-D` — one of the nine `checked` foundations has had the WRONG LICENCE for two passes

| row | published p114 / p115 / 🆕 **p116** | 🔴 tree, p117 | published p93–p112 |
|---|---|---|---|
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟢 Apache-2.0 ×3<!--corrected-->| 🔴 **AGPL-3.0** | 🟢 **AGPL-3 — correct** |

🔴 **It is now THREE passes, not two, and the third happened while this pass was measuring it.**
The independent `p116-lock-agreement` run pushed to `origin/main` (`2ec715f`) mid-census and
republished this row as 🟢 `Apache-2.0` a fourth time. 🔵 **So `Gap 406` is not a historical
observation about a stale column — it is a live propagation mechanism, caught in the act: a
carried column was copied forward once more, by a different pass, on the same day, after the
error was already twenty passes old.**

🔵 **This is a REGRESSION, not a long-standing error. This same file publishes `AGPL-3` for the
row under p93, p110, p111 and p112, and `Apache-2.0` under p114 and p115.** 🔴 **The KB had it
right for twenty passes; a licence column carried forward instead of re-read overwrote it with
the most consequential possible mistake — a strong network copyleft presented as a permissive
licence.** 🟢 **Read from `master/LICENSE`, 35 135 B, title line `GNU AFFERO GENERAL PUBLIC
LICENSE`, `Version 3`.**

## 🟢 🆕 `P117-I` — the other eight are RIGHT, and that is the point

| repo | 🟢 stars (API) | published licence | 🟢 tree, p117 | verdict |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 7 473 | 🟡 GPL-3 | GPL-3.0 (`COPYING.txt`) | 🟢 AGREE |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 23 587 | 🟢 MIT | MIT | 🟢 AGREE |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 6 845 | 🟢 Apache-2.0 | Apache-2.0 | 🟢 AGREE |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 506 | 🟢 ECL-2.0 | ECL-2.0 | 🟢 AGREE |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1 141 | 🟢 MIT | MIT | 🟢 AGREE |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 64 | 🟢 Apache-2.0<!--corrected-->| 🔴 **AGPL-3.0** | 🔴 **DIFFER** |
| [`DSpace/DSpace`](https://github.com/DSpace/DSpace) ※ | 1 102 | 🟢 BSD-3 | BSD-3-Clause | 🟢 AGREE |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 167 302 | 🟢 Apache-2.0 | Apache-2.0 | 🟢 AGREE |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 1 127 | 🟢 AGPL-3 | AGPL-3.0 | 🟢 AGREE |

🔵 **※ published as `dspace/dspace`; the canonical spelling is `DSpace/DSpace` and
`git ls-remote` returns the same head (`9d355068…`) for both — case only, not a break
(`P117-G`).**

🟢 **Eight of nine correct. The eight are the ones this page MEASURED; the one that is wrong is
the one it carried.** 🔵 **That contrast is the most transferable thing p117 found, and it
applies across this KB: `agents/top.md`'s carried column is 9/14 wrong on the same axis.**

## 🔴 🆕 `P117-H` — a foundation row that declares itself unmaintained

🔴 [`atutor/ATutor`](https://github.com/atutor/ATutor) — 180★, last push 2026-09-09. Its own
API description begins: **"NO LONGER USER LEVEL SUPPORTED. CONTRIBUTING DEVELOPERS INTERESTED
IN MAINTAINING ATUTOR, SHOULD REQUEST COLLABORATOR ACCESS."** 🔴 **It commits no licence file**
— checked `LICENSE`, `LICENCE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`,
`docs/LICENSE` and `README.md` on `master`.

🔵 **Not archived and not stale by date, so every freshness axis this KB has run (p109, p110)
would pass it. The disqualifying fact is written in prose in a field no prior pass could
read.** 🟢 **`elmsln/elmsln` (253★, GPL-3.0 in `LICENSE.md`) is the comparable row and carries
neither problem.**

🟡 **Recommendation, stated as a judgement rather than a measurement: `ATutor` should not be
offered as a starting point for an engagement. An LMS with no licence file cannot be
relicensed, forked commercially or indemnified, and its maintainers have asked in writing for
someone else to take it over.**

## 🟢 🆕 `P117-J` — the shelf's canonical-name drift, verified by SHA

| this KB publishes | 🟢 canonical (API `full_name`) | how verified |
|---|---|---|
| `openedx/edx-platform` | 🟢 **`openedx/openedx-platform`** | same head `e6d65a85…` — a RENAME |
| `dspace/dspace` | 🟢 **`DSpace/DSpace`** | same head `9d355068…` — case only |
| `frdel/agent-zero` | 🟢 **`agent0ai/agent-zero`** | same head `983fc50a…` — rename redirect |

🟢 **None is broken — all three resolve today, which is why 115 passes never noticed.**
🔴 **All three are wrong to publish: `p443-canonical-spelling` exists because one artefact under
two spellings becomes two entities in any compiler that keys on the string, and this page keys
on the string.** 🟡 **Not re-spelled in this pass's content commit: the addresses feed nine
passes of row-for-row cross-tabs, and `P115-W` established that re-spelling belongs in a commit
that changes nothing else. One such commit was made this pass, for the `Apereo…/Larissa` row
(`ACTION B`); the other three are pre-registered the same way.**

# Education — foundational repos

**Pass 116, 2026-10-11.** ⏱️ **Second pass of this date** (census window
**2026-10-11 02:18 UTC → 02:33 UTC**; p114 ran 23:54 on the 10th → 00:25 UTC on the 11th).

🟢 **Instrument this pass: `compose/code/p116-lock-agreement/` — `test_p116.sh`
**113 passed / 0 failed** (fully offline: real git repositories committed on disk and
served to the real `agree.sh` over `file://`, no mocks, no `api.github.com`);
`agree.sh` read **134 of 134** addresses, `rc=0` on every one, **zero unread**, plus
**two** control runs over the same 134.**

🔵 **On the pass number, stated because it affects how every cross-tab below reads:**
a SECOND instrument also numbered itself p115 — `compose/code/p115-region-evidence/`,
measuring regional placement and `Gap 403` — and it landed in the window 01:13–01:25 UTC,
while this pass's own work was in progress. **The two are independent reads of the same
shelf, not a sequence.** That pass holds the number 115 and the trend ids `T50`–`T52`;
this one is therefore **pass 116**, its rules are `P116-*` and its trends `T53`–`T55`.
This pass cross-tabulates against **p114**, which is the axis its question comes from, and
**does not incorporate the concurrent p115's regional channel** — it could not have,
because that channel was not on the shelf when `agree.sh` started.

🔵 **Tenth axis in ten passes, sixth read from the TREE. It answers the question p114
wrote into its own trend table and left open:** p114 published 34.5 % `full-reach` and
said what the figure still hid — *“whether the pinned versions are any good”*. Of that,
version currency and known vulnerabilities need a registry and an advisory feed, and
neither is on this channel (`P116-D`). But whether the lock and the manifest describe the
**same dependency set** is decidable from committed bytes — and it is the half with a hard
failure mode: **`npm ci` does not install a stale lock, it exits 1 and installs nothing.**

### 🟢 🆕 `P116-A` — the shelf where a lock reaches the root, re-read on whether it MATCHES

🔵 **Denominator: p114's own rows with `lockable_man > 0` and `root_orphan == 0` — the
**134** addresses p114 says have a lockable root manifest that a lock does reach. Rows
p114 already failed are not re-failed here; this is a tightening of p114's positive
class, not a new census of the shelf.**

| figure | value |
|---|---|
| rows in the denominator (`P116-A`) | **134** |
| rows where agreement is **decidable** from the root pair | **64** |
| rows where it is not | 70 |
| declared dependencies compared | **3 100** |
| declared dependencies **present** in the reaching lock | 🟢 **3 100** |
| declared dependencies **missing** | 🟢 **0** |
| rows at `agree` | 🟢 **64 of 64 (100 %)** |
| rows at `drift` | 🟢 **0** |

🟢 **Where this shelf has a lock that reaches the manifest, the lock matches the
manifest. On this axis the shelf is clean — and it is the FIRST axis in ten of which
that is true.**

### 🟢 The zero is a measurement, not an empty code path

🔵 **A census that reports none of the thing it looks for has to show it could have
found it. This one does, twice, through the same code path.**

| control | what it changes | result |
|---|---|---|
| `P116_PEER=1` | counts `peerDependencies`, which npm does **not** require in the lock tree | 🔴 **1 row drifts** — `thu-maic/dsh-openmaic`, declared 7 → 15, **7 missing** |
| `P116_NO_DEV=1` | drops `devDependencies` / `require-dev` | declared 3 100 → **1 902**; still **0 missing** |

🔵 **The positive control emits `drift` on real shelf data, so the zero is about the
shelf. The second shows what the zero covers: 1 198 of the 3 100 compared dependencies
(38.6 %) are dev-only, and the locks account for those too.**

### 🟢 🆕 `P116-U` — the foundation rows, re-read on whether the lock matches

🔵 **`P116-A` reads only rows whose root manifest a lock REACHES, so four of p114's nine
are out of scope here by construction — they are the four p114 already failed at the root,
and this axis does not re-fail a row. Shown so the page does not read as if they passed.**

| repo | licence | p111 | p112 | p114 | 🆕 p115 | declared / present |
|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔵 GPL-3 | 🟢 `checked` | 🟢 `pinned` | 🟢 `full-reach` | 🟢 **`agree`** | 🟢 **118 / 118** (npm 71, composer 47) |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 `checked` | 🟢 `pinned` | 🟢 `full-reach` | 🟢 **`agree`** | 🟢 **170 / 170** (yarn) |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 `checked` | 🔵 `partial-pin` | 🔵 `partial-reach` | 🟢 **`agree`** | 🟢 **13 / 13** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 `checked` | 🟢 `pinned` | 🟢 `full-reach` | 🔵 `no-lock-grammar` | — root manifest is go, not npm/composer/cargo |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟢 `checked` | 🔵 `partial-pin` | 🔵 `partial-reach` | 🔵 `no-lock-grammar` | — root manifest is maven |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | 🟢 `checked` | 🔵 `partial-pin` | 🔴 root orphaned | 🔵 *out of scope* | 🔴 already failed p114 at the root |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 `checked` | 🔵 `self-pinned` | 🔵 `self-pinned` | 🔵 *out of scope* | maven: no claim either way |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 `checked` | 🔴 `floating` | 🔴 root orphaned | 🔵 *out of scope* | 🔴 already failed p114 at the root |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟢 AGPL-3 | 🟢 `checked` | 🔴 `floating` | 🔴 `no-reach` | 🔵 *out of scope* | 🔴 already failed p114 at the root |

🟢 **The three foundation rows this axis can read all hold, and `kolibri` holds on the
axis where p112 and p114 both marked it partial** — its root npm pair is internally
consistent even though two of its 57 manifests are orphaned deeper in the tree. 🔵 **Those
are different claims about different files and neither cancels the other:** p114 says two
directories cannot be reproducibly installed; p115 says the directory you start in can.

🔵 **A studio consequence worth stating plainly:** on this shelf the python and JVM
foundations (`temporal`, `opencast`, `dspace`, `transformers`, `tutor`) are precisely the
rows where the lock-vs-manifest question **cannot be answered from committed bytes** —
there is no lockfile grammar to compare against. 🔴 **The ecosystems with the weakest
pinning on this shelf are also the ones where agreement is undecidable**, so a gate built
on this axis alone would silently pass them.

### 🟢 🆕 `P116-P` — `Gap 404` CLOSED, and p114's sizing was exact

🔵 **p114 found that the anchored requirement-file rule — carried in TWO copies, p112's
`manifests.awk` and p114's `positions.awk` — refuses the prefixed half of its own
convention (`dev_requirements.txt`, `latest_requirements.txt`, `system_requirements.txt`).
It sized the gap (198 files seen, 8 missed, 5 rows affected, exactly ONE verdict),
declared it, and deliberately did not fix it, because `P237` forbids forking a shared
classifier.**

🟢 **Fixed where the rule lives.** [`lib/reqname.awk`](../compose/code/lib/reqname.awk)
now holds **one** definition, widened to
`^([a-z0-9._-]+[-_.])?requirements([-_.][a-z0-9._-]+)?\.txt$`, loaded by both passes with
a second `-f`. `lib/test_reqname.sh` — **22 passed / 0 failed** — pins every case,
including the `myrequirements.txt` exclusion that stops the prefix group swallowing any
word that merely ends in the literal string. Neither consumer regressed:
**`test_p114.sh` 98 / 0**, **`test_p112.sh` 109 / 0**.

| p114 figure | as published | 🆕 restated | delta |
|---|---|---|---|
| rows at `full-reach` | 102 (34.5 %) | 🟢 **103 (34.8 %)** | **+1** |
| lockable manifests | 2 135 | **2 143** | **+8** — the 8 missed files, exactly as sized |
| manifests reached | 1 625 (76.1 %) | **1 633 (76.2 %)** | +8 |
| manifests orphaned | 510 (23.9 %) | **510 (23.8 %)** | 🟢 **0** |
| rows whose ROOT manifest is orphaned | 88 | 🟢 **87** | **−1** |
| rows that moved | — | 🟢 **[`sdv-dev/sdv`](https://github.com/sdv-dev/sdv) `no-reach` → `full-reach`** | exactly one |

🔵 **The orphan count does not move at all — all 8 newly-visible files are pins that ADD
coverage, so numerator and denominator rise together.** That is the direction the widened
rule predicts in its own header, and it is why no row lost a verdict it held.

### 🔴 🆕 `Gap 406` — OPENED: there is a FOURTH npm lock flavour on this shelf, and it is sized at exactly one row

🔵 **`P116-I` widened this axis from one npm lock flavour to three. The shelf has
four.** Of the 70 rows this axis could not decide, **69** are rows whose root manifest is
in an ecosystem with no lock grammar here at all (python 28, `npm,py` 12, maven, go,
ruby). **The seventieth is not:**

| row | root tree | why undecided |
|---|---|---|
| [`mietiainvestigacion-creator/api-eduadapt`](https://github.com/mietiainvestigacion-creator/api-eduadapt) | `package.json`, **`bun.lock`**, `bunfig.toml` | 🔴 **`bun.lock` is a fourth npm lock flavour this axis does not read** |

🔵 **Sized, not guessed:** exactly **1 of 134** rows. The file is JSON-shaped — a
`workspaces` map keyed by path, each entry carrying its own `dependencies` — so it is
very likely parseable, which is precisely why it is **declared rather than parsed on a
hunch**: adding a grammar without a fixture and a control is how the three false
positives above were produced in the first place.

🔵 **Error direction:** one-way and benign. A flavour this axis cannot read makes a row
**undecidable**, never `agree` and never `drift`, so no published figure here is wrong
because of it — the decidable denominator is 64 rather than 65.

🔵 **How it ends:** a `bun.lock` grammar with its own fixtures in the suite, the census
re-run, and the decidable denominator restated from 64 to 65.

### 🟢 The 64 decidable rows, by declared-dependency volume

🔵 **Every row below read `agree` — `declared/present` with zero missing. Volume matters
because it is the size of the graph a client team inherits intact.**

| repo | declared / present | ecosystems |
|---|---|---|
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟢 **345 / 345** | npm (yarn, workspaces — `P116-L`) |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟢 **268 / 268** | npm 133 + composer 135 |
| [`yukazakiri/koakademy`](https://github.com/yukazakiri/koakademy) | 🟢 **214 / 214** | npm 125 + composer 89 |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🟢 **197 / 197** | npm (yarn) |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🟢 **174 / 174** | npm 54 + composer 120 |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **170 / 170** | npm (yarn) |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **118 / 118** | npm 71 + composer 47 |
| [`claroline/Claroline`](https://github.com/claroline/Claroline) | 🟢 **101 / 101** | npm 51 + composer 50 |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟢 **88 / 88** | npm |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🟢 **86 / 86** | npm (pnpm) |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🟢 **79 / 79** | npm 22 + composer 57 |
| [`libretexts/shapeshift`](https://github.com/libretexts/shapeshift) | 🟢 **73 / 73** | npm |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 **63 / 63** | npm |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟢 **63 / 63** | npm |
| [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks) | 🟢 **57 / 57** | npm 21 + composer 36 |
| [`openmage/magento-lts`](https://github.com/openmage/magento-lts) | 🟢 **50 / 50** | composer |
| [`elgg/elgg`](https://github.com/elgg/elgg) | 🟢 **49 / 49** | npm 7 + composer 42 |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟢 **46 / 46** | npm 18 + composer 28 |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟢 **43 / 43** | npm 6 + composer 37 |
| [`aiverify-foundation/moonshot-ui`](https://github.com/aiverify-foundation/moonshot-ui) | 🟢 **42 / 42** | npm |

🔵 *44 further rows read `agree` at smaller volumes; the full census is
`compose/code/p116-lock-agreement/result.2026-10-11.tsv`.*

# Education — foundational repos

**Pass 115, 2026-10-11.** ⏱️ **Second pass of this date** (census window
**01:13 → 01:25 UTC**).

🟢 **`region.sh` read **296 of 296** addresses in 12 min, zero unread, zero empty trees
(`compose/code/p115-region-evidence/`, `test_p115.sh` **193 passed / 0 failed**, fully
offline), plus four controls re-derived from the same token snapshot in 2.5 s each.**

### 🔴 🆕 `P115-AF` — the nine `checked` foundations place ZERO rows, and that is a property of being a foundation

🔵 **p112 shrank this page to nine `checked` code repositories and p114 re-read them on lock
reach. p115 reads the same nine, in the same order, on whether their own root metadata names
a country:**

| repo | licence | p112 | p114 | 🆕 p115 layer 0 | 🆕 layer 1 | 🆕 layer R |
|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 `pinned` | 🟢 `full-reach` | 🔴 `no-country` | 🔴 **`n-contested`** | 🔴 `r-no-country` |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 `pinned` | 🟢 `full-reach` | 🔴 `no-country` | 🔴 `n-no-country` | 🔴 `r-no-country` |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 `pinned` | 🟢 `full-reach` | 🔴 `no-country` | `n-none` | `r-none` |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟡 `partial-pin` | 🟡 `partial-reach` | 🔴 `no-country` | `n-none` | 🔴 `r-no-country` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟡 `partial-pin` | 🟡 `partial-reach` | 🔴 `no-country` | 🔴 `n-no-country` | 🔴 `r-no-country` |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | 🟡 `partial-pin` | 🔴 `partial-reach`, root | 🔴 `no-country` | `n-none` | 🔴 `r-no-country` |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🔵 `self-pinned` | 🔵 `self-pinned` | 🔴 `no-country` | 🔴 `n-no-country` | 🔴 `r-no-country` |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🔴 `floating` | 🔴 `partial-reach`, root | 🔴 `no-country` | `n-none` | 🔴 `r-no-country` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟢 AGPL-3 | 🔴 `floating` | 🔴 `no-reach` | 🔴 `no-country` | `n-none` | 🔴 `r-no-country` |

🔴 **Nine of nine `no-country`, at every layer. Not one foundational repository on this page
commits an address that names a country.** 🟢 **And the reason is not neglect — it is
structural, and it reverses the intuition a reader brings:**

🔵 **These nine are the largest, longest-lived, most international projects on the shelf. A
project at that scale registers `moodle.org`, `oppia.org`, `temporal.io`, `dspace.org`,
`huggingface.co` — a generic or vanity TLD, deliberately, because a country code in the
domain of a global project is a liability. 🔴 **Placeability on this channel is inversely
related to project maturity**: the rows that place are small academic repositories whose
maintainer still uses a university email, and the rows that cannot place are the ones a
studio is most likely to build on.**

### 🟡 🆕 `P115-AI` — `moodle/moodle` is the worked example of why layer 1 is never folded in

| layer | verdict | evidence |
|---|---|---|
| **0** (root) | 🔴 `no-country` | one address, not country-bearing |
| **1** (nested) | 🔴 **`n-contested`** | 🔴 **`gjcampbell.co.uk`, `tubo-world.de`, `www.mullie.eu` — maintainer emails of libraries Moodle BUNDLES under `lib/`** |
| **R** (README) | 🔴 `r-no-country` | — |

🔵 **Moodle HQ is in Perth and the committed org map places it APAC. A flat read of this tree
— every structured file, root and nested alike — offers TWO EUROPEAN COUNTRIES for an
Australian project**, and `region` is a field this KB filters on, so a wrong value reads
downstream as data and not as a guess (`P800`). 🟢 **`P115-F` excludes `vendor/` and
`node_modules/`; it cannot exclude `lib/`, because `lib/` is also where a project keeps its
own code. Depth can — and the suite pins this as a regression on a fixture whose bundled
libraries are both European, so layer 1 returns a single CLEAN region and a flat read would
have published it.**

🟢 **Measured shelf-wide by the `flat` control: the pre-depth-split read would have placed
**7 extra rows**, of which at least two are demonstrably wrong —
[`atutor/ATutor`](https://github.com/atutor/ATutor) into LATAM on `tiagogouvea.com.br` (ATutor
is a Toronto project) and [`elmsln/elmsln`](https://github.com/elmsln/elmsln) into EMEA on
three JS/PHP library authors' domains.**

### 🟢 🆕 The rows on the wider shelf that DO place, and what placed them

🔵 **22 of 296 at layer 0. Every North America placement — all seven — is `academic`:**

| region | places | strongest class present |
|---|---|---|
| **EMEA** | 9 | 1 `academic`, 1 `typed`, 7 `other` |
| **North America** | 7 | 🟢 **7 `academic`** — `berkeley.edu` ×3, `brynmawr.edu`, `calpoly.edu`, `lafayette.edu`, `gatech.edu`, `nd.edu`, `vt.edu`, `csail.mit.edu` |
| **LATAM** | 6 | 2 `typed` (`country: BR` ×2), 4 `other` (`.com.br` ×3, `ipn.mx`) |
| 🔴 **APAC** | 🔴 **0** | — |

🟢 **`.edu` is the single most productive token on this shelf** — a registry-restricted
suffix that names an institution and a country in the same string. 🔵 **The committed
address-keyed placements are in
`compose/code/p115-region-evidence/addresses.region.tsv`; the method, every control and the
pre-registered actions are in that directory's `README.md`.**

# Education — foundational repos

**Pass 114, 2026-10-11.** ⏱️ **First pass of this date** (census window
**2026-10-10 23:54 → 2026-10-11 00:25 UTC**).

🟢 **`reach.sh` read **296 of 296** addresses in 4 m 09 s, zero unread
(`compose/code/p114-lock-reach/`, `test_p114.sh` **98 passed / 0 failed**, fully
offline), plus three control runs over the same 296.**

🔴 **p112 shrank this page to nine `checked` code repositories and gave them a closure
verdict. p114 re-reads the same nine on whether the lock it found actually REACHES the
manifest — and three of the nine hold, three slip, and one of the slips is a root
manifest.**

### 🔴 🆕 `P114-U` — the nine, re-read on lock reach

🔵 **`full-reach` = every lockable manifest in the tree has a lock in its own directory
or an ancestor of it (`P114-B`). `reqpin` = the row's python coverage depends on a pinned
`requirements.txt` rather than a lockfile (`P114-C`), which the stage-B control measures
separately. p111/p112 columns are carried; this pass changed neither.**

| repo | licence | p111 | p112 | 🆕 p114 | orphaned / lockable | 🆕 verdict |
|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 63** | 🟢 **holds — 63 manifests, every one reached** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 2** | 🟢 **holds** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 6** | 🟡 **holds, but on a `requirements.txt` — see below** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟢 `checked` | 🟡 `partial-pin` | 🟡 `partial-reach` | 1 / 9 | 🟡 **one orphan, not at the root** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 `checked` | 🟡 `partial-pin` | 🟡 `partial-reach` | 2 / 57 | 🟡 **57 manifests, 2 orphaned** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | 🟢 `checked` | 🟡 `partial-pin` | 🟡 `partial-reach` | 🔴 **2 / 3, root** | 🔴 **the root manifest is orphaned** |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 `checked` | 🔵 `self-pinned` | 🔵 `self-pinned` | — | 🔵 **maven: no claim either way (`P114-E`)** |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 `checked` | 🔴 `floating` | 🔴 `partial-reach` | 🔴 **21 / 22, root** | 🔴 **pin at fork time; 20 requirement files, zero lockfiles** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟢 AGPL-3 | 🟢 `checked` | 🔴 `floating` | 🔴 **`no-reach`** | 🔴 **1 / 1, root** | 🔴 **pin at fork time; the root `pyproject.toml` has no lock at all** |

### 🟡 🆕 `P114-V` — how much of this page rests on a `requirements.txt` rather than a lock

🔵 **Run with stage B disabled (`P114_NO_BODY=1`), over the same 296 trees in the same
window, the nine read differently — and the gap is the measurement of what a pinned
`requirements.txt` is carrying on this page:**

| repo | with stage B | without stage B | what that means |
|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `full-reach` | 🟡 **`partial-reach`** | 🔴 **its top verdict rests entirely on a pinned `requirements.txt`; it carries no python lockfile** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟡 `partial-reach` | 🟡 `partial-reach` | unchanged |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `full-reach` | 🟢 **`full-reach`** | 🟢 **real lockfiles throughout; nothing rests on stage B** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 `full-reach` | 🟢 **`full-reach`** | 🟢 **real lockfiles (`go.sum`)** |

🔵 **This is not a demotion of `oppia/oppia`.** `P112-F` settled that a `requirements.txt`
pinned with `==` throughout **is** a lock, and oppia's is. It is a note about what breaks
it: a lockfile is regenerated by a resolver, a pinned requirements file is maintained by
hand, and the two decay differently. A studio vendoring oppia should expect to own that
file.

### 🟢 🆕 `P114-W` — the shape worth copying, measured

🔵 **23.9 % of this shelf's manifests are orphaned, so it is worth naming the rows that
prove a large polyglot tree CAN be pinned end to end. These are the three widest
`full-reach` rows on the shelf:**

| repo | licence | lockable manifests | reached |
|---|---|---|---|
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | 🔴 **"Fair Code License" v1.0 — NOT OSI** ⚠️ **was 🟢 Apache-2.0**<!--corrected--> | **114** | 🟢 **114 / 114** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | **63** | 🟢 **63 / 63** |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🟢 AGPL-3 | **58** | 🟢 **58 / 58** |

🔴 **The counter-example, for scale:** [`microsoft/autogen`](https://github.com/microsoft/autogen)
carries **87** lockable manifests and a lock reaches **23** of them — **64 orphans**, the
largest orphan count on the shelf. [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms)
is the opposite kind of near-miss: **595 of 596** reached, one orphan, and it is the row
that single-handedly carries North America's regional figure (see `intel/market.md`,
`P114-R`).

# Education — foundational repos

**Pass 113, 2026-10-10.** ⏱️ **Twenty-third pass of this date.**

🟢 **`bind.sh` read **296 of 296** addresses in 7 m 10 s, zero unread, zero stray lines,
zero capped rows (`compose/code/p113-provider-binding/`, `test_p113.sh` 121 passed / 0
failed, fully offline), plus a no-body control run over the same 296 for this pass's own
contribution.**

### 🟢 🆕 `P113-D` — the foundation tier's binding, over 166 addresses of this page

| verdict | rows on this page |
|---|---|
| 🔵 `no-model` — no declaration names a model | **130** |
| 🟢 `local` — a local inference runtime is declared | 🟢 **22** |
| 🔴 `hosted-only` — one vendor's endpoint, no abstraction, no override | 🔴 **7** |
| 🟢 `broker` — a provider-abstraction layer | 5 |
| 🟡 `override` — a configurable endpoint | 2 |

🟢 **36 of this page's 166 addresses bind a model, and 29 of those 36 (80.6 %) can be
pointed at one the client controls — a better ratio than the agent shelf's 79.4 %.**
🔵 **That direction is expected and worth stating anyway: a foundation is a library, and a
library that hard-wires a vendor would not be a foundation.**

### 🟢 The self-hostable foundation tier — the rows that need no egress at all

🔵 **Every row below declares a LOCAL inference runtime in a manifest, an environment
template, a compose file or a Modelfile. These are the bases an EMEA data-residency
engagement or an air-gapped deployment can be built on without a gateway in front.**

| repo | declares | p112 closure |
|---|---|---|
| [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 `ollama` | 🟢 `pinned` |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 `transformers`, HF local | 🔴 `floating` |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 `mlx`, `transformers`, `vllm` (+ `litellm` broker) | 🔴 `floating` |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | 🟢 `llama.cpp`, `ollama`, `whisper` | 🟡 `partial-pin` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟢 `transformers` | 🟢 `pinned` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟢 `transformers` | 🟢 `pinned` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟢 `transformers` | 🟡 `partial-pin` |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 `ollama`, `sentence-transformers`, `transformers`, `whisper`, HF local | 🟡 `partial-pin` |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `ollama`, `sentence-transformers`, `vllm` | 🟡 `partial-pin` |
| [`nextcloud/context_chat_backend`](https://github.com/nextcloud/context_chat_backend) | 🟢 `ctransformers`, `llama.cpp`, `sentence-transformers`, `transformers` | 🔴 `floating` |
| [`nextcloud/translate2`](https://github.com/nextcloud/translate2) | 🟢 HF local | 🔴 `floating` |
| [`nextcloud/text2image_stablediffusion2`](https://github.com/nextcloud/text2image_stablediffusion2) | 🟢 `transformers` | 🔴 `floating` |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 `sglang`, `transformers`, `vllm`, HF local | 🟢 `vendored` |
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | 🟢 `sentence-transformers`, `transformers`, `vllm`, HF local | 🟡 `partial-pin` |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | 🟢 `ollama`, `sentence-transformers`, `transformers` | 🟢 `pinned` |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🟢 `ollama` | 🟢 `pinned` |
| [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🟢 `ollama` | 🟢 `pinned` |
| [`nestauk/ojd_daps_skills`](https://github.com/nestauk/ojd_daps_skills) | 🟢 `sentence-transformers`, `transformers` | 🔴 `floating` |
| [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 `sentence-transformers` | 🔴 `floating` |
| [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) | 🟢 `transformers` | 🟡 `self-pinned` |
| [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) | 🟢 `llama.cpp`, `transformers`, `whisper`, HF local | 🔴 `floating` |
| [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 `sentence-transformers`, `transformers`, HF local | 🟡 `partial-pin` |

🔴 **The pattern across the column on the right is the warning: `ollama/ollama`,
`openedx/edx-platform`, `ILIAS`, `adaptive-knowledge-graph`, `moodle-mcp-server` and
`OtterDen-Lab/Autograder` are `local` AND `pinned`. Nine of the twenty-two are
`floating` — self-hostable and not reproducible, which is the p112 failure in a new place
and needs the same `uv lock` / `pip-compile` step at fork time.**

### 🔴 🆕 `P113-E` — seven foundations bind one vendor, and one of them is a national stack

| repo | hosted family | why it matters here |
|---|---|---|
| [`opetushallitus/ehoks`](https://github.com/opetushallitus/ehoks) | 🔴 **`bedrock`** | 🔴 **VERIFIED in its `pom.xml`: `bedrockruntime`, `bedrock`, `bedrockagentruntime`. The Finnish National Agency for Education's personal-competence-plan service — EUPL-licensed public infrastructure (`T33`) — binds its model layer to a US hosted provider** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🔴 `google` | Apache-2.0, `broad` bench, 2 959 tests, `pinned`, `checked` — and one vendor |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 `anthropic`, `openai` | two wired vendors is not an abstraction |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `anthropic` | Apache-2.0 Swiss LMS; `tests-only` on p111 |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 `openai` | 🔴 **Elastic-2.0 (not OSS) AT THE ROOT** — `p1040` read Elastic-2.0 as a `NON-GRANT` found *in tree* beside a root AGPL-3; `p118` read the root `LICENSE` itself (3 860 B, zero occurrences of "affero" or "general public") and it IS Elastic-2.0 |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🔴 `openai` | `floating` and `bare` — weakest row on three axes at once |
| [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | 🟡 `moonshot` | 🟢 **DISCOUNTED — self-name collision, adjudicated by hand on `agents/top.md` (`P113-R`)** |

🔴 **`T44` — the EMEA sovereignty story on this shelf is strong in its LIBRARIES and
broken in its ONE piece of national infrastructure.** 🟢 **EMEA leads every region on
controllability (7 of 10 model-bearing rows, 5 of them `local`), and the single public
national service in the set is the one row wired to a US endpoint.** 🔵 **That is a
procurement fact, not a code defect: `ehoks` is EUPL — adopt-and-contribute, per `T33` —
so the model layer is replaceable by a contributor, and the replacement is a deliverable
rather than a blocker.**

### 🔵 The error direction, stated before the figures are read

🔴 **This axis reads DECLARATIONS and never program text, so `local` and `broker` are
LOWER bounds and `hosted-only` is an UPPER bound (`P113-I`).** 🟢 **Compose files are read
and `Modelfile` is selected on its name, which are the two mitigations that matter; a repo
driving Ollama over plain `requests` with nothing declared still reads `no-model`.**

---

# Education — foundational repos

**Pass 112, 2026-10-10.** ⏱️ **Twenty-second pass of this date.**

🟢 **`depclosure.sh` read **296 of 296** addresses in 4 m 41 s, zero unread
(`compose/code/p112-dependency-closure/`, `test_p112.sh` 109 passed / 0 failed, fully
offline), plus a no-stage-B control run over the same 296 for this pass's own
contribution.**

🔴 **p111 gave "foundational" a TREE test and shrank this page to nine `checked` code
repositories. p112 gives the same nine a REPRODUCIBILITY test, and three of them pass
it.**

### 🔴 🆕 `P112-U` — the nine, re-read on dependency closure

🔵 **`pinned` = every lockable ecosystem in the tree has a lockfile (or, per `P112-F`, a
`requirements.txt` pinned with `==` throughout). Licences and bench figures are carried
from this page's prior passes; this pass changed neither and added four columns.**

| repo | licence | bench | p111 | ecosystems | locked | 🆕 p112 verdict |
|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 9 | 🟢 `checked` | npm,php | 2 / 2 | 🟢 **`pinned`** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 6 | 🟢 `checked` | npm,py | 2 / 2 | 🟢 **`pinned`** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 11 | 🟢 `checked` | go | 1 / 1 | 🟢 **`pinned`** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟢 6 | 🟢 `checked` | npm,py,maven | 🟡 1 / 2 | 🟡 **`partial-pin`** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 7 | 🟢 `checked` | npm,py,gradle | 🟡 2 / 3 | 🟡 **`partial-pin`** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟡 AGPL-3 | 🟢 7 | 🟢 `checked` | npm,py | 🟡 1 / 2 | 🟡 **`partial-pin`** |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 16 | 🟢 `checked` | maven | — | 🟡 **`self-pinned`** |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 11 | 🟢 `checked` | py | 🔴 **0 / 1** | 🔴 **`floating`** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟡 AGPL-3 | 🟢 6 | 🟢 `checked` | py | 🔴 **0 / 1** | 🔴 **`floating`** |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 GPL-2 | 🟢 6 | 🟡 `partial` | npm,php | 🟡 1 / 2 | 🟡 **`partial-pin`** |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | 🟢 CC0-1.0 | 🟢 6 | 🔵 `no-code` | — | — | 🔵 **`no-manifest`** |

🟢 **So the foundation layer of this KB, after three independent tests (bench, tree
verification, tree closure), is **three repositories**: `moodle/moodle`,
`oppia/oppia` and `temporalio/temporal`. Three of 296 addresses is 1.0 % of the
shelf — down from p111's nine (3.0 %) and p110's eleven (3.7 %), and now resting on a
test each previous axis could not apply.**

### 🔴 🆕 `P112-V` — `huggingface/transformers` is the most consequential single row on this page

🔴 **It has the second-widest bench on the shelf (11 authors), 1 797 test files, CI that
names a runner and fires on `pull_request`, **20 deployment artefacts in the tree** — and
not one lockfile. Its `py` ecosystem declares ranges and nothing resolves them.**

🔵 **Why that is a foundation-level finding rather than a nit: every pattern on
`compose/patterns.md` that touches inference, tokenisation or fine-tuning goes through
this repository, and p110 established that two thirds of this shelf must be vendored at a
SHA rather than depended on. Vendoring `transformers` at a SHA vendors the CODE and
leaves the ENVIRONMENT floating — and it is the one repository on this page where the
environment is the hard part.**

🟢 **The remedy is cheap, nameable and belongs in an engagement's week one: resolve and
commit the environment yourself (`uv pip compile` / `pip-compile` against the vendored
SHA, committed beside it), and treat the resulting lock as a deliverable of the fork
rather than an artefact of CI. The same step covers `overhangio/tutor`, and the two
together cover both floating rows on this page.**

### 🟢 🆕 `P112-W` — the wider dependable set: `checked` + `pinned`, bench `small` or better

🔵 **Three rows is too narrow to source an engagement from. Relaxing the bench to `small`
(3–5 authors) while REQUIRING both a `checked` tree and a `pinned` one gives the set that
is staffed, verifiable and reproducible at once:**

| repo | licence | bench | test files | ecosystems | region |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 broad | 🟢 5 014 | npm,php | APAC (AU) |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 broad | 🟢 2 959 | npm,py | North America |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟡 GPL-3 | 🟡 small | 🟢 2 276 | npm,php,maven | EMEA (DE) |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 **MIT** | 🟢 broad | 🟢 1 208 | go | North America |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 Elastic-2.0 (not OSS) | 🟡 small | 🟢 770 | npm,php | North America |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3** | 🟡 small | 🟢 757 | npm,py,php | North America |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟡 GPL-2 | 🟡 small | 🟢 469 | npm,php | LATAM (BR) |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟡 contested | 🟡 small | 🟢 304 | npm,ruby | APAC (IN) |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 **MIT** | 🟡 small | 251 | npm,py | North America |
| [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🔴 **AGPL-3.0** | 🟡 small | 201 | npm | EMEA (DE) |
| [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | 🟢 **Apache-2.0** | 🟡 small | 150 | py | APAC (SG) |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🟡 GPL-3 | 🟡 small | 18 | npm,php | North America |

🟢 **Twelve rows, every region represented, five of them permissive. This is the honest
answer to "what can Globant build on in open-source education" — 12 of 296 addresses,
4.1 %, each one read live this pass with `rc=0`.**

### 🟢 🆕 `P112-X` — three `tests-only` rows whose trees ARE reproducible, which changes their price

🔵 **p111 ruled these "big suite, no pipeline" or worse. p112 finds the expensive half
already done: the dependency set resolves, so a fork can run that suite on day one and
only needs a pipeline pointed at it.**

| repo | licence | p111 | 🆕 p112 | what the fork actually has to supply |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | 🟡 `tests-only`, 1 634 tests | 🟢 **`pinned`** | 🟢 a CI pipeline only |
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 ECL-2.0 | 🟡 `tests-only`, 1 791 tests | 🟡 `self-pinned` (maven) | a pipeline; transitives resolve, not locked |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟡 GPL-2 | 🔴 `fossil-ci` (Travis) | 🟢 **`vendored`** | 🟢 a pipeline; **deps are committed in-tree** |

🔴 **`OS4ED/openSIS-Classic` is the correction worth carrying: `fossil-ci` reads as the
worst verdict on p111's ladder, and its dependency tree is committed, so its suite is
runnable offline today. The p111 verdict priced it as a rewrite; p112 prices it as a
pipeline.**

### 🔵 🆕 `P112-Y` — 20 code-bearing rows declare no dependencies, and 7 declare them somewhere this instrument cannot read

🟢 **All 31 rows p111 called `no-code` come back `no-manifest` here — 31 of 31, from a
different file set entirely. Two independent tree axes agree exactly on which rows of
this shelf are not software.**

🔴 **The remainder is where the first draft of this pass was WRONG, and the correction is
recorded rather than quietly applied (`P112-N`). Seven rows declare dependencies in a
build system `depclosure.sh` does not resolve, and the draft reported all seven as
declaring NOTHING:**

| repo | source files | declares its dependencies in |
|---|---|---|
| [`oppia/oppia-android`](https://github.com/oppia/oppia-android) | 🟢 1 213 | Bazel `WORKSPACE` + `BUILD.bazel` |
| [`microsoft/o365-moodle`](https://github.com/microsoft/o365-moodle) | 🟢 352 | Moodle plugin `version.php` (`$plugin->dependencies`) |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 163 | Odoo `__manifest__.py` |
| [`sngdtechnologies/ai-moodle-security`](https://github.com/sngdtechnologies/ai-moodle-security) | 35 | Moodle plugin `version.php` |
| [`alvarogregori/moodle-ai-graded-assignment`](https://github.com/alvarogregori/moodle-ai-graded-assignment) | 32 | Moodle plugin `version.php` |
| [`jeanlucio/moodle-local_aihub`](https://github.com/jeanlucio/moodle-local_aihub) | 25 | Moodle plugin `version.php` |
| [`limekiller/moodle-block_openai_chat`](https://github.com/limekiller/moodle-block_openai_chat) | 16 | Moodle plugin `version.php` |

🟢 **They are now `foreign-build`, which makes NO reproducibility claim in either
direction. The pattern inside it is useful on its own: five of the seven are Moodle
plugins, so the Moodle plugin layer of this shelf is invisible to every manifest-based
supply-chain tool a client is likely to already own — and that is worth saying in a
Moodle engagement before the client's scanner says it instead.**

---

**Prior passes on this page follow, newest first.**

# Education — foundational repos

**Pass 111, 2026-10-10.** ⏱️ **Twenty-first pass of this date.**

🟢 **`vsurface.sh` read **296 of 296** addresses in 9 m 41 s, zero unread
(`compose/code/p111-verification-surface/`, `test_p111.sh` 66 passed / 0 failed, fully
offline).**

🔴 **p110 gave "foundational" a bench test and shrank this page to 11 rows. p111 gives
it a TREE test, and one of those 11 rows turns out to contain no source code at all.**

### 🔴 🆕 `P111-L` — the correction to `P110-J`

🔵 **`P110-J` published eleven rows as "the shelf's actual foundation" on the strength of
`bus_factor` ≥ 6 plus a commit within 30 days. Both are properties of the HISTORY, and a
Markdown list has a history exactly like a compiler does.**

| repo | licence | `bus_factor` | p109 | 🆕 p111 verdict | test files | CI |
|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 9 | 🟢 fresh 7 d | 🟢 **`checked`** | 🟢 5 014 | 6 · gha |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 6 | 🟢 fresh 0 d | 🟢 **`checked`** | 🟢 2 959 | 16 · gha |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 11 | 🟢 fresh 1 d | 🟢 **`checked`** | 🟢 1 797 | 59 · circle+gha |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 11 | 🟢 fresh 0 d | 🟢 **`checked`** | 🟢 1 208 | 22 · gha |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟢 6 | 🟢 fresh 1 d | 🟢 **`checked`** | 🟢 1 033 | 21 · gha |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 16 | 🟢 fresh 0 d | 🟢 **`checked`** | 🟢 1 025 | 9 · gha |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 7 | 🟢 fresh 1 d | 🟢 **`checked`** | 🟢 777 | 43 · gha |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟡 AGPL-3 | 🟢 7 | 🟢 fresh 10 d | 🟢 **`checked`** | 🟢 235 | 7 · gha |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟡 AGPL-3 | 🟢 6 | 🟢 fresh 2 d | 🟢 **`checked`** | 38 | 9 · gha+gitlab |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 GPL-2 | 🟢 6 | 🟢 fresh 3 d | 🟡 **`partial`** | 🟢 577 | 4 · gha |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | 🟢 CC0-1.0 | 🟢 6 | 🟢 fresh 6 d | 🔴 **`no-code`** | 🔴 **0** | 🔴 **0** |

🔴 **`lukeslp/awesome-accessibility` is a curated link list: 46 authors, `bus_factor` 6,
committed six days ago, **zero source files**. It is a perfectly good list and it was
never a code foundation — it was in the table because no axis before this one could tell
code from prose.**

🟢 **So the corrected foundation layer of this KB is **nine `checked` code
repositories**, with `tao-core` at `partial` beside them. Nine of 296 addresses is
3.0 % of the shelf — slightly smaller than p110's 3.7 %, and now resting on three
independent axes (bench, liveness, verification) rather than two.**

### 🟢 🆕 `P111-T` — the wider dependable set: `broad` or `small` bench, `checked`, suite ≥ 200

🔵 **Nine rows is too narrow to source an engagement from, and `P110-J`'s `broad`
threshold (≥ 6 authors) was deliberately severe. Relaxing the bench to `small` (3–5
authors) while REQUIRING a `checked` tree and a suite of at least 200 test files gives a
set that is both staffed and verifiable:**

| repo | licence | `bus_factor` | test files | CI | region |
|---|---|---|---|---|---|
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | 🟢 12 | 🟢 **7 664** | 5 · gha+jenkins | North America |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 9 | 🟢 5 014 | 6 · gha | EMEA |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 6 | 🟢 2 959 | 16 · gha | North America |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟡 GPL-3 | 🟢 4 | 🟢 2 276 | 5 · gha | EMEA |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 11 | 🟢 1 797 | 59 · circle+gha | North America |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 11 | 🟢 1 208 | 22 · gha | North America |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 ECL-2.0 | 🟢 6 | 🟢 1 033 | 21 · gha | EMEA |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 16 | 🟢 1 025 | 9 · gha | North America |
| [`oppia/oppia-android`](https://github.com/oppia/oppia-android) | 🟢 Apache-2.0 | 🟢 4 | 🟢 888 | 22 · gha | North America |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 7 | 🟢 777 | 43 · gha | North America |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 Elastic-2.0 (not OSS) | 🟢 3 | 🟢 770 | 10 · gha | North America |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 BSD-3 | 🟢 5 | 🟢 757 | 13 · gha | North America |
| [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | 🟡 **contested** ※ | 🟢 5 | 🟢 616 | 2 · gha | 🟢 **LATAM** |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar)  | 🔴 GPL-2.0 | 🟢 3 | 🟢 469 | 2 · gha | 🟢 **LATAM** |
| [`ed-fi-alliance-oss/Ed-Fi-ODS`](https://github.com/ed-fi-alliance-oss/Ed-Fi-ODS) | 🟢 Apache-2.0 | 🟢 3 | 🟢 423 | 26 · gha | North America |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | 🟢 MIT | 🟢 4 | 🟢 306 | 12 · gha | North America |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟡 **contested** ※ | 🟢 4 | 🟢 304 | 3 · gha | APAC |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 MIT | 🟢 3 | 🟢 251 | 17 · gha | North America |
| [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) | 🟢 MIT | 🟢 5 | 🟢 250 | 15 · circle+gha+jenkins | 🟢 **APAC** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟡 AGPL-3 | 🟢 7 | 🟢 235 | 7 · gha | North America |
| [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | 🟢 MIT | 🟢 7 | 🟢 228 | 6 · circle+gha+jenkins | 🟢 **APAC** |
| [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🟡 **contested** ※ | 🟢 3 | 🟢 201 | 3 · gha | 🟢 **EMEA** |

🔵 **22 rows. Licences are carried from this page's prior passes: this pass changed no
licence reading and discovered no new repository — it added three columns.**

🔴 **※ `P111-V` — three of these rows carry CONTRADICTORY licence readings across the
live pages of this KB, and this pass declines to pick a side rather than publish one:**

| repo | reading A | reading B |
|---|---|---|
| [`portabilis/i-diario`](https://github.com/portabilis/i-diario) | `AGPL-3.0` | 🟡 `LGPL-3` |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | 🟢 `MIT` | 🟡 `MIT/AGPL split` (and a `CC-BY-SA-4.0` reading on a third page) |
| [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🔴 `AGPL-3.0` (as `FWU-DE/ais-chat`) | 🟢 `EUPL-1.2` (as `fwu-de/ais-chat`) |

🔵 **Two of the three have a plausible mechanism already named on this shelf: a split
licence read once per component, and a case-variant slug read as two repositories
(`P439`, `P288`). The third may be a relicensing this KB straddled.** 🟢 **None is
p111's axis, so none is resolved here. They are flagged because a foundation table is
exactly the wrong place to launder a contradiction into a single confident cell, and
because the licence tier is where this KB has the most instruments — `P963`, `P637` and
`P342` all exist to settle precisely this.**

### 🔴 🆕 `P111-U` — two rows p109 and p110 downgraded that this axis argues back up

🔴 **`instructure/canvas-lms` and `project-sunbird/sunbird-lms-service` were both
excluded from `P110-J` for cooling: p109 graded them 🟡 `slowing` at 163 d and 291 d.
On the tree axis they are `checked`, with 7 664 and 228 test files and PR-gated CI.**

🟢 **For a FORK-AND-OWN engagement — which p110 says is the common case on 67.6 % of this
shelf — a cooling repository with a large PR-gated suite is a better target than a
freshly-committed solo repository with none. `canvas-lms` has the largest verified suite
on this shelf; `rosariosis` was committed to yesterday and has zero tests across 603
source files.**

🔵 **Stated as a rule, because it is the reusable part: liveness tells you whether
upstream will MEET you; verification tells you whether you can proceed without them.
When the plan is to proceed without them, the second one dominates.**

### 🔴 🆕 `P111-P` — the biggest suites on this shelf that nothing runs

| repo | test files | CI | verdict | why |
|---|---|---|---|---|
| [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🔴 **8 347** | 2 · gitlab+azure | 🟡 `partial` | 🔴 **no PR trigger at all** (`P111-M`) |
| [`kuali/rice`](https://github.com/kuali/rice) | 🔴 **1 791** | 🔴 **0** | 🟡 `tests-only` | no CI configuration at HEAD |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🔴 **1 634** | 🔴 **0** | 🟡 `tests-only` | no CI configuration at HEAD |
| [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 🔴 **1 996** | 34 · 🔴 **travis** | 🔴 `fossil-ci` | 34 configs for a dead service (`P111-D`) |
| [`EducationalTestingService/factor_analyzer`](https://github.com/EducationalTestingService/factor_analyzer) | 702 | 1 · gitlab | 🟡 `partial` | no PR trigger |

🔴 **45 rows (15.2 % of the shelf) are `tests-only`: a suite committed, and no CI
configuration of any kind at HEAD. `kuali/rice` and `OpenOLAT/OpenOLAT` are both major
institutional platforms, and between them they carry 3 425 test files that no pipeline
on this shelf is configured to run.**

🟢 **That is an OPPORTUNITY line, not just a defect: wiring an existing 1 600-file suite
into GitHub Actions is days of work, it is the kind of contribution upstreams accept,
and it converts a `tests-only` platform into a `checked` one for whoever does it.**

---


**Pass 110, 2026-10-10.** ⏱️ **Twentieth pass of this date.**

🟢 **`busfactor.sh` read **296 of 296** addresses, zero unread
(`compose/code/p110-bus-factor/`, `test_p110.sh` 46 passed / 0 failed, fully offline).**

🔴 **"Foundational" has been a licence-and-liveness claim on this page for 110 passes.
This pass gives it a bench test, and the foundation layer shrinks to **11 rows** —
3.7 % of the shelf.**

### 🟢 🆕 `P110-J` — the only rows that are both institution-backed and alive

🔵 **`broad` = `bus_factor` ≥ 6: no five people can walk away and stall it. Paired with
p109's `fresh` band (commit within 30 d), these eleven are the shelf's actual
foundation:**

| repo | licence | `bus_factor` | top author | authors | p109 |
|---|---|---|---|---|---|
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | 🟢 16 | 🟢 11 % | 373 | 🟢 fresh 0 d |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 Apache-2.0 | 🟢 11 | 🟢 12 % | 70 | 🟢 fresh 1 d |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 MIT | 🟢 11 | 🟢 10 % | 51 | 🟢 fresh 0 d |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 9 | 🟢 13 % | 319 | 🟢 fresh 7 d |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟢 7 | 🟢 17 % | 249 | 🟢 fresh 1 d |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟡 AGPL-3 | 🟢 7 | 🟢 13 % | 62 | 🟢 fresh 10 d |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | 🟢 CC0-1.0 | 🟢 6 | 🟢 29 % | 46 | 🟢 fresh 6 d |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 GPL-2 | 🟢 6 | 🟢 14 % | 47 | 🟢 fresh 3 d |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 Apache-2.0 (ECL-2.0) | 🟢 6 | 🟢 21 % | 198 | 🟢 fresh 1 d |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | 🟢 6 | 🟢 14 % | 37 | 🟢 fresh 0 d |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟡 AGPL-3 | 🟢 6 | 🟢 15 % | 58 | 🟢 fresh 2 d |

🔵 **Licences are carried from this page's prior passes; this pass changed no licence
reading and discovered no new repository. It added one column.**

### 🔴 🆕 `P110-M` — four repos this page has called foundational have a wide bench that stopped showing up

| repo | `bus_factor` | authors | p109 liveness |
|---|---|---|---|
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | 🟢 21 | 232 | 🔴 **dormant 383 d** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟢 12 | 66 | 🟡 **slowing 163 d** |
| [`project-sunbird/sunbird-devops`](https://github.com/project-sunbird/sunbird-devops) | 🟢 8 | 97 | 🔴 **abandoned 1 263 d** |
| [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | 🟢 7 | 57 | 🟡 **slowing 291 d** |

🔵 **These are the inverse of the shelf's usual failure. Breadth is not the problem —
`kaldi` has 232 authors and the widest bus factor on the shelf — the problem is that
the bench has left.** 🟢 **A wide, cold repo is the best FORK candidate on this shelf:
the code was reviewed by many and nobody will contest the fork. A narrow, warm repo is
the opposite.**

### 🟡 🆕 `P110-D` — a figure on this page that must NOT be compared across rows

🔴 **`commits_read` ranges from 200 to 16 946 at the same `--depth=200`, because git's
`--depth` is a GENERATION limit and each generation of a merge-heavy history branches.**
🟢 **So no claim on this page rests on commit counts. `bus_factor` and `top author %`
are both ratios WITHIN a row and are the only cross-row-comparable figures the
instrument emits.**

# Education — foundational repos

**Pass 109, 2026-10-10.** ⏱️ **Nineteenth pass of this date.**

🟢 **`freshness.sh` read **296 of 296** addresses, zero unread
(`compose/code/p109-freshness/`, `test_p109.sh` 32 passed / 0 failed, fully offline).**
🔵 **Every foundation row below gains the figure that says whether anyone still works on
it.** 🔴 **`Gap 376` — a maintenance signal, owed since pass 92 — is **DISCHARGED** here,
on the axis it actually named, after two passes answered adjacent questions.**

### 🟢 🆕 p109 — foundations, with liveness beside the pin

| repo | licence | `class` | pin | last commit | age | band |
|---|---|---|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `semver` | `v3.5.3` | 2026-10-10 | **0 d** | 🟢 fresh |
| [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3 | `prefixed` | `dspace-10.1` | 2026-10-10 | **0 d** | 🟢 fresh |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 GPL-3 | `semver` | `v3.0.1` | 2026-10-09 | **0 d** | 🟢 fresh |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | `prefixed` | `OpenOLAT_21.0.3` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 | `semver` | `25.2` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `semver` | `v0.19.5` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 AGPL-3 | `semver` | `v2.1.0` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 LGPL-3 | `semver` | `v3.0.39` | 2026-10-08 | **2 d** | 🟢 fresh |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | `semver` | `v5.3.0` | 2026-10-03 | **7 d** | 🟢 fresh |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 LGPL-3 | 🔴 `stamp` | 🔴 SHA only | 2026-09-07 | **33 d** | 🟢 active |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 | `semver` | `1.28.0` | 2026-08-11 | **60 d** | 🟢 active |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🟡 AGPL-3 | `semver` | `v5.14.2` | 2026-04-30 | 🟡 **163 d** | 🟡 slowing |
| [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 MIT | `semver` | `v3.8.2` | 2026-03-24 | 🟡 **200 d** | 🟡 slowing |
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 ECL-2.0 | `semver` | `rice-2.6.0` | **2017-05-17** | 🔴 **3 433 d** | 🔴 **abandoned** |

🔴 **Twelve of the fourteen are fresh or active. Two are not, and both were being
recommended.** 🔴 **`kuali/rice` has not been touched in **nine years and five months**.
`instructure/canvas-lms` and `tunapanda/h5p-standalone` are both `slowing` — and both
default-branch readings were re-confirmed against a live `ls-remote --symref` this pass
(each defaults to `master`), so neither figure is a branch artefact.**

🟡 **The `h5p-standalone` reading is the uncomfortable one. p108 promoted it over the
GPL-3 H5P core precisely because it is MIT — and on liveness the MIT substitute (200 d)
is the WEAKER of the two: the GPL core it replaces is 60 d, `active`.** 🟢 **The licence
argument for `h5p-standalone` is unchanged and still correct; the maintenance argument now
runs the other way, and an engagement should be told both.**

### 🔴 🆕 p109 — 24 rows p108 called pinnable have been dead for over a year

🔵 **p108's axis (`class`) and p109's axis (liveness) are independent, and crossing them
is where the shelf's real size appears:**

| | 🟢 pinnable (`semver`/`prefixed`) | 🔴 SHA-only (`none`/`stamp`) |
|---|---|---|
| 🟢 fresh (≤30 d) | 🟢 **99** | 45 |
| 🟢 active (31–90 d) | 🟢 **20** | 14 |
| 🟡 slowing (91–365 d) | 25 | 27 |
| 🔴 dormant (1–2 y) | 🔴 **7** | 11 |
| 🔴 abandoned (>2 y) | 🔴 **17** | 31 |
| **total** | **168** | **128** |

🟢 **The tier Globant can actually build on is the top-left pair: pinnable AND still
worked on — **119 of 296, 40.2 %**.** 🔴 **Not 296, and not p108's 168.**
🔴 **24 of those 168 (14.3 %) are dormant or abandoned: p108 ranked them pinnable and had
no way to see they were dead.** 🟡 **45 rows are the mirror image — fresh but with no
version to pin: motion without shipping.**

### 🔴 🆕 p109 — the 17 abandoned-but-pinnable rows, named

🔵 **Stated in full because a pinnable row reads SAFE on every axis this KB had before
today, and these are the rows an engagement would have reached for:**

| repo | pin | last commit | age |
|---|---|---|---|
| [`adlnet/SCORM-to-TLA-Roadmap`](https://github.com/adlnet/SCORM-to-TLA-Roadmap) | `v1.0` · 🔴 **ARCHIVED** | 2017-01-24 | 🔴 3 546 d |
| [`kuali/rice`](https://github.com/kuali/rice) | `rice-2.6.0` | 2017-05-17 | 🔴 3 433 d |
| [`IMSGlobal/caliper-spec`](https://github.com/IMSGlobal/caliper-spec) | `1.1.0` | 2019-05-06 | 🔴 2 714 d |
| [`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | `1.2.3` | 2020-02-06 | 🔴 2 438 d |
| [`moodlehq/moodle-tool_dataprivacy`](https://github.com/moodlehq/moodle-tool_dataprivacy) | `34.9.0` · 🔴 **ARCHIVED** | 2020-06-16 | 🔴 2 307 d |
| [`kualico/rice`](https://github.com/kualico/rice) | `2.7.2` | 2020-07-01 | 🔴 2 292 d |
| [`openfun/xblock-proctor-exam`](https://github.com/openfun/xblock-proctor-exam) | `v1.0.0` | 2021-02-11 | 🔴 2 067 d |
| [`Jasig/SSP`](https://github.com/Jasig/SSP) | `ssp-2.9.0` | 2021-07-26 | 🔴 1 902 d |
| [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | `v0.6.0` | 2021-11-10 | 🔴 1 794 d |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | `v7.1.1` | 2021-11-16 | 🔴 1 789 d |
| [`anaistack/cefr-asag-corpus`](https://github.com/anaistack/cefr-asag-corpus) | `v1.0.1` | 2021-12-17 | 🔴 1 758 d |
| [`eribean/girth`](https://github.com/eribean/girth) | `v0.8.0` | 2022-01-30 | 🔴 1 713 d |
| [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | `v9.23.0` | 2022-12-30 | 🔴 1 380 d |
| [`atutor/ATutor`](https://github.com/atutor/ATutor) | `Atutor_1.4.1` | 2023-02-12 | 🔴 1 336 d |
| [`project-sunbird/sunbird-devops`](https://github.com/project-sunbird/sunbird-devops) | `release-6.0.0` | 2023-04-26 | 🔴 1 263 d |
| [`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml) | `v2.1.0` | 2023-05-05 | 🔴 1 254 d |
| [`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials) | `2.0.6` | 2024-02-02 | 🔴 981 d |

🔵 **Seven more are `dormant` (1–2 years): `EducationalTestingService/skll` and
`/rsmtool` (both 652 d), `/factor_analyzer` (627 d), `leemonade/leemons` (611 d),
`sukhrobyangibaev/mcp_hemis_student` (572 d), `nestauk/ojd_daps_skills` (488 d),
`adlnet/ADL_LRS` (484 d).**

### 🟡 🆕 p109 — Caliper: the rename hypothesis, tested and REFUTED

🔵 **`IMSGlobal/caliper-spec` reads 2 714 days abandoned, and the obvious innocent
explanation is that IMS Global renamed itself 1EdTech and the old address is a stale
mirror.** 🔴 **Probed: `1EdTech/caliper-spec` resolves to the SAME repository — GitHub
redirects the old owner — and carries the identical date, `2019-05-06`.** 🔴 **So Caliper's
specification repository really has been untouched for seven years and five months, under
either name.** 🟡 **The five other `caliper-*` addresses this KB's trending history cites
(`caliper-java`, `-js`, `-php`, `-python`) came back **UNREAD** over this channel, so
nothing is claimed about them either way — an unread row is unread (`P1040`).**
🟢 **By contrast `1EdTech/openbadges-specification` is **2 d, fresh**: the organisation is
alive, this one specification is not.**

### 🟢 🆕 p109 — the address list is CLOSED over this KB's live pages

🔵 **Before trusting a 296 denominator, it is worth asking whether 296 is the whole
shelf.** 🟢 **Every `github.com/owner/repo` reference on the six live non-trending pages
was extracted and diffed against `addresses.txt`: **297 cited, 296 censused**, and the
single residual is the literal string `owner/repo` from a prose example.** 🟢 **So the
denominator is right and no live page points at a repository this census never read.**

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
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` | 🟢 **23 / `v1.14.0`** ⚠️ **was 26 tags**<!--corrected--> | 🟢 **Foundational.** Permissive **and** released; 40+ tools over the Canvas API. |
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
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **Apache-2.0** · 11 324 B · `master` · `ea17c40` · 🔴 **ARCHIVED** | 42 | **North America** (US DoD / ADL) | The authoritative SCORM → xAPI statement mapping. The audit-trail spec. |
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
| 🆕 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | 443 | 🔵 unplaced | 🟢 **The reference deep-knowledge-tracing benchmark library** (NeurIPS 2022 datasets-and-benchmarks track, `pykt.org`). Standardised preprocessing plus a model zoo — **DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT** — over 7 datasets. 🔵 **This is the missing layer, not another tutor:** it turns "the agent remembers the conversation" into **a per-skill mastery estimate you can threshold on**, which is what adaptive sequencing and mastery-gated progression actually need. MIT, so it can sit inside a paid deliverable. |
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
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | 443 | 🔵 unplaced | 🟢 Deep knowledge tracing: DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT over 7 datasets (NeurIPS 2022). **Carried from pass 92 at its pass-92 SHA; not re-read this pass.** 🔵 Read it as the research ceiling, and `pyBKT` as the deliverable floor. |

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
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | 🟢 **Apache-2.0** · 11 324 B · 🔴 **ARCHIVED** | 42 |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** · 11 357 B | — |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **no payload / 24** · `master` · `3e532b8` · 🔴 **ARCHIVED** | 99 |
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
