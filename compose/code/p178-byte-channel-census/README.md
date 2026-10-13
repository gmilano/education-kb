---
industry: education
region: Global
updated: 2026-10-13
---

# `ACTION KU` — the byte-count channel, from its inputs rather than its outputs

**Pass `178` of `2026-10-13`.** `ACTION KS` (p177) proved from its OUTPUTS that one of two
byte-count channels in this repository silently drops a trailing line feed: `8` of `12` published
licence byte counts were short by exactly `1`. `ACTION KU` was pre-registered to find the CALL SITE.

🔴 **It found `12`, and then it found the repair — already written, already tested, already in this
repository since `2026-10-09`.**

## The mechanism, stated before anything was measured

| channel | idiom | behaviour |
|---|---|---|
| **FULL** | `wc -c < file`, or `curl … \| wc -c` | nothing is stripped — a pipe and a redirect both preserve the trailing newline run |
| **STRIPPING** | `body=$(curl …)` then `printf '%s' "$body" \| wc -c` | POSIX command substitution deletes **ALL** trailing newlines before `printf` runs, so the count is the file size minus that run |

Licence files almost always carry exactly one trailing `LF`, which is why the shelf saw `+1`.
🔵 **The rule must still be stated as *"the entire trailing run"*, not *"one byte"* — a point
`lib/payload_measure.sh` already makes and `ACTION KS` got slightly wrong.**

## What is here

| file | what it does |
|---|---|
| `two_channels.sh` | measures one licence through BOTH channels, on the same bytes, in the same second, and records `md5` + trailing-`LF` state. **Channel B is a deliberate control and is allowlisted by the gate.** |
| `call_sites.sh` | the static census: every byte-count call site in `compose/code` and `ingest`, classified `STRIPPING` or `FULL` |
| `check_channel.sh` | 🟢 **THE GATE.** Exits `1` on any unmarked stripping site. This is the deliverable |
| `test_check_channel.sh` | `6`/`6`. Fixtures built in a scratch tree so the suite never depends on the repository it guards (`P355`) |
| `result.two-channel-census.2026-10-13-p178.tsv` | `20` rows — every byte count this KB has published — on both channels |
| `result.call-sites.2026-10-13-p178.tsv` | the raw static census, `44` `FULL` and `17` `STRIPPING` matches before the comment filter |
| `result.gate.2026-10-13-p178.tsv` | the gate's findings against the live tree: `12` |

## Results

🟢 **Live control, and it reproduces p177's figures exactly on an independent read:**

| repo | FULL | STRIPPING | Δ | trailing `LF` |
|---|---|---|---|---|
| `dodona-edu/dolos` | `1 084` | `1 083` | `1` | YES |
| `ls1intum/Artemis` | `1 091` | `1 090` | `1` | YES |
| `Selleo/mentingo` | `1 062` | `1 062` | `0` | 🔵 **NO — nothing to strip** |

🟢 **Census: `20` of `20` rows measured. `18` end in `LF`, `13` were published short by exactly `1`,
`7` were exact.** The `5` corrected at p178 are `37743/Classroom-VR` → `1 079`,
`Arux-Software/Bright` → `1 076`, `opensacorg/learning-blocks` → `1 076`, `eagles-edu/sis` →
`1 067`, `kirilxd/claude-tutor` → `1 064`.
🟢 **`0` rows remain unaudited, and every row now carries an `md5`.**

🔴 **Static census — LIMB `2` of the falsifier FIRES: `12` live sites, in `12` files, across `10`
instruments.** `p117-second-channel` *(×2)*, `p122-prose-licence-census`,
`p170-headref-license-sweep`, `p206-erp-layer-license`, `p211-case-retro-sweep`,
`p250-commercial-use-axis`, `p324-corpus-upstream-cession`, `p326-titleholder-book-license` *(×2)*,
`p560-epl-mpl-version-read`, `p784-licence-scope-map`.

## 🔴 The finding that should have been p177's

[`../lib/payload_measure.sh`](../lib/payload_measure.sh), written at pass `74` of `2026-10-09`,
**already names this defect `P834`**, already measures it *(trailing newlines `0`/`1`/`3` → delta
`0`/`1`/`3`)*, already ships `size_of_file` as the byte-exact primitive, and already preserves the
broken form as `size_of_capture_BROKEN` with *"NEVER use this to publish a figure"* above it.

🔵 **`T280`: a defect fixed in a library is not fixed until something makes its absence FAIL.**
That is why this folder's deliverable is a gate and not a number — and why `ACTION KY` (repair all
`12` sites) is a separate, pre-registered action rather than something quietly done here.

## Usage

```bash
bash two_channels.sh <owner/repo> [<path>] [<branch>]   # one subject, both channels
bash call_sites.sh                                      # static census, TSV on stdout
bash check_channel.sh                                   # THE GATE — exit 1 on any unmarked site
bash test_check_channel.sh                              # 6/6
```

🟡 **Allowlisted as deliberate controls:** `lib/payload_measure.sh`
(`size_of_capture_BROKEN`), `two_channels.sh` (channel B), and `test_check_channel.sh` — whose
trailing-newline fixture the gate caught on its FIRST run. 🔵 **It was allowlisted rather than
reworded, because the measurement IS the control and `T276` says a gate reports its own scope.**
