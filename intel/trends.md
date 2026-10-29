---
industry: education
region: Global
updated: 2026-10-29
---

## 🆕 `p519` — `2026-10-29` — **🟢 THE TREND THIS PASS MEASURES IS AN ARCHITECTURAL ONE AND IT RESOLVES A STANDING DEADLOCK: the permissive/copyleft split in education software is reconciled not by picking a side but by a PACKAGE BOUNDARY, and both rungs of that boundary — LTI and SCORM — are now verified permissive on these shelves. 🔴 Second: `updated_at` is not a liveness signal, measured on sixteen rows, and the one row where it lies is the one a studio would have pitched. 🔴 Third: education is becoming a NAMED high-risk sector in statute rather than a sensitive one by interpretation. 🔴 Fourth, and it is about this base rather than the sector: fifteen passes blamed a publisher for what was the sandbox's doing.**

### 🟢 `T519-1` — The permissive/copyleft deadlock in edtech is an INTEGRATION problem, and the integration tier just turned out to be permissive

🔵 **The deadlock, as these shelves have carried it for many passes.** Every system of record in
education is copyleft — Open edX **AGPL-3.0**, Moodle **GPL-3.0**, `frappe/education` **GPL-3.0**,
`openeducat_erp` **LGPL-3.0**, `frappe/lms` **AGPL-3.0**. Every strong tutoring and content agent
is permissive. A studio asked for a **closed, client-owned** deliverable therefore appeared to face
a choice: rebuild the LMS, or accept copyleft reaching into the agent.

🟢 **The measurement that dissolves it.** Two standards runtimes were read today and both are
permissive:

| rung | repo | licence asserted `2026-10-29` | ★ / forks | `pushed_at` |
|---|---|---|---|---|
| **LTI / Common Cartridge** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | 377 / **267** | **`2026-10-29`** |
| **SCORM 1.2 / 2004** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 361 / 85 | `2026-10-28` |

🔵 **Why a package boundary is different in kind from a library boundary.** An agent that *links*
into Moodle invites the derivative-work question. An agent that **emits a SCORM package** which
Moodle *plays* does not: the interface is a file format. 🟢 And the sector has already produced the
matching emitter — `p518` shelved [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph)
(**MIT**) specifically because it **emits SCORM**. Emitter, runtime and 1,644-node curriculum
corpus all landed inside four weeks of each other.

🟢 **The trend claim, stated narrowly:** new education supply in this window is arriving
**standards-shaped** rather than platform-shaped — built to drop into whatever LMS the institution
already runs, instead of asking it to migrate. That is the opposite of the 2024–25 pattern of
all-in-one AI learning platforms, and it is what makes `P528` buildable. 🔴 **Scope:** this is read
from a handful of repos in one window, not from a population study. It is a direction, not a rate.

### 🔴 `T519-2` — `updated_at` is not a liveness signal, and the row it lies about is the row you would have sold

🟢 **Measured, not asserted.** Sixteen repositories graded by
[`compose/code/p519-liveness-fields/`](../compose/code/p519-liveness-fields/) (**21/21 controls
green**, portable under `python3 -I` from any directory):

| derived from [the TSV](../evidence/liveness-fields.2026-10-29-p519.tsv) | count |
|---|---|
| rows graded | **16** |
| `archived` | **1** |
| `STALE` (no push in >365 days, not archived) | **0** |
| rows where grading on `updated_at` would **disagree** with the sound grade | **1** |

🔴 **The one row is [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor)**: Apache-2.0,
**582★**, `archived: true`, last push **`2024-04-21`**, `updated_at` **`2026-10-12`**.

🔵 **Why a 1-in-16 error rate is the dangerous kind.** A reader that trusts `updated_at` is right
about fifteen rows. It is wrong about the archived one — and an archived, permissive,
582-star education platform is exactly the row that *looks* like a find worth proposing. 🟢 The
rule, now enforced in code: **`archived` first, then `pushed_at`. `updated_at` moves when metadata
moves and must never be read as maintenance.** This is `p518`'s `microsoft/autogen` retraction
generalised from an instance into an instrument.

### 🔴 `T519-3` — "Region" works for regulation and fails for adoption, and APAC is where it fails hardest

🟢 **The spread, on a single instrument and a single survey round** (TALIS 2024 via OECD Digital
Education Outlook 2026): 🇸🇬 Singapore **~75%** against 🇯🇵 Japan **<20%** — both APAC, **~4×
apart**, OECD average **36%**.

🔵 **So the five-value closed vocabulary this base writes `region:` from is doing two different
jobs, and only one of them works.** For **regulation** a region is real: the EU AI Act binds
EMEA as a bloc, and that is a genuine shared constraint. For **adoption** a region is an
artefact of sampling — "APAC adoption" means whichever member state the report happened to
measure. 🟢 **The discipline this pass adopts:** adoption cells are written as **ranges with their
endpoints named**, never as a regional average. See [`market.md`](market.md).

🔵 **And the same test applied to LATAM reverses a prior.** Brazil **56%**, Chile **55%**, Colombia
**53%**, Costa Rica **52%** — all four **above** the OECD average of 36%. The "LATAM lags on
adoption" assumption is not supported by the instrument that measures it.

### 🔴 `T519-4` — Education is moving from "sensitive by interpretation" to NAMED in statute, with the regulated FUNCTIONS specified

🔵 **The shift, in one comparison:**

| regime | how education is reached | what is actually regulated |
|---|---|---|
| **EU AI Act** (Annex III) | 🟡 **By interpretation of a use-case category** — an admissions tool is high-risk *because* its output affects access to education | the *consequence* of the decision |
| 🔴 **Vietnam's AI Law** | 🔴 **Education named as a high-risk sector in the statute itself** | 🔴 **Named mechanisms: automated assessment and behavioural monitoring** |

🔴 **Why naming the mechanism matters more than naming the sector.** "Education is high-risk"
leaves an architect guessing which component is in scope. *"Automated assessment and behavioural
monitoring"* tells them exactly which two components to keep out of the model's hands — and both
are components a tutoring agent acquires by default the moment it grades or tracks engagement.
🟢 **`P525`'s architecture already answers it** (the consequential decision is not the model's),
which is the useful result: a pattern built for the EU clock transfers to the Vietnamese one
without redesign.

🟡 **Declared:** Vietnam's commencement dates are **conflicted across sources** (1 March 2027 with
a six-month extension for pre-15-August-2026 systems, versus an account placing the law in force
March 2026). The *sectoral naming* is carried; the clock is not asserted.

### 🔴 `T519-5` — The channel-attribution error: fifteen passes blamed a publisher for the sandbox's behaviour

🔴 **What this base has recorded.** `Gap 483-K` and `Gap 513-D` have been filed for fifteen-plus
passes as *"EUR-Lex itself was not read"*, with `curl` **000** and `WebFetch` **ENOTFOUND** offered
as evidence about **EUR-Lex**.

🟢 **What this pass measured.** `WebFetch` was pointed at three unrelated primary publishers:

| host | result |
|---|---|
| `eur-lex.europa.eu` | 🔴 `ENOTFOUND` |
| `www.oecd.org` | 🔴 `ENOTFOUND` |
| `collimateur.uqam.ca` | 🔴 `ENOTFOUND` |

🔴 **Three publishers, one failure mode, with an explicit remedy in the error text: the host is
outside this session's allowlist.** EUR-Lex is not unreachable; **non-allowlisted hosts are**. The
gap was describing a property of the sandbox and attributing it to a publisher — which is
**exactly `Gap 511`'s class**, re-occurring on a different axis fifteen passes later.

🔵 **And the same correction applies to this pass's own ceiling.** `p518` could resolve a
`NOASSERTION` by reading the served licence file. `p519` cannot: `get_file_contents` is scoped to
this session's own repositories. 🟢 So `p519` is **strictly weaker than `p518` on the licence
axis** and says so, rather than carrying `p518`'s shelvings forward as if it had re-earned them.
**Two rows are left UNGRADEABLE and shelved nowhere** (`cn-math-taxonomy`, `canyongbs/advisingapp`)
where a pass with a raw-file channel would have settled both.

### 🟢 `T519-6` — New education agent supply is arriving LOCAL-FIRST, and that matches where the regulation is going

🟢 **Four of the six permissive agents added today are local-first or self-hostable by design** —
[`nichochar/ari`](https://github.com/nichochar/ari) (local-first, created `2026-10-18`),
[`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) (local-first, uses the school's own
curriculum), [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (self-hostable FastAPI + React),
[`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) (runs as a single file).

🔵 **Why this is a trend and not a coincidence.** Every binding instrument on
[`market.md`](market.md) pushes the same way: NYC bars AI from grading and discipline, California
**AB 1159** would bar training on student data, Quebec's new posture is governed use under
published guidelines, Vietnam names **behavioural monitoring**. 🟢 **An architecture where learner
data never leaves the institution satisfies all four without a per-jurisdiction variant** — and the
supply to build it is now permissive and on the shelf.

### 🟢 `T519-7` — The buy-side criterion has shifted from capability to evidence, on three independent issuers

🔵 Three readings, three different kinds of organisation, one direction:

- **HolonIQ** (2026 snapshot): selective acceleration, with buyers wanting **proof that products
  improve learning** — quality, persistence, well-being or job-relevant skills.
- **1EdTech**: the sector is moving **from experimentation to governance** — formal strategies
  setting oversight, compliance and evaluation; and **digital credentials** becoming a core
  mechanism for skills-based learning and hiring.
- **OECD Digital Education Outlook 2026**: institutions should move **beyond general-purpose AI
  tools toward purpose-built educational AI**.

🟢 **The commercial reading, and it is the sharpest thing on this page for a studio.** The
differentiator is no longer a better tutor. It is (a) **an evaluation story** a buyer can put in
front of a board, and (b) **governance and conformance tooling**. 🔵 LATAM quantifies the second:
**87% adoption against 26% formal strategy** (UNESCO IESALC, 200 institutions / 19 countries) — a
**61-point** deficit that is a consulting engagement, not a product gap. 🟢 And the
credentials rung now has permissive supply: [`iblai/lms`](https://github.com/iblai/lms) (**MIT**,
competency tracking + digital credentials).

## 🆕 `p518` — `2026-10-29` — **🟢 THE TREND THIS PASS MEASURES IS A LICENCE TREND, NOT A CAPABILITY ONE: the three highest-star "open" education repos found this window that a studio CANNOT ship are blocked by three DIFFERENT mechanisms — a bespoke non-OSI licence, a non-commercial CC grant, and a prose-only AGPL. 🟢 Second: new education-agent supply has gone NON-NORTH-AMERICAN, with every 2026-created agent on these shelves 🇨🇳, 🇧🇷 or 🇮🇹. 🔴 Third: the 2026 market figure is quotable again and the retraction that killed it was itself an error of units.**

### 🟢 `T518-1` — "Source-available" is displacing "open source" in high-star edtech, and the sidebar hides it

🟢 **The measurement.** Four education repositories read today, each ≥585★, each showing nothing
but a bare **"License"** link in GitHub's About sidebar because GitHub's own classifier declines
to name the grant. Each is blocked for a client deliverable, and **by a different mechanism**:

| Repo | ★ | Mechanism | What breaks |
|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | **2,050** | 🔴 **Bespoke non-OSI licence** — "CaviraOSS Community License": free for personal/educational use, *"commercial use or resale requires prior written permission"* | A client engagement is commercial use. There is no OSI grant to fall back on |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | **4,877** | 🔴 **Non-commercial Creative Commons** — `CC BY-NC 4.0` over graph, question bank, tool code *and* docs | The `-NC` clause. Permissive-looking family, non-commercial term |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 585 | 🟡 **Prose-only copyleft** — README says AGPL-3.0; the classifier does not confirm it | Strong copyleft asserted in prose, so the actual obligation is arguable rather than readable |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 922 | 🟡 **Content licence used for a code repo** — README: content under `CC BY-SA 4.0`, repo LICENSE governs "full terms" | The code/content boundary is never drawn, so neither grant is cleanly applicable |

🔵 **Why this is a trend and not four accidents.** All four are 2025–2026 repositories. The older
education projects on these shelves — Moodle, Sakai, Oppia, Kolibri, i-educar — all carry a
single, classifier-recognised SPDX grant. 🟢 **The new cohort does not**, and the common factor is
that each wants the distribution benefits of looking open while retaining a commercial claim.
🔴 **The operational consequence:** a star-count filter plus a "has a licence" filter — the two
checks most ingest pipelines actually run — admits all four.

### 🟢 `T518-2` — New education-agent supply has stopped being North American

🟢 **The measurement, from [`agents/top.md`](../agents/top.md) read today.** Every
education-specific agent on that shelf **created in 2026**:

| Agent | Created | Origin | ★ | Licence |
|---|---|---|---|---|
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `2026-03-11` | 🇨🇳 Tsinghua | 41,717 | MIT |
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | `2026-05-01` | 🇧🇷 | 36,435 | MIT |
| [`beltromatti/get-it`](https://github.com/beltromatti/get-it) | `2026-05-09` | 🇮🇹 GDG Milan | 1,138 | Apache-2.0 |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | `2026-06-24` | 🇨🇳 | 358 | MIT |
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | `2026-09-17` | 🇨🇳 | 1,249 | MIT |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | `2026-10-03` | — | 999 | MIT |
| [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | `2026-10-14` | — | 517 | MIT |

🔴 **North America's contribution to this shelf is `OATutor`** — UC Berkeley, MIT, 274★, created
**2019**. 🔵 **This inverts the usual regional story:** North America has the measured teacher
adoption (~60%, Gallup) and all of the binding 2026 legislation, while the permissive open-source
supply to serve it is being written in Shenzhen, São Paulo and Milan. 🟢 For a studio that is an
arbitrage, not a problem — the supply is MIT and Apache-2.0, so it travels.

🟡 **Honest limit on this trend.** Origin is attributed from account/organisation signals and
repo language, not from a residency check. 🔵 Two rows above are unplaced, and "created in 2026"
is a window, not a cohort — a 2024 repo that matured this year does not appear.

### 🟢 `T518-3` — The market figure was retired over a units error, and is quotable again

🔴 **What this base did.** Earlier passes read a "~3× spread across four estimates the same day"
and retired the 2026 market figure as unquotable. 🟢 **Re-read today, the spread is not in the
2026 totals** — Precedence **$9.58B**, Research and Markets **$10.6B**, Grand View **$11.4B**:
a 1.19× range across three houses. 🔴 **The fourth number was Technavio's `+$3.37B`, which is
incremental growth 2025→2030, not a market size.** Comparing it to a total produces exactly the
≈3× artefact that got the whole figure retired.

🟢 **The trend underneath, now that the units are right:** the *2026* number is close to settled
and the *disagreement has moved out-year* — $42.48B by 2030, $57.2B by 2033, $136.79B by 2035,
CAGRs 25.9%→41.5%. 🔵 Houses now differ about how long the growth lasts and whether embedded AI
revenue and corporate training count, not about today's size. 🟢 **For a studio that is good
news:** a near-term business case can be built on a defensible range, and the long-horizon
numbers should be quoted as scope-dependent rather than as forecasts.

### 🟢 `T518-4` — Governance is being written as architecture requirements, not as guidance

🟢 **The measurement.** Three instruments read this pass impose a *structural* constraint on how
an education AI system must be built, not merely a disclosure duty:

- 🇺🇸 **Oklahoma S.B. 1734** — AI is **barred as the primary basis** for high-stakes decisions such as grading or discipline. That is a requirement about where the decision lives.
- 🇪🇺 **EU AI Act, Annex III** — learner evaluation and admissions are **high-risk**, requiring documentation, conformity assessment and demonstrable **human oversight**.
- 🌐 **OECD *2026 Digital Education Outlook*** — urges institutions toward **purpose-built educational AI** rather than general-purpose tools.

🟢 **All three point at the same architecture**, and it is one a studio can build once: the
consequential decision (mastery, progression, discipline) computed by auditable deterministic
code, the model confined to explanation, drafting and dialogue, with a logged human gate at the
boundary. 🔵 **This is why `OATutor`'s Bayesian Knowledge Tracing matters out of proportion to its
274 stars** — it is the only agent on these shelves whose mastery estimate is a number you can
show a regulator. The recipe is `P525` in [`compose/patterns.md`](../compose/patterns.md).

🔵 **Contrast with the 2026 commentary trend**, which reads the year as "experimentation →
embedded infrastructure" and "experimentation → governance" (1EdTech, Campus Technology,
HolonIQ). 🟢 Those are the same movement described from the buyer's side; the three instruments
above are what it looks like in a technical spec.

### 🔴 `T518-5` — The demand-side trend axis is saturated for an eleventh consecutive window

🔴 **Searched this pass:** `AI {industry} industry trends 2026` globally plus the four regional
legs. 🔴 **Returned:** agentic AI in classrooms, governance catching up to usage, purpose-built
over general-purpose platforms, evidence-of-outcomes pressure, digital credentials for
skills-based hiring, multimodal tooling. 🟢 **All six are already recorded on this shelf from
prior passes.** 🔵 Recording the nil explicitly because an empty result and an unsearched axis
look identical in a file. 🟢 **The three trends above (`T518-1`, `-2`, `-4`) are supply- and
instrument-side, which is where this window's new information actually was.**

🔴 **One figure declined.** A widely-circulated "83% institutional adoption of AI teaching
assistants" and a "$12.3B market" appear only in vendor marketing and could not be traced to a
primary source. **Not recorded as data.**

## 🆕 `p517` — `2026-10-29` — **🟢 THE TREND THIS PASS ADDS IS MEASURABLE AND UNCOMFORTABLE: APAC open-source education supply is ABUNDANT AND TWO-THIRDS UNGRANTED — 8 of 12 repos probed carry no licence on 53 filenames in 14 languages. 🔴 That is a different failure mode from LATAM's, and it changes what "open source" means per region. 🔴 Demand-side trends saturated a TENTH time (~24 facts, 4 new). 🟢 The 2026 market figure is now demonstrably unquotable: a ~3× spread across four estimates read the same day.**

### 🟢 `T517-1` — "Open source" does not mean the same thing in APAC as in LATAM

🟢 **The measurement.** Twelve APAC-origin education repositories, probed this pass with
[`ingest/probe-grant.sh`](../ingest/probe-grant.sh) — default branch resolved, 53 grant filenames
across 14 languages:

| outcome | count |
|---|---|
| 🟢 permissively licensed (Apache-2.0 / MIT) | **4** |
| 🔴 **no grant file under any of 53 names** | **8** |

🔴 **So the modal APAC education repository is public, active, feature-complete in its README — and
carries no licence.** 🟢 **Under default copyright that means it is not usable**, however open it
looks. 🔵 Examples, each `UNRESOLVED` at its resolved default branch: `EduAgent-Platform`
(multi-agent orchestration, hybrid RAG, MCP tools), `eduAgent` (PolyU, vector RAG),
`bridge-ai-for-edu` (**Japan's national LLM project**), two Korean university course repos, one
Indonesian training repo.

🟢 **Why this is a trend and not an artifact.** It held across **four** independent language legs
and **three** national ecosystems, and it is the *opposite* of the LATAM pattern, where the supply
that eight English passes missed turned out to be cleanly licensed (`i-educar` GPL-2.0,
`bncc-dados` MIT, `bncc-benchmark` MIT + CC BY 4.0, with grants in Portuguese filenames).

🔴 **The forward-looking claim, stated as a claim:** if licensed APAC supply exists at scale it is
probably **not on GitHub** — `schoolcms` mirrors to Gitee and OSChina, and a Chinese LMS surfaced
this pass only on `gitcode.com`. 🟡 **Unverified** and logged as `Gap 517-C`; the probe cannot
reach those hosts today.

### 🟢 `T517-2` — Curriculum-grounding is becoming the product, and it is nationally specific

🔵 **`p516` established curriculum-as-data as shipping** (Brazil's BNCC as MIT open data).
🟢 **This pass shows the same instinct arriving independently in China, but bound to textbooks
rather than standards:** `AI_Tutor_Release` / `AI-Tutor` ground answers on **人教版 (PEP) textbook
PDFs**, with the README specifying that the AI *"prioritises quoting the textbook's original
wording"*, uses **Socratic questioning rather than giving answers**, and automatically collects the
knowledge points a student repeatedly gets wrong.

🟢 **The trend: tutors are differentiating on *whose* curriculum they are faithful to**, not on
model quality. 🔴 **The strategic consequence for a studio is unpleasant and worth saying:** a tutor
grounded on PEP textbooks does not transfer to BNCC, NCERT or a US state standard without
re-grounding — so *"an AI tutor"* is not one product, it is one product per curriculum authority.
🟢 **This is why `bncc-dados`-style curriculum-as-data is the higher-leverage asset**: the standard
is portable, the textbook corpus is not.

### 🔴 `T517-3` — The 2026 market figure has become unquotable, and the dispersion is the finding

🔴 **Four commercial 2026 estimates, read the same day: $3.7B, $10.6B, $11.4B**, against 2025 bases
of **$6.4B** and **$8.3B**. 🔴 One 2026 estimate sits **below** another firm's 2025 base. 🟢 **~3×
spread.** 🔵 The firms define *"AI in education"* differently — some include corporate and workforce
learning, some only K-12 and higher education.

🟢 **This is the third channel on which this base has now measured source dispersion** rather than
inheriting a number: aggregator star counts (`p515`, `p516` — 42.6K/45.2K/46K against 48.0k),
licence claims in search prose against licence bytes (`p516`, and twice this pass), and now market
sizing. 🟢 **The method generalises and should be stated as doctrine: when three sources disagree,
publish the spread and the direction, never the median.**

### 🟢 `T517-4` — Human-in-the-loop is being specified in code, not in policy decks

🟢 **A small repo with a disproportionate signal.** `yqy624/eduagent-digital-workforce` (MIT, 3★)
defines **five** education agents and gates each one *in its architecture*: grading requires
**teacher confirmation before a grade is written**; classroom vision **logs events without acting
on them**; learning analytics is **read-only and makes no final judgement**; supervision
**de-duplicates and requires manual confirmation**.

🔵 **Why that is a trend signal at 3★:** every education buyer across ten saturation passes has
asked for these guarantees, and this base has had to *specify them from scratch each time*. 🟢 The
guarantees are now appearing as **default repository structure** in new education agent projects —
which is what adoption of a norm looks like before it reaches policy documents. 🔴 **Counter-note,
kept visible:** the repo's own page calls it *"a demonstrable MVP rather than a production
system"*, so this is evidence of a design norm, not of production practice.

### 🔴 `T517-5` — Teacher enablement is the one demand trend that has never wobbled

🟢 **Ten saturation passes and this claim has moved only upward, from independent sources:** schools
offering AI professional development for teachers went **29% (early 2024) → 50% (late 2025)**;
**71%** of US teachers still report lacking AI training; only ~**10%** of institutions have formal
AI guidelines while **86%** of students across 16 countries already use AI; LATAM shows the same
shape at higher intensity (TALIS teacher use **52–56%** against the OECD's **36%**, Uruguay's Ceibal
**75%**) with only **26%** of institutions holding a formal strategy.

🟢 **The durable statement, and the only demand claim this base will put in front of a client
without a channel caveat:** *student adoption has outrun institutional capacity everywhere it has
been measured, and the gap is widening fastest where teacher use is highest.* 🔵 Everything else on
the demand axis is saturated or dispersed.


## 🆕 `p516` — `2026-10-29` — **🟢 THE TREND THIS PASS ADDS IS ABOUT THIS BASE'S OWN BLIND SPOT: a regional supply nil held for eight passes fell to a single query in Portuguese. 🔴 Demand-side trends saturated a NINTH time (~26 facts, 2 new). 🟢 Curriculum-as-data emerges as a real, shipped architecture — not a forecast.**

### 🟢 `T516-1` — Curriculum-as-data is shipping, and it reorders the adaptive-learning stack

🔵 **Until this pass, every adaptive-learning recipe on these shelves assumed the client supplies
the competency map.** 🟢 Brazil has published one as code: **`bncc-dados`** (MIT) emits the national
curriculum as **1,721 learning objectives** in JSON/SQLite/CSV **with provenance per record**,
**`bncc-pacotes`** serves it to agents over **MCP**, and **`bncc-benchmark`** measures whether a
model's curriculum claims are hallucinated. 🟢 **The significance is ordering**: factuality against
a *public standard* becomes measurable before any tutoring product is built, which inverts the usual
sequence of ship-then-evaluate. 🔵 Transferable to any jurisdiction with a published curriculum;
the Brazilian data is the reference implementation, not the asset.

### 🟢 `T516-2` — A supply nil is only as credible as the languages it was searched in

🔴 **This base ran eight consecutive passes of English-language discovery and concluded "0
LATAM-originated open-source education repositories at any star level."** 🟢 One query in
Portuguese returned five, all licence-verified from bytes — and a sixth
([`ipti/br.tag`](https://github.com/ipti/br.tag), GPL-2.0, 20★) was already on the shelves the nil
was published against. 🔴 **And the same bias sat in two other
instruments**: a licence probe that only knew English filenames (missing
`LICENSE-CODIGO.md` / `LICENSE-DADOS.md`) and a branch probe that only knew `main`/`master`
(missing `i-diario` @ `1.6`, `i-educar` @ `2.12`). 🟢 **Trend statement, for any industry KB and not
just this one: regional "there is nothing here" findings produced by English-only tooling are
systematically wrong in the direction of under-counting the Global South.** 🔴 **Live prediction:
APAC's thin supply shelf here is probably the same artifact** — it has never been probed in
Mandarin, Japanese, Korean or Hindi (`Gap 516-D`).

### 🔴 `T516-3` — Governance is the sector's binding constraint, and the gap is now measured on both sides

🟢 **The adoption/governance scissors is the most robust finding across all four regions this
pass**, and every number below was already on these shelves — which is what makes it a trend rather
than a datapoint:

| region | adoption | governance |
|---|---|---|
| LATAM | IESALC: **87%** of 200 institutions using AI in ≥1 area; **74%** in teaching and learning | only **26%** have a formal AI strategy; UNESCO: **<10%** have guidelines *and* capacity |
| North America | Gallup: **60%** of US teachers using AI | most US public schools still lack a formal student AI policy; 4 states now *mandate* district policies |
| EMEA | UNESCO: **70%** of NA+EU institutions have or are developing guidance | high-risk duties deferred to **2 Dec 2027**, so most schools are pre-compliance |
| APAC | Singapore **64.3%** vs Japan **24.7%** adoption | four incompatible regimes; Vietnam's education transition runs to **1 Sep 2027** |

🟢 **The commercial reading is consistent across regions: the buyer's pain is the policy gap, not
the capability gap.** Teachers have already adopted; institutions have not governed. 🔵 That is why
the LATAM offer sequences governance first even though LATAM now has verified buildable assets.

### 🔴 `T516-4` — Aggregator star counts are refuted a second time, independently

🔴 Three trending digests read within four days reported `DeepTutor` at **42.6K**, **45.2K** and
**46K**; the repo page read **48.0k** on `2026-10-29`. 🔴 **Dispersed across ~3.4k, all below a
ladder that has not decreased in fourteen readings.** 🟢 `p515` refuted this channel on one
datapoint; `p516` refutes it on three. **Aggregator stars are a discovery signal, never a
measurement.**

### 🟡 `T516-5` — Education remains a secondary theme in general AI trending

🔴 In the general AI open-source digests this window, education appears as a **secondary** theme;
`DeepTutor` (Apache-2.0, **48.0k★**, `v1.7.0` dated `2026.10.28`) is the only education repo at the
top of a live ranking. 🔵 The education-MCP axis is real but **small** — `tutor-mcp`, `canvas-mcp`,
`learnmcp-xapi` are the substantive entries and all are long held here; this pass's three new
addresses are ~4★-class micro-repos. 🟡 **Stated as information, not padding: the sector's open
source is concentrated in a few assets plus a long tail of very small ones.**



## 🆕 `p515` — `2026-10-28` — **🔴 NO NEW TREND WAS FOUND, AND THAT IS THE ENTRY: ~29 named facts across eight legs, one new and unverified. 🟢 But two trends on this base's own INSTRUMENT changed, and both change what later passes should do — aggregator star counts now proven to diverge from source in **both** directions (`DeepTutor` under-reported ~4% this pass, inflated in earlier cycles), and *"the API is 403"* exposed as ~16 passes of misdiagnosis for what is per-repository session scope. 🔴 Discovery yield has collapsed while internal-consistency yield has not: the scarce resource on this base is no longer information, it is AGREEMENT BETWEEN THE SHELVES. 🔴 The two gates that enforce exactly that have not run since `p511`.**

🔴 **Gate posture, stated first — and it is NOT the prior 18 denials.** The previous eighteen
passes recorded a classifier **DENIAL** (`Code from External`) on `make hooks`. 🟡 **This pass
the battery was never submitted:** every gate in `HOOK_GATES` executes `$(PY) -I` over Python
inside `compose/code/p*/` — interpreter runs over a freshly cloned third-party working tree —
and this session's standing rule is not to run interpreters over cloned repository content.
🟡 **So `p515`'s posture is a declared abstention, not a refusal received.** The distinction
matters because it is *stable*: a future pass should expect abstention, not retry-and-be-denied.
🔴 `p511`'s **45/63** remains the last gate-attested reading — now **four passes stale**.
🔵 Every figure below is named to the channel that produced it, and the one conflict this pass
resolved is resolved on a channel the refusing pass did not use.

### 🟢 What actually changed in the trend picture this pass

🔵 **No new trend was discovered, and the honest statement of that is the entry.** Four global legs
and four regional legs returned **~29 named facts, 1 of them new** (the IDB 193-solution review,
unverified — `Gap 515-D`). Seventh consecutive saturation pass. 🔴 The `ai-tutor` topic rows that
star-ranked discovery keeps surfacing are all already filed.

🟢 **Two methodological trends on this base's own instrument are worth recording as trends,
because they change what later passes should do:**

| trend | evidence this pass | consequence |
|---|---|---|
| 🟢 **Aggregator star figures diverge from source in BOTH directions** | `p514`'s trending channel put `DeepTutor` at **~46,026** against a ten-reading monotone shelf ladder ending at **47,834** and a same-day page read of **47.9k** — under-reported by ~4%. Earlier cycles recorded the opposite, pipeline-**inflated** counts. | 🔴 Aggregator stars are a discovery signal only. A star cell may be filled **only** from the page, the API, or a git-protocol read. |
| 🟢 **"The API is 403" has been a misdiagnosis for ~16 passes** | The 403 body names repository-level **session scope** and `add_repo` as its remedy — not a rate limit and not an outage. | 🔴 Stop recording an outage. Record out-of-scope, and name the repository that would have to be attached and whether that is proportionate. |

🔴 **The trend that matters most is internal: discovery yield has collapsed while
internal-consistency yield has not.** `p515` produced a refuted premise, a resolved conflict and a
corrected channel diagnosis — all from re-reading shelves — and **zero** new addresses from eight
search legs. 🟡 On a base of this maturity the scarce resource is no longer information, it is
**agreement between the shelves**, and that is precisely what `gate-shelf-consistency` and
`gate-prose-claims` exist to enforce. 🔴 They have not run since `p511`.

### 🔴 The regional battery saturated on a SEVENTH axis — measured, as `p514` established

🔵 **Method, unchanged from `p514` so the series stays comparable:** run the four regional legs and
the four global legs, then grep **every named datum** against the live shelves *before* writing
anything. The count below is the measurement, not an impression.

| leg | named data returned | already held | 🟢 new |
|---|---|---|---|
| North America | state-guidance counts, ≥25 states legislating K-12 AI, **Idaho SB 1227**, NYC traffic-light red tier, K-12 AI Literacy & Readiness Act 2026, SUNY 64-campus policy, UC Berkeley Law prohibition, Oklahoma deadline | 🔴 **all 8** | — |
| EMEA | EU AI Act Annex III point 3's four functions, **Regulation (EU) 2026/1744** Digital Omnibus, **2 Dec 2027** / **2 Aug 2028** dates, Art. 50 transparency from 2 Aug 2026, emotion-recognition ban from 2 Feb 2025 | 🔴 **all 5** | — |
| APAC | **Ipsos** ban-support spread (Indonesia 23% → South Korea 31%), Japan AI Promotion Act non-binding, China's service-specific measures, India governed via DPDP + 2025 rules, **Vietnam**'s 2 Jul 2026 high-risk decision naming education, Singapore 64.3% vs Japan 24.7% adoption | 🔴 **all 6** | — |
| LATAM | Brazil **PL 2.338/2023** high-risk *"selection of students"*, ANPD sandbox to Dec 2026, Mexico's unfinalised framework, **HolonIQ** LATAM EdTech 100, **Teachy**, Google.org **$4.6M** / Raspberry Pi *Experience AI* / 9 countries / **24,000** educators / **1.25M** students by 2028, UNESCO observatory with CONALEP + DGETI | 🔴 **9 of 10** | 🟡 **1** — the IDB 193-solution review |
| supply legs (4 global) | general agent lists (CrewAI, OpenHands, LangGraph, AutoGen), `ai-tutor` topic rows (`nichochar/ari`, `universal-diagnostic-tutor-skill`, `AI_Tutor_Release`/EduAgent, `flysheep-ai/education-skills`), LMS licence comparisons (Moodle GPL-3.0, Open edX AGPL-3.0, Sakai ECL-2.0, **OpenOlat Apache-2.0**, OpenEduCat LGPL-3.0) | 🔴 **all** | — |

🔴 **~29 named facts probed one by one; ONE was not already on these shelves.** Seventh
consecutive pass in which the demand axis returns a single-digit increment, and the supply legs
returned **zero** new addresses — the `ai-tutor` topic rows that a star-ranked search surfaces are
all already filed, most of them in [`agents/trending.md`](../agents/trending.md).

### 🟡 The one new regional datum — and it is channel-attributed, not promoted

🟡 **IDB (Inter-American Development Bank), review of AI-in-education solutions across Latin
America and the Caribbean, dated January 2026:** **193** solutions reviewed; **59%** used
generative AI; **27%** used language models. 🔴 **NOT promoted to fact.** The search channel
produced it; the primary source could not be read — **`www.iadb.org` does not resolve from this
session's network** (`getaddrinfo ENOTFOUND`), the same failure class already recorded for
`arxiv.org` and `www.unesco.org`. 🟡 Carried as `Gap 515-D`: re-probe `iadb.org` from a session
whose network policy allows it, or the three percentages stay search-attributed indefinitely.

🔵 **Why it is worth carrying even unverified.** The base holds LATAM *policy* densely and LATAM
*supply* at zero — **still 0 LATAM-originated open-source education repositories at any star
level**, now an eighth consecutive pass. A 193-solution regional inventory is the first signal
that the supply exists and is simply not on GitHub, which is a different gap from "there is none".


## 🆕 `p514` — `2026-10-28` — **🆕 `T50`: a PUBLISHED REFUTATION decays exactly like a published claim, and this base had never checked one — the Fedena refutation was wrong for 24 passes at a SHA that never moved. 🆕 `T51`: the probe's PATH SET is a bigger error source than the branch set, and this pass has 3 instances to 1. 🆕 `T52`: a grant can cover a branch nobody ships, which is a procurement hazard that "licensed" and "unlicensed" both describe wrongly. 🆕 `T53`: a repository dismissed as low-star institutional infrastructure is often the BROCHURE, and the system is one org away. 🔴 `T45` survives again — supply paid, demand saturated 24/25.**

🔴 **Gate posture:** `make hooks` **DENIED** (`Code from External`), eighteenth denial in nineteen
passes. 🟡 `p511`'s **45/63** is still the last gate-attested reading.

### 🆕 `T50` — a refutation is a claim, and this base audited only one direction

🔵 **This base has strong machinery for decaying *positive* claims**: `Gap 510-A`'s roundness rule,
`Gap 513-A`'s backlog-row rule, `T29`'s `archived` re-read, `gate-shelf-consistency`. 🔴 **Every one
of them watches a claim that something IS so.** Nothing watched a claim that something is **NOT**
so.

🔴 **The instance.** `repos/foundations.md` published a heading — *"Fedena: resolved, and the
Apache-2.0 claim does not survive contact with the repository"* — and a paragraph concluding that
*"neither ships a license file under any of the nine names probed"*. 🔴 **`NOTICE` was not one of
the nine.** Both repositories serve the Apache-2.0 grant clause there, on the default branch, at
`68a84ac445bf` and `333477b06f1d` — **the exact SHAs the section records**, unmoved.

🔵 **Why a refutation is the more dangerous object.** A positive claim invites re-checking: a row
with a star count and a SHA *looks* like something to re-read. 🔴 **A refutation closes the
question** — it is written precisely so no later pass spends budget there, and it reads as
diligence. 🔴 **This one survived ~24 passes and was quoted as settled.**

🟢 **The rule:** a published **negative** verdict carries its probe's **scope** — path set, branch
set, channel — or it is unfalsifiable. 🟢 **A negative verdict whose scope is not recorded is
"unread", never "absent"**, which is `Gap 510-B` generalised from one channel to all of them.

### 🆕 `T51` — the path set, not the branch set, is where the probe actually fails

🔵 `Gap 512-D` (`T42`) was registered on a branch argument, and it was right: `ICTSchool` carries
GPL-3.0 on `ictschool-laravel-5.5` and nothing on `main`. 🔴 **But this pass's 1,840 probes
produced three recoveries, and only ONE was a branch problem.** Two were **path-set** misses on the
**default** branch — both Fedena repos at `NOTICE`.

| cause | instances at `p514` | prior instances |
|---|---|---|
| 🔴 **path set too small** | **2** *(both Fedena, `NOTICE`)* | `frappe/erpnext` (`license.txt`), `formalms` (installer dir), `frappe/education` (19-byte declaration) |
| 🟡 **branch set too small** | 1 *(`ICTSchool`)* | `OpenRoberta/openroberta-lab` (`master` vs `develop`) |

🔴 **So the running score across this base's history is roughly 4:2 in favour of the path set**, and
the branch axis got the gap and the trend ID while the path axis kept being treated as a series of
one-offs. 🟢 **The rule: a licence probe's path set is a RECORDED artefact of the verdict**, listed
with it, and `NOTICE`, `COPYING`, `license.txt` and `*.rdoc`/`*.markdown` variants belong in it.
🔵 **Cheap test for any negative verdict already on these shelves: was `NOTICE` probed?**

### 🆕 `T52` — a grant can fail to reach the code that ships

🔴 **`ictinnovations/ICTSchool` is the specimen, and it is not an edge case — it is an active
project.** Default branch `main`: last commit **2026-10-13**, **no grant** at 20 paths. Branch
`ictschool-laravel-5.5`: last commit **2022-09-23**, **full GPL-3.0**, 35,149 B,
`sha256₁₆ 3972dc9744f6499f`.

🔵 **Both of the usual words are wrong.** *"Unlicensed"* is wrong — there is a grant in the
repository. *"GPL-3.0"* — what every aggregator prints — is wrong about **the code a client would
install**. 🔴 **The true statement is narrower and harder to say: the grant does not cover the
shipped branch.**

🟢 **The rule, and it is a delivery rule rather than a research one: a licence verdict is pinned to
a REF, and the ref must be the one the client will deploy.** 🔵 A licence cell without a ref is
incomplete in exactly the way a star cell without a date is incomplete — and this base already
fixed the star case.

### 🆕 `T53` — the dismissed repo is often the brochure

🔴 **This base has carried "Sunbird" since `p316`** — as
[`project-sunbird/project-sunbird.github.io`](https://github.com/project-sunbird/project-sunbird.github.io):
**41★**, default ref `dev`, HEAD **2018-12-21**. 🔵 It was filed as *evidence* for a good lesson —
*"a star-ranked search cannot see institutional infrastructure"* — and then the question closed.

🔴 **It was the website repo.** The system is [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal):
**MIT**, 1,072 B, `sha256₁₆ 7dde06716f259584`, grant on **78 of 79 heads**, HEAD **2025-12-16**, and
it is the portal behind **DIKSHA**, India's national platform. 🔴 **Different organisation**
(`Sunbird-Ed`, not `project-sunbird`), reachable by `git ls-remote` in one call.

🟢 **The rule: when an address is dismissed as low-star institutional infrastructure, enumerate its
ORGANISATION before filing the finding.** 🔵 **The irony is the useful part** — the lesson drawn in
`p316` was *correct*, and drawing it is what stopped the search. A conclusion that explains an
absence can prevent the search that would refute it.

### 🔴 `T45` re-tested — supply paid, demand saturated, for the second pass running

| axis | `p514` result |
|---|---|
| 🔴 **demand** | **24 of ~25** named regional facts already held; **1** new (`DIKSHA`). Sixth saturation axis |
| 🟢 **supply** | 🟢 **2 licence records corrected**, **1 refusal sharpened**, **1 national-scale MIT platform shelved**, **16 nils upgraded to enumerated** |

🔵 **`T45` said supply and legal usability are where this base still moves while demand repeats.
Two passes of evidence now.** 🟢 **The operative instruction stands: spend the regional budget on
instruments, and spend the rest on bytes.**
## 🆕 `p513` — `2026-10-28` — **🆕 `T46`: a statutory date this base treated as settled MOVED, and the amendment ran in BOTH directions at once — one duty deferred 16 months, another left to bite on the original date. 🆕 `T47`: a backlog row is not a cheap row, it is an UNVERIFIABLE row, and this pass caught one drifting to prove it. 🆕 `T48` sharpens `T43` into a rule with a counter-example: a licence that OPENS with MIT's own sentence and then forbids commercial use defeats every substring detector. 🆕 `T49`: in this sector traction and legal usability are ANTI-CORRELATED at the top — the four highest-traction content assets found this pass are the four Globant cannot use. 🔴 `T45` survives its first real test: supply saturated on a fifth axis while demand returned nothing primary.**

### 🆕 `T46` — a compliance date is a measurement, not a constant, and an amendment can run both ways

This base carried **2 August 2026** as the EU high-risk date for education. 🔴 **It is wrong, and
it has been wrong since 27 July 2026**, when **Regulation (EU) 2026/1744** entered into force and
deferred Annex III obligations — education among them — to **2 December 2027**.

🔴 **The non-obvious half is what did NOT move.** The same instrument left **Article 50
transparency** on its original date, so it has applied since **2 August 2026**. A single amendment
therefore pushed one duty **16 months out** and left another **already live**:

| duty | this base carried | actual |
|---|---|---|
| Annex III high-risk (grading, admissions, proctoring) | 2 Aug 2026 | 🔴 **2 Dec 2027** |
| Article 50 transparency / AI disclosure | — | 🔴 **2 Aug 2026 — live** |
| emotion recognition in schools, AI-literacy duty | — | **Feb 2025 — live** |

🟢 **The rule:** a regulatory date on a shelf needs a **re-read cadence like a star cell**, and the
re-read must enumerate *which* duties an amendment touched rather than accepting a headline date.
🔴 **"The deadline slipped" is the most dangerous possible summary** — it reads as relief and it
concealed a duty that was already enforceable. `T46` is the demand-side twin of `T36`: a convention
assumed instead of measured.

### 🆕 `T47` — a backlog row is an unverifiable row, and it decays where nobody is looking

`zijinz456/OpenTutor` was byte-read, described and star-counted by an earlier pass, then left in a
narrative table. 🔴 **Its HEAD has since moved off the SHA this base records** (`dbaab74ffe76` →
`2a604cc3935a`), and **no check in this base would ever have caught it**, because every drift and
currency sweep this base runs is framed on the shelves.

🟢 **So a backlog is not a cheap holding area — it is an exemption from verification.** The row's
licence happened to be byte-identical at both SHAs, so nothing was lost this time; that is luck,
not a control. 🆕 **The rule: anything worth byte-reading is worth either shelving or explicitly
refusing. There is no third state that survives contact with time.** `p513` acted on it by
promoting all nine such rows at once.

🔵 **`T47` also explains the shape of `T39`.** Discovery has looked saturated for several passes
partly because *found* and *shelved* had drifted apart: the supply was already in the base,
unwatched, and re-finding it kept reading as "nothing new".

### 🆕 `T48` — a detector that matches a sentence can be inverted by a licence that quotes one

`T43` said a classifier and a byte reader fail in opposite directions. 🆕 **`T48` is the specific
adversarial case, and it is live at 2,050★.**

[`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM)'s `LICENSE.md` is titled **"PageLM
Community License"** and its second line is MIT's own opening — *"Permission is hereby granted,
free of charge, to any person obtaining a copy…"* — before it continues *"…for **personal,
educational, or non-commercial research purposes**"* and later *"Redistribution … is strictly
prohibited"*, with a **revocable** grant.

🔴 **Every substring detector in this base's history scores that as MIT.** The same leg also scored
`apache/openmeetings` as MIT from a bundled dependency 51 KB into an appendix. 🟢 **The rule, in two
lines:**
1. **Match the TITLE and the operative grant clause**, never a sentence found anywhere in the file.
2. **Read the whole payload before naming a family** — a permissive opening does not bound what
   follows, and a 50 KB licence is a container, not a grant.

🔵 Counter-direction, same pass: `OpenOLAT` serves a **verbatim Apache-2.0 body with attribution
text appended** and GitHub's classifier reports `NOASSERTION`. 🔴 **So the two failure modes are
simultaneous, not alternatives** — the strict channel refused a real grant in the same sweep that
the loose channel accepted a fake one.

### 🆕 `T49` — traction and legal usability are anti-correlated at the top of this sector

Ranked by stars, the content-and-skills assets found this pass invert on licence:

| rank by ★ | asset | ★ | usable commercially |
|---|---|---|---|
| 1 | `cn-math-taxonomy` | 4,782 | 🔴 **No** — CC BY-NC 4.0 |
| 2 | `PageLM` | 2,050 | 🔴 **No** — bespoke non-commercial, no redistribution |
| 3 | `education-agent-skills` | 921 | 🟡 **Encumbered** — CC BY-SA 4.0 reaches derivatives |
| 4 | `ai-ethos` | 498 | 🔴 **No grant at all** |
| 5 | `claudemy` | 511 | 🟢 **Yes** — MIT |
| 6 | `Bloom` | 293 | 🟢 **Yes** — MIT |

🔴 **The four highest-traction assets are the four that cannot be used**, and the permissive ones
start below 600★. 🟢 **Why this is structural rather than coincidental:** these top assets are
**curriculum content and pedagogy corpora**, and the people who build those come from academic and
publishing norms where CC-NC is the default generous choice — while the permissive rows are
**software** built by engineers whose default is MIT. 🟢 **The operative consequence for Globant:
never shortlist an education asset by stars.** A stars-ranked shortlist in this sector is
approximately a list of things you must then discard, and the discovery sweep that produces it
must carry a licence column or it is actively misleading.

### 🔴 `T45` survives its first real test, with one correction

`p512` registered that in this sector **supply is discoverable and demand is not**. Both halves held:

- 🟢 **Supply:** four fresh legs, 27 addresses, **zero new to this base** — a fifth independent
  saturation axis.
- 🔴 **Demand:** no primary market-size figure obtained. Vendor pages offering "$12.5B in 2026" and
  "$12.3B by 2026" sit *above* both ends of this base's shelved range and trace to marketing
  copy — recording them would widen `T10`'s 3.3× spread on the weakest available evidence.

🟡 **The correction:** `T45` is too absolute as written. **Demand is not undiscoverable — *market
size* is.** This pass obtained hard, primary, demand-side numbers on the **governance** axis:
87 % / 26 % (UNESCO IESALC, 200 institutions, 19 countries), TALIS 2024 teacher use
(BR 56 / CL 55 / CO 53 / CR 52 vs OECD 36), PISA 2025 (9 in 10 students), **134 bills / 31 states**.
🟢 **Reframed: the sector's spend is unmeasurable from here, but its OBLIGATIONS and its GAPS are
measurable — and those are what an engagement is actually sold against.**

### 🆕 `T50` — high adoption with absent governance is the sector's dominant buying condition

The same two-part shape appears in every region measured this pass, which makes it a market
structure rather than a regional quirk:

| region | adoption | governance |
|---|---|---|
| **LATAM** | 87 % of HE institutions use AI | 🔴 **26 %** have a formal strategy |
| **LATAM (BR schools)** | 53 % of administrators use AI | 🔴 **22 %** have school guidelines |
| **North America** | 60–61 % teacher use | 🔴 most public schools lack a student AI policy |
| **EMEA** | 🔴 un-sourced (informed gap) | statute is live and dated |

🟢 **So the buyer is never being persuaded to adopt — they are being rescued from adoption that has
already happened without rules.** That inverts the usual pitch order: the inventory, the policy and
the eval harness lead; the tutor follows. 🔴 It also means a "pilot" framing is wrong on arrival,
because the pilot already ran — informally, ungoverned, at scale.

### 🔴 Carried trends, re-checked this pass

- 🟢 **`T43` holds in both directions**, and is now sharpened by `T48` into an operative two-line rule.
- 🟢 **`T42` holds** — `OpenOLAT`'s grant is on `master`; its payload is not canonical-length
  (10 982 B vs 11 358 B), which is the attribution-appendix shape, not a different licence.
- 🟢 **`T36` holds and gained three more cases**: `book-to-skill`, `tsugi`, `scorm-again` and
  `haxcms-php` all default to **`master`**; `kolibri` and `oppia` default to **`develop`**.
- 🔴 **`T9` (offline-first) is now load-bearing rather than contextual**, on the Argentina 75 %/42 %
  socio-economic split — connectivity is where the equity gap physically lives.
- 🔴 **`Gap 504-A` reproduced exactly:** a 15-slug batch returned **13**, and
  `openedx/edx-platform` was again among the silently dropped. **Reconcile returned `full_name`
  against the queried slug set on every call** — this pass did, which is the only reason it is known.
- 🔵 **`T10` unchanged by choice** — see `T45` above.

## 🆕 `p512` — `2026-10-28` — **🔴 `T40` IS HALF REFUTED ONE PASS AFTER IT WAS REGISTERED: typography is NOT a data-quality signal — bolded cells are wrong at 27 %, plain at 28 % — and only ROUNDNESS survives, as a screen with 56 % recall rather than a verdict. 🆕 `T42`: an absence must be enumerated over BRANCHES, not just paths, and a real repository just proved it. 🆕 `T43`: a licence detector and a byte reader fail in OPPOSITE directions, and knowing which is which is now a two-line rule. 🆕 `T44`: a self-checking query can annihilate its own control. 🆕 `T45`: the sector's supply is discoverable and its demand is not.**

### 🔴 `T40` — half refuted, and the surviving half is weaker than it was registered

`p511` registered `T40` as *"typography is a data-quality signal, and roundness beats provenance."*
🟢 **Tested this pass on 91 cells, classified before any value was seen:**

| feature | 🔴 wrong | 🟢 exact | wrong-rate | verdict |
|---|---|---|---|---|
| bolded | 8 | 22 | **27 %** | 🔴 **no signal** |
| plain | 17 | 44 | **28 %** | 🔴 **no signal** |
| ends in `00` | 14 | 3 | 🔴 **82 %** | 🟢 screen survives |
| does not | 11 | 63 | 🟢 **15 %** | — |

🔴 **Bolding discriminates nothing** — one percentage point apart — and among non-round cells it is
*mildly anti-informative* (**BOLD 25 % wrong vs plain 9 %**), because this base bolds its flagships
and a flagship's count moves fastest. 🔴 **And roundness is a screen, not a verdict: its recall is
14/25 = 56 %** — it misses nearly half the defects — while `p511` read 4/4 and took it for a law.
Three round cells are **exact** (`k12-teacher-skills` 600, `openeducat_erp` 900 twice).
🟢 **The rule, in its final form:** *a round star cell is unread until re-read* — a statement about
what you may claim, never about what the value is.

🔵 **The deeper lesson, which is about frames and not about stars.** `p510` framed its census on
bolded cells; `p511` framed on the live shelves' star cells; both frames were **typographic**, and
[`verticals/solutions.md`](../verticals/solutions.md)'s 26-row platform table has **two** bolded star
cells out of 26 — so it was structurally invisible to both, and **11 of its cells were wrong**.
🟢 **Framing on table STRUCTURE instead found 39 wrong cells against `p511`'s four.** A frame built
from a feature of the *writing* will systematically miss whichever part of the base writes
differently.

### 🆕 `T42` — an absence must be enumerated over BRANCHES, not only over paths

`T34` (`p509`) says an absence is a claim about everything, and only an enumeration can carry it — a
path list can never prove a licence missing. 🔴 **`p512` found the second axis of the same error.**
[`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) serves **no licence
payload at 12 paths on `develop`**, which `git ls-remote --symref` confirms is its true default
branch — and serves **Apache-2.0 at `master/LICENSE`, 11,359 B, `sha256₁₆ 8c6db340475136df`**.
🔴 **A 12-path probe on the resolved default branch is still a path list; it is just a longer one.**
🔵 This also **inverts** `T36`/`p509`'s practical advice. Resolving the true default branch is right
for *liveness* and for *pins*; for a **grant** it can manufacture a false absence, because a project
that cuts releases from `master` and works on `develop` has no reason to carry the licence file
forward. 🟢 **Rule: default branch for liveness, all branches for the grant.** Until branches are
enumerated, `NONE-OF-N-PATHS` means **unread**, not **unlicensed**.

### 🆕 `T43` — the detector and the byte reader fail in opposite directions, and both failures are now named

`T33` (`p508`) established that a detector's **abstention** is not a denial. 🟢 **`p512` met both
failure directions in one sweep of four new addresses, which makes the rule symmetrical and cheap:**

| address | API `license.spdx_id` | the bytes | who is wrong |
|---|---|---|---|
| [`expertiza/expertiza`](https://github.com/expertiza/expertiza) | 🟢 `MIT` | verbatim MIT body, **1,068 B**, 🔴 **no title line** | 🔴 **the byte reader** — `p455`'s title-block anchor sees nothing here (`p509`'s defect #4, now on a real address) |
| [`smithjohn78390/tongjiang-lab`](https://github.com/smithjohn78390/tongjiang-lab) | 🔴 `NOASSERTION` (`key: other`) | **CC BY-NC 4.0** named in prose, **643 B** | 🔴 **the detector** — it abstains on a grant that is explicit and **non-commercial** |

🔴 **The commercially dangerous direction is the second one.** A candidate pipeline that screens on
`spdx_id != NOASSERTION` keeps `tongjiang-lab` as *"licence unknown, investigate later"* — and
*unknown* is a far more comfortable label than **non-commercial**, so it survives triage. 🟢 **The
two-line rule:** a **recognised** `spdx_id` is admissible evidence *for* a grant even when the byte
anchor cannot see it; an **abstention** is never evidence *for* anything, and the bytes decide.
🔵 Both arms must run on every new address. Either alone is wrong about 1 in 2 of these four.

### 🆕 `T44` — a self-checking query can annihilate its own control

🟢 `T37` (`p510`) says a check that cannot fail is not evidence, and prescribed feeding every
instrument a known-bad. 🔴 **`p512` found the mirror failure: a known-GOOD control that the query
itself deletes.** The leg
`topic:education forks:>80 stars:<250 pushed:>2026-06-01 repo:HKUDS/DeepTutor` returned
**`total_count: 0` with `incomplete_results: false`** — a clean, confident zero — because search
qualifiers **AND**: `DeepTutor` satisfies neither `stars:<250` nor the topic, so the control was
eliminated along with everything else. 🔵 **A malformed query and an empty world return the same
byte on this channel**, and the control that was supposed to tell them apart was the thing removed.
🟢 **Rule: an in-query control is valid only on a pure disjunction of `repo:` terms. Any filtered leg
must be controlled by a second, separate call.** 🟢 Run that way, the same technique then produced
this base's strongest reading of `Gap 504-A`: `openedx/edx-platform` absent, the control present,
`incomplete_results: false` — **the channel, not the query**.

### 🆕 `T45` — in this sector, supply is discoverable and demand is not, and the fix for supply was a sort key

🔴 In one pass, with the same instrument: **eight prescribed demand legs returned zero new figures**
(third consecutive pass), while **one change of sort key on the supply side returned four addresses
new to this base**.

| axis | what was wrong | what fixed it |
|---|---|---|
| supply | ranking by **stars** — attention, already harvested | 🟢 ranking by **forks** — institutional copies, invisible to every trending list |
| demand | the **channel** — a general web search for a region | 🔴 unfixed. 🟢 `T30`'s workaround holds: query the **instrument** (the Act, an Annex, a national transposition), never the region |

🔵 **Why forks are the right key in education specifically:** a star is one person deciding to
remember a repository; a fork is frequently one *institution* deciding to run it. In a sector whose
buyers are institutions, the fork count is the commercial signal — and it reaches software that never
trends, like [`expertiza/expertiza`](https://github.com/expertiza/expertiza) at **1,329 forks against
194★**. 🔴 **The cost is precision: 36 of the leg's 40 rows were not education-AI at all**, because
`education` is a self-applied topic and the fork axis amplifies whatever the label admits —
Hacktoberfest starter repositories are forked by contributors, not institutions. **A finder, never a
ranking.**

### 🔴 Carried trends, re-checked this pass

- 🔴 **`T38` (an unenforced repair regresses within one pass) — CONFIRMED on a second shape, and a
  worse one.** `p511` saw a repaired heading regress; `p512` finds that **2 of `p511`'s own 4
  published corrections never reached the shelf at all** (`ai-agents-for-beginners` still at
  `78,059`; `14,300` alive in two live recipes). **A correction is not a correction until it is
  applied at every live site**, and the cross-file agreement check is now the instrument that proves
  it: **7 of 29 multiply-present addresses disagreed with themselves.**
- 🟢 **`T39` (discovery is saturated) — BOUNDED, not refuted.** Saturation is a property of
  attention-ranked discovery. See `T45`.
- 🟢 **`T26` (the newest supply is deliberately non-commercial) — holding, seventh pass, and this is
  its clearest instance:** the fastest-rising address this base has ever recorded in a day
  (`tongjiang-lab`, 446★ in <24 h) is refused on its licence, not its quality.
- 🟢 **`T29` / `Gap 504-A` standing checks:** `archived: false` on all 71 addresses read on the API
  this pass; `incomplete_results: false` on every batch.
- 🔴 **`T10` (market sizing is not usable) — STRENGTHENED.** The 2026 spread widens from **1.9× to
  3.3×** (`$3.7B` – `$12.3B`), and a second North-America share figure (**42 %**) now contradicts the
  shelved **36 %** that this file called the one point of agreement.

## 🆕 `p511` — `2026-10-28` — **🟢 THE GATE RAN, AND THE SINGLE MOST IMPORTANT TREND ON THIS BASE IS THAT SIXTEEN PASSES OF UNATTESTED WORK NOW HAVE A VERDICT: 45 of 63 gates green. 🆕 `T38`–`T41` registered. 🔴 One of them is the discovery channel's saturation, measured at 95.2 % shelf recall rather than asserted as "zero new addresses".**

### 🆕 `T38` — An unenforced repair regresses within one pass

🔴 **Evidence, from this pass and the two before it.** `p508` found [`market.md`](./market.md)
carrying two bare `## Opportunities by region` headings — the one contract the region filter depends
on — and repaired it by suffixing the newer heading. 🔴 **`p509` added a fresh unsuffixed heading and
the defect was back**, undetected by `p509` and `p510`, and caught at `p511` **by the gate**
(`P383-MULTIPLE-BLOCKS`, line 352) **and independently by hand in the same pass**.

🔵 **The trend is not "this base makes mistakes".** It is that **a repair recorded in prose has a
half-life of about one pass**, because nothing re-checks it and the next pass writes over the region
it lives in. 🟢 **The corollary is operational: a repair is only durable if a gate holds it, and this
base has had 63 gates the whole time with no evidence that any of them ran for sixteen passes.**

### 🆕 `T39` — Discovery is saturated; currency is where the defects are

🔴 Three consecutive passes reported *"the prescribed legs returned zero new addresses"*. 🟢 **This
pass measured the quantity behind it: 83 distinct addresses returned by five catalogue legs, 79
already shelved — 95.2 % recall.** One promotion.

🟢 **In the same pass, the CURRENCY axis produced four defects out of twenty-two cells read** — a
star cell overstated by 38, two understated by 41 and 61, one by 1 — plus a retired reading
(`DeepTutor`'s *"attention, not shipping"*) and an independently re-attested byte census.

🔵 **So the trend is a budget finding:** the supply axis is near-exhausted on this channel and the
currency axis is not. 🟢 **Operational form:** run the three prescribed `topic:` legs on a longer
cycle; spend the recovered budget on drift (pins, tags, stars, grants). 🔴 **Risk acknowledged:** a
longer discovery cycle is how a base goes blind to a genuinely new entrant, so the cycle must be
stated and kept, not drifted into.

### 🆕 `T40` — Typography is a data-quality signal, and roundness beats provenance

🟢 `p510` noticed two wrong star cells shared a missing `*(🟢 pNNN, API)*` suffix and read that as
the tell. 🟢 **Tested over all 22 star cells this pass, the suffix's absence has 100 % recall and
29 % precision** — every wrong cell lacks one, and ten correct cells lack one too.

🔴 **The clean discriminator is ROUNDNESS.** Split on *"ends in two or more zeros"*: **4 of 4
re-read round cells were WRONG; 15 of 15 non-round cells were EXACT.**

🔵 **Why this generalises beyond stars:** a round number in a measured column is a *remembered*
value wearing a measurement's typography, and the rounding is the fingerprint of the human step
between the read and the write. 🟢 **The rule any shelf can apply: a round figure in a measured
column is unread until re-read.** 🔴 **And the direction matters** — `kolibri` was **overstated**, so
a "values only grow" assumption cannot catch this class.

### 🆕 `T41` — A denial that names its remedy is a different kind of gap

🔴 `Gap 483-K` has been recorded as **unclosable** for fifteen passes on the basis of two channels
(proxy `CONNECT` refusal; `api.github.com` 403). 🟢 **A third channel was probed this pass and fails
differently: `WebFetch` returns `getaddrinfo ENOTFOUND` with an explicit cause — the host is outside
the session's allowed network domains.**

🔵 **That re-classifies the gap.** *"The open web is unreachable"* is a statement about the world and
cannot be acted on. *"Three hostnames are not in an allow-list"* is a statement about configuration
and is one action by one human. 🟢 **Trend form: before filing a denial as a property of the world,
probe a channel that fails for a DIFFERENT reason** — the failure modes carry the remedy, and
identical-looking refusals across two channels had hidden it for fifteen passes.

### 🔴 Carried trends, re-checked this pass

| trend | status |
|---|---|
| **`T34` — 18 shelf addresses carry no grant at all** | 🔴 **Unchanged, and now load-bearing twice over.** It is also the population on which `p510`'s prescribed liveness probe is undefined: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) and [`h9-tect/AI-Roadmaps`](https://github.com/h9-tect/AI-Roadmaps) are **LIVE** and answer `raw HEAD/LICENSE` with the same **404** as a repository that never existed |
| **`Gap 504-A` — silent per-repository exclusion** | 🔴 **Reproduced a FIFTH consecutive pass**, and at the smallest batch yet: [`openedx/edx-platform`](https://github.com/openedx/edx-platform) silently absent from a **5-slug** batch reporting `incomplete_results: false` |
| **`Gap 509-B` — no count without a known-good and known-bad control** | 🔴 **Instance nine and ten, both this pass's own.** A star extractor attributed one repository's figure to another from the same cell's prose (`oppia` "41,705", `TrenTorch` "385" — both shelves were RIGHT); a byte probe was 1 low on every newline-terminated payload. 🟢 Both caught by controls before publication |
| **the retired "134 bills / 31 states"** | 🔴 **Third re-appearance** on the North America leg. Recorded, not re-shelved |
| **`Gap 507-A` — a 2026 APAC teacher-adoption rate** | 🔴 **Fourth nil.** The Ipsos Education Monitor 2026 is a 2026 APAC instrument but measures attitudes, not use |

## 🆕 `p510` — `2026-10-28` — **🆕 `T37`: an instrument that answers identically to a live target and an absent one is not a check, and this base is prescribed to run one. 🆕 `T38`: a rounded number typeset as an exact read is invisible to review — the tell is the MISSING provenance, not the digits. 🔴 `T36` keeps its rule and loses its reason: the hazard is a stale 200, not a 404.**

Reads: [`url-check-control.2026-10-28-p510.tsv`](../evidence/url-check-control.2026-10-28-p510.tsv),
[`liveness-branch-census.2026-10-28-p510.tsv`](../evidence/liveness-branch-census.2026-10-28-p510.tsv),
[`stale-branch-byte-compare.2026-10-28-p510.tsv`](../evidence/stale-branch-byte-compare.2026-10-28-p510.tsv),
[`star-cell-staleness.2026-10-28-p510.tsv`](../evidence/star-cell-staleness.2026-10-28-p510.tsv).
Code: [`compose/code/p510-liveness-gate/`](../compose/code/p510-liveness-gate/) — **8/8 controls green**.

🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — sixteenth denial in seventeen passes.**

### 🆕 `T37` — a check that cannot fail is not evidence, and the only way to know is to feed it a known-bad

🔴 **The standing instruction to *"verify every URL before writing it (`curl -sI`)"* produces nothing
on this channel.** `github.com` answers **403** to `HKUDS/DeepTutor` (live, 47,725★), to
`learningequality/kolibri` (live), to a repository that never existed, and to a repository under an
**owner** that never existed. 🔴 **Four targets, two classes, one response.**

🔵 **The generalisation is the trend, and it is not about GitHub.** A verification step is only
evidence if it can come back negative. `T31` already says a measure needs its definition; `T37` adds
the operational half: **a measure needs a demonstrated failure mode.** A probe is unvalidated until
something known-bad has been pushed through it, and "all 154 verified" from an instrument that
cannot say "no" is indistinguishable from not having checked.

🟢 **Applied here it produced a real replacement, not just a complaint**: `git ls-remote --symref`
(liveness + true default branch) and `raw.githubusercontent.com` (**200** live / **404** absent),
both control-proven, carried **154 of 154 addresses to `LIVE`**.
🟡 **And it bounded its own replacement honestly: the git channel answers an ABSENT repository and a
PRIVATE one identically**, so `LIVE` is assertable and `ABSENT` is not — which is why the classifier
emits `UNREADABLE_ABSENT_OR_PRIVATE` and why no row may be retired on one channel (`Gap 510-B`).

### 🆕 `T38` — a rounded value dressed as an exact read, and the tell is what is missing

🔴 Two shelf cells read `**74,800**` and `**1,100**`. Both are **rounded**; both are typeset exactly
like the exact API reads beside them; 🔴 **and [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch)
actually reads 1,064 — the shelf OVERSTATED by 36, and the true count went DOWN.**

🔵 **The lesson is not "round numbers are suspicious" — it is that the evidence of a missing
measurement was already on the page and nobody read it as evidence.** Every re-measured cell on these
shelves carries a `*(🟢 pNNN, API)*` suffix. **These two carried none.** 🟢 **An absent provenance
annotation is a positive signal that a value was never read**, and it is mechanically checkable,
which is what makes `Gap 510-A` a gate rather than a habit.

🔴 **It also falsifies a comfortable assumption:** a staleness check that only looks for growth
cannot find this, because stars decrease. 🔵 `p504`'s *"the largest error on any exact-integer cell
is 595 → 598"* was true and **excluded the rounded cells by construction** — the quietest way for a
bound to be wrong is for its population to have been defined around the exceptions.

### 🔴 `T36` — the rule survives, the stated reason does not

🟡 `T36` (`p509`) says *"a default branch is a measurement, not a convention"*. 🟢 **The rule holds and
is re-attested**: **18 of 154** addresses default to neither `main` nor `master`, across **14
distinct names**, five of them version-pinned (`release_11`, `v31.0.00`, `19.0`, `2.12`,
`v4.0.x-develop`).

🔴 **But `p509`'s reason — that this *"invalidates a method this base has used throughout"* — is too
strong, and this pass tried hard to confirm it before giving it up.** A `main`/`master` probe mostly
does **not** fail on those 18: `GibbonEdu/core` and `bigbluebutton` answer **200 on both**;
`kolibri`, `openeducat_erp` and `ILIAS` answer **200 on `master`**. 🔴 **The hazard is therefore a
silent 200 from a stale branch, not a visible 404** — strictly worse as a failure mode, and invisible
to the `NOPAYLOAD` count that found the original problem. 🟢 **And then the consequence failed too:
the licence bytes are identical on 7 of 7**, so **no licence cell is wrong and `p509`'s 119 payloads
stand.**

🔵 **The surviving formulation is narrower and more usable: resolve the symref because *versioned*
content — code, migrations, releases — is branch-dependent, while licence payloads on this population
are branch-stable.** 🟢 **Two confident claims of my own died to measurement here, and the base is
better attested for both.**

## 🆕 `p509` — `2026-10-28` — **🆕 `T34`: an ABSENCE is a claim about everything, and only an enumeration can carry it — a path list can never prove a licence missing. 🆕 `T35`: a channel is not a host, and this base just found an endpoint-level gate inside a channel it treated as open. 🔴 `T33` gains a real fourth state and loses an invented one.**

Reads: [`licence-byte-census.2026-10-28-p509.tsv`](../evidence/licence-byte-census.2026-10-28-p509.tsv),
[`no-grant-tree-probe.2026-10-28-p509.tsv`](../evidence/no-grant-tree-probe.2026-10-28-p509.tsv),
[`probe-defects.2026-10-28-p509.tsv`](../evidence/probe-defects.2026-10-28-p509.tsv),
[`default-branch-census.2026-10-28-p509.tsv`](../evidence/default-branch-census.2026-10-28-p509.tsv),
[`channel-probe.2026-10-28-p509.tsv`](../evidence/channel-probe.2026-10-28-p509.tsv).

🔴 **Gate posture: `make hooks` not run (`Code from External`) — a fifteenth denial in sixteen
passes.** Nothing below is gate-attested.

### 🆕 `T34` — an absence must be enumerated, never inferred from the paths you thought to try

🔵 **`T33` taught that a detector's abstention is not a denial. `T34` is the same error one level
further out, and it is this base's most expensive remaining instrument gap: a 404 is a fact about
the URL you requested, and "no grant" is a claim about every path in the repository.**

🟢 **The pass that established it nearly published the opposite.** A 19-path probe reported
[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
(**67,603★**) as carrying no licence payload while the API reported `spdx_id: MIT`. 🔵 **That
disagreement was read, briefly, as a NEW licence state** — *detector asserts a grant, no payload
exists* — which would have been a genuine and interesting finding. 🔴 **It was a capital letter.**
The grant is at lowercase, extensionless **`license`**: **1,082 B, `sha256 22c7cae23a2b00cb`**,
opening `The MIT License (MIT)`. **A probe's path list is a hypothesis, and its misses are evidence
about the hypothesis before they are evidence about the repository.**

🟢 **The instrument that settles it, and it is cheap:**
`git clone --depth 1 --filter=blob:none --no-checkout` + `git ls-tree -r` enumerates a complete tree
with no blob transfer. **18 of 137 shelf addresses carry no licence path anywhere** — now a proven
nil, where before it was an inference from a handful of 404s.

🔴 **And enumeration immediately paid for itself twice, in opposite directions:**
🟢 [`formalms/formalms`](https://github.com/formalms/formalms) is **GPL-2.0** — grant served from
`html/lib/System/license/license_english.txt` (**15,146 B**, in four languages, because the
*installer* displays it) while the API carries **no `license` object** at all. **A row this base
would have called ungranted has a real grant in an unguessable place.**
🔴 [`victor-lubn/Special-Education-Planning`](https://github.com/victor-lubn/Special-Education-Planning)'s
four `licence` matches are **`licence.js`, `check-licence-dialog.component.ts`,
`licence-dialog-data.model.ts`** — **application code that implements a licence-check dialog.**
🔵 **`p455` named this class as *"adjacency is not attribution"* and retracted a 20.6% defect rate
over it. A filename-keyed probe cannot see a token's ROLE — `Gap 506-B`'s lesson, now demonstrated
on licences rather than star counts.**

🟡 **The corollary that costs nothing and prevents a whole class: a vendored dependency's licence is
not the repository's grant.** [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool)
(2,313 files) carries bootstrap, datatables and flot grants under `public/bower_components/` and
**none of its own**. Any sweep that greps for `LICENSE` recursively will shelve it as licensed.

### 🆕 `T35` — a channel is not a host, and availability can be gated per endpoint inside one

🔵 **`Gap 505-B` established that denial can be PER-ENDPOINT rather than per-host, on
`api.github.com`. `T35` generalises it to a channel this base has treated as uniformly open.**

🔴 **The MCP GitHub channel is gated inside itself.** `search_repositories` answers for **any**
repository — stars, `archived`, `license.spdx_id`, all read this pass. **`get_file_contents` returns
`ACCESS DENIED`, scoped to this session's one configured repository.** 🔵 **Consequence, and it is
why this trend is worth a number rather than a note: every future pass that plans *"list the repo's
files over the API"* as the remedy for a licence question will fail, and `T34`'s enumeration must go
over the git protocol instead.**

🟡 **Second instance in the same pass, and it concerns reliability rather than permission:
`git ls-remote` is not concurrency-safe here.** At `-P 10` it returned **NOREF for
[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)** — this base's flagship, **47,677★** —
and single-threaded the same address resolves `refs/heads/main` normally. 🔴 **A parallelism setting
is now part of a probe's result, not part of its performance.** Re-probe any nil serially before
recording it.

### 🔴 `T33` — one state added, one retracted, and the difference is the lesson

| state | evidence | is it a grant? |
|---|---|---|
| recognised `spdx_id` | payload classified | 🟢 yes |
| `NOASSERTION` | payload exists, classifier abstained — `gegok12`'s **1,150 B MIT** | 🟡 **read the payload** |
| no `license` object | — | 🔴 only evidence of no grant *with* `T34`'s enumeration |
| 🆕 **`POINTER_DANGLING`** | `codeforlife-*`: **121 B** *"Find our license here"* → **404** | 🔴 **an assertion with no referent** |
| 🆕 **`DECLARED_NOT_SERVED`** | `frappe/education`: `license.txt` = **19 B**, `"License: GNU GPL V3"` | 🟡 family stated, text absent |
| 🆕 **`NOTICE_ONLY`** | both `fedena` mirrors (679 / 680 B) | 🔴 a NOTICE grants nothing |
| 🔴 **retracted** | *"detector asserts MIT, no payload"* | 🟢 **not a state — a filename-case defect** |

🔵 **Three of these were invisible while licences were read one guessed path at a time, and the
retracted one is the point of the table: a new state is the most attractive possible conclusion and
therefore the one a pass should test hardest before publishing it.**

### 🟡 `T36` — a default branch is a measurement, not a convention

🔴 **18 of 136 shelf addresses (13.2%) default to neither `main` nor `master`**, and they are
disproportionately the **verticals** this base sells into: `frappe/*` on `develop`, `oppia` on
`develop`, `kolibri` on `develop`, `tao-core` on `develop`, `ILIAS` on `release_11`,
`bigbluebutton` on `v4.0.x-develop`, `openeducat_erp` on `19.0`, `overhangio/tutor` on `release`,
`i-educar` on `2.12`, `GibbonEdu/core` on `v31.0.00`.
🔵 **`francoisjacquet/rosariosis` defaults to `mobile`** — a name that reads like a side branch and
is the project's `HEAD`. 🟢 **Resolve `HEAD`'s symref before reading any path; never infer a default
branch from how its name sounds.** Six of this pass's own round-1 nils were this defect alone.


## 🆕 `p508` — `2026-10-28` — **🆕 `T33`: a detector's ABSTENTION is not a verdict — and quoting the abstention instead of the payload cost `p507` its headline vertical finding, on bytes this base had already read. 🟢 `Gap 504-A` characterised with the control `p504` only asserted. 🔴 The HTML limb of the GitHub channel is gone; the byte limb is all that is left.**

Reads: [`licence-bytes.2026-10-28-p508.tsv`](../evidence/licence-bytes.2026-10-28-p508.tsv),
[`query-shape.2026-10-28-p508.tsv`](../evidence/query-shape.2026-10-28-p508.tsv),
[`channel-probe.2026-10-28-p508.tsv`](../evidence/channel-probe.2026-10-28-p508.tsv),
[`saturation-sweep.2026-10-28-p508.tsv`](../evidence/saturation-sweep.2026-10-28-p508.tsv),
[`api-shelf-read.2026-10-28-p508.tsv`](../evidence/api-shelf-read.2026-10-28-p508.tsv),
[`apac-2026-instruments.2026-10-28-p508.tsv`](../evidence/apac-2026-instruments.2026-10-28-p508.tsv).

🔴 **Gate posture: `make hooks` not run (`Code from External`) — a fourteenth denial in fifteen
passes.** Nothing below is gate-attested.

### 🆕 `T33` — the detector's abstention is not a denial

🔵 **`T31` taught this base to record a figure's *measure definition* beside its value. `T33` is the
same lesson one layer down, for licences: record what the FIELD measures, not only what it says.**

🟢 GitHub's `license.spdx_id` is the output of a **classifier over the licence payload**. Its
`NOASSERTION` means *"this text is not a recognised instance of a known licence"* — an **abstention**.
It does **not** mean *"no grant exists"*, and on these shelves it does not even correlate with that:

| address | `license.spdx_id` | payload at `raw.githubusercontent.com` | the truth |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `NOASSERTION` | `master/LICENSE` — **10,982 B**, `sha256 6dbc5b605ed0…`, title `Apache License / Version 2.0` + an appended *"Additional license statement for the openolat.org code base"* | 🟢 **Apache-2.0 with attribution** — a modified Apache, which is precisely what a classifier refuses |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🔴 `NOASSERTION` | `main/LICENSE` — **1,150 B**, `sha256 b8694396d7dc…`, `MIT License` + `<!-- SPDX-License-Identifier: MIT -->` + holder *GegoSoft Technologies* | 🟢 **A complete MIT grant** |
| [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | 🔴 **no `license` object at all** | `LICENSE` and `LICENSE.md` both **404**; `README.md` **9,179 B** opens `# DISCONTINUED` | 🔴 **Genuinely no grant** — the carried reading holds |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) *(control)* | 🟢 `MIT` | **1,092 B**, `sha256 e3321a1b62cd…` | 🟢 a recognised MIT — **58 B smaller** than `gegok12`'s, the difference being the SPDX comment |

🔴 **So the channel has three distinct states and this base was reading two of them as one:**
`spdx_id` present and recognised; `spdx_id: NOASSERTION` (**a payload exists, the classifier declined
it**); and **no `license` object at all** (no payload found). 🟢 **Only the third is evidence of no
grant.** `p507` collapsed the second into the third and published the collapse as a finding.

🔵 **And the aggravating fact is not the error — it is that the bytes were already on the shelf.**
[`open-gaps.md`](./open-gaps.md) records the `no-label` signal *"fires on `gegok12`'s plain **1 150-byte
MIT payload**"*. The byte count in that line and the byte count measured this pass are the same number.
🔴 **`T32` said the defect class was treating a citation as exhausted. `T33` is narrower and worse: a
recorded measurement was contradicted by a weaker channel and nobody checked the register.**

🟢 **`T33`'s rule, and it is one request:** before writing *any* licence verdict that turns on
`NOASSERTION` or on an absent field, `curl` the payload path and record **bytes + sha256 + title
block** — and grep this base's own register for the address first. 🔵 A `NOASSERTION` with a payload is
a **routing instruction**, not a verdict.

### 🟢 `Gap 504-A` — the control, finally run

🟢 `p504` asserted that on the API search channel *"a missing row and a nonexistent repo are the same
observation."* 🟢 **Proven:** `repo:openedx/edx-platform` and
`repo:zzzz-nonexistent-org-9931/nope-repo-9931` return the **identical** `Validation Failed` string.
🟢 **Tightened twice:** the silent drop reproduces at **batch size 2** (1 of 2 returned,
`incomplete_results: false`) so it is not a batch-size effect; and `openedx/frontend-app-learning`
still answers, so exclusion is per-repository. 🔵 **Four passes of reporting the symptom; one control
and two cheap probes to characterise it.**

### 🔴 The channel narrowed again, in the opposite direction to `p506`

| limb | `p506`/`p507` | `p508` |
|---|---|---|
| `api.github.com` (raw `curl`) | 🔴 403 | 🔴 403 |
| `github.com` HTML | 🟢 answered | 🔴 **403 at the CONNECT — gone** |
| `raw.githubusercontent.com` | 🟢 answered | 🟢 **200 — the only non-MCP channel left** |
| MCP GitHub search | 🟢 answered | 🟢 answered, with `OR` now rejected and `repo:` space-separation required |

🔵 **`p506` called the two broken channels complementary. One of the two complements is now gone**, and
every licence verdict above exists only because the byte limb survived. 🔴 **If `raw` goes next, no
licence on these shelves is verifiable from this session at all** — that is the single-point-of-failure
to state to anyone who inherits this base.

### 🟢 Saturation on the agent axis, declared rather than left as silence

🟢 **Nine discovery legs, ~80 distinct addresses, ZERO not already carried.** 🔵 The useful part is the
**query-shape** finding underneath it: multi-term free-text legs return `total_count: 0` even where the
shelves hold matching repositories (`LLM agent grading rubric assessment students stars:>80` → **0**,
against six carried grading repos), and the **Spanish-language leg returns 0** — so this channel cannot
discover LATAM-language work through free text. 🟢 **`topic:` plus a star floor is the only productive
shape**, and that is now written down where the next pass will look.

## 🆕 `p507` — `2026-10-28` — **🆕 `T32`: a gap this base has failed twice was answerable from a source it already cites — the failure was not the query but the ASSUMPTION THAT A CITED SOURCE HAD BEEN FULLY READ. 🟢 Every region now has a teacher-adoption rate from one instrument. 🔴 A widely-republished "MIT" education ERP has no licence at all.**

Reads: [`talis-regional-placement.2026-10-28-p507.tsv`](../evidence/talis-regional-placement.2026-10-28-p507.tsv),
[`new-addresses.2026-10-28-p507.tsv`](../evidence/new-addresses.2026-10-28-p507.tsv),
[`probe-errors.2026-10-28-p507.tsv`](../evidence/probe-errors.2026-10-28-p507.tsv),
[`channel-probe.2026-10-28-p507.tsv`](../evidence/channel-probe.2026-10-28-p507.tsv).

🔴 **Gate posture: `make hooks` not run (`Code from External`), a thirteenth denial in fourteen
passes.** Nothing below is gate-attested.

### 🆕 `T32` — the unread citation

🔵 **`p506` concluded that breaking the EMEA nil took *"a different instrument class, not a better
query."* `p507` finds a third possibility that is cheaper than either: the instrument was already
cited, and only part of it had been read.**

🟢 **`Gap 488-Q`** asked for an APAC teacher-adoption rate. It failed at `p488`, failed again, and
[`open-gaps.md`](./open-gaps.md) records the fallback as OECD TALIS 2024's global *"about one in
three"*, graded 🔴 *"global, not APAC, and pre-2026."* 🟢 **TALIS 2024 publishes per-country
notes.** This base has quoted TALIS for 🇧🇷**56** / 🇨🇱**55** / 🇨🇴**53** / 🇨🇷**52** since `p490`
— **the LATAM numbers came from the country notes.** The APAC and EMEA notes were simply never
opened.

🔴 **So the defect class is new and it is not the carry, the channel, or the query.** It is
**treating a citation as exhausted**: once TALIS was on the shelf as "the global one-in-three
figure", no pass asked what else TALIS reports. 🟢 **Registered as `T32` with a concrete remedy:
when a source is cited for one region, check whether it covers the others BEFORE opening a gap for
them.** That check costs one search leg and would have closed `Gap 488-Q` four passes ago.

🔴 **And the gap only half-closes, which `T32` must not be allowed to obscure.** The original
objection was two-part. The country notes answer *"not APAC"*; they do **not** answer
*"pre-2026"*, because TALIS 2024 is **2024 fieldwork**. 🟢 **Re-registered as `Gap 507-A`.**

### 🟢 The trend the data actually shows: the spread, not the average

| | |
|---|---|
| highest | 🇸🇬 Singapore **~75%**, 🇦🇪 UAE **~75%** |
| | 🇦🇺 Australia **66%**, 🇦🇿 Azerbaijan **59%**, 🇧🇷 Brazil **56%** |
| OECD mean | **36%** (🔴 Education International reports **~41%** for the same survey) |
| | 🇺🇸 US **43%**, 🇸🇦 Saudi **43%**, 🇩🇰 Denmark **36%** |
| lowest | 🇫🇷 France **14%**, 🇯🇵 Japan **<20%** |

🔴 **A five-fold spread inside one survey.** 🔵 The trend this base has been reporting — *"adoption
is rising everywhere"* — is true and nearly useless. **The usable trend is that national adoption
has diverged far more than regional labels can carry**, and a deck that says "EMEA adoption is X"
is averaging 🇦🇪 **75** with 🇫🇷 **14**.

🟡 **Training tracks use, which makes the gap addressable.** Singapore: highest use, highest
training (**76%**). France: lowest use, lowest training (**9%**). 🟢 **This is the strongest
argument in this base that teacher enablement is a product line and not a precondition.**

🟢 **And what teachers use AI *for* has not moved:** summarise or learn a topic **68%**, generate
lesson plans **64%** — **both preparation**. 🔵 Across the agent shelf, the market map and now a
probability sample, **the demand is teacher-side preparation; student-facing tutoring is where the
stars are and not where the usage is.**

### 🔴 A licence claim that travelled further than the licence

🔴 **`GegoK12` is published as MIT by its own site and repeated by comparison pages.**
[`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) — **54★ / 102 forks, Laravel,
`archived: false`** — reads **`NOASSERTION`**: GitHub detects **no OSI licence**. 🟢 `p501`'s
standing finding — **there is no MIT-licensed education ERP** — therefore survives its first real
counter-candidate. 🔵 **The trend worth recording: "open source" in the education-ERP segment is a
marketing register, not a licence claim**, and the only reliable test is `license.spdx_id` at the
repository.

🔴 **Same reading on the new agent tier.** Of the five highest-starred new education repos this
pass, **two are AGPL-3.0 and one is `NOASSERTION`**; only
[`OpenCat`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) (**MIT, 5,518★**) and
[`TorchLeet`](https://github.com/Exorust/TorchLeet) (**MIT, 2,595★**) can be built on. 🔵 **The
permissive tier keeps thinning as the attention tier grows** — now observed on new entrants, not
just the standing shelf.

### 🔴 Five probes, five false answers, and one nearly corrected a correct row

🔵 `Gap 506-B` requires a known-good **and** known-bad control before any count is published. **It
fired five times this pass and every count it blocked was mine**, including a *"200 from
`api.github.com`"* that would have retired `p505`'s correct **403** row — the 200 came from `/` and
`/rate_limit`, **neither of which can read a repository**, while every `/repos/` path returns 403.

🔴 **The one to remember is the `menthor` false defect**: the probe reported an archived repo being
recommended unflagged. **The repo IS archived — and the shelf already says so.** 🟢 **A true
premise plus an unchecked assumption produced a false correction**, which is more dangerous than a
false count because it would have edited a right answer into a wrong one. **Corrections require the
context read, not the hit.**

## 🆕 `p506` — `2026-10-28` — **🆕 `T31` (a verified number can still be the wrong number — this base has five instruments that grade whether a figure is CURRENT and none that grade what it MEASURES, and the defect is live in its own best commercial sentence). 🟢 The EMEA adoption nil is BROKEN after thirteen passes, and `T30`'s instrument-class prediction is confirmed. 🔴 `T24` saturation holds on a fourth shape: the prescribed discovery query now returns zero repositories.**

Reads: [`emea-adoption-instruments.2026-10-28-p506.tsv`](../evidence/emea-adoption-instruments.2026-10-28-p506.tsv),
[`channel-probe.2026-10-28-p506.tsv`](../evidence/channel-probe.2026-10-28-p506.tsv).
Full narrative: [`agents/trending.md`](../agents/trending.md) `p506`.

### 🆕 `T31` — **Every verification instrument on this base grades provenance. None grades meaning. That is a whole missing axis, and it is already costing.**

This base has built, over ~500 passes, an unusually disciplined verification stack: licence payload
digests, pinned blob SHAs, star re-read cadence, pin-drift detection, `archived`, queried-vs-returned
reconciliation, tag censuses. 🟢 **Every one of them answers the same question — *is this number
current, and is it attributable to the thing it is attached to?***

🔴 **None of them answers: *does this number measure what the sentence built on it claims?*** And
the live instance is in this base's own self-declared *"best commercial sentence"*:

| | what the shelf says | what the instrument says |
|---|---|---|
| Sanoma Learning 2026, >20,000 teachers, 14 countries | 🔴 **"63 % of European teachers use AI"** | 🟢 **63 % EXPECT TO USE AI TO PREPARE LEARNING MATERIALS**, up from **49 %** (2023–2025) |
| the argument built on it | 🔴 *"a 47-point gap"* against the 16 % who think general-purpose AI improves outcomes | 🔴 **two different measures — not one population, so not a gap** |

🔵 **The provenance chain was flawless and that is the point.** `p270` caught a *propagation*
defect on this very figure (the file claimed Sanoma was shelved when it was not), fixed it, and
re-ran the grep to prove the fix. **It propagated the number faithfully and never asked what the
number counted.** A press release and a report said different things; the base shelved the press
release.

🟢 **`T31`'s method rule, and it is cheap:** for any figure a *client sentence* rests on, record the
**measure definition** beside the value — population, denominator, and the verb (*uses* / *expects
to use* / *has ever used* / *uses at least sometimes*). 🔵 **Those four verbs are not
interchangeable and this pass met all four in one week of European teacher data**: DfE **44 %**
(*uses at least sometimes*), DfE School and College Voice **82 % / 78 %** (*has ever used*), Sanoma
**63 %** (*expects to use, for one task*), OECD **37 %** (*used for their job*, **lower secondary
only**). 🔴 **Quoting any two of them side by side as a trend is a fabrication**, and it is an easy
one to commit by accident.
🔴 **Second live instance, found by the same rule:** the OECD **37 %** is specifically **lower
secondary** teachers. `lower secondary` returns **zero** hits across every shelf while
*Digital Education Outlook* appears **14** times — the instrument is shelved, the scope qualifier
that makes the figure true is not. 🟢 The shelves' own **36 %** is left unchanged; the OECD's
summary page and its PDF disagree by a point and the primary is unreadable here.

### 🟢 `T30` confirmed on its own prediction — and the EMEA nil is closed

🔵 `T30` predicted the next real finding would be *"a named nil, not a search"*, and named the
instrument classes: **national ministry statistics, Eurostat**. 🟢 **Both delivered on the first
attempt**, after the prescribed regional query had failed thirteen times:

| figure | instrument | measure |
|---|---|---|
| **39.3 %** | 🟢 **Eurostat** | EU **16–24s** using generative AI **for formal education**, 2025 (**9.4 %** at 16–74) |
| **63.8 %** | Eurostat | EU 16–24s using generative AI **at all**, 2025 |
| **44 %** | 🟢 **DfE England** (*Technology in Schools 2024–25*) | teachers using GenAI **at least sometimes for school activities** |
| **~two-thirds / ~one-third** | 🟢 **Eurydice** (*Digital education at school in Europe 2026*, 22 Sep 2026, 38 systems) | systems with an AI policy instrument / with AI in the **curriculum** |
| **29.7 %** | OECD **TALIS 2024** via the European Commission | EU teachers with **any AI professional development** |

🟢 **The trend this establishes is not "EMEA adopted AI".** It is that **EMEA's deficit is
capability and governance, not uptake** — demand arrived informally and is now measured, while under
30 % of teachers have had training and only a third of systems teach AI in the curriculum.
🔵 **That is a different engagement shape from North America's**, where the binding constraint is a
policy mandate acting as a procurement trigger. Commercial consequence in
[`intel/market.md`](market.md) `p506`.

🔴 **Grade, and it is a hard limit on everything above: `SEARCH-ATTESTED, PRIMARY UNREAD`.** Every
non-GitHub host is refused at the CONNECT in this session and **`WebFetch` shares the same
allowlist** — so `Gap 483-K` generalises from the `europa.eu` family to **every host but
`github.com` and `raw.githubusercontent.com`**, and **WebSearch is the only open-web channel here.**
🔴 This also makes `Gap 505-F`'s Maryland primary **unclosable from this session**, by the same
attested mechanism as EUR-Lex.

### 🔴 `T24` — a fourth test shape, and the channel is what saturated

The prescribed `top open source AI agents education 2026 github MIT` returned **zero GitHub
repositories** — vendor blogs and SEO roundups naming only commercial products. 🟢 Earlier
saturation tests said *this base already holds the supply*; **this one says the discovery channel
itself is exhausted.** 🔵 Run the battery to attest, not to find; find on the API channel.

## 🆕 `p505` — `2026-10-28` — **🆕 `T30` (the prescribed discovery battery has now saturated on BOTH axes — supply and demand — so the binding defect class in this base is no longer discovery but PROMOTION BETWEEN SHELVES, and this pass found a live instance). 🟢 `T29`'s one-field `archived` check ran clean on every address. 🔴 Three instrument defects registered, one of which nearly wrote a false falsification onto `agents/top.md`.**

Reads: [`api-reconciliation.2026-10-28-p505.tsv`](../evidence/api-reconciliation.2026-10-28-p505.tsv).
Full narrative: [`agents/trending.md`](../agents/trending.md) `p505`.

### 🆕 `T30` — **The discovery battery is saturated on both axes. What still fails is promotion between shelves.**

`T24` established saturation on the **supply** axis: new topic sweeps return rows this base already
holds. 🔴 **This pass establishes the same on the DEMAND axis.** All eight prescribed queries were
run — four global, four regional — and **every** named instrument, institution and figure returned
is already shelved outside `archive/`: the two US bill-count trackers, five named state and federal
bills, Korea's AI Basic Act, Japan's AI Promotion Act, Singapore's AI Verify, Vietnam's high-risk
listing and its "sole basis" qualifier, Brazil's PL 2.338/2023, Chile's bill, the 716-instrument
count, UNESCO IESALC, TALIS 2024, Ceibal, the Digital Education Council survey, and
Regulation (EU) 2026/1744 with both its deadlines.

🔵 **The consequence is a reallocation, not a conclusion that the sector stopped moving.** When a
battery's marginal yield reaches zero, the defects it *cannot* see become the binding ones. This
pass went looking for those and found two classes, both live:

| class | instance found this pass | why a discovery sweep cannot see it |
|---|---|---|
| 🔴 **Figure-level promotion failure** | Maryland's **`S.B. 720`** is shelved on [`intel/market.md`](market.md) in seven places, but its **operative clock — 24 districts, 120 days** — existed only in [`agents/trending.md`](../agents/trending.md). The *instrument* was promoted; the *number that makes it a procurement trigger* was not | the datum is *present* in the base at instrument level, so every "do we have it?" query answers yes |
| 🔴 **Stale carry in PROSE** | **six** `DeepTutor` star cells (`46.0k`, `47,051`) across three shelves, while `p504` re-read the row to `47,338` | `p504`'s re-read updated shelf *tables*; the same figure also lives in prose and cross-shelf summaries, which no star sweep touches |

🟢 **Both are fixed this pass.** 🔵 **The method rule `T30` yields:** a pass should spend its budget
on *reconciliation between shelves* and on *named nils*, not on re-running a saturated battery. And
the cheap instrument for the carry class is **grep the previous value before commit** — which is how
six cells were found for the cost of one grep.

🔴 **`T30` comes with a warning this pass earned the hard way.** Reconciliation probes are
*themselves* a defect source, and the first draft of this pass published one: it grepped Maryland's
**popular name** (`AI Ready Schools`), found it only in a trending log, and reported the instrument
as unshelved. 🔴 **It was shelved all along, under its bill number `S.B. 720`.** The claim is
**retracted in [`market.md`](market.md) `p505`**, and the lesson generalises: **a reconciliation
probe that keys on one spelling of an identifier measures a naming convention and reports a content
defect** — the same shape as `p455`'s retracted 20.6 % sweep. 🔵 US instruments travel under bill
number, popular name and session-law citation; these shelves prefer the bill number and trending
logs record whatever the source used. **Grep both, or report nothing.**

🔵 **`T30` also predicts where the next real finding is**, and it is a named nil, not a search:
**EMEA has returned no education adoption RATE for twelve consecutive passes.** That cell will not be
filled by the prescribed query — it has now failed twelve times — but by a different instrument
class (national ministry statistics, Eurostat). 🔴 Until then, an EMEA pitch cannot cite a regional
adoption baseline while LATAM has four.

### 🟢 `T29`'s check ran clean, and it stays cheap

`archived` was read on all four addresses touched this pass: **`false` on all four**. 🟢 No repeat of
the `ably-labs/realtime-quiz-framework` defect, and the check continues to cost nothing on a call
that already returns stars.

### 🔴 Three instrument defects, registered because an unstated defect is a future false verdict

1. 🔴 **`Gap 505-A` — `pushed_at` is not a shipping signal.** `DeepTutor` returned
   `pushed_at: 2026-10-28T13:22:04Z` while `HEAD` (`a31d82624c27`, **7th consecutive pass**) and the
   version-sorted newest tag (**`v1.6.15`** of 87) were both unchanged. It advances on a push to any
   ref. **The draft of this pass's own section read it as a refutation of the shelf's "attention, not
   shipping" claim and was wrong.**
2. 🔴 **`Gap 505-B` — `p502`'s channel correction is channel-specific.** The MCP channel answers
   **200**; raw `curl` to `api.github.com` is **403**. The retired row was true of the channel it
   described, so the verification table needs a **channel** column.
3. 🔴 **`Gap 505-C` — a lexicographic tag sort misreads the newest release.** `ls-remote --tags |
   tail` gives `v1.6.9`; `sort -V` gives `v1.6.15`. Off `tail`, DeepTutor reads as having regressed.

### 🔴 `T5` / `Gap 483-K` — the EU primary text is unreadable from this session, definitively

`eur-lex.europa.eu`, `digital-strategy.ec.europa.eu`, `publications.europa.eu`, `op.europa.eu`,
`data.europa.eu`, `ec.europa.eu`, `europarl.europa.eu`, `consilium.europa.eu` and
`artificialintelligenceact.eu` are **all refused at the CONNECT (403)**, attested by the proxy's own
`connect_rejected` log. 🟢 **Grade unchanged: `SECONDARY-CONVERGENT, PRIMARY UNREAD`** — but the gap
is now characterised as a **host-policy denial of an entire domain family**, so it is **not a probe
to retry each pass**. `T5` keeps its dates and keeps naming the reading.

## 🆕 `p504` — `2026-10-28` — **🆕 `T28` (education AI supply is shifting from apps to AGENT SKILLS, and 9 of the 11 rows carrying it were created in 2026) and 🆕 `T29` (archived upstreams are an unmeasured liability — a one-field check no pass in ~500 had run, and it was hiding a frozen repo on two live shelves). 🟢 `T24`'s saturation reading survives a THIRD test shape: 35 candidates swept on three topic axes, 34 already held.**

Reads: [`api-shelf-reconciliation.2026-10-28-p504.tsv`](../evidence/api-shelf-reconciliation.2026-10-28-p504.tsv),
[`api-silent-omission.2026-10-28-p504.tsv`](../evidence/api-silent-omission.2026-10-28-p504.tsv).

### 🆕 `T28` — **The fastest-growing education supply is not applications. It is agent skills, and the shape has commercial consequences.**

Eleven addresses found on this pass's topic sweeps are not deployable products at all — they are
**skill packages for a coding agent** (Claude Code, Codex, Gemini CLI), shipped as prompts, rubrics
and scaffolds rather than as services:

| repo | ★ | created | what it packages |
|---|---|---|---|
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | **36,386** | 2026-05-01 | any technical book PDF → an agent skill |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | **987** | 2026-10-03 | books → animated, narrated interactive lessons; **emits SCORM** |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **918** | 2026-03-01 | **165** evidence-grounded skills for teachers and school leaders |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | **585** | 2026-03-07 | 30+ skills, K-12 → career, on a cognitive-science spine |
| [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | **498** | 2026-10-14 | topic → researched course of audio lessons with cited sources |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | **356** | 2026-06-24 | exam coaching with page-level citation to the learner's own slides |
| [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) | **299** | 2025-10-21 | DSA mentor: progressive hints, mock interviews |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | **294** | 2026-03-10 | Bloom's 2-sigma as a skill **plus** a self-hostable app |
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | **252** | 2026-06-26 | diagnosis-first tutoring with no mode menu |
| [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | **209** | 2026-04-06 | 🇨🇳 civil-service exam prep |
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | **119** | 2026-01-29 | 🇨🇳 teaching/tutoring skill collection |

🟢 **9 of 11 were created in 2026**, and the two oldest are 2025. **41,000★ in aggregate.** This is
not a long tail — it is a layer that did not exist two years ago.

🟢 **Why it matters commercially, and it cuts both ways.** A skill package is **pedagogy as
portable text**: no hosting, no model lock-in, no integration project, and it drops into a client's
existing agent. That makes the *content* — rubrics, prerequisite graphs, diagnostic sequences — the
asset, and content is the thing a studio can actually author for a client.
🔴 **And it is why this layer is a weak moat**: a skill is copied by reading it. The defensible part
is the measurement around it, which is the `evaluators` / `pedagogy-benchmark` tier this base
already shelves, not the prompt.

🔴 **Stated limit on this trend: licences were NOT read from bytes for these eleven rows.** They are
a supply-shape observation from topic metadata and descriptions, **not promotions**. 🔵 Four of the
eleven are 🇨🇳-language-first, which is consistent with `T26`'s finding about where the newest
supply originates and with the APAC note in [`market.md`](market.md) `p504`.

### 🆕 `T29` — **Archived upstreams are an unmeasured liability on these shelves, and the check costs one field**

The API returns `archived` on the same call as `stargazers_count`. No pass in ~500 had read it.
Reading it on all 87 shelf addresses this pass found:

| repo | ★ | how it was carried |
|---|---|---|
| [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 77 | 🔴 **recommended on TWO live shelves as "the permissive base for live classroom response"** — no end-of-life flag, ~20 passes |
| [`AgnellusX1/GodsEye`](https://github.com/AgnellusX1/GodsEye) | 30 | 🟢 already flagged archived since `p497` |
| [`sagefy/sagefy`](https://github.com/sagefy/sagefy) | 120 | 🔵 surfaced archived in this pass's sweep; never shelved |

🔴 **The failure mode is specific and worth naming**: `realtime-quiz-framework` had its **licence
verified from bytes**, its **star count verified**, and its **blob SHA pinned** — every expensive
check passed, and the free one that says *"this project is over"* was never run. 🟢 **`archived` is
now part of the standing batch read.** 🔵 A frozen upstream is not disqualifying for a pattern you
lift or a fork you own; it is disqualifying for a row that tells a client "build on this".

### 🟢 `T24` saturation — a third test shape, same answer

| pass | axis tested | novel finds |
|---|---|---|
| `p502` | topic vocabulary, 50★ floor | 0 above floor |
| `p503` | creation date, 90- and 180-day windows | 0 of 24 |
| **`p504`** | **three topic axes at LOWER floors** (`edtech` >120★ + pushed since 2026-09; `ai-tutor` >25★; `personalized-learning` >40★) | **1 of 35, and it is out of scope** |

The single novel address,
[`mikhashev/personal-context-manager`](https://github.com/mikhashev/personal-context-manager)
(**107★**), is 🔵 **not promoted**: its own description makes it a messenger-genesis
context-personalisation project with education adjacent at best, and the same axis also returned a
NeurIPS image-retrieval paper, so `topic:personalized-learning` is noisy rather than productive.
🟢 **Lowering the floor does not find supply — it finds noise.** The binding constraint on this base
is the **promotion backlog**, not discovery, and that has now been tested three independent ways.

## 🆕 `p503` — `2026-10-28` — **🆕 `T26` (the newest supply is deliberately non-commercial, and the metadata hides it) and `T27` (agentic is a sized segment now); 🟢 `T24`'s saturation reading survives a test on a different axis — date instead of vocabulary; 🔴 and this file's own gate suite was run for the first time in ~26 passes: 48/63 green.**

### 🆕 `T26` — **The newest, fastest-growing education supply is deliberately non-commercial, and GitHub's metadata will not tell you**

Six rows with real traction and no shelf, licence read from bytes at a pinned SHA:

| licence family | rows | buildable for a paid engagement |
|---|---|---|
| 🟢 MIT | **3** | yes |
| 🔴 **PolyForm Noncommercial 1.0.0** | 1 | **no** — source-available |
| 🔴 AGPL-3.0 | 2 | only as a platform the client hosts, never as a component |

🔴 **The fastest-growing row is the unusable one.** [`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch)
went **385★ → 739★ in 14 days (+92%)** on an unchanged 4 635-byte **PolyForm Noncommercial**
payload, and the GitHub API reports its licence as **`NOASSERTION`**. 🔵 This is the **second**
non-OSI family found behind that label on these shelves — `p500` found Elastic License 2.0 on
`canyongbs/advisingapp` (340★) the same way.

🟢 **Why this is a trend and not a licence note:** the cohort is young (all six created inside
180 days) and the non-commercial choice is *deliberate and explicit* — PolyForm and AGPL are not
accidents of a template. Authors shipping education AI in 2026 are increasingly choosing grants
that **block the consultancy use case specifically** while remaining open to individuals. 🔴 The
practical consequence: **licence must be read before architecture**, and from bytes — a star count
is a popularity signal and `NOASSERTION` is not a licence.

### 🆕 `T27` — **"Agentic" stopped being a narrative and became a sized segment**

| | 2026 | horizon | CAGR |
|---|---|---|---|
| 🆕 Agentic AI in education + learning technologies (Mordor Intelligence) | **$2.37B** | $11.83B (2031) | **37.92%** |
| AI in education, whole market (Precedence / Grand View) | $9.58–11.4B | $136.79B (2035) | 25–43% |

🟢 **Agentic is about a fifth to a quarter of 2026 AI-in-education spend and compounds faster than
the category.** 🔵 Mordor adds the structural claim this base's `T6`/`T13` already imply from the
supply side: **tutoring is the gateway purchase that seeds platform penetration.** 🔴 One firm, one
methodology, no cross-check — a proposal may cite it, a shelf may not treat it as measured.

### 🟢 `T24`'s saturation reading survives a test on a different axis

`T24`/`Gap 498-A` hold that this base has largely read the education-AI supply; `p501` briefly
refuted it at 65% novelty and `p502` showed that figure was an artefact of the axis
(`topic:ai-in-education`). 🔵 The remaining doubt was that **every** such measurement is an axis
artefact. 🟢 **Tested by slicing on date instead of vocabulary:** `created:>2026-07-28` with
`stars:>50` (60 rows) and `created:>2026-04-01` with `stars:>25` (20 rows) → **0 of 24 read rows
new to this base.** 🟢 `T24` stands on two independent slicing dimensions. 🔴 And the corollary is
`T28`-shaped but not yet a trend: what the base fails at is **promotion**, not reading — 6 of 18
audited rows have never reached a shelf.

### 🔴 The gate suite was run, and it already knew

`Gap 446-A` has recorded *"`make hooks` was not run"* for ~26 passes. 🟢 Run this pass:
**48/63 green, 15 red**. 🔴 `gate-promotion` — a gate that has existed in the `Makefile` the whole
time — prints exactly the class of defect `p502` wrote prose about:
`wenflow-org/wenflow` (MIT, 59★) and `zhangl1001/civil-ai` (MIT, 41★), both marked **"Promoted"**
in a promotion table in [`agents/trending.md`](../agents/trending.md) and present on **no** curated shelf.
🔵 **The lesson is about instruments, not about these two rows:** this base builds gates faster than
it runs them, and an unrun gate is indistinguishable from a missing one. Full log:
[`hooks-run.2026-10-28-p503.log`](../evidence/hooks-run.2026-10-28-p503.log).

### Declared gaps

| id | statement |
|---|---|
| 🆕 **`Gap 503-A`** | **`p502`'s channel row is too wide.** The GitHub REST API answers *search* for arbitrary repositories and **refuses *contents*** outside the session's attached repos. Licence bytes still come from `raw.githubusercontent.com` at a `git ls-remote` SHA — the two-channel rule is unchanged and the verification table in `agents/top.md` has been corrected in place |
| 🆕 **`Gap 503-B`** | **Four registry channels are blocked by network policy** — `download.moodle.org`, `codeberg.org`, `huggingface.co`, `api.npmjs.org` (`000` ×3 each). So `Gap 500-A`'s *"LMS plugin registries"* axis and any demand-side (download-count) ranking are **unreachable from this session**, not unmined. Same class as `Gap 499-C`'s `gnu.org`: needs a policy change, not a pass |
| 🆕 **`Gap 503-C`** | **A third of what this base reads never reaches a shelf** — 6 of 18 audited rows, measured. 🔴 Three were promotable and are now promoted; three are licence-walled. Open: the audit covered one 90-day slice. **What is the shelf rate over the whole trending history?** `gate-promotion` cannot answer it — it reports `2877` rows ungraded by its own reach bound |
| 🆕 **`Gap 503-D`** | **A bare 12-hex payload token on these shelves is a sha256 prefix, not a git blob SHA-1.** `MANIFEST.tsv` carries both columns; shelf cells carry one unlabelled token. Fixtures: `wenflow-org/wenflow` 1 067 B → blob `2611735149f3`, sha256₁₆ `b6fac57d47103d5f` (published cell: `b6fac57d4710`). 🔴 A successor verifying with `git hash-object` reports **DRIFT on an unchanged payload**. Every p503 hash is labelled; the back history is not |
| 🆕 **`Gap 503-E`** | **Writing "Promoted" in a trending narrative is not a promotion.** `agents/trending.md:6517-6518` marks two MIT rows promoted; no shelf carries them. `gate-promotion-ledger`'s ratchet has risen to **197 un-landed claims against a pin of 148** |
| 🆕 **`Gap 503-F`** | **`OpenEduCat`'s interoperability claims (LTI 1.3, OneRoster, Ed-Fi, SCORM/xAPI) are vendor-sourced and unverified**, and its published pricing is internally inconsistent across its own pages. This base holds an LTI corpus to compare against and has not read the module |
| 🟡 carried | 🔴 **`Gap 446-A` is answered, not closed.** The suite ran: **15 gates are red**, including `recount`, `gate-shelf-consistency`, `gate-grant-path`, `gate-census-union` and `gate-cell-reproduction` (*"zero published cells parsed — a parse fault"*). A green suite is a separate project from a run suite |

---
## 🆕 `p501` — `2026-10-28` — **🆕 `T22` and `T23`; 🟢 `T15` extended with the two jurisdictions it named as missing; 🔴 and one measurement this file published as a sector property is re-read as a property of a search axis.**

### 🔴 `p499`'s saturation reading was about an axis, not the sector

This file and [`agents/trending.md`](../agents/trending.md) have carried `p499`'s finding that
education-AI supply in the 50–400★ band is **largely already read** — novelty **19.2%**, which
`Gap 498-A` closed *"BY REFUTATION"*. 🔴 **Re-measured this pass on `topic:ai-in-education`, an axis
never swept here: 13 of 20 rows are new — 65%.** Same sector, same week, **3.4×** the novelty.

🔵 **Nothing in `p499`'s method was wrong.** It measured the axis it swept and reported the number
honestly. The error is in how the number was *carried*: a saturation figure is only a sector claim if
the sampling frame is the sector, and this base's frame is `topic:edtech` plus named-project queries.
`Gap 499-I` already warned that the permissive-share move was *"a selection effect… the denominator
is this shelf, not the market"*. **This is the same defect on a different statistic, and it was
published anyway.** See `Gap 501-A`.

### 🆕 `T22` — The sector labels itself in two vocabularies, and they barely overlap

`topic:edtech` and `topic:ai-in-education` are **near-disjoint populations on GitHub**, not two views
of one. Measured on `ai-in-education` page 1 (20 of a stated 128 rows):

| | n | share |
|---|---|---|
| new to this base | **13** | **65.0%** |
| known, narrative only | 5 | 25.0% |
| known, on a curated shelf | 2 | 10.0% |

[`GeminiLight/SocialCoach`](https://github.com/GeminiLight/SocialCoach) — **Apache-2.0, 438★, 57
forks** — carries `ai-in-education`, `personalized-learning`, `social-emotional-learning` and **not
`edtech`**. No `edtech` sweep, at any star band or depth, could have returned it.

🔵 **Why this is a sector trend and not just a tooling note:** the split tracks *who built the
repo*. `edtech` is the **vendor and platform** vocabulary — LMS plugins, SIS integrations, standards
tooling. `ai-in-education` is the **practitioner and researcher** vocabulary — a teacher's skill
pack, a lab's audit, a classroom tool one person shipped. The two populations differ in size by an
order of magnitude and in licence posture too: `p500` found a **licence wall** on the `edtech` band
(only 4 of 31 residual rows permissive-and-live), while **10 of 13** new `ai-in-education` rows are
permissive.

**Consequence:** on an engagement, **query both vocabularies and expect different answers from
each.** Looking for a platform to extend → `edtech`, and budget for copyleft. Looking for a
practice-level agent to compose → `ai-in-education`, and expect MIT, small repos, no releases and
sometimes no licence at all. 🔴 **This base has swept one of the two for eleven passes.**

### 🆕 `T23` — Social-emotional learning is a real layer and this base had nothing on it

Before this pass, `social-emotional` and *"social emotional"* returned **0 hits across
[`agents/top.md`](../agents/top.md), [`agents/trending.md`](../agents/trending.md), this file and
[`verticals/solutions.md`](../verticals/solutions.md)**. Every tutoring row here is **cognitive**:
knowledge tracing (`OATutor`), content generation (`educhain`, `Skill-Anything`), lesson planning
(`k12-teacher-skills`, `Shiksha-Copilot`), classroom simulation (`OpenMAIC`), plagiarism detection
(`dolos`).

🟢 `SocialCoach` is the counter-instance and its **57 forks against 438★** read as use rather than
stargazing — role-play for conflict handling and communication with personalised feedback.

**Consequence:** *"AI tutor"* is two different products. An engagement that means **soft skills —
interview practice, conflict resolution, communication, SEL curricula** — was served by nothing on
these shelves until this pass, and is still served by **exactly one row with no release and no
tag**. 🔴 **Scope the word "tutor" explicitly in discovery.** 🔵 And note what SEL does to the
regulatory picture: a system coaching a child's emotional conduct sits closer to the EU's Annex III
*"evaluates learners"* line and to NYC's red tier than a maths tutor does, while being **less**
measurable — the evidence-of-learning demand `T13`'s successors describe has no obvious instrument
here.

### 🟢 `T15` extended — Kenya, Nigeria and Rwanda, the two gaps it named and one more

`T15` closed with *"🔵 Kenya and Nigeria remain **unmeasured** here despite an explicit by-country
query."* Both are now measured, and they **strengthen** the trend rather than qualify it:

| jurisdiction | instrument | what it shows |
|---|---|---|
| 🇰🇪 Kenya | **National AI Strategy 2025–2030** (MICDE), non-binding | 🟢 The **most education-explicit** African instrument found: AI literacy across education, **DigiKen** curriculum hubs. 🔴 Publication date conflicts between sources (March 2025 vs December 2025). |
| 🇳🇬 Nigeria | **National AI Strategy (2024)** (NITDA/FMCIDE), non-binding | 🔴 Its own education analysts: application in education systems *"remains aspirational rather than systemic"* — **policy present, implementation absent**, which is precisely `T15`'s claim. |
| 🇷🇼 Rwanda | **National AI Policy** + a **three-year Government-of-Rwanda ↔ Anthropic MoU (February 2026)** | 🟢 Model access and intent are settled; **delivery is the open question**. 🔵 An MoU is not an outcome. |

🔵 **`T15` holds and sharpens: the African constraint is not the absence of policy — policy is now
documented in four jurisdictions — it is capability and language.** Kenya and Rwanda name
curriculum and literacy; Nigeria's own reading is that the strategy has not reached systems; and
Ethiopia's reported obstacle remains Amharic and Afaan Oromo model quality. 🔴 Every one of these
instruments is **non-binding**, so unlike the EU or North Carolina there is **no deadline** driving
procurement.

🔴 **One instrument may have been retired and this base cannot confirm it.** South Africa's draft
National AI Policy 2026 — which `p500` placed here — is recorded by one general-reference source as
**abrogated 27 April 2026**. Read second-hand; the government's own publication was not reached.
**Flagged, not acted on** (`Gap 501-I`).

### 🔴 The APAC teacher rate is being supplied by invention

`Gap 488-Q` has asked for an APAC teacher-adoption rate for several passes. A dedicated query this
pass returned **three** figures and **all three fail verification**: 86% of SEA teachers (secondary
blog citing a publisher whose own material does not carry it), >95% of Chinese secondary schools
(aggregator, no source), 68% of Indian rural schools (aggregator, no source, and it counts schools
not teachers). The one credible cross-country figure is **OECD TALIS 2024's "about one in three"** —
global, and pre-2026.

🔵 **This is a trend about the information market, not the education market: a widely demanded
number that nobody has measured gets manufactured.** Anything on these shelves quoting a regional
teacher-adoption rate should be assumed to trace back to one of these three until a probability
sample appears.


# Education AI — current trends

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it: T4 and T5 updated, **two new trends (T11, T12)** added, and three declared gaps
narrowed. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/trends.md`](../archive/2026-10-27-p490-pre-rewrite/trends.md).

## T1 — Adoption is finished; institutional delivery is the gap

86% of students across 16 countries already use AI. In LATAM higher ed, **92% of students and
79% of faculty** use it, while **only 30% of students** say their institution's own AI use meets
expectations. K-12 teacher use doubled in a year (25% → 53%, RAND).

**Consequence:** nobody needs to be sold on AI tutoring. The buyable thing is the institution's
*sanctioned, integrated, governed* offering. Pitch delivery and governance, not capability.

## T2 — The education platform layer is copyleft, and this is now the binding constraint

Read from bytes this pass: of 16 foundational platforms, **3 are permissive**. Moodle (GPL-3.0),
Open edX (AGPL-3.0), Canvas (AGPL-3.0) — every incumbent is GPL or AGPL. Only OpenOlat
(Apache-2.0), Kolibri (MIT) and Oppia (Apache-2.0) permit a closed derivative.

**Consequence:** platform choice is a *licensing* decision before it is a technical one. If a
client wants hosted closed SaaS, the incumbent-LMS route is unavailable and the shortlist is
three repos long.

## T3 — "Open source" claims in this market are unreliable at the family level

This pass refuted, from bytes: `frappe/lms` is **AGPL-3.0, not MIT** as currently published;
`tutor-gpt` is **GPL-3.0**; `microsoft/autogen` serves **CC BY 4.0 at `LICENSE`** with the code
grant at `LICENSE-CODE`. Star figures were off by **31×** (`educhain`: 387, not ~12,000) and ~5×
(`OATutor`: 274, not ~1,500).

**Consequence:** never accept a license or a star count from a listicle, a vendor page, or this
KB's own history. Read the grant at a pinned SHA. The reader must anchor on the **title block** —
a body scan matches the GNU preamble's cross-reference and misgrades GPLv2 as LGPL (this pass's
own first run did exactly that).

## T4 — Regulation has split into four incompatible regimes, and that is a product requirement

| Regime | Mechanism | Live date |
|---|---|---|
| EU | risk tiers; **provider** carries conformity duties | Art. 50 marking **2 Dec 2026**; high-risk **2 Dec 2027** |
| South Korea | comprehensive mandatory AI Basic Act | **22 Jan 2026** |
| China | service filing + AI-content labelling | 988 services filed by **30 Jun 2026** |
| India | IT Rules: labels + provenance markers | **20 Feb 2026** |
| **Vietnam** | AI law **+ education named a high-risk sector** (Jul 2026 decision) | law **1 Mar 2026** |
| Japan | non-binding promotion | AI Basic Plan **14 Jul 2026** |
| US | state patchwork, no federal law | varies |
| LATAM | **no statute found** | — |

**Consequence:** jurisdiction behaviour (labelling, provenance, filing, oversight gates) belongs
in configuration, not in a fork per market.

🟢 **Updated `p491`: the count of regimes naming education specifically as high-risk is now two.**
The EU (Annex III) and **Vietnam** (July 2026 decision). South Korea's Basic Act carries a grace
period putting **penalties at roughly Jan 2027**. The regimes are diverging in *timing* as well as
in *mechanism*, which strengthens the configuration argument rather than weakening it.

## T5 — The EU deadline slipped 16 months and created a window

Regulation (EU) 2026/1744 (the Digital Omnibus) moved stand-alone high-risk education systems
from **2 Aug 2026 to 2 Dec 2027**. Article 50 transparency was *not* moved.

**Consequence:** a 14-month window to arrive conformant rather than remediate.

🟢 **Updated `p491` — the chronology is now firm, the primary read is still not done.** Ten
independent secondary sources converge: EP approval **16 Jun 2026**, Council adoption
**29 Jun 2026**, OJ publication **24 Jul 2026**, in force **27 Jul 2026**. What moved is
**Chapter III, Sections 1–3 of Regulation (EU) 2024/1689**; sandboxes move to **Aug 2027** and that
duty binds Member States. **Not moved:** Article 50, the prohibitions, the GPAI obligations.
🔵 `eur-lex.europa.eu` **does not resolve from this session's network**, so the OJ text remains
unread — convergent commentary is better evidence than p490's "secondary commentary", and still
not primary. Address for the next pass: `eur-lex.europa.eu/eli/reg/2026/1744/oj`. 🟡 Many guides,
**including a live DLA Piper update**, still describe the Omnibus as under negotiation — treat any
undated AI-Act guide as wrong by default.

## T6 — Emotion recognition in education is banned outright in the EU

Prohibited since **2 Feb 2025**. Not high-risk-with-conditions: **banned**.

**Consequence:** engagement-detection, attention-tracking and sentiment features — common in
proctoring and "engagement analytics" pitches — are not shippable in the EU at any price. Check
every roadmap for them before an EMEA pitch.

## T7 — Agent tool surfaces are arriving at the LMS boundary, unevenly

Canvas has a real, maintained MCP server ([`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp),
MIT, 309★) with ~102 tools, a published prompt-injection advisory (GHSA-hmr8-mvr2-mvw5), and —
notably — source that states a confirmation token does not prove a human approved anything.
Moodle and Open edX have no equivalent at a usable star floor.

**Consequence:** Canvas engagements can start at the agent layer. Moodle/Open edX engagements
must budget the connector as build work.

## T8 — Write-capable education agents are a real safety surface, not a hypothetical

`canvas-mcp`'s tool population distinguishes read-only from destructive hints explicitly, and a
prior first-hand read of its write tools found a subset carrying **none** of its three
write-safety mechanisms — one of which writes a grade.

**Consequence:** any education agent that can write grades, enrolments or feedback needs an
effect taxonomy, an operator allowlist and content-bound confirmation **designed in**. Grades are
a high-stakes decision under both EU high-risk rules and several US state laws.

## T9 — Offline-first is a regional differentiator, not a legacy feature

Kolibri (MIT) is the only permissive offline-first platform found. Rural LATAM, Africa and parts
of APAC cannot assume connectivity, and national programmes are exactly where the public money is.

**Consequence:** for ministry-scale LATAM/APAC work, offline capability plus MIT licensing makes
Kolibri the default base — a combination nothing else on the shelf offers.

## T10 — Market sizing in this sector is not currently usable

2026 estimates span **$6.4B–$12.3B** (~2×). Two figures this KB published are retired this pass
as unsupported: the "$42.48B by 2030 / 41.5% CAGR" pair, and "LATAM $1.5B → $4.2B" (contradicted
~12× by the only current regional sizing found). One widely-quoted $11B figure is called a
"final guess" by its own author.

**Consequence:** quote ranges with the firm named, or quote nothing. Never put a single
AI-in-education market number in a client deck without a primary source.

## T11 — The education-AI evaluation instruments now exist, and 🟢 **one of them is MIT** (`p493` correction)

This reverses the shape of the sector's biggest gap. `p490` reported the tier as empty. Measured
from bytes this pass: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (45★,
**EMNLP 2025 Oral**, 3 teacher skills × 7 tasks) and
[`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) (0★, KAIST, 923 dialogues)
are real, serious, and **ship no license file at all**. MathTutorBench's README contradicts itself —
badge `CC BY 4.0`, closing line `CC BY-SA 4.0` — and **neither is a software grant**; Creative
Commons advises against CC licenses for code, and one of the two is copyleft.

🔴 **`p493` — the "not one of them is licensed" claim in this trend's title and body is false.**
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) is
**MIT** (1 064 B, `sha1 ac3710f1a312`, read at `21a43a395ab4`; sidebar and README agree). It is
education-specific and substantive: **1,143 questions from teacher-qualification exams**, split
**920 CDPK** (cross-domain pedagogical knowledge) and **223 SEND** (special educational needs and
disabilities), with harness support for *"100+ models"*, behind *Benchmarking the Pedagogical
Knowledge of Large Language Models* (`arXiv:2506.18710`). 🔵 **It was read by this KB on
`2026-10-18` and dropped from the shelf by `p490`'s rewrite** — so this trend was built on an
incomplete shelf, not on an incomplete sector. See [`agents/trending.md`](../agents/trending.md)
`p493`.

**Consequence, restated.** The tier is **small and under-starred, not unlicensed**:

- 🟢 **Takeable now:** `pedagogy-benchmark` — **MIT**, so the exam-derived item bank *and* the
  multi-model harness are usable as code and data, not merely readable as a paper.
  🔴 **13★, 5 commits, no security process** — a corpus and a baseline, not a maintained
  dependency.
- 🔴 **Still blocked by licensing:** `mathtutorbench` (45★) and `TutorCaseBench` (0★) ship no grant
  at all. Their papers are readable and their *task designs* reimplementable; their repositories
  are not usable. MathTutorBench's self-contradicting README (badge `CC BY 4.0`, closing line
  `CC BY-SA 4.0`) stands as recorded, and neither is a software grant.
- 🟢 **So the eval capability is no longer a build from nothing, and no longer a build from a bare
  runtime either.** Start from `pedagogy-benchmark`'s MIT items and harness, keep
  [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
  (**MIT**, 14,300★, 1,066 B) underneath, and implement the two unlicensed instruments' published
  task designs on top.

🟢 **Why this matters commercially, unchanged and now cheaper to reach:** this is still the
clearest open-source credibility asset in the sector, and EU high-risk conformity will demand
exactly this evidence by **2 Dec 2027**. `p493` moves the starting line, not the deadline.

## T12 — A national AI mandate is not a durable demand floor: South Korea de-mandated one

South Korea planned **mandatory AI digital textbooks from 2025**. Adoption sat **below 30% by
March**, and in **August 2026 the National Assembly stripped them of official textbook status.**
Meanwhile China runs the opposite experiment successfully — **AI compulsory from age six since
Sept 2025**, with provincial contact hours (**Beijing 8 h/year**; **Guangdong 6 h**, rising to
**1 h/fortnight in grades 10–11**).

**Consequence:** government mandates in this sector are reversible within roughly a year, and
low adoption is the mechanism that reverses them. Two things follow for public-sector work.
**Price and stage it to survive de-mandating** — no engagement economics that only clear if a
mandate persists for its full term. And **treat teacher adoption as the contractual risk**, not
procurement: Korea's mandate did not fail on policy or technology, it failed at under-30% uptake.
That makes change management and teacher training the load-bearing deliverable, which is also the
part most often cut from a bid to win it.

## Declared gaps

- **EMEA: adoption gap partly closed, vendor-share gap still open.** `p491` added European sizing
  (**$2.64B 2026 → $8.0B 2030, 31.9% CAGR**), the first named K-12 leaders (**Finland, Estonia,
  Netherlands**), and a governance contrast (**~70%** of institutions in Europe/NA have AI guidance
  vs **45%** in LATAM & the Caribbean). 🔵 Still **no vendor-by-vendor European market share** —
  searched again this pass, still absent.
- **APAC: mandate structure now documented, adoption rates and vendor share still missing.**
  `p491` added China's compulsory-subject mandate and provincial contact hours, Korea's textbook
  reversal, Japan's 2030 digital-textbook horizon and Vietnam's high-risk education classification.
  🔵 Still **no institution-level adoption rate** for China, India or Japan and **no edtech vendor
  share for any APAC market**.
- **LATAM: still no AI-in-education statute in force — now with the reason.** Brazil's
  **PL 2338/2023** passed the Senate **10 Dec 2024**, reached the Chamber **17 Mar 2025**, and is
  **still in special committee awaiting the rapporteur's report** as of Oct 2026; an end-May 2026
  plenary vote did not happen. 🟡 Whether it names education high-risk is **claimed by one vendor
  blog and unconfirmed** — the sources describing its risk tiers do not mention education. Mexico:
  nothing found, again.
- **No *usable* education-AI evaluation harness exists — restated, not closed.** See **T11**: the
  instruments exist and **carry no license**. This is still the largest structural gap in the sector
  and the clearest build opportunity; what changed is that the obstacle is now known to be
  licensing rather than absence, and a permissive runtime base (`lm-evaluation-harness`, MIT)
  has been identified.
- **No maintenance signal for any repo on these shelves.** Stars and license bytes are readable on
  this session's channels; **latest-commit dates are not** (`api.github.com` is 403 for unattached
  repos, and page fetches returned commit counts without dates on every repo tried this pass). No
  file in this KB can currently distinguish an actively maintained project from an abandoned one —
  which matters most for the small rows, where abandonment is likeliest.


## 🆕 `p492` — `2026-10-28` — two trends move from thesis to evidence

### 🔴 `T8` is now closed: write-capable education agents are a demonstrated safety surface

`T8` has argued since it was written that this is "a real safety surface, not a hypothetical."
**That argument is over.** [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — the single
most deployable education-agent integration in this KB, and the base of pattern `P490-1` — now
publishes **four** security advisories in `v1.16.0`, where this KB had recorded **one**:

| advisory | subject | why it is the whole blast radius |
|---|---|---|
| `GHSA-7mj9-4mcg-hvhv` | **Canvas token handling** | The engagement hands this server an **institutional** Canvas API token. Read-only *tool* scoping does not protect the *token*. |
| `GHSA-7pp5-29mw-9jq3` | **local code sandbox** | Code execution reachable from an agent loop driven by **student-authored text**. |
| `GHSA-hmr8-mvr2-mvw5` | **file content fencing** | The one already carried — though upstream's words are *file content fencing*, not this KB's gloss of "prompt-injection path". |
| `GHSA-qf6c-jv93-38gv` | **Windows download permissions** | Low relevance on Linux hosting; still live. |

🟢 **The useful generalisation.** Four CVE-class advisories on a **309★, MIT, actively maintained,
security-policy-carrying** project is not a sign of a bad project — it is the **opposite**. It is
what a project looks like when it takes an exposed surface seriously and discloses. **The trend is
that the LMS agent boundary is now understood to be a security boundary**, by the maintainers
first. Treat any education MCP server with **zero** advisories as unexamined rather than safe.

🔴 **Operational rule this yields:** on an LMS agent integration, the **credential is the primary
asset**, not the tool scope. Scope tools *and* isolate the token. `P490-1` is amended accordingly.

### 🟢 `T2` holds, but the permissive numerator moved for the first time in three passes

`T2` ("the education platform layer is copyleft, and this is now the binding constraint") **stands
— 16 of 20 platforms are copyleft.** The correction is narrow and worth carrying:
[`apache/openmeetings`](https://github.com/apache/openmeetings) is **Apache-2.0** (51 425 B) at
**688★**, giving the **virtual-classroom** layer its first permissive option. The census goes
**19 → 20 platforms, 3 → 4 permissive**.

🔵 **It changes no conclusion.** No permissive **SIS** exists; no permissive **assessment/QTI**
engine exists; the only permissive **full LMS** is still `OpenOLAT`. And BigBlueButton (LGPL-3.0)
is **13×** OpenMeetings' size and stays the default. **The constraint is intact; one cell in it is
not as tight as this KB claimed.**

### 🟢 A new trend, `T13` — the education agent-skills tier is consolidating off hosted infrastructure

[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
(**917★**, `v3.1.0` dated **2026-10-22**) is **retiring its hosted public MCP service** in favour of
a **local MCP server**, with hosted access now gated behind an **auth token**. It ships composition
for **Claude, OpenAI Codex and Hermes Agent**, plus a portable ZIP edition — **165 skills across 20
domains**, of which domain 20 is **13 student-facing** skills.

**Two things to take from this:**

1. 🔴 **Its licence is `CC BY-SA 4.0` — content copyleft with ShareAlike, not a software grant.**
   ShareAlike propagates to *adapted* material, so lesson plans, rubrics and curriculum **derived**
   from these skills inherit the obligation. **Read it; do not ship it inside a proprietary
   deliverable.** That is a licence conclusion, not a quality judgement — the skills are
   evidence-graded and good.
2. 🟢 **The direction of travel is local, not hosted.** The largest education skills library in
   existence is moving *away* from a hosted endpoint. Anyone who demoed against the hosted MCP URL
   has a **migration**, not a config change. Design education-agent work for a **locally-run MCP
   server** by default.

### 🟢 Channel and method corrections (they belong in this file too)

- 🟢 **A standing gap in three files was overstated.** "No maintenance signal is available for any
  row" is **false for repos that tag releases** — release names and dates read fine via page fetch
  (`v1.16.0`, `v1.6.15` `2026-10-19`, `v3.1.0` `2026-10-22`, `v9.1.0`). **Liveness is readable.**
  Only untagged repos lack a signal.
- 🔵 **The `github.com` `curl` `403` is this session's own proxy access gate**, returning a JSON
  body that says so — **not** GitHub rate-limiting and **not** evidence a repo is missing. It
  carries zero information about existence. Open since `p472`, now diagnosed.
- 🔵 **Licence bytes must be measured with `curl -o file`.** `$(curl ...)` strips trailing newlines
  and undercounts by one byte, which **presents exactly as licence drift**. `p492` produced one
  byte of phantom drift this way before re-measuring. **Phantom drift is how a KB starts lying
  about licences.**
- 🔵 **Add lowercase `license` to every licence probe list.** `labmlai`'s MIT grant lives there, and
  a probe trying only `LICENSE`/`LICENSE.md` would call an MIT repo unlicensed.


## 🆕 `p493` — `2026-10-28` — a trend correction, and a method rule this KB needed

### 🔴 `T2`'s scope was too broad, and `T11` was simply wrong

Both corrections have one cause: **`p490`'s full-file rewrite of `agents/top.md`, and the earlier
rewrites of `repos/foundations.md`, deleted eight rows that previous passes had promoted** — with
no marker left behind, so the shelves then read as complete censuses. Full account and the
re-verified rows: [`agents/trending.md`](../agents/trending.md) `p493`.

| trend | published claim | `p493` |
|---|---|---|
| **`T2`** | "The education platform layer is copyleft, and this is now the binding constraint" | 🟡 **True of the LMS/SIS/assessment core only.** `OpenMAIC` (**MIT, 41,700★**, courseware), `open-tutor-ai-CE` (**BSD-3-Clause**, tutoring platform), `dolos` (**MIT**, integrity) and `pedagogy-benchmark` (**MIT**, evaluation) are all permissive and were all already in this KB. **Narrow the claim to the core; it is still true there and still binding there.** |
| **`T11`** | "not one of them is licensed" | 🔴 **False** — `pedagogy-benchmark` is MIT. Corrected in place above. |

🟢 **`T2`'s core survives and is worth restating precisely**, because the precise version is the
one that holds up in a client conversation: **the full LMS, the SIS and the assessment/QTI engine
are copyleft-bound** — `OpenOLAT` (Apache-2.0, 448★) is the only permissive full LMS, no permissive
SIS exists, no permissive QTI engine exists. Everything *above* that core now has a permissive
option. See [`repos/foundations.md`](../repos/foundations.md) `p493`.

### 🆕 `T14` — in this sector, a KB's own bookkeeping is a material source of error

Not a market trend; a trend in **how this KB fails**, recorded because it has now produced three
published falsehoods in two passes.

- `p492` declared a gap (Learning Commons licences unreadable) over evidence this KB had held since
  `p119`/`p120`. The pass searched the open web instead of `grep`-ing the repository it was editing.
- `p490`/`p491` published two "declared gaps" in `agents/top.md` that this KB's own trending log
  refuted: the permissive-agent gap (refuted by `OpenMAIC`, cited **51 times** in this KB's history)
  and the unlicensed-eval-tier gap (refuted by `pedagogy-benchmark`).
- `p492` reported the permissive platform numerator as `3 → 4` as though it were ecosystem
  movement, computed over a shelf missing eight promoted rows.

🔵 **Two rules, both cheap, both would have caught all three:**

1. **Before declaring a gap, `grep -ri` the subject across this repository.** A gap asserted over
   held evidence is worse than silence — it instructs the next pass not to look.
2. **A full-file rewrite must diff its promoted-row names against the version it replaces, and
   either carry each row forward or say why it was dropped.** The `archive/` copies make this a
   one-command check. 🔴 Without it, every rewrite is a silent data-loss event, and the shelf keeps
   reporting a census of this KB rather than of the sector.

## 🆕 `p494` — `2026-10-28` — a new trend, and two trends that need qualifying

Full narrative and reads: [`../agents/trending.md`](../agents/trending.md) `p494`;
[`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).

### 🆕 `T15` — Agentic AI now has its own governance instrument, and it is voluntary by design

🟢 **The claim.** Governance of *agentic* systems has separated from governance of AI generally, and
the first instrument written specifically for it is **voluntary**. Singapore's IMDA launched the
**Model AI Governance Framework for Agentic AI** on **22 January 2026** at the World Economic Forum
— described across multiple independent firm notes as the world's first such framework — covering
**how much autonomy an agent is granted**, **how its actions are bounded and logged**, **how humans
stay meaningfully in the loop**, and **how accountability is assigned when several agents
interact**. **AI Verify** supplies the assurance side: process checks plus technical tests.

🔵 **Why this is a trend and not a single-country fact.** Every other regime this file tracks
governs AI by **what the system decides about a person** — EU Annex III by use case, Vietnam's
Decision 33 by sector, Korea's Basic Act by high-impact domain. `T15`'s instrument governs
**how much the system is allowed to do on its own**, which is an orthogonal axis. 🔴 **No
education-specific regime anywhere has an agent-autonomy provision**, so for a multi-agent education
product this is currently the **only** published rubric that addresses its actual architecture.

🟢 **Commercial reading — this is a sales asset, not a compliance burden.** `T4` holds that
regulation has split into incompatible regimes and that the differentiator is the human-oversight
gate. `T15` says that for the agentic layer, the gate is **voluntary and therefore demonstrable**:
a vendor can design to a published rubric and point at it, rather than argue an obligation down.
🔵 And per this KB's own (previously deleted) Singapore note, vendors selling into government and
banks **are expected to point to these frameworks** — so a voluntary instrument operates as a
**procurement gate**. Pricing consequence: an agentic-conformity workstream in Singapore is a
*demonstrable-conformance* deliverable, closer in shape to EMEA's provider-conformity sale than to
APAC's jurisdiction-routing sale.

🟡 **One claim deliberately not carried.** An academic commentary (`arXiv:2608.15417`) states the
framework *"requires each agent to carry a verifiable digital identity and an audit trail"* —
which conflicts with the voluntary standing every firm note describes. 🔴 **`arxiv.org` is
`connect_rejected` by this session's egress proxy**, so it cannot be checked here. Recorded as an
open conflict. **Do not tell a client the framework imposes an agent-identity requirement.**

🔴 **How `T15` came to be written is itself the evidence for `T14`.** This was not a discovery. The
Singapore posture was in this KB at `p315` and **`p315`'s own rewrite deleted it**; HEAD mentioned
Singapore exactly once, as a ban-support percentage. `T15` exists because this pass read the KB
against its own archive, not because a search surfaced something new.

### 🔴 `T4` needs qualifying: "build conformity once in EMEA shape" is only partly true

`T4` holds that regulation has split into four incompatible regimes and that this is a product
requirement — that stands and is strengthened. 🔴 **But the corollary this KB repeats — that an
EU-conformant assessment design transfers to the other high-risk jurisdiction with little rework —
is true for one of Vietnam's three education triggers and false for the other two.**

Vietnam's Decision `33/2026/QD-TTg` names **three** education system types. `p492` recorded one:

| trigger | transfers from an EU-conformant build? |
|---|---|
| automatic **assessment, grading or ranking** of students | 🟢 **yes** — same functional trigger as EU Annex III |
| self-learning content from **uncontrolled data sources** | 🔴 **no** — a **corpus-governance** obligation. An EU-conformant build has no corpus-provenance artefact to show, and the trigger fires on **retrieval design alone**, with no grading feature in the product |
| **biometric** monitoring of learner behaviour | 🔴 **no, and the regimes point in opposite directions** |

🔴 **The biometric divergence is the sharpest regulatory asymmetry in this file, and it belongs to
`T6` as much as to `T4`.** `T6` records that the EU **bans** emotion recognition in education
outright (live since 2 Feb 2025, narrow medical/safety exception). Vietnam **permits biometric
learner monitoring as a high-risk category** — i.e. allowed, subject to conformity duties. 🟢 **This
is not stricter-versus-looser along one axis; it is a feature that must be *absent* in one
jurisdiction and *documented and governed* in the other.** A single configuration cannot satisfy
both, and no amount of EMEA conformity work produces the Vietnamese artefact. **Treat biometric
learner monitoring as a build-time jurisdiction fork, never a runtime policy flag.**

### 🟢 `T14` gains a second mode: a later pass can blunt a sharper finding

`T14` holds that in this sector a KB's own bookkeeping is a material source of error. `p493`
established the first mode — **a full-file rewrite silently drops promoted rows**. This pass adds
two more, both observed:

1. 🔴 **Rewrites drop *prose*, and prose loss is undetectable.** A dropped row can be found by
   `grep`-ing a repo URL, which is how `p493` found eight. **A dropped paragraph has no key to grep
   for** — nobody knows to look for a fact the file no longer mentions. `market.md`, `trends.md` and
   `patterns.md` are mostly prose and all have been rewritten in full.
2. 🔴 **A later pass can overwrite a precise finding with a blunter one and file the precise one as
   the defect.** `p492` resolved Vietnam's deadlines into a conditional table (the date depends on
   **when the system went live**, not what it does). `p493` re-read a secondary source that flattened
   that conditional into a single grace date, found the flat version disagreed with the KB, and
   flagged **the KB's correct entry** as unquotable, deferring it to this pass. This pass's
   independent read confirms `p492` term by term.

🔵 **Rule, as transferable as `p493`'s grep rule:** before filing a contradiction between a new read
and a KB entry, **read that entry's own pass note first.** And before a full-file rewrite, diff the
*prose* against the archive copy, not just the tables — 🔴 **this KB currently has no mechanism that
would catch a deleted paragraph, and that is the open gap this trend names.**


## 🆕 `p495` — `2026-10-28` — one new trend, and one existing trend gains its missing demand-side leg

### 🆕 `T15` — The agent surface on an incumbent system is where the security debt lands, and it lands fast

🟢 **Evidence, first-hand this pass.** [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) —
the only maintained agent surface on an incumbent LMS this KB has found, **309★**, MIT — published
**four security advisories on a single day (`2026-10-25`)**: two **High** (a sandbox escape at CVSS
**7.8** via `child_process` in `execute_typescript`; a prompt-injection path from course content to
**data disclosure and grade change**), one Moderate (**Canvas bearer token sent to a URL chosen by
the file-storage host**), one Low. 🟢 **All four patched at `v1.16.0`.**

🔵 **The trend is not "this repo is risky."** It is that **the integration layer inherits the
authority of the system it integrates with, and none of its defences.** Every advisory here is a
consequence of the agent holding a Canvas instructor token and reading attacker-reachable content:
course material a student can edit becomes an instruction channel, and a grade-write tool becomes
the payload. 🔴 **An LMS has decades of permission hardening; a six-month-old MCP server fronting it
has none of it, and the token does not care which side of the boundary it is on.**

🔴 **Three generalisations this KB will apply to every future integration row:**

1. 🔴 **A version string is not a patch.** `v1.16.0` closes the sandbox escape **only on
   Node.js ≥ 22.18**, because the fix is Node's permission model. **Right version on an old runtime
   = unpatched, reported as patched.** This is invisible to a lockfile audit.
2. 🔴 **The published fix may leave the worst path open, in writing.** The `1.16.0` advisory itself
   states that egress blocking is best-effort and **executed code can still reach the caller's
   token.** 🔵 So the mitigation that matters is **removing the capability** (disable
   `execute_typescript`) and **shrinking the credential** (scoped, short-lived token) — not upgrading.
3. 🔵 **Advisory counts must be re-read, not inherited.** `p492` recorded four IDs; `p494` flagged
   that an un-re-read count on a fast-moving repo is the one number not allowed to age; `p495`
   re-read it and the count **held at four** — but severities, CVSS and patched versions had **never**
   been read, and those are the fields that decide a deployment. **A stale count is a risk; an
   un-read severity is a bigger one.**

🔵 **Commercially this is a reason to be the integrator, not a reason to avoid the layer.** A client
cannot assess this on their own: it took a release-tag read, four advisory reads and a runtime
check to arrive at a deployable posture. 🟢 **That posture is now written down as
[`../compose/patterns.md`](../compose/patterns.md) `P495-1`** — which is a billable artefact, and is
the kind of thing an AI Studio sells that a tutor demo does not.

### 🟢 `T9` (offline-first is a regional differentiator) — the demand-side leg it was missing

`T9` and `P490-3` have been argued almost entirely from **regulation** — sovereignty rules,
data-residency, jurisdictional divergence. 🟢 **This pass's APAC return supplies a procurement
argument instead:** Forrester reads that **60% of firms and governments in major markets such as
India and China will integrate locally developed large language models**, with **education named as
a target sector**.

🔵 **Why this strengthens `T9` rather than merely repeating it.** A regulatory driver can be
repealed — `T12` already records South Korea **de-mandating** a national AI mandate, which is this
KB's own counter-example to regulation as a durable demand floor. 🟢 **A procurement *preference*
for locally developed models is not repealed; it is a buying habit.** So the architectural
requirement `T9` prescribes — **model-portability as a first-class design property**, not a
deployment detail — now has a reason to exist in jurisdictions **where no rule requires it**.
🔴 **Design consequence, unchanged but better supported: never bind a pattern to a single hosted
model.** Which is also the standing criticism of `naufaldi/teacher-exam` (MIT harness, hosted
proprietary generator) on this KB's own trending shelf.

### 🟡 `T10` (market sizing is not usable) — holds, fifth pass, with fresh contradictions

🔴 The mandated trends query returned, in one sweep: **$3.7B in 2026 → $14.1B by 2033** (Persistence),
**$10.6B in 2026 at 40.9% CAGR** (The Business Research Company), **$11.4B in 2026** (GII), and a
North America figure given once as **~$951M (2024) → ~$2.3B (2029)** and once as **"USD 26.32 MN"**.
🟢 **`T10` stands: these are marketing pages, they do not agree within a factor of three, and no
pass should quote a single figure to a client.** 🔵 Quote the **direction and the regional ordering**
instead — and in LATAM, quote the **adoption-versus-governance contrast** (`92%` student engagement
against `~30%` institutional policy coverage) which is measured, sourced and far more persuasive
than a sizing estimate.

### 🔴 Trend-adjacent method note: a trend this KB loses is a trend that never existed

🟢 `p494` proved a full-file rewrite drops prose; `p495` found a **second instance** — LATAM's
adoption instrumentation present in the KB's history and README but **absent from
`intel/market.md`**. 🔴 **This file is mostly prose and has been rewritten in full.** 🟢 **Four of its
load-bearing claims are therefore now registered in `make gate-prose-claims`** — including `T15`'s
Node floor and the EMEA adoption-rate gap — so a later rewrite that drops them **fails the build**
instead of looking like coverage.



## 🆕 `p496` — `2026-10-28` — a trend number used twice, and a new trend about the layer with the worst licence hygiene

### 🔴 Bookkeeping defect: **`T15` names two different trends**

🔴 **Found by counting headings, not by reading prose.** This file contains two sections both
numbered `T15`:

| heading | pass | subject |
|---|---|---|
| `### 🆕 T15 — Agentic AI now has its own governance instrument, and it is voluntary by design` | `p494` | a governance instrument |
| `### 🆕 T15 — The agent surface on an incumbent system is where the security debt lands, and it lands fast` | `p495` | security debt at the agent surface |

🔴 **Consequence, and it is live rather than theoretical: every cross-file reference to "`T15`" in
this KB is now ambiguous**, including the ones in `agents/top.md` and `compose/patterns.md`.
`T13` and `T14` were each introduced inside a pass section the same way, so the numbering has no
single registry to collide against — which is how `p495` reached `T15` without noticing `p494` had
taken it.

🟢 **Resolution, chosen to avoid breaking existing references.** Neither section is renumbered —
renaming them would silently invalidate every citation already written. Instead both are
**disambiguated by suffix** from here on:

- **`T15-GOV`** — the voluntary agentic-AI governance instrument (`p494`).
- **`T15-SEC`** — security debt at the agent surface of an incumbent system (`p495`).

🔵 **And the next free number is `T16`**, used below. 🔴 **Standing instruction: a pass introducing a
trend must `grep -n "^## T\|^### 🆕 \`\?T" intel/trends.md` first.** This is `T14` applying to
itself — the defect was in the registry, not in anyone's reading.

### 🆕 `T16` — The layer with the highest legal exposure in education has the **worst licence hygiene**, and the two facts are connected

🟢 **Measured this pass, from bytes.** Discovery produced **eight addresses absent from all 5,547
files** in this KB, all in special education and rubric grading. The grant split:

| grant at pinned SHA | count | addresses |
|---|---|---|
| 🟢 **MIT** | **3** | `jscott5811/IEP-and-Section-504-Plans-Skill` (1 068 B), `rtwergrfh-cmyk/iep` (1 080 B), `SahilC/AutomaticEssayGrading` (1 074 B) |
| 🔴 **no licence at six filenames** | **5** | `SudhanvaJ-bit/project-samarth`, `kennedyraju55/essay-grader`, `avivkatz1/easy-iep`, `victor-lubn/Special-Education-Planning`, `marckurniawan/essay-scoring-project` |

🔴 **Five of eight — 62.5% — carry no grant**, each confirmed with `README.md → 200` at the same SHA
so the tree was demonstrably reached. **Compare the general education-agent layer, where this KB's
permissive tier is concentrated but real** (`DeepTutor` 47.3k Apache-2.0 *(🟢 `p505`)*, `OpenMAIC` 41.7k MIT *(`p502`)*).
🔵 **The special-education layer inverts that: supply exists, grants do not.**

🟢 **The mechanism, and it is the part worth briefing.** These are the repositories of **practitioners
and parents**, not of labs or vendors — a special-education teacher, a district employee, a family
advocate, shipping 1 to 32 commits to solve their own problem. 🔴 **People in that position publish
to help, and a licence file is an artefact of intending redistribution.** So the layer governed by
the *strictest* statutes — **IDEA**, **Section 504**, **FERPA**, Illinois **SOPPA**, India's **RPwD
Act** — is also the layer where almost nothing can lawfully be reused.

🔴 **Why this is a commercial trend and not a curiosity.** The failure mode is specific: a search
returns a tool that does exactly what a district needs, it is public on GitHub, the engagement
assumes "open source", and **there is no grant** — so the build is unlicensed from day one, in the
one domain where a compliance review is certain to happen. 🔵 **`T3` ("open source" claims are
unreliable at the family level) said the *family* is often misstated. `T16` is sharper and worse:
here there is often no licence at all**, and this pass caught the search channel asserting
*"MIT-licensed"* for `kennedyraju55/essay-grader`, which has none.

🟢 **What to do with it on an engagement:** treat this layer as **read-only reference** by default.
The three MIT assets are knowledge packs and a deterministic renderer — they compose
([`P496-1`](../compose/patterns.md)) but they do not add up to a product. 🔴 **There is no
special-education platform, open or permissive, at all** (see
[`../verticals/solutions.md`](../verticals/solutions.md) `p496`), so the system of record stays the
district's and Globant builds beside it.

### 🟢 `T9` (offline-first is a regional differentiator) — its cleanest instance yet, and it is not regional

[`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) (MIT, 1 080 B, `sha1 fb30401f6782`)
runs **entirely in the browser with no server and no AI service** — rules-only IEP→plain-language
rendering. 🟢 **Offline by construction rather than by configuration**, which is the strongest form
of the `T9` argument this KB holds.

🔵 **And it extends `T9` past its regional framing.** This file has argued offline-first as a
*LATAM/APAC connectivity* differentiator. Here the driver is **data sensitivity in a high-income
market**: an IEP is among the most protected records a school holds, and a tool that never transmits
it answers the egress objection **architecturally instead of contractually**. 🟢 **So offline-first
is now two arguments — connectivity where bandwidth is the constraint, and non-egress where privacy
law is** — and the second one sells in North America and EMEA.

### 🟡 `T10` (market sizing is not usable) — holds, sixth pass, with the contradiction inside one query

🔴 A single mandated trends query returned **three figures for the same year**: **$3.7bn**,
**$10.6bn** and **$11.4bn** for 2026, with CAGRs from **15.9%** to **46.12%**, plus disagreement on
the leading segment (one source: higher education largest; another: K-12 at **45.62%**). 🟢 **`T10`
does not need restating so much as it needs the replacement**, which this pass has: the
**governance gap**, now measured independently in two regions — **26%** of LATAM institutions with a
formal AI strategy, **10%** of North American institutions with formal AI guidelines. 🔵 **Two
instruments, two sources, one conclusion**, and unlike the dollar figures it has been stable across
passes.

## 🆕 `p497` — `2026-10-28` — a new trend, `T16` qualified, and the registry grep from `p496` **fails on its own file**

### 🔴 The standing instruction's own grep misses a trend

`p496` left this file a standing instruction: *"a pass introducing a trend must
`grep -n "^## T\|^### 🆕 \`\?T" intel/trends.md` first."* 🟢 **Run, as instructed.** It returns
`T1`–`T12`, `T14`, `T15` (twice), `T16` — and **not `T13`**.

🔴 **`T13` exists.** It is at line 255, headed
`### 🟢 A new trend, \`T13\` — the education agent-skills tier is consolidating off hosted
infrastructure`. The pattern requires `🆕` immediately after `###`; `T13`'s heading uses `🟢` and
the words *"A new trend,"* before the number, so the registry check **cannot see it**.

🔴 **Consequence:** a pass obeying `p496`'s instruction exactly would read the highest number as
`T16` and could reasonably conclude `T13` was free — reintroducing the precise collision `p496`
spent a section resolving. 🟢 **Fix, and it replaces the old instruction:**

> `grep -no "T[0-9]\+" intel/trends.md | sort -u -t: -k2` — pattern-free, so heading decoration
> cannot defeat it.

🟢 **Run before being recommended** — because proposing an unverified checker is the defect this
section is about. Output:

```
T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T137 T148
```

🟢 **`T13` is visible (7 occurrences), the full `T1`–`T18` range resolves, and the `T1xx` series from
[`agents/trending.md`](../agents/trending.md) shows up too** — which is a bonus: the checker surfaces
the second registry's numbers, so a future collision between the two ranges would be visible at the
moment a trend is introduced.

🔵 **This is `T14` applying to itself for the second consecutive pass.** `p496` found the registry
defective and wrote a checker with the same class of defect: **a validator built from the convention
it is validating inherits the convention's blind spots.** The replacement greps for the *number*,
never the decoration. 🔵 **Note also that this KB runs two independent trend registries** — `T1`–`T17`
in this file, and a `T1xx` series in [`agents/trending.md`](../agents/trending.md) (`T137`, `T148`).
They do not collide today because the ranges are disjoint, but nothing enforces that.

### 🟡 `T16` needs qualifying after one pass

`T16` (`p496`) states that the layer with the highest legal exposure in education has the **worst
licence hygiene**, from a sample where **five of eight** new addresses carried no grant.

🔴 **This pass's sample points the other way.** Three new addresses in the same high-exposure
territory — the EU Annex III functions — split: **`ASUCICREPO/Admissions-AI-Agent` MIT**,
**`TaiRuiQu/oh-my-paper` MIT**, and the only unlicensed one a **2★ handwriting script** sitting
*below* the regulated layer rather than in it.

🟡 **`T16` is therefore downgraded from a sector characteristic to a sample observation.** Eleven
addresses across two passes support neither direction. 🟢 **What survives, and is worth carrying to a
client:** licence hygiene in this sector's long tail is **unpredictable per repository and
uncorrelated with how regulated the function is** — which is the operational reason every row in
this KB is read from bytes rather than from a badge, a listicle or an API field.

### 🆕 `T17` — This KB's enumeration of *ranked* education-AI supply is ~95% complete, so discovery spend should move to drift and function queries

🟢 **Measured, not asserted.** Five ranked discovery axes run through a star-ordered channel this KB
had declared unavailable: `topic:ai-tutor`, `topic:ai-education`, `topic:knowledge-tracing`,
`topic:student-information-system`, `topic:proctoring`+`topic:automated-grading`. **59 addresses
pulled, 56 already on these shelves — 94.9%.** Census:
[`saturation-census.2026-10-28-p497.tsv`](../evidence/saturation-census.2026-10-28-p497.tsv).

🔴 **The two axes that *are* this sector returned zero.** `topic:ai-tutor` and `topic:ai-education`,
at every star level down to 100★, produced **nothing** this KB does not hold; several hits appear in
**200+ files** here.

🟢 **All three new addresses came from the administrative layer** — proctoring, grading, admissions.
`p496` reached the same place from `IEP`/`accommodations`/`rubric`. **Two passes, independent query
sets, one answer.**

**Consequences, which are budget decisions:**

1. 🔴 **Ranking legs are spent.** The brief's keyword-and-star queries have returned nothing new for
   **six** consecutive passes, and this pass shows that is a property of the supply, not of the
   query — a *better* ranking channel found the same ceiling.
2. 🟢 **Function-shaped administrative queries are the only productive discovery channel.** Spend
   there: placement, scheduling, degree audit, credentialing, attendance, early-warning, accessibility.
3. 🟢 **Re-verification now outranks discovery.** With supply enumerated, the KB's value is in pins,
   licence bytes, security floors and drift — where `p495` (a security floor), `p496` (a reader
   defect) and this pass (`rosariosis`'s `mobile` default ref) each found something real.

🔵 **Scope limit, stated so this does not harden into dogma.** 94.9% is saturation **of the ranked,
starred, topic-tagged population**. It says nothing about repositories that are new, untagged,
unstarred or not in English — and `oh-my-paper`, found this pass at **1★** with a Chinese-language UI
on a `v2` default branch, is exactly the kind of address this measurement cannot see.

### 🆕 `T18` — The four functions regulators designate as high-risk are the four with the thinnest open-source supply

🟢 **The convergence is this pass's commercial finding.** Every regime examined names substantially
the same functions: the EU AI Act **Annex III point 3** (admissions, grading, placement, exam
proctoring); **Vietnam's Decision 33/2026/QD-TTg** (education among six high-risk sectors, naming
automated assessment); US states legislating district AI policy over the same decisions.

🔴 **Supply, measured against that list** ([`verticals/solutions.md`](../verticals/solutions.md)
`p497`):

| designated function | permissive open-source supply |
|---|---|
| Admissions | 🔴 **one** asset, **5★**, found `p497` (MIT, ASU) — and it is AWS-Bedrock-bound |
| Grading | 🟡 thin — `oh-my-paper` (MIT, 1★); `dolos` is MIT and maintained but detects plagiarism, not grades |
| Placement | 🔴 **nothing**, in any pass |
| Exam proctoring | 🔴 **nothing permissive** out of **145** repositories on `topic:proctoring` |

🟢 **Read together with `T5`** (the EU's 16-month slip to **2 December 2027**) **this is the sector's
clearest build signal**: a dated compliance runway on functions where there is almost nothing to
buy, fork, or compose. 🔴 **And the inverse warning:** a client who expects to *assemble* an
admissions or proctoring capability from open source will not find the parts. Price those as builds.
Recipe: [`compose/patterns.md`](../compose/patterns.md) `P497-1`.

---

## 🆕 `p498` — `2026-10-28` — a new trend about licence *text*, `T17` **refuted**, `T3` promoted from pattern to replicated property, and `T10` given its decisive measurement

### 🔴 `T17` — **refuted by this pass's own measurement**

🔵 `p497` published `T17`: *"this KB's enumeration of **ranked** education-AI supply is ~95%
complete, so discovery spend should move to drift and function queries."* It rested on 59 ranked
addresses across five topic axes, **56 already shelved**.

🔴 **One axis `p497` did not run — `topic:edtech` `stars:>400` — returns 13 ranked addresses of
which 9 are absent from every shelf: 69.2% novelty against `T17`'s 5.1%.** And the axis was not
unknown: **`p480` censused `topic:edtech` ≥50★ at 64 repositories, six passes earlier, and never
enumerated them.**

🔴 **`T17` is withdrawn as a trend.** It measured the five axes `p497` chose, not ranked supply.
🟢 **What survives is narrower and still useful:** the axes that name this sector directly
(`topic:ai-tutor`, `topic:ai-education`, `topic:knowledge-tracing`) *are* enumerated, and `p497`'s
finding that productive discovery now comes from **function-shaped** queries (proctoring, grading,
admissions, IEP) held again this pass — every new address came from a generic-platform axis or a
function axis, none from a sector-named one. 🔵 **The correct standing instruction is not "ranked
discovery is finished" but "ranked discovery on sector-named topics is finished; generic and
function axes are not, and at least 51 counted rows remain unread" (`Gap 498-A`).**

### 🔴 `T19` — Education-AI licence **text** is edited in the field, and the edits are inside the operative body

🔵 `T3` says *"open source" claims in this market are unreliable at the family level* — a repo
calling itself Apache may be AGPL, a repo calling itself open source may carry a bespoke licence.
🔴 **`T19` is a layer beneath that: the family is right and the text has been changed.**

🟢 **The instance, this pass:** [`beltromatti/get-it`](https://github.com/beltromatti/get-it)
(1 138★, live) ships an Apache-2.0 payload with **five words deleted from §6 *Trademarks***. The
canonical safe harbour *"reasonable and customary use in describing the origin of the Work"* becomes
*"describing the origin of the Work"*. Graded against two independent canonical payloads
(`menthorlabs/menthor` 11 337 B; `huggingface/smolagents` 11 357 B).

🟢 **It is not the first.** `p488` found [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
carrying **three one-word insertions inside Apache's `TERMS AND CONDITIONS`** plus an overwritten
appendix, and `freelingo` carrying a genuinely altered GNU payload. 🔴 **Three instances across
three unrelated repositories is a pattern, not a trio of accidents.**

🔴 **Why it is invisible.** `get-it`'s payload is **22 bytes longer** than the canonical one it
deviates from — its appendix copyright line adds ~54 B while the deletion removes ~28 B. **A
size check clears it. A badge clears it. A search-API `license` field clears it.** Only a
normalised comparison of the operative span against a known-good payload catches it, and this base
has no retained canonical set (`Gap 498-B`).

🟢 **The product consequence for a studio:** licence review on an education-AI dependency cannot be
*"what licence is it"*. It has to be *"is this licence's operative text the text we think it is"*.
That is one `git cat-file` and one diff per dependency, and it is cheap enough to put in CI. 🔴 What
is not cheap is discovering at contract stage that a trademark carve-out your client-facing
materials rely on was edited out by an upstream author who almost certainly did not mean anything
by it.

### 🟢 `T3` is promoted: the permissive/non-commercial split is a **replicated** property, not a pattern

🔵 `p479` measured a **complete** population — all 22 repositories in a 30-day ≥30★ `topic:education`
census — and found the **two** non-commercial rows were **exactly the two curriculum-and-content
repositories**.

🟢 **`p498` reproduces it on a disjoint population.** Of eight addresses graded from
`topic:edtech` `stars:>400`:

| class | rows | grants |
|---|---|---|
| 🟢 code / tooling | `book-to-skill`, `Papermorph`, `claudemy`, `get-it`, `menthor`, `frametell` | **MIT ×3, Apache-2.0 ×2, AGPL-3.0 ×1 — every one an OSI licence** |
| 🔴 **content / curriculum** | `cn-math-taxonomy`, `PageLM` | 🔴 **CC BY-NC 4.0** and a bespoke **"PageLM Community License"** — **both non-commercial** |

🔴 **Two independent populations, same boundary, no exceptions in either.** 🔵 **The planning
consequence is firm enough to put in a proposal: budget to *build* the curriculum model and the
item bank; expect to *acquire* the tooling.** The reverse assumption — that content is the
commodity and tooling the hard part — is how an education engagement discovers in month three that
its knowledge graph cannot ship.

### 🔴 `T10` gets its decisive measurement — and it is internal to one publisher

🔵 `T10` says market sizing in this sector is not currently usable, resting on cross-publisher
disagreement. 🔴 **The stronger argument needs no second publisher.** MarketsandMarkets puts **North
America at $951 M in 2024**; North America is widely put at **36–42 %** of this market; that implies
a **global $2.3–2.6 B in 2024** — an order of magnitude below the **$9.58 B** figure this KB carried
for 2026, and ~**100×** above its own "Rest of Latin America" series when set against this base's
carried LATAM figure.

🟢 **`T10` therefore hardens from "the publishers disagree" to "the figures are not arithmetically
compatible with their own regional components".** 🟢 Both carried figures are withdrawn as data on
[`intel/market.md`](market.md) this pass. Quote a range with a publisher, or quote a demand signal.

### 🟡 `T2` qualified — the copyleft platform layer has **two non-interoperable families**, not one

🔵 `T2` calls the copyleft platform layer *the binding constraint*. 🟢 `p498` measures a constraint
**inside** it: [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🇧🇷 municipal SIS,
live at 2026-10-22) and [`formalms/formalms`](https://github.com/formalms/formalms) are both
**GPL-2.0 with no *or-later* election in their source notices — GPL-2.0-only**.

🔴 **GPL-2.0-only and GPL-3.0 do not combine.** So the copyleft column on
[`verticals/solutions.md`](../verticals/solutions.md) is not one pool of mutually-compatible
platforms: `moodle` / `chamilo` / `ILIAS` (GPL-3.0) sit on one side and `i-educar` / `formalms`
(GPL-2.0-only) on the other, and code cannot move between them. 🔵 **For a Brazilian municipal SIS
engagement this is week-one information**, and no previous pass stated it.

### 🟢 `T7` gains its strongest instance — and the agent surface is a **kill switch**, not just a hook

🔵 `T7` says agent tool surfaces are arriving at the LMS boundary, unevenly. 🟢 `p498`'s code read of
[`learningequality/kolibri`](https://github.com/learningequality/kolibri) (HEAD `08e3ecace444`,
2026-10-27) finds the most deployable instance yet: **21 in-tree plugins**, a plugin that mounts its
own URLs and its own DRF API via `KolibriPluginBase.url_module` / `api_url_module`, **21
`api_urls.py`** surfaces, four out-of-tree plugins shipped as precedent (including an **OIDC
provider**), and 🔴 **zero native LLM integration** to displace.

🟢 **The part that matters for procurement:** plugins are enabled and disabled **from the CLI or a
UI** and through `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`.
🔵 **An AI surface the deploying institution can switch off with one environment variable and no
rebuild is a different regulatory object from one compiled into the platform** — it is an
AI-Act-friendly posture that falls out of the architecture rather than being engineered onto it.
🔴 The constraint to design around: hooks are singletons (`KolibriHookMeta(SingletonMeta)`,
`HookSingleInstanceError`) — **one registration per hook**, so two vendors shipping into one
deployment will collide.

### 🔴 Declared gaps on this file

- 🔴 **`T19` rests on three instances across three repositories, all found incidentally.** Nobody has
  measured the **rate** of operative-body edits across an education corpus. `Gap 488-T` asked for
  exactly this and it is still unmeasured — this pass added a third instance instead of a rate.
- 🔴 **`Gap 488-Q` failed a second time.** No 2026 APAC teacher-adoption figure. The ANZ-vs-Asia
  split remains measured on ban-support sentiment.
- 🔴 **`Gap 484-J` not narrowed.** The EMEA leg named Africa and the Middle East in the query and
  returned no instrument, figure or player for either. **"EMEA" on these shelves means Europe.**
- 🟡 **`T11`, `T12`, `T16` were not re-tested this pass.** Carried unchanged.

---

## 🆕 `p499` — `2026-10-28` — **🔴 `T19` IS NARROWED HARD BY THE MEASUREMENT IT ASKED FOR: licence text is NOT "edited in the field" at any measurable rate — 0 of 64 grants on these shelves are materially altered, and two of `p498`'s three claimed instances were a circulating template variant, not edits. 🟢 `T2`'s binding constraint is RE-SCOPED: the copyleft problem is real at the platform layer and FALSE at the integration layer above it. 🆕 `T20` and `T21`.**

### 🔴 `T19` — narrowed from a field practice to a single confirmed instance

`T19` (`p498`) reads: *"Education-AI licence **text** is edited in the field, and the edits are
inside the operative body."* It rested on three instances — `DeepTutor`, `freelingo`, `get-it` —
and `Gap 488-T` conceded the **rate was never measured**.

🟢 **The rate is now measured.** 76 census rows re-fetched at pinned SHAs, 64 gradeable against a
retained canonical set, operative span graded word-by-word
([`repos/trending.md`](../repos/trending.md) `p499`):

| | n | share |
|---|---|---|
| operative body **IDENTICAL** to canonical | 46 | 71.9% |
| deviant **but** the payload is a *different licence* (nearest-neighbour mislabel) | 8 | 12.5% |
| deviant **but** only appended provenance prose, no terms added | 2 | 3.1% |
| deviant **but** a benign vintage / URL / heading variant | 5 | 7.8% |
| deviant **but** a third-party **template** variant shared across unrelated repos | 3 | 4.7% |
| 🔴 **materially altered grant** | **0** | **0.0%** |

🔴 **And `p498`'s instance count is over by one.** `DeepTutor`'s Apache deviation — "submitted to
**the** Licensor", "received by **the** Licensor", §4(d) "excluding **any** notices" — appears
**identically on three repositories, two of them unrelated** (🇭🇰 `HKUDS/DeepTutor`, its derivative
`3yangyang9/DeepTutor-AILearning`, and 🇵🇰 `Orenda-Project/rumi-platform`). 🔵 **An author's edit does
not replicate across unrelated repositories; a template generator's output does.**

🟢 **`T19` restated as the evidence supports it:** *education-AI licence payloads deviate from
canonical often (28.1%) and almost always harmlessly — fill-ins, vintages, appended attribution,
circulating templates. **One** material alteration is confirmed base-wide (`beltromatti/get-it`'s
five-word §6 deletion). The commercial risk is **not** that grants are routinely edited; it is that
a single edited grant is **undetectable without a canonical set**, and one existed.*

🔵 **The method rule that falls out, and it is reusable:** a deviation found on **≥2 unrelated**
repositories is evidence of a shared upstream text. Only a deviation **unique to one project** is a
candidate alteration. `get-it` passes that test; `DeepTutor` does not.

### 🟢 `T2` re-scoped — the copyleft constraint is layer-specific, and the layer that matters is permissive

`T2` reads: *"The education platform layer is copyleft, and this is now the binding constraint."*
🟢 **True of the platform layer and false one layer up**, which changes what it implies.

| layer | licence picture | can a closed derivative ship? |
|---|---|---|
| **Incumbent LMS** (Moodle, Open edX, Canvas) | 🔴 GPL-3.0 / AGPL-3.0 / AGPL-3.0 | 🔴 no |
| 🟢 **Interoperability standards** (`tsugi` Apache-2.0 377★, `scorm-again` MIT 360★) | 🟢 **permissive** | 🟢 **yes** |
| 🟢 **Credentials / competency** (`iblai/lms` MIT) | 🟢 permissive | 🟢 yes |
| 🟢 **Authoring / client** (`haxcms-php` Apache-2.0, `tutors` MIT, `pytogether` MIT) | 🟢 permissive | 🟢 yes |
| 🟢 **Spaced repetition** (`mnemo` Apache-2.0, FSRS flashcards MIT) | 🟢 permissive | 🟢 yes |

🟢 **The correct strategic sentence is: you cannot close the LMS, but you can close everything you
build against it** — because **LTI is a network protocol, not linking**, so a tool speaking LTI to
an AGPL host is a separate work. 🔵 `T2`'s pessimism cost this KB real ground: it pushed engagements
toward `OpenOlat` (448★) and away from the installed base, when the installed base was always
reachable over a permissive integration layer. 🟢 Operationalised as `P499-1`.

🔴 **What `T2` keeps:** fork a Moodle plugin or an Open edX XBlock and the copyleft reaches you.
The constraint is real; it is just **narrower than this file has been stating.**

### 🆕 `T20` — In education, permissiveness tracks *position in the stack*, not project age or size

Across 29 foundational platforms now read from bytes, licence choice is **predicted by layer**:
systems of record are copyleft; the protocol, credential, authoring and client layers are
permissive. 🟢 This is not a size or recency effect — `tsugi` (377★) and `scorm-again` (360★) are
permissive and mature, while `Materia` (52★, 2013) is AGPL-3.0.

**Why it holds:** copyleft was chosen by the 2000s-era institutional platforms to keep public-sector
forks public. The layers built *since* exist to be embedded in someone else's product, and
embedding is what copyleft prevents. 🔵 **Consequence:** when scoping, ask *which layer* before
asking which project. The licence is mostly determined once the layer is fixed, which makes
licensing a **design decision taken early**, not a procurement surprise found late.

🔴 **Caveat, recorded:** the 15.8% → 37.9% permissive share this pass reports moved because `p499`
chose to look at layers nobody here had sampled. **That is a selection effect** (`Gap 499-I`); the
*direction* is evidence, the *magnitude* is not.

### 🆕 `T21` — "Grant by reference" is spreading, and it breaks every licence instrument including this base's

Three rows now ship a `LICENSE` file that **contains no grant** — only a pointer:

| repo | file | bytes | content |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | `license.txt` | **19** | `License: GNU GPL V3` |
| [`codeforlife-education/rapid-router`](https://github.com/codeforlife-education/rapid-router) | `LICENSE.md` | **121** | *"Find our license here"* + link |
| [`codeforlife-education/codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal) | `LICENSE.md` | **121** | same file |

🔴 **Three failures at once.** (1) GitHub's licence API reports a **declared** SPDX id with no text
behind it. (2) A byte-reading instrument — including this base's — finds a payload, grades it
against canonical, and produces a nonsense verdict (`frappe/education`: "−164 words"). (3) For
**GPL specifically**, conveying the work without a copy of the License is a problem under the
licence's own terms.

🟢 **Instrument requirement:** a grant payload must be classified **pointer / partial / full**
*before* it is graded, and a pointer must return "unresolved", not a diff. 🔵 This is adjacent to
`Gap 499-B` (no "unknown licence" verdict) and both come from the same omission: **the instrument
has no way to decline.**

🔵 **Commercially:** a pointer grant is not a blocker, it is a **diligence item** — the real licence
usually exists in a sibling repository or a `COPYRIGHT` file, as `openeducat_erp` does. **Resolve
it before an engagement; do not refuse the row and do not trust the API badge.**

### 🔵 A method finding about this base's own instruments, recorded as a trend because it will recur

🔴 **Two successive forms of `p499`'s own licence instrument deleted operative text**, and neither
was detectable from its own output:

| form | what it silently deleted | what exposed it |
|---|---|---|
| strip any line beginning `copyright` | GPL-3.0 §2's *"…for the term of copyright on the Program, and are irrevocable…"* | a **uniform −22-word "deletion" across 14 independent GPL/AGPL projects** |
| also accept a bare word after `copyright` (to catch `Copyright (c) Microsoft Corporation.`) | GPL-2.0 §1's wrapped *"copyright notice and disclaimer of warranty; keep intact all the"* | `formalms` §1 read **word-for-word canonical** by hand |

🟢 **Both were caught only by a control whose answer was already known** — which is precisely what
`Gap 498-M` says has never been done to a gate on this base. 🔵 **The generalisation: an instrument's
own output cannot validate it.** A plausible number is the expected output of a broken instrument.
Every gate needs a known-good **and** a known-bad input before its results are believed.

### 🆕 Declared gaps — `p499` (trends)

| gap | statement | cost to close |
|---|---|---|
| 🟡 **`Gap 499-J`** | `T20` is asserted on **29 rows of this shelf**, not a sample of the sector. Layer assignment was also done by hand, by me, and layers are not a defined taxonomy anywhere in this repo. | one pass, define the layers |
| 🟡 **`Gap 499-K`** | `T21` rests on **three instances**, two of which are the same organisation (`codeforlife-education`). That is really **two independent instances**. "Spreading" is not yet supported. | one pass, sweep for small grant payloads |
| 🔴 **`Gap 499-L`** | `T19`'s narrowing depends on my **hand classification of 18 diffs** (`Gap 499-F`). The headline *"0 of 64 materially altered"* is not reproducible by code in this repo, so a later pass cannot re-derive it without repeating my judgement. | one pass, encode the four classes |
| 🟡 **`Gap 499-M`** | `T2`'s re-scoping claims **LTI is arm's-length, not linking**, and therefore that AGPL does not reach an LTI tool. 🔴 **That is my reading of the licence and the standard, not legal advice and not a cited authority.** It is load-bearing for `P499-1`'s whole premise. | needs counsel, not a pass |

---

## 🆕 `p500` — `2026-10-28` — two new trends, and one of this file's own claims re-grounded

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten.

## T13 — The licence question has moved from the code to the data

**This is the new one, and it changes how to vet an education-AI component.** Two rows resolved
this pass carry **permissive code and restricted data**:

| Repo | Code | Data |
|---|---|---|
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 **MIT** | 🔴 prompts **CC BY 4.0**; annotated **CLEAR** and **PERSUADE 2.0** corpora **CC BY-NC-SA 4.0 — non-commercial** |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🟢 **MIT** | 🔴 licensed **per dataset**, per download — not uniform |

For an **evaluation** instrument the corpus *is* the product: an MIT rubric evaluator with
non-commercial reference corpora cannot be shipped in a paid engagement on the strength of its code
licence. The same split is what makes `knowledge-graph` unshelvable as data while shelvable as code.

**Consequence:** a two-column licence check — code **and** data — on every education-AI component.
A single SPDX field, which is what GitHub shows and what most curation reads, cannot express this
and will read as green. `Gap 500-E` carries the open commercial question.

## T14 — Mandate and prohibition arrive together, and the gap between them is the work

The 2026 pattern across regions is not adoption versus resistance. It is **the same authority doing
both at once**:

- 🇦🇪 **UAE** mandates AI teaching **KG → Grade 12** across all government schools *and* publishes
  **25 classroom prohibitions** including a **ban for students under 13**; reported teacher uptake
  is **48%**.
- 🇺🇸 **Oklahoma SB 1734** would require every district to adopt a written AI policy *and* bar AI as
  the **primary basis for grading or discipline**. **NYC** runs a moratorium on student-facing AI
  through grade 8 while US teacher use sits near **60%**.
- 🇪🇺 The **EU** treats education **access and assessment** as **Annex III high-risk** — permitted,
  conditioned, and dated (**2 December 2027**).

**Consequence for an engagement:** the deliverable is not a tutor. It is the **enforcement surface**
— age gating, per-district prohibition configuration, human-in-the-loop on grading and discipline,
and an audit trail of which model touched which student artefact — plus the teacher training that
closes a 48%-uptake gap under a full mandate. Capability is assumed; **governed delivery is bought.**

## T15 — Africa's constraint is language, not policy

First pass with named African instruments on these shelves. Ethiopia's Ministry of Education is
building a cross-level framework with **UNESCO** (begun May 2026) and testing teacher
lesson-planning AI; South Africa's **draft** National AI Policy 2026 names STEAM curricula and
community AI centres. 🔴 **The reported practical obstacle in Ethiopia is that models handle
Amharic and Afaan Oromo far less reliably than English.**

**Consequence:** on an African education engagement, scope **model and corpus capability in the
language of instruction before anything else**, and assume offline-capable delivery
([`Wakoma/Lokal`](https://github.com/Wakoma/Lokal), Kolibri). A curriculum-policy framing will
produce a product that does not work in the classroom it was bought for. 🔵 Kenya and Nigeria
remain **unmeasured** here despite an explicit by-country query.

## 🟢 `T2` re-grounded — the copyleft constraint now has a measured denominator

`T2` has said since `p491` that the education platform layer is copyleft and that this is the
binding constraint. It now has a rate rather than an impression. Of the **31** rows in the
`topic:edtech` 50–400★ band still absent from every curated shelf:

| | n |
|---|---|
| 🔴 copyleft (AGPL-3.0, GPL-3.0/2.0, LGPL-2.1, MPL-2.0, CERN-OHL-S-2.0) | 11 |
| 🔴 no resolvable grant at any root path | 6 |
| 🔴 dormant (no push since 2024 or earlier) | 9 |
| 🟢 permissive **and** live | **4** |

**25 of 31 are unusable for reasons that no amount of curation changes.** `T2` is correct and the
constraint is tighter than "mostly copyleft" suggested: on this axis the permissive-and-live yield
is **7.7%**.

## 🔴 `T11` — the claim about unlicensed evaluation instruments needs its third correction

`T11` originally held that **no** education-AI evaluation instrument is licensed. `p493` falsified
it once ([`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark),
MIT). `p500` falsifies the weaker successor claim too: `learning-commons-org/evaluators` is **MIT**
code. 🔴 **But the honest statement is narrower than "licensed instruments exist":** the licensed
ones are licensed **in their code and restricted in their corpora** (see `T13`). The tier has
permissive *software* and non-commercial *reference data*.


## 🆕 `p502` — `2026-10-28` — **🆕 `T24` and `T25`; 🔴 `T22` is re-scoped from a sector claim to an axis artefact; 🟢 `T11`'s evaluation tier gains the acceptance instrument it was missing**

Reads: [`channel-crosscheck.2026-10-28-p502.tsv`](../evidence/channel-crosscheck.2026-10-28-p502.tsv),
[`axis-saturation.2026-10-28-p502.tsv`](../evidence/axis-saturation.2026-10-28-p502.tsv).

## T24 — The compliance artefact every regime demands is the record layer, and its open-source supply is one region deep

Four regulatory regimes, four different statutes, **one shared deliverable**: a durable record of
what the system did and that a human reviewed it. EU AI Act Art. 26 deployer logging; Oklahoma's bar
on AI as the primary basis for grading or discipline; Vietnam's high-risk listing of automated
assessment; UNESCO IESALC's finding that **87%** of LATAM institutions use AI and **26%** have a
strategy. 🔵 **None of these is answered by a better tutor. All of them are answered by xAPI / cmi5 /
Caliper plumbing.**

🔴 **Measured supply, first-hand this pass:** of 31 record-layer addresses read, the permissive ones
are **5 North America, 1 EMEA (708 days stale), 0 APAC, 0 LATAM**.

| | permissive supply | live mainline |
|---|---|---|
| North America | 5 (`ADL_LRS` 334★, `lrsql` 144★, `lrs-conformance-test-suite` 78★, `CATAPULT` 59★, `project-persephone` 8★) | 🟢 1 (`lrsql`, 2 d) |
| EMEA | 2 (`ralph` 51★, `warren` 17★) | 🟡 1 (`ralph`, 16 d); `warren` 🔴 708 d |
| APAC | 🔴 **0** | — |
| LATAM | 🔴 **0** | — |

🔵 **And the asymmetry runs the other way at the agent tier**: APAC supplies the two largest
permissive education-AI repositories in existence (`DeepTutor` **47,338★** *(🟢 `p505`)*, `OpenMAIC` 41,690★ *(`p502`)*) and
nothing at the record tier. **Agents are abundant and global; the thing regulators actually ask for
is scarce and American.** 🟢 That is the clearest build-and-own opportunity on these shelves, and it
is strongest in LATAM, where the governance deficit is best evidenced (`intel/market.md` `p502`).

## T25 — A repository's "last activity" is reported by three channels and all three can be wrong

🔴 **`Gap 396-G` has now been confirmed against a third independent channel**, and the newest one is
the worst offender. Fixture: [`openfun/warren`](https://github.com/openfun/warren).

| channel | field | reports | error |
|---|---|---|---|
| `github.com/search` HTML | *Updated* | *"3 days ago"* | 🔴 702 d |
| REST API | `updated_at` | `2026-10-21` | 🔴 ~706 d |
| REST API | `pushed_at` | **`2026-10-28` — today** | 🔴 **708 d** |
| `git clone --depth 1` | committer date of `main` | **`2024-11-19`** | 🟢 correct |

🔵 **`pushed_at` is not lying — it is answering a different question.** It counts a push to *any*
ref, so a repository with an untouched `main` and an active side branch reads as pushed today. The
field is truthful about the repository and misleading about the mainline, and **the mainline is what
a shelf decision depends on.** 🔴 Reproduced at a second magnitude on
[`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS): `pushed_at` `2025-11-14` against a last
`master` commit of `2025-06-13` — **154 days apart**.

🟢 **Consequence for anyone reading these shelves:** a 334★ Apache-2.0 LRS that looks maintained is
**502 days dead**, and a 144★ one that looks smaller shipped two days ago. The star ranking and the
maintenance ranking in that tier are **inverted**, and the convenient date field conceals it.

🟢 **Standing rule, extended from `396-G`:** *enumerate, star, licence-family and topic with the
**API**; date with **git**; grant-bytes with **`raw`** at a pinned SHA.* Never let one channel do
another's job — and treat `pushed_at` as evidence about a repository, never about its mainline.

## 🔴 T22 — re-scoped, and the correction matters more than the trend

`T22` was recorded by `p501` as a sector finding: discovery here had been *axis-bound*, with
`topic:ai-in-education` yielding **65%** novelty against `topic:edtech`'s 19.2%.

🔴 **Re-measured with a star floor, the effect disappears.**

| axis | floor | `total_count` | 🟢 new to this base | novelty |
|---|---|---|---|---|
| `topic:ai-in-education` | `>50★` | **3** | **0** | **0.0%** |
| `topic:edtech` | `>150★` | 28 | **0** | **0.0%** |
| `topic:edtech license:apache-2.0` | `>20★` | 11 | **0** | **0.0%** |
| `topic:learning-analytics` | `>20★` | 9 | 1 | 11.1% |

🔵 **`p501`'s novel rows were overwhelmingly sub-50★.** The axis effect was real and the sector
conclusion drawn from it was not: above 50★ **every axis this base has swept is saturated**, and the
one new row — [`AkihikoWatanabe/paper_notes`](https://github.com/AkihikoWatanabe/paper_notes) — is a
research-notes list using **6,846 open issues as note storage**, not a deployable asset.

🟢 **`T22` is therefore narrowed to what it can carry:** *a topic-axis sweep measures its axis, and
novelty figures are not comparable across axes unless the same star floor is applied to both.*
`Gap 498-A`'s original *"the supply is largely read"* is **restored as the correct reading**, and
`p501`'s refutation of it is withdrawn. 🔵 The sub-50★ band is still genuinely unread — but that band
is `Gap 499-H`'s watch-row shape (no release, no tag), not shelf supply.

## 🟢 T11 — the evaluation tier gains its acceptance instrument

`T11` records that education-AI evaluation instruments exist and that `p493` corrected *"none of them
is licensed"*. 🟢 **The tier now has a conformance instrument as well as rubrics**:
[`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) — **MIT**,
1,045 B `f1083e4aa47d`, 78★, the official suite behind `lrstest.adlnet.gov`.

🔵 **The distinction is worth keeping sharp.** The rubric instruments (`pedagogy-benchmark`,
Learning Commons `evaluators`) grade whether output is *good teaching*. This one proves a system is
*standards-conformant*. 🟢 A regulator or a procurement office asks the second question, and until
this pass these shelves could only answer the first. 🔴 Its mainline is **419 days** stale — but a
conformance suite tracks a frozen specification, so staleness here is far weaker evidence of
abandonment than it would be for a product.

## Declared gaps — `p502`

| id | statement |
|---|---|
| 🆕 **`Gap 502-B`** | **No gate here knows that `pushed_at` is branch-agnostic.** Two fixtures, 708 d and 154 d of overstatement. A successor reaching for the API's convenient date field will publish dead repositories as live |
| 🆕 **`Gap 502-E`** | 🔴 **`T24`'s two absences were measured on one channel.** "No APAC or LATAM LRS" means *the xAPI/LRS/cmi5/Caliper vocabulary over the GitHub REST API returned none* — it is not a claim about the world. 🔵 The likeliest blind spot is **non-English naming and non-GitHub hosting** (GitLab, institutional forges), neither of which this channel reaches. Until that is probed, publish the absence **with its channel named** |
