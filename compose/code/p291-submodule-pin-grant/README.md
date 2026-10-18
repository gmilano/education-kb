# `ACTION p291` — a submodule's grant is verified **at the pin**, and `HEAD` is not the question

Built pass 291 (`2026-10-18`). Suite: **31 controls**, in `make hooks` as `gate-pin-grant`.
Offline. Online arm: none needed — the probe is `curl` against a pinned SHA.

## The gap it fills, and the rule it corrects

`p290` found the shape: a repository whose root `LICENSE` is a verbatim MIT payload and whose
*content* is seven `160000 commit` gitlinks. It wrote this base's first rule for it:

> a submodule's grant is verified when (1) its own payload is read first-hand **and**
> (2) the `HEAD` it was read at **equals** the pinned gitlink SHA.

🔴 **Condition (2) is wrong, and it is wrong in the restrictive direction.** `p290` read each
submodule at `HEAD` — because that is what `git ls-remote` returns — and then *checked* `HEAD`
against the pin. But `raw.githubusercontent.com` serves a payload **at an arbitrary commit**,
and a pinned SHA is a perfectly good ref. The grant a `--recurse-submodules` clone actually
lands on can be read **directly**. Measured this pass: **7/7 segments answered `200` at their
pinned SHA.**

| submodule state | `p290`'s rule says | the truth |
|---|---|---|
| `HEAD` == pin | `GRANTED-AT-PIN` | `GRANTED-AT-PIN` |
| `HEAD` has moved past the pin | 🔴 `UNVERIFIED-AT-PIN` | 🟢 **still readable at the pin** |
| `HEAD` was relicensed after the pin | 🔴 `UNVERIFIED-AT-PIN` | 🟢 **the pin's grant is the one that binds** |

Why the restrictive direction is the dangerous one: `p290`'s rule reports *"cannot verify"* for
a repository whose grant is sitting there readable. That invites the next pass to re-probe at
`HEAD`, find a relicensed `HEAD`, and publish **that** licence — when the superproject pins the
old commit and a vendoring studio receives the **pin**.

🟢 **The rule, as gated:**

> A submodule's grant is `GRANTED-AT-PIN` when its own payload is read first-hand **at the
> pinned gitlink SHA**. The submodule's `HEAD` is not an input.

A row read at `HEAD` is **not** a verification however equal the two SHAs happened to be on the
day it was measured — equality of timing is not evidence. That is control `C7`, and it rejects
`p290`'s own two rows if they are ever re-asserted without being re-read.

## What it found on its first run

**7 of 7 `iblai` segments `GRANTED-AT-PIN`** — discharging `p290`'s ranked item 1, which was to
probe the five it had left. One licence path per segment, at the root, and all seven payloads
**byte-identical** to each other and to the superproject's: `1 063 B`, sha256₁₂ `f1269b7b2313`,
`MIT License` / `Copyright (c) 2026 ibl.ai`. Full table:
[`evidence/submodule-pin-grant.2026-10-18-p291.tsv`](../../../evidence/submodule-pin-grant.2026-10-18-p291.tsv).

🟢 The gitlinks were re-derived **blind** (`git ls-tree HEAD` on a fresh clone) and reproduce
`p290`'s seven exactly, as do its `95` agents and `76` skills.

🔴 **And the shelf arm found a live instance of the very defect `p290` could only warn about**:
`repos/trending.md`'s `org:iblai` vendor-estate listing counts the superproject among
**`9`/`9` `MIT`** repositories with the submodule boundary named nowhere near it. That cell sits
in append-only history (see **Scope**), so it is recorded rather than rewritten — but the gate
now stops the next one.

## Scope, stated plainly because it is the judgement call

- **Verdict vocabulary is closed**: `GRANTED-AT-PIN`, `NO-GRANT-AT-PIN`, `UNVERIFIED-AT-PIN`,
  `UNPROBED`. A fifth spelling is a gate failure. This base has twice grown a bucket per variant
  and then lost the filter.
- **`UNPROBED` discharges the census.** Declaring is the duty; probing is the backlog. What
  fails is a superproject with submodules that carry **no row at all** — `p290`'s actual shape,
  2 rows against 7 declared paths (`C9`).
- **The shelf arm is block-scoped, not line-scoped.** `p291`'s own first draft was line-scoped
  and returned 7 findings, **6 of them false**: `compose/patterns.md` names the gitlinks *two
  lines below* the citation it was flagged for. A line is not the unit a reader reads.
- **It recognises plain words, not only its own jargon.** *"It is a pointer; the seven sector
  configurations are separate repositories"* names the boundary better than the word "gitlink"
  does. A gate that only matches its own vocabulary measures the vocabulary.
- **On the append-only shelves** (`agents/trending.md`, `repos/trending.md`) the scope is the
  newest `## Pass` section — **`p279-absence-claims`'s convention verbatim**, not a second one.
  Those files keep history by design; a gate that failed on passes 243 onward would be red on
  arrival and disabled within a pass. What is enforceable is that the pass being written **now**
  cannot cite a superproject without the boundary.

## Running it

```sh
make gate-pin-grant                       # suite + the live check, offline
cd compose/code/p291-submodule-pin-grant && python3 test_pin_grant.py   # 31 controls
python3 -I pin_grant.py --root . evidence/submodule-pin-grant.<date>.tsv
```

`submodule-bearing.txt` beside this file is the register of slugs measured as submodule-bearing.
The shelf arm fires only on those, so it cannot invent findings about ordinary repositories.
