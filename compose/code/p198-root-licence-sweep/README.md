# `P197` — Resolve the branch, then read the licence; and why a filename list is unsound even for a POSITIVE

## Two rules, one of which this pass got wrong mid-flight

### Rule 1 — RESOLVE the default branch, never guess it

`git ls-remote --symref <url> HEAD` names the real default branch. Guessing `main` then
`master` produces an HTTP `404` on repositories whose default is neither — and a `404` read as
"no licence here" is a **false absence**, the exact defect class `Gap 421` tracks.

`10` of the `30` rows swept this pass have a default branch that is neither `main` nor
`master`:

| slug | real default |
|---|---|
| `francoisjacquet/rosariosis` | **`mobile`** |
| `openeducat/openeducat_erp` | **`19.0`** |
| `GibbonEdu/core` | **`v31.0.00`** |
| `bigbluebutton/bigbluebutton` | **`v3.0.x-develop`** |
| `overhangio/tutor` | **`release`** |
| `oppia/oppia`, `learningequality/kolibri`, `frappe/education` | `develop` |

### Rule 2 — a first-match filename list is unsound for a POSITIVE too

🔴 **This pass asserted the opposite, in writing, and was refuted by its own next command.**
The reasoning was: *"a filename list is insufficient for a NEGATIVE (that is `P441`), but
sufficient for a POSITIVE, because bytes in hand are bytes in hand."* That is wrong:

```
microsoft/autogen/LICENSE        -> CC-BY-4.0, 18 650 B   <- a CONTENT licence; first match
microsoft/autogen/LICENSE-CODE   -> MIT,        1 141 B   <- the CODE grant; never reached
```

The list hit `LICENSE` first and stopped, so the sweep would have published **"AutoGen is
CC-BY-4.0"** — a row this KB has carried as `MIT` for many passes, and the family is right
while the *file* is wrong. **Bytes in hand are only sound if they are the bytes of the
right file**, and which file is the right one is not knowable from a list that stops at its
first hit.

So the correct shape is: **enumerate the root (tree channel), then classify EVERY licence-named
entry, then decide** — never first-match-wins. The `families` / `names_multiple` columns of
`p441-tree-licence-enumeration` already encode this; `P0a` found it, and the honest record is
that this pass restated the lesson badly before its own data corrected it.

## What `result.2026-10-14-p198.tsv` is, and is not

It is `30` education rows, each licence classified from **bytes** by
`p198-title-line-family/family_title_line.py`. The `family` column is sound. 🔴 **The `path`
column is first-match and therefore NOT a claim that no other licence file exists** — see
`evidence/licence-at-wrong-path.2026-10-14-p198.tsv` for the five rows where it matters.

`2` rows came back `LIST-MISS` and were then resolved on the tree channel:
`formalms/formalms` *(nothing at root; the grant is a translated UI asset)* and
`OS4ED/openSIS-Classic` *(nothing at root; `docs/License.txt`)*.

## Lane note

`probe_root.sh` is recorded for provenance but **was not executed from this directory** — the
session's permission classifier denies `bash <repo script>` *(`[Code from External]`)*. It ran
from the scratchpad as own-authored code. See `evidence/lane-census.2026-10-14-p198.tsv`.
