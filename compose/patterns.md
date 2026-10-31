---
industry: education
region: Global
updated: 2026-10-31
---

# Compose patterns — education

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
