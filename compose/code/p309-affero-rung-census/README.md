# `p309-affero-rung-census` — the gate that RUNS the classifiers instead of reading them

## Why it exists, and it is not a hypothesis

At `p309` the standing prober `p306-licence-probe` graded four payloads `AGPL-3.0`
— **every AGPL verdict in its life, all four in this one pass** — and **two of them
are GPL-3.0 by title:**

| slug | file | bytes | `sha256_12` | title line | prober said |
|---|---|---|---|---|---|
| [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | `LICENSE.md` | **35 191** | `57756125771d` | `GNU GENERAL PUBLIC LICENSE` | 🔴 `AGPL-3.0` |
| [`five-plus-one/AI-Marker-Suite`](https://github.com/five-plus-one/AI-Marker-Suite) | `LICENSE` | **35 154** | `1ab858f515df` | `GNU GENERAL PUBLIC LICENSE` | 🔴 `AGPL-3.0` |
| [`sourcegrade/jagr`](https://github.com/sourcegrade/jagr) | `LICENSE` | 34 523 | `0d96a4ff68ad` | `GNU AFFERO GENERAL PUBLIC LICENSE` | 🟢 `AGPL-3.0` |
| [`ai-lingnan/econai-agent-platform`](https://github.com/ai-lingnan/econai-agent-platform) | `LICENSE` | 34 523 | `0d96a4ff68ad` | `GNU AFFERO GENERAL PUBLIC LICENSE` | 🟢 `AGPL-3.0` |

The rung was `elif "affero" in low:`, ordered **before** the GPL rung, over the whole
lowercased payload. GPL-3.0 names the Affero licence three times — §13 is **titled**
*"Use with the GNU Affero General Public License"* — at lines **552 / 556 / 559** of
the 35 191 B payload. **No GPL-3.0 payload could ever reach the GPL rung.**

🔴 **And the fix was already in this base.** `p150-gpl-affero-discrimination`
(2026-10-12) refuted this exact test, named `p145` / `p147` / `p149` as its carriers,
shipped `title_licence()` plus a §13 cross-check, and **keeps the bad pattern as its
own negative control, `NAIVE_AGPL`**. `p306` was written *later* and restated the
refuted body test.

🔵 **The generalisation, and it is the pass's headline:** `p308` learned *"import the
canonical list, never restate it"* for **shelf data** and wrote it into
`p308-shelf-consistency`. **Nobody applied it to the CLASSIFIERS.** Two instruments
were carrying a pattern this base had already proved wrong.

## The two arms, and why the second one is the evidence

```
make gate-affero-rung        # 36 offline controls, the static screen, then the live run
make affero-rung-census      # the screen alone: a ranked backlog with a denominator
```

**`rung_census.py` — the static screen.** Parses every `.py` under `compose/code/`
with `ast`, takes each string literal naming the Affero licence, and runs it against
a **real GPL-3.0 payload and a real AGPL-3.0 payload** pinned in `fixtures/` by byte
length and digest. A rung's *shape* is an argument; whether it fires is a measurement.

**`run_classifiers.py` — the dynamic arm.** Imports each declared classifier and
**calls it** on those same payloads. A verdict about code that can be run is never a
reading.

🔴 **The screen was wrong 34 times out of 36.** That is the number that decides which
arm is the gate:

| run | flagged | what the next discrimination was |
|---|---|---|
| 1 | **36** | first draft — fires-on-GPL-3.0 and nothing else |
| 2 | 25 | the **label**: a rung that fires on GPL-3.0 and labels the hit `GPL-FAMILY`, `COPYLEFT` or `GRANT` is correct. `p228`'s §13 pattern **is the discriminator** |
| 3 | 16 | **ladder order** — and the first draft of the order check was handed only the *affero-bearing* literals, so a plain GPL rung could never be in it and **27 files read `LADDER-NO-GPL-RUNG`**. Right rule, wrong scope |
| 4 | 3 | the **title window**: a rung applied to the first five lines cannot see §13 at line 552 |
| 5 | **0** | the window markers were **English-only** and missed `p419`'s `_encabezado()`; and `p222` / `p221` take a **declared token**, never a payload |

🟢 **The dynamic arm, same pass: 11 declared classifiers, 11 correct, 0 unrunnable** —
after the two fixes. Before them: **2 defects**, both confirmed by execution, and one
of them had already shipped two wrong rows.

🔵 **What that asymmetry means, stated for the next pass:** a static screen over code
is a **candidate generator** with a precision of `2/36` here. Only running the code is
evidence. Where an instrument can be executed, executing it is not the expensive
option — it is the only one that settles anything.

## The false-positive classes, each now a control

| class | the file that taught it |
|---|---|
| **the discriminator itself** | `p228-shelf-gate` matches `13\.\s*Use\s+with\s+the\s+GNU\s+Affero` *in order to prove the payload is not AGPL*. Flagged in run 1 |
| **the family matcher** | `p152-vertical-election`, `p221` — `GNU (Affero\|Lesser\|)General Public` fires on GPL-3.0 **by design** |
| **the grant detector** | `p1052-stale-absence` asks *"is there any grant text here"*; GPL-3.0 is grant text |
| **the version-after-name rung** | `gnu affero…license[\s,]*version 3` is **SAFE**, because GPL-3.0 §13 writes *"version 3 of the GNU Affero General Public License"* — version **before** name. Four files carry it and a census by shape would have condemned all four |
| **ladder order** | an AGPL rung after the GPL rung never decides. `p150-grant-ladder-order` **owns** this question and the verdict defers to it by name |
| **the title window** | `p198-title-line-family` has the discipline without importing `p150` |
| **the Spanish window** | `p419-copyleft-identity` reads `_encabezado()`. 🔵 `p471-gap-gate-language` recorded this same failure for `p370-gap-gate`: **half this base's instruments are written in Spanish, and an English-only filter reads their discipline as its absence** |
| **the declared-token grammar** | `p222`, `p221` grade `AGPL-3.0` / `GPL-3.0-or-later` **tokens**. Same signature as a payload reader, opposite input. Graded on token fixtures instead |
| **`GPL-3.0` matches inside `AGPL-3.0`** | the family-label pattern graded every AGPL label as a GPL-family label. A lookbehind is the fix — 🔵 **a substring test standing in for an identity test, which is the same shape as the defect this whole instrument is about** |

## What it does NOT cover, so no later pass infers it

🔴 **Only the GPL/AGPL pair.** The LGPL, the BSD two-and-three-clause split and the
CC family are untouched by this instrument.
🔴 **`fixtures/ccbysa-4.0-education-agent-skills-1230.LICENSE`** — 877★
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills),
a **CC BY-SA 4.0 grant by reference** — still returns `NO-GRANT-CLAUSE`. That is
`ACTION p306-R` item 2's **POINTER class**, open since `p306`, and it is pinned as a
control so the gap cannot be mistaken for a reserved grant.
🟡 **`8` unwindowed AGPL-rung-first ladders remain** in the screen's backlog. They are
exposure with a denominator, not findings: none is a declared entry point, so none has
been run. Ranked for `p310`.
