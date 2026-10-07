---
industry: education
region: Global
updated: 2026-10-07
---

# `p448` — the fourth channel for a slug's spelling: what the neighbours call it

**Pass 28 of 2026-10-07.** Pre-registered action **C** of pass 26.

## What it proves

`p443` found **186 of 496** shelf slugs where no channel could confirm the spelling this KB uses,
and pass 26 showed **no case oracle exists on this host** (`raw`, `git ls-remote`, `info/refs`,
rendered `github.com`, `codeload` → `200 / resolves / 200 / 403 / 403`). This adds the channel the
first three missed and needs no forge API: **the other 495 repositories on the shelf**, read from 16
manifest and README paths.

Corpus: **488 of 496** repositories returned at least one file, **7,377,680 characters**.
Calibrated before any negative was believed — planted slug → **0** citers, `vishalsachdev/canvas-mcp`
→ **2** ⇒ 🟢 **DISCRIMINATES**.

| Verdict | n | |
|---|---|---|
| `UNCITED` | **173** | 93.0% |
| `CONSENSUS-CONFIRMS` | **13** | 7.0% |
| `CONSENSUS-DIFFERS` | **0** | |
| `CITERS-DISAGREE` | **0** | |

🟢 **Prediction confirmed** (*"fewer than 40 cited ⇒ the gap is structural"*) at **13**.

🔴 **And the action's premise is refuted.** It framed 495 neighbours as *"independent spellings by
third parties"*. Audited by owner, **5 of the 13 citations are the same owner one repository over** —
which is `p443`'s already-failed self-link channel, not a third party — and **3 of the 8
other-owner citations are fork/upstream pairs this KB already holds** (`kuali/rice` → `KualiCo/rice`,
`eduNEXT/` → `Pearson-Advance/openedx-lti-tool-plugin`, and pass 26's own `FOREIGN-PACKAGE` row
`pnp-v/bo-google-classroom-mcp-server` → `faizan45640/google-classroom-mcp-server`).

🔴 **Genuinely independent third-party citations: 5 of 186 (2.7%).** A repository nobody else cites
has no external spelling, so no further channel will resolve these 173.

## Reproduce

```sh
python3 test_crossref.py                                                    # 20/20, offline
python3 crossref.py shelf.input.2026-10-07.txt targets.no-oracle.2026-10-07.txt .   # ~5 m 30 s
```

## Declared limits

- A mention is a **string**, not a resolution. `foo/bar` in a README may be a dead link, a renamed
  project or a typo. What the channel establishes is that an independent party wrote that spelling.
- The corpus is the 16 paths in `CORPUS_PATHS` at `HEAD`. A citation in any other file, or in git
  history, is not seen. The list is published with the result because the corpus definition is part
  of the measurement (`P107`).
- GitHub slugs are case-insensitive for resolution, so two spellings differing only in case both
  work. This channel reports a disagreement; per pass 26 it still **cannot say which side is
  canonical**, and it does not pretend to.
