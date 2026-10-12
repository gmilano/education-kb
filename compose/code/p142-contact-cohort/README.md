---
industry: education
region: North America
updated: 2026-10-12
---

# `p142-contact-cohort` — `ACTION DG`: 🔴 NOT REFUTED. `oscm@edx.org` is a cohort, and a fourth spelling appeared

## The action, as p141 wrote it

> Test the Arbisoft prediction. `openedx/XBlock` was modernised 2026-06-05 and kept
> `oscm@edx.org`; `openedx/codejail` was modernised 2026-09-14 and corrected it. Clone five
> further `openedx/*` repositories, read each `pyproject.toml` for the contact address, and
> correlate against the date of its own `chore: modernize` commit. 🔴 *Refuted if no further
> repository carries `oscm@edx.org`, which would make `XBlock` a one-off rather than a cohort
> and would reduce the finding from a campaign defect to a single typo.*

## Verdict: 🔴 **DISCHARGED, NOT REFUTED — 5 of 7 carry it**

Seven repositories were read, not five.

| repository | contact at `HEAD` | where | set by | date |
|---|---|---|---|---|
| 🔴 `openedx/code-annotations` | 🔴 `oscm@edx.org` | `setup.py` | `bmesick@tcril.org` | 2025-04-08 |
| 🔴 `openedx/edx-lint` | 🔴 `oscm@edx.org` | `setup.cfg` | `cale@edx.org` | **2017-03-09** |
| 🔴 **`openedx/event-tracking`** | 🔴 **`oscm@edx.org`** | 🔴 **`pyproject.toml`** | 🔴 `irfan.ahmad@A006-01919.local` | 🔴 **2026-07-28** |
| 🔴 `openedx/openedx-events` | 🔴 `oscm@edx.org` | `setup.py` | `ty@axim.org` | 2026-03-31 |
| 🔴 `openedx/super-csv` | 🔴 `oscm@edx.org` | `setup.py` | `dstgermain@edx.org` | 2019-05-15 |
| 🆕 🟡 **`openedx/openedx-filters`** | 🟡 **`technical@edunext.co`** | `pyproject.toml` | `irfanuddinahmad` | **2026-10-02** |
| 🟢 `openedx/openedx-learning` | 🟢 `dave@axim.org` | `pyproject.toml` | `irfan.ahmad@gmail.com` | 2026-09-03 |

With p141's two rows, **6 of 9 known `openedx/*` repositories carry `oscm@edx.org` at `HEAD`.**

## 🔴 The strongest row is `event-tracking`, and it narrows p141's timeline

p141 read the June (`XBlock`, stale) and September (`codejail`, corrected) commits and concluded
*"a convention that changed mid-campaign and was never backported"*. 🔴 **`event-tracking` sits
between them: the stale address was carried into PEP 621 `pyproject.toml` again on
2026-07-28.** So the corrected form was adopted some time after July, and July is a second
instance of the same carry-forward rather than an outlier.

🔵 **And the authorship of that commit is its own small finding:**
`irfan.ahmad@A006-01919.local` is a **local machine hostname**, not a routable address — on an
official `openedx/*` repository, from the same contractor whose `modernize` campaign the June
and September commits belong to.

## 🆕 🟡 A FOURTH contact spelling, and it is a third party's

p140 found Open edX naming its holder *"three different ways across three layers"*. There are
now four, and the new one is not stale — it is commercial:

```toml
# openedx/openedx-filters/pyproject.toml   (AGPL-3.0-or-later)
authors = [
    {name = "eduNEXT", email = "technical@edunext.co"},
]
```

🟡 **A core extension-point library of the platform names a commercial Open edX partner as its
author of record**, set during the same `modernize` campaign, 2026-10-02. That is not a defect —
it may be perfectly accurate attribution — but it means *"who do I contact about `openedx-*`"*
has no single answer, and a procurement question about the platform's extension points resolves
to a vendor.

🔴 **The vendor's jurisdiction is NOT established by this pass and is not guessed.** The address
sits on `.co`, which is Colombia's ccTLD and is also widely used generically; `edunext.co` is
unreachable from this environment, so no readable channel confirms the company's country. It is
recorded as `UNVERIFIED_JURISDICTION` and registered as `ACTION DJ`. 🔵 **This is the exact
error class the `.edu`/Navarra counterexample caught one probe over**, and it is declined here
for the same reason.

## Reproduce

```sh
./cohort.sh /path/to/openedx-clone ...   # TSV: contact, file, setting commit, modernize commit
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv).
