# `p562` — the calibrated grant re-grader

Built to close `561-F` (*"re-grade every Apache-2.0 and AGPL-3.0 row on the shelf against the new
pins — 5 of an unknown total done"*) and `561-D` (*"state the fold constant's false-match rate"*).
It closes both, and it does it from a **re-implementation of `P561-A` that was calibrated against
`p561`'s committed pins before it was trusted**: **14 of 14 sources, 70 of 70 quantities, exact.**

| file | what it does |
| --- | --- |
| `norm.py` | the stages, **fully specified** — see the table below. This is the file `562-B` exists to make unnecessary |
| `calibrate.py` | re-reads all 14 sources in `evidence/canonical-grant-normalisation.2026-10-30-p561.tsv` and checks five quantities each. **Run this first. If it is not 14/14, nothing downstream is trustworthy** |
| `sweep.py` | resolves each repository's default branch with `git ls-remote --symref`, probes candidate grant filenames on `raw.githubusercontent.com`, grades against the pins |
| `classify.py` | for every residual, detects the family from the payload and sizes the residual against the canonical `ws` length |
| `fold.py` / `fold2.py` | the `p378` fold, and the equal-length false-match probe that closed `561-D` |
| `stage5.py` | the rejected fifth stage (`562-D`) — kept so the negative result reproduces |
| `ecl.py` | the `ECL-2.0` pin attempt and the shelf-wide ECL census (`562-C`) |
| `validate2.py` | the contract checks: frontmatter, region vocabulary, ragged tables, placeholder-as-data rows, and the **measured** gap-registration matrix |

## The stages — stated with the directions `562-B` found missing

1. `raw` — the bytes, unchanged. `wc -c` and `sha256`₁₂. The convention `560-A` adopted 8-to-1.
2. `ws` — NBSP (`U+00A0`) → space, then collapse every whitespace run to one space, then `strip()`.
   Dissolves **reflow**.
3. `punct` — applied **to the `ws` output**, in this order:
   `“ ” → "`, `‘ ’ → '`, `– — → -`, `© → (C)`, `® → (R)`, and then the URL folds
   **`http://fsf.org/` → `https://fsf.org/`**, **`http://www.fsf.org/` → `https://fsf.org/`**,
   **`http://www.gnu.org/` → `https://www.gnu.org/`**.
   🔴 **The direction is `http` → `https`.** The `p561` README says only *"normalise the `fsf.org`
   and `gnu.org` URL schemes"*; the faithful opposite reading **mismatches 8 of the 14 pins**, and
   `®` and the NBSP fold are not mentioned there at all. That omission is `562-B`.
4. `case` — **rejected** by `561-E`, retained so the negative reproduces.
5. *operative body* — **rejected** for its purpose by `562-D`. It converges Apache-2.0 3/3 at a
   tighter pin (`9 032 B` / `68b43f228ea6`) but does **not** converge `ECL-2.0`.

## What it measured

- 🔴 **38 of 91** in-family rows are **canonically verbatim** while a raw-byte gate calls them
  **modified** — `41.8 %`. This is `561-F`'s rate, on a denominator of 91 rather than "unknown".
- 🔴 The fold **length** false-matches **2 of 2** on equal-length operative substitutions.
  `permit` → `forbid` **inverts the grant** and holds the folded length at **exactly 1 062 B**.
  🟢 **Publish the folded digest; never gate on the folded length.**
- 🔴 `ECL-2.0` — **4 sources, 4 distinct digests at all five stages.** No canonical digest exists.
  🟢 Grade it by the clause `specific to the needs of the education`: **4/4** ECL, **0/3** Apache,
  **0** false positives over 100 payloads.

## Two defects in this instrument, found by using it

- 🔴 A `len(payload) < 40 B` guard discarded `frappe/education`'s **19 B** grant — `560-B`'s own
  pin. **Fixed**; it re-reads as `19 B` / `1fcecf395312`.
- 🔴 A 16-name filename probe missed `scancode-toolkit`'s grant at **`apache-2.0.LICENSE`**.
  🟢 **Enumerate the tree instead of probing names** — `p393-F`'s prescription, still the right one,
  and `562-G`'s second limb.

🔵 Run every file with `python3 -I` — these pages' own guidance is that a downloaded tree is
untrusted and an interpreter must not load code from it. 🔵 `sweep.py` takes the population JSON as
`argv[1]` and writes results to `argv[2]`; it does **not** read this repository's markdown, so the
enumeration step is deliberately left to the caller (the adjacency extractor that built this pass's
population is `562-A`, and it should not be reused as-is).
