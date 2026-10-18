---
industry: education
region: Global
updated: 2026-10-18
---

## 🔴 Pass 291 — the foundation layer gained NO NEW ROW, and what changed instead is that an existing row's grant is now verified across **all seven** of its repositories

⏱️ **Thirteenth pass of `2026-10-18`.** Evidence:
[`submodule-pin-grant.2026-10-18-p291.tsv`](../evidence/submodule-pin-grant.2026-10-18-p291.tsv) ·
[`p291-websearch.2026-10-18-p291.tsv`](../evidence/p291-websearch.2026-10-18-p291.tsv).

🔴 **No new foundational repository this pass, and the reason is the finding.** The mandated
agent leg returned its **seventeenth** consecutive nil and the trending leg its **eighth** for
education; both returned the same agent-engineering curricula they have returned since `p275`.
🔵 A filler row would be worse than the gap: `p288` set that precedent and it holds.

🟢 **What did change is verification depth, not breadth.** The `iblai` configuration set
already on these shelves was carried on **2 of its 7** repositories. All seven are now read
**at the commit the superproject pins** — `GRANTED-AT-PIN`, `MIT`, one root `LICENSE` each,
every payload byte-identical (1 063 B, sha256₁₂ `f1269b7b2313`):

| repository | pinned gitlink | files at the pin | grant |
|---|---|---|---|
| [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) | `1a2d898bbd04` | 90 | 🟢 MIT |
| [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | `54ee9d91eecd` | 79 | 🟢 MIT |
| [`iblai/enterprise-agents`](https://github.com/iblai/enterprise-agents) | `7f00879a9f57` | 77 | 🟢 MIT |
| [`iblai/government-agents`](https://github.com/iblai/government-agents) | `fbf903250c96` | 77 | 🟢 MIT |
| [`iblai/legal-agents`](https://github.com/iblai/legal-agents) | `b059cd452bf3` | 75 | 🟢 MIT |
| [`iblai/financial-services-agents`](https://github.com/iblai/financial-services-agents) | `6ea18f015b1e` | 78 | 🟢 MIT |
| [`iblai/medical-healthcare-agents`](https://github.com/iblai/medical-healthcare-agents) | `cd0d9fcfa523` | 76 | 🟢 MIT |

🔵 **The technique is the transferable part, and it is cheap.** A submodule's grant does not
have to be read at `HEAD` and then reconciled against the pin:
`raw.githubusercontent.com/<owner>/<repo>/<pinned-sha>/LICENSE` serves the payload **at the
pin**, which is the commit a `--recurse-submodules` clone actually lands on. 7/7 answered
`200`. Any foundational row that is a submodule of something else can be verified this way,
and [`gate-pin-grant`](../compose/code/p291-submodule-pin-grant/README.md) now requires it.

🔴 **A standing caution this pass re-measured, unchanged:** `api.github.com` and `github.com`
HTML both answer `403` from this environment. No star count on this shelf is first-hand.

## 🟢 Pass 290 — the early-warning layer gets its first two foundational rows, and one of them is a US STATE EDUCATION AGENCY's own code

⏱️ **Twelfth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`p290-websearch.2026-10-18-p290.tsv`](../evidence/p290-websearch.2026-10-18-p290.tsv).

🔵 **Why these are foundations and not agent rows.** Neither is an agent and neither wants to
be. They are the **measurement layer** underneath `retention-agent` and
`special-education-agent`: the thing that produces a risk score an agent then has to act on
without treating it as a verdict.

| repo | grant (read from payload) | what it gives you | base for AI? |
|---|---|---|---|
| 🟢 [`cedanl/student-signal`](https://github.com/cedanl/student-signal) | 🟢 **MIT** — root `LICENSE`, **1 078 B**, HEAD `4463e8d17cfb`, sha256₁₂ `2c4289f4e480` | 🇳🇱 Dropout prediction as a **domain library**: `prepare()` cleans and transforms, `rank()` orders students by predicted probability, `evaluate()` reports **precision/recall at multiple invitation thresholds** with a traffic-light status. Bring any sklearn-compatible estimator. **Invitation-rule methodology (Eegdeman, 2022)**. 36 files, Python 3.13+, `uv`, CI/docs/publish workflows, 4 test modules, synthetic demo data committed | 🟢 **yes — the cleanest foundation found for this layer.** It deliberately does NOT choose your model, so the agent layer sits on top without a rewrite |
| 🟡 [`jknowles/EWStools`](https://github.com/jknowles/EWStools) | 🟡 **GPL-3.0 only** — root `LICENSE`, **35 156 B**, sha256₁₂ `65a7aee2cb0d`; `DESCRIPTION`: `License: GPL-3` | 🇺🇸 R tooling for building and testing education early-warning models on top of `caret`: ROC testing, model search, post-prediction adjustment. 71 files. 🟢 **Provenance is the value**: README names it the source behind modules of the **Wisconsin Dropout Early Warning System** (Wisconsin Dept of Public Instruction; author `Jared.Knowles@dpi.wi.gov`) | 🔴 **no.** Last commit **`2016-02-03`**, `DESCRIPTION` Date `2015-02-10`, version `0.9.2.9000`, Travis badges. 🟢 Read it as the **reference design** a state agency actually shipped — the model-search and ROC-testing structure is the reusable part, not the code |

🔴 **The licence boundary, stated because the two rows are not interchangeable.**
`student-signal` is MIT: a client's proprietary model, features and scoring thresholds stay
proprietary beside it. `EWStools` is **GPL-3.0 only** — no "or later" bound; the three *"any
later version"* strings in its payload are the How-to-Apply boilerplate, **not** a grant on
this package. An R deliverable that links it is a derivative work. 🟢 In practice this costs
nothing, because nobody should take a 2016 dependency: **port the method, not the package.**

🟡 **Two addresses the same leg returned and neither is on this shelf:**
`anwarulh007/eduprotect` **does not resolve** on either channel while `awesome.ecosyste.ms`
publishes an **MIT licence field** for it, and `ekoffi2/Machine-learning` resolves with **no
grant in a 2-file tree**. Recorded in
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) so no
later pass re-reads them.

🔴 **Mandated verticals leg: no new permissive education ERP/CRM, ELEVENTH consecutive pass.**
The whole result set was `openeducat.org`'s own glossary in seven languages. 🟢 One datum kept,
from the vendor's own page: **OpenEduCat is LGPLv3, not MIT or Apache** — the vendor itself
rules out the licence class the leg asks for. Both it and Odoo are already carried.

# Foundational repos — Education

> The layer below the agents: platforms, standards, assessment engines and learner-model
> libraries that an engagement builds *on* rather than *with*. Licences read first-hand from
> each repository's `LICENSE` payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds 13 payload-verified repositories, refutes two published permissive claims
> (forma.lms, Fedena) and **retracts this file's own LATAM gap**. Extended by
> [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv) — pass 267
> ranks this layer by **commits** instead of stars and by that measure finds the largest education
> codebase in open source (`instructure/canvas-lms`, **78,765 commits**) was missing from this file
> altogether, along with three permissive autograding/infrastructure rows and a **national education
> ministry publishing production services under MIT**. Extended again by
> [`verified-repos.2026-10-17-p268.tsv`](../evidence/verified-repos.2026-10-17-p268.tsv) — pass 268
> probes the rows this base **named but never read**, and that corrects the sentence above: the
> largest education codebase in open source is **`code-dot-org/code-dot-org`, 215,796 commits**,
> 2.7x Canvas. Pass 268 also shelves the **Ed-Fi** stack, which this base's own gap register has
> carried as the only permissive North American system of record for roughly 200 passes while
> *this* file carried no Ed-Fi row at all.

## 🟢 Pass 289 — THE FOUNDATION LAYER GAINS A **NATIONAL CURRICULUM AS A VALIDATABLE GRAPH**, and the grant under it is a restatement

⏱️ **Eleventh pass of `2026-10-18`.** Evidence:
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv) ·
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../evidence/curriculum-authority-egress.2026-10-18-p289.tsv) ·
[`p289-websearch.2026-10-18-p289.tsv`](../evidence/p289-websearch.2026-10-18-p289.tsv).

🔴 **Mandated vertical/ERP leg: no new permissive education row, TENTH pass running.** Apache
OFBiz (Apache-2.0), Huly (Apache-2.0), Krayin CRM (MIT), Aureus ERP (MIT), Atomic CRM (MIT),
iDempiere, Compiere, ERPNext (**GPL-3.0**, the only system in the leg naming Education among
its verticals), Dolibarr (GPL-3.0), Twenty (**AGPL-3.0 / BSL — source-available, not open
source**). 🔵 The leg's own summary states the finding: *"The results don't identify any MIT or
Apache project built for education."* **Ten passes. The education ERP/CRM gap is a gap in the
world, not in this base's searching** — administration is served by copyleft or by proprietary
SIS vendors, and a studio needing a permissive admin core **builds** it.

### 🟢 The new foundation row, and it is a layer this file did not have

| repo | grant (read from payload) | what it puts under an engagement |
|---|---|---|
| [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) | 🔵 **SPLIT** — **MIT** (`CODE-LICENSE.md`, 1 491 B, sha256₁₂ `427f1d8b0cc1`) for `scripts/` and workflows · **OGL v3.0** (`DATA-LICENSE.md`, 2 408 B, `c117e319f357`) for `ontology/`, `data/`, `docs/` | The **National Curriculum for England (2014)** as a formal graph: 31 classes, 75 properties, **38 SHACL shapes**, served as Turtle, JSON-LD, RDF/XML, N-Triples, SQLite and property-graph JSONL. 50 948 key learning points, 11 207 misconceptions, 7 432 prerequisites, 160 progression threads, 12 subjects |

🔵 **Why this belongs on the foundation shelf and not only on a trending one.** Every other
row in this file is a *platform* — something an engagement runs. This is a **curriculum
substrate**: an agent that claims a learning objective can be made to *validate* that claim
against 38 SHACL shapes instead of asserting it. 🔴 **This base has published
"curriculum-aligned" for ~200 passes with no alignment target in it.** This is the first row
that is one.

### 🔴 The grant beneath it is not the kind this file has been grading

`ACTION p289` separates two populations `p742` collapses:

- **`AUTHORITATIVE-BODY`** — the payload *is* the licence; the body travels with the clone.
  Every MIT/Apache/AGPL row on this shelf is one.
- **`RESTATEMENT`** — the payload *paraphrases* a licence authored by a third party, and names
  an off-repo host for the real text. **Both grade `GRANTED` under `p742`.**

The OGL half of this row is a `RESTATEMENT`, and 🔴 **the authority it names
(`nationalarchives.gov.uk`) is one of 12 licensing-authority hosts measured
`POLICY-REFUSED` from this environment — 2 independent egress paths, 12/12, zero reachable.**

🔵 **Stated plainly for a studio:** the structure, the ontology and the SHACL shapes are
**usable and commercially clear** — read first-hand from the payload:
*"exploit the information commercially and non-commercially … by including it in your own
product or application."* What is **not** closable from the payload is the exemption for
*"third party rights Oak National Academy is not authorised to license"* across 50 948 learning
points. **Build on the graph; clear the assets per engagement.**

🟡 **One obligation to get right, because the payload states it twice and differently.** OGL
prescribes `"Contains public sector information licensed under the Open Government Licence
v3.0."`; the same file's summary block asks for `"Oak National Academy"`. **Ship both.** The
cheaper reading is the one the file's own terms do not support.

## 🔴 Pass 288 — the foundation layer gained NOTHING this pass, and the reason is worth more than a filler row

⏱️ **Tenth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p288.tsv`](../evidence/verified-repos.2026-10-18-p288.tsv) ·
[`p288-websearch.2026-10-18-p288.tsv`](../evidence/p288-websearch.2026-10-18-p288.tsv).

🔴 **Mandated vertical/ERP leg: no new permissive education row, NINTH pass running.** The leg
returned a clean set of general-purpose systems and **not one education-specific one under a
permissive grant**:

| system | licence as the leg reported it | why it is not a foundation row here |
|---|---|---|
| Apache OFBiz | Apache-2.0 | ERP/CRM/HR automation suite. **No education vertical** — no student records, no admissions, no enrolment |
| Huly Platform | Apache-2.0 | Team/project platform, not an education system |
| Krayin CRM | MIT | CRM only |
| Aureus ERP | MIT | ERP with a plugin system; no education module |
| Atomic CRM | MIT | CRM only |
| ERPNext | **GPL-3.0** | 🟡 **The only system in the whole leg that names Education among its verticals** — and it is copyleft, so it cannot join the permissive tier |
| Dolibarr | GPL-3.0 | Copyleft; no education module |
| Twenty | AGPL-3.0 / BSL-1.1 | 🔴 **Source-available, NOT open source.** Recorded so a later pass does not read it as permissive |

🔵 **Stated plainly: the education ERP/CRM gap is not a gap in this base's searching — it is a
gap in the world.** Nine passes have run this leg. The answer each time is that education
administration is served either by copyleft (ERPNext, OpenEduCat, Dolibarr) or by proprietary
SIS vendors, and the permissive tier has no entrant. A studio needing a permissive admin core
builds it; it does not adopt one.

### 🔴 The Blackboard integration surface is real, and nothing on it is vendorable

The directed LMS-MCP leg added **Blackboard Learn** to the MCP-addressable set (see
[`agents/top.md`](../agents/top.md) for the full comparison against Moodle, Canvas, Google
Classroom and Open edX). As a *foundation* question the answer is negative and precise:

- 🔴 [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) — **no grant** in 9
  enumerated files, though its `readme.md` claims MIT. **An ASK, not a licence.**
- 🔴 [`yoyoconnor/BlackboardMCP`](https://github.com/yoyoconnor/BlackboardMCP) — **no grant**
  in 9 files; `pyproject.toml` carries no `license` key.
- 🟡 [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) — **already carried**;
  AGPL-3.0 per the Open edX project's own announcement, targets Ulmo, Tutor local and
  Kubernetes, and re-checks platform staff/superuser flags live on every request.

🟢 **What IS a foundation here is the API, not the server.** The Blackboard Learn **REST API**
is the stable surface; the community MCP servers in front of it are 9-file wrappers with no
grants. `P41` in [`compose/patterns.md`](../compose/patterns.md) wires that surface directly
and names what must be written fresh.

🔴 **No row is added to the tables below this pass.** Five real foundation repos were sought
and none was found that is both education-specific and permissively licensed. **Fewer real
rows beat padding**, and the searches that produced this nil are written down leg by leg in
[`p288-websearch`](../evidence/p288-websearch.2026-10-18-p288.tsv).

## 🟢 Pass 287 — a Bangla NLP toolchain is the foundation layer a Bengali engagement has had no answer for, and the mandated vertical leg again found nothing

⏱️ **Ninth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p287.tsv`](../evidence/verified-repos.2026-10-18-p287.tsv) ·
[`p287-websearch.2026-10-18-p287.tsv`](../evidence/p287-websearch.2026-10-18-p287.tsv).

🔴 **The mandated verticals leg produced no new permissive row, for the ninth time in ten
passes.** It returned `OpenEduCat` (Odoo-based, licence unstated by the source; this shelf
already carries it), **ERPNext GPL-3.0**, and **Twenty CRM under BSL-1.1** —
*source-available, not open source*, which is the `PageLM`/`Suna`/`OpenGaokao` pattern arriving
for the fourth time through a fourth channel. 🟢 **Said plainly: there is still no education
ERP or CRM under MIT or Apache that this base has been able to locate**, and nine passes of
the same query is now evidence about the supply, not about the search.

### 🟢 The genuinely new foundation row, and it came from a NIL

🔵 **The Bangladesh leg found no tutor and that is not what makes it useful.** It found that
**real Bangla open source exists and is INFRASTRUCTURE**:

| repository | what it is | why it is a FOUNDATION and not an agent |
|---|---|---|
| [`sagorbrur/bnlp`](https://github.com/sagorbrur/bnlp) | *"Natural language processing toolkit for Bengali Language"* — tokenisation, embeddings, NER, POS | 🟢 **The layer a Bengali-medium tutor is built ON.** No education repo on any shelf here can serve a 🇧🇩 learner in Bangla without something at this level |
| [`banglakit/awesome-bangla`](https://github.com/banglakit/awesome-bangla) | A collection of tools, datasets and resources for Bangla computing | 🔵 An **index of the layer**, which is how a studio finds the rest of it in week one |
| [`me-shaon/bangla-programming-resources`](https://github.com/me-shaon/bangla-programming-resources) | Bangla-language programming tutorials and references | Content, not code — relevant to a **teacher-training** scope rather than a learner-facing one |

🟡 **Licences NOT read first-hand this pass and therefore NOT published here as grants** — these
rows arrived from a search result, and this base's own two-pass record is that **three of four
secondary "open source" claims are wrong**. They are **leads at the right layer**, and probing
them is a `p288` item. Recording them as leads rather than as shelf rows is the whole point of
the distinction.

🟢 **What this pass DID establish about them, because it is cheap and it shortens `p288`'s
probe: all three RESOLVE, and their default refs are resolved rather than assumed.**

| lead | `ls-remote --symref` default ref |
|---|---|
| `sagorbrur/bnlp` | `main` |
| `banglakit/awesome-bangla` | `main` |
| `me-shaon/bangla-programming-resources` | 🔴 **`master`** |

🔴 **The third row is the reason this table exists rather than a sentence.** A `p288` probe that
hardcodes `main` would publish `NONE_IN_TREE` over it — which is the exact failure this pass saw
a third time in four passes (`AIProf` on `dev`, `eledia` on `master`, `twiga` on `development`).
**Resolve the ref; never assume it.**

🔵 **The general lesson, which is about where this base looks for foundations:** the language
legs keep returning **tutors that are proprietary** and **language infrastructure that is
open**. For every non-English market probed so far — 🇧🇩 Bangla, 🇻🇳 Vietnamese, 🇮🇩 Indonesian,
🇹🇿 Swahili — *the permissive code sits one layer BELOW the agent*, and an engagement that goes
looking for a tutor finds nothing while the thing it actually needs is sitting there unclaimed.

### 🔴 A correction to how this shelf has been reading `NONE_IN_TREE`

🔴 **`saif2012004/PrepifyAI` (389 files, no grant) shows that a code grant is not always the
binding constraint.** Its tree carries **20 `Extracted text books/` JSON files** for
`FBISE_CLASS9/10` and `PUNJAB_CLASS9/10`. 🔵 **This shelf's standing remedy for a
`NONE_IN_TREE` row is "ask the author for a written grant"** (`P17`, `P19`, and `p286` item 5's
licence-intake ask). 🔴 **That remedy would not clear this repository**: the author cannot grant
what they do not hold, and board textbook text is third-party copyright. 🟢 **So the remedy for
a `NONE_IN_TREE` row depends on WHAT IS IN THE TREE**, and this shelf has been treating the
verdict as though it had one remedy. Annotated, not rewritten. `T-p287c`.

🟢 **The same seam, documented from the supply side by `avps82/mentar`'s own
`docs/CONTENT_LICENSES.md`** — see [`repos/trending.md`](trending.md) and
[`compose/patterns.md`](../compose/patterns.md) `P40`. Two independent arrivals at the same
boundary in one pass: **the code grant and the content grant are different questions, and the
content one is the one that bites a PAID deliverable.**

## 🟢 Pass 286 — a national EXAM-RESULTS channel joins this shelf, and it is the layer an East African engagement has had no answer for

⏱️ `2026-10-18`, eighth pass. Evidence:
[`regional-intake.2026-10-18-p286.tsv`](../evidence/regional-intake.2026-10-18-p286.tsv).

🟢 **One row added, and it is a FOUNDATION rather than an agent** —
[`vincent-laizer/NECTA-API`](https://github.com/vincent-laizer/NECTA-API), **MIT**, root `LICENSE`
1 092 B, payload-read `2026-10-18`. A Python package that fetches results of Tanzania's national
examinations (**NECTA**). 🔵 **Why it belongs on this shelf and not on `agents/top.md`:** it carries
no model and no pedagogy — it is the **system-of-record channel** that a tutor, a dropout-prediction
model or a ministry dashboard reads underneath. This shelf's thinnest column has been *national
assessment data outside Europe and North America*, and this is the first row in it.

⚠️ **Two cautions, both from the author's own words:** it is **not an official NECTA API** (it reads
the published results service, so it breaks when that service changes) and it is **still in
development**. 🟢 The licence, however, is clean and permissive — which is the part a studio cannot
fix for itself.

🟢 **Also permissive, also new, and shelved as a platform rather than a foundation:**
[`Jahirrrr/sekolahyuk-app`](https://github.com/Jahirrrr/sekolahyuk-app) (🇮🇩, **MIT**, 1 064 B) — see
[`verticals/solutions.md`](../verticals/solutions.md).

🔴 **What this shelf did NOT gain, and the reason is a licence rather than an absence.** Seven
Indonesian and six Vietnamese addresses were probed. The one with the most platform-shaped scope,
[`sira313/rapkumer`](https://github.com/sira313/rapkumer) — a working alternative to Indonesia's
official **e-Rapor** report-card system, with an AI generator for learning objectives from **BSKAP**
outcomes — serves a **bespoke non-commercial licence** and therefore cannot be a foundation for
anything billable. 🔵 **Recorded here because the next pass must not re-discover it as a candidate:
the grant is the blocker, and it is a written policy of its author, not an omission.**

## 🟢 Pass 285 — the `Kuali` lead is RESOLVED AT PAYLOAD, and "open foundation, therefore permissive" is refuted on the limb that mattered

⏱️ `2026-10-18`, seventh pass. Evidence:
[`tree-enumeration.2026-10-18-p285.tsv`](../evidence/tree-enumeration.2026-10-18-p285.tsv).

🔵 `p284` registered **Kuali** as a lead and graded it honestly: *"HE **ERP/SIS/research admin** —
the thinnest column on the vertical shelf. Source **undated**, **no ref or payload read**, and
*'open foundation therefore permissive'* is the **parent-inference** grade this base ranks weakest."*
🟢 **Resolved this pass, one `ls-remote` and one payload read per repository** — and the
parent-inference was wrong in both directions at once:

| repository | resolves? | grant, read from payload `2026-10-18` | what it is |
|---|---|---|---|
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 yes | 🟢 **ECL-2.0** — `master/LICENSE.txt`, 11 182 B, *"Educational Community License, Version 2.0, April 2007"* | middleware. **Apache-derived, permissive** — the only permissive row in the family |
| [`kuali/kfs`](https://github.com/kuali/kfs) | 🟢 yes | 🔴 **AGPL-3.0** — `master/LICENSE`, 33 755 B, title window *"The GNU **Affero** General Public License … requires the operator of a network server to provide the source code"* | **Financials / ERP**. Network copyleft |
| [`kuali/kc`](https://github.com/kuali/kc) | 🟢 yes (HEAD `53fee5c1abef`) | 🔴 **no grant anywhere in the tree** — **20 627 files enumerated**, every licence-like hit is a Java class, an XML config or a help page (`NoticeOfOpportunity*.java`, `copyingadocument.htm`, `copyrightandlicensing.htm`) | Coeus — research administration |
| [`kuali/student`](https://github.com/kuali/student) | 🔴 **DOES NOT RESOLVE** | — | 🔴 **the SIS — i.e. the exact thing the thin column needed** |
| [`kuali/ole`](https://github.com/kuali/ole) | 🔴 **DOES NOT RESOLVE** | — | library system |

🔴 **So the answer to the lead is "no", and it is specific:** there is **no public Kuali SIS
repository**; the ERP is **AGPL-3.0**, not permissive; the research-admin codebase serves **no
grant at all** across twenty thousand files; and the one permissive grant in the family
(**ECL-2.0**) covers **middleware**, not an administrative system.
🟢 **This confirms, at payload grade, this base's own earlier conclusion that *Kuali's licence is
per REPO, not per ORGANISATION*** — which secondary sources (Wikipedia, EDUCAUSE, Maven Central,
linux.com) flatten into a single *"Kuali is licensed pursuant to the ECL, Version 2.0"*.

🔵 **The vertical shelf's thinnest column stays thin — but now for a MEASURED reason rather than an
unread lead.** The permissive HE-administration row this base has wanted for many passes is still
`Gego-K12/gegok12` (MIT, open-core), and Kuali does not join it.

**Pass 273 — no rows added, eighth consecutive nil, and the reason is now specific.** The scheduled
platform/SIS/ERP leg returned only systems already shelved here or on
[`verticals/solutions.md`](../verticals/solutions.md), and two listicles contradicted each other on
`forma.lms` (Apache-2.0 vs GPL) — a question this base settled at payload in `p265`. 🔵 **One nil is now
explained rather than repeated:** the battery's *"github trending education AI"* leg returns repositories
that **teach AI** (`generative-ai-for-beginners`, `nanochat`, `developer-roadmap`), not repositories that
**serve the education sector** — a query defect, not an absence of supply. ⚠️ **This file's layer was not
where pass 273's finding landed**; it landed on the agent shelf and on licence method — see `T41` and
[`repos/trending.md`](trending.md).

## 🟡 Pass 284 — no row added, and the one candidate the leg produced is NOT shelved, on purpose

⏱️ `2026-10-18`, sixth pass. Evidence: [`p284-websearch.2026-10-18-p284.tsv`](../evidence/p284-websearch.2026-10-18-p284.tsv).

🔴 **What was searched and what came back.** The leg
`open source platform education ERP CRM MIT Apache student information system` returned
**OpenEduCat** (LGPL-3.0, built on Odoo) — **already on this base's vertical shelf** — and
explicitly returned **nothing MIT- or Apache-licensed**. The result's own words: *"It did not return
anything on MIT- or Apache-licensed education platforms."*

🟡 **One candidate, named and deliberately NOT shelved: the `Kuali Foundation`.** A Linux.com article
describes it as *"the premiere open source educational administration project"*, producing **ERP, SIS
and research-administration systems** for higher education — a category this base's vertical shelf
has thin coverage of. 🔴 **Three reasons it stays off the shelf this pass:**

1. 🔴 **The source is undated**, and it names **Compiere** and **Openbravo** alongside it — projects
   whose heyday was over a decade ago. That dates the article, not Kuali, but it means the
   *currency* of the claim is unestablished.
2. 🔴 **No repository, no grant, no ref was read.** This base's standing rule is that a row carries a
   licence read **first-hand from the payload**. Nothing was read here.
3. 🔵 **Kuali's licence history is the specific reason not to guess:** the project is widely
   associated with a move toward a commercial entity, so an inference of *"it is an open foundation,
   therefore the code is permissive"* is exactly the **parent-inference grade** this base ranks
   weakest and has already been burned by (`kolibri-design-system`, `Athena`).

🟢 **Registered, not published.** Resolving it costs one `git ls-remote` plus one payload read and
would extend the thinnest part of the vertical shelf (**higher-education administration**). It is in
the backlog in [`../README.md`](../README.md) rather than in a table, because a row here is a
recommendation and this is a lead.

## 🔴 Pass 283 — the Artemis row on THIS shelf recommended one repository twice, and `p282`'s correction never reached it

⏱️ `2026-10-18`, fifth pass. Evidence: [`repo-identity.2026-10-18-p283.tsv`](../evidence/repo-identity.2026-10-18-p283.tsv) · [`ladder-case-audit.2026-10-18-p283.tsv`](../evidence/ladder-case-audit.2026-10-18-p283.tsv) · [`p283-websearch.2026-10-18-p283.tsv`](../evidence/p283-websearch.2026-10-18-p283.tsv).

🔴 `p282` established that `ls1intum/Iris` and `ls1intum/Pyris` are **one repository** (identical
HEAD `d7b2c095204e`, 245 refs, root tree `4e2f096df767`, 203 files, the same 1 088-byte MIT payload)
and corrected `agents/top.md`, `compose/patterns.md` and `verticals/solutions.md`.

🔴 **It did not correct this file.** The `ls1intum/Artemis` row went on naming *"**Iris** (LLM tutor,
`ls1intum/Iris`, MIT)"* and *"**Pyris** (the LLM microservice behind it, `ls1intum/Pyris`, MIT)"* as
**two distinct config-gated AI subsystems**, inside a single cell. A studio reading this row would
have scoped two integrations where one exists. 🟢 **Corrected above.**

🟢 **Found by `make gate-identity`, which `p283` built and wired, on its first run** — the whole
point of the gate, demonstrated on the pass that shipped it. 🔵 The count that matters for this
shelf: **138 live addresses across the three shelves, 138 distinct HEADs, 0 unreachable** — no other
row on any shelf recommends one repository twice.

🔵 **No new foundation this pass**, and the star column stays **frozen at `2026-10-17`** — `p282`'s
channel finding is re-confirmed and sharpened: `github.com` pages and `api.github.com` still answer
`403`, while the **git** channel answered **138 of 138**. Grants and identity are current; only
popularity is stale.

## 🔴 Pass 282 — no new foundation, and the star column on this shelf is FROZEN

🔴 The mandated vertical and trending legs returned **no foundational repository this base does not
already hold**. Every candidate they named — `Apache OFBiz` (Apache-2.0, a general business suite,
not education), `Huly` (Apache-2.0), `OpenEduCat` (**LGPL-3.0**, Odoo-based, 73+ modules),
`frappe/lms`, `LearnHouse` — returned `CARRIED` under `make carried`. 🔵 The leg's own words:
*"the search turned up few education-specific platforms under MIT or Apache."*

🔴 **And the channel that serves star counts is shut this pass:** `github.com/<slug>`,
`/topics/*`, `/trending` and `api.github.com` all answer **`403`**, while
`raw.githubusercontent.com` and `git ls-remote` answer normally. 🟢 **So every licence on this shelf
is still first-hand and current, and every star figure is carried from `2026-10-17` and was not
re-measured.** Evidence:
[`channel-reach.2026-10-18-p282.tsv`](../evidence/channel-reach.2026-10-18-p282.tsv).

🟢 `ls1intum/Artemis` was re-read at payload this pass — **MIT, `main/LICENSE`, 1 090 B, HEAD
`dc78a2bcba53`** — unchanged. 🔴 **Note for anyone composing from it:** `ls1intum/Iris` is **not** a
second repository to pair with `Pyris`; it is an alias of `Pyris`. See
[`agents/top.md`](../agents/top.md) pass 282.

## Permissive foundations (MIT / Apache-2.0 / BSD)

> 🆕 **Pass 274 adds the first row to this table in nine passes, and it is a row this base REFUSED
> twice.** See the `gegok12` retraction below and `T44`.

| Repo | Licence | Stars | Why it is a foundation |
|------|---------|-------|------------------------|
| 🆕 [Gego-K12/gegok12](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** *(`main/LICENSE`, `1 150` B, payload read + diffed, `p274`)* — ⚠️ **core only: 12 Pro modules sold separately** | 54★ / **98 forks** *(carried; no star read from GitHub this pass)* | **Self-hosted school ERP / SIS** on PHP 8.4 + Laravel. 🟢 **The permissive SIS layer this base has said for nine passes does not exist** — and the reason it was missing is that the base probed a slug that does not resolve, twice (`T44`). 🔵 **Its fork network is its adoption evidence**: 98 forks, near-zero fork stars, institution-shaped fork names across **India, Indonesia and Vietnam** (`P933` — software institutions RUN rather than developers EXTEND). ⚠️ **Deployment-placed APAC; origin not established.** ⚠️ **Price the Pro modules before the SOW** |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | **Interactive learning with automated feedback**, from TUM Applied Education Technologies. Programming, quiz, modelling and text exercises with automatic assessment and an integrated CI runner. The strongest MIT-licensed teaching platform found this pass — production-grade and university-maintained. **Pass 266:** it ships three *config-gated* AI subsystems — **Iris/Pyris** (the LLM tutor and the microservice behind it: 🔴 **`p283`: ONE repository, [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), MIT** — `ls1intum/Iris` is a name alias of it, not a second subsystem; `p282` established the identity and corrected `agents/top.md`, `compose/patterns.md` and `verticals/solutions.md`, and **this row was missed**. *Iris* is the user-facing name of the tutor Pyris powers) and **Athena** (feedback suggestion, [`ls1intum/Athena`](https://github.com/ls1intum/Athena), 🟢 **MIT at metadata grade since p275** — no licence *file* exists (tree enumerated, 691 paths) but **12 of 14 manifests declare `license = "MIT"`**; the earlier *"all-rights-reserved"* verdict is retracted), plus **Hyperion** (AI exercise authoring, not a separate repo). Config-gated matters: the platform runs identically with AI off, which is the posture an EU AI Act high-risk classification wants. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | 4.1k | FSRS, the modern spaced-repetition scheduler. The highest-adoption learning-science component in open source. Pair with [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) (BSD-3-Clause) for a Rust core you can embed. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 450 | The reference PyTorch knowledge-tracing benchmark library: standard datasets, standard splits, comparable baselines. If a client asks "can you predict what this student knows", this is the honest starting point. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT | 352 | Source-code plagiarism detection (UGent). In the GenAI era this is no longer a niche: it is the integrity layer every coding course now needs. |
| [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | Apache-2.0 | 313 | Education datasets plus download/preprocess tooling. Removes the first two weeks of any learner-modelling project. |
| [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT | 82 | Knowledge tracing **plus** cognitive diagnosis **plus** exercise recommendation in one library. Broader than pyKT where the deliverable is a recommender, not a predictor. |
| [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) | MIT | 78 | Unified library for student cognitive modelling, with a configuration-driven pipeline. Good for sweeping many models when the client wants a comparison, not a bet. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | Apache-2.0 | 215 | Maths and science e-assessment: randomised questions, algebraic marking, SCORM-packaged output. Apache-2.0 makes it embeddable in a commercial deliverable. **Pass 266:** 215★, 4,209 commits, 130 forks, **Newcastle University** School of Maths, Stats & Physics (README-quoted → EMEA-origin). Tests run **entirely in the browser** — a Python 3 compiler producing a JavaScript runtime — so no student submission need leave the device. That answers a data-residency objection structurally rather than contractually. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | — | Framework for building **LTI** tools that plug into any compliant LMS. The sanctioned way to put an AI tool inside Moodle/Canvas/Open edX without forking the LMS. |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | — | The xAPI (Experience API) specification itself. The vocabulary for "what did this learner actually do" across systems. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | — | SQL-backed **Learning Record Store** for xAPI. The missing piece between an agent that observes learning and a model that needs training data. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | — | Modern SCORM 1.2 / 2004 and AICC runtime. Most institutional content is still SCORM; this is how an agentic front end keeps reading it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | MOOC portal CMS (Django + React) from France Université Numérique. MIT means the client's catalogue front end is genuinely theirs. |
| [openfun/marsha](https://github.com/openfun/marsha) | MIT | — | Video management for education, same FUN-MOOC provenance. The companion to Richie when the course is video-first. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | MIT *(payload-measured **1,094 B**, `main/LICENSE`, pass 272)* | — | Student information system (Laravel): enrolment, attendance, results. MIT SIS data is the input every dropout-prediction model needs. |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | Apache-2.0 | — | HAX authoring/CMS for web-component-based course content. Content as components survives an LMS migration; content as LMS pages does not. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 *(README-stated — see note)* | — | The component API for Open edX. The entry point for putting an agent inside an Open edX course. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** | 46 | **The K-12 student-data standard of North American public education, and it is permissive.** *"Serves as the foundation for enabling interoperability among secure education data systems."* 370 commits on `v6.2.0`. The vocabulary a US district or state agency already models its students in — so an AI deliverable that speaks Ed-Fi needs no bespoke integration per district. ⚠️ **Neither this README nor `Ed-Fi-ODS`'s names a single US state or education agency** — see the provenance note below before any state count reaches a deck. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** *(payload at `LICENSE.txt`, not `LICENSE`)* | 28 | The Operational Data Store and ODS API — the running system behind the standard. 1,054 commits, and **48 forks against 28 stars**: forks exceeding stars is the deployment signature this file named on Submitty. The permissive **system of record** that the "North America publishes no education platform" framing said did not exist. |
| [Ed-Fi-Alliance-OSS/Data-Management-Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** | — | The ODS/API's declared successor. ⚠️ **Price this one from the register, not the README:** `intel/open-gaps.md` (`Gap 303`) establishes from `docs/PRD-v8.0.md` that it is *"a ground-up rewrite"* and that adoption is a **re-platforming with a data migration, not an in-place cutover**. `Gap 314` adds that provisioning is **create-only**, so any AI deliverable writing back to the system of record — a predicted risk flag, an AI-assisted grade — is a **data-model extension and a re-provision**, not an insert. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** *(payload at `LICENSE.txt`)* | — | End-user applications and extensions over the ODS/API. The deployment surface of the row above. |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 6.9k | Full online learning platform built for low-resource contexts: structured lessons, built-in formative feedback, learner-progress model. **17,004 commits** on `develop`. The highest-adoption *permissively licensed* complete learning platform located by this KB — larger than Artemis and larger than every education agent except DeepTutor. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1.4k | *"A system for assigning and grading notebooks."* **Autograding that already exists.** This file previously declared that no high-adoption open-source grading option was found; nbgrader is 1.4k stars, BSD-3-Clause and the default in university data-science teaching. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1.2k | *"the offline app for universal education"* — a complete learning platform that runs with **no internet connection**, syncing when a link appears. **39,803 commits.** MIT, which makes it the second permissive complete platform in this KB and the only one designed for intermittent connectivity. The natural base for rural LATAM and low-bandwidth APAC deployments. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | Apache-2.0 | 808 | *"Course management service that enables auto-graded programming assignments."* Initially developed by students at **Carnegie Mellon University** per its README. Apache-2.0 autograding with a course-management shell around it — the permissive counterpart to Artemis. |
| [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** | 41 ⚠️ | **India's national education stack — the APAC-origin platform this KB said did not exist.** The codebase under **DIKSHA**, run by NCERT/Ministry of Education. README: *"next-generation scalable open-source learning solution for teachers and tutors"*, mission *"improve learning outcomes for 200 million children across India"*. **38,046 commits, 317 forks — against 41 stars.** ⚠️ **Do not read the star count as adoption**: ministry-funded digital public infrastructure accrues commits, forks and deployments but almost no stars, which is precisely why star-sorted search never surfaced it. Backend: [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) (MIT). Mobile: [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). |
| [oppia/oppia-android](https://github.com/oppia/oppia-android) | Apache-2.0 | — | The Android client beside `oppia/oppia`. Pairs with `learningequality/kolibri` (MIT) wherever mobile-first, low-connectivity delivery is the actual constraint rather than an afterthought. |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | **BSD-3-Clause** | 802 | *"Homework Submission, Automated Grading, and TA grading system."* From the **Rensselaer Center for Open Source Software** in RPI's CS department (README-quoted → NA-origin). **9,316 commits, and 1.1k forks against 802 stars** — forks exceeding stars is the signature of software that gets *deployed*, not bookmarked. The most permissive licence in this base's assessment layer, and it covers submission, autograding *and* the TA grading workflow in one system. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD-3-Clause** | 161 | *"A Python and R autograding solution"* from the **UC Berkeley Data Science Education Program**. 3,825 commits. Grades scripts and notebooks, and ships **adapters for the Canvas and Gradescope autograders plus a student-side check client** — so it attaches to the LMS the client already runs instead of replacing it. R support matters: it is the one autograder here that covers statistics teaching. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** | **8.4k** | *"Multi-user server for Jupyter notebooks."* 8,913 commits, 2.1k forks. The substrate under notebook-based teaching and under both permissive notebook autograders (`nbgrader`, `otter-grader`). At 8.4k stars it is the **highest-adoption permissive row in this file** — this base had catalogued the graders without the thing they run on. |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | **Apache-2.0** | 286 | *"Enterprise open source portal built by and for the higher education community."* 17,158 commits, 278 forks. The campus portal / single-pane-of-glass layer: where an institution aggregates its systems, and therefore where an agent surface reaches the most students per integration. **Note the licence divergence inside Apereo:** uPortal is Apache-2.0, while its siblings `sakaiproject/sakai` and `apereo/opencast` are ECL-2.0 — so the educational-use patent scoping this base flagged on those two **does not apply here**. |
| [learningequality/studio](https://github.com/learningequality/studio) | **MIT** | 193 | *"Content curation tools for Kolibri"* — **Kolibri Studio**, the authoring and publishing half of the offline-first stack this file already shelves. 15,493 commits, 312 forks. Organises content into channels Kolibri can import, remixes existing channels against **national curricula**, and builds learning pathways and assessments. Without it, a Kolibri deployment is a reader with no pipeline. *Licence note: the MIT copyright line reads "(internal apps)", but the grant and condition clauses are unmodified standard MIT — reading that parenthetical as a restriction would be a false positive.* |
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** *(under Crown Copyright)* | 38 | **A national education ministry's production service, MIT-licensed.** *"A service for applying to teacher training courses"* — **34,414 commits**, run by the **UK Department for Education** at `apply-for-teacher-training.service.gov.uk`. The payload reads *"Copyright (c) Crown Copyright (Department for Education)"*. Beside it, [`DFE-Digital/teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) (MIT, *"Department for Education - Digital"*). ⚠️ **38 stars against 34,414 commits** — the same instrument blindness as Sunbird. ⚠️ **And the licence file is spelled `LICENCE`**: a probe trying only `LICENSE` reads this MIT service as unlicensed. |
| 🆕 [meyerjp3/psychometrics](https://github.com/meyerjp3/psychometrics) | 🟢 **Apache-2.0** *(`pom.xml` `<licenses>`, `distribution=repo`, read first-hand `p276`; **no payload in the tree** — 395 paths enumerated)* | 57 | **The permissive psychometrics layer this shelf had no answer for.** Java: IRT (Rasch/2PL/3PL/GPCM), CTT, factor analysis, finite mixture models, **IRT linking (Mean-Mean, Mean-Sigma, Stocking-Lord) and score equating**. 🔵 An adaptive-assessment engagement needs exactly this under the model layer, and `OATutor`'s BKT does not cover equating. ⚠️ Modules: `-core`, `-ctt`, `-factor`, `-fmm`, `-irt`. [evidence](../evidence/manifest-channel.2026-10-17-p276.tsv) |
| 🆕 [open-spaced-repetition/fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper) | 🟢 **MIT** *(`License` — mixed case, no extension — `1 079` B, payload read `p276`)* | 325 | **FSRS scheduling as a foundation, not a feature.** Retention-targeted interval computation, load balancing, postpone/advance, reschedule-all. 🔴 Carried as *"NO GRANT in 6 filenames"* until `p276` enumerated the tree. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |

**31 permissive foundation rows** (17 from pass 264, 4 in pass 265, 6 added and payload-verified in
pass 267, 4 Ed-Fi rows in pass 268). Pass 267's six were all found by **ranking candidates by commits
and probing named institutions and ministries by hand** — not one of them would surface in a
star-sorted topic listing. **Pass 268's four were not found by searching at all**: they were sitting
in this base's own gap register, Apache-2.0 and payload-read, while this file had no row for them.
🔵 **The cheapest source of new shelf rows this pass was the base itself.**

> **Note on XBlock:** the repository's `README.rst` states *"The code in this repository is
> licensed the Apache 2.0 license unless otherwise"* and points at `LICENSE.txt`, but that
> path did not serve a payload on the raw paths tried this pass. The licence is therefore
> **README-stated, not payload-read** — the weakest evidence grade in this file, and marked
> as such rather than quietly promoted.

## Copyleft foundations — real, but priced

> 🆕 **Pass 274 adds [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen) — `GPL-3.0` at payload
> (`35 149` B, reproduced from this base's own `p195` census) — AND FLAGS ITS OWN README.** The README
> carries a **`License: MIT` badge that links to that GPL-3.0 payload**. 🔴 **A studio reading the badge
> would carry GPL-3.0 code into a deliverable believing it was MIT**, and this is a *platform-grade*
> artefact, not a snippet: a **learner-owned two-role e-learning platform**, shipped to production as
> `2.0.0`, with an authoring orchestrator that builds a private course from a one-sentence goal, a
> **course-scoped RAG tutor with lesson citations and a visible tool-call trace**, BYOK across four
> providers with envelope-encrypted keys, and **an MCP server registered in the official MCP registry**
> as `io.github.ahmedEid1/lumen`. 🔵 **The badge/payload split is `T9`'s species at its most expensive
> location — the project's front door** — and it is the inverse of `T9`'s `Open-TutorAi` case, where an
> alarming phrase turned out to be harmless boilerplate. **Here a reassuring badge is the error.**
> 🟢 **Usable across an HTTP boundary like any GPL-3.0 platform on this shelf** (GPL-3.0 has **no**
> network clause, unlike the AGPL rows); **not usable as a code base for a proprietary deliverable.**
> ⚠️ **Ask upstream which one is intended before anything else** — one of the two is a mistake, and
> `T27` says a grant nobody chose deliberately is the one most likely to move.


| Repo | Licence | Why you still care |
|------|---------|--------------------|
| [datawhalechina/ai-edu-for-kids](https://github.com/datawhalechina/ai-edu-for-kids) | **CC-BY-NC-SA-4.0 — README prose only, NO payload** *(new in pass 269)* | *"面向中小学的人工智能通识课开源课程"* — an open-source **AI general-education course for primary and secondary schools**, 128★ / 27 forks / 57 commits. 🔴 **It is the most-adopted primary-band AI-curriculum artefact this base has located, and it is the one licence form a studio cannot use: NonCommercial *and* ShareAlike.** No `LICENSE` file resolves on 19 paths; the claim lives in the README body. 🔵 **Why you still care: as a CURRICULUM SPECIFICATION it is free to read.** Pattern `P17` already exists for exactly this case — originate the content yourself on a free engine, using sources like this one to establish *what* a Class-3–8 course must cover rather than shipping its text. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | **The largest education codebase this KB has located — 78,765 commits — and it was missing from this file entirely.** *"The open LMS by Instructure, Inc."* 6.9k stars, 3.0k forks. Canvas is the dominant LMS in North American higher education **and it is open source**, which makes "North America is a proprietary-LMS market" a briefing error this file could have produced. AGPL-3.0: the network clause reaches a hosted deployment, so the integration boundary (LTI, the Canvas API, or `canvas-mcp` under MIT) is where the engagement lives — not a fork. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(in `COPYING.txt`, not `LICENSE`)* | The world's most deployed LMS and the largest plugin ecosystem in education. GPL is survivable because the integration point is a plugin boundary. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | MOOC-grade platform behind edX. **This base previously published Apache-2.0 for this repo — that was wrong, and the error mattered**: AGPL's network clause is exactly the kind of obligation a hosted-deployment engagement must price in from day one. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 *(prior cell said GPL-2.0)* | Lightweight LMS with deep LATAM public-sector deployment. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | The institutional LMS of the German-speaking EMEA market. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | School management / SIS. Attendance and behaviour data — the signal dropout models actually run on. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | K-12 student information system, light footprint, widely self-hosted. |
| [Vacademy-io/vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Modern e-learning platform with assessment management. AGPL network clause applies. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 *(re-read at its true default branch **`2.12`**, not `master` — `p281`)* | **Brazilian school-management system, and the LATAM-origin foundation this file previously said did not exist.** Originally built by the *prefeitura de Itajaí (SC)* and published on the Brazilian federal **Portal do Software Público in 2008** for Secretarias de Educação nationwide. 719 stars, **34,948 commits**, last commit **2026-10-14**. Laravel/PHP. Government provenance is exactly what Brazil's digital-sovereignty guidance asks for. |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | AGPL-3.0 | The teacher-facing portal for i-Educar (*portal do professor*), last commit **2026-10-09**. **Note for legal review: the licence payload in this repo is a Portuguese translation of the AGPL-3.0 text, not the FSF's English original.** FSF translations are unofficial; cite the English AGPL-3.0 in any SOW. AGPL's network clause applies to a hosted deployment. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 | Lecture capture and academic video management, university-consortium maintained. ECL-2.0 is Apache-derived and OSI-approved but scopes its patent grant to educational use — the same distinction this KB flagged on Sakai. |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 | Autograding platform from UCLouvain. The EMEA counterpart to Autolab, at an AGPL price. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0** | Interactive content types (the H5P authoring ecosystem embedded in Moodle, Canvas and Drupal). **H5P is widely cited — including in earlier Globant KB cycles — as MIT. The PHP library's payload is GPL-3.0.** Content authored *with* H5P is yours; the library you ship is not permissive. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Web conferencing built for teaching (breakouts, whiteboard, LMS integrations). LGPL means linking is survivable; modification is not free. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 | School ERP on the Frappe stack: admissions, fees, assessment. The Frappe/ERPNext alternative to OpenEduCat's Odoo lineage. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | Frappe Learning. AGPL network clause; pairs with `frappe/education` when the client is already on ERPNext. |
| [OpenBoard-org/OpenBoard](https://github.com/OpenBoard-org/OpenBoard) | GPL-3.0 | Interactive-whiteboard software (Geneva-origin) with pt-BR localisation. Classroom-front-end, not server-side; GPL is rarely a problem for a desktop deployment. |
| [oat-sa/package-tao](https://github.com/oat-sa/package-tao) | **GPL-2.0** | **TAO** — an open-source e-testing platform for authoring and delivering assessments, *"created by the University of Luxembourg"* and maintained by **Open Assessment Technologies** (README-quoted → EMEA-origin). Core framework: [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core), same GPL-2.0 payload. The permissive-assessment shelf (Artemis, Numbas, Submitty, otter-grader) does **not** include it — TAO is copyleft, and at GPL-2.0 it is not even AGPL-compatible. ⚠️ **Secondary sources routinely tie TAO to large-scale international assessment programmes; its README makes no such claim and this KB asserts none.** Verify any programme reference with OAT before it reaches a client deck. |
| [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) | **AGPL-3.0** | The server half of the **German school-cloud** stack — *"Schulcloud-Verbund-Software-Server"*, **16,192 commits**, 81 stars. Front end: [`hpi-schul-cloud/nuxt-client`](https://github.com/hpi-schul-cloud/nuxt-client) (AGPL-3.0). The nearest thing this base has to a *European public-sector school platform*, and a working reference for data-protection-first school IT. ⚠️ **Provenance is org-handle grade only:** the handle is `hpi-schul-cloud` and the README links `dbildungscloud.dev` docs, but **the README names no ministry, no funder and no Land.** Do not brief it as a federally-funded programme on this evidence. ⚠️ The GitHub sidebar shows a License link **with no label** — the payload is the only licence evidence that exists here. |
| [Tangerine-Community/Tangerine](https://github.com/Tangerine-Community/Tangerine) | **GPL-3.0** | *"Open-source software platform designed to support data collection in low-resource settings, especially in education."* **8,064 commits.** Offline-first assessment on tablets and phones that syncs when connectivity appears, built originally for early-grade reading and maths. The **assessment** counterpart to Kolibri's offline *delivery* — together they cover the low-connectivity lane end to end, at a GPL-3.0 price on this half. The logo is a registered trademark of **RTI International** (the only institutional statement the README serves). ⚠️ README claim, not independently verified: *"more than 5 million assessments and surveys across 65 countries and more than 80 organisations"* — **no country list is served**, so no specific national deployment is asserted. |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | **SPLIT LICENCE — read the payload, not the label** · *holder 🟢 `FILLED` (`p281`): `2021-present PrairieLearn, Inc.` jointly with `2013-2021 University of Illinois Board of Trustees`* | *"Online problem-driven learning system"*, 12,061 commits, 519 stars, 404 forks, UIUC in the copyright line. **This row exists as a warning as much as a recommendation.** The GitHub sidebar shows a License link *with no label*, and the payload partitions the tree four ways: the **Community Edition** (everything outside `apps/prairielearn/src/ee/`) is **AGPL-3.0**; `apps/prairielearn/src/ee/` is the **Enterprise Edition under its own separate licence**; **all client-side JavaScript**, served or compiled, is **AGPL-3.0**; and portions copyright UIUC and outside contributors are **MIT**. Any single-label cell — "AGPL-3.0" included — is wrong in two directions at once. |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | **MIT, with exceptions — one of them commercial** | The Runestone interactive-textbook platform. The grant is MIT, but the payload's **first paragraph** excepts, among others, the **Handsontable component, which is commercial software**: *"if you make a copy of this software, you must contact https://handsontable.com/ to verify your compliance with their license."* Two textbook texts also carry their own terms (GNU Documentation License; a publisher's copyright). **An MIT headline over a paid dependency** — exactly the shape that passes a licence audit and fails a procurement review. |
| [code-dot-org/code-dot-org](https://github.com/code-dot-org/code-dot-org) | **Apache-2.0 OVER A PROPRIETARY CURRICULUM — read the payload, not the label** | **The largest education codebase in open source, and pass 267's "largest" cell was wrong.** *"The code powering code.org and studio.code.org"* — **215,796 commits** (read twice, independently), 901★, 538 forks, last commit **2026-10-17** (merge 7995a55, PR #76166). That is **2.7x `instructure/canvas-lms`'s 78,765**. The GitHub sidebar shows a License link **with no label** — `p267`'s signal, and it fired correctly. The payload grants **Apache-2.0** over *"all source codes and assets"* **with one exception that swallows the deliverable**: Code.org's *"proprietary or licensed artwork, graphics, sounds, lectures, videos, logos, characters, fonts"* *"may not be used or distributed or accessed in any manner other than directly via Code.org's own web site, mobile applications, or social media channels ... **without modification or embedding in another format**."* And the `NOTICE` says why Code.org could not grant them even if it wanted to: the curriculum is built on **licensed entertainment IP** — Minecraft (Microsoft), Star Wars (Disney/Lucasfilm), Frozen (Disney), Ice Age (20th Century Fox), Angry Birds (Rovio), Plants vs. Zombies (PopCap), The Amazing World of Gumball (Cartoon Network), The Bad Guys (DreamWorks) — plus **Font Awesome Pro** and the Geist font (SIL OFL). 🔵 **So the engine is permissive and the lessons are not.** See `Gap 367` below: this row is the answer to it, and the answer is not the one that was being searched for. |
| [pressbooks/pressbooks](https://github.com/pressbooks/pressbooks) | **GPL-3.0** | Open-textbook authoring and publishing (WordPress-based). Shelved with a companion measurement: [`openstax/os-webview`](https://github.com/openstax/os-webview), the front end of the **OpenStax** open-textbook programme, declares **AGPL-3.0** in `package.json` (metadata grade — it serves no licence file). **The open-textbook layer is copyleft on both rows measured this pass**, which is worth knowing before an OER engagement is scoped as permissive. |

## What to reach for, by job

- **"Put an AI tutor inside our existing LMS"** → `tsugi` (LTI) or `openedx/XBlock`. Do not fork the LMS.
- **"Automatically assess student work"** → `Artemis` for programming and modelling, `Numbas` for maths.
- **"Tell us which students are at risk"** → `academico` or `GibbonEdu` for the data, `pykt-toolkit` or `pyedmine` for the model, `lrsql` + `xAPI-Spec` for the event stream.
- **"Make retention stick"** → `fsrs4anki` / `fsrs-rs`. Spaced repetition is the one intervention with a scheduler worth reusing instead of inventing.
- **"We must prove academic integrity"** → `dolos`.
- **"Our content is all SCORM"** → `scorm-again`, and keep the content where it is.
- **"Grade programming work automatically"** → `Submitty/Submitty` (BSD-3) where submission, autograding *and* TA grading must all be covered, `autolab/Autolab` (Apache-2.0) for a course-management shell with autograding, `jupyter/nbgrader` (BSD-3) or `ucbds-infra/otter-grader` (BSD-3, also R) where the work is notebooks, `Artemis` (MIT) where feedback matters more than marks. **Five permissive options, none of them an agent** — this is a solved, copyleft-free problem.
- **"The client runs Canvas"** → do **not** start from `instructure/canvas-lms` (AGPL-3.0, 78,765 commits). Reach it through its API — `vishalsachdev/canvas-mcp` (MIT) for an agent surface, LTI via `tsugi` for a tool — and keep your deliverable outside the AGPL boundary.
- **"Notebook-based data-science teaching"** → `jupyterhub/jupyterhub` (BSD-3) for the substrate, then `nbgrader` or `otter-grader` on top. All BSD-3: the whole lane is permissive end to end.
- **"We are a ministry or a public agency"** → the precedent is real and MIT: `Sunbird-Ed/SunbirdEd-portal` (India, 38,046 commits) and `DFE-Digital/apply-for-teacher-training` (UK, 34,414 commits). Public-sector education code is **shelf-grade**, and star counts hide all of it.
- **"Our learners lose connectivity"** → `learningequality/kolibri` (MIT). Offline-first is an architecture, not a setting, and retrofitting it onto a server-rendered LMS is a rebuild.
- **"We are a US district or state education agency"** → the **Ed-Fi** stack (Apache-2.0):
  `Ed-Fi-Data-Standard` for the model, `Ed-Fi-ODS` for the running system of record,
  `Data-Management-Service` for new builds. This is the permissive North American public-sector
  layer, and it is a **data standard and API** rather than a platform — which is the correct shape
  for this market, where the LMS is already bought. ⚠️ Price DMS adoption as a **re-platforming
  with a data migration** (`Gap 303`) and any write-back as a **model extension and re-provision**
  (`Gap 314`).
- **"Deliver a K-5 or K-12 AI/CS literacy mandate"** → reach for `code-dot-org/code-dot-org`'s
  **platform** under Apache-2.0, and **plan to originate or commission the lessons**. Do **not**
  plan to reuse Code.org's videos, characters, artwork or Minecraft/Star Wars activities: the
  payload forbids it and the `NOTICE` explains that Code.org cannot grant them either. The content
  is the deliverable; the engine is the freebie. See `Gap 367`.
- **"Brazilian municipal or state network, sovereignty-first"** → `portabilis/i-educar` (GPL-2.0) for the SIS and `i-diario` (AGPL-3.0) for the teacher portal, both actively maintained in October 2026, both already inside the federal software-public lineage. Keep studio code on the permissive side of an LTI or API boundary.

## Declared gaps — and three retractions

### Retracted: "no LATAM-maintained foundational repo identified"

**This was wrong, and it was wrong in the direction that costs the studio most.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) is a Brazilian school-management
system with **34,948 commits**, a commit from **2026-10-14**, origin in the *prefeitura de
Itajaí (SC)*, and publication on the **Portal do Software Público** of the Brazilian federal
government in 2008. Its teacher portal `i-diario` committed on **2026-10-09**. The region does
publish this layer; this KB had not looked in Portuguese.

The accurate, narrower claim: **no LATAM-origin *permissively licensed* foundation and no
LATAM-origin *agent* has been identified.** i-Educar is GPL-2.0 and i-Diário is AGPL-3.0 — the
LATAM supply exists and arrives copylefted, which is a pricing question, not an absence.

### Retracted: "no high-adoption open-source grading option"

`jupyter/nbgrader` (BSD-3-Clause, 1.4k) and `autolab/Autolab` (Apache-2.0, 808, CMU-origin)
are both higher-adoption than every education *agent* in this KB except DeepTutor. What does
not exist is a grading **agent**; autograding **platforms** are permissive, mature and
boring — which is the correct thing to put in front of a regulator.

### Retracted in pass 266: "no APAC-origin education platform"

Pass 265 narrowed its APAC conclusion to this one remaining gap and briefed integration work
on the strength of it. **[`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
is MIT, 38,046 commits, 317 forks, and is the stack beneath DIKSHA** — India's national school
education platform under NCERT. APAC publishes the platform layer, at national scale, under the
most permissive licence this KB tracks.

**Why it hid for 265 passes, stated as a method defect rather than bad luck:** every leg this
base runs sorts GitHub topic listings **by stars**, and `SunbirdEd-portal` has **41**.
Ministry-funded digital public infrastructure is used by system integrators and education
departments, not by developers who star repositories. The instrument cannot see this class of
code at all.

| | Sunbird | A star-findable agent |
|---|---|---|
| Stars | **41** | 300 – 41,500 |
| Commits | **38,046** | 21 – 12,437 |
| Forks | **317** | 1 – 395 |

**Standing instruction for later passes:** rank the *platform* layer by **commits and forks**,
and probe national-programme names by hand (DIKSHA/Sunbird, i-Educar, Kolibri, Me Capacito,
Ceibal). Also note the slug trap: `Sunbird-Ed/sunbird-ed-portal` does **not** resolve — the
live slugs are camel-case, and a kebab-case guess returns nothing that looks any different
from absence.

### Still open

- **Permissive complete platforms are at least three deep, not one** *(superseded in pass 266 — see the corrected count below)*. **OpenOLAT** (Apache-2.0),
  **Kolibri** (MIT) and **Oppia** (Apache-2.0) are now all payload-verified; see
  [`verticals/solutions.md`](../verticals/solutions.md) for how they differ in scope. The
  previous "exactly one candidate" framing understated the shelf and should not be repeated in
  a pitch. Everything else at full-LMS scale is still GPL or AGPL.
- **Star counts marked `—`** were not re-verified this pass; the licence was. An unverified
  number is left blank rather than carried forward from a prior pass, because carried-forward
  numbers are how this base previously published "pykt 1.2k" for a 450-star repository.
- **~~No LATAM-maintained foundational repo identified.~~ — struck in pass 266 as an
  internal contradiction.** This bullet survived in "Still open" while the *top of this same
  section* retracted exactly that claim on the evidence of `portabilis/i-educar` (34,948
  commits, commit 2026-10-14). Both statements were published in the same file on the same
  day. The accurate version: **LATAM publishes this layer and it arrives copylefted** —
  i-Educar is GPL-2.0, i-Diário AGPL-3.0. What is still missing is a LATAM-origin
  **permissively licensed** foundation. Chamilo, often cited for its deep LATAM public-sector
  footprint, is European-maintained (Belgium/Spain) and GPL-3.0.
- **Cross-shelf consistency is now a required check.** Two contradictions were found *inside
  this base* in pass 266 — this bullet, and `agents/top.md` declaring the grading category
  empty while line 21 of this file carried an MIT automated-feedback platform. Both were
  falsifiable with one `grep`, not more searching. **Before republishing any declared gap,
  grep the other shelves for its own counter-evidence.**
- **Permissive platform count, corrected again:** with **Sunbird** (MIT) and **Artemis** (MIT)
  the permissive complete-platform shelf is **five** deep — OpenOLAT, Kolibri, Oppia, Sunbird,
  Artemis — not three and certainly not one. Each prior count was published as if final.

### Added in pass 267

- **The commit-ranked view is not a refinement of the star-ranked one — it returns different
  software.** Ranking candidates by commits and probing named institutions by hand produced
  `instructure/canvas-lms` (**78,765 commits**, 6.9k★), `DFE-Digital/apply-for-teacher-training`
  (**34,414 commits**, 38★), `uPortal` (17,158, 286★), `hpi-schul-cloud/schulcloud-server`
  (16,192, 81★), `learningequality/studio` (15,493, 193★), `Submitty` (9,316, 802★),
  `jupyterhub` (8,913, **8.4k★**) and `Tangerine` (8,064, 70★). **Stars and commits agree on one
  of those eight.** This is the same instrument defect pass 266 found with Sunbird, now measured
  across a batch instead of a single row.
- **A licence LABEL cannot carry the SHAPE of a grant, and two rows this pass prove it.**
  `PrairieLearn` is AGPL-3.0 *plus* an Enterprise-Edition directory under separate terms *plus*
  MIT-licensed portions *plus* AGPL client-side JS; `RunestoneInteractive/rs` is MIT *over a
  commercial Handsontable dependency*. Both would be mis-shelved by any single-label field —
  including this file's own `Licence` column, which is why both carry their shape in prose
  instead of a name. **Add to the method note: when the GitHub sidebar shows a License link with
  no label, that is a signal to read the payload in full, not a missing datum.**
- **`LICENCE` — the British spelling — must be in every probe's path set.** `DFE-Digital/apply-for-teacher-training`
  serves MIT at `main/LICENCE` and **nothing** at `main/LICENSE`. Any prior pass that probed this
  class of repository would have published "unlicensed" for a live, MIT-licensed government
  service. Pass 267's path set is 19 paths x 4 refs, including `.md`/`.txt` variants, lowercase,
  `COPYING`, `docs/`, `.github/`, `NOTICE` and package metadata.
- **Four of this base's five "no licence payload" rows survived that wider probe** — `ls1intum/Athena`,
  `autograder-org/autoGrader-frontend`, `os4ed/openSIS-Classic` and
  `GeminiLight/awesome-ai-llm4education` serve nothing on any of the 76 combinations. **The earlier
  calls were right, and that is worth recording as plainly as a correction would be.** The fifth,
  `learningequality/kolibri-design-system`, resolves to **MIT at metadata grade** (`package.json`).
- **Still open, and now with the instrument named:** no LATAM-origin *permissively licensed*
  foundation. Pass 267 probed the most-cited LATAM national programme directly — **Uruguay's Plan
  Ceibal — and its GitHub organisation exists with ZERO public repositories** and no public
  members. Ceibal's platforms are not open code; a Ceibal-adjacent engagement is **integration,
  not adoption**. Brazil remains the only LATAM country in this file with published education
  source, and it arrives copylefted.
- **`OpenEMIS` is not shelved, and the reason is specific:** the EMIS most associated with
  ministry deployment serves, on the repo this KB can reach, a **32-commit Docker packaging
  project with no licence on any of 76 path/ref combinations and no ministry or country named in
  it.** The application source was not located. An unshelved row with a stated reason is worth
  more than a plausible one.

### Added in pass 268

- **🔴 Correction to pass 267's headline: the largest education codebase in open source is
  `code-dot-org/code-dot-org`, at 215,796 commits — not `instructure/canvas-lms` at 78,765.**
  Pass 267 published "the largest education codebase this KB has located" on a commit-ranked
  sweep; Code.org is **2.7x** larger and was not in the candidate set, because the sweep ranked
  *repositories this base had already named* and Code.org had only ever been named as a
  **curriculum vendor** in a gap note, never as a repository. 🔵 **The generalisable defect is the
  same one pass 267 found on Canvas and did not finish fixing:** this base reliably mistakes
  *"organisation known for a product"* for *"organisation with no source."* Canvas was in "not on
  the shelf" as commercial SaaS; Code.org was in a gap note as a curriculum provider. **Both
  publish at enormous scale.** The commit figure was read twice independently (repository page and
  `tree/staging`), both times 215,796, precisely because this base has a history of publishing
  numbers it read once.
- **🟢 The Ed-Fi stack is shelved, and the reason it was missing is the most uncomfortable finding
  of the pass: it was never missing from the *base*, only from the *shelves*.**
  `intel/open-gaps.md` carries Ed-Fi across at least six numbered gaps (`286`, `303`, `309`,
  `311`, `314`, and `ACTION TM`/`TR`), records all five repositories as **Apache-2.0,
  payload-read, placed North America**, and states plainly that **Ed-Fi DMS is the only permissive
  system of record this base has found.** Meanwhile *this* file had no Ed-Fi row, and
  [`verticals/solutions.md`](../verticals/solutions.md) published, in pass 267, that public-sector
  platforms exist for three regions *"and still none for North America."*
  🔵 **This is the third cross-shelf contradiction in three passes** (pass 266 found two: the LATAM
  gap bullet and the grading-category claim). The pass-266 standing instruction — *"before
  republishing any declared gap, grep the other shelves for its own counter-evidence"* — was
  followed against the four `.md` shelves and **still missed this**, because the counter-evidence
  lives in the **gap register**, which is not a shelf. **Amended standing instruction: grep
  `intel/open-gaps.md` too, and grep for the SLUG as well as the prose claim.** Pass 268 found
  Code.org by grepping for `code-dot-org` and getting **zero hits across every `.md` in this
  repository** while `Code.org` the phrase hit four files.
- **🟡 Ed-Fi's agency provenance is NOT established, and the state count must not be briefed.**
  Neither Ed-Fi README names a US state or an education agency; the Alliance's own pages give no
  number. A third-party directory lists 14 statewide adoptions (AZ, NM, TX, TN, GA, SC, KS, NE, IN,
  MI, WI, MN, VT, DE) and search reports South Carolina's own department page naming ODS/API 7.3
  for SY2025-26 plus a Texas Education Exchange deployment — but **`ed.sc.gov` and
  `www.ed.sc.gov` both returned `getaddrinfo ENOTFOUND` from this environment, so none of it was
  read first-hand.** Shelved on the **licence**, which is payload-grade; the **adoption** is
  search-summary grade and labelled as such. This is the `OpenEMIS` discipline applied to a row
  that *passes*: the licence earns the shelf, the provenance does not earn a claim.
- **🟢 2026 roadmap detail worth a sentence in a proposal** (search-summary grade, Ed-Fi's own
  docs blog): native **OneRoster 1.2** support shipped in **ODS/API 7.3.2**, the platform moved to
  **.NET 10** ahead of .NET 8 end-of-support in **November 2026**, and Ed-Fi API v8 and Admin API
  v2.4 are on the 2026 release line. 🔵 The OneRoster item matters because `Gap 309` records
  OneRoster as *absent* from DMS v8.0 — so the rostering story differs between the ODS/API line
  and its successor, and a proposal must say which line it is quoting.
- **🔵 The permissive complete-platform count is still five.** `classroomio/classroomio` was
  recommended to this pass by a 2026-dated source as the open alternative to Moodle and edX; its
  payload is **AGPL-3.0**, consistent with what the register already carried (AGPL core, MIT `mcp`
  package, plus a `LICENSE_KEY` gate on self-hosted enterprise features). Ed-Fi and Code.org are
  **not** platforms — one is a data standard, the other a curriculum delivery system with an
  unlicensable content layer — so neither raises the count. **Three consecutive passes have now
  added permissive rows without adding a permissive platform.**

### Added in pass 269

- **🟢 Gap 367's Chinese limb — the limb pass 268 itself named as the cheapest way to falsify its
  own biggest claim — was run, and the closure HELD.** Pass 268 closed `Gap 367` (*"primary-school
  AI literacy has no permissive curriculum"*, carried ~175 passes) as **correctly empty**, on the
  licences of three **Western** sources: Code.org (Apache-2.0 over a proprietary-materials
  carve-out), MIT Day of AI (CC), `touretzkyds/ai4k12` (no payload). It then wrote down, honestly,
  that it had **not** run the gap's own costed next step — *"probe CBSE/MoE-aligned repos in Hindi
  and Chinese"* — and that a permissive Hindi or Chinese primary curriculum would reopen the gap.
  **Pass 269 ran both legs. Neither reopens it, and each fails for a different reason.**
- **🔴 The Chinese leg found the row this base had never seen, and p268's amended rule is exactly
  why.** [`datawhalechina/ai-edu-for-kids`](https://github.com/datawhalechina/ai-edu-for-kids) is
  now on the table above. 🔵 **The mechanism matters more than the row:** the *organisation*
  `datawhalechina` already appears on two shelves here — so a prose or org-level check would have
  reported this as covered — while the **slug** `ai-edu-for-kids` returns **zero hits in every file
  of this base.** That is `p268`'s `code-dot-org` finding (*"grep the SLUG as well as the prose
  claim"*) firing one pass later, in a second language, on a different organisation. **The rule is
  not a one-off patch; it is load-bearing.**
- **🔴 And the licence is a TEMPLATE DEFAULT, which is a new failure mode on this base's list.**
  `ai-edu-for-kids` carries CC-BY-NC-SA-4.0 under a `## LICENSE` heading followed by this, verbatim:
  *"注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议"* — **"note: CC 4.0 is used by default,
  you may choose another licence depending on your project."** 🔵 The most restrictive attribute of
  the most on-point curriculum artefact in this category is therefore **boilerplate carried over
  from an organisation's project template, not a decision anyone made about this course.** `T20`
  catalogues licence risk by the *shape* of a grant; this is risk from a grant's *provenance*.
  Practically: it is the kind of licence that an upstream maintainer may well change if asked, and
  the kind a studio must never assume.
- **🟢 The Hindi leg found supply — ONE BAND TOO HIGH, which restates the gap more precisely than
  it has ever been stated here.** India has the hardest deadline in this KB (AI and computational
  thinking **compulsory from Class 3**, CBSE **Circular Acad-15/2026**, implementation from the
  2026–27 session, with IIT Madras, IIT Gandhinagar and Azim Premji University named as
  contributors and NCERT approving the framework — ⚠️ search-summary grade; the circular itself was
  not read, per `p268`'s DNS finding). The permissive Indian supply this base carries —
  [`Naitik-xd/CurriculumCraft-AI`](https://github.com/Naitik-xd/CurriculumCraft-AI), **MIT at
  payload** — targets **grades 9–12**. 🔵 **So the correct form of `Gap 367` is not "no permissive
  AI curriculum" and not "a search-language artefact": it is BAND-SPECIFIC. Permissive
  curriculum-generation supply exists for the senior secondary band and not for the primary band,
  in the one country where the primary band is legally mandated.** That is a sentence a studio can
  take to a ministry.
- **🟢 Three carried APAC rows were re-measured BLIND and reproduced exactly — recorded as
  prominently as a correction would be.** `CurriculumCraft-AI` (MIT at `main/LICENSE`, 1,091 B,
  0★, 7 commits), `arjav0703/cbse-ai` (AGPL-3.0, **34,523 B — agreeing to the byte** with
  `evidence/p244-withheld.2026-10-16-p244.tsv`, and still archived), and
  `crpf-mitadt/Indian-AI-for-Education` (CC0-1.0, 7,048 B). 🔵 **`p268` warned that rewriting a
  good figure on noise is as bad as publishing a bad one. Three independent agreements, including
  one to the byte, say this base's APAC licence cells are sound.**

## Pass 280 — the bound on "no grant here" was the example's own size, and lifting it corrected the biggest count on this shelf

🔵 **Evidence:** [`channel-conflict.2026-10-18-p280.tsv`](../evidence/channel-conflict.2026-10-18-p280.tsv)
*(14 slugs, 19 columns, `MANIFEST_CAP` `14 → 250`, **0 skipped on every row**)* ·
[`package-provenance.2026-10-18-p280.tsv`](../evidence/package-provenance.2026-10-18-p280.tsv) *(192
manifests graded per package)*.

`p279` closed by making every vendored-manifest count on these shelves **a lower bound**, because a
path vocabulary is a floor. 🟢 **Two of the three bounds are now closed, and the third is named.**

| bound | p279 | p280 |
|---|---|---|
| 🔴 the **cap** — `MANIFEST_CAP = 14`, which is `ls1intum/Athena`'s own manifest count | `leemonade/leemons`: **12 declaring of 114, 100 skipped** | 🟢 **72 declaring of 114, 0 skipped** — a **6× correction** |
| 🔴 the **residual** no path convention reaches (`ui/static/pyodide/`) | *"only reachable by name … this base has no such list"* | 🟢 **reached, with no list** — the payload declares `pyodide/pyodide` in `repository` **and** `homepage` |
| 🟡 the **path vocabulary** itself | two conventions added | 🟡 **a third class added** (`.vite` `.next` `.nuxt` `.turbo` build caches), **and it is still a floor** — stated, not claimed closed |

### 🔴 `leemonade/leemons` — the same verdict, six times better evidenced

**72 of 114 manifests declare `MIT`.** The committed `LICENSE.md` (10 830 B) is **FAIRCODE**.
🔵 `p121`'s operational rule is what a studio needs here — *"a manifest licence field is a HINT; the
committed licence file is the GRANT"* — and the number of hints is now 72. 🔴 **Any manifest-reading
licence scanner returns PASS on this repository**, and the obligation it misses is non-commercial.
🟢 **42 of the 114 declare nothing at all**, which is the honest remainder: silence, not a grant.

### 🟢 The counts that did NOT move are the control

`ls1intum/Athena` reads **14 in tree / 12 declaring / 1 distinct / 0 skipped** — `p275`'s census
exactly, now reproduced by a **third** independent instrument (`p275`'s enumeration, `p279`'s walk,
`p280`'s per-package grader). 🔵 **A vendoring predicate that rejects a monorepo's own workspace
packages destroys the very count it was added to protect** — `p279` measured that when a root-name
check rejected 12 of Athena's 14 — so `Athena` is the negative control, and it is unchanged.

## Pass 279 — a vendored-path exclusion is a FLOOR, so every "no grant here" on this shelf is a lower bound

🟢 **`p278` established that *a licence file inside a repository is not the repository's licence*
(`T58`). `p279` found the same principle one channel over, and it bites harder: a MANIFEST inside a
repository is not the repository's manifest either**, and the predicate this base uses to tell them
apart is weaker than the repositories it is pointed at.

🔴 **Measured, not inferred.** `tadreeb-lms/tadreeblms` vendors `moment`, `swiper`, `tailwindcss`,
`prismjs` and three CKEditor builds **twice**, under two different directory spellings in the same
repository:

| spelling | caught by `is_bundled` before `p279`? |
|---|---|
| `public/assets/libs/…` | 🔴 **no** — the vocabulary knew `node_modules/`, `vendor/`, `third_party/`, `dist/`, `build/`, `bower_components/`, `Pods/`, `.yarn/`, `target/`, `site-packages/` and not this |
| `resources/views/backend/assetslib/libs/…` | 🔴 **no** — and still not after `assets/libs` was added, which is the point |
| `inc/libraries/…` *(LearnPress, the WordPress convention)* | 🔴 **no** |

🟢 **All three spellings are in `lib/licence_path.sh` now, with 10 new controls — 4 positive and 6
negative, so the widening cannot swallow a real workspace package** (`packages/ai-assistant/`,
`apps/api/`, Athena's `assessment_module_manager/` and `src/libs/` are all asserted NOT vendored).
The **byte-for-byte identity control against `p196`'s copy stays green**, which is how this base stops
a shared predicate becoming a fork: the suite went **44/44 → 54/54**.

🔴 **The honest consequence for this shelf: a path vocabulary can only reject the conventions somebody
enumerated, and one repository defeated it twice inside one hour.** So every vendored-manifest count
published here is a **LOWER BOUND**, and the residual is named rather than hidden —
`Open-TutorAi/open-tutor-ai-CE`'s `ui/static/pyodide/package.json`, a bundled Pyodide runtime under a
path no convention names. 🔵 **The durable channel reads a package `name` against a list of known
third-party projects. This base does not have that list.** Registered for `p280`.

🔵 **And the controls themselves taught the lesson a third time.** They were first appended **below**
the suite's `echo "$p/$t"; [ "$p" = "$t" ] || exit 1` line — so they ran, graded nothing, and could
not have failed the build. **The count gave it away: 44/44 both before and after adding ten
assertions.** Position relative to the thing that reads you is load-bearing.

---

## Pass 278 — a licence file inside a repository is not the repository's licence, and the biggest LMS plugin on this base proves it twice

🔵 **Evidence:** [`tree-enumeration.2026-10-17-p278.tsv`](../evidence/tree-enumeration.2026-10-17-p278.tsv)
*(6 trees, every path enumerated)* ·
[`channel-conflict.2026-10-17-p278.tsv`](../evidence/channel-conflict.2026-10-17-p278.tsv).

🔴 **[`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) enumerates to 1,985 paths at
`ca5296320435`, and BOTH of its licence-like paths belong to something else:**

| path | what it is | verdict |
|---|---|---|
| `inc/libraries/wp-background-process/license.txt` | a **vendored third-party library's** grant | 🔴 not the project's |
| `inc/TemplateHooks/Admin/Notices/AdminNotesTemplate.php` | a **PHP source file** matching the licence-name pattern | 🔴 not a grant |

🟢 **`pass275-grant-enumeration`'s scope test rejects both** — `VENDORED` catches the first, `SOURCEY`
the second — confirmed by running `candidate_grants()` on the enumerated paths this pass, which
returns `[]`. **So the repository commits no grant of its own, and `p120`'s resolution stands: the
licence is GPL-3.0, declared in the WordPress `readme.txt`.**

🔵 **Why this belongs on a FOUNDATIONS shelf rather than only in a licence ledger.** A client's SCA
scanner that reports *"GPL-3.0 found"* from `inc/libraries/.../license.txt` has found a **dependency's**
grant and attributed it to the parent. **An intake gate must ask whose grant a path carries, not only
which grant it is** — the mirror image of the manifest problem, where the declared field is read as the
grant. Both errors are automatic, and both default to the wrong answer.

🟢 **`p277`'s declared sub-rule `T57` is discharged on this shelf too: every absence now carries its
path count**, and the counts span three orders of magnitude (15 → 15,448). *"No licence file in 15
paths"* and *"no licence file in 15,448 paths"* are the same sentence and different claims.

🟢 **And one declared item was already closed before it was ranked.** `p277` registered the `.vue`
false-candidate class for `p278` — `learningequality/kolibri-design-system`'s **15,448** paths carry
**7** licence-like paths, every one a **Material Design icon component**
(`precompiled-icons/.../copyright/*.vue`, `mdi/license.vue`). **`p277` had already fixed it in `p277`**
(`precompiled-icons` in `VENDORED`, `.vue` in `SOURCEY`); verified here rather than assumed.

## Pass 277 — six absences on this base stopped resting on path ladders, and one of them changed meaning when enumerated

🟢 **No row on this shelf changed licence this pass.** What changed is the **grade** under six absence
verdicts, which `P275`/`P278` hold is the difference between a sayable absence and an unmeasured one:
*to sustain an absence in a tree you must ENUMERATE it; a count of zero over a path that does not exist
in that ref measures the **path**, not the content.*

Each row below was re-run first-hand this pass — `git ls-remote` for existence, then a blobless
`--depth 1 --filter=blob:none --no-checkout` clone, then `git ls-tree -r HEAD`, then every candidate
path read at payload, plus eight manifest paths. Evidence:
[`tree-enumeration.2026-10-17-p277.tsv`](../evidence/tree-enumeration.2026-10-17-p277.tsv).

| row | was carried as | now rests on | licence-like paths | manifest grant |
|---|---|---|---|---|
| [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) | *"no payload on 19 of 19 paths"* | 🟢 **310 paths enumerated** | **0** | none |
| [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) | *"(no payload)"*, `repos/foundations.md` | 🟢 **190 paths enumerated** | **0** | none |
| [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) | absence asserted, 3 lines | 🟢 **119 paths enumerated** | **0** | none |
| [`autograder-org/autoGrader-frontend`](https://github.com/autograder-org/autoGrader-frontend) | absence asserted | 🟢 **36 paths enumerated** | **0** | none |
| [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) | absence asserted, 2 lines | 🟢 **31 paths enumerated** | **0** | none |
| [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) | absence asserted | 🟡 **11 paths enumerated** | **0** | none |

🔴 **`OpenEMIS/OpenEMIS-Core` is the row where enumeration did not confirm the verdict so much as
reframe it.** **Eleven paths in total is not a codebase.** The absence is true of *this repository* and
tells a studio **almost nothing about OpenEMIS the product** — an education-management system used by
ministries. A reader told *"OpenEMIS serves no grant"* will conclude the platform is unlicensed; what
was actually measured is an eleven-file shell, which is consistent with the code living elsewhere (a
release artefact, a different org, or submodules a blobless clone does not expand).

🟢 **New sub-rule, and it is cheap to apply: publish the path count beside every absence.** An absence
over **310** paths and an absence over **11** are not the same claim, and this shelf has been writing
them in the same words. 🔵 **The counts are already being collected** — every enumeration this base runs
produces one — so this costs a column, not a probe. Registered for `p278` as `T57`.

⚠️ **One limit of the method, stated because it bounds all six rows above.** A blobless
`--no-checkout` clone enumerates the tree **at one ref** — `HEAD` — and `p269` already paid for ref
sensitivity here (`learningequality/kolibri` serves **MIT on `develop`** and **404 on `main`**). **These
six are enumerated at `HEAD` only.** A grant sitting on a non-default branch would still be missed, and
six clean trees do not discharge that. **The absences are upgraded, not closed.**

## Pass 276 — the permissive table was missing its separator, and two foundations were missing their grants

🔴 **A formatting defect first, because it hid `p274`'s own prize row.** The permissive table's
`|------|` separator sat **below** the `Gego-K12/gegok12` row rather than above it, so the row this base
spent two passes recovering rendered **as part of the table header**. Restored this pass. 🔵 **No gate on
this base reads table structure**, which is why a defect in the shape of the evidence outlived several
passes of scrutiny of its content.

🟢 **Two rows join the permissive tier, and neither came from a search:**

- **`meyerjp3/psychometrics`** — `Apache-2.0`, declared in `pom.xml` `<licenses>`. This base already
  graded it correctly at manifest grade; `p276` read the manifest first-hand and promoted it onto this
  shelf, where the **IRT-linking and score-equating** layer had no permissive answer at all.
- **`open-spaced-repetition/fsrs4anki-helper`** — `MIT`, at **`License`**: mixed case, no extension. Six
  filename probes missed it; one `git ls-tree -r` found it.

🔴 **And one absence became a procurement finding.**
[`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials)
— the **European Commission's own** European Digital Credentials reference implementation — serves **no
grant across `2 970` enumerated paths** and **no `license` element in its `pom.xml`**. Its only
licence-like files are three `licenseInfo.mustache` codegen templates. ⚠️ **An EMEA credentialing
engagement cannot build on it as open source**, and this is the first time that is stated from an
enumeration rather than from a ladder.

**State:** `QUEUE-UNENUMERATED` **124 → 70**, `VERIFIED-ABSENT` **28 → 48**, `REFUTED` **0**.


## Pass 275 — a GPL-2.0 grant was sitting at `docs/License.txt`, and the ladder that missed it had been extended four times

⏱️ **Twenty-first pass of `2026-10-17`.** Evidence:
[`tree-enumeration.2026-10-17-p275.tsv`](../evidence/tree-enumeration.2026-10-17-p275.tsv) ·
[`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv) ·
[`verified-repos.2026-10-17-p275.tsv`](../evidence/verified-repos.2026-10-17-p275.tsv).

- 🟢 **`ls1intum/Athena` is CLOSED, and it closed upward.** Carried on this shelf as *"still silent — no
  grant across 76 path/ref probes over three passes."* **12 of its 14 manifests declare
  `license = "MIT"`**, unanimous. The 76 probes were aimed at the **root** `pyproject.toml` — a 632-byte
  Poetry workspace stub with **zero occurrences of `license`**. See `T47`: **a monorepo declares its
  grant per package**, and Athena's reusable modules are exactly the packages that declare it.
- 🔴 **`os4ed/openSIS-Classic` was never unverifiable** (`verticals/solutions.md`): **`docs/License.txt`**
  serves verbatim **GPL-2.0**, HTTP 200, **17 286 B**, complete instrument, rider-cleared. The ladder
  tried `docs/LICENSE`; it never tried **mixed case + `.txt`**. The vendor comparison articles this base
  dismissed were right.
- 🟢 **Eleven carried absences are now DEFINITIVE rather than probabilistic**, because the trees were
  *enumerated* rather than sampled — and two are explained rather than merely confirmed:
  `datawhalechina/ai-edu-for-kids` has no payload because **its tree holds two files**, and
  `OpenEMIS/OpenEMIS-Core` holds **11**, confirming `p267`'s read that what this base can reach is a thin
  Docker packaging repo and **not** the ministry application source.
- ⚠️ **A licence-like path is not a grant.** `kolibri-design-system` enumerates **7** licence-like paths
  and **all 7 are Vue icon components** (`KIcon/precompiled-icons/mdi/license.vue`); openSIS carries **20**
  vendored dependency licences (ckeditor, PhpSpreadsheet, htmlpurifier); Artemis carries a
  `LicenseService.java`. The gate in `compose/code/pass275-grant-enumeration/` has a control for each.
- 🟢 **`make gate-enumeration` is now in `make hooks`** and will fail any shelf that asserts an absent
  grant an enumeration refutes. **`QUEUE-UNENUMERATED=124`** negative verdicts across this base still
  rest on a ladder — the honest size of the backlog, printed on every run.

## Pass 274 — the nine-pass nil on this file ENDS, with a row this base had refused twice

⏱️ **Twentieth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p274.tsv`](../evidence/verified-repos.2026-10-17-p274.tsv) ·
[`p274-websearch.2026-10-17-p274.tsv`](../evidence/p274-websearch.2026-10-17-p274.tsv) *(leg 9)*.

🔵 **The brief's platform/SIS/ERP leg ran and did what `p273` predicted: it re-served a claim this base
had already refuted.** 🟢 **And this time the re-service was RIGHT and the refutation was wrong.**

| what the leg returned | what `p274` established first-hand |
|---|---|
| *"GegoK12 … free, MIT-licensed open-source school ERP, built for self-hosting, PHP 8.4 + Laravel, core free forever under MIT with optional paid add-on modules"* | 🟢 **MIT CONFIRMED** at `Gego-K12/gegok12` `main/LICENSE`, `1 150` B, diffed and byte-accounted. 🟢 **The "optional paid add-on modules" half CONFIRMS this base's own open-core caveat** — so the vendor page and this base were each half right, about different things |
| Gibbon (GPL-3.0), RosarioSIS (GPL), OpenEduCat CE, openSIS, Academico, OpenOLAT (Apache-2.0) | 🔵 **All already shelved here or on [`verticals/solutions.md`](../verticals/solutions.md).** `Academico` reproduces `p272`'s MIT-at-payload finding |
| 🔴 **NOT ONE platform returned describes any AI feature** | 🟢 **Corroborates this base's standing structural read from the OUTSIDE:** the SIS/ERP layer has no AI, so the agent layer is the opening and the platform is the installed base. **An absence that confirms a thesis is worth recording as a result** |

🔴 **The method finding, and it is the one to carry forward.** Both of this file's standing refusals were
produced by probing a slug. **One slug was wrong** (`gegok12/gegok12` → `Gego-K12/gegok12`) and the
refusal recorded the probe count — *"15 path/ref combinations"* — **which reads as thoroughness and was
15 probes against a string.** ⚠️ **A negative licence result must record the slug and ref it probed AND
a positive control that the slug resolves at all** (`git ls-remote` returning refs), or it is not a
measurement. 🟢 **This base's ledger format already has the columns.** See `T44`.
## Pass 272 — no new rows, one measurement supplied, and two candidate rows refused

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) ·
[`p272-websearch.2026-10-17-p272.tsv`](../evidence/p272-websearch.2026-10-17-p272.tsv).

🔵 **This file gains no rows: the SEVENTH consecutive measured nil on education-specific supply.**
The brief's generic legs ran **last**, per `p269`'s standing instruction. Stated precisely, because *how*
it failed is the information:

- 🟢 **`academico-sis/academico`'s byte column is filled in** — `1,094 B`, `main/LICENSE`, MIT,
  *"Copyright (c) 2020 Thomas Debay and project contributors"*. The row carried `MIT | —` since it was
  shelved. 🔵 Worth noting the direction: the vendor page that surfaced it this pass says the licence
  **"is not named"**; the payload names it. **An aggregator's hedge is not evidence of absence.**
- 🔴 **`gegok12/gegok12` REFUSED** *(**SUPERSEDED** — overturned immediately below; the slug does not exist)* — an MIT claim with no payload on 15 path/ref combinations, and an
  **open-core shape** (26 of 38 modules free, 12 Pro modules sold) that would not deliver what the claim
  implies even if verified.
  🔴 **OVERTURNED IN PASS 274, AND THE SENTENCE ABOVE CONTAINS ITS OWN DIAGNOSIS: THE SLUG IS WRONG.**
  `gegok12/gegok12` **does not exist** — it fails `git ls-remote` identically to any nonexistent
  repository, so *"no payload on 15 path/ref combinations"* was 15 probes against a **string**. The
  repository is [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12), and it serves **MIT** at
  `main/LICENSE`: **HTTP 200, `1 150` B, full payload read, normalised terms diff against stock differing
  only in line-wrap column, zero rider keywords.** The `+82` B over stock accounts **exactly**: `+39`
  SPDX HTML comment, `+8` four typographic quotation marks, `+35` a longer copyright holder
  (*"GegoSoft Technologies and GegoK12 Contributors"*). 🔵 **Two instruments produced the same false
  negative and both read like a measurement:** a kebab-case slug guess (`T15`'s trap, here taking down a
  licence verdict) and a byte **ceiling** (`T39`'s proof, upward). See `T44`.
  🟢 **The open-core half of the refusal STANDS and is the only live caveat**: MIT covers the core, **12
  Pro modules are sold separately** (`T20`, failure mode 3). **Quote the grant, scope the modules.**
  🟢 **Row added below** — and note where it lands: this base's standing APAC gap is *platform supply*,
  and `P933` has already measured this repository's **98 forks with near-zero fork stars and
  institution-shaped fork names across India, Indonesia and Vietnam** — the signature of software that
  institutions **run**. ⚠️ **Deployment-placed APAC on that fork evidence; origin NOT established** (a
  copyright holder's name is not a provenance read).
- 🔴 **`projectfedena/fedena` REFUSED, reproducing `p265`** — and `p272` adds the provenance of the false
  claim: it comes from **a direct competitor's comparison page**.
- 🟡 **Two repositories were LOCATED BUT NOT RESOLVABLE, and they are recorded as an informed gap rather
  than as rows: `Bloom`** (Socratic-method tutoring) **and `Lumen`** (self-hosted, course-scoped RAG with
  citations). A GitHub topic listing named them **without an owner/repo**, so there is no slug to probe.
  ⚠️ **A project name is not a row.** Resolving these two is a cheap, named step for `p273`.
  🔴 **RETRACTED IN PASS 274 — BOTH LIMBS WERE ALREADY IN THIS BASE.**
  **`Bloom` = [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom), MIT, `1 069` B** — and it has been a
  **row on [`agents/top.md`](../agents/top.md)** since `p264`, which is where the contradiction is
  sharpest: *that* file declares the same slug unresolvable in a later section of itself, 168 lines below
  the row that tables it.
  **`Lumen` = [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen)**, resolved from this base's **own
  `p195` licence census** via [`compose/code/p196-population-diff/`](../compose/code/p196-population-diff/),
  which recorded it at **GPL-3.0, `35 149` B** — reproduced to the byte in `p274`.
  🔵 **Neither resolution needed a search; one needed a `grep` of this repository and the other needed a
  `grep` of this file's sibling.** `p272` spent a search leg on them and `p273` ranked spending another.
  **`T25` re-earned, and `T34`'s amendment — grep the other shelves before re-declaring an absence —
  failed because nobody ran it on this gap.**

🔵 **The supply conclusion is now stable across seven passes and three languages:** education-specific
permissive *agents* are scarce, the generic legs return either general-purpose frameworks this base already
holds or **learning-ABOUT-AI** teaching material, and the growth on these shelves comes from
**platforms, standards and assessment engines** — this file's actual subject — rather than from agents.
**Nothing was added to meet a quota.**

## Pass 270 note — no rows added, and the three legs that would have added them were not run on purpose

🟢 **This file gains no repositories this pass.** `p269` measured the generic supply legs
(`top open source AI agents education`, `github trending education AI`, `open source platform /
ERP / SIS`) as **saturated across four consecutive passes** — nine platforms returned, **all nine
already shelved**, zero education-specific agents — and instructed that they be spent **last, not
first**. **Pass 270 did not spend them at all.** It ran one targeted supply leg instead
(`Gap 367`'s Spanish limb), which returned **nine repositories, eight of them university student
course portfolios and the ninth already held.**

🔵 **The brief's five-repo minimum is met many times over by the table above, and nothing was added
to pad it.** An informed nil return is the honest output of a saturated channel; a padded row is
not. **Where this base's shelf-grade rows have come from for five consecutive passes is probing a
named thing by hand or grepping this repository** — not from a generic search leg.

🟡 **Where this file is still weak, restated rather than quietly inherited:**
- 🔴 **No permissive North American system of record.** The **Ed-Fi** stack remains shelved
  (`p268`), and nothing has replaced it.
- 🟢 **CLOSED in `p275` — `ls1intum/Athena` was never silent, and the 76 probes were aimed at the
  one manifest that is.** No licence *file* exists (tree **enumerated**: 691 paths, zero
  licence-like), but **12 of 14 manifests declare `license = "MIT"`**, unanimous. The ladder
  probed the ROOT `pyproject.toml` — a 632-byte Poetry workspace stub with **zero occurrences of
  `license`**. 🔵 **A monorepo declares its grant per package**, so a root-only metadata probe
  cannot see it. The *"worth an email"* judgement is inverted too: Athena needed no email, and
  `muskvdc/EduTwin-Africa` (`PRE-LICENCE`, `p269`) remains the row where asking is the only path —
  its tree was enumerated this pass as well (384 paths, nothing licence-like).
- ⚠️ **A ref-sensitivity reminder that cost a published figure once:** `learningequality/kolibri`
  serves **MIT on `develop`** and **404 on `main`**. Probe the **resolved** default ref
  (`git ls-remote --symref`), never a guessed one.
