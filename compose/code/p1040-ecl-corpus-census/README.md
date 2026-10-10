# `p1040-ecl-corpus-census` — the ECL remedy, wired in, run over the whole corpus

**Pass 106, 2026-10-10.** Written and executed in-pass (`P1028`, a fourth consecutive pass).

`test_p1040.sh` — **82 passed, 0 failed**.
`census.sh lost-addresses.corpus-census-1381.2026-10-10.txt 8` → `1 381` rows in **2 m 22 s**, stderr empty.

## Why it exists

Pass 105 opened `Gap 398`: `classify_payload` returns `UNRECOGNISED` for every ECL-2.0 payload,
because the real ECL text names the *"Apache 2.0 license"* in lower case and contains **zero**
occurrences of the string `Apache License` that the Apache branch keys on. A permissive row landed
in neither the permissive nor the copyleft bucket — **invisible rather than mislabelled**, which
`P1036` records as the worse failure, because the census footing stays correct while the
composition silently shifts.

Pass 105 wrote the remedy (`classify_ecl`) and **left it beside the instrument instead of inside
it**. Its own lead #1 said so: *"`Gap 398` is open precisely because the remedy exists and is not
yet in the instrument. The 99-address probe found 2 uncounted permissive rows; the corpus is 1 400+
addresses and has never been audited for this."*

This instrument is that wiring, plus the audit.

## What it measures

| limb | file | question |
|---|---|---|
| A | `census.sh` | every corpus address's grant, with ECL **visible** |
| A — calibration | `calibrate.sh` | does the new, cheaper probe path agree with `p1029`'s? |
| A2 | `unread.sh` | what else is the classifier blind to? (`P1036`, by hand) |
| A3 | `manifest.sh` | the rows whose grant is **not in the `LICENSE` file** |
| A4 | `reconcile.sh` | do the hand-reads reconcile to the last row? |
| B | `packagist.sh`, `retry.sh` | `Gap 399` — a channel that reaches the Moodle plugin layer |
| C | `holder.sh` | `P1035` applied to **EMEA**, which is pass 105's lead #2 |

## Results

```
addresses=1381 live=1084 nogrant=233 absent=38 nocontrol=25 throttled=1
permissive=804 copyleft=199 cc=51 non_grant=13 unread=17
ecl=10 eupl=8
```

**804 + 199 + 51 + 13 + 17 = 1 084.** It reconciles.

### The headline: the sample understated the blindness five-fold

The 99-address probe of pass 104 held **2** uncounted ECL rows. The corpus holds **10**, carrying
**six** distinct ECL texts — pass 105 had pinned four across six repositories:

| text (`sha256`-16) | bytes | repositories |
|---|---|---|
| `0688f62d04f14e4b` | 11 120 | `sakaiproject/sakai` |
| `76a975068930323e` | 11 340 | `opencast/opencast` |
| `a9ea5cca8da2c8d5` | 11 087 | `lap-sakai-extractor`, **`openlrs`** |
| `fb10d1260ddc8dff` | 9 919 | `LearningAnalyticsProcessor`, `OpenDashboard-api`, `OpenDashboard-legacy` |
| **`f339063d2f604ce9`** | 9 878 | **`openlrw`** — a text pass 105 had not seen |
| **`d4db8f22f8d564eb`** | 11 182 | **`kuali/rice`, `kualico/rice`** — one text at two org names |

### And ECL was one blind spot of six

`unread.sh` read all 54 `UNRECOGNISED` payloads from the first run, as `P1036` requires. Reading
them found five further mechanisms, each of which had put a real grant in no bucket at all:

| mechanism | rows | evidence |
|---|---|---|
| **EUPL** — the EU's own licence, never in any branch | **8** | all `opetushallitus/*`, 296–654 B, named by reference not by body |
| **case** — `GNU Affero General Public License` in title case | 4 | branches keyed on the ALL-CAPS title only |
| **punctuation** — `Mozilla Public License, version 2.0` | 1 | one comma and a lowercase `v` |
| **language** — `LICENÇA PÚBLICA GERAL AFFERO GNU` | 2 | `portabilis/*`, one text at 35 326 B |
| **manifest** — the grant is in `DESCRIPTION`, not `LICENSE` | 5 | `LICENSE` is 45–108 B of `YEAR:` / `COPYRIGHT HOLDER:` |
| **non-grant** — Elastic 2.0, BUSL, PolyForm, bespoke terms | 13 | sitting in `UNRECOGNISED` **beside real grants** |

That last row is the one that cuts both ways, and it is why `NON-GRANT` is now a bucket of its own:
recovering a permissive row is an opportunity, but promoting one of **these** by mistake is a legal
problem. `dssg/student-early-warning` — the subject of `Gap 392` — is a click-through terms-of-use,
not a licence. `sdv-dev/sdv` is BUSL-1.1. `sodadata/soda-core` and `canyongbs/advisingapp` are
Elastic-2.0.

## Three regressions this instrument found in its own code

Each was a real misclassification over the live corpus, found by **diffing two census runs** rather
than by inspection, and each is now a test against the actual payload that produced it.

1. **`Community License` swallowed ECL.** `"Educational Community License"` *contains* the substring
   the bespoke-terms branch matches. Unguarded, the non-grant branch took the exact permissive
   family this instrument exists to recover: 10 rows moved to `NON-GRANT` — **the `Gap 398` fix
   inverted into a worse error than the one it repaired.**
2. **A copyright formula demoted three Apache-2.0 rows.** `huggingface/transformers`,
   `mlflow/mlflow` and `masakhane-io/masakhane-ner` carry a conventional `All rights reserved` line
   above a full Apache-2.0 text. The generic branch on that phrase is **gone**: it is a copyright
   formula, not a restriction, and it appears inside BSD notices, which are grants.
3. **MPL-2.0 classified as GPL-3.0.** MPL section 3.3 *names* the GNU GPL, LGPL and AGPL as
   "Secondary Licenses", so 15 921 B of plain MPL (`dequelabs/axe-core`) matched the case-folded GNU
   branch. **A licence that references another family must be settled before the family it
   references** — the hazard `classify_payload` already documents for AFFERO-before-GPL, one level up.

The general rule arrived at from (1) and (2): **a restriction branch must never fire unchallenged on
a payload that declares a known grant family.** Where both are genuinely present the answer is not a
silent pick either way — it is `GRANT+RESTRICTION-CONFLICT`, bucketed `UNREAD` for a hand-read
(`caviraoss/pagelm`: an MIT grant plus 7.5 KB of other terms).

And the rule needed a third attempt, because the strip has to run on **flattened** text. Licence
files are hard-wrapped at ~72 columns, so a multi-word pattern can straddle a newline: the ECL title
appears five times in the Sakai payload and the fifth wraps as `Licensed under the
Educational\nCommunity License`. A strip keyed on the unwrapped title removed four of five and left
a bare `Community License` at the start of line 196 — so ECL came back a conflict again, **from one
line break.**

## And two in its own plumbing

`probe_one` runs inside an `xargs bash -c` subshell, so every function it calls must be named in
`export -f`. Twice in this pass one was not:

- the first time, `classify_restricted` failed, its empty output fell through `classify_grant`'s
  final case, and **1 077 rows published a blank licence that tallied as `UNREAD`** — the `Gap 398`
  failure mode in its purest form, a silence counted as data, produced by plumbing rather than by
  any licence text;
- the second time the hand-written guard added to catch exactly that **missed it too**, because the
  guard kept its own copy of the same list and `declares_known_grant` was in neither.

So the export list is now **derived from `classify.sh`** — every top-level `name()` definition — and
the guard iterates the derived list and **refuses to emit rows** if any function is not visible to a
child shell. Verified by removing an export and observing
`REFUSING TO RUN: classify_payload is defined but not exported to the worker subshell`, exit 2.

## The cheaper probe path, and its calibration

`p1029` spent a `git ls-remote --symref` per address purely to learn the default branch name for the
raw path. `raw.githubusercontent.com` serves the literal ref `HEAD`, so that round-trip is
unnecessary — and the case that would break a guessed branch name is real:
`sakaiproject/sakai` answers **200 at `HEAD`** and **404 at `main`**, because its default is
`master`. Dropping it is what makes a 1 381-address census affordable: **99 addresses in 13 s**
against the old path's per-address git calls.

`ls-remote` is kept as the **tie-breaker**, not the first step: without it, "repository is gone" and
"repository has no `LICENSE` and no `README`" are the same pair of 404s, so it runs only for the
rows where that distinction is load-bearing.

Calibrated against `p1029`'s own 99 rows — licence, bytes and `sha256`:

```
compared=99 agree=92 recovered_by_ecl=2 disagree=5
```

The 92 agree **byte for byte and hash for hash**. The 2 recovered are exactly the two rows pass 105
predicted (`lap-sakai-extractor`, `opendashboard-legacy`) — **a second instrument confirming pass
105's 38 → 40 correction**. The 5 reported as disagreeing are the 5 `ABSENT` rows and are a
**spelling** difference, not an answer: `p1029` writes `-` in the licence column of an absent row
where this limb writes `ABSENT`. A comparator keyed on a field's spelling reports a formatting
choice as a contradiction; recorded here so the next reader does not re-investigate it.

## Limb B — `Gap 399`, and what packagist is NOT

Pass 105 measured `moodle.org` at `http=000` and opened `Gap 399`: the plugin-directory denominator
`T30`/`P1033` needs "cannot be measured here at all". Its lead #6 named `packagist.org`, never
probed from this session. **Probed this pass: `packagist.org` = 200, `repo.packagist.org` = 200.**
The channel is **OPEN**.

What it is **not** is a mirror of the plugin directory — and that is the finding:

```
types_probed=46  types_nonempty=21  types_zero=25  packages=159
```

**All 143 packages that declare a licence at all declare the GPL-3 family. Not one is
permissive.** `P1033`/`T30` — "the copyleft frontier is the plugin tree" — was carried on **7 rows**;
it now rests on 143, and it holds without exception.

Two further measurements:

- the declaration is **free text**: `GPL-3.0-or-later` (136), `GPL-3.0+` (5), `GPLv3` (2) are three
  spellings of one grant. A census keyed on an exact string would split the dominant family into
  three buckets and report none of them as dominant — `P1037` reaching the *declared* field;
- **`moodle-aiprovider` = 0 and `moodle-aiplacement` = 0.** The two plugin types Moodle's own AI
  subsystem defines have **no packagist presence at all**, against 159 packages across 21 older
  types. The AI seam of the world's most-installed LMS does not publish through the PHP package
  channel, which is the commercial reading of `T28` arriving through a second channel.

`retry.sh` exists because limb B's first run lost 2 types and 18 packages to a dropped tunnel and
published them as `HTTP-000000` — a status code that does not exist, caused by
`curl -w '%{http_code}' || echo 000` emitting **both**. Fixed, and the lost rows re-probed on their
own: `retry: recovered=44 still_lost=0`.

## Limb C — `P1035` applied to EMEA

Pass 105's lead #2: *"If a university name cannot place a row in LATAM, it cannot place one in EMEA
either — and `fwu-de` / `dini-ag-kim` were placed on org-name reasoning this pass has just
invalidated."* So the org name is not evidence here either. Every row carries the string that
placed it.

| row | region | placed by |
|---|---|---|
| `fwu-de/fwu-kc-extensions` | EMEA | ccTLD `fwu.de` |
| `dini-ag-kim/schulfaecher` | EMEA | ccTLD `dnb.de` |
| `fwu-de/lehrplan-ontologie`, `fwu-de/schulfach-ontologie` | EMEA | country word `Germany` |
| `opetushallitus/ataru` | EMEA | system name `Opetushallitus`; holder *Finnish National Agency for Education* |
| `opetushallitus/koski` | EMEA | ccTLD `eduuni.fi` |
| `portabilis/i-diario` | LATAM | ccTLD `com.br` |
| `fwu-de/ais-chat`, `fwu-de/mem-mcp`, `fwu-de/schulart-ontologie`, `dini-ag-kim/school-curriculum-pg` | **UNPLACED** | no placing string in the tree |

**And the limb caught a trap that would have misplaced the whole copyleft tier.** The holder line of
`fwu-de/ais-chat` reads `Copyright (C) 2007 Free Software Foundation`, and `portabilis/i-diario`
reads `Copyright © 2007 Free Software Foundation` — because that is the **licence text's own**
copyright, not the project's. A holder reader that takes the first copyright line out of a GPL or
AGPL payload reads the FSF as the holder of every copyleft project in the corpus, and the FSF is in
Boston. Here it returned `UNPLACED` rather than a wrong region, but **by luck, not by design**: the
FSF line happens to carry no placing string. `i-diario` placed LATAM only on its README's `.com.br`.

## Files

| file | what it is |
|---|---|
| `classify.sh` | the classifier: `p1029`'s carried over verbatim, plus `classify_ecl` wired in, plus the six families limb A2 found, plus `classify_restricted` / `declares_known_grant` |
| `test_p1040.sh` | 82 assertions, no network |
| `fixtures/` | the three real payloads behind the three regressions |
| `lost-addresses.corpus-census-1381.2026-10-10.txt` | 1 381 addresses: every `github.com/owner/repo` on every page and TSV, minus GitHub's reserved namespaces and non-repository paths |
| `result.corpus.2026-10-10.tsv` | the census |
| `result.corpus-pass1/pass2.*.tsv` | the earlier runs, **kept** — the diff between them is the evidence for the three regressions |
| `lost-addresses.census-diff.2026-10-10.txt` | that diff |
| `result.unread.2026-10-10.tsv` | all 54 hand-read payloads with the line that identifies each |
| `lost-addresses.calibration-agreement.2026-10-10.txt` | the agreement against `p1029` |
| `result.types-packagist.*.tsv`, `result.packages-packagist.*.tsv` | limb B |
| `result.holder.2026-10-10.tsv` | limb C |
| `counts.txt` | the numbers above, as emitted |

## `P1034` compliance — and this instrument got it WRONG first

`p1026`'s archive census counts addresses in every tracked `.md`, `.sh`, `.py`, `.tsv` and `.txt`
file outside `archive/`, and `P1034` records that a new instrument's **input** files enter that
corpus and can silently disable it: if an archived address appears in a live worklist, `p1026` reads
it as still held and reports a loss of zero.

**This instrument was staged for commit in violation of that, and its own README asserted
compliance.** Eight files carried addresses and matched none of `p1026`'s exclusions — the worst
being a plain `corpus-addresses.2026-10-10.txt` holding **all 1 381** live addresses, which is the
single file most able to make `p1026`'s next run report `lost_total 0`.

`p1026` excludes **by filename**, not by directory: `result.*.tsv`,
`held-only-in-a-worklist.*.txt`, `lost-addresses.*.txt`, `excluded-controls.txt`. So every file here
that carries an address is now named inside one of those patterns:

| carries addresses | named |
|---|---|
| the 1 381-address census input | `lost-addresses.corpus-census-1381.2026-10-10.txt` |
| the 99-address calibration input | `lost-addresses.calibration-input-99.2026-10-10.txt` |
| limb C / A3 / lead-#3 / battery inputs | `lost-addresses.{holder-rows-11,manifest-rows-5,newaddr-rows-3,battery-rows-4}.*.txt` |
| the two prose reports that quote slugs | `lost-addresses.{census-diff,calibration-agreement}.2026-10-10.txt` |
| every result table | `result.*.tsv` |

Verified by replicating `p1026`'s own `find` and exclusion predicate — `p1026` itself cannot be run
(`Gap 383` refuses the back catalogue), so the check is re-implemented in-pass rather than invoked.
After the renaming, **16** address-carrying files fall inside the guard and **none** outside it holds
a list.

Stated precisely, because a blanket claim is what was wrong the first time: five individual
repository addresses remain cited in code comments outside the guard — `sakaiproject/sakai` in
`census.sh`, and `caviraoss/pagelm`, `dequelabs/axe-core`, `huggingface/transformers`,
`mlflow/mlflow` in `classify.sh` and `test_p1040.sh`, each naming the row that motivated a branch.
Those are **not** a `P1034` hazard and are left alone: `p1026`'s own design comment says *"Code and
TSVs count: an address cited only by an instrument is still held by this repository"*, and all five
are in fact still held. The hazard `P1034` names is a **bulk list**, which is what masks a loss
wholesale, and every bulk list here is now excluded. `counts.txt`, `census.stderr.txt` and
`fixtures/*` carry no addresses at all.

**The lesson is `P1034`'s own, arriving from the inside:** a pass that cites the principle in its
documentation has not thereby honoured it. The compliance claim is only worth the check that backs
it, and the check is one `find` away.
