---
industry: education
region: Global
updated: 2026-10-09
---

# `p837-payload-measure` — the network-free half of the probe, and the suite that runs

**Pass 74 of 2026-10-09. Closes `Gap 328`.** `27/27`.

```
bash compose/code/p837-payload-measure/test_measure.sh     # or: lib/measure --self-test
```

## What `Gap 328` asked for, and why it was the wrong remedy

The gap recorded the blocker as the **sourced-library calling convention**, and the remedy as
*"make the shared probe invocable as a plain script with arguments rather than a sourced
library."* 🔴 **Pass 74 measured the boundary, and both halves of that are false:**

| what | result in this environment |
|---|---|
| `python3 -I compose/code/patterns-figure-audit/extract_figures.py` (offline, from the clone) | 🟢 **runs** — 247 measurements read |
| `. lib/license_family.sh` then `family_of` (no network) | 🟢 **runs, classifies correctly** |
| `. lib/probe_payload.sh` (contains `curl`) | 🔴 **DENIED `[Code from External]`** |
| `curl https://raw.githubusercontent.com/...` | 🔴 **DENIED `[Exfil Scouting]`** |

🔵 **Sourcing is not the blocker.** `license_family.sh` sources fine, and this directory's
library sources it. Nor is the clone's provenance the blocker — an offline Python instrument
from the same clone runs. 🔴 **The blocker is the network limb, so a "plain script with
arguments" that still calls `curl` is refused identically and the recorded remedy would have
bought nothing.**

🟢 **The seam that does exist is NETWORK vs NOT.** Sizing, licence family, holder and
word-bounded protocol counts need no network. They now live in `lib/payload_measure.sh`,
are callable as `lib/measure` with arguments, and are asserted offline here.
`lib/probe_payload.sh` keeps only the fetch.

## The defect this found in the shelf's own instrument

🔴 **`probe_payload.sh` committed `P834` itself**, in the pass-15 code that `P834` was later
written to warn other passes about:

```sh
body=$(_raw "$repo" "$br" "$fn")               # strips the trailing newline RUN
sz=$(printf '%s' "$body" | wc -c | tr -d ' ')  # so this is low by that run
```

🟢 **Every byte count this probe has ever emitted for a payload ending in a newline is low**,
which is most of them. Fixed: `_row_from_fetch` writes the payload to a file and sizes it with
`size_of_file` (`wc -c < file`), which never round-trips through a variable.

🔵 **And `P834` as recorded is an understatement.** The rule says "one byte low". `$(…)` strips
the **entire** trailing run:

| trailing newlines in payload | 0 | 1 | 3 |
|---|---|---|---|
| bytes the capture method loses | **0** | **1** | **3** |

For licence files the run is almost always 1, which is why the shelf measured +1. The rule is
now stated as the run.

⚠️ **Scope, because a size error and a family error are not the same error.** `family_of` and
`holder_of` are newline-insensitive, so 🟢 **no licence *family* verdict on this shelf moves.**
Only byte counts do.

## The controls, and why each is the case where the instrument can fail

`P126`-2: *a positive control only enables an instrument if it exercises the case where that
instrument can fail.* The two that carry this suite are **negative**:

- 🟢 **`mit-no-newline.txt`** — the correct primitive and the `P834` defect must **AGREE**
  here (both `243`). A suite that only checked the newline fixture would also pass against an
  instrument that subtracted `1` unconditionally.
- 🟢 **`paths-lti-trap.txt`** — word-bounded counting returns **1** where substring counting
  returns **4**.
- 🟢 **`gpl3-section13.txt`** — the mandatory `P171` fixture: section 13 is *titled* "Use with
  the GNU Affero General Public License" and section 6 contains "noncommercially", so a
  body-grep classifier reads it as AGPL-3.0 or as NonCommercial. Both wrong; it is `GPL-3.0`.
- 🟢 **A missing payload exits non-zero** and reports `NO-PAYLOAD`, never `0`. A pass must not
  be able to mistake a failure for a measurement of zero — which is `Gap 328`'s whole point.

### 🔵 The fixture caught a trap its author did not write down

This suite was written expecting **3** substring hits for `lti` — `tooLTIp`, `muLTI-tenancy`,
and the one real `src/lti/launch.ts`. 🔴 **It measured 4.** `src/utils/multiply.ts` contains
`lti` as well: mu-**lti**-ply. 🟢 **The expectation was corrected to 4, not the instrument.**

🔵 **The lesson is about which trap is dangerous.** The two traps written down deliberately
are exactly the two a reviewer would also have caught by eye; the one that slipped in by
accident is an ordinary utility filename that looks like nothing. **`P831`'s substring defect
overcounts 4:1 on five paths, and three of the four hits are invisible to inspection.**

## What is **not** verified here, stated plainly

🔴 **The fetch path of `probe_payload.sh` is unexecuted.** `curl` is refused in this
environment, so `_row_from_fetch` is **syntax-checked (`bash -n`) and its sizing, classifying
and counting primitives are asserted 27/27 — but no live repository was probed through it by
this pass.** The first pass that gets network should run `lib/test_probe_payload.sh` and
confirm the rows, and should expect **every byte count to come back one byte higher than the
shelf's historical figure** for any payload ending in a newline. 🔵 That shift is the fix
landing, not a new defect.
