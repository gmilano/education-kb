# `p418-register-currency-gate` — `ACTION p417-D`, built

## What it measures

The gap register (`intel/open-gaps.md`) must not lag the shelves it registers gaps
for. The contract, in `ACTION p417-D`'s own words:

> if the newest `` ## 🆕 `pN` `` header in `intel/open-gaps.md` is older than the
> newest on `agents/top.md`, the register is stale and the gate is red

Generalised one step: the register is measured against **every** shelf passed to
it, not only `agents/top.md`, because a register owes currency to all of them.
A register may **lead** a shelf (`p419` register against a `p418` shelf is fine);
it may never **lag** one.

## Why it exists

Register staleness is not a one-off. It has failed **four times**:

| pass | state on arrival | repaired by |
|---|---|---|
| `p411` | register one pass behind | `p412`, which recorded it as a standing warning |
| `p414` | register at `p413` | — |
| `p415` | register still at `p413` | — |
| `p416` | register still at `p413` — **three passes stale for a full day** | `p417`, as labelled backfill |

`p412` responded with a warning. The warning did not hold, and `p414`–`p416`
followed. 🔴 **A usage contract that has to be remembered is not a control**
(`P237`) — which is why `p417` registered `ACTION p417-D` asking for a gate, and
why this is a gate rather than another note.

## Historical validation

Run against the **real commits**, the gate reproduces the failure and its repair:

| commit | pass | gate | detail |
|---|---|---|---|
| `4a53447` | `p414` | 🔴 `exit=1` | `register newest=p413; agents/top.md newest=p414; stale by 1 pass(es)` |
| `1d3f173` | `p415` | 🔴 `exit=1` | `stale by 2 pass(es)` |
| `ea583bf` | `p416` | 🔴 `exit=1` | `stale by 3 pass(es)` |
| `20aa033` | `p417` | 🟢 `exit=0` | green — `p417` repaired it |

🟢 **It would have fired on `p414`, the pass the drift started** — not three
passes later. That is the whole value: the failure was visible from the first
instance, and nothing was looking.

## Findings

| code | meaning |
|---|---|
| `P418-REGISTER-STALE` | the register's newest pass is behind a shelf's newest pass; the detail names both and the distance |
| `P418-NO-HEADER` | a file carries no `` ## 🆕 `pN` `` header, so its currency cannot be established — reported, never skipped silently |
| `P418-NO-INPUT` | called with fewer than two paths; **refuses** (exit `2`) rather than printing `total 0` |

## Parser contract

The pass number is the first backticked `pN` on an **h2 marked 🆕**, anchored at
line start. Three negative controls in the suite pin this, because each is a way
a naive `grep` gets it wrong:

- a header **quoted inside a table cell** is not a section of the file;
- an `###` is not an `##` — heading level is a type contract (`p383`);
- a `## ` header **without** the 🆕 marker is a superseded block, not a pass.

And the newest is a **maximum**, not the first match, so section order cannot
change the answer.

## Run

```sh
cd compose/code/p418-register-currency-gate && python3 -I test_gate.py   # 16/16
# or from the repo root, via the standing check:
make gate-register-currency
```

🔵 Green under `python3 -I` — the suite re-inserts its own directory on
`sys.path`, per `P115-AK`, so the documented invocation is the one that works.
