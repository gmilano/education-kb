---
industry: education
region: Global
updated: 2026-10-13
---

# `ACTION KW` — `dolos` on a real corpus, with a ground truth

**Pass `179` of `2026-10-13`.** `ACTION KW` was pre-registered at p177, carried unattempted at
p178, and is DISCHARGED here. 🟢 **`LIMB 2` FIRES.**

`ACTION KQ` (p177) verified [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) past its
licence and measured its language coverage and false-positive behaviour **on its own controls**.
`ACTION KW` asked the question a client asks instead: run REAL code through it.

## What was run

`@dodona/dolos@2.9.3` from `npm` *(`npm` is reachable from this environment; `PyPI` is not — see
`gap 139`)*, Node `v22.22.0`, tree-sitter `^0.25.0`.

**Corpus:** the `13` Python modules and test files of [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom)'s
FastAPI backend — `MIT`, `HEAD b3918981bb34`, `3 965` lines — which is the same repository this
pass read for `ACTION KX`. 🔵 **Deliberate: the corpus is auditable from this KB's other evidence
instead of being a private fixture.**

**Ground truth, which real code otherwise lacks:**

| file | role | how it was made |
|---|---|---|
| `p_rename.py` | 🟢 known POSITIVE | `recommendations.py` with every identifier mechanically renamed — the transform a student actually performs |
| `p_rename_reorder.py` | 🟢 known POSITIVE | the same, with top-level `def`/`class` blocks emitted in reverse order |
| the other `13` | 🔵 known NEGATIVES | real sibling modules: same framework, same ORM, same test style, same author. The HONEST false-positive test |

**Template for the `-i` limb:** built from the lines the real files actually share — every
`import`/`from` line present in `≥ 3` modules. `10` lines.

## The four criteria, fixed before the numbers were seen

| # | criterion | result |
|---|---|---|
| `M1` | top-`5` membership changes | 🔴 `False` — identical sets |
| `M2` | a known positive moves `≥ 2` ranks | 🔴 `False` — all three move `0` |
| `M3` | median `|Δ similarity| ≥ 0.02` | 🔴 `False` — median `0.00064`, max `0.04515` |
| `M4` | positive/negative separation changes sign | 🔴 `False` — `A = 1`, `B = 1` |

🔴 **None fired → `LIMB 2`: on this corpus, template exclusion does not change the ranking. The
`-i` step in Pattern `1` is CARGO CULT as written.**

## 🟢 But the pass's useful findings are the other two columns

| measurement | run A (no `-i`) | run B (`-i`) |
|---|---|---|
| pure identifier rename | **`1.0000`** | `0.9889` |
| rename + block reorder | `0.9898` | `0.9786` |
| highest known NEGATIVE | `0.6720` *(`test_courses` ↔ `test_full_flow`, overlap `1 307`, longest fragment `56`)* | `0.6720` |

- 🟢 **Identifier renaming is completely ineffective against `dolos`: `1.0000`, a perfect score.**
  It fingerprints the parse tree, so the rename is invisible to it. Reordering top-level blocks
  costs `0.0102`. 🔵 **For an education engagement this is the headline: the two transforms
  students actually use do not work.**
- 🔴 **And the number that should set the threshold: real sibling code that merely shares a
  framework scores up to `0.6720`.** The gap between the best negative and the worst positive is
  **`0.3066`**. 🔴 **A `0.7` threshold — the round number a client reaches for — sits `0.028` above
  the honest-work band and would flag it on the next, slightly more similar, pair.** 🟢 **The
  threshold belongs in the empty band, near `0.85`.**

## 🟡 Why `LIMB 2` fired, stated so the next pass does not over-read it

The template is `10` lines against modules of `2`–`63` KB, so excluded fingerprints are a
negligible fraction of each submission. 🔵 **`T284`: `-i` can only matter when the handed-out
template is a LARGE FRACTION of the submission.** That is the scaffolded-assignment case, and it
is exactly the case this corpus does not contain. 🟢 **So Pattern `1` keeps `-i` but must now
state the condition, rather than prescribing it unconditionally** — and `ACTION LB` pre-registers
the measurement that would settle it.

## Usage

```bash
bash build_corpus.sh <bloom_backend_dir> <out_dir>        # corpus + 2 positives + template
dolos run -l python -f csv -o out-noi  <out>/corpus/*.py  # run A
dolos run -l python -f csv -o out-i -i <out>/template.py <out>/corpus/*.py   # run B
python3 -I compare_runs.py out-noi/pairs.csv out-i/pairs.csv                 # the limbs
```

`result.dolos-template-limb.2026-10-13-p179.txt` is the full output of the last step.

🔵 **Reproducibility caveat, declared:** the corpus is built from a third-party `HEAD`, so a later
pass must pin `b3918981bb34` to reproduce these exact numbers (`T281`).
