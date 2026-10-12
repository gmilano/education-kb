---
industry: education
region: Global
updated: 2026-10-12
---

# p150-identifier-collision — `ACTION FM` discharged, and `P32` was not the only one

`ACTION FM` asked for a committed identifier-collision gate: scan `compose/patterns.md`
for a pattern number assigned to two different patterns, and the thesis register for the
same. 🔴 *Refuted if `P32` is the only collision on the shelf* — which would make `T75` a
single slip rather than a property of allocating from an unread high-water mark.

## 🟢 DISCHARGED — a second collision, independent of `P32`

🔴 **`P18` names two different patterns, both allocated in p139:**

| line | pattern | fate |
|---|---|---|
| 1453 | *The tool-surface gate: enumerate what the connector can DO* | 🟢 **keeps `P18`** |
| 1546 | *Stop-ship gate for the one copyleft row on this shelf* | 🔴 **renumbered to `P37`** |

🟢 **The allocation is not arbitrary.** `P18` has been **amended five times** since p139 —
at step 1 (p145), steps 2 and 5 (p144), corrected for four static shapes (p143), again at
step 5 (p141, p140) — and 🟢 **every one of those amendments is about tool-surface
enumeration.** The tool-surface gate is the live `P18`; the copyleft stop-ship gate was
never revisited and is the orphan. 🔵 **Same rule p149 applied to `P32`: the first
allocation keeps the number.**

🟢 **`T75` is therefore a property, not a typo.** Two collisions, two different passes,
same cause: a number picked from memory rather than from the page.

## What counts as a collision

A revisit is legitimate and must not be flagged — `P18` is amended on purpose, five times.

| heading shape | kind | flagged |
|---|---|---|
| `## 🆕 `P30` — … *(new, p146)*` | `FIRST` | — |
| `## P1 — …` (predates the marker convention) | `UNMARKED` | — |
| `## 🔁 `P18` AMENDED at step 1 — …` | `REVISIT` | 🟢 never |
| two `FIRST`/`UNMARKED` with **different** titles | 🔴 **`COLLISION`** | 🔴 **fails the gate** |
| two with the **same** title | 🟡 `DUPLICATE_HEADING` | reported, does not fail |

🔵 **The two are separated because the remedy differs**: a collision needs a renumber, a
duplicate heading needs a deletion.

🟢 **Subsections are not allocations.** `### 🔴 What `P36` does NOT solve` and
`### 🔴 `P35` does NOT reach the data layer` carry a word before the identifier, which is
what rules them out — `markers` admits only non-word characters.

## Run it as the CI step

    python3 identifier_collision.py compose/patterns.md     # exit 1 on a collision
    python3 test_identifier_collision.py                    # 30 tests, offline

🟢 **Exit status is the gate**: non-zero when a collision is present, so it drops into CI
as one line. 🟢 **After the `P37` renumber: `ids=37 collisions=0 duplicate_headings=0`,
exit 0.**

## 🔴 What this does NOT do

- 🔴 **It does not catch a DANGLING citation**, and the shelf has at least one:
  `compose/patterns.md` line 406 cites *"this KB's own `P240` gate"* and **no `P240` is
  allocated anywhere** — the highest pattern on the page is `P37`. 🔵 **A cited-but-never
  -allocated identifier is the mirror image of a collision and the same habit produces
  it.** 🔵 **Registered as `ACTION FQ`.**
- 🔴 **The thesis register is not scanned in this run.** `register_collisions()` exists and
  is tested against authored fixtures, but it has not been pointed at the live thesis
  register, which is spread across pass sections rather than held in one table. 🔵 **The
  machinery is ready and the target is not identified.** 🔵 **Registered as `ACTION FR`.**
- 🔴 **It reads one page.** Patterns cited from `agents/top.md`, `intel/trends.md` and the
  instrument READMEs are not cross-checked against the allocation table.
