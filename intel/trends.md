---
industry: education
region: Global
updated: 2026-10-27
---

# Education AI — current trends

**Pass `p490` — reads of 2026-10-27.** Rewritten this pass; 84 prior pass-sections preserved in
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
| Japan | non-binding promotion | AI Basic Plan **14 Jul 2026** |
| US | state patchwork, no federal law | varies |
| LATAM | **no statute found** | — |

**Consequence:** jurisdiction behaviour (labelling, provenance, filing, oversight gates) belongs
in configuration, not in a fork per market.

## T5 — The EU deadline slipped 16 months and created a window

Regulation (EU) 2026/1744 (the Digital Omnibus) moved stand-alone high-risk education systems
from **2 Aug 2026 to 2 Dec 2027**. Article 50 transparency was *not* moved.

**Consequence:** a 14-month window to arrive conformant rather than remediate. Verify against
EUR-Lex — the dates here are from secondary commentary and many guides still print the old one.

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

## Declared gaps

- **No reliable EMEA adoption or vendor-share data.** European coverage is regulatory only.
- **No APAC school-adoption or edtech-share data** for China, India or Japan — only the Ipsos
  attitude series.
- **No LATAM AI-in-education statute found**, so no compliance hook to sell against there.
- **No open-source education-AI evaluation harness above 60★ exists**, so there is no standard
  way to measure whether any of this works. This remains the largest structural gap in the
  sector and the clearest build opportunity.
