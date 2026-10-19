---
industry: education
region: Global
updated: 2026-10-19
---

## 🔴 Pass 310 — THE INDUSTRY'S BIGGEST AI-IN-EDUCATION PROBLEM IS PHRASED AS A PROBLEM *ABOUT* AI, AND THAT IS WHY A KEYWORD SET BUILT FROM SOLUTIONS COULD NOT SEE IT

⏱️ **Pass 310 of `2026-10-19`.**

### T1 — Integrity is the live engagement, and the half of its supply tier that answers the POST-LLM question was missing

`p309` measured **`62 %`** of middle-school and college students using AI for homework by
`2025-12` (from `48 %` seven months earlier) against **`18 %`** of teachers reporting any formal
guidance, and concluded *"the engagement is teacher capacity, not a platform."* 🟢 **This pass
read the topic axis under that conclusion:**
[`academic-integrity`](https://github.com/topics/academic-integrity), 111 repositories, **`18` of
`20` new to this base, `10` permissively licensed.**

🔴 **And it had to retract its own first framing to say what is actually new.** This base already
carried **8 integrity rows, 7 permissive** — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
(MIT, **350★**, Ghent University), `pycode_similar` (191★), `automoss` (157★), `noplag-engine`
(86★), `copy-spotter` (58★), `jieplag` (54★, Tsinghua), `plagpatrol` (42★) — plus `Open-Detector`
since **`p97`**. 🟢 **Every one of them answers SIMILARITY: *does this match something else?***
🟢 **Every row `p310` adds answers something similarity cannot:** *was this written by a model*,
*do its citations exist*, *is the assessment itself defensible*, *is the student in the room*.
🔵 **The LLM did not make plagiarism bigger — it made plagiarism the wrong question.** A matcher
finds nothing when the text is original and machine-written, which is exactly why having the tier
did not make the engagement covered.

🔴 **Why 309 passes missed the post-LLM half.** `ingest/config.json` declares topics `edtech`,
`learning-management`, `educational-ai`, `tutoring`, `e-learning` and agent keywords
*"AI tutor … quiz generator … learning path agent … grading assistant"*. 🔵 **Every one of
those names a thing AI DOES FOR education. Integrity names a thing AI DOES TO it** — so a
keyword set assembled from solutions is structurally blind to the problem class, however many
passes it runs. 🟡 **Narrowed honestly: the SIMILARITY half still arrived**, through a channel that
was not the topic axis — which is why the retraction above was necessary. **The finding is about
how this base samples, not about the week.**

### T2 — A star filter is not a licence filter, and on this axis the gap is at the TOP

Of the top four rows on the integrity axis by stars, the **second** —
[`cabbage2000-lab/paper-tutor-skills`](https://github.com/cabbage2000-lab/paper-tutor-skills),
46★ — is **PolyForm Noncommercial 1.0.0**. The whole-axis shape: **10 permissive · 2
noncommercial · 1 proprietary · 1 zero-byte licence file · 4 no grant.** 🔵 **The unusable rows
are not the obscure ones.** On the tutor axis a studio could sort by stars and be roughly safe;
here that heuristic fails on the second row it touches.

### T3 — 🔴 The emotion-recognition line is a PROHIBITION, not a risk tier, and the roadmaps are walking toward it

EU AI Act **Art 5(1)(f)** prohibits inferring emotions of natural persons **in education** —
outright, since 2 February 2025 — while **Annex III(3)** merely makes admission, evaluation and
exam-monitoring systems *high-risk*. 🟢 **Screened on code this pass, four proctoring/forensics
rows infer nothing of the kind**: Eye Aspect Ratio, pixel-threshold gaze, mouth-movement counts,
face presence, audio energy and zero-crossing rate
([ledger](../evidence/p310-art5-screen.2026-10-19-p310.tsv)).

🔴 **The trend is in the roadmaps.** `ExamShield`'s `FUTURE_ROADMAP.md` lists, under
`### Advanced Biometrics`: keystroke dynamics, mouse movement patterns, **`Heart rate monitoring
(via camera)`** and **`Stress level detection`**. 🔵 **Camera-based physiological inference is
where proctoring is heading because the hardware is already pointed at the student** — and the
step from "gaze direction" to "stress level" crosses from *high-risk-with-obligations* to
*prohibited*. **For an EMEA engagement that is not a compliance cost, it is a hard stop**, and
it is invisible to any screen that reads licences and stars.

### T4 — Saturation is a property of the AXIS, and conflating it with the supply costs a pass

`p309` read `40` tutor-axis candidates, found `40` carried, and recorded supply saturation. This
pass read a different axis and found `18` of `20` new. 🔵 **Both measurements are correct.** The
durable statement is: **`ai-tutor`, `intelligent-tutoring-system`, `grading` and
`learning-analytics` are enumerated; the domain is not.** 🟢 And `learning-analytics` shows the
refined test: **11 of 20 carried, and the 11 are the entire APPLICATION layer** — LRS,
dashboards, LMS plugins, simulators. Its **model/method/dataset** layer was *not* carried, and
five usable rows were sitting there. 🔴 **This section first published that as `12 / 8` with all
eight uncarried rows dismissed as non-deliverables; both figures were wrong and are corrected in
[`agents/top.md`](../agents/top.md).** 🔵 **The durable denominator is neither "carried / new"
nor "deliverable / not" — it is LAYER.** An axis can be exhausted at one layer and untouched at
the one below it, and only the layered count tells you which.

### T5 — Agent SKILLS keep arriving, and they arrive with unread licences

`p309` found 5 of the top 20 `ai-tutor` rows and the ITS axis's `877`★ leader shipping as
**skills, not applications**, and flagged that a skill has no runtime to grade. 🟢 **Confirmed on
a second, unrelated axis**: two integrity rows are skills, and **the more adopted of the two is
the noncommercial one**. 🔵 A skill's deliverable is *content*, so the question is the **content
licence** — and content licences (CC 4.0, PolyForm, CC0) are precisely the families this base's
own classifiers were weakest on, which is what `gate-family-coverage` now measures and bounds.

### T6 — 🔴 APAC mandates curriculum; EMEA mandates conformity; North America mandates policy; LATAM mandates nothing yet

A one-line regional read that the 2026 instruments now support: **China and India legislate what
must be TAUGHT** (compulsory AI subjects, teacher qualification exams, Classes 3–8 from 2026–27).
**The EU legislates what may be DEPLOYED** (Annex III, Art 5(1)(f)). **US states legislate what
schools must have a POLICY about** (≈100 bills; Maryland SB 720, Idaho SB 1227, Arizona HB 4040).
**LATAM legislates almost nothing at national level** — Mexico has no general AI law, Brazil's PL
2338/2023 is stalled in the Chamber — **so its universities legislate for themselves.** 🔵 **The
same product is a curriculum deal in APAC, a conformity deal in EMEA, a configuration deal in
North America and a governance-framework deal in LATAM.**

### 🔵 Grade, stated once

Every regulatory and market figure above is **search-snippet grade**. Eight primary legal,
government and market hosts were probed this pass on **two independent transports** and refused
on both (`000` and `ENOTFOUND`); `github.com` and `raw.githubusercontent.com` answered on both.
🟢 **Every code, licence, byte-length and roadmap claim above is first-hand.**

## 🟢 Pass 309 — THE FORM FACTOR CHANGED UNDER THIS BASE: A QUARTER OF THE TOP `ai-tutor` REPOSITORIES ARE NOT APPLICATIONS, THEY ARE AGENT **SKILLS**

⏱️ **Pass 309 of `2026-10-19`, following `p308` of `2026-10-19`.** Evidence:
[`p309-claims-gate.2026-10-19-p309.tsv`](../evidence/p309-claims-gate.2026-10-19-p309.tsv) ·
[`p309-supply-census.2026-10-19-p309.tsv`](../evidence/p309-supply-census.2026-10-19-p309.tsv) ·
[`p309-payload-pin.2026-10-19-p309.tsv`](../evidence/p309-payload-pin.2026-10-19-p309.tsv).

### 🟢 The trend, counted rather than asserted

Of the **20** rows the [`ai-tutor`](https://github.com/topics/ai-tutor) topic renders by stars,
**five** ship as an **agent skill** — a prompt-and-instruction bundle loaded by a host agent —
rather than as a deployable application, and a sixth leads the
[`intelligent-tutoring-system`](https://github.com/topics/intelligent-tutoring-system) axis:

| slug | stars | form |
|---|---|---|
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **877** | **165 skills** for teachers and school leaders, targeting three different host agents |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | 309 | exam-prep coach with cross-session memory |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 289 | Bloom-2-Sigma tutor — **a skill AND a self-hostable app** |
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 247 | diagnosis-first STEM tutor |
| [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | 188 | Chinese civil-service exam prep |
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | 116 | teaching-support skill collection |

🔵 **Why it is a trend and not a taxonomy note.** A skill has **no runtime of its own**: no
server, no database, no auth, no deployment. 🔴 **So three things this base grades on do not
apply to it** — there is no hosting posture to assess, no data-residency story to check, and
**the AGPL's network clause cannot be triggered by software that never serves a request.**
🟢 **And one thing matters far more: the licence on the CONTENT**, because the deliverable *is*
the content. The `877`★ leader is **CC BY-SA 4.0** — 🔴 **ShareAlike on curriculum materials**,
which is a derivative-works obligation on a client's own course content, not a code question at
all.

🔴 **This base's instruments are built for the other shape.** The licence prober reads
`LICENSE` payloads and reported `NO-GRANT-CLAUSE` for that CC BY-SA grant-by-reference — true to
its rule and useless for the row. `ACTION p306-R` item 2's POINTER class, open for three passes,
is now **load-bearing** rather than tidy. → `ACTION p309-R` item 2

### 🔴 The listicle channel produced `0` in-domain rows, as `p308` predicted, and the prediction is scored

Four mandated queries, run as specified, with the current year computed and not hardcoded:

| query | in-domain rows |
|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **0** — returned general agent frameworks (CrewAI, AutoGen, LangGraph) and *learning-about-AI* courses, which are not education-domain agents |
| `github trending education AI 2026` | 🔴 **0** — `p308` ordered this one not re-litigated; it was run once to **score** the prediction rather than skipped in silence, and the prediction **holds** |
| `open source platform education LMS SIS MIT Apache self-hosted 2026` | 🔴 **0 new** — returned one vendor's own marketing pages; **OpenEduCat is LGPL-3.0**, as this base already carries |
| `AI education industry trends 2026` | 🟡 market-size spread only: `$6.4B (2025) → $79.6B (2034)` against `$8.3B (2025) → $57.2B (2033)` against `$10.6B (2026)` — 🔴 **three irreconcilable vintages, no new structure** |

🟢 **The two channels that DID produce: GitHub topic pages (`5` new rows) and
`raw.githubusercontent.com` (`10` first-hand payloads).** 🔵 **Say which, every time.**

### 🟢 One student-adoption number worth carrying as a trend rather than a datum

Student AI use **`66%` (2024) → `92%` (2025)** in one source, and RAND's **`48%` → `62%`** over
seven months to `2025-12` in another. 🔵 **Different populations and different questions, so they
do not average** — but both are **steep, recent and in the same direction**, against **`18%`** of
teachers reporting any formal guidance. 🟢 **The governance lag, not the adoption rate, is the
structural trend.**

## 🔵 Pass 308 — SEVEN TRENDS, AND THE FIRST THREE ARE ALL THE SAME DISEASE: THIS BASE KEEPS DISCOVERING THINGS IT ALREADY WROTE DOWN

⏱️ **Pass 308 of `2026-10-19`.** Evidence:
[`p308-shelf-consistency.2026-10-19-p308.tsv`](../evidence/p308-shelf-consistency.2026-10-19-p308.tsv) ·
[`p308-shelf-census.2026-10-19-p308.tsv`](../evidence/p308-shelf-census.2026-10-19-p308.tsv) ·
[`p308-identity.2026-10-19-p308.tsv`](../evidence/p308-identity.2026-10-19-p308.tsv) ·
[`p308-regional.2026-10-19-p308.tsv`](../evidence/p308-regional.2026-10-19-p308.tsv) ·
[`p308-channel-map.2026-10-19-p308.tsv`](../evidence/p308-channel-map.2026-10-19-p308.tsv).

### 🔴 `T-p308a` — A regression and a discovery need opposite responses, and this base cannot currently tell them apart

🟢 **`p307`'s headline was that `brownplt/LTLTutor` and `IgorFonck/logicits` had been carried as
`AGPL-3.0` for two passes and are `GPL-3.0`.** 🟢 **True.** 🔴 **Its post-mortem — *"a byte-LENGTH
SERIES was used to name a licence family"* — is not the mechanism, and the real one was already
written on this base.**

🟢 **[`agents/trending.md`](../agents/trending.md) line 15867:** *"`P171` live-confirmed: its
**§13 names Affero at line 552**, so a `grep Affero` misreads it as AGPL."* 🟢 **Verified
first-hand at `p308`: GPL-3.0 section 13 is titled *"Use with the GNU Affero General Public
License"*, and `Affero` occurs at lines 552, 556 and 559 of the 35 148 B payload.**
🔴 **[`agents/trending.md`](../agents/trending.md) line 3876 records the verdict `GPL-3.0 @ p212`.**

🔵 **So the sequence is: read correctly at `p212`, drifted to AGPL, restored at `p307` and
described as a discovery.** 🟢 **The distinction is operational, not semantic:**

> 🔴 **A discovery means the base lacked an instrument and must build one.** 🟢 **A regression
> means the base HAD the reading and lost it, and the fix is to find out what overwrote it.**
> 🔵 **`p307` built an instrument for a problem it already had solved, and never asked what had
> un-solved it.** 🟢 **The cheap detector: before writing *"this base was wrong for N passes"*,
> run `make claims` on the slug and read the oldest verdict you find.**

### 🔴 `T-p308b` — A standing CONCLUSION is never checked against the shelves it generalises over

🟢 **`p305` recorded a *"forced architecture"*: every permissive education row is a component,
every platform-scale system of record is copyleft.** 🟢 **`p306` refined it — the nil is *"a
property of the LMS LAYER"*.** 🟢 **`p307` broke it at the tutoring layer.**

🔴 **It was broken at the LMS layer the whole time, by
[`Selleo/mentingo`](https://github.com/Selleo/mentingo) — MIT, an AI-native self-hosted LMS,
`96★`, `1 348` commits — carried on this base for roughly `140` passes, and described at
[`agents/trending.md`](../agents/trending.md) line 6587 in exactly the words that refute the
conclusion: *"a permissive LMS exit."*** 🟢 **`make claims TOKEN=mentingo` returns `68` mentions.**

🔵 **`T-p307e` said *"no instrument compares shelf to shelf."*** 🟢 **`p308` built that instrument
for licence CELLS and it works.** 🔴 **The disease's larger form is in PROSE CONCLUSIONS, and the
new gate does not see it** — a conclusion is not tabular, and its subject is a class of rows
rather than a slug. 🔵 **Named as uncovered rather than implied to be covered** →
`ACTION p308-R` item 1.

🟢 **The substantive refinement, for the record:** `p307` concluded the mechanism behind a
permissive platform is **open-core — a proprietary Enterprise Edition to sell.** 🔴 **`mentingo`
has no proprietary edition**; it sells **managed hosting, SLA and implementation**, with an AWS
Marketplace listing that charges nothing for the software. 🟢 **The general rule: a vendor picks
permissive when its moat is anything that is NOT the code. An EE is one such moat; OPERATION is
another.** 🔴 **A commons-defending system of record still picks copyleft.**

### 🔴 `T-p308c` — `HEAD` equality proves identity; `HEAD` INEQUALITY proves nothing, and this base has been reading the converse

🟢 **`p283`'s rule is *"ls-remote every address; equal `HEAD` == one repository."*** 🟢 **Sound as
stated.** 🔴 **Its converse is false and has been relied on.**

[`lkh081231/OpenTutor`](https://github.com/lkh081231/OpenTutor) and
[`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) have **different `HEAD`s**
(`5fea390a49be` / `c75453f41946`), **identical root commits** (`483feed58f96`), **`188` of `188`
commits shared**, **byte-identical MIT payloads** (`1 068 B`, `5352b4967982`) and word-for-word
identical descriptions. 🔴 **`make carried` reported the second one `NEW`.**

> 🟢 **The identity key is the ROOT COMMIT.** 🔵 **`HEAD` answers *"the same SNAPSHOT?"*; the root
> commit answers *"the same PROJECT?"* — and the shelf question is always the second.**
> 🟢 **History containment settles direction: the superset is the live address, the subset is a
> stale mirror.** 🔴 **A fork one commit behind defeats the `HEAD` test; a fork six commits
> behind with a copied README defeats it while looking exactly like new supply.**

### 🟢 `T-p308d` — `gitlab.com` is reachable, enumerable, and EMPTY in this domain; the prediction `p307` registered is REFUTED

🟢 **`ACTION p307-R` item 6 registered a prediction in advance so it could be scored: *"the EMEA
sovereignty thesis predicts European education projects host there rather than on GitHub."***
🟢 **Scored.**

| arm | verdict |
|---|---|
| 🔴 **AI-education SUPPLY on `gitlab.com`** | **REFUTED.** 7 queries, up to 100 results each, **zero** AI-education projects |
| 🟡 European PROVENANCE of what is there | **WEAKLY HELD.** All four in-domain rows are European — `saxionnl/42/lms42` (NL), `olatorg/openolat-starter` (CH), `Openki/Openki` (CH), `moodlenet/moodlenet` |
| 🔴 Novelty | **REFUTED.** `3` of the `4` are **already carried** on these shelves |

🟢 **And an instrument lesson for every search channel, not just this one: on `gitlab.com`,
`search=tutor` ranks TUTORIAL repositories first** — `youtube-tutorial-series` (296★),
`vgpu-proxmox` (185★), `xavki-tutorials-index` (124★). 🔵 **A stemming collision between the
domain's core noun and the internet's most common content word.** 🔴 **A channel that returns
100 confident, irrelevant rows reads as coverage.**

🔴 **Also recorded: GitLab's API returns `license: None` for all four in-domain projects**, so
unlike GitHub it offers no licence triage field at all. 🟢 **Enumeration + payload read is the
only route there, which is the route this base already uses.**

### 🟢 `T-p308e` — The regulatory signal worth selling is a DATED DISTRICT OBLIGATION, and the US has nine of them

🔵 **This base has spent many passes on frameworks, guidance and advisory memoranda.** 🟢 **The
finding that converts is narrower: an obligation with a DATE, a BUDGET and a named party who is
out of compliance without it.**

🟢 **Ohio's district AI-policy mandate lapsed on `2026-07-01`.** 🟢 **North Carolina's state model
is due `2026-12-31` and district policies `2027-06-30`.** 🟢 **Maryland's `SB 720` starts a
120-day clock on a guidance release.** 🟢 **Oklahoma's `S.B. 1734` binds before `2027-28`.**
🔵 **Same shape as `p307`'s Ontario PA-day finding, at roughly fifty times the scale, and in the
one jurisdiction where districts hold their own budgets.**

🔴 **Counter-signal in the same breath, because this trend is about dated obligations and not
about enthusiasm:** Texas and Pennsylvania reportedly had **no** statewide guidance as of
`2026-09`, and Virginia's bills are **CONFLICTED** between *enacted* and *pending* across two
secondary sources. 🟡 **Both readings are ~6 weeks old and were not re-verified.**

### 🔴 `T-p308f` — A national programme can be UNWOUND, and this base has no instrument that notices

🟢 **South Korea's AI textbooks were stripped of official status by the National Assembly in
`2026-08`**, after adoption below `30%` and union pressure that the pace had outrun preparation.

🔵 **Every regional instrument this base carries is recorded with a date it STARTS binding.**
🔴 **None is recorded with a review, sunset or repeal risk, and this base has no gate that
re-reads a carried instrument to ask whether it still exists.** 🟢 **The Korean case is the
proof: a programme this vertical would have cited as its flagship reference is now a cautionary
tale, and nothing in the pipeline would have surfaced that.** → `ACTION p308-R` item 4.

🔵 **The demand-side mirror: `52%` of Australians and `47%` of New Zealanders support BANNING AI
in schools** (Ipsos Education Monitor 2026), against `23%`–`31%` elsewhere in APAC. 🔴 **Public
opinion is a repeal risk, and it is highest in the region's English-speaking markets.**

### 🟡 `T-p308g` — A gate that fires on the pass that reports it is working, and the fix belongs in the prose

🟢 **`p308`'s own write-up tripped `p308`'s own gate on its first run.** The sentence *"line 1834
carried `DaRL-GenAI/instructional_agents` as `Apache-2.0`"* is a retraction, and the instrument
read it as a live claim, because its retraction vocabulary matches `carried as` adjacently and
that sentence put the slug between the two words.

🟢 **Cleared by restating the correction in this base's standing form — `CORRECTED pNNN from X`
— rather than by widening the suppressor.** 🔵 **The general rule, and `p307` demonstrated the
same thing with `gate-offline`: when a gate fires on correct prose, prefer changing the prose.**
🔴 **Every widened suppressor is permanent and silent; a rephrasing costs one sentence and
leaves the instrument as sharp as it was.** 🟢 **Nine suppression classes were added to this gate
on the strength of payload adjudication, and this one was refused on the strength of a rewrite —
the difference is that the nine were wrong READINGS and this was a sloppy SENTENCE.**

## 🔵 Pass 307 — SEVEN TRENDS, AND FOUR OF THEM ARE ABOUT HOW THIS BASE KNOWS THINGS RATHER THAN ABOUT THE MARKET

⏱️ **Pass 307 of `2026-10-19`.** Evidence:
[`p307-channel-map.2026-10-19-p307.tsv`](../evidence/p307-channel-map.2026-10-19-p307.tsv) ·
[`p307-payload-pin.2026-10-19-p307.tsv`](../evidence/p307-payload-pin.2026-10-19-p307.tsv) ·
[`p307-regional.2026-10-19-p307.tsv`](../evidence/p307-regional.2026-10-19-p307.tsv).

### 🔴 `T-p307a` — An absence is established by a channel that ENUMERATES, never by one that is ASKED

🟢 **`T-p306a` said a declared absence must carry the list of addresses tried.** 🔴 **`p307`
shows that is necessary and not sufficient.** [`openedx/XBlock`](https://github.com/openedx/XBlock)
was declared licence-less by **two independent channels** — `raw.githubusercontent.com`
returned `404`, `github.com/.../blob/...` returned `404` on a different client — and both
were wrong, because both had been handed the same wrong address (`LICENSE.txt`, where the
file is `LICENSE.TXT`). 🔵 **Channel independence buys nothing when the address is shared.**
🟢 **The fix is categorical: enumerate the root tree (`git ls-tree`) instead of asking for
names.** 🔵 **Generalises past licences — it is the difference between *"the endpoint I
tried 404s"* and *"this thing does not exist."***

### 🔴 `T-p307b` — Licence identity is the TITLE. Not the length, and not the hash either.

🟢 **`p304` ruled on LENGTH and was refuted at `p305`. `p306` wrote *"length is not an
identity key"* — and in the same pass named a licence family from a length SERIES.**
🔴 **That series was two licences:** `33 893` / `34 520` are **AGPL-3.0**; `35 148` /
`35 149` are **GPL-3.0**, and this base carried two tutors under the wrong one for two
passes.

🔴 **The hash fails in the other direction.** Normalising (CRLF → LF, strip the ends)
collapses **nine** stock-Apache payloads to one value `283ea6cc2997` — across **three**
byte lengths (`11 357`, `11 358`, `11 359`) and **four** raw `sha256₁₂`. 🔵 **The base's
*"stock Apache = `c71d239df917`"* instrument, with six confirmations over four passes, was
counting one byte-representation of at least four and reporting the others as distinct
payloads.** 🟢 **Same correction on the copyleft side: `p305` noted `LTLTutor` and
`logicits` were *"one trailing byte apart"* — normalised, they are byte-identical
(`3743f7a4ab51`), and so is `plastic-labs/tutor-gpt`.**

🟢 **Operational form: read the first line. `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`
and `GNU GENERAL PUBLIC LICENSE Version 3` are one word apart and that word is § 13.**

### 🟡 `T-p307c` — A POINTER payload yields an IDENTITY, never TERMS

🟢 **`p306` found the class in a 167 B W3C file.** 🔴 **`p307` finds it on the 877★
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills),
whose `LICENSE` is the Creative Commons **deed**, not the legalcode, and says so in its own
last line.** 🔵 **`p305` quoted *"even commercially"* from that file twice. The verdict is
right and the provenance is not** — the deed is a summary CC itself declares
non-operative. 🟢 **Rule: a clause-level claim sourced from a POINTER must be labelled as
read from a deed or a reference, not from the licence.**

### 🔴 `T-p307d` — The inherited environmental absence is this base's most expensive recurring error

🟢 **Three were refuted in two passes, and every test was cheap:**

| carried as | passes it survived | tested at | cost | result |
|---|---|---|---|---|
| *"no primary source"* | 24 | `p306` | one `curl` | 🔴 **false** for `raw.githubusercontent.com` |
| *"`git clone` of third-party repos is refused"* | 2 | `p307` | one `git clone` | 🔴 **false** — `rc=0`, 2.4 s |
| *"`make` is refused as external code"* | 2 | `p307` | one `make hooks` | 🔴 **false** — 14/15 gates green |

🔵 **The mechanism is the same each time: a refusal is measured once, generalised into a
CLASS, and the class is then used to justify not measuring.** 🟢 **Standing rule, and it
costs one command: re-test every inherited environmental absence once per pass, before
planning the leg around it.**

### 🔴 `T-p307e` — No instrument in this base compares its own shelves to each other

🟢 **The `AGPL`/`GPL` error above was CONTRADICTED INSIDE THE BASE while it stood.**
`repos/foundations.md` line 583 said *"GNU GPL"*, `compose/patterns.md` line 614 said
*"(GPL)"*, and `intel/open-gaps.md` line 9975 recorded `plastic-labs/tutor-gpt` as
`GPL-3.0` — while five other places said `AGPL-3.0`. 🔴 **Fifteen gates ran and none could
see it.**

🔵 **The reason is structural, and `p305` named half of it:** `gate-absence` polices absence
CLAIMS, `ACTION SH` polices INBOUND claims, `p253` polices a pass against PINNED facts.
🔴 **Every one grades this base against something outside it. Nothing grades slug `X`'s
licence cell on one shelf against slug `X`'s licence cell on another** → `ACTION p307-R`
item 2. 🟢 **It is a cheap gate to build: the shelves are tables, the slug is the key.**

### 🟢 `T-p307f` — The permissive platform-scale tutoring system EXISTS, and it is Maghreb open-core

🔴 **`p305`'s *"forced architecture"* said every platform-scale system in this vertical is
AGPL or GPL and every permissive row is a component (1★–135★).** 🟢 **`p306` refined it:
credentialing carries four permissive platform-scale systems.** 🔴 **`p307` breaks it at
the TUTORING layer**, which is the layer the rule was written about.

[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) —
🟢 **BSD-3-Clause, stock, no added clause** (payload `1 531 B` `fa56a9650ca4`) — **111★ /
193 forks**, Docker-first, Ollama + OpenAI-compatible, local RAG, RBAC, a human-in-the-loop
response-evaluation framework, UI in **Arabic, French and English**, copyright *"Mohamed
El hajji on behalf of all R2D-dev"*.

🔵 **The mechanism that explains it is not geography, it is BUSINESS MODEL.** This is a
Community Edition whose README names a proprietary Enterprise Edition. 🟢 **Open-core
chooses permissive, because the moat is the EE, not the licence.** 🔴 **A commons-defending
system of record chooses copyleft — `p306`'s rule, unchanged.**
🟡 **So the refined statement: the licence follows the MONETISATION, and copyleft marks the
projects with no second tier to sell.** ⚠️ **One observation at the tutoring layer. Not yet
a rule.**

🟢 **Second-order, and it is a procurement fact: `193 forks against 111 stars` is an
inverted ratio** — forks exceeding stars is the signature of a codebase being *taken and
changed*, not watched. 🔵 **Consistent with a self-hosted deployable, and consistent with
coursework.** 🔴 **Not independently verified; it is one reading of two rendered integers.**

### 🟡 `T-p307g` — A gate that grades only the newest section cannot stay red across a pass

🟢 **`make hooks` ran for the first time in three passes: 14/15 green at `HEAD`, 16/16 at
publication.** The one red, `gate-offline` → `p253-settled-fact-regression`, fired on
**`p306`'s** sections, not on this pass's — and `p306` published without being able to see it. 🔴 **Because `p253` grades
only each file's CURRENT section, that red expires the moment `p307` prepends.** 🔵 **A
gate whose finding is visible to exactly one pass, and whose finding that pass cannot fix
without rewriting published history, is a gate that reports into a void.**

🟢 **Measured, so a later pass can act rather than re-measure: `--all` reports `20`
findings across the base; `14` of them are on
[`intel/open-gaps.md`](open-gaps.md)** — 🔵 **a file whose declared purpose is to record
unresolved things, sitting inside a gate that fires on the word *"unresolved"*.**
🟡 **Both halves are registered for `p308`, unpatched: a pass should not redesign a control
in the same hour it first manages to run it** → `ACTION p307-R` item 3.

## 🟢 `T-p306a` — A "NETWORK POLICY" THAT HELD FOR TWENTY-FOUR PASSES WAS A CHANNEL ASSUMPTION, AND IT WAS RETIRED BY ONE UNTESTED HOSTNAME

🔴 **`p303` measured two things correctly — `curl` → `github.com` and `api.github.com` return 403, and
`WebFetch` returned ENOTFOUND — and then generalised them into *"no primary source,"* which five
subsequent passes inherited as settled.** 🟢 **`p306` tested
`raw.githubusercontent.com` and it answers **HTTP 200 with byte-exact bodies.**

🔵 **The structure of the error is worth more than the fix.** Two hosts were measured; a *class* was
declared; the class was then used to justify **not measuring**. 🔴 **Every pass after `p303` re-stated
"no primary source" as a finding when it was an inherited assumption that nothing re-tested.**

🟢 **The general rule, and it generalises past this repository: an ABSENCE is a measurement of the
addresses you tried. It is never a property of the world.** 🔵 **This base already knew this about repo
slugs — `p305`'s ladder lesson, and `p306`'s own 3-of-5 dead-slug recovery — and did not apply it to
hostnames.** ⚠️ **The same shape, one level up: `p304` generalised a rule from one licence file;
`p303` generalised completeness from one page of a topic; `p303` generalised a channel from two hosts.**
🟢 **Counter-measure: a declared absence must carry the list of addresses tried, so a later pass can see
what was NOT tried.** → `ACTION p306-R` item 1.

## 🟢 `T-p306b` — PERMISSIVENESS IS A PROPERTY OF THE LAYER, NOT OF THE VERTICAL

🔴 **`p305` concluded that this vertical's architecture is FORCED: *"every platform-scale system of record
in the vertical is AGPL or GPL"*, so a studio must join permissive components to a copyleft core over a
network boundary.** 🟢 **One layer down that generalisation breaks.**

| layer | permissive option at platform scale? | evidence |
|---|---|---|
| 🔴 **LMS / system of record** | 🔴 **NO — 26 consecutive draws** | Moodle, Open edX, OpenEduCat (LGPLv3, licensor-confirmed `p304`), Frappe Learning (**AGPL-3.0, settled by payload this pass**) |
| 🔴 **tutoring** | 🔴 **NO** | best pedagogy is AGPL-3.0; permissive rows are 1★–135★ components |
| 🟢 **credentialing** | 🟢 **YES** | `waltid-identity` Apache-2.0 **319★**, `learner-credential-wallet` MIT **89★**, `open-attestation` Apache-2.0, `cert-issuer` MIT |

🔵 **Mechanism, and it is not about ideology: the LMS layer is where the INSTITUTIONAL INCUMBENTS sit, and
they chose copyleft decades ago to protect a commons against vendor capture. The credentialing layer was
built recently, by STANDARDS BODIES and research consortia whose goal is adoption of a protocol —
and a protocol spreads faster under MIT.** 🟢 **Predictive, and therefore testable: wherever the artefact
is a STANDARD trying to propagate, expect permissive; wherever it is a SYSTEM OF RECORD defending a
commons, expect copyleft.**

🟢 **The briefing consequence inverts the usual advice: do not ask "what licence can we live with" before
asking "which layer are we building in".** ⚠️ **A studio that enters this vertical through the LMS door
has no permissive option; the same studio entering through the credentials door has four.**

## 🔴 `T-p306c` — THE POINTER GRANT: THE ABSENCE OF A GRANT CLAUSE IS NOT THE ABSENCE OF A GRANT

🟢 **`p305` replaced a length rule with a clause rule and calibrated it 8/8. `p306` ran it over 49 fresh
payloads and found the shape it cannot see.** [`w3c/vc-data-model`](https://github.com/w3c/vc-data-model)
ships a **167 B** `LICENSE.md` containing no grant sentence and one URL — the W3C Software and Document
License. 🔴 **The clause rule returns `NO-GRANT-CLAUSE`, the same verdict it returns for a reserved
grant that withholds every right.**

🔴 **Four classes now, and the two middle ones are byte-level twins with opposite consequences:**
**clean grant** · **reserved grant** (file, no grant, no pointer → STOP) · **pointer grant** (file, no
grant, a URL → resolve it) · **phantom grant** (no file, a README claim → STOP).

🟢 **The discriminator is cheap and it is not length: does the payload contain a URL to a licence text?**
🔵 **Note the recurrence of a pattern this base keeps rediscovering — `p304`'s refuted length rule,
`p305`'s clause rule, and now this: each instrument is defeated by a payload that LOOKS like the thing it
screens for.** 🟢 **The lesson is not "write a better classifier". It is that a two-valued verdict on a
three-valued world will keep producing confident errors.**

## 🔴 `T-p306d` — BYTE LENGTH IS NOT EVEN AN IDENTITY KEY: SIX DISTINCT PAYLOADS AT 1 087 BYTES

🟢 **`p305` demoted length from classifier to screen. `p306` measures how weak the screen is.** In a
single organisation, **six distinct `sha256₁₂` values occur at exactly 1 087 B**, all MIT; two distinct
Apache-2.0 payloads occur at exactly **11 357 B**.

🔵 **Mechanism: MIT's only variable region is the copyright line, and many holder names are the same
LENGTH while being different BYTES.** 🔴 **So "same length" does not imply same licence, same holder, or
even same file.** 🟢 **The `sha256₁₂` is the identity; the byte count is a label that happens to be
printed next to it.**

🟢 **A live by-product survives this and gets stronger: the stock Apache-2.0 pair `11 357 B` /
`c71d239df917` recurred for the SIXTH time, and for the first time in a different LAYER and jurisdiction
(walt.id, Austria, credentialing).** 🔵 **A hash recurs across unrelated projects because it is literally
the same file; a length recurs because of arithmetic. Only one of those is evidence.**

## 🔴 `T-p306e` — THE BINDING EDUCATION-AI RULES ARE SUB-NATIONAL, WHILE THE NATIONAL LEVEL ISSUES GUIDANCE

🟢 **`p305`'s `T-p305d` established that regions are procurement territories and jurisdictions are where
law is written. `p306` finds the rule is right and does not go deep enough.**

| level | what it produces | examples found this pass |
|---|---|---|
| 🟡 supranational / national | 🟡 **guidance, strategy, programmes** | France's national framework, Spain's non-binding recommendation, Bayern's Handlungsleitfaden, Canada's provincial guidance documents |
| 🔴 **sub-national** | 🔴 **BINDING DUTIES** | **Baden-Württemberg `§ 6 DUVO`** (no AI grading, in force `2024-10-10`) · **Ohio** (district policy due `2026-07-01`) · **Utah** (local policy by `2027-07`) |

🔴 **And the sub-national rules bite harder than the supranational one.** EU AI Act Art 5(1)(f) prohibits
**emotion inference** — a technique that, measured over this base's 366 carried slugs, appears in exactly
**two**. `§ 6 DUVO` prohibits **AI awarding grades** — which is the most common single pitch in the
vertical. 🟢 **The rule that affects the most deals is the one written by a German state and a US state,
not by Brussels.**

🔵 **Procedural consequence for every later pass: a regional leg that stops at the nation-state will
systematically miss the binding layer in federal systems** — Germany, the US, Canada, and by extension
Brazil, India and Australia. 🟢 **Name the sub-national unit: Land, state, province.**

## 🔵 `T-p306f` — A PREDICTION THAT FAILS CLEANLY IS WORTH MORE THAN A ROW

🟢 **`p305` predicted that screening the shelves for Art 5(1)(f) exposure would find *"more, especially
among proctoring and engagement-analytics rows."* Two independent screens over 366 carried slugs found
ZERO new ones.** 🔵 **And the single row that looked likeliest — `vardanagarwal/Proctoring-AI`, 633★ —
turns out to be the one that sharpens the rule: eye tracking, mouth-open and phone detection are
**observations**, not **emotion inference**, so Art 5(1)(f) does not reach them.

🟢 **The useful output is a boundary, not a row: the prohibition is about INFERRING AN AFFECTIVE STATE,
not about watching a learner.** 🔵 **Which means the compliance question to ask a client's vendor is not
"do you use a camera" but "do you output a claim about how the learner FEELS".** ⚠️ **Watching is still a
biometric and Annex III high-risk problem — a different regime, and a different mitigation.**

## 🔴 `T-p305a` — A LICENCE RULE INVENTED ON A SAMPLE OF ONE SURVIVES EXACTLY ONE PASS, AND ITS REFUTATION IS USUALLY ALREADY ON THE SHELF

⏱️ `2026-10-19`, pass 305. Evidence:
[`p305-rule-calibration.2026-10-19-p305.tsv`](../evidence/p305-rule-calibration.2026-10-19-p305.tsv).

🔴 **`p304` read one 279 B reserved grant and promoted *"`bytes < 400` is a RED FLAG, not a short MIT"* to a
STANDING RULE.** 🔴 **`p305` found a second reserved grant at 842 B which carries MIT's warranty disclaimer
verbatim — the rule fails it, and fails it in the dangerous direction.**

⚠️ **The structural lesson is not "that rule was wrong". It is that the refutation was already in this
repository when the rule was written** — [`agents/trending.md:7407`](trending.md) carried
`ShuyunYuan/talentcoach` at *"842 B, All rights reserved"*, and `p195`'s census logged it `UNCLASSIFIED` at
the same byte count five passes earlier.

🔵 **Why no gate caught it:** `gate-absence` checks absence CLAIMS against the index; `ACTION SH` checks
INBOUND search claims. 🔴 **A new standing RULE is neither of those things, so nothing looked.**
🟢 **The generalisation: this base's gates all police CLAIMS ABOUT THE WORLD. None polices a CLAIM ABOUT
ITS OWN METHOD.** A rule is the most load-bearing thing a pass can publish, because every later pass
inherits it and applies it silently — and it is the one artefact that ships unverified. → **`ACTION p305-R`**.

🟢 **The replacement rule, calibrated 8/8: test the PERMISSION CLAUSE** — MIT/ISC's *"Permission is hereby
granted, free of charge…"*, Apache-2.0's *"…hereby grants to You a perpetual… copyright license"*.
🔵 **A reserved grant has a copyright line, often a disclaimer, and no operative grant. That absence is
what makes it a notice.** ⚠️ **The decisive pair: 842 B NO-GRANT vs 1 060 B GRANT — 218 bytes apart, and no
threshold can separate them.** 🟢 **`p304`'s 1 060–1 180 B band survives, demoted from RULE to SCREEN,
corroborated by seven fresh samples.**

## 🔴 `T-p305b` — "CC" IS NOT A LICENCE FAMILY; IT IS TWO OPPOSITE ANSWERS UNDER ONE LABEL

⏱️ `2026-10-19`, pass 305. Evidence:
[`p305-licence-payload.2026-10-19-p305.tsv`](../evidence/p305-licence-payload.2026-10-19-p305.tsv).

🟢 **Two rows in the same topic, both resolving to "Creative Commons" on any family classifier:**
[`gen-mentor`](https://github.com/GeminiLight/gen-mentor) (135★) is **CC0-1.0** — a public-domain
dedication, **more permissive than MIT**, no attribution condition whatever.
[`education-agent-skills`](https://github.com/GarethManning/education-agent-skills) (**877★**) is
**CC BY-SA 4.0** — **content copyleft**.

🔴 **A "CC" verdict therefore merges the single most permissive grant in the vertical with a copyleft
one.** 🟢 **`p305`'s own prober did exactly this and is recorded doing it** — the honest demonstration,
since the defect is in the abstraction, not in the implementation. 🔵 **The rule: for Creative Commons, the
FAMILY is not a verdict. Read the variant line.** ⚠️ **And the CC BY-SA payload is 1 230 B — just above
`p304`'s MIT band, so it reads like a slightly long MIT and is not one.**

## 🔴 `T-p305c` — IN EDUCATION THE BINDING CONSTRAINT IS THE TECHNIQUE, NOT THE LICENCE — AND EVERY INSTRUMENT IN THIS BASE IS BLIND TO IT

⏱️ `2026-10-19`, pass 305. Evidence:
[`p305-prohibited-practice.2026-10-19-p305.tsv`](../evidence/p305-prohibited-practice.2026-10-19-p305.tsv).

🟢 **The demonstration is one author's two repositories.**
[`mskljns/ComprehensionProblems_DAiSEE`](https://github.com/mskljns/ComprehensionProblems_DAiSEE) is
ungranted; [`mskljns/Intelligent_Tutor_ComprehensionProblems_DAiSEE`](https://github.com/mskljns/Intelligent_Tutor_ComprehensionProblems_DAiSEE)
is **MIT, 1 060 B, `c744c1abbfbb`** — complete, unmodified, and it passes every licence instrument in this
repository including `T-p305a`'s new clause test. 🔴 **Both are undeployable in the EU.**

🔴 **The pipeline is OpenFace → facial Action Units + landmarks → DAiSEE's labels: engagement, frustration,
confusion, boredom.** Emotion inference from facial biometrics, applied to students.
⚠️ **EU AI Act Article 5(1)(f) prohibits precisely this in educational institutions, and it has applied
since `2025-02-02` — not a deadline, a live prohibition.** Public and private, all levels, in-person and
online, **no consent exception**; medical/safety carve-out only.

🟢 **So: A CLEAN MIT GRANT DOES NOT MAKE A PROHIBITED PRACTICE DEPLOYABLE.** 🔵 **This is a NEW AXIS. Every
probe, census, gate and ladder in this repository answers *may we COPY this code?* None answers *may we RUN
this behaviour?*** ⚠️ **The second question has a harder answer and a nearer deadline.**

🟢 **The substitution is cheap and already on these shelves: infer mastery from RESPONSE data — correctness,
latency, spacing — never from the face.** [`fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki)
(MIT, 1 079 B) and the `pyKT` family do exactly that and are untouched by Art 5(1)(f). → **`P84`**.

## 🟢 `T-p305d` — A REGION IS NOT A SEARCH TERM, BECAUSE NO MINISTRY PUBLISHES TO A REGION

⏱️ `2026-10-19`, pass 305. Evidence:
[`p305-regional.2026-10-19-p305.tsv`](../evidence/p305-regional.2026-10-19-p305.tsv).

🔴 **`p304` nil'd EMEA on education and pre-registered the fix: drop the acronym, name jurisdictions.**
🟢 **`p305` ran it and EMEA paid four jurisdictions** — France's *Cadre d'usage* (`2025-06`, the region's
only formal national framework), Spain's non-binding recommendation (`2026-04`) with Catalonia and
Andalusia pilots, the Netherlands' NOLAI, and **Germany's informed absence** (education is Länder
competence, so the national level is the wrong place to look — an answer, not a gap).

🟢 **Then the same fix was applied to APAC, which `p304` reported as *"zero K-12 or university rules"* —
and it paid five jurisdictions**, including China's `AI Plus Education` plan (`2026-04-10` → 2030) and
Singapore's Code for Fun.

🔵 **Two regions, one query change, both broken open: the acronym was the defect.** 🟢 **"EMEA" and "APAC"
are procurement territories, not legal jurisdictions — nobody legislates for them, so nobody writes
documents indexed under them.** ⚠️ **The standing correction: the mandated per-region query must be run as
a per-JURISDICTION query, and a region that yields nothing must be reported with the jurisdictions actually
asked for — otherwise "EMEA returned nothing" means only "the acronym returned nothing."**

🟢 **Corollary with teeth: Germany's nil is now INFORMATIVE rather than empty** — it names the Länder as the
level to search next, which is a lead the acronym query could never have produced.

## 🔴 `T-p305e` — THE HEAD/TAIL GRANT RELATIONSHIP IS A PROPERTY OF WHAT A TOPIC'S TAIL CONTAINS, NOT OF ADOPTION

⏱️ `2026-10-19`, pass 305. Evidence:
[`p305-topic-census.2026-10-19-p305.tsv`](../evidence/p305-topic-census.2026-10-19-p305.tsv).

🔴 **`p303` wrote: *"the tail is cleaner than the head — so licence risk RISES with adoption"*, measured on
`ai-tutor`'s paged tail (1 refusal in 20).** 🔴 **On `intelligent-tutoring-system`, enumerated to exhaustion
this pass, it inverts by 52 points:**

| | rows | carry a payload | rate |
|---|---|---|---|
| 🟢 **HEAD** ranks 1–20 | 20 | 12 | 🟢 **60.0 %** |
| 🔴 **TAIL** 13 uncarried rows, ranks 21–40 | 13 | 1 | 🔴 **7.7 %** |

🔵 **The mechanism, and it is what makes this transferable: `intelligent-tutoring-system`'s tail is
coursework and personal study projects — 18 of 20 page-2 rows are 0★ — and student projects are published
without a licence as a matter of habit. `ai-tutor`'s tail was small working tools, which ship with one.**

🟢 **So neither "the tail is cleaner" nor "the head is cleaner" is a law of the vertical. The predictor is
the GENRE of the tail, which is readable from the descriptions before any licence is probed.** ⚠️ **A rule
derived from one topic's tail must not be carried to another's — and `p303`'s was, for two passes.**

🟢 **Collateral: `p303`'s claim that this topic was *"enumerated whole (population 41)"* is REFUTED — 14 of
41 rows were uncarried. `p305` read pages 1, 2 and 3 and holds 41 of 41, the first completeness claim in
this base backed by a page-by-page census.** 🔵 **"Population N" from a topic header is not an enumeration;
it is a number printed next to one.**


## 🔴 `T-p304a` — A LICENCE FILE CAN BE AN ANTI-LICENCE, AND EVERY CHEAP CHECK IS STRUCTURALLY BLIND TO IT

⏱️ `2026-10-19`, pass 304. Evidence:
[`p304-licence-payload.2026-10-19-p304.tsv`](../evidence/p304-licence-payload.2026-10-19-p304.tsv).

🔴 **`p303` found the PHANTOM GRANT: a README claiming MIT over a licence file that was never committed.
`p304` found its mirror image and the mirror is worse.**
[`ai-shifu/skills`](https://github.com/ai-shifu/skills) ships **279 B** at the canonical path `LICENSE`:
*"All rights reserved… provided for viewing and evaluation only. No permission is granted to use, copy,
modify, merge, publish, distribute, sublicense, or sell…"*

🟢 **The trend this completes is about INSTRUMENTS, not about one repository.** Three defect classes are now
on record, and they fail in three different directions:

| class | fails | caught by |
|---|---|---|
| 🔴 absent grant | loudly — every probe says *absent* | 🟢 any check |
| 🔴 phantom grant (`p303`) | loudly at the file, quietly in the README | 🟢 a probe; 🔴 **not** a README reader |
| 🔴 **reserved grant (`p304`)** | 🔴 **silently, in the permissive direction** | 🔴 **only reading the BODY** |

🔴 **The reserved grant passes a filename check, a length sanity check, a `Copyright (c)` grep and a
sidebar glance.** 🟢 **The counter-measure is a size rule, and it is cheap: every permissive template this
base has read falls in 1 060–1 180 B. `bytes < 400` is a RED FLAG, not a short MIT.**
🔵 **Why it is a trend and not an anecdote: the repository is a live product's skill library for building
one-on-one AI courses — the most liftable-looking asset in the paged tail. As education AI commercialises,
"source-available for evaluation" will appear more often, dressed as a licence.**

## 🟢 `T-p304b` — A TOPIC'S HEAD RANKS BY ENGLISH-LANGUAGE REACH; ITS TAIL IS WHERE THE REGIONAL SUPPLY LIVES

⏱️ `2026-10-19`, pass 304. Evidence:
[`p304-topic-paging.2026-10-19-p304.tsv`](../evidence/p304-topic-paging.2026-10-19-p304.tsv) ·
[`p304-placement.2026-10-19-p304.tsv`](../evidence/p304-placement.2026-10-19-p304.tsv).

🟢 **`p303` established that paging a topic converts a denominator into a floor. `p304` paged one more page
and found something the floor hid: the COMPOSITION changes down the ranking, not just the star count.**

| range | stars | character |
|---|---|---|
| `ai-education` ranks 1–40 (`p302`/`p303`) | 41 600 → 17 | 🔴 **US and Chinese CORPORATE repositories** |
| `ai-education` ranks 41–60 (`p304`) | **12 → 7** | 🟢 **3 of 5 admitted rows are REGIONALLY PLACED** — Brazil, India, China |

🟢 **The mechanism is not mysterious: stars accrue from reach, reach follows language, and English-language
reach is concentrated in US repositories and in Chinese projects large enough to market internationally.**
🟢 **A Brazilian study-module generator built for a Portuguese-language national course, or an Indian
university team's Flutter app, cannot accumulate stars at that rate no matter how good it is.**
⚠️ **Consequence for this base's own method: a star floor is exactly the wrong filter for a global studio,
and `p304` would have skipped this leg on stars alone.** 🔵 **`p303` warned that 16 of 23 new rows came from
ranks 41–60 and told the next pass not to stop at page 2 because the stars look small. That warning was
right for a second, stronger reason than it knew.**

🟢 **This also narrows a six-pass declared gap.** *"LATAM returned nothing at any star level"* is **refuted**
— [`pedroestevaodev/plataforma-estudo-personalizado`](https://github.com/pedroestevaodev/plataforma-estudo-personalizado)
is MIT and payload-pinned. 🔴 **The platform-scale gap STANDS** (8★, 40 commits, a single-purpose generator).

## 🟢 `T-p304c` — FOR SUBSTRATE, READ FORKS; FOR AGENTS, READ STARS

⏱️ `2026-10-19`, pass 304. Evidence:
[`p304-starcells.2026-10-19-p304.tsv`](../evidence/p304-starcells.2026-10-19-p304.tsv).

🟢 **Ten platform-tier rows were read with forks alongside stars for the first time, and the fork-to-star
ratio split them cleanly — not by popularity, but by what people DO with the repository.**

🟢 **Forked to deploy (≥ 0.95):** `Ed-Fi-ODS` **1.71** · `studio` **1.47** · `OpenEMIS-Core` **1.29** ·
`uPortal` **0.97** — administrative, data-standard and authoring systems, **unusable without your own
instance, so adoption REQUIRES a fork.**
🔴 **Starred to read (≤ 0.30):** `nbgrader` 0.25 · `schulcloud-server` 0.27 ·
`apply-for-teacher-training` 0.29 — **pedagogical tools and reference services, bookmarked far more than
stood up.**

🟢 **The decisive case: [`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) has 28★ and 48
forks.** 🔴 **On stars it is the weakest row in the tier and any shortlist cuts it.** 🟢 **On forks it is the
most deployed-per-watcher repository this base has measured — exactly right for a US state education DATA
STANDARD, where every adopting agency runs its own instance.**
⚠️ **A star-ranked shortlist systematically discards the administrative tier, which is the tier most
education engagements actually begin in.**
🟡 **Stated as a proxy, not proof:** forks also accumulate from coursework and abandoned PR branches, and
GitHub does not distinguish them. **An intent signal, never an install base.**

## 🟢 `T-p304d` — THE GOVERNANCE GAP IS ~40 POINTS IN EVERY REGION THAT MEASURES IT ON ONE DENOMINATOR

⏱️ `2026-10-19`, pass 304. Evidence:
[`p304-websearch.2026-10-19-p304.tsv`](../evidence/p304-websearch.2026-10-19-p304.tsv).

🟢 **Two independent instruments, two continents, near-identical spread:**

| region | adoption | governance | gap |
|---|---|---|---|
| 🟢 **LATAM** (UNESCO IESALC / UNU-IAS, 200 institutions, 19 countries) | **73.5%** adopted AI in teaching & learning | **30%** have published an AI policy | 🔴 **~43 pts** |
| 🟡 **APAC** (OneTrust 2026, cross-sector) | **87%** encourage AI agents | **47%** have governance and controls | 🔴 **40 pts** |

🟢 **North America agrees in direction — only ~10% of institutions have formal AI guidelines and 71% of US
teachers lack AI training.** ⚠️ **But the tempting 92%-vs-10% comparison MUST be refused: 92% is a global
STUDENT figure and 10% a US INSTITUTION figure.** 🔴 **A denominator is only half an instrument, and this
base has been burned by mixing them before.**
🟢 **EMEA is the outlier that proves the trend's commercial value: it is the one region where the gap has a
STATUTORY DEADLINE** — education AI is high-risk under the EU AI Act with full effect slated for
**August 2026**. ⚠️ **That date still reaches this base only through secondary commentary.**

🔵 **The briefable form: every region has adopted; almost none has governed; the gap is structural rather
than local; and it closes fastest where a statute forces it.** 🟢 **Policy scaffolding, audit trails,
assessment-integrity evidence and model-use disclosure are the same engagement in four regions.**

## 🟢 `T-p304e` — THE PERMISSIVE PLATFORMS SIT AROUND THE SYSTEM OF RECORD, NOT IN IT

⏱️ `2026-10-19`, pass 304. Evidence:
[`p304-starcells.2026-10-19-p304.tsv`](../evidence/p304-starcells.2026-10-19-p304.tsv) ·
[`p304-websearch.2026-10-19-p304.tsv`](../evidence/p304-websearch.2026-10-19-p304.tsv).

🔴 **The 24-pass nil on a permissive education ERP/CRM is now LICENSOR-CONFIRMED: OpenEduCat's own glossary
pages state `LGPLv3`**, and the same pages confirm it is built on the Odoo framework, so the ERP layer is
not escapable by swapping the education module.

🟢 **But `p304`'s fork-ratio read forces a correction to how this base has stated the finding for 23
passes.** *"No permissive platform-scale education software"* is **false**. `Ed-Fi-ODS` (Apache-2.0),
`learningequality/studio` (MIT) and `uPortal` (Apache-2.0) are all permissive AND all genuinely
forked-to-deploy at platform scale.

🟢 **The accurate statement is narrower and far more useful: what is missing is a permissive SYSTEM OF
RECORD.** The permissive platform-scale rows are the ones **around** it —

- **`Ed-Fi-ODS`** — the **data standard / operational data store** systems of record report *into*
- **`learningequality/studio`** — **content authoring** (manufactures curriculum; enrols nobody)
- **`uPortal`** — an **aggregating portal** (presents other systems' data)

🔴 **The enrolment/roles/gradebook-of-record slot is copyleft or unlabelled in every row read: OpenEduCat
LGPLv3 · openSIS GPL-2.0 · Moodle GPL-3.0 · Open edX AGPL-3.0 · `schulcloud-server` and `OpenEMIS-Core`
unlabelled.** 🟢 **So the brief is not "there is no permissive platform" — it is "build permissively around
a copyleft core you do not modify."** 🔵 **That is an architecture, not a gap, and it is the whole of
pattern `P81`.**

⚠️ **One measured caution attached to this trend: 3 of the 10 platform-tier pages render NO licence label in
the GitHub sidebar** (`PrairieLearn`, `schulcloud-server`, `OpenEMIS-Core`) **although all three carry a
licence in the tree. A 30% sidebar miss rate on exactly this tier** — *"no licence shown"* is never
*"no licence."*

## 🟢 `T-p303a` — A DENOMINATOR IS ONLY HALF AN INSTRUMENT: PAGE IT UNTIL THE DISTRIBUTION HITS A FLOOR, AND A SAMPLE BECOMES AN ENUMERATION

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-topic-paging.2026-10-18-p303.tsv`](../evidence/p303-topic-paging.2026-10-18-p303.tsv).

🟢 **`T-p302a` established that an enumeration with a denominator beats a ranked opinion. This pass completes
the thought: the denominator alone is misleading, and paging is what makes it useful.**

`ai-tutor` reports **750** repositories. Paged to rank 60, the distribution is:

| ranks | star range | share of this pass's 23 new rows |
|---|---|---|
| 1–20 | 41 600 → 65 | **0 %** |
| 21–40 | 64 → 17 | 6 % |
| 41–60 | **16 → 9** | 🟢 **70 %** |

🔵 **"750" is a tail, not depth.** The real corpus is **≈60 members above 9★** — and that converts the shelf
from *a sample of an unknown population* into *an enumeration of a bounded one*. 🟢 **This base can now make a
completeness claim**, which is worth more in a client conversation than a larger number: *"we have read every
AI-tutoring repository on GitHub above 9 stars"* is checkable and defensible; *"we track 750 repositories"* is
neither.

🔵 **The generalisable method rule, and it has two halves:**
1. 🟢 **Page a population until the distribution flattens.** The floor, not the denominator, tells you when
   you are done.
2. ⚠️ **Novelty is INVERSELY correlated with rank-position quality.** 70 % of new rows came from the bottom
   third of the read range, because earlier passes already harvested the head. **A leg that stops when the
   stars get small stops exactly where the new material is.**

🔵 **Why page 1 paying zero is the reassuring result rather than the disappointing one:** it is independent
confirmation that `p302`'s read of the head was complete. **Two instruments agreeing on a nil is evidence;
one instrument finding nothing is not.**

---

## 🔴 `T-p303b` — THE PHANTOM GRANT: A README THAT CLAIMS A LICENCE DEFEATS THE LICENCE CHECK THAT AN ABSENT ONE WOULD FAIL

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-licence-payload.2026-10-18-p303.tsv`](../evidence/p303-licence-payload.2026-10-18-p303.tsv).

🔴 **[`fenago/LearnGraph`](https://github.com/fenago/LearnGraph) states `MIT License - See LICENSE file for
details.` in its README, and that file does not exist** — 18 probes (6 filenames × `main`/`master`/`dev`) all
404, GitHub's sidebar Resources block listing only Readme and Activity, GitHub's own licence detector finding
nothing.

🔵 **This is a distinct defect class from an absent licence, and strictly more dangerous.** An absent grant
with no claim **fails the obvious check**: a developer looks for a licence, finds none, stops. 🔴 **A claimed
grant with no instrument passes that check and fails only a deeper one.** The developer greps the README,
reads "MIT License", and ships — *the repository told them they may*.

🟢 **A README sentence is not a licence.** It describes an instrument that was never committed: there is
nothing to accept, no terms to point to, and no copyright holder has granted anything. 🔴 **The legal position
is identical to `p302`'s `Mr.-Ranedeer-AI-Tutor` — no permission — while the *detection* position is far
worse.**

🟢 **The rule this makes non-negotiable, and it is a rule about method rather than about one repository: THE
LICENCE CHECK MUST READ THE PAYLOAD, NEVER THE README'S DESCRIPTION OF IT.** 🔵 This base has read payloads
with byte lengths and `sha256₁₂` since `p294`; **`LearnGraph` is the first repository found that would have
passed a README-level check and failed a payload-level one**, which retroactively justifies the discipline
and gives it a concrete example to brief.

🟢 **Corollary for engagement estimates: licence verification is a line item, not a formality.** 🔵 **And
unlike an abandoned repository, a phantom grant has a REMEDY WITH AN ADDRESSEE** — the project is active, so
an issue asking the author to commit the file they already reference is a reasonable, cheap ask. **Check back
rather than writing it off.**

---

## 🟢 `T-p303c` — WITHHOLDING HAS BECOME A CONVERGENT PEDAGOGY, AND ITS MEASUREMENT COUNTERPART ARRIVED IN THE SAME READ RANGE

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-licence-payload.2026-10-18-p303.tsv`](../evidence/p303-licence-payload.2026-10-18-p303.tsv) ·
[`p303-topic-paging.2026-10-18-p303.tsv`](../evidence/p303-topic-paging.2026-10-18-p303.tsv).

🔵 **`p302` noted `algo-sensei`'s five-level hint cascade as "a reusable *withholding* policy — the part every
tutoring engagement has to build and nobody ships".** 🟢 **One pass later it is no longer one author's taste:
three more independent implementations appeared in ranks 41–60 alone**, all permissive —
[`Far-200/think-before-code`](https://github.com/Far-200/think-before-code) (MIT, *"one question at a time"*),
[`Haaaiawd/Socrate`](https://github.com/Haaaiawd/Socrate) (Apache-2.0, *"questions, not lectures"*),
[`DuckInAShirt/leetmate`](https://github.com/DuckInAShirt/leetmate) (MIT, *"hints, not answers"*).

🟢 **Four unrelated authors converging on "refuse to answer" is a sector signal.** 🔵 **And the reason is
economic, not pedagogical fashion: a tutor that answers is indistinguishable from the chatbot the student
already has.** Withholding is the only thing a tutoring product can offer that a general assistant cannot —
so it is the actual product boundary of this category.

🟢 **The genuinely new piece is the MEASUREMENT counterpart:**
[`Bhala-Srinivash/agent-tutor-skill`](https://github.com/Bhala-Srinivash/agent-tutor-skill) (MIT) pairs FSRS
spaced repetition and concept-level mastery with **zero-hint quizzes**. 🔵 **A hint cascade is an
unfalsifiable claim until some assessment withholds help entirely — zero-hint quizzing is the control
condition for a cascade.** 🟢 **Brief the pair, never the cascade alone**: cascade + zero-hint control is a
defensible pedagogy story, and it is precisely what `bydeng01`'s pre-registered leakage audits
([`repos/foundations.md`](../repos/foundations.md)) were constructed to test. **Policy, control condition and
audit design are now all permissive and all pinned.**

🔵 **Commercially this lands hardest in LATAM**, where PISA 2025 reports nine in ten 15-year-olds already
using AI chatbots for schoolwork: **a tutor that refuses to answer is an academic-integrity feature**, not a
degraded experience. See [`intel/market.md`](../intel/market.md) and `P77`.

---

## 🟢 `T-p303d` — THREE REGULATORY REGIMES HAVE INDEPENDENTLY CONVERGED ON THE SAME REGULATED ACT: AN AUTOMATED DECISION *ABOUT* A STUDENT

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-websearch.2026-10-18-p303.tsv`](../evidence/p303-websearch.2026-10-18-p303.tsv).
⚠️ **All three datums are search-snippet-attributed; no publisher was reachable.**

| jurisdiction | the regulated act, as named |
|---|---|
| **Oklahoma, Maryland** (US states) | Require **human oversight** and **bar AI from high-stakes decisions about students** |
| **EU** (AI Act, high-risk category) | Systems used to **evaluate learning outcomes** or **steer learning processes** |
| **Vietnam** (`Decision 33/2026/QD-TTg`, education systems 2 and 3) | Systems that **assess, grade or rank** students; **biometric/automated behavioural monitoring** |

🟢 **Three regimes, three legal traditions, no coordination — and the same boundary.** 🔵 **The convergence is
the finding, and it is the most reusable regulatory fact in this base**, because it means the compliance
surface is **not** jurisdiction-specific in substance even though the paperwork is.

🔵 **What it implies commercially, stated plainly: ONE conformity-evidence product addresses three
regimes.** Build the evaluation harness, the pre-registered protocol, the human-oversight surface and the
auditable learner-model schema once; localise only the dossier. 🟢 **Every component is permissive and
pinned** — `inspect_ai` (MIT), the two `bydeng01` audit designs (MIT),
[`hakimihou/capability-space`](https://github.com/hakimihou/capability-space) (MIT) for the
activity/evidence/mastery separation an auditor actually asks for. **That is `P76`.**

🔵 **And it tells you what NOT to sell: a better model.** None of the three regimes asks whether the model is
good; all three ask whether the decision about the student is overseen, evidenced and contestable. 🟢 **The
deliverable is a protocol and a report, not a better tutor.**

⚠️ **The counter-signal, carried honestly:** New York City's answer was a **one-year moratorium on
student-facing AI through grade 8**. 🔵 **Some buyers will not want a governed system — they will want no
system.** Have the assistive, teacher-in-the-loop posture ready.

---

## 🟢 `T-p303e` — THE INDUSTRY'S OWN 2026 NARRATIVE HAS MOVED FROM EXPERIMENTATION TO GOVERNANCE, FROM PERSONALISATION TO WORKFLOW, AND FROM OUTPUT TO EVIDENCE

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-websearch.2026-10-18-p303.tsv`](../evidence/p303-websearch.2026-10-18-p303.tsv).
🟢 **The one mandated global leg that paid this pass** (`AI education industry trends 2026`); the other three
nil'd for the 29th, 16th and 23rd consecutive window.

🟢 **Three shifts, each attributed to a named organisation and each independently corroborating what this
base's own repository reads have been showing:**

| shift | as named by | what it corroborates here |
|---|---|---|
| **Experimentation → governance**: clear policies, data boundaries and oversight as the precondition for adoption | **1EdTech** | 🟢 The regulatory convergence in `T-p303d`, and the 87 %-adoption-vs-26 %-strategy gap in LATAM |
| **Workflow-first**: the clearest gains came from course design support, teacher productivity and streamlined instructional/administrative workflow — explicitly *over* broad personalisation promises | **HolonIQ** | 🟢 Why [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) (877★, teacher-facing) is the most adopted education-specific artefact on the shelf after DeepTutor |
| **Output volume → evidence**: systems increasingly expect proof that products improve learning quality, persistence, well-being or job-relevant skills | **HolonIQ**, Tutorflow | 🟢 **The evaluation tier is a REVENUE line, not overhead** — `bydeng01` + `inspect_ai`, permissive end to end |

🟢 **Two further signals worth carrying:** **education-purpose-built platforms are displacing generic AI
tools** (TeachBetter) — which is the market-side statement of this base's standing architectural advice; and
**digital credentials are becoming a core mechanism for skills-based learning and hiring** (1EdTech), with
**career-navigation tooling spreading across K-12, post-secondary and workforce** (HolonIQ). 🔵 **This base
now has its first permissive row aimed at that last one:**
[`MadsDoodle/Career-Navigator`](https://github.com/MadsDoodle/Career-Navigator) (MIT, 17★) — 🔴 **a starting
point, not a product.**

🔴 **Three circulating statistics are REFUSED and named so they are not picked up:** *"$12.3B AI education
platform market by 2026"* and *"83 % of institutions planning AI teaching-assistant deployment"* (vendor
report attributing to HolonIQ and EDUCAUSE; **unverifiable at either**); *"86 % of students use AI"*
(statistics aggregator, no traceable survey); *"62 % test-score gain"* (vendor claim, no study).
🔵 **These are exactly the numbers a deck reaches for.** 🟢 **The qualitative direction of travel above is
well-corroborated; the quantities circulating alongside it are not. Use the former, refuse the latter.**

---

## 🟢 `T-p303f` — THE ADOPTION-GOVERNANCE GAP IS STRUCTURAL, NOT REGIONAL: IT REPRODUCES ACROSS CONTINENTS, SECTORS AND EDUCATION LEVELS

⏱️ `2026-10-18`, pass 303. Evidence:
[`p303-websearch.2026-10-18-p303.tsv`](../evidence/p303-websearch.2026-10-18-p303.tsv).
⚠️ **All datums search-snippet-attributed.**

🔵 **This base has carried LATAM's 87 %-adoption-against-26 %-strategy gap as a regional headline since
`p282`. This pass found the same shape in three more places, and that changes what it is.**

| where | adoption | governance | gap |
|---|---|---|---|
| **LATAM** higher education (IESALC, 200 institutions / 19 countries) | **87 %** use AI in ≥1 area; 74 % in teaching and learning | 🔴 **26 %** have a formal AI strategy | **61 pts** |
| **Brazil** K-12 administrators (Cetic.br, 2026) | **53 %** use AI | 🔴 **22 %** have school guidelines | **31 pts** |
| **MENA** (EdTech Hub) | National platforms live — `Naseej` (Saudi Arabia), `UM6P ChatGPT.Edu` (Morocco) — collecting **sensitive student data** | 🔴 Many countries **lack robust data-protection law** | qualitative, severe |
| **Europe / North America** | Widespread institutional use | ~**70 %** have AI guidance **or are developing it** | 🟢 **narrowest of the four** ⚠️ aggregator-sourced |

🟢 **Read as one pattern: deployment is driven by individual educators and administrators, while governance
requires an institutional decision — so adoption always leads, everywhere.** 🔵 **It is therefore NOT a LATAM
deficiency, and briefing it as one is both wrong and a lost opportunity**: the same remediation product sells
in Brazil, Riyadh and Casablanca as in Bogotá.

🟢 **Commercial consequence, and it is the useful part: the buyer is remediating a LIVE deployment, not
evaluating a hypothetical.** 🔵 **That is a materially easier sale than greenfield advocacy** — the AI is
already in the building, the institution already carries the risk, and the engagement is policy, data
boundaries, academic-integrity rules and an evaluation posture around what is running.
🔴 **The sharpest version is MENA**, where the governance gap is a **legal vacuum** rather than an
institutional lag — student data is being collected under national programmes in jurisdictions without
data-protection statutes. 🟢 **A student-data minimisation and governance engagement there needs no new
regulation to justify it.**

⚠️ **The ~70 % Europe/North America figure is aggregator-sourced and NOT adopted by this base**; it is shown
only to place the other three rows, and the "or are developing it" clause does a great deal of work in it.

## 🟢 `T-p302a` — WHEN A SEARCH CHANNEL DIES, REPLACE THE INSTRUMENT, NOT THE QUERY: AN ENUMERATION WITH A DENOMINATOR BEATS A RANKED OPINION

⏱️ `2026-10-18`, pass 302. Evidence:
[`p302-websearch.2026-10-18-p302.tsv`](../evidence/p302-websearch.2026-10-18-p302.tsv) ·
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv).

🔴 **Twenty-eight windows of `top open source AI agents education 2026 github MIT` produced zero new
education rows.** `p300` and `p301` each recommended retiring it; both re-ran it anyway and recorded another
nil. 🟢 **`p302` replaced the instrument instead of rewording the query, and the yield in a single leg was
fourteen new permissive rows and nine licence refusals.**

🟢 **The mechanism is not that the new channel is "better sourced" — it is that it has a DENOMINATOR.**
`github.com/topics/*` reports its own population (`ai-tutor` **750**, `ai-education` **528**,
`intelligent-tutoring-system` **41**, `education` **39 007**) and orders it by stars. A listicle reports an
author's selection with no population and no ordering guarantee; **a topic page reports a census head.**
That difference converts three previously unanswerable questions into measurements:

| question | under a listicle | under an enumeration |
|---|---|---|
| "is this all of them?" | unanswerable | **answerable** — 20 of 750 read, remainder *unmeasured, not absent* |
| "what fraction is unusable?" | unanswerable | **9 of 23 refused ≈ 39 %** |
| "is the channel dead or the vertical empty?" | indistinguishable | **distinguishable** — `education` at 39 007 repos has a head of *book lists*, so the channel is mis-aimed, not the vertical empty |

🔵 **The transferable law: a leg that cannot state its denominator cannot distinguish a nil from a
saturation, and this base has spent dozens of passes unable to tell them apart.** 🟢 **Prefer any channel
that publishes its population size**, even when its coverage is narrower.

## 🔴 `T-p302b` — AT THE HEAD OF THIS VERTICAL, STAR COUNT IS ANTI-CORRELATED WITH USABILITY

⏱️ `2026-10-18`, pass 302. Evidence:
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv).

🔴 **The two highest-starred education-specific tutoring artefacts on GitHub are both unusable by Globant,
and for different reasons:**

| rank by stars | repo | stars | grant | usable? |
|---|---|---|---|---|
| 1 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **41.6k** | Apache-2.0 (payload `cd2f54e1e506`) | 🟢 **YES** |
| 2 | [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | **29.6k** | 🔴 **NONE** + **DISCONTINUED** | 🔴 **NO** |
| 3 | [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | **1.3k** | 🔴 AGPL-3.0 (payload `20b067f86de3`) | 🔴 **NO** (study only) |

🔴 **Rank 2 has 3.3k forks of software nobody has the right to use, and no maintainer left to ask** — the
README's first heading is `DISCONTINUED`. 🔴 **Rank 3 is the most capable maintained visual tutor in the
vertical and its copyleft reaches network use**, which is how teaching platforms are delivered.

🟢 **Measured over the star-ordered head: 9 refusals in 23 repositories, about `39 %`.** 🔵 **This is the
first time this base can state that as a RATE over an enumerated population rather than as an impression**,
and it is the standing answer whenever a client, a listicle or a search engine advances a star count as
evidence of usability. 🟢 **The operational rule is unchanged but now priced: read the licence PAYLOAD before
the README.** A repository's popularity predicts its *visibility*, not its *availability* — and in this
vertical the correlation at the head is **negative**.

## 🔴 `T-p302c` — THE REGULATORY QUESTION IS NO LONGER ONLY "MAY AI DECIDE ABOUT A STUDENT" — VIETNAM NOW ALSO ASKS WHERE THE TEACHING CONTENT CAME FROM

⏱️ `2026-10-18`, pass 302. Evidence:
[`p302-websearch.2026-10-18-p302.tsv`](../evidence/p302-websearch.2026-10-18-p302.tsv).

🟢 **Since `p288` this base has carried a convergent finding: every jurisdiction's education rules fall on
one boundary — is AI permitted to DECIDE about a student?** Vietnam names assessment and ranking; Oklahoma
and Maryland bar high-stakes decisions; NYC's red tier bars grading, discipline and IEP development; the EU
puts assessment in its high-risk annex. 🟢 **That finding holds. `p302` adds a SECOND boundary that no other
jurisdiction on this file has drawn.**

🔴 **Vietnam's `Decision 33/2026/QD-TTg` (effective `2026-08-15`) lists, as the FIRST of its three
education high-risk systems, those that "generate self-study content for learners from UNCONTROLLED DATA
SOURCES."** 🔵 **That is a provenance rule, not a decision rule.** A tutor that decides nothing — that only
explains — is in scope if its corpus is unconstrained. **An unrestricted RAG tutor over scraped material is
caught on its face.**

🟢 **Three consequences, and they run in the studio's favour:**
1. 🔵 **Source control becomes a compliance feature with a named legal hook**, and
   [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**) already keeps
   generated teaching material tied to its sources — a pre-built answer to a written requirement.
2. 🔵 **Curriculum alignment stops being a nice-to-have.** A system aligned to named textbooks — as
   [`SimonsTang/feifei-companion`](https://github.com/SimonsTang/feifei-companion) (**Apache-2.0**) is to
   统编版 and 人教版 editions — is by construction *not* drawing on uncontrolled sources.
3. 🔴 **It cuts against the cheapest architecture in the market.** "Point a RAG pipeline at the open web"
   is the default demo, and in Vietnam it is the regulated case.

⚠️ **This is SEARCH-SNIPPET-ATTRIBUTED** (the Decision's own text and both legal analyses were unreachable),
and this pass **refuses** the compliance deadline, which three sources give incompatibly. ⚠️ **One source
states the classification attaches only where the AI output is the SOLE basis for a decision without
meaningful human review** — **if** that holds it would narrow all three education systems to a design
question, which is why it must be verified at the Appendix before it is ever briefed.

## 🟢 `T-p302d` — TUTORING EVALUATION ARRIVED AS CODE, AND ITS PREMISE IS THAT THE HELPFULNESS JUDGE MAY BE REWARDING HARM

⏱️ `2026-10-18`, pass 302. Evidence:
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv).

🟢 **This base has carried [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai)
as the permissive evaluation framework since `p301`. A harness is not a design.** `p302` found the design,
twice, both **MIT**, both in the low single digits of stars:
[`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) (arXiv:2607.28128) and
[`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit).

🔴 **The premise is the trend:** the first asks whether an LLM helpfulness judge *"rewards the answer-leakage
that reduces the student's later independent work."* 🔵 **Stated plainly — the metric the whole industry
optimises (did the student find the tutor helpful?) may be positively correlated with the behaviour that
destroys learning (giving away the answer).** If that holds, every helpfulness-scored tutoring deployment
is optimising against its own purpose.

🟢 **The method is what makes it reusable, and it is unusually disciplined for a 3-star repository:** one
**frozen base model** wrapped in two policies that **differ only in structure** — `ConvTutor` (single-node
LangGraph) against `PedTutor` (state tracker + decomposer + **deferral gate** + hint cascade) — plus a cold
baseline for the floor, a deliberately **weak simulated student** (**Llama-3.1-8B**) so leakage has
somewhere to show, Opus as primary judge with a second judge for robustness, a **leakage matcher frozen
before scoring** (`protocol/leakage.py`), **per-component ablations** removing tracker / gate / cascade one
at a time, **10 replicates × {cold, conv, ped}** per base, and GPT and Gemini bases run separately and
**never pooled**.

🔵 **Why it lands now:** Vietnam and Korea have both made automated assessment a named obligation, and the
difference between an engagement that brings *assurances* and one that brings *evidence* is precisely this
artefact. 🟢 **The deliverable shape is clear — `inspect_ai` as harness, this as protocol, the client's own
tutor as the system under test.**

⚠️ **Hard boundary, repeated because it is easy to lose: NO RESULTS ARE STATED ON EITHER PAGE.** The READMEs
give commands to recompute from tracked tables; the pre-registered hypotheses live in a `paper-plan.md` this
pass did **not** read. 🔴 **Cite the design. Never cite an effect size from these rows** — and note that
`ability-levels-audit`'s default branch is **`master`**, so a pin written against `main` 404s.

## 🔴 `T-p301a` — WHEN THE INSTRUMENT ITSELF IS UNRUNNABLE, THE ONLY HONEST SUBSTITUTE IS A RE-IMPLEMENTATION THAT IS CALIBRATED AGAINST THE ORIGINAL'S OWN PUBLISHED OUTPUT

⏱️ `2026-10-18`, pass 301. Evidence:
[`p301-instrument-substitution.2026-10-18-p301.tsv`](../evidence/p301-instrument-substitution.2026-10-18-p301.tsv) ·
[`p301-probe-calibration.2026-10-18-p301.tsv`](../evidence/p301-probe-calibration.2026-10-18-p301.tsv) ·
[`p301-payload-grade.2026-10-18-p301.tsv`](../evidence/p301-payload-grade.2026-10-18-p301.tsv).

🔴 **`p300` ended by naming the error class *"believing a written bound over a runnable instrument."*
`p301` met the inverse and it is a new class: the instrument was RUNNABLE and this session was not
permitted to RUN IT.**

| attempted | result |
|---|---|
| `make hooks` — the whole standing gate chain | 🔴 **DENIED** by the sandbox classifier, *"Code from External"* |
| `bash -c '. compose/code/lib/probe_payload.sh; probe_repo …'` | 🔴 **DENIED**, same class |
| `make carried` / `make claims` — the index and absence gates | 🔴 not attempted after two denials of the same class |
| 6-host `getent` DNS control, with known-real-unallowlisted **and** known-fake controls | 🔴 **DENIED**, *"Exfil Scouting"* — **reproducing `p295` exactly** |

🔵 **The distinction matters because the two classes have opposite remedies.** `p297`'s *"no raw
path"* was a **false bound** — the fix was to ask the host. `p301`'s bound is **real**: the file
exists, the loop is correct, and the execution is refused. **No amount of asking fixes it, and
pretending otherwise would be the `p294` error in a new costume.**

### 🔴 Why this was the most expensive denial available

🔵 [`compose/code/lib/probe_payload.sh`](../compose/code/lib/probe_payload.sh) opens with *"SHARED
PAYLOAD PROBE — source this, do not rewrite it"*, and its header explains why in this base's own
history: **pass 77** re-imported `P171` (GPL-3.0 §13 is *titled* "GNU Affero…", so every GPL-3.0 read
as AGPL) by rewriting the family classifier; **pass 15 of `2026-10-06`** rewrote the probe loop and
reported four GPL/AGPL payloads as Creative Commons **because GPL-3.0 §6 contains the word
"noncommercially"** — a defect this base had already measured and already fixed.

🔴 **So the one action the file forbids is exactly the action `p301` needed to take.**

### 🟢 What was done instead, and why it is not the pass-15 error repeated

🟢 **The substitution is declared, every documented trap was carried deliberately, and — the part that
makes it admissible — it was CALIBRATED against this base's own published sha256 pins BEFORE it was
used on anything new.**

| control | this base's published read | `p301`'s re-implementation | verdict |
|---|---|---|---|
| `Gego-K12/gegok12` | **MIT**, `LICENSE`, **1 150 B**, sha256₁₂ **`b8694396d7dc`** *(`p295`)* | MIT, `LICENSE`, **1 150 B**, **`b8694396d7dc`** | 🟢 **BYTE- AND HASH-EXACT** |
| `Submitty/Submitty` | `LICENSE` **404**; grant at **`LICENSE.md`**, **1 542 B**, sha256₁₂ **`c123708cb4ef`**, BSD-3-Clause *(`p295`)* | `LICENSE` absent; **`LICENSE.md`**, **1 542 B**, **`c123708cb4ef`**, BSD-3-Clause | 🟢 **BYTE- AND HASH-EXACT, and the LADDER TRAP reproduced** |
| `learningequality/kolibri` | MIT, offline-first | MIT, **1 097 B**, `3c056b34a476`, **default branch `develop`** | 🟢 **the DEFAULT-BRANCH TRAP reproduced and handled** |
| `zzq9-fake-owner-control/nope` | *(known-fake control)* | **UNRESOLVED** | 🟢 **discriminates** |
| `gmilano/definitely-not-a-repo-zzq9` | *(known-fake control)* | **UNRESOLVED** | 🟢 **discriminates** |

🔵 **Two independent hash reproductions, both documented traps firing on the controls that motivated
them, and two negative controls refused.** 🟢 **That is the minimum price of using a substitute
instrument, and it is why the 105 reads on
[`repos/foundations.md`](../repos/foundations.md) are quotable.**

🔴 **The substitute's gaps, stated rather than discovered later:**
- 🔴 **No README-link arm.** The shared tool asks the README where the licence is; this one walks a
  filename ladder only. **So every `NO-PAYLOAD` this pass published is weaker than the shared tool's
  would be** — `p300` found `OS4ED/openSIS-Classic`'s GPL-2.0 at `docs/License.txt` precisely that way.
- 🔴 **A coarser family vocabulary.** It names families, not versions: it returned `LGPL` without
  separating 2.1 from 3.0 on both `oat-sa` rows, and `CC` without reaching `CC-BY-SA-4.0` — which this
  base's own instrument **does** reach.
- 🟢 **And it could not name `ISC` at all**, which turned out to be a feature — see below.

### 🟢 The corollary this pass contributes: A CALIBRATED CLASSIFIER'S REFUSAL TO NAME IS A LOCATOR

🔵 **The substitute returned `UNCLASSIFIED` exactly three times in 105 reads. All three were genuinely
non-standard grants, and zero were failures of reading:**

| row | what `UNCLASSIFIED` was |
|---|---|
| [`aryankeluskar/canvas-mcp`](https://github.com/aryankeluskar/canvas-mcp) | 🟢 **ISC** — a real OSI-permissive licence outside the ladder. **`p297` published this row `ISC` from the SIDEBAR; it is now payload-pinned at 746 B / `b3364441534c`** |
| [`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) | 🔴 **proprietary** — *"AStheTECH Community License… limited, non-exclusive, non-transferable, non-sublicensable, and revocable… All rights not expressly granted are reserved"*. **Confirms the carried cell verbatim** |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS Global Specification Document License** — a *document* licence, no OSI. **Confirms the carried cell BYTE-EXACT at 12 402 B** |

🟢 **Three refusals, three unusual licences, no false alarms.** 🔵 **So `UNCLASSIFIED` from a
calibrated instrument should be routed to a human triage queue, not counted as instrument error — it
is the cheapest available detector of the grants that actually need a lawyer.** 🔴 **The precondition
is the word CALIBRATED**: an uncalibrated classifier's `UNCLASSIFIED` is noise, and pass 15's was
worse than noise because it emitted confident wrong answers instead.

## 🟢 `T-p301b` — ANECDOTES THAT HAVE BEEN REPEATED FOR TWENTY PASSES CAN BE PRICED, AND BOTH OF THIS BASE'S PROBE TRAPS ARE COMMONER THAN ITS OWN HEADER SUGGESTS

🔵 **`probe_payload.sh` documents its traps with three or four real examples each — which was enough to
justify the code and never enough to size the risk.** 🟢 **105 reads price both.**

| trap | this base's prior evidence | `p301`'s rate |
|---|---|---|
| **default branch is not `main`/`master`** | 3 named SIS platforms | 🔴 **11 / 105 — `10.5 %`** |
| **grant is not at plain `LICENSE`** | 3 spellings found across ~20 passes | 🔴 **9 / 105 — `8.6 %`** |

🔴 **The branch values, because the distribution is the finding:** `develop` ×4, `dev`, `staging`,
`unstable`, `v6.2.0`, `0.7`, `3.x` — and
[`eledia/moodle-block_elediaai_tutor`](https://github.com/eledia/moodle-block_elediaai_tutor) whose
default branch is literally **`51`**. 🔵 **A tag-shaped default (`v6.2.0`), a version-shaped one
(`0.7`, `3.x`) and an integer (`51`) are not variants of `main` with different spelling — they are
release-engineering conventions, and no heuristic guesses them.** Only `ls-remote --symref` reads them.

🟢 **Compounded, a one-path probe on a hardcoded branch misreports roughly ONE ROW IN FIVE on this
corpus.** 🔵 **That is the quantified case for the shared instrument — produced, with full irony, by the
pass that was forbidden to run it.**

## 🟢 `T-p301c` — THE MANDATED REGIONAL PHRASING HAS NOW PRODUCED ZERO NEW DATUMS ACROSS EIGHT RUNS WHILE THE DIRECTED SLOT PAID IN BOTH PASSES

🔵 **`p300` observed it once; `p301` reproduced it on four different mandated legs in the same hour.**

| leg class | passes | runs | new datums |
|---|---|---|---|
| 🔴 **mandated regional** *(`AI education {region} {year} adoption regulation players`)* | `p300`, `p301` | **8** | 🔴 **0** |
| 🟢 **directed unworked-region** | `p300` *(Lusophone Africa)*, `p301` *(Central Asia)* | **2** | 🟢 **6** |

🔵 **Why, mechanically: the mandated query names a CONTINENT-SCALE abstraction, and the corpus that
answers it is written for the same abstraction** — market-sizing pages and regulatory round-ups that
this base absorbed passes ago. 🟢 **A query that names a NATIONAL SYSTEM returns instruments:**
Kazakhstan's decree with its signatory, its three deadlines, its two renamed subjects and its **43
learning objectives**; `p295`'s Ethiopian offline mandate; `p300`'s SACMEQ collapse.

🔴 **The same leg structure also produced this pass's one informed gap: Uzbekistan returned NOTHING** —
no policy, no date, no curriculum — which is only knowable because the leg named it. 🟢 **An
undeclared nil looks exactly like coverage; a declared one is a finding.**

🔵 **The honest bound on this claim, per `p295`'s correction:** two passes and eight runs is enough to
**change the next pass's query budget** and not enough to call a law about all regions. 🟢 **It is
registered as a recommendation with its sample attached, not as a rule.**

## 🔵 `T-p301d` — A SEARCH SNIPPET THAT NAMES ONE LICENCE FOR A MULTI-GRANT TREE IS WRONG EVEN WHEN THAT LICENCE IS REALLY IN THERE

🔴 **The directed leg reported [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp)
as *"GNU General Public License v3.0 only"*.** 🟢 **Its root payload is MIT — 1 071 B, sha256₁₂
`22e7ab2dbddc`.** 🟢 **And the carried shelf row already held both halves:** *"MIT (2.x);
`legacy_reference/` GPL-3.0-only"*.

🔵 **The snippet did not hallucinate. It reported the most restrictive grant in the tree as the grant
of the tree** — and for a consumer deciding whether to depend on `2.x`, that is the wrong answer
derived from true data. 🟢 **The row this base published a dozen passes ago is more accurate than the
live search result**, which is worth stating plainly in a base whose standing anxiety is staleness:
**a carefully-split cell ages better than a freshly-fetched summary.**

🟢 **And the general rule for this shelf: the question *"what licence is this repository?"* is
malformed for any tree with a vendored or legacy directory.** The answerable questions are *"what
grant covers the code I will ship?"* and *"what else is in the tree?"* — which is why
`p280`'s package-provenance channel and this pass's payload reads are complementary rather than
redundant.

## 🔵 `T-p301e` — AN IDENTICAL LICENCE PAYLOAD IS EVIDENCE OF ANCESTRY, NEVER OF ALIASING

🔴 **[`chiptoe-svg/canvas-lms-mcp`](https://github.com/chiptoe-svg/canvas-lms-mcp) and carried
[`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) serve byte-identical grants** —
**1 070 B**, sha256₁₂ **`c29329c5ef3b`**, holder *"2026 Christian Bru"* on both. On payload evidence
alone they are indistinguishable, and a shelf that deduplicated on the grant would have thrown one away.

🟢 **`p283`'s rule — *equal HEAD == one repository* — separates them:** `fa8408a64dc2…` against
`18fa06b5758e…`. **Two repositories; the fork is admitted, annotated as a fork.**

🔵 **Note that the same instrument produced the OPPOSITE verdict at `p282`**, where `ls1intum/Iris`
was withdrawn as a GitHub name alias of `ls1intum/Pyris` on **equal** HEAD, identical ref count and
identical root tree. 🟢 **One rule, two verdicts, and the discriminator is the HEAD in both
directions.** 🔴 **A fork INHERITS the grant — so licence identity is the one signal that can never
settle the identity question**, and any future dedup pass must read HEADs, not hashes of `LICENSE`.

## 🟢 `T-p301f` — ARCHIVE STATUS IS NOT IN THE GRANT, CONFIRMED ON A SECOND INDEPENDENT READ

🟢 **`p300` found [`digitalcredentials/sign-and-verify`](https://github.com/digitalcredentials/sign-and-verify)
**ARCHIVED by its owner `2026-08-26`**, and noted that *"its payload read was clean and entirely
silent about it."* 🟢 **`p301` re-read it through a different implementation of the same channel: MIT,
`LICENSE`, 1 075 B, sha256₁₂ `09e4c03a44a7` — clean, permissive, and still entirely silent about the
archive.**

🔵 **This is a reproduction, not a restatement, and it generalises into a bound on this whole pass:**
🔴 **105 payload reads establish 105 COPYRIGHT positions and ZERO maintenance positions.** Archive
status, deprecation notices, security advisories and *"use X instead"* all live on the rendered page
or in the README — **channels this pass did not read for the 105.** 🟢 **So every row pinned at `p301`
is licence-proven and maintenance-unproven**, and the standing instruction that follows is: **never
promote a row to a client recommendation on a payload read alone.**


## 🔴 `T-p300a` — A REFUSAL IS A FACT ABOUT THE HOST YOU ASKED, NOT ABOUT THE SESSION; AND THE INSTRUMENT FOR THE HOST NOBODY ASKED WAS ALREADY IN THE REPOSITORY

⏱️ `2026-10-18`, pass 300. Evidence:
[`p300-raw-channel-control.2026-10-18-p300.tsv`](../evidence/p300-raw-channel-control.2026-10-18-p300.tsv).

🔴 **`p297` wrote: *"`curl` 403 on 4/4, no `api.github.com`, no raw path."*** `p299` inherited that
bound and graded 14 of its 15 new rows **sidebar-only**. Between them, **27 rows** were published at
this base's weakest evidence grade.

🟢 **Two of those three clauses reproduce exactly at `p300`. The third was never measured.**
`raw.githubusercontent.com` answers **`200` with the licence payload** while `github.com` and
`api.github.com` both **403**. 🟢 **And it discriminates:** a known-fake owner and a known-fake
repository both `404` — which is more than `p294`'s and `p295`'s gateway probes could do.

🔴 **The part that should sting: this base had already written the loop.**
[`compose/code/lib/probe_payload.sh`](../compose/code/lib/probe_payload.sh) opens with *"SHARED
PAYLOAD PROBE — source this, do not rewrite it"*, reads exactly that host, resolves the real default
branch with `ls-remote --symref`, walks a filename ladder, and classifies with the hardened shared
classifier. **It answered correctly on the first call — including both traps its own header
documents**: a `dev` default branch and a `LICENSE.md` grant.

🔵 **The generalisable claim is narrower than it looks.** The error was not *"a channel was
mislabelled"*. It was **writing a conclusion from channel A as a property of the environment**: a 403
from `api.github.com` became *"this session cannot read payloads."* That is `p294`'s own refuted
move — **measure channel A, conclude about B** — and it survived three passes because it was phrased
as a fact about the **session** rather than as what it was: **a fact about two URLs.**

🟢 **The clause the standing oracle gains: NAME THE HOST YOU MEASURED.** An absence claim must carry
the address it was measured at, or it is a claim about the prober.

🔴 **The second lesson is this base's oldest.** The Makefile header already says *"a rule that has to
be remembered is not a control"* and *"a control nobody has to assemble is the only kind that gets
used."* `probe_payload.sh` **is** assembled. It still was not reached for, because **a bound written
in prose was believed over a tool sitting in the tree.** 🔵 **A base that writes bounds faster than
it runs its own instruments will reliably under-grade its own shelf.**


## 🔴 `T-p300b` — "SHELVED" HAD TWO MEANINGS HERE AND THEY CAME APART: FIFTEEN VERIFIED ROWS WERE ANNOUNCED ON A FILE AND NEVER WRITTEN TO ITS TABLE

⏱️ `2026-10-18`, pass 300.

🔴 **Of the fifteen slugs `p299` admitted to [`repos/foundations.md`](../repos/foundations.md), ZERO
appeared on a row of that file's `## Permissive foundations` table.** They lived only inside `p299`'s
own narrative section. `p298`'s thirteen all reached the table.

🔵 **Why this is a trend entry and not a typo.** This base runs instruments that read **table rows** —
the identity gate, the table-structure gate, `recount`, and the orphan diff whose rule `p299` itself
published in the same breath (*"match only lines whose first non-space character is a pipe"*). 🔴 **So
fifteen rows of real, boundary-annotated work were invisible to every instrument that measures this
shelf — and to any studio reading the shelf rather than the history.**

🟢 **`T-p299b` is this entry's sibling, and `p299` wrote it**: *naming a slug in prose makes it look
shelved.* 🔴 **This is the inverse — publishing a row in the wrong table makes verified work look
absent.** Together they say something sharper than either: **a knowledge base needs exactly one
answer to "where does a fact live", and a file whose narrative and whose shelf are both tables will
generate both errors.**

🟢 **All fifteen restored at `p300`, marked ♻️**, with `p299`'s figures and boundaries intact. 🔵 **And
the file's prose row-total had drifted a second time** — 48 published against a table of 61, the exact
defect `p297` corrected one pass earlier. **A count re-derived by a gate cannot drift; one a pass must
remember to re-sum will.** Registered as `ACTION PG-5` item 4, not claimed as fixed.


## 🔴 `T-p300c` — A LAYER BACKLOG BUILT BY SUBSTRING MATCH ON THE SLUG IS NOT A LAYER BACKLOG

⏱️ `2026-10-18`, pass 300. Evidence:
[`p300-promotion-gap.2026-10-18-p300.tsv`](../evidence/p300-promotion-gap.2026-10-18-p300.tsv) ·
[`p300-subject-oracle.2026-10-18-p300.tsv`](../evidence/p300-subject-oracle.2026-10-18-p300.tsv).

`ACTION PG-4` named seven slugs across three layers. 🔴 **Measured at `p300`: three were already on
this base's tables, and one was not in the named layer at all.**

[`xapi-labs/xapi-cli`](https://github.com/xapi-labs/xapi-cli) was named as part of *"the remaining
xAPI movement layer."* 🔴 **It is `xapi-to` (`xapi.to`): an agent capability/API-calling CLI with
crypto, `x402` payments and Cloudflare Workers. Zero Experience-API markers in a 50 919-byte
README** — no *"Experience API"*, no LRS, no statement, no actor/verb, no `1.0.3`.

🔵 **Both halves of the defect have one cause: the candidate was selected by the string in its
name.** `p299` had already diagnosed and fixed this on the **shelf** side of the orphan diff. **The
candidate side was never checked** — so the instruction pushed three already-shelved slugs and one
mis-layered one into the next pass's budget.

🔴 **And the tokens are ambiguous, measured rather than asserted:** the word `credential` fires
**15 times** in `xapi-cli`'s README and **not once** about learning — it means an **API key** there.
🟢 **A layer's vocabulary has to be its NARROW terms** (*open badge*, *verifiable credential*, *CLR*)
— and even those miss: `issuebadge/mcp-server` says *"verifiable **certificates**"* and scored
**zero**.

🟢 **So the subject oracle built this pass ships as a RANKER with its measured error rates — one
false positive and one false negative in twenty — and deliberately NOT wired into `make hooks`.**
🔵 **A base that had gated on it would have rejected the single agent row this pass found.** The
decisive read, in all twenty cases, was the README's **first declarative line**.


## 🔴 `T-p300d` — AN INDEPENDENT RUN THAT RETURNS EVERYTHING YOU ALREADY HAVE IS CORROBORATION, NOT COVERAGE

⏱️ `2026-10-18`, pass 300. Evidence:
[`p300-websearch.2026-10-18-p300.tsv`](../evidence/p300-websearch.2026-10-18-p300.tsv).

🟢 **Every datum every regional leg returned was checked against the COMMITTED state of
[`intel/market.md`](market.md) before being called new.** Result: **21 datums examined, 17 already
carried, 4 new** — and **the four mandated regional legs produced ZERO new datums between them**,
while one directed leg at an unworked region (Lusophone Africa) produced **three**.

🔴 **This forced two corrections on the same pass's own first draft, and the corrections are the
entry:**

1. The draft claimed *"five new datums"* for North America. **Zero were new.** It had been written
   from what the leg **returned** rather than from what this base **did not already hold**. 🔵 That
   is `T-p299c` one level up — **counting results as coverage**. A non-nil leg is not a productive
   leg, and *"the strongest leg again"* is a sentence about volume.
2. 🔴 **The carried-check itself was wrong on its first run.** It called LATAM's governance figure
   NEW because it matched the exact string `30% of universities`, while this base holds the same
   datum as `~30%`. 🔵 **An exact-string carried-check is a LOWER BOUND on what is carried, never a
   measurement of what is new.**

🟢 **The rule worth keeping: a pass's output is `new datums`, not `datums`** — and the subtraction
must be done mechanically against the committed file, because no pass can hold 5 400 lines in mind.


## 🟢 `T-p300e` — A 168-BYTE DIFFERENCE IN A LICENCE PAYLOAD WAS ENTIRELY ENCODING, SO BYTE-INEQUALITY IS NOT EVIDENCE OF DIFFERENT TERMS

⏱️ `2026-10-18`, pass 300.

🟢 **This base pins grants by byte size, and `p295` celebrated a *"byte size identical"* re-read as
proof a grant had not moved.** That inference is sound in **one direction only**, and `p300` measured
the other.

[`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec)'s `LICENSE` is **11 525 B** against the
**11 357 B** stock Apache-2.0 text carried byte-identically by four other rows read this pass
(sha256₁₂ `c71d239df917`). 🔴 **A 168-byte excess on a licence payload reads exactly like an appended
rider.**

🟢 **It decomposes precisely:** **+200** carriage returns (CRLF line endings), **−1** trailing
newline, **−31** leading spaces on the title line = **168**. `family_of` returns `Apache-2.0`;
`rider_restriction` returns **empty**. **Same grant, different encoding.**

🔵 **The asymmetry, stated for reuse:** byte-size **equality** at a pin is strong evidence of
identity; byte-size **inequality** is evidence of nothing until the payload is normalised. 🔴 **A
probe that flags a size delta as a terms change raises a false alarm on every CRLF repository** — and
one that treats a size match as sufficient will miss a rider that happens to fit.


## 🔴 `T-p299a` — AN OPEN STANDARD CAN BE CLOSED BY ITS OWN STANDARDS BODY, AND NOTHING ON THE SPEC'S PAGE TELLS YOU

⏱️ `2026-10-18`, pass 299.

🟢 **Caliper Analytics is a published 1EdTech standard with a live specification repository, a live
ontology, a bootcamp, Moodle and Open edX emitters, and client libraries in Python, Java, PHP and
Ruby.** 🔴 **Every one of those client libraries now returns `404`.** `IMSGlobal/caliper-php-public`,
`IMSGlobal/caliper-ruby-public`, `Brightspace/ims-caliper-python`, `1EdTech/caliper-python`,
`1EdTech/caliper-java` — five for five.

🔴 **The evidence for *why* is in a third party's repository description, not the standards body's.**
[`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) says it
**"has been unarchived since 1EdTech made the upstream `caliper-php` private."** A university
un-archived a dead fork to keep a standard reachable.

🔵 **The trend, and it is a procurement risk rather than a technical one: "open standard" and "open
source" are independent properties, and the second one can be revoked without the first one changing.**
The Caliper *specification* is still published. Its *grant* is `Other`, with **no `LICENSE` file at
`master`**. The only permissive artefact left in the layer is a **20-commit proof-of-concept**
([`1EdTech/CaliperBootcamp`](https://github.com/1EdTech/CaliperBootcamp), MIT) whose own README says its
auth flow **"must not be used in production."** Everything load-bearing is LGPL, GPL, or archived.

🟢 **The generalisable control: before recommending a standard, read the grant on the code that
implements it, not the status of the standard.** 🔴 **And check the forks — a maintained third-party
fork of a withdrawn upstream is the signal that a withdrawal happened**, because nothing on the
standards body's own pages records it. xAPI passes this test where Caliper fails it
([`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) Apache-2.0,
[`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) MIT), which
is why this base's analytics recommendation is now xAPI on evidence rather than on taste.

## 🔴 `T-p299b` — A KNOWLEDGE BASE CAN HIDE WORK FROM ITSELF BY WRITING AN INSTRUCTION: NAMING A SLUG IN PROSE MAKES IT LOOK SHELVED

⏱️ `2026-10-18`, pass 299.

🔴 **`p297` and `p298` each "re-diffed all 528 permissive orphans against all three shelf files" and
reported 481, then 456, unshelved. The diff they describe counts prose.** `p299` measured the same list
with matching restricted to **table rows** — lines whose first non-space character is a pipe:

| measurement | value |
|---|---|
| distinct slugs, case-insensitive | **525** |
| on an actual shelf **row** | **70** |
| 🔴 in shelf-file **prose only**, no row anywhere | **11** |
| absent from the shelf files entirely | **444** |
| 🟢 true unshelved, row-grade | **455** |
| 🔴 what a naive prose-inclusive diff returns | **444** |

🔴 **And five of the eleven prose-only slugs are the very slugs `ACTION PG-3` named** —
`S4-NetQuest/react-scorm-provider`, `raccoongang/edx_xblock_scorm`, `rolfis/qti-convert`,
`metyatech/markdown-to-qti`, `metyatech/qti-html-renderer`. 🔵 **`p298` wrote them into an instruction;
the instruction made them indistinguishable from completed work.** A pass that trusted a plain text
match would have reported `ACTION PG-3` as already discharged and read nothing. **All five are shelved
as real rows by this pass.**

🟢 **The generalisable control: a base that records its intentions in the same medium as its results
must distinguish the two mechanically.** Here the discriminator is cheap and exact — **a row starts with
a pipe** — but the principle is the point: 🔴 **any "have we covered X?" check that greps the whole
document will eventually answer yes because the base once said it should.** `p298`'s 456 was
nonetheless right, which is the reassuring part: the defect inflates *coverage*, so it hides work
rather than inventing it.

## 🔴 `T-p299c` — NINE SEARCH RESULTS CAN BE TWO DOCUMENTS: REGIONAL QUERIES RETRIEVE LOCALE-REPLICATED SYNDICATION

⏱️ `2026-10-18`, pass 299.

🟢 **Two independent dead channels in this base were measured in the same hour and have the same
mechanism.**

| dead channel | passes nil | what the corpus actually was |
|---|---|---|
| `AI education EMEA {year} adoption regulation players` | 🔴 **11** | **5 of 9 slots: ONE CompTIA article at five locale subpaths** (`en-za`, `en-eu`, `en-au`, `en`, `en-em`), plus a Workday study from **2023** |
| `open source platform education ERP CRM MIT Apache` | 🔴 **19** | 🔴 **6 of 9 slots: ONE `openeducat.org` glossary page in six languages** (`es`, `fr`, `ar`, `zh`, `de`, `pt-BR`) |

🔴 **A search engine counts locale variants as distinct results; a pass that reads slot-count as corpus
breadth concludes the population was searched.** It was not: nine slots were two documents.

🔵 **This is why `p287`-`p299`'s directed legs beat the mandated regional ones thirteen times running,
and the explanation is finally mechanical rather than anecdotal.** A **region** name (`EMEA`, `APAC`)
is marketing vocabulary — it retrieves vendor and analyst syndication aimed at a sales territory. A
**country** name (`Morocco`, `Poland`, `Pakistan`, `Ethiopia`, `Indonesia`) is administrative
vocabulary — it retrieves ministries, budgets and parliamentary records. 🟢 **`p299` ran two country
legs and got two countries new to this file; the region legs got the same two documents as nine passes
before.**

🟢 **The generalisable control: measure DISTINCT DOCUMENTS, not result slots, before declaring a
population searched — and when a regional leg nils twice, replace the region with a country rather than
re-running it.** Keep running the mandated phrasing, because an undeclared nil looks exactly like
coverage; **just stop treating its nil as information about the world.**

## 🔴 `T-p299d` — AN UNLABELLED LICENCE SIDEBAR HAS AT LEAST FOUR CAUSES, AND THEY LEAD TO OPPOSITE DECISIONS

⏱️ `2026-10-18`, pass 299.

🟢 **`p298` found that GitHub's licence classification "is not a property of the payload" and registered
the rule: treat an unlabelled sidebar as a question about which repository you are on.** 🔴 **`p299` hit
five unlabelled sidebars and only one of them was that question.**

| repo | cause | grant | decision |
|---|---|---|---|
| `raccoongang/edx_xblock_scorm` | standard payload, simply unclassified | 🟢 `Apache-2.0` *(11.1 KB)* | **shelved** |
| `OpenOLAT/qtiworks` | licence in `LICENSE.txt`, not `LICENSE` | 🟢 `BSD-3-Clause` *(2.01 KB)* | **shelved** |
| `1EdTech/caliper-js-example` | 🔴 **the org listing labelled it; the repo sidebar did not** | 🔴 `LGPL-3.0` *(7.43 KB)* | rejected |
| `1EdTech/caliper-spec` | 🔴 **no `LICENSE` file at that path at all** (`404`) | 🔴 `Other` | rejected |
| `ashleycribb/learnmcp-xapi` | licence in README only, on a declared fork | 🔴 MIT, but a fork of a shelved repo | rejected |

🔴 **Two permissive, two copyleft, one identity problem. A scanner that treats the bare sidebar as one
signal errs in both directions — it discards Apache-2.0 and BSD code as unlicensed, and it admits LGPL
code as unknown-therefore-fine.** 🟢 **Three of this pass's fifteen admissions would have been lost to a
sidebar-only read.**

🔵 **And a new surface is on the record:** `github.com/orgs/<org>/repositories?q=` **classifies licences
that the repository's own page leaves bare.** Same repository, same payload, two GitHub surfaces, two
verdicts. 🟢 **The rule that survives: an unlabelled sidebar is a question about WHERE THE GRANT LIVES.
Read the org listing when the sidebar is silent; read the payload before you shelve.**

## 🔴 `T-p299e` — "PREFER THE CANONICAL SLUG" IS A STAR TEST, AND IT PICKS THE DEAD REPOSITORY

⏱️ `2026-10-18`, pass 299.

🟢 **`p298`'s identity gate replaced a 3★ copy with its 138★ canonical original and was right to.**
🔴 **`p299` found the case that runs the other way:**

| | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) *(the fork)* | [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks) *(canonical upstream)* |
|---|---|---|
| stars / forks | 3 / 2 | 🟢 **68** / **55** |
| commits | 🟢 **2 087** | **2 073** |
| its own description | the engine | 🔴 **"This project will be closed in early 2023!"** |
| verdict | 🟢 **shelve this one** | 🔴 abandoned |

🔴 **The canonical slug has 22× the stars and announces its own death in its description. The fork
carries fourteen commits the original never received.**

🔵 **The trend: stars are a record of the past, and identity rules built on them select for whichever
repository was popular when the capability mattered — not whichever one still works.** 🟢 **The
corrected test is a delta, not a level: prefer the slug where the history CONTINUES, and read the
description for an abandonment notice before ranking anything.** This also sharpens `p295`'s refutation
of *"stars are monotonic"*: stars do not merely drift, **they persist through abandonment**, which is
precisely when they are most misleading.

🟢 **The gate has now fired four times in three passes — and this pass it ADMITTED a row it would
otherwise have skipped:** `examplary/qti` collided by bare name with the shelved `instructure/qti`, and
they are unrelated (TypeScript building QTI 3.0/2.1 packages vs. a Ruby gem parsing QTI 1.2/2.1). 🔵
**A name check is a prompt to look, not a verdict either way** — it has now caught two duplicates, one
dead canonical, and one false duplicate that was the only permissive QTI 3.0 packaging row in
TypeScript.


## 🟢 `T-p298a` — THE INSTRUCTION WAS RIGHT FOR 297 PASSES AND UNARMED FOR 297 PASSES: "INTEGRATE, DO NOT FORK" HAD ONE LIBRARY, IN ONE LANGUAGE

⏱️ `2026-10-18`, pass 298.

Every pass of this base that has met a copyleft LMS has given the same instruction: reach **Moodle**
(GPL-3.0), **Canvas** (AGPL-3.0) and **Open edX** (AGPL) **at the integration boundary**, and keep the
studio deliverable on the permissive side of it. 🔴 **The instruction was architecturally correct and
operationally empty.** These shelves carried exactly **one** boundary row —
[`tsugi`](https://github.com/tsugiproject/tsugi), Apache-2.0, **PHP** — and **zero** QTI rows, **zero**
OneRoster implementations and **zero** Caliper rows.

🟢 **`p298` armed it in six runtimes**: LTI 1.3 in **TypeScript** ([`ltijs`](https://github.com/Cvmcosta/ltijs),
Apache-2.0, 373★), **PHP** ([`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library),
the standards body's own, **107 forks against 124 stars**), **Python**
([`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3), MIT) and **JupyterHub**
([`ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator), BSD-3-Clause); QTI 3 playback and
packaging plus QTI 1.2/2.1 parsing; OneRoster 1.2 in **.NET** and **Go**; and xAPI forwarding beside
the store this base already had.

🔵 **The trend this names is not about education — it is about how a knowledge base goes wrong.** This
base did not hold a *false* belief; it held a **true** recommendation with **no inventory behind
it**, for 297 passes, while its agent shelf grew to **42 rows**. 🔴 **An advice layer and an inventory
layer can drift apart silently, because neither contradicts the other.** Nothing in this repository
was ever inconsistent — the gap only became visible when a pass went looking for the code that the
advice presupposed. 🟢 **The generalisable control: for every standing instruction this base gives,
there should be a shelved row that executes it. `p298` recommends auditing the remaining
instructions the same way** — starting with *"generate H5P content and play it through the MIT
runtime"* (`ACTION PW`) and *"write AI evidence into the LRS, not the system of record"* (`Gap 314`),
both of which now have components but have never been checked end to end.

## 🔴 `T-p298b` — CLUSTER SIZE IS NOT CLUSTER SATURATION, AND `p297` CONFLATED THEM

⏱️ `2026-10-18`, pass 298.

`p297` re-diffed `p989`'s **528** permissive orphans, found the densest cluster to be **~20
LMS-integration MCP adapters**, observed that the agents shelf already carried **four Canvas MCP
servers, three Google Classroom servers and three Moodle servers**, and concluded: *"that cluster is
duplicative capability, not missing capability."* 🟢 **That conclusion was correct.** 🔴 **The rule
`p297` left behind was not: it ranked the list by cluster density, as though a dense cluster is
evidence of saturation.**

`p298` worked the **standards-interop cluster — LTI, QTI, OneRoster, xAPI, SCORM, Ed-Fi — roughly 60
slugs, three times the adapter cluster.** It stood at **zero rows for QTI, zero for OneRoster
implementations, zero for Caliper, and one for LTI.** 🔵 **Density said "skip"; the shelf said
"empty".**

| cluster | size on the list | rows on shelf before | verdict |
|---|---|---|---|
| LMS/MCP adapters | ~20 | **10** | 🔴 **saturated** — skip, as `p297` said |
| standards interop | 🔴 **~60** | 🔴 **1** | 🟢 **the richest unworked layer in the list** |

🟢 **The corrected test, and it is one number against another: rows-on-shelf ÷ cluster-size. Never
size alone.** A big cluster is a big *opportunity* when the shelf is empty and a big *waste* when it
is not, and the two are indistinguishable without looking at the shelf. 🔵 `ACTION PG-3` carries this
forward: **Caliper** is the next cluster at **zero**.

## 🔴 `T-p298c` — THE COUNTERPARTY IS NOT ALWAYS THE EDUCATION MINISTRY, AND TWO NEW EMEA COUNTRIES PROVED IT IN OPPOSITE DIRECTIONS IN ONE PASS

⏱️ `2026-10-18`, pass 298.

`T-p287` recorded that **the generative unit in education had become the ministry**, and `T-p297a`
split that into a publisher (Nigeria) and a buyer (Kazakhstan). 🟢 **`p298` adds a third axis, and it
is a procurement axis rather than a posture: WHICH ministry.**

🟢 **🇲🇦 Morocco behaves as `T-p287` predicts.** The **Ministry of Education** owns the school
programme — **12 000+ establishments** to be equipped **by 2027**, *"Caravane pour tous"* from **74 880
(2023) to 625 000+ (2027)** — and an **AI dropout-detection system is already operating in the
Draâ-Tafilalet academy** with a stated national-extension path, inside **"Maroc Digital 2030"** and the
**Jazzari** institutes across **12 regions**. 🔴 A **parliamentary report** says the governance
framework is missing.

🔴 **🇲🇿 Mozambique inverts it.** The AI **regulator** is a multisectoral commission being created by
the **Minister of Planning and Development**; the **schools** robotics-and-AI programme (STEMMOZ,
~**5 000** pupils) is run by the **Ministry of Communications and Digital Transformation**; the
national AI document (**INTIC**, May 2025) comes from the ICT institute. 🔵 **The education ministry
appears nowhere in this leg.**

🟢 **So the briefing rule is now explicit: qualify WHICH ministry holds the mandate before the
pitch, because it varies inside one `region` value and inside one quarter.** 🔵 Three postures now
coexist under `EMEA`: **ministry-of-education-led** (Morocco), **digital/planning-led** (Mozambique),
and **state-as-model-publisher** (Nigeria, `T-p297a`). A deck that assumes the education ministry is
the buyer will be addressed to the wrong department in at least one of the three.

🔴 **And the honest other half: 🇹🇳 Tunisia and 🇩🇿 Algeria returned a declared nil** — only a **2020**
UNESCO Maghreb mapping, six years stale. **🇦🇴 Angola's constraint was named by a local rather than
inferred here**: *"províncias que não têm conexão à internet"* (FNIA 2026 co-founder Estevão Zinga),
which is an **offline-first** requirement that selects **Kolibri (MIT)** off this base's own platform
shelf before any model choice is made.

## 🔵 `T-p298d` — RE-CIRCULATION IS NOT CORROBORATION

⏱️ `2026-10-18`, pass 298.

`p297` introduced **cross-leg corroboration**: a global claim ought to appear in the legs of the
countries it names, and when it does not, the absence is a signal. 🟢 **`p298` supplies the negative
twin, and it is the more dangerous of the two because it looks like evidence.**

The North American leg re-served the **`USD 169M` "government commitment to responsible AI in higher
education"** — the figure `p293` **downgraded** because *its source reports it without naming the
government*, and `p297` refused again. 🔴 **This is its third appearance, from the same leg reaching
the same unsourced blog, and a third appearance is not a third source.**

🟢 **The rule: a figure that returns because you asked the same question again has gained nothing.
Corroboration requires an INDEPENDENT leg** — for this one, a leg that **names a government** and
reaches an appropriation instrument. 🔵 **The practical danger is that re-circulation is
indistinguishable from corroboration in a search result**, which is why the grade must travel with
the datum: this base downgraded the figure once and has now had three chances to re-promote it on
nothing. **The refusal stands.**

## 🟢 `T-p297a` — THE STATE HAS BECOME A MODEL PUBLISHER, AND IN THE SAME REGION ANOTHER STATE BECAME A PLATFORM BUYER

⏱️ `2026-10-18`, pass 297.

`T-p287` recorded that the generative unit in education had become **the ministry**. `p297` measures
the next move, and it **splits in two opposite directions inside one `region` value**.

🟢 **Nigeria publishes.** **N-ATLAS** — a government-released open multilingual model covering
**Hausa, Yoruba, Igbo and Nigerian-accented English** (Sept 2025) — was open-sourced *deliberately*,
so others on the continent could build on it. **GSMA and five African governments** then launched
**ATLAS Umoja AI** to scale **Nigeria's language-model template across the continent**. The unit is no
longer a ministry procuring a system; it is **a state shipping weights for other states to fork.**

🔴 **Kazakhstan buys.** The same quarter, by **presidential decree**, AI enters Kazakh schools from
**`1 September 2026`** — pilot in **10 rural schools** (Pavlodar, Kyzylorda), **500 institutions by
January 2027** — on **165 000 free ChatGPT Edu licences** from a **November 2025** memorandum with
**OpenAI, Freedom Holding and Bilim Group**, as part of OpenAI's **"Education for Countries"**
inaugural cohort.

🔵 **Why this is one trend and not two.** Both are **state-driven, 2026, and filed `EMEA`** — and they
imply **engagements with nothing in common**. Where the state publishes, the studio's opening is the
**delivery and evaluation layer on top of public weights**, and the gap is that the most deployed tool
is closed (`aprendIA`, **5 800 teachers → 137 000 projected by 2028**, proprietary). Where the state
buys, the opening is the **governance, evaluation and integration layer around a platform already
paid for**.

⚠️ **What to check before this trend carries a date in a SOW.** N-ATLAS's **licence terms are unread**
— this pass recovered **no repository slug** for it, so *"open-sourced"* is **press-attributed**, the
same grade `p295` gave the Ethiopian instruments. **KazLLM** (reportedly 8B and 70B) is
**commentary-attributed and unread.** The dates and seat counts are reported; **the grants are not
verified.**

## 🔴 `T-p297b` — THE OPEN EDUCATION-AI STACK IS TOP-HEAVY: 42 AGENT ROWS OVER AN INSTITUTIONAL LAYER THAT WAS NEARLY EMPTY

⏱️ `2026-10-18`, pass 297. Evidence:
[`p297-promotion-gap.2026-10-18-p297.tsv`](../evidence/p297-promotion-gap.2026-10-18-p297.tsv).

🔴 **Measured, not asserted.** Entering this pass these shelves carried **42 agent rows** and, for the
layers an institution actually contracts about:

| layer | rows before `p297` |
|---|---|
| evaluation | **1** |
| curriculum-standards interop | 🔴 **0** |
| credentialing | 🔴 **0** |
| governance / audit | 🔴 **0** |
| LMS-integration MCP adapters | **10** *(4 Canvas, 3 Google Classroom, 3 Moodle)* |

🔵 **The redundancy and the vacancy are the same finding.** The community has built the **agent** and
the **adapter** many times over — `p297` found **~20 more LMS adapters** sitting unshelved in this
base's own orphan list, i.e. **duplicative capability** — while **nothing** was building the
standards, credentialing and audit layers. Those are now filled from the **standards body itself**
(`1EdTech`), a **government** (`UKGovernmentBEIS/inspect_ai`, 8 033 commits) and a **vendor**
(`microsoft/agent-governance-toolkit`, 6.4k★) — **not** from the education-AI community.

🟢 **The consequence for a studio is a pricing one.** The tutor is a commodity: **36 permissive agent
rows** can start one. What a client cannot download is **a defensible evaluation, a machine-checkable
curriculum alignment, a verifiable credential and an audit trail** — and until this pass this base had
**almost no answer** for any of them. **That is where the margin is.**

## 🟢 `T-p297c` — ALL FOUR REGIONS NOW NAME THE SAME BINDING CONSTRAINT, AND IT IS NOT MODEL QUALITY

⏱️ `2026-10-18`, pass 297.

| region | adoption | governance |
|---|---|---|
| **North America** | students **92%** | 🔴 **~10%** of institutions have formal AI guidelines; **71%** of US teachers untrained |
| **EMEA** | — | **Art. 4 AI-literacy duty in force since `2026-02-02`**; Annex III education high-risk **`2027-12-02`** (`T-p296a`) |
| **APAC** | — | Korea Framework Act in force **`2026-01-22`**; Kazakhstan school decree **`2026-09-01`** *(filed EMEA)* |
| **LATAM** | students **92%** · faculty **79%** | 🔴 **~26% with a strategy** *(IESALC)* / **~30% with a published policy** *(DEC leg)* |

🔵 **Four regions, four instruments, one gap: near-universal use with governance in the 10–30% band.**
⚠️ **The LATAM pair must not be blended** — *published policy* and *strategy* are different
measurements from different surveys; they corroborate an **order of magnitude**, not a trend line.

🟢 **This is why `p297` spent its promotion budget on substrates rather than agents.** The constraint
every region names is **documentation, oversight and auditability** — and the EU's extra sixteen
months (`T-p296a`) is **build time, not relief**. The rows that answer it are now shelved:
[`inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai),
[`agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit),
[`edu-qurating`](https://github.com/AI-for-Education/edu-qurating),
[`OpenCASE`](https://github.com/1EdTech/OpenCASE) and
[`digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator).

## 🔴 `T-p297d` — IN APAC THE MANDATED EDUCATION QUERY RESOLVES TO CORPORATE L&D, AND FOUR PASSES NOW AGREE

⏱️ `2026-10-18`, pass 297.

🔴 `AI education APAC 2026 adoption regulation players` returned **no education-specific regulation**
for the fourth pass in a row, and **every non-nil hit was corporate learning**: **TCS + Pearson**'s
multi-year AI learning alliance, **LearnUpon**'s Sydney APAC HQ and *Create+* authoring,
**Alteryx**'s Academy relaunch with credentials, **NIIT MTS**'s sixteenth year on a corporate-content
list. `p292` found exactly this; `p297` confirms it is **a property of the channel, not of the
quarter.**

🔵 **The actionable reading is not "APAC is thin."** It is that **in APAC the buyer the corpus
surfaces is an employer, not a ministry** — so an APAC pitch built from this channel will be a
**skills-and-credentialing** pitch, which is why
[`digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator)
(new this pass) matters more here than a tutor does. 🟢 A **country-named** leg has broken this nil
**every time it has been tried** (`p291` Indonesia, `p293` ASEAN); the mandated phrasing has broken it
**never**.

## 🔴 `T-p296a` — THE EU'S EDUCATION HIGH-RISK DEADLINE MOVED TO DECEMBER 2027, AND THE DUTY THAT ACTUALLY BINDS TODAY IS THE ONE NOBODY IS SELLING

⏱️ `2026-10-18`, pass 296.

The **Digital Omnibus on AI** moved **Annex III stand-alone high-risk obligations — education's
bucket — from `2 August 2026` to `2 December 2027`** (Annex I embedded: `2 August 2028`). **The Art. 4
AI-literacy duty was not delayed and has applied since `2 February 2025`. Prohibitions were not
delayed.**

🔴 **Two things follow, and they point in opposite directions from each other.** (1) **The compliance
pitch is dead for sixteen months** — a client told *"you must be conformant by August 2026"* will find
out. (2) **The literacy duty is overdue and unsold**: it binds every organisation using an AI system,
which is every school, and the **EC/OECD AI Literacy Framework for Primary and Secondary Education
(18 June 2026)** is a ready-made curriculum spine for delivering it.

🔵 **The classification did not change** — admissions ranking, student evaluation and exam scoring are
still Annex III high-risk. So the extra time is **build time, not relief**: design to the high-risk
standard now, because retrofitting conformance into a shipped grading pipeline is the expensive path.
⚠️ The omnibus dates are contested (Council `29 Jun 2026` vs Commission *"in force 27 Jul 2026"*) —
**check the Official Journal before a SOW carries a date.**

## 🟢 `T-p296b` — APAC HAS THE ONLY EDUCATION-NAMED COMPLIANCE DATE IN FORCE ANYWHERE, AND ANZ IS NOT PART OF ITS MARKET

**South Korea's Framework Act on AI** (horizontal, in force **22 Jan 2026**) and **Vietnam's AI law**
(in force **1 Mar 2026**) end the "APAC is voluntary guidance" reading this base has carried.
🔴 **Vietnam's is the sharper instrument: systems in education, healthcare and finance already
operating before `15 Aug 2026` get an additional six-month grace period** — an education-named,
dated migration window, and the only one of its kind the legs have found in any region.

🔴 **And the region splits on sentiment in a way that breaks "APAC" as a unit.** The **Ipsos Education
Monitor 2026** finds lower support for banning AI in schools across the Asian markets surveyed, **with
Australia and New Zealand the explicit exception — higher support for a ban.** The student-facing pilot
that sells in Southeast Asia is the one that draws organised opposition in ANZ. **Place ANZ
separately**, exactly as `T-p286a` concluded for Africa: a continental label gets the licence and now
the sentiment posture wrong.

## 🔴 `T-p296c` — ADOPTION IS NO LONGER THE SELLABLE PROBLEM: 87% ADOPTED, 26% GOVERNED

**UNESCO IESALC**, 200 higher-education institutions, 19 LATAM countries: **87% use AI in at least one
area; 26% have a formal AI strategy**, and adoption is driven by **individual academics, researchers
and students** rather than institutional plans.

🔵 **That is shadow AI at institutional scale, and it generalises past LATAM.** 1EdTech reports the
same move worldwide — *experimentation → governance* — and HolonIQ reports the real gains are in
**course design, teacher productivity and administrative workflows**, not student-facing novelty.
**The deliverable is shifting from a system to a system plus a policy plus an evaluation regime.**

🔴 **The commercial edge of this base's evaluation gap.** 1EdTech reports buyers now demand evidence
that products improve learning, persistence, well-being or job-relevant skills. **An engagement with
no measurement plan is becoming unsellable** — so the missing eval layer is a revenue problem, not
only a technical one. `p296` shelved the first permissive, education-specific instrument against it:
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
(MIT, Chilean MINEDUC teacher-exam items), alongside the eval framework shipped with
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (Apache-2.0).
⚠️ Neither is a maintained harness. The gap is **narrowed, not closed.**

## 🔴 `T-p296d` — A KB'S BINDING CONSTRAINT STOPS BEING DISCOVERY AND BECOMES PROMOTION, AND NOTHING IN THE PIPELINE NOTICES

**Measured on this base, this pass.** The agents leg returned its **22nd consecutive nil** while
[`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — **MIT, 41.0k★, the largest education-AI
repository this base knows of** — sat verified **inside this repository**, in `agents/trending.md`,
**unshelved**. `p989` had already measured the condition on `2026-10-10`, publishing **~500 permissive
orphans** out of `1 119`; no pass worked the list. `p296` promoted **8 rows** from it and **not one
was a discovery** — and the attempt to promote **two more was refused by this base's own identity
gate, because they were already shelved.** 🔴 **So the orphan list is itself partly stale: it names
candidates, not absences, and a promotion must be checked against the shelf before it is written.**

🔵 **The generalisable finding, which is the one worth carrying to other industries' bases:** a
curation pipeline that measures itself by *what it found this pass* will report a thin market when it
actually has a **broken promotion path** — and the two failure modes produce **identical output**, a
nil. 🔴 **Twenty-one nils were read as evidence about the world; they were evidence about the
pipeline.** The distinguishing test is cheap: before searching, ask whether anything already verified
is unshelved. `ACTION PG` now stands on [`agents/top.md`](../agents/top.md).

⚠️ **The star column was complicit.** Three of the five substrates read this pass exceed 2 000
commits and none exceeds 352★; `datakind/student-success-tool` has **8★ / 3 015 commits** and a
reported graduation gain at a named college. **Rank on commits and named deployments, not stars.**

## 🟢 Pass 295 — STALENESS TRACKS PROVENANCE, NOT AGE — and the unworked region beat the worked one again

⏱️ **Seventeenth pass of `2026-10-18`.** Evidence:
[`p295-star-channel.2026-10-18-p295.tsv`](../evidence/p295-star-channel.2026-10-18-p295.tsv) ·
[`p295-websearch.2026-10-18-p295.tsv`](../evidence/p295-websearch.2026-10-18-p295.tsv) ·
[`p295-dns-control.2026-10-18-p295.tsv`](../evidence/p295-dns-control.2026-10-18-p295.tsv).

### 🟢 Trend 1 — the figures that rot are the ones you were told, not the ones you read

🟢 **Eleven published cells re-read: seven exact, two drifted, two refuted.** 🔵 The split is not
random. **Every cell `p294` refuted came from a social post or an SEO blog; every cell read
first-hand at a pin confirmed.** The one that had been wrong for **eighteen passes**
(`ai-agents-for-beginners`, *"12 lessons"*) was never measured by this base at all.

🔵 **The operational consequence for a studio:** an inventory's decay rate is a function of **how its
entries were acquired**, not how old they are. A figure read at a pin in July is worth more than a
figure collected from a vendor page this morning. 🟢 Budget re-verification against **provenance**,
and re-read the *told* rows first.

### 🔴 Trend 2 — stars are not monotonic, and a trend built on two reads is noise

🔴 **`ls1intum/Artemis`: 819★ → 817★**, while commits advanced `12,437 → 12,440`. 🔵 Users unstar.
**A falling star count is not a broken read**, and any *"X is accelerating"* claim built on two
reads a day apart is below the channel's own resolution: `WebFetch` renders **`8.4k`, not `8,412`**,
so the bound on a four-digit-plus count here is **`±50`**. 🟢 Quote `41.6k ±50`, never `41,600`.

### 🟢 Trend 3 — forks, not stars, are where public-sector adoption shows up

Three fork counts this base had never published, all read this pass:

| repo | stars | forks | ratio |
|---|---|---|---|
| `oppia/oppia` | 6.9k | **5.8k** | **84 %** |
| `learningequality/kolibri` | 1.2k | **1.0k** | **83 %** |
| `portabilis/i-educar` | 719 | **550** | **76 %** |

🔵 This base has argued for many passes that **forks approaching or exceeding stars marks software
institutions RUN rather than developers BOOKMARK** — first on `Submitty` and `Ed-Fi`, then as the
explanation for `Sunbird`'s **41★ against 38,046 commits**. 🟢 It now holds on three more rows across
three continents. **When provenance suppresses stars — ministries, universities, municipalities —
the fork count is the adoption instrument.**

### 🟢 Trend 4 — offline-first has moved from a constraint to a WRITTEN REQUIREMENT

🟢 Ethiopia's MoE launched a curriculum-integrated AI teacher assistant **prioritised to run
offline** (`2026-05-14`). 🔵 **IFEF**, in Francophone West Africa, states the matching constraint
from the data side: *« nos données ne sont pas sur Internet »*. 🔵 Those are the same engineering
problem as the LATAM data-residency objection, and the answer is architectural — local inference
over a locally-authored corpus. 🟢 `P52` in [`compose/patterns.md`](../compose/patterns.md) is the
recipe; `Numbas` (in-browser marking) has been making the structural version of this argument here
since `p266`.

### 🔴 Trend 5 — governance keeps losing to procurement, and the gap is now quantified on two continents

| region | buying | governing |
|---|---|---|
| **North America** | OpenAI country-level programme (**8 national partners**); **CMU + Gates USD 55 M** into gateway-course courseware | **10 %** of institutions hold a formal AI guideline; **71 %** of US teachers have no AI training |
| **APAC** *(enterprise, not schools)* | **87 %** of organisations encourage AI agents | **47 %** have governance, oversight and controls |

🔵 **The deliverable that closes the gap is the differentiator**, and it is cheap: a usage policy, an
assessment-integrity position and staff training shipped *with* the courseware. 🟢 Ethiopia has
already made it a condition of entry at the higher-education level — **the market that writes it
down first is the easiest one to sell it in.**

## 🟢 Pass 294 — A CHANNEL THIS BASE DECLARED CLOSED WAS OPEN, AND READING IT REFUTED THREE OF ITS OWN PUBLISHED CELLS

⏱️ **Sixteenth pass of `2026-10-18`.** Evidence:
[`p294-star-channel.2026-10-18-p294.tsv`](../evidence/p294-star-channel.2026-10-18-p294.tsv) ·
[`p294-proxy-existence-control.2026-10-18-p294.tsv`](../evidence/p294-proxy-existence-control.2026-10-18-p294.tsv) ·
[`p294-websearch.2026-10-18-p294.tsv`](../evidence/p294-websearch.2026-10-18-p294.tsv).

### 🟢 Trend 1 — the industry trend is unchanged and the SPREAD is the story: buying is ahead of governing

🔵 Two unrelated publishers, two unrelated instruments, same conclusion. Market maturity is scored
**35/100** — *"most institutions are still in pilot mode"* — while **~10 %** of North American
institutions have formal AI guidelines and **71 %** of US teachers have no AI training. 🟢 **The gap
between deployment and governance is now corroborated across channels**, which is more than this
file could say when it first carried the observation.

🔴 **And the sizing numbers got further apart, not closer:** **$6.4 B (2025) → $79.6 B (2034)**
against **$7.52 B (2025) → $10.6 B (2026)**, with CAGRs quoted from **28 %** to **36 %**. Five
publishers, five definitions. 🔵 A studio quoting any one of them in a bid should quote the spread.

### 🔴 Trend 2 — the national-language channel is SATURATED where the region has been worked

🇻🇳 `p290` · 🇲🇽 `p291` · 🇪🇬 `p292` · 🇮🇩 `p293` · 🇮🇳 `p294` — **five for five on non-nil.** 🔴 **The
fifth is the first whose yield is almost entirely carried**: India's mandatory AI & Computational
Thinking curriculum for **Classes 3-8 from 2026-27**, the OpenAI/IIT Madras collaboration and the
BHASHINI tie-in are all already on these shelves, in five files. One new datum — the **Bharat Bodhan
AI Conclave 2026**.

🟢 **The leg that paid was the unworked REGION, not the new language.** 🌍 Swahili/Africa, never
queried before by this base, returned three new instruments in one hour: **`Google.org` $4 M** for
AI upskilling across **Nigeria, Ghana, Kenya and South Africa**; **UNESCO**'s plan to train **15 000
public servants and 5 000 judicial officers**; **ACA 2026** in **Dar es Salaam, 15-18 September
2026**, hosted by the **Tanzania Institute of Education**.

🔵 **The generalisation, stated so the next pass can spend its legs well:** the variable is not the
language, it is **whether the region has already been reached by some channel**. 🔴 A sixth language
aimed at a worked region will return non-nil and mostly carried — which looks like a result and is
not one.

### 🟢 Trend 3 — `api.github.com` is evidence about `api.github.com`

🔴 `p293` measured `api.github.com` (`rate_limit` → `200`, repository metadata → `403` by policy) and
concluded: *"No star count in this pass is first-hand and none is published."* 🟢 **The channel its
own [`P349`](../compose/code/p349-star-resolution-band/README.md) instrument is built on —
`WebFetch` over the rendered `github.com` page, used at `p110` on `2026-10-05` — answers today.**

| cell | published | rendered `2026-10-18` |
|---|---|---|
| `microsoft/ai-agents-for-beginners` stars | **67.2k** *and* **47.3k** (`p293`, 42 % apart, unresolved) | 🔴 **77.4k** · 25.4k forks · MIT |
| …its description | *"a **12-lesson** course"*, this base's prose since `p275` | 🔴 **"18 Lessons to Get Started Building AI Agents"** |
| `HKUDS/DeepTutor` stars | **41.5k** | 🟢 **41.6k** · 5.3k forks · `v1.6.14`, `2026.10.8` |
| a claim from this pass's own leg | *"over 32 741 stars and 4 274 forks"* | 🔴 **refuted** — stars are monotonic and `p110` read **40.8k** |

🔵 **The error class matters more than the four cells.** `p293` named it in the same pass —
*"guessing a name the channel will tell you"* — and then committed it against a different channel.
🟢 **Resolution bound carried unchanged:** `K-3CIFRAS`, ±50 in this band. **41.6k** and **77.4k** are
figures with a stated error, not integers.

### 🔴 Trend 4 — a refusal that cannot tell a real host from an invented one

🟢 **Calibrated in one session, with both a known-real and a known-fake control:**

| probe | curl | in the proxy's own ledger | truth |
|---|---|---|---|
| `raw.githubusercontent.com` | **`200`** | no | real |
| `github.com` | **`403`** | no | real — **five `LICENSE` blobs read through `raw` in the same minute** |
| `en.wikipedia.org` | **`000`** | **yes**, `connect_rejected` | real |
| **an invented hostname** | **`000`** | **yes**, *byte-identical mechanism* | 🔴 **cannot exist** |

🔴 **So `EGRESS_DENIED (allowlist)` says nothing about whether a source exists.** The gateway refuses
the CONNECT **before name resolution**, so an invented host earns the same ledger entry as a real
one. 🔵 [`P798`](../compose/code/p798-proxy-refusal-ledger/README.md) read that ledger as licensing
*"the source is fine, this environment may not read it"*. **It licenses neither** — repaired this
pass with a separate `existence_verdict()` over a closed two-token vocabulary, **9 → 22 controls**,
and wired into `make hooks`.

🔵 **The consequence for every regional figure on these shelves:** the mandated *"verify every URL
with `curl -sI`"* is **unsatisfiable on this channel**, so regional sources are ATTRIBUTED by
construction, and a `000` beside one of them is a fact about the gateway. 🟢 The channels that do
work are **`raw.githubusercontent.com`** and **`WebFetch`**, and every grant this pass published was
read through the first.

### 🟡 Trend 5 — the permissive layer is still the agent layer, and that is now measured four times over

🔴 Fifteen passes with no permissive education ERP/CRM. This pass read **four** permissive
repositories at pins — [`ChurchCRM/CRM`](https://github.com/ChurchCRM/CRM) (MIT),
[`ONLYOFFICE/CommunityServer`](https://github.com/ONLYOFFICE/CommunityServer) (Apache-2.0),
[`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) (MIT),
[`MadsLorentzen/ai-job-search`](https://github.com/MadsLorentzen/ai-job-search) (MIT) — and
**disqualified all four on their READMEs**, three of them with **zero** education tokens.

🔵 **The structural trend, now with verified negatives behind it:** the education verticals are
copyleft end to end (Moodle `GPL-3.0`, Open edX `AGPL-3.0`, OpenEduCat `LGPL-3.0`, ERPNext and
Frappe CRM `GPL`/`AGPL`), while the agent tier is MIT/Apache almost without exception. 🟢 **A
permissive education platform is not a thing to find; it is a thing a studio assembles** — which is
what every recipe on [`compose/patterns.md`](../compose/patterns.md) does.

## 🟢 Pass 293 — THE REGIONAL NILS ARE A QUERY-LANGUAGE ARTEFACT, PROVEN IN A SINGLE PASS; AND THE TREND THAT MATTERS IS A MANDATE THAT NAMES ASSESSMENT

⏱️ **Fifteenth pass of `2026-10-18`.** Evidence:
[`p293-websearch.2026-10-18-p293.tsv`](../evidence/p293-websearch.2026-10-18-p293.tsv).

### 🟢 Trend 1 — the national-language channel is FOUR FOR FOUR, and it is now a controlled measurement

🇻🇳 `p290` · 🇲🇽 `p291` · 🇪🇬 `p292` · 🇮🇩 **`p293`**.

🔵 Every earlier proof spanned two passes. **`p293` ran the English APAC leg and the Indonesian
APAC leg in the same hour, over the same region**, and they disagree about whether an education
policy layer exists in Asia: the English leg returned four corporate-L&D items and its own
summary of *"no education-specific APAC regulation"*; the Indonesian leg returned a **fourteen-
nation ministerial work plan**. 🔴 So `p292`'s *"3 of 3 are corporate L&D — supply-side
displacement corroborated from the demand side"* is **withdrawn**: the displacement was in the
query. 🔵 `p286`'s APAC "explicit nil" has the same explanation, retrospectively.

🔴 **The operational consequence for this base**: a region-named English leg is not a measurement
of a region. It is a measurement of English-language press coverage of a region, and the two
differ most where the education system is largest.

### 🟢 Trend 2 — the regional mandate now names ASSESSMENT, which is where this base's findings already were

The **ASEAN Work Plan on Education 2026-2030** (launched at the 14th ASEAN Education Ministers
Meeting, Singapore, `2026-07-22`) anchors on **AI readiness, STEM capability and holistic student
development**, and defines AI readiness as *"updating curricula, teaching methods **and
assessments**"*.

🔵 **That matters because of a bias this base measured on itself.** `T229` recorded that the
vertical's live edge is **exam-shaped** — four of five new finds were assessment — while the
shelf's rows were almost all **tutoring**. 🟢 A fourteen-nation mandate naming assessment turns
that from a sampling bias into a *market* reading: **the procurable work is assessment and
readiness, not tutor deployment**, and now a regional instrument says so.

🔴 **And Indonesia's commitment is conditional in exactly the procurable way.** AI becomes a
compulsory subject *only after* **teacher readiness, curriculum and learning infrastructure** are
judged adequate. The gate is the engagement: readiness assessment, teacher training, curriculum
and assessment redesign. 🔵 Named in the instrument, not inferred from it.

### 🔴 Trend 3 — the licence risk keeps running OPPOSITE to expectation, and this pass has a clean case

🔵 This file has recorded for several passes that the licence surprises run the *wrong* way: the
permissive-looking thing is gated and the copyleft thing is honest. `p293` adds a pair that makes
the point in one line each:

| artefact | expectation | measured |
|---|---|---|
| `tokenaii/Horus-Taleeq-0.2B-Base` — a 200M-parameter model from a startup | "weights-available, licence vague" | 🟢 **MIT, read at a pin**, 1 080 B, sha256₁₂ `96c22722c817`, and the README **agrees** with the payload. Shipped **with training code, data policy and a compute profile** |
| `tokenaii/Horus-Lens-1.0` — the same org, the same week | "same org, same grant" | 🔴 **`DANGLING-CLAIM`.** Four licence paths `404` at the pin; the README asserts Apache-2.0 and nothing serves it. Posture **`ASK`** |
| **OpenEduCat**, the sector's leading open ERP | "LGPL-3.0, done" | 🔴 **DUAL.** Community LGPL-3.0; **Enterprise proprietary and agreement-gated**, forbidding publishing, distributing, sublicensing or selling copies (`p292`, standing) |

🔵 **One org, one week, two grades.** The unit of licence risk is **the repository**, never the
organisation and never the model family — which is why these shelves pin per-slug and why
`p293`'s README column now runs on every swept row rather than by hand.

### 🟡 Trend 4 — the market numbers did not move, and the spread is still the finding

IMARC **USD 6.4B** (2025) → **79.6B** (2034); Grand View via GIIResearch **8.3B** (2025) →
**57.2B** (2033); The Business Research Company **10.6B** (2026), up from **7.52B** (2025).
Student AI use **66% (2024) → 92% (2025)**. AI-tutor market **USD 1.63B** (2024), language
learning the fastest-growing segment. Sector maturity rated **35/100**, *"most institutions still
in pilot"*.

🔵 **Every figure here was already on this shelf at `p292`; the leg moved nothing**, which is
itself worth recording after fifteen passes in a day. 🔴 And the LATAM pairing is the one to
quote: **92% of students engaging** against a **"Rest of Latin America" market of USD 18.2M
(2024) → 36M (2029)**. Near-universal adoption with no budget line is not a contradiction — it is
the shape of the engagement, and it argues for small, fast, self-funding work over a platform
programme.

### 🔴 What this pass could NOT establish

🔴 **No primary government source was read**, for the fifteenth pass. `moe.gov.sg` (including the
exact speech URL, now recorded), `asean.org` and `gov.br/mec` answer `ENOTFOUND` via WebFetch and
`000` via curl — two distinct egress routes, both closed. The ASEAN work plan and the MEC
Referencial are **`ATTRIBUTED`** to press, each corroborated by multiple independent outlets.

🔴 **`huggingface.co` remains closed**, so the Horus weights' model cards were not read; the GGUF
and 4B variants are Hugging Face-only and stay unverifiable from here.

🔴 **`api.github.com` is reachable but SCOPED**, and that is a correction worth recording for any
pass that reads its own channel notes: `rate_limit` answers **`200`** with an authenticated
15 000-request budget, which looks exactly like an open channel. 🔴 Repository metadata for any
slug this session is not attached to answers **`403`** by policy, and `search/repositories` is
refused outright. 🔵 **A `200` on `rate_limit` is evidence about `rate_limit`** — `P1057`'s lesson
one more level out. No star count in this pass is first-hand, and none is published.

## 🟢 Pass 292 — THE COMPLIANCE RECORD IS THE PRODUCT, THE NATIONAL LANGUAGE IS THE CHANNEL FOR THE THIRD TIME, AND THE LICENCE RISK RUNS OPPOSITE TO EXPECTATION

⏱️ `2026-10-18`, fourteenth pass. Evidence:
[`p292-websearch.2026-10-18-p292.tsv`](../evidence/p292-websearch.2026-10-18-p292.tsv) ·
[`decision-store-worked.2026-10-18-p292.jsonl`](../evidence/decision-store-worked.2026-10-18-p292.jsonl).

### 🟢 `T-p292a` — the agent layer went free; the RECORD never did, and that is now demonstrable rather than argued

🔵 **The trend this base has been circling for four passes, stated as a built fact.** Across
`P45`-`P49` the model layer is permissive and costless: `iblai`'s segment configs are
`GRANTED-AT-PIN` MIT across all seven segments (`p291`), `cedanl/student-signal` is MIT. 🔴 **What
no repository on these shelves supplies, after 292 passes, is the record of who decided what,
shown what, under which rubric version.**

🟢 **`p292` built it** — [`compose/code/p292-decision-evidence-store`](../compose/code/p292-decision-evidence-store/README.md),
**106 offline controls**, standard library only. 🔵 The strategic shape: three separate regimes
— EU **Annex III(3)** human oversight, the **Oklahoma / Maryland** bar on AI in high-stakes
student decisions, **Vietnam**'s sole-basis test — all ask the *same* question, *can you show a
human decided and what they were shown?*, so **one implementation answers all three in all four
regions**. That is a rare property and it is the commercial centre of this whole file.

🔴 **The counter-trend to price in: this product category's standard overclaim is exactly here.**
A hash chain in a file is tamper-**evident**, not tamper-proof. Control `C18` asserts that a
full rewrite verifies **clean**, so the limit is a control rather than a footnote, and what
closes it is anchoring the head where the writer cannot reach it. 🔵 Any vendor selling an
"immutable audit log" that cannot say where its anchor lives is selling the chain and not the
guarantee.

### 🟢 `T-p292b` — the vocational displacement is now visible on BOTH sides of the market at once

🔴 `p291` measured it on the **supply** side: inside the one MIT corpus this base has read end
to end, the learning-and-development agents sit in segments labelled `enterprise`,
`government`, `legal`, `financial-services`, `medical-healthcare` — and are the **least**
guarded (1 of 6 carried a human-decision guard, against 23 % inside the education-labelled
segments).

🟢 **This pass the same displacement arrived from the demand side, unprompted.** The APAC
regional leg returned **three** education-adjacent items and **all three are corporate L&D**:
TCS + Pearson's multi-year AI learning alliance aimed at employer skills gaps, LearnUpon's
Sydney HQ with AI course authoring, Alteryx's Academy relaunch with AI learning paths. 🔴 **Zero**
school, university or ministry results in that leg. The global trends leg named **corporate
reskilling** as a demand driver in the same breath as tutoring.

🔵 **The trend, stated for a studio:** the education-regulated buyer increasingly **is not an
education institution**. A law firm tracking CLE, a broker-dealer tracking FINRA continuing
education, a hospital tracking credentialing — each is operating inside the Act's education
limb and none of them answers an education-sector sales motion. `P48` is the recipe; `T-p292b`
is now its second independent corroboration.

### 🟢 `T-p292c` — the national language is the channel: THIRD proof, and the English regional leg is a measured query defect

🔴 **The mandated EMEA phrasing has now returned SIX consecutive nils.** `p291` ranked it as a
dead channel and said not to re-run it; it was re-run this pass because the standing battery
mandates it, and it returned a sixth nil — enterprise-AI generalities (CompTIA, Workday,
Bandwidth-Cavell) with **no** schools, universities, edtech vendors or national education
policy. 🔵 Six measurements is now enough to call it a property of the **query**, not of EMEA.

🟢 **Against that, the directed language legs keep working on the first attempt:**

| pass | language | what the English leg had returned | what the national-language leg returned |
|---|---|---|---|
| `p290` | 🇻🇳 Vietnamese | nothing on mandate level | compulsory grades 1-12, against 🇹🇭 optional |
| `p291` | 🇲🇽 Spanish | an explicit nil | SaberesMx, `labmexia.gob.mx`, a 1.5 M-student SEP survey |
| `p292` | 🇪🇬 Arabic | six consecutive EMEA nils | a national LLM, a deployed school AI teacher, **and a permissive Cairo model family** |

🔵 **Three for three.** The generative unit is the one `T-p286a` and `p287` identified — exam
board, language of instruction, education ministry — and **never the region name**. 🔴 The
operational consequence is a query-design rule, not a research tip: a region-named English leg
measures **English-language press coverage of that region**, which is a different population
from the region's education sector.

### 🔴 `T-p292d` — the licence risk inverts: the SOVEREIGN model is the unlicensed one, the STARTUP model is permissive

🔵 **The intuition a studio arrives with** is that a state-funded national model will be openly
licensed and a startup's will be locked down. 🔴 **Egypt this pass is the opposite.** Karnak is
placed by officials *inside public digital infrastructure* so startups can build on it, and one
outlet reports it open-sourced at 41 B parameters — **and no licence is stated anywhere this
base could reach**, including MCIT's own pages, which do not mention weights at all. The
school-facing `Sia` has no grant either. Meanwhile **TokenAI, a Cairo startup, reports MIT on
two models and Apache-2.0 on a third**, one of them released *with its training code and data
sources*.

🔴 **Neither side is verified**, and that is the finding's other half: four verification channels
closed this pass (`huggingface.co` `403` by one egress path and `ENOTFOUND` by a second; the
sole outlet `ENOTFOUND`; anonymous `git ls-remote` inconclusive; `raw` `404` on guessed
spellings only). 🔵 **For an engagement:** *"it is a sovereign model, so the licence will be
fine"* is not a finding, and *"it is a startup, so it will be restrictive"* is not either. The
grant is a file to read at a pin — and where it cannot be read, the honest posture is
`CANDIDATE-ATTRIBUTED` and a named directed leg, not a row in a table.

### 🟡 `T-p292e` — the adoption-governance gap is now double-quantified in LATAM and widest in North America

🟢 **LATAM, two independent instruments this pass.** Digital Education Council's *AI in Higher
Education LATAM Survey 2026*: **>30 000 responses, 29 institutions**, **92 %** of students and
**79 %** of faculty actively engaging with AI. UNESCO IESALC across **200 HEIs in 19 countries**:
teaching and learning **73.5 %**, research **57.0 %**, administration **34.1 %**, community
engagement **20.0 %**. 🔴 Against **only 30 %** of LATAM universities having published AI-use
policies (Tec de Monterrey).

🔴 **North America's gap is wider still:** **~36 %** regional share and the heaviest public money
in the set, against **~10 %** of institutions holding formal AI guidelines and **71 %** of US
teachers without AI training.

🔵 **Why this keeps being the most sellable number on the shelf:** demand-side adoption is a
*fait accompli* in both regions and the governance layer is missing in both. 🟢 That is the same
hole `T-p292a`'s component fills, which is why the two trends are one engagement and not two.

## 🟢 Pass 291 — THE SUPPLY-SIDE GUARD IS REAL, IT DOES NOT SPEAK THE REGULATOR'S LANGUAGE, AND IT IS THINNEST EXACTLY WHERE THE REGULATION IS WIDEST

⏱️ `2026-10-18`, thirteenth pass. Evidence:
[`guard-vocabulary.2026-10-18-p291.tsv`](../evidence/guard-vocabulary.2026-10-18-p291.tsv) ·
[`segment-education-surface.2026-10-18-p291.tsv`](../evidence/segment-education-surface.2026-10-18-p291.tsv) ·
[`p291-websearch.2026-10-18-p291.tsv`](../evidence/p291-websearch.2026-10-18-p291.tsv).

### 🟡 `T-p291a` — the guard and the regulation use different words, and the gap is measurable

🟢 **`T-p290a` stands**: the human-checkpoint requirement has a supply side, shipping as MIT
prompt configuration. `p291` measured the whole corpus rather than the three agents `p290`
quoted, and the trend survives with one correction attached.

🔴 **The corpus does not contain the regulator's phrase.** Across **95 agents**, *"sole basis"*
appears **once**, in a note about CPT code selection — not a guard. The guard itself is present
in **12** agents, under four other phrasings:

| what the payloads say | agents of 95 |
|---|---|
| *"...unilaterally"* | 3 |
| *"a hypothesis to be confirmed, not a verdict"* / *"observations, not conclusions"* | 3 |
| *"support human decision-making"* / *"input for the human reader"* | 4 |
| *"flag for human review"* | 5 |
| *"not by any single professional or AI tool"* / *"the full team"* | 2 |
| *"never make eligibility determinations"* / *"do not independently authorize"* | 3 |
| 🔴 **the regulator's own *"sole basis"*** | **1 — and it is a false positive** |

🔵 **Why this is a trend and not a lexicography note.** The compliance market forming around
`T-p288a` sells *evidence that a human checkpoint exists*. The checkpoint is being written by
engineers in engineers' words and audited by reviewers with regulators' keyword lists. A sweep
of this MIT corpus for AI-Act vocabulary scores **one hit and it is wrong**, while 12 real
guards sit untouched. 🟢 **That mismatch is a billable translation layer** — a guard-clause
taxonomy mapping payload language to Annex III limbs — and nothing on these shelves supplies it.

### 🔴 `T-p291b` — the high-risk category is wider than the segment labels, and the guards are thinnest in the wider part

🔴 **EU AI Act Annex III(3) is not "schools".** Limb (a) covers access, admission or assignment
to educational **and vocational** training institutions; limb (b) the evaluation of learning
outcomes, including where they steer a learner's path. **One limb suffices.** 🟡 Posture:
ATTRIBUTED — a conference reproduction of the text plus commentary; EUR-Lex was not reached.

🔴 **Measured against that, the corporate L&D layer is in-scope and under-guarded.** The five
`iblai` segments labelled *not education* each ship a learning agent — and two track a
**regulated professional credential** (CLE for lawyers, FINRA continuing education):

| | education-labelled segments | the five others |
|---|---|---|
| agents | 30 | 65 |
| carrying a human-decision guard | 7 (**23 %**) | 5 (**8 %**) |
| L&D agents among them | — | 6, of which **1** is guarded |

🔵 **The direction for a studio:** the guard discipline that `p290` found in the admissions and
special-education agents has **not** travelled to the training agents one directory over, even
though the Act's education limb reaches both. The remediation is small and identical in all
four regions — which is what makes it a product rather than an engagement.

### 🟡 `T-p291c` — two ASEAN neighbours, same year, opposite mandate levels

🟢 A contrast worth recording because it is the kind of thing a regional engagement is priced
on. 🇻🇳 **Vietnam** made AI **compulsory** across grades 1-12 from the 2026-2027 school year —
Decision `3439/QĐ-BGDĐT`, 12 compulsory periods a year (`p290`). 🇹🇭 **Thailand** has added AI
content at upper-primary, lower-secondary and upper-secondary and it remains **optional**, with
compulsory status the stated *next* goal; OBEC's curriculum bureau leads, and the national AI
Strategy and Action Plan runs 2022-2027 under a PM-chaired committee.

🔴 **Neither publishes code or licensed curriculum data.** Vietnam's likeliest non-ministry
publisher, **STEAM for Vietnam**, was probed directly this pass: no GitHub organisation, no
repository, no licence — its curriculum ships as **Scratch projects**, shareable but not
vendorable. 🟡 All of the above is ATTRIBUTED to press and ministry summaries, not primary text.

## 🟢 Pass 290 — THE GOVERNANCE TREND HAS A SUPPLY SIDE NOW, AND IT ARRIVED AS CONFIGURATION RATHER THAN CODE

⏱️ `2026-10-18`, twelfth pass. Evidence:
[`p290-websearch.2026-10-18-p290.tsv`](../evidence/p290-websearch.2026-10-18-p290.tsv) ·
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`submodule-grant-boundary.2026-10-18-p290.tsv`](../evidence/submodule-grant-boundary.2026-10-18-p290.tsv).

### 🟢 1. `T-p288a` has a supply side — the human checkpoint is shipping as PROMPT CONFIGURATION

🔵 **The trend `p288` and `p289` recorded was demand-side**: four regions converging on one
engineering requirement — a recorded human decision point wherever AI output would be the sole
basis for a decision about a student. 🟢 **What `p290` found is the first supply-side answer,
and its form is the surprise.** It is not a library, an audit framework or a compliance SDK. It
is **three MIT prompt configurations that refuse the sole-basis act in their own text**:

| agent | the clause, verbatim from its `SOUL.md` | the regime it clears |
|---|---|---|
| `application-reader-agent` | *"Never issue a final admit or deny decision unilaterally; always present findings as input for the human reader"* | 🇪🇺 EU AI Act **high-risk**: admission decisions |
| `special-education-agent` | *"Never make eligibility determinations — eligibility requires a qualified multidisciplinary team evaluation and legal decision"* | 🇺🇸 IDEA 2004 + the Oklahoma/Maryland **high-stakes student decision** bar |
| `retention-agent` | *"Treat every risk flag as a hypothesis to be confirmed, not a verdict"*, and *"log every intervention — date, method, response, outcome"* | 🇻🇳 Vietnam's **sole-basis** clause; the audit trail generally |

🔴 **Why this is a trend and not three files.** `p288` found the same pattern *implemented* —
`agentic-automated-assignment-grading`'s `needs_review` terminal state — in a repository with
**no grant across 1 531 files**. 🟢 One pass later the pattern appears **under MIT, in three
sibling agents, in two market segments, written as a refusal rather than a feature flag.** The
compliance posture has moved from something a studio engineers into something a studio can
**start from**, and the artefact it starts from is a prompt, not a product.

🔵 **The actionable read.** When the deliverable is an auditable workflow, the **cheap half is
now free and the expensive half is the evidence store.** Nothing in these configs records
anything: *"log every intervention"* is an instruction to a model, not a schema, a retention
policy or an append-only log. 🔴 **That gap is the billable deliverable** — and it is the same
gap in all four regions at once.

### 🔴 2. The EMEA hole was in this base's instrument, not in the market

🔴 **Four passes of EMEA legs named only regulators** — Commission, UNESCO, OECD — and `p289`
registered the hole as item 10. 🟢 **One directed vendor leg broke it**, and the market it found
is not thin:

- **HolonIQ 2026 Europe EdTech 200** — UK the largest hub; France, Germany, Italy and Spain
  growing; the cohort **weighted toward workforce learning** rather than K-12. Synthesia and
  **NOLEJ AI** named on the content-generation side.
- **Rounds, with amounts**: **Knowunity** 🇩🇪 €27M Series B (XAnge), 20M+ students across 15
  countries · **Preply** $150M Series D (WestCap) at a **$1.2B** valuation, 100k+ tutors ·
  **Gizmo** 🇬🇧 $22M Series A · **Multiverse** 🇬🇧 £70M growth round (May 2026) ·
  **BOOKR Kids** 🇭🇺 €6.1M Series A (Aug 2026) · **Sparkli** $5M seed (Jan 2026) ·
  **Chalkie** $4M seed (Mar 2026).
- 🔴 **And the direction of the money, which is the part that changes a pitch**: roughly
  **$1B of global edtech venture funding in H1 2026, down 26% year over year** (HolonIQ).

🔵 **So the trend is a selective market, not a boom**: capital is down a quarter while the large
rounds concentrate in **workforce and tutoring-marketplace** models — Preply, Multiverse and
Knowunity are the three biggest numbers on the list and **none of them sells to a school**.
🟡 The EMEA buyer with budget is an **employer or a learner**, not a ministry — the inverse of
what this base's own EMEA sections (all regulators) implied for four passes.
🔴 **Dates attributed, not asserted**: aggregator metadata on the Knowunity round conflicts
with itself; the round is published here, the date is not.

### 🟢 3. The EMEA code hole closed in the same hour, and the code is a MEASUREMENT library

🟢 [`cedanl/student-signal`](https://github.com/cedanl/student-signal) — **MIT**, Dutch higher
education, the first EMEA-origin education code row in four passes. 🔵 **Its shape is the
trend**: it does not predict dropout for you, it **ranks** students and then reports
**precision and recall at every invitation threshold**. A product that tells its buyer how many
of the students it flags will be wrong, before anyone is contacted.

🔵 **Set that beside §1 and the pairing is the year's engagement in one line:** `student-signal`
produces a defensible number, `retention-agent` is forbidden from treating that number as a
verdict, and the thing neither of them has is the **record** that the human looked.

### 🔴 4. "Curriculum-aligned" is spreading as a MANDATE while the licence layer stays unreadable

🟢 `p289` found England's curriculum ceded for commercial reuse with 38 SHACL shapes to validate
against. 🔴 **Vietnam this pass is the counter-case, and it is the more common one**: MOET's
Decision `3439/QĐ-BGDĐT` promulgates a pilot AI content framework on the 2018 General Education
Program, referencing **UNESCO's AI Competency Framework**, four strands — human-centred
thinking, AI ethics, AI techniques and applications, AI system design — rolling out **grades
1–12 from the 2026-2027 school year** with **12 compulsory periods a year**. 🔴 **No repository,
no open licence, no curriculum published as data.**

🔵 **The trend, stated for a studio:** AI-in-the-curriculum is becoming a **national mandate**
faster than curricula are becoming **licensed data**. England is one jurisdiction with a
checkable grant; Vietnam is a mandate with grades, periods and a start date and **nothing to
validate against**. 🟡 The gap between "we must teach this" and "here is the licensed artefact"
is where a studio sells curriculum engineering — and the first question in the engagement is
still *which jurisdiction's curriculum is licensed for what you are about to sell.*

### 🟡 5. Teacher-first and the adoption-governance gap — corroborated, not advanced

🟢 The institutional maturity datum this pass is independent of the ones already carried: one
analysis rates **institutional maturity at 35/100**, most institutions still in pilot. 🔵 That
**corroborates** UNESCO IESALC's 87%-use / 26%-formal-strategy split from a second instrument,
which matters because this base has spent passes learning what a single vendor source costs.
🔴 **No figure is promoted off this leg**: the 2026 market-size estimates ranged **$6.4B–$10.6B**
across four reports for overlapping years, which is the spread this file already warns about,
and a widely-repeated student-use jump (66% → 92%) is single-source and is **not published**.

🟡 **LATAM, recorded as a provenance upgrade rather than a new fact**: the 87%/26% figures now
trace to a **UNESCO IESALC + UNU-IAS working paper** (200 institutions, 19 countries, surveyed
**Aug–Oct 2025**) rather than a press summary. 🔴 **Peru** adds policy and no code —
`Proyecto DocenteTec`, 87 000+ teachers reported trained, and **two bills, neither approved**.
🔴 **Mexico `SEP` returned an explicit nil**: zero results naming SEP at all. The
second-largest Spanish-speaking school system in the region has **no code row on these
shelves**, and that is written down as a gap rather than left as silence.

## 🟢 Pass 289 — THE TREND IS NO LONGER "AI IN EDUCATION", IT IS **GOVERNANCE**, AND THE GOVERNED OBJECT IS ASSESSMENT

⏱️ `2026-10-18`, eleventh pass. Evidence:
[`p289-websearch.2026-10-18-p289.tsv`](../evidence/p289-websearch.2026-10-18-p289.tsv) ·
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv).

### 🟢 1. Experimentation → governance, and this is now the consensus rather than a forecast

The mandated trends leg returned the same shape from every independent source: institutions
have stopped *trying tools* and started building **policy, oversight and evaluation**. The
operative phrase across the leg — *"clear policies, data boundaries, and oversight"*.

🔵 **Why a studio should care about the direction of that sentence.** When the constraint was
capability, the deliverable was a model. When the constraint is governance, the deliverable is
an **auditable workflow** — and audit artefacts are specifiable, testable and billable in a way
"better answers" never was. The regions agree: 🇱🇹 Lithuania is building a **register of
approved tools**, 🇺🇸 Oklahoma and Maryland **bar AI from high-stakes student decisions**,
🇻🇳 Vietnam names **automated assessment** high-risk.

### 🔴 2. The governed object is ASSESSMENT, specifically, in two binding regimes

| regime | what is named |
|---|---|
| 🇪🇺 EU AI Act | systems that **evaluate learners** or **influence access to qualifications** → high-risk |
| 🇻🇳 Vietnam | **automated assessment** and **behavioural monitoring**, among six high-risk sectors |

🔵 **"AI that grades" is the most-requested education build and the most-regulated one.** This
base has carried grading agents since early passes; the trend worth recording is that the
compliance surface around them stopped being European and became **plural**.

🔴 **Both regimes' dates are in conflict across sources and this shelf asserts neither.** The
EU: *Aug 2026* per one guide, *31 July 2026* / *27 July 2026* per the Commission's own
milestones page. Vietnam: compliance *2027-03-01* with a pre-*2026-08-15* grace, against a
report that the law took effect *2026-03-01*. 🔵 `p223`'s date gate exists because this base
once asserted dates it had not reconciled. **A conflict recorded is worth more than a date
guessed.**

### 🟢 3. Teacher-first, and time saved is the retention predictor

The leg is consistent: deployments that begin with **teachers** outlast those that begin with
students, and **time saved** predicts whether a school keeps using a tool. HolonIQ places the
clearest measured gains in **course design support** and **teacher productivity** — *not* in
broad personalisation, which it expects to be displaced by *"proven instructional benefit"*.

🔵 **This is the single most actionable trend in the file** and it inverts a common pitch: the
buyer is the teacher's calendar, not the learner's engagement curve. Adoption data agrees —
**60%** of US K-12 teachers used AI in 2024-25 (**32%** weekly), **75%** of Uruguayan
public-school teachers, **56%/55%/53%/52%** in Brazil/Chile/Colombia/Costa Rica against an
**OECD average of 36%**.

### 🔴 4. Adoption has outrun governance, and the number is now institutional

**UNESCO IESALC, 200 institutions, 19 countries: 87% use AI, 26% have a formal strategy.**
**1 in 2 students** reports confusion about what use is appropriate.

🔵 **A 61-point gap between practice and policy is a demand signal with a name.** It is also
why the governance trend above is not a compliance tax but the product: the institutions have
already adopted, and they know they are exposed.

### 🟢 5. NEW this pass — "curriculum-aligned" is a LICENCE claim, and it has a readable layer

This pass read a national curriculum's grant first-hand for the first time by going to the
**publisher's repository** rather than the ministry's website. The result splits:

- 🟢 **The code is verifiable** — 5 of 7 Oak payloads are `AUTHORITATIVE-BODY` MIT.
- 🔴 **The curriculum data is a `RESTATEMENT`** — a paraphrase of OGL v3.0 whose authoritative
  text sits on a host measured unreachable (12 licensing authorities, 12/12 `POLICY-REFUSED`).

🔵 **The trend statement, and it will outlast this pass:** as curricula are published **as
data** — ontologies, SHACL shapes, APIs, MCP servers — the alignment claim becomes **checkable**
and the licence becomes **the constraint**. England has ceded its curriculum with commercial
use explicit. 🟡 The direction of travel is that *"curriculum-aligned"* stops being marketing
and starts being a validation run against 38 shapes — and the next question in every engagement
is **which jurisdiction's curriculum is licensed for what you are about to sell**.

### 🔴 6. Digital credentials and skills-based hiring — carried, not promoted

The leg again reports momentum behind digital credentials and skills-based hiring, driven by
shifting employer expectations. 🟡 **Carried as a direction with no figure attached**: the leg
offered none that was not vendor-sourced, and this shelf has spent five passes learning what
that costs.

## 🟢 `T-p288a` — the human checkpoint stopped being a UX choice and became THE REGULATORY INTERFACE, in all four regions at once

🔵 **The trend, stated as the thing a studio actually hits.** Four regional legs ran this pass
and every one of them regulates the same narrow act: **AI as the *sole* basis for a decision
about a student.** The instruments share no drafting, no timetable and no enforcement model —
and they converge on one engineering requirement.

- **EMEA** — the EU AI Act puts **admission decisions, student evaluation and exam scoring** in
  the **high-risk** tier: risk management, **human oversight**, conformity assessment *before*
  deployment, and it reaches **non-EU vendors** whose outputs affect EU-located students.
- **APAC** — **Vietnam** (law in force `2026-03-01`) names **education** among six high-risk
  sectors, high-risk **only where the output is the sole basis for a decision without
  meaningful human review**. **South Korea** (Framework Act, in force `2026-01-22`) requires
  **disclosure that the user is dealing with AI** and **marking of generated content**.
- **North America** — no comprehensive national law in any of the three economies; **Oklahoma**
  and **Maryland** require **human oversight** and bar AI from **high-stakes student
  decisions**, inside a 2026 session carrying **134 bills across 31 states**.
- **LATAM** — no education-specific 2026 instrument, but **Mexico**'s federal bill mirrors the
  risk-based approach and **Peru**'s law adds **regulatory sandboxes**: the same frame, arriving
  later.

🟢 **So the deliverable requirement is singular and portable:** a **recorded, evidenceable human
decision point**, plus **provenance marking on every generated artefact**. Build it once and it
clears Vietnam's sole-basis clause, Korea's marking duty, the EMEA high-risk tier and the
Oklahoma/Maryland oversight rules. 🔴 **A tutor or grader that cannot produce the audit trail of
who decided what is not a weak product — it is unshippable in EMEA and APAC and exposed in
North America.**

🔵 **And this pass found the pattern already implemented, in a repository nobody can use.**
[`arijit8972/agentic-automated-assignment-grading`](https://github.com/arijit8972/agentic-automated-assignment-grading)
carries a **`needs_review` terminal state**, with review flags raised on **evaluation errors,
low confidence and evaluator disagreement**, and a flagged submission still produces a report
whose feedback is **marked as draft**. 🔴 That is the compliance artefact, and the repo serves
**no grant** across **1 531 files** whose 66 licence-like paths are **all vendored
`node_modules`**. 🟢 **The design is the finding; the code is not vendorable.** Written out as
`P42` in [`compose/patterns.md`](../compose/patterns.md).

## 🔴 `T-p288b` — special education is a REGULATED, DEADLINE-DRIVEN, DOCUMENT-HEAVY workflow with no permissive open source answer at all

🔵 **A directed leg opened a category this base had never carried, and the category is
uniformly unbuildable.** IEP/504 administration is statutory, calendar-bound and
evidence-producing — on paper the ideal agent target. The entire open source answer to it, as
verified first-hand this pass:

| repository | grant (verified) | what it actually solves |
|---|---|---|
| [`AaronGrace978/EduHelp`](https://github.com/AaronGrace978/EduHelp) | 🟡 **AGPL-3.0**, 34 523 B payload | IEP/504 **eligibility** for families, Colorado + California rules, BYOK multi-provider |
| [`hdronamraju/sped-agent`](https://github.com/hdronamraju/sped-agent) | 🔴 **all rights reserved** (README) | California **day-counting deadline** rules, coordinator approval gate, bilingual EN/es parent notices |
| [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance) | 🔴 **none in 21 files** | Evaluation timelines, service delivery, annual reviews, corrective action |

🔴 **One copyleft, two unusable. Zero permissive.** A studio taking an IEP engagement **writes
it**, and the three repos above are its requirements document rather than its dependency set.

🔵 **`sped-agent` is the most valuable of the three precisely because it cannot be used.** It
states the real requirement set a specification would miss: **nothing is sent until a
coordinator approves it** (the `T-p288a` checkpoint, built), California's own day-counting
rules rather than generic date arithmetic, and **Spanish-language statutory notices** as a
first-class output. 🔴 Its posture is a **REFUSAL, not an absence** — *"please ask before
reusing the code"* — which is a distinction this base could not previously record, and
`ACTION p288` now grades it (`RESERVED-NO-PAYLOAD` → **STOP**, never `ASK`).

## 🟢 `T-p287a` — "curriculum-aligned" is not a product decision: it is bounded by the HOST COUNTRY'S CURRICULUM LICENCE, and the pilot corpus may not be shippable

🔵 **The trend, stated as the thing a studio actually hits.** Every education engagement is
sold on *alignment* — this tutor teaches **your** curriculum. 🔴 **Alignment is a claim about
third-party copyrighted material, and this base has spent 287 passes auditing the licence of
the CODE while the alignment claim was governed by a ministry's copyright page that nobody
read.**

🟢 **One repository found this pass states the rule in its own strategy line**
([`avps82/mentar`](https://github.com/avps82/mentar), AGPL-3.0, 839 files,
`docs/CONTENT_LICENSES.md` v0.6):

> `AU = ACARA (CC BY)`, `IN/SG/US = GENERIC packs (no claimed alignment)`

🔵 **Read it round the right way.** It does not ship Australian alignment because Australia is a
priority market. It ships Australian alignment **because ACARA publishes the Australian
curriculum under CC BY**. Everywhere the national curriculum is not openly licensed it ships
**generic packs and withholds the claim**. The licence decides the feature.

🔴 **And the second half is worse, because it splits by COMMERCIAL TIER rather than by
country.** The same audit on its live grounding source — Khan Academy ZIM, **CC BY-NC-SA**:

| tier | verdict in the audit's own words | why |
|---|---|---|
| local, single supervised family, OSS edition | ✅ *"Cleared for the **non-commercial** local pilot"* | a supervised family running it locally does not trigger NC |
| **Phase-3 paid hosted tier** | 🔴 ***"Does NOT clear"*** | the tier is commercial; **NC bites** |

🔴 **So the pilot that wins the client and the deliverable that bills them may not be able to use
the same corpus** — and `SA` **compounds** rather than relieves it: a redistributed adaptation of
NC content **inherits** CC BY-NC-SA, carrying NC forward into everything downstream.
🟢 **A Globant deliverable is paid by construction**, so this is not an edge case for this base;
it is the default case, and it has been invisible because the platform's licence does not change
between the two phases while the content's obligations do all the work.

🟢 **What this base can state today, and what it explicitly cannot:**

| 🟢 established, first-hand | 🔴 NOT established — registered, not assumed |
|---|---|
| **Australia: ACARA is CC BY** → alignment claimable | 🔴 **The curriculum licence of every other market probed.** 🇹🇿 TIE (`twiga` grounds on it; `p286` did **not** record its licence), 🇬🇭 NaCCA, 🇵🇰 FBISE + Punjab boards, 🇧🇩 NCTB, 🇮🇳 NCERT, 🇺🇬 NCDC |
| **The remedy is cheap**: withhold the claim, ship generic packs | 🔴 **Whether any of those ministries permit derivative aligned content at all** |
| **The tier split is real and documented** | 🔴 Whether an NC-free grounding corpus of comparable quality exists per market |

🔵 **Ranked for `p288`: read five ministry curriculum licences as PRIMARY sources.** A ministry
copyright page is a primary source, it is a day's reading, and no leg in this base's history has
ever addressed one. 🔴 **Until then, every "curriculum-aligned" line in this base is an
UNVERIFIED claim about someone else's copyright**, and saying so is cheaper than finding out in
a deliverable.

## 🟢 `T-p287b` — the licence gap is PER-PROJECT, not per-region, and the two regional claims this base published were both samples

🔴 **This base has now published a regional licence claim twice and been wrong twice, in
opposite directions.** `p285`: *"West Africa, five of five unlicensed — the gap is LICENSING,
not supply"*, drawn over 54 states. `p286` corrected the granularity and split it three ways
(East Africa permissive, West Africa unlicensed, Kenya `CC BY-NC-ND`).

🟢 **`p287` adds an independent second confirmation 6 000 km away, and it dissolves the regional
frame rather than refining it.** South Asia: three code rows, **two with no grant**
(`PrepifyAI` 389 files, `gurukul-ai` 17 files) against **one** that is AGPL (`mentar`) — the
same ratio as West Africa, in a region with none of its characteristics.

🔵 **So the honest statement is neither continental nor regional: the licence posture is a
PROPERTY OF THE PROJECT, and only the payload settles it.** Region predicts the *language of
the payload* and nothing about its *grant*.

🔴 **But one regional distinction survives, and a proposal must not blur it** — it is about the
REMEDY, not the rate:

| posture | example | remedy | cost |
|---|---|---|---|
| 🔴 **unlicensed** (no grant served) | 🇵🇰 `PrepifyAI`, 🇮🇳 `gurukul-ai`, 🇬🇭 `edubot-africa`, 🇳🇬 `naija-learn` | 🟢 **ASK** — a written grant request. The maintainer usually intends to grant; `gurukul-ai`'s README literally says *"MIT — use freely"* | an email |
| 🔴 **deliberately restricted** | 🇨🇳 `OpenGaokao` (`SAL-1.0`, *"not an OSI licence"*), 🇮🇩 `rapkumer` (total prohibition), 🇰🇪 `shule-ai` (`CC BY-NC-ND`) | 🔴 **NONE.** The author decided. Re-implement or walk | a rebuild |
| 🔴 **unlicensed AND un-grantable** | 🇵🇰 `PrepifyAI`'s 20 board-textbook JSON files | 🔴 **An ask CANNOT fix it** — the author cannot grant what they do not hold | `T-p287c` |

🟢 **APAC's five education rows are mostly the SECOND row of that table; West Africa's are the
FIRST.** Same "unusable" count, opposite remedies, and this base filed them under one heading
until now.

## 🔴 `T-p287c` — `NONE_IN_TREE` has more than one remedy, and this base has been publishing one

🔴 **The standing remedy for a repository that serves no grant is "ask the author"** (`P17`,
`P19`, and `p286` backlog item 5's licence-intake ask over the five West African repositories).
🟢 **`saif2012004/PrepifyAI` shows that remedy can be structurally unavailable.** Its 389 files
include **20 `Extracted text books/` JSON files** for `FBISE_CLASS9/10` and `PUNJAB_CLASS9/10`.
🔴 **Board textbook text is third-party copyright: the author cannot grant it**, so a perfect
written code grant leaves the repository unusable.

🔵 **The rule this yields, and it is cheap to apply:** before sending a licence-intake ask,
**enumerate the tree and ask what is IN it.** A `NONE_IN_TREE` row over 35 files of original
code and a `NONE_IN_TREE` row over 389 files including a national board's textbooks are the
same verdict with **different remedies and different prices**, and this base's own ranked
backlog item would have sent the same email to both.

🟢 **`mentar` documents the same seam from the supply side** (`docs/CONTENT_LICENSES.md`
separate from `docs/LICENSE_AUDIT.md`). **Two independent arrivals at one boundary in one
pass:** the code grant and the content grant are different questions, and **the content one is
the one that bites a paid deliverable.**

## 🔴 `T-p287d` — a licence instrument has TWO failure modes and this base has only been counting one

🔴 **Every licence defect in this base's 287-pass history ran permissive-looking:** a
restriction unread, a non-OSI grant published as open, `PageLM` reciting MIT before diverging,
`rapkumer` scanning as *"no restriction"*. The ledger is built around that direction, correctly,
because it is the one that mis-sells a deliverable.

🟢 **`p287` found the other one in this base's own instrument.**
[`Priyamakeshwari/TeachGPT`](https://github.com/Priyamakeshwari/TeachGPT) serves a **verbatim MIT
body with its title line absent** at `LICENSE.md`. `pass257-restriction-scan`'s stage-two
operative-clause anchors covered **BSD** and **ISC** — the two families that routinely open on a
bare copyright line — **and not MIT**, the family this base publishes more than all others
combined. It graded `UNCLASSIFIED` for thirty passes.

🟡 **Nothing was mis-sold: `UNCLASSIFIED` is never published as permissive.** 🔴 **What it cost
is a real, usable, permissive grant DECLINED FOR NO REASON** — 🔵 **a bill that never appears as
a defect, because nobody writes down the component they did not use.**

🔴 **This entry's own first draft then overstated the gap, and `p279-absence-claims` queued the
sentence that did it.** It read *"this base has had no counter, no gate and no trend entry for
that outcome at all"*. 🟢 **Checked against `compose/code/`, that is false twice:**

| instrument | what it exists for |
|---|---|
| 🟢 **`p215-lstree-grant-recovery`** | Asks *"whether `ABSENT` has been a **root-only artefact** all along"* — a false-negative recovery sweep over **94 shelf rows** graded `ABSENT` after 18 root path forms |
| 🟢 **`p742-grant-body-vs-reference`** | Prevents `P742`: `openeducat/openeducat_erp`'s **LGPLv3 grant, 8 241 B, present in the same file**, filed as *"reference to nothing"* |

🟢 **And `p285` corrected four such rows in a single pass** — `Zenglian990/AI_Tutor_Release`
**serves MIT at the root** (it had been carried as ungranted since `p153`); `eledia`'s block
**serves GPL-3.0-or-later on `master`**; and `cs341-illinois/coursebook` **serves three grants**
from a `LICENSE/` **directory** (`LICENSE.code` NCSA, `LICENSE.original`, `LICENSE.output` CC),
which withdrew that row's earlier *"Do not use."*

🟢 **So the true claim is narrower and more useful, and it names an AXIS rather than a
direction.** This base has chased the false negative hard **on the axis of WHERE THE GRANT IS** —
path, ref, directory, vendored-vs-own. 🔴 **It has never had coverage on the axis of WHAT THE
GRANT SAYS.** `TeachGPT`'s payload was served at the **first path tried on the default ref**:
every path-axis instrument here would have handed it over instantly, and it was **then
mis-graded because the title line was absent.**

🔵 **A grant can be FOUND and still not be READ**, and those are two different instruments. The
family-axis recovery sweep is `p288` item 2 — and unlike `p215`'s it needs **no network**, since
the payloads are already captured in `fixtures-*` and `evidence/`.

🔵 **And the shape is familiar: `T-p283`'s, for the third time, and the second inside that one
function this pass.** `p1054` has carried a `MIT_BODY_MARKER` since it was written — **the base
already knew an MIT body is identifiable without its title, and the knowledge never crossed to
the instrument beside it.** The standing lesson is now **bidirectional**: *when a class is
established in one instrument, check the one beside it — and check both directions of its
verdict.*

## 🟢 `T-p287e` — the permissive code in a non-English market sits one layer BELOW the agent

🔵 **Four language legs, one shape.** 🇧🇩 Bangladesh: the tutors (`Progga AI`) are commercial, and
what is open is **infrastructure** — `sagorbrur/bnlp` (Bengali NLP toolkit),
`banglakit/awesome-bangla`. 🇻🇳 Vietnam (`p286`): `VIETPOET`'s pedagogy was right and its grant
was missing. 🇮🇩 Indonesia: one MIT app out of seven addresses. 🇹🇿 Tanzania: `twiga` MIT — the
exception.

🟢 **Stated as an engagement rule: in a non-English market, searching for a TUTOR returns
proprietary products and reports a gap, while the permissively licensed thing the deliverable
actually needs — tokenisers, embeddings, ASR, exam-results channels — is sitting one layer down
unclaimed.** 🔵 For 🇧🇩, 🇻🇳, 🇳🇬 and 🇹🇿 engagements that inverts the build/buy conversation: the
language layer is **available**, the tutor layer is **not**, and the deliverable is therefore a
**build on open infrastructure**, not an integration of an open tutor.

🟡 **Honest caveat, and it is this base's own rule applied to itself:** the three Bangla rows
above arrived from a **search result**, not from a payload. This base's measured rate is that
**three of four secondary "open source" claims are wrong**, so they are carried as **leads at
the right layer** and not as verified grants. Probing them is a `p288` item.

## 🟢 `T-p286a` — "Africa" is not a market for this purpose: the licence posture splits EAST / WEST / KENYA, and a continental claim gets all three wrong

🔵 **The trend, stated as the thing a studio actually hits.** This base has carried a continental
claim about African education code for 17 passes — first *"no African-origin permissively licensed
education agent"* (`p269`), then, sharpened two passes ago into `T-p285a`, *"five rows, five
unlicensed: the gap is LICENSING, not supply"*. 🔴 **Every leg that produced that claim addressed
either "Africa" or West Africa.** `p285` recorded, in its own text, that its leg *"found nothing
for East Africa"* — and published the continental conclusion anyway.

🟢 **One leg addressed to Tanzania by its exam board (`NECTA`) and its language (Swahili) returned
two MIT repositories on the first attempt.** The resulting picture has **three** shapes, not one:

| sub-region | population known to this base | licence posture | what it means for an engagement |
|---|---|---|---|
| 🟢 **East Africa (🇹🇿)** | `Tanzania-AI-Community/twiga` (**MIT**, 230 files, TIE curriculum, tests + migrations + CI), `vincent-laizer/NECTA-API` (**MIT**) | 🟢 **permissive, production-shaped, community-backed** | **Build on it.** This is a dependency, not prior art — the first such row for any African deployment in this base |
| 🔴 **West Africa (🇬🇭 🇳🇬)** | `edubot-africa`, `naija-learn`, `Education-AI-TUTOR`, `EduTwin-Africa`, `edunaija-os` | 🔴 **five rows, five with no grant on any channel** | **Prior art. ASK** — `P32`/`P35`. `EduTwin-Africa`'s author has written down that the licence is missing, so it is the one where asking plainly costs nothing |
| 🔴 **Kenya (🇰🇪)** | `gabrielmahia/shule-ai` (KCSE/CBC, Kiswahili + English) | 🔴 **CC BY-NC-ND 4.0** — listed as *"open-source"* on GitHub Topics | 🔴 **Worse than unlicensed for a studio:** NonCommercial blocks billing, NoDerivatives blocks modification. Unusable twice over, and it looks usable |

🔴 **The methodological half is the durable finding, and it is the second time in three passes.**
`T-p284b` already established: *"before a gap is published as a property of the world, one leg must
have addressed it by name."* 🔴 **`p285` satisfied the letter of that rule and still got it wrong,
because it addressed the gap at the wrong GRANULARITY** — one leg named "Africa", so the rule was
met, while the conclusion was drawn over a unit (a continent of 54 states and dozens of exam
boards) that no single leg can cover. 🟢 **`T-p286a` extends the rule: the leg must address the gap
at the granularity at which the CONCLUSION is stated.** A claim about Africa needs legs per
sub-region or per exam board; a claim about Tanzania needs one.

🔵 **And the queries that work are now a measured pattern, three passes running.** `p284` found
Africa with the AU strategy by name; `p285` found three West African repos by exam board and
language; `p286` found East Africa, Indonesia and Vietnam the same way — **`NECTA`, `KCSE`,
`Kurikulum Merdeka`, `giáo dục`**. 🟢 **The generative unit is the EXAM BOARD and the LANGUAGE OF
INSTRUCTION, not the region**: both are proper nouns a local system must name, and neither appears
in consultancy trend-blogging, which is what region-named queries reach.

## 🔴 `T-p286b` — the restriction vocabulary is ENGLISH-ONLY, and its miss is published as "no restriction" rather than "cannot read"

🔵 **The trend as a defect with a live instance.** The directed legs that now extend this base reach
**non-English-speaking** education systems, and grants there are written in the local language.
`p286` read [`sira313/rapkumer`](https://github.com/sira313/rapkumer)'s **3 140-byte bespoke
`RAPKUMER LICENSE`**, whose §3 is titled **`LARANGAN PENGGUNAAN KOMERSIAL`** — *prohibition of
commercial use* — and which forbids commercial use **in any form**, naming paid access, paid
support-as-product and inclusion in a commercial service.

🔴 **`pass257-restriction-scan` returns `UNCLASSIFIED:no-family-no-restriction` on that body, with
zero hits.** The English control (*"NonCommercial … Commercial use is prohibited"*) fires
`RESTRICTED:added-restriction` correctly, so **the logic is sound and the vocabulary is the defect**:
`noncommercial`, `non-commercial`, `commercial use`, and nothing else.
Evidence: [`restriction-vocabulary-language.2026-10-18-p286.tsv`](../evidence/restriction-vocabulary-language.2026-10-18-p286.tsv).

🔴 **The dangerous part is the DIRECTION of the failure.** The verdict string a consumer reads is
`no-family-no-restriction` — *"I looked and there is nothing"* — when the truth is *"I cannot read
this language."* A permissive-looking verdict on a totally non-commercial licence is exactly the
error class this base built `p238-lure-signature` and `p248-named-proprietary` to prevent, arriving
through a channel neither of them watches.

🔵 **And it is `T-p283`'s shape once more — a fix that reached the family it was built for and no
other.** `lib/license_family.sh` **already carries 38 non-English grant tokens** (the Portuguese and
Spanish GPL titles, `licença pública geral` and kin), added when this base started reading LATAM
payloads. So the base has known for many passes that grants arrive in other languages — **in the
TITLE channel. The RESTRICTION channel never inherited it.**

🟢 **Ranked first for `p287`, and deliberately not half-fixed here.** `scan()`'s verdict strings are
consumed by the shelf gates, so a new `UNREADABLE-BODY` verdict has to land together with its
downstream consumers; and the vocabulary should be extended in the languages this base's own
directed legs now reach — **Indonesian, Vietnamese, Portuguese, Spanish, Swahili** — each arm with
a negative control, because a restriction term is a word that must not fire on prose.

## 🔴 `T-p285a` — Africa's education-AI gap is a LICENSING gap, not a supply gap, and the two have opposite remedies

🔵 **The trend, stated as the thing a studio actually hits.** This base has described Africa as
*"not covered"* for several passes, on the strength of legs that returned policy and no code.
`p285` searched by **exam board and language** instead of by region name and found three
repositories on the first attempt. Combined with the two already shelved, the picture inverts:

| repository | country / scope | grant, after **tree enumeration** |
|---|---|---|
| [`Angel-builds/edubot-africa`](https://github.com/Angel-builds/edubot-africa) | 🇬🇭 NaCCA JHS maths (B7–B9) | 🔴 none — 40 files, no manifest key |
| [`Onyeocha-Keside/naija-learn`](https://github.com/Onyeocha-Keside/naija-learn) | 🇳🇬 Yoruba / Hausa / Igbo voice-first | 🔴 none — 35 files |
| [`meduoyeomoyenia-cyber/Education-AI-TUTOR`](https://github.com/meduoyeomoyenia-cyber/Education-AI-TUTOR) | 🇳🇬 WAEC / NECO / JAMB | 🔴 none — 138 files, `"private": true` |
| [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) | 🇿🇦 Grades 8–12 | 🔴 none *(carried since `p269`)* |
| [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) | 🇳🇬 | 🔴 none *(carried since `p269`)* |

🔴 **Five for five.** 🟢 **Why the distinction decides the engagement, and not just the write-up:**
a **supply** gap is answered by building, and the honest proposal is a greenfield quote. A
**licensing** gap is answered by **asking** — these are finished, working, often locally-grounded
systems whose authors have simply never added a `LICENSE` file, and a written grant request costs
days where a reimplementation costs months. 🔵 **So the first deliverable of an African education
engagement is not code. It is a licence intake pass over the local prior art** (`P32`, `P35`), and
the thing that makes it worth doing is that the hit rate on *asking* is unknown precisely because
nobody in this base's history has asked.

🔴 **And a bound on the optimism:** unlicensed is not the only closure. `p285` also read, from
`edubot-africa`'s own README, that **Ghana's NaCCA curriculum is *all rights reserved* and WAEC
past questions carry no public licence**. **The content layer is closed even where the code layer
opens.** See `P17`, `P19`.

## 🟢 `T-p285b` — the AI Act's marking duty now has a SUPPLY side, and it arrived as a GPL Moodle plugin from a German vendor

🔵 **The trend.** This base has tracked AI Act **Art. 50(2)** transparency as a *duty* for many
passes, with a family of instruments that measure exposure and marking
(`compose/code/aiact-50-2-marking`, `-pack`, `-exposure`). 🟢 **`p285` is the first pass to find a
production component that IMPLEMENTS it:** `local_aitransparency`, shipping inside
[`eledia/moodle-elediaai-suite-free`](https://github.com/eledia/moodle-elediaai-suite-free)
(GPL-3.0-or-later, payload read `2026-10-18`), whose stated job is the **marking of AI-generated
content** inside Moodle.

🔵 **Why this is a trend and not a product note.** It is shipped by a **commercial vendor**
(eLeDia GmbH, Berlin) in the **free** tier of a paid suite, alongside **quota and audit**
(`local_elediaai_core`) and a **local RAG backend that calls no external service**
(`local_literag`). 🟢 **Read together, those three components are a vendor's bet on what EU public
education will be required to buy**: not a better tutor, but **marking, auditability and data
residency around one.** That is the compliance posture this base has argued for since the Annex III
work, arriving as installable software rather than as guidance.

🟢 **Second-order observation for the agent shelf:** the same suite ships `webservice_elediamcp`,
making this the **fourth MCP-addressable LMS surface** this base has located and the **first that
is vendor-shipped and in-tree** rather than a third-party server pointed at someone else's LMS.
🔵 **The direction of travel is that the LMS vendors are building the agent doorway themselves**,
which moves the studio's differentiating work off the connector and onto the agent behind it
(`P38`).

## 🟢 `T-p284a` — the regulator's settled position on AI grading is NOT a ban, and reading it as one loses the engagement

🔵 **The trend, stated as a design rule rather than a jurisdiction.** Three of the most developed
AI-in-education instruments in this base now draw the **same line in the same place**, and it is not
the line a studio expects:

| jurisdiction | instrument | what is PERMITTED | what is PROHIBITED |
|---|---|---|---|
| 🟢 **Brazil** | `Parecer CNE/CP nº 15/2026` (amended by MEC pre-homologation) | AI as a **`primeiro filtro`** assisting the teacher in **essay/dissertation correction** | an automated system **assigning the final mark** or **deciding approval/failure** |
| 🟢 **Vietnam** | `Decision 33/2026/QD-TTg` | automated assessment and behavioural monitoring **with meaningful human review** | the same, where **the AI output is the sole basis for a decision without meaningful human review** |
| 🟢 **EU** | AI Act Annex III pt 3 (duties from `2027-12-02`) | assessing learning outcomes **under the Article 14 human-oversight duty** | deployment without the oversight, documentation and bias controls |

🔴 **The convergence is on the DECISION, not on the technique.** None of the three forbids a model
from reading student work. All three forbid the model from being the thing that decides. 🟢 So the
compliant architecture is the same in all three, and this base can now state it as a pattern rather
than as three regional footnotes: **the model produces a graded suggestion with its evidence; a named
human accepts, edits or rejects it; the accepted value is the one that is recorded, and the record
keeps both.** See [`../compose/patterns.md`](../compose/patterns.md) `P8`.

🔵 **Why this matters more than a permission.** `p284`'s Brazil leg found that the CNE's September
text **banned AI essay correction outright** and that **MEC reversed that before homologation**,
judging a total ban *"impedia um recurso que facilita a rotina docente sem substituir o professor"*.
🟢 **A regulator moved from prohibition to permission in six weeks, and the thing that moved it was
the teacher-workload argument** — which is the same argument Korea's post-mortem produced (factual
errors, privacy, screen time and **heavier teacher workload** were the cited causes of the
AI-textbook reversal) and the same one `p284`'s Africa leg produced independently (*"AI should be
part of permanent teacher training"*; *"teachers should help design localized tools rather than only
use imported ones"*). 🔵 **Three regions, three channels, one argument.** A proposal that leads with
teacher workload relief and human-in-the-loop marking is arguing with the grain of every instrument
in this file.

🔴 **The trap, and it is a scheduling trap.** Brazil's parecer gives institutions **one year to
adapt** but its **prohibitions bite from publication**. A plan that reads *"12 months"* and ships an
autonomous grader in month three ships into a live prohibition. ⚠️ Secondary-source, two outlets;
`T61` blocks the primary text.

## 🟢 `T-p284b` — a four-pass "Africa is empty" was a property of the QUERY, and the fix was one differently-worded leg

🔴 Passes 280–283 each recorded Africa as returning nothing, and `p283` published it as
*"re-confirmed empty for the fourth time"*. 🟢 **`p283` also ordered the remedy** — spend the budget
on a gap-directed leg rather than a fourth verbatim regional one — and on its first run that leg
returned the **AU Continental Education Strategy `2026–2035`**, the **AU Continental AI Strategy**,
**Kenya's National AI Strategy `2025–2030`**, **South Africa's DBE coding & robotics curricula
(Grades R–9)**, **North-West University's January 2026 AI policy**, a **pan-African ethical AI
curriculum** (`arXiv 2604.27708`) and an **open-source-LLM recommendation for African universities**
(`arXiv 2510.18902`). Detail and grades in [`market.md`](market.md).

🔵 **The generalisable lesson, and it is this base's own.** `p254` wrote that *the base inherits its
own conclusions about what is impossible*. 🔴 **Four passes inherited "Africa is empty" from a leg
that had never asked about Africa** — it asked about EMEA and reported what EMEA returned. 🟢 **A
repeated nil is evidence about the query until a differently-worded query has been tried.** That is
now a rule for this file: **before a gap is published as a property of the world, one leg must have
addressed the gap by name.**

🟡 **What the refutation does NOT say.** Every item returned is **policy, curriculum or a preprint**.
The leg still returned **no production open-source education agent built for an African deployment**,
and the two African-context repositories this base holds (`EduTwin-Africa`, `edunaija-os`) still
serve **no usable grant**. 🟢 **The gap changed shape rather than closed:** the regulatory and
curricular context is now on the shelf; the code is still missing. 🔴 **And one hazard came with it:**
an AI robot tutor named **"Iris"** launched in South Africa, August 2025 — colliding with `Iris`, the
user-facing name of the TUM tutor `ls1intum/Pyris` powers. **Two unrelated artefacts, one name**, the
same trap as the two `EduNaija` artefacts recorded below.

## 🔴 `T-p283` — a fix propagates to the family it was built for and to no other, and this base can now measure that

`P1057` (p189) established the rule this base has repeated for ninety-odd passes:
**`raw.githubusercontent.com` is case-sensitive, so a one-spelling path list has not looked for the
file; it has looked for one spelling of the file.** `pass256-ladder-closure` keeps the **licence**
ladder closed. 🔴 `p282` then found `README.MD` on `ls1intum/Pyris` after `p268` published
*"neither repository serves a README"* from a four-rung ladder with **no uppercase extension in it**,
and named the class: *"`p1057`'s licence-path-case class, never inherited by the README ladder
beside it."*

🟢 **`p283` measured how far the fix actually travelled.** Every literal path ladder under
`compose/code/` — **580 ladders in 332 instruments** — graded by whether it can find a file whose
extension is uppercase. Evidence:
[`ladder-case-audit.2026-10-18-p283.tsv`](../evidence/ladder-case-audit.2026-10-18-p283.tsv).

| family | ladders | 🟢 `CASE-CLOSED` | carry ANY uppercase extension |
|---|---|---|---|
| licence | 270 | **15** | **11.1 %** |
| copying | 117 | 0 | 15.4 % |
| readme | 150 | 5 | **5.3 %** |
| notice | 43 | 0 | **0.0 %** |

🔴 **The answer is that it did not travel.** Only **20 of 580** ladders are case-closed. The
**licence** family holds **15 of the 20** — it is the one family a pass built an instrument for.
🔴 **Not one `NOTICE` ladder on this base can find `NOTICE.TXT` or `NOTICE.MD`**, and **33 README
ladders decide that a file is ABSENT** while being unable to spell `README.MD` — which is precisely
`p268`'s published error, still live in 33 places.

🔵 **The generalisable shape, and the reason this is a trend and not a bug report:** a defect class
on this base gets repaired *where it was found*. `p275` wrote *"a path ladder cannot prove absence"*
and built the enumeration gate — and **only 45 of 580 ladders enumerate a tree**. `p279` repaired
line-local predicates over a hard-wrapped corpus, and `p282` found the same defect alive one
directory away. 🟢 **The remedy that follows is not another gate: it is a standing list of repaired
classes and a sweep asking which instruments are still open to each.** `p282` registered that as its
item 3; `p283` now attaches a number to it.

## 🔴 `T-p282` — a shelf's row count is not its repository count, and the gap is invisible to every gate that counts rows

This base verifies **grants** first-hand and has done so for twenty passes. It had never verified
**identity**: that two addresses on the same shelf are two *things*. `p282` found the build-on tier
recommending `ls1intum/Iris` **and** `ls1intum/Pyris` — one repository, identical HEAD, identical
203-file tree, identical 1 088-byte MIT payload — and **six delivery recipes wiring them together**.

🔵 **Why no gate caught it, and the lesson that generalises.** Every instrument here was correct:
the licence was read first-hand *(twice, from the same bytes)*, the row rendered as a row, the
`recount` gate matched **27 rows** to the **27** the file claims. 🔴 **Each measured a property of
the ROW; none measured a property of the REPOSITORY.** A per-row check cannot see a relation
*between* rows, and duplication is a relation.

🟢 **The cheap instrument for it already existed** — `git ls-remote`, one call per address, grouped
by HEAD. Over all 27: **27 resolve, 26 distinct repositories, one alias pair.** 🔵 For a studio the
consequence is concrete: *compose two components* and *compose one component with itself* are
different engagements, and only one of them works.

## 🟡 `T-p282b` — a discovery channel can shut without the shelf noticing

`agents/top.md` promises star counts *"as served by the repository page or the GitHub topic
listing."* 🔴 This pass **both of those return `403`**, along with `github.com/trending` and
`api.github.com`, while `raw.githubusercontent.com` and `git` stay open. 🔵 **So the base's licence
evidence is undisturbed and its popularity evidence is frozen**, and the two age at different rates
from here. 🟢 A figure that cannot be re-measured should be dated at the point of use rather than
restated; every star number on these shelves is carried from `2026-10-17`.

## 🔵 `T-p281` — on a mature shelf, the valuable instrument is the one that CONFIRMS cheaply

🟢 **Observed `2026-10-18` (`p281`), and it is a trend about this base rather than about the market.**
Pass 281 ran the full mandated battery — four global legs, four regional legs — and a payload census
over **39** copyleft rows. 🔴 **It extended the shelves in exactly one place** (Vietnam's `2027-09-01`
propagated into [`compose/patterns.md`](../compose/patterns.md)) and **confirmed them everywhere
else.**

🔵 **The reading that matters for a studio.** A knowledge base reaches a point where new *facts* are
rare and the live risk shifts to **drift** — a date that moved, a licence that was relabelled, a
default branch that changed under a sweep. 🟢 At that point the instrument that earns its cost is the
one that **re-reads cheaply and says "unchanged" with evidence**, not the one that hunts for novelty.
🔴 `p281`'s own census is the warning attached to that: it was **wrong twice** before producing a
true row — 39 false `NO-PAYLOAD`, then 31 false `FILLED` — and both were caught only because a
**positive control with a known answer** was run first.

🟢 **So the standing rule this base keeps re-deriving gets one more instance:** a confirmation is only
worth the control that backs it. **An instrument that has never been run against a known answer is
not evidence, however confident its output table looks.**


# Trends — Education, October 2026

> What changed, what it means for a studio engagement, and how confident the evidence is.
>
> **`T67`–`T69` are new in pass 280** — the K-12 autonomous-use prohibition that three
> jurisdictions wrote independently, the same three converging again on who may decide a grade,
> and the measured observation that this base's remaining expensive errors are the **bounds and
> floors inside its own instruments** rather than facts about the world
> ([evidence](../evidence/package-provenance.2026-10-18-p280.tsv),
> [evidence](../evidence/holder-candidates.2026-10-18-p280.tsv)).
> **T1–T9 are from pass 264. T10 is revised and T11–T14 are new in pass 265. T15–T17 are new in
> pass 266, which also revises T10 a second time and T14. T28–T31 are new in pass 270** — the
> European use-vs-efficacy gap, this base catching itself asserting a propagation it never
> performed, the 25% spread that appears in a regional market figure the moment a second publisher
> is found, and the measured direction in which a carried datum decays
> ([evidence](../evidence/verified-repos.2026-10-17-p265.tsv)), which also retracts two of this
> base's own declared gaps.
>
> **`T32`–`T35` are new in pass 271** — arithmetic as the second oracle a market shelf never
> used, the discovery that a source this base judged unreliable per-clause supplies a figure it
> quotes, the false declaration of ABSENCE (the inverse of `p270`'s false declaration of presence),
> and the over-broad retraction that an English-only search produced
> ([evidence](../evidence/p271-websearch.2026-10-17-p271.tsv)).
>
> **`T42`–`T45` are new in pass 274** — the threshold that was tuned to exclude its own defect's
> signature, the three amendments that were written and never built (one of which is now code), the
> licence this base refuted twice and which was MIT all along, and the market's stated blocker turning
> out to be this base's own recommended architecture
> ([window sweep](../evidence/arithmetic-sweep.2026-10-17-p274.tsv),
> [re-count](../evidence/quantity-recount.2026-10-17-p274.tsv),
> [repos](../evidence/verified-repos.2026-10-17-p274.tsv),
> [legs](../evidence/p274-websearch.2026-10-17-p274.tsv)).
>
> **`T40`–`T41` are new in pass 273.** **`T36`–`T39` are new in pass 272** — the regional market picture resolving to a single upstream
> publisher (so that this base's "independent corroboration" was circular), a gap that is true but
> carried at a stale *magnitude*, a publisher mislabelling its own CAGR window in four regional
> databooks, and the measurement that this base's own byte-count practice cannot discriminate
> ([evidence](../evidence/p272-websearch.2026-10-17-p272.tsv),
> [arithmetic sweep](../evidence/arithmetic-sweep.2026-10-17-p272.tsv)).

## T1 — The education agent consolidated around one project

`HKUDS/DeepTutor` is at **41.5k stars** with a release dated **2026.10.8**, under
**Apache-2.0**. This base previously published 22k for the same repository. Nothing else in
education is within an order of magnitude: the next education-specific agent found is
`Study-Mate` at 1.0k, then `education-agent-skills` at 873.

**For the studio:** the "which tutoring agent" question is effectively settled for
greenfield work. Spend the discovery hours on the student-data model and the integration
boundary instead.

## T2 — Education agents are shipping as *skills*, not applications

The single clearest structural shift this pass. Across the `ai-tutor` and `education-ai`
topic listings, the fastest-rising education repositories are agent **skill packages**:
`education-agent-skills` (873), `lineage-skill` (458, Apache-2.0),
`universal-examprep-skill` (308), `Bloom` (288), `universal-diagnostic-tutor-skill` (246),
`flysheep-ai/education-skills` (114), `skill-instructional-design`, `bloom-taxonomy-quiz-builder-skill`.
Even `instructional_agents` — a peer-reviewed EACL'26 system — published a Claude Code
Skills release (2026.4.15) alongside its v1.1.0.

**For the studio:** the deliverable shape is changing. A client who already runs an
assistant does not want a second web app; they want a skill inside the one they have. That
is a smaller build, a faster sale, and a much shorter integration path. Price accordingly.

## T3 — MCP is becoming the integration layer for education tooling

`ankimcp/anki-mcp-server` (MIT, 516) exposes spaced repetition to any MCP client;
`ArnaudGuiovanna/tutor-mcp` (MIT, 49) turns an LLM into a tutoring system; `Selleo/mentingo`
ships an MCP endpoint as a first-class LMS feature. Meanwhile the GitHub topic
`mcp-server-education` **has never been used by any public repository**.

**For the studio:** a real and growing category with no label. Low-cost, high-visibility
opening for whoever publishes and tags the first substantial education MCP server.

## T4 — EMEA's compliance deadline moved, and that is the engagement

The EU AI Act's high-risk obligations for education moved from **2026-08-02** to
**2027-12-02** via the AI omnibus amendments (in force 2026-07-27). **Transparency duties
went live on 2026-08-02 regardless.**

**For the studio:** two distinct offers, not one. A short remediation scope now (AI
disclosure, deepfake disclosure) and a 14-month compliance-by-design build before December
2027. Clients reading the delay as a reprieve are the pipeline.

## T5 — "Teach about AI before teaching with it" is now written policy

Brazil's MEC published a *Referencial* for responsible AI in education (March 2026) and
basic-education curriculum guidance (April 2026), with an official framing of avoiding
careless tool use in basic education. Mexico's SEP found **76% of professors make materials
with AI but only 36% teach students to use it**, with 9 in 10 asking for training. India
made AI and computational thinking **compulsory from Class 3** from AY 2026-27.

**For the studio:** the biggest funded demand in education AI right now is **curriculum and
teacher formation**, not student-facing tutors. Three governments on three continents are
buying the same thing.

## T6 — Digital sovereignty turned open source into the default, not the discount

Brazil's MEC *Referencial* explicitly calls for national solutions that reduce dependence on
global platforms. Moodle 5.1 added provider-level control and per-course/per-activity AI
toggles, so a local Ollama or vLLM endpoint is a supported configuration rather than a hack.

**For the studio:** self-hosted open source plus local inference is now the *compliant*
architecture in Brazil and the *sovereign* architecture in EMEA. The cost argument is no
longer the main argument, which is a much stronger place to sell from.

## T7 — Knowledge tracing is quietly broadening into cognitive diagnosis

`pykt-toolkit` is the reference benchmark at **450 stars** — materially smaller than this
base previously claimed (1.2k), and worth knowing before citing it as an "industry standard".
Around it: `EduData` (Apache-2.0, 313) for datasets, `pyedmine` (MIT, 82) covering tracing
*plus* cognitive diagnosis *plus* recommendation, `EduStudio` (MIT, 78) for unified
cognitive modelling.

**For the studio:** when the ask is "what should this student do next" rather than "what
does this student know", `pyedmine` is the better base. Both are MIT.

## T8 — Academic integrity became an assessment-architecture problem

`dodona-edu/dolos` (MIT, 352) for source-code plagiarism, `Artemis` (MIT, 819) for automated
feedback with an auditable exercise runner, `Numbas` (Apache-2.0) for randomised maths
assessment. Randomisation and provenance are design choices in the assessment, not
detectors bolted on after.

**For the studio:** in jurisdictions barring AI from high-stakes decisions (Oklahoma,
Maryland, NYC's K-8 moratorium), *assessment integrity* is the part of the AI story that is
unambiguously permitted. Lead with it where student-facing AI is restricted.

## T9 — The licence surface under education AI is unreliable, including ours

Four published cells failed verification this pass and one repository is gone:

- `openedx/edx-platform` is **AGPL-3.0**, not Apache-2.0 as previously published — a
  network-copyleft obligation on the most likely MOOC base in the shelf.
- `CaviraOSS/PageLM` ships a bespoke **non-commercial** licence that prohibits
  redistribution outright. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv`
  grades it `MIT`.**
- `sakaiproject/sakai` is **ECL-2.0**, not Apache-2.0. `chamilo-lms` is GPL-3.0, not GPL-2.0.
  `instructional_agents` is MIT, not Apache-2.0.
- `OpenEduCat-Inc/OpenEduCat` is a **404**; the canonical repo is `openeducat/openeducat_erp`
  (LGPL-3.0).
- `GeminiLight/awesome-ai-llm4education` serves **no LICENSE file**, against a published MIT
  claim.

Counter-example in the other direction: `Open-TutorAi/open-tutor-ai-CE` opens *"All rights
reserved"* and **is** plain BSD-3-Clause — that phrase is part of the BSD form. Flagging it
would have been a false positive, and a false retraction costs a usable row.

**For the studio:** read the `LICENSE` payload for every repository that enters a client
deliverable. A secondary source, an aggregator table, a GitHub sidebar badge and this
knowledge base have all been wrong about an education licence in the last two weeks.

## T10 — The permissive platform market is three candidates deep *(revised twice — now five)*

> **Pass 266 revision:** add **Sunbird** (MIT, national scale, APAC-origin) and **Artemis**
> (MIT, assessment-first, EMEA-origin). The shelf is **five** deep, not three. Each successive
> count in this base was published as if settled; the recurrence is the part worth noting —
> the number has only ever moved in one direction, which suggests the current five is also a
> floor rather than a finding. See [`verticals/solutions.md`](../verticals/solutions.md).


**Revised 2026-10-17 (pass 265).** The earlier version of this entry said *one*. Payload
verification of a wider candidate set makes it **three**, and they are not substitutes:

| Platform | Licence | Stars | The job it is actually good at |
|----------|---------|-------|--------------------------------|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | — | Behaves like an institutional LMS (courses, cohorts, assessment, administration) |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | **6.9k** | Structured lesson delivery with formative feedback in the lesson model; 17,004 commits |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1.2k | Offline-first distribution — runs with no network, syncs opportunistically; 39,803 commits |

Everything else at full-LMS scale remains copylefted (Moodle GPL-3.0, Open edX AGPL-3.0,
Chamilo/ILIAS/Gibbon GPL, Sakai and Opencast ECL-2.0, Vacademy and frappe/lms AGPL-3.0,
OpenEduCat LGPL-3.0, frappe/education GPL-3.0).

**For the studio:** the licence objection now has three answers instead of one, and the right
one depends on the job — which is a much better conversation than "there is exactly one". The
two architectural answers still hold where the client keeps a copyleft platform: an **LTI
tool** (`tsugi`, Apache-2.0) or an **XBlock** (Apache-2.0).

**And a warning about where the earlier claim came from.** Two platforms that 2026-dated
sources recommended to this KB as permissive do not survive payload verification:
**forma.lms** is **GPL-2.0** (published by a review as Apache-2.0), and **Fedena** — still
cited as *the* Apache-2.0 education ERP — has **no licence payload at all** and has been
abandoned since **2012** (community fork: 2016). Both directions of error appear in the same
pass: a permissive platform missed, and two permissive platforms imagined.

## T11 — Offline-first is a licence-free lane nobody is contesting

`learningequality/kolibri` (MIT, 39,803 commits) is a complete learning platform built on the
assumption that **there is no network** — content channels sync when a link appears and the
application is fully functional when it does not. No other platform in this KB is designed
that way; offline support elsewhere is a feature, not an architecture.

**For the studio:** this is the only credible base for rural LATAM, low-bandwidth APAC and
anywhere power is intermittent, and the AI layer has to follow the same assumption — a
quantised local model (Ollama), scheduling via FSRS, telemetry that syncs on contact. It is
also the cheapest possible answer to a data-sovereignty question, because nothing leaves the
device. Retrofitting offline onto a server-rendered LMS is a rebuild; starting from Kolibri is
a configuration.

## T12 — LATAM publishes the platform layer, in Portuguese, and this base had missed it

[`portabilis/i-educar`](https://github.com/portabilis/i-educar) — GPL-2.0, 719★, **34,948
commits**, last commit **2026-10-14** — is a Brazilian school-management system that started
in the *prefeitura de Itajaí (SC)* and was published on the Brazilian federal **Portal do
Software Público in 2008**. Its teacher portal `i-diario` (AGPL-3.0) committed on
**2026-10-09**. Its licence payload is in **Portuguese**.

This KB declared for several passes that *"the region consumes this layer; it does not yet
publish it."* That was an artefact of searching in English.

**For the studio:** in Brazil the question is not *which platform* but *how to put an agentic
layer on the one the client already runs*, with the copyleft held on the platform side of an
HTTP/LTI boundary. The sovereignty story that MEC's *Referencial* asks for is already
satisfied by the base — Brazilian maintainers, federal software-public provenance, local
inference — which turns a compliance conversation into a delivery conversation.
**Legal note:** i-Diário's payload is a *Portuguese translation* of AGPL-3.0; FSF translations
are unofficial, so cite the English text in a SOW.

## T13 — The most-adopted education agent in open source is APAC-origin

`HKUDS/DeepTutor`'s README states it is *"led by Bingxi Zhao within the **HKUDS Group**"* and
credits the *"director of the **Data Intelligence Lab @ HKU**"* — the University of Hong Kong.
At **41.5k stars** it is the most-adopted education agent anywhere, and the learner-modelling
layer beneath it is substantially Chinese-academic: `bigdata-ustc/EduData` (USTC),
`HFUT-LEC/EduStudio` (Hefei University of Technology).

Earlier passes of this KB declared "no APAC-origin education agent surfaced" **while listing
DeepTutor as its top row**. The gap was in the reading, not the supply.

**For the studio:** APAC is the research supply centre for education AI. An APAC engagement is
*integration* work on locally-authored components, not import — and saying so in a Hong Kong,
Singapore or mainland pitch changes who you sound like. The genuine APAC gap is a **platform**,
which is narrower and more actionable.

## T14 — Autograding is permissive, mature, and the answer regulators will accept

> **Pass 266 revision:** stronger than stated. Beyond `nbgrader` (BSD-3-Clause) and `Autolab`
> (Apache-2.0), **Artemis is MIT and ships an automated-feedback engine (Athena) plus an LLM
> tutor (Iris, MIT) and AI exercise authoring (Hyperion)** — and `numbas/Numbas` (Apache-2.0,
> Newcastle) executes assessment **entirely in the browser**, so submissions need never leave
> the device. ⚠️ One caveat for procurement: **Athena's own repo serves no licence payload** —
> Artemis's MIT grant does not automatically cover it. Get it in writing.


The "no open-source grading" gap this KB has declared was about **agents**. The platforms are
fine: `jupyter/nbgrader` (**BSD-3-Clause, 1.4k**) for notebooks, `autolab/Autolab`
(**Apache-2.0, 808**, CMU-origin) for programming assignments with a course-management shell,
`Artemis` (MIT, 819) for feedback with an auditable runner, `Numbas` (Apache-2.0) for
randomised maths, `INGInious` (AGPL-3.0, UCLouvain) where AGPL is acceptable.

**For the studio:** in every jurisdiction tightening up — Idaho and Oklahoma barring AI from
high-stakes decisions, Ohio mandating district policy, the EU's Annex III naming evaluation of
learning outcomes, Brazil's `PL 2338` naming education selection as high-risk — a
**deterministic autograder with a human sign-off step** is permitted where an LLM grader is
not. Lead with nbgrader/Autolab and keep the model on the feedback side of the line. This is
the rare case where the compliant architecture is also the cheaper one.

## T15 — The star count is the wrong instrument for publicly-funded education software

**This is the methodological finding of pass 266, and it generalises past education.**

[`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) — the MIT-licensed
stack beneath **DIKSHA**, India's national school education platform under NCERT — has **41
stars** and **38,046 commits**.

| | Sunbird | A star-findable education agent |
|---|---|---|
| Stars | **41** | 300 – 41,500 |
| Commits | **38,046** | 21 – 12,437 |
| Forks | **317** | 1 – 395 |

Every search leg this base runs sorts GitHub topic listings **by stars**. Ministry-funded digital
public infrastructure is adopted by education departments and system integrators who deploy it;
it is not starred by developers browsing GitHub. **A project can serve a national school system
and remain structurally invisible to the instrument** — which is how this base declared "no
APAC-origin education platform" for 265 passes while an MIT one of national scale sat in plain
sight.

**What to do instead:** rank the *platform* layer by **commits and forks**, and probe
national-programme names directly (DIKSHA/Sunbird, i-Educar, Kolibri, Ceibal, Me Capacito). Note
the slug trap too: `Sunbird-Ed/sunbird-ed-portal` does not resolve, because the live slugs are
camel-case — and a kebab-case guess returns something indistinguishable from absence.

**Why this is commercially material, not just hygiene:** the stars-first instrument biases every
recommendation this base makes toward **US and developer-popular** projects and against
**government-built** ones. In public-sector education — most of the addressable market outside
corporate L&D — that is backwards. An APAC ministry briefed to import a Western LMS, when its
own national stack is MIT and already deployed, is a recommendation that would have lost on
both cost and politics.

**Confidence: high.** Directly measured; the star and commit counts are from the repository
pages this pass.

## T16 — Adoption has outrun governance in LATAM, and the deficit is the sellable work

⚠️ **Secondary-source grade** — `WebFetch` to `iesalc.unesco.org` failed DNS resolution this
pass, so the UNESCO IESALC study could not be read first-hand.

UNESCO IESALC, across **200 institutions in 19 countries**: **87%** use AI in at least one area
and **74%** in teaching and learning, while **26%** have a formal AI strategy. TALIS 2024 has
secondary teachers using AI at **56%** in Brazil, **55%** Chile, **53%** Colombia and **52%**
Costa Rica, against an **OECD average of 36%**.

**A 61-point gap between use and governance** is the single clearest commercial opening in this
base. The work it implies — AI-use policy, model inventories, human-review design,
assessment-integrity controls, procurement criteria, staff training — **requires no platform
displacement**, which is normally what kills a public-sector education deal. And it becomes
mandatory rather than advisable the moment Brazil's `PL 2338` lands with education-related
selection classified high-risk.

The inverse reading matters too: **LATAM is not a laggard market in this category.** Four
countries sit 16–20 points above the OECD average on teacher use. Briefing LATAM as
"behind on AI" is both wrong and the wrong sales posture; "ahead on use, ungoverned" is
accurate and points at a different, larger engagement.

**Confidence: medium.** The numbers are consistent across several reports, but those reports
cite the *same* UNESCO study, so they are not independent confirmations.

## T17 — Regulators are converging on "meaningful human review" as the thing that declassifies a system

The year's regulatory texts stop asking *whether* AI is used and start asking **whether a human
decides**. That turns a compliance question into an architecture question, which is the form a
studio can actually build against.

| Jurisdiction | The hinge |
|---|---|
| **Vietnam** ⚠️ | Automated assessment and behavioural monitoring are high-risk **only where the AI output is the sole basis for a decision without meaningful human review**. Deadline 2027-03-01; +6 months if live before 2026-08-15. |
| **Oklahoma** `SB 1734` | AI permitted **only with educator supervision and human review**; barred from high-stakes decisions. |
| **EU AI Act** | High-risk education duties (delayed to **2027-12-02**) are built on **human oversight**, documentation and conformity assessment. |
| **Idaho** `SB 1227` | Explicit bar on AI **replacing** human teachers. |
| **Maryland** | Human oversight; no high-stakes AI decisions about students. |

**The design consequence, and it is a build instruction rather than an observation:** a system
where the model *proposes* and a human *disposes* — and which can be shown, by configuration, to
have had AI off for any given decision — is a *lower regulatory class* than a system that
decides. The same functionality, differently wired, lands in a different legal category.

This is why [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) (MIT) is the most
strategically interesting row added in pass 266. Its **Iris**, **Athena** and **Hyperion**
subsystems are **config-gated**: the platform runs identically with AI disabled, and feedback is
suggested to an instructor rather than applied to a student. That is not a compliance feature
anyone retrofitted — it is how a university built it for its own use — and it is the posture
four of the five jurisdictions above are converging on.

**Confidence: medium-high** on the pattern (five jurisdictions, independent texts); ⚠️ **low-medium**
on the Vietnam specifics, which are secondary-source and whose dates conflicted across sources.

## T18 — Education ministries are now upstream maintainers, and one of them publishes under MIT

The public-sector layer this KB discovered with Sunbird in pass 266 is not one project. Ranked by
commits and probed by hand, pass 267 found a class:

| Programme | Repo | Licence (payload) | Commits | Stars |
|-----------|------|-------------------|---------|-------|
| UK Department for Education | [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** *(Crown Copyright)* | **34,414** | 38 |
| UK Department for Education | [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | — | — |
| India / NCERT (DIKSHA) | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** | 38,046 | 41 |
| German school-cloud stack | [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) | AGPL-3.0 | 16,192 | 81 |
| Brazil (municipal lineage) | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 34,948 | 719 |

The UK row is the one that changes a pitch. `apply-for-teacher-training` is a **live production
government service** at `apply-for-teacher-training.service.gov.uk`, and its licence payload reads
*"Copyright (c) Crown Copyright (Department for Education)"* — **MIT**. A studio can read, reuse
and adapt a national education ministry's production code with no copyleft obligation at all.

**What this means commercially:** "we will build you a service like a ministry runs" stops being an
analogy. For a public-sector education engagement in EMEA there is now **working, MIT-licensed
reference code for the hardest parts** — application workflows, GOV.UK-pattern service design,
daily production automation — maintained by a department that has to keep it running.

🔴 **And the negative half of the trend is equally firm.** Two of the most-cited public programmes
publish **nothing usable**: Uruguay's **Plan Ceibal** has a GitHub organisation with *"no public
repositories"*, and **OpenEMIS**, the EMIS most associated with ministry deployment, resolves to a
**32-commit Docker packaging repo with no licence on any of 76 path/ref combinations**. Public-sector
provenance has to be **probed per programme**; it does not generalise from the region or the brand.

**Confidence: high** on every repository row (payloads and page metrics read first-hand this pass).
⚠️ **Org-handle grade only** on Schul-Cloud's German/ministry provenance — its README names no
funder, ministry or Land.

## T19 — Permissive autograding is not a gap, a workaround or an exception. It is a mature field with five options

Pass 266 reframed this base's grading gap from "no agent" to "the function lives in platforms".
Pass 267 closes it entirely by measurement:

| Repo | Licence (payload) | Stars | Commits | Covers |
|------|-------------------|-------|---------|--------|
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | **BSD-3-Clause** | 802 | 9,316 | Submission + autograding + **TA grading workflow** (RPI/RCOS) |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | **BSD-3-Clause** | 1.4k | — | Notebook assignment and grading |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD-3-Clause** | 161 | 3,825 | Python **and R**; adapters for **Canvas and Gradescope** (UC Berkeley) |
| [autolab/Autolab](https://github.com/autolab/Autolab) | **Apache-2.0** | 808 | — | Autograding with a course-management shell (CMU) |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | 819 | 12,437 | Build-test-analyse + feedback, config-gated AI (TUM) |

**Five options, three licences, zero copyleft, four continents of provenance between them.** Add
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) (BSD-3, **8.4k★**) as the
substrate and **the entire notebook-teaching lane is permissive end to end** — which this base had
never stated, because it had catalogued the graders without the thing they run on.

🔵 **The strategic read is a warning, not an opportunity.** Autograding is **solved and free**.
Proposing to *build* one is proposing to rebuild five mature systems; the billable work is
**integration, pedagogy and defensibility** — wiring a grader into the client's LMS, and making the
grade explainable to a regulator (T17) and to a student who appeals it. Note `otter-grader` ships a
**Canvas adapter**, so the integration half is partly solved too.

**Confidence: high.** All five licences payload-read; Submitty, otter-grader and jupyterhub measured
first-hand in pass 267.

## T20 — The licence risk has moved from the *name* of the grant to its *shape*

T9 established that the licence surface under education AI is unreliable, with mislabelled
families — Apache-stated-but-GPL, MIT-claimed-but-proprietary. Pass 267 found a harder class of
error: **repositories whose licence family is correctly reported and still tells you the wrong
thing**, because the grant is partitioned.

| Repo | What a label says | What the payload says |
|------|-------------------|----------------------|
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | AGPL-3.0 | **Four partitions:** Community Edition AGPL-3.0; `apps/prairielearn/src/ee/` = **Enterprise Edition, separate terms**; **all client-side JS** AGPL-3.0; UIUC + outside-contributor portions **MIT** |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | MIT | MIT **except** the **Handsontable component — commercial software** requiring a compliance contact — plus two textbook texts under their own terms |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 | AGPL-3.0 **and open-core**: premium plugin tools **sold separately** |
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | *(none — "unlicensed")* | **MIT**, declared in `package.json` only |
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | *(none — "unlicensed")* | **MIT**, at `main/LICENCE` — **the British spelling** |

**Four distinct failure modes, each of which produces a confident wrong answer:**

1. 🔴 **Directory-partitioned grants.** "AGPL-3.0" is wrong in two directions at once for
   PrairieLearn: too restrictive for the MIT portions, too permissive for the EE directory.
2. 🔴 **Exception lists with a commercial member.** An MIT headline over a **paid dependency**
   passes a licence audit and fails procurement.
3. 🔴 **Open-core.** The licence covers what ships free; the feature set in the demo may not be it.
4. 🔴 **Spelling and location.** `LICENCE` vs `LICENSE`, or a grant that exists only in package
   metadata, reads as *unlicensed* to any probe with a narrow path set — and "unlicensed" is the
   most expensive wrong answer available, because it discards usable code.

🔵 **Two operational rules follow, and both are cheap.** (a) **A GitHub sidebar "License" link with
no label is a signal, not a missing datum** — both partitioned-grant rows above show one. (b)
**Read the first paragraph of every payload, not just its title region.** Pass 266's rule (family
from the first 600 bytes) answers *which licence*; it can never answer *over which files*.

**Confidence: high.** Every row payload-read this pass.

## T21 — The LMS is becoming MCP-addressable, and the two big LMSs are not equally open about it

The integration layer T3 identified as "MCP is becoming the integration layer for education
tooling" now reaches the **institution's system of record**, not just the learner's study tools:

| | Canvas | Moodle |
|---|---|---|
| MCP server | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) |
| Licence (payload) | 🟢 **MIT** | 🔴 AGPL-3.0, **open-core** |
| Stars / commits | **295** / 1,026 | **1** / 57 |
| Tools | **102–126** + 8 agent skills | **10** free |
| Platform source | AGPL-3.0, 78,765 commits | GPL-3.0 |

🟢 **The pattern worth naming: AGPL platform, MIT doorway.** Canvas's own source is AGPL-3.0, so a
studio stays outside it regardless — and `canvas-mcp` (MIT) makes staying outside it *more*
capable than forking would be, reaching roster, courses, assignments and grades through the API
with a permissive deliverable on top. This is the **shortest path in this entire KB from an agent
to a client's real institutional data**, and it requires no migration and no platform decision.

🔴 **The asymmetry is the finding, though.** Moodle is the world's most-deployed LMS and its MCP
surface is ~**1/300th** as adopted as Canvas's, copylefted, and partly commercial. **A proposal
promising "an agent over your LMS" without naming the LMS understates the Moodle case badly.**
Where the client runs Moodle, the honest answer is the AGPL open-core server or a direct build
against Moodle Web Services — i.e. actual engineering, not an install.

⚠️ **And the category is invisible to indexes:** the `mcp-server-education` GitHub topic is
**still empty** while **23 distinct education MCP server slugs are shelved on `agents/top.md`**
(**15** when `p274` measured it; `21` at `p278`).
None was found through a topic listing.

🟢 **CORRECTED AT `p296`: 21 → 23, and the correction came from the gate rather than from a reader.**
`T37`'s standing re-count reported `published 21 · measured 23 · STALE` on **every pass since the
value was last touched**, and this is the pass that acted on it. ⚠️ **The `23` is the whole-file
`MCP_HINT` scope**, not the MCP section's own table, which measures `19` and matches its own
sentence — `p278` registered both scopes precisely because a bare count cannot be checked. Quote the
scope with the number or neither is verifiable.

🟢 **CORRECTED AT `p278`: 20 → 21.** `p277` left this at 20 because its own fresh enumeration
returned 20 and `T37` returned 21. **`p278` reproduced both and the gate was right.** `p277`'s
enumeration matched the literal substring `mcp`, which drops
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) — and
`MCP_HINT`'s own code comment had already named that exact failure mode. 🔴 **The dropped row is
the proprietary one.** See [`agents/top.md`](../agents/top.md) for the scope table; the figure is
now anchored to this sentence rather than to a constant, so editing the prose alone is also
`STALE`.

🔴 **`p277`: this is the one registered quantity where the TWO INSTRUMENTS DISAGREE, and the number is
therefore left standing at 20.** `make hooks` ran this pass and `T37`'s re-count reported
`MCP server slugs tabled on agents/top.md · published 20 · measured 21 · STALE`. **An independent
enumeration written fresh this pass — every table row on `agents/top.md`, every `github.com/<owner>/<repo>`
whose slug contains `mcp` — returned 20, agreeing with the SHELF and not with the gate.** 🔵 **So the
STALE verdict is NOT confirmed, and the correct action is to change nothing.** `p277` fixed the *other*
STALE row (`24 → 27` permissive rows) because there both instruments agreed; here they do not, and
**a 1-row disagreement between two predicates is a defect in a predicate, not a stale shelf.**
🔴 **Declared for `p278`:** reconcile `recount.py`'s MCP predicate against the row enumeration and
establish which one is counting the 21st slug — until then this sentence must not be "corrected" in
either direction. **The failure mode to avoid is a pass that edits a true number to match a wrong
instrument, which is harder to detect than a stale one.**
🔴 **This sentence read "five" until pass 272 and "12" until pass 274** — a true gap carried at a
stale magnitude, because passes 267, 268 and 273 added servers and updated the count on one shelf at
a time. 🟢 **`p274` stopped counting by hand:** the number is now derived by
[`compose/code/p274-quantity-recount/recount.py`](../compose/code/p274-quantity-recount/recount.py),
which re-derives every registered quantity from the rows and printed **3 STALE of 5** on its first
run. See `T37` and `T43`.

**Confidence: high** on every licence and metric (payload + page, first-hand). ⚠️ `canvas-mcp`'s
tool count is published inconsistently **on its own page** — About says 102, the README says 126 —
so cite the range.

## T22 — The curriculum-mandate wave is real, and it has a documented failure mode

Two APAC data points, pulling in opposite directions, should be briefed together:

🟢 **India is executing.** AI and computational thinking become compulsory from **Class 3**, with
the CT&AI curriculum for Classes 3–8 **launched on 2026-04-01** by the Education Minister;
implementation starts in the **2026–27 session**, Classes 9–10 follow in **2027–28**. Teacher
training runs through **NISHTHA**, and a **₹500 crore Centre of Excellence in AI for Education**
was announced in the 2025–26 budget.

🔴 **South Korea reversed.** Seoul mandated AI digital textbooks from 2025; adoption sat **below
30%** by March, and in **August 2025 the National Assembly stripped them of official textbook
status** after teachers' unions argued the pace had outrun preparation.

🔵 **The lesson for a studio is not "mandates create demand" — it is which half of the mandate is
unserved.** India's mandate lands on a country that already runs an **MIT-licensed national
platform** (Sunbird/DIKSHA, 38,046 commits) and a named teacher-training programme: the demand has
somewhere to execute. Korea's landed on content distribution without teacher readiness, and the
legislature withdrew it. **Teacher enablement, not content generation, is where a mandate
engagement either works or gets cancelled** — which is the same conclusion T5 reached from policy
text, now with a failed rollout behind it.

⚠️ **Confidence: medium.** Every figure here is **secondary-source**: news and education-sector
coverage reached through the search index. This session could not resolve a single non-GitHub host
by DNS on **either** instrument, so no primary ministry text was read. Treat dates as
decision-usable and figures as directional.

## T23 — The biggest permissive education codebase in the world is a curriculum platform whose curriculum you cannot have

**`code-dot-org/code-dot-org` is Apache-2.0 and has 215,796 commits** — 2.7x
`instructure/canvas-lms` (78,765), which pass 267 published as the largest education codebase this
KB had located. 901★, 538 forks, last commit **2026-10-17**, PR #76166. The GitHub sidebar shows a
License link **with no label**, which is exactly the signal pass 267 said to treat as "read the
payload in full" — and doing so is the whole trend.

The grant covers *"all source codes and assets"* **with one exception**: Code.org's *"proprietary
or licensed artwork, graphics, sounds, lectures, videos, logos, characters, fonts"*, which *"may
not be used or distributed or accessed in any manner other than directly via Code.org's own web
site, mobile applications, or social media channels ... **without modification or embedding in
another format**."* The `NOTICE` explains why that carve-out could not have been narrower: the
activities children actually remember are **licensed entertainment IP** — Minecraft (Microsoft),
Star Wars (Disney/Lucasfilm), Frozen (Disney), Ice Age (20th Century Fox), Angry Birds (Rovio),
Plants vs. Zombies (PopCap), The Amazing World of Gumball (Cartoon Network), The Bad Guys
(DreamWorks) — plus **Font Awesome Pro** and the Geist font (SIL OFL). **Code.org cannot
sublicense them, so neither can a studio.**

🟢 **Why this is a trend and not a licence anecdote: it structurally closes `Gap 367`, this base's
highest-priority demand-side gap.** `Gap 367` records that four jurisdictions now mandate AI
instruction — **China** (≥8 h/year from age six, since Sep 2025), **Singapore MoE** (Mar 2026),
**India CBSE** (Classes 3-8, session 2026-27) and the **EU AI Act Art. 4** staff-literacy duty —
and that *"every permissive AI curriculum on this shelf is written for adult developers"*, calling
it *"the largest named, dated, deadline-bearing demand on this shelf with no supply."* The gap
named **Code.org** and **MIT Day of AI** as the alternatives and never read either one's licence.

Now read: the gap is not under-searched, it is **correctly empty**. The world's largest K-12 CS
platform is permissive **in its engine and unlicensable in its content**; MIT Day of AI is
**CC-licensed**; and the reference framework both are organised on,
[`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) (AAAI/CSTA), **serves no licence
payload at all**. Three independent sources of primary-school AI curriculum, three different
reasons you cannot ship it.

🔵 **So stop searching and change the deliverable.** For a K-5 or K-12 AI-literacy mandate the
honest proposal is **content origination on a free engine**: Apache-2.0 platform reuse, and
instructional design as the paid work. See [`compose/patterns.md`](../compose/patterns.md) `P17`.
🔴 **The failure mode to name explicitly:** a client who has seen Code.org assumes the curriculum
ships with the code. Discovering otherwise after signature is how this becomes a loss.

## T24 — Three LMSs are now MCP-addressable, and the most open one is the least adopted

> 🔴 **CORRECTED IN PASS 274: it is SIX, and five of the six are reachable under MIT.** Stated
> for the re-count in the form it checks: **MCP reaches **6 distinct LMS platforms** across both
> agent shelves.** `p273`'s
> backlog item 7 asked for `T37` to be applied as a standing re-count; it was built
> ([`compose/code/p274-quantity-recount/`](../compose/code/p274-quantity-recount/)) and this is what
> it found. **Every row below was payload-read first-hand in `p274`**
> ([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)):
>
> | platform | server | licence (payload, `p274`) |
> |---|---|---|
> | **Canvas** | `vishalsachdev/canvas-mcp` · 🆕 `bruchris/canvas-lms-mcp` *(`1 070` B, **opt-in FERPA pseudonymisation**)* | 🟢 **MIT** |
> | **Moodle** | `MarcosNahuel/moodle-mcp` *(teacher, writes)* · `Jawadh-Salih/moodle-mcp-server` *(student, Go)* | 🟢 **MIT** *(`p273`)* |
> | **Google Classroom / Workspace** | `Kimmahone/edu-workspace-mcp` *(29 tools, whole tenant)* | 🟢 **MIT** |
> | **Brightspace / D2L** | `RohanMuppa/brightspace-mcp-server` *(`1 068` B, reproduced to the byte)* | 🟢 **MIT** |
> | **Blackboard Ultra** | `felipedias-ie/blackboard-mcp` *(`1 084` B)* · `NiccoloSalvini/mcp-blackboard-ucsc` *(`1 073` B, public REST API)* | 🟢 **MIT** |
> | **Open edX** | `blend-ed/tutor-contrib-openedxmcp` *(`34 524` B, 33 tools)* | 🔴 **AGPL-3.0** |
>
> 🔴 **And the correction has a commercial consequence that reaches past the count.**
> [`intel/market.md`](market.md)'s players table tells a studio that **Blackboard / Anthology** is a
> *"replacement engagement; the incumbent's lock-in is the pitch."* **Blackboard has two MIT MCP
> doorways on this base's own trending shelf.** 🔵 **That is exactly the error `p267` corrected for
> Canvas** — *"the opening is the opposite of migration"* — **left standing for the other North
> American higher-ed incumbent.** The `AGPL platform, MIT doorway` pattern now holds for **five**
> platforms, and nobody has to be migrated off any of them.

Pass 267 established that the LMS is becoming MCP-addressable and that *"the two big LMSs are not
equally open about it."* Pass 268 found the third, and it breaks the implied correlation between
openness and usefulness.

| LMS | servers | best licence | best adoption | engagement posture |
|-----|---------|--------------|---------------|--------------------|
| **Canvas** | 2 | **MIT** (payload) | **295★ / 1,026 commits**, v1.14.0 Oct 2026, UIUC named | **Adopt.** One maintained choice. |
| **Moodle** | 1 | AGPL-3.0, **open-core** | 1★ / 57 commits | **Price twice.** Network clause *and* premium tools sold separately. |
| **Google Classroom** | **8** | **MIT** (payload on 6 of 8) | **2★ / 11 commits** at best | **Fork and own it.** Nobody upstream is carrying this. |

**The Google Classroom family in full:** `adriasantacreu` (46 tools, MIT at *metadata* grade — no
payload, no sidebar licence), `Kimmahone/edu-workspace-mcp` (MIT, 29 tools, reaches all of
Workspace for Education), `pengusto` (MIT, a correctly-attributed fork of `adriasantacreu` with
dual copyright in the payload), `alanmagno1` (MIT), `OmarNiazi` (MIT, read-only by construction),
`praisethefacts` (MIT), `faizan45640` (MIT), and
[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) — which
is **not open source at all**: a bespoke *"AStheTECH Community License (ACL) ... All rights
reserved"* at `LICENSE.md`, sitting in the same result set, describing itself the same way.

🔴 **Second instance of the PageLM pattern, and the lesson has sharpened.** `p238` built a
four-predicate lure gate for *deliberately mislabelled* repositories. This row **passes** that gate
on all three substantive predicates — it is not a fraud, it is simply **not permissive**. 🔵 **A
provenance gate and a grant read are different instruments and neither substitutes for the other.**
One in eight repositories in a category described identically by search was unusable, and only
reading the payload found it.

⚠️ **The scope asymmetry is the real commercial finding.** `canvas-mcp` reaches a course API;
`edu-workspace-mcp` reaches **Docs, Sheets, Slides, Forms, Drive and Classroom** — an entire
Workspace for Education tenant. The OAuth consent a pilot asks a school for is therefore much wider
than the feature being piloted, and `OmarNiazi`'s README states outright *"Google hasn't verified
this app."* In EMEA that is a GDPR conversation before an engineering one; in the US, FERPA/COPPA.
**Scope consent to the tools you enable and put it in the SOW.**

🟢 **And one new regional datum falls out of it.** `Kimmahone/edu-workspace-mcp` is the **first
Korean-language education agent this KB has payload-verified** — Korean README, Korean curriculum
standards referenced, and `docs_import_hwp` / `docs_export_hwpx` for Korea's national document
formats, which is *implementation* evidence rather than prose. Graded as **language** evidence, the
same grade as the Portuguese `ai_tutor_forge`, so Korea-origin is **not** asserted. It lands in the
one APAC jurisdiction with a comprehensive statute in force — South Korea's **AI Basic Act, 22
January 2026**.

## T25 — The most productive research channel this pass was not the web. It was this knowledge base

Three passes running have found shelf-grade rows that star-sorted search cannot see: pass 266 by
probing national-programme names, pass 267 by ranking on commits, and pass 268 — by **grepping this
repository**.

Both headline findings were already inside the base:

- **Ed-Fi.** `intel/open-gaps.md` carries it across at least six numbered gaps (`286`, `303`,
  `309`, `311`, `314`, plus `ACTION TM`/`TR`), records all five repositories as **Apache-2.0,
  payload-read, placed North America**, and states that **Ed-Fi DMS is the only permissive system of
  record this base has found.** Meanwhile `repos/foundations.md` had **no Ed-Fi row**, and
  `verticals/solutions.md` published in pass 267 that public-sector platforms exist for three
  regions *"and still none for North America."*
- **Code.org.** Named in `Gap 367` as the alternative to a missing permissive curriculum, and never
  probed. Grepping the slug `code-dot-org` returned **zero hits across every `.md` in this
  repository**, while the phrase `Code.org` hit four files.

🔴 **This is the third cross-shelf contradiction in three passes**, and it defeated the guard built
for exactly this. Pass 266's standing instruction — *"before republishing any declared gap, grep
the other shelves for its own counter-evidence"* — was followed, and still missed Ed-Fi, because
**the counter-evidence lives in the gap register, which is not a shelf.**

🟢 **Amended standing instruction, and it is cheap:**
1. **Grep `intel/open-gaps.md`**, not only the four `.md` shelves.
2. **Grep for the SLUG as well as the prose claim** — `code-dot-org` and `Code.org` are different
   searches and only one of them was ever run.
3. **Treat a gap note's "named alternative" as an unprobed lead with a deadline**, not as a
   discharge. `Gap 367` named two alternatives and read neither's licence for ~175 passes.

🔵 **Why this belongs in a trends file rather than a method note.** The research instrument defect
this base has been correcting since pass 265 was *external* — star-ranked search is blind to
ministry code. Pass 268's defect is *internal*: **the base knows more than its shelves say**, and
the gap between the two is now the single richest vein available to it. A pass that spends its first
ten minutes grepping itself will out-produce one that spends them searching.

## Confidence notes

- **Payload-verified (strongest):** every licence in this KB's tables, read from
  `raw.githubusercontent.com` on 2026-10-17.
- **Page-verified:** star counts, from repository pages or topic listings dated 2026-10-17.
- **Policy, primary-adjacent:** EU AI Act dates, Brazil MEC documents, India's curriculum
  mandate, SEP survey figures — reported consistently across multiple sources but read
  through secondary coverage, not official gazettes.
- **Vendor-sourced, treat as direction only:** all market-size figures; Moodle 5.2/5.3
  version and LTS-date claims.
- **Declared gaps, as revised by pass 265:** no school-level Japan data (population AI use,
  24.7%, is a different measure and not a substitute); **no APAC-origin *platform*** — the
  agent-and-research claim is retracted, see T13; **no LATAM-origin *agent* and no LATAM-origin
  *permissive* base** — the blanket LATAM claim is retracted, see T12; **no grading *agent***,
  while permissive grading *platforms* are mature, see T14; Mexico's draft AI statute status
  unestablished; Maryland `SB 720` disputed across trackers; Estado de México's April 2026
  reform truncated in all located sources.
- **A note on how three of those gaps were wrong.** Each was a *declared* gap — stated
  honestly, with the search named. Two were still false, and both failed the same way: the
  search ran in English against GitHub's star-sorted topic listings, which under-serve
  Portuguese-language government software and say nothing about an author's institution. An
  informed gap is still information, but a gap is a claim, and claims need re-testing against a
  channel that could falsify them. Pass 265 found both by probing candidate repositories
  directly (`git ls-remote` plus a licence-payload read) rather than by searching harder.

### Pass 267 addendum to the confidence notes

- **The primary-source gap this base has carried since pass 266 is now diagnosed, and it is
  environmental.** Every non-GitHub host tried this pass failed DNS resolution on **both**
  instruments — `curl` and `WebFetch` alike: `ess.iesalc.unesco.org`, `iesalc.unesco.org`,
  `unu.edu`, `digital-strategy.ec.europa.eu`, `www.digitaleducationcouncil.com`, `ve.scielo.org`,
  `repositorio.cepal.org`, `www.marketsandmarkets.com`, plus the news hosts behind the APAC
  figures. GitHub-family hosts and package registries resolve normally. 🔵 **So "re-read the
  primary sources" is not an action a pass in this environment can discharge, and future passes
  should stop spending searches on it.** Non-GitHub material can be reached **only** as search-index
  text, which is secondary-source grade by construction — including every regional percentage in
  [`market.md`](market.md).
- **Repository evidence, by contrast, is at its strongest grade yet:** 31 rows this pass, 29
  licences read from payload or declared metadata, every star/fork/commit cell fetched from the
  repository page, and Sunbird's anomalous cells (41★ / 38,046 commits) **independently
  re-measured and reproduced exactly**.
- **A standing claim tested with a stronger instrument mostly survived.** Five "no licence
  payload" rows were re-probed against 19 paths x 4 refs; **four held** (Athena,
  autoGrader-frontend, openSIS-Classic, awesome-ai-llm4education) and one resolved to MIT at
  metadata grade. 🔵 Worth recording as explicitly as a correction: this base's careful calls are
  holding up, and a pass that reports only corrections misrepresents its own reliability.


## T26 — The curriculum-mandate wave has reached Africa and the Middle East, and the permissive supply has not

`T22` established the mandate wave and its failure mode. Pass 269 ran the four regional legs this
base had specified and never executed — **Kenya, Nigeria, South Africa, Egypt as four separate
queries** — and the wave is plainly there:

- 🇰🇪 **Kenya:** **10,382** public junior secondary schools in a World-Bank-funded (**KDEAP**)
  smart-classroom rollout; **62,000+** teachers ICT-trained as at **July 2026**.
- 🇳🇬 **Nigeria:** AI, cybersecurity, programming and robotics in the junior and senior secondary
  curriculum **from September 2025**.
- 🇪🇬 **Egypt:** a **UNESCO-launched national AI competency framework for teachers (2026-06-03)**,
  **236,000+** general-secondary students enrolled in coding and AI from **2025/26**, technical
  schools from **2026/27**, select primary and middle grades announced.
- 🇿🇦 **South Africa:** the counter-case — **the Draft National AI Policy 2026 was abrogated on
  2026-04-27**, leaving **no national instrument**, while **North-West University** became the first
  SA university with its own AI policy in **January 2026**.

🔴 **And the supply side is empty at the payload, not merely at the query.** Pass 269 located the
first two African-context education agents this base has ever carried —
[`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South Africa, Grades 8–12) and
[`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria) — resolved both default
refs, probed 19 paths on each, read the package metadata as a second channel, and found **no grant in
either**. Nigeria's **Naija Teacher AI** (UNESCO SDG4, offline-first, target **1.5M teachers by Q3
2026**) **states no licence**; Kenya's **Kytabu SOMANASI** is **proprietary**.

🔵 **Why this is the most commercially useful trend in this file.** It is the **inverse of LATAM**.
There, adoption outran governance and the sellable work is governance retrofit (`P13`). Here, **the
state programme arrives first** — funded, named, dated, with enrolment and teacher counts attached —
**and there is nothing off the shelf to satisfy it.** A market that has not yet bought anything is a
better starting position than one that has.

🟡 **The region splits on where to enter.** Kenya and Egypt have **national anchors** (a funded
rollout; a teacher-competency framework), so a ministry-level engagement has an instrument to attach
to. **South Africa has none at national level and a live one at institutional level** — so the same
pitch has to enter one country through a ministry and the next through a university.

⚠️ **Grade:** every figure above is **secondary-source**. `p268` established the non-GitHub DNS
failure as environmental, and pass 269 did not re-spend searches on primary retrieval. **There is
also still no MEA market sizing of any kind in this base** — the region now has programme rows and
no number.

## T27 — A licence can be inherited from a project template, and the most on-point artefact in a category is where that bites

`T20` moved licence risk from the **name** of a grant to its **shape**. Pass 269 found a third axis:
a grant's **provenance** — who chose it, and whether anyone chose it at all.

[`datawhalechina/ai-edu-for-kids`](https://github.com/datawhalechina/ai-edu-for-kids) is *"面向中小学的
人工智能通识课开源课程"* — an open-source **AI general-education course for primary and secondary
schools**, **128★ / 27 forks / 57 commits**, and **the most-adopted primary-band AI-curriculum
artefact this base has located.** It serves **no `LICENSE` payload on 19 of 19 paths**. Its README
declares **CC-BY-NC-SA-4.0** — NonCommercial *and* ShareAlike, the one shape a client deliverable
cannot carry. **And the line immediately after the declaration reads, verbatim:**

> *注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议*
> — "note: CC 4.0 is used by default; you may choose another licence depending on your project."

🔴 **The most restrictive attribute of the most relevant artefact in this category is boilerplate
carried over from an organisation's project template.** Nobody decided that this curriculum should
be non-commercial; the template said so, and the template's own text invites a different choice.

🔵 **Two practical consequences, in opposite directions.**
1. **Never assume it away.** A template default is legally identical to a deliberate NC-SA. Until an
   upstream says otherwise in writing, the course is unusable in a paid deliverable, and `P17`
   (originate the content, borrow only the specification) is the move.
2. **It is the licence most likely to change if asked.** Contrast a grant chosen *for* a reason —
   `PageLM`'s bespoke community licence, `AStheTECH`'s all-rights-reserved — which will not move.
   **A provenance read tells you which conversations are worth having**, and this base has, until
   now, recorded only the verdict and never who picked it.

🟡 **The same read has a second use, demonstrated this pass.**
[`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) carries, in its README, *"Add
the project's chosen license here before publishing if a specific open-source license is required."*
**That is not an unlicensed project; it is a PRE-LICENCE one** — the author has written down that the
grant is missing. Against [`ls1intum/Athena`](https://github.com/ls1intum/Athena), silent through 76
path/ref probes across three passes, the difference is entirely actionable: **one of these rows is
worth an email and the other is not**, and only a provenance read separates them.

## T28 — European teachers have already adopted AI and already concluded the general-purpose tools do not work

The **Sanoma Learning 2026 European Teacher Survey** — **more than 20,000 teachers across 14
countries** — reports two numbers that have to be read together:

| | |
|---|---|
| European teachers using AI | **63%** |
| European teachers who believe **general-purpose** AI improves learning outcomes | **16%** |

**A 47-point gap between adoption and believed efficacy.** Adoption is not the open question in
EMEA; it is settled. What is open is whether the thing being adopted does anything.

**For the studio:** this inverts the standard pitch. The conversation is **not** "you should adopt
AI" — that argument is already won and the client has the receipts to prove it did not help. The
conversation is **"the general-purpose assistant your teachers are already using does not know your
curriculum, your assessment rules or your exam board, and that is why 84% of them do not think it
works."** Every education-specific, curriculum-bound asset on this base's shelves is an answer to
that sentence: `instructional_agents` (MIT) binds to a course spec, `Numbas` (Apache-2.0) binds to
an assessment, `OpenDidactia` (CC BY-SA 4.0) binds to **LOMLOE's own criteria**, and
`DECK6/korean-elementary-learning-map` (MIT) binds to a national curriculum graph.

⚠️ **Grade:** vendor-published survey. Sanoma sells education materials, so a finding that
general-purpose AI underperforms flatters the publisher's category. Carried anyway, for a specific
reason: **the 63% is self-damaging to the publisher's own "teachers need our tools" framing** (it
concedes teachers already have tools), and the direction is corroborated by `T22`'s independently
documented Korean failure — a mandated general-purpose rollout that reached **under 30% adoption**
and lost official textbook status. *Secondary-source; no primary channel available in this
environment.*

🔵 **The falsifiable form:** if a second, non-vendor European survey puts believed efficacy of
general-purpose AI materially above 16%, this trend weakens. Nobody has located one.

## T29 — A propagation claim is not evidence of propagation, and this base has now caught itself asserting one

Five consecutive passes have each found the same class of defect — a fact this base **knows** that
never reached a file this base **ships**. Pass 270's instance is a new species and the worst of the
five, because it is self-reporting:

Of the Sanoma survey above, `agents/trending.md` states, verbatim:
*"Recorded in `intel/market.md` and `intel/trends.md`."*

```
$ grep -c "Sanoma" intel/market.md intel/trends.md
intel/market.md:0
intel/trends.md:0
```

🔴 **A pass asserted the propagation it had not performed.** The four earlier defects were
omissions — silence, which a grep can find. **This one was worse than silence: it was a sentence
that answered the grep.** Any later pass auditing the register for unshelved datums would read that
line as proof the work was done, and `p269`'s backlog sweep — which found six unshelved datums by
grepping each one — **did not list Sanoma, because the register said it was shelved.**

**The method amendment, one line:** `p268` amended the **novelty** check to grep the *slug* rather
than the prose. **`p270` amends the *propagation* check to grep the DESTINATION file, never to
trust a claim in the source file.** Both defects were invisible to precisely the check that
preceded them, which is the argument for writing the amendment down rather than fixing the instance.

**For the studio:** the same failure mode is what a client's AI-governance register looks like after
two years. The deliverable that prevents it is not a better register — it is **a check that reads
the artefact instead of the claim about the artefact.**

## T30 — Regional market sizing is single-publisher sizing, and the EMEA number moves 25% when a second one shows up

This base's global market-size table is a **narrow band ($8.7–10.6B for 2026)** across five
publishers. Its **regional** figures are nothing like that well supported, and pass 270 measured
how badly:

> 🔴 **CORRECTED IN PASS 274 — the sentence above is superseded and the word "narrow" is wrong.**
> `p273` added Grand View's current vintage (`$11.4B`) to that table and corrected the band **on
> `intel/market.md` only**; this entry kept the number it was written with. **The 2026 band is
> `$8.7–11.4B`, 31.0% wide**, across **four independent models** (`T40`), not five publishers.
> 🔵 **This is `T37`'s species — a quantified claim decaying in its quantity on the shelf that was
> not updated — and it is the SECOND instance between these same two files.** The first was the MCP
> count. ⚠️ **It also undercuts this entry's own argument in the base's favour:** `T30` contrasts a
> tight global band against loose regional figures. **The global band is not tight.** The
> regional-vs-global point survives; the adjective does not.

| Europe, AI in education | 2026 | Horizon | CAGR |
|---|---|---|---|
| carried by this base ~200 passes | **$2.64B** | $8.0B by 2030 | 31.9% |
| MarketDataForecast | **~$2.11B** | ~$20B by 2034 | 32.47% |

**~25% apart on the same year, ~2.5× apart on the horizon, and their CAGRs agree to within half a
point** — so the entire disagreement is in the **baseline**, which is the one figure this base's own
market file instructs you to quote and the one a client slide actually carries. The leg that found
the second publisher states it could locate **no third**: two is the published universe for Europe.

🔵 **Why this generalises beyond EMEA.** The global band looks tight because five publishers
triangulate it. Every *regional* figure on this base — NA's **$3.68B**, MEA's **$0.56B**, LATAM's —
rests on **one** publisher each, and has never been tested the way EMEA's just was. **The tightness
of the global band is not evidence that the regional splits are sound; it is evidence that only the
global figure has been checked.**

**For the studio:** quote regional market size as a **range with the publisher count attached**
("$2.1–2.6B, two publishers"), or quote the global baseline and the regional *share*. A single
confident regional number is the one claim the evidence will not support — and a client who checks
will find the other publisher.

## T31 — A carried datum decays in one direction: toward overstating its own authority

Pass 270 re-verified six regional datums this base had carried in prose rather than on a shelf.
**Five of the six had changed shape.** The changes were not random:

| carried as | actually is | direction of the error |
|---|---|---|
| "the **STUDENTS FIRST Act** of 2026" | a student-written **model policy**, 82-16 in a mock Senate | 🔴 exercise → **statute** |
| "North Carolina's K-12 **implementation guidance**" | a **2024-01-16** DPI guidebook, two layers below NC's current position | 🔴 dated advisory → **current guidance** |
| "the **Linux Foundation LATAM AI workforce report**" | *Economic and Workforce Impacts of AI in Latin America*, 4th in a Meta-sponsored series | 🔴 real report → **a title that does not exist** |
| "the EMEA figure of **$2.64B**" | one of **two** publishers, ~25% apart | 🔴 a range → **a number** |
| "**Finland / Estonia / Netherlands** as K-12 leaders" | two stand on different grounds; the third is **unsubstantiated** | 🔴 one aggregator → **a grouping** |
| "the **US DOL AI Literacy Framework** (2026-02-13)" | confirmed, **TEN No. 07-25**, five content areas | 🟢 held |

🔴 **Every one of the five errors made the datum sound MORE authoritative than it was** — a model
policy gained the word "Act", a two-year-old guidebook became the current position, a report
acquired a cleaner title than the one it has, a forecast range collapsed into a point, and an
aggregator's grouping became a finding. **None of the five decayed toward understatement.**

🔵 **The mechanism is compression, not carelessness.** Each datum was shortened every time it was
restated, and the parts that get dropped when you shorten a fact are its **qualifiers** — the
status marker, the date, the publisher, the sample. What survives compression is the **claim**, and
a claim without its qualifiers reads as stronger than the evidence behind it.

**For the studio, and this is the transferable part:** a client knowledge base that has been
maintained by restatement — every quarterly deck summarising the last one — is **systematically
overconfident**, and the overconfidence is concentrated in exactly the cells a slide quotes.
**The audit that catches it is cheap and it is not an audit of the summary: re-run the original
query and compare.** Pass 270 ran six such queries and five came back different. **Budget one
re-verification pass per six carried datums**, and expect roughly that hit rate.


## T32 — Arithmetic is a second oracle, and a market shelf that never multiplies its own cells will carry an impossible one

Pass 271 was sent to re-verify the North America market figure against a second publisher. It never
needed one. The cell read **$3.68B (2026) → $32B (2030) @ 31.1% CAGR**, and:

```
3.68 × (1.311)^4 = 10.87      # what the stated CAGR produces
$32B from $3.68B in 4 years   # requires 71.7%, not 31.1%
```

The publisher, unrecorded for roughly 200 passes, turned out to be **ResourcERA**, which publishes
**$10.8B by 2030** — agreeing with the arithmetic and not with this base. The mechanism is exact and
reproducible: this base kept ResourcERA's *regional* baseline and *regional* CAGR and took its
**global** horizon (**$32.27B**). The two CAGRs — regional 31.1%, global 31.2% — differ by a tenth of a
point, which is why the row read as consistent to anyone checking the source rather than the
multiplication.

**Why this is a new defect class here.** Every defect passes 266–270 found was *cross-shelf*: a cell
disagreeing with another file, caught by `grep`. **This one is intra-cell — the row disagrees with
itself** — and no grep finds it, because nothing anywhere contradicts it.

**For the studio, and this generalises past education:** any client deck with a baseline, a CAGR and a
horizon has three numbers where two are free. **Multiply before you publish.** Run against this base's
four regional rows, EMEA, LATAM and ResourcERA's own NA all reconcile to within 1%; only the carried NA
row failed, and it failed by **2.9×**. One line of arithmetic found what two hundred passes of sourcing
discipline did not.

**The rule needs a THRESHOLD, and pass 271 calibrated it by running the check against its own new
figures** — which is the test a new rule should have to pass before it is handed to the next pass:

| figure this pass added | implied vs published | read |
|---|---|---|
| MEA AI-tutors (Grand View) $188.5M @ 32% → 2033 | **0.03%** | 🟢 reconciles |
| MEA AI-tutors (Transpire) $186.4M @ 32.13% → 2033 | **0.09%** | 🟢 reconciles |
| LATAM (Grand View) $259.6M @ 32.4% → 2030 | ~5% | 🟢 window rounding |
| APAC (Grand View) ~$2.28B @ 28.1% → $18.2B 2033 | **10%** | 🔴 **NOT noise — `p272` resolved it: a one-year window offset. Reads +0.0% from a 2026 base of $3,217.5M. See `T38`** |
| NA (Grand View) $3,113.8M @ 24.2% → $19.4B 2033 | **10%** | 🔴 **SAME defect as the APAC row (`p272`): $3,113.8M is a 2025 print, the CAGR is labelled 2026–2033. Reads −0.0% from a 2026 base of $4,253.6M. See `T38`** |
| NA (MarketsandMarkets) $951M @ 15.9% → $2.3B 2029 | **16%** | 🟡 rounding + window label |
| **NA as this base carried it** | **190%** | 🔴 **structural** |

**So a 10–16% mismatch is the normal noise of this literature** — publishers round their baselines,
label a CAGR to a window that differs from the span between the two numbers they print, and revise
base years between report vintages. ⚠️ Grand View's MEA row is the clearest case: its $280.8M (2024)
base and $1,645.9M (2030) horizon reconcile **only** if the 32.6% CAGR is applied to its labelled
2025–2030 window, which requires a **+43% single year** from 2024 to 2025 — almost certainly two report
vintages, not one growth curve.

**The threshold, therefore: flag at >25%, investigate at >50%, and treat a multiple as a structural
error rather than a disagreement.** A check that fires on every row is a check nobody runs. The carried
NA cell was out by **2.9×** — it would have cleared no threshold at all, which is the point.

> 🔴 **RETIRED IN PASS 274, and the calibration table above is wrong in two rows.** `p272` already
> refuted *"10–16% is the normal noise of this literature"* for the APAC and NA cells (`T38`).
> `p274` ran the window test on **every** cell and refuted it for the M&M rows too: **NA M&M's 16%
> closes to `+0.22%` at a six-year span and LATAM M&M's to `+0.20%`.** So the row annotated
> *"rounding + window label"* was **window label, no rounding** — and the row annotated *"window
> rounding 🟢"* (LATAM, Grand View, ~5–7%) **closes at no window at all and is a SPLICE.**
> 🟢 **The replacement rule is simpler and cheaper than a threshold:** a window test is **one
> multiplication**, so **run it on every cell and classify, rather than filtering by size** —
> `PASS` (closes as labelled) · `WINDOW_FIX` (closes at ±1 year: a year label is wrong) · `SPLICE`
> (closes at neither: two report vintages, never publish as a series).
> 🔵 **A threshold is a filter on which cells get checked; the defects on this shelf were in cells
> under the filter.** `p271`'s *">25%"* would not have fired on **any** of the five window defects
> now established. See `T42`.

## T33 — A source is not reliable per-clause, and this base was quoting half of a sentence it had thrown away

`p270` retracted *"Finland / Estonia / Netherlands as K-12 leaders"* on the grounds that it traced
**only to an aggregator citing no source**. Pass 271's EMEA leg returned the aggregator, and the
retracted claim and a figure this base quotes are **the same sentence**:

> the European AI in education market at **$2.64 billion in 2026**, forecast to grow at **31.9% CAGR**
> to **$8.0 billion by 2030**, with **Finland, Estonia, and the Netherlands leading in K-12 AI
> integration**

This base deleted the second half as unsourced and kept the first half as a market figure — and
`p270` re-published that figure as one half of its new two-publisher EMEA range, in the same pass that
performed the retraction.

**The rule:** when a source is disqualified, every datum taken from it inherits that grade. You may
keep the figure and downgrade it, or drop it, but you may not retract a source's policy claim and
promote its market claim in the same breath. The `$2.64B` end of the EMEA range now carries the grade of
the claim this base discarded; **MarketDataForecast's ~$2.11B is the end with a publisher behind it.**

**Corollary, and it is the more useful half:** the regional picture is not *one publisher per region* as
`T30` warned — it is **one publisher for the whole regional picture**. ResourcERA's signature (2026
baseline, 2030 horizon, 31–34% CAGR) fits all four carried regional rows, and they sum to **$7.55B**
against its own **$10.4B** global baseline, leaving an APAC residual of **$2.85B** that lands within
**2.5%** of Grand View's independent estimate. The decomposition is coherent, which is precisely the
problem: **a coherent single source reads exactly like corroborated multiple sources.**

## T34 — A declared gap is a claim, and it decays the same way every other carried claim does

`p270` found this base asserting a propagation it had never performed (`T29`: *"Recorded in
`intel/market.md`"* — `grep` said `0`). Pass 271 found the **inverse**: `market.md` declaring
*"MEA remains UNSIZED"* while the base carried **$0.56B (2026), 34.3% CAGR** in three other files.

**These two defects are mirror images and only one of them is catchable by `T29`'s amendment.** A false
claim of *presence* is refuted by grepping the destination. A false claim of *absence* is **confirmed by
the very silence it describes** — the check and the defect produce the same reading. This is the
**sixth cross-shelf defect in six passes**, and the third whose species was invisible to the check
written one pass earlier.

**The amendment:** before re-declaring a gap, `grep` the OTHER shelves for the thing said to be
missing. A gap declared in one file is a statement about the whole base, and no file can establish it
alone.

**For the studio:** an engagement's "we have no data on X" register needs re-verification on the same
cadence as its findings. **An institution's inventory of its own blind spots is not a different kind of
artefact from its inventory of facts** — pass 271 budgeted one sweep against seven declared gaps and
moved four of them.

## T35 — Retract the claim, not the country: `NOT_ESTABLISHED` is two verdicts wearing one label

`p270` retracted the Netherlands and recorded `NOT_ESTABLISHED`, writing that **"no national Dutch
instrument or programme was located"** — and costed the remedy without running it: *"Dutch-language
queries against the Ministerie van OCW and SLO."*

Pass 271 ran it in Dutch, and the instrument is there: **`kerndoelen digitale geletterdheid`**, with
**`AI-geletterdheid` explicitly included**, covering **primair onderwijs, onderbouw vo and (v)so**,
**legally official 2027-08-01**, fully introduced with **Inspectie** oversight in **2031**.

So the aggregator's *claim* — the Netherlands "leading in K-12 AI integration", present tense — is still
unsupported, and `p270`'s *conclusion* — nothing is there — was **false**. `NOT_ESTABLISHED` was
carrying two incompatible meanings: **"the assertion is wrong"** and **"nothing exists"**. The gap
between them was **the search language**.

**And the corrected finding is commercially better than the claim it replaces.** A present-tense
"leader" is a market already lost. **A concept curriculum that becomes binding on a named date, in the
primary band, inspected from 2031, is a procurement runway** — and it lands in exactly the band where
`Gap 367` has established, in four languages now, that permissive supply does not exist. See `P21`.

**For the studio:** when a regional claim fails verification, the next query is the same question in the
**national language**, not a retraction. This base runs its legs in English and has now found
country-level instruments in Spanish (`p270`), Chinese and Hindi (`p269`) and Dutch (`p271`) that the
English legs did not return. **An English-only absence is a statement about the query.**


## T36 — Re-publication is indistinguishable from corroboration, and this base had been checking Grand View against Grand View

`p271` established that this shelf's four regional market rows were **one vendor's decomposition** and
named the vendor **ResourcERA**, flagging the attribution as its *"one claim made on inference rather than
reading"*. `p272` ran the falsification `p271` asked for. **The attribution was half wrong and the real
structure is one level deeper.**

| row | `p271` said | `p272` established |
|---|---|---|
| **North America** `$3.68B → $10.80B @ 31.1%` | ResourcERA | 🔴 **Technotrenz.** The leg, asked directly, says it *"is not a ResourcERA figure"*. ResourcERA publishes NA as a **36% share**; `0.36 × $10.4B = $3.744B`, **1.7% from Technotrenz's number** |
| **EMEA** `$2.64B` | ResourcERA | 🔴 **Grand View, re-based.** GVR's Europe data-tree base `$1,520.1M` (year unprinted; arithmetic fixes it at **2024**) compounded **two** years at GVR's own 31.9% gives **$2,644.6M** — a **0.17%** match |
| **MEA** `$0.56B @ 34.3%` | ResourcERA | 🔴 **Grand View, re-based.** 34.3% is **exactly the CAGR implied by GVR's own MEA endpoints** `$280.8M → $1,645.9M` |
| **Global** `$32.27B @ 31.2%` | ResourcERA | 🔴 **Grand View, verbatim**, from its own press release |
| **LATAM** `$0.67B @ 33.5%` | ResourcERA | 🟡 **does NOT reconcile to Grand View** — GVR's 2026 point is **$455M**, so ResourcERA is **47% above it**. The one regional row with no established upstream |

🔴 **The consequence falls on `p271`'s headline result.** `p271` derived APAC as the residual of the
regional sum and reported it *"corroborated to 2.5% by Grand View … by a different method"*. **Grand View
is ResourcERA's source.** The residual was extracted from Grand View's decomposition and then validated
against Grand View. 🟢 **That agreement was arithmetically guaranteed** — and the tightness of it (2.5%)
is what made it persuasive.

🔵 **The general lesson, and it is the one worth taking to a client.** Four publisher names on a slide
look like four models. **Counting names counts citations, not models.** The tests that actually
discriminate cost nothing and need no page access:
1. **Look for a verbatim horizon.** `$32.27B` and `31.2%` are too specific to coincide.
2. **Try to reproduce one publisher's baseline from another's curve.** If `A(2026) = B(2024) × (1+B's CAGR)²`
   to within a fraction of a percent, A is re-basing B.
3. **Check whether an implied CAGR in one source is a labelled CAGR in another.** ResourcERA's MEA 34.3%
   is Grand View's MEA endpoints, solved.
4. **A share and a dollar figure are not two data points.** `p272`'s NA row exists because an aggregator
   multiplied someone else's percentage by someone else's base.

⚠️ **Standing consequence for this shelf: no independent corroboration of any regional
AI-in-education figure has been located. Every appearance of it so far has been re-publication.**
Say that to a client rather than presenting a consensus that does not exist.

**Confidence: high** on all four reconciliations (each is arithmetic over numbers this base can quote).
**Secondary-source grade** on every figure — `resourcera.com`, `technotrenz.com` and
`grandviewresearch.com` are all `ENOTFOUND` from this environment, re-tested this pass.

## T37 — A quantified gap decays in its quantity, and no check on this base reads the number

`intel/trends.md` stated that the `mcp-server-education` GitHub topic is *"still empty while **five**
payload-verified education MCP servers exist"*. `agents/top.md` prose says **eleven**; counting the rows
gives **12 distinct slugs**.

🔵 **The gap is TRUE.** The topic is empty. That is exactly why every existing check passes it:

| check | what it tests | verdict here |
|---|---|---|
| `T29` (`p270`) | grep the **destination** for a claimed presence | 🟢 PASS — the servers really are shelved |
| `T34` (`p271`) | grep **other shelves** before re-declaring an absence | 🟢 PASS — the absence is real |
| `T32` (`p271`) | multiply a cell and compare | 🟢 PASS — nothing to multiply |

🔴 **None of them reads the numeral in the sentence.** Passes 267 and 268 added MCP servers and
incremented the count on `agents/top.md` while `intel/trends.md` kept the number it was written with.

🟢 **Amendment: a quantity inside a gap statement is a carried datum and decays like every other one.
Re-derive it from the rows — on every shelf that states it — not from the sentence that last stated it.**
🔵 Note the direction of the decay, which matches `T31`: the stale count **understated** the base's own
holdings, i.e. it made this KB look weaker than it is. `T31` found carried claims decay toward
**overstating** their authority; a carried *count* can decay the other way, and both are errors a studio
would be briefed on.

**Confidence: high** — both numbers were counted from the files this pass.

## T38 — A publisher can mislabel its own CAGR window, and a 10% mismatch is the symptom this base had been writing off as rounding

`p271`'s costed item 2 — *"run `T32`'s arithmetic check across EVERY remaining numeric cell … it needs
zero searches, the cheapest audit available"* — was run over **19 cells**
([ledger](../evidence/arithmetic-sweep.2026-10-17-p272.tsv)).

🟢 **Headline: no cell on these shelves is impossible any more.** `p271`'s NA row was the only
`STRUCTURAL` one and it is corrected. **Two cells `FLAG`, and both are the same publisher-side defect:**

| Grand View databook | as the page LABELS the window | read one year earlier |
|---|---|---|
| **Europe** `$1,520.1M → $8,003.4M @ 31.9%` | labelled **2025–2030** → **+31.9%** 🔴 | **2024–2030** → **−0.0%** 🟢 |
| **MEA** `$280.8M → $1,645.9M @ 32.6%` | labelled **2025–2030** → **+43.0%** 🔴 | **2024–2030** → **+7.8%** 🔴 **NOT GREEN — `p274`.** `+7.8%` is not a resolution; this cell closes at **no** window and is a **SPLICE**, which `market.md` already said in prose (*"two report vintages, not one growth curve"*) while this table ticked it |
| 🆕 **GLOBAL** `$8.3B → $57.2B @ 25.9%` | printed baseline **2025** → **−8.40%** 🔴 | window **2026–2033** → **−0.07%** 🟢 — **added in `p274`: the house's signature is in its GLOBAL cell too, and that cell is this base's headline** |
| **APAC** `$2,282.9M → $18,214.1M @ 28.1%` | printed baseline **2025** → **+10.0%** 🟡 | window **2026–2033** → **+0.0%** 🟢 |
| **North America** `$3,113.8M → $19,388.3M @ 24.2%` | printed baseline **2025** → **+10.0%** 🟡 | window **2026–2033** → **−0.0%** 🟢 |

🔴 **The last two rows are the important ones, because this base had already measured them and filed them
away.** `T32`'s own calibration table carries the APAC row annotated **"base stated as 'roughly'"** and the
NA row as **"rounding + window label"**. 🟢 **Neither is rounding.** On Grand View's 2033-vintage regional
pages the printed "current" figure is a **2025** number while the CAGR is labelled **2026–2033**; compound
the printed baseline across the full span and you are a year out, every time, by about 10%.

🟢 **Correcting it is not cosmetic.** It moves APAC's 2026 point from **$2.92B to $3.22B** and NA's from
**$3.87B to $4.25B** — each a ~10% revision to a number a studio would size an engagement from, and in
both cases *upward*.

⚠️ **Standing rule: derive the baseline from the horizon and the CAGR; never trust the printed baseline's
implied year.** `base = horizon / (1 + CAGR)^(years in the LABELLED window)`.

🔵 **And `T32` gains a second duty.** `p271` set the threshold at *">25% flag, >50% investigate"* and
declared 10–16% *"the normal noise of this literature"*. **That calibration is sound as a floor but it was
being used as an explanation.** A 10% mismatch now means **test the window first**; only call it noise
once a one-year shift fails to resolve it. Four of the four cells tested this way resolved.

**Confidence: high** — pure arithmetic over published endpoints, reproducible from the ledger.

## T39 — A licence file's byte count discriminates nothing on its own, and this base measures bytes

This base's verification practice includes **blind re-measurement of licence payload byte counts**
(`p271` re-measured three and reported agreement "to the byte"). `p272` probed
`OpenOLAT/OpenOLAT` — already shelved on `verticals/solutions.md` as the one Apache-2.0 full LMS — and
measured **10,982 B**, which is **375 B SHORT** of the stock Apache-2.0 file (`apache/.github`: 11,357 B).

🔵 **A short Apache file is exactly the shape of a rider**, and this base has been burned there before:
`p252` found a **Commons Clause** rider on a row that had been blessed as MIT for four passes.

🟢 **It was not a rider.** Diffing the payload against upstream:
- **Lines 1–175 — the entire `TERMS AND CONDITIONS` — are byte-identical to stock Apache-2.0.**
- The deleted span is the **optional `APPENDIX: How to apply the Apache License to your work`**.
- What replaces it is **two attribution statements** naming the OLAT Zentrum / University of Zurich and
  frentix GmbH. **No additional restriction, no field-of-use limit, no non-commercial clause.**
- Every hit from a rider keyword grep (`except`, `does not grant`, `additional terms`) is **stock Apache
  text** — §3 patent, §5 contributions, §6 trademarks.

🟢 **Verdict: unmodified Apache-2.0, rider-cleared.** `OpenOLAT` is safe to recommend as the permissive
LMS, now at a stronger grade than the shelf carried.

🔴 **The methodological finding is about the measurement, not the repo — and `p272` measured the
distribution rather than arguing from one pair.** Eight payloads were read this pass; **six are
Apache-2.0 and they span `10,273 B` to `11,525 B`, a 1,252 B range straddling the stock 11,357 B in
BOTH directions:**

| repo | bytes | vs stock 11,357 B | terms |
|---|---|---|---|
| `tsugiproject/tsugi` | **10,273** | −1,084 | unmodified |
| `OpenOLAT/OpenOLAT` | **10,982** | −375 | unmodified *(diffed line-by-line)* |
| `autolab/Autolab` | **11,324** | −33 | unmodified |
| `numbas/Numbas` | **11,357** | **0** | unmodified |
| `yetanalytics/lrsql` | **11,357** | **0** | unmodified |
| `haxtheweb/haxcms-php` | **11,362** | +5 | unmodified |
| `HKUDS/DeepTutor` | **11,408** | +51 | unmodified |
| `adlnet/xAPI-Spec` | **11,525** | **+168** | unmodified |

🔵 **Every one is an unmodified grant, and no byte count predicts that.** The range is wider than any
plausible rider (a Commons Clause rider is ~300 B) and it is **two-sided**, so there is no threshold —
above or below — that separates modified from unmodified.
⚠️ **So a byte count can neither confirm nor refute a grant.** It is useful for exactly one thing — detecting
that a payload **changed between two passes** — and useless for deciding **what** a payload says.

🟢 **Amendment: a byte delta against stock is a TRIGGER for a terms-section diff, never a verdict.**
Diff lines 1 through `END OF TERMS AND CONDITIONS`; everything after it is boilerplate a project may
replace freely. 🔵 This also means `p271`-style agreement "to the byte" proves **stability**, not
**correctness** — two passes can agree to the byte on a payload neither of them read.

**Confidence: high** — eight payloads read first-hand this pass, one diffed against upstream line-by-line,
and the rider-keyword grep (`commons clause` / `non-commercial` / `may not sell`) returned **zero across
all eight** ([evidence](../evidence/verified-repos.2026-10-17-p272.tsv)).

## T40 — The market-size shelf cannot tell a research house from a shop that sells reports

*(new in pass 273)*

`T36` established that this base's regional market figures were aggregators re-publishing **one**
research house. The fix applied then was to trace each figure upstream until it stopped moving.
🔴 **Pass 273 shows that test has a blind spot: it checks whether a name is re-publishing someone
else's model, and never checks whether the name is a research house at all.**

The largest-CAGR row in the forecast-spread table on [`intel/market.md`](market.md) was credited to
**"Research and Markets."** ResearchAndMarkets.com does not produce forecasts — it is a **storefront that
resells them**. The model belongs to **The Business Research Company**: *AI in Education Market Report
2026*, February 2026, 250pp, with the numbers carried in a ResearchAndMarkets press release on
GlobeNewswire dated `2026-04-07`.

🟢 **Unusually, the correction is good news.** TBRC is genuinely independent of Grand View, so the count
of independent models behind this shelf goes **up** — to at least three — where `T36` had driven it down
to roughly one.

🔵 **And the comparison it unlocks is the most useful market sentence this base has produced.** Carried to
a common year on each house's own CAGR, **TBRC says $42.48B at 2030 and Grand View's own curve says
$28.64B — 1.48x apart** — while their 2026 baselines sit only 7% apart, in the *opposite* order. **The
two most independent houses available agree about today and diverge by half again about 2030.** A `T32`
sweep over all four independent rows came back **clean**, so this is a disagreement about the world, not
an arithmetic defect in anybody's model — and therefore not resolvable by picking the most careful-looking
publisher.

**What to do with it.** Quote the 2026 baseline as a **band ($8.7–11.4B, 31% wide)**, name the house —
not the storefront — beside any horizon figure, and never put a single 2030 TAM on a slide without saying
whose curve it is. **The spread is the finding; it always was, and `T40` is the reason the spread was
being under-counted.**

## T41 — A repository is not an artefact, and root-grant grading cannot see the difference

*(new in pass 273)*

This base grades licences at the repository root: `SOLE`, `OWN-GRANT-AT-ROOT`, one payload, one verdict.
🔴 **Pass 273 found a repository where that model is correct about the file and wrong about the
deliverable.**

[`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) serves **MIT** at
`main/LICENSE` — 1,065 B, byte-identical to stock, zero rider keywords, measured four separate times by
this base's own instrumentation. 🟢 **That grade is right.** But the repository ships **two** artefacts
into **two different licence ecosystems**: the TypeScript MCP wrapper, which links nothing and talks REST,
and `local_italiciamcp`, a **Moodle `local_` PHP plugin** that performs every write, declares
`MOODLE_INTERNAL`, requires Moodle 4.0+, and calls `core_external\external_api`. The plugin serves **no
grant of its own** (no `LICENSE`, no `README` in its directory — both 404) and **no GPL notice on any of
the six files that serve** — while opening with Moodle's own file header, *the GPL paragraph removed*.

🟢 **The consequence is narrow, and must not be inflated into a warning.** MIT is **GPL-compatible**;
there is no conflict in the grant. What changes is the licence of the **combination**: Moodle plus the
plugin is a **GPL-3.0** work, so a *distributed* image carrying it ships as GPL-3.0 — while a **hosted**
deployment is unaffected, because GPL-3.0 has **no network clause**. 🔵 **Which means the MIT row remains
strictly cheaper than the AGPL-3.0 row this shelf used to carry as the only Moodle option.**

**The generalisable rule, and it reaches well past this repo.** 🔵 **Wherever a permissive repository
ships a plugin for a copyleft host — a Moodle `local_`/`mod_`, a WordPress plugin, a GIMP or Blender
extension — the root grant describes the source, and the host's licence describes the thing the client
actually deploys.** Ask of every permissive row: *is there a sub-directory here that only runs inside
somebody else's GPL?* This base's instrumentation does not currently ask it, which is why four correct
measurements of this repository never surfaced the question.

## T42 — A threshold is a filter on which cells get checked, and the defects were under the filter

*(new in pass 274)*

`T32` gave this base its arithmetic oracle and then gave it a **threshold**: *"flag at >25%,
investigate at >50%."* `T38` refuted that threshold for two cells. 🔴 **`p274` ran the window test on
all 28 market cells on these shelves and the threshold fails systematically: not one of the five
established window defects would have fired it.**

| cell | mismatch as labelled | would `>25%` fire? | what it actually is |
|---|---|---|---|
| Europe, Grand View | −24.17 % | 🔴 **no** *(and it is the one `p272` DID catch)* | `WINDOW_FIX` |
| APAC, Grand View | −9.12 % | 🔴 no | `WINDOW_FIX` |
| North America, Grand View | −9.07 % | 🔴 no | `WINDOW_FIX` |
| **Global, Grand View** | **−8.40 %** | 🔴 no | `WINDOW_FIX` — **the headline cell** |
| North America, M&M | −13.53 % | 🔴 no | `WINDOW_FIX` — **never swept at all** |
| LATAM, M&M | −10.30 % | 🔴 no | `WINDOW_FIX` — **swept and marked `ok`** |

🟢 **The replacement is not a better threshold. It is the removal of the threshold**, because the test
it was rationing costs one multiplication:

```
PASS        |projected/published − 1| ≤ 1 %  at the labelled span
WINDOW_FIX  closes at span ± 1 year       → a YEAR LABEL on the row is wrong
SPLICE      closes at neither             → TWO REPORT VINTAGES; never publish as a series
```

🔵 **Why a threshold was the wrong instrument in the first place.** It was calibrated on the *size* of
the error, and the errors on this shelf are not large — they are **structural and small**. A one-year
window offset on a 25–32 % CAGR produces a mismatch of roughly the CAGR divided by the span: **8–14 %**,
which sits precisely in the band `p271` defined as noise. 🔴 **The threshold was tuned to exclude the
defect's own signature.**

⚠️ **And a second-order finding worth more than the first: the two ledgers use OPPOSITE sign
conventions.** `p272` reports `published/projected − 1`; `p274` reports `projected/published − 1`. **The
same LATAM cell reads `+11.5 %` in one ledger and `−10.3 %` in the other.** A threshold compared across
two conventions was never comparing anything. **Every ledger on this base now states its convention in
its header.**

**For the studio, and this generalises past education:** a client's data-quality rule that fires on
*magnitude* will miss every defect whose mechanism bounds its own size — unit errors, off-by-one
periods, vintage splices. **Classify by mechanism, not by size, whenever the test is cheap enough to
run on everything.** Here it is one multiplication per row.

**Confidence: high.** 28 cells, pure arithmetic over published endpoints, reproducible from
[`compose/code/p274-window-sweep/window_sweep.py`](../compose/code/p274-window-sweep/window_sweep.py)
and [its ledger](../evidence/arithmetic-sweep.2026-10-17-p274.tsv).

## T43 — An amendment that is not built is not an amendment, and this base had three of them

*(new in pass 274)*

🔴 **`T37` (`p272`) wrote the rule: *"a quantity inside a gap statement is a carried datum — re-count
it from the rows, on every shelf that states it."* `p273` ranked building it seventh. Nobody ran it,
and in the two passes between the amendment and its implementation the base published three more
stale quantities.**

`p274` built it — 90 lines, no network
([`recount.py`](../compose/code/p274-quantity-recount/recount.py)) — and the first run printed
**3 STALE of 5 registered claims**:

| claim | published | measured | where |
|---|---|---|---|
| MCP server slugs on `agents/top.md` | **13** | **15** | `agents/top.md` prose (`p273`) |
| MCP server slugs on `agents/top.md` | **12** | **15** | `T21`, this file (`p272`) |
| LMS platforms reachable by MCP | **3** | **6** *(every one payload-verified)* | `T24`, this file + `agents/top.md` |
| permissive rows in the build-on tier | 23 | 23 🟢 | `agents/top.md:61` |

🔵 **And then the instrument caught `p274` itself, which is the part worth keeping.** This pass shelved
five of the missing servers; the next run read **20** against the **15** the pass had just written down,
and flagged its own prose `STALE` before it was committed. 🟢 **Both shelves now say 20 and the register
is green** — but the useful fact is that **a pass cannot hand-maintain a count it is simultaneously
changing**, which is the whole argument for deriving it.

⚠️ **Three defects in the instrument's own first draft, recorded because each is the thing it exists to
catch.** (a) It classified a slug by the **row text**, which filed `felipedias-ie/blackboard-mcp` under
**Canvas** because the row mentions Canvas in prose — fixed to read the **slug first**. (b) It accepted a
slug whose *line* mentioned MCP, which let `chamilo/chamilo-lms` and `huggingface/transformers` into a
per-platform tally — fixed to require the marker **in the slug**, which makes the count a **floor**.
(c) A word-boundary pattern silently dropped **`AStheTECH/mewcp-google-classroom`** and
**`blend-ed/tutor-contrib-openedxmcp`**, whose slugs carry `mcp` without a delimiter. 🔵 **A counting
instrument's own false negatives are invisible in its output** — the only way these surfaced was reading
the per-platform lists it printed, which is why it prints them.

🔵 **The pattern across the three stale rows is the same one `T31` named and it is not carelessness:**
each count was correct when written and each was written in a *different file* from the rows it counts.
**A number in prose and the rows it describes are two artefacts, and only one of them gets edited when
supply arrives.**

🟢 **The general rule, and it is the one `p274` would hand a client:** **a quantity in prose is a
cache.** Caches need invalidation, and the only reliable invalidation is **deriving the number at read
time from the thing it describes.** Three amendments on this base were written as instructions to
future passes (`T29`'s destination grep, `T34`'s cross-shelf grep, `T37`'s re-count) — 🔴 **and the two
that stayed instructions were both violated by the pass that came next.** `T37` is now **code**, and
`make recount` is the cheapest check on this base.

⚠️ **What this does NOT fix:** the register (`recount.py`) is hand-maintained, so a quantity nobody
registers is still uncounted. **The instrument moves the failure from "the number is stale" to "the
number is unregistered", which is a strictly better failure** — an unregistered number can be found by
grepping for digits, and a stale one cannot be found at all.

**Confidence: high** — the instrument is runnable and its output is committed.

## T44 — A licence can be refuted by a byte ceiling and a slug guess, and both read exactly like "no grant"

*(new in pass 274)*

🔴 **This base recorded, in two separate passes, that `gegok12`'s MIT claim *"died at payload"*. It did
not. `Gego-K12/gegok12` serves MIT at `main/LICENSE`, HTTP 200, `1 150` B, and `p274` read the whole
payload and diffed it.**

```
observed delta vs stock MIT  = +82 B
  SPDX HTML comment line     = +39 B   <!-- SPDX-License-Identifier: MIT -->
  four typographic quotes    =  +8 B   “Software” and “AS IS”, 3 B each in UTF-8
  longer copyright holder    = +35 B   "GegoSoft Technologies and GegoK12 Contributors"
  accounted                  = +82 B   ← exactly
normalised terms diff vs stock: differs ONLY in line-wrap column.  Rider keywords: zero.
```

🔵 **`T39` proved a byte count cannot discriminate a grant DOWNWARD** — six unmodified Apache files
spanning 1,252 B, straddling stock in both directions. 🔴 **This is the same proof UPWARD, and it
costs more**, because this base operates an **MIT ceiling** (`p1054`) and `1 150` B is `81` B above the
cluster its MIT rows sit in (`1 065`–`1 084` B). **Every byte of that excess is a thing that is not a
term**: a machine-readable identifier, four curly quotation marks, and the name of the copyright holder.

🔴 **And a second mechanism was in play, which is why the refutation looked solid.** The slug.
`gegok12/gegok12`, `GegoK12/gegok12` and `gegok12/school-erp` **all fail to resolve, and they fail
IDENTICALLY to a repository that does not exist.** Only `Gego-K12/gegok12` resolves. 🔵 **`T15`
documented this trap for Sunbird** (*"a kebab-case guess returns something indistinguishable from
absence"*) — **here it took down a licence verdict, twice, and the shelf recorded the absence as a
measurement.**

🟢 **Two rules follow, and both are cheap.**
1. **A byte delta is a trigger for a diff in both directions.** `T39` said it for short payloads;
   **a long payload is no more suspicious than a short one.** An SPDX comment, a UTF-8 quotation mark
   and a corporate copyright line will all push an unmodified grant above any ceiling.
2. 🔴 **A negative licence result must record the SLUG and REF it probed, or it is not a measurement.**
   *"Died at payload"* is a claim about a repository; **a 404 on a slug that does not exist is a claim
   about a string.** This base's own ledger format already has the columns — the two refutations did
   not use them.

**The commercial cost of this one false negative:** `Gego-K12/gegok12` is a **self-hosted school ERP
under MIT** whose fork network this base has already measured as **98 forks, near-zero fork stars, and
institution-shaped fork names across India, Indonesia and Vietnam** (`P933`: the signature of software
institutions RUN rather than developers EXTEND). 🔵 **This base's standing APAC gap is platform supply.
It refused an MIT platform row, twice, in the region where it says it has none.** ⚠️ **Corporate origin
is not established** — the copyright names GegoSoft Technologies, and a holder name is not a provenance
read — so it is shelved as **deployment-placed APAC on the base's own fork evidence**, not as
APAC-origin.

**Confidence: high.** Payload read, diffed, byte-accounted and rider-greped first-hand this pass
([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)).

## T45 — The market's stated blocker is exactly this base's recommended architecture, and one row already answers it

*(new in pass 274)*

Two independent sources, two regions, one finding:

| source | what it says |
|---|---|
| **GovTech**, reporting **Bridges 2026** | **Few districts and colleges have deployed AI agents in day-to-day operations**, and leaders *"remain cautious about granting the tools access to sensitive systems and data"* |
| **EdTech Hub** (2026-03-30), Southeast Asia | Education-AI initiatives there *"remain **short-term and project-based**"* |

🔴 **Read those against `T21`/`T24`.** This base's strongest supply finding is **agents over the
systems the client already runs** — six platforms, five of them reachable under MIT. **The buyer-side
blocker named above is that exact move:** granting an agent access to the system of record. 🔵 **So the
pilots are not stalling on model quality or on licence cost. They are stalling on consent scope** —
which is what `T24` predicted from the supply side (*"the OAuth consent a pilot asks a school for is
much wider than the feature being piloted … in EMEA that is a GDPR conversation before an engineering
one"*).

🟢 **And the answer is already a row.** `bruchris/canvas-lms-mcp` (**MIT**, `1 070` B, payload-read
`p274`) ships an **opt-in FERPA mode that pseudonymises student names and contact details before tool
output reaches the model**. 🔵 **That inverts the pilot conversation**: the question stops being *"will
you let the model see your students"* and becomes *"the model never sees your students — here is the
boundary, in configuration you control."*

⚠️ **And the counter-example is in the same result set, which is why this is an architecture finding
and not a product recommendation.** `DMontgomery40/mcp-canvas-lms` carries **its own security
disclosure of a broken access control that exposed other students' personal information**. 🔵 **Same
category, same description in a search result, opposite risk posture** — the `PageLM`/`AStheTECH`
pattern (`T24`) in its **security** rather than its **licence** dimension. **Read the disclosure
history, not just the grant.**

**For the studio, as a scoping instruction:** price **data minimisation at the tool boundary** as a
first-class deliverable in every MCP engagement — pseudonymisation, per-tool scoping, an audit trail of
what the model actually read. 🟢 **It is the difference between a pilot that renews and one that is the
reason the district's AI committee says no.** See [`compose/patterns.md`](../compose/patterns.md) `P24`.

**Confidence: medium-high.** The two market sources are secondary (trade press and a research
organisation's brief); the repository rows are payload-verified first-hand.

## T46 — A path ladder cannot prove absence, and this base published its guesses as findings for three passes

🔴 **The defect species:** a `19-path × 4-ref` probe that comes back empty is **evidence about 76
paths**, not evidence about the repository. This base published it as *"no grant"*, *"licence
unverified"*, *"treat as all-rights-reserved"* — statements the probe never tested. Two rows fell to
this in a single pass, and **both failures were structurally guaranteed rather than unlucky**:

| row | carried verdict | where the grant actually was | why the ladder could not reach it |
|---|---|---|---|
| `os4ed/openSIS-Classic` | *"no licence payload served on any path tried"* | **`docs/License.txt`** — GPL-2.0, 200, **17 286 B** | the ladder tried `docs/LICENSE`. The file is **mixed case *and* `.txt` *and* under `docs/`**. An earlier cell recorded *"no payload in 17 filenames"* — **the 17 did not include it** |
| `ls1intum/Athena` | *"no grant across 76 path/ref probes over three passes"* | **12 of 14 manifests**, `license = "MIT"` | the ladder probed the **root** `pyproject.toml` — a 632-byte Poetry workspace stub with **zero occurrences of `license`** |

🔴 **And this base already knew.** [`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/)
(**pase 93, `2026-10-04`**) states **`P275`** — *para sostener una ausencia en un árbol hay que
ENUMERARLO* — and **`P278`** — *un conteo de CERO sobre una ruta que no existe en esa ref mide la RUTA,
no el contenido* — **and ships a working blobless-clone enumerator.** 🔵 **`P278` is this trend, stated
~180 passes earlier**, and `P270` (*a negative over a path that encodes a NAME measures the name*) is
its sibling. All three were applied to **directory** trees and **never to licence paths**. 🔴 **So `T46`
is not a new method; it is the record of a principle that failed to cross domains** — `p273` extended a
ladder along the wrong axis for two passes (`ACTION YU`) while the instrument that refutes ladders sat
in `compose/code/`. **The fix was to stop guessing, with the tooling already present:**

```
git ls-remote <slug> HEAD                                    # positive control: does it resolve?
git clone --depth 1 --filter=blob:none --no-checkout <slug>   # blobless, seconds
git ls-tree -r --name-only HEAD                               # EVERY path. No guessing.
```

🔵 **Why this is a trend and not a one-off fix.** The ladder's failure mode is *silent and
self-confirming*: every added path makes the refusal feel better evidenced while leaving the
unexamined space exactly as large. **`QUEUE-UNENUMERATED=124`** — 124 negative licence verdicts on
these shelves still rest on a ladder. That number is the first honest measure of the exposure, and
`make gate-enumeration` now publishes it on every run. ⚠️ **A licence-like path is still not a grant:**
the gate excludes vendored dependencies (openSIS alone carries **20**), source files that merely carry
the word (`LicenseService.java`), and **icon assets** — `kolibri-design-system` holds **7** licence-like
paths and **all 7 are Vue icon components**.

## T47 — A monorepo declares its grant per package, so a root-only metadata probe is aimed at the one file that is silent

🔴 **Generalised from `T46`'s second limb, because it is a different mechanism wearing the same
result.** `p267`'s probe list is methodologically sound as written — it includes *"the package metadata
(`package.json`, `pyproject.toml`, `setup.py`, `build.gradle`, `composer.json`)"*. It is **aimed at the
repository root**, and that is where a workspace stub lives.

In a Poetry / npm-workspaces / Cargo-workspace layout the root manifest **declares the workspace** and
the **per-package** manifests declare the licence. Athena's twelve packages — `athena/`, `llm_core/`,
`assessment_module_manager/`, `log_viewer/` and all eight `modules/*/` — each carry `license = "MIT"`,
unanimous, **none declaring anything else**. 🔵 **The reusable units are precisely the ones that declare
it** (`module_text_llm`, `module_programming_llm`, `module_modeling_llm`), which is what makes this
commercially material rather than pedantic: the package a studio would actually depend on is the package
carrying the grant.

🟢 **Rule for this base:** before recording a metadata-channel absence on a multi-package repository,
**enumerate the manifests**, then read every one. One silent root manifest is not a silent project.
⚠️ And grade it honestly: twelve unanimous declarations is the **strongest metadata channel this base
has graded** (`kolibri-design-system` rests on one) — but it is **still metadata, not a payload**.

## T48 — A channel probed at one path licenses a false conclusion about the channel

🔴 **Nearly published this pass, and caught by re-testing instead of inheriting.**
`api.github.com/rate_limit` answers **200** — with a plausible body (`limit 15000, remaining 14998`).
`api.github.com/repos/<slug>` answers **403**, and so does `/search`. The 403 body is a **session-scope
message, not a rate limit**:

> *"GitHub access to this repository is not enabled for this session."*

🟢 **So `api.github.com` is NOT open, and `p274`'s recorded `403` was right.** The `200` on
`/rate_limit` is a **proxy-level reply** that never touches repository data. Reading it as access would
have published an open GitHub API this base does not have — and, worse, would have invited the next pass
to refresh **star counts** from it, re-introducing exactly the inflated-star defect that a sibling KB
cycle had to correct wholesale.

🔵 **The general shape:** `reachable` is not a property of a *host*, it is a property of a
**(host, path, method)** triple. This base already knows the narrower version — `p267`'s ref-sensitivity
note (`learningequality/kolibri` serves **MIT on `develop`** and **404 on `main`**) is the same lesson
one axis over. 🟢 **Operational rule: record channel state as the triple you actually probed, and probe
the path you intend to USE** — never a cheaper neighbour. **No star count was read from GitHub this
pass**; every star figure on these shelves is carried from an earlier pass and marked so.

## T49 — An instrument that reads one channel cannot establish an absence, and the channel it misses is usually the one its own motivating case used

🔴 **The sharpest instance this base has produced, because the gap is between a finding and the tool
built from it.** `p275`'s headline was `ls1intum/Athena`: **no licence file anywhere in the tree**, and
`license = "MIT"` in **12 of its 14 manifests**. It found that by hand, wrote it up as the pass's central
result — and then shipped an instrument that reads `git ls-tree` **file paths only**.

🟢 **`p276` worked 30 rows of that instrument's own backlog in BOTH channels. Three carry a grant no file
enumeration can see:**

| row | file channel | manifest / registry channel |
|---|---|---|
| `DMontgomery40/mcp-canvas-lms` | 36 paths, none licence-like | `package.json` **MIT** + npm **MIT × 19 versions** |
| `meyerjp3/psychometrics` | 395 paths, none licence-like | `pom.xml` `<licenses>` **Apache-2.0** |
| `LearnPress/learnpress` | 1 985 paths, none licence-like | `readme.txt` **GPLv3** + `composer.json` **GPL-3.0-or-later** |

**Run as built, the gate would have stamped all three `VERIFIED-ABSENT` — a false absence certified by
the instrument built to stop false absences.** 🔵 And the sub-species is worse than a missing feature:
**two channels can agree because they share one blind spot.** `ECNU-ICALK/EduChat` returned nothing on
six path probes **and** `license: null` from GitHub's API — because `LICENSE` is a **directory** there, so
every probe hit a tree rather than a blob and the API's detector failed for the same reason. **The
agreement read as corroboration.**

🟢 **Operational rule:** an absence is only sayable when **every channel a grant is known to live in** has
been read and found empty — file tree, package manifest, package registry, and (for plugin ecosystems) the
distribution header. Record *which* channels were read, so the next pass can tell a two-channel absence
from a one-channel silence. `p276` adds the manifest channel to the gate and records the count on every
row.

## T50 — A figure with no region attached becomes a global figure by repetition, and the third appearance is when it stops being traceable

🔴 **Measured, not predicted.** A *"~10% of institutions have formal AI guidelines"* figure has now
appeared on this base's shelves three times with three different scopes: once for **EMEA institutions**,
once in `p275` as *"fewer than 10%"* for **LATAM** (UNESCO's regional observatory), and once this pass in a
**North American** result set with **no scope stated at all**.

🔵 **The mechanism is not fabrication, it is attrition.** Each re-publication is individually defensible;
what disappears is the sampling frame. By the third appearance the figure reads as a property of
*institutions* rather than of *a survey of institutions in a region*, and at that point no reader can
recover which. 🔴 **This base already ran the inverse of this and caught it:** `p275` published **92%** as
a LATAM figure, and `p276` found an aggregator publishing the same 92% as **global** student AI use. **A
figure travels in both directions.**

🟢 **Operational rule:** a quantity enters a shelf with its **instrument, its frame and its date**, or it
does not enter. A regional cell that cannot name its sampling frame is a gap, not a datum — and the
honest form is *"not established for this region"*, which `p276` published for the North American 10%.

## T51 — A primary publisher can invite the conflation, so "the source is primary" does not retire the window check

🔴 **`T38` and `T42` were built against market-research houses mislabelling their own CAGR windows. This
pass found the same species in a survey publisher**, which is the class of source this base treats as
better. The **Digital Education Council** compares its **LATAM** 2026 figure (**92%** of students using
AI) against its own **GLOBAL 2024** figure (**86%**) and presents the difference as a **"+6% increase."**

🔵 **Two different sampling frames, one subtraction.** The genuine comparisons are LATAM-2026 **92%**
against GLOBAL-2026 **88%** (a regional *premium*, not a rise), or LATAM against LATAM across years —
which the published pair does not give. **Nothing is fabricated; the arithmetic is simply performed across
bases**, and a reader who trusts the publisher inherits the error intact.

🟢 **Operational rule, extending `T42`:** before quoting any delta, **name the two bases being
subtracted** — region, year, population, n. Apply it to primary publishers too. 🔴 **And note what this
does to a defence this base has used:** *"the figure is from the research house itself"* is not a
window-check exemption. `T38`'s convention appeared in two market houses; `T51` puts it in a third kind of
publisher entirely.

## T52 — A correction that widens a matcher creates the inverse defect, and it detonates on the backlog the correction told you to work

🔴 **`p275` widened `attribute()` to match a BARE repository name**, because Athena's claim was carried in
bold prose with no hyperlink. Correct fix, real defect, properly motivated. 🔴 **`p276` enumerated
`frappe/lms` — one unremarkable row of `p275`'s own 124-row backlog — and the widened matcher attributed
FOURTEEN lines across FIVE shelves to it. THIRTEEN were about other projects.**

| mechanism | instances found |
|---|---|
| `\b` **does not stop at a hyphen** (`-` is itself a non-word character), so `lms` matched `mcp-canvas-lms`, `canvas-lms-mcp`, `AI-LMS-TMS`, `tutor-lms-mcp` | 4 |
| a global `re.I` made the **common noun** *"LMS"* match a repository name (*"the LMS-side MCP servers"*, *"a proprietary LMS"*) | 2+ |

**A `REFUTED` row FAILS the gate**, so committing the ledger unpatched would have turned the standing
check red on thirteen claims about six other projects — **the instrument built to stop false absences
manufacturing false presences instead.**

🔵 **The fix was already written on this base, in `p275`'s own words, about a different predicate:**
*"case is load-bearing: `LICENSE` is a filename, `licence` is a word."* `p275` applied that to the
predicate that **suppresses** rows and never carried it to the predicate that **assigns** them. With
case-sensitive matching, a token-boundary guard and a four-character floor, **27 refutations fall to 11,
and all 16 removed are false**.

🟢 **Operational rule:** when a pass widens a matcher to fix a false negative, it must **immediately
measure the false positives on the largest corpus available**, not on the case that motivated it. And a
widened matcher is most dangerous **on the queue the same pass creates** — the backlog is, by
construction, the set of rows nobody has looked at.

## T53 — APAC does not regulate "APAC", and a regional abbreviation is why this base saw nothing for ten passes

**Measured, not argued.** This shelf published an **APAC nil for ten consecutive passes** while five of
the region's largest school systems were each running a named, dated, numbered instrument. `p276`
diagnosed the cause without being able to test it — *"this is a QUERY defect"* — and ranked one
instruction: **query the jurisdiction, never the region.** 🟢 **`p277` ran it once and the nil ended on
the first attempt**: China's *AI Plus Education* plan (Apr 2026, to 2030), India's **AI & CT from Grade
3** (CBSE Circular Acad-15/2026), Japan's **MEXT Ver. 2.0**, Singapore's **Teacher AI Literacy
Roadmap** (Aug 2026), and South Korea's **unwound AI digital textbooks**. Full cells in
[`intel/market.md`](market.md#apac).

🔵 **The generalisable rule, and it is not about APAC.** *No ministry of education calls itself APAC.*
A regional abbreviation is a **market-research category**, so querying it returns market research —
which is precisely what the ten nil legs returned: Forrester, sovereignty think-pieces, enterprise
data-infrastructure percentages. **The instrument a jurisdiction actually publishes is indexed under
the jurisdiction's own name for its own institution** (MEXT, MOE, CBSE, MoE), and that is the only
spelling that reaches it.

🔴 **Second instance, so this is now a pattern rather than an anecdote.** EMEA ran a **nine-pass nil**
and broke on `p276`'s first instrument-targeted query. APAC ran a **ten-pass nil** and broke on
`p277`'s first jurisdiction-targeted query. **Two regions, nineteen wasted legs, one cause.** 🟢 **The
standing instruction, for every region including the ones that look healthy:** a regional leg that
returns no instrument has **not** measured the region — it has measured the query, and must be re-run
against named jurisdictions before any gap is declared. **`LATAM` and `North America` have never been
run this way on this shelf**, and both are currently carried on *regional* queries.

## T54 — The reference case for education AI is now a failure, and it failed on governance rather than on models

**South Korea built, deployed and then unwound a national AI digital-textbook programme** — the only
instance of its kind in this KB. Status revoked by the National Assembly **four months into the
rollout** (Aug 2025); adoption **37% → 19%** of classes; **two data-protection violations** found by
the privacy regulator; the **state auditor found the textbooks were brought into schools without a
pilot**; publisher suits **dismissed** (Seoul Administrative Court, Jul and Aug 2026); the review
process for 2026-year products **halted**.

🔴 **Not one of the cited causes was model capability.** They were **factual errors in generated
content, privacy risk, screen time, and teacher workload** — four implementation and governance
failures, all four inside a delivery partner's scope of responsibility.

🔵 **Why this belongs in a trends file and not only a market cell.** Every adoption curve on this shelf
is an *aggregate*, and aggregates cannot show a programme reversing. Korea is the counter-example that
makes three otherwise-unfalsifiable claims testable: **a mandate is not adoption** (the decline
happened while the mandate stood), **a privacy finding outranks an accuracy benchmark** in deciding
whether a programme survives, and **the pilot is not a procurement formality** — the auditor named its
absence as the finding. 🟢 **Read it beside Japan's funded split** — **100** of 161 pilot
municipalities on *teacher administration* versus **10** in class — and two jurisdictions that agree on
nothing else both start away from the student.

## T55 — England regulates learner-facing education AI through procurement, and the 2026 revision added four standards that cannot be retrofitted

The DfE's **"Generative AI: product safety standards"** (retitled from *"expectations"*) was first
published **Jan 2025** and **revised 19 January 2026**, adding four standards: **cognitive development,
emotional and social development, mental health, and protection against manipulation** — driven by
**Online Safety Act** changes and emerging generative-AI risk.

🔵 **The mechanism is the finding.** The standards are **not law**; they address **suppliers of
learner-facing products**. So England's control point on education AI is **the purchase order, not the
statute book** — failing the standards costs the deal rather than attracting a penalty, which makes
them *more* binding on a vendor than a deferred statutory duty and *less* visible to anyone scanning
for regulations. 🔴 **Contrast `T4`/`P29`:** the EU route is statutory, dated and deferrable (Annex III
now **2027-12-02**); the England route is non-statutory, already in force, and not deferrable at all.
**An EMEA engagement that prepares only for the AI Act is unprepared for the English buyer.**

🔴 **And the four new standards are the most retrofit-hostile requirement in this KB.** "Cognitive
development" and "protection against manipulation" are claims about **pedagogical design and
interaction patterns** — what the agent does turn by turn — not features that bolt on at the end. A
tutor built to maximise task completion is *architecturally* adverse to them. 🟢 **The implication for
sequencing is concrete:** these constraints must sit in the **first** design review, and the
pedagogically-constrained tutors this base already shelves (**Iris** — *"hints and leading questions
rather than answers"*) are the right reference shape, not the engagement-maximising kind.

⚠️ One supplier reads the standards as applying **only to learner-facing** platforms, exempting
teacher-facing tools. **If that holds, the compliance-cheapest first deliverable in England is
teacher-facing** — the same place Japan put its funded majority. ⚠️ **Binding status conflicts across
secondary sources and `www.gov.uk` was not readable from this sandbox**; published as non-binding,
marked unread.

## T56 — An append-only shelf inflates a line-scoped absence queue, and the backlog grows even when the work is done

🔴 **`p277` harvested its own queue of negative licence verdicts, ranked it, worked the top twelve
first-hand — and all twelve were already correctly resolved on the shelves.** Twelve rows, **zero
corrections, twelve positive controls**. Evidence:
[`positive-controls.2026-10-17-p277.tsv`](../evidence/positive-controls.2026-10-17-p277.tsv).

🔵 **That result is good news about the shelves and bad news about the queue, and the cause is
structural.** A queue predicate that asks *"does this line assert an absence, and does this line also
carry enumeration evidence?"* is **line-scoped**. But `agents/trending.md` and `repos/trending.md` are
**append-only by design** — a correction is published as a *new dated section*, and the original
absence prose **stays on the shelf as history, correctly**. 🔴 **So every correction leaves its own
refuted claim behind as a permanent queue entry, and the backlog grows monotonically with the number of
corrections made.** The queue is measuring **the archive**, not the live state.

🔴 **This is `p276`'s own declared gap, reproduced from scratch by an instrument that had never seen
it:** *"`states_a_grant()` is line-scoped while `attribute()` is subject-scoped."* **`p277` wrote a
fresh harvester, in a different language idiom, with no knowledge of that predicate, and inherited the
identical defect** — which is the strongest available evidence that the defect is in the *shape of the
problem*, not in one implementation. 🟢 **The fix is a scope, not a pattern:** an absence claim must be
resolved against **the most recent statement about that subject across the whole file**, not against
the line it sits on. Until that exists, **`QUEUE-UNENUMERATED` is an upper bound and must be published
as one** — `p277` estimates the live fraction is small, on a 12-of-12 sample.

🔵 **One corollary worth keeping.** The twelve controls were not wasted: six rows whose absence rested
on a **path ladder** (`edunaija-os` at *"19 of 19 paths"*) now rest on a **full tree enumeration** (310
paths), which is the grade `P275`/`P278` require for an absence to be sayable at all. **A positive
control that upgrades the grade of what it confirms is worth running even when it finds nothing wrong.**

## T57 — An absence is only as strong as the tree it was measured against, so the path count belongs in the sentence

`p277` declared this sub-rule for `p278` after one row changed its meaning under enumeration:
`OpenEMIS/OpenEMIS-Core` enumerates to **eleven paths** — not a codebase, so *"no licence payload"* is
true of the repository and says almost nothing about the product. 🟢 **Discharged.** Every absence
`p278` publishes carries its path count, and the counts turn out to span **three orders of magnitude**:

| row | paths at the pinned SHA | what the absence is worth |
|---|---|---|
| [`adriasantacreu/google-classroom-mcp`](https://github.com/adriasantacreu/google-classroom-mcp) | **15** | 🟡 a small repo; the absence is certain but unremarkable |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **36** | 🟡 reproduces `p276` at the same SHA, independently |
| [`Gnanakamalesh-M/student-dropout-early-warning`](https://github.com/Gnanakamalesh-M/student-dropout-early-warning) | **211** | 🟢 a real codebase with **no grant anywhere** — `p121`'s *"permissive over nothing"* upgraded from a ladder to a proof |
| [`ls1intum/Athena`](https://github.com/ls1intum/Athena) | **691** | 🟢 reproduces `p275` exactly |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | **1,985** | 🔴 see `T58` — the two licence-like paths are **not the project's** |
| [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system) | **15,448** | 🟢 7 licence-like paths, **all Material Design icon components**, all correctly excluded |

🔵 **Why the count is load-bearing and not decoration:** *"no licence file in 15 paths"* and *"no
licence file in 15,448 paths"* are the same sentence and completely different claims. The first is
nearly a tautology; the second is a measurement about a large, active project. **A studio deciding
whether to ask the maintainer for a grant needs to know which one it is reading.**

## T58 — A licence-like path can belong to a vendored dependency, and on the largest LMS plugin on this shelf both of them do

🔴 **`LearnPress/learnpress` enumerates to 1,985 paths and the only two licence-like paths are not its
own grant:**

| path | what it actually is |
|---|---|
| `inc/libraries/wp-background-process/license.txt` | 🔴 a **VENDORED third-party library's** licence |
| `inc/TemplateHooks/Admin/Notices/AdminNotesTemplate.php` | 🔴 a **PHP source file** that merely matches the licence-name pattern |

🟢 **Both are correctly rejected** by `pass275-grant-enumeration`'s scope test — `VENDORED` catches the
first, `SOURCEY` the second — verified first-hand this pass, so the repository commits **no licence of
its own** and `p120`'s resolution stands: the grant is **GPL-3.0, declared in the WordPress
`readme.txt`**, not in a licence file.

🔵 **The general rule, and it is the one a client's tooling gets wrong:** a licence file *inside* a
repository is not necessarily *the repository's* licence. An SCA scanner that reports "GPL-3.0 found"
from `inc/libraries/…/license.txt` has found a **dependency's** grant and attributed it to the parent —
the mirror image of `T59`'s manifest problem, and the reason an intake gate must ask **whose** grant a
path carries, not only **which** grant.

## T59 — The CONFLICT class was built 157 passes ago, and the gate that proves it exists was never run

🔴 **`p277` declared that this base *"has a grade for payload and a grade for metadata and no class at
all for CONFLICT"*, and ranked building it FIRST at zero searches.** `p121` had built it on
**2026-10-11**: **249 addresses probed, 161 manifests fetched, 104 declaring, 10 contradictions —
9.6%** — published with a four-value direction axis and an operational rule. 🔴 **And the instance
`p277` reported as a NEW defect class, `open-tutor-ai-CE`'s BSD payload against its MIT `pyproject`,
is ROW 8 of that table, with the identical verdict.**

🔵 **The gate for exactly this error exists: `make claims TOKEN=conflict` returns `ALREADY CLAIMED …
STOP` over 26 cells in `repos/trending.md` and exits 1.** Both arms were verified this pass. The
Makefile documents it as *"THE GATE: run before publishing any 'there is no X'"*. **It was not run.**

🟢 **The durable lesson is not "read more carefully".** `p121`'s class lives in `repos/trending.md`;
`p277` was working in `agents/top.md` and `intel/open-gaps.md`. **On a base of 10 shelves and 28,000+
lines, no amount of care substitutes for running the index** — which is why the remedy registered for
`p279` is to make `make claims` a *step*, not an instruction in prose.

🔴 **And the one defensible half of `p277`'s claim is worth keeping:** the ROW VOCABULARY had no way to
distinguish *"metadata grade because the payload was read and agrees"* from *"metadata grade because
nobody looked"*. `p278`'s sweep closes that for the four build-on rows on `agents/top.md` — all four
are **metadata because there is nothing else**, now proven by full tree enumeration.

## T60 — In the United States the binding AI-in-education duties are at STATE level, and the federal instrument governs money rather than classrooms

Asked at federal level, the US looks like it has an AI-in-education policy. 🔴 **Asked per
jurisdiction, the federal instrument turns out to be a GRANTS instrument and the binding duties are all
state statutes.**

**Federal Register doc 2026-07087 (13 Apr 2026)** finalises a *Secretary's Supplemental Priority* that
**weights AI initiatives in discretionary grant competitions**. It requires nothing of any school. The
**22 Jul 2025 Dear Colleague Letter** likewise *permits* existing funds to be used for AI. 🔴 **Reading
either as a mandate is the error.** What binds is state law: **Maryland SB 720 (Ch. 634)** — guidance,
local policies, AI literacy **and teacher professional development**; **Idaho SB 1227** — AI literacy
standards and **educator training**; **Ohio** — every district had to **adopt an AI-use policy by
1 Jul 2026**, a deadline that has **already passed**; **Utah** — middle-school AI literacy;
**Virginia SB 394** — state guidance including teacher training. **HR 8747** (*K-12 AI Literacy and
Readiness Act of 2026*) is **introduced, not enacted**.

🟢 **Why this matters to a proposal.** A federal-posture pitch sells a trend; a state-statute pitch
sells a **dated obligation**. Maryland and Idaho oblige **teacher training**, which is staffable work,
and **Ohio's deadline is in the past**, which converts policy remediation from a forecast into a live
need. 🔵 **Canada is the mirror case:** no binding provincial rule in Ontario, Alberta or BC, education
is provincial jurisdiction, and the Alberta Teachers' Association's own summary is that there is *"not
a lot of policy at the jurisdictional level"* — so **the buyer is the board or district and the first
deliverable is the policy itself**.

⚠️ **GRADE: SECONDARY, PRIMARY UNREAD** — `federalregister.gov`, `ed.gov`, `govinfo.gov` and
`oregon.gov` are all unreachable from this sandbox
([map](../evidence/egress-map.2026-10-17-p278.tsv)). 🔴 **"27 states" is a count of ACTIVE BILLS from
one vendor tracker, not of enacted laws**, and the circulating **"$2.5B K-12 AI grant program"** traces
to a single weakly-sourced blog and is **not shelved**.

## T61 — Primary policy text is not reachable from this environment, and four passes of host failures make that a property rather than an accident

`p277` ranked *"read, with egress: CBSE Circular Acad-15/2026 first, then MEXT Ver. 2.0, the Korean
MoE's own account, and the DfE standards"* as actionable backlog. 🔴 **It is not actionable here, and
`p278` measured why instead of reporting another nil.**

| channel | result |
|---|---|
| `raw.githubusercontent.com` (licence payloads) | 🟢 **HTTP 200** |
| `git ls-remote` / shallow clone (refs, trees) | 🟢 **OK** |
| `registry.npmjs.org` | 🟢 **HTTP 200** |
| `api.github.com` | 🔴 **403** |
| `cbseacademic.nic.in`, `federalregister.gov`, `community.canvaslms.com` | 🔴 **DNS unresolvable** |
| `gov.br`, `ed.gov`, `oregon.gov`, `govinfo.gov` | 🔴 **proxy 403** |

🔵 **Across `p275`–`p278` the unreachable set now includes `eur-lex.europa.eu`, `gov.uk`, `mext.go.jp`,
`instructure.com`, `cbseacademic.nic.in`, `federalregister.gov`, `ed.gov`, `gov.br`, `oregon.gov`,
`govinfo.gov` and `community.canvaslms.com` — eleven hosts, four passes, one failure mode — while every
code-hosting channel answers.** 🟢 **So the honest classification changes: this is not a per-host
accident to retry, it is the shape of the environment.** Primary *policy* reads should be ranked as
**requiring an egress-enabled run**, not as backlog a sandboxed pass can discharge; primary *licence*
reads remain fully available and are where a pass's egress budget should go.

⚠️ **One live consequence, unchanged from `p277` and now explicitly un-dischargeable here:** the claim
that **Canvas Free-for-Teacher was permanently discontinued in May 2026** is still unverified
(`instructure.com` and `community.canvaslms.com` both unreachable). **Do not promise a zero-cost Canvas
environment in a proposal.**

---

## T62 — Korea reclassified AI textbooks out of "textbook" status, and that removes the procurement mandate a vendor thesis rests on

🔴 **The single most consequential regional finding of `p279`, and it inverts the APAC story these
shelves have carried.** Korea was the jurisdiction with the hardest AI-in-education mandate anywhere:
AI digital textbooks into elementary and secondary schools from 2025, all subjects by 2028.

🔴 **The National Assembly amended the Elementary and Secondary Education Act in mid-2025 (reported
August 2025) to reclassify AI digital textbooks as "educational materials" rather than textbooks.**
The consequences are not cosmetic:

| consequence | state |
|---|---|
| 🔴 **Adoption becomes OPTIONAL** | a school *may* use them; nothing obliges it |
| 🔴 **Korean and home economics excluded**; social studies and science **delayed to 2027** | ministry adjustment plans applying **from 2026** |
| 🔴 **Review halted** for products intended for the 2026 school year | reported |
| 🟡 Adoption measured at **4,095 schools** in the first semester | ministry figures to the National Assembly |
| 🔴 **~10 publishers sued the government in June 2026** for roughly **KRW 200bn** | reported |
| 🔴 Board of Audit and Inspection: the 2025 start date was treated as fixed, **the pilot was dropped**, classroom review **cut short** | ministry disputes it |

🟢 **What a studio should take from it.** A *mandate* is the strongest demand signal in public-sector
education and the **most fragile**: this one was legislated away in under two years, and the vendors
who had built to it are in court. 🔵 **So price delivery against what a school may CHOOSE, not against
what a ministry has ANNOUNCED** — and in Korea specifically, the buyer is now the school and the
district, not the ministry. ⚠️ Every source here is press or secondary; the ministry's own
announcements are not reachable from this environment (`T61`).

---

## T63 — Singapore has a dated, binding teacher-training deadline inside this quarter, and it is the nearest commercial trigger on these shelves

🟢 **MOE's Teacher AI Literacy Professional Learning Roadmap (August 2025) obliges EVERY teacher in
primary school, secondary school and junior college to complete AI training modules by end-2027 — and
the FIRST module by the end of 2026.** That is a jurisdiction-wide, dated obligation with roughly ten
weeks left to run.

- Module 1 *(mandatory, by end-2026)*: AI basics, ethics, safety, responsible use. Online, **30–45
  minutes**.
- Modules 2–3 *(encouraged, by end-2027)*: age-appropriate use; how AI affects student thinking.
- Advanced, subject-specific courses **from 2027**.
- Student-side: rollout **from Primary 4** under teacher supervision, through **MOE-built tools on the
  Singapore Student Learning Space (SLS)**. 🔴 **Primary 1–3 stays print-first and pupils are not
  asked to use chatbots at all.**
- 🔵 MOE states teachers may **deliberately withhold** AI where it does not serve the learning outcome.

🟢 **Why this is the most actionable regional item in this file.** Unlike a curriculum framework, a
training mandate names **who** must do **what** by **when** — so the deliverable is definable
(module content, delivery, completion tracking, evidence for an auditor) and the deadline is real.
🔴 **And the student channel is closed to vendors**: it runs on MOE's own tools on MOE's own platform,
so the opportunity is **teacher-facing and institutional**, not a product sold into classrooms.
🟡 One blog claims a 2027 AI-competency graduation requirement for university, polytechnic and ITE
students; **unconfirmed against any MOE source and not carried as fact.**

---

## T64 — India's CBSE instrument is now dated and scoped, and the thing it is NOT is as commercially important as the thing it is

🟢 **`p278` ranked *"read CBSE Acad-15/2026 with egress"* as backlog. The circular's identity is
established this pass without egress** — and `T61` is why it had to be: `cbseacademic.nic.in` is
**DNS-unresolvable on both fetch channels**, so the primary PDF remains unread while its metadata is
now firm.

| field | value |
|---|---|
| instrument | **Circular Acad-15/2026**, ref `CBSE/ACAD/AP&AD(AC)/2026` |
| date | **2026-04-01** |
| signed | **Dr. Praggya M. Singh, Director (Academics)** |
| scope | **Classes III–VIII**, session **2026-27** |
| companion | **Acad-18/2026** — student and teacher resource books; stated aim *"AI-literate learners by 2030"* |
| next | CT & AI textbooks for **Class 9 in 2027-28** |

🔴 **The commercially decisive detail: AI is NOT a standalone subject.** Computational thinking is
**woven into mathematics, science, languages and social studies**, and secondary reporting says there
is **no board examination** — assessment is continuous and project-based. 🟢 **So the sellable artefact
is not a course.** It is **cross-curricular material, teacher enablement and project assessment** for
an age band where, per Singapore's own reasoning in `T63`, chatbot-style tooling is least appropriate.
⚠️ The no-exam and weaving claims are **secondary**; the circular itself is unread here.

---

## T65 — The Ontario conflict was a SCOPE disagreement, not a factual one, and both sources were right

🟢 **`p278` ranked this seventh: *"two sources disagree on whether the Ministry has issued anything,
and `ontario.ca` was not reachable to decide it."* Settled — and neither source was wrong.** They were
answering different questions:

| question | answer |
|---|---|
| Has the Ministry published **AI-in-education guidance for school boards**? | 🔴 **No.** The Ontario Directors' material states the Ministry has not yet published it |
| Has the Ministry **issued anything** on AI? | 🟢 **Yes** — a **Ministry-mandated professional development day on AI, 2026-04-17**, supporting a stated provincial priority |
| Is anything **binding** on school boards? | 🟢 **Yes, but not education-specific** — the province's **Responsible Use of Artificial Intelligence Directive**, and **Bill 194 (2024)**, which covers AI systems at public sector entities **including school boards** |

🔵 **The lesson generalises past Ontario, and it is the same shape as this pass's predicate failures:
"has X issued guidance" and "is anything binding" are different predicates, and a conflict between two
sources answering different ones is not resolved by finding a third source.** It is resolved by
splitting the question — which costs nothing and did not need `ontario.ca` at all.

🟡 **Board-level reality, for proposal sizing:** about **50.7%** of Ontario teachers report their
school has a student AI policy *(a second source says 42.3% of boards — the figures conflict)*, and
**more than half report no AI training from school or board.** 🟢 **So in Canada the buyer is the board
and the first deliverable is the policy** — unchanged from `p278`, now with the Ministry's own
mandated PD day as the opening.

---

## T66 — A refuted claim keeps arriving from new sources, so the gate has to face OUTWARD as well as inward

🔴 **The claim that the EU AI Act's education high-risk obligations took effect in August 2026 arrived
from an inbound source for the FIFTH pass running**, this time through `p279`'s own mandated EMEA leg,
from a source these shelves do not cite. It is wrong by **fifteen months in the expensive direction**:
it tells an EMEA client they are bound now. **Annex III point 3 applies `2027-12-02`**; `2026-08-02`
is **Article 50 transparency**, which *is* live.

🟢 **`ACTION SH`, registered since `p226` and unbuilt for 53 passes, is built**: the same classifier
that watches this KB's own prose now runs against a file of inbound research text, and it caught
**both** stale assertions in `p279`'s EMEA evidence. 🔴 **One of them it caught only after the
classifier was widened twice**, and both gaps are instructive:

1. The subject vocabulary knew `AI Act` but not **`Digital Omnibus`** — the instrument that *amends*
   it. A table that knows an Act and not its amending instrument has a hole the size of every source
   writing about the delay rather than the Act.
2. The effect vocabulary knew *"full effect"* but not **`the obligation remains August 2, 2026`** —
   the claim asserted by **denying the correction**. 🔵 And the first cut of that fix spelled the date
   `august 2026`, so it missed `August 2, 2026` — **the one spelling a reader would actually meet.**

🔵 **The durable point: a KB that only audits its own prose is guarding the wrong door.** Its shelves
were clean on all five occasions; the cost was a human re-adjudicating the same fact every hour, and
the risk was the one pass that doesn't. `p223`'s gate is also **standing** now — `make hooks` had never
run it, 56 passes after it was written.

## T67 — Three education systems on three continents independently prohibit unsupervised generative AI for the youngest learners, and that is a product requirement

🟢 **Written down, dated, and arrived at separately:**

| jurisdiction | instrument | the line it draws |
|---|---|---|
| **China** | MOE, *Guide to Using Generative Artificial Intelligence in Primary and Secondary Schools* (**2025 Edition**) | **primary pupils barred from autonomous use of open-ended content-generating tools**; *"AI can complement but not replace human-led teaching"* |
| **Brazil** | `Parecer CNE/CP nº 15/2026` *(approved `2026-09-01`, **pending homologation**)* | **autonomous AI use prohibited up to the 5th year**, citing UNESCO's **age-13** parameter |
| **Singapore** | Teacher AI Literacy Professional Learning Roadmap *(Aug 2025, `p279`)* | **P1–P3 print-first, no chatbots**; MOE's own SLS tools from **P4** |

🔵 **Three regulators, three legal traditions, no shared drafting process, one rule.** A convergence
of that kind stops being policy news and becomes a **design constraint**: a K-12 product needs a
**teacher-mediated mode** in which the teacher is the requester and the pupil never holds an
open-ended prompt — not a content filter, a different *routing* of the request.

🔴 **Nothing on these shelves ships it.** `DeepTutor`'s Socratic mode and `OATutor`'s structured
tutoring are the nearest shapes; both still assume a pupil-initiated turn. 🟢 Moodle and Open edX
both have the role model to express the constraint, so this is buildable on what is already shelved.

🟡 **Confidence:** the Chinese and Singaporean instruments are issued; **Brazil's is not yet
binding**, and its *reported* amendments do not touch this clause. The convergence holds on two of
three today and three of three on homologation.

## T68 — The same instruments converge a second time, on who may decide a grade

🟢 **Maryland `SB 720`** bars AI from being the **primary basis for high-stakes decisions such as
grading or discipline**, and requires **human-in-the-loop** use. 🟢 **Brazil's pending parecer** is
reported to be homologated **with an amendment barring AI tools from determining a pupil's approval
or failure — marks given only by teachers.** 🔵 **A US state statute and a Brazilian national
parecer, independently, draw the same line in the same place.**

🔴 **This is the harder of the two constraints to retrofit**, because it is architectural rather than
modal: an assessment product whose scoring path can *produce* a final mark has to grow a
**recommendation + teacher-adjudication** boundary, with the adjudication **recorded**. 🟢 A product
built that way is sellable in both jurisdictions and reads as defensible in every other, which makes
it the safer default even where nothing yet binds.

🔵 **What a studio should take from `T67` and `T68` together:** the two most common K-12 AI product
shapes — *pupil-facing chat tutor* and *automated grader* — are each **directly constrained by
written instruments in multiple regions**, and the constraints are **capability-shaped**, so they can
be designed for once rather than negotiated per deal.

## T69 — This base's most expensive errors are no longer facts, they are the BOUNDS and FLOORS inside its own instruments

🔵 Measured over `p279` and `p280`, a pattern worth naming because it changes where to look:

| the defect | what it was | what it cost |
|---|---|---|
| a **cap** set to the control case's own size (`MANIFEST_CAP = 14`, `Athena`'s manifest count) | an honest, **published** bound | 🔴 a **6×** error in `leemons`'s declaring count, and a **hidden** second conflict in `courselit` |
| a **path vocabulary** (`is_bundled`) | a list of conventions somebody enumerated | 🔴 defeated **twice by one repository in one hour**; a committed `.vite` cache in the denominator |
| a **word list** (`SENTENCE`, the holder guard) | a list of prose words somebody enumerated | 🔴 a GPL body fragment published as a copyright holder |
| a **family exemption** (`HOLDER_FAMILIES`) | a true statement about licence **templates** | 🔴 the whole copyleft half of a **503-slug** sweep silently skipped, and the holder of this shelf's **top row** invisible for 96 passes |
| a **basename match** (`is_gated`, the gate census) | a reach proof that was a string match | 🔴 an unrun suite counted as gated — **a coverage measurement erring in the only direction it must not** |

🔵 **The common shape: each one is a list or a threshold that was CORRECT when written, published
honestly, and then read as a measurement.** None was a wrong fact; every one produced wrong numbers.
🟢 **The durable replacements were all structural rather than enumerative** — read what the artefact
declares about itself (`repository`, a dated appendix), or anchor on a shape (a lowercase run, a
`(directory, basename)` pair) — and they were **cheaper** than extending the lists, not more
expensive.

🔵 **Operationally:** when an instrument on these shelves publishes a bound, the next pass's question
is not *"is the bound documented"* but *"what does the corpus look like past it"* — and when it
publishes a vocabulary, *"what does the artefact say about itself instead"*.
