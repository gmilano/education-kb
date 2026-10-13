# `p163-script-equity-gate` — is OpenOLAT's graded-path gate fair across writing systems?

**Pass 163, 2026-10-13.** Written and executed in-pass, discharging `ACTION IG`.

`test_script_equity.py` — **21 passed, 0 failed**, of which **15 are OpenOLAT's own JUnit
oracle cases** transcribed verbatim.
`run_equity.py` → `result.2026-10-13-p163.tsv`, 14 rows.
`probe_margins.py` → `probe.2026-10-13-p163.txt`, three follow-up probes.

Measured against `openolat/openolat` at HEAD `e4be14f0d1bb5840cba54136f753d97e4bfa5b60` —
**the same tree p161 and p162 read**, so this is a third reading of identical bytes.

## Why it exists

`ACTION IG` was pre-registered at the end of p162:

> assess `GibberishPreFilter` (`entropy ≥ 1.5`, `letter ratio ≥ 0.45`) and
> `AiGradingTier.classify()` for equity across non-Latin scripts.
> *Refuted if either threshold rejects or down-tiers a valid CJK, Arabic or Devanagari answer
> that a Latin-script equivalent would pass.*

These two classes stand between a learner's answer and the grader. A gate that refuses an
answer never reaches a human, so a script bias here is an **access** defect, not a quality one.

## Why a replication rather than the JVM

Running OpenOLAT's own tests needs a JVM, a Maven resolve and a database. The two gates are
pure static functions over a `String`, so they can be replicated exactly and measured for the
cost of a Python import — **provided the replication is proved faithful first**, which is what
`test_script_equity.py` is for. It fails loudly if upstream's own expectations are not met.

Three fidelity details are load-bearing, because the bias lives in exactly these places:

| detail | why it matters |
|---|---|
| `String.length()` and `substring()` count **UTF-16 code units** | an astral character is TWO units, so a code-point letter count over a code-unit total is a mixed ratio |
| `Character.isLetter(cp)` is true for `Lu Ll Lt Lm Lo` and **false for `Mn`/`Mc`** | the combining marks that carry Devanagari and Thai vowels, and Arabic harakat, are **not letters** |
| the trigram walk is over 3 **code units**, lower-cased | astral characters have their surrogate pairs split |

Declared approximation: Java's `toLowerCase(Locale.ROOT)` is modelled by `str.lower()`.
Lower-casing is the identity on Han, Kana, Hangul, Arabic, Devanagari and Thai, so the
approximation **cannot move any non-Latin verdict**.

## What it measures

| limb | file | question |
|---|---|---|
| A | `test_script_equity.py` | does the replication agree with OpenOLAT's own 15 oracle cases? |
| B | `corpus.py` + `run_equity.py` | one essay answer, same content, nine scripts: what does each gate decide? |
| C1 | `probe_margins.py` | how much letter-ratio **headroom** does each script have, and at what mark density does it reject? |
| C2 | `probe_margins.py` | the astral-Han margin, and how little punctuation closes it |
| C3 | `probe_margins.py` | which scripts fall off `countWords`' CJK branch, and what that does to the word count |

The corpus is a school-biology staple — *explain photosynthesis* — so **every row is a valid
answer a real learner could submit**. Content parity is the point: if a gate treats these rows
differently, it is treating the **script** differently, not the answer. Four rows are controls
and are labelled `CTRL-` in the data.

## Results — the falsifier is SILENT

**Nothing valid was rejected.** All ten valid answers passed both thresholds, and all ten
classified `SHORT`, the same tier as their Latin equivalents. Both negative controls rejected,
each for the expected reason. `ACTION IG` is **DISCHARGED with its falsifier silent.**

And one structural reason the down-tier limb could not have fired at this tree, stated so the
clean result is not read as more than it is: **all three tiers assert `maxTokens = 16_384`**
(upstream's own tests assert it three times) and `softTimeoutMs` is documented *"Not currently
read by any caller"*. So `SHORT` versus `MEDIUM` is **functionally inert** here; the only live
consequence of `classify()` is the `LONG` refusal.

### C1 — the verdicts are equal; the MARGINS are not

| row | letter ratio | margin above the `0.45` floor | relative to English |
|---|---|---|---|
| English | 0.976 | **0.526** | 1.0× |
| German | 0.977 | 0.527 | 1.0× |
| Arabic, unvocalised | 0.980 | 0.530 | 1.0× |
| Korean | 0.953 | 0.503 | 1.0× |
| Japanese | 0.941 | 0.491 | 0.9× |
| Chinese | 0.935 | 0.485 | 0.9× |
| Thai | 0.815 | 0.365 | 0.7× |
| **Hindi (Devanagari)** | **0.591** | **0.141** | **0.27×** |
| **Arabic, vocalised** | **0.552** | **0.102** | **0.19×** |

Whitespace is stripped before the ratio is taken, so `ratio = 1 − m` where `m` is the fraction
of code points that are combining marks. A rejection therefore needs **`m > 0.55`** — and the
empirical sweep finds the boundary exactly:

```
1 mark per letter, on up to 100% of letters -> ratio floor 0.495  passed
2 marks per letter, on 40% of letters       -> ratio       0.398  REJECTED (letter-ratio)
```

**One mark per letter never rejects. Two marks per letter always does.** Shadda-plus-vowel is
two marks on one letter and is ordinary Arabic orthography — it occurs in this corpus' own
vocalised row. So a fully-diacritised answer, the register of a primary reader or a
Quranic-studies class, is the case that crosses the floor.

### C2 — astral Han passes by `0.050`, and five full stops close it

18 CJK Extension B ideographs: 18 letters by code point, **36 units** by UTF-16, ratio exactly
**0.500**. The same 18 ideographs from the BMP would score **1.000**.

```
+0 punctuation -> ratio 0.500  passed
+4 punctuation -> ratio 0.450  passed
+5 punctuation -> ratio 0.439  REJECTED (letter-ratio)
```

**Five ideographic full stops reject an eighteen-ideograph answer.** Rare-character answers —
classical Chinese, Taiwanese and Hong Kong personal names, kanji variants — are exactly where
Extension B appears.

### C3 — three Han/Hangul families fall off the CJK branch, and Thai never had one

`isCJK` lists three ranges: `3040–30FF`, `4E00–9FFF`, `AC00–D7AF`.

| case | words | cjk ratio | branch taken |
|---|---|---|---|
| BMP Han ×40 | 13 | 1.000 | `cjk-charcount/3` |
| **Ext A Han ×40** (`U+3400+`) | **1** | 0.000 | `whitespace-split` |
| **Compatibility Han ×40** (`U+F900+`) | **1** | 0.000 | `whitespace-split` |
| **Hangul Jamo, NFD ×45** | **1** | 0.000 | `whitespace-split` |

And Thai, which has no inter-word spaces and no range in `isCJK`:

```
Thai x1    chars=   203  words=   4   tier=SHORT      (the English equivalent: 56 words)
Thai x20   chars=  4079  words=  80   tier=SHORT
Thai x100  chars= 20399  words= 400   tier=MEDIUM
Eng  x20   chars=  7039  words=1120   tier=LONG
```

**Thai is undercounted ~14×.** A Thai answer needs `20 399` characters to reach `MEDIUM` where
the English answer reaches `LONG` at `7 039`. The failure direction is **permissive**: these
answers are never refused, they are sent to the grader. That is a cost and output-truncation
exposure, not an equity rejection — and it is silent, which is the part worth fixing.

## The finding that makes the fix contributable

`GibberishPreFilterTest` has **six cases: English, German, keyboard mash, symbol spam, blank
and short.** Zero non-Latin. `AiGradingTierTest`'s only CJK cases are `"好".repeat(150)` and
`"字".repeat(300)` — a single repeated character, which is not language, and no Arabic,
Devanagari or Thai at all.

**No regression test guards any of the above.** `P163-A` is therefore a test contribution
before it is a code one, and `test_script_equity.py`'s corpus ports straight into
`src/test/java/.../essay/` as JUnit cases.

## How to re-run

```
python3 -I test_script_equity.py     # must stay 21/21 — the gate on everything else
python3 -I run_equity.py > result.$(date +%F)-pNNN.tsv
python3 -I probe_margins.py | tee probe.$(date +%F)-pNNN.txt
```

Re-clone the measured tree with p162's cheap census instrument — **`1.3 MB` of `.git` for
`25 823` paths**, then sparse-checkout only the AI subsystem for a `7.0 MB` working tree:

```
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/openolat/openolat DIR
git -C DIR sparse-checkout init --cone
git -C DIR sparse-checkout set src/main/java/org/olat/core/commons/services/ai \
                              src/test/java/org/olat/core/commons/services/ai
git -C DIR checkout HEAD
```
