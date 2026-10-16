---
industry: education
region: Global
updated: 2026-10-16
---

# `p248-named-proprietary` — the windowless name tier, the rider port, and the arm closure that makes both safe

**`ACTION XE`, registered by `p247`, discharged here.** 38 controls, in `make hooks`.

`p247` measured three different causes of the same wrong answer — a payload that forbids
commercial use returning `ALLOWED` — and named them `ORDER`, `VOCABULARY` and `WINDOW`.
`ACTION XA` fixed `ORDER` by hoisting the source-available anchors. This instrument settles the
other two, and in doing so it found a fourth that `p207` had already written down.

## 1. What was broken, with the numbers

| payload | bytes | before `p248` | after | cause |
|---|---|---|---|---|
| `cockroachdb/cockroach` CSL (2024) | 8 782 | `UNCLASSIFIED` → **`ALLOWED`** | `NAMED-PROPRIETARY (CockroachDB-CSL)` → `DENIED` | **`VOCABULARY`** — the name is at offset `0`, fully inside the `4 000` window. Position cannot matter for a name nobody looks for |
| `redpanda-data/common-go` Community License | 27 204 | `UNCLASSIFIED` → **`ALLOWED`** | `NAMED-PROPRIETARY (RedpandaCommunity)` → `DENIED` | **`WINDOW`** — its own name at `2`, and its real `Business Source License v.1.1` reference at `4 969` of `24 661`, beyond the truncation every anchor works inside |
| `p207/fixtures/commons-clause-mit.txt` | 621 | `MIT` → **`ALLOWED`** | `MIT` → `DENIED` | **`RIDER`** (`D14`) — the family is *correct*; the rider removes the right to **Sell** |

## 2. `ACTION XE`'s limb 2 fires, and it is worse than XE stated

XE's own hazard note said the change was unsafe until `commercial_use_ok`'s default arm was
**proven** to deny. It was measured instead of assumed — `osi_family_of` shadowed with a stub,
payload carrying no restriction vocabulary in any language, so the arm taken is the only thing
the verdict can depend on — and the default arm **permitted, 6 of 6 candidate names**
([`p248-default-arm`](../../../evidence/p248-default-arm.2026-10-16-p248.tsv)).

And one step further than XE saw: `P241`'s blanket-denial branch is gated on
`[ "$__f" = "UNCLASSIFIED" ]`. **Naming a family removes that protection** — `$__f` stops being
`UNCLASSIFIED`, so the branch does not run. Emitting the name without closing the arm would have
made the verdict *worse* than leaving the payload unclassified.

**The fix is not an inverted default.** Inverting it alone would deny every OSI family this base
emits and does not list; measured instance — `CC0-1.0` does **not** match the `CC-*` glob, so it
reached the default and returned `ALLOWED` *by accident*: right answer, wrong road. So the
enumeration is **closed** and the default is left as an unreachable net that now denies. The
`family-arm closure` control reads the arm patterns **out of the source** and fails if any family
`osi_family_of` can emit would reach that net.

> `NO-CESSION (negativa explicita)` is deliberately outside the closure list: `P299`'s early
> return sits **above** the family `case`, so demanding an arm for it would be demanding dead
> code. It is asserted separately on a real payload shape.

## 3. The position question, measured rather than argued

XE asked for a windowless pre-scan and did not say where to put it. Both positions were swept
over the same 354 fixtures ([`p248-position-delta`](../../../evidence/p248-position-delta.2026-10-16-p248.tsv)):

- **Position A** — the name above every anchor. `20` of `354` fixtures carry a name, and **`19`
  are no-ops**: the name *is* the family the anchors already return. Exactly `1` differs.
- **Position B** — after the full-text anchors, before the `<= 400 B` declaration tier. Blast
  radius on already-identified payloads is **zero by construction**.

**Position B is published**, and the single non-no-op row is a finding rather than a tie-breaker:
position A would have answered `NAMED-PROPRIETARY (CommonsClause)` on the Commons Clause payload
— the right verdict by the wrong route, because it throws away the inner `MIT` grant that really
does govern everything the rider does not touch.

The tier does sit **above** the `<= 400 B` declaration level, and that is load-bearing: a
constructed `Licensed under the CockroachDB Software License, not Apache 2.0.` returned
`Apache-2.0 (declaracion)` → `ALLOWED` off the loose `apache` token before. A full proprietary
name is stronger evidence than a bare token. *(For a name an anchor already knows, the anchor
still wins and the verdict is right anyway — both cases are controlled.)*

## 4. The fourth cause: `D14`, which this base had already measured and never wired

| instrument | in `make hooks` before `p248` | verdict on the same payload | correct |
|---|---|---|---|
| `p207-permissive-half-audit::classify_grant` | 🔴 **no** | `NON-OSI-CommonsClause+MIT` | 🟢 **yes — the only one** |
| `lib/license_family.sh` | 🟢 yes | `MIT` → `ALLOWED` | 🔴 no |
| `p1054-mit-plus-clause::classify` | 🟢 yes | `MIT`, `usable_permissive=True` | 🔴 no |

`p207` wrote the sentence this pass acted on: a Commons Clause body returns *"a confident, clean
`MIT` — no suffix, no flag, nothing to notice"*, which is **worse** than `UNRECOGNISED`, because
`UNRECOGNISED` at least asks to be looked at.

**The defect was never the reading — it was the wiring.** This is `p241`'s finding in a new place:
*this KB already owned a correct classifier that `make hooks` has never run.* So `p207` is now in
`make hooks` (12/12), and its predicate is ported into the shared classifier — **narrow on
purpose**, the same two anchors `p207::rider_token` uses, with a parity control against it
(`P637`: two implementations of one predicate are measured against each other).

🟡 **`p1054` is still wrong after this pass** and is `ACTION XI`. Its own numbers say why:
`MIT_CANONICAL_LOW = 1020`, the payload is `621 B`, so `excess = max(0, 621 - 1150) = 0`. **A
rider that makes a licence file *shorter* than canonical MIT is invisible to a byte-excess test**,
and no term in `RESTRICTION_TERMS` matches `commons clause` or `right to Sell`.

## 5. Blast radius, both populations

| population | what it is | moved |
|---|---|---|
| **354** fixture payloads | `compose/code/**/fixtures*`, excluding `.py .sh .json .tsv .expected .toml .xml` | **4** — 3 verdict corrections, 1 precision gain, **0 correct cells broken** |
| **183** real repository payloads | every first-hand licence payload cached on these shelves (`p118-licence-column-sweep/evidence/`, sha256-named) | **0** |

The second row is the one that matters for the shelves: **no published cell is implicated by this
change, and none is corrected here.** Method is `p247`'s own — the pre-change file recovered with
`git show HEAD:` and both versions run over the same payloads in the same window.

🔴 **Stated rather than left to be assumed:** `183` is the *cache*, not the shelves. A published
row whose payload is not cached here was **not** re-graded, and `ACTION XH` still holds the `60`
`UNREAD` slugs.

## 6. Files

| file | what it is |
|---|---|
| `test_named_proprietary.sh` | the 38 controls, in `make hooks` |
| `sweep.sh` | the fixture blast-radius sweep; the population rule is in the script, not in a memory of it |
| `regrade.sh` | the 183-payload re-grade; takes the classifier path, so an old version can be run against a new one |
| `posdelta.sh` | the position A/B measurement |

The predicates themselves (`named_proprietary_of`, `rider_restriction`,
`__source_available_names`) live in `lib/license_family.sh`, because a classifier that is not in
the shared classifier is not in anyone's path.
