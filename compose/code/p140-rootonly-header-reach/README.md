---
industry: education
region: Global
updated: 2026-10-12
---

# `p140-rootonly-header-reach` — `ACTION CQ`: the foreign-header class holds, weakly; the real finding is that three rows record ownership NOWHERE in source

**Executes p139's pre-registered `ACTION CQ`**, written as:

> Extend `ACTION CJ` to the **five unread `ROOT_ONLY` rows** (`Crosstalk-Solutions/project-nomad`,
> `overhangio/tutor`, `adaptlearning/adapt_framework`, `openedx/XBlock`, `openedx/codejail`).
> 🔴 *Refuted if none carries a foreign source header, which would make the 2-of-3 a property
> of the three largest rather than of the class.*

## Verdict: **DISCHARGED, NOT REFUTED — but 🟡 weakly: 1 of 5, against p139's 2 of 3**

| row | tree paths | source headers | own | 🔴 foreign | header verdict | 🆕 where ownership IS recorded |
|---|---|---|---|---|---|---|
| `Crosstalk-Solutions/project-nomad` | 664 | 1 | 1 | 0 | 🟢 `OWN_HEADERS_ONLY` | `ROOT_LICENCE_FILLED` + `PACKAGE_METADATA` |
| `overhangio/tutor` | 249 | 🔴 **0** | 0 | 0 | 🔴 `NO_HEADER_AT_ALL` | 🔴 `ROOT_LICENCE_TEMPLATE` + `PACKAGE_METADATA` |
| `adaptlearning/adapt_framework` | 118 | 1 | 0 | 🔴 **1** | 🔴 `FOREIGN_HEADER_IN_SOURCE` | `ROOT_LICENCE_FILLED` |
| `openedx/XBlock` | 193 | 🔴 **0** | 0 | 0 | 🔴 `NO_HEADER_AT_ALL` | `NOTICE_FILE` + `PACKAGE_METADATA` + 🔴 `ROOT_LICENCE_TEMPLATE` |
| `openedx/codejail` | 43 | 🔴 **0** | 0 | 0 | 🔴 `NO_HEADER_AT_ALL` | `NOTICE_FILE` + `PACKAGE_METADATA` |

Combined with p139: **3 of 8** `ROOT_ONLY` rows carry a foreign source header. The class is
real and thinner than the first three rows suggested. The single foreign holder here is
`Tim Branyen, contributors` in `grunt/tasks/handlebars.js` — an **MIT-licensed vendored grunt
task inside a GPL-3.0 repository**, so a notice obligation, not a conflict.

## 🆕 `P140-D1` — the finding `ACTION CQ` did not ask for: 287 source files, zero headers

🔴 **`overhangio/tutor` (157 source files read), `openedx/XBlock` (99) and `openedx/codejail`
(31) carry no copyright header in any source file.** That is not an absence of ownership — it
is ownership recorded somewhere else, so each row is also scored for *where a holder is
findable at all*. 🔵 **A delivery team asking "who holds this code?" needs to know which file
to open, and for these rows it is increasingly not the one named `LICENSE`:**

| row | `LICENSE` names a holder? | elsewhere |
|---|---|---|
| `project-nomad` | 🟢 yes — Apache appendix **filled**: `Copyright 2024-2026 Crosstalk Solutions LLC` | `package.json` |
| `adapt_framework` | 🟡 only inside the GPL's **interactive-mode example**: `adapt_framework  Copyright (C) 2013  ADAPT LEARNING` | — |
| `XBlock` | 🔴 no — appendix left as `Copyright [yyyy] [name of copyright owner]` | `NOTICE.txt`, `pyproject.toml` |
| `codejail` | 🔴 no — the appendix carries **no copyright line at all** | `NOTICE.txt`, `pyproject.toml` |
| `tutor` | 🔴 no — template left as `Copyright (C) <year>  <name of author>` | `pyproject.toml` only |

🔵 **`adapt_framework` is a third form this KB has not recorded**: the holder appears in the
licence file *only* as part of the GPL's illustrative `show c` snippet. It is a real
attribution in a place no scanner treats as one.

## 🆕 `P140-D2` — Open edX names its holder three different ways across three layers

| layer | artefact | holder | contact domain |
|---|---|---|---|
| repo | `openedx/XBlock` `NOTICE.txt` + `pyproject.toml` | `edX` | 🔴 `oscm@edx.org` |
| repo | `openedx/codejail` `NOTICE.txt` / `pyproject.toml` | `edX` / 🆕 **`Open edX Project`** | 🆕 `oscm@openedx.org` |
| registry | `openedx-core` 1.9.1 (PyPI, 2026-10-09) | 🆕 `David Ormsbee` | 🆕 **`dave@axim.org`** |

🟢 **The holder NAME is defensible**: edX Inc. was *renamed* Axim Collaborative — same
trustees, same mission, same tax ID — after Harvard and MIT sold the edX brand to 2U, so
`Copyright 2014, edX` names the pre-rename identity of the current steward rather than a
third party.

🔴 **The CONTACT domain is not.** `edx.org` is operated by **2U**, a different company from the
steward, and `openedx/XBlock`'s `pyproject.toml` still routes to it while its sibling
`openedx/codejail` routes to `openedx.org`. 🔵 **Two repositories in one GitHub organisation,
same licence, different holder string and different contact domain** — and a third domain
(`axim.org`) on the live PyPI artefact. For a client asked to send a notice, that is three
answers to one question.

## 🟡 `P140-D3` — `tutor`'s metadata is FRESHER than its organisation name

`overhangio/tutor` declares `authors = [{name = "Edly"}, {email = "hello@edly.io"}]` — neither
`overhangio` nor the original author. 🟢 **That is correct and current**: Edly, the edtech
division of Pakistan-based Arbisoft, acquired Overhang.IO on **2023-03-27**, and Tutor's
founder Régis Behmo became Edly's VP of Engineering and still leads its technical direction.

🔵 **So this row inverts the expected reading.** This KB has repeatedly found metadata lagging
reality; here the `pyproject.toml` is accurate and the **GitHub organisation name is the stale
signal**. 🔴 **A row's org name is not evidence of anything**, which is the same lesson
`ACTION CU` reaches from the other direction.

## 🔴 A latent defect in p139's classifier, found and guarded

🔴 `header_holder.extract_holder("Copyright © 2024")` returns **`"2024"`**. The year is
optional in the marker group, so a notice carrying a marker and a year and **no name** lets
the year fall through into the holder capture.

🟢 **p139's published results are NOT affected** — its three rows contain no nameless notice,
and an audit of its committed detail table finds zero year-shaped holders. 🔴 **The defect
fired on the first new row this pass read**: `adaptlearning/adapt_framework` ships
`"attribution": "Copyright © 2024"` in `src/course/en/components.json`, and an unguarded run
publishes **`2024` as a foreign copyright holder of the repository**.

🔵 **p139's committed code is left exactly as it was.** Its result is a dated record, and
editing the instrument beneath it would invalidate the record rather than correct it. The
guard lives here, and [`test_rootonly_reach.py`](test_rootonly_reach.py) pins the defect and
the fix in both directions — including that the guard costs no real holder, and that
`1EdTech Consortium` survives a rule that must reject `2024` without rejecting names
beginning with a digit.

## Method

The foreign-header question re-runs **p139's own collector, unchanged and imported rather
than copied** — a second instrument would confound a change of result with a change of method.
This module adds the nameless-holder guard and the ownership-location axis. Holder names are
classified against an explicit, recorded list of each row's own names, so a reader can
disagree with the list rather than re-derive it.

## Reproduce

```sh
for r in Crosstalk-Solutions/project-nomad overhangio/tutor \
         adaptlearning/adapt_framework openedx/XBlock openedx/codejail; do
  git clone --depth 1 "https://github.com/$r" "$(echo "$r" | tr / _)"
done

python3 -I rootonly_reach.py \
  Crosstalk-Solutions_project-nomad  Crosstalk-Solutions/project-nomad  "Crosstalk Solutions" \
  overhangio_tutor                   overhangio/tutor                   "Edly,Overhang,Regis Behmo,Régis Behmo" \
  adaptlearning_adapt_framework      adaptlearning/adapt_framework      "ADAPT LEARNING,Adapt Learning" \
  openedx_XBlock                     openedx/XBlock                     "edX,Axim,Open edX" \
  openedx_codejail                   openedx/codejail                   "edX,Axim,Open edX"

python3 -I test_rootonly_reach.py   # 14 tests
```
