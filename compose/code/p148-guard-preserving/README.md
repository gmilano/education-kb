---
industry: education
region: Global
updated: 2026-10-12
---

# p148-guard-preserving — `ACTION EU`: the guard wrapper is verdict-preserving

`ACTION EJ` (p147) wired `p146-empty-walk-guard` **around** the five at-risk instruments
rather than editing their bytes, because editing them would have destroyed the
"baseline reproduces" discipline p145 established. 🟢 **`p147-guard-harness` showed the
wrapper refuses on 10 of 10 npm pairs and 2 of 220 clone pairs.** 🔴 **What it never showed
is what the wrapper does on the 218 pairs that DO have input.**

> 🟡 **`ACTION EU`** — test whether the guard harness changes any PUBLISHED figure over the
> full 44-row census. 🔴 *Refuted if any row's published value changes.*

🔵 **The falsifier is inverted relative to the rest of this shelf, deliberately: here a
silent falsifier is the good outcome.**

    python3 guard_preserving.py <clone-dir>
    python3 test_guard_preserving.py     # 9 tests, authored fixtures, offline

## 🟢 Result — 218 preserved, 2 refused, 0 changed

| status | pairs | meaning |
|---|---|---|
| 🟢 **`PRESERVED`** | 🟢 **218** | both runs equal, on a non-empty enumeration |
| 🟢 `REFUSED` | **2** | the enumeration is empty; the verdict is **withdrawn**, not changed |
| 🔴 **`CHANGED`** | 🟢 **0** | 🟢 **falsifier silent** |

🟢 **`ACTION EJ`'s "wrap, do not rewrite" answer is safe as implemented.** The wrapper adds
refusals and changes nothing else.

## Method — the instrument's own verdict function, twice

🔵 **This shares no code with `p147-guard-harness`**, which called each at-risk module's
*enumeration* once. This module calls each module's **published verdict entry point** —
`is_mcp_server`, `hosts_in`, `survey`, `scan`: the same callables the figures on these pages
came from — **twice**, and compares:

| run | what it is |
|---|---|
| `bare` | the entry point called directly, as the published pass called it |
| `guarded` | the same call, but only after `walked_or_refuse` says the enumeration saw files |

🟢 **So the 2 refusals reproducing p147's 2-of-220 is an independent reproduction**, not the
same measurement run again.

## 🟢 Both refusals are the row that now has a reader

🟢 **`zavora-ai/mcp-student-records` is both refusals**, on `p141-surface-gate` and
`p143-surface-gate2`. 🔵 **Those two gates read `.py .js .mjs .cjs .ts .go .php` and the row
is Rust** (`T64`). 🟢 **`ACTION EO` reads it at 46 this pass**, so the refusal now comes with
a remedy rather than only a refusal. 🔵 **A refusal plus a reader for the refused case is the
whole correction.**

## The 9 tests

Five pin `freeze`, without which *"bare equals guarded"* is meaningless: order-independent
for dicts and sets, order-**sensitive** for lists (a list order is a measurement), stable
under nesting, and not conflating a tuple with a list. Two pin the population — that
`SUBJECTS` has the arity `census()` splats, and that it is exactly `P146-D`'s five at-risk
instruments. Two pin the failure paths: an unloadable module is reported as `LOAD_FAILED`
rather than raised, and 🟢 **an empty tree is `REFUSED`, never `PRESERVED` over nothing.**

    9/9 passed
