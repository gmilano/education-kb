---
industry: education
region: Global
updated: 2026-10-07
---

# `git-recency-channel` — dating the shelf without a forge API (pass 23 of 2026-10-07)

Trend 52, written one pass earlier, said this KB **cannot** measure whether its own shelf is alive,
because `api.github.com` serves `pushed_at` and returns 403 here. **The status was real; the
conclusion was not.** `git` is not an API and `git` is not blocked.

This instrument dated **884 of 904** GitHub references in under two minutes and **falsified the
trend that said it was impossible** — using two commands that trend 52's own closing paragraph had
already named as open.

## What it does

| Step | Command | Yields |
|---|---|---|
| existence | `git ls-remote <url> HEAD` | ref SHA, or nothing |
| fetch head only | `git fetch --depth 1 --filter=blob:none origin HEAD` | commit + tree objects, no blobs |
| date it | `git log -1 --format=%cI FETCH_HEAD` | ISO-8601 committer date |

Blob filtering is what makes it cheap: a repository of any size answers in roughly a second, because
no file contents cross the wire.

## Why the negative result means something

🟢 **The probe discriminates, and that is the property most of this KB's channels lack.** Four
repository slugs invented by earlier passes as controls were swept blind alongside the real ones and
**all four failed to resolve**, while 884 real references returned a date.

Compare: pass 22's `gitlab.com` rendered-page probe **302s on an invented slug**, so a 200 from it
proves nothing. And the 15 LATAM self-hosted forges probed this pass returned **000 — exactly what a
deliberately bogus host returns**, which is why this KB records that sweep as *unmeasurable* rather
than as *empty*.

`test_git_recency.py` is that discrimination test, not a smoke test.

## Invocation

```sh
# whole reference list
python3 -I git_recency.py data/references-2026-10-06.txt > recency.tsv

# one repository
python3 -I git_recency.py --slug learningequality/kolibri
# learningequality/kolibri	2026-10-06T14:32:46-07:00	5ea5d47	OK

# the control tests — plain python3, because -I strips the script directory
# from sys.path and the test imports the module beside it
python3 -m unittest -v test_git_recency
```

Output is TSV: `slug`, ISO-8601 committer date, short sha, `OK|FAIL`.

## Data in this directory

| File | Contents |
|---|---|
| `data/references-2026-10-06.txt` | the **904** distinct `owner/repo` references extracted from all 8 KB files |
| `data/recency-2026-10-06.tsv` | the measurement: 884 dated, 20 unresolved |

**Reference date for every age published from this run: 2026-10-06.** The sweep ran
2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC, so a few rows carry a head commit dated `2026-10-07`
from timezones ahead of UTC.

## Reading the 20 unresolved rows

🟢 **None is newly dead.** They decompose as:

| Cause | n | Examples |
|---|---|---|
| already recorded as 404 by an earlier pass | 12 | `radhepa/Teacher-MCP` (5th confirmation), `1EdTech/caliper-java` (the consortium announced a move to private repos), `yetanalytics/lrspipe` (product name ≠ repo name) |
| deliberate controls planted by earlier passes | 4 | `UniTime/this-repo-does-not-exist-xyz123`, `openedx/fake-repo-zzz999` |
| citation artefacts, not repositories | 4 | `owner/repo`, `your-username/SafeTutors`, `repos/HKUDS`, a truncated `UOC/java-lti-1.3-provider` |

⚠️ **The extraction regex is the weak point, not the probe.** It matches `github.com/<a>/<b>` in
prose, so placeholder slugs inside code fences and truncated inline references enter the list. Any
future run should treat an unresolved row as *"check how this is cited"* before *"this is dead"*.

## The rule this instrument exists to enforce

**P22.4 — currency.** Record the head-commit date of every component entering a deliverable, and
**run it over the dependency closure, not the dependency list.** The shape it catches:
`ucfopen/cookiecutter-python-lti` is MIT and 147 days old, and its Flask template pins
`git+https://github.com/ucfopen/pylti1.3.git@master` — a fork, **1,363 days cold**, at a moving
branch. Neither the template's licence nor its own date reveals that.

🔴 **Never prune on date alone.** A finished conformant implementation and an abandoned one are
indistinguishable to this probe; only reading the project tells you which it is. The verdicts are
**disclose** and **price**, never **delete**.
