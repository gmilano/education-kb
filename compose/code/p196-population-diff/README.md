---
industry: education
region: Global
updated: 2026-10-14
---

# `p196-population-diff` — the shelf grew `27` rows and nobody re-divided; and `5` of its rows are the same repository twice

**Pass `196`, `2026-10-14`.** Runs p195's third pre-registered action.

## What was pre-registered

> *"Re-extract the shelf slug population from the CURRENT pages and diff against p192's `472`.
> **Limb 1:** the diff is small → p192's population is still usable with a footnote.
> **Limb 2:** the diff is large → **every per-shelf percentage since p192 has the wrong
> denominator**."*

🔵 p192's rule is applied **verbatim**, quoted from [`repos/foundations.md`](../../../repos/foundations.md):
*"every `github.com/<owner>/<repo>` URL appearing in `agents/top.md`, `repos/foundations.md`
and `verticals/solutions.md`, de-duplicated, with GitHub's own non-repository paths
(`topics/`, `orgs/`, `users/`, …) excluded."* **Three pages, not four.**

## Measured

| | count |
|---|---|
| p192's population *(`2026-10-14`)* | `472` |
| 🟢 **p196's population, same rule** | **`499`** |
| 🔴 added since p192 | **`27`** |
| 🟢 **removed since p192** | 🟢 **`0`** |
| 🔴 **distinct after case-folding** | 🔴 **`494`** |

[`evidence/shelf-population.2026-10-14-p196.txt`](../../../evidence/shelf-population.2026-10-14-p196.txt).

## 🟡 The limbs SPLIT, and the split is the useful part

🟢 **Limb `1` holds on the axis that would have been expensive: `0` removed.** p192's `472` is
a strict **subset** of p196's `499`. No percentage computed over it was wrong about rows that
later vanished, and this shelf still does not rot.

🔴 **Limb `2` holds on the denominator: `+27` in three passes, `+5.7`%, all on
`agents/top.md`** *(one also on `verticals/solutions.md`)*. 🔴 **And the mechanism is
structural, not sloppiness: the population is extracted FROM the pages, and the pass that
runs a census also WRITES to those pages.** A census published in pass `N` has a denominator
that pass `N`'s own writes invalidate. The `27` is the measured size of that staleness —
it is not a figure anybody chose to get wrong.

🔵 This is the same hole p195's own retraction fell into from the other side: it accused `4`
ranked rows of *"diverging"* when they were simply **absent from p192's population**.
🟢 All `4` are in this pass's `27`: `virgiliojr94/book-to-skill`,
`PetoiCamp/OpenCat-Quadruped-Robot`, `ai-infra-curriculum/ai-infra-engineer-learning`, and
`ahmedEid1/Lumen` — on which see below.

## 🆕 🔴 `5` rows are one repository counted twice — case-variant slugs

GitHub resolves owner and repo **case-insensitively**; this KB's extractors de-duplicate
**case-sensitively**. So a page that spells a slug two ways yields two population rows:

| pair | |
|---|---|
| `ahmedEid1/Lumen` ↔ `ahmedEid1/lumen` | the lowercase form is the one in p195's licence census *(`GPL-3.0`, `35 149` B)* |
| `OS4ED/openSIS-Classic` ↔ `os4ed/openSIS-Classic` | 🟢 **proved identical by measurement** — see below |
| `OpenOLAT/OpenOLAT` ↔ `openolat/OpenOLAT` | both `Apache-2.0`, `10 982` B |
| `Hesham0-0Nasser/tutor-lms-mcp` ↔ `hesham0-0nasser/tutor-lms-mcp` | |
| `ShuyunYuan/talentcoach` ↔ `shuyunyuan/talentcoach` | the `Gap 421` view-only row |

🟢 **Not an inference.** [`p196-none-tree-reach`](../p196-none-tree-reach/) independently
cloned both `OS4ED/openSIS-Classic` and `os4ed/openSIS-Classic` and the complete-tree
enumeration returned **identical figures for both** — `5 656` paths, `11` own subtree grants,
`11` bundled. One repository, two rows.

🔵 p192's `472` case-folds to **`468`** — exactly its own `LIVE` count. 🟡 **Suggestive, not
proved**: p192 attributed its `4` non-`LIVE` rows to an empty repo, an absent repo and an
extractor false positive, which is a different cause from case-variance. Recorded as a
coincidence worth one pass's attention, not as a finding.

## 🔴 The instrument's own artefacts, and what they cost to find

p192 recorded subtracting **one** artefact *"by hand"* — `repos/`, from an `api.github.com`
URL. This instrument encodes that as a rule, and then its own diff exposed two more of mine:

| version | artefact it emitted | fix |
|---|---|---|
| v1 | `repos/..` — a relative-link path segment | enumerate `.` and `..` |
| 🔴 v2 | 🔴 **`repos/...` — THREE dots** | 🔴 enumerating dot-segments **is** list-widening |
| 🟢 v3 | none | 🟢 *"a name with no non-dot character is not a repository"* |

🔴 **v1 and v2 were both list-widenings, written in the same pass whose headline finding is
that list-widening does not work** *(`P441`, see [`p196-none-tree-reach`](../p196-none-tree-reach/))*.
🔵 Recorded because the pass that names a defect is not immune to it.

## What this re-divides

| figure | as published | re-divided |
|---|---|---|
| p195's *"no licence at root"* | `88` / `468` = **`18.8`%** | over `494` distinct, with `26` rows never probed: **not computable without probing them** |
| 🟢 genuinely ungranted at any depth *(this pass)* | — | 🟢 **`76` / `468` = `16.2`%** |
| the phrase *"the whole shelf"* | p192's `472`, inherited unchanged by p194 **and** p195 | 🔴 **wrong by `27` rows, and by `5` more that are phantoms** |

## Suite

`test_extract.sh` — **`20`/`20`**, offline, over the two reserved-name predicates: the
exclusions p192's rule names explicitly, the artefact p192 subtracted by hand, the three
dot-segment forms, and nine real owners and repos from this shelf that must survive.

## Pre-registered for p197

| action | 🟢 limb `1` | 🔴 limb `2` |
|---|---|---|
| Probe the `26` population rows p195's census never reached | their licence rate matches the shelf's → `16.2`% is stable and the denominator question closes | it diverges → the `27` additions are a **biased** sample, because each pass adds what it just researched |
| Case-fold the de-duplication in every extractor on this shelf and re-run p192's existence census | `494` resolves to `494` live repositories → the phantom class closes | some case-variant is a genuine distinct repo → case-folding is itself unsafe, and say which row |
| Record the population count **in the census artefact itself**, so a pass cannot inherit a denominator without inheriting its date | every later census carries its own denominator → the staleness class closes structurally | — |
