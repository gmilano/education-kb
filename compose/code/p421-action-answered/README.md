---
industry: education
region: Global
updated: 2026-10-24
---

# `p421-action-answered` — the other half of `action-gap-crosscheck`, wired

**Pass 421, 2026-10-24.** Written, measured, amended three times and wired in-pass.
`test_action_answered.py` — **29 controls, 29 pass**. `gate-action-answered` is in `HOOK_GATES`.

```sh
make gate-action-answered              # the suite, then the report
python3 action_answered.py ../../..    # the report alone
python3 action_answered.py ../../.. --tsv
```

## Why it exists, and why the instrument that already existed was not enough

`compose/code/action-gap-crosscheck` (pase 59) is this base's instrument for the question
*«que ninguna acción entregada esté ya contestada por el propio corpus»*. Two things were
measured about it at `p421`:

| | measured |
|---|---|
| 🔴 It is in **no `make` target at all** | `grep -n action-gap-crosscheck Makefile` → **nothing**, for ~360 passes. `make hooks` has never run it |
| 🔴 Wiring it as-is would have bought **nothing** | Run over the live corpus: `gap citations inside action blocks : 0`. Its suite still passes **16/16** |

The second is the load-bearing one. It is calibrated to the **retired** ledger notation —
`^## ... acciones que el pase N deja escritas`, `gap 51`, `CERRADO`, `al cierre del pase N` —
while the register now writes `### 🟢 Actions`, `ACTION p420-E` and `Gap 420-C`. Three
independent reasons it reads nothing: the action-block heading, the gap-citation shape, and the
closure vocabulary.

🔴 **A gate whose denominator is zero is green for the same reason a correct one is green.**
That is `gate-backlog-denominator`'s class, and it is why `test_denominator_is_not_zero` is the
first control in this suite rather than a printed figure.

## The specimen

`ACTION p420-E` asked a successor to *"resolve first-hand whether any Open edX component or
Sakai is Apache-2.0"*, citing `p289` (*no restatement of an unreachable authority is a verified
grant*). **Both halves were already on these shelves when it was written:**

- `verticals/solutions.md` carries `| **Sakai** | 🟡 **ECL-2.0**` and `| **Open edX** | AGPL-3.0`;
- `compose/patterns.md` has carried the Apache-2.0 Open edX component since **`p390`** —
  `openedx/XBlock` and `openedx/xblock-sdk`, grant at `LICENSE.TXT`.

🟢 `p421` re-read all of it first-hand anyway (`T106`, at the commit SHA): Sakai **ECL-2.0**
`11 120` B `sha256₁₂ 0688f62d04f1` at `c35e7a2`; XBlock and xblock-sdk **Apache-2.0**
`11 358` B `cfc7749b96f6` at `c73c4bb` and `e61f9d2`, **byte-identical to each other**.

## The three arms

| arm | fires when |
|---|---|
| `STALE` | the clause cites a `Gap` the register declared **closed in an earlier pass** (the ported arm) |
| `ANSWERED-BY-ADDRESS` | the clause asks a licence question whose **object** is an `owner/repo` a live shelf already grades |
| `ANSWERED-BY-PLATFORM` | the same, where the object is a platform `verticals/solutions.md` already grades |

🔴 **What no arm catches, stated rather than implied:** an action whose subject is a project
named only in prose and absent from the platform vocabulary. A loose name-matcher would
reproduce `Gap 420-A` exactly — the defect `gate-absence` has, attributing a claim by **token** —
so it is not built. The vocabulary is **closed** and derived from this base's own platform shelf.

## The first draft reported 268 findings, and the amendments are each a control

🔴 **268 over 103 action blocks is a 99 %-false instrument** — the shape `p420` refused to ship
for `ACTION p419-A`. Three measured defects, three amendments, three regression controls:

| # | defect, measured | amendment |
|---|---|---|
| 1 | A bare `owner/repo` regex admitted **file paths** — including `agents/top.md`, `intel/open-gaps.md`, `compose/patterns.md` and `verticals/solutions.md`, **this base's own shelf paths**. `p351`'s `classify` returns `None` (may-be-an-address) for all four; `repos/foundations.md` is rejected only because GitHub happens to use `repos` as one of its own namespaces | The address channel is **`p348`'s `slugs_in`**, anchored on `github.com/`, so a path cannot enter by construction. Not a list |
| 2 | A clause citing a **second** action (*"build X, not to `ACTION p419-A`"*) was graded as if that action had been delivered with this clause's ask | The subject of a register row is the **first** action id in it; later mentions are references |
| 3 | A licence **token** fired on the word *"granted"* inside a fixture list, so `ACTION p420-B` matched on `moodle/moodle` — a fixture for a gate it asks to **build** | An **ordered template** over a bounded span: `ASK_VERB … SUBJECT … COPULA … LICENCE_TOKEN`, cell-scoped, and the asked licence must **differ** from the one the base carries. A bound question (`ACTION RV`) and a population sweep (`ACTION RQ`) cannot take that shape |

**268 → 13 → 12 → 2.** The two survivors are both `ACTION p420-E`, on its two halves, over a
denominator of **551** delivered actions in **103** action blocks across **10** register sections.
Zero false positives on the whole corpus. `test_the_whole_corpus_yields_exactly_the_specimen`
pins that as the **RATCHET**.

## The hole that is pinned OPEN, and the fix that was refuted

🟡 A **one-word prose** first cell (`Inside`, `Outside`) enters the platform vocabulary when its
row happens to carry a licence token. It is **latent**: the live vocabulary is 14 entries and
contains no prose label.

🔴 **The obvious closure was built and refuted in-pass.** Requiring a vocabulary entry to
co-occur with a `github.com/…` slug on the verticals shelf drops the vocabulary to 12 and
**removes `sakai` — the specimen's own subject** — because this shelf grades Sakai `ECL-2.0` on a
row carrying **no address at all** (the address lives on `repos/foundations.md` instead; a
cross-shelf split, not a missing address). A closure that deletes the specimen is worse than the
hole, so the hole is pinned as `test_the_prose_first_cell_hole_is_open` — `p364`'s disposition for
the locale-prefixed docs path, and `action-gap-crosscheck`'s own for its absent fixture.

## What is deliberately NOT done

🔵 `action-gap-crosscheck` is **left in place and untouched**. Its 16 controls still pass and its
`test_mandated_fixture_is_not_real` still holds an absence worth holding. Deleting it would erase
the evidence that this base can carry a correct instrument for ~360 passes without running it,
which is the finding, not a tidiness problem.
