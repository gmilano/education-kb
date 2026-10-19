# `p307-payload-pin` — the three-valued grant classifier, and the end of the filename ladder

`ACTION p306-R` ranked three instrument items. This directory implements all three, and
implements the third by **deleting** what it asked to extend.

| item | asked for | delivered |
|---|---|---|
| 1 | pin the sidebar/README backlog by bytes | 🟢 70 payloads, 59 of them the backlog |
| 2 | make the verdict three-valued | 🟢 `GRANT` / `POINTER` / `RESERVED` |
| 3 | add lower-case `license.txt` to every ladder | 🔴 **the ladder is retired** — see below |

## Why the ladder had to go

Built to item 3's spec — fifteen filenames, lower case included, branch read from
`git ls-remote` rather than guessed — the first version of `probe_p307.py` reported
`NO-PAYLOAD` for [`openedx/XBlock`](https://github.com/openedx/XBlock), whose README says
the code is Apache-2.0 and links `LICENSE.txt`.

Two independent channels agreed with the absence: `raw.githubusercontent.com` returned
`404`, and `github.com/openedx/XBlock/blob/master/LICENSE.txt` returned `404` through a
different client. **Both were wrong, and they were wrong together, because both had been
handed the same address.** The file is `LICENSE.TXT`.

PyPI's sdist resolved it (`License-Expression: Apache-2.0`, `License-File: LICENSE.TXT`),
and the payload then read `11 358 B`, `sha256₁₂` `cfc7749b96f6`.

Inside one organisation: `openedx/edx-platform` → `LICENSE`, `openedx/openedx-events` →
`LICENSE.txt`, `openedx/XBlock` → `LICENSE.TXT`. **The case axis has no bound, so the
ladder cannot be completed.** The replacement enumerates:

```
git clone --depth 1 --filter=blob:none https://github.com/{slug}   # rc=0, ~2.4 s, ~1.5 MB
git -C {repo} ls-tree HEAD                                         # exact root entries + type
git -C {repo} show HEAD:{picked}                                   # lazy single-blob fetch
```

Fewer requests than a ladder, no guessed filename, no guessed branch, and an absence that
is a measurement rather than a failed question.

> The clone channel was carried by `p305` and `p306` as *"refused by the execution
> policy."* Re-tested at `p307`: it is not. Third inherited environmental absence refuted
> in two passes, alongside *"no primary source"* (`p306`) and *"`make` is refused"*
> (`p307`).

## The verdict

```
GRANT    a permission clause is present
POINTER  no clause, but an http(s) URL to a licence text
RESERVED no clause and no URL
```

A `POINTER` yields an **identity**, never **terms**. `p306` found the class in a 167 B W3C
file; `p307` found the second instance on the 877★
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills),
whose `LICENSE` is the Creative Commons *deed* and says so in its own last line. Any
clause-level claim read from a `POINTER` must be labelled as read from a deed.

Order matters: the **clause** test runs before the **reserved** test, because stock
BSD-3-Clause opens with the words *"All rights reserved"*. Reverse them and every BSD-3
grant in this vertical grades as withheld.

## Three defects this instrument shipped, all caught before publication

`p306` named the class — a rule defeated by the very thing it screens for — and
`ACTION p305-R` item 1 asked for exactly this control. Each is now a standing test case.

1. **A line-wrapped clause.** Apache-2.0's *"hereby"* and *"grants to You a perpetual"*
   fall on opposite sides of a newline in `tsugiproject/tsugi`'s payload, and a raw-bytes
   matcher graded a full Apache licence as a `POINTER`. Fix: match whitespace-flattened
   text.
2. **A directory read as a payload.** `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` has a root entry
   `Licenses` that is a folder of six PDFs; `git show HEAD:Licenses` prints the tree index,
   the index contains *"GNU Lesser General Public License.pdf"*, and the row graded `LGPL`
   against a repository that is Apache-2.0 at `LICENSE.txt`. Fix: `ls-tree` with the type
   column, blobs only. One of 70 rows was affected, and it is the only row that moved.
3. **GPL-2.0 graded as LGPL**, because GPL-2.0's own body says *"use the GNU Lesser General
   Public License instead of this License"*. Fix: the GNU family is read from the **title**,
   version included. Caught by an independent channel — Packagist reports
   `oat-sa/tao-core` as `GPL-2.0-only`, agreeing with the shelf and disagreeing with the
   instrument.

The same title rule is what surfaced this pass's headline defect: `brownplt/LTLTutor` and
`IgorFonck/logicits` were carried as AGPL-3.0 for two passes on the strength of a byte
**length series**, and both titles read `GNU GENERAL PUBLIC LICENSE Version 3`.

## Two hashes

`sha12` is byte-identity. `nsha12` is computed over CRLF-normalised, end-stripped text and
is **licence**-identity: nine stock-Apache payloads at three byte lengths and four distinct
`sha12` collapse to one `nsha12` (`283ea6cc2997`).

## Running it

```
cd compose/code/p307-payload-pin
python3 test_probe_p307.py                 # 9 offline controls; also `make gate-payload-pin`
printf 'owner/repo\n' | python3 -I probe_p307.py   # online; TSV on stdout
```

The offline suite is wired into `make hooks` as `gate-payload-pin`, which is how
`ACTION p305-R` item 1 — outstanding for two passes because `make` could not be run — is
discharged. The online half stays out of `hooks`, per this repository's standing rule that
a gate must be runnable where there is no egress.
