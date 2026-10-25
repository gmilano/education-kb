# `p435-promotion-sweep` — `Gap 434-A` closed, and `gate-promotion`'s predicate refuted by its own population

**Pass 435, 2026-10-25.** `Gap 434-A` was registered as *"the highest-value single leg
available to `p435`"*: an online sweep running `p228-shelf-gate`'s ladder over the
unpromoted set, so `gate-promotion` would stop judging a 2 457-address surface from a
7-row grade table. 🟢 **Done — all 2 450 ungraded addresses are graded, every grant read
first-hand.** 🔴 **And the result refutes the gate's own predicate.**

## What the sweep cost and what it returned

| quantity | value |
|---|---|
| addresses probed | **2 450** |
| grant payloads read first-hand off `raw.githubusercontent.com` | **1 950** |
| `NO-GRANT` — 404 on all 8 paths × 2 refs | **500** |
| distinct licence families found | **27** |
| wall clock, `parallelism=20` | **~3 min** |
| HEAD commit objects read for the permissive arm | **1 449** (0 failures) |

    make promotion-sweep SWEEP_SLUGS=... SWEEP_WORK=...   # ONLINE: p228's ladder
    make promotion-heads SWEEP_SLUGS=... SWEEP_WORK=...   # ONLINE: the recency channel
    make promotion-recency                                # the completed table's split
    make gate-recency                                     # 18 offline controls (blocking)

Evidence: `evidence/promotion-backlog-grants.2026-10-25-p435.tsv` (2 450 rows, one per
address, with the ref, path, byte count and payload digest that produced each verdict) and
`evidence/promotion-backlog-families.2026-10-25-p435.tsv` (the family histogram).

## 🔴 The refutation: a predicate that selects 59.1 % of its population is not a detector

`p434` built `gate-promotion` on **PERMISSIVE and absent from every curated shelf**. On a
7-row grade table it fired twice and looked like a defect detector. On the complete table:

| arm | n | share |
|---|---|---|
| MIT | 1 022 | 41.7 % |
| Apache-2.0 | 330 | 13.5 % |
| BSD-3-Clause / BSD-2-Clause / ISC / CC0-1.0 / ECL-2.0 / Unlicense | 97 | 4.0 % |
| **PERMISSIVE total** | **1 449** | **59.1 %** |
| NO-GRANT | 500 | 20.4 % |
| GPL / AGPL / LGPL family | 329 | 13.4 % |
| other / unrecognised (CC-BY-NC-SA, CC-BY, PolyForm, BUSL, SSPL, MPL, EPL, EUPL, one MIT-or-GPL dual, 83 unrecognised) | 172 | 7.0 % |

🔴 **Permissiveness is this backlog's ordinary property, not a rare one.** A predicate
that selects the majority of its population is a *classifier of that population*, and
`gate-promotion`'s own README already says the verdict *"is not an instruction to shelve
it"*. Handing the complete table to the blocking arm would turn 1 449 measurements into
1 449 blocking findings, which is why this pass does **not** do that: the gate keeps its
pinned table, and the completed census is committed as evidence with a non-blocking
census target, per this base's standing distinction between a backlog and a failure.

🟢 **`p434`'s substantive conclusion survives intact** — nothing permissive was being
*hidden* by a star threshold. What did not survive is the idea that licence alone decides
a promotion.

## 🟢 The missing conjunct is RECENCY — and unlike stars, `make` can reach it

`Gap 434-B` said no star count on these shelves is reproducible from a run, and prescribed
either an `api.github.com` allowlist entry or a standing "advisory colour" rule.
🔴 **Re-measured here, the premise is wrong in a way that changes the remedy.**
`api.github.com` is **not** dead: it answers **200** on `/rate_limit` (and reports an
authenticated 15 000/h core limit) and **200** with full JSON on a repository attached to
this session. The 403 on a third-party repository is a **per-repository authorization**
refusal whose body says so in words:

    GitHub access to this repository is not enabled for this session. Use add_repo to
    request access.

🔴 **So no allowlist entry can fix it**, because the boundary is per repository and these
are 1 449 third-party repositories. `github.com` HTML (403) and `codeload.github.com`
(403) are genuinely refused; `raw.githubusercontent.com` (200), `pypi.org` (200) and git
smart-HTTP answer. 🟢 The standing rule therefore holds **more** firmly than `p434` could
show: **a star count is advisory colour, never a gate predicate** — and this pass publishes
no star column at all.

🟢 **What IS reachable, for any public address, with no credentials and no API:**

    git clone --depth 1 --bare --filter=tree:0 https://github.com/<slug>

**~0.5 s and ~270 KB per address** — against ~20 MB for a plain `--depth 1` — yielding the
HEAD commit object, hence its committer date **and** its timezone offset, which is the same
channel `gate-offset-region` already places regions with. Measured over all 1 449
permissive addresses: **1 449 dated, 0 clone failures.**

| HEAD commit age (permissive arm) | n |
|---|---|
| 0–30 d | **627** |
| 31–90 d | 233 |
| 91–180 d | 141 |
| 181–365 d | 137 |
| 1–2 y | 116 |
| > 2 y | 195 |

🔵 **This is a better discriminator than traction for this base's own stated reasons** —
`Trend 9` (a permissive licence has a shelf life) and `Trend 13` (the supply has a currency
problem) — and it is the only one of the two a `make` target can obtain.

## Reuse, not reimplementation (T108)

- the grant ladder is `p228-shelf-gate/fetch_grants.sh`, unchanged, and the family verdict
  is `p228-shelf-gate/classify_grant.py`, unchanged — this pass wrote a **runner**, not a
  classifier;
- the population and its folding are `p434-promotion-gate`'s own census functions;
- `PERMISSIVE` is **imported** from `p444-root-vs-tree-family` and control `C13` asserts
  object identity, so the two can never drift;
- both sweeps are **resumable** — a slug already in the output file is skipped — so a
  killed run continues instead of restarting.

## What this does not claim

🟡 **The recency window is a filter, not a verdict on quality.** A 0–30 d HEAD says the
project is alive; it says nothing about whether it belongs on a recommendation shelf. The
627-row slate still needed a human read, and this pass declined two of its own candidates
on exactly that ground (`arvoreeducacao/seedling`, a coding-interview sandbox, and
`CENIA-DEV/multilingual-translator-app`, a translator) — both permissive, both fresh,
neither an education component.

🟡 **The non-permissive arm is undated.** The recency sweep was run over the permissive
set only, so the 1 001 non-permissive rows carry `head_committed = -`. That is a reach
bound, stated here and in the data rather than inferred from a blank cell.
