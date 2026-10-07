---
industry: education
region: Global
updated: 2026-10-07
---

# `p444-root-vs-tree-family` — pass 26's action A: the root file is complete 92% of the time, and the escalation runs the opposite way

**Executes pass 26's pre-registered action A**, written as:

> Run `p441`'s tree enumeration over the **412 `LICENSED`** rows, not the 87 — the slugs
> where a root filename *did* answer — and compare the family read from the root file
> against every other licence text in the tree.
> **Prediction:** expect **more than five** repositories to carry a second, different
> grant somewhere below the root that the rooted probe never saw, concentrated in the
> **dual-licensed and monorepo** tiers. The interesting class is the inverse of this
> pass's: a repository whose root `LICENSE` is permissive and which ships a
> **copyleft** text deeper in.

## Why the `LICENSED` side is the harder half

`p441` ran the enumeration over the 87 rows where the root probe found **nothing**, so
anything it found was new by construction. Here the root probe already answered, and
the question is whether that answer is **complete**. A root `LICENSE` is one file; a
repository is a tree; nothing makes the two agree.

Every stage is imported from `p441` and `p436` rather than rewritten — rule 1 of
**P126** — so the family vocabulary, the bundled-path exclusions and the multi-family
mark counter are the ones those passes published. **The only new thing here is the
comparison.**

## Measured, 2026-10-07, over all 412

| Verdict | n | share |
|---|---|---|
| `ROOT-ONLY` — the root file is the only licence text in the tree | **323** | 78.4% |
| `BUNDLED-ONLY-EXTRA` — the extra texts are all vendored dependencies' | **54** | 13.1% |
| `TREE-AGREES` — other own texts exist, all the root's family | **26** | 6.3% |
| 🔴 `TREE-ADDS` — an own text names a family the root does not | **9** | 2.2% |

🟢 **The prediction's number holds: 9 against "more than five".**

🔴 **The prediction's interesting class is empty. 0 of 412 are permissive-root with a
copyleft text deeper in.** The escalation runs the **other way**: 2 are
**copyleft root with a permissive text deeper in**, and the remaining 7 stay inside one
class.

🔵 **This is the second consecutive pre-registration where the count was right and the
named interesting class was empty** — pass 26's action A predicted a
registry-only grant and found none of those either. **A pre-registration that gets the
magnitude right can still be wrong about the mechanism, and the mechanism is the part
that would have gone into a proposal.**

### The 9 `TREE-ADDS` rows

| Slug | root | adds | where | shelf knew? |
|---|---|---|---|---|
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | `CC-BY` | **MIT** | `LICENSE-CODE` | 🟢 **yes** |
| [`yongsoojoo/esd2026-agent-workflow`](https://github.com/yongsoojoo/esd2026-agent-workflow) | `MIT` | **CC-BY** | `LICENSE-docs` | 🔴 no |
| [`ankitects/anki`](https://github.com/ankitects/anki) | `AGPL-3.0` | **CC-BY** | `docs-site/LICENSE` | 🔴 no |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | `AGPL-3.0` | **MIT** | `docs/LICENSE` | 🔴 no |
| [`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication) | `CC-BY` ⚠️ | **MIT** | `ggml/LICENSE` | 🔴 no |
| [`SapuSeven/BetterUntis`](https://github.com/SapuSeven/BetterUntis) | `GPL` | **Apache-2.0** | `material-color-utils/LICENSE` | 🔴 no |
| [`mlcommons/croissant`](https://github.com/mlcommons/croissant) | `Apache-2.0` | **MIT** | `croissant-rdf/LICENSE` | 🔴 no |
| [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | `EUPL` | **Unlicense** | `json-schema-viewer/LICENSE` | 🔴 no |
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | `UNKNOWN` | **MIT** | `LICENSE.md` | 🔴 no |

🔵 **The dominant shape is not a hidden obligation — it is a DOCUMENTATION grant.** Five
of the nine are a code licence beside a content licence: `LICENSE-CODE`,
`LICENSE-docs`, `docs/LICENSE`, `docs-site/LICENSE`. That is **correct licensing
hygiene**, not a risk, and a root probe reports only one half of it.

🔴 **Which half it reports is the finding.** [`microsoft/autogen`](https://github.com/microsoft/autogen)
— on this KB's core shelf — has a root `LICENSE` that is **CC-BY-4.0** (`Attribution
4.0 International`) and its **code** grant in `LICENSE-CODE` (**MIT**, Microsoft
Corporation). ⚠️ **A rooted probe therefore returns a CONTENT licence as the licence of
a software project.** CC-BY is not a software grant; it imposes attribution on
redistribution and says nothing about patents or warranty. `agents/top.md` already
records this (*"`LICENSE` at HEAD is CC-BY-4.0 (dual with MIT)"*), so the shelf is
ahead again — **1 of 9 rows was already known, 8 are new.**

⚠️ `seamless_communication`'s root is `CC-BY` **as `family_of` reports it**; it is
actually **CC-BY-NC-4.0**, non-commercial. See `p445`.

## P444's own three defects

| | Defect | Effect |
|---|---|---|
| 1 | 🔴 **the root family was INHERITED from `p436`'s pass-25 TSV** | That TSV predates pass 26's family reordering, so a tree classified **today** was compared against a root classified **last pass**. **14 of 412 rows** reported version skew as a licence disagreement: **9 × `UNKNOWN`→`EUPL`** and **5 × `GPL`→`MPL-2.0`** |
| 2 | 🔴 **a root file NAMED for third-party licences read as an own grant** | `dequelabs/axe-core`'s `LICENSE-3RD-PARTY.txt` is at the **root**, so `is_own_path` accepted it, and its body is a real MIT text reading *"Applies to: colorjs.io; core-js-pure; css-selector-parser"*. **One such path in 412 — and it was in the escalation class, where a false positive costs most** |
| 3 | ⚠️ the root file counted among the "extras" it is compared against | every row would have been `TREE-AGREES` |

🟢 **Defect 1 is a bonus measurement.** Re-deriving the root family rather than
inheriting it quantifies exactly how much pass 26's reordering changed: **14 of 412
published root families were wrong**, and the two causes are precisely the two that
reordering targeted — the **missing EUPL vocabulary** (9) and **MPL §1.12 naming the
GNU licences** (5). The `p436_skew` column reports it per row.

⚠️ **Bare `CC-BY` is deliberately in neither the permissive nor the copyleft set.**
`p445` measured that `family_of` returns plain `CC-BY` for five CC-BY-**NC** payloads,
so a `CC-BY` from this classifier does not establish that commercial use is permitted.
Such rows escalate to `SAME-CLASS` and the commercial question is answered by `p445`.

## Limits

- **Depth 0 of the licence question, not the dependency closure.** These are the cited
  repositories' own files.
- **`family_of` only**, with the blindness `p445` measures: no NonCommercial axis, no
  Elastic/PolyForm, and GPLv2 read as LGPL in 4 rows.
- **40 candidate paths per repository**, inherited from `p441`.
- **`docs/LICENSE.rtf` is not read** — RTF, per `p441`'s own limit.
- 🔴 **"The root is complete" is a claim about licence FILES, not about obligations.** A
  repository with one root `LICENSE` can still vendor code under other terms; that is
  `dependency-licence-closure`'s question, and 54 rows here carry bundled grants.

## Run

```sh
python3 test_root_vs_tree.py                               # 24/24, offline
grep -P '\tLICENSED\t' ../p436-fork-hypothesis/payloads.2026-10-07.tsv \
  > payloads.licensed.2026-10-07.tsv
python3 -I root_vs_tree.py payloads.licensed.2026-10-07.tsv   # ~80 s for 412 trees
```

Exit 2 on an empty denominator: a path fault is not a clean tree (**P355**).
