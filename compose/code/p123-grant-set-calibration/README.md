# `p123-grant-set-calibration` — ACTION W, X, Y, Z, and V implemented

**Pass 123 — 2026-10-11.** Tenth pass of this date (census window **08:4x → 09:4x UTC**).

`./test_p123.sh` — **35 passed / 0 failed**, fully offline, no network and no clock.

## What p122 pre-registered, and what happened

| action | clause (verbatim from p122) | verdict |
|---|---|---|
| `ACTION W` | calibrate every census against rows known to be CORRECT and publish the false-positive rate beside the defect count. *Refuted if no existing instrument's rate exceeds 20 %* | 🟢 **DISCHARGED, NOT REFUTED — the one-token model's rate is 68 %** |
| `ACTION X` | verify the remaining prose candidates, tables included, with a multi-file grant reader. *Refuted if fewer than 5 survive verification* | 🔴 **DISCHARGED and REFUTED — 2 survived of 41 read by hand** |
| `ACTION Y` | replace every guessed branch with `resolve_head.sh` and re-probe the `NO-FILE` addresses. *Refuted if fewer than 3 do not exist* | 🟢 **DISCHARGED, NOT REFUTED — 18 genuinely absent** |
| `ACTION Z` | record a grant as a SET of (path → token) pairs; read `LICENSE-CODE`, `LICENSE-DOCS`, `LICENSE-DADOS`, `DESCRIPTION`. *Refuted if fewer than 8 addresses carry more than one grant file* | 🟢 **DISCHARGED, NOT REFUTED — 17 addresses** |
| `ACTION V` | emit `<!--corrected-->` on repaired rows instead of teaching the guard new vocabulary | 🟢 **IMPLEMENTED — 51 rows across 6 files, idempotent** |

## 🔴 `P123-H` — the three improvements cut the candidate count and did NOT cut the error rate

This is the pass's main result and it is stated first, because it is the one a reader should
carry forward.

p123 changed three things that p122 identified as the causes of its 95 % false-positive rate:
the grant became a SET rather than one token (`ACTION Z`), attribution became ROW-scoped inside
tables rather than paragraph-scoped (`P123-C`), and the correction guard became an exact marker
rather than a vocabulary (`ACTION V`). All three work, and they are measurable:

| | raw candidates | high-consequence subset | survived |
|---|---|---|---|
| p122 model — paragraph scope, vocabulary guard, one token | **576** | 72 | — |
| p123 model — row scope, exact marker, grant SET | **359** | **41** | **2** |

🔴 **And yet the false-positive rate is unchanged: 39 of 41 high-consequence candidates are
false, 95.1 %, against p122's 95 %.** Cutting the candidate count by 38 % bought no accuracy at
all. 🟢 **The reason is worth more than the instrument: the residual false positives are not
errors in this KB — they are this KB's correction apparatus working correctly.** Its audit tables
carry the OLD and the NEW licence in adjacent columns on purpose:

```
| [`fwu-de/ais-chat`](…) | 🟢 MIT | 🔴 **AGPL-3.0** | network-use copyleft |
```

A census that reads a row and finds `MIT` has found a column heading's worth of meaning, not a
claim. 🔵 **So the ceiling on this whole family of instruments is not attribution or path
coverage. It is that a correction record and a claim are the same bytes, and only the column
they sit in tells them apart.** `ACTION V`'s marker solves this for ONE of the three forms this
KB uses; `ACTION AB` below covers the other two.

## 🟢 `ACTION W` — the calibration, and why the gold label is not circular

The gold label does not come from the instrument under test and does not come from prose. A
claim is GOLD-CORRECT when the live tree grants that licence in SOME grant file, established by
reading EVERY grant file (`ACTION Z`) on the repository's REAL default branch (`ACTION Y`). The
model under test then reads only PART of that same evidence, so the calibration measures exactly
one thing: what the narrower model loses.

The gold set is restricted to the **25** rows where the models CAN disagree — addresses carrying
more than one grant file, or one file that is itself a split grant. On a repository with a single
plain `LICENSE` both models read the same bytes and agree trivially; including those rows would
pad the denominator and flatter the narrower model.

| model | false positives on gold-correct rows | rate |
|---|---|---|
| **ONE-TOKEN** (the p114–p122 model: first matching path wins) | **17 / 25** | 🔴 **68.0 %** |
| **MAIN-ONLY** (the pre-p122 branch guess) | 0 / 25 | 🟢 0.0 % |
| **GRANT-SET** (p123) | 0 / 25 | 🟢 0.0 % — by construction |

🟢 **`MAIN-ONLY` scoring 0 % is reported rather than smoothed**: all 25 gold rows happen to sit
on `main` or `master` defaults, so this gold set cannot see the branch defect even though
`ACTION Y` proves it is real on 77 other addresses. 🔵 **A calibration set is only as good as the
disagreements it contains, and saying so is part of publishing the rate.**

What the one-token model would have flagged as defects, all of them correct:

| address | the page says | one-token read | the tree |
|---|---|---|---|
| [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs) | Apache-2.0 | MIT | `LICENSE-APACHE` **and** `LICENSE-MIT` — dual, the user chooses |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | MIT | CC | `LICENSE-CODE`=MIT, `LICENSE`=CC |
| [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) | MIT | CC-BY-NC-SA-4.0 | `LICENSE-CODE`=MIT, `LICENSE`=CC-BY-NC-SA data |
| [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | MIT | STUB | `LICENSE` is a stub, `DESCRIPTION`=MIT, `LICENSE.md`=MIT |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | MIT · CC BY 4.0 · CC BY-NC-SA | one arm | a **three-arm** split, all three claims correct |

## 🔴 `ACTION X` — REFUTED on 2 survivors, and both are the same repository

41 high-consequence candidates were read by hand: 32 where the page claims a MORE permissive
licence than the tree grants (the direction that creates legal exposure) and 9 in the
over-restriction direction `P121-C` opened. **Two survived**, and the clause required five.

🔴 **`P123-A` — both survivors are `xiaochong0302/course-tencent-cloud` (1 173★, GPL-2.0), and
both are on `intel/market.md`, the page that ANNOUNCES the repair.** p121 repaired this address
and called it *"the largest-star licence defect of the pass"*. That announcement is at line 5500.
Two cells on the same page were never repaired:

| line | what it said | why it matters |
|---|---|---|
| 1761 | *"(MIT, fresh 1 d — a complete course platform…)"* | a plain live claim, no marker, no hedge |
| 5585 | *"(MIT, 1 173★ 🇨🇳 — **the only permissive full MOOC platform on the shelf**)"* | 🔴 the stale token carries a **load-bearing conclusion**: a studio reading this picks GPL-2.0 code believing it is the one permissive option |

🟢 **Both repaired this pass, with the `ACTION V` marker.** 🔵 **The generalisable point is about
where a repair stops: p121 fixed the row it found the defect in, and the prose that CITED that
row kept the old value. A repair has to be a search, not an edit.**

The other 39 fall into four classes, none of them KB errors:

| class | n | example |
|---|---|---|
| audit table — OLD and NEW in adjacent columns | 21 | `agents/top.md:451` |
| prose correction without the `ACTION V` marker shape | 9 | *"was 🟢 Apache-2.0 in this page's…"*, *"(⚠️ was MIT)"* |
| the page is MORE precise than the census | 6 | *"MIT badges over a 404"*; `classroomio` AGPL core + MIT `mcp` package |
| my own classifier under-read a split grant | 3 | see `P123-B` |

## 🔴 `P123-B` — p123's instrument carries the defect p123 was built to remove

[`Elgg/Elgg`](https://github.com/Elgg/Elgg) (1 677★) serves one `LICENSE.txt` on default branch
`7.x` that opens: *"Bundled plugins (the contents of the `/mod` directory) are available only
under the GPLv2 license. The remainder of the project is…"*. That is a split grant stated in
prose, and **none of my `SPLIT_MARKERS` match it**, so the classifier reduced it to a single
`MIT` — then flagged this KB's three Elgg rows, which already read *"🟡 **GPL-2.0 + MIT**
(bundled plugins MIT)"*, as over-restriction defects.

🔴 **So p123 reproduced p122's exact structural finding inside p123's own code: the page was more
precise than the census that audited it.** 🟢 **`ACTION AA` follows, and it is deliberately
narrow: detect the split by its SHAPE — a path-scoping noun phrase followed by two licence
tokens — rather than by adding a phrase to a marker list that the next repository will not use.**

## 🟢 `ACTION Y` — 18 genuinely absent, and a non-existence count that was 68 % noise

`resolve_head.sh` is now the only branch source. p122's 56-address `NO-FILE` list was not
committed, so p123 re-derived the population from the live pages: **1 365 folded addresses, 1 327
EXISTS, 38 ABSENT**, each ABSENT confirmed on **three** independent probes with zero flips.

🔴 **But 38 is not the finding, because 20 of them are not repository addresses at all:**

| kind | n | what they are |
|---|---|---|
| URL-path artefacts | **14** | `topics/ai-tutor`, `trending/python`, `search/repositories`, `orgs/opetushallitus` — the extraction regex reading `github.com/topics/…` as an owner/repo |
| this KB's own negative controls | **6** | `openedx/fake-repo-zzz999`, `owner/repo`, `your-username/safetutors` |
| 🟢 **genuinely absent** | **18** | the finding |

🟢 **Of the 18, exactly ONE appears on a live content page — and it is already recorded as
*"does not resolve"*.** The other 17 appear only in the append-only trending history, which is
not rewritten. 🔵 **So the live pages carry zero false existence claims, which is the opposite of
what a raw count of 38 would have suggested, and `NOT_A_REPO` filtering is now part of the
extractor.**

Several of the 18 are p122's `P122-G` class recurring — an address assembled from a product
NAME: `yetanalytics/lrspipe` (the product is LRSPipe; the repository is
[`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe), verified Apache-2.0),
`imsglobal/caliper-python` (1EdTech renamed), `1edtech/caliper-{java,js,php}`.

## 🟢 `ACTION Z` — 17 addresses, and the branch was the bigger defect

**17 of 1 096 addresses with a readable grant carry more than one grant file** — 11 with two, 6
with three. The clause needed 8. They are not a long tail of noise; they are five recognisable
conventions, and each has a different legal meaning from any single arm:

| convention | n | addresses | why one token is wrong |
|---|---|---|---|
| R/CRAN: stub `LICENSE` + grant in `DESCRIPTION` | 7 | `rstudio/ggcheck`, `rstudio/tblcheck`, `sonsoleslp/tna`, `sidneybissoli/educabr`, `cambridgeassessmentresearch/kerneqwps`, `r-dcm/measr`, `dexter-psychometrics/dexter` | `LICENSE` alone reads as a stub or `UNKNOWN`, inviting *"no grant"* |
| dual MIT **OR** Apache-2.0 | 2 | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs), [`contentauth/c2pa-python`](https://github.com/contentauth/c2pa-python) | 🟢 the **licensee chooses**; reporting either arm alone removes a right the grant gives |
| code / docs split | 3 | [`microsoft/autogen`](https://github.com/microsoft/autogen), `azure/moodle`, `wildcat430524/stepstogreat` | docs under CC, code permissive |
| code / **data** split | 1 | [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) | 🔴 `CC-BY-NC-SA` data: non-commercial, and this is an education KB where the DATA is the asset |
| GPL + `COPYING.LESSER` | 1 | `datacamp/catsim` | 🟢 the LGPL file is the operative grant; reading `COPYING` alone over-restricts |

🟢 **`ACTION Z`'s new paths paid for themselves: 20 grants sit on paths p122's probe never
requested** — `DESCRIPTION` ×13, `LICENSE-CODE` ×2, `LICENSE-DOCS` ×2, `LICENSE-APACHE` ×2,
`COPYING.LESSER` ×1.

🔴 **The branch, though, was the larger blind spot: 84 of 1 327 addresses default to neither
`main` nor `master`, and 77 of those hold a readable grant that a `main`/`master` probe could not
reach.** The non-standard defaults are not junk branches — they are release lines, which is the
convention of exactly the platforms this KB cares about:

| address | default | grant |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `19.0` | LGPL-3.0 |
| [`claroline/claroline`](https://github.com/claroline/claroline) | `15.0` | AGPL-3.0 |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` | GPL-2.0 |
| [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | `7.x` | the split grant of `P123-B` |
| [`eclipse-ee4j/jersey`](https://github.com/eclipse-ee4j/jersey) | `4.x` | EPL-2.0 |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | `develop` | MIT |

## 🟢 `P123-D` — a readable channel this KB recorded as closed

p122 recorded `api.github.com` and `github.com` HTML as **403 through the session proxy**, and
that is still true of `curl`. 🟢 **It is not true of the `WebFetch` channel, which returned the
rendered repository page for every address tried.** That restores star counts, commit counts and
the archived banner to a KB that had been inferring them. Verified this pass, and the figures
agree with the tree where both can be read:

| address | stars | licence | commits | note |
|---|---|---|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | **816** | MIT | 12 316 | 🟢 **agrees with p122's 816 exactly** |
| [`UCL-INGI/INGInious`](https://github.com/UCL-INGI/INGInious) | 243 | AGPL-3.0 *(tree)* | 3 323 | the page omits the token; the tree gives it |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 144 | Apache-2.0 | 2 269 | |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 139 | MIT | 191 | |
| [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | 23 | EUPL | **22 212** | a national system of record |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 15 | MIT | 32 | 🟡 architecturally interesting, 32 commits |
| [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) | 15 | MIT | 🔴 **4** | 🔴 **not a foundation; recorded as measured-and-rejected** |
| [`skolverket/dnp-ss12000-reference-api`](https://github.com/skolverket/dnp-ss12000-reference-api) | 5 | Apache-2.0 | 35 | the value is the STANDARD, not the stars |
| [`KI-Campus/LRS`](https://github.com/KI-Campus/LRS) | 3 | MIT | 212 | 🔴 **archived 2026-02-20** |

🔵 **The two 15★ rows are the useful ones to state plainly: a search engine surfaced both as
"top open source AI agents for education", and one of them has four commits.**

## 🟢 `P123-E` — the EUPL tier, and Finland's stack is split across two versions

[`opetushallitus/koski`](https://github.com/opetushallitus/koski)'s 654-byte `LICENSE.txt` grants
*"the EUPL, Version 1.1 or — as soon as they will be approved by the European Commission —
subsequent versions"* and reproduces no body. p122's classifier returned `UNKNOWN`; this KB
recorded it as bare **EUPL**, losing both the version and the upgrade clause. The new
by-reference tier reads it as **EUPL-1.1-or-later** and places **9** addresses:

| version | n | addresses |
|---|---|---|
| **EUPL-1.1-or-later** | 6 | `koski`, `ehoks`, `eperusteet`, `oppijanumerorekisteri`, `organisaatio`, `valtionavustus` |
| **EUPL-1.2-or-later** | 2 | `ataru`, `suorituspalvelu` |
| **EUPL-1.2** | 1 | `public-ui/kolibri` |

🟢 **Finland's national education agency publishes its systems of record across TWO EUPL versions,
and the upgrade clause is what reconciles them** — a distinction a single `EUPL` token cannot
carry, on the supply-side evidence that `ACTION C` showed is a European public-sector convention.

## 🟡 Declared instrument gaps

- 🔴 **`CC` ×41, `UNKNOWN` ×40, `GPL-UNTITLED` ×16** — 97 of 1 096 readable grants (8.9 %) do not
  resolve to a version. The `CC` bucket matters most in education, where `CC-BY` and
  `CC-BY-NC-SA` differ commercially and the census cannot currently tell them apart.
- 🔴 **`P123-B`: split grants stated in prose are read as single grants.** `ACTION AA`.
- 🟡 **The gold set contains no branch disagreement**, so `MAIN-ONLY`'s 0 % is a property of the
  set, not of the model.
- 🟡 **No `git ls-remote` tag or commit-date channel was used this pass**; recency figures carried
  on these pages were not re-measured.

## Files

| file | role |
|---|---|
| `resolve_head.sh` | existence + REAL default branch in one call (`ACTION Y`) |
| `grant_set.sh` | reads ALL grant files per address, HEAD then GET (`ACTION Z`) |
| `classify_licence.py` | text → token; title-anchored, split-aware, EUPL by-reference |
| `classify_set.py` | classifies a whole fetched set in one process |
| `extract_claims.py` | row scope in tables, paragraph scope in prose, marker-aware |
| `join_grant_set.py` | scores a claim against the grant SET |
| `calibrate.py` | `ACTION W` — false-positive rate against gold-correct rows |
| `rowscope.py` | re-attributes a candidate with row scope, for hand verification |
| `backfill_marker.py` | `ACTION V` — idempotent marker back-fill |
| `test_p123.sh` | **35 passed / 0 failed**, offline |

## Pre-registered for p124

🔵 **Written here AND in the root `README.md` AND in `intel/open-gaps.md`. `P122-F` was an action
that existed in only one of the three records; `ACTION T` caught it, and this pass's own
consistency check caught the same drift in THIS file before commit — the instrument listed
`ACTION AA` and `ACTION AB` in prose and omitted `AC`, `AD`, `AE`.**

🟢 **`ACTION AA`** — detect a split grant by its SHAPE (a path-scoping noun phrase followed by two
licence tokens), not by appending a phrase to `SPLIT_MARKERS`. Earned by `P123-B`:
[`Elgg/Elgg`](https://github.com/Elgg/Elgg)'s *"Bundled plugins (the contents of the `/mod`
directory) are available only under the GPLv2 license. The remainder of the project is…"*.
🔴 *Refuted if fewer than 3 addresses change verdict.*

🟢 **`ACTION AB`** — extend the `ACTION V` marker to the other TWO correction forms this KB uses:
the audit-table OLD column (21 of the 39 false positives) and unmarked prose *"was X"* /
*"(⚠️ was X)"* (9 of them). `ACTION V` covered one form of three, which is why `P123-H`'s rate did
not move. 🔴 *Refuted if fewer than 15 rows need it.*

🟢 **`ACTION AC`** — a repair must be a SEARCH, not an edit: after repairing an address, assert
that no page carries its old token outside a marked span. Earned by `P123-A`, where p121's repair
left two citing cells stale on the page that announced it. 🔴 *Refuted if the assertion passes on
all 51 already-repaired rows.*

🟢 **`ACTION AD`** — resolve the `CC` bucket (41 rows) to a version. `CC-BY` and `CC-BY-NC-SA`
differ commercially, and in an education KB the DATA is often the asset. 🔴 *Refuted if fewer than
10 resolve.*

🟢 **`ACTION AE`** — build a gold set that CONTAINS branch disagreements, so `MAIN-ONLY` is scored
honestly instead of reading 0 % on 25 rows that all sit on `main`/`master`. 🔴 *Refuted if fewer
than 5 gold rows sit on a non-`main`/`master` default.*

🔴 **`ACTION X`** — **CLOSED as refuted** (2 survivors of a required 5); not to be re-listed.
