---
industry: education
region: Global
updated: 2026-10-23
---


**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No platform
was added.** The vertical-platform leg returned **OpenEduCat**, **ERPNext** (GPL-3.0), **Twenty CRM**
(BSL-1.1, not OSI-permissive) and **Odoo** — 🔴 all already carried or already excluded here, and the
leg's own summary again volunteered this shelf's standing result: *"no education-specific MIT or
Apache platform"*, the capable ones being AGPL, GPL or source-available.

🟢 **What changed for this shelf is upstream of it.** Every platform here is deployed into a
jurisdiction, and [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) — the file a deployment
pre-flight actually reads — 🔴 **carried no LATAM teaching-mandate row at all** until this pass.
🟢 It now carries **six**, headed by **Colombia's `Ley 2626 de 2026`** (binding, official schools,
curricular guidelines due **Feb 2027**).

🔵 **Concretely for this shelf:** a Moodle, Open edX or Chamilo engagement in **CO** is no longer a
greenfield curriculum question — there is a statute naming the competencies the deliverable must
carry, and a **Feb 2027** date it must land before. 🔵 That is a scoping input, not a licence one,
which is why it is recorded here as a pointer rather than as a new row. `Gap 398-C`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No platform was
added.** The open-source-LMS leg returned **Open edX, Chamilo, ILIAS, Frappe LMS and Sakai** — 🔴 **all
already carried here**, and the leg's own summary volunteered what this shelf has recorded for many
passes: *"no strong option under MIT or Apache"*, the capable ones being AGPL or GPL. 🟢 **One tracked
signal did move.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) re-read first-hand —
**MIT**, **41.3k ★**, corroborating this base's `41 208` and the `p389` finding that a third-party
review's *"AGPL-3.0 with commercial licensing"* claim is simply wrong. 🆕 **`v1.3.0-rc.1` is dated
2026-10-22**, while [`repos/trending.md`](../repos/trending.md) tracked `v1.2.0-rc.1` (2026-10-04) as
*"still a pre-release, 11 days on"* — 🔴 **a second RC series opened without the first reaching
stable.** 🔵 For a platform recommendation that matters: the grant is clean and the adoption is real,
but **this project has not shipped a stable release in two RC cycles**, so pin a commit rather than a
tag. `Gap 398-C`.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **A platform's
address and a platform's *project* are not the same thing, and this pass can finally tell the
difference without reading prose.** `396-F`'s root-commit arm, extended with a HEAD comparison and
run over the shelf, folded **eight** address pairs into single artefacts — and one of those folds is
a **governance** change a studio should quote to a client. Evidence:
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

### 🔴 The fold this pass thought it had found, and the register that already held it

🔴 **`p397`'s draft announced the credential wallet's move to a Linux Foundation umbrella as a
governance finding. This shelf already carries it, and `p350` put it there.**
[`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
is recorded `CANONICAL` in [`alias-register`](../evidence/alias-register.2026-10-21-p370.tsv), with
`digitalcredentials/learner-credential-wallet` as its **STALE** sibling, proven at `p349` from the
search index's `full_name` and repository `id` — and `p350`'s note says in so many words that the
canonical was **already applied to this shelf**. 🟢 Caught by `gate-alias-canonical`, which went red
on the draft.

🟢 **The substance stands and is worth restating once, because it is what a client actually asks:**
the MIT Digital Credentials Consortium wallet is maintained under **OpenWallet Foundation Labs**, a
**Linux Foundation** project — a materially better answer to *"who maintains this after the grant
ends"* than *"a university lab"*. 🔵 **What `p397` adds is corroboration from an independent
channel**, not the fact: shared root `af51e5505cbf`, identical HEAD `1c46a82ba384`, read from git
with no index and no API.

🟡 **And one register row this pass can genuinely move.** For `ease`, the register's index channel is
**blind** — both rows read `index-returns-ZERO` / `NO-CANONICAL`, which is why **`ACTION ZZ-al`** has
been unresolved since `p350`. 🟢 The clone arm proves [`openedx/ease`](https://github.com/openedx/ease)
and `edx/ease`, its **STALE** sibling, are **one repository** (shared root `79dd16652a23`, identical
HEAD `056da0adc6f3`) without the index at all. 🔴 **It cannot say which address is canonical**, which
is `ZZ-al`'s real question — so the identity half is proven and the direction half is still open.
🔵 Prefer the `openedx` path for anything written today, on the stewardship argument rather than on
the register.

### 🔵 The standards layer, de-duplicated

🟢 **`IMSGlobal` → `1EdTech`** is a rename GitHub keeps answering on both paths, and this base
harvested both for `caliper-spec`, `openbadges-specification` and `lti-1-3-php-library` — three
"pairs" that are three repositories, not six. 🟢 **Cite the `1EdTech` path** when writing a conformance
clause into a statement of work; it is the one the standards body publishes from.

🔵 **What did NOT fold, and that is the useful half:** `OpenLRS`
(`Apereo-Learning-Analytics-Initiative` vs `openHPI`), `qti-convert` (`citolab` vs `rolfis`),
`ims-lti` (`instructure` vs `omsmith`) and `lrs` (`yetanalytics` vs `escolalms`) all have **distinct
root commits** — same name, unrelated code. 🔴 **Four same-name pairs on this shelf that a
name-matching de-duplication would have wrongly merged**, which is the error the arm was built not to
commit.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** 🟢 **The platform question this shelf could not
answer until now: once a platform is customised, where does the learning data go, and can the client
own it?** `p395` settled how an agent *launches* from Moodle, Canvas, Blackboard or D2L (LTI 1.3).
This pass settles how it *records*. Evidence:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

### 🟢 The emitter shelf — getting data out of the platform

| Platform | Emitter | Licence | HEAD | Age | Note |
|---|---|---|---|---|---|
| **Moodle** | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 **GPL-3.0** | `df5c665` | 🟢 **2 d** | 82 ★, 95 forks — the live, maintained route out of Moodle |
| **Open edX** | Aspects → [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** | `91fef11` | 🟢 **10 d** | Open edX's own analytics stack **already ships Ralph as its LRS** |

🔵 **The Moodle row is a licence note, not a licence problem.** `moodle-logstore_xapi` is GPL-3.0
because every Moodle plugin is — Moodle itself is GPL, and a plugin inherits the obligation. A studio
deploying it into a client's Moodle is *using* it, not redistributing a derived product, which is the
ordinary posture for the whole Moodle plugin estate already on this shelf. 🔴 It is a problem only if
a client wants the emitter embedded in a proprietary product they ship.

🟢 **The Open edX row is the strongest platform+AI story on this shelf**, and it needs no
integration work invented here: Open edX Aspects already selected Ralph as its LRS with ClickHouse
underneath. A studio customising Open edX gets an **MIT, 10-day-fresh, French-public-sector-maintained
LRS** in the architecture by default.

### 🔴 What is NOT on this shelf, stated because the absence is the finding

🔴 **No permissive LRS ships inside any of the big platforms.** Moodle, Canvas, Blackboard and D2L
all expect you to bring one. 🔴 **And `LearningLocker` — the LRS almost everyone names — has not had
a commit since 2021-11-16 (1,801 days), is GPL-3.0, and carries no archived banner or deprecation
notice on its page.** 585 ★ and 294 forks make it look maintained. 🔵 **This is the single most
likely wrong decision a studio could make on this layer**, and nothing on GitHub warns against it.

🟢 **The replacement depends on the client's runtime**, which is the cross-layer table in
[`repos/foundations.md`](../repos/foundations.md): Python → Ralph, JVM → `lrsql`, .NET →
`xapi-dotnet`, Node/TS → `pelotech/xapi-lrs` **only after you run the conformance suite yourself**.

### 🟡 A conformance toolkit worth watching, not yet worth quoting

[`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) — 🟢 **MIT** (1,080 B,
`df57b343c1a3`), HEAD `3596bb5`, **37 d**, 🔴 **2 ★** — is a TypeScript monorepo offering typed
contracts, a headless QTI runtime and conformance runners across **xAPI, cmi5, LTI 1.3, QTI 2.x/3.0,
Caliper, Common Cartridge, CLR 2.0, Open Badges 3.0, OneRoster 1.2, CASE, h5p and W3C VC 2.0**. Its
`package.json` wires `lrsql` as its xAPI backend through podman-compose, so the pairing is real code
rather than a claim.

🔴 **Two stars.** 🔵 Recorded here because it is the only address found that covers the standards
surface this shelf cares about in one place, and because its own README is unusually honest — it
states plainly that it is *"not affiliated with, endorsed by, or certified by 1EdTech, ADL/ADLNet,
W3C"* and that it produces *"conformance assessments, not official certification."* 🟡 **Do not quote
it to a client as a conformance guarantee.** Watch it; re-date it next pass.


# Education vertical platforms — real systems to customise with AI on top

**🆕 Pass `p395` · reads and commit both 2026-10-23.** 🔴 **A constraint that lands directly on this
shelf's headline pattern.** `p394` shelved **LAMB** on the strength of its publishing into **Moodle as
an LTI external tool** — so the LTI layer is load-bearing for the platform story here, and this pass
dated all 13 known LTI 1.3 addresses: [`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).
🟢 The maintained permissive set is **PHP, Node and Python** (`packbackbooks` 6 d, `ltijs` 9 d,
`lti-tool` 1 d, `django-lti` 2 d, `ltiauthenticator` 113 d). 🔴 **There is nothing live in Go or
Java** — `StevenWeathers/peregrine-lti` 679 d, `UOC/java-lti-1.3-core` 1,193 d, `macewan-cs/lti`
1,918 d. 🔵 **At procurement this is the question to ask before the licence question:** *what runtime
does the client's platform team own?* A Java shop cannot take an in-process LTI dependency from this
base at all, and should be quoted an HTTP edge instead (see `Pattern AC`).

🟢 **Re-confirmed independently, not inherited:**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp)'s grant was re-read at the
payload this pass — **8,241 B at `master/LICENSE`**, *"OpenEduCat is published under the GNU LESSER
GENERAL PUBLIC…"* — which **agrees with this shelf's existing LGPL-3.0 row**. 🔵 Recorded because a
re-read that agrees is the only thing that makes a re-read that disagrees meaningful, and this shelf
has had several of the latter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** 🟢 **One addition, and it is the
EMEA-authored platform layer this shelf has been short of.** [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb)
— **LAMB, Learning Assistants Manager and Builder** — 🟡 **GPL-3.0** (35,349 B, `sha256`₁₆
`17fe6d0ffa96`, read first-hand), **7,087 files**, HEAD **2026-10-20 — 2 d**. Teachers build LLM
learning assistants **with no code** and publish each one into **Moodle as an LTI external tool**; its
companion [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) is the **LTI activity module
for assignments graded by a LAMB assistant**. Authored by **Marc Alier (UPC Barcelona)** and **Juanan
Pereira (UPV/EHU)** and published in *Computer Standards & Interfaces*. 🔴 **Maturity caveat carried on
every LAMB row:** its own Moodle.org thread (Feb 2026) calls it *"at a very beta stage"* with *"a few
universities running pilots"*, so this is a **pilot base, not a ministry platform** — said here and in
the pattern, not only in the evidence file.

🔴 **Three grants in one tree, which is `p382`'s subtree axis and it matters at procurement.** Root
**GPL-3.0**; `lamb-kb-server-stable/` carries its own stock **GPL** payload; and `open-webui/` is a
**vendored third party** under verbatim **BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). A root-only licence
read is wrong about this repository in both directions. 🔵 That vendored BSD payload is also the
specimen that exposed **`P459`**: this base's own grant gate was reading verbatim BSD-3 as
`granted: False`, because *"All rights reserved."* is line 2 of the BSD template.

🔴 **Also corrected on this shelf's neighbours:** `anastasasenov/bbmcps`, carried across these shelves
as one of nine Blackboard servers, is **not a Blackboard Learn integration at all** (deps `mcp` +
`sqlite3`, no Learn API surface; `blackboard://` is the *architectural pattern*). Blackboard goes
**9 → 8 addresses, 6 MIT + 2 dead + 0 ungranted**. See [`agents/top.md`](../agents/top.md).

**🆕 Pass `p393` · 2026-10-22.** Three additions, all from the new `pypi.org/simple/` index-dump
channel ([`compose/code/p393-pypi-index-channel/`](../compose/code/p393-pypi-index-channel/README.md)):
🟢 a **permissive LATAM-native LMS** (`now-lms`, Apache-2.0, Nicaragua) on the four-way decision, the
🟢 **Ed-Fi** K-12 data path for North America, and the 🔴 copyleft **QTI exchange** layer for EMEA
assessment migration. Region placements updated under *Regional fit*.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md`](../archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md).
All addresses and licences verified first-hand on this date —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).
🆕 **`p386` adds the permissive-base row this shelf has been missing**, and corrects the MCP section
below: Blackboard and D2L both have verified MIT servers now.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p386.tsv).

🆕 **Pass `p392` · 2026-10-22.** Two of this shelf's sentences are **withdrawn and replaced**, both
of them absences this base held the refutation for in its own harvest log: the **interop boundary**
row (Python LTI 1.3 is in-process after all — `django-lti`, MIT, 2 days) and the **proctoring**
bullet at the end (two granted components, one clean). Both were found by the instrument built this
pass — [`gate-capability-absence`](../compose/code/p392-capability-absence/README.md) — rather than by
accident, which is the first time that is true of this error class.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p392.tsv) ·
[`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

This shelf answers one question: **what existing system does the client already run (or could run),
and what can be bolted onto it?** Same role Odoo plays for ERP or OpenMRS for healthcare.

🆕 **`p389` adds a fifth answer to that question, and it is a different kind of answer: what if the
client runs nothing, and the *classroom itself* is the platform?** See
*[The generated classroom as a platform](#-p389--the-generated-classroom-as-a-platform-openmaic)*.
`p389` also **dates every base on this shelf** — 60 addresses, last-commit date read from the payload
at the real default ref — and the dates change two things below: a decade-dead lookalike sits at the
obvious ERP address, and the Canvas row needs a sentence it did not have.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv).

## Choosing the base: the four-way decision

| if the client needs… | base | licence | the catch |
|---|---|---|---|
| **To own closed extensions to the platform itself** | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Smaller plugin ecosystem than Moodle; more build, less assemble. **The only permissive major LMS.** |
| **The widest plugin ecosystem and the largest talent pool** | [Moodle](https://github.com/moodle/moodle) | 🟡 GPL-3.0 (`COPYING.txt`) | Copyleft on anything linked. Extend through web services / the MCP plugin, not by patching core. |
| **MOOC scale, cohort analytics, deep data control** | [Open edX](https://github.com/openedx/edx-platform) + [tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | AGPL reaches **hosted** use. Build XBlocks and LTI tools; keep proprietary logic the other side of the boundary. |
| **🆕 `p389` No incumbent platform at all, and lessons needed now** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** | Not an LMS: no enrolment, no gradebook of record, no SIS. You get the *teaching surface* and you still owe the system of record. See the section below. |
| **🆕 `p390` To *ship* a modified platform, not host one** | [OLI Torus](https://github.com/Simon-Initiative/oli-torus) | 🟢 **MIT** | **The only permissive answer on this shelf, and the catch is staffing, not licensing.** Carnegie Mellon Open Learning Initiative's courseware engine: authoring + delivery, adaptive scripted activities, per-objective mastery reporting, LTI 1.3 delivery into a host LMS. Every other base of comparable scope here is GPL/AGPL, so this is the row to reach for when the deliverable is **software the client redistributes or embeds in a product**. 🔴 **Elixir/Phoenix + PostgreSQL** — a genuine staffing constraint; cost the hiring before proposing it. 🔴 Slug trap: `CMU-OpenLearning/oli-torus` does not resolve. Dated **2026-10-22**. |
| **🆕 `p393` To ship a small permissive LMS, in Spanish, with billing already in it** | [now-lms](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | **21 ★** and no multi-tenancy claim. A Flask application a studio can read in a day — which is the point — but not a ministry platform. |
| **North American higher-ed integration reality** | [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0, open-**core** | The published tree ≠ the commercial ecosystem. Scope integrations against the real tenant, not the repo. 🆕 `p389` **And the published tree is also *older than it looks*: `master` last moved 2026-04-30 — 175 days — while the `stable/*` branches move.** Read the API surface off the tenant, and if you must read it off the repo, say which ref. 🟡 🆕 `p390` **Dating caveat, so nobody demotes Canvas off a bad read:** its `master` last moved **2026-04-30 — 175 days**, but Canvas **ships from tags** (`v5.14.2` current), not from the default ref. For any tag-releasing project, a last-commit-on-default-ref date under-reports maintenance; check `git ls-remote --tags` before calling it stale. |

### Regional fit
- **LATAM / Iberia:** 🆕 `p393` **the permissive option now exists and it is regional:**
  [now-lms](https://github.com/bmosoluciones/now-lms) (🟢 **Apache-2.0**, © BMO … S.A., **Nicaragua**;
  676 files, 505 commits, HEAD **2026-08-31**) is the only Spanish-language LMS on this shelf a studio
  can fork and ship **closed**. Use it for SME and pilot delivery; keep Chamilo for public-sector scale.
  [Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — strongest
  Spanish/Portuguese public-sector base. [academico-sis/academico](https://github.com/academico-sis/academico)
  (MIT) for SME-scale administration with Spanish built in.
  🆕 `p387` For **Brazil specifically**, the base a municipal engagement will already be running is
  [portabilis/i-educar](https://github.com/portabilis/i-educar) (GPL-2.0-or-later, **real default
  ref `2.12`**) — see the administration table below — and the agent tier now has three granted
  LATAM-native options on [`agents/top.md`](../agents/top.md),
  including one that ships **as an Open edX plugin** rather than as a separate app.
- **EMEA public sector:** [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) (GPL-3.0, default ref
  `release_11`) and [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland).
  🆕 `p393` For **assessment migration**, which EMEA procurement is beginning to specify as QTI 3.0:
  [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0** — run it
  as a batch tool at arm's length, never linked), from the lab of **Cito, the Dutch national assessment
  institute**. For a **Swiss university** engagement,
  [Dathis/swiss-moodle-mcp](https://github.com/Dathis/swiss-moodle-mcp) (🟢 MIT) already speaks ZHAW,
  FHNW, ETH and EPFL Moodle with **SWITCH edu-ID** user-held authentication — 🔴 but at **0 ★** and
  self-described as an unofficial student project, so it is a pilot reference, not a dependency.
  [Serlo](https://github.com/serlo/serlo.org) (Apache-2.0, Germany) and
  [Richie](https://github.com/openfun/richie) (MIT, France) for content and catalogue.
- **APAC:** Moodle itself is Australian in origin; [netless-io/flat](https://github.com/netless-io/flat)
  (MIT) for live online classrooms.
- **Low-connectivity anywhere:** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
  default ref `develop`) — offline-first by design, not as a degraded mode.
- **K-12 administration anywhere:** [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
  (GPL-2.0, default ref `master`) — the student-record half that no permissive base supplies.
- 🆕 `p393` **North America K-12 data integration:** the standard is **Ed-Fi**, and the granted client
  is [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) (🟢 **Apache-2.0**,
  stock 11,357 B, HEAD **2026-10-06 — 16 d**). The **Canvas / Google Classroom / Schoology → Ed-Fi**
  extractors exist at [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit)
  (🟢 Apache-2.0) 🔴 **but that repository was ARCHIVED by its owner on 2025-03-10 and is read-only** —
  port its field mappings, never depend on it.

## 🔴 The sovereign-stack story in EMEA, corrected

The previous pass carried a headline that **openDesk Edu** was deployed in **8,600 German schools**
and then downgraded it to "traces to a single news item with no official confirmation". **This pass
re-ran the search and the downgrade stands — in fact it goes further:**

- What is **confirmed**: openDesk is a free and open-source productivity suite from **ZenDiS** (the
  German Center for Digital Sovereignty in Public Administration); **v1.0 released 20 Oct 2024**.
  ZenDiS works with France's **DINUM** on the French equivalent **LaSuite**, and the two agencies
  added videotelephony, note-taking and SSO to both suites in **100 workdays**.
- What is **not confirmed**: **no school deployment of openDesk appears in any source found this
  pass.** Named users are public-administration bodies (BWI GmbH for the Bundeswehr, the ÖGD public
  health service). Germany's **DigitalPakt Schule** (€6.5bn school infrastructure) is a separate
  programme and is not evidence of openDesk in schools.
- **How to use it anyway:** the *pattern* is real and sellable even if the school number is not —
  **ILIAS (learning) + OpenProject (collaboration) behind a single SSO**, all open source, all
  EU-hosted. That is the sovereign education stack an EMEA public-sector client will ask for. Sell
  the architecture; do not quote the 8,600.

## Student information and administration

| platform | repo | default ref | licence | fit |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 `19.0` | 🟡 LGPL-3.0 | Odoo-based SIS/ERP: admissions, curriculum, fees, library, hostel. The Odoo ecosystem is the reason to pick it — AI modules can be ordinary Odoo addons. |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 MIT | Laravel, Spanish + French built in, SME-scale: courses, enrolments, scheduling, reports. |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 `master` | 🟡 GPL-2.0 — 🔴 grant at **`docs/License.txt`**, not at any root path | 🆕 `p384`. The K-12 default: enrolment, attendance, grades, scheduling, parent/student portals. GPL-2.0 is survivable the Moodle way — reach it over its API, never link. 🔵 A root-only licence read reports this repo as ungranted; it is not. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 AGPL-3.0 (`license.txt`) | Only where the client already runs ERPNext — then the student record and the finance record are one system. |
| **i-Educar** 🆕 `p387` | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 GPL-2.0-or-later (`2.12/LICENSE`, 18,092 B) | 🟢 **The LATAM row this table was missing.** Brazil's largest free education software — municipal student records, enrolment, grades — deployed by Brazilian municipalities at scale and maintained by Portabilis plus a community. 🔴 Its default ref is the version branch **`2.12`**: clone and read the grant there, not at `main` or `master`. Reach it over its API; keep AI alongside it, never inside it. Sibling `i-diario` (classroom diary) is **AGPL-3.0** — different grant, same organisation. |

### 🆕 `p386` — the permissive ERP **base**, since the permissive education ERP does not exist

Every row in the table above is copyleft except `academico` (MIT, SME-scale). The prescribed ERP/CRM
research leg was run directly at that gap. **It does not close it** — no education-specific
permissive ERP was found, which *confirms* the structural claim on
[`repos/foundations.md`](../repos/foundations.md) — but it returns three permissive bases, all three
licence payloads read first-hand this pass:

| base | real default ref | licence | what you get, and what you build |
|---|---|---|---|
| [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 🔴 **`master`** | 🟢 **MIT** *(1,077 B, "Copyright 2010-2025, Webkul Software"; `composer.json` also declares `"license": "MIT"`)* | Laravel 13 + FilamentPHP 5 modular ERP **with a plugin system**: accounting, inventory, HR, CRM, projects, and a Filament admin panel a client's staff can actually use. 🔴 **No education module** — admissions, curriculum, fees, attendance and transcripts are **your build**. |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** *(version branch; no `main`)* | 🟢 **MIT** *(1,078 B, same Webkul holder)* | The **admissions funnel** as a CRM: lead → applicant → enrolment, with the pipeline, activity log and email already built. The piece an SIS always lacks and a school always asks for. |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🔴 **`trunk`** | 🟢 **Apache-2.0** *(11,906 B; `NOTICE` 166 B, "Copyright 2001-2026 The Apache Software Foundation")* | The ASF alternative: accounting, CRM, manufacturing, order management. 🔴 Developer-facing and heavy — pick it for ASF governance and longevity, not for time-to-first-demo. 🆕 `p389` **Dated: `trunk` committed 2026-10-22 — 0 days. The ASF-longevity argument holds up.** 🔴 **But write the `-framework` suffix into the proposal.** [apache/ofbiz](https://github.com/apache/ofbiz) — the address anyone guesses — resolves, carries a valid Apache-2.0 grant, and its `trunk` **last moved 2017-02-12, 3,539 days ago**. It is the retired monolith. A client engineer who checks the obvious address finds a nine-year-dead tree and concludes the recommendation was careless. |

🔵 **What this changes in a pitch.** [OpenEduCat](https://github.com/openeducat/openeducat_erp)'s
**LGPL-3.0** used to be the only road to an open-source education ERP, so it was not a decision. It
is now a **trade against a named alternative**:

- **Take OpenEduCat (LGPL-3.0)** → admissions, curriculum, fees, library and hostel exist today, on
  the Odoo ecosystem, and AI features can be ordinary Odoo addons. You accept LGPL on the modules
  and the Odoo version-branch cadence (`19.0`).
- **Take Aureus (MIT) + Krayin (MIT)** → the client owns every line, including the education
  modules you write. You are costing **admissions, curriculum, fees, attendance and transcripts as
  a build**, on a base whose plugin system is designed for exactly that.

🔴 **Do not sell the second option as "an open-source education ERP."** It is a permissive ERP plus
a scoped education build, and the honest version of that sentence is the one that survives the
client's own technical review.

🟡 **Still not found, and still the clearest build-vs-buy opening in the rotation:** no open-source
Brazilian or Mexican academic-management system. Aureus + Krayin is now the most *defensible*
starting point for one — Laravel, MIT, and `academico` (MIT, Spanish-native) already proves that
stack fits the region's SME school market.

## Content, assessment and media layers

| layer | platform | licence | note |
|---|---|---|---|
| Interactive content | [H5P](https://github.com/h5p/h5p-php-library) | 🟡 **GPL-3.0** | Embeds in Moodle, Open edX, Canvas, Drupal, WordPress. 🔴 Widely mislabelled MIT. Treat as runtime content, not linked code. |
| 🆕 `p393` H5P **inside Open edX** | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** *(1,064 B)* | 🟢 **The permissive way to get H5P content into an AGPL platform.** Self-hosted H5P player as an XBlock — HEAD **2026-10-16 — 6 d**, 82 commits, 23 releases, **19 ★**. 🔵 Note the licence shape, which is `p390`'s firewall again: the **content library** above is GPL-3.0 and the **platform** is AGPL-3.0, but this bridge is MIT, so the part a studio writes against stays permissive. |
| 🆕 `p393` QTI assessment exchange | [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) (🟡 **LGPL-3.0**) · [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0**) | 🟡 / 🔴 copyleft | **Write** QTI packages for Canvas/Blackboard, and **convert** QTI 2.x ↔ 3.0. The assessment-portability layer this shelf had no row for. 🔴 Neither is permissive: use the LGPL one as a **linked dependency** and the GPL one as an **arm's-length batch tool**. 🔴 A third family — PyPI's `timeback-qti` / `-oneroster` / `-caliper`, 147 releases, MIT **declared** — has an **unresolvable source repository**, so it is listed here only as a warning, not an option (`Gap 393-B`). |
| Structured pedagogy | [Oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | Misconception-aware lesson branching. Permissive and pedagogically serious — unusual combination. |
| Open-response assessment | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | Peer + self + staff assessment rubrics. The place an LLM grader must plug in to stay auditable. |
| Lecture capture | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 | Video pipeline → the transcript corpus every education RAG build needs. |
| 🆕 `p390` Self-hosted video delivery | [Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube) | 🔴 **AGPL-3.0** | Federated (ActivityPub) video hosting — the option when lecture video must stay off YouTube and off a hyperscaler, which is a recurring EMEA public-sector requirement. 🔴 **Network copyleft: hosting it as a service for the client triggers source obligations** — fine for a public institution, usually not for a commercial product. Dated **2026-10-16**. 🔴 **A wrong-slug trap worth naming, because it inverts the licence:** [`PeerTube/PeerTube`](https://github.com/PeerTube/PeerTube) also resolves, is **3,660 days stale**, and reads **GPL-3.0** — so a careless licence read off that slug gets the *wrong grant* for the project, not merely a stale one. The canonical owner is `Chocobozzz`. |
| Live classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 MIT | Whiteboard, recording, real-time session. |
| Interop boundary | 🆕 `p392` [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) (**Python**) · [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (Node) · [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) (Node, **serverless**) · [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) (PHP) | 🟢 **MIT / Apache-2.0 / MIT / Apache-2.0** | **The copyleft firewall, and as of `p392` it is maintained in THREE languages including Python.** 🆕 `p392` `django-lti` (🟢 MIT, 1,098 B, HEAD **2026-10-20**, PyPI v0.10.1) puts LTI Advantage **inside** a Django agent — one middleware, no second runtime — so `p391`'s *"the edge must be Node or PHP in front of the agent"* is withdrawn; `lti-tool/lti-tool` (🟢 MIT, HEAD **2026-10-20**, npm `@lti-tool/core` v1.3.2) is the **serverless** Node option for Lambda / Cloudflare Workers, where `ltijs` assumes a long-running process with Mongo. 🔴 `p390` dated the standards-body reference copy at 2,332 days and concluded the boundary had no installable implementation; that was wrong. **`ltijs`** — npm v7.0.7, **207 versions, published 2026-10-06**, HEAD 2026-10-13 — and **`packbackbooks/lti-1p3-tool`** — packagist v6.4.4, **68 versions, published 2026-09-23**, HEAD 2026-10-16 — are both live, both Apache-2.0, and either one keeps permissive code the right side of a GPL/AGPL platform boundary without linking to it. Prefer **`ltijs`** unless the client's platform work is already PHP. 🔴 Cite [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) as the **spec reference only** — 2,333 days, and `IMSGlobal/lti-1-3-php-library` is the same project at a renamed org (identical HEAD `3a192de`). 🔴 There is **no maintained Python LTI library**, so the edge is Node or PHP in front of a Python agent. Full note in [`repos/foundations.md`](../repos/foundations.md). |
| Local-first tutoring workspace | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | 🆕 `p386`. Self-hosted, block-based adaptive workspace: PDF in → notes, flashcards, quizzes and an adapting tutor out, with **FSRS** scheduling, a knowledge graph and cognitive-load detection. Runs on local open-weight models — **no API key, no data leaving the host**, which is the answer to a DPO who will not approve an external model call at all. |
| Campus LLM gateway | [LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | Multi-provider, SSO, quota, audit log. The audit log is what gets a deployment past a university's data-protection officer. |
| Courseware platform | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🆕 `p384`. Django courseware with autograding, flexible access rules and per-student statistics. Course-scale and permissive — the base when the client must own the platform code but does not need an institutional LMS. |
| **Agent-native teaching OS** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 **AGPL-3.0** (`main`) · 🟢 MIT at tag `v0.1.0` | 🆕 `p385`. The **inverse** of every other row here: instead of bolting an agent onto an LMS, the classroom itself is an MCP server (~50 tools) and the agent is bring-your-own. Courses, lessons, FSRS flashcards, graded exercises, and a persistent learner-memory layer (`get_context` / `get_learner_brief`) that survives a change of model or session. 🔴 **v1 is single-machine and unauthenticated** — a pilot substrate, not a tenant-ready platform. AGPL reaches hosted use, so a client deployment must either accept that or pin the MIT `v0.1.0` tag and forgo upstream. |
| **Curriculum prerequisite graph** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | 🆕 `p384`. 1,930 micro-topics, 4,102 prerequisite edges, 9 subjects; aligned to NGSS, Common Core, UK National Curriculum, Australian curriculum. 🔴 **Share-alike database licence, not a code licence** — ground a tutor on it (§4.3 *Produced Work*, attribution only); do **not** ship an extended taxonomy (§4.4 *Derivative Database*, share-alike). See **Pattern H**. |

## 🟡 MCP has reached the LMS — and this is new as of 2026

This did not exist a year ago and it changes the integration story:

- 🆕 `p387` **Moodle, the tenancy layer — and this is the part a client-ready deployment needs
  before any MCP server:** [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
  (GPL-3.0-or-later, granted in `version.php`, release **5.1.1**) is a **multi-tenant AI backend**
  offered as the alternative to Moodle 4.5's own single-tenant AI subsystem: `aitool` subplugins
  connect providers (ChatGPT, Gemini, Dall-E, **Ollama** for on-premises), `aipurpose` subplugins
  bind a purpose to a provider **per role**, with per-role rate limits, per-tenant enable/disable,
  usage monitoring and capability-gated teacher visibility of student prompts. 🔵 The same project
  is also published at `mebis-lp/moodle-local_ai_manager` — **identical HEAD sha, one project, two
  addresses.** 🔴 Its own README warns it is **not compatible with core-AI-subsystem plugins and
  vice versa**: choosing it is an architectural fork in the road, taken once, early.
- 🆕 `p387` **Open edX, first-party AI extension point:**
  [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) (AGPL-3.0-only)
  is the platform org's own AI extensibility framework — **experimental**, but it is the contract to
  build against instead of forking `edx-platform`. Pair it with
  [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) for the agent-facing surface.

- **Moodle, first-party path:** the **`webservice_mcp`** plugin in **Moodle's own plugin directory**
  (and the Moodle Marketplace) exposes Moodle's external functions as **MCP tools over JSON-RPC
  2.0**. Supports **Moodle 4.5–5.2**, latest release **23 Jul 2026**, gated on the
  `webservice/mcp:use` capability. Configured inside Moodle — no fork, no patch, **no GPL exposure
  for the agent on the other side of it.**
- **Canvas, community path:** [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (MIT)
  and its fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT, adds office
  hours, syllabus read/write, student groups, course-content copy).
  [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) advertises 54
  tools and Streamable HTTP; it has **no licence file**, but `package.json` declares
  `"license": "MIT"` — 🟡 **manifest-only MIT**, usable if you record the manifest line and ask for
  the file.
- 🆕 `p386` **Blackboard, community path — and it is no longer empty.** Nine addresses probed,
  **6 MIT grants read first-hand**, 1 ungranted, 2 dead. 🟢 **[nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
  (MIT) is the only institution-grade LMS MCP server on any of these shelves**: official Blackboard
  Learn REST API, OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log,
  Prometheus `/metrics`, 40 tools including **grade write-back** (maintainer self-claims, read not
  executed). The other five —
  [Mattlo0546](https://github.com/Mattlo0546/blackboard-mcp),
  [alanwtom](https://github.com/alanwtom/blackboard-mcp),
  [lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp) (ref **`tcd`**),
  [felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp),
  [Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp) (ref **`master`**) — are
  **student-side**: they ride the signed-in user's own browser SSO session. 🔴 Granted, useful, and
  **not deliverable to an institution**.
- 🆕 `p386` **Brightspace / D2L — six addresses, six MIT grants.**
  [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) is the fullest
  (TOTP/OAuth/browser auth strategies, retry + circuit-breaker + cache, **opt-in writes**);
  [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) is the
  upstream of a fork family whose copies publish **byte-identical** licence payloads, so count it
  once. 🔵 **All six are student-side** — an institution-grade D2L server is the one genuine
  greenfield contribution left on this platform.
- **No official server** from Instructure, Moodle HQ, Anthology/Blackboard or D2L. 🟡 Verified gap —
  every server named on this shelf is community-built.
- 🔴 [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) is **UNGRANTED** — no licence file
  *and* no `license` field in its `pyproject.toml`. Use the plugin-directory route for Moodle:
  [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has no root
  licence file either, but its `version.php` carries the full **GPL-3.0-or-later** header that
  Moodle requires of every plugin, so it *is* granted.

## 🆕 `p388` — The parent portal is a platform surface, and it was missing from this shelf

This shelf asks *"what does the client already run, and what can be bolted onto it?"* For every
platform below it answered that for **the learner, the teacher and the administrator**. It never
answered it for **the parent** — yet in K-12 the parent portal is a shipped feature of every SIS and
the one surface families actually log into.

| platform | server | ref · HEAD | licence | what it bolts on |
|---|---|---|---|---|
| **Infinite Campus** (Campus Parent) | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS parent portal on this shelf.** 20 tools: schedule, assignments (`missingOnly`), grades + 14-day recent window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, messaging from three sources. Linked districts auto-discovered via **CUPS SSO**; `FeatureDisabled`-aware, so a district that has switched a module off degrades instead of erroring. **47 npm releases**, → 2026-10-19. |
| **Canvas** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | 18 `canvas_*` tools held to **the read-only observer surface** (`canvas_list_observees` is the hinge) plus student self-access; four auth modes in priority order; hardened file download (host-pinned, directory-confined, no symlink writes, `0600`). **43 releases**, → 2026-10-16. |

🔵 **Why it belongs on the *verticals* shelf and not only on the agents shelf.** Infinite Campus is a
**major North American K-12 SIS** that this base has only ever been able to name as a proprietary
system with nothing attachable. It now has a granted, maintained, MIT integration surface — so the
"what can be bolted on" answer for a US K-12 district changes from *nothing* to *the parent portal*.

🔴 **The boundary that decides the engagement, and it is not a licence boundary.** Both servers
authenticate as **a person** — a parent's own token, OAuth, or a scraped session. Deployed by a family
for their own child, that is the parent exercising their own access. **Hosted by a studio on behalf of
a district, the same call becomes an institutional disclosure of an education record and FERPA
governs it.** The code is identical; the obligation is not. 🆕 `Pattern P` in
[`compose/patterns.md`](../compose/patterns.md) is built around that line, and it is the same
tenancy problem `p386` found for student-side LMS servers — **the parent surface inherits it
unchanged**, which is worth knowing before a district pilot is scoped.

## 🆕 `p388` — Canvas: the integration surface reordered, and a FERPA mode shipped as a feature

`p387` recorded that the richest Canvas server (`canvas-mcp-server`, 54 tools) had not shipped since
**2025-06-27**. For a client engagement that mattered and there was nothing better to recommend.
There is now:

- 🟢 **[bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp)** — `main` · `34e6156`,
  🟢 **MIT** (1,070 B), `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22
  (today)**. **187 tools on the teacher/admin surface**, including the ones an institution asks about
  and demos usually lack: gradebook *history*, quiz **accommodations**, grading standards, content
  exports and migrations, outcomes, analytics, appointment groups, plus **link audit**,
  **accessibility audit** and **grade projection**. Three deployment modes (stdio, HTTP, library
  import). 🟢 **It ships a FERPA mode.** That is the first time on these shelves that an education
  compliance regime appears as a *product feature* of an open-source component rather than as a
  caveat this base has to supply — and in a procurement conversation it is worth more than the tool
  count.
- 🟢 **[Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local)**
  (`c7e5725`) and its remote twin
  **[`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server)** (`8e424f1`) — 🟢 **MIT**
  (1,091 B each), **209 tools on the student surface**, split deliberately into a **Local Edition**
  that opens no port and a **Remote Edition** on ngrok with OAuth 2.1 and multi-computer failover.
  🔴 The Remote Edition exposes a **public HTTPS address**: a school's decision, never a default, and
  not a thing to leave switched on in a pilot.

🔵 **Pick by persona, not by tool count.** 187 (teacher/admin) vs 209 (student) vs 20 (parent) is
**scope**, not quality: three different people reading the same institutional data. An engagement
usually needs one, occasionally two, and should deploy them separately — the FERPA posture differs
per surface, and a single server covering all three personas would be the hardest version of this to
get approved.

🟢 **And a wider Moodle surface than `webservice_mcp`:**
[gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) — `main` · `7962e49`, 🟡 **GPL-3.0**
(284 B short-form notice) — a Node client and CLI against Moodle Core web services **plus the MoodlIA
plugin, a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser
path. GPL survives here for the same reason it does for `webservice_mcp`: the agent reaches it over
REST, it is not linked.

## 🆕 `p389` — The generated classroom as a platform (OpenMAIC)

[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT**, Tsinghua University, real
default ref `main` @ `269fde2d991f`, **committed 2026-10-22 (0 d)**, ~41.3k ★. Grant read from the
payload: `LICENSE` is stock MIT text, `package.json` declares `"license": "MIT"`.
🔴 **A 2026 third-party review of this project reports it as AGPL-3.0 with paid commercial licensing.
That is false** — see [`agents/top.md`](../agents/top.md#-two-licence-traps-that-a-badge-read-would-miss).

**Why it belongs on *this* shelf and not only the agent shelf.** Every other row here is a system of
record that AI gets bolted onto. OpenMAIC inverts it: the artefact is a **classroom** — narrated
slides, an AI teacher with a voice, teaching assistants, simulated classmates, auto-graded quizzes,
HTML interactives, a shared whiteboard — generated from a topic or an uploaded document, and then
*taught*. It is a Next.js 16 / React 19 / TypeScript application on **PostgreSQL 16**, self-hosted
with Docker, and it has the three properties that separate a platform from a demo:

| property | what it is | why an institution needs it |
|---|---|---|
| **Server-first generation** (v1.2.0) | Generation runs on the server, survives closed tabs and restarts; the web app and the API share one pipeline | A teacher who closes a laptop does not lose a lesson. The demo-grade alternative generates in the tab. |
| **Central model governance** | Every AI use is a named **slot** in `openmaic.yml` (outline, slide content, TTS, web search, …), each pinned to a declared provider, keys referenced as `${VAR}` from `.env.local`; a capability is switched off with `video: null`, and the server can be configured to **forbid user-supplied keys** | This is the artefact a district's AI policy is actually written against: *which model saw student input, under whose contract*. Almost nothing else in this base can answer that in one file. |
| **Export to one offline HTML file** | A finished classroom exports as a single self-contained HTML that plays the lesson, or as a PPTX that keeps every scene | The low-connectivity story (`Pattern D`) **and** the procurement story: a reviewer can be sent the lesson without being given access to the system. |

🟢 **Local inference is a supported path, not a fork:** **Lemonade** for local models and **FunASR**
for local ASR, so a deployment that may not send audio or text off-premises has a configuration
rather than a rewrite. 🟢 **Provenance:** grew out of **MAIC**, run inside Tsinghua and validated on
**700+ students**; paper in **JCST 2026**. 🟢 **Security handled as product work** — five releases
since September 2026 carry SSRF, DNS-rebinding, access-token-expiry and provider-redirect fixes under
published GHSAs, which is a maturity signal almost nothing else on the agent shelf has.

🔴 **What you still owe, and it is the whole administrative half.** No enrolment, no gradebook of
record, no transcripts, no SIS, no LTI story stated. It is a **teaching surface**, so in an engagement
with an incumbent LMS it sits *beside* Moodle/Canvas/Open edX as a content and delivery tool, and the
system of record stays where it is. 🔴 **Pin the ref.** Head is **v1.3.0-rc.1** (knowledge base,
2026-10-22) and the project states **breaking upgrade conditions with no rollback below that
release**; a pilot pins **v1.2.1** (2026-10-18). 🔴 **Operational floor:** Node ≥ 22.19, pnpm ≥ 10,
PostgreSQL 16, a long-running server — Vercel is capped at the 1.1.x line, so "we'll put it on Vercel"
is a downgrade, not a deployment.

🔵 **Where it lands by region.** Origin is **APAC** (China), the interface is EN + zh-CN, and the
provider catalogue is built for a market that includes DeepSeek and Kimi alongside OpenAI, Anthropic
and Gemini. For an engagement under **EU AI Act** or **FERPA** constraints the slot-pinning and
forbid-user-keys controls are an asset, and the *data-residency* question is answered by the local
Lemonade/FunASR path — but the assessment features (auto-graded quizzes, mastery signals) are exactly
what Annex III and Vietnam's Decision 33/2026 treat as high-risk, so human review of any consequential
score is a build item, not a setting. See [`intel/trends.md`](../intel/trends.md).

## What is *not* available as open source, and matters

An informed gap, recorded so silence is not mistaken for coverage:

- **No open-source equivalent of Khanmigo or LearnLM.** The pedagogically-tuned model layer is
  closed across the board; the open supply is agents and scaffolding over general models.
- **No open-source Brazilian or Mexican academic-management system was found.** A targeted search
  for SIGAA source and for Portuguese/Spanish-language academic management on GitHub returned
  nothing usable. `academico` (MIT) and Chamilo are the closest fits, neither region-native at
  university scale. See [`intel/market.md`](../intel/market.md) — this is the clearest
  build-vs-buy opening in the current rotation.
- **No official Instructure or Moodle-HQ MCP server** (community only, as above).
- 🔴 🆕 `p392` **~~Proctoring and AI-detection have no credible permissive open-source option~~ —
  WITHDRAWN. There are two granted components, and one of them is clean.**
  [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
  manifest agrees, HEAD **2026-09-28**, npm v0.5.1) does tab-switch, camera, **face** (face-api on
  TF.js, in-browser), audio and **virtual-camera / loopback / screen-share** detection, and states
  *"nothing leaves the page unless you set `backend.endpoint`"*.
  [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) (🔴 **grant
  CONFLICT** — Apache-2.0 payload, ISC manifest and npm; HEAD **2026-10-13**, 398 commits) is the
  bigger codebase but ships **lockdown and event telemetry only** — its README marks object
  detection, multi-face and eye tracking *"(To be Done)"*.
  🔵 **What survives of the old sentence, and it is the half worth saying to a client:** the
  *liability* boundary is real and unchanged — an exam decision driven by either component makes the
  client a **deployer of an Annex III high-risk system** (standalone obligations from **2 Dec 2027**).
  The absence of code was never what made proctoring expensive; the obligations are. 🟢 So the honest
  advice flips from *"we cannot build this"* to **"we can build this, and here is what it commits you
  to"** — see [`compose/patterns.md`](../compose/patterns.md) `Pattern Y`. Full rows on
  [`repos/foundations.md`](../repos/foundations.md).
