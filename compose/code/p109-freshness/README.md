# `p109-freshness` — is the shelf ALIVE?

**Pass 109, 2026-10-10.** Third axis added to the shelf in three passes, and the
one `Gap 376` actually asked for when it was opened at pass 92.

## The question, and why the two previous answers missed it

| pass | axis | question it answers | what it cannot say |
|---|---|---|---|
| p107 | tag **count** | how much ref traffic | nothing — it inverts (`4 468` tags, never a release) |
| p108 | release **identity** | *can I pin it* | whether the thing you pin is from 2019 |
| p109 | commit **recency** | **is it alive** | how good it is |

A row can be flawless semver, Apache-2.0, and five years dead. p108 would rank
it `semver` / pinnable and say nothing was wrong. That is the gap this closes.

## Channel

Anonymous git lane only. Probed live at the start of this pass:

```
git ls-remote / git fetch      rc=0    <- the only lane that works
raw.githubusercontent.com      200
api.github.com                 403     P107-A, session scoping
github.com HTML                403
github.com/…/commits/X.atom    403     <- NEW, P109-B
github.com/…/releases.atom     403     <- NEW, P109-B
```

`P109-B` matters because the Atom feeds are the usual fallback when the API is
closed — they are unauthenticated and carry commit dates. They are closed too.
So the date cannot be read from any *description* of the repo; it has to come
from the commit object. `freshness.sh` therefore does a `--depth 1
--filter=blob:none` fetch of `HEAD` and asks `git log` for the date. That is
~1 s and a few KB per address.

## Date discipline

- **`P109-C` — committer date (`%cI`), never author date (`%aI`).** Author date
  survives rebase and cherry-pick, so a commit pushed today can be authored in
  2019. Reading `%aI` would report a live project as abandoned. Both columns are
  emitted so the disagreement stays visible; only `%cI` is banded.
- **`P109-D` — age is in UTC calendar days.** An earlier draft of this script
  differenced raw timestamps, which made the answer depend on the time of day of
  the reference date and on the commit's own timezone: a commit nine calendar
  days back reported as eight. Both sides are floored to a UTC date first.
- **A future-dated commit is a clock fault, not freshness.** Clamped to 0; no
  negative age is ever emitted.
- **`P1040` holds: `rc!=0` is `UNREAD`, never "abandoned".** Not reaching a
  repository tells you nothing about whether it is maintained.

## Bands

```
fresh      <=  30 days
active      31 ..  90
slowing     91 .. 365
dormant    366 .. 730
abandoned  >   730
```

## Files

| file | what |
|---|---|
| `freshness.sh` | the census. `./freshness.sh [list] [YYYY-MM-DD]` |
| `addresses.txt` | 296 shelf addresses, inherited from p108 (case-deduped, `P108-F`) |
| `test_p109.sh` | **32 passed / 0 failed**, fully offline |
| `validate.sh` | cross-checks every HEAD sha against p107's independent ref read |
| `result.2026-10-10.tsv` | this pass's output |

## Why the tests are worth trusting

`test_p109.sh` uses **no network and no mocks**. It builds real git
repositories in a temp dir with `GIT_COMMITTER_DATE` pinned and serves them over
`file://`, so the real fetch/log path runs. It covers: all eight band
boundaries exactly (30/31, 90/91, 365/366, 730/731); the rebase trap, where
author and committer dates differ by seven years and only one answer is right;
an unreachable remote landing as `UNREAD` with no band; a future-dated commit;
blank and `#` lines in the address list; and four structural invariants of
`addresses.txt` itself.

Supporting `file://` remotes is the one thing that made those tests possible —
`freshness.sh` resolves a bare `owner/repo` against github.com and uses anything
carrying a scheme verbatim.

## Honest limits

- **HEAD of the default branch only.** A project doing all its work on release
  branches reads staler than it is.
- **A commit is not a release, and neither is maintenance.** A daily
  dependency-bot commit reads `fresh`. Pair this column with p108's `class`:
  `fresh` + `semver` is the strong pair; `fresh` + `none` is motion without
  shipping.
- **Recency is not quality and not security.** It says someone touched it.
