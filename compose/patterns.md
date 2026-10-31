---
industry: education
region: Global
updated: 2026-10-31
---

# Compose patterns — education

<!-- machine-readable count claim, p569, for ingest/derive-counts.py -->
`derived recipes: **21**` — recipe headings on this page, counted with that gate's
own id regex (family-suffixed form, `P-572-A`).

Concrete recipes. Every component is a repo verified first-hand on 2026-10-31
with its licence named — and for everything added or re-read in the fourth pass,
**the licence text itself was read, not GitHub's summary of it**. Every pattern
obeys the one hard constraint of this industry: **the platform of record is
copyleft, so you attach to it, you do not fork it.**

**New in the fourth pass:** **P-569-A** (SCORM delivery — the attach doctrine
finally covers content moving *into* the platform) and **P-569-B** (the courseware
factory, built on the 71,498★ MIT content-production layer that four passes of
education-topic sweeps could not see). **P-568-K** carries a licence correction
that changes what it may ship.

Shared rule for all thirteen patterns — the licence boundary:

```
  [ client's LMS of record ]          GPL-3.0 / AGPL-3.0  ← never forked, never patched
   Moodle | Open edX | Canvas | Chamilo | i-educar
            │
            │  attach ONLY across a standard, permissively licensed boundary:
            ├── LTI 1.3 ....... Cvmcosta/ltijs        Apache-2.0  (launch + grades back)
            ├── MCP ........... canvas-mcp/moodle-mcp MIT         (agent reads LMS data)
            ├── xAPI → LRS .... adlnet/xAPI-Spec      Apache-2.0  (telemetry out)
            │                   openfun/ralph         MIT
            ├── SCORM ......... jcputney/scorm-again  MIT         (courseware IN)
            │
  [ Globant-built layer ]             your licence, your IP
```

**Shared step 0 — licence preflight (half a day; method upgraded again
2026-10-31, fourth pass).** Before any component enters a statement of work,
establish its licence from the **GitHub REST index** (`license.spdx_id`) and then
**read the licence file itself** over
`https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filename}`, which
answers HTTP 200 from this session while `api.github.com` and `github.com` HTML
return 403 and MCP `get_file_contents` refuses third-party repositories. **Read
the file for every component, not only the ones the API flags** — the two licence
questions this KB carried longest were both resolved by reading text the API had
summarised as `NOASSERTION` or matched against no filter. Try **every filename**
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `licence`, `COPYING`) on **every
branch**: `24kchengYe/human-skill-tree` is AGPL-3.0 on `master` and 404 on
`main`, and two passes recorded it unresolved for exactly that reason. Do not
accept a sidebar or a README sentence. Across three passes this check has caught a defect
in roughly half the repos run through it. The failure modes, with the live
example to cite in a SoW appendix:

- *no licence field at all* → genuinely unlicensed, default exclusive copyright.
  **Disqualified.** `digitalinnovationone/dio-agent` — **2,750★** and no licence.
- *licence claimed in prose, file absent* → **disqualified**, regardless of the
  README. `DMontgomery40/mcp-canvas-lms` says "MIT License - see LICENSE file";
  that file 404s on every name and both branches, and GitHub's own licence index
  returns zero results for it.
- *`NOASSERTION` but actually a **split grant*** → **conditionally usable, per
  asset.** `learning-commons-org/knowledge-graph`: `LICENSE.md` with code **MIT**
  and datasets **"By data publisher"**, some datasets gated. The code clears; each
  dataset must be cleared individually.
- *content licence on code-shaped work* → **usable but viral on the text.**
  `brycewang-stanford/Auto-Empirical-Research-Skills`, 4,843★, **CC BY-SA 4.0**,
  and `GarethManning/education-agent-skills`, 932★, **also CC BY-SA 4.0** — the
  two largest education skill libraries in existence, both read from the licence
  file this pass. Share-alike propagates to derivatives of the skill text: fatal
  for a billable methodology asset, fine for internal reference. **Expect this
  shape whenever the artefact is pedagogy written in markdown.**
- *split grant with a **non-commercial** tier* → **the trap that matters most to
  a consultancy, because the restricted tier is the part you were going to
  ship.** `learning-commons-org/evaluators`, 87★: code **MIT**, prompts
  **CC BY 4.0**, and the **Annotated CLEAR and PERSUADE 2.0 corpora
  CC BY-NC-SA 4.0 — non-commercial.** The scoring machinery clears; the benchmark
  data does not. **Check every tier of a split grant for `NC`, not just the
  first.**
- *copyleft with a **per-directory** dual grant* → **partly usable, and no
  licence column can say so.** `24kchengYe/human-skill-tree`, 586★: AGPL-3.0
  overall, with `skills/*.md` available under **AGPL-3.0 or MIT at your option**.
  The platform is disqualified; the bundles inside it are not. Record the
  directory, not just the repository.
- *wrong version* → `openSIS-Classic` is GPL-**2.0**, not GPL-3.0: no patent
  grant, incompatible with GPL-3.0-only code in the same binary.
- *unparsed but present* → Odoo (LGPL-3.0) and `frappe/education` (GPL-3.0) name
  no licence in the sidebar and are perfectly licensed in the file.

A cheap corroborating trick worth knowing: `license:mit repo:owner/name` in
GitHub repository search returns **zero results** when GitHub detects no MIT
grant. It is a second, independent opinion for the cost of one query, and it is
how the `mcp-canvas-lms` defect was re-confirmed on the third pass.

One `curl` per dependency, written into the SoW appendix. It is the cheapest
risk control in this document and it has already caught a real defect. See
[`../intel/trends.md`](../intel/trends.md) for the measured results.

---

## P-568-A — LTI-attached AI tutor over a copyleft LMS (6–8 weeks)

**For:** any client on Moodle, Open edX, Canvas or Chamilo who wants AI tutoring
inside their existing LMS without a platform migration or a licence problem.
**Regions:** all. This is the default engagement shape.

**Wiring:**
1. **Tutor core** — [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
   (Apache-2.0, 52k★, `v1.7.0`). Deploy from `ghcr.io/hkuds/deeptutor`. Apache-2.0
   permits commercial use and the derivative stays yours.
2. **Mastery model** — [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT).
   Take its **Bayesian Knowledge Tracing** implementation as the per-skill
   mastery estimator rather than letting the LLM self-assess mastery. This is the
   step that makes the tutor defensible under "proven instructional benefit."
3. **Attachment** — [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0). Wrap the tutor as an LTI 1.3 tool provider: Deep Linking so
   instructors place it in a course, Names and Role Provisioning for roster and
   role, **Assignment and Grade Services to write results back to the gradebook**.
   Zero lines of LMS code modified.
4. **Telemetry** — emit [xAPI](https://github.com/adlnet/xAPI-Spec) (Apache-2.0)
   statements into [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) as
   the LRS.
5. **Acceptance gate** — score the tutor on
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) **before** go-live and keep the score as release evidence.

**Why it holds up:** steps 1–5 are Apache-2.0/MIT throughout. The client's
AGPL obligations are never triggered because their platform is never modified.

---

## P-568-B — Canvas agent fleet with a read-only default (3–4 weeks)

**For:** institutions on Canvas wanting agent access to course data for staff and
students. **Region:** North America primarily (Canvas's install base, and the
verified agents are North American).

**Wiring:**
1. **Base server** — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, 310★, `v1.16.0`). The most established option; also ships ready-made
   agent skills — **pre-semester course audit** and **accessibility auditor** —
   which are deliverables on their own and the fastest demonstrable value here.
2. **Lean alternative** — [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms)
   (MIT per README, `v2.2`, 54 tools) where a smaller, containerised surface is
   preferred over maximum coverage.
3. **Write-surface decision, made explicitly.** Tool counts here run from 54 to
   128 and some tools mutate LMS state (submit, grade, delete). Enumerate the
   tool list of the exact version you deploy, classify each tool read vs. write,
   and **expose the read set by default**; every write tool is enabled
   deliberately, per role, never by default. Do not infer the surface from the
   README — tool counts are version-specific and the README and sidebar of the
   same repo disagree.
4. **Grades stay on the sanctioned path.** Writes back to the gradebook go
   through LTI AGS (`ltijs`), not through an MCP write tool — AGS is the
   auditable, spec-sanctioned channel.
5. **Audit** — xAPI → `ralph`, so every agent action against student data is
   reconstructible. This is what satisfies a district AI policy.

---

## P-568-C — District AI policy instrumentation, North America (8–10 weeks)

**For:** US districts and state education agencies. **Region:** North America.
**Driver:** Maryland, Idaho, Oklahoma and Virginia now **require** state guidance
*and* district-level AI policy adoption; 134 bills across 31 states in 2026. Most
US public schools have no formal student AI policy. This is statutory work
districts cannot self-serve.

**Wiring:**
1. **Policy → machine-checkable rules.** Translate the district's adopted AI
   policy into enforceable predicates, not a PDF. The NY A 9190 shape —
   classroom AI restricted to **grade 9 and above, with exceptions for
   diagnostics and special education** — is the worked example: it requires
   per-cohort age gating plus a documented exception path.
2. **Enforcement point** — the MCP layer from **P-568-B**. Roster and role come
   from LTI Names and Role Provisioning (`ltijs`, Apache-2.0), so grade-level
   gating is driven by the SIS's own data rather than a hand-maintained list.
3. **Evidence layer** — xAPI into `ralph` (MIT), retained as the compliance
   record: who used which AI tool, in which course, under which policy version.
4. **Instructional-quality evidence** — `pedagogy-benchmark` (MIT) scores on any
   tool the district approves, including the special-educational-needs subset
   (**SEND, 223 questions**), which maps directly onto the special-education
   exception the statutes carve out.
5. **Deliverable.** Policy document, enforcement configuration, audit pipeline,
   and a per-tool evaluation report — the four artefacts a district needs to show
   it complied.

**Procurement note:** the contested USD 10 m Khanmigo earmark in North Carolina
SB 1006 shows large single-vendor AI tutoring buys are politically exposed.
Platform-neutral, policy-first work is the easier sell.

---

## P-568-D — EU AI Act Annex III conformity package (10–12 weeks)

**For:** EMEA institutions and edtech vendors whose systems evaluate learners or
affect access to qualifications — **Annex III high-risk** under the EU AI Act.
**Region:** EMEA.

**Timing, which is the whole reason to run this now:** stand-alone Annex III
obligations were **deferred to 2027-12-02** (Digital Omnibus, in effect late July
2026), and embedded-in-product to 2028-08-02. That is a ~14-month readiness
runway. Guidance still claiming August 2026 is superseded.

**Wiring:**
1. **Substrate choice matters here.** Where the client wants a
   licence-clean European build rather than an attachment,
   [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0 per
   README badge, Switzerland) is the only permissively licensed institutional LMS
   verified in this KB. Otherwise attach to Moodle via `ltijs` as in P-568-A.
2. **Human oversight, built in, not bolted on.** Implement the
   lesson-plan/assessment flow as **draft-for-teacher-review** — the shape
   Educativa reports the market converging on and the shape Annex III requires.
   The teacher's approval event is an xAPI statement, so oversight is evidenced
   rather than asserted.
3. **Evaluation evidence** — `pedagogy-benchmark` (MIT) gives reproducible,
   documented pedagogical-knowledge scores for the technical documentation pack.
4. **Telemetry under data-protection constraint** — self-host `ralph` (MIT) in
   region; xAPI's actor model lets you pseudonymise the learner at emission.
5. **Package** — risk classification memo, human-oversight design, technical
   documentation, evaluation results, post-market monitoring plan.

**Also in scope for EMEA:** the December 2026 ban on certain AI-generated
intimate imagery and abuse material — a content-safety obligation on any
deployment handling student-generated media, and it lands *before* the high-risk
duties.

---

## P-568-E — LATAM institutional AI strategy, from 87% use to 26% strategy (6–8 weeks)

**For:** Latin American universities and ministries. **Region:** LATAM.
**Driver:** UNESCO IESALC / UNU-IAS across 200 institutions in 19 countries —
**87% already use AI somewhere, only 26% have a formal strategy**, with adoption
driven by individuals rather than institutions. The client's problem is not
starting; it is that it already started without them.

**Wiring:**
1. **Shadow-use census first.** The engagement opens by measuring what is
   already in use, because individual-led adoption means nobody has the list.
   `ralph` (MIT) as LRS plus xAPI emission from sanctioned tools turns shadow use
   into an inventory.
2. **Strategy artefacts on UNESCO's own recommendations** — fold higher education
   into the national AI strategy, develop institutional guidance, fund it, and
   **integrate AI literacy and governance into accreditation and quality
   assurance**. That last one is the procurement wedge: accreditation is already
   a budgeted, calendared institutional function, so the work attaches to an
   existing budget line rather than requesting a new one.
3. **Public-sector build path, Brazil** —
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (**GPL-2.0**,
   722★) is the reference municipal platform for *Secretarias de Educação*.
   GPL-2.0 means the AI layer attaches over LTI/xAPI; an i-educar fork would have
   to be released.
4. **Spanish/Portuguese-language capability** — Chamilo (GPL-3.0) has a notable
   LATAM and francophone install base and is a second common platform of record.
5. **Convening route** — the **UNESCO Observatory on AI in Education for Latin
   America and the Caribbean**, launched 2026-04-14 in Santiago with **CAF**
   (Development Bank of Latin America and the Caribbean). Partners include CENIA
   (Chile), Cetic.br (Brazil), ECLAC, Fundación Ceibal (Uruguay), Fundación
   Santillana, Tecnológico de Monterrey, ProFuturo and IRCAI. A funded regional
   body with a named partner list is a better entry point than institution-by-
   institution outreach.

---

## P-568-F — Africa: national strategy to institutional policy, offline-first (8–10 weeks)

**For:** a ministry or university system in a country with a national AI
strategy on paper and no institutional capacity behind it. **Region: EMEA**
(Africa sits inside the EMEA value — see
[`../intel/market.md`](../intel/market.md)).

**Why this pattern now exists.** The first pass of this KB declared "no
Africa-specific pattern" because the *demand evidence was missing*, while naming
Kolibri as the obvious component. The second pass found the evidence, so the
pattern can be written: **AU Continental AI Strategy** names education a
priority sector; **Zimbabwe** (National AI Strategy 2026–2030) and **Ghana**
(2025–2035, plus a July 2026 draft curriculum putting **AI literacy in
kindergarten through Primary 6**) have funded mandates; and only **14%** of
higher-education respondents can confirm their institution has an AI policy,
against **69% who do not know** (Frontiers, 2026).

**The two constraints that shape it:** connectivity cannot be assumed, and the
deficit is *institutional awareness*, not tooling. A cloud-first tutor
deployment answers neither.

**Wiring — permissive and offline-capable end to end:**
1. **Delivery substrate** —
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
   (**MIT**, 1.2k★). Offline-first by design; the only platform in this KB built
   for intermittent connectivity. MIT means the deployment and any derivative
   stay licence-clean.
2. **Institutional corpus** —
   [`DSpace/DSpace`](https://github.com/DSpace/DSpace) (**BSD-3-Clause**, 1.1k★)
   as the repository of record for curriculum material, theses and local
   language content. Permissive, so a client-specific derivative is permitted —
   see P-568-G.
3. **Model hosting** — local/edge inference, not an API dependency. The
   connectivity constraint and the data-residency question resolve the same way.
4. **Curriculum alignment artefact** — the **Ghana KG–P6 AI-literacy curriculum
   draft** is the most procurement-ready single item in the region. Build the
   content packs against it; they are reusable across Anglophone systems.
5. **Policy instrumentation** — the deliverable that closes the 69%
   don't-know gap is *not* software: an institutional AI policy template derived
   from the national strategy, plus the training records and usage telemetry
   (xAPI → [`openfun/ralph`](https://github.com/openfun/ralph), MIT) that prove
   it is live. Ship this *first*; it is what the mandate is actually missing.
6. **Quality gate** —
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT), whose **SEND** subset (223 questions) matters in systems with limited
   specialist-teacher provision.

**Why it holds up:** steps 1, 2, 5 and 6 are MIT or BSD-3-Clause — **the only
pattern in this document with no copyleft component anywhere in it**, because
Africa's institutions are less likely to be locked to an incumbent Moodle or
Canvas estate. That is the one structural advantage of a late-starting market.

**Sell it on the strategy, not the software.** The buyer has a national mandate
and no implementation path. Lead with step 5.

**Caveats, stated plainly.** South Africa's draft National AI Policy status is
**contested** (Gazette Notice 3880 of 2026 versus a tracker marking it
withdrawn) — do not build a pitch on it without the primary record. Namibia has
no national strategy at all. And the **supply side of this region is unmapped**:
no African education platform or agent repository appears anywhere in this KB,
so every component above is imported. Partnering locally is a gap-closing move,
not a courtesy.

---

## P-568-G — Permissive research-corpus agent on DSpace (4–6 weeks)

**For:** a university that wants AI discovery over its own scholarly output —
theses, datasets, faculty publications, grey literature — and wants to **own the
result**. **Regions:** all.

**Why this is the exception in this document.** Every other pattern here is an
*attachment* to something Globant may not fork. This one is not.
[`DSpace/DSpace`](https://github.com/DSpace/DSpace) is **BSD-3-Clause** —
verified in the sidebar and in `LICENSE` on `main` ("Copyright (c) 2002-2021,
LYRASIS") on 2026-10-31. It is the **only platform of record in this KB that
permits a proprietary derivative.** If a client needs owned IP in the substrate
rather than beside it, this is the one place in the education stack where that is
available, and it happens to sit on the corpus a RAG agent most wants.

**Wiring:**
1. **Substrate** — DSpace (BSD-3-Clause). Fork or extend freely; the derivative
   may stay closed. Java.
2. **Retrieval layer** — build it *into* the repository rather than beside it,
   which the licence permits and which is why this pattern is shorter than
   P-568-A: no LTI handshake, no plugin approval, no change-control queue on
   someone else's AGPL platform.
3. **Agent surface** — reuse the MCP shape the rest of the field has
   standardised on (four of six agents in [`../agents/top.md`](../agents/top.md)
   are MCP servers) so the corpus is reachable from whatever assistant the
   institution adopts later. Do not invent a bespoke connector.
4. **Course-facing delivery** — when results need to appear inside the LMS,
   attach *that* step with [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0). The copyleft boundary applies to the LMS, not to DSpace.
5. **Library-system adjacency** — if the engagement also touches the catalogue,
   [`Koha-Community/Koha`](https://github.com/Koha-Community/Koha) is **GPL-3.0**:
   back inside the attach-don't-fork rule. Note Koha takes contributions through
   its **own bug tracker, not GitHub issues** — plan the upstreaming path.

**The trap to avoid:** DSpace's permissive licence tempts a full fork. Fork only
what the retrieval layer needs and track upstream, or the client inherits a
maintenance burden on a Java platform in exchange for IP they may not need.

**Honest sizing.** DSpace is 1.1k★ — an order of magnitude below Moodle or
Canvas. This is a narrower engagement than the LMS patterns and should be priced
and pitched as such. Its value is the licence position, not the market size.

---

## P-568-H — APAC award-integrity and assessment reform, Australia-first (8–10 weeks)

**For:** Australian higher-education providers (and the ASEAN institutions that
follow TEQSA's lead) that have an institutional gen-AI action plan on file and no
operational governance behind it.
**Region:** APAC.

**Why this is now a pattern rather than a note.** The previous pass declined to
write an APAC recipe, on the view that the region needed P-568-D run per
jurisdiction. Two pieces of evidence found on this pass change that: TEQSA
required a credible gen-AI action plan addressing **risk to award integrity**
from *every* Australian provider and received a **100% response rate**, and a
peer-reviewed AJET national document analysis of **39** universities found
operational governance structures documented in only **7**. So there is a named
population of ~32 institutions that have a filed plan, a regulator that has read
it, and no machinery underneath. That is a pattern, not a per-country variant of
an EU one — the driver is **award integrity**, not conformity assessment.

**Wiring:**
1. **Pick the assessment posture first.** TEQSA's own follow-up resource names
   three that have emerged: programme-wide assessment reform, assuring learning
   in every unit, or a combination. This is a curriculum decision and it sets
   everything downstream — do not start with tooling.
2. **Attach to Moodle, which is a home-region product.** Moodle HQ is in Perth.
   Use [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) for the
   LTI 1.3 boundary, and
   [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (MIT, Rust) for
   agent read access — it is validated against **Moodle 3.7 → 5.x**, which
   matters because APAC institutional estates run old versions. Borrow the design
   choice of the AGPL-licensed `csmediapro/moodle-mcp-server` without using it:
   work through **Moodle Web Services** so no plugin install is needed on the
   client's server, which is usually the real blocker.
3. **Instrument integrity as evidence, not assertion.** Every AI-assisted step in
   an assessment flow emits an **xAPI** statement into a self-hosted
   [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) LRS: what the student
   was shown, what the agent drafted, which human approved it. Award integrity is
   an evidentiary claim and this is what makes it auditable.
4. **Gate the generated material.** Score assessment items with
   [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
   (rubrics — **clear its licence at step 0**) and the model's pedagogical
   knowledge with [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT). Without this the deliverable is an opinion.
5. **Package:** the governance structures the AJET study found missing —
   decision rights, escalation path, review cadence, a register of AI-touched
   assessments — plus the xAPI evidence trail and the evaluation results.

**Adoption-risk section is mandatory in this region, and cite Korea for it.**
South Korea's AI textbooks reached **below 30% adoption by March** and lawmakers
then **removed their official status**. Contrast Singapore, which mandated
*teacher capability* first (one compulsory AI module by end 2026, two more
recommended by end 2027). The lesson to put in front of an executive sponsor:
**fund the teacher, not the artefact.**

**Per-jurisdiction note (still true):** for Vietnam — risk-based law effective
**2026-03-01**, with education and automated assessment named high-risk — and for
Korea's AI Basic Act (in force **2026-01-22**, guidance-first grace period
through 2026), run **P-568-D**'s conformity artefacts against local thresholds.
The artefacts are the same; the thresholds differ.

---

## P-568-I — Multi-agent interactive classroom on OpenMAIC (4–6 weeks)

**For:** any client who wants course material turned into taught, interactive
lessons rather than documents — corporate L&D, exam-prep providers, universities
building a self-study track.
**Region:** Global (component origin APAC).

**Why this pattern exists now.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC)
is **MIT**, **41,981★**, TypeScript, `v1.3.0` dated 2026-10-29, from Tsinghua —
and it did not exist when this KB's earlier patterns were written (repo created
2026-03-11). It is the largest permissively licensed, *deployable* education
application in existence: topic or uploaded documents in, interactive lesson out,
with AI teachers **and AI classmates**, slides, quizzes, simulations, speech,
whiteboard and live discussion. MIT means the client owns the derivative.

**Wiring:**
1. **Stand it up on its own stack, not the client's LMS.** Node.js ≥ 22.19,
   pnpm ≥ 10, PostgreSQL 16. It is a separate application by design — which is
   exactly what the copyleft constraint wants.
2. **Attach it to the LMS of record across LTI 1.3** with `ltijs` (Apache-2.0):
   launch a lesson from inside Moodle/Canvas, write the quiz result back through
   Assignment & Grade Services. The client's platform is never touched.
3. **Feed it the client's corpus.** Its document-to-lesson path is the integration
   point. Where the material is scattered across an institutional repository, pull
   from **DSpace** (BSD-3-Clause) as in P-568-G.
4. **Use its export formats as the commercial hedge.** It exports **PPTX**, a
   **single offline HTML file**, and a classroom ZIP. The offline HTML export is
   the answer to low-connectivity delivery *and* to a client who will not host a
   new service: you can ship the artefact without shipping the platform.
5. **Add retention.** OpenMAIC teaches; it does not schedule revision. Pair with
   [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT,
   539★) so an agent writes cards into a real spaced-repetition scheduler instead
   of a reimplemented one.
6. **Gate and evidence it** exactly as in P-568-H step 4 and step 3.

**Risks to state plainly.** 211 open issues and eight months of existence. Pin a
commit, not a tag, and budget for upstream churn. Its origin is a Chinese
university, which is a procurement question in some public-sector contexts and
should be raised early rather than discovered at security review.

---

## P-568-J — Permissive AI-native LMS substrate, EMEA (6–8 weeks)

**For:** corporate L&D and compliance-training clients who want an AI-native
learning platform they can **own, rebrand and keep closed** — not an attachment
to someone else's copyleft LMS.
**Region:** EMEA.

**Why this is newly possible.** Every previous pattern in this file is an
*attachment*, because every platform of record is copyleft. [`Selleo/mentingo`](https://github.com/Selleo/mentingo)
is **MIT**, from **Selleo (Poland)**, and describes itself as a self-hosted
alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX, with
an AI Mentor and role-play, **SCORM and xAPI** built in, and white-labelling as a
stated goal. It is the first time this KB can offer substrate replacement rather
than boundary attachment.

**Wiring:**
1. **Fork it, and mean it.** MIT: the derivative is the client's. This is the
   whole point of the pattern and the only reason to prefer it over P-568-A.
2. **Keep the standards boundaries anyway.** It ships xAPI, so point telemetry at
   a self-hosted `openfun/ralph` (MIT, France) rather than its internal store —
   that keeps analytics portable if the client later outgrows it. SCORM support
   is the migration path *in* from an incumbent LMS.
3. **Compose the tutor layer rather than writing one.** `Li-Evan/Bloom` (MIT) for
   Socratic tutoring, `GeminiLight/SocialCoach` (Apache-2.0) for the role-play
   and conflict-handling content that maps directly onto compliance training, and
   `dmoshehun-prog/learn-from-materials` (MIT) to turn the client's existing PDFs
   and policies into traceable lessons.
4. **An entirely permissive, entirely EMEA-origin stack is assemblable** —
   `mentingo` (Poland, MIT) + `ralph` (France, MIT) + `ltijs` (Apache-2.0) +
   `pedagogy-benchmark` (MIT). For a client with data-sovereignty or
   supply-chain-origin requirements, that combination is the differentiator;
   state it explicitly in the proposal.

**Risks to state plainly, because this one is easy to oversell.** 102★, 31 forks,
**105 open issues**. SSO, accessibility conformance, data residency and
Moodle migration were **not** verified by this KB. Scope a two-week technical
spike against the client's actual non-functional requirements *before* committing
to substrate replacement; if the spike fails, fall back to P-568-A, which is
mature.

---

## P-568-K — Governance harness for agent-skill deliverables (3–4 weeks)

**For:** any client adopting education AI that arrives as **agent skills** —
markdown instruction bundles loaded by Claude Code, Codex, OpenCode, Cursor or
Antigravity — rather than as a hosted application.
**Region:** Global.

**Why this is the most contemporary pattern in this file.** **Six of the
fourteen** agents on [`../agents/top.md`](../agents/top.md) are skill bundles, and
`topic:agent-skills topic:education stars:>50` returns 13 repositories led by one
at 4,843★. A skill bundle has **no runtime to monitor, no semver by convention,
no test suite by convention**, and its behaviour changes when the harness or the
underlying model changes — neither of which the client controls. Clients are
adopting these today with no governance at all.

**Wiring:**
1. **Licence-screen every bundle first** (step 0 above). This cohort is where the
   defects are: the largest member is **CC BY-SA 4.0** (share-alike on the skill
   text), the second-largest (**2,750★**) has **no licence**. A skill bundle looks
   like documentation and is governed like a work of authorship.
2. **Pin the harness and the model, and write both into the contract.** The
   deliverable is a prompt contract evaluated by a third party's runtime. If the
   model version is not pinned, the behaviour the client accepted is not the
   behaviour they will get.
3. **Build the regression suite the ecosystem does not have — and source your own
   corpus.** Freeze a golden set of task → expected-property pairs for the
   client's own syllabus. Score with `learning-commons-org/evaluators` for content
   quality and `pedagogy-benchmark` (MIT, 1,143 teacher-qualification questions)
   for pedagogical knowledge. Run it on every harness or model change. **This is
   the missing runtime-monitoring layer identified in
   [`../intel/trends.md`](../intel/trends.md), built by hand because nothing
   open-source provides it.**

   ⚠️ **Licence correction, fourth pass — read this before quoting the work.**
   `evaluators` is a **three-tier grant** (`main/LICENSE.md`, 1,615 B, read
   first-hand): the **code is MIT** and the **rubric prompts and settings are
   CC BY 4.0**, both fine commercially with attribution — but its **Annotated
   CLEAR Corpus** and **Annotated PERSUADE 2.0 Corpus** are **CC BY-NC-SA 4.0,
   non-commercial**, and the upstream originals are NC too, so there is nothing
   cleaner to substitute. **The scoring machinery goes into a billable
   deliverable; those two corpora do not.** The golden set must be built from the
   client's own syllabus and assessed work — better practice anyway, since a
   client-specific corpus is what makes the suite meaningful, but now also a
   licence requirement. **Price the corpus construction explicitly**; it is the
   line nobody budgets for.
4. **Check curriculum alignment, do not assume it.** `learning-commons-org/knowledge-graph`
   (code MIT, datasets per-publisher, ships an MCP server) links academic
   standards and curricula; where the client has no rich national standard, use
   `AI-for-Education/gpf-alignment` (MIT) against the **Global Proficiency
   Framework**.
5. **Require citation provenance as an acceptance criterion.** Prefer bundles
   engineered for it — `ZeKaiNie/universal-examprep-skill` (MIT) teaches from the
   instructor's own slides **with page citations** and is explicitly built against
   hallucination. Then cite the reason: **South Africa's draft National AI Policy
   was withdrawn because at least 10% of its academic references were
   fictitious.** That is the cheapest executive-level argument available for
   provenance work, and it is a matter of public record.

**What the client is buying.** Authoring and maintenance, not hosting. Say so in
the pricing conversation: infrastructure cost collapses, and the
recurring-revenue story has to be the regression suite and the model-upgrade
re-certification, not the servers.

---

## P-569-A — SCORM courseware delivery into an untouched LMS (4–6 weeks)

**For:** any client whose platform of record is copyleft (Moodle, Open edX,
Canvas, Chamilo) and who wants **AI-generated or AI-assisted courseware delivered
into it** without a platform project, an xAPI migration, or an LTI integration
review.
**Region:** Global. Strongest fit where procurement specifies SCORM by name,
which in practice means corporate L&D, compliance training and public-sector
tenders.

**Why this pattern exists, and why it did not until now.** Three passes of this
KB built the attach doctrine on **LTI 1.3**, **MCP** and **xAPI** — launch, read,
telemetry — and omitted the one standard that moves *content inward*. xAPI is the
better specification and **SCORM is the incumbent**: every platform on
[`../verticals/solutions.md`](../verticals/solutions.md) ingests it, and
`Selleo/mentingo` ships it alongside xAPI because buyers ask for it. The fourth
pass located a permissive, maintained runtime, so the gap closes.

**Components — every licence read from the licence file on 2026-10-31:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| SCORM runtime | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | SCORM 1.2, SCORM 2004, cross-frame, `offline-first`. 362★, 85 forks, pushed 2026-10-30. |
| Deck/courseware generation | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (1,069 B) | 71,498★. Native `.pptx` with the **client's own template** — i.e. branding compliance, which is what kills generated-content pilots. |
| Interactive conversion | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (1,069 B) | 1,034★. Books → animated, narrated, interactive web experiences; already carries a `scorm` topic. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ its two annotated corpora are **CC BY-NC-SA 4.0**; bring your own corpus. See step 0. |
| Pedagogical check | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 1,143 teacher-qualification questions (CDPK 920, SEND 223). |
| Telemetry (optional) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | If the client wants learner data out as well as content in. |

**Wiring:**

1. **Establish the SCORM version the client's LMS actually consumes.** 1.2 and
   2004 are not interchangeable and the installed base is split. `scorm-again`
   supports both; the LMS decides which one you ship. Ask for a sample package
   that already imports successfully and match it.
2. **Generate the artefact, do not generate the package.** Produce decks with
   `ppt-master` against the client's own `.pptx` template, or interactive units
   with `Papermorph`. Keep generation separate from packaging so the quality gate
   sits between them.
3. **Gate before packaging.** Score every unit with `evaluators` rubrics for
   content quality and sample-check the generating model against
   `pedagogy-benchmark`. **A SCORM package is an opaque zip once imported** — the
   LMS will not tell you the content was wrong, and neither will the learner
   until the cohort has finished. This is the step that distinguishes the pattern
   from a content farm.
4. **Package with `scorm-again` and import through the client's normal course
   upload.** No LMS code is touched, no plugin is installed, no platform upgrade
   is blocked, and the licence boundary is never crossed — the GPL/AGPL platform
   simply consumes a file, which is exactly what it was built to do.
5. **Keep the source artefacts, version them, and hand them over.** The
   deliverable the client owns is the generator configuration, the template and
   the gated source units — not the zip. Re-packaging is then a build step.

**What the client is buying.** Courseware at a cadence their authoring team
cannot match, delivered through a route their platform team does not have to
approve. **What to be honest about:** SCORM telemetry is thin compared with xAPI
(completion, score, time — not behaviour), so if the engagement's value story is
learning analytics, this pattern is the wrong one and **P-568-A** with an LRS is
the right one. Say which is being bought.

---

## P-569-B — Courseware factory: syllabus in, gated multi-format units out (6–8 weeks)

**For:** a client with a large existing corpus — textbooks, lecture notes,
ministry curriculum PDFs, internal training manuals — and a mandate to turn it
into teachable material far faster than their authoring capacity allows.
**Region:** Global. The LMIC and ministry variant is noted at the end and it is
materially different.

**Why this is now possible and was not a pass ago.** The content-production layer
in [`../repos/foundations.md`](../repos/foundations.md) did not exist in this KB
before the fourth pass, because every sweep filtered on an education topic and
**the largest component carries none**. `hugohe3/ppt-master` is **MIT with
71,498★** — the largest permissively licensed repository anywhere in this
knowledge base, 1.4× DeepTutor — and it generates native PowerPoint from
documents or topics, with the client's own template, data-backed charts, and
**audio narration from speaker notes**. That last feature is a lecture-capture
path for free.

**Components — licences read first-hand 2026-10-31:**

| Role | Component | Licence | What it contributes |
| --- | --- | --- | --- |
| Deck and lecture generation | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** | Documents/topics → native `.pptx`: shapes, transitions, animations, charts, tables, **narration from speaker notes**, client templates. 5,578 forks. |
| Interactive/animated units | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** | Books → animated, narrated, interactive web experiences. For the material that should not be a deck. |
| Self-paced audio course | [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** | Topic → course of **2-minute audio lessons with cited sources**. The only generator here that starts from citations. |
| Document→study-page | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | **MIT** | PDFs/books/papers → traceable interactive pages with quizzes. 1,201★. |
| Retention layer | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** | Hands the pipeline a real spaced-repetition scheduler instead of reimplementing one. |
| Standards alignment | [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | **code MIT / data per publisher** | Checks units against academic standards and curricula; ships an MCP server. Clear each dataset individually. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) + [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT / CC BY 4.0** + **MIT** | ⚠️ `evaluators`' two annotated corpora are **non-commercial**; the golden set comes from the client's syllabus. |
| Delivery | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | Into the existing LMS (see **P-569-A**). |

**Wiring:**

1. **Classify the corpus by target format before generating anything.** Expository
   material → `ppt-master` decks. Narrative or conceptual material that benefits
   from motion → `Papermorph`. Material learners consume while commuting →
   `claudemy` audio. Reference material learners need to *search* →
   `learn-from-materials` pages. **Routing is the pattern's intellectual content;
   generating is the cheap part**, and a factory that sends everything through one
   generator produces 400 identical decks nobody opens.
2. **Pin the client's template and brand on day one.** `ppt-master`'s `.pptx`
   template support is the single feature that gets generated decks past an
   institution's communications team. Do this before volume, not after.
3. **Align to the standard, then gate on quality.** Run every unit through
   `knowledge-graph` for standards alignment, then `evaluators` rubrics for
   quality, then sample the generating model against `pedagogy-benchmark`. **Three
   checks, because they fail differently:** alignment catches off-syllabus,
   rubrics catch badly written, the benchmark catches a model that does not know
   how to teach.
4. **Attach spaced repetition rather than inventing it.** Emit flashcards from
   gated units into Anki via `anki-mcp-server`. Retention is the part of the value
   story a client can actually measure, and the scheduler is a solved problem.
5. **Package and deliver over SCORM** (P-569-A), keeping source artefacts and
   generator configuration as the versioned deliverable.
6. **Require citation provenance as an acceptance criterion**, and use `claudemy`
   as the reference for what that looks like in a generator rather than bolted on
   afterwards. The argument to make to an executive is on the public record:
   **South Africa's draft National AI Policy was withdrawn because at least 10% of
   its academic references were fictitious.**

**The LMIC / ministry variant.** Swap the front end: parse the national
curriculum with `AI-for-Education/lesson-plan-parse-mbsse` (MIT — real Sierra
Leone **MBSSE** lesson plans, PDF → structured JSON), align with
`AI-for-Education/gpf-alignment` (MIT) against the **Global Proficiency
Framework** where no rich national standard exists, deliver offline through
`learningequality/kolibri` (MIT) instead of SCORM, and add
`AI-for-Education/nemoasr-android` (on-device ASR) where literacy or devices are
the binding constraint. For vocabulary and language work,
[`orionsheep/wordlink`](https://github.com/orionsheep/wordlink) (MIT, 262★) runs
a fine-tuned 1.5B model **entirely in the browser via WebGPU** — no connectivity
and no inference bill, which is the only configuration that survives a
low-bandwidth classroom.

**What the client is buying.** Throughput with a quality floor, and the floor is
the product. **What to be honest about:** none of these generators knows whether
its output teaches. The gate is hand-built, the corpus behind it must be the
client's own for licence reasons as well as validity, and **nothing here monitors
the pipeline after go-live** — see the standing evaluation gap in
[`../intel/trends.md`](../intel/trends.md). Quote the gate as a permanent cost,
not a setup cost.

---

## P-570-A — Textbook-in, multi-format course-out: the client's own material as the starting point (6–8 weeks)

**For:** any institution or training provider that already owns the material —
textbooks, past papers, lecture PDFs, scanned worksheets — and wants it turned
into usable digital courseware. **This is the pattern the fifth pass's capability
sweep made possible**, and it inverts the usual pitch: it does not generate new
content that competes with the client's faculty, it **migrates what they already
have**.
**Region:** Global. Every component is permissive and every one runs on-premises.

**Why this pattern exists.** Four passes of this KB described the
content-*production* layer (`ppt-master`, `Papermorph`, `Claudemy`) and had no
**ingestion** layer at all, because every sweep filtered on an education topic
and no document parser carries one. The capability sweep returned sixteen
permissive components, three above 69,000★. **The ingestion step is the
commercially better place to start**: generating material competes with the
client's own authors, while ingesting their corpus is migration work — scopeable,
valuable, and not replicable with a chatbot subscription.

**Components — every licence read from the licence file on 2026-10-31:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Primary document → structured text | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** (1,072 B) | 69,909★. PDF/DOCX/**PPTX**/XLSX/HTML → markdown or JSON, **table structure preserved**. MIT, so the default choice. |
| STEM/formula-heavy fallback | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + additional terms** (3,301 B) | 82,860★. Best on formulas, tables, multi-column. **Carries a mandatory attribution duty — see step 5.** Branch `master`. |
| Scanned / handwritten input | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | **Apache-2.0** (11,376 B) | 92,024★. Strongest CJK and handwriting. For exam scripts and worksheets. |
| Offline OCR fallback | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (11,358 B) | 77,267★, 100+ languages, no model licence, no inference bill. The ministry/offline answer. |
| Mixed legacy estates | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** (11,360 B) | Use when the input is a repository of mixed formats rather than a book. |
| Knowledge structuring | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | **MIT** (1,090 B) | Knowledge Space Theory: material → knowledge graph → adaptive assessment. The pedagogical spine, from a named university. |
| Quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ corpora are **CC BY-NC-SA 4.0** — bring your own. |
| Deck output | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (1,069 B) | Native `.pptx` against the client's own template. |
| In-place document editing | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | **Apache-2.0** (11,375 B) | 32,854★. For "update our 400 existing lesson plans", which `ppt-master` cannot do. |
| Typesetting | [tw93/Kami](https://github.com/tw93/Kami) | **MIT** (1,061 B) | Layout rules so output does not look machine-made. The cheapest fix for teacher rejection. |
| Audio + captions | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** (1,069 B) | EPUB/PDF → narrated audio **with synchronised captions** — an accessibility deliverable, a transcript and a search index from one run. |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (1,079 B) | FSRS as an algorithm. Build it in; do not invent a review schedule. |
| Delivery | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | Package into the untouched copyleft LMS. See **P-569-A**. |

**Wiring:**

1. **Triage the corpus before writing any code.** Split the client's material
   into three buckets: born-digital text (→ `docling`), formula- and
   table-heavy STEM (→ `MinerU`), and scanned or handwritten (→ `PaddleOCR`, or
   `tesseract` where nothing may leave the premises). **The triage is the
   estimate** — mixing these in one pipeline is the usual reason this work
   overruns.
2. **Extract to a single intermediate representation** (markdown + JSON with
   structure preserved) and **keep it as the versioned asset.** Every later
   output is a render of it. This is also what makes the deliverable ownable:
   the client ends up owning their corpus in an open format, which has value
   independent of whatever is generated from it.
3. **Impose structure before generating anything.** Run `knowledge-spaces` to
   derive the knowledge graph and prerequisite ordering. Skipping this yields a
   pile of generated units with no learning sequence — the most common failure of
   AI courseware and the one a teacher spots immediately.
4. **Gate, then render.** Score units with `evaluators` rubrics; only then
   render to decks (`ppt-master`), edited documents (`OfficeCLI`), typeset PDFs
   (`Kami`) and narrated audio with captions (`abogen`). Attach FSRS scheduling
   to anything that needs retention.
5. **If `MinerU` is in the shipped pipeline, the attribution duty is a product
   requirement, not a legal footnote.** Its licence obliges any online service
   built on it to state prominently — in the interface or public documentation —
   that MinerU is used, with **automatic termination** on breach. Route this to
   the client's engineering and UX teams at design time. **If that is
   unacceptable to the client, use `docling` (MIT) and accept weaker formula
   handling** — that trade is the decision, and it belongs to the client.
6. **Deliver through SCORM into the untouched platform of record** (P-569-A), or
   over LTI 1.3 if a live tutor is also in scope (P-568-A).

**What the client is buying.** Their own institutional knowledge, in an open
structured format they own, rendered into every format their learners and
platforms need. **What to be honest about:** ingestion quality on degraded scans
is genuinely variable and no amount of model choice fixes a bad scan — quote a
**sample-based** accuracy measurement on the client's real documents before
committing to a volume price. Run that sample in week one.

---

## P-570-B — Accessibility remediation of the document estate (4–6 weeks)

**For:** public-sector education bodies, universities and school systems facing
an accessibility conformance obligation over a large back-catalogue of PDFs.
**Region:** **EMEA** primarily — the **European Accessibility Act** — and
**North America**, where updated **ADA** web-accessibility guidance has obliged
large public institutions since April 2026. Applicable anywhere procurement
specifies WCAG or PDF/UA.

**Why this pattern exists.** This KB has carried accessibility remediation as a
North American opportunity since the third pass with **no open-source component
behind it** — scoped as audit-only, via `canvas-mcp`'s accessibility-auditor
skill. The capability sweep found a remediation engine, so the offer can change
from *finding* defects to *fixing* them, which is a materially larger engagement.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| PDF accessibility automation | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | **Apache-2.0** (11,358 B) | 30,129★, Java, 2,881 forks. Topics include **`eaa`**, **`pdf-ua`**, `tagged-pdf`, `a11y`. **The only accessibility-as-a-feature asset in this KB.** |
| Structure extraction | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Heading hierarchy and table structure — the inputs tagging needs. |
| Scanned-document OCR | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** | A scanned PDF has no text layer and therefore **cannot** be made accessible without OCR first. |
| Audio alternative | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** | Narrated audio with synchronised captions as an alternative format. |
| Live-session captioning | [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | **MIT** (Collabora Ltd., **EMEA**) | Lecture captioning, where the obligation extends to live teaching. |
| LMS-side audit | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | Its accessibility-auditor skill, for the Canvas-resident content. |

**Wiring:**

1. **Inventory and classify.** Separate tagged PDFs, untagged born-digital PDFs
   and scanned images. Only the middle group is cheap; the third needs OCR first
   and the first may already pass.
2. **OCR the scans** (`tesseract`, on-premises — these are often student records).
3. **Extract structure** with `docling`, then **generate tagged, PDF/UA-oriented
   output** with `opendataloader-pdf`.
4. **Produce alternative formats** — narrated audio with captions (`abogen`) —
   because several conformance regimes accept an accessible alternative where
   remediating the original is disproportionate.
5. **Audit what stays inside the LMS separately** with `canvas-mcp`'s auditor.
6. **Deliver a conformance evidence pack**, not just fixed files: what was
   remediated, what was given an alternative, what was exempted and why.

**What the client is buying.** A regulator-facing evidence pack plus a remediated
estate, at a cost per document no manual process can match. **What to be honest
about: automated tagging is not conformance.** These tools produce structurally
tagged output; **WCAG and PDF/UA conformance requires human judgement** on
reading order, alt text and table semantics. Quote automation plus **sampled
human review**, and never let a client believe a tool signed off their legal
obligation. The evidence pack must say which documents a human checked.

---

## P-570-C — Efficacy trial for an AI tutor already in production (6–8 weeks)

**For:** a client who has deployed an AI tutor — often one bought or piloted
before this engagement — and is being asked by a board, a ministry or a funder
whether it actually works.
**Region:** Global. Strongest fit in **APAC** (Singapore's **AI Verify** makes
*evidence of testing* the deliverable; Korea's AI Basic Act imposes
human-oversight duties on high-impact education AI) and in **EMEA**, where Annex
III conformity work will need evidence of performance.

**Why this pattern exists, and its limits stated up front.** Six consecutive
passes of this KB have recorded that **no education-specific agent observability
or runtime regression tooling exists**. That is still true. What this pass found
is the adjacent thing: an **Apache-2.0 randomised-controlled-trial platform**
that attaches to the LMS over LTI. **It answers "did this intervention change
outcomes" and not "has the tutor degraded since Tuesday."** Both questions get
asked; only the first now has an open-source answer, and conflating them is the
mistake this pattern exists to prevent.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Randomised trial harness | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** (11,323 B) | LTI plug-in: treatment variation inside real assignments, random assignment, **informed consent hidden from the teacher**, non-consenting students filtered from exports, identifiers stripped. Branch `development`. ⚠️ Licence names no licensor (template placeholders). 21★ — small. |
| Pedagogical-knowledge baseline | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 1,143 teacher-qualification questions. Measures whether the model knows how to *teach*. |
| Output-quality rubrics | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **code MIT / prompts CC BY 4.0** | ⚠️ **corpora CC BY-NC-SA 4.0 — the regression suite must source its own corpus.** |
| Mastery measurement | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** (1,073 B) | BKT behind MCP — an independent mastery estimate, not the tutor's own self-report. |
| Behavioural telemetry | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS. The event stream the trial analyses. |

**Wiring:**

1. **Fix the outcome measure before touching the tutor.** Assessment scores,
   completion, or an independent mastery estimate from `tutor-mcp` — decided and
   written down first. A trial whose outcome is chosen after the data arrives is
   not a trial.
2. **Get the ethics apparatus in place early, because it is the long pole.**
   `terracotta`'s consent model (hidden from the teacher, non-consenting students
   filtered from exports, identifiers stripped) is designed for exactly this, but
   institutional review timelines are measured in weeks and run in parallel with
   nothing. Start day one.
3. **Randomise within assignments, not between classes.** Class-level assignment
   confounds the teacher with the treatment, which is the standard way education
   pilots produce uninterpretable results. `terracotta` varies content *inside*
   an assignment for this reason.
4. **Stand up a model-side baseline too** — `pedagogy-benchmark` for pedagogical
   knowledge, `evaluators` rubrics on generated output, **on a corpus the
   engagement sources itself** (the bundled CLEAR and PERSUADE 2.0 corpora are
   non-commercial and cannot ship in a billable deliverable).
5. **Stream telemetry into `ralph`** so behavioural data is available alongside
   outcome data.
6. **Report the null if it is null.** The commercial value here is the client's
   ability to defend a decision to a board or a regulator, and a trial that can
   only produce good news defends nothing.

**What the client is buying.** Defensible evidence about a system they already
run — the artefact a funder, ministry or Annex III conformity assessment asks
for. **What to be honest about, twice over:** `terracotta` is a **21★** project
and should be treated as a methodology implementation to be understood and
possibly forked, not as vendor software; and **this is not monitoring.** If the
client's actual question is "will we know when it breaks", the answer today is
that they will need a bespoke harness, because open source does not supply one —
which is also, as this KB has recorded for six passes, the clearest unmet build
opportunity in the industry.

---

## P-571-A — Defensible assessment pipeline: model-authored items, human-provable marking (8–10 weeks)

**For:** exam boards, awarding bodies, universities with central assessment
units, and any client whose marking will be automated and audited.
**Region:** **EMEA** primarily — the EU AI Act's **Annex III** category
*evaluation of learning outcomes*, obligations landing **2 December 2027** — and
**North America**, where the binding constraint is student-data law rather than
conformity assessment (California's proposed A.B. 1159; Idaho's bias-evaluation
and privacy duties). Applicable in **LATAM** wherever a *secretaría* must show a
regulator what was marked and by whom.

**Why this pattern exists.** Five passes of this KB recorded *"nothing permissive
generates psychometrically defensible items"* and went looking for a generator.
The sixth pass found that the buyable artefact is the **gate**, not the generator
— and the gate is what the regulation actually demands evidence of. This pattern
is the first in this KB that can answer *"prove a human marked everything a
machine could not defensibly mark."*

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Source-material ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client's own syllabus, textbooks and past papers → markdown/JSON with table structure. The items must be grounded in the client's curriculum, not the model's memory. |
| STEM/handwriting ingestion | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + commercial thresholds** | Formulas and multi-column STEM papers. ⚠️ Its **prominent-attribution clause binds any online service** built with it — that reaches UX, not just legal. |
| **Item authoring contract** | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | 🟢 **The load-bearing component.** Markdown banks, `itembank lint` **blocking on error**, `itembank guard` failing CI on committed real banks, deterministic scoring, **short-answer never auto-graded**. |
| Rubric quality gate | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA** | Scores generated content against research-backed rubrics. ⛔ **The two annotated corpora are non-commercial — bring your own corpus for a billable regression suite.** |
| Cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** | Infers learner mastery from responses. ⚠️ **Not item calibration** — see the honest limit below. |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | FSRS, which `itembank` already implements — use the library form if you need it outside the bank. |
| Telemetry store | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS: every item served, every response, every human override, timestamped. **This is the audit trail.** |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | What the assessment board looks at. `potsie` is Jsonnet, so dashboards ship as reviewable code. |
| Drift baseline | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** | Regression and drift on the authoring model's output distribution. 🔴 The **only** permissive option — see the licence warning below. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch into Moodle/Canvas/Open edX without touching platform code. |

**Wiring:**

1. **Ingest the client's curriculum** with `docling` (and `MinerU` for STEM
   papers). Every item must trace to a source document — provenance is the first
   thing an auditor asks for.
2. **Author items with the model into `itembank`'s markdown format**, never
   straight into a database. The format is the contract.
3. **Gate in CI, not in review.** `itembank lint` blocks the merge on error —
   unexplained distractors, answer-position skew, select/key mismatch, duplicate
   stems. `itembank guard` keeps live banks out of the repository. 🟢 **A model may
   author; it may not merge.**
4. **Score deterministically.** Objective items score in `itembank`'s own runtime
   with **no model in the path**; `check` items run learner code against hidden
   cases. **Short-answer items are routed to a human rubric marker and stay
   pending** — this is the step that produces the conformity evidence, so
   instrument it rather than optimising it away.
5. **Layer rubric scoring as advisory only** (`evaluators`) on generated
   *content*, never as a score of record.
6. **Emit xAPI to `ralph` at every transition** — item served, response, lint
   verdict, human override, final mark. Surface it in `warren`/`potsie`.
7. **Baseline the authoring model in `evidently`** and re-run on every model or
   prompt change, so "the item quality changed in March" is answerable.
8. **Deliver a conformity pack**: the lint ruleset, the CI logs, the
   human-marking record, the drift baselines, and a written statement of which
   decisions were automated and which were not.

🔴 **Honest limits — state all four to the client before quoting.**

- **`itembank` gates items; it does not calibrate them.** There is **no live,
  permissive, education-specific item-calibration asset** on this base:
  `eribean/girth` (MIT) last shipped **2022**, `inuyasha2012/pypsy` (MIT)
  **2018**, `meyerjp3/psychometrics` (the most capable, Java) has **no licence
  file at all**, and the R options are copyleft. `EduCDM` does cognitive
  diagnosis. **Difficulty parameters mean a stale dependency, a licence risk, or
  a build.**
- **`itembank` ships no QTI.** Interchange (QTI/CASE/SCORM) is explicitly
  backburner — the README says it *"waits for a named consumer."* 🔵 If the client
  needs QTI, this pattern needs a build step or `tremby/questionbank` (⚠️ **CC BY**),
  and the engagement could be that named consumer.
- **`itembank`'s MCP surface is unshipped** ("Phase 999.3") and its wider course
  workspace is not yet runnable. Integrate over its **key-free JSON session
  protocol** (`start`/`next`/`submit`/`report`/`teach`), which does work.
- ⛔ **Do not reach for `Arize-ai/phoenix` for the observability slot.** It is
  **Elastic License 2.0**: *"You may not provide the software to third parties as
  a hosted or managed service."* For a studio that hosts and operates client
  solutions that is a **prohibition, not a threshold**, and it also forbids
  disabling its licence-key mechanism. ⚠️ `langfuse/langfuse` is usable but is
  MIT-Expat **only outside** `ee/`, `web/src/ee/`, `worker/src/ee/` and
  `packages/shared/src/server/ee/` — a build-configuration requirement. 🟢
  `evidently` is the clean pick.

## P-571-B — Lecture-video factory that never leaves the client's infrastructure (6–8 weeks)

**For:** ministries, national operators and universities that must produce
narrated courseware at volume **and** cannot send student or curriculum material
to a third-party cloud.
**Region:** **APAC** primarily — Vietnam's AI law duties by **1 March 2027**
(grace for education systems operating before **15 August 2026**), Taiwan's **AI
Basic Act** in force **14 January 2026**, Indonesia's **GR 71** data residency —
and **LATAM**, where widening compute and connectivity gaps argue for local
inference. In **EMEA** the driver is different: the **European Accessibility
Act** makes captions a procurement gate.

**Why this pattern exists.** The fifth pass asked for a `topic:video` sweep. The
sixth ran it and found **no open-source lecture-video product to adopt** — but a
well-understood four-stage pipeline (slides → page images → narration script →
TTS and mux) with a permissive component at every stage. 🔴 **Three of the four
pipelines found terminate in Amazon Polly and require AWS credentials**, which
disqualifies them by default for exactly the clients who need this most. The
pattern is the pipeline **with the TTS stage swapped**.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Reference pipeline | [galaxyproject/video-lectures](https://github.com/galaxyproject/video-lectures) | **MIT** (1,071 B, "Galaxy Project") | Pandoc → HTML slides → `wkhtmltoimage` page images → script extraction → mux. 🔴 **Replace its Polly stage.** |
| Narration/assembly engine | [jhudsl/ari](https://github.com/jhudsl/ari) | **MIT** (declared in `DESCRIPTION`) | R package, **Johns Hopkins Data Science Lab**. ⚠️ Its grant is **not** in `LICENSE` — that file is a 40 B stub. |
| Local-voice pipeline | [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) | **MIT** (1,070 B) | 🟢 **The sovereignty pick** — PDF deck + script, slides split on `NEWSLIDE`, with **optional local voice cloning**. The only row on this axis that needs no cloud TTS at all. |
| Script drafting | [htlin222/slides-to-video](https://github.com/htlin222/slides-to-video) | **MIT** (1,065 B) | Drafts **speaker notes** from the slides, then TTS + `ffmpeg`. Use when the client has decks but no narration scripts. |
| Captioned audio | [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** | 🟢 Emits **synchronised captions** — the EAA/WCAG deliverable, not an extra. |
| On-device TTS | [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | **MIT** | Apple Silicon. ⚠️ `supertonic` (MIT, on-device) is **archived** — grant perpetual, patches not. |
| Source ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client's existing textbooks and decks → structured markdown to drive the slides. |
| Lesson construction | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | Topic or documents → slides, quizzes, whiteboard; **exports PPTX and single-file offline HTML**, which feeds this pipeline directly. |
| Delivery into the client LMS | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (1,072 B) | SCORM 1.2 / 2004 runtime, `offline-first`. Ships the finished units into the incumbent LMS **without touching it**. |
| Telemetry | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI record of what was delivered and watched. |

**Wiring:**

1. **Ingest** the client's existing material with `docling`; keep a
   source-to-slide map so every claim on a slide is traceable.
2. **Build the lesson** — `OpenMAIC` for interactive units (it exports PPTX and
   offline single-file HTML), or author markdown slides directly for the
   `galaxyproject` pipeline.
3. **Render page images** (`wkhtmltoimage`, or ImageMagick on the
   `slides-to-video` path).
4. **Produce the narration script.** Have `htlin222/slides-to-video` draft
   speaker notes where none exist, then **put them through human review** — this
   is a content-accuracy gate, and in the EU the **transparency duty on
   synthetic teaching material has been live since 2 August 2026**.
5. 🟢 **Synthesise locally.** `Changochen/slide-to-video`'s local voice cloning,
   or `mlx-audio`/`abogen`. **Do not configure Polly**; that single default is
   what would otherwise breach the client's residency position.
6. **Generate captions with `abogen`** as a first-class output, not a retrofit.
7. **Package with `scorm-again`** and deliver into the incumbent LMS; emit xAPI
   to `ralph` for what was actually watched.

🔴 **Honest limits.** Every component on this axis is **tiny** — 2★ and single
digits, against a document layer where five repositories clear 30,000★. 🔵 These
are *scripts to assemble*, not products to adopt, and the estimate must say so:
the engineering is in the integration and the voice quality, not in the
components. ⛔ **`harry0703/MoneyPrinterTurbo` (MIT, 136,744★) is explicitly not
in this pattern** — it is short-form social video, and its star count makes it the
most likely asset to be mis-offered here as courseware tooling.

## Declared gaps

- **No pattern for Blackboard, Brightspace or Google Classroom.** No agent
  population for these platforms reached verification this run, so no recipe is
  offered rather than a speculative one.
- ~~**No Africa-specific pattern.**~~ **Closed on the second pass of
  2026-10-31**: the regional demand and policy evidence was found, and the
  pattern is written up as **P-568-F** above, with Kolibri (MIT) as predicted
  plus DSpace (BSD-3-Clause). Its own caveats are stated in place.
- **No Canada pattern, deliberately.** Canadian findings are now in
  [`../intel/market.md`](../intel/market.md), but the two engagement shapes are
  **P-568-C run per board** (Ontario — ~58% of boards have no student AI policy
  and no ministry template is coming) and a reinstatement case in Quebec, where
  a **March 2025 directive suspended AI assistants**. Same artefacts, different
  trigger, so no new recipe — but **francophone delivery is a hard requirement**
  in Quebec, which is a staffing constraint rather than a technical one.
- ~~**No APAC pattern.**~~ **Closed as P-568-H above**, on evidence the previous
  pass did not have: TEQSA's 100%-response institutional census and the AJET
  finding that only **7 of 39** Australian universities document operational
  governance. The driver turned out to be **award integrity**, not conformity
  assessment, which is why it is a pattern and not a per-jurisdiction run of
  P-568-D.
- ~~**No pattern uses an EMEA-origin agent.**~~ **Partly closed.** The *agent*
  layer in EMEA is still imported, but **P-568-J** is built on an EMEA-origin
  permissive **platform** (`Selleo/mentingo`, MIT, Poland) and composes an
  entirely EMEA-origin permissive stack with `ralph` (France) and
  `pedagogy-benchmark`. **LATAM remains unclosed and the reason is now specific:**
  the one LATAM-origin agent found (`digitalinnovationone/dio-agent`, 2,750★) is
  **unlicensed**, so it cannot enter a pattern. It is evidence of demand, not a
  component.
- ~~**Africa's supply side is unmapped.**~~ **Closed, and P-568-F should be
  revised to use it.** `AI-for-Education` (MIT, LMIC-focused) publishes a Sierra
  Leone **MBSSE** lesson-plan parser, Luganda benchmarks, Global Proficiency
  Framework alignment, and on-device Android ASR for no-connectivity classrooms —
  see [`../repos/foundations.md`](../repos/foundations.md). Every repo is 0–13★,
  so local partnership stays part of the pattern, but P-568-F no longer has to
  compose *entirely* imported components. **Next pass: rewrite P-568-F around
  these components rather than around Kolibri alone.**
- ~~**No pattern delivers content *into* the platform of record.**~~ **Closed as
  P-569-A.** Three passes built the attach doctrine on LTI, MCP and xAPI —
  launch, read, telemetry — and never noticed that **nothing moved courseware
  inward**, which is what procurement actually asks for and what every platform
  on this KB's own verticals page ingests. `jcputney/scorm-again` (MIT, 362★,
  SCORM 1.2 + 2004) closes it. The gap survived three passes because the doctrine
  was built from the *integration* literature, where xAPI is the modern answer,
  rather than from what a buyer specifies.
- **The content-production layer arrived late and the next pass should expect
  more of it.** `ppt-master` (**MIT, 71,498★**) is the largest permissively
  licensed repository in this KB and went unfound for four passes because every
  sweep filters on an education topic and it carries none. **P-569-B** is built on
  it. Assume the same blind spot still hides document parsers, TTS pipelines,
  assessment-item generators and video tooling: sweep by **capability**
  (`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`, `topic:scorm`)
  crossed with licence.
- **Every quality gate in this file now has a licence boundary through it.**
  `evaluators` is code-MIT / prompts-CC-BY-4.0 / **corpora-CC-BY-NC-SA-4.0**, and
  the upstream corpora are NC too. So the golden set in **P-568-K**, **P-569-A**
  and **P-569-B** must be built from the client's own syllabus — which is better
  practice and is now also a licence requirement. **It is also an unbudgeted
  line in most proposals**, and the main reason these three patterns should not be
  quoted from their component list alone.
- **No pattern uses `academico` yet.** `academico-sis/academico` (MIT, 410★,
  151 forks, `student-information-system`) is the permissive education SIS whose
  non-existence this KB asserted for three passes. It is a real option for a
  small-or-medium-institution client and there is no recipe built on it. **Next
  pass: a permissive-SIS pattern for the language-school / training-institute /
  private-school-group buyer**, which is a different buyer from every pattern
  currently in this file.
- **No pattern has been run end to end.** Every recipe here is composed from
  verified components with stated licences; none has been executed on a client
  engagement by this KB. Durations are estimates, not measured delivery times,
  and should be presented as such.

---

## P-572-A — Item calibration and score equating, with the assurance a 0★ library cannot supply (6–8 weeks)

**For:** any client in `P-571-A`'s position who has to defend a *score*, not just
a marking process — awarding bodies issuing grades, universities with placement
testing, certification programmes running multiple test forms a year.
**Region:** **EMEA** first (EU AI Act **Annex III**, *evaluation of learning
outcomes*, obligations landing **2 December 2027** — a conformity assessment will
ask how item parameters were estimated and how two forms were made comparable),
then **North America** for certification bodies under accreditation review.
Applies in **APAC** and **LATAM** wherever a ministry equates a national test
across sittings.

**Why this pattern exists, and why it could not exist last pass.** `P-571-A`
ships a defensible *marking* pipeline and closes with an admission: items could
be authored and gated permissively but **not calibrated**. 🟢 That is no longer
true — [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) (**MIT**,
dependency-free TypeScript) implements the calibration, adaptive-administration
and **equating** layer. 🔴 **But it is `0.1.0`, one author, 0★ and unpublished to
npm, so this pattern is half library and half assurance work.** The assurance
half is the billable, defensible part and it is specified here rather than left
implied.

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Item authoring + blocking gate | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | Carried from `P-571-A`. Produces the gated bank this pattern calibrates. Exports **answer-key TSV** — that is the response-matrix interface. |
| **Calibration + CAT + equating** | [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** (1,064 B) | 🟢 **Load-bearing.** 2PL/3PL **and** graded-response / partial-credit / generalized-partial-credit; **marginal maximum likelihood** (and joint, with its structural bias demonstrated); **four linking methods**; **DIF**; person-misfit; score→ability tables with SE. **Zero runtime dependencies** — verified from `package.json`. |
| **Reference implementation (assurance, not runtime)** | [eribean/girth](https://github.com/eribean/girth) | **MIT** | 🔴 Stale since **2022-09-09** — and that is *fine for this role*. A frozen, independently written MIT estimator is exactly what you want to cross-check `calibrate`'s MML output against. **Pin it, do not ship it.** |
| Gain validation | [finite-sample/guess](https://github.com/finite-sample/guess) | **MIT** (via `DESCRIPTION`) | R. Latent-class correction using **pre/post transitions** — answers "is this gain real or is it guessing?" after the scores are on one metric. |
| Cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** | Mastery inference for reporting. ⚠️ Still **not** calibration — keep the roles distinct in the report you hand the client. |
| Telemetry store | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS. Every administered item, response and ability estimate, timestamped — the evidence trail the equating argument rests on. |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | Item-parameter drift and form-comparability panels as reviewable Jsonnet. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch; the adaptive session runs beside Moodle/Canvas, never inside it. |

**Wiring:**

1. **Export the gated bank** from `itembank` as answer-key TSV, and hold a
   pilot administration (paper or fixed-form) to get a response matrix. You
   cannot calibrate without responses; budget this as a real data-collection
   step, not a sprint task.
2. **Calibrate twice, on purpose.** Run `calibrate`'s `fit` (joint) and `mml`
   (marginal) over the same matrix. The library demonstrates JML's structural
   bias itself; **record both and report MML.** Divergence beyond expectation is
   a data problem, not a library problem, and you want it surfaced here.
3. 🟢 **Build the assurance artefact — this is the step that answers the 0★
   objection.** Estimate the *same* matrix with `girth` and diff the item
   parameters. Keep the diff, the seed and the matrix in the repository as a
   committed fixture. **Two independently written MIT estimators agreeing to a
   stated tolerance is evidence; a star count never was.** Re-run it in CI on
   every `calibrate` bump.
4. **Screen for DIF** across the demographic splits the client is accountable
   for before any item reaches a live form. Annex III conformity work will ask;
   so will any North American bias-evaluation duty.
5. **Equate the forms.** Use `calibrate`'s linking methods over a common anchor
   set to put sittings on one metric, and publish the score→ability conversion
   table *with its standard errors*. Run all four methods; if they disagree
   materially your anchor set is too thin, which is a finding you want before
   results day, not after.
6. **Administer adaptively** through the LTI launch, with maximum-information
   selection and a precision stopping rule. Stream every event to `ralph`.
7. **Validate observed gains** with `guess` on the pre/post transitions, so a
   reported improvement is net of guessing.
8. **Panel it** in `warren`/`potsie`: item-parameter drift between sittings,
   anchor stability, form comparability, DIF flags.

**What to tell the client, in one sentence.** *The whole chain — authoring,
gating, calibration, DIF, equating, gain validation — is permissively licensed
and self-hosted, and the calibration engine is eight weeks old, so you are
buying a cross-validation harness as part of the delivery.* 🔴 **Do not present
this stack as mature.** The honest pitch is that the alternative is a per-seat
psychometrics licence and a vendor who will not show you the estimator.

**Effort:** 6–8 weeks on top of `P-571-A`. Roughly half of it is steps 3 and 5 —
the cross-validation harness and the equating argument — and that split is the
point.

---

## P-572-B — Adopting a measurement-first learning platform without inheriting its AGPL obligation (4–6 weeks)

**For:** a client who wants `AI Learning OS`'s audit pipeline — equivalent
pre/post testing, CTT item analysis, mastery validity, metacognitive calibration,
effect sizes gated in CI — delivered as a **hosted** service by Globant.
**Region:** **APAC** as found (HarmonyOS target, `ChinaTextbook` integration),
but the pattern is region-neutral; the licence surgery is the same anywhere.

**Why this pattern exists.** [`swsgbl/ai-learning-os`](https://github.com/swsgbl/ai-learning-os)
is the only platform on these shelves whose selling point is **proving learning
happened** rather than delivering content, and at **1★ / 1,313 commits** it is a
real codebase. 🔴 **Its `main/LICENSE` says MIT and that answer is incomplete:**
its own `NOTICE.md` puts `services/api/` under **AGPL-3.0 combination
obligations**, because it links **PyMuPDF (AGPL-3.0)** in-process. Host that over
a network and §13 obliges you to hand your deployment's source to its users.
🟢 **The whole pattern is: remove one dependency, keep the platform.**

**Components:**

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Platform | [swsgbl/ai-learning-os](https://github.com/swsgbl/ai-learning-os) | ⚠️ **MIT root; AGPL-3.0 on `services/api/`** | Clients (`apps/web`, `apps/android`, `apps/harmony`) and `services/console` are **MIT and untouched** by this work. |
| ⛔ Dependency to remove | **PyMuPDF** | ⛔ **AGPL-3.0** | The single cause. Used for PDF textbook parsing — page anchors and outline. |
| 🟢 Replacement parser | [py-pdf/pypdf](https://github.com/py-pdf/pypdf) | **BSD-3-Clause** | Outline and page-level extraction. First choice for structure. |
| 🟢 Replacement parser | [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | **MIT** | Better word/table geometry where page anchors must be precise. |
| Scanned-book OCR | **rapidocr-onnxruntime** + **onnxruntime** | **Apache-2.0** · **MIT** | Already in the platform's dependency table and already permissive — **no change needed.** |
| Retention | **py-fsrs** | **MIT** | Already permissive. Same FSRS algorithm as `itembank` and `fsrs4anki`. |
| Local speech | **funasr** · **CosyVoice** | **MIT** · **Apache-2.0** | Already permissive. 🟢 **Keep these: local ASR/TTS is why voice audio never leaves the client's infrastructure.** |
| Assessment upgrade (optional) | [onionviolet/itembank](https://github.com/onionviolet/itembank) · [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** · **MIT** | Its audit pipeline is **CTT**. Bolt `P-572-A` on where the client needs IRT and equating. |

**Wiring:**

1. **Read `NOTICE.md` first and put it in the engagement record**, not the
   licence file. 🔴 **The lesson generalises past this repo: for a platform, the
   licence surface is the dependency manifest, not `LICENSE`.** A
   `raw.githubusercontent.com/.../LICENSE` read — the standard instrument —
   returns `MIT` here and misses an AGPL network obligation entirely.
2. **Fence the blast radius.** Everything except `services/api/` is MIT. Confirm
   the client's hosted surface and check whether `services/api` is even in it;
   if the deployment is private and single-tenant with no third-party users,
   §13 may not trigger and the cheapest answer is a documented legal position
   rather than code.
3. **Swap the parser** where it does trigger. Isolate PyMuPDF behind the
   existing parse interface, reimplement page-anchor and outline extraction on
   `pypdf` (fall back to `pdfplumber` where geometry matters), and keep the
   platform's own parser tests as the acceptance criterion.
4. **Prove the removal.** `pip`-tree the service and assert no AGPL-licensed
   package remains; make that assertion a **CI gate**, so a future dependency
   bump cannot reintroduce the obligation silently. This is the deliverable the
   client's counsel will ask for.
5. **Keep the audit pipeline intact.** The mastery-simulation validity study,
   metacognitive calibration (gamma) and pre/post effect sizes are the reason
   for the engagement — regression-test them before and after the swap and show
   the numbers unchanged.
6. **Alternative, priced honestly:** `NOTICE.md`'s other exit is a **commercial
   PyMuPDF licence from Artifex**. If the client's timeline is shorter than the
   swap, buy it and say so. ⚠️ Per-deployment cost, forever, versus a bounded
   one-off engineering task — that is the trade, and it is the client's call.

**Effort:** 4–6 weeks. Step 3 dominates; steps 1, 2 and 4 are days and carry
most of the risk reduction.

---

## P-572-C — Sub-floor supply census: find the open-source layer a star-sorted search cannot see (1 week, reusable across industries)

**For:** Globant's own studio practice, at the start of any engagement where
"we checked and there is no open-source option for X" would otherwise go in a
deck.
**Region:** **Global** — and it is the only pattern here whose value is highest
in **LATAM**, **EMEA** and **APAC**, because non-English, non-US-institutional
projects attract stars last and are therefore the most systematically hidden by
a star sort.

**Why this pattern exists.** This KB ran the same star-sorted discovery for six
passes and concluded three axes were saturated. 🔴 **They were saturated at the
floor, not in the field:** `topic:ai-tutor` answers **816** results sorted by
stars and **793** at `stars:<50`. 🟢 **One sweep of the band produced 13
addresses new to this base, against 0 from eight keyword search legs** — and two
of those 13 closed gaps this KB had published for five and six passes
respectively. The method, not the industry, was the limit.

**Components (all standard tooling — this is a method, not a stack):**

| Role | Tool | Note |
| --- | --- | --- |
| Discovery | `github.com/search?q=topic:<axis>+stars:<50&s=updated&o=desc` | 🔴 **Sort by `updated`, not stars** — inside the band, stars are pure noise (`3,2,1,1,0,0,…`). |
| Licence gate (**runs first**) | `raw.githubusercontent.com/<r>/{main,master}/{LICENSE,LICENSE.md,LICENSE.txt,LICENCE,COPYING}` | 🔴 This band is where ungranted repos concentrate: **2 of 13** here carried no grant at 5 filenames × 2 branches. Gate before you read. |
| Manifest gate (**second**) | `package.json` · `DESCRIPTION` · `pyproject.toml` · `NOTICE.md` | 🟢 Catches what `LICENSE` cannot: an R package's real grant (`guess`), and an AGPL obligation reaching one directory through one dependency (`ai-learning-os`). |
| **Ranking signal** | `git clone --filter=blob:none` + `git rev-list --count HEAD` | 🟢 **The discriminator.** Blobless, so it is cheap; exact, so it is not a rendered figure. |
| Absence-claim check | [`../ingest/absence-claims.py`](../ingest/absence-claims.py) | 🟢 Run it against your own findings page before publishing an absence. |

**Wiring:**

1. **Name the axes as topics, not keywords.** Keyword search legs returned **0**
   new addresses six passes running; `topic:` + a star bound returned 13 in one.
2. **Pull the band sorted by recency**, 10–30 rows per axis. Record the
   `total_count` — a null with no denominator is not a finding.
3. **Gate on licence before reading anything else.** Five filenames × two
   branches over `raw.githubusercontent.com`. 🟢 Accept on a **property test** —
   OSI-approved, no copyleft, no network clause — which admits `ISC`, `0BSD`,
   `Unlicense`, `MIT-0`, and not on a name list.
4. **Read the manifest even when `LICENSE` answered.** `ai-learning-os` reads MIT
   at `LICENSE` and carries an AGPL-3.0 network obligation in `NOTICE.md`.
5. **Rank by commits, and split the field.** Blobless-clone the survivors and
   `rev-list --count`. Expect a clean separation: here, **4 above 200 commits**
   and **5 at or below 9**, the latter first-committed within 48 hours.
   🔴 **Recency puts a two-commit announcement and a 1,313-commit platform on the
   same page; only the commit count tells them apart.**
6. 🔴 **Apply the right floor per layer.** Commit density for **tooling**
   (`calibrate`: 0★/214 commits, shelved). Stars for **tutors and agents**, where
   stars *are* the adoption evidence (`voyage` 1★/224 commits, **not** shelved).
   Promoting a 1★ tutor to a client deck is the failure mode this step prevents.
7. **Re-check your own absence claims** with `absence-claims.py` before the deck
   ships. It found this base publishing a gap its own shelf had closed.

**What this buys an engagement.** Two closed gaps and thirteen addresses for
about a week of one person's time — and, more valuable, it stops the studio
telling a client to *build* something that already exists permissively.
🟢 **Nothing in this pattern is education-specific; run it unchanged on gaming,
legal, financial, healthcare, media, retail, travel, technology, automotive,
energy and enterprise.**

**Effort:** 1 week per industry, 3 axes. Repeat quarterly, not hourly — the band
turns over fast but a quarter is the shortest interval over which a commit
history means anything.
