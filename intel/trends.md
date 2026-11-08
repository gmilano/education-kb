---
industry: education
region: Global
updated: 2026-11-08
---

# 📡 Trends — Education

> What is actually changing in AI + education as of November 2026. Each trend names its evidence and its confidence.

🔴 **Read this before citing any `T` number: four identifiers on this page resolve to two different trends each, and `156` references across the shelves point at them.** Re-measured at p685 by counting headings rather than trusting the last figure: **`87` `## T` headings, `83` distinct numbers, `0` gaps** — 🔄 **re-derived at p687: `93` headings, `89` distinct numbers, `max = T93`, and now `4` gaps at `T84`–`T87`.** 🟢 **Those four gaps are the reservation this banner's own repair plan created, not a defect — do NOT close them.** p685 set aside `T84`–`T87` to receive the renumbered second occurrences of `T31`/`T32`/`T39`/`T40`; p686 then filed `T88`–`T90` and p687 `T91`–`T93`, both correctly numbering from `max(## T)` and stepping over the reserved block. 🔴 **A future pass that re-derives this census will see `4` gaps and may read them as a numbering error. Reusing `T84`–`T87` for new trends would consume the only free identifiers the collision repair can land in, and the repair would then have nowhere to go.** The reserved block is load-bearing; the next `T` number is `T125` — so the heading count is *not* the trend count (the `distinct` vs `total` distinction this page records as **T62**). The collisions are **`T31`, `T32`, `T39` and `T40`**, each used once by `p657`/`p658` and again by `p661`/`p664`:

| id | first use | second use | shelf references |
|---|---|---|--:|
| `T31` | psychometric measurement layer (`p657`) | regional "zero" as a query artefact (`p664`) | `43` |
| `T32` | spoken assessment (`p657`) | LATAM adoption vs licensability (`p664`) | `36` |
| `T39` | permissive code around unlicensed courseware (`p658`) | absence claims refuted in logs (`p661`) | `47` |
| `T40` | Scratch's two licences (`p658`) | "no permissive supply" claims as adoption gaps (`p661`) | `30` |

🔧 **`p671` annotated the four *headings* and stopped there, which fixed the symptom a reader sees on this page and left the one they cannot see.** A reader arriving from `**T39**` on `repos/foundations.md` still has no way to know which of two unrelated trends was meant.

🔴 **p685 deliberately did not repair it, and the reason is a data-integrity one rather than a scheduling one.** Renumbering the second of each pair to free identifiers (`T84`–`T87`) is mechanical, but **rewriting the `156` citations is not**: each site meant one specific trend, that intent is not recoverable from the token `T39`, and a bulk reassignment would silently point a documented claim at the wrong evidence. **A wrong citation is worse than an ambiguous one, because it reads as resolved.** The repair is therefore: renumber the four second-occurrence headings, then disambiguate references **one at a time, by reading each site**, and leave `T31`/`T32`/`T39`/`T40` permanently retired rather than reused. 🔵 **Until that is done, every `T31`/`T32`/`T39`/`T40` citation on these shelves should be read as naming a *pair*, not a trend.** New trends are numbered from `max(## T)`, never from the last heading in file order — `p685` filed **T82** and **T83** that way and both are unique.

## 🆕 T168–T169 — added at p708 (2026-11-08)

🔴 **Numbering hazard hit and recorded, because p708 nearly committed the defect this page's own banner warns about.** Deriving the next free identifier from `max(## T ...)` returns **`155`** — and `T154`/`T155` **already exist**, filed at `p704`. 🟢 **The reason is a heading-STYLE change, not a counting error:** from `p704` onward trends are filed as `## 🆕 T{a}–T{b} — added at pNNN` with each trend at `### `T{n}``, so a scan for `^## T` sees nothing after `T155` and misses `T156`–`T167` entirely. 🔵 **The correct instrument is `max` over EVERY `T{n}` appearing in ANY heading of level 2–4, which returns `167`** — excluding `T273`, which is a cross-reference into the pre-reset base's namespace and not a trend on this page. 🟢 **Re-derived at p708 that way: `167` carried in, `T168`–`T169` filed, max `169`.** 🔴 **The `T84`–`T87` gap block remains RESERVED — do not close it** — and `T125` is skipped deliberately (recorded further down this page). The `T31`/`T32`/`T39`/`T40` collisions are unrepaired by design.

### `T168` — The institutional agent is a class, it has crossed four countries independently, and it is the only education-AI subject that places itself in a region without inference

**Signal.** p708 verified and filed **seven** subjects that share a shape no earlier trend on this page names: an **unofficial MCP server over one named university's own running systems**, published by a student or a lecturer at that university, authenticating as the user with the user's own credentials.

| subject | institution | country | reach beyond the LMS | grant, read from the bytes `2026-11-08` |
|---|---|---|---|---|
| [`jamestesting0/tum-mcp`](https://github.com/jamestesting0/tum-mcp) | Technische Universität München | 🇩🇪 Germany | **Artemis** (autograder), Zulip, **TUMonline** (campus management) | 🟢 MIT, `1,092 B`, `ce90dfa77bef` |
| [`kad-xyz/spbstu-mcp`](https://github.com/kad-xyz/spbstu-mcp) | Peter the Great St. Petersburg Polytechnic | 🇷🇺 Russia | mailbox, timetable, the **national** `openedu.ru` | 🟢 MIT, `1,064 B`, `0dc1ec808f28` |
| [`simonseifert/merlin-mcp`](https://github.com/simonseifert/merlin-mcp) | **SRCE** — national academic computing centre | 🇭🇷 Croatia | a **national Moodle tenancy** for Croatian universities | 🟢 MIT, `1,070 B`, `c458af6b099b` |
| [`changazo/udesa-mcp`](https://github.com/changazo/udesa-mcp) | Universidad de San Andrés | 🇦🇷 Argentina | role-aware write policy, private OAuth deployment | 🟢 **Apache-2.0**, `10,173 B`, `a6cba85bc92e` |
| [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) | Universidad Tecnológica Nacional | 🇦🇷 Argentina | forum posting and assignment submission on confirmation | 🔵 **ISC**, `748 B`, `2ad14eb14513` |
| [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) | Argentine universities, multi-tenant | 🇦🇷 Argentina | **SIU Guaraní** — a student-records system, not an LMS | 🟡 **MIT + ISC conjunctive**, `1,980 B`, `727b864af003` |
| [`EduardoKrausME/moodle-local_mcp`](https://github.com/EduardoKrausME/moodle-local_mcp) | any Moodle, **in-tree** | — | separate READ/WRITE registries, preview-and-approve | 🔴 **GPL-3.0**, `35,149 B`, `3972dc9744f6` |

🟢 **They were written independently — different authors, different languages, different stacks — and they converge on the same four controls:** server-side role-aware scope; a compulsory preview-and-approve step before any write; student **pseudonymisation** before anything reaches a model; and provenance, coverage and warnings on every result, with an error never returned as an empty result. 🟢 **Credentials never leave the user in any of them** — OS secure store, the institution's own session, or private single-account OAuth.

🔵 **Why it is a trend rather than a cohort.** This base has `192` agent rows and has struggled for eleven passes to place them: `Global` is the largest column at `83` precisely because a generic tutor repo names no country. 🟢 **An institutional agent is named after a university, so the region is a fact in the subject, not an inference from a README.** Filing these seven moved `EMEA 15 → 18` and `LATAM 16 → 19` — the two thinnest columns — in one pass, with **zero** region guesses. 🟡 `falkenslab/miyagi` is the control that proves the rule: Spanish-language Moodle tooling that names **no** institution and **no** country, so it is filed `Global` and stays there.

**Confidence.** 🟢 **High on the class and its properties** — all seven payloads were read first-hand from `raw.githubusercontent.com` at the live default ref, all seven proved alive by `git ls-remote --symref`, all seven have a commit inside the last `13` days. 🟡 **Low on the class's size**: seven is what one Spanish-language leg plus one upstream thread produced, not a census.

**Action.** 🔴 **The next sweep of this class should be run per country in the authors' own language, naming the institution** (`708-C`) — never as `AI education {region} 2026`, which returns UNESCO and ministries and has never once returned a repository. 🔴 **The APAC form has not been run at all**, so APAC's `0` institutional agents is an unswept channel, not an empty one. 🟢 **For an engagement: the authority layer above is the reusable asset, and three of its four controls are already MIT or Apache-2.0.** The fourth — write authority — has its best reference under GPL-3.0 **by construction** (it lives in Moodle's tree), so it must be re-implemented out-of-tree, not copied.

---

### `T169` — Licence-NAME gating fails on this class three distinct ways, and p708 hit all three in a single pass

**Signal.** Globant's own filter is *“MIT / Apache 2.0 / BSD”*. 🔴 **Applied as a string match — which is how a client's compliance gate is actually built — it produced a wrong answer on three of the nine subjects p708 read, in three different directions.**

| failure mode | subject | what a name-matcher answers | what the bytes say |
|---|---|---|---|
| **1. Permissive but not on the list** | [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) | 🔴 **refuse** — `ISC` matches neither `MIT`, `Apache-2.0` nor `BSD` | 🟢 **ISC is OSI-approved, BSD-family and permissive.** `748 B` — the smallest grant on this base. A correct gate accepts it |
| **2. On the list, but it is only HALF the grant** | [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) | 🔴 **accept as MIT and stop** — the file is titled `MIT License` | 🟡 **Two live grants in one file.** Below a separator sits a standalone **ISC** grant © *Joaquín Peñalva* for the portions derived from `utn-mcp`. A deployment takes **both**. `1,980 B`, `sha256₁₂ 727b864af003` — byte-identical to the record this base holds for it at `T427` in [`open-gaps.md`](open-gaps.md), so this is confirmed, not inferred |
| **3. On the list, and there is NO grant at all** | [`MoralesPascualJosue/Plataforma-educativa-MC-`](https://github.com/MoralesPascualJosue/Plataforma-educativa-MC-) | 🔴 **accept as MIT** — `composer.json` says `"license": "MIT"` | ⛔ **All rights reserved.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` and `license` each `404` at `master`. The manifest is the **unedited Laravel skeleton**: `name` = **`laravel/laravel`**, `description` = **`"The Laravel Framework."`**, `require.laravel/framework` = `^6.2`. The MIT is **Laravel's, declared by Laravel, about Laravel** |

🔵 **Mode 3 has a precedent on this base and this instance is strictly worse.** The `Gego-K12/gegok12` finding named the unedited-scaffold manifest — but that repository *also* had a real root `LICENSE`, so the scaffold field was redundant and harmless. 🔴 **Here the scaffold field stands alone: it is the only licence signal in the repository, and it is false.** Call it the **scaffold field standing alone**.

🟢 **A fourth direction was measured too, and it is the one that moves fastest:** `p707` found [`Kernel0x19/klyro`](https://github.com/Kernel0x19/klyro) had gone **MIT → AGPL-3.0** seven days after being filed. 🟢 **p708 bounded it** — the youngest `81` rows on this base re-read from the bytes, **`81 / 81` alive and `81 / 81` byte-identical**, so the measured reversal rate is **`1 / 81`** across six passes and `klyro` is a singleton, not a wave.

**Confidence.** 🟢 **High.** Every claim here is a payload read from `raw.githubusercontent.com` at a named default ref on `2026-11-08`, with the byte size and `sha256₁₂` published beside it; the three refusals name the probe that produced them.

**Action.** Three discriminators, each one line, in the order they must run:
1. 🔴 **Read `name` before `license` in any manifest.** If `name` is the framework's own (`laravel/laravel`, and the equivalent for `package.json`), the `license` field is scaffold and carries **zero** weight.
2. 🔴 **Gate on the SPDX family's permissive property, not on a three-string whitelist.** `ISC`, `0BSD`, `Zlib` and `BSD-2-Clause` are all permissive and all absent from the mandate's wording.
3. 🔴 **Read the whole payload, not the title line.** A grant file may carry two families **conjunctively**; the title names only the first.
🔵 And the instrument note that makes all three runnable here: on this network `gh api` and `curl -sI https://github.com/...` both return **`403`** for live repositories, so existence is `git ls-remote --symref` and the grant is `raw.githubusercontent.com`.

---

## 🆕 T167 — added at p707 (2026-11-08)

### `T167` — A payload-read licence is a **dated** fact, not a standing one — and the dangerous direction of drift is the one no changelog announces

🟢 **Confidence: HIGH.** Direct, dated, in-pass, with the superseded blob still retrievable for comparison.

**Evidence (direct, this pass).** [`Kernel0x19/klyro`](https://github.com/Kernel0x19/klyro) was filed at `p701` with its grant read from the bytes: 🟢 **MIT**, `LICENSE`, `1,076 B`, sha256₁₂ `47da2dc24851`. Seven days later, commit `7fa0ebe` (`2026-11-08`) replaced it with 🔴 **AGPL-3.0** (`33,725 B`, `70adc423756c`). Both blobs are still in history, so the `p701` reading can be confirmed byte-exact rather than assumed: **the reading was right and went stale.**

**Why it is a trend and not an anecdote — three structural claims, each falsifiable.**

🔴 **(1) The consequential direction is permissive → copyleft, and it is the under-watched one.** `T158` recorded drift *toward* permissive (`OpenMAIC`: AGPL-3.0 → MIT, `v0.3.0`) and read it as research projects chasing adoption. That direction is **benign to a stale row**: a row saying 🔴 AGPL about an MIT repository under-sells a usable asset. The reverse is **not symmetric** — a row saying 🟢 MIT about an AGPL-3.0 repository tells an engagement it may embed network-copyleft code in a managed service. **The cost of the two errors differs by about the price of the engagement**, so they do not deserve equal monitoring.

🔴 **(2) The announcement channel fails exactly where the risk is highest.** `T158`'s operational rule was *“check the changelog for the word **relicensed**”*. `klyro` has **no changelog**, and its commit says *“update license to AGPLv3”* — the string `relicensed` appears nowhere in the repository. The asymmetry is sociological: a project relicensing *toward* permissive is **courting adopters and therefore announces it**; a solo maintainer going copyleft is **closing a door and buries it in a patch bump** (`v0.2.1`, alongside an unrelated OAuth fix). 🔵 **So the keyword heuristic is systematically blind to the direction that costs money.**

🟢 **(3) There is a cheap channel that does not depend on the maintainer's prose: the API `spdx_id`.** On `klyro` the detector agreed with the payload and disagreed with this base — the inverse of this page's usual finding (`T162`, `T166`, and the `NOASSERTION` families at `690-R2`/`690-S`), where the detector under-reads a grant the payload states plainly. 🔵 **Both facts are true at once and they are not in tension:** `spdx_id` is a **poor adjudicator** of what a grant says and a **good tripwire** for the fact that it *changed*. Use it for the second job only, then read the bytes.

**Measured scope of the exposure.** This base holds **`595` distinct repositories** across three shelves, the overwhelming majority payload-read **once, at filing**, some more than `100` passes ago. `p707` diffed all `595` and found `1` reversal — but `klyro` was the **youngest row on the shelf**, which says nothing reassuring about rows filed at `p550`. 🔴 **The base has no re-read cadence, and `T167` is the argument that it needs one more than it needs a `36th` supply sweep.**

**Operational consequence.** 🟢 Carry a **date** with every licence cell and treat an undated one as unverified. 🟢 Run the `spdx_id` diff over the whole shelf as a standing pass step — `50` calls, under four minutes, cheaper than one mandated leg (`707-R2`). 🟢 Confirm every disagreement by reading the payload bytes **before** touching a row, and scope the comparison to the **licence column** (`707-R3`: a row-wide regex scored `0/17`). ⚠️ And when a relicence is found, do **not** quietly reroute reuse to the last permissive tag: that snapshot's grant is not retroactively withdrawn, but choosing to rely on it is a decision for counsel, not for a KB row. Wired as **`P102`**.

## 🆕 T162–T166 — added at p706 (2026-11-08)

### `T162` — A licence is identified by its **operative text**, not its title — and the instrument can now under-read a grant that is entirely in order

This base has spent many passes on payloads that claim **more** freedom than they grant (`686` on `spdx_id`, `704` on dangling grant references, `705-A` on a dependent misreporting its dependency). **p706 recorded the opposite failure for the first time: a textbook MIT grant that a title-matching detector cannot classify, because the three letters `MIT` do not occur in the payload at all.**

[`particify/arsnova-webclient`](https://github.com/particify/arsnova-webclient)'s `LICENSE.md` (`1,073 B`) opens on its copyright line and goes straight into *“Permission is hereby granted, free of charge…”*. Every operative clause is present and unmodified. It was **one grep away from being refused a shelf row for an unreadable licence.**

🔵 **Why this direction is the expensive one, and it is the mirror of `705-A`:** permissive-washing creates legal exposure, which is loud. **Under-reading a clean grant is silent — a viable MIT substrate simply never reaches the client's option set, and nobody ever learns it was dropped.** 🟢 **The trend to watch: licence *detection* is becoming a distinct source of error from licence *claims*.** Treat an `UNKNOWN` from any fast-path classifier as a **queue for a body read**, never as a verdict.

### `T163` — The unit of education-AI work is becoming the **agent layer over a national system of record**

p706 filed the first two worked examples this base has seen: [`aikarjal/wilmai`](https://github.com/aikarjal/wilmai) (`82★`) over **Wilma**, Finland's school information system, and [`Casperjuel/aula-mcp`](https://github.com/Casperjuel/aula-mcp) (`65★`) over **Aula**, Denmark's national school platform — the latter with **first-party MitID (national eID) authentication and explicitly no headless browser.**

🟢 **These are not tutors. They are connectors with agent skills attached**, and they are the two highest-starred EMEA education subjects this base holds. 🔵 **The trend reading: the scarce asset has moved.** Models are abundant and interchangeable; **authenticated, sanctioned access to the system where grades, messages and schedules actually live is not.** A national eID integration is a compliance artefact that takes months and cannot be prompted into existence.

🔵 **Corollary for a studio: the reusable asset across engagements in one country is the connector, and it is reusable precisely because the platform is national.** Finland has one Wilma; Denmark has one Aula.

### `T164` — Grading is bifurcating into **decided** and **estimated**, and defensibility is becoming the selection criterion

p706 probed five permissive autograders in one pass and they split cleanly on a question nobody was asking two years ago: **is the grade a decision or an estimate?**

- **Decided** — [`robertylewis/lean4-autograder-main`](https://github.com/robertylewis/lean4-autograder-main): the **Lean 4** proof checker is the ground truth. No rubric drift, no judge prompt, no temperature.
- **Estimated** — the LLM-judge and rubric patterns across this base, plus [`uhafner/autograding-model`](https://github.com/uhafner/autograding-model)'s metric configuration as the deterministic middle (tests, coverage, static analysis: decided, but of *proxies*).

🔵 **The trend is not that proof-checking will spread — most subjects cannot be formalised.** It is that **the existence of a decided mode establishes the standard against which estimated grading is now judged**, and “the model scored it” is becoming an insufficient answer wherever a grade is contestable — admissions, certification, academic-integrity proceedings. 🟢 **Expect “how is this grade defensible?” to arrive as a procurement question.**

### `T165` — The **deployment constraint** has become a design axis, and it is the same axis in all four regions

p706's four regional legs produced four different reasons for one architectural requirement:

| Region | Stated constraint |
|---|---|
| North America | **COPPA** — under-13 data |
| EMEA | AI Act post-market surveillance; **“prioritise European LLMs”** (EUA, Jan 2026) |
| APAC | **AI sovereignty** as the region's organising theme for `2026` |
| LATAM | **Connectivity and device limits** in rural/underserved public schools |

🟢 **Four rationales, one requirement: the tutor must not assume a cloud round-trip to a single foreign provider.** p706 filed three distinct answers already shipping — **offline-first with a local *or* cloud model** ([`Luxshan2000/ielts-prep`](https://github.com/Luxshan2000/ielts-prep)), **closed-network / zero-egress** ([`skt09/IndiGrader`](https://github.com/skt09/IndiGrader)), and **BYOK**, which moves model cost *and* data custody to the learner ([`its-ahoh/litcode`](https://github.com/its-ahoh/litcode)).

🔵 **The trend reading: provider-swappability and graceful degradation are moving from engineering preference to contract term.** A cloud-only, single-provider tutor is becoming unsellable in three of four regions for three different reasons.

### `T166` — Licence payloads are starting to be **retyped or model-generated** rather than copied

[`tryskilly/skilly`](https://github.com/tryskilly/skilly) ships an Apache-2.0 payload at `10,785 B` against canonical `11,357 B` whose body contains **three word-level edits** (`to Licensor` → `to the Licensor` twice; `excluding those notices` → `excluding any notices` in §4(d)). **All three are semantically inert — verified by reading each in context — so the grant is Apache-2.0.**

🔵 **The finding is the mechanism, not this instance.** A verbatim legal text does not acquire definite articles by accident: **this payload was regenerated rather than copied.** Apache-2.0 §4(a) obliges a redistributor to supply *a copy of this License*, and a paraphrase is not that copy.

🟢 **Why it is a trend and not a curiosity: the generation step is cheap and now routine, and the next paraphrase may not be inert.** A single altered word in §2 (grant scope) or §3 (patent grant) would be substantive and would read exactly as innocuous as these three do. 🟢 **Standing, cheap defence, which paid for itself in one pass:** keep a byte-exact canonical control (this base now uses [`howardlau1999/autograder-server`](https://github.com/howardlau1999/autograder-server), `11,357 B`, sha256₁₂ `c71d239df917`) and **diff any payload whose size diverges** — `4 / 4` divergent payloads explained, `3` cleared, `1` flagged.


## 🆕 T158–T161 — added at p705 (2026-11-08)

### `T158` — A licence claim now propagates DOWNSTREAM faster than a relicence does, so the dependent's README is the stale copy

**Evidence (direct, this pass).** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) **relicensed from AGPL-3.0 to MIT at `v0.3.0` on `2026-06-28`** (its own changelog). Read at `main` at `p705`: `LICENSE` `1,065 B`, sha256₁₂ `ba2525637432`, MIT, © *2026 THU-MAIC*; `package.json` `"license": "MIT"` at `"version": "1.4.1"`. Its dependent [`CogEvol/CogEvol-4B`](https://github.com/CogEvol/CogEvol-4B) (`48★`) still states in §12: *"The OpenMAIC patch modifies AGPL-3.0 code; combined works inherit AGPL-3.0."* **Stale by over four months and `11` releases.**

**Why it is a trend and not an anecdote.** Relicensing *toward* permissive has become common as research projects chase adoption — and the act is a one-line changelog entry in one repository, while the claim about it lives in every dependent's prose. 🔴 **The asymmetry is structural: a relicence is `O(1)` to perform and `O(n)` to propagate.** The error therefore skews **pessimistic** — dependents under-report their upstream's freedom — which is the opposite of the permissive-washing this base usually guards against, and it is costlier in practice because nobody audits a *conservative* licence claim.

**Confidence: high** on the instance (two first-hand channels plus a dated changelog); **medium** on the generalisation (one measured case, a second in `p704`'s canonical-versus-fork).

**Operational consequence.** *Licence facts travel only from the owner's grant payload at the real default ref.* Treat a dependent's statement about its dependency as a lead. 🟢 **And always check the changelog for the word "relicensed" before accepting ANY licence claim older than the upstream's last minor release.**

### `T159` — The teaching artifact is shipping as a skill inside someone else's agent host, which makes it invisible to platform-shaped triage

**Evidence.** `3` of the `4` agents filed at `p705` have no deployable surface: `dsh-openmaic` and `dsh-answer-reviewer` are DeepSeek Harness host plugins, `feifei-companion` is an OpenClaw skill distributed via ClawHub. The measured symptom: **`feifei-companion` was written into this base `26` times and shelved `0` times** before `p705`. `p704` found the same pathology at scale — `12` of `13` verified subjects already written, none shelved.

**The mechanism, stated as a defect in the OBSERVER.** A triage question of the form *"can this be stood up?"* silently rejects everything that has nothing to stand up. 🔴 **So the `26`-sighting miss was not a supply gap, it was an instrument gap** — the same class of error `T130` recorded for LATAM, where a star floor manufactured a regional nil.

**Confidence: high** on the shift (counted across two passes); **medium** on durability (it tracks host-plugin ecosystems that are themselves young).

**Consequence for Globant.** 🟢 A skill inherits the host's auth, UI and session management, so engagement cost collapses to **rubric + content**. 🟡 The cost is plugin-API lock-in — and the mitigation is visible in `dsh-answer-reviewer`, whose gate is host-agnostic logic behind a host-specific adapter.

### `T160` — Education's regulatory duties are arriving through general high-risk classification, not education statutes — with Australia the exception

**Evidence across three regions this pass.** **Vietnam** (AI law effective `1 Mar 2026`) names education among **six high-risk sectors**, with *automated assessment* as the worked example. **South Korea's** AI Basic Act (in force `22 Jan 2026`) imposes transparency, risk assessment, human oversight and documentation on *high-impact* systems generally. The **EU's** Annex III catches education where a system evaluates learners, assigns them to programmes, detects prohibited assessment behaviour, or influences access to qualifications. 🟢 **The exception: Australia's `TEQSA` acts as an education regulator directly, requiring ALL higher-education providers to file institutional generative-AI action plans.**

**Why the distinction is commercially decisive.** A horizontal high-risk regime attaches to a **product feature**; an education-regulator mandate attaches to **every institution**. 🔵 **The first produces a conformity-file engagement with one vendor; the second produces a universal, per-institution, document-shaped engagement.** North Carolina's Session Law `2026-41` is the North American instance of the second shape — statutory dates, every local unit in scope.

**Confidence: high** on the pattern; **the commencement dates are secondary and contested** (see `705-C` — EUR-Lex is network-policy-blocked from this environment and the conflict is retired as unresolvable).

**Consequence.** 🟢 Scope by **trigger feature** in horizontally-regulated markets: a system that *scores a learner* is caught; a lesson-authoring tool no learner is scored by generally is not. That boundary, not the date, sets an EMEA or APAC product's cost.

### `T161` — On-device course generation has crossed from demo to deployable, and it resolves the budget constraint and the sovereignty constraint with one artifact

**Evidence.** [`CogEvol/CogEvol-4B`](https://github.com/CogEvol/CogEvol-4B) (MIT code; weights Apache-2.0 on HuggingFace; `arXiv:2608.30968`): a `4B` model post-trained (Qwen3.5-4B hybrid, `48` GDN linear-attention + `16` full-attention layers → mix SFT on `53,687` production-verified samples → slide RL → HTML RL) that turns a one-line brief into structured slide JSON **and** self-contained interactive HTML in a single forward pass. **One `2.4 GB` `Q4_K_M` GGUF file**; the README's own measurement is **~`33` tok/s generation, ~`470` tok/s prefill on an M2 Pro (16 GB)**, a full interactive course in **~`6` minutes**, **zero external dependencies at inference**, demoed with WiFi off.

**Why it matters now rather than as a curiosity.** Two separate constraints this base has recorded independently collapse into one solution: 🟢 **LATAM's budget constraint** — UNESCO IESALC `2026`: `55%` of institutions have **no AI budget** and public universities run **`4%`** dedicated funding, against `87%` already using AI — and 🟢 **APAC's data-sovereignty precondition**, where Malaysia and others treat sovereignty as foundational to adoption. A model that runs on the lecturer's existing laptop has **no per-seat cost and no data egress**, satisfying both by construction rather than by contract.

**Confidence: medium-high.** The capability claims are the authors' own measurements on named hardware and are reproducible in principle (weights are public, the file is one download); adoption is low (`48★`). 🟡 **The deployment takes TWO grants — MIT for the repository's code, Apache-2.0 for the weights on HuggingFace** — and anyone costing it must read both.

**Consequence.** 🔵 Where bandwidth or budget is the binding constraint, the offline generator is now the *default* candidate and the hosted platform is the one that needs justifying — an inversion of this base's standing assumption for low-connectivity engagements.

## 🆕 T154–T157 — added at p704 (2026-11-08)

### `T154` — "Open source" in education is now a claim to be verified, not a category to be filtered on

🟢 **Evidence, all read at the grant payload this pass, not inferred:** of `19` subjects probed, `4` failed the permissive test and **each failed in a different way** — Elastic 2.0 presented as open source at `340★` ([`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp)); AGPL-3.0 asserted as MIT by a search leg at `8,944★` ([`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm)); a README advertising MIT with **no licence file at any of `10` paths** at `104★` ([`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms)); and a BSD-3 notice naming **no holder** ([`langx/langx`](https://github.com/langx/langx)).

🔵 **Why education amplifies this more than other verticals:** the buyer is a procurement office or a ministry, the artefacts spread through blog roundups and star rankings rather than vendor diligence, and the deployment is usually **hosted on the institution's behalf** — which is exactly the act source-available licences single out. **The trend is not "more restrictive licences"; it is a widening gap between the licence a project is believed to have and the one in its repository.** `P96` monetises closing that gap.

### `T155` — LMS agents are moving from per-user API tokens to institutional SSO, and that is what unblocks pilots

🟢 [`Mattlo0546/canvas-mcp`](https://github.com/Mattlo0546/canvas-mcp) (MIT, filed at `p704`) authenticates to Canvas by **university single sign-on instead of an API token**, with a UK institution hard-coded as its default host. Every other Canvas and Moodle MCP server on these shelves — and this base carries **`14`** of them — requires a per-user token.

🔵 **The token step is where campus pilots die**, and it is an administrative failure rather than a technical one: it requires each student or instructor to generate and paste a credential, which no institution will instruct at scale and no privacy office will wave through. **Riding the institutional login the user already has converts a per-seat onboarding task into a one-time integration.** 🟡 At `2★` this is an early signal, not an established pattern — filed for the mechanism. **Watch for the same move in Moodle servers**; whichever one makes it first becomes the default recommendation on this shelf.

### `T156` — Cognitive load is appearing as a first-class, instrumented signal rather than a pedagogical aspiration

🟢 [`wenflow-org/wenflow`](https://github.com/wenflow-org/wenflow) (MIT, `64★`) tracks named load metrics — `LSS`, `KTL`, `LF`, `LSB` — alongside forgetting-curve review, and clarifies the learner's goal **in dialogue before** generating a path. 🔵 **The contrast with the rest of this shelf is the finding:** essentially every other tutor row instruments **completion** (lessons finished, items correct). Completion is a proxy that rises when material is too easy, which is the failure mode adaptive learning exists to prevent. **An explicit load signal is the first thing on these shelves that could close that loop**, and it is the natural input to the retention layer `T157` describes. 🟡 One instance; the metric definitions are the project's own and this base has not validated them.

### `T157` — The tutor/retention split is hardening into two separately adoptable layers

🟢 `p704` filed a dedicated **retention** artefact — [`kirill-markin/flashcards-open-source-app`](https://github.com/kirill-markin/flashcards-open-source-app) (MIT, `108★`, iOS/macOS/Android/web from one codebase) — alongside tutor-shaped and **assessment-rehearsal**-shaped rows ([`PrepLabsAI/InterviewMentor`](https://github.com/PrepLabsAI/InterviewMentor), MIT, `116★`).

🔵 **Three distinct slots are now visible and separately populated on this shelf: explain (tutor), rehearse (assessment), retain (spaced repetition).** They are being built by different authors with no shared interface, which is both the opportunity and the cost — composition means writing the glue, and the glue is where an engagement's margin is. `P95` wires explain→author→retain explicitly for that reason.

## T130 — LATAM's open-source education supply was never nil: it was **below the star floor**, and the floor was this base's own instrument 🔴 new at p700

**The standing claim this overturns.** This page has said for six passes that LATAM's open-source education supply is *nil on three independent channels* — collided English topic heads, Spanish and Portuguese **description** terms (`0/90` at `p691`), and institutional organisations (`422` on all five probed at `692-I`) — and concluded that **LATAM is build-and-translate, not procurement**.

🔴 **The conclusion was an artefact of the adoption floor.** p700 swept the Spanish and Portuguese **`topic:` heads** — a channel distinct from the description terms `p691` spent — and read `total_count` directly for each: `topic:educacion` → **`427`**, `topic:educacao` → **`405`**, `topic:enem` → **`145`**, `topic:aprendizaje` → **`107`**, `topic:ensino` → **`75`**, `topic:vestibular` → **`36`**. Deduplicated against all `5,565` slugs this base holds and filtered to **permissive, unarchived, pushed since 2026-06**: **`108` novel repositories.**

🔴 **And here is the mechanism, which is the part that transfers.** Every supply census this base has run used a `stars:>20` or `stars:>40` floor. Of those `108` LATAM rows, the **highest is `5★`** and the median is `1★`. The entire layer sits *underneath* every floor this base has ever used, so six consecutive censuses returned a true `0` for the query they actually ran and a false `0` for the question they were asking.

| What was measured | Reading |
|---|--:|
| Novel permissive live LATAM-vocabulary repositories, p700 | **`108`** |
| Highest star count among them | **`5★`** |
| Star floor used by every prior LATAM census | `≥20★` / `≥40★` |
| Prior passes concluding "LATAM supply nil" | `6` |

🟢 **What is actually down there is not hobby code.** A complete **MIT Chilean national curriculum** — twelve levels, `149` subject guides, PAES and SIMCE instruments with rubrics ([`chilean-school-learning-path`](https://github.com/vladimiracunadev-create/chilean-school-learning-path)). A **calibrated Apache-2.0 ENEM essay grader with its own evals harness** ([`mooose`](https://github.com/matheussilvano/mooose)). A **pt-BR model that labels the five intervention elements and refuses to score** ([`enembert`](https://github.com/akagabi/enembert)). An ENEM item API, an MCP server over it, and a Brazilian state high school running a seven-repository MIT estate.

🔵 **This is `680-D` and `692-J` arriving at a region.** Both findings said the star floor hides substance; neither applied the observation to a *regional* conclusion, and so a measurement artefact was published as regional intelligence six times. **The transferable rule: a regional supply claim may never be made from a star-floored query.** If the floor cannot be dropped, the claim must be stated as *"no adopted supply"*, which is a different and much weaker sentence than *"no supply"*.

---

## T131 — A licence probe must be exhaustive in **case**, not only in name — and the one that is not fails toward *refusal* 🔴 new at p700

**`T123` (p698) is correct and incomplete.** It added non-canonical licence *names* (`MIT-LICENSE`) to the sweep and retired the British `LICENCE` spelling as a non-finding. It did not touch **case**.

🔴 [`nwuzmedoutlook/university`](https://github.com/nwuzmedoutlook/university) — **`1,230★`**, Apache-2.0, a 120-university course corpus — carries its grant at **`License`**. At the real default ref, `LICENSE` returns `404` and `license` returns `404`.

🔵 **Controlled at both signs in the same pass.** `License` → `200` on `nwuzmedoutlook/university` and `404` on `google/comprehensive-rust`; `LICENSE` → exactly the reverse. **`raw.githubusercontent.com` is strictly case-sensitive on the path; GitHub's own licence detector is case-insensitive** and resolved `spdx=Apache-2.0` correctly.

🔴 **So the usual direction of distrust inverts.** This base routinely treats `license.spdx_id` as the weaker channel (`T121`, and `p686`'s measurement of it). Here **the index was right and the payload probe was wrong**, and a five-name uppercase sweep would have recorded *no grant* on a clean Apache-2.0 repository and refused it. 🟢 **The fix: iterate case variants (`LICENSE`, `License`, `license`) across every name, and treat a full-sweep miss as a statement about filenames — never about rights.** `T123`'s own closing sentence, now with one more axis.

---

## T132 — LATAM's institutional channel is a **grant** nil, not an existence nil, and that is a different problem with a different fix 🔴 new at p700

🔴 **`692-I`'s conclusion rested on a bad owner list.** It probed `org:ceibal`, `org:ceibal-uy`, `org:fundacionceibal`, `org:plan-ceibal` and `org:cenia`, got `422` on all five, and concluded the LATAM institutional channel was dead. p700 probed a different list and **`org:fundacion-sadosky` resolves to `21` repositories** — Argentina's public-private ICT foundation, tied to its Ministry of Science, Technology and Innovation. Controls green (`org:learningequality` → `203`, `org:moodle` → `12`).

🔵 **A `422` is a statement about the owner *string*, not about the region.** `T129` made `org:` an existence oracle **for an owner**; it is not an existence oracle for an institution, because the institution's GitHub handle is a fact you must look up rather than guess. Five guessed handles produced a regional conclusion.

🔴 **But the honest finding is the licence, and it is worse for an engagement than absence.** Across that estate the 2026 education-relevant output is [`microbitML`](https://github.com/fundacion-sadosky/microbitML) (**GPL-3.0**) and `GURO`, a robotics-kit updater carrying **no grant at any of seven name-and-case variants**. The remainder is security and CTF material at `NONE` or `NOASSERTION`.

🟢 **So the regional statement that survives is sharper than either prior version:** LATAM institutions *do* publish education software, and they publish it **copyleft or ungranted**. The gap is not discovery and not supply — it is **permissive licensing**, which is a conversation an engagement can actually have with a ministry, unlike an absence.

---

## T133 — Brazil's national examination is a permissively-supplied **assessment stack**, and it is the only national exam on these shelves that is 🟢 new at p700

🟢 **Five permissive, live, independently-owned components now cover ENEM end to end**, every one filed at p700 and every grant payload byte-read at its real default ref:

| Layer | Component | Grant |
|---|---|---|
| Item bank | [`lyodekkendev/enem-api`](https://github.com/lyodekkendev/enem-api) | 🟢 MIT |
| Agent surface | [`EduardoMilani8/mcp-enem`](https://github.com/EduardoMilani8/mcp-enem) | 🟢 MIT |
| Essay marking (production-shaped) | [`matheussilvano/mooose`](https://github.com/matheussilvano/mooose) | 🟢 Apache-2.0 |
| Essay marking (research scorer) | [`hito-boo/enem-essay-scoring`](https://github.com/hito-boo/enem-essay-scoring) | 🟢 MIT |
| Decidable span labelling | [`akagabi/enembert`](https://github.com/akagabi/enembert) | 🟢 MIT |

🟢 **The stack's design is better than its star counts suggest, and in one specific way it is ahead of the English-language rows on these shelves.** `mooose` constrains output to the only legal ENEM score set (`0/40/80/120/160/200`), encodes the zeroing rules, scores Competency 5 from an explicit checklist, ships an **evals harness against human-marked essays**, and labels its own output an unofficial estimate. `enembert` goes further and **removes the score**, returning only which of the five intervention elements are present — a verdict a teacher can check and a regulator can audit.

🔵 **`T90` said the strongest agents demote the LLM to narrator and take ground truth from a domain solver.** This stack is the first place where the *ground truth is a published national marking guide* and the artefact is a span label rather than a number. 🟡 **The limit, stated:** adoption is near zero (`0–5★`), so these are bases to fork and harden, not services to depend on.

🟢 **And one institutional row underneath it all:** [`org:eemtijca`](https://github.com/eemtijca) — a **Ceará state high school** — publishes a seven-repository MIT estate covering school management, attendance with its own MLOps engine, teacher lesson-note authoring, and twenty BNCC-aligned games built on **UDL** principles for Brazil's specialised-support programme. `p693` filed one of those repositories. The other six were one query away for seven passes. See `T134`.

---

## T134 — Every filed row carries an **unqueried owner**, and that channel is cheaper and richer than any topic head left 🟢 new at p700

🔴 **The defect, found by a gate rather than by reasoning.** p700 attempted to file [`eemtijca/buscapp`](https://github.com/eemtijca/buscapp) as novel; the duplicate-slug gate rejected it, because `p693` had already shelved it. **The school was known. The school's *organisation* had never been queried** — and it holds six more repositories, five of them novel and permissive.

🔴 **Generalised across eleven owners this base has already filed from, the gap is systematic and large:**

| Owner already on these shelves | Repositories it publishes | Rows this base held |
|---|--:|--:|
| `endlessm` | `233` | `1` |
| `alibaba-damo-academy` | `92` | `1` |
| `pisan-labs` | `60` | `2` |
| `openjournals` | `40` | `1` |
| `dodona-edu` | `36` | `2` |
| `insightflo` | `24` | `1` |
| `groundworklms` | `14` | `1` |
| `eemtijca` | `7` | `1` |

**Measured yield across those owners: `356` siblings pulled → `337` novel to this base → `159` permissive, unarchived and pushed in 2026 → `20` education-shaped → `6` filed at p700.** That is a `1.7%` filing rate on raw siblings and a `30%` filing rate on the education-shaped subset — **against a topic channel that `680-B` measured as `1/21` adoptable and declared finished.**

🟢 **What it actually produced this pass, to make the yield concrete.** `dodona-edu` — held since `p680` as *"the one live permissive option"* in academic integrity — also publishes **TESTed**, a peer-reviewed language-agnostic autograder (`doi:10.1016/j.softx.2023.101404`), plus **four per-language judges**. `groundworklms` — one row filed at `0★` on substance at `692-J` — is a **five-service Apache-2.0 LMS platoon** including an offline grounding engine that refuses uncited answers and a **JSON→SCORM cartridge builder** that drops generated courseware into Moodle or Canvas and reports to the gradebook. `pisan-labs` publishes a course Q&A box that answers **only** in verbatim quoted sentences and says *"Not stated in the course documents"* otherwise.

🔵 **Why this channel is structurally better than the one it replaces.** A topic head is a **stranger's** tagging decision, which is why `692-H` found four heads returning a different industry and `T105` had to be written. An owner is a **fact this base has already verified** — it filed a row from it, read its grant, confirmed its liveness. Expanding a known-good owner inherits that provenance; querying a new topic head inherits nothing. 🟢 **The standing instruction: when a row is filed, query its owner in the same pass.** `680-J` found the ledger under-records addresses the tree already held; this is the same shape one level up — **the base under-queries the owners it has already trusted.**

---


## T126 — Permissive density in public-sector education software tracks the **procurement doctrine**, not the jurisdiction: a declared digital public good runs `92%` permissive where one national ministry runs `62%` and another runs `0.5%` 🟢 new at p699

**Measured at p699 over six organisations, `212` repositories, licence read from GitHub's `license.spdx_id` and the grant payload read at first hand for the six filed rows:** India's **Sunbird** estate is **`196 / 212` = `92.5%`** permissive (`185` MIT + `11` Apache-2.0). Set against `p698`'s European readings on the identical instrument — **UK DfE `515 / 828` = `62.2%`, France (`openfun`) `52 / 100`, Finland (`Opetushallitus`) `1 / 182` = `0.5%`, GÉANT `0 / 54`** — the spread is a factor of **`185`** between the top and bottom estates, and **it does not line up with the continent.**

🔴 **This supersedes the causal claim in `T122`, and the correction matters because `T122` was already being used to reason about regions.** `T122` read the UK-versus-Finland split as *"bimodal by jurisdiction"*. Jurisdiction is a **proxy**. The operative variable is whether the estate was **built to be adopted by someone else**: Sunbird is a **Digital Public Goods Alliance**-registered DPG whose entire purpose is third-party adoption, and it is MIT by construction across six orgs and eleven years of copyright lines. Finland's ministry publishes source code without granting rights to it — publication as transparency, not as supply. **The UK's `62%` sits between the two because the DfE estate is genuinely mixed: shared libraries are MIT, individual services often are not.**

🔵 **The operational consequence for a studio: ask what the estate was FOR before pricing the licence risk.** An estate built as a public good can be cleared cheaply and in bulk (`T128`); an estate published for transparency must be cleared repository by repository and will mostly come back unusable. `T122`'s observation stands as data and is retired as an explanation.

## T127 — The grant-payload `sha256` is a provenance discriminator for **MIT** and a **non**-discriminator for **Apache-2.0**, because MIT carries the holder inside the payload and Apache-2.0 does not 🔴 new at p699

**This base publishes `sha256₁₂` in nearly every shelf row as an identity signal. For an Apache-2.0 row that signal certifies the stock text and nothing whatsoever about who granted it.**

🟢 **Control run at both signs at p699.** The payload `c71d239df917` / **`11,357 B`** is **byte-identical** across [`Sunbird-inQuiry/editor-v2`](https://github.com/Sunbird-inQuiry/editor-v2), [`Sunbird-inQuiry/player-v2`](https://github.com/Sunbird-inQuiry/player-v2) **and** [`lungstrahv/T2AG`](https://github.com/lungstrahv/T2AG) — a single-author project in a different jurisdiction with no relation to Sunbird whatever. Two of those three addresses are the same estate and one is a stranger, and **the digest cannot tell them apart**, because the stock Apache-2.0 text keeps the holder in the file headers and the `NOTICE`, not in `LICENSE`.

🟢 **The same instrument on MIT does the opposite, and does it well** — see `T128`: sixteen MIT payloads in one estate partition into **five** digests that differ *only* in the copyright line, and the partition reconstructs the estate's own history.

🔴 **Two readings this base has made, and should stop making, on Apache rows:** that a matching digest across two rows evidences common provenance (it evidences a shared boilerplate), and that a digest is a sufficient per-row licence fingerprint (for Apache-2.0 the discriminating bytes are the **appendix fill state** and the `NOTICE` file, neither of which `LICENSE`'s digest reaches). **For an Apache-2.0 row, read the `NOTICE` or read nothing about the holder.**

## T128 — A licence-uniform estate can be cleared with **one** grant read, and the `sha256` partition recovers a holder history the project never documented 🟢 new at p699

**Measured at p699: `18` Sunbird repositories sampled across all six organisations, `LICENSE` read at the real default ref for each. `16` MIT payloads → `5` distinct digests, every difference confined to the copyright line:**

| `sha256₁₂` | Bytes | Copyright line | Repos seen |
|---|--:|---|--:|
| `fbafd6479167` | `1,074` | © *2015* **EkStep** | `1` |
| `7dde06716f25` | `1,072` | © *2018* Project Sunbird | `5` |
| `fd3adcd57676` | `1,072` | © *2019* Project Sunbird | `3` |
| `47022c44beee` | `1,072` | © *2020* Project Sunbird | `3` |
| `bea3458f45df` | `1,078` | © *2021* **Sunbird for Education** | `1` |

🟢 **Two results, and the second is the one worth keeping.** (1) **Clearance is cheap on an estate like this**: five payload reads clear sixteen repositories, and the marginal read is near-free, so a due-diligence quote priced per repository is mispriced for a DPG estate by an order of magnitude. (2) **The digest partition is a provenance instrument.** The oldest payload names **EkStep** — the foundation that built the platform *before* the Sunbird brand existed — and the newest names *Sunbird for Education*. **Three holder identities and four year-cohorts, in strict chronological order, none of it stated in any README this pass read.** The grant files are the only first-hand record of the handover.

🔵 **Why this is an instrument and not a curiosity:** a client licence gate asks *who granted this*. On an MIT estate the answer is already in the bytes this base publishes, and a change of digest between two sibling repositories is a signal to go and ask why. `T127` is the boundary — this works for MIT precisely because it fails for Apache-2.0.

## T129 — `search/repositories` with an `org:` qualifier is an **existence oracle for an owner**, where the mandated `curl -sI` is an oracle for nothing 🟢 new at p699

🟢 **Measured at p699 over `44` distinct owner logins probed on the authority channel: `20` returned a counted payload, `24` returned HTTP `422`** (*"the listed users and repositories cannot be searched either because the resources do not exist or you do not have permission to view them"*). The two answers are cleanly separated, so **the `org:` qualifier decides owner existence in one call** — and it returns the repository count and the full licence census in the same call, which is why `698-B`'s channel keeps paying.

🔴 **The `curl -sI` check the operating instructions mandate was re-controlled at p699 at four signs and is still inert:** `403` for `torvalds/linux`, `403` for `moodle/moodle`, `403` for [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) and `403` for a repository that **does not exist**. `p684` and `p698` recorded this; p699 confirms it a third time and adds the positive replacement rather than only the complaint:

| Question | Instrument that answers it | Instrument that does not |
|---|---|---|
| Does this **owner** exist? | `gh api search/repositories -f q='org:X'` — count vs `422` | `curl -sI https://github.com/X` → `403` either way |
| Does this **repository** exist, and what is its real default branch? | `git ls-remote --symref <url> HEAD` | `curl -sI` → `403` either way |
| Does this **grant file** exist, and what does it say? | `curl` on `raw.githubusercontent.com` — `200`/`404`, and the payload | `curl -sI` on the repository page |

🔵 **The general rule: `403` is the agent proxy answering, not GitHub.** Any check whose negative and positive signs are both `403` is measuring the proxy. `raw.githubusercontent.com` is reachable and discriminating, which is why every licence claim on this base is read there.

🔵 **A note on numbering, so the next pass does not re-derive it:** p699's trends start at **`T126`**. `T125` is skipped deliberately — archived `trending.md` prose from the pre-reset `p425` era already cites a *different* `T125` (the Frappe-LMS claim), and reusing the label would silently merge two unrelated trends. This file's `## T…` headings are the authoritative registry; it already contains gaps at `T84`–`T87`, so a documented skip is consistent with its own precedent.

## T122 — Permissive supply in European public-sector education is **bimodal by jurisdiction**, not scarce: `515 / 828` MIT in one national authority against `1 / 182` in another 🟢 new at p698

**Measured, both sides, same instrument** (`gh api search/repositories`, `org:` qualifier, `license:` facet), `2026-11-08`:

| National education authority | Repos | MIT | Share |
|---|--:|--:|--:|
| [`DFE-Digital`](https://github.com/DFE-Digital) — UK Department for Education | **828** | **515** | **`62.2 %`** |
| [`Opetushallitus`](https://github.com/Opetushallitus) — Finnish National Agency for Education | `182` | **`1`** | **`0.5 %`** |
| [`openfun`](https://github.com/openfun) — France Université Numérique | `100` | `52` | `52.0 %` |
| [`GEANT`](https://github.com/GEANT) — European research networking | `54` | `0` (`5` Apache-2.0) | `0 %` |

🔴 **`p690` concluded, from the Finnish EUPL block, that *"Europe's public-sector education software reads as unlicensed to every scanner."* That generalisation is now refuted at the continental level and confirmed at the jurisdictional one.** The UK estate is not merely permissive, it is permissive *at scale and under active development* — `161` of its `828` repositories were pushed in the five weeks before this pass.

🔵 **Why the spread is a licence-policy artefact rather than a culture artefact.** The EUPL is the European Commission's own instrument and is what a continental-European public body reaches for by default; it is copyleft, and it is the licence `p690` showed no automated scanner attributes. The UK, outside that instrument's gravity, defaults to MIT. **So the variable that predicts whether a European education authority's code is adoptable is which licence its government's own guidance names** — not its size, its activity or its maturity.

🟢 **Operationally, for an EMEA engagement:** there is no European answer to *"is there permissive public-sector education code to build on?"* — there is a per-country answer, and the countries differ by two orders of magnitude. Ask the question per jurisdiction, and read the payload (`T110`, `T123`), because the Finnish `1 / 182` is **not** a measure of how much Finnish code exists, only of how much of it a licence gate will pass.

## T123 — A five-name licence sweep reports *no grant* on an MIT repository, and the British spelling is **not** the cause 🔴 new at p698

**The hypothesis this pass set out to confirm, and refuted.** `2` of the `10` UK DfE repositories verified ship their grant as the British [`LICENCE`](https://github.com/DFE-Digital/buy-for-your-school) rather than `LICENSE`, and the obvious guess is that GitHub's detector misses it. **It does not:** `gh api` resolves `spdx=MIT`, `key=mit` for both. 🔵 **The British spelling is a non-finding, and it is worth publishing as one**, because it is the kind of plausible mechanism a later pass would otherwise re-derive and act on.

🔴 **The real hazard found in the same probe is a *non-canonical* filename.** [`DFE-Digital/dfe-analytics`](https://github.com/DFE-Digital/dfe-analytics) returns `404` at the real default ref for **all five** names this base sweeps — `LICENSE`, `LICENCE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` — while the grant sits at **`MIT-LICENSE`** (`1,052 B`, `sha256₁₂ 3f9964f228bc`), the Rails-engine convention, and `dfe-analytics.gemspec` declares `spec.license = 'MIT'`.

**So the three channels disagree in a specific pattern:** `gh api` says MIT (it reads the manifest), the payload says MIT (once found), and **the filename sweep says nothing at all.** A sweep that treats `404`-on-five-names as *unlicensed* will mark a cleanly-MIT government library as unusable.

🟢 **The fix is one name and one fallback:** add `MIT-LICENSE` (and `APACHE-LICENSE`) to the sweep, and when all names miss, **read the language manifest** — `gemspec`, `package.json`, `pyproject.toml`, `*.csproj` — before recording absence. 🔵 **This is the exact inverse of the `hacktick/DiLer` case at `p697`** (a declared grant with no file, where prose asserted AGPLv3 and no file existed): there, absence of a file meant the grant had to be read from prose; here, absence of the *expected* file means the grant has to be read from a *manifest*. **Both say the same thing — `404` is a statement about filenames, never about rights.**

## T124 — A regional query token that is a prefix of a common English word returns a majority of homograph noise, and the regional "zero" that follows is an artefact 🔴 new at p698

**`enem`** is Brazil's national secondary-education examination (*Exame Nacional do Ensino Médio*) and the highest-value Portuguese-language education token there is. `enem stars:>10` returns `51` repositories, and the top of the ranking is **English-language `enemy`**: `NatsunXD/EnemySpawnMultiplier` (a Helldivers 2 mod), `freakanonymous/enemy` (an **IoT botnet**), `CiaNCI-Studio/3D-Enemy-Toolkit`, `jhlothamer/behavior_tree_enemy_ai_demo`, `bypell/horror-game-enemy-demo`, `Hamunii/LC-ExampleEnemy`, `EnemyV/EnemyNationsRevival`, `LOVEIII486/EliteEnemies`. **Substring matching makes a national examination indistinguishable from game-mod enemy AI.**

🔵 **This is `T31`'s class — a regional "zero" as a query artefact — reached through a new mechanism, and it is the mechanism that matters.** `T120` recorded that a *two-letter* native-language token is unsearchable because it is too short. `T124` records that a *four-letter* one can be worse than unsearchable: it returns a full page of confident, irrelevant, well-starred results, so the leg looks **productive** while carrying no regional signal at all. A leg that returns nothing invites a second attempt; a leg that returns noise gets believed.

🔴 **Also measured this pass, and the cause is the opposite problem:** three-term AND queries in Spanish and Portuguese (`educacion inteligencia artificial`, `educacao inteligencia artificial professor`) return **`total_count 0`** — not because the layer is empty but because GitHub `AND`s the terms across name/description/topics, and no description carries all three. **`7` legs built that way returned `0` rows; the same `7` concepts as single terms returned `383`.** 🟢 **The rule for every regional leg from here: one native-language product noun per query, and check the token against its English homographs before believing any count it produces.**

## T118 — A star floor stops filtering noise once the noise is star-farmed, and it fails first in the KEYWORD channel 🔴 new at p697

**Claim.** `stars:>N` is a proxy for adoption only while noise is unstarred. A description-identical cluster of **`1,524`** repositories, spread over ~`93` owner accounts and carrying `40`–`90` stars each, now occupies **`30 / 36` rows (`83.3 %`)** of this base's mandated `tutor LLM created:>2026-06-01 stars:>25` leg — `1,656` stars between them, `35` of them farming `tutor` / `tutorial` in the repository **name**, and not one of them an education repository, an agent or a tutorial.

**Evidence.** Measured at p697 (`agents/trending.md` `697-A`): `gh api search/repositories` on the leg as mandated, then the cluster bounded by its byte-identical description string. `topic:` and `org:` legs run in the same pass were unaffected.

**Why it fails in the keyword channel specifically.** A keyword leg selects on **name** and **description** — the two fields a farm fully controls — and then ranks by stars, which a farm can manufacture. A `topic:` facet requires the owner to classify themselves into a taxonomy the farm has no reason to join, and an `org:` enumeration takes the owner as given.

**Consequence.** Prefer a structured facet you do not control over a text match the subject controls. When a keyword leg must be run, measure the share of its rows that share a description before concluding anything about supply — **a nil and a flood look identical in a row count**. Four consecutive passes of this base read this flood as saturation.

**Confidence.** High for the measurement; the cluster is directly countable. The `93`-owner figure is a first-page sample and is a floor, not a total.

## T119 — Institution *adjacency* cannot distinguish an affiliation from a citation, so a placement guard must type the CONTEXT 🔴 new at p697

**Claim.** `p672` established that an institution detector must drop a bare `MIT` unless it is adjacent to `University`, `Institute`, `CSAIL` or `Media Lab` — otherwise it places repositories in Massachusetts off their own licence name. **Adjacency is necessary and not sufficient.** [`TetiAI/lucid`](https://github.com/TetiAI/lucid) passes p672's guard (`MIT` beside `Media Lab`) and must still not be placed, because the token appears in *"[MIT Media Lab, 2025](docs/RESEARCH.md)"* — **the study that motivates the product**, cited in a literature link.

**Repair.** Admit an institution token only from an **authorship context**: a copyright line, a `by <org>` attribution, an author or maintainer list, or a funding statement. Refuse it from a references block, a citation, a documentation link or a "related work" section. This is a *type* judgement about the surrounding text, not another dictionary entry — and `p669` already showed that a dictionary cannot police itself.

**Evidence.** All three placements filed at p697 stand on a copyright line in the grant payload (two naming the Canton of Bern, one refused for naming only a corporate form). `lucid` stands on a citation and is filed `Global`.

**Confidence.** High. One clean counterexample is enough to bound a guard, and the replacement rule is testable on every row this base has placed.

## T120 — A two-letter native-language AI token is unsearchable, so the product-noun shape is not an improvement but the only access to that layer 🟢 new at p697

**Claim.** `KI` — German for AI, and the token any German-language AI probe reaches for first — cannot be used on GitHub's index. `Lernen OR Unterricht OR Schule KI` returns **`15,042`** results whose top thirty are `the-book-of-secret-knowledge`, `spec-kit`, `awesome-rust`, `kitty`, `kibana`, `kivy`, `SnapKit` and `dnd-kit`: the index matches `KI` inside `kit`, `kind`, `kivy`, `kibana`. **`0` relevant.**

**Consequence, and it is the useful half.** `T107` prescribed product nouns over subject nouns because a subject noun returns everything *about* a field. For a language whose AI token is two letters, the ranking is stronger: the subject-noun channel does not merely under-perform, it **does not exist**. Re-run on product nouns (`Schulverwaltung`, `Lernplattform`, `Unterrichtsplanung`), the same layer yielded **three shelf rows** including a cantonal authority's MIT front end.

**Generalisation to check before trusting it elsewhere.** The same hazard applies to any short native AI token — `IA` (Spanish, French, Portuguese, Italian), `IE` (Irish), `KI`. `T108` already found that a Romance-language token selects a family spanning three continents; this is the complementary defect, where the token is too **short** rather than too **wide**. Probe with a multi-word product noun in both cases.

**Confidence.** High for German, measured in-pass. Medium as a general rule for `IA`: this base's Spanish and Portuguese legs used product nouns already and never isolated the token.

## T121 — `NOASSERTION` is not licence-neutral: it can conceal a **NonCommercial** grant, and it conceals it behind the highest star count on the page 🔴 new at p697

**Claim.** `T99` established that `NOASSERTION` is a fact about GitHub's detector rather than about the grant, and that in education it lands hardest on public-sector Europe — where the concealed grants are real, short EUPL texts. **T121 is the sharper and more dangerous case: the detector's silence does not correlate with the grant being usable.** [`HytidelLegend/ai-aug-edu`](https://github.com/HytidelLegend/ai-aug-edu) — `492★`, created `2026-09-23`, the largest novel education repository p697 found by an order of magnitude — reports `NOASSERTION`, and its payload (`750 B`, sha256₁₂ `687d735a7fa1`) is **`Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)`**.

**Why the star count matters to the claim.** A ranked discovery channel surfaces the highest-starred novel repository first, so this is the **first** row a studio evaluates and the **last** one it can build a commercial derivative on. A licence gate that files `NOASSERTION` as *unknown, review later* carries it into a proposal unexamined.

**Operational rule.** `NOASSERTION` is never a reason to skip the payload read, and it is never a reason to assume the payload is benign. Read it, measure it, and classify the **family** — permissive, weak copyleft, network copyleft, **non-commercial**, or none — before the repository is cited anywhere.

**Confidence.** High; single payload read, reproducible, with the API's own disagreement recorded alongside it.
## T115 — A README's declared tool count is not a capability measure: it is wrong in `4 / 4` repositories measured, and it errs in BOTH directions 🔴 new at p696

**Measured at p696, on every MCP server it filed, by counting distinct registered tool names at the real default ref:**

| Repository | README declares | Shipped (measured) | Error |
|---|--:|--:|---|
| [`pdg6/bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) | `12` | **`8`** | 🔴 **`−33 %`** |
| [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | `20` | **`21`** | `+5 %` |
| [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | *“about 230”* | **`269`** | `+17 %` |
| [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | — (**this base** published `35`) | **`39`** | this base's own pin stale |

🔵 **Why this is a trend and not four anecdotes.** The error is **not conservative** — it runs both ways, so a README cannot even be used as a lower bound. And the direction that matters commercially is the overstating one: a studio scoping *“12 curriculum tools”* and receiving `8` has lost a third of an integration surface it already quoted. 🔵 **The understating direction costs differently and is worth hunting:** `moodle-mcp` ships `269` tools and advertises `230`, so **capability discovery by README systematically under-ranks the most capable projects** — which at `2★` is exactly how this base nearly missed the strongest agent surface on its shelf.

🔵 **The method, stated so it is cheap to repeat.** Resolve the real default branch (`git ls-remote --symref`), then count **distinct registered tool NAMES** — not README prose, and not raw call sites, which double-count re-registrations and conditional branches (`273` sites against `269` names here). 🔴 **Corollary for this base's own shelves:** a published tool figure is a *measurement with a date*, not a property. `librus-mcp`'s `35` was correct when taken and wrong when re-read two minor versions later.

## T116 — A curation base's binding constraint flips from DISCOVERY to FILING, and the flip is measurable before it is felt 🔴 new at p696

**p696's measurement on this base, from three independent instruments:** the promotion backlog — addresses written on these pages, absent from all three sell shelves — is **`4,691`**. Its most-cited `90` resolve to `82` live repositories of which **`39` (`47.6 %`) are permissive**. This base's own gate, independently, reports a **filing rate of `8.1 %`** (`447` filed against a union of `5,497`).

🔵 **The diagnostic, and it is the transferable part.** Compare **rows filed per pass** across the two channels on the same base: the four mandated discovery legs have returned `0`–`2` filable rows per pass for nine months and nilled `37` consecutive times in North America alone; **one backlog probe returned `18` in a single pass.** That is roughly an order of magnitude, measured on the same shelves in the same hour by the same instruments.

🔴 **The failure mode this trend names is that a saturated discovery channel LOOKS like a saturated market.** Every nil is honest and every nil is locally correct — *“the leg returned nothing novel”* was true `37` times. The inference *“the region has no permissive supply”* was false the whole time, and p696 refuted it by filing four North America rows in the same pass the North America leg nilled again. **A nil measures the channel, never the field.**

🔵 **The operational rule.** Once filing rate falls below `~10 %`, a pass spent probing the base's own backlog dominates a pass spent searching, and it dominates it on *verified* output rather than candidate volume. 🔵 **The ranking function is the one real choice**: p696 ranked by citation frequency, which reaches the head and **structurally cannot reach a region in the tail** — which is precisely why it filed `0` LATAM rows while `p693` had already counted `163` unshelved LATAM-bearing addresses. **Rank by the axis you owe a row to.**

## T117 — `main` is an assumption, not a fact: one permissive education repository in five defaults elsewhere, and the probe fails toward *absent* 🔴 new at p696

**Measured at p696 over the `39` permissive repositories its backlog probe resolved: `8` (`20.5 %`) have a default branch that is not `main`** — `trunk` ([`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework)), `develop` ([`frappe/frappe`](https://github.com/frappe/frappe), [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi), [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool)), `master` ([`uPortal-Project/uPortal`](https://github.com/uPortal-Project/uPortal), [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)), `2.2` ([`krayin/laravel-crm`](https://github.com/krayin/laravel-crm)) and a **tag-shaped** `v6.2.0` ([`ed-fi-alliance-oss/ed-fi-data-standard`](https://github.com/ed-fi-alliance-oss/ed-fi-data-standard)).

🔴 **The direction of failure is what makes this dangerous rather than merely untidy.** A licence probe that fetches `…/main/LICENSE` gets a `404` and records **no grant** — which reads as *unlicensed*, the verdict that reverses the commercial answer and does so while looking like diligence. Same shape as `695-C` (the `LICENCE`-spelling false negative) and `694-C` (the R-package `LICENSE`-as-metadata case: **three distinct causes, one failure direction**).

🔵 **The skew is not random, and knowing that is worth more than the percentage.** The non-`main` set is concentrated in **old, institutional, standards-adjacent projects** — an ASF project on `trunk`, Apereo on `master`, a data standard pinned to a release tag — i.e. exactly the mature infrastructure an education engagement most wants to build on, and exactly what a `main`-assuming sweep silently deletes from its own candidate pool. **The newest `1★` repositories are the ones reliably on `main`.**

🔵 **Fix, one line, used on all `18` of p696's filings:** `git ls-remote --symref <url> HEAD` returns the real default ref without cloning. 🔴 **Never infer the ref from the host's web UI either** — see `696-J`: in this environment `curl -sI` answers with the agent proxy's `HTTP/1.1 200 Connection Established` for every URL, live or dead.

## T113 — Command substitution strips trailing newlines, so a byte count and a digest published through `$(curl …)` are both wrong — and this base has already "corrected" one row to the true value without naming the cause 🔴 new at p695

**This is a defect in this base's own primary verification instrument, not in the sector.** Every grant cell on these shelves publishes `bytes` + `sha256₁₂` as the identity of a licence payload. Where that pair was produced by `out=$(curl -sSL …)` and then measured with `printf '%s' "$out" | wc -c`, **both numbers are wrong**: command substitution discards *all* trailing newlines before the bytes are ever counted.

**Controlled at both signs, on three payloads, same fetch and same second:**

| Payload | `curl -o file` (true) | `$(curl …)` (substitution) | Δ |
|---|---|---|--:|
| [`edificeio/infra-front`](https://github.com/edificeio/infra-front) `LICENSE` | **34,520 B** · `76a97c878c9c` | 34,519 B · `d8de517917a5` | **−1 B** |
| [`edificeio/springboard`](https://github.com/edificeio/springboard) `LICENSE` | **34,521 B** · `432d251a78db` | 34,519 B · `91b65277959e` | **−2 B** |
| [`apache/.github`](https://github.com/apache/.github) `LICENSE` | **11,357 B** · `c71d239df917` | 11,356 B · `43070e2d4e53` | **−1 B** |

🔴 **The consequence is a manufactured collision, and it is the dangerous half.** `infra-front` and `springboard` are genuinely different files — `34,520` against `34,521` true bytes, different digests — and they differ in one line of the AGPL appendix's word-wrap plus a trailing blank line. **Under the faulty instrument they both report `34,519 B`.** A pass comparing byte counts concludes "same payload"; a pass comparing digests does not. **So the digest survives the defect and the byte count does not**, which inverts how this base presents the pair: the byte count is printed first and read as the identity.

🟢 **And the base has already paid for this once, on a row it repaired without diagnosing.** `p674` re-measured [`oppia/oppia`](https://github.com/oppia/oppia) and corrected its Apache-2.0 payload from `11,357 B` to **`11,358 B`** (`cfc7749b96f6`). Re-measured at p695 with both instruments: the true file is **`11,358 B` / `cfc7749b96f6`** and the substitution reading is **`11,357 B` / `58d1e17ffe51`**. 🔵 **`p674`'s "correction" was the exact difference between the two instruments.** It fixed one cell and left the instrument in place, so the same `−1 B` sits in every cell measured the same way and nothing on the page distinguishes them.

🔴 **A second, independent reason byte count cannot be an identity: Apache-2.0 in the wild is a *family* of payloads, and p695 measured four of them in one sitting.**

| Apache-2.0 payload | True bytes | sha256₁₂ | Shape |
|---|--:|---|---|
| [`edificeio/web-utils`](https://github.com/edificeio/web-utils) · `cas-server-async` · `mod-postgresql` | **10,174** | `0d542e0c8804` | appendix **stripped** (three repos, byte-identical) |
| [`apache/.github`](https://github.com/apache/.github) · [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | **11,357** | `c71d239df917` | with appendix (three repos, byte-identical) |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **11,358** | `cfc7749b96f6` | with appendix |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **11,408** | `cd2f54e1e506` | with appendix |

**Four byte counts, four digests, one licence — and `11,357` against `11,358` is a one-byte difference between two genuine, widely-deployed copies.** This base uses `11,358 B` as *the* canonical reference figure; **it is one member of a family, not a test.** 🟢 **The constructive half: byte-identity across repositories is strong evidence and is cheap to check** — the two triples above each collapse to a single digest, which is how a pass should say "same payload".

**Remedy, and it is mechanical:** fetch to a file (`curl -sSL --fail -o f`), then `wc -c < f` and `sha256sum f`. Never measure a payload through a shell variable. Where a published cell cannot be re-derived, **the digest is load-bearing and the byte count is advisory**.

**Confidence: high** — three payloads, both instruments, deltas of `−1`, `−1` and `−2` B reproduced, plus one historical row on this base whose published correction equals the instrument delta exactly.

## T114 — A licence probe keyed on the American spelling `LICENSE` returns a false negative on French-authored repositories, and the detector this base distrusts gets them right 🔴 new at p695

**This is distinct from `T97`.** `T97` says licence *detectors* are monolingual and miss non-English copyright lines. `T114` is the inverse and it lands on this base rather than on GitHub: **the grant's filename is localised, GitHub's detector handles it, and the hand-rolled `raw.githubusercontent.com/<repo>/<branch>/LICENSE` probe — this base's own method — does not.**

**Measured on `30` repositories across the two organisations of the French national ENT, by listing root trees (`git clone --depth 1 --filter=blob:none --no-checkout` + `ls-tree`), not by guessing filenames:**

| Grant filename at root | count | share |
|---|--:|--:|
| `LICENSE` | 24 | 80% |
| 🔴 **`LICENCE`** | **5** | **17%** |
| none | 1 | 3% |

The five: [`edificeio/edifice-mobile-framework`](https://github.com/edificeio/edifice-mobile-framework), [`OPEN-ENT-NG/exercizer`](https://github.com/OPEN-ENT-NG/exercizer), [`OPEN-ENT-NG/presences`](https://github.com/OPEN-ENT-NG/presences), [`OPEN-ENT-NG/competences`](https://github.com/OPEN-ENT-NG/competences), [`OPEN-ENT-NG/magneto`](https://github.com/OPEN-ENT-NG/magneto). **`licence` is the correct spelling in French and in British English; `license` is American.** The sector this base covers is disproportionately public-sector and non-American, which is exactly where the blind spot concentrates — the same regions `T97` already names.

🔴 **The failure is silent and shaped like a finding.** A `404` from the probe is indistinguishable from *no grant file*, and this base's vocabulary for "no grant file" is `unlicensed` — a verdict that **reverses** the commercial answer. Every one of the five is **AGPL-3.0**.

🔴 **It compounds with a second axis, because the default branch is not `main` either.** Across the same `30` root trees, the default ref resolved by `git ls-remote --symref`: `master` **16**, `dev` **7**, `develop` **5**, `main` **2**. **A probe defaulting to `main` reaches `2 / 30` — `6.7%`.** Three of the four branch names in use are ones a habitual probe does not try.

**The worked specimen carries both defects at once** — [`edificeio/edifice-mobile-framework`](https://github.com/edificeio/edifice-mobile-framework), default branch `main`, grant file `LICENCE`:

| probe | result |
|---|---|
| `main/LICENSE` — the habitual shape | 🔴 **`404`** |
| `main/LICENCE` — correct | 🟢 `200` · **2,203 B** · sha256₁₂ `862c9d4f2e98` · bespoke **AGPL-3.0** statement |

🟢 **GitHub's `spdx_id` got all five right.** It reports `NOASSERTION` for this one — which is `T99`'s mechanism (a bespoke grant statement, not canonical text), **not a filename failure**. So on this axis the index this base has learned to distrust outperforms the base's own probe.

**Remedy:** resolve the default branch with `git ls-remote --symref` (never assume `main`), enumerate the root tree rather than guessing filenames, and match `LICEN[CS]E` case-insensitively alongside `COPYING`. **A probe that returns `404` must report "not found by this probe", never `unlicensed`.**

**Confidence: high** — `30` root trees enumerated rather than probed, the false negative reproduced on a named specimen, and the control (GitHub's own field) correct on all five.

## T110 — A `LICENSE` file is not a grant: for an entire language ecosystem it holds only a year and a holder 🔴 new at p694

**The claim.** This base's primary licence instrument is *read the `LICENSE` payload at the real default ref*. **For R packages that returns a file with no licence text in it**, because CRAN's convention is that `DESCRIPTION`'s `License:` field **is** the grant and `LICENSE` carries only the `YEAR` and `COPYRIGHT HOLDER` that the named template interpolates.

**Measured at p694, two for two.** [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr): `LICENSE` = `108 B`, `YEAR: 2020-2022` / `COPYRIGHT HOLDER: UC Berkeley Data Science Education Program` / `ORGANIZATION: copyright holder`; `DESCRIPTION` = `License: BSD_3_clause + file LICENSE`. [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna): `LICENSE` = `46 B`, `YEAR: 2025-2026` / `COPYRIGHT HOLDER: tna authors`; `DESCRIPTION` = `License: MIT + file LICENSE`. **GitHub's API reports `NOASSERTION` for both.**

🔴 **Why this is worse than `T99`'s `NOASSERTION` finding rather than an instance of it.** `NOASSERTION` is *visibly* uninformative — it announces that the detector declined. **A `108 B` `LICENSE` file that returns `200` looks like a successful read.** The instrument reports success and delivers nothing, so the failure is silent, and it fails toward *"ships no licence"* — this base's standard ground for refusal. **It discards permissive assets while appearing to work.**

🔵 **The rule.** For any R-shaped repository (`DESCRIPTION`, `NAMESPACE`, `.Rproj`, `man/`), the grant is `DESCRIPTION`'s `License:` field; a `LICENSE` file under `~200 B` is a CRAN metadata stub and is **not** evidence of absence. 🟢 **And this is not a niche correction: R is the language of statistics, biostatistics, psychometrics and social-science teaching — which is where a large part of education research and assessment actually runs.** Two permissive education rows were recovered by applying it at p694. Generalise before assuming it stops at R: **any ecosystem whose package manifest carries a licence field can put the grant there** — Python's `pyproject.toml`, Node's `package.json`, Rust's `Cargo.toml`, Julia's `Project.toml`.

## T111 — Citation frequency inside a knowledge base measures interest, not usability, and is uncorrelated with the grant 🔴 new at p694

**The claim.** Ranking a backlog by how often the base itself cites an address is an excellent **discovery** heuristic and tells you **nothing** about whether the asset can be used.

**Measured at p694 on the top three.** [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) (`41` citations, `6,905★`) — **AGPL-3.0**. [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (`38`, `2,062★`) — a bespoke **"PageLM Community License"** permitting only *"personal, educational, or non-commercial research"* use, declaring redistribution ***"strictly prohibited"***, and requiring a **revenue-sharing agreement** before any commercial deployment. [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (`37`, **`7,016★`**) — **CC BY-NC 4.0**. **Three of three unusable, for three different reasons, and the latter two both report `NOASSERTION`.**

🔵 **The mechanism, which is why the correlation is absent rather than merely weak.** An address accumulates citations in this base by being *interesting* — large, newly trending, frequently written about, or repeatedly offered up by a search leg. **None of those processes reads the licence.** `cn-math-taxonomy` is the sharpest case: `7,016★`, pushed the same day, a `1,644`-node K-12 knowledge graph that is an almost perfect input to an adaptive-learning engine — **and the one clause that matters forbids exactly the use it would be bought for.**

🟢 **The operational consequence.** Rank by citation to decide **what to verify**; never to decide **what to publish**. At p694 the ranking was `31 %` productive — far better than the `~1 %` search channel (`T109`) — **but the `69 %` it wasted were wasted on assets that looked, by every signal except the grant, like the best things this base had found.**

## T112 — An all-permissive *chain* is worth more than any individual row, and chains are what a deliverable needs 🟢 new at p694

**The claim.** A shelf of `172` permissive foundations is not the same as a **usable path** through a function, because one copyleft link makes the whole delivery copyleft. **Completeness of a chain, not count of rows, is the shelf's real quality metric.**

**Measured at p694.** This base has carried learning-analytics components for hundreds of passes. **Every previous path through the function ran through Anki (AGPL-3.0), `learnhouse` (AGPL-3.0) or `oat-sa/lib-lti1p3-core` (GPL-2.0).** p694 closed one in three links: [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) (**Apache-2.0**, graded verbatim) routes xAPI statements → [`openfun/warren`](https://github.com/openfun/warren) (**MIT**) visualises them → [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) (**MIT**) models the transitions. **No copyleft anywhere in the path.** The same pass closed two more: the credential loop (`euron-open-lms` issues → `learner-credential-wallet` holds, **both MIT**) and the retention half (`py-fsrs`, **MIT**, reaching Anki's own scheduling algorithm **without Anki's AGPL**).

🔵 **Why this reframes what these shelves are for.** Row count has been this base's visible metric for `694` passes. **It is the wrong one.** `py-fsrs` at `524★` and `tna` at `13★` changed what can be *delivered*; several much larger rows did not, because something copyleft already sat in their path. 🟢 **The instruction: when choosing what to verify from the backlog, prefer the address that completes a chain over the address with more stars.** The three chains closed at p694 came from rows of `524★`, `17★`, `13★`, `12★` and `3★`.


## T107 — A discovery probe must name a PRODUCT, not a SUBJECT, or it returns everything that is merely *about* the field 🟢 new at p693

**Evidence.** Three arms over the same language layer, same index, same licence filter:

| arm | probe shape | distinct repositories | real education **systems** |
|---|---|--:|--:|
| p691 | single **subject** noun ×7 (`educacion`, `aprendizaje`, `escolar`, `docente`, …) | `90` | 🔴 **`0`** |
| p693 Arm A | single **subject** noun ×9, `stars:>5` (replication) | `402` | 🔴 **`0`** |
| p693 Arm B | multi-word **product** noun ×16 (`gestão escolar`, `diário de classe`, `boletim escolar`, `avaliação docente`, `secretaria escolar`, `plataforma educativa`) | `473` | 🟢 **`13`**, `9` novel to the whole base |

**Mechanism, which is why this generalises past Spanish and Portuguese.** GitHub free-text search matches **name, description and topics**. A **subject** noun (`educación`, `education`, `aprendizaje`) appears in the description of *anything about the field* — coursework, reading lists, LaTeX dissertation templates, bootcamp exercises, conference talks, and personal **profile READMEs**. A multi-word **product** noun (`gestão escolar` = *school management*, `diário de classe` = *class register*) can only describe a thing that **is** that product. **The subject noun maximises collision; the product-noun phrase minimises it.**

🔴 **The residual, and it never goes to zero:** the collision survives wherever the product noun is **polysemous**. `sistema de notas` returned Markdown note-taking applications, because `notas` in Portuguese is both *grades* and *notes* — the same defect as `currículo` meaning *résumé* (`T105`). **Budget one refusal per polysemous term rather than expecting a clean channel.**

🔵 **Consequence for this base:** two passes concluded the Spanish/Portuguese layer was empty of supply (`p691` measured it, `p692` prescribed re-running the same instrument). **It was not empty; the question was wrong.** And the thing it actually contains is an **administrative** layer, not an agent layer — which is a separate finding that survived the channel correction (`P73`).

**Confidence: high** — three arms, two of them replications, with the collision class named and one instance refused on the record.

## T108 — A Romance-language token selects a language family spanning three continents, so it can narrow a search and can never place a row 🟢 new at p693

**Evidence, at two opposite signs inside one pass.**

🔴 **Sign one — the token points *out* of the region it was used to find.** A probe for `docente`, run to surface LATAM supply, returned [`datomatic/carta-del-docente`](https://github.com/datomatic/carta-del-docente): a PHP integration for **Italy's** *Carta del Docente*, a teacher spending entitlement (🟢 MIT at **`LICENSE.md`** on `main`, `1,099 B`, sha256₁₂ `e340e4990cdb`; README Italian throughout — *"Il pacchetto non ufficiale per integrare facilmente la Carta del Docente in un progetto PHP"*). `docente` is Italian as well as Spanish and Portuguese. **A LATAM-intended probe surfaced an EMEA government integration.**

🔴 **Sign two — the token was already used to place a row, wrongly.** [`Antonio-Neves/Gestao-Escolar`](https://github.com/Antonio-Neves/Gestao-Escolar) was published on this base as **LATAM**, described as *"the most active permissive Portuguese-language school system"*. Its README is **European** Portuguese — *"sectores Académico"* (pt-BR: *setores Acadêmico*), *"base de dados"* (pt-BR: *banco de dados*), the tu-imperative *"considera apoiar"* — and the grant holder is *"**António**"*, the pt-PT spelling. **Withdrawn and re-placed EMEA (Portugal).** A second pt-PT instance ([`ajacs10/AvaliaDocente`](https://github.com/ajacs10/AvaliaDocente): *"anónima"*, *"académico"*, *"recolha"*) was placed EMEA at first filing rather than defaulted to LATAM.

🟢 **The usable discriminator is orthography, not vocabulary.** pt-PT vs pt-BR separate on `sectores`/`setores`, `Académico`/`Acadêmico`, `base de dados`/`banco de dados`, `ficheiro`/`arquivo`, and on `António`/`Antônio` in the grant's own copyright line. ⚠️ **It is an inference, not a registry fact:** `Gestao-Escolar` carries one Brazilian counter-signal (*"arquivo"* ×2), so both rows are placed at **MEDIUM** confidence with the counter-signal stated in-cell, overturnable by one registry fact.

🔵 **Extends `683-B`** (a jurisdiction substring must be checked against the token it sits inside) **from substrings to whole languages**, and it bites hardest exactly where this base's coverage is thinnest.

**Confidence: high** for the rule; **medium** for the two specific placements, and they say so in the cell.

## T109 — This base discovers four to five times faster than it shelves, in every region 🔴 new at p693

**Evidence.** Slugs appearing on a region-bearing line in the two trending files, against rows actually carried on the three sell shelves:

| region | found (trending) | **on no sell shelf** | shelved |
|---|--:|--:|--:|
| LATAM | `163` | 🔴 **`140`** | `20` |
| North America | `195` | 🔴 `149` | `23` |
| EMEA | `312` | 🔴 `257` | `32` |
| APAC | `327` | 🔴 `279` | `37` |
| **total** | `997` | 🔴 **`825`** | `112` of `440` rows |

🔴 **Why it matters more than any single discovery.** A trending file is a **log**; a sell shelf is what a studio reads when an engagement starts. **825 region-labelled addresses have been found, licence-read, written up and left where nobody selling an engagement will see them.** For six consecutive passes this base declared LATAM supply *nil* and prescribed more discovery, while holding `163` LATAM addresses in its own logs. **The bottleneck was never discovery.**

⚠️ **Upper bound by construction, and the error direction is known.** Co-occurrence on a line is not a placement, so slugs sharing a line with a region name are counted (`huggingface/transformers` and `carpentries/instructor-training` sit inside the `163`). **The measurement can only overstate the backlog — but not the ratio's direction**, which is consistent across all four regions and robust to the noise. 🔴 **`2` of the `163` are not addresses at all** (`topics/ai-tutor`, `topics/education-ai`), which is **`Gap 248` still live in these files, `28` passes after declaration**.

🔵 **This is `Gap 247`'s `QUEUE-UNENUMERATED` (recorded at `104`) measured at its true scale, and the remedy is already written:** before any pass writes the word *"filed"*, `grep` the slug against the sell shelves — and **spend part of every pass promoting the backlog rather than extending it.** p693 promoted `9`.

**Confidence: high** on the ratio and its direction; the absolute backlog is an explicit upper bound.


## T102 — A zero from a search index has two causes, and only one of them is a finding

🔴 **Discovery nils are the most-published result on these shelves, which makes a false nil the most expensive defect available.** `p690` (`690-C`) found zeros that were **transport** failures: six of ten queries returned `total_count: 0` and the run read as a clean nil across six categories until it was re-probed. `p691` found the complementary class on the same channel — zeros that were **query-construction** failures. Five Spanish/Portuguese probes (`educacion ia tutor`, `educación inteligencia artificial`, `educacao ia professor`, `tutor inteligente educacion`, `plataforma educativa ia`) each returned `total_count: 0`. Nothing was wrong with the channel: free-text `machine learning` returned `1,320,779` and `education` returned `284,220` in the same session. **The queries were `3`-way conjunctions**, and GitHub ANDs free-text terms, so each was asking for three strings in one repository's indexed fields. Decomposed to single terms the same channel answered at once: `educacion` `8`, `aprendizaje` `37`, `educacao` `15`.

🔵 **The two causes are indistinguishable at the call site** — both are `{"total_count": 0, "items": []}` — and both are shaped exactly like a finding, which is why neither can be published without a test. **Procedure: a `total_count: 0` becomes a nil only after (1) a known-positive control on the same channel in the same session, and (2) decomposition of every multi-term conjunction into single terms.** A zero from an over-constrained AND is a statement about the conjunction, never about the supply.

🟡 **Why this matters beyond method:** both failure modes bite hardest on the legs that probe **under-covered regions**, because those are the legs whose queries carry the most terms (a language word *plus* a domain word *plus* a role word) and whose true results are smallest. A region that is genuinely thin and a region that was mis-probed produce the same output, and the base will cheerfully publish the mis-probe as regional intelligence. **`p691`'s LATAM supply figure survived only because the zero was tested rather than written down.**

## T103 — A two-column fact sheet is indistinguishable from a leaked header to anything that reads column 1 as a name

🔴 **The brief's sharpest data-quality rule is that a header row must never survive as data — a row reading `| Nombre | Repo | Licencia |` has compiled into an entity literally named *"nombre"* more than once, across several industries.** `p691` swept all eight education shelves for that defect and found **`0` instances**. What it did find is a second route to the same corrupted entity, and this one is produced by **correct** authoring.

`71` rows across `agents/trending.md` (`37`), `repos/trending.md` (`33`) and `intel/market.md` (`1`) have a header-like token in column 1 and are **not** followed by a `|---|` separator. All `71` were read. All `71` are legitimate **two-column fact sheets**, a format this base uses deliberately and consistently for per-artefact dossiers: `| Region | **LATAM** — the artefact *is* a national curriculum standard … |`, `| Stars | 🔴 **UNMEASURABLE** (`mcp-unindexed`, `curl-403`) — not `0` … |`.

🟡 **The risk is real even though the authoring is right.** A compiler that takes column 1 of a two-column table as the entity name turns these rows into entities named `region`, `licence` and `stars` — the brief's exact failure mode, reached without a single misplaced header. 🔵 **The discriminator is structural and cheap: a record-oriented table declares itself with a `|---|` separator under a header row.** A two-column block with no separator is a dossier, and its column 1 is a *field label*, not a subject. **The fix belongs in the compiler, not in the `71` rows** — two of the three files holding them are append-only, so "repairing" a well-formed dossier would mean rewriting trend history to satisfy a reader that mis-parses it.


## T99 — `NOASSERTION` is a fact about the detector, not about the grant — and in education it lands hardest on public-sector Europe 🟢 new at p690

`p690` cross-checked **every** repository this base shelves — `339` subjects across [`agents/top.md`](../agents/top.md), [`repos/foundations.md`](../repos/foundations.md) and [`verticals/solutions.md`](../verticals/solutions.md) — against GitHub's own `license.spdx_id`. **`44` diverged from what this base holds. `0` of the `44` were errors in this base.** Every one is GitHub's `licensee` declining to classify a grant that demonstrably exists, and the `44` sort into **five** reproducible modes:

| Mode | What the payload actually is | Named cases |
|---|---|---|
| **1. Detector blind to EUPL** | Short, reference-style EUPL grant | **`11`** `Opetushallitus` repos — `koski` `653 B` EUPL-**1.1**-or-later, `ataru` `296 B` EUPL-**1.2**-or-later |
| **2. MIT + appended provenance clause** | MIT verbatim plus an attribution paragraph for derived portions | `brightspace-d2l-mcp` `1,200 B`, `teach-skill` `1,234 B` |
| **3. Apache-2.0 with appendix filled or prefix added** | Boilerplate replaced by real copyright, or project name prefixed | `feedbacksystem` `10,785 B` (`dev`), **`apache/openmeetings` `50,907 B`**, `rasbt/LLMs-from-scratch` `11,505 B` |
| **4. Genuinely split grant** | Several licences in one file; no single SPDX id is correct | `evaluators` `1,615 B` (MIT + CC-BY-4.0 + **CC-BY-NC-SA-4.0** ×2), `student-dropout-early-warning` (MIT + CC-BY-4.0 data), `code-dot-org` (Apache-2.0 + enumerated proprietary artwork) |
| **5. Grant off-root or manifest-only** | Nothing at the root for a scanner to read | `openSIS-Classic` → `docs/License.txt` `17,286 B`; `kolibri-design-system` → `package.json` field only, `404` on five filenames across three branches |

🔵 **The sharpest single proof that `NOASSERTION` describes the tool:** **the Apache Software Foundation's own `openmeetings` repository reads as unlicensed to GitHub.** Its `LICENSE` is `50,907 B` because it is prefixed `Apache OpenMeetings License:` and has bundled third-party grants appended.

🔴 **Mode 1 is the one with money attached, and it is an EMEA finding.** The EUPL is the licence European public bodies publish under. A client's software-composition-analysis gate does not report *copyleft — price it*; it reports **`unknown licence`**, and `unknown` cannot be risk-assessed, so the review stops. 🟢 **Three sellable things follow, none of which require building an agent:** a licence attestation resolving every `unknown` to a named family with payload evidence; the EUPL reciprocity boundary priced correctly (its *Distribution or Communication* definition reaches network availability, so it is **not** GPL's boundary); and the **version split**, since EUPL-1.1 and EUPL-1.2 are different instruments and this shelf carries both. 🔵 **`T22` said licence form and licence hygiene are independent variables. `T99` adds the third: licence *detectability*, which is independent of both and is the one the client's tooling actually reports.**

## T100 — A search index is authoritative when it answers and silent when it fails, and the two are the same shape 🟢 new at p690

`p690` used `gh api search/repositories` as its verification channel, because `gh api repos/{owner}/{repo}` answers **`403 GitHub access to this repository is not enabled for this session`** for anything outside the session grant while `search/*` stays open. The channel is excellent — `stargazers_count` and `license.spdx_id` for arbitrary public repositories, `15` subjects per call via ORed `repo:` qualifiers. 🔴 **It also fails in two distinct ways that both look exactly like a nil.**

🔴 **Failure 1 — the persistent index gap.** `5` shelved repositories return `total_count: 0` and are **ALIVE** under `git ls-remote --symref`: [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents), [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor), [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library), [`theopenem/oneroster.net`](https://github.com/theopenem/oneroster.net), [`thc1006/moodle-mcp`](https://github.com/thc1006/moodle-mcp). Re-probed individually; still `0`. 🔵 **`mitodl/open-learning-ai-tutor` was promoted onto the shelf at `p688`** — a pass that trusted the index would have deleted a row it had just filed. **Liveness comes from `git ls-remote`; a search miss is never grounds to retire a row.**

🔴 **Failure 2 — the silent transient zero.** Six of ten queries in this pass's first harvest returned `0` and looked like a clean nil across six categories. Controls say otherwise: `AI grading assessment stars:>60 pushed:>2026-08-15` → `0`, while `AI grading assessment` → **`650`**; `autograder AI stars:>60` → `0`, while `autograder stars:>60` → **`6`** and `autograder` → **`2,437`**.

🔵 **This is the `T92` class again** — the trend that named `curl -sSL` without `--fail` turning a `404` into a `14`-byte document. Same defect at a different layer: **the probe's failure is indistinguishable from the answer it is probing for**, so an unguarded run converts tooling trouble into a confident claim about the world. 🟢 **The guard this pass adopted and which every later pass should keep:** `3` retries per query, a bare-term control for any `0`, and a surviving `0` logged as **`UNCONFIRMED`** rather than as an absence. One query survived all three retries (`lesson plan generator stars:>40`) and is on the record as unconfirmed, not as a nil.

## T101 — The permissive education-agent supply is saturated at the keyword layer, and the remaining discovery channel is institutional 🟢 new at p690

`p690` ran `22` discovery queries (star floors `40`–`200`, push floors from `2026-08-01`, plus `topic:ai-in-education` and `topic:ai-tutor`), harvested **`131`** unique repositories, and diffed them against **every** slug this base holds anywhere — `5,434` distinct `owner/name` pairs. 🔴 **`27` were novel. `0` were filable.**

The novel tail is `0`–`3★` coursework and conference artefacts (`aied2026-es-llms` `2★`, `stage-aware-AI-tutor` `2★`, `Academic-Instability-Early-Warning-System` `2★`, `learner_agency_simulator` `0★`). The two largest permissive novelties are **not education agents** and were refused on substance: `flashcards/flashcards.github.io` (MIT, `185★`, developer flashcards) and `dcavar/python-tutorial-notebooks` (Apache-2.0, `166★`, NLP teaching notebooks).

🔴 **The CJK discovery leg is actively contaminated, and the contamination outranks the signal.** `教育 AI agent stars:>100` returns, above every education repository, [`cirosantilli/china-dictatorship`](https://github.com/cirosantilli/china-dictatorship) (`3,323★`) and **three** near-duplicate mirrors (`385★`, `215★`, `132★`) — political-speech archives that rank for Chinese-language queries on README mass alone. 🔵 **`p669` already established that a repository's own files, not an owner's metadata, decide a region.** `T101` extends that from *placement* to *discovery*: **a CJK keyword query against this index is not a CJK education channel.**

🟢 **The constructive half, and it is the actionable one.** At `84` rows with a `≥40★` floor, the keyword layer is exhausted — but this base's best recent rows did not come from keywords. `p670` found `DaRL-GenAI` by **enumerating an owner account** (`gh api search/repositories -f q='user:DaRL-GenAI'`); `p676` promoted three American university systems off this base's own backlog; `p688` promoted `mitodl/open-learning-ai-tutor` after `24` prior mentions in [`agents/trending.md`](../agents/trending.md). 🔵 **The next real row will come from owner enumeration, a named institution, or this base's own mention backlog — and `T101` is the measurement that says to stop spending passes on star-ranked keyword legs.**

## T96 — The most-cited open-source education artefacts are disproportionately ungranted, and star count is anti-correlated with legal usability

**Evidence:** `50` of the most-mentioned repository slugs in this base's own append-only logs were graded at p689 — permissive and copyleft verdicts by reading the root grant payload at the real default ref, absence verdicts by **enumerating the tree** (treeless partial clone) **and reading the manifests**, per `ACTION p275`/`p276`. Ledger: [`evidence/p689-backlog-licence-ledger.tsv`](../evidence/p689-backlog-licence-ledger.tsv); enumerator: [`ingest/p689-enumerate.sh`](../ingest/p689-enumerate.sh).

| verdict | n | share |
|---|--:|--:|
| 🟢 permissive (MIT / Apache-2.0 / BSD) | 27 | `54.0 %` |
| 🟡 copyleft (AGPL / GPL / LGPL) | 7 | `14.0 %` |
| 🔴 restricted — reads open, is not | 6 | `12.0 %` |
| 🔴 **verified grant-absent** (tree + manifest both empty) | 5 | `10.0 %` |
| 🟠 **unresolved** (a grant exists, but not as a root payload) | 5 | `10.0 %` |

🔴 **The single most-starred AI tutor in open source has no grant anywhere.** [`jushbjj/mr.-ranedeer-ai-tutor`](https://github.com/jushbjj/mr.-ranedeer-ai-tutor) — **`29,540★`** — has `12` files in its enumerated tree, none a licence, and no manifest. [`adlnet/scorm-to-xapi-wrapper`](https://github.com/adlnet/scorm-to-xapi-wrapper) is the same shape and worse as a signal: **ADL authored SCORM and xAPI and did not licence their own wrapper.** And the *most-cited* slug in these logs, [`caviraoss/pagelm`](https://github.com/caviraoss/pagelm) at `34` citations, serves a bespoke **"PageLM Community License"**.

**Confidence: high** on the five enumerated absences and on all `40` payload-read verdicts. 🔧 **Medium, and explicitly downgraded, on the prevalence figure — because p689's own first measurement of it was wrong by 2×.** The draft graded absence from a ladder of candidate root filenames; `gate-enumeration` refused the commit, and a compliant re-run turned `10` claimed absences into `5`. **A prevalence measured on `50` slugs by one method, once, is an indication.**

🔵 **Why it is a trend and not a list.** Prompt-shaped and skill-shaped artefacts — the fastest-growing class in this sector — are published as *content* by authors who never expected a licence question, while the infrastructure layer (LMS, LRS, interop, modelling libraries) is published as *software* by people who did. So the sector's most visible artefacts are among its least usable, and **the more an artefact is shared, the less likely it is to carry a grant you can read.**

🟢 **Three operational rules for a studio, each one earned by a specimen above.** (1) **Screen on the grant before the star count.** (2) **Read the file, don't trust the field** — GitHub's licence field is `null` on all five enumerated absences, and on [`portabilis/i-diario`](https://github.com/portabilis/i-diario) it reads `NOASSERTION` for a perfectly valid AGPL that happens to be in Portuguese (T97). (3) 🔴 **Enumerate the tree and read the manifest before you call anything unlicensed** — `dmontgomery40/mcp-canvas-lms` declares `"license": "MIT"` in `package.json` while shipping no licence file, and `learnpress/learnpress` declares `ISC` in one manifest and `GPL-3.0-or-later` in another. **"Declared but not delivered" and "two incompatible grants" are both common, and neither is visible to a filename probe.**

## T97 — Licence detectors are monolingual, and the blind spot lands on the regions this sector keeps calling underserved

**Evidence:** [`portabilis/i-diario`](https://github.com/portabilis/i-diario) serves a complete, valid AGPL-3.0 as **`LICENÇA PÚBLICA GERAL AFFERO GNU`** — `35,325 B`, `sha256₁₂ 837b5cf19787`, at default ref `1.6`. **GitHub's licence field reads `NOASSERTION`. This base's own grader read `OTHER:`.** Both key on English title lines. p689 read the first five lines by hand and graded it correctly.

**Confidence: high** for the specimen and the mechanism; **medium** for the prevalence, which p689 did not sweep.

🔵 **Why it matters beyond one row.** Every automated supply-side census in this sector — including this base's, for `688` passes — filters on a licence field or an English-keyed grader. A Brazilian, Mexican, Indonesian or Vietnamese project that translates its grant therefore reads as *unlicensed* to the instrument and drops out of the census. 🔴 **An absence measured with a monolingual detector is partly a measurement of the detector**, and this base has published LATAM thinness repeatedly while carrying this bug. The fix is one title line per language. The finding is that `689` passes went by before anyone opened a licence file in another language.

## T98 — The structural weakness of LLM tutoring has an eleven-year-old answer, and it is Apache-2.0

**Evidence:** [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) — Apache-2.0 (`LICENSE.txt`, `11,558 B`, `sha256₁₂ 49bbe9114e49`), `28★`, `14` forks, born `2015-10-08`, **still pushed `2026-09-05`** — a joint project of the Open University of the Netherlands and Utrecht University. It builds **domain reasoners**: components that *compute* the next correct step and the feedback for a wrong one, for mathematics, linear algebra, logic, Haskell (the *Ask-Elle* tutor) and communication skills.

**Confidence: high** on the artefact; **medium** on the adoption thesis, which is p689's reading rather than a measured market move.

🔵 **The weakness it addresses is the one every row on `../agents/top.md` shares: an LLM tutor cannot be sure its hint is correct.** This base's shelves hold `84` agent addresses and not one of them can certify a step. A domain reasoner can, for the domains it covers — and it narrows what the model is trusted with to language and dialogue, which is what models are actually good at. 🟢 **Under EU AI Act Annex III a deployer must be able to explain an output: a generated hint cannot be explained, a computed one traces to the rule that produced it.** 🔴 **The honest caveat: `28★` and Haskell.** This is a correctness asset for a client with a correctness bar, not a mass-market component — and the coverage is per-domain, so anything outside the shipped reasoners is new work. Composition recipe: `../compose/patterns.md` `P67`.

## T94 — The state-operated school AI platform has arrived, it is open source, and it is AGPL

Every school-facing AI platform this base has tracked until now was either a vendor product or a project. **Germany is running one as public infrastructure, in the open:** [`FWU-DE/ais-chat`](https://github.com/FWU-DE/ais-chat) — `AIS.chat`, formerly `telli` — a **DigitalPakt Schule** sub-project of **AIS** (*Adaptives Intelligentes System*), developed openly since **November 2024**, coordinated by the **FWU** on behalf of **all 16 Bundesländer**, with **12 states live as of 09/2026** on secondary reporting.

**Three consequences, in order of commercial weight:**

1. 🔴 **The grant is AGPL-3.0** (`34,523 B`, sha256₁₂ `8486a10c4393`, byte-read). Network use is distribution: a hosted, state-branded fork owes modified source to teachers and pupils. **This is the first time this base has had to say that about a platform a client would *operate* rather than install.** It redirects the motion from forking to integration across a licence boundary.
2. 🔵 **Adoption is not measurable in stars.** `27★` on a platform serving twelve federal states. Any shelf or scoring model that ranks education software by stars will rank public infrastructure near zero — and this base's own `agents/top.md` star column is exactly such a model. Read the star column as *developer* adoption, never as deployment.
3. 🔴 **It was renamed mid-life, and the rename defeated retrieval.** `telli` → `AIS.chat`, **May 2026, trademark reasons**. This base held neither string. The literature indexes the old name; the repository carries the new one. **A product rename is a retrieval failure mode with no current guard**, and the fix is cheap: when a leg returns a renamed artefact, record *both* strings in the cell.

**Confidence: high on the repository and its grant** (read first-hand, `gh api` agrees). **Medium on reach** — the 12-of-16 count and the per-state list are from German education-press and state-portal sources, not from a federal register.

## T95 — Human-in-the-loop is becoming a property of the tool surface, not a sentence in the policy

The sector's governance documents all promise human oversight of AI assessment. [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) (**MIT**) is the first address this base has found where the promise is **structural**:

- the tool list is partitioned — `12` read-only, `4` local-only, **`3` that write to Canvas**;
- the three writers (`post_staged_grades`, `post_comment`, `add_gradebook_note`) **each require `confirm=true`**;
- proposed grades are **staged on the grader's own disk** until that second act;
- **anonymous and moderated assignments are read-only by construction.**

🔵 **Why this is a trend and not a feature.** The EU AI Act's Annex III names *evaluation of learning outcomes* as high risk, and its deployer duties — like the US state guidance this base tracks — are discharged by evidence that a human decided. **A tool that cannot post without a second human act produces that evidence as a by-product of working.** Compare the alternative already on this shelf: [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT) grades directly. Same licence, same LMS, opposite conformity posture.

🔴 **The counter-reading, stated because it will come up in a client room:** the same README is explicit that student work still reaches the model behind the client, and names FERPA. **Confirmation gating is an *authority* control, not a *data* control** — it decides who decides, not where the data goes. A conformity story needs both, and the second half is a hosting decision, not a tool choice. See [`../compose/patterns.md`](../compose/patterns.md) **P64**.


## T91 — An Apache-2.0 payload's byte count is not its identity, and this pass measured five of them
*Added p687. Confidence: **high** — five payloads read first-hand the same day, every size and digest reproduced.*

This base already records (**T56**) that `11,357` and `11,358` are two different Apache-2.0 canonicals and that size alone cannot tell them apart. p687 shows the ambiguity is not a pair — it is a **sliding window**, and the window now has five measured positions:

| bytes | sha256₁₂ | what it is | API `license` field |
|--:|---|---|---|
| `10,172` | `59899c6091b5` | canonical, clause 4(a) wrapped one way — `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 🟢 `Apache-2.0` |
| `10,173` | `c4a2cd14eb3a` | **same licence text**, clause 4(a) wrapped the other way — `learning-commons-org/agent-skills` | 🟢 `Apache-2.0` |
| `11,356` | `f1a2e5fccede` | canonical with the appendix placeholder **filled on one line** — `122-syf-wcy/PhysicsOS` | 🟢 `Apache-2.0` |
| `11,356` | `43070e2d4e53` | 🔴 **the `11,357` canonical with its trailing newline stripped by a shell capture** — a measurement error, not a payload | — |
| `11,357` | `c71d239df917` | the `apache/.github` canonical — `ably-labs/realtime-quiz-framework`, `THU-MAIC/MAIC-Core` | 🟢 `Apache-2.0` |
| `11,505` | `4b6615cdb446` | canonical with the appendix **block replaced** by a completed notice — `rasbt/LLMs-from-scratch` | 🔴 **`NOASSERTION`** |

Three results follow, and the third is the expensive one.

**(1) The `10,172`/`10,173` byte is a line re-wrap, not a licence difference.** `diff` gives one changed pair inside clause 4(a): `"…of the Work or / Derivative Works…"` against `"…of the Work or Derivative / Works…"`. Two legitimate upstream reflows of identical terms.

**(2) `11,356` is occupied twice, by a real payload and by an error.** `122-syf-wcy/PhysicsOS` genuinely measures `11,356 B` because filling `Copyright [yyyy] [name of copyright owner]` → `Copyright (c) 2026 PhysicsOS contributors` is one character shorter. And `printf '%s' "$(cat canonical)" | wc -c` → `11356` for the `11,357` canonical, because a shell capture strips the trailing newline — the defect p674 proved on `Opetushallitus/compleap`. **A cell reading `11,356 B` without a digest cannot say which of the two it saw.** Write the payload to a file and hash the file; never measure through `$(...)`.

**(3) 🔴 Filling the appendix can cost you the licence field, and the threshold is how much canonical text survives.** `PhysicsOS` filled **one line** and still matches `Apache-2.0`. `rasbt/LLMs-from-scratch` replaced **the whole appendix block** with a real notice (`Copyright 2023-2026 Sebastian Raschka` plus the completed *"Licensed under the Apache License…"* paragraph), `+148 B`, and the SPDX matcher stops recognising it — so **`gh api` reports `NOASSERTION` on a verbatim Apache-2.0 grant held by a `107,940★` repository.** A licence filter over the API field drops the highest-starred repository on this base's foundations shelf. **The remedy is not a better filter; it is reading the payload.** Consistent with p686's finding that `NOASSERTION` carries no information, now with the *mechanism* named rather than just the spread.

## T92 — `curl -sSL` without `--fail` makes a 404 into a 14-byte document, and this pass measured its own probe doing it
*Added p687. Confidence: **high** — caught in p687's own instrument, with the artefact reproduced.*

p687 measured README language shares to place regions. For `SafeExamBrowser/seb-server` the probe reported **"README `14 B`, CJK `0`"**. There is no `README.md` in that repository — the document is `README.rst`. `curl -sSL` returned GitHub's `404` body, the literal bytes `404: Not Found`, **with exit status `0`**, and the measurement was computed over that string.

🔴 **A 14-byte README is not a terse README; it is the absence of one, wearing the shape of data.** Every pipeline in this base that reads a URL into a buffer and then measures the buffer is exposed: CJK share, title-line grading, byte counts, digests. A digest of `404: Not Found` is a perfectly stable, perfectly reproducible, perfectly wrong digest — and it is the *same* digest (`d5558cd419c8`) on every repository that lacks the file, so it will even cross-validate against itself.

**Rule:** `curl --fail --silent --show-error --location`, check the HTTP status explicitly, and treat any payload under ~`64 B` as a probe failure to be investigated rather than a value to be recorded. 🔵 This is the same class as **T56** and **T91(2)**: in all three, the instrument produced a number that was internally consistent and described bytes the repository does not serve.

## T93 — The mandated search legs report this sector late, and the lag is now quantified at `-19.4%`
*Added p687. Confidence: **medium-high** — two first-hand comparisons, one of them large; the direction is structural, the magnitude is a sample of two.*

This base has recorded `29` consecutive passes in which the eight mandated legs produced no new address. The standing interpretation has been that the legs are saturated. p687 adds a second, sharper reading: **the legs are not just saturated, they are stale, and the staleness is measurable.**

| subject | figure the leg returned | first-hand, same week | error |
|---|--:|--:|--:|
| `HKUDS/DeepTutor` | `45,224★` (October roundup) | **`56,080★`** | 🔴 **−19.4%** |
| `THU-MAIC/OpenMAIC` | *"about 42K★"* | **`42,851★`** | ≈ −2% |

The mechanism is not error, it is **latency**: a roundup's number is frozen at publication while the repository keeps moving, and the search channel surfaces roundups in preference to repositories. The bias is therefore **one-directional** — always low, never high — which is exactly what a filter tuned on adoption thresholds will mis-rank.

🔵 **Two consequences for how this base should be read.** First, a nil streak on these legs is evidence about the *channel*, not about the sector: `DeepTutor` added `~10,800★` in the window the legs described as quiet. Second, any star figure this base publishes must name whether it is first-hand or cited, because the two are not the same kind of number — which is why every star cell added at p687 states the ref and date it was read at.

## T1 — The agentic classroom arrives, and it simulates peers

The year's structural shift is from *tutor* to *classroom*. OpenMAIC (Tsinghua, MIT, **42.7k ★**, v1.4.0 released 2026-11-04) generates a full lesson from a topic or document and staffs it with AI teachers **and AI classmates** that speak, draw on a shared whiteboard and argue with each other. DeepTutor (HKU, Apache-2.0, **55.0k ★**) holds the one-to-one position with a persistent learner model.

Together these two repositories hold ~98k stars — more adoption than every other open source education project combined. **Confidence: high** (both verified first-hand this pass).

**Why peer simulation matters:** a one-to-one tutor cannot produce disagreement, and disagreement is where a good deal of learning happens. This is a genuinely new capability, not an incremental one.

## T2 — The reference stack is MCP + LangGraph

OpenMAIC orchestrates with LangGraph. `canvas-mcp` (MIT, 317★) exposes ~102–128 LMS tools over the Model Context Protocol, and `tutor-mcp` packages Bayesian Knowledge Tracing itself as an MCP server. Bloom (MIT, 302★) ships as a Claude Code skill *and* a web app.

The pattern has settled: **pedagogy in MCP servers, orchestration in LangGraph, the LMS left untouched.** That is good news for licence containment (see T6). **Confidence: high.**

## T3 — Usage has outrun governance, and governance is now the buying trigger

86% of education organisations use generative AI and most have no policy. 54% of K-12 students and 92% of university students use AI. In LATAM, >50% of teachers in Chile and Brazil use AI tools while <10% of institutions have formal guidelines (UNESCO).

The consequence for sellers: in 2026 the thing a client lacks is usually **control**, not capability. Governance frameworks, audit trails and policy enforcement are the wedge; the tutor is what gets bought afterwards. **Confidence: high.**

## T4 — Agent deployment is still rare, which is where the work is

The Bridges 2026 survey of K-12 and college leaders found relatively few institutions running agents in daily operations, with leaders explicitly unwilling to give agents access to sensitive student data. Pilots exist for tutoring and enrolment.

The gap between chatbot adoption (near-universal) and agent deployment (rare) is precisely the systems-integration gap. The blocker named by buyers is **data access governance**, not model quality. **Confidence: high** (survey-based).

## T5 — One LATAM deployment is the proof point the industry lacked

A Chilean university reported **194 pedagogical agents across ~100 courses serving 4,600+ students** (February 2026). This is the largest concrete agentic-education deployment surfaced anywhere in this pass — and it is in LATAM, not North America or Europe.

**Confidence: medium** (single secondary source, institution unnamed in the reporting). Worth verifying directly; if it holds, it is the strongest reference case available for the region.

## T6 — The institutional LMS is no longer copyleft-only: there is an Apache-2.0 platform, and it has the LLM layer in-tree

🔴 **This entry has now been wrong twice and is being rewritten a second time. Both earlier versions are withdrawn.**

| Pass | What this entry claimed | Why it failed |
|---|---|---|
| ≤ p650 | "Open source education has no permissive platform, only permissive components" | `learningequality/kolibri` is MIT, 1.2k ★, a production offline-first platform |
| p651–p652 | "No permissive platform **of the Moodle / Open edX class**" — i.e. institutional course management | `OpenOLAT/OpenOLAT` is **Apache-2.0**, 449 ★ / 167 forks / **32,210 commits**, and is institutional course management: courses, enrolment, assessment, QTI testing, portfolio, curriculum management |

**The current claim, and this one is a count rather than a generalisation.** Across fifteen platform rows: **ten copyleft** (GPL-3.0: Moodle, Chamilo, ILIAS, Gibbon; AGPL-3.0: Open edX, Frappe LMS, Veo; GPL-2.0: RosarioSIS, openSIS; LGPL-3.0: OpenEduCat) and **five permissive** (Apache-2.0: **OpenOlat**; MIT: Kolibri, Richie, GegoK12; ECL-2.0: Sakai). One of those five is in the institutional class. The licence-only objection to a permissive institutional deliverable is gone.

🟢 **And the part that matters more than the licence:** OpenOlat ships `langchain4j` 1.23.0 (Apache-2.0) in `pom.xml` with the OpenAI, Anthropic and **embeddings** modules, plus Apache Lucene. Read at first hand from the manifest on 2026-11-04. Because `langchain4j-open-ai` speaks the OpenAI-compatible wire protocol that Ollama and vLLM both serve, **an in-jurisdiction no-egress deployment is a configuration change, not a fork** — which is exactly the architecture EMEA public education keeps asking for.

🔵 **The methodological finding, which generalises past education.** This base missed OpenOlat for seven consecutive passes because every pass ranked the platform shelf by stars. OpenOlat's star:commit ratio is **1:72**. A star-ordered channel buries a 32,000-commit university LMS beneath tutorial repositories — and this base had already written down the reason (it notes that Moodle has *more forks than stars*, "a codebase institutions take copies of, not a project people watch") without applying it to its own instrument. **Institutional software is under-starred by construction. For the platform shelf, rank by licence or by commit depth; a star floor is the wrong tool.** The row came back from one licence-first query.

**What has *not* changed, and still governs most engagements:** the LMS a client *already runs* is almost always copyleft — Moodle and Chamilo across LATAM and EMEA K-12, Canvas and Blackboard across North America. Stock-platform-plus-out-of-tree-agent remains the common case. What changed is the **greenfield** choice.

## T7 — The EU's high-risk deadline moved to December 2027, and most guidance is stale

The Digital Omnibus (Regulation (EU) 2026/1744) deferred high-risk obligations for stand-alone education AI from 2 August 2026 to **2 December 2027**. Article 50 transparency duties still apply from 2 August 2026. Emotion recognition in schools has been banned since February 2025. Article 4's AI-literacy duty was softened to "taking measures".

**Most published guidance still cites August 2026 and is wrong.** That is itself a commercial opening: clients working from stale advice are either over-panicking or mis-scoped. **Confidence: medium** — multiple secondary sources agree, but Commission primary text was not read this pass. Verify before quoting to a client.

## T8 — Regulation is diverging by region, not converging

| Region | Shape |
|---|---|
| EMEA | Horizontal, binding, risk-tiered, dated |
| North America | Sub-national patchwork: 134+ bills across 31 states |
| APAC | Service-by-service (China), labelling-first (India), voluntary (Japan) |
| LATAM | Largely pending; only Peru enacted |

A single global compliance posture is no longer achievable. Multi-region clients need per-jurisdiction policy nodes in the agent itself — a concrete architectural requirement, not a legal footnote. **Confidence: high.**

## T9 — Knowledge tracing is still research-grade, not productised

pyKT (MIT) is the field's reference implementation at **457 stars** — not the 1.2k this KB previously published. OATutor (MIT, 276★) is the main production-grade BKT system.

🔴 **One piece of evidence in this entry is withdrawn.** It previously read "`tutor-mcp` packages BKT as an MCP server but has **0 stars**". That measured `kvnloo/tutor-mcp`, which the repository page states is a **fork**; the upstream `ArnaudGuiovanna/tutor-mcp` has **96 ★ / 13 forks** and packages BKT *and* FSRS spaced repetition behind one MCP tool surface. The broader claim stands on pyKT (457★) and OATutor (276★); the 0-star datum does not.

The honest read: knowledge tracing is scientifically mature and commercially immature. Budget real integration effort; do not promise adaptive mastery modelling as an off-the-shelf component. **Confidence: high** (star counts measured directly) — but see **T13**, because the adjacent problem of *review scheduling* has an answer that knowledge tracing does not.

## T10 — The evidence base remains the sector's weak point

A July 2026 scoping review of **474 studies** found the field fragmented, with pedagogical design poorly connected to technical capability. A 2025 study found AI tutors adapt worse in real time than human tutors, following predictable response patterns.

Sophisticated buyers know this, which is why 2026 procurement favours measured pilots. **Ship with measurement attached** — pre/post assessment, retention tracking, teacher time saved. An engagement that cannot show an effect will not renew. **Confidence: high.**

## T11 — Public support for banning AI in schools is rising in parts of APAC

Ipsos Education Monitor 2026, support for a ban: South Korea 31%, Japan 29% (**up from 21%**), Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%; Australia and New Zealand higher still.

Roughly a quarter to a third of the public in major APAC markets would ban AI in schools outright. Visible, teacher-in-the-loop designs are the commercially safer posture there. **Confidence: high** (single reputable polling source).

## T12 — Binding, education-specific AI regulation is no longer only a European phenomenon

**South Korea's AI Basic Act (Law No. 20676) has been in force since 22 January 2026**, and its "high-impact AI" definition names **AI used for student assessment in early-childhood, elementary and secondary education**. Operators must determine whether their system qualifies before deployment and must make efforts to assess its impact on fundamental rights beforehand. MSIT has signalled a grace period of at least one year before administrative fines, putting the enforcement edge around **January 2027** — *earlier* than the EU's deferred high-risk date of 2 December 2027. Vietnam's Law on AI has been in force since 1 March 2026.

**Why this matters more than a second data point:** until this pass, "conformity by design" was an EMEA offer and APAC was characterised as service-specific, labelling-first and voluntary. That characterisation is now incomplete. The same engagement shape — risk classification, documentation, human oversight, impact assessment on the assessment and placement use cases — is sellable in two jurisdictions against two dates, and the Asian one lands first. A client operating in both needs **one conformity programme with two jurisdictional profiles**, which is a larger and more defensible engagement than either alone.

**Confidence: high** on the statute, its date and the education clause (multiple independent legal-practice sources and the official text's definition agree). **Medium** on the grace-period length, which is reported as "at least one year" and should be confirmed with MSIT before being relied on contractually.

## T13 — Spaced repetition is the one permissive education algorithm that is already in production

The pattern across this KB has been permissive-but-research-grade (pyKT, 457★) or adopted-but-copyleft (every institutional platform). **FSRS breaks it in both directions at once.**

| | Reading |
|---|---|
| `open-spaced-repetition/fsrs4anki` | **MIT**, 4.1k ★ — scheduler plus an optimiser that machine-learns parameters from a learner's own review history |
| `open-spaced-repetition/fsrs-rs` | **BSD-3-Clause**, 456 ★ — the embeddable Rust engine; bindings for C, Python, Node.js, Dart, PHP |
| Adoption | **The algorithm ships inside Anki itself from v23.10** — mainstream production software, consumer scale, not awaiting integration |

Knowledge tracing answers *"does this learner know X?"*. FSRS answers *"when should this learner see X again?"* — and the second question is the one that drives retention, which is the outcome institutions actually measure. The two are complementary, and `ArnaudGuiovanna/tutor-mcp` (MIT, 96★) already exposes both behind one MCP tool surface.

**Why it is commercially interesting:** it is permissive, per-learner optimisable, computable on-device with no model call, and already validated at scale. It is therefore the cheapest credible "measured outcome" a pilot can ship — see **T10**, where the sector's weak evidence base makes measurable retention the difference between a pilot that renews and one that does not. **Confidence: high** (licence payloads read byte-for-byte; the Anki integration is stated in the project README).

## T14 — African education AI is real, offline-first, and built on open weights rather than released as open source

Previous passes recorded "no Africa-specific data" as a gap. The gap was in the search, not the territory — and what the territory contains has a consistent shape:

- **Demand and public investment are moving.** Google launched a free, **offline-capable** AI and digital-skills training platform for Nigeria and other African markets around **3 November 2026** (English, Swahili, Arabic; Hausa being added; lessons downloadable over Wi-Fi then usable without mobile data). Saudi Arabia and the UAE, at the other end of EMEA, have made AI literacy a mandatory or system-wide part of education.
- **Builders exist and are product companies, not projects.** **Mdali** (Johannesburg) adapts open-source models into an offline-first CAPS Grades 10–12 maths tutor that runs on basic phones and keeps student data on-device. Nigeria's EDAT piloted offline-sync tutoring across 60+ Edo State secondary schools. Kenya's M-Shule and Ghana/Côte d'Ivoire's Chalkboard Education are older precedents in the same mould.
- **But the code is not open.** No African open-source education repository was found at any adoption level. These products are built *on* open weights and released as **proprietary applications**.

**The commercial reading, which is different from every other region:** elsewhere the motion is "adopt the regional open source stack and extend it". For Africa there is no stack to adopt, so the motion is **co-development with existing product teams**, and the differentiating capability is offline-first architecture rather than model work. The one thing that would change this is the stated Google/Fab AI programme with innovators in Kenya, Ghana and South Africa, under which **datasets, evaluation suites and open-source models are to be published**. Worth watching specifically.

**Confidence: medium.** Every item rests on secondary reporting; `blog.google` does not resolve under this session's network policy, so Google's own announcements could not be read first-hand. The *absence* of African open-source supply is the better-evidenced half, since it survived a dedicated search.


🔧 **Sharpened at p688, not overturned.** Two further dedicated legs were run — one on policy (Nigeria, Kenya, South Africa, Egypt), one on supply. **The supply leg produced the first openly-licensed Africa-origin artefact this base has been able to file: [`aicollectiveng/Nigeria-AI-Repository`](https://github.com/aicollectiveng/Nigeria-AI-Repository) (CC0-1.0, `7,048 B` / `a2010f343487`, `26★`)** — and it is a **catalogue of products**, carrying **Wazobia** (open chatbot/translator for Hausa, Igbo, Yoruba) and **GMind AI** (teacher platform with the **Teacher Registration Council of Nigeria**), plus **Deep Learning Indaba 2026, Lagos, August**. 🔴 **A catalogue of products is not a stack to build on, so the headline above stands: the code gap is real and survives a third dedicated search.** What *did* close is a different gap — this base now holds openly-licensed, structured intelligence about **who builds there**, which is precisely the input a co-development motion needs. 🟢 **New policy datapoint:** **Egypt's National Generative AI Guidelines (2026)** are indexed under education and skills — the first Egyptian education-facing instrument located here, school-specific content unread. **The OECD's `Strengthening AI governance in Africa` (April 2026) is named as the primary source a future pass should read.** 🔴 `blog.google` still does not resolve, so the Fab AI open-release commitment remains a watch item on secondary sourcing for a second pass.

## T15 — The EU is now the *last* of three binding education-AI deadlines, not the forcing function

This page has treated the EU AI Act as the sector's clock since it was written. At p652 that is no longer accurate, and the correction changes how a multi-region programme should be sequenced.

| Date | Jurisdiction | Trigger |
|---|---|---|
| **≈ January 2027** | South Korea | Administrative fines become available after MSIT's signalled grace period. Student assessment in early-childhood, elementary and secondary education is **high-impact by statute**. |
| **1 September 2027** | Vietnam | Compliance deadline for education systems already operating before 15 August 2026. **Decision 33/2026/QD-TTg** lists 46 high-risk systems across six sectors; **education is three of them**. |
| **2 December 2027** | EU | Stand-alone Annex III high-risk obligations, after the Digital Omnibus (Regulation (EU) 2026/1744) deferred them from 2 August 2026. |

**Why it matters, beyond the ordering.** The EU deferral bought European clients sixteen months of runway and bought APAC clients nothing — so the two regions this KB has long characterised as "the regulated one" and "the supply one" have swapped position on urgency. Vietnam's trigger is also the sharpest-edged of the three: the high-risk classification bites **only where results serve as the official basis** for assessing learning outcomes or ranking learners, which makes the architecture decision — formative tool versus system of record — the compliance decision.

Three consequences: a proposal that frames December 2027 as "the deadline" is eleven months late for any client with Korean exposure; a multi-region conformity programme should be sequenced to the Korean date with EU and Vietnamese profiles layered on, not the reverse; and **"APAC is the supply side" and "EMEA is the compliance side" are both now wrong** — APAC is both.

**Confidence: medium-high on the dates** (consistent across multiple legal-practice summaries), **low on clause-level detail** — no primary Korean, Vietnamese or Commission text has been read at first hand in any pass.

## T16 — The licence unit is the dependency graph, not the repository

Every pass of this KB has got more rigorous about reading `LICENSE` from bytes. p652 found the limit of that discipline: three separate findings, all the same defect, none of them detectable by reading `LICENSE`.

| Project | Badge | What is in the tree |
|---|---|---|
| **OpenMAIC** (42.7k★, this KB's #2 agent) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** — 7,652 B payload, `"license": "LGPL-3.0-or-later"` verbatim in its `package.json`, declared `"workspace:*"` in the root manifest, and compiled as the **first step** of `build:packages`. A deliverable built from OpenMAIC links it. |
| **OmniEdu** (590★) | Apache-2.0 | The payload covers the **code**. The weights — the artefact a client deploys — have **no named grant anywhere in the repository**: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen. |
| **open-moodle** (0★) | MIT | Depends on **PyMuPDF (AGPL-3.0)** for PDF extraction, stated in its own README. |

LGPL-3.0 is not the GPL and does not make a whole application copyleft; it requires that the component stay replaceable with its source available, and "or-later" means a client cannot freeze the terms. For a bundled, transpiled JavaScript component in a shipped web app that is an engineering requirement rather than a formality. **Workable — but it has to be designed in, and nothing on the badge says so.**

Alongside these, this base now holds **five distinct grant-defect classes** in education open source, four of which pass a licence-badge check: grant absent while a README asserts permissiveness; grant complete but delegating copyright to a missing `COPYRIGHT` file; grant replaced by a 19-byte pointer to its own name (`frappe/education`: `License: GNU GPL V3`); grant complete but contradicted by the README (`protorubric`: Apache-2.0 payload, MIT README); and grant permissive but not covering the artefact that matters (`Omni-Edu`).

**The operational rule:** read `LICENSE` *and* the manifests — `package.json`, `pyproject.toml`, `Cargo.toml` — and for a model, read the weight card. **Confidence: high.** Every item was read from bytes or from the manifest field verbatim.

## T17 — Education gets its own open-weight foundation models, and FP8 makes it a deployment story

Until p652 every agent on this shelf was an application calling somebody else's general-purpose model. **OmniEdu** (Apache-2.0 code, 590★ / 93 forks, Peking University + UCAS + Zhongguancun Academy, arXiv:2609.23088, 22 September 2026) is the first education-domain open-weight family this base has found: 4B / 9B / 27B, trained on 69,999 instruction examples and 15.96M supervised response tokens across subject competence, curriculum grounding, diagnostic reasoning and pedagogical scaffolding.

**The number that makes it operational is not a benchmark, it is a file size.** The FP8 checkpoints are 37–44% smaller than BF16: 27B at 28.30 GiB against 50.96, 9B at 11.09 against 17.53, 4B at 5.14 against 8.46. A ~11 GiB curriculum-grounded tutoring model is single-GPU, in-jurisdiction, no-egress and offline-capable — which is simultaneously the EMEA data-residency architecture, the Sub-Saharan African offline-first architecture and the Korean/Vietnamese "keep it off the system of record" architecture. One artefact answers the binding constraint in three regions.

**Two caveats, both load-bearing.** The benchmark results are self-reported (27B: K12-Bench 63.12 EM / 76.69 F1, MathFish 85.89, EDUMATH MaC 86.95, MathTutorBench Scaffold 78.74, against 16 compared models). And **the weight licence is unknown** — see T16. **Confidence: high on the artefact's existence and composition** (repository and README read at first hand), **nil on the weights' usability** (`huggingface.co` does not resolve in this session).

## T18 — Open source invested in Canvas-shaped institutions, and the bill lands in LATAM and EMEA

This KB declared in every prior pass that no permissively-licensed Moodle-side agent existed. p652 searched the category properly: **seven MIT Moodle MCP servers exist, in five languages** — Rust, Python, TypeScript, Go and Python again — one with full write coverage and a web-service escape hatch.

**And the entire category tops out at 27 stars.** `canvas-mcp`, doing the identical job for Canvas, sits at 317★. Six of the eight Moodle servers measured have four stars or fewer.

So the gap was never a supply gap. It is a **consolidation and adoption gap**, and it is distributed along exactly the fault line that matters commercially: Canvas dominates North American higher education, Moodle dominates LATAM and much of EMEA, and open source has put roughly **12× more reviewed effort** into the agent layer for the former. A LATAM or EMEA client running Moodle is paying for that asymmetry in integration risk, and the honest scoping consequence is that **the Canvas pattern is cheaper than the Moodle pattern today** and should not be priced as though it were not.

The useful half: adopt-and-harden is a weeks-scale input, not a build. `G36maid/moodle-mcp` is the only credible base — most tools, most commits, broadest version claim (Moodle 3.7 → 5.x), real write support — and the engagement is hardening it and contributing upstream. **Confidence: high.** All eight repositories were verified from bytes and their pages measured on 2026-11-04.

## T19 — The strongest statement of this sector's evidence problem now comes from model builders, not critics

**T10** has recorded for several passes that the sector's weak point is its evidence base, resting on third-party analyses. At p652 the claim acquired a better source: the OmniEdu authors, reporting what they say are the leading open-weight results across curriculum-grounding and pedagogical-tutoring benchmarks, write in their own README:

> "Benchmark performance does not establish classroom learning gains."

The OECD says the same thing from the policy side in the **Digital Education Outlook 2026** (January 2026): tools with an intentional pedagogical purpose *"tend to show sustained improvements in learning"*, while *"if designed or used without pedagogical guidance, outsourcing tasks to GenAI simply enhances performance with no real learning gains"* — and it recommends that *"education systems should incentivise the development of tools that aim to enhance teaching and learning"*. And the demand side agrees it has not happened: only **15% of students** say AI is integrated into many of their courses and only **29%** think their instructors are equipped to guide its use (Digital Education Council global survey 2026), against **87% institutional adoption but ~9% outcome evaluation** in LATAM (UNESCO IESALC).

**The convergence is the finding.** Builders, the OECD and students independently describe the same hole: performance has been demonstrated, learning has not, and almost nobody is measuring. Two commercial consequences. First, **measurement is a product** — an evaluation wrapper whose deliverable is the client's own evidence is the one offer that does not require anyone to believe a vendor's efficacy claim, and in a market where 9% of institutions evaluate anything it is close to uncontested. Second, an OECD recommendation to incentivise purpose-built tools over general-purpose chatbots is a policy tailwind under precisely the shelf in `agents/top.md`. **Confidence: high on the quotations and the survey figures; the OECD text is quoted from search excerpts of the PDF because `www.oecd.org` does not resolve in this session.**

## T20 — Permissive assessment software exists now; the *agentic* half of it **also does** — the research-artefact claim is withdrawn 🔴 corrected at p657

Four passes of searching produced, in order: nothing; two education-specific graders with **no usable grant**; one permissive general rubric primitive that is **not** education-specific (`microsoft/LLM-Rubric`, MIT, 45★); and at p653, searching the automated-essay-scoring literature rather than the agent ecosystem, **two permissive education-specific systems**.

| Project | Licence | Adoption | What it is |
|---|---|---|---|
| `wwrwbs/AI_AWE` (**ArguLens**) | Apache-2.0 (notice form) | **2★ / 2 commits** | Scorer **and** label-aware feedback generator. Decomposes AES into a discourse-move classifier, a grade-independent LightGBM scorer over 31 features, and feedback generation. arXiv:2608.17356 |
| `littlecookie0722/AI-Teaching-Agent` | MIT | **0★ / 30 commits** | Exam generation plus a `WAITING_REVIEW` human-approval state machine, Docker-sandboxed grading, no auto-publish. Author declares grading and MCP tracks **frozen** |

**The trend is the shift in the *kind* of gap, and it is the second time this base has seen that shift.** The Moodle bridge went from "no permissive supply" to "seven MIT servers capped at 27★" — a consolidation gap. Assessment has now made the same move: from absent to present-but-unadopted. **This is a better commercial position than it sounds**, because adopt-and-harden against a peer-reviewed decomposition is scopeable, while building a grader from zero is not. It is also the one place in this KB where the production artefact would be Globant's to create.

🔴 **The half that has not moved is the regulated half.** Scoring now has permissive research supply; **assessment *integrity* and proctoring have none, in any pass** — and under EU AI Act Annex III that is the high-risk half, with emotion recognition in schools prohibited outright since February 2025. Permissive supply is appearing where the regulatory exposure is lowest.

🔴 **Refined at p656, and the original heading was too strong.** This trend read *"all of it is a research artefact"*. [`numbas/Numbas`](https://github.com/numbas/Numbas) is **Apache-2.0** (11,357 B, byte-exact canonical), **216 ★ / 129 forks**, pushed 2026-10-28, and is the browser e-assessment system **Newcastle University builds and runs for its own teaching** — randomised question generation, algebraic answer marking, partial credit, SCORM packaging. That is production university software, not a paper's companion code, and it was already present in this repository's logs when the claim was published. The defensible core of the trend survives and is now the heading: **agentic** assessment — LLM scoring, generated feedback, agent-run marking — remains research-grade, and the two rows in the table above (2 ★ and 0 ★) are still the whole permissive supply for it. 🔵 The regulated half named below has not moved either: assessment *integrity* and proctoring still have no permissive production supply, with `SafeExamBrowser` (MPL-2.0, 363 ★) the nearest thing and deliberately not shelved pending a pass that can scope proctoring properly. Shelved at p656 on `repos/foundations.md` and `verticals/solutions.md`.

🔴 **Corrected at p657, and this time the heading itself was wrong.** The claim that the agentic half of permissive assessment is a research artefact rested on two repositories at **2 ★** and **0 ★**. [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) is **MIT** (1,091 B payload read on its real default branch, `develop`), **826 ★ / 395 forks**, pushed **2026-11-05**, latest tag **`10.3.1`**, built and operated by **TUM for its own teaching** — and it ships **three AI subsystems in the tree**: **Iris**, an LLM tutor that guides with hints and leading questions; **Athena**, which suggests feedback on text, modeling and programming submissions; and **Hyperion**, AI-assisted exercise authoring on Spring AI. All three are configuration-gated. That is permissively-licensed, production, agentic assessment running against real cohorts, and it was reachable by searching `topic:autograding` — a topic head no prior pass had swept.

🔵 **The same sweep found three more permissive production autograders this KB did not hold**: `autolab/Autolab` (Apache-2.0, 808 ★, CMU), `Submitty/Submitty` (BSD-3-Clause, 805 ★ / **1,119 forks**, RPI) and `ucbds-infra/otter-grader` (BSD-3-Clause, 162 ★, Berkeley, **and it grades R as well as Python**). With `nbgrader` and `Numbas`, that is **six** permissive production assessment systems, not one exception.

🟢 **What survives, and it is the part worth keeping.** The split **T24** argues for — deterministic grading for what is checkable, calibrated LLM rubrics for what is not, a human decision boundary on anything consequential — is not weakened by this correction; `Artemis` and `Submitty` both *implement* it, `Athena` **suggests** feedback rather than issuing it and Submitty's manual-grading workflow is first-class. 🔴 **And the regulated half has still not moved: assessment integrity and proctoring have no permissive production supply in any pass**, with `SafeExamBrowser` (MPL-2.0, 363 ★) the nearest thing. Permissive supply continues to appear where regulatory exposure is lowest.

🔵 **The method lesson, repeated for the third pass running: saturation is a property of the query.** p656 wrote that sentence about `topic:xapi`. This pass proves it again on a claim this KB had already "refined" once — a refinement that corrected the scope of the error without re-testing its premise. **When a trend is refined rather than retested, re-run the search that produced it.**

## T21 — Local-first by default is becoming a product category, not a deployment option

Three independent signals converged in this base's measurements this pass, and none of them is a cloud product:

- **`zijinz456/OpenTutor`** (MIT, **166★**, 274 commits) defaults to **Ollama**, with the README claiming *"no API keys required, no data leaves your machine"*, and ships **FSRS 4.5** in-tree. Cloud providers are the alternative, not the default.
- **`OpenOlat`** (Apache-2.0) carries `langchain4j-embeddings` — embeddings computed in-process — and Lucene, so semantic search over course content needs no external call.
- **`OmniEdu`**'s FP8 checkpoints (9B ≈ 11 GiB) put a curriculum-grounded model on one GPU, and `Kolibri` (MIT) already runs with no connectivity at all.

**Why this is a trend and not a coincidence:** the three forces pushing it are all strengthening at once — EU AI Act deployer obligations on schools, the sovereignty turn in EMEA public procurement, and the plain fact that student data is minors' data under LGPD, FERPA/COPPA and GDPR alike. The commercial consequence is concrete: **"nothing leaves your hardware" is now demonstrable in an afternoon with permissively-licensed parts**, where a year ago it was an architecture diagram. That is the fastest-moving sales argument on this shelf, and `compose/patterns.md` P7, P9 and P11 all now rest on it.

## T22 — Licence form and licence hygiene are independent variables

p653 catalogued a **sixth** grant-defect class — *grant by reference*: the Apache-2.0 **notice** (the short boilerplate for source headers) used in place of the licence terms, as in `wwrwbs/AI_AWE`'s 1,865-byte `LICENSE`. It is materially stronger than Class 5 (`frappe/education`'s 19-byte `License: GNU GPL V3`) because it carries the operative grant language, the exact version and the canonical URL; what it omits is the copy of the text that Apache-2.0 §4(a) obliges a redistributor to provide. Usable, with a one-line upstream fix.

🔵 **The instructive part is the inversion.** Those same 1,865 bytes enumerate every component and its licence, name the vendored paths, and state what is deliberately **not** redistributed (the Qwen2.5-7B base model; the academic-use-only Persuade 2.0 corpus), closing with a bias notice against high-stakes automated use. That is better licence hygiene than any other repository this base has read — **while the 42.7k★ repository with a byte-perfect MIT payload quietly builds an LGPL-3.0-or-later component.**

**The operational rule this yields:** a short or unusual grant file is a reason to **read** it, not to reject the project; and a perfect grant file is not evidence about the tree. Five of the six defect classes pass a licence-badge check. The sixth fails the badge and passes on substance. Badges measure neither.

## T23 — The permissive-platform claim has collapsed completely, and the blind spot was vocabulary, not availability 🟢 new at p655

This base spent six passes asserting that no permissively-licensed production LMS existed, narrowed it at p651, and retracted it at p653 when `OpenOLAT` (Apache-2.0) was found after seven passes of looking. **p655 shows the retraction was not enough.** Three more permissive platform-class projects were found in a single pass: **`jupyterhub`** (BSD-3-Clause, **8,362★**), **`oppia`** (Apache-2.0, **6,974★**) and **`mentingo`** (MIT, 106★). Two of them out-adopt every copyleft platform this KB tracks except `edx-platform` itself.

**The diagnosis matters more than the rows.** None of the three was hidden; all three were missed because they do an education job without education vocabulary — JupyterHub calls itself infrastructure, Oppia calls itself a learning platform for *explorations*, Mentingo files itself under corporate L&D. **The search instrument was looking for the word "LMS".** Trend-level statement: in 2026 the permissive education stack is substantially larger than keyword search on education terms reveals, and any claim of the form "there is no open source X for education" should be treated as a statement about the searcher.

**Signal:** 5 permissive platform-class rows at p655 against 2 at p653, with no new releases in between — pure measurement, not market change.

## T24 — The assessment gap had a permissive answer the whole time, and it is deterministic rather than AI 🟢 new at p655

Four consecutive passes searched for a permissively-licensed education grader and reported the field as unlicensed or research-grade; the best available row was `microsoft/LLM-Rubric` at 45★. **`jupyter/nbgrader` — BSD-3-Clause, 1,370★, pushed 2026-11-03 — has been autograding university coursework for roughly a decade.**

**The reason it was invisible is the trend.** Every pass searched for an *AI* grader, and nbgrader is not one: it runs tests, allocates points per cell, and separates release → collect → autograde → **manual grade** → feedback. In 2026 the instinct is to look for the LLM-shaped answer to an assessment problem, and for the checkable half of assessment the pre-LLM answer is better — auditable, deterministic, reproducible, and already acceptable to an academic board. **The defensible architecture is a split, not a model:** deterministic autograding for what is checkable, calibrated LLM rubrics for what is not, and a human decision boundary on anything consequential — which is also what the **DC OSSE ban on AI in grading and discipline decisions** and **NY A 9190** make legally necessary in North American K-12.

**Signal:** this KB's own declared assessment gap closed at p655 by a project older than the LLM era.

## T25 — Open edX's official agent bridge arrived, and it is AGPL — the licence boundary inside the stack is now fixed 🟢 new at p655

The Open edX project announced **Open edX MCP** through its own blog in September 2026: a Django app (`blend-ed/openedx-mcp`) plus a Tutor plugin (`blend-ed/tutor-contrib-openedxmcp`) exposing staff and superuser administration operations to MCP clients, targeting the **Ulmo** release. Both grant payloads were read at p655: **34,522 bytes, GNU Affero GPL v3** — matching `edx-platform` itself. `openedx/openedx-ai-extensions`, the official AI-helpers plugin, is the same.

This settles a question this KB has carried open, and settles it negatively: **the official route from an agent into Open edX is network-copyleft, and the permissive route into that stack remains `XBlock` (Apache-2.0) and nothing else.** The practical consequence is a clean architectural line rather than a problem — AGPL components run as separate, unmodified services behind their own network boundary; client IP lives in XBlocks and in out-of-tree agents. ⚠️ Note the correction this forces: earlier notes in this programme described `openedx-ai-extensions` as Apache-2.0. **It is Affero.**

**Signal:** 4 of 4 official-or-announced Open edX AI/agent components read at p655 are AGPL-3.0. Zero permissive.

## T26 — The permissive shelf is tilting from tutors to delivery, and content generation now outnumbers conversation 🟢 new at p655

Of seven agent rows added at p655, **six generate or schedule content rather than converse with a learner**: `Papermorph` (book → animated narrated explainer, 1,211★), `claudemy` (topic → cited audio-lesson course, 611★), `anki-mcp-server` (agent → spaced-repetition scheduler, 544★), `wordlink` (offline fine-tuned 1.5B in-browser vocabulary trainer, 280★), `AILearningGuide` (58 offline labs, 248★) and `lumen` (one-sentence goal → private course + cited RAG tutor, 92★). All MIT, all payloads read at first hand.

**Two structural reads follow.** First, `anki-mcp-server` completes a chain this KB has been assembling for three passes: FSRS (`fsrs4anki` MIT, `fsrs-rs` BSD-3-Clause) is the retention algorithm, `tutor-mcp` (MIT) is the mastery estimator, and this is the tool surface that lets an agent *write into* the scheduler that already ships inside Anki — see **T13** and `compose/patterns.md` **P6**. Second, `wordlink` is the first row on the shelf that **ships its own task-specific fine-tuned weights small enough to run in a browser tab**, which is the EMEA data-residency and low-connectivity argument demonstrated in working MIT code rather than argued. ⚠️ Its code grant is MIT; the weights carry no separately named licence — the same defect this KB flags on `OmniEdu`, and now visibly a pattern rather than an incident.

**Signal:** 6 of 7 new permissive rows at p655 are delivery-shaped; 1 is a tutor.

## T27 — The interoperability layer is permissive and the content layer is copyleft, and the line between them is clean 🟢 new at p656

p656 read the grant payload of every open source component in the layer that joins an AI tool to an institution. The licence split is not a tendency; it is a clean break along a functional boundary:

| Sub-layer | What it does | Licences measured | Verdict |
|---|---|---|---|
| **LTI 1.3** | Launches a tool inside an LMS | Apache-2.0 (`tsugi`), MIT (`pylti1.3`, `marsha`), BSD-3 (`ltiauthenticator`) | 🟢 **Entirely permissive** |
| **SCORM / cmi5** | Plays existing packaged courseware | MIT (`scorm-again`) | 🟢 Permissive |
| **xAPI / LRS** | Records what the learner did | Apache-2.0 (`xAPI-Spec`, `lrsql`, `ADL_LRS`, `TinCanJS`) | 🟢 **Entirely permissive** |
| **Assessment** | Delivers and marks | Apache-2.0 (`Numbas`) vs GPL-2.0 (`tao-core`) | 🟡 Split |
| **Interactive content authoring** | Builds the content | GPL-3.0 (`h5p-php-library`, `H5P-Nodejs-library`), no grant (`Lumi`) | 🔴 **Entirely copyleft** |
| **Accessibility remediation** | Finds and fixes WCAG defects | GPL-3.0 (`UDOIT`, `adapt_framework`) | 🔴 **Entirely copyleft** |

**Why the break falls there, and why it is stable.** The permissive half is the half written by *specification bodies and their implementers* — ADL (US Department of Defense), Rustici, 1EdTech's ecosystem, IMS LTI. A specification wants maximum adoption, so its reference implementations are Apache or MIT by design. The copyleft half is the half written by *product communities* — H5P, Adapt, UDOIT — who chose GPL precisely to keep commercial forks out. 🔵 **This is not an accident of sampling and it will not drift: the incentives that produced each half are still in place.**

**The commercial consequence is a scoping rule.** Globant can own the pipes — get in over LTI, move content over SCORM, record to an Apache-2.0 LRS, assess with Numbas — and must treat authoring and accessibility as *integrate, do not fork*. See `compose/patterns.md` **P17** and `verticals/solutions.md` **Pattern I**. **Confidence: high** — every licence in the table was read byte-for-byte from `raw.githubusercontent.com` on the repository's real default branch, not taken from a GitHub sidebar.

## T28 — The sector's measurement problem had a permissive answer the whole time, and there is exactly one of it 🟢 new at p656

T10 and T19 have recorded across many passes that the evidence base is this sector's weakest point — and T19 noted that the sharpest statement of the problem now comes from model builders rather than critics. p656 closes the *supply* half of that gap and replaces it with a narrower, harder one.

**The answer exists:** xAPI is a ratified Apache-2.0 specification, and a Learning Record Store is the database that implements it — every learner interaction as a statement with actor, verb, object, result and timestamp, queryable by the client's own analysts. This is what turns "the tutor seems to help" into a cohort delta somebody can audit. [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) is **Apache-2.0** (11,357 B, byte-exact canonical), 144 ★, pushed **2026-11-03**, nine open issues, running on SQLite, PostgreSQL and MySQL.

🔴 **And there is exactly one.** The field around it is copyleft, dormant, or both:

| LRS | Licence | Last push | Status |
|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | **2026-11-03** | 🟢 **The only live permissive option** |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | 2025-11-14 | ⚠️ ~12 months quiet — reference, not production |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 GPL-3.0 | 🔴 2024-05-30 | 🔴 Copyleft **and** dormant ~17 months. 584 ★ — the one a client most likely already runs |

**So the gap moves rather than closing.** It was *"no permissive way to measure outcomes."* It is now *"one permissive way to measure outcomes, maintained by one small project, with no permissive fallback."* That is a better problem — it is buildable today — but it is a single-vendor dependency and any proposal selling measurement on a permissive stack should name it. 🔵 **The failure was never discovery: `lrsql` appears in 230 files of this repository's own logs, described there as the permissive production candidate, and had never reached a shelf.** **Confidence: high** on the licences and dates (all measured this pass); **moderate** on `lrsql`'s project health, which rests on commit recency and issue count rather than on any funding or governance signal.

## T29 — The April 2026 US accessibility deadline decomposes into four capabilities, and three of them had permissive answers in this base's own logs all along 🔴 corrected at p661

This base records an **April 2026 ADA deadline for large US public institutions** as a North America demand driver, alongside the state-level activity in T3 and T12. p656 swept for the supply side and the result is negative:

- `topic:accessibility topic:education` returns **442 repositories**. Star-ranked, the permissive rows at the top are `evoluteur/braille-tools` (MIT, 43 ★) and `osunyorg/admin` (MIT, 49 ★) — **neither is a WCAG remediation tool.**
- The production tool is [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) — scans Canvas content for WCAG defects, explains them, fixes many in place, University of Central Florida, 117 ★, pushed 2026-11-04 — and it is 🔴 **GPL-3.0** (35,147 B payload read).
- The authoring tool with accessibility as a design goal, `adaptlearning/adapt_framework` (632 ★), is also 🔴 **GPL-3.0**.
- `screen-reader`, `captioning`, `dyslexia` and `special education` return **zero rows on any shelf** of this KB, before and after this pass.

**Why this is a trend and not merely a gap.** Every other regulatory driver this base tracks — the EU AI Act's Article 50 transparency duty, Korea's high-impact assessment scope, US state model policies — creates demand that *permissive software can serve*. Accessibility is the exception: the mandate is hard, dated and enforceable, and the only real tool forbids a proprietary derivative. 🔵 **The engagement shape is therefore different in kind:** deploy UDOIT inside the client's own estate, bill the remediation work and the integration, and ship no derivative. It is a services engagement, not a product one — and saying that up front is more valuable than discovering it after a proposal has promised a platform. **Confidence: high** on the licence and the supply absence (both measured); **moderate** on the deadline itself, which this KB carries from secondary sources and has not read in primary form.

🔧 **CORRECTED AT p661 — the headline claim above is withdrawn, and the paragraph below replaces it.** What was true: `topic:` and star-ranked queries over `accessibility`, `captioning`, `screen-reader` and `dyslexia` return nothing usable, and no shelf row carried those tags. What was false: the inference drawn from it — *"the one named demand driver in this KB with no permissive answer"*. **The mandate is not one capability, and this base held production-grade permissive answers to three of its four parts without ever shelving them.**

| Capability the April 2026 deadline actually creates | Permissive answer | Verified first-hand at p661 |
|---|---|---|
| **Caption existing lecture video and audio** — by volume, the largest task the deadline creates | [`openai/whisper`](https://github.com/openai/whisper) | 🟢 **MIT**, `1,063 B`, `sha256₁₂ b5d65a59060e`, **`111,975★`**, pushed `2026-08-31` |
| **Make mathematical content accessible** (speech, braille, navigation) | [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | 🟢 **MIT**, `1,065 B`, `sha256₁₂ f8f65c73234f`, DAISY-sourced, ★ unmeasured (three channels refused) |
| **Audit course pages for WCAG defects** | [`GoogleChrome/lighthouse`](https://github.com/GoogleChrome/lighthouse) | 🟢 **Apache-2.0**, `11,358 B`, **`31,019★`**, pushed `2026-11-04`, **runs locally** |
| **Repair WCAG defects *in place* inside an LMS course** | [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0**, `35,147 B`, `117★`, pushed `2026-11-04` — **still the only tool** |

🔵 **So the engagement conclusion narrows from the whole mandate to one quarter of it.** *"Deploy UDOIT in the client's estate, bill the remediation, ship no derivative"* is correct **only** for in-place WCAG repair. Captioning, mathematical accessibility and auditing all permit a closed, client-branded deliverable — and captioning is the biggest piece of the work. The useful sentence for a proposal is therefore the opposite of the one this trend used to carry: **most of an accessibility remediation programme can be built permissively; the last mile inside the LMS cannot.** Shipped as `compose/patterns.md` **P26**.

🔴 **Why the claim survived five passes.** It was checked against the shelves and refuted only in the logs — see **T39**. `whisper` is named in *both* append-only logs as *"the ASR baseline"*. **Confidence: high** on all four licence readings (payloads byte-read this pass); **moderate** on the April 2026 deadline itself, which this base still carries from secondary sources and has never read in primary form — that half of T29 is unchanged and still unverified.

## T30 — Autograding is not an AI story and not a thin layer: it is university infrastructure, permissively licensed, and six systems deep 🟢 new at p657

Across p652–p656 this base searched for education *agents* and for *AI* graders, found the field thin, and recorded the thinness as a market gap. The thinness was in the query. Sweeping `topic:autograding` — **94 repositories, never swept before** — returns a shelf of production systems each run by the university that wrote it:

| System | Licence | ★ / forks | Institution | Pushed |
|---|---|--:|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **MIT** | **826 / 395** | TUM | **2026-11-05** |
| [`autolab/Autolab`](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** | **808 / 234** | Carnegie Mellon | 2026-11-03 |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** | **805 / 1,119** | Rensselaer | **2026-11-05** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | 1,370 | Project Jupyter | 2026-11-03 |
| [`okpy/ok`](https://github.com/okpy/ok) | 🟢 Apache-2.0 | 370 / 88 | UC Berkeley | ⚠️ 2025-07-02 |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3-Clause | 162 / 80 | UC Berkeley DS | 2026-11-01 |

**Three structural reads.** First, **not one of the six is copyleft** — MIT, Apache-2.0 and BSD-3-Clause throughout, which is the opposite of the pattern on the LMS and content shelves and consistent with **T27**: this software was written by universities for peer adoption, not by product communities defending a market. Second, **`Submitty` has 1,119 forks against 805 ★ and `Tango` has 63 against 49** — the adoption signature of infrastructure institutions copy and run, so star counts systematically *understate* this layer. Third, **the sector's grading problem was never a supply problem; it was a discovery problem**, and the thing that hid it was filing autograders as developer tooling rather than as education software.

**Commercial consequence:** the credible engagement is **adopt-and-harden** — deploy, integrate over LTI, migrate real exercises, calibrate, train graders — not build. Any proposal to write a grader from scratch for a university client should now have to argue against six working systems. See `compose/patterns.md` **P19** and `verticals/solutions.md` Pattern J.

## T31 — The psychometric measurement layer is permissive, complete, and almost entirely dormant 🟢 new at p657 🔧 **`p671`: this identifier is used twice on this page.** `p664` reused `T31` for an unrelated trend (the query-language artefact). Both are kept — `82` cross-page references point at the four duplicated numbers and renumbering would break every one — so each collision is named at both ends instead. **This is the `p657` `T31`.**

This base has held knowledge tracing (`pyBKT`, `pykt-toolkit`) for several passes and **T9** correctly called it research-grade. It never held **psychometrics**, which is a different question: knowledge tracing predicts *whether the next answer will be right*; psychometrics estimates *how hard each item is, which skills a learner actually holds, and which item to ask next*. Only the second yields the calibrated item parameters an adaptive test is built on. Sweeping `topic:psychometrics` (517 repos), `topic:item-response-theory` (153) and `topic:computerized-adaptive-testing` (24) returns a full pipeline, all permissive:

| Stage | Component | Licence | ★ | Live? |
|---|---|---|--:|---|
| Parse the client's item bank | [`bigdata-ustc/EduNLP`](https://github.com/bigdata-ustc/EduNLP) | Apache-2.0 | 64 | 🔴 2024-03 |
| Cold-start calibration data | [`tswsxk/EduData`](https://github.com/tswsxk/EduData) | Apache-2.0 | 83 | 🔴 2023-05 |
| Fit item difficulty / discrimination | [`eribean/girth`](https://github.com/eribean/girth), [`17zuoye/pyirt`](https://github.com/17zuoye/pyirt), [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy) | MIT | 127 / 111 / 242 | 🔴 2022 / 2023 / **2018** |
| Diagnose which skills are held | [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | Apache-2.0 | 203 | 🔴 2024-10 |
| Predict the next response | [`bigdata-ustc/EduKTM`](https://github.com/bigdata-ustc/EduKTM) | Apache-2.0 | 267 | 🔴 2024-01 |
| **Choose the next item** | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | BSD-3-Clause | 153 | 🟢 **2026-11-01** |
| Learned selection policies | [`bigdata-ustc/EduCAT`](https://github.com/bigdata-ustc/EduCAT) | MIT | 77 | 🔴 2024-08 |

🔴 **One of seven stages is maintained.** `catsim` — BSD-3-Clause, tag `0.9.1`, default branch **`dev`** — is the only live component, and it happens to be the one that matters most, because it is the piece that converts a question bank into an adaptive test and the piece `compose/patterns.md` **P4** has assumed for several passes without naming.

**This is a different kind of gap from T28's and should be scoped differently.** T28 found *one live permissive LRS with no fallback* — a single-vendor dependency. Here the **mathematics is published and stable** (IRT is five decades old; these are implementations of textbook estimators, not model wrappers that rot), so dormancy is a far smaller risk than it looks: a 2022 maximum-likelihood 2PL fitter is not stale in the way a 2022 LLM integration is. ⚠️ **But the engagement must own them.** Any proposal built on this layer is taking maintenance responsibility for unmaintained code, and should price that in explicitly rather than describe seven dormant repositories as a stack. See `compose/patterns.md` **P18**.

## T32 — Spoken assessment is a layer this KB had never seen at all, and it has a permissive answer that displaces a paid API 🟢 new at p657 🔧 **`p671`: duplicate identifier — `p664` reused `T32`. This is the `p657` `T32`.**

Before this pass, `grep` for `pronunciation` and `speech assessment` across all eight shelves returned **zero files** — and, unlike the p656 interop finding, **zero files in the 5.8 MB and 4.5 MB append-only logs as well.** Not held-but-unshelved: genuinely never seen. `topic:pronunciation` (331 repositories) returns a working stack:

- [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) — **MIT**, 184 ★, pushed 2026-08-15. Phoneme-level assessment: a score, the mispronounced words with the sounds **actually heard in IPA**, a confidence per word, the transcription, and pitch and energy curves. Wav2Vec2 + DTW, **CPU-only**, `pip install openpronounce`.
- [`Kyubyong/g2p`](https://github.com/Kyubyong/g2p) — **Apache-2.0**, 936 ★. English grapheme-to-phoneme: the reference the learner is scored against.
- [`CUNY-CL/wikipron`](https://github.com/CUNY-CL/wikipron) — **Apache-2.0**, 376 ★, live. Pronunciation lexicons mined across **hundreds of languages**, which is what makes this multilingual rather than English-only.
- [`liguozheng-ac/japanese-speech-xray`](https://github.com/liguozheng-ac/japanese-speech-xray) — **MIT**, 177 ★, live. Prosody and pitch-accent, which phoneme scoring alone cannot represent.

**Two things make this commercially unusual for this KB.** First, **it displaces a named line item rather than filling a vacuum**: `OpenPronounce` is positioned by its own author as a self-hosted alternative to **Azure Pronunciation Assessment**, so the proposal is a metered cloud cost replaced by a container in the client's estate — and because voice is biometric-adjacent personal data, that *removes* an EMEA transfer question instead of answering it. Second, the licence advantage runs **against** adoption: the better-known project in the layer, `Thiagohgl/ai-pronunciation-trainer` (525 ★), is 🔴 **AGPL-3.0** and cannot be a client deliverable. ⚠️ **State two boundaries in writing:** a single maintainer at 184 ★, and **phoneme accuracy is not fluency and not a CEFR level** — it does not replace a human oral examiner.

**Regional fit is the strongest of any finding this pass:** English-language training is a large, funded, measurable LATAM and APAC market, and `wikipron` means Spanish and Portuguese learners can be scored on the same stack.

## T33 — The credential-issuing layer is the mirror image of T27: entirely copyleft, with exactly one permissive exception 🟢 new at p657

**T27** established a clean functional break — the *interoperability* layer (LTI, SCORM, xAPI) is permissive because specification bodies write it, while the *content* layer (H5P, Adapt, UDOIT) is copyleft because product communities write it. Credentialing is the second case, and sharply:

| Project | Function | Licence (payload read) | ★ |
|---|---|---|--:|
| [`learningeconomy/LearnCard`](https://github.com/learningeconomy/LearnCard) | Issue / earn / store / share / map credentials | 🟢 **MIT** (1,109 B) | **70** |
| [`fedora-infra/tahrir`](https://github.com/fedora-infra/tahrir) | Open Badges issuer | 🔴 **AGPL-3.0** (34,917 B) | 85 |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | Course / conference certification | 🔴 **AGPL-3.0** (33,820 B) | 64 |
| [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | Open Badges 3.0 / W3C VC library | 🔴 **LGPL-3.0** (7,650 B) | 2 |
| [`edubadges/badgr-ui`](https://github.com/edubadges/badgr-ui) | Badgr front end (SURF edubadges) | 🔴 **AGPL-3.0** | — 🔴 **archived** |

🟢 **`LearnCard` is the only permissive route, and it is a real one:** its monorepo package list, read this pass, carries `vc-plugin`, `vc-api-plugin`, `openid4vc-plugin`, `sd-jwt-vc-plugin`, `didkit-plugin`, `did-web-plugin` and `chapi-plugin` — **W3C Verifiable Credentials, VC-API, OpenID4VC, SD-JWT-VC and DIDs**, standards rather than a bespoke badge format — and it ships an **agent skill** (`npx @learncard/cli skill install`), which makes it directly composable with `agents/top.md`. Pushed **2026-11-05**.

⚠️ **And it is 70 ★ with 42 open issues and one sponsoring organisation.** That is the same single-vendor shape **T28** flagged for `lrsql`, and it should be named in any proposal rather than discovered during delivery. 🔵 **Why the break falls where T27 predicts:** `LearnCard` is written by a *standards-adjacent* body (Learning Economy Foundation, in the 1EdTech/W3C orbit) and the copyleft rows are *products* — badge platforms defending a market. T27's incentive argument holds on a layer it was not derived from, which is the first out-of-sample test it has passed.

## T34 — Skills-based credentialing is a named 2026 buying trend, and the permissive supply for it is one project 🟢 new at p657

1EdTech's own 2026 watch-list names **skills-based credentialing** alongside AI governance as the year's structural shifts, driven by employer expectations moving from degrees to demonstrated skills. Campus Technology's 2026 survey of industry leaders describes AI becoming core infrastructure across **admissions, advising, accessibility and administration** rather than standalone pilots — all four of which are credential- and record-shaped workloads.

**So the demand signal and the supply constraint are both unusually crisp**, and they point in opposite directions: a named, dated, employer-driven buying trend met by **one MIT project at 70 ★** (see **T33**). This is the third demand driver in this KB whose supply side is a single point of failure — alongside `lrsql` for measurement (**T28**) and nothing at all for accessibility remediation (**T29**).

🔵 **The pattern across all three is worth stating as a rule, because it keeps recurring:** where education's demand is *regulatory or institutional* (accessibility mandates, evidence duties, credential recognition), permissive supply is one project deep or absent; where demand is *pedagogical* (tutoring, content generation, autograding), permissive supply is abundant. **Globant's differentiated work is therefore concentrated on the institutional side**, because that is where there is nothing to adopt — and it is also where the client cannot buy an alternative. See `compose/patterns.md` **P21**.

## T35 — The 2026 consensus is governed, purpose-built education AI — and three independent bodies now say the same thing 🟢 new at p657

**T3** recorded that usage had outrun governance and that governance had become the buying trigger. The 2026 sources converge further, and the convergence is the trend:

- **OECD**, *Digital Education Outlook 2026*: move beyond general-purpose AI tools toward **purpose-built educational AI** — curriculum-aligned, with safeguards for minors.
- **1EdTech**, 2026 watch-list: the field is moving **from experimentation to governance**, with explicit policy and oversight as the central concern.
- **HolonIQ**, 2026 Education Trends Snapshot: buyers now favour approaches that demonstrate **instructional value** over broad personalisation promises.
- **Campus Technology** (industry-leader survey): AI as **core operational infrastructure** across admissions, advising, accessibility and administration, not pilots.
- 🆕 **European Parliament (EPRS)**, briefing `784574`, *“Artificial Intelligence in Classrooms: Pedagogical Dimensions”* (`15` pp., Vasiliki Charisi, requested by the CULT Committee) — **read at p669, and it is a fourth independent body saying the same thing**, this time from the EU's own research service and aimed at primary and secondary education: *“A learner-centred approach requires that clearly defined educational objectives, rather than technological capabilities, guide the use of AI in classrooms.”* It names **insufficient pedagogical guidance in classroom AI tools** as a concern. ⚠️ **Evidence class: a search-index read, not a byte-read** — `www.europarl.europa.eu` does not resolve in this session; see the host bullet below. 🔵 **The heading of this trend says “three independent bodies” and the list now carries four. The list is the derived figure and the list is what to count** — `668-O`'s defect is that every derived figure goes stale independently, so the count is stated here rather than buried in a heading written at p657.

⚠️ **One adoption statistic qualifies all of this and should travel with it: 85% of educators report feeling unprepared to manage generative AI in the classroom** (Azumo's 2026 compilation of secondary sources — treat the figure as indicative, not measured). Against **60% of US teachers already using AI tools** (Gallup, n > 2,200), the gap between use and readiness *is* the services market.

**Commercial reading, and it is a reversal of the 2024–25 pitch.** "A general assistant for your institution" is now the weaker proposal; the stronger one is narrow, curriculum-aligned, evidenced and governed — which is exactly what the permissive stack on these shelves supports: `Artemis` with AI configuration-gated per cohort, `lrsql` producing an auditable statement log, `catsim` making item selection explainable rather than learned, and a human decision boundary wherever a jurisdiction requires one. 🔵 **The one claim to avoid** is that purpose-built means proprietary: three of the four bodies above are standards or policy organisations, and their recommendation is satisfied better by auditable open components than by a closed product.

## 🔴 What this page does not claim

- 🟢 **Retracted at p655: the assessment gap.** This page carried "no permissive education-specific grader exists" for four passes. `jupyter/nbgrader` (BSD-3-Clause, 1,370★) existed throughout. See **T24**. What survives of the claim is narrower and still true: **no permissive proctoring or assessment-integrity tool was found**, in five passes of searching.
- 🔴 **No primary regulatory text was read at p655 either**, unchanged for four passes. The EU deadline shift to December 2027 (Regulation (EU) 2026/1744), the Korean AI Basic Act, the Vietnamese AI law and the US state statutes are all carried from secondary commentary — much of it vendor blogs. **Any date that will appear in a contract must be confirmed against the primary instrument.** This is the oldest open item on this page and it is not closing by search alone.
- 🔴 **`huggingface.co` and `openedx.org` do not resolve under this session's network policy**, so the OmniEdu and `wordlink` model cards and the Open edX MCP announcement were read only at second hand (the MCP packages' *grant payloads* were read directly from `raw.githubusercontent.com` and are first-hand).
- 🟡 **The four mandated regional legs returned real material at p655, for the first time in three passes** — US state bill counts, the EU deadline split, the Ipsos APAC ban-support range and Korea's teacher-training spend, the LATAM 90%-use/26%-strategy split and the UNESCO Observatory's partner list. **The one leg that returned nothing is LATAM open source code**, and that is now a measured finding rather than a gap: see `intel/market.md`, LATAM.

- ~~**No verified star counts for `richie`, `chamilo-lms` or `sakai`**~~ — 🟢 **closed at p652**: 318, 1.0k and 1.2k respectively, measured from the repository pages on 2026-11-04 after three passes flagged it. `edx-platform` (8.2k), `moodle` (7.6k), `XBlock` (471) and `kolibri` (1.2k) were re-measured in the same batch and **all four reproduce**.
- **No first-hand reading of any primary regulatory text.** The EU Digital Omnibus, the Korean AI Basic Act and the Vietnamese AI law are all carried from legal-practice and secondary summaries. They agree with one another, which is why confidence is high on the dates — but no Commission, MSIT or Vietnamese National Assembly document was fetched. Verify before quoting a clause to a client.
- ~~**No country-level education AI regulation for any Sub-Saharan African state**~~ — 🟢 **resolved at p652 into an accurate statement rather than an absence**: national AI *strategies* with explicit education commitments exist (Kenya's National AI Strategy 2025–2030 commits to AI literacy across primary, secondary and higher-education curricula; Nigeria's digital economy strategy references AI), and education-sector *rules* still do not. South Africa's draft National AI Policy was published 10 April 2026 and withdrawn 27 April 2026. The African Union's own roadmap puts Phase 1 (2025–2026) at strategy-building, so this is where the continent is scheduled to be. 🔴 **Still absent: any published Kenyan AI-literacy framework** implementing the strategy's commitment — a named, unfilled deliverable as of September 2026.
- **The "agentic university" framing** carried by earlier versions of this page rested on a single arXiv preprint. It is a useful taxonomy, not measured adoption, and has been demoted accordingly.
- **No evidence was found of a dominant open source assessment-integrity or proctoring tool.** Given this is the most heavily regulated use case in the sector, the absence of permissive supply is notable and is recorded as a gap rather than a finding. p652 widened the search to general rubric-scoring libraries and found **one** permissive, credible option — `microsoft/LLM-Rubric` (MIT, 45★), which is **not education-specific** — plus `protorubric`, whose payload and README name different licences. **Three passes, two search strategies, same hole** — 🟢 **and at p653 a third strategy broke half of it.** Searching the automated-essay-scoring literature instead of the agent ecosystem found two permissive education-specific systems: `wwrwbs/AI_AWE` / ArguLens (Apache-2.0, scorer + feedback, arXiv:2608.17356, **2★ / 2 commits**) and `littlecookie0722/AI-Teaching-Agent` (MIT, exam generation + `WAITING_REVIEW` approval gate + sandboxed grading, **0★ / 30 commits**, grading track frozen by its author). **So the accurate split is now: assessment *scoring* has permissive supply at research-artefact adoption; assessment *integrity* and proctoring have none at any adoption, in four passes.** The hole that remains is the regulated half — which is the one that matters under Annex III. See **T20**. 🔵 The methodological point is that the hole was partly in the *channel*: three passes searched for agents, and the supply was in the literature.
- 🔴 **One claim was tested at p652 and rejected rather than published:** that **TEQSA requires Australian higher education providers to submit institutional gen-AI action plans.** No submission mandate was found; TEQSA publishes guidance ("Assuring quality learning in a gen AI-integrated future", 24 June 2026), maintains a Gen AI Knowledge Hub, and leans on Threshold Standard 5.2. This is the second consecutive pass whose mandated regional leg produced a valuable *negative* result — the first was the North Carolina SL 2026-41 dates at p651. **The regional leg's job is partly adversarial, and that is now a pattern rather than an anomaly.**
- 🔴 **A seven-pass blind spot in this base's own instrument, found at p653.** `OpenOLAT/OpenOLAT` — Apache-2.0, 449★, **32,210 commits**, the institutional LMS of much of German-speaking European higher education — was missed by every prior pass because the platform shelf was always ranked by stars, and its star:commit ratio is **1:72**. This page had already recorded the reason (Moodle's forks exceed its stars; institutional software is taken, not watched) and did not apply it to its own ranking. **The correction is a channel change, not a row: for platforms, rank by licence or commit depth.** Counted honestly, this is the third consecutive pass in which the most consequential finding was a defect in this knowledge base rather than a change in the world.
- 🔴 **Still no first-hand reading of the three AI-education statutes, unchanged at p653**, and `huggingface.co` still does not resolve, so OmniEdu's weight licence remains unread for a second pass. Both are cheap to lift and neither was lifted.
- 🟡 **The four mandated regional legs returned almost nothing new at p653, and that is the honest result rather than a gap.** North America, EMEA, APAC and LATAM were each searched; the great majority of what came back — the EU Digital Omnibus deferral to 2 December 2027, Korea's AI Basic Act, Vietnam's education transition date, the UNESCO IESALC 87%/26% denominators, the Universidad de los Andes count of 716 instruments — **this base already held and already sourced.** Four genuinely new readings are recorded in `intel/market.md` under p653. Reproduction is not waste: it is the only evidence that the regional picture is stable rather than stale.
- 🔴 **Five hosts did not resolve in this session at p652** — `www.oecd.org`, `www.unesco.org`, `www.iesalc.unesco.org`, `www.dlapiper.com`, `huggingface.co` — so the OECD recommendations, the Canadian strategy detail and OmniEdu's weight licence rest on secondary sources or are unresolved. The IESALC LATAM figures were independently re-derived from search and reproduce. This is a network-policy ceiling on verification, not a research gap, and it is cheap to lift.
- 🔴 **A sixth host joins that list at p669 — and p669 establishes *why* the class exists, not merely that it does.** `www.europarl.europa.eu` was registered at p668 as a novelty this base could not verify, with the instruction to retry the fetch. p669 retried it on a **different channel** — `WebFetch` rather than `curl` — and got **`getaddrinfo ENOTFOUND`**. 🔵 **Two independent channels failing at *name resolution* is not a transport failure, a proxy refusal or a rate limit: it is the session's network policy.** Every host on this list is therefore in the same class, and **none of them is a retry target.** Stated so no later pass spends budget on it: **these hosts have to be allowed in the session's network settings — re-fetching them cannot succeed.** The documents behind them stay filable at the **secondary** class, which is how the EPRS briefing is filed on `intel/market.md` and in the list above, and they must never be re-quoted as primary reads.

## T36 — The substrate under every school coding tool changed hands, and almost nobody re-pointed at it 🟢 new at p658

**Blockly — the drag-and-drop block library underneath Scratch Blocks, Microsoft MakeCode, Code.org, ardublockly and openblock — moved from Google to the Raspberry Pi Foundation on 10 November 2025.** Google announced it on its Open Source blog in late October 2025; the Foundation published its own notice on 28 October 2025; the library stays Apache-2.0, and Google funded the handover with a grant.

Verified at first hand rather than taken from the announcement: `git ls-remote` returns **the same HEAD SHA** (`a4dbe9f`) for `google/blockly` and `RaspberryPiFoundation/blockly`, and the same again (`8c1a305`) for the `blockly-samples` pair. Identical SHAs on both pairs means these are **redirects of one repository**, not forks — the canonical address is now `RaspberryPiFoundation/*`.

Three consequences, in descending order of how much they cost:

1. 🔴 **A star-ranked census structurally cannot see Blockly.** `blockly in:name stars:>3000` returns `RaspberryPiFoundation/blockly` at **13,600 ★** and does **not** return `google/blockly` at all, because the stars travelled with the transfer and the old address is only a redirect. This base held **zero** Blockly rows before p658 while running star-floor sweeps for hundreds of passes. That is p647-C's finding — *the sort key is the filter* — arriving through a second mechanism: **a transfer silently removes an address from every ranked query that names the old owner.**
2. **The governance fact is procurement-grade.** The library under the world's school coding tools is now stewarded by an **education charity in the UK (EMEA)** rather than a US advertising company. For a public-sector or ministry engagement that is an argument, not trivia.
3. ⚠️ **The ecosystem has not re-pointed.** `TutoriaLLM`, shelved this pass and pushed 2026-11-03, still badges `github.com/google/blockly` in its README. Expect client codebases, docs and SBOMs to name the old owner for years; treat `google/blockly` as an **alias**, not a different project.

**Confidence: high** — transfer verified by SHA identity on two independent repository pairs, date corroborated by Google's and the Foundation's own announcements.

## T37 — The largest blind spot this base has ever had was not a hard layer, it was an unswept one: learn-to-code 🟢 new at p658

Before p658 the shelves held 27 agents and 52 foundations covering tutoring, autograding, psychometrics, spoken assessment, credentialing, LMS and SIS — and **not one row** for block-based programming, physical computing or CS-education delivery. The words `makecode`, `pxt` and `micro:bit` appeared **nowhere** in the repository, not even in `archive/`; `blockly` appeared only inside archived prose describing another project's feature list.

That is the category with the **widest installed base in K-12 worldwide** — Scratch, MakeCode, micro:bit and Code.org are what "computing" means in most school systems. Eighteen foundation rows and five platform rows now cover it.

🔵 **Why it stayed invisible is the transferable lesson, and it is not "nobody looked".** Three mechanisms compounded:
- **T36's redirect** removed Blockly from every star-ranked query naming Google.
- **Topic homonymy**, p646-H's finding, at four new heads at once: `topic:oer` is dominated by ASN.1 **O**ctet **E**ncoding **R**ules (`eerimoq/asn1tools`, 338 ★) and a RISC-V core; `topic:scratch` by "from scratch" tutorials (`geektutu/7days-golang`, **17,036 ★**); `topic:captioning` by image-captioning ML; `topic:wcag` by colour-contrast libraries. A star-ranked read of these four heads publishes a Go tutorial, a CAPTCHA widget and a Swift colour library as education's leading assets.
- **Vintage**: this layer predates the `main` default. **15 of the 21 addresses verified this pass (71%) sit off `main`** — `develop` ×3, `master` ×11, `staging` ×1 — against p645-B's 34.0% population baseline. p646-J said branch name tracks project vintage; here it tracks it at **double** the base rate, because this is the oldest layer in the KB.

**Confidence: high** (the absence was measured by grep over the whole repository including `archive/`; the 21 addresses were verified individually).

## T38 — The index's licence field is unsafe in the permissive direction, and this pass has the worst specimen yet 🟢 new at p658

p657 established that `NOASSERTION` is not a licence finding. p658 establishes the sharper and more dangerous half: **a licence field that names a permissive family can also be wrong.**

🔴 **`TurboWarp/extensions` (194 ★, pushed 2026-11-05) is reported by `gh api search/repositories` as plain `MIT`.** It has **no root grant file at all** — seven filenames probed, all 404. Its `package.json` declares:

```
"license": "MIT AND LGPL-3.0-only AND GPL-3.0-only AND CC-BY-SA-4.0 AND CC-BY-4.0
            AND CC-BY-2.5 AND CC0-1.0 AND Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND ISC"
```

Eleven families joined by **AND**, two of them GPL. A studio that trusted the index's "MIT" would ship GPL-3.0 code inside a proprietary deliverable. **This is the first address this base has found where the index's error runs toward permissive**; every prior case (`NOASSERTION`, p646's `ltijs`) erred toward restrictive, which is the safe direction to be wrong in.

The pass's other two index disagreements both resolved the *other* way, which is why the asymmetry matters: `microsoft/pxt-microbit` (`NOASSERTION` → **MIT**, canonical body behind a two-line bespoke header) and `code-dot-org/code-dot-org` (`NOASSERTION` → **Apache-2.0 + carve-out**). **Rule: the index's licence field is a hint in both directions and evidence in neither.**

**Confidence: high** (all three read byte-for-byte on the resolved default branch).

## T39 — The sector's standard licence shape is permissive code wrapped around unlicensed courseware 🟢 new at p658 🔧 **`p671`: duplicate identifier — `p661` reused `T39`. This is the `p658` `T39`.**

`code-dot-org/code-dot-org` states it in one payload: Apache-2.0 for "all source codes and assets", **except** Code.org's artwork, graphics, sounds, lectures, videos, logos, characters and fonts, enumerated in a 4,271 B / 77-line `NOTICE`, which "may not be used or distributed or accessed in any manner other than directly via Code.org's own web site, mobile applications, or social media channels … **without modification or embedding in another format**". The Minecraft assets inside it are **Microsoft's**, and any distribution outside Code.org's own site needs a separate agreement with Microsoft.

This is the same shape p657 found at the OER layer and p656 at the platform layer, and it is the shape that decides education engagements: **the engine is free, the lesson content is not.** A proposal that says "we will build on Code.org" and means "we will ship their courses" is a licence incident waiting to be discovered by the client's counsel.

**Confidence: high** (licence and `NOTICE` both read in full).

## T40 — Scratch is two licences, and which one you touch decides the business model 🟢 new at p658 🔧 **`p671`: duplicate identifier — `p661` reused `T40`. This is the `p658` `T40`.**

Not one project: `scratch-gui` (4,807 ★) and `scratch-vm` (1,306 ★) are **AGPL-3.0**; `scratch-blocks` (2,769 ★, pushed 2026-11-05) is **Apache-2.0**. Hosting a modified Scratch editor as a service triggers network copyleft on the hosted work; building on the blocks library does not.

Two permissive escape routes exist and both were verified this pass: build the editor on **`scratch-blocks`**, and execute projects with **MIT-licensed `forkphorus`** (150 ★) instead of the AGPL `scratch-vm`. `goboscript` (MIT, 577 ★) compiles text to `.sb3`, and `leopard` (MIT, 168 ★) converts Scratch projects to readable JavaScript — the block→text migration path a curriculum needs after year two.

🔴 **A payload finding sits underneath this trend.** `scratch-blocks` and `ardublockly` ship **byte-identical** Apache-2.0 payloads (`md5 f15febb3…`, 10,174 B) that are **not canonical**: the header is misdated **"Version 2.0, January 2011"** (canonical: January 2004) and the entire APPENDIX is truncated. Operative terms, lines 1–177, are byte-identical to canonical, so **the grant is Apache-2.0** — but a byte-equality or template-identity test keyed on 11,357 B scores both `UNKNOWN-TEMPLATE`. Two independent downstream Blockly derivatives carrying the same corrupted text is a **copy lineage**, and it is bounded: `openblock-desktop`, `aily-blockly` and `pxt` all differ.

**Confidence: high** (diffed line by line against a canonical payload read the same hour).

## T41 — The runtime is the distribution channel: education tools now ship as a plugin per agent host 🟢 new at p659

For most of this base's history an education AI tool was *an application* — something an institution deployed, or a learner opened in a browser. p659 measures how far that has moved, and the number is on this KB's own shelf: **9 of the 29 rows on `agents/top.md` are not applications at all, they are surfaces into an agent runtime** — seven MCP servers (`canvas-mcp` × 2 independent projects, `moodle-mcp`, `tutor-mcp`, `anki-mcp-server`, `brightspace-mcp-server`, `brightspace-d2l-mcp`), one agent *skill* (`universal-examprep-skill`) and one runtime *plugin* (`PAIDEIA`). **Just under a third of the permissive education shelf is plumbing for somebody else's agent.**

🔵 **The clearest single specimen is `OPTIMETA/PAIDEIA`, and it is why this trend gets its own number rather than a line under T27.** One author shipped the same study engine as **five separate repositories**, one per agent host — Claude Code, OpenAI Codex CLI, `sst/opencode`, `NousResearch/hermes-agent`, and a standalone local MCP server — all MIT, all created between **21 April and 14 June 2026**, all still pushed through **September 2026**. Not a port forced by a client; a *distribution decision*. The engine is identical; what varies is the host it plugs into.

🔴 **Why this is a commercial fact and not a packaging detail.** It inverts where the integration cost sits. An application has to be deployed, hosted, secured and signed off by an institution before a learner touches it — months, in public education. A plugin inherits its host's installed base, its auth, its file access and its model access, and reaches a learner the day it is published. **That is also the catch:** it reaches the learner *and nobody else*. A tool distributed this way has no institutional telemetry, no roster, no grade book and no audit trail — which is precisely what the EU AI Act's Article 50 and every Annex III obligation ask a deployer to produce (**T15**, **T35**). 🔵 **So the two halves of this sector are now diverging on who the customer is:** runtime plugins are consumer distribution to individual learners, and the institutional sale still needs the evidence spine of **P17**. A client proposing to “ship a plugin” for an accredited programme is proposing something that cannot be evidenced.

🟡 **Read the star counts honestly before building a thesis on them.** The four `PAIDEIA` ports carry `26`, `3`, `2` and `1` star against the canonical's `92`. This trend is evidenced by **what builders are choosing to ship**, not by adoption — there is no adoption here to measure. The canonical's `#1` placing on GeekNews and a Product Hunt launch are reach signals for the *project*, not for the ports.

🔵 **The port worth watching is the MCP one**, for the same reason `anki-mcp-server` mattered at p655 and `tutor-mcp` before it: an MCP server is the one shape on this list that is **not** tied to a single vendor's runtime, so it is the only one an institution can point at a local model it controls. If this trend resolves anywhere durable, it resolves there — see **P24**.

## T42 — `NOASSERTION` has a second mechanism, and it is the one with a commercial consequence 🟢 new at p660

p659 named a mechanism for `NOASSERTION`: on a controlled five-repo set, appending text to an otherwise byte-stock MIT grant flips GitHub's classifier off a correct verdict. That mechanism is real, and it is **benign** — the stated licence still governs the whole repository, so reading the payload recovers the right answer and nothing about the engagement changes.

p660 found a **second, distinct mechanism with the opposite consequence.** Both `NOASSERTION` repositories measured this pass carry a payload that is **not a grant at all**. It is a *licence-split manifest*: a short file naming two or three different licences for different directories.

| Repository | Classifier | Payload, byte-read at p660 | What the file actually says |
|---|---|---|---|
| [`scratchfoundation/Scratch_1.4`](https://github.com/scratchfoundation/Scratch_1.4) | `NOASSERTION` | `LICENSE`, `1,008 B` | **Three licences in one repo.** Code **GPL-2.0**; `/src/plugins` **MIT**; `/Help`, `/Media`, `/Projects` **CC BY-SA 3.0**. Plus a term rarely seen in this KB: modified versions must be *designated as modified in the `Help > About` dialog at runtime* — an attribution obligation in the **UI**, not just the source. |
| [`RaspberryPiFoundation/scratch-curriculum`](https://github.com/RaspberryPiFoundation/scratch-curriculum) | `NOASSERTION` | `LICENSE.md`, `551 B` | **CC BY-NC-SA 4.0** — Attribution–**NonCommercial**–ShareAlike, plus Code Club terms and conditions by reference. |

**Why the distinction matters more than it sounds.** Under p659's mechanism, a payload read *resolves* `NOASSERTION` into a usable licence. Under p660's, a payload read resolves it into **a question you still have to answer**: which licence governs the part you intend to ship. A pipeline that files one SPDX value per address — as this base's own ledger schema does — cannot represent either row honestly, and `Scratch_1.4` is filed in `evidence/address-ledger.tsv` as `licence-split:GPL-2.0+MIT+CC-BY-SA-3.0` for exactly that reason.

### 🔴 And the curriculum-licence finding gets worse, not just confirmed

This base has been accumulating a hypothesis: permissively-licensed education **software** is common, permissively-licensed education **content** is not. The evidence was two assets, both ShareAlike — [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) (949★, CC BY-SA 4.0, declined at p651) and a French K-12 curriculum pack (CC BY-SA 4.0, declined at p658).

`scratch-curriculum` (212★, **357 forks** — more forks than stars, the signature of material institutions take copies of) is the third, and it is **stricter than both**: CC BY-**NC**-SA 4.0. ShareAlike bars a *closed* derivative. NonCommercial bars **commercial use at all** — a Globant engagement cannot ship it, cannot bundle it, and cannot charge for a service built on it, regardless of whether the derivative is open.

**3 of 3 curriculum assets this base has measured are non-commercialisable, and the newest is the hardest.** The single counter-case remains [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) (MIT, `1,066 B`, re-read at p660), which is precisely why `compose/patterns.md` **P10** is built on that one and not on a school curriculum. **Confidence: high** on the licences (three payloads byte-read); **medium** on the generalisation — three assets is a pattern, not a census, and this base says so rather than rounding it up.

🔵 **The practical rule this yields.** In an education engagement, price the *content* licence separately from the *code* licence and read it first. The code is usually MIT or Apache; the curriculum is usually the thing that cannot be sold, and it is usually the thing the client actually wanted.

🟢 **Extended at p662 with a controlled specimen that isolates the filename axis.** `anchore/syft` serves canonical Apache-2.0 at `LICENSE` (`11,357 B`, `sha256₁₂ c71d239df917`) and classifies **`Apache-2.0`**. `aboutcode-org/scancode-toolkit` serves **the same bytes and the same digest** at `apache-2.0.LICENSE` on `develop`, and classifies **`NOASSERTION`**. Payload held constant, filename varied, verdict flipped — which is the cleanest demonstration this base holds that a `NOASSERTION` carries no information about the grant. 🟢 **And the complementary control:** `CycloneDX/cyclonedx-cli` *filled in* the Apache `APPENDIX` boilerplate (`Copyright OWASP Foundation`, brackets `{}`, `11,341 B`, `sha256₁₂ 6c29f22a4a73`) and still classifies `Apache-2.0`. **Completing the appendix is safe; removing it and appending text — OpenOLAT's shape — is what flips the classifier.** All four readings taken first-hand on `2026-11-05`. Wired as `compose/patterns.md` **P27**.

## T39 — This base's absence claims are checked against its shelves and refuted in its logs, and that is now its dominant defect class 🟢 new at p661 🔧 **`p671`: duplicate identifier — `T39` was already taken by `p658`'s courseware-licence trend. This is the `p661` `T39`.**

Four of the last six passes found the same thing, on four different layers: **the finding was already held and had never reached a shelf.** p656 — the interop, telemetry and accessibility layer, measured in the logs for many passes, never promoted. p659 — `PAIDEIA` measured since p540 and never filed; `ollama/ollama` cited on five shelves while its ledger verdict read `unstated`. p660 — `35` of `159` shelf addresses missing from the base's own index, `22.0%` invisible. p661 — the accessibility layer again, plus a proctoring absence claim its own log had refuted `451` passes earlier.

🔵 **p661 names the mechanism, and it is a scope bug in one instrument rather than carelessness in many passes.** `evidence/absence-claim-census.2026-10-31-p569.tsv` exists precisely to catch an absence claim the base's own holdings contradict, and it works — it flagged `27` gateable claims and closed a 145-pass-old gap. Its scope:

```
broad   pages_scanned         11      live pages only, archive excluded
broad   shelf_rows_indexed    10892   lines carrying a github.com address
narrow  supply_claims         569     absence sentence naming a buildable-on noun
narrow  full_token_collision  27      the gateable set
```

A claim is flagged only when its content tokens collide with a **shelf row**. The two append-only logs are a further **`124,015` lines** carrying exactly such addresses (`agents/trending.md` `69,591`, `repos/trending.md` `54,424`) and collisions there are **not scored at all**. So the census can catch *"X does not exist"* when X is on a shelf, and is structurally blind to it when X is in a log — which is where this base puts everything it measures before deciding whether to promote it. **The blind spot is exactly the backlog.**

🔴 **And the ledger makes the diagnosis worse, not better.** `evidence/address-ledger.tsv` is a dated, machine-readable index of `3,228` addresses, and it **held the refuted material with the correct licence the whole time**: [`openai/whisper`](https://github.com/openai/whisper) has been in it since **`p6`** with verdict `MIT` and `filed_on = "-"` — `655` passes indexed, correctly licensed, never shelved — and `GoogleChrome/lighthouse` since **`p19`** with verdict `Apache-2.0`, likewise. So this is not a case of the base not knowing. **It knew, in a machine-readable file, and no instrument compares that file against the sentences the pages assert.** 🔵 **`filed_on = "-"` is a ready-made promotion backlog and the least-used column in this base** — one `awk` filter produces it. 🔧 p661 also repaired two verdicts that were wrong in the **restrictive** direction (`lebmatter/exampro` and `vardanagarwal/Proctoring-AI`, both carried `unstated` while serving clean MIT payloads). **T38** warned that the licence field is unsafe in the permissive direction; the restrictive direction is quieter and costs more, because an `unstated` verdict on an MIT repository silently removes a usable asset and nobody ever finds out.

🔴 **Why this matters outside this repository.** Every absence claim on these pages is load-bearing for an engagement: *"there is no permissive proctoring software"* becomes a line item to build, and *"accessibility has no permissive answer"* becomes a services-only proposal with no product. Two such claims were wrong this pass, and both would have changed a proposal's shape and price. **An append-only log is an asset only if something reads it back.** Registered as `Gap 661-C`; the fix is to index the logs as a refutation corpus distinct from the shelf corpus, and it was not performed because `make hooks` and `ingest/` have been denied for eleven consecutive passes. **Confidence: high** — the mechanism is read directly off the instrument's own recorded scope, and both p661 cases fit it exactly.

## T40 — Every "no permissive supply" claim this base has tested has turned out to be an adoption gap instead, and that is now five for five 🟢 new at p661 🔧 **`p671`: duplicate identifier — `T40` was already taken by `p658`'s Scratch trend. This is the `p661` `T40`.**

The pattern is complete enough to state as a rule. Each of these was published as a supply absence and each, when the right query was finally run, turned out to be shallow-but-real supply:

| Layer | Published as | Turned out to be | Pass |
|---|---|---|---|
| Moodle agent bridges | *"no permissive Moodle-side agent"* | **7 MIT servers**, whole field ≤ `27★` | p652 |
| Permissive institutional LMS | *"no permissive platform of the Moodle class"* | **`OpenOLAT`**, Apache-2.0, `32,210` commits | p653 |
| Assessment scoring | *"no permissive assessment agent"* | **2 education-specific**, both research artefacts | p653 |
| Learn-to-code | not even searched for `657` passes | **18 foundation rows**, incl. BSD-3 ScratchJr | p658 / p660 |
| Proctoring and integrity | *"genuinely unsupplied under a permissive licence"* | **6 permissive addresses**, held since `p202` | p661 |

🔵 **The mechanism is the same every time and it is a vocabulary problem, not a search-effort problem.** Each absence was measured with a `topic:` head or a star-ranked query, and each was broken by a different channel: licence-first for OpenOlat, the academic literature for assessment, org enumeration for ScratchJr, and at p661 **`license:mit` sorted by stars** for proctoring — none of those six proctoring repositories is tagged `proctoring` in a way the topic sweeps reached. p658 wrote the prescription — *"a future pass should query by capability, not by tag"* — and p661 is the pass that applied it to a different gap and was paid out twice.

🔴 **The operating rule for a proposal.** When these pages say a layer has no permissive supply, read it as **"no permissive supply this base has found with the queries it has run"** — and expect the true answer to be *shallow, fragmented, unadopted supply* rather than emptiness. That distinction changes the engagement from *build* to *adopt-and-harden*, which is a different scope, a different price and a different risk profile. 🟢 **The two absences that have survived every re-probe are worth naming for contrast**, because they are the ones that look real: **in-place WCAG repair inside an LMS** (UDOIT, GPL-3.0, re-verified p661) and **any OpenOlat agent bridge at all** (`0 of 5` addresses resolve, re-probed p661, fourth consecutive confirmation). **Confidence: high** on the five cases, each of which is a measured reversal recorded on these pages with first-hand licence reads.

## T43 — A knowledge base's index can assert filings its own pages no longer carry, and the cause is the rewrite, not the research 🟢 new at p662

T39 named this base's dominant defect class as *claims checked against shelves and refuted in logs*. p662 found the adjacent one, and it is larger. `evidence/address-ledger.tsv` is the index that answers *"do we already own this?"*; its `filed_on` column made **`259`** claims and **`29`** were exactly right. **`142`** named a page that does not carry the address at all, and **`100`** of those name an address the live tree carries nowhere. In the other direction, **`59`** addresses sitting on a curated page carried `filed_on = "-"`.

🔴 **The cause is a step missing from a procedure the base performs deliberately.** Traced against `archive/`, **`85`** of the `142` were last carried by the `p568` pre-rewrite snapshot and **`52`** by `p650`'s. Both passes rewrote all six curated pages and both archived the previous version first — the discipline was there. Neither reconciled the index against the page that replaced it, and no pass ever has. `85` claims stood false for `94` passes.

🔧 **And the headline metric could not have caught it, because it was right by cancellation.** `ingest/promotion-ratchet.json` reported `filed: 258`. The true count of distinct index addresses present in the curated tree is **`176`** — and `259 − 142 + 59 = 176` exactly. An over-count and an under-count of opposite sign and near-equal size produced a number one away from the truth while `230` of its `259` constituents were inaccurate.

🔵 **Why this generalises past this base.** Any curated knowledge store that (a) rewrites whole pages and (b) keeps a separate index of what it holds will drift the same way, and the drift is invisible precisely because the index is what you would check. The control is cheap — re-derive the index from the tree and diff — and it belongs **in front of** a rewrite, not after one. Confidence: 🟢 **high**, measured twice with a re-implemented instrument and `6/6` hand controls; the generalisation beyond this repository is 🟡 **argued, not measured**.

🔴 **One scope question is deliberately left open.** `42` of the `142` are still reachable on `intel/open-gaps.md` or `intel/measured-unusable.md` — reader-facing pages outside the index's `CURATED` list. Either those pages join `CURATED`, or `filed_on` needs a third state for *demoted, still readable*. p662 did not decide it, because deciding it silently is how the column became wrong.

## T44 — The sixth "no permissive supply" claim fell too, but to a different mechanism: the supply was there and the base was searching in the wrong language 🟢 new at p663

**T40** records that every *"no permissive supply"* claim this base has tested turned out to be an **adoption** gap instead — five for five. p663 makes it **six for six and changes the mechanism**, which is why this is a separate entry rather than another tally mark on T40.

The claim under test was this base's longest-standing structural gap: **`agents/top.md` carried *"EMEA and LATAM have zero placed agent rows between them"***, and had carried some version of it for dozens of passes.

🟢 **It is now closed for LATAM, with two rows** — [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Universidad Tecnológica de Pereira, Open edX XBlock) and [`AndresGuido9820/trabajo2-agente-tutor`](https://github.com/AndresGuido9820/trabajo2-agente-tutor) (MIT, Universidad Nacional de Colombia, 151 commits / 314 tests). Both placed on a **named institution in the repository's own text**; the placement rule was not relaxed to get there.

🔵 **The mechanism is new, and it is the transferable part.** The first five instances were all *adoption* gaps: the software existed, was findable in English, and was simply shallow or unadopted. This one was an **instrument** gap:

| Leg | In-scope addresses returned | Novel |
|---|---|---|
| 4 × mandated **English-language** supply legs | 🔴 **0** — sixth consecutive pass | 0 |
| `…educación IA agente tutor español México Chile Colombia licencia MIT 2026` | 4 | 🟢 1 |
| `…tutor agent Brazil Mexico Argentina universidad github MIT licença educação` | 7 | 🟢 1 (an AGPL refutation) |

**Both** novel addresses in the pass came from non-English legs, and **both** were LATAM. The English legs have returned nothing in scope since p658.

🔴 **Why this is a trend and not a one-off.** The three forces behind it are structural, not accidental. (1) **Education software is written in the language of its curriculum** — a tutor for Colombian rural higher education is described in Spanish, names a Colombian university, and uses the word *tutor* in a Spanish sentence that an English-keyword query does not match. (2) **This base's own placement rule compounds it**: author names and README language are correctly excluded as placement channels, so a project that *is* placeable only shows up as placed if a query reaches it at all. (3) **Star-ordered discovery buries it further** — both rows are `0★`, and this base has already measured that stars mis-rank education software by up to **1:72** on star:commit (`OpenOlat`).

🟡 **The honest limit, stated with the claim.** Closing the LATAM zero did **not** produce an adoptable production base: both rows are `0★` university coursework. So T40's underlying shape survives intact — supply exists, and it is shallow and fragmented. What changed is that this base can no longer attribute a regional supply gap to the *region* without first running the legs in the region's own languages.

🔴 **EMEA is still zero, and it is now the sharper anomaly** — it is where the binding statute is, and where this base's strongest *platform* rows are built (OpenOlat, ILIAS, Artemis), yet it has no placed **agent** row. T44 predicts the fix and the next pass should test it: **run the supply legs in German, French, Spanish and Portuguese before concluding anything about EMEA agent supply.**

⚠️ **Consequence for every absence claim on this page.** Any *"searched and not found"* on a non-anglophone region that rests only on English-language legs is **provisional**, not settled, and should be re-stated as such rather than cited as a measured gap.

🔧 **Numbering note:** this entry is **T44** because **T43** is the highest unique number on the page — `T39` and `T40` each appear **twice** (p658 and p661 both minted a pair). The duplicates are left in place rather than silently renumbered, since other pages cite them by number; flagged here so the next pass does not mint a third `T39`.

## T31 — A regional "zero" on this base's shelves has twice turned out to be a query-language artefact, and the instrument is the finding 🟢 new at p664 🔧 **`p671`: duplicate identifier — `T31` was already taken by `p657`'s psychometric-layer trend. This is the `p664` `T31`.**

Two regions carried zero placed agent rows on `agents/top.md`. Both closed inside two passes, and neither closed because the sector changed.

| Region | Closed at | Leg that closed it | What the mandated English legs returned |
|---|---|---|---|
| LATAM | p663 | **Spanish** | nothing in scope |
| EMEA | p664 | **German** — first attempt | nothing in scope, 7th consecutive pass |

The four mandated English-language supply legs have now returned **zero in-scope novel addresses for seven consecutive passes**, and the trending digests have gone **twenty** passes without a yield. In the same window, non-English legs produced `TutorIA`, `Profe Bit`, `EduRAG` and `RUCAI` — every regionally placed row added since p662.

🔵 **The generalisable claim is narrow and worth stating precisely:** English-language search surfaces the *most-starred* education repositories, which are disproportionately American and Chinese, and it does not surface *institutionally-situated* ones, which are where regional placement evidence lives. A base that searches only in English will therefore measure a world in which only APAC and the unplaced global middle build education agents — which is exactly what this base measured for its first ~660 passes.

🔴 **The counter-case that stops this becoming a rule.** **North America now has one placed row against APAC's eight** and its query language is already English. So language is a sufficient explanation for the LATAM and EMEA zeros and **not** a general theory of regional coverage. The North American thinness is unexplained and is registered as an open question in `intel/market.md`, not papered over with this trend.

**Operationally:** run the supply legs in German, French, Spanish and Portuguese as standing practice, and treat a declared regional absence as a statement about the instrument until it has been tested in the region's own language.

## T32 — In LATAM, adoption and licensability are inversely correlated, which makes licence remediation the cheapest intervention available 🔴 new at p664 🔧 **`p671`: duplicate identifier — `T32` was already taken by `p657`'s spoken-assessment trend. This is the `p664` `T32`.**

Measured at p664, the Brazilian education-agent field:

| Address | Stars | Forks | Grant |
|---|---|---|---|
| `digitalinnovationone/dio-agent` (DIO) | **2,988** | **367** | 🔴 **none at four root filenames; `spdx = null`** |
| `LabSirius/TutorIA` | 0 | 0 | 🟢 MIT |
| `AndresGuido9820/trabajo2-agente-tutor` | 0 | 0 | 🟢 MIT |
| `ThallesYVasconcelos/Agente-Educacional` | 0 | 0 | 🟢 MIT |

**The one with three orders of magnitude more adoption than the others combined cannot be built on at all**, and neither can the 367 forks already downstream of it.

🔵 This is a different problem from the one **T18** describes. T18 is about where open source *invested* — Canvas-shaped institutions, at the expense of Moodle-shaped ones. T32 is about **licence hygiene tracking adoption in the wrong direction**: the projects that earned users are the ones that never did the paperwork. **T22** established that licence form and licence hygiene are independent variables; T32 is the regional consequence, and it is severe enough to invert the standard advice. Where this base would normally say *adopt-and-harden* (**T18**, **P8**), in LATAM the first move on the most-adopted repositories is **neither adopt nor build: it is ask for a licence file.**

That is weeks of relationship work with a named publisher, it converts a dead 2,988-star base into a reusable one, and it is the highest-leverage, lowest-cost move this base has identified in the region. Scoped as **`compose/patterns.md` P29**.

⚠️ **Scope limit:** measured on Brazilian repositories in one pass. Whether it holds for Spanish-speaking LATAM, or outside LATAM, is **untested** — the Spanish leg's novel addresses at p663 and p664 were all research-scale, so there was no high-adoption case to grade.

## T45 — A declared filing is not a filed row, and the log is where the claim goes to be believed 🟢 new at p665

**T43** measured an *index* asserting filings its pages no longer carried, and traced the cause to whole-page rewrites. p665 found the sibling one level up, and it is cheaper to cause and harder to see: **the append-only log asserts filings that were never written at all.**

`repos/trending.md` at **`p588`** published a table under the heading *“SIX ROWS FILED”*, with star counts, provenance and a passes-unfiled column — the full apparatus of a completed action. Re-measured at p665 against every sell shelf (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`, `compose/patterns.md`, `intel/trends.md`, `intel/market.md`):

| `p588` declared filed | ★ | On a shelf at p665 | `MOVED` records |
|---|--:|---|--:|
| `microsoft/generative-ai-for-beginners` | 122,693 | 🔴 no — only in `intel/open-gaps.md` | 3 |
| `rasbt/LLMs-from-scratch` | 107,625 | 🔴 no — only in `intel/open-gaps.md` | 1 |
| `jingyaogong/minimind` | 64,710 | 🔴 **no — on no page at all** | 2 |
| `karpathy/nanochat` | 59,252 | 🟢 yes (`agents/top.md`) | 3 |
| `ashishpatel26/500-AI-Agents-Projects` | 39,200 | 🔴 **no — on no page at all** | 6 |
| `apache/openmeetings` | 688 | 🔴 no | 🔴 **0** |

**Five of six, four passes later.** And the `MOVED` column separates two different failures that look identical from the index: rows that were written and later dropped by a rewrite (**T43**'s mechanism), and `apache/openmeetings`, which has **zero** drop records — it was *never written*. p588's own prose had already called it the sharpest specimen of this base's bottleneck, having found it in a file named `permissive_unshelved.txt` that nothing had read for 63 passes. **The pass that diagnosed the bottleneck then reproduced it.**

🔵 **The generalisable claim.** In any store where the narrative log is append-only and the curated pages are rewritten, **the log accumulates intentions and the pages hold state** — and because the log is the richer, more recent and more confident document, a later pass reads the intention and stops. The control is not another census: it is that *a filing is a row in a table*, verified by looking at the table in the same pass that claims it. p665 wrote six rows across three shelves and re-derived every count from the columns rather than incrementing them.

🔴 **Corollary, and it retires a signal one pass after it was introduced.** p664 promoted off the signature *“`filed_on = -` plus many distinct passes”*. Over the whole ledger `filed_on = -` covers **3,050 of 3,237 addresses (94.2 %)**, and on the 23 education-shaped candidates this pass served, **20 were demotions** (`MOVED` to the log), not omissions. p664's own true positive, `academico-sis/academico`, carries **10** `MOVED` records, so the obvious refinement — *never dropped* — would have missed it. The signal that survives is the conjunction **never dropped ∧ ≥ 5 distinct passes**, which narrows 3,050 to **10** addresses; everything else needs a *stated re-filing reason*, in-cell, of the kind `universal-diagnostic-tutor-skill` and `TorchLeet` now carry.

## T46 — The reference implementation of statutory personalised learning is a government's production repository, and it is licensed EUPL 🟢 new at p665

Four passes of EMEA legs on this base have returned regulation: the **Annex III** postponement to 2 December 2027, the UK DfE's product-safety standards, KHDA guidance. p665's EMEA fact came from a different channel — the repository channel — and it changes what an EMEA engagement can start from.

**`Opetushallitus`, the Finnish National Agency for Education, runs its learner-facing stack in public**: applications (`ataru`), the statutory **personal competence development plan** every vocational student is entitled to (`ehoks`), the machine-readable **national core curriculum and qualification requirements** (`eperusteet`), attainments (`suorituspalvelu`), learner identity, organisations and state grants. Seven repositories, all pushed `2026-11-05`, all under the **European Union Public Licence** — two at EUPL-1.2-or-later, five at EUPL-1.1-or-later, every payload read at p665.

🟢 **Two of those objects are things this base has watched agents reinvent.** Every curriculum-grounded tutor on `agents/top.md` grounds itself in a *document* — BNCC as PDF, a `Rahmenlehrplan` as PDF. `eperusteet` is that object **as a service, with a data model, maintained by the authority that issues it**. And “personalisation” in a European public tender usually means `ehoks`'s statutory object, not an adaptive-tutoring claim; here it is, implemented.

🔴 **The licence is the constraint, and it is not GPL's.** The EUPL is copyleft whose own definition of *“Distribution or Communication”* reaches making the Work available **online** — so a modified fork stood up as SaaS triggers the obligation, the way AGPL-3.0 does and GPL-3.0 does not. Its appendix brings two compensations a procurement office cares about: a **compatibility list** permitting relicensing onto GPL-2.0, AGPL-3.0, EPL, MPL-2.0, LGPL, OSL, CeCILL or LiLiQ, and **legal validity in 23 EU languages**.

🔵 **So the trend is not “ministries are going open source” — it is that the open artefacts of European public education are arriving under a licence that prices forking and rewards integration.** The commercial shape that follows is arm's-length: an MIT/Apache agent layer in its own process, calling these services over their APIs, inheriting nothing — written up as **P32**. 🔵 **And a measurement lesson worth carrying: `gh api` reports all seven as `NOASSERTION`.** Third instance of that trap in three passes (p663 on MIT, p664 on AGPL-3.0), and the first to hide a whole licence *family* — the classifier does not match a four-line EUPL reference, so a tier was missing from `verticals/solutions.md` for want of reading four lines.

## T47 — A licence identifier is not a licence: three mechanisms by which the index and the payload disagree, measured on one organisation 🟢 new at p666

🔵 **Why this is a trend and not a bug report.** This base has recorded index/payload disagreement four passes running — `663` (MIT), `664` (AGPL-3.0), `665` (EUPL) — each time as an instance of `NOASSERTION`. p666 enumerated a single owner and found **three distinct mechanisms** in one pass, two of them in the opposite direction to `NOASSERTION`. Grouping them under one name was the error.

| Mechanism | Instance at p666 | `gh api` says | The payload says | Direction |
|---|---|---|---|---|
| **1. Pointer, not grant** | `Opetushallitus/koski`, `varda`, `ludos`, `eperusteet-ylops`, `kouta-backend`, `oph-design-system` — short `"Licensed under the EUPL, Version 1.x"` references of `295`–`653 B` | 🔴 `NOASSERTION` | 🟢 EUPL-1.1 / 1.2-or-later | **under**-reports a real grant |
| **2. Appendix capture** | `Opetushallitus/compleap` — the **full** EUPL v1.2 text, **`13,957 B`** 🔧 (p674; published as `13,956 B`) | 🟢 **`EUPL-1.2` — correct** | 🟢 EUPL-1.2 | 🔴 **the *classifier* fails, not the index**: a keyword reader matches `GNU Affero General Public License` **inside the EUPL's compatibility appendix** and returns `AGPL-3.0` |
| **3. Phantom grant** | `amandasiqueirasouza1-ux/ia-para-professores` | 🔴 **`MIT`** | 🔴 **no grant file at any of five standard paths** | **over**-reports an absent grant |
| **4. Family slip** | `Ignacio-Ghub/asistente-docente-sin-conexion` | 🔴 `GPL-3.0` | 🟠 **AGPL-3.0** (`35,148 B`, full text) | wrong **family**, and the difference is network copyleft |

🔴 **Mechanism 2 is the one that will cost this base money, and it is self-inflicted.** `NOASSERTION` is *visibly* unhelpful — it asserts nothing, so a pass goes and reads the file. **An appendix-captured classifier is confidently wrong**, and it is wrong about precisely the licence family `verticals/solutions.md` has just started carrying. 🟢 **The remedy is one line of discipline: bind the verdict to the payload's opening declaration, not to any licence name occurring anywhere in it.** The EUPL declares itself on line 1 (`EUROPEAN UNION PUBLIC LICENCE v. 1.2`) and then spends a page naming the licences it is compatible with.

🔵 **And `665-H` narrows.** p665 inferred from `7/7` `NOASSERTION` that the API *hides the EUPL family*. It does not: it reported `EUPL-1.2` correctly for the one repository that ships the full text, and it was the **only** SPDX it reported in `100`. **`NOASSERTION` tracks the payload's form, not its family** — an index can classify a licence and cannot classify a pointer to one.

🟢 **The operational consequence for a client engagement.** Any licence posture built from a repository-metadata API — an SBOM tool, a procurement scan, a compliance dashboard — inherits all four mechanisms. For European public-sector education code specifically, mechanism 1 is the *common* case: **the default reading of a ministry's repository is "no licence", and the truth is usually EUPL.** Read the file.

## T48 — A national education ministry is an organisation, not a repository set, and the search leg returns its newest member 🟢 new at p666

🔵 **Twice measured, same shape.** `p660` read a search leg's account of `scratchfoundation`'s permissive options, enumerated the org instead, and found a **whole BSD-3-Clause product** (ScratchJr) in it. `p665` read a search leg's account of `Opetushallitus` and published *"seven repositories in which a national education ministry runs its production learner stack in public"*. p666 enumerated the org: **`182` repositories, `52` pushed in the last ten weeks.**

🔴 **The systematic bias, and it is not random.** The member the search leg missed is not an obscure one — [`koski`](https://github.com/Opetushallitus/koski) at **`23★` and 12 forks** is the **most-adopted education-domain repository in the organisation**, and it is the *incumbent* system in the very domain whose `0★` newcomer (`suorituspalvelu`) p665 did file and described as *"the credential-records end"* of the family. 🔵 **Freshness-ranked discovery surfaces what was created or pushed most recently and most visibly; a public body's crown jewels are old, boring, and named in Finnish.**

🟢 **What the enumeration added that no amount of searching would have.** The early-childhood register (`varda`) — a tier `p660` went looking for and reported as unsupplied. The **local**-curriculum authoring tool (`eperusteet-ylops`) — without which p665's national-curriculum row is half a story, because deployments ground against local curricula. The matriculation-exam content service (`ludos`) — against a standing assessment gap. **None of the three was returned by any search leg in this base's history; all three are production services pushed this week.**

🔵 **So the channel rule, stated for the next pass:** when a row's owner is an institution rather than a person — a ministry, an agency, a university, a foundation — **enumerate the owner before writing the row, and write the org's size into the cell.** A family size that is really a page size is a claim this base has now published twice.


## T49 — Retention is a layer, not an algorithm: the sector's one "proven" primitive sits on a dense permissive field with a choice of objective function 🟢 new at p667

🔵 **What T13 said, and why it was true and incomplete.** **T13** has recorded for many passes that spaced repetition — specifically FSRS, via `fsrs4anki` and `fsrs-rs` — is *"the one permissive education algorithm that is already in production"*. Every word of that holds. What it also did was end the conversation: a client asking how generated material is made to stick got a single answer and no trade-off, and this base carried retention as **one point** rather than a layer.

🟢 **p667 mapped the field underneath it, and it is dense.** Sixteen rows filed to `repos/foundations.md` in one pass, all permissive, all with the grant payload read at first hand:

- **A published alternative scheduler.** [`maimemo/SSP-MMC`](https://github.com/maimemo/SSP-MMC) (MIT, `227★`) solves for the **stochastic shortest path** to a target recall — it minimises *total review cost to mastery*, trained on MaiMemo's own large-scale learner data. FSRS optimises predicted recall; SSP-MMC optimises cost. **These are different objective functions and both are permissive and published.**
- **The peer-reviewed optimum the heuristics approximate.** [`Human-Centric-Machine-Learning/memorize`](https://github.com/Human-Centric-Machine-Learning/memorize) (MIT, `190★`) is the code **and the real data** for *Enhancing Human Learning via Spaced Repetition Optimization*, **PNAS 2019**.
- **Clients in every delivery form.** `olmps/memo` (BSD-3, **`1,870★`**, Flutter → iOS/Android/desktop), `shaankhosla/repeater` (Apache-2.0, terminal), `lakesare/memcode` (MIT, web, ten years of history), and three Obsidian-native systems — `ctrlaltwill/LearnKit`, `kitschpatrol/yanki-obsidian`, `bjsi/incremental-writing`.
- **The write primitive.** [`repeat-space/anki-apkg-export`](https://github.com/repeat-space/anki-apkg-export) (MIT, `182★`) produces a `.apkg` deck **file** with no Anki installed, completing the pair with `anki-mcp-server`, which drives a *running* instance.
- **A different primitive entirely.** `bjsi/incremental-writing` and `campfirium/foliole` schedule **engagement with long material** in prioritised queues rather than retrieval of atoms — a job no flashcard scheduler does.
- **And content.** `nastaso/cloudcertprep` (MIT, `246★`) is a **1,469-question** permissive item bank for AWS CLF-C02 and AIF-C01.

🔴 **The trend is not "there is more of it".** It is that **retention stopped being a library choice and became an architecture choice**, with four decisions a studio now has to make explicitly: the objective function (recall vs cost-to-mastery vs the PNAS optimum), the primitive (atom retrieval vs incremental reading), the delivery form (mobile, web, terminal, vault-native, or a deck file handed over), and whether the item bank is generated or adopted.

🟢 **Why three of these rows matter beyond retention.** `yanki-obsidian`, `LearnKit` and `incremental-writing` keep the cards as **plain Markdown in a repository**. That makes generated learning material reviewable in a pull request and version-controlled — which is the provenance and governance answer that **T3** identifies as the buying trigger and that regulated buyers in EMEA, and increasingly North America, ask for by name. The retention layer turns out to be where the auditability argument is cheapest to satisfy.

🔵 **Read the staleness, not just the stars.** Four of the sixteen have not been pushed in over a year and two (`incremental-writing`, `memorize`) are effectively finished work; `microsoftarchive/Learn-LTI` is formally `archived`. Each row on `repos/foundations.md` states its push date and says whether it is a dependency, a codebase to adopt, or a design reference. In this layer specifically, "finished" is often the correct state for an algorithm implementation and a disqualifying one for a client application — and the rows distinguish the two.

## T50 — The student-information layer is where open source education software stops being permissive and stops being adopted at the same time 🟢 new at p668

🔵 **This base has measured the tutor layer, the delivery layer, the retention layer, the assessment layer, the credential layer and the interoperability layer. The *record-keeping* layer — the system of record that actually runs a school — turns out to behave unlike all of them, and p668 has the numbers.**

**The layer is small.** GitHub's own topic counts, read at `2026-11-05`: `lms` → **`2,646`** tagged repositories, `ai-tutor` → **`880`**, `student-information-system` → **`193`**, `intelligent-tutoring-system` → **`45`**. The SIS layer is an order of magnitude thinner than course delivery, and it is thinner than *AI tutoring*, a category that did not exist four years ago.

**Its head is copyleft, with exactly one permissive member.** The three most-adopted members, all already on this base's shelves:

| Repo | Stars | Licence | Note |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `652` | **GPL-2.0** | The topic's `#1`. School management, PHP. Default ref **`mobile`** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | `411` | 🟢 **MIT** | **The only permissive member of the head.** Laravel + Filament |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `349` | **GPL-2.0** | Multi-institution, PHP |

**And its tail is both unadopted and unlicensable.** `11` of the topic's top `20` were addresses this base had never recorded — but **every one sits at `≤20★`**, and the three most plausible, byte-read at their real default refs, are `AGPL-3.0` (`MeetPlan/MeetPlanFrontend`, `34,523 B`), `GPL-3.0` (`ClassyCreations/ScheduleCheck`, `35,069 B`) and **no grant at all** (`LindungiLw/student_information_portal`, `404` on four payload names).

🔴 **Why this is a trend and not a gap.** Every prior "no permissive supply" claim this base tested turned out to be an **adoption** gap — `T40` says so, and it has held six times. The SIS layer is the first one where **both** variables fail together: the permissive supply is a single 411-star repository, and the copyleft supply is where all the adoption is. That is a different market, and it has a different consequence.

🟢 **The consequence for an engagement.** On every other layer this base tracks, the move is to take a permissive component and build on it. Here there is **no permissive system of record to build on at any scale** — so a client who needs AI inside the system of record is choosing between (a) building on `academico` (MIT, real, but 411 stars of external review for software that holds student records), (b) integrating *alongside* a GPL SIS across a process boundary and keeping the derivative question off the table — the `P27`/`P36` licence-provenance work is the gate for this — or (c) treating the SIS as a data source and putting the AI in the layer above it, which is where the permissive supply actually is. 🔵 **Option (c) is the one this base's shelves can staff today, and the reason to say so is that options (a) and (b) both look cheaper on a slide and are not.**

**Caveat, stated:** the `11`-of-`20` novelty figure measures *this base's* coverage of a topic page, not global supply, and the topic-page channel reads only the first 20 of 193. The licence readings are first-hand and the star counts are GitHub's own as displayed on `2026-11-05`.


## T51 — The licence boundary has moved out of the repository and into the run-time download, and a manifest-derived SBOM can no longer see it 🔴 new at p670

**The claim.** This base has said since p666 that *a licence identifier is not a licence* (**T47**), and `agents/top.md` has carried a section arguing that **the licence unit is the dependency graph, not the repository**. p670 found an instance that breaks even that: a product whose copyleft dependency is **neither declared, vendored nor pinned in any manifest**, because it is **fetched after installation**.

**The evidence, measured this pass.** [`DaRL-GenAI/instructional_agents_studio`](https://github.com/DaRL-GenAI/instructional_agents_studio) is MIT in full — payload `1,093 B`, `sha256₁₂ 338aae8b3c7c`, read at the real default ref. It ships `123` tracked files. **Nothing in the repository would fail a licence scan.** Its `NOTICE` then states that the slides and documents editor **is not in the package**: the application downloads it on first use into `~/.cache/instructional-agents/editor/<version>/`, verifies a SHA-256, and serves it to the browser — a trimmed build of [`ranuts/document`](https://github.com/ranuts/document) embedding **ONLYOFFICE `sdkjs` and `web-apps`**. **Both verified independently at p670 rather than taken from the NOTICE: `ranuts/document` is AGPL-3.0 (`2,018★`, pushed `2026-11-03`); `ONLYOFFICE/sdkjs` is AGPL-3.0.**

🔴 **So a client SBOM generated from the manifest reports this product as MIT, and it is wrong.** Not through concealment — the `NOTICE` is explicit and even explains the Section 7 additional terms and where the corresponding source is published. **The disclosure is in a file almost nobody reads, and in the one format no tool parses.**

🔴 **The second half of the same mechanism is a data-residency finding, not a licence one.** When the editor download is absent, the app falls back to a **hosted editor at `edit.chaxus.com`** — a third-party domain, named in the shipped `bin/cli.mjs`. The product's pitch is that the API key and the data stay in the browser. **The documents can leave to a third party by default.** For the EMEA public-sector and LATAM budget conversations this base tracks, that is the first question a buyer asks, and the honest answer is not the one on the README.

🔵 **Why this is a trend and not an anecdote.** The shape is a consequence of how 2026 education tooling is built, not a quirk of one lab. Browser-only, bring-your-own-key agents are the fastest route to a demo that installs nothing — which is exactly why this row was worth filing — and the heavyweight parts they cannot ship in a `123`-file static bundle (document editors, model weights, speech engines) get fetched at run time instead. **Every one of those fetches is a licence and egress decision made after the scan.** This base has already flagged the same shape once on weights: `wordlink` grants MIT on its *code* and names no licence for its released model.

**The rule, stated so it is not re-derived.** 🟢 **Read the `NOTICE`, not only the `LICENSE`, and ask what the artefact downloads on first run.** Add it to the triage in `compose/patterns.md` **P36**; the remediation — keep the MIT shell, replace the editor — is **P39**.

**Confidence.** 🟢 **High on the facts** — all four licence readings and the `bin/cli.mjs` reference were taken first-hand this pass. 🟡 **Medium on the generality**: one measured instance of the run-time mechanism, plus one adjacent instance on weights. **It is filed as a trend on the strength of the mechanism being structural, and the next pass should test it by counting how many shelf rows download anything on first run** — a question no pass has yet asked.

## T52 — The addresses rot faster than the software, and every integrity check the industry runs is blind to it 🆕 new at p671

**The claim.** An open-source education dependency can change *stewardship* — move from an individual maintainer to a standards body, or be renamed under its own foundation — while every automated check an engagement runs on it keeps passing at the old address, indefinitely. The URL stays live, the licence payload stays byte-identical, the default branch still resolves. **Nothing in the ordinary toolchain reports that the thing you are depending on is now owned by someone else.**

**The evidence, measured first-hand at `p671` on this base's own `197` shelf addresses.**

| Old address | New address | What proves identity | What still answers at the dead address |
|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform)** | identical `HEAD` `78b892c6a`; licence payload **`sha256` identical** (`e12d78569742`, `35,136 B`, AGPL-3.0) | `git ls-remote --symref` → `refs/heads/master`; `raw.githubusercontent.com` → `200`; the full AGPL grant |
| [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | **[`daisy/MathCAT`](https://github.com/daisy/MathCAT)** — the **DAISY Consortium** | identical `HEAD` `c6bba2f3a`; MIT `1,065 B`, *Copyright (c) 2022 NSoiffer* unchanged across the move | `git ls-remote --symref` → `refs/heads/main`; `raw.githubusercontent.com` → `200`; the full MIT grant |

**`2` of `197` addresses — `1.0%` — and both moved in the same direction: toward an institution.** An individual maintainer's accessibility library is now held by the accessibility standards body; a platform is now named after its own foundation. That direction is the substance of the trend, because **stewardship is what licence and governance risk actually track.** A row that reads *"MIT, maintained by an individual"* and a row that reads *"MIT, held by the DAISY Consortium"* carry the same licence and completely different answers to *who will still be maintaining this in three years*, which is the question a client asks.

🔴 **Why the toolchain cannot see it.** GitHub honours a rename redirect **indefinitely**. So the three channels this base — and essentially every SBOM, dependency audit and link checker — uses as proof of life all keep answering at the dead address: existence (`git ls-remote`), payload (`raw.githubusercontent.com`), and licence (the grant bytes, which are *identical*, not merely similar). 🔵 **The only channel that distinguishes them is the search index, and only as an error**: `repo:<old>` returns `422`, and `user:<owner>` returns `≥1`, so the address is unresolvable while its owner is fine. That pair is the detector (`repos/trending.md` `671-J`).

🔴 **And the second specimen shows how long this survives undetected in practice.** `p526` published the Open edX rename on **2026-10-29**. The correct address had been in `evidence/address-ledger.tsv` since **`p28`**, never filed. `p671` — **145 passes later** — still found the dead slug on `9` places across `3` live pages, including a component table that also still called the AGPL platform `Apache-2.0`. **The rename was not missed. It was published and not propagated.**

🔵 **What follows for an engagement, concretely.** An open-source inventory built on URL liveness is not an inventory of *what you depend on*, it is an inventory of *what still answers*. Add the `422`/`user:` pair to the audit (see **P40**), and treat a rename as a governance event rather than a link fix: re-read the grant at the new address, re-check the copyright holder, and ask who the new owner is before assuming the licence means what it meant.

**Confidence.** 🟢 **High on the facts** — both renames proven at `HEAD`-sha and licence-payload level this pass, the detector controlled on `18` probes at both signs. 🟡 **Medium on the rate** — `2` of `197` is this base's shelves at one moment, not a sector-wide measurement, and `p671` makes no claim about the general rename rate in education open source. 🟢 **High on the blindness** — that `git`, `raw` and the licence bytes all pass at a dead address is not an inference, it is what was measured.


## T53 — Every instrument that reads a licence agrees on the family and disagrees on the terms that decide usability 🆕 new at p672

🔴 **The finding.** Run three independent licence readers over one repository and they return three answers that are all "about" the same licence and are not interchangeable. On `July-Tea/EssayMate` at p672: `gh api` said **`NOASSERTION`**; this repository's own `ingest/probe-grant.sh` said **`CC-BY-4.0`**; the byte read said **`Attribution-NonCommercial-ShareAlike 4.0 International`**. Only the third is correct, and the difference between the second and third is the entire commercial question — `NC` forbids the derivative, `SA` forces reciprocity, and a label of `CC-BY-4.0` implies neither.

🔵 **Why this is a trend and not a bug report.** The three readers fail in three different, structural ways, and all three are in production across the industry:
- **A classifier that does not match emits a null** (`NOASSERTION`). `p658` established this means *"the classifier did not match"*, never *"no licence"* — but it is routinely rendered as "unlicensed" in dependency dashboards, which is a **false negative** that blocks usable software.
- **A classifier that normalises to a family drops the modifiers.** This is the dangerous direction: `CC-BY-NC-SA` → `CC-BY` turns a non-commercial grant into a permissive-looking one. **A false positive on usability.**
- **A grader with an unvalidated reference text condemns correct payloads.** `672-B`: a canonical MIT reference missing the words `THE USE OR` reported `4` of `4` verbatim payloads as mutated.

🔵 **The structural reason it keeps happening: a licence is not a label, it is a *conjunction of terms*, and every layer between the file and the dashboard is lossy by design.** SPDX identifiers compress well for permissive licences, where family and terms coincide, and badly for everything with modifiers — Creative Commons variants, dual grants, split grants by material type (`542-A`), run-time grant boundaries (`T51`). The compression is invisible because the output still looks like a licence.

🟡 **What is genuinely hard here.** You cannot byte-read every grant in a real dependency tree; classifiers exist because the volume demands them. So the usable rule is not "never use a classifier" but **"a classifier may triage and may never decide"**: let it rank, and byte-read the payload of anything you intend to *ship on*, anything it labels with a family that has modifiers, and anything it labels null. That is tens of reads, not thousands.

🔵 **For an engagement.** The inventory question a client asks is *"what are we allowed to do with this?"* and the artefact most tools hand back answers *"what family is this in?"*. Those come apart precisely on the licences that restrict commercial use — which is to say, precisely where the answer matters. **A licence column in an SBOM is a triage field, not a finding**, and the deliverable that is worth money is the short list of payloads actually read.

**Confidence.** 🟢 **High on the mechanism** — three readers, one payload, three answers, all four reproduced first-hand at p672 with the byte read as ground truth (`20,849 B`, `sha256₁₂ 1349a4b61484`), and the reference-text defect reproduced at both signs on five further payloads. 🟡 **Medium on the breadth claim** — the three failure modes are each evidenced here on one or two specimens, not surveyed across a corpus; the *family-collapse* mode in particular is demonstrated on Creative Commons and is predicted, not shown, for dual and split grants.

## T54 — The interoperability layer is where open source education software is still permissive, and it is specification-complete 🆕 new at p673

**`T50` established the floor:** the **student-information layer** — the system of record — is where open source education software stops being permissive (GPL-2.0 `i-educar`, LGPL-3.0 `fenixedu-academic`, AGPL-3.0 Open edX) *and* stops being adopted at scale. That trend has held for `25` passes and is not revised here.

**`T54` is its corollary, and it is the more useful half:** the layer **immediately above** the SIS is almost entirely **MIT / Apache-2.0 / ECL-2.0**, and every standard in it has a working permissive implementation this base has now read byte-for-byte:

| Standard | What it carries | Permissive implementation | Licence (byte-read) |
|---|---|---|---|
| **LTI 1.3 / Advantage** | launch, identity, roles, course context, grade return | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 (`11,361 B`) |
| **xAPI** | learning-activity records | [`openfun/ralph`](https://github.com/openfun/ralph) | MIT (`1,094 B`) |
| **xAPI + Caliper (warehouse)** | institution-scale analytics store | [`Apereo…/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **ECL-2.0** (`9,878 B`) |
| **OneRoster 1.2** | rosters, enrolments, classes | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) · [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) | Apache-2.0 · MIT |
| **QTI 3** | portable assessment items | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | MIT (`1,072 B`) |
| **Open Badges** | verifiable credentials | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 (`13,185 B`) |
| **(evaluation)** | randomised trials in a live course | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | Apache-2.0 (`11,323 B`) |

🟢 **Why this changes the engagement shape.** The integration surface has historically been the expensive, bespoke, re-written-every-time part of an education project, and the copyleft SIS underneath it has been treated as the blocker. `T54` says the blocker is routable: **nobody has to relicense or replace the system of record** — the work is to put a permissive, standards-conformant **adapter** in front of it. `edfi-oneroster` is the specimen: a OneRoster 1.2 API served from an Ed-Fi ODS, Apache-2.0, `6★`. Adoption is negligible and that is the point — this layer is **specification-driven, not popularity-driven**, so a six-star repository implementing a certified standard is a safer dependency than a six-thousand-star one implementing nobody's.

🔴 **The cost this trend carries.** These components are **maintained thinly**: `OpenLRW` ~14 months stale, `openbadges-validator-core` ~12, `OneRoster.NET` **three years**. Permissive and specification-complete does **not** mean actively maintained, and every one of those rows is filed with its staleness as a headline rather than a footnote. The correct reading is *fork base*, not *dependency* — and that maintenance cost belongs in the estimate.

🟡 **Standing prediction, falsifiable:** if `T54` is right, the next genuinely novel education supply this base finds will be **adapters and evaluators**, not tutors. `p673` found `9` of the former and `0` of the latter from the same eight legs that have returned tutors for `25` passes.

## T55 — The licence label from an index is now wrong in both directions on this base, and only the byte read is load-bearing 🆕 new at p673

**`T47` recorded three mechanisms by which an index and a payload disagree. `T53` sharpened it: every instrument agrees on the *family* and disagrees on the *terms that decide usability*. `T55` closes the loop by establishing the two signs, measured one pass apart:**

- 🔴 **Fails UNSAFE — understates restrictions.** `672-D`: `July-Tea/EssayMate` is **CC BY-NC-SA 4.0** (NonCommercial — it bars the commercial derivative this KB exists to scope). `gh api` said `NOASSERTION`; this repository's own `ingest/probe-grant.sh` said **`CC-BY-4.0`**, collapsing the family and dropping both the `NC` and `SA` terms. A pipeline trusting either label ships a grant it must not.
- 🔴 **Fails by HIDING SUPPLY — overstates restrictions.** `673-B`: three `NOASSERTION` labels in one pass, decomposing into **three unrelated mechanisms, all permissive** — a **split grant** whose scope preamble precedes verbatim MIT (`pupilfirst`), an **OSI-approved licence the classifier does not know** (`OpenLRW` → ECL-2.0), and a **verbatim Apache-2.0 body with the `APPENDIX` stripped** (`feedbacksystem`, `−524` normalised). A pipeline filtering on `spdx_id` discards all three.

🟢 **The operational rule, and it is cheap:** **never filter candidates on `license.spdx_id`.** Treat `NOASSERTION` as an instruction to **byte-read**, not as a verdict. Read the payload from `raw.githubusercontent.com` at the **real default ref** — which `p673` found to be `master`, `development`, `develop` and `dev` for four of its `18` candidates, so reading at `main` would have returned `404` and been recorded as *no licence*.

🔴 **And grade by normalised diff, not by length or hash.** `673-A`: `UniTime/unitime`'s payload is **`11,357 B`, the canonical Apache length exactly**, and hashes differently — a blank line added at byte `0` and the trailing newline dropped, `+1` and `−1` cancelling in length but not in hash. `671-R` said *hash, do not count*; `673-A` adds that **hash alone condemns an honest grant**. Length-equality is not identity; hash-inequality is not mutation. Both are descriptors; the normalised diff is the verdict.

## T56 — A published byte count can be an artefact of how it was read, and a stripped digest makes different payloads look identical 🟢 new at p674

**Evidence.** p674 re-measured every byte cell over `7 000 B` on this base's three sell shelves — `69` cells across `59` repositories. **`62` reproduce exactly.** Five are short by precisely their payload's **trailing-newline run**, which is the `P834` signature: a payload read into a shell variable loses its *entire* trailing newline run, so the count and the digest both describe bytes that are not what the repository serves.

🔴 **One case is proven rather than inferred, and it is the one that matters.** `Opetushallitus/compleap` was published as `13 956 B` with `sha256₁₂ 900a5a8a3c56`. The payload is **`13 957 B`** (`922e7e3be8ed`), and `900a5a8a3c56` is **the digest of the stripped bytes**. When *both* halves of a cell — size and hash — come from the capture, the cell is internally consistent and still wrong. 🔵 **A self-consistent cell is therefore not a verified cell**, which is the part that generalises.

🔴 **The consequence is worse than an off-by-one, because stripping DESTROYS DISTINCTIONS.** This base published *"`34,522 B` each"* across three AGPL-3.0 rows. Measured: the two `blend-ed` repositories are **`34 524 B`** (digest `8d56b405468a`, trailing run `2`); `openedx/openedx-ai-extensions` is **`34 523 B`** (`8486a10c4393`, run `1`). They are **different payloads**. All three collapse to the same `34 522 B` text (`20b067f86de3`) only *after* stripping — so the published figure did not just understate three sizes, it **manufactured a three-way identity that does not exist in any tree.** A byte count whose discriminating power has been stripped out of it cannot do the job a byte count is carried for.

🟢 **The fix that makes the numbers safe to read again is a digest, not a bigger number.** `11 357` is **simultaneously** the `apache/.github` canonical size and the *stripped* size of the `apache.org` canonical, so a cell reading `11 357 B` cannot be typed from its number alone. With both canonicals pinned — `11 357` / `58d1e17ffe51` and `11 358` / `cfc7749b96f6` — `numbas/Numbas` at `11 357 B` is demonstrably **correct** and `oppia/oppia` at `11 357 B` is demonstrably **wrong**, a distinction that was unavailable one pass ago.

🔵 **Why this is a sector trend and not merely housekeeping.** This base sells *licence certainty*: the byte count and digest exist so a client can confirm that the grant in a deliverable's dependency is the grant that was audited. An artefact in that figure attacks the one claim the artefact was introduced to support. 🔴 **And the defect was in the published cells, not in the library** — this repository's own `lib/payload_measure.sh` carries the correct primitive *and* predicted, in its own header, the environment denial that stopped p674 from sourcing it. **A control that exists but is not the only path to the number is not yet a control.**

⚠️ **Scope, stated plainly: a trailing-newline error changes the SIZE and the DIGEST, never the FAMILY.** Every licence *family* verdict this base has published stands. Only byte counts and hashes moved, and only in the five cells named.

## T57 — A grant verdict without a quotation cannot be audited, and the sector's corpora are where that costs money 🆕 new at p675

**Confidence: high — read at every author repository in the chain, both corpora, both releases.**

🔵 **`T21` and `P957` got the direction right:** as AI work moves from code to code-plus-evaluation-data, licence risk migrates to the corpus. 🔵 **And `P1007` got the channel right:** *"a corpus's licence is stated by its AUTHOR's repository, never by its funder's or distributor's page."* 🔴 **What p675 found is that the verdict recorded beside `P1007` is the opposite of what that channel says.**

| Corpus | Author's own repository | Grant, verbatim | Licence file |
|---|---|---|---|
| **PERSUADE 1.0** | [`scrosseye/PERSUADE_corpus`](https://github.com/scrosseye/PERSUADE_corpus) `main` @ `6b69a55c9d36` | 🟢 **CC BY 4.0** (README `3,486 B`, sha256₁₆ `809c25c2379d639e`; ⚠️ grant sentence ends in a truncated `…d.en)` link fragment) | 🔴 none |
| **PERSUADE 2.0** | [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0) `main` @ `5bdbad1175d1` | 🟢 **CC BY 4.0** (README `2,081 B`, sha256₁₆ `2f984c8712650050`) | 🔴 none |
| **CLEAR** *(same author)* | [`scrosseye/CLEAR-Corpus`](https://github.com/scrosseye/CLEAR-Corpus) `main` @ `dbf1cf0df30b` | 🔴 **CC BY-NC-SA 4.0** (README `1,795 B`, sha256₁₆ `44d9d46bbd540d39`) | 🔴 none |

🔴 **`Gap 390` / `T21` has carried *"PERSUADE 2.0 is `CC-BY-NC-SA-4.0` by its author's own repo"* since p57. Two author repositories say `CC BY 4.0`. The `NC-SA` sentence is real and belongs to the author's *other* corpus** — same single-sentence construction, same author, one token apart. 🔵 The redistributor (`learning-commons-org/evaluators`, `LICENSE.md` `1,615 B`) makes the same substitution in a claim *about* upstream, linking to the repository that contradicts it.

🟢 **The trend, which is the mechanism and not the two data points.**

1. **A verdict without a quotation is unauditable.** `P1007` named the right channel and recorded no quoted payload, so for 618 passes there was nothing for a successor to check the verdict *against* — only a citation to re-trust. 🟢 **Every grant cell on these shelves now carries bytes and a digest; grant *prose* must carry the sentence.**
2. **The error ran in the safe direction, which is why nothing surfaced it.** Over-restrictive licence errors produce no ticket, no breach and no complaint — only work that was never proposed. 🔴 **It is the one class of licence error that is invisible by construction**, and this sector's corpora are where it bites, because the corpus is the valuable half.
3. **Corpora have no licence file.** All three repositories here grant in README prose; six licence filenames `404` on each; GitHub detects no licence on any. 🔵 **SPDX classifiers, `licensee`, SBOM tooling and GitHub's own label all return nothing**, so the only working reader is a person reading a sentence — and `P965`'s inverse shape (a grant with no file) is now three instances strong.
4. **The grant is detached from the bytes it governs.** The data is on Google Drive, not in the repositories. A README can be edited and a link replaced. 🔴 **A corpus grant can only be pinned by pinning the commit of the sentence that makes it** — which is what `P45`'s evidence pack must now do for data rows, and `P46` does.
5. **Sibling artefacts by one author are a contamination channel.** Two corpora, one author, near-identical grant sentences, different terms. 🔵 **Read the grant on the row you are filing, never on its neighbour.**

🟢 **Commercial consequence, stated once.** An automated writing evaluation product **can** be trained on PERSUADE under attribution alone — `P46` wires it. CLEAR **cannot** be shipped, and `SA` reaches derivatives including fine-tunes. 🔵 **`P675-A`: a grant verdict must quote the payload it came from.**

## T58 — 🔄 `T273`'s channel alias reproduces a third time, and the arm that had never been graded is this base's own `Ref` **column** 🔄 re-measured at p675

**Confidence: high — four fresh positives, the asymmetry control re-run, and a 61-repository sweep of an arm the existing census cannot see.**

🔵 **This is not a new finding and p675 nearly filed it as one.** The mechanism is already this base's `T273` (p273), re-stated as `T429` and `Gap 419-B`, and it already has a standing instrument — `make gate-branch-alias` (p428, **36 assertions over 26 controls**), which 🟢 **was run at p675 and PASSES**. 🔴 **Recording the near-miss, because it is the same defect class the base keeps finding in itself:** a measurement was made, it was correct, and it was about to be published as novel because the prior pass's record lived under a different name.

🟢 **What p675 adds is evidence, not a claim.** Four fresh positives for the alias, and the asymmetry `T273` left as *"mechanism NOT established"* re-run on both signs:

| Probe | Repositories | `raw…/master/…` | `raw…/main/…` | arbitrary ref |
|---|---|---|---|---|
| **`main`-only** (no `master` head) | `scrosseye/CLEAR-Corpus` (single ref), `scrosseye/persuade_corpus_2.0` (single ref), `HKUDS/DeepTutor` (11 heads), `learning-commons-org/evaluators` (44 heads) | 🔴 **`200`**, default-branch bytes | — | 🟢 `404` |
| **`master`-only** (no `main` head) | `CAHLR/pyBKT`, `adlnet/xAPI-Spec`, `chamilo/chamilo-lms`, `numbas/Numbas` | 🟢 `200` (genuine) | 🔴 **`404`** | 🟢 `404` |

🟢 **The asymmetry is confirmed on 8 repositories at both signs: `master` is aliased to the default branch, `main` is not.** 🔵 So it behaves exactly like GitHub's legacy redirect for repositories renamed away from `master`, and not like a general fallback — arbitrary names `404`.

🟢 **And the genuinely new arm.** `Gap 428-D` declared, on the pass that built the gate, that `branch-alias-census` *"grades PATHS and cannot see the PROSE that qualifies them"* — it inspects published `raw`/`blob` URLs. 🔴 **The `Ref` column of the three sell shelves is prose, so it has never been graded by anything.** p675 graded it: **`70` `master` cells over `61` distinct repositories** across `agents/top.md` (1), `repos/foundations.md` (44) and `verticals/solutions.md` (25), each re-resolved with `ls-remote --heads` plus `--symref HEAD`.

> 🟢 **`61 / 61` MASTER-EXISTS, `master` the default in every case, `0` corrupted cells, `0` unreachable.**

🟢 **That is the useful outcome and it closes an exposure rather than opening one:** the alias is live on the channel this base reads payloads with, it had an ungraded arm, and that arm is clean. 🔵 **`P675-B`: a ref is established by `ls-remote`, never by a `raw` `200` — which is `ACTION p419-B`'s instruction, now also applied to the `Ref` column and not only to published paths.**

## T59 — The ledger addresses a payload; it does not grade one — and this base's own backlog column is wrong in the unsafe direction 🆕 new at p676

**What was measured.** `p665` established, and `p673` confirmed across `16` of `16` filed addresses, that this base's yielding supply channel is its **own backlog**: `evidence/address-ledger.tsv` carries **`3,032`** addresses with `filed_on = -`, of which **`1,497`** have a recorded verdict in the permissive family. The ledger also carries a `last_verdict` column. Promoting from the backlog *on that column* is the obvious economy — the licence is already measured, and working a backlog off its own index is what a backlog is for.

🔴 **`p676` re-read the grant payload for the `5` best-tracked backlog candidates against their ledger verdict. Two contradicted it. Both contradictions point the wrong way.**

| Address | Ledger verdict | Payload, re-read at the real default ref | `p555` grader | Direction |
|---|---|---|---|---|
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | **`MIT`** since `p12`, `7` passes | **Fair Code License** on the **Sustainable Use License** — not OSI; Leemons Edtech Solutions SL, Madrid | **SUBSTANTIVE** | 🔴 **UNSAFE** |
| [`beltromatti/get-it`](https://github.com/beltromatti/get-it) | **`Apache-2.0`** since `p123`, `9` passes | **modified Apache-2.0** — §6 trademark clause rewritten | **SUBSTANTIVE** | 🔴 **UNSAFE** |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | `GPL-3.0｜Apache-2.0` since `p14` | **MIT**, verbatim, © *2016 Public Consulting Group* | **COSMETIC** | 🟢 safe — hid supply `6` passes |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | `MIT` since `p90`, `19` passes | **MIT**, verbatim | **COSMETIC** | 🟢 correct |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `GPL-2.0` since `p2`, `27` passes | GNU GPL, `15,214 B`, not verbatim against canon | **SUBSTANTIVE** | 🟢 correct in family |

**Why this is a trend and not a bookkeeping note.** `T55` established at `p673` that *the licence label from an index is wrong in both directions*. `T59` is the same defect **one level in** — the index that is wrong is now **this base's own**, and it is the index the base had just finished identifying as its most productive channel. `p673-B` found `NOASSERTION` concealing permissive supply (failing **safe**, costing opportunity). `T59` finds the ledger concealing **restricted** supply (failing **unsafe**, costing a client). The two are not symmetric: one loses a row, the other ships an AGPL-or-worse dependency into a commercial derivative.

🔧 **The operative rule, and it is cheap:** *re-read the grant payload at the real default ref, every time, for every promotion.* It cost `29` `git ls-remote` calls and `29` `raw.githubusercontent.com` reads for this pass's whole candidate set — roughly one minute of wall-clock — and it is the only step that caught either error.

🔵 **What a reader should take from this about the KB itself.** Every licence cell on the four curated shelves now carries a byte count and a `sha256₁₂`. Those are not decoration and they are not provenance theatre: they are the record that *someone opened the file*. A row without them is a row that inherited its verdict, and after `T59` an inherited verdict is a claim, not a measurement.


## T60 — `T50` survives as a *scale* statement and dies as a *tier* statement: the permissive student-information layer exists, at the size where most private education actually operates 🆕 new at p676

**`T50`, held for 28 passes, in its published form:** *the student-information layer is where open source education software stops being permissive and stops being adopted at the same time.* The evidence was consistent and it is still true at the top of the market.

🟢 **`p676` re-measured the tier rather than re-asserting it, and found the exception:**

| System of record | Licence | Stars | Scale it is built for |
|---|---|---|---|
| Open edX (`openedx/openedx-platform`) | 🔴 `AGPL-3.0` | — | national platforms, large universities |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` (`15,214 B`, re-read at `p676`; default branch 🔴 **`mobile`**) | **652** | districts, public K-12 |
| `i-educar` | 🔴 `GPL-2.0` | — | Brazilian municipal networks |
| `FenixEdu/fenixedu-academic` | 🟠 `LGPL-3.0` | — | universities |
| `AlekSIS` | 🔴 `AGPL-3.0` | — | German public schools |
| `foradian/fedena` | 🟡 refused at `p673` — three independent liveness signals failed | — | — |
| 🟢 [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **`MIT`** (`1,094 B`, `6051a15f4d44`, verbatim) | **411** | 🟢 **small and medium institutions, multi-tenant** |

**The narrowed claim, which is the useful one.** The copyleft wall in the system-of-record tier is real **where the buyer is a ministry, a district or a university** — institutions whose procurement produced those licences on purpose. It is **not** present at the tier below, where the buyer is a private school, a language school, a training centre or a franchise network, and where Academico is MIT, maintained and multi-tenant by design (`storage/tenants/<id>`).

🔵 **Why that distinction is commercially load-bearing for a studio.** `p673` established the `T54` pattern — *nobody has to relicense the system of record; the work is a permissive adapter in front of it* — which is the right answer for a ministry engagement and an expensive one for a 40-school private network. For the latter, `T60` says the system of record **itself** can be permissive, so the AI layer is built *inside* the tenant model rather than bolted onto an API in front of a GPL core. That is a materially shorter engagement and it is the segment with the shortest procurement cycle.

⚠️ **Bounded, and the bound is stated.** `411★` is one address. `T60` claims the tier is *not uniformly copyleft*; it does not claim a permissive SIS exists at every scale, and this base has found exactly one. The next pass should test the tier at the **training-centre / corporate-academy** scale, which neither `T50` nor `T60` has measured.


## T61 — A knowledge base fails at publication before it fails at research, and nothing in the pipeline reads the destination file 🆕 new at p677

**Confidence: high — measured, not inferred.** p677 audited `p597`'s promotion ledger — `11` addresses, each with a *“promoted to”* cell naming a shelf file — against the files those cells name. **`4` correct, `1` on a different shelf than claimed, `6` absent from every shelf.** And [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) was claimed-as-filed by **two passes `25` days apart** while absent throughout; `prometheus-eval` and `rubric`, claimed in the same breath, are in **none** of the eight shelf files.

🟢 **The measurements were sound.** All six absent payloads re-measured at p677 to **exactly** the byte counts the ledger published. **So the failure is not epistemic — it is clerical, and it is invisible precisely because the research half worked.**

🔵 **Why this is a trend and not an incident.** This base verifies licences byte-for-byte against the internet, re-reads payloads across passes, grades operative bodies and pins digests — an unusually rigorous apparatus, pointed entirely **outward**. It has **no check pointed at itself**: no pass has ever asked *“is the row I said I filed actually in that file?”* That asymmetry is structural in automated knowledge bases, because the external claim is the one that feels falsifiable. 🔴 **The cost is total for the affected rows:** an unpublished row and a wrong row are indistinguishable to the studio engineer who opens the shelf before an engagement.

🔧 **The remedy is `6` lines and no network:** for every *“filed to”* / *“promoted to”* cell, `grep -iF` the address against the path the cell itself names. Run today it finds all seven defects. **`ACTION p677-B`.**

🔵 **Generalises past this KB.** Any pipeline that writes a provenance ledger and a content shelf in the same run should treat the ledger as an **assertion about the shelf** — and assert it. A ledger never checked against its own target is documentation, not provenance.

## T62 — Re-deriving a count from the table fixes staleness and creates blindness to duplication 🆕 new at p677

**Confidence: high — measured.** Four separate passes repaired a *stale* row count on these shelves (`p658`, `p663`, `p668`, `p676`), and the remedy each time was **“re-derive by counting the table rather than incrementing.”** p677 measured a different way — extracting the address from the **subject column only** and looking for repeats:

| Shelf | Rows | Distinct subjects |
|---|--:|--:|
| `agents/top.md` | `59` | `58` |
| `repos/foundations.md` | `128` | 🟢 `128` |
| `verticals/solutions.md` | `61` | `58` |

**All four duplicate rows were created at p676**, each labelled *“New at p676”*, each on a repository its own shelf already carried (`OpenMAIC`; `OpenOlat` since p653; `Academico` since p664; `frappe/lms` earlier). **The counts are no longer behind the table; they are ahead of the inventory.**

🔵 **The mechanism is general: a remedy inherits the blind spot of the thing it measures.** Counting rows is a faithful measure of rows and is silent about subjects, so the fix for staleness cannot see double-counting — and the pass that re-derived the number correctly still published a wrong one. **A row count is not an inventory count.** 🔴 **The harm is not cosmetic.** The two `frappe/lms` rows give **opposite advice** — one recommends it, the p676 one flags it as AGPL-3.0 and not a build-on option — and a reader gets whichever row they reach first. The two `OpenMAIC` rows publish two different star figures for one repository in one table.

🔵 **Same family as `T56`, one level up.** `T56`: a published byte count can be an artefact of **how** it was read. `T62`: a published count can be an artefact of **what unit** was counted. In both the number is honest and the *question* was wrong. 🔧 **`ACTION p677-C`:** add the distinct-subject check to `ingest/derive-counts.py`. 🔧 **`ACTION p677-A`:** merge the four pairs, preserving both cells' facts.

## T63 — A correction verified on the channel that caused the defect is not a correction 🆕 new at p677

**Confidence: high — four payloads measured four ways.** `p674` correctly diagnosed that `11,357` is *also* the newline-stripped size of the `11,358`-byte Apache-2.0 payload, so the byte count alone cannot separate the two canonicals, and it added digests to pin them. **One of the two digests it published is itself a stripped-capture artefact:**

| Payload | Bytes | sha256₁₂ |
|---|--:|---|
| `apache.org` canonical, as served | `11,358` | `cfc7749b96f6` |
| `apache/.github` canonical, as served | `11,357` | **`c71d239df917`** |
| `apache.org` canonical, newline stripped | `11,357` | **`58d1e17ffe51`** ← published as the `apache/.github` canonical |
| `apache/.github` canonical, newline stripped | `11,356` | `43070e2d4e53` |

**Four distinct values; the page published two of them as the two canonicals, and both describe the same document.** The distinguisher names one canonical twice, so it distinguishes nothing.

🔵 **The operational cause is mundane and reproducible: a shell `$(...)` capture strips trailing newlines**, so any payload measured through command substitution is silently one byte short and hashes to a value that exists nowhere on the internet. **Write the payload to a file; hash the file.** p677 re-measured all four that way, and re-confirmed `c71d239df917` independently from a new address — [`THU-MAIC/MAIC-Core`](https://github.com/THU-MAIC/MAIC-Core)'s `LICENSE` is byte-identical to `apache/.github` (`diff` exit `0`).

🔵 **The general claim, which is the point of this trend:** a remediation pass must verify on a **different channel** from the one that produced the error, because the cause is still live in the original channel. `T63` is the fourth member of a family this base has measured end to end — `671-R` (byte equality is not identity), `673-A` (hash inequality is not mutation), `676-A` (a `+2` residual concealing an edit to the operative terms), and now **the fix for a measurement defect, measured with the defect.** 🟢 **Each was caught by adding a channel, never by trusting one harder.**

## T64 — The licence boundary inside a platform runs through its components, and it runs in both directions 🆕 new at p678

A platform's licence is routinely used as a proxy for its parts. **p678 found that proxy failing in both directions, in the same pass, on two of this industry's most prominent assets.**

- **Permissive parts inside a copyleft platform.** Open edX core is `AGPL-3.0` — the standing copyleft objection this base has recorded against it. Its two **official mobile clients are `Apache-2.0`**: [`openedx/openedx-app-android`](https://github.com/openedx/openedx-app-android) and [`openedx/openedx-app-ios`](https://github.com/openedx/openedx-app-ios), carrying a **byte-identical** grant payload (`11,356 B`, `43070e2d4e532684`). A branded commercial mobile client ships without the binary inheriting AGPL.
- **An ungranted part inside a permissive project.** `THU-MAIC/OpenMAIC`, the ~42k-star multi-agent classroom, is permissively granted. Its front end [`THU-MAIC/MAIC-UI`](https://github.com/THU-MAIC/MAIC-UI) — `184★`, `39` forks — has **no grant payload at all**: six licence paths probed at the real default ref, all `404`.

🔵 **Both errors are invisible to a repository-level licence badge, and both change a scope.** The first *expands* what a studio may sell; the second *removes* a component someone would reasonably assume was adoptable. **The unit of licence diligence is the component you will actually ship**, which is this base's standing *"the licence unit is the dependency graph"* clause pushed down one level — from dependencies to **sibling repositories under one owner**.

🔧 **The practical test is cheap:** for every platform in a proposal, byte-read the grant of **each repository you will ship code from**, at its real default ref. p678 did this for `12` addresses in one pass.

## T65 — Forks per star separates deployed platforms from imported libraries, and the floor matters more than the ranking 🆕 new at p678

This base hypothesised at `p540` that **forks beat stars for institutional software** and ranked `14` points by forks-per-star, finding a boundary near `0.5` between a *deploy-per-institution* class and an *import-as-dependency* class. p678 is the **out-of-sample test**: `12` new points, measured independently, merged into [`evidence/forks-per-star-rank.2026-11-06-p678.tsv`](../evidence/forks-per-star-rank.2026-11-06-p678.tsv).

🟢 **The boundary held.** Institutional infrastructure landed above `0.5` without exception — LMS mobile clients (`1.632`, `1.097`), LTI libraries (`1.074`, `0.800`), a school ERP (`0.725`), Kolibri installers (`0.806`). The two **agent-shaped** repositories landed below it: `MAIC-UI` `0.212`, `moodlehq/wiki-rag` `0.189`. **Platform code is forked and deployed; agent code is imported.**

🟢 **New `#1` at adequate `n`:** `openedx/openedx-app-android` at `1.632`, displacing `dspace/dspace` (`1.364`), which had led since `p540`.

🔴 **But the adequacy floor, not the ranking, is where this metric earns trust.** Three of the top seven *raw* ratios are inadmissible at `n >= 20` stars: `oppia/oppia-ml` (`3.000`, `n=3`), `learningequality/kolibri-app` (`1.727`, `n=11`), `moodlehq/moodle-mlbackend-python` (`1.053`, `n=19`). **An unfloored ratio ranks a three-star repository first.** Published with the caveat in the cell rather than ranked — and the `n=3` verdict reproduces the one this base already recorded for `ucfopen/pylti1.3`.

🔧 **For a platform shortlist: rank by forks per star, apply an `n >= 20` floor, and read the stale date before the ratio** — `1EdTech/LTI-Tool-Provider-Library-PHP` ranks `#6` and was last pushed in `2018`.

## T66 — A curated base's standing failure mode is republishing its own holdings as discovery 🆕 new at p678

`p677` diagnosed this base as one that **measures well and publishes unreliably**: six addresses claimed-as-filed were absent from every shelf. **p678 found the same defect at the opposite sign** — a pass about to publish, as a new mechanism, something the tree already held.

The intended headline was that two verbatim `Apache-2.0` payloads can share a byte count and hash differently because the appendix placeholder style differs (`{yyyy}` vs `[yyyy]`), and that the authoritative `apache.org` text is `11,358 B`. **Scored against the tree before drafting: all of it held** — the ASF digest `cfc7749b96f63bd3` in `22` files, both variant digests already recorded, the `11,356–11,358 B` span stated verbatim on the foundations shelf, and the general rule already registered as **`T101` — *a length is not an identity***.

🔵 **The two failures are one rule at opposite signs**, which is the same shape as `667-C`: *a knowledge base must test its own claims against itself, in both directions.* `p677` tested whether a published claim was **on the shelf**; p678 tested whether a **new claim was already** on the shelf. **Neither test is expensive and neither was standing practice.**

🔧 **`ACTION p678-H`, now registered:** a pass's headline claim is scored against the tree **before** it is drafted, with the same variant-spelling discipline already applied to search legs — because `667-B` proved a fixed-string needle misses a held fact `53.8%` of the time on orthography alone.

## T67 — A reachability verdict belongs to an endpoint, not a host 🆕 new at p678

This base has recorded `api.github.com` as `403` **channel-wide** since `p670`, repeated at `p677`. **p678 refutes the scope of that claim with a control pair:**

| Call | Result |
|---|---|
| `gh api repos/openedx/openedx-app-android` | 🔴 `403` — *"GitHub access to this repository is not enabled for this session"* |
| `gh api -X GET search/repositories -f q='repo:openedx/openedx-app-android'` | 🟢 `200`, **returning the same fields**: stars, forks, `license.spdx_id`, `pushed_at`, `language` |

**Same host, same tool, same credential — opposite verdicts.** The block is a **session repository-scope** restriction on the per-repository path, not a network block on the host. Every star and fork count published at p678 came through the search path.

🔵 **The general claim:** a one-line-per-host reachability table **cannot express this**, and in recording the host as dead it discarded a live channel for an unknown number of passes. 🔧 Reachability tables name the **endpoint**, and a dead verdict on one path requires a second path tested before the host is written off.

## T68 — Placement is a property of the *search*, not of the repository 🟢 new at p679

Two consecutive passes ran the same eight legs against the same sector and got opposite placement results, and the difference was which legs supplied the finds. p678 sourced nine addresses by enumerating owner organisations and placed **zero** of them. p679 sourced four from the **four regional legs** and placed **three**. The mechanism is not subtle: a global query ranks on popularity, which selects for software that has deliberately shed its locale in order to travel; a regional query selects for software that is bound to a curriculum, a statute, a language or a timezone — and that binding *is* the placement evidence.

**Consequence for this base:** an unplaced shelf is not evidence that the sector is placeless. It is evidence that the search was global. Regional legs are not a reporting courtesy to be run after the real search; they are the only legs that return placeable supply.

## T69 — The strongest placement evidence is what a deployer *inherits*, not what an author *declares* 🟢 new at p679

This base has ranked its placement channels repeatedly, and p679 adds a class that outranks most of them: **the shipped default**. `Gego-K12/gegok12` had been carried unplaced through many passes, because its owner declares nothing and its README names no country. Its `.env.example` ships `TIMEZONE = 'Asia/Kolkata'`, and `config/app.php` resolves the application timezone from that variable — so every operator who installs it without editing config inherits an Indian locale. Similarly, `yasserhegazy/lab-grader-skill` writes student feedback in **Palestinian colloquial Arabic by default**.

A default is better evidence than a declaration for three reasons: it is **load-bearing** (changing it changes behaviour, so it is maintained), it is **unmarketed** (nobody sets a default timezone for positioning), and it describes **who is affected** rather than who wrote it. The adjacent new class is the **regulatory regime**: a `FERPA Compliance` section places `jlouisbru/Canvas-grading-with-AI` in North America more reliably than its author's address, because FERPA is meaningless outside the United States. Ranking, strongest first: national curriculum standard → jurisdiction-specific statute → shipped locale default → named institution with matching institutional domain → body-text language → owner self-declared location. 🔴 Below the line entirely: **language of instruction** — `bp-master-agent` teaches Brazilian Portuguese and is for that reason *not* LATAM-placed.

## T70 — The sector finally has a measurement instrument, and it is regional rather than global 🟢 new at p679

This base has recorded the evidence problem as education AI's central weakness across many passes, and has repeatedly noted that no dominant open-source evaluation exists. `bncc-dev/bncc-benchmark` is the first asset here that closes a usable part of it — and the significant thing is that it does so **for one country's curriculum**, not for education in general. It measures how much models fabricate BNCC codes and texts without access to the structured source, publishes **17,100 raw responses** from 19 models, holds a **private set back against contamination**, and reports a faithful-text spread of **88% down to 3%**.

The design choice that generalises is scoring **"refused a fake code"** separately from **"reproduced a real one"**. Those come apart in the published round — a model can sit mid-table on fidelity while accepting **10%** of fabricated codes — and they fail differently in production: confident confirmation of a curriculum objective that does not exist is a safeguarding problem, where poor recall is merely a quality problem. **The transferable lesson is that education evaluation is curriculum-shaped**, so it will arrive as a family of national benchmarks rather than one global leaderboard, and whoever grounds a tutor in a curriculum should be reporting both columns against the benchmark for *that* curriculum.

## T71 — Forks per star has **two regimes**, not one scale, and the adoption floor hides the second one 🔴 narrows T65, new at p680

`T65` established forks-per-star as this base's instrument for separating a **deployed platform** from an **imported library**, and said the floor matters more than the ranking. p680 keeps the instrument and breaks the single scale it assumes.

`jsboige/CoursIA` measures **`f/★ = 9.563`** — `153` forks against `16` stars. The census maximum this base had recorded was `moodle/moodle` at `1.017` (`p489`), with `openedx/openedx-app-android` at `1.632` (`p678`) as the outlier. `9.563` is not a larger value on the same axis; it is **a different behaviour**:

| Regime | `f/★` | What a fork means | Example |
|---|--:|---|---|
| **Deployment** | ~`0.3` – `1.6` | one institution runs its own instance | `moodle/moodle` `1.017`, `portabilis/i-educar` `0.767` |
| **Classroom** | ~`10` | one *learner* takes a working copy | `jsboige/CoursIA` `9.563` |
| **Reading** | <`0.3` | consumed in place, rarely copied | `BedirT/ACM-ICPC-Preparation` `0.274`, `hyyhf/agent-book-code` `0.153` |

Two consequences for anyone scoping from these shelves. **First, a single ranking is uninterpretable** — a course repository and a platform appear on the same list with the course repository on top, and the number means something different in each row. **Second, and this is the expensive one: the `stars:>40` floor that every supply census on this base has used excludes `CoursIA` outright.** The adoption filter and the adoption signal point in opposite directions here: `16` stars reads as *nobody uses this*, while `153` forks of a curriculum actively pushed the same day reads as *a class is running on it right now*. A star floor is a proxy for *attention*, and teaching material is used without being starred.

🔵 **The practical rule:** rank by `f/★` within a class, never across classes, and when a candidate fails a star floor, read its fork count before dropping it.

## T72 — A channel is exhausted when its new findings stop being *usable*, not when it stops returning rows 🔴 new at p680

p680 swept nine GitHub topic heads, six of which this base had never queried, and the raw yield looks healthy: `80` candidates at `stars:>40`, `21` of them absent from this repository entirely. On a row count, that is a productive channel. On the only test that matters it is finished: **of the `21` novel addresses, `1` is a permissive, live education asset.** The other `20` fail on licence (GPL-3.0, AGPL-3.0, `NOASSERTION`, no grant), on dormancy (several large curricula last pushed in 2023–2024), or on being the wrong sector entirely (`topic:plagiarism-detection` returns music-tooling and binary-similarity research alongside academic integrity).

This matters because the two readings recommend opposite actions. *"The channel returned 21 new addresses"* argues for sweeping more topics. *"The channel returned one usable address"* argues for spending the next pass somewhere else — and the second reading is the correct one, because `63.8%` of everything the channel returned is already on these shelves.

🔵 **Three topic heads are simply empty**, and that is a vocabulary finding rather than a supply finding: `topic:early-childhood-education` → `0` repositories, `topic:teacher-tools` → `0`, `topic:competency-based-education` → `1` (already held). These are terms **educators** use and **repository owners do not tag with** — the same mismatch `T23` found from the other direction when the permissive-platform claim collapsed on vocabulary rather than availability. A `0` on a topic head is evidence about the tagging, not about the world.

## T73 — GitHub's licence field has no direction, and the licensor it punishes is the careful one 🔴 new at p681

Every supply census on these shelves works from the mandate *"focus on MIT / Apache-2.0 / BSD"*, and the cheapest way to honour it is GitHub's own licence facet — the `spdx_id` that `search/repositories` returns. p681 read the **grant bytes** of five repositories that all report **`NOASSERTION`**, on the same day, at their resolved default refs:

| repo | `spdx` | grant payload, byte-read | what a facet filter does |
|---|---|---|---|
| `Saidkhusayn/student-dropout-early-warning` | `NOASSERTION` | 🟢 **verbatim MIT** + an explicit `CC BY 4.0` data carve-out | 🔴 **drops a permissive row** |
| `ChrisWhiteSr/teach-skill` | `NOASSERTION` | 🟢 **MIT** + a portions notice naming an upstream that verifies | 🔴 **drops a permissive row** |
| `GarethManning/education-agent-skills` | `NOASSERTION` | 🔴 **CC BY-SA 4.0** | 🟢 right, by accident |
| `PreTeXtBook/pretext` | `NOASSERTION` | 🔴 **GPL-2-or-3**, text absent from the repo | 🟢 right, by accident |
| `workforce-data-initiative/skills-api` | `NOASSERTION` | 🔴 **non-commercial**, and names a different program | 🟢 right, by accident |

🔴 **Two of five sit on verbatim MIT and three on grants that forbid a commercial derivative.** The field is not a weak signal that needs a wider threshold; it is a signal with **no direction** — the three it classified usefully it classified for reasons unrelated to the two it got wrong.

🔵 **The mechanism, which makes the behaviour predictable rather than random.** GitHub's detector matches licence **bodies**. Anything appended to, prepended to, or substituted for a canonical body defeats it. So the repositories it fails on are precisely the ones whose authors did something *more* careful than pasting a template: `Saidkhusayn` separated code from data in the grant file, `ChrisWhiteSr` attributed an upstream inside the grant, and `PreTeXtBook` wrote a correct licence *notice* and shipped no body for the detector to find. **The detector rewards the template and punishes the drafting.**

🟡 **Scope, so this is not overread.** This says nothing about SPDX as a standard, nor about repositories that do report `MIT` — in **`9` of `9`** cases this pass where the facet read `MIT`, the bytes agreed (counted from [`evidence/p681-candidate-verification.2026-11-06-p681.tsv`](../evidence/p681-candidate-verification.2026-11-06-p681.tsv), not estimated). **A positive `MIT` reading was reliable every time it appeared; it is the absence of a reading that carries no information.** The claim is narrower and operational: **`NOASSERTION` is not evidence of anything, in either direction, and a census that treats it as "no permissive grant" will systematically lose the most carefully licensed projects in the field.** The only reading is the bytes at the resolved default ref.

## T74 — Where a copyleft education platform fronts a public API, the permissive opportunity is the client 🟢 new at p681

This base's standing objection to the education platform layer is licence-shaped: the systems institutions actually run are copyleft. Moodle is GPL-3.0, Chamilo GPL-3.0, Open edX AGPL-3.0, Pressbooks GPL-3.0, and `PreTeXtBook/pretext` is GPL-2-or-3 — so a client-branded fork carries source disclosure, and `T6` treats the arrival of an Apache-2.0 LMS as news precisely because the alternative is so constrained. **p681 found that the objection is avoidable without an Apache-2.0 platform, by moving one layer out.**

| layer | project | licence | reaches your code? |
|---|---|---|---|
| platform | `pressbooks/pressbooks` | 🔴 GPL-3.0 | yes, if you fork it |
| authoring toolchain | `PreTeXtBook/pretext` | 🔴 GPL-2-or-3 | yes, if you derive from it — **no**, if you run it as a program |
| **corpus access client** | `johnnyrobot/pressbooks-cli` | 🟢 **MIT** | 🟢 **no — it holds no platform code** |
| corpus | 28 networks, **`9,601`** open textbooks | openly licensed per book | reachable with **no account, key or token** |

🟢 **The mechanism is ordinary copyright law rather than a licence loophole, which is why it is safe to build on.** Copyleft attaches to derivative works. A client that speaks a platform's public REST API links against nothing the platform licenses, so it inherits nothing — and running a GPL program over a client's content (PreTeXt converting XML to PDF) imposes obligations on neither the content nor the code beside it. **The obligation follows the code, not the data and not the pipeline.**

🔵 **Generalised, and this is the reusable part: for any copyleft platform on `verticals/solutions.md` that exposes an API, ask what the permissive client tier would be before asking whether the platform can be relicensed.** Moodle, Open edX, Chamilo, Sakai and ILIAS all expose web services. The permissive asset is the agent, the exporter, the analytics client or the corpus reader that talks to them — and `P51`'s "ship over the LMS via LTI, never fork it" is the same argument arriving from the integration side rather than the licence side.

🔴 **The limit, stated so the trend is not over-applied.** This buys access, not control: you cannot change platform behaviour from outside it, and anything you need *inside* the platform is still copyleft. It also assumes the API is public and adequate — and `pressbooks-cli`'s README is a catalogue of how inadequate a real one can be (no directory endpoint, a `search` parameter accepted and discarded, `per_page` hard-capped at `10`, `403` to an unrecognised `User-Agent`). **The licence problem moves to an engineering problem, which is the trade worth making, not a free lunch.**


## T75 — The next binding education-AI deadline in North America is a **funding** rule, and it buys outcome plumbing rather than AI 🟢 new at p682

Every deadline this file has tracked in North America has been a *restriction*: state bills, exam bans, district policy mandates. **Workforce Pell is the first one that is a cheque.** The US Department of Education's final rule extends Pell eligibility to **short-term programmes** — roughly **`150`–`599` clock hours**, about **8–15 weeks** — **generally effective `2026-07-20`, with optional early implementation from `2026-07-01`**, offered only by accredited institutions, with **governors and state workforce boards** designating high-demand industries and approving programmes.

🟢 **The trend is in the eligibility condition, not in the money.** A programme keeps Workforce Pell only by passing **completion, outcome and earnings tests, per programme, over time** — and a programme with zero or negative value-added earnings **loses eligibility**. That converts a funding opportunity into a **longitudinal, auditable, per-programme reporting obligation**, landing on community and technical colleges and continuing-education arms: precisely the institutions whose student-records estate is thinnest and whose BI layer is a spreadsheet.

| What the rule demands | What answers it on these shelves | Licence |
|---|---|---|
| per-learner activity and completion evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (`144★`) over [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (`955★`) | 🟢 Apache-2.0 / permissive |
| roster and programme identity across systems | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster), [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) | 🟢 permissive |
| at-risk detection before the completion test fails | [`Saidkhusayn/student-dropout-early-warning`](https://github.com/Saidkhusayn/student-dropout-early-warning) | 🟢 **MIT** (+ `CC BY 4.0` data carve-out) |
| credential evidence | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 permissive |

🔵 **Why this generalises past one US rule.** The pattern — *a regulator funds a programme and makes the money conditional on measured outcomes* — is the strongest buying trigger this file has found in any region, because it is **dated, statutory, and unambiguous about what must be produced**. `T3` recorded that governance became the buying trigger when usage outran policy; `T75` is the sharper form: **the buying trigger is an audit you cannot pass with a spreadsheet.** 🔴 **The limit, stated so the trend is not over-sold: none of this is AI.** The compliance work is data plumbing, and an engagement that leads with an AI tutor will lose to one that leads with an earnings-linkage report. The AI is what you sell *second*.

## T76 — A closed vocabulary decays silently, and the report that it was fixed is the most dangerous artefact it produces 🔴 new at p682

This KB's `Region` field is a closed vocabulary of five values. At p682 it held **`114` distinct strings**, with **`367` of `795` cells (46 %) outside the vocabulary**: `**EMEA**` beside `EMEA`, `🟢 **LATAM**` beside `LATAM`, `EMEA (Finland)`, `APAC 🇨🇳`, `Global (unplaced)`, `Not placed`, `—`, and in seven rows an entire sentence of prose sitting in the field a filter reads.

🔴 **The failure mode is not untidiness — it is partial answers that look complete.** A reader filtering `Global` lost the `38` rows spelled `Global (unplaced)`. A reader filtering `EMEA` lost the `32` spelled `**EMEA**` and the `8` spelled `EMEA (Finland)`. **Nothing in the output was marked wrong**, because a bucket of size zero and a bucket that was never queried are indistinguishable downstream. This is the same shape as `T73` (a licence field with no direction) and `682-C` (two rows for one subject): **in each case the defect is invisible to the consumer of the data and visible only to a census.**

🔵 **The decay mechanism, which is the transferable part.** Each individual deviation was *locally reasonable*: bolding a region to match the row's typography, appending `(Finland)` because the country is the useful fact, writing `Not placed` because it is more honest than `Global`. **A closed vocabulary cannot absorb local reasonableness** — every well-meant annotation is a new bucket. The field must carry the value and **nothing else**, with the country, the evidence class and the confidence living in prose or in their own fields.

🔴 **And the most dangerous artefact was the fix report.** `p669` recorded this column *normalised* — truthfully, for one table out of eight — and that note then stood for thirteen passes as evidence the problem was handled, which is why it was never re-measured. **A repair stated at the top of one file is not a repair of the base.** The rule p682 adopts: **a normalisation claim must publish the census it is derived from, before and after, over every file it claims to cover** — `114` → `8` distinct, `367` → `3` non-conforming, and all three survivors shown to be non-placements (`Verdict`, `Adopcion`, `mixed`). ⚠️ **The residue is honest and unresolved:** `Global` now means both *truly global* and *not placed*, `240` cells hold it, and a sixth value would re-break the filter. The right fix is a `placed: true|false` field beside the region.

## T77 — A knowledge base's own novelty measurement is a channel, and it decays toward optimism 🔴 new at p683

p683 swept `558` education repositories over `22` search heads and measured novelty **twice**. Against the three sell shelves (`344` slugs): **`71.1 %` novel**. Against the whole tree (`5,053` slugs): **`47.1 %` novel** — `90` already shelved, **`205` already in the tree but never shelved**, `263` absent.

🔴 **The shelves and the tree answer different questions, and only one of them is the question.** A shelf records what was *bought*. The tree records what was *looked at and rejected*. Measure against the shelf and every rejected candidate reads as a discovery — so the error has a **direction**: it always overstates novelty, never understates it. On p683's own hand-picked set the overstatement was `17` of `21` candidates.

🔵 **Why this is a trend and not a one-off.** The bias grows monotonically: every pass that assesses a candidate and declines it adds another row to the tree and nothing to the shelves, so the gap between the two denominators widens with every pass forever. A base at pass `683` has `5,053` slugs in the tree and `344` on the shelves — a factor of `14.7`. At pass `100` that factor was small enough that the wrong denominator gave nearly the right answer, which is exactly why the habit survived.

**Signal**: p680 measured the split correctly (`51` shelved / `8` in-tree unshelved / `21` absent). p683 reproduced the *method* and still used the wrong denominator. A measurement discipline that is written down but not instrumented regresses to the convenient default.

**What to do with it on an engagement**: the same asymmetry governs a client's own build-vs-buy inventory. An architecture review that lists what the client *runs* and not what they *evaluated and rejected* will re-propose rejected tools as new options, and will do it confidently.

## T78 — Jurisdiction evidence has a strength ordering, and the strongest channel available is a registry fact 🟢 new at p683

Across p683's sweep, five distinct placement channels were exercised on the same candidate set, and they do not have equal authority:

| rank | channel | authority | why |
|---|---|---|---|
| `1` | 🟢 **committed ccTLD / restricted TLD host** | registry fact | `.br` is registry-restricted to Brazil; `.edu` to US institutions. Not an inference |
| `2` | 🟢 **named national examination** | statutory fact | 公务员笔试, 高考, ENEM — an examination is a jurisdiction |
| `3` | 🟡 **named institution, singular** | strong | `uni-heidelberg.de`, `hax.psu.edu`. Fails the moment it becomes a *list* |
| `4` | 🟡 **body-text language, measured** | weak but defensible | `55.7 %` CJK is a number; "it looks Chinese" is not |
| `5` | 🔴 **owner `location` field** | empty in practice | three consecutive passes have produced nothing from it |

🔴 **Each channel has its own characteristic false positive, and they are not interchangeable.** The TLD channel's is the **documentation placeholder** (`acme.edu` matched on this very sweep). The named-institution channel's is the **enumeration** (`vkaravir/JSAV`'s grant names Aalto *and* Virginia Tech — two regions, so no placement). The language channel's is the **substring inside an identifier** (`china` inside the org name `datawhalechina`).

🔵 **The practical rule, and it is cheap**: take the highest-ranked channel that returns a *single* answer, verify that answer is not a placeholder or a list, and write down which channel it came from in the row. p683 placed three repositories on channels `1`, `1` and `4`, and **refused three placements outright** rather than drop to channel `5`.

**What to do with it on an engagement**: a client's data-residency or sovereignty audit faces the identical problem. Residency claimed from a vendor's marketing page is channel `5`; residency read from the TLD and the contracted region of a storage bucket is channel `1`. The EU AI Act and Vietnam's Decision 33 both bind on where a system *operates*, not on where its vendor says it does.

## T79 — Academic integrity is the sector's one *statutorily forced* AI demand with essentially no permissive supply behind it 🟢 new at p684

Every other demand this base tracks has a permissive answer somewhere on its shelves. This one does not, and the asymmetry is measured rather than impressionistic.

**Demand side, all of it already held on this base's own pages:** Ofqual published AI-and-coursework-integrity resources in March 2026; the UK DfE issued generative-AI product safety standards in January 2026; the EU treats assessment as Annex III high-risk from `2027-12-02`; Vietnam's Decision `33/2026/QD-TTg` names **automated assessment** as high-risk; TEQSA requires every Australian higher-education provider to file a generative-AI risk action plan; UNESCO IESALC finds `87 %` of surveyed Latin American institutions using AI with `26 %` holding a strategy. Assessment integrity is the single capability named by regulators on **four** continents.

**Supply side, censused at p684 across four never-swept heads:** `395` candidates, `337` novel, `132` permissive — and **`0` live permissive repositories above `20★`**. The category's most-starred permissive asset (`163★`) is self-declared archived *and* built on an upstream API that no longer exists. The usable shelf is `16★` and below.

🔴 **The gap is not a discovery failure — it is a property of the problem.** AI-text detection is a classifier against an adversary that is already productised (`Cam3L1/ghost-skill` exists to defeat GPTZero, Turnitin and CopyLeaks), so an open detector is obsolete the week it ships and nobody accumulates stars on it.

🟢 **Which is why the three assets worth having are the ones that are not detectors.** `OSLL/code-plagiarism` compares ASTs — structure, not style, and renaming does not defeat it. `DSL4-Digital/RefExists` resolves citations against Crossref, arXiv and Semantic Scholar — a DOI either resolves or it does not. `pisan-labs/code-viva` examines the student about their own code — authorship by examination. **All three are decidable; none of them classifies prose.** The sellable position in this category is deterministic evidence, and it is open for the taking.

## T80 — The licensor's legal-entity suffix is a rank-1 jurisdiction fact, and it is sitting in a file this base already reads for every row 🟢 new at p684

`T78` ranked five placement channels and put registry facts at rank 1. p684 adds a sixth that belongs at rank 1 and costs **nothing**.

**`DSL4-Digital/RefExists`** carries `Copyright (c) 2026 DSL4 Digital, S.L.U.` in its `LICENSE`. `S.L.U.` is *Sociedad Limitada Unipersonal* — a company form that exists only in the **Spanish** commercial register. That is not an inference about where someone lives: it is the jurisdiction of incorporation, stated by the licensor, in the operative grant.

🟢 **The economics are what make it matter.** This base already fetches and hashes the grant payload for **every** row it files — the channel is a `grep` over bytes already in hand, with no extra request. The equivalent class generalises directly: `S.L.`/`S.L.U.`/`S.A.U.` (Spain), `GmbH`/`UG` (Germany), `S.à r.l.` (Luxembourg, France), `B.V.` (Netherlands), `Oy`/`Ab` (Finland, Sweden), `Pty Ltd` (Australia), `Ltda`/`S.A.` (Brazil and Spanish-speaking LATAM), `K.K.`/`G.K.` (Japan), `LLC`/`Inc.` (United States — weakest of the set, since US entity suffixes do not identify a state and barely identify a country).

⚠️ **Two limits, stated so the channel is not over-read.** It gives the jurisdiction of **incorporation**, which for a vendor is usually the right answer and for a holding company may not be. And it only fires when the licensor is a **company** — p684's other five candidates were licensed by individuals or contributor collectives, so the channel placed `1 of 6`. 🔵 Low hit rate, zero cost, rank-1 authority: run it on every row, expect it to be silent most of the time.

## T81 — Past a certain maturity, a curated base learns more demand-side facts from repositories than from demand-side searches 🔴 new at p684

p684 ran the four mandated regional demand legs and the four mandated English legs. `18` facts returned, **`16` already held** — and held in more detail than the sources gave them.

🟢 **The two facts that were genuinely novel arrived through a repository's README.** **Lei 12.764** (Brazil's national autism-rights policy) and the **LBI / Lei 13.146** were absent from this entire knowledge base, and both came out of `Fernandosr85/sistema-gestao-pei` — a `1★` prototype found by a `topic:special-education` sweep, not by any question about Brazilian education policy.

🔴 **This inverts the direction the mandated legs assume.** Demand legs read secondary commentary, which converges on the same canonical set of statutes and surveys; a base that has already absorbed that set will keep scoring near-total nil on them (`T72`). A *working implementation*, by contrast, cites the statutes its author actually has to comply with — including the ones no commentary mentions, because they are too specific to generalise about.

🟢 **The operational consequence is a reordering, not an abandonment.** Keep the demand legs — they are the control that proves nothing was missed, and the nil is only informative because the denominator is written down. But **mine the shelved repositories' own texts as a demand channel in their own right**: statutes, named examinations, accreditation bodies and funding programmes cited in a README are facts a client's legal team will recognise, and `T78` already ranks them above anything a trend article can offer. This also explains why `T78` rank 2 keeps producing: a statute citation is simultaneously the best **placement** evidence and a novel **demand** fact.

## T82 — A repository name is not a licence, and the collision risk is concentrated exactly where adoption is highest 🟢 new at p685

Measured at p685 across all `104` distinct bare repository names on `agents/top.md`, filtered to exact name equality: **`63` (`60.6 %`) share their name with at least one other repository**, `23` have a namesake whose grant *differs* from the canonical's, and **`43` pair a permissive canonical with a namesake that is copyleft or carries no grant at all.** In total `1,422` foreign repositories wear this shelf's names, of which **`936` (`65.8 %`) have no licence file at all** and `82` are copyleft.

🔴 **The `60.6 %` is not a defect rate**, and quoting it as one would repeat the `p455` error this base already retracted once. A collision is trivial when the name is a dictionary word, and nobody searching for `lumen` is looking for a shelf row. **The risk is a function of the canonical's own adoption**, because adoption is what puts a bare name into a blog post, a README instruction or an agent's tool call:

| canonical adoption | dangerous-class subjects |
|---|--:|
| ≥ `10,000★` | **`3`** |
| ≥ `1,000★` | `6` |
| ≥ `100★` | `18` |
| any | `43` |

**All three `≥10,000★` cases are rows this base sells from**, and the sharpest is its #2: `THU-MAIC/OpenMAIC` is **MIT** (`1,065 B`, `ba2525637432`), while `kolbyzhu5/OpenMAIC` and `ChengZhuo2025/OpenMAIC` are both **AGPL-3.0** with a payload that is byte- *and* hash-identical between them (`34,523 B`, `0d96a4ff68ad`). `HKUDS/DeepTutor` is Apache-2.0 while `rddy/deeptutor` is MIT — the quieter half of the defect, where the grant changes permissive-to-permissive and nothing looks wrong.

🔵 **Two consequences, both actionable.** (1) **Resolve by owner-qualified slug, never by bare name** — and treat a bare name in a dependency manifest, a vendoring script or an agent tool definition as a lint error. (2) **Checking for the word "GPL" catches less than a fifth of the class**; the dominant failure is the *ungranted* repository, which conveys no rights at all and is therefore worse than copyleft, not better. The buildable rule is **P61** in `compose/patterns.md`: pin slug **and** payload digest, and enumerate vendored subtrees — because `OpenMAIC`'s own MIT root sits above an LGPL-3.0-or-later vendored subpackage, so a root-only check passes it and still ships copyleft.

**Confidence: high** for the measurements (one instrument, `gh api search/repositories`, exact-name filtered, controls at both signs). **Confidence: moderate** for the risk ordering, which rests on the claim that high adoption drives name-resolution — plausible and consistent with how the legs themselves returned these repositories (the `github trending education AI 2026` leg named `DeepTutor`, `OpenMAIC` and `ai-engineering-hub` **without owners**), but not directly measured.

## T83 — A verification channel certifies nothing until it has been controlled at both signs 🔴 new at p685

`p684` found that the standing quality bar's `curl -sI` URL check returns `403` in this environment for a real repository **and** for one that does not exist, so it can never fail. p685 reproduced that and then found the **same defect in a channel this base had been treating as authoritative**: `gh api repos/<slug>` returns `403` for every repository here, real or imaginary, because repository access is session-scoped — and the error text is identical in both cases (*"GitHub access to this repository is not enabled for this session"*).

| channel | real repo | real repo, absent file | non-existent repo | discriminates? |
|---|---|---|---|---|
| `curl -sI github.com/<slug>` | `403` | — | `403` | 🔴 **no** |
| `gh api repos/<slug>` | `403` | — | `403` | 🔴 **no** |
| `git ls-remote --symref` | `ref: refs/heads/main` | — | `fatal` | 🟢 **yes** |
| `raw.githubusercontent.com/.../LICENSE` | `200` + bytes | `404` | `404` | 🟡 **partly** |
| `gh api search/repositories` | row + stars + SPDX | — | `total_count 0` | 🟢 **yes** |

🟡 **The `raw` row is the one that changes a protocol rather than just annotating it.** It cannot separate *"live repository, no file at that path"* from *"no such repository"* — both are `404`. So the two-channel procedure this base already follows is not stylistic: **existence must come from `ls-remote` first**, and only then does a `404` from `raw` carry the meaning *"ships no grant at that path."* Reversed, or used alone, `raw` would report a nonexistent repository as one with a missing licence.

🔵 **The transferable rule is about instruments, not about GitHub.** A channel that returns the same answer for a true and a false input has zero information content, and it fails *silently* — every candidate "passes", including invented ones. **Any channel used to certify a row must be run against a negative control in the same pass that relies on it**, because scope rules, proxies and rate limits change underneath a base that is re-run hourly: `gh api repos/<slug>` presumably worked when something started depending on it. 🔴 **And a standing instruction can itself be the defect** — the mandated `curl -sI` check is now in its second pass of being demonstrably inert, and no number of passes "complying" with it would have revealed that.

**Confidence: high.** Every row above was measured at p685 with explicit positive and negative controls, on two tools.


---

## T88 — `NOASSERTION` is not a licence state, it is the absence of a classification — and in education what it hides is a Creative Commons plurality 🔴 new at p686

**This extends T82/T83 and P61 rather than discovering something new in kind.** p685 already recorded that `license.spdx_id` is a classifier's opinion and wrong in both directions. What p686 adds is the **magnitude and the composition**, which change what you do about it.

Of `31` repositories in this pass's candidate pool reported `NOASSERTION`, resolved by reading each grant payload at the real default ref: **`12` permissive and adoptable** (Apache-2.0, MIT, MIT/X, Unlicense), `1` **ECL-2.0** (OSI-approved, Apache-derived), `4` copyleft, **`5` Creative Commons**, `2` split-grant, `2` with **no licence file at all**, and **`1` outright proprietary**.

🔴 **The distribution has no mode you can bet on.** It spans public domain to all-rights-reserved, so **both** default policies are wrong: *unknown → skip* discards `12` adoptable repositories including the only institutional LMS in this industry under a permissive grant (OpenOlat, Apache-2.0) and an eleven-year-old autograding platform (RELATE, MIT/X) this base had never shelved in `686` passes; *unknown → probably fine* adopts a repository whose `LICENSE` reads *"All rights reserved — Source Available — Personal Use"* **while its own GitHub description calls itself open-source**.

🟢 **The education-specific finding is Creative Commons.** `5` of `31`, and `2` of the pool's `3` largest subjects by stars, carry a CC grant — because education repositories are frequently **content wearing a code repository's clothes**. `xiaoyang111222/cn-math-taxonomy` at `6,928★` is a taxonomy; `5mdld/anki-jlpt-decks` at `3,117★` is a deck. **CC cannot license software**, and no amount of package manifest makes it do so. This failure mode is far more common in education than in the other industries this KB covers, and a general-purpose ingest filter will not be looking for it.

🟡 **A single licence cell is also insufficient where the grant is split.** `andymatuschak/orbit` is Apache-2.0 across most of the tree **but `packages/app` and `packages/backend` are AGPL-3.0-or-later or BUSL-1.1** — the deployable halves are precisely the non-permissive ones. A cell reading "Apache-2.0" would be true of the repository and false of anything shippable.

**Confidence: high.** All `31` resolved first-hand at p686 by payload read, with byte counts and digests, and negative controls clean.

---

## T89 — A search index's `422` is not evidence of absence, and it under-reports exactly the largest subjects 🔴 new at p686

`gh api search/repositories` answers `repo:openedx/edx-platform` with **`422 Validation Failed`** — *"the listed users and repositories cannot be searched either because the resources do not exist or you do not have permission to view them"*. The repository is fully alive on the other channel: `ls-remote --symref` resolves **`master`**, and `LICENSE` reads `35,136 B`, `sha256₁₂ e12d78569742`, AGPL-3.0. Three further `422`s at p686 (`patchy631596/awesome-ai-agents`, `open-learning-exchange/treehouses`, `open-resources/open-education`) were re-probed and **none was absent**.

🔴 **The error has a direction, and that is what makes it dangerous.** It does not add noise symmetrically; it **removes** subjects, and it removed the largest open platform in this industry. This is the `p674` search-index-absence condition recurring on a different org, so it is a property of the channel rather than an incident. **A census built on `search/repositories` alone silently under-counts, and its own `total_count 0` looks exactly like a clean negative result.** Every `422` must be re-probed on `ls-remote` before it is recorded as an absence — the rule T83 states in general, applied to the specific instrument this base relies on for stars and grants.

**Confidence: high.** Four instances at p686, each contradicted on an independent channel.

---

## T90 — The strongest new education agents demote the LLM to narrator and take ground truth from a domain solver 🟢 new at p686

Two independent instances arrived in a single pass, in unrelated domains, both permissively licensed:

- [`wimi321/GoAgent`](https://github.com/wimi321/GoAgent) (MIT) wires **KataGo** — a superhuman Go engine — to a multimodal LLM. The engine scores the move; the model explains *why* the score is what it is.
- [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) (Apache-2.0) puts **OpenFOAM** behind an MCP surface for CFD teaching with Socratic questioning. The solver computes the field; the model surfaces the gap between it and the student's prediction.

🟢 **Why this matters more than either repository does.** Every tutor on this base's agent shelf asks one model to be **both examiner and explainer**, which is why hallucinated correctness is the sector's standing risk and why academic-integrity demand (**T79**) has no permissive supply behind it. This architecture removes the conflict structurally rather than by prompting: correctness is **decidable** because a solver decides it, and the model is confined to the one task it is reliably good at — narrating a result it did not author. It also degrades honestly: when the solver has no answer, the system can say so, which a single-model tutor cannot.

🟡 **The limit is scope, and it is severe.** It only works where a *checkable oracle exists* — board games, physics, mathematics, code, symbolic algebra. It does not transfer to essay feedback, language production or history, which is most of the curriculum. ⚠️ Both instances are also small and partly dormant (`58★`; `127★`, last push `2026-01-18`), so this is a **pattern worth building**, not a dependency worth adopting — see **P62**.

**Confidence: medium.** The architecture is clearly evidenced and verified first-hand in two instances; its durability is not, and `n = 2`.

## T104 — Education OSS is consolidating into monorepos, and the archived component repositories keep the stars 🔴 new at p692

**The measurement.** Two unrelated, healthy education projects moved their per-component and per-platform repositories into a single tree in the same window, and in both cases the **archived** address outranks the live one on every star-ordered channel:

| Project | Archived (and star-ranked) | ★ | Live successor | ★ | Ratio |
|---|---|--:|---|--:|--:|
| Scratch Foundation | `scratch-gui` | **4,807** | `scratch-editor` (monorepo) | **310** | **15.5×** |
| Scratch Foundation | `scratch-vm` | 1,306 | same monorepo, `packages/` | 310 | 4.2× |
| Learning Equality | `kolibri-installer-android` | 31 | `kolibri@develop:platforms/android` | 1,170 | — (inverted) |
| Learning Equality | `kolibri-app` | 11 | `kolibri@develop:platforms/desktop-app` | 1,170 | — (inverted) |

Learning Equality also archived `kolibri-installer-windows` (`6★`), `kolibri-installer-debian` (`4★`), `kolibri-installer-gnome` (`3★`) and `kolibri-android-wrapper` (`0★`): **the entire per-platform installer tier, `55★` in total, collapsed into one `1,170★` MIT tree under `platforms/`.**

**Why it is a trend and not two coincidences.** Both projects state the same reason in the same place — the first line of the archived repository's README (*“will be archived… opened in the mono-repo”*, *“moved to the Kolibri monorepo”*). Neither is decay. Both are consolidation by maintainers who are still shipping: `scratch-editor` was pushed the day this was written, `kolibri` the same day.

**The consequence that costs money.** Where a project consolidates, **the unit of delivery stops being a repository and becomes a path inside one.** That breaks three things a studio relies on:

1. **Star-ranked discovery points at the corpse.** A sweep ordered by stars — including every sweep this base has ever run — returns `scratch-gui` at `4,807★` and never sees `scratch-editor` at `310★`.
2. **`git ls-remote` and `pushed_at` both say “alive”.** An archived repository keeps its refs and its last commit date. `rdennler/thinkpad` reads `archived=true` with `pushed_at` three days old. **The only field that answers the question is `archived`, and it exists only on the API, not on the git channel.**
3. **A fork instruction written against the old address silently freezes.** This base published exactly that instruction for Kolibri and carried it for `14` passes.

**What to do instead.** Pin the **path**, not the repository: `learningequality/kolibri@develop:platforms/android`. Record the monorepo's grant, because it governs the path — Kolibri's root `LICENSE` is MIT (`1,097 B`, sha256₁₂ `3c056b34a476`), so the installers' MIT conclusion survives the move intact. And read `archived` on every address **already on a shelf**, not only on candidates: see `T105`.

## T105 — A `topic:` head in English education vocabulary can return a different *industry*, and three of them do 🔴 new at p692

`T23` established that educators use terms repository owners do not tag with, and `p680` found three topic heads that are simply empty. p692 found the third failure mode, which is worse than both because **it returns a full page of plausible results**:

| Topic head | Repositories | What it actually returns | Education yield |
|---|--:|---|--:|
| `topic:curriculum-development` | `43` | **Personal CVs and résumé sites.** `currículo`/`currículum` is Spanish and Portuguese for *résumé*; the head's population is `my-curriculum`, `curriculum-laravel`, `cv-virtual`, `Gabriel-Leon-CV`, `portafolio` | **`0`** |
| `topic:exam-preparation` | `35` | **IT certification cram material** — CKAD, AWS Solutions Architect, AI-900, CNCF, `Free-Exam-Dumps` | **`0`** |
| `topic:study-notes` | `172` | **The same certification/CS-course population** — `Game-Programmer-Study-Notes` (`10,079★`), `aws-csa-2017`, `Learn-Web-Hacking` | **`1`** of `172` |
| `topic:quiz` | `109` | **Quiz *games* and classroom-cheating tools** — `quizizz-cheat`, `piano-trainer`, `whisperify` | **`0`** |

**Why this is the dangerous shape.** An empty head is self-announcing — `0` results and you move on. A **colliding** head returns `43` repositories with real stars, real licences and real activity, and a pipeline that scores on licence and liveness will happily promote a stranger's résumé into an education knowledge base. This is the mechanism behind the *“nombre”* class of defect: **the row passes every mechanical gate and is about something else entirely.**

**The rule.** A topic head is a claim about *tagging*, never about *meaning*. Before a head is used as a channel, read the top five results and name the population; if the population is not the industry, **record the collision and retire the head** rather than filtering it row by row every pass. And treat a head whose English term is a false friend in Spanish or Portuguese as collided until proven otherwise — `curriculum` is the first one found, and it will not be the last.


### 🔴 The third collision, and it is the most expensive one: the LATAM institutions this base's market intel rests on are not on GitHub — and the one whose name *is* indexed is indexed as hardware

[`intel/market.md`](./market.md) rests its entire LATAM demand case on four named institutions — **Ceibal** (Uruguay), **Cetic.br** (Brazil), **CENIA** (Chile) and **Tecnológico de Monterrey** (Mexico). p692 queried them as GitHub organisations, a channel neither `p691`'s language probes nor any earlier topic sweep had touched:

| Probe | Result |
|---|---|
| `org:ceibal`, `org:ceibal-uy`, `org:fundacionceibal`, `org:plan-ceibal` | 🔴 **`422` — no such organisation**, all four handles |
| `org:cenia` | 🔴 **`422` — no such organisation** |
| `org:learningequality` *(control)* | 🟢 `203` repositories |
| `org:moodle` *(control)* | 🟢 `12` repositories |
| `ceibal in:name,description,readme` | 🔴 **`526` results, and the entire head is device-fingerprinting libraries** — `matomo-org/device-detector` (`3,552★`), `podigee/device_detector`, `DeviceDetector.NET`, `certified-android-devices` |
| `tecnologico-de-monterrey OR tecdemonterrey in:name,description` | 🟡 `441` results; head is student coursework at `3`–`15★`, nothing institutional |

**Why `ceibal` resolves to device detectors is the whole point.** Ceibal is Uruguay's national one-laptop-per-child programme, so **its tablets are entries in device-identification databases** — and the single most-cited LATAM education institution in this base's market intel is therefore indexed on GitHub as *hardware* rather than as *software*. That is this trend's mechanism a third time, at the worst possible place: **the collision sits exactly on the name a studio would search first.**

⚠️ **Stated with its limit:** five plausible handles were tested for Ceibal and CENIA, not every possible handle; the controls were green. **Absence of these handles is not proof the institution has no GitHub presence under another name** — it is evidence that the obvious ones do not resolve, which is what a studio actually hits.

**The regional conclusion.** LATAM's education-AI *demand* is the best-measured in the world. Its open-source *supply* is now nil on three independent channels — English topic heads (collided), Spanish and Portuguese description terms (`p691`, `0` adoptable of `90`), and institutional organisation accounts (`p692`, no resolving handles). **A LATAM engagement is a build-and-translate engagement, not a procurement one.**

## T106 — `T79` holds for student integrity and fails one level up: research integrity is permissively supplied and almost entirely 2026-vintage 🟢 new at p692

`T79` states that academic integrity is the sector's one statutorily forced AI demand with essentially no permissive supply behind it. **That claim survives, narrowed:** it is true of **student-facing** plagiarism detection, where [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (`357★`, MIT, Ghent University) remains the only live permissive option this base holds — `p680-B2` measured that layer across `19` repositories and found exactly one.

One level up, at **research** integrity, the picture inverts. `topic:peer-review` — a head no pass of this base had swept in `692` passes — holds `526` repositories, `40` above `20★`, and the permissive supply is dense:

| Asset | ★ | Licence | What it is |
|---|--:|---|---|
| [`ecnu-sea/SEA`](https://github.com/ecnu-sea/SEA) | 91 | Apache-2.0 | Automated paper review, **EMNLP 2024 Findings**, East China Normal University |
| [`Michael-Jiahao-Zhang/game-the-llm-reviewer`](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer) | 219 | MIT | Meaning-preserving rewrites that move an LLM reviewer's verdict |
| [`kael-odin/awesome-academic-research-skills`](https://github.com/kael-odin/awesome-academic-research-skills) | 198 | MIT | Auto-updated daily ranking of research agent-skill repositories |
| [`THUROI0787/absent-author`](https://github.com/THUROI0787/absent-author) | 147 | MIT | Detecting AI-produced papers no human author stands behind |
| [`ShaishavMaisuria/research-paper-lifecycle-skills`](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) | 60 | Apache-2.0 | `42` skills: review → writing → citation verification → rebuttal |
| [`amirkiarafiei/open-scholar-peer`](https://github.com/amirkiarafiei/open-scholar-peer) | 51 | MIT | Open implementation of DeepMind's **ScholarPeer Protocol** |
| [`FanBroWell/AI-paper-reviewer`](https://github.com/FanBroWell/AI-paper-reviewer) | 50 | MIT | LLM-based academic paper review |

**`26` of the `40` were novel to this entire base** — absent from every shelf, both trending files and all `3,321` ledger lines. Of those with a classifiable grant, the permissive share is the **majority**, and nearly every one was created in `2026`.

**Two consequences, pulling in opposite directions.**

- 🟢 **For a higher-education engagement, the supply problem `T79` describes is solved at the research tier.** A university asking for AI governance over its research output can be served from permissive components today; one asking for student-submission integrity still cannot.
- 🔴 **The best-starred asset in the layer is the attack, not the defence.** `game-the-llm-reviewer` at `219★` outranks every defensive tool listed above. **Any criterion-referenced LLM assessor a studio ships — rubric grader, Annex III learner assessment, automated reviewer — now has a public, MIT-licensed, `219★` adversarial corpus aimed at it.** Treat it as a mandatory red-team input: if a grading pipeline's scores move under meaning-preserving rewrites, the pipeline is not defensible, and that is cheaper to learn before a conformity assessment than during one.
## T135 — In education repositories the content and the code are routinely licensed differently, and SPDX cannot express it
**Evidence (first-hand, p701).** [`woolimi/robotics-roadmap`](https://github.com/woolimi/robotics-roadmap), `95★`, APAC: the `LICENSE` payload (`1,220 B`, sha256₁₂ `30b5135acd4d`) is a **verbatim MIT body plus an appended scope clause** — *"This license covers the map site in `site/`. The lessons in `lessons/` and the images in `docs/` are licensed under CC BY-NC-SA 4.0."* The shell is permissive; **the teaching material, which is the entire reason to want the repository, is non-commercial and share-alike.** GitHub reports `NOASSERTION`.
**Why it is a trend and not an anecdote.** The same split appeared independently at p701 in [`TTNAN/yinshi`](https://github.com/TTNAN/yinshi) (MIT code, OFL-1.1 fonts, externally-hosted corpus) and is the structural reason the procedural-simulation-lab category named this pass is valuable: [`Haosen-Zhang/MRI-Anatomy-Physics-Lab`](https://github.com/Haosen-Zhang/MRI-Anatomy-Physics-Lab), [`wixette/jacquard-loom-simulator`](https://github.com/wixette/jacquard-loom-simulator), [`OppositeNor/render-lab`](https://github.com/OppositeNor/render-lab) and [`Kernel0x19/klyro`](https://github.com/Kernel0x19/klyro) **generate what they teach from code**, so their grant covers the reusable asset. Education is unusual this way: a code repository's deliverable is normally code, but an education repository's deliverable is usually *content*, and content is where restrictive licences live.
**Confidence: high** for the instances (payloads read byte-for-byte); **medium** for prevalence (`4` observed instances in one pass, no census yet).
**Action for a studio.** Before reusing any educational repository, read the grant **to its last line** and check for a path-scoped carve-out. An `spdx_id`, a licence badge and a star count are all silent on this.

## T136 — The SPDX detector's refusals are trustworthy; its approvals are not
**Measured at p701 on `40` MIT-family payloads read byte-for-byte.** `37` were byte-identical in body (differing only in the copyright line); `3` were not. GitHub's `license.spdx_id` returned `NOASSERTION` for **`3`** repositories in total, and **all `3` were genuinely non-standard** — `robotics-roadmap` (appended CC BY-NC-SA carve-out), `yinshi` (appended third-party annex), `workstation-subject-teacher` (bespoke non-commercial grant). **No false alarms.**
🔴 **But it missed one of the three non-verbatim MIT bodies.** [`dduenhas/globo-interativo`](https://github.com/dduenhas/globo-interativo) is reported as clean `MIT`, and its warranty disclaimer reads `DAMAGES OR **OR** OTHER LIABILITY` — a duplicated word **inside the operative clause**. The two it caught deviate *after* a correct body; the one it missed deviates *within* it. The detector is tolerant exactly where tolerance costs most.
🔵 **This corrects how previous passes of this base framed `NOASSERTION`** — as "the detector declining to classify a grant this shelf has already read". On this sample it was never noise: every refusal marked a real deviation. The actionable inversion is that **`NOASSERTION` is a reliable instruction to read the payload, and `MIT` is not a guarantee that you can skip it.**
**Corollary on byte counts.** [`wixette/jacquard-loom-simulator`](https://github.com/wixette/jacquard-loom-simulator) carries a complete, valid Apache-2.0 grant at **`10,280 B`** — `1,078 B` short of the `11,357`/`11,358 B` canonical this base fingerprints against — because the text is reflowed and de-indented; `APPENDIX`, the unfilled copyright placeholder and the `limitations under the License` line are all present. **A byte count flags a payload for reading; it cannot adjudicate one.**
**Confidence: high.** `n = 40`, every payload read first-hand, both error directions reported.

## T137 — A language is not a region, and the closed `region` vocabulary makes a guess worse than an abstention
**Evidence (p701).** [`niuxito/human-body`](https://github.com/niuxito/human-body) (`11★`, MIT) is a 934-structure 3D anatomy atlas with a bilingual Spanish/English interface and a grant line reading © *2026 Alexis Parrón*. Every available signal is Spanish-language; **none of them separates Spain (EMEA) from Latin America (LATAM).** It is filed `Global`.
**Why this is a standing rule and not one row's problem.** `region` is a **closed five-value field** (`North America`, `EMEA`, `APAC`, `LATAM`, `Global`) that downstream filters depend on. A wrong bucket is not a softer version of an empty one — it is a false positive that a regional filter will serve to an engagement team as evidence. The placement hierarchy this base now uses, strongest first: **(1)** the grant payload naming an institution or corporate form (as with the *Private Limited* in [`euron-sde-team/euron-open-lms-mobile-application`](https://github.com/euron-sde-team/euron-open-lms-mobile-application)); **(2)** repository content naming a national curriculum, examination or institution (BNCC, ENEM, 统编 textbook, 计算机二级, UTN/UBA, Chalmers, Carnegie Mellon, Turkish Wikipedia); **(3)** the content's language *plus* a country-specific referent; **(4)** the owner account `location` field — flagged weakest at p668/p669 and **not used at p701**.
**Confidence: high.** This is a method rule, applied to `16` agent rows and `21` foundation rows this pass.

## T138 — The SIS holding most American K-12 student records has no maintained open-source extension layer
**Evidence (p701, `topic:powerschool` leg, `50` results).** The only permissive **PowerSchool** artefact returned is [`sriehl/PowerSchool-Student-Map`](https://github.com/sriehl/PowerSchool-Student-Map) — MIT, `8★`, © **2019**, default ref `master`, **last push `2024-03-27`**, alive and not archived but untouched for over two and a half years.
**Contrast with Canvas, measured in the same pass.** `topic:canvas-lms` returns a dense, *currently maintained* client layer: [`jjuanrivvera/canvas-cli`](https://github.com/jjuanrivvera/canvas-cli) (`20★`, Go, pushed `2026-11-05`), [`xieyanran/chalmers-calendar-sync`](https://github.com/xieyanran/chalmers-calendar-sync) (`53★`), [`Famalhaut04/canvas-weekly-hub`](https://github.com/Famalhaut04/canvas-weekly-hub) (`18★`, CityU Hong Kong), [`JERRIYHAN/tongji-online`](https://github.com/JERRIYHAN/tongji-online) (`12★`, Tongji), [`ImmortalKilan/Canvasist`](https://github.com/ImmortalKilan/Canvasist) (`9★`), [`leejamesss/cmu-cli`](https://github.com/leejamesss/cmu-cli) (`6★`, Carnegie Mellon), [`mihirargulkar/canvas-obsidian`](https://github.com/mihirargulkar/canvas-obsidian) (`6★`) — **all MIT.**
**The asymmetry is the finding.** Higher education's LMS has a global volunteer client layer; K-12's SIS has none. The plausible cause is access: Canvas gives every student an API token, PowerSchool's API is mediated by the district. 🟢 **Consequence for a North American engagement:** budget to build against the PowerSchool vendor API and do not expect community scaffolding — whereas a Canvas integration can start from a maintained CLI.
**Confidence: high** for the measurement; **medium** for the causal explanation.

## T139 — A non-commercial grant written in a language the reviewer does not read is reported as "unknown", and "unknown" reads as "proceed to review"
**Evidence (p701).** [`cyberdaddyleo/workstation-subject-teacher`](https://github.com/cyberdaddyleo/workstation-subject-teacher), `33★`, APAC, a genuinely useful teacher workbench (multi-class timetables and substitutions, teaching progress, homework registration, parallel-class grade analysis, drag-to-reseat, AI assistant). Its `LICENSE` (`2,351 B`, sha256₁₂ `147601097b6a`) is a bespoke Chinese-language grant that **explicitly forbids** selling the software or any renamed/reskinned/repackaged derivative, bundling it into a paid product, course, service or membership tier, and building a paid hosted service on it. **GitHub reports `NOASSERTION`.**
**The failure mode is a translation problem wearing a licence problem's clothes.** The gate emits *unknown licence*; a reviewer sees a 2,351-byte file of Chinese prose; the prohibition is in clause three. Nothing in the pipeline says **"commercial use prohibited"**, which is what the document actually says.
🟢 **Mitigation that costs nothing:** when a grant payload is not in a language the reviewer reads, translate the payload before classifying it, and treat `NOASSERTION` + non-Latin-script payload as **presumed restrictive until read**. Of `3` `NOASSERTION` repositories at p701, `1` was outright non-commercial — a base rate too high to defer.
**Confidence: high** for the instance and the licence text; **medium** for the base rate (`n = 3`).

## T140 — An MIT education app whose content is fetched at runtime from third-party APIs is a permissive shell around an unowned dependency
**Evidence (p701).** [`TTNAN/yinshi`](https://github.com/TTNAN/yinshi), `72★`, APAC: MIT code, and its licence annex states that the classical-poem corpus is **not in the repository** — it is fetched at runtime from two third-party public HTTP APIs, with *"no code from those projects included in this repository"*. The bundled typefaces are **OFL-1.1**, which carries reserved-font-name conditions MIT does not.
**Why it generalises.** The pattern recurs wherever the teachable content is a corpus rather than code: the permissive grant is real and covers everything the author wrote, while the thing the application is *for* arrives over the network from someone else, under no agreement, with no availability guarantee. Fork the repository and you have inherited a client, not a product.
🟢 **Action:** for any such row, a client deployment must **mirror the corpus** and record its licence separately, and the engagement estimate must include that mirroring. 🔵 This is the content-side twin of `T135`: there the content was in-tree under a different licence, here it is out-of-tree under none.
**Confidence: high** for the instance (annex read first-hand); **medium** for prevalence.

## T141 — The mandated search legs have now returned nil `29` consecutive times; the supply is real and sits below the queries' resolution
**Measured at p701.** All eight mandated legs — four global, four regional, run for the computed current year `2026` — returned **`0` addresses this base did not already hold**: OpenMAIC (held `p2`, `42,933★` confirmed), `ai-engineering-hub` (held `p651`), DeepTutor, Moodle, Open edX, Chamilo, ILIAS, ERPNext, OpenEduCat, RosarioSIS, GibbonEdu, openSIS. **Twenty-ninth consecutive nil.**
🟢 **The same pass found `1,018` novel repositories on three channels the legs cannot reach**, by changing *one* thing — adding a `created:` window to topic heads that had been swept before but never windowed: `20` English heads → `812` distinct / **`685` novel (`84.4%`)** / `309` novel and permissive; `10` Spanish/Portuguese heads → `255` / `224` / `65`; `10` North-American instrument heads (`topic:canvas-lms`, `topic:powerschool`, `topic:k12`, `topic:common-core`, `topic:ngss`, `topic:fafsa`, `topic:title-ix`…) → `259` / `209` / `74`.
🔴 **The diagnosis, stated so it is falsifiable.** Prose web search returns *what has been written about*, which is a popularity index with a months-long lag; a windowed `topic:` query returns *what has been published*, which is the supply. For a KB at `5,553` held slugs, the first is saturated by construction and the second is not. **A pass that runs only the mandated legs will correctly report nil and incorrectly imply scarcity.**
**Action.** Keep running the legs — they are a cheap liveness check on the shelves and they caught `0` regressions this pass — but **never report their nil as a finding about the industry.** State the channel and the window alongside any absence claim (the `T31`-second-sense rule about regional "zero" as a query artefact).
**Confidence: high.** `n = 29` passes for the nil; the novel counts are measured against the `5,553`-slug held set.

## T142 — A row count written into the commit message is not a row count on the page, and `p699`'s singleton rule does not catch that
**Measured at p702.** `p701` filed `16` agent rows and took [`../agents/top.md`](../agents/top.md) from `119` to `135`. Its commit message says so, precisely and correctly: *"agents/top.md 119 -> 135 (16 filed, arity 135/135 @ 6 cols)"*. **The page's own `## The agents — N rows` heading still read `119`** — and so did the region census under it, which was wrong in **four of its five figures** (`APAC 32` vs `34`, `Global 51` vs `61`, `LATAM 10` vs `14`, total `119` vs `135`; only `North America 18` and `EMEA 8` happened to survive).
🔴 **Why `p699`'s rule missed it.** `p699` found this page carrying *three* live row-count headings and stated the remedy as a singleton rule: *a row-count heading is a singleton, and the pass that writes a new one demotes the old one in the same edit.* `p701` did not violate that rule — it left exactly one heading standing. **It simply never wrote one.** A rule about what to do when you write a heading is silent about not writing one at all.
🔵 **The rule's missing second half, stated so a later pass can gate on it:** *a pass that changes a table's row count MUST update that table's count heading in the same edit, and a count recorded anywhere outside the page — commit message, PR body, session log — does not count as recording it.* A reader of this KB never sees the commit message; a compiler walking the headings never reads `git log`. **Published-but-wrong is worse than absent**, because the next pass re-derives from a number it has no reason to distrust.
**Action.** Every count heading this base publishes carries the pass that derived it. On any insert, re-derive by counting the table *after* the write and rewrite the heading in the same edit — never increment the published figure, which is `p684`'s and `p694`'s rule, now with `p701` as the case where the figure was not incremented but abandoned.
**Confidence: high.** Directly measured: `p701`'s commit message and `p701`'s published heading disagree by `16` rows, and the disagreement survived a full pass.

## T143 — `$(curl …)` strips the payload's trailing newline, so a grant's byte count and `sha256` taken through command substitution are both wrong — `14` of `15` measured
**Measured at p702, and it invalidated this pass's own first instrument.** The grant verifier read each payload as `body=$(curl -sf …)` and measured `printf '%s' "$body" | wc -c` and `| sha256sum`. **Bash command substitution deletes all trailing newlines from the captured output.** Most `LICENSE` files end in exactly one, so the byte count comes back **one short** and the digest — being a hash — comes back **entirely different**, with no visible sign that anything is off.
🟢 **What caught it was a cross-pass disagreement, not a control this pass designed.** Two rows p702 drafted collided with rows this base already held, and the held values disagreed by exactly one byte in both cases:
| Subject | This base already held | p702 via `$(…)` | p702 via file | Verdict |
|---|---|---|---|---|
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | `1,078 B` · `a76aa4a4405c` | `1,077 B` · `c6dca3b0db5b` | **`1,078 B` · `a76aa4a4405c`** | the shelf was right; p702's instrument was wrong |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `8,241 B` | `8,240 B` | **`8,241 B`** | same, confirmed independently |
**Two bytes of disagreement on two unrelated repositories is not a coincidence, and the re-measurement proved the mechanism:** `curl -o file` then `wc -c` on the file returns `1078`/`a76aa4a4405c`, reproducing a figure this base recorded passes ago **byte-exact and hash-exact**. That agreement across passes, on a different instrument, is the strongest grant control this base has run.
🔴 **Blast radius, and why it is not uniform.** `14` of the `15` payloads p702 measured were wrong. The one that was right — [`psd401/aistudio`](https://github.com/psd401/aistudio), `1,082 B` · `59aa4a374522` on both instruments — is right **because its `LICENSE` has no trailing newline at all**, so there was nothing to strip. **So the defect is silent *and* intermittent**: it agrees with the truth on exactly the files that happen to lack a final newline, which is the worst possible failure shape, because a spot-check can pass.
**Action.** Never measure a payload through `$(…)`. Write it to a file with `curl -sf -o`, then `wc -c` and `sha256sum` that file. Add this as step `0` of `P87`'s gate — it sits *before* the byte-count fingerprint of `P87` step `4`, because a fingerprint computed through command substitution will mismatch canonical for a reason that has nothing to do with the grant. 🔵 **And the generalisation worth more than the bug:** a figure this base already holds is a free control on any new instrument, and p702 only found this because it tried to shelf something already shelved.
**Confidence: high.** Mechanism isolated, reproduced on demand, and confirmed against two independently recorded prior values.

## T144 — The mandated legs' `X OR Y <noun>` keyword forms spend their recall on the common noun, not on `X` or `Y`
**Measured at p702.** `p699` named the legs' failure mode as *returning tutorials about AI rather than AI for education*. p702 measured a mechanism one level down. The leg form `quiz OR exam generator llm` — the shape the mandated leg set invites — returned, at the top of its ranking: an **audiobook** generator, an **avatar** generator, a **cold-email** generator, a **README** generator, a **presentation** generator, a **song** generator, an **antibody** generator and a **comic** generator. **None is a quiz. None is an exam.** The query's recall was spent almost entirely on `generator`.
🔴 **Likewise `sis OR lms mcp server education`**, which returned nine `awesome-*` list repositories in its top twenty — `awesome-selfhosted`, `awesome-mac`, `awesome-cpp`, `awesome-vue`, `awesome-public-datasets`, `awesome-machine-learning` — because an `awesome` list mentions every term in the query and therefore matches all of them weakly. Of `100` distinct subjects across p702's first eight-query batch, `39` were "novel and permissive" and **`0`** were education agents.
**Action.** In a keyword leg, the discriminating term must be the **head noun**, not a modifier joined by `OR`. Prefer `topic:` facets (`topic:intelligent-tutoring-system`, `topic:learning-analytics`) which are curator-assigned and cannot be matched incidentally, and reserve free-text for phrases whose head noun is itself the subject (`socratic tutor`, `lesson planning agent teacher`). Both of p702's productive queries were of the second form. This refines `T141`'s action rather than replacing it: keep running the mandated legs, but expect their prose forms to be dominated by whichever word in them is commonest on GitHub.
**Confidence: high.** Measured on `28` queries across three batches, with the false-positive sets enumerated above.

## T145 — A licence-family detector that greps the payload body reports the cross-reference, not the grant
**Measured at p702.** p702's grant probe classified the family by grepping the payload for `MIT License|Apache License|BSD|GNU GENERAL PUBLIC|Mozilla Public|…` and taking the first match. On [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly, `28,072★`) it reported **`GNU General Public`**. The payload is **Eclipse Public License v2.0** — its first line is literally `Eclipse Public License - v 2.0` — and it matched `GNU General Public` only because **EPL-2.0 contains a "Secondary Licenses" clause that cross-references the GNU GPL by name**. A detector that scans the whole body will find a licence named inside another licence.
🟢 **The API agreed with the payload and against the detector:** `license.spdx_id` returned `EPL-2.0`. This is the inverse of `p701`'s `701-A` finding — there the API's *approvals* were untrustworthy while payload reads were sound; here a naive payload *detector* was the untrustworthy party. **Neither channel is authoritative alone; the first line of the payload is.**
**Action.** Classify the family from the payload's **first non-blank line**, not from a scan of the body, and only fall back to a body scan when the head is uninformative — then report the fallback explicitly. Any grant whose head and body disagree is an unresolved permission and gets `🔴`, as `p701` did for `jacobphillips99/protorubric`.
**Confidence: high.** One decisive case, mechanism identified in the EPL-2.0 text itself, with API corroboration.

## T146 — The mandated vertical-platform leg got one of three licence claims right, and this base's shelves already held the two it got wrong
**Measured at p702.** The mandated leg `open source platform {industry} ERP CRM MIT Apache` made three licence claims. Verified against payloads read at the real default ref:
| The leg's claim | Payload read at p702 | Verdict |
|---|---|---|
| *"The Huly Platform is fully open-source under the **Apache License 2.0**"* | **EPL-2.0**, `14,197 B` · `8c349f80764d`, ref `develop` | 🔴 **refuted** — weak copyleft, not Apache |
| *"Krayin CRM is fully open-source under the **MIT** license"* | **MIT**, `1,078 B` · `a76aa4a4405c`, ref `2.2` | 🟢 correct |
| OpenEduCat named as the education ERP, **licence not stated** — *"check its LICENSE file before assuming MIT or Apache"* | **LGPL-3.0**, `8,241 B` · `528f84036800`, ref `19.0` | ⚠️ copyleft; the leg was right to decline |
🔵 **The result that matters for how this base spends its time: both figures the leg got wrong were already correct on [`../verticals/solutions.md`](../verticals/solutions.md).** The shelf had OpenEduCat at LGPL-3.0 `8,241 B` and Krayin at MIT `1,078 B` · `a76aa4a4405c` from an earlier pass. **The curated shelf out-performed the live search leg on the only question that decides whether Globant can build on a platform.** Against `T141`'s standing advice — keep the legs as a liveness check, never as a finding — p702 adds: **never as a licence source either.** A prose search result's licence claim is a secondary report of a primary document that takes thirty seconds to read.
**Confidence: high.** Three claims, three payload reads, two prior shelf values corroborating.

## T147 — "Held somewhere in this base" is not "shelved on this table", and a global slug ledger cannot gate a single shelf's insert
**Measured at p702, by nearly publishing the defect.** p702 built a novelty check the way earlier passes describe it: extract every `github.com/owner/repo` slug from every `.md` and `.tsv` in the repository (`5,594` slugs) and treat a candidate as novel if its slug is absent. That ledger is the right instrument for *discovery* — it answers "has this base ever seen this address" — and it is **the wrong instrument for an insert**, which asks "is this address already a row on *this* table".
🔴 **The two questions diverged on this pass.** `openeducat/openeducat_erp` and `krayin/laravel-crm` were flagged `HELD` by the ledger, which p702 read as *mentioned in prose somewhere* and shelved anyway; both were **already rows on [`../verticals/solutions.md`](../verticals/solutions.md)**. Worse, `hcengineering/platform` was never novelty-checked at all, because it reached the candidate list from a web-search leg rather than from the deduplicated `gh api` pipeline that the ledger gates. The inserts took that shelf to `102` rows with **`100` distinct subjects**.
🟢 **It was caught before publication by the distinct-subject control**, which is the fourth time a structural control on this base has paid for itself (`p674` cell arity, `p684` separator arity, `p686` table termination, now `p702` subject distinctness) — and the first time it caught a *semantic* duplicate rather than a rendering defect. The two rows were withdrawn; the shelf stands at `100` rows / `100` distinct. **`T143` exists only because of this near-miss**, since the collision is what exposed the one-byte disagreement.
**Action.** Gate an insert on the **destination table's own subject set**, re-derived from that table immediately before the write — not on the repository-wide ledger, and not on a candidate pipeline's own memory. Keep the global ledger for ranking discovery. Run both: the ledger says *worth looking at*, the table says *safe to insert*.
**Confidence: high.** Two duplicate subjects measured and withdrawn in-pass, with the third candidate's gap in coverage identified.

## T148 — The arity sweep this base trusts never covered the two files that hold most of its tables, and a sweep written to find that was itself wrong by `5×`
**Measured at p702, with the instrument corrected mid-measurement.** `p684` reported *"a cell-arity sweep now scores `0` disagreeing rows across all six shelf files"*, and p702 reproduces that exactly: [`../agents/top.md`](../agents/top.md), [`../repos/foundations.md`](../repos/foundations.md), [`../verticals/solutions.md`](../verticals/solutions.md), [`market.md`](market.md), [`trends.md`](trends.md) and [`../compose/patterns.md`](../compose/patterns.md) carry **`233` tables and `0` ragged rows**. The claim was true and is still true.
🔴 **But "all six shelf files" is `233` tables out of `4,419`.** The two append-only history files hold the rest — `2,165` tables on [`../agents/trending.md`](../agents/trending.md) and `2,021` on [`../repos/trending.md`](../repos/trending.md) — and they were never in scope. Swept for the first time at p702 they score **`40` ragged rows**:
| Shape | Count | What it means |
|---|---|---|
| row has **fewer** cells than its header (mostly `2`-col header, `1`-cell row) | `32` | renders with an empty trailing cell; the `Verdict` column is merged into the finding text. Cosmetic |
| row has **more** cells than its header | **`7`** | 🔴 **the `p674` harm exactly** — a stray `\|` splits a cell and renderers drop the overflow, so published evidence becomes invisible without any error |
| other | `1` | |
🔴 **And the sweep that found them was wrong first.** p702's initial sweep reported **`223`** ragged rows including `7` in [`market.md`](market.md). The separator pattern `^\|[-: \|]+\|$` matches `| | |` — **an intentionally empty header row, which is legal GFM and appears in `market.md`** — so the sweep read a header as a separator, the row below it as data, and reported a defect in a clean table. It also mis-scored the `2`-column history tables by not excluding escaped `\|`. Requiring **at least one `-`** in the separator and discounting `\\|` took the figure from `223` to `40`, a factor of `5.6`.
**Action.** (1) Extend the arity gate to the trending files, **read-only** — they are append-only by rule, so the `7` over-wide rows are reported and left, not rewritten; rewriting history to fix a renderer is the trade `p699` already refused. (2) New sections appended to those files must pass the gate before they are written, which p702's own appended sections do (`0` ragged). (3) Any sweep this base publishes a `0` from must state **which files it covered** — `p684`'s did, which is why its claim survived scrutiny and p702's `223` did not.
🔵 **p702 then reproduced the defect itself, by imitation, and caught it before publication.** Its first draft of the `p702` section on [`../agents/trending.md`](../agents/trending.md) copied the house style of the surrounding history — a `| … registered | Verdict |` header over rows that merge the verdict into the finding text — and so shipped **`7` single-cell rows under a two-column header**, which is precisely what this finding is about. That is the same mechanism `p699` identified for the triple row-count heading: **the defect propagates because each pass imitates the last.** Repaired in-pass by giving every row a real `Verdict` cell; both p702 sections now score `0` ragged, so the claim in this entry's **Action (2)** is true as published rather than aspirational.
**Confidence: high.** Both figures measured on the same tree minutes apart; the `| | |` false positive is reproducible and the regex fix is one character class; p702's own section was measured before and after repair (`7` → `0`).

## T149 — Three teams in three languages independently built the SAME grading architecture this pass: the model transcribes, a deterministic program judges

**Signal.** p703 filed three grading artefacts found on three separate channels, written in Chinese, Korean and French by authors with no apparent connection, and all three refuse to let the model assign the mark.

- [`lihaiyang616/chemeq-grader`](https://github.com/lihaiyang616/chemeq-grader) (MIT, APAC) states the division explicitly: the VLM **only transcribes** — instructed to copy a wrong equation wrongly and not correct it — and a deterministic parser checks balancing, charge, conditions, ↑↓, state symbols and ΔH. The author's stated reason: *balancing, charge, conditions and arrows are deterministic rules, and asking a model to do them in its head produces answers that look right and are wrong.*
- [`blueshadow62/fairhand`](https://github.com/blueshadow62/fairhand) (Apache-2.0, APAC) transcribes handwritten Korean scripts and then **compares against an answer key**; the AI's output is text, never a score.
- [`eulogep/Corrector-ai`](https://github.com/eulogep/Corrector-ai) (MIT, EMEA) names the whole product *correction **supervisée*** — OCR plus AI-assisted barèmes with the teacher in the loop by construction.

🔵 **Why this is a trend and not a coincidence: the three teams converged on the same boundary because the boundary is where the economics are.** Transcription is a perception task with a measurable error rate a teacher can check in seconds. Scoring is a judgement task whose errors are invisible, uncorrelated between runs, and expensive to audit. Splitting them means the expensive-to-verify half is replaced by code that is right by construction.

🟢 **And it yields a property none of the all-LLM graders on these shelves has: `chemeq-grader` re-grades locally with NO further API call when the teacher fixes a mis-transcription.** Review is free, so the marginal cost of a careful teacher is zero — the opposite of an all-LLM pipeline, where every correction is another billed inference.

**Action.** Make the transcribe/judge split the default architecture in any assessment proposal where the rubric contains *any* mechanically checkable component, and quantify the split in the pitch: what fraction of the rubric is deterministic (and therefore free and certain) versus what fraction needs judgement. [`decentralizeallengineering/officecheck`](https://github.com/decentralizeallengineering/officecheck) (Apache-2.0) is the ready-made deterministic half for `.docx`/`.xlsx`/`.pptx`/`.pdf` coursework.

**Confidence: high** for the convergence (three independent artefacts, grants and mechanisms read from bytes this pass). **Medium** for the generality — all three are small projects with ≤1★, and none publishes an agreement-with-human-markers figure.

## T150 — A held row is an unexplored owner, and this base has 5,257 of them

**Signal.** p703 ran owner expansion on six owners and got back **530 sibling repositories**. Two of those owners were already represented on these shelves by exactly one row each — [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) and [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) — and **neither owner had ever been queried.**

| Owner | Repositories | Held before p703 | Filed at p703 | What was sitting there |
|---|--:|--:|--:|---|
| `michael-borck` | **243** | `1` (`study-buddy`) | `4` | A Curtin University teaching estate: grading over LiteLLM, curriculum generation with an offline mode, speech-practice desktop app, an assessment *bench* that measures LLM marking consistency against human marks |
| `malkreide` | **75** | `1` (`global-education-mcp`) | `5` | A uniformly-MIT Swiss estate: cantonal education statistics, ETH Library, a Luanti learning-world framework tagged against **Lehrplan 21**, and a Socratic-method skill at **`55★`** — the most-adopted artefact p703 found anywhere |
| `cyanheads` | **181** | `0` | `4` | OECD (1,500+ datasets), OpenAlex (270M+ publications), Project Gutenberg (78,000+ full texts), and the TypeScript MCP framework all of them are built on (`153★`) |
| `onderwijsin` | **18** | `0` | `3` | A named Dutch education nonprofit: the teacher-pipeline MCP, an agent-skill marketplace, and the HOVI/KiesMBO national registry adapter |
| `quietbytehq` | **10** | `0` | `2` | A pre-alpha school information system with ministry-scale tenancy in its data model, and an offline timetable solver |
| `VIABLE-Learning-Lab` | **3** | `0` | `1` | A teaching harness whose unit of configuration is the teacher's help limit |

🔴 **The defect is in the ledger, not the supply.** This base holds **`5,257`** distinct repository slugs. Every one names an owner, and the owner is one API call away. `9` of p703's `44` rows came from the two owners already represented here — found not by searching for education AI, but by asking *who else does this person publish as.*

🔵 **Why owner expansion outperforms every keyword leg: an owner is a curated set with a known licence posture and a known domain.** `malkreide`'s `75` repositories are uniformly MIT, so a sibling's grant is predictable before it is read. `michael-borck`'s estate is one university lecturer's teaching output, so every repository is education by construction — no keyword can match that precisely, and `T130`'s star floor and `p702`'s common-noun recall problem both vanish, because nothing is being matched on a word.

**Action.** Promote owner expansion from an opportunistic channel to a standing sweep: for every owner appearing on these shelves, query `user:<owner>` once and record the result, so the sweep is never re-bought. Order by estate size — `cyanheads` (181), `michael-borck` (243) and `malkreide` (75) are done; `5,257` slugs remain, and their distinct-owner count is the real size of the backlog.

**Confidence: high.** Counts are from `gh api search/repositories` with `user:` qualifiers, read this pass; the two already-held slugs were confirmed against this base's own extracted slug set before the claim was written.

## T151 — The licence-payload hash this base prints in every cell identifies the OWNER, not the repository

**Signal.** Reading p703's own verification output rather than its conclusions: four `malkreide` repositories filed this pass all carry `sha256₁₂ ac1fc40e61a6` at `1,069 B`, and `michael-borck`'s `talk-buddy`, `netsim` and `assessment-bench` all carry `b4fdbc9f39ce` at `1,070 B`.

🔵 **The cause is structural, not accidental.** An MIT payload is a fixed template whose only variable content is the copyright line, which is constant across one owner's portfolio. So an identical hash across two repositories is evidence of **common ownership** — the expected, correct result — and not of a copied or forked grant.

🔴 **The harm, if the hash were trusted as an identity: a dedupe, provenance or "is this the same grant" scheme keyed on grant-payload hash would collapse an owner's entire estate into one subject.** For `malkreide` that is `75` repositories reduced to `1`. These shelves print `sha256₁₂` in every licence cell and had never stated what the value does and does not identify.

🟢 **What it remains good for, unchanged:** an integrity check on **re-reads of the same repository** — the use these shelves actually make of it, confirming a grant has not been edited since it was last read. That is worth keeping.

**Action.** State the scope in the licence-verification convention: the payload hash is an integrity check across time for one repository, never an identity across repositories. Keep printing it.

**Confidence: high.** Seven payloads read from bytes this pass at the real default ref; the two hash collisions are reproducible and the mechanism (constant copyright line) is inspectable in the payloads themselves.

## T152 — The three regions need three different engagement shapes, because their open-source supply is constrained in three different ways

**Signal.** p703 placed rows on all five region values, and the obstacle between a studio and usable open source was different in each.

| Region | What constrains the supply | What p703 measured | The engagement shape it implies |
|---|---|---|---|
| **EMEA** | Nothing hides the data — **the adapter is missing** | `7` filed rows are public-sector data layers; Zurich BISTA, four French national datasets (Annuaire de l'éducation, UAI, IPS, Parcoursup), ETH Library and the Dutch HOVI/KiesMBO registries are all **published by the authority and reachable with no API key** | Build the MCP adapter — `~1,000` lines of TypeScript over data that is already open. The scarce artefact is the connector, not the data |
| **APAC** | **Language**, not availability | `7` of `14` new agent rows are APAC; the strongest (`chemeq-grader`, `fairhand`, `Glass-grading`, `格致`) are Chinese- and Korean-first, and `p702` measured that English keyword legs match them on the common noun only | Read the primary language. The artefacts are mature and the mechanisms are the best on these shelves; they are simply not written in English |
| **LATAM** | **This base's own star floor** (`T130`) | `3` filed platforms are LATAM, with the licensor naming a public institution in-repo — a Pará state programme run by PRODEPA, IFPA, SIMBIC/UFPA and the state government | Partner with the public programme that already exists. The supply is institutional and sits at `0–1★`, so any star-filtered search declares the region empty |
| **North America** | Not supply — **demand articulation** | The demand leg has nilled `43` times; supply arrives via named institutions (a school district's own platform at `p702`) | Sell against a named peer institution's published build, not against a market-size figure |
| **Global** | Model-layer and framework supply is abundant and already held | `3` of `14` new agent rows; the novel ones are mechanisms (a teacher's help limit, a refusal boundary, a learner model) rather than platforms | Compose, don't build. The gap is pedagogy encoded as configuration |

🔵 **The transferable point: "is there open source for this in region X" is the wrong question, because in all five regions the answer is yes.** The right question is what stands between the studio and it — a missing connector, a language, a search filter, or a buyer who cannot name the need — and the answer differs by region, so one sourcing method cannot serve all five.

**Action.** Record the constraint per region alongside the opportunity in [`market.md`](market.md), so a sourcing sweep for an EMEA engagement looks for authority data portals, an APAC sweep reads `topic:` heads in the primary language, and a LATAM sweep drops the star floor to zero.

**Confidence: high** for EMEA, APAC and LATAM (each rests on rows filed and verified this pass). **Medium** for North America and Global, which rest on the accumulated nil record rather than on a p703 measurement.

## T153 — A rule enforced on the page where the defect was last seen is not enforced

**Signal.** `p699` found a stale row-count heading on [`../repos/foundations.md`](../repos/foundations.md), fixed it, and published the singleton-heading rule: *a row-count heading is a singleton, and a promotion and the heading it invalidates must land in the same edit.* `p702` found the identical defect on [`../agents/top.md`](../agents/top.md), fixed it, and restated the rule.

🔴 **p703 arrived to find both sibling shelves broken the same way, including the very page where the rule was first written.** `repos/foundations.md` published **`199` over a table of `233`** — understating its own shelf by `34` rows, for two full passes. `verticals/solutions.md` published **`94` over a table of `100`**.

🔵 **The rule was never wrong; its scope was.** Each pass fixed the page in front of it and left the rule attached to that page. A convention that lives in the narrative of one shelf is a note, not a gate — it binds whoever reads that shelf next, which on a three-shelf base is a one-in-three chance.

**Action.** Two parts, and the second is the one that generalises. (1) p703 counts and re-publishes **all three** headings in one edit — done, and verified by counting after the insert: `158`, `254`, `109`. (2) **A convention that applies to every shelf belongs in a gate or in the pass procedure, not in the prose of the shelf where it was discovered** — the same reasoning `T148` applied to the arity sweep that never covered the two files holding most of this base's tables.

**Confidence: high.** Both stale figures were read off the published files before the edit and both deltas were re-derived by counting rows between the header separator and the terminating blank line.
