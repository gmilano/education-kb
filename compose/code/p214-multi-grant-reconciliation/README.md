# p214 — `ACTION PZ`: multi-grant reconciliation across the client-facing shelves

Discharges `ACTION PZ`, registered by p211 with falsifiers.

`P211-1` found that **6 of 7** wrong licence cells named a repository whose correct
grant this KB had already published somewhere else, and concluded: *"the dominant
failure mode of a large append-only knowledge base is not getting the answer wrong.
It is getting it right once and leaving the stale cell standing."* `PZ` prices that
backlog by asking a question that needs no network at all: **which repositories does
this KB print two different grants for?**

## The one decision that makes the measure honest

A row printing two licence tokens is **not** a contradiction. On these shelves it is
usually a **correction-trail** row, which prints the wrong value and the right value
side by side *on purpose* — `axe-core │ GPL │ MPL-2.0` is this KB working correctly.
Counting those would manufacture findings out of its own integrity work.

So `PZ` adjudicates **unambiguous cells only**: a row naming exactly one repository
and exactly one licence family. **140 multi-token rows are excluded by construction.**

## Result

`8` of `518` repositories print more than one grant family → **limb 2 fires** (`<10`).
The propagation backlog is small. Two further readings matter more than the count:

| | |
|---|---|
| **`8` of `8`** sit on the **GNU axis** | `P211-3` measured `5` of `7`; on this independent measure it is total |
| **`6` of `8`** are real | `4` repositories with genuinely wrong cells, `2` recovered from `ABSENT` |
| **`2` of `8`** are **false positives of this script** | see below — recorded, not hidden |

### `GibbonEdu/core` — the finding, and its mechanism

`4` cells published `AGPL-3.0`; the grant is **`GPL-3.0`**, agreeing on three
independent channels (`LICENSE` title line, `composer.json` `"license"`, `README` l.81).
One cell had hardened the error as *"not `GPL`, as secondary sources say"* — exactly
backwards.

**The mechanism:** `GPL-3.0` **§13 is titled "Use with the GNU Affero General Public
License"**, and the word `Affero` appears **3 times** in the blob (lines `552`, `556`,
`559`). A whole-body matcher reads `GPL-3.0` as `AGPL-3.0`.

This is the defect p205/p211's **"title window only"** rule exists to prevent — the
mirror image of the documented `odoo` trap, where an `LGPL` blob embedding `GPL` text
reads as `GPL`.

**And none of that is new.** `P171` documented this exact mechanism and stated outright
*"Gibbon es `GPL-3.0`"*, having caught its own instrument one commit from publishing the
wrong correction. `P205` turned it into the title-window rule. The four cells stood
regardless. **A rule does not retroactively clean the cells written before it.**

`ACTION QF`, registered for p215 and then run in this pass because it is one `grep`,
found the same for **3 of the 4** wrong-cell repositories — `GibbonEdu` (`P171`), `certo`
(p98, same bytes and sha), `frappe/lms` (the listicle correction). Only `MoFaCTS` was new.
**The contradiction backlog is small (limb 2); the propagation failure rate inside it is
~80% across two independent samples.** That is what `ACTION QG` is registered to fix: make
the correction, not the discovery, the unit of work.

### The false-positive mode, stated so the next pass does not re-find it

`bigbluebutton` and `odoo` appear to contradict themselves and do not. Both tokens sit
in a table *about licence-text structure* — *"`GPL-3.0` by **reference**"*,
*"`GPL-3.0` included by **value**"* — describing how `LGPL-3.0` is published. **A
licence token in prose about licence text is not a grant claim.** Both cells are
correct and were left untouched.

Any future column audit over these shelves needs this exclusion, or it will report
two standing findings that are not there.

## Usage

```sh
python3 -I reconcile.py pz-contradictions.json
```

Entirely offline: the shelves and the p211 census are both on disk. The blob re-reads
that confirmed every verdict used `raw.githubusercontent.com`, which answers `200`.

## Regression check, run after the corrections landed

Re-running `reconcile.py` over the corrected shelves:

```
repos printing >1 distinct grant family : 2   (was 8)
  bigbluebutton/bigbluebutton   blob=LGPL-3.0
  odoo/odoo                     blob=LGPL-3.0
```

**8 → 2, and the 2 survivors are exactly the two documented false positives** — the
blob-structure table that prints *"`GPL-3.0` by reference"* and *"`GPL-3.0` included by
value"*. Nothing else on the four shelves now prints two grants for one repository.

This is the property that makes the script usable as `ACTION QG`'s write-time gate: it
returns to a known, explainable floor rather than to zero, and the floor is documented
here so a future pass does not "fix" two correct cells.
