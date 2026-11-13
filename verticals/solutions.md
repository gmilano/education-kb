---
industry: education
region: Global
updated: 2026-11-13
---

# Education vertical platforms — real systems to customize AI on top of


## 🟢 Seventeenth pass (`p812`, 2026-11-13) — the second open-source education ERP gains an agent surface, and LATAM's university systems gain one for the first time

### Frappe Education — reachable with no education-specific code, on a FIRST-PARTY MIT connector

🟢 **This file has said since `p807` that OpenEduCat is the cheapest SIS engagement in this KB
because Odoo has generic connectors. There is now a second, and its connector is better.**

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| **Frappe Education** | https://github.com/frappe/education | 🔴 GPL-3.0 (byte-read `license.txt`, `19 B`) | 709 | Students, programs, enrolment, assessment, fees, on the Frappe framework. `494` forks. 🟢 **Reachable through Frappe Framework's BUILT-IN MCP server (MIT) with no education-specific code** — `13` DocType-generic tools, discovery included. 🔴 Copyleft core: integrate, never derive |
| **Frappe Framework** | https://github.com/frappe/frappe | **MIT** | 11.1k | The substrate. 🟢 **The connector is first-party, reuses the site's REST v2 permissions, labels `update`/`delete` with `destructiveHint: True`, and is OFF until `enable_mcp` is set.** 🔵 **Unlike Odoo, no third-party connector and no "YOLO mode" to grep for** |
| **Frappe LMS** | https://github.com/frappe/lms | 🔴 AGPL-3.0 | 3.4k | Same substrate, same connector, `1,593` forks. 🔴 Network clause — hosted delivery needs legal review |

🔵 **The decision rule, now that there are two.** Odoo/OpenEduCat (`P12`) where the client already
runs Odoo or needs its finance and procurement depth; **Frappe Education (`P29`) where the client
is greenfield or already on Frappe/ERPNext** — because its connector is first-party and MIT, which
removes the third-party-connector risk that `P12` has to manage.

### 🇦🇷🇧🇷 The LATAM university self-management tier — a platform layer this file had never named

🔴 **Every section below assumes Moodle, Canvas, an SIS vendor or a European school portal.** 🟢
**Across Argentina and Brazil the system a student actually logs into is a national or
institutional self-management platform, and `p812` found agent surfaces for three of them.**

| Platform | What institutions run it | Agent surface found this pass | License | Risk posture |
|---|---|---|---|---|
| **SIGAA** (*Sistema Integrado de Gestão de Atividades Acadêmicas*) | 🇧🇷 Brazilian federal and state universities and institutes (UNEMAT, IFSC, UFRPE, UFPA observed) | [`GallegoSz/sigaa-mcp`](https://github.com/GallegoSz/sigaa-mcp) (`13` tools), [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp), [`Pedromaia0/sigaa-mcp`](https://github.com/Pedromaia0/sigaa-mcp), [`EduardoBidese/sigaa-agente`](https://github.com/EduardoBidese/sigaa-agente) | MIT ×4 | 🟢 **read-only by construction** 🔴 **plaintext password in client config; HTML parsing; one student per install** |
| **Sysacad + UTN aula virtual** | 🇦🇷 Universidad Tecnológica Nacional, `18` regionales named | [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) (`12★`, `8` forks) | **ISC** | 🟢 **OAuth server; password never stored; token hashed; session encrypted; preview-then-confirm writes; REFUSES campuses without valid HTTPS** |
| **SIU Guaraní** | 🇦🇷 most Argentine national universities | [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) (Moodle + Guaraní) | **MIT + inherited ISC** | 🟢 **Guaraní read-only — *"Guaraní no tiene API"*, the server reads the G3W pages** 🔴 tested thoroughly only at UNJu |
| **SUAP** | 🇧🇷 Institutos Federais | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) — prepares the teacher's RIT as a **draft** | 🔴 AGPL-3.0 | 🟢 draft-not-submit 🔴 copyleft; the only other SUAP server has no licence |
| **SIAGIE** | 🇵🇪 Peruvian national K-12 | 🔴 **NONE — `25` repositories, zero agents, zero licences** | — | 🔴 **widest open slot found this pass** |
| **SIMAT** | 🇨🇴 Colombian national enrolment | 🔴 **NONE — `total_count=0`** | — | 🔴 hard nil |

🔵 **Scoping consequence, and it is the kind that decides a bid.** A Brazilian or Argentine
university engagement does **not** start at the LMS. It starts at SIGAA, Sysacad or Guaraní —
**none of which publishes an API** (Guaraní's own integrator says so outright), so every path
above is an unofficial parser, scraper or RPA driver against an authenticated session. 🔴 **That
is a contract and data-protection question before it is an architecture one**, exactly as `p810`
concluded for the proprietary national SIS products in EMEA.

## 🟢 Sixteenth pass (`p811`, 2026-11-13) — a whole PLATFORM LAYER this file had never named: the national and regional school portal

🔴 **Every section below this one assumes the institution's system of record is an LMS or an
SIS.** 🟢 **In European state school systems it very often is neither.** What a parent and a
pupil actually log into is a portal operated by a ministry, a federal state or a regional
authority — and `p811` found an agent surface for five of them, all published within five
days of each other, all permissive, all tiny.

| Platform | Operated by | Country | Agent surface found this pass | Licence | Stars |
|---|---|---|---|---|---|
| **Schulportal Hessen (Lanis)** | the federal state of Hesse | 🇩🇪 Germany | [`udondan/lanis`](https://github.com/udondan/lanis) — SDK + CLI + MCP server | MIT | 2 |
| **DSBmobile** | schools via the DSB substitution-plan service | 🇩🇪 Germany | [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) — SDK + CLI + MCP server | MIT | 0 |
| **Admentum** | the Swedish school-platform vendor | 🇸🇪 Sweden | [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) — **read-only**, one item per call | MIT | 0 |
| **iPasen / Séneca** | Junta de Andalucía (regional education authority) | 🇪🇸 Spain | [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) — grades, absences, messages, **confirmed actions** | MIT | 0 |
| **Greek School Network (`sch.gr`)** | the Greek Ministry of Education | 🇬🇷 Greece | [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) — IMAP/SMTP MCP server | MIT | 0 |
| **edu.by site constructor** | the Belarusian national school-web service | 🇧🇾 Belarus | [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) — CLI + MCP + skills, **preview and confirmation before every write** | 🔴 GPL-3.0 | 0 |
| **PRONOTE** (with EduConnect) | Index Éducation; EduConnect is the state identity provider | 🇫🇷 France | [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) — self-hosted MCP connector | 🔴 GPL-3.0-or-later (byte-verified against `NOASSERTION`) | 2 |

🔵 **Why this is a market fact and not a curiosity.** Four of these are operated by a STATE
BODY. That changes who the buyer is (a ministry or a Land, not a university CIO), what the
procurement looks like (public tender), and which regulation binds first (for the EU ones,
Art. 27 FRIA duties fall on PUBLIC deployers). 🟢 **It also answers `ACTION p802-B` from the
supply side:** this base has twice failed to find German classroom deployment STATISTICS,
and has now found German classroom INTEGRATION CODE instead — at the Land level, which is
where `p810` predicted the evidence would sit.

🔴 **Do not mistake any of these for a product.** Every one is `0–2★`, single-maintainer,
self-declared unofficial, and built against an undocumented or semi-documented portal API.
🟢 **What they are worth is the seam**: they prove the integration is possible and they show
which verbs the portal actually exposes, which is normally the expensive unknown in a
public-sector education bid.

🟢 **And one genuinely new system of record, from the same window:**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| **Chalk** | [`usechalk/chalk`](https://github.com/usechalk/chalk) | 🔴 AGPL-3.0 | 2 | **New this pass (`p811`).** *"The open-source **K-12 IT stack**: mixed-fleet device tracking (ChromeOS, Intune, Jamf), help desk, 1:1 lifecycle, **rostering, SSO**, and Google/AD/Entra provisioning **in one Rust binary**. Self-host free, or we host it."* Pushed `2026-11-09`. 🟢 **It is the only artifact in this base that puts rostering and device lifecycle in the same system** — which is what a district IT director actually buys. 🔴 **AGPL-3.0 with a hosted commercial offering: the classic open-core posture, and the network clause rules it out as the base of a hosted deliverable.** 🔵 Read it for the data model of a district IT stack; propose integration, never derivation |


## 🟢 Fifteenth pass (`p810`, 2026-11-13) — three platforms institutions actually run gain an agent surface, and one gains a SECOND at a different risk level

🔵 **This file's premise is that an AI engagement means adding an agent layer to a system the
institution already runs.** 🟢 **`p810` added that layer for three such systems, and for the
first time can offer one platform at two risk postures.**

| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |
|---|---|---|---|---|
| **Sakai** | Higher ed, heavily US/consortium; named `3,937` times in this base — more than any other LMS — and carried **zero** agents until now | [`jtayped/sakai-mcp`](https://github.com/jtayped/sakai-mcp) | `MIT` | 🔴 **WRITE — includes submission on the student's behalf. Gate it** |
| **Sakai** | " | [`sayt25606-rgb/sakai-tasks-mcp`](https://github.com/sayt25606-rgb/sakai-tasks-mcp) | `Apache-2.0` | 🟢 **READ-ONLY and local** |
| **Canvas** | The largest higher-ed LMS in North America | [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) `119★` | `MIT` (byte-verified, blob `5ba93171ff8f`) | 🟢 **Read-only by construction — no write path exists** |
| **Schoology** | US K-12 districts | [`riripatate/schoology-mcp`](https://github.com/riripatate/schoology-mcp) | `MIT` | 🟡 Student-session scope; **no admin API key needed** |
| **Schoology + StudentVUE** | FCPS (one of the largest US districts) | [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | `MIT` | 🟡 Single-district |
| **Schoology + Infinite Campus** | PAUSD | [`dajun666/schoology-mcp`](https://github.com/dajun666/schoology-mcp) | `MIT` | 🟡 🟢 **First Infinite Campus surface in this base** |
| **Cubite LMS** | Vendor-hosted LMS (SCORM, xAPI, certificates, cohorts) | [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp) | `MIT` | 🔴 **`137` tools at the signed-in user's permission level** |

🟢 **The Sakai pair is the genuinely new capability.** 🔵 **Same platform, same week, opposite
postures** — quote the read-only local server to a cautious district and the submission-capable
one only behind a write gate. 🔴 **This base has never before been able to offer that choice on
any LMS**, and it is the single most common objection in an education pilot conversation.

🔴 **`137` tools is a governance object, not a feature.** [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp)
runs at the teacher's own permission level — the same unclaimed risk `p792-D` raised over
[`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)'s `77` tools, **at nearly
twice the surface.** 🟢 **The counter-example now exists and it is in this base:** the Ed-Fi
prototype exposes **six** tools behind a read-only database role (`T28`). 🔵 **Tool count is a
design choice, and the standards body chose six.**

## 🟢 Student information systems — the layer this file has been thinnest on

🟢 **New this pass:** [`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic)
(`LGPL-3.0`, `175★`, `111` forks) — a full academic SIS from **Instituto Superior Técnico,
Lisbon 🇵🇹**: curricular plans, enrolment, degrees, grading, theses. 🟢 **The largest dedicated
open-source SIS in this base, and the only named EMEA-origin institutional system in it.**
🔴 **Dormant since `2023-06-14`** — an architecture reference and a migration source, not a
platform to deploy. 🔴 **LGPL-3.0 is weak copyleft: linking is fine, modifications to the
library itself must be released.**

🔵 **Rostering is the layer BETWEEN the SIS and the LMS, and `p810` added it to
[`repos/foundations.md`](../repos/foundations.md):** OneRoster now has a conformance suite
([`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests),
`Apache-2.0`), an importer ([`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import),
🔴 `GPL-2.0`) and a Go server ([`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster),
`MIT`, 🔴 stale since `2020`). 🔴 **And no agent at all** — a dedicated leg returned an empty
result set. 🟢 **Use the conformance suite as a contractual acceptance gate on any roster
integration**, whoever builds it.

The education equivalent of "Odoo for ERP". These are the systems institutions
already run; an AI engagement almost always means **adding an agent layer to one
of these**, not replacing it. All licenses and star counts verified from the
repository page (2026-11-13, with the LTI and Moodle-MCP rows verified this
pass).

### What changed this pass (thirteenth pass, `p808`, 2026-11-13) — nothing was added, and one licence was independently re-verified

🔴 **Zero new platforms this pass — the vertical leg returned this shelf's own contents
for a NINTH consecutive pass.** `open source platform education ERP CRM MIT Apache`
returned `OpenEduCat`, `Krayin`, `Huly` and `ERPNext`. 🟢 **All four are already held**,
and `p807`'s structural reading of this nil — *every education ERP/CRM in the open is
copyleft, every permissive one is general-purpose* — was **reproduced exactly** by this
window rather than contradicted. `OpenEduCat` `LGPL-3.0`, `ERPNext` `GPL-3.0`,
against `Krayin` `MIT` and `Huly` `Apache-2.0`, both horizontal. 🔵 **A finding that
survives a ninth independent reproduction should now be treated as a property of this
market, not an observation about it.**

🟢 **One licence independently re-verified, and it carries a trap worth recording.**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) was re-read
from its rendered repository page this pass: **`LGPL-3.0`**, **`911★`**, *"Comprehensive
Open Source ERP for Educational Institutes"*. 🟢 **This matches the row below exactly —
nothing changed.** 🔴 **But the GitHub sidebar renders no SPDX licence name for this
repository**; the `LGPL-3.0` appears only in the README body and a badge, and the
search-tier result for it stated **no licence at all**. 🔵 **So an automated licence
scrape of this repository returns EMPTY, not wrong** — and `OpenEduCat` is the single
most load-bearing platform on this shelf (it is the only open-source SIS in this base
with a working agent surface). 🟢 **A future pass that sees a blank licence field here
must not read it as a regression, a relicensing or grounds for rejection.** The LGPL-3.0
obligation on a client deliverable is unchanged: dynamic linking and module-level
separation keep it manageable, modifying its own files does not.

<details>
<summary>Prior pass (<code>p807</code>, twelfth) — a new section, because the saturated vertical leg finally said something</summary>

### What changed at the twelfth pass (`p807`, 2026-11-13)

🟢 **One new section, three new rows, no changes to any existing row:
`## Admissions and enrolment CRM`.** The prescribed vertical-platform leg has now
returned this shelf's own contents **eight passes running**. 🔵 **This pass the nil was
read instead of recorded:** the leg keeps pairing education platforms that are copyleft
with permissive platforms that are not educational, and that pairing is a structural
fact about the market rather than a failure of the query.

🟢 **Consequence: admissions is CRM-shaped work and this base had no CRM.** Added
`krayin/laravel-crm` (**MIT**, `24.1k★` — the largest permissively licensed CRM this base
has found), `cortezaproject/corteza` (**Apache-2.0**, `2.2k★`) and `apache/ofbiz-framework`
(**Apache-2.0**, `1.2k★`, listed with a caution). All three verified from the rendered
repository page this pass.

🔴 **One claim was withdrawn before publication** — Corteza's origin — and the withdrawal
is recorded in the section rather than quietly dropped.

### What changed this pass (eleventh pass, `p806`, 2026-11-13) — two rows, and the second one changes the altitude of every North American engagement

🟢 **`numbas/Numbas` (Apache-2.0, `217★`/`130` forks) is the largest permissively
licensed education platform of EMEA origin this base has found.** Browser-based
e-assessment with an emphasis on mathematics, built by **Newcastle University's School
of Mathematics, Statistics and Physics**. It matters because this file's `T7`-shaped
problem — *the platform layer is copyleft, so the client's host system constrains
everything* — **does not apply to it.** TAO is GPL-2.0; Moodle is GPL; Canvas CE and
Open edX are AGPL-3.0. Numbas is Apache-2.0, which means a studio can fork it, embed it
and ship it.

🔴 **`Ed-Fi` is the bigger finding, and it is an indictment of this base rather than a
discovery.** US K-12 student data does not move school-by-school; it moves through the
**Ed-Fi** standard, which state education agencies run their reporting on. Every pattern
in this KB that touches a student record reaches it through an LMS or through one
institution's SIS — **the wrong altitude for North America.** 🔴 **This base mentioned
Ed-Fi `249` times in its append-only trending logs and `0` times in any file a studio
reads.** It is now shelved in `repos/foundations.md` under a new K-12 data-standard
layer, and summarised in the standards table below.

🔵 **Neither row came from a search.** Both came from a scripted audit of this base
against itself (`scratchpad/p806/propagation-audit.sh`), because the prescribed search
battery returned nil on new platforms for a **seventh consecutive pass** — every
vertical leg returns Moodle, Canvas, Open edX, Sakai, Chamilo, OpenEduCat and RosarioSIS,
which is this file's own contents.

### What changed this pass (tenth pass, `p805`, 2026-11-13) — three SIS rows, none of them new

🔴 **The prescribed search battery returned nil on supply for the third consecutive
pass.** 🟢 **So this pass audited what the base had already verified and never
shelved, and the student-information table was where the damage was.** Three
systems — `Gego-K12/gegok12` (**MIT**), `SVWS-NRW/SVWS-Server` (**BSD-3-Clause**)
and `portabilis/i-educar` (**GPL-2.0**) — were license-verified in earlier passes,
recorded in the append-only trending log, and **written to no shelf file at all**.
One of them had been described in that log as already being on this shelf. All
three were re-verified live before being added below.

### Unresolved this pass (ninth pass, `p804`, 2026-11-13) — an informed gap, not a finding

🔴 **The Open edX stewardship and licence question was raised this pass and could not
be closed.** The LMS search leg returned vendor comparisons asserting, variously, that
Open edX is **AGPL**, that it is stewarded by **Axim Collaborative** (a nonprofit
founded by Harvard and MIT), and — in one case — that Canvas's community edition is
**ECL-2.0** rather than AGPL-3.0. 🔴 **`openedx.org` does not resolve from this session
(`getaddrinfo ENOTFOUND`, outside the allowed network domains), so none of it could be
verified at the source.**

🟢 **Nothing in the table below was changed on the strength of it.** The Open edX and
Canvas rows retain the grants this file verified from the repository page in earlier
passes. 🔵 **Recorded here because a vendor blog disagreeing with a verified row is
exactly the kind of noise that becomes wrong data if a later pass reads it without the
context that it was checked and rejected.** `ACTION p804-V` tracks re-verification of
the stewardship claim when the host is reachable.

</details>

## The decision that governs every education engagement

**Do not fork the LMS — but the "no permissive LMS exists" half of that rule is
withdrawn this pass.** 🔴 **Correction (sixth pass, 2026-11-13):** every earlier
edition of this file said *"only Sakai is permissive, ECL-2.0."* That is wrong.
**OpenOLAT is Apache-2.0** — read verbatim from the repository's `LICENSE` file,
which opens *"Apache License / Version 2.0, January 2004"* — and it is a mature
platform (32,338 commits, 451 stars, 165 forks, Java), not a toy. GitHub's
sidebar shows only a generic "License" link and the org listing renders it as
**"Other"**, which is exactly why four passes of license-field reads missed it.
**There are two permissive LMS platforms, not one**, and the second one is the
more interesting of the pair because of what it ships natively (below).

The rest of the rule stands: six of the eight significant open-source LMS
platforms are GPL-3.0 or AGPL-3.0. A fork
makes the client's derived platform copyleft. Instead mount the AI layer as an
**LTI 1.3 tool** or an **MCP server** against the platform's API, keep that
layer MIT/Apache, and emit **xAPI** or **Caliper** events so the institution can
report on it. Every pattern in `compose/patterns.md` follows this shape.

**Update (fifth pass, 2026-11-13): there is now a third mounting surface, and it
is the one that reaches the student record.** Where the incumbent system is built
on a **general-purpose platform**, the agent surface may already exist as a
*platform* connector rather than an education one. **OpenEduCat is Odoo addons,
and Odoo has two mature MCP servers whose tools take the model name as a
parameter** — so the leading open-source education ERP is agent-reachable today
with no education-specific code. See the SIS table below. 🔵 **The general rule
to carry into any engagement: before concluding a platform has no agent surface,
check the platform it is *built on*.**

**Both halves of that sentence now have verified implementations.** LTI 1.3:
`Cvmcosta/ltijs` (Apache-2.0, 373 stars, full LTI Advantage). MCP: Canvas via
`canvas-mcp` (MIT, 324) and — new this pass — **Moodle via `Faixiang/Moodle-MCP`
(MIT, 206)**. The previous edition of this file said Moodle had no significant
MCP server. It does.

## Learning management — the host systems

| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |
|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.6k | Global, strongest in EMEA, LATAM, APAC public education | Mature plugin API; LTI 1.3; web services REST API. **MCP now available: `Faixiang/Moodle-MCP` (MIT, 206) read-only; `falkenslab/moodle-mcp` (MIT) ~260 tools via browser SSO; `MarcosNahuel/moodle-mcp` (MIT) idempotent content publishing** |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | MOOCs, corporate academies, national platforms | **`openedx-ai-extensions`** is the official AI plugin point; XBlocks; deploy via `tutor`. MCP only via `openedx-mcp` (AGPL-3.0, 3 stars) |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | North American higher ed (dominant) | Rich REST API + LTI 1.3; **`canvas-mcp` (MIT, 324) — README claims up to 128 tools, sidebar says 102** |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 | 3.4k | SMB/corporate training, India | Frappe framework hooks; shares a stack with ERPNext |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Research universities | **Permissive license** — a platform a studio can extend without copyleft reaching the product. `Simon-Initiative/lti_1p3` (MIT, Elixir) comes from adjacent higher-ed work |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | 451 | **German-speaking EMEA** — Swiss and German universities, vocational and public sector. Origin: OLAT at the University of Zurich; maintained by **frentix GmbH** (Switzerland) and the community | 🟢 **New this pass, and it changes the EMEA answer. The only LMS in this table that ships a first-party, provider-pluggable AI layer in-tree** — you do not have to mount an agent to get AI into it. `org/olat/core/commons/services/ai/` defines an SPI (`AiSPI`, `AiEmbeddingSPI`, `AiApiKeySPI`) with **four provider implementations: `anthropic`, `generic` (any OpenAI-compatible endpoint), `localonnx`, `openAI`**. Five features are declared in the `AiFeature` enum — `mc-question-generator`, `image-description-generator`, `essay-generation`, `essay-grading`, `taxonomy-matching` — of which two are user-controlled (a learner can switch them off over the admin default). Ships `AiUsageLog` (per-call token/cost accounting) and `AiUserPreference`. **Apache-2.0 + `generic` provider = point the whole thing at a self-hosted vLLM and nothing leaves the institution.** See `compose/patterns.md` `P13` |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LATAM, francophone Africa, Spain | Web services API; accessibility-first. PHP — pair with `packbackbooks/lti-1-3-php-library` (Apache-2.0) |
| ILIAS | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | German-speaking EMEA, vocational and public sector | Plugin slots; SCORM/xAPI |

## The integration layer — build once, mount everywhere

| Library | Repo | License | Stars | Use when |
|---|---|---|---|---|
| ltijs | https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | Default choice. Node.js, full LTI Advantage (launches, Deep Linking, AGS, NRPS, Dynamic Registration) |
| lti-1-3-php-library | https://github.com/packbackbooks/lti-1-3-php-library | Apache-2.0 | 54 | The client is a PHP shop (Moodle, Chamilo); roster via NRPS, grade writeback via AGS |
| lti_1p3 | https://github.com/Simon-Initiative/lti_1p3 | MIT | 16 | Elixir stack, or you need to act as **Platform** as well as Tool |
| lti-tool | https://github.com/lti-tool/lti-tool | MIT | 8 | Serverless target (Lambda, Cloudflare Workers); early but the only one of its shape |

## Student information systems and institutional ERP

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | **SIS + LMS + finance as Odoo modules** — the literal "Odoo for education", and **the only open-source SIS with a working agent surface (new finding, fifth pass)**. 789 forks; branch/tag `19.0`; modules `openeducat_core`, `_admission`, `_exam`, `_fees`, `_attendance`, `_timetable`, `_parent`, `_library`, `_activity`, `_assignment`, `_classroom`, `_facility`. **Because it is Odoo addons, it is reachable by a generic Odoo MCP server** — `erpipe-org/mcp-odoo` (MIT, 433★, three-call gated writes) or `ivnvxd/mcp-server-odoo` (MPL-2.0, 415★, per-model allowlist in a companion module) — so `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` need no new connector. 🔴 **Architecturally verified, not yet run against a live instance (`Gap 286`).** If the client already runs Odoo this is now the shortest path **by a wide margin**. |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 707 | **New this pass.** Admissions, fees, scheduling, exams, attendance on the Frappe framework. **The one-framework play: pair with `frappe/lms` (AGPL-3.0) and ERPNext for SIS + LMS + ERP on a single stack** — but the two halves carry *different* licenses (GPL-3.0 vs AGPL-3.0), which matters the moment anything is network-served. License read from `license.txt`, not GitHub's sidebar. Strong India/SMB footprint. |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | K-12 school management; widely deployed in LATAM, Spanish/French/Portuguese localization in core. |
| Gibbon | https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible school management; strong in international K-12 schools. |
| openSIS Classic | https://github.com/OS4ED/openSIS-Classic | GPL (README) | 351 | Student information system; commercial editions available from OS4ED. |
| **GegoK12** | **https://github.com/Gego-K12/gegok12** | **MIT** | 56 | 🟢 **The first genuinely MIT school ERP/SIS in this base, and this pass is the one that put it on the shelf.** Laravel/PHP 8.4+, 123 commits, API-first with a mobile app. Covers student management, attendance, timetables and fees. 🔴 **The licence had to be read from the file: GitHub's classifier returns `NOASSERTION` because the `1,150 B` grant carries `<!-- SPDX-License-Identifier: MIT -->` on line 3 and curly quotes in the operative text.** Confirmed first-hand this pass — the file opens `MIT License`, SPDX `MIT`, *"Copyright (c) 2025 GegoSoft Technologies and GegoK12 Contributors."* 🔵 **Region: APAC** — `.env.example` ships `TIMEZONE = 'Asia/Kolkata'` and `config/app.php` resolves from it, which is a stronger placement signal than an owner profile because a deployer inherits it without choosing it. 🔴 **56 stars: this is a real but small project.** Vendor pages also market a cloud edition, so read the repo, not the marketing. |
| **SVWS-NRW** | **https://github.com/SVWS-NRW/SVWS-Server** | **BSD-3-Clause** | 42 | 🟢 **A state-government school-administration server, permissively licensed — new to this shelf this pass.** *Schulverwaltungssoftware Nordrhein-Westfalen*: the SIS the German state of **North Rhine-Westphalia** builds for its own schools, Java + TypeScript, **10,015 commits**. 🔵 **Region: EMEA.** 🔴 **The index reads `NOASSERTION`; BSD-3-Clause is stated in the README** (*"lizenziert unter der BSD 3-Clause Lizenz"*). 🟢 **Engagement reading: commit count says this is a maintained production system, not a pilot, and a BSD-3 grant on public-sector education software is rare enough to be the reason to look at EMEA public K-12 at all.** German-language domain model — budget for that, not for the licence. |
| **i-educar** | **https://github.com/portabilis/i-educar** | **GPL-2.0** | 725 | 🟢 **The largest free-software school-management system in Brazil, and the most-starred SIS in this table.** PHP/Laravel, **34,951 commits** on branch `2.12`, 555 forks; first built by the Itajaí (SC) city government and now deployed by municipalities across Brazil. 🔵 **Region: LATAM.** 🔴 **GPL-2.0 — copyleft, so this is a system a client self-hosts and you extend, not a tree a studio derives a product from.** Companion `i-diario` (AGPL-3.0) is the class-diary/attendance-and-grades surface from the same vendor. 🔴 **Correction recorded this pass: the trending log has claimed since `p667` that this row was "carried on the verticals shelf", and it was not — it had never been written to any shelf file.** |

🔴 **Agent surface across the SIS row, stated plainly because it decides which
client you can serve this quarter.** **OpenEduCat: yes**, via the Odoo
connectors above. **Frappe Education and Frappe LMS: unknown and worth one
search** — they sit on the Frappe framework, which is the next place to look for
the same generic-connector trick, and nobody has checked. **RosarioSIS
(PHP/Postgres) and Gibbon (PHP/MySQL): no agent interface and no generic
connector of the Odoo kind** — searched by project name this pass, nothing
returned. Those two are the genuinely unserved incumbents, and they are
precisely the ones that dominate **LATAM K-12** (RosarioSIS) and
**international K-12** (Gibbon). 🔴 **Amended this pass: naming
RosarioSIS as what dominates LATAM K-12 understated the field — `portabilis/i-educar`
is larger by stars, forks and commits and is deployed by Brazilian municipalities,
and it had never been written to this shelf.** 🔵 **Engagement reading: a LATAM K-12 client on
RosarioSIS is a build; a private-education or India/LATAM SMB client on
OpenEduCat is a configuration.**

🟢 **The licence picture of this table changed this pass, and it is the most
consequential thing on this page.** Every SIS row above used to be copyleft —
LGPL-3.0, GPL-3.0, GPL-2.0 — which meant the standing advice was *integrate,
never derive*. **`GegoK12` is MIT and `SVWS-NRW` is BSD-3-Clause.** Both are
small next to OpenEduCat or i-educar, so this is not a recommendation to replace
them; it is the first time a studio has **a permissive SIS tree it can actually
fork and ship** when the engagement calls for a product rather than an
integration. 🔵 **Placed: `GegoK12` → APAC, `SVWS-NRW` → EMEA, `i-educar` →
LATAM, OpenEduCat → APAC/LATAM SMB, RosarioSIS → LATAM, Canvas/Open edX →
North America.** 🔴 **Both permissive rows are under 60 stars; verify
maintenance before committing a client to either.**

## Open-core platforms — a real MIT grant over a commercial system of record (new, `p809`)

🔴 **Read this section before quoting any ibl.ai repository to a client.** The estate is
genuinely `MIT` — every payload below was fetched and hashed this pass — **and every
application in it is a front-end client whose backend is not in the repository and is
sold under an enterprise licence.** Both halves of that sentence are true at once, and
this base has twice come close to publishing only the first half.

| Platform | Repo | License (payload-verified) | Stars | What you actually get | What you do NOT get |
|---|---|---|---|---|---|
| ibl.ai SIS | https://github.com/iblai/sis | MIT (`1,089 B`, `969b7073d1c42ac2`) | 1 | Next.js 16 + Tauri 2 student information **front end**: students/staff directory, enrolment, grades & GPA, credentials, guardians, course runs, rosters, gradebook, terms/periods/rooms, reports, messaging, ⌘K palette. **4 languages** (en/es/fr/zh), native shells for macOS/Windows/Linux/iOS/Android. | 🔴 The system of record. README: *"a front end for the ibl.ai platform"*; *"If you need the full backend, reach out at ibl.ai/contact for an enterprise license."* Writes **no backend endpoints of its own**; sign-in goes to `login.iblai.app`; requires ibl.ai Data Manager + Open edX with ibl plugins + Studio. |
| ibl.ai LMS | https://github.com/iblai/lms | MIT (`1,063 B`, `f1269b7b2313456a`) | 95 | Skills-intelligence learning platform: course discovery, **skill-growth tracking, digital credentials, learning paths**, admin analytics, multi-tenant branding. `1,071` commits. 🟢 The closest open artefact in this base to the skills-first direction `T23` describes. | 🔴 README: *"To use this app, you need access to an ibl.ai backend instance"* — skills/course API, EdX delivery, auth, data platform, optional AI-mentor API. |
| ibl.ai OS | https://github.com/iblai/os | MIT (`1,070 B`, `13029f084e13d864`) | **638** | Agent platform: institution-defined agents bound to their own documents, multi-provider routing, voice, analytics, SSO, embeddable widgets. | 🔴 README: *"requires the ibl.ai backend platform for authentication, AI agent APIs, and data services"*, *"not included in this repository"*. |
| ibl.ai Ontology | https://github.com/iblai/ontology | MIT (`1,063 B`, `f1269b7b2313456a`) | 12 | 🟢 **The one piece of the estate that stands alone.** On-premise knowledge layer making **PeopleSoft, Snowflake, Canvas and Salesforce** queryable by agents **over MCP** — *"no data extraction, your data stays in your network"*. `97` commits. | — |

🔴 **Star correction carried into this file: `iblai/os` is `638★`. This base published
`821★`.** Measured from the rendered page, 2026-11-13.

🟢 **How to use this honestly in an engagement.** These are high-quality front ends under
a permissive grant — forking and white-labelling `sis` or `lms` is legitimate and fast.
🔴 **But the SIS gap in this base does not close here**, because the record these clients
display lives in a proprietary backend. If the client needs to own the system of record,
the open paths remain OpenEduCat-on-Odoo (LGPL-3.0 addons + `MIT`/`MPL-2.0` Odoo MCP
servers), or building on Frappe. Say which one you mean.

## Brightspace and Blackboard — the two incumbents this file had no agent surface for (new, `p809`)

🔴 **Both platforms were named repeatedly across this KB and carried zero connector
rows.** Corrected this pass. Neither vendor publishes an MCP server of its own (checked
2026-11-13), so **every path below is unofficial** — REST API, SSO session, or scraped
cookie — which is a contract question before it is an architecture one.

| Platform | Incumbent where | Open agent surface found | License | Stars |
|---|---|---|---|---|
| **D2L Brightspace** | Canadian & US higher ed, Dutch, Singaporean, Colombian institutions | https://github.com/RohanMuppa/brightspace-mcp-server — `29` tools, **read-only by declaration**, SSO + 2FA, OS keychain, AES-256-GCM session state | MIT | 67 |
| **D2L Brightspace** | — | https://github.com/JhostinAleck/brightspace-mcp — `29` tools (`26` read / `3` write), **two-opt-in write gate + `dry_run` + idempotency key + audit log**, 4 auth strategies, `es-419` locale | MIT | 16 |
| **Blackboard Learn** | LATAM private universities (UPC, UPN — Peru) | https://github.com/alejooroncoy/campus-cli — CLI **and** MCP server, `851` commits. 🔴 **Tools are brokered by a remote relay (`mcp.campuscli.com`)**: credentials cross a third party | ISC | 13 |
| **Blackboard Learn** | APAC (NTU Singapore) | https://github.com/kingdonkatsu/ntulearn-mcp — `8` tools. 🔴 Auth is a **`BbRouter` session cookie auto-read from the browser** | MIT | 4 |
| **Blackboard Learn (Ultra)** | Vendor-neutral | https://github.com/Mattlo0546/blackboard-mcp — read-only, university SSO, Python. 🔴 **`4` commits — reference only** | MIT | 1 |

## Admissions and enrolment CRM — where the permissive option is general-purpose, not educational

🟢 **New section at the twelfth pass (`p807`, 2026-11-13).** The prescribed
vertical-platform leg (`open source platform education ERP CRM MIT Apache`) has returned
this shelf's own contents for **eight consecutive passes**. 🔵 **This pass it returned
them again — but the shape of the nil is itself the finding, and it had never been
written down.**

🔴 **The structural fact: every education-specific ERP/CRM in the open is copyleft, and
every permissive ERP/CRM is general-purpose.** There is no MIT or Apache-2.0 system in
existence that ships an *education* admissions pipeline. The leg confirms it from the
other direction each time it runs — `OpenEduCat` (LGPL-3.0), `Frappe Education`
(GPL-3.0), `ERPNext` (GPL-3.0) on the education side; `Apache OFBiz`, `Corteza`,
`Krayin`, `Huly`, `iDURAR` on the permissive side, none of them educational.

🔵 **Why this matters more than it sounds.** Admissions and enrolment is **CRM-shaped
work, not SIS-shaped work** — pipelines, stages, campaigns, attribution, nurture — and a
studio that reaches for the SIS table above to serve it is reaching for the wrong tool
and inheriting copyleft for no reason. 🟢 **The correct move is a permissive general CRM
with an education domain model built on top**, which is a configuration exercise plus an
agent, not a platform build.

| Platform | Repo | License | Stars | Why it is the right base for education admissions |
|---|---|---|---|---|
| **Krayin CRM** | https://github.com/krayin/laravel-crm | **MIT** | 24.1k | 🟢 **The largest permissively licensed CRM this base has found, by a wide margin — `24.1k★`, `1.7k` forks.** Laravel/PHP, built for lead, customer and sales management; the lead→opportunity→stage model maps onto enquiry→application→offer→enrolment with no structural violence. 🔵 **MIT means a studio can fork it and ship an admissions product**, which is impossible anywhere on the SIS table except `GegoK12` (`56★`). 🔴 **Nothing in it is education-aware** — no applicant, programme, intake or qualification entity — so budget the domain model as net-new. 🟢 **Shares a stack with `i-educar` (PHP/Laravel), which makes a LATAM pairing unusually cheap.** |
| **Corteza** | https://github.com/cortezaproject/corteza | **Apache-2.0** | 2.2k | 🟢 **Low-code platform for data-driven business apps and workflows — Apache-2.0, `532` forks, not archived.** Where Krayin gives a CRM to bend, Corteza gives a **modeller**: define the admissions entities and the workflow, rather than inherit a sales one. 🔵 **The better choice when the institution's process is unusual** (multi-intake, competitive programmes, ministry reporting) and the worse choice when it is ordinary. 🟡 Materially smaller community than Krayin — read the release cadence before committing. |
| **Apache OFBiz** | https://github.com/apache/ofbiz-framework | **Apache-2.0** | 1.2k | 🟡 **Listed for completeness and with a caution.** Java enterprise automation spanning ERP, CRM, e-commerce, SCM and manufacturing, `764` forks. 🔴 **Its breadth is the problem, not the attraction** — an admissions pipeline uses a thin slice and pays the whole framework's learning curve. Reach for it only where the client already runs OFBiz. |

🔴 **Agent surface: none of the three ships one, and no MCP server for any of them was
found this pass.** 🟢 **That is a smaller obstacle here than on the SIS table**: all three
are API-first with conventional REST/GraphQL surfaces, so an MCP wrapper over an
admissions subset is days of work, not a connector project. See `compose/patterns.md`
`P21`.

🔵 **Placement, and one correction made before this page was written.** `Krayin`'s GitHub
organisation states its location as **India** → 🟢 **APAC-origin**, though the product is
deployment-neutral. 🔴 **`Corteza` was drafted here as "EMEA-origin (Slovenia)" from
recollection and that claim was withdrawn on checking:** the `cortezaproject` organisation
states its location as **"International"**, and `cortezaproject.org` is outside this
session's allowed network domains, so **no origin is asserted** → `Gap 807-D`. `OFBiz` is
an ASF project with no regional centre. 🟢 **None of the three carries a regional
constraint — unlike the SIS table, where the incumbent decides the region for you.**

## Content, delivery and classroom

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| Kolibri | https://github.com/learningequality/kolibri | **MIT** | 1.2k | Offline-first learning platform. The right base for low-connectivity deployments (rural LATAM, Sub-Saharan Africa, remote APAC). Permissive. |
| Oppia | https://github.com/oppia/oppia | **Apache-2.0** | 7.0k | Interactive lesson "explorations" with built-in misconception handling. Permissive and substantial. |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | The de facto interactive-content format; renders inside Moodle, Canvas, Open edX. |
| Khan Perseus | https://github.com/Khan/perseus | **MIT** | 1.6k | Khan Academy's exercise editor/renderer. MIT — drop real exercise rendering into any product. |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Virtual classroom with LTI into Moodle/Canvas; recordings feed transcript pipelines. |
| Opencast | https://github.com/opencast/opencast | ECL-2.0 | 511 | Lecture capture at scale — the upstream source for transcript/summarization agents. |
| Anki | https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition scheduling; the algorithm is the asset for retention features. |

## Teaching, grading and learning-data infrastructure

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| JupyterHub | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user notebooks; the standard for CS/data-science teaching. |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assignment release and autograding for notebooks. **The grading substrate to wrap an agent around.** |
| pyKT | https://github.com/pykt-team/pykt-toolkit | **MIT** | 461 | Deep knowledge-tracing benchmarks — real mastery estimation to pair with an LLM tutor. |
| ODK Collect | https://github.com/getodk/collect | Apache-2.0 | 805 | Offline Android form collection; used for education field assessment at national scale. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (README) | 2 | Essay scoring + label-aware feedback, locally deployable. Prototype scale, but the only open grading *system* found. |
| Numbas | https://github.com/numbas/Numbas | **Apache-2.0** | 217 | **New this pass (`p806`) — the largest permissively licensed education platform of EMEA origin in this base.** *"A completely browser-based e-assessment/e-learning system, with an emphasis on mathematics."* Built by **Newcastle University** (UK). This repo is the standalone **Python 3 compiler**; the authoring editor is `numbas/editor` in the same org. `130` forks. 🟢 **Apache-2.0 is the whole point of the row:** TAO is GPL-2.0 and every LMS in the table above is GPL or AGPL, so Numbas is the only assessment platform here a studio can fork, embed and ship inside a proprietary client deliverable. 🔵 Strongest fit is STEM formative assessment, where its maths-expression engine and randomised question generation are the differentiator — **not** a general item bank; pair with the QTI 3 player for interchange. 🔴 Promoted by audit — `39` mentions in the trending logs, never shelved. |
| TAO | https://github.com/oat-sa/tao-core | GPL-2.0 | 64 | **New this pass — the one assessment *platform* with real item banking that a client may already be running.** Long-standing open e-testing system. 🔴 **Two constraints decide whether it fits: the open-source edition is QTI 2.2-based, not QTI 3, and it ships no Results Management** — a QTI 3 contract or a reporting requirement lands outside it. GPL-2.0: a host to extend, not a base to embed. |
| QTI 3 item player | https://github.com/amp-up-io/qti3-item-player | **MIT** | 30 | **New this pass — the delivery surface for assessment, and the only QTI repo claiming conformance certification** (QTI 3 Basic *and* Advanced "Delivery"). 🔴 Vue 2.6, which is end-of-life. Pair with `LongsightGroup/qti3` (MIT) for authoring, scoring and migration — **no single repo does both**. |
| Caliper spec | https://github.com/1edtech/caliper-spec | IMS spec-document license | 22 | Learning analytics event spec. Implement it; do not vendor the repo. **Implementations now exist — see the two rows below and `repos/foundations.md`.** |
| caliper-ts | https://github.com/CarnegieLearningWeb/caliper-ts | **MIT** (read from `LICENSE`; sidebar shows only a generic link) | 0 | **New this pass — the only permissively licensed Caliper sensor found anywhere.** TypeScript Sensor API, Caliper **1.1**. 🔴 Published to the **GitHub Package Registry** as `@imaginelearning/caliper-ts`, not public npm, and 0 stars — budget to carry it. |
| Moodle Caliper logstore | https://github.com/open-lms-open-source/moodle-logstore_caliper | GPL-3.0 | 1 | **New this pass — the only Caliper emitter for a real LMS, at any licence.** Moodle logstore plugin: Expander → Translator → Emitter, immediate or batched, Moodle **2.7+**. 🟢 GPL-3.0 is correct for a Moodle plugin and does **not** reach a separately deployed MIT/Apache AI layer. |

## Standards that make the above interchangeable

| Standard | Why it decides the architecture |
|---|---|
| **LTI 1.3 / LTI Advantage** | Build the AI tool once as an LTI tool provider and it mounts in Moodle, Canvas, Open edX, Sakai, and ILIAS. Highest-leverage single investment in an education engagement — and `ltijs` means you do not write it from scratch. |
| **Ed-Fi** 🆕 | 🔴 **The standard this base missed for eleven passes.** The US K-12 data-interoperability model that **state education agencies** run their reporting on. It decides the architecture of any North American K-12 engagement, because an agent that speaks Ed-Fi reaches a *state*, not a school — while an agent that speaks one SIS reaches one district. 🟢 **Permissively implemented and deployable today:** `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` (Apache-2.0, v7.x) and `Ed-Fi-Alliance-OSS/Data-Management-Service` (Apache-2.0, **v8 — build against this one**). 🔴 **There is no Ed-Fi MCP server anywhere in this base and none was found: the agent edge is unbuilt (`Gap 806-A`), and it is a build that must be priced as one.** Region: **North America**. |
| **xAPI** | Learner-activity telemetry; what an agent should emit so the institution can report on it. |
| **Caliper Analytics** | The 1EdTech-native alternative to xAPI; common in North American higher ed. **Updated fifth pass: six implementations now verified — an MIT sensor, a GPL-3.0 Moodle emitter, an Apache-2.0 analysis layer and LGPL-3.0 reference sensors — but NO permissively licensed event store, and 1EdTech's reference code is member-gated.** Free choice → still xAPI. Contract names Caliper → you write the store and nothing else. Ask which Caliper **version**: the only 1.2 implementation found is unlicensed. |
| **QTI** | Assessment item interchange — matters as soon as item banks must move between systems. **Updated fifth pass: seven implementations verified, five of them MIT — but scoring, item banking and *certified delivery* live in different repos, so every QTI engagement is a pairing exercise.** `qti3-item-player` (MIT) is certified delivery-only; `LongsightGroup/qti3` (MIT) authors, scores and migrates but claims no certification. 🔴 Confirm which **branch** a QTI licence was read from: `Learnosity/learnosity-qti` is MIT on `master` and GPL-2.0 on its default `develop`. |
| **SCORM** | Legacy but ubiquitous in corporate and vocational training; still the delivery format many EMEA/APAC clients require. |

## Declared gaps

- 🔴 **`Gap 806-A` — no Ed-Fi agent interface exists, and this is the best-shaped
  contribution opportunity in this file.** Ed-Fi is Apache-2.0, exposes a conventional
  REST API with a published specification, and reaches US state education agencies
  rather than single districts. Every ingredient for an MCP server over it is already
  on a shelf in this KB: the spec, the Apache-2.0 reference implementation, and **three
  independent MIT write-gating designs** to copy from `agents/top.md`
  (`che-ntucool-mcp`'s elicitation-plus-single-use-token, `waseda-moodle-mcp`'s
  `prepare_*`/`confirm_action` split, `Smartschool-MCP`'s read-only posture). 🔵 **The
  gating design is not optional here** — a write path into a state longitudinal data
  system is the highest-consequence write surface in this entire knowledge base.

- **No permissively licensed LMS at deployment scale** except Sakai. Surface
  this constraint in week one of any engagement that needs a proprietary
  derived platform.
- **MCP coverage is no longer absent for Moodle — it is fragmented.** Seven
  Moodle MCP servers verified, 1–206 stars, licenses split MIT/GPL/AGPL, and no
  two agree on tool surface or auth model (web-service token vs interactive
  browser SSO vs companion plugin). Canvas, by contrast, has consolidated on
  one 324-star MIT server. **Open edX remains the real gap**: `openedx-mcp`
  (AGPL-3.0, 3 stars) is the only option and it is reference-grade at best.
- 🟢 **SIS MCP: CLOSED for OpenEduCat, corrected again 2026-11-13 (fifth
  pass).** The fourth-pass correction below said SIS servers exist "but not for
  any SIS in this table." **That is now withdrawn too.** OpenEduCat **is in this
  table** and is reachable by a generic Odoo MCP server (`erpipe-org/mcp-odoo`,
  MIT, 433★; `ivnvxd/mcp-server-odoo`, MPL-2.0, 415★), because it is Odoo addons
  and those servers address models by name. 🔴 **Architecturally verified, not
  run (`Gap 286`).** What stays true: **RosarioSIS and Gibbon have neither an
  agent interface nor a generic connector** — they are the unserved rows, and
  they are the LATAM K-12 and international K-12 incumbents respectively.
  🔵 **The method worth institutionalising: when a vertical system has no agent
  surface, check the general-purpose platform underneath it.**
- **SIS MCP servers exist — but not for any SIS in this table. Superseded by the
  bullet above; kept for the record (fourth pass).** The previous three editions of this file said "no
  MCP server for any SIS" and called it a confirmed absence. That claim was
  **over-generalized and is now withdrawn.** Two verified MCP servers do reach a
  student information system: `oliverhruby/edupage-mcp` (MIT, 4 stars, **31
  tools**) over **EduPage**, the SIS used across Slovakia and Czechia, and
  `sukhrobyangibaev/mcp_hemis_student` (MIT, 0 stars) over **HEMIS**, the
  higher-education SIS used by Uzbek universities. **What remains true, and is
  the sharper statement:** OpenEduCat, RosarioSIS, Gibbon, openSIS and
  `frappe/education` — every *open-source* SIS in this table — still have **no**
  agent interface. The integration is happening against **national proprietary
  SIS products with captive markets**, built by individual developers, not
  against the open-source platforms a studio would deploy. Two consequences for
  an engagement: the topology is proven (so `P8` is no longer greenfield), and
  **EduPage's server reaches the SIS through a community library on undocumented
  endpoints** — a pattern to learn from, not a dependency to ship.
- **The learning-record store, by contrast, is now solved and permissive.** New
  this pass: `yetanalytics/lrsql` (Apache-2.0, 144) and `openfun/ralph` (MIT,
  51) as LRS implementations, with `DavidLMS/learnmcp-xapi` (MIT, 16) as the
  agent interface. **An LRS is not an SIS** — it holds learning *activity*, not
  the student record — so this closes the telemetry gap and leaves the advising
  gap exactly where it was.
