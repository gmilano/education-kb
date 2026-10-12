# `p144-population-audit` — `ACTION DU`

> Ask whether `T37` applies to this KB's OTHER population-defined probes. Audit the subject
> lists of `p142-origin-at-scale`, `p141-pom-chain-sweep` and `p140-live-surface-bound` for
> trees that the artefact does not ship.
> 🔴 *Refuted if none of the three includes a non-shipped tree.*

## Verdict: 🔴 **DISCHARGED and REFUTED on the literal criterion — and it returns something better**

🔴 **On the criterion as registered, none of the three has the defect `librus-mcp` had.** The
falsifier fires and `T37` is not a pattern across these probes.

🟢 **But each of the three fails the criterion for a different reason, and the three reasons
together say what `T37` should have said.**

| probe | population unit | non-shipped tree? | verdict |
|---|---|---|---|
| `p140-live-surface-bound` | published npm tarball (8) | 🟢 **NO — 0 of 8** contain `examples/`, `docs/`, `tests/` or `scripts/` | 🟡 **CLEAN BY ARTEFACT, NOT BY CODE** |
| `p141-pom-chain-sweep` | Maven coordinate (5) | 🔴 **YES — 3 of 5** inherit their licence from a parent POM that is never distributed | 🟢 **NON-SHIPPED BUT PROPERTY-BEARING** |
| `p142-origin-at-scale` | git commit (44 repos) | n/a — measures no trees | 🔴 **CONTAMINATED, DIFFERENT KIND** |

## 🆕 `T39` — exclusion must be property-relative, and `p141` is the proof

🔴 **`p141` includes non-shipped artefacts on 3 of 5 rows and is RIGHT to.**
`org.verapdf:verapdf-library:1.30.3` declares no licence of its own; its licence lives in
`org.verapdf:verapdf-parent:1.30.1`, three levels up a chain of POMs that ship with nothing.
🟢 **Excluding the non-shipped parent would delete the very property being measured.**

🔵 **So "not shipped" is not a defect in itself.** What made `legacy_reference/` a defect is
that it did **not carry the property** — a dead reference server tells you nothing about the
shipped tool surface — while a parent POM **does** carry the effective licence.

> **`T39`**: a population exclusion is sound only relative to the property measured. Exclude a
> non-shipped tree when it cannot bear the property; include it when it is where the property
> lives. A blanket `NOT_SHIPPED` list is a heuristic standing in for that test, and
> `ACTION DS` shows nine of its eleven names are currently standing in for nothing.

## 🟡 `p140` is safe by luck, and `ACTION DP` spent the luck

🔴 **`surface_bound.py` has no `NOT_SHIPPED` exclusion of any kind, and does not skip `dist/`
or `build/`.** It is sound today only because its subjects are *published tarballs*, which are
shipped by construction — npm applies `files`/`.npmignore` before publishing.

🔴 **Point the same instrument at a repository and it breaks immediately.** `ACTION DP` did:
`canvas-mcp-server` and `mcp-canvas-lms` **commit their own `dist/`**, so a clone holds source
*and* a stale bundle, three and two server instances are found, and the count is suppressed as
`MULTI_SURFACE` — **54 tools read as 0**. 🔵 **`p140`'s correctness is a property of its
artefact choice, not of its code**, and that distinction is now recorded rather than assumed.

## 🔴 `p142` carries a population defect of a kind `T37` does not describe

🔴 **9 of 44 rows count BOT commits as evidence of a human author's location**, 123 commits in
all. The instrument takes a `dominant_offset` over every commit.

| row | bot commits | of total | share |
|---|---|---|---|
| 🔴 `nitsuah/bb-mcp` | **78** | 241 | 🔴 **32.4%** |
| `BetterSEQTA/BetterSEQTA-Plus` | 22 | 2 255 | 1.0% |
| `alejooroncoy/campus-cli` | 11 | 582 | 1.9% |
| `BetterSEQTA/DesQTA` | 5 | 1 559 | 0.3% |
| `malkreide/global-education-mcp`, `oliverhruby/edupage-mcp` | 2 each | 151 / 111 | 1.3% / 1.8% |
| `krzysztofbury/librus-mcp`, `trindadetiago/sigaa-caiu`, `zijinz456/OpenTutor` | 1 each | 106 / 42 / 191 | ≤2.4% |

🔴 **`nitsuah/bb-mcp` is the row where it bites**: `dependabot` commits at **both `+0000` and
`-0400`**, so a third of that row's offset evidence was written by a robot. 🟢 **`ACTION DT`'s
instrument excludes bots** for exactly this reason, and its author list for that row drops from
four to two.

🔵 **The defect is not a non-shipped tree — it is a non-human author.** Same shape as `T37`, a
population carrying members the measurement must not count, transposed from files to commits.
🟢 **And the aggregate would not have shown it**: 8 of 9 rows are under 2.5%, which is noise,
and the one that matters is 32%.

## Run

See `result.2026-10-12-p144.tsv` and `bot-commits.2026-10-12-p144.tsv`.
