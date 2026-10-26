# `p455-version-axis` — the licence reader gains a version axis (`Gap 454-C`)

Closes the axis `Gap 454-C` named, and registers five gaps of its own — four of
them defects in this pass's own instruments, three caught by controls before
anything was published.

## What is here

| file | what it does |
|---|---|
| `family_version.py` | `p454`'s title-anchored family reader **plus** a version axis: returns `GPL-2.0` / `GPL-3.0` / `LGPL-2.1` / `LGPL-3.0` / `AGPL-3.0`. Adds `only_or_later()` (the forward grant) and `compatible()` (the GNU axis only). `canon()` **preserves** the version instead of collapsing it |
| `family_title.py` | `p454`'s reader, copied verbatim and imported, not re-implemented |
| `fetch.py` | the read channel: `raw.githubusercontent.com` gated on `%{http_code}`, plus registry reads with **record-shape assertion** (`Gap 455-C`) |
| `fetch_fast.py` | the same channel with a cheap probe ladder, usable at a 481-cell denominator (`Gap 455-A`) |
| `controls.py` | **34 controls, both directions**, incl. digests earlier passes published and a fabricated negative control |
| `probe.py`, `followup.py`, `flap.py` | the candidate probe, its three resolution misses, and the registry stability measurement |
| `sweep.py`, `sweep2.py` | the GNU sweep, and its **re-attribution** after the first run's headline was retracted |

## The closure

`Gap 454-C`: *"A family-level reader cannot grade a version-level
incompatibility, and this base has one live."*

`edu-sharing/Edu-Sharing` declares `GNU GPL v2` on npm and serves GPL **v3**.
GPL-2.0 and GPL-3.0 are mutually incompatible, and `p454`'s `canon()` collapsed
both onto `GPL` and graded the pair `AGREE`. Here it `DISAGREE`s and
`compatible()` returns `False`.

The version is read from the **title block** — the same anchor `p454` chose for
the family, and for the same reason: GPLv2's preamble recommends the LGPL at
non-empty line 15, inside any 40-line window, which is the defect `Gap 454-A`
records as still unfixed in the carried `verify.py`.

`only_or_later()` reads the **whole** payload, deliberately: the forward grant
lives in the per-file notice and the *How to Apply* appendix, outside the title
block by construction. `UNSTATED` is a real answer and is never guessed —
guessing `or-later` invents a combination right, guessing `only` invents a
prohibition. Read first-hand, `oat-sa/tao-core`'s GPLv2 is `or-later`.

## What the sweep established, and what it retracted

481 addresses whose shelf line names a GNU family; 461 after cell-level
attribution. `306 AGREE (66.4 %)`, `56 UNCHECKABLE (12.1 %)`,
`11 UNDER_SPECIFIED (2.4 %)`, `20 AMBIGUOUS` (refused and named).

**`88 FAMILY_DISAGREE (19.1 %)` is retracted in full** — see `Gap 455-B`. Three
mechanisms: line-level co-occurrence, sole-address prose rows, and per-subtree
grants that a root-only reader cannot see. The shelves were right, and already
carried a taxonomy for this population (`DEPENDENCY-SCOPED`, `BOUNDARY-NAMED`)
that the sweep should have consumed instead of re-deriving.

## Defects this pass found in its own instruments

1. **`Gap 455-A`** — `HEAD` is not the default branch. `kurwjan/LanisAPI`:
   `HEAD/LICENSE` 404 with a 331 B README, `master/LICENSE` 200 (1 076 B, MIT)
   with a 3 554 B README. A ladder that accepts the first live ref publishes a
   false *ungranted*, discarding a usable permissive dependency.
2. **`Gap 455-C`** — a registry `200` with a malformed body read as "declares no
   licence". 1 of 20 reads of the same npm URL; the other 19 were correct and 12
   consecutive reads across three registries were stable, so the channel is
   sound and the single-read discipline was not.
3. **`Gap 455-D`** — `canon()`'s `\bv(\d)` cannot fire inside `gplv3`, the
   compact form registries actually serve. `p454`'s `FAMILY_TOKENS` anticipated
   it; this `canon()` did not.
4. Two **control** defects, both failing safe: an expectation of `MIT` where
   `p454` correctly grades `MIT (body form, no title)`, and an assertion that
   every GNU grade must differ from `p454`'s — wrong for `AGPL`, whose only
   live version is 3.0.

## Running it

```
cd compose/code/p455-version-axis
python3 -I controls.py     # 34/34 must pass before any verdict is read
python3 -I probe.py        # candidate set, registry -> back-link -> grant
python3 -I sweep.py        # the GNU population, parallel; writes sweep.json
python3 -I sweep2.py       # re-attribution; writes the evidence TSV
```

`-I` drops the script directory from `sys.path`, so each entry point adds it
back explicitly rather than running without isolation.

## For the next pass

Import `family()` and `canon()` from `family_version.py`, not from
`p453-vocabulary-ledger/verify.py` — `Gap 454-A` records the latter's 40-line
window as unsound and it is still unpatched. This pass did not edit it, for
`p454`'s stated reason: gate-adjacent code should not be changed by a pass that
cannot run the gate against it, and `make hooks` has now been denied ten times
in eleven passes.
