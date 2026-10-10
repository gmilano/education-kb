# p108-release-identity — from "does it release?" to "what do I pin?"

**Pass 108, 2026-10-10.** Anonymous git lane only. No `api.github.com`, no clone, no search.

## What this answers that p107 did not

`p107-git-lane-census` established, over 299 shelf addresses, **how many tags** each
carries, and concluded that 38 % of the shelf has never shipped a release. That holds.
p107 also hand-read a **pin** for six named rows of `agents/top.md`; this instrument
reproduces all six exactly (`DeepTutor v1.6.14`, `unitime v4.9.152`,
`moodle-local_aihub v1.3.4`, `pyBKT 1.4.3`, `OATutor v1.7`, `bncc-dados dados-2026.07.1`),
which is the closest thing to an independent check either pass has had.

What six hand-reads cannot do is expose the *systematic* faults, and all four found here
are invisible at that sample size: a repo with 4 468 tags and no version, a release
hiding under a project prefix, a date crowned as a release, and a double-counted
denominator. **A tag count is not a release ladder, and a handful of spot-checks is not a
census.**

## Output

`census.sh` → TSV, one row per address:

| column | meaning |
|---|---|
| `slug` | `owner/repo` |
| `rc` | `0` = refs read; non-zero → `class=UNREAD`. **An unread row is never "no releases"** (`P1040`) |
| `tags_uniq` | tag refs, `^{}`-peeled rows excluded (`P108-A`) |
| `stable_n` / `latest_stable` / `latest_stable_sha40` | bare `vN.N.N` lane |
| `prerel_n` | version-shaped tags carrying a suffix (`-rc1`, `-beta`) — counted, never pinned |
| `prefix_n` / `latest_prefix` / `latest_prefix_sha40` | project-prefixed lane (`OpenOLAT_21.0.3`) |
| `class` | **the decision column**: `semver` \| `prefixed` \| `stamp` \| `none` \| `UNREAD` |

### Read `class` first

`class` says which version column is authoritative. `latest_prefix` is **noise on a
`semver` row** — on 14 of the 159 it holds things like `test-build-v23.0.01` or
`Drupal-7.x-1.55`, which are not that repo's release. Pin from `latest_stable` when
`class=semver`, from `latest_prefix` when `class=prefixed`, and **do not pin by version
at all** when `class` is `stamp` or `none`.

## The seven rules, each one a wrong answer before it was a rule

- **`P108-A`** `^{}` rows dropped first (inherits `P107-C`): an annotated tag is emitted
  twice, and its peeled row can otherwise win the sort.
- **`P108-B`** A stable tag is `^v?N.N(.N)?$` and nothing else. "Latest tag" and "latest
  pinnable release" are different questions.
- **`P108-C`** Rank with `sort -V`, never `sort`. **Live case: `dspace`.** Lexically
  `dspace-7.6` beats `dspace-10.1`, so a lexical reader pins three majors stale and the
  output looks perfectly reasonable.
- **`P108-D`** Tags without semver are *two* different situations. CI **deploy stamps**
  (`va-green-dev-2026-08-08T22_31_36+00_00`) carry no version. **Project-prefixed
  releases** (`OpenOLAT_21.0.3`, `dspace-10.1`) carry a good one. Collapsing them
  slanders the second group — and OpenOLAT is an Apache-2.0 LMS, so the slander has a cost.
- **`P108-E`** The prefix lane anchors the version at end-of-ref and requires a
  separator, else `green-dev-1791293242` parses as version `1791293242`.
- **`P108-F`** Case-duplicate addresses are one repo (GitHub `owner/repo` is
  case-insensitive). p107's list carried three such pairs, so its denominator of 299
  double-counted. Honest denominator: **296**. Fixed in `addresses.txt`.
- **`P108-G`** A **trailing** year is a date, not a version. `production_16.01.2017`
  parses as `16.1.2017` and `sort -V` then crowns it the latest release of a repo that
  has never cut one. CalVer survives because CalVer puts the year **first**
  (`dados-2026.07.1`); a date puts it last. Rule: reject when the final numeric
  component is ≥ 1900.

## Running it

```sh
./test_p108.sh    # 38 passed / 0 failed — offline, fixtures only, no network
./census.sh > result.$(date +%F).tsv
```

`test_p108.sh` is fully offline. Two fixtures are real captures (`moodle`, `kolibri`);
five are hand-built to pin `P108-C`, `-A/B`, `-E` and `-G`.

`census.sh` read **296 of 296** addresses in 1 m 49 s, `rc=0` on every one, **zero unread**.

## Result, 2026-10-10

| class | n | share | meaning |
|---|---|---|---|
| `semver` | 159 | 53.7 % | pin `latest_stable` |
| `prefixed` | 9 | 3.0 % | pin `latest_prefix` |
| `stamp` | 15 | 5.1 % | **tags exist, no version anywhere** — pin a SHA |
| `none` | 113 | 38.2 % | no tags — pin a SHA |
| | **296** | | **pinnable by version: 168 (56.8 %)** |
