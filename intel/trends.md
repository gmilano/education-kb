---
industry: education
region: Global
updated: 2026-10-27
---

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

## T11 — The education-AI evaluation instruments now exist, and not one of them is licensed

This reverses the shape of the sector's biggest gap. `p490` reported the tier as empty. Measured
from bytes this pass: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (45★,
**EMNLP 2025 Oral**, 3 teacher skills × 7 tasks) and
[`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) (0★, KAIST, 923 dialogues)
are real, serious, and **ship no license file at all**. MathTutorBench's README contradicts itself —
badge `CC BY 4.0`, closing line `CC BY-SA 4.0` — and **neither is a software grant**; Creative
Commons advises against CC licenses for code, and one of the two is copyleft.

**Consequence:** the instrument tier is blocked by **licensing, not scarcity** — a harder problem,
because scarcity is fixed by searching and no-grant is fixed only by the authors. The papers are
readable and the *task designs* are reimplementable; the repositories are not usable. So a
tutoring-eval capability is still a **build**, but it is no longer a build from nothing: rebase it
on [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
(**MIT**, 14,300★, grant read at 1,066 B) and implement the published task designs on it. This is
the single clearest open-source credibility asset available in this sector, and EU high-risk
conformity will demand exactly this evidence by **2 Dec 2027**.

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
