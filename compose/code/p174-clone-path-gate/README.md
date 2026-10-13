---
industry: education
region: Global
updated: 2026-10-13
---

# `P174` — an instrument that names its own clone cannot be reused

Artefacts and suite of the **one hundred and seventy-fourth pass (2026-10-13)**.
🟢 **12/12 green under `python3 -I`, fully offline.**

## Why the pass needed the gate

🔴 p172 wrote `classify_bodies.sh` to source the shared licence classifier at
`/tmp/education-kb/compose/code/lib/license_family.sh`. p173's clone was at
`/home/user/education-kb`, so **the instrument could not run at all** and the pass that
needed it re-implemented the classifier it was supposed to reuse (`T247`). The cost was
not a crash; it was a *duplicate* of the one component this KB most wants to have exactly
one of.

🟢 `ACTION KC` asked whether that was a typo or a class. **It is a class:**

| | instruments | files | lines |
|---|---|---|---|
| 🔴 **live clone root at commit `f5cdcf0`** | 🔴 **`4`** | 🔴 **`9`** | 🔴 **`13`** |
| 🟢 after the `P174-KC` repair | 🟢 **`0`** | 🟢 **`0`** | 🟢 **`0`** |
| 🔵 narrative mentions, left readable on purpose | 🔵 `4` | 🔵 `4` | 🔵 `4` |

🔴 **`ACTION KC` limb 1 FIRED** — `p172-manifest-attribution` was not the only one.
`p120-unread-grant-resolution`, `p121-stale-token-crosspage` and `p996-promotion-ledger`
carried one too. 🟢 **Limb 2 stayed silent** at `4 < 5`, and only because the rule below
draws the line at *executable* text.

## The classification rule, stated because the count depends on it

🔵 A hit is **`LIVE`** when the line — with any `#` comment stripped and outside any
triple-quoted block — still contains a KB clone root. Otherwise it is **`COMMENT`**.
🟢 **`/tmp` scratch files (`/tmp/lic.$$`) and example INPUT directories (`/tmp/edu-trees`)
are not clone roots and are not hits at all.** A gate that fired on them would be switched
off within a pass, and `p151`'s two usage examples are correct as written.

🔵 **Count the narrative mentions and the answer is `8` instruments, which is a different
question.** p174 answers the one `ACTION KC` asked — *"fix each to resolve relative to
itself"* — and only executable text can be fixed that way.

## What the repair looks like

```sh
# shell: <kb>/compose/code/<instrument>/x.sh  ->  ../../..
KB="${KB_ROOT:-$(cd "$(dirname "$0")/../../.." && pwd)}"
```
```python
# python: same arithmetic, same place
KB = pathlib.Path(__file__).resolve().parents[3]
```

## 🔴 Why the behaviour controls read "IDENTICAL", and why that is the point

🔵 This pass's clone sits at `/home/user/education-kb` — **the very path four of those
instruments hardcoded.** They were *accidentally correct here*, so their suites score the
same before and after:

| control, run from a foreign cwd | pre-patch | post-patch |
|---|---|---|
| 🔴 `p172-manifest-attribution/classify_bodies.sh` | 🔴 **DEAD** — `No such file or directory` on line `6` | 🟢 **RUNS** |
| `p120-unread-grant-resolution/test_p120.sh` | `51` passed / `4` failed | `51` passed / `4` failed |
| `p121-stale-token-crosspage/test_p121.sh` *(no argument)* | `22` passed / `6` failed | `22` passed / `6` failed |
| `p996-promotion-ledger/*.py` | run | run |
| `p355-cwd-portability/test_p355.py` | `24/24` | `24/24` |

🔵 The pre-existing `4` and `6` failures are page drift from fifty-odd passes and are
**unchanged by this repair** — which is the assertion worth making: the patch moved the
root and nothing else.
🟢 **So the repair is invisible in this container and decisive in the next one.** That is
precisely why the deliverable is a gate rather than nine edits.

## The negative controls

🟢 `fixtures/comment_only.sh`, `fixtures/docstring_only.py`, `fixtures/scratch_tmp_only.sh`
and `fixtures/fabricated_other_repo.sh`. The last one is **fabricated**: a hardcoded
`/usr/share/misc/helper.sh` that the gate must ignore, because a gate that fires on every
absolute path fires on half the tree.
🟢 `test_the_narrative_hits_are_still_there_and_still_readable` asserts the repair did
**not** work by deleting the history of the defect.

## 🟢 The positive control, which is the half that makes it a gate

🔵 A gate only ever seen passing is a decoration. `fixtures/pre-patch-lines.tsv` keeps all
**`13`** removed lines verbatim, and the suite asserts the classifier calls **every one of
them `LIVE`** and that they map to exactly `9` files in exactly `4` instruments.

## Invocación

```sh
python3 -I check_clone_paths.py                 # TSV a stdout; exit 1 si hay un LIVE
python3 -I check_clone_paths.py /path/to/kb     # contra otro árbol (así se midió f5cdcf0)
python3 -I test_check_clone_paths.py            # 12/12, offline
```

🔵 **Where it belongs:** this is a pre-commit check, not a suite to remember. `exit 1` on
any `LIVE` hit is the whole interface.
