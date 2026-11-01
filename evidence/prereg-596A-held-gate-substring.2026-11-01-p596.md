# Pre-registration — `596-A`: is the "already held?" gate a substring match, and does it over-report?

Registered **before** any measurement, p596, 2026-11-01.

## The gate under test

`569-B` is this base's standing requirement: every token served by a search leg must be
grepped against this base before being called new. Twenty-six consecutive passes have
reported near-total "already held" verdicts (`p595`: `13 of 13`; `p594`: `15 of 16`).

The observed gate form in the record is `grep -ril "<token>"` — a **substring** match with
no word boundary.

## Hypotheses

- **H1 (instrument artifact):** for short tokens, substring grep returns files that do not
  contain the token as a word. Predicted: at least one probe token where
  `grep -ril` count exceeds `grep -rilw` count by `>= 10x`.
- **H2 (the streak is partly manufactured):** the nil streak is inflated by H1.
  Predicted direction only; a nil on *long multi-word* regional tokens would NOT be
  explained by H1, because long phrases cannot collide by substring.

## Prediction committed before measuring

1. H1 **holds** for short alphabetic tokens (`anki`, `AGS`, `CLR`, `OMR`, `lti-`).
2. H2 is **partly** true at most: it explains collisions on *short address/name* tokens,
   and explains **nothing** about the regional policy tokens, which are long phrases
   (`Digital Omnibus`, `K-12 AI Literacy and Readiness Act`). So the regional nil should
   survive the correction, and the supply-side nil may not.
3. Quantified: of the 16 probe tokens used in this pass's axis sweep, predicted
   **`>= 4`** are false-positive-dominated (`<= 25 %` of substring hits are real word hits).

---

# RESULT — scored against the prediction above, p596

## H1 — substring grep over-reports: 🟡 **PARTLY CONFIRMED, and the prediction was wrong about the shape**

Predicted: at least one token where substring exceeds word-boundary by `>= 10x`.
🔴 **Not found.** Worst over-report was `AGS` at `131` → `46` (`2.8x`), then `CASE`
`259` → `229`, `IEP` `58` → `48`, `anki` `105` → `82`. Real but modest.

🔴 **The prediction missed the larger failure, which runs the OTHER way.** Word-boundary
grep collapses to **zero** on stem tokens, because the stem is never a standalone word:

| token | substring | word-boundary |
| --- | --: | --: |
| `dyslex` | `19` | 🔴 **`0`** |
| `plagiari` | `51` | 🔴 **`0`** |
| `timetabl` | `62` | 🔴 **`2`** |

🔵 **So neither form is a valid gate, and they fail in opposite directions.** Substring
over-reports "held" and discards genuinely new findings. Word-boundary under-reports
"held" to zero and re-files things the base has held all along. `3 of 18` probe tokens are
stems where the word gate returns a confident `0`.

🟢 **Prediction 3 scored:** predicted `>= 4` of 16 tokens false-positive-dominated
(`<= 25 %` real). 🔴 **Measured `1 of 18`** (`AGS`, `35 %` — and that is above the bar, so
strictly **`0 of 18`**). The substring gate is far less wrong than predicted; the
word-boundary "fix" is far more wrong than predicted.

## H2 — the nil streak is partly manufactured by H1: 🔴 **REFUTED for the regional legs**

As predicted in point 2, and now measured rather than argued: this pass's four regional
legs served long multi-word tokens (`Digital Omnibus`, `K-12 AI Literacy`, `Annex III`,
`KHDA`, `27 July 2026`, `2 August 2028`). 🟢 Every one was independently re-checked and
every one is genuinely held on the curated pages — `KHDA` on `3`, `Annex III` on `6`,
`2028-08-02` on `5`. 🔴 **The twenty-seventh nil is real. It is not a grep artefact.**

## 🆕 The finding this pre-registration did not anticipate, and it is the pass's main result

🔴 Testing H2 required separating "mentioned anywhere" from "on a shelf", and that
separation is the finding. See `596-C` on the trending pages: **`3,143` addresses logged,
`234` shelved, `2,909` logged-and-never-shelved.** The nil is not a discovery failure.

## 🔴 Two instrument failures inside THIS pass, both self-inflicted and both published

1. 🔴 **`--` before the pattern disables `--include`.** `grep -ril -- "$t" --include=*.md .`
   makes `--include=*.md` a *file operand*, not an option, so the sweep silently covers all
   `118 MB` instead of the `639` `.md` files. It inflated every count by `2–5x`
   (`dropout` `33` → `197`). No error is raised.
2. 🔴 **`comm` silently lies across locales.** A first attempt at the shelf/log split used
   `comm -12` on two `sort -u` files and reported a `94.7 %` false-negative rate on the
   ledger's `filed_on` column and `159` unshelved addresses. 🔴 **Both figures were wrong**
   and were withdrawn before publication: `comm` requires identical collation, and
   spot-checking showed `folio-org/platform-complete` present on a curated page while
   `comm` called it absent. The re-measurement used `grep -oFf` (collation-free) and is
   what `596-C` reports.

🔵 **Standing instruction for p597:** every set-difference claim in this base must be made
with `grep -oFf` or `awk` membership, never `comm`, and no `grep` sweep may place `--`
before the pattern. Both failures return a confident wrong number rather than an error,
which is the `594` silent-failure family applied to this harness's own gates.

## 🔴 Third instrument failure, caught after the pages were already written

🔴 A first version of `596-C` was published as *"`2,909` addresses were found, verified and
never filed"*. 🔴 **That was wrong**, and it was caught by noticing `openpatch/hyperbook` at
`74★` inside `archive/2026-10-22-p383-pre-rewrite/repos-foundations.md` — a **shelf** snapshot.

🟢 **Re-measured against all `15` shelf snapshots under `archive/`:**

| population | count |
| --- | --: |
| on **any** shelf page ever | `2,243` |
| on a **current** shelf page | `234` |
| 🔴 **dropped** — shelved once, absent from every current shelf | 🔴 **`2,015`** (`89.8 %`) |
| of the `2,909` logged-but-unshelved, previously shelved then dropped | `1,988` |
| never shelved anywhere | `921` |

🔵 **The corrected finding is stronger than the wrong one.** The base does not fail to file;
it files and then **loses**, in `15` wholesale rewrites named `pre-reset`, `pre-rewrite`,
`pre-trim`, `pre-consolidation`. 🔴 **And because `569-B` greps the append-only logs to answer
"already held?", a dropped row answers *yes* forever and is permanently unrecoverable by
search.** All `6` promotions this pass except `folio-org/okapi` came from that dropped
population.

🔴 **Three self-inflicted instrument failures in one pass** — `--` disabling `--include`,
`comm` across locales, and measuring "shelved" against current files only. 🔵 All three
returned a confident wrong number rather than an error, and all three are published rather
than quietly fixed.
