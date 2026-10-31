# `p561` — the four-stage grant normaliser

Built to close `560-C` ("pin canonical digests for the other families this shelf
grades against — each from two independent sources"). It does that, and in doing
it establishes that **a byte digest is the wrong instrument for four of the five
families**, because it cannot separate formatting from content.

| file | what it does |
| --- | --- |
| `read-grant.sh` | resolves a repository's default branch with `git ls-remote --symref`, then status-gates six candidate grant filenames on `raw.githubusercontent.com`. Prints `raw` bytes (`wc -c`) and `sha256/12`, per `560-A`'s adopted convention |
| `normalise.py` | the four stages, across five licence families and 14 sources. Emits `p561-canonical-grant-census.json` |
| `residual-hunks.py` | sentence-level diff of two normalised texts — what a non-convergence actually *is* |
| `prepend.py` | inserts a pass section after a page's frontmatter without appending a duplicate (`557-C`) |

## The stages

1. `raw` — the bytes, unchanged. What `wc -c` returns and what a client's scanner hashes.
2. `ws` — collapse every run of whitespace to one space, strip. Dissolves **reflow**.
3. `punct` — fold curly quotes/dashes to ASCII, `©`→`(C)`, normalise the `fsf.org`
   and `gnu.org` URL schemes. Dissolves **typographic** variance.
4. `case` — lowercase. 🔴 **Rejected by its own measurement**: it reduced no family's
   distinct-digest count below stage 3, and it destroys the capitalisation that marks a
   defined term (`"This License"` vs `this license`). Kept in the instrument only so the
   negative result stays reproducible.

## The classifier

The **stage at which a family's sources converge** is what classifies it:

| converges at | class | meaning | family measured |
| --- | --- | --- | --- |
| `ws` | **A** | reflow-equivalent — publisher wraps, SPDX does not | Apache-2.0, 3 of 3 sources |
| `punct` | **A** | typographic only — SPDX ships `“ ” © https://fsf.org/`, repositories ship `" " (C) http://fsf.org/` | GPL-3.0, 3 of 3 sources |
| never — residual is a clause | **D** | **modified grant** | AGPL-3.0 — `openedx/openedx-platform` |
| never — residual is a form | **B** | two legitimate published forms | LGPL-3.0 — rider-only vs rider+GPL |
| never — residual is a filled placeholder | **C** | **no canonical digest exists** | BSD-3-Clause, 3 of 3 distinct; MIT already known |

Evidence: [`../../../evidence/canonical-grant-normalisation.2026-10-30-p561.tsv`](../../../evidence/canonical-grant-normalisation.2026-10-30-p561.tsv).

🔵 Run `normalise.py` with `python3 -I` — these pages' own guidance is that a
downloaded tree is untrusted and an interpreter must not load code from it.
