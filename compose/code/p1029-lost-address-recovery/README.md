---
industry: education
region: Global
updated: 2026-10-10
---

# `p1029-lost-address-recovery` — the 68 `Gap 394` carried, probed to the payload

**Pass 104, 2026-10-10.** Closes the **measurement** limb of **`Gap 394`**.

`p1026-archive-regression-census` found that the 2026-10-06 reset dropped **82 of 681** archive
addresses and said plainly what it could not do: *"It does not check whether a lost address still
resolves."* Pass 103 probed **14**. This instrument probed **99** — the whole `LOST` list of 82 plus
the **17** of the 21 worklist-only addresses that pass 103 had not reached.

🟢 **99 of 99 measured. Nothing in `Gap 394` is now unprobed.**

## What it measures, per address

| field | how | why not the cheaper thing |
|---|---|---|
| resolves? | `git ls-remote --symref <url> HEAD` | 🔴 **Anonymous resolution only.** A private repo fails identically to a deleted one, so the class is `ABSENT`, never "deleted" |
| default ref + HEAD SHA | the `ref:` line and the `HEAD` row | 🔴 **the `HEAD` ROW, not the first row** — a repo that lists other refs first would otherwise bind the wrong SHA (test 15) |
| tags | `git ls-remote --tags`, peeled refs folded | 🔴 **`wc -l` over-counts every annotated tag by one.** `dspace/dspace`: **226 lines, 136 tags** (test 10) |
| grant | `raw.githubusercontent.com` payload read, 11 filenames in order, first 200 wins | 🔴 **A licence *name* in metadata is not a grant.** Only the payload decides (`P1005`) |
| bytes + `sha256` | of the payload actually served | 🔴 **byte count is not identity** (`P1025`) |
| **200-control** | `README.md` at the same ref | 🔴 **Without it, "no licence file" and "the raw host refused us" are ONE observation.** A row whose control is also non-200 is `LIVE-NOCONTROL` — unmeasurable, 🔴 **never reported as ungranted** |

## Result

`result.2026-10-10.tsv` — 99 rows.

| status | n | meaning |
|---|---|---|
| `LIVE` | 🟢 **68** | resolves, and a licence payload was read |
| `LIVE-NOGRANT` | 🔴 **23** | resolves, clean 200-control, **no payload at 11 filenames** |
| `LIVE-NOCONTROL` | 🟡 **3** | resolves, and the control is 404 too — **unmeasurable, not ungranted** |
| `ABSENT` | 🔴 **5** | does not resolve anonymously |

Licence families among the 68: **MIT 29 · GPL-3.0 13 · Apache-2.0 7 · AGPL-3.0 5 · CC 5 ·
unrecognised-by-pattern 4 · GPL-2.0 2 · BSD 2 · LGPL-3.0 1.** 🟢 **38 permissive, 19 of them with at
least one tag.**

## Calibration — the part that makes the other 95 rows worth reading

🟢 **The four addresses pass 103 probed were left in the input and re-measured blind. 4 of 4 agree
to the byte and to the tag.**

| slug | pass 103 recorded | pass 104 measured | |
|---|---|---|---|
| `aiverify-foundation/moonshot-cicd` | Apache-2.0 · 11 357 B · 6 tags · `main` | Apache-2.0 · 11 357 B · 6 tags · `main` | 🟢 |
| `bigbluebutton/bigbluebutton` | LGPL-3.0 · 7 652 B · 319 tags · `v3.0.x-develop` | LGPL-3.0 · 7 652 B · 319 tags · `v3.0.x-develop` | 🟢 |
| `dspace/dspace` | BSD-3-Clause · 1 504 B · 136 tags · `main` | BSD-3-Clause · 1 504 B · 136 tags · `main` | 🟢 |
| `concentricsky/badgr-server` | ABSENT | ABSENT | 🟢 |

🔵 **Two instruments, two passes, two authors, one set of numbers. That is the only reason to trust
the rows nobody has checked.**

## What the pristine reference turned out to be

🔴 **This KB has been comparing Apache-2.0 payloads against 11 357 B as "pristine". The canonical
text is 11 358 B.**

`apache-2.0-pristine.sha256.txt` records it, fetched from the publisher, not inferred:

```
cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30   11 358 B
```

🟢 **`apereo-learning-analytics-initiative/larissa` is byte-identical AND `sha256`-identical to it.**
🔵 **So the KB now has a pristine `sha256`, which `P1024` needs and a byte count cannot supply: the
11 357 B rows (`moonshot-cicd`, `fwu-kc-extensions`, `attention-monitor`) are pristine *minus a
trailing newline*, and that is a different fact from "pristine".**

## Oracles

- Licence family comes from the **operative sentence**, never a filename or a title. `classify.sh`
  is pure, sourced, and tested on its own.
- 🔴 **Ordering is the classifier's whole risk and it is tested directly:** the LGPL and AGPL texts
  both contain the string `GNU GENERAL PUBLIC LICENSE` by reference, so a plain-GPL test placed
  first mislabels both (tests 3 and 4).
- A zero-byte 200 is `EMPTY`, never a grant (test 6). A repo can serve an empty `LICENSE`.
- `CC-FAMILY` is reported as a family and never folded into permissive — `PERSUADE 2.0` is why
  (`P1007`).

## 🔴 `P1034` — this instrument's INPUT files would have disabled `p1026`

🔴 **A new instrument's inputs enter the corpus an existing instrument measures.** `p1026`'s census
asks which archive addresses appear in **no live file**. 🔴 **Committing a 99-address input list
into the live corpus would have made all 99 "live" and returned a loss of zero** — the very trap
`p1026` was built around, re-entered from outside through a *different* instrument.

🟢 **`p1026` guards by FILENAME, not directory, so the fix needed no edit to someone else's
instrument — only names its guard already catches:**

| this instrument's file | named to match | caught by `p1026` |
|---|---|---|
| `lost-addresses.input-99.2026-10-10.txt` | `lost-addresses.*.txt` | 🟢 yes |
| `lost-addresses.lost-82.2026-10-10.txt` | `lost-addresses.*.txt` | 🟢 yes |
| `held-only-in-a-worklist.unprobed-17.2026-10-10.txt` | `held-only-in-a-worklist.*.txt` | 🟢 yes |
| `result.2026-10-10.tsv` | `result.*.tsv` | 🟢 yes |
| `counts.txt` | — | 🟢 n/a, carries no addresses |

🔵 **So `P1026`'s "a worklist is not a shelf" has a second edge: a worklist is not a shelf, AND it
must not be able to pass for one.** 🟢 **Naming an output into an existing guard's pattern is the
cheapest form of instrument composition there is — and the check belongs in every pass that writes
an address list.**

## Run

```
bash test_probe.sh                                       # 18 tests, offline, fixtures only
bash probe.sh                                            # defaults to the committed 99-address input
bash probe.sh lost-addresses.input-99.2026-10-10.txt     # TSV on stdout, counts on stderr
```

## Execution record

🟢 **Executed pass 104, both limbs.** `test_probe.sh`: **18 passed, 0 failed**.
`probe.sh addresses.txt`: `live=94 absent=5 with_grant=68 no_grant=23 no_control=3`.

🔵 **`P1028` holds a second pass**: this instrument was **authored in this pass and ran**; the
repository's pre-existing instruments remain refused. The split is by authorship, not by date.

## What this instrument does NOT do

- 🔴 **It reports a DUAL-licensed payload as its first-matching family.**
  `magnusvron/llm-benchmark-quality-index` classifies `MIT` and is in fact MIT **for the code and
  separate terms for the data**. 🟢 **The tell is the byte count — 2 488 B against an MIT pristine
  of ~1 070 B — and that is `P1030`.** The 29 MIT rows were spread-checked for exactly this:
  28 fall in **1 058–1 152 B**, and the one outlier is the dual.
- 🔴 **It does not read `pom.xml`, `package.json` or SPDX metadata.** Two rows classify
  `UNRECOGNISED` and were resolved by **reading them**: both are **ECL-2.0**.
- 🔴 **It does not place a region.** Region binding stays a human act against the holder line
  (`P1012`, `P184`).
- 🔴 **It cannot distinguish deleted from private.** 5 `ABSENT` means 5 unreachable anonymously.
