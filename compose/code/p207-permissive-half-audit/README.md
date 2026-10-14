# p207 — the permissive half of the licence column, and four more instrument defects

`ACTION PI` (p206) audited **the copyleft half** of this KB's licence column: 281 repositories
carrying a copyleft token in a published table row. It found **0 wrong cells**. `ACTION PB`
(p205) audited the 60 highest-★ rows and found **0 wrong cells**. Both passes concluded that the
column was sound and the instrument was not.

p207 audited **the other half** — the 199 rows published with a *permissive* family token — and
found **0 wrong cells** — and two false positives better than any this KB has recorded.

## Why the half matters — and the prior it refuted

A row published as **copyleft** is a row someone was being careful about. Nobody over-claims
restriction: there is no upside to printing `AGPL-3.0` on an MIT repository, so that half of the
column is self-correcting. A row published as **permissive** is the one with upside to being
wrong: `MIT` is what a hurried reader wants a row to say.

That was the hypothesis, and it is **wrong**. The permissive half is as clean as the copyleft
half.

| pass | population | method | reported | **true** | false |
|---|---|---|---|---|---|
| p205 | 60 highest-★ rows | regex over the licence column | 3 | **0** | 3 |
| p206 | 281 copyleft rows | table-row extraction, blobs at `HEAD` | 3 | **0** | 3 |
| **p207** | **199 permissive rows** | **blob-first, fixed instrument** | **18** | **0** | **18** |

**Three consecutive passes. Three populations. Three methods. 24 reported, 0 true.** `Gap 467`
is no longer a suspicion about one method — it is a measured property of auditing this column.

## The false positives got MORE seductive, not less

p206's false positives were incidental: a university named `MIT`, a vendored third-party file.
p207's two best candidates were neither. Both were rows whose **prose is specifically about a
licence divergence** — which is why the word `MIT` appears in them at all:

| repo | what the audit saw | what the KB actually publishes |
|---|---|---|
| [`ShuyunYuan/talentcoach`](https://github.com/ShuyunYuan/talentcoach) | row mentions `MIT`; blob reserves all rights | 🔴 **VIEW-ONLY / DO-NOT-USE**, and the KB had already written up *"its view-only negation of `MIT`'s verb list"* and the verbatim-copied MIT warranty paragraph |
| [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | row mentions `MIT`; blob is a `CC-BY-NC-SA-4.0` deed | 🔴 **`CC-BY-NC-SA-4.0`**, with `package.json` says MIT vs the licence FILE recorded as *"the divergence IS the row"* (`P204-1`) |

A third, [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph),
is the KB's own `P965`: *a file at a licence filename can be a FRAMEWORK, not a grant.*

🔴 **The rows that look most like findings are the rows where the curation already happened.**
An automated reader rediscovers the KB's subject matter and reports it as an error. Had p207
published its first draft, it would have overwritten three correct, hard-won cells with two
wrong ones and a redundant one.

**The operational rule stands and is now cheap to state:** adjudicate against the published CELL
*and the prose around it* before reporting a mismatch — and when a flagged row's prose is about
licensing, assume the row is the finding, not the error.

## The four instrument defects, each reproduced on a real body

| # | defect | p206 returns | truth | fixture |
|---|---|---|---|---|
| D11 | the dot in `cc0 1\\.0 universal` is **double-escaped**, so the CC0 title line never matches and every CC0 body falls to the body fallback | `CC-unversioned` | `CC0-1.0` | `0voice/Awesome-CS-OpenCourse`, `brootware/…`, `O0000-code/…` |
| D12 | `bsd [0-9]-clause` is in `TITLE_RE` but has **no arm in the title `case` block**, so a titled BSD-3 body falls through to the body fallback | `BSD-2-Clause` | `BSD-3-Clause` | `fixtures/bsd3.txt` |
| D13 | `attribution-noncommercial` is tested **before** any ShareAlike check, and the deed branch tests `/by-sa/` and `/by-nc/` but never `/by-nc-sa/` | `CC-BY-NC` / `CC-unversioned` | `CC-BY-NC-SA-4.0` | `cccareers/open-source-curriculum` |
| D14 | a **rider** amends the licence below it, so it cannot be found by anchoring on a title line — the title line belongs to the licence being restricted | 🔴 `MIT` | `NON-OSI-CommonsClause+MIT` | `fixtures/commons-clause-mit.txt` |

**D14 is the one to read twice.** `T206-4` called `UNRECOGNISED` on a non-OSI family *"the single
worst failure mode a licence reader has"*. D14 is worse. A Commons Clause body returns a
**confident, clean `MIT`** — no suffix, no flag, nothing to notice. `UNRECOGNISED` at least asks
to be looked at.

D14 is also **structural, not incidental**: p205's fix was to anchor on the title line and p206's
was to undress it. The better that anchoring gets, the more reliably it finds the *inner* licence
and misses the rider sitting above it. So the rider check must run **before** the title walk, and
it does — `classify_grant` tests `rider_token` at step 0 and reports both halves.

Three of these four defects are in the **lookup table**, not the anchoring logic. p205 and p206
both repaired how the title line is *found*; nobody had re-read what it is matched *against*.

## L1 — the locator has the same disease, one level up

`raw.githubusercontent.com` is case-sensitive, and this KB's path lists have always been
fixed-case enumerations. [`openedx/XBlock`](https://github.com/openedx/XBlock) — `Apache-2.0`,
11 358 B, in this KB's own foundations table — spells its file **`LICENSE.TXT`** and returns
`404` on all 22 path forms p206 used. p207's first probe duly recorded it as ungranted.

p206 fixed everything the *title line* can be wearing. The **filename** can wear the same costume,
and `licence_paths()` in [`locate.sh`](locate.sh) enumerates 10 bases × 9 extensions = 90 forms.

After the re-probe: 15 apparent absences → **3 recovered** (`LICENSE.TXT`, `license.txt`,
`License`), **2 NOTICE-only** (p206's `D7` — a channel, not a body), **12 true absences** at 90
path forms. **An absence is only reportable after the case variants have been tried.**

## Running it

```sh
./test_classify.sh     # 12/12, no network
```

`classify.sh` is a drop-in replacement for
[`../p206-classifier-language-shape/classify.sh`](../p206-classifier-language-shape/classify.sh);
every p205 and p206 repair is kept and guarded by a regression fixture.

Evidence: [`permissive-half-census`](../../../evidence/permissive-half-census.2026-10-14-p207.tsv) ·
[`licence-locator-case`](../../../evidence/licence-locator-case.2026-10-14-p207.tsv) ·
[`byte-cell-conflicts`](../../../evidence/byte-cell-conflicts.2026-10-14-p207.tsv)
