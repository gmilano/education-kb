---
industry: education
region: Global
updated: 2026-10-19
---

# `p310-family-coverage` — `ACTION p309-R` items 1, 2 and 4

**Pass 310 — 2026-10-19.** `python3 test_family_coverage.py` — **58 passed / 0 failed**,
fully offline, no network and no clock. Wired standing as `gate-family-coverage`;
**19/19 gates green** at publication.

## The one-line version

🔴 **`p309` repaired the GNU rungs of `p306-licence-probe` and did not read the next five
lines.** The CC rungs below them carried the identical defect — a substring test standing in
for an identity test, ordered so the specific case is unreachable — and at `p310` they graded a
real **`CC-BY-NC-4.0`** payload as **`CC0-1.0`**. 🔵 **`p309`'s error excluded usable supply.
This one admits unusable supply into a client deliverable, which is the direction that costs.**

## What was measured

| | |
|---|---|
| 🔴 **the live defect** | [`aclascollege/aegis-graph`](https://github.com/aclascollege/aegis-graph), `LICENSE` **19 347 B** `41003d4a7474`, title line *"Attribution-NonCommercial 4.0 International"* → `p306` said **`CC0-1.0`**. [`Amey-Thakur/WRITING-SUPPORT`](https://github.com/Amey-Thakur/WRITING-SUPPORT), **18 873 B** `aa0d3c9d6a28`, *"Attribution 4.0 International"* → also **`CC0-1.0`** |
| 🔴 **the mechanism, exactly** | the rung was `elif "cc0" in low or "public domain dedication" in low:` over the whole body, ordered **before** the CC-BY and CC-BY-SA rungs. Every CC 4.0 legalcode names `CC0` **once**, in its *Considerations for licensors* boilerplate — **measured: exactly 1 occurrence in each payload** — so **no CC 4.0 file could ever reach its own rung** |
| 🔴 **and the remedy was 186 passes old** | [`p124-correction-form-marker/cc_version.py`](../p124-correction-form-marker/cc_version.py) was **built on this defect** (its first cut returned CC0 for 9 of 13 rows, including `openstax/osbooks-college-physics-bundle`, which is CC-BY-NC-SA-4.0) and carries the warning at the rung: *"ZERO is NOT consulted here … CC0 is reachable by channel 1 and 2 only, on purpose."* `p124` also registered it as **instance 3 of `ACTION AG`**, labelled `DOCUMENT-TEXT` |
| 🟢 **realised loss, RE-MEASURED rather than argued** | **zero published rows — and this was checked, not reasoned.** All **seven** CC0 rows this base publishes were re-probed first-hand at `p310` ([ledger](../../../evidence/p310-cc0-reaudit.2026-10-19-p310.tsv)): `gen-mentor`, `crpf-mitadt/Indian-AI-for-Education`, `O0000-code/awesome-academic-skills`, `chrisliu298/awesome-rubric-rewards`, `Lendarixon/awesome-ai-detection`, `open-spaced-repetition/awesome-fsrs` and `caramaschiHG/awesome-ai-agents-2026`. **All seven are genuinely `CC0-1.0`**, six at **7 048 B** (the legalcode's exact length) and one at 2 207 B. 🔵 **The defect was caught on its first two real CC 4.0 payloads.** 🔴 Four of the seven had **no byte length anywhere in the evidence store** before this audit, so the claim could not have been made without running it |
| 🔴 **the coverage denominator — the pass's durable finding** | `p309` reported `declared=11 CORRECT=11 DEFECT=0` on a corpus of **3 families**. This base publishes **22**. 🔴 **`p309` was green at 3/22 = 14 % coverage.** `p310` takes it to **8/22 = 36 %** — and **MIT (5 501 cells) and Apache-2.0 (2 313), the two most-published families on this base, have still never been run through any dynamic arm** |

## 🟢 The rule this pass adds

> **P310.** A dynamic gate is a statement about the **families in its corpus**, never about the
> classifier. `DEFECT=0` without a coverage ratio is an unbounded claim. The families a gate
> owes a payload to are not a matter of taste — they are **the ones the shelves publish**, and
> `family_coverage.py` derives that set rather than listing it.

🔵 This is why `p309` could be simultaneously right about its method and blind to the rung
below the one it fixed. The method was sound; the corpus was three families wide.

## What is in here

| file | what it does |
|---|---|
| `fixtures.py` | the five payloads pinned at `p310`, each with its **canonical family** read off its own title line and its **commercial-use** verdict. Handles are **prefixes**, resolved by listing the directory — `p309`'s convention, adopted rather than reinvented |
| `family_coverage.py` | the census: published families (from the shelves, via `carried_index.SHELVES`) × families with a pinned payload → **uncovered remainder with a denominator** |
| `run_families.py` | the dynamic arm, run on the five families `p309`'s corpus did not contain. **`ENTRY_POINTS` is imported from `p309`**, not restated |
| `test_family_coverage.py` | 58 offline controls, including the refuted rung itself as a **live negative control** |

## 🔴 The three false positives this instrument produced on itself

Kept as controls, not as anecdotes — and all three are `p309`'s own recorded error
(*"grading them with a payload fixture condemned two correct instruments"*) recurring in the
file written to generalise it:

| build | what it condemned | why it was wrong |
|---|---|---|
| 1 | **six instruments, 16 defect rows** | every house spelling of *"I decline"* read as a wrong answer: `p419`'s `unclassified`, `p211`'s `unrecognised`, `p228`'s `no recognised licence title`, `p198`'s `no-family` |
| 2 | **`p419`, four times** | a longer `ABSTENTIONS` list did not help, because `p419` returns a **Spanish sentence** — *«el encabezado no nombra una familia — tratar como no-osi (`p412`)»* — which is an abstention **with the safe advice attached**, and on these payloads the soundest answer any of the nine gives. 🔴 I had already guessed `sin-familia` and guessed wrong: **a vocabulary asserted instead of read is the same defect as the rung under audit** |
| 3 | **`p306` after its own repair** | the flattener took the first non-empty element of `(verdict, family)` and read the new `GRANT-NONCOMMERCIAL` **verdict** as that row's **family**. 🔵 `P250`'s two columns have to be known to the grader too |

🟢 **The durable fix was to invert the default:** an answer counts as a family **claim** only if
it matches the licence-token grammar, **imported** from `family_coverage.TOKENS`. Anything else
— a sentence, a sentinel in any language, an empty string — is an abstention. An instrument can
then only be condemned for **naming a family**, which is the only thing a classifier can be
wrong about.

## Result after the repair

```
# declared=9  ABSTAIN=8  OUT-OF-DOMAIN=1
🟢 PASS — no classifier crosses a commercial-use boundary on these five families.
```

🔵 Read `ABSTAIN=8` correctly: on these five families **eight of nine instruments decline**, and
declining is the right answer for most of them — `p150` discriminates GNU titles, `p129` reads
holders. The one instrument whose job this is, `p306`, is now **`CORRECT=3 ABSTAIN=1`**:
**`CORRECT=4 ABSTAIN=1`** — `CC-BY-NC-4.0`, `CC-BY-4.0`, `PolyForm-Noncommercial-1.0.0` and
`CC0-1.0` exactly, and an honest decline on the proprietary notice.

## 🟢 What was repaired in `p306-licence-probe`

1. **The CC family is delegated** to `p124`'s `cc_version.resolve()`. The three body rungs are
   deleted, not replaced: *a rung that cannot be reached correctly should not exist.*
2. **`P250`'s second column**, settled 60 passes ago and never wired in — *«familia de licencia
   y uso comercial son dos preguntas»*. Implemented **including its safe half** (*«el detector
   de restricciones corre SÓLO cuando no hay familia que lo proteja»*), which is what keeps
   AGPL-3.0 §6's *"noncommercially"* and the Unlicense's *"commercial or non-commercial"* out of
   the prohibited bucket — `p250`'s own versioned negative control.
3. **The POINTER class, three-valued** — `ACTION p306-R` item 2 / `ACTION p309-R` item 2,
   **open four passes. DISCHARGED.** `GarethManning/education-agent-skills` (1 230 B
   `f952182df4eb`, 877★) now reads `POINTER` / `CC-BY-SA-4.0` instead of `NO-GRANT-CLAUSE`.
4. 🔴 **The CC0 grant clause, which could never fire — and `P310`'s rule proving itself
   inside one pass.** The coverage census listed `CC0-1.0` among the 15 unexercised families;
   running the repaired prober over all seven published CC0 rows (for the loss measurement
   above) returned **`POINTER` on all seven**. Cause: `GRANT_CLAUSES` carried
   `"has waived all copyright"`, which is the **CC0 DEED SUMMARY's** wording. The **legalcode**
   — the 7 048 B file every one of those rows actually serves — reads *"hereby overtly, fully,
   permanently, irrevocably and unconditionally **waives, abandons, and surrenders** all of
   Affirmer's Copyright and Related Rights"*, and contains the deed's phrase **zero times**.
   🔵 **A clause list written against a document the prober never fetches is the same error as
   a rung asserted and never run** — and it is the third instance in this one file. The
   legalcode is now pinned as the fifth fixture, which is what moved coverage to 36 %.
5. **`EMPTY-GRANT-FILE`**, a class this base had not recorded (below).
6. **The holder channel** — `ACTION p309-R` item 4 (below).

### 🔴 The control that was holding its own action item shut

Discharging item 2 required turning a **green gate red first**.
`p309-affero-rung-census/test_rung_census.py` carried
`test_the_cc_content_payload_is_still_unresolved_and_says_so`, asserting
`verdict == "NO-GRANT-CLAUSE"` with a comment stating that `ACTION p306-R` item 2 was *still
open*. 🔵 **A standing gate held its own instrument's known wrong answer as the expected one.**
The control existed so the gap *could not be mistaken for* a reserved grant — and
`NO-GRANT-CLAUSE` vs `RESERVED-NO-GRANT` is exactly the distinction a consumer cannot make,
which is why the POINTER class was registered. **A pin on a value a standing ACTION exists to
change must name that action, or the gate becomes the reason the action stays open.**

### 🔴 `EMPTY-GRANT-FILE` — found by the clone channel, not by the prober

[`danialtranz/sentinel-agent-proctoring`](https://github.com/danialtranz/sentinel-agent-proctoring)
serves `LICENSE` at `main` with **HTTP 200 and ZERO BYTES** (`e3b0c44298fc`, the empty-string
digest). The guard read `if code == "200" and body:`; an empty body is falsy, so the row fell
through every remaining candidate and was written to the evidence store as **`404` /
`NO_PAYLOAD`** — **a false cell: the resource exists and returns 200.** 🔵 A zero-byte `LICENSE`
reads as *licensed* to GitHub's UI and to any file-presence check while granting nothing — the
`p304` class (*"a file named LICENSE that withholds every right"*) in its degenerate form.

### 🟢 `ACTION p309-R` item 4 — the holder channel, with its blindness declared per row

`p309` added this by hand, measured **1 placement in 5**, and recorded the blindness as *"the
stock copyleft payloads carry the FSF's copyright."* 🟢 **Measured again over 18 payloads, the
boundary is wider than copyleft and it is a property of the licence FORM:**

| licence form | holder line | measured |
|---|---|---|
| MIT · BSD · ISC — a **fill-in slot** | present | **13 of 13** |
| Apache-2.0 — a **fixed document** | 🔴 the first "copyright" match is Apache's own *"'Licensor' shall mean the copyright owner…"* | 0 of 3 |
| CC 4.0 legalcode · PolyForm · GPL/AGPL stock | 🔴 boilerplate | 0 of 3 (+ `p309`'s four) |

🔴 **And the match rate is not the yield.** A personal name places nobody — `p309`'s own
standard. Of **12** holder lines, exactly **two are INSTITUTIONAL**: `The Regents of the
University of California` ([`BridgeSuite/GradeBridge-Student-Submission`](https://github.com/BridgeSuite/GradeBridge-Student-Submission)
→ **North America**) and `Sejong University`
([`MORSHEDMDMONOARUL/ExamShield`](https://github.com/MORSHEDMDMONOARUL/ExamShield) →
**APAC**). 🟢 **2 of 18 = 11 % first-hand institutional placement**, and the channel now emits
`INSTITUTION` / `PERSON` / `BLIND-FIXED-DOCUMENT` / `NO-LINE` so a boilerplate sentence can
never again be passed off as a holder.

## 🔴 What this instrument does NOT do

- **It does not grade the 14 uncovered families.** They are exposure, not findings: no arm has
  run a classifier against their legalcode, so nothing is claimed about them in either
  direction. **`MIT` and `Apache-2.0` are first in that queue by cell count.**
- **It takes no position on `p419`, `p211`, `p228`, `p198`, `p191`, `p153`, `p150`.** All
  abstain on these four families, and abstention is a reported risk, not a realised one.
- **There is still no importable commercial-use oracle on this base.** `P250`'s rule lives in a
  shell script (`p250-commercial-use-axis/sweep_commercial.sh`), which is **why `p306` could not
  import it and restated nothing instead** — it simply had no second column. The rule is now
  implemented in `licence_probe.commercial_use()`; promoting it to a module every classifier
  imports is registered for `p311`.
