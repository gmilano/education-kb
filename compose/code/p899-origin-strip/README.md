# `p899-origin-strip` — origin evidence over stripped README text

**Written against:** `intel/open-gaps.md` → `898-G1`.
**Status:** 36/36 controls PASS. `898-G1` discharged, with a finding against its own acceptance test.

## What it is

`origin_strip.py` yields **content evidence for origin** from a repository README. It is not an
origin oracle. Per `884-G5`, no reachable channel serves author location from this session —
`gh api users/{login}` returns `403` and `gh api search/users` returns 20 fields with no
`location`, `company` or `name` among them — so content evidence is the only instrument available,
and its verdicts are hints to corroborate, never placements on their own.

## Run it

```
python3 -I origin_strip.py path/to/README.md
python3 -I test_origin_strip.py          # 36 controls
```

## The three mechanisms, in order of how much work they do

1. **Exclusive markers.** Only tokens that are near-impossible in English prose
   (`ã õ ç ção você não` / `ñ ¿ ¡ ción qué más`, plus script ranges for CJK, Kana, Hangul,
   Devanagari, Arabic, Cyrillic, Thai). Shared Romance function words — `la de no con um os` —
   are **deliberately absent**; they are what produced p898's false positive.
2. **Stripping.** Fenced code, inline code, URLs, bare `*.com`-style hostnames, markdown links,
   images and HTML tags are removed before scoring.
3. **Dispersion (`MIN_SPREAD = 0.10`).** Hits must span at least 10% of the document. Prose in a
   language is dispersed; a language switcher or a supported-languages table is not.

## 🔴 The finding this instrument produced against `898-G1`

`898-G1` concluded that **stripping** was the fix. Decomposed on the `aula` fixture:

|  | PT | ES |
|---|---|---|
| p898-style non-exclusive markers / **raw** | 464 | 653 |
| p898-style non-exclusive markers / **stripped** | 287 | **362** |
| **exclusive** markers / raw | 0 | 2 |
| **exclusive** markers / stripped | 0 | **2** |

**Stripping alone removes 38% and still places `aula` as LATAM by ~70× the threshold.**
Exclusivity alone removes **99.7%**. The acceptance test named the weaker lever, and could have
been passed in full by an instrument that still published the false row. Pinned as the control
`aula-stripping-ALONE-insufficient`.

## 🔴 The second defect class: a language list is not an origin

Found by running the instrument on real candidates, not by reasoning about it:

| Repo | Signal | Spread | What it actually is |
|---|---|---|---|
| `virgiliojr94/book-to-skill` | CYRILLIC=7 | **0.001** | `English · Русский · 简体中文` — a switcher |
| `Orenda-Project/rumi-platform` | DEVANAGARI=11 | **0.001** | a supported-languages table |
| `Mcp-Brasil/mcp-brasil` | PT=228 | **0.977** | genuine Portuguese prose |

A language list is evidence of **translation** or of a **target market**. The separation measured
is 1,000×, so the dispersion test is not a close call.

## Fixtures

| File | Role |
|---|---|
| `fixtures/aula-README.NEGATIVE-FIXTURE.md` | The named known-good negative `898-G1` requires. English README, Spanish/Portuguese repo *name*. Must never place. |
| `fixtures/menthor-README.PT-POSITIVE-FIXTURE.md` | Real Portuguese prose. Must survive stripping and place PT. |
| `fixtures/studymate-README.CJK-POSITIVE-FIXTURE.md` | Real CJK prose. Must survive stripping and place CJK. |

## Reading a verdict

- `PT=228`, `CJK=1490` — dispersed exclusive markers. **Corroborate before publishing**
  (organisation name, subject matter, author emails).
- `LANGUAGE-LIST(...)` — markers found, concentrated in one span. **Not an origin.**
- `ENGLISH-OR-UNKNOWN` — **never** evidence of Anglophone origin. Most of the world publishes in
  English. Use institutional evidence instead: `Submitty` and `pyBKT` were placed North America
  from README institutional claims and author emails, not from language.

## Known limits

- A README written in English by a non-Anglophone author is invisible to this instrument. That is
  the **intended** failure direction: `898-G1` records that false positives land hardest in the
  regions where this KB has the least evidence and a reader has no counterexample.
- `MIN_SPREAD` is calibrated on a 1,000× separation, not tuned on a corpus. A short README with
  genuinely clustered prose could in principle be rejected; none was observed across 15 candidates.
