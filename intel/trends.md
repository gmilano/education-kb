---
industry: education
region: Global
updated: 2026-10-26
---
## 🆕 Trend 49 — `p449` **An instrument sampled faster than the thing it measures reports its own clock and calls it a finding — and this base has now done that four times in a row, in the one file whose entire purpose is to record change**

🟢 **Gate posture first (`Gap 446-A`): `make hooks` RAN** — the fourth trial after three
denials, so `p448`'s settlement of that gap as *"a property of the host class"* is **refuted**.
The denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 two of them new
and both `p448`'s.

### The trend, stated as a measurement

`Trend 48` found that this base's instrument defects are **not random** — every one caught that
hour failed toward the answer the base already believed. 🟢 **`Trend 49` names the mechanism one
level down: the sampling rate.**

| quantity | value |
|---|---|
| inter-pass interval, median (n=**309**, `p49`-`p448`, commit→commit) | 🔴 **61.1 min** |
| p10 / p90 | **46.0** / **78.1** min |
| share inside 45-75 min | 🔴 **79.6 %** |
| `p448` commit → `p449` read | 🔴 **40 min 20 s** |
| GitHub trending refresh period | **daily** |
| ⇒ passes per channel snapshot | 🔴 **≈ 23.6** |
| ⇒ P(a pass observes an unchanged channel) | 🔴 **≈ 95.8 %** |

🔵 `p446`, `p447`, `p448` and `p449` each recorded a **saturated discovery channel**. 🔴 At this
cadence **that is the expected observation**, and it is consistent with an ecosystem moving at
full speed. Four saturations are **~zero bits** about supply
(`evidence/inter-pass-cadence.2026-10-26-p449.tsv`).

### Why this is a trend about *measurement* and not a scheduling complaint

🔴 **The failure mode is directional, exactly as `Trend 48` predicts.** A saturated channel reads
as *"the supply has been exhausted; the shelves are complete"* — which is the conclusion the base
already wants, because it is the conclusion under which its own shelves look finished. 🔵 Three
passes drew progressively stronger versions of it (`p446` "saturated", `p447` "standing",
`p448` "a third time"), and `p448` was right to register `Gap 448-A` rather than a fourth.

🟢 **The same lesson has now fired on three instruments in two passes, and the sign is always the
same:**

| instrument | defect | direction of failure |
|---|---|---|
| `p448` substring novelty check (`Gap 447-A`) | unscoped `grep -ri` | toward *"already known"* → suppress a real finding |
| `p448` tool extractor (`Gap 448-C`) | regex over all of `src/` | toward *"no write tools here"* → confirm read-only |
| 🆕 `p449` URL probe (`Gap 449-A`) | `curl -sI` on `github.com` → **403 on every real repo** | toward *"dead row"* → discard a live address |
| 🆕 `p449` URL probe (`Gap 449-B`) | case-normalised path | toward *"dead row"* → `XBlock` read 404 three times, then **200 / 11 358 B** at the recorded case |
| 🆕 `p449` discovery channel (this trend) | hourly sampling of a daily channel | toward *"saturated"* → shelves look complete |

🟢 **So the operating rule this base should adopt, and `p449` applies it to itself:** a nil is
not reportable without the **interval** over which it was measured, and an instrument is not
trustworthy until a **negative control** has been run through it. 🔵 `p449`'s URL probe carries
one (`zzz-fake-org-p449/zzz-fake-repo` → `404 / 14 B`); its tool count carries a second channel
(README prose, **187** against a true **188**); and its cadence claim carries a population of
**309** rather than the single interval `p448` could cite.

🔴 **The residual risk, named rather than resolved.** This measurement is one repository's commit
history on one schedule. It does **not** establish the refresh period of the *web search* channel,
only of GitHub trending — and the four global legs run each hour go through the former
→ `Gap 448-D` remains open and is now the binding uncertainty on every nil this base reports.

---

## 🆕 Trend 48 — `p448` **This base's measurement errors are NOT random: every instrument defect caught this hour failed toward the answer the base already believed. Three independent instruments, three different mechanisms, one direction — which means a saturated channel and a confirmed hypothesis are exactly what a broken instrument looks like.**

🔵 **Why this is a trend and not one pass's housekeeping.** `p447` caught a substring novelty
check reporting *"already known"* for a genuinely new item and registered it as `Gap 447-A`,
calling out that *"a substring check fails toward 'already known', which suppresses real
findings silently."* `p448` found **two more instruments with the same bias, by different
mechanisms, in the same hour** — and in one of them the bias would have **confirmed a published
hypothesis that is in fact false**. One instance is a defect. Three, pointing the same way, is a
property of how this base measures.

### 🔴 The three instances, each with its mechanism and the false conclusion it would have produced

| instrument | mechanism of the defect | the comfortable answer it produced | 🟢 the truth, measured |
|---|---|---|---|
| **substring novelty check** (`grep -ri`) | `teds` matches inside `relaTEDSubject` and `generaTEDStatus` — 3 hits, **0** word-scoped | 🔴 *"TSDS/TEDS already known"* → the NA state finding suppressed | 🟢 `grep -riw` = **0**. `TEDS`, `TSDS`, `PEIMS`, `CAASPP`, `ELPAC` all genuinely new |
| **MCP tool extractor** (regex over registries) | three unseen idioms: bare `@mcp.tool` with no parens (**130** occurrences read as **1**), nested-paren decorator args, and a **Go** codebase scanned only for `.py`/`.ts`/`.js` (read as **0**) | 🔴 *"the community LMS connectors are read-only"* → `Gap 447-B` **CONFIRMED** | 🟢 **136 of 414** declarations mutate (**32.9 %**); `create_course`, `toggle-module-publish`, `update-syllabus` all read from source |
| **pin-stability sample** (`Pattern AZ`) | the 18 pins were drawn from pins **already carried across passes**, i.e. pre-selected for having survived | 🔴 *"17 of 18 survive 24 h — a cheap minority repair"* | 🔴 Over 496 unbiased pinnings, **67.3 %** survive. **A third die.** |

🟢 **The first two were caught only because something external contradicted them.** The
substring hit was questioned because a *state-shaped* search had just produced a name the base
did not recognise. The extractor was questioned because its output was **absurd** — one tool in
a repository `p446` had independently counted at **128**. 🔴 **Neither was caught by a gate**;
`make hooks` has now been denied three passes running.

### 🔴 The structural reason, and it generalises past this base

Every one of these instruments answers a question of the form *"is there anything here?"*, and
each fails by **not finding** rather than by finding wrongly:

- a substring match **adds** false hits → the novelty test, which reads *hits = known*, flips to *known*
- a regex that misses an idiom **removes** tools → a capability test flips to *absent*
- a sample drawn from survivors **removes** failures → a stability test flips to *stable*

🔵 **A null result is therefore the least trustworthy result this base can produce**, because
it is the result every broken instrument produces. 🔴 And this base's most-repeated recent
finding is a null: **three consecutive passes of "discovery saturated, zero new rows."**

### 🟡 The second-order finding: `n = 1 per unit` manufactures confident, wrong rules

`Pattern AZ` published **three** quantitative claims from **five** observations — one pinning
per repository. `p448` re-measured with 14 pinnings per repository:

| `AZ`'s claim, from n = 5 | 🟢 `p448`, n = 496 |
|---|---|
| *"`pinned_date == HEAD date` **iff** the pin held, in every row"* | 🔴 biconditional **fails in 44 of 167** rows |
| *"**days** → settled, safe to quote"* | 🔴 at **1–3 days the pin fails 28 %** of the time; the real gate is **7 days → 97.4 %** |
| *"commit volume gets staleness **backwards**"* | 🔴 **ρ = +0.886.** Volume is a **good** predictor; the sign was inverted |

🔵 `Trend 45` already recorded an **n = 5 artefact** being published as a rule one pass earlier
(`Trend 44`), and `Trend 41` recorded that **12 %** of this base's own published figures came
from a method it had written a rule against. 🔴 **This is the third time.** The recurring shape
is not a bad instrument but a **denominator of one per unit**.

### 🟢 What follows, as checks rather than sentiment

1. 🟢 **Word-scope every novelty check.** `grep -riw`, never `grep -ri`. Two confirmed
   suppressions in two consecutive passes.
2. 🟢 **Never publish a null without an instrument control.** `Gap 446-D` is the model to copy:
   eleven primaries returning 403 was only interpretable because `raw.githubusercontent.com`
   returned **200** from the same shell in the same minute. A saturated discovery leg has **no
   such control** — and `p448`'s legs ran **43 minutes** after `p447` committed (`Gap 448-A`).
3. 🟢 **Make the absurdity check routine.** The extractor was caught because its output
   disagreed with a number another channel had already published. 🟢 Cross-channel agreement is
   now double-sourced on this shelf: source extraction reproduces `p446`'s README tool counts
   **exactly** at **128 / 126 / 89 / 69**.
4. 🔴 **One observation per unit is not a measurement.** Before a rule is published, state the
   per-unit denominator next to the population denominator.

🟡 **Limit of this trend:** three instances, one hour, one base. The *direction* is unanimous
and each mechanism is identified, but no one has gone back over earlier passes' nulls to measure
how many were instrument artefacts — the audit `Gap 444-D` asks for, still unpaid.

---

## 🆕 Trend 47 — `p447` **A region is a reporting bucket, not a research unit — and the cost of confusing them is not a thin answer but a MANUFACTURED one. The same hour that a region-level EMEA query produced two false, quotable facts, a country-shaped query killed both.**

🔵 **Why this is a trend and not one pass's bad luck.** This base has now nilled the EMEA
region-level leg on **three consecutive passes** (`p445`, `p446`, `p447`) and the North America
region-level leg on **six**. `p445` diagnosed the shape and prescribed country legs; `p446`
re-confirmed the nil and re-registered the prescription; `p447` finally **acted** on it. The
result was not a marginal improvement in yield. It was a **change in kind**.

### 🔴 What the region-level leg produced, and what the country leg did to it

| region-level output | country-leg verdict |
|---|---|
| French ministry signed a February partnership with Mistral to put a chatbot in **lycées** from 2026-27 | 🔴 **FALSE.** Amue is trialling two Mistral tools across **81 public HIGHER-EDUCATION establishments**, bounded to 2026; a separate pilot put a Mistral assistant in front of **10 000 state agents**. A *school* deployment that resolves to a *university* experiment plus a *staff* pilot |
| UK Generative AI in Education framework **updated March 2026** | 🔴 **FALSE.** Product-safety expectations were retitled and expanded **19 January 2026**; *module 3* carries **19 May 2026**; the only May-2026 circular is **Northern Ireland's DE Circular 2026/02** — a different jurisdiction |

🟢 **The mechanism, and it is the part worth generalising.** "EMEA" has no ministry, no statute,
no department and no publication calendar. A query addressed to it cannot be answered by
quotation, so the channel answers by **synthesis** — and synthesis across thirty jurisdictions
produces a sentence that is *shaped* like a fact, carries a month, names a real vendor and a real
department, and is wrong. 🔴 **A thin answer announces itself; a manufactured one does not.** This
is the failure mode `Trend 46` found on the supply side (ten addresses reading as ten options)
appearing on the **demand** side.

### 🟢 What a country leg does differently, mechanically

1. 🟢 **It has an addressable primary**, so the answer can be a quotation rather than a synthesis.
2. 🟢 **It can be run in the jurisdiction's own language** — the French leg was, and that is what
   separated *lycée* from *établissement d'enseignement supérieur*, a distinction the
   English-language region query collapsed.
3. 🟢 **It fails loudly.** A country leg that finds nothing returns nothing; a region leg that
   finds nothing returns an average.

🔵 **Standing instruction this base should now follow:** the five `###` headings on
`intel/market.md` are a **reporting** vocabulary — closed, five values, unchanged. They are
**not a research unit**. Research is addressed to a **country**; findings are **filed** to a
region. 🔴 Where a regional claim on these shelves cannot be traced to a country-shaped query,
it should be re-read as **possibly manufactured**, not merely as thin.

🟡 **The uncomfortable corollary, recorded rather than buried:** this base cannot currently
check any of it against a primary. Eleven official and one commercial host all refuse from this
host (`Gap 446-D`), on two independent channels with two different failure signatures. **The
country leg improves which question gets asked; it does not fix who can be read.**

---

## 🆕 Trend 46 — `p446` **An address count is not an option count. In the one education category where this base has the densest supply, 10 addresses are 6 projects — and the inflation is invisible to every channel this base routinely uses: stars, descriptions, file sets and directory listings all report ten.**

🔵 **Why this is a trend and not a one-off correction.** The LMS-MCP tier is where this base has
its **largest cluster of same-shaped addresses**, and it is also the tier an engagement reads
first, because the question a studio is asked on day one is *how many options do we have*.
`p446` measured it and the answer was **40 % smaller** than the shelf implied.

### 🔴 What each channel reports, against what lineage reports

| channel | what it says about the ten | correct? |
|---|---|---|
| **name** | ten addresses, seven of them literally `canvas-mcp` under seven owners | 🔴 no — says nothing either way |
| **description / README** | tool counts 187, 128, 126, 99, 89, 69 and four silent — **all different** | 🔴 **no, and actively misleading**: it splits `vishalsachdev` (128) from `Harikeshav-R` (126), which are the same project, and groups `bruchris` (187) with them, which is not |
| **file set** | ten distinct file-set digests | 🔴 **no** — a fork that adds or deletes files diverges immediately |
| **licence payload cell** | 🟢 **three collisions**: `5385a26e2fac` ×3, `ab5109aafdb8` ×2 | 🟡 **a strong hint** — a fork inherits the payload byte-identically |
| 🟢 **root commit** | 🟢 **six distinct roots across ten addresses** | 🟢 **yes, and it is decisive** |

### 🟢 The mechanism, stated so it generalises past this tier

🔵 A fork **cannot change its root commit** without rewriting history, and a project that was
genuinely written twice **cannot share one**. Every other signal is downstream of authorship
choices — a fork's owner renames the repo, rewrites the README, adds files, bumps the tool
count — and so every other signal decays toward *looks independent* over time. 🔴 **Which means
the inflation is systematically biased upward and grows with fork age**: the stalest forks look
the most distinct.

🔴 **`NelsonSpencer/canvas-mcp` is the specimen.** 416 commits, 218 files, a file set unlike any
other address, a README claiming 99 tools — and **714 commits behind** an upstream it shares a
2025-02-27 root with, carrying **2** commits of its own. 🟡 By every channel except lineage it
is a project. It is a stale fork with a local patch.

### 🟢 What this trend asks of the shelves

1. 🟢 **Count projects, cite addresses.** `p405` already fixed the citable unit as the
   **family**; this trend supplies the cheap instrument — `git clone --filter=blob:none` plus
   `git rev-list --max-parents=0`, **~1 s per repository, no GitHub API** (which is 403 here
   anyway).
2. 🔴 **Never infer lineage from prose similarity.** `Gap 445-C` did, and was right about the
   arms for a reason that does not hold — see `Gap 446-C`.
3. 🟡 **Treat a payload-cell collision as a lineage alarm, not a curiosity.** Two cells
   repeating across five addresses was visible in this base's own published cells before any
   clone was made, and nothing was looking for it.
4. 🟢 **Where a fork is the maintained side, say so.** In ARM-2 the root (`r-huijts`) is an
   **ancestor** of the fork (`mdweaver`, 4 ahead). Publication order and ownership do not
   predict direction; only history does.

🔵 **Scope, stated honestly.** This is measured on **one category, ten addresses, one pass**. It
is a method result, not a population estimate: this base does **not** yet know what fraction of
its ~134 shelved repositories are fork arms of one another. 🟢 **That is the obvious next
measurement and it is now cheap** — the instrument exists, and the root-commit column is the
whole test. Registered as `Gap 446-E`.


## 🆕 Trend 45 — `p445` **Publisher class does NOT predict grant presence in education open source. 🔴 `Trend 44`, published on this file one pass ago, was an n=5 artefact: measured over 3 932 first-hand addresses the institutional grant rate is 72.2 % against a 76.3 % baseline, Fisher p = 0.558. 🟢 What DOES predict the licence is the PLATFORM's developer community**

### 🔴 The claim this trend replaces, and why it was published

`Trend 44` (`p444`) reads: *"Where the institution publishes the integration code itself, it
publishes it WITHOUT a grant — and the third-party copy is the licensed one."* Its entire
basis:

| publisher class | n | grants present |
|---|---|---|
| institution | 3 | 🔴 **0** |
| individual | 2 | 🟢 **2** |

🔴 **One country (Brazil), one platform (SUAP), one institution (IFRN), five repositories.** A
measured rate of zero on three addresses became a trend about institutions — one pass after
this base corrected `Trend 42` for the identical error, *too small to carry the claim it was
used for*. The pattern is now twice-recorded on this file, which makes it a property of how
this base generalises and not of either tranche.

### 🟢 The test, at a denominator three orders of magnitude larger

`Gap 444-A` prescribed probing institutional GitHub orgs. That needs org enumeration, which is
**403 on this host** (`api.github.com`, `github.com/search` and `codeload.github.com` all
re-measured this hour). 🟢 **But the question needed no new network:** every address this base
has verified first-hand over 445 passes is on disk — **1 228 TSVs** under `evidence/`. Those
were classified by publisher class instead. Instrument, pipeline and stated limits:
[`compose/code/p445-publisher-class-census/README.md`](../compose/code/p445-publisher-class-census/README.md).

| | n |
|---|---|
| evidence files read | 1 228 |
| rows scored | 18 957 |
| rows excluded as unscoreable, and counted as excluded | 26 287 |
| 🟢 **distinct addresses with a first-hand grant verdict** | 🟢 **3 932** |

| class | n | grant | rate | 95 % CI |
|---|---|---|---|---|
| INSTITUTIONAL | 36 | 26 | 🟡 **72.2 %** | 56.0 – 84.2 % |
| NON-INSTITUTIONAL | 3 896 | 2 971 | **76.3 %** | 74.9 – 77.6 % |

🔴 **Fisher exact, two-tailed: p = 0.558.** Then all **36** institutional rows were
hand-labelled — the whole class, not a sample. **Nine were false positives** (precision
**75.0 %**): `UniversalDependencies`, an NLP treebank consortium caught on `univ` *inside its
own name*; `EscolaLMS`, a Polish LMS **vendor**; `schoolutils`, a developer utility org;
`schoolyardsms`, an SMS product. Every one is a **supplier or project** matched on an
institution word.

| after correction | n | grant | rate |
|---|---|---|---|
| by ADDRESS | 27 | 18 | **66.7 %** |
| by **PUBLISHER** (the correct unit) | 15 | 11 | **73.3 %** |
| non-institutional, same unit | 2 914 | 2 246 | **77.1 %** |

🟡 **The direction survives every cut — institutional is lower, by 4 to 10 points — and not one
cut makes it distinguishable from noise.** Predictions registered before the census ran
(`scratchpad/p445/predictions.txt`): **P3** (direction) confirmed but insignificant; **P4**
(*the rate of zero will not reproduce*) 🟢 **confirmed** — the rate is 66.7–73.3 %, nowhere
near 0 %; **P5** (*the classifier, not the arithmetic, is the binding error term*) 🟢
**confirmed**.

### 🔴 And the finding about this base, which is the part a successor must not skip

Only **36 of 3 932** addresses — **0.9 %** — have an institutional publisher at all. Nine are
misclassifications. The surviving 27 come from **15 publishers**, and **one of them — `cahlr`,
a UC Berkeley research lab — supplies 9 of the 27.**

🔴 **So the correct unit of analysis is the publisher, the real institutional n is 15, and after
445 passes this base has barely ever measured the class it published a trend about.** The
honest verdict is therefore neither *yes* nor *no*: the claim is **refuted at the magnitude it
was stated**, and the corpus is too thin in this class to put a sharp number on any residual
effect. That thinness is now measured instead of assumed — `Gap 445-A`.

🟢 **The sharp fact that does survive, and it is still worth money.** `ifrn` + `ifrn-oficial`
remain the **only** institutional publisher in the entire 3 932-address corpus with multiple
addresses and zero grants (3 of 3 ungranted, 81 ★ between them). That is a real and actionable
fact about **IFRN** — `Pattern AW` is unchanged — and it was never a fact about institutions.

### 🟢 What replaces it: the platform's developer community, not the publisher's class

Three readings of the same question now sit on this file, each from a different denominator:

| | claim | denominator |
|---|---|---|
| `Trend 42` (`p443`) | the student side of the glass is **permissive** — 6 of 8 | 8 addresses, 2 platforms |
| `Trend 43` (`p444`) | the modal grant is **NO GRANT** — 18 of 37, permissive 22 % | 37 addresses, 9 platforms |
| 🆕 `p445` | on **SIGAA**, measured end to end, the student side is **uniformly copyleft** — GPL-3.0, 3 of 3 | 3 addresses, 1 platform |

🔵 **Three incompatible answers, and they are not in conflict — they are three platforms.**
The variable that moves is not the side of the glass (`Trend 42`), not the publisher's class
(`Trend 44`), and not the country (`p443`/`p444` both tested that). **It is the licence habit of
the developer community that forms around a particular platform.** SUAP's community attached
MIT and nothing at all; SIGAA's attached GPL-3.0 three times out of three, in two languages,
across two publishers and four years.

🟢 **The operational form, which is the only part that should reach a client conversation:**
**the licence distribution is a property of the PLATFORM, so it must be measured per platform
and can be carried across neither regions nor publisher classes.** An engagement that meets a
new system of record has learned nothing about its grant posture from the last one, and the
probe is cheap — `git ls-remote` plus a blobless tree enumeration, which is what
`lib/probe_payload.sh` already does.

🔴 **The falsifiable half, so this trend is testable rather than another story:** a fourth
platform, measured end to end, should return a **fourth** distribution that matches neither
MIT-and-nothing nor uniform GPL-3.0. If two platforms in different countries return the same
distribution, this trend is wrong and the variable is something above the platform.

---

## 🆕 Trend 43 — `p444` **The LATAM education integration layer is not permissive and not copyleft: it is UNLICENSED. 18 of 37 addresses carry no grant at all, and `Trend 42` — published one pass ago — does not survive the larger denominator**

🔴 **The correction first, because this base published the claim it is correcting.**
[`Trend 42`](#) (`p443`) states that the open-source education supply is *permissive on the
student's side of the glass and copyleft on the institution's*, measured over **one tranche of 8
Brazilian and Argentine addresses**: 6 permissive (5 MIT, 1 Apache-2.0), 2 GPL-3.0.

`p444` measured the **same side of the same glass** in four more countries — Mexico, Brazil,
Chile, Colombia — over **37 addresses**, every one read first-hand this hour:

| grant | n | share | `Trend 42` predicted |
|---|---|---|---|
| 🔴 **no grant file at all** | 🔴 **18** | 🔴 **49 %** | not a category it had |
| GPL-3.0 | 9 | 24 % | — |
| 🟢 MIT | 7 | 19 % | 🟢 the majority |
| AGPL-3.0 | 2 | 5 % | — |
| 🟢 BSD | 1 | 3 % | 🟢 the majority |

🔵 **Permissive is 22 %, not 75 %, and the modal outcome is no licence at all.** `Trend 42` was
not wrong about its eight rows — re-read, all eight reproduce. It was **too small to carry the
claim it was used for**, and the claim it was used for was a composition decision: *"connectors
are safe to vendor, platforms are not."* On the larger denominator that is false for half the
connectors, and the failure mode is worse than copyleft, because copyleft at least grants.

🔴 **A missing LICENSE is not a permissive default and it is not an oversight to work around.**
Absent an express grant, the default is exclusive copyright: no right to copy, modify or
redistribute. A GPL-3.0 connector can be integrated under known obligations. An unlicensed one
**cannot be used at all**, however public the repository is, and however obviously the author
meant it to be shared.

### 🔴 And the unlicensed half is not the junk half, which is what makes it expensive

The intuition is that ungranted repositories are abandoned student scratch work. Measured
against last-commit dates, that intuition is **wrong**:

| | 🟢 live (HEAD 2026) | 🟡 2023–25 | 🔴 dead (≤ 2022) |
|---|---|---|---|
| 🟢 MIT / BSD | 🟢 1 | 1 | 6 |
| GPL-3.0 | 2 | 3 | 4 |
| 🔴 **no grant** | 🔴 **5** | 🔴 **4** | 9 |

🔴 **Five of the eight most recently maintained addresses in the whole tranche carry no
licence**, against **one** permissive one. Among them: `sebassg/sia-unal-mcp`, an **MCP server**
for a Colombian national university's system of record (TypeScript, HEAD 2026-03-12), and
`jeanhrm/siagie-analytics` (Laravel, 146 files, HEAD 2026-08-22). 🔵 **The licence frontier does
not track quality or activity — it tracks nothing at all**, which means a licence screen cannot
be deferred to a late diligence step: the best-maintained candidate is as likely to be unusable
as the worst.

---

## 🆕 Trend 44 — `p444` **Where the institution publishes the integration code itself, it publishes it WITHOUT a grant — and the third-party copy is the licensed one**

🟢 **Measured on the one tranche where both publisher classes exist at once.** Brazil's SUAP
ecosystem (Instituto Federal network) contains both institutional and individual publishers, at
comparable star counts:

| publisher class | addresses | combined ★ | grants |
|---|---|---|---|
| 🏛️ **the institution** (`IFRN/`, `ifrn-oficial/`) | 3 | **81** | 🔴 **0 of 3** |
| 👤 **individuals / student projects** | 4 | 71 | 🟢 **3 of 4** (2 MIT, 1 AGPL-3.0) |

🔴 **So the *sanctioned* integration path — official OAuth2 clients for Django and JavaScript,
and an API client suite, maintained under the institution's own GitHub organisations — is the
one with no right of use.** The engagement that reaches for the official client *because* it is
official reaches for the only one it cannot ship.

🟢 **The resolution exists and is on the shelf**, which is why this is a trend and not just a
complaint: [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) — **MIT,
HEAD 2026-09-05**, 98 Python files, 92 `.rst` of Sphinx docs, on PyPI, with CI, Codecov and a
`SECURITY.md` — does the *same job* as the unlicensed `ifrn-oficial/cliente_suap_django`, and
does it better. 🔵 **The individual's package is more professionally maintained than the
institution's**, which inverts the usual assumption about which to prefer.

🔵 **Why it probably generalises.** An institution publishes code as a *service to its own
users*, not as a product for redistribution, so nobody in the chain has a reason to pick a
licence. An individual publishes to a package registry — PyPI, Packagist, npm — and **a registry
asks for a licence field**. The forcing function is distribution, not governance.

🔴 **What is NOT established:** this is one network in one country. `Gap 444-A` prescribes the
test — probe the institutional GitHub organisations behind the paying platforms (UANL,
U. de Chile, UNAL, the SIGAA operators) and count grant presence **by publisher class**, not by
stars. Until then this is a one-tranche trend with a mechanism, not a measured law.

### 🟢 The engagement rule, usable today

1. 🔴 **Never start from an institution's own client.** Check its grant first; expect none.
2. 🟢 **Prefer the registry-distributed third-party package** — PyPI/Packagist/npm presence is a
   weak but real proxy for a licence actually having been chosen.
3. 🟡 **For a Moodle-side component, expect GPL-3.0 and treat it as coherent**, not as a problem:
   the host platform already imposes it (`moodle-local_suap`, HEAD 2026-10-19).
4. 🔵 **Ask.** 18 addresses here are one polite issue away from being usable, and no pass on this
   base has ever tested whether asking works (`Gap 444-C`).

---


## 🆕 Trend 42 — `p443` **In every region, the open-source education supply is permissive on the student's side of the glass and copyleft on the institution's — and the boundary is the system of record**

🟢 **The claim, with the first LATAM denominator behind it.** This base has recorded a "licence
frontier runs the wrong way" observation for EMEA for many passes. `p443` measured the same
boundary in LATAM, first-hand, over one tranche:

| layer | what it is | permissive | copyleft |
|---|---|---|---|
| 🟢 **student / teacher side of the glass** — readers, extensions, exporters, MCP connectors onto an academic portal | 8 addresses | 🟢 **6** (5 MIT, 1 Apache-2.0) | 2 GPL-3.0 |
| 🔴 **the institution's system of record** — platforms that hold enrolment, grades and attendance | 4 addresses | 🔴 **0** | GPL-2.0, GPL-3.0, GPL-3.0, AGPL-3.0 |

🔵 **And it is the same shape in the other three regions**, from rows already on these shelves:
EMEA's connectors (`librus-mcp`, `iserv-mcp`, `Smartschool-MCP`, `edupage-mcp`,
`dtu-learn-mcp`) are **MIT** while the platforms behind them are vendor-closed or copyleft;
North America's `canvas-mcp` and `fcps-school-mcp` are **MIT** against a closed Canvas and
Schoology; APAC's `SGU-Academic-MCP` is **MIT** against a closed university portal; and the
platform map on [`verticals/solutions.md`](../verticals/solutions.md) is **GPL-3.0, AGPL-3.0,
AGPL-3.0, LGPL-3.0, LGPL-3.0, GPL-3.0** with **Apache-2.0 OpenOLAT and MIT Kolibri as the only
two exceptions in the tier.**

🟢 **Why this is one trend and not two coincidences.** The asymmetry is structural, not
licensing fashion. A system of record is written by the institution that is accountable for the
records — a ministry, a municipality, a university consortium — and public money plus
public-good framing produces copyleft, which is exactly what `ipti/br.tag` (IPTI with Santa
Luzia do Itanhy/SE, *Tecnologia Social*), `eXeLearning` (Spain's education ministry) and Open
edX all are. The glass-side tooling is written by **students, lecturers and single authors who
want it adopted**, and that produces MIT. 🔵 The licence tells you **who wrote it and why**,
and in this industry that correlates with **which side of the record boundary it sits on**.

🔴 **What it costs a team that does not know this.** The platform is the part a client points at
and says *"start from that"*, and it is the part that cannot be vendored into a proprietary
deliverable. Two failure modes follow, and both are live on this base's evidence:

1. 🔴 **Vendoring the platform.** `ipti/br.tag` is the sharpest case ever recorded here, because
   its **README states BSD-3-Clause while its payload is GPL-2.0** — the conflict runs in the
   *permissive* direction, so the careless read is the expensive one, not the cautious one.
2. 🔴 **Reading the root and stopping.** `p442` found **12 of 134** repositories carrying more
   than one grant, and one row sold as MIT shipping a complete GPL-3.0 below its root. The
   copyleft in this industry hides **below** the root as well as behind the README.

🟢 **The design rule it yields, and it is the same rule in all four regions:** put the AI
**beside** the system of record and talk to it over an interface — an MCP server, a REST or
Web-Services client, an XBlock — and keep every line you intend to own on the glass side of the
boundary, where the grants are permissive. 🟢 **That is what makes a connector, not a platform
fork, the sellable unit of an education engagement** — and it is why `p443`'s one-row addition
to [`agents/top.md`](../agents/top.md) (`jpmanson/siu-guarani-mcp`, MIT, read-only, PII-gated)
carries more commercial weight than the 158-★ AGPL-3.0 school-management app it was found
beside. Recipe: `Pattern AV`.

🟡 **The bound on this trend, stated as one.** The LATAM half rests on **12 granted
repositories in one tranche** keyed on two platform names (SIGAA, SIU Guaraní) in two
countries. Peru, Colombia, Chile and Uruguay returned nothing on the name leg and that is an
**unverified nil, not an absence** — the leg ran once, in one shape (`Gap 443-B`). The
four-region claim above is **consistent across every row this base holds** but has a measured
denominator in LATAM only.

---

## 🆕 Trend 40 — `p442` **The second grant lives below the root, and in this industry that is where the copyleft is**

🔵 `Trend 37`: a licence **name** without a licence **text**. `Trend 38`: a tool that declines
and a tool that clears produce the same green. `Trend 39`: a complete grant no title-keyed
tool can classify. 🟢 **`Trend 40` is the structural one: the repository's licence question has
more than one answer, and the extra answers are not at the root.**

🔴 **Measured, 2026-10-25, over the 134 repositories whose payload path these shelves
publish** — every tree enumerated first-hand:

| | n |
|---|---|
| exactly one own-grant path | 🟢 121 |
| 🔴 **more than one** | 🔴 **12 (9 %)** |
| 🔴 more than one **family** | 🔴 **4 (3 %)** |

🔴 **And the direction is the commercially dangerous one.** Of the four multi-family
repositories, **three put the stronger obligation below the root**:
`krzysztofbury/librus-mcp` is MIT at the root with a complete **GPL-3.0** in
`legacy_reference/`; `Hiepler/EuConform` is MIT at the root with **EUPL-1.2** beside it;
`withmarbleapp/os-taxonomy` is ODbL at the root with **CC BY-SA 4.0** for its content. 🔵 The
root file is the *permissive* one in each case, which is exactly the shape a rooted probe —
and a GitHub licence badge, and every scanner that reads one file — reports as clean.

🟢 **The inverse exists too and is worth as much money.** `24kchengYe/human-skill-tree`'s root
payload is a **notice**, so the project reads as ungranted while its real AGPL-3.0 sits in
`app/` — and that same notice carries a **dual AGPL-or-MIT option for `skills/`** that no
root-only read can see. **An enumeration finds permissive lanes, not only obligations.**

🔵 **Why this industry specifically.** Education repositories are *assemblies*: courseware
plus code, a platform plus per-module restatements, a skills pack plus an MCP server, a
taxonomy plus its data. Four of the twelve are per-module restatements of one grant
(`sakaiproject/sakai` ×4, `dodona-edu/dolos` ×3, `microsoft/agent-governance-toolkit`,
`The-Morrow-Project/Morrow-Bridge`) — harmless, and evidence of the same cause: **a
multi-artefact repository is forced to say the licence more than once, and the moment it says
it twice the two can differ.**

🟢 **What to do with it:** `Pattern AU` is the four-step screen, and step 1 is the enumeration.
The cost is **~0.7 s per repository** (blobless depth-1 clone, no API), so there is no version
of this trend where the screen is too expensive to run.

## 🆕 Trend 41 — `p442` **A published figure is a claim about a measurement, and 12 % of this base's own were produced by a method it had already written a rule against**

🔴 **The measurement, on this base's own shelves.** All **162** payload cells on
`agents/top.md`, `repos/foundations.md` and `verticals/solutions.md` were re-measured from the
file **and** through the preserved defect: 🟢 **143 reproduce**, 🔴 **19 (11.7 %) carry the
`P834` capture signature** — byte count short by the trailing-newline run and a digest taken
**of the stripped bytes**.

🔵 **Why this is a trend and not a bug report.** The rule existed (`lib/README.md`: *no byte
figure is published from `$(…)`*), the fix existed (`lib/payload_measure.sh::size_of_file`,
asserted 27/27 at `p837`), and the rows were written **afterwards, by passes that had both**.
Attributed: `p432` **5 of its 5**, `p433` **2 of 5**, `p438` **2 of 11**, every other pass
**0 of 113**. 🔴 So the defect is **intra-pass** — the same pass used the library for some rows
and typed others by hand — which means a reader cannot infer a cell's trustworthiness from
*who wrote it*, only from *re-measuring it*.

🟢 **The generalisation for anyone reading this base, or building one:** a correction needs
three things and the industry habit is to ship one. A **rule** tells the next author what not
to do. A **fix** gives them a correct primitive. 🟢 **Only a gate makes the wrong path cost
something** — and only if the gate sits on the artefact the reader trusts, which here is the
**cell**, not the payload. `make gate-cell-reproduction` is that gate: 21 offline controls,
11 of them negative, and a `CELL-UNMEASURED` verdict for any cell nobody has re-measured.

🔵 **The client-facing version of the same lesson, which is the reason it is on a trends
shelf:** when a vendor hands you a licence report, ask which figures were *re-derived from the
artefact* and which were *copied from the sentence that last stated them*. In this base's own
file the two were visually identical and 19 of them disagreed with the file they named.

## 🆕 Trend 39 — `p441` **Five of the twelve BSD payloads in this industry's teaching tier carry no title line, so every title-keyed licence tool reports them as UNKNOWN — and the tier they sit in is the one a university actually runs**

🔵 `Trend 37` found the supply chain shipping a licence **name** without a licence **text**.
`Trend 38` found that a tool which *declines* and a tool which *clears* produce the same
green. 🟢 `Trend 39` is the third member of that family and the most mechanical: **a
complete, unambiguous grant that no title-keyed tool can classify at all.**

🔴 **The measurement, first-hand, 2026-10-25.** Every BSD row this base publishes was probed
and graded clause-by-clause — **12 payloads across 11 repositories**. Five carry **no title
line**: they open on `Copyright (c) …` and go straight into `Redistribution and use in source
and binary forms`. Four of the five are **complete BSD-3 grants**:

| repository | payload | what a title-keyed tool sees |
|---|---|---|
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 1 475 B, complete BSD-3 | 🔴 no family |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 1 512 B, complete BSD-3 | 🔴 no family |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 1 531 B, complete BSD-3 | 🔴 no family |
| [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 2 819 B, BSD-3 **+ branding + CLA** | 🔴 no family |

🔴 **That is 1 in 3 of the tier, and the tier is not peripheral.** `jupyterhub` and `nbgrader`
are how a cohort gets identical compute and how assignments are released, collected, graded
and returned. A procurement review that runs a title-keyed scanner over this stack gets
`UNKNOWN` on the two most load-bearing components and a clean `BSD-3-Clause` on the
peripheral ones — **the opposite of the ranking a buyer needs.**

🟢 **The structural reason is worth more than the four rows.** GitHub's licence picker emits
a title; a maintainer pasting the OSI text does not. So the title is a property of **how the
file was created**, not of the grant — and any instrument keyed on it is measuring
authoring history. The grant itself is in the clauses, and the clauses were uniform across
all 11 complete payloads measured here (164 B → 2 819 B).

🔴 **And one family cannot be resolved from its body at all.** BSD-2 and BSD-3 differ in
exactly one clause, and it is a clause a grant-checker grades. Resolve the variant from it
and a **BSD-3 truncated at that clause** grades as a complete BSD-2 — a false clearance on
the precise shape the check exists to catch. 🔵 The generalisable rule, for every family and
every tool: **ask what the payload DECLARES that is independent of the clauses you are
grading.** GPL declares `version 3` in its operative text; BSD declares its variant in a
title line or not at all; and when there is no independent declaration, declining is the only
correct answer. Mechanism, controls and mutation results: `compose/code/p441-bsd-variant/README.md`.

### 🟡 The second half of this trend is about the research channel, not the code

🔵 `p440` recorded the regulatory channel as **saturated** after four regional legs returned
zero new facts. 🟡 `p441` ran nine legs and the refinement is sharp: **saturation is at the
STATUTE tier.** Four facts had zero prior mentions on this base and all four are
sub-statutory — Arkansas `H.B. 1958` (authorised-use policies, named human decision-maker),
Illinois `S.B. 1920` (state-board guidance due 1 July 2026), Austria's **Schoolpackage AI**
pilot programme, Singapore's **AI for Fun** elective modules.

🟢 **The instruction that follows, for successors and for engagement teams:** a statute names
a *deadline*; a programme names a *buyer*. Ask **which programme funds the pilot**, not what
the law requires — the law is already on `intel/market.md` and has been for nine passes.

🔴 **One channel is now declared unusable rather than re-bought.** The agentic-AI-in-education
market-size leg returned **$2.1 B (2026) → $3 B by 2034 at 4.5 % CAGR** and **$1.72 B (2025) →
$27.23 B by 2034 at 35.92 %** in the same search: a 9× divergence on one horizon. 🔵 Neither
figure is carried. A number that arrives with a 9× sibling is not evidence, and the next pass
should spend the leg elsewhere.

## 🆕 Trend 38 — `p440` **"Unknown" and "fine" render identically in every licence report in this industry, and the copyleft tier is where the difference is worth the most**

🔵 `Trend 37` (`p439`) established that the supply chain ships a licence **name** without
a licence **text**, and that every scanner reads the name. 🟢 `p440` measured the
*second* half of that failure, and it is the half a vendor's dashboard is built to hide:
**what an instrument does when it cannot answer.**

🔴 **The number.** This base's own grant-presence instrument, shipped one pass earlier and
working correctly, returned `GRANT-UNCALIBRATED` for **101 of 218** licence payloads —
46 %. Not wrong: *declining*, because it carried clause profiles for MIT, Apache-2.0 and
ISC only. 🔴 **And the declined set was not a random 46 %.** It was GPL (40), AGPL (22),
BSD (14), MPL (9), EPL (9) and LGPL (7) — **the entire copyleft tier**, which in
education is Moodle, Open edX, Canvas, Chamilo, Frappe LMS, BigBlueButton, OpenEduCat and
every SIS a LATAM ministry runs. 🔵 The instrument was most confident exactly where the
industry's exposure is smallest, and silent exactly where it is largest.

🟢 **After profiling the GPL family the remainder falls to 39 of 218 — and 10 payloads
move from "not judged" to "not a grant".** Seven of the ten are AGPL. They range from
287 B to 3 000 B under filenames like `agpl-3.0.txt`, against a real AGPL-3.0 of
34 523 B. 🔴 **None of them was a new defect.** They sat on this base for passes, inside a
verdict that reads, in any report that aggregates it, exactly like a pass.

**Why this is a trend about the industry and not a note about one tool:**

- 🔴 **The three-way answer is almost never rendered.** `PRESENT` / `ABSENT` /
  `NOT ASSESSED` collapses to two columns in every dashboard, SBOM summary and
  procurement spreadsheet this base has read. A row that says *"AGPL-3.0 ✓"* means "the
  title said AGPL-3.0", and the tick is supplied by the renderer.
- 🔴 **Copyleft is where the collapse costs most, and it is the direction nobody
  checks.** A truncated MIT payload costs an attribution line. A payload that names
  AGPL-3.0 and carries none of its clauses is a repository whose **§13 source-offer
  obligation is unresolved** — and the party who discovers that is the client who has
  already deployed it over a network.
- 🔴 **Version-blindness is the same failure one level down.** `GPL` is not a licence;
  GPL-2.0 and GPL-3.0 are, and they differ on the question that decides hosted
  deployments. Measured here: a complete GPL-2.0 licence lacks **four of GPL-3.0's six**
  operative clauses. Any tool that grades "GPL" against one text is wrong about the
  other, and in education the GPL-2.0 estate is concentrated in **one region's** SIS
  tier — so the error is not evenly distributed, it lands on LATAM.
- 🟢 **The honest instrument is the one that says it cannot tell.** `LGPL-3.0`
  incorporates GPL-3.0 **by reference by design**, so profiling it with GPL-3.0's clauses
  would mark every valid LGPL payload as a non-grant — true, and useless. `p440`
  declines on LGPL and registers why (`Gap 440-B`) rather than shipping a confident
  wrong answer about **BigBlueButton** and **OpenEduCat**.

🟢 **What to sell.** The artefact is a **three-column** component clearance report —
*verdict · the clauses actually found · what was not assessed and why* — with the
uncalibrated set published rather than suppressed. 🔵 `Pattern AQ` specifies the
clearance gate and `Pattern AR` makes it a CI artefact; `Pattern AS` (this pass) wires the
copyleft-specific read into both. A
client who has never seen the third column has never seen their real exposure, and in
this industry the third column is where their LMS lives.

---

## 🆕 Trend 37 — `p439` **The AI supply chain has learned to ship a licence NAME without a licence TEXT, and every scanner in the industry reads the name**

🔵 **The one-sentence trend.** As AI code generation and template scaffolding become the
default way a repository starts, the `LICENSE` file is increasingly **inherited furniture**
rather than an authored act — and the inherited artefact is often a *pointer* to a licence, or
a template vendor's own notice, instead of the grant the repository needs. 🔴 Measured in
live education supply this pass, not inferred.

**The specimen, and it is ordinary rather than exotic.**
[`spragginsdesigns/ai-tutor-webapp`](https://github.com/spragginsdesigns/ai-tutor-webapp)
ships `LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28` @ `963dfa9c55c7`. Titled Apache-2.0.
Graded by this base's own census: `scan_verdict = PERMISSIVE`, `stock = True`,
🔴 `needs_a_human = False`. Read, it is the Apache-2.0 **APPENDIX notice** — *"You may obtain a
copy of the License at"* a URL — and the holder it names is 🔴 **Vercel, Inc.**: the Next.js
template's notice, carried unchanged into a tutor application. Nothing in the repository
grants anything over the code its author actually wrote.

**Why this is a trend and not an anecdote — three independent observations from one hour:**

1. 🔴 **The deep tail of the discovery channel is mostly ungranted.** Of **23** new addresses
   at `ai-tutor` ranks 61–80 and `education-ai` ranks 21–40, **10 (43 %) carry no licence
   payload of any kind**. Supply is being produced far faster than it is being licensed.
2. 🔴 **Payload reuse is now visible at the byte level.** `Devanik21/AI-Nano-Course-Generator`
   and `Devanik21/FluentFlow` carry a **byte-identical** payload (`1e4635354929`) naming a
   holder, `Debanik21`, that **matches no GitHub account** — one letter off the owner. The
   notice obligation cannot be discharged against it. The same shape appeared at `p433`
   (`dmoshehun-prog` shipping `virgiliojr94`'s copyright line).
3. 🔴 **The class is already everywhere in this base's own corpus and nobody had joined the
   facts.** `make grant-presence-census`: of **218** titled payloads, **29** carry no granting
   words — **24 licence payloads plus 5 registry-metadata files** — and 🔴 **23 of them grade
   `stock = True, needs_a_human = False`.**

**What it means commercially, which is the part a client pays for.** A licence *scan* answers
"what is this called?" A licence *read* answers "what may we do, and what do we owe?" These
have been treated as the same question because for a decade the name implied the text.
🔴 **That implication is breaking.** Two obligations cannot be discharged from a by-reference
payload at all:

- **Apache-2.0 §4(a)** requires a redistributor to **give recipients a copy of the License**.
  A repository holding only the pointer has not done it, so the duty lands on whoever vendors
  it next — on an engagement, the client.
- **MIT's notice obligation** requires reproducing a holder name. Where that name is a
  template vendor or a misspelling, there is no name to reproduce that means anything.

🟢 **The defensible position, and it is cheap.** Ask the question of **clauses, not bytes**:
are the words that perform the grant present? That is `Gap 439-A`'s instrument
(`make gate-grant-presence`, 19 controls). 🔵 A byte floor is the tempting shortcut and this
base's own corpus refutes it — BSD stock payloads run **221 B → 1 514 B**, because BSD-0,
BSD-2 and BSD-3 are three lengths under one family name, so any single floor either misses a
truncated BSD-3 or condemns every valid BSD-0.

🔴 **And the tooling lesson is not "nobody thought of this" — it is that the fix did not
travel.** `P1065` on this base settled in pass 254 that **a pointer to a licence is not a
grant**, and `pass258-content-licence-family` implements the predicate by the right method.
🔴 It covers **Creative Commons content licences only**. The predicates that grade MIT,
Apache-2.0 and BSD — the families a client redistributes — never inherited it. 🔵 For a studio
reading this trend the transferable point is the one this base keeps paying for: **a licence
correction implemented in one classifier is not a capability of your pipeline.** Ask which
instrument *writes the verdict*, and whether the rule reaches it.

🟡 **How this trend connects to `Trend 36`.** `Trend 36` (`p438`) found that licence tooling
has learned to **detect** a modified grant and not to **escalate** one. 🔴 `Trend 37` is the
harder half: an **absent** grant is not detected at all, because every "is this stock?"
predicate in common use asks about the title, the family and the restrictions — and none of
them asks whether the granting text is in the file. 🔵 Together they are one trend seen from
two sides: **licence tooling matured against hand-written licences and the supply chain has
stopped hand-writing them.**

---

## 🆕 Trend 36 — `p438` Licence tooling has learned to **detect** a modified grant and not to **escalate** one, and the gap is widest exactly where the AI supply chain is growing

🟢 **The datum, measured on this base's own instruments rather than a vendor's.** One call to
`bespoke_census.grade()` on a new education specimen returns, in a single row,
`p1054_verdict = MIT-BODY-PLUS:unclassified-addition` **and** `needs_a_human = no`. Over the
**238** licence payloads committed under `compose/code/**/fixtures/`, **9** carry an addition
verdict and 🔴 **7 of those 9 are routed `needs_a_human = no`** — including `p427`'s own
two-family specimen, the payload this base wrote a 24-control gate about because it carries a
notice obligation of two. 🔴 A second instrument, `p427`'s `conjunctive_grant.classify()`,
returns `scope: None` on the same payload because every entry in its `SCOPE_MARKERS` is an
English phrase, and the clause is in Chinese.

🔵 **Why this is a trend and not a bug report.** The pattern holds across three generations of
tooling on this base, and the direction is consistent: **detection capability keeps growing
and the escalation surface does not.** `p228`'s shelf gate graded families. `p341` added a
title-form and an addition column. `p427` added conjunctive families. `p382` added subtrees.
Every one of those instruments **widened what can be seen**; `needs_a_human` — the one
function whose docstring says it produces *"the rows a consultancy must not clear from a
scanner's output alone"* — still reads the same three inputs it was written with: an English
restriction hit, a bespoke title, an unreadable payload. 🔴 **The industry shape is the same
one**: SBOM and licence-scanning tools report an SPDX identifier per file, and an SPDX
identifier is exactly the column that says `MIT` here.

🟢 **What makes 2026 the year it starts to bite.** The AI layer on an education engagement is
no longer three large dependencies; it is dozens of small permissive repositories, and
`p438`'s own census shows where they come from: the **tail** of the topic listings (0 new at
ranks 1–20, 7 new at ranks 41–60), written by individual authors, in their own language,
often in the last ninety days. 🔴 Those are precisely the payloads most likely to be a stock
text **plus a sentence the author added by hand** — and least likely to have been read by
anyone. **1 of the 9 addresses graded this pass (11 %) carried such a clause**, and the clause
shifted content-copyright liability onto the operator.

🔴 **The consequence that reaches a client, stated plainly.** A scanner report saying *"MIT,
cleared"* and a payload saying *"you carry the copyright liability for the material you feed
this"* are the same row. On an education engagement the material is textbooks and the operator
is the school or the ministry. 🟢 **The defensible position is a three-column clearance** —
family, addition column, and a human read of any bytes above the family's stock band, in the
payload's own language — now standing on `repos/foundations.md` and wired as a step in
`Pattern AQ`.

🟡 **What would refute this trend**: an addition column that routes to escalation by default
(the one-disjunct fix priced as `Gap 438-A`), or a measurement showing the addition class is
confined to sub-20 ★ repositories and therefore never reaches production. 🔵 The second is
testable and **this base cannot currently claim it**: the 7 un-escalated payloads in the
census include components already on these shelves, not only this pass's tail rows.


## 🆕 Trend 35 — `p437` Regulatory change now outpaces the open-source tooling built to track it, and the tools **fail confidently**

🟢 **The datum**: of five permissive EU-AI-Act compliance repositories graded first-hand this
pass, **two independently hardcode `2026-08-02`** as the high-risk enforcement deadline —
the date superseded by Regulation (EU) 2026/1744, which moved Annex III (education among them)
to **2 December 2027**. Neither repository contains a single reference to the amending
regulation. Both **assert the stale value in their own test suites**.

🔴 One of the two is `ark-forge/mcp-eu-ai-act`, which this base shelved at `p436` and wired
into `compose/patterns.md` as its `Obligation check` step. **The KB was shipping a recipe whose
compliance oracle contradicted the KB's own market intelligence.**

🔵 **Why this is a trend and not a one-off bug.** Three properties make it structural:

| axis | an ordinary stale dependency | a stale **regulatory** dependency |
|---|---|---|
| how it fails | throws, or drifts visibly | 🔴 returns a confident, well-formatted, **wrong** answer |
| what the test suite does | catches the regression | 🔴 **pins the error in place** — the wrong date is the expected value |
| who notices | CI | 🔴 nobody, until a client acts on the deadline |
| what screening catches it | version pinning, dependabot | 🔴 **none of licence, stars, recency or activity** |

🟢 **The two repositories share no code and no authors.** That is what makes it convergent
rather than coincidental: the ecosystem absorbed the original AI Act timeline, encoded it as a
constant, wrote tests around the constant, and then the law moved. Every project that did its
job carefully in 2025 is now carefully wrong.

### 🔴 The second-order effect, which is the commercially dangerous one

A stale deadline is not symmetric. `2026-08-02` is **in the past**, so these tools report that
a conformity deadline **has already been missed**:

- `ark-forge/mcp-eu-ai-act` `tests/test_compliance_roadmap.py:252` records that once that date
  passed, roadmap generation moved behind the paid plan — 🔴 **the stale date is load-bearing
  for a commercial funnel**, which is a reason it is unlikely to be fixed quickly.
- An education client told its Annex III obligations lapsed in August 2026 will either buy
  remediation it does not need, or conclude the regime is unenforced and disengage. Both
  outcomes are worse than no tool.

🟢 **The defensible position, and it is a sellable one.** Globant should treat
regulatory constants as **versioned data with a provenance claim**, never as code constants:
a date in a compliance artefact cites the instrument that set it (`Art. 113 as amended by
Reg. (EU) 2026/1744`), the way `tomdxb0004/eu-ai-act-risk-checker` does at `engine.js:32`.
🔵 That is the single discriminator between the correct and incorrect tools found this pass —
not architecture, not licence, not maturity. **Citation-carrying constants are the control.**

🟡 **The bound on this trend, stated.** Five repositories is a small sample, and all five are
EU-AI-Act tools; this pass did not test whether the same staleness affects education-specific
instruments (state guidance trackers, UNESCO frameworks). 🔴 That is the obvious next
measurement, and it is worth taking — this base's own regional shelves are themselves
collections of dated regulatory constants, which makes the KB a candidate for exactly the
defect it just found in someone else's code.

## 🆕 Trend 34 — `p436` In the two largest APAC school systems, AI in education has become a **teacher-licensing** question, not a curriculum question

🟢 **The datum**: China's 《"人工智能+教育"行动计划》 (`教科信〔2026〕1号`, 2026-04-02) states
that AI is to be written **into the teacher-qualification examination and certification**
(将人工智能纳入教师资格考试和认证内容), alongside bringing AI education **into local curriculum
systems** with mandated per-stage class hours.

🔵 **Why this is a trend and not a fact.** Every other instrument on these shelves regulates the
*system* — what software may decide, what data it may hold, which decisions need a human. A
licensing requirement regulates the **workforce**, and it behaves differently in three ways:

| axis | a system rule | a licensing rule |
|---|---|---|
| what it creates | a compliance obligation on a vendor | **standing demand** from every teacher-training institution |
| how it decays | superseded when the rule changes | **does not decay** — it is in the credential |
| who buys | the ministry or the district | **universities, normal schools, certification bodies** |

🟢 **Corroboration on the same axis, from a different jurisdiction and a different pass**: the
UAE's Cabinet AI curriculum (`p435`) is paired with **~22 000 educators to be trained**, and
India's CBSE mandate (`p435`) runs to a **2029 board examination**. 🔵 **Three of the four
largest APAC mandates are enablement programmes with a workforce number attached.**

🟡 **The counter-case is Japan, and it sharpens rather than weakens the trend**: MEXT's school
guideline is still **Ver. 2.0 (2024-12-26)** with Ver. 2.1 in committee since 2026-06-30. Where
there is no mandate there is no workforce number — so the two systems now need **opposite**
offers: compliance-and-enablement in China, and in Japan a voluntary-adoption case that has to
survive without a regulatory forcing function.

🔴 **Citation limit**: `moe.gov.cn` and `mext.go.jp` are unreachable from this host; both legs
rest on ~10 consistent secondary mirrors. Strong, and still secondary (`Gap 436-C`).

## 🆕 Trend 35 — `p436` A knowledge base's **own citations** decay faster than the repositories they point at, and nothing in this industry measures that either

🔵 **`Trend 9` established that a permissive licence has a shelf life.** `p436` measured a second
kind of decay on the same tree, and it is faster and less visible:

| decay channel | measured rate | instrument that sees it |
|---|---|---|
| a permissive grant going stale (`Trend 9`) | 195 of 1 449 older than two years (13.5 %) | 🟢 `gate-recency` |
| a shelf **row** silently deleted | **176** claimed promotions on no live row | 🟢 `gate-promotion-ledger` (`p436`) |
| a **citation** whose referent is gone | **110 of 464 register citations (23.7 %)** | 🔴 **nothing, before `p436`** |

🔴 **The second and third rows are self-inflicted**, which is what makes this a trend worth a
client conversation rather than housekeeping. The mechanism is ordinary: a full-file rewrite is
the cheapest way to keep a long document readable, and it is also a silent delete. On this tree a
rewrite at **pass 90** removed the rows defining `P527`, `P543` and `P599` **without taking an
`archive/` snapshot**, so 80 of the 110 dead citations are recoverable only from `git log -S`.

🟢 **The generalisable lesson for any client knowledge system**: an append-only log and a curated
shelf decay at completely different rates. `p436` measured **0** drops from this base's two
append-only shelves and **176** from its curated ones. 🔵 **So the architecture, not the
discipline, is what preserved the evidence** — the curated shelves were maintained by the same
passes that lost 176 rows.

🔵 **What to sell from this**: any "AI knowledge base" engagement needs a **join** between the
claim and the artefact, re-run on every write. Not a review process — a gate. `p436`'s is three
controls and 22 offline tests (`compose/code/p436-promotion-ledger/`), and it caught **three
defects in its own first builds** before publication.

# 📈 Trends — Education AI

> Current trends, re-measured each pass. Trends 1–8 are the standing set; 9–11 were added
> or amended on 2026-10-25 from first-hand measurement.

## 🆕 Trend 32 — `p435` Restriction in education has a **second axis**, and it is the learner's AGE, not the decision's autonomy

`Trend 31` (`p434`) found four jurisdictions on three continents converged on one operative
predicate: **AI as the operative basis of a learner decision with no human able to
intervene**. That is an *autonomy* test, and one architecture — human-in-the-loop, staged
artefacts, a recorded approval — serves all four. 🆕 **`p435` adds a fifth jurisdiction that
does not fit that shape at all.**

### The measurement

| Jurisdiction | Instrument | Axis | Effect |
|---|---|---|---|
| 🆕 **Norway** | PM Støre's announcement, **19 June 2026**, in force at the start of the **2026–27 school year** (late August) | 🔴 **AGE** | Near-total prohibition of generative AI for **grades 1–7 (ages 6–13)**; **grades 8–10 only under direct teacher supervision** |
| **NYCPS** (largest US district) | 2K-8 moratorium, with an exemption for assistive tech under an already-signed plan | 🔴 **AGE** | Student-facing generative AI barred below a grade floor |
| **Vietnam** | Decision **33/2026/QĐ-TTg**, sectoral compliance **1 Sep 2027** | 🟡 AUTONOMY | 46 high-risk categories, three in education |
| **EU** | Annex III via Regulation (EU) 2026/1744 → **2 Dec 2027**; Article 50 live since 2026-08-02 | 🟡 AUTONOMY | Grading, admissions, proctoring as high-risk |
| **Oklahoma / Maryland** | state statutes | 🟡 AUTONOMY | Human oversight; AI may not be the sole basis of a decision |

### 🔴 Why the two axes are not interchangeable, and what it costs to confuse them

An **autonomy** rule is satisfied by *architecture*: insert a human, stage the artefact,
record the approval, and the same build ships in Hanoi, Brussels and Oklahoma City. 🔴 **An
age rule cannot be satisfied by architecture at all.** No amount of human-in-the-loop makes
a generative tutor lawful for a Norwegian eight-year-old, because the rule is addressed to
**who the user is**, not to **how the output is used**.

🔵 **This is the same category error `p434` untangled inside NYCPS**, one level up. There,
*developing* an IEP and *delivering* an accommodation were read as one subject and they are
two. Here, *restricting the decision* and *restricting the audience* are being read as one
regulatory trend and they are two, with different remedies and different costs.

### 🟢 The engineering consequence: an age gate is a first-class requirement

| Requirement | Autonomy axis | Age axis |
|---|---|---|
| Human-in-the-loop on every learner-affecting output | 🟢 required | 🔵 insufficient on its own |
| Staged draft → human approval → record | 🟢 required | 🔵 insufficient on its own |
| **Per-learner age or grade band, enforced at the model boundary** | 🔵 optional | 🔴 **required** |
| **Teacher-supervision mode as a distinct runtime state** | 🔵 optional | 🔴 **required** (Norway's grades 8–10, exactly) |
| Roster-sourced age data, with its own retention rule | 🔵 optional | 🔴 required — and it is student PII |

🔴 **The trap, named:** an age gate needs the learner's age, which means the build now
processes a protected attribute it previously did not — in the EU under GDPR, in the US
under FERPA and COPPA, and in California under AB 1159's bar on training against student
data. **A compliance feature that creates a new data-protection exposure is the most common
way this goes wrong**, and the mitigation is that the age band must come from the roster
system of record and never be inferred, stored longer than the session, or sent to the
model provider.

### 🟢 Why this is commercially *good* news, stated without softening

🔵 **Both Norway and NYCPS exempt the same thing**: supervised use for older learners, and
delivery of accommodations under an existing plan. 🟢 **And both leave the entire
teacher-facing surface untouched** — lesson planning, differentiation, drafting, marking
support, administration. `Pattern AM` (the teacher-facing courseware factory, legal in NYC
*because* no student touches the model) is the architecture that clears an age restriction
by construction, and it now clears two instruments rather than one.

🔴 **What it closes:** any student-facing tutor pitch into Norwegian primary education, from
late August 2026. That is not a configuration change — it is a market that is shut, and a
proposal that does not say so is wrong rather than optimistic.

🟡 **Grade:** multiple consistent secondaries on Norway (AACRAO among them), **no primary
read** — `regjeringen.no` and `udir.no` are unreachable from this host, which is the same
ceiling `Gap 433-C` records for every government primary on these shelves. 🔵 Norway's own
directorate publishes code here under Apache-2.0
([`Utdanningsdirektoratet/PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public)),
so the **supply** side of this jurisdiction is first-hand even where the **policy** side is
not.

## 🆕 Trend 33 — `p435` A permissive licence has a measurable shelf life now, and in education **59 % of the supply is permissive while 20 % has no licence at all**

`Trend 9` asserted that a permissive licence has a shelf life and that nothing in this
industry measures it. `Trend 13` asserted that the supply has a currency problem. 🟢 **Both
are now measured, on this base's own corpus, from two channels that need no API access.**

### The licence distribution of education's visible open-source supply

All **2 450** addresses this base had recorded and never promoted, each grant read
first-hand off the repository's own payload on 2026-10-25:

| arm | n | share | what it means for a build |
|---|---|---|---|
| 🟢 **MIT** | 1 022 | 41.7 % | build on, ship, relicense the derivative |
| 🟢 **Apache-2.0** | 330 | 13.5 % | build on, with a patent grant and a NOTICE duty |
| 🟢 BSD / ISC / CC0 / ECL-2.0 / Unlicense | 97 | 4.0 % | build on |
| 🔴 **`NO-GRANT`** | **500** | **20.4 %** | **all rights reserved — not usable, and no badge says so** |
| 🔴 GPL / AGPL / LGPL | 329 | 13.4 % | integrate across a process boundary; never vendor |
| 🟡 CC-BY-NC-SA, CC-BY, PolyForm, BUSL, SSPL, MPL, EPL, EUPL | 89 | 3.6 % | read the specific terms; several bar commercial use |
| 🟡 UNRECOGNISED | 83 | 3.4 % | a real payload no classifier here names — a human must read it |

🔴 **The `NO-GRANT` arm is the finding.** One address in five in education's visible supply
has **no licence file on any of eight paths, on either `main` or `master`**. 🔵 This is not
the same as "unclear licensing": it is the absence of a grant, which defaults to all rights
reserved. 🔴 **And it is invisible to the channel most teams use** — a GitHub licence badge,
a package manifest, or a directory listing. `Trend 29` already showed GitHub's `license`
field failing in both directions; this puts a denominator under it.

### The currency distribution, from a channel `make` can reach

    git clone --depth 1 --bare --filter=tree:0 https://github.com/<slug>   # ~0.5 s, ~270 KB

| HEAD commit age (the 1 449 permissive addresses) | n | share |
|---|---|---|
| 🟢 0–30 d | **627** | 43.3 % |
| 31–90 d | 233 | 16.1 % |
| 91–180 d | 141 | 9.7 % |
| 181–365 d | 137 | 9.5 % |
| 1–2 y | 116 | 8.0 % |
| 🔴 > 2 y | **195** | **13.5 %** |

🟢 **43 % of the permissive supply committed this month.** 🔴 **13.5 % has not been touched
in two years** and is, for procurement purposes, archived — while carrying exactly the same
MIT badge as the 43 %.

### 🔵 Why the channel matters as much as the number

A star count is the usual proxy for "is this alive", and on this host it is **unobtainable
for a third-party repository**: `api.github.com` answers 200 and is authenticated, but
returns **403 per repository** with the body *"GitHub access to this repository is not
enabled for this session"*. 🔴 **No egress allowlist can fix a per-repository authorization
boundary across 1 449 repositories.** 🟢 The HEAD-date channel has none of that problem, is
reproducible from a `make` target, and measures the thing that actually matters — **whether
anyone is still maintaining it** — rather than how many people once bookmarked it.

🔵 **The practical rule this yields:** when qualifying an open-source base in education,
read the **payload** for the grant and the **HEAD date** for the life. Both are one request.
Neither is a badge.

## 🆕 Trend 31 — `p434` Four jurisdictions on three continents have converged on the **same predicate**, and it is a software-architecture requirement rather than a compliance checkbox

🟢 **The finding.** This pass's four regional legs were run for adoption and players, and what
came back from three of them was one sentence in four different legal traditions. The regulated
object is not *AI in education*. It is **AI as the operative basis of a decision about a learner,
without a human who can intervene**:

| Jurisdiction | Instrument | The operative predicate |
|---|---|---|
| **Vietnam** (APAC) | Decision **33/2026/QĐ-TTg**, under AI Law **134/2025/QH15** + Decree 142/2026/NĐ-CP | Automated testing/assessment is high-risk where the output is used **as the official result** of learner evaluation; requires human supervision, control **and the ability to intervene while the system operates** |
| **Oklahoma, Maryland** (NA, state) | 2026 session statutes | Human oversight required; AI barred as the **sole basis** for a high-stakes student decision |
| **Charleston County, NYCPS** (NA, district) | District policy | AI not the **sole basis**; NYCPS goes further — special-education documents **must be developed by qualified professionals** |
| **EU** (EMEA) | AI Act Annex III + Regulation (EU) 2026/1744 | Education access and assessment are high-risk: risk management, data governance, **human oversight**, conformity assessment |

🔵 **Why this is a trend and not a list.** Four bodies with no coordination, no shared legal
tradition and opposite political economies wrote the same operative test. That is convergence, and
convergence is what makes an architecture *portable* — the rarest property in a market whose
standing description on this file (`Trend 3`) is **regulatory divergence**.

🟢 **So `Trend 3` is now half wrong, and the half that is wrong is the commercially useful half.**
Divergence is real in **scope** — who is covered, which grades, which subjects, what the penalties
are — and a single global *configuration* remains non-viable. But at the level of **mechanism**
the rules agree, which means one architecture satisfies all four:

1. the model **proposes**; it never commits;
2. a qualified human **approves**, and the identity and timestamp of that approval are **recorded**;
3. the operative record is written by **human action** into the authorised system of record;
4. the human can **intervene while the system runs**, not only after it finishes (Vietnam's clause
   is the strictest and therefore the one to build to).

🔴 **The trap, and it is the reason this is worth a trend rather than a line.** Draft-and-sign
satisfies predicates 1–4 **only where the regulated act is the DECISION.** Where a rule is
addressed instead to **who may develop the document**, human sign-off cures nothing — the drafting
itself is the prohibited act. 🔴 **That case is now measured and it is in the largest US school
district**: NYCPS's red tier bars **IEP and 504 plan development** outright (`Gap 433-B`, closed
this pass). 🔵 **So the architectural question to ask of every jurisdiction is not "do we have a
human in the loop?" but "is the regulated act the decision, or the drafting?"** — those need
different products, and `compose/patterns.md` `Pattern AL` now carries the split.

🟢 **What this is worth in a pitch.** The four-point architecture above is a **reusable compliance
asset**: built once, it is defensible in Hanoi, Brussels, Oklahoma City and Charleston on the same
evidence. 🔵 Two rows already on `agents/top.md` implement it today —
[`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp)
(draft for human sign-off **by default**) and
[`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent)
(`WAITING_REVIEW` with a **recorded** approve/reject) — both MIT. The compliance story is not a
document to write; it is two MIT repositories to wire together.

🔴 **The grade on the evidence, stated so nobody over-cites it.** Every regulatory cell in the
table is **corroborated across independent secondaries and not read in the official text**:
`Gap 433-C`'s egress ceiling is unchanged and was re-measured this pass. Vietnam's sectoral
compliance deadline of **1 September 2027** (education, healthcare, finance) is 🆕 new to this
file and carries the same grade.

## 🆕 Trend 30 — `p433` In North America the **district**, not the state, is now the layer that decides whether a build is legal

Every regulatory read on these shelves has been organised by **state**: 134 bills across 31
states, California AB 1159, Oklahoma and Maryland on human oversight, Ohio HB 96 and Tennessee
SB 1711 on policy mandates, Alabama HB 329 on graduation. That framing is now **the wrong unit for
a build decision**, and this pass can say why with three cases rather than one.

**What the states actually did.** Read the mandates together and a pattern appears: the states
that legislated mostly legislated *procedure*. Ohio and Tennessee require districts **to write
their own AI policies** — Ohio's deadline was **1 July 2026** and has passed. 35+ states publish
**guidance**. Oklahoma and Maryland set a *standard* ("not the sole basis") rather than a
prohibition. **A state telling every district to write a policy is a state declining to write
one.** The binding text ends up one level down, and by statutory design.

**What the districts did with that delegation.** They prohibited things, specifically and
unevenly:

| District | Instrument | What it bars |
|---|---|---|
| **New York City** | 2026-27 guidance, enacted **2026-09-02** | Student-facing generative AI, **grades 2K-8** (~600,000 students); **companion chatbots in every grade**, high school included. Preliminary (March 2026) red tier was reported to bar grading, discipline, counselling, placement **and special-education / 504 plan development**. 🆕 `p434`: **CONFIRMED in the current guidance** — the *"Red: Do Not Proceed"* tier names **IEP and 504 plan development** (*"All special education documents are developed by qualified professionals"*, citing IDEA and **Chancellor's Regulation A-710**). `Gap 433-B` **CLOSED, restrictively.** The IEP/504 *exemption* in the moratorium is a different subject — student-facing assistive tech under an existing plan — not a permission to draft one |
| **Charleston County** | district policy | Discipline, placement, **special-education determination** |
| **Katy ISD** | district policy | Generative chatbots K-6, scaffolded access to grade 12 |

🔴 **The three do not agree with each other, and none of them is a state rule.** NYC draws its
line at **grade 8** and adds an all-grades companion-chatbot ban; Katy ISD draws it at **grade 6**;
Charleston County draws it by **decision type** rather than by grade. A vendor compliant in Texas
is non-compliant in New York on the same product.

**Why this is a trend and not a list.** The delegation is *structural*: Ohio and Tennessee
**require** per-district policy, so the number of binding, mutually inconsistent AI rules in US
K-12 grows with the number of districts — roughly **13,000** of them — not with the number of
states. State-level tracking, which is what every tracker and every vendor summary does, is
measuring the layer that chose not to decide.

**What it changes in a build, concretely:**

1. **Student-facing vs teacher-facing stops being a product decision and becomes a
   configuration axis.** `Trend` guidance on this file already said *"student-facing optional
   should be an architectural switch from day one"*. NYC makes it unavoidable: the same deployment
   must run teacher-facing-only in grades 2K-8 and limited-student-facing in high school, **in one
   district**. A product that cannot be switched per grade band cannot be sold to NYC at all.
2. **Grade band becomes a first-class policy input**, alongside jurisdiction. Not a setting in an
   admin screen — a constraint the agent layer enforces and logs.
3. **Companion-chatbot shape is separately regulated from AI generally.** NYC bars companion
   chatbots in **every** grade while permitting teacher-facing AI. A persistent-persona tutor and a
   task-scoped assistant are now **different regulatory objects** even though they are the same
   technology, which is an argument for building the task-scoped one.
4. **Due diligence moves from statute to district policy.** `Pattern AL` now carries this as a
   go/no-go in week 1 rather than a formality.

🔵 **The honest limit on this trend.** All three district instruments are read from secondary
reporting; `Gap 433-C` records that no government primary is reachable from this host, so **none
of the three was read in its official text**. The *structure* of the argument — states delegating
by statute, districts prohibiting unevenly — rests on the Ohio and Tennessee mandates, which are
themselves corroborated across independent trackers. 🔴 Three districts is also not a census: this
is a pattern with three data points and a stated mechanism, not a measured rate across 13,000
districts. **What would strengthen it:** a sweep of the twenty largest US districts' AI policies.
No instrument on this base does that, and this pass did not build one.

## 🆕 Trend 28 — `p432` Regulatory intensity and open-source supply are **inversely** correlated in education, and special education is the proof

Every other trend on this file reads the market from the demand side. This one reads it from the
supply side and finds the opposite of what a market should do.

Rank education's surfaces by how hard the law constrains them, and special education is first in
North America by a wide margin: IDEA and §504 make the individualised education program a
**statutory instrument** with mandated timelines, mandated team composition and a mandated human
decision. Oklahoma and Maryland bar AI as the sole basis for a high-stakes student decision;
Charleston County names special-education determination explicitly. There is no surface in this
industry where "an agent drafts, a human signs" is more clearly *required* rather than merely
advisable.

Now rank the same surfaces by open-source supply. Measured this pass:

| surface | established open-source bases | ceiling |
|---|---|---|
| tutoring | DeepTutor, OATutor, OpenTutor, Bloom, Study-Mate, tutor-gpt, … | **42 610 ★** |
| LMS / platform | Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, Chamilo, … | institutional scale |
| LMS agents (MCP) | ~40 addresses across Canvas, Moodle, Classroom, Blackboard, D2L | hundreds of ★ |
| evaluation (`p431`) | tutorbench, tutor_gym, MathTutorBench | low hundreds |
| **special education / IEP** | **none** | **1 ★** |

584 addresses match the category and the top 30 by recency are all ≤ 5 ★. Three MIT tools exist;
they were created on 2026-10-14, 2026-10-23 and (the parent corpus) maintained to 2026-10-24.

**Why the inversion happens, and it is not mysterious.** Open source in education is built by the
people who can ship it — researchers, platform engineers, teachers automating their own marking.
A statutory workflow cannot be shipped by any of them alone: it needs district authorisation, a
system of record, a privacy review and professional liability. So the hardest-regulated surface is
the one hobbyist supply cannot reach, and the commercial market (PowerSchool Special Programs,
Frontline, SEIS) owns it uncontested.

**What it means commercially — and this is the actionable half.** The inverse correlation is a map
of where a services studio is *structurally* advantaged. Globant can supply exactly the things the
open-source channel cannot: the district relationship, the authorisation path, the audit trail and
the liability posture. On tutoring, Globant competes with a 42 k-star project; on IEP workflow,
there is no incumbent open base at all, and the three MIT seeds that exist are fork-and-own by
construction.

🔴 **The honest counterweight, stated so no deck overstates this.** No incumbent also means no
validation: no benchmark, no reference deployment, no second contributor on any of the three
addresses, and no evaluation harness that scores IEP goal quality (`p431`'s evaluation tier does
not reach this category). A first engagement here is a build, not an integration, and it must be
priced and sold as one.

🔵 **Prediction this base can be held to:** if the inversion is structural rather than a sampling
artefact, the special-education tier will still have no address above ~50 ★ in six months, while
tutoring adds another order of magnitude. Re-measure and record either way.

---

## 🆕 Trend 29 — `p432` GitHub's `license` field is a detector, not a verdict — and it failed in **both** directions in one eleven-repo sample

This base already carries three licence-trap trends: `Trend 6` (the permissive frontier runs
across the stack), `Trend 9` (a permissive licence has a shelf life) and `Trend 27` (a grant with
no title, a title with no grant). `Trend 29` is narrower and more mechanical, and it invalidates a
shortcut that is tempting precisely because it is cheap.

Two of eleven addresses measured this pass returned `license: NOASSERTION` ("Other") from the
GitHub API. **Neither was unlicensed.** Reading the payload at the pinned SHA resolved them to two
real licences at opposite ends of the commercial spectrum:

| Address | API said | Payload says, at HEAD | Commercial consequence |
|---|---|---|---|
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | `NOASSERTION` | **AGPL-3.0-or-later** · `LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f` | 🔴 Strong network copyleft. Cannot be vendored into a client deliverable. |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `NOASSERTION` | **CC BY-SA 4.0** · `LICENSE` 1 229 B · `40db9b472090` @ `135d6275e7db` | 🟡 Commercial use **and** adaptation expressly permitted — with a ShareAlike obligation on derivatives. |

**Why the detector abstained, in both cases for a formatting reason rather than a legal one.**
AlloFlow's grant sits behind a project title line and an SPDX header (`AGPL-3.0-or-later`) instead
of the stock licence title; the skills repo ships a short CC BY-SA notice-and-summary rather than
the full legal code. Both are perfectly valid grants. Neither matches the templates
`licensee` scores against.

**The three failure modes this produces, all of which cost money:**
1. **`NOASSERTION` read as "no licence"** → a usable base (CC BY-SA, commercially permitted) is
   discarded. A cost of omission, invisible in any audit.
2. **`NOASSERTION` read as "probably fine, it's on GitHub"** → AGPL-3.0 enters a hosted
   deliverable. This is the expensive one.
3. **A roundup's unsourced claim substituted for the file** → one article we read asserted
   "CC BY-SA 4.0" without citing the payload and happened to be right. The same article would have
   read identically if it were wrong.

**The rule, and it costs seconds.** `NOASSERTION` is not a value — it is a *flag to read the file*.
`git ls-remote` for the SHA, fetch the payload at that SHA, size + `sha256` it, read the first
twenty lines. And "no licence" is only ever established by `git ls-tree -r` over the whole tree:
that is how `grasped-dev/staircase` (0 of 33 files) and
`eakarsu/ai-special-education-iep-compliance` (0 of 29 files) were confirmed ungranted this pass,
rather than by a missing-file guess at one candidate path.

🔵 **New obligation family on these shelves.** CC BY-SA 4.0 is the first *content* ShareAlike grant
to land on a build-relevant row. `Trend 11` recorded data licences (ODbL on `os-taxonomy`);
ShareAlike-on-prompts is a third category again, and it bites a studio hardest where the
deliverable *is* text: a skill pack, a prompt library, a curriculum corpus. A pack derived from
those 165 skills must ship under CC BY-SA 4.0 — publishable, not proprietary. Decide that before
the statement of work, not after.

---

## 🆕 Trend 26 — `p431` The evaluation layer arrived, and it is permissive — which moves the sellable unit from *adoption* to *evidence*

For many passes this file carried `Trend 8` as a standing, unclosed **measurement gap**: this base
could supply tutoring agents but could not name the instrument that scores them. Measured
first-hand on 2026-10-25, **that gap closes on the tutoring side**:

| Harness | Grant | Maintained | What it scores |
|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 (code) | 🟢 commit 2026-10-25 | Scenario-based pedagogical failure + **regression** after a fix |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | 🔴 silent since 2025-09-10 | A model as **tutor** and as **simulated student**, inside real ITSs |

**Why this is a trend and not an inventory note.** `Trend 1` says adoption is finished and
governance is the market; `Trend 2` says procurement is being rewired around **evidence**. Both have
pointed at a deliverable this base could not actually build, because *“our tutor is pedagogically
sound”* was an assertion with no instrument behind it. With an MIT harness that binds to
`CAHLR/OATutor` — already on this base's verified shelf — and `pykt-toolkit` (MIT) underneath for
knowledge tracing, **tutor → measurement → evaluation is MIT end to end.**

🟢 **What that changes commercially.** The sellable unit stops being the tutor and becomes the
**evidence pack**: a scored baseline, a regression suite, and a re-test after each change. That is
the artefact HolonIQ's “evidence of improved learning” expectation, the EU's Article 50 transparency
duty, and a US district's procurement review each separately ask for — **one deliverable, three
jurisdictions**, which is `Trend 3`'s divergence problem answered rather than absorbed.

🔴 **The half that did not arrive, and it is the regulated half.** Everything measured scores
**tutoring**. **Nothing open scores grading.** The one grading-side candidate
([`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader)) is non-commercial by clause 2 of its
licence. Meanwhile NA (Oklahoma, Maryland: no high-stakes AI decisions without human oversight),
EMEA (Annex III: assessment is high-risk) and APAC (Vietnam: automated assessment on the high-risk
list) all regulate **assessment** hardest. **The most exposed surface is the one with no harness.**
Tracked as `Gap 431-C`; it is now the most valuable open gap in this base.

## 🆕 Trend 27 — `p431` The licence trap inverted: a grant with no title, and a title with no grant, in the same eleven-repo sample

`Trend 25` says a string matched as though it were a meaning is this base's most productive error
class. This pass produced **both directions of that error at once**, which is worth separating out
because the two need *different* instruments:

| Direction | Address | What a naive read returns | What the payload says |
|---|---|---|---|
| **Grant without title** | `Teachable-AI-Lab/tutor_gym` | `UNKNOWN` — the payload never contains the string `MIT License`; it opens at `Copyright 2025 …` | 🟢 **Verbatim MIT**, fully permissive |
| **Title without grant** | `sdrangan/llmgrader` | `MIT` — the file is named `LICENSE` and its first grant sentence is the MIT one, word for word | 🔴 **“PySilicon Research License”** — clause 2 forbids commercial use |

🔵 **The practical consequence: no single cheap check is sound.** A title sweep false-negatives the
first row and false-positives the second. A byte-size heuristic fails too — `llmgrader` is 1 224 B
against the stock MIT ~1 069 B, a 155 B difference that looks like a longer copyright line. A
`sha256` sweep catches the second only *after* someone has read it once and recorded the digest.

**The only instrument that is correct on both is reading the operative clauses.** For a studio this
is a cost line, not a philosophy: **budget one human licence read per address you intend to ship**,
and let the digest sweep do what it is actually good at — detecting *change* at a known address
between passes, which is how `p429` caught the `pengusto` relicensing within 24 hours.

🟡 **A third variant, same family:** `eth-lre/MathTutorBench` has **no licence file at all**, and a
README that cites CC-BY-4.0 in a badge and CC-BY-**SA**-4.0 in its licence section. Here even
reading does not settle it — the repository contradicts itself, so the honest record is
*ungranted*, not *probably CC*.

## 🆕 `p430` · 2026-10-25 — **Three trends added from first-hand measurement: a permissive licence has a SHELF LIFE (`Trend 9`), education's permissive supply is in the agent layer and not the platform layer (`Trend 10`), and DATA licences have arrived in education (`Trend 11`).**

## 🆕 Trend 9 — A permissive licence has a shelf life, and nothing in this industry measures it

The sharpest finding of 2026-10-25, and it generalises well beyond education.
`pengusto/google-classroom-mcp` was read as **MIT** by three separate passes
(2026-10-03, 2026-10-20, 2026-10-21). Every one of those readings was **correct when
taken**. On 2026-10-23 the maintainer relicensed to a proprietary **"Pengusto Commercial
License 1.0"**, effective 2026-10-24, whose §3 requires a paid agreement from
*"an educational institution or training provider, whether nonprofit or commercial"* — by
name, the exact buyer in this industry.

🔴 **The failure mode is not a wrong reading; it is a stale one.** A dependency inventory
that records `licence: MIT` with no re-read date will keep asserting MIT indefinitely.
Badges, package manifests and MCP directories all lagged the change.

🟢 **The practice that follows, and it is cheap:** read the licence payload at the commit
SHA you are actually consuming, record the SHA and a digest alongside the family, and
re-read before any engagement commits. On this pass the whole 24-repo sweep cost minutes.
Digest equality is also a *discovery* instrument: the abandoned MIT bytes
(1 145 B, `a01639b20880`) were found alive at `vTanco/google-classroom-mcp`, so the lane
was recovered rather than written off.

## 🆕 Trend 10 — Education's permissive supply is in the agent layer, and the platform layer is closed to it

Re-measured in full on 2026-10-25 across ten platforms and fourteen agents.

- **Platform tier:** 7 of 10 are copyleft — Moodle (GPL-3.0), Open edX (AGPL-3.0),
  Chamilo (GPL-3.0), eXeLearning (AGPL-3.0), Frappe LMS (AGPL-3.0), BigBlueButton
  (LGPL-3.0), OpenEduCat (LGPL-3.0). Only **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) and
  **Sakai** (ECL-2.0) are permissive.
- **Agent / MCP tier:** **14 of 14** verified rows are MIT, Apache-2.0 or BSD-3.

🟢 **This is a structural fact an engagement can be designed around**, not a complaint: put
the AI in the agent layer, talk to the platform over its API or component SDK
(`openedx/XBlock`, Apache-2.0, is the supported seam), and no copyleft obligation reaches
the client's IP. Building AI *into* the platform inherits its licence.

## 🆕 Trend 11 — Data licences are arriving in education, and they bite differently

`withmarbleapp/os-taxonomy` — the one genuinely new trending in-domain address this pass,
a 1 590-topic curriculum graph mapped to NGSS and Common Core — is **ODbL**, not a code
licence. Share-alike attaches to *derived databases*. A client's curriculum graph built on
it inherits the obligation.

🟡 As curriculum knowledge graphs become the substrate for adaptive learning, **licence
review in education has to cover data, not just code**. A code-only audit passes this repo
and misses the only obligation it carries.

---

## Trend 1 — Adoption is finished. Governance is the market.

**88–95% of students and faculty already use AI; 26–54% can name a governing policy.**
That gap, not the adoption curve, is what 2026–27 budget buys.

- Coursera (n=4,200, 5 countries): **95%** using AI academically, **26%** of educators report a
  formal institutional policy.
- EDUCAUSE 2026: only **54%** are aware of *any* policy or guideline.
- Ellucian (n=779): institutional adoption **49% → 66%** year on year, with **data privacy the top
  barrier**.
- Digital Education Council (n=45,398, 35 countries): **88%** of students, **77%** of faculty.

- 🆕 `p384` **UNESCO IESALC** (n=**200 institutions, 19 countries**, Sept 2026): **87%** of LAC
  higher-ed institutions use AI in at least one area — **74%** in teaching and learning, **57%** in
  research — against **26%** with a formal AI strategy. 🟢 **An independent, institutional source
  landing on the same 26%** as Coursera's educator-reported figure, in a different region with a
  different method. The governance gap is no longer an inference from one survey; it replicates.
- 🆕 **OECD TALIS 2024** puts teacher AI use at **~50%+** in Brazil, Chile, Colombia and Costa Rica
  against an **OECD average of 36%**; Uruguay's **Ceibal** reports **75%** of public-school
  teachers. 🔵 Practitioner uptake is running ahead of the OECD mean in LATAM — the governance gap
  is widest exactly where adoption is fastest, which is the opposite of the usual assumption.

**So:** stop selling introduction. Sell policy-to-configuration, audit trails and a governed
gateway. The shadow-AI estate already exists on every campus. 🟢 And sell it **hardest in LATAM**,
not last — the 87%/26% split there is the widest measured in this file.

## Trend 2 — The ROI reckoning arrived, and procurement is being rewired around evidence

- **~80%** of institutions are investing in AI; **29%** of CTOs say it met or exceeded ROI
  expectations (Inside Higher Ed / Hanover).
- **~7 in 10 provosts** use AI weekly themselves; **1 in 10** report a centralised institutional
  strategy. Personal adoption has outrun institutional capability.
- The **US Department of Education's "Dear Colleague" letter** tells states to evaluate ed-tech by
  **measurable learning outcomes rather than screen time**, and to put **evidence requirements into
  procurement**.
- **US/Canada faculty intent to keep using AI fell 76% → 67%** in one year.

**So:** a before/after measurement on the client's own subject mix is becoming a procurement
precondition, not a nice-to-have. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
MMLU and GSM8K are all MIT; there is no licence reason not to ship this with every engagement.

## Trend 3 — Regulatory divergence hardened in 2026. One global configuration is no longer viable.

Four regimes moved in four different directions in a single year:

| region | 2026 direction |
|---|---|
| **EU** | **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) pushed high-risk education systems from 2 Aug 2026 to **2 Dec 2027** — while **Art. 50 transparency still starts 2 Aug 2026** and **Art. 4 AI literacy has bound every school since 2 Feb 2025**. Emotion recognition in education: prohibited. 🆕 `p385` **The nearest date is neither of those: machine-readable marking of AI-generated content on systems ALREADY on the market is due 2 Dec 2026.** Annex I (AI embedded in regulated products) moves to **2 Aug 2028**. |
| **US** | No federal rule; **134+ bills across 31 states**, **33–35 states** with guidance, and binding district-policy mandates (Idaho SB 1227 effective 1 Jul 2026; Oklahoma SB 1734 by 2027-28). |
| **India / China** | **Content labelling and provenance**: India's amended IT Rules from **20 Feb 2026**; China's labelling measures from **1 Sep 2025** (988 services filed by 30 Jun 2026). |
| **Vietnam / Brazil / Mexico** | **Sectoral high-risk designation**: Vietnam names education among six high-risk sectors; Brazil's PL 2.338/2023 reportedly covers student selection; Mexico replicates the EU risk model. |

**So:** regional configuration is now a product requirement. The same tutor needs provenance
watermarking for India, a transparency notice for the EU, a prohibited-uses lockout for DC, and a
teacher-facing-only mode for ANZ and Brazil.

🆕 `p385` **Two corrections to how this trend gets sold.** First, **the EU deferral is widely
misread as breathing room.** It defers the *high-risk* regime; it defers nothing for a system already
deployed, which owes machine-readable marking on **2 Dec 2026**. A client told "the EU moved to 2027"
and nothing else has been misinformed about the only date within the current budget year. Second,
**employment-adjacent AI is separating from student-facing AI as its own regulated surface**:
**Illinois SB 2909** restricts AI in *teacher* evaluation from **1 Jan 2027**, where DC had only a
non-mandatory ban. A product that evaluates staff is a different compliance object from one that
teaches learners, and the two are still being scoped as one in most pitches.

## Trend 4 — Restriction is a real countertrend, not noise

For two years the only direction was adoption. In 2026 the brake appeared:

- **District of Columbia** 2026-27 policy bans AI from **grading, discipline, IEP decisions and
  teacher evaluations** — four of the highest-value automation targets.
- **Ipsos Education Monitor 2026:** **Australia and New Zealand show the highest support for
  banning AI in schools**, while Asian markets show the lowest. One company, two opposite mandates.
- **European Schools:** **no** generative AI tool approved for system-wide use.
- 🟢 **CONFIRMED at `p433`** (held 🔴 `UNCONFIRMED` from `p386`): the **New York City moratorium**
  on student-facing generative AI was **enacted 2026-09-02** for the 2026-27 school year, grades
  **2K-8**, ~600,000 students, with **companion chatbots barred in every grade**. **It holds — the
  largest US district has gone the other way**, which is no longer a conditional.

**So:** "student-facing optional" should be an architectural switch from day one, not a retrofit.
A product that cannot run teacher-facing-only is unsellable in a growing share of the market.

## Trend 5 — Teacher-facing is beating student-facing where growth is fastest

HolonIQ's **2026 LATAM EdTech 100** finds regional AI positioning concentrated in **teacher-facing
instructional tools rather than consumer tutoring** — Teachy (Brazil) in lesson preparation, Ginia
(Mexico) in employability. The regulation points the same way: Brazil's draft law targets
**student selection**, DC bans AI in grading and discipline, ANZ sentiment is restrictive.

**So:** the market and the regulator agree for once. Lesson preparation, assessment drafting,
feedback generation and administrative load carry the growth and avoid the hot zone.

## Trend 6 — The permissive-licence frontier runs *across* the stack, not along it

Measured first-hand this pass over 58 live repositories:

- **Platform tier is copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, Chamilo
  GPL-3.0, ILIAS GPL-3.0, Tutor AGPL-3.0, Frappe LMS AGPL-3.0, Sakai ECL-2.0, Opencast ECL-2.0,
  OpenEduCat LGPL-3.0, H5P GPL-3.0.
- **Exactly one permissive major LMS**: **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT),
  Apache-2.0** — and no roundup we read mentions it.
- **Agent tier is permissive almost throughout**: MIT / Apache-2.0 / BSD-3.

**So:** the architecture follows from the licences. Compose permissive agents **over** a copyleft
platform across **LTI 1.3**, **MCP** or web services — never fork the platform. The interop boundary
is a legal artefact as much as a technical one.

## Trend 7 — MCP reached the LMS, and that is genuinely new

As of 2026 the LMS is addressable by agents without a fork:

- **Moodle's own plugin directory** carries **`webservice_mcp`**, exposing Moodle's external
  functions as **MCP tools over JSON-RPC 2.0** — **Moodle 4.5–5.2**, latest release
  **23 Jul 2026**, gated on the `webservice/mcp:use` capability.
- **Canvas** is served by community MIT servers ([r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp),
  fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp)).
- 🔴 **No official server from Instructure or Moodle HQ**, and two of the most-advertised community
  Canvas/Moodle servers are **unlicensed** — see [`agents/top.md`](../agents/top.md).
- 🆕 `p387` **27 distinct education MCP server slugs are shelved** on
  [`agents/top.md`](../agents/top.md) — re-derived by this base's own `recount` instrument, which
  was runnable this pass for the first time in several (the figure stood at **12** here while the
  shelf had grown to 27). Across both agent shelves **MCP reaches **6 distinct LMS platforms**** —
  Canvas, Moodle, Google Classroom, Blackboard, Brightspace/D2L and Open edX. The cumulative
  harvest behind that is lopsided: **35 Canvas servers and 20 Moodle**, against **2 for Open edX**.
- 🔴 🆕 `p387` **A correction this shelf owed since `p386`, and did not carry.** The bullet above
  used to end *"Blackboard has 9 with not one verified grant and D2L has 6 with the only one
  checked ungranted"* — and concluded that a permissive server on either platform *"would be a real
  contribution."* `p386` probed all fifteen addresses and found **6 MIT grants on Blackboard and 6
  on D2L**; it corrected [`agents/top.md`](../agents/top.md) and **left this sentence standing**.
  🔵 The live claim is: on Canvas and Moodle the work is *selection*; on Blackboard and D2L the
  grants exist and the missing thing is **tenancy** — every granted server there authenticates as
  the signed-in student (see `compose/patterns.md` **Pattern N**, and `Gap 387-A`).

**So:** the integration cost of an LMS-aware agent dropped by an order of magnitude this year, and
the remaining risk moved from engineering to licensing.

## Trend 8 — Measurement gap in this pass, stated rather than papered over

**No popularity metric is published this pass.** Every star channel was closed in this sandbox:
`api.github.com` 403, `github.com` HTML 403, `img.shields.io` blocked, `api.star-history.com`
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated across several industries**; carrying unverifiable numbers forward would
repeat that error. Licence, default ref and liveness **were** verified first-hand for all 58 live
addresses — see [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

**So:** rank by licence permissiveness, maintenance signal and fit. Popularity was never the
decision criterion for a studio engagement anyway.

🟢 🆕 `p387` **Partially closed — and by a channel, not by a workaround.** "Maintenance signal" was
the one criterion in that sentence this base could not actually measure. It can now: **package
registries publish dates**, and 26 education packages are dated in
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv). 🔴 **Still open:** repository
commit activity, contributor counts and issue latency (all behind `api.github.com`, 403), and the
many shelf entries that are **not published packages at all** — for those, publication is absent
rather than old, which is itself worth telling a client.

## Trend 9 — 🆕 `p384` The curriculum-data layer arrived, and its licence is a *database* licence

**Every adaptive-learning pitch rests on knowing what a learner must master before the next topic.
Until this pass, no shelf here held that artefact. Now one does — and it is not licensed like code.**

[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) `v1` publishes **1,930
micro-topics** and **4,102 prerequisite edges** as a DAG — each edge tagged `hard`/`soft` with a
one-line reason — over **9 subjects**, aligned to **NGSS, Common Core, the UK National Curriculum**
and the Australian curriculum. Its grant, read first-hand at `main/LICENSE` (25,289 B), is the
**Open Data Commons Open Database License (ODbL)**. There is **no separate code grant**.

**Why this is a trend and not just a row.** Every licence question these shelves have answered so
far was a **copyright** question about code: can we link to it, can we ship closed extensions. ODbL
is a **share-alike database right**, and it draws its line in a different place:

- **§4.3 — a *Produced Work*** (the tutor's output: a lesson plan, a next-topic choice, an
  explanation) needs **an attribution notice and nothing else**. 🟢 This is the permissive path.
- **§4.4 — a *Derivative Database*** (the client's topics merged in, standards remapped, the graph
  re-cut) must be publicly used **only** under ODbL, a later ODbL, or a compatible licence. §4.4(b)
  is explicit that extracting *"the whole or a Substantial part of the Contents into a new
  database"* **is** a Derivative Database. 🔴 This is the trap, and it is the thing a studio would
  naturally do next.

🔴 **A licence scanner pointed at code will not see this at all.** Neither will a licence badge:
ODbL is not in the permissive/copyleft taxonomy these shelves have been using, so the row cannot be
classified green or red — it is **green on one axis and red on the other, depending on what you
ship**. `Pattern L` was built for the case where a badge misreports a code grant; this is the case
where the *category* is wrong.

**So:** three concrete consequences.
1. **Ground on it, do not fork it.** Keep client curriculum data in a separate store joined at
   query time, so the taxonomy stays an **input** rather than a component of the deliverable. That
   is **Pattern H** in [`compose/patterns.md`](../compose/patterns.md).
2. **Add a data-rights question to intake.** Alongside "what licence is the code", ask "what rights
   govern the **data** we ground on". Education runs on standards, item banks and curriculum maps —
   this will not be the last ODbL/CC-BY-SA artefact on these shelves.
3. **Check coverage before promising it.** The maintainers state their own gap: teaching research
   covers **1,049** topics (Science and Mathematics) and **881 topics have none**. A
   research-backed-guidance claim is true for roughly half the graph.

## Trend 10 — 🆕 `p388` The parent is the unserved persona in education AI, and the statutes are pushing toward them

Every market map this base has built, and every roundup it has read, segments education AI into
**student-facing** and **teacher-facing** — `Trend 5` is about which of the two is growing faster.
Both categories are about people *inside* the institution. **The parent is outside it, and is the
person who actually logs into the portal.**

**The supply arrived this pass and it is not a prototype tier.**
[chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) (**MIT**, 20 tools
over **Infinite Campus / Campus Parent**, **47 published releases**) and
[chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) (**MIT**, 18 tools,
**43 releases**) are maintained, deliberately scoped to the observer surface, and built by one
maintainer working the same problem across two platforms — which is what a real need looks like
rather than a weekend demo.

**Three reasons this is a trend and not a curiosity:**

1. **The statutes are already there.** Every North American instrument this base tracks puts
   **family transparency** in the text — Oklahoma SB 1734 names it outright; Maryland's Chapter 634
   is built around guidance districts must hand down to families. Regulators keep asking
   institutions to *explain AI to parents*; nobody is building the surface that would.
2. **There is no incumbent to displace.** The parent portal is a **feature of the SIS**, not a
   market. No vendor defends it, and the SIS vendors have no incentive to open it. That is the rarest
   condition in education software, where every other surface has a 20-year incumbent.
3. **It inverts the tenancy problem instead of solving it.** `p386`'s finding — every granted LMS
   server authenticates as the signed-in user, so a studio cannot hand one to an institution — reads
   as a *defect* for student and teacher tools. For the parent it is **the correct architecture**:
   the parent's own credential, the parent's own child, no institutional tenancy required at all.

🔴 **And the boundary that defines the engagement, because it is not a licence boundary.** Hosted by a
family, these tools are a person exercising their own access. **Hosted by a studio for a district, the
identical API call becomes a FERPA-governed disclosure of an education record.** The code does not
change; the obligation does. 🔵 So the honest market shape is **two different products**: a
parent-side tool (no tenancy, no FERPA exposure, no institutional sale) and a district-side one (full
tenancy, full FERPA, a real procurement cycle). Conflating them is how this gets sold wrong.
`Pattern P` in [`compose/patterns.md`](../compose/patterns.md) is built on that split.

## Trend 11 — 🆕 `p388` Jurisdictional curriculum content is becoming the defensible layer, and it is arriving region by region

`Trend 9` recorded that a curriculum-data layer had arrived and that its licence was a **database**
licence. `p388` shows the *shape* that layer is taking, and it is not one global graph:

| region | asset | licence | what makes it local |
|---|---|---|---|
| **North America** | 🆕 [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 🟢 MIT | The **BC Ministry** K–12 curriculum in its real three-column **KDU** structure — and the **First Peoples Principles of Learning**, a provincial requirement no imported product carries |
| **LATAM** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) (`p387`) | 🟢 MIT | **BNCC** skill codes, Brazil's national curriculum, with invented codes discarded before a teacher sees them |
| **Global** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (`p384`) | 🟡 **ODbL** (database licence) | 1,590 topics / 3,221 prerequisite edges mapped to NGSS and Common Core |

**The pattern across the three:** the model is interchangeable, the *curriculum authority* is not.
A tutor that cites a BNCC code, a BC Big Idea or an NGSS standard is doing something a
general-purpose tutor **cannot** — not because its reasoning is better, but because it is anchored to
the instrument the jurisdiction grades against.

**Three consequences for an engagement:**

1. **Curriculum grounding is now demonstrable in three regions, not described in one.** `Pattern H`
   stops being a proposal and becomes a reference build with a local example in hand.
2. 🟡 **The risk on these assets is currency, not licence.** The BC server is 🟢 MIT — clean — but it
   is a **crawl** of `curriculum.gov.bc.ca`, last published **2026-03-27**. Curricula are revised on
   political timetables. **Quote the re-crawl as a maintenance line item**, and never let a client
   believe a crawl is a feed.
3. **Keep asking the data-rights question from `Trend 9`.** Two of the three assets above are code
   (MIT); one is a **database** under ODbL. "What licence is the code?" and "what rights govern the
   data we ground on?" remain two different intake questions with two different answers.

## Trend 12 — 🆕 `p388` An exhausted channel is not an exhausted supply — and "published but unreadable" is now a real category

This is a trend about **how this industry's open-source supply is actually distributed**, and it has
a direct procurement consequence.

**The discovery finding.** `p382` recorded that this industry's address supply was **exhausted**.
What was exhausted were four search-engine legs. **`registry.npmjs.org/-/v1/search` is open**, and 29
education queries returned **383 GitHub addresses absent from this entire base**, of which **22 are
granted and education-specific** — the largest single intake in this base's recorded history. 🔵 The
general lesson, and it is the third of its kind here: `p386` learned *a count of addresses is not a
count of grants*; `p387` learned *a null leg is not a null supply*; `p388` adds *an exhausted channel
is not an exhausted supply*. All three are one error — **a property of the instrument reported as a
property of the industry.**

🔵 **Why a package registry is structurally the better instrument for this industry.** A trending page
ranks by attention over days. Education tooling is **institutional, unglamorous and
low-star** — a 47-release parent-portal server for a US K-12 SIS will never trend anywhere. The
registry indexes it anyway, and returns its **entire publish history in the same call**, which
answers "is it maintained?" at the moment of discovery rather than two steps later.

🔴 **The new supply category, and it is the uncomfortable half.** Of 32 addresses probed, **6 publish
to npm from a repository that is not publicly readable** — `git ls-remote` prompts for credentials,
so the repository is **closed, not missing**. The package installs; the provenance cannot be audited.
The costliest instance is **103 published versions** of an AI-generation quiz library **with SCORM
support** ([thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)); the
most instructive is [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest
declares **`"SEE LICENSE IN LICENSE"` — pointing at a file inside a repository nobody can read.**

**So the licence-reading discipline this base built needs one more rule.** `Pattern L` clears a
repository by reading its **subtree**; for these there *is* no subtree. The rule that replaces it:
**for an npm-only dependency, the manifest is a claim and the tarball is the evidence** —
`registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves the published artefact even when the repository is
closed, and **it is the licence that actually ships**. 🔴 That is how this pass established that a
major publisher's tutoring SDK (**115 published versions**) carries **no licence at all**: not from
the repo, which is private, but from the artefact, which is not. 🔵 And the corollary a studio should
internalise: **commercial education vendors are starting to distribute as closed SaaS with an npm
veneer.** The npm scope looks like open source, installs like open source, and grants nothing.

🔵 🆕 `p391` **The channel now has a decay curve, not just a verdict.** Re-run with 32 queries of
*fresh* vocabulary (tenancy, SEN/IEP, proctoring, QTI, xAPI, OneRoster, FERPA, standards, personas):
**321** addresses absent from this base → 37 past a domain filter → 11 probed → **3 shelvable**.
That is **0.9%**, against `p388`'s **5.7%** (22 of 383). 🟢 The channel is **depleting, not
exhausted** — it still produced three rows, one of which opened a category (`Pattern W`). 🔴 But the
seam `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary.
🔴 **And the instrument nearly lied:** the first draft of the domain filter matched the query column
of its own output and "confirmed" 37 education rows that were Vercel, AWS and Storybook packages.
Caught before a shelf. *A filter that scores its own prompt is not a filter.*

## Trend 13 — 🆕 `p389` The supply has a currency problem, and it is now a number

This base has built a careful discipline about *licences* and almost none about *time*. `p387` and
`p388` both recorded that no maintenance signal was available. It was: **`git` read access is open to
every public repository**, and a blobless shallow clone returns the last commit date at the real
default ref in about a second. Sixty addresses were dated this pass.

**The distribution, which is the trend.** 58 live, 2 dead. **48 of 58 moved within 30 days**, and 17
of those were committed **on the day of the pass**. That is a healthier supply than this industry's
reputation suggests — education tooling is unglamorous, not abandoned. But **7 of 58 are past 120
days, and four of those seven carried a recommendation on these shelves**:

| stale address | days | what it was being recommended for |
|---|---|---|
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 343 | a Tier-1 tutor |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 242 | Moodle integration |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 209 | North American curriculum grounding |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 144 | Canvas integration — **and it is ungranted** |

🔵 **The general shape, and it is this base's fourth instance of one error.** `p386`: a count of
addresses is not a count of grants. `p387`: a null leg is not a null supply. `p388`: an exhausted
channel is not an exhausted supply. **`p389`: a closed popularity channel is not a closed maintenance
channel.** Four passes, one mistake — *a property of the instrument reported as a property of the
industry* — and each time the fix was to ask which channel was actually being measured.

🔴 **The procurement consequence, which outlives the instrument.** A licence tells you whether you
*may* build on something. A date tells you whether you will be **alone** on it. Those are different
risks and they price differently: an MIT repository that has not moved in eight months is a
**vendoring decision with a maintenance line in the estimate**, not an integration. Both numbers
belong in the same row of a proposal, and until this pass only one of them was here.

🟡 **And the limit, stated so the number is not over-read.** A commit date says someone pushed — not
to the branch a release is cut from, and not that the project is healthy.
[instructure/canvas-lms](https://github.com/instructure/canvas-lms) is the case in point: `master` is
175 days behind while its `stable/*` branches move, because that is how Instructure ships. A
specification or a dataset that is *finished* is not decaying either. Read the date against what the
artefact is.

## Trend 14 — 🆕 `p389` APAC has become the net exporter of open-source education AI, and the Gulf the net importer

**The supply side.** The largest education-native repository in open source is
[**OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, ~41.3k ★, from **Tsinghua
University**, committed the day of this pass, published in **JCST 2026** and validated inside the
university on **700+ students**. It is not an outlier in its region: the Tier-1 tutor shelf on
[`agents/top.md`](../agents/top.md) is now **majority APAC by origin** — DeepTutor (HKU, Apache-2.0),
ai-shifu (China, Apache-2.0), educhain (India, MIT), OpenTutor (China, MIT), Aha Tutor (China, MIT),
learn-shell (China), ChatTutor (APAC) — against one EMEA entry (mentingo, Poland) and, at Tier 1, one
North American (tutor-gpt, now 343 days stale). 🔵 **The pattern is not "China ships a lot of AI."**
It is that **the pedagogy is being designed in the repository** — mastery estimates that record
*confidence* separately from correctness, FSRS review built in, cognitive-load detection,
misconception-aware branching — in projects whose authors are university teaching groups rather than
startups. That is a supply a studio can build a practice on, and its licences are permissive.

**The demand side, created by statute rather than by procurement.** The **UAE** approved an AI
curriculum across **all public and private schools** by Cabinet decision in September 2026, with
**22,000 teachers and education professionals** to be trained, and for 2026-27 merged Design,
Innovation and Computer Science into a single subject, *Artificial Intelligence and Technology*,
KG–Grade 12. **Saudi Arabia** began a comprehensive AI curriculum across all levels of public
education in the 2025-26 academic year, led by the **National Curriculum Center** with **SDAIA**.
These are the most aggressive AI-in-education mandates anywhere: not permission to pilot, a
**compulsory subject with a teacher-training number attached**.

🔴 **And the mismatch is the opportunity.** This pass found **no Gulf-origin and no Arabic-first
open-source education agent or platform** — not one address. The region with the world's strongest
statutory demand for AI teaching material has, as far as this base can see, **no local open-source
supply at all**, while the permissive supply that does exist is EN + zh-CN. The gap is not a model
gap; it is **curriculum-grounding and language**: Arabic-first content, alignment to the UAE MoE's
seven curriculum areas, and the teacher-training surface those 22,000 professionals will be trained
on. 🟡 Recorded as an informed gap, not a finding: the searches run were English-language, and an
Arabic-language search is the obvious next leg.

## Trend 15 — 🆕 `p389` The parent surface now has a cautionary case, and it is in LATAM

`p388` added the parent/guardian persona and named **FERPA** as the line that splits a family-run
assistant from a district-hosted one. The LATAM equivalent of that line is **LGPD Article 14**, and
unlike FERPA it already has a public failure attached to it.

- **Brazil has no AI statute in force.** As of October 2026 **PL 2338/2023** — passed by the Senate
  in December 2024 — is still in the Câmara dos Deputados, with reports that the vote resumes after
  the October 2026 elections. So the binding instrument for an education engagement today is the
  **LGPD**, not an AI law.
- **Children's data has its own consent basis.** For core teaching a school generally relies on
  contract and legal obligation, but uses **beyond** that — images, communications, extracurricular
  activity — require **specific, explicit, recorded and revocable consent from a parent or guardian**
  under Art. 14. An AI parent portal is squarely in the "beyond" category.
- **The cautionary case.** In 2023 the São Paulo state education department (**SEDUC**) had its
  *Minha Escola* app installed on parents' phones without notice or consent; Data Privacy Brasil
  assessed it as a probable LGPD violation. 🔵 **This is the precise failure mode of the persona
  `p388` added** — a district-hosted parent surface deployed *to* families rather than *for* them —
  and it is the reference a LATAM client will have in mind, so bring it up first.

🟢 **What this makes defensible rather than risky.** The pattern that survives Art. 14 is the one
`Pattern P-1` already describes: the **family runs the agent and exercises its own access right**, so
no new disclosure is created. For the district-hosted variant (`P-2`), the deliverable a Brazilian
client should be sold is the **consent and revocation mechanism itself** — per-guardian, recorded,
revocable, auditable — as a first-class feature, not a checkbox. 🟡 **Mexico: informed gap.** No
education-specific AI guidance or student-data rule was found for Mexico in this pass; the general
position is a data-protection regime and no AI statute. Stated, not inferred.

## Trend 16 — 🆕 `p390` The copyleft firewall moved inside the platform, and it is a packaging decision rather than a licensing one

For several passes this shelf framed "permissive agent + copyleft platform" as a problem solved at
the **boundary**: hold the agent outside the LMS and talk to it over LTI or MCP, so no copyleft
reaches your code. That is still a valid pattern, but `p390` found the cleaner answer was in the
platforms' own packaging the whole time, and **nobody had read it per-package**:

| package | role | licence |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | the platform you deploy | 🔴 **AGPL-3.0** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | the component API your plugin imports | 🟢 **Apache-2.0** |
| [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | what you develop against | 🟢 **Apache-2.0** |
| [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) | newer core data layer | 🔴 **AGPL-3.0** |

All four read from the payload at their real default ref on **2026-10-22**; the two Apache grants are
at `LICENSE.TXT`, which is also why a badge-level or root-`LICENSE` read misses them.

**Why this is a trend and not a trivium.** It means the in-platform plugin — the deepest, most
useful integration, with full access to course state and no network hop — is **also** the one that
can stay MIT or proprietary. The industry had been treating depth of integration and licence freedom
as a trade-off, and for Open edX specifically they are not. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(MIT, Universidad Tecnológica de Pereira) has been shipping on exactly this basis.

🔴 **The trend has a sharp edge: the boundary is per-package, and it is moving.** `openedx-learning`
is the newer core data layer and it is **AGPL-3.0**. As more platform functionality migrates there,
the set of imports that keeps a plugin permissive **shrinks**. Audit the dependency list in CI, not
once at kick-off. The general rule this generalises to: **licence is a property of the package you
import, not of the organisation that publishes it** — and in education, where every major platform is
copyleft, that distinction is worth real money.

## Trend 17 — 🆕 `p390` Voice is the next interface gap, and the open-source supply has not arrived

Across seven passes these shelves accumulated tutors, graders, LMS connectors, parent portals and a
generated classroom. **Every one of them is text-first.** `p390` found exactly **one** granted
voice-first education agent in the open-source supply — [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
(MIT, Brazil, pt-BR, 15 days old, self-described as *"in development"* with no public deployment).

**Why the gap matters commercially.** Voice is not a convenience feature in this industry; it is an
access feature, and it maps onto precisely the markets with the fastest growth and the least supply:

- **Early grades**, where reading and typing fluency is the thing being taught, not assumed.
- **Shared-device and phone-only households** — the LATAM and APAC reality `Trend 10` documents.
- **Language learning**, where pronunciation *is* the assessed skill and text cannot carry it.
- **Accessibility**, which in EMEA public procurement is frequently a scored requirement rather
  than a nice-to-have.

**Why the gap is narrow rather than deep, which is the opportunity.** The hard parts are already
permissive and maintained: [`livekit/agents`](https://github.com/livekit/agents) (Apache-2.0) solves
turn detection, interruption and barge-in — the things that actually make a spoken tutor usable — and
[`mozilla/common-voice`](https://github.com/mozilla/common-voice) supplies **CC0-1.0** speech corpora
across ~130 language variants for ASR evaluation and fine-tuning. What is missing is not
infrastructure; it is **an education-grade assembly of it** — mastery model in the loop, symbolic
checking behind the arithmetic, and the biometric/disclosure posture a school can sign.
🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md) is that assembly.

🔴 **`Gap 390-A` — the informed gap, stated rather than left as silence.** The searches this pass ran
for an open-source voice or multilingual tutor in an **African or South Asian language** returned
**nothing granted and maintained**. What came back instead: one India-first multilingual *toolkit*
(not a tutor), an arXiv framework for low-cost home language learning with **no public code located**,
and a repository that teaches *Spanish to non-speakers* inside an agent CLI — which is the inverse of
a Spanish-language tutor for Spanish-speaking learners, a category error this base recorded in `p388`
and which keeps recurring in search results. 🔵 **Read this as a null result in the open-source
supply, not a null in demand** — Africa is among the fastest-growing online-education markets. For a
client engagement in those languages the honest position is: **the substrate is permissive and ready,
the localised tutor does not exist and would be built, and Common Voice is where its evaluation set
comes from.**


## Trend 18 — 🆕 `p391` Education AI is shipping as **harness extensions**, not standalone applications

Three of this base's education rows are now plugins to the *same* agent harness, by **three
unrelated maintainers**, all MIT, all published inside about ten days:

| row | what it is | published |
|---|---|---|
| [`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (`p388`, Tier 1) | narrated-blackboard adaptive tutor | npm v1.7.0, 2026-10-22 |
| [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🆕 `p391`, Tier 1) | diagnosis-first learning runtime | npm v0.1.1, 2026-10-17 |
| [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (🆕 `p391`) | K8s + OIDC multi-tenant hosting for the same harness | npm v0.10.0-rc.1, 2026-10-12 |

They are extensions to **DeepSeek Harness**, and the pattern is not harness-specific — this pass also
read [`mackt/pi-language-tutor`](https://github.com/mackt/pi-language-tutor) (MIT) as an extension to
the Pi agent. 🟢 **Why it is a trend and not a coincidence:** a harness extension inherits model
plumbing, tool calling, auth, UI shell and a distribution channel for free, so a single maintainer can
ship a credible tutor in weeks. The economics now favour the plugin over the application.

🔵 **The operational consequence, and it explains a channel result this base has hit repeatedly.** The
distribution channel for education AI is becoming **the agent harness's package registry** — which is
why `registry.npmjs.org` keeps yielding education supply while `moodle.org` has never once been
reachable *or* necessary. Looking for education AI in LMS plugin directories is looking where it was
built in 2019.

🔴 **The cost a studio inherits, stated plainly.** A harness extension is **not deployable without its
harness**. `dsh-diagnostic-tutor` requires DeepSeek Harness; adopting it means adopting that runtime,
its update cadence and its governance. For a client who cannot, the move is to copy the *structure*
(see `Pattern X`) rather than the package — which is exactly why `Pattern X` separates the pedagogy
from the runtime instead of recommending the repository wholesale.

## Trend 19 — 🆕 `p391` The standards body's reference implementation goes stale; the **vendor fork** carries the maintenance

`p390` dated [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) at 2,332
days and concluded the LTI 1.3 integration path had no installable implementation. The grant and the
dating were both right; the conclusion was wrong, because the maintained line is not at the
authoritative-looking address:

| address | last commit | registry | verdict |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **2026-10-16** | packagist `lti-1p3-tool` **v6.4.4**, 68 versions, 2026-09-23 | 🟢 **install this** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Node) | **2026-10-13** | npm `ltijs` **v7.0.7**, 207 versions, 2026-10-06 | 🟢 **install this** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 2020-06-03 | — | 🔴 spec citation only |
| [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) | 2020-06-03, **identical sha `3a192de`** | — | 🔴 the same project, renamed org |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) | 2022-11-21 | PyPI `PyLTI1p3` 2.0.0, **2022-11-20** | 🔴 genuinely dead |

🟢 **The generalisable rule:** in standards-driven education interop, the consortium publishes the
spec and a demonstration; a **vendor with production traffic** maintains the library. So when a
reference implementation dates badly, the next question is *who ships this in production* — not
*should we vendor the spec*. Check the fork network and the package registry before concluding a path
is closed.

🔴 🆕 `p392` **The "language asymmetry" half of this trend is WITHDRAWN, and withdrawing it sharpens
the rule above rather than weakening it.** `p391` closed this trend with: *"Node and PHP have
maintained LTI 1.3; Python does not… the interop edge is therefore a separate Node or PHP service in
front of the agent."* Read first-hand this pass, **Python has three**:

| address | grant | last commit | registry | role |
|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | **2026-10-20 — 2 d** | PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07 | 🟢 **in-process**, Django app + middleware |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 — 113 d | PyPI **v1.6.3**, 15 releases | 🟢 LTI 1.1 **and** 1.3 into JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | **2026-10-22 — 0 d** | PyPI `lti-consumer-xblock` **v11.4.2** | 🔴 best-maintained of the three, **copyleft** |

🟢 **And the maintainer pattern holds in Python too, which is the trend's real content.** The three
Python implementations are maintained by a **university innovation centre** (Michigan), an
**ecosystem project** (Jupyter) and a **platform vendor** (Open edX) — not by the standards body. The
rule is unchanged and now has six instances instead of four: *in standards-driven education interop,
ask who ships this in production.*

🔴 **What survives as a constraint is licence-shaped, not language-shaped**, and that is a more useful
thing to tell a client: the best-maintained Python LTI implementation is **AGPL-3.0**, the
best-maintained Node one is Apache-2.0, and the permissive Python options are smaller (26 ★ and 73 ★)
and framework-bound. The question is never *"does this language have LTI"* but *"does the maintained
implementation in my language carry a grant I can ship?"* `Gap 391-A` **CLOSED**.

## Trend 20 — 🆕 `p392` The granted proctoring supply covers the **lockdown**, not the **inference** — which is the opposite of the regulatory exposure

For four passes this base recorded proctoring as having *"no credible permissive open-source option"*
and treated that as a liability boundary to name rather than fill. Probed first-hand, the supply
exists — and its **shape** is the trend:

| component | grant | last commit | what it actually does | the AI part |
|---|---|---|---|---|
| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) | 🟢 **MIT** (1,069 B, manifest agrees) | **2026-09-28** | tab-switch, right-click, DevTools shortcuts, clipboard events, camera state, **faces**, audio loudness, **virtual-camera / loopback / screen-share detection** | 🟢 **real** — face-api on TF.js, **in the browser** |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 🔴 **CONFLICT** — Apache-2.0 payload, `ISC` manifest **and** npm | **2026-10-13**, 398 commits | blocks copy/paste/cut, right-click, selection, shortcuts; detects `tabSwitch`, `browserBlur`, `exitTab`, `fullScreen`; periodic page and webcam snapshots POSTed to an endpoint you build | 🔴 **absent** — object detection, multi-face and eye tracking are marked *"(To be Done)"* |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🔴 **AGPL-3.0** | 🆕 re-read `p392`: `master` HEAD **2026-10-22 — 0 d** (this base's harvest row said 2026-05-30; the live read is today), 253 releases | the exam **workflow** — attempts, review states, integration points | 🔴 none; it brokers a vendor |

🔵 **The asymmetry, stated as a rule:** open-source proctoring is **deterministic browser lockdown and
event telemetry**, while the **inference** — identity, gaze, multiple faces, behavioural scoring — is
either absent, roadmapped, or the proprietary service the AGPL workflow brokers. 🟢 **And the
regulatory exposure runs the other way.** Lockdown and event logs do no biometric inference: they
are not what the EU AI Act's Annex III is reaching for, and they are explainable to a student
(*"you left fullscreen at 14:03"*). The inference layer is where high-risk obligations, biometric
rules and the whole evidentiary argument live — and that is exactly the layer the permissive supply
does not have.

🟢 **So the honest advice to a client flips, and it is now sellable in both directions:** *we can
build the integrity layer you can defend — lockdown, event trail, human review — permissively and
today; the part that would flag a student automatically is the part that makes you a deployer of a
high-risk system, and neither of us should want it in v1.* 🔴 The obligation attaches to the
**deployment**, not the dependency, so an open-source grant transfers no compliance relief whatsoever.

## Trend 21 — 🆕 `p392` LATAM's public buyers are procuring AI education platforms as **subscriptions**, and no tender asks for open source

A replacement regional leg shaped like a **buyer** rather than a supplier — public-procurement
vocabulary in Spanish and Portuguese — returned five live 2026 instruments where three passes of
English, stars-sorted supply legs returned nothing: Santa Fe province (Argentina, Tender 01/26,
*subscriptions* to AI-enhanced educational cloud platforms), **OEI-Chile `OEI-LIC-1-25`** (design and
build of an AI platform for **administrative management in Chilean schools** over regulatory,
financial and operational data), UNOPS Argentina `ITB/2026/62779` (educational platform **licences**,
2+2 years), the **CIEDEPAR** consortium in Paraná (multi-municipality SaaS education management) and
Francisco Morato, SP (**R$1,924,665.00**).

🔴 **Not one of the five specifies free or open-source software.** The spend is real, the AI framing
is explicit, and the procurement shape is **product subscription**.

🔵 **Why this is a trend and not five anecdotes:** it is the demand-side mirror of *Trend 6*. This
base's whole thesis is permissive assembly, and the buyers writing the cheques are specifying
subscriptions — so the binding constraint on an open-source education engagement in LATAM is **the
specification, not the licence frontier**. 🟢 The opening is a total-cost bid against subscription
pricing, with the OEI-Chile scope (administrative management, compliance recommendations) matching the
`i-educar` + agent shape these shelves already hold; the work is to get *"or equivalent open-source
implementation"* into a specification written for a product. 🟡 Graded **`ATTRIBUTED-UNVERIFIED`** —
aggregators and news items; no official portal (COMPR.AR, ChileCompra, PNCP) is reachable here.


## Trend 22 — 🆕 `p393` The education **interoperability layer is Python** while the agent layer is TypeScript, and a one-registry sweep answers half the question

**What was measured.** `p393` opened the channel `Gap 392-C` said did not exist: `pypi.org/simple/`
under PEP 691 returns **920,784 project names in 45,189,043 B in 1.4 seconds**, unauthenticated. A
sweep of 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, 13 live and
verified first-hand.

**What came back was a layer, not a list.** Not more tutors or more agents — **plumbing**:

| standard / surface | granted Python supply found | grant |
|---|---|---|
| **LTI 1.3 / Advantage** | `openfun/django-lti-toolbox` (France Université Numérique), `Harvard-University-iCommons/django-lti-dynamic-registration` | 🟢 MIT, 🟢 MIT |
| **QTI** (assessment exchange) | `vosslab/qti_package_maker`, `Citolab/qti-convert-python` (Cito, NL) | 🟡 LGPL-3.0, 🔴 GPL-3.0 |
| **OneRoster / Caliper** | the `timeback-*` family — 🔴 **source unresolvable** | 🔴 unauditable |
| **Ed-Fi** (US K-12 data) | `edanalytics/edfi_api_client`; `Ed-Fi-Exchange-OSS/LMS-Toolkit` 🔴 archived | 🟢 Apache-2.0 ×2 |
| **LMS → agent bridge** | `Dathis/swiss-moodle-mcp`, `Snaw80/moodle-mcp` | 🟢 MIT ×2 |
| **Autograding** | `edulinq/autograder-py`; `otter-grader` already carried, now measured at **161 ★** | 🟢 MIT, 🟢 BSD-3 |

🔵 **Why this is a trend and not a haul.** The split is systematic. The **agent** layer — MCP servers
for Canvas, tutors, parent agents — is overwhelmingly **npm/TypeScript**, which is why eleven passes of
npm sweeps built a rich agent shelf. The **standards and institutional-data** layer is
**PyPI/Python**, because it lives next to the Django and Flask applications that universities and
ministries actually run (Open edX, `now-lms`, campus SIS integrations) and next to the
notebook-and-grading stack. 🔴 **A supply claim is therefore only as wide as its registry.** This base
published *"there is no maintained Python LTI 1.3 library"* (`Gap 391-A`) from a channel that
**cannot index PyPI** — and then found five.

🟢 **The rule for a studio:** one discovery channel per ecosystem, named before any absence is
published. This base's set is now npm + PyPI + Packagist (measured, 0 yield) + `git ls-remote` and
`raw.githubusercontent.com` for verification. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** —
and CRAN matters here, because `otter-grader` grades **R** and the statistics-teaching stack is
R-shaped.

🔴 **The cost of the channel, stated with it:** the dump carries **names only**, so it discovers by
token and a token is not a capability. Two of fifteen candidates were pure collisions — `proctor-ai`
is a **prompt-engineering** library, `xapi-python` is the **xStation5 broker API** — and whole keys are
unusable (`canvas` returns 146 names dominated by HTML-canvas and AWS Nova Canvas; `d2l` is
Dive-into-Deep-Learning). Discovery is cheap; **adjudication is the work**.

## Trend 23 — 🆕 `p393` A new supply class: **live releases, dead source** — and the licence claim is unauditable in principle

**The instances, found the same hour.** [`superbuilders/timeback-dev-python`](https://github.com/superbuilders/timeback-dev-python)
is the declared `Repository` of **three** actively-released PyPI packages — `timeback-qti`,
`timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last
**2026-07-18**, each declaring **MIT**, together the most complete 1EdTech client family in Python on
paper. 🔴 **The repository does not resolve for an unauthenticated clone.** Second instance:
`moodle-mcp-bridge` v1.7.0, advertising *"a Moodle site as 88 typed AI tools"* → `NmaaAlhawary/MCP-Moodle`,
also unresolvable.

🔵 **Why this is a distinct class and not a variant of an existing one.** This base already grades
three failure modes, and none of them covers this:

| class | the payload | the verdict |
|---|---|---|
| `UNGRANTED` (no licence file) | exists, is empty of a grant | read, and found wanting |
| `README-ONLY` / `MANIFEST-ONLY` | a grant **asserted** somewhere other than a payload | downgraded, because the assertion is checkable against the absence |
| 🆕 **`LIVE-RELEASES-DEAD-SOURCE`** | 🔴 **cannot be fetched at all** | **not assessable** — there is nothing to read, and no amount of care fixes it |

🔴 **The procurement consequence is sharper than it looks.** `p388`'s *"published but unreadable"* was
about a payload that says nothing; this is about a payload that **cannot be obtained**. A studio can
install these packages — pip will resolve them happily — but it **cannot warrant the licence to a
client**, because warranting a grant means having read it. And an MIT declaration in registry metadata
is a claim by the uploader, not a grant in a distributable artefact.

🟢 **What to do with it.** Evaluate in a sandbox if the capability is needed; **never ship it into a
client deliverable**; ask the publisher to open the repository, which is a cheap request and a fair
one. 🔵 And record the class, because the economics favour its growth: publishing to a registry is
free and keeping a public repository is a maintenance commitment, so **more supply will arrive this
shape**, not less.

## Trend 24 — 🆕 `p394` In the teaching stack the **delivery** layer is permissive and the **measurement** layer is copyleft, and a language boundary rides along with it

🟢 **The observation.** `p394` opened the R half of the CS-teaching stack and the licence column split
cleanly down the middle of the pedagogy:

| what it does | components | licence |
|---|---|---|
| **Deliver** the teaching loop — present, accept, grade, respond | `rstudio/gradethis` (**MIT**, 164 ★), `rstudio/learnr` (**Apache-2.0**, 738 ★), `ucbds-infra/ottr` (**BSD-3-Clause**) | 🟢 **permissive, all three** |
| **Measure** the learner — item response theory, adaptive item selection, exam generation, item analysis | `cran/exams` (**GPL-2 \| GPL-3**), `philchalmers/mirt` (**GPL >= 3**), `cran/catR` (**GPL >= 3**), `cran/TAM` (**GPL >= 2**), `ShinyItemAnalysis` (**GPL-3**) | 🔴 **copyleft, all five** |

🔵 **Why it is not a coincidence.** The delivery components are **vendor-authored** — Posit, a company
selling an R platform, and a university programme that needed its autograder to be adoptable. The
measurement components are **academic instruments**, written by psychometricians inside a GPL research
culture and in some cases decades old. **The licence tracks who paid for the code and why**, and it has
produced a split running exactly along the boundary between *product* and *science*.

🟢 **Why that is good news rather than a blocker.** The boundary falls where a studio's product
boundary has to fall anyway: own the teaching loop, reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. 🔴 **The
trap is reading it as a licence problem and swapping in a permissive psychometrics library instead.**
There is no credible permissive equivalent of `mirt` or `catR`; building one is a multi-year research
project and approximating one is how a studio ends up shipping an adaptive engine whose claims it
cannot defend. 🔵 This base already carries the symptom: `adaptive-knowledge-graph` (~350 ★) and
`OATutor` implement IRT and BKT from scratch, and `mirt` — **235 ★, committed daily** — is the thing
they are approximating.

🔵 **And the language boundary rides along with it.** `Trend 22` recorded that the agent layer is
npm/TypeScript while the standards layer is PyPI/Python. `p394` adds that the **measurement** layer is
**CRAN/R**. Three layers, three registries — and a supply claim is still only as wide as the registry
it was swept from. 🔴 **R is the worst case of the three**, because its registry is unreachable here on
**both** tools and its grants are invisible to GitHub's licence sidebar (`Gap 394-B`): five granted GPL
packages in this tier show **no licence** in the GitHub UI, because the grant lives only in
`DESCRIPTION`. **So a GitHub-UI-driven sweep does not merely under-count R supply — it reports it as
unlicensed.**

## Trend 25 — 🆕 `p394` A string matched as though it were a meaning is this base's most productive error class, and it runs in three directions

🟢 **The observation, as a count rather than an impression.** Three independently-found defects, three
different instruments, one mechanism:

| gap | instrument | direction | what the string was |
|---|---|---|---|
| `Gap 392-A` | capability-absence gate | 🔴 **over-refutes** — denies a real absence | a runtime key read as a capability |
| `Gap 393-A` | PyPI index channel | 🔴 **over-discovers** — invents supply | a package *name* read as a capability (`proctor-ai`, `xapi-python`, `canvas`, `d2l`) |
| **`P459`** 🆕 | `licence-grant-gate` | 🔴 **strips a grant** — denies a real permission | **"all rights reserved"**, line 2 of the canonical BSD template, read as a refusal |

🔵 **`P459` is the most expensive of the three and it was the last to be found**, because the other two
produce *visible* nonsense — a claim you can check, a candidate you can reject — whereas this one
produces a **false absence of a grant**, which looks exactly like diligence. A usable component is
quietly marked unshippable and nobody re-opens the question. 🟢 On these shelves its realised damage
was **nil** — no published row was graded from an untitled BSD payload, checked rather than assumed —
and its exposure was **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells.

🔴 **And the fourth instance is on this base's own shelf rather than in an instrument.**
`anastasasenov/bbmcps` sat in the Blackboard census for eight passes because its URL scheme reads
`blackboard://`. It is a shared-memory MCP server; the word is an **architectural metaphor**. So the
class does not only mis-discover and mis-refute — **it mis-files what the base already owns**, and a
census cell inherited as a count is exactly where it hides.

🟢 **The transferable rule, and it is cheap.** Before a token decides a verdict, ask what else that
token means. The gate that got this wrong already holds the right idea one screen away:
`AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`, with a comment noting each is simultaneously a
licence name and something else. 🔵 **The insight was applied to licence names and never to licence
clause text, nor to package names, nor to URL schemes.** One lexicon separating a **string** from a
**capability** would close `Gap 392-A`, `Gap 393-A` and the `bbmcps` class together — which is why
`p393` ranked that unification fifth and why `p394` ranks it **first**.
