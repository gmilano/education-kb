---
industry: education
region: Global
updated: 2026-10-14
---

# `P1059` — the licence COLUMN at full depth, and the three ways an instrument manufactures a contradiction

**Pass 191 · 2026-10-14 · 24/24 controls passing · 1 273 trees enumerated, 0 refusals**

## What `ACTION NK` asked for, and why it is not what ran

`ACTION NK` registered: *run the full `156`-variant `P1057` sweep over all `160` published
licence rows*. 🔴 **Both halves of that instruction were wrong, and both are findings.**

| the instruction | why it does not hold |
|---|---|
| `156` **case variants** | 🔴 a variant list is still a LIST. It cannot reach `aoe-web-frontend/LICENSE` *(depth)*, `LICENSE/LICENSE.code` *(a licence DIRECTORY)*, `debian/copyright` *(packaging)* or `LICENSE.GPL` + `LICENSE.MPL` *(family suffix)*. 🟢 **`P441` already proved the generalisation in this KB** — *a filename list can only FIND a licence; to sustain its ABSENCE you must ENUMERATE the tree* — and `ACTION NK` was written one instrument behind it |
| `160` **published rows** | 🔴 `160` was what p190 happened to sweep, not the population. Derived from the pages themselves, the population is **`1 273` slugs carrying a published licence id** — so p190's *"all published licence rows"* was `13`% of them |

🟢 **So the sweep enumerates trees instead of guessing paths**, over the whole population,
and every case variant `P1057` would have probed at the root is a strict subset of what
`git ls-tree -r` returns.

## The result

| verdict | n | |
|---|---|---|
| 🟢 `AGREE` | **1 037** | an own grant is present and its family matches a published id |
| 🟡 `FAMILY-AMBIGUOUS` | **141** | the payload NAMES more than one family — `P441`'s `?`, handed over as a reading list, never decided |
| 🟡 `TEXT-ABSENT` | **78** | the tree holds no licence text, yet a licence is published *(`Gap 421`'s family: a registry classifier, a badge, a `pyproject.toml` string)* |
| 🔴 `CONTRADICTED` | **2** | an own grant is present and no published id matches it |
| 🟡 `BUNDLED-ONLY` | 6 | every grant found belongs to a vendored dependency |
| 🔴 `UNRESOLVABLE` | 8 | the repository does not resolve over `git` |
| 🟡 `PAIRING-AMBIGUOUS` | 1 | the only row naming this slug also names other repos and other ids |

🔴 **`ACTION NK` limb `2` fires** — `≥1` contradicted — but at a rate of **`2` in `1 273`**,
and both are small single-repository rows, not platforms:

| slug | this KB published | the tree holds | where |
|---|---|---|---|
| [`linyeping/GemMate`](https://github.com/linyeping/GemMate) | 🔴 `MIT` | 🟢 **`Apache-2.0`** *(`LICENSE`, `11 305` B)* | `repos/trending.md` + `compose/patterns.md` ×2 |
| [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) | 🔴 `MIT` | 🟢 **`GPL-3.0`** *(`LICENSE`, `35 183` B)* | `agents/top.md` + `agents/trending.md` — while `repos/foundations.md` **already carries the correction** |

🔵 **`edupage-mcp` is the more interesting of the two**, because the correction already
happened: `repos/foundations.md` publishes `🔴 AGPL-3.0 → 🟢 GPL-3.0` and two other pages
still say `MIT`. 🟢 **A full-depth sweep over the whole population is how a KB finds the
pages a correction did not reach.**

## 🔴 The three defects this instrument found in ITSELF, in the order it found them

Its first build reported **`6`** contradictions. Read against the pages, **three were its
own**, and each has a control in `test_column_full_depth.py`.

| # | the defect | the row it accused | the fix |
|---|---|---|---|
| `1` | **cross-product pairing.** A row naming several repos and several ids paired every slug with every id | 🔴 `AlexandreL0pes/q-scraper` accused of contradicting an `Apache-2.0` that belonged to `adiel-calixto/IFAcademico`, four cells away | an id is attributed only from a line carrying **exactly one** slug; a slug seen only on multi-slug lines is `PAIRING-AMBIGUOUS`, never contradicted |
| `2` | **a prose id read as the published id** | 🔴 `opencast/opencast` — which publishes `ECL-2.0` and EXPLAINS it in the same cell as an *"OSI-approved `Apache-2.0` derivative for universities"* | survivable without a prose parser: ANY published id matching the tree settles the row |
| `3` | **vocabulary drift between the two halves.** The extractor's id list lacked `ECL-2.0`; the comparator's family map had it | 🔴 `sakaiproject/sakai` *and* `opencast/opencast` — the two largest platforms on the shelf, both published correctly, both reported wrong | one vocabulary, in `published_rows.IDS`, and `column_full_depth` **raises at import** if the family map does not cover it |

🔵 **Defect `3` is the one worth carrying forward.** The row that is misread is not the
sloppy row — it is the row that is **most carefully documented**, because a cell that
explains its licence against a better-known one contains two ids, and an extractor that
cannot spell the first will find the second. 🟢 **Rule: when two modules each carry a
vocabulary, the drift between them is a defect with no symptom. Assert it at import.**

## Declared limits

- 🔴 **Comparison is at FAMILY level.** `family_of` answers `GPL`, not `GPL-3.0`, so a
  published `GPL-2.0` against a GPL-3.0 tree reads `AGREE` here. Version discrimination is
  `lib/licence_identity.title_version`'s job and `P613`'s; asserting it from a coarse family
  would manufacture a fourth class of false contradiction.
- 🟡 **`TEXT-ABSENT` is not `CONTRADICTED`,** deliberately. Collapsing them would turn this
  KB's own documented `Gap 421` shapes into refutations.
- 🟡 The population is **slugs on published table rows**. A licence named in a sentence is
  not a published row.

## Run

```sh
python3 test_column_full_depth.py                      # 24/24, offline
python3 -I published_rows.py /path/to/education-kb > population.tsv
python3 -I column_full_depth.py population.tsv > result.tsv
```

## Files

- `published_rows.py` — the population, from the pages, with the pairing rule
- `column_full_depth.py` — `P441`'s tree channel + the published-vs-tree comparison
- `test_column_full_depth.py` — 24 controls, offline, three of them the defects above
- `population.2026-10-14.tsv` (`1 273`) · `result.2026-10-14.tsv` — **authoritative**
