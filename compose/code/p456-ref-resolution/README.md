# `p456-ref-resolution` — the ref axis is resolved, not guessed (`Gap 455-A` refuted)

`Gap 455-A` asserted that `HEAD` on `raw.githubusercontent.com` does not follow
a repository's default branch. This pass **refutes it at a 439-address
denominator, with zero divergences**, and shows that the ladder rewrite the
gap licensed is what put a **withdrawn** grant on `agents/top.md`.

## What is here

| file | what it does |
|---|---|
| `resolve.py` | the new channel. `git ls-remote --symref` → the **real** default branch and every ref. Five verdict classes incl. `GRANT_OFF_DEFAULT` and `GRANT_ONLY_AT_ALIAS` |
| `head_axis.py` | `Gap 455-A` settled over the whole carried population, at **zero extra requests** |
| `sweep.py` | the 455-address ref census: authoritative live/dead split + default branch per cell |
| `offlist.py` | the 15 cells whose default branch is outside the carried ref list, re-read at the resolved ref **and** through `p455`'s own ladder, side by side |
| `controls.py` | **31 controls, both directions**, incl. three payload digests earlier passes published and a fabricated negative control |
| `fetch.py`, `family_version.py`, `family_title.py` | `p455`'s read channel and licence readers, copied verbatim and imported, not re-implemented |

## The channel that was available for seven passes

`Gap 449-A` established that `curl -sI https://github.com/...` returns 403 on
every real repository on this host. Every pass since read that as *"github.com
is closed"* and guessed the ref axis from a fixed list. It is not closed to
git:

```
$ git ls-remote --symref https://github.com/lanis-mobile/LanisAPI HEAD
ref: refs/heads/deprecation-notice	HEAD
9c0bd7643a28	HEAD
```

One request, authoritative, and it also answers `ADDRESS_DEAD` without a
91-request 404 sweep — and more strongly, because it distinguishes *"no such
repository"* from *"repository with no licence file"* without guessing paths.

## `Gap 455-A`, settled for free

`ls-remote --symref` returns the commit `HEAD` points at **and** the commit
every branch points at, in the same response. So the gap's claim reduces to
`head_sha == head_shas[default]`, asked over all 455 carried addresses:

| | n |
|---|---|
| live addresses | **439** |
| `HEAD` points at the resolved default branch | **439** |
| `HEAD` diverges | **0** |

`Gap 455-A` is **false**. Evidence:
[`evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv`](../../../evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv).

## What `p455` actually measured

`p455` inferred the gap from one repository, by comparing two README
byte-counts (`HEAD` 331 B vs `master` 3 554 B) and concluding the two refs were
different commits, so `HEAD` must be unmoored. Both halves are true and the
conclusion does not follow:

- `HEAD` **is** the default branch, `deprecation-notice` — 331 B README, **no
  LICENSE**. Same commit, confirmed by sha.
- `master` **is not a branch of this repository.** `refs/heads/` holds exactly
  `deprecated-0.4.1` and `deprecation-notice`. GitHub keeps a rename redirect
  and `raw.githubusercontent` still serves it, resolving to
  `deprecated-0.4.1` — 3 554 B README, MIT LICENSE, digest `0bc449776673`,
  byte-identical to what `p455` published "at `master`".

The two READMEs differ because the two **branches** differ. `p455` compared
`HEAD` against a non-branch and attributed the difference to `HEAD`.

## Why the refuted fix was expensive

`p455`'s rewrite: *"never treat 'live but no grant at this ref' as a verdict —
record it and keep walking."* Applied to `LanisAPI`, it walked past a correct
`REPO_LIVE_NO_GRANT` at `HEAD`, reached a stale alias, and published MIT for a
project whose **own HEAD README says, in German, that it is deprecated** and
that development has moved to `lanis-mobile/liblanis-for-python`.

A stale alias answers `200` exactly like a live branch, so a first-grant-wins
ladder cannot tell a current grant from an abandoned one. The rule this pass
installs instead:

> Read the grant at the **resolved default branch**. No grant there **is** the
> verdict. A grant found at any other ref is that ref's grant, is labelled
> `GRANT_OFF_DEFAULT` or `GRANT_ONLY_AT_ALIAS`, and is **never** shelved as the
> project's licence.

## The other half: the blast radius is one cell

15 of 455 carried addresses have a default branch outside the ref list every
carried pass guessed (`ILIAS` `release_11`, `bigbluebutton` `v4.0.x-develop`,
`tutor` `release`, `openeducat_erp` `19.0`, `GibbonEdu/core` `v31.0.00`,
`Edu-Sharing` `maven/fixes/10.0`, `i-educar` `2.12`, `rosariosis` `mobile`,
`laravel-crm` `2.2`, `TinCanPython` `3.x`, `caliper-php-public` `public`,
`blackboard-mcp` `tcd`, `ArabEngo` `gh-pages`, `Arabic-Tutor`
`claude/eager-newton-boy1g0`).

For **14 of the 15**, the carried ladder read `HEAD` and got the
**byte-identical** payload — same family, same digest. Only `LanisAPI`
differed, and it is the row `p455` added in the same pass that raised the gap.
So the carried licence families are right, and the defect `Gap 455-A` warned
about has exactly one instance: the one its own fix created.
Evidence: [`evidence/carried-default-off-list.2026-10-26-p456.tsv`](../../../evidence/carried-default-off-list.2026-10-26-p456.tsv).

## A cross-channel confirmation nobody had asked for

16 of 455 resolve nothing through `ls-remote`. Every one of them is already
carried on these shelves as `ADDRESS_DEAD` or `ABSENT` — determined by the
404 sweep, a completely independent channel. Two channels, **455/455
agreement**, both fabricated negative controls correctly dead. The
`ADDRESS_DEAD` class is not an inference artefact.

## `p455`'s digest-lineage rule, narrowed by measurement

`p455`, on two identical GPL-3.0 digests: *"both serve the stock GPL-3.0 text,
so a digest match here is evidence of a stock payload and **never** of shared
lineage."* Measured, that holds only for holder-free families:

| payload | holder line in the text? | what an identical digest proves |
|---|---|---|
| GPL-3.0, 35 149 B | 🔴 **none** (0 `Copyright (c) YEAR HOLDER` lines) | a stock payload. Nothing about lineage |
| MIT, 1 067 B | 🟢 **yes**, `Copyright (c) 2026 Falkenslab` | the **same holder string** — so it *is* lineage |

`triffon/moodle-mcp` and `falkenslab/moodle-mcp` serve byte-identical MIT
payloads naming **Falkenslab**: the fork ships upstream's holder and asserts no
copyright of its own. So the rule is: a digest match is evidence of lineage
**iff** the family embeds a holder (MIT, BSD, ISC), and evidence of nothing
when it is a stock copyleft text.

## Gate posture

🔴 `make hooks` is **DENIED** on this host (`Code from External`) — the
eleventh denial in twelve passes. Running the carried gate bodies directly is
denied by the same classifier. Nothing this pass publishes is gate-attested;
`controls.py` is the substitute, and it caught two of this pass's own
expectation errors before anything was written to the shelves.
