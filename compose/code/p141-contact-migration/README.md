---
industry: education
region: North America
updated: 2026-10-12
---

# `p141-contact-migration` — `ACTION DB`: 🔴 REFUTED. The split is a live migration that reached one repo and not the other

## The action, as p140 wrote it

> Read `openedx/XBlock`'s and `openedx/codejail`'s commit history for when `oscm@edx.org` and
> `oscm@openedx.org` diverged, and whether either was updated after the Axim rename. 🔴
> *Refuted if both addresses predate the rename and neither has been touched since — which
> would make the three-way contact split an artefact of neglect rather than a live
> inconsistency, and a far weaker procurement finding.*

## Verdict: 🔴 **DISCHARGED and REFUTED. Both were touched in 2026, by the same campaign.**

[`result.2026-10-12-p141.txt`](result.2026-10-12-p141.txt),
[`diffs.2026-10-12-p141.txt`](diffs.2026-10-12-p141.txt):

| repository | at `HEAD` | the commit that set it | author | date |
|---|---|---|---|---|
| 🔴 `openedx/XBlock` | 🔴 **`oscm@edx.org`** in `pyproject.toml` | `94a759c` *"chore: modernize the repo"* | `salmannawaz <salman.nawaz@arbisoft.com>` | **2026-06-05** |
| 🟢 `openedx/codejail` | 🟢 `oscm@openedx.org` in `pyproject.toml` | `0b38ff8` *"chore: modernize codejail to use uv and pyproject.toml"* | `farhan <farhan.khan@arbisoft.com>` | **2026-09-14** |

🔴 **So neither address "predates the rename and was untouched since".** Both lines were
rewritten this year, three months apart, by two contributors **at the same company**, under the
same `chore: modernize` banner. The exact diffs:

```diff
# openedx/codejail  0b38ff8  2026-09-14  farhan@arbisoft.com
-    author_email="oscm@edx.org",
+    {name = "Open edX Project", email = "oscm@openedx.org"},

# openedx/XBlock    94a759c  2026-06-05  salman.nawaz@arbisoft.com
-    author_email='oscm@edx.org',
+    {name = "edX", email = "oscm@edx.org"},
```

🔵 **Read them together and the cause is unmistakable.** Both commits migrated the same legacy
`setup.py` field into PEP 621 `authors = [...]`. The September one corrected the organisation
*and* the domain. The June one **retyped the stale organisation name and the stale domain into
the new syntax** — it had the line open, in an editor, and carried it forward verbatim.

🔴 **The divergence is a convention that changed mid-campaign and was never backported.** Not
neglect: a live, in-flight migration, with the corrected form adopted only after June.

## 🔴 Why this is the stronger procurement finding p140 hoped it would not be

`oscm@edx.org` is live at `HEAD` in `openedx/XBlock` — the component every XBlock-based course
component in the Open edX ecosystem builds against. p140 established that **`edx.org` is a
domain 2U operates**, while the project's steward is **Axim Collaborative**
(`dave@axim.org`), the renamed edX Inc.

🔴 **So XBlock today directs maintainer and security correspondence for an Open edX core
component to a domain controlled by a different company than its steward — and the line was
looked at four months ago and kept.** `openedx/codejail`, the sandbox that executes untrusted
learner-submitted code, now points at `oscm@openedx.org`. 🔵 **Two core components, one
ecosystem, two different companies' domains in the field a vulnerability reporter reads
first.**

🟢 **The finding has a clean remedy and it is already written**: the September commit is the
template. This is a one-line change in `pyproject.toml`, not a design question.

## 🆕 🔵 And the modernisation campaign itself places a region

Both 2026 commits are `@arbisoft.com`, at `+0500`. 🔵 **p140 recorded Arbisoft — the
Pakistan-based firm whose edtech arm Edly acquired Overhang.IO (Tutor) on 2023-03-27 — as an
APAC market fact.** It is also, measurably, the contractor modernising Open edX core
repositories. 🟡 The 2017 commit that first introduced `oscm@edx.org` is authored
`rraposa@edx.org` — the organisation's own domain, when it still was.

🔵 So the North America / APAC split on this component is not steward-vs-user: **a US
non-profit holds the stewardship and an APAC contractor holds the commit bit on the files that
record who to contact.** Neither fact is a defect; the contact field that disagrees with both
is.

## Reproduce

```sh
git clone https://github.com/openedx/XBlock   /tmp/XBlock
git clone https://github.com/openedx/codejail /tmp/codejail
./trace_contact.sh /tmp/XBlock /tmp/codejail
```

🔵 `git log -S` (the pickaxe) is the instrument, not `git log -p | grep`: it reports commits
where the **count** of the string changed, so a commit that moves the line between files
without changing it does not appear and a commit that deletes it does.
