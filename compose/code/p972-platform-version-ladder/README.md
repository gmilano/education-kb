# `p972-platform-version-ladder` — a platform's version is readable from the payload

**Pass 94, 2026-10-10 (fourth pass of this date).** Evidence directory.

🔴 **No executable here, deliberately — and for the second pass running.** This session's sandbox still
declines to run repository code (`bash compose/code/grant-ladder-v4/ladder.sh --help` is refused before it
starts), so pass 94 could not run this KB's own instrument and **did not write a replacement**. `P237`
forbids forking the shared classifier; `P970` says the correct response is to run the *oracle map* by hand
and print payloads instead of matching on them. What is committed here is **measurement, not an
instrument** — four TSVs with HTTP codes, byte counts, refs and SHAs, so the next pass that can execute
code has fixtures ready instead of a claim to re-derive.

## The finding (`P972`)

**Every version string in this KB's platform tier arrived as prose.** It need not. Two free oracles, both
already in the pass-92 oracle map, return a platform's version at payload grade:

| oracle | returns | cost |
|---|---|---|
| `git ls-remote --heads <slug>` / `--tags <slug>` | the **release ladder** the project actually maintains | one request, no auth, no API quota |
| `raw.githubusercontent.com/<slug>/<SHA>/<version file>` | the **release string** the code declares about itself | one request per read |

### Measured, on the market leader

`moodle/moodle`, `main` · `f205347`:

```
$version  = 2026100500.00;              // YYYYMMDD      = weekly release date of this DEV branch.
$release  = '6.0dev (Build: 20261005)'; // Human-friendly version name
$branch   = '600';                      // This version's branch.
$maturity = MATURITY_ALPHA;             // This version's maturity level.
```

`MOODLE_503_STABLE` · `4262229` → `$release = '5.3 (Build: 20261005)'`, `$branch = '503'`,
**`MATURITY_STABLE`**.

🔴 **Every secondary source read this pass said Moodle 5.2 was the current stable release.** The payload
says **5.3 is stable and 6.0 is in alpha**, and both carry a build stamp of **2026-10-05** — five days
before this pass. 🔵 **A vendor blog is at least one release stale by construction; the branch ladder is
current to the day.** For a KB whose whole method is "read the payload", the version column was the last
field still being taken on trust.

## 🔴 The second finding, and it is the expensive one (`P973`)

**`version.php` at the repository root is HTTP 404.** The file is at **`public/version.php`**.

Moodle **moved its web root into `public/`** at 5.0. A root-only probe reports *absent* for a file that
exists, which is `P969` one level up: **the root-only reach defect is not a licence problem, it is a path
problem**, and this KB has probed 24 licence filenames at the root for ninety-odd passes.

🔵 **And it costs money in an engagement, not just in a KB.** Every Dockerfile, reverse-proxy rule,
`config.php` path, CI job and customisation written against pre-5.0 Moodle points at the wrong directory.
That is a week-0 discovery if you read `public/version.php`, and a week-3 discovery otherwise.

## 🟡 The instrument's own limit, measured on the second platform (`P977`)

`openedx/edx-platform` has **19 `open-release/*` heads and the newest is `sumac.master`**. Open edX did not
stop releasing:

- `refs/tags/release/teak.1` … `teak.3`
- `refs/tags/release/ulmo.1` … `ulmo.4`

🔴 **Two things changed at once between Sumac and Teak: the ladder moved from heads to tags, AND the prefix
changed from `open-release/` to `release/`.** So a heads-only probe reports Sumac and is silently two named
releases stale, and a `grep open-release` over the tags misses Teak and Ulmo entirely.

🟢 **Cross-check that catches it:** the *deployment* distribution. `overhangio/tutor` is at **`v22.0.2`** —
what operators actually install. 🔵 **Rule: read the ladder from the remote, then confirm against the thing
that gets deployed.** One oracle is a reading; two disagreeing oracles are a finding.

🔴 **Also measured:** `openedx/edx-platform`'s `openedx/__init__.py` is a docstring and carries **no version
string at all** (HTTP 200, 417 B). Not every platform declares its version in code — recorded so the next
pass does not read that 200 as a version.

## Files

| file | what it holds |
|---|---|
| `pass94-versions.tsv` | version-file reads: slug, ref, SHA, path, HTTP, release string, branch, maturity |
| `pass94-release-ladders.tsv` | what each remote reports as its ladder, and where the ladder lives |
| `pass94-scoring-payloads.tsv` | the automated-scoring tier's licence payloads, with the Apache clause count |
| `pass94-grant-ratios.tsv` | `P976` — raw GNU-family term counts from two payloads, GPL-2.0 vs real LGPL-3.0 |

## What a pass that *can* execute code should do with this

1. Add a **version channel** to `grant-ladder-v4`'s oracle map: ladder from `ls-remote`, release string from
   the project's own version file, with `moodle/moodle` (`public/version.php`) and
   `openedx/edx-platform` (no version string) as the two fixtures — a positive and a negative.
2. Wire `compose/code/p199-perfile-license/` into the ladder, which is `Gap 370`, and generalise its path
   list beyond licence filenames — `P973` is the same defect for a different file.
3. Do **not** turn `pass94-grant-ratios.tsv` into a classifier branch on n=2. `P237` exists because pass 91
   did exactly that and it cost two platform licences and one client recommendation.
