---
industry: education
region: Global
updated: 2026-10-13
---

# `ACTION KY` — the defect is the CAPTURE, not the count

**Pass `179` of `2026-10-13`.** `ACTION KY` was pre-registered as a cleanup: *"fix all `12`
stripping call sites and see `check_channel.sh` exit `0`"*, limb `1` being *"a mechanical swap to
`size_of_file` works at every site → one commit closes it."*

🔴 **LIMB `1` IS FALSE. `1` of `12` sites can take the mechanical swap. The other `11` cannot be
repaired at the line the gate flags at all.**

## Why

`size_of_file` takes a **PATH**. At `11` of the `12` sites the payload never touches the disk — it
is a shell variable, and the trailing newline run was destroyed by the command substitution **one
line above** the line `check_channel.sh` points at:

```bash
body=$(curl -sS -f "$RAW/$slug/$br/$p")     # <- the run dies HERE, at the CAPTURE
bytes=$(printf '%s' "$body" | wc -c)        # <- the line the p178 gate flags
```

🔵 **`T283`: a gate must flag the line where the INFORMATION is lost, not the line where the loss
becomes visible.** p178's gate located the symptom, and because it located the symptom, `ACTION
KY` was written as a one-commit cleanup. It is not one.

## The three repair shapes (`result.repair-classes.2026-10-13-p179.tsv`)

| class | count | what the site holds at the count | repair |
|---|---|---|---|
| **`A`** | 🟢 **`1`** | the payload is on DISK | `size_of_file` on the path already in scope — **mechanical, one line** |
| **`B`** | 🔴 **`5`** | `var=$(curl …)`, no file exists | change the **FETCH** to `curl -o FILE`, then size the file |
| **`C`** | 🔴 **`6`** | `out=$(curl -w '\n%{http_code}')`, status line stripped back off | everything in `B`, **plus the boundary is AMBIGUOUS** |

## 🔴 Class `C` is ambiguous, not merely lossy — and that kills p178's remedy

`ACTION KS` and `ACTION KU` both treated the defect as LOSS: the figure is low by the trailing
run, so add the run back. 🟢 **That works on `A` (re-measure the file) and on `B` (re-fetch to a
file). 🔴 On `C` it is not implementable at all.** `ambiguity_proof.sh` runs the class-`C`
pipeline with the network replaced by a local fixture:

| fixture | true size | class-`C` recovery | `md5` of the recovery |
|---|---|---|---|
| `run0` *(no trailing newline)* | `38` | `38` | `597f938a7b321f71d6e6b15d9ff99190` |
| `run1` *(one)* | `39` | `38` | `597f938a7b321f71d6e6b15d9ff99190` |
| `run3` *(three)* | `41` | `38` | `597f938a7b321f71d6e6b15d9ff99190` |

🔴 **Three different sizes recover to ONE identical byte string.** There is no run left to add
back, so **no arithmetic correction to a class-`C` figure can be right for all three** — such a
figure can only be repaired by RE-FETCHING. `6` of the `12` sites are class `C`.

## 🟢 The trailing run is not always `1`, measured on real corpora

p178 wrote that licence files *"almost always carry exactly one trailing `LF`"*, and `ACTION KS`
stated the error as `+1`. `trailing_census.sh` over `21` payloads in three corpora this KB
already holds:

| corpus | payloads | with a run | run `> 1` |
|---|---|---|---|
| `p560-epl-mpl-version-read/fixtures` | `8` | `2` | 🔴 **`1`** — `epl-1.0-junit4.LICENSE`, run of **`2`** |
| `p308-phrase-anchor-sweep/fixtures` | `12` | `10` | 🔴 **`1`** — `mit-adlnet-xapi-lab.LICENSE`, run of **`2`** |
| `p288-agpl-casefold/fixtures` | `1` | `0` | `0` |

🔴 **`2` of `21` real payloads carry a run of `2`, so a blanket `+1` correction is wrong on ~`10`%
of real payloads** — which is `payload_measure.sh`'s own point (`P834` is *"the entire trailing
run"*), now measured outside its fixtures for the first time.

## 🟢 What was actually repaired

| site | class | evidence |
|---|---|---|
| `p560-epl-mpl-version-read/sweep_versions.sh` | `A` | swapped to `wc -c < "$p"`. 🟢 **Its own suite `22`/`22` GREEN after the change.** Two figures moved: `epl-1.0-junit4` `11 374` → **`11 376`** *(Δ`2`)* and `mpl-1.1-spdx-canonical` `23 668` → **`23 669`** *(Δ`1`)*. The other `6` were already exact |
| `p117-second-channel/licence.sh` | `B` | 🟢 **the reference repair, end to end.** Rewritten onto `lib/fetch_payload_to_file.sh`; now emits an `md5` column too |

🟢 **The reference repair is VERIFIED, not claimed.** The rewritten `p117` reproduces p178's
FULL-channel figures exactly — `dolos` `1 084`, `Artemis` `1 091`, `mentingo` `1 062`,
`Pyris` `1 089` *(`md5 5cc3b98…`, byte-identical to p178's record)* — and agrees with an
INDEPENDENT channel on the two rows this pass read by clone: `Study-Mate` `1 064` /
`md5 5ebdff60…` and `Bloom` `1 069` / `md5 d3ac8ed0…` match the cloned working trees exactly.

🟡 **The remaining `4` class-`B` and `6` class-`C` sites are NOT repaired.** They are a
fetch-shape migration across `10` instruments, which is `ACTION LA`, pre-registered rather than
half-done.

## 🟢 The new vocabulary, and the reason this is `T280` one layer up

[`../lib/fetch_payload_to_file.sh`](../lib/fetch_payload_to_file.sh) names the correct idiom:
body to a file, `%{http_code}` to stdout, nothing round-tripping through a variable.

🔴 **And the finding behind it: the right fetch shape has been in this repository since pass
`120`.** `capture_gate.sh`'s first run flagged `46` sites, among them
`p120-unread-grant-resolution/probe.sh`, which already writes `curl -s -o "$f" -w '%{http_code}'`
— the correct form, as a false positive of this pass's own gate. 🔵 **`P834`'s counter has existed
since p74 and `p120`'s fetch since p120; what was missing was never the knowledge.**

## `capture_gate.sh` — the second gate

Two steps, because one is either blind or deafening:
1. every variable assigned from a `curl` command substitution — the capture;
2. kept **only if** a byte count follows in the same file.

Step `2` is what keeps it honest: a capture that only feeds a CLASSIFIER is correct and is not
flagged, because `family_of`/`holder_of` are newline-insensitive and `payload_measure.sh` says so
itself. A capture carrying `-o` is skipped — the body went to a file and the substitution holds
only the code.

🔴 **It finds `24` capture sites across `14` instruments — `25` before this pass repaired `p117`, which removed one, against the `12` count sites p178 found:
the defect surface is more than DOUBLE what the count-shape gate could see.**

🟡 **Over-approximation, declared rather than hidden:** step `2` is FILE-granular, so some of the
`24` captures may feed only a classifier in a file that byte-counts something else. `12` are
proven to reach a count. 🔵 **The `12`→`24` gap is the gate's own slack, and narrowing it is
`ACTION LA`'s second limb — a gate that over-reports is still a gate, but it must say so
(`T276`).**

## Usage

```bash
bash trailing_census.sh <dir>        # trailing-run census over a corpus on disk
bash classify_repair.sh              # the 12 sites, by the repair each needs
bash ambiguity_proof.sh              # the class-C proof. exit 0 = AMBIGUOUS
bash capture_gate.sh [ROOT]          # THE SECOND GATE. exit 1 on any capture-then-size site
bash test_capture_shape.sh           # 14/14
```

🟡 **Instrument-honesty note:** `classify_repair.sh` carries the `12` sites as
`file:line:variable`, and repairing `p560` moved its count from line `62` to line `68` — the
repair's own comment shifted it. 🔵 **A line number is not an identity, exactly as a `HEAD` is not
(`T281`); the list had to be re-pinned by hand after the fix, and a later pass must expect the
same.**
