---
industry: education
region: Global
updated: 2026-10-11
---

# `p115-region-evidence` — the region a repository DECLARES about itself

**Pass 115, 2026-10-11.** Census window **2026-10-11 01:13 UTC → 02:0x UTC**.

🟢 **`test_p115.sh` — 193 passed / 0 failed**, fully offline: the unit layers drive
`evidence.awk`, `tokens.awk` and `place.awk` directly; the integration layer builds **real
git repositories** on disk, commits them, and serves them to the **real `region.sh`** over
`file://`. No mocks, no network, no `api.github.com`.

## Why this axis, and why now

Eight passes have measured this shelf — tag count, release identity, commit recency, author
concentration, verification surface, dependency closure, provider binding, lock reach. Every
one of them published its figures by region, and every one of them published the same caveat:

> Every regional figure on this page therefore describes the **104 placed rows only**.
> — `intel/market.md`, p114

`orgs.region.tsv` (`P112-L`) places an **org** only when this KB already records its home. It
covers 52 orgs and reaches about a third of the shelf. p113 opened **`Gap 403`** on it, p114
corroborated it from an independent axis, and `intel/market.md` pre-registered the remedy:

> **`Gap 403`** — "The remedy is offline, zero-egress and bounded — **extend the placement
> file** — which makes it the cheapest open item on this page."

**p115 runs that remedy and measures whether it is in fact cheap.** It asks the only question
about region a repository can answer about *itself*:

> **does the tree COMMIT an address that places it?**

Ninth axis in nine passes and the **fifth read from the TREE**. It is also the first pass
whose axis is the brief's own `region` field rather than a property of the code — and the
brief says why that matters: *"A finding with no region attached is worth less than one that
is placed."*

## The three layers, and why they are never added together

| layer | what it reads | does it place a row? |
|---|---|---|
| **0** | a structured metadata file **at the repository ROOT** — `CITATION.cff`, `codemeta.json`, `.zenodo.json`, `package.json`, `composer.json`, `pyproject.toml`, `setup.cfg`, `setup.py`, `pom.xml`, `Cargo.toml`, `go.mod`, `pubspec.yaml`, `DESCRIPTION`, `*.gemspec` | 🟢 **YES — this is the verdict** |
| **1** | the same kinds of file **nested** in the tree | 🔴 **never** — reported as a CONTRAST |
| **R** | the **root README** | 🔴 **never** — reported as a CEILING |

### `P115-N` — the depth split is the difference between a right answer and a confident wrong one

🔴 **The smoke test proved it on the largest row of this shelf before the census ran.** Read
flat — every structured file in the tree, root and nested alike — **`moodle/moodle` comes back
`contested`** on the evidence of `gjcampbell.co.uk`, `tubo-world.de` and `www.mullie.eu`: the
maintainer emails of three third-party libraries Moodle **bundles** under `lib/`. Moodle HQ is
in Perth.

🔵 **The flat read does not merely fail to place the row. It offers two European countries for
an Australian project** — and `region` is a field this KB filters on, so a wrong value does not
read as a guess downstream, it reads as data (`P800`).

🟢 **`P115-F` excludes `vendor/`, `node_modules/`, `third_party/` and friends; it cannot exclude
`lib/`, because `lib/` is also where a project keeps its own code. Depth can.** A declaration
at the ROOT is the repository's; one nested under it belongs to whatever is nested there. The
suite pins this as a regression with a fixture whose bundled libraries are BOTH European, so
layer 1 returns a single clean region — the sharp form of the trap, because a flat read would
have published it.

## The rules, each one with its stated cost

| rule | what it does | what it COSTS, stated rather than discovered later |
|---|---|---|
| `P115-B` | layer-0 filenames are a **closed list, matched on the basename** | `my-package.json` is never read — and neither is a real manifest under an unusual name |
| `P115-F` | vendored prefixes excluded **before any body is fetched**, and the exclusion is counted | a project that genuinely lives in `vendor/` is invisible |
| `P115-H` | a token counts only on a line carrying a **declared key** | a **minified** JSON file is one line, so every key matches and the scope widens to the whole file. It never reads LESS. `wideline` counts how often it happened |
| `P115-I` | **only emails and URLs** are harvested, never bare hostnames | `affiliation: University of Helsinki` places nothing, and neither does `helsinki.fi` written bare. It also cannot mistake `package.json` or `1.2.3` for a host |
| `P115-D` | `.io .co .me .ai .be .ly .gg .to .sh .st .fm .tv .cc .gl .im .is .so .md .ws .nu .sc .ms` are a **vanity class** and never place | a genuinely Belgian university address is **dropped**. `youtu.be` is not Belgian, `bit.ly` is not Libyan, `shields.io` is not in the Indian Ocean — and a map that reads those as countries mis-states whichever rows happen to carry a badge |
| `P115-E` | a **committed stoplist** of 86 service, registry, forge, standards-body and regulator hosts | a repository that really is maintained BY a listed body is dropped. A repo that **cites** the EU AI Act is not European, and `ec.europa.eu` in a `url:` field would otherwise place it in EMEA |
| `P115-J` | the region column is the **country's** region; the class column decides whether a **hostname** may use it. A **typed** `country:` field (ISO-3166 by the CFF schema) places on `cc` **or** `vanity` | — |
| `P115-K` | two regions in the evidence is **`contested`**, never a majority vote | a genuinely cross-regional project is left unplaced — which is a result a reader can act on, where a confident single answer is not |
| `P115-C` | the country→region map is a **committed file**, 123 `cc` + 11 `cc?` + 23 vanity + 17 gTLD rows | — |

🔵 **The direction of every one of these costs is the same, on purpose: this instrument
UNDER-counts.** On a closed field that a filter reads downstream, an under-count that cannot
invent a country is the only error worth having.

## `P115-Q` — the controls read the SAME snapshot, not a later one

p112 and p114 ran their controls as **separate censuses**, minutes or hours apart. A control
fetched from a different snapshot of 296 moving repositories measures two things at once.

Everything downstream of the token stream here is pure stage C, so `region.sh` keeps each
row's stream (`P115_TOK=<dir>`) and **`controls.sh` re-derives all three controls from those
exact bytes** — same window, same trees, zero extra egress, re-runnable by any later pass.
🟢 **The suite drives BOTH the refetching env-var controls and the replay, and compares them
row for row across all four modes; a replay that disagreed with a refetch would be worthless
as evidence.**

| mode | what it measures |
|---|---|
| `nostop` | what `P115-E`'s stoplist is worth |
| `novanity` | what `P115-D`'s vanity class costs AND prevents |
| `nor` | layer R's whole contribution |
| `flat` | 🔴 **what this instrument itself would have published before the depth split** — layer-1 tokens relabelled as layer 0, which is how `P115-N` stops being an anecdote about one row and becomes a figure for the whole shelf |
| `P115_CAP=<n>` | the blob cap's contribution |

🔵 **A row with no saved stream reads `NO-STREAM`, never `0` (`P1040`): an UNREAD remote and an
empty tree are rows the controls **cannot speak for**, and a control that filled them with
zeros would be counted as evidence of absence.**

## Six faults the suite found in this instrument before the shelf did

🟢 **Every one of these would have produced a published figure that was wrong and silent.**

| # | fault | what it would have published |
|---|---|---|
| `P115-L` | `mawk 1.3.4` does not compile `/^[0-9a-f]{40}( |$)/` — it aborts with `REcompile() - panic: values still on machine stack` | the whole program dies; caught loudly |
| `P115-M` | the two committed maps were loaded **by FILENAME**, and the driver materialises them under different names for the control modes. Both fell through unread | 🔴 **296 rows of `no-country`, with a straight face.** Now positional, plus a `MAPFAIL` guard in `END` |
| `P115-O` | the `eval` key class `[a-z_]*` was copied from p112/p114, whose keys have no digits. This pass's keys are `region_0`, `dom_1`, `cc_r` — so `region_0=North America` passed through unquoted and the shell ran `America` as a command | 🔴 **rows printed with the REGION COLUMN EMPTY**, plus a stray line of output. A copied idiom is a parameter too |
| `P115-P` | `regionlist()` iterated `for (r in REGIONS)`, whose order awk leaves unspecified | `EMEA|APAC` and `APAC|EMEA` for the same evidence. The verdict was right and the **bytes were not reproducible**, which defeats the point of committing the TSV |
| — | `P115_NO_R=1` left the readme **counter** on, so the row reported `r-no-address` — "there is a README and it holds no address" — when the truth was "layer R was not read" | a control misreporting its own reason |
| — | `printf` arity: 36 specifiers for 37 columns, **twice** (`region.sh`, then again in `controls.sh`) | 37-column rows against a 38-column header; the final `inst` column silently dropped |

🔵 **A seventh was found in the SUITE, not the instrument, and is kept as a fixture:** a bundled
fixture was planted at `lib/thirdparty/package.json`, which `P115-F` excluded as vendored —
correctly. The fixture moved to `lib/bundled/`, which is the shape `P115-N` is actually about.

## Channel

Anonymous git lane only, re-probed live this pass. **Nothing below is a new discovery; all four
lines are carried from `P107-A`, `P247`, `P249` and `P798`, and `compose/code/` was searched for
an existing instrument before any channel defect was written (`P249`'s second clause).**

| probe | result |
|---|---|
| `git ls-remote` / `git fetch --depth=1 --filter=blob:none` | 🟢 `rc=0` |
| `raw.githubusercontent.com/<slug>/HEAD/<file>` | 🟢 `200` |
| `api.github.com` | 🔴 `403` |
| `curl -sI https://github.com/<live-slug>` | 🔴 **`403` — the brief's own mandated verifier, wrong on this channel (`P247`/`P249`)** |
| every non-GitHub host (`ncleg.gov`, `dpi.nc.gov`, `unesco.org`, `eur-lex.europa.eu`, `en.wikipedia.org`) | 🔴 **`000` / `connect_rejected`, read from the proxy's own ledger (`P798`)** |
| `WebFetch` on any host | 🔴 **`getaddrinfo ENOTFOUND` — a NEW mechanism for `P798`'s ledger: DNS-layer, not CONNECT-layer** |

Tree from a depth-1 blob-filtered fetch; evidence-file **bodies** from a batched lazy blob
fetch against the same promisor remote (`P111-H`, reused by p112, p114 and reused again here).

## How to re-run it

```sh
cd compose/code/p115-region-evidence
./test_p115.sh                                   # 193 / 0, offline

P115_TOK=/tmp/tok ./region.sh addresses.txt > result.$(date -u +%F).tsv
./controls.sh /tmp/tok addresses.txt nostop   > result-nostop.CONTROL-$(date -u +%F).tsv
./controls.sh /tmp/tok addresses.txt novanity > result-novanity.CONTROL-$(date -u +%F).tsv
./controls.sh /tmp/tok addresses.txt nor      > result-nor.CONTROL-$(date -u +%F).tsv
./controls.sh /tmp/tok addresses.txt flat     > result-flat.CONTROL-$(date -u +%F).tsv

./emit_placements.sh result.$(date -u +%F).tsv > addresses.region.tsv

./crosstab.sh result.$(date -u +%F).tsv          # every figure, enumerated
```

🔵 **`crosstab.sh` exists so that no figure in `intel/market.md` is counted by hand.** `P93`:
a count is only a count if it ENUMERATES.

---

# What it measured

**Census window 2026-10-11 01:13 → 01:25 UTC.** `region.sh` read **296 of 296** addresses in
**12 minutes**, `rc=0` on every one, 🟢 **zero UNREAD, zero empty trees**, **579 448 files**
enumerated. Four controls re-derived from the same snapshot in **2.5 seconds** each.

🔴 **ONE OPERATIONAL FAULT, OWNED: I edited `region.sh` WHILE the census was running** (file
mtime `01:21:04`, inside the `01:13 → 01:25` window), adding the `class_0` column. Bash
re-read the file from a byte offset and emitted one parse error to stderr. 🟢 **The 296 token
streams were already on disk, so the authoritative `result.2026-10-11.tsv` is the REPLAY,
produced by `controls.sh default` from those streams with the final code — and its 38 shared
columns are `md5`-identical to the live run's, row for row (`1545c426f7ff…`).** 🔵 **`P115-Q`
was built to make the controls comparable and it is what made the run salvageable; without
the saved streams this pass would have had to refetch 296 repositories or publish figures
from a script that changed underneath them.**

## The headline: the remedy `Gap 403` pre-registered is nearly empty, and the one it discarded is not

| figure | value |
|---|---|
| addresses read | 🟢 **296 / 296**, zero unread |
| rows with a structured metadata file anywhere | 214 |
| rows with one at the **ROOT** | **175** |
| rows layer 0 **PLACES** | 🔴 **22 (7.4 %)** — 19 `placed` + 3 `typed` |
| of those, rows the committed org map leaves **entirely unplaced** | 🟡 **11** |
| plus rows it holds only as **provisional** | 🟡 **1** |
| **`Gap 403`'s remedy, measured** | 🔴 **12 of 193 unplaced rows — 6.2 %** |
| rows **layer R** (the README) would place | 🟢 **59**, of which **48** layer 0 cannot |
| layer R checked against the committed org map | 🟢 **25 of 25 AGREE, 0 contradict** |

🔴 **`Gap 403` called its remedy "offline, zero-egress and bounded — which makes it the
cheapest open item on this page". Bounded it is. Cheap it is not: it buys 12 rows of 193.**
🔵 **The reason is structural and now measured: 82 of 296 rows commit no structured metadata
at ALL, only 175 carry any at the root, and of those 175 just 22 put a country-bearing
address inside a declared key. The channel is almost empty before any rule of this
instrument is applied.**

🟢 **And the channel this pass built as a throwaway — layer R, the README, declared a CEILING
that never places — is the one that works.** It places **59** rows, **48** of them beyond
layer 0's reach, and on every one of the **25** rows where an independent committed baseline
can check it, **it agrees**.

## Placements, by region and by evidence class

| region | layer 0 places | academic | government | other | typed |
|---|---|---|---|---|---|
| **EMEA** | 9 | 1 | 0 | 7 | 1 |
| **North America** | 7 | 🟢 **7** | 0 | 0 | 0 |
| **LATAM** | 6 | 0 | 0 | 4 | 2 |
| 🔴 **APAC** | 🔴 **0** | — | — | — | — |

🟢 **Every one of North America's seven placements is `academic`** — `berkeley.edu` (×3),
`brynmawr.edu`, `calpoly.edu`, `lafayette.edu`, `gatech.edu`, `nd.edu`, `vt.edu`,
`csail.mit.edu`. 🔵 **That is the `.edu` registry doing the work: a US-restricted suffix is
the one address on this shelf that names an institution and a country in the same token.**

🔴 **APAC places ZERO rows at layer 0, and the brief asks for that to be written down rather
than left silent.** 🟢 **It is not that the shelf has no APAC rows — layer R finds **seven**,
and they are among the cleanest evidence on the shelf:**

| row | layer-R evidence |
|---|---|
| [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) + `-cicd` + `-ui` | `aiverifyfoundation.sg`, 🟢 **`www.imda.gov.sg`** (Singapore's IMDA — `government` class) |
| [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) | 🟢 **`acm.hdu.edu.cn`** (Hangzhou Dianzi University — `academic`) |
| [`tzyll/goparrot`](https://github.com/tzyll/goparrot) | 🟢 **`www.gavo.t.u-tokyo.ac.jp`** (University of Tokyo — `academic`) |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | `educhain.in` |
| [`Earth-OL-Player/Ai_learn_project`](https://github.com/Earth-OL-Player/Ai_learn_project) | `ai-studyhub.cn` |

🔵 **So APAC's zero is a property of WHERE this instrument looks, not of the shelf.** Three
Singaporean, two Chinese, one Japanese and one Indian row are sitting in plain sight in their
READMEs, two of them behind registry-restricted academic suffixes and one behind a government
one. **That is the single strongest argument for promoting layer R, and it is the reason this
pass pre-registers the promotion instead of performing it.**

## The controls: every rule is now a number, and every number is a named row

🟢 **No rule below is asserted. Each was switched off over the SAME 296 token streams
(`P115-Q`), and what moved is listed by address.**

### `nostop` — the stoplist is worth 2 rows, and the interesting part is that they were RIGHT

| row | would be placed | on |
|---|---|---|
| [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | EMEA | 🔴 **`ec.europa.eu`** |
| [`opetushallitus/organisaatio`](https://github.com/opetushallitus/organisaatio) | EMEA | 🔴 **`ec.europa.eu`** |

🔵 **`opetushallitus` IS the Finnish National Agency for Education and the committed org map
already places it EMEA. So the stoplist cost two placements that happened to be CORRECT —
and it was still right to cost them, because the evidence was a European Commission URL, not
a Finnish one.** 🟢 **A rule that only ever blocks wrong answers is easy to justify; this one
blocked two right answers reached by invalid reasoning, which is the harder and the more
important case to get right. `P115-E` stands.**

### `novanity` — the vanity class prevents 4 wrong rows, 3 of them in LATAM

| row | would be placed | on | why that is wrong |
|---|---|---|---|
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🔴 **LATAM** | `huggingface.co` | 🔴 **`.co` is Colombia. The org map holds `huggingface` as `North America?`** |
| [`kualico/rice`](https://github.com/kualico/rice) | 🔴 **LATAM** | `www.kuali.co`, `nexus.kuali.co` | Kuali is a US company |
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🔴 **LATAM** | `ankimcp.ai` | `.ai` is Anguilla |
| [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) | 🔴 EMEA | `sonsoles.me` | `.me` is Montenegro; this is a personal vanity domain |

🔴 **LATAM places 6 rows. Without the vanity class it would place 9 — and a THIRD of the
region's figure would be `.co` and `.ai` vanity domains.** 🔵 **On a KB whose brief exists to
serve a LATAM engagement as well as a North American one, an instrument that inflates LATAM
by 50 % from vanity TLDs is worse than one that reports a small number. `P115-D` stands, and
its cost — a genuinely Belgian or Icelandic address dropped — is the price.**

### `flat` — what the pre-depth-split read would have published (`P115-N`, shelf-wide)

| row | flat would place | on | correct? |
|---|---|---|---|
| [`atutor/ATutor`](https://github.com/atutor/ATutor) | 🔴 **LATAM** | `tiagogouvea.com.br` | 🔴 **no — ATutor is a Toronto project** |
| [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 🔴 **EMEA** | `keithcirkel.co.uk`, `enshrined.co.uk`, `sensiolabs.de` | 🔴 **no — three JS/PHP library authors, not the maintainer** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟡 EMEA | `synchromedia.co.uk` | 🟡 right region, wrong evidence (the org map places it EMEA on its own grounds) |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟢 EMEA | `www.ilias.de` | 🟢 plausibly right |
| [`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials) | 🟢 EMEA | `www.edcisupport.eu` | 🟢 plausibly right |
| [`aiverify-foundation/moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) | 🟢 **APAC** | `aiverify.sg` | 🟢 right |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 **APAC** | `buaa.edu.cn` | 🟢 right, `academic` |

🔵 **Seven rows, of which at least two are demonstrably wrong and four look right. That is the
honest shape of the flat read: it is not noise, it is a 70/30 instrument** — and `region` is
a closed field a filter reads downstream, where 30 % wrong is not a tolerable rate. 🔴 **Note
also that the flat read is the ONLY way APAC appears at all in a structured layer, and it
arrives in the same breath that puts a Canadian project in Brazil.**

### `nor` — layer R's whole contribution, isolated

| figure | layer R on | layer R off |
|---|---|---|
| `r-placed` rows | **59** | 🟢 **0** |
| layer-0 placements | 22 | 🟢 **22 — unchanged** |

🟢 **The layers are genuinely separate: switching layer R off moves no layer-0 verdict.**

## 🔴 The caveat that keeps layer R from being promoted THIS pass

🔵 **Two measurements, published together because either alone would mislead:**

| | |
|---|---|
| 🟢 layer R checked against the committed org map | **25 of 25 agree, 0 contradict** |
| 🔴 r-placed rows with **no settled org** to check against | **34 of 59 (58 %)** |
| 🔴 of the 11 rows BOTH layers place, how many does layer R read on the **same host** | 🔴 **8 of 11** |

🔴 **So the 25/25 is measured on 42 % of layer R's own output, and layer R's agreement with
layer 0 is mostly NOT independent — in 8 of 11 cases both layers are reading the same
hostname, which is one piece of evidence counted twice.** 🟢 **A channel that is right on
every row you can check, and unverifiable on the majority of the rows it claims, is a
promotion CANDIDATE, not a promotion. Pre-registered as this pass's action, below.**

## 🟡 `P115-W` — the one-row disagreement p114 recorded and declined to reconcile is case folding

p114 wrote, of its own regional denominator:

> **the two readings of the same committed file differ by ONE row.** Recorded rather than
> reconciled silently; the likely cause is the treatment of the 11 provisional placements.

🟢 **Re-derived from the two committed files, the cause is not the provisionals. It is CASE,
and it is exactly one address:**

| reading | settled | provisional | unplaced |
|---|---|---|---|
| org prefix matched **case-sensitively** | 93 | 10 | 🟡 **193** ← p113's figure, and `Gap 403`'s |
| org prefix matched **case-insensitively** | 93 | 11 | 🟡 **192** ← p114's figure |

🔴 **The row is [`apereo-learning-analytics-initiative/larissa`](https://github.com/apereo-learning-analytics-initiative/larissa).**
`addresses.txt` holds **six** addresses under `Apereo-Learning-Analytics-Initiative/` and
**one** under `apereo-learning-analytics-initiative/`. The map spells the org with capitals,
so the lowercase address misses an exact match and finds one under case folding.

🟢 **GitHub org names resolve case-insensitively, so p114's 104/192 is the correct reading and
p113's 103/193 is not — for a reason neither pass stated.** 🔴 **But the DEFECT is not in
either map: the shelf itself holds one organisation under two spellings**, which is the
`p439-case-collision-gate` / `p443-canonical-spelling` family of fault landing on
`addresses.txt`. 🔵 **Not fixed here: p114 carried `addresses.txt` verbatim from p112 "so the
cross-tab is row-for-row", and silently re-spelling a row would break nine passes of
comparability. Pre-registered as an action instead.**

## 🟢 `P115-X` — one of p112's three contested placements is now settled by evidence

| row | org map | 🆕 p115 | evidence |
|---|---|---|---|
| [`Apereo-Learning-Analytics-Initiative/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 🟡 **`EMEA?`** | 🟢 **North America** | 🟢 **`vt.edu`** — Virginia Tech, `academic` class |

🔵 **p112 flagged this org `EMEA?` with its own note: *"p111 placed it EMEA; the Apereo
Foundation is US-registered (P112-M)"*. The repository's own root metadata carries a
`.edu` maintainer address, which is the strongest class short of a typed field, and it points
where p112 suspected.** 🟡 **It settles ONE ADDRESS, not the org: `P115-U` is address-keyed
precisely because one org can hold repositories maintained from different places, and the
other six `Apereo-…` addresses place nothing at layer 0.**

## The reasons the other 274 rows do not place, enumerated

| verdict | rows | % | what it means |
|---|---|---|---|
| `no-country` | **97** | 32.8 % | root metadata holds addresses, none of them country-bearing |
| `no-struct` | **82** | 27.7 % | 🔴 **no structured metadata file anywhere in the tree** — this channel can never reach these |
| `no-address` | **56** | 18.9 % | root metadata exists and carries no address in any declared key |
| `nested-only` | **39** | 13.2 % | structured metadata exists, none of it at the root (`P115-N` refuses it) |
| 🟢 `placed` | **19** | 6.4 % | — |
| 🟢 `typed` | **3** | 1.0 % | a CFF `country:` field: `BR`, `BR`, `GB` |

Across the 97 `no-country` rows the domain classes seen were **170 stoplisted**, **105 gTLD**,
**23 vanity**, **0 contested-ccTLD** and **0 unknown TLD**. 🟢 **The two zeros are worth
stating: the committed country map has no gaps on this shelf — every TLD that appeared is
classified — and no row was lost to a contested country.**

🟢 **`P115-H`'s stated error never fired: `wideline` is 0 across all 296 rows.** No metadata
file on this shelf is minified, so the key-scoping rule read exactly what it claims to read.
🔵 **11 rows hit the 40-blob cap and each declares it (`capped=1`); 42 rows carry a vendored
path that was excluded before any body was fetched.**

## Coverage after this pass

| | rows | % of 296 |
|---|---|---|
| settled by the committed **org** map (`orgs.region.tsv`) | 93 | 31.4 % |
| 🆕 settled by the committed **address** map (`addresses.region.tsv`) and nothing else | 🟢 **12** | 4.1 % |
| **covered** | 🟢 **105** | 🟢 **35.5 %** |
| provisional only (`EMEA?` / `North America?`) | 9 | 3.0 % |
| 🔴 still **UNPLACED** | 🔴 **182** | 🔴 **61.5 %** |

Union by region: **North America 47**, **EMEA 36**, **APAC 13**, **LATAM 9**. 🔴 **APAC's 13
all come from the org map; p115 adds none.**

## Actions this pass pre-registers

| # | action | the clause that would refute it |
|---|---|---|
| **A** | **Validate layer R on the 34 rows with no settled org to check**, by a second channel (the `raw.githubusercontent.com` lane reaches `CODEOWNERS`, `.github/FUNDING.yml` and `AUTHORS`, none of which this pass reads). Promote layer R to a placing layer only if it holds | 🔴 **refuted if layer R contradicts the second channel on ≥ 3 of 34** |
| **B** | **Re-spell `apereo-learning-analytics-initiative/larissa`** to the canonical casing in `addresses.txt`, in a commit that changes NOTHING else, so nine passes of row-for-row cross-tabs break visibly once rather than silently forever | 🔴 refuted if the lowercase address and the canonical one resolve to different repositories |
| **C** | **Re-read the 8 `other`-class placements whose evidence is a single personal domain**, [`inducer/relate`](https://github.com/inducer/relate) first: its EMEA placement rests entirely on `documen.tician.de`, its README names no institution (`inst=0`), and layer R "corroborates" it by reading **the same host** | 🔴 refuted if every `other`-class row also carries institutional evidence the instrument did not read |
| **D** | **Add the Epesi family to `addresses.txt`** (see `verticals/solutions.md`, `P115-T`) at the next census, not this one — `addresses.txt` is carried verbatim this pass so every cross-tab above is row-for-row against p114 | — |

## 🟢 `P115-AK` — the gates this pass ran against its own writes were themselves unrunnable

🔵 **Validating a pass's writes against this KB's gates is part of the pass. Doing it found
that all FIVE python gates fail under `python3 -I`, which is the invocation several of their
own READMEs prescribe:**

| gate | plain `python3` | 🔴 `python3 -I` |
|---|---|---|
| `p370-gap-gate` | 🟢 27/27 | 🔴 `ModuleNotFoundError` |
| `p471-gap-gate-language` | 🟢 25/25 | 🔴 `ModuleNotFoundError` |
| `p243-frontmatter-coverage` | 🟢 23/23 | 🔴 `ModuleNotFoundError` |
| `p239-table-integrity` | 🟢 OK | 🔴 `ModuleNotFoundError` |
| `p383-region-heading-gate` | 🟢 11/11 | 🔴 `ModuleNotFoundError` |

🟢 **Cause: `-I` is isolated mode and drops the script's own directory from `sys.path`; it
also ignores `PYTHONPATH`, so the obvious workaround fails too. Fixed in two lines per file
and verified green under BOTH invocations, with no regression.** 🔵 **A gate that cannot be
RUN is a gate that passes everything — `P471`'s failure one step earlier in the pipeline.**
