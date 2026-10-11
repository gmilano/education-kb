---
industry: education
region: Global
updated: 2026-10-11
---

# `p136-licence-residue` — `ACTION BV` discharged, premise refuted, three cells resolved

**Pass 136, 2026-10-11.** `ACTION BV` asked whether the three payloads p135 left `UNMATCHED` at
`0.996`–`0.998` against a GNU text carry a **substantive added clause** (which would make each a
`MODIFIED_SUPERSET` and a licence risk) or **editorial drift** (a gap in the canonical table).
It predicted refutation *"if any of the three turns out to carry a substantive added clause."*

🟢 **Zero of three.** All three resolve, and the residue is four mechanical classes:

| repo | payload | ratio | opcodes | residue | resolved |
|---|---|---|---|---|---|
| [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) | 35 196 B | `0.998672` | 3 | sign ×1, appendix ×2 | 🟢 **GPL-3.0** |
| [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 35 129 B | `0.997431` | 11 | sign ×1, delimiter ×8, appendix ×2 | 🟢 **GPL-3.0** |
| [`CoopCodeCommun/pyopenbadges`](https://github.com/CoopCodeCommun/pyopenbadges) | 26 526 B | `0.998056` | 7 | delimiter ×6, **steward ×1** | 🟢 **LGPL-2.1** |

## The four residue classes, and why each is not a licence change

| class | what it is | example measured here |
|---|---|---|
| `SIGN_TRANSLITERATION` | the copyright **sign** written as ASCII | `©` → `(C)` |
| `PLACEHOLDER_DELIMITER` | the appendix's delimiters written another way | `<https://fsf.org/>` → `{https://fsf.org/}`; SPDX's LGPL-2.1 drops the brackets, `adapt_framework` uses braces |
| `APPENDIX_INSTANTIATION` | the "How to Apply" appendix **filled in** | `<program>` → `adapt_framework`; `<year> <name of author>` → `2024 Stichting Cito Instituut voor Toetsontwikkeling, Arnhem` |
| `STEWARD_DIVERGENCE` | a word **neither project chose** | `pyopenbadges` says *"a brief idea of what it does"*; SPDX's LGPL-2.1 text says *"an idea"* |

🔴 **`STEWARD_DIVERGENCE` is the one that matters beyond this table.** It is not a project edit and
not drift: the canonical text and the payload differ in a word the **licence steward** controls, so
the canonical table is the thing that is wrong. p135 found the FSF editing its own text twice (the
`http`→`https` move and `why-not-lgpl.html` moving from `/licenses/` to `/philosophy/`). This is a
third instance and the first on the **transcription** side rather than the publication side.

🔵 **`ADDED_CLAUSE` is kept as a distinct class with a control test**, because an instrument whose
job is to resolve near-misses will launder real licence risk if "near" is allowed to mean "same".
`test_a_real_added_clause_is_still_caught` adds a visible-attribution clause — the `P134-F` class —
to a resolving payload and requires the verdict to flip to `MODIFIED`.

## One correction found by building it

End-stripping brackets is not enough. SPDX's LGPL-2.1 appendix writes the signature line without
delimiters, so the payload's `Coon>,` must compare equal to the canonical `Coon,` — with the `>`
**inside** the token. The first run of this instrument reported that single opcode as an
`ADDED_CLAUSE`, which would have published `pyopenbadges` as a modified LGPL. 🔵 Recorded because it
is the instrument's own near-miss, caught by its own result file rather than after publication.

## Scope — stated, because it bounds every cell above

- 🔴 **`-only` vs `-or-later` is NOT decided here.** The GPL-3.0 text is identical either way; the
  election lives in the per-file headers, which this instrument does not read. The three cells above
  are the **text**, not the election.
- 🔴 The canonical bodies come from the **SPDX mirror on GitHub**, because `gnu.org` and
  `creativecommons.org` are both refused in this channel (403 CONNECT / DNS `ENOTFOUND`). Primary
  source, secondary transport — the same posture `ACTION BO` was discharged under.
- 🔵 `STEWARD_WORDINGS` currently holds **one** measured pair. It is a table of known divergences,
  not a general theory of transcription.

## Running it

```
python3 -I test_residue.py     # 7 tests
```

## Files

| file | what it holds |
|---|---|
| `residue.py` | normalisation, the five classes, `residue()`, `summarise()` |
| `test_residue.py` | 7 tests, including the added-clause control and the FSF-edit case |
| `result.2026-10-11-p136.tsv` | the three real runs **with every opcode verbatim**, so the verdict can be re-judged without re-running |
