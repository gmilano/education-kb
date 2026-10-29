---
industry: education
region: Global
updated: 2026-10-29
---

# `p521-commercial-posture` — the base's own licence gate PASSES both repos `p520` refused

```
python3 test_commercial_posture.py     # 40 checks, offline, no network
```

🟢 **Result this pass: `40/40` green offline, and the 31-row live sweep in
[`agents/top.md`](../../../agents/top.md) reproduces every `p520` hand verdict — including the two
refusals the existing instrument gets wrong.**

## Why it exists

`p520` refused two repositories by hand and was right both times:

- [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) — "bespoke non-commercial grant"
- [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) — CC BY-NC 4.0

🔴 **Run the base's own [`licence-grant-gate`](../licence-grant-gate/) against the same two
payloads and it passes both:**

```
PageLM   -> {'state': 'LICENSED', 'family': 'MIT', 'granted': True, 'note': 'grant read from payload'}
cn-math  -> {'state': 'LICENSED', 'family': 'CC',  'granted': True, 'note': 'grant read from payload'}
```

That is reproducible from the served bytes stored in [`fixtures/`](fixtures/). 🔵 **The gate is not
wrong about what it measures.** `verdict()` answers *"is a licence granted?"*, and in both cases one
is. It is silent about *commercial posture* — and in education that is the axis that decides,
because, as [`intel/trends.md`](../../../intel/trends.md) recorded at `p520`, the grant that blocks
an education engagement is a **content** licence, not a code licence. A caller reading `granted` as
*"may a paid engagement build on this?"* gets the wrong answer on exactly the rows that matter.

## The two defect classes

### 1. MIT-incipit camouflage

`PageLM`'s `LICENSE.md` (`8 563` B) **opens with the verbatim MIT incipit** —

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
> associated documentation files (the "Software"), to use, copy, modify, and run the Software for
> **personal, educational, or non-commercial research purposes** …

— and only then imposes: redistribution **"strictly prohibited"** (§2), no commercial use without
written consent (§3), a **revenue-sharing agreement** executed *before* any commercial deployment
(§4), and a **revocable** grant (Grant of License). `family_of` reads the title region only, the
incipit matches, and the restrictions below are never seen.

🔵 **This is not a drafting accident — it is the shape of the problem.** The MIT opening sentence is
doing the work of making a restricted grant *look* permissive to exactly the automated check a
studio would run. Any classifier keyed on that sentence — this base's, and GitHub's own sidebar,
which shows no licence name for this repo — is defeated by it.

**Fix:** scan the **whole** payload for restriction terms and let them **override** a permissive
family read. A refusal cites the clause that caused it, so it can be checked by hand.

### 2. A non-commercial family read as commercial

`family="CC"` is not a posture. CC BY-4.0 is commercially usable; CC BY-NC-4.0 is not; CC BY-SA
carries reciprocity. Collapsing all three to `CC` and returning `granted: True` is how a
**non-commercial** licence reaches a paid engagement.

**Fix:** resolve the CC **variant**, never the bare family.

## Two bounds this pass's own suite caught

Neither was hypothetical; both were found by a failing check, not by reading.

- **Window.** A 1 200-character title window is too generous. The GPLv3 names the AGPL in
  section 13 (*"Use with the GNU Affero General Public License"*), and on a payload with a short
  preamble that section falls inside the window.
- **Order.** Resolving family-by-family over the window lets a *later* line beat the title: the
  AGPL probe matches section 13 even though line 1 reads `GNU GENERAL PUBLIC LICENSE`. 🔵 **Scan the
  title lines in order and take the first line that names a family.** This is safe for the GNU pair
  because `GNU AFFERO GENERAL PUBLIC LICENSE` does not contain the substring
  `GNU GENERAL PUBLIC LICENSE` — the word AFFERO separates them.

A body-wide grep misclassifies **every** GPLv3 payload as AGPL. On this pass's sweep that is
`moodle/moodle`, `chamilo/chamilo-lms`, `ILIAS-eLearning/ILIAS` and `GibbonEdu/core` — four
institutional platforms whose reciprocity obligation would have been overstated.

## Posture vocabulary (closed)

| Posture | Buildable in a paid engagement | Meaning |
|---|---|---|
| `PERMISSIVE` | 🟢 yes | MIT, BSD, Apache-2.0, ECL-2.0, CC BY |
| `COPYLEFT` | 🟢 yes, with an accepted reciprocity obligation | GPL, AGPL |
| `WEAK-COPYLEFT` | 🟢 yes, file/library-scoped reciprocity | LGPL, MPL, CC BY-SA |
| `NON-COMMERCIAL` | 🔴 **no** | CC BY-NC |
| `BESPOKE-RESTRICTED` | 🔴 **no** | a custom grant carrying restriction terms |
| `NOT-OSI` | 🔴 no | Elastic and similar |
| `UNKNOWN` | 🔴 no — absence is not permission | no payload, or no recognised family |

🔵 **`buildable_in_paid_engagement()` is the call a studio should make.** `granted` is not that
question and was never meant to be.

## Interface

```python
posture_of(text)                     # -> (family, posture, reasons)
buildable_in_paid_engagement(text)   # -> (bool, family, posture, reasons)
restrictions_in(text)                # -> [(label, matched_text), ...]
cc_variant(text)                     # -> "CC-BY" | "CC-BY-NC" | "CC-BY-SA" | None
family_from_title(text)              # -> (family, posture) from the first naming title line
```

This module does **not** replace `licence-grant-gate`; it answers the question that one leaves open.
Run both: the gate decides whether a grant exists, this decides whether you may build on it.

## Fixtures

[`fixtures/`](fixtures/) holds the served bytes read `2026-10-29`, so the suite needs no network and
a later pass can re-grade without re-fetching:

| Fixture | Bytes | Source |
|---|---|---|
| `pagelm.LICENSE.md.txt` | `8 563` | `raw.githubusercontent.com/CaviraOSS/PageLM/main/LICENSE.md` |
| `cn-math-taxonomy.LICENSE.txt` | `19 347` | `raw.githubusercontent.com/xiaoyang111222/cn-math-taxonomy/main/LICENSE` |
