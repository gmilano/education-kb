---
industry: education
region: Global
updated: 2026-10-08
---

## 🟢 Pass 50, 2026-10-08 — one gap **refuted at its stated cause**, one **narrowed by a full gate run**, three declared

> 🔵 **This pass's opening hypothesis was that `Gap 254` needed its cheapest next probe run.
> 🟢 That hypothesis was CORRECT and the probe refuted the gap's own Route C.** The register
> pointed at the right work for the first time in three passes — 🟢 **which is what `P598`'s
> freshness gate was built to make possible**, and is recorded here as the gate earning its cost.

### 🟢 `Gap 254` (pass 49) — **REFRAMED and partially REFUTED.** The Spanish restriction is a version pin, not a structural fact

| Pass 49's claim | Verdict after `P609`–`P611` |
|---|---|
| *"`es_core_news_sm` declares GNU GPL 3.0"* | 🟢 **STANDS** — and extended to 3.5.0 / 3.6.0 (`P610`); 3.8.0 is the latest release |
| *"inherited from `UD_Spanish-AnCora`"* | 🟡 **TRUE OF `v2.8` ONLY** — the ref spaCy pins |
| *"the GNU licence is inherited from the original dataset"* (quoted as current) | 🔴 **VESTIGIAL PROSE.** The same README's changelog records `r2.9` (**2021-11-15**): *"The license changed to CC BY 4.0"* |
| *"the restriction is structural, a tier above `Gap 237`"* | 🔴 **REFRAMED** — it is a **five-year-old version pin** |
| Route **C**: *"retrain on a permissive Spanish corpus — none found by this KB"* | 🔴 **REFUTED** — `UD_Spanish-AnCora` `r2.9`+ is **CC BY 4.0** (`P611`), and it is the *same corpus* |

🟢 **What remains open, and it is narrower:** nothing in this KB has **built** the retrained pipeline.
🔵 **Cost: one training run on a CC BY 4.0 corpus with an MIT trainer** — recipe and wiring at `P620`,
`compose/patterns.md`. 🔴 **And `Gap 237` is untouched**: no national Spanish essay exam, so still no
public rubric and no graded Spanish essay corpus. 🟢 **Routes A and C differ in licence, not in
capability.**

### 🟡 `Gap 255` (pass 49) — **NARROWED, not closed.** The invocation list exists and was run; nothing yet obliges it

🟢 **Remedy part 1 LANDED (`P621`):** all **110** suites in `compose/code/` were run from their own
directories, exit codes recorded, and diffed against the same sweep on a **pristine clone of `HEAD`**.

| | Pristine `HEAD` | After this pass |
|---|---|---|
| suites passing | **107 / 110** | 🟢 **108 / 110** |
| diff | — | 🟢 **one line: `p550` red → green** |

🟢 **The run paid for itself immediately: it found `P614`** — `p550` red at `HEAD` and **accusing the
shared classifier of two defects it does not have**.

🔴 **Why it stays open.** Running the list once is not a control. 🔵 **`P237`: a convention a pass has
to remember is not a control.** 🟢 **What is now true and was not: the list is written down as a
runnable recipe (`P621`), with the two harness rules that invalidate it if broken** — run each suite
from its own directory, and **never** with `python3 -I` (isolated mode drops the script's directory
from `sys.path` and reported **28** suites as `ModuleNotFoundError` against their own modules — 🔴 **a
harness defect indistinguishable from 28 broken instruments**).

### 🟢 `Gap 253` (pass 49) — **no instruments fixed this pass.** Stated so no pass reads this one as progress

🔴 **This pass fixed none of the `P541` instruments `Gap 253` enumerates.** 🔵 **The count is pass
49's (21), carried forward rather than re-measured** — this pass did not re-run the `p542` acceptance
sweep to completion, and so does not assert a current number. 🟢 **That is the honest form: `P469` is
this KB's own record of what happens when a gap's status is asserted instead of measured.** 🔵 The enumeration stands at
`p542-empty-input-sweep/result.2026-10-07.tsv`, so there is still no search step. 🟢 **One adjacent
instance was fixed for a different reason:** `p550`'s suite now **refuses** when its shared dependency
fails to load (`P614`) — 🔵 **the same discipline as `Gap 243`/`Gap 245` applied to a failed `source`
rather than to empty `argv`**, which is a class those gaps did not cover.

### 🔴 `Gap 256` (new, pass 50) — the **LGPL** branch under-reads a version the payload names

**Statement.** *"`lib/license_family.sh` reads the LGPL version only from a full-text anchor, so an
LGPL title stub answers bare `LGPL` even when it names Version 3."*

🟢 **Measured** (`P613` side-channel), all in one run:

| Input | Answer |
|---|---|
| `GNU LESSER GENERAL PUBLIC LICENSE` + `Version 3, 29 June 2007` (stub) | 🔴 **`LGPL`** |
| `GNU LESSER GENERAL PUBLIC LICENSE 3.0` (numeric stub) | 🔴 **`LGPL`** |
| canonical SPDX `LGPL-3.0-only` (42 098 B) | 🟢 **`LGPL-3.0`** |

🔵 **Why this is NOT `P613`.** The GNU branch **stamped** a version the payload never names
(*invention*); the LGPL branch **discards** one the payload does name (*under-read*). 🟡 **A version
too few is honest and coarse; a wrong version makes a reader reason about another licence's
obligations.** 🟢 **That asymmetry is why `P613` was repaired and this is declared.**

**Why it matters here.** 🔴 **`openeducat/openeducat_erp` is the LGPL-3.0 platform on this KB's
verticals shelf**, and LGPL-3.0 vs LGPL-2.1 is exactly the distinction a linking question turns on.

**Why it is open rather than fixed.** 🔴 **The fix moves a second contract:** `LGPL-2.1` is **absent**
from `OSI_RECONOCIDAS` in `p411-cession-identity-gate`, so emitting it would have that gate reject a
string its own library produces. 🔵 **`P562` — the correction must travel to the consumer — and
`P562` also says you do not touch an instrument whose contract you have not read.** 🟢 **Bounded:
one branch, one allowlist entry, one suite re-run.** 🟢 **The suite ASSERTS the current behaviour**
(`Gap 256` ×2 in `lib/test_license_family.sh`) so it cannot drift silently.

### 🔴 `Gap 257` (new, pass 50) — `p351-star-digit-sweep` is red at `HEAD` on **hard-coded tree counts**

**Statement.** *"`p351` fails at `HEAD` on three assertions that encode absolute counts of a growing
tree, plus one real unattributed star occurrence."*

🟢 **Measured** (`P621`, and present on the pristine `HEAD` clone, so **not** caused by this pass):

| Assertion | Failure |
|---|---|
| prediction threshold | 🔴 `244 not greater than or equal to 254` |
| attribution sweep | 🔴 `74` occurrences with no pass attributed |
| class sweep | 🔴 `agents/trending.md:8231` — `6.400 ★ (K-3CIFRAS, ±50)` attributed to pass 124 but carrying **none** of the 4 required classes |

🔴 **Two different defects on one gate, and they need opposite treatments.** The **threshold**
assertions go red on **growth alone** — an append-only tree crossing a hardcoded number is not a
finding, it is a treadmill. 🟡 **The third is a real `P479` instance**, in a historical row of an
**append-only** file.

**Why it is open rather than fixed.** 🔴 **The remedy for the real instance would be rewriting history
in `agents/trending.md`, which this KB's own append-only rule forbids.** 🟢 **The honest remedy is
stated instead:** derive `p351`'s thresholds from the tree rather than from a literal, and treat
pre-`P479` rows as a **declared historical band** rather than as live violations. 🔵 **Cost: one
instrument change, no content rewrite.**

### 🟡 `Gap 258` (new, pass 50) — `p213-envelope-aad` cannot run in this environment

**Statement.** *"`p213-envelope-aad/test_envelope.py` fails at import with
`pyo3_runtime.PanicException` from the `cryptography` package."*

🟢 **Measured on the pristine `HEAD` clone as well**, so it is environmental and **not** a regression.
🔵 **Not a logic defect and not a licence defect** — a native-extension load failure in a third-party
dependency. 🟢 **Declared rather than left in the red column unexplained**, so a later pass does not
spend budget debugging this KB's code for it. 🔴 **It does mean `p213`'s property is unverified in this
environment**, and that is the part that is actually open.

## 🔴 Pass 48, 2026-10-08 — this register is **maintained**, and still misroutes a top-down reader: three verdicts on one row, oldest first

> 🔵 **This pass's opening hypothesis was that nobody had re-adjudicated `Gap 39`'s first half.
> 🔴 That hypothesis is REFUTED and is recorded as such.** Pass 42 re-adjudicated it (line 236), pass
> 42 declared the successor `Gap 238` (line 250), and pass 43 recorded `Gap 238`'s closure (line 265).
> 🟢 **Credit where it is due: this file did its job.** What `P582` finds is a **positional** defect,
> not a maintenance one.

### 🔴 `P582` — three live verdicts on one row, in chronological order, with the superseded one on top

| Line | Pass | Verdict on `Gap 39` first half |
|---|---|---|
| **191** | 40 | 🔴 *"STILL OPEN and still untested… **the cheapest remaining win on this KB after `P480`**"* |
| **236** | 42 | 🟢 *"TESTED, and it splits."* Refuted for the writer, confirmed for the runtime |
| **265** | 43 | 🟢 `Gap 238` **closed**, with its two stated limits |

🔴 **Because this file appends, the oldest verdict is encountered first** — and line 191 sits inside
the block introduced as *"the rows a future pass should read first"*. 🟢 **A pass reading top-down
finds a target labelled "cheapest remaining win", and it is settled work.** 🔴 **Nothing on line 191
says it has been superseded**, and nothing obliges a reader to scroll 45 lines on.

🔵 **This is a supersession defect, not a status error.** The status is recorded correctly three
times. 🟢 **Remedy landed in place this pass:** line 191's row now carries a forward pointer to lines
236 and 265, so the superseded verdict cannot be read as current.

### 🟢 `Gap 39` (first half) — the citation form, fixed so no pass quotes it bare

🔵 **Pass 42's split verdict stands and was re-confirmed this pass from a fresh clone** (`P584`:
upstream `main` = `0ca7d6fc`, unmoved since pass 43; writer **33 exports / 0** template references).
🔴 **What was missing was the one-line form**, and the bare form misleads:

- 🔴 **Never:** *"`Gap 39` closed"* / *"the QTI 3 authoring tool emits parametric variant families."*
- 🟢 **Always:** *"first half — **refuted** for upstream's writer (pass 42), **remedied** by this KB's
  own emitter `P533` (pass 43); second half closed for **IRT linking** only."*

🟢 **Second half unchanged:** closed for IRT linking (`EqUMP` 0.3.6, MIT — Mean-Mean, Mean-Sigma,
Haebara, Stocking-Lord, true-score), 🔴 **not** for observed-score or kernel equating (`P500`:
0-byte stubs; only GPL implementations). 🟢 **Both halves now sit in one worked recipe** — `P594`,
`compose/patterns.md`.

### 🔴 `Gap 251` (new, pass 48) — the Alabama instrument cannot be identified from this environment

**Statement.** A US state-policy tracker reports *"Alabama's `HB 329` requires an approved CS course
that includes AI instruction to graduate."* 🔴 **Three defects** (`P586`): it is a **bill**, not a
law, with passage unconfirmed; the identifier is **contested** (`HB 332` in one committee summary of
the same proposal); and the graduation requirement it is credited with **predates it** — 2024
Alabama Administrative Code, effective **class of 2032**, with required implementation **2027–28**.

**Why it matters.** 🔴 An engagement planning to "an Alabama 2026 AI curriculum mandate" would be
planning to the wrong instrument **and six years early**.

**Why it is open rather than closed.** 🔴 **Three primaries all refused by the egress proxy**
(`P587`): `alison.legislature.state.al.us` (the bill text), `billtrack50.com` (status/last action),
`cs4alabama.org` (the administrative-code instrument). 🔵 **Same class as `Gap 56`** (eur-lex),
**`Gap 92`** (docs.moodle.org) and **`P533`** (purl.imsglobal.org).

**What would close it.** One read of the enrolled bill text or the Alabama Administrative Code
section, from an environment whose proxy permits `.gov`/`.state.al.us`. 🟢 **Bounded and cheap — for
a pass that can reach the primary.** 🔴 **Until then the claim stays out of every table in this KB.**

### 🔴 `Gap 252` (new, pass 48) — this register has no **supersession marker**, and its priority column has no freshness guarantee

**Statement.** When a later pass revises a row, the earlier row is **left exactly as written**
(`P582`). Correct as a log, misleading as an index: a top-down reader meets the oldest verdict first.
🔴 **And the column that misleads hardest is not status but *priority*** — line 191's *"cheapest
remaining win on this KB"* is a recommendation, and recommendations are acted on without being
re-derived.

**Why this file's existing hedge does not cover it.** 🔵 The preamble warns *"Treat every row as a
pointer to read, not a verdict to quote"* — a warning about **status**. 🔴 **No warning covers a stale
ranking**, and the ranking is what recruits a pass's budget.

**The three remedies, and which one landed.**

| Remedy | Cost | Status |
|---|---|---|
| **Forward pointer** on a superseded row | 🟢 one line | 🟢 **LANDED this pass** for `Gap 39` first half (line 191 → 236, 265) |
| **Freshness rule for the priority column**: no row may carry "cheapest/next win" unless re-asserted by the latest pass that touched it | 🟡 a convention plus a check | 🔴 **OPEN** — the honest next instrument |
| Re-adjudicate the remaining **11 open** + **5 undeterminable** rows and forward-point each | 🔴 more than one pass can do honestly, as this file already says | 🔴 **OPEN**, and `P582` is the evidence it is not optional |

🔵 **Scope stated honestly:** this pass forward-pointed **one** row — the one it could prove was
superseded by reading both corrections in full. 🔴 **It did not audit the other 16**, and does not
claim the defect is confined to `Gap 39`.

### 🟢 `Gap 252` (pass 48) — remedy 2 **LANDED at pass 49**

| Remedy | Status |
|---|---|
| **Forward pointer** on a superseded row | 🟢 **LANDED** — pass 48 (`Gap 39`), pass 49 (`Gap 246`, `Gap 238`, `Gap 245`) |
| **Freshness rule for the priority column** + a check | 🟢 **LANDED pass 49** — `compose/code/p598-register-freshness-gate/` (`P598`): **58 assertions, 7/7 mutants killed, refuses its own empty input.** Sweep after this pass's forward pointers: **12** rows carry a freshness claim → 🟢 **0 RANCIA**, **7 CITA**, **5 SOSTENIDA**, exit **0** |
| Re-adjudicate the remaining open + undeterminable rows | 🔴 **OPEN** — but 🟢 **now mechanical**: `p598 --sweep` names the stale rows instead of a pass reading 40 by hand |

🟢 **The rule, stated so it can be cited.** *No row may carry a priority superlative ("cheapest
win", "smallest gap") if a later row closes that gap; and no row may assert a measurement claim
("unmeasured", "untested", "unjudged") whose subject is measured elsewhere in the live tree.*
🔵 **Enforced by `python3 freshness_gate.py --sweep RAIZ`, exit 1 on any `P598-RANCIA`.**

🔴 **Honest limit, from the instrument's own first run.** v1 produced **4 false positives of 6**. The
three defects and their fixes are at `P598` (`intel/trends.md`, Trend D); the one that matters most
is that v1 flagged the *"rows pass N changed"* correction tables — 🔴 **a staleness detector whose
naive form punishes the act of correcting will be switched off in a week.**

### 🔴 `Gap 253` (new, pass 49) — the **21** remaining `P541` instruments

**Statement.** *"Twenty-one instruments in `compose/code/` still exit `0` having judged nothing."*

🟢 **`Gap 245` enumerated 23; pass 49 fixed the two it named as priority** — `p370-gap-gate` and
`p471-gap-gate-language`, the gates that exist to catch undeclared gaps — each with an `if not
argv:` refusal **and** a regression assertion, suites **27/27** and **25/25**. 🟢 **Acceptance test
re-run rather than asserted:** `p542` sweep `P541-FALSE-PASS` **16 → 14**, `P541-SILENT-SUCCESS`
**7 → 7**, 🟢 **total 23 → 21**.

🔴 **The other 21 are untouched**, enumerated by path and class in
`p542-empty-input-sweep/result.2026-10-07.tsv`, so there is no search step. 🔵 **Cost: mechanical,
~21 guards and 21 assertions, each needing its own suite re-run.** 🟢 **The sweep is the acceptance
test — it must reach 0.** 🔵 **Renumbered rather than left inside `Gap 245` so that no pass can read
`Gap 245` as closed.**

### 🔴 `Gap 254` (new, pass 49) — the **Spanish** pipeline artefact is GPL-3.0, one tier above `Gap 237`

**Statement.** *"There is no permissively-licensed Spanish NLP pipeline artefact for an assessment
feature layer."*

🟢 **Measured, not inferred** (`P595`): `es_core_news_sm` declares **GNU GPL 3.0** at **3.8.0 and
3.7.0**, inherited from `UD_Spanish-AnCora`, whose own README — read from payload — says *"The GNU
license is inherited from the original dataset, downloaded from the AnCora website."*

🔴 **Why this is a new gap and not part of `Gap 237`.** `Gap 237` is a **data** gap: no national
essay exam, so no rubric and no graded corpus. 🔴 **This one bites a tier higher** — even with a
rubric and a corpus in hand, the default pipeline cannot ship permissively. 🔵 **The string
`es_core_news` appeared in ZERO files of this KB before pass 49**: the Portuguese chain was measured
to four tiers and Spanish was never examined below the corpus.

**Routes, priced at `P605`** (`compose/patterns.md`): **A** ship GPL-3.0 — zero engineering, and
usually the right answer for public-sector work; **B** `xx_ent_wiki_sm` (**MIT**) plus reimplemented
indices — 🔴 **the cost is an agreement study, not an extractor**; **C** retrain on a permissive
Spanish corpus — 🔴 **none found by this KB**.

🔵 **Cheapest next probe:** enumerate the other UD Spanish treebanks (`UD_Spanish-GSD`,
`UD_Spanish-PUD`) for a non-GPL grant, exactly as pass 47 did for Portuguese.

### 🔴 `Gap 255` (new, pass 49) — a correct gate that nobody invokes is worth nothing

**Statement.** *"Nothing in this KB's workflow invokes its own gates, and one of them was red at
`HEAD` for five passes."*

🟢 **Measured** (`P603`): `p383-region-heading-gate` run against `intel/market.md` at `HEAD`, before
pass 49 → **`P383-MULTIPLE-BLOCKS`, 2 canonical blocks, exit 1**. Pass 48 prepended a new
`## Opportunities by region` block, did not mark the previous one superseded — the convention six
older blocks in that same file already follow — and **did not re-run the gate it inherited**.

🟢 **Instance fixed this pass:** both older blocks marked superseded, 🟢 **`### Global` added** (it was
absent — `P383-MISSING-REGION`), 🟢 **`p383` re-run → exit 0**.

🔴 **Why it stays open after being fixed.** The *instance* is fixed; the *class* is not. `Gap 243`
and `Gap 245` made the instruments honest about empty input; 🔴 **neither makes anyone invoke them.**
🔵 **Remedy and cost:** one invocation list — the gates every pass runs before committing, with
expected exit codes — and ideally a single entry point that runs all of them. 🔴 **A convention a
pass has to remember is not a control (`P237`)**, which is exactly why this is declared rather than
called done.

# 🔴 Open-gap register — restored to the live tree

> **This file exists because `P483` prescribed it at pass 38 and pass 38 did not create it.**
> See `P495` in `intel/trends.md`.
>
> 🔵 **What this file is.** A **reachability index** of every gap this KB declared for itself before the
> `2026-10-06` reset. The reset moved all eight working files to `archive/2026-10-06-pre-reset/` and the
> gap declarations went with them, so for twelve passes no pass could see a gap that a previous pass had
> already identified, priced and prescribed a remedy for. `Gap 39` is the documented casualty: declared at
> pass 25, recovered by accident at pass 38, and — as `P492` shows — **closed at half** even then.
>
> 🔴 **What this file is NOT.** It is **not** a re-adjudication. The status column below is assigned
> **mechanically, from the declaring line alone**, and several of these gaps were closed, reopened or
> split by later passes whose text is not on the declaring line. 🔵 **Treat every row as a pointer to
> read, not a verdict to quote.** Re-adjudicating 40 gaps is more work than one pass can do honestly, and
> `P469` is this KB's own record of what happens when a gap's status is asserted rather than measured.

## How this index was built

```
grep '**Gap N' over archive/2026-10-06-pre-reset/*.md   # bold-declared gaps only
```

**40 distinct bold-declared gap numbers** recovered across the eight archived files. Gap numbers that
appear only in prose references (`ver gap 54`, `el control del gap 71`) are **not** rows here — they are
citations, not declarations, and a declaration is what a later pass needs in order to act.

🔴 **Known incompleteness, stated rather than hidden.** Numbers missing from the sequence below
(`1`–`9`, `11`–`30`, `38`, `41`, `43`–`49`, `57`–`61`, `66`–`67`, `69`–`80`, `82`, `84`–`85`, `87`, `89`,
`98`, `103`–`232`) were either never bold-declared, declared in a pass whose file did not survive to the
archive, or renumbered. 🔵 **The register's job is to make what survives reachable; it cannot reconstruct
what the archive does not hold.**


## 🔴 Declared open on the declaring line — 12 rows

These are the rows a future pass should read first. 🔵 **`Gap 39` is the worked example of why**: its first half is still unmeasured — see `P492`.

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **10** | `repos-trending.md:8341` | Gap 10 abierto. |
| **31** | `repos-foundations.md:5989` | Gap 31 — SIGUE ABIERTO, y el pase 19 lo buscó con los términos que el pase 18 dejó escritos. Se buscó |
| **34** | `repos-foundations.md:6074` | Gap 34 (nuevo en el pase 19) — *unlearning* evaluado sobre modelos del alumno. Formulación precisa, que es |
| **35** | `repos-foundations.md:6245` | Gap 35 (nuevo en el pase 20) — ningún benchmark pedagógico está empaquetado como prueba de conformidad, y |
| **36** | `repos-foundations.md:6037` | Gap 36 (nuevo en el pase 21) — el borrado del LRS permisivo no deja evidencia. `lrsql` borra de forma |
| **37** | `repos-foundations.md:6059` | Gap 37 (nuevo en el pase 22) — el registro de eventos que el stack oficial de Open edX conserva tras una |
| **39** | `repos-foundations.md:6013` | Gap 39 (nuevo en el pase 25) — no hay banco de ítems que genere familias de variantes equivalentes, y es el |
| **40** | `repos-foundations.md:6025` | Gap 40 (nuevo en el pase 25) — el cartucho MCP de CaSS está declarado y no está medido, y de él depende la |
| **65** | `agents-top.md:1883` | Gap 65 (confirmado, del pase 34): |
| **81** | `intel-trends.md:76` | Gap 81 PARTIDO EN DOS clases con riesgo y acción distintos: `@timadey/proctor` declara MIT tres veces en el árbol y le falta el archivo; `sisu-mcp` tiene UNA declaración en todo el mundo (te |
| **88** | `repos-foundations.md:4190` | Gap 88: cerrado como medición, abierto como decisión de legales. |
| **100** | `agents-trending.md:7267` | Gap 100 CERRADO; gap 97 REABIERTO y matizado. |


## 🟡 Status not determinable from the declaring line — 5 rows

The declaring line carries no status word. 🔴 **Not "open" and not "closed" — unread.**

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **56** | `intel-market.md:1158` | Gap 56: `eur-lex.europa.eu` y `data.europa.eu` están BLOQUEADOS por el proxy — van siete fuentes secundarias y cero primarias, y la fecha no se cita como primaria. APAC: ~530 M de alumnos de |
| **62** | `agents-trending.md:9664` | Gap 62. |
| **68** | `agents-top.md:1882` | Gap 68 (nuevo): la puerta oficial de Open edX publicó 12 releases en dos días (2026-07-24/25) y |
| **92** | `agents-trending.md:6447` | Gap 92 suma dos canales, y los dos bloquearon una PRIMARIA: `docs.moodle.org` (sexto) y |
| **102** | `agents-trending.md:7290` | Gap 102 (nuevo). |


## 🟢 Declared closed on the declaring line — 23 rows

Kept for citation integrity: a later pass citing `gap N` must be able to resolve N. 🔵 **Closure is as recorded, not as re-verified.**

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **32** | `repos-foundations.md:6083` | Gap 32 — ✅ CERRADO EN EL PASE 19, REFUTANDO LA HIPÓTESIS. El gap decía que nada conecta el pedido de |
| **33** | `repos-foundations.md:6001` | Gap 33 (abierto en el pase 19) — 🔴 CERRADO POR REFUTACIÓN EN EL PASE 21. La formulación original era: |
| **42** | `intel-trends.md:84` | Gap 42 sigue cerrado pero ahora medido en los dos lenguajes: `ltijs` v7.0.6 (Apache-2.0, 2026-09-18) tiene 0 menciones de MCP, y `pylti1p3` lleva casi cuatro años sin release (tendencia 90). |
| **50** | `intel-trends.md:84` | Gap 50 CERRADO leyendo código, invirtiendo la consigna: el `v0` de *authoring* de Open edX está DEPRECADO en favor del `v1`, con directiva `.. deprecated::` y `DeprecationWarning` emitido en |
| **51** | `agents-top.md:1890` | Gap 51 CERRADO en negativo, medido en tres registros: `opencase` da 7 / 404 / 665 con cero del dominio (cajas de skins, `opencage`, `opencast`) y `cass` da 26.726 en Packagist; el instrument |
| **52** | `intel-trends.md:85` | Gap 52 CERRADO leyendo cinco archivos de OpenCASE: 72 rutas, la regla del prefijo, dos endpoints OpenAPI y una capa CGE de federación que nadie había visto. ✅ Gap 53 medido ejecutando el ser |
| **53** | `intel-trends.md:85` | Gap 53 medido ejecutando el servidor: 132 tools, y el «164» era *aliasing*, no supresión —el 100 % de las operaciones se sirve (tendencia 83)—, aunque 🔴 la antigüedad era peor de lo registra |
| **54** | `intel-trends.md:84` | Gap 54: la consigna del registro de paquetes rinde — aparece una SEGUNDA puerta MCP de OneRoster y es MIT (`@eduware/oneroster` v1.2.11, ejecutable `mcp` empaquetado; tendencia 89). 🟢 Entra  |
| **55** | `intel-trends.md:84` | Gap 55 MEDIDO sin Docker, bajando el wheel de PyPI: 35 rutas (28 LMS + 7 CMS), 19 escrituras en 6 scopes, AGPL-3.0 leída del `LICENSE` del artefacto, y 🔴 11 escrituras piden *confirm token*  |
| **63** | `agents-top.md:1889` | Gap 63, mitad arquitectura, CIERRA por evidencia de archivo: los tres `config/plugins/{lrsql,ralph,veracity}.yaml` dan 200 y `.env.example` declara `LRS_PLUGIN`; la mitad fecha se reclasific |
| **64** | `agents-top.md:1889` | Gap 64 CERRADO en negativo con tres instrumentos: ningún LRS publica puerta MCP propia — Docker Hub de `yetanalytics` (6 imágenes, ninguna MCP), `deps.edn`+README de `lrsql` (0 menciones), ` |
| **83** | `intel-trends.md:76` | Gap 83 CERRADO por la historia de dos archivos, y baja de bloqueante a anotación: las dos licencias en conflicto son permisivas OSI (tendencia 154). ⚠️ Gap 81 PARTIDO EN DOS clases con riesg |
| **86** | `agents-trending.md:7885` | Gap 86 CERRADO — `compose/code/sebserver-mcp-gate/`: 79 tools, 36 expuestas, 37 escrituras con |
| **90** | `agents-trending.md:7887` | Gap 90 CERRADO con código — `compose/code/seb-proctoring-validator/`: el validador de upstream acepta un |
| **91** | `agents-trending.md:7700` | Gap 91 CERRADO. Tendencias |
| **93** | `agents-trending.md:7668` | Gap 93 CERRADO. Tendencias 175–177. |
| **94** | `repos-trending.md:5303` | Gap 94 CERRADO. |
| **95** | `agents-trending.md:7520` | Gap 95 CERRADO. |
| **96** | `agents-trending.md:7490` | Gap 96 CERRADO. |
| **97** | `agents-top.md:8797` | Gap 97 decidido a favor: |
| **99** | `agents-trending.md:7369` | Gap 99 CERRADO con un NO. |
| **101** | `agents-trending.md:7328` | Gap 101 CERRADO, gap 103 (nuevo) abierto. |
| **233** | `intel-trends.md:62` | Gap 233 CERRADO —hay dos puertas MIT de Canvas con texto y la mayor cubre el núcleo, así que el gap 232 baja de bloqueante a opcional. 🔴 Y los hallazgos que corrigen a esta base: el defecto  |


## 🟢 The rows pass 40 changed, 2026-10-07

| Gap | Pass 39 said | 🟢 Pass 40 says |
|---|---|---|
| **39** (second half — *equivalence/comparability*) | 🔴 **Open.** *"la equivalencia psicométrica entre variantes no la cubre ninguna pieza open source de esta KB"*, with only one permissive implementation (Java, Apache-2.0) and one GPL R package found | 🟢 **CLOSED for *IRT linking*, and closed permissively in Python.** 🆕 **`EqUMP` 0.3.6 — MIT**, artefact-verified: Mean-Mean, Mean-Sigma, **Haebara** and **Stocking-Lord**, all four with test files, plus **true-score equating**. See `P499` (`repos/foundations.md`) and the chain at `P507` (`compose/patterns.md`). 🔴 **NOT closed for *observed-score* or *kernel* equating** — `EqUMP` declares those directories and they are **0-byte stubs** (`P500`), so for those two methods the gap stands and the only implementations remain **GPL** |
| **39** (first half — *parametric variant generation*) | *"inferido de la descripción de los paquetes, no probado"* | 🔴 **⛔ SUPERSEDED — DO NOT ACT ON THIS ROW.** Pass 40 wrote: *"STILL OPEN and still untested… the cheapest remaining win on this KB after `P480`"*. 🔴 **That verdict was overturned by pass 42 and the gap was remedied by pass 43** — see **"The rows pass 42 changed"** (🟢 *"TESTED, and it splits"*) and the **`Gap 238`** closure row below. 🟢 **Current verdict:** refuted for upstream's writer, remedied by this KB's own emitter (`P533`). 🔵 Forward pointer added by pass 48 (`P582`); the pass-40 text is kept verbatim above for citation integrity |

> 🔵 **Note on how this closure was reached, because `P492` exists to prevent the opposite.** The
> declaring line was read in full from `archive/2026-10-06-pre-reset/repos-foundations.md:6013` before
> anything was declared closed, and the closure is **split by method** rather than asserted for the whole
> gap. 🔴 **A later pass must not quote "Gap 39 closed" without the method qualifier.**

## 🟢 The one row pass 39 changed

| Gap | Pass 38 said | 🔴 Pass 39 says |
|---|---|---|
| **39** | 🟢 *"closes `Gap 39`"* — the item-calibration library was found (`py-irt`, `irtorch`, `catsim`) | 🔴 **Closed at half.** The gap has two halves and the archived text says so: *"la segunda mitad del gap es más grande que la primera"*. The calibration half is closed. 🔴 **The equivalence half is not** — see `P492` in `intel/trends.md` and `P496` in `compose/patterns.md` |

> 🔵 **Rule for every later pass, and it is the whole point of this file:** before declaring a gap closed,
> read the **declaring line in full** from the archive path in the table above. `P492` exists because
> pass 38 quoted the gap's last sentence and acted on it as though it were the gap.


---

## 🟢 Live gaps declared **after** the 2026-10-06 reset — a register that is a verdict, not a pointer

🔵 **Everything above is a *reachability index* of pre-reset declarations, and its status column is
explicitly not a verdict.** 🟢 **This section is different: these gaps were declared by a pass whose text
is still in the live tree, so a later pass can read the declaring line without going into `archive/`.**
🔵 **Keep it that way — append here when a pass declares a gap, and cite the file and finding.**

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| **233** | pre-reset ceiling | (highest gap number in the tree before pass 41) | — |
| 🆕 **234** | **2026-10-07**, pass 41 | `repos/foundations.md` · `P508` / `P509` | 🔴 **OPEN.** *"There is no permissive implementation of observed-score or kernel equating in any language whose runtime is permissive."* 🟢 **Narrowed, not closed**: `KernEqWPS` 1.0.7 is **MIT** and implements both, but `Imports: MASS` (**GPL-2 \| GPL-3**) and runs on the **GPL** R interpreter, so the closure is not permissive. 🔵 **Remedy named and scoped**: port `KernelEquateFromScoresEG` + `LevineObservedEquate` + `FindBestBandwidth` to Python with `KernEqWPS` as the test oracle (`P504` shape). 🟢 **Interim workaround already specified** — the R side-car in `compose/patterns.md` `P518` |
| 🆕 **235** | **2026-10-07**, pass 41 | `intel/trends.md` · `P516` / `P517` | 🔴 **OPEN.** **No confirmed open-source essay or short-answer scorer for Portuguese or Spanish.** The only LATAM-origin candidate, `AIRGOLAB-CEFET-RJ/textgrader` (CEFET-RJ), has an **unresolvable repo path** — `0` refs from `git ls-remote`, matching the negative control, no licence payload on `main`/`master`/`develop` — although a search result hyperlinks it as a repository. 🔴 **Every permissive asset in the essay-scoring tier scores English.** 🔵 **Next step named**: query the Portuguese-language corpus directly (`corretor automático de redação código aberto`) and check whether CEFET-RJ publishes under a renamed organisation |

🔴 **Both gaps are declared with the remedy *and* its cost, which is what `P469` and `P492` exist to
enforce.** 🟢 **Neither is a wish; each names the specific artefact a later pass would have to produce.**

---

## 🟢 The rows pass 42 changed, 2026-10-07

🔵 **Both changed rows were read **in full from their declaring line** before anything was declared
closed, as the rule above requires.**

| Gap | What it said | 🟢 Pass 42 says |
|---|---|---|
| **39** (first half — *parametric variant generation*) | 🔴 *"STILL OPEN and still untested… the chain's oldest untested assumption and the cheapest remaining win on this KB"* | 🟢 **TESTED, and it splits.** 🔴 **Refuted for the writer**: `LongsightGroup/qti3`'s `packages/writer` has **0 of 33 exports** and **0 files** referencing `qti-template-declaration` / `qti-template-processing`, so the step every recipe wrote as *"author N parametric variants with `qti3`"* is **false as written**. 🟢 **Confirmed for the runtime**: `packages/core` implements the whole mechanism — declaration parsing, a real `randomInteger` draw over `min`/`max`/`step`, answer keys derived from the draw, and a constraint-retry loop up to **100 restarts** — with a working parametric fixture. See `P527` (`repos/foundations.md`) and the corrected recipe in `compose/patterns.md`. 🔴 **Stated limit: read from the cloned tree; the suite was *not executed* (installing a third-party repo's dependencies is not permitted here)** |
| **235** | 🔴 *"No confirmed open-source essay or short-answer scorer for Portuguese or Spanish"*, with the next step named as the Portuguese-language query and the CEFET-RJ org check | 🟢 **CLOSED for Portuguese, as a *measured* result rather than a found component — and it closes in three parts.** 🟢 **(a)** The prescribed query worked first time: **six distinct trees** (seven slugs; two share head SHA `da2e8d3d`) — `P521`, `P522`. 🔴 **(b) Not one carries a licence grant** across 12 filenames × every served ref + manifests + README, so the tier is **ungranted, not absent**. 🟢 **(c) The tier's permissive asset is the *corpus*: `lplnufpi/essay-br`, MIT, human-graded on ENEM C1–C5, peer-reviewed** — `P524`. 🟢 **The org check also paid: `AILAB-CEFET-RJ`, not `AIRGOLAB` (`P523`).** 🔴 **Spanish does NOT close — see `Gap 237`** |

🔵 **Note for a later pass, because `P492` exists to prevent the opposite.** 🔴 **Do not quote "Gap 39
closed" or "Gap 235 closed" unqualified.** `Gap 39`'s first half is **answered and negative for
authoring**; `Gap 235` is **closed for Portuguese only**, and closed with the finding that the tier is
unusable rather than with a usable scorer.

## 🟢 Live gaps declared by pass 42 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **236** | **2026-10-07**, pass 42 | `agents/top.md` · `P522`; `repos/foundations.md` · `P524` | 🔴 **OPEN.** *"There is no permissively-licensed essay **scorer** for Portuguese — only a permissively-licensed graded **corpus**."* 🟢 **Narrowed hard, not closed**: every layer a scorer needs now exists permissively or ownably (corpus MIT via `P524`; open weights at the proprietary baseline via `P526`; calibration worth more than model size; LanguageTool as an LGPL-2.1 service via `P525`) — 🔴 **but nobody has published the assembled scorer under a permissive licence.** 🔵 **Remedy named and scoped**: fine-tune an open-weight model on `essay-br` with theme-separated folds, per-competency prompting, anchors and bias calibration, and publish it MIT — the chain is written step-by-step at `P532` (`compose/patterns.md`). 🔴 **Cost stated: GPU time for the fine-tune, which is the exact constraint that pushed `P526`'s source onto hosted APIs mid-run; and the realistic target is QWK ~0.63 (mid-band of the published 0.60–0.73), not state-of-the-art** |
| 🆕 **237** | **2026-10-07**, pass 42 | `intel/trends.md` · `P531` | 🔴 **OPEN, and structural rather than unmeasured.** **No open-source essay scorer for Spanish**, searched this pass in Spanish (`corrector automático ensayos español código abierto licencia MIT github`). The channel returns only the **orthography/grammar** tier — none of which grades against a rubric. 🔵 **Why it is structural, which changes the remedy**: Brazil has one national essay-graded exam with a published five-competency rubric (ENEM), which produced both `essay-br` and a community; **Spanish-speaking LATAM has no single equivalent instrument**, so there is no rubric to standardise on and no graded corpus to train against. 🔴 **Remedy and cost**: the first deliverable is **a rubric and a human-graded corpus**, per target country — an annotation programme, not an engineering sprint, and far more expensive than `Gap 236`. 🔵 **Cheaper next probe before committing: query per country (`prueba de egreso`, `PAES`, `examen de admisión`) rather than pan-Spanish, since `P521` is this KB's own evidence that the query's shape hides tiers** |
| 🆕 **238** | **2026-10-07**, pass 42 | `repos/foundations.md` · `P527`; `compose/patterns.md` | 🔴 **⛔ SUPERSEDED — DO NOT ACT ON THIS PRIORITY CLAIM.** 🟢 **`Gap 238` was CLOSED at pass 43** with a tested artefact (`P533`) — the closure row is 15 lines below. 🔵 Forward pointer added by pass 49, **flagged mechanically by `P598`** rather than by inspection. Pass-42 text kept verbatim: OPEN, and it is the cheapest gap on this KB. *"`LongsightGroup/qti3`'s `writer` cannot emit `qti-template-declaration` / `qti-template-processing`, so parametric item variants cannot be **authored** on the stack that can **deliver** them."* 🟢 **Remedy named, scoped and unusually small**: add a `buildQti3TemplateDeclaration` + template-processing emitter to the `writer` package — 🟢 **`qti3` is MIT (© 2026 Longsight, Inc.), so this is a contribution, not a procurement** — and `core`'s parser plus `packages/fixtures/xml/random-integer-template-reference.xml` give it a **ready-made round-trip oracle** (write → parse → execute → assert the draw lands on the declared grid). 🔵 **Interim workaround already specified and costs nothing**: hand-author the template XML from that fixture (~35 lines) and let `core` execute it — `compose/patterns.md`, corrected step 1. 🔴 **Prerequisite for whoever takes it: run the suite.** `P527` is read from source and fixtures because installing a third-party repository's dependencies is not permitted in this environment |

🔴 **All three are declared with the remedy *and* its cost, and none is a wish: each names the specific
artefact a later pass would have to produce.** 🟢 **`Gap 238` is the one a single pass could close
outright.**

---

## 🟢 The rows pass 43 changed, 2026-10-07

🔵 **Both rows were read **in full from their declaring line** before anything was declared closed or
re-scoped, as the rule at the top of this file requires.**

| Gap | What it said | 🟢 Pass 43 says |
|---|---|---|
| **238** | 🔴 *"`LongsightGroup/qti3`'s `writer` cannot emit `qti-template-declaration` / `qti-template-processing`, so parametric item variants cannot be **authored** on the stack that can **deliver** them."* Declared *"the cheapest gap on this KB… the one a single pass could close outright"* | 🟢 **CLOSED with a tested artefact** — `compose/code/p533-qti3-template-emitter/` (`P533`). The gap was **reproduced first** at HEAD `0ca7d6fc`: writer **0 of 33** exports, core **34** files. The emitter regenerates **two** upstream fixtures **node-for-node**; those fixtures are the documents `qti3`'s own schema gate validates against the sha256-pinned official ASI schema, so validity is **transitive** rather than asserted. **43 assertions, 0 failures, 19 negative controls, 11 of 11 mutations detected.** 🔴 **Two stated limits**: the TypeScript port for upstream is **parse-checked only, not executed**, and the official XSD could not be fetched (`purl.imsglobal.org` proxy-blocked, `Gap 56` class). 🔴 **Nothing has been contributed upstream → `Gap 240`** |
| **237** | 🔴 *"No open-source essay scorer for Spanish"*, declared **structural**, with the remedy priced as *"a rubric and a human-graded corpus, per target country"* and the cheaper next probe named as the per-country query | 🟡 **RE-SCOPED, not closed — and its premise is refuted for Chile** (`P537`). The prescribed per-country probe was run verbatim and returned PAES practice platforms that grade **no written work**, 🔴 **because the PAES has no essay component**. 🔵 **So for Chile there is no rubric to automate and no corpus to build — the remedy as written is not expensive, it is void.** 🟢 **The gap's first question is therefore prior to its remedy**: *which Spanish-speaking systems examine writing against a published rubric?* Only those are candidates. 🟢 **The same probe also returned `P535`**, an asset ten passes of English queries had missed |

🔴 **Do not quote "Gap 238 closed" without its two limits, and do not quote "Gap 237" as merely
unmeasured** — one of its countries is now answered in the negative.

## 🟢 Live gaps declared by pass 43 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **239** | **2026-10-07**, pass 43 | `agents/top.md` · `P535`; `compose/patterns.md` · `P540` | 🔴 **OPEN, and it is now the binding constraint on `Gap 236`.** *"The feature layer of the only permissive assembled essay scorer is English-locked."* 🟢 **Narrowed by measurement**: `wwrwbs/AI_AWE` is **Apache-2.0 with permissive closure across its whole tree** (only other payload: vendored `TextComplexityToolkit` → **MIT**), and its architecture, Qwen2.5 base family and LoRA harness all transfer. 🔴 **What does not transfer is module 2** — a LightGBM model over **31 TAALED/QuanSyn features** computed from **English wordlists** (`dep_files/adj_lem_list.txt`, `real_words.txt`). 🔵 **Remedy named and scoped**: measure whether spaCy's `pt_core_news_*` pipelines support TAALED-equivalent lexical and syntactic metrics, and if so port the extractor; if not, select a Portuguese feature set from scratch. 🔴 **Cost stated**: this is a linguistics task before an engineering one, and it is the reason `Gap 236` is a *retarget* and not an *integration* |
| 🆕 **240** | **2026-10-07**, pass 43 | `repos/foundations.md` · `P533` | 🔴 **OPEN, and it is the smallest gap on this KB.** *"The `Gap 238` emitter exists and tested, and has not been contributed to the upstream repository it was written for."* 🟢 **The whole artefact is ready**: `writer-contribution.ts` is already in the host project's idiom with verified imports, and `qti3` is **MIT (© 2026 Longsight, Inc.)**, so this is a contribution rather than a procurement. 🔴 **Prerequisites, both outside this environment**: run `qti3`'s own suite (third-party dependencies are not installable here) and run `scripts/check-test-xsd.mjs` against the official ASI schema (`purl.imsglobal.org` is proxy-blocked). 🔵 **Cost: one pull request by someone with a working `qti3` checkout.** 🔴 **Opening it is a deliberate outward action and was not taken unprompted by this pass** |
| 🆕 **241** | **2026-10-07**, pass 43 | `intel/trends.md` · `P538` | 🔴 **OPEN as a citation gap, not a measurement gap.** *"The EU Annex III education deferral to December 2027 cannot be cited primarily from this environment."* 🟢 **The split itself is consistent across every secondary source found**: Annex III high-risk education obligations **deferred ~16 months to December 2027**, **Article 50** transparency **unchanged at 2026-08-02**, **Article 4** AI-literacy in effect with relaxed scope. 🔴 **But `eur-lex.europa.eu` and `data.europa.eu` are proxy-blocked (`Gap 56`, open since ~pass 24) and the secondary sources name the amending instrument inconsistently.** 🔵 **Remedy and cost**: one pass with eur-lex reachable pins the amending regulation's identifier and OJ date — minutes of work, blocked on network policy rather than effort. 🔴 **Until then this date must not appear in a client deliverable as settled law** |
| 🆕 **242** | **2026-10-07**, pass 43 | `intel/market.md` · `P539` | 🟡 **OPEN as an unresolved contradiction inside one publisher.** *"The Digital Education Council's own summary says EMEA has the lowest future AI adoption intent of any region, while its survey coverage reports EMEA at 89% and US & Canada at 67%."* 🔵 **Both figures are quoted; the summary's claim is not carried.** 🔴 **Why it matters rather than being pedantry**: `P539` is the first **comparable** four-region measurement this file has ever held, and the regional ordering it produces — LATAM 94 > APAC 92 > EMEA 89 > NA 67 — **inverts this KB's standing assumption** that LATAM is a follower region. 🔵 **Remedy and cost**: obtain the primary DEC 2026 report and read its regional definitions; low cost, and it decides whether a headline ordering is usable in a pitch |
| 🆕 **243** | **2026-10-07**, pass 43 | `intel/trends.md` · `P541` | 🔴 **OPEN, and mechanically closable.** *"Instruments in `compose/code/` that take paths by argument are not known to refuse empty input, and one of them reported success while measuring zero files."* 🟢 **Measured, not suspected**: of the three gates invoked this pass, `p243` self-discovers its files (correct), `p239` crashes (ugly but unmistakable), and 🔴 **`p383` printed `total 0` and exited `0` having read nothing** — proven by planting a `### Latam` that it still passed. 🟢 **`p383` is fixed** (`main([]) → 2`, plus three regression assertions; suite **8/8 → 11/11**). 🔴 **The other ~120 directories in `compose/code/` were NOT swept.** 🔵 **Remedy and cost**: one pass, one loop — invoke every argument-taking instrument with no arguments and assert a non-zero exit. Cheap, and it audits every pass-count this KB has ever published |

🔴 **All five are declared with the remedy *and* its cost.** 🟢 **`Gap 240` is the one a single person
with a working checkout could close outright, and `Gap 243` is the one that would tell this KB how much
of its own evidence is real.**

---

## 🟢 The rows pass 44 changed, 2026-10-07

🔵 **Every row below was read **in full from its declaring line** before anything was declared closed
or re-scoped, as the rule at the top of this file requires.**

| Gap | What it said | 🟢 Pass 44 says |
|---|---|---|
| **243** | 🔴 *"Instruments in `compose/code/` that take paths by argument are not known to refuse empty input, and one of them reported success while measuring zero files."* Declared **"mechanically closable"** and *"the one that would tell this KB how much of its own evidence is real"*, with the remedy as *"one pass, one loop — invoke every argument-taking instrument with no arguments and assert a non-zero exit"* | 🟢 **CLOSED with a tested artefact** — `compose/code/p542-empty-input-sweep/` (`P542`). **187** invocation points swept; 🔴 **23 confirmed** `P541`-class defects (**16** `FALSE-PASS` proved by an audit-hook read count, **7** `SILENT-SUCCESS`), against **43** `REFUSES`, **15** `MEASURES`, **31** library modules and **35** stdin filters correctly excluded. **42/42 suite, 7 mutants killed**, and the sweep **refuses its own empty input**. 🔴 **Two of the 23 are this KB's own gap gates** (`p370`, `p471`). 🟢 **The gap's prediction paid immediately**: `p383` run against `intel/market.md` for the first time returned **14 findings** — an **8-block / missing-`Global`** backlog seven passes old, invisible because the gate had been invoked with no arguments. 🟢 **Backlog cleared; `p383` now exits `0`.** 🔴 **Two stated limits**: the gap's one-line remedy **over-accuses** (49 → 23, `P543`), and oracle A does not reach shell → **`Gap 244`**; the 23 defects are **named and unfixed** → **`Gap 245`** |
| **239** | 🔴 *"The feature layer of the only permissive assembled essay scorer is English-locked."* Remedy: *"measure whether spaCy's `pt_core_news_*` pipelines support TAALED-equivalent lexical and syntactic metrics, and if so **port the extractor**"* | 🟡 **NARROWED HARD and its remedy RE-SHAPED — not closed.** 🟢 **The prescribed probe paid and over-delivered**: a Brazilian-Portuguese feature layer exists and is more complete than the gap assumed — `nilc-nlp/nilcmetrix`, **23** metric modules, a Go HTTP service, HEAD `5416e43` (2026-08-27). 🔴 **But the whole tier is non-permissive, measured from payload** (`P544`): nilcmetrix **AGPL-3.0** (and it is a *network* service, so §13 is the live trigger), `coh-metrix-port` **GPL-3.0**, and 🔴 **`kristopherkyle/TAALED` — the tool this gap names as module 2's feature source — is CC-BY-NC-SA-4.0, NonCommercial**, refused by `commercial_use_ok()`. 🟢 **So the verb changes: *reimplement* from published index definitions over spaCy (MIT, verified `c2dabfc`), with nilcmetrix as a locally-run comparison oracle only — the `P504` shape.** 🔴 **A later pass must not read pass 43's "31 TAALED/QuanSyn features" as "TAALED is available to build on."** → residual at **`Gap 246`** |
| **242** | 🟡 *"The Digital Education Council's own summary says EMEA has the lowest future AI adoption intent of any region, while its survey coverage reports EMEA at 89% and US & Canada at 67%."* Remedy: *"obtain the primary DEC 2026 report and read its regional definitions"* | 🟡 **NARROWED — a better instrument is named, and the remedy is cheaper than it was.** 🟢 **`P548`: the UNESCO IESALC + UNU-IAS working paper (September 2026)** — **200 higher-education institutions across 19 countries**, fielded **August–October 2025**, mapping AI use across teaching and learning, research, community engagement, administration and governance. 🔵 **Why it supersedes the remedy as written**: its sampling frame, fielding window and country list are stated, which is the precise property the DEC summary lacks and the reason the contradiction could not be settled. 🔴 **Located and named, NOT read — no figure from it is quoted anywhere this pass**, so `Gap 242` stays open and the DEC ordering stays unusable in a pitch |

🔴 **Do not quote "Gap 243 closed" without its two limits**, and 🔴 **do not quote "Gap 239" as
merely English-locked** — its blocker is now a **licence**, not a language.

## 🟢 Live gaps declared by pass 44 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **244** | **2026-10-07**, pass 44 | `repos/foundations.md` · `P542`; `compose/code/p542-empty-input-sweep/README.md` | 🔴 **OPEN, and it is the half of `Gap 243` that did not close.** *"The read-count oracle does not reach shell, so 31 shell instruments that exit `0` after emitting output are unjudged, and 9 more time out."* 🟢 **Bounded, not vague**: the exact 40 rows are named in `result.2026-10-07.tsv` as `P542-UNADJUDICATED-OUTPUT` (31) and `P542-UNADJUDICATED-TIMEOUT` (9). 🔵 **Why it matters rather than being completeness for its own sake**: oracle B (silence) already caught **7** shell defects, so the shell population is **known to contain** this defect class and the 31 are where the rest would be. 🔵 **Remedy named and scoped**: a `PATH` shim exporting logging wrappers for `grep`/`cat`/`sed`/`awk`/`curl`/`git` ahead of the real tools, so a shell gate's judged-input count becomes measurable the way the audit hook makes Python's. 🔴 **Cost: one pass.** 🔴 **A tracer is NOT the remedy here — `strace` works but wrapping the cloned tree's code in it is not permitted in this environment** |
| 🆕 **245** | **2026-10-07**, pass 44 | `repos/foundations.md` · `P542` | 🟡 **PARTIALLY CLOSED at pass 49 — 2 of 23.** 🟢 The two this row names as priority (`p370-gap-gate`, `p471-gap-gate-language`) are fixed, each with a guard **and** a regression assertion; suites **27/27** and **25/25**; 🟢 **`p542` sweep re-run: 23 → 21 defects** (`P599`). 🔴 **The remaining 21 are re-declared as `Gap 253`** so this row cannot be read as closed. 🔵 Pass-44 text kept verbatim: OPEN, and it is the cheapest gap on this KB — cheaper than `Gap 240`. *"The 23 instruments that report success over an empty input are identified and not one of them is fixed."* 🟢 **The fix is known, written and already proven once**: `p383-region-heading-gate` is the worked example — `if not argv:` → print a refusal naming the correct invocation, `return 2`, plus a regression assertion. 🟢 **The 23 are enumerated by path and class** in `result.2026-10-07.tsv`, so there is no search step. 🔴 **Cost: mechanical, one pass, ~23 guards and 23 assertions** — and the sweep itself is the acceptance test, since it must drop to **0** `P541-*` rows. 🔴 **Why it was not done this pass, stated rather than hidden**: 23 edits across 23 directories, each needing its own suite re-run, is a second pass's work and bundling it with the instrument that found them would have left neither verifiable. 🔵 **Priority order named: `p370-gap-gate` and `p471-gap-gate-language` first** — they are the gates that exist to catch undeclared gaps |
| 🆕 **246** | **2026-10-07**, pass 44 | `agents/top.md` · `P544`; `compose/patterns.md` · corrected step | 🔴 **OPEN, and it is now the binding constraint on `Gap 236` in place of `Gap 239`'s language framing.** *"No permissively-licensed Portuguese text-complexity feature extractor exists, and the spaCy `pt_core_news_*` **model artefact** licences are unmeasured."* 🟢 **Narrowed by measurement on both halves**: the index definitions (TTR, MTLD, MATTR, HD-D, syntactic-complexity indices) are **published statistics, free to reimplement**, and spaCy's **code** is **MIT** (payload read at HEAD `c2dabfc`, holder `ExplosionAI GmbH / spaCy GmbH / Matthew Honnibal`). 🔴 **⛔ SUPERSEDED IN PART — the artefact licences ARE measured.** 🔵 Forward pointer added by pass 49 (`P597`): `pt_core_news_sm/md/lg` are **CC-BY-SA-4.0** at **3.8.0 and 3.7.0** (`agents/top.md`, `verticals/solutions.md`), inherited from `UD_Portuguese-Bosque`; measured **before** pass 49 and re-confirmed by it. 🔴 **Pass 49 read this row top-down, believed "unmeasured", and spent budget re-measuring settled work** — the second instance of `P582`, and the first found by paying for it. 🟢 **Still genuinely open: halves (b) and (c) only** — the *extractor* and its validation. 🔴 **And `P595` adds what this row never covered: `es_core_news_*` is GPL-3.0** → **`Gap 254`**. 🔵 Pass-44 text kept verbatim for citation integrity: what was unmeasured is the model artefacts, which ship separately from the MIT code and may carry different terms — and a scorer that cannot license its tokeniser has no feature layer at all. 🔵 **Remedy and cost, split**: (a) read the `pt_core_news_*` artefact licence — minutes, and it gates everything else; (b) reimplement the index set over that pipeline — days; (c) 🔴 **the expensive part is validation**, since the published tools carry years of it and a reimplementation inherits none, so an agreement study against `essay-br`'s human scores is part of the work. 🔵 **Use nilcmetrix as a local comparison oracle only — never vendored, never hosted** (`P504` shape, and AGPL §13 is why) |

🔴 **All three are declared with the remedy *and* its cost, and none is a wish.** 🟢 **`Gap 245` is
the one a single pass could close outright, and `Gap 246`'s first step is minutes of work that gates
the rest.**
