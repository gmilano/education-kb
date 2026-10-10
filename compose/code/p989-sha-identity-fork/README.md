# p989 — the SHA is the identity test, and the promotion ledger this KB never had

**Pass 97, 2026-10-10.** Seventh pass of this date.

🔴 **Repository code was refused for a FIFTH consecutive pass** (`[Code from External]`), so
`grant-ladder-v4/ladder.sh` and its offline `test_ladder.sh` were both denied before starting.
🟢 **No classifier was written** (`P237`). The oracle map was run by hand, as in passes 93–96
(`P970`): `git ls-remote --symref` for existence/ref/SHA, then
`raw.githubusercontent.com/<slug>/<FULL-SHA>/<name>` for the payload, printing the title block
instead of matching on it.

`results.2026-10-10.tsv` — 20 slugs resolved: 11 licence payload reads, 7 negatives, 2 forks.

## P989 — two slugs at the same HEAD SHA are one repository

`api.github.com` returned **HTTP 403 for a sixth consecutive pass**, and this pass measured that
`github.com` **HTML is 403 as well** — so there is no star channel at all, by either route. That
closes the question passes 92–96 left open and it makes the cheap identity test worth naming:

| slug | ref | HEAD SHA (14) | verdict |
|---|---|---|---|
| `Halleck45/OpenPronounce` | `main` | **`74bc17ea406e6f`** | upstream |
| `CHINOBv/OpenPronounce` | `main` | **`74bc17ea406e6f`** | 🔴 **same object — a non-diverged fork** |
| `Ronald-TR/OpenPronounce` | `main` | `f43079b80fcbef` | 🟡 a fork that has moved |

🔵 **A search for the technique returned these three as three projects.** There is one project and
two forks: all three serve a **byte-identical 1 113 B MIT payload** whose holder is
`Jean-François Lépine` — the upstream author. 🟢 **`git ls-remote` costs one round trip, needs no
token, and answers the identity question through the only channel that is open.** 🔴 **A 7-char
prefix is not enough for this claim** (`P987`); the match is published at 14.

## P991 — the title block can be DISPLACED rather than absent

`kaldi-asr/kaldi` serves `COPYING` at **17 264 B**, and it is **not** a pristine Apache-2.0 file:

| measurement | value |
|---|---|
| total bytes | **17 264** |
| first occurrence of `Apache License` | 🔴 **byte offset 2 531** |
| first occurrence of `TERMS AND CONDITIONS` | byte offset 6 068 |
| Apache clause headings present (`P974` probe) | 🟢 **4 of 4** |

The first 2 531 bytes are a joint-ownership clarification notice ("*Update to legal notice, made
Feb 2012, modified Sep 2013*"), prepended ahead of the full, unabridged Apache-2.0 body.

🟢 **The shared classifier holds.** `lib/license_family.sh` reads its title-block window as
`head -c 4000` (line 106), and 2 531 < 4 000, so the family resolves. 🔵 **What is new is the
margin: the worst displacement this KB has measured consumes 63 % of the window, leaving 1 469 B.**
🔴 **That bound is now measured rather than assumed** — the comment at line 95 says the limit is
*"MEDIDO, NO ELEGIDO"*, and this is the specimen that prices it.

## P992 — the authority and the pristine copy differ by one byte

| source | bytes | opens with |
|---|---|---|
| `apache.org/licenses/LICENSE-2.0.txt` | **11 358** | 🔴 a blank line |
| pristine copy in a repository | **11 357** | `                                 Apache License` |

`diff` reduces to `0a1 > $` — one leading newline. 🔴 **So a byte-equality check against the
authoritative text marks every pristine repository copy "modified".** 🟢 **11 357 B is the correct
repo-side constant**, now on its third independent instance (`UniTime/unitime` p96,
`HendrikStrobelt/detecting-fake-text` p97, and the canonical compare here).

## P990 — a file named `LICENSE` is not necessarily a grant

`dssg/student-early-warning` (Data Science for Social Good, University of Chicago) serves
`LICENSE` at 2 069 B. It opens:

> BY DOWNLOADING THE STUDENT EARLY WARNING PROGRAM YOU AGREE TO THE FOLLOWING TERMS OF USE:

🔴 **Its permission sentence is BSD/MIT-shaped** — *"Permission to use, copy, modify, and distribute
this software … is hereby granted, provided that the above copyright notice, this paragraph and the
following two paragraphs appear in all copies"* — **and it is not an open-source licence.** The same
paragraph restricts the grant to *"academic research or other not-for-profit scholarly purposes …
undertaken at a non-profit or government institution"* and states that
*"educational and not-for-profit research purposes **excludes any service or part of selling a
service that uses the Program**"*, with a commercial-licence contact at the Polsky Center.

🟢 **The shared classifier answers correctly**, and not by luck: `osi_family_of` returns
`UNCLASSIFIED` (the MIT anchor is the stricter *"Permission is hereby granted, free of charge"*,
which is absent), `UNCLASSIFIED` falls through `commercial_use_ok`'s gate to the token match, and
the payload trips both `*"not-for-profit"*` and `*"excludes any service or part of selling a
service"*` — so `family_of` emits **`NONCOMMERCIAL-NOT-OSI`** and commercial use is **PROHIBITED**.

🔴 **But that branch had no software fixture.** All four fixture sets under `lib/` were Creative
Commons *content* licences (`fixtures-p551`, `fixtures-p613`, `fixtures-p845`, `fixtures-p854`).
🟢 **`lib/fixtures-p990/` is the first real-world specimen of a non-OSI non-commercial licence
applied to CODE**, committed with its provenance so the branch whose wrong answer costs the
deliverable (`P312`'s own words) can be regression-tested.

## Gap 384 — the promotion step from trending to shelf is unrecorded

Measured this pass with `grep` over the committed pages, not with a model's recollection:

| population | n |
|---|---|
| distinct slugs in the append-only history (`agents/trending.md`, `repos/trending.md`) | **1 259** |
| distinct slugs on the shelf pages (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`, `compose/patterns.md`, `intel/*.md`) | **146** |
| 🔴 in the history, on **no** shelf page | **1 119** |
| 🔴 …of those, carrying a **permissive** grant and **no** rejection marker | **528** |
| on the shelf, never in the history | 6 |

🔵 **1 119 is not the defect, and must never be cited as one.** The history is append-only and
records **rejected** candidates by design — homonyms, ungranted repos, NC licences — and those are
*correctly* absent from the shelf. A shelf is curated, not exhaustive.

🔴 **The defect is that nothing distinguishes "measured, and judged not worth shelving" from
"measured, and forgotten."** Both of this KB's recent instances are the second kind and **both were
found by accident, not by a sweep**:

- `UniTime/unitime` — pass 96 found an Apache-2.0 timetabling platform that
  `compose/code/unitime-mcp-gate/` had used since **pass 42** and no shelf page listed.
- 🔴 **The entire pronunciation/CAPT layer** — verified in the history since **pass 14**
  (`OpenPronounce`, `kaldi`, `speechocean762`, later `gopt`, `Phonos`, `open-apa`, `HiPAMA`) and
  carrying **zero** rows on `agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`
  until this pass promoted it.

🟢 **So pass 96's find was not a one-off; it was an instance of a class, and the class now has a
measured upper bound of 528.** `promotion-gap-permissive-orphans.txt` is that list, committed so a
later pass can contradict this one on the record. 🔵 **The 528 is a heuristic** — it keys on a
permissive family appearing on a line mentioning the slug, with no rejection marker on the same
lines — **so it is an upper bound on the forgotten set, not a worklist of 528 real omissions.**

🟢 **Pre-registered remedy, and it is a ledger rather than a sweep:** a row promoted to a shelf page
should record the pass that promoted it, and a candidate measured-and-declined should record the
decline. Neither exists today, which is why the question can only be answered by `grep` and only as
a bound. **The next pass that can execute code should write `promotion_ledger.sh` over the
committed pages — not a new classifier (`P237`), just the two-column fact the pages do not carry.**

## P994 — the corpus can be ungranted while every tool around it is permissive

| layer member | grant |
|---|---|
| `Halleck45/OpenPronounce` | 🟢 MIT |
| `MontrealCorpusTools/Montreal-Forced-Aligner` | 🟢 MIT |
| `lingjzhu/charsiu` | 🟢 MIT |
| `YuanGongND/gopt` | 🟢 BSD-3-Clause |
| `doheejin/HiPAMA` | 🟢 BSD-3-Clause |
| `Fuann/open-apa` | 🟢 BSD-3-Clause |
| `kaldi-asr/kaldi` | 🟢 Apache-2.0 (displaced title, `P991`) |
| 🔴 `jimbozhang/speechocean762` — **the reference corpus of the task** | 🔴 **no licence payload, 24 names** |
| 🔴 `CyanXLab/Phonos` | 🔴 **no licence payload, 24 names** |
| 🔴 `tzyll/goparrot`, `JazminVidal/gop-pykaldi` | 🔴 **no licence payload** |

🔴 **`Phonos` is a CORRECTION, not a new negative.** The history counted it inside a
*"pronunciation assessment + benchmark"* layer of three. It has **no grant**, and a layer count that
includes it overstates what is buildable.

🔵 **The consequence is specific and it is the one a client engagement hits:** the engine is MIT and
the benchmark is BSD-3, so the pipeline is shippable — **but the data that calibrates it is not
licensed**, so a deliverable either licenses a corpus or collects its own. That is a line item,
not a footnote.

## P995 — derivation is readable from the grant

`doheejin/HiPAMA` serves `LICENSE` (BSD-3-Clause, 1 526 B) whose **first** copyright line is
**`Copyright (c) 2022, Yuan Gong`** — the author of `YuanGongND/gopt` — followed by HiPAMA's own.
🟢 **The lineage the paper asserts is provable from the payload**, by the same mechanism `P800` used
for region provenance: the holder order is evidence.
