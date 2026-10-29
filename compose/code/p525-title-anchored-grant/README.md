# `p525` — title-anchored grant classifier

## What this is

A replacement for `spdx_of()` in [`ingest/probe-grant.sh`](../../../ingest/probe-grant.sh), plus the
control harness that proves it, plus the promotion-gap sweep it was built to serve.

## Why it exists

The standing probe classifies a licence by **scanning the body**. `p525` measured what that does to
the three grants `p520` refused for paid client work:

| Address | Served grant | `probe-grant.sh` | Correct |
|---|---|---|---|
| `CaviraOSS/PageLM` | bespoke; **prohibits redistribution**, demands revenue share | 🔴 `MIT` | `BESPOKE-NONCOMMERCIAL` |
| `xiaoyang111222/cn-math-taxonomy` | title line: *"Attribution-**NonCommercial** 4.0 International"* | 🔴 `CC-BY-4.0` | `CC-BY-NC-4.0` |
| `canyongbs/advisingapp` | title line: *"Elastic License 2.0"* | 🔴 `unknown-text` | `Elastic-2.0` |

One cause: the family is on the **title line** in all three cases, and a body scan never reads it.
`PageLM`'s payload *opens* with MIT's own first sentence and then takes the grant back over 8 KB.

## Files

| File | What it is |
|---|---|
| `title_grant.py` | the classifier. Title block (first 200 B) first; `BESPOKE` for a non-canonical title; `NonCommercial` kept in the family; body fallback labelled `(BY-BODY)` / `body-only`; `UNREADABLE` rather than a guess |
| `controls.tsv` | 13 controls, each a case this base recorded by hand, with expected family **and** expected confidence band |
| `run_controls.sh` | fetches each control at its **pinned SHA** and compares. `13/13 PASS` → `result.controls.2026-10-29-p525.tsv` |
| `candidates.txt` | the 138 addresses `agents/top.md` names and does not shelve |
| `sweep_unshelved.sh` | resolves each default ref over the git protocol, probes 7 grant filenames, classifies from bytes |
| `result.sweep-unshelved.2026-10-29-p525.tsv` | the sweep: **71 permissive**, 23 copyleft, 14 refused, 26 `UNRESOLVED-on-7`, 1 dead |
| `permissive_unshelved.txt` | the 71 permissive addresses, before the shelf cross-check that reduced them to 39 |

## How to run

```sh
cd compose/code/p525-title-anchored-grant   # p355/p229: these suites only pass from their own dir
./run_controls.sh                           # expect PASS on all 13 rows
./sweep_unshelved.sh                        # ~138 addresses, needs github.com + raw.githubusercontent.com
```

## Three things that will bite the next pass

1. 🔴 **Never add `shopt -s nocasematch` to `probe-grant.sh`, and never lowercase a payload before
   its `case`.** The GNU branches are correct *only* because their patterns are uppercase and bash
   `case` is case-sensitive — `oat-sa/tao-core`'s GPLv2 contains the mixed-case string *"GNU Lesser
   General Public License"*, so a case-insensitive match grades every GPL-2.0 row here as `LGPL`.
   (`Gap 525-A`.)
2. 🔴 **`UNRESOLVED-on-7` is not a nil.** This sweep probes seven filenames; `probe-grant.sh` probes
   53. `rasbt/LLMs-from-scratch` serves Apache-2.0 at `LICENSE.txt` and would be one of the 26.
3. 🔴 **`bash cannot export an array.**` `sweep_unshelved.sh`'s name list must stay *inside* `one()`,
   and the HEAD SHA must be matched as 40 hex — the `--symref` line also ends in `HEAD`. Both
   mistakes were made here first and each reported `137 of 138` addresses ungranted.
