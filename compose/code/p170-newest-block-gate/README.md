---
industry: education
region: Global
updated: 2026-10-13
---

# `P170-A` region gate and `P170-B` action-label gate

Artifacts of **pass 170 (`2026-10-13`)**. Both run the half of `ACTION JF` that corrects the
instrument rather than the shelf — and both needed correcting more than once before they measured
anything.

## `check_newest_block.py` — `gap 112`, closed by being wrong twice

`ACTION JF` (registered by p169) asked for `P383` to be amended so that only one canonical
`## Opportunities by region` block is judged in an append-only file. Implementing it surfaced three
defects, all in the gate or the ACTION's own wording:

| # | defect | correction |
|---|---|---|
| `1` | `ACTION JF` said judge the **LAST** block. This KB prepends, so the last block is the **OLDEST**. | judge the **FIRST** |
| `2` | `P383` collected every `###` up to the next `##`, so finding headings like `### 🔴 T203 — ...` were judged as region labels. That is where most of `OUT-OF-VOCAB 13` came from. | the region list is the run of `###` after the canonical `##`, cut at the first finding heading |
| `3` | `MULTIPLE-BLOCKS` counted the append-only convention itself as a defect, growing by `1` per pass. | reported as `P170-STALE-BLOCKS`, **informational**, not counted |

### Result on the p169 tree

| instrument | `OUT-OF-VOCAB` | `MISSING-REGION` | `MULTIPLE-BLOCKS` | total | real defects |
|---|---|---|---|---|---|
| `P383` as published | `13` | `11` | `4` | `28` | not separable |
| `P170-A` amended | **`0`** | **`1`** | `0` *(4 informational)* | **`1`** | **`1`** |

**`27` of `28` findings were instrument noise — a `96%` false-positive reduction** on a gate that had
been reported as a growing defect count for three passes.

**And `ACTION JF`'s falsifier FIRES.** It read: *"refuted if the amended gate's count is NOT
`OUT-OF-VOCAB 0` / `MISSING-REGION 0` for the newest block — which would mean the newest block is
non-compliant and this gap was a misdiagnosis of the gate rather than of the convention."*
`MISSING-REGION` is `1`: p169's own block carries `North America`, `EMEA`, `APAC` and `LATAM`, and
not `Global`. So **both limbs are true at once** — the gate was mis-shaped *and* the newest block was
non-compliant. p169 wrote the falsifier that catches its own claim.

p170's block carries all `5` regions and the gate reports `0` defects.

### The consequence that outlived the gate

Once only the newest block is canonical, **every row a pass does not re-state is lost from the
compiled view** while remaining true in the history below it. That is `T216`, and it is how
`OpenOLAT` — `Apache-2.0`, verified at pass `138` at `10 982` bytes, re-measured to the same
`10 982` bytes at pass `170` — stayed off the permissive-LMS route for `32` passes. The gate and
`T216` are one defect seen from two sides.

## `check_action_labels.py` — `T218`, and three unsound attempts

p169 issued `ACTION JF` twice in one pass, from `agents/top.md` (penecho's grant files) and
`intel/open-gaps.md` (this gate), for two unrelated tasks.

| attempt | produced | why unsound |
|---|---|---|
| `grep -c` on the label | `10` labels with `19`–`41` "definitions" | a label appears in every pass that **judges** it. Flagging the whole tree is `P471` |
| `+ awk '{print $2}'` | the string `` `ACTION `` on every row | `awk` splits on the space **inside** the label |
| restricted to register **sections** | flagged p170's own `JJ`–`JN` | `README.md` summarises in prose and `agents/top.md` links; neither **defines** |
| restricted to register **table rows** | **`0`** duplicates among p170's labels | a definition is the row carrying the action's **falsifier** |

Standing backlog, measured not hidden: **`17` historical labels** are defined in a register table in
both `README.md` and `intel/open-gaps.md`. They predate `T218` and are not retro-fixed. The gate
exists to stop the eighteenth.

## Running them

```sh
python3 -I check_newest_block.py  ../../../intel/market.md [...] [--require]
python3 -I check_action_labels.py ../../../README.md ../../../intel/open-gaps.md [...]
python3 -I test_gates.py          # 8/8
```

Both refuse to run with no arguments (`P541`): a gate printing `total 0` having measured zero files
is indistinguishable from a clean tree.
