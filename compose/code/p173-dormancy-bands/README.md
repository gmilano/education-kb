---
industry: education
region: Global
updated: 2026-10-13
---

# `p173-dormancy-bands` — dormancy without `api.github.com`, and the denominator question it answers on the way

**Pass 173, 2026-10-13. `ACTION JV` (`gap 121` / `T242`) and the second limb of `ACTION JW`
(`gap 122` / `T238`).**

## The method, and why it needs no API

`ACTION JV` asked for the distribution of days-since-last-commit over the `135` repositories of
`topic:ai-education pushed:>=2026-04-16 license:mit`, and registered a falsifier for the case where
the measurement *"cannot be taken without `api.github.com`"*.

It can. **Band the population by re-running the same query with a moving `pushed:>=` bound** and
subtract. Four queries, four counts, no enumeration, no API, and every string written down:

| query | count | dormant at that band | % of `135` |
|---|---|---|---|
| `… pushed:>=2026-04-16 license:mit` *(the `180`-day bar)* | `135` | — | — |
| `… pushed:>=2026-09-13 license:mit` *(`30` d)* | `39` | 🔴 **`96`** | 🔴 **`71.1%`** |
| `… pushed:>=2026-08-14 license:mit` *(`60` d)* | `71` | 🔴 **`64`** | 🔴 **`47.4%`** |
| `… pushed:>=2026-07-15 license:mit` *(`90` d)* | `101` | 🔴 **`34`** | 🔴 **`25.2%`** |

🔴 **Falsifier limb 1 SILENT at `25.2%` dormant at `90` days.** The bar is wrong and
`codementor-ai-platform` is not an outlier: **one in four** of the `135` has not been pushed to in
three months, and **seven in ten** not in a month. 🟢 **Limb 2 SILENT: taken with no API call.**

## What this measures, stated because it is not what the action asked

`pushed:` is **push** recency. The action asked for **commit** recency. They are different fields
and the whole reason `T242` exists is that a repository can satisfy one and fail the other. The
subsample where this pass has **both** is in
[`evidence/commit-date-sample.2026-10-13-p173.tsv`](../../evidence/commit-date-sample.2026-10-13-p173.tsv):
the `5` named members of the `≥20`★ head, read with
`git clone --depth 1 --filter=blob:none --no-checkout` + `git log -1 --format=%cI`.

**So the band figures are a LOWER BOUND on commit dormancy, never an upper one** — a push can be a
tag, a merge or a branch nobody develops on, and all three keep a dead default branch inside the
band. Report them as *"not pushed to in N days"* and not as *"not worked on"*.

## The finding nobody registered: the topic's star head is deader than the shelf

| population | rows | dormant ≥`30` d by COMMIT | dormant ≥`60` d |
|---|---|---|---|
| 🔴 the `≥20`★ head OF the `135` | `5` | 🔴 **`3`** | 🔴 **`3`** |
| 🟢 shelf rows sampled *(not in the `135` — `T238`)* | `5` | 🟢 **`0`** | 🟢 **`0`** |

🔴 **`T253` — the denominator is not merely the wrong size, it points the wrong way on liveness.**
The repositories this KB **routes** committed `0`, `1`, `3`, `4` and `22` days before this pass.
The repositories the `ai-education` topic **puts at its top by stars** sit at `14`, `18`, `79`,
`85` and `88`. A client shown *"the vertical's leading permissive projects"* from the topic head
would be shown three projects nobody has touched since July.

## The denominator, measured (`ACTION JW`, second limb)

`ACTION JW` asked what population the `485` / `357` / `135` figures actually describe. They describe
**repositories that tag themselves `ai-education`** — and `1` of this KB's `12` shelf rows does.
Same filters, different topic:

| query | count | ratio to `135` |
|---|---|---|
| `topic:ai-education pushed:>=2026-04-16 license:mit` | `135` | `1×` |
| 🔴 `topic:education pushed:>=2026-04-16 license:mit` | 🔴 **`8.2k`** | 🔴 **~`61×`** |
| 🔴 `topic:edtech pushed:>=2026-04-16 license:mit` | 🔴 **`1.3k`** | ~`10×` |
| `topic:ai-tutor pushed:>=2026-04-16` *(no licence filter)* | `581` | ~`4×` |

🆕 🔴 **`T252` — and this channel ROUNDS above `1 000`.** It returned *"8.2k"* and *"1.3k"*, not
`8 214` and `1 307`. `T227` says record the query string; this adds: **record the channel's
precision, because a four-figure count from the rendered page is an order of magnitude and not a
count.** Every exact figure this KB holds — `485`, `357`, `135`, `101`, `71`, `39`, `29`, `14`, `5`,
`0` — is exact *because it is under `1 000`*, which is luck and not method.

## Re-run it

The eight strings are in `queries.txt`, verbatim. Fetch each as
`https://github.com/search?q=<urlencoded>&type=repositories` and read the *"N results"* header.
`curl` on `github.com` is `403` from this container; the rendered-page channel is the one that
answers.
