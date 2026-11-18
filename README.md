---
industry: education
region: Global
updated: 2026-11-18
---

# Globant AI Studios — Education KB

Curated, verified starting points for an education engagement: the open-source platforms a
client already runs, the AI agents worth composing, the regulation that constrains the build,
and concrete recipes that name specific repos.

## Start here

| If you need… | Read |
|---|---|
| An AI agent to adopt or customise | [`agents/top.md`](agents/top.md) |
| What changed recently | [`agents/trending.md`](agents/trending.md) · [`repos/trending.md`](repos/trending.md) |
| The substrate to build on | [`repos/foundations.md`](repos/foundations.md) |
| A platform the client may already run | [`verticals/solutions.md`](verticals/solutions.md) |
| Market sizing and regional opportunity | [`intel/market.md`](intel/market.md) |
| Where the industry is heading | [`intel/trends.md`](intel/trends.md) |
| A concrete build recipe | [`compose/patterns.md`](compose/patterns.md) |

## The four facts that shape every education engagement

1. **The platforms are copyleft; the tooling is permissive.** Moodle (GPL-3.0), Open edX
   (AGPL-3.0) and Canvas (AGPL-3.0) are what clients run. Integrate over **LTI 1.3** or **MCP**
   and your tool stays a separate work; fork the platform and it does not. When a client needs a
   proprietary derivative, start from **Artemis (MIT)**, **Kolibri (MIT)**, **Oppia (Apache-2.0)**
   or **OpenOLAT (Apache-2.0)**.

2. **The best open education agents are academic, not commercial.** DeepTutor (HKU,
   Apache-2.0, 60,165 ★), OpenMAIC (Tsinghua, MIT, 43,856 ★), the Artemis/EduTelligence/Pyris
   stack (TU Munich, MIT), OATutor (UC Berkeley, MIT). The commercial tutors are closed. These
   projects want implementation partners — which is the opening.

3. **Regulation now constrains *use*, not existence, and the rules differ by region.**
   Oklahoma bars AI-only grading. The EU postponed high-risk education obligations to
   **2 December 2027** (Regulation (EU) 2026/1744) while Article 50 disclosure already applies.
   Korea's AI Basic Act is in force. India and China require AI-content labelling on dated
   schedules. **Auditable human oversight is the product.** See `intel/market.md`.

4. **Adoption has outrun governance, and that is the fastest sale.** In Brazil 53% of school
   administrators use AI and 22% have guidelines; 87% of regional universities use AI and 26%
   have a strategy. The offer is governance for AI already in use, not adoption.

## How findings in this KB are verified

Two independent channels, both re-run 2026-11-18:

- **Existence and licence text** — `LICENSE`/`COPYING` fetched from
  `raw.githubusercontent.com` and the grant read as text.
- **Stars, SPDX licence, last push, archived** — `gh api search/repositories` with batched
  `repo:` qualifiers (a *single* `repo:` qualifier returns `422`; batches of ~8 work).

`github.com` HTML returns `403` through this environment's proxy and `api.github.com/repos/`
is session-scoped, so those are not used. 116 of 119 tracked repos resolved on both channels;
the three that did not are named in `agents/top.md`. Every table row has a real repo URL, a real
licence and a real description. Where a licence cannot be confirmed, the row says so instead of
guessing.

**Star counts and `last push` are both recorded, because stars alone mislead:**
`stanford-oval/storm` has 31,906 ★ and has not been pushed in 414 days.

## What this KB does not cover

- **No LATAM-origin education agent exists at scale** — only `warleysr/ankipa` (10 ★, Brazil).
  LATAM engagements mean localising APAC- or EMEA-origin assets.
- **No Africa or Middle East coverage.** This KB's closed region vocabulary files both under
  EMEA, and the EMEA evidence is in practice European.
- **No open agent for student information systems, admissions, financial aid or proctoring.**
  The largest build-vs-adopt gap in the industry — and the most defensible studio IP, with the
  caveat that several of these are EU Annex III high-risk categories.
- **No credible primary evidence of learning-outcome gains from AI at scale.** The widely
  quoted figures trace to blogs with no primary study. `compose/patterns.md` P7 exists to
  measure it rather than claim it.

## Note on this revision

The eight content files had accumulated a large volume of self-referential pass-over-pass
commentary — roughly 800 KB across six files, much of it about the curation process rather than
the industry. Those versions are preserved verbatim in
[`archive/2026-11-18-pre-cleanup/`](archive/2026-11-18-pre-cleanup/) and the files were rewritten
as a reference a studio team can use. `agents/trending.md` and `repos/trending.md` are
append-only and retain their full history below the newest dated section.

One substantive error was corrected: **`openedx/openedx-platform` does not exist** (404 on every
branch) and had propagated through four files. The real slug is `openedx/edx-platform`.
