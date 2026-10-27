---
industry: education
region: Global
updated: 2026-10-27
---

## 🆕 `p485` — `2026-10-27` — **🟢 A FOUNDATION THIS SHELF HAS NEVER LISTED, AND IT IS THE MOST DEPLOYED EDUCATION CODEBASE IN LATIN AMERICA: `portabilis/i-educar` — 721★ against **552 forks**, GPL-2.0, PHP/Laravel, with a module that files Brazil's national school census. 🔴 Its sibling `i-diario` fails this shelf's licence bar for a reason no prior instrument could detect.**

🔵 This shelf's test is whether a repository is something **others build on**. Fork-to-star ratio is
the cheapest honest proxy for that, and this pass applied it to the LATAM supply that
[`intel/market.md`](../intel/market.md) surfaced for the first time. Licences are **bytes**; census in
[`latam-supply-census`](../evidence/latam-supply-census.2026-10-27-p485.tsv).

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted**; nothing gate-attested.

### 🟢 Why `i-educar` belongs on the foundations shelf

| foundation property | evidence |
|---|---|
| **fork-to-star ratio** | **552 forks / 721 stars = 0.77** — extraordinarily high. Compare DeepTutor at 5 724/45 506 = **0.13**. Stars measure attention; forks at this ratio measure **people standing up their own instance**. |
| extension mechanism | A published **package** architecture, not a monolith: `i-educar-reports-package` (35★, JasperReports), `i-educar-transport-package` (14★), `i-educar-library-package` (13★), `i-educar-educacenso-package` (3★). Third parties ship modules against it. |
| **statutory integration** | `i-educar-educacenso-package` files **Educacenso**, Brazil's national school census. A codebase wired into a country's statutory reporting is infrastructure, not an app. |
| institutional framing | Self-described *"o maior software livre de educação do Brasil"*, tagged **`software-publico`** — Brazil's public-software designation. |
| companion products | `i-diario` (117★/62 forks, Ruby/Rails teacher gradebook), `i-diario-app` (29★/23 forks, **offline** attendance capture), `pre-matricula-digital` (21★/10 forks, enrolment + waitlists). |
| longevity | Created **2013-01-31**, pushed **2026-10-27** — thirteen years live, active today. |
| 🔴 no AI surface | Nothing. No `ai`, `llm` or `mcp` module in the package set. 🟢 **That is the opportunity, not a defect.** |

🟡 **The ratio is read as deployment and that is an inference** (`Gap 485-K`): 552 forks is consistent
with municipalities self-hosting, but no instance was probed and no municipality named.

### 🔴 The licence split inside one organisation — and the new instrument it needed

🔴 The `portabilis` repositories **do not share a licence**, and the difference decides whether
Globant can touch them:

| repository | licence from bytes | B | `sha12` | shelf verdict |
|---|---|---|---|---|
| `portabilis/i-educar` | 🟡 **GPL-2.0** *Version 2* | 18 091 | `f9c375a1be4a` | 🟢 **admitted** — copyleft, usable over an API boundary |
| `portabilis/i-educar-reports-package` | 🟡 GPL-2.0 | 18 091 | `f9c375a1be4a` | 🟢 admitted |
| `portabilis/i-educar-transport-package` | 🟡 GPL-2.0 | 18 091 | `f9c375a1be4a` | 🟢 admitted |
| `portabilis/i-diario` | 🔴 **AGPL-3.0 in Portuguese translation** | 35 325 | `837b5cf19787` | 🔴 **grant unresolved** |
| `portabilis/i-diario-app` | 🔴 AGPL-3.0 **translated** | 35 325 | `837b5cf19787` | 🔴 grant unresolved |
| `portabilis/pre-matricula-digital` | 🔴 AGPL-3.0 **translated** | 35 325 | `837b5cf19787` | 🔴 grant unresolved |

🔴 **The three AGPL files contain zero English licence text** — the string
`GNU AFFERO GENERAL PUBLIC LICENSE` occurs **0 times**. The FSF holds its translations unofficial and
not legally operative, so the grant is, strictly read, undefined. Full treatment on
[`agents/top.md`](../agents/top.md).

🟢 **The instrument lesson is the transferable part.** This base already graded licences on
*deviation from canonical* (`p484`) and on *version* (`p455`). **Neither detects a change of
language** — a translated AGPL has no byte overlap with the canonical text, so a deviation counter
reports noise and a version reader finds "Versão 3" and moves on. A **language axis** is now required
and is declared as `Gap 485-S`.

### 🟡 `Gap 484-T` paid a dividend to this shelf too

🟢 `uPortal-project/uPortal` is **Apache-2.0, 11 358 B, byte-identical to the `apache.org` canonical
text — 0 deviations**. 🔵 That makes it the **cleanest permissive foundation** on this shelf by licence
hygiene, and it is a *portal* framework — the institutional front door an AI surface can be mounted
into without touching an AGPL LMS core. 🔴 `tsugiproject/tsugi` (Apache-2.0, 10 272 B) has **§4's
`(a)(b)(c)(d)` sub-clause labels stripped**, leaving the NOTICE obligation unlabelled; it remains the
LTI bridge of choice but its grant text is not clean.

### 🟢 The shelf, as it stands

| repository | ★ | forks | f/★ | licence (bytes) | why it is a foundation |
|---|---|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 45 506 | 5 724 | 0.13 | 🔴 Apache-2.0, 6 deviations | Plugin-extensible agent platform: 110 tool definitions, 51-file MCP host layer, quota'd sandbox, three-layer memory (`p484`, `a31d826`) |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | 721 | **552** | **0.77** | 🟡 GPL-2.0 · 18 091 B | 🟢 **NEW** — deployed municipal SIS, package architecture, statutory census integration |
| [oppia/oppia](https://github.com/oppia/oppia) | 6 947 | 5 857 | **0.84** | 🟢 Apache-2.0 · 11 357 B | Interactive-lesson platform with an explorations model others extend; permissive |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | — | — | — | 🟡 GPL-3.0 · 35 146 B | 17 087 files; **99.99 % es / 99.98 % pt** localisation — the deepest on either shelf |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | — | — | — | 🔴 **ECL-2.0** · 11 119 B | 18 348 files, 219 bundle families with full `en`+`es`+`pt_BR` triples |
| [uPortal-project/uPortal](https://github.com/uPortal-project/uPortal) | — | — | — | 🟢 **Apache-2.0 · 0 deviations** | 🟢 cleanest permissive grant here; institutional portal frame |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | — | — | — | 🟢 **MIT** · 1 096 B | 6 040 files; offline-first; ships **`es_419`** at 96.7 % — the LatAm Spanish macro-locale |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | — | — | — | 🟡 LGPL-3.0 · 8 240 B | Odoo-framework education ERP; 100 % es and pt in core; the ERP seam |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 56 | 9 | 0.16 | 🟢 MIT · 1 072 B | 🟢 **NEW** — MCP server implementing BKT; a protocol others build against, which is what a foundation is |
| [cortega26/chile-hub](https://github.com/cortega26/chile-hub) | 135 | 12 | 0.09 | 🟢 **MIT** · 1 069 B | 🟢 **NEW** — curated, normalised Chilean public data incl. education; Polars/DuckDB/SQLite ready |

🔵 **Ten rows, ten real repositories, stated as ten.** Four are new this pass. The shelf is not padded
to a round number, and 🔴 `A-R007/Multi-Agent-Study-Assistant` (64★) was **refused** for having no
licence file.

### 🔴 Declared gaps

| gap | statement |
|---|---|
| 🔴 **`Gap 485-S`** | **A licence LANGUAGE axis is required and does not exist.** Deviation counting and version reading both fail on a translated grant. Until it exists, every non-English licence payload on these shelves is ungraded — and this pass only looked at Portuguese. |
| 🔴 **`Gap 485-T`** | **`i-educar` has not been cloned or read.** Its package architecture, Educacenso module and absence of an AI surface are all from repository metadata, descriptions and topics — **not from source**. The highest-value unread repository on this shelf. |
| 🟡 **`Gap 485-U`** | **Fork-to-star ratio is an unvalidated proxy.** It is used here to admit `i-educar` and it is doing real work, but nothing establishes the threshold, and forks inflate from coursework and one-off patches as well as deployments. |
| 🟡 **`Gap 485-V`** | **`Gap 484-P`, `484-Q`, `484-R` carry forward unaddressed:** DeepTutor's plugin contract is still read rather than exercised, `OpenTutor` still rests on metadata plus licence bytes, and the sandbox remains the least-examined part of the most-examined row. |
| 🟡 **`Gap 485-W`** | **Star and fork counts for five rows are absent** (ILIAS, Sakai, uPortal, Kolibri, OpenEduCat) — the search channel was spent on discovery, so the f/★ column is incomplete and the ratio argument covers only half the shelf. |

---

## 🆕 `p484` — `2026-10-27` — **🟢 THE FOUNDATION ROW THIS SHELF NEVER EXAMINED IS NOW EXAMINED: `HKUDS/DeepTutor` is not only the star leader, it is a **plugin-extensible agent platform** — 110 tool definitions, a 51-file MCP host layer, a quota'd sandbox and a three-layer memory — which makes it a *foundation* in this shelf's sense and not merely an application. 🔴 Its Apache-2.0 text is non-canonical in six operative lines.**

🔵 Measured first-hand at commit **`a31d826`** (tag `v1.6.15`, 2026-10-19), cloned
`--filter=blob:none --depth 1`: **3 875 tracked files**, 1 971 Python, 1 306 TS/JS, **881 test
files**. 🟢 Licence bytes fetched from `raw.githubusercontent.com`, which is reachable this pass
(`Gap 483-C` corrected — see [`intel/market.md`](../intel/market.md)).

### 🟢 Why DeepTutor belongs on the foundations shelf, not only the agents shelf

🔵 This shelf's test is whether a repository is something **others build on**. DeepTutor passes it on
structure, not on reputation:

| foundation property | evidence at `a31d826` |
|---|---|
| documented tool contract | `deeptutor/core/tool_protocol.py` — `BaseTool` ABC, `ToolDefinition`, `ToolParameter` with a `sensitive` flag and provider-strictness handling for Gemini/Anthropic array schemas |
| plugin system | `deeptutor/plugins/` (12 files); *"Every tool — built-in or contributed via plugin — implements `BaseTool`"* |
| capability packaging | **103 files** across 13 capability packages (`reading`, `solve`, `mastery`, `obsidian`, `marginnote4`, `subagent`, `course_study`, `partner_*`, …) |
| **MCP host layer** | **51 files** — catalog + loader, OAuth, secret store, per-user config, network guard, session state |
| provider abstraction | `services/llm/provider_core/` — Anthropic, Azure OpenAI, local; plus `runtime/providers/{allowlist,authorize,scope}.py` |
| execution isolation | `services/sandbox/` — `backends.py`, `quota.py`, `runner/server.py`, `spec.py`, `artifacts.py` |
| multi-tenancy | `deeptutor/multi_user/` (20 files) — grants, per-user tool access, context |
| memory | three-layer memory graph; `api/routers/memory.py`, `runtime/coordination/memory.py`, `memory_probe.py` |

🟢 **The distinction that matters for an engagement:** a studio adopting DeepTutor is adopting a
*platform with a plugin contract and a tenancy model*, which is a 4–6 week integration, not a
2-week fork of an application. That is a different line item and no prior pass could say it.

### 🔴 The licence caveat that now attaches to this shelf's largest row

🔴 Apache-2.0 confirmed from bytes (11 408 B) — but **6 operative-body deviations** against a
normalised canonical instrument (control green), including §4(d) `excluding any notices` where
canonical reads `excluding those notices`, with §4(c) three lines above still reading `those`.
Comparators `braiinz94/braiinz-education` and `towardsai/ai-tutor-app` score **0**. Full analysis on
[`agents/top.md`](../agents/top.md).
🔵 **Grant clauses §2, §3, §5, §7–§9 are byte-identical to canonical** — the copyright and patent
grants Globant relies on are intact. This is diligence, not a blocker.

### 🟢 The foundations panel — licence column verified from bytes this pass

| repository | role | licence (bytes, `2026-10-27`) | read depth |
|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | agent platform: plugin contract, MCP host, sandbox, tenancy | 🔴 Apache-2.0 · 11 408 B · **6 operative deviations** | 🟢 cloned `a31d826` |
| [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | institutional LMS with 4-provider AI SPI + 66-file native MCP server | 🟢 Apache-2.0 (bytes; API says `NOASSERTION`) | 🟢 cloned `96546d9` (`p483`) |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | LMS bridge — 128 tools over Canvas | 🟢 MIT · 1 071 B | 🟢 cloned `becd181` (`p483`) |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | AI-native LMS — 142 MCP tools, Postgres RLS tenancy | 🟢 MIT · 1 062 B | 🟢 cloned `e137ca4` (`p483`) |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | block-based local-first adaptive workspace; 10+ LLM providers | 🟢 MIT · 1 068 B | 🟡 API + licence bytes |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | 173 teacher skill definitions + hosted MCP server | 🔴 **CC BY-SA 4.0** (ShareAlike, code included) | 🟢 cloned `135d627` |

🔵 **Six rows, all real, all licence-verified from bytes.** The shelf minimum is five; this is six
and no row is padding. 🔴 One of the six (`education-agent-skills`) is **not permissively licensed**
and is listed with that marked, because a foundation a studio cannot build on commercially without
ShareAlike obligations is still a foundation the studio needs to know about.

### 🔴 Declared gaps

| gap | statement |
|---|---|
| 🔴 **`Gap 484-P`** | **DeepTutor's plugin contract is read, not exercised.** No plugin was written against `BaseTool`; the 4–6 week integration estimate above is inferred from structure and is uncalibrated (`Gap 483-Q` applies). |
| 🟡 **`Gap 484-Q`** | **`OpenTutor` (152★) is on this shelf on API metadata and licence bytes only.** It is described as local-first with 10+ providers; nothing was cloned, so its provider abstraction is a README claim, not a measurement. |
| 🟡 **`Gap 484-R`** | **The sandbox is the least-examined part of the most-examined row.** `services/sandbox/` was enumerated by filename; `quota.py`, `backends.py` and `runner/server.py` were not read. For a platform whose tenancy story depends on isolation, that is the wrong file to have skipped. |

## 🆕 `p483` — `2026-10-27` — **🟢 `Gap 482-C` CLOSED, AND IT IS THE FIND OF THE CYCLE: `OpenOLAT` — the institutional Java LMS this base graded "on its grant alone" — ships a **four-provider AI SPI including a local-ONNX backend**, a **66-file native MCP server on the official MCP Java SDK 2.1.0**, and an AI essay-grading pipeline with **five pre-filters and a plausibility check**. 🔴 It also exposes GitHub's licence field as an unreliable instrument: the API says `NOASSERTION`, the LICENSE bytes and every source header say Apache-2.0.**

🔵 Measured first-hand at commit **`96546d9`**, cloned `--filter=blob:none --depth 1` (26,015 files in tree,
**14,971** `.java`), then sparse-checked-out to read only `org/olat/mcp`, `services/ai` and `pom.xml`.
Evidence: [`evidence/openolat-ai-mcp-surface.2026-10-27-p483.tsv`](../evidence/openolat-ai-mcp-surface.2026-10-27-p483.tsv).

---

### 🟢 What `Gap 482-C` was hiding

`p482` admitted OpenOLAT entered the shelves "as a licence finding, not as a capability claim" and listed
LOC, AI surface and "whether any MCP/agent integration exists" as unread. All three are now read:

| measurement | value | instrument |
|---|---|---|
| files in tree | 26,015 | `git ls-tree -r --name-only HEAD` |
| `.java` files | 14,971 | pattern count over that list |
| AI service files | **106** `.java` under `core/commons/services/ai` | `find` |
| MCP server files | **66** `.java` under `org/olat/mcp` | `find` |
| AI SPI providers | **4** — `anthropic`, `openAI`, `localonnx`, `generic` | `ls services/ai/spi/` |
| essay pre-filters | **5** | filenames matching `PreFilter` in `services/ai/essay` |
| MCP SDK | `io.modelcontextprotocol.sdk:mcp-core` **2.1.0** | `pom.xml` |
| Anthropic binding | `langchain4j-anthropic` | `pom.xml` |
| QTI · SCORM · LTI path hits | 837 · 172 · 361 | pattern count over the file list |

🔵 **The `pom.xml` dates the MCP work precisely.** The dependency block carries the comment
`<!-- MCP server (spike S1, 2026-10-02): official MCP Java SDK, Jackson 2 binding -->`. This is **25 days old**
— an institutional LMS with a 2018-era GitHub history adopting MCP three weeks ago, and saying in its build
file that it is still a spike.

### 🟢 The AI service layer is a feature surface, not a chat box

| interface | what it does |
|---|---|
| `AiEssayGradingService` · `AiEssayGenerationService` | grade and generate free-text essay items |
| `AiMCQuestionService` | multiple-choice item generation |
| `AiImageDescriptionService` | alt-text / accessibility descriptions |
| `AiEmbeddingSPI` | embeddings behind the same provider abstraction |
| `AiUsageLog` · `AiUsageLogSearchParams` · `AiUsageLogStatus` | 🟢 **per-call usage auditing as a first-class entity** |
| `AiUserPreferenceService` | per-user AI opt-in state |
| `AiFeature` · `AiModule` | feature-flagging the whole surface |

🟢 **`localonnx` is the row that matters commercially.** A provider SPI with an on-device ONNX backend alongside
Anthropic and OpenAI means the same LMS deployment can run AI features **without any outbound call** — which is
the EMEA sovereignty requirement this base has described for three cycles without being able to name a
permissively-licensed LMS that satisfies it. 🔵 `AiApiKeySPI` sits beside it, so the choice is per-deployment
configuration, not a fork.

### 🟢 The essay pipeline is shaped like an Annex III control, and that is unusual

Reading `services/ai/essay/` (38 files) the architecture is not "call a model, store a grade":

| component | role |
|---|---|
| `GibberishPreFilter` · `LanguagePreFilter` · `LengthPreFilter` | reject input before it reaches a model |
| 🔴 **`InjectionPreFilter`** | **prompt-injection filter on student-submitted text** |
| `GradingPlausibilityCheck` | check the model's output is credible before it is surfaced |
| `GradingSuggestion` · `MarkKind` · `AiGradingTier` | the output is a **suggestion** with a tier, not a mark |
| `EssayGradingIntegrityException` · `EssayGradingPreFilterException` · `RejectionReason` | explicit refusal paths |
| `FormativeFeedback` · `EssayFormativeFeedbackService` | feedback decoupled from grading |
| `AnnotatedParagraph` · `AnnotatedSpan` | span-level annotations, so a human can see *where* |
| `AiBloomLevel` | Bloom-taxonomy level attached to generated items |

🟢 **Why this is a finding and not a feature list.** EU AI Act Annex III names "evaluating learning outcomes" as
high-risk, and Art. 14 requires human oversight. A pipeline that returns a *suggestion* at a declared tier,
with span annotations showing the evidence, a plausibility check in front of the human, and named refusal
reasons, is **the shape an auditor asks for** — and it exists, in a permissively-licensed Java LMS, today.
🟡 Whether the filters actually reject what they claim is unverified: nothing was executed (`Gap 483-A`).
🔴 `InjectionPreFilter` is the first prompt-injection control this base has found in any education repository.

### 🔴 GitHub's `license` field disagrees with the file — on two rows

| repo | API `license.spdx_id` | LICENSE file | source headers | verdict |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 **NOASSERTION** | 🟢 Apache-2.0 · 10,982 B · grant body **verbatim** (`p482`) | 🟢 **Apache-2.0**, "you may not use this file except in compliance with the License", © frentix GmbH | 🟢 **Apache-2.0** — two instruments beat the metadata |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | 🔴 **NOASSERTION** | 🔴 unreadable this session | 🔴 unread | 🔴 **unknown — do not reuse** |

🔵 **The lesson generalises.** `p482` built a careful byte-level instrument for Apache grant text and asked, in
`Gap 482-G`, whether the result scales past 13 repositories. The cheap scaling path looked like the API's
`license` field. It is not: on OpenOLAT the field is **wrong in the direction that loses a usable grant**. A
`NOASSERTION` is a *prompt to read the file*, never a finding. 🔴 And the inverse holds too — an API `spdx_id`
of `mit` attests what GitHub's detector matched, not that the grant is unmodified, which is exactly the
deviation `p482` measured on 6 of 13.

### The foundations shelf — every row API-verified at `2026-10-27T15:58Z`

| project | repo | licence | ★ | role | AI/MCP surface |
|---|---|---|---|---|---|
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 (file + headers; API says NOASSERTION) | 448 | institutional LMS: QTI, SCORM, LTI, curriculum, lectures, surveys | 🟢 **106 AI files · 4 SPI providers incl. local ONNX · 66-file MCP server** |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** (API-verified) | 1,240 | higher-ed LMS/VLE in production at research universities | 🔴 none found in path census |
| **Opencast** | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 **ECL-2.0** (API-verified) | 509 | automated lecture capture and video distribution at scale | 🟡 adjacent: `opencast/editor`, `opencast/studio` (subtitles) |
| **Tsugi** | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** (API-verified; grant text measured `p482`) | 377 | LTI / IMS Common Cartridge tool hosting framework |  🔴 none found |
| **uPortal** | [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** (API-verified) | 287 | enterprise higher-ed portal, portlet/soffit model | 🔴 none found |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 MIT | 99 | AI-native LMS; Moodle/Open edX alternative | 🟢 **142 MCP tools · 44 RLS-isolated tables** |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT | 308 | agent bridge **into** an existing Canvas tenant | 🟢 **128 tools · 51 Canvas writes** |

🟡 **The Apache/ECL split is the procurement fact on this shelf.** All four Apereo-family licences were read
from the API this pass: Sakai **ECL-2.0**, Opencast **ECL-2.0**, Tsugi **Apache-2.0**, uPortal **Apache-2.0**.
ECL-2.0 is Apache-2.0 with its patent grant **narrowed to the contributor's own academic and research use** —
which is precisely the clause a commercial integrator must read before building a product on it. 🔴 **No ECL
text was byte-compared against canonical ECL-2.0 this pass**, so whether Sakai's and Opencast's grants are
verbatim is unmeasured — the same question `p482` answered for 13 Apache rows. See `Gap 483-G`.

### 🔴 `mentingo`'s RLS numbers do not reproduce

`p482` published "tenant isolation in **Postgres RLS — 44 enablements, 204 policy clauses**". At `e137ca4`:

| instrument | value | verdict |
|---|---|---|
| `ENABLE ROW LEVEL SECURITY` | **44** | 🟢 reproduces exactly |
| `CREATE POLICY` | **44** | 🟡 one policy per RLS-enabled table |
| `USING (` | 47 | — |
| `WITH CHECK` | 45 | — |
| `FOR` SELECT / INSERT / UPDATE / DELETE / ALL | 35 | — |
| `.sql` files containing `ROW LEVEL SECURITY` | 26 | — |
| **"204 policy clauses"** | 🔴 **not reproduced by any of five instruments** | the mechanism is real; the number is not |

🔵 The isolation claim stands — 44 tables have RLS enabled and 44 policies exist. **The "204" should not be
cited again** until an instrument that produces it is named.
## 🆕 `p482` — `2026-10-27` — **🔴 THIS SHELF'S HEADLINE FROM ONE PASS AGO IS WRONG: `Selleo/mentingo` is **not** "the foundations shelf's first permissively-licensed platform-scale row". `OpenOLAT` has been **Apache-2.0** the whole time, and its grant body is **word-identical to the canonical Apache text through all 1,408 operative tokens** — measured, not asserted. `sakaiproject/sakai` is **ECL-2.0**, also permissive. Both predate `mentingo` by a decade. 🟢 And the Apache alarm `p481` raised is **not supported once the deviations are located**: of the 6 repositories it classed "operative-text ALTERED", **none narrows the rights granted**.**

---

### 🔴 The "first permissive platform-scale LMS" claim, retracted

This base argued from `p478` that no permissively-licensed LMS or SIS exists, and `p481` announced `mentingo`
as the first. The claim was never tested against the mature platforms, only against the four this shelf
already carried. Grants fetched to files and the **files** measured:

| repo | grant file | bytes | licence | permissive | verdict |
|---|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | `LICENSE@master` | 10,982 | 🟢 **Apache-2.0**, grant body **verbatim** | 🟢 YES | **overturns "first"** — Java LMS with QTI, SCORM, curriculum management; descends from OLAT 7.1 |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | `LICENSE@master` | 11,120 | 🟢 **ECL-2.0** (OSI-approved, Apache-2.0 derivative) | 🟢 YES | **overturns "first"** — repo on GitHub since 2014-12-29 |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | `LICENSE` (clone `e137ca4`) | 1,062 | 🟢 MIT | 🟢 YES | still the **newest** and the only **MIT** one — not the first permissive one |
| [frappe/lms](https://github.com/frappe/lms) | `license.txt@develop` | 33,893 | 🔴 **AGPL-3.0** | 🔴 NO | **a widely-cited 2026 LMS comparison lists this as MIT. The grant file is AGPL-3.0.** |
| [frappe/frappe](https://github.com/frappe/frappe) | `LICENSE@develop` | 1,118 | 🟢 MIT | 🟢 YES | the MIT grant belongs to the **framework**; the LMS app on top of it does not inherit it |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | `LICENSE@19.0` | 8,241 | 🟡 defers to a `COPYRIGHT` file; reported LGPL-3.0 | 🔴 no (weak copyleft) | the only row combining **LMS + SIS on one database** |

🔵 Evidence:
[`evidence/permissive-lms-census.2026-10-27-p482.tsv`](../evidence/permissive-lms-census.2026-10-27-p482.tsv).
🔴 `frappe/lms` is the sharpest lesson on this shelf: the framework is MIT, the application is AGPL-3.0, and a
comparison site reading "Frappe" as one thing published the framework's licence for the product. A studio that
took that at face value would have mis-scoped a client's obligations.

### 🟢 The Apache instrument, refined — a word count cannot tell you whether rights changed

`p481` compared operative **token counts** against the canonical text and classed **6 of 13** education
repositories "operative-text ALTERED", concluding that "the supply-side refinement cuts into the permissive
half this base has been relying on". This pass re-fetched the **same six artefacts** — every byte count
reproduces `p481`'s record exactly — and located each change positionally.

🔵 Instrument, reproduced from `p481` and validated: operative text = file truncated at `APPENDIX`,
whitespace-tokenised. On the canonical text it returns **11,358 B, `sha256_16 cfc7749b96f63bd3`, 1,413 tokens** —
identical to `p481`'s reference, so the two passes are using the same ruler. The **grant body** is
tokens `[0:1408]`; tokens `[1408:1413]` are `END OF TERMS AND CONDITIONS`.

| repo | Δ tokens | first change | changes **inside** the grant | section | what actually changed | narrows rights? |
|---|---|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | +99 | **1408** | **0** | none | +99 tokens of trailing OLAT/OpenOLAT provenance prose, after the terms end | 🟢 **NO — grant verbatim** |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2 | 349 | 3 | §1, §4 | `"the"` inserted before `Licensor` ×2; `excluding those notices` → `excluding any notices` | 🟢 NO |
| [ANFAIA/SkillNet](https://github.com/ANFAIA/SkillNet) | +83 | 349 | 3 | §1, §4 | **the identical 3-change signature** | 🟢 NO |
| [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) | +9 | 235 | 12 | §1, §4 | same signature, plus `(an example is provided in the Appendix below)` dropped | 🟢 NO |
| [beltromatti/get-it](https://github.com/beltromatti/get-it) | −5 | 1092 | 5 | **§6 Trademarks** | **deletes** `reasonable and customary use in` | 🟡 NO — it **widens** the exception |
| [onemnemo/mnemo](https://github.com/onemnemo/mnemo) | 0 | 1220 | 5 | §8 Liability | parentheses → commas at 4 positions; **zero words added or removed** | 🟢 NO |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | −4 | 712 | 4 | §4 Redistribution | list labels `(a) (b) (c) (d)` removed; **all four conditions' text intact** | 🟢 NO |

🟢 **The corrected conclusion: all six do deviate from the canonical bytes, and none of the six narrows what a
licensee may do.** Five are stylistic — two definite articles, a determiner, some parentheses, four list
labels. The sixth, `get-it`, is a genuine edit to §6 and it runs in the **licensee's favour**. `p481`'s
direction ("not canonical") was right; its inference ("cuts into the permissive half") does not survive
reading where the cuts fall.

🔵 The most useful by-product: `SkillNet`, `DeepTutor` and `feifei-companion` carry the **same three changes
at the same token offsets** while differing by 650 bytes in file size. That is **one circulating variant text
being copied**, not three projects editing a licence. The byte count was never going to show that.
Evidence: [`evidence/apache-grant-localisation.2026-10-27-p482.tsv`](../evidence/apache-grant-localisation.2026-10-27-p482.tsv).

### 🔵 What this means for the shelf's licence posture

| claim this base has published | status after `p482` |
|---|---|
| "no permissively-licensed platform-scale LMS exists" (`p478`–`p480`) | 🔴 **false** — OpenOLAT (Apache-2.0) and Sakai (ECL-2.0) |
| "`mentingo` is the first permissively-licensed platform-scale row" (`p481`) | 🔴 **false** — it is the newest, and the only MIT one |
| "6 of 13 Apache education repos do not carry canonical operative text" (`p481`) | 🟢 **true as stated**, and now localised |
| "one has had a clause narrowed" (`p481`) | 🔴 **not supported** — the one real edit widens §6 |
| "the Apache finding cuts into the permissive half" (`p481`) | 🔴 **not supported** |
## 🆕 `p481` — `2026-10-27` — **🟢 THE FOUNDATIONS SHELF GAINS ITS FIRST PERMISSIVELY-LICENSED PLATFORM-SCALE ROW, READ AS SOURCE: `Selleo/mentingo` — **MIT**, 584,229 LOC, 794 test files, multi-tenant, with a native MCP surface and an OAuth consent controller — against a shelf whose three incumbent platforms are all AGPL-3.0. 🟢 And the canonical Apache-2.0 text is now held in this base as a measured reference (11,358 B · 1,413 operative word tokens), which turns "is this really Apache-2.0?" from a judgement into a diff.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — the harness refuses execution of
code arriving in a clone. Nothing below is gate-attested, and **nothing cloned this pass was run**
(`Gap 481-A`).

---

### 🟢 The reference this shelf never had

Every licence verdict this base has published for an Apache-2.0 row has been a comparison against remembered
text. The licensor's own copy is now fetched, measured and stored as the comparison basis:

| property | value |
|---|---|
| source | `https://www.apache.org/licenses/LICENSE-2.0.txt` (`http=200`) |
| bytes | **11,358** |
| `sha256` (16) | `cfc7749b96f63bd3` |
| operative word tokens (to `END OF TERMS AND CONDITIONS`) | **1,413** |

🔵 Two instruments follow from it, and they disagree in a way that matters. Comparing *bytes* calls 13 of 13
education Apache repositories non-canonical. Comparing *operative words* calls **7 of 13 verbatim**. The
word-level instrument is the correct one, because Apache-2.0 instructs the licensee to fill in the appendix —
so an appendix difference is compliance, not deviation. Full table on `repos/trending.md`.

### 🟢 The foundations tier — grant, liveness, and source read first-hand where stated

| repo | ★ · grant | last pushed | read this pass | what it is |
|---|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · 35,136 B | live | 🔵 carried from `p480` | MOOC-scale LMS; **carries the RPC scope clarification** (`p480`) |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0-only** · 34,520 B | live | 🔵 carried from `p480` | LMS of record in much of US higher ed; **no scope clarification** |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 · 34,523 B | live | 🔵 carried from `p480` | the supported Open edX deployment path; Docker-based |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | live | 🔵 carried; not re-read | the default open LMS worldwide |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** · 1,062 B | **2026-10-27** | 🟢 **cloned `e137ca4`** | **584,229 LOC** multi-tenant LMS; MCP + OAuth consent; Langfuse tracing; **794 test files** |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT · 1,071 B | 2026-10-26 | 🟢 **cloned `becd181`** | 32,878 LOC; **130 tools under a 4-class effect policy**; 21 confirmation guards; 60+ security tests |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟡 Apache-2.0 · 11,408 B *(operative text **altered**, 4 tokens)* | 2026-10-27 | 🔵 grant re-diffed this pass | 819,646 LOC (`p480`); 45,069★; the largest education-AI repository on GitHub |
| [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) | 🟢 MIT · 1,072 B | 2026-10-27 | 🔵 carried from `p480` | 1,276 LOC; **26 read-only tools**, 33 calls, zero writes |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT · 1,073 B | 2026-10-27 | 🟢 **cloned `0342cfb`** | 171,107 LOC **Go**; MCP over HTTP with auth middleware; 365 tests; `Dockerfile` |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 MIT · 1,068 B | 2026-10-26 | 🟢 **cloned `039bfb9`** | 108,286 LOC; 136 tests; `docker-compose.prod.yml`; no MCP surface |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 Apache-2.0 · `NOTICE` + 175 headers | 2016-07-20 | 🔵 carried from `p480` | 273,846 LOC SIS; **Rails 2.3.5 — not a viable base** (`p480`) |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT | 2026-10-22 | 🔵 grant + metadata only | 536★; spaced repetition as MCP tools |

### 🟢 Why `mentingo` changes the shape of this shelf

The shelf's platform tier has been uniformly copyleft, which forces every recipe this base writes into the
"deployed beside, not linked into" architecture that `p480` finally found first-hand grant-text support for
(Open edX's RPC clarification). A **permissively licensed** platform removes that constraint for the first time:

| signal read first-hand | value | why it counts |
|---|---|---|
| grant | `MIT License` · `Copyright (c) 2024 Selleo` · 1,062 B | no source-disclosure duty on a hosted service |
| scale | 584,229 LOC; **794** test files | not a demo |
| domain model | `courses`, `chapters`, `lessons`, `groups`, `certificates`, `quiz` schema | a real LMS, not a course-content generator |
| tenancy | `tenant-aware-session` in the storage layer | multi-tenant by construction |
| agent surface | `apps/api/src/mcp/` — admin tools, customization tools, upload tools, content resource, **`mcp-oauth.controller.ts`**, **`mcp-consent.controller.ts`**, `mcp-auth.guard.ts` | the agent integration is **in** the platform, with an OAuth consent step |
| observability | `@langfuse/{client,core,otel,tracing,vercel-ai-sdk}`, `@ai-sdk/openai` | LLM tracing wired in, not bolted on |
| deployment | `docker-compose.yml`, `docker-compose.langfuse.yml`, preview template | a documented path to running it |

🔴 **What this is not.** 99★. Against Moodle's and Canvas's institutional install bases this is a *licensing*
answer and a *architecture* answer, not an adoption answer. Migration cost, accessibility conformance, LTI
support and SIS integration are all unexamined (`Gap 481-C`).

### 🔵 The permissive-platform question, restated now that it has two answers

| candidate | grant | blocker |
|---|---|---|
| `projectfedena/fedena` | 🟢 Apache-2.0 | 🔴 **architectural** — Rails 2.3.5, no `Gemfile`, Flash reporting, last push 2016 (`p480`) |
| `Selleo/mentingo` | 🟢 **MIT** | 🟡 **adoption** — 99★, maturity and institutional integrations unexamined |

🔵 These are different kinds of blocker, and the second kind is the kind a studio can absorb. `p479`'s
conclusion — *"the permissive SIS is not missing, it is fifteen years old"* — needs amending for the LMS tier:
**the permissive LMS is not missing and not old; it is small.**

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 481-F`** | **Nothing on this shelf was executed** (`Gap 481-A`). `mentingo`'s 794 test files were counted, not run; its `docker-compose.yml` was not brought up. "A documented path to running it" means a file exists. |
| 🟡 **`Gap 481-G`** | **`mentingo` is profiled, not audited** (`Gap 481-C`): the OAuth consent controller, the MCP auth guard and the tenant-isolation test were identified **by filename** and not read. Whether its MCP tools are write-guarded is **unknown** — and this pass's own `canvas-mcp` finding is the reason that question should not be assumed either way. |
| 🟡 **`Gap 481-H`** | **The four copyleft platform rows were not re-read this pass.** Their grants, byte counts and elections are carried from `p479`/`p480`. Only `DeepTutor`'s Apache file was re-diffed. |
| 🟡 **`Gap 481-I`** | **The canonical Apache reference is one fetch on one day.** It was not checked against a second channel, and `apache.org` was the only licensor text this base holds — there is still **no canonical MIT, GPL-3.0 or AGPL-3.0 reference stored here**, so those families remain byte-compared rather than word-compared. |
## 🆕 `p480` — `2026-10-27` — **🟢 `Gap 479-H` IS CLOSED ON BOTH ROWS, AND ONE OF THE TWO ANSWERS IS WORTH MORE THAN AN ELECTION: Canvas LMS elects **AGPL-3.0-only** — read from its per-file header, not guessed — and Open edX's `LICENSE` carries **616 bytes the bare FSF text does not have**: an explicit edX Inc. clarification that a separate web service talking to it over **RPC is not a derivative work**. 🟢 That is the first first-hand grant-text basis this base has ever had for the "deployed, not linked" boundary its whole compose shelf rests on.**

🔵 **Gate posture, unchanged (`Gap 446-A`):** `make hooks` **not attempted** — the harness refuses execution of
code arriving in a clone (`Code from External`). **Nothing below is gate-attested.** Frontmatter, closed-vocabulary
`region`, table pipe-counts, no-header-as-data, prepend-only and grant-measured-as-a-file all re-checked in this
session's own code.

---

### 🟢 `Gap 479-H`, row one — Canvas LMS elects AGPL-3.0-**only**, and the election was never in the `LICENSE` file

🔵 `Gap 479-H`: *"Two elections remain unread — `canvas-lms` (bare `AGPL-3.0`)…"* 🔵 The reason prior passes could
not read it is that they read the wrong file. `instructure/canvas-lms`'s `LICENSE` is the **bare FSF text**
(34,520 B); the only "any later version" strings in it sit in the FSF's own non-operative *"How to Apply These
Terms"* appendix. 🟢 **The operative election lives in the per-source-file header**, and it is unambiguous
(`app/models/course.rb`, read via `raw.githubusercontent.com`):

> *"Canvas is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General
> Public License as published by the Free Software Foundation, **version 3 of the License.**"*

🔴 **No "or (at your option) any later version".** Canvas LMS is **AGPL-3.0-only** — the same election `tutor`
carries on the Open edX deployment path, so the two dominant open LMS platforms now read the same way on version.

### 🟢 `Gap 479-H`, row two — Open edX's `LICENSE` is 616 bytes longer than the bare text, and the extra bytes are the finding

🔵 `openedx/edx-platform`'s `LICENSE` is **35,136 B** against `canvas-lms`'s 34,520 B and `tutor`'s 34,523 B.
🟢 Diffing it against `canvas-lms` isolates the difference exactly: **ten appended lines, in edX Inc.'s own voice**:

> *"EdX Inc. wishes to state, in clarification of the above license terms, that any public, independently
> available web service offered over the network and communicating with edX's copyrighted works by any form of
> inter-service communication, including but not limited to Remote Procedure Call (RPC) interfaces, **is not a
> work based on our copyrighted work** within the meaning of the license. 'Corresponding Source' of this work, or
> works based on this work, as defined by the terms of this license **do not include source code files for
> programs used solely to provide those public, independently available web services.**"*

🟢 **This is the single most useful sentence this base has found for its own compose shelf.** `Gap 478-T`,
`Gap 479-R` and `Gap 479-AS` all say the same thing: the "AI service alongside the platform, talking over
HTTP" boundary is *architectural reasoning, never verified*. For **Open edX specifically**, it no longer is —
the copyright holder states in the licence file that an independently available service communicating by RPC is
outside the copyleft scope and that its source is not Corresponding Source.

🔴 **Three limits, stated plainly, because this is a legal reading and this base does not give advice:**

| limit | why it matters |
|---|---|
| 🔴 It is a **clarification of the licensor's interpretation**, not an amendment to the AGPL text | its weight against a third party is a legal question this base cannot answer |
| 🔴 It names **edX Inc.** | Open edX is now stewarded by the **Axim Collaborative**; whether the statement binds successors or later contributors is unread here |
| 🔴 It covers a service that is **"public, independently available"** and reached by **inter-service communication** | an AI component embedded as a *plugin inside* the platform process is plainly **not** what this sentence protects |

🔴 **And the contrast is decision-grade: Canvas carries no equivalent clarification.** Two platforms, the same
AGPL-3.0-only election, the same proposed architecture — and **materially different documented posture**. See
`verticals/solutions.md` and `compose/patterns.md`.

### 🟢 `Gap 479-M` closed, in the opposite direction from the gap's suspicion

🔵 `Gap 479-M`: *"Fedena's Apache-2.0 rests on a `NOTICE`, not a `LICENSE`… **No source file header was read to
corroborate it.**"* 🟢 The repository was cloned (`68a84ac`) and the headers were read:
**175 Ruby files under `app/` and `lib/` carry the full per-file Apache-2.0 notice**, `app/models/student.rb`
among them:

> `#Licensed under the Apache License, Version 2.0 (the "License");` … `#You may obtain a copy of the License at`
> … `#  http://www.apache.org/licenses/LICENSE-2.0`

🟢 **The grant is corroborated per-file, exactly as the gap asked.** A `NOTICE` plus 175 concordant source
headers is a far stronger statement of intent than a `NOTICE` alone. 🔵 Whether a `NOTICE` *suffices as the
instrument* remains a legal determination this base cannot make — but the evidentiary position is no longer
one file.

### 🟢 The foundations tier — grant, liveness and, for four rows, source read first-hand

| repo | ★ · grant | last pushed | read this pass | what it is |
|---|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · 35,136 B | live | 🟢 `LICENSE` diffed byte-for-byte | MOOC-scale LMS; **carries the RPC scope clarification above** |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 · 34,520 B | live | 🟢 `LICENSE` + per-file header | LMS of record in much of US higher ed; **AGPL-3.0-only, no clarification** |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 · 34,523 B | live | 🟢 `LICENSE` payload | the supported Open edX deployment path; Docker-based |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟡 Apache-2.0 · 11,408 B *(non-canonical)* | 2026-10-27 | 🟢 **cloned `a31d826`** | **819,646 LOC** (523,055 Python · 173,012 TSX · 123,255 TS); v1.6.15; wheels `deeptutor`, `deeptutor-cli` |
| [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) | 🟢 MIT · 1,072 B | 2026-10-27 | 🟢 **cloned `a91eeb9`** | 1,276 LOC; **26 read-only tools onto Canvas**; 500-item/list ceiling |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT · 1,071 B | 2026-10-26 | 🟢 **cloned `becd181`** | 32,878 LOC Python; **136 tools, 12 write call sites**, incl. rubric grading |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟢 Apache-2.0 · `NOTICE` 680 B **+ 175 file headers** | 2016-07-20 | 🟢 **cloned `68a84ac`** | 273,846 LOC SIS; **Rails 2.3.5** — see `verticals/solutions.md` |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT | 2026-10-22 | 🔵 grant + metadata only | 536★; spaced repetition exposed as MCP tools |

🔵 **Four of eight rows on this shelf now rest on a clone.** That is the first time any row here has.

### 🟢 What a clone shows about DeepTutor that no metadata channel could

🔵 `Gap 479-L`: *"No row was installed, run or benchmarked."* 🔴 Still true — execution is refused. 🟢 But the
tree itself carries maturity signals that a star count cannot:

| signal | what was found | why it reads as maturity |
|---|---|---|
| `.importlinter` | present at repo root | the project **enforces layer/import contracts in CI** — a deliberate architectural boundary, rare at this size |
| `pyproject.toml` | `requires-python = ">=3.11,<3.15"` with a commented forward-cap rationale | the cap is *reasoned* ("compiled base dependencies such as FAISS publish compatible wheels"), not copied |
| published artefacts | `pip install deeptutor` / `deeptutor-cli` | a **wheel**, not a clone-only project — unlike `boyuchengz/canvas-mcp`, which is `"private": true` |
| `.secrets.baseline`, `.pre-commit-config.yaml` | present | secret scanning and hooks wired in |
| `THIRD_PARTY_NOTICES.md`, `CITATION.cff` | present | attribution and citation handled deliberately |
| MCP client | in **core** dependencies, not an extra | tool-calling is architectural, not an add-on |

🔵 For a studio deciding whether a 44.9k★ repository is a toy or a base to build on, **these are the signals that
answer the question**, and all six require a clone to see.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 480-G`** | **The Open edX clarification is read, not adjudicated.** Whether it binds the Axim Collaborative as edX Inc.'s successor, whether it reaches later third-party contributors' code in the same tree, and whether a court would read it as the gap says are **three separate legal questions, none of them answerable here**. The sentence is quoted so a lawyer can rule on it — it is not itself a ruling. |
| 🔴 **`Gap 480-H`** | **`Gap 479-G` and `Gap 478-J` stand: no depth or scope probe ran.** Rows are graded on one grant file plus, for four of them, a static source read. The ECL-2.0 patent reading on `sakaiproject/sakai` is untouched this pass and remains this base's own reading of licence text. |
| 🔴 **`Gap 480-I`** | **`Gap 479-I` unchanged: BigBlueButton's per-source-file notice is still unread**, and the LGPL-3.0 reading still rests on one `LICENSE` plus one module's `build.sbt`. The per-file technique that closed `Gap 479-M` for Fedena and the election for Canvas **was not applied to it**, which is an omission of effort, not of instrument. |
| 🟡 **`Gap 480-J`** | **Canvas's election rests on one source file.** `app/models/course.rb` is representative of a convention, not proof of it; no sweep across the tree confirmed that every file carries the same "version 3 of the License" wording, and `canvas-lms` was **not** cloned — it was read one path at a time. |
| 🟡 **`Gap 480-K`** | **`Gap 479-J` and `Gap 479-K` carry forward untouched.** No digest family was mapped to an FSF publication event, and `last push` versus `updated_at` is still a mixed basis for "alive" across the older rows on this shelf. |
| 🟡 **`Gap 480-L`** | **DeepTutor's maturity signals are *present*, not *exercised*.** `.importlinter` existing is not the same as its contracts passing; the wheels are named in packaging metadata and **were not installed**; `requires-python` was read, not satisfied. Every row of that table is a static read (`Gap 480-A`). |

---

## 🆕 `p479` — `2026-10-27` — **🟢 THE AGPL-3.0 CONTROL EXISTS AFTER ALL — four unrelated projects are byte-identical at **34,523 B · `0d96a4ff68ad`** — and the same measurement found the thing this base has been asserting without proof: a **byte-count collision**. Two projects carry 34,523 B with a **different digest**, so for AGPL-3.0 a matching byte count is not merely weak evidence, it is *actively misleading*. 🔴 And the maintenance read is the commercial finding: **`EduKTM` has not been pushed since 2024-01-02** and **`pelotech/xapi-lrs` has 0★** — both are load-bearing components in this base's own recipes.**

🔵 Gate posture unchanged (`Code from External`; `make hooks` not attempted; session-local checks green — see the
agents shelf). Grants in
[`evidence/grant-payload.2026-10-27-p479.tsv`](../evidence/grant-payload.2026-10-27-p479.tsv); licence-text
controls in [`evidence/license-controls.2026-10-27-p479.tsv`](../evidence/license-controls.2026-10-27-p479.tsv);
elections in [`evidence/election-probe.2026-10-27-p479.tsv`](../evidence/election-probe.2026-10-27-p479.tsv).

---

### 🟢 The AGPL-3.0 control, and the collision that makes byte counts unsafe

🔵 `p478` recorded: *"no AGPL control exists — four byte counts, so a byte count alone can never identify AGPL-3.0
here."* 🟢 The control was missing because the sample was four copyleft **platforms**, all shipping older
renderings. This pass read AGPL payloads from **ten** projects and the FSF text appears cleanly:

| byte count | digest | projects seen at this digest | reading |
|---|---|---|---|
| **34,523** | `0d96a4ff68ad` | [overhangio/tutor](https://github.com/overhangio/tutor), [sitor-ai/frametell](https://github.com/sitor-ai/frametell), [penecho/penecho](https://github.com/penecho/penecho), [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | 🟢 **four unrelated projects byte-identical — this is the control** |
| **34,523** | `8486a10c4393` | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse), [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | 🔴 **same length, different bytes** — and reproduced across two unrelated projects, so it is a second rendering, not a typo |
| 34,522 | `20b067f86de3` | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | 🟡 the control minus its final newline |
| 34,520 | `57c8ff33c9c0` | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🟡 older rendering; tail cites `http://` gnu.org |
| 34,514 | `ea94d5765c59` | [artcc/freelingo](https://github.com/artcc/freelingo) | 🟡 unmatched |
| 35,240 | `119d54a4bd57` | [1111philo/learn](https://github.com/1111philo/learn) | 🟡 unmatched; 17 occurrences of *"Affero"* |
| 35,326 | `fe85f94658bf` | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **a Portuguese translation** of AGPL-3.0 |
| 35,136 | `e12d78569742` | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🟡 older rendering |
| 33,893 | `db1a87ba81e8` | [frappe/lms](https://github.com/frappe/lms) | 🟡 older rendering, lowercase `license.txt` |
| **1,134** | `3fb8cda58638` | [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 🔴 **a 1.1 KB notice, not the licence** — 584★ and no full text in the repository |

🔵 **`diff` on the collision pair**, run against the control: the two 34,523-byte files differ at lines 636–637,
inside the FSF *"How to Apply"* appendix, where `as published by / the Free Software Foundation` is re-wrapped as
`as published / by the Free Software Foundation`. 🟢 **The operative terms are identical**, so `learnhouse` and
`edgameclaw` really are AGPL-3.0 unmodified in substance. 🔴 **But the method is now disproved**: a byte count that
*matches the control exactly* can still be a different file. For AGPL-3.0 only the digest identifies the text, and
every AGPL row on every shelf of this base should be read as digest-identified or not identified at all.

🟢 The same reading gives the other two families a second control each: **Apache-2.0** at 11,357 B ·
`c71d239df917` now appears in three unrelated projects ([yetanalytics/lrsql](https://github.com/yetanalytics/lrsql),
[pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs), [f3an/kodeida](https://github.com/f3an/kodeida)), with a
**+1-byte** variant at `cfc7749b96f6` shared by two more
([cyyeh/agent-loop-visualizer](https://github.com/cyyeh/agent-loop-visualizer),
[Amine-LG/RootToRun](https://github.com/Amine-LG/RootToRun)); **GPL-3.0** at 35,149 B · `3972dc9744f6` now appears
in three ([plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt),
[saniales/ai-lesson-planner](https://github.com/saniales/ai-lesson-planner),
[ahmedEid1/lumen](https://github.com/ahmedEid1/lumen)).

### 🔴 The maintenance read — two components this base recommends are not alive

🔵 `Gap 478-N` asked whether the knowledge-tracing libraries are maintained; `Gap 478-M` asked for any differenceable
state at all. 🟢 The search channel answers both with first-hand timestamps:

| repo | ★ | created | last push / update read | reading |
|---|---|---|---|---|
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 452 | 2022-05-14 | **pushed 2026-10-18** | 🟢 **alive** — nine days before this pass |
| [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) | 267 | 2021-03-17 | 🔴 **pushed 2024-01-02** | 🔴 **dormant 2 y 10 m** — and it is P12's mastery-model component |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 271 | 2019-12-19 | **pushed 2026-10-27** | 🟢 alive, pushed the day of this pass |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 144 | 2021-05-06 | updated 2026-10-27 | 🟢 alive |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | **0** | 2026-03-04 | 🔴 updated 2026-08-08 | 🔴 **zero stars, nothing in 2½ months** — and it is P12's record store |
| [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 15 | 2025-05-24 | updated 2026-08-22 | 🟡 quiet |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 22 | 2026-07-09 | updated 2026-10-19 | 🟢 recent |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 1,162 | 2016-01-19 | updated 2026-10-27 | 🟢 alive; the one permissive platform here |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 1,143 | 2017-02-13 | updated 2026-10-27 | 🟢 alive |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 956 | 2012-12-19 | updated 2026-10-22 | 🟢 the interop contract, maintained |

🔵 **`pelotech/xapi-lrs` also explains an apparent anomaly.** It did not appear in a name search for `xapi-lrs`
sorted by stars — because it has **none**. 🟢 Its grant is two-pass consistent (11,357 B · `c71d239df917`, the
Apache control, same as `p478`) and `git ls-remote` resolves it, so this is **not** a canonicality problem of the
kind `Gap 478-AO` describes: it is a real address with zero adoption. 🔴 Which is worse for a recipe than a
rename would be.

### 🟢 Elections: two of the four unread ones are now read

🔵 `Gap 478-K` and `Gap 478-Q` named four copyleft rows whose election — *version 3 only* vs *or later* — had never
been read. Two are now resolved from the projects' own packaging declarations:

| repo | declaration read | election | channel |
|---|---|---|---|
| [frappe/lms](https://github.com/frappe/lms) | `"license": "AGPL-3.0-or-later"` | 🟢 **or-later** — an upgrade option exists | `package.json` line 18 |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | `'license': 'LGPL-3'` plus a file header reading *"either version 3 of the License, or (at your option) any later version"* | 🟢 **LGPL-3.0-or-later** | `openeducat_core/__manifest__.py` line 25 + header |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | `"license": "AGPL-3.0"` | 🔴 **unresolved** — a bare, deprecated SPDX identifier that elects nothing | `package.json` line 3 |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | **nothing** — no licence field in `package.json`, no `license` key or classifier in 48,283 B of `pyproject.toml`, `setup.py` 404 | 🔴 **unresolved** | two channels read, both silent |

🔵 `frappe/lms` was the row this base most wanted, because `p477` found a vendor table calling it MIT. 🟢 It is
AGPL-3.0, **or-later**, declared by the project itself.

### 🟢 The permissive foundation tier, every grant first-hand

🔵 Unchanged rows carry their payload from the pass that read them; new rows are read this pass.

| repo | grant (payload) | bytes · sha | what it is | region |
|---|---|---|---|---|
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | 11,357 · `c71d239df917` | SQL-backed xAPI Learning Record Store, Clojure; 144★ | North America |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | 11,525 · `a1587287ff04` | the xAPI specification itself; 956★ | North America |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | 1,066 · `f5f955194636` | deep knowledge-tracing benchmarks; 452★, pushed this month | APAC |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | 1,105 · `5baaaf977a28` | BKT-driven open ITS, UC Berkeley CAHL; 271★, pushed today | North America |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1,097 · `3c056b34a476` | offline-first learning platform; 1,162★ | Global |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** | 11,906 · `cbac9a0fde05` | general ERP framework — the permissive fallback; 1,143★ | Global |
| [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** | 1,069 · `4aa758cb51b2` | MCP server writing agent turns as xAPI statements; 15★ | EMEA |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** | 1,092 · `e162f8f4b461` | 1,721 BNCC curriculum objectives, JSON/SQLite/CSV; 22★ | LATAM |
| [boyuchengz/canvas-mcp](https://github.com/boyuchengz/canvas-mcp) | 🟢 **MIT** | 1,072 · `4450dee7f762` | 🆕 **read-only MCP server onto Canvas LMS** — the LTI/REST boundary as a component; 115★, created 2026-10-25 | Global |
| [cortega26/chile-hub](https://github.com/cortega26/chile-hub) | 🟢 **MIT** | 1,070 · `277707dcaa3b` | 🆕 curated Chilean public data incl. education, Polars/DuckDB/SQLite-ready; 135★ | LATAM |
| [Universidade-Livre/ciencia-da-computacao](https://github.com/Universidade-Livre/ciencia-da-computacao) | 🟢 **MIT** | 1,087 · `6520b550c69f` | 🆕 Brazilian self-study CS curriculum, 20,970★ — the most-starred Portuguese-language education repository measured here | LATAM |
| [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) | 🟢 **Apache-2.0** | 11,367 · `59f13c04f0e6` | knowledge-tracing model zoo — 🔴 **dormant since 2024-01-02** | APAC |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | 🟢 **Apache-2.0** | 11,357 · `c71d239df917` | xAPI 1.0.3 + 2.0 LRS on Hono + Postgres — 🔴 **0★, quiet since 2026-08-08** | Global |

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 479-G`** | **`Gap 478-J` and `Gap 478-O` stand: no depth or scope probe ran.** Every row is graded on one grant file; the ECL-2.0 patent reading on `sakaiproject/sakai` is still this base's own reading of licence text and not advice. |
| 🔴 **`Gap 479-H`** | **Two elections remain unread** — `canvas-lms` (bare `AGPL-3.0`) and `openedx-platform` (nothing declared in two channels). For Open edX the deployment path's election is known (`tutor` is AGPL-3.0-**only**), so the platform's own election is the gap that matters least in practice and most in principle. |
| 🔴 **`Gap 479-I`** | **`Gap 478-L` unchanged: BigBlueButton's per-source-file notice is still unread**, and the LGPL-3.0 reading still rests on one `LICENSE` plus one module's `build.sbt`. |
| 🟡 **`Gap 479-J`** | **The digest families are observational, not exhaustive.** Ten AGPL payloads produced eight distinct digests; nothing here maps those digests to FSF publication events, so "older rendering" is an inference from the `http://` vs `https://` tail and the byte count, not a dated provenance. |
| 🟡 **`Gap 479-K`** | **`last push` is read for six rows and `updated_at` for the rest.** They are different events — a metadata touch updates one and not the other — so "alive" is graded on a weaker signal for `lrsql`, `kolibri`, `ofbiz-framework`, `xAPI-Spec`, `learnmcp-xapi` and `bncc-dados` than for `EduKTM` and `pykt-toolkit`. |
| 🟡 **`Gap 479-L`** | **No row was installed, run or benchmarked**, repeating `Gap 478-N`'s core objection. "`pykt-toolkit` is maintained" is now measured; "`pykt-toolkit` works" is not. |

---

## 🆕 `p478` — `2026-10-27` — **🟢 `Gap 477-N` IS CLOSED AND THE ANSWER IS THE RESTRICTIVE ONE: `overhangio/tutor` elects **`AGPL-3.0-only`**, declared in `pyproject.toml`, so the standard Open edX deployment path has no upgrade option. 🟢 A declared nil in the secondary literature — "no open source knowledge tracing library" — is refuted by two payload-verified repositories. 🔴 And this pass's own 404 on `frappe/lms` was an artefact of its own path list: the grant is there, in lowercase, and it is AGPL-3.0.**

🔵 Gate posture unchanged from the agents shelf (`Code from External`; `make hooks` not attempted;
session-local checks green). Grants in
[`evidence/grant-payload.2026-10-27-p478.tsv`](../evidence/grant-payload.2026-10-27-p478.tsv) (39 rows);
licence-text controls in
[`evidence/license-controls.2026-10-27-p478.tsv`](../evidence/license-controls.2026-10-27-p478.tsv).

---

### 🟢 `Gap 477-N` closed — `tutor` elects AGPL-3.0-**only**

🔵 `Gap 477-N`: *"`overhangio/tutor`'s AGPL-3.0 election is unread, and it is the one row in the tier where the
answer would matter."* 🟢 It is readable, one file above the licence.

| channel | result |
|---|---|
| `LICENSE.txt` payload | 34,523 B · `0d96a4ff68ad` — AGPL-3.0 body; `"any later version"` appears **3×**, all inside the FSF *How to Apply* appendix |
| 🟢 `pyproject.toml` line 6 | **`license = {text = "AGPL-3.0-only"}`** — the project's own election, unambiguous |
| `pyproject.toml` classifier | `License :: OSI Approved :: GNU Affero General Public License v3` — 🟡 silent on the election |
| `README.rst` badge | `AGPL License`, linking `agpl-3.0.en.html` — 🟡 silent on the election |

🔴 **The restrictive reading is the correct one, and it is the one that matters.** `tutor` is the official
Docker-based deployment tool for Open edX, so a studio deploying Open edX the recommended way is bound to
AGPL-3.0 **with no option to move to a later AGPL**, and the AGPL's network clause reaches users served over a
network, not only redistributors. 🟢 **The method generalises and should be reused:** the `"any later version"`
string inside a GPL-family payload is boilerplate from the appendix and is **never** evidence of an election —
the election lives in packaging metadata, which is exactly where `p476` found `penecho`'s.

### 🔴 This pass's own instrument error, published because it is the reusable part

🔵 The first probe of [frappe/lms](https://github.com/frappe/lms) reported `NO LICENSE FILE AT ANY PROBED PATH` —
a clean 404 across `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` on both `main` and `master`.
🔴 **That was wrong, and the cause was the path list, not the repository.**

| probe | result |
|---|---|
| 5 uppercase variants × 2 branches | 🔴 **all 404** |
| 🟢 `license.txt` — **lowercase** | 🟢 **200 · 33,893 B** on `main`, `develop` **and** `master` |
| payload's first line | **`GNU AFFERO GENERAL PUBLIC LICENSE Version 3`** |

🔵 `raw.githubusercontent.com` paths are case-sensitive and the Frappe projects use lowercase. 🔴 **So a 404 from
a path probe is not evidence that a repository has no grant** — it is evidence that the probed list was
incomplete, and the two are indistinguishable from the outside. 🟢 This has a direct bearing on the agents shelf:
the rejection of `yashas-wi/Personalised-AI-Tutor` rests on a 404 **plus a blank About sidebar**, which is why
the second channel matters. A 404 alone would not have been enough.

🟡 **And it corrects the secondary literature twice over.** A vendor comparison table reached this pass listing
*"Frappe LMS | MIT"*. It is **AGPL-3.0**, read from the payload. Mirror listings saying AGPL were right and the
comparison table was wrong — which is the ordinary case, not the surprising one.

### 🟢 A declared nil refuted: knowledge tracing has two permissive libraries

🔵 A targeted search for knowledge-tracing libraries returned LRS projects and concluded *"the search did not find
any open source knowledge tracing library"*. 🔴 **Two exist and both are permissive**, grants read as payloads:

| repo | grant (payload) | what it is |
|---|---|---|
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · 1,066 B · `f5f955194636` | deep knowledge tracing benchmark library; copyright 2022 |
| [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) | 🟢 **Apache-2.0** · 11,367 B · `59f13c04f0e6` | knowledge-tracing model toolkit, USTC big-data lab |

🔵 Same lesson as `p477`'s nil refutation, different instrument: **a nil from a keyword search is a statement
about the query**, not about the world. Knowledge tracing is the mechanism underneath adaptive sequencing, and
this base had been carrying BKT as something only `OATutor` and `tutor-mcp` implement inline.

### 🟢 The permissive infrastructure tier — every grant a payload read this pass

| repo | grant (payload) | bytes · sha | what it is | region |
|---|---|---|---|---|
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | 11,357 · `c71d239df917` | SQL-backed xAPI Learning Record Store, Clojure | North America |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | 🟢 **Apache-2.0** | 11,357 · `c71d239df917` | xAPI 1.0.3 + 2.0 LRS on Hono + Postgres, embedded PGlite mode | Global |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | 11,525 · `a1587287ff04` | the xAPI specification itself — the interop contract both LRSs implement | North America |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | 1,066 · `f5f955194636` | deep knowledge tracing benchmarks | APAC |
| [bigdata-ustc/EduKTM](https://github.com/bigdata-ustc/EduKTM) | 🟢 **Apache-2.0** | 11,367 · `59f13c04f0e6` | knowledge tracing models | APAC |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | 1,105 · `5baaaf977a28` | BKT-driven open ITS; UC Berkeley CAHL lab | North America |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1,097 · `3c056b34a476` | offline-first learning platform — the one permissive **platform** in this base | Global |
| [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** | 1,069 · `4aa758cb51b2` | MCP server that writes agent turns as xAPI statements | EMEA |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** | 1,092 · `e162f8f4b461` | 1,721 BNCC curriculum objectives, JSON/SQLite/CSV; held by *Profy Tecnologias Educacionais Ltda* | LATAM |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** | 11,906 · `cbac9a0fde05` | general ERP framework — the permissive fallback where no education ERP is | Global |

🟢 **Ten rows, ten permissive grants, all payload-verified.** 🔵 Two of them close `Gap 477-AH` and are flagged on
`compose/patterns.md`: `learnmcp-xapi` was carried and `bncc-dados` had **never** been read first-hand in any pass
— it was described from its README as *"open data"*. It is **MIT**, held by a named Brazilian company. That is a
better footing for the LATAM recipe than "open data" ever was, and it is also a narrower one: MIT covers the
repository's contents as distributed; it is not a statement about the BNCC curriculum as a public instrument.

### 🟢 Licence-text controls — the fetch channel is byte-faithful, and one project differs by exactly one byte

| control | repos | bytes | sha | finding |
|---|---|---|---|---|
| FSF GPL-3.0, unmodified | `moodle/moodle` (`COPYING.txt`), `chamilo/chamilo-lms`, `ILIAS-eLearning/ILIAS` | 35,147 | `8ceb4b9ee5ad` | 🟢 three unrelated projects **byte-identical** |
| FSF GPL-3.0 less final newline | `h5p/h5p-php-library` | 35,146 | `c53a65c2fd56` | 🟢 `diff` says line 674, *"No newline at end of file"* — **one byte, not a modified licence** |
| Apache-2.0, unmodified | `yetanalytics/lrsql`, `pelotech/xapi-lrs` | 11,357 | `c71d239df917` | 🟢 byte-identical across two unrelated projects |
| AGPL-3.0 | `frappe/lms` 33,893 · `overhangio/tutor` 34,523 · `openedx` 35,136 · `canvas-lms` 34,520 | 🔴 four different | — | 🔴 **no AGPL control exists** — four byte counts, so a byte count alone can never identify AGPL-3.0 here |

🔵 **Why this is worth a table.** `Gap 468-A` requires the *file* to be measured rather than the response, and the
risk in that method is a channel that silently alters bytes. 🟢 Three byte-identical GPL-3.0 payloads from three
unrelated owners rule that out. 🔴 The AGPL row is the warning: this base cannot use byte count as a licence
fingerprint for AGPL, so every AGPL row needs its first line read, and `frappe/lms` at 33,893 B is **not**
evidence of a trimmed or custom AGPL.

### 🟡 `sakaiproject/sakai` is ECL-2.0, and the payload says what that means

🔵 [sakaiproject/sakai](https://github.com/sakaiproject/sakai) · `LICENSE` · 11,120 B · `0688f62d04f1`. The
payload's own line 10 describes ECL-2.0 as *"the Apache 2.0 license, modified to change the scope of the patent
grant in section 3"*. 🟢 **Permissive, and copyleft-free.** 🔴 **But the patent grant is narrower than
Apache-2.0's**, which is the entire point of the modification and is a fact no comparison table in the secondary
literature carries. 🔵 For a studio, ECL-2.0 is usable like Apache-2.0 on the copyright axis and should be read by
counsel on the patent axis — the difference is deliberate and it is in the text.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 478-J`** | **`Gap 477-O` stands: no depth or scope probe ran on any row this pass.** The ten infrastructure rows are graded `WHOLE_WORK` by assumption, the same assumption `Gap 475-J` objected to, and the seven platform rows still have no depth probe. |
| 🔴 **`Gap 478-K`** | **Only `tutor`'s election was probed.** The nine other permissive rows make the question moot, but `frappe/lms`'s AGPL-3.0 election, `openedx`'s and `canvas-lms`'s are **unread**, and `frappe/lms` is the one where a studio would most want the answer. `openeducat_erp`'s payload names *"Version 3"* in prose with no election clause located. |
| 🔴 **`Gap 478-L`** | **`Gap 477-P` is unchanged: BigBlueButton's per-source-file notice is still unread.** Its `LICENSE` reproduced at 7,652 B · `e3a994d82e64`, matching `p477`'s byte count exactly, so the LGPL-3.0 reading is now two-pass consistent — but it still rests on one `LICENSE` plus one module's `build.sbt`. |
| 🟡 **`Gap 478-M`** | **The ten infrastructure rows carry no HEAD or digest**, repeating `Gap 477-Q` verbatim. Their grants are measured and addresses resolved; no byte-level control of the *code* was stored, so the next pass still cannot difference them. |
| 🟡 **`Gap 478-N`** | **`pykt-toolkit` and `EduKTM` are published on grant and description only.** Neither was installed, run, or benchmarked, and neither star count was read — so "two permissive knowledge-tracing libraries exist" is established while "either is maintained or usable" is not. `pykt-toolkit`'s copyright year is 2022. |
| 🟡 **`Gap 478-O`** | **The ECL-2.0 patent reading is this pass's reading of the licence text**, not advice. The payload states the modification; its practical scope for a commercial deliverable was not determined and cannot be determined here. |

---

## 🆕 `p477` — `2026-10-27` — **🟢 BOTH REMAINING ELECTION GAPS ARE CLOSED, AND `Gap 476-G`'s CAUSE IS NOT THE ONE IT GUESSED: OpenOLAT has NO parent POM, its root POM DOES declare the licence, and p476's extractor failed because the project MISSPELLS its own licence name as `L6icense`. 🟢 BigBlueButton's election is found in a module `build.sbt` — a bare `LGPL-3.0`. 🔴 And the tier below the platforms turns out to be the opposite shape: 10 of 12 infrastructure repos are permissive while 8 of 11 platforms are copyleft.**

🔵 Gate posture unchanged from the agents shelf (`Code from External`; `make hooks` not attempted;
session-local checks green). Grants are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p477.tsv`](../evidence/grant-payload.2026-10-27-p477.tsv) (27 rows this
pass); elections in
[`evidence/version-election.2026-10-27-p477.tsv`](../evidence/version-election.2026-10-27-p477.tsv).

---

### 🟢 `Gap 476-G` closed — and the diagnosis is a typo in the project, not a limit in the reader

🔵 `Gap 476-G` supposed two things: that the extractor was the limitation, and that *"a Maven POM can declare the
licence in a parent POM this pass did not follow"*. 🔴 **Both are wrong**, and one `grep` settles it.

| question | measured on `OpenOLAT/OpenOLAT` `master/pom.xml` (86,049 B) |
|---|---|
| is there a `<parent>` to follow? | 🔴 **`grep -c '<parent>'` → 0.** There is no parent POM. |
| does the root POM declare a licence? | 🟢 **Yes** — a full `<licenses><license>` block with the Apache-2.0 URL. |
| what is the declared `<name>`? | 🔴 **`Apache 2.0 Open Source L6icense`** — *sic*, digit `6` where the letter `l` belongs. |
| is there an election to read? | 🟢 **N/A.** Apache-2.0 has no `or-later`/`only` concept. |

🟢 **So the row was never unprobed — it was unmatchable.** Any extractor looking for the token `License` cannot
match `L6icense`. 🔵 The practical lesson for this base's readers: **match on the licence URL, not the licence
name**, because the URL is machine-generated and the name is typed by a human. OpenOLAT's
`http://www.apache.org/licenses/LICENSE-2.0` was correct all along.

### 🟢 `Gap 476-K` closed — BigBlueButton's election exists, one module deep

🔵 `Gap 476-K`: *"`bigbluebutton` has no root packaging file, so its version election is unprobed — the only live
foundation row with no election evidence of any kind."* 🟢 The premise checks out and the conclusion does not.

| channel | result |
|---|---|
| root `build.gradle` · `build.sbt` · `pom.xml` · `package.json` | 🔴 **all 404** — `Gap 476-K`'s premise confirmed |
| `LICENSE` payload (7,652 B) | **GNU LESSER GENERAL PUBLIC LICENSE Version 3** — names v3, silent on future versions |
| 🟢 `bbb-common-web/build.sbt` line 99 | `licenses := Seq("LGPL-3.0" -> url(...))` — 🟡 **bare deprecated id, no election** |
| per-source-file notice | 🔴 2 candidate paths probed, both 404 — path guessing failed (`api.github.com` is 403, so no tree listing) |

🔵 **Tally moved:** the *"bare deprecated id, no election recorded"* bucket is now **3** — `canvas-lms`,
`h5p-php-library` and **`bigbluebutton`** — and the *"unreadable on every channel"* bucket stays at 2
(`openedx-platform`, `echo-loop/Echo-Loop`). OpenOLAT leaves the unprobed set as **N/A**, not unknown.

### 🔴 The structural finding: the platforms are copyleft, the tier beneath them is not

🔵 This base has always tabulated education platforms. It has never tabulated the **infrastructure and
standards** tier those platforms sit on. Twelve such repos, every grant read first-hand this pass:

| repo | ★ | grant (payload, first-hand) | bytes | role |
|---|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 8,360 | 🟢 **BSD-3-Clause** | 1,475 | multi-user notebook server — the CS-teaching backbone |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 4,117 | 🟢 **MIT** | 1,079 | FSRS scheduler — the state of the art in spaced repetition |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 1,374 | 🟢 **BSD-3-Clause** | 1,512 | assign and autograde notebooks |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 1,143 | Apache-2.0 (carried) | — | ERP/CRM substrate for institutional back office |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 1,131 | 🔴 **AGPL-3.0** | 34,523 | the Docker Open edX distribution — *the* way Open edX is deployed |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 822 | 🟢 **MIT** | 1,091 | interactive exercises with automated feedback (TUM) |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 452 | 🟢 **MIT** | 1,066 | deep knowledge-tracing benchmark library |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 373 | 🟢 **Apache-2.0** | 11,361 | LTI 1.3 tool provider — how anything plugs into an LMS |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 359 | 🟢 **MIT** | 1,072 | modern SCORM runtime (1.2 / 2004) |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | 355 | 🟢 **MIT** | 1,084 | source-code plagiarism detection |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 291 | 🟢 **MIT** | 1,132 | Bayesian Knowledge Tracing (UC Berkeley) |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 144 | 🟢 **Apache-2.0** | 11,357 | SQL Learning Record Store — xAPI storage |

🟢 **10 of 12 are MIT / Apache-2.0 / BSD-3-Clause.** Set that against the platform tier, where 8 of 11 rows are
GPL/AGPL/LGPL. 🔴 **The one trap in this tier is `overhangio/tutor` at AGPL-3.0** — and it is the component most
likely to be reached for first, because it is how Open edX actually gets deployed.

🔵 **What this changes for a studio:** the layer where a client's differentiating code lives — tracing, scheduling,
grading, LTI plumbing, record storage — is permissive end to end. The copyleft sits in the *platform* and in the
*deployment wrapper*, both of which are **deployed, not linked**. That is the licensing basis for every recipe on
`compose/patterns.md`, and it is now measured rather than assumed.

### Declared gaps

| gap | what is not known |
|---|---|
| 🔴 **`Gap 477-N`** | **No election was probed for any of the 12 new infrastructure rows.** Permissive grants make the `or-later` question moot for 10 of them, but `overhangio/tutor`'s AGPL-3.0 election is **unread**, and it is the one row in the tier where the answer would matter. |
| 🔴 **`Gap 477-O`** | **`Gap 476-F` is still open: 7 platform rows have no depth probe.** This pass scope-probed none. The `SPLIT_SCOPE` hit rate remains 1 of 2 examined, and the 12 new rows were graded `WHOLE_WORK` by assumption — exactly the assumption `Gap 475-J` objected to. |
| 🔴 **`Gap 477-P`** | **BigBlueButton's per-source-file notice is still unread**, so its election rests on one module's `build.sbt`. `Gap 476-C`'s objection — that a single-channel election is one declaration in one file, and a packaging licence field is routinely wrong in ways a `LICENSE` file is not — now applies to BBB too. |
| 🟡 **`Gap 477-Q`** | **The 12 infrastructure rows carry no HEAD or digest**, unlike the platform rows above them. Their grants were read and measured; their addresses were resolved; but no byte-level control was stored, so next pass cannot difference them. |
| 🟡 **`Gap 477-R`** | **"10 of 12 permissive vs 8 of 11 copyleft" compares two sets this base chose**, not two populations. The infrastructure tier was assembled this pass from addresses already in history; a differently drawn tier could give a different ratio. |

---


## 🆕 `p476` — `2026-10-27` — **🔴 THIS BASE HAS BEEN PUBLISHING A STALE ADDRESS FOR OPEN edX SINCE ITS EARLIEST PASSES: the project is `openedx/openedx-platform`, not `openedx/edx-platform`. The old address still serves git and raw — GitHub forwards renames transparently on both — so every prior pass's content was CORRECT while its link was WRONG. 🟢 `Gap 475-K` is closed: all ten foundation rows now carry a first-hand star count, and the tier is far smaller than the agent tier.**

🔵 Gate posture unchanged from the agents shelf (`Code from External`; `make hooks` not attempted;
session-local checks green). Grants and metadata are the first-hand reads in
[`evidence/grant-payload.2026-10-27-p476.tsv`](../evidence/grant-payload.2026-10-27-p476.tsv) and
[`evidence/version-election.2026-10-27-p476.tsv`](../evidence/version-election.2026-10-27-p476.tsv).

---

### 🔴 The address correction, and the new instrument that caught it

🔵 `Gap 475-H` found a wrong address by **non-resolution** (`openeducat/openeducat` did not resolve at all).
That instrument cannot catch a *rename*, because a renamed repository resolves perfectly at its old address.
🟢 This pass caught one with a different instrument: **absence from the search index.**

| channel | `openedx/edx-platform` (the carried address) | `openedx/openedx-platform` (the real one) |
|---|---|---|
| `git ls-remote --symref` | 🟢 resolves — `master` · `03698e2b6ff4` | 🟢 resolves — `master` · `03698e2b6ff4` |
| `raw.githubusercontent.com` `master/LICENSE` | 🟢 200 — 35,136 B · `e12d78569742` | 🟢 200 — 35,136 B · `e12d78569742` |
| authenticated search, `repo:` qualifier | 🔴 **Validation Failed** — *"the listed repositories cannot be searched"* | 🟢 returns the repo — **8,211★** |
| `org:openedx edx-platform in:name` | 🔴 **0 results** | 🟢 returned as `openedx/openedx-platform` |

🟢 **The proof the two addresses are one repository: identical HEAD and a byte-identical grant payload at
both**, and `e12d78569742` is the exact digest `p475` recorded. 🔴 **The proof the carried address is stale:**
git and raw forward renames silently, the search index does not. An `org:openedx` listing returns 175
repositories and the platform is in it under the **`openedx-platform`** name only.

🔵 **This generalises into a cheap, repeatable check, and it was run as a sweep this pass:** every address on
the agents and foundation shelves was put through the `repo:` qualifier. **22 addresses swept, exactly 1
stale.** A repository that resolves on git but is unsearchable has been renamed; a repository that resolves
on neither is gone. 🔴 Neither `curl -sI` (blocked, `Gap 472-A`) nor `ls-remote` can distinguish these, which
is why two passes missed this one.

### 🟢 The foundation tier — 10 real rows, every grant and every star read first-hand

🔵 `★` read `2026-10-27` from the authenticated channel. **Default branches re-resolved this pass: all ten
match `p475`.** 🟡 **HEADs are a different matter — `sakaiproject/sakai` moved** from `849cc0d9f991` to
`9962d2bc808b` between the two passes. Its grant was re-fetched at the new HEAD and is **unchanged**
(`master/LICENSE` · 11,120 B · `0688f62d04f1`), so the row below carries the **new** HEAD and a grant
verified against it. The other nine HEADs reproduce `p475` exactly.

| repo | ★ (first-hand) | default branch · HEAD | grant path · bytes · digest | grant read | version election (`p476`) | build-on-able |
|---|---|---|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 9,255 | `v4.0.x-develop` · `4eabedfb8045` | `…/LICENSE` · 7,652 B · `e3a994d82e64` | **LGPL-3.0** | not probed (no root packaging file) | 🟡 weak copyleft |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 8,211 | `master` · `03698e2b6ff4` | `master/LICENSE` · 35,136 B · `e12d78569742` | **AGPL-3.0** | 🔴 **UNREADABLE, all channels** | 🔴 network copyleft |
| [moodle/moodle](https://github.com/moodle/moodle) | 7,550 | `main` · `46c042e7da65` | `main/COPYING.txt` · 35,147 B · `8ceb4b9ee5ad` | **GPL-3.0** | 🟢 **`GPL-3.0-or-later` elected** (2 channels) | 🔴 copyleft |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 6,890 | `master` · `1c9f0bb8013e` | `master/LICENSE` · 34,520 B · `57c8ff33c9c0` | **AGPL-3.0** | 🟡 bare id, no election | 🔴 network copyleft |
| [frappe/lms](https://github.com/frappe/lms) | 3,351 | `develop` · `11b6244724b7` | `develop/license.txt` · 33,893 B · `db1a87ba81e8` | **AGPL-3.0** | 🟢 **`AGPL-3.0-or-later` elected** (1 channel) | 🔴 network copyleft |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 1,240 | `master` · `9962d2bc808b` | `master/LICENSE` · 11,120 B · `0688f62d04f1` | **ECL-2.0** | 🟢 `pom.xml` agrees with payload | 🟢 **YES** (narrowed patent grant, `p474`) |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 1,162 | `develop` · `f72936bd41e5` | `develop/LICENSE` · 1,097 B · `3c056b34a476` | **MIT** | 🟢 `package.json` agrees with payload | 🟢 **YES** |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 899 | `19.0` · `46a5d7d40082` | `19.0/LICENSE` · 8,241 B · `528f84036800` | **LGPL-3.0** | 🟢 **`LGPL-3.0-or-later` elected** (187 of 209 files) | 🟡 weak copyleft |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 448 | `master` · `aac489d1d429` | `master/LICENSE` · 10,982 B · `6dbc5b605ed0` | **Apache-2.0** | `pom.xml` carries no extractable licence name | 🟢 **YES** |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 152 | `master` · `1e21b7a2da4a` | `master/LICENSE.txt` · 35,146 B · `c53a65c2fd56` | **GPL-3.0** | 🟡 bare id, no election | 🔴 copyleft |

🔴 **The tier is 8-of-10 copyleft, unchanged from `p475` — reading the elections did not make any row more
permissive.** What the elections changed is the *shape* of the copyleft: three rows are now known to be
`or-later` (a downstream user may move to a future GPL/AGPL/LGPL), two carry bare deprecated ids, and
Open edX's is unrecorded anywhere reachable.

### 🟢 A structural fact `Gap 475-K` was blocking, now measurable

| tier | total ★ | rows |
|---|---|---|
| all ten foundation platforms combined | **39,158** | 10 |
| `HKUDS/DeepTutor` alone | **44,531** | 1 |

🟢 **One education-AI agent outstars the entire open-source education platform tier by 1.14×.** 🔴 **Stars
measure developer attention, not deployment**, and this comparison is the clearest available proof: Moodle
has 7,550★ and runs a large share of the world's institutional LMS installs, while DeepTutor has 44,531★ and
is ten months old. 🔵 For a studio the inversion is the point — the platforms a client already runs are
*under*-represented in open-source attention, and the agents are *over*-represented relative to installed
base. Neither number is a demand signal on its own.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 476-E`** | **Every other address in retained history is unswept.** 22 addresses on the two live shelves were put through the rename detector; the hundreds of addresses in history below were not. Given a 1-in-22 hit rate on the *current* shelves, history likely carries more stale addresses, and nothing here has measured how many. |
| 🔴 **`Gap 476-F`** | **`Gap 475-J` is only partly answered.** `p475` graded 9 of 10 foundation rows `WHOLE_WORK` by assumption. This pass scope-probed exactly one further repo (`openeducat_erp`, by clone) and read packaging metadata for four more; **`bigbluebutton` was not scope-probed at all** (no root packaging file found), and seven rows still have no depth probe. The `SPLIT_SCOPE` hit rate remains 1 of 2 examined. |
| 🟡 **`Gap 476-G`** | **`OpenOLAT`'s `pom.xml` yielded no licence name** to the extractor used here, so its Apache-2.0 is payload-only and its election is unprobed. The extractor, not the project, is the likely limitation — a Maven POM can declare the licence in a parent POM this pass did not follow. |
| 🟢 **`Gap 475-K` closed** | All ten rows carry a first-hand star count, read `2026-10-27`. |

## 🆕 `p475` — `2026-10-27` — **🔴 THE EDUCATION FOUNDATION TIER IS 8-OF-10 COPYLEFT WHEN YOU READ THE PAYLOADS INSTEAD OF THE BADGES, and the two permissive exceptions are the two smallest. 🟢 Every grant below was fetched, written to a file and measured this pass; two of them had been readable all along at filenames this base's probe never asked for.**

🔵 Same gate posture as the agents shelf: `make hooks` **not attempted** (`Code from External`);
checks re-implemented in session-local code and green. Evidence:
[`evidence/grant-payload.2026-10-27-p475.tsv`](../evidence/grant-payload.2026-10-27-p475.tsv).

### 🟢 The foundation tier, 10 real rows, every grant read first-hand at a resolved HEAD

| repo | default branch · HEAD | grant path · bytes · digest | grant read | 🟢/🔴 build-on-able |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `main` · `46c042e7da65` | `main/COPYING.txt` · 35,147 B · `8ceb4b9ee5ad` | **GPL-3.0** | 🔴 copyleft |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | `master` · `03698e2b6ff4` | `master/LICENSE` · 35,136 B · `e12d78569742` | **AGPL-3.0** | 🔴 network copyleft |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | `master` · `1c9f0bb8013e` | `master/LICENSE` · 34,520 B · `57c8ff33c9c0` | **AGPL-3.0** | 🔴 network copyleft |
| [frappe/lms](https://github.com/frappe/lms) | `develop` · `11b6244724b7` | `develop/license.txt` · 33,893 B · `db1a87ba81e8` | **AGPL-3.0** | 🔴 network copyleft |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `master` · `1e21b7a2da4a` | `master/LICENSE.txt` · 35,146 B · `c53a65c2fd56` | **GPL-3.0** | 🔴 copyleft |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | `v4.0.x-develop` · `4eabedfb8045` | `…/LICENSE` · 7,652 B · `e3a994d82e64` | **LGPL-3.0** | 🟡 weak copyleft |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | `19.0` · `46a5d7d40082` | `19.0/LICENSE` · 8,241 B · `528f84036800` | **LGPL-3.0**, 🔴 `SPLIT_SCOPE` | 🟡 weak copyleft, bundled libs disclaimed |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | `master` · `849cc0d9f991` | `master/LICENSE` · 11,120 B · `0688f62d04f1` | **ECL-2.0** | 🟢 **YES** (narrowed patent grant, `p474`) |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `develop` · `f72936bd41e5` | `develop/LICENSE` · 1,097 B · `3c056b34a476` | **MIT** | 🟢 **YES** |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | `master` · `aac489d1d429` | `master/LICENSE` · 10,982 B · `6dbc5b605ed0` | **Apache-2.0** | 🟢 **YES** |

🔴 **The census, stated as a number:** 10 platforms, **3 build-on-able without a copyleft obligation**
(Sakai ECL-2.0, Kolibri MIT, OpenOLAT Apache-2.0), 2 weak-copyleft, 5 strong or network copyleft.
🟢 This **confirms** `p469`'s permissive-foundation census on re-measurement, and `p469`'s exact star
figures reproduce first-hand: `OpenOLAT` **448★** (`p469`: 448★) and `frappe/lms` **3,351★** (`p469`: 3,350★).

### 🔵 Where the permissive three actually differ, because "permissive" is not one thing

| platform | grant | the real constraint a studio hits |
|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 🟢 Cleanest. Express patent grant, no copyleft. Java/JEE — the cost is operational, not legal |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 🟢 Cleanest legally, **but no patent grant at all** — MIT is silent on patents. Offline-first is its real differentiator |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | 🟡 Apache-2.0 **with the patent grant narrowed** to the contributor's own contributions (`p474`, `Gap 473-B`) — the narrowing bites exactly where a university consortium contributes back |

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 475-J`** | **Nine of these ten rows are graded `WHOLE_WORK` by assumption, not by reading.** Only `openeducat_erp` was scope-read this pass, and it came back `SPLIT_SCOPE` on the first look — a **1-for-1 hit rate** on the only row examined. That is the strongest available evidence that `Gap 474-A`'s backfill matters, and it still has not been run across the shelf. |
| 🟡 **`Gap 475-K`** | **No star count is published for 7 of these 10 rows.** The authenticated channel returns stars only for repos named in a `repo:` query, and this pass spent that budget on the agents shelf. Magnitude for the foundation tier is therefore **unmeasured this pass**, not estimated — no web-relayed figure was substituted. |


## 🆕 `p474` — `2026-10-27` — **🔴 LATIN AMERICA'S PUBLIC-SECTOR EDUCATION DATA IS PUBLISHED WITHOUT A GRANT: a municipal education secretariat and a national education ministry both ship their open data UNGRANTED at all 14 probed paths, so the most authoritative education data in the region is the data an engagement may not use. 🟢 And the Brazilian school-management vendor stack is now mapped end to end — four components, THREE DIFFERENT COPYLEFT TRIGGERS, one of them rendered in Portuguese.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — KB cloned outside the harness
repo. **Nothing below is gate-attested.** Every address resolved first-hand (`git ls-remote
--symref`); every grant read first-hand from `raw.githubusercontent.com`, body written to a file and
the file measured (`Gap 468-A`). Stars index-relayed from MCP `search_repositories`, **2026-10-27**
(`Gap 467-D`). 🔴 `curl -sI` not used — dead on this harness (`Gap 472-A`).

### 🔴 The ungranted public sector — measured, and the most actionable row on this shelf

| Repo | Grant | ★ | Region | What it holds, and why the grant matters |
|---|---|---|---|---|
| [prefeiturasp/dados-educacao](https://github.com/prefeiturasp/dados-educacao) | 🔴 **UNGRANTED** — 14 paths probed on `master` | 57 | LATAM | Open-data analyses and tutorials from the **São Paulo Municipal Education Secretariat** — the largest municipal school system in the Americas. 🔴 Published as open data, licensed as nothing |
| [mecpy/mec-opendata](https://github.com/mecpy/mec-opendata) | 🔴 **UNGRANTED** — 14 paths probed on `master` | 11 | LATAM | **Paraguay's Ministry of Education and Culture** open-data portal. 🔴 Same shape, national rather than municipal |

🔴 **Why this is not a nitpick.** "Open data" from a public body reads as free to use, and a
procurement review will ask for the grant. Neither repository states one, so neither can be
vendored into a client deliverable on the strength of the repository alone — the terms, if they
exist, live in a portal's terms of use, not in the artifact. 🔵 **The engagement move is to treat
these as read-only reference and to source the licensed equivalent** — which, for curriculum, is
[`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (**MIT**, `main/LICENSE` 1,092 B
`e162f8f4b461`), and for admissions-grade public data
[`agn3si/ResultadosUNAM---data`](https://github.com/agn3si/ResultadosUNAM---data) (**MIT**, 1,063 B
`13e4dd489fe9`) and [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) (**MIT**,
1,070 B `277707dcaa3b`).

### 🟢 The Brazilian school-management stack, mapped — one vendor, three copyleft triggers

| Component | Repo | Grant (path read · bytes · digest) | ★ | Trigger |
|---|---|---|---|---|
| School information system | [portabilis/i-educar](https://github.com/portabilis/i-educar) | **GPL-2.0-or-later** — `2.12/LICENSE` · 18,092 B · `8177f9751321` | 721 | 🟡 distribution |
| Gradebook / class diary | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0-or-later** — `1.6/LICENSE` · 35,326 B · `fe85f94658bf` *(Portuguese payload)* | 117 | 🔴 **network use** |
| Enrolment + waiting lists | [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) | 🔴 **AGPL-3.0-or-later** — `2.12/LICENSE` · 35,326 B · `fe85f94658bf` *(Portuguese payload)* | 21 | 🔴 **network use** |
| School-management (independent vendor) | [ipti/br.tag](https://github.com/ipti/br.tag) | **GPL-2.0-or-later** — `main/LICENSE` · 18,027 B · `111e1f411730` | 20 | 🟡 distribution |

🟢 **New this pass: the enrolment module, and it is AGPL — identical bytes AND digest to the
gradebook's Portuguese payload.** So **two of the three Portabilis components carry the
network-use trigger**, and the pattern is the vendor's default rather than one component's choice.
🔴 An AI enrolment-triage or attendance agent that calls either over a network is inside the AGPL
boundary; the boundary, not the model, is the architecture decision.

🟢 **`p473`'s 18 KB GNU size band reproduces, on a different vendor.** `ipti/br.tag` serves
**18,027 B** against `i-educar`'s **18,092 B** — 65 B apart, both GPL-2.0-or-later. 🔵 `p473` noted
it had never observed a GNU payload below 34 KB before `i-educar`; this is the **second**
observation, from an unrelated organisation, so the band is real. 🔴 It remains provenance only —
[`Gap 466-C`](../intel/open-gaps.md) holds and **no code path in this pass's reader touches
`bytes`.**

### 🟢 Public-education delivery assets added — Spanish-speaking LATAM, which `Gap 473-G` had written off

| Repo | Grant (path read · bytes · digest) | ★ | Region | Role |
|---|---|---|---|---|
| [datauy/ElijoEstudiar](https://github.com/datauy/ElijoEstudiar) | **GPL-3.0-or-later** — `master/LICENSE` · 35,149 B · `3972dc9744f6` | 5 | LATAM | 🟢 **Uruguay**: search and visualisation across public initial, primary and secondary education centres and courses. A real public-education product, not course material |
| [prefeiturasp/SME-PratoAberto-Edu](https://github.com/prefeiturasp/SME-PratoAberto-Edu) | **GPL-3.0-or-later** — `master/LICENSE` · 35,141 B · `589ed823e9a8` | 9 | LATAM | 🟢 **São Paulo's municipal education chatbot** — a deployed conversational public-service channel in a school system, predating the LLM wave. The integration surface an AI layer would replace |
| [gpassero/uol-redacoes-xml](https://github.com/gpassero/uol-redacoes-xml) | 🟢 **Apache-2.0** — `master/LICENSE` · 11,357 B · `b40930bbcf80` | 39 | LATAM | Brazilian essay corpus in XML as a test and validation set for automated writing assessment |
| [huseyingulsin/Acik-Kaynak-Bilgisayar-Bilimleri](https://github.com/huseyingulsin/Acik-Kaynak-Bilgisayar-Bilimleri) | 🟢 **MIT** — `main/LICENSE.md` · 1,074 B · `050d076b61bd` | 254 | EMEA | Turkish-language open computer-science curriculum — the highest-starred Turkish education asset found. 🔵 Curriculum, **not** infrastructure; it is on this shelf as content, and the distinction is the point |
| [Turkish-AI-Community/hsd-agu-egitim](https://github.com/Turkish-AI-Community/hsd-agu-egitim) | 🟢 **MIT** — `main/LICENSE` · 1,073 B · `2f311e0a9f67` | 33 | EMEA | Agentic-RAG bootcamp materials from the Turkish AI Community — the EMEA in-language teaching-material tier |

🔵 **`LICENSE.md` matters.** The Turkish curriculum grants at `LICENSE.md`, not `LICENSE` — so
`Gap 472-B`'s widened 14-path probe set earns its keep again this pass, on a path **case** rather
than on lowercase.

### 🟡 One provenance note, because `p467` proved size screens nothing

🔵 `gpassero/uol-redacoes-xml` serves an Apache-2.0 payload of **11,357 B** — the **same byte count**
as `yetanalytics/lrsql`'s Apache-2.0 on [`p473`'s shelf](../repos/foundations.md), with a
**different digest** (`b40930bbcf80` vs `c71d239df917`). 🟢 Third demonstration on this base that
identical size is not identity and that the digest is the only provenance claim worth printing.

## 🆕 `p473` — `2026-10-27` — **🟢 `Gap 467-I` IS CLOSED AND ITS PREMISE IS REFUTED: the learning-record / analytics tier is not copyleft-only, it is the MOST PERMISSIVE TIER THIS BASE HAS MEASURED — 5 of 9 rows permissive (55.6 %) against the agent tier's 42.9 %, including an MIT Learning Record Store. 🔴 And a permissive licence on these shelves has been carrying a clause nobody here has graded: ECL-2.0's patent grant is NARROWER than the Apache-2.0 it is derived from, by design and in writing.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — KB cloned outside the harness
repo. **Nothing below is gate-attested.** Every address resolved first-hand (`git ls-remote
--symref`); every grant read first-hand from `raw.githubusercontent.com`, body written to a file and
the file measured (`Gap 468-A`). Stars from MCP `search_repositories`, **2026-10-27**, and
**index-relayed, never first-hand** (`Gap 467-D`).
🔴 `curl -sI` not used for verification — dead on this harness (`Gap 472-A`).

### 🟢 `Gap 467-I` — what it said, and what the payloads say

🔵 The gap read: *"No permissive row exists at the LRS / learning-analytics tier. The only Learning
Record Store carried (`g3i/lxHive`) is GPL-2.0-or-later, so an xAPI analytics component cannot enter
a proprietary deliverable from these shelves."* 🟢 Its closure contract was to **probe the
xAPI / `caliper` / LRS vocabulary and grade every hit.** Run, graded, and the conclusion inverts.

| Repo | Grant (path read, bytes, digest) | Stars | Region | Role, and what it is for |
|---|---|---|---|---|
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** — `main/LICENSE`, 11,357 B `c71d239df917` | 144 | North America | 🟢 **A SQL-backed Learning Record Store** — Postgres/SQLite rather than a document store. Pushed **today** (`61594164edf5`). **The default LRS pick:** permissive, actively maintained, and it lands xAPI statements in a database a client's BI team already knows how to query |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** — `master/LICENSE`, 11,357 B `58d1e17ffe51` | 334 | North America | The **reference** LRS from the ADL Initiative, the body that authored the Experience API itself. 🔵 Use it as the conformance oracle to test against, even when shipping another |
| [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** — `main/LICENSE.md`, 1,094 B `08ea77291de9` | 51 | EMEA | 🟢 **An MIT-licensed LRS and learning-analytics pipeline** from **France Université Numérique**: FastAPI + Pydantic validation, Elasticsearch/ClickHouse backends, stream processing, a CLI. Pushed **today** (`91fef112394d`). 🔴 Its grant lives at `LICENSE.md`, not `LICENSE` — a root-path probe that stops at `LICENSE` publishes this row as ungranted |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 **ECL-2.0** — `master/LICENSE`, 9,878 B `f339063d2f60` | 62 | North America | A standards-based learning-record **warehouse** speaking **xAPI, IMS Caliper and OneRoster** together — the only row here that bridges all three. 🔴 **Read the patent note below before building on it** |
| [tl-its-umich-edu/my-learning-analytics](https://github.com/tl-its-umich-edu/my-learning-analytics) | 🟢 **Apache-2.0** — `master/LICENSE`, 11,379 B `b89b380a589b` | 37 | North America | **MyLA**, University of Michigan: student-facing analytics dashboards (resource access, assignment planning, grade distribution) running against an LMS. 🟢 The *consumer* end of the pipeline, permissive — so a studio can restyle and extend the dashboards for a client |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** — `development/LICENSE`, 11,323 B `6dc0e068dcf3` | 21 | North America | 🟢 **Randomised controlled trials inside a live LMS, over LTI**: assignment content differentiated by experimental condition, random assignment to arms, informed consent hidden from the teacher, non-consenting participants filtered from exports, identifiers stripped. 🔵 **This is the apparatus for proving an AI intervention worked** — and it is permissive. See `compose/patterns.md` `P473-3` |
| [PlaypowerLabs/EdOptimize](https://github.com/PlaypowerLabs/EdOptimize) | 🟡 **GPL-3.0-or-later** — `master/LICENSE`, 35,149 B `3972dc9744f6` | 31 | APAC | K-12 learning-analytics platform in R: curriculum analytics, content usage, assessment dashboards. 🔴 Distribution copyleft — run it as an internal analysis tool, do not ship it |
| [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) | 🟡 **GPL-3.0-or-later** — `master/LICENSE`, 35,141 B `589ed823e9a8` | 585 | EMEA | The best-known open LRS (Learning Pool, UK/IE), **started 2014**. 🔴 **Last push 2024-05-30** — the highest-★ row in this tier is also the stalest. Named for recognition, not recommended |
| [g3i/lxHive](https://github.com/g3i/lxHive) | 🟡 **GPL-2.0** — carried from prior passes | 79 | APAC | The row `Gap 467-I` was written about. It is real and it is copyleft; it was never the whole tier |

### 🟢 The tier, stated as a number — and the comparison that makes it matter

| grant class | rows | share |
|---|---|---|
| 🟢 Permissive (Apache-2.0 ×4, MIT ×1) | 5 | **55.6 %** |
| 🟢 ECL-2.0 (permissive, narrowed patent grant) | 1 | 11.1 % |
| 🟡 GPL-2.0 / GPL-3.0 | 3 | 33.3 % |
| 🔴 Ungranted | **0** | **0 %** |

🟢 **Zero ungranted rows in nine.** Against the agent tier (14.3 % ungranted, `p472`) and this pass's
evaluation tier (**44.4 %** ungranted, `agents/top.md`), the infrastructure tier is the only shelf in
this KB where a studio can pick by capability and not have the grant decide for it. 🔵 The reading:
**standards-driven tiers are licensed tiers.** xAPI, Caliper and OneRoster are consortium
specifications, and a project built to be interoperable is built to be adopted — which means it
carries a grant.

### 🔴 The new axis this pass is forced to open: ECL-2.0 is permissive, and its patent grant is not Apache's

🔵 Two ECL-2.0 payloads were read first-hand and they are **1,242 B apart** — `OpenLRW` at 9,878 B
`f339063d2f60`, [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) at 11,120 B
`0688f62d04f1` (the same text with an SPDX-style title line prepended). 🔵 Another clean
reproduction of *size identifies nothing*, on a family this base had never graded first-hand.

🔴 **But the substance is the finding.** The payload states its own derivation in its second
paragraph:

> *"The Educational Community License version 2.0 ("ECL") consists of the Apache 2.0 license,
> **modified to change the scope of the patent grant in section 3 to be specific to the needs of the
> education communities** using this license."*

🔴 **So ECL-2.0 is not "Apache-2.0 with a different name."** It is OSI-approved and permissive on
copyright — modify freely, keep it closed, ship it — and its §3 patent licence is **deliberately
narrower**. 🟢 Operative guidance, stated plainly because this base has been treating ECL as
Apache-equivalent for several passes:

- 🟢 **Copyright-wise, treat ECL-2.0 as permissive.** Sakai and OpenLRW may be forked, modified and
  shipped closed. Nothing on this shelf changes.
- 🔴 **Patent-wise, do not tell a client ECL-2.0 gives them Apache-2.0's patent peace.** Where a
  client's counsel has approved *Apache-2.0* specifically — common in enterprise procurement — ECL-2.0
  is a **different instrument requiring its own review**, and the clause that differs is the one
  procurement cares about.
- 🔵 **Registered as `Gap 473-B`:** every ECL cell on these shelves was graded on the Apache-family
  resemblance of its body. The next pass should re-read §3 of each ECL payload directly and publish
  the patent-scope sentence, rather than inferring it from the family.

### 🔴 Declared gaps on this shelf

- 🔴 **IMS Caliper is one row.** `OpenLRW` is the only Caliper-speaking row found, and the
  `caliper` token on its own returned nothing usable at any star floor. The LRS tier is
  **xAPI-shaped**; a client standardised on Caliper has one option and it is ECL-2.0.
- 🔴 **No LRS row is LATAM- or Africa-origin.** The permissive five are North America ×4 and EMEA
  (France) ×1. 🔵 This sits against the same pass's finding that the only usable *evaluation*
  instruments are West-African and Brazilian — the regional asymmetry **inverts between tiers**, and
  neither direction should be generalised from one pass.
- 🔵 **`Gap 467-D` unchanged:** every star figure above is index-relayed. `api.github.com` → `403`
  on this harness, reproduced once as a control this pass and not retried.

## 🆕 `p472` — `2026-10-27` — **🔴 THE EDUCATION STACK'S LOAD-BEARING CORE IS COPYLEFT AND ITS PERMISSIVE ALTERNATIVES ARE UNDER-KNOWN: Moodle GPL-3.0, Canvas AGPL-3.0, Open edX AGPL-3.0, `frappe/lms` AGPL-3.0 — while Sakai (ECL-2.0), OpenOLAT (Apache-2.0), Oppia (Apache-2.0) and Kolibri (MIT) sit permissive and unmentioned in every vendor comparison searched this pass. 🔴 And `frappe/lms` grants at `develop/license.txt` — a NINTH path, lowercase, absent from the seven-path probe set this base has used for 471 passes.**

🔵 Stars from MCP `search_repositories`, **2026-10-27**. Licence column names the **path read
first-hand** from `raw.githubusercontent.com` and its measured byte count (`Gap 468-A`).
🔴 `curl -sI` not used — dead on this harness, see `Gap 472-A` in `agents/top.md`.

### 🟢 Permissive foundations — what Globant can build on and modify freely

| Repo | Licence (path read, bytes) | Stars | Region | Role in an education build |
|---|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** — `develop/LICENSE`, 11,358 B | **6,944** | Global | Interactive **explorations** engine with built-in misconception handling; the only permissive full learning platform at this scale. 5,855 forks |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** — `master/LICENSE`, 11,120 B | 1,240 | Global | Full higher-ed LMS incl. **gradebook of record**. 🔵 Educational Community License 2.0 is an **Apache-2.0 derivative, OSI-approved and permissive** — the one copyleft-free LMS core with a gradebook |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** — `develop/LICENSE`, 1,097 B | 1,162 | Global | **Offline-first** learning platform for low-connectivity deployment. 🟢 Directly answers the LATAM compute/connectivity gap in `intel/market.md` |
| [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** — `master/LICENSE`, 11,324 B | 808 | North America | Auto-graded programming assignments with course management; CMU-origin |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** — `main/LICENSE.md`, 1,542 B | 804 | North America | Homework submission + automated grading + TA grading. 1,119 forks |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** — `master/LICENSE`, 10,982 B | 448 | EMEA | LMS with **QTI assessment, SCORM, curriculum management, certification**. Swiss-origin, used across DACH higher ed |
| [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** — `main/LICENSE`, 1,094 B | 409 | EMEA | 🟢 **A permissive student information system.** Laravel/Filament school-management platform. Directly fills the gap the vendor comparison searched this pass declared unfillable — *"the results don't identify an open-source SIS under MIT or Apache"* |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** — `master/LICENSE`, 1,072 B | 359 | Global | Modern SCORM 1.2 / 2004 JS runtime, offline-first. 🔵 **The integration seam**: lets an AI layer report completion and scores into any SCORM-consuming LMS without touching the LMS source |
| [openfun/richie](https://github.com/openfun/richie) | 🟢 **MIT** — `master/LICENSE`, 1,079 B | 316 | EMEA | Django CMS for education **portals and catalogues**, front-ends Open edX / Moodle. France Université Numérique-origin |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 🟢 **MIT** — `main/LICENSE`, 1,070 B | — | APAC | Graph-RAG retrieval engine from the lab that ships DeepTutor. 🟢 **Same-lab licence-compatible retrieval layer** under an AI tutor |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | 🟢 **MIT** — `main/LICENSE`, 1,088 B | — | APAC | Multimodal document ingestion (PDF, slides, figures) feeding the same retrieval layer |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | 🟢 **MIT** — `development/LICENSE`, 1,088 B | — | EMEA | Markdown-native course publishing toolchain; Ireland-origin *(carried, re-verified `p472`)* |

### 🟡 Copyleft foundations — real, dominant, and a design constraint

| Repo | Licence (path read, bytes) | Stars | Region | Constraint it imposes |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | 🟡 **GPL-3.0** — `main/COPYING.txt` | **7,549** | Global | The world's most-deployed LMS, 7,684 forks. 🔵 Grant is at **`COPYING.txt`, not `LICENSE`** — a root-path probe that only tries `LICENSE*` publishes NO GRANT on the largest LMS on earth |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🟡 **AGPL-3.0** — `master/LICENSE`, 34,520 B | **6,889** | North America | 🔴 **Network-use copyleft.** Hosting a modified Canvas for a client triggers source disclosure to that client's users |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** — `master/LICENSE`, 35,136 B | — | North America | MIT/Harvard-origin, now Axim Collaborative. 🔵 **Search anomaly recorded honestly:** MCP `search_repositories` returns this address for neither `repo:openedx/edx-platform` nor `edx-platform in:name` (which returns only forks). Existence and grant proved by payload: `master/README.rst` → 200, `master/LICENSE` → 35,136 B AGPL-3.0. **No star count claimed, because none was read** |
| [frappe/lms](https://github.com/frappe/lms) | 🟡 **AGPL-3.0** — 🔴 **`develop/license.txt`** | **3,351** | APAC | 🔴 **A ninth licence path, and a lowercase one.** Absent from all seven root paths this base probes and from the six tried first this pass; `LICENSE.txt`, `LICENSE.md` and `COPYING` all 404. India-origin (Frappe), 1,562 forks. Registered as **`Gap 472-B`**: the probe set must include **lowercase `license.txt` / `license.md`**, because a case-sensitive object store does not fold them |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🟡 **AGPL-3.0** — `release/LICENSE.txt`, 34,523 B | 1,131 | EMEA | The Docker/Kubernetes Open edX distribution — the practical way to run Open edX. France-origin |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🟡 **GPL-3.0** — `master/LICENSE`, 35,147 B | 1,020 | EMEA + LATAM | Accessibility-focused LMS with **strong Spanish-speaking and LATAM deployment base** |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🟡 **GPL-3.0** — `release_11/LICENSE`, 35,147 B | 505 | EMEA | German-origin LMS, heavy public-sector and university use |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🟡 **AGPL-3.0** — `dev/LICENSE`, 34,523 B | 2,424 | Global | AI-oriented next-gen learning platform; headless API |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,523 B | 1,732 | Global | Customer-training platform shape (SaaS companies teaching their users) |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,764 B | 243 | EMEA | Secure automated exercise assessment with an LTI seam to an existing LMS. Belgium (UCLouvain)-origin |

### 🔴 The finding that matters for a proposal

🔵 Of the four LMS cores a client is most likely to already run — Moodle, Canvas, Open edX,
`frappe/lms` — **all four are GPL or AGPL**. Two of them (Canvas, Open edX, plus Tutor) are
**AGPL**, where merely *hosting* a modified build for the client's users triggers disclosure.

🟢 **The permissive escape routes exist and are not in the comparisons.** The vendor LMS comparison
surfaced by this pass's search names Moodle, Open edX, Sakai, ILIAS, Canvas, Chamilo and OpenEduCat
— and **does not state that Sakai is permissive**, nor mention OpenOLAT, Oppia, Kolibri or
Academico at all. For a client that needs to keep modifications closed, the shortlist is
**Sakai (ECL-2.0) · OpenOLAT (Apache-2.0) · Oppia (Apache-2.0) · Kolibri (MIT) · Academico (MIT)**,
and that shortlist appears nowhere in the market literature read this pass.

🔵 **12 permissive foundations and 10 copyleft ones are published above — all 22 grant-verified by
payload this pass.** No row is carried on a prior pass's word except the three marked as carried and
re-verified.

## 🆕 `p471` — **🔴 TWO FOUNDATION-TIER PLATFORMS THIS SHELF REFUSED FOR WANT OF A GRANT ARE GRANTED, and one of them is published as ungranted on the SELL shelf: `particify/arsnova-server` serves **GPL-3.0** at `core/LICENSE` and `formalms/formalms` serves **GPL-2.0** at `html/license.txt`, both read first-hand. 🟢 And foundation selection gains a screen that costs one command and runs BEFORE any licence is read: partition risk is monotonic in tree size, 0.0 % under 25 paths to 66.7 % over 2 000.**

🔵 Gate not attested (`Gap 446-A`); checks re-implemented in-session and green. Every grant read
first-hand from `raw.githubusercontent.com` at the resolved ref, written to a file and the file
measured (`Gap 468-A`). Star counts from the MCP `search_repositories` channel, `2026-10-27`.

### 🔴 The two recoveries, and what they cost this shelf

🔵 Both were refused by a **root-path** probe. Both are granted below the root. Neither is a new
discovery — they are rows this base already carried, with the wrong verdict on them.

| platform | repo | ref | grant found below the root | ★ | what it is |
|---|---|---|---|---|---|
| **forma.lms** | [`formalms/formalms`](https://github.com/formalms/formalms) | `master` `446a77a9b9cb` | 🟢 **GPL-2.0** · `html/license.txt` · 18 346 B · `4e63feff285d`; a second copy at `html/lib/System/license/license_english.txt` · 15 146 B · `81688a796b2f`, with **9 further language translations** beside it | 37 | PHP corporate-training LMS, mirror repository |
| **ARSnova** | [`particify/arsnova-server`](https://github.com/particify/arsnova-server) | `master` `424b2ef60517` | 🟢 **GPL-3.0** · `core/LICENSE` · **35 147 B · `8ceb4b9ee5ad`** | 67 | Kotlin audience-response-system backend; most-forked unlicensed row this shelf carried (44 forks, created 2013) |

🟢 **The ARSnova digest is a cross-pass control passing.** `35 147 B · 8ceb4b9ee5ad` is **this
base's own canonical stock-FSF GPL-3.0 cell** — the value these shelves record for
`moodle/moodle`'s `COPYING.txt` and for Chamilo. It reproduces exactly, from a repository this base
had never read for GPL, which is the strongest evidence available that the payload is the real
licence text and not a fragment.

🔴 **And ARSnova carries a reservation as well as a grant.** `formatting/LICENSE` is **133 B**:
*"Copyright (c) 2020-present Particify — Gerhardt, Mauß, Käsler GbR, Gießen, Germany. All rights
reserved."* Copyright line, reservation, **no permission sentence** — against a BSD-3 body of
~1.5 KB, so the base's own "All rights reserved is BSD boilerplate" warning was checked and does not
apply here. 🔴 **A studio vendoring `arsnova-server` wholesale would ship a module whose author has
reserved all rights.** The usable boundary is `core/` under GPL-3.0, with `formatting/` excluded.

🟡 **The bound, stated with the claim.** A GPL payload carries the **FSF's** copyright, not the
project's, so nothing in `core/LICENSE` names Particify. That it grants the `core` module is read
from the subtree's position, not from the payload — registered as `Gap 471-C` on `agents/top.md`.
`formatting/`'s reservation, by contrast, names Particify outright and is certain.

### 🟢 The foundation screen this pass contributes — one command, before any licence read

🔵 `Gap 470-A` established that a root read establishes the root tree only. The question a
foundation choice actually asks is *when is a root read sufficient?* Measured over **229** shelf
addresses:

| tree size (`git ls-files \| wc -l`) | n | carry a grant below the root | rate |
|---|---|---|---|
| < 25 | 44 | 0 | **0.0 %** |
| 25–99 | 82 | 4 | **4.9 %** |
| 100–499 | 58 | 6 | **10.3 %** |
| 500–1 999 | 27 | 11 | **40.7 %** |
| ≥ 2 000 | 18 | 12 | **66.7 %** |

🟢 **Monotonic across all five bands.** Shelf-wide **33 of 229 (14.4 %)** are partitioned, across
**580** anchored licence paths. For this shelf specifically — which carries the large platforms — the
reading is blunt: **every foundation-tier platform here sits in the top two bands, where a root read
is more likely wrong than right.** The six largest trees on the shelf confirm it:

| platform | subtree licence paths found |
|---|---|
| `moodle/moodle` | **149** |
| `openedx/openedx-platform` | **148** |
| `openedx/edx-platform` | **148** |
| `ILIAS-eLearning/ILIAS` | **64** |
| `instructure/canvas-lms` | **56** |
| `chamilo/chamilo-lms` | **27** |

🔵 These counts are **not** 149 separate grants on Moodle — they are overwhelmingly vendored
third-party dependencies, the `V` class on `agents/top.md`. The number is a **work estimate**, not a
licence finding: it says how many payloads a genuine pre-vendoring audit of that platform has to
read, and for the deployed world's default LMS that number is 149.

### 🟢 The instrument, so the next pass can re-run it

🔵 No API access is needed and none was used — the GitHub API refuses these repositories outright
(`agents/top.md`, channel matrix):

```
git clone --depth 1 --filter=blob:none https://github.com/OWNER/REPO d
git -C d ls-files | grep -Ei '(^|/)(LICEN[CS]E|COPYING|COPYRIGHT|NOTICE|EULA|THIRD[-_]PARTY)([._-][A-Za-z0-9.+-]{1,20})?$'
```

🔴 **The anchoring is load-bearing, not cosmetic.** The unanchored form of that pattern produced a
**44.4 % false-positive rate** on this pass's first run (464 of 1 044 matches), counting
`NoticeTaskController.java` as a licence grant. The `([._-]…)?$` tail is what makes the numbers
above trustworthy.

### 🔵 No new foundation row is added, and the reason is measured

🔵 The general-vocabulary discovery legs returned **14 candidates, 0 of 14 unshelved** — including
`withmarbleapp/os-taxonomy`, which the trending channel named as the week's most education-specific
riser and which these shelves already carry **correctly graded `ODbL-1.0` + `CC BY-SA 4.0`**, a
grant that is not permissive software supply. The two rows this pass does add are rubric components
rather than substrate and are filed on `agents/top.md`.

## 🆕 `p470` — **🟢 THE GOVERNANCE SUBSTRATE THESE SHELVES HAVE BEEN SHORT OF IS FOUND, GRANTED AND APACHE-2.0: `panaversity/ksor` (232★) builds one authoritative knowledge record for humans and agents, and names education institutions in its own opening. 🔴 And the foundation question this shelf answers best is a warning: a permissive root grant does not make a repository permissive — `edukors_graph` is MIT at the root and GPL-3.0-or-later two directories down.**

🔵 **Gate posture:** `make hooks` not attempted (KB cloned outside the harness repo). Nothing here
is gate-attested. Every grant below was read first-hand at `HEAD` on **2026-10-27** from
`raw.githubusercontent.com`, written to a file and the file measured per `Gap 468-A`; every default
ref resolved by `git ls-remote --symref`.

### 🟢 Foundation rows added this pass

| component | repo | grant (first-hand) | ★ | region | why it is substrate, not an application |
|---|---|---|---|---|---|
| **KSoR** | [`panaversity/ksor`](https://github.com/panaversity/ksor) | **Apache-2.0** · 11 342 B · `2f538e0b9e84` | **232** (51f) | APAC | A **Knowledge System of Record**: the governed, authoritative source of truth that tutor, teaching-assistant and assessment agents read from, so they cannot contradict each other or the catalogue. Vendor-neutral SDK, TypeScript, `main` `b50f28926fae`, pushed 2026-10-01, 35.8 MB tree, topics include `ai-governance`. This is a *layer*, not a product |
| **Edukors Graph schema** | [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) | 🟡 **MIT** · 1 087 B · `625342dc4d3d` at the root — **GPL-3.0-or-later** at `plugin/edukorsplayer/` | 17 (2f) | **LATAM** (BR) | An **open standard** for learning graphs — a course as nodes and edges in one JSON Schema file — plus a standalone player. The schema is the substrate; see the boundary below before vendoring |
| **Bodhi Map** | [`AI-First-Community/Bodhi`](https://github.com/AI-First-Community/Bodhi) | **MIT** · 1 095 B · `967480f4f094` | 5 (1f) | Global | A **permissively granted** concept graph of modern AI: 123 concepts with typed connections, tokens and attention through LoRA, DPO, reasoning models, agents. Installable PWA, 59.6 MB tree |
| **SyllabusGraph** | [`OscarBarreraGithub/syllabusgraph`](https://github.com/OscarBarreraGithub/syllabusgraph) | **MIT** · 1 083 B · `3cc3fae03d97` | 1 | Global | Builds a concept graph **with source evidence attached to each relationship** and an independent review step. The citation-audit component that every "show what the answer rested on" clause needs |
| **Curriculum Knowledge Graph** | [`mizcausevic-dev/curriculum-knowledge-graph`](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** · 1 069 B · `a5ed17e0b90a` | 1 | Global | FastAPI graph service over courses, prerequisites, skills and outcomes, with **prerequisite bottleneck analysis** — the registrar-facing half of a pathway product. 🟡 Portfolio-tier, see the caveat below |
| **recall** | [`Garuda8887/recall`](https://github.com/Garuda8887/recall) | **MIT** · 1 099 B · `0bfc98ccf58b` | 5 | Global | Self-hosted **SM-2 spaced-repetition scheduler** with forgetting curves — the retention substrate a tutor needs and almost never ships. Default ref `master` |

🔵 **Six rows. Five permissive without qualification; one permissive only above its plugin
directory.**

### 🔴 The boundary on `edukors_graph`, because a foundation row must state it

🔵 Read first-hand at `main` `6bc743c6a5fe`:

| path | payload | class |
|---|---|---|
| `LICENSE.md` | 1 087 B · `625342dc4d3d` | **MIT** — schema, standalone player, original resources |
| `plugin/edukorsplayer/COPYING.txt` | **35 151 B** · `e79e9c8a0c85` | 🔴 **GPL-3.0-or-later** — the Moodle integration |

🔴 **`Gap 469-C` said the grant is read at `HEAD` or the row does not ship. That is necessary and it
is not sufficient.** The grant was read at `HEAD`, at thirteen root paths, and the answer was MIT —
correctly, and incompletely. The GPL grant is not at the root and no root path hints at it.
🟢 Registered as **`Gap 470-A`** (also on `agents/top.md`): a root-path sweep establishes the grant
on the **root tree only**; where a repository ships a plugin, integration or vendored subtree, the
grant is re-read at that subtree, and the README's own licence heading is the cheapest index to
which subtrees to check.

🔵 **For a studio the boundary is clean, not fatal:** the JSON Schema and the standalone player
vendor under MIT into a client deliverable. The Moodle plugin, if shipped, is GPL-3.0-or-later. 🔵
And the cause generalises — Moodle is GPL, so **every permissive education project that ships an LMS
integration has this split waiting inside it**. Expect it; probe for it.

### 🟢 `p467`'s specified-but-unsourceable substitute is sourced

🔵 `p467` recorded that the standard build for a curriculum-aligned tutor reaches for a **4 000★
`CC-BY-NC-4.0` knowledge graph**, unusable in paid work, and specified a permissive replacement it
could not find. A licence-filtered leg found **ten MIT concept- or curriculum-graph projects** this
pass; four are shelved above as substrate and the rest sit on `agents/top.md`.

🔴 **State the trade, not just the closure.** The replacement set's star counts are 17, 16, 5, 5, 3,
3, 2, 2, 1, 1. The NonCommercial graph's curation is worth something real and **no permissive peer
exists within two orders of magnitude of it**. What the studio gets instead is a *schema it may
sell* and the obligation to populate it. 🟡 `curriculum-knowledge-graph` in particular is
portfolio-tier — its own README section is titled "Why This Repo Is Good" and it cross-sells a
sibling showcase repo; read it as a working reference implementation of the FastAPI/graph shape, not
as a maintained dependency.

### 🔴 Refused as substrate this pass

| candidate | probe at `HEAD` | why it is not a foundation row |
|---|---|---|
| [`chat-edu/v3`](https://github.com/chat-edu/v3) | `main` `f44f5eeeb68b` · **MIT** · 1 064 B · `3dc45db43baf` · 16★ | 🟡 **abandoned.** Described as an education knowledge-graph builder and a Microsoft AI Classroom hackathon winner, but last pushed **2026-05-22** and its README is the **unmodified `create-next-app` boilerplate**. 16★ on a repository that never documented itself |
| [`FIY-pc/vibe-logisim`](https://github.com/FIY-pc/vibe-logisim) | `main` `a69438637ccc` · **GPL-3.0** · 35 149 B · `3972dc9744f6` · 9★ | copyleft — a deployment-or-fork decision. Placed on `verticals/solutions.md` |
| [`lhd23333/QuizForge`](https://github.com/lhd23333/QuizForge) | `master` `10138fbfb368` · **GPL-3.0** · 35 149 B · `3972dc9744f6` · 7★ | copyleft, same reason; byte- and digest-identical grant |
| [`ChengshuaiZhao0/Awesome-Trustworthy-AI4Edu`](https://github.com/ChengshuaiZhao0/Awesome-Trustworthy-AI4Edu) | `main` `b0ff5eb7dc09` · **no licence at 13 paths** | ungranted — and it is the only trustworthy-AI-for-education index found. A research entry point this base cannot carry as an asset |
| [`shenquan520/reading-analysis`](https://github.com/shenquan520/reading-analysis) | `main` `a63f496bc1ec` · **CC BY-NC-SA 4.0** · 17 124 B · `f5042f838c57` | 🔴 NonCommercial |
| [`caijimiao345/study-abroad-planner`](https://github.com/caijimiao345/study-abroad-planner) | `main` `86a123f19181` · **CC BY-NC-SA 4.0** · 20 850 B · `e66c269d4819` | 🔴 NonCommercial |

### 🔴 `Gap 466-A`'s size finding reproduces on a family it has never been tested on

🔵 This base has established that **AGPL-3.0 has many live byte-values** and that any size-based
licence screen therefore misclassifies. Two new data points, both read first-hand this pass:

| observation | bytes | consequence |
|---|---|---|
| **GPL-3.0** vs **AGPL-3.0** are **2 bytes apart** at the values seen here — GPL at 35 149 / 35 151, and this base's AGPL rows run 32 920–34 616 | ±2 | 🔴 the two licences whose difference is *the entire network-copyleft question* are not separable by length at the margin, and a 2-byte tolerance separates nothing |
| **CC BY-NC-SA 4.0** appears at **17 124 B** and **20 850 B** — short-notice form and full legalcode, same licence | 3 726 apart | 🔴 the CC family has the same defect as AGPL: one licence, multiple legitimate payload lengths |

🟢 **And the cross-pass control passes on the largest denominator this base has used for one:** the
base already records `35 149 B · 3972dc9744f6` as **GPL-3.0** across **31 distinct repositories**,
and `35 151 B` as GPL-3.0 on `Koha-Community/Koha`. This pass reproduces both byte-values and both
digests exactly, from three repositories none of those rows named.

🔴 **A second axis the size screen cannot see at all:** GitHub's own licence field returned
`NOASSERTION` for both CC BY-NC-SA rows above. The field was **silent exactly where the answer was
disqualifying** — a screen built on stars plus "has a LICENSE" plus the API's licence field would
have shown those two as *unknown*, not as *forbidden*, and `p467`'s conclusion stands unchanged:
that screen carries no information about whether software can be delivered.

## 🆕 `p469` — **🟢 THE PERMISSIVE-FOUNDATION QUESTION IS ANSWERED WITH A LICENCE CENSUS, NOT A PREFERENCE: of the eight education platforms Globant is most often asked to build on, exactly ONE is permissively granted — `OpenOLAT` (Apache-2.0, 448★) — and the most-cited "MIT" alternative is AGPL-3.0.**

🔵 Every licence below was read first-hand at `HEAD` on **2026-10-27**: default branch resolved by
`git ls-remote --symref`, payload fetched from `raw.githubusercontent.com` at that ref, written to
a file and the file measured (`Gap 468-A`). Star counts from the session GitHub tool channel the
same day.

### 🟢 Licence census — the eight foundations, graded by what Globant can ship

| repo | default ref | licence file · bytes · `sha256₁₂` | class | ★ | can a Globant SaaS build on it? |
|---|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `master` `891b9434e822` | `LICENSE` · 10 982 B · `6dbc5b605ed0` | 🟢 **Apache-2.0** | 448 | 🟢 **Yes, unconditionally.** Java LMS for universities and corporates; QTI, SCORM, curriculum management, assessment. The only permissive full LMS on this shelf |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `develop` `f72936bd41e5` | `LICENSE` · 1 097 B · `3c056b34a476` | 🟢 **MIT** | 1 161 | 🟢 **Yes.** Offline-first learning platform for low-connectivity deployments; OER, SDG-4 |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `19.0` `46a5d7d40082` | `LICENSE` · 8 241 B · `528f84036800` | 🟡 **LGPL-3.0** | 899 | 🟡 **Yes, with care.** Education ERP on Odoo. Weak copyleft: link and extend as modules; modifying the LGPL files themselves carries the obligation |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `main` `46c042e7da65` | `COPYING.txt` · 35 147 B · `8ceb4b9ee5ad` | 🔴 **GPL-3.0** | 7 548 | 🔴 Plugin-boundary only. The deployed world's default LMS; build *beside* it via plugins and LTI, not *into* it |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `master` `cd27c720ee18` | `LICENSE` · 35 147 B · `8ceb4b9ee5ad` | 🔴 **GPL-3.0** | 1 020 | 🔴 Plugin-boundary only. 🔵 Digest **identical** to Moodle's — both serve stock GPLv3 |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master` `03698e2b6ff4` | `LICENSE` · 35 136 B · `e12d78569742` | 🔴 **AGPL-3.0** | — | 🔴 Network-use copyleft. A hosted derivative owes source to its users |
| [`frappe/lms`](https://github.com/frappe/lms) | `develop` `54ad7dea5b1d` | `license.txt` · 33 893 B · `db1a87ba81e8` | 🔴 **AGPL-3.0** | 3 350 | 🔴 **Same class as Open edX — and this is the row the roundups get wrong.** See below |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` `435649b0474f` | `LICENSE` · 18 092 B · `8177f9751321` | 🔴 **GPL-2.0** | 720 | 🔴 Plugin/integration boundary. 🟢 **LATAM-specific**: Brazil's largest free school-management system, *software público*, Laravel + PHP |

🔵 Eight rows, eight first-hand grants. Two permissive, one weak-copyleft, five strong-copyleft.

### 🔴 `frappe/lms` is AGPL-3.0 and a 2026 roundup calls it MIT

🔵 A current "10 Best Open-Source Learning Management Systems in 2026" listing places Frappe
Learning under **MIT**, with "self-hosted data ownership" as the selling point. 🔴 First-hand at
`develop`: there is **no** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` or `COPYING.txt`. The
grant lives at **`license.txt`**, and it is the **GNU Affero General Public License v3**, 33 893 B,
`db1a87ba81e8`.

🔴 **Why this one costs more than an ordinary mislabel.** MIT and AGPL-3.0 sit at opposite ends of
the only axis that matters to a hosted engagement. Under MIT, Globant forks Frappe Learning, adds
a client's AI layer and ships it as a managed service with no disclosure duty. Under AGPL-3.0, the
same act obliges Globant to offer the **complete corresponding source of the modified work to
every user who interacts with it over the network** — including the AI layer, if it is linked into
the same program. A studio that took the roundup's licence column at face value would discover
this at contract review, not at selection. 🟢 Registered as **`Gap 469-C`**: no platform enters a
foundation shelf on a secondary source's licence column; the grant is read at `HEAD` or the row
does not ship.

🔵 Two notes that keep the correction honest. **AGPL-3.0 is not a defect** — it is a deliberate,
OSI-approved choice, and Frappe Learning is a strong platform. The defect is the *label*. And the
probe that found it had its own bug first: my six-path licence sweep returned **"no grant"** for
both `frappe/lms` and `moodle/moodle`, because neither serves its licence at any of the six
conventional paths. Moodle uses `COPYING.txt`, Frappe uses `license.txt`. 🟢 Registered as
**`Gap 469-D`**: a "no licence found" verdict is only publishable after `COPYING.txt`,
`license.txt`, `LICENSE.rst` and `copyright.txt` have also been probed — the four paths that
caught both false negatives this pass.

### 🔴 `formalms/formalms` — the "disputed Apache-2.0" row resolves to NO GRANT

🔵 Secondary sources split on forma.lms: one calls it Apache-2.0 ("so modified versions deploy
without copyleft obligations"), others call it GPL or LGPL. 🔴 First-hand at `master`
`446a77a9b9cb`, **ten** paths probed — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`,
`COPYING.txt`, `license.txt`, `LICENCE`, `lib/license.txt`, `doc/LICENSE`, `GPL.txt` — **all 404**.
There is no licence payload in the repository at `HEAD`. The repository's own description calls it
a **"forma.lms mirror repository"** (37★, last updated 2026-08-10), so the grant may exist
upstream off GitHub; it does not exist here. 🔴 **Refused.** The dispute is not Apache-vs-GPL — the
premise that a grant is readable at this address is false.

### 🔴 No permissive LMS+SIS exists, and that is the shelf's structural gap

🔵 Searched this pass for a single permissively-granted product covering both learning management
and student information. 🔴 **None found.** The only SIS-class systems that surfaced are
`francoisjacquet/rosariosis` — resolved live, default ref **`mobile`** `fa5f4b66caf4`, `LICENSE`
**GPL-2.0** 15 214 B `d954e14e5c75` — and `portabilis/i-educar`, also GPL-2.0. 🟢 The honest
recommendation follows from the census rather than from preference: **an integration between a
permissive LMS and a separate copyleft SIS, with the AI layer outside both process boundaries.**
`compose/patterns.md` carries that wiring as `P469-1`.

## 🆕 `p468` — **🟢 `Gap 467-D` CLOSES on this shelf too, and the way it closes is the lesson: the dead channel was `curl`, not the data. 🔴 And the pass's most-starred novel foundation candidate is a 272★ LLM-architecture course under `CC-BY-NC-SA-4.0` — a NonCommercial grant on exactly the asset a corporate-upskilling engagement would reach for first.**

### 🟢 Foundation-tier controls, re-read first-hand at `HEAD`

🔵 Every figure below was read today with the file-backed probe (`Gap 468-A`): the payload is
written to disk and the file is measured. Nothing is counted through a shell variable.

| foundation | grant · bytes · `sha256₁₂` | HEAD | vs `p467` |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11 408 B · `cd2f54e1e506` | `a31d82624c27` | 🟢 identical |
| [`av-leschinskiy/moodle-mcp`](https://github.com/av-leschinskiy/moodle-mcp) | MIT · 1 078 B · `67b516c28e67` | `69c36847e7ad` | 🟢 identical |
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | MIT · 1 078 B · `d0a329112827` | `d8849a82e9ea` | 🟢 identical |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 `CC-BY-NC` · 19 347 B · `41003d4a7474` | `cf262d886821` | 🟢 identical — and still unusable in a paid engagement |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🔴 bespoke · 8 563 B · `c834209c5f33` | `a6646794661b` | 🟢 identical |

### 🔴 Candidate foundations refused this pass

| candidate | ★ | grant · bytes · `sha256₁₂` @ HEAD | why it is not a foundation |
|---|---|---|---|
| [`walkinglabs/modern-llm-notebook`](https://github.com/walkinglabs/modern-llm-notebook) | 272 | 🔴 `CC-BY-NC-SA-4.0` · 425 B · `d65ff2212f3e` @ `03715769cb94` | 🔴 `UNSELLABLE`. A hands-on course on modern LLM architectures, training and inference — the obvious spine for a paid upskilling curriculum, and **NonCommercial forbids exactly that**. ShareAlike compounds it: derived course material would have to carry the same grant |
| [`mdakram2001/AMU-Utilities`](https://github.com/mdakram2001/AMU-Utilities) | 0 | 🔴 **NO GRANT** at 10 root paths @ `cb8b178ef9f8` | University SIS MCP server (Aligarh Muslim University, India). No grant, no foundation |
| [`s-caserta99/DocuQuery_MCP`](https://github.com/s-caserta99/DocuQuery_MCP) | 0 | 🔴 **NO GRANT** at 10 root paths @ `85523c2f8252` | Literature-Q&A MCP server for researchers |
| [`leonine1983/aprendix`](https://github.com/leonine1983/aprendix) | 0 | 🔴 **NO GRANT** at 10 root paths @ `7df5ee4c76d6` | Brazilian school-management system with AI dropout support. 🔴 The right LATAM product shape, nothing to build on |

### 🟢 Added to the index tier

| repo | grant · bytes · `sha256₁₂` @ HEAD | what it is good for |
|---|---|---|
| [`StudentSuite/awesome-student-resources`](https://github.com/StudentSuite/awesome-student-resources) | MIT · 1 069 B · `537c697c69a5` @ `602df143c5a9` | IB / IGCSE / SAT tool index — a **catalogue input** for a market-scan deliverable, not a codebase |
| [`StudentSuite/awesome-study-resources`](https://github.com/StudentSuite/awesome-study-resources) | MIT · 1 069 B · `537c697c69a5` @ `74d5a7bbf17b` | 🟡 Exam-prep index with free / freemium / paid / open-source tags. **Byte-identical grant payload to the row above** — two repositories, one grant |

### 🔵 Measurement note carried from `Gap 468-A`

🔴 This pass's first probe read `falkenslab/miyagi` at 1 077 B and a different digest. The cause is
the `$(curl …)` idiom, whose command substitution strips trailing newlines — **every payload read
that way is short by its trailing-newline count**. This is `p465`'s −1-byte defect, reproduced
independently, and the correct statement of it is about the idiom rather than about a script. The
file-backed reader reproduces all five controls above exactly.

---

## 🆕 `p467` — **🟢 `Gap 466-C` IS CLOSED IN THE STRONG FORM: the size screen is not merely replaced, it is GONE — no verdict in this pass's reader branches on payload bytes, and 41/41 controls hold without them. 🔴 And the re-grade the gap prescribed found that the base's own standing reader carries a defect the size screen was hiding: it returns `MIT` for a payload that recites MIT and then forbids commercial use.**

### 🟢 What the gap asked for, and what was actually built

🔵 `Gap 466-C`: *"replace the size screen with a first-non-blank-line match against the SPDX title
strings, keep size and digest as provenance only, and re-grade every carried cell that asserts a
licence family from a size."*

| the prescription | 🟢 delivered as |
|---|---|
| first-non-blank-line match against SPDX titles | [`grant_class.py::TITLE_RULES`](../compose/code/p467-grant-class/grant_class.py) — 26 title patterns, matched on the first non-blank line, **AGPL before GPL** and the NC-bearing CC variants before plain `CC-BY` |
| size and digest as provenance only | 🟢 **no code path reads `bytes`.** `bytes` and `sha256₁₂` are carried per row so a later pass can prove it read the same payload, and nothing else |
| re-grade cells asserting a family from a size | 🟢 103 addresses probed, graded and published: [`evidence/grant-class.2026-10-26-p467.tsv`](../evidence/grant-class.2026-10-26-p467.tsv) |

### 🟢 Why a size screen could never have worked — the two-sided demonstration

🔵 `p466` showed the divergent side: AGPL-3.0 at **7** live byte values spanning 1 116 B. This pass
measured the **convergent** side, which is the half that produces false *positives*:

| payload | bytes | `sha256₁₂` | carried by |
|---|---|---|---|
| Apache-2.0, variant A | **11 357** | `c71d239df917` | `ably-labs/realtime-quiz-framework`, `mytechnotalent/HNN` |
| Apache-2.0, variant B | **11 408** | `cd2f54e1e506` | `HKUDS/DeepTutor` (the base's headline control) |

🔴 **Two Apache-2.0 payloads 51 B apart, and two unrelated projects byte-identical at 11 357 B.** A
size screen reading 11 357 against a carried 11 408 would report a disagreement where there is
none, and would report agreement between any two licences that happen to land on the same count.
🟢 Both are graded `Apache-2.0 / PERMISSIVE` here from their title line, and the 51 B is recorded
as provenance and used for nothing.

🔴 **And the collision is not hypothetical — it is live on these shelves at MIT:**

| payload | bytes | `sha256₁₂` |
|---|---|---|
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) `LICENSE` | **1 073** | `1e05c9440068` |
| [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) `LICENSE` | **1 073** | `b7b08f330649` |

🔴 **Two MIT payloads at the IDENTICAL byte count with DIFFERENT digests** — the copyright line
differs, the grant does not. 🟢 So size is simultaneously **over-sensitive** (51 B apart, same
licence) and **under-sensitive** (0 B apart, different text): it is not a weak screen, it is not a
screen at all. 🔵 The digest, by contrast, does its one job — proving a later pass read the same
bytes — and `eu-ai-act-risk-checker` reproduces `p437`'s record **byte-, digest- and
HEAD-identical** (1 073 B · `b7b08f330649` @ HEAD `41da87feb238`), a **fifth** cross-pass control
this pass.

### 🔴 The defect the size screen was hiding, and it is in this base's standing reader

🔵 Re-grading on the title axis surfaced a class a size axis structurally cannot see: a payload
whose **bytes and family are both unremarkable** and whose **terms are not**.

[`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) — 2 049★, `LICENSE.md` **8 563 B**
`c834209c5f33` @ HEAD `a6646794661b` — is titled *"PageLM Community License"*, opens with MIT's
grant sentence verbatim, and then restricts it to *"personal, educational, or non-commercial
research purposes"* with a **revenue-sharing requirement** and a **redistribution prohibition**.
🔴 [`family_title.py`](../compose/code/p456-ref-resolution/family_title.py) — the reader `p454`
built and this base has relied on for thirteen passes — grades it
**`MIT (body form, no title)`**, because its `PERMISSIVE_GRANT` arm suppresses the bespoke-licence
check whenever the body recites a permissive grant form. 🔵 Full account and remedy on
[`agents/top.md`](../agents/top.md) as **`Gap 467-A`**; the remedy is a **restriction override**
that runs after the body layer and outranks it.

### 🟢 Foundational rows re-graded on the new axis, all read first-hand this pass

🔵 These are the infrastructure-tier rows in this pass's population — the ones an engagement builds
*on* rather than composes. Every grant below is from the payload's own title line unless `line1=0`
is noted.

| repository | ★ | `grant_class` · grant · `sha256₁₂` | what it is foundational for |
|---|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1 161 | 🟢 `PERMISSIVE` · MIT · 1 097 B · `3c056b34a476` @ HEAD `f72936bd41e5`, `br=develop` | 🟢 The offline-first learning platform for low-connectivity deployment. Confirmed MIT at root, reproducing this base's `DEPENDENCY-SCOPED` reading against the GPL fragments in its tree |
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | 36 190 | 🟢 `PERMISSIVE` · MIT · 1 068 B · `be9b04bccfb4` · `LICENSE.md` @ HEAD `a24e62f4d8ca` | The skill *compiler* — the largest education-adjacent artefact in this window, and a build step rather than an app |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 359 | 🟢 `PERMISSIVE` · MIT · 1 072 B · `383b85b370e8` @ HEAD `86ab328f0e5b` | 🟢 **The SCORM/xAPI runtime.** The carrier that lets agent-generated content run inside an estate's existing LMS without touching the LMS |
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 377 | 🟢 `PERMISSIVE` · Apache-2.0 · 10 273 B · `73ba74dfaa52` @ HEAD `d48c2a6ae053` | LTI tool hosting — the standards-side counterpart to `scorm-again` |
| [`g3i/lxHive`](https://github.com/g3i/lxHive) | 79 | 🟡 `STRONG_COPYLEFT` · **GPL-3.0-or-later** | A lightweight xAPI Learning Record Store. 🟡 **GPL *2.0*-or-later**, read from the payload: the version axis `p455` built is what separates it from the GPL-3.0 rows, and the `or-later` election is read, not assumed — per `p455`'s version axis |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 117 | 🟡 `STRONG_COPYLEFT` · **GPL-3.0-or-later** · 35 147 B · `8ceb4b9ee5ad` | 🟢 **Accessibility conformance scanning inside the LMS** (Canvas/LTI, Section 508/WCAG) — the compliance component the EU and US accessibility duties on [`intel/market.md`](../intel/market.md) actually require |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | 🟡 **`COMPOSITE_PER_ASSET`** · 5 789 B · `d849ffef4f98` @ HEAD `a7547180c47d` | 🟢 Standards-aligned curriculum data as a layer for educational AI — **code MIT, datasets per-asset**, two of three access tiers not open. The first *sellable-in-part* answer to `p466`'s `CC-BY-NC` curriculum-data finding |
| [`Wakoma/nimble`](https://github.com/Wakoma/nimble) | 110 | 🟡 `STRONG_COPYLEFT` · **CERN-OHL-S** · 13 419 B · `d6475a84171f` @ HEAD `315910f164c0` | 🆕 **A licence class this base has never carried.** Deployable offline wireless mesh — the *physical* layer under Kolibri. Hardware derivatives must ship design sources |

🔵 **Eight rows, each with a first-hand grant and a stated role.** Not a minimum — the count is what
the population at this tier yielded.

### 🔴 Gap this pass registers at this tier

| gap | statement | how the next pass closes it |
|---|---|---|
| 🟡 **`Gap 467-I`** | **This base has no foundational row for the LRS/analytics tier under a permissive grant.** The only Learning Record Store carried (`g3i/lxHive`) is GPL-3.0-or-later, so an engagement needing xAPI analytics inside a proprietary deliverable has no build-on option on these shelves. | Probe the xAPI/LRS and `caliper` vocabulary specifically — a token set this base has not run — and grade every hit; if the tier is genuinely copyleft-only, publish that as a measured finding rather than leaving the tier silent |

---

## 🆕 `p466` — **🟢 `Gap 465-A` IS CLOSED WITH FIXTURES — AND THE CONTRACT IT PROPOSED IS NOT SUFFICIENT. Declaring "raw bytes" fixes the convention defect but does NOT fix the comparison, because TWO legitimate canonical texts of Apache-2.0 circulate ~1.1 KB apart, and that — not tampering — is what explains the three different Apache-2.0 sizes this base carries. 🔴 AGPL-3.0 now has SIX observed live byte-values, so any size-based licence screen misclassifies.**

### 🟢 Stock-licence fixtures, fetched first-hand from the SPDX canonical corpus

🔵 `Gap 465-A` asked for "a `sha256` of stock MIT/Apache-2.0/GPL-3.0/AGPL-3.0 as fixtures".
Fetched from `raw.githubusercontent.com/spdx/license-list-data/main/text/<id>.txt`, measured under
the **raw-bytes** contract (`curl -o`, then `wc -c`):

| SPDX id | canonical raw bytes | `sha256₁₂` |
|---|---|---|
| `MIT` | **1 078 B** | `b05785f9f18e` |
| `Apache-2.0` | **10 280 B** | `074e6e32c86a` |
| `GPL-3.0-only` | **34 674 B** | `fb981668c18a` |
| `AGPL-3.0-only` | **34 020 B** | `d8a6cc31abc1` |
| `BSD-3-Clause` | **1 460 B** | `5a93d5831e12` |
| `CC-BY-SA-4.0` | **18 375 B** | `cde7883b9050` |

### 🔴 And the fixtures REFUTE the assumption the gap rested on

🔵 `Gap 465-A` assumed one stock text per licence, so that a carried cell could be graded against
it. **For Apache-2.0 that is false**, and the three Apache-2.0 payloads read first-hand this pass
fall into two clean families:

| repository | first-hand payload | family |
|---|---|---|
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | **10 273 B** · `73ba74dfaa52` @ HEAD `d48c2a6ae053` | 🟢 **bare licence text** — within 7 B of the SPDX canonical **10 280 B** |
| [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) | **11 337 B** · `36d6788503b8` @ HEAD `94cedd7d4e02` | 🟡 **licence + "APPENDIX: How to apply"** boilerplate |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **11 408 B** · `cd2f54e1e506` @ HEAD `a31d82624c27` | 🟡 **licence + appendix, with the holder fields filled in** |

🟢 **So the ~1.1 KB spread this base has carried across passes is the APPENDIX, not a variant
grant.** The two families differ by whether the project copied GitHub's template (which includes
the appendix) or SPDX's bare text. 🔵 This retires, with a mechanism, any reading of the Apache-2.0
size spread as evidence of a modified licence.

### 🔴 AGPL-3.0: six live byte-values, so a size screen cannot classify

🔵 Combining this pass's GitLab reads (below) with the GitHub-side controls the base already
carries:

| payload bytes | `sha256₁₂` | observed at |
|---|---|---|
| **34 020 B** | `d8a6cc31abc1` | 🟢 SPDX canonical `AGPL-3.0-only` |
| **34 449 B** | `feff6860d5ea` | `moodlenet/backend` (GitLab) |
| **34 481 B** | `6dbb120dadf0` | `moodlenet/frontend` (GitLab) |
| **34 520 B** | `57c8ff33c9c0` | `Openki/Openki` (GitLab) |
| **34 523 B** | `0d96a4ff68ad` | 🔵 the base's carried GitHub control — `Vacademy-io`, `RubricSpan`, `gygy-open/question-bank`, three unrelated HEADs |
| **34 588 B** | `a7f13bbcc053` | `DD-workspace/DD` (GitLab) |
| **35 136 B** | `e12d78569742` | 🔵 carried: `openedx/edx-platform` |

🟢 **`p462`'s payload-identity rule survives and is sharpened:** the digest identifies the licence
text **plus holder**; the size identifies **nothing** — seven values spanning 1 116 B for one
licence. 🔴 A pass screening AGPL-3.0 on `size == 34 523` (the only value this base carried before
today) would have misclassified **all four** GitLab rows as non-AGPL. Registered as
**`Gap 466-C`**.

### 🟢 MIT confirms the same shape at small scale

🔵 Six MIT payloads read first-hand this pass: **1 063 / 1 064 / 1 066 / 1 068 / 1 072 / 1 092 B**,
six distinct digests, against the SPDX canonical **1 078 B**. The variance is the copyright holder
line. 🟢 Consistent with `p464`'s finding that two MIT payloads can share a size and differ in
digest — **neither size nor digest identifies a project, and size does not identify a licence**.

### 🟢 Substrate rows confirmed permissive this pass — assessment plumbing

🔵 `Gap 464-C` says to stop reading a foundation nil from the application-tier recency channel and
source substrate elsewhere. The `topics/grading` channel, sampled here for the first time, is a
**substrate** channel: these are the pieces an assessment build stands on, and all three are
permissive.

| repository | ★ | grant · `sha256₁₂` · HEAD | what it gives a build |
|---|---|---|---|
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 1 400 | 🟢 **BSD-3-Clause** · 1 512 B · `3a83d5b8e22c` @ `c2e1ab63512b` | the reference assign→release→collect→autograde→feedback pipeline for notebook coursework, with a release/solution split that keeps answers out of student copies. 🟢 The deterministic spine an LLM grader should be bolted *onto*, not replace |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 359 | 🟢 **MIT** · 1 072 B · `383b85b370e8` @ `86ab328f0e5b` (`br=master`) | a modern SCORM 1.2 / 2004 + AICC runtime in JavaScript. 🔵 **The unglamorous row that decides whether a build can ship into an incumbent LMS at all** — SCORM is how content talks to Moodle/Canvas/Cornerstone |
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 377 | 🟢 **Apache-2.0** · 10 273 B · `73ba74dfaa52` @ `d48c2a6ae053` (`br=master`) | an **LTI** framework — the standards-based way to mount an external tool inside any compliant LMS, with roster and grade passback. 🟢 Together with `scorm-again` this is the full integration surface for selling *into* existing institutional estates rather than replacing them |

🔵 **`Gap 464-C` is answered in substance, not just in method**: a channel chosen for substrate
returned 3 substrate rows out of 3 probed, against the recency channel's 1-in-12. The channel, not
the supply, was the limiting variable.

### 🔴 Gap registered

| gap | what is wrong | what would close it |
|---|---|---|
| 🔴 **`Gap 466-C`** | **Payload size is used on these shelves as if it screened licence family, and it does not.** AGPL-3.0 shows **7** live byte-values spanning 1 116 B; Apache-2.0 shows two canonical families ~1.1 KB apart; MIT shows 6 values in 29 B. The `34 523 B` AGPL value the base carried as *the* control is one of seven. | Replace the size screen with a **first-non-blank-line match** against the SPDX title strings, keep size and digest as provenance only, and re-grade every carried cell that asserts a licence family from a size. |

## 🆕 `p465` — **🟢 THREE substrate rows from twenty novel addresses, and all three are REGISTRIES OR LANGUAGE SUBSTRATE rather than models or frameworks. 🔴 One of them carries a defect class this base has never named: a `LICENSE` that states an INTENTION to license rather than granting anything.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes; nothing
below is gate-attested. 🔵 Payload figures below are **raw bytes** (the `p464` convention); see
`Gap 465-A` on [`agents/top.md`](../agents/top.md) for why that has to be said out loud.

### 🟢 Foundation rows added this pass

| repository | ★ | created | grant · `sha256₁₂` | region · basis | why it is substrate and not an application |
|---|---|---|---|---|---|
| [`stanleyHayes/ghanaschools`](https://github.com/stanleyHayes/ghanaschools) | 1 | 2026-09-01 | 🟢 Apache-2.0 · `0be2dbbe5781` · 11 355 B | **EMEA** · Ghanaian institutions, `ghana` topic | source-linked registry of Ghanaian education institutions in Go, with **stable identifiers and field-level provenance**. 🟢 **It declares its own exclusions**: "no personal, student or quality data" — so it is an identifier spine a client system can join against without inheriting a privacy surface. 🟢 Framed as digital public infrastructure, not a product; HEAD `14e953e9386d` |
| [`Open-Syria/data-universities`](https://github.com/Open-Syria/data-universities) | 4 | 2026-06-28 | 🔴 **see defect below** · `76f7100206a3` · 864 B (`LICENSE.md`) | **EMEA** · Syrian higher education | open dataset of Syrian universities — Arabic *and* English names, websites, locations, identifiers, logos, source attribution, served as CSV/JSON with an API shape. 🟢 The only first-hand instance of Syrian education data on this base; HEAD `b886b54de41d` |
| [`boi-network12/igboscript`](https://github.com/boi-network12/igboscript) | 12 | 2025-09-16 | 🟢 MIT · `ad3d62daf713` · 1 082 B | **EMEA** · Igbo language, Nigeria | JavaScript transpiler driven by **Igbo keywords**. Substrate rather than courseware: it is a language layer other teaching material is written *in*. 🔵 **It is also the highest-starred repository in the entire African education census below** — 12★ is the ceiling, and this is it; HEAD `698b69afbf67` |

### 🔴 The defect: a licence payload that states an INTENTION instead of granting

🔵 `Open-Syria/data-universities` splits data from code, which is correct practice for a dataset.
🔴 **But the operative sentence is conditional.** Read first-hand at `b886b54de41d`:

> "Released data artifacts and documentation **are intended to be published under**: `Creative Commons Attribution 4.0 International (CC BY 4.0)`"

🔴 **"Intended to be published under" is not a grant.** It describes a plan. Nothing in the payload
conveys any permission to the reader, and no present-tense licensing verb appears. A
classifier keyed on the string `CC BY 4.0` grades this row **CC-BY-4.0 and clean**; a lawyer
grades it **unlicensed with a stated aspiration**. 🟢 The row is therefore carried as
**substrate with its grant marked unsettled**, not as CC-BY-4.0 supply.

🔵 **Why this is a class and not one repository.** This base's grant reader — every version of it
across `p228`, `p411`, `p455` — anchors on the licence **title block** and on family/version
strings. An anchor that reads *which licence is named* cannot see *whether it was granted*. Both
`NOASSERTION` (`Gap 461-B`) and this case defeat it, in opposite directions. Registered as
**`Gap 465-E`**.

### 🔵 What the recency channel did NOT return, stated so the shape is visible

🔴 **Zero models, zero frameworks, zero datasets-at-scale.** Twenty novel addresses, and the
substrate yield is two registries and a transpiler. 🟢 This reproduces `p464`'s finding ("the
recency channel returns APPLICATIONS and SKILLS, not substrate") for a second pass, now with a
larger denominator — and it means the foundations shelf cannot be grown by recency discovery
alone. 🟡 `Gap 465-F`: the substrate legs need a channel keyed on **package registries**
(PyPI/npm/HF) rather than on repository recency, which `p393`'s PyPI cache already half-builds.


## 🆕 `p464` — **🔴 ONE foundation row from twelve novel addresses, and the 1-of-12 is itself the finding: the recency channel returns APPLICATIONS and SKILLS, not substrate. 🟢 The one row it did return is the first citation-AUDIT component this base has carried, which is the piece every "show what the answer rested on" clause in `intel/market.md` actually needs.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED, and so was every
individual gate.** The harness permission classifier refused both `make hooks` and a direct
`python3` invocation of the repo's own gate scripts (`Code from External`) — **eleven denials in
twelve passes, and one step stricter than `p463`**, which was still permitted to run
`p277-table-structure` and `p383-region-heading-gate` by hand. 🔵 **Nothing below is
gate-attested.** Mitigation, re-implemented in this session's own code rather than the repo's:
frontmatter keys and closed-vocabulary `region` checked on all eight shelves; every new table
checked for separator presence, pipe-count consistency and **no header row published as data**;
append-only proved on both trending shelves by prior-section containment; **every address
introduced this pass re-resolved by `git ls-remote`.**

🔵 **Instrument.** Two first-hand channels, as `p450` and `p463` established:
`git ls-remote <addr> HEAD` (**tree identity**) and
`raw.githubusercontent.com/<addr>/<branch>/LICENSE` (**payload bytes** → size + `sha256₁₂`).
🔴 **The `curl -sI https://github.com/<addr>` probe the ingest brief prescribes is reproduced
unusable, now from a fourth independent direction:** it returns `403` for a live address and for
a nonexistent one *alike* — `openedx/edx-platform` and `gmilano/this-does-not-exist-xyz123` are
indistinguishable through it. No row here rests on it.

🔴 **A channel measurement that is new this pass, and a future pass will misread it if it is not
written down: the GitHub *search* API is not reachable from the `gh` CLI here.**
`gh api "search/repositories?q=..."` returns **`403 — "sessions are bound to their configured
repositories. Use repository-scoped endpoints"`**. Repository search survives **only** through
the MCP `search_repositories` tool; `gh` reaches only the two attached repos. 🔵 A pass that
reaches for `gh` to discover supply will read that `403` as *no results* and publish a nil that
is an artifact of the channel — the exact error class `p463` caught on the web legs.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p463` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

### 🟢 Foundation-tier row added this pass

| repository | ★ | created | grant · `sha256₁₂` | region · basis | why it is substrate rather than an app |
|---|---|---|---|---|---|
| [`yukunou703/studyproof`](https://github.com/yukunou703/studyproof) | 20 | 2026-09-07 | 🟢 MIT · `e250f7a46d43` · 1 065 B | Global | ships as **CLI + browser + MCP server**, not a product surface: indexes local PDFs and notes, builds **cited AI context packs**, and **audits quotations** back to source. Holder "Lapmlnex". HEAD `408d51f2ce68` |

🟢 **Why this one is promoted to the foundation shelf and the other six are not.** It has no
learner-facing opinion — no course model, no mastery model, no review schedule. It answers one
question (*does this quotation exist in the cited source?*) behind an MCP boundary, which makes it
composable under anything else on these shelves. 🔵 Every other granted row this pass is an
application or a skill with pedagogy baked in.

### 🔴 The foundation nil, typed by measurement — 1 of 12, and this is now the third pass to see the shape

| tier the novel addresses landed in | n of 12 | reading |
|---|---|---|
| 🟡 application / desktop app | 5 | `unyra`, `pickq`, `PenFlow`, `essay-grader`, `olympiad-problem-forge` |
| 🟡 agent skill / harness plugin | 3 | `feynman-technique`, `dsh-plugin-lookatstudy`, `SocraMetry` |
| 🟡 platform | 2 | `gygy-open/question-bank` (AGPL-3.0), `omega-epsilon-problem-forge` |
| 🟢 **substrate / library / MCP** | **1** | `studyproof` |
| 🔴 **evaluation harness** | **0** | 🔴 **the efficacy gap holds for a sixth pass** |

🔵 `p463` measured *7 of 13 ship as an agent skill*; this pass measures **1 of 12 is substrate**.
🟢 Same phenomenon from the other end, by an independent operator on a different slice: **the
recency channel is a channel onto the application tier.** 🔴 A pass that needs foundations cannot
get them from `created:>` bounds, and this base should stop expecting it to. Registered as
`Gap 464-C`.

### 🟡 What the measurement instrument learned, and one rule that must NOT be over-read

🟢 **`p462`'s payload-identity rule gains a THIRD instance, and this pass found it by accident:**
[`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) serves the AGPL-3.0
payload **34 523 B · `0d96a4ff68ad`** — byte- and digest-identical to the
`Vacademy-io/vacademy_platform` control and to `p463`'s `sitor-ai/frametell`, at a **third**
unrelated HEAD (`aba4510778ff`). Three unrelated projects, one payload.

🔴 **And the over-reading this base is one step away from making.** Measured on this pass's own
seven payloads:

| observation | what it licenses | what it does **not** license |
|---|---|---|
| 🟢 AGPL-3.0 at `0d96a4ff68ad` on three unrelated repos | the payload is the **canonical FSF text**, so digest ⇒ **licence-text identity** | 🔴 digest ⇒ *project* identity. These are three different projects |
| 🔴 `openedx/edx-platform` is **also** AGPL-3.0 but **35 136 B · `e12d78569742`** | there are **≥ 2 circulating byte-variants of AGPL-3.0** | 🔴 a digest allow-list keyed on one AGPL digest will mis-grade the other as unknown |
| 🔴 `maplexrain/unyra` and the `instructional_agents` control are **both MIT at exactly 1 067 B** with **different** digests (`f7ef32f1240e` vs `4e085d826a64`) | 🟢 for MIT the digest separates on the **copyright-holder line**, so digest ⇒ text **+ holder** | 🔴 **size ⇒ identity. Equal size, different grant holder.** |

🟢 **The usable rule, stated once:** *size* is a screen, *digest* is an identity for the licence
text and its holder, and **neither is an identity for the project**. 🔵 That is why the
`feynman-technique` anomaly above was read rather than rounded off — the size screen fired, and
the payload turned out to carry a carve-out.

## 🆕 `p463` — **🟢 Four foundation rows added, every grant permissive and read first-hand (Apache-2.0 ×2, MIT ×2), and the discovery nil four passes published is shown to be an artifact of the CHANNEL: a `created:>` bound returned 13 unshelved addresses where the prescribed legs returned 0. 🔴 And `pytorch/opacus` — the only differential-privacy component this base has ever carried — is recovered from a silent eviction that no gate here would have caught.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN.** The harness
permission classifier **refused the invocation outright** (`Code from External`) — the same
refusal `p462` recorded, not a proxy failure and not a missing target. **Nothing below is
gate-attested**, and the gate's inability to run remains the standing obstacle: `Gap 446-A`
cannot be closed by a pass that is not permitted to run the gate.

🔵 **Instrument, and one channel the prescribed probe cannot replace.** Two channels, both
first-hand: `git ls-remote <addr> HEAD` (**tree identity**) and `raw.githubusercontent.com`
(**payload bytes**). 🔴 **The `curl -sI https://github.com/<addr>` check this base is instructed
to use is unusable from this host: it returns `403` for every address, live or withdrawn** —
`openedx/edx-platform` and a non-existent slug are indistinguishable through it. A probe that
returns the same code for a 200 and a 404 is not a verification step, and no row below rests on
it. This reproduces `p450`'s replacement of that probe from an independent direction.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p462` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

🟢 `p462`'s rule — *a byte-identical licence payload is near-zero evidence of repository
identity* — is **independently confirmed on a new pair this pass found**:
[`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) serves the **same** AGPL-3.0
payload as `Vacademy-io/vacademy_platform` (34 523 B · `0d96a4ff68ad`) at a **different** HEAD
(`683b3e5e8cfa` ≠ `3a9c66db938c`). Two unrelated projects, one stock text.

### 🟢 The saturation nil is an artifact of the DISCOVERY SLICE, not of supply — and the variable is RECENCY

🔴 Four consecutive passes (`p459`–`p462`) graded the prescribed channel and published the same
verdict: *usable novel repository yield ZERO*. 🟢 **That verdict is correct about the channel and
wrong about the supply.** Both legs were run this pass, side by side:

| channel | addresses returned | absent from the ENTIRE base | granted | permissive |
|---|---|---|---|---|
| 🔴 the prescribed web-search legs (4 global + 4 regional) | ~30 repo-shaped tokens | 🔴 **0** | — | — |
| 🟢 GitHub repository-search API, `created:>` × `stars:>` slice | **17** | 🟢 **13** | 🟢 **11** | 🟢 **10** |

🔴 **Every repo-shaped token the web legs returned falls into one of three already-known
buckets**, which is why they grade nil: a general-purpose agent (OpenHands, CrewAI, `opencode`,
OpenClaw — not education supply), an already-carried vertical platform (OpenEduCat, Open edX,
ERPNext/`frappe`, Moodle, Kolibri, RosarioSIS, Dolibarr, Fedena), or an already-carried education
repository (`withmarbleapp/os-taxonomy`).

🟢 **One of those requires a correction to how a nil gets read.** The vertical leg returned
**openSIS**, and a slug-shaped guess (`openSIS-Classic/OpenSIS-Classic`) is `grep`-absent from
this base — which looks like a discovery. It is not: the platform is carried under its real
address [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic), on **3** sell
shelves. 🔴 **A novelty check keyed on a guessed slug manufactures false positives**; the check
must be keyed on the address the probe resolves.

🟢 **And the probe returned a free identity reading while confirming it:**
`OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` both resolve to HEAD
**`8348cd069aa2`** — the same tree under two names. 🟡 Graded honestly, same-HEAD is **alias *or*
undiverged fork** and this pass does not claim which; per `p462` the payload cannot settle it
either (both serve no root grant at all). Registered as `Gap 463-C`.

🔵 **The variable that bought the 13, stated so the next pass can reuse it.** Not vocabulary —
`p453`'s vocabulary-spend ledger already shows vocabulary exhausted, and this pass's Spanish and
platform-name legs returned **0** and **0**. The variable is **`created:>2026-06-01`**. The
education supply is being written *now*, faster than the shelves sample it, and a star-ranked
query without a date bound returns the same incumbents every hour. **A date bound is the cheapest
discovery instrument this base has.**

### 🟢 Novel foundation rows — 4, each grant read first-hand this hour

🔵 `p443`'s split applies: these are **integration surface** — a schema and compiler, a
curriculum, a deployable stack, a teaching artefact — not agents. The agent-addressable half of
this pass's harvest is on [`agents/top.md`](../agents/top.md) `p463`.

| repository | grant · payload · `sha256₁₂` | HEAD | ★ | region · basis | why it is a foundation |
|---|---|---|---|---|---|
| [`kevindegila/construire-un-llm-de-zero`](https://github.com/kevindegila/construire-un-llm-de-zero) | 🟢 **Apache-2.0** · `LICENSE` 11 344 B · `3ac10e0c7f91` | `bc15ffd6d9c0` | 46 | **EMEA** · francophone, `llmdezero.com` | 22-chapter from-scratch LLM curriculum **in French**, tensors → agents, as runnable notebooks. 🟢 **The only non-English-language curriculum foundation this base carries**, and francophone EMEA/Africa is precisely where `Gap 456-D`'s coverage is thinnest |
| [`romanticamaj/promptasy`](https://github.com/romanticamaj/promptasy) | 🟢 **MIT** · `LICENSE` 1 226 B · `677fe7e31abe` | `fd8eabe431a6` | 43 | **APAC** · 繁體中文 + author site | prompt-engineering taught as a browser game, **each technique cited to its OpenAI / Anthropic / Google / xAI source** — a citable curriculum, not a vibe |
| [`rasidi3112/pondok-ai`](https://github.com/rasidi3112/pondok-ai) | 🟢 **MIT** · `LICENSE` 1 079 B · `c3dc4b0503f8` | `05fcd0dcdc01` | 37 | **APAC** · Indonesia | 🟢 one command stands up a **whole-classroom on-prem** stack — Ollama + Open WebUI + RAG + Qdrant + an OpenAI-compatible API, sized to the hardware, shared to phones on the LAN. **The data-residency answer for any jurisdiction where student data cannot leave the building** |
| [`seehiong/eduvis`](https://github.com/seehiong/eduvis) | 🟢 **Apache-2.0** · `LICENSE` 9 831 B · `898c5a5080eb` | `ed82a1870b6e` | 28 | 🟡 Global · author signal only, **weak** — not placed on it | a curriculum-aware **intermediate representation**: schema, validator, compiler pipeline and reference SVG renderer, separating pedagogical structure from rendering |

🟡 **One placement is deliberately withheld.** `seehiong/eduvis` has an author/host signal that
points APAC and **no first-hand national or institutional claim anywhere in the repository**.
Per this base's own closed-vocabulary rule it is recorded **Global** rather than placed on a
guess — a wrong placement is worse than an unplaced row, and `region` is a filter, not a hint.

### 🔴 Ten permissive foundation-tier addresses were EVICTED and are recovered here

🔵 The eviction audit is on this pass's section of [`agents/top.md`](../agents/top.md) in full.
The one row this file must not lose again:
[`pytorch/opacus`](https://github.com/pytorch/opacus) — **Apache-2.0 · 10 241 B ·
`bcf6964d43d8` · HEAD `df040e4a1594`** — is the **only differential-privacy component this base
has ever carried**, it was dropped from every sell shelf between `p406` and `p462` with no
recorded reason, and it is the exact control an EMEA high-risk education deployment is asked for.
🟢 `meta-pytorch/opacus` resolves to the **same HEAD**: one project, two addresses, cite one.

### 🔵 Gap register opened by this pass

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 463-A`** | The sell shelves have **no eviction ledger**. 21 projects left every sell shelf between `p406` and `p462` with no row, no reason and no gate; every existing gate measures arrival. | Write `evidence/evictions.<date>-p<N>.tsv` from the `Pattern AW` diff, and add a gate that fails when an address on the previous commit's sell shelves is absent from this one **without a reason cell**. |
| 🔴 **`Gap 463-B`** | A novelty check keyed on a **guessed slug** manufactures false positives — `openSIS` read as uncarried when `OS4ED/openSIS-Classic` sits on 3 shelves. | Resolve the product name to an address through the probe **before** the `grep`, and key the check on the resolved address. |
| 🟡 **`Gap 463-C`** | `OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` share HEAD `8348cd069aa2`. Alias or undiverged fork is **unsettled**, and neither serves a root grant so the payload channel cannot settle it. | Run `gate-fork-direction`'s full-history channel on the pair. |
| 🔴 **`Gap 463-D`** | **The Middle East and Africa returned nothing on any EMEA leg** — EMEA's evidence here is EU-27 + UK + Germany only. | Run legs keyed on named national systems (as `p443` did for LATAM) rather than on the region word: Gulf ministry platforms, Nigerian and Kenyan HE systems, francophone African curricula. |
| 🟡 **`Gap 463-E`** | Skill-tier supply (**7 of 13** novel addresses) carries **derivation chains stated only in the README**. A `LICENSE` read grades such a row clean while saying nothing about what it was built from. | Make `p288`'s README channel standing for the skill tier: every skill-tier row records a provenance cell (declared upstream + its grant) or `PROVENANCE-UNSTATED`. |
| 🔴 **`Gap 446-A`** | **Still open, and still not closable by this pass.** `make hooks` was refused (`Code from External`); nothing in this pass is gate-attested. | Needs a harness permission decision, not a pass. |

## 🆕 `p462` — **No foundation row is added; the prescribed vertical-platform leg returned only carried addresses. 🟢 What changes is a GRANT and an ADDRESS: `openeducat/openeducat_erp` is `NOASSERTION` in the index and serves an explicit LGPL-3.0 payload at a default ref of `19.0`, and two carried addresses are confirmed rename aliases by HEAD sha while a third is confirmed NOT to be one.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN, and the reason is new.**
This pass is executing under a harness whose permission classifier **refused the `make hooks`
invocation outright** (`Code from External`) — not a proxy failure, not a missing target, a refusal
to execute the repository's own Makefile. So **nothing below is gate-attested**, and the gate's
inability to run is itself the standing obstacle: `Gap 446-A` cannot be closed by a pass that is
not permitted to run the gate.

### 🟢 `Gap 461-B` gains a first-hand instance: `NOASSERTION` is an index verdict, not an absent grant

[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) is classified
**`NOASSERTION`** (`"license": {"key": "other", "name": "Other"}`) by the GitHub index. Its payload
is not absent and not ambiguous:

| field | value |
|---|---|
| default ref | 🔴 **`19.0`** — not `main`, and `main` 404s |
| grant path | `19.0/LICENSE` (also served at `master`) |
| bytes · digest | **8 241 B** · `528f840368` |
| declared family | **LGPL-3.0** — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below"*, with the GPL text appended beneath it as the LGPL's base |
| notice obligation | the payload reserves bundled external libraries to *"other GPL-compatible licenses"*, per-file |

🔴 So an index-only reader records this platform as ungranted, and a `main`-assuming payload reader
records it as ungranted too — **two independent ways to lose a real, readable copyleft grant on the
same row.** The grant is LGPL-3.0: usable as a dependency boundary, not a tier Globant can
relicense.

### 🟢 Identity graded by HEAD sha — the channel `p461` did not have

`git ls-remote <addr> HEAD` works from this host and returns the commit the address resolves to.
Two addresses that return the **same sha** are the same repository; two that return **different
shas** are two repositories, whatever their licence payloads look like.

| address pair | raw `LICENSE` payload | HEAD sha, alias | HEAD sha, canonical | verdict |
|---|---|---|---|---|
| `openedx/edx-platform` → `openedx/openedx-platform` | identical · 35 136 B · `e12d78569742` | `addd09d7801b` | `addd09d7801b` | 🟢 **same repository** — rename alias, and it still resolves |
| `Vacademy-io/vacademy_platform` → `Vacademy-io/vacademy_edtech_platform` | identical · 34 523 B · `0d96a4ff68ad` | `3a9c66db938c` | `3a9c66db938c` | 🟢 **same repository** — rename alias, and it still resolves |
| `DaRL-GenAI/instructional_agents` vs `Hyan-Yao/instructional_agents` | identical · 1 067 B · `4e085d826a64` | `f835eb45f508` | `1c2a9f9e3d26` | 🔴 **NOT the same repository** — two live, divergent HEADs |
| `OpenEduCat-Inc/OpenEduCat` → `openeducat/openeducat_erp` | alias **404** at `19.0`, `master` and `main`; canonical **200** · 8 241 B · `528f840368` | 🔴 unresolvable — `ls-remote` falls through to a credential prompt | `46a5d7d40082` | 🔴 **alias is ABSENT**, not a redirect |

### 🔴 The rule this establishes, and it is reusable

🔴 **A byte-identical licence payload is near-zero evidence of repository identity, and for the
boilerplate grant families it is no evidence at all.** `p461` read an identical 1 067 B MIT text at
`DaRL-GenAI/instructional_agents` and `Hyan-Yao/instructional_agents` and concluded one was the
other's stale alias. The HEAD shas say otherwise: `f835eb45f508` ≠ `1c2a9f9e3d26`, two live
repositories with independent histories. The payloads match **because stock MIT text is
universal** — the same 1 067 B body appears on dozens of unrelated rows on these very shelves.
Identity is a property of the **tree**, and only the sha channel reads the tree.

### 🟡 Address hygiene for the foundation tier, stated as an action rather than a defect

🟢 Both confirmed aliases **still resolve and still serve the correct tree**, so no foundation row
is broken and nothing here is urgent. The canonical names are recorded so that future passes
grade the right address:

| carried address | canonical address to prefer | why it matters |
|---|---|---|
| `openedx/edx-platform` | `openedx/openedx-platform` | the index no longer resolves the old name, so an index-driven pass reads it as absent while `raw` and `git` both serve it |
| `Vacademy-io/vacademy_platform` | `Vacademy-io/vacademy_edtech_platform` | same failure mode, same remedy |

🔴 **And one address pair must NOT be merged:** `DaRL-GenAI/instructional_agents` and
`Hyan-Yao/instructional_agents` are two repositories (`f835eb45f508` vs `1c2a9f9e3d26`), not one
under two names. Collapsing them would lose a row.

### 🔴 The prescribed channel, graded in full — 36 tokens, and the novel repository yield is ZERO

This pass ran **the eight prescribed legs and no others**: the four global legs
(`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`,
`open source platform education ERP CRM SIS MIT Apache`, `AI education industry trends 2026`) and
the four regional legs (North America, EMEA, APAC, LATAM). Every repository-shaped token any leg
returned was graded against these shelves.

| | n | share |
|---|---|---|
| repository/project tokens returned and graded | **36** | |
| 🔴 already carried on these shelves | **34** | **94.4 %** |
| 🟡 unshelved | **2** | **5.6 %** |
| 🔴 **unshelved AND a repository — i.e. usable** | **0** | **0 %** |

🔴 **The two unshelved tokens are not repositories.** `BYJU'S` is a company name, returned by a
market-research vendor page as an APAC "key player"; `spacebasic.com` is the blog host that served
one of the vertical-platform hits. Neither is an address, a licence or a thing to build on.

🟢 **Fifth consecutive nil, and the first on the PRESCRIBED channel itself.** `p458`–`p461` reached
their nils on GitHub-API and topic-page channels while recording the prescribed web-search channel
separately. This pass ran the prescribed wording verbatim, global and per region, and it returns
**nothing these shelves do not hold** — so the saturation is now reproduced on the channel the
encargo actually specifies, not only on the substitutes built around it.

🟡 **Carried tokens, named so the denominator is auditable rather than asserted:**
`500-AI-Agents-Projects`, `ai-agents-for-beginners`, `agents-course`, `nanochat`, `llm-course`,
`ML-For-Beginners`, `OpenHands`, `MetaGPT`, `OpenClaw`, `CrewAI`, `LangChain`, `LangGraph`,
`smolagents`, `AutoGen`, `DeepTutor`, `OpenTutor`, `maxew6/ai-tutor-project`,
`krishna16-origin/ai-tutor`, `k-dense-ai/scientific-agent-skills`, `withmarbleapp/os-taxonomy`,
`HuggerHustle/ai-radar`, `ARUNAGIRINATHAN-K/awesome-ai-agents-2026`,
`caramaschiHG/awesome-ai-agents-2026`, `GegoK12`, `RosarioSIS`, `frappe/erpnext`, `Dolibarr`,
`OpenEduCat`, `Open edX`, `Moodle`, `Kolibri`, `BigBlueButton`, `Canvas`, `Pearson`.

## 🆕 `p461` — **No foundation row is added; the four candidate channels returned only addresses already carried. 🔴 What changes is the grant state of carried rows: `openeducat/openeducat_erp` is confirmed LGPL-3.0 by payload against an index that says `NOASSERTION`, and `openedx/edx-platform` is confirmed to be an ALIAS for `openedx/openedx-platform`.**

🔴 **Gate posture per `Gap 446-A`: `make hooks` was NOT RUN** — fresh clone, not the Makefile.
Nothing below is gate-attested.

### 🟢 The permissive foundation set, with index-exact ★ and payload-verified grants

🔵 Grants below are recorded with the channel that attested them. Where the index and the payload
disagree, **the payload governs** and the disagreement is recorded rather than resolved silently.

| repo | grant | attested by | ★ exact | last push | base for AI? |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | payload `COPYING.txt` 35 147 B (reproduced `p460`) | **7 543** | 2026-10-21 | ✅ plugin subsystem; copyleft — integrate at the API, do not vendor |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | **AGPL-3.0** | payload `LICENSE` 35 136 B · `e12d78569742` | **8 209** | 2026-10-26 | ⚠️ AGPL — network copyleft; XBlock boundary only |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | payload `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | **471** | 2026-10-26 | ✅ **the permissive seam into Open edX** |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | index + `license:mit` | **452** | 2026-10-18 | ✅ knowledge tracing, cleanest permissive core |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | index + `license:mit` | **316** | 2026-10-26 | ✅ course-catalogue front, MIT end to end |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | index + `license:mit` | **271** | 2026-10-26 | ✅ ITS with BKT, UC Berkeley |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | payload `LICENSE` 11 120 B · `0688f62d04f1` (reproduced `p460`) | **1 239** | 2026-10-26 | ✅ Apache-derived, permissive |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** | **payload 8 241 B — index says `NOASSERTION`** | **899** | 2026-10-26 | ✅ education ERP/SIS; weak copyleft, linkable |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | **GPL-3.0** | index `license:gpl-3.0` | **1 020** | 2026-10-26 | ✅ LATAM-weighted LMS; copyleft |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | **GPL-3.0** | index `license:gpl-3.0` | **637** | 2026-10-23 | ✅ school management / SIS |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **GPL-3.0** | index `license:gpl-3.0` | **505** | 2026-10-26 | ✅ EMEA-weighted LMS (DE/CH/AT) |

🟢 **Permissive subset Globant can build on without copyleft obligation — five rows:**
`openedx/XBlock` (Apache-2.0), `pykt-team/pykt-toolkit` (MIT), `openfun/richie` (MIT),
`CAHLR/OATutor` (MIT), `sakaiproject/sakai` (ECL-2.0). 🔵 Every other foundation row above is
copyleft of some strength, which is the single most load-bearing fact on this shelf and the reason
`Gap 461-B` matters: a `NOASSERTION` read as a permission puts AGPL and share-alike material
inside that five-row set.

### 🟢 Permissive knowledge-tracing bench — all MIT, all index-attested

🔵 `license:mit` over `topic:knowledge-tracing` returns **8 of 17** repos in the topic. The
permissive share of this sub-field is unusually high and the shelf should treat it as the
dependable corner:

| repo | grant | ★ exact | last push |
|---|---|---|---|
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT | **452** | 2026-10-18 |
| [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) | MIT | **194** | 2026-10-04 |
| [`jhljx/GKT`](https://github.com/jhljx/GKT) | MIT | **141** | 2026-09-23 |
| [`jilljenn/ktm`](https://github.com/jilljenn/ktm) | MIT | **140** | 2026-05-13 |
| [`lccasagrande/Deep-Knowledge-Tracing`](https://github.com/lccasagrande/Deep-Knowledge-Tracing) | MIT | **107** | 2026-09-07 |
| [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | MIT | **82** | 2026-10-22 |
| [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) | MIT | **80** | 2026-10-25 |
| [`THUwangcy/HawkesKT`](https://github.com/THUwangcy/HawkesKT) | MIT | **31** | 2026-09-16 |

🟡 `tswsxk/EduData` (**83**★) sits in the same topic but is **not** in the MIT set and was not
payload-probed this pass — recorded as unresolved, not as permissive.

### 🔴 Refused this pass — stated so the gap is informed rather than silent

| address | why not a foundation row |
|---|---|
| 🔴 `GeminiLight/awesome-ai-llm4education` (**221**★) | **NO GRANT** — 404 × 3. A paper index, and unvendorable regardless |
| 🔴 `ECNU-ICALK/EduChat` (**975**★) | **NO GRANT** + ~15 months stale |
| 🔴 `JushBJJ/Mr.-Ranedeer-AI-Tutor` (**29 548**★) | **NO GRANT** — the field's most-starred education repo is unusable |
| 🔴 `aaryansamanta/ai-ethos` (**498**★) | **NO GRANT** |

---
## 🆕 `p460` — **No foundation row is added. 🟢 But seven carried foundation grants were re-read first-hand from their bytes and ALL SEVEN reproduce exactly — and the one that appeared not to was this pass's own case-sensitivity defect, on a row these shelves had already got right.**

🔴 **Gate posture, stated first: `make hooks` was NOT RUN** — this pass reached the shelves through
a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 Instrument: a byte-read of the payload at `raw.githubusercontent.com`, gated on `%{http_code}`,
with two fabricated addresses as negative controls (both **404, 14-byte `404: Not Found`** —
`Gap 453-E` (d)'s exact mode, correctly refused).

### 🟢 Seven carried foundation grants, re-read and reproduced

| address | shelf value | read this pass | verdict |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 · `COPYING.txt` 35 147 B | **35 147 B** | 🟢 reproduced |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | AGPL-3.0 · 35 136 B · `e12d78569742` | **35 136 B · `e12d78569742`** | 🟢 reproduced |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | Apache-2.0 · `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | **11 358 B · `cfc7749b96f6`** | 🟢 reproduced **at the uppercase path the shelf names** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 ECL-2.0 · 11 120 B · `0688f62d04f1` | **11 120 B · `0688f62d04f1`** | 🟢 reproduced |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT | **MIT · 1 066 B · `f5f955194636`** | 🟢 confirmed, digest now on file |
| [`openfun/richie`](https://github.com/openfun/richie) | MIT | **MIT · 1 079 B · `e4b2a3148135`** | 🟢 confirmed, digest now on file |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT | **MIT · 1 105 B · `5baaaf977a28`** | 🟢 confirmed, digest now on file |

🟡 Three digests above (`pykt-toolkit`, `richie`, `OATutor`) are **new to this file** — the grants
were already correct, they simply had no byte count or digest recorded. That is the whole of this
pass's additive contribution to this shelf.

### 🔴 The defect, on the row that looked like a finding

🔴 This pass's grant ladder probed `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`
and four more — **and not `LICENSE.TXT`**. It therefore produced *"`openedx/XBlock` — NO GRANT at
9 probed paths, head `4b3f5246f43f`, resolved default ref `master`"*, for a **live** repository
(`AUTHORS` 1 373 B and `README.rst` 7 455 B both 200 on the same ref).

🟢 **The shelf was already right, and more specific than the instrument** — it carries the path as
**`LICENSE.TXT`, uppercase extension**, and had already recorded the trap verbatim: *"LICENSE.txt
404 x3, LICENSE.TXT -> 200"*. 🔵 The failure direction is `Gap 455-A`'s — a false *ungranted*
**discards a usable permissive dependency** — reached by a new mechanism: filename **case**, not
ref. 🔴 Registered as `Gap 460-A`: no carried probe on these shelves is known to be
case-insensitive on the extension, and the `REPO_LIVE_NO_GRANT` population has not been re-probed
for case variants.

## 🆕 `p459` — **No foundation row is added, and the reason is stated rather than padded: of 42 addresses probed, the 2 unshelved ones carry no licence grant and neither is foundation-grade.**

🔴 **Gate posture, stated first: `make hooks` was NOT RUN** — this pass reached the shelves
through a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 Instrument: a two-stage probe — `git ls-remote --symref` for liveness and default ref, then a
10-path grant read at that ref. **Controlled in both directions before use:**

| control | result |
|---|---|
| 🟢 `HKUDS/DeepTutor` — positive, asserted against the grant these shelves carry | **Apache-2.0**, `LICENSE` **11 408 B**, head `a31d82624c27` — **reproduced** |
| 🟢 two fabricated addresses — negative | both **`ADDRESS_DEAD`** |
| 🔴 **instrument defect, recorded against this pass, not against the shelves** | the probe's *fallback* licence matcher (a bare substring scan, used only when no licence title matches in the first 30 lines) read `withmarbleapp/os-taxonomy` as **"MIT"**. It is **not** MIT. The shelves' own first-hand record — **ODbL-1.0 + CC BY-SA 4.0**, `LICENSE` **25 289 B** — was re-read and **stands uncorrected**. Every grant quoted below was read from the licence title, never from the fallback |

### What was searched, and what was missing

🔵 Three legs against the GitHub repository-search API (`topic:ai-tutor`, `topic:education` +
`topic:ai-agent`, `topic:edtech` + `topic:education`/`topic:mcp-server`), plus the four prescribed
global web legs. 🔴 **Nothing foundation-grade was returned that these shelves do not already
carry.** The candidates that *looked* foundational on first pass were all already shelved:

| candidate | status on these shelves |
|---|---|
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | 🔵 already carried — ODbL-1.0 + CC BY-SA 4.0, 25 289 B |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔵 already carried, 🔴 correctly flagged **CC BY-NC-4.0** |
| [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🔵 already carried (23 files) |
| [`frappe/lms`](https://github.com/frappe/lms) · [`learningequality/kolibri`](https://github.com/learningequality/kolibri) · [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) · [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🔵 all already carried |

🟢 The existing foundation table below is **unchanged and still current** — every row in it was
reachable this pass. 🔴 What this pass establishes is that *adding* to it now requires a deeper or
different channel than the one the encargo prescribes, not another hour on the same one.

## 🆕 `p458` — **Two foundation-grade rows arriving from the GitHub API channel, and one of them is the first curriculum-graph row these shelves carry that is built from OFFICIAL curricula rather than a scrape**

🔵 Grants read first-hand at the resolved default ref; instrument and controls as recorded in
[`agents/top.md`](../agents/top.md).

| Repo | Licence (read at `HEAD`) | ★ | What it gives a build |
|---|---|---|---|
| [`enpasos/skillpilot`](https://github.com/enpasos/skillpilot) | **Apache-2.0** · 10 089 B `6bbe4ace8a18` | 3 | Curriculum-backed **skill graphs** with mastery tracking — dependency-aware learning paths generated from *official* curricula (currently German Gymnasium). Java/Spring Boot + React, MCP surface. |
| [`Man0dya/Tutor-AI`](https://github.com/Man0dya/Tutor-AI) | **Apache-2.0** · 10 251 B `0ac1681f915c` | 17 | A complete **multi-agent tutoring reference**: content generation → question-set generation → answer evaluation → feedback, as four separable agents. FastAPI + React, vector search. Useful as an architecture to copy, not a product to deploy. |

### 🟢 Why `skillpilot` is a foundation row and not an agent row

🔵 These shelves already carry two larger curriculum graphs, and **the grant is why neither
replaces this row** — both were re-probed first-hand this pass:

| graph | size | grant served at `HEAD` | usable in paid client work? |
|---|---|---|---|
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | 1 590 topics · 3 221 edges | 🟡 **ODbL** · 25 289 B `77d2692c3d64` | 🟡 Share-alike on the *database* — derived graphs must be re-published |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 1 644 points · 2 403 edges · **3 948 ★** | 🔴 **CC BY-NC 4.0** · 19 347 B `41003d4a7474` | 🔴 **No — NonCommercial bars it from paid work** |
| [`enpasos/skillpilot`](https://github.com/enpasos/skillpilot) | German Gymnasium, official | 🟢 **Apache-2.0** · 10 089 B `6bbe4ace8a18` | 🟢 **Yes** |

🟢 **So `skillpilot` differs on the two axes that decide an engagement, not on size.** Its graph is
derived from a **published state curriculum**, so the prerequisite edges can be defended to a
Kultusministerium rather than only to a product manager — and Apache-2.0 means the graph *and* the
mastery-tracking code are both buildable on, which is true of neither larger graph. 🔴 The largest
and fastest-growing of the three is the one a studio may not bill against.

🟡 Both rows are small by stars (3 and 17). 🔵 They are shelved on provenance and architecture, and
the star count is published here so nobody mistakes either for a widely-reviewed dependency.


## 🆕 `p457` — **🟢 A SUPPLY TIER THESE SHELVES HAVE NEVER CARRIED, AND IT IS THE ONE MOST OF THE WORLD'S SCHOOLS ACTUALLY RUN ON: paper assessment. Eight permissive rows — four OMR engines and four assistive/accessible-learning foundations — every grant read first-hand at the resolved default ref. 🔴 Plus the whole shelf re-read: 390 of 457 carried addresses serve a grant, and 64.6 % of them are MIT.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes. 🔵 Nothing
below is gate-attested; the instrument, its two fabricated negative controls and its two positive
controls are at [`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py).
🔴 **Seven defects in this pass's own code — five in the reader, two in the controls — are
published on [`agents/top.md`](../agents/top.md)** rather than hidden.

### 🔴 The absence this pass closes, and why it was invisible for 456 passes

🔵 Searched against these three shelves before searching the web: **`OMR`, `optical mark
recognition`, `bubble-sheet`, `mark recognition`, `phoneme`, `braille`, `sign language`,
`dyslexia`, `speech-to-text` — all NINE at ZERO mentions.** 🔴 **These shelves carry 457 addresses
for an industry whose dominant assessment instrument, across most of its install base, is a sheet
of paper** — and they carried nothing that reads one.

🟡 The mechanism is the one `p453` named: the vocabulary is the variable. Every discovery leg these
shelves have run was phrased in the language of *digital* education — LMS, MCP, tutor, autograder,
LTI, xAPI. **A school in Nepal grading NEET practice exams off an ADF scanner is not in that
vocabulary**, so it was never returned, and the silence read exactly like coverage.

### 🟢 Tier 7 — paper assessment (OMR). Every grant read at the resolved default ref this pass

| repo | grant | ref | what it is | region |
|---|---|---|---|---|
| [`Udayraj123/OMRChecker`](https://github.com/Udayraj123/OMRChecker) | 🟢 **MIT** · `LICENSE` **1 104 B** `3d72ab01aefd` | 🔴 `master` | The canonical OMR engine: reads marked sheets *"fast and accurately using a scanner 🖨 or your phone 🤳"* — **a phone camera is a supported input**, which is the whole low-infrastructure case | ⚪ Global · India-origin |
| [`crispin0007/OMR`](https://github.com/crispin0007/OMR) | 🟢 **Apache-2.0** · `LICENSE` **11 358 B** `cfc7749b96f6` | `main` | Full exam pipeline, **offline on one Windows PC with no internet and no fees**: design answer sheets → scan from any ADF scanner → marks, ranks, **merit lists**, Excel + PDF scorecards, optional negative marking. Scoped by its own README to **Nepal CEE, NEET, JEE and school exams** | 🟢 **APAC** |
| [`sajidbuet/OMRFlow`](https://github.com/sajidbuet/OMRFlow) | 🟢 **MIT** · `LICENSE` **1 081 B** `71787b5c24e2` | `main` | Examination-administration grade: template design, **uncertain-mark review**, **attendance reconciliation**, MCQ scoring, **auditable** Excel results, entirely local | 🟢 **APAC** |
| [`power0matin/omr-bubble-sheet-marker`](https://github.com/power0matin/omr-bubble-sheet-marker) | 🟢 **MIT** · `LICENSE` **1 072 B** `440f3c6ab70c` | `main` | Offline marker for MCQ sheets as **PDF or image** (OpenCV + PyMuPDF). 🟡 **The thinnest row of the four** — the README is largely badges, and it is shelved as a component, not a platform | ⚪ Global |

🔴 **One copyleft flag, stated rather than shelved as permissive:**
[`bthicks/OMR-Grader`](https://github.com/bthicks/OMR-Grader) is **GPL-3.0** (`LICENSE.txt`
**35 149 B** `3972dc9744f6`) — a Python/OpenCV bubble-sheet grader. 🟡 Usable, but it carries the
obligation outward and so is not a vendoring candidate for a client deliverable.

🔴 **One refusal:** [`sakethbachu/OMR-scanner`](https://github.com/sakethbachu/OMR-scanner) is live
at `master` and serves **no grant at any of 12 probed paths**.

🟢 **Why this is a foundations tier and not a curiosity:** `crispin0007/OMR` and `sajidbuet/OMRFlow`
both state **offline, single-machine operation** as a feature, not a limitation. That is the exact
deployment envelope of the institutions these shelves' regional sections describe as
under-served — and it is the one envelope the entire MCP/LMS-connector tier on these shelves
**cannot** serve, because every row in it assumes a hosted LMS and a network.

### 🟢 Tier 8 — assistive and accessible-learning foundations

🔵 Accessibility is a **statutory** requirement in the two regions these shelves sell into hardest
(IDEA and Section 504 in the US; the European Accessibility Act in the EU), and it was carried here
only as the word *"accessibility"* in prose. These are the readable, permissive foundations:

| repo | grant | ref | what it is | region |
|---|---|---|---|---|
| [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | 🟢 **MIT** · `LICENSE` **1 065 B** `f8f65c73234f` | `main` | **The strongest row in this tier.** MathML → speech **and braille** (**Nemeth, UEB Technical, CMU** and others) plus **navigation of math** by structure. Speech in **15 shipped languages** (Chinese Traditional, English, Finnish, French, German, Greek, Hungarian, Indonesian, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Vietnamese); sourced from the **DAISY Consortium** | ⚪ Global |
| [`AVauraTech/assistive-ai-accessibility-suite`](https://github.com/AVauraTech/assistive-ai-accessibility-suite) | 🟢 **MIT** · `LICENSE` **1 065 B** `142a4062de61` | `main` | Eight assistive tools in **one browser tab with no cloud dependency**: ASL fingerspelling, eye-gaze control, air writing, live captions, braille studio, scene description, document reader, depth obstacle warning. **MediaPipe on-device via WASM**, optional VLM with offline fallback | ⚪ Global |
| [`open-source-accessibility/monarch-message`](https://github.com/open-source-accessibility/monarch-message) | 🟢 **MIT** · `LICENSE` **1 082 B** `43433fb8ca32` | `main` | Braille messenger for the **APH Monarch** — the American Printing House's refreshable multi-line braille tablet, a device with a real US school install base. 🟡 Small surface, concrete hardware target | 🟢 **North America** |
| [`Sais-gallego/braillevision-ocr`](https://github.com/Sais-gallego/braillevision-ocr) | 🟢 **MIT** · `LICENSE` **1 069 B** `4fdf172c6b2d` | `main` | **Braille OCR in the reverse direction**: decodes *embossed and printed* 6-dot cells into text and speaks it. Full Grade-1 English: alphabet, numeric prefix `⠼`, capital indicator `⠠`, punctuation | ⚪ Global |

🔴 **One refusal:** [`davidjenner/OpenDyslexic-Converter`](https://github.com/davidjenner/OpenDyslexic-Converter)
is live at `main` with **no grant served**.

🟢 **The composition that makes this a tier rather than four rows:** `MathCAT` turns the *content*
accessible, `braillevision-ocr` turns *existing paper* accessible, `monarch-message` reaches the
*device*, and the AVaura suite covers the *input* modalities. 🔵 Wired together they are the
accessibility layer for the OMR tier above — see
[`compose/patterns.md`](../compose/patterns.md) `P457-2`.

### 🟢 The whole shelf re-read — `Gap 456-A`'s numbers, in the form that matters here

🔵 Full result and grading on [`agents/top.md`](../agents/top.md). For a foundations reader the two
load-bearing numbers are:

- 🟢 **390 of 457** carried addresses serve a grant at their resolved default ref; **252 are MIT**
  (**64.6 %** of grants read) and **49 Apache-2.0** — so **77 %** of the readable supply on these
  shelves is in the two families a client can build on without a service boundary.
- 🔴 **54 are `REPO_LIVE_NO_GRANT`** and **13 are dead**. 🟡 Of the 20 whose cell states a licence
  with no payload behind it, **8 are recoverable from an in-repo manifest** — `package.json`,
  `pyproject.toml` or a CRAN `DESCRIPTION` — and **12 are recoverable from neither channel**
  (`Gap 457-B`).

🟡 **A correction to this shelf, in the safe direction:** [`cran/exams`](https://github.com/cran/exams)
is carried as **GPL-3.0** and its `DESCRIPTION` grants **`GPL-2 | GPL-3` disjunctively** — the
integrator may elect **GPL-2.0**. The cell is narrower than the grant, not wrong.


## 🆕 `p456` — **🟢 Every foundational platform on this shelf now carries its RESOLVED default branch, and for 11 of them it is not what a bare `git clone` would suggest: ILIAS checks out `release_11`, Tutor `release`, OpenEduCat `19.0`, BigBlueButton `v4.0.x-develop`. 🟢 And the licence families this shelf carries are CONFIRMED — 14 of 15 off-list cells re-read byte-identical.**

🔴 **`make hooks` DENIED** (`Code from External`) — eleventh denial in twelve passes. 🔵 Nothing
below is gate-attested; 31 controls run in both directions
([`compose/code/p456-ref-resolution/controls.py`](../compose/code/p456-ref-resolution/controls.py)).

### 🟢 The ref column this shelf has never had, and why it is a foundations fact

🔵 A foundational repo is one a client **vendors, forks or pins**. For 15 of the 455 addresses
carried across these shelves the **resolved default branch is outside the ref list every pass
since `p449` guessed** — so a recipe that names a repository without naming a ref gets whatever
the project's maintainers point `HEAD` at, which for these eleven platforms is a **release line**,
not a trunk:

| foundation | address | resolved default branch | grant re-read at that ref | re-read agrees with the carried cell? |
|---|---|---|---|---|
| ILIAS | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | **GPL-3.0** · `LICENSE` | 🟢 byte-identical |
| BigBlueButton | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **`v4.0.x-develop`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Tutor (Open edX) | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **`release`** | **AGPL-3.0** · `LICENSE.txt` | 🟢 byte-identical |
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Gibbon | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **`v31.0.00`** | **GPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Edu-Sharing | [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | 🔴 **`maven/fixes/10.0`** | **GPL-3.0** · `LICENSE.txt` | 🟢 byte-identical |
| i-Educar | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | **GPL-2.0** · `LICENSE` | 🟢 byte-identical |
| RosarioSIS | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`mobile`** | **GPL-2.0** · `LICENSE` | 🟢 byte-identical |
| Krayin CRM | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** | **MIT** · `LICENSE` | 🟢 byte-identical |
| TinCanPython (xAPI) | [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | 🔴 **`3.x`** | **Apache-2.0** · `LICENSE` | 🟢 byte-identical |
| Caliper PHP | [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | 🔴 **`public`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |

🔴 **The operational consequence, and it is not cosmetic:** `git clone https://github.com/ILIAS-eLearning/ILIAS`
gives you `release_11`, not a trunk — a *maintenance line* that will stop moving. `overhangio/tutor`
gives `release`, which tracks whatever Open edX named current. 🟢 **Every clone or vendor step in
[`compose/patterns.md`](../compose/patterns.md) must name `-b <ref>` explicitly**, and the refs are
the column above. 🔵 Four further off-list cells are not foundations and are recorded in the
evidence rather than here: `lukecarroll15/blackboard-mcp` (`tcd`), `michaelsboost/ArabEngo`
(`gh-pages`), `jibrilsettles-dot/Arabic-Tutor` (🔵 default branch
`claude/eager-newton-boy1g0` — an agent session branch left as the project's default, and it
carries **no grant**), and `lanis-mobile/LanisAPI` (`deprecation-notice`, the corrected row).

### 🟢 The licence families on this shelf are confirmed, by a channel that could have refuted them

🟢 **14 of the 15 off-list cells re-read byte-identical** — same family, same digest — against
`p455`'s own ladder reproduced in `p456`'s instrument. Only `lanis-mobile/LanisAPI` differed, and
that is the corrected row on [`agents/top.md`](../agents/top.md). 🔵 So the exotic default branches
were **never** the hazard `Gap 455-A` feared: `HEAD` on `raw.githubusercontent.com` followed the
resolved default branch for **439 of 439 live addresses, zero divergences**, and that is why the
carried reads were right. Evidence:
[`evidence/carried-default-off-list.2026-10-26-p456.tsv`](../evidence/carried-default-off-list.2026-10-26-p456.tsv),
[`evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv`](../evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv).

### 🟢 The dead-address class is confirmed cross-channel, 455/455

🟢 16 addresses resolve nothing through `ls-remote`, and **every one is already carried as
`ADDRESS_DEAD` or `ABSENT`** from the independent 404 sweep — including both fabricated negative
controls. 🔵 `Gap 454-H` left standing the worry that an `ADDRESS_DEAD` cell might be an artefact
of guessing paths and refs; two independent channels agreeing on all 455 settles it.

### 🔵 What this does not establish

🔴 **`Gap 456-A`:** the **424** cells whose default branch is inside the guessed list were checked
for *ref identity* (`HEAD` == default, 439/439) but **not re-read for payload** at the resolved
ref. A payload drift there would be invisible to this pass.

## 🆕 `p455` — **🟢 `Gap 454-C` IS ANSWERED: the licence reader gains a VERSION AXIS, and the `edu-sharing` pair that `p454`'s `canon()` graded `AGREE` now disagrees — `GPL-2.0` declared against `GPL-3.0` served, mutually incompatible. 🔴 And the sweep that answer was supposed to deliver produced 88 apparent family disagreements that are RETRACTED IN FULL, because the mechanism is this pass's extractor and the shelves were right.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes. 🔵 Contracts
re-implemented and run independently; 34 controls pass
([`controls.py`](../compose/code/p455-version-axis/controls.py)).

### 🟢 `Gap 454-C` closed on the axis it named

`Gap 454-C` stated the defect and its cost precisely: *"A family-level reader cannot grade a
version-level incompatibility, and this base has one live."* `canon()` collapsed `GPL-2.0` and
`GPL-3.0` onto the family `GPL`, so the one real mismatch on these shelves graded `AGREE`.

🟢 **[`family_version.py`](../compose/code/p455-version-axis/family_version.py)** keeps `p454`'s
title-block anchor — the only region of a payload a preamble cannot reach — and reads the version
from the same anchor, where the GNU licences state it. Measured on the pair the gap named:

| | declared | served at `HEAD` | `p454` `canon()` | `p455` `canon()` |
|---|---|---|---|---|
| [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | npm `ngx-edu-sharing-api@10.0.1` → **`GNU GPL v2`** | **GPL *Version 3*** · `LICENSE.txt` `35 148` B `8b1ba204bb69` | 🔴 `GPL` vs `GPL` → **`AGREE`** | 🟢 `GPL-2.0` vs `GPL-3.0` → **`DISAGREE`**, and `compatible()` returns **`False`** |

🟢 **And a second axis the same title block does NOT carry, which decides whether the
incompatibility actually bites.** `GPL-2.0-only` cannot combine with `GPL-3.0`; `GPL-2.0-or-later`
can, because it may be taken forward. That election lives in the per-file notice and the
*How to Apply* appendix, never in the title block, so `only_or_later()` reads the whole payload and
returns **`UNSTATED`** when the payload does not say — guessing `or-later` invents a combination
right, guessing `only` invents a prohibition. 🟢 **Read first-hand this pass, it changes a live
verdict:** [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core)'s GPLv2 (`18 025` B
`a01259a1b522`) is **`or-later`**, so TAO *may* be combined with GPL-3.0 code — where a
version-only reader would have called it a dead end.

### 🔴 The sweep's headline is RETRACTED, and the mechanism is worth more than the number was

The sweep ran over **481 distinct addresses** across all eight shelves whose shelf line names a
GNU family ([`evidence/gnu-version-axis.2026-10-26-p455.tsv`](../evidence/gnu-version-axis.2026-10-26-p455.tsv)).
Its first run reported **99 `FAMILY_DISAGREE` (20.6 %)**. 🔴 **That number is an artefact, and so
is the 88 that survived a first correction.** Three mechanisms, each found by reading the shelf
line the verdict was built on:

1. 🔴 **Line-level co-occurrence.** The extractor attributed every GNU token on a line to every
   address on it. These shelves are prose and multi-project tables, so it "found"
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) claiming `GPL-3.0`
   (Kolibri is **MIT**) and [`junit-team/junit4`](https://github.com/junit-team/junit4) claiming
   `GPL` — 🔴 **and this pass's own first write of that sentence called JUnit 4 "EPL" from
   background knowledge rather than a read; re-probed, `junit-team/junit4` serves NO grant at
   any of 13 root paths (`REPO_LIVE_NO_GRANT`), so the shelf's `GPL` is unsupported and so was
   the correction.** Corrected to cell-level attribution: 481 → 461 cells.
2. 🔴 **Sole-address prose rows.** The correction's fallback — *a row naming exactly one address is
   about that address* — is also unsound, because a prose sentence mentioning one repository and
   one licence is not a grant assertion about that repository.
3. 🔴 **Per-subtree grants, which a root-only reader cannot grade at all.** The decisive case:
   [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) is carried as **MIT at
   root** (`1 071` B `22e7ab2dbddc`) **and GPL-3.0 on its `legacy_reference/` subtree**
   (`35 149` B `3972dc9744f6`), with an explicit instruction — *integrate over MCP, never vendor
   the repository*. The sweep compared a root payload against a claim that was never about the root.

🔵 **And the finding that makes this a closure rather than a failure: a previous pass had already
built the taxonomy.** The trending shelves classify exactly this population —
`DEPENDENCY-SCOPED` for Kolibri (*"explicitly scoped to dependencies … the repo is MIT and the
prose says so"*) and `BOUNDARY-NAMED` for
[`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (*"it is MIT while
in-tree Moodle plugins are GPL-3.0 — the licence boundary **is** the architecture finding"*).
🔴 **Registered as `Gap 455-B`:** a GNU sweep must CONSUME that taxonomy, not re-derive it, and
no shelf carries a machine-readable grant column that would let it. **On a prose shelf, adjacency
is not attribution** — the same rule `Gap 451` set for registry names and `Gap 454-I` for table
shapes, now measured a third time on a third channel.

### 🟢 What the sweep DOES establish, with its denominator

| verdict | cells | share | what it means |
|---|---|---|---|
| 🟢 `AGREE` | 306 | 66.4 % | payload grade matches a cell-attributed shelf claim |
| 🔴 `FAMILY_DISAGREE` | 88 | 19.1 % | 🔴 **RETRACTED as instrument error** — an upper bound on *apparent* disagreement, not a shelf-defect rate |
| 🔴 `UNCHECKABLE` | 56 | 12.1 % | `ADDRESS_DEAD` or `REPO_LIVE_NO_GRANT`: the carried grant cannot be checked against anything. 🔵 Consistent with `Gap 454-H`'s **22.5 %** on a smaller, differently-selected population |
| 🟡 `UNDER_SPECIFIED` | 11 | 2.4 % | 🟢 **The sound new number.** The shelf states a bare `GPL`/`LGPL`/`AGPL` with no version while the payload serves one — so these 11 cells **cannot support a compatibility decision in either direction** |
| 🔵 `AMBIGUOUS` (refused) | 20 | — | no cell-level attribution anywhere; excluded from the denominator and **named** in the evidence file, because a silently-dropped cell looks exactly like one that agreed |

### 🔴 Two more defects of this pass's own instrument, both caught by controls before publication

🔴 **`Gap 455-D` — `canon()` could not normalise the commonest shorthand there is.** The
version-stripping rule was `\bv(\d)` → digit. `l` and `v` are both word characters, so there is no
boundary inside **`gplv3`**: `"GNU GPL v2"` (spaced) normalised correctly and `GPLv3` (compact)
fell through to the identity branch and compared unequal to everything. The compact form is what
npm and crates.io actually serve. 🔵 `p454`'s own `FAMILY_TOKENS` anticipated it (`\bgplv?[23]\b`);
this pass's `canon()` did not — a defect **inside one pass, between two files**.

🔴 **`Gap 455-C` — a `200` is not evidence of a well-formed record.** `registry.npmjs.org/pawnote`
was read **twenty times**: nineteen returned `1.6.2 / GPL-3.0-or-later / LiterateInk/Pawnote.js`,
and **one returned HTTP 200 with a body that parsed as JSON and carried no `dist-tags` at all**.
An unguarded parser records that as *"the package declares no licence"* — a silent false negative
on the channel every registry-sourced cell on these shelves rests on. 🟢 Fixed by asserting record
**shape**, not status ([`fetch.py`](../compose/code/p455-version-axis/fetch.py) `REQUIRED_SHAPE`).
🔵 And the repeat reads are the reason this is stated as a rate rather than a flap: 12 consecutive
reads of three registries were **STABLE**, so the channel is sound and the *single-read* discipline
was not.

🔴 **Two control defects were this pass's too**, and they failed in the safe direction: the first
cut expected `MIT` where `p454` correctly grades a titleless payload `MIT (body form, no title)`,
and asserted that every GNU grade must *differ* from `p454`'s — wrong for `AGPL`, whose only live
version is 3.0, so there was nothing to refine. 🟢 Both were the **expectation's** error, not the
reader's, and both were corrected before any verdict was published.

### 🔴 `Gap 454-A` is still open, and this pass deliberately did not close it

`Gap 454-A` records that the defective 40-line-window reader in
[`p453-vocabulary-ledger/verify.py`](../compose/code/p453-vocabulary-ledger/verify.py) is *"still
what the next pass will import unless it reads this row"*. 🔴 **This pass read the row and did not
patch that file** — it built `family_version.py` beside it instead, for `p454`'s stated reason:
gate-adjacent code should not be edited by a pass that cannot run the gate against it, and the
gate has now been denied ten times in eleven passes. 🟢 **The actionable form:** any later pass
should import `family()` and `canon()` from
[`p455-version-axis/family_version.py`](../compose/code/p455-version-axis/family_version.py),
which is title-anchored, version-bearing and control-covered, and treat `verify.py::family` as
superseded. 🔴 Until the gate runs, that is a convention and not an enforcement.

## 🆕 `p454` — **🟢 `Gap 453-D` CLOSES for APAC with Indonesia's national register reached by four permissive clients, and a fifth region gains a foundational OER repository. 🔴 And that repository is the pass's second licence correction: npm declares `GNU GPL v2`, the payload at `HEAD` is `GPL-3.0` — two incompatible licences under one hint.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes. Nothing here is
gate-attested; the contracts were re-implemented and are listed in `intel/open-gaps.md`.

### 🟢 The APAC institution-registry layer — the region `Gap 453-D` named as unsearched

🔵 `Gap 453-D` recorded the layer as *"two regions deep and three never searched"*, with
**Indonesia, Japan, the Philippines** named. 🟢 **Indonesia closes.** Its national education data
system, **Dapodik** (*Data Pokok Pendidikan*, `dapo.kemendikdasmen.go.id`), is reachable from
permissively-granted code in three languages, and the student-identity tier (**VerValPD**) in a
fourth:

| repo | grant (first-hand, `HEAD`) | stratum | region |
|---|---|---|---|
| [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `1 739` B `29e7d361ee3d` | national register — typed SDK (TS/JS) | APAC |
| [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** · `1 105` B `ce39902853af` | national register — PHP client, CI-tested | APAC |
| [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `1 068` B `0ae5076b1e03` | student-identity verification (VerValPD) | APAC |
| [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `1 072` B `3508ba25c5ad` | provincial teacher-data aggregate | APAC |
| [`pipeworx-io/mcp-estat-japan`](https://github.com/pipeworx-io/mcp-estat-japan) | **MIT** · `1 070` B `42501667035e` | national statistics portal (e-Stat), education one domain of ~5 000 tables | APAC |

🟢 **Why this is a foundation and not a trend row: all four Indonesian grants are MIT, and they
stack.** The register (`dapodik-sdk` / `dapodik-api-php`), the identity tier (`vervalpd-node`) and
the aggregate tier (`dapodik-data-guru`) are three different strata of one national system, each
separately vendorable. That is the same shape `p453` closed for North America with IPEDS, and the
first time this base can say it for an APAC country.

### 🔴 EMEA/Global — a foundational OER repository, and a GPL **version** disagreement

| repo | registry hint | payload at `HEAD` | region |
|---|---|---|---|
| [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | npm `ngx-edu-sharing-api@10.0.1` declares **`GNU GPL v2`** | 🔴 **`GNU GENERAL PUBLIC LICENSE Version 3`** · `LICENSE.txt` `35 148` B `8b1ba204bb69` | EMEA *(Germany)* |

🟢 **edu-sharing is a genuine foundational asset** — an open-source repository/federation layer for
**open educational resources**, with maintained Angular API and UI bindings (`ngx-edu-sharing-api`,
`ngx-edu-sharing-ui`, modified `2026-08-07`), used across German-speaking state education portals.

🔴 **But the licence hint is wrong in the one way that cannot be waved through: GPL-2.0 and
GPL-3.0 are mutually incompatible.** A deliverable assembled on the npm field's authority could
not lawfully combine edu-sharing with a GPL-2.0-only dependency. 🔵 And this base's **own** family
reader hides it: `canon()` collapses `GPL-2.0-only` and `GPL-3.0` onto the family `GPL`, so the
sweep graded the pair `AGREE`. 🔴 That is `Gap 454-C`, registered this pass — **a family-level
reader cannot grade a version-level incompatibility**, and three of this base's carried GPL cells
are family-level only.

### 🔵 Philippines — an INFORMED ABSENCE, with a denominator and a named cause

🔴 **No Philippine school-registry asset surfaced, and the reason is the search term, not the
country.** `deped` returned **59 candidates and 0 education assets**: on Packagist it matches the
substring `dep` in `deptrac/deptrac`, `php-di/php-di`, `symfony/dependency-injection`,
`shipmonk/composer-dependency-analyser` and every other dependency-shaped package. `psa`
(Philippine Statistics Authority) matched ConnectWise PSA, PureScript `psa` and Oracle `oci-psa`.

🟡 **What DID surface is a different stratum, and it is real:** the **PSGC** (Philippine Standard
Geographic Code) layer — [`pcofilada/psgc`](https://github.com/pcofilada/psgc),
[`jobuntux/psgc`](https://github.com/jobuntux/psgc),
[`anthonygacis/psgc-js`](https://github.com/anthonygacis/psgc-js),
[`aivangogh/ph-address`](https://github.com/aivangogh/ph-address) — administrative geography, the
same stratum as LATAM's `municipios-br`. 🔵 Grants **not** read first-hand this pass and therefore
**not** celled; they are candidates for `p455`, not rows.

🟢 **Stated so the absence is not mistaken for coverage:** the Philippine *school* register
(DepEd's EBEIS/LIS) is **not** reachable from any package registry this pass searched, and the
unambiguous vocabulary for it — a long, distinctive proper name — **has not been identified**.
That is the actionable half of the nil.

## 🆕 `p453` — **🟢 `Gap 452-D` IS CLOSED FOR NORTH AMERICA, AND IT WAS THE CHEAP GAP `p452` SAID IT WAS: five permissively-granted US institution-registry assets, all read first-hand at `HEAD`, where the prior pass could name none and had searched for none. 🔴 APAC is closed as an INFORMED ABSENCE instead: India's school directory exists at 1.47 M rows and NOT ONE of its packaged forms carries a permissive grant.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

### 🟢 The North America institution-registry layer — the gap `p452` opened, closed one pass later

🔵 `p452` registered `Gap 452-D` as *"the institution-registry layer is one country deep and four
of five regions have never been searched for it"*, and named the US series (NCES CCD, IPEDS) whose
*"packaged permissive form is simply unknown here"*. 🟢 It is known now.

| repository | grant, read first-hand at `HEAD` | what it actually is | region |
|---|---|---|---|
| [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) | 🟢 **MIT** — `LICENSE` **1 115 B `sha256₁₂ a3a16c648652`** | 🟢 **The strongest row of the five.** An open **Common Data Set** API and preservation archive: each school's CDS document found, extracted to a canonical schema (**1 105 fields** keyed by stable question number from the official 2025-26 template) and published beside the raw source, plus an NCES/IPEDS federal baseline keyed by zero-padded `UNITID`. Self-reported integrity audit of 2026-08-06: **6 322 institutions** in the federal directory, **4 071** archived CDS documents, **262 537** `cds_fields` rows | 🟢 **North America** — US |
| [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) | 🟢 **MIT** — `LICENSE` **1 056 B `sha256₁₂ 1126322e2cc8`** | Builds a harmonised **DuckDB** database from 20+ years of IPEDS in one command: **~27 M rows across 23 tables**, every US postsecondary institution **1997-2024** — admissions, enrolment, completions, tuition, aid, graduation rates, staffing | 🟢 **North America** — US |
| [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) | 🟢 **MIT** — `LICENSE` **1 088 B `sha256₁₂ e04b31a1be21`** *(body-form grant: no title line, opens at `Permission is hereby granted`)* | Python package that pre-processes and standardises IPEDS into a queryable store; carries **institutional-characteristics directory** data, which is the registry axis proper. `v0.0.9` adds 2025 data | 🟢 **North America** — US |
| [`UrbanInstitute/ipeds-scraper`](https://github.com/UrbanInstitute/ipeds-scraper) | 🟢 **MIT** — `LICENSE.md` **1 058 B `sha256₁₂ bac93c5411aa`** *(body-form)* | Downloads IPEDS complete data files and dictionaries — the ingestion leg under the two rows above. Institutional publisher (**Urban Institute**) | 🟢 **North America** — US |
| [`rhawrami/genpeds`](https://github.com/rhawrami/genpeds) | 🟢 **MIT** — `LICENSE.md` **1 071 B `sha256₁₂ c39fac37d50c`** *(body-form)* | Python API for requesting and cleaning IPEDS data, `pip`-installable | 🟢 **North America** — US |

🟢 **Why this is a foundations row and not an agents row.** None of the five is an agent. They are
the **system of record an engagement keys its rollout to** — the question *"which institutions
exist, and what is true of them"* — which `p452` identified as the layer this base had eight
platforms to *run* a school with and almost no data about *which schools exist*.

### 🔴 `ajhaller/IPEDS` — a grant that is neither present nor absent, and the mechanism is the R ecosystem

🔴 Its `LICENSE` is **43 B** — `YEAR: 2022` / `COPYRIGHT HOLDER: IPEDS authors`. 🔵 **That is not a
grant and not an absence**: `DESCRIPTION` declares `License: MIT + file LICENSE`, and the MIT text
is served from `LICENSE.md`. The R convention **splits the grant across two files**, so a payload
reader sees 43 B of metadata and a code-licence grader returns `UNREAD`.
🟢 **This base already records the sibling class** — `cran/catR` is carried as *"GPL (>= 3) —
`DESCRIPTION` only"* — so what `p453` adds is the **two-file composite** (`cran/shiny` is the
control instance, `YEAR`/`COPYRIGHT HOLDER` stub plus `MIT + file LICENSE`), not the ecosystem
itself. 🔴 Registered as `Gap 453-C`.

### 🔴 APAC: recorded as an informed absence, with the denominator that makes it informative

🔴 **India's school directory is the largest in the world and none of its packaged forms is
permissively granted.** Probed first-hand at `HEAD` this pass:

| address | grant at `HEAD` | consequence |
|---|---|---|
| [`deedy/cbse_schools_data`](https://github.com/deedy/cbse_schools_data) | 🟡 **CC-BY-SA-4.0** — `LICENSE` **20 131 B `sha256₁₂ 1f5de47ca3fb`** | ~20 367 CBSE schools (2018). 🔴 **Share-alike**: a derived registry inherits the obligation, so it is not a permissive base |
| [`learnram/ads-schools-data`](https://github.com/learnram/ads-schools-data) | 🔴 **no payload at 9 probed paths** | UDISE+-derived national directory, ~28 MB gzipped CSV — **ungranted** |
| [`dougj892/public-datasets`](https://github.com/dougj892/public-datasets) | 🔴 **no payload at 9 probed paths** | India education datasets — ungranted |
| [`unknownsteve7/UDISE_DATA_ANALYSIS`](https://github.com/unknownsteve7/UDISE_DATA_ANALYSIS) | 🔴 **no payload** | 4 GB pipeline over 1.47 M schools, 2023-24 + 2024-25 — ungranted |
| [`mukulyadav0118/india-school-education-analytics`](https://github.com/mukulyadav0118/india-school-education-analytics) | 🔴 **no payload** | UDISE+ 2025-26, seven states — ungranted |

🔵 **This is the kind of absence the encargo asks to be written down rather than left silent:
the supply exists, it is large, and 4 of 5 packaged forms grant nothing**, so an APAC engagement
keyed to a school registry must go to the UDISE+ portal's own terms, not to GitHub. 🔴 `Gap 453-D`
carries the unsearched remainder: **Global** and the rest of **APAC** (Japan, Indonesia,
Philippines) have still not been searched for this layer.

### 🟢 One LATAM data row, and it is a licence disagreement as well as a registry asset

| repository | grant | surface | region |
|---|---|---|---|
| [`nataliasm23/icones-bandeiras-br-uf`](https://github.com/nataliasm23/icones-bandeiras-br-uf) | 🔴 **CC0-1.0** — `LICENSE` **7 048 B `sha256₁₂ a2010f343487`**. 🔴 **npm `municipios-br@3.2.1` declares `MIT`** — see `Gap 453-A` | Brazilian municipality and UF (state) reference data with flag icons — the administrative-geography key a LATAM rollout joins a school list to | 🟢 **LATAM** — Brazil |

🔵 **CC0 is the right instrument for data and the wrong one to infer from a code manifest**: the
registry's `MIT` would have been published here as the grant had the payload not been read.

## 🆕 `p452` — **🟢 `Gap 450-C` ANSWERED WITH A NUMBER after carrying one pass: 394 carried byte cells re-read with the corrected method, 361 reproduce EXACTLY, and the uncorrected trailing-newline method accounts for 11 of them — 2.8 %, not a sweep-wide defect. 🔴 Getting that number took FOUR cuts of the extractor, and the first three each produced a confident phantom-drift list of 200, 104 and 5 rows. Every phantom was caught by a control, never by inspection.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

### 🟢 `Gap 450-C`'s open question, and the answer

`p450` found that reading a payload through shell command substitution **strips the trailing
newline**, so every byte count taken that way runs **exactly one byte low** — silently, and
selectively, since a payload with no trailing newline measures identically both ways. 🔵 It left the
question: *"how many byte counts already on these shelves were produced by the uncorrected
method?"*, with the warning that a one-byte-low cell is indistinguishable from drift.

🟢 The instrument is
[`compose/code/p452-byte-census/extract_cells.py`](../compose/code/p452-byte-census/extract_cells.py);
the census output is committed to
[`evidence/byte-cell-census.2026-10-26-p452.tsv`](../evidence/byte-cell-census.2026-10-26-p452.tsv).
Every cell was re-read with `curl -w '%{size_download}'`, the method `p450` proved correct.

| verdict | n | share of 394 | reading |
|---|---|---|---|
| 🟢 `EXACT` | **361** | 91.6 % | the carried cell is reproduced to the byte |
| 🔴 `OFF_BY_ONE` | **13** *(11 confirmed by hand)* | 2.8 % | `measured − carried = 1`, and **every one of them ends in a trailing newline** — `p450`'s mechanism exactly |
| ⚪ `UNREACHABLE` | **12** | 3.0 % | `404` at `HEAD`; several are addresses this base already carries as withdrawn |
| 🟡 `OTHER_DELTA` | **8** *(5 genuine)* | 1.3 % | a real disagreement, listed below |

🟢 **The mechanism is confirmed and it is bounded.** Not one of the 361 `EXACT` cells is off by one,
and all 13 off-by-one cells end in a trailing newline — so the `+1` class is **not noise**, it is
`p450`'s defect, and it touched under 3 % of the population rather than the sweep `Gap 450-C` feared.

### 🔴 The eleven confirmed, each one a cell to correct rather than a drift to investigate

| address | carried | re-read | ends in newline? |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 11 342 B | 🔴 **11 343 B** | 🟢 yes |
| [`Git-Kaushal/AI-Teacher-Training`](https://github.com/Git-Kaushal/AI-Teacher-Training) | 2 099 B | 🔴 **2 100 B** | 🟢 yes |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 11 356 B | 🔴 **11 357 B** | 🟢 yes |
| [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) | 1 524 B | 🔴 **1 525 B** | 🟢 yes |
| [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | 1 067 B | 🔴 **1 068 B** | 🟢 yes |
| [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | 1 071 B | 🔴 **1 072 B** | 🟢 yes |
| [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | 1 076 B | 🔴 **1 077 B** | 🟢 yes |
| [`baker-jr-john/automated-summary-evaluation-llm`](https://github.com/baker-jr-john/automated-summary-evaluation-llm) | 1 070 B | 🔴 **1 071 B** | 🟢 yes |
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 11 350 B | 🔴 **11 351 B** | 🟢 yes |
| [`0xnavarro/IA-PARA-TODOS`](https://github.com/0xnavarro/IA-PARA-TODOS) | 11 470 B | 🔴 **11 471 B** | 🟢 yes |
| [`ClassroomIO/ClassroomIO`](https://github.com/ClassroomIO/ClassroomIO) | 34 522 B | 🔴 **34 523 B** | 🟢 yes |

🟡 Two further `OFF_BY_ONE` rows are **withheld**, not published: `Ebimsv/AITutorAgent`, whose shelf
text in fact reads `1 072 B` — equal to the re-read, so the `1 071` my extractor paired with it came
off a multi-address line; and `GibbonEdu/core`, whose matched line is about `frappe/education`, so
the attribution cannot be confirmed. 🔵 A cell I cannot attribute is not a finding.

### 🟡 The five genuine disagreements — candidates for upstream drift, not for correction

| address | path | carried | re-read | δ |
|---|---|---|---|---|
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | `LICENSE` | 1 520 B | 1 094 B | 🔴 **−426** |
| [`Django-CRM/Django-CRM`](https://github.com/Django-CRM/Django-CRM) | `LICENSE` | 1 069 B | 1 101 B | 🟡 **+32** |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | `LICENSE` | 1 073 B | 1 092 B | 🟡 **+19** |
| [`junit-team/junit4`](https://github.com/junit-team/junit4) | `LICENSE-junit.txt` | 11 374 B | 11 376 B | 🟡 **+2** |
| [`jagmarques/awesome-eu-ai-act`](https://github.com/jagmarques/awesome-eu-ai-act) | `LICENSE` | 7 047 B | 7 049 B | 🟡 **+2** |

🔵 A `+2` on an 11 KB Apache payload is the shape of a copyright-year edit; **−426 B** is not, and
`MysterionRise/adaptive-knowledge-graph` is the one row here that warrants a grant re-read rather
than a byte correction.

### 🔴 Four cuts of the extractor, and what each wrong cut would have published

🔴 **This is recorded in full because the failure mode is invisible without a control, and three
separate cuts of this instrument produced a fluent, specific, entirely wrong drift report.**

| cut | defect | phantom "drifts" | how it was caught |
|---|---|---|---|
| 🔴 1 | `(\d(?:SEP?\d{3})*)` — unanchored, separator **optional**: on `11 408 B` the engine skipped the leading digit and returned `1408` | **200 of 395**, in a telltale band of +10000 / +20000 / +30000 | 🟢 a hand-written control row asserting DeepTutor is **11 408 B** disagreed with the extracted `1 408` |
| 🔴 2 | negative lookbehind and mandatory separator added — but the separator class held only **spaces**: on `1,070 B` it matched `070` | **104**, all exactly +1000 / +11000 / +35000 | 🟢 `cat -A` on the raw shelf bytes showed the comma |
| 🔴 3 | comma added; one cell still failed | **1** | 🟢 an 8-value self-check: the shelf writes `**1.071 B**` with a **period** |
| 🟢 4 | all four separators; self-check gates the run | **0** | 🟢 8/8 self-check, then 361/394 `EXACT` |

🟢 **The finding underneath the bug, and it is why no earlier pass built this census: across 451
passes these shelves group thousands FOUR different ways** — U+202F narrow no-break space, plain
space, comma, and period. 🔴 Any single-separator reader silently truncates the other three **and
reports the truncation as upstream drift**. The extractor now carries all four and will not run at
all unless it reproduces eight cells read by hand, one for each separator form.

🔴 **A fifth defect, of a different kind: the path key is a basename.** `LICENSE` at the repository
root and `legacy_reference/LICENSE` on a vendored subtree collapse to one key, which paired
`krzysztofbury/librus-mcp`'s **35 149 B GPL-3.0 subtree** figure with its **1 071 B MIT root** cell
and reported a −34 078 B drift. 🟢 The root cell re-reads at **1 071 B `sha256₁₂ 22e7ab2dbddc`** —
byte-identical *and* hash-identical to what this base carries, and `p442`'s GPL-3.0 subtree finding
stands untouched. 🔵 **Four of the five withheld rows are this one defect**, so basename keying is
the single largest source of phantom drift in a census of this kind.

### 🟢 One foundational repository promoted — and it is reference DATA, not code

| repository | grant, read first-hand at `HEAD` | what it is | region |
|---|---|---|---|
| [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) | 🟢 **MIT** — `LICENSE` **1 101 B `sha256₁₂ 691e4ec845d7`**, title `MIT License`. 🔴 npm declares only `SEE LICENSE IN LICENSE`, so **the payload is the grant and the manifest is not** | A machine-readable registry of **Algeria's education estate**, published as scoped npm packages with GPS coordinates, contacts, capacity and boarding: 🟢 **11 858 schools** and kindergartens classified by cycle (primaire / CEM / lycée / préscolaire) from OpenStreetMap; 🟢 **1 932 vocational-training establishments** — 856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs — from **MFEP / takwin.dz**; 🟢 **177 higher-education institutions** — universities, grandes écoles, ENS, centres — with official sites, from **MESRS**. All **69 wilayas**. Trilingual `README` (EN / FR / AR). 10 versions, 2026-06-22 → 2026-10-21 | 🟢 **EMEA** — Algeria, asserted by the ministries it sources and the wilaya coverage |

🟢 **Why it belongs on a foundations shelf and not an agents shelf.** It executes nothing. It is the
layer every education engagement needs first and that this base has had almost nowhere: an
authoritative, permissively-licensed **master list of institutions** to key a deployment, a rollout
plan or a market sizing against. 🔵 **And it moves this base's EMEA coverage off Europe for the
first time** — the EMEA tier here has been Romania (`ase-moodle-mcp`), France, the Netherlands and
Germany; Algeria and the Maghreb were an unstated absence. 🔴 Stated plainly as `Gap 452-E`: the
*rest* of the Middle East and Africa remains absent, and this one address does not close it.

## 🆕 `p451` — **🟢 THE "CIRCULAR GRANT" THIS FILE HAS CARRIED SINCE `p390` IS NOW PROVED RATHER THAN INFERRED — and the proof makes it worse: npm's own record shows `beadkit` published TWO versions whose licence string names a file in a repository that no longer exists, so the grant is not merely unread, it is UNREADABLE BY ANYONE. 🔴 And a second address on this shelf tier turns out to have shipped FOUR `proprietary` versions before its last two went BSD-3-Clause.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no cell below is
gate-attested. Stated first, per `Gap 446-A`. Six denials in seven passes.

### 🟢 `ale-alejandro/beadkit` — the circle closed, with dates

🔵 This file has recorded since `p390` that `beadkit`'s *"manifest reads `"SEE LICENSE IN LICENSE"`
— pointing at a file in a repository nobody can read"*, and `compose/patterns.md` carries it as the
worked example of the class. 🟢 **The registry record now supplies what the inference lacked:**

| measured 2026-10-26 | value |
|---|---|
| npm package | **`beadkit`**, **`0.1.0`** latest, **2** versions |
| window | **created 2026-08-26**, **last modified 2026-10-12** |
| maintainer | `alebuild.co` |
| `repository` back-link | 🟢 **`git+https://github.com/ale-alejandro/beadkit.git`** — the exact carried slug |
| declared licence | 🔴 **`SEE LICENSE IN LICENSE`** |
| the repository that holds `LICENSE` | 🔴 `404` on `raw`, `128` on `ls-remote`, byte-identical to a fabricated control |

🟢 **So the address was real** — a registry does not invent a back-link for 2 published versions —
🔴 **and the grant is unrecoverable on every channel this host has.** 🔴 **Not recommendable, and
for a stronger reason than "unverified": there is no longer any party able to verify it.** The
package is installable today; its licence is not knowable today. 🔵 For a Globant engagement that
is the worst of the three states — *available, attractive and unlicensable*.

### 🔴 `dev-cucei-itrans/siiau-api-client` — a licence that CHANGED mid-life, recoverable only from Packagist

🔵 [`verticals/solutions.md`](../verticals/solutions.md) has carried this address as the only SIS
integration SDK that ever existed for SIIAU, *"marked abandoned"* on Packagist. 🟢 **Read
first-hand this pass** (`packagist.org/packages/dev-cucei-itrans/siiau-api-client.json`, after the
positive control `laravel/framework` → `200`):

| version | published | licence as published |
|---|---|---|
| `v1.0.0-BETA` | 2023-10-20 | 🔴 **`proprietary`** |
| `v1.0.0` | 2023-10-23 | 🔴 **`proprietary`** |
| `v1.1.0` | 2024-08-13 | 🔴 **`proprietary`** |
| `v1.1.1` | 2024-08-14 | 🔴 **`proprietary`** |
| `v1.1.2` | 2024-08-25 | 🟢 **`BSD-3-Clause`** |
| `dev-main` | 2024-10-08 | 🟢 **`BSD-3-Clause`** |

🔵 Package created **2023-10-13**, **7** versions, **1 023** downloads, **7** stars recorded by
Packagist, `abandoned: true`. 🔴 **Four of seven published versions are `proprietary`**, and the
repository that could settle the intent is gone — **Packagist is now the only channel on which
this grant exists at all.**

🔴 **The consequence is a pinning rule, not a footnote:** a composer constraint such as `^1.0`
resolves into the **proprietary** band. 🟢 **Only `v1.1.2` or later is BSD-3-Clause**, and because
the repository is withdrawn, that boundary can never be re-read from source. 🔵 Any engagement
touching SIIAU must pin `>=1.1.2` **and** carry the Packagist record as its grant evidence, or
have no grant at all.

### 🟢 The classification this shelf tier gains: licence RECOVERABILITY, independent of licence

🔵 These shelves grade *what* a licence is. 🔴 **Six withdrawn addresses this pass show that is one
axis short** — a grant can be permissive and still unusable because nothing can serve its text:

| recoverability class | n (of the 6 withdrawn) | instances |
|---|---|---|
| 🟢 **Registry-recoverable** — a registry declares an SPDX identifier | **3** | `interactive-quiz-kit` (MIT) · `unist-blackboard-mcp` (MIT) · `GraphLMS` (MIT) |
| 🟡 **Manifest-only** — identifier declared, no payload ever shipped | **1** | `santillana-ai/tutor-sdk` (MIT in `@santillana-ai/create-tutor-app`, no payload in the tarball) |
| 🔴 **Version-dependent** — the identifier changes across published versions | **1** | `siiau-api-client` (`proprietary` → `BSD-3-Clause` at `v1.1.2`) |
| 🔴 **Unrecoverable** — the declaration points at a file nobody can serve | **1** | `beadkit` (`SEE LICENSE IN LICENSE`) |

🟢 **Only the first class is buildable on without a legal review**, and it is 3 of 6. 🔵 That ratio
is the reason this axis is worth carrying: *"MIT"* on a withdrawn address is three different
situations, and two of them are not a grant.

---

## 🆕 `p450` — **🔴 A ONE-PATH README PROBE WOULD HAVE CONDEMNED FOUR OF THIS SHELF'S MOST IMPORTANT PLATFORMS AS DEAD — `openedx/edx-platform`, `oppia/oppia`, `overhangio/tutor` and `h5p/h5p-php-library` all serve 404 at `HEAD/README.md` while being entirely alive. 🟢 And a licence instrument written THIS PASS was caught misreading GPL-3.0 as LGPL on 2 of 15 reads, because GPLv3's own closing paragraph recommends the LGPL; it was fixed before publication and both readings are kept side by side.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`), so no cell below is
gate-attested. Stated first, per `Gap 446-A`.

### 🔴 The false-negative class a single-path probe publishes as dead — 19 of 375 addresses

`agents/top.md`'s `p450` section establishes the two-stage probe. This is the half that matters to
*this* file: **19 live addresses serve nothing at `HEAD/README.md`** and are recovered only by the
`ls-remote` escalation (`evidence/shelf-reachability-census.2026-10-26-p450.tsv`):

| address | 🟢 README path, MEASURED | default ref | 🔴 verdict a one-path `README.md` probe prints |
|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **`README.rst`** | `master` (294 heads) | 🔴 **DEAD** — the reference Open edX platform |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **`README.rst`** | 🔴 **`release`** (17 heads) | 🔴 **DEAD** — the canonical Open edX deployer |
| [openedx/XBlock](https://github.com/openedx/XBlock) · [openedx/edx-ora2](https://github.com/openedx/edx-ora2) · [openedx/xblock-lti-consumer](https://github.com/openedx/xblock-lti-consumer) · [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | **`README.rst`** ×4 | `master` ×3, `main` ×1 | 🔴 **DEAD ×4** — the whole XBlock extension surface, incl. ORA2 (open response assessment) |
| [raccoongang/openedx-ai-extensions](https://github.com/raccoongang/openedx-ai-extensions) · [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) | **`README.rst`** ×2 | `main` ×2 | 🔴 **DEAD ×2** — the EMEA and LATAM Open edX integrators |
| [inducer/relate](https://github.com/inducer/relate) · [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **`README.rst`** ×2 | `main`, `master` | 🔴 **DEAD ×2** — incl. the LTI 1.3 Python library, MIT, first-hand read this pass |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🟡 **`README.txt`** | `master` (60 heads) | 🔴 **DEAD** — embedded in nearly every LMS |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟡 **`README.markdown`** | `master` | 🔴 **DEAD** — the open SIS of the India/APAC shelf |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) · [arthtyagi/judge](https://github.com/arthtyagi/judge) · [ivmelo/suapbot](https://github.com/ivmelo/suapbot) · [juan-c-cardenas/sia-scraper](https://github.com/juan-c-cardenas/sia-scraper) | 🔴 **`readme.md`** — lowercase ×4 | `main` ×1, `master` ×3 | 🔴 **DEAD ×4** — and this is `Gap 449-B`'s case-sensitivity class, now MEASURED rather than asserted |
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 **none at 10 probed paths** | 🔴 **`develop`** (500 heads) | 🔴 **DEAD** — Apache-2.0, grant read first-hand this pass |
| [cran/catR](https://github.com/cran/catR) · [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | 🔴 **none at 10 probed paths** | `master`, `main` | 🟡 live, and genuinely without a root README |

🟢 **Measured distribution of the 19 — this is the finding, not the anecdotes.** README path:
**`.rst` 10**, lowercase **`readme.md` 4**, none-at-10-paths **3**, `README.txt` **1**,
`README.markdown` **1**. Default ref: **`master` 11, `main` 5, `develop` 1, `release` 1** — 🔴 **only
5 of 19 are on `main`**, and two of the most consequential addresses on this shelf default to
`develop` (Oppia) and `release` (Tutor).

🔴 **Four of the nineteen are pure case collisions**, which settles the open half of `Gap 449-B`
with a number: `raw.githubusercontent.com` is **case-sensitive on the path** while GitHub's web UI
is not, so `readme.md` is invisible to a `README.md` probe. 🟢 That is **21 % of this file's
false-negative class** caused by one character of case.

🟡 **`Gap 420-B`'s mechanism, answered for ONE of its four cases and explicitly not the others.**
`Gap 420-B` asked why four refs that `ls-remote` lists serve nothing on `raw` at *"nine common
control paths"*. 🟢 **For `projectfedena/fedena` the mechanism is now named: its root README is
`README.markdown`**, an extension outside any nine-path control set — so the absence was the
probe's, not the repository's. 🔴 **The other three are NOT answered here and the difference is the
ref.** `Gap 420-B` probed *non-default* refs (`gh-pages`, `Version_8.0`,
`projectfedena-patch-1`, a feature branch); this pass probed **`HEAD` only**. For
`Seechange-edu/act-ai-tutor-backend` even `HEAD` serves nothing at ten paths, so that case is
reproduced and still unexplained. 🔵 The empty-orphan-vs-LFS question stays open; what is now
closed is the assumption that a nine-path control set is exhaustive. 🟢 **The general mechanism is
stated as a rule: `raw` is a PATH server, not a repository server** — it resolves
`{ref}/{exact-cased-path}` and nothing else, so the README's extension, its case, and the default
ref are three independent variables and a probe that fixes all three measures none of them.

🔴 **Consequence for the standing protocol, stated as a rule:** a 404 at one path is **never** a
reachability verdict on this shelf, because **1 in 20 live addresses here fails it** — and the
failures are concentrated in the platform tier, not the long tail. `T104`'s finding that *"a grant's
PATH is a function of the REF"* has a sibling: **a README's path is a function of the ecosystem.**

### 🟢 Fifteen grants re-read first-hand — and the instrument was wrong before it was right

Read through the `raw` channel at seven candidate paths each, **2026-10-26**
(`evidence/licence-title-anchored.2026-10-26-p450.tsv`, both classifiers kept side by side):

| repo | grant path | 🟢 family *(title-anchored)* | bytes |
|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `LICENSE` | 🟢 **Apache-2.0** | 11 408 |
| [oppia/oppia](https://github.com/oppia/oppia) | `LICENSE` | 🟢 **Apache-2.0** | 11 358 |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | `LICENSE` | 🟢 **Apache-2.0** | 11 343 |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `LICENSE` | 🟢 **MIT** | 1 092 |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | `LICENSE` | 🟢 **MIT** | 1 105 |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | `LICENSE` | 🟢 **MIT** | 1 132 |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `LICENSE` | 🟢 **MIT** | 1 097 |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `LICENSE` | 🟢 **MIT** | 1 071 |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | `LICENSE` | 🟢 **MIT** | 1 070 |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | `LICENSE.md` | 🟢 **BSD** | 1 542 |
| [moodle/moodle](https://github.com/moodle/moodle) | `COPYING.txt` | 🔴 **GPL-3.0** | 35 147 |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `LICENSE.txt` | 🔴 **GPL-3.0** | 35 146 |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | `LICENSE` | 🔴 **AGPL-3.0** | 35 136 |
| [overhangio/tutor](https://github.com/overhangio/tutor) | `LICENSE.txt` | 🔴 **AGPL-3.0** | 34 523 |
| [UCL-INGI/INGInious](https://github.com/UCL-INGI/INGInious) | `LICENSE` | 🔴 **AGPL-3.0** | 34 764 |

🔴 **The defect, declared because it was the instrument's and it nearly reached a table.** A
whole-body `grep -i "GNU LESSER"` classifier returned **LGPL** for `moodle/moodle` and
`h5p/h5p-php-library`. Both are **GPL-3.0**. The cause is in the licence text itself: GPLv3's
closing *"How to Apply"* paragraph reads *"…if your program is a subroutine library… use the GNU
Lesser General Public License instead of this License"*, so **every GPLv3 file matches an LGPL
whole-body grep.** 🟢 **Fix: anchor the family to the first six non-blank lines — the title — and
test LESSER before GENERAL.** 2 of 15 reads flipped; 13 were unaffected.

🟢 **Two independent confirmations fall out of the corrected read.** `moodle/moodle`'s grant is at
**`COPYING.txt`**, exactly where `T104` placed it, at **35 147 B**. And `h5p/h5p-php-library`'s
`LICENSE.txt` carries **the same GPLv3 text at 35 146 B — one byte short of Moodle's, the trailing
newline being the whole difference** — which corroborates
this file's line 954 (*"routinely described as MIT; it is not"*) on a channel that pass did not use.
🔵 That carried row is **confirmed, not amended**; the contradicting row lives in
`verticals/solutions.md` and is fixed there this pass.

### 🔴 A SECOND instrument defect, caught the same way, and it is the one that would have looked like drift

🔴 **Every byte count in the table above was one short on first measurement.** Reading a payload
through shell command substitution (`$(curl …)`) **strips the trailing newline**, so any grant file
ending in `\n` measured one byte under its true length. 🟢 **Fix: take the length from the transfer,
not from the captured string** — `curl -w '%{size_download}'`. 🔴 **The defect is silent and
selective**: `Ed-Fi-ODS`'s `LICENSE.txt` has **no** trailing newline, so it measured **10 172 B**
both ways and looked like a confirmation that the method was sound.

🟢 **The corrected method reproduces three cells this base published on earlier passes, to the
digit** — which is the test that matters under `gate-cell-reproduction`:

| cell | carried on these shelves | 🟢 `p450` authoritative re-read |
|---|---|---|
| `HKUDS/DeepTutor` `LICENSE` | **11 408 B** *(`repos/foundations.md`)* | 🟢 **11 408** — EXACT |
| `learningequality/kolibri` `LICENSE` | **1 097 B** | 🟢 **1 097** — EXACT |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` `LICENSE.txt` | **10 172 B** *(reproduced by `p449`)* | 🟢 **10 172** — EXACT |

🔴 **Had the uncorrected numbers been published, all three would have read one byte low** and a
future pass would have recorded drift on cells that never moved — a fabricated finding on a real
gate. 🔵 **Rule for any pass that measures a payload: the length is a property of the transfer, and
a string that has been through a shell is not the payload.** 🟢 The full GPL-3.0 text on these
shelves is **35 147 B** (Moodle `COPYING.txt`, Chamilo root `LICENSE`), which the corrected method
now agrees with.
## 🆕 `p449` — **🟢 TWO PUBLISHED PAYLOAD CELLS REPRODUCE TO THE DIGIT ON AN INDEPENDENT FETCH, including `p448`'s North American headline: `Ed-Fi-ODS` at 10 172 B and `XBlock` at 11 358 B. 🔴 But the probe that read them is case-sensitive and returned THREE false 404s against a live row first — and the probe this base is instructed to use (`curl -sI`) returns 403 on EVERY real GitHub repo on this host.**

🟢 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` RAN** — fourth trial after
three denials, so `p448`'s settlement of that gap as *"a property of the host class"* is
**refuted**; the denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 **two
of them NEW and both `p448`'s**. Three green on exit; the fourth is `DECLARED_RED` and left
(`Gap 449-D`).

### 🟢 Cell reproduction — the two most load-bearing grants on these shelves, re-read first-hand

| address | cell this shelf records | 🟢 `p449` independent fetch | verdict |
|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | Apache-2.0 · `LICENSE.txt` **10 172 B** | 🟢 **200 / 10 172 B** | 🟢 **EXACT** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | Apache-2.0 · `LICENSE.TXT` **11 358 B** | 🟢 **200 / 11 358 B** | 🟢 **EXACT** |

🔵 `Ed-Fi-ODS` is `p448`'s headline — **the only permissively-licensed system of record on these
shelves**, reached through a state-shaped NA leg after six region-level nils. 🟢 It is now
double-sourced across two passes and two hosts. Nine further shelved rows returned `200` with
byte sizes in the same sweep; none is contradicted.

### 🔴 `Gap 449-A` — the prescribed probe cannot verify a single row on this host

| probe | real repo | fake control | usable? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s -r 0-200 https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s https://api.github.com/repos/<slug>` | — | 🔴 **403** | 🔴 **cannot discriminate** |
| 🟢 `curl -s https://raw.githubusercontent.com/<slug>/<branch>/<path>` | 🟢 **200** + bytes | 🟢 **404 / 14 B** | 🟢 **YES** |

🔴 `github.com` HTML is 403 for **every** real repository here while `git clone` of the same
address succeeds. Obeyed literally, *"verify every URL with `curl -sI`; a 404 is not a finding"*
would condemn **all ~134 addresses this base has shelved.** 🟢 The sound probe needs a **negative
control**, and it has one: `zzz-fake-org-p449/zzz-fake-repo` → `404 / 14 B`
(`evidence/url-probe-soundness.2026-10-26-p449.tsv`).

### 🔴 `Gap 449-B` — and it failed toward "dead row" three times before it succeeded, on a row that was never dead

`openedx/XBlock` read **404** at `master/LICENSE.txt`, `main/LICENSE.txt` and `main/LICENSE`.
🟢 This shelf records `LICENSE.`**`TXT`** — at that exact case, **200 / 11 358 B**. 🔴
`raw.githubusercontent.com` is **case-sensitive**: normalising case **manufactures** dead rows,
and this base has a `LICENSE.TXT`/`License.txt`/`LICENSE` mix across its rows. 🔵 Rule:
**probe the case the shelf recorded; a 404 against a shelved cell is a probe finding until the
case is re-checked.** The same instrument-defect direction `Trend 48` named — toward the answer
already believed, which here is *"the row is stale"*.

### 🔴 Zero new foundational rows, and the nil is reported with its interval attached

Four global legs returned only shelved addresses (`os-taxonomy` 10 word-scoped files, `Ed-Fi` 10,
`OpenEduCat` 10). 🔵 Per `Gap 448-A`, now answered: the schedule is **hourly** (median
**61.1 min**, n=309) against a **daily** trending channel, so an unchanged channel is expected at
**P ≈ 95.8 %** and this nil is **not** evidence about supply.

---

## 🆕 `p448` — **🟢 THE NORTH AMERICAN SYSTEM OF RECORD HAS A GRANT, AND IT IS APACHE-2.0: `Ed-Fi-ODS` read first-hand at `LICENSE.txt` 10 172 B · `59899c6091b5`, reached through the state channel that six consecutive region-level NA legs failed to find. 🟢 `openSIS`'s below-root grant REPRODUCES to the digit. 🔴 Gate DENIED, third consecutive pass.**

🔴 **Gate posture: `make hooks` DENIED** (`Gap 446-A`, third consecutive pass, third container).
Nothing below is gate-checked; every cell carries its command.

### 🟢 A new foundational row, and it is the one `Gap 447-D` was blocking

🔵 Texas's TEA has **mandated** that student-information vendors submit to TSDS through **API
transactions** built on TEDS, and TEDS is *"a collection of data standards based on the national
**Ed-Fi** core"* — so the NA state system of record **is** an Ed-Fi deployment. That makes
`Ed-Fi-ODS` a foundations row rather than an integration curiosity. Grant read this hour over
the `raw.githubusercontent.com` channel (the one channel `Gap 446-D` shows returns **200**):

| repo | grant path | bytes | `sha256`[:12] | licence | verdict |
|---|---|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | `LICENSE.txt` | **10 172** | `59899c6091b5` | 🟢 **Apache-2.0** | 🟢 **GRANT-PRESENT**, HEAD `4d626f9ab257` |
| same | `NOTICES.md` | **233 924** | `609e95c99d9b` | third-party notices | 🟡 a 234 kB notices file is a **dependency-closure obligation**, not a blocker |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | — | — | — | — | 🟢 reachable, HEAD `b6b72e594bc4` |

🟢 **Why this row is worth more than its licence line.** Every other system-of-record row on
these shelves is either copyleft (`SIGAA` GPL-3.0, `suapbot` AGPL-3.0, `openSIS` GPL-2.0,
`RosarioSIS` GPL-2.0) or carries **no grant at all** (`sia-unal-mcp`). 🟢 `Ed-Fi-ODS` is the
**first permissively-licensed system of record on this shelf** — and it is the one a US state
*requires* its vendors to speak to. 🔵 That is a **vendor-and-build** row, not a
read-and-reimplement row.

🟡 **Bounded, and the bound is named:** the 234 kB `NOTICES.md` means an Ed-Fi-derived
deliverable owes a dependency-closure pass before it ships
(`compose/code/dependency-licence-closure` is the existing instrument). Apache-2.0 at the root
does **not** clear the tree — that is `Trend 40`'s whole point.

### 🟢 `openSIS`'s below-root grant reproduces, and the absence re-enumerates

`p4xx` published `openSIS Classic`'s grant at `docs/License.txt` · **17 286 B** ·
`224ac3d403e3` · GPL-2.0. Re-read this hour, independently:

| check | result |
|---|---|
| `docs/License.txt` payload | 🟢 **17 286 B · `224ac3d403e3`** — reproduces the published cell **to the digit** |
| first line | `GNU GENERAL PUBLIC LICENSE` |
| root grant paths probed | 🔴 **9 of 9 return 404** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license`, `license.txt`, `LICENCE`, `Licence.txt`) |
| README's own statement | *"openSIS is an Open Source Project licensed under the GNU General Public License"*, pointing at `docs/License.txt` |

🟢 **`ABSENCE-ENUMERATED` at root, `GRANT-PRESENT` below it** — a second, independent
confirmation of `Trend 40` (*the second grant lives below the root*), and a validation of the
raw-channel + `sha256`[:12] method **against an already-published cell** before any new cell
was written this pass.

### 🟢 Pinned rows on this shelf: all four HELD

| row | published pin | live HEAD | verdict |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `d073ad444fe5` | `d073ad444fe5` | 🟢 **HELD** |
| [`frappe/lms`](https://github.com/frappe/lms) | `5d6df8e3ed8e` | `5d6df8e3ed8e` | 🟢 **HELD** |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | `7bd8b6794cb7` | `7bd8b6794cb7` | 🟢 **HELD** |
| [`GeminiLight/awesome-ai-llm4education`](https://github.com/GeminiLight/awesome-ai-llm4education) | `48f2d16ca617` | `48f2d16ca617` | 🟢 **HELD** |

🔴 **But do not read that 4-of-4 as reassurance, because this pass measured what it is worth.**
Those pins are **43 minutes** old (`p447` committed 00:58:40Z, `p448` read 01:41:58Z). Over the
proper denominator — **496** simulated pinnings across **36** of these repositories — only
**67.3 %** of pins survive 24 h. 🔴 `p447`'s published budget line (*"17 of 18 of this base's
pins survived 24 h, so this is a cheap minority repair"*) is **survivorship-biased** and is
corrected in `Pattern BA`. 🟢 The predictor that actually works, and the one to apply before
putting any row below into a client deliverable, is **age of the commit at the moment you pin
it**: ≥ 7 days → **97.4 %** survival; < 7 days → **48.9 %**.

🔵 **Instrument validation for that claim, against a cell this base already published:**
`Apomera/AlloFlow`'s two refs date to `2026-10-24T12:35:30-04:00` and
`2026-10-25T18:50:44-04:00` — reproducing `p447`'s published *"pinned 10-24 12:35 with HEAD at
10-25 18:50"* **to the minute**.

---

## 🆕 `p447` — **🔴 Gate posture: DENIED, no baseline (`Gap 446-A`). 🟢 No foundational repo changes grant this pass, and that is a MEASURED statement rather than an unexamined one: every pinned row on this shelf was re-resolved against its live HEAD, and the single mover's licence payload is byte-identical across the move.**

🟢 **Every pinned row on the three sell shelves was re-resolved this hour** —
`git ls-remote <slug> HEAD`, 18 line-scoped rows, no GitHub API (403 here). **17 of 18 pins are
still exact.** The foundations rows specifically (`OpenOLAT/OpenOLAT` `d073ad444fe5`,
`frappe/lms` `5d6df8e3ed8e`, `withmarbleapp/os-taxonomy` `7bd8b6794cb7`,
`GeminiLight/awesome-ai-llm4education` `48f2d16ca617`) are **all unchanged**.

🟢 **The one mover is not a foundations row, and its grant did not move:** `Apomera/AlloFlow`
`LICENSE` is **35 442 B · `698099632698`** at both refs. 🔵 Which means **no grant on this shelf
requires re-grading this pass** — stated as a measurement with its instrument, not as silence.

🔴 **What this shelf still cannot do, and it is worth naming here rather than only in the gap
register:** `make hooks` has now been **denied on two consecutive passes**, so none of the
above is gate-checked. 🟢 The mitigation is the one `Gap 446-A` prescribes — every cell is
published with the command that produced it, and the hash method (`sha256` first 12 over raw
bytes) was validated against an already-published cell (`p433`'s `698099632698`) **before** any
new cell was written.

🔴 **Discovery added nothing.** `OpenOLAT`, `sakaiproject/sakai`, `openeducat/openeducat_erp`
and `francoisjacquet/rosariosis` all re-returned from the global platform leg; **all four are
already on this shelf**. Second consecutive saturated hour.

---

## 🆕 `p446` — **🟢 An upstream this base has audited twice has now published its OWN provenance review, and it is first-hand readable: `krzysztofbury/librus-mcp` ships a 9 662 B `LICENSE_REVIEW.md` that confirms `p442`'s GPL-3.0 subtree finding from the other side — and names a THIRD lane this base did not have, in which the MIT grant does NOT hold**

🔵 **How this was found.** Not by a search leg. `p446` re-measured a published payload cell to
validate its own hashing method (`agents/top.md` `p446`), and the licence-path enumeration over
the live tree returned **three** paths where `p442` recorded two:

```
LICENSE                     1 071 B · 22e7ab2dbddc   MIT          (reproduces p442)
legacy_reference/LICENSE   35 149 B · 3972dc9744f6   GPL-3.0-only (reproduces p442)
LICENSE_REVIEW.md           9 662 B · 6905cca1f0b4   🆕 NEW — a provenance review
```

🟢 **`p442`'s two cells reproduce to the digit** from an independent blobless clone this hour,
which is the strongest confirmation this base has of its own subtree instrument.

### 🟢 What the upstream says, in its own words, and why it matters commercially

| what the review states | first-hand quote | consequence for an engagement |
|---|---|---|
| the GPL subtree is deliberate and quarantined | *"Original 1.x source … preserved under the original GPL-3.0-only license. **Excluded from every 2.0 build inventory.** No relicensing or runtime fallback."* | 🟢 **Installing the published wheel/sdist does not pull GPL-3.0.** `p442` could only say *"a tree copy carries it"*; this says the **distributed artefact is clean** |
| the licence HISTORY is non-monotone | *"The root originally used MIT, then switched to GPL-3.0-only in `1a59c56` because apix's distributed license contradicted its MIT package metadata."* | 🔴 **MIT → GPL-3.0 → MIT on one root path.** A single-cell read at any one commit is right about that commit and wrong about the project |
| 🔴 **a flattened bundle is NOT approved** | *"This review approves the independent MCP distributions and ordinary separate dependency installation, **not an all-MIT standalone bundle**. Anyone bundling the whole installed environment … must review their additional notices, LGPL source/relinking obligations and resource terms separately."* | 🔴 **This is the lane an engagement actually ships** — one container image, one PyInstaller binary, one vendored wheelhouse |
| the named hazard in that lane is `lxml` | *"Its binary wheels can bundle zlib (zlib license), **iconv (LGPL-2.1)**, libxml2, libxslt and libexslt (MIT) … Some schema-transformation resources are described as **unlicensed** in the upstream notice."* | 🔴 **LGPL-2.1 relinking obligations and an unlicensed resource set** arrive inside a wheel nobody reads |

### 🔴 The third lane, stated plainly, because this base has been publishing two

| lane | grant status | who does this |
|---|---|---|
| integrate over the MCP interface, process boundary | 🟢 MIT holds | the disposition `p442` published |
| `git clone` and vendor the tree | 🔴 GPL-3.0-only arrives at `legacy_reference/` | the hazard `p442` named |
| 🆕 **`pip install`, then flatten the environment into one shipped artefact** | 🔴 **outside the upstream's own approval**; LGPL-2.1 + unlicensed resources via `lxml` | 🔴 **the default delivery shape of a studio engagement** |

🟢 **Prescription, and it is cheap:** the MIT lane survives a container **if** the dependency
distributions keep their own licence files inside the image and are not relinked or
repackaged — which is the ordinary `pip install` layout, and breaks the moment anyone runs a
single-binary packer. 🔵 Put that sentence in the engagement's build review, not in its legal
review, because the thing that violates it is a `Dockerfile` optimisation.

### 🟢 Why this is a foundations finding and not an agents one

🔵 `librus-python-api` (MIT, on this file) is the dependency the review is *about*: the pin moved
`1.0.2 → 1.6.2 → 1.6.3` across **2026-10-09 / -19 / -22**, each step with its PyPI licence
expression re-inspected by the upstream and recorded with a date. 🟢 **That is a maintained
licence-provenance trail on a foundational dependency — the artefact this base asks engagements
to produce, published by a single-maintainer project.** It is the reference implementation of
`Pattern AX`'s per-platform licence probe, done by the supplier instead of the consumer, and it
is worth citing as such.

🔴 **One limit, stated:** the review is the upstream's own engineering inventory and says so
(*"not legal advice"*). It is **evidence of diligence**, not a warranty, and the 35 149 B
GPL-3.0 payload is still physically in the tree.


## 🆕 `p445` — **Three new SIGAA addresses, and all three land in the COPYLEFT tier — so the Brazilian system-of-record integration layer is now known to be real supply that cannot be vendored. 🔴 Zero permissive rows added, and the reason is measured: the mandated discovery legs returned 0 new addresses from 14 candidates**

🔵 **Where these came from.** `Gap 444-B` named three unrun legs — a Peruvian university's
**system-of-record** noun, a UdelaR platform noun for Uruguay, and Mexico beyond UANL. All
three were run. Mexico returned one address and it is **deleted**; Uruguay and Peru returned
nothing; and the **SIGAA** channel `p443` opened returned three addresses nobody here had
seen. Mechanism, the two nils and the saturation measurement:
[`repos/trending.md`](trending.md) `p445`.

### 🟡 Copyleft and current-enough to read — integrate over the interface, never vendor

Every cell read first-hand on **2026-10-25**: existence and real default ref via
`git ls-remote --symref`, **every** grant path via `git ls-tree -r` over a blobless shallow
clone, every payload measured from the file (so `P834`'s trailing-newline run is in the byte
count). Driver: `compose/code/p445-publisher-class-census/probe_tranche.sh`. Evidence:
[`evidence/verified-repos.2026-10-25-p445.tsv`](../evidence/verified-repos.2026-10-25-p445.tsv).

| Repo | Licence | HEAD | Payload | Region | Why it is here, and the bound on using it |
|---|---|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 **GPL-3.0** | `cbdcf32a9188` · 2017-01-26 · 168 files | `LICENSE` 35 141 B · `589ed823e9a8` | **LATAM** (Brazil) | The **largest and most API-shaped** of the three: a Rails app that parses UFPB's **SIGAA** and exposes curriculum data at `/api/curricula`, via the author's own `sigaa_parser` gem. 🟢 The useful artefact is the **parser's logic and the endpoint shape**, which is what an engagement needs to rebuild. 🔴 GPL-3.0 reaches a distributed derivative, so this is a **read-and-reimplement** row |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 **GPL-3.0** | `85b9a51f5603` · 2020-01-04 · 25 files | `LICENSE` 35 149 B · `3972dc9744f6` | **LATAM** (Brazil) | Python client/CLI that authenticates against **any** SIGAA instance by configurable base URL — so it is the **portable** one of the three rather than UFPB-specific. 🔴 Carries a registry defect worth knowing: its PyPI record's `license` field is **EMPTY** while the repository ships a complete GPL-3.0 payload, so every registry-reading scanner will report this strongly-copyleft package as unlicensed |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 **GPL-3.0** | `4fa17f22c442` · 2016-02-07 · 14 files | `LICENSE` 35 141 B · `589ed823e9a8` | **LATAM** (Brazil) | Sinatra service over the same UFPB SIGAA curriculum data, self-described as dated and use-at-your-own-risk. 🔴 Ten years stale and superseded by the row above it. Shelved only as the **reference shape** for "SIGAA behind an HTTP API", never as a dependency |

🟢 **What the three together establish, which no single row does.** SIGAA — the system of
record at the Brazilian federal universities — **has** a public integration layer, in two
languages, with a working parser and a documented endpoint shape. 🔴 **And it is uniformly
GPL-3.0 and 6–10 years stale.** So the sellable shape at a Brazilian federal university is
*reimplement the parser against the interface these repositories document*, on a clean
permissive base, and the three rows above are **specification, not supply**. Recipe:
`Pattern AY`.

🔵 **This also sharpens `p444`'s correction of `Trend 42` rather than just agreeing with it.**
`p443` published *the student side of the glass is permissive, 6 of 8*; `p444` refuted it over
37 addresses (*permissive is 22 %, modal outcome is no licence*). This pass adds a third
reading: on **one platform, measured end to end, the student side is neither permissive nor
unlicensed — it is uniformly copyleft, 3 of 3.** The honest generalisation is that **the
licence distribution is a property of the PLATFORM's developer community, not of the side of
the glass**, which is `Trend 45`'s second half.

### 🔴 Zero permissive rows added, and the denominators are published rather than implied

| leg | candidates | 🟢 new to this base | permissive and new |
|---|---|---|---|
| 4 × mandated global English legs | 🔴 0 addresses returned | 🔴 **0** | 🔴 **0** |
| LMS MCP servers (Canvas + Moodle) | 10 | 🔴 **0** — all already here, up to **77** prior mentions | 🔴 **0** |
| SIGAA platform noun | 3 | 🟢 **3** | 🔴 **0** (all GPL-3.0) |
| SIIAU platform noun (Mexico) | 1 | 🔴 **0** — 🔴 `git ls-remote` **DOES NOT RESOLVE** | 🔴 **0** |
| UdelaR / `bedelías` noun (Uruguay) | 🔴 0 | 🔴 **0** | 🔴 **0** |
| Peru system-of-record noun | 🔴 0 | 🔴 **0** | 🔴 **0** |

🔵 **Read the top row before concluding the tier is saturated.** The ten MCP candidates were
not *rejected* — they were **already shelved**, several of them on this file and on
`agents/top.md`. Generic English discovery is exhausted for this base (`p443` got 1 of 29, this
pass got 0 of 10 on a differently-shaped query); the platform-noun channel is the one still
paying, and it has now paid on three consecutive passes.

---

## 🆕 `p444` — **The LATAM academic-portal tier triples, and two things the licence column alone would never have shown: 🔴 across the 37 addresses the PLATFORM-NAME legs returned, the permissive-and-maintained intersection is EXACTLY ONE — and 🟢 the best address of the pass came from a DIFFERENT leg shape entirely, which is the more useful finding**

🟢 **What was added and why it is small.** `p443` opened this tier with six Brazilian and
Argentine SIGAA/SIU-Guaraní addresses. `p444` ran the same channel at Mexico (SIASE), Brazil
(SUAP), Chile (U-Cursos, UCampus) and Colombia (SIA UNAL) and verified **37** addresses
first-hand. Eight carry a permissive grant. **Seven of those eight have not been touched since
2021.**

🔴 **The cross-tab is the finding, and no single column shows it.** Licence and recency,
measured over all 37 (`git log -1 --format=%cs` at the probed HEAD):

| grant | 🟢 live (HEAD 2026) | 🟡 2023–2025 | 🔴 dead (≤ 2022) | total |
|---|---|---|---|---|
| 🟢 **MIT / BSD** | 🟢 **1** | 1 | 🔴 **6** | 8 |
| GPL-3.0 | 2 | 3 | 4 | 9 |
| AGPL-3.0 | 0 | 0 | 2 | 2 |
| 🔴 **no grant at all** | 5 | 4 | 9 | 🔴 **18** |
| **total** | **8** | **8** | **21** | **37** |

🔵 **Read the top-left cell.** A screen on licence alone returns eight "build-on" addresses and
feels like a tier. A screen on licence **and** last commit returns **one**. This base has
screened on licence and stars for many passes; `p415` already measured stars as a weak positive
class, and this is the same lesson arriving through the recency axis. **Shelved below with the
true HEAD date in every row**, because a 2019 MIT scraper against a portal that has since
changed its HTML is not a starting point — it is a worked example.

### 🟢 The rows that are both permissive and current

🔵 **The second one is the methodological finding of this file.** `sia-unal-bridge` came from
the platform-name leg that `p443` prescribed. `django-auth-suap` came from a leg this pass ran
almost as an afterthought — the platform's **expanded name** (*"suap sistema unificado
administracao"*), asked to find whether the SUAP **platform itself** was open source. It is not;
but that leg returned **12 results of which 3 are production-grade**, and its best address is
better engineered than anything the bare-acronym leg found in four countries. **An ecosystem leg
and a name leg are not the same channel** (`Gap 444-E`).

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| 🟢 [django-by-kelsoncm/django-auth-suap](https://github.com/django-by-kelsoncm/django-auth-suap) | 🟢 **MIT** | `1f0b4e1a` · **2026-09-05** | `LICENSE.md` 1 065 B · `113d1a85e628` | 🟢 **LATAM — Brazil. The strongest LATAM address on these shelves, and the direct answer to this pass's IFRN finding.** Django **OAuth2 authentication backend for SUAP**, the Instituto Federal academic-management system — i.e. *the same job as `ifrn-oficial/cliente_suap_django`, which carries no grant at all*. 245 files: **98 `.py`, 92 `.rst` of Sphinx documentation**, published to **PyPI as `django-suap-auth`**, GitHub Actions CI + Codecov + pre-commit, `SECURITY.md`, bilingual PT-BR/EN README, declared support for **Django 5.2 and 6.0**, and an `audit/` submodule with middleware, migrations and an `audit_archive` management command. 🔵 This is the one row in the tranche that looks like a maintained library rather than a student utility, and it is the row an IFRN-network engagement should start from. |
| 🟢 [gabotachak/sia-unal-bridge](https://github.com/gabotachak/sia-unal-bridge) | 🟢 **MIT** | `c8c25ddaac12` · **2026-10-16** | `LICENSE` 1 085 B · `7521387e0869` | 🟢 **LATAM — Colombia.** JSON API over the SIA (Sistema de Información Académica) subject catalogue of the Universidad Nacional de Colombia. **301 files, Go (76) + TypeScript (42) + TSX (37)** — a deployed service with a front end, not a scraper script, and **the only address of the 37 platform-name hits that is simultaneously permissive and maintained**. Read first-hand 2026-10-25. |
| 🟢 [luizpicolo/suap_api](https://github.com/luizpicolo/suap_api) | 🟢 **MIT** | `718183f6` · 🟡 **2023-03-02** | `LICENSE.txt` 1 078 B · `798df9e7634a` | **LATAM — Brazil.** Ruby wrapper for the SUAP API, written against **IFMS** rather than IFRN — 🔵 the one address in the tranche that evidences the SUAP API is **shared across more than one Instituto Federal**, which is what makes a SUAP integration reusable beyond a single institution. 24 files. |

### 🟡 Permissive but stale — shelved as reference implementations, dated so nobody mistakes them

Each is a *worked example of the integration shape* for its platform, not a dependency to take.
🔴 **Every HEAD below predates 2025**; the portals they read have had five or more years to
change.

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [Open-Source-eUdeC/UdeCursos-bot](https://github.com/Open-Source-eUdeC/UdeCursos-bot) | 🟢 **MIT** | `cab987ccd1a5` · 🟡 **2024-03-17** | `LICENSE` 1 074 B · `198619b5e4a3` | **LATAM — Chile.** Telegram bot over **UdeCursos**, Universidad de Concepción's course platform. 29 files, Python (18). The freshest permissive *agent-shaped* LATAM address: a working model of the notify-the-student pattern, 8 ★. |
| [ivmelo/suap-api-php](https://github.com/ivmelo/suap-api-php) | 🟢 **MIT** | `fc2a679fe78a` · 🔴 **2021-04-13** | `LICENSE` 1 071 B · `8dd4b842ad4d` | **LATAM — Brazil.** PHP wrapper for the **SUAP** API (Instituto Federal network). 34 ★ — the most-starred *licensed* SUAP address, and the licensed counterpart to IFRN's own unlicensed clients (see the publisher split in `agents/trending.md`). 7 files. |
| [Projeto-SIAC/suap-wrapper](https://github.com/Projeto-SIAC/suap-wrapper) | 🟢 **MIT** | `bfe75f6147c3` · 🔴 **2019-03-12** | `LICENSE` 1 061 B · `7d6794d36990` | **LATAM — Brazil.** JS wrapper for the SUAP API, 12 ★, 8 files. Second licensed SUAP read seam; useful as the Node-side shape where `suap-api-php` gives the PHP one. |
| [juan-c-cardenas/sia-scraper](https://github.com/juan-c-cardenas/sia-scraper) | 🟢 **MIT** | `e557dac6c26d` · 🔴 **2020-08-18** | `LICENSE` 1 085 B · `ca571ae2faa5` | **LATAM — Colombia.** SIA UNAL course-documentation scraper, 7 files, JS. The scrape-path counterpart to `sia-unal-bridge`'s API path, and the cheaper read when only the catalogue is needed. |
| [ramomar/siase-schedule-scraper](https://github.com/ramomar/siase-schedule-scraper) | 🟢 **MIT** | `d5713cf636d2` · 🔴 **2019-12-07** | `LICENSE` 1 077 B · `09c43d110fc7` | **LATAM — Mexico.** Timetable scraper for **SIASE** (UANL), JavaScript, 10 ★, 5 files. Smallest complete worked example of the SIASE read in the tranche. |
| [ramomar/uniswag-chrome](https://github.com/ramomar/uniswag-chrome) | 🟢 **MIT** | `c62306458f04` · 🔴 **2019-07-06** | `LICENSE` 1 070 B · `b36468e555d3` | **LATAM — Mexico.** SIASE integrated with Todoist and Google Drive as a Chrome extension, 21 files. 🔵 The only address in the tranche that pushes portal data **outward into a third-party productivity tool** — the shape an engagement is usually asked for, implemented once, in 2019. |
| [molguin92/UCampusViz](https://github.com/molguin92/UCampusViz) | 🟢 **BSD** · 1 514 B | `eabef308b7d8` · 🔴 **2019-01-16** | `LICENSE` 1 514 B · `3510752bf472` | **LATAM — Chile.** Course-prerequisite dependency graph for FCFM, Universidad de Chile. ⚠️ **Shelved with a caveat read from its own tree: 289 of its 297 files are `.html`** — it is a *generated artefact dump* with one `.py`, so it is evidence that the UCampus prerequisite graph is extractable, not a library to import. |

🔵 **Not promoted, and named so the absence is informed:** the 18 ungranted addresses
(`Gap 444-C`), among them an **MCP server** (`sebassg/sia-unal-mcp`, TypeScript, HEAD
2026-03-12) and **three official IFRN OAuth2 clients totalling 81 ★**. They are live, they are
relevant, and there is no right to use them. Every one is listed with its HEAD and grant state
in [`evidence/verified-repos.2026-10-25-p444.tsv`](../evidence/verified-repos.2026-10-25-p444.tsv).

---


# 🏗️ Foundational repos — Education

## 🆕 `p443` — **The tier grows by FIVE after six passes of zero, and not one of them came from a search this base had not already run. 🔴 They were in its own append-only record, unshelved, and invisible to the promotion ledger**

🟢 **The LATAM academic-portal integration tier.** Six consecutive passes wrote *"zero rows
added"* on this file while the shelf stood at **1 LATAM row of 8**. The addresses below close
that, and the discovery cost was one query: **the name of the platform the institutions
actually run**, sorted by stars, with no capability words added.

🔴 **Where they came from is the finding.** Five of the six were already written into
[`agents/trending.md`](../agents/trending.md) and [`trending.md`](trending.md) by earlier
passes and promoted by none; all six are `grep`-absent from
`evidence/promotion-ledger.2026-10-25-p436.tsv`. The measurement — **2 361** record addresses
absent from the ledger, **69** of its 219 rows already landed, so `PROMO_RATCHET = 148` counts
claims rather than findings — is `Gap 443-A`.

🔵 **Why these are foundations and not agents.** None of the five is an AI system. Each is the
**read seam** onto a national academic portal — the thing an agent has to call before it can
tutor, advise or chase a deadline. That is this file's job, and it is precisely how this base's
EMEA line began: `librus-python-api` sits here and `librus-mcp` sits on the agents shelf. The
agent-addressable half of this tranche (`jpmanson/siu-guarani-mcp`, MIT) is on
[`agents/top.md`](../agents/top.md) for the same reason.

🔴 **The licence frontier in LATAM, measured here for the first time, and it runs the wrong way
exactly as it does in EMEA:** of 8 academic-portal addresses **6 are permissive**; of the 4
institutional platforms that actually hold student records, **0 are** — GPL-2.0, GPL-3.0,
GPL-3.0, AGPL-3.0. 🟢 **So the foundation layer is buildable and the platform layer must be
integrated, never vendored.**

### 🟢 The five rows, read first-hand — tree-enumerated, file-measured

Grant paths from `git ls-tree -r` over a blobless clone (`p442`/`Pattern AU`), not a root
ladder; every payload fetched at the pinned SHA and measured from the file, so the
trailing-newline run is intact (`P834`). 🟢 **14 of 14** granted repositories in this tranche
carry **exactly one** own-grant path — no `librus-mcp`-style second grant anywhere in the arm.

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [aquario-ufpb/aquario](https://github.com/aquario-ufpb/aquario) | **MIT** | `662a345962d2` | `LICENSE` 1 070 B · `ca675f365799` | **LATAM — Brazil.** UFPB's Computing Centre information hub: the largest and most active address in the tranche (86 ★, 948 files, HEAD **2026-10-21**). The one row here that is a *deployed institutional product* rather than a utility, so it is the reference for what a Brazilian federal-university front end is expected to contain. |
| [PucaVaz/sigaa-tools](https://github.com/PucaVaz/sigaa-tools) | **MIT** | `a5a86e0a9b28` | `LICENSE` 1 065 B · `75d9af3e2e90` | **LATAM — Brazil.** Python SIGAA tooling, 209 files, HEAD **2026-10-20** — 🟢 the **most recently maintained SIGAA read seam in existence**, which is what makes it the default starting point over the better-known archived API below. |
| [trindadetiago/sigaa-caiu](https://github.com/trindadetiago/sigaa-caiu) | **MIT** | `7373c6abac62` | `LICENSE` 1 071 B · `e69df76328c3` | **LATAM — Brazil.** SIGAA-derived study tooling, 48 files, HEAD **2026-09-02**. Live, small and readable — the cheapest row to fork when an engagement needs a bespoke SIGAA reader rather than a library. |
| [juliancasaburi/siu-guarani-promedio-extension](https://github.com/juliancasaburi/siu-guarani-promedio-extension) | **MIT** | `6962638adbdd` | `LICENSE` 1 073 B · `652d46c067d4` | **LATAM — Argentina.** Computes grade averages from a SIU Guaraní academic record (Chromium/Firefox). 🟢 Documents the **student-side** record layout, where `siu-guarani-mcp` covers the teaching-staff profile — together they span both SIU Guaraní personas. 🟡 HEAD **2025-07-08**: read the parsing, do not depend on the extension. |
| [GeovaneSchmitz/sigaa-api](https://github.com/GeovaneSchmitz/sigaa-api) | **MIT** | `a7aab3d605d7` | `LICENSE` 1 108 B · `ecb193695a94` | **LATAM — Brazil.** 🔴 **ARCHIVED by its owner on 2024-04-10 and read-only — shelved as a REFERENCE, never as a dependency**, and the README's own `ARQUIVAMENTO` section says so. Why it earns a row anyway: at 61 ★ / 23 forks / 247 commits / 232 files it is **the most complete SIGAA model that exists in the open** — classes, grades, absences, news, teacher search, class members, file downloads — and it is the only address here that states which instances it was tested against (**IFSC, IFFar, UFPB**). Read it to learn the portal; build on `sigaa-tools`. |

🔴 **One row in this tranche is deliberately NOT here.** `ipti/br.tag` — Brazil's live municipal
school-management platform — is on [`verticals/solutions.md`](../verticals/solutions.md)
instead, because its grant is **GPL-2.0** and because its **README states BSD-3-Clause**, a
two-channel conflict established first-hand at one commit and written up in
[`agents/trending.md`](../agents/trending.md) `p443`. 🔵 It is the sharpest argument on this
file for why a promotion test reads the payload and not the README: the README is the *more
permissive* of the two, which is the direction that costs a client money.

### 🔴 Refused in the same tranche, and the reason is recency, not licence

| repository | grant | HEAD | verdict |
|---|---|---|---|
| [luizpicolo/code](https://github.com/luizpicolo/code) | 🟢 MIT `1 074 B · a2874113b3b5` | 🔴 **2016-10-31** | Ten years cold |
| [rodrigmatrix/sigaa_ufc_android](https://github.com/rodrigmatrix/sigaa_ufc_android) | 🟢 Apache-2.0 `11 357 B · c71d239df917` | 🔴 **2021-03-19** | Permissive and dead |
| [ernestosrf/sigaa-horarios-extension](https://github.com/ernestosrf/sigaa-horarios-extension) | 🔴 **none in tree** (9 files) | 2025-07-23 | `REFUSED-UNGRANTED` |
| [Cristianojr9/sigaa-new-design](https://github.com/Cristianojr9/sigaa-new-design) | 🔴 **none in tree** (30 files) | 2020-08-20 | `REFUSED-UNGRANTED` |
| [G3-Devs/siu-auto-asistencia](https://github.com/G3-Devs/siu-auto-asistencia) | 🔴 **none in tree** (11 files) | 2026-04-18 | `REFUSED-UNGRANTED` |

🔵 **Two of the five were refused with a clean permissive grant in hand** — the
`davemckain/qtiworks` precedent on this file, and the right call both times. A licence-only
promotion test would have shelved them. 🟢 The three ungranted verdicts are from a **tree
enumeration**, not a root ladder, so they are absences of a grant *anywhere in the repository*.


## 🆕 `p442` — **Zero rows added, sixth pass running — and the tier's own cells were the finding: 5 of them did not reproduce, and one platform ships a 1 614 B POINTER beside its 35 147 B grant**

🔴 `p442` adds **no** foundation row. Its six new permissive addresses are **Agent Skills and
tutoring tools**, not things a deliverable vendors as a dependency; they are shelved on
`agents/top.md`. 🔵 The work this file got instead is **verification of what it already
sells**.

### 🔴 Five cells on this file were measured through a capture, and are repaired in this commit

All 162 payload cells across the three sell shelves were re-measured from the file and
through `lib/payload_measure.sh`'s preserved `P834` control. 🔴 **19 carried the capture
signature** — bytes short by the trailing-newline run, digest taken of the stripped bytes —
and **five of them are on this file**:

| row | published | 🟢 now |
|---|---|---|
| [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) | 1 064 B · `2524a8e74f10` | **1 065 B · `43554d1189d8`** |
| [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) | 1 068 B · `523f156051cf` | **1 069 B · `aa8cfde0dc31`** |
| [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | 1 068 B · `68657618a157` | **1 069 B · `fc7c8b90fee1`** |
| [`ezixen/PlannedEducation`](https://github.com/ezixen/PlannedEducation) | 1 085 B · `4ec3cc564448` | **1 086 B · `53de23fdecc2`** |
| [`rwrife/rubric-desk`](https://github.com/rwrife/rubric-desk) | 1 062 B · `ec0b7dad19a4` | **1 063 B · `c186f5cb204a`** |

🟢 The grant itself was never in doubt for any of the five — MIT in every case, unchanged —
and that is the point worth taking: **a cell can be wrong in a way that does not change the
licence and still destroys the one thing a reader can check.**
`make gate-cell-reproduction` now holds it, and `lib/measure --cell` builds the string.

### 🔴 `chamilo/chamilo-lms` carries its grant TWICE, and one of the two is not a grant

Enumerating the tree (`Gap 441-A`'s fix, now in the shared library) returned two licence
paths for Chamilo: the root `LICENSE` — **35 147 B · `8ceb4b9ee5ad`**, the full GPL-3.0 this
file publishes — and **`license.txt`, 1 614 B · `0aaf39205490`**, which grades 🔴
`GRANT-BY-REFERENCE`: GPL-3.0 titled, **all six profiled clauses absent**, a URL in place of
the text.

🔵 **Nothing is wrong with the shelf row, and that is what makes this worth recording.** The
ladder in `lib/probe_payload.sh` emits `LICENSE` before `license.txt`, so it happened to land
on the complete text. 🔴 **The order of a hand-tuned filename list is the only thing that
stood between this file and publishing a 1 614 B pointer as Chamilo's grant** — and `p337`
already refuted that list's empirical basis by finding a real project whose only payload is a
**lowercase** `license.txt`. For a repository shaped like that one and licensed like this one,
the ladder picks the pointer.

## 🆕 `p440` — **Zero rows added, for the fourth pass running — and this time the screening question has an answer the previous three could not compute**

🔴 `p440` adds **no** foundation row. The pass's one new address,
[`AnkitClassicVision/tutor-engine`](https://github.com/AnkitClassicVision/tutor-engine),
is a self-hosted application under **AGPL-3.0**: nothing downstream can depend on it, and
network copyleft is the wrong grant to put in a tier whose whole purpose is *things a
deliverable may vendor*. It is shelved on `agents/top.md` with that posture attached.

### 🟢 The screening amendment: "can the grant be READ" is now answerable for copyleft too

`p439` added the screening question — 🔵 *before a dependency is shelved here, ask not
only which licence it names but whether the payload contains the words that perform the
grant.* 🔴 That question had a hole exactly where this file's risk is: `grant_presence.py`
carried profiles for **MIT, Apache-2.0 and ISC only**, so every GPL, AGPL, LGPL, BSD, MPL
and EPL payload returned `GRANT-UNCALIBRATED` — **101 of 218**. A foundation row under
GPL-2.0 could not be screened by the screening rule.

🟢 `p440` profiles the GPL family (AGPL-3.0, GPL-3.0, GPL-2.0), and the remainder falls to
**39 of 218**. For this file that means the 🔴 **Copyleft foundations** section below is
screenable for the first time, and the ten platform repositories behind it were read at
source this hour: **10 of 10 `GRANT-PRESENT`** (table on `verticals/solutions.md`).

🔵 **The amendment, stated so the next pass can apply it without re-deriving it:**

1. **Ask the grant question before the tier question.** A payload that names a family and
   does not contain its operative clauses is not a candidate for *any* tier — the row is
   `GRANT-TRUNCATED` or `GRANT-BY-REFERENCE`, and the obligation it names lands on
   whoever vendors it next. On this base's own corpus that is 🔴 **36 payloads**.
2. **Resolve the version before judging a GPL-family grant.** A complete GPL-2.0 licence
   is missing four of GPL-3.0's six operative clauses. Grading it against the wrong
   version condemns a valid grant — and the three GPL-2.0 platforms on these shelves
   (`i-educar`, `RosarioSIS`, `openSIS`) are the LATAM / low-cost SIS tier, so the error
   would have fallen entirely on one region's supply.
3. 🟡 **`LGPL` still declines, and two shelved platforms carry it.** LGPL-3.0
   incorporates GPL-3.0 by reference *by design*, so it needs a fourth verdict rather
   than a profile (`Gap 440-B`). **BigBlueButton** and **OpenEduCat** are
   `GRANT-UNCALIBRATED` and must not be read as cleared.
4. 🟢 **`BSD` is PROFILED as of `p441`, variant-aware — `GRANT-UNCALIBRATED` on the BSD
   slice falls 14 → 3, and the remaining three are KB markdown tables, not licence
   payloads.** `MPL` (9) and `EPL` (9) are still unprofiled and are the remainder of
   `Gap 440-A`. 🔴 **Two corrections to that gap's own text, both measured:**
   - Its denominator was **27 % high**: of the 14 BSD-titled fixtures, three are markdown
     tables naming a licence in a cell. The real payload count was **11**.
   - Its prescribed method — *resolve the variant from the clause structure* — is
     **unsound**. BSD-2 and BSD-3 differ in exactly one clause, and it is a clause the
     instrument grades, so a **BSD-3 truncated at that clause** resolves as a complete
     BSD-2 and returns `GRANT-PRESENT`. 🟢 The variant is now resolved from the payload's
     own **declaration** (the title line, the only BSD signal independent of the graded
     clauses), with the structural arm permitted to answer **only** in the direction that
     cannot be wrong — presence of the discriminator, never its absence.
   - 🔴 And the row the gap named,
     [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE),
     carries **no title line**, so no BSD profile could have screened it: the blocker was
     the family answer, not the variant. It is now verified `GRANT-PRESENT` with the family
     supplied by `lib/license_family.sh` (`grant_presence.py --family BSD`).

---

## 🆕 `p439` — **Zero rows added, and the screening question is now a measured one: can a dependency's grant even be READ from the repository?**

🔴 **No foundation rows this pass.** All **23** new addresses `p439` discovered (`ai-tutor`
ranks 61–80, `education-ai` ranks 21–40) are single-purpose tutoring skills, exam coaches,
prompt packs or student apps. A foundation on this shelf is something another component can
**depend on**; none of these is. 🟡 They are shelved on `agents/top.md` where they belong,
and the count here stays where it was rather than being inflated to look like progress.

### 🟢 The screening amendment — a third question, before licence family

This shelf has screened candidate foundations on existence, then default branch, then
licence family. `p439` adds a question that must come **between** family and adoption, because
it is the one that defeated every instrument on this base at once:

> **Is the granting text actually present in the repository, or only named?**

🔴 Measured on live supply this pass: `spragginsdesigns/ai-tutor-webapp` ships `LICENSE`
**552 B** titled Apache-2.0 — the APPENDIX *notice*, holder **Vercel, Inc.**, pointing at a
URL. This base's census returned `titled_family = Apache-2.0`, `scan_verdict = PERMISSIVE`,
`stock = True`, `needs_a_human = False`. 🔵 **A scan cannot answer this question and a byte
count should not**: the same measurement over this base's corpus shows BSD stock payloads
spanning **221 B → 1 514 B** (n=8), so any single BSD floor either misses a truncated BSD-3
or condemns every valid BSD-0. 🟢 **`p441` re-measured that span on 11 fixture payloads and
12 live ones and widened it to 164 B → 2 819 B** — the conclusion is unchanged and the
clause-based profile it argued for is now built.

🔴 **And the question was already settled here, one directory away.** `P1065` (pass 254):
*a pointer to a licence is not a grant* — implemented in
`pass258-content-licence-family/content_licence.py::is_grant()` for **Creative Commons content
licences only**, and never carried into the code-licence path that grades MIT, Apache-2.0 and
BSD. 🔵 A rule that exists in one classifier is not a property of the screen.

🟢 **So the question is asked of clauses, and it is now a `make` target, not a habit**:

```
make gate-grant-presence     # 19 controls, offline, committed fixtures
make grant-presence-census   # the live corpus; a MEASUREMENT, always exits 0
```

**Why it matters specifically for a foundation.** A foundation is vendored, so its
obligations travel to whoever ships it next. Two of them cannot be discharged from a
by-reference payload at all: Apache-2.0 **§4(a)** requires giving recipients a copy of the
License — a repository holding only the pointer has not done it, and the duty lands on the
integrator — and MIT's notice obligation requires reproducing a holder name, which in the
Vercel case names a party that never wrote the code. 🔵 For a dependency the client will
redistribute, `GRANT-BY-REFERENCE` is a **procurement finding**, not a footnote.

### 🟢 Four existing foundation-tier and platform addresses re-measured, and the shelf held

Independent re-probe this hour, byte-for-byte and HEAD-for-HEAD against what these shelves
already carry — a staleness check run as a measurement rather than assumed:

| Address | Re-measured 2026-10-25 | Agrees with shelf |
|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0, `LICENSE` 11 408 B, HEAD `a31d82624c27` | 🟢 yes |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 AGPL-3.0, `license.txt` 33 893 B, HEAD `5d6df8e3ed8e`, branch **`develop`** | 🟢 yes |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0, `LICENSE` 10 982 B, HEAD `d073ad444fe5`, branch **`master`** | 🟢 yes |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 ODbL, `LICENSE` 25 289 B, HEAD `7bd8b6794cb7` | 🟢 yes |

🔴 **And the secondary sources are still wrong about the first one a client will Google.**
Three of this pass's own 2026 search results named Frappe LMS "the MIT-licensed option" for
self-hosted LMS. It is **AGPL-3.0**; the MIT belongs to `frappe/frappe`, the *framework*.
`p425`'s `T125` re-verified at source — and the same two-key confusion (framework permissive,
application copyleft) is the single most expensive licence error available in this industry's
platform tier.

---

## 🆕 `p438` — **This pass adds ZERO foundation rows, and that is the finding** — plus the screening amendment that applies to every row already here

🔴 **Stated rather than padded.** `p438` graded **nine** new addresses first-hand (eight
permissive: 7 MIT, 1 Apache-2.0) and shelved all eight on `agents/top.md`. 🔴 **None of them
belongs on this file.** A foundation on this shelf is a component other work is built *on* —
`learningequality/kolibri`, `openedx/XBlock`, `pykt-team/pykt-toolkit`, `OpenOLAT/OpenOLAT`.
The eight new rows are single-purpose agent skills topping out at **18 ★** on their listing
page: real grants, real code, and **nothing downstream can depend on them**. 🟢 Promoting
them here to reach a count is the failure mode this base has a standing rule against, so the
count stays where the evidence puts it: **zero**.

🔵 **What was searched, so a successor does not re-spend the leg.** Four channels at measured
depth — GitHub topic `ai-tutor` pages 1–3 (ranks 1–60), topic `education-ai` page 1, topic
`intelligent-tutoring-system` page 1 — **89 slugs dup-checked, 80 already shelved**. The
foundation-shaped candidates the legs returned were `open-spaced-repetition/fsrs4anki`,
`GarethManning/education-agent-skills`, `GeminiLight/gen-mentor`, `Selleo/mentingo`,
`luffycodes/Tutorbot-Spock` and `thm-mni-ii/feedbacksystem` — 🟢 **every one already carried
on these shelves**. The platform legs re-returned `OpenOLAT` (Apache-2.0), `Sakai` (ECL-2.0,
Apache-derived), `formalms`, `francoisjacquet/rosariosis` and `GibbonEdu/core`, all carried,
with the licence-source conflict on `formalms` (Apache-2.0 in one comparison, GPL-2.0 in
another) 🔵 **already resolved on this base from the payload rather than the comparison**.

### 🔴 The amendment: a foundation is cleared on **three** columns now, not one

`p438`'s specimen `fangyuan-3149/book-learning-tutor` grades `titled_family = MIT`,
`scan_verdict = PERMISSIVE`, `stock = YES` — and, from the **same** `bespoke_census.grade()`
call, `p1054_verdict = MIT-BODY-PLUS:unclassified-addition` with `needs_a_human = no`. 🔴 Over
the **238** licence payloads committed under `compose/code/**/fixtures/`, **7 of the 9**
addition-bearing payloads are routed `needs_a_human = no` — **`p427`'s own two-family
specimen among them**, the payload this base wrote a 24-control gate about because it carries
a notice obligation of two.

🟢 **Why that matters more on this file than on `agents/top.md`.** A foundation is the row a
client's product *inherits* from, so an unread clause in a foundation payload propagates into
everything built on it and surfaces years later in a diligence review. The qualifying test on
this shelf is therefore:

1. 🟢 `titled_family` ∈ {MIT, Apache-2.0, BSD-*, ISC} — necessary, **not** sufficient;
2. 🟢 `p1054_verdict` carries **no** unclassified addition — the column `needs_a_human`
   currently ignores;
3. 🟢 payload bytes inside the family's stock band, or the surplus **read by a person** —
   and read in whatever language it is written in, which `p427`'s English `SCOPE_MARKERS`
   cannot do.

🔵 Every row currently on this file passes 1 and 3 on first-hand reads already recorded here.
🟡 **Column 2 has never been applied to this shelf as a screen** — it is registered as
`Gap 438-A` with its price, not back-fitted into the rows this pass did not re-grade.

## 🆕 `p437` — The permissive foundation tier grows by one, and the qualifying test is **not** the licence

🟢 Five MIT-licensed EU-AI-Act compliance repositories were graded first-hand this pass
(payloads and HEADs in `agents/top.md` `p437`). On licence alone, all five qualify as
foundations. 🔴 **On fitness, one does.**

| repo | grant · payload | foundation? |
|---|---|---|
| [tomdxb0004/eu-ai-act-risk-checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 **MIT** · `LICENSE` 1 073 B · `b7b08f330649` @ `41da87feb238` | 🟢 **Yes.** Zero dependencies, no build step, no backend, no telemetry; `engine.js` is a pure function with no DOM access, so the classifier is directly embeddable in a Globant deliverable. Encodes Annex III = `2027-12-02` **with its citation inline**, carries education as Annex III point 3, and implements the Art. 6(3) profiling override |
| [Hiepler/EuConform](https://github.com/Hiepler/EuConform) | 🟢 **MIT** · 1 073 B · `65335056589f` @ `011a5ad9bea2` | 🟡 **Component, not foundation.** Take the Annex IV report generator and the bias-evaluation harness; its date handling is too vague to anchor a compliance gate |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** · 1 074 B · `7df20dcdf919` @ `70a4ab8e8a04` | 🟡 **Component.** Annex III checklist naming education, plus agent controls; carries no dates, so it must be paired with a dated classifier |
| [sjgant80-hub/fall-euaiact](https://github.com/sjgant80-hub/fall-euaiact) | 🟢 **MIT** · 1 067 B · `0ddf3b67a14a` @ `5d8d27b65f68` | 🟡 Dates correct; 🔴 **no education scope**. A cross-check, not a base |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | 🟢 **MIT** · 1 056 B · `1126322e2cc8` @ `fff58f6e8906` | 🔴 **No.** Encodes the superseded `2026-08-02` at `packages/cli/src/commands/gaps.ts:199` and pins it in tests. 🟢 Its `data/annexes.json` Annex III cat. 3 education block (all four statutory use cases) **is** worth vendoring as reference data — take the data, leave the logic |

### 🔴 Why this belongs on the *foundations* shelf and not only on the agents shelf

A foundation is something an engagement's architecture **rests on**, so a wrong constant in it
propagates into every deliverable built above. 🔵 This pass found that four of five
candidates would have passed this base's normal foundation screen — permissive grant, payload
read, active, recent — while carrying either a superseded statutory date or no date at all.
🟢 **The screen has been extended accordingly**: a repository whose output includes a
regulatory date is only a foundation if that date **cites the instrument that set it**. The
three-grep version of that test is in `repos/trending.md` `p437`.

🟡 **And the reach bound, stated as one:** this test was applied to EU instruments only. The
NA state-guidance trackers and the APAC instruments this base cites on `intel/market.md` have
**not** been screened the same way, and `intel/trends.md` Trend 35 names that as the next
measurement — including against this KB's own shelves.

> The bases worth starting from, with licences read from each repository's own payload at
> the HEAD SHA shown (2026-10-25). Permissive first — those are the ones Globant can build on.

## ✅ The permissive foundations — verified 2026-10-25

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` | University-grade LMS and **the only Apache-2.0 platform in the tier**. The default base when the client needs a full LMS and cannot take copyleft. Badly under-used relative to its terms. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | Offline-first learning platform. The only MIT platform; the answer to connectivity and equity constraints (LATAM, rural APAC, Africa). |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | Component SDK for Open edX. **The licence seam**: ship an Apache-2.0 AI component into an AGPL-3.0 platform without the platform's terms reaching your code. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` | Knowledge tracing (DKT/SAKT/BKT family, standard datasets). The measurement layer that makes an "adaptive" claim defensible rather than rhetorical. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | **Apache-2.0** | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` | Minimal agent framework, EU-domiciled. The base for a bespoke tutor/grader when a full tutoring platform is too much. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** | `7cf513c235ee` | `LICENSE` 1 079 B · `e4b2a3148135` | Django/React course-portal CMS (France Université Numérique). The public-sector MOOC front-end. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL** (Apache-derived) | `4debc94780cc` | `LICENSE` 11 120 B · `0688f62d04f1` | Higher-ed consortium LMS. Permissive in practice — but record it as ECL-2.0, **not** Apache-2.0. |
| [Utdanningsdirektoratet/PAS2-Public](https://github.com/Utdanningsdirektoratet/PAS2-Public) | **Apache-2.0** | `489129c42c9d` | `LICENSE` 11 325 B · `cb5e8e7e5f4a` | 🆕 `p435`. **Norway's Directorate for Education (Udir) publishing the public code of its new exam and test administration services (PAS2)**, issue tracker and wiki open to the public. 🟢 A national assessment authority's own administration stack under a permissive grant — the single strongest EMEA public-sector row on this file, and the counterpart to Norway's own age-tiered AI restriction. Default branch is `master`. |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** | `ad46faf42690` | `LICENCE` 1 116 B · `e18299fd1942` | 🆕 `p435`. England's **school registry** service (GIAS) — the authoritative establishment dataset behind every DfE service. 🔵 Note the grant is at `LICENCE`, the British spelling: a ladder that only tries `LICENSE` reports this UK government repository as ungranted. |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | `a2d4f5fdec58` | `LICENSE` 1 092 B · `c561ea849ed6` | 🆕 `p435`. The DfE's national teaching job service (Rails + PostgreSQL + Redis), source **and** infrastructure definitions. The reference for a public-sector education service a client can read end to end. |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** | `3cdbf2cbf47b` | `LICENSE` 1 091 B · `5a22fb5576a5` | 🆕 `p435`. **FBIT** — the DfE's school financial benchmarking and insights tool: compare resource use against similar schools, interrogate the financial data, support governor oversight. 🟢 The one row on this file that is a *finance* analytics surface over school data, which is where a UK trust-level engagement starts. |
| [oaknational/oak-curriculum-api](https://github.com/oaknational/oak-curriculum-api) | **MIT** | `0561df5aac12` | `LICENSE` 1 077 B · `0eeb9d32caed` | 🆕 `p435`. **Oak National Academy's** curriculum API — England's national-curriculum content as a documented, versioned OpenAPI surface. 🟡 `oaknational/oak-openapi` is the **same repository** (identical HEAD under `git ls-remote`, and the repo's own badges use that name); one row, two spellings, shelved once. |
| [instructure/ims-lti](https://github.com/instructure/ims-lti) | **MIT** | `724f1ae45315` | `LICENSE.txt` 1 068 B · `f7e95fbe6fa9` | 🆕 `p435`. **Instructure's own** Ruby IMS-LTI implementation — the Canvas vendor publishing the integration library under MIT. 🟢 The vendor-maintained half of the LTI layer that `Trend 19` says goes stale at the standards body and is carried by the vendor fork. |
| [hyunbinseo/neis-school-info](https://github.com/hyunbinseo/neis-school-info) | **MIT** | `5c9ecede5208` | `LICENSE` 1 068 B · `e82e1769aaaf` | 🆕 `p435`. TypeScript client for **NEIS**, Korea's national education information open-data portal (`open.neis.go.kr`) — school basic information. 🟢 The APAC analogue of GIAS above: a national school registry reachable from code. 🟡 The README warns the upstream dataset is not routinely reconciled, so treat records as reported, not current. |
| [krzysztofbury/librus-python-api](https://github.com/krzysztofbury/librus-python-api) | **MIT** | `fba65fe807eb` | `LICENSE` 1 071 B · `22e7ab2dbddc` | 🆕 `p435`. The independent Python client for **Librus Synergia** that `librus-mcp` (on `agents/top.md`) is built on — the library layer under the Polish gradebook connector. 🔵 Byte-identical MIT payload to the server, same copyright holder: one author, two addresses, no third-party-holder question. |

**15 verified permissive foundations** in the platform/agent tiers above. Each resolved under
`git ls-remote` and each licence was read from the repository's own payload. 🆕 `p435` adds the
**eight** above — the **public-authority** tier: a national assessment authority (Udir), three
UK Department for Education services, England's national-curriculum API, Korea's national school
registry client, the Canvas vendor's own LTI library and the client library under the Polish
gradebook connector. 🆕 `p431` adds a further **4** in **Tier 9 — the evaluation layer** below,
for **19** permissive foundations in all.

## 🔁 Restored by `p436` — including the repository two open gaps are written against

> 🔴 **Restorations, not discoveries**, from the **171**-address population `p436`
> measured for `Gap 435-B`. Every payload below was re-read first-hand on **2026-10-25**.
> 🔴 **The most serious single row is `LongsightGroup/qti3`**: `Gap 238` was closed
> against it with a tested artefact and `Gap 240` is still open on it, yet it was on
> **no live shelf** — the rewrite deleted the evidence under two registered gap verdicts
> while the verdicts themselves survived. That is `Gap 435-B`'s mechanism reaching the
> gap register itself.

| Repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | Why it is a foundation | Region |
|---|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** | `db379e0c8757` | `LICENSE` 10 173 B · `a6cba85bc92e` | Serves a **OneRoster 1.2 API from an Ed-Fi ODS** (Data Standard 4.0, 5.x and 6.1). The roster-interoperability seam for US district data, and the row that lets an agent read enrolment without touching the SIS directly. | North America |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** | `902996d89729` | `LICENSE.md` 1 072 B · `00ed05b90bf8` | QTI 3 toolkit whose `packages/core` implements the **full parametric-item mechanism** — template declaration parsing, a real `randomInteger` draw over min/max/step, answer keys derived from the draw, and a constraint-retry loop. **This is the repository `Gap 238`/`Gap 240` are written against**, and it had been off every live shelf. | North America |
| [OpenOLAT/qtiworks](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** | `57cdf4affa26` | `LICENSE.txt` 2 058 B · `a5c692f12090` | QTI 2.1 delivery engine with **JQTI+** and **MathAssess** (Edinburgh lineage). 🟢 **The live fork**: byte-identical payload to the abandoned `davemckain/qtiworks` and maintained to **2026-06-30** — see the decline note below. | EMEA |
| [amp-up-io/qti3-item-player](https://github.com/amp-up-io/qti3-item-player) | **MIT** | `2e304fd0efb0` | `LICENSE` 1 076 B · `7faa621251d7` | QTI 3 **item player** — the rendering half of the assessment boundary, pairing with `qti3`'s authoring and `qtiworks`' delivery. | North America |
| [Kennisnet/php-qti3](https://github.com/Kennisnet/php-qti3) | **MIT** | `cad6125a16ff` | `LICENSE` 1 066 B · `27fb6d463569` | PHP QTI 3 implementation published by **Kennisnet, the Dutch national education-ICT body** — a state education body shipping its own permissive assessment code, which is the EMEA supply tier this base kept recording as absent. | EMEA |
| [datakind/student-success-tool](https://github.com/datakind/student-success-tool) | **MIT** | `e35c41af1dc1` | `LICENSE.md` 1 080 B · `04c23f1c41cd` | DataKind's data-assisted advising tool for retention: a **deployed** intervention, with John Jay College reporting a 32 % rise in senior graduation over two years via its CUSP programme (the project's own claim). Backed by google.org. 🟡 HEAD 2025-09-08 — over a year old; check currency before building on it. | North America |
| [marcosroriz/sete](https://github.com/marcosroriz/sete) | **MIT** | `9f1f9c87ec93` | `LICENSE` 1 069 B · `0bbd32e7e09a` | **SETE** — school-transport e-governance from CECATE/UFG, with web, desktop and mobile builds; the desktop build exists specifically so municipalities **with restricted internet** can operate it. The clearest LATAM public-sector education system on this base. 🔴 HEAD 2023-03-20 — stale; treat as a reference design, not a live dependency. | LATAM |
| [AI-for-Education/edu-qurating](https://github.com/AI-for-Education/edu-qurating) | **MIT** | `e007badc4e66` | `LICENSE` 1 063 B · `e6081fef4354` | **Edu-QuRating** — educational-quality rating of pretraining text, with a paper (arXiv 2609.09425) and released models; began as a fork of Princeton NLP's QuRating, upstream kept under `upstream/` with history. The data-curation layer under any education-domain model work. 🟡 `+0000` does not place a region on the offset channel; recorded Global. | Global |

### 🔴 Declined in the same tranche — `davemckain/qtiworks`

🔴 **Not restored, and the reason is in its own README**: *"IMPORTANT! This project is no
longer supported and is going to be closed in early 2023."* HEAD **2023-01-04**.
🟢 **The payload is BSD-3-Clause and re-read clean (2 058 B, `a5c692f12090`) — the grant
was never the problem**, and a licence-only promotion test would have shelved it.
🟢 **`OpenOLAT/qtiworks` carries the identical payload digest and is maintained to
2026-06-30, so it is restored in its place.** 🔵 This one row is the concrete
demonstration of `Gap 435-A`'s finding that *permissive* is not *recommendable*: both
forks pass the licence test, one is dead, and only a README read separates them.
Recorded as `DECLINED-p436` in the ledger so it is never re-litigated.

🟡 **Stated reach bound**: the QTI layer is restored on **grant + currency + README**;
no suite was executed, because installing a third-party repository's dependencies is not
permitted in this environment — the same limit `P533` carried.

## 🔴 Copyleft foundations — usable, but integrate, do not vendor

| Repo | Licence | HEAD | Payload | Note |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `46c042e7da65` | `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | Largest installed base and plugin ecosystem worldwide. Talk to it over its API. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | AGPL-3.0 | `87cd3811a425` | `LICENSE` 35 136 B · `e12d78569742` | Network copyleft. Use XBlock as the seam. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `2e5139a816d3` | `LICENSE` 35 147 B · `8ceb4b9ee5ad` | Lightest self-host; strong LATAM footprint. |
| [exelearning/exelearning](https://github.com/exelearning/exelearning) | AGPL-3.0 | `c848eca0018d` | `LICENSE` 34 523 B · `0d96a4ff68ad` | Authoring tool led by Spain's Ministry of Education — state-backed EMEA credibility. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `5d6df8e3ed8e` | `license.txt` 33 893 B · `db1a87ba81e8` | 🔴 Listed as MIT by several 2026 roundups. **That is wrong** — read at source. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `ec452b65043b` | `LICENSE` 7 652 B · `e3a994d82e64` | Virtual classroom. Link against it; don't fork. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `46a5d7d40082` | `LICENSE` 8 241 B · `528f84036800` | LMS + SIS on Odoo — the closest thing to an education ERP. |

> Moodle and Chamilo ship a **byte-identical** GPL-3.0 payload (`8ceb4b9ee5ad`) — the stock
> FSF text. Recorded so a digest sweep does not misread the collision as a fork.


## 🆕 `p435` — The permissive foundation tier grew for the first time in six passes, and what grew it was a **census**, not a search

`p434`, `p433`, `p432` and the three before them all reported this tier unchanged. 🟢
**This pass added eight rows, and none came from a web search.** They came from grading the
2 450 unpromoted addresses this base already held (`Gap 434-A`, closed:
`compose/code/p435-promotion-sweep`, evidence in
`evidence/promotion-backlog-grants.2026-10-25-p435.tsv`).

### 🔴 The number that explains six passes of "unchanged"

| arm of the unpromoted backlog | n | share |
|---|---|---|
| **PERMISSIVE** (MIT 1 022 · Apache-2.0 330 · BSD/ISC/CC0/ECL/Unlicense 97) | **1 449** | **59.1 %** |
| `NO-GRANT` — 404 on all eight paths × two refs | 500 | 20.4 % |
| GPL / AGPL / LGPL family | 329 | 13.4 % |
| other / unrecognised | 172 | 7.0 % |
| **total probed** | **2 450** | 100 % |

🔴 **The permissive supply was never scarce — it was unexamined.** Six passes reported "no
growth" while 1 449 permissive addresses sat on the trend record ungraded. This also
sharpens `Trend 10` rather than refuting it: the permissive supply really is in the agent
and integration layers, and the **platform** tier is still almost entirely copyleft — what
changes is that the agent/integration layer turns out to be an order of magnitude larger
than this file's seven rows suggested.

### 🟢 What the eight rows have in common: a public authority wrote them

Udir's exam-administration services, three DfE services, Oak National Academy's curriculum
API, Korea's NEIS registry client — **state education bodies publishing their own
production code under MIT or Apache-2.0.** 🔵 That is a different kind of foundation from a
framework: it is the *schema and the service contract a national system already runs*, so a
build on top of it inherits the jurisdiction's own data model instead of inventing one.

### 🔵 And one ladder detail worth more than it looks

`DFE-Digital/get-information-about-schools` carries its grant at **`LICENCE`** — the
British spelling. `p228-shelf-gate`'s ladder tries it; a ladder that stops at `LICENSE`,
`LICENSE.md` and `LICENSE.txt` reports a UK government repository as **ungranted**. 🟢 The
ladder earns its eighth path here, on a real row, for the first time on these shelves.

### 🟡 The reach bound, stated as one

The recency channel (`head_dates.sh`) was run over the **permissive arm only**: 1 449
addresses dated, 0 failures. The 1 001 non-permissive rows carry `head_committed = -` in
the evidence file. 🔵 That is a deliberate bound, not a gap in the data — a stale AGPL row
is not more shelvable for being fresh.

## 🆕 `p434` — The permissive foundation tier is unchanged for a **fifth** pass, and this time the sweep says *why* with a number

`p434` promoted two permissive addresses to `agents/top.md`
([`wenflow-org/wenflow`](https://github.com/wenflow-org/wenflow), MIT, `LICENSE` 1 067 B ·
`b6fac57d4710`; [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai), MIT,
`LICENSE` 1 067 B · `5731a2d3ccea`). 🔵 **Neither belongs on this file, for `p433`'s reason:**
both are agent-layer — a learning-path agent and an adaptive-tutoring *runtime seam*. They
compose onto a base; they are not one.

🔴 **The permissive foundation tier above is unchanged:** OpenOLAT (Apache-2.0), Kolibri (MIT),
XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents (Apache-2.0). **Five rows, five passes, no
movement** — and `verticals/solutions.md` records the education-ERP sweep returning a **standing
nil for the third consecutive pass**.

🟢 **What is new is that the asymmetry `p433` described in prose now has a measured number.**
This pass graded the seven highest-traction addresses sitting unpromoted in the trending shelves
and **not one is a foundation, nor is one promotable**:

| ★ band | Addresses | Grants found | Foundations among them |
|---|---|---|---|
| ≥ 190 ★ | 5 | 🔴 3 × AGPL-3.0 · 1 × CC-BY-SA-4.0 · 1 × **no licence file** | **0** |
| < 100 ★ | 2 | 🟢 2 × MIT | **0** |

🔴 **So the asymmetry is sharper than "foundations move slowly".** In education's new supply,
**traction and permissiveness are anti-correlated** (`repos/trending.md`, `p434`): the biggest new
addresses are copyleft, content-licensed or ungranted, and the permissive ones are an order of
magnitude smaller — *and none of either kind is platform-shaped*. 🔵 **Pricing consequence,
unchanged in direction but now defensible with a count:** a proposal may assume it can adopt a
fresh permissive **agent**; it may not assume it can adopt a fresh permissive **platform**, and
it may not use stars as a proxy for adoptability at all. The highest-traction education address
this base has ever recorded is **4 771 ★ and CC-BY-SA-4.0**.

🟢 **Instrument added this pass**, and it is the reason this file can state the above as a
standing property rather than a pass observation: `compose/code/p434-promotion-gate`
(`make gate-promotion`, 28 offline controls, wired into `hooks`) fails whenever a **permissive**
address recorded in the trending shelves appears in **no** curated shelf. It was **red on its
first run** and is green after the two promotions, so this tier's completeness is now checked by
a gate instead of by a pass remembering to look.

## 🆕 `p433` — The permissive foundation tier did **not** grow, and that is the finding

`p433` promoted three permissive addresses into `agents/top.md` after first-hand payload reads —
[`learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) (MIT,
`LICENSE.md` 1 122 B · `15ce43afa44a`, **1 118 ★**),
[`PhysicsOS`](https://github.com/122-syf-wcy/PhysicsOS) (Apache-2.0, `LICENSE` 11 356 B ·
`f1a2e5fccede`) and
[`textbook-writer-skills`](https://github.com/cabbage2000-lab/textbook-writer-skills) (MIT,
`LICENSE` 1 064 B · `0d5a33d13ca9`). 🔵 **None of them belongs on this file**, and saying why is
the point: all three are **agents and skill packs**, not foundations. They compose *onto* a base;
they are not a base.

🔴 **The permissive foundation tier above is unchanged for the fourth consecutive pass:**
OpenOLAT (Apache-2.0), Kolibri (MIT), XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents
(Apache-2.0). The `p433` ERP sweep (see `verticals/solutions.md`) independently confirms there is
**no MIT/Apache education ERP** to add, and the trending sweep returned no permissive platform.

🔵 **The asymmetry is worth naming for anyone sizing an engagement.** New permissive supply in this
industry arrives almost entirely as **agent-layer** work — small, fast-moving, APAC-origin, often
skill-pack shaped. The **foundation** layer moves on a scale of years and is majority copyleft.
A proposal that assumes it can pick a fresh permissive platform is mispriced; a proposal that
assumes it can pick a fresh permissive agent is usually right. `Trend 14` is the demand-side
reading of the same fact.

## 🆕 `p432` — Tier 10: the special-education / IEP layer, and why it is a tier of seeds

The surface North American law regulates hardest has the thinnest open-source supply measured
anywhere in this repository. These are the bases that exist, with grants read from each
repository's own payload at the HEAD shown (2026-10-25).

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit) | **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 065 B · `43554d1189d8` | The **knowledge and boundary layer**. Two CA special-education roles as pinned knowledge packs with a declared draft-only / authorised-system-of-record boundary. Start an NA special-education engagement from this, not from a blank prompt. 🔴 Prose discipline, no runtime enforcement — adding that is the work. |
| [67tallchris/iep-builder](https://github.com/67tallchris/iep-builder) | **MIT** | `b39df0e9a4a1` | `LICENSE` 1 069 B · `aa8cfde0dc31` | The **deployment reference**: Svelte + Cloudflare Pages Functions + D1 with bring-your-own-key AI. Shows a per-district deployment that holds no vendor key and no central student store. Jurisdiction-pinned to Arizona K-8. |
| [dougdevitre/access-to-education](https://github.com/dougdevitre/access-to-education) | **MIT** | `f8abd70707ba` | `LICENSE` 1 069 B · `fc7c8b90fee1` | The **parent-facing corpus**: 69 files / ~120 k words on IEP navigation, family–school communication and advocacy, under a code licence. The only MIT answer to the unserved-parent persona of `Trend 10`. |
| [ezixen/PlannedEducation](https://github.com/ezixen/PlannedEducation) | **MIT** | `06fb12159f5e` | `LICENSE` 1 086 B · `53de23fdecc2` | Adjacent, not special-ed specific: grading companion + secure test-taking, privacy-first self-host. Default branch `dev`. |
| [rwrife/rubric-desk](https://github.com/rwrife/rubric-desk) | **MIT** | `010a44006014` | `LICENSE` 1 063 B · `c186f5cb204a` | The **offline marking surface** (Flutter; phone/tablet/Windows, no accounts, no cloud LMS). Pairs with `kolibri` wherever connectivity cannot be assumed. 🟡 Created 2026-10-25. |

**5 permissive additions**, taking this file to **16 permissive foundations** in all.

🟡 **Adjacent but copyleft — integrate, do not vendor:**
[`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) is **AGPL-3.0-or-later**
(`LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f`, standard AGPLv3 body, SPDX header, no added
clauses) and is the only maintained accessibility-first differentiation engine found — UDL, WCAG,
AAC, text-to-speech, offline-first, i18n, commit on 2026-10-25. Network copyleft over a hosted
engine is the worst-case shape; reach it over an interface.

🔴 **Two addresses are excluded for cause, both proved by `git ls-tree -r` over the whole tree:**
[`grasped-dev/staircase`](https://github.com/grasped-dev/staircase) (@ `9236fce606c2`, 0 of 33 files)
and [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance)
(@ `ec2516b76699`, 0 of 29 files) carry **no licence at all**. Between them they hold the tier's best
technique (a standards graph for goal reasoning) and its most complete-sounding product. Neither is
a base.

🔴 **The honest health warning on this entire tier.** Star counts are 0, 0, 1, 0 and 0. Two of the
five were created inside the eleven days before this pass. None has a second contributor. These are
**seeds to fork and own**, not dependencies to track — and that is a different commercial
conversation from the one `kolibri` or `OpenOLAT` supports. Said plainly to a client, it is also an
argument *for* the engagement rather than against it: there is no incumbent to displace.

🔴 **Declared gap:** the tier is entirely US. The sweep found **no** open-source tooling for
England's EHCP process or for the inclusive-education mandates of Brazil, Chile or Colombia — a nil
result, not a thin one.

---

## 🔴 Read this before choosing a base: the licence frontier in education runs the wrong way

**The platform tier is copyleft. The agent tier is permissive.** That is the single most
consequential structural fact in this industry for a studio that needs to ship client-owned code:

| tier | licences actually found | what it means |
|---|---|---|
| **LMS / platform** | GPL-3.0 (Moodle, Chamilo, ILIAS, H5P), AGPL-3.0 (Open edX, Canvas, Tutor, Frappe LMS), ECL-2.0 (Sakai, Opencast), LGPL-3.0 (OpenEduCat) | Forking the platform pulls copyleft into the deliverable. AGPL additionally reaches **hosted** use. |
| **the one exception** | 🟢 **Apache-2.0 — [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | The only major open-source LMS a studio can extend with closed code. Underweighted by every roundup we read. |
| **agents / tooling** | MIT, Apache-2.0, BSD-3 almost throughout | Permissive. |

🆕 `p389` — **the "one exception" row is wrong, and the dating is what shows it.** There are **four**
permissive platform-tier bases on this shelf, not one, and the reason the claim survived this long is
that the other three were each filed as something narrower than a platform:

| permissive platform base | licence | last commit | the role it actually fills |
|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for an **institution**. Swiss, mature, full LMS. |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | 🔴 `master` | 🟢 **MIT** *(`LICENSE.md`)* | 🆕 `p390`. 🟢 **The permissive courseware engine, and the gap it fills is a licence gap rather than a feature gap.** **Torus** is the authoring-and-delivery platform behind **Carnegie Mellon's Open Learning Initiative** — the group whose course-effectiveness studies are the most-cited evidence base in the field. Pages, structured activities, adaptive **scripted "advanced authoring"** activities, mastery/proficiency reporting per learning objective, LTI 1.3 delivery into a host LMS, and a research-grade analytics surface. 🟢 **Everything else at this scale is copyleft** (Open edX AGPL-3, Canvas AGPL-3, Moodle GPL-3) — so when a client needs to *ship a modified platform* rather than host one, this is the only row on this shelf that lets them. Elixir/Phoenix + PostgreSQL. Dated **2026-10-22** — committed today. 🔴 **Mind the slug:** `CMU-OpenLearning/oli-torus` does not resolve; the canonical owner is `Simon-Initiative`. 🟡 Elixir is a real staffing constraint for most studio teams — cost it before proposing it. |
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for **pedagogy**: misconception-aware branching lessons. Filed in *Tier 2* as content, but it is a platform. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **2026-10-22 (0 d)** | The permissive base for **low-connectivity delivery**, and the only MIT one. Filed as a runtime; it is the platform in any engagement where bandwidth is the constraint. |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🟢 **2026-10-21 (1 d)** | The permissive base for a **course**. |

🔵 **What to say instead of "the platform tier is copyleft."** *The platform tier is copyleft wherever
the install base is* — Moodle, Canvas, Open edX, Chamilo, ILIAS are where the clients already are, and
those are GPL/AGPL/ECL. **Permissive platform bases exist, are all actively maintained, and all cost you
the install base.** That is a trade a client can be walked through; "there is one exception" was not.
The design consequence below is unchanged and is still the default — it is the *greenfield* branch of
the decision that just got three more options.

🆕 `p385` **And a third axis the table above cannot show: the grant can differ by *ref* within one
repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) reads **AGPL-3.0** at
`main` (34,523 B) and **MIT** at tag **`v0.1.0`** (1,081 B) — both read first-hand this pass. It relicensed on
**2026-08-16**. 🔵 So "what is this repository licensed as?" is not a well-formed question; **"what is it
licensed as at the ref I am shipping?"** is. That is now **Pattern L step 10**, and it cuts both ways: a
permissive grant can be *retrievable at a tag* after the project has moved away from it, and a repository
a prior audit cleared as MIT can be AGPL at `main` today.

**The design consequence**, not a preference: compose permissive agents **over** a copyleft platform
across a documented interop boundary — **LTI 1.3**, **MCP**, or the platform's web-services API —
rather than forking the platform. Recipes in [`compose/patterns.md`](../compose/patterns.md).

## Tier 1 — Learning platforms

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** — 🔴 grant is in **`COPYING.txt`**, there is **no root `LICENSE`** | The install base. Moodle Pty Ltd reports 400M+ users and ~150,000 registered sites. Originates in Australia (APAC). Huge plugin catalogue, and now a first-party MCP path. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 `master` | 🔴 **AGPL-3.0** | The MOOC-scale platform: LTI 1.3, XBlocks, deep data control. Deploy via `tutor` below, not by hand. |
| 🆕 `p393` [bmosoluciones/now-lms](https://github.com/bmosoluciones/now-lms) | `main` · `53dcb60` | 🟢 **Apache-2.0** *(10,915 B, `sha256`₁₆ `a9c4042d767d`)* | 🟢 **The permissive LMS this shelf did not have, and it is LATAM-native.** © 2021–2024 **BMO Moreno Berroteran Ortiz Soluciones, S.A. (Nicaragua)**. A complete Flask/Python LMS — courses, delivery, certificates, **monetisation** — at **676 files, 505 commits, 57 releases**, HEAD **2026-08-31 — 52 d**, PyPI `now-lms` v2.0.4, **21 ★**. 🔵 **Why it matters out of proportion to its stars:** every other platform on this tier is GPL (Moodle), AGPL (Open edX, Canvas) or LGPL, so `now-lms` is the **only Tier 1 row a studio can fork, extend and ship closed** — the licence frontier this file opens by describing, crossed at last. 🔴 The trade is scale: 21 ★ against Moodle's install base, and no multi-tenancy claim. Pilot and SME delivery, not a ministry. 🔵 Its non-stock Apache byte count is the **appendix FILLED IN**, not narrowed — `Pattern L` step 4's benign case, distinct from `Ed-Fi`'s absent appendix below. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 `master` | 🔴 **AGPL-3.0** | Dominant in North American higher ed. Open-**core**: the published tree is not the commercial ecosystem, so scope assumptions break on integration. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** | Swiss, mature, permissive. The default recommendation whenever a client needs to own closed extensions to the LMS itself. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** | The LATAM/EMEA public-sector base. Strongest Spanish/Portuguese-language footing of any platform here. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🔴 `master` | 🟡 **ECL-2.0** | Apache-2.0-derived **Educational Community License** — permissive-shaped with an education-specific patent/attribution twist. Read it; do not assume Apache. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** | German public-sector LMS and the learning component of the openDesk sovereign stack. Default ref is a release branch. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 🔴 **AGPL-3.0** *(`LICENSE.txt`)* | The Docker distribution for Open edX and the de-facto deployment path. Nobody should be installing `edx-platform` without it. |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT** *(`LICENSE`, 1,145 B — "MIT/X Consortium license")* | 🆕 `p384`. Django courseware with autograding, flexible access rules, per-student statistics and multi-course support. 🟢 **Permissive at the platform level**, which almost nothing else in this tier is. 🟡 Courseware-scale: the permissive base for a **course**, where OpenOLAT is the permissive base for an **institution**. Do not pitch it as a Moodle replacement. |
| [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | `main` | 🔴 **AGPL-3.0-only** *(`LICENSE`, 34,523 B; `pyproject.toml` → `AGPL-3.0-only`)* | 🆕 `p387`. 🟢 **The platform's own AI extension point — read this before anyone proposes forking Open edX to add AI.** First-party `openedx` org, so the extension surface is maintained with the platform rather than against it; the grant matches the platform's, which is why it can exist inside it. 🟡 Marked **experimental, not for production** in its own docs, so treat it as the contract to build against, not the thing to ship. Compare [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) (`main`, AGPL-3.0, Aulasneo — Argentina) for the LATAM-maintained customisation route. |
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🔴 `master` | 🟢 **MIT** *(`LICENSE`, 1,072 B, "Copyright (c) 2018 Project Sunbird")* | 🟢 **The counter-example to this file's opening thesis, and the largest one available: a permissive grant at NATIONAL-PLATFORM scale.** Sunbird ED is the building block **DIKSHA**, India's national school platform, is built on — so unlike every other permissive row here it comes with a ministry adopter rather than a pilot. 🔴 **The cost is maintenance, and it is large:** HEAD `9efc8b5` **2025-12-16 — 311 d**. Fork at a pinned SHA, run the client's CVE sweep before week 1 ends, and price a maintenance line; this is a fork-and-maintain base, not an integrate-and-extend one. 🔵 The exact inverse of Moodle's trade (current code, hostile grant) — see `Pattern AG`. 🔴 Sibling `Sunbird-Ed/sunbird-learning-platform` **resolves no ref** and must not be named in a deliverable; a failed resolve cannot distinguish private from deleted. |
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | `main` | 🟢 **MIT** *(`LICENSE`, 1,078 B)* | The handset client for the row above, and the surface that matters wherever the learner's only device is a phone. 🔴 HEAD `9de5e08` **2025-09-19 — 399 d**, staler than the portal, so the mobile path carries the heavier maintenance share. 🔵 Pairs with [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) rather than competing with it: Kolibri owns the offline-first runtime, this owns the DPI-aligned content contract. |

## Tier 2 — Content, courseware and assessment

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 **Apache-2.0** | Structured interactive lessons with a real pedagogy engine (misconception-aware branching). Permissive, which is rare at this level of pedagogical depth. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🟢 **MIT** | Offline-first learning runtime for low-connectivity deployment. The single most important repo on this shelf for LATAM and African engagements. |
| [serlo/serlo.org](https://github.com/serlo/serlo.org) | `main` | 🟢 **Apache-2.0** | German open learning platform — permissive, EMEA-native, curriculum-aligned content model. 🔴 🆕 `p390` **Dated: last commit `2023-02-09` — 1,351 days.** Serlo the *service* is very much alive (`serlo.org` serves German schools daily); this *repository* is not where it is developed any more. Keep it as the **content-model reference** — the permissive, curriculum-aligned data shape is still the most useful thing here — but do not plan a fork or a dependency on it, and ask Serlo where the current code lives before quoting an EMEA-native platform base. |
| [openfun/richie](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** | Course catalogue and portal front-end from France Université Numérique. Pairs with Open edX as the public face. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 `master` | 🟡 **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in nearly every LMS. 🔴 **Routinely described as MIT; it is not.** Keep H5P as *content* loaded at runtime, not as linked code. |
| [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 `master` | 🔴 **AGPL-3.0** | Open-response and peer assessment. 🔴 `edx/openassessment` and `openedx/openassessment` are both **DEAD** — this is the live address. |
| [opencast/opencast](https://github.com/opencast/opencast) | 🔴 `develop` | 🟡 **ECL-2.0** | Lecture capture and video pipeline. 🔴 `apereo/opencast` is **DEAD**; use this org. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(`LICENSE.md`, 11,342 B; `composer.json` declares `"license": "Apache-2.0"`)* | 🟢 **THE LTI 1.3 DEPENDENCY TO INSTALL — and it corrects `p390`'s finding #1, which told three shelves there was none.** LTI 1.3 is *the* standards surface for putting an agent inside Moodle, Canvas, Blackboard or D2L, and this is a **live** implementation of it: HEAD `66d8e4e`, **2026-10-16 — 6 days**, shipping as packagist **`packbackbooks/lti-1p3-tool` v6.4.4, 68 versions, published 2026-09-23**. Same Apache-2.0 grant as the 1EdTech copy (byte-identical 11,342 B licence), under active maintenance. 🟢 It keeps the **copyleft-firewall** role intact: permissive code talks to a GPL/AGPL platform over the LTI boundary without linking to it. 🔵 Note the ref is **`master`**, not `main` — a `main`-assuming licence read fails silently. |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(11,360 B; `package.json` agrees)* | 🟢 **The Node LTI 1.3 route, and the better default for an agent stack.** HEAD `41f150c`, **2026-10-13 — 9 days**; npm **`ltijs` v7.0.7, 207 published versions, 2026-10-06** — the most actively released LTI implementation this base has read. A standalone LTI *tool* provider rather than a platform plugin, which is the shape an agent engagement actually needs: the agent is its own service, and the LMS launches into it. 🟢 Prefer this over the PHP line unless the client's platform work is already PHP (a Moodle plugin, an Open edX fork). |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🔴 `master` | 🟢 **Apache-2.0** | 🔴 **DEMOTED to a spec citation — do not install it.** Last commit `2020-06-03` — **2,333 days**, and `composer.json` carries no licence field. An unmaintained PHP library handling OAuth 2 / JWT signing and key rotation is a **security** dependency, not merely a compatibility one. 🟢 The architectural role it was shelved for is not lost: it moves to `packbackbooks/lti-1-3-php-library` (above), which is the maintained line. 🔴 🆕 `p391` **It also has an alias:** [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) returns the **identical HEAD sha `3a192de`** — an org rename, one project at two addresses. Counted **once**. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) 🆕 `p391` | `master` | 🟡 **MIT** | 🔴 **The Python LTI route, and it is genuinely dead — which is an architecture constraint, not a shelf note.** Last commit `2022-11-21` — **1,431 days**; PyPI **`PyLTI1p3` 2.0.0, published 2022-11-20**, 29 releases, none since. 🔴 🆕 `p392` **And `p391`'s conclusion from this row is withdrawn.** It read *"so there is no maintained in-process Python LTI option: the edge must be `ltijs` (Node) or `packbackbooks` (PHP) fronting the Python agent over HTTP"*. `pylti1.3` is dead — that part is right — but **it is not the Python route**; it is one dead address on a road with three live ones (next three rows). `Gap 391-A` is **CLOSED**. |
| [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) 🆕 `p392` | `main` | 🟢 **MIT** *(1,098 B, "Copyright (c) 2022 The Regents of the University of Michigan"; PyPI classifier agrees)* | 🟢 **THE IN-PROCESS PYTHON LTI 1.3 ROUTE, AND IT IS THE ONE `Gap 391-A` SAID DID NOT EXIST.** A Django reusable app providing **LTI Advantage** — `pip install django-lti`, add `lti_tool` to `INSTALLED_APPS`, add `LtiLaunchMiddleware` after `SessionMiddleware`, migrate. That is the whole integration: **no second runtime, no sidecar, no HTTP hop**, which is the deployment component `p391` told three shelves and two patterns to budget for. HEAD `1ac0b56`, **2026-10-20 — 2 days**; PyPI **`django-lti` v0.10.1, 17 releases, 2026-08-07**; 264 commits, **26 ★**. 🟢 Maintained by the **University of Michigan Center for Academic Innovation** — an institutional maintainer in the region that buys the most LMS integration work. 🔴 Django-shaped: a FastAPI or Flask agent still needs the launch handled elsewhere, and there is **no release tagged on GitHub** (read PyPI for the version, not the Releases tab). |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) 🆕 `p392` | `main` | 🟢 **BSD-3-Clause** *(1,528 B, "Copyright (c) 2016, Project Jupyter Contributors")* | 🟢 **The Python LTI route for the one surface where most CS and data-science teaching already happens.** Implements **both LTI 1.1 and LTI 1.3** authenticators for JupyterHub, so an LMS launch lands the student directly in a running notebook with their identity attached. HEAD `c0c3bf3`, **2026-07-01 — 113 days**; PyPI **`jupyterhub-ltiauthenticator` v1.6.3, 15 releases, 2026-03-26**; 523 commits, **73 ★**. 🟢 **This is what makes `Pattern B` whole** — `jupyterhub`, `nbgrader` and [jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) are already on these shelves, and this is the missing launch edge between them and the client's Moodle or Canvas. 🟡 113 days is slower than `django-lti`; for a Jupyter stack that is a feature, not a risk — but read it as a stable component, not an active one. |
| [openedx/xblock-lti-consumer](https://github.com/openedx/xblock-lti-consumer) 🆕 `p392` | 🔴 `master` | 🔴 **AGPL-3.0** *(34,520 B)* | 🔴 **The best-maintained Python LTI 1.3 implementation in any language — and it is off the permissive shelf.** HEAD `5ba9d16`, **2026-10-22 — committed today**; PyPI `lti-consumer-xblock` **v11.4.2**. Recorded as a **boundary, not a pick**: it is the *platform* side (Open edX consuming an external tool), and AGPL-3.0 reaches hosted use. 🔵 Its existence is why `Gap 391-A` should never have been written as a supply claim — the Python LTI supply was not thin, it was **licence-filtered**, and nobody had split those two readings. |
| [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) 🆕 `p392` | `main` | 🟢 **MIT** *(1,076 B)* | 🟢 **The serverless Node LTI 1.3 route — the shape `ltijs` cannot take.** *"Serverless-native LTI 1.3 toolkit for Node.js (Lambda, Workers, Hono)"*: a seven-package monorepo (`@lti-tool/core`, `hono`, `memory`, `dynamodb`, `postgresql`, `mysql`, `d1`) with **OIDC, Assignment and Grade Services, Names and Role Provisioning, Deep Linking and Dynamic Registration** all implemented, and the session store chosen at deploy time rather than assumed. HEAD `1fa0148`, **2026-10-20 — 2 days**; npm **`@lti-tool/core` v1.3.2, 2026-10-21**; 353 commits, **8 ★**. 🟢 Prefer it over `ltijs` when the deliverable is **Cloudflare Workers or Lambda**: `ltijs` assumes a long-running Node process with Mongo. 🔴 **8 ★ and no stated production claim** — the README's only such wording is a *"Production-ready security features"* heading, which is about the security section, not the project. Pilot it; do not put a ministry on it this quarter. |
| [mdestafadilah/proctoring.js](https://github.com/mdestafadilah/proctoring.js) 🆕 `p392` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **THE GRANTED PROCTORING COMPONENT `Gap 391-C` SAID DID NOT EXIST — and its privacy posture is the reason to shelve it rather than merely record it.** *"Zero-dependency browser proctoring toolkit: tab-switch, camera, face and audio monitoring with a single event API."* Detects tab switching, right-click, DevTools/view-source shortcuts, clipboard copy/cut/paste, camera state, **faces**, audio loudness, and **third-party capture software — virtual cameras, loopback audio, screen shares**. Face detection is `@vladmandic/face-api` 1.7.15 on TensorFlow.js/WebGL, **in the browser**. HEAD `c49b41c`, **2026-09-28 — 24 days**; npm **`proctoring.js` v0.5.1, 2026-09-24**; 46 commits, **1 ★**. 🟢 The README's claims are the sellable part, and they are unusually specific: *"No hidden network calls. Nothing leaves the page unless you set `backend.endpoint`"*; audio is analysed in memory and **discarded, never recorded**; the clipboard is **never read** (the event, the element and a character count only); screenshots are **off by default** and held in memory. 🔴 **1 ★, 46 commits, one maintainer** — vendor it, read it, own it; do not sell it as a maintained dependency. 🔴 By default it loads face-api **and its weights from jsDelivr at runtime** — a supply-chain and data-residency defect in any EU or public-sector deployment. **Self-host the weights**; the README says you can. 🔴 And the EU obligation does not transfer with the licence: *you* become the deployer of a high-risk Annex III system the moment this drives an exam decision. |
| [Scaler-Opensource/exam-guard](https://github.com/Scaler-Opensource/exam-guard) 🆕 `p392` | `main` | 🔴 **CONFLICT — Apache-2.0 in the payload, ISC in the manifest** *(`LICENSE` 11,356 B is the stock Apache-2.0 text; `package.json` at the same ref declares `"license": "ISC"`, and npm `@exam_guard/core` v10.1.0 declares ISC too)* | 🟡 **The bigger proctoring codebase, the weaker grant record, and the AI half is explicitly unbuilt.** *"AI Proctoring tool developed by Scaler"* — 398 commits, HEAD `d1193a6`, **2026-10-13 — 9 days**, npm **`@exam_guard/core` v10.1.0, 2026-10-13**, **3 ★**. What it actually ships is **browser lockdown and event telemetry**: blocks copy/paste/cut, right-click, text selection and keyboard shortcuts; detects `tabSwitch`, `browserBlur`, `rightClick`, `exitTab`, `copyPasteCut`, `restrictedKeyEvent`, `textSelection`, `fullScreen`; takes periodic page and webcam snapshots and POSTs events to an `eventsUrl` **you must build**. 🔴 **The README marks object detection, multiple-face detection and eye tracking *"(To be Done)"*** — so the "AI" in the name is a roadmap, not a dependency. 🔵 **Which is good news for a regulated deployment:** lockdown and event telemetry do no biometric inference, so this component is *not* the Annex III surface — the inference you add on top is. 🔴 Both readings of the grant are permissive and OSI-approved, so this is **publishable but ambiguous**; get the maintainer to reconcile the two files before a client depends on it (`gate-conflict`'s class). 🔵 [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) returns the **identical HEAD sha `d1193a6`** — one project at two addresses, counted **once**. |
| [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) 🆕 `p392` | `main` | 🟡 **MIT — CODE ONLY** *(1,069→1,072 B, "Copyright (c) 2025-2026 MCP Brasil"; `pyproject.toml` and the PyPI classifier agree — **and the README states the grant covers the code alone: each of the 70 data sources carries its own licence in `SOURCES.md`, under an `ACCEPTABLE_USE.md` policy**)* | 🟢 **THE LATAM ANALOGUE OF THE US DISTRICT-TARGETING INSTRUMENT — `Gap 391-B` closed for Brazil, 24 hours after it was opened.** An MCP server over **70 Brazilian public data sources**, 533 tools, **66 of them needing no API key**, with large datasets cached locally and queried through embedded DuckDB. The education ones are the point: **INEP `censo_escolar`** (the national school census — the per-school enrolment and infrastructure base a Brazilian pilot is scoped against) and **INEP `enem`** (the national exam microdata). HEAD `2efb258`, **2026-08-18 — 65 days**; PyPI **`mcp-brasil` v0.14.0, 18 releases, 2026-04-24**. 🟢 **Its LGPD handling is why this is shelvable and not merely findable.** `SOURCES.md` grades *Educação* **RISCO ALTO**, records that INEP withdrew microdata in 2022 under LGPD and resumed anonymised publication in 2024, states that the bundled snapshot is **2023, post-LGPD**, and documents a **code safeguard**: `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate categories only (UF, sex, age band, race, school) and **does not expose** `NU_INSCRICAO`, name or CPF. 🔴 **Three limits to state in a proposal:** the data is a **2023 snapshot**, so currency is the risk and not the licence; the project's own note is to *validate a sample to confirm anonymisation*; and it is **explicitly not an official government service**. 🔴 A dating disagreement, published rather than resolved: this base's harvest row reads *"pushed 2026-10-20"* while `main`'s HEAD commit is **2026-08-18**. Two different signals — `pushed_at` spans every ref, a HEAD date does not. 🔵 This row is also `Gap 549` in the flesh: **a code grant and a data grant in one repository**, and this shelf's licence column was built for the first. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main` | 🟡 **`(ODbL-1.0 AND CC-BY-SA-4.0)`** 🆕 `p390` *(exact SPDX expression, read from `package.json`; the tree carries **two** files — `LICENSE` (ODbL, 25,289 B) and `LICENSE-CONTENT`. There is still no separate permissive code grant.)* | 🆕 `p384`. **The curriculum prerequisite graph**: `v1` ships **1,930 micro-topics** and **4,102 prerequisite edges** as a DAG (`hard`/`soft`, each edge carrying a reason) over **9 subjects**, aligned to NGSS, Common Core, the UK National Curriculum and the Australian curriculum. Data at `data/topics.json`, `data/dependencies.json`, `data/teaching-research.json` (~24 MB). 🔴 **A share-alike *database* licence, not a code licence** — grounding a tutor on it is a §4.3 *Produced Work* (attribution notice only); shipping an extended taxonomy is a §4.4 *Derivative Database* (share-alike). See **Pattern H**. 🟡 Maintainer-stated gap: teaching research covers **1,049** topics, **881 have none**. 🔴 🆕 `p390` **The `CC-BY-SA-4.0` half is the one that reaches the client deliverable**: the *content* (topic prose, teaching research) is share-alike independently of the ODbL database right, so a curriculum document generated from it can inherit SA even where the DAG itself is only a Produced Work. Clear this with the client's legal team **before** it is a deliverable, not after. Dated `2026-10-22` — actively maintained. |
| [intellectif/learning-kit](https://github.com/intellectif/learning-kit) 🆕 `p391` | `main` | 🟢 **MIT** *(1,071 B; `package.json` agrees)* | 🟢 **A permissive, headless alternative to H5P — and the assessment component this shelf was thin on.** TypeScript-first SDK for interactive educational activities, described by its own README as *"a lightweight, composable, bring-your-own-backend alternative to H5P"*, for React 19. `@intellectif/lk-core` is the part that matters to a studio: **schemas, a pure scoring engine, rubric and deferred grading, assessment composition, attempt plans, redaction, and an xAPI statement builder — with zero runtime dependencies beyond Zod**. `@intellectif/lk-react` adds components and a resumable exam/review pager. 🟢 **Three properties that decide an engagement:** scoring is a *pure function* a client can unit-test and an auditor can read; **deferred grading** means a human marker stays in the loop by construction, which is the posture EU high-risk assessment obligations ask for; and **redaction** is in the core rather than bolted on. 🟢 Pairs directly with the xAPI/LRS rows on this shelf — it emits statements, it does not store them. HEAD `1e39e9e`, **2026-10-18 — 4 days**. 🔴 **It is deliberately not a CMS:** authoring UI, content storage, delivery, auth and the learner database are the consuming application's job. 🟡 The two packages' version numbers moved apart at 1.0, so a `lk-react` major is not by itself a breaking React API change — read its changelog. |

## Tier 3 — Grading, notebooks and the CS-teaching stack

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | `main` | 🟢 **BSD-3-Clause** | Multi-user notebook serving — the standard way a cohort gets identical compute. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** | Release / collect / autograde / return. The assignment lifecycle, already solved. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🔴 `master` | 🟢 **BSD-3-Clause** | Autograding at Berkeley cohort scale; container-isolated execution. |
| 🆕 `p393` [edulinq/autograder-py](https://github.com/edulinq/autograder-py) | `main` · `7984bd2` | 🟢 **MIT** *(1,071 B, `7eb48830c022`)* | The **submission and feedback** client for the edulinq autograding server — the half `nbgrader` and `otter-grader` leave to the institution. **49 releases**, 494 commits, HEAD **2026-10-02 — 20 d**, **16 ★**. 🔵 Pairs with `otter-grader` (grading) rather than competing with it. |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Pedagogical assessment of *how* code was written. The missing half of autograding. 🔴 🆕 `p387`: **PyPI `pybryt` has had no release since v0.7.0 on 2022-04-28.** Keep it as the design it states, vendor the code, and do not sell a client a dependency that has not shipped in four and a half years. The maintained halves of this tier (`nbgrader`, `otter-grader`) are where the running infrastructure should sit. |
| 🆕 `p394` [rstudio/gradethis](https://github.com/rstudio/gradethis) | `main` · `48aaf89` | 🟢 **MIT** *(1,078 B, `48c18e68ffed`; `DESCRIPTION`: `MIT + file LICENSE`)* | **Automated feedback for student exercises**, from **Posit Software, PBC**. `grade_this_code()` compares against a model solution; `grade_this()` takes a predicate you write. HEAD **2026-06-18 — 126 d**, **164 ★**, 41 forks. 🟢 **The most-starred *maintained* autograder on this shelf and the most permissively licensed** — it edges `otter-grader` at 161 ★. 🔴 `okpy/ok` leads outright at **370 ★**, 532 d stale (`Gap 397-A`). 🔴 **Not a CRAN package** (`cran/gradethis` ABSENT), so install from GitHub or r-universe, not from CRAN. |
| 🆕 `p394` [rstudio/learnr](https://github.com/rstudio/learnr) | `main` · `e7164a8` | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* | **Interactive tutorials in R Markdown** — the runtime `gradethis` grades inside; the two are a pair, not alternatives. **738 ★**, 241 forks. 🟡 HEAD **2025-11-13 — 343 d**: a stable substrate rather than an abandoned one, and the movement is in `gradethis`. |
| 🆕 `p394` [ucbds-infra/ottr](https://github.com/ucbds-infra/ottr) | 🔴 `master` · `693b3df` | 🟢 **BSD-3-Clause** *(🔴 the grant is at `LICENSE.md`, **1,555 B · `1677c5307530`**, re-read at this commit on 2026-10-25 and `GRANT-PRESENT` clause-by-clause; `LICENSE` itself is a **108 B** `YEAR:` / `COPYRIGHT HOLDER:` stub — `DESCRIPTION`: `BSD_3_clause + file LICENSE`. A probe that takes the first filename-ladder hit reads this repository as ungranted: `Gap 441-A`)* | **The R autograding extension for `otter-grader`** (row above), UC Berkeley Data Science Education Program — grades R scripts, Rmd documents and Jupyter notebooks with R kernels. HEAD **2026-07-06 — 108 d**. 🟢 So this tier's flagship autograder is permissive in **both** languages. 🔴 **3 ★**: the adoption sits on the Python parent, but this is the component an R course actually deploys. |
| 🆕 `p394` [cran/exams](https://github.com/cran/exams) | `master` · `baa3e28` | 🟡 **GPL-2 \| GPL-3** — 🔴 **disjunctive**, and 🔴 **no licence file at any tree path**: the grant is the `License:` field in `DESCRIPTION` | **R/exams v2.4-5**, Achim Zeileis (R-project). HEAD **2026-10-08 — 14 d**. 🟢 **The broadest assessment exporter on these shelves**: QTI 1.2, QTI 2.1, Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS, TestVision, Particify, ARSnova, Kahoot!, Grasple, TCExam — read from the `R/` source filenames in the clone (`exams2qti21.R`, `exams2moodle.R`, `exams2canvas.R`, …), not from its prose. 🟢 **Plus NOPS**: a standardised PDF printed, scanned and marked automatically — the only offline assessment loop in this base. 🔵 Belongs with **Tier 8** as much as here; it is the generator the standards layer consumes. |
| 🆕 `p394` [philchalmers/mirt](https://github.com/philchalmers/mirt) | `main` · `e37f14c` | 🟡 **GPL (>= 3)** — 🔴 **`DESCRIPTION` only; GitHub's sidebar shows no licence** | **Multidimensional item response theory** — the canonical IRT engine, v1.48.2. HEAD **2026-10-21 — 1 DAY**, **235 ★**, 88 forks. 🔵 This shelf's Tier 4 carries `adaptive-knowledge-graph` (IRT + BKT, ~350 ★) and `OATutor` (BKT) as the adaptive layer; **`mirt` is the thing those approximate**, and it is committed daily. Sibling [`cran/catR`](https://github.com/cran/catR) (🟡 GPL >= 3, v3.17) is the **computerized adaptive testing** engine, [`cran/TAM`](https://github.com/cran/TAM) (🟡 GPL >= 2, v4.3-25) the test-analysis modules, and [`patriciamar/ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) (🟡 GPL-3, **47 ★**) the non-programmer front end. |

🔴 **The licence line through this tier runs between DELIVERY and MEASUREMENT, and `p394` found it by
accident.** The three components that *run the teaching loop* are permissive — `gradethis` MIT,
`learnr` Apache-2.0, `ottr` BSD-3-Clause — and every component that *measures the learner* is GPL:
`exams`, `mirt`, `catR`, `TAM`, `ShinyItemAnalysis`. 🟢 **That is a workable boundary rather than a
blocker**, because it falls exactly where a studio's product boundary falls anyway: embed the tutoring
and grading loop, reach the psychometrics **over a process boundary**, the same discipline `Pattern A`
and `Pattern O` already apply to copyleft LMSs. 🔴 **But `cran/exams`'s grant is disjunctive — GPL-2
*or* GPL-3 at the licensee's choice — and that choice must be recorded once, deliberately**, because
downstream compatibility differs between the two rungs.

🔴 **A provenance warning this tier needs and the others do not.** `cran/exams`, `mirt`,
`ShinyItemAnalysis`, `cran/catR` and `cran/TAM` have **no licence-shaped file at any path in their
trees** — enumerated, not guessed. GitHub's sidebar therefore shows **no licence** for all five, and a
reviewer who checks the sidebar will report five granted GPL packages as unlicensed. The authoritative
grant is the `License:` field in `DESCRIPTION`, which is what CRAN itself enforces. 🔵 Registered as
**`Gap 394-B`**, because this base already knows the rule — `p1052` carries `DESCRIPTION` in its
manifest list with a test asserting *"CRAN: the grant lives in DESCRIPTION and must be read
verbatim"* — and `licence-grant-gate`, the instrument that produces the verdicts, does not.

## Tier 4 — Measurement, memory and retrieval (what makes the agents honest)

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | 🟢 **MIT** *(`LICENSE.md`)* | The eval runner. Nothing in this industry should ship without a before/after on the client's own subject mix. |
| [hendrycks/test](https://github.com/hendrycks/test) | 🔴 `master` | 🟢 **MIT** | **MMLU** — 57 academic subjects. The subject-level breakdown is the useful part, not the headline score. |
| [openai/grade-school-math](https://github.com/openai/grade-school-math) | 🔴 `master` | 🟢 **MIT** | **GSM8K** — multi-step arithmetic reasoning; the canonical K-12 maths probe. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | 🟢 **MIT** | **FSRS** scheduler. A retention model with published parameters — the part of "personalisation" that is actually measurable. Note [ankitects/anki](https://github.com/ankitects/anki) itself is **AGPL-3.0**; the scheduler is the reusable piece. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | 🟢 **Apache-2.0** | Document-aware RAG — handles the textbook/worksheet/PDF reality of course material. |
| [livekit/agents](https://github.com/livekit/agents) | `main` | 🟢 **Apache-2.0** | 🆕 `p390`. 🟢 **The realtime voice substrate — the piece a spoken tutor should never write itself.** Full-duplex STT → LLM → TTS pipelines with **turn detection, interruption handling and barge-in**, the three things that separate a tutor a child will talk to from a demo. Provider-agnostic on all three legs, so the ASR can be swapped for a local model where data residency demands it. This is what `Manu` (Tier 4, [`agents/top.md`](../agents/top.md)) is built on, and why that project is ~15 days old and already has a working voice loop. Dated **2026-10-22**. See 🆕 `Pattern V`. |
| [mozilla/common-voice](https://github.com/mozilla/common-voice) | `main` | 🟡 **MPL-2.0** *(code; the **corpora** are **CC0-1.0**)* | 🆕 `p390`. 🟢 **The licence answer to regional-language speech.** Crowd-sourced, CC0 speech corpora across ~130 language variants — including **pt-BR, es-419 variants, Kiswahili, Hindi and Bengali** — which is the fine-tuning and ASR-evaluation data a voice tutor needs outside English. 🟢 **CC0 on the data is the strongest possible position**: no attribution, no share-alike, usable in a commercial deliverable. 🟡 MPL-2.0 is weak file-level copyleft and applies to the **platform code**, not the corpora — do not conflate the two when quoting. Dated **2026-10-21**. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | `main` | 🟢 **Apache-2.0** *(`LICENSE.md`)* | Ingest for the formats education actually runs on: PDF, DOCX, PPTX, scans. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | 🟢 **MIT** | Programmatic prompt optimisation — turns "we tuned the tutor prompt" into something with a metric attached. |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | 🟢 **MIT** | The campus LLM gateway universities actually deploy: multi-provider, SSO, per-user quota, audit. MIT where the obvious alternative is not (see [`agents/top.md`](../agents/top.md)). |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🔴 `master` | 🟢 **MIT** | 🆕 `p389`. **Bayesian Knowledge Tracing, fitted from the client's own interaction logs** — and the maintained answer to a gap this base has carried for two passes. `Pattern B` stands on [microsoft/pybryt](https://github.com/microsoft/pybryt), whose published artefact has had **no release since 2022-04**; this is a *different* job (mastery estimation, not approach assessment) but it is the piece that makes "adaptive" a number instead of an adjective. 🟢 **Last commit 2026-10-21 (1 d)**, from UC Berkeley's CAHLR, who also maintain [`OATutor`](https://github.com/CAHLR/OATutor) (MIT) on [`agents/top.md`](../agents/top.md). 🟢 Per-skill learn/guess/slip/forget parameters are inspectable and defensible — which is what a district's procurement rubric asks for when it asks how the system decides a student is behind. |
| [docling-project/docling](https://github.com/docling-project/docling) | `main` | 🟢 **MIT** | 🆕 `p389`. **Course-material ingest, MIT, and committed today (0 d).** Layout-aware parsing of PDF, DOCX, PPTX, XLSX, HTML and images into a structured document model, with table structure and reading order preserved — which is the difference between a tutor that can cite page 7's table and one that cannot. 🟢 Chosen over [allenai/olmocr](https://github.com/allenai/olmocr) (Apache-2.0) **on the date**: olmocr's last commit is **2026-03-25, 211 days**. 🟢 Complements, not replaces, [`unstructured`](https://github.com/Unstructured-IO/unstructured) — docling is the stronger reader for textbook-shaped PDFs, `unstructured` has the wider connector set. |
| [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) | `main` | 🟢 **BSD-3-Clause** | 🆕 `p389`. **Jupyter with no server: the kernel runs in the browser via WebAssembly.** Last commit 2026-10-16 (6 d). 🟢 Two education problems it solves outright: a CS or data-science exercise that needs **no per-student compute, no container and no install** (the cost line that kills notebook teaching at scale), and a **lab that works offline once the page is cached** — the `Pattern D` constraint, met without shipping a server. 🟡 No server means no server-side autograding: pair it with [`nbgrader`](https://github.com/jupyter/nbgrader) on a submitted notebook rather than expecting it to assess in place. |
| [pipeworx-io/mcp-education-data](https://github.com/pipeworx-io/mcp-education-data) 🆕 `p391` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **The first row on these shelves that answers *which district*, rather than *what to build* — engagement targeting and funding data, not a classroom capability.** Four MCP tools over **keyless US federal data**: `education_find_schools` (NCES Common Core of Data via the Urban Institute — enrolment, charter/magnet status, grade range, free/reduced-price lunch counts), `education_find_districts` (LEA id, schools, enrolment, teacher counts), **`education_district_finance`** (revenue split **federal / state / local** and expenditure by function, with computed **per-pupil spending**) and **`education_child_poverty`** (Census SAIPE estimates of 5–17-year-olds in poverty — **the figures that drive federal Title I funding**). 🟢 **Why a studio cares:** a North America pitch can be priced against a named district's actual per-pupil budget and Title I eligibility before the first call. 🔴 **Three caveats that belong in the row:** it is an **unofficial** integration, not affiliated with the upstream provider; the default path is a **hosted gateway** (`gateway.pipeworx.io`), so a district deployment means self-hosting or accepting a third party in the data path — the data is public, but the *query pattern* may not be something a client wants off-premises; and a scoped endpoint also lists **~30 shared gateway meta-tools**, so the real context cost is far above four tools. 🟡 The finance survey **lags the directory data by 1–2 years** — never quote per-pupil spend as current-year. HEAD `060371b`, **2026-10-21 — 1 day**. |

## Tier 5 — Student information / administration

| repo | default ref | licence | note |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** | Odoo-based education ERP/SIS. Default ref is a **version branch**, `19.0` — there is no `main`. 🔴 `OpenEduCat/OpenEduCat` is **DEAD**; this is the live address. Its Brazil and Mexico country pages are vendor marketing — treat feature claims as unverified. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 **MIT** | Laravel school-management platform with **Spanish and French built in**. SME-scale, not university-scale. The only permissive, Spanish-native administration platform found in this pass — relevant to the LATAM supply gap recorded in [`intel/market.md`](../intel/market.md). |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`master`** | 🟡 **GPL-2.0** — 🔴 grant is at **`docs/License.txt`** (17,286 B), **not** at any root path; `index.php` and `Modules.php` headers pin *"version 2 of the License"* | 🆕 `p384`. The most widely deployed open-source SIS in the K-12 tier. GPL-2.0 is survivable the same way Moodle is — reach it over its API, do not link to it. 🔵 **This repo is why the licence probe set grew from seven paths to eight**: a root-only read returns "ungranted" for a repository with a perfectly standard grant one directory down. |
| 🆕 `p393` [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) | `main` · `6b13cb9` | 🟢 **Apache-2.0** *(11,357 B, `c71d239df917` — 🔵 **STOCK**, this pass's reference byte count)* | 🟢 **The North American K-12 data path, and the first Ed-Fi row on these shelves.** Ed-Fi is the dominant US K-12 **data standard** (state longitudinal systems, district warehouses); this is a maintained Python client for its API — paging, auth, swagger introspection, async pulls. HEAD **2026-10-06 — 16 d**, 79 commits, PyPI v0.4.1, **15 ★**. 🔵 For a North America engagement this is the **roster-and-outcomes join** that `Gap 391-B`'s district instrument needs, and it is Apache-2.0. |
| 🆕 `p393` [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit) | `main` · `b1266b7` | 🟢 **Apache-2.0** *(10,141 B, `cc4d4de0920b` — 🔴 non-stock: the **APPENDIX IS ABSENT**)* | 🔴 **ARCHIVED BY ITS OWNER ON 2025-03-10 — READ-ONLY.** Extractors for **Canvas, Google Classroom and Schoology** into Ed-Fi, plus a harmonizer: 763 files, 451 commits, PyPI `edfi-lms-harmonizer` v1.2.2. 🔵 Published **because** it is archived: it is the best available map of the LMS→Ed-Fi field mappings, and a studio should **read it and port it**, never depend on it. An archived upstream takes no security patch. 🔴 This is the state the licence column cannot show — `Gap 393-E`. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 **AGPL-3.0** — grant is in lowercase **`license.txt`** | Frappe/ERPNext-ecosystem LMS; attractive where the client already runs ERPNext. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 **GPL-2.0-or-later** *(`2.12/LICENSE`, 18,092 B; `composer.json` → `GPL-2.0-or-later`)* | 🆕 `p387`. 🟢 **Brazil's largest free education software, and the SIS a LATAM public-sector engagement will actually meet** — *"o maior software livre educacional do Brasil"*, municipal-scale student records, enrolment, grades. 🔴 **Its real default ref is `2.12`** — a version branch, neither `main` nor `master`: resolved with `git ls-remote --symref` (HEAD `7903a3e`). A `main`-assuming clone or licence read fails or reads the wrong tree, and a `master`-assuming one reads a branch that is not HEAD. 🟡 GPL-2.0 at the platform, so reach it over its API and keep the agent a separate service (`Pattern O`). Sibling `portabilis/i-diario` is AGPL-3.0 — the grant is a per-repository fact, not an organisation-wide one. |

## 🆕 `p387` — Tier 6: the multi-tenant AI layer, which is the thing `p386`'s tenancy gap was asking for

`p386` replaced a licensing gap with a **tenancy** gap: every granted LMS MCP server authenticates
as the signed-in student, so *"a studio cannot deliver one of those to an institution."* On Moodle
the tenancy layer already exists, it is maintained by a state education authority, and this base
has never shelved it.

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) | `main` | 🟡 **GPL-3.0-or-later — granted in the source headers** (`version.php`), no root licence file | 🟢 **A multi-tenant AI backend for Moodle, explicitly offered as the alternative to Moodle 4.5's own single-tenant AI subsystem.** Two subplugin types — `aitool` (connect ChatGPT, Gemini, Dall-E, **Ollama**…) and `aipurpose` (bind a *purpose* to a tool **per role**) — plus per-role rate limits, per-tenant user enable/disable, usage monitoring, teacher visibility of student prompts (capability-gated), and tenant-handling hooks. Release **5.1.1**, version code **2026102305**. 🟢 This is the component that turns "an agent talks to the LMS" into "an institution can deploy it": the **sovereign EMEA option in `Pattern E`**, from Bavaria's state school platform, with a local-model path via the Ollama tool. 🔵 **Cite this address.** The `mebis-lp` organisation serves the same repository at `mebis-lp/moodle-local_ai_manager`, which this base's alias register already records as **STALE** (canonical: `bycs-lp/moodle-local_ai_manager`, resolved `p350`, confirmed `p370`) — 🆕 `p387` re-confirms it mechanically: `git ls-remote --symref` returns the **identical HEAD sha `4ff5a87`** at both, and `version.php` the identical component, release **5.1.1** and version code **2026102305**, which upgrades `p226`'s sibling-set inference from *weak* to an identity read. One repository, one row. |
| [bycs-lp/moodle-block_ai_chat](https://github.com/bycs-lp/moodle-block_ai_chat) | `main` | 🟡 **GPL-3.0-or-later** in `version.php` | The chat frontend that consumes the manager's API. 🔵 Cited at the canonical org, as above; the manager's own README links the sibling set under `mebis-lp` — `tiny_ai`, `block_ai_control` — and both orgs answer, so resolve the ref before you pin one. The family also includes [marcusgreen/moodle-qtype_aitext](https://github.com/marcusgreen/moodle-qtype_aitext) (AI-marked question type, `main`, resolved this pass). **Deploy the manager first, then pick frontends** — not the other way round. |

🔵 **Second instance of `Pattern L` step 8, and it is now a Moodle-wide rule, not an anecdote.**
`p386` found [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp)
granted **only** in `version.php`. Both plugins above are the same: **no root licence file, a full
GPL-3.0-or-later header in `version.php`.** For a Moodle plugin that is the convention Moodle
requires, so *"no `LICENSE` file"* on a Moodle plugin means **read `version.php`**, never
"ungranted".

## 🆕 `p388` — Tier 7: the integration layer, reordered by maintenance rather than by tool count

`p387` dated this shelf and found its richest LMS integration was also its stalest. **This pass found
the replacements**, via a channel nobody here had asked: `registry.npmjs.org/-/v1/search` is open and
**indexes by relevance while reporting publish history**, so "does this exist?" and "is it
maintained?" are answered in one call. 29 education queries → 383 addresses absent from this base →
**22 granted**. Full method in [`repos/trending.md`](trending.md).

| repo | default ref · HEAD | licence | why it is foundational |
|---|---|---|---|
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` · `34e6156` | 🟢 **MIT** (1,070 B) | 🟢 **The maintained teacher/admin Canvas surface, and the new default for an institutional engagement.** 187 tools: grade, comment, rubrics, New Quizzes (LTI), gradebook *history*, enrollments, accounts, analytics, outcomes, grading standards, content exports/migrations, quiz **accommodations**, appointment groups — plus **link audit**, **accessibility audit** and **grade projection**, three deployment modes (stdio, HTTP, library import) and a one-click `.mcpb`. 🟢 **It ships a FERPA mode** — the first time compliance appears as a *product feature* on these shelves rather than a caveat in this base's prose. `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22 (today)**: the most actively published LMS integration here. |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) · [`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server) | `main` · `c7e5725` / `8e424f1` | 🟢 **MIT** (1,091 B, both) | The **student-side** Canvas surface, 209 tools, shipped as a deliberate pair: **Local Edition** (stdio, *no port opened, nothing exposed*) and **Remote Edition** (ngrok, OAuth 2.1, multi-computer failover). Distinctive part is grade *intelligence* rather than grade retrieval: `what_if_grade`, `compute_needed_score`, `grade_impact_ranking`, `study_priority_ranking`, `semester_snapshot`, plus full `.imscc` export. 🔴 Remote Edition opens a **public HTTPS address** — a school's decision, never a default. |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS-side integration on this shelf, and it opens the parent/guardian persona.** 20 tools over **Campus Parent** — schedule, assignments, grades, attendance *events with codes*, behavior, food service, documents, standardized assessment scores, fees, messaging from three sources — with linked districts auto-discovered via **CUPS SSO** and `FeatureDisabled`-awareness so it degrades per district. **47 releases**, → 2026-10-19. 🔵 Every SIS on this shelf until now was a *platform to deploy* (openSIS, i-educar); this is a *surface to read*. |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | The parent-observer scope over Canvas: 18 tools, `canvas_list_observees` as the hinge. 🟢 Download path is hardened in a way worth copying — host-pinned to the Canvas origin, confined to a download directory, never writes through a symlink, new files `0600`. **43 releases**, → 2026-10-16. |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` · `139bb11` | 🟢 **BSD-3-Clause** (1,532 B) | 🟢 **The live replacement for this shelf's most-depended-on stale artefact.** `Pattern B` rested on `pybryt`, last published **2022-04-28**. This is maintained (**v0.3.2, 7 releases, → 2026-09-25**) and from **QuantStack**, a known Jupyter-ecosystem maintainer. Per-cell **Explain Code** sends source, kernel language, **the traceback**, and preceding cells as the exercise statement; the tutor persona lives in a **`TUTOR.md` found by walking up from the notebook**, so it is per-course and version-controlled; `reference_solution` and `evaluation_criteria` ride in cell metadata, **ROT13-encoded** to keep them from the student. |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` · `687c55b` | 🟢 **MIT** (1,070 B) | 🟢 **The North American curriculum-data layer** — the third region to acquire one. 12 tools over the whole **BC Ministry of Education K–12 curriculum** in its real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search, and the **First Peoples Principles of Learning**. Hosted HTTP *or* local stdio. 🟡 2 releases, both **2026-03-27**, and the data is a crawl of `curriculum.gov.bc.ca` — **currency is the risk here, not the licence**. |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` · `3c680e0` | 🟢 **MIT** (1,070 B) | 🟢 **The EMEA institution-shaped integration, and the governance reference on this shelf.** One server spanning **Brightspace + OSIRIS (official records) + MyTimetable + the public Study Guide** behind a single browser sign-in **including MFA**, session self-renewing. 🟢 **Every write action shows a preview and requires confirmation** — the human-oversight control EU high-risk obligations ask for, implemented as the default rather than documented as advice. |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` · `ac0c75f` | 🟢 **MIT** (1,063 B) | Teacher-facing **semester refresh**: reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, emits Canvas-safe HTML. 🟢 The **no-token path is first-class** — generate the HTML, paste it in — so it delivers before anyone grants API access, which is how a pilot actually begins. |
| [gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) | `main` · `7962e49` | 🟡 **GPL-3.0** (284 B short notice) | Node client and CLI for Moodle Core web services **plus the MoodlIA plugin — a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser path. 🔵 A far wider surface than `webservice_mcp`, and GPL is survivable the same way: reached over REST/JSON-RPC, never linked. |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` · `a333415` | 🟢 **MIT** (1,094 B) | 🔵 **Not a teaching tool — a build-cost tool, which is why it is on a foundations shelf.** RAG over a **Moodle codebase** for developers: semantic code search, 7 agents, 9 slash commands, all local. `Pattern A`'s real cost is Moodle plugin work; this is aimed at exactly that. 🟡 v1.0.0, single publish 2025-10-12. |

🔵 **How to read this tier against Tier 1–6.** Those tiers are **systems to deploy**; this one is
**surfaces to read and write**. A studio picks one platform base from Tier 1 and then one integration
row here *per persona* — and the personas are no longer two. Teacher/admin (`bruchris`), student
(`Fireiscoolsolo`), parent/guardian (`chrischall`) are three distinct tool surfaces over the *same*
institutional data, and **the tool counts are scope, not quality**: 187 vs 209 vs 20 reflects who is
being served, not which is better built.

🔴 **The maintenance rule this tier is sorted by, stated so it survives the next pass.** `p387`
established that **recency replaces popularity** here, because no star channel is open. `p388` adds
the corollary: **where two integrations cover the same surface, prefer the one still publishing** —
`canvas-mcp-server` (54 tools, last shipped 2025-06-27) is now dominated on both axes by a 187-tool
server that published today. Tool count and maintenance pointed in opposite directions for one pass;
they no longer do.

🔴 **And a supply category this shelf could not previously name: published-but-unreadable.** Six
addresses from the same sweep **publish to npm from a repository that prompts for credentials** —
the dependency is installable, its provenance is not auditable. The costliest is
[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit) (**103
published versions**, manifest MIT, SCORM support), and the most instructive is
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest reads
**`"SEE LICENSE IN LICENSE"`** — pointing at a file in a repository nobody can read. 🔵 `Pattern L`
clears a repository by reading its subtree; **there is no subtree here to read**, so these cannot be
cleared that way. For an npm-only dependency the rule is: **the manifest is a claim, the tarball is
the evidence** — and `registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves that tarball even when the
repository is closed. Full table and the Santillana case in
[`agents/top.md`](../agents/top.md#-no-licence-file--and-ungranted-is-three-different-things).

## 🆕 `p393` — Tier 8: the 1EdTech standards layer, which is where Python's education supply actually is

`p388` opened Tier 7 with a channel nobody had asked (npm search). This tier exists because `p393`
opened the **other** channel — `pypi.org/simple/`, PEP 691, **920,784 names in 45 MB in 1.4 s** — and
what came back was not more MCP servers but the **interoperability plumbing**: LTI, QTI, OneRoster,
Caliper, Ed-Fi. 🔵 **Read that as a sourcing rule, not a curiosity:** the integration layer is written
in Python and the agent layer is written in TypeScript, so a sweep of one registry answers only half
the question — and this base answered it with npm alone for eleven passes.

| repo | default ref · HEAD | licence (payload) | why it is foundational |
|---|---|---|---|
| 🆕 `p393` [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | 🔴 `master` · `22c6f2f` | 🟢 **MIT** *(1,078 B, `504c17f9869b`)* | **The fourth Python LTI 1.3 implementation**, from **Open FUN — France Université Numérique**, the French state's higher-education platform operator. A Django app for building LTI **Tool Providers**. PyPI v2.0.0, 7 releases, 53 files, **14 ★**. 🔴 **HEAD 2024-11-14 — 707 days.** Granted and architecturally useful; **cold**. Read it for its shape, pick `django-lti` to ship. |
| 🆕 `p393` [Harvard-University-iCommons/django-lti-dynamic-registration](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) | `main` · `2873d2f` | 🟢 **MIT** *(1,100 B, `1ade29a33914`)* | **The fifth**, and the only one covering **LTI Dynamic Registration** — the flow that lets a tool be installed in an LMS without a human exchanging keys. An explicit add-on to `academic-innovation/django-lti`, so it **composes with** `Pattern B`'s pick rather than replacing it. 🔴 HEAD **2025-09-15 — 402 days**, 19 commits, **3 ★**: a small, single-purpose, cold component — vendor it and own it. |
| 🆕 `p393` [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) | `main` · `e22fc04` | 🟡 **LGPL-3.0** *(7,652 B, `e3a994d82e64`, at **`LICENSE.LGPL-3.0`**)* | **Writes QTI** assessment packages for **Canvas and Blackboard** from plain question banks — the export half of an assessment pipeline. 381 commits, HEAD **2026-10-12 — 10 d**, PyPI `qti-package-maker` v26.7.14, **4 ★**. 🔴 **This base first published this row as UNGRANTED and was wrong**: a six-name licence-filename probe missed `LICENSE.LGPL-3.0`. Corrected by enumerating the tree. 🟡 **LGPL, so library-linking is fine and modification is not**: use it as a dependency, do not fork it into a product. |
| 🆕 `p393` [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) | `main` · `7a7ec60` | 🔴 **GPL-3.0** *(35,196 B, `f93eb1d94904`)* | **Converts QTI 2.x → 3.0 and 3.0 → 2.1** — items, tests, stimuli and content packages — from **Citolab**, the lab of **Cito, the Dutch national assessment institute**. The migration nobody else here supplies, and QTI 3.0 is the version procurement is starting to demand in EMEA. 🔴 **GPL-3.0: off the permissive shelf.** Run it as a **batch tool at arm's length** (a container invoked by a pipeline), never linked into delivered code. 🔵 Its TypeScript sibling [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) serves the **byte-identical** payload — so here the grant is **org-shaped, not language-shaped**, the exact complement of `Gap 391-A`'s lesson. |
| 🆕 `p393` `superbuilders/timeback-dev-python` *(🔴 unlinked deliberately — an absent address may not be linked from a live shelf: `gate-dead-citation` I2)* | 🔴 **does not resolve** — 🔵 and `p371`/`p372` already recorded it `NO-REMOTE`; what is new is that it is the declared source of **147 live releases** | 🔴 **UNAUDITABLE — MIT declared on PyPI, no payload obtainable** | The declared source of **three** live PyPI packages — `timeback-qti`, `timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last **2026-07-18**: on paper the most complete 1EdTech client family in Python. 🔴 **The repository does not resolve for an unauthenticated clone, so the MIT claim cannot be checked even in principle.** `Gap 393-B`. 🔵 **The procurement line to say out loud:** a studio may evaluate these in a sandbox; it may not **warrant** them to a client, because warranting a licence means having read it. If the roster/QTI client is needed and granted, build on `oneroster`-shaped code you can read, or ask the publisher to open the repository. |

🔵 **What this tier changes about how this base searches.** `Gap 392-C` was right that the language
bias of a discovery channel becomes a supply claim — and the correction is not "also sweep PyPI once".
It is that **a supply question needs one channel per ecosystem**, and this base can now name its set:
`registry.npmjs.org/-/v1/search` (npm, relevance + publish history), `pypi.org/simple/` (PyPI, the
whole name space), `packagist.org/search.json` (PHP — open, measured by `p392`, **0 shelvable**), and
`raw.githubusercontent.com` + `git ls-remote` for first-hand verification of whatever any of them
returns. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** — and `R` matters here, because
`otter-grader` grades R and the statistics-teaching stack is CRAN-shaped.

## 🆕 `p431` — Tier 9: the evaluation layer, which is what makes every other tier's claim checkable

Every tier above supplies something that **does** tutoring, grading or delivery. None of them
supplies anything that says whether the tutoring was any **good**. `Trend 8` has carried that as an
open measurement gap for many passes. Measured first-hand on 2026-10-25, the layer exists:

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` | Scenario-based evaluation **and regression** engine. Diagnoses a concrete pedagogical failure and keeps the evidence to re-test it after the fix. The CI gate for a tutoring deliverable. **Maintained** — commit 2026-10-25. |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | **MIT** | `772f5cdca5dd` | `LICENSE` 1 099 B · `8a0a4ba421a0` | Runs a model as tutor **and** as simulated student across existing ITSs (`ctat`, `apprentice`, `oatutor`). The acceptance-test fixture. 🟡 Stale since 2025-09-10 — fork it. |
| [DannyWeitekamp/tutorenvs](https://github.com/DannyWeitekamp/tutorenvs) | **MIT** | `eacba91d2b6b` | `LICENSE` 1 064 B · `eb1ef5e1a637` | `tutor_gym`'s upstream. Relevant only if the fork diverges; recorded for lineage. |
| [Teachable-AI-Lab/tutorenv](https://github.com/Teachable-AI-Lab/tutorenv) | **MIT** | `b90a4d01f2f1` | `LICENSE` 1 064 B · `eb1ef5e1a637` | Lineage root. Payload **byte-identical** to the row above — same grant, re-attributed at the fork. |

**4 verified permissive rows, bringing this file to 11 permissive foundations.**

🟢 **The composition that comes free.** `tutor_gym`'s `oatutor` backend binds to
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT), already on this shelf, and `pykt-toolkit`
(MIT) already supplies knowledge tracing. **Tutor → measurement → evaluation is now MIT end to end**,
which is the first time this base can price an *evidence* deliverable without a licence caveat.

🔴 **What this tier does NOT cover, and it is the regulated half.** Every address above scores
**tutoring** — dialogue, hinting, diagnosis. **Nothing found scores grading.** The only grading-side
candidate measured, [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader), is
**non-commercial** (see `agents/top.md`). NA, EMEA and APAC statutes all bite hardest on
**assessment**, so the surface with the most regulatory exposure is the one with no open harness.
Tracked as **`Gap 431-C`**.

## 🔴 Dead addresses corrected this pass

Four addresses in common circulation do not resolve. Each has a live replacement:

| dead address | live replacement |
|---|---|
| `apereo/opencast` | [opencast/opencast](https://github.com/opencast/opencast) |
| `edx/openassessment` **and** `openedx/openassessment` | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) |
| `OpenEduCat/OpenEduCat` | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) |

## 🔴 `p384` — an address that resolves but has no tree

[`projectfedena/fedena`](https://github.com/projectfedena/fedena) is listed by a vendor comparison
article as an **Apache-2.0** student information system. It is neither confirmed nor refutable from
a resolution check alone, which is the point:

| check | result |
|---|---|
| `git ls-remote --heads` | 🟢 **resolves** — two refs: `master`, `projectfedena-patch-1` |
| `master/README`, `README.md`, `LICENSE`, `Gemfile`, `app` | 🔴 **404, all five** |

🔵 **`ls-remote` proves a ref, not a tree.** The base's verification method pairs resolution with a
first-hand payload read precisely so this case is caught: there is no readable tree here to carry a
licence, so the Apache-2.0 claim is recorded as **unsubstantiated — nothing read**, not as a
licence of any kind. Any address census built on resolution alone over-counts the supply.

**Still absent from the supply, and it did not change this pass:** no platform is both an **LMS and
a SIS** under a permissive licence. The shape is permissive *courseware*
([`inducer/relate`](https://github.com/inducer/relate),
[`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors)), one permissive *major LMS*
([OpenOLAT](https://github.com/OpenOLAT/OpenOLAT), Apache-2.0), and copyleft everywhere else —
Moodle GPL-3, Open edX AGPL-3, Canvas CE AGPL-3, openSIS GPL-2.0, OpenEduCat LGPL-3. **Pairing two
bases is the only route**; the single permissive LMS+SIS does not exist to be found, and a pitch
that assumes it will be found is a pitch with a hole in it.

🆕 `p386` **— the claim survives a search aimed straight at it, and gains a third route.** The
prescribed ERP/CRM leg (`open source platform education ERP CRM MIT Apache 2026`) returned **no
permissive education platform**, which is this shelf's claim holding up under test rather than for
want of looking. What it did return is three **permissive general ERP/CRM bases**, licence payloads
read first-hand: [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (🟢 **MIT**, 1,077 B,
default ref **`master`**, Laravel 13 + FilamentPHP 5 **with a plugin system**),
[krayin/laravel-crm](https://github.com/krayin/laravel-crm) (🟢 **MIT**, 1,078 B, default ref
**`2.2`**) and [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) (🟢 **Apache-2.0**,
11,906 B, default ref **`trunk`**). 🔵 So the pairing routes are now three, not two: copyleft
LMS + copyleft SIS, copyleft LMS + permissive courseware, or **copyleft LMS + a permissive ERP base
whose education modules you build**. The trade is written out on
[`verticals/solutions.md`](../verticals/solutions.md) — and none of the three bases ships an
education module, so the third route is a **build**, costed as one.

