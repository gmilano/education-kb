---
industry: education
region: Global
updated: 2026-10-10
---

# `grant-ladder-v4/` — the instrument stops having a classifier of its own

**Pass 92, 2026-10-10.** ⏱️ **Second pass of this date.** Pass 91 ran 2026-10-09 23:0x → 00:00 UTC;
this one ran 2026-10-10 00:4x → 01:0x UTC. Stated because this shelf pins SHAs and two passes sharing
a date is exactly what later reads as a contradiction.

```sh
./ladder.sh moodle/moodle oat-sa/tao-core      # first-match verdict, one line per slug
./ladder.sh --all microsoft/autogen            # EVERY licence file found, and SPLIT-GRANT detection
./ladder.sh --reach                            # names=24 byte-floor=1B classifier=lib/license_family.sh
./test_ladder.sh                               # 16 cases, all offline, all real payloads
```

## Why v4 exists: v3 forked the classifier, and this base has a registered rule against it

🟢 v3 got two things right and they are kept: **SHAs are pinned**, and the **filename reach is
printable** (`P953`). 🔴 It got one thing wrong, and it is the thing `compose/code/lib/` exists for:

> **`P237`: a licence classifier must not be forked to be fixed.**

v3 inlined a fresh 30-line Python classifier instead of sourcing `../lib/license_family.sh` — the
hardened shared classifier that has been in this repository **since pass 77** and that carries the
corrections of `P171`, `P255`, `P299`, `P304`, `P308`, `P312`, `P453`, `P454`, `P561`, `P854` and
`Gap 256`. 🔴 **The fork re-imported defects the shared file had already closed. The cost is
measured, not feared, and it reached a published client recommendation.**

### What the fork got wrong — `P960`

| slug | v3 said | the payload's **title block** says | published as |
|---|---|---|---|
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 `LGPL-3.0` · 18 025 B | **GNU GENERAL PUBLIC LICENSE, Version 2, June 1991** → **GPL-2.0** | 🔴 *"LGPL: linkable"* in `repos/foundations.md` |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 `LGPL-3.0` · 18 092 B | **GNU GENERAL PUBLIC LICENSE, Version 2, June 1991** → **GPL-2.0** | 🔴 *"`i-educar` (LGPL-3.0) — link, don't absorb"* in `verticals/solutions.md` |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟡 bare `GPL` · 15 214 B | **Version 2, June 1991** → **GPL-2.0** | the version was in the payload and was dropped (`P561`) |

🔴 **The mechanism is `P171` verbatim, on a pair `P171` never covered.** The canonical GPL-2.0
**preamble** reads *"(Some other Free Software Foundation software is covered by the **GNU Lesser
General Public License** instead.)"* — measured at **byte 847** in `tao-core`'s payload and **byte
849** in `i-educar`'s, both inside v3's 4 000 B window — and v3 tested `"gnu lesser"` **before**
`"gnu general public"`. 🔴 **So the cross-reference stole the payload. Every canonical GPL-2.0 text
carries that sentence, so the defect was universal, not incidental.**

🟢 **And the natural control is in the same verdict class, from the same run.** `rosariosis` is also
GPL-2.0, but its 15 214 B variant text contains **no `"gnu lesser"` at all** (offset `-1`), so the
same classifier returned bare `GPL` for it. 🔵 **One instrument, one pass, one licence family, two
different verdicts — decided by whether a cross-reference sentence happened to be present.**

🟢 `../lib/license_family.sh` classifies on the **title block** and returns all five GNU rows
correctly. **So v4 has no classifier. It sources the shared one.** That is the entire design.

### The cost was already on the shelf, in this KB's own words

🔴 **This base had already measured both answers, in earlier passes, and then overwrote them:**

| where | what it already said |
|---|---|
| `repos/trending.md` | *"17 rows gained family precision **by reusing the shared classifier `lib/license_family.sh` (`P237`) instead of rewriting it**"* — headline row `oat-sa/tao-core`: `GPL` → **`GPL-2.0`** |
| `repos/trending.md` | *"**The row that decides a project: `oat-sa/tao-core` is GPL-2.0**"* |
| `agents/trending.md` | `\| portabilis/i-educar \| LGPL \| 🔴 **GPL-2.0** \| LATAM — Brazilian municipal school system \|` |
| `agents/trending.md` | i-educar **GPL-2.0** (`2.12/LICENSE`, *"Version 2, June 1991"*) |

🔵 **So the finding is not "tao-core is GPL-2.0" — this KB knew that. The finding is that a new
instrument re-derived a corrected value from scratch and regressed it, and nothing noticed.**
🆕 **`P963` is the check that notices.** See `../p963-shelf-licence-agreement/`.

## What v4 fixes *in the shared library*, because reuse obliges repair

🔵 **`P237` cuts both ways.** Reusing the hardened file is only an improvement if the fork's genuine
coverage travels back into it. 🟢 **Pass 100 had already written that procedure down** — `P312`'s
comment in `lib/license_family.sh` says BUSL/Elastic/PolyForm *"go in here so the rewiring is an
improvement and not a loss"* — 🔴 **and it is the procedure pass 91 did not follow.** Three repairs,
each with the real payload committed in `fixtures/`:

### `P962` — lib's CC0 branch was **unreachable for its own canonical text**

🔴 The CC0 test lived **nested inside** a gate requiring `Creative Commons` / `CC BY` within the
4 000 B title-block window. Measured on the real payload of
[`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) (`LICENSE`,
6 464 B, `d146ae6`):

| token | offset (normalised) | inside the 4 000 B window |
|---|---|---|
| `CC0` | **0** | 🟢 yes — the identity |
| `creative commons` | **6 227** | 🔴 no, by 1.6× |
| `creativecommons.org`, `CC BY`, `CC-BY` | **absent from the entire payload** | 🔴 no |

🔴 **So the gate read false and the verdict fell to `UNCLASSIFIED` on the most permissive text that
exists** — the direction of `P304`: shelf is lost, a public-domain row discarded for want of a name.

🔵 **And the detail that makes it structural rather than a window tweak: the only appearance of
"Creative Commons" in the CC0 legalcode is the clause that *disclaims* Creative Commons** — *"Creative
Commons is not a party to this document and has no duty or obligation with respect to this CC0"*.
🔴 **The gate was conditioned on a disclaimer, not on a grant.**

🔴 **And `lib`'s own suite passed 199/199 with the branch unreachable**, because its CC0 fixture is a
hand-written one-liner that *opens with the gate's own token*:

```sh
CC0='Creative Commons CC0 1.0 Universal Public Domain Dedication
```

🔵 **Three passing CC0 assertions, built on a fixture that encoded the guard instead of testing it.**
🟢 **The rule: a licence fixture is a real payload at a pinned SHA, or it is a restatement of the
code.** This is `p613`'s lesson for the third time in this base's history — there, 152 passing
assertions and 4 canonical SPDX texts coexisted with a GNU version defect.

### `P964` — reuse alone would have **lost** a family the fork knew

🔴 Re-measuring with `lib` alone moved [`leemonade/leemons`](https://github.com/leemonade/leemons)
(292★, listed under `topics/lms`) from v3's `FAIRCODE-NOT-OSI` to **`UNCLASSIFIED`**: lib knew BUSL,
Elastic and PolyForm but **not Fair Code and not the Sustainable Use License**.

🔵 **So neither classifier dominated the other** — lib read GNU and CC0 better; the fork knew two
non-OSI families lib ignored. 🔴 **And the lost direction is not neutral:** `UNCLASSIFIED` falls
through to `commercial_use_ok`'s token match, and the Sustainable Use License *grants* use
*"for commercial purposes"* before restricting resale — **so a lost non-OSI family could come back
`ALLOWED`.** Both now resolve in lib and both are denied explicitly alongside BUSL.

### `P965` — a file at a licence filename may be a **framework, not a grant**

🔴 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
publishes `LICENSE.md` (5 789 B, `65701e9`) that **grants nothing**. It *explains* a per-dataset
licensing framework: *"Code … MIT"*, *"Open … CC BY 4.0 … CC0"*, and then the clause that actually
governs — **"Gated — Not covered by an open license. Access requires Data Provider approval"**, and
**"Gated content isn't yours to redistribute by default."**

🔴 **Classifying it returned the most permissive family the document merely *mentions*** — `CC0-1.0` —
**for a payload whose operative term is the opposite.** That is the `P299`/`P954` direction: a
permission is invented. 🔵 **It is the worst of the three licence-risk shapes this base now carries:**

| shape | can filename probing see it? |
|---|---|
| `P627`/`P957` multi-**file** split | 🟢 yes, via `--all` |
| `P957` **in-file** split | 🔴 no — but there *are* grants in the file to read |
| 🆕 `P965` **framework, not a grant** | 🔴 no — and **there is no grant in the file at all** |

🟢 **The threshold is measured, not chosen.** Counting licence families *named* in the normalised
4 000 B window across all 14 real payloads in `fixtures/`:

| payload class | families named |
|---|---|
| every real grant | **0, 1 or 2** — and the 2s are always one lineage (GPL+LGPL in `tao-core`/`LTI-PHP`/`openeducat`, GPL+AGPL in `edx-platform`) |
| the framework document | 🔴 **3, from three different lineages** (MIT + CC-BY + CC0) |

🟢 **The position is measured too.** The guard runs **late**, after the title and grant anchors:
**MPL-2.0 names all three GNU marks in its §1.12** (`P454`), so a threshold of 3 applied *early*
would swallow every MPL-2.0 payload. Placed after the grant anchors, only payloads that matched no
grant anchor reach it — which is exactly the population where a framework lives.

## `P961` — the byte floor is part of the reach, and the honest result is that it cost nothing *here*

🔴 v3 accepted a payload only at **`bytes > 200`** while publishing its reach as *"24 filenames"*. So
every v3 negative was really *"24 names **and** nothing over 200 B"* — **a denominator with an
undisclosed second term**, which is `P953`'s defect in a different place. And the floor was never
hypothetical: this base owns a **real 68-byte GPL title stub**, found by `p613`.

🟢 **v4 accepts any non-empty payload and prints both terms** (`--reach` → `names=24 byte-floor=1B`).
🔵 **Measured effect on this corpus: zero.** Re-running the 15 v3 `NO-LICENCE-PAYLOAD` rows at a 1-byte
floor produced **no new positives** — no payload on this shelf sits between 1 and 200 bytes. 🟢 **So
this is a latent reach defect that cost nothing, stated as such rather than inflated into a
correction.** The reach is now printable; that is the whole claim.

## The oracle map — unchanged from v3 and re-confirmed

| probe | real slug | invented slug | discriminates? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | proxy's `200 Connection Established` only | same | 🔴 no |
| `curl -o /dev/null -w '%{http_code}'` on `github.com` or `api.github.com` | **403** | **403** | 🔴 no |
| `git ls-remote --symref https://github.com/<slug> HEAD` | ref + SHA | empty | 🟢 **yes** |
| `raw.githubusercontent.com/<slug>/<SHA>/<file>` | `200` + bytes | `404` | 🟢 **yes** |
| `WebFetch` on `github.com/topics/<t>` | renders page, stars, topic total | — | 🟢 **yes** (`curl` is 403) |

## Two-sided control — held

🟢 `moodle/moodle` → `COPYING.txt` at **35 147 B**, `main` · `f205347`. **Byte-identical to the eight
prior passes that measured it — the tenth independent reproduction.**
🟢 Two invented slugs (`zz-invented-control-a/nope`, `zz-invented-control-b/nope`) → `ABSENT`.

## This pass's census

`pass92-results.tsv` — **133 slugs**: the 122 unique slugs pass 91 resolved, **11 new rows**, and the
2 invented controls. 🔴 **Stated plainly, because pass 91 did not: that file has 133 rows and 133
unique slugs.** Pass 91's `pass91-results.tsv` published **123 rows for 122 unique slugs and claimed
"120 slugs resolved"** — `leemonade/leemons` appears **twice at the same SHA with two different
verdicts** (`FAIRCODE-NOT-OSI` and `OTHER/unclassified`), so its own verdict histogram was not a
census. 🆕 **`P966`: a census file must assert its own row count and uniqueness, or it is a log.**

## Rules it enforces

1. **No classifier of its own.** `. ../lib/license_family.sh` (`P237`). Repairs go upstream into
   that file, never into a fork (`P962`, `P964`, `P965`).
2. **Pin the SHA.** The payload is fetched at the resolved commit, never at a branch name.
3. **Classify from the title block**, never the body, never a badge, never a blog (`P171`, `P960`).
4. **Two-sided control every run**, and the control's byte count is published.
5. **The whole reach is printable** — names *and* byte floor *and* which classifier (`P953`, `P961`).
6. **Fixtures are real payloads at pinned SHAs**, committed beside the suite (`P962`).
