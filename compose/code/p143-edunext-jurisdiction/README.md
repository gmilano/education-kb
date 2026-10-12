---
industry: education
region: LATAM
updated: 2026-10-12
---

# `p143-edunext-jurisdiction` — `ACTION DJ`: eduNEXT is LATAM, and the pooled test was the wrong unit

🟢 **Falsifier silent, and the row is booked on affirmative evidence rather than on `.co`.**
`eduNEXT` moves from `UNVERIFIED_JURISDICTION` to **LATAM (Colombia)**.

## What was registered

> 🟡 **`ACTION DJ`** — establish eduNEXT's jurisdiction from a readable channel: commit
> offsets across `eduNEXT/*` repositories, or a package the company publishes.
> 🔴 **Refuted if the offsets across eduNEXT's own repositories are not predominantly
> `-0500`** — which would mean the `.co` reading is wrong and the row must stay unplaced.

## Why the row was held

`openedx/openedx-filters` (AGPL-3.0-or-later) names eduNEXT as author of record, set
2026-10-02 during the `modernize` campaign. 🔴 **`.co` is Colombia's ccTLD *and* a generic
registration**, and `edunext.co` is unreachable from this environment — so p142 declined to
book it.

## Population

5 repositories, **1 485 commits**, **63 distinct authors**. Full history, `git clone`.

| repo | commits | dominant offset |
|---|---|---|
| `eduNEXT/eox-core` | 751 | `-0500` (451) |
| `eduNEXT/eox-tenant` | 458 | `-0500` (298) |
| `eduNEXT/eox-theming` | 134 | `-0500` (68) |
| `eduNEXT/eox-audit-model` | 102 | `-0500` (57) |
| `eduNEXT/picasso` | 40 | `-0500` (22) |

🟢 **`-0500` is the dominant offset in 5 of 5.** The falsifier as written does not fire.

## 🔴 And "`-0500` is dominant" is not sufficient, for a reason in the same data

`-0500` is Colombia (COT) **and** US Eastern Standard Time. The pooled offsets carry a
large `-0400` population alongside, which is what EST/EDT looks like. So the real question
is not which bucket is biggest but 🔴 **whether the `-0400` sits in the daylight-saving
window.**

🔴 **Pooled, the answer is unreadable** — `pooled-dst.2026-10-12-p143.tsv` returns
`MIXED` on 5 of 5: both offsets appear both inside and outside the DST window.

| pooled | count |
|---|---|
| `-0500` total | 896 |
| `-0400` total | 446 |
| `-0400` inside DST (Apr–Oct) | 271 |
| 🔴 `-0400` **outside** DST (Jan, Feb, Dec) | **102** |
| 🔴 `-0500` **inside** DST (Apr–Oct) | **596** |

🔵 **Pooling was the wrong unit.** A repository's commits come from many people, and two
zones pool into exactly the shape one ambiguous zone would.

## 🟢 The author is the unit that carries a timezone

For each author, the offset *set* across the DST boundary is decisive, because the two
candidate zones differ in whether they move:

* **Colombia, Peru, Ecuador** — `-0500` year round. No DST since 1993.
* **US Eastern** — `-0500` in January, `-0400` in July.
* **US Central** — `-0600` in January, `-0500` in July.

🔴 **So a single offset places nothing, and the BOTH-WINDOWS condition is what closes it:**
`-0500` in January rules out US Central; `-0500` in July rules out US Eastern. Only an
author satisfying both is booked.

| author class | authors | commits |
|---|---|---|
| 🟢 **`-0500` in both windows, never `-0400`** — a non-DST `-0500` zone | **13** | **491** |
| 🔴 US Eastern DST shape (`-0400` in summer, `-0500` in winter) | **2** | **28** |
| `-0400` in both windows, never `-0500` — a non-DST `-0400` zone (Venezuela, Bolivia) | 3 | 201 |
| `-0500`, one window only — undetermined | 15 | — |
| `-0400`, one window only — undetermined | 5 | — |
| mixed multi-zone (travel, CI, relocation) | 9 | — |
| not an American offset | 16 | — |

🟢 **13 authors against 2.** The US Eastern reading accounts for **1.9%** of commits.

## The corroboration that does not come from offsets at all

🟢 **`edunext.co` is the author mail domain on 998 of 1 485 commits (67%)** — the company's
own domain, and **6 of the 13 year-round `-0500` authors** carry it (315 commits). The
`.co` string and the offset channel are therefore not one piece of evidence counted twice:
one is a registration, the other is 491 commits of human working hours.

🔵 **Only mail DOMAINS are published here, never addresses.** The jurisdiction question is
about the organisation; a contributor's personal address is not this KB's to post.

## Verdict, with its residual stated

🟢 **eduNEXT books LATAM.** 🔴 **The offset channel does not separate Colombia from Peru or
Ecuador** — all three are `-0500` year round. Colombia is the reading because `edunext.co`
is the company's own domain and `.co` is Colombia's ccTLD; 🔵 **the *region* field, which is
the closed vocabulary the compiler reads, is determined either way.**

🔴 **What would overturn it:** evidence that the year-round `-0500` cohort is Peruvian or
Ecuadorean, which would keep the row LATAM and change only the country. 🔵 **Nothing
available here would move it out of LATAM**, and that is the claim being published.

## Run it

```
python3 -I dstsplit.py   name=path [...]    # pooled-dst.2026-10-12-p143.tsv
python3 -I authorzone.py name=path [...]    # per-author.2026-10-12-p143.tsv
```

🔵 **Boundary months March and November are reported separately and never forced** — US DST
runs from the second Sunday in March to the first Sunday in November, and whole-month
buckets cannot resolve a transition week.
