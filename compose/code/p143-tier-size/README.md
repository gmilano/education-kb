---
industry: education
region: Global
updated: 2026-10-12
---

# `p143-tier-size` — `ACTION DL`: the falsifier FIRED, the mechanism is refuted

🔴 **npm rows are NOT smaller. They carry twice the tools.** `T30`'s proposed mechanism is
refuted, and `T30` was already withdrawn the same pass by `ACTION DM` — 🔵 **two
independent falsifiers on one trend.**

## What was registered

> 🔴 **`ACTION DL`** — find the mechanism behind `T30`'s npm correlation, or demote it.
> Compare tool count and source size between the 8 npm rows and the 10 non-npm servers.
> 🔴 **Refuted if the npm rows are not systematically smaller** — which leaves `T30` a
> correlation with no proposed cause, and it must be **demoted from a trend to an
> observation**.

## Result

| | npm | non-npm |
|---|---|---|
| **median tool count** | 🔴 **18** | **9** |

🔴 **The opposite of the hypothesis.** The npm tier carries the *larger* surfaces —
`@imazhar101/mcp-canvas-server` alone declares **227** tools, more than any repository-only
row on these shelves. The proposed cause ("npm rows are simply smaller, and small projects
register literally") is refuted.

| tier | n | median tools | ships source |
|---|---|---|---|
| npm | 8 | 18 | 🔴 **1 of 8** |
| agent | 4 | 5 | 4 of 4 |
| github-only | 6 | 31 | 6 of 6 |
| foundations | 1 | 10 | 1 of 1 |

## 🔴 And the byte comparison the pre-registration asked for cannot be made

7 of the 8 npm rows ship **only compiled output**:

| package | ships | source bytes | compiled bytes |
|---|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 `dist/` only | 0 | 553 166 |
| `@ink-waffle/moodle-mcp` | 🔴 `dist/` only | 0 | 108 123 |
| 🟢 **`@n35da/brightspace-mcp`** | 🟢 **source** (`.mjs`, `lib/`) | **45 368** | 56 976 |
| `@owen-x-tech/canvas-mcp` | 🔴 `build/` only | 0 | 78 261 |
| `canvas-mcp-server` | 🔴 `build/` only | 0 | 85 399 |
| `eth-moodle-mcp` | 🔴 `build/` only | 0 | 53 873 |
| `mcp-canvas-lms` | 🔴 `dist/` only | 0 | 47 623 |
| `moodle-mcp-server-aql` | 🔴 `dist/` only | 0 | 256 548 |

🔴 **A byte count over an npm row measures a BUNDLE** — minified, inlined, dependencies
folded in. **A byte count over a git row measures SOURCE.** Those do not answer the same
question, and a tier comparison built on them would repeat, one layer down, the exact error
`T30` was written to name.

🟢 **So this probe prints both columns and books neither as like-for-like.** The one
directly comparable npm row is `@n35da/brightspace-mcp`, and 🔴 **n=1 is reported as n=1**
rather than averaged into a tier.

## What survives

🔴 **`T30` is withdrawn, not demoted.** `ACTION DL` alone would have demoted it to an
observation — a correlation with no cause. 🔴 **`ACTION DM` removed the correlation
itself**, by showing the three figures came from two instruments over two artefact kinds.

🔵 **The order matters for the record:** `ACTION DL` was registered to find a *mechanism*
for a pattern, and the pattern turned out not to exist. 🟢 **Hunting a mechanism is a good
way to discover there is nothing to explain** — the hypothesis was specific enough to be
checked, and checking it cost one probe.

🔵 **`T21` remains the counter-example that still holds** — PyPI 0% / npm 33% / Maven 83%
licence-payload — because it was stated per ecosystem from the start, measured on one
instrument, over one artefact kind.

## Run it

```
python3 -I tiersize.py tier=subject=path[=tools] [...]   # result.2026-10-12-p143.tsv
```

Tool counts are taken from `p143-surface-gate-repair` for source rows and from
`p140-live-surface-bound` for the compiled npm rows. 🔴 **That those two numbers come from
two instruments is the finding, not a convenience** — see `T36`.
