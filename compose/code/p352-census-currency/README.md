---
industry: education
region: Global
updated: 2026-10-21
---

# `p352-census-currency` — a census over the shelves is stale in the pass that publishes it

**Pass 352, 2026-10-21.** 🔵 Fourth pass of this date (`p349` 2026-10-20; `p350` and `p351`
earlier today).

## The defect, named rather than described

`p351` discharged `ACTION ZZ-an` and published its headline denominator as:

> **2 476** harvested shapes → **33** are not addresses → **2 443 addresses** (1.33 % inflation).

🔴 **Re-derived over the nine `SHELF_FILES` of the tree `p351` actually committed, the triple is
`2 478 → 33 → 2 445`.** The working tree was clean and no byte was edited before measuring.

🟢 **The published figure is not approximately wrong, it is exactly something else: it is the
`p350` tree's triple.** Measured across three committed trees with `p351`'s own classifier:

| tree | harvested | rejected | addresses |
|---|---:|---:|---:|
| `HEAD~2` — `p349` as committed | 2 473 | 33 | 2 440 |
| `HEAD~1` — `p350` as committed | 2 476 | 33 | **2 443** ← what `p351` published |
| `HEAD` — `p351` as committed | 2 478 | 33 | **2 445** ← what `p351`'s own tree yields |

🟢 **And the two missing addresses are nameable, which settles the mechanism.** `p351`'s commit
added exactly two folded addresses and removed none: **`aclascollege/polymath`** — which is
`p351`'s *own* new `repos/foundations.md` row — and **`imsglobal/openbadges-validator-core`**.

## Why it is structural, and why "re-run it next time" is not the fix

🔵 A census whose **input is the shelves**, published in the pass that then **writes to the
shelves**, is stale the moment it is written. The ordering that produces the defect is the
natural one: measure, then write up what you measured.

🔴 **It has now happened three passes running.** `p350`'s own commit message records the same
shape about its predecessor — *"p349's own headline denominator is wrong by one group and two
addresses"* — and `p351`, which wrote that correction, published a stale denominator of its own
one pass later. 🟢 **A pass that knows about the defect still commits it**, so the remedy cannot
be attention. It has to be a gate.

## What this gate does

`gate-census-currency` reads the **live** (first) census sentence in `README.md`, derives the
triple over `SHELF_FILES` using **`p351`'s own classifier** — imported, not reimplemented — and
goes **RED** when they disagree. The census can then only be published correctly: *write the
pass, derive, then state the figure.*

🔵 **Two boundaries carry the design.**

1. **The anchor file is not a `SHELF_FILE`.** `README.md` is excluded from the derivation, so
   stating the number cannot change the number. A gate that checked a figure against a corpus
   the figure is part of could never be trusted.
2. **Only the LIVE occurrence is judged.** History below it holds previous passes' figures,
   which were correct against **their** trees. A gate that demanded the whole file agree with
   today's tree would force exactly the retro-editing this base's *artefacts are dated by
   MEASUREMENT* convention forbids.

## Invocation

```sh
make gate-census-currency      # suite + the live comparison; RED on disagreement
make hooks                     # it is IN the standing check, per p338's lesson
```

🔴 **`p338`'s lesson is why it is wired on the pass that builds it:** `gate-region-headings`
existed with a passing suite for forty-five passes and was in no target, so `make hooks` never
judged region structure at all. A gate outside `HOOK_GATES` judges nothing.

## Controls — 24, all offline

- `p351`'s **actual published sentence**, parsed to `(2476, 33, 2443)`.
- The separator is a **plain space** (`0x32 0x20 0x34 0x34 0x33` at `README.md:23`) — measured,
  not assumed; the thin, no-break, figure and comma separators are accepted too, so a cosmetic
  paste cannot read as a stale denominator.
- **The live occurrence wins over history** — the load-bearing control.
- **Each of the three cells is load-bearing alone**: a pass can get the total right and the
  rejection count wrong, and that still means the census ran at the wrong time.
- A **missing anchor is RED, not silently green** — a headline denominator that quietly stops
  being stated is how `p349`'s went unchecked for two passes.
- The derivation **ignores the anchor file**, pinned as a control rather than left to the reader.
- A **missing shelf file raises** rather than under-counting a denominator.
- **`P541`**: no `README.md` is **refused with exit 2**, distinguishable from a stale figure's
  exit 1.
- An anchor that survives **re-wrapping** — `p278`'s first anchor missed because the phrase it
  pinned wrapped.
- The anchor **ladder is CASE-CLOSED** in stem *and* extension; a lowercase write-up is
  **found**, the first rung wins when several exist, and no rung at all is a **real absence**.

## 🔴 A second defect, and `p283`'s audit caught it the moment this gate was wired

🔴 **Adding `gate-census-currency` to `HOOK_GATES` turned `gate-ladder-case` RED**:
`STANDING:SINGLE-SPELLING` rose **17 → 18**, and the eighteenth row was this file —
`('compose/code/p352-census-currency/census_currency.py', 'readme', 'SINGLE-SPELLING',
'no-upper-ext', 'STANDING', 'README.md')`.

🟢 **The audit was right, and the temptation was to say it was not.** The reading that excuses
it is available and plausible: `README.md` here is *this* repository's own fixed artefact, not
a path probed on an arbitrary repository, so a case-closed ladder "is not needed" — which is
precisely the shape of `p351`'s `THIRD_PARTY_SCOPE` argument, and it would have been the third
instance of the scope-defect class this pass spent its length documenting. 🔴 **It is also
wrong on the merits.** If this base's write-up were renamed `Readme.md`, a gate pinned to the
single spelling would report its anchor **MISSING** and refuse — loud, but still a wrong
answer about a file that is sitting right there.

🟢 **So the ladder was CLOSED rather than the gate taught to look away** —
`ANCHOR_LADDER = ("README.md", "README.MD", "Readme.md", "readme.md", "README", "readme")`,
walked first-hit-wins by `resolve_anchor`, graded **`CASE-CLOSED` / `UPPER-EXT`** on re-audit.
`make hooks` is **31/31**.

🔵 **One note on the ratchet's own reasoning, because it is slightly off and the gate still
worked.** `C14`'s comment argues it is safe because *"adding instruments can never break it …
`STANDING:<verdict>` keys bind only the ladders `make hooks` actually invokes."* 🔴 **Adding a
hooks-invoked instrument that spells a family literal once DOES raise `STANDING:SINGLE-
SPELLING`,** as this pass demonstrates. 🟢 **That is the ratchet working, not failing** — a new
single-rung ladder in the standing set is exactly the weakness it should refuse — but it is
caught as a *regression* when it is really an *admission*, and a successor reading `C14`'s
comment would not expect it.

## 🔴 One defect this instrument nearly shipped, recorded because it is `p253`'s

The first recipe ended `... | sed "s/^/   /" || exit 1`. 🔴 **A pipeline returns its LAST
command's status, so `sed`'s `0` masked the gate's `1` and the `|| exit 1` was unreachable** —
the gate printed `STALE` and the recipe exited `0`. That is exactly `p253-gate-propagation`'s
class, in the one direction `p253`'s own note does not spell out: not `&&`-list errexit, but
**pipe masking**. 🟢 Repaired with `set -o pipefail`, and verified by watching the gate actually
fail on `p351`'s live triple before this pass restated it.
