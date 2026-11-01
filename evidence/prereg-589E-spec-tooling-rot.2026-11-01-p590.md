# Pre-registration — `589-E`: is `Trend 41` about specifications, or about tooling decay?

- **Pass:** `p590` — `2026-11-01`
- **Written BEFORE any measurement on `topic:xapi` or `topic:qti`.** The `topic:scorm`
  figures below are `p589`'s, already published; the two new axes are unmeasured at the
  time of writing.

## What `589-E` asked

`p589` found that on `topic:scorm` the **emit-side** permissive tooling is dead — of `80`
permissive repositories, exactly **two** are alive (`jcputney/scorm-again` MIT `362★`,
`sr258/scorm-h5p-wrapper` MIT `58★`), and `adlnet/SCORM-to-xAPI-Wrapper`, from the body
that authored SCORM, is **unlicensed and archived, last pushed 2017**. `589-E`'s
prescription: test the same rot on `topic:xapi` and `topic:qti` **before** generalising.

## Definitions, fixed now

- **live** = `pushed_at` within `90` days of `2026-11-01`, i.e. `>= 2026-08-03`.
- **permissive** = `license.spdx_id` in {`MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `0BSD`, `Unlicense`}.
- **emit-side** = produces or packages conformant content/statements (a player, wrapper,
  packager, statement library), as opposed to consuming or displaying it.
- **spec-body repo** = `adlnet/*` for xAPI, `1EdTech/*` or `IMSGlobal/*` for QTI.

## Prediction

**H1 (tooling decay, the hypothesis `589-E` wants tested):** both new axes repeat the
SCORM pattern — **`<= 2` live permissive emit-side libraries per axis**, and the
spec body's own repo is **archived or `>= 12` months idle**.

**H0 (SCORM-specific):** at least one axis carries **`>= 5` live permissive emit-side
libraries**, in which case the rot is a SCORM fact and `Trend 41` must stay narrow.

## Decision rule, committed in advance

| outcome | consequence for `Trend 41` |
|---|---|
| both axes `<= 2` live permissive emitters | H1 upheld — restate `Trend 41` as *"ask whether the spec's tooling is maintained"*, delivery rule changes |
| exactly one axis `>= 5` | 🔴 **partial refutation** — `Trend 41` stays SCORM-scoped and names the axis that broke it |
| both axes `>= 5` | 🔴 **H1 refuted** — the SCORM result is an outlier, withdraw the generalisation |
| an axis denominator `< 10` | 🔴 **unmeasurable on that axis**, declared, not quietly dropped (`584-E`'s `topic:truancy` failure mode) |

🔵 Reported with raw-hit count, false-positive count and the token that fired, as `589-C`
requires. Hand-grading is mandatory: `589-C` measured a `34.5 %` false-positive rate on an
unaudited matcher.
