# `p253-captured-body-census` — `ACTION XY`

**What it answers.** `p252` registered `ACTION XY` as its highest priority after walking
into `P834` on its own first probe: *"bound the population of instruments that measure a
payload's bytes or `sha256` through a CAPTURED BODY rather than a file. `p178` and `p179`
own the class; neither counted it."* This is the count.

## The population, graded

| verdict | n | what it means |
|---|---|---|
| `CLEAN` | `180` | no content producer in a command substitution |
| `STATUS` | `51` | the capture holds a status code or a header, never a body |
| `PIPED` | `4` | the body was measured INSIDE the substitution — sound |
| `BODY-ONLY` | `66` | a body capture exists but no byte/hash measurement consumes it; `family_of`/`holder_of` are newline-insensitive, so those verdicts stand |
| `CAPTURED-SUBJECT` | `4` | the instrument measures the SAME payload by both channels, because `P834` is its subject |
| `CAPTURED-CONTROL` | `1` | `lib/payload_measure.sh`'s `size_of_capture_BROKEN`, preserved so a suite can assert the failing case |
| 🔴 **`CAPTURED-LIVE`** | **`5`** → 🟢 **`0`** | a byte count or hash taken from a shell variable holding the payload, and PRINTED. 🟢 **All five fixed in the same pass**: fetch to a file, size the file, keep the capture for the newline-insensitive classifier only. `p326/controls.sh` became `CAPTURED-SUBJECT`, printing both channels labelled, because the difference is the question it asks |

🔴 The five, each read by hand before it was pinned:
[`p117-second-channel/title.sh`](../p117-second-channel/) ·
[`p122-prose-licence-census/scan_licences.sh`](../p122-prose-licence-census/) ·
[`p326-titleholder-book-license/controls.sh`](../p326-titleholder-book-license/) ·
[`p326-titleholder-book-license/sweep_titleholder.sh`](../p326-titleholder-book-license/) ·
[`p784-licence-scope-map/probe.sh`](../p784-licence-scope-map/)

## `ACTION XY` limb 1 — the discriminator, and the three ways a naive one is wrong

`XY` warned that a pipe to `wc -c` is CORRECT and must not be swept up, with a named
falsifier: *"falsified if the rule flags `p176-grant-path-vocabulary/probe_spellings.sh`,
which pipes and is sound."* It grades `PIPED`, and a control asserts it by name.

Three further shapes had to be measured, and each was found by this instrument's own
output rather than by reasoning:

| shape | direction | where it was measured |
|---|---|---|
| a COMMENT quoting the defect in order to warn against it | 🔴 false positive | `p117-second-channel/licence.sh` — the warning read as the thing it warns about |
| `2>/dev/null` read as an output file | 🔴 **false negative** | `lib/payload_measure.sh` vanished from the census entirely |
| a hash of a FILE and a capture of the BODY on one printed line | 🔴 false positive | `p172-manifest-attribution`, `p173-apache11-family` — the capture goes only to a newline-insensitive classifier |
| `body="$(cat …)"` — a QUOTED substitution assignment | 🔴 **false negative** | `p178-byte-channel-census/two_channels.sh`, and it recovered a fifth live site |

🔵 A false negative is the worse direction: nothing downstream can notice an absence.

## `ACTION XY` limb 2 — the published figures, re-read

`XY`'s second limb: *"any instrument whose recorded SHAs were taken through a captured body
has published hashes that can never be reproduced — those cells need re-reading."*
`p326-titleholder-book-license` published both, in committed files dated `2026-10-05`.
Re-read first-hand this pass from `raw.githubusercontent.com`, FILED:

| payload | published | true | trailing run |
|---|---|---|---|
| `openstax/osbooks-calculus-bundle/main/LICENSE` | 🔴 `21 443` B, `sha256`₁₆ `ced5bed6eec9c127` | 🟢 **`21 444` B, `61288b08584b5130`** | `1` |
| `openstax/osbooks-college-algebra-bundle/main/LICENSE` | `21 013` B, `8e63d319b3d085a7` | 🟢 identical | `0` |
| `openstax/osbooks-prealgebra-bundle/main/LICENSE` | `21 442` B, `ab1a44bbba582526` | 🟢 identical | `0` |

🟢 **And the discrimination that makes this a measurement rather than a guess:** applying
the CAPTURED channel to today's payload reproduces `21 443` and `ced5bed6eec9c127`
exactly. So the payload has not changed since `2026-10-05`; the measurement lied.

🔴 **The finding worth carrying is the incidence: `1` of `3`.** A captured-body instrument
is wrong only when the payload ends in a newline run, so it is right most of the time and
wrong unpredictably — which is why the class survived `253` passes inside a base that
documented it five times.

## What this does not claim

It reads shell source lexically. A body reaching a measurement through a second variable,
an array or a function argument is invisible to it. Every verdict is a LOWER bound on the
defect. `--pin` writes [`sites.tsv`](sites.tsv), `--verify` checks it and is what
`make hooks` runs; an absent pin file is a FAILURE, never a clean census.

**Proven able to fail:** the quoted-substitution fix reverted in a throwaway copy inside
`compose/code` → `exit 1` with `4` named failures, `--verify` among them. `29/29` restored.
