# `p392-capability-absence` — the absence check keyed on CAPABILITY

**Registered by `p391` as the top-ranked instrument for the next pass, with its predicate
already corrected by `p391` itself.** Built here, **15 controls green**, and its first run on the
live shelves **refutes all three gaps `p391` opened eight hours earlier**.

## What it answers

> *An absence sentence is on a shelf. Does this base's own harvest log already carry an
> evidence-complete row for the **capability** that sentence says is missing — even though the
> two share no token?*

`gate-absence` (`p279`) answers the same question keyed on **string identity**, and is correct
and deliberately narrow. Every instance this base has actually published crossed a **vocabulary
boundary**, which identity cannot see:

| pass | absence published on a shelf | refutation, already in the harvest log | token in common |
|---|---|---|---|
| `Gap 386-C` | LATAM-native agent supply is structural | three granted LATAM agents | none |
| `p387` | a null leg reported as a null supply | two legs in pt/es | none |
| `p391` | *"LTI 1.3 — never a dependency to install"* | `packbackbooks/lti-1-3-php-library` | none |
| 🆕 `p392` | `Gap 391-A` — no maintained **Python** LTI 1.3 | `academic-innovation/django-lti` | none |
| 🆕 `p392` | `Gap 391-B` — no non-NA district-targeting data | `Mcp-Brasil/mcp-brasil` (INEP Censo Escolar) | none |
| 🆕 `p392` | `Gap 391-C` — no granted proctoring row | `mdestafadilah/proctoring.js` | none |

Six for six is why this is an instrument and not a reading habit.

## The predicate

    an ABSENCE SENTENCE on a shelf, scoped to the SEGMENT it sits in, whose CAPABILITY KEY is
    QUALIFIED, is REFUTED-CANDIDATE when a HARVEST row carries the whole key set AND is
    EVIDENCE-COMPLETE — slug + licence + (date or registry version).

Verdicts follow `gate-enumeration`'s polarity: `REFUTED-CANDIDATE` (fatal in the pass arm),
`UNREFUTED` (the honest, publishable absence), `NO-KEY` (the backlog — grow the lexicon, never
the matcher).

## Run it

```bash
python3 -I compose/code/p392-capability-absence/capability_absence.py --root . --census
python3 -I compose/code/p392-capability-absence/capability_absence.py --root . \
        --fatal verticals/solutions.md repos/foundations.md      # the files THIS pass writes
make gate-capability-absence
```

## What it measured at `p392`

| | |
|---|---|
| harvest index | **1,116** evidence-complete rows over **17** capabilities |
| absence sentences read | **356** |
| `REFUTED-CANDIDATE` | **46** — **36** in `intel/open-gaps.md`'s historical pass sections, **8** in `p392`'s own closure table (correct firings: those absences *are* refuted, which is what that table says), **2** on the live shelves |
| the 2 on the live shelves | 🔴 **both known-false, both registered as gaps** (`392-A`, `392-G`) and both written into [`adjudicated.2026-10-22-p392.tsv`](adjudicated.2026-10-22-p392.tsv) with a reason |
| the run that found the findings | the **first** run, before this instrument's own bugs were fixed: **8** live candidates, **7 true** on hand-adjudication → `Gap 391-A`, `391-B` and `391-C` closed |
| controls | **15**, green |

🟢 **Read the "2 on the live shelves" correctly.** The fatal arm is green on this pass's files not
because the instrument stopped finding things, but because **the absences it found were corrected**
across six places (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`,
`intel/market.md`, `intel/trends.md` `Trend 19`, and two patterns). That is the loop working.

🔴 **The two survivors are named rather than filtered:**

* **`Gap 392-A`** — `repos/foundations.md:123`, the `microsoft/pybryt` row, keys as `{python}` alone,
  so *"no PyPI release since 2022"* is adjudicated against every granted Python row. The lexicon
  cannot separate *"there is no maintained Python X"* from *"this Python thing is stale"*.
* **`Gap 392-G`** — `intel/market.md:1081`, a **region-partitioned** claim (*"closed for Brazil, open
  for Mexico, EMEA and APAC"*). `Mexico` is a surface form of `r:latam`, so the Brazilian row that
  closed half the gap refutes the half that stays open. Sub-region granularity.

## The ledger, and why a gate needs one

A gate that fails on candidates its own gap log has already adjudicated is switched off within a
pass; a gate that filters them silently hides the measurement. So a pass may subtract a candidate
**only by writing down the file, the line, the verdict and the reason**:

```
repos/foundations.md	123	FALSE-POSITIVE	Gap 392-A — keys as {python} alone …
```

`--ledger <tsv>` then reports each one as `ADJUDICATED-FALSE-POSITIVE` **with its reason printed**
and does not fail on it. Same discipline this base already uses for a declared nil.

## 🔴 Two of the five classes were found by this instrument failing on its own author

`p392` pointed the fatal arm at its **own draft** of the shelves and it failed on four candidates.
Two were real defects in this file:

* **Class 3b — a quote spanning a segment boundary stopped looking quoted.** The segmenter cuts on
  `:` and `. `, and quote detection was running *per segment*, so `p392`'s own **withdrawal** of
  `p391`'s claim — which quotes it across a colon — was reported as an unchecked absence. Quotes are
  a property of the **line**; the offset now travels with the segment.
* **Class 5 — a struck-through absence is a retraction, not a claim.** This base withdraws a sentence
  by striking it through and saying what replaced it. Reporting that as an unchecked absence
  **punishes the correction**, which is the one thing a gate must never do.

## The four false-positive classes, kept as controls

Each one was in the draft and is now a named control in `test_capability_absence.py`:

1. **A table row is not a sentence.** An absence phrase in cell 2 and a capability term in cell
   5 are not the same claim. Reading lines returned **75** candidates; reading segments, **44**.
2. **A region alone is not a capability.** *"Brazil has no AI statute"* keyed `{r:latam}` and was
   "refuted" by any granted Brazilian repository.
3. **A quoted absence is not a published absence.** `p391`'s own correction quotes the claim it
   refutes; the draft reported that sentence as unchecked. `p279` hit this too.
4. **A negated region scope must be refuted from another region.** *"North America only, and
   there is no analogue"* was "refuted" by the North American row it is about.
