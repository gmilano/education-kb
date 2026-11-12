---
industry: education
region: Global
updated: 2026-11-12
---

# Current trends — `p788`

🟢 **Byte-verified** claims concern repositories, grants, `sha`s and dependency manifests.
🔴 **Search-channel testimony** covers every market, adoption and regulatory figure (`T844`).

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
