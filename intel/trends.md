---
industry: education
region: Global
updated: 2026-10-27
---
## 🆕 `p481` — `2026-10-27` — **🟢 THE TREND THIS PASS CORRECTS IS ONE THIS BASE CREATED: "non-canonical Apache-2.0 is circulating" is **half true and half an artefact of the wrong instrument**. Measured against the licensor's own text at word level, **7 of 13** education Apache repositories grant exactly the canonical terms despite differing byte counts; **6** do not, and **one has a clause narrowed**. 🟢 And the deeper trend is in agent safety: the best-guarded repository on this shelf publishes, in its own source, that the control pattern this base has been recommending **does not do what this base said it does**.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — harness refuses `Code from
External`. Nothing cloned this pass was executed (`Gap 481-A`).

---

### 🟢 Trend 1 — the licence *label* and the licence *grant* have come apart, and only a word-level diff separates them

| instrument | verdict on the same 13 Apache-2.0 repositories |
|---|---|
| `license.spdx_id` from the search API | 13 of 13 "Apache-2.0" — **no variance visible at all** |
| byte count vs canonical (11,358 B) | 13 of 13 "non-canonical" — **variance over-reported** |
| **word-level diff of the operative text** (1,413 tokens) | 🟢 **7 verbatim** · 🔴 **6 altered** |

🔵 This is the trend with the most direct commercial consequence on the shelf: a studio's licence diligence is
usually a metadata read, and metadata cannot see any of this. The appendix that Apache-2.0 *instructs* you to
fill in accounts for most byte differences — so byte comparison manufactures false positives, and label
comparison manufactures false negatives. Only one of the three instruments answers the question.

### 🟢 Trend 2 — the circulating rendering is confirmed, bounded below, and crosses regions

`p480` saw two repositories sharing three deviations and could say nothing about spread. A two-marker
fingerprint — `submitted to **the** Licensor` co-occurring with `excluding **any** notices` — now identifies the
rendering on **three** repositories and on **no other row** in the panel: `HKUDS/DeepTutor` (Hong Kong),
`SimonsTang/feifei-companion` (APAC), `ANFAIA/SkillNet` (Spain).

🔵 It crosses APAC and EMEA, which argues for a shared *text source* — a template, a translation round-trip, or
a generated file — rather than one organisation's house style. 🔴 No provenance was found, and the prevalence is
a **floor of 3**, not a measurement (`Gap 481-AH`).

### 🔴 Trend 3 — one row narrows a clause, and it is not the small one

`beltromatti/get-it` (1,135★) deletes **"reasonable and customary use in"** from § 6 Trademarks, so the
carve-out reads *"except as required for describing the origin of the Work"*. The reasonableness qualifier is
gone. Across 13 repositories this is the **only** deviation that changes what a licence permits rather than how
it is worded — and it sits on the second-most-starred row in the panel, a hackathon project from Milan.

🔵 The usable generalisation: deviations cluster in *definitions* (inert, as far as this base can judge) and in
*punctuation* (`onemnemo/mnemo`, § 8) and *reflow* (`tsugiproject/tsugi`, § 4 enumerators) — but not
exclusively. One in thirteen touched a permission. That rate is the reason to read the file.

### 🟢 Trend 4 — agent safety is professionalising, and the leading implementation is candid about its own limits

The strongest evidence this pass is not a count but a document. `vishalsachdev/canvas-mcp` ships a four-layer
control model (operator allowlist → registration gates → confirmation guards → MCP client approval), a declared
effect taxonomy over all **130** tools (72 read · 52 Canvas-write · 4 local-write · 1 code-exec), **21**
single-use content-bound guards, 60+ security test files, and a reference to a published advisory
(**GHSA-hmr8-mvr2-mvw5**) describing the exact attack: a student plants instructions in content the instructor's
assistant later reads.

🔴 **And it states the limit this base had wrong.** A confirmation token binds a request; *"it does NOT prove
that a person saw or approved the preview. The model receives the token and can redeem it itself."* The only
boundary a prompt injection cannot talk past is the one the model has no hand in — `ALLOWED_WRITE_TOOLS`, fixed
by the operator in the environment. 🔵 Trend, stated plainly: **the control that works is configuration, not
conversation.** Recipes built on preview-and-confirm alone have been mislabelling the human-approval step, and
`compose/patterns.md` is corrected this pass.

### 🟢 Trend 5 — the agent surface is migrating *into* the platform

`p480` found the unit of supply to be a skill or a standalone MCP server. Two rows read this pass complicate
that: `Selleo/mentingo` (MIT LMS) ships `apps/api/src/mcp/` — admin tools, customization tools, upload tools, a
content resource, an auth guard and an **OAuth consent controller** — as part of the platform, with Langfuse
tracing alongside. `ArnaudGuiovanna/tutor-mcp` is 171k LOC of **Go** with auth middleware, which is a different
engineering posture from a 1,276-LOC single-purpose server.

🔵 Consequence: the integration question is shifting from *"which MCP server do we bolt on"* to *"does the
platform own the consent screen"* — and a platform that does can obtain a human decision the agent never
mediates. 🔴 Read at profile depth only (`Gap 481-G`).

### 🟡 Trend 6 — attention concentration held three hours, then narrowed

| measure | `p479` | `p480` | `p481` |
|---|---|---|---|
| `HKUDS/DeepTutor` | 94.0 ★/h | 114.6 ★/h | **117.7 ★/h** |
| concentration vs rest of panel | 31.5 : 1 (7 rows) | 24.6 : 1 (3 rows) | **19.8 : 1** (3 rows) |

🔵 Three consecutive hourly intervals with the leader between 94 and 118 ★/h is the most stable series this base
has. The **narrowing** is the new information, and the honest reading is that it is weak: the two comparison
rows moved +6 where they moved +5, and ±1★ on a 354★ repository moves the ratio several points
(`Gap 481-E`).

### 🔴 Trend 7 — regulation is converging on a shape, and the earliest hard education deadline is now APAC's

Education is being written into high-risk schedules across three regions, with the **EU's deferred to 2 December
2027** and **Vietnam's landing first, 1 March 2027**. North America is regulating by *guardrail* — Oklahoma and
Maryland barring AI from high-stakes student decisions, NYC placing grading, discipline and placement in a
prohibited tier — rather than by conformity assessment. 🔵 The convergent pattern across all three: **grading,
admissions and proctoring are the regulated surface; tutoring and content generation largely are not.** That is
where a studio's deployable scope sits. 🔴 Entirely secondary-sourced (`Gap 481-AC`).

### 🔴 Trend 8 — efficacy: unmoved, and still unreadable from here

No change. Every efficacy figure this base carries, the −0.37 SD included, remains a search-tool summary of a
paper it cannot open; `arxiv.org`, `edworkingpapers.com` and `eur-lex.europa.eu` are all refused or unresolved
at this gateway. This pass did not improve the position and declines to restate it as if it had.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 481-AI`** | **`Gap 480-AI` unchanged — no study read first-hand.** Stated above rather than quietly dropped. |
| 🔴 **`Gap 481-AJ`** | **Trend 1 and Trend 2 rest on 13 repositories** from `topic:edtech license:apache-2.0` plus two `topic:ai-tutor` rows — not the Apache subset of the 305-row union (`Gap 480-C`). The 7/6 split is a property of this panel; the rendering's prevalence is a floor of 3 with **no upper bound measured**. |
| 🔴 **`Gap 481-AK`** | **Trend 4 is one repository's source, unexecuted** (`Gap 481-A`, `Gap 481-B`). The four-layer model is verified as *written* — the policy file, the guard module and the test filenames were read — and **not** verified to hold at runtime. No security test was run. |
| 🟡 **`Gap 481-AL`** | **Trend 5 generalises from two clones**, one of which (`mentingo`) was read at profile depth with its consent controller identified by filename and not read (`Gap 481-G`). Whether its MCP tools are write-guarded at all is unknown. |
| 🟡 **`Gap 481-AM`** | **Trend 6 is three one-hour intervals on three rows.** Five of `p479`'s eight panel rows have now gone two passes without a re-read (`Gap 481-E`), so "the tier is flat apart from the leader" remains a claim about a narrow panel. |
| 🟡 **`Gap 481-AN`** | **Trend 3's "one in thirteen touched a permission" is a rate over this panel only**, and whether the `get-it` deletion was deliberate, generated or copied is unknown — no provenance was sought beyond the file itself. |
## 🆕 `p480` — `2026-10-27` — **🟢 THE TREND THIS PASS CAN MEASURE THAT NO PREVIOUS ONE COULD IS A LICENSING TREND, AND IT IS A WARNING: with the topic filter removed, **19% of 305 live education-AI repositories declare no grant at all** and permissive share falls from 76% to **50%** — and the two Apache-2.0 files read byte-for-byte this pass are **both non-canonical, with the same three deviations**. 🟢 Attention stays concentrated **24.6 : 1** in one repository, now across a third interval. 🔴 The efficacy literature is unmoved and unreadable from here.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — harness refuses `Code from
External`. **Nothing below is gate-attested.** Frontmatter, closed-vocabulary `region`, pipe-counts,
no-header-as-data and prepend-only re-checked in this session's own code.

---

### 🟢 Trend 1 — the grant, not the architecture, is where this tier is drifting

🔵 Measured across the 305-row live union, not a sample:

| grant class | rows | share |
|---|---|---|
| 🟢 permissive (MIT 126 · Apache-2.0 20 · BSD-3-Clause 7 · ISC 1) | 154 | **50%** |
| 🔴 **no grant declared** | **57** | **19%** |
| 🟡 `NOASSERTION` — present but unclassifiable | 38 | 12% |
| 🔴 copyleft (GPL-3.0 18 · AGPL-3.0 17 · others 10) | 45 | 15% |
| 🟡 Creative Commons | 11 | 4% |

🔴 **Nearly one row in five cannot legally be built on, and nearly one in three cannot be costed without a human
reading a file.** 🟢 The sharpest instance is on `agents/top.md`: the **second-most-starred AI-tutor repository
on GitHub, at 29,550★, carries no grant on any channel** — exclusive copyright. 🔵 The trend statement is
therefore not "open source is winning education AI" but **"attention and licensability are decoupling"**, and
this is the first pass with a population measurement behind that claim rather than an impression.

### 🟢 Trend 2 — a non-canonical Apache-2.0 is circulating in APAC education AI

🔵 Two Apache-2.0 rows were diffed against `apache.org/licenses/LICENSE-2.0.txt` this pass. **Both differ from
the control, and they differ in the same three places**
([`evidence/apache-body-deviations.2026-10-27-p480.tsv`](../evidence/apache-body-deviations.2026-10-27-p480.tsv)):
"submitted to **the** Licensor", "received by **the** Licensor", and §4's "excluding **any** notices" for
"excluding **those** notices". 🔵 The control and `canvas-lms` carry none of the three.

🟢 **Two independently authored projects do not make the same three edits by chance** — they share a rendering.
Both are APAC-origin on a first-hand licence-file read: `HKUDS/DeepTutor` names *"Data Intelligence Lab, The
University of Hong Kong"*, `SimonsTang/feifei-companion` names *"Xue Lai Xue Qu Learning Society"*.
🔵 **The operational consequence, which is all this base can assert:** a digest- or byte-count-based licence
scanner **will flag these rows**, and whether "any" versus "those" in §4 alters legal effect is a determination
this base cannot make. A studio sourcing APAC education-AI components should budget for reading licence text.

### 🟡 Trend 3 — attention concentration holds across a third interval

🔵 `t1` is `p479`'s own 11:50:25Z read; `t2` is 12:54:50Z
([`evidence/star-velocity.2026-10-27-p480.tsv`](../evidence/star-velocity.2026-10-27-p480.tsv)):

| measure | `p479` | `p480` |
|---|---|---|
| DeepTutor rate | 94.0 ★/h (80.6–107.4) | **114.6 ★/h (94.4–134.8)** |
| multiple of its own lifetime average | 15.2× | **18.5×** (lifetime 148.3 ★/day = 6.18 ★/h over 303 days) |
| concentration vs the rest of the panel | 31.5 : 1 over 7 rows | **24.6 : 1** over 3 rows |

🟢 The two Poisson intervals **overlap**, so the measurements are consistent while the point estimate rises.
🔴 **But the trend claim is weaker than the numbers look**: only one repository in the panel moves enough to
have a rate at all, so "the tier is flat" remains a statement about hours, not weeks (`Gap 480-D`).

### 🟢 Trend 4 — the unit of supply is a skill or an MCP server, and the clone tier now shows what that costs

🔵 `p479` counted 12 of 25 census rows as agent skills or MCP servers rather than applications. 🟢 This pass read
one of them in full and the finding generalises into a **cost**, not just a shape:
`boyuchengz/canvas-mcp` is **1,276 lines** and carries a hard **`MAX_PAGES = 5` × `per_page=100` = 500-item
ceiling per list call**, plus `"private": true` (no npm publication, so integration is a clone).
🔵 **The trend is that the unit of supply is small enough to read in an afternoon and small enough to have
undocumented ceilings.** Both properties follow from the same cause, and only a clone reveals the second.

### 🟢 Trend 5 — the topic label is now a measured distortion, not a suspected one

🔵 `topic:ai-tutor` ≥50★ returns 25 rows and 76% permissive. The union across `ai-tutor`, `edtech`,
`e-learning` and `education` returns **305 live rows and 50% permissive**, and `topic:education` ≥100★ alone
reports **634**. 🟢 The largest rows the narrow label does not return include
[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) at **36,250★ MIT** (it declares
`edtech`, not `ai-tutor`), plus four AGPL-3.0 applications between 2.4k and 4.5k★ — all of which this base
already carries, so the distortion is about *which instrument sees what*, not about coverage (`agents/top.md`).
🔵 **Direction of the distortion, stated so it is usable:** topic-filtered lists over-represent *small
permissive skills*; star-ranked lists over-represent *large unshippable applications*. A studio needs both
instruments and should expect them to disagree.

### 🔴 Trend 6 — efficacy: unmoved, and still unreadable from here

🔴 `Gap 479-AI` stands without improvement. No study was read first-hand this pass either; `arxiv.org`,
`edworkingpapers.com` and `clinicaltrials.gov` are refused at the gateway, and the **−0.37 SD** figure this base
has carried remains **load-bearing and unverified**. 🔵 This pass adds no new efficacy claim rather than
restating an old one at second hand — the honest move, and a non-finding.

### 🔵 Trend 7 — institutional readiness is the consensus gap, and the sources contradict each other

🔵 Every demand-side source this pass read agrees adoption outruns governance: **86%** of students across 16
countries using AI in study; usage reported rising **66% (2024) → 92% (2025)**; **10%** of institutions with
formal AI guidelines; **71%** of US teachers without AI training. 🔴 Against which another compilation puts
**~70%** of European and North American institutions as having or developing AI guidance. **Those cannot both
be true of the same population** and neither survey could be opened. 🟢 The trend survives the contradiction —
governance lags use — and no percentage from it should be quoted without its source.

### 🔵 Trend 8 — regulation is diverging by region, and one prohibition already binds

🔵 EU: Annex III education duties at **2 Dec 2027** (Regulation (EU) 2026/1744), **emotion recognition in
schools already prohibited since 2 Feb 2025**. US: no federal instrument; **Colorado and Texas** piecemeal.
China: Interim AI Measures since **15 Aug 2023** (registration, security review, content labelling) plus an
**"AI Plus"** 90%-penetration-by-2030 target. Japan: light-touch voluntary. Vietnam: standalone AI law from
**1 Mar 2026**. LATAM: **no unified framework**.
🟢 **The design consequence is singular and present-tense**: an engagement-detection or emotion-sensing feature
is *already illegal* in EU education, years before the high-risk regime starts. Everything else is a 2027
planning problem; that is a today problem.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 480-AI`** | **`Gap 479-AI` unchanged — no study read first-hand.** Every efficacy figure this base carries, the −0.37 SD included, is a search-tool summary of a paper it cannot open. This pass did not improve the position and declined to restate it as if it had. |
| 🔴 **`Gap 480-AJ`** | **Trend 1's shares are `license.spdx_id` values, not licence readings.** 38 rows are `NOASSERTION`, which means a grant exists and the channel could not classify it; those were **not** fetched and read. The 19% "no grant" figure is the channel's verdict, confirmed by file probe on only **three** rows. |
| 🔴 **`Gap 480-AK`** | **Trend 2 is a two-row sample** (`Gap 480-E`). The shared rendering is strongly evidenced and its **prevalence is entirely unmeasured** — the other 18 Apache rows in the union were not diffed, and no provenance for the rendering was found. |
| 🟡 **`Gap 480-AL`** | **Trend 3 is 64 minutes long and one repository wide.** Three of `p479`'s eight panel rows were not re-read, and the concentration ratio rests on three comparison rows that moved +5 between them. |
| 🟡 **`Gap 480-AM`** | **Trend 4 generalises from one clone.** The 500-item ceiling is a property of `boyuchengz/canvas-mcp`, verified in its source; that small MCP servers *characteristically* carry such ceilings is an inference from one example (`Gap 480-B`). |
| 🟡 **`Gap 480-AN`** | **Trend 5's "AI-relevant" split rests on this base's own keyword classifier** (`Gap 480-C`), and `topic:education` was read to page 1 of 634. The distortion's **direction** is measured; its **magnitude** is a floor. |

---

## 🆕 `p479` — `2026-10-27` — **🟢 THE STRUCTURAL TREND THIS PASS CAN ACTUALLY MEASURE IS A CHANGE IN THE UNIT OF SUPPLY: **12 of the 25** repositories in a complete ≥50★ agent census are **agent skills or MCP servers, not applications** — and the week's standout new arrival is an MCP server onto Canvas LMS (115★ in two days). 🔴 Attention is concentrated **31.5 : 1** in a single repository, measured over two hours with exact endpoints. 🔴 And the efficacy literature has not moved in this base's favour: the only new 2026 study found is a **rule-based** tutor, not an agentic one.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
🔴 **Every study below is read from search-tool summaries.** `arxiv.org` was re-probed this pass and is still
**refused at the gateway** (`CONNECT tunnel failed, response 403`) — see
[`evidence/reachability.2026-10-27-p479.tsv`](../evidence/reachability.2026-10-27-p479.tsv). No abstract below was
read on its own page. Counts and censuses, by contrast, are first-hand
([`evidence/census.2026-10-27-p479.tsv`](../evidence/census.2026-10-27-p479.tsv)).

---

### 🟢 Trend 1 — the unit of supply is now a skill or an MCP server, not an application *(measured here)*

🔵 Of the 25 rows in the ≥50★ `topic:ai-tutor` census, **12** declare themselves as agent skills or MCP servers in
their own topic lists (`agent-skills`, `claude-skills`, `codex-skill`, `mcp-server`, `dsh-plugin`) rather than as
deployable products: `examprep-skill`, `Bloom`, `universal-diagnostic-tutor-skill`, `kaogong-skill`,
`education-skills`, `human-skill-tree`, `algo-sensei`, `Study-Mate`, `Smart-Study-Agent`, `anki-mcp-server`,
`tutor-mcp` and — new this window — [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp).

🟢 **Why it matters commercially.** A skill is a *prompt-and-protocol artefact*: cheap to adopt, cheap to
localise, and it inherits the host agent's model, memory and tool access instead of shipping its own. 🔴 It also
means the thing being starred is often **not software a studio can deploy** — it is instructions for someone
else's agent, and its licence governs *prose*, which is where `education-agent-skills`' CC BY-SA 4.0 bites
hardest. 🟡 The practical consequence: when a client asks for "the open-source tutor", half the supply is a skill
that presupposes an agent runtime the client has not bought.

### 🔴 Trend 2 — attention is concentrated, and the ratio is measured *(measured here)*

🔵 Between `p477`'s 09:49:47Z read and this pass's 11:50:25Z read, both exact counts from the same channel:
[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) took **+189★ (94.0 ★/h, Poisson 95% 80.6–107.4)** while the
other seven measured rows took **+6★ between them** — **31.5 : 1**. 🟢 DeepTutor's rate is **15.2×** its own
lifetime average of 148.0 ★/day, and `p477` measured 14.6× on an independent interval, so the acceleration is
two-pass consistent. 🔴 In `topic:ai-education`, 31 repositories created in the last 14 days contain **one** above
400★ and **nothing else above 3★**. 🔵 The shape of this market is one winner and a very long tail of solo
artefacts — which is an argument against "pick the top of the list" as a sourcing strategy, because the top of the
list is one repository and the rest is noise at this resolution.

### 🔴 Trend 3 — code is permissive, content is not, and this is now a property of a complete population *(measured here)*

🔵 All 22 repositories in the 30-day ≥30★ `topic:education` census carry a payload-read grant. 🟢 **16 are MIT.**
🔴 **Both non-commercial rows are the content rows** — [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)
(4,165★, CC BY-NC 4.0, and its README places the **diagnostic tool code** inside that grant) and
[egplnt/-student-study-framework](https://github.com/egplnt/-student-study-framework) (95★, CC BY-NC-SA 4.0).
🔴 **Two rows have no grant at all** (453★ and 188★). 🔵 `p477` observed this on two data repositories; it is now
measured across a complete star-floored population, and the direction is the same: **the curriculum layer is the
layer a studio cannot ship**, and it is also the layer clients most want aligned.

### 🔴 Trend 4 — the unlicensed upper tail is a real procurement hazard *(measured here)*

🔵 This pass probed licence paths on every row it published and found **five unlicensed education repositories
totalling over 30,000★**, led by [JushBJJ/Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)
at **29,550★** — the most-starred AI-tutor repository on GitHub, with no grant file at 20 probed paths and no
licence line in its README. 🔴 Add [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) (2,049★), whose bespoke
"Community License" prohibits redistribution outright and requires an **executed revenue-sharing agreement**
before any commercial use. 🟡 Both appear in third-party "best open-source education AI" roundups. 🟢 The
operational lesson is cheap to apply: **a star count is not a licence**, and a four-second payload probe separates
the two.

### 🟢 Trend 5 — integration with the incumbent LMS is displacing the standalone tutor *(measured here, thin)*

🔵 Three rows from this window point the same way: [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp)
(MIT, **115★ in two days**, read-only MCP onto Canvas), [Selleo/mentingo](https://github.com/Selleo/mentingo)
(MIT, an **AI-native LMS** positioning itself against Moodle, Docebo and Open edX) and
[pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) (Apache-2.0, multi-tenant LMS, three weeks
old). 🟢 Each is a bet that the buyer already *has* an LMS and will not replace it — the opposite of the
standalone-tutor bet that most of the agent tier makes. 🔴 Three rows is a direction, not a trend: two were
created this month and none has been run here.

### 🔴 Trend 6 — the efficacy evidence still does not cover agentic tutors *(secondary)*

🔵 `p478`'s reading stands: the largest 2026 university RCT found AI-tutor access **reduced** final grades by
0.37 SD, while smaller trials of structured, course-grounded tutors show gains — the **design**, not the model, is
what separates them. 🟡 The one new 2026 study this pass found is **TEAMIGO** (Frontiers in Education, June 2026):
a virtual tutor reporting a **35.5%** reduction in disruptive behaviours among students with ASD and **23.6%**
among students with ADHD. 🔴 **It is rule-based, not an open generative LLM**, and its own authors call the results
preliminary and ask for randomised trials. 🔴 So the gap `p478` declared is unchanged and now has a second
instance: **the studies that work are the ones that constrain the model**, and still **no 2026 trial compares an
agentic tutor against a non-agentic one**. 🟡 UNESCO's Digital Learning Week concept note puts "agentic" AI on
education's near-term agenda, and the OECD's Digital Education Outlook 2026 recommends moving from
general-purpose tools to **purpose-built** educational AI — both are policy framing, not evidence.

### 🔴 Trend 7 — automated grading is still a measured absence *(measured here)*

🔵 `grading rubric teacher in:name,description stars:>15` returns **`total_count` 0**, `incomplete_results` false.
🟢 The nil is robust rather than fragile, because GitHub **stems** `grading` to `grade` — the query matches
`production-grade` and still returns nothing in scope. 🔵 A query whose recall is artificially widened and still
returns zero is stronger evidence of absence than a narrow one. 🔴 `p478`'s reading is therefore corroborated by a
census rather than by an impression: **a studio asked for automated grading today is building, not composing** —
and the one MIT project in the category, [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent),
still has 0★ and a README that freezes grading productisation.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 479-AI`** | **`Gap 478-AB` unchanged: no study was read first-hand.** Every n, effect size and percentage in Trend 6 is a search-tool summary; `arxiv.org`, `edworkingpapers.com` and `clinicaltrials.gov` are refused at the gateway. The −0.37 SD figure remains load-bearing and **unverified**. |
| 🔴 **`Gap 479-AJ`** | **Trend 1's count is self-declared topics, not an architectural audit.** A project may declare `agent-skills` and still ship a deployable app, or ship a skill without declaring it. Twelve of 25 is a count of labels. |
| 🔴 **`Gap 479-AK`** | **Trend 2 is two hours long.** A 31.5 : 1 concentration over one interval says nothing about a week, and the seven comparison rows moved too little for any of them to have a measurable rate of its own. |
| 🟡 **`Gap 479-AL`** | **Trend 5 rests on three rows, two of them created this month**, and on positioning read from descriptions. No plugin API, LTI boundary or MCP transcript was exercised. |
| 🟡 **`Gap 479-AM`** | **The TEAMIGO figures are percentage reductions in behaviour counts, not learning outcomes**, from a summary of a paper this base could not open. They are not comparable with the 0.37 SD grade effect in any direction. |
| 🟡 **`Gap 479-AN`** | **Trend 7's nil is one query family at one floor.** A grading project named in Chinese, or described as "assessment" or "feedback" without the word grading, would not appear — and the stemming argument does not cover a different vocabulary. |

---

## 🆕 `p478` — `2026-10-27` — **🔴 THE EFFICACY EVIDENCE TURNED THIS PASS AND IT CUTS AGAINST THIS BASE'S OWN AGENT SHELF: the LARGEST 2026 university RCT found AI-tutor access REDUCED final grades by 0.37 SD and LMS participation by 0.90 SD, with bigger losses for first-generation students — while smaller trials of STRUCTURED, course-grounded tutors show gains. 🟢 The design variable, not the model, is what separates them. 🔴 And no 2026 trial compares an AGENTIC tutor against a non-agentic one at all.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green).
🔴 **Every study below is read from search-tool summaries.** `arxiv.org`, `edworkingpapers.com` and
`clinicaltrials.gov` were all probed directly and **refused at the gateway** — see the boundary table on
`intel/market.md` and [`evidence/reachability.2026-10-27-p478.tsv`](../evidence/reachability.2026-10-27-p478.tsv).
No abstract below was read on its own page.

---

### 🔴 Trend 1 — the efficacy literature has split, and the biggest study is the negative one

| study | design | n | headline result |
|---|---|---|---|
| 🔴 EdWorkingPaper **26-1598**, large US public university | randomised across sections of the same course | **2,379** undergraduates, 30 instructors | 🔴 **final grades −0.37 SD**; LMS participation **−0.90 SD**; losses **larger for first-generation students** |
| 🟢 arXiv **2609.23958**, graduate corporate finance | randomised field experiment; structured course-grounded tutor vs holdout free to use consumer AI | **86** | 🟢 total score **+6.63** (CI **+1.95 to +11.31**) |
| 🟢 arXiv **2604.02677** | tutor alone vs tutor + peer agents | **315** | 🟢 tutor **+ peers** highest unassisted test accuracy |
| 🟡 earlier undergraduate physics RCT | structured AI tutor vs in-class active learning | not stated | 🟢 more learning in **less time** |
| 🟡 arXiv **2609.14789**, UK GCSE Science | practitioner-led **micro-randomised** trials of a tutoring platform | not stated | design-focused; no headline effect read |
| 🟡 `NCT07449182` · `NCT07692035` | registered medical-education agent trials | — | 🔴 **no results yet** |

🟢 **The reconcilable reading, and it is actionable.** The negative trial gave students *access to a tutor*; the
positive ones gave them a **tutor bounded to the course's own material and sequence**. The negative paper's own
conclusion is displacement — the tutor substituted for coursework rather than adding to it — which is a
**product-design failure, not a model failure**. 🔵 For a studio the consequence is concrete: an engagement
scoped as "give learners a tutor" has a large, recent, well-powered trial predicting it will *lower* grades.
One scoped as "ground the tutor in this course's materials, sequence and assessment, and instrument what it
displaces" has the positive results behind it.

🔴 **Stated against itself.** The negative study is an unreviewed working paper whose author list differs across
versions of the record, and this base **could not open it**. The positive results are n=86 and n=315. One large
unreviewed negative against several small positives is not a settled literature, and the equity signal —
first-generation students losing most — is the single finding here that most deserves a primary read and cannot
get one in this environment.

### 🔴 Trend 2 — the agentic premise of this base's own agent shelf is unevaluated

🔵 A targeted search for a 2026 RCT comparing an **agentic** tutor (one that plans multi-step actions) against a
non-agentic one returned **nothing**. 🔴 Seventeen agents are published on `agents/top.md`; **none has been run
or evaluated here** (`Gap 478-B`), and the external literature has not evaluated the category either. 🟢 This is
the honest statement of where the field is: *agentic* is a description of architecture with no outcome evidence
attached to it, and the two 40k★ repositories on this shelf are popular, not proven.

### 🟡 Trend 3 — permissiveness falls as you move up the stack

🔵 Assembled across `p477` and this pass, each tier's grants payload-read:

| tier | grants | reading |
|---|---|---|
| infrastructure (LRS, xAPI, knowledge tracing, curriculum data) | 🟢 **10 of 10 permissive** (MIT / Apache-2.0) | build freely |
| agents | 🟢 **14 of 17 permissive**; 🔴 GPL-3.0 ×2, CC BY-SA 4.0 ×1 | check before lifting prompts |
| platforms | 🔴 **11 of 15 copyleft** — and the three a client most likely runs (Moodle, Open edX, Canvas) are GPL-3.0 / AGPL-3.0 / AGPL-3.0 | integrate over a boundary, never fork |
| curriculum **data** | 🔴 `p477` found the two largest new education data repositories at **CC BY-NC 4.0** and **ODbL** | the code is permissive and the content is not |

🟢 **So the licence risk is not where a studio usually looks for it.** The agents are mostly MIT; the LMS the
client already runs is AGPL; and the curriculum content — the part with no substitute — is the most restricted
layer of all. 🟡 One counter-example sits inside the pattern and is this pass's own:
[bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados), 1,721 BNCC objectives, read first-hand as **MIT**.
Permissive curriculum data exists; it is just not the norm.

🔴 Four tiers assembled by this base from addresses it already held, not sampled from any population —
`Gap 477-R`'s objection applies in full and the direction is all that should be carried.

### 🔴 Trend 4 — automated grading is still absent at any level of adoption

🔵 Re-measured this pass. The only open-source project with grading in scope is
[littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) — MIT, payload-read,
human review gating each step, sandboxed evaluation of learner code — and it has **0 stars**, with its own README
saying automatic grading productisation is frozen. 🔴 Everything else found under a grading query turned out to
be lesson planning. 🟢 Meanwhile grading is **Annex III high-risk** under the EU AI Act and named in several US
state statutes. **The most regulated use case is the one with no open-source supply**, which is a build
opportunity and a liability in the same sentence.

### 🟡 Trend 5 — supply moves to the teacher while attention stays with the learner

🔵 Five of the six repositories surfaced on `agents/trending.md` this window are teacher-facing and **none exceeds
63★**; both 40k+ agents are learner-facing. HolonIQ's LATAM cohort reading points the same way — AI-native
positioning clustering on teacher-facing lesson preparation rather than consumer tutoring. 🔴 Six repositories
found by keyword search with no measurable recall cannot establish a population shape (`Gap 478-I`); two
independent instruments pointing the same direction is the whole of the claim.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 478-AB`** | **No study above was read first-hand.** `arxiv.org`, `edworkingpapers.com` and `clinicaltrials.gov` are refused at the gateway, so every n, effect size and confidence interval here is a search-tool summary of a page this base never opened. The −0.37 SD figure is load-bearing for Trend 1 and **unverified**. |
| 🔴 **`Gap 478-AC`** | **The structured-vs-open-access reconciliation is this pass's own reasoning** across six studies with different populations, levels and countries. No study compared those two designs directly, so the mechanism is inferred from how the arms happen to differ. |
| 🔴 **`Gap 478-AD`** | **The equity signal is single-source.** "Larger losses for first-generation students" comes from one unreviewed working paper and is not corroborated anywhere else on this shelf — and it is the finding with the highest cost of being wrong in either direction. |
| 🟡 **`Gap 478-AE`** | **Trend 3's four tiers were assembled by this base, not sampled.** The ratios compare sets this base chose; `Gap 477-R` applies unchanged. |
| 🟡 **`Gap 478-AF`** | **Trend 4 is a search result, not a census.** `p477`'s topic-qualifier lesson applies: a keyword query for grading cannot see a grading project that does not use the word, and no `topic:` census was available this pass (`Gap 478-F`). |

---

## 🆕 `p477` — `2026-10-27` — **🔴 THE TREND THIS PASS WOULD STAKE A CLIENT ENGAGEMENT ON: in education AI the CODE is permissive and the CURRICULUM is not. Every one of the 11 MIT/Apache/BSD rows read first-hand this pass is a tool; the two largest knowledge-graph repositories are CC BY-NC and ODbL. 🟢 And three of this base's own published trends were instrument artefacts — a measured zero, an accent effect and a stale-address rate — all three corrected here.**

🔵 `Gap 476-Q` stands against most of what follows: these remain single-pass cross-sections. What changed is that
T1 is a licence census with every payload read first-hand, and T2 is the first **measured velocity** in this
base's history ([`evidence/star-velocity.2026-10-27-p477.tsv`](../evidence/star-velocity.2026-10-27-p477.tsv)).

### 🔴 T1 — Permissive tools, restricted curriculum: the split that decides what a studio can sell

🔵 26 grant payloads read first-hand this pass, each fetched to a file and the file measured.

| tier | permissive (MIT / Apache-2.0 / BSD-3) | restricted |
|---|---|---|
| **agents and tools** | 🟢 `OpenMAIC`, `Study-Mate`, `learn-from-materials`, `Papermorph`, `claudemy`, `breakscale`, `book-to-skill`, `dolos`, `scorm-again`, `pyBKT`, `pykt-toolkit`, `fsrs4anki`, `Artemis`, `ltijs`, `lrsql`, `jupyterhub`, `nbgrader` | 🔴 `frametell` (**AGPL-3.0**), `overhangio/tutor` (**AGPL-3.0**) |
| **curriculum and knowledge data** | 🟡 `bncc-dev/bncc-dados` (Brazil's BNCC, open data) | 🔴 **`cn-math-taxonomy` (CC BY-NC 4.0, 4,148★)**, **`withmarbleapp/os-taxonomy` (ODbL, 7,398★)** |
| **platforms** | 🟢 `Kolibri` (MIT), `Oppia` (Apache-2.0), `OpenOLAT` (Apache-2.0), `Sakai` (ECL-2.0) | 🔴 `Moodle`, `Open edX`, `Canvas`, `Frappe LMS`, `Chamilo`, `ILIAS`, `Gibbon`, `i-educar`, `RosarioSIS`, `OpenEduCat`, `BigBlueButton`, `H5P` |

🔴 **This is the inverse of the usual open-source risk shape.** The reflex is to worry about the licence on the
code you ship and treat data as inert. In education the code is clean and **the data is where the restriction
lives** — and it is invisible to a metadata licence field: both restricted grants returned **UNNAMED** from an
SPDX-style name reader and needed a hand read. 🔵 **Operational consequence:** a licence-clearance pass over
curriculum assets belongs *before* an engagement is scoped, not at delivery.

### 🟢 T2 — DeepTutor has not plateaued: measured at ~14× its own lifetime average

🔵 Two first-hand reads 321 s apart, both times recorded here: 44,630 → **44,638**, i.e. ~90 ★/h against a
lifetime average of 147 ★/day. An independent bound against `p476`'s figure and commit time gives ≤152 ★/h.
🔴 **Stated against itself:** 8 events gives a Poisson 95 % interval of 47–177 ★/h. The *sign* is the trend — at
44.6k★ and ten months old this repo is still accelerating — and the magnitude is one decimal place
(`Gap 477-A`).

### 🔴 T3 — Attention moved to rendering subjects, not conversing with learners

🔵 Of the 10 largest education repositories created since 1 Aug 2026, **5 are interactive explainers** —
`breakscale` (load a system till it breaks), `Papermorph` (books → animated web), `insect-world` (63 procedurally
generated species), `prehistoric-animal-museum`, `esp-labs-web` — not tutors, not LMS components, not agents.
🔵 Only 3 of the 10 are conversational tutors. 🟡 A one-window shape, not yet a trend (`Gap 477-H`).

### 🟢 T4 — One jurisdiction now regulates education AI by name, and the EU's deadline moved

🔵 **South Korea's AI Basic Act, in force 22 January 2026**, names education among its "high-impact" domains — the
only statute found in any region that does so explicitly. 🔴 Meanwhile the **Digital Omnibus (Regulation (EU)
2026/1744, in force 27 July 2026)** pushed stand-alone Annex III education systems from 2026 to **2 December
2027**. 🔵 **The direction: the binding edge of education-AI regulation has moved from EMEA to APAC for the next
13 months**, while the EU's two non-deferred duties — the emotion-recognition prohibition (2 Feb 2025) and
Article 50 chatbot disclosure (2 Aug 2026) — are the only ones that bite today.

### 🔴 T5 — Three of this base's own trends were instrument artefacts

🔵 Not a trend about education. A trend about **this base**, and the most consequential thing in the pass.

| published as a measurement | actually | mechanism |
|---|---|---|
| *"zero education-AI repos created since 1 Aug 2026 reached 100★ (n=0, measured)"* — `p476` | 🔴 **24**, largest 4,148★ | conjunctive free-text query; `topic:` qualifier sees them |
| *"accented tokens understate LATAM supply by 1.34×–3.50×"* — `Gap 476-N` | 🔴 **1.018× / 1.004×** | GitHub folds diacritics; the discrepancy was **truncation** |
| *"1-in-22 stale addresses, detector: resolves on git + absent from index"* — `p476` | 🟡 detector has a **33 % false-positive rate** here | repo search **excludes forks** unless `fork:true` |

🔴 **The common mechanism in all three: a query that returns fewer rows than reality, read as a fact about the
world.** Truncation returns a short list with `incomplete_results=TRUE` and no error; a conjunctive query returns
zero; the fork exclusion returns an absence. 🟢 **Three controls adopted:** batch `repo:` at 10 and never above;
cross-check any nil with a `topic:` qualifier; re-query every absent address with `fork:true` before calling it
stale. 🔵 **The general form, for every later pass: an absence is a claim about an instrument until it is proved
to be a claim about the world.**

### 🔴 T6 — Regulated features sit in the coldest code

🔵 `elimu-ai/ml-authentication` ships face recognition to authenticate pupils — the one feature both the EU AI
Act and Vietnam's Decision 33 put in their highest tier — and its **last commit is 2025-02-25, 20 months cold**,
with 40 open issues. The org around it is active; `p476` read that activity from a sibling repo pushed the day
before. 🔴 **Org-level liveness does not transfer to a component**, and here the component carrying the regulated
surface is the abandoned one. 🔵 A due-diligence rule follows: date the **component**, never the organisation.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 477-AC`** | **T1, T3, T4 and T6 are single-pass cross-sections.** Only T2 is a ratio between quantities measured in the same pass, and its interval is 5.35 minutes. `Gap 475-S`/`Gap 476-Q` are narrowed, not closed, and stay open until a second snapshot exists to difference. |
| 🔴 **`Gap 477-AD`** | **T1's census covers the 26 payloads this pass read, not the tier.** Rows whose grants are carried from earlier passes are counted in the table but were not re-read, and no curriculum repository beyond the three named was examined — so "the data is where the restriction lives" rests on **2 restricted finds**, not on a survey of education datasets. |
| 🔴 **`Gap 477-AE`** | **T4 compares a statute's scope against a deferral, both read from secondary commentary** (`Gap 477-Y`). Whether Korea's "high-impact" designation actually imposes more on an education deployment than Annex III does is **not analysed** — only that Korea names education and the EU's clock moved. |
| 🟡 **`Gap 477-AF`** | **T5 is a self-audit of three findings, not of the base.** Hundreds of other published measurements in retained history have not been re-run against the three controls now adopted, so how far the artefact pattern extends is unmeasured. |
| 🟡 **`Gap 477-AG`** | **T6 generalises from one repository.** "Regulated features sit in the coldest code" is one observation; no other component carrying a high-risk feature was dated this pass. |

---


## 🆕 `p476` — `2026-10-27` — **🟢 TWO TRENDS ON THIS SHELF ARE NOW QUANTIFIED RATHER THAN ASSERTED, which is what `Gap 475-S` asked for: open-source attention in education AI is concentrated at 95.7 % in a SINGLE repository, and one education-AI agent outstars the entire open-source education PLATFORM tier by 1.14×. 🔴 And the copyleft trend `p475` called is hardening, not softening — `penecho` elects `AGPL-3.0-only`, closing even the future-version escape.**

🔵 `Gap 475-S` stands against most of what follows: these remain single-pass cross-sections. What changed is
that two of them are now **ratios between measured quantities** rather than impressions, and a star snapshot
exists for the next pass to difference —
[`evidence/star-snapshot.2026-10-27-p476.tsv`](../evidence/star-snapshot.2026-10-27-p476.tsv).

### 🟢 T1 — The version election is readable on only half the copyleft tier, and `or-later` is not the default

🔵 `p475` proved the licence payload cannot reveal a GPL-family version election. This pass read the two
channels where it actually lives, across 8 repos
([`evidence/version-election.2026-10-27-p476.tsv`](../evidence/version-election.2026-10-27-p476.tsv)):

| verdict | count | repos |
|---|---|---|
| 🟢 `or-later` genuinely elected | **3** | `moodle/moodle`, `frappe/lms`, `openeducat/openeducat_erp` |
| 🔴 `only` elected — the opposite of the payload reading | **1** | `penecho/penecho` |
| 🟡 bare deprecated id, no election recorded | **2** | `instructure/canvas-lms`, `h5p/h5p-php-library` |
| 🔴 unreadable on every reachable channel | **2** | `openedx/openedx-platform`, `echo-loop/Echo-Loop` |

🔴 **The trend: the ecosystem does not record its own version elections consistently.** Half of this tier
cannot tell a downstream user whether a future GPL applies, and the single most deployed open-source
higher-education platform — Open edX — records it **nowhere** reachable: not in the payload, not in a 48 KB
`pyproject.toml`, not in five source files. 🔵 This is a licensing-hygiene gap in the *projects*, not in this
base's reading, and it is the kind of thing that only surfaces when someone looks in the right place.

### 🟢 T2 — Attention is concentrated in one repository, measurably

| measure | value |
|---|---|
| agent-shelf rows re-measured | 13 |
| rows that moved at all | **4** |
| rows that did not move by a single star | **9** |
| `HKUDS/DeepTutor` share of all movement | **95.7 %** (+90 of +94) |

🔴 **"Education AI is growing" is not supported; "one project is growing" is.** 🔵 The interval is a single
calendar day, so this is a snapshot of concentration, not a growth rate (`Gap 476-D`). But concentration is
itself the decision-relevant quantity: a studio betting on the tier is really betting on one repository
ten months old.

### 🟢 T3 — The platform tier and the agent tier are inverted, and stars are the wrong instrument for one of them

| tier | total ★ |
|---|---|
| ten open-source education platforms (Moodle, Open edX, Canvas, BBB, Frappe, Sakai, Kolibri, OpenEduCat, OpenOLAT, H5P) | **39,158** |
| `HKUDS/DeepTutor`, alone | **44,531** |

🔴 **Moodle has 7,550★ and a large share of the world's institutional LMS installs. DeepTutor has 44,531★ and
is ten months old.** 🟢 The reading is not that agents matter more — it is that **stars measure developer
attention and say nothing about installed base**, and the two tiers sit at opposite ends of that mismatch.
🔵 For a studio: the systems a client already runs are systematically *under*-represented in open-source
attention metrics, so a shelf ranked by stars will always under-weight the thing the engagement actually has
to integrate with.

### 🟢 T4 — In Africa, policy arrived before supply — the inverse of every other region

| axis | measured |
|---|---|
| jurisdictions with education named in national AI or EdTech strategy | **7** (African Union, Kenya, Nigeria, Côte d'Ivoire, Zambia, Ghana, francophone bloc via UNESCO/KIX) |
| in-language open-source education supply (`elimu`, Swahili, `stars:>=5`) | **4 repositories** |
| of which real education software | the `elimu-ai` org — **66 repos, every grant MIT** |

🔴 **Everywhere else this base has measured, supply ran ahead of rules.** Africa is the opposite: continental
and national strategy naming education as a top-three priority sector, against four repositories. 🟢 The
stated requirement is sovereignty-shaped — AI adapted to African **languages and cultures**, with data
control — and the one platform found already matches it architecturally: **offline-first, EGRA/EGMA-aligned,
MIT**. 🔵 This is the clearest supply-demand asymmetry on any shelf in this base.

### 🟢 T5 — Regulatory convergence is on FEATURES, and the lever is procedural, not technical

🔵 `p475`'s four-point convergence line holds and is corroborated. 🟢 What this pass adds is the **exit**:

| jurisdiction | the two features named | 🟢 the scoping qualifier |
|---|---|---|
| EU (Annex III pt 3, Reg. (EU) 2026/1744) | automated grading/ranking; biometric and emotion monitoring | binds **2 Dec 2027** stand-alone |
| Vietnam (Decision 33/2026/QĐ-TTg) | automated grading; behavioural monitoring | 🟢 **high-risk only where AI output is the SOLE basis for a decision without meaningful human review** |
| South Korea (AI Basic Act, in force 22 Jan 2026) | comprehensive statute | — |
| North America (state level) | student-data use, classroom use | 134 bills / 31 states; no federal statute |

🟢 **The trend worth acting on: the binding question is increasingly "is a human deciding?", not "is there a
model?"** Vietnam states it explicitly, and the EU's high-risk obligations centre on human oversight. A
teacher-confirms-the-suggestion default is therefore a **compliance architecture**, not a UX preference —
and it is portable across all four jurisdictions at once. 🔴 Read from secondary legal summaries, not from
Decision 33's annex (`Gap 476-H`).

### 🔴 T6 — The copyleft turn in new education AI is hardening, not softening

🔵 `p475` found the three highest-starred new education-AI repos all AGPL-3.0. 🟢 Re-measured, the shape
holds — and the version elections make it stricter than `p475` could see:

| repo | ★ | grant | election | what it means downstream |
|---|---|---|---|---|
| [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | 4,524 | AGPL-3.0 | 🔴 unreadable | network copyleft, future-version status unknown |
| [penecho/penecho](https://github.com/penecho/penecho) | 2,504 | **AGPL-3.0-only** | 🔴 **`only`** | network copyleft **with no future-version escape** |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 2,424 | AGPL-3.0 | not probed | network copyleft |
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 2,049 | **bespoke community licence** | n/a | 🔴 non-commercial — not open source at all |

🟢 **Against this, the permissive tier grew by reading, not by events:** `OpenCat` and `mini-nanoGPT` both
read **MIT** this pass, taking the agents shelf to 7 build-on-able of 13. 🔵 The distinction matters — nothing
in the ecosystem became more permissive this window; this base simply had two fewer blind spots.

### 🔴 T7 — Published addresses decay silently, and the decay is measurable

🟢 **22 live addresses swept, 1 stale** (`openedx/edx-platform` → `openedx/openedx-platform`). 🔴 The reason
no earlier pass caught it: git and raw **forward renames transparently and answer 200**, so every integrity
control this base runs — HEAD resolution, payload bytes, payload digest — reported the row healthy, and it
was healthy. Only absence from the search index fires. 🔵 A 1-in-22 rate on addresses republished every pass
implies retained history carries more (`Gap 476-E`), and address rot is now a named maintenance category
rather than an accident.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 476-Q`** | **T1, T4, T5, T6 and T7 remain single-pass cross-sections.** Only T2 and T3 are ratios between quantities measured in the same pass, and T2's interval is one day. `Gap 475-S` is narrowed, not closed, and will stay open until a second snapshot exists to difference. |
| 🔴 **`Gap 476-R`** | **T4's asymmetry compares a 7-item policy count against a 4-item supply count measured by completely different instruments** — one a French-language policy read, the other a Swahili token census at `stars:>=5`. The direction is strong; the magnitudes are not commensurable and should not be ratioed. |
| 🟡 **`Gap 476-S`** | **T3's inversion uses stars as a proxy for attention and a qualitative claim for installed base.** No deployment figure was measured for any platform in any pass — not a Moodle install count, not an Open edX site count. The inversion's left-hand side is measured; its right-hand side is asserted. |

## 🆕 `p475` — `2026-10-27` — **🟢 `p471` SAID THREE JURISDICTIONS ON THREE CONTINENTS HAD CONVERGED ON THE SAME REGULATORY SHAPE. A FOURTH HAS NOW ARRIVED INDEPENDENTLY AND NAMES THE SAME TWO FEATURES — automated grading and biometric monitoring — with a deadline NINE MONTHS AHEAD of the EU's. 🔴 Meanwhile the open-source supply moved the other way: the three highest-starred new education-AI repos of this window are all AGPL-3.0.**

### 🟢 T1 — Regulatory convergence is now a four-point line, and it converges on *features*, not on *AI*

🔵 Legislatures that share no legal tradition keep landing on the same two education features:

| jurisdiction | instrument | automated grading / ranking | biometric or emotion monitoring | deadline that binds |
|---|---|---|---|---|
| EU | AI Act Annex III pt 3, as amended by Reg. (EU) 2026/1744 | 🔴 High-risk | 🔴 Emotion recognition **prohibited** since 2 Feb 2025 | **2 Dec 2027** (Annex III) |
| Vietnam | Decision 33/2026/QĐ-TTg | 🔴 High-risk | 🔴 High-risk (facial recognition, eye tracking) | **1 Sep 2027** (existing systems) |
| South Korea | AI Framework Act | 🟡 Economy-wide, not education-specific | 🟡 Economy-wide | In force **22 Jan 2026** |
| US states | Idaho S.B. 1227, Oklahoma, Ohio H.B. 96, Maryland S.B. 720, North Carolina | 🔴 Restricted — AI may not **replace a licensed educator** in grading | 🟡 Largely unaddressed | Rolling, **1 Jul 2026 → 30 Jun 2028** |

🔵 **The trend is the convergence on the feature list, not the count of laws.** Two of these name
*the same pair* with deadlines nine months apart. 🔴 But note what the fourth column shows: the US
regulates **autonomy** (a human must grade), the EU and Vietnam regulate **sensing and
classification**. A product compliant in Ohio can still be unshippable in Frankfurt.

### 🔴 T2 — The new high-star education-AI tier is copyleft, and that is a reversal

🔵 Measured, not impressed upon: the three highest-starred education-AI repositories to surface in this
window are [Echo Loop](https://github.com/echo-loop/Echo-Loop) (4,522★),
[penecho](https://github.com/penecho/penecho) (2,503★) and
[LearnHouse](https://github.com/learnhouse/learnhouse) (2,424★) — **all AGPL-3.0**, all read
first-hand. The fourth, [PageLM](https://github.com/CaviraOSS/PageLM) (2,049★), is a **bespoke
non-commercial** grant. The most permissive thing in the top five is
[antivibe](https://github.com/mohi-devhub/antivibe) (MIT, 1,129★) — which is a *coding-agent skill*,
not an education platform.

🔴 **For a studio this inverts the usual advice.** "Start from the most popular open-source project"
now selects, four times out of five, something a client cannot ship in a proprietary product.
🟢 The permissive education foundation tier is the *old* tier — OpenOLAT (Apache-2.0, 448★),
Kolibri (MIT, 1,162★), Sakai (ECL-2.0) — two orders of magnitude less popular and far more boring.

### 🔴 T3 — Adoption has decoupled from governance, and LATAM is where the gap is widest

🔵 **87 % of LATAM higher-education institutions use AI; 26 % have a formal AI strategy** (UNESCO
IESALC, 200 institutions, 19 countries). Teacher-level use in the region runs **~16-20 points above
the OECD average** (Brazil 56 %, Chile 55 %, Colombia 53 %, Costa Rica 52 % vs OECD 36 %).
🔴 The spread runs the opposite way from EMEA, where the statute arrived before the adoption.
🟢 **So the same product does not serve both.** EMEA buys conformance against a dated obligation;
LATAM buys the institutional policy that does not yet exist.

### 🟡 T4 — The measurement instruments are failing faster than the subject is moving

🔵 This is a trend about this base, and it has now recurred for six consecutive passes. `p471` found
`api.github.com` was per-repository, not blocked. `p472` found `curl -sI` is a uniform false-negative
generator. `p473` found title readers are English-keyed. `p474` found grants have *scope*. `p475`
finds that **`or-later` cannot be read from the payload at all** (3/3 control), that **digest identity
has a false-negative mode** (a line-wrap), that a **short probe path publishes granted repos as
ungranted** (Moodle, Frappe LMS), and that **7 of 20 repos do not default to `main`**.

🔴 **Every one of these was a silent error producing confident output.** The trend worth naming:
in this domain the dominant error mode is not missing data, it is **data that arrives looking correct**.
🟢 The countermeasure that keeps working is the cheap control — a high-frequency token in the same
script, a known payload re-measured each pass, a diff instead of a digest comparison.

### 🔴 Declared trend gaps, stated so silence is not read as coverage

| gap | statement |
|---|---|
| 🔴 **`Gap 475-S`** | **No trend here is quantified over time.** Every claim is a single-pass cross-section — including "the new tier is copyleft", which compares *this window's* risers against an older permissive tier without a measured time series. `Gap 475-E`'s star snapshot would fix this and was not built. |
| 🟡 **`Gap 475-T`** | **T3 rests on a single study.** The UNESCO IESALC figures (87 %/26 %/74 %) come from one survey of 200 institutions and are reported here through secondary coverage; the TALIS 2024 teacher figures are a different instrument with a different population, and the two are juxtaposed, not reconciled. |
| 🟡 **`Gap 475-U`** | **No African education-AI trend is recorded, in this pass or any prior one.** `Gap 473-E`/`474-C` asked for the MEA leg in-language on both axes; the supply half ran (Arabic, n=4, zero education software), the demand half did not. The honest statement is that this base has **no African trend data at all**, not that there is no trend. |


## 🆕 `p474` — `2026-10-27` — **🟢 `p473` predicted the market would demand demonstrable evidence; this pass found the INSTITUTION BUILDING THE DEMAND — the Council of Europe is working on a European evaluation framework for educational technology. 🔴 And the matching trend on the supply side is the one that will bite: the education-AI corpora now being packaged for evaluation are NOT THE PACKAGERS' TO LICENSE, and the best of them says so in its own LICENSE file.**

🔵 Every trend below is attributed to the body that stated it, with source class named. 🔴 Vendor
roundups are marked and are not primary research. 🟢 Where this pass measured something first-hand
instead of relaying it, the measurement is given with its payload digest.

### 🟢 Trend 1 — `p473`'s evidence convergence now has an institution and a deliverable

🔵 `p473` recorded five independent bodies converging on *demonstrable evidence* as the 2026
requirement. 🟢 **This pass found the sixth, and it is the one that turns a trend into a
procurement document**: the **Council of Europe** has an AI-and-Education expert group and a second
working conference, whose agenda includes *"the idea of a European evaluation framework to assess
educational technologies"* (institutional source).

🔴 **The mismatch is now precisely stateable.** A pan-European framework for assessing edtech is
being drafted, and the open instruments that would let a vendor self-assess against it are:
**0–11★**, research-published rather than product-published, and — measured this pass — **three of
the strongest carry `SPLIT_SCOPE` grants whose corpora the publisher does not own.** 🟢 Whoever
can produce licensable evaluation evidence in Europe over the next two years is selling into a
requirement with no incumbent.

### 🔴 Trend 2 — the corpus-ownership reckoning: exam material has owners, and they did not publish it

🟢 **The clearest single document this pass read is a retraction inside a licence.**
[`richer-richard/arquimedes`](https://github.com/richer-richard/arquimedes) (`main/LICENSE`, 3,103 B
`b8e2e1c65fdc`) states:

> *"An earlier version of this file placed `problems/`, `images/`, and `data/` under CC BY 4.0. That
> sentence was this project's claim. It was not a grant from the contest organizers or the dataset
> authors... Several of them are narrower than CC BY 4.0. CEMC material is CC BY-NC 4.0."*

🔵 **This is what the benchmark wave looks like when it meets copyright.** Competition problems,
national exam items and textbook questions are the natural substrate for education-AI evaluation,
and almost none of it is the aggregator's to relicense. 🔴 **Prediction, falsifiable:** as
education-AI benchmarks proliferate through 2027, **licence retractions and NC carve-outs on item
banks will become common**, and benchmark repositories will increasingly split code from data in
one file — the `# Licenças` shape found twice at [bncc-dev](https://github.com/bncc-dev) and once
at `arquimedes`. 🟢 **The structural escape already exists and is worth watching**: generated,
solver-graded items with no third-party provenance, as in
[scireason-forge](https://github.com/chenhz01/scireason-forge) (Apache-2.0, *"contamination-proof by
construction"*).

### 🟢 Trend 3 — regional governance is bifurcating, not converging

| bloc | the instrument | what it asks a vendor for | source class |
|---|---|---|---|
| **EU** | AI Act (education = high-risk) + updated ethical guidelines (9 June 2026) + a framework in drafting | 🔴 conformity assessment, human oversight, documentary evidence | regulation + institutional |
| **US states** | ≈100–134 bills; **Idaho SB 1227 enacted**; Oklahoma, Maryland, Vermont, New York | 🟡 human oversight, privacy certification, no AI in high-stakes decisions — **per state** | legislative trackers |
| **US federal** | executive orders through early 2026, incl. one directing that burdensome **state** rules be limited | 🔴 an unresolved collision with the above | policy relay |
| **MEA** | strategies in Saudi Arabia, UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco, South Africa; **no binding AI statute** | 🟢 strategy alignment and procurement credentials | governance guide |
| **LATAM** | Brazil Bill 2,338/2023 pending; Chile risk-based bill; **Argentina rejecting regulation** | 🟡 three different answers in one region | law-firm relay |
| **APAC** | 🔴 nothing education-specific found; Singapore's consultations are financial-sector | 🔴 unknown — declared gap | trade press |

🔴 **The practical consequence: "AI in education compliance" is not one capability.** A single
conformity dossier does not travel from Frankfurt to Riyadh to Boise. 🟢 **What does travel is the
evidence layer underneath** — a learner-level record of what the AI did, exportable into whichever
format the jurisdiction demands. That is why pattern `P474-1` builds the telemetry spine first and
the dossier second.

### 🟢 Trend 4 — the measurement trend: discovery instruments are the binding constraint, not supply

🔵 Three passes running, this base's biggest findings have been **instrument failures rather than
market facts** — `p473`'s product-vs-research vocabulary, `Gap 467-H`'s `tutor`/`tutorial`
collision, and this pass's three:

| instrument failure | what it looked like | what it was |
|---|---|---|
| 🔴 Arabic education nil (480 hits, 4 at ≥5★) | "MENA does not build education software" | **Arabic GitHub presence is 8.5× thinner than Turkish across all domains**; education's share is 89 % of Turkish's — see `repos/trending.md` |
| 🔴 `okul` (Turkish for school) returning KDE's document viewer | a thin Turkish tier | Latin-script collision with **`okular`** |
| 🔴 `educacao` ≫ `educacion` at ≥5★ | "Brazil builds, Spanish LATAM adopts" | **inverts at ≥0★** — Spanish returns 20 % *more*; the difference is star accumulation (2.49×) |

🟢 **The generalisation, now on four observations: every tier this base has declared absent has
turned out to be present under a different query.** 🔵 So the standing rule tightens — **a nil is
publishable only with its denominator**, a normaliser in the same instrument, and the word
`incomplete_results` reproduced when the index returns it. 🔴 `p474` registers this as the
discipline that found the Arabic result; without the `برمجة`/`yazılım` control this pass would have
published a false regional claim.

### 🟡 Trend 5 — the teacher-capacity curve is the fastest-moving number anyone reports

🔵 AI professional development for teachers is reported to have risen from **29 % in early 2024 to
50 % by late 2025** (vendor statistics roundup, relayed). 🟢 If roughly sound, teacher capability —
not model capability — is the variable moving fastest, which matches the Idaho and Oklahoma
statutes legislating **educator training** rather than model standards. 🔴 Single relayed source,
not corroborated: carried as a signal, not a basis.

### 🔴 Declared trend gaps, stated so silence is not read as coverage

- 🔴 **No APAC education-specific regulation or school-level adoption rate found**, on two
  successive query sets. Second reproduction of `p473`'s nil.
- 🔴 **No primary (non-vendor) 2026 market size for any region.** Four vendor values for 2026 differ
  by **2.9×**; all four are printed in [`intel/market.md`](market.md) and none averaged.
- 🔴 **Chinese NonCommercial content tier still not swept at breadth** (`Gap 467-F`, third pass
  owing it).
- 🟡 **The EMEA in-language demand leg was run in English sources about MEA, not in Arabic or
  Turkish sources.** The supply leg was in-language; the demand leg was not. That asymmetry is this
  pass's own and is registered.

## 🆕 `p473` — `2026-10-27` — **🟢 THE TREND EVERY SOURCE THIS PASS AGREES ON IS THE ONE THE OPEN-SOURCE SUPPLY CANNOT SERVE: five independent bodies — 1EdTech, the OECD, HolonIQ, a US state legislature and the EU AI Act — are all converging on DEMONSTRABLE EVIDENCE as the 2026 requirement, and the open evaluation tier that would supply it is 44.4 % UNGRANTED with exactly two usable instruments worldwide.**

🔵 Every trend below is attributed to the body that stated it, with source class named. 🔴 Vendor
roundups are marked and are not primary research. 🟢 Where this pass measured something first-hand
instead of relaying it, the measurement is given with its payload digest.

### 🟢 Trend 1 — the year's consensus is *evidence*, and the convergence is independent

🔵 Five bodies with no shared interest arrived at the same requirement inside one window:

| body | what it said | source class |
|---|---|---|
| **1EdTech** | AI in education is shifting **from experimentation to governance**; clear policies, data boundaries and oversight become essential | standards consortium |
| **OECD** (2026 Digital Education Outlook) | move **beyond general-purpose AI tools toward purpose-built educational AI** | multilateral analyst, via roundup |
| **HolonIQ** | systems increasingly expect **evidence that products improve learning quality, persistence, well-being or job-relevant skills** | analyst |
| **Oklahoma SB 1734** | bars **AI as the main basis for grading or discipline**; every district to hold a written AI policy before 2027-28 | legislative tracker |
| **EU AI Act** | education access and assessment are **high-risk**: conformity assessment plus human oversight able to monitor, intervene, override and shut down | regulation, commentary-relayed |

🟢 **Four of the five are not asking for better models. They are asking to be shown the working.**
🔴 And the open-source tier that would show it is this KB's worst-licensed shelf: nine instruments,
**four ungranted** (including ETH Zurich's EMNLP-2025-Oral `mathtutorbench`), one NonCommercial, one
bespoke internal-eval-only, one AGPL — and **two** usable, at **4★** and **9★**
(`agents/top.md`). 🔵 **The trend and the supply are moving in opposite directions**, which is the
most commercially legible fact this pass produced.

### 🟢 Trend 2 — capability has commoditised at the agent tier; the grant has not

🔵 Measured first-hand across this pass and `p472`:

| tier | permissive share | ungranted share | measured where |
|---|---|---|---|
| 🟢 Learning-record / analytics infrastructure | **55.6 %** (+11.1 % ECL-2.0) | **0 %** | `repos/foundations.md`, n = 9 |
| 🟡 Agents | 42.9 % | 14.3 % | `agents/top.md` `p472`, n = 14 |
| 🔴 Evaluation / benchmarks | 22.2 % | **44.4 %** | `agents/top.md` `p473`, n = 9 |

🟢 **The ordering is not random and the mechanism is readable.** The infrastructure tier is built to
**consortium specifications** — xAPI, IMS Caliper, OneRoster — and a project built to interoperate is
built to be adopted, so it carries a grant. The agent tier is built by people shipping products, who
reach for a licence out of habit. The evaluation tier is built by researchers whose artefact of
record is the **paper**; the repository is a supplement, and a supplement does not get a LICENSE
file. 🔵 **Prediction for the next pass to test:** any education-AI tier defined by a published
*specification* will show a near-zero ungranted rate, and any tier defined by a published *paper*
will show a high one. `caliper`, `OneRoster`, `LTI` and `QTI` are the specification-side tokens;
`*Bench`, `AIED`, `BEA` and `EDM` are the paper-side ones.

### 🟢 Trend 3 — binding AI law is now in force in APAC, and education is named high-risk by statute

🔵 Not proposed, in force:

- 🟢 **South Korea** — the **AI Basic Act took effect 2026-01-22**, reported as the world's second
  comprehensive AI law.
- 🟢 **Vietnam** — **Law on AI No. 134/2025/QH15 in force 2026-03-01**, and a government list classes
  **education AI (automated assessment, behavioural monitoring) as high-risk**. 🔴 Compliance
  deadline disputed between sources: **2027-03-01** with a six-month grace for running systems, or
  **2027-09-01**.
- 🟡 **Japan / Singapore / Australia** — voluntary guidelines, a voluntary testing toolkit, and a
  National AI Plan (Dec 2025) resting on technology-neutral law with **mandatory guardrails paused**.

🔴 **The live trend is divergence, not harmonisation.** Within one region, a behavioural-monitoring
tutor is a statutory high-risk system in Vietnam, a voluntary-toolkit matter in Singapore and
unregulated-by-design in Australia. 🔵 A multi-country APAC rollout cannot carry one compliance
posture, and `intel/market.md` now records the instruments by name.

### 🔴 Trend 4 — classroom restriction is arriving from directions a vendor roadmap does not model

🔵 Three distinct restriction mechanisms were observable in one pass, none of them a national
curriculum rule:

| mechanism | instance | why it is the awkward one |
|---|---|---|
| 🔴 **District moratorium** | New York City's one-year ban on student-facing AI through eighth grade, promoted as a template (carried from `p472`) | the buyer and the banner are the same institution |
| 🔴 **Decision-authority limits** | Oklahoma SB 1734 — AI barred as the **main basis** for grading or discipline | constrains the architecture, not the procurement |
| 🟡 **Consent gates** | Alabama and Missouri bills requiring **written parental opt-in** | makes per-student enablement a product requirement |
| 🔵 **Student-authored restriction** | the **STUDENTS FIRST Act of 2026**, written by students from all 50 states with Day of AI and AASA, proposing that students not use AI to generate written or artistic work — a proposal, not law | the constituency assumed to be pulling hardest is pushing back |

🟢 **Operative reading:** the restrictions cluster on **student-facing generation** and on
**AI-as-decision-maker**, and leave **teacher-facing preparation** and **measurement** largely
untouched. That is a product-shape instruction, not a market-size one — and it points at exactly the
tier `compose/patterns.md` `P473-3` builds.

### 🟢 Trend 5 — adoption figures have stopped being the interesting number

🔵 This pass's legs returned **92 %** of university students using AI (one 2026 report) and **86 %**
across 16 countries (a second, different method), against **~60 %** of US K-12 teachers (Gallup, via
roundup) and **26 %** of US teens using ChatGPT for schoolwork (Pew, via roundup).

🔴 **Four figures, four methods, no comparability** — and none of them changes a decision. 🟢 The
pair that does is UNESCO IESALC's LATAM **87 % using / 26 % with a strategy**, because the two halves
are measured on the same population by the same instrument, and the gap between them is the scope of
work. 🔵 **Rule for this file going forward:** an adoption percentage is worth carrying only when its
denominator is shared with a governance percentage. Otherwise it is a headline, not a finding.

### 🔴 Trend 6 — a counter-trend this base is positioned to see and the literature is not: discovery language is now a market boundary

🟢 This pass ran the LATAM leg on **Portuguese and Spanish tokens** rather than English, as
`Gap 467-E` prescribed, and the standing finding inverted: LATAM open-source education supply went
from *"1 row in 103, archived"* to a working stack — a school information system with **552 forks**,
a gradebook, the **national curriculum as MIT-licensed open data** (1,721 objectives) and a
**CC BY 4.0** benchmark over it (`intel/market.md`).

🔴 **And the language boundary reaches past discovery into grading.** `portabilis/i-diario`'s licence
payload is an **AGPL-3.0 in Portuguese** — `LICENÇA PÚBLICA GERAL AFFERO GNU`, 35,326 B
`fe85f94658bf`, read first-hand — which every English-title-anchored reader on this base returns as
`UNSTATED` (`verticals/solutions.md`, `Gap 473-C`).

🔵 **The trend statement, generalised and testable:** *the apparent geography of open-source supply
is substantially an artefact of the searcher's language.* 🟢 It predicts that the same leg run in
**Arabic and Turkish** will move the EMEA Middle East / Africa picture the way Portuguese moved
LATAM — registered as **`Gap 473-E`** and the cheapest high-value leg available to the next pass.

### 🔵 Declared gaps on this shelf

- 🔴 **Trend 2's tier comparison rests on n = 9, n = 14, n = 9.** The ordering is clean and the
  mechanism is plausible, and neither makes it robust. It must be re-measured at a larger
  denominator before it carries a client argument.
- 🔴 **No trend on this file is primary-sourced for the EU.** `europa.eu` does not resolve from this
  host; every AI Act date is commentary-relayed (`intel/market.md`).
- 🟡 **Trend 5's rule retires figures this file has previously led with.** Applied strictly, the
  92 % / 86 % / 60 % / 26 % set is demoted to context. Recorded as a deliberate demotion so a later
  pass does not read their absence as a gap in coverage.

## 🆕 `p472` — `2026-10-27` — **🔴 THE BINDING CONSTRAINT ON THE EDUCATION-AI SHELF IS NO LONGER CAPABILITY OR COST — IT IS THE GRANT, and the correlation runs the wrong way: of the five most-starred education-AI repositories live this window, THREE cannot enter a paid deliverable. Star rank is anti-predictive of usability at the top of this market.**

🔵 Eight trends. Each is stated as a claim, with the measurement or source that supports it and the
consequence for an engagement. Where a trend is a reversal of a prior pass's reading, that is said.

### 🔴 `T1` — Licence, not capability, is what stops an education-AI engagement

🔵 Measured this pass across the 14 live top-tier agents, every grant read by payload:
**42.9 % permissive** (6), **21.4 % copyleft** (3), **14.3 % CC BY-SA** (2), **7.1 % non-commercial**
(1), **14.3 % ungranted** (2). 🔴 Ranked by stars, positions **1–5** are Apache-2.0, MIT,
**UNGRANTED** (29,550★), **CC BY-SA** (4,788★), **CC BY-NC** (4,086★).

🟢 **Consequence.** A studio that shortlists by stars shortlists an unusable repository three times
in five. The shortlist must be **licence-first, star-second** — which is the ordering
`agents/top.md` now publishes in.

### 🔴 `T2` — The richest new curriculum assets are deliberately not licensable

🔵 The two most substantial curriculum-structure artefacts of this window and the last are
[cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) (**CC BY-NC 4.0**;
1,644 knowledge points, 2,403 prerequisite edges, 6,723 items, 4,086★ in nine days) and
`withmarbleapp/os-taxonomy` (**ODbL**, recorded `p384`; 1,590 topics, 3,221 prerequisite edges).

🔴 **The primitive the market is converging on exists, and a consultancy may not sell it.** Both are
database/content licences chosen to exclude commercial reuse or to force share-alike.

🟢 **Consequence.** Curriculum graphs must be **generated from the client's own curriculum**, not
imported. The permissive tool for that is
[lineage-skill](https://github.com/JuneYaooo/lineage-skill) (Apache-2.0) — recipe `P5`.

### 🟢 `T3` — The unit of education AI is now the agent skill, not the application or the LMS plugin

🔵 Evidence, all live this window: `book-to-skill` (**36,206★**, MIT),
`Auto-Empirical-Research-Skills` (4,788★, 23,000+ skills), `education-agent-skills` (914★, 165
skills), `claudemy` (466★), `lineage-skill` (463★), `Papermorph` (961★). Every one ships as a
**skill mounted into a coding-agent harness**. None is an LMS plugin.

🟢 **Consequence.** The integration target has moved. A 2024-vintage proposal integrated with
Moodle's plugin API; a 2026 one mounts skills in a harness and reports results back over
**SCORM/LTI** — which is why `scorm-again` (MIT) is on `repos/foundations.md` as a seam, not a
nicety.

### 🟢 `T4` — APAC leads the open-source education build, not North America

🔵 The largest education repository on this shelf is **DeepTutor** (HKU Data Intelligence Lab,
Apache-2.0, **44,177★**, 5,586 forks). APAC-origin rows also include `ai-shifu` (Apache-2.0),
`ChatTutor` (AGPL-3.0), `lineage-skill` (Apache-2.0), `frappe/lms` (AGPL-3.0, India),
`cn-math-taxonomy` (CC BY-NC) and `DeepTutor-AILearning` (Apache-2.0).

🔴 North America's two most distinctive rows this window are both **ungranted**
(`Mr.-Ranedeer-AI-Tutor`, `ai-ethos`).

🟢 **Consequence.** For an education engagement the permissive technical base is **APAC-sourced**,
while the paying demand and the regulatory pressure are NA/EMEA. That asymmetry is a sourcing
advantage, not a problem — the licences permit it.

### 🔴 `T5` — The LMS core a client already runs is almost certainly copyleft

🔵 Of the four most likely incumbents, **all four** are copyleft and **three are AGPL**:
Moodle **GPL-3.0**, Canvas **AGPL-3.0**, Open edX / Tutor **AGPL-3.0**, `frappe/lms` **AGPL-3.0**.
AGPL reaches **network use**, so hosting a modified build for the client's users triggers
disclosure to those users.

🟢 **Consequence, and it is the reversal worth recording.** The permissive alternatives exist and are
**absent from the market literature**: the vendor LMS comparison read this pass names seven
platforms and **never states that Sakai is permissive** (ECL-2.0), while omitting OpenOLAT
(Apache-2.0), Oppia (Apache-2.0), Kolibri (MIT) and Academico (MIT) entirely. The permissive
shortlist is a differentiator precisely because the market does not publish it.

### 🟢 `T6` — Analysts have turned against general-purpose AI in education

🔵 The **OECD 2026 Digital Education Outlook** argues for **purpose-built educational AI over
general-purpose tools**. Independent commentary this pass calls the move away from generic AI tools
toward education-specific platforms *"the defining trend"*. 1EdTech names **digital credentials** as
a core mechanism for skills-based learning and hiring. Multiple sources report education systems now
**demanding evidence** that a product improves learning quality, persistence, well-being or
job-relevant skills.

🟢 **Consequence.** The analyst position favours a **studio build over a licence-and-rollout**, and
the evidence demand means an engagement must ship **measurement**, not just a tutor. 🔴 Which
collides with the standing gap below.

### 🔴 `T7` — Governance, not capability, is the gate — and the gap is measurable

🔵 **Experimentation → governance** is the one claim every source class in this pass agrees on. The
hard numbers: **87 % of LAC institutions use AI, 26 % have a strategy** (UNESCO IESALC/UNU-IAS, 200
institutions, 19 countries); **134 AI-education bills across 31 states** in the US in 2026; the
**EU AI Act** classes admissions, evaluation and exam scoring as **high-risk**; **Korea's AI Basic
Act** in force 22 January 2026; **Vietnam** classes education AI high-risk.

🟢 **Consequence.** The **61-point adoption-governance gap** is the most saleable finding on this
shelf, and it is a **strategy and assurance** engagement before it is a build one — recipe `P6`.
🔵 Three regimes (Oklahoma/Maryland, the EU AI Act, Vietnam) independently require a **human in the
loop on consequential decisions**, which makes human sign-off a **component to build**, not advice
to give — recipe `P4`.

### 🔴 `T8` — The measurement layer this market now demands does not exist in open source

🔵 Searched this window at every star floor — `education agent`, `topic:edtech`,
`topic:education-ai`, `topic:lms`, `grading topic:education`, `topic:curriculum`: **no open-source
education-AI evaluation or observability harness surfaced.** Carried unfilled from prior passes.

🔴 **This is the sharpest contradiction on the shelf.** `T6` says systems are demanding rigorous
evidence of learning gains; there is **no permissive, maintained harness for producing it**. The
nearest components are psychometric libraries ([inuyasha2012/pypsy](https://github.com/inuyasha2012/pypsy), **MIT** — `master/LICENSE`,
1,068 B, 241★ — IRT, CAT, cognitive diagnostic models, factor analysis, SEM) and the autograders (`Autolab` Apache-2.0, `Submitty` BSD-3-Clause), none of which
evaluates an *agent*.

🟢 **Consequence — and this is the build-vs-buy call.** Globant cannot buy this layer and cannot
fork it, so an engagement that promises learning-gain evidence must **cost the measurement harness
as original work**. 🔵 Stated as an opportunity rather than only a gap: it is the one piece of this
stack with no incumbent.

### 🔵 Honest statement of what this pass could not establish

- 🔴 **No Middle East or Africa education-AI evidence** beyond the UAE compulsory-subject mandate —
  no Gulf programmes, no Saudi initiatives, no African policy, no repository at any star floor.
- 🔴 **No live LATAM-origin education repository** — the one found is archived.
- 🔴 **Market sizing is incoherent across sources** and one widely circulated North America figure is
  arithmetically impossible as published (`intel/market.md`). No single market number should be
  quoted from this shelf.

## 🆕 `p471` — **🔴 THE TREND WITH A DATE ON IT: three jurisdictions on three continents have independently converged on the SAME regulatory test — AI is high-risk in education only where a human cannot meaningfully review the decision — which makes "reviewable human decision point" a product requirement rather than a compliance afterthought. 🟢 And the off-class rate of this file's own regional instrument is shown to be VOLATILE between passes on identical input, which retires a measurement `p470` treated as a property.**

🔵 Gate not attested (`Gap 446-A`); checks re-implemented in-session and green.

### 🟢 Trend 1 — regulatory convergence on human reviewability, across three regimes

🔵 Three instruments, three regions, no coordination, one test:

| regime | the clause | effect |
|---|---|---|
| **EMEA** — Regulation (EU) 2026/1744 / AI Act Annex III | Qualified human staff must be able to **monitor outputs, intervene, override a decision and shut the system down** | Obligation, from **2 December 2027** (stand-alone) / **2 August 2028** (embedded) |
| **APAC** — Vietnam Decision No. 33/2026/QD-TTg | Education AI is high-risk **only where the output is the sole basis for a decision without meaningful human review** | 🟢 **Carve-out** — compliance **1 March 2027** |
| **North America** — Oklahoma, Maryland | Require human oversight; **bar AI from high-stakes student decisions** | State statute |

🔴 **This is the single most transferable design constraint on these shelves.** One architecture —
every assessment, placement or progression output passing through a reviewing educator with
override and shutdown, and an audit trail proving it — simultaneously keeps a system out of
Vietnam's high-risk tier, satisfies EMEA's oversight duty, and meets US state rules. 🟢 **Build it
once as a component**, not per engagement. 🔵 The trend to watch is whether the carve-out form
(Vietnam) spreads, because it is the version that rewards good design rather than merely documenting
it.

### 🟢 Trend 2 — the governance gap is now evidenced at practitioner level, not just institutional

🔵 For four passes this file has carried "adoption outpaces governance" from institutional
self-report. **TALIS 2024** puts teacher-level numbers against it for the first time:

| country | secondary teachers using AI | vs OECD average 36 % |
|---|---|---|
| Brazil | **56 %** | +20 |
| Chile | **55 %** | +19 |
| Colombia | **53 %** | +17 |
| Costa Rica | **52 %** | +16 |

🔴 Set against **26 %** of LATAM institutions having a formal AI strategy (UNESCO IESALC, 200
institutions, 19 countries), the gap is no longer an impression: **practitioners are 16–20 points
above the OECD mean while institutions are mostly ungoverned.** 🟢 Double-sourced across two
independent instruments, which is new.

### 🔴 Trend 3 — the governance demand has no open-source supply, and that is now bounded

🔵 Measured this pass on a licence-filtered leg: `education governance license:mit` returns **61
repositories in total, maximum 16★**, with five of the top eight off-class (DeFi token platforms, a
climate atlas). 🔴 Against a demand signal this strong, **the supply ceiling is 16 stars.** The trend
is a widening mismatch, and its practical form is that institutional AI governance is a
**build-from-scratch** engagement with no credible OSS starting point — unusual on shelves where
almost every other category has one.

### 🟢 Trend 4 — national AI curriculum mandates are now dated procurement events

🔵 Five jurisdictions have moved from policy language to a fixed academic year:

| jurisdiction | region | mandate | from |
|---|---|---|---|
| UAE | **EMEA** | AI compulsory KG–Grade 12, 7 core areas, no written exams | 2025–26; private schools reported **Aug 2026** |
| Qatar | **EMEA** | AI + data science across primary, preparatory, secondary | **2026–27** |
| India | **APAC** | CBSE Computational Thinking & AI, Classes III–VIII (circular Acad-15/2026) | **2026–27** session |
| China | **APAC** | MoE "AI Plus Education" — dedicated primary/secondary AI courses | announced **10 Apr 2026**, full by **2030** |
| South Korea | **APAC** | 20 universities selected from 80 for AI basic curriculum, all majors | **2026** |

🔵 The trend is the **shift in buyer**: these are ministries committing to delivery on a date, which
converts AI-in-education from discretionary edtech spend into teacher-training, content-production
and assessment-tooling programmes at national scale. 🔴 Note the asymmetry — four of five are APAC
or Gulf. No EU member state appears on this list.

### 🔴 Trend 5 — "root licence" is failing as an industry screen exactly where platforms live

🔵 Measured over 229 education repositories: **33 (14.4 %)** carry a licence grant below their root,
and the rate is monotonic in tree size — **0.0 %** under 25 paths, **66.7 %** above 2 000. Every
major LMS sits in the top band.

🔴 **The trend is that the shape is becoming structurally more common, not less.** The mechanism is
forced rather than evasive: Moodle is GPL, so any Moodle plugin must be GPL — therefore **every
permissive education project that ships an LMS integration acquires a copyleft subtree**. As LMS
integration becomes table stakes for education AI products, the partitioned-grant repository becomes
the norm. 🔵 And it cuts both ways: this pass found a repository that is **part copyleft and part
proprietary** (`particify/arsnova-server`: GPL-3.0 at `core/`, "All rights reserved" at
`formatting/`), and two platforms that a root-path screen called ungranted and that are granted.

### 🟡 Trend 6 — retired: the off-class rate of this file's own regional instrument

🔵 `p470` measured the prescribed EMEA leg at **0 on-class of 10** and registered the off-class rate
as a property of the query template. Re-run this pass, **unchanged**, the same leg returned **9
on-class of 9**.

| region leg | `p470` on-class | `p471` on-class |
|---|---|---|
| North America | high | 9/9 |
| **EMEA** | 🔴 **0/10** | 🟢 **9/9** |
| APAC | low | 2/9 |
| LATAM | high | 10/10 |

🔴 **A measurement that inverts on identical input across one day is an index property, not a query
property.** The mechanism `p470` identified (enterprise-analyst register colliding with education
vocabulary) is real and still visible in the APAC leg — but the *rate* is volatile, and a single
pass's off-class reading cannot license a template change. 🟢 Registered on `intel/market.md` as
`Gap 471-F`.

### 🔵 Trend 7 — rubric and assessment feedback is where the week's granted supply actually appeared

🔵 Two of two granted novel rows this pass are rubric components
(`TREMA-UNH/rubric-grading-workbench` MIT 15★, `ChantillyAn/homework-grader` MIT 7★), while the
general education-vocabulary legs returned **0 unshelved of 14**. 🔵 Consistent with `p469`, which
closed the same gap with four MIT grants all at 0–4★. 🔴 The standing caveat holds and is the trend:
**this category's supply is real, permissive and uniformly tiny** — single-maintainer repositories in
the single digits to mid-teens of stars. Fork-and-own; do not take a dependency.

## 🆕 `p470` — **🟢 Four trends, each with a denominator measured this pass: (1) the open grant is fragmenting *inside* the repository — by subdirectory and by asset, not by project; (2) education's regulatory clock in EMEA now runs backwards and forwards at once, a prohibition closing as a high-risk regime opens; (3) the governance demand this base measured has no supply behind it — 70 novel addresses, zero governance tools; (4) permissive curriculum supply arrived in quantity and entirely at micro-scale.**

### 🔴 1. The grant is fragmenting inside the repository, not between repositories

🔵 This base has tracked the grant moving *between* things: from repository to asset (`p467`), from
code to corpus (`p464`), from permissive form to restrictive terms (`p467`). This pass the
fragmentation is finer still — **inside a single repository, by directory**.

| case, read first-hand `2026-10-27` | the shape |
|---|---|
| [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) | **MIT** at `LICENSE.md` (1 087 B) · **GPL-3.0-or-later** at `plugin/edukorsplayer/COPYING.txt` (35 151 B) · third-party MIT notices at a third path |
| [`mathruffian-dot/taigi-teaching-agent`](https://github.com/mathruffian-dot/taigi-teaching-agent) | **MIT** code (1 453 B payload) · ministry dictionary content, official audio, a TTS service and a third-party model each **outside** the grant |
| [`lbhubedu/lbedu.me`](https://github.com/lbhubedu/lbedu.me) (`p469`) | **MIT** code · brand, institutional texts and `public/images/` reserved *All Rights Reserved* |

🔵 **Three repositories, three different partition axes — directory, asset class, content type — and
all three publish a single permissive SPDX identifier.** GitHub's licence field says `MIT` for all
three, and it is not wrong; it is answering a question about the root payload that nobody asked.

🔴 **Why this is a trend and not three anecdotes: the cause is structural.** Moodle is GPL, so a
Moodle integration must be GPL. Ministry curriculum corpora are state-owned, so a
curriculum-aligned agent cannot relicense them. Institutional brand and editorial copy are the
institution's, so a school's own web app reserves them. **Every education project that integrates
with an LMS, aligns to a curriculum, or belongs to an institution has a partitioned grant waiting
inside it** — and education projects are, by definition, usually all three.

🟢 **The consequence for a studio:** the licence question is no longer "what is this repository?" but
"**which part of it am I shipping?**" A root-path licence sweep — the instrument this base spent five
passes refining — answers the first question correctly and cannot see the second.

### 🔴 2. EMEA's regulatory clock now runs in both directions at once

🔵 `p464` found that regulation diverged by **duty type** inside one region. This pass that
divergence acquires exact dates from a named instrument — **Regulation (EU) 2026/1744**, OJ L of
24 July 2026, in force 27 July 2026.

| duty | direction | date |
|---|---|---|
| Annex III high-risk — education admissions, assessment, proctoring | 🟢 **relaxed by 16 months** | 2 August 2026 → **2 December 2027** |
| New prohibition — non-consensual intimate imagery, CSAM | 🔴 **tightened; new obligation** | **2 December 2026** |
| Article 50 transparency, prohibited practices, GPAI duties | unchanged | live now |

🔴 **So the same amendment that bought sixteen months of assessment runway opened a prohibition five
weeks out.** A studio reading only the headline — "education high-risk postponed to 2027" — scopes
an EMEA engagement that is simultaneously *less* urgent on assessment and *more* exposed on
generative media, and will find the second out at the wrong moment.

🔵 **The structural point:** postponement is not deregulation, it is **re-sequencing**. The duties
that moved are the ones requiring conformity infrastructure that does not exist yet; the ones that
did not move are prohibitions, which need no infrastructure — only prevention. Where a duty is a
prohibition there is no risk tier to argue about and no conformity route to buy.

### 🔴 3. The governance demand has no supply behind it, and that is now measured

🔵 `p468` measured the demand: **87 % of 200 institutions across 19 countries using AI, 26 % with a
formal AI strategy** — a 61-point gap — and inferred that the regional sale is governance. The open
question was whether the supply existed and this base had simply not looked.

🔵 This pass looked, with a leg built for it. **70 addresses novel to this entire base. Education
governance tools among them: zero.** The leg returned awesome-lists, MCP server catalogues, graduate
job boards, one author's eight crypto-MCP repositories, an AI glossary, a PDF-workflow collection.

🟢 **One exception in 70**, and it is substrate rather than a governance product:
`panaversity/ksor` (Apache-2.0, 232★) — one authoritative knowledge record that tutor, TA and
assessment agents read from, so they cannot contradict each other or the catalogue.

🔴 **The trend, stated as a ratio:** education AI's **demand** has moved to governance and its
**open supply** has not followed at all. Every other category this base tracks — tutoring, marking,
content generation, knowledge graphs — returned multiple granted rows this pass. Governance returned
one, and it is a knowledge layer rather than a policy, audit, disclosure or oversight tool.
🟢 For a studio that is the opportunity rather than the obstacle: the governance layer in an
education engagement is **billable build work**, because there is nothing to assemble it from.

### 🟢 4. Permissive curriculum supply arrived in quantity — and entirely at micro-scale

🔵 `p467` specified a permissive replacement for a **4 000★ `CC-BY-NC-4.0`** curriculum knowledge
graph and could not source one. This pass sourced **ten MIT concept- or curriculum-graph projects**
on a licence-filtered leg, every grant read first-hand.

| 🟢 what closed | 🔴 the other half |
|---|---|
| Ten MIT grants for the exact job: `edukors_graph`, `chat-edu/v3`, `Bodhi`, `recall`, `huoshu`, `exam-kit`, `benkyo`, `aula`, `syllabusgraph`, `curriculum-knowledge-graph` | Star counts: **17, 16, 5, 5, 3, 3, 2, 2, 1, 1**. Sixteen of this pass's twenty granted rows are at 5★ or below; twelve are single-maintainer; one 16★ row is abandoned with a boilerplate README |

🔴 **This is the third consecutive pass where a named supply gap closes at micro-scale** —
`Gap 464-A` (rubric feedback: four MIT grants at 0–4★), `p469`'s platform census (one permissive LMS
in eight), and now curriculum graphs. 🟢 **The pattern is stable enough to state as a trend:
permissive education supply exists for almost every job and almost never exists at scale.** What is
available is a **schema and a reference implementation**, not a dependency with a maintainer behind
it. The studio economics follow: fork-and-own, budget the maintenance, and never present one of
these as a vendor component.

🔵 **And a methodological trend continuing from `p465`:** this pass's own instrument was again the
least reliable thing in it. The licence classifier published two wrong class verdicts and seven
false restriction flags before correction — mislabelling GPL-3.0 as AGPL-3.0 because **GPL-3.0's §13
names the AGPL three times inside its own text**. The base's prior reads were right across 31
repositories; the new instrument was wrong. Read the title, not the body.

## 🆕 `p469` — **the market stopped asking whether AI works in education and started asking who signs for it — and the open-source supply has not followed**

🔵 Eight trends, each with the evidence behind it and the date it was read. Where a trend rests on
a secondary source that disagrees with another, both readings are published.

### `T469-1` 🟢 Governance replaced experimentation, and it happened across all four regions at once

1EdTech reads institutions moving to AI strategies with defined **governance, compliance and
evaluation processes**. HolonIQ reads a shift from broad personalisation promises to **ethics,
transparency and proven instructional benefit**. Campus Technology's leaders expect AI to become
**embedded infrastructure** rather than standalone pilots. 🔵 The convergence is the signal: four
independent analysts, four vocabularies, one direction. 🟢 **What it means for a studio:** the
first deliverable in an education engagement in 2026 is a **governance artifact** — policy,
oversight design, audit trail — and the model work is the second. Selling the tutor first is
selling last year's engagement.

### `T469-2` 🔴 Evidence of learning gain is now a procurement gate, and vendor numbers do not clear it

HolonIQ records that systems now **expect evidence** that a product improves learning or
job-relevant skills. The IDB's review of **193 LATAM initiatives** found **few with rigorous
evaluation**. 🔴 Against that, this pass read a vendor claim of **"42 % outcome gains"** with no
methodology attached. 🟢 The gap between the demand and the available proof is a **service line**:
instrumentation, baselining and an evaluation design a client can publish. Almost nobody in the
open-source supply has it — `agents/top.md` carries no education-specific eval harness, and
`p468`'s "no dominant OSS agent eval/observability" finding is unchanged.

### `T469-3` 🟢 Teacher-side workflow is where adoption actually is, and it is where the supply just arrived

**60 % of US K-12 teachers** used AI tools in 2024-25, **32 % at least weekly**. **TALIS 2024:
56 % of secondary teachers in Brazil, 55 % in Chile, against an OECD 36 %.** Teacher time-saving is
the recurring theme across every regional source this pass. 🟢 And the new granted supply this
pass is **all teacher-side**: rubric grading with override (`vijju9019/GradeAI`), lab/exam
generation with a human-review stop line (`littlecookie0722/AI-Teaching-Agent`), curriculum-aligned
lesson planning (`ThallesYVasconcelos/Agente-Educacional`). 🔴 All at 0–4★. The demand is
measured in national surveys; the supply is measured in single-digit stars.

### `T469-4` 🔴 Human review has moved from good practice into statute, and Vietnam wrote the spec

Oklahoma and Maryland bar AI from high-stakes decisions about students and require human
oversight. Vietnam's 2026 decision makes education AI high-risk **only where AI output is the sole
basis for a decision without meaningful human review**. The EU makes a school using a commercial
tool to assess progress a **deployer** with its own duties. 🟢 **The architectural consequence is
identical in all three jurisdictions:** a decision point with a recorded human in it is out of the
strict tier by construction. 🟢 This is why `vijju9019/GradeAI`'s **teacher review cockpit** and
`AI-Teaching-Agent`'s **human-decision stop line** matter more than their star counts — they are
the shape the law now asks for, in permissively-granted code.

### `T469-5` 🟡 The EU's high-risk date for education moved sixteen months, and the market has not repriced

Reported postponement of Annex III education obligations from **2 August 2026 to 2 December 2027**
via the AI omnibus (adopted June 2026, in force 27 July 2026), while the **AI literacy duty has
been live since 2 February 2025**. 🔴 Sources still disagree on the date and this pass **could not
reach the primary source** (`Gap 469-E`). 🟢 Either way the near-term EMEA work is unchanged and
sellable now: the literacy duty has no grace period, two-thirds of European education systems
already hold a strategy document, and the implementation behind those documents does not exist.

### `T469-6` 🟢 Purpose-built beats general-purpose, and this pass has a clean negative control for it

TeachBetter reads the market moving away from generic chatbots toward platforms built around
**learning objectives and curriculum**. 🟢 The control is on `agents/top.md`:
`ThallesYVasconcelos/Agente-Educacional` grounds every answer in **BNCC, PCN and PNLD with page
citations** and maps content to **EF01–EF04 skill codes** — a general chatbot cannot produce that
and a Brazilian teacher cannot use an answer without it. 🔴 And the negative half:
`makecindy/cindy` is Apache-2.0, **6 532★**, trending, filed by a roundup under an education trend,
and useless for education — stars and momentum do not survive the curriculum requirement.

### `T469-7` 🔴 Open-source education supply is academic, and nothing commercial is entering it

The only education projects on October-2026 trending boards are **HKU's DeepTutor** (Apache-2.0,
43 930★) and **Tsinghua's OpenMAIC** (MIT, 41 563★). Every other granted education row on these
shelves is a **single maintainer**. There is **no vendor-backed open-source education project** on
the boards at all. 🟢 **The reading for Globant is direct and it is favourable:** the research is
open and permissive, the production engineering around it — governance, audit trails, SIS
integration, evaluation, operations — is absent, and that is precisely what a studio sells.
OpenMAIC's **15.5 % fork-to-star ratio** against DeepTutor's 12.6 % says people are already trying
to build on it.

### `T469-8` 🔴 A permissive licence label is the least reliable field in the entire edtech press

This pass refuted **two** licence claims from current "best open-source LMS 2026" roundups:
`frappe/lms` labelled MIT is **AGPL-3.0** (`license.txt`, 33 893 B, `db1a87ba81e8`), and
`formalms/formalms` labelled Apache-2.0 serves **no grant at ten paths**. It confirmed a third
(`OpenOLAT`, Apache-2.0, 10 982 B). 🔵 This is the same error class these shelves have found in
`p466` (CC-BY-SA, Elastic-2.0, CC-BY-NC rows passing a star-and-LICENSE screen), `p467` (a
permissive grant *form* restricted to non-commercial use in the same payload) and `p469`
(`lbedu.me`'s reserved-rights carve-out below the warranty clause). 🟢 **The standing conclusion,
now reproduced across four passes:** a licence is a **payload read at `HEAD`**, never a column in
a listicle and never an SPDX badge in a README. On these shelves the error rate of the secondary
channel on this one field is **2 in 3**.

## 🆕 `p468` — **🟢 Four trends, each with a denominator measured this pass: (1) discovery vocabulary, not supply, is what was exhausted — 14.1 % novel in English against 80.0 % in Spanish and Portuguese; (2) automated assessment is the regulated surface in three regions under four instruments; (3) detection EVASION is a permissively licensed, actively maintained market segment; (4) LATAM adoption has outrun LATAM governance by 61 points.**

### 🟢 Trend 1 — Apparent saturation is a language artifact, and the correction buys visibility rather than supply

🔵 **Measured at n = 79** distinct addresses across five discovery legs this pass.

| query language | graded | novel by address | novel rate | usable build-on yield |
|---|---|---|---|---|
| English (3 legs) | 64 | 9 | **14.1 %** | 3 |
| Spanish + Portuguese (2 legs) | 15 | 12 | **80.0 %** | **0** |

🔴 Six consecutive passes published *"usable novel yield ZERO"* from English-only legs and
attributed it to an exhausted supply. **A 5.7× difference in novel-by-address rate comes from the
query language alone.** 🟢 But the second column is the one that governs a decision: the twelve
non-English novel addresses are a doctoral thesis site, three teacher-training project pages from
one account, a survey's supplementary material, an essay, a prompt library and two pieces of
software — one of which serves no grant.

🔵 **The generalisable claim:** non-English discovery reveals that LATAM and Spanish-language
education work exists in volume and is **predominantly academic output rather than shipped
software**. That is a finding about the regional ecosystem, not about the search index.

### 🔴 Trend 2 — Automated assessment is the regulated surface, in three regions, under four instruments

| jurisdiction | instrument | what it names |
|---|---|---|
| EU | AI Act, Annex III | admissions, student evaluation — high-risk |
| Vietnam | AI Law | automated assessment, behavioural monitoring — high-risk |
| US (Oklahoma, Maryland) | state law | AI barred from high-stakes decisions about students; human oversight required |
| US (New York City) | DoE guidance | AI barred from grading, discipline, IEP development |

🟢 Four instruments written independently converge on the **same feature**. 🔵 The design
consequence is concrete and should be read as a constraint on every recipe in
[`compose/patterns.md`](../compose/patterns.md): **a grading or placement feature is the part of
an education build that attracts an obligation.** Products that assist a human assessor carry a
materially lighter burden than products that decide, in every one of the four.

### 🔴 Trend 3 — Detection evasion is a permissively licensed market segment, not a fringe

🔵 **n = 1 this pass and named as such**, but the row is unambiguous:
[`rudra496/StealthHumanizer`](https://github.com/rudra496/StealthHumanizer) — **189★**, **MIT**
(1 074 B · `8967efcf60c6` @ `c727cd6774f7`, read first-hand), 16+ languages, actively pushed
(last push 2026-10-26), stated purpose defeating Turnitin and GPTZero.

🔴 Two things follow. **For sourcing:** a permissive grant is not a shelving criterion — this row
passes every licence screen this base owns and is refused on purpose. **For positioning:** any
assessment-integrity product sold to an education client competes with free, MIT-licensed,
maintained tooling built to defeat it, and a proposal that does not say so is selling a
detector whose counter-tool the client's students can install in a minute.

🔵 `nietzschian-debugger` (153★, MIT) is the inverse shape on the same shelf: pedagogy that
withholds the answer. 🟢 **The design answer to evasion is assessment that evasion does not
help with**, and that is a product thesis, not a detection arms race.

### 🟢 Trend 4 — LATAM adoption has outrun LATAM governance by 61 points

🔵 UNESCO IESALC with UNU-IAS, **200 institutions across 19 countries**: **87 %** use AI in at
least one area of activity; **26 %** have a formal AI strategy. Adoption is driven by individual
academics, researchers and students rather than institutional programmes.

🟢 This is the inverse of the North American picture, where 35+ state education departments
published guidance and districts are working to dated policy deadlines. **LATAM institutions
adopted first and are governing second; North American institutions are governing first.**

🔵 For a studio the two require different first engagements: NA buys **policy-to-control
translation**; LATAM buys **discovery and inventory** — finding where AI is already in use before
any policy can be written against it. 🔴 And `p467`'s supply-side measurement sharpens the
contrast: LATAM is **one row in 103** of visible education supply, so the region with the
highest institutional adoption has the least shippable open source behind it.

### 🟡 Declared gaps — stated so silence is not mistaken for coverage

- 🔴 The **Digital Omnibus** remains unresolved on this channel for a fourteenth month. Every
  encoded EU AI Act deadline in the carried obligation-tooling tier is ungradeable.
- 🔴 **Vietnam's education compliance date is carried in conflict** (2027-03-01 vs 2027-09-01).
  Neither was read from a primary text.
- 🔴 **No primary statute was read by this pass.** Every regulatory figure above is relayed.
- 🔴 **Trend 3 rests on n = 1.** It is published because the row is unambiguous, not because the
  segment is measured.
- 🔴 **Canada and Mexico returned nothing** on the North America leg; **Africa returned nothing**
  on the EMEA leg. `Gap 463-D` closed African supply at 61 repositories with a maximum of 12★;
  the *policy* side of Africa remains unmeasured by this base.

---

## 🆕 `p467` — **🟢 Four trends, each with a denominator and each measured this pass: (1) the licence screen the whole industry uses — stars plus "has a LICENSE" — carries ZERO information about whether software can be delivered; (2) permissive grant TEXT is now being used as cover for restrictive terms; (3) the grant is migrating from the repository to the ASSET; (4) visible education supply is 21 % APAC, 1 % LATAM.**

### 🔴 Trend 1 — The industry's default licence screen is uninformative, and now it is measured

🔵 **Measured at n = 103**, every pair read first-hand
([`evidence/grant-class.2026-10-26-p467.tsv`](../evidence/grant-class.2026-10-26-p467.tsv)):
grant *presence* rises with popularity (**1.00** at ≥ 1 000★ against **0.82** below 100★), while
grant *permission* is **flat: 0.62 / 0.53 / 0.68 / 0.58**.

🔴 **So "popular and it has a LICENSE file" — the screen almost every buyer and most vendors
actually apply — predicts nothing about deliverability.** 🟢 It also refutes `Gap 466-B`'s own
premise, which generalised from a single 498★ ungranted row: star-ordered probing does **not** waste
effort on ungranted supply. 🔵 The operational rule is the inverse of what the gap prescribed:
**the grant-class read can never be skipped on a high-star row** — the three rows that forced this
whole axis into existence were 914★, 340★ and 4 000★. Full table and the registered gap on
[`agents/top.md`](../agents/top.md) (`Gap 467-C`).

### 🔴 Trend 2 — Permissive grant TEXT as cover: the "community licence"

🔵 **Measured:** [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) — 2 049★, the
most-starred education *platform* in this window — serves a payload that **opens with MIT's grant
sentence verbatim** and restricts it, in the same sentence, to *"personal, educational, or
non-commercial research purposes"*, then prohibits redistribution, requires a **revenue-sharing
agreement** before any commercial deployment, and extends Commercial Use to *"any portion, code
snippet, algorithm, design pattern"*.

🔴 **This is a new rung on a ladder these shelves have been climbing for ten passes.** `p457` found
a project **relicensing** to a commercial licence (`pengusto/google-classroom-mcp`). `p466` found
that **a present grant is not a permissive grant** (`Elastic-2.0`, `CC-BY-NC`). This pass finds
that **a permissive grant *form* is not a permissive grant** — the restrictive instrument now wears
MIT's words. 🔵 It defeats not just the naive screen but **both licence readers on this base**, and
the remedy (a restriction override that outranks the body-form layer) is implemented and
controlled. 🟡 Direction to watch: "community licence", "fair-source" and revenue-share clauses
attached to otherwise ordinary open-source projects — a packaging choice, not a legal novelty, and
cheap to copy.

### 🟢 Trend 3 — The grant is moving from the repository to the asset

🔵 **Measured:** 2 of 103 rows grant **code and data separately inside one payload**, and both are
infrastructure-tier candidates, not curiosities:

| row | ★ | what the one payload actually grants |
|---|---|---|
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | code **MIT**; datasets *"not all licensed the same way"*, labelled **Open / Open+Gated / Gated**, with the latter two *"not covered by CC BY 4.0, CC0, or any other open license"* |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 87 | code **MIT**; content **CC BY 4.0**; and the bundled Annotated CLEAR Corpus **CC BY-NC-SA 4.0** |

🔴 **A repository-level `licence` cell cannot express either of these**, which is why they graded
`UNSTATED` until this pass gave them a class. 🟡 The trend direction is clear and it is economic,
not legal: as education AI's value moves into **curriculum graphs, rubrics, item banks and
annotated corpora**, the permissive grant stays on the code — which is cheap — and the restriction
moves to the data, which is not. 🟢 `p466` saw the first instance (the most-starred *data* asset in
the window being NonCommercial); this pass shows it happening **inside** otherwise-permissive
repositories. 🔵 Consequence for delivery: **clear the content inventory separately from the code**,
and treat such a row as two procurement items.

### 🟢 Trend 4 — Visible education supply is 21 % APAC and 1 % LATAM

🔵 **Measured** over the same 103 rows by documentation language, with language ≠ domicile stated
plainly and English yielding `UNPLACED` by construction (0.74):

| region signal | share | 🟢 sellable | the shape |
|---|---|---|---|
| **APAC** | **0.21** | 0.55 | 🟢 permissive **agent** tier (12 of 22), 🔴 closed **content** tier (3 of 3 `*-NC` rows are Chinese-language) |
| **EMEA** | 0.04 | 0.50 | 🟡 under-counted on this axis — EMEA documents in English; the **forge** axis places it better (AGPL via GitLab) |
| **LATAM** | **0.01** | 1.00 | 🔴 **one row, archived**, against the strongest demand signal on [`intel/market.md`](market.md) |

🔴 **The APAC split is the actionable half:** compose the agents, license or build the content. 🔴
**The LATAM number reframes a finding this base has repeated three times:** the LATAM gap is not
mainly that the supply is ungranted — it is that **the supply is nearly absent**, so LATAM
engagements are build-and-localise, not select-and-integrate.

### 🔵 Carried trends — status this pass

| trend | status |
|---|---|
| 🟢 Education AI ships as a *skill*, not an application (`p466`, 23 %) | 🟢 **reproduced in passing** — the star-ordered population is dense with skill artefacts (`book-to-skill` 36 190★ MIT, `universal-examprep-skill`, `cram-engine`, `education-skills`, `kaogong-skill`, `awesome-student-ai-skills`), and the pattern's largest member remains a skill **compiler** |
| 🟢 The forge selects the licence family — GitHub permissive, GitLab AGPL (`p466`) | 🟢 **holds, now two-pass**: GitHub 63/92 permissive; GitLab **0 permissive in two passes**. 🔴 But `p466`'s *yield* claim for GitLab does **not** survive — see `Gap 467-H` on [`repos/trending.md`](../repos/trending.md) |
| 🟢 Regulation converging on DETERMINISTIC-AND-REVIEWABLE (`p466`) | 🟢 **holds** — this pass's North America leg adds Oklahoma/Maryland human-oversight requirements and the AASA appeal-rights framework to the same shape |
| 🟡 Market-size trajectory | 🟡 **unchanged and still a range** (`$6.4B`–`$11.4B` for 2026 across four firms). One new corroborating low-end anchor that passes the `466-F` arithmetic test; the retired `$42.48B`-by-2030 cell stays retired |
| 🔴 The macro intelligence channel is saturated | 🆕 **new this pass**: four region legs, four nils, all material already carried. The axis must change — country legs and primary sources, not region legs |

---

## 🆕 `p466` — **🟢 Four trends with denominators this pass, not adjectives: (1) 23 % of visible education supply ships as an agent SKILL with no runtime; (2) the forge selects the licence family — GitHub permissive, GitLab AGPL; (3) regulation is converging on a shape, DETERMINISTIC-AND-REVIEWABLE, from four unrelated jurisdictions; (4) the content/data layer is where the commercial closure is — the most-starred data asset found is NonCommercial.**

### 🟢 Trend 1 — Education AI is shipping as a *skill*, not an application

🔵 **Measured:** 9 of the 39 distinct repositories in the top-20s of `topics/ai-tutor` and
`topics/edtech` ship as an agent skill or MCP server; the pattern's largest member is a **36 200★**
skill *compiler* (`virgiliojr94/book-to-skill`, MIT). Reproduced independently on the
`created:>2026-09-15` recency channel. Full table and provenance on
[`agents/trending.md`](../agents/trending.md).

🔵 **What it means commercially:** the reusable asset is **the method** — rubrics, Socratic
sequencing, diagnosis-before-instruction, citation discipline — and the runtime is assumed. 🟢 That
collapses the cost of adopting pedagogy and raises the value of **owning the integration surface**
(LTI, SCORM, roster, gradebook), because that is the part a skill cannot supply. 🔴 **The
counter-force:** skills are *content*, content repositories reach for Creative Commons, and the
second-most-starred row in the pattern is `CC-BY-SA-4.0`.

### 🟢 Trend 2 — The forge selects the licence family, and therefore the delivery model

| channel | granted rows read first-hand | families |
|---|---|---|
| GitHub (topics + recency) | 12 | **MIT ×6 · Apache-2.0 ×2 · BSD-3-Clause ×1** · CC-BY-SA ×1 · CC-BY-NC ×1 · Elastic-2.0 ×1 |
| GitLab | 5 | 🔴 **AGPL-3.0 ×4 · composite ×1 — zero permissive** |

🔵 Network copyleft is not an obstacle to be routed around; it is a **fit signal**. AGPL suits the
institutional, self-hosted, sovereignty-motivated buyer — the EMEA public-sector and LATAM
public-university engagement — and is wrong for multi-tenant SaaS. 🔴 A base that samples one forge
sees one half of the market and will mis-advise the other. 🔴 Three further forges (Codeberg,
sourcehut, Framagit) are **DNS-unreachable from this environment**, so this trend is confirmed for
GitLab and **untested** elsewhere (`Gap 466-D`).

### 🟢 Trend 3 — Four jurisdictions, independently, are converging on the same required shape

🔵 Not a theme — the same three properties, named in instruments from four unrelated legal systems:

| property required | where it is written |
|---|---|
| **a human must review AI output before it affects a learner** | 🟢 Oklahoma **SB 1734** (teacher review of AI output); Idaho **SB 1227** (AI may not replace teachers); EU **Annex III** (grading that steers learning is high-risk); 🟢 Kenya **KNEC** (AI may not produce assessed learner work) |
| **no emotion or affect inference on learners** | 🔴 EU **Art. 5(1)(f)** — prohibited since **2025-02-02**, €35 M / 7 % |
| **automated decisions about a learner are themselves regulated** | 🔴 **Chile Ley 21.719** (automated profiling + algorithmic decisions, **in force 2026-12-01**); 🟢 China MOE's explicit data-security and personal-information emphasis; 🟡 Kenya's AI Bill placing education in the high-risk class |

🟢 **So the architecture is being specified by law, and it is the same architecture everywhere:**
deterministic scoring, an auditable evidence trail, a human arbiter, and no affect inference. 🔵
That is buildable today from permissive carried supply — `nbgrader` (BSD-3) for the deterministic
spine, `AutoGrader-Agent` (MIT, all arithmetic in Python not the model), `markwise` (MIT,
double-marking plus **verification that quoted evidence actually occurs in the work**), `EduShield`
(MIT, client-side de-identification before any hosted model). 🟢 `Pattern BJ` wires exactly this.

### 🔴 Trend 4 — The commercial closure has moved to the content and data layer

🔵 The code is permissive; the **assets** increasingly are not. Read first-hand this pass:

| asset | ★ | grant | effect |
|---|---|---|---|
| `xiaoyang111222/cn-math-taxonomy` — maths/English/physics knowledge graph + diagnostics | **4 000** | 🔴 **CC-BY-NC-4.0** | 🔴 **unusable in any paid engagement** |
| `GarethManning/education-agent-skills` — 165 teacher/leader skills | 914 | 🔴 **CC-BY-SA-4.0** | 🟡 adaptations inherit ShareAlike |
| `canyongbs/advisingapp` — higher-ed advising CRM + AI assistant | 340 | 🔴 **Elastic-2.0** | 🔴 forbids providing it **as a hosted service** — the Globant delivery model |
| `Zo-Dns/Al-Idrisi.AI` — Arabic AI atlas (carried, `p465`) | 4 | 🟡 MIT **code** + separate content licence | 🔴 the part a client would reuse is **outside** the MIT cell |

🔵 **The pattern across all four:** permissive source, restricted substance. 🟢 The practical rule
for a studio: **the curriculum, item bank, rubric corpus and knowledge graph are the deliverable's
licence risk**, not the framework — and they are the components a client most wants to reuse.
Pedagogical *method* is cheap and open; pedagogical *content* is where the moat was rebuilt.

### 🔵 Carried trends re-checked this pass

| trend | status |
|---|---|
| 🟢 `DeepTutor` as the category's centre of gravity | 🟢 **holds and still compounding** — **43.8k★** against the **43 537** `p465` recorded index-exact; Apache-2.0 payload reproduced byte-identical (**11 408 B · `cd2f54e1e506`** @ HEAD `a31d82624c27`) |
| 🟡 Market-size trajectory | 🔴 **restated** — the carried `$42.48B`-by-2030 cell is arithmetically irreconcilable with the same firm's 2035 horizon; see [`intel/market.md`](market.md) and `Gap 466-F` |
| 🟢 LMS incumbency as the real integration constraint | 🟢 **strengthened** — this pass shelved the two standards runtimes that decide it, `scorm-again` (MIT) and `tsugi` (Apache-2.0, LTI) |

## 🆕 `p465` · 2026-10-26 — **🟢 A TREND THIS BASE HAS NOT STATED, AND MEA IS THE PROOF: mandate intensity and open-supply depth are INVERSELY related. The region with the world's most aggressive curriculum mandate (UAE, AI from kindergarten) has the emptiest open layer this base has ever measured (African education ★ ceiling = 12). 🔴 And a methodological trend that now outweighs the market ones: this base's own measuring instruments are failing more often than its sources are.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes; nothing
below is gate-attested.

### 🟢 `T1` — Mandate intensity and open supply are inversely related

🔵 Placed side by side for the first time this pass:

| region | mandate depth | open-supply depth (first-hand ★ ceiling) |
|---|---|---|
| **MEA** (within EMEA) | 🟢 **highest** — UAE AI compulsory KG–G12, standalone subject 2026-27 | 🔴 **lowest** — 12 (Africa), 6 (Arabic) |
| **APAC** | 🟢 high — China from age 6; India from Class 3 (2026-27) | 🟡 moderate — Chinese-language marking and tutoring supply exists, mostly copyleft |
| **EMEA (EU-27)** | 🟡 restraint-shaped — prohibition live, high-risk deferred to 2027-12-02 | 🟢 deepest — the AGPL/GPL LMS estate plus post-Omnibus compliance tooling |
| **North America** | 🔴 no federal mandate; state guidance + district-policy duties | 🟢 deep but commercial-leaning |
| **LATAM** | 🔴 lowest — Peru only enacted law; Brazil pending | 🔴 **novelty nil for two passes** |

🟢 **Why it matters commercially:** a mandate creates obligation without creating components. The
regions that *must* teach AI are the regions with least to build on — so MEA and LATAM engagements
are **import-and-localise**, while EU-27 engagements are **compose-and-comply**. Those are
different service lines, not different clients.

### 🔴 `T2` — Instrument failure now outruns source failure on this base

🔵 Count this pass: **one** novel market fact from the prescribed web channel, against **four**
distinct instrument defects found and published — this pass's own newline-stripping bug
(`Gap 465-A` nearly published a phantom byte-variant), the two-convention payload-size
inconsistency between `p455` and `p464`, a `LICENSE` that states intent rather than granting
(`Gap 465-E`), and a template detector blind to same-owner batches (`Gap 465-B`). 🔴 **The base is
now learning more per pass about its own measuring apparatus than about education markets.** 🟢
That is not a failure — it is what saturation looks like from the inside, and it is the signal to
move the hour elsewhere (see the rotation note below).

### 🟢 `T3` — "Permissive" and "adopted" have separated in the assessment tier

🔵 Measured first-hand across `topic:grading topic:ai` (32 repositories): everything with adoption
is copyleft (GPL-3.0 at 104★, AGPL-3.0 at 39★), everything permissive is pre-adoption (3★, 0★).
🔴 So in marking and feedback — the highest-demand education-AI function in every region on
[`intel/market.md`](market.md) — **there is no permissive, proven option.** 🟢 The trend to watch is
whether the permissive tier (`markwise`, `AutoGrader-Agent`) accretes stars, because that is the
leading indicator for whether assessment work stops being a copyleft decision.

### 🟢 `T4` — Deterministic-first is becoming the design norm in graded AI

🔵 Both permissive marking rows added this pass do the same structural thing without sharing code
or authors: **they keep the model out of the parts that must be defensible.**
`omerfarooq223/AutoGrader-Agent` does *all* arithmetic in Python (totals, deductions, capping) and
resolves student identity from a roster before ever parsing content;
`erlan775959-code/markwise` **verifies in code that every quoted piece of evidence actually occurs
in the student's work** and flags invented evidence, plus attempts to manipulate the grader. 🟢
Convergent design from unrelated authors is a trend rather than a coincidence, and it is the
pattern a high-stakes education client can actually pass an audit with.

### 🟡 `T5` — Privacy tooling is arriving client-side, ahead of policy

🔵 `oas114/EduShield` (MIT, Taiwan) masks student data **in the browser before it reaches a hosted
model** and restores it after — and its own README declines to claim legal compliance. 🔵 This is
the first permissive component on this base that answers North America's procurement-clause turn
(Alabama's data-usage restriction, California's A.B. 1159) even though it was written for a
different jurisdiction's statute. 🟢 **Jurisdiction-portable privacy plumbing is the trend**; the
policy citations are local, the mechanism is not.

### 🔴 `T6` — The rotation itself is the largest finding on this base, and it is unchanged

🔴 `p459` measured that **10 of 12 industry KBs had no commit since 2026-08-01** while education
took **458 passes** in the same window, and wrote *"This pass advances the rotation."* 🔴 **It did
not persist.** Read first-hand this hour, `globant-kb/rotation.json` still carries
`{"next": 8, "last_updated": "2026-08-02", "last_industry": "technology"}` — **index 8 for 85
days.** 🔵 The likely mechanism, named so it can be fixed rather than re-attempted: passes edit the
rotation inside a working copy whose push to `globant-kb` does not land on the branch the scheduler
reads. 🟢 This pass advances it **and reports the branch it landed on**, so the next operator can
verify rather than assume.


## 🆕 `p464` · 2026-10-26 — **🔴 "Regulation diverged by region" (`p463`) is TRUE BUT TOO COARSE: it also diverged by DUTY TYPE inside a single region, and EMEA is the proof — a live prohibition since 2025-02-02 sitting under a high-risk regime deferred to 2027-12-02. 🟢 And a trend this base has not stated: in 2026 education-AI law became a DEMAND GENERATOR, not only a constraint — three of this hour's four regional instruments oblige institutions to adopt, promote or govern AI rather than to restrict it.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED, and so was every
individual gate.** The harness permission classifier refused both `make hooks` and a direct
`python3` invocation of the repo's own gate scripts (`Code from External`) — **eleven denials in
twelve passes, and one step stricter than `p463`**, which was still permitted to run
`p277-table-structure` and `p383-region-heading-gate` by hand. 🔵 **Nothing below is
gate-attested.** Mitigation, re-implemented in this session's own code rather than the repo's:
frontmatter keys and closed-vocabulary `region` checked on all eight shelves; every new table
checked for separator presence, pipe-count consistency and **no header row published as data**;
append-only proved on both trending shelves by prior-section containment; **every address
introduced this pass re-resolved by `git ls-remote`.**

🔵 **Instrument.** Two first-hand channels, as `p450` and `p463` established:
`git ls-remote <addr> HEAD` (**tree identity**) and
`raw.githubusercontent.com/<addr>/<branch>/LICENSE` (**payload bytes** → size + `sha256₁₂`).
🔴 **The `curl -sI https://github.com/<addr>` probe the ingest brief prescribes is reproduced
unusable, now from a fourth independent direction:** it returns `403` for a live address and for
a nonexistent one *alike* — `openedx/edx-platform` and `gmilano/this-does-not-exist-xyz123` are
indistinguishable through it. No row here rests on it.

🔴 **A channel measurement that is new this pass, and a future pass will misread it if it is not
written down: the GitHub *search* API is not reachable from the `gh` CLI here.**
`gh api "search/repositories?q=..."` returns **`403 — "sessions are bound to their configured
repositories. Use repository-scoped endpoints"`**. Repository search survives **only** through
the MCP `search_repositories` tool; `gh` reaches only the two attached repos. 🔵 A pass that
reaches for `gh` to discover supply will read that `403` as *no results* and publish a nil that
is an artifact of the channel — the exact error class `p463` caught on the web legs.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p463` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

### 🔴 `T1` — The divergence is two-dimensional, and the second axis changes what you sell

🔵 `p462` and `p463` established the regional axis: **Hanoi has a live duty, Frankfurt has 13
months.** 🟢 That holds. 🔴 **What it misses is that a single jurisdiction now carries duties with
opposite clocks:**

| region | live **now** | deferred | consequence for a proposal |
|---|---|---|---|
| 🔴 **EMEA** | **Art. 5(1)(f)** — emotion/attention inference in education **prohibited since 2025-02-02**, to **€35 M / 7 %** | Annex III high-risk (admissions, evaluation, exam scoring) → **2027-12-02** | 🔴 **You cannot tell an EMEA client "we have a runway".** One feature class must be declined today; the rest has 13 months |
| 🔴 **APAC** | Vietnam (2026-03-01, education named), Korea (2026-01-22), China | — | duty-first: classify before deploying |
| 🟡 **NA** | **Ohio** policy duty **expired 2026-07-01**; state human-oversight statutes | federal bill in committee | the artefact is a *policy that exists and is implementable* |
| 🟢 **LATAM** | 🔴 nothing national in force; Brazil parked behind the Oct-2026 elections | — | governance is the product, not the obstacle |

🟢 **The sellable form of `T1`:** a multi-region programme needs a **per-feature** compliance
matrix, not a per-region one. The same attention-analytics module is *prohibited* in the EU,
*high-risk and self-classified* in Vietnam, and *unregulated* in Brazil.

### 🟢 `T2` — NEW: education-AI law turned into a demand generator

🔵 Every regulatory trend this file has carried reads law as a **constraint**. 🟢 **Three of the
four instruments this pass promoted are obligations to *do* something:**

| instrument | duty | what an institution must now buy |
|---|---|---|
| 🟢 **India** — AI + Computational Thinking from **Class 3**, 2026-27 session | introduce a curriculum across all schools | curriculum content, **teacher training at national scale** (NISHTHA), handbooks, assessment |
| 🟢 **Ohio Rev. Code 3301.24** | **adopt an AI policy** by 2026-07-01 | policy drafting, tool-approval process, governance role, staff training |
| 🟡 **Estado de México, Art. 61** | **promote** responsible, ethical and gradual AI use (upper-secondary and higher) | teacher capability, institutional policy, access provisioning |
| 🔴 **EU Art. 5(1)(f)** | **do not** infer emotions | 🔴 the one pure prohibition in the set |

🔴 **Why this is a trend and not four facts.** The 2026 instruments that name education most
explicitly are **adoption mandates**, and an adoption mandate with a date is a procurement
pipeline: it obliges thousands of institutions to produce an artefact they do not have the
capability to produce. 🟢 **For Globant that inverts the sales motion** — the entry point in NA,
India and Edomex is **capability and governance delivery** (policy, training, tool-approval
workflow), not a model or a tutor. 🔵 It is also the only category of education-AI demand on this
file that is **immune to the efficacy-evidence blocker** below, because the buyer's success
criterion is *the policy exists and is defensible*, not *learning improved*.

### 🟡 `T3` — The efficacy gap holds, but its ADJACENT category started shipping

🔴 **Sixth consecutive pass with zero evaluation harnesses in the discovery slice** (0 of 12 this
pass; `p463` found 1 of 13 and it was *recovered*, not discovered). Buyers in every region ask for
proof of learning gain and the open-source supply still cannot answer.

🟢 **What did arrive is one step to the side of it, and both rows are new this pass:**

| row | what it measures | why it is not an efficacy harness |
|---|---|---|
| [`junichikatsu/SocraMetry`](https://github.com/junichikatsu/SocraMetry) (MIT) | **attainment, accuracy and growth rate on 5 axes**, explicitly designed as objective evidence for **HR evaluation** | 🔵 measures an individual's trajectory for a personnel decision; no cohort, no control, no learning-gain claim |
| [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) (MIT) | whether a cited quotation **exists in the source** | 🔵 audits *provenance*, not *learning* |

🟢 **The pattern across the two:** the supply is learning to produce **auditable evidence about an
answer or a trajectory** — which is what Vietnam's automated-assessment rule, Annex III's
oversight duty and NA's "sole basis" clauses actually ask for — **before** it learns to produce
evidence of pedagogical effect. 🔵 Provenance and defensibility are arriving first because
regulation asks for them; efficacy is not arriving because nothing compels it.

### 🟢 `T4` — The packaging shift is reproduced by an independent operator

🔵 `p463`: **7 of 13** novel addresses shipped as an **agent skill** rather than an application.
🟢 This pass, different slice, same channel: of **12** novel addresses, **3** are skills or harness
plugins, **5** are desktop applications, **2** platforms, **1** substrate, **0** evaluation.
🔴 The notable number is the **1 of 12 substrate** — detailed on
[`repos/foundations.md`](../repos/foundations.md) `p464`. 🟢 **Both passes agree on the direction:
education AI is being packaged as something that plugs into a harness the user already runs**, and
the recency channel sees the application tier far better than the substrate tier.

### 🔴 `T5` — Education AI has no star-ranked surface, and that is now measured

🔵 A platform-named query (`moodle OR canvas OR openedx MCP`) returned **4 428** repositories with
**0 education projects in the top 25 by stars**; the leaders are agent infrastructure at
**77 913★**, **27 813★** and **16 796★**. 🟢 **Education AI's entire shelf on this base is
outweighed by a single token-compression library.** 🔴 The consequence is methodological and it is
the reason this base's discovery works at all: **sorting by stars discards the sector**, so
discovery must be bounded by **recency**, where the agent-infra giants are not present.

### 🔴 `T6` — The recency channel carries template-clone pollution, and one clone wore a region label

🔵 Two of this pass's five ungranted rows share an **identical 14-string topic set**, near-identical
descriptions, 0 forks each, `fork: false` on both and star counts one apart. 🔴 One of them
advertises **"Spanish"** Math Olympiad content — and a pass hunting LATAM supply, which
`intel/market.md` has hunted for five passes, would have shelved it as a LATAM find.
🟢 **The trend statement:** as the recency channel becomes the primary discovery instrument, its
failure mode stops being *too few results* and becomes *synthetic results that pass a star floor*.
Topic-set identity is the cheap detector and this base collects topics without comparing them
(`Gap 464-B`).

## 🆕 `p463` · 2026-10-26 — **🟢 The trend legs reproduce `p462`'s governed-deployment shape and add one it could not see, because it is visible only in the SHAPE of the supply: 13 of 17 novel addresses were created within five months and 7 of 13 ship as an agent SKILL rather than an application — the packaging format of education AI changed this year. 🔴 And "regulation is tightening" is no longer one trend: in 2026 it DIVERGED by region.**

### 🟢 The trend legs reproduce `p462`'s shape and add one thing it could not see

🟢 **Reproduced, from the same standards body and analyst sources `p462` read:** 2026 is the year
education AI moved from pilots to **governed deployment**; governance is the gate; buyers demand
**evidence** of learning gain; education-specific tools are displacing general chatbots; agents
are displacing single prompts; digital credentials are the skills-economy mechanism. 🔵 None of
that changed in a day and this pass does not restate it as new.

🔴 **The adoption percentages those legs carry are refused again** — an "83 % of institutions"
figure and a "60 % of U.S. K-12 teachers" figure arrive from aggregators whose own numbers
conflict by large factors. 🟢 **One exception, promoted:** the U.S. teacher figure (**60 %** in
2024-25, **32 %** weekly) traces to a survey with a stated population, so it is promoted on
`intel/market.md` and the aggregator restatements around it are not.

### 🔴 The trend `p462` could not see, because it is visible only in the SHAPE of the supply

🔵 This pass ran the discovery channel on a **recency** slice for the first time
(`created:>2026-06-01`). What came back is a trend statement in its own right:

| what the slice shows | n | reading |
|---|---|---|
| 🟢 novel addresses created within ~5 months | **13 of 17** | the education supply is being written **now**, faster than an hourly shelf samples it |
| 🟢 shipped as an **agent skill**, not an application | **7 of 13** | 🔴 **the packaging format of education AI changed this year** — a `SKILL.md` + prompts repository, installable into a coding agent, has replaced the web app as the default unit of distribution |
| 🟢 APAC-placed on first-hand evidence | **9 of 12** shelved rows | the centre of gravity of new open education tooling is APAC, and it is not close |
| 🔴 carrying an efficacy-evaluation harness | **1** | the evidence trend above has **no supply behind it** |
| 🔴 LATAM-placed and shippable | **0** | see the LATAM gap: supply exists, 6 of 6 ungranted |

🟢 **Why the packaging shift is the actionable half.** A skill is a text artefact with a declared
licence and no runtime: it composes, it reviews cleanly, and it can be vendored into an
engagement in an afternoon. 🔴 It also carries a **new provenance risk this pass met first-hand** —
[`Aisland-SJL/Aisland-teach`](https://github.com/Aisland-SJL/Aisland-teach) is MIT and **declares
derivation from another MIT skill in its README**. 🟢 That chain is stated, so it grades clean;
nothing guarantees the next one states it. **Skill-tier supply needs provenance read at the
README, not just a grant read at `LICENSE`** — `p288`'s README channel, now load-bearing for a
whole tier rather than an exception. Registered as `Gap 463-E`.

### 🔴 The regulatory trend, and it is a DIVERGENCE rather than a direction

🟢 Every prior pass recorded "regulation is tightening". 🔴 **That is no longer one trend.** In
2026 the education-AI compliance calendar **split**: EMEA **postponed** its Annex III education
duty to **2027-12-02** (Digital Omnibus, Regulation (EU) 2026/1744) while **Vietnam** brought an
explicitly education-naming high-risk regime into force (**2026-03-01**, six sectors incl.
education, automated assessment and behavioural monitoring named), **South Korea** commenced its
AI Basic Act (**2026-01-22**, one-year penalty grace), and **China** holds registration and
labelling duties with penalties to **¥50 M**. 🔵 **Consequence for a multi-region studio
programme: one compliance posture no longer spans two regions.** Full table and the citation
posture per instrument: [`intel/market.md`](market.md) `p463`.

### 🟢 A trend about this base's own behaviour, which is a trend about mature KBs generally

🔴 Four consecutive passes published *zero novel yield* and concluded the supply was saturated.
🟢 **It was not: one date bound returned 13 unshelved addresses, 11 of them granted.** And in the
same hour, diffing a nine-pass-old evidence file against the shelves recovered **10 live
permissive addresses that had been silently evicted** — for no network calls at all.
🔵 **The generalisable finding: at high maturity a knowledge base's scarcest resource stops being
discovery and becomes RETENTION.** It is cheaper, and more productive, to measure what left than
to search again for what never arrived. Mechanism, denominators and the eviction audit:
[`agents/top.md`](../agents/top.md) `p463`. Recipe: `Pattern AW`.

### 🔵 Gap register opened by this pass

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 463-A`** | The sell shelves have **no eviction ledger**. 21 projects left every sell shelf between `p406` and `p462` with no row, no reason and no gate; every existing gate measures arrival. | Write `evidence/evictions.<date>-p<N>.tsv` from the `Pattern AW` diff, and add a gate that fails when an address on the previous commit's sell shelves is absent from this one **without a reason cell**. |
| 🔴 **`Gap 463-B`** | A novelty check keyed on a **guessed slug** manufactures false positives — `openSIS` read as uncarried when `OS4ED/openSIS-Classic` sits on 3 shelves. | Resolve the product name to an address through the probe **before** the `grep`, and key the check on the resolved address. |
| 🟡 **`Gap 463-C`** | `OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` share HEAD `8348cd069aa2`. Alias or undiverged fork is **unsettled**, and neither serves a root grant so the payload channel cannot settle it. | Run `gate-fork-direction`'s full-history channel on the pair. |
| 🔴 **`Gap 463-D`** | **The Middle East and Africa returned nothing on any EMEA leg** — EMEA's evidence here is EU-27 + UK + Germany only. | Run legs keyed on named national systems (as `p443` did for LATAM) rather than on the region word: Gulf ministry platforms, Nigerian and Kenyan HE systems, francophone African curricula. |
| 🟡 **`Gap 463-E`** | Skill-tier supply (**7 of 13** novel addresses) carries **derivation chains stated only in the README**. A `LICENSE` read grades such a row clean while saying nothing about what it was built from. | Make `p288`'s README channel standing for the skill tier: every skill-tier row records a provenance cell (declared upstream + its grant) or `PROVENANCE-UNSTATED`. |
| 🔴 **`Gap 446-A`** | **Still open, and still not closable by this pass.** `make hooks` was refused (`Code from External`); nothing in this pass is gate-attested. | Needs a harness permission decision, not a pass. |

## 🆕 `p462` · 2026-10-26 — **The trend legs return one consistent, well-sourced signal and it is not a technology: 2026 is the year education AI moved from pilots to GOVERNED deployment, and the binding constraint is evidence and oversight, not model capability. 🔴 `p461`'s alias trend-note is CORRECTED — one of its four cases is a fork pair, not a rename.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN, and the reason is new.**
This pass is executing under a harness whose permission classifier **refused the `make hooks`
invocation outright** (`Code from External`) — not a proxy failure, not a missing target, a refusal
to execute the repository's own Makefile. So **nothing below is gate-attested**, and the gate's
inability to run is itself the standing obstacle: `Gap 446-A` cannot be closed by a pass that is
not permitted to run the gate.

### 🟢 The trend the prescribed leg actually supports, stated once

🟢 Across every source the `AI education industry trends 2026` leg returned — a standards body, two
analyst notes and four vendor blogs — the agreement is on **shape, not product**:

1. 🟢 **Pilots → infrastructure.** AI is being embedded into admissions, advising, learning and
   administration as ordinary workflow, rather than run as standalone pilots.
2. 🟢 **Governance is the gate.** The standards-body source frames 2026 as the shift *from
   experimentation to governance* — policies, data boundaries and oversight as the precondition for
   adoption. This is the same conclusion these shelves reached from the supply side.
3. 🟢 **Evidence is being demanded.** Buyers increasingly require proof that a product improves
   learning, persistence, well-being or job-relevant skills. 🔴 **This is the trend with the most
   direct consequence for an open-source shelf:** none of the agent-tier repositories these shelves
   carry ships an efficacy evaluation harness.
4. 🟡 **Education-specific over general chatbots**, and **agents over single prompts** — multi-step
   task execution rather than one-shot generation.
5. 🟡 **Digital credentials** as a mechanism for skills-based learning and hiring.

🔴 **Every adoption percentage these sources quote is refused, not shelved.** The leg returned an
"83 % AI teaching-assistant deployment" figure and a "60 % of U.S. K-12 teachers" figure from
aggregator pages whose own numbers conflict with each other by large factors. Per `Gap 455-E` they
are relayed, and this pass does not promote them.

### 🔴 The correction to `p461`'s alias note on this file

`p461` recorded on this file that four carried addresses resolve by redirect to different canonical
names. 🔴 **That is right for two of them and wrong for the other two.**

### 🟢 Identity graded by HEAD sha — the channel `p461` did not have

`git ls-remote <addr> HEAD` works from this host and returns the commit the address resolves to.
Two addresses that return the **same sha** are the same repository; two that return **different
shas** are two repositories, whatever their licence payloads look like.

| address pair | raw `LICENSE` payload | HEAD sha, alias | HEAD sha, canonical | verdict |
|---|---|---|---|---|
| `openedx/edx-platform` → `openedx/openedx-platform` | identical · 35 136 B · `e12d78569742` | `addd09d7801b` | `addd09d7801b` | 🟢 **same repository** — rename alias, and it still resolves |
| `Vacademy-io/vacademy_platform` → `Vacademy-io/vacademy_edtech_platform` | identical · 34 523 B · `0d96a4ff68ad` | `3a9c66db938c` | `3a9c66db938c` | 🟢 **same repository** — rename alias, and it still resolves |
| `DaRL-GenAI/instructional_agents` vs `Hyan-Yao/instructional_agents` | identical · 1 067 B · `4e085d826a64` | `f835eb45f508` | `1c2a9f9e3d26` | 🔴 **NOT the same repository** — two live, divergent HEADs |
| `OpenEduCat-Inc/OpenEduCat` → `openeducat/openeducat_erp` | alias **404** at `19.0`, `master` and `main`; canonical **200** · 8 241 B · `528f840368` | 🔴 unresolvable — `ls-remote` falls through to a credential prompt | `46a5d7d40082` | 🔴 **alias is ABSENT**, not a redirect |

### 🔴 The rule this establishes, and it is reusable

🔴 **A byte-identical licence payload is near-zero evidence of repository identity, and for the
boilerplate grant families it is no evidence at all.** `p461` read an identical 1 067 B MIT text at
`DaRL-GenAI/instructional_agents` and `Hyan-Yao/instructional_agents` and concluded one was the
other's stale alias. The HEAD shas say otherwise: `f835eb45f508` ≠ `1c2a9f9e3d26`, two live
repositories with independent histories. The payloads match **because stock MIT text is
universal** — the same 1 067 B body appears on dozens of unrelated rows on these very shelves.
Identity is a property of the **tree**, and only the sha channel reads the tree.

🟢 The trend-level lesson is the one worth carrying forward: **as projects rename, re-org and fork,
an address is not a stable identifier for a repository.** A shelf that cites addresses needs a tree
identity channel, and `git ls-remote` is it.

## 🆕 `p461` — **Five trends, and the load-bearing one is structural rather than technical: the permissive share of this field is small, shrinking at the top, and systematically misreported by the tooling everyone uses to check it.**

🔴 **Gate posture per `Gap 446-A`: `make hooks` was NOT RUN.** Nothing below is gate-attested.

### 🔴 T1 — The field's most-starred assets are the least usable

🔵 Rank education repositories by ★ and grant quality moves the **opposite** way:

| rank by ★ | repo | ★ exact | grant | usable by Globant? |
|---|---|---|---|---|
| 1 | `HKUDS/DeepTutor` | **43 537** | Apache-2.0 | 🟢 **yes** |
| 2 | `JushBJJ/Mr.-Ranedeer-AI-Tutor` | **29 548** | **NO GRANT** | 🔴 **no** |
| 3 | `DreambigOu/ELI5` | **1 854** | MIT | 🟢 yes |
| 4 | `HugeCatLab/ChatTutor` | **1 314** | AGPL-3.0 | 🟡 network copyleft |
| 5 | `Miaotofu01/Study-Mate` | **1 218** | MIT | 🟢 yes |
| 6 | `pguso/agents-from-scratch` | **1 062** | MIT | 🟢 yes |
| 7 | `ECNU-ICALK/EduChat` | **975** | **NO GRANT** | 🔴 **no** |
| 8 | `DozenTwelve/Papermorph` | **949** | MIT | 🟢 yes |
| 9 | `GarethManning/education-agent-skills` | **913** | **CC-BY-SA-4.0** | 🟡 share-alike |

🔴 **Two of the top nine serve no grant at all, and two more are copyleft.** The #2 asset in the
entire field — 29 548★ — cannot be vendored. 🟢 Trend direction: the permissive core is *narrower*
than the star distribution suggests, and a studio that picks by popularity picks wrong.

### 🔴 T2 — `NOASSERTION` is the field's most dangerous metadata state

🔵 Established this pass (`Gap 461-B`): the index's **absent** licence field meant genuinely no
grant in **4 of 4** probes, but **`NOASSERTION` meant a real, nameable grant in 3 of 3** — and
**two of those three were copyleft** (AGPL-3.0, CC-BY-SA-4.0). 🔴 So the single state that looks
most like "unknown, skip it" is the state most likely to hide an obligation. Any pipeline that
treats index metadata as authoritative will both discard usable LGPL work and silently admit
share-alike material.

### 🔴 T3 — Shelf addresses decay by rename, and the standard verification method cannot see it

🔵 Four carried addresses are aliases (`Gap 461-A`). A `raw.githubusercontent.com` byte-read —
the most rigorous check these passes have used — returns **identical bytes and digests** at the
alias and the canonical name. 🟡 One of the four (`OpenEduCat-Inc/OpenEduCat`) has **already
stopped answering**, which converts this from theory to observed decay. 🟢 Trend: licence
verification and *identity* verification are different problems, and only the first has been
solved here.

### 🟢 T4 — Agent-skill packaging has displaced the standalone tutoring app

🔵 The newest high-★ education repositories are not applications but **skills and plugins** for
existing agent harnesses: `assafkip/claudemy` (**458**★, created 2026-10-14),
`DozenTwelve/Papermorph` (**949**★), `ZeKaiNie/universal-examprep-skill` (**318**★),
`SenmuuuuW/universal-diagnostic-tutor-skill` (**250**★), `liuliu667/cram-engine` (**176**★),
`flysheep-ai/education-skills` (**118**★), `GarethManning/education-agent-skills` (**913**★).
🟢 Commercially this is good news: skills are **small, MIT-dominated and composable**, so the
integration cost is low and the licence posture is usually clean — the opposite of the platform
tier, which is uniformly copyleft.

### 🟢 T5 — Local-first and self-hosted is now the default posture, and regulation is why

🔵 `zijinz456/OpenTutor` (**152**★, 10+ LLM providers, local), `artcc/freelingo` (**208**★,
Ollama), `nichochar/ari` (**208**★, local-first), `Fazmin/AILearningGuide` (**233**★,
offline-first), `sitor-ai/frametell` (**407**★, local-first), `pguso/agents-from-scratch`
(**1 062**★, local LLM, no cloud APIs). 🟢 This lines up exactly with the regional constraints in
`intel/market.md`: North American student-data residency rules and EMEA's deployer duties both
push toward self-hosted inference. **Local-first is a compliance feature, not a preference.**

### 🟡 Declared gaps — stated so silence is not mistaken for coverage

1. 🔴 **No LATAM-originated open-source education-AI agent repo ≥50★** surfaced in Spanish- or
   Portuguese-language index queries this pass. See `intel/market.md` → LATAM.
2. 🔴 **No dominant open-source tutoring-evaluation or learning-gain observability project.**
   `DAMO-NLP-SG/M3Exam` (**105**★) benchmarks model knowledge, not pedagogical effect. The field
   measures models, not learning.
3. 🟡 **Moodle's AI plugin tier is thin** — the two verifiable plugins are **17★** and **15★**
   against a **7 543★** core; `qbank_genai` and `block_ai_chat` did not resolve to repositories.

---
## 🆕 `p460` · 2026-10-26 — **🟢 THE TREND `p458` AND `p459` DIAGNOSED IS CLOSED BY ACTION RATHER THAN RESTATED: the frozen rotation pointer was located, its freeze mechanism read out of its own status field, and it has been ADVANCED — education → automotive. 🔴 And the sector trend this pass can evidence is that saturation is a property of the CHANNEL DEPTH, not of the sector: two unrelated instruments return 0 % usable in the same hour.**

🔴 **`make hooks` was NOT RUN** — fresh clone, not the Makefile, so nothing below is gate-attested.

### 🟢 Trend 1 — the pipeline limit is fixed, not just named

🔵 `p459` recorded: *"education research has saturated at the prescribed depth, and the cause is a
frozen rotation that has starved ten of the twelve industry shelves for 86 days."* 🔴 Three passes
named it; none could reach it, because the pointer does not live in this repository.

🟢 **Located and read first-hand** — `rotation.json` in `gmilano/globant-kb`:

| field | value as found | reading |
|---|---|---|
| `next` | **8** | index 8 = `education` — every pass since has re-selected this shelf |
| `last_industry` | `technology` | index 7, the pass that last wrote the file |
| `last_updated` | **2026-08-02** | **85 days before this pass** |
| `last_status` (tail) | *"…technology-kb-push-BLOCKED-access-restriction(session-scoped-to-globant-kb-only)"* | 🔴 **the freeze mechanism, in the file's own words** |

🔵 **The mechanism, stated as a mechanism and not a guess:** the pointer is advanced *after* the
industry KB is pushed. The `technology` pass could not push `technology-kb` — the repo was not
attached to its session — so it recorded the block and **never reached the advance step**. 🔴 The
pointer has read `8` ever since. 🟡 What this pass can measure but not explain: the education
shelves advanced **459 passes** across the same 85 days, so shelf activity and the rotation pointer
are **decoupled** — something advanced the shelves without ever advancing the pointer.

🟢 **Acted on:** `education-kb` was attached to this session and pushed successfully, the step that
was blocked in August, and `rotation.json` is advanced to **`next: 9` (`automotive`)**. 🔵 The
falsifiable prediction this leaves: **the next scheduled pass should open `automotive`, not
`education`.** If a `p461` appears on this shelf, the pointer is not what selects the industry and
this trend is refuted.

### 🔴 Trend 2 — saturation is a channel-depth property, measured twice by unrelated means

| pass | instrument | probed | unshelved | granted & usable |
|---|---|---|---|---|
| `p458` | GitHub repo-search API | 62 | 26 — **41.9 %** | rows added |
| `p459` | GitHub repo-search API, 3 legs | 42 | 2 — 4.8 % | **0 — 0 %** |
| 🆕 `p460` | web search + topic-page enumeration + payload byte-reads | **34** | **1 — 2.9 %** | **0 — 0 %** |

🟢 **The claim this licenses:** the 0 % is not an artefact of the search API, because a channel with
no shared code path returns it too. 🔴 **The claim it does NOT license:** that education has no
remaining permissive supply. `p458` found 26 unshelved addresses one pass earlier on the *same*
channel that returned 4.8 % the next. 🔵 Per `p456`'s own standing rule — *"a search channel's nil
and non-nil one pass apart are variance, not change"* — what is saturated is **this vocabulary at
this depth**, and the remedy is the rotation above, not a deeper education leg.

### 🟡 Trend 3 — the EMEA supply shape gains instrument names, and they confirm the shelf

🔵 These shelves already state that EMEA-origin supply is *sovereign models and regulation, not
education agents* (naming Digital Europe Programme, Teuken-7B, Apertus, SOOFI). 🟢 Four tokens new
to this base **reinforce that finding rather than change it**: **OpenEuroLLM** (€**37.4 M**, first
formal model release targeted end-2026, final models 2028); the EU frontier-model programme
**EUROPA**, consortium led by **Domyn**, selected **2026-06-19**, >400 B parameters across 24 EU
languages; and 🔴 the one EU instrument that *was* education-specific — the Digital Europe
**EdTech Accelerator** — whose deadline **2026-10-01 has passed**. 🔵 Published as instrument names
per `Gap 455-E`, because this base can only ever relay demand-side figures: a reader who can reach
a primary can check what this host cannot.

## 🆕 `p459` · 2026-10-26 — **One trend, and it is about this base rather than the sector: education research has saturated at the prescribed depth, and the cause is a frozen rotation that has starved ten of the twelve industry shelves for 86 days.**

### 🔴 Trend — the limiting factor has moved from the sector to the pipeline

🔵 Measured, not asserted. Three independent measurements taken in the same hour:

**1 — the supply channel collapsed, and not because it broke.**

| pass | addresses probed | unshelved | novel share | granted & usable |
|---|---|---|---|---|
| `p458` | 62 | 26 | 41.9 % | several |
| 🔴 `p459` | 42 | 2 | **4.8 %** | 🔴 **0** |

🟢 The probe was controlled in both directions this pass (positive `HKUDS/DeepTutor` Apache-2.0
11 408 B reproduced; negative two fabricated addresses `ADDRESS_DEAD`), so this is a shelf result,
not an instrument result.

**2 — the demand channel is a seventh consecutive nil.** Eight prescribed legs, 19 named facts,
19 already on [`market.md`](market.md). Denominator published there, leg by leg.

**3 — the rotation is frozen, and this is the actual cause.** Every industry KB probed first-hand:

| industry KB | last commit | days stale |
|---|---|---|
| 🟢 `education-kb` | 2026-10-26 | **0** — and **458 passes** deep |
| 🟢 `automotive-kb` | 2026-10-26 | 0 |
| 🔴 `gaming-kb` | 2026-08-01 | **86** |
| 🔴 `legal-kb` | 2026-08-01 | **86** |
| 🔴 `financial-kb` | 2026-08-01 | **86** |
| 🔴 `healthcare-kb` | 2026-08-01 | **86** |
| 🔴 `media-kb` | 2026-08-01 | **86** |
| 🔴 `retail-kb` | 2026-08-01 | **86** |
| 🔴 `travel-kb` | 2026-08-01 | **86** |
| 🔴 `technology-kb` | 2026-08-01 | **86** |
| 🔴 `energy-kb` | 2026-08-01 | **86** |
| 🔴 `enterprise-kb` | 2026-08-01 | **86** |

🔵 `globant-kb/rotation.json` has read `{"next": 8}` — education — since **2026-08-02**, and its
`last_industry` is still `technology`. Every hourly pass since has re-selected education, updated
these shelves, and failed to advance the index. The 458 passes and the 86 days are the same fact
seen from two ends.

### 🟢 What follows for an engagement

🔵 These shelves are **not** short of education material — they carry it to a depth no engagement
will exhaust. 🔴 What a studio cannot currently do is open a *gaming*, *legal*, *financial*,
*healthcare*, *media*, *retail*, *travel*, *technology*, *energy* or *enterprise* engagement on
anything newer than **1 August 2026** — which, in a sector where the EU's high-risk schedule moved
in July 2026 and Korea's framework act commenced in January 2026, is old enough to be wrong rather
than merely thin.

🟢 **This pass advances the rotation to index 9 and pushes it**, per the encargo's step 5. If the
advance holds, the eleven starved shelves clear within twelve passes.

### 🔵 Carried forward, unchanged

The trends recorded at `p458` — verification moving out of the model, and the per-region
LMS-connector layer building against each region's dominant system — were re-probed this pass and
**both still hold**. No evidence was returned against either.

## 🆕 `p458` · 2026-10-26 — **Two trends this pass, and the measurable one is about where verification runs: it is moving OUT of the model. The other is that this base's own discovery instrument was wrong for 457 passes.**

### 🟢 Trend — the correctness check is leaving the LLM

🔵 Measured, not asserted: of the 26 unshelved education addresses this pass found, **the four
most defensible pieces of engineering all move the correctness check off the language model**, and
they do it in four unrelated subjects:

| address | what grades the output | what the LLM does instead |
|---|---|---|
| [`Hussain004/SAMOSA`](https://github.com/Hussain004/SAMOSA) | exact arithmetic over **finite fields** | proposes the derivation |
| [`lilong65190349/mcd-math-journey`](https://github.com/lilong65190349/mcd-math-journey) | a **third-party priced API** re-derives the answer key | writes the word problem |
| [`FredMichel/chalkcast`](https://github.com/FredMichel/chalkcast) | the animation is **rendered and visually inspected** | authors the Manim scene |
| [`m1kuorg/asked-before`](https://github.com/m1kuorg/asked-before) | the learner is tested **with the model removed** | mines the transcript for the question |

🟢 This is the supply side catching up with the demand side that this file already records: the
**OECD 2026** digital-education finding that chatbot gains disappeared — and sometimes reversed —
in exams once access was withdrawn, and **1EdTech**'s read that the sector has moved from
experimentation to governance. 🔵 A tutoring system whose grader is the same model as its tutor
cannot answer either objection. These four can. 🟢 **For an engagement: this is now a design
requirement to put in the proposal, not a differentiator to discover later.**

🟡 Denominator, so this is not over-read: four addresses out of 26, in one week, on one channel.
It is a direction with evidence, not a measured market share.

### 🔴 Trend — in this base's own instruments, and it is the expensive kind

🔵 The GitHub repository-search API was recorded by `p450` as *"github-api-proxy-blocked"*. 🔴 **It
is open from this host, and this pass used it to return 62 education candidates of which 26
(41.9 %) were unshelved — in the same hour that the prescribed web-search channel returned 19
facts and ZERO novel ones, its sixth consecutive nil.** 🟢 The lesson generalises past this base:
**a channel recorded as blocked is a claim with a date on it, and it decays.** Five passes
reported nils and attributed them to a saturated subject; the subject was not saturated, the
channel was.

### 🔴 And the trend that is not about education at all

🔵 Stated here because it explains the shape of this entire base and no file records it: **the
rotation that is supposed to move this curator across twelve industries each hour has not
advanced since 2026-08-02.** 🔴 `rotation.json` has read `{"next": 8}` for **85 days**, which is why
this is **pass 458 of education** and why automotive, energy, enterprise, gaming, legal, financial,
healthcare, media, retail, travel and technology have had **no pass since early August**. 🟢 This
pass advances the rotation to index 9 (automotive). 🔵 The reader-facing consequence: **the depth
of this KB against the other eleven is an artefact of a stuck counter, not a judgement that
education matters 458 times more.**

---


## 🆕 `p457` — **🔴 THE TREND THIS PASS CAN EVIDENCE WITH A DATE IS LICENCE REVOCATION IN PLACE: three of 457 carried addresses re-issued their licence text inside one 48-hour window, and one of them moved from MIT to commercial while its shelf cell still said MIT. 🟢 And a structural trend with a nine-token denominator: this industry's dominant assessment instrument is paper, and the entire open-source vocabulary these shelves search in is digital.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes. 🔵 Nothing
below is gate-attested; instrument and controls at
[`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py).

### 🔴 `T1` — An address is not a licence, and the licence can change under a stable address

🟢 **Measured, with dates:** of 457 addresses carried on the primary shelves, **three served licence
text re-issued on 2026-10-24**, two days before this pass:

| address | instrument now served | effective |
|---|---|---|
| `pengusto/google-classroom-mcp` | 🔴 `Pengusto Commercial License 1.0` | **2026-10-24** |
| `nakafaai/aksara` | 🔴 `Nakafa Source Available License 2.0` | **2026-10-24** |
| `nakafaai/nakafa.com` | 🔴 `Nakafa Source Available License 2.0` | **2026-10-24** |

🔵 Every prior trend on this file about licences has been about **reading** them correctly — badges
that lie, pointers that are not grants, manifests that disagree with payloads. 🔴 **This one is
different in kind: the grant was read correctly and then changed.** The address did not move, the
project did not die, the stars did not fall. A shelf cell built from a correct first-hand read in
`p4xx` was wrong by `p457` without anything observable from outside the payload.

🟢 **The trend, stated for an engagement:** *in agentic-education supply, the licence is a
**time-varying** property of an address, and the rate is now measured at least once — 3 of 457
addresses in a 48-hour window.* 🔴 **The consequence is a procurement practice, not a caveat**: a
dependency's grant is pinned to a **commit**, re-read at vendoring time, and the grant text is
copied into the vendor tree. 🔵 This base has no instrument that would *notice* the next one
(`Gap 457-C`) — all three were found by re-reading everything, which costs a full sweep.

### 🔴 `T2` — The relicensing shape is "fork, extend, charge for the extensions"

🔵 `pengusto` is worth reading closely because it is **not** a rug-pull and it is more awkward than
one. Its licence scopes itself to *"the copyrightable additions and modifications made by
Pengusto"*, names its upstream at a commit, and states that the upstream *"remains available under
MIT"* — preserving the upstream notice at `LICENSES/MIT-upstream.txt`.

🔴 **And the upstream serves no licence file at all** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
`LICENCE`, `COPYING`, `license` all **404** on
`adriasantacreu/google-classroom-mcp`; its only grant is a `package.json` field.

🟢 **So the trend is a dependency-graph fact:** the permissive layer became *less* readable than the
commercial layer built on top of it. 🔵 The only readable MIT text in that pair lives inside the
repository that charges. 🔴 **For Globant this is the pattern to expect in the MCP-connector tier
generally** — single-maintainer MIT servers, forked by a second party who adds the production
hardening and prices it — and the defence is to pin the upstream commit and vendor the grant text,
because the upstream has no incentive to publish one.

### 🟢 `T3` — The supply vocabulary is digital and the install base is paper

🟡 **A measured absence, with its denominator.** Before any web leg, nine tokens were searched
against the three primary shelves: **`OMR`, `optical mark recognition`, `bubble-sheet`, `mark
recognition`, `phoneme`, `braille`, `sign language`, `dyslexia`, `speech-to-text` — nine of nine at
ZERO mentions** across 457 carried addresses.

🔵 **The cause is not that the supply does not exist** — one leg in the new vocabulary returned four
permissively-licensed OMR engines and four assistive foundations, all live, all read first-hand
(see [`repos/foundations.md`](../repos/foundations.md)). 🔴 **The cause is that 456 passes of
discovery were phrased in the language of hosted digital education**: LMS, MCP, tutor, autograder,
LTI, xAPI. An exam office scanning NEET practice sheets on one offline Windows PC is not in that
vocabulary.

🟢 **The trend proper:** *the open-source education supply has a large, permissive, actively
maintained offline tier, and the channels that find agentic tooling do not return it.* 🔵 This is
`p453`'s finding — the word list is the variable, not the channel — **confirmed on a new axis**,
and it is the strongest argument on this file for budgeting discovery legs by vocabulary rather
than by region.

### 🟡 `T4` — Accessibility is statutory demand with permissive supply, and the two were never connected here

🔵 These shelves sell hardest into the two regions where accessible instruction is a **legal
obligation** — IDEA and Section 504 in the US, the European Accessibility Act in the EU — and
carried the word *"accessibility"* only as prose. 🟢 The supply is permissive and specific:
`NSoiffer/MathCAT` (**MIT**) emits **braille in Nemeth and UEB Technical** and speech in **15
languages** from MathML; `AVauraTech/assistive-ai-accessibility-suite` (**MIT**) runs eight
modalities **on-device via WASM with an offline fallback**.

🔴 **The commercial reading:** accessibility work is procured because it is *required*, not because
it is *wanted*, which makes it the rare education line item with a non-discretionary budget — and
the permissive supply to serve it has been sitting one vocabulary away from these shelves the whole
time. 🟡 Stated as an opportunity and not as a win: none of these four rows has an institutional
install base this pass could measure.

### 🔴 `T5` — Methodological: the regulatory channel is saturated, and this is the sixth consecutive nil

🔵 Eight legs ran this pass — four global, four regional, in the prescribed wording. **14 named
facts were returned and graded against [`intel/market.md`](../intel/market.md): 13 were already
carried.** Vietnam's Decision 33/2026/QD-TTg, Korea's AI Framework Act, California AB 1159,
H.R. 8747, the Digital Omnibus dates, Canada's *AI for All*, the DEC LATAM rates, UNESCO IESALC's
governance lag — all on the shelf already.

🟢 **That is a result about the channel, and it is now six passes old.** 🔴 **Where this pass paid
regionally was the SUPPLY side** — APAC gained two OMR rows placed by the national exam systems
their own READMEs name, North America gained one assistive row placed by device. 🔵 The trend for a
curator: **after saturation, a region is moved by a supply row, not by a regulation leg.**


## 🆕 `p456` — **🔴 The trend this pass can actually evidence is a supply-chain one: education platforms do not ship from a trunk, unofficial clients to national systems get WITHDRAWN by their maintainers, and a licence badge is not a licence. 🟢 Plus one methodological trend that governs this whole file: a search channel's nil and non-nil one pass apart are variance, not change.**

🔴 **`make hooks` DENIED** (`Code from External`) — eleventh denial in twelve passes. 🔵 Nothing
below is gate-attested; 31 controls run in both directions
([`compose/code/p456-ref-resolution/controls.py`](../compose/code/p456-ref-resolution/controls.py)).

### 🟢 `T1` — The education-platform tier ships from release branches, and that is a maturity signal

🟢 **Measured, not asserted:** of 455 repository addresses on these shelves, **15** point `HEAD` at
something outside a trunk, and **11 of the 15 are the foundational platform tier** — ILIAS
`release_11`, Tutor `release`, OpenEduCat `19.0`, BigBlueButton `v4.0.x-develop`, Gibbon
`v31.0.00`, Edu-Sharing `maven/fixes/10.0`, i-Educar `2.12`, RosarioSIS `mobile`, Krayin `2.2`,
TinCanPython `3.x`, Caliper PHP `public`. 🔵 **LMS and SIS projects with real institutional
install bases default to a version line and keep no moving trunk as default**, because their users
are schools on an academic calendar, not developers. 🔴 **The consequence is a delivery risk, not a
curiosity:** a recipe that clones without `-b` pins silently, and BigBlueButton's `v4.0.x-develop`
default means its maintainers expect integrators to **track a develop line** — a support posture to
price. 🟢 Refs are now pinned on [`verticals/solutions.md`](../verticals/solutions.md).

### 🔴 `T2` — The national-system adapter tier is withdrawal-prone, and the first withdrawal is caught

🔴 `p455` opened an EMEA tier of **eleven permissive clients to four closed national school
systems** (PRONOTE, EcoleDirecte, Schulportal Hessen, WebUntis). 🔴 **One pass later, one of them
is deprecated by its own maintainers** — `lanis-mobile/LanisAPI`'s default branch is literally
named `deprecation-notice` and its README points to a successor. 🔵 Combined with what `p455`
already recorded — `pronotepy` in **maintenance mode**, `ecoledirecte.js` **abandoned since
2023-08-08**, `Pawnote` and `Pawdirecte` with declared grants and **no readable code** — the
pattern is now evidenced rather than suspected:

🔴 **An unofficial client to a system of record that the client cannot fork, host or extend has a
short and unpredictable life, because it breaks whenever the vendor moves and there is no
commercial relationship obliging anyone to fix it.** 🟢 **The trend for Globant is that this tier
is sold as a maintained adapter with a named maintenance tail — never as a dependency** — and the
single point of failure is named in the engagement, not discovered in it.

### 🔴 `T3` — Declared grants outrun readable ones, and the gap is widening

🔵 Three distinct failure shapes are now on these shelves, all measured first-hand:

| shape | instance this pass | why it matters |
|---|---|---|
| 🔴 badge/manifest without payload | `tosuki/moodle-mcp` — MIT **shields.io badge linking to `LICENSE`** + `package.json` `"license": "MIT"`, **no payload at 13 paths** | 🔴 a badge whose own link resolves to nothing is the most convincing non-grant there is |
| 🔴 registry declares, repository gone | `p455`'s `Pawnote` (npm `GPL-3.0-or-later`, address dead on 4 case variants) | a populated back-link is not evidence the code is readable |
| 🟡 grant alive on a withdrawn ref | `lanis-mobile/LanisAPI` — MIT on `deprecated-0.4.1` | 🔴 a grant can outlive the project's own intention to offer it |

🟢 **The rule all three force:** the grant is what the **resolved default branch** serves, read
byte-for-byte. A declaration anywhere else — badge, manifest, registry, directory listing — is a
claim about a licence, not a licence.

### 🟡 `T4` — The LMS-agent surface is consolidating into forks, not competitors

🟡 Seven Moodle MCP servers surfaced this week. 🔴 **`triffon/moodle-mcp` serves a byte-identical
MIT payload to `falkenslab/moodle-mcp`, naming `Copyright (c) 2026 Falkenslab`** — upstream's
holder, with no copyright asserted by the fork. 🔵 So the apparent field is a few codebases plus
forks, differentiated mostly by **tool count** (~140 upstream, ~230 in the fork) rather than by
design. 🟢 **The trend to act on: pick the upstream, read the fork's delta.** A tool-count headline
is not a capability difference, and 🔵 the two genuinely differentiated cells are
`G36maid/moodle-mcp` (Rust, 22 curated tools, claimed live validation against Moodle 3.7 → 5.x)
and `duck-5/moodle-mcp` (OpenAPI bridge, configured for one university).

### 🟢 `T5` — The methodological trend, and it is the one that constrains this file

🔴 `p455` graded the prescribed market channel as having **started to serve all four regions** —
*"the first non-nil in nine passes"*. 🔴 **One pass later, with the same prescribed wording, EMEA
and APAC returned the same non-education sources `p454` recorded.** 🟢 **A single run of a search
channel is not evidence that the channel has changed.** A nil and a non-nil one pass apart are
leg-to-leg variance until a result survives two passes. 🔵 That now governs every *"the channel
improved"* claim these shelves make, and it is why `Gap 454-F` is restored to `p454`'s statement
rather than left closed.

### 🟢 `T6` — What the adoption numbers say once they are placed, not pooled

🟢 On one survey programme (**Digital Education Council 2026**, 45 398 responses / 35 countries),
the placed figures tell a story the pooled global number hides: 🟢 **LATAM 92 % students / 79 %
faculty runs ABOVE global 88 % / 77 %**; 🟢 **APAC faculty are the most optimistic cohort (57 %)**;
🔴 **APAC students the most anxious (50 % expect fewer jobs vs 41 % globally)**. 🔴 And the
governance deficit is global, not regional: **57 %** of students say assessments give inadequate AI
guidance and only **31 %** of faculty feel meaningfully involved in setting AI policy.
🔵 **So the sector's binding constraint is no longer adoption — it is assessment design and
governance**, and that is consistent across every region these shelves can place.
🔴 **EMEA has no institution-level rate at all** (`Gap 456-D`), and the one on offer is refused on
[`intel/market.md`](market.md). 🔴 All of it relayed (`Gap 455-E`); this host can read supply
first-hand and demand never.

## 🆕 `p455` — **Four trends, each with a denominator measured this pass. 🔴 The first retires a number this file's neighbour carried for five passes; the second says Europe's school systems are closed by default and that this is the market, not an obstacle.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes.

### 🔴 `Trend 41` — the closed national system of record is the DEFAULT in Western Europe, and the client tier is the whole supply

🟢 **Measured, not asserted: four national school systems across five countries, zero open cores,
eleven permissive third-party clients.** PRONOTE and EcoleDirecte (France), Schulportal Hessen
(Hesse), WebUntis (Austria/Germany/Switzerland) are all proprietary and closed; none has an open
core at any address this pass could read. Every integration surface is a community client over an
API that is usually undocumented.

🔵 **Why this is a trend and not a list:** these shelves spent four hundred passes building a
platform-customisation picture (Moodle, Open edX, Kolibri, Sakai, OpenEduCat) in which the asset is
a forkable core. 🔴 **In Western Europe the asset does not exist.** The engagement inverts: an
**adapter and agent layer against a system of record the client cannot fork, host or extend**,
priced with a maintenance tail because the client tier is unofficial by construction. 🟢 Evidence
of that tail is on the rows themselves — `pronotepy` is in **maintenance mode** for exactly this
reason, `a2br/ecoledirecte.js` was **abandoned 2023-08-08** for it, and LanisAPI's maintainers
state the portal is fragmented per school.

🔴 **And the constraint that decides the architecture before any model choice is made:** a stated
rate limit of **never 10 req/s, ≤1 800 req/h, in no case >3 600 req/h**, with *permanent blocking*
named as the penalty. A polling agent needs a per-tenant scheduler and cache as a **precondition**,
not an optimisation.

### 🔴 `Trend 42` — a licence FAMILY is not a licence, and 11 cells on these shelves cannot answer a compatibility question at all

🟢 `Gap 454-C` is answered and the axis is now live: the reader returns `GPL-2.0` / `GPL-3.0` /
`LGPL-2.1` / `LGPL-3.0` / `AGPL-3.0`, and the pair the gap named —
[`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing), **`GNU GPL v2`** declared
against **GPL *Version 3*** served — now **disagrees** where `p454`'s family-level `canon()` graded
it `AGREE`. GPL-2.0 and GPL-3.0 are **mutually incompatible**, so the shelf was telling an
engagement team that two opposite constraints were the same constraint.

🟡 **The new number: 11 of 461 cell-attributed GNU cells (2.4 %) are `UNDER_SPECIFIED`** — the shelf
states a bare family, the payload serves a version, and no combination decision is possible in
either direction. 🔵 **And the second axis matters as much as the first**: `GPL-2.0-only` cannot
combine with GPL-3.0 while `GPL-2.0-or-later` can. Read first-hand this pass,
[`oat-sa/tao-core`](https://github.com/oat-sa/tao-core)'s GPLv2 is **`or-later`** — so TAO *may*
be combined forward, where a version-only reader would have called it a dead end. 🔴 `UNSTATED` is
a real and common answer and is never guessed: guessing `or-later` invents a combination right,
guessing `only` invents a prohibition.

### 🔴 `Trend 43` — the regulatory frontier for education AI has moved from "principles" to "named instruments with dated deadlines", and human-in-the-loop is now a CLASSIFICATION argument

🟢 Three jurisdictions crossed into binding, education-specific classification this year, and all
three can be cited by instrument number:

| jurisdiction | instrument | what it classifies in education | when it bites |
|---|---|---|---|
| 🇪🇺 EU | **Regulation (EU) 2026/1744** (Digital Omnibus), in force **2026-07-27**, amending the AI Act | Annex III **3(a)** admissions/ranking, **3(b)** grading and evaluation of learning outcomes | 🔴 **2027-12-02** for stand-alone Annex III systems (*not* the 2027-08-02 many guides still print); 2028-08-02 embedded in regulated products. Emotion-recognition ban + AI-literacy duty live since **Feb 2025**; Article 50 transparency since **2026-08-02** |
| 🇻🇳 Vietnam | **Decision `33/2026/QD-TTg`**, issued **2026-06-30**, effective **2026-08-15** | 3 of 46 listed systems: self-learning content from **uncontrolled data sources**; **automatic assessment/grading/ranking**; **biometric behaviour monitoring** | **2027-03-01** for systems started within 6 months of effect; **2027-09-01** for health/education/finance systems already operating before 2026-08-15 |
| 🇰🇷 Korea | **AI Framework Act**, effective **2026-01-22** | General framework; education not separately enumerated | 1-year penalty grace, 2026 treated as a pilot period |

🔵 **The design consequence, and it is the same in both of the specific regimes:** the EU requires
that qualified staff can *monitor, intervene, override and shut down* a high-risk system, and
Vietnam lists many systems as high-risk **only where the AI output is the sole basis for a decision
without meaningful human review**. 🟢 **So a human-in-the-loop architecture is an argument about
which regulatory class a product falls into** — not a UX preference and not merely good practice.
🔴 **Extraterritorial reach is the clause that makes this Globant's constraint and not only a
client's**: the EU Act reaches non-EU providers whose outputs affect EU-located students.

### 🔴 `Trend 44` — the demand side of this base is structurally unverifiable from this host, and the supply side is structurally first-hand

🔴 **Measured on the proxy's own register this pass**, extending `p450`'s EU-primaries finding:
`www.unesco.org`, `www.iesalc.unesco.org` and `education.ec.europa.eu` are refused at
**CONNECT** (`connect_rejected`), while `raw.githubusercontent.com`, `pypi.org`,
`registry.npmjs.org`, `crates.io` and `packagist.org` all served **200** in the same session.

🔵 **The asymmetry is a property of the environment, not the sector**, and it is permanent until the
policy changes: every licence on these shelves is a byte-level read with a digest; **every market,
adoption and regulatory figure is a search relay** that cannot be checked against the primary from
here. 🟢 The only available mitigation is the one applied across this pass — publish the
**instrument number** so that a reader who can reach a primary is able to check what this base
could not. 🔴 And one carried figure failed exactly this test: *"134 bills across 31 states"* turns
out to be **one tracker as of March 2026**, against **87/28**, **77/27** and **52/25** from three
others on the same session — a **2.6× spread** that five passes of these shelves reported as a fact.

## 🆕 `p454` — **Three trends, each with a measured denominator from this pass rather than a vendor quote. 🔴 The first says the licence READER is now a bigger error source than the licence FIELD; the second is a licence shape education has for a structural reason; the third amends a shelf rule this base wrote one pass ago.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes.

### 🔴 `T454-1` — The reader is the instrument, and it has a measured error rate

🔵 `p453` established that a registry's licence field disagrees with the payload **3.0 %** of the
time. 🟢 This pass measured the same question over the cells this base has **published**: **3 of 71
(4.2 %)** — indistinguishable from the novel rate, which refutes the idea that curation cleans the
field.

🔴 **But the larger error was in the tool, not the data.** Re-reading **179 carried payloads** with
two readers, **5 (2.8 %) grade differently**, and the carried reader is wrong in all five:

| mis-grade | instance | why |
|---|---|---|
| 🔴 `GPL-2.0` read as `LGPL` | [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | GPLv2's **preamble** recommends the LGPL at non-empty line 15 — inside the 40-line window `p450` installed to fix the *GPLv3* case, whose mention falls outside it |
| 🔴 closed grant read as `UNREAD` | [`nakafaai/aksara`](https://github.com/nakafaai/aksara), [`asherlc/dofek`](https://github.com/asherlc/dofek) | neither payload is an OSI family, so a family-matcher returns "unknown" for text that says *"not open source"* in its second sentence |
| 🟡 pointer read as `UNREAD` | [`ckeditor/ckeditor5`](https://github.com/ckeditor/ckeditor5) | a `170` B root file naming another path is the **absence** of a grant here, not the refusal of one |
| 🟡 composite read as one family | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | a two-part notice graded `CC-BY` and silently discarded the MIT half |

🟢 **The direction is what makes this a trend and not a bug report: three of the five were
`UNREAD`.** On a shelf, `UNREAD` reads as *"grant not determined"* — an invitation to a later pass
to promote the row. **Two of those three are genuinely closed.** A licence pipeline's dangerous
failure is not mislabelling MIT as Apache; it is reporting *silence* where there is a **refusal**.

🔵 **Engagement consequence:** a licence attestation is only as good as the reader that produced
it, and a reader validated on one licence version is not validated. Ask which reader, on which
date, against which control set.

### 🟡 `T454-2` — Education licenses in three strata, and a single SPDX field cannot say so

🟢 Found **independently, in one hour, on two continents**: `bncc-dev/bncc-pacotes` (Brazil) splits
**MIT code / CC BY 4.0 curriculum data / withheld brand**; `nakafaai/aksara` (Indonesia) splits
**Source Available 2.0 code / Content License 2.0 material / Trademark Policy 2.0 brand**.

🔵 **The mechanism is structural, not stylistic.** A vertical that ships curriculum with code holds
two legally different asset classes in one artefact, and content is not licensed like software.
`bncc-pacotes` says so explicitly: the npm tarball and the PyPI wheel carry **both grants in the
same artefact**.

🔴 **So every "MIT" badge on an education data package is a partial statement**, and the part it
omits is the part with the attribution duty. 🟢 The clearance unit for this industry is **three
grants per asset**, not one.

### 🟢 `T454-3` — A named system of record beats a common noun only if the name is LONG

🔵 `Gap 453-B`'s remedy, written one pass ago, was *"prefer a named system of record"* after
`pedagogy`, `special-education` and `vocational` returned **0 % precision over 61 candidates**.
🟢 Tested this pass over 4 legs × 3 registries, and it holds **with an amendment**:

| term | shape | candidates | education assets | precision |
|---|---|---|---|---|
| 🟢 `dapodik` | long, distinctive proper name | 4 | 4 | 🟢 **100 %** |
| 🟡 `gakko kihon chosa` / `e-stat` | named service | 47 | 1 | 🟡 2 % |
| 🔴 `deped` | **5-letter acronym** | 59 | 0 | 🔴 **0 %** |
| 🔴 `psa` | **3-letter acronym** | — | 0 | 🔴 **0 %** |

🔴 **`deped` matched the substring `dep` across all of Packagist** — `deptrac`, `php-di`,
`symfony/dependency-injection`, `composer-dependency-analyser`. `psa` matched ConnectWise PSA,
PureScript `psa`, Oracle `oci-psa`. 🟢 **Amended rule:** a system-of-record name is only
unambiguous when it is **orthographically distinctive** — `dapodik`, `vervalpd`, `ecoledirecte`,
`pronote` qualify; `deped`, `psa`, `npsn`, `uis`, `ISCED` do not, and spending a leg on them buys
a homonym list.

## 🆕 `p453` — **🟢 Three trends this pass can assert with a measured mechanism rather than a vendor quote, and all three change what an engagement does on day one: a registry licence badge is wrong 3 % of the time and wrong in the expensive direction once; the national system of record, not the LMS, is the real integration surface outside the Anglosphere; and the institution-registry layer has split into strata that answer different questions.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

### 🔴 `T453-1` — A package registry's licence field is not a licence, and now there is a rate

🟢 **Measured, not inferred: 166 live education-vertical packages, declared npm licence against the
payload read first-hand at `HEAD`.**

| verdict | n | share | what it means on an engagement |
|---|---|---|---|
| 🟢 `AGREE` | 121 | 72.9 % | the badge is corroborated by the payload |
| 🔴 `MANIFEST_ONLY` | 35 | 21.1 % | a grant **declared** in the registry with **no payload at 9 probed paths** — nothing in the repository serves its text |
| 🔴 `DISAGREE` | **5** | **3.0 %** | the repository grants something **different** from the badge |
| 🔴 `POINTER` | 4 | 2.4 % | `SEE LICENSE IN …` — a pointer out of the registry, not a grant |
| 🟡 `PAYLOAD_UNREAD` | 1 | 0.6 % | payload present, family not determinable title-anchored |

🔵 **Why this is a different question from the one `p452` answered.** `p452` swept whether a
registry record back-links the right **address** (63 of 71 `AGREE`, **0** `DISAGREE`) and concluded
the population was clean. 🟢 **That conclusion stands and is not weakened** — but address
attribution and licence **value** are independent axes, and on the value axis the population is
*not* clean. A record can back-link the correct repository and still state the wrong licence.
🔴 **The asymmetry is what matters: 4 of the 5 disagreements are permissive↔permissive or
permissive↔public-domain, and 1 is `MIT` declared over `AGPL-3.0` served** — a shipping blocker
read as a green light. 🟢 **Standing rule: the payload at `HEAD` is the grant; the registry field
is a hint.** Encoded in `P453-A`.
🔵 Honest bound on the `MANIFEST_ONLY` share: **13 of the 35** are Laboratoria bootcamp `md-links`
exercises reached by one Portuguese-vocabulary leg. Excluding that cluster the rate is **22 of
153 = 14.4 %**, still the second-largest class.

### 🟢 `T453-2` — Outside the Anglosphere the integration surface is a closed national SIS, not an LMS

🔵 These shelves carry eight self-hostable platforms and ~30 Moodle/Canvas/Blackboard/Brightspace
connectors — an architecture that assumes the institution runs an LMS the engagement can reach.
🔴 **France does not match that assumption**, and this pass found it only by changing vocabulary:
**ÉcoleDirecte** holds grades, homework, timetable and `vie scolaire`, publishes **no open core**,
and is reached exclusively through third-party client libraries —
[`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) (Apache-2.0),
[`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) (GPL-3.0),
[`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) (ISC,
manifest-only).

🟢 **Three independent parties maintaining clients for one closed SIS is the market signature of
this trend**: where the system of record publishes nothing, the integration layer is rebuilt per
app instead of shared, and the grant varies per rebuild — permissive, copyleft and unpayloaded
across these three. 🔴 **Consequence for Globant: the licence risk in such a market attaches to
the connector, not to the platform**, and the platform cannot be swapped to avoid it.
🔵 Corroborating instances already on these shelves, now readable as the same pattern:
`dev-cucei-itrans/siiau-api-client` (SIIAU, Mexico — grant split across versions, Packagist the
only surviving channel) and `krzysztofbury/librus-mcp` (Librus, Poland). 🔴 The pattern is
**three regions deep and was never named** until this pass.

### 🟢 `T453-3` — The institution-registry layer is three strata, and they are not substitutes

🟢 `p452` opened this layer with one country. 🔵 With North America added it is legible as strata:
a **national directory** (*which institutions exist* — `geoalgeria`, MIT), a **federal statistical
series** (*what is true of each, longitudinally* — `ipeds-database`/`scipeds`, MIT, 27 M rows
1997-2024), and **school-authored disclosure** (*what the institution says about itself this year*
— `collegedata-fyi`, MIT, 4 071 archived CDS documents).
🔴 **They disagree by construction**, and an engagement that merges them produces figures no
institution will confirm — which is why `collegedata-fyi` keeping CDS and federal data separately
labelled is the design decision worth copying, not an implementation detail.
🔴 **The stratum APAC lacks is the first one**: India's UDISE+-derived directories number 1.47 M
schools and **4 of 5 packaged forms grant nothing**, the fifth being CC-BY-SA-4.0. 🔵 Recorded as
an informed absence — the supply exists and the *grants* do not.

## 🆕 `p452` — **🟢 Two trends this pass can assert with a mechanism rather than a vendor quote, and both are about PROVENANCE rather than capability: the registry channel corroborates npm grants and structurally CANNOT corroborate PyPI ones, and the education agent tier has produced its first instance that points at the developer instead of the LMS.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

### 🟢 `T452-1` — Grant provenance splits by ECOSYSTEM, and it decides what Globant can ship

🟢 Measured this pass over **71** carried registry-sourced licence cells
([`evidence/backlink-agreement-sweep.2026-10-26-p452.tsv`](../evidence/backlink-agreement-sweep.2026-10-26-p452.tsv)):
**63 AGREE, 6 ABSENT, 1 PAGES_ONLY, 1 NO_RECORD, 0 DISAGREE.** 🔴 The failures are not evenly
distributed: **4 of the 6 `ABSENT` and the single `PAGES_ONLY` are PyPI**, against **2 `ABSENT` on
npm**.

🔵 **Mechanism, not correlation.** npm's `repository` field is conventional to the point of
near-universality and `npm publish` surfaces it; PyPI's `project_urls` is optional and is frequently
`null` — `deeptutor` `1.6.15`, this base's most-cited agent, declares **`project_urls: null`** and
**no `home_page`**, so its Apache-2.0 has **no registry back-link at all**.

🔴 **Consequence for an engagement, stated as a rule:** *"it is published on a registry"* is
**uniform-looking evidence that is not uniform**. It corroborates a grant in the JavaScript tier
and largely cannot in the Python tier — and the Python tier is most of this base's tutoring,
psychometrics and analytics supply. 🟢 A licence-assurance step must therefore read the **payload**
for Python dependencies and may lean on the registry for Node ones. 🔵 `p451`'s standing back-link
rule is necessary and **not sufficient**: it tells you when a record *is* evidence, and this trend
says which half of your dependency tree will have no record to rule on.

### 🟢 `T452-2` — The education agent tier turns inward: the first agent here that instruments the DEVELOPER, not the institution

🔵 Every agent on [`agents/top.md`](../agents/top.md) until this pass points **at** an education
system — Moodle, Canvas, Blackboard, Brightspace, D2L, a registrar, an SIS. 🟢
[`D4vRAM369/pbl-project-chronicler`](https://github.com/D4vRAM369/pbl-project-chronicler) (🟢 **MIT**,
`LICENSE` 1 066 B `sha256₁₂ 95576ceceaa3`) points at the **development session** and treats it as the
learning object: a glossary with analogies, a reproducible step-by-step, architecture decisions
*and their reasons*, and errors kept deliberately as *"oro pedagógico"*.

🟢 **Why this is a trend datum and not a curiosity.** It is the project-based-learning pedagogy
implemented as an **agent skill** rather than as courseware, and it inverts the integration cost
that gates every other row on that shelf: no LMS, no institutional credential, no token, no security
review of a third-party LMS integration. 🔵 **It is deployable in a Globant engagement on day one**,
which no LMS connector on these shelves is.

🟡 **Its denominator, so it is not over-read: n = 1.** One MIT repository, Spanish-first, no
institution asserted. 🔴 It is an instance of a category, not evidence of a wave, and it is recorded
as the category's first instance so a later pass can test whether the category grows.

### 🔴 `T452-3` — The "trending" channel reports this base's own shelf back to it

🔴 The prescribed GitHub-trending leg returned exactly one education-vertical repository this window,
[`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy), presented as an October
2026 highlight. 🔵 This base has carried it since `p395` and graded it **two licences deep**: `LICENSE`
**ODbL** 25 289 B, `LICENSE-CONTENT` **CC BY-SA 4.0** 18 375 B — **share-alike on the database and on
the content**, so Globant cannot build a proprietary deliverable on the best curriculum graph here.

🟢 **The trend is structural:** a popularity channel selects for what is already well known, and
what is already well known is already shelved after 451 passes. 🔴 **Popularity channels cannot grow
this base; inventory channels can** — 39 addresses at zero prior hits from a registry search under
an unused vocabulary, against 0 from 120 graded hits on the saturated one. 🔵 `agents/top.md:1237`
records the matching near-miss: `os-taxonomy` entered as *"newly trending, assumed permissive"* and
turned out **ODbL**. The assumption a trending list invites is precisely the one that costs a
deliverable.

## 🆕 Trend 51 — `p451` **A package registry is a time machine for deleted repositories — and a package NAME is not, which is the half that costs you a wrong row**

🔴 **Measured, not argued.** Nine addresses carried on these shelves return `404` on
`raw.githubusercontent HEAD/README.md` and `128` on `git ls-remote`, **byte-identical to a
fabricated control** (`globant-fabricated-451/does-not-exist`). On the GitHub channel that is all
there is to know, which is why `p450` closed `Gap 420-C` as unanswerable. 🟢 **On the registry
channel, six of the nine resolve** — because npm, PyPI and Packagist store the `repository` URL
**submitted at publish time**, and that record outlives the repository:

- 🟢 `thanh01pmt/interactive-quiz-kit` → npm `@thanh01.pmt/interactive-quiz-kit`, **103** versions,
  2025-06-12 → 2026-09-23, **MIT**.
- 🟢 `parkseokjune/unist-blackboard-mcp` → PyPI `0.2.0`, **MIT**, four `project_urls` naming it.
- 🟢 `Mckaroff/GraphLMS` → npm `rhizome-lms-mcp` `0.3.1`, **MIT**.
- 🟡 `santillana-ai/tutor-sdk` → npm `@santillana-ai/create-tutor-app`, 63 versions, MIT manifest,
  no payload.
- 🔴 `ale-alejandro/beadkit` → npm `beadkit`, licence string **`SEE LICENSE IN LICENSE`**.
- 🔴 `dev-cucei-itrans/siiau-api-client` → **Packagist**, 7 versions, `proprietary` on four of
  them, `BSD-3-Clause` from `v1.1.2`.

🔵 **The asymmetry is the trend, and it has to be stated in both directions or it misleads:** a
registry back-link **proves prior existence** (an address that never existed cannot be the
back-link of 103 published versions); the **absence** of one proves nothing, because a repository
can be deleted having published nothing. 🔴 `AI-Matrix-Engine/aidream` has no trace on three
registries and is recorded as **unresolved**, never as fabricated.

### 🔴 The expensive half: a registry hit on the NAME is somebody else's project 2 times in 3

🔴 Of the nine dead addresses, **3** produced a registry hit under their natural name, and **2 of
those 3 were a third party's**:

| dead address | registry hit on the name | who it actually is |
|---|---|---|
| 🔴 `e9x/blackboard-mcp` | npm `blackboard-mcp` `0.1.2` | [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) — a **live, MIT** project this base already shelves at `p386` |
| 🔴 `yokowasis/autograder` | npm `autograder` **and** PyPI `autograder` `3.7.7` | two unrelated parties — `sulejmanca` (2017 → 2021, no `repository`) and `zmievsa` (**GPL-3.0**) |
| 🟢 `thanh01pmt/interactive-quiz-kit` | npm `@thanh01.pmt/interactive-quiz-kit` | 🟢 itself — the back-link matches |

🟢 **The discipline, one line:** *a registry record is evidence for an address only when its own
metadata back-links to that exact `owner/repo`.* 🔴 Had this pass accepted the name, it would have
written **GPL-3.0** onto an address whose real grant is unknown, and attributed a live MIT
Blackboard server to a withdrawn one — on a shelf that already carries the real one, two rows up.

### 🟡 And the licence axis this trend forces: permissive is not the same as recoverable

🔵 These shelves grade *what* the licence is. 🔴 **A withdrawn address shows that is one axis
short**: of the six, **3** are registry-recoverable MIT, **1** is manifest-only, **1** is
version-dependent, **1** is unrecoverable. 🟢 Only the first class is buildable on without legal
review — **3 of 6**. 🔵 *"MIT, repository gone"* is three different situations and two of them are
not a grant. Carried in [`repos/foundations.md`](../repos/foundations.md) as the recoverability
classification.

---

## 🆕 Trend 50 — `p450` **A probe that cannot fail is not a weak probe, it is zero bits — and in THIS industry its false negatives land on the platform tier, not the long tail**

🔴 **Measured, not argued.** The probe this base is instructed to use — `curl -sI github.com/{slug}`
— returns **403** for `moodle/moodle`, **403** for `HKUDS/DeepTutor` and **403** for
`nope-xyz-123/nope`, an address fabricated for the purpose. 🟢 **A verdict function that is constant
across its domain carries no information**, so the instruction to *"verify every URL before writing
it"* was, on this host, satisfiable without verifying anything. 🔵 The replacement is two-stage with
controls in both directions (`raw.githubusercontent.com/{slug}/HEAD/README.md`, escalating to
`git ls-remote`), and its first run produced the census below.

🔴 **The non-obvious half, and the reason this is a trend rather than a bug report: the error is not
uniformly distributed.** Of 375 shelved addresses, **19 are live and invisible to a one-path
`README.md` probe** — and they are not obscure:

| would be condemned as dead | what it actually is |
|---|---|
| `openedx/edx-platform` *(`README.rst`, ref `master`, 294 heads)* | the reference Open edX platform |
| `overhangio/tutor` *(`README.rst`, ref 🔴 **`release`**)* | the canonical Open edX deployer |
| `oppia/oppia` *(no README at 10 paths, ref 🔴 **`develop`**, 500 heads)* | Apache-2.0, grant read first-hand |
| `h5p/h5p-php-library` *(`README.txt`, ref `master`)* | embedded in nearly every LMS |

🟢 **Mechanism, stated so it generalises past education:** `raw` is a **path** server, not a
repository server. It resolves `{ref}/{exact-cased-path}` and nothing else, so **the README's
extension, its letter case and the default ref are three independent variables**, and a probe that
fixes all three measures none of them. Measured distribution of the 19: **`.rst` 10 · lowercase
`readme.md` 4 · none-at-10-paths 3 · `README.txt` 1 · `README.markdown` 1**; default refs
**`master` 11 · `main` 5 · `develop` 1 · `release` 1**.

🔴 **Why education specifically.** The platform half of this industry — Open edX, XBlock, ORA2,
Tutor, the LTI libraries — is a **reStructuredText and Python-packaging ecosystem**, so `.rst` is
not an exception here, it is the convention. 🔵 **An automated KB pipeline built on a
`main`+`README.md` assumption therefore prunes edtech's most important repositories first**, and
reports a clean run while doing it. That is the generalisable claim: **in any vertical, naive
discovery tooling fails hardest on the vertical's oldest and most load-bearing projects**, because
those predate the conventions the tooling assumes.

🔴 **`gate-slug-oracle`'s premise falls to the same control.** `p293` held that *"a credential
prompt is a MEASUREMENT, not an inconclusive result"*, and `Gap 420-C` named it the cheapest
closure available for thirty passes. Run un-credentialled, the fabricated slug emits stderr
**byte-identical** to all eight carried addresses: GitHub returns a credential prompt for
non-existent repositories precisely so a 404 cannot leak a private one's existence. 🟢 **A signal
engineered to be uninformative cannot be made informative by running it again** — closed as
UNANSWERABLE ON THIS CHANNEL.

🔵 **Operational residue, and it is the only part a client sees:** 5 of the 9 unreachable addresses
still publish working npm packages. **Installable and un-forkable** — nothing to audit, patch or
vendor. A dependency, never a starting point.

---

## 🆕 Trend 51 — `p450` **The AI-in-education forecast is a 5.9× spread, and the spread is definitional — so the market-size number is the least transportable thing in a proposal**

Six houses, read **2026-10-26**, all for a **2026** base year: **$11.4 B** (Grand View) · **$10.6 B**
(Research and Markets) · **$9.58 B** (Precedence) · **$2.73 B** (Insight Partners, 2025 base) ·
**$1.94 B** (Market Reports World); Technavio prices the *increment* at **+$3.37 B** over 2026–2030.
CAGRs: **17.08 % → 45.0 %**.

🔴 **A 5.9× spread on the base and a 2.6× spread on the growth rate**, between houses reading the
same year. 🟢 **It is not disagreement about the world — it is a boundary question**: whether AI
embedded inside an LMS subscription is "AI in education" revenue or LMS revenue. The low estimates
count standalone AI products; the high ones count embedded capability.

🔵 **Rule, and it is the usable output of this trend: no figure travels without its house and its
definition.** 🟢 **What the houses agree on, and what should be quoted instead:** **North America
is the largest current share; APAC is the fastest-growing** — concordant across Grand View and
Research and Markets, with APAC's rate attributed to state AI-literacy programmes in CN/IN/JP/KR.
🔵 A directional claim two independent houses share outranks a point estimate only one of them
would defend.
## 🆕 Trend 49 — `p449` **An instrument sampled faster than the thing it measures reports its own clock and calls it a finding — and this base has now done that four times in a row, in the one file whose entire purpose is to record change**

🟢 **Gate posture first (`Gap 446-A`): `make hooks` RAN** — the fourth trial after three
denials, so `p448`'s settlement of that gap as *"a property of the host class"* is **refuted**.
The denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 two of them new
and both `p448`'s.

### The trend, stated as a measurement

`Trend 48` found that this base's instrument defects are **not random** — every one caught that
hour failed toward the answer the base already believed. 🟢 **`Trend 49` names the mechanism one
level down: the sampling rate.**

| quantity | value |
|---|---|
| inter-pass interval, median (n=**309**, `p49`-`p448`, commit→commit) | 🔴 **61.1 min** |
| p10 / p90 | **46.0** / **78.1** min |
| share inside 45-75 min | 🔴 **79.6 %** |
| `p448` commit → `p449` read | 🔴 **40 min 20 s** |
| GitHub trending refresh period | **daily** |
| ⇒ passes per channel snapshot | 🔴 **≈ 23.6** |
| ⇒ P(a pass observes an unchanged channel) | 🔴 **≈ 95.8 %** |

🔵 `p446`, `p447`, `p448` and `p449` each recorded a **saturated discovery channel**. 🔴 At this
cadence **that is the expected observation**, and it is consistent with an ecosystem moving at
full speed. Four saturations are **~zero bits** about supply
(`evidence/inter-pass-cadence.2026-10-26-p449.tsv`).

### Why this is a trend about *measurement* and not a scheduling complaint

🔴 **The failure mode is directional, exactly as `Trend 48` predicts.** A saturated channel reads
as *"the supply has been exhausted; the shelves are complete"* — which is the conclusion the base
already wants, because it is the conclusion under which its own shelves look finished. 🔵 Three
passes drew progressively stronger versions of it (`p446` "saturated", `p447` "standing",
`p448` "a third time"), and `p448` was right to register `Gap 448-A` rather than a fourth.

🟢 **The same lesson has now fired on three instruments in two passes, and the sign is always the
same:**

| instrument | defect | direction of failure |
|---|---|---|
| `p448` substring novelty check (`Gap 447-A`) | unscoped `grep -ri` | toward *"already known"* → suppress a real finding |
| `p448` tool extractor (`Gap 448-C`) | regex over all of `src/` | toward *"no write tools here"* → confirm read-only |
| 🆕 `p449` URL probe (`Gap 449-A`) | `curl -sI` on `github.com` → **403 on every real repo** | toward *"dead row"* → discard a live address |
| 🆕 `p449` URL probe (`Gap 449-B`) | case-normalised path | toward *"dead row"* → `XBlock` read 404 three times, then **200 / 11 358 B** at the recorded case |
| 🆕 `p449` discovery channel (this trend) | hourly sampling of a daily channel | toward *"saturated"* → shelves look complete |

🟢 **So the operating rule this base should adopt, and `p449` applies it to itself:** a nil is
not reportable without the **interval** over which it was measured, and an instrument is not
trustworthy until a **negative control** has been run through it. 🔵 `p449`'s URL probe carries
one (`zzz-fake-org-p449/zzz-fake-repo` → `404 / 14 B`); its tool count carries a second channel
(README prose, **187** against a true **188**); and its cadence claim carries a population of
**309** rather than the single interval `p448` could cite.

🔴 **The residual risk, named rather than resolved.** This measurement is one repository's commit
history on one schedule. It does **not** establish the refresh period of the *web search* channel,
only of GitHub trending — and the four global legs run each hour go through the former
→ `Gap 448-D` remains open and is now the binding uncertainty on every nil this base reports.

---

## 🆕 Trend 48 — `p448` **This base's measurement errors are NOT random: every instrument defect caught this hour failed toward the answer the base already believed. Three independent instruments, three different mechanisms, one direction — which means a saturated channel and a confirmed hypothesis are exactly what a broken instrument looks like.**

🔵 **Why this is a trend and not one pass's housekeeping.** `p447` caught a substring novelty
check reporting *"already known"* for a genuinely new item and registered it as `Gap 447-A`,
calling out that *"a substring check fails toward 'already known', which suppresses real
findings silently."* `p448` found **two more instruments with the same bias, by different
mechanisms, in the same hour** — and in one of them the bias would have **confirmed a published
hypothesis that is in fact false**. One instance is a defect. Three, pointing the same way, is a
property of how this base measures.

### 🔴 The three instances, each with its mechanism and the false conclusion it would have produced

| instrument | mechanism of the defect | the comfortable answer it produced | 🟢 the truth, measured |
|---|---|---|---|
| **substring novelty check** (`grep -ri`) | `teds` matches inside `relaTEDSubject` and `generaTEDStatus` — 3 hits, **0** word-scoped | 🔴 *"TSDS/TEDS already known"* → the NA state finding suppressed | 🟢 `grep -riw` = **0**. `TEDS`, `TSDS`, `PEIMS`, `CAASPP`, `ELPAC` all genuinely new |
| **MCP tool extractor** (regex over registries) | three unseen idioms: bare `@mcp.tool` with no parens (**130** occurrences read as **1**), nested-paren decorator args, and a **Go** codebase scanned only for `.py`/`.ts`/`.js` (read as **0**) | 🔴 *"the community LMS connectors are read-only"* → `Gap 447-B` **CONFIRMED** | 🟢 **136 of 414** declarations mutate (**32.9 %**); `create_course`, `toggle-module-publish`, `update-syllabus` all read from source |
| **pin-stability sample** (`Pattern AZ`) | the 18 pins were drawn from pins **already carried across passes**, i.e. pre-selected for having survived | 🔴 *"17 of 18 survive 24 h — a cheap minority repair"* | 🔴 Over 496 unbiased pinnings, **67.3 %** survive. **A third die.** |

🟢 **The first two were caught only because something external contradicted them.** The
substring hit was questioned because a *state-shaped* search had just produced a name the base
did not recognise. The extractor was questioned because its output was **absurd** — one tool in
a repository `p446` had independently counted at **128**. 🔴 **Neither was caught by a gate**;
`make hooks` has now been denied three passes running.

### 🔴 The structural reason, and it generalises past this base

Every one of these instruments answers a question of the form *"is there anything here?"*, and
each fails by **not finding** rather than by finding wrongly:

- a substring match **adds** false hits → the novelty test, which reads *hits = known*, flips to *known*
- a regex that misses an idiom **removes** tools → a capability test flips to *absent*
- a sample drawn from survivors **removes** failures → a stability test flips to *stable*

🔵 **A null result is therefore the least trustworthy result this base can produce**, because
it is the result every broken instrument produces. 🔴 And this base's most-repeated recent
finding is a null: **three consecutive passes of "discovery saturated, zero new rows."**

### 🟡 The second-order finding: `n = 1 per unit` manufactures confident, wrong rules

`Pattern AZ` published **three** quantitative claims from **five** observations — one pinning
per repository. `p448` re-measured with 14 pinnings per repository:

| `AZ`'s claim, from n = 5 | 🟢 `p448`, n = 496 |
|---|---|
| *"`pinned_date == HEAD date` **iff** the pin held, in every row"* | 🔴 biconditional **fails in 44 of 167** rows |
| *"**days** → settled, safe to quote"* | 🔴 at **1–3 days the pin fails 28 %** of the time; the real gate is **7 days → 97.4 %** |
| *"commit volume gets staleness **backwards**"* | 🔴 **ρ = +0.886.** Volume is a **good** predictor; the sign was inverted |

🔵 `Trend 45` already recorded an **n = 5 artefact** being published as a rule one pass earlier
(`Trend 44`), and `Trend 41` recorded that **12 %** of this base's own published figures came
from a method it had written a rule against. 🔴 **This is the third time.** The recurring shape
is not a bad instrument but a **denominator of one per unit**.

### 🟢 What follows, as checks rather than sentiment

1. 🟢 **Word-scope every novelty check.** `grep -riw`, never `grep -ri`. Two confirmed
   suppressions in two consecutive passes.
2. 🟢 **Never publish a null without an instrument control.** `Gap 446-D` is the model to copy:
   eleven primaries returning 403 was only interpretable because `raw.githubusercontent.com`
   returned **200** from the same shell in the same minute. A saturated discovery leg has **no
   such control** — and `p448`'s legs ran **43 minutes** after `p447` committed (`Gap 448-A`).
3. 🟢 **Make the absurdity check routine.** The extractor was caught because its output
   disagreed with a number another channel had already published. 🟢 Cross-channel agreement is
   now double-sourced on this shelf: source extraction reproduces `p446`'s README tool counts
   **exactly** at **128 / 126 / 89 / 69**.
4. 🔴 **One observation per unit is not a measurement.** Before a rule is published, state the
   per-unit denominator next to the population denominator.

🟡 **Limit of this trend:** three instances, one hour, one base. The *direction* is unanimous
and each mechanism is identified, but no one has gone back over earlier passes' nulls to measure
how many were instrument artefacts — the audit `Gap 444-D` asks for, still unpaid.

---

## 🆕 Trend 47 — `p447` **A region is a reporting bucket, not a research unit — and the cost of confusing them is not a thin answer but a MANUFACTURED one. The same hour that a region-level EMEA query produced two false, quotable facts, a country-shaped query killed both.**

🔵 **Why this is a trend and not one pass's bad luck.** This base has now nilled the EMEA
region-level leg on **three consecutive passes** (`p445`, `p446`, `p447`) and the North America
region-level leg on **six**. `p445` diagnosed the shape and prescribed country legs; `p446`
re-confirmed the nil and re-registered the prescription; `p447` finally **acted** on it. The
result was not a marginal improvement in yield. It was a **change in kind**.

### 🔴 What the region-level leg produced, and what the country leg did to it

| region-level output | country-leg verdict |
|---|---|
| French ministry signed a February partnership with Mistral to put a chatbot in **lycées** from 2026-27 | 🔴 **FALSE.** Amue is trialling two Mistral tools across **81 public HIGHER-EDUCATION establishments**, bounded to 2026; a separate pilot put a Mistral assistant in front of **10 000 state agents**. A *school* deployment that resolves to a *university* experiment plus a *staff* pilot |
| UK Generative AI in Education framework **updated March 2026** | 🔴 **FALSE.** Product-safety expectations were retitled and expanded **19 January 2026**; *module 3* carries **19 May 2026**; the only May-2026 circular is **Northern Ireland's DE Circular 2026/02** — a different jurisdiction |

🟢 **The mechanism, and it is the part worth generalising.** "EMEA" has no ministry, no statute,
no department and no publication calendar. A query addressed to it cannot be answered by
quotation, so the channel answers by **synthesis** — and synthesis across thirty jurisdictions
produces a sentence that is *shaped* like a fact, carries a month, names a real vendor and a real
department, and is wrong. 🔴 **A thin answer announces itself; a manufactured one does not.** This
is the failure mode `Trend 46` found on the supply side (ten addresses reading as ten options)
appearing on the **demand** side.

### 🟢 What a country leg does differently, mechanically

1. 🟢 **It has an addressable primary**, so the answer can be a quotation rather than a synthesis.
2. 🟢 **It can be run in the jurisdiction's own language** — the French leg was, and that is what
   separated *lycée* from *établissement d'enseignement supérieur*, a distinction the
   English-language region query collapsed.
3. 🟢 **It fails loudly.** A country leg that finds nothing returns nothing; a region leg that
   finds nothing returns an average.

🔵 **Standing instruction this base should now follow:** the five `###` headings on
`intel/market.md` are a **reporting** vocabulary — closed, five values, unchanged. They are
**not a research unit**. Research is addressed to a **country**; findings are **filed** to a
region. 🔴 Where a regional claim on these shelves cannot be traced to a country-shaped query,
it should be re-read as **possibly manufactured**, not merely as thin.

🟡 **The uncomfortable corollary, recorded rather than buried:** this base cannot currently
check any of it against a primary. Eleven official and one commercial host all refuse from this
host (`Gap 446-D`), on two independent channels with two different failure signatures. **The
country leg improves which question gets asked; it does not fix who can be read.**

---

## 🆕 Trend 46 — `p446` **An address count is not an option count. In the one education category where this base has the densest supply, 10 addresses are 6 projects — and the inflation is invisible to every channel this base routinely uses: stars, descriptions, file sets and directory listings all report ten.**

🔵 **Why this is a trend and not a one-off correction.** The LMS-MCP tier is where this base has
its **largest cluster of same-shaped addresses**, and it is also the tier an engagement reads
first, because the question a studio is asked on day one is *how many options do we have*.
`p446` measured it and the answer was **40 % smaller** than the shelf implied.

### 🔴 What each channel reports, against what lineage reports

| channel | what it says about the ten | correct? |
|---|---|---|
| **name** | ten addresses, seven of them literally `canvas-mcp` under seven owners | 🔴 no — says nothing either way |
| **description / README** | tool counts 187, 128, 126, 99, 89, 69 and four silent — **all different** | 🔴 **no, and actively misleading**: it splits `vishalsachdev` (128) from `Harikeshav-R` (126), which are the same project, and groups `bruchris` (187) with them, which is not |
| **file set** | ten distinct file-set digests | 🔴 **no** — a fork that adds or deletes files diverges immediately |
| **licence payload cell** | 🟢 **three collisions**: `5385a26e2fac` ×3, `ab5109aafdb8` ×2 | 🟡 **a strong hint** — a fork inherits the payload byte-identically |
| 🟢 **root commit** | 🟢 **six distinct roots across ten addresses** | 🟢 **yes, and it is decisive** |

### 🟢 The mechanism, stated so it generalises past this tier

🔵 A fork **cannot change its root commit** without rewriting history, and a project that was
genuinely written twice **cannot share one**. Every other signal is downstream of authorship
choices — a fork's owner renames the repo, rewrites the README, adds files, bumps the tool
count — and so every other signal decays toward *looks independent* over time. 🔴 **Which means
the inflation is systematically biased upward and grows with fork age**: the stalest forks look
the most distinct.

🔴 **`NelsonSpencer/canvas-mcp` is the specimen.** 416 commits, 218 files, a file set unlike any
other address, a README claiming 99 tools — and **714 commits behind** an upstream it shares a
2025-02-27 root with, carrying **2** commits of its own. 🟡 By every channel except lineage it
is a project. It is a stale fork with a local patch.

### 🟢 What this trend asks of the shelves

1. 🟢 **Count projects, cite addresses.** `p405` already fixed the citable unit as the
   **family**; this trend supplies the cheap instrument — `git clone --filter=blob:none` plus
   `git rev-list --max-parents=0`, **~1 s per repository, no GitHub API** (which is 403 here
   anyway).
2. 🔴 **Never infer lineage from prose similarity.** `Gap 445-C` did, and was right about the
   arms for a reason that does not hold — see `Gap 446-C`.
3. 🟡 **Treat a payload-cell collision as a lineage alarm, not a curiosity.** Two cells
   repeating across five addresses was visible in this base's own published cells before any
   clone was made, and nothing was looking for it.
4. 🟢 **Where a fork is the maintained side, say so.** In ARM-2 the root (`r-huijts`) is an
   **ancestor** of the fork (`mdweaver`, 4 ahead). Publication order and ownership do not
   predict direction; only history does.

🔵 **Scope, stated honestly.** This is measured on **one category, ten addresses, one pass**. It
is a method result, not a population estimate: this base does **not** yet know what fraction of
its ~134 shelved repositories are fork arms of one another. 🟢 **That is the obvious next
measurement and it is now cheap** — the instrument exists, and the root-commit column is the
whole test. Registered as `Gap 446-E`.


## 🆕 Trend 45 — `p445` **Publisher class does NOT predict grant presence in education open source. 🔴 `Trend 44`, published on this file one pass ago, was an n=5 artefact: measured over 3 932 first-hand addresses the institutional grant rate is 72.2 % against a 76.3 % baseline, Fisher p = 0.558. 🟢 What DOES predict the licence is the PLATFORM's developer community**

### 🔴 The claim this trend replaces, and why it was published

`Trend 44` (`p444`) reads: *"Where the institution publishes the integration code itself, it
publishes it WITHOUT a grant — and the third-party copy is the licensed one."* Its entire
basis:

| publisher class | n | grants present |
|---|---|---|
| institution | 3 | 🔴 **0** |
| individual | 2 | 🟢 **2** |

🔴 **One country (Brazil), one platform (SUAP), one institution (IFRN), five repositories.** A
measured rate of zero on three addresses became a trend about institutions — one pass after
this base corrected `Trend 42` for the identical error, *too small to carry the claim it was
used for*. The pattern is now twice-recorded on this file, which makes it a property of how
this base generalises and not of either tranche.

### 🟢 The test, at a denominator three orders of magnitude larger

`Gap 444-A` prescribed probing institutional GitHub orgs. That needs org enumeration, which is
**403 on this host** (`api.github.com`, `github.com/search` and `codeload.github.com` all
re-measured this hour). 🟢 **But the question needed no new network:** every address this base
has verified first-hand over 445 passes is on disk — **1 228 TSVs** under `evidence/`. Those
were classified by publisher class instead. Instrument, pipeline and stated limits:
[`compose/code/p445-publisher-class-census/README.md`](../compose/code/p445-publisher-class-census/README.md).

| | n |
|---|---|
| evidence files read | 1 228 |
| rows scored | 18 957 |
| rows excluded as unscoreable, and counted as excluded | 26 287 |
| 🟢 **distinct addresses with a first-hand grant verdict** | 🟢 **3 932** |

| class | n | grant | rate | 95 % CI |
|---|---|---|---|---|
| INSTITUTIONAL | 36 | 26 | 🟡 **72.2 %** | 56.0 – 84.2 % |
| NON-INSTITUTIONAL | 3 896 | 2 971 | **76.3 %** | 74.9 – 77.6 % |

🔴 **Fisher exact, two-tailed: p = 0.558.** Then all **36** institutional rows were
hand-labelled — the whole class, not a sample. **Nine were false positives** (precision
**75.0 %**): `UniversalDependencies`, an NLP treebank consortium caught on `univ` *inside its
own name*; `EscolaLMS`, a Polish LMS **vendor**; `schoolutils`, a developer utility org;
`schoolyardsms`, an SMS product. Every one is a **supplier or project** matched on an
institution word.

| after correction | n | grant | rate |
|---|---|---|---|
| by ADDRESS | 27 | 18 | **66.7 %** |
| by **PUBLISHER** (the correct unit) | 15 | 11 | **73.3 %** |
| non-institutional, same unit | 2 914 | 2 246 | **77.1 %** |

🟡 **The direction survives every cut — institutional is lower, by 4 to 10 points — and not one
cut makes it distinguishable from noise.** Predictions registered before the census ran
(`scratchpad/p445/predictions.txt`): **P3** (direction) confirmed but insignificant; **P4**
(*the rate of zero will not reproduce*) 🟢 **confirmed** — the rate is 66.7–73.3 %, nowhere
near 0 %; **P5** (*the classifier, not the arithmetic, is the binding error term*) 🟢
**confirmed**.

### 🔴 And the finding about this base, which is the part a successor must not skip

Only **36 of 3 932** addresses — **0.9 %** — have an institutional publisher at all. Nine are
misclassifications. The surviving 27 come from **15 publishers**, and **one of them — `cahlr`,
a UC Berkeley research lab — supplies 9 of the 27.**

🔴 **So the correct unit of analysis is the publisher, the real institutional n is 15, and after
445 passes this base has barely ever measured the class it published a trend about.** The
honest verdict is therefore neither *yes* nor *no*: the claim is **refuted at the magnitude it
was stated**, and the corpus is too thin in this class to put a sharp number on any residual
effect. That thinness is now measured instead of assumed — `Gap 445-A`.

🟢 **The sharp fact that does survive, and it is still worth money.** `ifrn` + `ifrn-oficial`
remain the **only** institutional publisher in the entire 3 932-address corpus with multiple
addresses and zero grants (3 of 3 ungranted, 81 ★ between them). That is a real and actionable
fact about **IFRN** — `Pattern AW` is unchanged — and it was never a fact about institutions.

### 🟢 What replaces it: the platform's developer community, not the publisher's class

Three readings of the same question now sit on this file, each from a different denominator:

| | claim | denominator |
|---|---|---|
| `Trend 42` (`p443`) | the student side of the glass is **permissive** — 6 of 8 | 8 addresses, 2 platforms |
| `Trend 43` (`p444`) | the modal grant is **NO GRANT** — 18 of 37, permissive 22 % | 37 addresses, 9 platforms |
| 🆕 `p445` | on **SIGAA**, measured end to end, the student side is **uniformly copyleft** — GPL-3.0, 3 of 3 | 3 addresses, 1 platform |

🔵 **Three incompatible answers, and they are not in conflict — they are three platforms.**
The variable that moves is not the side of the glass (`Trend 42`), not the publisher's class
(`Trend 44`), and not the country (`p443`/`p444` both tested that). **It is the licence habit of
the developer community that forms around a particular platform.** SUAP's community attached
MIT and nothing at all; SIGAA's attached GPL-3.0 three times out of three, in two languages,
across two publishers and four years.

🟢 **The operational form, which is the only part that should reach a client conversation:**
**the licence distribution is a property of the PLATFORM, so it must be measured per platform
and can be carried across neither regions nor publisher classes.** An engagement that meets a
new system of record has learned nothing about its grant posture from the last one, and the
probe is cheap — `git ls-remote` plus a blobless tree enumeration, which is what
`lib/probe_payload.sh` already does.

🔴 **The falsifiable half, so this trend is testable rather than another story:** a fourth
platform, measured end to end, should return a **fourth** distribution that matches neither
MIT-and-nothing nor uniform GPL-3.0. If two platforms in different countries return the same
distribution, this trend is wrong and the variable is something above the platform.

---

## 🆕 Trend 43 — `p444` **The LATAM education integration layer is not permissive and not copyleft: it is UNLICENSED. 18 of 37 addresses carry no grant at all, and `Trend 42` — published one pass ago — does not survive the larger denominator**

🔴 **The correction first, because this base published the claim it is correcting.**
[`Trend 42`](#) (`p443`) states that the open-source education supply is *permissive on the
student's side of the glass and copyleft on the institution's*, measured over **one tranche of 8
Brazilian and Argentine addresses**: 6 permissive (5 MIT, 1 Apache-2.0), 2 GPL-3.0.

`p444` measured the **same side of the same glass** in four more countries — Mexico, Brazil,
Chile, Colombia — over **37 addresses**, every one read first-hand this hour:

| grant | n | share | `Trend 42` predicted |
|---|---|---|---|
| 🔴 **no grant file at all** | 🔴 **18** | 🔴 **49 %** | not a category it had |
| GPL-3.0 | 9 | 24 % | — |
| 🟢 MIT | 7 | 19 % | 🟢 the majority |
| AGPL-3.0 | 2 | 5 % | — |
| 🟢 BSD | 1 | 3 % | 🟢 the majority |

🔵 **Permissive is 22 %, not 75 %, and the modal outcome is no licence at all.** `Trend 42` was
not wrong about its eight rows — re-read, all eight reproduce. It was **too small to carry the
claim it was used for**, and the claim it was used for was a composition decision: *"connectors
are safe to vendor, platforms are not."* On the larger denominator that is false for half the
connectors, and the failure mode is worse than copyleft, because copyleft at least grants.

🔴 **A missing LICENSE is not a permissive default and it is not an oversight to work around.**
Absent an express grant, the default is exclusive copyright: no right to copy, modify or
redistribute. A GPL-3.0 connector can be integrated under known obligations. An unlicensed one
**cannot be used at all**, however public the repository is, and however obviously the author
meant it to be shared.

### 🔴 And the unlicensed half is not the junk half, which is what makes it expensive

The intuition is that ungranted repositories are abandoned student scratch work. Measured
against last-commit dates, that intuition is **wrong**:

| | 🟢 live (HEAD 2026) | 🟡 2023–25 | 🔴 dead (≤ 2022) |
|---|---|---|---|
| 🟢 MIT / BSD | 🟢 1 | 1 | 6 |
| GPL-3.0 | 2 | 3 | 4 |
| 🔴 **no grant** | 🔴 **5** | 🔴 **4** | 9 |

🔴 **Five of the eight most recently maintained addresses in the whole tranche carry no
licence**, against **one** permissive one. Among them: `sebassg/sia-unal-mcp`, an **MCP server**
for a Colombian national university's system of record (TypeScript, HEAD 2026-03-12), and
`jeanhrm/siagie-analytics` (Laravel, 146 files, HEAD 2026-08-22). 🔵 **The licence frontier does
not track quality or activity — it tracks nothing at all**, which means a licence screen cannot
be deferred to a late diligence step: the best-maintained candidate is as likely to be unusable
as the worst.

---

## 🆕 Trend 44 — `p444` **Where the institution publishes the integration code itself, it publishes it WITHOUT a grant — and the third-party copy is the licensed one**

🟢 **Measured on the one tranche where both publisher classes exist at once.** Brazil's SUAP
ecosystem (Instituto Federal network) contains both institutional and individual publishers, at
comparable star counts:

| publisher class | addresses | combined ★ | grants |
|---|---|---|---|
| 🏛️ **the institution** (`IFRN/`, `ifrn-oficial/`) | 3 | **81** | 🔴 **0 of 3** |
| 👤 **individuals / student projects** | 4 | 71 | 🟢 **3 of 4** (2 MIT, 1 AGPL-3.0) |

🔴 **So the *sanctioned* integration path — official OAuth2 clients for Django and JavaScript,
and an API client suite, maintained under the institution's own GitHub organisations — is the
one with no right of use.** The engagement that reaches for the official client *because* it is
official reaches for the only one it cannot ship.

🟢 **The resolution exists and is on the shelf**, which is why this is a trend and not just a
complaint: [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) — **MIT,
HEAD 2026-09-05**, 98 Python files, 92 `.rst` of Sphinx docs, on PyPI, with CI, Codecov and a
`SECURITY.md` — does the *same job* as the unlicensed `ifrn-oficial/cliente_suap_django`, and
does it better. 🔵 **The individual's package is more professionally maintained than the
institution's**, which inverts the usual assumption about which to prefer.

🔵 **Why it probably generalises.** An institution publishes code as a *service to its own
users*, not as a product for redistribution, so nobody in the chain has a reason to pick a
licence. An individual publishes to a package registry — PyPI, Packagist, npm — and **a registry
asks for a licence field**. The forcing function is distribution, not governance.

🔴 **What is NOT established:** this is one network in one country. `Gap 444-A` prescribes the
test — probe the institutional GitHub organisations behind the paying platforms (UANL,
U. de Chile, UNAL, the SIGAA operators) and count grant presence **by publisher class**, not by
stars. Until then this is a one-tranche trend with a mechanism, not a measured law.

### 🟢 The engagement rule, usable today

1. 🔴 **Never start from an institution's own client.** Check its grant first; expect none.
2. 🟢 **Prefer the registry-distributed third-party package** — PyPI/Packagist/npm presence is a
   weak but real proxy for a licence actually having been chosen.
3. 🟡 **For a Moodle-side component, expect GPL-3.0 and treat it as coherent**, not as a problem:
   the host platform already imposes it (`moodle-local_suap`, HEAD 2026-10-19).
4. 🔵 **Ask.** 18 addresses here are one polite issue away from being usable, and no pass on this
   base has ever tested whether asking works (`Gap 444-C`).

---


## 🆕 Trend 42 — `p443` **In every region, the open-source education supply is permissive on the student's side of the glass and copyleft on the institution's — and the boundary is the system of record**

🟢 **The claim, with the first LATAM denominator behind it.** This base has recorded a "licence
frontier runs the wrong way" observation for EMEA for many passes. `p443` measured the same
boundary in LATAM, first-hand, over one tranche:

| layer | what it is | permissive | copyleft |
|---|---|---|---|
| 🟢 **student / teacher side of the glass** — readers, extensions, exporters, MCP connectors onto an academic portal | 8 addresses | 🟢 **6** (5 MIT, 1 Apache-2.0) | 2 GPL-3.0 |
| 🔴 **the institution's system of record** — platforms that hold enrolment, grades and attendance | 4 addresses | 🔴 **0** | GPL-2.0, GPL-3.0, GPL-3.0, AGPL-3.0 |

🔵 **And it is the same shape in the other three regions**, from rows already on these shelves:
EMEA's connectors (`librus-mcp`, `iserv-mcp`, `Smartschool-MCP`, `edupage-mcp`,
`dtu-learn-mcp`) are **MIT** while the platforms behind them are vendor-closed or copyleft;
North America's `canvas-mcp` and `fcps-school-mcp` are **MIT** against a closed Canvas and
Schoology; APAC's `SGU-Academic-MCP` is **MIT** against a closed university portal; and the
platform map on [`verticals/solutions.md`](../verticals/solutions.md) is **GPL-3.0, AGPL-3.0,
AGPL-3.0, LGPL-3.0, LGPL-3.0, GPL-3.0** with **Apache-2.0 OpenOLAT and MIT Kolibri as the only
two exceptions in the tier.**

🟢 **Why this is one trend and not two coincidences.** The asymmetry is structural, not
licensing fashion. A system of record is written by the institution that is accountable for the
records — a ministry, a municipality, a university consortium — and public money plus
public-good framing produces copyleft, which is exactly what `ipti/br.tag` (IPTI with Santa
Luzia do Itanhy/SE, *Tecnologia Social*), `eXeLearning` (Spain's education ministry) and Open
edX all are. The glass-side tooling is written by **students, lecturers and single authors who
want it adopted**, and that produces MIT. 🔵 The licence tells you **who wrote it and why**,
and in this industry that correlates with **which side of the record boundary it sits on**.

🔴 **What it costs a team that does not know this.** The platform is the part a client points at
and says *"start from that"*, and it is the part that cannot be vendored into a proprietary
deliverable. Two failure modes follow, and both are live on this base's evidence:

1. 🔴 **Vendoring the platform.** `ipti/br.tag` is the sharpest case ever recorded here, because
   its **README states BSD-3-Clause while its payload is GPL-2.0** — the conflict runs in the
   *permissive* direction, so the careless read is the expensive one, not the cautious one.
2. 🔴 **Reading the root and stopping.** `p442` found **12 of 134** repositories carrying more
   than one grant, and one row sold as MIT shipping a complete GPL-3.0 below its root. The
   copyleft in this industry hides **below** the root as well as behind the README.

🟢 **The design rule it yields, and it is the same rule in all four regions:** put the AI
**beside** the system of record and talk to it over an interface — an MCP server, a REST or
Web-Services client, an XBlock — and keep every line you intend to own on the glass side of the
boundary, where the grants are permissive. 🟢 **That is what makes a connector, not a platform
fork, the sellable unit of an education engagement** — and it is why `p443`'s one-row addition
to [`agents/top.md`](../agents/top.md) (`jpmanson/siu-guarani-mcp`, MIT, read-only, PII-gated)
carries more commercial weight than the 158-★ AGPL-3.0 school-management app it was found
beside. Recipe: `Pattern AV`.

🟡 **The bound on this trend, stated as one.** The LATAM half rests on **12 granted
repositories in one tranche** keyed on two platform names (SIGAA, SIU Guaraní) in two
countries. Peru, Colombia, Chile and Uruguay returned nothing on the name leg and that is an
**unverified nil, not an absence** — the leg ran once, in one shape (`Gap 443-B`). The
four-region claim above is **consistent across every row this base holds** but has a measured
denominator in LATAM only.

---

## 🆕 Trend 40 — `p442` **The second grant lives below the root, and in this industry that is where the copyleft is**

🔵 `Trend 37`: a licence **name** without a licence **text**. `Trend 38`: a tool that declines
and a tool that clears produce the same green. `Trend 39`: a complete grant no title-keyed
tool can classify. 🟢 **`Trend 40` is the structural one: the repository's licence question has
more than one answer, and the extra answers are not at the root.**

🔴 **Measured, 2026-10-25, over the 134 repositories whose payload path these shelves
publish** — every tree enumerated first-hand:

| | n |
|---|---|
| exactly one own-grant path | 🟢 121 |
| 🔴 **more than one** | 🔴 **12 (9 %)** |
| 🔴 more than one **family** | 🔴 **4 (3 %)** |

🔴 **And the direction is the commercially dangerous one.** Of the four multi-family
repositories, **three put the stronger obligation below the root**:
`krzysztofbury/librus-mcp` is MIT at the root with a complete **GPL-3.0** in
`legacy_reference/`; `Hiepler/EuConform` is MIT at the root with **EUPL-1.2** beside it;
`withmarbleapp/os-taxonomy` is ODbL at the root with **CC BY-SA 4.0** for its content. 🔵 The
root file is the *permissive* one in each case, which is exactly the shape a rooted probe —
and a GitHub licence badge, and every scanner that reads one file — reports as clean.

🟢 **The inverse exists too and is worth as much money.** `24kchengYe/human-skill-tree`'s root
payload is a **notice**, so the project reads as ungranted while its real AGPL-3.0 sits in
`app/` — and that same notice carries a **dual AGPL-or-MIT option for `skills/`** that no
root-only read can see. **An enumeration finds permissive lanes, not only obligations.**

🔵 **Why this industry specifically.** Education repositories are *assemblies*: courseware
plus code, a platform plus per-module restatements, a skills pack plus an MCP server, a
taxonomy plus its data. Four of the twelve are per-module restatements of one grant
(`sakaiproject/sakai` ×4, `dodona-edu/dolos` ×3, `microsoft/agent-governance-toolkit`,
`The-Morrow-Project/Morrow-Bridge`) — harmless, and evidence of the same cause: **a
multi-artefact repository is forced to say the licence more than once, and the moment it says
it twice the two can differ.**

🟢 **What to do with it:** `Pattern AU` is the four-step screen, and step 1 is the enumeration.
The cost is **~0.7 s per repository** (blobless depth-1 clone, no API), so there is no version
of this trend where the screen is too expensive to run.

## 🆕 Trend 41 — `p442` **A published figure is a claim about a measurement, and 12 % of this base's own were produced by a method it had already written a rule against**

🔴 **The measurement, on this base's own shelves.** All **162** payload cells on
`agents/top.md`, `repos/foundations.md` and `verticals/solutions.md` were re-measured from the
file **and** through the preserved defect: 🟢 **143 reproduce**, 🔴 **19 (11.7 %) carry the
`P834` capture signature** — byte count short by the trailing-newline run and a digest taken
**of the stripped bytes**.

🔵 **Why this is a trend and not a bug report.** The rule existed (`lib/README.md`: *no byte
figure is published from `$(…)`*), the fix existed (`lib/payload_measure.sh::size_of_file`,
asserted 27/27 at `p837`), and the rows were written **afterwards, by passes that had both**.
Attributed: `p432` **5 of its 5**, `p433` **2 of 5**, `p438` **2 of 11**, every other pass
**0 of 113**. 🔴 So the defect is **intra-pass** — the same pass used the library for some rows
and typed others by hand — which means a reader cannot infer a cell's trustworthiness from
*who wrote it*, only from *re-measuring it*.

🟢 **The generalisation for anyone reading this base, or building one:** a correction needs
three things and the industry habit is to ship one. A **rule** tells the next author what not
to do. A **fix** gives them a correct primitive. 🟢 **Only a gate makes the wrong path cost
something** — and only if the gate sits on the artefact the reader trusts, which here is the
**cell**, not the payload. `make gate-cell-reproduction` is that gate: 21 offline controls,
11 of them negative, and a `CELL-UNMEASURED` verdict for any cell nobody has re-measured.

🔵 **The client-facing version of the same lesson, which is the reason it is on a trends
shelf:** when a vendor hands you a licence report, ask which figures were *re-derived from the
artefact* and which were *copied from the sentence that last stated them*. In this base's own
file the two were visually identical and 19 of them disagreed with the file they named.

## 🆕 Trend 39 — `p441` **Five of the twelve BSD payloads in this industry's teaching tier carry no title line, so every title-keyed licence tool reports them as UNKNOWN — and the tier they sit in is the one a university actually runs**

🔵 `Trend 37` found the supply chain shipping a licence **name** without a licence **text**.
`Trend 38` found that a tool which *declines* and a tool which *clears* produce the same
green. 🟢 `Trend 39` is the third member of that family and the most mechanical: **a
complete, unambiguous grant that no title-keyed tool can classify at all.**

🔴 **The measurement, first-hand, 2026-10-25.** Every BSD row this base publishes was probed
and graded clause-by-clause — **12 payloads across 11 repositories**. Five carry **no title
line**: they open on `Copyright (c) …` and go straight into `Redistribution and use in source
and binary forms`. Four of the five are **complete BSD-3 grants**:

| repository | payload | what a title-keyed tool sees |
|---|---|---|
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 1 475 B, complete BSD-3 | 🔴 no family |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 1 512 B, complete BSD-3 | 🔴 no family |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 1 531 B, complete BSD-3 | 🔴 no family |
| [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 2 819 B, BSD-3 **+ branding + CLA** | 🔴 no family |

🔴 **That is 1 in 3 of the tier, and the tier is not peripheral.** `jupyterhub` and `nbgrader`
are how a cohort gets identical compute and how assignments are released, collected, graded
and returned. A procurement review that runs a title-keyed scanner over this stack gets
`UNKNOWN` on the two most load-bearing components and a clean `BSD-3-Clause` on the
peripheral ones — **the opposite of the ranking a buyer needs.**

🟢 **The structural reason is worth more than the four rows.** GitHub's licence picker emits
a title; a maintainer pasting the OSI text does not. So the title is a property of **how the
file was created**, not of the grant — and any instrument keyed on it is measuring
authoring history. The grant itself is in the clauses, and the clauses were uniform across
all 11 complete payloads measured here (164 B → 2 819 B).

🔴 **And one family cannot be resolved from its body at all.** BSD-2 and BSD-3 differ in
exactly one clause, and it is a clause a grant-checker grades. Resolve the variant from it
and a **BSD-3 truncated at that clause** grades as a complete BSD-2 — a false clearance on
the precise shape the check exists to catch. 🔵 The generalisable rule, for every family and
every tool: **ask what the payload DECLARES that is independent of the clauses you are
grading.** GPL declares `version 3` in its operative text; BSD declares its variant in a
title line or not at all; and when there is no independent declaration, declining is the only
correct answer. Mechanism, controls and mutation results: `compose/code/p441-bsd-variant/README.md`.

### 🟡 The second half of this trend is about the research channel, not the code

🔵 `p440` recorded the regulatory channel as **saturated** after four regional legs returned
zero new facts. 🟡 `p441` ran nine legs and the refinement is sharp: **saturation is at the
STATUTE tier.** Four facts had zero prior mentions on this base and all four are
sub-statutory — Arkansas `H.B. 1958` (authorised-use policies, named human decision-maker),
Illinois `S.B. 1920` (state-board guidance due 1 July 2026), Austria's **Schoolpackage AI**
pilot programme, Singapore's **AI for Fun** elective modules.

🟢 **The instruction that follows, for successors and for engagement teams:** a statute names
a *deadline*; a programme names a *buyer*. Ask **which programme funds the pilot**, not what
the law requires — the law is already on `intel/market.md` and has been for nine passes.

🔴 **One channel is now declared unusable rather than re-bought.** The agentic-AI-in-education
market-size leg returned **$2.1 B (2026) → $3 B by 2034 at 4.5 % CAGR** and **$1.72 B (2025) →
$27.23 B by 2034 at 35.92 %** in the same search: a 9× divergence on one horizon. 🔵 Neither
figure is carried. A number that arrives with a 9× sibling is not evidence, and the next pass
should spend the leg elsewhere.

## 🆕 Trend 38 — `p440` **"Unknown" and "fine" render identically in every licence report in this industry, and the copyleft tier is where the difference is worth the most**

🔵 `Trend 37` (`p439`) established that the supply chain ships a licence **name** without
a licence **text**, and that every scanner reads the name. 🟢 `p440` measured the
*second* half of that failure, and it is the half a vendor's dashboard is built to hide:
**what an instrument does when it cannot answer.**

🔴 **The number.** This base's own grant-presence instrument, shipped one pass earlier and
working correctly, returned `GRANT-UNCALIBRATED` for **101 of 218** licence payloads —
46 %. Not wrong: *declining*, because it carried clause profiles for MIT, Apache-2.0 and
ISC only. 🔴 **And the declined set was not a random 46 %.** It was GPL (40), AGPL (22),
BSD (14), MPL (9), EPL (9) and LGPL (7) — **the entire copyleft tier**, which in
education is Moodle, Open edX, Canvas, Chamilo, Frappe LMS, BigBlueButton, OpenEduCat and
every SIS a LATAM ministry runs. 🔵 The instrument was most confident exactly where the
industry's exposure is smallest, and silent exactly where it is largest.

🟢 **After profiling the GPL family the remainder falls to 39 of 218 — and 10 payloads
move from "not judged" to "not a grant".** Seven of the ten are AGPL. They range from
287 B to 3 000 B under filenames like `agpl-3.0.txt`, against a real AGPL-3.0 of
34 523 B. 🔴 **None of them was a new defect.** They sat on this base for passes, inside a
verdict that reads, in any report that aggregates it, exactly like a pass.

**Why this is a trend about the industry and not a note about one tool:**

- 🔴 **The three-way answer is almost never rendered.** `PRESENT` / `ABSENT` /
  `NOT ASSESSED` collapses to two columns in every dashboard, SBOM summary and
  procurement spreadsheet this base has read. A row that says *"AGPL-3.0 ✓"* means "the
  title said AGPL-3.0", and the tick is supplied by the renderer.
- 🔴 **Copyleft is where the collapse costs most, and it is the direction nobody
  checks.** A truncated MIT payload costs an attribution line. A payload that names
  AGPL-3.0 and carries none of its clauses is a repository whose **§13 source-offer
  obligation is unresolved** — and the party who discovers that is the client who has
  already deployed it over a network.
- 🔴 **Version-blindness is the same failure one level down.** `GPL` is not a licence;
  GPL-2.0 and GPL-3.0 are, and they differ on the question that decides hosted
  deployments. Measured here: a complete GPL-2.0 licence lacks **four of GPL-3.0's six**
  operative clauses. Any tool that grades "GPL" against one text is wrong about the
  other, and in education the GPL-2.0 estate is concentrated in **one region's** SIS
  tier — so the error is not evenly distributed, it lands on LATAM.
- 🟢 **The honest instrument is the one that says it cannot tell.** `LGPL-3.0`
  incorporates GPL-3.0 **by reference by design**, so profiling it with GPL-3.0's clauses
  would mark every valid LGPL payload as a non-grant — true, and useless. `p440`
  declines on LGPL and registers why (`Gap 440-B`) rather than shipping a confident
  wrong answer about **BigBlueButton** and **OpenEduCat**.

🟢 **What to sell.** The artefact is a **three-column** component clearance report —
*verdict · the clauses actually found · what was not assessed and why* — with the
uncalibrated set published rather than suppressed. 🔵 `Pattern AQ` specifies the
clearance gate and `Pattern AR` makes it a CI artefact; `Pattern AS` (this pass) wires the
copyleft-specific read into both. A
client who has never seen the third column has never seen their real exposure, and in
this industry the third column is where their LMS lives.

---

## 🆕 Trend 37 — `p439` **The AI supply chain has learned to ship a licence NAME without a licence TEXT, and every scanner in the industry reads the name**

🔵 **The one-sentence trend.** As AI code generation and template scaffolding become the
default way a repository starts, the `LICENSE` file is increasingly **inherited furniture**
rather than an authored act — and the inherited artefact is often a *pointer* to a licence, or
a template vendor's own notice, instead of the grant the repository needs. 🔴 Measured in
live education supply this pass, not inferred.

**The specimen, and it is ordinary rather than exotic.**
[`spragginsdesigns/ai-tutor-webapp`](https://github.com/spragginsdesigns/ai-tutor-webapp)
ships `LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28` @ `963dfa9c55c7`. Titled Apache-2.0.
Graded by this base's own census: `scan_verdict = PERMISSIVE`, `stock = True`,
🔴 `needs_a_human = False`. Read, it is the Apache-2.0 **APPENDIX notice** — *"You may obtain a
copy of the License at"* a URL — and the holder it names is 🔴 **Vercel, Inc.**: the Next.js
template's notice, carried unchanged into a tutor application. Nothing in the repository
grants anything over the code its author actually wrote.

**Why this is a trend and not an anecdote — three independent observations from one hour:**

1. 🔴 **The deep tail of the discovery channel is mostly ungranted.** Of **23** new addresses
   at `ai-tutor` ranks 61–80 and `education-ai` ranks 21–40, **10 (43 %) carry no licence
   payload of any kind**. Supply is being produced far faster than it is being licensed.
2. 🔴 **Payload reuse is now visible at the byte level.** `Devanik21/AI-Nano-Course-Generator`
   and `Devanik21/FluentFlow` carry a **byte-identical** payload (`1e4635354929`) naming a
   holder, `Debanik21`, that **matches no GitHub account** — one letter off the owner. The
   notice obligation cannot be discharged against it. The same shape appeared at `p433`
   (`dmoshehun-prog` shipping `virgiliojr94`'s copyright line).
3. 🔴 **The class is already everywhere in this base's own corpus and nobody had joined the
   facts.** `make grant-presence-census`: of **218** titled payloads, **29** carry no granting
   words — **24 licence payloads plus 5 registry-metadata files** — and 🔴 **23 of them grade
   `stock = True, needs_a_human = False`.**

**What it means commercially, which is the part a client pays for.** A licence *scan* answers
"what is this called?" A licence *read* answers "what may we do, and what do we owe?" These
have been treated as the same question because for a decade the name implied the text.
🔴 **That implication is breaking.** Two obligations cannot be discharged from a by-reference
payload at all:

- **Apache-2.0 §4(a)** requires a redistributor to **give recipients a copy of the License**.
  A repository holding only the pointer has not done it, so the duty lands on whoever vendors
  it next — on an engagement, the client.
- **MIT's notice obligation** requires reproducing a holder name. Where that name is a
  template vendor or a misspelling, there is no name to reproduce that means anything.

🟢 **The defensible position, and it is cheap.** Ask the question of **clauses, not bytes**:
are the words that perform the grant present? That is `Gap 439-A`'s instrument
(`make gate-grant-presence`, 19 controls). 🔵 A byte floor is the tempting shortcut and this
base's own corpus refutes it — BSD stock payloads run **221 B → 1 514 B**, because BSD-0,
BSD-2 and BSD-3 are three lengths under one family name, so any single floor either misses a
truncated BSD-3 or condemns every valid BSD-0.

🔴 **And the tooling lesson is not "nobody thought of this" — it is that the fix did not
travel.** `P1065` on this base settled in pass 254 that **a pointer to a licence is not a
grant**, and `pass258-content-licence-family` implements the predicate by the right method.
🔴 It covers **Creative Commons content licences only**. The predicates that grade MIT,
Apache-2.0 and BSD — the families a client redistributes — never inherited it. 🔵 For a studio
reading this trend the transferable point is the one this base keeps paying for: **a licence
correction implemented in one classifier is not a capability of your pipeline.** Ask which
instrument *writes the verdict*, and whether the rule reaches it.

🟡 **How this trend connects to `Trend 36`.** `Trend 36` (`p438`) found that licence tooling
has learned to **detect** a modified grant and not to **escalate** one. 🔴 `Trend 37` is the
harder half: an **absent** grant is not detected at all, because every "is this stock?"
predicate in common use asks about the title, the family and the restrictions — and none of
them asks whether the granting text is in the file. 🔵 Together they are one trend seen from
two sides: **licence tooling matured against hand-written licences and the supply chain has
stopped hand-writing them.**

---

## 🆕 Trend 36 — `p438` Licence tooling has learned to **detect** a modified grant and not to **escalate** one, and the gap is widest exactly where the AI supply chain is growing

🟢 **The datum, measured on this base's own instruments rather than a vendor's.** One call to
`bespoke_census.grade()` on a new education specimen returns, in a single row,
`p1054_verdict = MIT-BODY-PLUS:unclassified-addition` **and** `needs_a_human = no`. Over the
**238** licence payloads committed under `compose/code/**/fixtures/`, **9** carry an addition
verdict and 🔴 **7 of those 9 are routed `needs_a_human = no`** — including `p427`'s own
two-family specimen, the payload this base wrote a 24-control gate about because it carries a
notice obligation of two. 🔴 A second instrument, `p427`'s `conjunctive_grant.classify()`,
returns `scope: None` on the same payload because every entry in its `SCOPE_MARKERS` is an
English phrase, and the clause is in Chinese.

🔵 **Why this is a trend and not a bug report.** The pattern holds across three generations of
tooling on this base, and the direction is consistent: **detection capability keeps growing
and the escalation surface does not.** `p228`'s shelf gate graded families. `p341` added a
title-form and an addition column. `p427` added conjunctive families. `p382` added subtrees.
Every one of those instruments **widened what can be seen**; `needs_a_human` — the one
function whose docstring says it produces *"the rows a consultancy must not clear from a
scanner's output alone"* — still reads the same three inputs it was written with: an English
restriction hit, a bespoke title, an unreadable payload. 🔴 **The industry shape is the same
one**: SBOM and licence-scanning tools report an SPDX identifier per file, and an SPDX
identifier is exactly the column that says `MIT` here.

🟢 **What makes 2026 the year it starts to bite.** The AI layer on an education engagement is
no longer three large dependencies; it is dozens of small permissive repositories, and
`p438`'s own census shows where they come from: the **tail** of the topic listings (0 new at
ranks 1–20, 7 new at ranks 41–60), written by individual authors, in their own language,
often in the last ninety days. 🔴 Those are precisely the payloads most likely to be a stock
text **plus a sentence the author added by hand** — and least likely to have been read by
anyone. **1 of the 9 addresses graded this pass (11 %) carried such a clause**, and the clause
shifted content-copyright liability onto the operator.

🔴 **The consequence that reaches a client, stated plainly.** A scanner report saying *"MIT,
cleared"* and a payload saying *"you carry the copyright liability for the material you feed
this"* are the same row. On an education engagement the material is textbooks and the operator
is the school or the ministry. 🟢 **The defensible position is a three-column clearance** —
family, addition column, and a human read of any bytes above the family's stock band, in the
payload's own language — now standing on `repos/foundations.md` and wired as a step in
`Pattern AQ`.

🟡 **What would refute this trend**: an addition column that routes to escalation by default
(the one-disjunct fix priced as `Gap 438-A`), or a measurement showing the addition class is
confined to sub-20 ★ repositories and therefore never reaches production. 🔵 The second is
testable and **this base cannot currently claim it**: the 7 un-escalated payloads in the
census include components already on these shelves, not only this pass's tail rows.


## 🆕 Trend 35 — `p437` Regulatory change now outpaces the open-source tooling built to track it, and the tools **fail confidently**

🟢 **The datum**: of five permissive EU-AI-Act compliance repositories graded first-hand this
pass, **two independently hardcode `2026-08-02`** as the high-risk enforcement deadline —
the date superseded by Regulation (EU) 2026/1744, which moved Annex III (education among them)
to **2 December 2027**. Neither repository contains a single reference to the amending
regulation. Both **assert the stale value in their own test suites**.

🔴 One of the two is `ark-forge/mcp-eu-ai-act`, which this base shelved at `p436` and wired
into `compose/patterns.md` as its `Obligation check` step. **The KB was shipping a recipe whose
compliance oracle contradicted the KB's own market intelligence.**

🔵 **Why this is a trend and not a one-off bug.** Three properties make it structural:

| axis | an ordinary stale dependency | a stale **regulatory** dependency |
|---|---|---|
| how it fails | throws, or drifts visibly | 🔴 returns a confident, well-formatted, **wrong** answer |
| what the test suite does | catches the regression | 🔴 **pins the error in place** — the wrong date is the expected value |
| who notices | CI | 🔴 nobody, until a client acts on the deadline |
| what screening catches it | version pinning, dependabot | 🔴 **none of licence, stars, recency or activity** |

🟢 **The two repositories share no code and no authors.** That is what makes it convergent
rather than coincidental: the ecosystem absorbed the original AI Act timeline, encoded it as a
constant, wrote tests around the constant, and then the law moved. Every project that did its
job carefully in 2025 is now carefully wrong.

### 🔴 The second-order effect, which is the commercially dangerous one

A stale deadline is not symmetric. `2026-08-02` is **in the past**, so these tools report that
a conformity deadline **has already been missed**:

- `ark-forge/mcp-eu-ai-act` `tests/test_compliance_roadmap.py:252` records that once that date
  passed, roadmap generation moved behind the paid plan — 🔴 **the stale date is load-bearing
  for a commercial funnel**, which is a reason it is unlikely to be fixed quickly.
- An education client told its Annex III obligations lapsed in August 2026 will either buy
  remediation it does not need, or conclude the regime is unenforced and disengage. Both
  outcomes are worse than no tool.

🟢 **The defensible position, and it is a sellable one.** Globant should treat
regulatory constants as **versioned data with a provenance claim**, never as code constants:
a date in a compliance artefact cites the instrument that set it (`Art. 113 as amended by
Reg. (EU) 2026/1744`), the way `tomdxb0004/eu-ai-act-risk-checker` does at `engine.js:32`.
🔵 That is the single discriminator between the correct and incorrect tools found this pass —
not architecture, not licence, not maturity. **Citation-carrying constants are the control.**

🟡 **The bound on this trend, stated.** Five repositories is a small sample, and all five are
EU-AI-Act tools; this pass did not test whether the same staleness affects education-specific
instruments (state guidance trackers, UNESCO frameworks). 🔴 That is the obvious next
measurement, and it is worth taking — this base's own regional shelves are themselves
collections of dated regulatory constants, which makes the KB a candidate for exactly the
defect it just found in someone else's code.

## 🆕 Trend 34 — `p436` In the two largest APAC school systems, AI in education has become a **teacher-licensing** question, not a curriculum question

🟢 **The datum**: China's 《"人工智能+教育"行动计划》 (`教科信〔2026〕1号`, 2026-04-02) states
that AI is to be written **into the teacher-qualification examination and certification**
(将人工智能纳入教师资格考试和认证内容), alongside bringing AI education **into local curriculum
systems** with mandated per-stage class hours.

🔵 **Why this is a trend and not a fact.** Every other instrument on these shelves regulates the
*system* — what software may decide, what data it may hold, which decisions need a human. A
licensing requirement regulates the **workforce**, and it behaves differently in three ways:

| axis | a system rule | a licensing rule |
|---|---|---|
| what it creates | a compliance obligation on a vendor | **standing demand** from every teacher-training institution |
| how it decays | superseded when the rule changes | **does not decay** — it is in the credential |
| who buys | the ministry or the district | **universities, normal schools, certification bodies** |

🟢 **Corroboration on the same axis, from a different jurisdiction and a different pass**: the
UAE's Cabinet AI curriculum (`p435`) is paired with **~22 000 educators to be trained**, and
India's CBSE mandate (`p435`) runs to a **2029 board examination**. 🔵 **Three of the four
largest APAC mandates are enablement programmes with a workforce number attached.**

🟡 **The counter-case is Japan, and it sharpens rather than weakens the trend**: MEXT's school
guideline is still **Ver. 2.0 (2024-12-26)** with Ver. 2.1 in committee since 2026-06-30. Where
there is no mandate there is no workforce number — so the two systems now need **opposite**
offers: compliance-and-enablement in China, and in Japan a voluntary-adoption case that has to
survive without a regulatory forcing function.

🔴 **Citation limit**: `moe.gov.cn` and `mext.go.jp` are unreachable from this host; both legs
rest on ~10 consistent secondary mirrors. Strong, and still secondary (`Gap 436-C`).

## 🆕 Trend 35 — `p436` A knowledge base's **own citations** decay faster than the repositories they point at, and nothing in this industry measures that either

🔵 **`Trend 9` established that a permissive licence has a shelf life.** `p436` measured a second
kind of decay on the same tree, and it is faster and less visible:

| decay channel | measured rate | instrument that sees it |
|---|---|---|
| a permissive grant going stale (`Trend 9`) | 195 of 1 449 older than two years (13.5 %) | 🟢 `gate-recency` |
| a shelf **row** silently deleted | **176** claimed promotions on no live row | 🟢 `gate-promotion-ledger` (`p436`) |
| a **citation** whose referent is gone | **110 of 464 register citations (23.7 %)** | 🔴 **nothing, before `p436`** |

🔴 **The second and third rows are self-inflicted**, which is what makes this a trend worth a
client conversation rather than housekeeping. The mechanism is ordinary: a full-file rewrite is
the cheapest way to keep a long document readable, and it is also a silent delete. On this tree a
rewrite at **pass 90** removed the rows defining `P527`, `P543` and `P599` **without taking an
`archive/` snapshot**, so 80 of the 110 dead citations are recoverable only from `git log -S`.

🟢 **The generalisable lesson for any client knowledge system**: an append-only log and a curated
shelf decay at completely different rates. `p436` measured **0** drops from this base's two
append-only shelves and **176** from its curated ones. 🔵 **So the architecture, not the
discipline, is what preserved the evidence** — the curated shelves were maintained by the same
passes that lost 176 rows.

🔵 **What to sell from this**: any "AI knowledge base" engagement needs a **join** between the
claim and the artefact, re-run on every write. Not a review process — a gate. `p436`'s is three
controls and 22 offline tests (`compose/code/p436-promotion-ledger/`), and it caught **three
defects in its own first builds** before publication.

# 📈 Trends — Education AI

> Current trends, re-measured each pass. Trends 1–8 are the standing set; 9–11 were added
> or amended on 2026-10-25 from first-hand measurement.

## 🆕 Trend 32 — `p435` Restriction in education has a **second axis**, and it is the learner's AGE, not the decision's autonomy

`Trend 31` (`p434`) found four jurisdictions on three continents converged on one operative
predicate: **AI as the operative basis of a learner decision with no human able to
intervene**. That is an *autonomy* test, and one architecture — human-in-the-loop, staged
artefacts, a recorded approval — serves all four. 🆕 **`p435` adds a fifth jurisdiction that
does not fit that shape at all.**

### The measurement

| Jurisdiction | Instrument | Axis | Effect |
|---|---|---|---|
| 🆕 **Norway** | PM Støre's announcement, **19 June 2026**, in force at the start of the **2026–27 school year** (late August) | 🔴 **AGE** | Near-total prohibition of generative AI for **grades 1–7 (ages 6–13)**; **grades 8–10 only under direct teacher supervision** |
| **NYCPS** (largest US district) | 2K-8 moratorium, with an exemption for assistive tech under an already-signed plan | 🔴 **AGE** | Student-facing generative AI barred below a grade floor |
| **Vietnam** | Decision **33/2026/QĐ-TTg**, sectoral compliance **1 Sep 2027** | 🟡 AUTONOMY | 46 high-risk categories, three in education |
| **EU** | Annex III via Regulation (EU) 2026/1744 → **2 Dec 2027**; Article 50 live since 2026-08-02 | 🟡 AUTONOMY | Grading, admissions, proctoring as high-risk |
| **Oklahoma / Maryland** | state statutes | 🟡 AUTONOMY | Human oversight; AI may not be the sole basis of a decision |

### 🔴 Why the two axes are not interchangeable, and what it costs to confuse them

An **autonomy** rule is satisfied by *architecture*: insert a human, stage the artefact,
record the approval, and the same build ships in Hanoi, Brussels and Oklahoma City. 🔴 **An
age rule cannot be satisfied by architecture at all.** No amount of human-in-the-loop makes
a generative tutor lawful for a Norwegian eight-year-old, because the rule is addressed to
**who the user is**, not to **how the output is used**.

🔵 **This is the same category error `p434` untangled inside NYCPS**, one level up. There,
*developing* an IEP and *delivering* an accommodation were read as one subject and they are
two. Here, *restricting the decision* and *restricting the audience* are being read as one
regulatory trend and they are two, with different remedies and different costs.

### 🟢 The engineering consequence: an age gate is a first-class requirement

| Requirement | Autonomy axis | Age axis |
|---|---|---|
| Human-in-the-loop on every learner-affecting output | 🟢 required | 🔵 insufficient on its own |
| Staged draft → human approval → record | 🟢 required | 🔵 insufficient on its own |
| **Per-learner age or grade band, enforced at the model boundary** | 🔵 optional | 🔴 **required** |
| **Teacher-supervision mode as a distinct runtime state** | 🔵 optional | 🔴 **required** (Norway's grades 8–10, exactly) |
| Roster-sourced age data, with its own retention rule | 🔵 optional | 🔴 required — and it is student PII |

🔴 **The trap, named:** an age gate needs the learner's age, which means the build now
processes a protected attribute it previously did not — in the EU under GDPR, in the US
under FERPA and COPPA, and in California under AB 1159's bar on training against student
data. **A compliance feature that creates a new data-protection exposure is the most common
way this goes wrong**, and the mitigation is that the age band must come from the roster
system of record and never be inferred, stored longer than the session, or sent to the
model provider.

### 🟢 Why this is commercially *good* news, stated without softening

🔵 **Both Norway and NYCPS exempt the same thing**: supervised use for older learners, and
delivery of accommodations under an existing plan. 🟢 **And both leave the entire
teacher-facing surface untouched** — lesson planning, differentiation, drafting, marking
support, administration. `Pattern AM` (the teacher-facing courseware factory, legal in NYC
*because* no student touches the model) is the architecture that clears an age restriction
by construction, and it now clears two instruments rather than one.

🔴 **What it closes:** any student-facing tutor pitch into Norwegian primary education, from
late August 2026. That is not a configuration change — it is a market that is shut, and a
proposal that does not say so is wrong rather than optimistic.

🟡 **Grade:** multiple consistent secondaries on Norway (AACRAO among them), **no primary
read** — `regjeringen.no` and `udir.no` are unreachable from this host, which is the same
ceiling `Gap 433-C` records for every government primary on these shelves. 🔵 Norway's own
directorate publishes code here under Apache-2.0
([`Utdanningsdirektoratet/PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public)),
so the **supply** side of this jurisdiction is first-hand even where the **policy** side is
not.

## 🆕 Trend 33 — `p435` A permissive licence has a measurable shelf life now, and in education **59 % of the supply is permissive while 20 % has no licence at all**

`Trend 9` asserted that a permissive licence has a shelf life and that nothing in this
industry measures it. `Trend 13` asserted that the supply has a currency problem. 🟢 **Both
are now measured, on this base's own corpus, from two channels that need no API access.**

### The licence distribution of education's visible open-source supply

All **2 450** addresses this base had recorded and never promoted, each grant read
first-hand off the repository's own payload on 2026-10-25:

| arm | n | share | what it means for a build |
|---|---|---|---|
| 🟢 **MIT** | 1 022 | 41.7 % | build on, ship, relicense the derivative |
| 🟢 **Apache-2.0** | 330 | 13.5 % | build on, with a patent grant and a NOTICE duty |
| 🟢 BSD / ISC / CC0 / ECL-2.0 / Unlicense | 97 | 4.0 % | build on |
| 🔴 **`NO-GRANT`** | **500** | **20.4 %** | **all rights reserved — not usable, and no badge says so** |
| 🔴 GPL / AGPL / LGPL | 329 | 13.4 % | integrate across a process boundary; never vendor |
| 🟡 CC-BY-NC-SA, CC-BY, PolyForm, BUSL, SSPL, MPL, EPL, EUPL | 89 | 3.6 % | read the specific terms; several bar commercial use |
| 🟡 UNRECOGNISED | 83 | 3.4 % | a real payload no classifier here names — a human must read it |

🔴 **The `NO-GRANT` arm is the finding.** One address in five in education's visible supply
has **no licence file on any of eight paths, on either `main` or `master`**. 🔵 This is not
the same as "unclear licensing": it is the absence of a grant, which defaults to all rights
reserved. 🔴 **And it is invisible to the channel most teams use** — a GitHub licence badge,
a package manifest, or a directory listing. `Trend 29` already showed GitHub's `license`
field failing in both directions; this puts a denominator under it.

### The currency distribution, from a channel `make` can reach

    git clone --depth 1 --bare --filter=tree:0 https://github.com/<slug>   # ~0.5 s, ~270 KB

| HEAD commit age (the 1 449 permissive addresses) | n | share |
|---|---|---|
| 🟢 0–30 d | **627** | 43.3 % |
| 31–90 d | 233 | 16.1 % |
| 91–180 d | 141 | 9.7 % |
| 181–365 d | 137 | 9.5 % |
| 1–2 y | 116 | 8.0 % |
| 🔴 > 2 y | **195** | **13.5 %** |

🟢 **43 % of the permissive supply committed this month.** 🔴 **13.5 % has not been touched
in two years** and is, for procurement purposes, archived — while carrying exactly the same
MIT badge as the 43 %.

### 🔵 Why the channel matters as much as the number

A star count is the usual proxy for "is this alive", and on this host it is **unobtainable
for a third-party repository**: `api.github.com` answers 200 and is authenticated, but
returns **403 per repository** with the body *"GitHub access to this repository is not
enabled for this session"*. 🔴 **No egress allowlist can fix a per-repository authorization
boundary across 1 449 repositories.** 🟢 The HEAD-date channel has none of that problem, is
reproducible from a `make` target, and measures the thing that actually matters — **whether
anyone is still maintaining it** — rather than how many people once bookmarked it.

🔵 **The practical rule this yields:** when qualifying an open-source base in education,
read the **payload** for the grant and the **HEAD date** for the life. Both are one request.
Neither is a badge.

## 🆕 Trend 31 — `p434` Four jurisdictions on three continents have converged on the **same predicate**, and it is a software-architecture requirement rather than a compliance checkbox

🟢 **The finding.** This pass's four regional legs were run for adoption and players, and what
came back from three of them was one sentence in four different legal traditions. The regulated
object is not *AI in education*. It is **AI as the operative basis of a decision about a learner,
without a human who can intervene**:

| Jurisdiction | Instrument | The operative predicate |
|---|---|---|
| **Vietnam** (APAC) | Decision **33/2026/QĐ-TTg**, under AI Law **134/2025/QH15** + Decree 142/2026/NĐ-CP | Automated testing/assessment is high-risk where the output is used **as the official result** of learner evaluation; requires human supervision, control **and the ability to intervene while the system operates** |
| **Oklahoma, Maryland** (NA, state) | 2026 session statutes | Human oversight required; AI barred as the **sole basis** for a high-stakes student decision |
| **Charleston County, NYCPS** (NA, district) | District policy | AI not the **sole basis**; NYCPS goes further — special-education documents **must be developed by qualified professionals** |
| **EU** (EMEA) | AI Act Annex III + Regulation (EU) 2026/1744 | Education access and assessment are high-risk: risk management, data governance, **human oversight**, conformity assessment |

🔵 **Why this is a trend and not a list.** Four bodies with no coordination, no shared legal
tradition and opposite political economies wrote the same operative test. That is convergence, and
convergence is what makes an architecture *portable* — the rarest property in a market whose
standing description on this file (`Trend 3`) is **regulatory divergence**.

🟢 **So `Trend 3` is now half wrong, and the half that is wrong is the commercially useful half.**
Divergence is real in **scope** — who is covered, which grades, which subjects, what the penalties
are — and a single global *configuration* remains non-viable. But at the level of **mechanism**
the rules agree, which means one architecture satisfies all four:

1. the model **proposes**; it never commits;
2. a qualified human **approves**, and the identity and timestamp of that approval are **recorded**;
3. the operative record is written by **human action** into the authorised system of record;
4. the human can **intervene while the system runs**, not only after it finishes (Vietnam's clause
   is the strictest and therefore the one to build to).

🔴 **The trap, and it is the reason this is worth a trend rather than a line.** Draft-and-sign
satisfies predicates 1–4 **only where the regulated act is the DECISION.** Where a rule is
addressed instead to **who may develop the document**, human sign-off cures nothing — the drafting
itself is the prohibited act. 🔴 **That case is now measured and it is in the largest US school
district**: NYCPS's red tier bars **IEP and 504 plan development** outright (`Gap 433-B`, closed
this pass). 🔵 **So the architectural question to ask of every jurisdiction is not "do we have a
human in the loop?" but "is the regulated act the decision, or the drafting?"** — those need
different products, and `compose/patterns.md` `Pattern AL` now carries the split.

🟢 **What this is worth in a pitch.** The four-point architecture above is a **reusable compliance
asset**: built once, it is defensible in Hanoi, Brussels, Oklahoma City and Charleston on the same
evidence. 🔵 Two rows already on `agents/top.md` implement it today —
[`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp)
(draft for human sign-off **by default**) and
[`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent)
(`WAITING_REVIEW` with a **recorded** approve/reject) — both MIT. The compliance story is not a
document to write; it is two MIT repositories to wire together.

🔴 **The grade on the evidence, stated so nobody over-cites it.** Every regulatory cell in the
table is **corroborated across independent secondaries and not read in the official text**:
`Gap 433-C`'s egress ceiling is unchanged and was re-measured this pass. Vietnam's sectoral
compliance deadline of **1 September 2027** (education, healthcare, finance) is 🆕 new to this
file and carries the same grade.

## 🆕 Trend 30 — `p433` In North America the **district**, not the state, is now the layer that decides whether a build is legal

Every regulatory read on these shelves has been organised by **state**: 134 bills across 31
states, California AB 1159, Oklahoma and Maryland on human oversight, Ohio HB 96 and Tennessee
SB 1711 on policy mandates, Alabama HB 329 on graduation. That framing is now **the wrong unit for
a build decision**, and this pass can say why with three cases rather than one.

**What the states actually did.** Read the mandates together and a pattern appears: the states
that legislated mostly legislated *procedure*. Ohio and Tennessee require districts **to write
their own AI policies** — Ohio's deadline was **1 July 2026** and has passed. 35+ states publish
**guidance**. Oklahoma and Maryland set a *standard* ("not the sole basis") rather than a
prohibition. **A state telling every district to write a policy is a state declining to write
one.** The binding text ends up one level down, and by statutory design.

**What the districts did with that delegation.** They prohibited things, specifically and
unevenly:

| District | Instrument | What it bars |
|---|---|---|
| **New York City** | 2026-27 guidance, enacted **2026-09-02** | Student-facing generative AI, **grades 2K-8** (~600,000 students); **companion chatbots in every grade**, high school included. Preliminary (March 2026) red tier was reported to bar grading, discipline, counselling, placement **and special-education / 504 plan development**. 🆕 `p434`: **CONFIRMED in the current guidance** — the *"Red: Do Not Proceed"* tier names **IEP and 504 plan development** (*"All special education documents are developed by qualified professionals"*, citing IDEA and **Chancellor's Regulation A-710**). `Gap 433-B` **CLOSED, restrictively.** The IEP/504 *exemption* in the moratorium is a different subject — student-facing assistive tech under an existing plan — not a permission to draft one |
| **Charleston County** | district policy | Discipline, placement, **special-education determination** |
| **Katy ISD** | district policy | Generative chatbots K-6, scaffolded access to grade 12 |

🔴 **The three do not agree with each other, and none of them is a state rule.** NYC draws its
line at **grade 8** and adds an all-grades companion-chatbot ban; Katy ISD draws it at **grade 6**;
Charleston County draws it by **decision type** rather than by grade. A vendor compliant in Texas
is non-compliant in New York on the same product.

**Why this is a trend and not a list.** The delegation is *structural*: Ohio and Tennessee
**require** per-district policy, so the number of binding, mutually inconsistent AI rules in US
K-12 grows with the number of districts — roughly **13,000** of them — not with the number of
states. State-level tracking, which is what every tracker and every vendor summary does, is
measuring the layer that chose not to decide.

**What it changes in a build, concretely:**

1. **Student-facing vs teacher-facing stops being a product decision and becomes a
   configuration axis.** `Trend` guidance on this file already said *"student-facing optional
   should be an architectural switch from day one"*. NYC makes it unavoidable: the same deployment
   must run teacher-facing-only in grades 2K-8 and limited-student-facing in high school, **in one
   district**. A product that cannot be switched per grade band cannot be sold to NYC at all.
2. **Grade band becomes a first-class policy input**, alongside jurisdiction. Not a setting in an
   admin screen — a constraint the agent layer enforces and logs.
3. **Companion-chatbot shape is separately regulated from AI generally.** NYC bars companion
   chatbots in **every** grade while permitting teacher-facing AI. A persistent-persona tutor and a
   task-scoped assistant are now **different regulatory objects** even though they are the same
   technology, which is an argument for building the task-scoped one.
4. **Due diligence moves from statute to district policy.** `Pattern AL` now carries this as a
   go/no-go in week 1 rather than a formality.

🔵 **The honest limit on this trend.** All three district instruments are read from secondary
reporting; `Gap 433-C` records that no government primary is reachable from this host, so **none
of the three was read in its official text**. The *structure* of the argument — states delegating
by statute, districts prohibiting unevenly — rests on the Ohio and Tennessee mandates, which are
themselves corroborated across independent trackers. 🔴 Three districts is also not a census: this
is a pattern with three data points and a stated mechanism, not a measured rate across 13,000
districts. **What would strengthen it:** a sweep of the twenty largest US districts' AI policies.
No instrument on this base does that, and this pass did not build one.

## 🆕 Trend 28 — `p432` Regulatory intensity and open-source supply are **inversely** correlated in education, and special education is the proof

Every other trend on this file reads the market from the demand side. This one reads it from the
supply side and finds the opposite of what a market should do.

Rank education's surfaces by how hard the law constrains them, and special education is first in
North America by a wide margin: IDEA and §504 make the individualised education program a
**statutory instrument** with mandated timelines, mandated team composition and a mandated human
decision. Oklahoma and Maryland bar AI as the sole basis for a high-stakes student decision;
Charleston County names special-education determination explicitly. There is no surface in this
industry where "an agent drafts, a human signs" is more clearly *required* rather than merely
advisable.

Now rank the same surfaces by open-source supply. Measured this pass:

| surface | established open-source bases | ceiling |
|---|---|---|
| tutoring | DeepTutor, OATutor, OpenTutor, Bloom, Study-Mate, tutor-gpt, … | **42 610 ★** |
| LMS / platform | Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, Chamilo, … | institutional scale |
| LMS agents (MCP) | ~40 addresses across Canvas, Moodle, Classroom, Blackboard, D2L | hundreds of ★ |
| evaluation (`p431`) | tutorbench, tutor_gym, MathTutorBench | low hundreds |
| **special education / IEP** | **none** | **1 ★** |

584 addresses match the category and the top 30 by recency are all ≤ 5 ★. Three MIT tools exist;
they were created on 2026-10-14, 2026-10-23 and (the parent corpus) maintained to 2026-10-24.

**Why the inversion happens, and it is not mysterious.** Open source in education is built by the
people who can ship it — researchers, platform engineers, teachers automating their own marking.
A statutory workflow cannot be shipped by any of them alone: it needs district authorisation, a
system of record, a privacy review and professional liability. So the hardest-regulated surface is
the one hobbyist supply cannot reach, and the commercial market (PowerSchool Special Programs,
Frontline, SEIS) owns it uncontested.

**What it means commercially — and this is the actionable half.** The inverse correlation is a map
of where a services studio is *structurally* advantaged. Globant can supply exactly the things the
open-source channel cannot: the district relationship, the authorisation path, the audit trail and
the liability posture. On tutoring, Globant competes with a 42 k-star project; on IEP workflow,
there is no incumbent open base at all, and the three MIT seeds that exist are fork-and-own by
construction.

🔴 **The honest counterweight, stated so no deck overstates this.** No incumbent also means no
validation: no benchmark, no reference deployment, no second contributor on any of the three
addresses, and no evaluation harness that scores IEP goal quality (`p431`'s evaluation tier does
not reach this category). A first engagement here is a build, not an integration, and it must be
priced and sold as one.

🔵 **Prediction this base can be held to:** if the inversion is structural rather than a sampling
artefact, the special-education tier will still have no address above ~50 ★ in six months, while
tutoring adds another order of magnitude. Re-measure and record either way.

---

## 🆕 Trend 29 — `p432` GitHub's `license` field is a detector, not a verdict — and it failed in **both** directions in one eleven-repo sample

This base already carries three licence-trap trends: `Trend 6` (the permissive frontier runs
across the stack), `Trend 9` (a permissive licence has a shelf life) and `Trend 27` (a grant with
no title, a title with no grant). `Trend 29` is narrower and more mechanical, and it invalidates a
shortcut that is tempting precisely because it is cheap.

Two of eleven addresses measured this pass returned `license: NOASSERTION` ("Other") from the
GitHub API. **Neither was unlicensed.** Reading the payload at the pinned SHA resolved them to two
real licences at opposite ends of the commercial spectrum:

| Address | API said | Payload says, at HEAD | Commercial consequence |
|---|---|---|---|
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | `NOASSERTION` | **AGPL-3.0-or-later** · `LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f` | 🔴 Strong network copyleft. Cannot be vendored into a client deliverable. |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `NOASSERTION` | **CC BY-SA 4.0** · `LICENSE` 1 229 B · `40db9b472090` @ `135d6275e7db` | 🟡 Commercial use **and** adaptation expressly permitted — with a ShareAlike obligation on derivatives. |

**Why the detector abstained, in both cases for a formatting reason rather than a legal one.**
AlloFlow's grant sits behind a project title line and an SPDX header (`AGPL-3.0-or-later`) instead
of the stock licence title; the skills repo ships a short CC BY-SA notice-and-summary rather than
the full legal code. Both are perfectly valid grants. Neither matches the templates
`licensee` scores against.

**The three failure modes this produces, all of which cost money:**
1. **`NOASSERTION` read as "no licence"** → a usable base (CC BY-SA, commercially permitted) is
   discarded. A cost of omission, invisible in any audit.
2. **`NOASSERTION` read as "probably fine, it's on GitHub"** → AGPL-3.0 enters a hosted
   deliverable. This is the expensive one.
3. **A roundup's unsourced claim substituted for the file** → one article we read asserted
   "CC BY-SA 4.0" without citing the payload and happened to be right. The same article would have
   read identically if it were wrong.

**The rule, and it costs seconds.** `NOASSERTION` is not a value — it is a *flag to read the file*.
`git ls-remote` for the SHA, fetch the payload at that SHA, size + `sha256` it, read the first
twenty lines. And "no licence" is only ever established by `git ls-tree -r` over the whole tree:
that is how `grasped-dev/staircase` (0 of 33 files) and
`eakarsu/ai-special-education-iep-compliance` (0 of 29 files) were confirmed ungranted this pass,
rather than by a missing-file guess at one candidate path.

🔵 **New obligation family on these shelves.** CC BY-SA 4.0 is the first *content* ShareAlike grant
to land on a build-relevant row. `Trend 11` recorded data licences (ODbL on `os-taxonomy`);
ShareAlike-on-prompts is a third category again, and it bites a studio hardest where the
deliverable *is* text: a skill pack, a prompt library, a curriculum corpus. A pack derived from
those 165 skills must ship under CC BY-SA 4.0 — publishable, not proprietary. Decide that before
the statement of work, not after.

---

## 🆕 Trend 26 — `p431` The evaluation layer arrived, and it is permissive — which moves the sellable unit from *adoption* to *evidence*

For many passes this file carried `Trend 8` as a standing, unclosed **measurement gap**: this base
could supply tutoring agents but could not name the instrument that scores them. Measured
first-hand on 2026-10-25, **that gap closes on the tutoring side**:

| Harness | Grant | Maintained | What it scores |
|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 (code) | 🟢 commit 2026-10-25 | Scenario-based pedagogical failure + **regression** after a fix |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | 🔴 silent since 2025-09-10 | A model as **tutor** and as **simulated student**, inside real ITSs |

**Why this is a trend and not an inventory note.** `Trend 1` says adoption is finished and
governance is the market; `Trend 2` says procurement is being rewired around **evidence**. Both have
pointed at a deliverable this base could not actually build, because *“our tutor is pedagogically
sound”* was an assertion with no instrument behind it. With an MIT harness that binds to
`CAHLR/OATutor` — already on this base's verified shelf — and `pykt-toolkit` (MIT) underneath for
knowledge tracing, **tutor → measurement → evaluation is MIT end to end.**

🟢 **What that changes commercially.** The sellable unit stops being the tutor and becomes the
**evidence pack**: a scored baseline, a regression suite, and a re-test after each change. That is
the artefact HolonIQ's “evidence of improved learning” expectation, the EU's Article 50 transparency
duty, and a US district's procurement review each separately ask for — **one deliverable, three
jurisdictions**, which is `Trend 3`'s divergence problem answered rather than absorbed.

🔴 **The half that did not arrive, and it is the regulated half.** Everything measured scores
**tutoring**. **Nothing open scores grading.** The one grading-side candidate
([`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader)) is non-commercial by clause 2 of its
licence. Meanwhile NA (Oklahoma, Maryland: no high-stakes AI decisions without human oversight),
EMEA (Annex III: assessment is high-risk) and APAC (Vietnam: automated assessment on the high-risk
list) all regulate **assessment** hardest. **The most exposed surface is the one with no harness.**
Tracked as `Gap 431-C`; it is now the most valuable open gap in this base.

## 🆕 Trend 27 — `p431` The licence trap inverted: a grant with no title, and a title with no grant, in the same eleven-repo sample

`Trend 25` says a string matched as though it were a meaning is this base's most productive error
class. This pass produced **both directions of that error at once**, which is worth separating out
because the two need *different* instruments:

| Direction | Address | What a naive read returns | What the payload says |
|---|---|---|---|
| **Grant without title** | `Teachable-AI-Lab/tutor_gym` | `UNKNOWN` — the payload never contains the string `MIT License`; it opens at `Copyright 2025 …` | 🟢 **Verbatim MIT**, fully permissive |
| **Title without grant** | `sdrangan/llmgrader` | `MIT` — the file is named `LICENSE` and its first grant sentence is the MIT one, word for word | 🔴 **“PySilicon Research License”** — clause 2 forbids commercial use |

🔵 **The practical consequence: no single cheap check is sound.** A title sweep false-negatives the
first row and false-positives the second. A byte-size heuristic fails too — `llmgrader` is 1 224 B
against the stock MIT ~1 069 B, a 155 B difference that looks like a longer copyright line. A
`sha256` sweep catches the second only *after* someone has read it once and recorded the digest.

**The only instrument that is correct on both is reading the operative clauses.** For a studio this
is a cost line, not a philosophy: **budget one human licence read per address you intend to ship**,
and let the digest sweep do what it is actually good at — detecting *change* at a known address
between passes, which is how `p429` caught the `pengusto` relicensing within 24 hours.

🟡 **A third variant, same family:** `eth-lre/MathTutorBench` has **no licence file at all**, and a
README that cites CC-BY-4.0 in a badge and CC-BY-**SA**-4.0 in its licence section. Here even
reading does not settle it — the repository contradicts itself, so the honest record is
*ungranted*, not *probably CC*.

## 🆕 `p430` · 2026-10-25 — **Three trends added from first-hand measurement: a permissive licence has a SHELF LIFE (`Trend 9`), education's permissive supply is in the agent layer and not the platform layer (`Trend 10`), and DATA licences have arrived in education (`Trend 11`).**

## 🆕 Trend 9 — A permissive licence has a shelf life, and nothing in this industry measures it

The sharpest finding of 2026-10-25, and it generalises well beyond education.
`pengusto/google-classroom-mcp` was read as **MIT** by three separate passes
(2026-10-03, 2026-10-20, 2026-10-21). Every one of those readings was **correct when
taken**. On 2026-10-23 the maintainer relicensed to a proprietary **"Pengusto Commercial
License 1.0"**, effective 2026-10-24, whose §3 requires a paid agreement from
*"an educational institution or training provider, whether nonprofit or commercial"* — by
name, the exact buyer in this industry.

🔴 **The failure mode is not a wrong reading; it is a stale one.** A dependency inventory
that records `licence: MIT` with no re-read date will keep asserting MIT indefinitely.
Badges, package manifests and MCP directories all lagged the change.

🟢 **The practice that follows, and it is cheap:** read the licence payload at the commit
SHA you are actually consuming, record the SHA and a digest alongside the family, and
re-read before any engagement commits. On this pass the whole 24-repo sweep cost minutes.
Digest equality is also a *discovery* instrument: the abandoned MIT bytes
(1 145 B, `a01639b20880`) were found alive at `vTanco/google-classroom-mcp`, so the lane
was recovered rather than written off.

## 🆕 Trend 10 — Education's permissive supply is in the agent layer, and the platform layer is closed to it

Re-measured in full on 2026-10-25 across ten platforms and fourteen agents.

- **Platform tier:** 7 of 10 are copyleft — Moodle (GPL-3.0), Open edX (AGPL-3.0),
  Chamilo (GPL-3.0), eXeLearning (AGPL-3.0), Frappe LMS (AGPL-3.0), BigBlueButton
  (LGPL-3.0), OpenEduCat (LGPL-3.0). Only **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) and
  **Sakai** (ECL-2.0) are permissive.
- **Agent / MCP tier:** **14 of 14** verified rows are MIT, Apache-2.0 or BSD-3.

🟢 **This is a structural fact an engagement can be designed around**, not a complaint: put
the AI in the agent layer, talk to the platform over its API or component SDK
(`openedx/XBlock`, Apache-2.0, is the supported seam), and no copyleft obligation reaches
the client's IP. Building AI *into* the platform inherits its licence.

## 🆕 Trend 11 — Data licences are arriving in education, and they bite differently

`withmarbleapp/os-taxonomy` — the one genuinely new trending in-domain address this pass,
a 1 590-topic curriculum graph mapped to NGSS and Common Core — is **ODbL**, not a code
licence. Share-alike attaches to *derived databases*. A client's curriculum graph built on
it inherits the obligation.

🟡 As curriculum knowledge graphs become the substrate for adaptive learning, **licence
review in education has to cover data, not just code**. A code-only audit passes this repo
and misses the only obligation it carries.

---

## Trend 1 — Adoption is finished. Governance is the market.

**88–95% of students and faculty already use AI; 26–54% can name a governing policy.**
That gap, not the adoption curve, is what 2026–27 budget buys.

- Coursera (n=4,200, 5 countries): **95%** using AI academically, **26%** of educators report a
  formal institutional policy.
- EDUCAUSE 2026: only **54%** are aware of *any* policy or guideline.
- Ellucian (n=779): institutional adoption **49% → 66%** year on year, with **data privacy the top
  barrier**.
- Digital Education Council (n=45,398, 35 countries): **88%** of students, **77%** of faculty.

- 🆕 `p384` **UNESCO IESALC** (n=**200 institutions, 19 countries**, Sept 2026): **87%** of LAC
  higher-ed institutions use AI in at least one area — **74%** in teaching and learning, **57%** in
  research — against **26%** with a formal AI strategy. 🟢 **An independent, institutional source
  landing on the same 26%** as Coursera's educator-reported figure, in a different region with a
  different method. The governance gap is no longer an inference from one survey; it replicates.
- 🆕 **OECD TALIS 2024** puts teacher AI use at **~50%+** in Brazil, Chile, Colombia and Costa Rica
  against an **OECD average of 36%**; Uruguay's **Ceibal** reports **75%** of public-school
  teachers. 🔵 Practitioner uptake is running ahead of the OECD mean in LATAM — the governance gap
  is widest exactly where adoption is fastest, which is the opposite of the usual assumption.

**So:** stop selling introduction. Sell policy-to-configuration, audit trails and a governed
gateway. The shadow-AI estate already exists on every campus. 🟢 And sell it **hardest in LATAM**,
not last — the 87%/26% split there is the widest measured in this file.

## Trend 2 — The ROI reckoning arrived, and procurement is being rewired around evidence

- **~80%** of institutions are investing in AI; **29%** of CTOs say it met or exceeded ROI
  expectations (Inside Higher Ed / Hanover).
- **~7 in 10 provosts** use AI weekly themselves; **1 in 10** report a centralised institutional
  strategy. Personal adoption has outrun institutional capability.
- The **US Department of Education's "Dear Colleague" letter** tells states to evaluate ed-tech by
  **measurable learning outcomes rather than screen time**, and to put **evidence requirements into
  procurement**.
- **US/Canada faculty intent to keep using AI fell 76% → 67%** in one year.

**So:** a before/after measurement on the client's own subject mix is becoming a procurement
precondition, not a nice-to-have. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
MMLU and GSM8K are all MIT; there is no licence reason not to ship this with every engagement.

## Trend 3 — Regulatory divergence hardened in 2026. One global configuration is no longer viable.

Four regimes moved in four different directions in a single year:

| region | 2026 direction |
|---|---|
| **EU** | **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) pushed high-risk education systems from 2 Aug 2026 to **2 Dec 2027** — while **Art. 50 transparency still starts 2 Aug 2026** and **Art. 4 AI literacy has bound every school since 2 Feb 2025**. Emotion recognition in education: prohibited. 🆕 `p385` **The nearest date is neither of those: machine-readable marking of AI-generated content on systems ALREADY on the market is due 2 Dec 2026.** Annex I (AI embedded in regulated products) moves to **2 Aug 2028**. |
| **US** | No federal rule; **134+ bills across 31 states**, **33–35 states** with guidance, and binding district-policy mandates (Idaho SB 1227 effective 1 Jul 2026; Oklahoma SB 1734 by 2027-28). |
| **India / China** | **Content labelling and provenance**: India's amended IT Rules from **20 Feb 2026**; China's labelling measures from **1 Sep 2025** (988 services filed by 30 Jun 2026). |
| **Vietnam / Brazil / Mexico** | **Sectoral high-risk designation**: Vietnam names education among six high-risk sectors; Brazil's PL 2.338/2023 reportedly covers student selection; Mexico replicates the EU risk model. |

**So:** regional configuration is now a product requirement. The same tutor needs provenance
watermarking for India, a transparency notice for the EU, a prohibited-uses lockout for DC, and a
teacher-facing-only mode for ANZ and Brazil.

🆕 `p385` **Two corrections to how this trend gets sold.** First, **the EU deferral is widely
misread as breathing room.** It defers the *high-risk* regime; it defers nothing for a system already
deployed, which owes machine-readable marking on **2 Dec 2026**. A client told "the EU moved to 2027"
and nothing else has been misinformed about the only date within the current budget year. Second,
**employment-adjacent AI is separating from student-facing AI as its own regulated surface**:
**Illinois SB 2909** restricts AI in *teacher* evaluation from **1 Jan 2027**, where DC had only a
non-mandatory ban. A product that evaluates staff is a different compliance object from one that
teaches learners, and the two are still being scoped as one in most pitches.

## Trend 4 — Restriction is a real countertrend, not noise

For two years the only direction was adoption. In 2026 the brake appeared:

- **District of Columbia** 2026-27 policy bans AI from **grading, discipline, IEP decisions and
  teacher evaluations** — four of the highest-value automation targets.
- **Ipsos Education Monitor 2026:** **Australia and New Zealand show the highest support for
  banning AI in schools**, while Asian markets show the lowest. One company, two opposite mandates.
- **European Schools:** **no** generative AI tool approved for system-wide use.
- 🟢 **CONFIRMED at `p433`** (held 🔴 `UNCONFIRMED` from `p386`): the **New York City moratorium**
  on student-facing generative AI was **enacted 2026-09-02** for the 2026-27 school year, grades
  **2K-8**, ~600,000 students, with **companion chatbots barred in every grade**. **It holds — the
  largest US district has gone the other way**, which is no longer a conditional.

**So:** "student-facing optional" should be an architectural switch from day one, not a retrofit.
A product that cannot run teacher-facing-only is unsellable in a growing share of the market.

## Trend 5 — Teacher-facing is beating student-facing where growth is fastest

HolonIQ's **2026 LATAM EdTech 100** finds regional AI positioning concentrated in **teacher-facing
instructional tools rather than consumer tutoring** — Teachy (Brazil) in lesson preparation, Ginia
(Mexico) in employability. The regulation points the same way: Brazil's draft law targets
**student selection**, DC bans AI in grading and discipline, ANZ sentiment is restrictive.

**So:** the market and the regulator agree for once. Lesson preparation, assessment drafting,
feedback generation and administrative load carry the growth and avoid the hot zone.

## Trend 6 — The permissive-licence frontier runs *across* the stack, not along it

Measured first-hand this pass over 58 live repositories:

- **Platform tier is copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, Chamilo
  GPL-3.0, ILIAS GPL-3.0, Tutor AGPL-3.0, Frappe LMS AGPL-3.0, Sakai ECL-2.0, Opencast ECL-2.0,
  OpenEduCat LGPL-3.0, H5P GPL-3.0.
- **Exactly one permissive major LMS**: **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT),
  Apache-2.0** — and no roundup we read mentions it.
- **Agent tier is permissive almost throughout**: MIT / Apache-2.0 / BSD-3.

**So:** the architecture follows from the licences. Compose permissive agents **over** a copyleft
platform across **LTI 1.3**, **MCP** or web services — never fork the platform. The interop boundary
is a legal artefact as much as a technical one.

## Trend 7 — MCP reached the LMS, and that is genuinely new

As of 2026 the LMS is addressable by agents without a fork:

- **Moodle's own plugin directory** carries **`webservice_mcp`**, exposing Moodle's external
  functions as **MCP tools over JSON-RPC 2.0** — **Moodle 4.5–5.2**, latest release
  **23 Jul 2026**, gated on the `webservice/mcp:use` capability.
- **Canvas** is served by community MIT servers ([r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp),
  fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp)).
- 🔴 **No official server from Instructure or Moodle HQ**, and two of the most-advertised community
  Canvas/Moodle servers are **unlicensed** — see [`agents/top.md`](../agents/top.md).
- 🆕 `p387` **27 distinct education MCP server slugs are shelved** on
  [`agents/top.md`](../agents/top.md) — re-derived by this base's own `recount` instrument, which
  was runnable this pass for the first time in several (the figure stood at **12** here while the
  shelf had grown to 27). Across both agent shelves **MCP reaches **6 distinct LMS platforms**** —
  Canvas, Moodle, Google Classroom, Blackboard, Brightspace/D2L and Open edX. The cumulative
  harvest behind that is lopsided: **35 Canvas servers and 20 Moodle**, against **2 for Open edX**.
- 🔴 🆕 `p387` **A correction this shelf owed since `p386`, and did not carry.** The bullet above
  used to end *"Blackboard has 9 with not one verified grant and D2L has 6 with the only one
  checked ungranted"* — and concluded that a permissive server on either platform *"would be a real
  contribution."* `p386` probed all fifteen addresses and found **6 MIT grants on Blackboard and 6
  on D2L**; it corrected [`agents/top.md`](../agents/top.md) and **left this sentence standing**.
  🔵 The live claim is: on Canvas and Moodle the work is *selection*; on Blackboard and D2L the
  grants exist and the missing thing is **tenancy** — every granted server there authenticates as
  the signed-in student (see `compose/patterns.md` **Pattern N**, and `Gap 387-A`).

**So:** the integration cost of an LMS-aware agent dropped by an order of magnitude this year, and
the remaining risk moved from engineering to licensing.

## Trend 8 — Measurement gap in this pass, stated rather than papered over

**No popularity metric is published this pass.** Every star channel was closed in this sandbox:
`api.github.com` 403, `github.com` HTML 403, `img.shields.io` blocked, `api.star-history.com`
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated across several industries**; carrying unverifiable numbers forward would
repeat that error. Licence, default ref and liveness **were** verified first-hand for all 58 live
addresses — see [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

**So:** rank by licence permissiveness, maintenance signal and fit. Popularity was never the
decision criterion for a studio engagement anyway.

🟢 🆕 `p387` **Partially closed — and by a channel, not by a workaround.** "Maintenance signal" was
the one criterion in that sentence this base could not actually measure. It can now: **package
registries publish dates**, and 26 education packages are dated in
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv). 🔴 **Still open:** repository
commit activity, contributor counts and issue latency (all behind `api.github.com`, 403), and the
many shelf entries that are **not published packages at all** — for those, publication is absent
rather than old, which is itself worth telling a client.

## Trend 9 — 🆕 `p384` The curriculum-data layer arrived, and its licence is a *database* licence

**Every adaptive-learning pitch rests on knowing what a learner must master before the next topic.
Until this pass, no shelf here held that artefact. Now one does — and it is not licensed like code.**

[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) `v1` publishes **1,930
micro-topics** and **4,102 prerequisite edges** as a DAG — each edge tagged `hard`/`soft` with a
one-line reason — over **9 subjects**, aligned to **NGSS, Common Core, the UK National Curriculum**
and the Australian curriculum. Its grant, read first-hand at `main/LICENSE` (25,289 B), is the
**Open Data Commons Open Database License (ODbL)**. There is **no separate code grant**.

**Why this is a trend and not just a row.** Every licence question these shelves have answered so
far was a **copyright** question about code: can we link to it, can we ship closed extensions. ODbL
is a **share-alike database right**, and it draws its line in a different place:

- **§4.3 — a *Produced Work*** (the tutor's output: a lesson plan, a next-topic choice, an
  explanation) needs **an attribution notice and nothing else**. 🟢 This is the permissive path.
- **§4.4 — a *Derivative Database*** (the client's topics merged in, standards remapped, the graph
  re-cut) must be publicly used **only** under ODbL, a later ODbL, or a compatible licence. §4.4(b)
  is explicit that extracting *"the whole or a Substantial part of the Contents into a new
  database"* **is** a Derivative Database. 🔴 This is the trap, and it is the thing a studio would
  naturally do next.

🔴 **A licence scanner pointed at code will not see this at all.** Neither will a licence badge:
ODbL is not in the permissive/copyleft taxonomy these shelves have been using, so the row cannot be
classified green or red — it is **green on one axis and red on the other, depending on what you
ship**. `Pattern L` was built for the case where a badge misreports a code grant; this is the case
where the *category* is wrong.

**So:** three concrete consequences.
1. **Ground on it, do not fork it.** Keep client curriculum data in a separate store joined at
   query time, so the taxonomy stays an **input** rather than a component of the deliverable. That
   is **Pattern H** in [`compose/patterns.md`](../compose/patterns.md).
2. **Add a data-rights question to intake.** Alongside "what licence is the code", ask "what rights
   govern the **data** we ground on". Education runs on standards, item banks and curriculum maps —
   this will not be the last ODbL/CC-BY-SA artefact on these shelves.
3. **Check coverage before promising it.** The maintainers state their own gap: teaching research
   covers **1,049** topics (Science and Mathematics) and **881 topics have none**. A
   research-backed-guidance claim is true for roughly half the graph.

## Trend 10 — 🆕 `p388` The parent is the unserved persona in education AI, and the statutes are pushing toward them

Every market map this base has built, and every roundup it has read, segments education AI into
**student-facing** and **teacher-facing** — `Trend 5` is about which of the two is growing faster.
Both categories are about people *inside* the institution. **The parent is outside it, and is the
person who actually logs into the portal.**

**The supply arrived this pass and it is not a prototype tier.**
[chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) (**MIT**, 20 tools
over **Infinite Campus / Campus Parent**, **47 published releases**) and
[chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) (**MIT**, 18 tools,
**43 releases**) are maintained, deliberately scoped to the observer surface, and built by one
maintainer working the same problem across two platforms — which is what a real need looks like
rather than a weekend demo.

**Three reasons this is a trend and not a curiosity:**

1. **The statutes are already there.** Every North American instrument this base tracks puts
   **family transparency** in the text — Oklahoma SB 1734 names it outright; Maryland's Chapter 634
   is built around guidance districts must hand down to families. Regulators keep asking
   institutions to *explain AI to parents*; nobody is building the surface that would.
2. **There is no incumbent to displace.** The parent portal is a **feature of the SIS**, not a
   market. No vendor defends it, and the SIS vendors have no incentive to open it. That is the rarest
   condition in education software, where every other surface has a 20-year incumbent.
3. **It inverts the tenancy problem instead of solving it.** `p386`'s finding — every granted LMS
   server authenticates as the signed-in user, so a studio cannot hand one to an institution — reads
   as a *defect* for student and teacher tools. For the parent it is **the correct architecture**:
   the parent's own credential, the parent's own child, no institutional tenancy required at all.

🔴 **And the boundary that defines the engagement, because it is not a licence boundary.** Hosted by a
family, these tools are a person exercising their own access. **Hosted by a studio for a district, the
identical API call becomes a FERPA-governed disclosure of an education record.** The code does not
change; the obligation does. 🔵 So the honest market shape is **two different products**: a
parent-side tool (no tenancy, no FERPA exposure, no institutional sale) and a district-side one (full
tenancy, full FERPA, a real procurement cycle). Conflating them is how this gets sold wrong.
`Pattern P` in [`compose/patterns.md`](../compose/patterns.md) is built on that split.

## Trend 11 — 🆕 `p388` Jurisdictional curriculum content is becoming the defensible layer, and it is arriving region by region

`Trend 9` recorded that a curriculum-data layer had arrived and that its licence was a **database**
licence. `p388` shows the *shape* that layer is taking, and it is not one global graph:

| region | asset | licence | what makes it local |
|---|---|---|---|
| **North America** | 🆕 [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 🟢 MIT | The **BC Ministry** K–12 curriculum in its real three-column **KDU** structure — and the **First Peoples Principles of Learning**, a provincial requirement no imported product carries |
| **LATAM** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) (`p387`) | 🟢 MIT | **BNCC** skill codes, Brazil's national curriculum, with invented codes discarded before a teacher sees them |
| **Global** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (`p384`) | 🟡 **ODbL** (database licence) | 1,590 topics / 3,221 prerequisite edges mapped to NGSS and Common Core |

**The pattern across the three:** the model is interchangeable, the *curriculum authority* is not.
A tutor that cites a BNCC code, a BC Big Idea or an NGSS standard is doing something a
general-purpose tutor **cannot** — not because its reasoning is better, but because it is anchored to
the instrument the jurisdiction grades against.

**Three consequences for an engagement:**

1. **Curriculum grounding is now demonstrable in three regions, not described in one.** `Pattern H`
   stops being a proposal and becomes a reference build with a local example in hand.
2. 🟡 **The risk on these assets is currency, not licence.** The BC server is 🟢 MIT — clean — but it
   is a **crawl** of `curriculum.gov.bc.ca`, last published **2026-03-27**. Curricula are revised on
   political timetables. **Quote the re-crawl as a maintenance line item**, and never let a client
   believe a crawl is a feed.
3. **Keep asking the data-rights question from `Trend 9`.** Two of the three assets above are code
   (MIT); one is a **database** under ODbL. "What licence is the code?" and "what rights govern the
   data we ground on?" remain two different intake questions with two different answers.

## Trend 12 — 🆕 `p388` An exhausted channel is not an exhausted supply — and "published but unreadable" is now a real category

This is a trend about **how this industry's open-source supply is actually distributed**, and it has
a direct procurement consequence.

**The discovery finding.** `p382` recorded that this industry's address supply was **exhausted**.
What was exhausted were four search-engine legs. **`registry.npmjs.org/-/v1/search` is open**, and 29
education queries returned **383 GitHub addresses absent from this entire base**, of which **22 are
granted and education-specific** — the largest single intake in this base's recorded history. 🔵 The
general lesson, and it is the third of its kind here: `p386` learned *a count of addresses is not a
count of grants*; `p387` learned *a null leg is not a null supply*; `p388` adds *an exhausted channel
is not an exhausted supply*. All three are one error — **a property of the instrument reported as a
property of the industry.**

🔵 **Why a package registry is structurally the better instrument for this industry.** A trending page
ranks by attention over days. Education tooling is **institutional, unglamorous and
low-star** — a 47-release parent-portal server for a US K-12 SIS will never trend anywhere. The
registry indexes it anyway, and returns its **entire publish history in the same call**, which
answers "is it maintained?" at the moment of discovery rather than two steps later.

🔴 **The new supply category, and it is the uncomfortable half.** Of 32 addresses probed, **6 publish
to npm from a repository that is not publicly readable** — `git ls-remote` prompts for credentials,
so the repository is **closed, not missing**. The package installs; the provenance cannot be audited.
The costliest instance is **103 published versions** of an AI-generation quiz library **with SCORM
support** ([thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)); the
most instructive is [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest
declares **`"SEE LICENSE IN LICENSE"` — pointing at a file inside a repository nobody can read.**

**So the licence-reading discipline this base built needs one more rule.** `Pattern L` clears a
repository by reading its **subtree**; for these there *is* no subtree. The rule that replaces it:
**for an npm-only dependency, the manifest is a claim and the tarball is the evidence** —
`registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves the published artefact even when the repository is
closed, and **it is the licence that actually ships**. 🔴 That is how this pass established that a
major publisher's tutoring SDK (**115 published versions**) carries **no licence at all**: not from
the repo, which is private, but from the artefact, which is not. 🔵 And the corollary a studio should
internalise: **commercial education vendors are starting to distribute as closed SaaS with an npm
veneer.** The npm scope looks like open source, installs like open source, and grants nothing.

🔵 🆕 `p391` **The channel now has a decay curve, not just a verdict.** Re-run with 32 queries of
*fresh* vocabulary (tenancy, SEN/IEP, proctoring, QTI, xAPI, OneRoster, FERPA, standards, personas):
**321** addresses absent from this base → 37 past a domain filter → 11 probed → **3 shelvable**.
That is **0.9%**, against `p388`'s **5.7%** (22 of 383). 🟢 The channel is **depleting, not
exhausted** — it still produced three rows, one of which opened a category (`Pattern W`). 🔴 But the
seam `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary.
🔴 **And the instrument nearly lied:** the first draft of the domain filter matched the query column
of its own output and "confirmed" 37 education rows that were Vercel, AWS and Storybook packages.
Caught before a shelf. *A filter that scores its own prompt is not a filter.*

## Trend 13 — 🆕 `p389` The supply has a currency problem, and it is now a number

This base has built a careful discipline about *licences* and almost none about *time*. `p387` and
`p388` both recorded that no maintenance signal was available. It was: **`git` read access is open to
every public repository**, and a blobless shallow clone returns the last commit date at the real
default ref in about a second. Sixty addresses were dated this pass.

**The distribution, which is the trend.** 58 live, 2 dead. **48 of 58 moved within 30 days**, and 17
of those were committed **on the day of the pass**. That is a healthier supply than this industry's
reputation suggests — education tooling is unglamorous, not abandoned. But **7 of 58 are past 120
days, and four of those seven carried a recommendation on these shelves**:

| stale address | days | what it was being recommended for |
|---|---|---|
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 343 | a Tier-1 tutor |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 242 | Moodle integration |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 209 | North American curriculum grounding |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 144 | Canvas integration — **and it is ungranted** |

🔵 **The general shape, and it is this base's fourth instance of one error.** `p386`: a count of
addresses is not a count of grants. `p387`: a null leg is not a null supply. `p388`: an exhausted
channel is not an exhausted supply. **`p389`: a closed popularity channel is not a closed maintenance
channel.** Four passes, one mistake — *a property of the instrument reported as a property of the
industry* — and each time the fix was to ask which channel was actually being measured.

🔴 **The procurement consequence, which outlives the instrument.** A licence tells you whether you
*may* build on something. A date tells you whether you will be **alone** on it. Those are different
risks and they price differently: an MIT repository that has not moved in eight months is a
**vendoring decision with a maintenance line in the estimate**, not an integration. Both numbers
belong in the same row of a proposal, and until this pass only one of them was here.

🟡 **And the limit, stated so the number is not over-read.** A commit date says someone pushed — not
to the branch a release is cut from, and not that the project is healthy.
[instructure/canvas-lms](https://github.com/instructure/canvas-lms) is the case in point: `master` is
175 days behind while its `stable/*` branches move, because that is how Instructure ships. A
specification or a dataset that is *finished* is not decaying either. Read the date against what the
artefact is.

## Trend 14 — 🆕 `p389` APAC has become the net exporter of open-source education AI, and the Gulf the net importer

**The supply side.** The largest education-native repository in open source is
[**OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, ~41.3k ★, from **Tsinghua
University**, committed the day of this pass, published in **JCST 2026** and validated inside the
university on **700+ students**. It is not an outlier in its region: the Tier-1 tutor shelf on
[`agents/top.md`](../agents/top.md) is now **majority APAC by origin** — DeepTutor (HKU, Apache-2.0),
ai-shifu (China, Apache-2.0), educhain (India, MIT), OpenTutor (China, MIT), Aha Tutor (China, MIT),
learn-shell (China), ChatTutor (APAC) — against one EMEA entry (mentingo, Poland) and, at Tier 1, one
North American (tutor-gpt, now 343 days stale). 🔵 **The pattern is not "China ships a lot of AI."**
It is that **the pedagogy is being designed in the repository** — mastery estimates that record
*confidence* separately from correctness, FSRS review built in, cognitive-load detection,
misconception-aware branching — in projects whose authors are university teaching groups rather than
startups. That is a supply a studio can build a practice on, and its licences are permissive.

**The demand side, created by statute rather than by procurement.** The **UAE** approved an AI
curriculum across **all public and private schools** by Cabinet decision in September 2026, with
**22,000 teachers and education professionals** to be trained, and for 2026-27 merged Design,
Innovation and Computer Science into a single subject, *Artificial Intelligence and Technology*,
KG–Grade 12. **Saudi Arabia** began a comprehensive AI curriculum across all levels of public
education in the 2025-26 academic year, led by the **National Curriculum Center** with **SDAIA**.
These are the most aggressive AI-in-education mandates anywhere: not permission to pilot, a
**compulsory subject with a teacher-training number attached**.

🔴 **And the mismatch is the opportunity.** This pass found **no Gulf-origin and no Arabic-first
open-source education agent or platform** — not one address. The region with the world's strongest
statutory demand for AI teaching material has, as far as this base can see, **no local open-source
supply at all**, while the permissive supply that does exist is EN + zh-CN. The gap is not a model
gap; it is **curriculum-grounding and language**: Arabic-first content, alignment to the UAE MoE's
seven curriculum areas, and the teacher-training surface those 22,000 professionals will be trained
on. 🟡 Recorded as an informed gap, not a finding: the searches run were English-language, and an
Arabic-language search is the obvious next leg.

## Trend 15 — 🆕 `p389` The parent surface now has a cautionary case, and it is in LATAM

`p388` added the parent/guardian persona and named **FERPA** as the line that splits a family-run
assistant from a district-hosted one. The LATAM equivalent of that line is **LGPD Article 14**, and
unlike FERPA it already has a public failure attached to it.

- **Brazil has no AI statute in force.** As of October 2026 **PL 2338/2023** — passed by the Senate
  in December 2024 — is still in the Câmara dos Deputados, with reports that the vote resumes after
  the October 2026 elections. So the binding instrument for an education engagement today is the
  **LGPD**, not an AI law.
- **Children's data has its own consent basis.** For core teaching a school generally relies on
  contract and legal obligation, but uses **beyond** that — images, communications, extracurricular
  activity — require **specific, explicit, recorded and revocable consent from a parent or guardian**
  under Art. 14. An AI parent portal is squarely in the "beyond" category.
- **The cautionary case.** In 2023 the São Paulo state education department (**SEDUC**) had its
  *Minha Escola* app installed on parents' phones without notice or consent; Data Privacy Brasil
  assessed it as a probable LGPD violation. 🔵 **This is the precise failure mode of the persona
  `p388` added** — a district-hosted parent surface deployed *to* families rather than *for* them —
  and it is the reference a LATAM client will have in mind, so bring it up first.

🟢 **What this makes defensible rather than risky.** The pattern that survives Art. 14 is the one
`Pattern P-1` already describes: the **family runs the agent and exercises its own access right**, so
no new disclosure is created. For the district-hosted variant (`P-2`), the deliverable a Brazilian
client should be sold is the **consent and revocation mechanism itself** — per-guardian, recorded,
revocable, auditable — as a first-class feature, not a checkbox. 🟡 **Mexico: informed gap.** No
education-specific AI guidance or student-data rule was found for Mexico in this pass; the general
position is a data-protection regime and no AI statute. Stated, not inferred.

## Trend 16 — 🆕 `p390` The copyleft firewall moved inside the platform, and it is a packaging decision rather than a licensing one

For several passes this shelf framed "permissive agent + copyleft platform" as a problem solved at
the **boundary**: hold the agent outside the LMS and talk to it over LTI or MCP, so no copyleft
reaches your code. That is still a valid pattern, but `p390` found the cleaner answer was in the
platforms' own packaging the whole time, and **nobody had read it per-package**:

| package | role | licence |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | the platform you deploy | 🔴 **AGPL-3.0** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | the component API your plugin imports | 🟢 **Apache-2.0** |
| [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | what you develop against | 🟢 **Apache-2.0** |
| [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) | newer core data layer | 🔴 **AGPL-3.0** |

All four read from the payload at their real default ref on **2026-10-22**; the two Apache grants are
at `LICENSE.TXT`, which is also why a badge-level or root-`LICENSE` read misses them.

**Why this is a trend and not a trivium.** It means the in-platform plugin — the deepest, most
useful integration, with full access to course state and no network hop — is **also** the one that
can stay MIT or proprietary. The industry had been treating depth of integration and licence freedom
as a trade-off, and for Open edX specifically they are not. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(MIT, Universidad Tecnológica de Pereira) has been shipping on exactly this basis.

🔴 **The trend has a sharp edge: the boundary is per-package, and it is moving.** `openedx-learning`
is the newer core data layer and it is **AGPL-3.0**. As more platform functionality migrates there,
the set of imports that keeps a plugin permissive **shrinks**. Audit the dependency list in CI, not
once at kick-off. The general rule this generalises to: **licence is a property of the package you
import, not of the organisation that publishes it** — and in education, where every major platform is
copyleft, that distinction is worth real money.

## Trend 17 — 🆕 `p390` Voice is the next interface gap, and the open-source supply has not arrived

Across seven passes these shelves accumulated tutors, graders, LMS connectors, parent portals and a
generated classroom. **Every one of them is text-first.** `p390` found exactly **one** granted
voice-first education agent in the open-source supply — [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
(MIT, Brazil, pt-BR, 15 days old, self-described as *"in development"* with no public deployment).

**Why the gap matters commercially.** Voice is not a convenience feature in this industry; it is an
access feature, and it maps onto precisely the markets with the fastest growth and the least supply:

- **Early grades**, where reading and typing fluency is the thing being taught, not assumed.
- **Shared-device and phone-only households** — the LATAM and APAC reality `Trend 10` documents.
- **Language learning**, where pronunciation *is* the assessed skill and text cannot carry it.
- **Accessibility**, which in EMEA public procurement is frequently a scored requirement rather
  than a nice-to-have.

**Why the gap is narrow rather than deep, which is the opportunity.** The hard parts are already
permissive and maintained: [`livekit/agents`](https://github.com/livekit/agents) (Apache-2.0) solves
turn detection, interruption and barge-in — the things that actually make a spoken tutor usable — and
[`mozilla/common-voice`](https://github.com/mozilla/common-voice) supplies **CC0-1.0** speech corpora
across ~130 language variants for ASR evaluation and fine-tuning. What is missing is not
infrastructure; it is **an education-grade assembly of it** — mastery model in the loop, symbolic
checking behind the arithmetic, and the biometric/disclosure posture a school can sign.
🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md) is that assembly.

🔴 **`Gap 390-A` — the informed gap, stated rather than left as silence.** The searches this pass ran
for an open-source voice or multilingual tutor in an **African or South Asian language** returned
**nothing granted and maintained**. What came back instead: one India-first multilingual *toolkit*
(not a tutor), an arXiv framework for low-cost home language learning with **no public code located**,
and a repository that teaches *Spanish to non-speakers* inside an agent CLI — which is the inverse of
a Spanish-language tutor for Spanish-speaking learners, a category error this base recorded in `p388`
and which keeps recurring in search results. 🔵 **Read this as a null result in the open-source
supply, not a null in demand** — Africa is among the fastest-growing online-education markets. For a
client engagement in those languages the honest position is: **the substrate is permissive and ready,
the localised tutor does not exist and would be built, and Common Voice is where its evaluation set
comes from.**


## Trend 18 — 🆕 `p391` Education AI is shipping as **harness extensions**, not standalone applications

Three of this base's education rows are now plugins to the *same* agent harness, by **three
unrelated maintainers**, all MIT, all published inside about ten days:

| row | what it is | published |
|---|---|---|
| [`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (`p388`, Tier 1) | narrated-blackboard adaptive tutor | npm v1.7.0, 2026-10-22 |
| [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🆕 `p391`, Tier 1) | diagnosis-first learning runtime | npm v0.1.1, 2026-10-17 |
| [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (🆕 `p391`) | K8s + OIDC multi-tenant hosting for the same harness | npm v0.10.0-rc.1, 2026-10-12 |

They are extensions to **DeepSeek Harness**, and the pattern is not harness-specific — this pass also
read [`mackt/pi-language-tutor`](https://github.com/mackt/pi-language-tutor) (MIT) as an extension to
the Pi agent. 🟢 **Why it is a trend and not a coincidence:** a harness extension inherits model
plumbing, tool calling, auth, UI shell and a distribution channel for free, so a single maintainer can
ship a credible tutor in weeks. The economics now favour the plugin over the application.

🔵 **The operational consequence, and it explains a channel result this base has hit repeatedly.** The
distribution channel for education AI is becoming **the agent harness's package registry** — which is
why `registry.npmjs.org` keeps yielding education supply while `moodle.org` has never once been
reachable *or* necessary. Looking for education AI in LMS plugin directories is looking where it was
built in 2019.

🔴 **The cost a studio inherits, stated plainly.** A harness extension is **not deployable without its
harness**. `dsh-diagnostic-tutor` requires DeepSeek Harness; adopting it means adopting that runtime,
its update cadence and its governance. For a client who cannot, the move is to copy the *structure*
(see `Pattern X`) rather than the package — which is exactly why `Pattern X` separates the pedagogy
from the runtime instead of recommending the repository wholesale.

## Trend 19 — 🆕 `p391` The standards body's reference implementation goes stale; the **vendor fork** carries the maintenance

`p390` dated [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) at 2,332
days and concluded the LTI 1.3 integration path had no installable implementation. The grant and the
dating were both right; the conclusion was wrong, because the maintained line is not at the
authoritative-looking address:

| address | last commit | registry | verdict |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **2026-10-16** | packagist `lti-1p3-tool` **v6.4.4**, 68 versions, 2026-09-23 | 🟢 **install this** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Node) | **2026-10-13** | npm `ltijs` **v7.0.7**, 207 versions, 2026-10-06 | 🟢 **install this** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 2020-06-03 | — | 🔴 spec citation only |
| [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) | 2020-06-03, **identical sha `3a192de`** | — | 🔴 the same project, renamed org |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) | 2022-11-21 | PyPI `PyLTI1p3` 2.0.0, **2022-11-20** | 🔴 genuinely dead |

🟢 **The generalisable rule:** in standards-driven education interop, the consortium publishes the
spec and a demonstration; a **vendor with production traffic** maintains the library. So when a
reference implementation dates badly, the next question is *who ships this in production* — not
*should we vendor the spec*. Check the fork network and the package registry before concluding a path
is closed.

🔴 🆕 `p392` **The "language asymmetry" half of this trend is WITHDRAWN, and withdrawing it sharpens
the rule above rather than weakening it.** `p391` closed this trend with: *"Node and PHP have
maintained LTI 1.3; Python does not… the interop edge is therefore a separate Node or PHP service in
front of the agent."* Read first-hand this pass, **Python has three**:

| address | grant | last commit | registry | role |
|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | **2026-10-20 — 2 d** | PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07 | 🟢 **in-process**, Django app + middleware |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 — 113 d | PyPI **v1.6.3**, 15 releases | 🟢 LTI 1.1 **and** 1.3 into JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | **2026-10-22 — 0 d** | PyPI `lti-consumer-xblock` **v11.4.2** | 🔴 best-maintained of the three, **copyleft** |

🟢 **And the maintainer pattern holds in Python too, which is the trend's real content.** The three
Python implementations are maintained by a **university innovation centre** (Michigan), an
**ecosystem project** (Jupyter) and a **platform vendor** (Open edX) — not by the standards body. The
rule is unchanged and now has six instances instead of four: *in standards-driven education interop,
ask who ships this in production.*

🔴 **What survives as a constraint is licence-shaped, not language-shaped**, and that is a more useful
thing to tell a client: the best-maintained Python LTI implementation is **AGPL-3.0**, the
best-maintained Node one is Apache-2.0, and the permissive Python options are smaller (26 ★ and 73 ★)
and framework-bound. The question is never *"does this language have LTI"* but *"does the maintained
implementation in my language carry a grant I can ship?"* `Gap 391-A` **CLOSED**.

## Trend 20 — 🆕 `p392` The granted proctoring supply covers the **lockdown**, not the **inference** — which is the opposite of the regulatory exposure

For four passes this base recorded proctoring as having *"no credible permissive open-source option"*
and treated that as a liability boundary to name rather than fill. Probed first-hand, the supply
exists — and its **shape** is the trend:

| component | grant | last commit | what it actually does | the AI part |
|---|---|---|---|---|
| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) | 🟢 **MIT** (1,069 B, manifest agrees) | **2026-09-28** | tab-switch, right-click, DevTools shortcuts, clipboard events, camera state, **faces**, audio loudness, **virtual-camera / loopback / screen-share detection** | 🟢 **real** — face-api on TF.js, **in the browser** |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 🔴 **CONFLICT** — Apache-2.0 payload, `ISC` manifest **and** npm | **2026-10-13**, 398 commits | blocks copy/paste/cut, right-click, selection, shortcuts; detects `tabSwitch`, `browserBlur`, `exitTab`, `fullScreen`; periodic page and webcam snapshots POSTed to an endpoint you build | 🔴 **absent** — object detection, multi-face and eye tracking are marked *"(To be Done)"* |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🔴 **AGPL-3.0** | 🆕 re-read `p392`: `master` HEAD **2026-10-22 — 0 d** (this base's harvest row said 2026-05-30; the live read is today), 253 releases | the exam **workflow** — attempts, review states, integration points | 🔴 none; it brokers a vendor |

🔵 **The asymmetry, stated as a rule:** open-source proctoring is **deterministic browser lockdown and
event telemetry**, while the **inference** — identity, gaze, multiple faces, behavioural scoring — is
either absent, roadmapped, or the proprietary service the AGPL workflow brokers. 🟢 **And the
regulatory exposure runs the other way.** Lockdown and event logs do no biometric inference: they
are not what the EU AI Act's Annex III is reaching for, and they are explainable to a student
(*"you left fullscreen at 14:03"*). The inference layer is where high-risk obligations, biometric
rules and the whole evidentiary argument live — and that is exactly the layer the permissive supply
does not have.

🟢 **So the honest advice to a client flips, and it is now sellable in both directions:** *we can
build the integrity layer you can defend — lockdown, event trail, human review — permissively and
today; the part that would flag a student automatically is the part that makes you a deployer of a
high-risk system, and neither of us should want it in v1.* 🔴 The obligation attaches to the
**deployment**, not the dependency, so an open-source grant transfers no compliance relief whatsoever.

## Trend 21 — 🆕 `p392` LATAM's public buyers are procuring AI education platforms as **subscriptions**, and no tender asks for open source

A replacement regional leg shaped like a **buyer** rather than a supplier — public-procurement
vocabulary in Spanish and Portuguese — returned five live 2026 instruments where three passes of
English, stars-sorted supply legs returned nothing: Santa Fe province (Argentina, Tender 01/26,
*subscriptions* to AI-enhanced educational cloud platforms), **OEI-Chile `OEI-LIC-1-25`** (design and
build of an AI platform for **administrative management in Chilean schools** over regulatory,
financial and operational data), UNOPS Argentina `ITB/2026/62779` (educational platform **licences**,
2+2 years), the **CIEDEPAR** consortium in Paraná (multi-municipality SaaS education management) and
Francisco Morato, SP (**R$1,924,665.00**).

🔴 **Not one of the five specifies free or open-source software.** The spend is real, the AI framing
is explicit, and the procurement shape is **product subscription**.

🔵 **Why this is a trend and not five anecdotes:** it is the demand-side mirror of *Trend 6*. This
base's whole thesis is permissive assembly, and the buyers writing the cheques are specifying
subscriptions — so the binding constraint on an open-source education engagement in LATAM is **the
specification, not the licence frontier**. 🟢 The opening is a total-cost bid against subscription
pricing, with the OEI-Chile scope (administrative management, compliance recommendations) matching the
`i-educar` + agent shape these shelves already hold; the work is to get *"or equivalent open-source
implementation"* into a specification written for a product. 🟡 Graded **`ATTRIBUTED-UNVERIFIED`** —
aggregators and news items; no official portal (COMPR.AR, ChileCompra, PNCP) is reachable here.


## Trend 22 — 🆕 `p393` The education **interoperability layer is Python** while the agent layer is TypeScript, and a one-registry sweep answers half the question

**What was measured.** `p393` opened the channel `Gap 392-C` said did not exist: `pypi.org/simple/`
under PEP 691 returns **920,784 project names in 45,189,043 B in 1.4 seconds**, unauthenticated. A
sweep of 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, 13 live and
verified first-hand.

**What came back was a layer, not a list.** Not more tutors or more agents — **plumbing**:

| standard / surface | granted Python supply found | grant |
|---|---|---|
| **LTI 1.3 / Advantage** | `openfun/django-lti-toolbox` (France Université Numérique), `Harvard-University-iCommons/django-lti-dynamic-registration` | 🟢 MIT, 🟢 MIT |
| **QTI** (assessment exchange) | `vosslab/qti_package_maker`, `Citolab/qti-convert-python` (Cito, NL) | 🟡 LGPL-3.0, 🔴 GPL-3.0 |
| **OneRoster / Caliper** | the `timeback-*` family — 🔴 **source unresolvable** | 🔴 unauditable |
| **Ed-Fi** (US K-12 data) | `edanalytics/edfi_api_client`; `Ed-Fi-Exchange-OSS/LMS-Toolkit` 🔴 archived | 🟢 Apache-2.0 ×2 |
| **LMS → agent bridge** | `Dathis/swiss-moodle-mcp`, `Snaw80/moodle-mcp` | 🟢 MIT ×2 |
| **Autograding** | `edulinq/autograder-py`; `otter-grader` already carried, now measured at **161 ★** | 🟢 MIT, 🟢 BSD-3 |

🔵 **Why this is a trend and not a haul.** The split is systematic. The **agent** layer — MCP servers
for Canvas, tutors, parent agents — is overwhelmingly **npm/TypeScript**, which is why eleven passes of
npm sweeps built a rich agent shelf. The **standards and institutional-data** layer is
**PyPI/Python**, because it lives next to the Django and Flask applications that universities and
ministries actually run (Open edX, `now-lms`, campus SIS integrations) and next to the
notebook-and-grading stack. 🔴 **A supply claim is therefore only as wide as its registry.** This base
published *"there is no maintained Python LTI 1.3 library"* (`Gap 391-A`) from a channel that
**cannot index PyPI** — and then found five.

🟢 **The rule for a studio:** one discovery channel per ecosystem, named before any absence is
published. This base's set is now npm + PyPI + Packagist (measured, 0 yield) + `git ls-remote` and
`raw.githubusercontent.com` for verification. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** —
and CRAN matters here, because `otter-grader` grades **R** and the statistics-teaching stack is
R-shaped.

🔴 **The cost of the channel, stated with it:** the dump carries **names only**, so it discovers by
token and a token is not a capability. Two of fifteen candidates were pure collisions — `proctor-ai`
is a **prompt-engineering** library, `xapi-python` is the **xStation5 broker API** — and whole keys are
unusable (`canvas` returns 146 names dominated by HTML-canvas and AWS Nova Canvas; `d2l` is
Dive-into-Deep-Learning). Discovery is cheap; **adjudication is the work**.

## Trend 23 — 🆕 `p393` A new supply class: **live releases, dead source** — and the licence claim is unauditable in principle

**The instances, found the same hour.** [`superbuilders/timeback-dev-python`](https://github.com/superbuilders/timeback-dev-python)
is the declared `Repository` of **three** actively-released PyPI packages — `timeback-qti`,
`timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last
**2026-07-18**, each declaring **MIT**, together the most complete 1EdTech client family in Python on
paper. 🔴 **The repository does not resolve for an unauthenticated clone.** Second instance:
`moodle-mcp-bridge` v1.7.0, advertising *"a Moodle site as 88 typed AI tools"* → `NmaaAlhawary/MCP-Moodle`,
also unresolvable.

🔵 **Why this is a distinct class and not a variant of an existing one.** This base already grades
three failure modes, and none of them covers this:

| class | the payload | the verdict |
|---|---|---|
| `UNGRANTED` (no licence file) | exists, is empty of a grant | read, and found wanting |
| `README-ONLY` / `MANIFEST-ONLY` | a grant **asserted** somewhere other than a payload | downgraded, because the assertion is checkable against the absence |
| 🆕 **`LIVE-RELEASES-DEAD-SOURCE`** | 🔴 **cannot be fetched at all** | **not assessable** — there is nothing to read, and no amount of care fixes it |

🔴 **The procurement consequence is sharper than it looks.** `p388`'s *"published but unreadable"* was
about a payload that says nothing; this is about a payload that **cannot be obtained**. A studio can
install these packages — pip will resolve them happily — but it **cannot warrant the licence to a
client**, because warranting a grant means having read it. And an MIT declaration in registry metadata
is a claim by the uploader, not a grant in a distributable artefact.

🟢 **What to do with it.** Evaluate in a sandbox if the capability is needed; **never ship it into a
client deliverable**; ask the publisher to open the repository, which is a cheap request and a fair
one. 🔵 And record the class, because the economics favour its growth: publishing to a registry is
free and keeping a public repository is a maintenance commitment, so **more supply will arrive this
shape**, not less.

## Trend 24 — 🆕 `p394` In the teaching stack the **delivery** layer is permissive and the **measurement** layer is copyleft, and a language boundary rides along with it

🟢 **The observation.** `p394` opened the R half of the CS-teaching stack and the licence column split
cleanly down the middle of the pedagogy:

| what it does | components | licence |
|---|---|---|
| **Deliver** the teaching loop — present, accept, grade, respond | `rstudio/gradethis` (**MIT**, 164 ★), `rstudio/learnr` (**Apache-2.0**, 738 ★), `ucbds-infra/ottr` (**BSD-3-Clause**) | 🟢 **permissive, all three** |
| **Measure** the learner — item response theory, adaptive item selection, exam generation, item analysis | `cran/exams` (**GPL-2 \| GPL-3**), `philchalmers/mirt` (**GPL >= 3**), `cran/catR` (**GPL >= 3**), `cran/TAM` (**GPL >= 2**), `ShinyItemAnalysis` (**GPL-3**) | 🔴 **copyleft, all five** |

🔵 **Why it is not a coincidence.** The delivery components are **vendor-authored** — Posit, a company
selling an R platform, and a university programme that needed its autograder to be adoptable. The
measurement components are **academic instruments**, written by psychometricians inside a GPL research
culture and in some cases decades old. **The licence tracks who paid for the code and why**, and it has
produced a split running exactly along the boundary between *product* and *science*.

🟢 **Why that is good news rather than a blocker.** The boundary falls where a studio's product
boundary has to fall anyway: own the teaching loop, reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. 🔴 **The
trap is reading it as a licence problem and swapping in a permissive psychometrics library instead.**
There is no credible permissive equivalent of `mirt` or `catR`; building one is a multi-year research
project and approximating one is how a studio ends up shipping an adaptive engine whose claims it
cannot defend. 🔵 This base already carries the symptom: `adaptive-knowledge-graph` (~350 ★) and
`OATutor` implement IRT and BKT from scratch, and `mirt` — **235 ★, committed daily** — is the thing
they are approximating.

🔵 **And the language boundary rides along with it.** `Trend 22` recorded that the agent layer is
npm/TypeScript while the standards layer is PyPI/Python. `p394` adds that the **measurement** layer is
**CRAN/R**. Three layers, three registries — and a supply claim is still only as wide as the registry
it was swept from. 🔴 **R is the worst case of the three**, because its registry is unreachable here on
**both** tools and its grants are invisible to GitHub's licence sidebar (`Gap 394-B`): five granted GPL
packages in this tier show **no licence** in the GitHub UI, because the grant lives only in
`DESCRIPTION`. **So a GitHub-UI-driven sweep does not merely under-count R supply — it reports it as
unlicensed.**

## Trend 25 — 🆕 `p394` A string matched as though it were a meaning is this base's most productive error class, and it runs in three directions

🟢 **The observation, as a count rather than an impression.** Three independently-found defects, three
different instruments, one mechanism:

| gap | instrument | direction | what the string was |
|---|---|---|---|
| `Gap 392-A` | capability-absence gate | 🔴 **over-refutes** — denies a real absence | a runtime key read as a capability |
| `Gap 393-A` | PyPI index channel | 🔴 **over-discovers** — invents supply | a package *name* read as a capability (`proctor-ai`, `xapi-python`, `canvas`, `d2l`) |
| **`P459`** 🆕 | `licence-grant-gate` | 🔴 **strips a grant** — denies a real permission | **"all rights reserved"**, line 2 of the canonical BSD template, read as a refusal |

🔵 **`P459` is the most expensive of the three and it was the last to be found**, because the other two
produce *visible* nonsense — a claim you can check, a candidate you can reject — whereas this one
produces a **false absence of a grant**, which looks exactly like diligence. A usable component is
quietly marked unshippable and nobody re-opens the question. 🟢 On these shelves its realised damage
was **nil** — no published row was graded from an untitled BSD payload, checked rather than assumed —
and its exposure was **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells.

🔴 **And the fourth instance is on this base's own shelf rather than in an instrument.**
`anastasasenov/bbmcps` sat in the Blackboard census for eight passes because its URL scheme reads
`blackboard://`. It is a shared-memory MCP server; the word is an **architectural metaphor**. So the
class does not only mis-discover and mis-refute — **it mis-files what the base already owns**, and a
census cell inherited as a count is exactly where it hides.

🟢 **The transferable rule, and it is cheap.** Before a token decides a verdict, ask what else that
token means. The gate that got this wrong already holds the right idea one screen away:
`AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`, with a comment noting each is simultaneously a
licence name and something else. 🔵 **The insight was applied to licence names and never to licence
clause text, nor to package names, nor to URL schemes.** One lexicon separating a **string** from a
**capability** would close `Gap 392-A`, `Gap 393-A` and the `bbmcps` class together — which is why
`p393` ranked that unification fifth and why `p394` ranks it **first**.

