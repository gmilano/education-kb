---
industry: education
region: Global
updated: 2026-10-11
---

## 🟢 Pass 118 — 2026-10-11 (fifth pass of this date), 03:4x–04:2x UTC

🔵 **APPEND-ONLY page. This section is added above p117's and nothing below it is edited.**

🔴 **What is new this week is not an agent. It is that eight of the thirteen agents on this KB's
shelf were under the wrong licence, and the sweep that found it ran on a channel this page had
already recorded as working.** `ACTION E` discharged: 957 licence claims, 249 addresses,
249/249 measured from the DEFAULT branch, **18 wrong licences, 38 published cells repaired**.

### 🟢 Agents — star counts and recency read from the API this pass, not carried

🔵 **Channel: the MCP relay's `/search/repositories` endpoint. `P118-A` corrects p117 here — the
`/repos/{owner}/{repo}` endpoint is refused on ALL THREE transports, and it is the SEARCH endpoint
that answers. p117 read "three transports, three outcomes" where the real structure is a
transport × endpoint matrix.**

| agent | ★ this pass | p117 | Δ | last push | licence, from the tree |
|---|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **41 103** | 41 100 | 🟢 +3 | 2026-10-11 | 🟢 Apache-2.0 |
| [`frappe/frappe`](https://github.com/frappe/frappe) | **10 913** | — | 🆕 | 2026-10-11 | 🟢 **MIT** ⚠️ was GPL-3.0 |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | **2 335** | — | 🆕 | 2026-10-10 | 🔴 **AGPL-3.0** ⚠️ was Apache-2.0 |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | **931** | — | 🆕 | 🔴 **2026-02-20** | 🔴 **GPL-3.0** ⚠️ was MIT |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | **389** | 389 | ⏸️ 0 | 2026-10-06 | 🟢 MIT |
| [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | **253** | — | 🆕 | 🟡 2026-08-14 | 🔴 **GPL-3.0** ⚠️ was Apache-2.0, p117 said AGPL-3.0 |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **92** | — | 🆕 | 2026-10-10 | 🟢 **MIT** ⚠️ was Apache-2.0 |
| [`Tadreeb-LMS/tadreeblms`](https://github.com/Tadreeb-LMS/tadreeblms) | **34** | — | 🆕 | 2026-10-06 | 🔴 **AGPL-3.0** ⚠️ was GPL-3 |
| [`FWU-DE/ais-chat`](https://github.com/FWU-DE/ais-chat) | **25** | — | 🆕 | 2026-10-10 | 🔴 **AGPL-3.0** ⚠️ was MIT |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **17** | — | 🆕 | 2026-10-08 | 🟢 **MIT** ⚠️ was Apache-2.0 |

🟡 **`DeepTutor` +3 stars in the ~75 minutes between p117's census and this one.** 🔵 It remains
this KB's largest education-specific agent by an order of magnitude, and `educhain` is flat at the
389 p117 corrected it to from a published "~12k".

🔴 **The recency finding worth carrying forward: [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt)
— the theory-of-mind tutor this KB has recommended across several passes — has not been pushed
since 2026-02-20, EIGHT MONTHS, and is GPL-3.0 rather than the MIT every roundup still reports.
Stale and copyleft is the worst pair for a recommendation shelf.** 🟡 `elmsln/elmsln` is also
drifting: last push 2026-08-14, and the API reports `has_issues: false` — the project has turned
off its own issue tracker.

### 🟢 Canonical spellings corrected this pass

🔵 **Three addresses this page has been citing under a non-canonical spelling, resolved by the API
and by `git ls-remote` agreeing:**

| cited here as | canonical | note |
|---|---|---|
| `fwu-de/ais-chat` | **`FWU-DE/ais-chat`** | case only |
| `tadreeb-lms/tadreeblms` | **`Tadreeb-LMS/tadreeblms`** | case only |
| `elgg/elgg` | **`Elgg/Elgg`** | case only; both resolve to default branch `7.x` |

🔵 **`Gap 408`'s shape again: one entity under two spellings makes every later cross-reference
ambiguous.** Recorded here rather than rewritten into the history below.

### 🔴 What the mandated searches added to this page this pass: nothing

🔵 **`github trending education AI 2026` and `top open source AI agents education 2026 github MIT`
both ran. Every address they surfaced is already held** — `rohitg00/ai-engineering-from-scratch`,
`microsoft/generative-ai-for-beginners`, `ashishpatel26/500-AI-Agents-Projects`,
`awesome-ai-agents-2026`, `HKUDS/DeepTutor`, `satvik314/educhain`,
`microsoft/ai-agents-for-beginners`. 🟡 **Neither search returned a live GitHub Trending page;
both returned third-party trackers and roundup blogs, and one of those roundups is the source of
the "tutor-gpt is MIT" claim this pass refuted from the tree.**

🔴 **Zero new addresses. `Gap 402` weakens a third consecutive pass.** Stated, because silence
here would look exactly like coverage.

