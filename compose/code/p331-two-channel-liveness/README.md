---
industry: education
region: Global
updated: 2026-10-20
---

# `p331-two-channel-liveness` — making pass 24's rule executable (pass 331 of 2026-10-20)

## Why this exists

🟢 **Pass 24 built `registry-recency-channel` and wrote the rule down:**

> citing tier → head commit date → *any* commit, including a typo fix in a README
> installed tier → latest release upload → a **deliberate publication**
> ⚠️ **The two numbers are not interchangeable, and no claim may treat them as one series.**

🔴 **Pass 329 then opened the `git` channel, pass 330 built the `(commits, authors, last_commit)`
triple on it, and both re-graded this KB's entire shelf for aliveness on the citing channel
alone.** The rule was correct, written, and in this repository the whole time. **Nothing executed it.**

🔴 **The cost, measured at p331:** `Cvmcosta/ltijs` — a row this KB marks 🟢 *Recommended* — was
mis-gradeable as abandoned by 2.4 years.

| repo | citing channel | installed channel | single-channel verdict | truth |
|---|---|---|---|---|
| `Cvmcosta/ltijs` | newest tag **v5.9.5, 2024-05-01** | **`ltijs` 7.0.7, 2026-10-06** | 🔴 *"abandoned 2.4 years"* | 🟢 **ALIVE** |
| `dmitry-viskov/pylti1.3` | 2022-11-21 | **`PyLTI1p3` 2.0.0, 2022-11-20** | DEAD | 🟢 **DEAD** |

🔵 **One method called both repositories abandoned. It was wrong about the first by two and a half
years and right about the second to the day — and it had no way to tell which was which.** That is
the dissociation this module is built to catch.

## What it does

| function | channel | answers |
|---|---|---|
| `git_head_date(slug)` | `git ls-remote` | does the slug resolve at all? |
| `registry_release(pkg, registry)` | `registry.npmjs.org` / `pypi.org` | what was the last **deliberate publication**, and when? |
| `verdict(...)` | both | a liveness grade — **or `UNPUBLISHED`** when a row resolves on git and is absent from the registry it claims to ship to |
| `gate(rows)` | — | 🟢 **refuses a shelf write**: returns every packaged row carrying only one channel |

🟢 **`gate()` is the part that matters.** The prose rule has been ignored for 307 passes because
prose cannot refuse a write. **`gate()` returns a non-empty list and the caller stops.**

## The three cases it separates

- 🟢 **Packaged, two channels** → graded. `GRADED:7.0.7@2026-10-06`
- 🔴 **Packaged, registry absent** → `UNPUBLISHED`, **not** `NO-REF` and **not** "alive". This is
  `Liberate-Labs/ltikit-sdk`: 38 commits, 1 author, **no npm package**. A client's build cannot
  install it, which is the axis that matters, and the git channel alone calls it healthy.
- 🟢 **Unpackaged** → `ALIVE-CITING-ONLY` is a **legitimate** single-channel grade. `os-taxonomy`
  ships no package; demanding a release date from it would be the opposite error.

## Tests

`test_two_channel.py` — **11 tests, all passing offline**, channels injected so the gate is
testable without the network. 🟢 **They are discrimination tests, not smoke tests:** the central
one, `test_the_two_are_distinguishable`, asserts that `ltijs` and `pylti1.3` receive **different**
verdicts from the same call — the exact property the single-channel method lacked.

```
$ python3 test_two_channel.py
Ran 11 tests in 0.243s
OK
```

🔴 **Known limit, stated so no pass re-derives it:** star and fork counts remain unmeasurable.
`api.github.com` has returned 403 since p37, and this session's `mcp__github__*` tools — the first
time this KB has had them — **refuse every repository not attached to the session**
(*"Allowed repositories: gmilano/globant-kb, gmilano/education-kb"*). 🔵 **Those are two different
refusals with two different causes and must not be recorded as one blocked channel.** This module
grades **liveness**, never popularity.
