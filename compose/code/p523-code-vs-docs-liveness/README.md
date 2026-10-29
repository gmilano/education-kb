# `p523` — code-vs-docs liveness

## Why this exists

[`agents/top.md`](../../../agents/top.md) publishes a verification table whose
liveness row reads:

| mainline freshness | `git clone --depth 1`, committer date | 🟢 authoritative |

🔴 **`microsoft/autogen` falsifies it.** On `2026-10-29` that channel answers
**one day old**: HEAD `d07c667a3239`, committer date `2026-10-28T14:45:27Z`.
The commit's subject is

> `docs: add archive caution to landing page (#8393)`

The last commit that changed code is `8544314f`, `2026-03-25` — a **217-day**
gap. The GitHub `archived` flag is **`false`**, so `archived`-based gates pass it
too, and `ls-remote` resolves it, and `updated_at` is hours old. **Every liveness
channel this base has reads LIVE on a project that spent its last three commits
telling people it is dead.**

`p518` read the posture correctly from prose and recorded it as *"IS ARCHIVED"*.
The flag contradicts that, so a later pass reading the flag reverses a correct
call — 🔵 the same shape as `p522`'s `commercial_posture` finding, one layer out
again.

## What it measures

`classify()` takes a commit list, newest first, and reports the newest commit
that touched a **non-docs** path, the gap in days, and any commit whose subject
retires the project.

| verdict | meaning |
|---|---|
| `SHIPPING` | code landed, gap `< 90 d`, no retirement notice |
| `STALE-CODE` | code landed but the gap is `≥ 90 d` |
| `NOTICES-ONLY` | HEAD is docs-only **and** the window names the project's own retirement |
| `NO-CODE-IN-WINDOW` | the window holds no code commit at all |

## 🔴 Its own first draft shipped the defect it was written to remove

`announces_retirement` matched any `archiv*`. It then graded
[`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki)
— **MIT, 4,119★** — as `NOTICES-ONLY`, on two commits from `2024-11-27` reading

> `use archive link of Chinese version of the tutorial`

🔵 **That is an archived URL for a tutorial, not a retired project.** The false
verdict would have kept a 4,119-star permissive asset off the shelf — the
*opposite* direction from `p520`/`p522`'s false-permissive reads, and the same
class: a probe written against one failure producing the mirror failure.

Both commits are **permanent negative controls** in the suite. The tightened
matcher removed **5** false retirement notices across the population
(`canyongbs/advisingapp` 4 → 0, `oat-sa/tao-core` 1 → 0) and kept **all 3** true
ones on `autogen`.

## Run it

```sh
python3 -I test_code_liveness.py          # 38 checks, offline, no network
python3 -I code_liveness.py <owner/repo>…  # clones blobless, reads 60 commits
```

The suite is offline: every fixture is a commit list, either read from bytes on
`2026-10-29` or written as a control. `measure()` is the only function that
touches the network.

## Population, `2026-10-29`

[`population.2026-10-29-p523.txt`](population.2026-10-29-p523.txt) — 20 rows off
this base's own shelves: **17 `SHIPPING`, 2 `STALE-CODE`, 1 `NOTICES-ONLY`**.

🔴 The two `STALE-CODE` rows are both published rows:

- `gongfuxiang/schoolcms` — HEAD `2020-04-22`, last code `2019-10-22`. One
  branch, and HEAD *is* that 2020 commit. The API's `updated_at` reads
  `2026-10-15T14:30:50Z`: a **2 367-day** error, on a row
  [`verticals/solutions.md`](../../../verticals/solutions.md) sells.
- `open-spaced-repetition/fsrs4anki` — **340 d**. The live FSRS code is
  `fsrs-rs` (BSD-3-Clause, 6-day gap) and `ankitects/anki` (0 d), not here.

## Limits, stated

- 🔴 A 60-commit window. A repository that merges squashed release commits can
  hide a code change outside it; the verdict then reads `NO-CODE-IN-WINDOW`,
  which is *unread*, not *dead*.
- 🔴 `DOCS_RE` is deliberately conservative, so a repository whose product **is**
  prose (a curriculum, a skills pack) reads `NOTICES-ONLY`/`STALE-CODE` when it
  is shipping normally. Do not point this at `anthropics/k12-teacher-skills`-shaped
  rows without reading the verdict's subject lines.
- 🔵 It cannot see work on non-default branches. `ls-remote` can; use both.
