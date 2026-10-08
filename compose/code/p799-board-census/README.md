---
industry: education
region: Global
updated: 2026-10-08
---

# `P799` — the board is counted, and every red is attributed to a cause

Artefacts and suite of the **sixty-fifth pass (2026-10-08)**. 🟢 **12/12 green under `python3 -I`.**
Data: `board.2026-10-08.tsv`, one row per suite.

## 🟢 `Gap 257`/`Gap 258` — the board was finally RUN

🔴 For several passes this KB said its board of suites was unmeasured, and pass 63 put the shortfall
plainly: *three greens are not 112.* 🟢 **This pass ran all of it.**

| verdict | n | what it means |
|---|---|---|
| 🟢 `green` | **62** | passed under `python3 -I` |
| 🟢 `green-slow-137s` | **1** | `p471` — passed, 137.5 s, exceeded the sweep's own 120 s cap |
| 🟡 `red-minusI-syspath` | **41** | **unread**, not failed — see below |
| 🔴 `red-env-cryptography` | **1** | `p213` — `cryptography`'s Rust binding panics in this environment |
| 🔴 `red-real` | **1** | **`p351`**, and it is this KB's own star-count gate |
| | **106** | |

## 🔴 Two corrections to figures this KB had been repeating

🔴 **The board is 106 suites, not 112.** 112 was never measured. 106 is
`find compose/code -name 'test_*.py' | wc -l`, across **143** directories — so **37 directories
carry no suite at all**, and the census counts suites and says so.

🔴 **41 of the 44 first-pass reds were an artifact of the instrument, not a defect in the tree.**
`python3 -I` implies `-P`, which drops the script's own directory from `sys.path[0]`, so every suite
importing its sibling module raises `ModuleNotFoundError`. 🟢 **Verified by control probe** — an own
script with an own sibling module: plain `python3` imports it, `-I` and `-P` both fail, `sys.path[0]`
becomes `/usr/lib/python311.zip`. 🔵 A fact about the **flag**.

🟡 **They are recorded as `unread`, not green.** Calling them green would be the same error pointing
the other way. `test_forty_one_are_UNREAD_and_are_not_counted_green` is the guard.

## 🔵 And a timeout is not a failure

🟢 `p471` was written down red by the sweep because the sweep capped each suite at 120 s. Re-run
uncapped: **27/27 then 25/25, exit 0, 137.5 s.** 🔴 **The instrument's timeout had become the suite's
verdict** — the same shape of defect as `000`-for-a-refusal in `p798`.

## 🔵 The denominator moved, and this file says so rather than letting a later pass find it

🟢 **The census measures the board AS IT STOOD BEFORE this pass wrote anything: 106 suites.**
🟢 **This pass then added its own three** — `p798` (9/9), `p799` (12/12), `p800` (8/8) — so a sweep
run *after* publication finds **109 suites and 65 passes**, re-measured and confirmed:
`TOTAL=109 PASS=65 FAIL=44`.

🔵 **The 44 failures are unchanged, and that is the control that matters:** nothing this pass wrote
turned an existing suite red. 🔴 **`board.2026-10-08.tsv` is deliberately NOT back-filled with the
three new rows** — it is the record of a measurement taken at a moment, and editing a measurement to
match a later state is how a census stops being one.

## 🟢 What the residue is worth

🔵 Of 106 suites, **exactly one is a real red**, and it is `p351` — the gate this KB wrote to catch
unbanded star counts in its own prose. 🟢 **Pass 64 published a tree it could not run; this pass
publishes a tree it ran, with one named defect in it.** `Gap 296` carries that defect.

## 🔴 The narrow permission still outstanding

🟢 The suites' own docstrings have carried a standing request since pass 58: *permission to run the
OFFLINE suites of this tree.* 🟡 **It is now half-granted and the half matters:** `python3 -I` is
permitted and reads 65 of 106; plain `python3` is refused by the session's auto-mode classifier
(`[Code from External]`), which is what leaves 41 unread. 🔵 **Attributed to the layer that issued
it (`P797`), not written as a property of the suites.** The remedy is one of: permission for plain
`python3` on this tree, or the suites made import-free in the manner of `p798`/`p799`/`p800`.
