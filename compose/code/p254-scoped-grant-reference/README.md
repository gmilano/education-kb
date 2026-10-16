# `p254-scoped-grant-reference` — `P1065`: a POINTER to a licence is not a GRANT

**The subject**, read FILED at a resolved ref:
[`steveyeow/Feynman`](https://github.com/steveyeow/Feynman) — root `LICENSE`, `1 217` B,
`sha256₁₆ aa8325eadd7fea1c`, ref `849c336c378c`.

| bytes | what they are |
|---|---|
| `1`–`1 067` | canonical **MIT**, `Copyright (c) 2026 Steve Yao` |
| the last `150` | *"The contents of the `app/pro/` directory are licensed separately under the Business Source License 1.1. See `app/pro/LICENSE` for details."* |

`app/pro/LICENSE` is a **real BSL 1.1** (`917` B, `9cf07d243fa7da6e`, `Licensor: Steve Yao`,
`Change License: MIT`). Both grants are genuine: the repository is **dual-scope**.

The shared classifier returned **`BUSL`** for the root file, and `holder_of_file` then
returned `NOT-APPLICABLE (BUSL: holder not in the license text by construction)` over a
payload that *has* its copyright line. One misread family took the attribution with it.

## Why this matters beyond one row

`P1062` (p247, `ACTION XA`) hoisted the five source-available anchors above every OSI anchor,
because a BSL payload's mandatory `Change License:` names an OSI licence and the OSI anchors
matched first — the `BUSL` branch was dead code by construction.

`p247` pre-registered the inverse risk as **limb 2**: a real OSI payload that merely
*mentions* the BSL. It measured that population with GitHub's code-search API, found it empty
at measurable reach, and published it honestly as **a measured upper bound, not a proof of
vacuity**. It was a bound, it held for seven passes, and `p254` broke it — not with a better
code search, but with the ordinary row channel on a 160★ education repository.

## The discriminant

From the licence's own text, not from the prose citing it. BSL 1.1 has **mandatory
parameters**: `Licensor:`, `Licensed Work:`, `Change Date:`, `Change License:`.

| payload | parameters |
|---|---|
| `iaga-sentinel.busl-1.1`, `sdv.busl-1.1`, `feynman app/pro/LICENSE` | 4 / 4 |
| `p129 licence-bsl11-change-license-mit` | 3 / 4 |
| **`feynman LICENSE` (root)** | **0 / 4** |

## Why it cannot weaken a verdict

When the phrase appears **without** parameters the branch does not decide `MIT` — it *skips*,
and the payload keeps descending the chain. If the chain ends in `UNCLASSIFIED` (nothing
positively identified), the fall-through returns `BUSL` anyway. The anchor is only ever lost
to a **positively identified** family, never to the absence of one — and `UNCLASSIFIED` →
`ALLOWED` by token match is the direction `P1063` already paid for. A control pins it: a bare
mention with no grant body comes back `NAMED-PROPRIETARY (BUSL)` and is **refused**.

## The first version of this fix was wrong

It used `^[[:space:]]*(Licensor|…)`. `$t` has already been through `tr -s '[:space:]' ' '`
(license_family.sh line ~210), so it is **one line** and `^` matches only byte 0 — the regex
matched nothing and returned **all four real BSL payloads to their Change License**, exactly
the regression `P1062` exists to prevent.

| | result |
|---|---|
| the patch, read | looked correct |
| the patch, run over 332 fixture payloads | **5 changed, 4 catastrophically** |
| the corrected patch, same 332 | **0 changed** |

Both halves are pinned as controls, including one asserting the anchored form still finds
nothing in squeezed text. Blast radius:
[`p254-hoist-blast-radius`](../../../evidence/p254-hoist-blast-radius.2026-10-16-p254.tsv).

## Usage

```sh
bash test_scoped_reference.sh    # 16 controls; also wired into `make hooks`
```
