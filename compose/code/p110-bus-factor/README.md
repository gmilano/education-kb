# p110-bus-factor — contributor concentration over the shelf

**Pass 110, 2026-10-10.** `test_p110.sh` → **46 passed / 0 failed**, fully offline
(real git repositories served over `file://`; no mocks, no network).
`busfactor.sh` read **296 of 296** shelf addresses in 3 m 48 s, `rc=0` on every one,
**zero unread**.

## The question

Three passes have measured this shelf's maintenance and none of them can answer the
question an engagement asks next.

| pass | axis | answers | cannot say |
|---|---|---|---|
| p107 | tag **count** | how much ref traffic | inverts at the top of the shelf |
| p108 | release **identity** | *can I pin it* | whether the pin is from 2019 |
| p109 | commit **recency** | *is it alive* | **who is keeping it alive** |
| **p110** | author **concentration** | **what happens if they stop** | how good the code is |

A repo can be flawless semver, Apache-2.0, pinnable, and committed to this morning —
and be one unpaid human. p109 graded exactly such rows 🟢 `fresh` and reported nothing
wrong, because liveness is a property of the history and this is a property of the
*bench*.

## What it emits

Ten columns, one row per address:

```
slug  rc  commits_read  bots_stripped  authors_email  authors_name
      top_author_share  bus_factor  committer_bus_factor  band
```

`bus_factor` is the **fewest authors whose commits exceed 50 %** of the window.
`band` is `solo` (1) · `pair` (2) · `small` (3–5) · `broad` (≥6), or
`UNREAD` / `EMPTY` / `BOTONLY`.

## Channel

Anonymous git lane only, re-probed live this pass:

| endpoint | result |
|---|---|
| `git ls-remote` / `git fetch` | `rc=0` |
| `raw.githubusercontent.com` | `200` |
| `api.github.com` | `403` (`P107-A`, session scoping) |

So `/contributors` cannot be read. Authorship comes from the commit objects: a
depth-limited, blob-filtered fetch, then `git log`.

## Six disciplines, each of which a draft of this script got wrong

- **`P110-A` merge commits are excluded (`--no-merges`).** On a PR-merge workflow the
  maintainer authors every merge commit — one commit per PR credited to the person who
  merged it and none to the person who wrote it.
- **`P110-B` author identity, not committer (`%aE`, not `%cE`).** This **inverts p109's
  choice for a principled reason**: p109 asked *when was this history written* (committer
  date is correct); p110 asks *who wrote the code*. Under "Squash and merge" or "Rebase
  and merge" GitHub rewrites the committer to whoever clicked the button.
- **`P110-C` bots are not contributors.** Stripped before any arithmetic and **counted**,
  so the stripping is auditable rather than silent.
- **`P110-D` this is a window, not a history.** And `--depth` is a **generation** limit,
  not a commit count: `--depth=200` yielded 200 commits on `UniTime/unitime` and 8 374 on
  `moodle/moodle`, because each generation of a merge-heavy history can branch. The
  windows are therefore **not comparable in size**, which is why `commits_read` is
  load-bearing output and not diagnostics.
- **`P110-E` email is the key, name is the cross-check.** Email is lower-cased (Git
  preserves case). Distinct names are emitted beside distinct emails: when names <
  emails one human holds several addresses and the email count **overstates** the bench.
- **`P110-F` `users.noreply.github.com` is a HUMAN.** A draft stripped
  `/noreply@github\.com$/` as a bot pattern. That address is GitHub's **default privacy
  email**, so the regex silently deleted real contributors — hardest on the most
  privacy-conscious ones. Only the exact machine forms `noreply@github.com` and
  `web-flow@users.noreply.github.com` are stripped.

`P1040` is honoured: `rc!=0` emits `UNREAD` with **blank** metrics. A fetch failure must
never be arithmetically indistinguishable from a genuinely solo repo.

## The two measurement flags are not reporting modes

`P110_MERGES=1` and `P110_BOTS_KEEP=1` exist **only** so `P110-A` and `P110-C` can be
measured on this shelf instead of asserted from first principles. No reported figure
comes from either.

That measurement overturned the hypothesis the script was written on. A draft of the
test suite asserted that counting merges always reads **more** concentrated. It is
false, and this shelf falsifies it in both directions:

| | clean | distorted | direction |
|---|---|---|---|
| `moodle/moodle`, merges kept | `broad`/9 | `small`/5 | understates the bench by 4 |
| `pr-merge` fixture, merges kept | `pair`/2 | `small`/3 | overstates it by 1 |
| `langchain-ai/langgraph`, bots kept | `small`/3 | `solo`/1 | concentrates |
| `jupyterhub/jupyterhub`, bots kept | `solo`/1 | `pair`/2 | hides a solo human |

Both filters inflate the top contributor's **share** (which concentrates) *and* add a
pseudo-author (which disperses); which effect wins depends on the shape of the history.
So `--no-merges` and bot-stripping are **not bias corrections in a known direction** —
they are correctness requirements. Without them the figure is wrong in a direction you
cannot predict, which is worse than wrong in a known one, because you cannot adjust for it.

Measured on the real shelf: **29 of the 98 bot-carrying rows** change band or bus factor
when bots are kept (20 disperse, 9 concentrate).

## Reproducing

```sh
./test_p110.sh                      # 46/46, offline, no network
./busfactor.sh addresses.txt        # the census -> result.<date>.tsv
P110_DEPTH=500 ./busfactor.sh       # widen the window
```

## Known limits

- The window is recent history. A repo with a broad past and a solo present reads
  `solo` — the correct answer to the engagement question, but **not** the claim "only
  one person ever worked on it".
- `bus_factor` counts commits, not their weight. One author of 51 % of small commits
  outranks a reviewer who shaped the architecture.
- `authors_email` cannot see that two addresses are one human unless the name matches;
  `P110-E` detects the discrepancy but does not resolve it. 158 of 296 rows show
  name/email counts that disagree.
- `EMPTY` is unreachable for any repo that fetches at all, because a root commit can
  never be a merge. It stays as a guard.
