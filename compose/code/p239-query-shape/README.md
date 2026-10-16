# `p239-query-shape` — the predicate `238` passes of query evidence never recorded

**Why this exists.** `p237` moved supply discovery to the GitHub REST search channel.
`p238` found that channel's `license:` filter **admits a download-lure farm** and built
[`p238-lure-signature`](../p238-lure-signature/) against the lures. `p239` measures what
both passes left out of every one of their evidence tables: **the sort key.**

🔴 **Measured on this KB's own evidence directory: `0` of `20` `*queries*.tsv` files
record a sort key.** Not one. The channel was audited for a pass and a half; the
parameter that decides whether its output is a sample was never written down.

## What was measured

Six harvests this pass, on-topic rate of page one (education vocabulary over name +
description), recorded in
[`evidence/p239-query-shape.2026-10-16-p239.tsv`](../../../evidence/p239-query-shape.2026-10-16-p239.tsv):

| `total_count` | sort | page | on-topic | verdict |
|---|---|---|---|---|
| `24` | `updated` | 24 | 🟢 **`91.7`%** | `SCOPED` — `org:Ed-Fi-Alliance-OSS` |
| `253` | `updated` | 30 | 🟢 `63.3`% | `SAMPLE` |
| `2 326` | `updated` | 40 | 🔴 **`2.5`%** | `SLICE` |
| `7 576` | **`stars`** | 50 | 🟡 **`48.0`%** | `HEAD` |
| `8 618` | `updated` | 30 | 🔴 **`0.0`%** | `SLICE` |
| `81 905` | `updated` | 40 | 🔴 **`0.0`%** | `SLICE` |

🔵 **The discriminator is not breadth. It is breadth interacting with a RECENCY SORT.**
`7 576` results sorted by stars returned `48`% on-topic; `8 618` sorted by `updated`
returned `0`%. **Comparable breadth, a `48`-point swing, attributable to the sort key
alone.**

Why: over a large result set `sort:updated` ranks by **last push**, so page one selects
for push **frequency**. What pushes most often is not what is most relevant — it is
bot-refreshed job boards, trending-trackers, VPN subscription lists and freshly minted
lure repositories. 🔴 **Relevance is not in the ordering at all.**

## It re-attributes `p238`'s headline

`p238` concluded that its `license:mit` filter admits the lure farm. 🟢 **The filter does
admit it.** 🔴 **But the filter is not what put it on page one.** Same query, same
`total_count` (`10 815`), same day, sort key the only difference:

| sort | release-channel names on page one |
|---|---|
| `stars` | 🟢 **`0` of `30`** |
| `updated` | 🔴 **`3` of `30`**, including [`pewcrusher-1922/Jclic-Full-Version`](https://github.com/pewcrusher-1922/Jclic-Full-Version) — a brand `p238` never saw |

🟡 **`p238`'s gate is still needed** — `sort:updated` is the natural choice for *"what is
new this week"*, and `agents/trending.md` cannot be filled any other way. 🔵 **But the
cheapest mitigation for the same farm is one parameter, not four predicates.**

## Three axes, which the controls forced apart

An early version of this gate refused `HEAD` as un-harvestable. 🔴 **A control anchored
on the `48`% measurement rejected it** — that harvest supplied six of this pass's rows
(`PowerSchool-API`, `PyPowerSchool`, `clever-go`, `LMS-Toolkit`, plus two withheld as
non-permissive). 🟢 **So the question splits:**

| | `SCOPED` | `SAMPLE` | `NARROW` | `HEAD` | `SLICE` |
|---|---|---|---|---|---|
| `is_harvestable` — may supply published rows | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| `supports_absence` — may ground *"there is no X"* | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |
| `supports_recency` — may fill a `trending` shelf | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |

🔵 **`supports_absence` has a counter-example in this KB's own history.** `p238` ran the
`FERPA OR COPPA` query and recorded *"`0` North America education agents"*. At `stars`
page one is awesome-lists and CS curricula, which would support the same absence; at
`updated` it is the lure farm, which would also support it. 🟢 **`p239` then published
`16` permissive North America rows by SCOPING the query instead.** The absence was an
artefact of the harvest's shape, at both sort keys.

## The remedy the gate names

🟢 **Scope the query; do not sort your way out of a broad one.** The one scoped harvest
this pass ran returned the highest on-topic rate of the six (`91.7`%) — and `org:`,
`topic:`, `user:` and `repo:` make a query a sample of a namespace at **any**
`total_count`, which is why `SCOPED` has no threshold.

## Usage

```bash
python3 -I compose/code/p239-query-shape/query_shape.py <total_count> [sort] [query]
python3 -I compose/code/p239-query-shape/test_query_shape.py   # 70 controls
make gate-offline                                              # standing check
```

Exit `0` when the shape may supply rows, `1` otherwise. No network — it classifies a
query's shape **before the query is spent**. Runs from its own directory and under `-I`
from the repository root (`p355-cwd-portability`).

## Thresholds, and what sets them

`CAUTION_MAX = 253` is the **last count measured to still work**; `REFUSE_MIN = 2326` is
the **first measured to fail**. 🟡 They are observations, not round numbers, and the
boundary is genuinely unknown inside `(253, 2326]` — `NARROW` is that interval, and it
is harvestable but may not ground an absence.

## What it does not do

🔴 It cannot see a query whose *terms* are wrong; a perfectly shaped harvest of the wrong
vocabulary is still `SAMPLE`. 🔴 It reads `total_count`, which GitHub caps and estimates
above `1 000`, so the thresholds rest on a number the API itself rounds. 🟡 **`ACTION VK`:
the `(253, 2326]` interval wants one harvest at `~800` and one at `~1 500` to close it.**
