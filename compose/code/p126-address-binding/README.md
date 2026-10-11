# `p126-address-binding` — ACTION AJ, AK, AL, AM

**Pass 126 — 2026-10-11.** Thirteenth pass of this date (census window **11:4x → 12:1x UTC**).

`./test_p126.sh` — **20 passed / 0 failed**, fully offline, no network and no clock. Every
markdown fixture is a real construction copied off this KB's own live pages; `al-learnpress-readme.txt`
carries the real plugin-header bytes of [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress).

## What p125 pre-registered, and what happened

| action | clause (verbatim from p125) | verdict |
|---|---|---|
| `ACTION AJ` | bind a licence token to an ADDRESS, not to a line. *Refuted if fewer than 12 of the 15 are explained by mis-binding* | 🔴 **DISCHARGED, REFUTED — 0 of 15.** The mechanism is real and now implemented; it explains none of the 15 |
| `ACTION AK` | give the correction apparatus p123's grant-as-a-SET. *Refuted if treating the old and new values as SETS does not clear all 6* | 🟢 **DISCHARGED, NOT REFUTED — 6 of 6 cleared** — but only when composed over `AJ`. Alone it launders 9 live false claims |
| `ACTION AL` | extend the grant path list by `LICENSE.GPL`/`LICENSE.MPL` and the WordPress `readme.txt` header. *Refuted if fewer than 3 "genuinely absent" addresses turn out to carry a grant* | 🔴 **DISCHARGED, REFUTED — 1 of 3**, and that one was already known to this KB |
| `ACTION AM` | mark at WRITE time instead of sweeping afterwards. *Refuted if a write-time check cannot reproduce ≥ 90 % of the 81 rows* | 🟢 **DISCHARGED, NOT REFUTED — 81 of 81 = 100 %** |

## 🔴 `P126-A` — the committed evidence cannot be found again on the committed pages

p125 committed `out/ac-after.triples`: 36 `path:line|address|token` records, the residue of its
own `ACTION AC` assertion. **Not one of those 36 line numbers names the address it is filed
under.** The cause is not drift and not a bug in the recogniser — it is ordering. p125 measured
the pages, then **prepended its pass section to each page it had just measured**, and every
coordinate below the insertion moved down by the length of that section.

| page | p125 section length | recorded → true |
|---|---|---|
| `agents/top.md` | **58** lines | `163` → **221** (`pupilfirst`, CC-BY-SA-4.0) |
| `intel/market.md` | **63** | shift `+63` across all 4 of its records |
| `intel/trends.md` | **33** | shift `+33` across both |
| `intel/open-gaps.md` | **186** | shift `+186` across all 4 |

The finding is not that the claims were wrong. **Relocated by `(page, address, token)` all 15 of
`AJ`'s set are found, 0 unlocatable** — the same claims, at coordinates the pass itself
invalidated. It is the lineage's own pattern one level up: p122 found a census less precise than
the page, p123 a repair that was an edit, p124 a token read without its scope, p125 an assertion
run without its domain, and p126 finds **evidence keyed on a coordinate the pass does not
preserve.** So this instrument's own `out/` is keyed on `(page, address, token)`, never on a line.

## 🔴 `P126-B` — one unreadable column heading, and the table reporting three false claims is itself unmarked

Recomputed on the committed pages with p125's own code, the assertion returns **49** violations,
not the 36 reported. **12 of the 49 sit inside p125's own section** — the single largest bucket by
pass. Attributed with each page's `**Pass NNN,` datelines:

| pass section | violations |
|---|---|
| 🔴 **p125** | 🔴 **12** |
| p122 | 6 |
| p93 | 5 |
| p118 | 4 |
| p120 / p116 / p104 | 3 each |

The cause is one heading. `P125-A`'s defect table — the table reporting the three live false
claims — is headed

```
| # | where | the page said | the file says | how it was missed |
```

and `HDR_OLD` carries `this KB said`, `KB said` and `pNNN said` but **not `the page said`**. So
`classify_header` returns `None`, the table is not a correction table to the apparatus, its quoted
OLD values read as live claims, and the assertion re-raises them on each of the **6** pages the
table was copied onto. 🔵 **p125 invented a new column spelling in the same commit that shipped
the sweep for forms 1–13** — which is `ACTION AM`'s argument restated as a fact rather than a
prediction.

**Repaired:** three spellings added to `HDR_OLD` (`the page said`, `the {shelf,row,cell,table}
said`, `as published`), after which p125's own writer reaches the rows. **6 rows marked, form 2,
one per page.** Rows 2 and 3 of that table are correctly *not* hits: row 2's old value `MIT` is
also a new value (for `pyBKT`), and row 3's old cell carries no licence token at all.

## 🔴 `P126-C` — `AJ` and `AK` are one mechanism, and neither works alone

The 15 violations `ACTION AF` newly surfaced decompose exhaustively, and **mis-binding explains
none of them**:

| n | class | why |
|---|---|---|
| **6** | `pupilfirst/pupilfirst` CC-BY-SA-4.0 | `AK`'s class — a split grant collapsed to one token, so the surviving member reads as superseded |
| **4** | `oat-sa/tao-core` LGPL-3.0 | unmarked correction apparatus: a quoted retraction and an old column whose header was not read |
| **3** | `canvas-lms`, `edx-platform` `GPL` | 🔴 **SUBSTRING**, not binding — see below |
| **2** | `1EdTech/openbadges-specification` Apache-2.0 | the referent is *"the validator"*, named in prose and not as an address, so binding structurally cannot reach it |

🔴 **The 3 are `ACTION AG`'s own SUBSTRING class, recurring in a function `AG` never reached.**
`repair_search.violations` tests `re.escape(tok)` between word boundaries instead of the
vocabulary, and `\bGPL\b` matches inside `GPL-3.0`. Line 524 of `compose/patterns.md` carries no
bare `GPL` at all — the vocabulary reads `GPL-3.0` and `AGPL-3.0`. `AG` guarded token *reading*
(`marked_regions`, `label_span`); the violation *check* was outside it.

🔴 **And `AK` cannot be implemented without `AJ`.** An address-level survivor set must be fed by
*bound* tokens, not co-occurring ones. `compose/patterns.md` carries

```
| mastery | `CAHLR/pyBKT` + `douglasrizzo/catsim` | 283 + 153 |
| 🟢 **MIT** (`pyBKT`) + **BSD-3-Clause** (`catsim`) ⚠️ **was 🟢 MIT both**<!--corrected--> |
```

and an unbound union hands `MIT` — true of `pyBKT` — to `catsim` as a surviving member. That
clears `catsim`'s superseded `MIT` on **9** live rows: the defect p125 called *the one worth the
pass*, re-opened by its own remedy.

| run | `pupilfirst` rows cleared (wanted 6) | `catsim/MIT` rows kept (wanted 9) | verdict |
|---|---|---|---|
| `AK` alone (`--no-bind`) | 🟢 6 | 🔴 **0 — laundered** | 🔴 refuted |
| 🟢 **`AK` over `AJ`** | 🟢 **6** | 🟢 **9** | 🟢 **not refuted** |

So `AJ` is refuted as a **cause** and indispensable as a **mechanism**, and those are not
opposites. The binder needed three rules, in priority order:

1. 🟢 **short name** — a backticked identifier within 30 characters of the token matching an
   address's owner or repository name. This is the only rule that resolves the `pyBKT`/`catsim`
   row; the cell rule and the distance rule both get it wrong.
2. 🟢 **ordinal pairing** — k addresses in one cell and k tokens in another pair by position
   (`` `moodle` *or* `canvas-lms` | GPL-3.0 / **AGPL-3.0** ``).
3. 🟢 **cell wall, then nearest address** — a token binds only inside its own cell; if its cell
   names none, to the row's subject.

Composed, the assertion falls from **49** violations over 23 addresses to **27** over 13.

## 🔴 `P126-D` — two writers ship side by side and nothing says which is live

`compose/code/p125-retraction-cue/` contains **two** `apply_marks`: one in `correction_form.py`
and one in `mark_forms.py`. Only the second carries the `APPARATUS` guard and the cue model.
Nothing in the directory marks the first as superseded.

🔴 **This pass used the wrong one and published a false number before catching it.** Measured
against `correction_form`, `ACTION AM` reproduced **41 of 81 = 50.6 %** and the conclusion was
that 40 marks had no provenance in the repository. Measured against `mark_forms` — p125's actual
writer — it reproduces **81 of 81 = 100 %, per page exactly**, and `AM` is not refuted.

| writer | proposes on p125's own committed pages | APPARATUS guard |
|---|---|---|
| 🟢 `mark_forms.apply_marks` | **0** — converged, as p125 claimed | 🟢 yes |
| 🔴 `correction_form.apply_marks` | 🔴 **50** | 🔴 none |

Run with `P126-B`'s header patch, the superseded writer marks p125's own prose *about* the
marker — *"(`⚠️ **was 🟢 MIT**` inside the cell)"* — which is exactly the false-positive class
p125's fourth defect fixed. Two such lines were written and reverted before `repair.py` was
pointed at `mark_forms`; `AM.5` now pins both numbers so the hazard cannot be hit silently again.

🔵 **The lesson is the pass's own:** p125 was measured against an instrument that did not produce
its output. A reproduction claim is only as good as the identification of what it reproduces, and
a directory that ships two writers without saying which is live invites exactly this error.

## 🔴 `ACTION AL` — a blind spot with nothing behind it

`ACTION AI` inferred the toolchain was blind to two conventions. Both were added and probed over
**32** candidate addresses × **21** paths = **672 probes**, every one reading the repository's own
bytes on its real default branch (`raw.githubusercontent.com` resolves `HEAD`, so no branch is
guessed). **200 × 3, 404 × 669, and zero `000`/`403` — no proxy noise.**

| path class | probes | grants found |
|---|---|---|
| 🔴 `LICENSE.GPL`, `LICENSE.LGPL`, `LICENSE.MPL`, `LICENSE.APACHE`, `LICENSE.BSD` | **160** | 🔴 **0** |
| 🟢 `readme.txt` / `README.txt` / `Readme.txt` (WordPress plugin header) | 96 | 🟢 **1** — `LearnPress/learnpress`, `License: GPLv3` at line 7 of 41 951 B |

🔴 **The clause needed 3 and got 1, and this KB already knew that one** — it is `P125-A`'s own
defect 3. The dual-licence filename convention does not occur anywhere in this corpus's no-grant
set. 🟢 **The extended path list is still correct to keep**: it is the right convention and it
costs nothing. The honest statement is that it has no further yield here.

🔵 **Two caveats on the candidate set, both from its own output.** It was harvested by text search
for no-grant language, which over-captures: 2 of the 3 hits — `moodle/moodle` (`COPYING.txt`) and
`celtic-project/LTI-PHP` (`LICENSE`) — are addresses the corpus never claimed were grantless, and
`AL`'s literal subject, the **18 "genuinely absent"** addresses of p123's `ACTION Y`, are
repositories that **do not exist**. A 404 repository cannot carry a grant on any path, so that
reading of the clause is vacuous and the operative set had to be the exists-but-unread one.

## What is measured, and where

| file | what it carries |
|---|---|
| `binding.py` | the three binding rules, and `is_substring_only` |
| `grant_set.py` | the address-level survivor set; `--no-bind` reproduces the laundering |
| `composed.py` | the assertion restated once, with both |
| `relocate.py` | `P126-A`'s dislocation census |
| `section_origin.py` | attribution of each violation to the pass section it lives in |
| `reproduce_marks.py` | `AM`'s reproduction, against `mark_forms` |
| `write_time.py` | `AM`'s LINE / BLOCK context decomposition |
| `repair.py` | the three added header spellings, applied with p125's own writer |
| `probe_paths.sh` | `AL`'s 672-probe grant-path census |
| `out/` | every number above, keyed on `(page, address, token)` and never on a line |

## Pre-registered for p127

🟢 **`ACTION AN`** — give `repair_search.violations` the vocabulary instead of `re.escape(tok)`, so
a family token cannot match inside a precise one, and re-run the whole lineage's baselines. 🔴
*Refuted if fewer than the 3 `GPL` records this pass classified as SUBSTRING are removed, or if
any of the other 24 live violations disappears with them.*

🟢 **`ACTION AO`** — mark the superseded writer as superseded. Add a module-level refusal to
`correction_form.apply_marks` naming `mark_forms.apply_marks` as the live one, and assert that no
instrument in `compose/code/` calls the former. 🔴 *Refuted if any pass's committed instrument
turns out to depend on it.*

🟢 **`ACTION AP`** — bind a token to a referent named in PROSE, not as an address. The 2
`openbadges-specification` records are *"the spec carries no grant while the validator is
Apache-2.0"*, and the validator is a real, separate, published address in this corpus. 🔴
*Refuted if fewer than both are resolved by matching a prose noun phrase to an address this KB
already publishes.*

🟢 **`ACTION AQ`** — the 8 remaining `catsim/MIT` rows. All sit on append-only pages or in the
`"MIT both"` quantifier cell, where a repair may not rewrite. Decide and record the rule: does an
append-only page carry a correction *annotation* without being rewritten? 🔴 *Refuted if the rule
cannot be applied without editing a single historical claim.*
