# `p255-channel-reachability` — `ACTION YE`

**The question:** a channel answered `403`. Will it answer later?

`ACTION YE` (p254) asked for the `(channel × transport)` table to become *"a standing
instrument that a pass RUNS rather than retypes"*. 🔵 A table of statuses cannot be
standing — it is stale the hour it is written. What is standing is the **rule a pass
applies to a status**, and that rule is the thing p254 got wrong.

## What p254 published, and what p255 measured

p254 retracted the sixteen-pass `403` wall and replaced it, in the same pass, with a new
rule:

> Treat a `403` from this channel as *budget exhausted* until `rate_limit` says otherwise.

🔴 **p255 measured the stated condition and it fails.**

| | |
|---|---|
| `api.github.com/rate_limit` via WebFetch | `core` `limit 60`, **`remaining 51`**, `used 9` |
| four `api.github.com/repos/{slug}` via WebFetch, same minute | **`403` × 4** |
| `rate_limit` re-read immediately after | `remaining 51`, `used 9` — 🔴 **the four calls billed nothing** |
| `api.github.com/search/repositories` via WebFetch, same window | 🟢 **`200`** |

**A denial that does not bill is not a budget.** And on the other transport the same shape
appears with the opposite identity: `curl` through the session proxy is *authenticated*
(`core` `limit 15000`, `remaining 14996`) and is refused on every out-of-scope path —
including the static `/licenses/mit`, which has no repository in it at all.

🟢 **So neither the host nor the transport is the discriminator. Two different mechanisms
are in play at once:**

| transport | identity | what limits it | shape of the refusal |
|---|---|---|---|
| `curl` (session proxy) | 🟢 authenticated, `15 000`/h | a **repository-scope allow-list** | every out-of-scope path, meter untouched |
| `WebFetch` | 🔴 unauthenticated, `60`/h core + `10`/h search | an **endpoint allow-list** | `/search/*` answers, `/repos/*` does not |

🔴 **Neither transport alone can read an arbitrary repository's metadata, and neither can
both together.** That is why a star cell is `UNMEASURABLE` here by `/repos/{slug}` — and
why the **search endpoint is the only star channel this base has**, since it returns
`stargazers_count` for up to `100` repositories per call.

## The rule

| status | meter | sibling on same host+transport | verdict |
|---|---|---|---|
| `2xx`/`3xx` | — | — | `OPEN` |
| refusal | `> 0` | — | 🟢 **`POLICY-DENIED`** |
| refusal | `0` | — | `BUDGET-EXHAUSTED` |
| refusal | unread | answered `200` | 🟢 **`POLICY-DENIED`** |
| refusal | unread | unknown | 🟡 **`INDETERMINATE`** |
| `0` (CONNECT never reached the origin) | — | — | `POLICY-DENIED` |

🔵 **`INDETERMINATE` is the state p254 was actually in**, and naming it is most of the
value: only `BUDGET-EXHAUSTED` comes back on its own, so `is_retryable_later()` is false
for everything else. A pass that records a policy denial as a budget re-probes it forever;
a pass that records a budget as a wall builds an architecture around its absence. **This
base has now done both, one pass apart.**

## Controls

`47`, `0` failing. `measured.2026-10-16-p255.tsv` pins all `20` of this pass's measurements
and every row is replayed through the rule, so the table and the rule cannot drift.

🔴 **The adversarial control is the one that matters:** p254's own published row
*(`/repos/{slug}` on WebFetch, `403`, no meter reading)* must grade `INDETERMINATE` and
`unsound_budget_claim()` must return `True` for it. If this suite ever blesses that row,
the instrument has inherited the defect it was built to catch.

🟢 **Proven able to fail.** Reverting the discriminator to p254's rule in a throwaway copy
produces **`15` failures and exit `1`**.
