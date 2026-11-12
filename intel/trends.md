---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p791` — four findings, and one of them is that this base can finally PUBLISH

🟢 **Channel status, re-measured this pass:** `git ls-remote` 🟢 · blobless clone + `ls-tree` 🟢 · `git cat-file` on a `--filter=blob:none` clone 🟢 (lazy blob fetch works, and it is the cheapest byte channel this base has) · `search/repositories` 🟢 (exact integers) · `api.github.com/repos/*` 🔴 `403` · `github.com` page 🔴 `403`. Unchanged from `p790`.

🟢 **`T879-bis` — the push block is GONE, and four cycles of this base's history explain why it mattered.** `rotation.json` records, for education alone, `local-commit(421e4d7)-education-kb-push-blocked` (cycle 2) and `local-commit(4564416)-push-blocked-access-restriction` (cycle 3); the technology base records the same at `b46d379`. The cause was never GitHub — it was that `gmilano/education-kb` sat outside this session's authorised repository set, so the git proxy declined to inject a credential and returned `403` on push while `clone` succeeded. 🟢 **Attaching the repository to the session fixes it; this pass pushed.** 🔵 **The lesson is diagnostic, not clerical: a `403` on push with a working `clone` is an authorisation scope symptom, not a network one, and it should never again be recorded as "blocked" without naming the scope.**

## `T880` — `NOASSERTION` is NOT a licence verdict, and it fails in BOTH directions

🔴 **This pass found the two opposite causes of the same classifier output, in the same sector, hours apart.** GitHub's `licensee` matcher reports `NOASSERTION` when it cannot match canonical bytes. That is a statement about the matcher, not about the grant.

| Repository | `search/repositories` says | The bytes say | Why they disagree |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | `NOASSERTION` | 🔴 **`19 B`** — `License: GNU GPL V3`, blob `beca17940a71`, and **nothing else** | There is **no operative grant text at all** — only a family *name* |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | `NOASSERTION` | 🟢 **`1,150 B` valid MIT**, blob `f86101816893` | The matcher is defeated by an injected `<!-- SPDX-License-Identifier: MIT -->` HTML comment on line `3` and by **typographic curly quotes** (`“Software”`) in the operative text |

🔴 **`frappe/education` is the more consequential half, because this base already carries it** in `repos/foundations.md` and `verticals/solutions.md`. Its own siblings show what a grant looks like in the same org: [`frappe/lms`](https://github.com/frappe/lms) serves `33,893 B` and [`frappe/erpnext`](https://github.com/frappe/erpnext) serves `35,149 B` — full operative texts. `frappe/education` serves `19`.

🟡 **What that means for an engagement.** `License: GNU GPL V3` is a **stated intent**, not a licence: GPL-3.0 is granted by reproducing its terms, and a bare reference leaves the actual permission unstated. Treat the row as **intent-to-GPL-3.0** — plan for copyleft at the boundary, and get the grant confirmed in writing before any derivative ships. 🔵 It is almost certainly an oversight rather than a trap, and the fix is an upstream issue, not an avoidance.

🟢 **Rule added: `NOASSERTION` is a prompt to read the bytes, never an answer.** It joins `T875` (a long licence file may be an anthology) as the second case of a licence *signal* that cannot be graded without reading.

## `T881` — a star count this base published was inflated `23×`, and a name sweep proves it was not a namesake

🔴 **Published by this base at cycle 2 (`~9k★`) and cycle 3 (`~12k★`):** [`satvik314/educhain`](https://github.com/satvik314/educhain).

🟢 **Measured, `search/repositories` with a `repo:` qualifier — exact integer: `★388`.** MIT (`1,092 B`, blob `b46290b36e7f`), last push `2026-05-29`.

🔵 **The obvious defence is a namesake — so it was tested.** A `search/repositories` sweep on the bare name `educhain` returns, in full: `satvik314/educhain` `★388` · `lukepark327/educhain` `★22` · `SailFish-Finance/educhain-ai-agent-kit` `★6` · `EDUchain-US/EDUchain` `★3` · `Tuprott991/Educhain-AI` `★4` · `Kaustubh-1-7/crowdRaise-educhain` `★0`. 🔴 **No repository of that name anywhere exceeds `★22`.** The `~9k`/`~12k` figures were not a near-miss on a different repo; there is no candidate they could describe.

🔴 **This is the same defect class the technology base recorded** (`prior cycles' star counts were pipeline-inflated`) and it is now confirmed independently in education. 🟢 **The row survives on its licence and is corrected on its count** — MIT and genuinely useful for document-to-course generation, but it is a `★388` project with a six-month-stale tree, and it must never again be presented to a client as a `12k★` one.

## `T882` — an MIT root is not an MIT tree, and this pass found a non-OSI grant inside a `43,376★` MIT repository

🟢 [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — `★43,376`, pushed `2026-11-12`, root `LICENSE` **MIT**, `1,065 B`, blob `76abc5f13261`. 🟢 **Root grant confirmed, and the seven first-party sub-packages are MIT too** (`dsl`, `editor`, `generation`, `geometry`, `importer`, `renderer`, `storage` — each `1,065 B`).

🔴 **Then the tree was enumerated — `4,388` files — and it is not uniformly MIT:**

| Path in tree | Bytes | Grant on the bytes |
|---|---|---|
| `packages/mathml2omml/LICENSE` | `7,652 B` | 🔴 **LGPL** — vendored copyleft inside an MIT repo |
| `packages/@openmaic/renderer/font-licenses/ARPHIC-PL.txt` | `6,863 B` | 🟡 **ARPHIC Public License** (copyleft-style font grant) |
| `packages/@openmaic/renderer/font-licenses/OFL.txt` | `4,998 B` | 🟢 SIL Open Font License |
| `packages/@openmaic/renderer/font-licenses/ZcoolHappy-LICENSE.txt` | `817 B` | 🔴 **Not an OSI licence at all** — see below |

🔴 **`ZcoolHappy-LICENSE.txt` is a bespoke Chinese-language font grant** (站酷快乐体, ZCOOL). Its operative terms, read on the bytes: **free perpetual use including commercial use** (`可免费商用，永久免费授权所有人使用`), but **the font's original name may not be changed** (`禁止...改变站酷免费字体的原有名称`), **the font may not be resold as a product or used to profit as a product** (`禁止任何人将站酷免费字体作为商品进行转售及牟利`), and **attribution to the typeface designers is retained** (`造字者保留署名权`).

🟡 **What that means for an engagement.** The restrictions are mild and compatible with ordinary client delivery — but they are **not MIT**, they are **not OSI**, and they are written in a language the rest of the audit chain is not reading. Shipping OpenMAIC's `renderer` ships this grant. 🟢 **Deliverable rule: if the renderer goes to a client, carry the three font-licence files with it and keep the font names intact.** 🔴 **And an education deliverable must never resell the bundled font as an asset** — which a "template pack" or "font bundle" line item would do.

🟢 **`T882` extends `T861` (read the dependencies) and `T875` (a licence file may quote others) one layer further: read the TREE, and read it in every language it is written in.** This base has now been bitten by Spanish (`p790`, defects 1–3) and Chinese (this pass) on the same axis.

## `T883` — "EMEA" as one bucket hid an entire continent, and the gap was in the QUERY, not the territory

🔴 **The regional sweep for EMEA returned, on Africa, nothing.** The honest summary of that result was: *"For Africa, I found no useful source in these results"* and *"Africa coverage is essentially absent."*

🟢 **A single targeted query returned five named instruments and a continental strategy.** They are recorded in `intel/market.md` under `EMEA`. 🔴 **So the finding is not "Africa has no AI-education policy" — it is that a query which buckets Europe, the Middle East and Africa into one term returns European results and calls it EMEA.**

🔵 **Why this is a method finding and not a note.** This base's brief asks that an empty region be written down explicitly, because *"an informed gap is information, while silence looks exactly like coverage."* `T883` adds the failure mode one level up: **a region that is ANSWERED but answered only in part looks exactly like a region that is covered.** A composite region must be probed by its parts before any gap over it is declared. 🟢 **EMEA is now probed as Europe · Middle East · Africa separately, and the Africa row is placed.**


# Current trends — `p790`

🟢 **Byte-verified** claims concern repositories, grants, `sha`s and dependency manifests.
🔴 **Search-channel testimony** covers every market, adoption and regulatory figure (`T844`).

## `T875` — A licence file may QUOTE other licences, so substring grading is unsound in both directions

🔴 **The finding that reversed one of this base's own published verdicts, and it is a method change
rather than an erratum.** This base published, twice, that
[`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) is **PROPRIETARY**, reasoning that *"a
`39,890 B` licence file is not evidence of an open grant — it is evidence of a long one."*

🟢 **Measured.** The file is served at **`license.txt`** (lowercase, `.txt`) and is a licence
**anthology** with its own table of contents:

| § | Contents | Whose terms |
|---|---|---|
| 1 | Overview | nextSIS |
| 2 | **nextSIS GNU General Public License Version 3** | 🟢 nextSIS's own grant — **full operative GPL-3.0**, `Version 3, 29 June 2007` |
| 3 | CodeIgniter License | EllisLab, Inc. — a bundled framework |
| 4 | Twitter Bootstrap License | a bundled front end |

🔴 **The single `All rights reserved.` in `39,890` bytes is at line `703` — the second line of §3,
`Copyright (c) 2008 - 2011, EllisLab, Inc.` — and EllisLab's very next clause reads `You are
permitted to use, copy, modify, and distribute the Software`.** The line the verdict rested on is
not nextSIS's, **and the licence it belongs to is not proprietary either.**

🔴 **Then the same file defeated two more probes, differently each time.** A fresh instrument built
for this pass graded it **`AGPL-3.0`**, because **GPL-3.0's own §13 names the GNU Affero GPL**; and
its NonCommercial gate fired, because **GPL-3.0 §6 uses the word "noncommercial"**. 🔵 **Three
probes, three different wrong answers, one cause.**

🟢 **The rule, and it generalises past this row.** Grade by **anchored title lines** — a licence
title occupying its own line — and **report the set, not a family**. A file containing `N` licence
titles is an **`ANTHOLOGY`** and has no single family. `nextSIS` reads
`ANTHOLOGY[GPL-3.0, +CodeIgniter]`; **`odoo/odoo`**, the most-cited vertical platform in this sector,
reads **`ANTHOLOGY[LGPL, GPL-3.0]`** at `43,529 B` — so the education-ERP tables that call Odoo
"LGPL" are stating one of its two families.

🟢 **And read the tree, never a filename list.** `raw.githubusercontent.com` is **case-sensitive**;
`p789` missed this grant on `11` candidate paths and this pass missed it on `10`:

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/OWNER/REPO /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -iE 'licen|copying|legal|terms|notice'
```

🔵 **Relationship to the base's existing laws.** This is `metabase`'s *split-by-directory* finding
**split by section instead**, and it is `T845` (*"length is not a verdict"*) proved at **both** ends
in one pass: **`39,890` bytes was not proprietary, and `19` bytes is a real grant** —
[`frappe/education`](https://github.com/frappe/education) serves exactly `License: GNU GPL V3` and
nothing else.

## `T876` — Brazil mandated a human in the loop, not a ban, and the research channel served the superseded draft

🔴 **`Parecer CNE/CP nº 15/2026`, homologated `2026-11-10` and published in the `DOU` `2026-11-11`
(reported; primary act NOT read), gives Brazilian institutions `12` months to adapt.** Under
**`Lei nº 9.131/1995`** a CNE parecer binds only once the Minister's homologation act is published,
so the clock starts there and not at the `2026-09-01` approval.

🔴 **The version the CNE approved on `2026-09-01` prohibited AI correction of essays and
dissertative questions outright. MEC judged that too restrictive and released the use.** At least
one outlet still reports the prohibition as current, and **this base's first reading of the research
channel took that superseded draft as the rule.** 🟢 The error was caught by noticing that sources
*disagreed* and chasing the disagreement to its history — not by a better query.

🟢 **The homologated position:** AI **may assist** correction as a first filter; **the mark is
reserved to the teacher**; **no student may be penalised on an AI detector's output alone**;
**educação infantil and anos iniciais (to `5º ano`) may not use AI tools unsupervised**; individual
use is permitted from **ensino médio** upward.

🟢 **Commercially this is the best news in the LATAM block.** A human-in-the-loop grading pipeline
with a reserved teacher decision is what `P788-1` already is. 🔴 **What Brazil forbids is the
autograder that assigns the mark** — the product most vendors lead with. 🔵 **Convergence worth
naming:** Florida bars AI on graded work unless the instructor permits; New York would gate direct
student use by grade; the EU regulates assessment as Annex III high-risk; Brazil reserves the mark.
**Four jurisdictions, one regulated surface — and now an age dimension too.**

🔴 **Standing caution this trend creates.** `T858`/`p758` recorded the research channel handing this
base a **superseded federal deadline**. It has now happened again, in a different country, on the
single most decision-relevant rule in the region. 🟢 **When sources disagree about a regulation,
the disagreement is usually a *version history*, not noise — look for the draft before the
amendment.**

## `T877` — A category error can FABRICATE a region as easily as it can hide one

🟢 **`p789`'s best result was finding that Japan's "measured gap" was a category error:** the supply
was real and sat in `校務` (school administration), not tutoring. 🔴 **This pass found the same error
running backwards, and it would have produced a false placement rather than a false absence.**

🔴 **`p789` declared Tanzania a measured gap at `0`.** `elimu AI Tanzania` returns **`2`**
repositories, and one of them —
[`sangadanson1-dot/-Vet-IDEA-TZ`](https://github.com/sangadanson1-dot/-Vet-IDEA-TZ) — **is MIT,
byte-verified at `1,067 B` · `238c1bbb3bc0`**. Grant: clean. Education: present. AI: present.
Country: Tanzania. **On every field this base indexes, it discharges the gap.**

🔴 **Read in Swahili, it serves `wafugaji na wataalamu wa mifugo` — livestock keepers and veterinary
professionals — teaching `afya ya wanyama, magonjwa, chanjo, lishe`: animal health, disease,
vaccination, nutrition.** 🟢 It is real, granted, AI-bearing education. **It is veterinary extension
education, and this base is about school education.**

🔵 **The asymmetry that makes this worth a trend of its own.** A category error in the *hiding*
direction costs a pass and is recoverable — Japan was rescued. **A category error in the
*fabricating* direction is not self-correcting**: the gap closes on the shelf, the region stops being
queried, and the first time anyone finds out is when an engagement opens the row. 🔴 **`elimu` means
*education* in Swahili and the word does not distinguish schooling from extension work** — exactly
the semantic trap `T867` recorded for Korean `교육`, but with the trap set in the opposite direction.

🟢 **The gate, added to `P788-8`:** after a grant verifies, **read what the artefact teaches and to
whom, in its own language, before placing it.** A grant gate is not a relevance gate (`T873`) — and
a *relevance* gate is not a *sector* gate either.

## `T878` — A declared ecosystem is not a built one, and the honest ones say so

🟡 **[`jinlize-tech`](https://github.com/jinlize-tech/education-ai-ecosystem) is the largest
permissively-granted education-agent repository set this base has ever measured, and the claim is
true:** **`132`** repositories under the owner, **`100` of `100`** sampled carrying **Apache-2.0**,
hub licence byte-verified at `11,358 B` · `cfc7749b96f6`. The hub declares **`130` products — `97`
Skills and `33` Agents**.

🔴 **And its own README states what it has not got:** `WorkBuddy platform validation: 0/130,
NOT_EXECUTED` · `GitHub Release verified: 30/130` · *"They do not prove WorkBuddy parsing,
installation, model behavior, review, or publication."* Sampled agent repositories read
`Agent | … | Planned / 待研发` — **planned / to be developed**.

🔵 **Writing "`33` education agents, Apache-2.0" was the single largest padding opportunity available
to this base this pass, and the repository itself supplied the refutation.** 🟢 **It is carried as
`2` byte-verified rows plus a measured org count** — see `agents/top.md`.

🟢 **What it is genuinely worth is the taxonomy, and that part needs no validation at all:** an
`8`-centre decomposition of the education **back office** — 招生营销 (admissions-marketing),
教学教研 (teaching-research), 教务运营 (academic-operations), 财务运营 (finance), 人力组织 (HR),
校区标准化 (multi-campus standardisation). 🔵 **It is the first *organisational* map of education AI
this base holds** rather than another list of tutors, and it agrees with `T858` and the OECD: the
money is moving to the back office.

🔵 **The general rule for this base:** when a repository set is large and uniformly licensed,
**measure the org on the claim channel, sample it on the byte channel, and then read what the
repositories say about their own readiness** — because a set this size is usually a *plan* expressed
as repositories, and a plan is intelligence of a different kind than code.

## `T879` — In education ERP the permissive layer is not narrow, it is EMPTY — and two vendor claims do not survive a probe

🟢 **`6` education ERP / SIS platforms probed on the byte channel this pass. `0` carry MIT, Apache-2.0
or BSD.**

| Platform | Claimed | Measured on the bytes |
|---|---|---|
| **OpenEduCat** | LGPL-3 | 🟡 **LGPL** `8,241 B` — 🟢 **the only vendor claim that holds** |
| **Odoo** | LGPL | 🔴 **`ANTHOLOGY[LGPL, GPL-3.0]`** `43,529 B` — two families, not one |
| **Frappe Education** | "based on ERPNext" | 🔴 **GPL-3.0 by reference, in `19` bytes** — and **not** the AGPL-3.0 of its sibling `frappe/lms` |
| **openSIS Classic** | GPL-2.0 | 🔴 **no licence served** (`8348cd069aa2` — reproduced this base's own prior measurement as an unplanned 11th control) |
| **Fedena** | **Apache-2.0**, per a competitor's comparison table | 🔴 **REFUTED — no licence served on `10` paths** |
| **GegoK12** | **MIT**, plus *"modification, rebranding and resale are permitted"* | 🔴 **REFUTED — `gegok12/gegok12` does not exist (`rc=128`), and a GitHub-wide search for `gegok12` returns `13` results, none of them this product** |

🔴 **The most permissive claim in the entire education-ERP market has no locatable source.** 🟢 **An
MIT claim with no repository is not a finding** — the same rule as *a 404 is not a finding*, applied
to a licence rather than a URL.

🟢 **The architectural conclusion, now measured on the administrative side as well as the
instructional one.** `T852` established that the famous **LMSs** are copyleft. This pass establishes
that the **SIS/ERP** layer is too — including `nextSIS`, whose correction *adds* a copyleft open SIS
rather than a permissive one. 🔴 **So the AI layer in this sector is always an integration, never an
embed.**

🔵 **Which makes the MIT attachment points this base holds worth more than they look:**
`brightspace-d2l-mcp`, `classcharts-agent` (read-only), `teams-facultad-mcp`,
`LearningLocker/xapi-service`. 🟢 **An MIT MCP server in front of a GPL platform is the whole
architecture, not a convenience** — and it is the one shape that is deliverable in every region this
base covers.

## `T869` — In education the grant is often TWO grants, and a single-file probe reads it as none

🟢 **Education repositories ship code *and* teaching content, so they licence them separately** —
and the split is structural to the industry, not incidental. Measured this pass:

| Repo | Code | Content | How it is served |
|---|---|---|---|
| [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | 🟢 MIT `1,102 B` · `c42f19d27c4d` | 🟢 CC BY 4.0 `925 B` · `738b8fc14a61` | **Two files** — `LICENSE-CODE` and `LICENSE-CONTENT` |
| [`VictorOsondu/ai-adoption-education`](https://github.com/VictorOsondu/ai-adoption-education) | 🟢 MIT | 🟢 CC BY 4.0 | **One file**, two headed sections, `752 B` |

🔴 **Both were reported `NOASSERTION` or unlocatable by the claim channel, and both are usable.**
The first defeated this pass's probe entirely: GitHub asserted `MIT` while the byte channel found
**no licence on 11 filename paths**, because the file is named `LICENSE-CODE`. The second was
graded `CC` by a first pass that read only its opening heading and missed the MIT section below.

🟢 **The operative consequence is a question, not a flag.** For an education asset the right question
is never *"what licence is this repo?"* but **"what licence covers the code, and what licence covers
the material?"** — because the content grant is the one that decides whether a client may publish
derived worksheets, and `NC` on the content bars the engagement even when the code is MIT
(see [`nahisaho/teacher-genai-playbook`](https://github.com/nahisaho/teacher-genai-playbook),
CC BY-NC 4.0). 🔵 This is the same shape as `T864` (`paes-mcp`: MIT code, third-party exam corpus)
and `764-C`/`metabase` (split by directory) — **three different mechanisms, one lesson: the grant has
a scope, and the scope is part of the grant.**

## `T870` — Japan's supply gap was a CATEGORY error, and `T867` needs amending

🔴 **`p788` measured Japan at `3` repositories in Japanese and called it this base's only *measured*
rather than suspected gap** — a gap that had already survived translation into the local language.
🟢 **It did not survive a change of *category*.** The query `校務 AI` (*kōmu* — school
administrative duties) returns **`5`** repositories, `塾 AI 学習` (cram-school learning) returns
**`7`**, `学習指導要領 AI` (national curriculum guidelines) returns **`2`**, and two of those carry
clean MIT grants, including a full `12`-grade curriculum tree.

🟢 **`T867` said supply gaps in this base are *vocabulary* gaps. Amend it: some are *taxonomy*
gaps.** Translating "tutoring agent" into Japanese was correct and still found almost nothing,
because **Japan is not publishing tutoring agents.** It is publishing school administration and
curriculum alignment. The missing step was not a dictionary but a question: *what would this
country's teachers actually automate first?*

🔵 **And the answer differs by country in a way that is now measured, not asserted:** India publishes
**curriculum-specific tutors** (NCERT/CBSE), China publishes **evaluated multi-agent classrooms**
and commercial derivatives, Korea publishes **tutoring APIs**, Japan publishes **administrative
workflow and curriculum alignment**. 🔴 A single "APAC education agent" search term cannot find all
four, and a pass that uses one will report three absences.

## `T871` — Africa's curriculum supply is large and almost entirely ungranted

🟢 **`WAEC AI tutor` returns `35` repositories.** 🔴 **`32` of them serve no licence.**
The same ratio holds for South Africa: `CAPS curriculum South Africa AI` → **`10`**, of which **`2`**
carry a grant. Ghana: **`1`** repository, ungranted. Tanzania (`NECTA`): 🔴 **`0`**.

🟢 **The finding is the ratio, not the count.** `p788` recorded African curricula beyond Kenya and
Morocco as *"none found"*. The supply was there; what is missing is **licensing practice**, not
engineering. 🔵 And the ungranted repositories include the *best-designed* ones —
[`7irelo/aptiverse`](https://github.com/7irelo/aptiverse) (CAPS practice tests with **auditable
marking**, the highest-starred of the set) and
[`tosinamuda/teacher-agent-itu-hackathon`](https://github.com/tosinamuda/teacher-agent-itu-hackathon)
(**teacher-in-the-loop**, from the ITU AI for Good Lab). **Auditable marking and
teacher-in-the-loop are the two design choices this base recommends in every pattern it
publishes, and both are sitting in African repositories without a grant.**

🟢 **The actionable consequence:** for West and Southern African engagements the deliverable is an
**upstream licence request campaign**, not a build. Three MIT WAEC tutors and two CAPS tools exist
today; a handful of emails could double the usable set. 🔴 Until then the permissive African base is
`5` repositories plus the `66`-repo `elimu-ai` ecosystem.

## `T872` — A first-layer dependency audit is a screen, not a clearance

🟢 **`p788` audited `473` direct dependencies across `7` repositories and found `nbgrader` clean.**
🔴 **At layer 2, `nbgrader` is not clean** — `65` new transitive packages bring **MPL-2.0**
(`requests` → `certifi`) and **LGPL-2.1** (`jupyter-client` → `paramiko`).

🟢 **Both are weak copyleft and neither bars the pattern.** MPL-2.0 is file-level and triggers on
modifying `certifi`'s own files; LGPL-2.1 permits dynamic linking. `P788-1` remains deliverable.
🔴 **What changes is the sentence a client is told.** "Entirely permissive dependencies" was true of
layer 1 and is false of the graph. The accurate claim is narrower and survives diligence:
*MPL-2.0 and LGPL-2.1 are present at layer 2, both weak copyleft, neither triggered by this
deployment shape.*

🔵 **Two mechanical notes worth carrying.** First, **PEP 639 `license_expression` decided `28` of the
`65`** — a classifier-only reader would have called them `UNDECLARED`, which is the defect `p788`
recorded in its own instrument. Second, **SPDX compound expressions are mis-read in opposite
directions**: `packaging` is `Apache-2.0 OR BSD-2-Clause` (**an election** — pick one) while
`prometheus-client` is `Apache-2.0 AND BSD-2-Clause` (**cumulative** — both apply). Reading `AND`
as a choice under-states the obligation; reading `OR` as a conjunction over-states it.

🔴 **Declared boundary:** depth `3+` is unmeasured, the npm-side graphs are unmeasured at layer 2,
and these are declared ranges from registry metadata rather than resolved versions from a lockfile.

## `T873` — `tutor` is a polluted search term, and a grant gate is not a relevance gate

🔴 `tutor AI created:>2026-10-01 stars:>30` returns **`39`** repositories, and **`5` of the top `8`
are one repository re-published under five owners** — `apimartyvp957u6/api-proxy-tutorial`,
`apimartpx0d7edg8/llm-gateway-tutorial`, `apimartat5/llm-api-tutorial`,
`apimartmk8/multi-model-api-tutorial`, `apimartc30lq1/unified-ai-tutorial` — at `78`–`91★` with
byte-identical descriptions advertising a commercial API relay. 🔵 **They are not education at all;
they match because `tutor` ⊂ `tutorial`.**

🟢 **The instructive part: one of them serves a perfectly valid MIT licence** (`1,181 B` ·
`9c1378a7528b`). **A real grant on an irrelevant repository.** This base's grant gate (`P788-7`)
would pass it; only a human or a relevance gate rejects it. 🔴 Star-sorted education queries must
exclude the `tutorial` stem, and **a licence check is not evidence that a row belongs in the base.**

## `T874` — The school-operations category is a solver with an approval gate, not a chatbot

🟢 **The category `p788` recorded as empty has five permissive rows, and they agree with each other
about architecture.** Two independent rows put a **real constraint solver** at the centre —
Timefold ([`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study))
and OR-Tools ([`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable)) — with the LLM at the
edges, turning plain-English policy into constraints and explaining rejections. A third
([`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent)) puts a **human
approval step** before any schedule is written. A fourth
([`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent)) attaches to a live
school MIS **read-only**.

🟢 **Nobody in this category is asking a language model to produce a timetable**, and that is the
finding. Scheduling is a constraint-satisfaction problem with hard feasibility requirements; an LLM
that invents a plausible-looking timetable produces a school day that does not work. 🔵 The same
division of labour — deterministic core, LLM at the edges, human gate before write — is what
`P788-1` arrived at independently for grading. **Two unrelated categories converging on one
architecture is the strongest design signal this base has.**

## `T861` — A repository grant is not a dependency grant, and 4 of 7 permissive leaders carry copyleft

🟢 **Byte-verified across 7 repositories and 473 declared direct dependencies.** `ACTION p787-D`
discharged, and it is the most consequential measurement this base has made about its own
recommendations.

| Repo | Repo grant | Direct deps | Copyleft in the first layer |
|---|---|---|---|
| `oppia/oppia` | Apache-2.0 | `171` | 🔴 **`angular-shepherd` — AGPL-3.0** |
| `learningequality/kolibri` | MIT | `32` | 🔴 `zeroconf-py2compat` LGPL-2 · `json-schema-validator` LGPL |
| `HKUDS/DeepTutor` | Apache-2.0 | `27` | 🔴 `pyte` LGPL-3.0 |
| `THU-MAIC/OpenMAIC` | MIT | `181` | 🔴 `mathml2omml` LGPL-3.0-or-later · 🟡 `jszip` `MIT OR GPL-3.0-or-later` |
| `CAHLR/OATutor` | MIT | `43` | 🟢 none |
| `jupyter/nbgrader` | BSD-3 | `18` | 🟢 none |
| `zijinz456/OpenTutor` | MIT | `1` | 🟢 none |

🔴 **The sharpest row is Oppia.** This base files Oppia under *"build on these, link them, **ship
them in client code**"*. It depends on an **AGPL-3.0** front-end library, and AGPL's trigger is
network delivery — which is exactly how a browser bundle reaches a learner.

🔵 **Three consequences a studio should act on.**
1. 🟢 **The flagship pattern survives unchanged.** `nbgrader` and `OATutor`, the two components
   `P788-1` rests on, are the two that audit clean. That was luck; it is now a documented reason.
2. 🟡 **LGPL is survivable, AGPL is not.** Python and Node both link dynamically, so Kolibri and
   DeepTutor stay usable provided the LGPL component remains replaceable and its source available.
   Oppia's AGPL dependency must be removed or replaced, not managed.
3. 🟡 **A dual grant is permissive only once you elect it.** `jszip` is `MIT OR GPL-3.0-or-later`.
   Election is a decision with a date and an author, not an assumption.

🔴 **And state the limit of the measurement honestly: this is the FIRST dependency layer only.**
Transitive dependencies were not audited. The first layer was already enough to change four rows,
so the second will change more.

## `T862` — The EMEA agent gap was an artefact of English-only querying, and it is refuted

🔴 **`T856` is REFUTED, not refined.** `p787` recorded: *"no European-origin education agent
repository surfaced … Europe is building the substrate and not the education layer on top of it."*
🟢 **Querying the same slot in the languages Europe actually writes in returned agents on the first
attempt**, and six are byte-verified in `agents/top.md`:

| Query | Language | Result |
|---|---|---|
| `tutor education AI Germany France Netherlands Spain` | 🔴 English | **`0`** |
| `onderwijs AI agent` | 🟢 Dutch | **`1`** — `onderwijsin/agents`, MIT |
| `tuteur IA education` | 🟢 French | **`9`** — incl. `sherpa`, `dowze`, `parcours-maths-ia`, all MIT |
| `KI Unterricht Agent` | 🟢 German | **`2`** — incl. a Swiss LP21-curriculum agent |

🟢 **Plus `elimu-ai`: 66 repositories, MIT, an African education ecosystem pushed this week** — and
**this base was already citing it** at `agents/trending.md:24964` without ever placing it.

🔵 **The lesson generalises past Europe, and it is the same lesson as `T848`.** An instrument written
in English, against American naming conventions, with a star floor, will under-report every region
that is not the United States. This base has now been caught doing that **twice** — once on a
licence probe (`T848`, Spanish MIT read as no grant) and once on a discovery query (here). 🔴 **Both
times the under-reported regions were the two the base is explicitly told to serve.**

## `T863` — Six defects in one pass's own instruments, and four are biased against non-English grants

🟢 **Every one was caught by a control on a row this base had already published; none by inspection.**

| | Failure mode | How it showed up | Fix |
|---|---|---|---|
| 🔴 **NEW** | **Trailing-newline erasure** | `$(curl …)` strips the trailing newline, so **every** licence in the pass measured exactly `1 B` short — `11,407` against the recorded `11,408`, six for six | Bytes counted **on the file**, never through command substitution |
| 🔴 **NEW** | **Single-rendering translation matching** | The `T848` fix matched *one* Spanish rendering. `paes-mcp` says `partes sustanciales`; the probe required `porciones sustanciales` — **the repaired probe still scored a valid Spanish MIT as `UNGRADED`** | Every clause matched as a **set** of circulating renderings per language |
| 🔴 **NEW** | **Byte-wise accent blindness** | `SIN GARANT.A` cannot match `SIN GARANTÍA`: `grep` matches bytes, and `Í` is two of them, so `.` fails. 🔴 **The fix for language-blindness was itself defeated by the locale** | Patterns ASCII-only up to the first accent; locale declared explicitly |
| 🔴 **NEW** | **Fixed-window title search** | `p787` widened the title check to 5 lines for Odoo's line-3 deferral. `INGInious` defers to **line 9** behind a prose scope caveat, and graded `UNGRADED` — against a grant this base had already correctly recorded as AGPL-3.0 | The title is **found by scanning for a line that *is* a licence title**, at any depth. A fixed line budget is the wrong instrument and the next file will exceed any budget chosen |
| 🔴 **NEW** | **Abbreviation blindness** | `frappe/education` serves **19 bytes**: `License: GNU GPL V3`. Matching only expanded names scored a real grant `UNGRADED` | Abbreviations (`GPL`, `AGPL`, `LGPL`, `v3`) graded as titles |
| 🔴 **NEW** | **Metadata-field blindness** (dependency instrument) | PyPI's legacy `license` field is empty for modern packages, so `pydantic`, `tenacity`, `typer`, `jsonschema` and `packaging` all reported `NONE-DECLARED` — 5 false absences on the first dependency audit this base has ever run | **PEP 639 `license_expression`** read first, then classifiers, then the legacy field |

🔴 **Three of these six under-report non-English grants specifically**, and a fourth under-reports
short grants. 🟢 **The two corrections they produced on already-published rows:**

- **`luscitiosus/Dirigo`** — published as *"a Latin boast and no grant of any kind"*. The Latin is
  line 1; **lines 3–5 grant CC BY-NC-SA 4.0 in Spanish** with a link to the Spanish legal code.
  Still barred commercially, 🔴 **but the published reason was false** and NonCommercial is a harder
  bar than an absence.
- **`MyScript/MyScriptJS`** — published as a *"proprietary notice"* at `570 B`, left `UNGRADED`.
  The bytes are the **standard Apache-2.0 grant-by-reference boilerplate**, URL and AS-IS clause
  included. 🟢 **Removed from the unusable class.** It was dismissed for being short, which is
  precisely what `T845` forbids.

🔵 **Seven recorded failure modes have now become thirteen**, and the pattern across all of them is
one sentence: **a licence probe fails in whichever direction its author's defaults point.**

## `T864` — The grant covers the code; the corpus belongs to someone else

🟢 **Byte-verified, and it corrects a pattern this base shipped.** `goyanedelv/paes-mcp` is MIT —
and its licence text states in terms that the grant covers **the source code and the documentation
only**, and does *not* and *could* not cover the PAES question stems, figures and answer keys, whose
rights belong to **DEMRE, Universidad de Chile**. That material is included from freely published
official sources, for educational use, with attribution.

🔴 **`P787-3` was written as though the exam corpus were MIT.** It is not. The pattern is repaired as
`P788-3` with the boundary explicit.

🔵 **This is the third time this base has made the same mistake**, and it is now a rule rather than
an anecdote: `legalize-dev/legalize-pt` (MIT for a *different* repository, Portuguese statutes under
public-sector open data), `Dirigo` (CC BY-NC-SA for the code, BOE/BOC statutory texts excluded), and
now `paes-mcp`. 🟢 **In education this will be the normal case, not the exception** — exam items,
textbooks and curricula are the assets with rights-holders, and the repository that wraps them is
the cheap part. **Read the scope clause, and ask who owns the content** before costing a deliverable
on it.

## `T865` — Identical `HEAD` proves two addresses are one project, with no page read

🟢 **`ACTION p787-G` discharged mechanically.** `p787` recorded that the only evidence separating a
fork from a distinct project was the fork notice on the github.com page. 🔴 **That page returns `403`
this pass.** 🟢 `lehrer-tools/lehrer-agent` and `NikolasSchaeffner/lehrer-agent` both resolve to
`3ddcfbbabc560675914da9703f53101c1c4d5123` — **the same commit**. One German teacher agent, carried
by this base as two separate ungranted rows.

🔵 **This is a better instrument than the one `p787` asked for.** It needs no page, no API and no
licence fetch: `git ls-remote` already returns the discriminating value, and two addresses sharing a
`HEAD` are one project until proven otherwise. 🟢 **It is also cheap enough to run on every row**,
which the page read never was.

## `T860` — The page channel closed; the claim channel got better

🔴 **Channel status changed between `p787` and `p788`, and it must be stated rather than assumed.**
`github.com` and `api.github.com/repos/{owner}/{repo}` now return **`403`** through this session's
proxy for every non-attached repository — so `p787`'s page-read star counts cannot be reproduced by
the method that produced them.

🟢 **The replacement is better than what it replaces.** `search/repositories` with `repo:` qualifiers
is reachable and returns **exact integers**: DeepTutor `58,508`, OpenMAIC `43,365`,
`agent_skills` `6,813`, `hedyorg/hedy` `1,697`, Kolibri `1,176`, OATutor `279`, OpenTutor `175`.
🔵 **Every one reproduces `p787`'s rounded page figure** (`58.5k`, `43.4k`, `6.6k`, `1,697`, `1.2k`,
`279`, `175`), which both validates the new channel and retires the old one. 🟢 **Stars in this base
are now exact and dated, not rounded** — and still claim-channel, so still weaker evidence than a
licence byte.

## `T866` — South Korea binds education, so APAC is no longer the low-regulation region

🔴 **Search-channel, and it overturns this base's APAC position.** `p787` recorded APAC as *"the
region with the strongest open-source agent supply and the weakest binding regulation"*, naming
**Vietnam** as its one binding education hook. 🔴 **South Korea's AI Basic Act (Act No. 20676) took
effect `2026-01-22`** — a risk-based statute with mandatory transparency and impact assessment for
**high-impact AI**, and the high-impact category **names education explicitly**, alongside
healthcare, finance, employment and essential services.

🟢 **So the regional story is now: Korea and the EU both bind education; the US binds it state by
state; Japan does not bind it at all.**

| Jurisdiction | Instrument | Binding on education? |
|---|---|---|
| 🟢 **South Korea** | **AI Basic Act, Act No. 20676, in force `2026-01-22`** | 🔴 **Yes — education named as high-impact AI** |
| EU | AI Act Annex III point 3; Reg. (EU) 2026/1744 defers to `2027-12-02` | 🔴 Yes |
| Vietnam | 2026-07 high-risk sector list, citing automated assessment | 🔴 Yes |
| Japan | AI Promotion Act (2025); AI Basic Plan `2026-07-14` | 🟢 **No penalties, no risk tiers** |
| India | Amended IT Rules from `2026-02-20` | 🟡 Provenance labelling only |
| China | Sector measures; Cybersecurity Law AI clause from `2026-01-01` | 🟡 Not education-specific |

🔵 **Commercially this is the most actionable regulatory change in the pass**, because Korea's
statute is **already in force** while the EU's education obligations are 13 months out. An APAC
engagement in Korea is remediation work today.

## `T867` — Supply gaps in this base are vocabulary gaps

🟢 **Measured on the claim channel, `ACTION p787-F` discharged.** The same slot, queried two ways:

| Country | English query | Result | In-vocabulary query | Result |
|---|---|---|---|---|
| India | `tutor agent education India CBSE NCERT curriculum` | 🔴 **`0`** | `NCERT AI` | 🟢 **`330`** |
| Netherlands | `tutor education AI … Netherlands` | 🔴 **`0`** | `onderwijs AI agent` | 🟢 **`1`** (MIT) |
| Korea | — | — | `AI 교육 에이전트` | 🔴 **`20`, almost none relevant** |
| Korea | — | — | `학습 튜터 AI` | 🟢 **`12`, relevant** |
| Japan | — | — | `AI 教育 エージェント` | 🔴 **`3` — a real gap** |

🔴 **Korea carries a semantic trap worth recording:** **교육** means both *education* and *corporate
training*, so the obvious query returns agent-training **course material** — a Samsung practitioner
curriculum, "AI maestro" coursework — rather than education agents. The productive term was
**학습** (*learning*).

🟢 **Japan is the one gap that survived in-language querying**, which makes it this base's only
*measured* rather than *suspected* supply gap. Its best artefact,
`narumi-mase/osaka-lesson-dataset` (Osaka City Education Center lesson plans), serves **no licence**.

🔵 **The operating rule:** before recording a regional absence, query in the region's language and
in the region's own curriculum vocabulary — `NCERT`, `CBSE`, `PAES`, `LP21`, `CBC`, `Bac`. **A gap
found in English is a gap in the query.**

## `T851` — Tutoring is packaged as a *skill*, and the derivative arrived in six days

🟢 **Byte-verified, and now with downstream evidence.** `janestreet/agent_skills` (MIT, `1,120 B`,
`6,813★`) ships `socratic-tutor/` as a prompt-and-protocol directory: diagnostic, skill map at
levels 0–5, one question at a time, spaced review, final assessment. 🟢 **`nuwaves/socratic-tutor`
(MIT, `1,143 B`, created `2026-11-09`) is the same skill extracted as a standalone installable unit
with saved progress** — a third party re-packaged it within a week.

🔵 **Why this remains the cheapest viable unit of educational IP:** no runtime, no server, no model
dependency; reviewable by a curriculum specialist who cannot read code; versionable in git; portable
across whichever model the client already bought. 🟢 `myvipbackup2/china-k12-teacher-skills`
(Apache-2.0) is the same pattern applied to a national curriculum, and `onderwijsin/agents` (MIT) is
the Dutch one.

## `T868` — A localised derivative can be *less* usable than its parent

🟢 **Byte-verified, and new.** `dpaul0501/OpenVidya` is OpenMAIC *"redesigned for NCERT/CBSE"* — the
exact localisation move `P787-5` recommends. 🔴 **Its grant is AGPL-3.0, where OpenMAIC's is MIT.**

🔵 MIT permits relicensing a derivative under AGPL, so nothing improper happened. But the
consequence matters for a studio: **the India-localised classroom cannot be embedded in a client
deliverable the way its permissive parent can.** 🟢 **The practical reading: localise OpenMAIC
yourself from the MIT parent rather than adopting a copyleft fork of it** — and check the grant of
any localisation before treating it as a shortcut.

## `T852` — The permissive layer is narrow, and it is not where the famous names are

🟢 **Byte-verified across 38 foundational repositories this pass: 18 permissive, 18 copyleft,
2 EUPL-1.2.** The split follows institutional history, not chance.

| The names a client will say | Grant | The permissive repo that does the same job |
|---|---|---|
| Moodle | 🔴 GPL-3.0 | Sakai (ECL-2.0) · OpenOLAT (Apache-2.0) |
| Open edX · Canvas | 🔴 AGPL-3.0 | Sakai (ECL-2.0) |
| D2L Brightspace | proprietary SaaS | 🟢 `brightspace-d2l-mcp` (MIT) — attach, don't replace |
| H5P content types | 🔴 GPL-3.0 | `Khan/perseus` (MIT) |
| edx-ora2 assessment | 🔴 AGPL-3.0 | `jupyter/nbgrader` (BSD-3) |
| xAPI / learning records | — | 🟢 `LearningLocker/xapi-service` (MIT) — **rescued this pass** |
| Anki scheduling | 🔴 AGPL-3.0 | — 🔴 no permissive equivalent in this base |

🟢 `csev/tsugi` (Apache-2.0) remains the most useful licensing component in education open source,
because **LTI across a process boundary** lets permissive code serve a copyleft LMS without becoming
a derivative work of it.

## `T853` / `T854` — Regulation bifurcated, and assessment is the regulated surface everywhere

🔴 **Search-channel, carried and re-confirmed.** 🟢 **EU:** Regulation (EU) 2026/1744 (*Digital
Omnibus on AI*), OJ `2026-07-24`, in force `2026-07-27`, moved Annex III stand-alone high-risk —
education included — from `2026-08-02` to **`2027-12-02`**. 🔴 **Not** deferred: Art. 5 prohibitions
and Art. 4 AI literacy (live since `2025-02-02`, **including the emotion-recognition ban in
education**), and Art. 50 transparency from `2026-08-02`. The Commission's own FAQ confirms
supervision and enforcement rules apply from `2026-08-02`, and that the AI-literacy duty already
applies; **Art. 4 is enforced by national market surveillance authorities, not the AI Office.**

🟢 **North America is enacting now, not pending:** **Idaho, Maryland, Oklahoma and Virginia** all
enacted education-specific AI measures in 2026; **Maryland SB 720 / HB 1057** direct the state
education department to issue guidance and require local AI policies; **California AB 1159** bars
using student data to train AI models; **Ohio's** district AI-policy mandate had a July 2026
deadline; **North Carolina** defended a **`$10M`** earmark in **Senate Bill 1006** to fund Khanmigo
tutoring statewide; **New York City** issued traffic-light guidance in March 2026. 🔴 **Do not quote
tracker totals** — `134` bills / `31` states and `68` / `27` circulate simultaneously, and guidance
counts range `33`–`35+`. **Cite the bill.**

🟢 **One architecture satisfies every jurisdiction that regulates assessment** — EU Annex III
(admissions, learning outcomes, education levels, **exam proctoring**), Korea (high-impact),
Vietnam (automated assessment), Oklahoma (AI used **solely** for grading, discipline or promotion),
New York A 9190 (grade floor): **AI proposes, a named human decides, and the system keeps an audit
trail joining the proposal, the evidence and the decision-maker.** 🔵 The word doing the work in
Oklahoma's statute is **"solely"** — it regulates *autonomy*, not assistance, so human-in-the-loop
is the product rather than a compliance tax. `jupyter/nbgrader` (BSD-3, **and `0` copyleft
dependencies**) already has that shape, which is why it anchors `P788-1`.

## `T855` — LATAM adoption has outrun LATAM governance by about 60 points

🔴 **Search-channel.** Teacher AI use in the past year (TALIS 2024): **Brazil `56%`, Chile `55%`,
Colombia `53%`, Costa Rica `52%`** against an **OECD average of `36%`**. UNESCO's observatory launch
reports **more than `50%`** of teachers already using these tools in countries such as Chile and
Brazil, while **fewer than `10%`** of regional institutions have formal guidelines. `87%` of regional
universities use AI, **`26%`** have a strategy, **`9%`** evaluate it (UNESCO IESALC); in Brazilian
schools `53%` of administrators use AI and **`22%`** report any guidelines (Cetic.br).

🟢 **New this pass, and it changes the regulatory read:** general AI bills are now **moving** —
**Brazil's comprehensive AI bill is in the Chamber of Deputies** (so the text can still change), and
**Chile has a government-sponsored risk-based bill** tied to its forthcoming data-protection
authority. 🔴 **Mexico remains the laggard: multiple bills introduced, none enacted.** 🔴 **Still no
AI-in-*education* statute in Brazil, Mexico or Chile** — the governing layer remains UNESCO-convened
soft governance. A regional index (October 2026) adds that all `20` countries offer postgraduate AI
programmes, `65%` have specialised research centres, and **more than half have incorporated AI into
school curricula**; Brazil holds **`87.7%`** of the GPUs in that study's coverage.

🔵 **The strategic reading is unchanged and now better evidenced.** This is not a market to be
*introduced* to AI — that already happened, bottom-up, through teachers. It is a market that needs
its existing, ungoverned use made defensible. The buying trigger is institutional risk and the
readiness gap, not a deadline.

## `T858` — Purpose-built is displacing general-purpose, and the commits agree with the commentary

🔴 **Search-channel.** The OECD's 2026 Digital Education Outlook recommends moving **beyond
general-purpose AI tools toward purpose-built educational AI** designed for durable learning gains;
1EdTech frames 2026 as the shift **from experimentation to governance**.

🟢 **Byte-verified corroboration, which is the useful part — and it got stronger this pass.** Of the
30 agents new to this base, the ones with traction are curriculum- and instrument-specific rather
than general: an NCERT/CBSE classroom, a PAES admissions MCP server, a Swiss LP21 lesson planner, a
Mexican Sign Language tutor, a Greek etymology tutor with an MCP server, a storybook **reading-level
model**, a Socratic protocol extracted as an installable skill. 🔵 **Nothing in this pass's new
supply is a general-purpose chatbot.**

## `T859` — A national AI policy was withdrawn for citing sources AI invented

🔴 **Search-channel, carried.** South Africa's draft National AI Policy was gazetted as **Notice 3880
of 2026 on `2026-04-10`** and **withdrawn on `2026-04-26`** by Minister Solly Malatsi, after
fabricated, AI-hallucinated citations were found in its reference list — reportedly **at least 6 of
its 67** academic citations. One source records abrogation on `2026-04-27`, so 🔴 **cite both
dates**. A seven-person panel is reviewing it with no published timeline; the Department of Basic
Education's **National AI in Education Framework** remains 🔴 **unpublished, with no timeline**.

🔵 **Keep this row.** It is the most persuasive provenance argument available in an education
engagement: the failure mode was not a model hallucinating in a classroom but **an AI-drafted
governance document failing its own review**. 🟢 **And this pass adds the component that answers it:**
`SeydinaBANE/sherpa` (MIT, EMEA) is a tutor built on **grounded RAG with citations** — provenance as
an architectural property rather than a policy promise.
