---
industry: education
region: Global
updated: 2026-11-12
---

# Current trends — `p787`

🟢 **Byte-verified** claims concern repositories, grants and `sha`s. 🔴 **Search-channel testimony**
covers every market, adoption and regulatory figure (`T844`).

## `T850` — The sector's two leading agents are both permissive, and both APAC-origin

🟢 **Byte-verified.** `HKUDS/DeepTutor` is **Apache-2.0** (`11,408 B`) at `58.5k★`;
`THU-MAIC/OpenMAIC` is **MIT** (`1,065 B`) at `43.4k★`. Hong Kong and Tsinghua respectively.

Two things follow, and they point in opposite directions:

- 🟢 **Commercially:** the state of the art in education agents needs no licensing negotiation. A
  studio can fork, embed and ship. In most verticals the leaders are proprietary; here they are not.
- 🔴 **Strategically:** the capability centre of gravity in education AI sits in **APAC**, while the
  **regulatory** centre of gravity sits in **EMEA** and **North America**. Engagements in the
  regulated regions will consist largely of **wrapping APAC-origin agents in regional governance**.

⚠️ **One licensing trap already found:** OpenMAIC's repo grant is MIT, but the bundled workspace
package `packages/mathml2omml` is **LGPL-3.0-or-later**. A repo-level licence read is not a
dependency audit.

## `T851` — Tutoring is being packaged as a *skill*, not an application

🟢 **Byte-verified.** `janestreet/agent_skills` — **MIT**, `1,120 B`, `7c6715c29548`, **2 commits** —
contains a `socratic-tutor/` directory: a diagnostic, a skill map with levels 0–5, one question at a
time, spaced review, a final assessment. 🔴 **Search-channel:** ~`2.1k★` on `2026-11-10`;
🟢 **page-channel, read this pass:** `6.6k★` on `2026-11-12`. **Roughly tripling in two days.**

🔵 **Why it matters more than the star count.** The pedagogy here ships as a **prompt-and-protocol
directory**, with no runtime, no server and no model dependency. It drops into any agent host. For a
studio this is the cheapest viable unit of educational IP: a skill is reviewable by a curriculum
specialist who cannot read code, versionable in git, and portable across whichever model the client
has already bought. `myvipbackup2/china-k12-teacher-skills` (Apache-2.0) is the same pattern applied
to a national curriculum.

## `T852` — The permissive layer in education is narrow, and it is not where the famous names are

🟢 **Byte-verified across 35 foundational repositories this pass.** Of these, **15 permissive, 18
copyleft, 2 EUPL-1.2.** The split is not random — it follows institutional history:

| The names a client will say | Grant | The permissive repo that does the same job |
|---|---|---|
| Moodle | 🔴 GPL-3.0 | Sakai (ECL-2.0) · OpenOLAT (Apache-2.0) |
| Open edX · Canvas | 🔴 AGPL-3.0 | Sakai (ECL-2.0) |
| Frappe LMS · ERPNext | 🔴 AGPL / GPL-3.0 | — 🔴 no permissive equivalent in this base |
| H5P content types | 🔴 GPL-3.0 | `Khan/perseus` (MIT) |
| edx-ora2 assessment | 🔴 AGPL-3.0 | `jupyter/nbgrader` (BSD-3) |
| Anki scheduling | 🔴 AGPL-3.0 | — 🔴 no permissive equivalent in this base |

🟢 **The actionable consequence:** `csev/tsugi` (Apache-2.0) is the most useful licensing component
in education open source, because LTI across a process boundary lets permissive code serve a
copyleft LMS without becoming a derivative work of it.

## `T853` — Regulation has bifurcated: the EU bought 13 months, the US states did not

🔴 **Search-channel.** 🟢 **EU:** Regulation (EU) 2026/1744 (*Digital Omnibus on AI*), OJ
`2026-07-24`, in force `2026-07-27`, moved Annex III stand-alone high-risk — education included —
from `2026-08-02` to **`2027-12-02`**. 🔴 **Not** deferred: Art. 5 prohibitions and Art. 4 AI
literacy (both live since `2025-02-02`, including the **emotion-recognition ban in education**), and
Art. 50 transparency from `2026-08-02`.

🟢 **North America, meanwhile, is enacting now:** North Carolina's model policy is due
`2026-12-31`; Ohio's mandate is in force; Oklahoma bars AI used *solely* for grading, discipline or
promotion; the U.S. Department of Education finalised AI-grant prioritisation on `2026-04-13`.

🔵 **So the pitch inverts by region.** In EMEA the deadline is the selling instrument and there is
runway to build properly. In North America the obligation is already live and the work is
remediation. 🔴 **And do not quote tracker totals** — `134`/`31 states` and `68`/`27 with 10 enacted`
circulate simultaneously. Cite the bill.

## `T854` — Assessment is the regulated surface in every jurisdiction that regulates at all

🔴 **Search-channel, and strikingly consistent across unrelated legal systems:**

| Jurisdiction | Instrument | What it catches |
|---|---|---|
| EU | AI Act **Annex III, point 3** | Admissions · evaluating learning outcomes · assigning education levels · **exam proctoring**; final-grade determination is high-risk |
| Vietnam | 2026-07 high-risk sector list | Education named, **citing automated assessment** |
| Oklahoma | Responsible Technology in Schools Act | AI used **solely** for grading, discipline or promotion |
| New York | A 9190 (pending) | Classroom AI restricted to grade 9+, diagnostic/special-ed exceptions |
| India | Amended IT Rules, from `2026-02-20` | Provenance labels on AI-generated content — reaches generated courseware |

🟢 **One architecture satisfies all five:** AI proposes, a named human decides, and the system keeps
an audit trail joining the proposal, the evidence and the decision-maker. `jupyter/nbgrader`
(BSD-3) already has that shape, which is why it anchors `P787-1`. 🔵 The word doing the work in
Oklahoma's statute is **"solely"** — it regulates *autonomy*, not assistance, and a
human-in-the-loop design is not a compliance tax but the product.

## `T855` — LATAM adoption has outrun LATAM governance by about 60 points

🔴 **Search-channel.** Teacher AI use in the past year (TALIS 2024): **Brazil `56%`, Chile `55%`,
Colombia `53%`, Costa Rica `52%`** against an **OECD average of `36%`**. 🟢 **LATAM teachers
out-adopt the OECD.** Meanwhile `87%` of regional universities use AI, **`26%`** have a strategy,
**`9%`** evaluate it (UNESCO IESALC); in Brazilian schools `53%` of administrators use AI and
**`22%`** report any guidelines (Cetic.br).

🔵 **The strategic reading.** This is not a market to be *introduced* to AI — that already happened,
bottom-up, through teachers. It is a market that needs its existing, ungoverned use made
defensible. 🔴 **And there is no regulator to sell against:** no AI-in-education statute was found
for Brazil, Mexico or Chile; the governing layer is UNESCO-convened soft governance. The buying
trigger is institutional risk and the readiness gap, not a deadline.

## `T856` — EMEA is building the substrate and not the education layer

🔴 **Search-channel, and a deliberate negative result.** A query for European-origin open-source
education **agents** returned **only** sovereign-LLM infrastructure and compliance commentary:
OpenEuroLLM, Germany's SOOFI (~€20M, public-sector deployment targeted mid-2026), the Netherlands'
**GPT-NL** (explicitly scoped to health, **education** and public services), Switzerland's Apertus,
Fraunhofer's Teuken, Mistral, Haystack.

🟢 **Byte-verified counterpoint:** EMEA's real education open source is **platforms and languages**,
not agents — OpenOLAT (Apache-2.0), Opencast (ECL-2.0), ILIAS, Chamilo, H5P, and `hedyorg/hedy`
(EUPL-1.2, `1,697★`). One EMEA-placed *agent* exists in this base and it is Kenyan
(`Moses-Githinji/meta-cv-hktn-edu-agent`, MIT).

🔵 **An empty slot with a funded substrate beneath it and a `2027-12-02` deadline above it is the
most legible build opportunity in this pass.**

## `T857` — Three more failure modes of one instrument, all caught by controls *before* publication

🟢 **This is `ACTION p786-A` discharged: the grant gate is now in the probe, not in the record** —
and putting it there immediately paid for itself three times. Controls ran before any verdict shipped.

| | Failure mode | How it showed up | Fix |
|---|---|---|---|
| `T847` | **Title-line insufficiency** (recorded by `p786`) | `odoo/odoo`, `openeducat_erp` state LGPL-3.0 on line 3 behind a deferral | Carried; both graded LGPL correctly this pass |
| 🔴 `T848` | **Language-blindness** — NEW | `goyanedelv/paes-mcp` served a **valid MIT grant in Spanish** and the English-only clause probe returned `UNGRADED`. 🔴 **A translated grant looked exactly like no grant** | Gate now matches MIT's four clauses in **English, Spanish, Portuguese and French**, and reports `MIT(translated)` so the distinction survives |
| 🔴 `T849` | **Appendix contamination** — NEW | `hedyorg/hedy` and `open-education-api/specification` both serve an identical `13,827 B` licence and both graded `GPL-?` — because **EUPL-1.2 names GPL-2.0, GPL-3.0, AGPL, EPL and CeCILL inside its compatibility appendix** | A licence that *lists other licences* is matched **before** any family check |
| 🔴 — | **Pipe-swallowed exit status** | A negative control returned exit `0` because `git ls-remote` was piped into `head`, so `head`'s status was read | Status read directly; `${PIPESTATUS[0]}` never relied on |
| 🔴 — | **Affero-in-GPLv3** | Moodle graded `AGPL-3.0`, because **GPL-3.0 §13 names the Affero licence**. 🔴 Caught only because a known-good control asserted GPL-3.0 | Family decided on the **title line**, not a whole-file grep |

🔵 **The lesson this base should stop re-learning.** Five distinct ways to misread a licence have now
been recorded — case-blindness (`T842`), title-line insufficiency (`T847`), length-as-integrity
(`T845`), language-blindness (`T848`), appendix contamination (`T849`). 🟢 **Every one was found by a
control on a row this base had already published, and none by inspection.** The instrument that
catches them is cheap; the discipline that runs it before shipping a verdict is the whole method.

🟢 **And both new failure modes are biased in a direction that matters commercially:**
language-blindness under-reports **LATAM**, and appendix contamination mis-grades the **EU's own
licence**. 🔴 **A probe written in English against American licence conventions will quietly
under-report exactly the two regions this base is told to serve.**

## `T858` — Purpose-built is displacing general-purpose, on the record

🔴 **Search-channel.** The OECD's 2026 Digital Education Outlook recommends moving **beyond
general-purpose AI tools toward purpose-built educational AI** designed for durable learning gains;
1EdTech frames 2026 as the shift **from experimentation to governance**; HolonIQ expects focus on
ethics, transparency, agentic use cases and proven instructional benefit. One outlook calls 2026
"the year of the agentic AI university".

🟢 **Byte-verified corroboration, which is the useful part:** the artefacts actually trending are
purpose-built rather than general — a classroom generator (OpenMAIC), a lifelong tutor with mastery
tracking (DeepTutor), a Socratic protocol (`agent_skills`), a curriculum-specific skill pack
(`china-k12-teacher-skills`), an admissions-test MCP server (`paes-mcp`). 🔵 **The commentary and the
commits agree for once**, which is rare enough in this base to note.

## `T859` — A national AI policy was withdrawn for citing sources AI invented

🔴 **Search-channel, and `p786-C` is now settled.** South Africa's draft National AI Policy was
gazetted as **Notice 3880 of 2026 on `2026-04-10`** and **withdrawn on `2026-04-26`** by Minister
Solly Malatsi, after fabricated, AI-hallucinated citations were found in its reference list —
reportedly **at least 6 of its 67 academic citations**. One source records abrogation on
`2026-04-27`, a day later, so 🔴 **cite both dates**. A seven-person panel is reviewing it with no
published timeline. The Department of Basic Education's **National AI in Education Framework**
remains 🔴 **unpublished, with no timeline**.

🔵 **Keep this row.** It is the most persuasive provenance argument available in an education
engagement: the failure mode was not a model hallucinating in a classroom but **an AI-drafted
governance document failing its own review** — and the cost was a withdrawn national policy and a
governance vacuum in a country where, as commentary in the same window put it, AI is already inside
the classrooms and nobody is governing it.
