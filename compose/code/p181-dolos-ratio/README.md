---
industry: education
region: Global
updated: 2026-10-13
---

# `ACTION LB` — does `dolos`'s `-i` effect depend on the template-to-submission ratio?

**Pass `181` of `2026-10-13`.** `ACTION LB` was pre-registered at p179, carried unattempted at
p180, and is DISCHARGED here with these limbs:

> **limb `1`:** the effect rises with the ratio and crosses `0.02` → `T284` holds and Pattern `1`'s
> condition is right.
> **limb `2`:** flat at every ratio → `-i` is cargo cult and Pattern `1` must DROP the step.

🟢 **LIMB `1` FIRES on the letter of the criterion** — median `|Δsim|` crosses `0.02` at ratio
`0.5099`. 🔴 **But the effect is NOT monotonic, and above ratio `1.0` it is HARMFUL.** The honest
reading is more useful than either limb, and Pattern `1` gains an **upper** bound rather than
losing its step.

## Why this needed measuring

p179 discharged `ACTION KW` and fired limb `2`: on a `10`-line template over a `304`-line mean
submission *(ratio `0.033`)*, template exclusion changed nothing material — median `|Δsim|`
`0.00064` over `105` pairs. Pattern `1` was then amended to make `-i` **conditional on a scaffolded
assignment**, on the *reasoning* that a bigger handout would matter. **That reasoning was never
measured.** This action measures it.

## The corpus — identical to p179's, deliberately

Rebuilt with this KB's own
[`p179-dolos-real-corpus/build_corpus.sh`](../p179-dolos-real-corpus/build_corpus.sh) against
[`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) at **`HEAD b3918981bb34`** — the same commit
p179 used, re-cloned independently. `13` real `MIT` Python modules + `2` constructed known
positives; `15` files, `4 561` lines, mean submission `304` lines. `105` pairs.

Ground truth: `p_rename.py` *(every identifier mechanically renamed — the transform a student
actually performs)* and `p_rename_reorder.py` *(the same with top-level blocks reversed)*. All other
pairs are honest sibling code sharing a framework, an ORM, a test style and an author.

Tool: `@dodona/dolos@2.9.3` from `npm`, Node `v22.22.0`.

## The ladder — `7` rungs, each built FROM the corpus

| rung | template lines | ratio | median `\|Δsim\|` | worst positive | best honest negative | separation |
|---|---|---|---|---|---|---|
| *(baseline — no `-i`)* | `0` | `0` | — | `0.9898` | `0.6720` | `+0.3178` |
| `imports_ge6` | `1` | `0.0033` | `0.00000` | `0.9898` | `0.6720` | `+0.3178` |
| `imports_ge3` *(p179's)* | `10` | `0.0329` | `0.00064` | `0.9786` | `0.6720` | `+0.3066` |
| `imports_ge2` | `13` | `0.0428` | `0.00025` | `0.9803` | `0.6720` | `+0.3083` |
| **`handout_1mod`** | `42` | `0.1382` | `0.00816` | `0.9770` | **`0.6004`** | **`+0.3766`** |
| **`handout_3mod`** | `155` | `0.5099` | **`0.02347`** | `0.9532` | `0.5951` | `+0.3581` |
| `anyline_ge3` | `300` | `0.9868` | `0.00862` | `0.9172` | `0.6251` | `+0.2922` |
| `anyline_ge2` | `512` | `1.6842` | `0.01412` | `0.8912` | `0.6016` | **`+0.2897`** |

`510`× ratio span. `105` pairs retained at every rung — no rung lost a pair.

## What it means

* 🔴 **Below ratio `0.05`, `-i` does nothing.** Median `|Δsim|` `≤ 0.00064`. p179's limb-`2` result
  was correct **for its ratio** and was over-generalised to the step.
* 🟢 **Between ratio `0.1` and `0.5`, `-i` earns its place.** The honest-work ceiling falls
  `0.6720` → `0.6004` and the separation a grader's threshold sits in WIDENS by up to `+0.0588`.
  This is the realistic case: the handout is a module or three.
* 🔴 **Above ratio `1.0`, `-i` is HARMFUL.** The known positive erodes `0.9898` → `0.8912` and the
  separation falls to `+0.2897`, **below** the no-template baseline. A template bigger than the
  submission removes the evidence.
* 🟡 **The published `0.85` threshold survives the whole ladder** — the worst positive never drops
  below `0.8912`, the best negative never exceeds `0.6720`. 🔴 **But its margin shrinks from
  `0.1398` to `0.0412` as the template grows.** A team that both raises the threshold and supplies
  a large template will start missing renames.
* 🟢 **The separation never changes sign at any rung.** `-i` does not break the detector; it tunes
  it, in both directions.

`T310`: template exclusion is not a hygiene step to always-enable or always-skip. It has an
optimum, it is on the order of one handout module, and past the submission's own size it eats the
signal it was meant to clean.

## What this does NOT establish

* 🔴 **One corpus, one language.** `Bloom`'s FastAPI backend, Python only. The ratio effect is
  measured on this corpus's structure, not proved general.
* 🔴 **The constructed positives are mechanical.** A real student's edit is not `sed`.
* 🔴 **`anyline_*` templates are machine-generated** and are deliberately *unrealistic* handouts —
  they are the upper end of the ladder, included to find where the step turns harmful, not as
  advice.
* 🔴 **The `0.02` threshold was not met monotonically.** The criterion said *"rises with the ratio
  and crosses"*; the measurement crosses once at ratio `0.51` and falls back above it. Reported as
  measured, not as predicted.

## Files

| file | what it holds |
|---|---|
| `lb_ratio_sweep.sh` | builds the `7`-rung ladder from the corpus and runs `dolos` at each rung |
| `lb_analyse.py` | computes median `\|Δsim\|`, the positive/negative extremes and the separation |
| `ladder.2026-10-13-p181.tsv` | the rungs, with template line counts and ratios |
| `result.2026-10-13-p181.txt` | the output the table above is read from |

## Usage

```
bash lb_ratio_sweep.sh <corpus_dir> <out_dir>
python3 -I lb_analyse.py <out_dir>/ladder.tsv <out_dir>/runs/base/pairs.csv
```
