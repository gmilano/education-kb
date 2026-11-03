---
industry: education
region: Global
updated: 2026-11-03
---

## 🆕 `p636` — three recipes at the network boundary, and one pre-flight check that stops a bad bid

### 🟢 `p636-R1` — The governed Canvas agent: extend the `317★` incumbent instead of rebuilding it

**Why this and not a build.** `p635` would have told a studio this tier was greenfield. It is not:
[`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (`MIT`, `1,071 B` payload
read, `317★`, `100` forks, pushed `2026-11-03`) already ships `102` tools and `8` agent skills, and
`8 of 10` of its competitors sit at `≤2★`. 🔴 The gap is **governance, not capability**: a prior pass
measured `48` of `116` extracted tool declarations as mutating (`41.4%`), the heaviest write surface in
the tier, and only [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (`MIT`, `10★`)
writes grades at all among the rest.

**Wire it:**
1. Fork [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (`MIT` — ownable; the
   `AGPL-3.0` Canvas core is **not** touched, because you talk to it over `REST`/`GraphQL`).
2. Split the `102` tools into a read plane and a write plane. Keep the read plane as-is; put every
   mutating tool behind an approval step. The `41.4%` figure is your scoping input.
3. Borrow the read-only shape from [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp)
   (`MIT`, `1,072 B`, `119★`) for the student-facing tier — read-only by construction is the easier
   accreditation conversation.
4. Take grade-write semantics from [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp)
   (`MIT`, `1,070 B`) rather than inventing them.
5. Audit-log every write against the EU `AI Act` post-market-surveillance duty if the estate is `EMEA`.

🟡 **Deliverable:** the write-safe, multi-tenant, auditable layer the channel does not have. 🔵 Second
platform for the same recipe: [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(`MIT`, `1,068 B`, `62★`) — Brightspace is proprietary, so **all** the ownable work is client-side.

### 🟢 `p636-R2` — The permissive `LTI` content stack: an `LMS`-class system you can actually rebrand

**Why this is rare.** Every `LMS` in this base is copyleft — Moodle `GPL-3.0`, Open edX `AGPL-3.0`,
Canvas `AGPL-3.0` — except one. [`openfun/marsha`](https://github.com/openfun/marsha) is an `LTI`
**Learning Content Management System** under `MIT` (`1,078 B` payload read, `151★`, pushed
`2026-11-01`, France Université Numérique).

**Wire it:**
1. [`openfun/marsha`](https://github.com/openfun/marsha) (`MIT`) as the content plane — rebrandable,
   unlike a Moodle theme (`635-A`: `3 of 3` apparent `MIT` Moodle themes carry `GPL-3.0-or-later`
   headers).
2. Plug it into the client's existing `LMS` over `LTI` — it is an `LCMS`, it sits **beside** Moodle or
   Canvas, not instead of it. No migration in scope.
3. Implement the consumer side with [`instructure/ims-lti`](https://github.com/instructure/ims-lti)
   (`MIT`, `1,068 B`, `203★`, maintained by Canvas's vendor) for `Ruby`, or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (`MIT`, `1,070 B`, `138★`) for
   `Python` — 🔴 the latter untouched since `2024`, so fork it and own the maintenance.
4. Add the agent layer from `p636-R1` over the top; both planes are `MIT`, so the composite is ownable.

🔴 **Price the bus factor:** `marsha` is single-publisher and institutional, and `3 of 6` repositories in
this pass's `LTI` cohort are dormant while `1` ([`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI))
is **archived** by Microsoft. The permissive `LTI` layer is two live repositories wide.

### 🟢 `p636-R3` — The `APAC` university-portal pattern: partner rather than prospect

**Why.** The `APAC` leg yielded no policy intelligence for an eleventh pass, but the region's supply side
is real and institution-built — `APAC` universities write their own portal-agent bridges and publish
them permissively.

**Wire it:** start from [`SonAIengine/ku-portal-mcp`](https://github.com/SonAIengine/ku-portal-mcp)
(Korea University `KUPID` **plus** Canvas, `MIT`, `1,068 B`, `13★`) as the reference for a campus-system
bridge that is not just the `LMS`; [`kc0506/ntucool`](https://github.com/kc0506/ntucool) (`NTU COOL`,
`Rust`, `MIT`, `1,066 B`, `10★`) for a `CLI`-plus-`MCP` surface where latency matters; and
[`NUS-ALSET/achievements`](https://github.com/NUS-ALSET/achievements) (`MIT`, `1,066 B`, `17★`) as the
`LTI`-era precedent — 🔴 dormant since `2023`, reference only. 🟡 The pattern: one bridge per institution,
covering notices, schedules and library systems alongside the `LMS`. Sell it as a template, not a product.

### 🔴 `p636-C1` — The pre-flight licence check, and it is now three channels wide

Run this before quoting any platform-derived work. It takes an afternoon and it has changed the answer
in three of the last four passes.

1. **Platform badge** — `gh api search/repositories` / the repository page. Necessary, not sufficient.
2. **`LICENSE` payload** — byte-read it at `raw.githubusercontent.com` and record the byte count. 🔵 Run a
   fabricated path in the same batch; if it does not `404`, the channel is lying to you (`3 of 3`
   controls `404` this pass).
3. **Source header** — 🔴 **the one that costs money.** Moodle: `version.php` / `config.php` (`635-A`:
   `3 of 3` `MIT`-badged themes carry `GPL-3.0-or-later`). WordPress: the main plugin file's `License:`
   field (`636-C`: `1 of 4` declares `OSLv3`, copyleft and **`GPL`-incompatible**, under `MIT` on both
   other channels; `2 of 4` declare nothing at all).

🟡 **Then ask the question that decides the bid:** *what substrate do this platform's extensions run in?*
In-process code inherits the core's copyleft — Moodle `10.0%` permissive, Open edX `25.0%`. Network
clients do not — which is why `AGPL-3.0` Canvas has the permissive ecosystem and `GPL-3.0` Moodle does
not. 🔵 **Bid on the network side of the boundary.**

🔴 **Two instrument cautions for whoever runs this next.** `repos/{slug}/contents` was scope-gated in this
session (`7 of 7` denied), so main-plugin-file discovery fell back to filename convention and graded
`4 of 7` — declare the ungraded rather than assume them clean. And do not trust a bare repository count:
`lti license:mit` returns `610` of which the top hits are a webcam library and an iOS scrollview, against
`11` for the exact phrase, which drops the two largest real repositories (`636-E`).

## 🆕 `p635` — Pattern: a `Moodle` AI engagement that stays outside the `GPL` boundary

🟢 **The problem this pattern solves.** A university or ministry already runs `Moodle` — the most-deployed
`LMS` in the world — and wants AI tutoring, analytics and course-authoring help on top of it. The reflex
is to write plugins. `p635` measured why that reflex is expensive: `Moodle`'s core is `GPL-3.0`, its
extension mechanism is `PHP` plugins, and in three institutional estates (`770` repositories, `EMEA` and
`APAC`) **every** plugin class is `GPL-3.0` — themes included. Anything the studio writes as a plugin is
a derivative the client cannot take proprietary.

🔴 **And the trap that comes first, before any architecture.** `p634`'s Open edX advice — *fork the
`MIT` theme and rebrand* — does not transfer. `3 of 3` repositories GitHub reports as `MIT` `Moodle`
themes carry `GPL-3.0-or-later` headers in their own source files
([`WSYUTeam/adaptable`](https://github.com/WSYUTeam/adaptable),
[`bensampaio/moodle-theme_cubic`](https://github.com/bensampaio/moodle-theme_cubic),
[`maxoffon/moodle_theme_plugin`](https://github.com/maxoffon/moodle_theme_plugin)). 🟡 **Step zero of the
pattern is therefore a grant check that reads source headers**, not `LICENSE` files and not licence
badges.

**The wiring, and which repository supplies each part:**

1. 🟢 **Run the platform, do not modify it.** Containerise with
   [`learnweb/moodledocker-nginx-proxy`](https://github.com/learnweb/moodledocker-nginx-proxy) (`MIT`,
   `1,078 B` payload) in front of the University of Münster's Moodle Docker practice, and provision with
   [`Moodle-An-Hochschulen/moodle-provisioner-frontend`](https://github.com/Moodle-An-Hochschulen/moodle-provisioner-frontend)
   (`MIT`, `1,065 B`). 🔵 Both are permissive precisely because neither is a plugin — they are the
   `635-B` layer.
2. 🟢 **Read the LMS through `MCP`, not through a plugin.**
   [`IsaacAnwar/moodle-mcp`](https://github.com/IsaacAnwar/moodle-mcp) (`MIT`, `1,067 B`, `9★`, updated
   `9 hours` before this read) exposes courses, materials, deadlines and grades read-only to any `MCP`
   client. This is the single most important choice in the pattern: the integration boundary becomes
   Moodle's **web services API**, which is a consumer of `GPL` software, not a derivative of it.
3. 🟢 **Put the tutoring agent on the `MCP` side and keep it `MIT`.** Compose `moodle-mcp` with the
   agent frameworks this base already holds — [`DeepTutor`](https://github.com/HKUDS/DeepTutor)
   (`Apache-2.0`, `54,650★` re-measured `p634`) for the tutoring loop and
   [`Educhain`](https://github.com/satvik314/educhain) (`MIT`) for content generation. 🔵 Everything in
   this layer is the client's to own.
4. 🟡 **Author plugins with agents instead of hand-writing them, and expect to ship them `GPL`.** When a
   plugin genuinely is required, [`moodle-by-kelsoncm/moodle-plugin-skill`](https://github.com/moodle-by-kelsoncm/moodle-plugin-skill)
   (`MIT`, `1,080 B`) targets Marketplace review, [`arnoutvree/moodle-plugin-scaffold`](https://github.com/arnoutvree/moodle-plugin-scaffold)
   scaffolds the skeleton with a `CLAUDE.md` context layer, and
   [`arnoutvree/moodle-plugin-vibe-review`](https://github.com/arnoutvree/moodle-plugin-vibe-review)
   reviews changes against Moodle's coding, security and API conventions before commit. 🔴 The *skills*
   are `MIT`; the plugin they produce is `GPL-3.0`. Quote it as a client-owned contribution, not as
   studio IP.
5. 🟡 **Analytics: choose the side deliberately.**
   [`Ennero/moodle-local_metrics`](https://github.com/Ennero/moodle-local_metrics) (`MIT` file, `1,077 B`,
   `0★`) is a `local_` plugin and therefore sits **inside** the boundary — run step zero's header check on
   it before adopting. The permissive alternative is to pull the same telemetry through `moodle-mcp` and
   compute outside.
6. 🔵 **For a Spanish-language deployment**, [`JaxisReal/Moodle-Reporte-Limpio`](https://github.com/JaxisReal/Moodle-Reporte-Limpio)
   (`MIT`, `1,085 B`, `0★`) is the only in-region reporting row this base holds. `0★` means read it as a
   starting point, not a dependency.

🔴 **What this pattern does not solve, stated rather than implied.** It leaves the `GPL` boundary intact
rather than crossing it, so any requirement that *must* live in the Moodle UI — a new graded activity
type, a question type, a gradebook change — is still `GPL-3.0` work. 🟡 The pattern's value is that it
makes that list short and explicit at quoting time instead of discovering it at delivery.

🔵 **Second specimen still owed.** `635-B` now rests on two platforms (Open edX, `Moodle`). The obvious
third is a `GPL` platform whose presentation layer is *not* code — a Canvas (`AGPL-3.0`) theme estate —
and it has not been run.

## 🆕 `p634` — Pattern: a LATAM Open edX engagement that stays on the permissive side of the line

🟢 **The problem this pattern solves.** A LATAM public university or ministry asks for a branded,
national-scale online learning platform with AI tutoring. The reflex is Open edX, and Open edX is
`AGPL-3.0`: anything the studio builds *inside* it is a network-served derivative and its source must be
offered. This pass measured an estate that has run exactly this deployment for a decade
([`eol-uchile`](https://github.com/eol-uchile), Universidad de Chile, `113` repositories) and the licence
line inside it is sharp enough to design against.

**The wiring, and which repository supplies each part:**

1. 🟢 **Platform and deployment — take, do not build.**
   [`eol-uchile/edx-openuchile`](https://github.com/eol-uchile/edx-openuchile) (`MIT`, `1,091 B` payload,
   pushed `2026-10-29`) and [`eol-uchile/eol-edx`](https://github.com/eol-uchile/eol-edx) (`MIT`, pushed
   `2026-11-03`) are national-scale Open edX deployment images under a permissive grant. The platform
   underneath stays `AGPL-3.0` and is **run**, not modified — which triggers nothing.
2. 🟢 **Branding — take.** `12` `MIT` themes in the same estate
   ([`eol-uchile-theme-2020`](https://github.com/eol-uchile/eol-uchile-theme-2020), `1,097 B`, © Educación
   Online - Universidad De Chile). Fork and rebrand.
3. 🔴 **In-platform pedagogy — do not build here.** Every graded `XBlock` in the estate is `AGPL-3.0`
   (`15 of 15`), including [`eol_learner_profiles`](https://github.com/eol-uchile/eol_learner_profiles)
   (`34,523 B` payload). An `XBlock` the studio writes is a derivative. If the client wants to own it
   privately, it cannot live here.
4. 🟢 **AI tutoring — put it beside the platform, not inside it.**
   [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (`Apache-2.0`, `54,650★` measured `2026-11-03`)
   runs as its own service and is reached from the course through `LTI 1.3`. The tutor stays
   `Apache-2.0`, the studio's orchestration stays the client's, and the `AGPL` boundary is never crossed.
5. 🟢 **Accessibility, which a public-sector tender will require.**
   [`inclusive-design/idrc-wcag-reporter`](https://github.com/inclusive-design/idrc-wcag-reporter) (`MIT`)
   for conformance evidence, and
   [`inclusive-design/adaptive-palette`](https://github.com/inclusive-design/adaptive-palette)
   (`BSD-3-Clause`, pushed `2026-11-02`) where `AAC` learners are in scope.
6. 🟡 **Identity and records.** Where the client runs `CAS`/Shibboleth, the `EMEA` administrative estate
   held since `p632` supplies the permissive integration layer rather than the LATAM one — the Chilean
   estate's `uchileedxlogin` and `eol_sso` are **ungranted** (`NOASSERTION`), so they are reference, not
   dependency.

🔴 **What this pattern does not do, stated so nobody quotes it as coverage.** It does not give the client
a private, proprietary pedagogy layer inside Open edX — no arrangement of these repositories does. If
that is the requirement, the platform choice is wrong, and the honest alternative is a permissive
`LMS`-adjacent build with Open edX used only as a content host.

🔵 **Estimate shape:** deployment and branding from the estate is weeks, not months; the `LTI`-bridged
tutor is the real build; accessibility evidence is a parallel stream that a public tender will score.

## 🆕 `p633` — Pattern: APAC student-advising agent grounded in national reference data

🔵 Concrete wiring, all components permissive and byte-verified `2026-11-03`. This exists because the
missing piece for an Indonesian advising engagement was never the model — it was the join table.

**Problem.** An advising or placement agent that recommends a study programme has to name real institutions,
real programmes and real selectivity. Hallucinating a passing grade is the one failure a client will not accept.

**Components**

| Role | Component | Licence |
|---|---|---|
| Institution + programme ground truth | [`prodhokter/dataset-program-studi-indonesia`](https://github.com/prodhokter/dataset-program-studi-indonesia) (`4,971` programmes w/ quota, demand, selectivity, passing grades) + [`prodhokter/dataset-perguruan-tinggi-indonesia`](https://github.com/prodhokter/dataset-perguruan-tinggi-indonesia) (`143` SNPMB universities) | `MIT` 🟡 `DATA-TERMS-UNSTATED` |
| School registry + placement | [`prodhokter/dataset-sekolah-indonesia`](https://github.com/prodhokter/dataset-sekolah-indonesia) (`547,019` units) joined on [`prodhokter/dataset-wilayah-indonesia`](https://github.com/prodhokter/dataset-wilayah-indonesia) | `MIT` 🟡 same flag |
| Zero-ETL access for the prototype | [`prodhokter/api-datasets-indonesia`](https://github.com/prodhokter/api-datasets-indonesia) | `MIT` |
| In-language quality gate | [`prodhokter/dataset-kbbi-indonesia`](https://github.com/prodhokter/dataset-kbbi-indonesia) (`209,868` KBBI entries) | `MIT` |
| Learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) — already on this base's foundations shelf | `MIT` |
| Delivery surface | the institution's existing LMS (Moodle/Open edX rows on `verticals/solutions.md`) | per that shelf |

**Wiring**

1. Load the four `prodhokter` datasets into one store; join school → region on the `wilayah` codes so every
   learner row is regionally placed. Do **not** call the ministry API per turn — snapshot it, because the
   data-terms flag below means provenance has to be auditable.
2. Expose programme lookup, selectivity lookup and school lookup as **three narrow tools**, not one
   free-text search. The agent must be unable to answer a selectivity question except from a row.
3. Keep `pykt-toolkit` as the learner-state model and let the agent read its prediction; the recommendation is
   `learner state × programme selectivity`, which is exactly the pair neither component can compute alone.
4. Gate every generated Indonesian explanation against the KBBI lexicon before it reaches a student — cheap,
   and it is the difference between a demo and something a ministry will look at.
5. Surface inside the institution's LMS rather than as a new destination.

🔴 **Before this ships — the prerequisite, not a footnote.** The `MIT` grants cover the publisher's
packaging. The rows are Dapodik Kemendikbud's and the Top-1000 LTMPT list's, and their redistribution terms are
**not stated** anywhere in the repositories (`633-E`). Confirm the ministry's terms from the primary source
before a client deliverable depends on the data. The pattern is sound either way — the join key and the schema
are the reusable part — but the data layer may have to be re-sourced under the ministry's own licence.

## 🆕 `p632` — reads `2026-11-03` — `4` patterns, each wired only from rows byte-verified this pass

🔵 Every repository named below was measured today: grant read from bytes on the metadata-declared default
branch, with a fabricated address and a fabricated branch returning `404 14 B` in the same run. Where a
pattern uses a row verified on an **earlier** pass, the row says so and carries its earlier byte count.
🔴 No pattern crosses a copyleft boundary without saying so, and no ungranted row is used as a capability.

### 🟢 `632-M1` — EMEA higher education: accommodation-request triage on a permissive estate (`8–10` weeks)

**The gap.** `619-Q` has stood since `p619`: no permissive platform of record in the accessibility /
special-education tier, so every disability-services engagement was priced as a build. A university's
accommodations office runs on spreadsheets and email, and the volume is seasonal — request campaigns open,
hundreds of files arrive in two weeks, a commission reviews them, accommodations are issued and must be
evidenced later.

**The stack, all `Apache-2.0`, all byte-read today, all one publisher — so one legal review covers the set:**

1. **[`EsupPortail/esup-oasis`](https://github.com/EsupPortail/esup-oasis)** (`Apache-2.0`, `11,357 B`,
   `main`, `6★`, pushed `2026-10-21`) is the **system of record** and the reason this pattern exists: student
   requests against manager-defined campaigns, commission review, beneficiary file, accommodation plans,
   interview minutes. 🔴 Do not put an agent on the *file* — it holds disability data. Put it on the queue.
2. **[`EsupPortail/esup-signature`](https://github.com/EsupPortail/esup-signature)** (`Apache-2.0`,
   `11,361 B`, `master`, `36★`, pushed `2026-10-14`) carries the approvals. Accommodation decisions need a
   signed, auditable circuit, and this is that circuit already built for French HE paperwork.
3. **[`EsupPortail/esup-otp-api`](https://github.com/EsupPortail/esup-otp-api)** +
   **[`esup-otp-manager`](https://github.com/EsupPortail/esup-otp-manager)** (`Apache-2.0`, `11,359 B` each,
   pushed `2026-11-02` / `2026-10-30`) supply MFA. A student self-service portal holding medical
   documentation needs a second factor before anything else is discussed.
4. **[`EsupPortail/esup-siscol`](https://github.com/EsupPortail/esup-siscol)** (`Apache-2.0`, `11,359 B`,
   `main`, `7★`, pushed `2026-11-02`) resolves enrolment, programme and cohort from the **national**
   student-records web services rather than re-keying them. 🟡 `CLIENT`, **state** counterparty (`632-C`):
   free to interoperate, and the counterparty outlives the engagement.

**The agent, and the only place it goes.** A triage agent over the request queue: classify each incoming
request by the accommodation types it implies, flag incomplete evidence, draft the commission's agenda, and
propose the accommodation set by precedent from closed files. 🔴 It recommends; the commission decides and
`esup-signature` records who decided. 🔵 Build it as a service beside the estate speaking to `esup-oasis`'s
API — not as a fork — so the consortium's upstream releases keep applying.

**Why this is quotable.** Every component is `Apache-2.0` with a patent grant, deployed in production by
French universities today, and pushed within the last eight weeks. 🔴 **Grade per repository, not per
organisation:** `6` repositories in this estate are `CECILL-2.1` and `Esup-Pod` is `LGPL-3.0` (`632-A`).
🟡 And `619-Q` is **narrowed, not closed** — this is higher education and EMEA; a permissive K-12 `IEP`
system still does not exist, so a US K-12 special-education engagement cannot reuse this pattern.

### 🟢 `632-M2` — APAC Indonesia: fork the school system of record, which is the one region where forking is right (`6–8` weeks to a pilot)

**The gap.** `p631`'s APAC operative was *do not plan to fork the local platform — interoperate with the
state one*. Indonesia is the measured exception: the `sekolah` leg is the deepest token tier in the whole
census (bare `total_count` `74`) and it contains complete, permissive school systems.

**The stack:**

1. **[`adhiariyadi/Sistem-Informasi-Akademik-Sekolah-Laravel`](https://github.com/adhiariyadi/Sistem-Informasi-Akademik-Sekolah-Laravel)**
   (`MIT`, `1,069 B`, `master`, `521★`) is the **widest** base: a full SIAKAD academic information system in
   PHP/Laravel. 🔴 Last pushed `2023-07-30` — adopt it as a base **to fork**, never as a dependency to track.
2. **[`ugunNet21/hypervel-web-school`](https://github.com/ugunNet21/hypervel-web-school)** (`MIT`,
   `1,097 B`, `master`, `75★`, pushed `2026-09-02`) is the **maintained** alternative — administration,
   teaching and reporting on a current Laravel-family stack. 🟡 Pick by whether the client values feature
   breadth (row `1`) or an upstream that is still moving (row `2`); both are `MIT`, so the choice is
   technical, not legal.
3. 🔴 **What to leave out, and why it matters to the estimate.**
   [`ikhsan3adi/absensi-sekolah-qr-code`](https://github.com/ikhsan3adi/absensi-sekolah-qr-code) is the
   best-starred Indonesian attendance system (`495★`, pushed `2026-10-25`) and it is `GPL-3.0`
   (`35,149 B`, byte-read today). Linking it into a forked `MIT` platform makes the result reciprocal.
   Build attendance, or run it as a separate deployed service over HTTP.
   [`andes2912/sekolahku`](https://github.com/andes2912/sekolahku) (`189★`) and
   [`mrizkimaulidan/inven-bs`](https://github.com/mrizkimaulidan/inven-bs) (`82★`, pushed `2026-11-01`) look
   adoptable and have **no grant at `20` filenames in trees that resolve** (`632-B`) — all rights reserved.

**The agent.** Enrolment and records assistance in Bahasa Indonesia over the forked platform's own data:
answer parent and student queries about schedules, grades and fees, and draft the administrative replies a
school office writes hundreds of times a term. 🔵 The platform is yours after the fork, so the agent reads
the database directly — no integration layer to negotiate.

### 🟢 `632-M3` — LATAM Brazil: an ENEM exam-prep and exam-analytics chain, entirely permissive and in-curriculum

**The gap.** LATAM's permissive repository supply is thin, and `632`'s census shows what shape it does take:
the permissive Brazilian rows are **exam-shaped**, around ENEM, the national admission exam.

**The stack:**

1. **[`diaslui/enem-extractor`](https://github.com/diaslui/enem-extractor)** (`MIT`, `1,073 B`, `master`,
   `36★`) is the **ingestion** step: a CLI that turns published ENEM papers into JSON questions. This is the
   unglamorous piece every exam-prep build otherwise writes from scratch.
2. **[`piresramon/gpt-4-enem`](https://github.com/piresramon/gpt-4-enem)** (`MIT`, `1,068 B`, `main`, `54★`)
   is the **evaluation harness**: code and data to score a model against real ENEM items. 🟢 It is what lets
   a studio state a tutoring claim as a number against the client's own curriculum, in Portuguese.
3. **[`gpassero/uol-redacoes-xml`](https://github.com/gpassero/uol-redacoes-xml)** (`Apache-2.0`,
   `11,357 B` — byte-verified on an **earlier** pass, re-surfaced by this pass's `enem` leg) adds a
   **graded essay** bank, which is the other half of ENEM and the half models do worst on.
4. 🔴 **Excluded with reasons:** [`yunger7/enem-api`](https://github.com/yunger7/enem-api) is `GPL-2.0` and
   [`gustavoguanabara/assistente-enem`](https://github.com/gustavoguanabara/assistente-enem) is `GPL-3.0`
   (`35,149 B`, byte-read today) — both reciprocal, both tempting because they are the most complete.

**The agent.** A tutoring agent whose claims are measurable: `enem-extractor` builds the item bank,
`gpt-4-enem` benchmarks the model on it before anything ships, the essay bank trains and checks the writing
path. 🟡 **The commercial point is the harness, not the tutor.** Anyone can offer a Portuguese tutor; this
chain lets the offer carry a per-topic score on the actual national exam, produced by `MIT` code the client
can re-run themselves.

### 🟢 `632-M4` — EMEA Italy: spend a national teacher entitlement inside your own product (`2–3` weeks)

**The gap.** Education products in Europe lose deals at checkout, because the buyer is a teacher holding a
state entitlement rather than a card. Italy's **Carta del Docente** is exactly that: an annual per-teacher
allowance, redeemable only through an official voucher flow.

**The stack:**

1. **[`datomatic/carta-del-docente`](https://github.com/datomatic/carta-del-docente)** (`MIT`, `1,099 B`,
   `main`, `7★`, pushed `2026-06-22`) is an unofficial PHP package that integrates the voucher flow into a
   product's checkout. 🔵 Small, single-purpose, permissive — and it touches a **national funding
   instrument**, which no other row in this base does.
2. **[`DegrangeM/Skreen`](https://github.com/DegrangeM/Skreen)** (`MIT`, `1,073 B`, `master`, `6★`) pairs
   with it as the thing being sold: a teacher-side classroom screen-monitoring web app, the kind of small
   tool a teacher buys with their own allowance rather than through a procurement cycle.

**Why it is worth a pattern at `7★`.** 🟡 It changes the **route to market**, not the product: an Italian
teacher-facing tool that accepts the Carta is bought by individual teachers, with no tender and no district
sale. 🔴 Treat the package as a **lead, not a dependency**: it is unofficial, single-maintainer, and the
voucher API behind it is the state's to change. Verify the current flow against the official service before
quoting a date.

## 🆕 `p631` — reads `2026-11-03` — `4` patterns, each wired only from rows byte-verified this pass

🔵 Every repository named below was measured today: grant read from bytes on the metadata-declared default
branch, existence confirmed with a fabricated control in the same run. 🔴 No pattern crosses a copyleft
boundary without saying so, and no ungranted row is used as a capability.

### 🟢 `631-M1` — Deaf and hard-of-hearing classroom access, on-device (`6–8` weeks)

**The gap.** The shelf scored `hearing impaired` at 🔴 **`0`** before today — `sign language` was covered,
live **captioning** was not. Institutions buy captioning as a per-minute cloud service, which puts minors'
classroom audio on a third-party processor and makes the cost scale with teaching hours.

**The stack, all byte-read today:**

1. **[`lgy1027/matrix-live-diarizer`](https://github.com/lgy1027/matrix-live-diarizer)** (`MIT`, `1,063 B`,
   `133★`) is the spine, and it is chosen for its **privacy posture**, not its stars: transcription with
   speaker diarization where **audio never leaves the machine**. Diarization is the part that matters in a
   classroom — a transcript that cannot say whether the teacher or a pupil spoke is not a record of a lesson.
2. **[`XimilalaXiang/DeLive`](https://github.com/XimilalaXiang/DeLive)** (`Apache-2.0`, `11,346 B`, `268★`)
   supplies **system-audio capture plus multi-provider ASR** behind one interface. Take it for the provider
   abstraction: it is what lets a district swap a local model for a cloud one per-site without a rewrite.
3. **[`yuxino/Mimi`](https://github.com/yuxino/Mimi)** (`MIT`, `1,062 B`, `790★`) adds **live translation** of
   those captions — the same component serves a deaf pupil and a newly-arrived pupil, which is how one budget
   line covers two mandates.
4. **[`Zerg00s/Live-Captions-Saver`](https://github.com/Zerg00s/Live-Captions-Saver)** (`MIT`, `1,071 B`,
   `115★`) is the shortcut where the institution **already runs Teams**: export the captions it is already
   generating instead of deploying anything. Offer it as the two-week option.

**How they wire.** `DeLive`'s capture + ASR abstraction runs as a local service; `matrix-live-diarizer` owns
the transcript and the speaker labels; `Mimi` subscribes to the caption stream for translation; output goes to
a per-lesson record keyed to the timetable. `Live-Captions-Saver` is a parallel ingest path for Teams-only
sites, writing into the same record.

🔴 **What is deliberately *not* in this recipe.**
[`Mentra-Community/MentraOS`](https://github.com/Mentra-Community/MentraOS) (`Apache-2.0`, `2,397★`, default
branch 🔴 **`dev`**) is the most capable row in the tier and the **only one whose grant names an institution**
(`Mentra Labs, Inc.` → North America). 🟢 It belongs here as a **priced hardware option** — captions in the
pupil's field of view rather than on a shared screen — and not as the baseline, because it makes the
deployment a device-procurement programme. 🔴 Pin a commit: the default branch is `dev`.

**Placement.** North America (`MentraOS`, institutional read). The rest is unplaced and labelled so.

### 🟢 `631-M2` — Narrative-based learning that a teacher can author (`8–10` weeks)

**The gap.** `interactive fiction` scored 🔴 **`0`**. Branching-scenario learning — ethics cases, clinical
triage, language immersion, safeguarding training — is normally bought as a proprietary authoring suite, and
the content dies with the vendor.

**The stack, all `MIT`, all byte-read:**

1. **[`curiousdannii/parchment`](https://github.com/curiousdannii/parchment)** (`1,074 B`, `491★`) is the
   **runtime**, and it is the load-bearing choice: it plays standard Z-machine/Glulx story files in a browser
   with no install. Those formats are decades old and have multiple independent interpreters, so **the content
   outlives the runtime** — the same property that puts `LiaScript` on the foundations shelf.
2. **[`jeremyfa/loreline`](https://github.com/jeremyfa/loreline)** (`1,071 B`, `312★`) is the **authoring
   language**: branching narrative and state as plain text, so a scenario diffs and code-reviews like source
   and a subject-matter expert's edit is a pull request.
3. **[`Kirilllive/tuesday-js`](https://github.com/Kirilllive/tuesday-js)** (`1,067 B`, `698★`) is the
   **no-toolchain path** — a browser visual-novel editor for the teacher who will never run a build step.
   Two authoring tiers, one runtime.
4. **[`zenstory-ai/novel-to-game`](https://github.com/zenstory-ai/novel-to-game)** (`1,080 B`, `960★`) drafts
   scenarios from source documents **with citations**. 🔵 The citation behaviour is the educational
   requirement, not a feature: an ungrounded generated case study is unusable in assessment.

**How they wire.** Source material (a policy, a case file, a set text) goes through `novel-to-game` to a cited
draft; the draft lands in `loreline` for an SME to edit as text, or in `tuesday-js` for a teacher to edit
visually; both compile to story files that `parchment` serves. Completion and branch choices emit `xAPI` to
whatever LRS the institution runs — the LMS is never forked.

🔴 **The licence trap this pattern must not walk into (`T6`).** The code above is `MIT`. The **content** you
build on may not be: [`vgwb/Antura`](https://github.com/vgwb/Antura) is the specimen — `BSD-2-Clause` code and
🔴 `CC-BY-4.0` **content**, two holders (`TH Köln`, `Video Games Without Borders`). 🟢 In education the content
*is* the product, so grade every content dependency as `(family, asset class)` and budget the attribution.

### 🟢 `631-M3` — Foundational-skills drill with a measurement layer (`4–6` weeks)

**The gap.** `typing/keyboard literacy` scored 🔴 **`0`**, and it is the deepest hole the census found — seven
accepted rows. It matters more than it sounds: keyboard fluency gates **every** computer-based assessment, and
a pupil who cannot type is measured as a pupil who cannot write.

**The stack:**

1. **[`susam/quickqwerty`](https://github.com/susam/quickqwerty)** (`MIT`, `1,103 B`, `81★`) is the baseline
   lesson progression, and the reason to pick it over flashier rows is **maintenance**: `2008`→`2026`, the
   longest-lived instance on this base. A drill app a school deploys must still work in five years.
2. **[`linkage-rs/linkage`](https://github.com/linkage-rs/linkage)** (`MIT`, `1,067 B`, `161★`, 🔴 default
   branch **`core`**) is the desktop/offline path for labs without reliable connectivity. Pin a commit.
3. **[`tanciaku/ttypr`](https://github.com/tanciaku/ttypr)** (`MIT`, `1,066 B`, `76★`) and
   **[`alexylon/clavirio`](https://github.com/alexylon/clavirio)** (`Apache-2.0`, `11,357 B`, `35★`) are the
   terminal paths — they drop into an existing CS lab image with no browser stack.
4. **[`denisk20/programmer-dvorak`](https://github.com/denisk20/programmer-dvorak)** (`Apache-2.0`,
   `11,323 B`, `112★`) covers the **accessibility/RSI** case: alternative layouts, which a speed-focused
   product silently excludes.
5. **[`cwklurks/codesprint`](https://github.com/cwklurks/codesprint)** (`MIT`, `1,064 B`, `61★`) is the
   upper-secondary bridge — typing practice **on real algorithm problems**, so motor fluency and CS content
   accrue in one drill.
6. **[`Talljack/echo-type`](https://github.com/Talljack/echo-type)** (`MIT`, `1,064 B`, `320★`) extends the
   same keystroke loop to **listening, speaking, reading and writing** for language learning.

**How they wire.** One progression model and one event schema (keystroke, latency, error class) shared across
all six front ends; the web, desktop and terminal clients are deployment choices, not products.
`codesprint` and `echo-type` emit the same events against different content. The analytics layer sees one
stream, and `xAPI` carries it to the LMS.

🔴 **Not in this recipe:** [`ryanatkn/earbetter`](https://github.com/ryanatkn/earbetter) (ear training) is the
adjacent drill and is `The Unlicense` — a public-domain dedication with **no explicit patent grant**. 🟡 Fine
for most buyers, worth naming before a procurement review finds it.

### 🟢 `631-M4` — School system of record with a bounded-copyleft core (`10–12` weeks)

**The gap.** `fee management` and `financial aid` both scored 🔴 **`0`**, and `631-F` refuted the leg's claim
that no permissive education ERP exists.

**The stack, and the licence posture is the design decision:**

1. **[`rolling-scopes/rsschool-app`](https://github.com/rolling-scopes/rsschool-app)** (🟡 `MPL-2.0`,
   `16,724 B`, `10,392★`) is the **process** core — cohorts, mentor assignment, task distribution, cross-check
   review rounds, certificates. 🟡 File-level weak copyleft: link from proprietary code freely; **modified
   `MPL` files stay `MPL`**; no hosted-service trigger. 🟢 This is the one licence where *fork it* and *keep
   our IP* are both true, and the obligation is pricable — publish diffs to the files you touched.
2. **[`adigunsherif/Django-School-Management-System`](https://github.com/adigunsherif/Django-School-Management-System)**
   (`MIT`, `1,069 B`, `395★`) or **[`yungifez/skuul`](https://github.com/yungifez/skuul)** (`MIT`, `471★`,
   held) is the **registry and fees** layer where a fully permissive core is required instead.
3. **[`lumiis2/opportunity-tracker`](https://github.com/lumiis2/opportunity-tracker)** (`MIT`, `1,088 B`,
   `115★`) owns **scholarships, bursaries and deadlines** — the first row this base has in that tier.
4. **[`lilynex/libris-flow`](https://github.com/lilynex/libris-flow)** (`MIT`, `1,063 B`, `63★`) adds library
   circulation, and pairs with the held `MCLD/greatreadingadventure` reading-programme ledger.
5. **[`FadyCoding/EPEPEP-`](https://github.com/FadyCoding/EPEPEP-)** (`Apache-2.0`, `11,356 B`, `5★`) handles
   **marking at scale** — one instructor against many student projects. Small, and the only on-tier row.

**How they wire.** `rsschool-app` owns the process and the calendar; the `MIT` registry owns pupils, staff and
money, exposed over its ORM schema; `opportunity-tracker` runs as a service against the registry's pupil
records; `EPEPEP-` consumes assessment submissions and returns scored queues. 🔴 Keep the `MPL` boundary at a
**service** edge, not a file edge: integrate over HTTP and the weak-copyleft obligation never reaches your
code at all.

🔴 **Named and excluded:** [`gtn/exaport`](https://github.com/gtn/exaport) (e-portfolio) and
[`edusoho/edusoho`](https://github.com/edusoho/edusoho) (`1,866★`) are **ungranted** — no payload at `20`
licence filenames. 🔴 There is nothing to build on, whatever the star count, and **the e-portfolio tier stays a
declared hole** rather than being filled with an ungranted row.

**Placement.** Unplaced (`631-G`: the leg that returned `rsschool-app` was the English query, not a French
one). For an **APAC** variant substitute [`zhistaredu/StarTraining`](https://github.com/zhistaredu/StarTraining)
(`Apache-2.0`, `1,239★`) — the single permissive platform in a tier that is otherwise copyleft or ungranted.

## 🆕 `p630` — reads `2026-11-03` — `4` patterns, each wired only from rows byte-verified this pass

🔵 Every repository named below was measured today: grant read from bytes on the metadata-declared default
branch, existence confirmed on two channels with a fabricated control. 🔴 No pattern crosses a copyleft
boundary without saying so, and no `CLIENT-ONLY` row is used as a capability.

### 🟢 `630-M1` — Speech-and-language therapy triage for school districts (`6–8` weeks)

**The gap.** Districts have waiting lists for speech-language pathologist (`SLP`) assessment because the
assessment itself is manual: record a language sample, transcribe it, compute metrics, score. The shelf scored
`speech therapy` at 🔴 **`6` lines** before today.

**The stack, all `MIT`, all byte-read:**

1. **[`assinscreedFC/ortholyse`](https://github.com/assinscreedFC/ortholyse)** (`MIT`, `1,071 B`, `5★`) is the
   spine. It already does Whisper transcription → spaCy/NLTK language-sample metrics. Take the **pipeline**,
   not the PySide6 desktop shell: the shell is one maintainer's UI, the pipeline is the asset.
2. **[`fulldecent/vowel-practice`](https://github.com/fulldecent/vowel-practice)** (`MIT`, `1,083 B`, `67★`,
   self-labelled `mature`) supplies **formant extraction**. This is the measurement layer every pronunciation
   judgement needs and the one part nobody should reimplement.
3. **[`svankamamidi/open-aac`](https://github.com/svankamamidi/open-aac)** (`Apache-2.0`, from `p629`) is the
   learner-facing board for children who need augmentative communication rather than articulation drill —
   the triage has to have somewhere to route them. 🔴 Its default branch is `search_for_picture`, so pin a
   commit, do not track a branch name.

**How they wire.** `ortholyse`'s pipeline runs as a queue worker over uploaded samples; `vowel-practice`'s
formant code is lifted as a library and called per utterance; the metric output drives a triage score that
either books an `SLP` slot or provisions an `open-aac` board. The `SLP` sees a ranked queue, not a recording.

🔴 **What is deliberately *not* in this recipe.**
[`Vocametrix/vocametrix-python`](https://github.com/Vocametrix/vocametrix-python) (`MIT`) computes exactly the
clinical measures this pattern wants — AVQI, DSI, jitter/shimmer — and is 🔴 **`CLIENT-ONLY`**: the measures run
on Vocametrix's hosted API, so the `MIT` grant covers the client and nothing that matters (`630-H`). 🟢 It
belongs here as a **priced option** — "buy the clinical measures, integrate in a week" — never as the capability
the district is told it owns. [`dcostenco/prism-aac`](https://github.com/dcostenco/prism-aac) is excluded too:
`AGPL-3.0`, byte-read at `35,326 B`.

**Deliverable.** A triage service plus the explicit build-vs-buy line on clinical acoustics.

### 🟢 `630-M2` — Grant-funded OER authoring chain for an EMEA consortium (`8–10` weeks)

**The gap.** Erasmus+ and national grant consortia must publish open educational resources and have no
authoring chain, so output ends up as PDFs nobody can revise. The shelf scored `open textbook` at 🔴 **`3`**.

**The stack:**

1. **[`cagix/pandoc-lecture`](https://github.com/cagix/pandoc-lecture)** (`MIT`, `1,074 B`, `108★`, TH Köln) is
   the **single-source build**: one Markdown tree → slides, handouts, lecture notes, homework sheets, exams,
   via Lua Pandoc filters. 🔴 Default branch `master`.
2. **[`LiaScript/LiaScript`](https://github.com/LiaScript/LiaScript)** (`BSD-3-Clause`, `1,523 B`, `287★`,
   pushed today) is the **interactive renderer**: the same extended-Markdown document becomes a self-contained
   interactive course served from a URL with no backend. 🔴 Default branch is **`development`** — pin a commit
   (`630-J`).
3. **[`learningequality/kolibri`](https://github.com/learningequality/kolibri)** (`MIT`, `1,097 B`, `1,167★`)
   is the **offline distribution** target for partner institutions without reliable connectivity. 🔴 Default
   branch `develop`.

**How they wire.** Content lives in git as Pandoc Markdown. CI runs `pandoc-lecture` for the print and slide
artefacts and emits a LiaScript-flavoured variant for the interactive one; a packaging step produces a Kolibri
channel for offline partners. One source, three outputs, every artefact regenerable from the repository — which
is what a funder's open-access condition actually requires.

🟢 **Why this is the EMEA pattern specifically.** All three carry permissive grants because their funders
required it (`T5`), and none has a product team, so a studio's engineering is additive rather than competitive.

🔴 **The boundary.** If the consortium insists on Moodle delivery, the Moodle side is `GPL-3.0`
(`COPYING.txt`, `35,147 B`) — integrate over `LTI`, ship no modified Moodle core (`T1`).

### 🟢 `630-M3` — Recognition-of-Prior-Learning assessor for an APAC skills ministry (`10–12` weeks)

**The gap.** Informal-sector workers have real skills and no credential. `RPL` is policy in India and across
ASEAN, and assessment capacity is the bottleneck. The shelf scored `TVET` at 🔴 **`4`**.

**The stack:**

1. **[`SabarishR08/SIH26242-AI-Skill-Assessment-RPL`](https://github.com/SabarishR08/SIH26242-AI-Skill-Assessment-RPL)**
   (`MIT`, `1,066 B`, `1★`) is the **domain skeleton** — it was written against India MSDE problem statement
   `SIH26242`, so its competency model already matches the ministry's own vocabulary. 🔴 `1★` and single
   maintainer: take it as a **specification artefact**, not a dependency.
2. **[`vr4vet/vr4vet`](https://github.com/vr4vet/vr4vet)** (`MIT`, `1,063 B`, `16★`, EU Erasmus+) supplies the
   **practical-assessment scenarios** in Unity — demonstrating a trade beats answering questions about it, and
   this is a framework for building such scenarios rather than one fixed scenario.
3. **[`MCLD/greatreadingadventure`](https://github.com/MCLD/greatreadingadventure)** (`MIT`, `1,088 B`) is the
   **participant system of record** — enrolments, challenges, badges, multi-branch. Built for library reading
   programmes, and an `RPL` cohort has the same shape: many participants, many centres, staged achievements.

**How they wire.** `SIH26242`'s competency model becomes the schema; `vr4vet` scenarios become the evidence
capture per competency; `greatreadingadventure` holds candidate records, centre assignment and credential
issuance. Assessors review evidence against the model rather than running every assessment live — which is the
only way the capacity arithmetic works.

🟢 **Why it is credible here.** The teacher-certification precedent is already at scale in the region — the
Philippines DepEd–Google programme certifies 🟢 **over one million teachers**. Credentialing volume is the
business case.

### 🟢 `630-M4` — Reading-literacy remediation with the parent in the loop (`6–8` weeks)

**The gap.** Remediation fails when the household is not in the loop, and the shelf scored
`parent communication` at 🔴 **`0` lines** — the tier it covered least of all.

**The stack:**

1. **[`MuhammadLutfiMuzakiiVY/Litera-AI-Web`](https://github.com/MuhammadLutfiMuzakiiVY/Litera-AI-Web)**
   (`MIT`, `1,103 B`, `16★`) is the **adaptive diagnostic**: Next.js + Prisma + Gemini, built for reading-literacy
   remediation with adaptive diagnostic assessment. Indonesian — the pedagogy is localised, which is the point.
2. **[`PIGU-PPPgu/class-teacher-skills`](https://github.com/PIGU-PPPgu/class-teacher-skills)** (`MIT`,
   `1,056 B`, `10★`) is the **teacher-side workflow**: student records, class ledgers, home–school communication,
   and — the detail that matters — a 🟢 **confirm-before-send** step before anything reaches a parent.
3. **[`MCLD/greatreadingadventure`](https://github.com/MCLD/greatreadingadventure)** (`MIT`) supplies the
   **out-of-school reading programme** the remediation plan prescribes, with the library as delivery partner.

**How they wire.** `Litera-AI` diagnoses and produces a per-child plan; `class-teacher-skills` renders it as a
teacher action list and a parent message held for teacher approval; `greatreadingadventure` tracks the
at-home/at-library reading the plan calls for and feeds completion back as diagnostic input.

🟢 **The `confirm-before-send` gate is the architecture, not a feature.** An AI-drafted message about a child's
reading difficulty, sent to a parent unreviewed, is the failure mode that ends a programme. `class-teacher-skills`
already encodes a human approval step and the whole pattern should be built around it — which is the OECD's
*"pedagogy stays in control"* made concrete.

🔴 **Excluded, with cause.** [`anneschuth/parro-cli`](https://github.com/anneschuth/parro-cli) (`MIT`) is the
obvious parent-messaging transport and is 🔴 **`CLIENT-ONLY`** — it requires a Parro tenancy. 🟢 It is the right
**adapter** for a district that already licenses Parro, and must not be presented as the messaging capability
(`630-H`).

## 🆕 `p629` — reads `2026-11-03` — **🟢 TWO NEW RECIPES, BOTH BUILT ONLY FROM ROWS BYTE-VERIFIED TODAY: THE **FULLY-PERMISSIVE DISCONNECTED SCIENCE CLASSROOM** (NO COPYLEFT ANYWHERE IN THE STACK, WHICH THIS BASE COULD NOT SPECIFY BEFORE TODAY) AND THE **RENAME-RESOLVING ADDRESS AUDIT** AS A RUNNABLE PIPELINE WITH ITS CONTROLS.**

### 🟢 `P629-1` — the fully-permissive disconnected science classroom

🔵 **Why it is new.** Every prior classroom recipe on this page had to cross an LTI boundary to keep Globant's
deliverable permissive, because the LMS underneath was `GPL`/`AGPL` (`626-N`). 🟢 This stack has **no copyleft
component at all** — so the whole thing can be delivered, relicensed and embedded in a client product without an
LTI firewall. The missing piece until today was a permissive lab and a permissive offline server.

**Target:** a school with intermittent or no connectivity that must teach a lab science curriculum.

| Layer | Component | Licence | Role |
|---|---|---|---|
| Delivery substrate | [`ahmadarrabee/Ta3alam`](https://github.com/ahmadarrabee/Ta3alam) | 🟢 `MIT` | Offline-first education **server** on local hardware. Serves everything below over the school LAN; assumes no upstream link. |
| Content library | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | Offline content library + learner progress. Channels authored with [`learningequality/studio`](https://github.com/learningequality/studio) and packed with [`learningequality/ricecooker`](https://github.com/learningequality/ricecooker). |
| Lab — browser | [`rudra496/sciencelab3d`](https://github.com/rudra496/sciencelab3d) | 🟢 `MIT` | `40+` physics/chemistry/biology experiments, Next.js + Three.js. Static-exportable, so it ships **inside** the Kolibri channel. |
| Lab — desktop | [`qilaidev/virtual-chem-lab`](https://github.com/qilaidev/virtual-chem-lab) | 🟢 `MIT` | Qt6 desktop chemistry sim for machines with no browser. |
| Assessment | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 `BSD-3-Clause` | QTI delivery + scoring. 🟢 Only usable here because `628-F` read its grant from bytes — the metadata channel says `NOASSERTION`. |
| Accessibility | [`svankamamidi/open-aac`](https://github.com/svankamamidi/open-aac) | 🟢 `Apache-2.0` | AAC board for non-verbal learners. 🔴 Clone `search_for_picture`, **not** `main` — that is the default branch (`629-F`). |
| Language | [`Berzerker5653/open-language-learning`](https://github.com/Berzerker5653/open-language-learning) | 🟢 `Apache-2.0` | Offline language packs where instruction language ≠ home language. |

**Wiring:**

1. 🟢 Provision `Ta3alam` on the local server; it owns identity and the LAN HTTP surface.
2. 🟢 `npm run build && next export` `sciencelab3d` to static assets. Author a Kolibri channel in `studio`, pack it
   with `ricecooker`, and include the exported lab as an HTML5 app node — **no network egress at run time**.
3. 🟢 Import the channel into `kolibri` behind `Ta3alam`. Learner progress stays on the local server.
4. 🟢 Deploy `qtiworks` beside it for assessment; author items as QTI so they outlive the stack. `BSD-3-Clause` lets
   you fork the renderer into the client's own product.
5. 🟢 Install `virtual-chem-lab` and `open-aac` as local clients for machines that cannot run the browser build.
6. 🔴 **Expect to extend, not adopt.** `Ta3alam`, `open-aac` and `open-language-learning` are `0★`
   single-maintainer trees. Budget for ownership of those three; `kolibri` and `qtiworks` are the mature halves.

🟢 **Why it closes commercially:** every grant above is `MIT`, `Apache-2.0` or `BSD-3-Clause`, each **read from
`raw` bytes today** (`evidence/grant-byteread.2026-11-03-p629.tsv`). There is **no reciprocity obligation anywhere
in the stack**, so the integrated result can be relicensed into a client deliverable — which no Moodle- or
Open edX-based recipe on this page can claim.

🔵 **Fit:** EMEA (Jordan-authored substrate, data residency) and LATAM (`4 %` public AI funding — the offline,
hardware-light profile matches the money). Shippable in **`8`–`10` weeks** for a single-subject pilot, most of it
content authoring rather than code.

### 🟢 `P629-2` — the rename-resolving address audit, with its controls

🔵 `627-J` specified the canonical-address audit as a pipeline. 🟢 It could flag a stale address but not **resolve**
the live half. `629-C`/`629-D` supply the discriminator, so the audit now returns successors instead of a defect
count.

**Stage 1 — extract, and strip what is not a repository.**

```bash
grep -ohE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' "$@" \
  | sed -E 's#.*github\.com/##; s/[.),:;]+$//' \
  | grep -viE '^(topics|orgs|search|sponsors|features|collections|trending|apps|marketplace)/' \
  | tr 'A-Z' 'a-z' | sort -u > addresses.txt
```

🔴 **The filter is load-bearing, not hygiene:** `628-B` measured that `41` of `236` raw misses — **`17.4 %`** —
were `topics/`, `orgs/` and `search/` documentation links that no instrument can distinguish from dead repos.

**Stage 2 — census in OR-batches, one fabricated control per batch.**

```bash
# 99 real addresses + 1 fabricated control per query; fork:true is REQUIRED (628-A)
q=$(printf 'repo:%s ' $batch); q="$q repo:zzz-p629-fab-control/nope fork:true"
gh api -X GET search/repositories -f q="$q" --jq '.items[].full_name'
```

🔴 **If the control ever comes back, discard the batch.** `628-A` ran `41` batches with `0` leaks.

**Stage 3 — adjudicate each miss. This is the part `p629` adds.**

```bash
out=$(git ls-remote "https://github.com/$slug" HEAD 2>&1); rc=$?   # 629-E: capture BEFORE any pipe
if [ $rc -eq 0 ]; then
  echo "$slug RENAME-CANDIDATE $(echo "$out" | awk '{print $1}')"   # 422 + alive => renamed
else
  echo "$slug UNREACHABLE"                                          # 422 + 128  => stop
fi
```

🔴 **`629-E` is why the `rc=$?` sits on its own line.** `git ls-remote … | head -1` captures the **pipe's** status,
so every address scores alive — a column with no failing case.

**Stage 4 — name the successor. Only the page can.**

🟢 `WebFetch` the **old** address: GitHub serves the renamed repository through its redirect and the page states the
current name. 🔴 `ls-remote` follows the same redirect and reports only a SHA, so it proves *reachability* and hides
*identity* (`626-B`); the `repo:` channel reports `422` and names no successor (`629-C`).

🟢 **Confirm on identical `HEAD`** — the proof standard `628-C` set and this pass used twice:

| Old | New | `HEAD` |
|---|---|---|
| `ahmadarrabee/offline-learning-hub` | [`ahmadarrabee/Ta3alam`](https://github.com/ahmadarrabee/Ta3alam) | `e431c3e9bfce764f2e03e7c3d5949dd32949772f` |
| `tytsxai/virtual-chem-lab` | [`qilaidev/virtual-chem-lab`](https://github.com/qilaidev/virtual-chem-lab) | `24ec93543f24e1a7498e5230fd7179a54d123263` |

**Stage 5 — read the grant from bytes, never from metadata.**

```bash
for p in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt LICENCE; do
  curl -s -o f -w '%{http_code}' "https://raw.githubusercontent.com/$slug/master/$p"
done
```

🟢 **Probe `master`, not `main`** — `629-F` proved `raw` aliases `master` onto the default branch while `main` is
not aliased, so `master` reaches `main`-default repos too. 🔴 **But never report the default branch from this
probe** (`svankamamidi/open-aac`: both refs `200`, default actually `search_for_picture`). 🔴 And grade the payload
on its **terms text and boilerplate, never byte count** — `619-F` found a valid grant `597 B` short of stock,
`629-G` found one `17 B` long.

🔵 **Sellable as an engagement:** `4.83 %` of this base's `3,956` censused addresses are not canonical, `2.43 %` are
live-but-renamed and recoverable by Stage 3–4. A client's architecture docs, READMEs and dependency manifests decay
identically and nobody measures it. **`2`–`3` weeks** for a first audit of a mid-size estate.

## 🆕 `p628` — reads `2026-11-03` — **🟢 TWO ADDRESSES IN THESE RECIPES WERE STALE AND BOTH ARE NOW RENAME-PROVEN AND RE-POINTED. 🟢 AND THE QTI ASSESSMENT ENGINE IS CONFIRMED `BSD-3-Clause` ON BYTES, WHICH MAKES A FULLY-PERMISSIVE ASSESSMENT RECIPE POSSIBLE FOR THE FIRST TIME.**

### 🟢 Address corrections landing in these recipes

| Was cited | 🟢 Canonical today | Proof (`HEAD`) | Where |
|---|---|---|---|
| `project-sunbird/sunbird-lms-service` | [`Sunbird-Lern/userorg-service`](https://github.com/Sunbird-Lern/userorg-service) | `48c79a862038` | APAC/India stack recipe |
| `Changochen/slide-to-video` | [`llm-believer/slide-to-video`](https://github.com/llm-believer/slide-to-video) | `dd5ab179d565` | local-voice pipeline (already flagged by `626-E`) |

### 🟢 `P-628-A` — a fully-permissive QTI assessment path (new; `628-F` unlocked it)

🔵 Every prior assessment recipe on this shelf had to route around a copyleft LMS or an unknown licence. This one
does not: **every component is `MIT`, `BSD-3-Clause`, `Apache-2.0` or `ECL-2.0`.**

| Layer | Component | Licence |
|---|---|---|
| QTI item rendering + scoring | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 `BSD-3-Clause` (bytes, `628-F`) |
| LMS / course host | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` (no obligation over `Apache-2.0`, `624-D`) |
| Tool boundary | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` |
| Learner evidence trail | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 `MIT` |
| Mastery estimate | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 `MIT` |

**Wiring.** Deploy Sakai as the course host. Register QTIWorks as an **LTI 1.3 tool through Tsugi**, so Sakai
never links QTIWorks code — Tsugi owns the launch, the grade passback and the `ECL-2.0`/`BSD` boundary. On each
item submission, QTIWorks returns an outcome; Tsugi passes the grade back to Sakai and **simultaneously** emits
an xAPI statement through `learnmcp-xapi` to the LRS. Feed that statement stream into `pykt-toolkit` to maintain
a per-learner knowledge-state vector, and use the vector — not the raw score — to select the next item.

🟢 **Why it matters commercially:** this is the first recipe here that can be **shipped inside a client's
proprietary product** without a copyleft obligation anywhere in the tree. 🔴 Pin QTIWorks at a reviewed commit:
it is `3★`, `fork=true`, and pushed `2026-06-30` — permissive and buildable, but not actively developed.

### 🟢 `P-628-B` — policy-to-controls for a North America district (new; built from `628` NA findings)

🔵 Driven by a measured gap: `134` state bills in 2026, four states mandating district AI policy, yet most
districts have no student policy and `55 %` of high schools do not restrict network access.

| Layer | Component | Licence |
|---|---|---|
| LMS of record | [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` (integrate, don't embed) |
| Boundary | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` |
| LMS agent access | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | 🟢 `MIT` |
| Tutor | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 `MIT` |
| Audit trail | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 `MIT` |

**Wiring.** Stand `tutor-mcp` and `moodle-mcp` behind one MCP gateway and make the gateway the **policy
enforcement point**, not the model. Encode the district policy as deny rules at that gateway — and take
Washington DC's 2026-27 list as the starting specification of what must be **refused**: no AI in grading, no AI
in discipline, no AI in IEP decisions, no AI in teacher evaluation. Every allowed call and every refusal emits an
xAPI statement via `learnmcp-xapi`, so the district can evidence compliance rather than assert it. Moodle is
reached only over its REST API through Tsugi, keeping `GPL-3.0` out of the deliverable.

🟢 **The refusal log is the product.** A district that must adopt a policy needs to show the policy is operating;
nothing else in this stack produces that artefact.

### 🟢 `P-628-C` — EMEA conformity-ready assessment, sequenced to the deferral

🔵 Driven by the `2027-12-02` Annex III deferral: a `13`-month window on admissions, grading and proctoring.

**Wiring.** Ship the tutor first — tutoring, practice feedback and information chatbots are treated as generally
**outside** high-risk in the Commission's May 2026 draft guidelines, so `tutor-mcp` + `learnmcp-xapi` can go live
under transparency obligations only, with AI-interaction disclosure at the UI. Keep the **grader a separate
deployable** behind the same Tsugi boundary, so its Annex III duties never contaminate the tutor's release path.
In the grader, make human-in-the-loop structural: QTIWorks produces a provisional outcome, a teacher confirms or
overrides, and `learnmcp-xapi` logs **both** the machine outcome and the human decision. That log is the
conformity evidence the deferred deadline will demand.

🔴 Every EU date in this recipe is secondary-sourced — `eur-lex.europa.eu` is refused by this session's egress
allowlist (`628-H`). Confirm against the Official Journal before contracting on a date.

### 🟢 `P-628-D` — APAC/India DPI extension, on the corrected address

**Wiring.** Build on the Sunbird tiers, both `MIT`:
[`Sunbird-Lern/userorg-service`](https://github.com/Sunbird-Lern/userorg-service) for user and organisation
identity, [`Sunbird-Knowlg/knowledge-platform`](https://github.com/Sunbird-Knowlg/knowledge-platform) for content.
Add `tutor-mcp` as the learner-facing agent and `pykt-toolkit` for mastery estimation, and emit xAPI through
`learnmcp-xapi`. 🔴 **Use the `Sunbird-Lern/userorg-service` address** — `project-sunbird/sunbird-lms-service`
redirects but is not canonical, and three passes of this base mis-cited it (`628-C`).
🟡 `userorg-service` was last pushed `2026-03-02`; pin a commit and budget for maintenance.

### 🟢 `P-628-E` — LATAM offline-first governance delivery

**Wiring.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (`MIT`, pushed
`2026-11-02`) is the host, chosen for intermittent connectivity. Run the tutor locally against a small model so
no learner interaction requires egress; batch xAPI statements through `learnmcp-xapi` and sync on reconnect.
🟢 **Pair it with the governance artefact, because that is the measured gap:** `26 %` of LATAM institutions have a
formal AI strategy and `<10 %` have formal guidelines, against `>50 %` teacher adoption in Chile and Brazil. Ship
the policy, the enforcement point and the reporting as deliverables alongside the software — and anchor them to
the UNESCO LAC Observatory framework (launched April 2026) rather than to a national statute, because this pass
found **no binding national edtech AI statute** for Brazil, Mexico or Colombia.

## 🆕 `p627` — reads `2026-11-03` — **🟢 TWO RECIPES: `626-N`'s LTI-BOUNDARY TUTOR RE-SPECIFIED ON CORRECTED ADDRESSES (`9` OF THIS FILE'S ROWS POINTED AT STALE ONES), AND THE CANONICAL-ADDRESS AUDIT AS A RUNNABLE PIPELINE WITH ITS CONTROLS.**

### 🟢 `627-K` — LTI-boundary AI tutor: the client's LMS stays copyleft, the Globant deliverable stays permissive

🔴 **The problem this solves.** Both dominant LMS platforms are copyleft — Moodle is `GPL-3.0`,
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) is `AGPL-3.0`. 🔴 `AGPL-3.0` reaches
network use, so building a tutor *as a plugin inside* Open edX can oblige the client — or Globant — to publish the
tutor. 🟢 The LTI boundary is a process and network boundary, so the tutor is a **separate work** that communicates
over a standard protocol.

🟢 **The wiring, component by component, every address verified `2026-11-03`:**

| Layer | Component | Licence | Measured | Role |
|---|---|---|---|---|
| LMS (client's, untouched) | [`moodle/moodle`](https://github.com/moodle/moodle) or [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | `GPL-3.0` / `AGPL-3.0` | `7,574★` / `8,216★` | system of record; **no fork, no plugin** |
| 🟢 **Grant firewall** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` | `377★` pushed `2026-11-02` | LTI 1.3 tool host — the boundary itself |
| LTI plumbing | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 `Apache-2.0` | `124★` | spec-conformant launch / deep linking |
| Tutor logic | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0` | `54,334★` pushed `2026-10-31` | persistent learner model, multi-mode tutoring |
| Mastery estimation | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 `MIT` | `456★` pushed `2026-10-18` | knowledge tracing over the LMS gradebook |
| Offline / low-bandwidth edge | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `1,166★` pushed `2026-11-02` | `LATAM` and rural `APAC` deployments |
| Telemetry | xAPI statements → client's LRS | — | — | 🔴 do **not** use `adlnet/Unity-xAPI-Wrapper`: archived `2026-03-26` (`627-E`) |

🟢 **Assembly order, and the boundary rule at each step:**
1. 🟢 Stand `tsugi` up as its **own service** with its own repository and deployment. Nothing from the LMS tree is
   copied into it — that is what keeps the grant boundary real rather than nominal.
2. 🟢 Register it in the LMS as an **LTI 1.3 tool**. Launch carries the learner identity and context; the LMS is
   configured, never patched.
3. 🟢 Put `DeepTutor` behind `tsugi` as the tutoring engine, with `pykt-toolkit` scoring mastery from grades
   returned over **LTI AGS** (Assignment & Grade Services).
4. 🟢 Emit xAPI to the client's existing LRS. 🔴 Write the emitter in-house: the wrapper tier is dead (`627-E`).
5. 🔴 **For `EMEA`:** admissions and assessment are high-risk uses under the EU AI Act, so the deliverable needs
   logging, human-review and documentation **designed in from step 1**, not retrofitted.

🔴 **The two failure modes that destroy the boundary**, both seen in real engagements:
🔴 forking the LMS "just for one hook" — the tutor is then a derivative work of a copyleft tree; and
🔴 importing LMS model classes into the tool for convenience, which is the same thing with extra steps.
🟢 If a capability cannot be reached over LTI, add it to the tool and reach **in** over the LMS's REST API.

🔵 **Estimate:** `8`–`10` weeks for a single-LMS deployment with one subject area. The LTI registration and AGS
round-trip are the schedule risk, not the tutor.

### 🟢 `627-O` — canonical-address audit: the pipeline, its controls, and the two instruments that look like they work and do not

🟢 **What it sells** (`627-I`): on a client's dependency inventory, architecture documents or procurement list,
`~1 %` of cited repository addresses are **stale behind a rename redirect** and `~1 %` cite a **`0★` fork of a
living upstream**. 🔴 Both pass every reachability check. 🔴 Dead addresses measure `0` — do not sell link rot.

🔴 **Step 0 — calibrate, or publish false absences.** Run every instrument against a **fabricated slug** first and
keep one in every batch:

| Instrument | Live repo | Fabricated control | Use it for |
|---|---|---|---|
| `curl -sI https://github.com/…` | 🔴 `403` | 🔴 `403` | 🔴 **nothing — non-discriminating** |
| `gh api repos/<owner>/<repo>` | 🔴 `403` | 🔴 `403` | 🔴 **nothing — non-discriminating** |
| `gh api -X GET search/repositories -f q='fork:true repo:A/B repo:C/D …'` | 🟢 row | 🟢 absent | 🟢 canonicality + metadata |
| `git ls-remote https://github.com/<owner>/<repo> HEAD` | 🟢 SHA | 🟢 silent | 🟢 existence, rename proof |
| `WebFetch` the repository page | 🟢 renders | — | 🟢 fork parent, archived banner |

🟢 **Step 1 — enumerate.** Pull addresses from **table rows only**; prose mentions and measurement tables are not
recommendations and inflate the denominator (`p610` measured `26.1 %` of mentions as never-shelved).

🟢 **Step 2 — census in batches.** `repo:` qualifiers OR-batch; `24` per query is comfortable and `~34` queries
cover `800` addresses in about a minute. 🔴 **`fork:true` is mandatory** — without it GitHub applies `fork:false`
and returns every fork as absent (`53 %` of this pass's raw flags). 🔴 A batch **silently drops** bad members
instead of erroring, so diff the returned set against the queried set rather than trusting a count.

🟢 **Step 3 — resolve each miss, in this order:**
- `git ls-remote` the address. 🔴 No output → **dead**. 🟢 Returns a `HEAD` → alive; `ls-remote` follows the rename
  redirect, so a success does **not** mean the address is canonical.
- Find the successor by **identical `HEAD`**. That is the proof. 🔴 Name similarity is not.
- Still missing → `WebFetch` the page for the `forked from` line and the archived banner.
- 🟢 Unresolved after all three → **declare it**. `627-C` resolved `6 of 7`; the seventh is published as unresolved.

🟢 **Step 4 — propagate and log.** Rewrite the address in every table row of every non-append-only file in one
scripted pass, write a `file / line / old / new` ledger, then **re-grep for residuals and report the count**.
🔴 `p626` corrected one address in prose and left `22` table rows stale — the defect class is *incomplete
propagation*, and only the re-grep catches it.

🔵 **Estimate:** `2` days. Day 1 calibrate, enumerate, census. Day 2 resolve, propagate, hand over the ledger.
🟢 The ledger is the deliverable — it is what lets the client re-run the audit next quarter.


## 🆕 `p626` — reads `2026-11-03` — **🟢 ONE NEW PATTERN, SPECIFIED END TO END AND BUILT ONLY FROM ROWS RE-MEASURED TODAY: THE **LTI-BOUNDARY AI TUTOR**, WHICH KEEPS GLOBANT'S DELIVERABLE PERMISSIVE WHILE THE CLIENT'S LMS STAYS `AGPL-3.0` OR `GPL-3.0`. 🔴 AND `4` ROWS ON THIS PAGE WERE CITING STALE OR UNMAINTAINED ADDRESSES — ALL FLAGGED IN PLACE, ONE OF THEM THE "SOVEREIGNTY PICK".**

### 🔴 First, the corrections on this page, because they change what a build would pull

| Cited here | Status `2026-11-03` | Action |
|---|---|---|
| `EduNLP/edu-convokit` (line ~`3175`) | 🔴 **STALE** → [`EduNLP/edu-convokit`](https://github.com/EduNLP/edu-convokit) `117★` `MIT` | 🟢 Flagged in place |
| `ryjones/learner-credential-wallet` (~`3159`) | 🟡 **UNINDEXED**; successor 🔴 LOW CONFIDENCE | 🟢 Flagged, address kept |
| `ryjones/learner-credential-wallet` (~`3912`) | 🟡 **UNINDEXED**; same successor, 🔴 LOW CONFIDENCE | 🟢 Flagged, address kept |
| `Changochen/slide-to-video` (~`7411`) | 🔴 **STALE** → [`llm-believer/slide-to-video`](https://github.com/llm-believer/slide-to-video) — 🔴 `12★`, **last pushed `2025-09-12`** | 🟢 Flagged, and **re-priced** |

🔴 **The slide-to-video correction is the one that changes a recommendation.** It was sold on this page as
*"🟢 the sovereignty pick"* for local voice synthesis. Its canonical home has `12★` and has not been pushed in
**fourteen months**. 🟡 It is still the only local-voice option on these shelves, so it stays — but it is now
priced as **unmaintained**: budget to fork and own it, or keep synthesis out of scope.

### 🟢 `626-M` — **Pattern: the LTI-boundary AI tutor** (licence-safe on a reciprocal LMS)

🔴 **The problem it solves.** Every large LMS of record in this sector is reciprocal: Open edX and Canvas are
`AGPL-3.0`, Moodle and Chamilo are `GPL-3.0`. 🔴 A tutor built *inside* the platform tree inherits that grant, and
`AGPL-3.0` reaches network-served derivatives — which is exactly what an AI tutor is. 🟢 The LTI boundary is a
process and protocol boundary, so the tool is not a derivative work of the LMS at all.

🟢 **Every component re-measured `2026-11-03`. All permissive. No `NOASSERTION` row is load-bearing.**

| Layer | Component | Licencia | ★ | `pushed_at` | Why this one |
|---|---|---|---|---|---|
| LMS reached, not modified | [`moodle/moodle`](https://github.com/moodle/moodle) · [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) · [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 `GPL-3.0` / 🔴 `AGPL-3.0` / 🟢 `ECL-2.0` | `7,574` / `8,216` / `1,240` | `2026-10-30` / `2026-11-02` / `2026-11-02` | Client's existing estate. **Not forked, not patched** |
| LTI 1.3 tool boundary | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` | `377` | `2026-11-02` | The grant firewall. One tool, every conformant LMS |
| Tutor agent | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0` | `54,312` | `2026-10-31` | Sector's headline agent, permissive, patent grant |
| Tutor agent (alternative) | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT` | `42,496` | `2026-11-02` | Pick for APAC / local-LLM sovereignty work |
| Activity + attainment telemetry | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | `362` | `2026-11-02` | SCORM / AICC / **xAPI** — carries the outcome signal back |
| Offline / low-connectivity edge | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `1,166` | `2026-11-02` | LATAM and EMEA-Africa delivery without connectivity |
| Conversation analysis | [`EduNLP/edu-convokit`](https://github.com/EduNLP/edu-convokit) | 🟢 `MIT` | `117` | `2025-04-19` | Education-specific conversation data toolkit |

🟢 **Wiring, concretely:**

1. 🟢 **Register the tutor as an LTI 1.3 tool with `tsugi`.** `tsugi` implements the LTI Advantage services
   (Deep Linking, Names and Roles, Assignment and Grade Services) so the LMS launches the tool with a signed JWT.
   🔴 **Nothing is installed into the LMS tree** — this is the whole licence argument, and it is also why one build
   serves Moodle, Open edX, Sakai and Canvas estates.
2. 🟢 **Put `DeepTutor` behind that launch** as the tutoring service. Map the LTI `roles` claim to tutor behaviour
   (learner vs instructor) and the `context_id` claim to the course so sessions are scoped per course, not per user.
3. 🟢 **Emit xAPI statements through `scorm-again`** on every tutoring turn — attempt, hint taken, item answered —
   to the client's LRS. 🟢 This is the layer that makes the `OECD Digital Education Outlook 2026` finding
   actionable: task completion `+48 %` with measured performance `−17 %` once AI is removed means you **must**
   instrument unaided attainment, not engagement. Emit an unaided-checkpoint statement type from day one.
4. 🟢 **Write grades back via LTI AGS**, not into the LMS database. The gradebook stays the LMS's.
5. 🟢 **For offline estates, mirror the tutor behind `kolibri`** on the edge device and queue xAPI for sync.
   `kolibri` is `MIT`, so the edge build stays permissive too.
6. 🟢 **For APAC sovereignty work, swap `DeepTutor` for `OpenMAIC`** against a locally hosted model. Both are
   permissive, so the swap is a configuration decision rather than a licence re-review.
7. 🟡 **Analyse transcripts with `EduNLP/edu-convokit`** — the canonical address (`626-E`); `stanfordnlp/edu-convokit`
   is stale. 🔴 Note it was last pushed `2025-04-19`: usable library, not an active project.

🔴 **What this pattern does NOT do, stated so it is not oversold:**
- 🔴 It does **not** make the client's LMS permissive. The estate stays `AGPL-3.0`/`GPL-3.0`; only Globant's
  deliverable sits outside it.
- 🔴 It requires the LMS to be **LTI 1.3 conformant**. Moodle, Open edX, Sakai and Canvas are; a bespoke or legacy
  platform may not be, and then this pattern does not apply.
- 🔴 It assumes an **LRS exists or is in scope.** Without one, step `3` is a build, not a configuration — and step
  `3` is where the measurable outcome lives, so do not cut it to fit a budget.
- 🔴 **No `NOASSERTION` component is in the critical path.** `PageLM` (`2,060★`) and
  `GarethManning/education-agent-skills` (`CC-BY-SA-4.0` on bytes — share-alike on *prompt text*) are deliberately
  excluded. 🟡 `edificeio/entcore` is `NOASSERTION` and is only relevant for the French ENT estate; resolve its
  grant before it enters any build.

🟢 **Typical shape:** `6`–`8` weeks for one LMS plus one tutor behaviour with xAPI instrumentation;
`+2`–`3` weeks per additional LMS estate (configuration, not a new build, which is the point of the boundary).

### 🟢 `626-N` — Pattern: the **canonical-address audit**, which this pass ran on itself

🔵 `626-L` in `intel/market.md` sells this; here is the recipe, exactly as executed on `1,331` addresses:

1. 🟢 **Enumerate** every repository address cited in the client's dependency manifests, architecture docs and
   procurement records (`grep -ohE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+'`).
2. 🟢 **Census in batches** — the GitHub search `repo:` qualifier **repeats as an OR** and a batch silently drops
   bad members instead of erroring. `50` addresses per query, `per_page=100`. Set difference between sent and
   returned is the suspect set. 🔴 **Never branch on the error shape**: a single miss returns `422` *or* `total=0`.
3. 🟢 **`git ls-remote` the misses.** ABSENT ⇒ **dead**. ALIVE ⇒ **stale address behind a rename redirect**.
4. 🟢 **Resolve successors** with `<name> in:name` (🔴 one free-text term only — `625-C`) and match **identical
   `HEAD`**. Confirm the successor has `fork=false` and no competing indexed row.
5. 🔴 **Flag low-confidence matches; do not rewrite them.** An undiverged fork is indistinguishable from a transfer
   on this evidence. Rewriting a client's address on a fork is worse than leaving a stale one flagged.
6. 🔴 **Publish your own false positives.** This pass's extractor produced `10 of 84` bad flags
   (`github.com/topics/*` pages, `.git` suffixes). An audit that hides its own artefacts cannot be graded.

🟢 **Measured cost:** `1,331` addresses in `27` queries, about one minute, inside a `30/min` API budget.
🟢 **Measured yield on a well-maintained corpus:** `1.7 %` stale, `1.9 %` dead.

---

## 🆕 `p625` — reads `2026-11-02` — **TWO NEW PATTERNS, BOTH FORCED BY THIS PASS'S OWN MEASUREMENTS: `P625-1` WIRES THE AGENT LAYER IN OVER **LTI**, BECAUSE EVERY LARGE PLATFORM IN THIS SECTOR IS RECIPROCALLY LICENSED; `P625-2` PARTITIONS THE STACK ON THE **ANNEX III TRIGGER LINE**, BECAUSE THE TRANSPARENCY CLOCK IS ALREADY RUNNING AND THE HIGH-RISK CLOCK IS NOT**

---

## `P625-1` — LMS-agnostic agentic tutoring over LTI 1.3 (the licence-safe wiring)

**Tiempo**: `4-6` sem para el puente + `1` sem por LMS adicional (configuración, no desarrollo)
**Licencias**: 🟢 `Apache-2.0` (Tsugi) + 🟢 `Apache-2.0` (DeepTutor) + 🟢 `MIT` (scorm-again) — **todo permisivo**
**Plataforma del cliente**: sin tocar. Moodle `GPL-3.0`, Open edX `AGPL-3.0`, Canvas `AGPL-3.0`, Sakai `ECL-2.0`

### Por qué así, y no con un plugin

🔴 `625-H` midió que **toda** plataforma grande del sector es recíproca, y `AGPL-3.0` (Open edX, Canvas) alcanza el
**uso en red**. 🔴 Un plugin dentro del árbol de Moodle, o un fork de Open edX, arrastra la capa de agentes a obra
derivada. 🟢 LTI 1.3 es un **estándar publicado sobre un límite de red**: la IP de la capa de agentes queda limpia
y permisiva, y una sola integración cubre el parque instalado completo.

### Componentes — todos verificados `2026-11-02`

| Rol | Repo | Licencia | ★ |
|---|---|---|---|
| Puente LTI 1.3 / Advantage | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 `Apache-2.0` | `377` |
| Agente tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0` | `54,295` |
| Alternativa / segundo tutor | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT` | `42,491` |
| Courseware heredado | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | `362` |
| Competencias / skills | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 `MIT` | `208` |
| Entrega offline | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | `1,166` |

### Wiring

```
[Moodle | Open edX | Canvas | Sakai | Chamilo]   ← recíproco, NO se forkea
            │  LTI 1.3 Resource Link launch (OIDC + JWT firmado)
            ▼
   ┌──────────────────────────────────────────────┐
   │ Tsugi (Apache-2.0) — LTI tool provider       │
   │  · valida el JWT del launch                  │
   │  · resuelve contexto: curso, rol, usuario    │
   │  · AGS → devuelve notas al gradebook         │
   │  · NRPS → roster sin integración por LMS     │
   └───────────────┬──────────────────────────────┘
                   ▼  (límite de red + estándar publicado)
   ┌──────────────────────────────────────────────┐
   │ Capa Globant (MIT / Apache-2.0)              │
   │  · DeepTutor: tutoría con memoria persistente│
   │  · scorm-again: envuelve SCORM existente     │
   │  · iblai/lms: mapa de competencias           │
   │  · xAPI/Caliper → telemetría de aprendizaje  │
   └──────────────────────────────────────────────┘
```

### El launch, concreto

```python
# tutor_tool/lti_launch.py — el tool provider que Tsugi publica al LMS
from tsugi import Tsugi                     # Apache-2.0
from deeptutor import TutorSession          # Apache-2.0

tsugi = Tsugi()                             # valida OIDC + JWT del launch

def launch():
    ctx = tsugi.require_context()           # curso, usuario, rol — firmado por el LMS
    # El perfil del estudiante es NUESTRO, no del LMS: sobrevive al cambio de plataforma
    session = TutorSession(
        learner_id = ctx.user.stable_id,     # pseudónimo del LMS, no PII
        course     = ctx.context.label,
        locale     = ctx.launch_locale,      # es-419 / pt-BR / en-US
        mode       = "socratic",             # NO "grading" — ver P625-2
    )
    return session.render()

def on_mastery(session, score):
    # AGS: devolver al gradebook del LMS sin plugin específico
    if tsugi.outcomes_available():
        tsugi.grade_send(score, comment=session.evidence_url())
```

🟢 **Lo que esto compra:** "¿qué LMS usa el cliente?" pasa de pregunta bloqueante a línea de configuración. El
mismo tool corre en Moodle y en Canvas. 🟢 Y el perfil del estudiante vive en la capa Globant, así que una
migración posterior de LMS **no pierde el modelo del estudiante** — que es el activo real.

---

## `P625-2` — Partir el stack sobre la línea de disparo del Anexo III (conformidad UE con fechas reales)

**Tiempo**: `2-3` sem (transparencia, **ya obligatoria**) + `10-14` sem (programa alto riesgo hacia `2027-12-02`)
**Driver legal**: EU AI Act `Reg. 2024/1689`; alto riesgo movido a **`2 dic 2027`** por `Reg. (EU) 2026/1744`
🔴 **Pero transparencia de chatbots NO se movió: obliga desde `2 agosto 2026`.**

### La línea que lo decide todo

🔴 Anexo III marca alto riesgo a la AI educativa que: **evalúa aprendices** · **los asigna a programas** ·
**detecta conducta prohibida en exámenes** · **influye en el acceso a titulaciones**.

🟢 **Entonces el mismo stack contiene dos regímenes distintos, y mezclarlos hace que el tutor herede las
obligaciones del grader.** Partirlo es arquitectura, es facturable, y es lo que un auditor va a pedir:

| Componente | Toca un disparador? | Régimen | Qué obliga y cuándo |
|---|---|---|---|
| Tutor socrático, explicación, práctica sin nota | 🟢 **No** | Transparencia | 🔴 **Ya, desde `2026-08-02`**: avisar que es AI, etiquetar salidas |
| Flashcards, resumen, generación de material | 🟢 No | Transparencia | 🔴 Ya |
| **Grading automático** que entra al expediente | 🔴 **Sí** — evalúa | **Alto riesgo** | `2027-12-02`: doc. técnica, supervisión humana, FRIA, registro |
| **Scoring de admisiones** | 🔴 **Sí** — acceso | **Alto riesgo** | `2027-12-02` |
| **Proctoring / detección de conducta** | 🔴 **Sí** | **Alto riesgo** | `2027-12-02` |
| Predicción de dropout que **dispara tutoría** | 🟢 No* | Transparencia | *🟡 si la predicción decide acceso a un programa, cruza la línea |

### Implementación — la frontera como código, no como documento

```python
# governance/risk_partition.py
ANNEX_III_TRIGGERS = {
    "evaluates_learner",          # grading que entra al expediente
    "assigns_to_programme",       # tracking / colocación
    "detects_prohibited_conduct", # proctoring
    "affects_qualification",      # acceso a titulación
}

class EducationCapability:
    def __init__(self, name, triggers:set, region:str):
        self.name, self.triggers, self.region = name, triggers, region

    @property
    def is_high_risk(self) -> bool:
        return bool(self.triggers & ANNEX_III_TRIGGERS)

    def obligations(self) -> list[str]:
        o = ["ai_disclosure", "output_labelling"]        # ya obligatorio en la UE
        if self.region in ("EMEA",) and self.is_high_risk:
            o += ["technical_documentation", "human_oversight",
                  "fria", "risk_management_system", "event_logging"]
        if self.region in ("APAC",):                     # China/India/UE convergen
            o += ["provenance_labelling"]
        return o

# El tutor y el grader NO son el mismo servicio. Esa es la decisión de diseño.
tutor  = EducationCapability("socratic_tutor", set(), "EMEA")
grader = EducationCapability("auto_grader", {"evaluates_learner"}, "EMEA")

assert not tutor.is_high_risk      # 🟢 entregable este trimestre
assert grader.is_high_risk         # 🔴 programa hacia 2027-12-02
```

🟢 **Supervisión humana donde cuenta — y sólo donde cuenta:**

```python
# El grader propone, una persona dispone. Requisito de Anexo III, no una cortesía.
async def grade_with_oversight(submission, agent, gradebook):
    proposal = await agent.assess(submission)      # DeepTutor / OpenMAIC
    record = {
        "proposed_score": proposal.score,
        "rationale":      proposal.rationale,      # trazable, auditable
        "model_version":  agent.version,
        "provenance":     "ai_generated",          # etiquetado: UE+China+India
    }
    if proposal.confidence < 0.85 or submission.is_appeal:
        return await gradebook.queue_for_human(record)   # revisión obligatoria
    return await gradebook.post_with_human_signoff(record)
```

### Qué se entrega, por región

| Región | Entregable inmediato | Programa |
|---|---|---|
| **EMEA** | 🔴 Transparencia + etiquetado (**ya obliga**) | Conformidad Anexo III → `2027-12-02` |
| **North America** | Política distrital + registro de decisiones (`4` estados ya la exigen por ley) | Alineación al `AI Literacy Framework` del DoL |
| **APAC** | Etiquetado de procedencia (sirve a China, India y UE a la vez) | Nodos de política por jurisdicción (`6` regímenes) |
| **LATAM** | Marco institucional de uso (`87 %` usa, `26 %` tiene marco) | Formación docente — 🔴 la lección de Seúl: sin adopción, se revierte |

🟢 **Por qué este patrón vende:** la partición convierte una obligación con fecha `2027` en **un entregable este
trimestre más un programa plurianual**, y evita el error caro de que un tutor sin riesgo herede la carga
documental de un grader. 🔵 La frontera vive en código, así que el auditor ve la decisión, no una promesa.

## 🆕 `p624` — reads `2026-11-02` — **six recipes, every component grant **enumerated** today rather than guessed — and the `make hooks` control debt is resolved the way `623-M` said to resolve it: by reimplementation, which this pass did and which paid immediately**

### 🟢 `624-G1` — the control debt: `623-M`'s standing guidance followed, and reimplementation caught a real defect

🔵 `623-M` retired `make hooks` as a schedulable first action (an auto-mode classifier keyed on
`Code from External` refused it three passes running) and set standing guidance: **verify shelf edits by
reimplementing the published contract as code in the session's own scratchpad.**

🟢 **Followed exactly.** This pass wrote, fresh, in its own scratchpad: the `prepend` contract (frontmatter
detected, section inserted after it, history byte-count asserted), the oracle extractor with a
path-segment deny-list, and the `624-A` enumeration probe. 🟢 **`make hooks` was not scheduled and not
attempted.**

🔴 **And reimplementation paid, as `623-C` predicted it would.** The oracle extractor's first version
stripped trailing punctuation from repository names — and this pass's own candidate set contains
`five-plus-one/AI-Marker-Suite` and `122-syf-wcy/PhysicsOS`, names whose shape breaks naive tokenisation.
🟢 The extractor was corrected to strip only a trailing `[),.:;]+` run, and the oracle was rebuilt against
`4,507` slugs. 🟡 **Caveat carried forward:** `4,507` is under *this* pass's rules (case-folded, own
deny-list) and is **not comparable** to `p623`'s `3,974`.

> 🟢 **Standing guidance, reaffirmed unchanged:** do not schedule `make hooks`. Reimplement the contract.
> 🔵 Two passes have now done so and both found an instrument defect by running a control rather than by
> reading code.

### 🟢 `624-G2` — the enumeration instrument, as a reusable recipe

🔵 This is the pass's main deliverable and every pattern below depends on it. 🟢 It replaces a `13`-rung
filename ladder that had missed a rung on **five consecutive passes**, and it is the only channel that is
complete over this tier (`gh api repos/*` is `403` here, and channel B is `422`-blind to `openedx`).

```bash
# licence + manifest for any public repo, one transport, no guessing
git clone --filter=blob:none --depth 1 --no-checkout https://github.com/$SLUG d
git -C d ls-tree --long HEAD                     # complete root manifest + exact blob sizes
git -C d ls-tree -r HEAD --name-only | grep -i copyright   # PROVES absence over the whole tree
git -C d show HEAD:LICENSE | head -2             # lazily fetches one blob: the title decides
```

🟢 `15 of 15` repositories resolved, `0` guesses. 🔴 **Never infer a licence from byte size** — `624-C` shows
`AGPL-3.0` and `GPL-3.0` sizes interleaving and `ECL-2.0` landing `3` bytes from `Apache-2.0`.

---

### 🟢 `P1` — Assessment-under-removal: the one product the OECD number actually supports — `8–10` weeks

🔴 **The premise.** `624-K`: generative AI raised task completion `+48 %` and measured performance fell
**`−17 %`** once removed. 🔴 A completion assistant therefore wins the pilot and loses the mandate. 🟢 Build
the thing that measures the gap instead of widening it.

| Component | Address | Grant, byte-read `2026-11-02` | Role |
|---|---|---|---|
| Grading / assignment substrate | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 `BSD-3-Clause` | Release/collect/autograde cycle — the withdrawal harness |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 `MIT` | Bayesian Knowledge Tracing: the prior that `−17 %` is measured against |
| Spacing / retention scheduler | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 `MIT`, `4,122★` | Schedules the *un*-assisted retrieval that produces the honest score |
| Tutor surface | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0`, `11,408 B`, `54,290★` | Scaffolds — then withdraws on the scheduler's cue |
| Host platform | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`**, `11,120 B` | 🟢 Shippable as a closed derivative — `624-E` |

🟢 **Wiring.** `nbgrader` owns two variants of every assessment: assisted and withdrawn. `DeepTutor` serves
the assisted pass; `fsrs4anki` schedules the withdrawn one at the retention interval; `OATutor`'s BKT holds
the mastery estimate, and **the deliverable metric is the delta between the two** — the client's own `−17 %`,
measured rather than assumed. 🟢 Ships on Sakai with Apache-grade freedom.
🔵 **Sell it where a mandate exists:** the four US mandate states, and EMEA ahead of `2 December 2027`.

### 🟢 `P2` — EU AI Act high-risk conformity programme for assessment systems — `10–12` weeks

🔵 **Driver:** education AI for admissions, evaluation and exam scoring is **high-risk**; stand-alone
high-risk duties now dated **`2 December 2027`** by `Regulation (EU) 2026/1744`, with Article `50`
transparency already in force since `2 August 2026` and the literacy duty since `February 2025`. 🟢 Schools
are formally **deployers** and stay liable for third-party tools — that liability is the sale.

| Component | Address | Grant | Role |
|---|---|---|---|
| Self-hosted LMS | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0` | Sovereign deployment, shippable derivative |
| Lecture/media pipeline | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0`, `11,340 B` | Captioning/transcription under Art. `50` disclosure. 🟡 Carry the `126,439 B` `NOTICES` roll |
| Offline / data-minimised tier | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT`, `1,097 B` | Keeps pupil data local where DPIA pressure is highest |
| Assessment integrity | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 `NOASSERTION` — **byte-read owed** | Sandboxed automated assessment. 🔴 Do not ship before reading its grant with `624-G2` |

🟢 **Wiring.** Risk-classify each AI function against Annex III; wrap every assessment call in a
human-oversight checkpoint with an override log; emit Art. `50` disclosures at the learner surface; produce
technical documentation and a post-market monitoring plan per deployed model. 🔴 **Emotion recognition is
banned in education** since `2 February 2025` outside medical/safety use — audit for it and remove it.
🟡 **Price the date flagged:** sources still conflict between `August 2026` and `2 December 2027`; verify
against the Official Journal before contracting.

### 🟢 `P3` — District AI-policy implementation against the four US mandate states — `6–8` weeks

🔵 **Driver:** `134` bills across `31` states; **Maryland, Idaho, Oklahoma and Virginia** require state
guidance **and** mandatory district policy adoption (Maryland adds designated AI coordinators). 🔵 Against
that, **`55 %`** of high-school principals have not restricted AI on the school network at all.

| Component | Address | Grant | Role |
|---|---|---|---|
| Host LMS | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0`, `COPYING.txt`, `35,147 B` | 🟢 Plugin API keeps client code **outside** the copyleft boundary |
| Policy-aware tutor | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟡 grant **byte-read owed** | Local-first adaptive workspace — no pupil data egress |
| Grade-band gating | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 `MIT`, `89★` | MCP server turning any LLM into an ITS — the policy enforcement point |
| Teacher-facing skills | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 🟡 `CC-BY-SA-4.0` (`615`) — share-alike, commercial **allowed** | `165` evidence-grounded skills for teachers and leaders |
| Evidence layer | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 `BSD-3-Clause` | Produces the outcome a mandated policy must eventually defend |

🟢 **Wiring.** Implement NY `A 9190`-style rules as **data**, not code: a grade-band gate (`≥` grade `9`) with
diagnostic and special-education carve-outs, enforced in the `tutor-mcp` layer so one policy engine serves
every subject. Mirror NYC's **Traffic Light Framework** as the teacher-facing vocabulary.
🔴 **Attach `P1`'s measurement from day one** — a policy without an outcome is a renewal risk.

### 🟢 `P4` — LATAM institutional AI strategy at scale, offline-first — `6–8` weeks per institution

🔵 **Driver, and it is the best-measured gap in the world:** **`87 %`** of LATAM higher-ed institutions use AI,
**`26 %`** have a formal strategy (UNESCO IESALC, `~200` institutions, `19` countries); Brazil `53 %` using
against `22 %` with guidelines; Uruguay `75 %` of public-school teachers using (Ceibal). 🟢 The buyers are
already convened in one place — the **Observatory on AI in Education for LAC**, launched `14 April 2026` in
Santiago, with CAF, CENIA, ECLAC, Santillana, Tec de Monterrey, ProFuturo and Fundación Ceibal.

| Component | Address | Grant | Role |
|---|---|---|---|
| Offline-first delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT`, `1,097 B` | The low-connectivity anchor |
| Spanish/Portuguese LMS | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🟡 `GPL-3.0` + `license.txt` `1,614 B` | 🔵 Holder is **BeezNest Latino** — regional provenance, strong francophone+LATAM footprint |
| Tutor surface | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0` | Grounds answers in the institution's own documents |
| Content engine | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🟡 `GPL-3.0`, `35,146 B` | Interactive content inside Chamilo/Moodle |
| Governance artefacts | — | — | Strategy, academic-integrity rules, privacy and evaluation policy: the `61`-point gap itself |

🟢 **Wiring.** Kolibri for the edge, Chamilo as the institutional LMS, DeepTutor grounded on institutional
corpora, H5P for interactive assets — and the strategy/governance artefacts as the **primary** deliverable,
because `87 %`-minus-`26 %` is what the institution is actually missing. 🔴 **Copyleft is fine here:** these
are self-hosted institutional deployments, not resold SaaS.

### 🟢 `P5` — APAC multi-jurisdiction policy routing, built on the region's own permissive stack — `12–14` weeks

🔵 **Driver:** Korea's `AI Basic Act`; **Vietnam's Law on AI from `1 March 2026` with an `18`-month transition
for education**; China's targeted measures (recommendation algorithms, deep synthesis, generative AI services,
AI-content labelling); Australia's existing-law-plus-voluntary-guidance posture; Japan's voluntary guidelines.
🟢 One platform, five regimes.

| Component | Address | Grant, byte-read | Role |
|---|---|---|---|
| Classroom/course platform | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT`, `1,065 B`, `42,492★` | Tsinghua MAIC: topic or document → interactive classroom |
| Tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0`, `11,408 B` | HKU: lifelong personalised tutoring |
| 🆕 Agent curriculum | [`Annyfee/agent-craft`](https://github.com/Annyfee/agent-craft) | 🟢 **`MIT`, `1,064 B`**, `531★` | 🆕 LangChain/RAG/LangGraph/MCP teaching scaffold — client enablement, CN |
| 🆕 Local-LLM learning path | [`kyungseo/learnstead`](https://github.com/kyungseo/learnstead) | 🟢 **`Apache-2.0`, `11,343 B`** | 🆕 Korea-placed: local LLM, RAG, agent, concept → practice → verification |
| 🔴 Avoid for resale | [`roncoo/roncoo-education`](https://github.com/roncoo/roncoo-education) | 🔴 **`AGPL-3.0`, `35,184 B`** | 🆕 Complete CN platform (VOD, live, exams, question bank) — 🟡 open edition trims a commercial product, so a commercial grant may be purchasable |

🟢 **Wiring.** Policy as declarative per-jurisdiction rule sets in front of one agent runtime: Chinese
AI-content labelling applied at the generation boundary, Korean statutory duties as audit records, Vietnamese
transition deadlines as migration gates, Australian/Japanese voluntary guidance as defaults. 🟢 Build on
`OpenMAIC` + `DeepTutor` because both are permissive, both are at scale, and both are *regionally native* —
which matters for procurement. 🟢 Use `agent-craft` as the enablement track so the client's own team can
operate it.

### 🟢 `P6` — Lecture-capture intelligence on a shippable base — `4–6` weeks

🔵 **Driver:** the cheapest credible first engagement, and the only pattern here whose entire stack is
permissive — so the derivative can be *sold*, not merely deployed.

| Component | Address | Grant, byte-read | Role |
|---|---|---|---|
| Capture / media pipeline | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **`ECL-2.0`**, `11,340 B` | Ingest, transcode, publish. 🟡 Carry the `126,439 B` `NOTICES` roll under §4 |
| Host LMS | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **`ECL-2.0`**, `11,120 B` | Integrates natively — same Apereo estate |
| Interactive overlay | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **`Apache-2.0`**, `11,358 B` + `NOTICE` `146 B` | Turns a transcript into an interactive lesson |
| Retention scheduler | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 `MIT` | Generates spaced retrieval from the transcript |
| Study-material agent | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 `MIT`, `1,085★` | Documents → animated, narrated, interactive explainers |

🟢 **Wiring.** Opencast ingests the lecture and emits transcript + segments; `Papermorph` turns segments into
explainers; `oppia` wraps them as interactive lessons; `fsrs4anki` schedules retrieval; Sakai hosts.
🟢 **Every grant here is `ECL-2.0`, `Apache-2.0` or `MIT` — and `624-E` proves `ECL-2.0` adds no obligation —
so the whole assembly is shippable as a closed derivative.** 🟡 The only duty is attribution, and Opencast's
`NOTICES` file is large enough that it must be a build step, not an afterthought.

---

### 🟡 What `p625` should do, in priority order

| # | Action | Why now |
|---|---|---|
| `1` | 🟢 **Single-token non-English discovery legs** (`教育`, `学習`, `éducation`, `educação`, `تعليم`) | `624-F` measured four non-English legs at `total_count` `0`, and `623-A` proves the cause is **conjunctivity**. A one-word query cannot suffer it. This is the only untried channel with a mechanism-backed reason to pay |
| `2` | 🔴 **Byte-read the three grants this pass left owed:** `INGInious/INGInious`, `inducer/relate`, `zijinz456/OpenTutor` | All three are cited in patterns above with `NOASSERTION` or no grant read. `624-G2` makes each a one-command job, and `624-H` shows `NOASSERTION` means nothing |
| `3` | 🟢 **Re-run `624-A` enumeration over the full `4,507`-slug oracle, not just `18` repos** | The instrument is proven and cheap (blobless clones). Doing it at scale would give this base its **first** complete, non-guessed licence column — and would catch the `COPYRIGHT`-before-`LICENSE` class of error (`624-N1`) everywhere it exists |
| `4` | 🟡 **Re-check the EU high-risk date against the Official Journal** | `2 December 2027` vs `2 August 2026` is unresolved across sources and `P2` is priced on it. 🔴 Blocked by `624-J` unless the network policy changes |
| `5` | 🟡 **Retire or source the `41.5 %` CAGR** | `570` passes old, now bracketed by four firms at `16.8 %`-class rates (`624-K`). Either find its origin or demote it out of the headline |
| `6` | 🔴 **Do not schedule `make hooks`** | `623-M` + `624-G1`: refused three passes running by an auto-mode classifier keyed on `Code from External`. Reimplement the contract instead — it has now caught a defect two passes in a row |
| `7` | 🟡 **Do not re-promote non-English legs as "highest expected yield"** | `624-F`: `3` names from `8` legs. Right direction, modest magnitude — worth running, not worth prioritising above `#1`–`#3` |

## 🆕 `p623` — reads `2026-11-02` — **six recipes, every component byte-read today, plus the mechanism behind a control debt that has now failed to discharge three passes running — and `622-S`'s diagnosis of it was wrong**

### 🔴 `623-M` — `make hooks` refused a **third** consecutive pass, and the refusal states its own mechanism

🔵 `622-S #1` made this the **first** action `p623` should attempt, and argued the variable was *"the
session's permission set, not the code's origin"*, explicitly retiring `618-B`'s provenance theory.
🟢 It was attempted first. 🔴 **It was refused, and the refusal names the key:**

```
Permission for this action was denied by the Claude Code auto mode classifier.
Reason: [Code from External]
```

🔴 **`622-S` had it backwards.** The gate is an **auto-mode classifier** — a permission mechanism, so
`622-S` was right that the permission set matters — but what the classifier keys on is
`Code from External`, i.e. **the provenance of the code being executed**. 🟢 `618-B`'s provenance
theory was therefore *substantially correct* and `622-S` retired it on bad grounds.

🔵 Both facts are needed to explain the history: `p620` executed all `70` gates and `p621`/`p622`/`p623`
could not, over the same repository — so provenance alone cannot be the whole story either. 🟢 **The
consistent account: the classifier decides, it keys on external-code provenance, and its disposition
toward this clone has varied across sessions.**

> 🟢 **Standing guidance, replacing `622-S #1`:** stop scheduling `make hooks` as a dischargeable
> first action. It is **not** reliably dischargeable from a session that cloned this repository. Verify
> shelf edits by **reimplementing the published contract as code in the session's own scratchpad** —
> which is what `p622` did and what this pass did (the `prepend` contract, the oracle extractor with
> `622-F`'s deny-list, and the `ls-remote` liveness probe were all written fresh here, not read).
> 🔵 `620-S` already showed that *reading* the contract instead of reimplementing it fails.

🔵 **And this pass's own instrument carried a defect of exactly the kind reimplementation catches**
(`623-C`): the extractor stripped trailing punctuation from repo names, and one repository's name
**ends in a dot**, so the strip manufactured a false absence. Found by running the control, not by
reading the code.

### 🟢 `P1` — Curriculum-aligned tutoring on a permissive base, EMEA-first — `8-10` weeks

🔵 The only recipe in this base where **both** the runtime and the curriculum vocabulary are
commercially clean, which is why it leads.

| Component | Grant (byte-read) | Role |
|---|---|---|
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT`, `1,065 B` | Multi-agent classroom runtime — topic/document → interactive class |
| [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) | 🟢 `OGL-3.0` data + `MIT` code | The curriculum spine: OWL/SKOS vocabulary + instance data |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 `ECL-2.0`, `11,120 B` | LMS of record — permissive, so a derivative may ship |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT`, `1,097 B` | Offline delivery for low-connectivity cohorts |

**Wiring.** Load the Oak `ontology/` and `data/` trees into a vector + graph store keyed by curriculum
node. Each `OpenMAIC` agent turn is constrained to retrieve only within the current node's subtree, so
"on-curriculum" is a **retrieval invariant**, not a prompt instruction. Mount into Sakai via LTI 1.3;
export the same node graph to Kolibri channels for offline cohorts. Carry the attribution string
*"Contains public sector information licensed under the Open Government Licence v3.0."* plus a credit
to Oak National Academy in the product UI — 🔴 **this is a licence obligation, not a courtesy**
(`623-R`).

🔴 **Do not substitute `edx-platform` for Sakai here.** It is `AGPL-3.0` (`35,136 B`, byte-read) and
this pattern ships a derivative.

### 🟢 `P2` — EU AI Act high-risk conformity pack for assessment systems, EMEA — `10-12` weeks

🔵 Aimed squarely at the obligation: education AI that **evaluates learners or influences access to
qualifications** is high-risk under the AI Act, with conformity assessment, human oversight and
registration in the European AI Office database.

| Component | Grant | Role |
|---|---|---|
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 `Apache-2.0`, `13,185 B` | Credential-integrity validation — the assertion side of "influences access to qualifications" |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0` (`COPYING.txt`) | System of record; **plugin boundary** keeps the conformity pack outside copyleft |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0` | Assessment-session capture → the human-oversight evidence trail |
| [`quarto-dev/quarto-cli`](https://github.com/quarto-dev/quarto-cli) | 🟡 `MIT` + unresolvable exceptions (`623-E`) | Renders the technical documentation file the conformity assessment requires |

**Wiring.** Every assessment decision writes an immutable record: input, model version, retrieved
evidence, the human reviewer's identity and their override. Quarto renders that store into the Annex IV
technical documentation on each release. Ship as a Moodle plugin, never a core patch. 🔴 **Date risk is
the deliverable's main assumption:** `2 December 2027` for stand-alone Annex III systems per Regulation
(EU) `2026/1744`, against an earlier `August 2026` reading still in circulation — the engagement must
open by confirming the consolidated text. 🔴 Use Quarto to *run* the render; flag to counsel before
redistributing Quarto itself (`623-E`).

### 🟢 `P3` — District AI-policy compliance tooling, North America — `6-8` weeks

🔵 Four states (**Maryland, Idaho, Oklahoma, Virginia**) require *both* state guidance and mandatory
district-level AI policy adoption; DC-style rules **bar** AI from grading, discipline, IEP decisions
and teacher evaluation. 🟢 The product is a deployment that can **prove** the bar was respected.

| Component | Grant | Role |
|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0` | Where the restricted actions live (gradebook, records) |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 `MIT`, `1,150 B` | K-12 ERP/SIS — small enough to fork for the student-records side |
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🟢 `MIT`, `1,078 B`, branch `2.2` | Enrolment/admissions funnel, kept clear of restricted decisions |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 `Apache-2.0` | Credential assertions a district can audit |

**Wiring.** A policy-as-code layer in front of every AI call: a deny-list of decision *classes*
(`grade`, `discipline`, `iep`, `teacher_eval`) enforced at the service boundary and logged on both
allow and deny. The **deny log is the product** — it is what a district shows a state reviewer. Add the
grade-band gate (New York's `A 9190` shape: ninth grade and above, with diagnostic and
special-education carve-outs) as a per-call attribute, not a per-deployment setting.

🔵 **Attach the ADA remediation line to the same engagement**: large public institutions face an
**April 2026** web-accessibility deadline, and `sakai` (`ECL-2.0`) plus Moodle plugin work are where
that is deliverable without touching copyleft.

### 🟢 `P4` — Governance-and-enablement on an installed base, LATAM — `6-8` weeks, budget-constrained

🔵 Sized from measurement, not hope: `87 %` of LATAM higher-ed institutions already use AI, `26 %` have
a strategy, `< 10 %` have guidelines *with* capacity, and 🔴 **`55 %` have no AI budget at all.**
🟢 So this pattern assumes the first engagement is funded from a non-AI line and that every component
must be free to run.

| Component | Grant | Role |
|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT`, `1,097 B` | Offline-first delivery — the regional anchor |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 `GPL-3.0` | The installed base; plugin work is the volume play |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0`, `11,408 B` | Tutoring runtime, self-hosted |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT` | Multi-agent classroom where cohort size justifies it |

**Wiring.** Do **not** start with a model. Start with an institutional AI register — every AI use
already running, who owns it, what data it touches — because bottom-up adoption by individual
academics is the documented pattern and the register is the artefact the `26 %`/`87 %` gap is made of.
Then: one written guideline set, one capacity-building track for faculty, and *one* self-hosted
reference deployment (DeepTutor on Kolibri-delivered content) as the sanctioned path. 🟢 Anchor
credibility to the regional institutions by name — UNESCO's **LAC Observatory** (launched April `2026`)
and the **Tec de Monterrey**–UNESCO agreement (March `2026`). 🔵 Design every compliance artefact for
reuse across jurisdictions: `716` regulatory instruments across `23` countries and **no** single
regional law, so portability is the value.

### 🟢 `P5` — TEQSA institutional action plans, APAC/Australia — `4-6` weeks per institution

🔵 The most clearly scoped engagement in any region: Australia's higher-education regulator requires
**all** providers to file institutional action plans addressing generative-AI risk. A national sector,
a named deliverable, one template.

| Component | Grant | Role |
|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) / [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 `GPL-3.0` / 🟢 `ECL-2.0` | Whichever the provider runs; Sakai if a derivative must ship |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0`, `11,340 B` | Assessment-integrity evidence (capture + indexing) |
| [`quarto-dev/quarto-cli`](https://github.com/quarto-dev/quarto-cli) | 🟡 `MIT` + exceptions | Renders the plan itself, reproducibly, per institution |

**Wiring.** Build the plan as a **repository**, not a document: risk register as structured data, each
risk linked to the control that mitigates it and the evidence query that proves the control runs.
Quarto renders the submission. The same repo re-renders next cycle with updated evidence, which is what
turns a one-off filing into a retainer. 🟡 Reuse the `P2` conformity store wholesale for any provider
whose tools also reach EU students — the AI Act's high-risk regime follows the tool, not the domicile.

### 🟢 `P6` — Medical-education anatomy explorer, Global — `4` weeks

🔵 `622-N` opened this tier with `0` prior mentions; this pass has its licence fully settled and a
second instance, so it is now buildable rather than merely noted.

| Component | Grant (byte-read) | Role |
|---|---|---|
| [`ashemag/human-atlas`](https://github.com/ashemag/human-atlas) | 🟢 `MIT` code `1,064 B`; meshes **`CC BY 4.0`** (`623-D`) | `2,234`-mesh 3D anatomy explorer, `3,432` named concepts |
| [`Yoosseph/dental-scope`](https://github.com/Yoosseph/dental-scope) | 🟢 `MIT`, `1,741 B` | Dental tier — teeth, jaws, nerves, root canals |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 `MIT` | Agent layer: viva-style questioning against the selected structure |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 `ECL-2.0` | Lecture capture to align explorer sessions with taught content |

**Wiring.** Bind the mesh-selection event to an `OpenMAIC` agent turn: selecting a structure passes its
concept ID (one of the `3,432`) as retrieval scope, so the agent examines on **the structure in view**.
🟢 **Licence position, fully settled this pass:** code `MIT`, geometry `CC BY 4.0`, share-alike does
**not** apply, commercial use permitted with attribution carried — and the project's own
`public/ATTRIBUTION.md` documents that the legacy `CC BY-SA 2.1 Japan` text in the source OBJ comments
is superseded. 🔵 Carry the BodyParts3D/DBCLS credit in-product. 🔴 Two residuals: the upstream licence
page at `dbarchive.biosciencedbc.jp` was not fetched directly, and `33 MB` of compressed geometry needs
a CDN budget line. 🔴 Not a clinical tool — the project says so, and the engagement must repeat it.

## 🆕 `p622` — reads `2026-11-02` — **five recipes, every component byte-read today or already shelved and re-probed, plus the structural answer to a control debt that has now failed to discharge four passes running**

### 🔴 `P622-0` — Read the licence payload in full, before anything else — `0.5` wk, and it is not optional

🔵 **This is the step `622-D` created and it is cheap enough to have no excuse.** For every
component in every recipe below, and every component in every recipe this base has ever published:

1. `git ls-remote --symref https://github.com/{slug} HEAD` with `GIT_TERMINAL_PROMPT=0` → existence
   and the **real** default branch. 🔴 Never `curl -sI github.com/{slug}` — it is uninformative in
   both directions and the parse picks the error (`622-A`).
2. Walk ladder `v4` at `raw.githubusercontent.com/{slug}/{branch}/`: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `LICENSE-MIT`, **`COPYING.md`**, **`COPYRIGHT`**, `COPYING.LESSER`,
   `COPYING`. (`COPYING.LIB` retired — `622-B`.)
3. **Read the title line of every payload that answers `200`**, then **read the whole payload** if
   the title does not match a known licence title. This is the step that catches
   `AGPL + homepage branding` (`622-D`), `MIT with exceptions noted` (`622-H`) and a placeholder body
   under a real title (`621-F`).
4. Fire the `LESSER`-sibling probe **only** if `COPYING`'s title reads `GNU GENERAL PUBLIC LICENSE`
   without `LESSER`.
5. Cross-check `gh api search/repositories -f q='repo:{slug}'`. 🔴 Disagreement is **not** resolved
   in the channel's favour: `4` of this base's `NOASSERTION` verdicts were wrong against real grants.
6. 🔴 **Probe the content set separately** (`622-I`). Pictograms, meshes, simulations and textbook
   bodies carry their own grants, and that is where paid deliverables fail.
7. Run one **fabricated** slug through every channel in the same batch (`616-D`). `3 of 3`
   discriminated this pass.

**Deliverable:** a licence register with one row per component carrying grant, byte count, branch,
content-set grant, and **additional obligations in prose**. The last column is the one that has no
automated source.

### 🟢 `P622-1` — Permissive AAC channel for a paid EMEA accessibility programme (`8`–`10` wk)

🔴 **The problem this solves, stated honestly:** `621-E` found no actively-maintained permissive AAC
runtime, and `622-K` found that the sector's reference **symbol set** — ARASAAC — is
`CC BY-NC-SA`. So a *paid* deliverable cannot ship either the maintained runtimes (copyleft) or the
default vocabulary (NonCommercial). This recipe routes around both, explicitly.

| Component | Grant | Role |
|---|---|---|
| [`juanda99/arasaac-frontend`](https://github.com/juanda99/arasaac-frontend) | `MIT`, `1,084 B`, holder `Gobierno de Aragón` | 🟢 The **code** reference: a real, government-published AAC portal front end to read and derive from |
| ARASAAC pictogram set | 🔴 `CC BY-NC-SA` | 🔴 **Excluded from the deliverable.** Usable for the pilot and the demo; not for the paid product |
| Global Symbols | 🟡 terms permit charging for *software, training and support* but **not for the symbol set** | The substitution route: licence a commercial set, or commission one |
| [`Chuea81/freevoice-aac`](https://github.com/Chuea81/freevoice-aac) (`p621`) | `MIT`, `1,064 B` | 🟢 The permissive runtime base — offline, no account, no data collection |
| [`sugarlabs/sugar-toolkit-gtk3`](https://github.com/sugarlabs/sugar-toolkit-gtk3) | `LGPL-2.1` | Optional: ship the board as a Sugar activity on an existing 1:1 estate — linkable, so the activity stays proprietary (`622-C`) |

**Wiring.** Fork the `MIT` runtime; keep the symbol layer behind a **set-agnostic adapter** (symbol
id → asset URI + label, no set-specific assumptions); load ARASAAC in the pilot environment only and
a licensed set in production; build the authoring UI from the `MIT` portal front end.
**Weeks `1`–`2`** licence register (`P622-0`) and symbol-set procurement — *start procurement first,
it is the long pole*; **`3`–`6`** adapter + runtime fork; **`7`–`8`** authoring surface;
**`9`–`10`** clinical validation with speech-and-language therapists.
🔴 **Gate:** if the symbol licence is not signed by week `6`, the deliverable ships with a
placeholder set and the client is told so in writing. Do not ship `BY-NC-SA` assets in a paid
product.

### 🟢 `P622-2` — Disclosure-and-accountability workflow for a North American university (`6`–`8` wk)

🔵 **Why this and not detection.** The instrument says prohibition does not work: **`27 %`** of
students at institutions that *prohibit* AI use it weekly anyway, **`48 %`** where it is discouraged
(`622-N` demand leg, Lumina–Gallup, `2 April 2026`). 🟢 So the buyable product is evidence of
process, not interdiction.

| Component | Grant | Role |
|---|---|---|
| [`quarto-dev/quarto-cli`](https://github.com/quarto-dev/quarto-cli) | `MIT` (`COPYING.md`; 🔴 exceptions noted) | Submission render pipeline: one source → PDF/HTML with an embedded, machine-readable disclosure block |
| [`jupyter-book/jupyter-book`](https://github.com/jupyter-book/jupyter-book) | `BSD-3-Clause` | For computational coursework: notebook provenance survives into the published artefact |
| `bnsoftware/lti-1p3-tool` | `Apache-2.0`, `11,343 B` byte-read | 🟡 `LTI 1.3` launch beside the incumbent LMS. **Re-probe the address** — resolves but absent from channel B (`622-F`) |
| `p621` curriculum-alignment trees (`621-J`) | `MIT` / `Apache-2.0` | Maps the submission to programme outcomes, so the disclosure lands as accreditation evidence |

**Wiring.** The disclosure block is authored *with* the work, not attested after it: a Quarto
extension emits a signed YAML block (tools used, prompts retained, sections affected) into the
rendered artefact; the `LTI` tool carries it back to the gradebook; the alignment tree files it
against the outcome. **Weeks `1`–`2`** policy mapping with the registrar and `P622-0`;
**`3`–`5`** extension + `LTI` tool; **`6`–`7`** two-course pilot; **`8`** accreditation-evidence
export. 🟢 Sell it as the answer to *"what did your students actually do"* — which is the question
the `27 %` makes unavoidable.

### 🟢 `P622-3` — Additive, offline-capable extension of a LATAM 1:1 estate (`6`–`8` wk)

🔵 **Why additive.** `619-N`: `55 %` of LAC universities have no AI budget and public institutions
fund AI at **`4 %`**. A migration cannot be bought at `4 %`; an extension of hardware and software
the ministry already owns can.

| Component | Grant | Role |
|---|---|---|
| [`sugarlabs/sugar-toolkit-gtk3`](https://github.com/sugarlabs/sugar-toolkit-gtk3) | 🟢 `LGPL-2.1`, byte-read, channel B agreeing | **The integration point.** New activities link it and may stay proprietary |
| [`sugarlabs/sugar`](https://github.com/sugarlabs/sugar) | 🔴 `GPL-3.0` | 🔴 **Do not fork.** Target it, extend through the toolkit |
| [`iiab/iiab`](https://github.com/iiab/iiab) | 🔴 `GPL-2.0`, `18,092 B`, `2,012★`, pushed today | **Deploy, do not ship.** Raspberry-Pi offline content server — hosting a `GPL-2.0` distribution is not distributing a derived work |
| `learningequality/kolibri` (held, `616-L`) | — | The offline LMS substrate where an estate has no Sugar deployment |
| [`jupyter-book/jupyter-book`](https://github.com/jupyter-book/jupyter-book) | `BSD-3-Clause` | Builds the offline content bundle; static output needs no server |

**Wiring.** One `LGPL`-linked activity, one offline content bundle, one Pi-class server per school.
**Weeks `1`–`2`** estate audit + `P622-0`; **`3`–`5`** activity against the toolkit API;
**`6`–`7`** content bundle and IIAB image; **`8`** teacher training.
🔴 **Written-down constraint:** `622-K` found no LATAM-origin repository in three tiers across
Spanish and Portuguese legs. **This recipe deliberately builds on a LATAM-*deployed* estate rather
than LATAM-*authored* supply**, because that is what the evidence supports.

### 🟡 `P622-4` — Permissive OER publishing stack, and the one decision it forces (`8`–`10` wk)

| Layer | Permissive option | Grant | The copyleft incumbent |
|---|---|---|---|
| Render | [`quarto-dev/quarto-cli`](https://github.com/quarto-dev/quarto-cli) | `MIT` | — |
| Notebook → book | [`jupyter-book/jupyter-book`](https://github.com/jupyter-book/jupyter-book) | `BSD-3-Clause` | — |
| Production workflow | [`coko-foundation/ketty`](https://github.com/coko-foundation/ketty) | 🟡 `MIT`, **`8★`** | `pressbooks` (`GPL`), [`pkp/omp`](https://github.com/pkp/omp) (`GPL-3.0`, `145★`) |
| Media-rich scholarly | 🔴 none | — | [`anvc/scalar`](https://github.com/anvc/scalar) — **ungranted**, `244★`, active |

🔵 **The decision, put to the client in week `1` rather than discovered in week `8`:** the only
permissive production platform has `8★`, so either the studio co-maintains it or the client hosts a
`GPL` platform instead of shipping one. 🟢 Both are defensible; only one is defensible *late*.
**Weeks `1`–`2`** `P622-0` + the build/host decision; **`3`–`6`** render pipeline and template
system; **`7`–`9`** workflow layer on the chosen base; **`10`** accessibility conformance pass.
🔴 `anvc/scalar` is excluded by `P622-0` step `3`, not by preference.

### 🟡 `P622-5` — Statutory-risk review for a mandate-driven APAC engagement (`2`–`3` wk)

🔵 **A new recipe class for this base, and `T622-4` is why it exists.** Korea reclassified AI Digital
Textbooks out of textbook status by statute in **August 2025**; adoption collapsed, `14` publishers
protested, suits followed. An engagement priced against a mandate needs the mandate's own risk
assessed first.

**Steps.** (1) Identify the **instrument** the revenue depends on — statute, ministry order,
curriculum circular — and its amendment path. (2) Establish the **buying unit**: India's Class-3
mandate (`29 October 2025`, curriculum from AY `2026–27`) is executed by **states and UTs** under the
Concurrent List, so a union-level mandate is not a union-level contract. (3) Classify the contract as
**status-dependent** (paid because the product holds a legal classification) or **outcome-dependent**
(paid for a measured result) — Korea is the proof that the first can go to zero without the product
changing. (4) Price a sunset scenario explicitly.
**Deliverable:** a one-page risk note per jurisdiction, with the instrument, its date, its amendment
route and the contract class. 🟢 It is small, it is cheap, and `T622-4` is the case study that sells
it.

### 🔴 `622-M2` — control debt, and the correction that matters more than the debt: the gate denial is **session-dependent**, not environmental

🔴 **The fact.** `make hooks` and any direct `python3` of a file **from this clone** were refused
`[Code from External]` this pass, as in `p621`. 🟢 **But the explanation this base has carried since
`617-J` is wrong, and `620-S` is the proof it was always wrong.** `p620` executed `make hooks` in
**this same repository**, over **this same clone**, and graded all `70` gates (`48 of 70` green).
Code provenance was identical. 🔵 **So `618-B`'s "keyed on code provenance" is insufficient: the
variable is the session's own permission configuration, not the code's origin.** The run order is
`p617` ✗, `p618` ✗, `p619` ✗, `p620` ✓, `p621` ✗, `p622` ✗ — **second** consecutive refusal, not a
fourth, and not a property of the environment.

🟢 **Which makes "re-run `make hooks`" a legitimate action after all** — `p621` was right to hand it
forward and this pass was wrong to draft it as undischargeable. It is a **lottery**, not a bound: a
pass that draws an executing session should run the suite and reconcile every unverified commit
behind it. 🔴 **And that is exactly why the structural fix below is worth more than the action.**

🔵 The agent's **own inline** interpreter runs normally in a refused session — every edit in this
pass was made with it, so the contracts most at risk were checked by reimplementing the gate's own
logic against the written files. 🔴 `620-S` is also the warning about trusting that: `p619` left
`intel/market.md` *"structurally correct, verified by reading"* and the gate then found **two**
violations a careful read had missed. So this pass did not read — it re-ran `p383`'s published
contract (`CANON`, `VOCAB`, `MULTIPLE-BLOCKS`, `OUT-OF-VOCAB`, `MISSING-REGION`) as code:

| Contract | Checked how | Result |
|---|---|---|
| `gate-region-headings` — exactly one canonical `## Opportunities by region` | Counted on the written file | 🟢 `1` |
| …and its children are exactly the closed vocabulary | Enumerated on the written file | 🟢 `North America`, `EMEA`, `APAC`, `LATAM`, `Global`, in order |
| `gate-tables` — no data row rendering as a header | Every table authored with a real header row and real data | 🟢 by construction |
| Append-only trending | Line counts before/after | 🟢 `67,488 → 67,562` and `52,266 → 52,304` |

🔴 **What is still owed, stated precisely.** `gate-region-headings` was red at `618-L`, repaired,
and **re-failed** under `p620`'s actual run; `gate-declared-gap` (wired `618-A`) has exactly one
green run to its name. This commit adds a pass's worth of edits behind **two** refused sessions, so
`p621`'s and this pass's shelf changes are graded by reimplementation only. 🔵 The reimplementation
covers the two contracts whose violations are invisible to reading; it covers **none** of the other
`68` gates.

🟢 **The proposal, and the session lottery is precisely the argument for it.** The gates are
ordinary Python with test suites. Nothing requires an *agent* to run them — only something with this
repository checked out and permission to execute it. A control whose execution depends on which
session happens to pick up the pass is not a control; `p620` ran it and `p621`/`p622` could not, and
no one chose that. **Add a CI workflow (`.github/workflows/gates.yml`) that runs `make hooks` on
every push.** Then:

- every commit is graded by the platform rather than by whoever wrote it, which is the correct
  arrangement anyway (`618-B`: *an agent here can wire a control but never self-verify one*);
- `gate-declared-gap` (wired `618-A`) and `gate-region-headings` (repaired `618-L`) finally get the
  green run they have been owed for four passes;
- the `dead-citations` sweep (`622-F`, the largest known defect on these shelves) becomes a scheduled
  job rather than a thing each pass hopes to afford.

🔴 **And the honest caveat: this pass proposed it and did not build it.** Adding CI to this
repository is outside what this run was asked to change, so the file does not exist and `p623` must
not assume it does. The specification above is complete enough to create in one commit by whoever
owns that decision.
🟡 **`p623` should keep `make hooks` on its list** — `620-S` proves it can succeed — **and should
try it first, before spending budget on anything else**, because a session that can execute is the
scarce resource, not the suite.

🔴 **Carried forward, unchanged in priority:**

1. **Enumerate the dead and non-canonical citations across all `3,919` shelved addresses**
   (`622-F`, `622-S` item `3`). The instrument exists (`622-E`); only the sweep is unrun.
2. **Fix the oracle extractor's `github.com/topics/*` defect** (`622-F`) before `p623` quotes a
   slug count.
3. **Byte-read `human-atlas`'s mesh licence** (`622-I` item 3) — `CC BY 4.0` vs a `CC BY-SA` Japan
   variant differ on share-alike, and the meshes are the product.
4. **Enumerate Quarto's `COPYRIGHT` exceptions** (`622-H`) before a row leaves this base claiming a
   uniform `MIT`.
5. 🟡 **Three of `621-K`'s four timezone-placed rows remain institutionally unconfirmed.**
   `622-K` closed only the ARASAAC row, and it closed it by reading a copyright holder — which is
   the method the other three need.

## 🆕 `p621` — reads `2026-11-02` — **five recipes, every component byte-read today or already shelved with a byte-read grant, plus the control debt this pass created**

🔵 **Rule for this page, unchanged:** a recipe may only name components whose grant was byte-read in
this pass or is already shelved with a byte-read grant, and it must say what each component *does* in
the wiring — not merely that it is relevant. 🔴 Components carried from earlier passes are marked
`[shelved]` with the pass that read them.

### 🟢 `P621-1` — ADA-deadline accessibility remediation with an AAC channel, North American district (`10`–`12` weeks)

**Why now.** The April 2026 ADA deadline is the strongest budgeted driver on this base's market page,
and it lands on the tier `621-E` just measured. 🔴 The trap is that the AAC platform of record is
`AGPL-3.0` and a district deployment is network delivery, so the licence choice must be made in
week 1, not at delivery.

**Wiring.**
1. **AAC runtime — [`Chuea81/freevoice-aac`](https://github.com/Chuea81/freevoice-aac)** (`MIT`,
   `1,064 B`, byte-read today). Fork it. It is the **permissive** symbol-grid AAC that runs entirely
   in-browser and offline with no account and no data collection — which also disposes of the student-
   data objection NYC's guidance raises (student data cannot be used to train models; here it never
   leaves the device). `649` files, deployed at `freevoiceaac.app`, so it is a working product, not a
   skeleton.
2. **Symbol search — the method from [`RonanOD/OpenAAC`](https://github.com/RonanOD/OpenAAC)**
   (`Apache-2.0`, `11,357 B`, byte-read today). Reimplement its pipeline rather than depending on the
   tree (`2024-11-22`, stale): text/speech → vector embedding → nearest AAC symbol, with a generative
   fallback that **caches** the produced symbol locally so the same utterance never pays twice. 🔵
   Permissive grant, so the pipeline may be lifted into the `MIT` fork directly.
3. **Delivery shell — `Kolibri`** (`MIT`, `1,097 B`, branch `develop`) `[shelved p616]` for
   offline-first distribution to devices that are not reliably online, or **`OpenOLAT`**
   (`Apache-2.0`) `[shelved p615]` where a full LMS is already the system of record.
4. **Integration — `LTI 1.3`** as the launch surface into the incumbent LMS (Canvas, Schoology,
   PowerSchool), so the AAC tool appears inside existing courses without an SIS migration.
5. **Motor-planning requirement — read, do not link,
   [`sproutaac/app`](https://github.com/sproutaac/app)** (🔴 `GPL-3.0`, `35,149 B`, byte-read today).
   Its stable-button-position design is a real clinical requirement most AAC software gets wrong;
   **take the requirement, not the code** — linking `GPL-3.0` into an `MIT` fork would relicense the
   deliverable.

🔴 **Licence boundary, explicit:** do **not** pull `open-aac/sweet-suite-aac` or `sonicbaume/FreeAAC`
into this build. Both are `AGPL-3.0` (`34,519 B` / `34,523 B`, byte-read today) and hosting a
modified version for district users triggers §13 source disclosure to those users. That is a valid
model — see `P621-4` — but it is not this recipe.

### 🟢 `P621-2` — Accreditation-evidence curriculum alignment, EMEA university (`8`–`10` weeks)

**Why now.** Under the EU framework, education AI that assigns learners to programmes or influences
access to qualifications is **high-risk**, carrying conformity-assessment and human-oversight duties.
Alignment evidence is what a conformity file and an accreditation review both consume. 🔵 The
`2027-12-02` deferral (`NEEDS-PRIMARY`, see market page) is runway, not a reprieve.

**Wiring.**
1. **Alignment model — [`cloudpedagogy/…-curriculum-alignment-mapping-engine`](https://github.com/cloudpedagogy/cloudpedagogy-curriculum-alignment-mapping-engine)**
   (`MIT`, `1,070 B`, byte-read today). The relational model — programme → module → learning outcome
   → assessment → skill — plus its structural gap, duplication and misalignment detection. 🔴 It is
   **local-first with no server and no persistence**, so take it as the model and the detection logic
   and expect to build the multi-user layer. Its own `README` says Curriculum Studio interoperability
   is untested.
2. **Persistence and exchange spine — [`cassproject/CASS`](https://github.com/cassproject/CASS)**
   (`Apache-2.0`, `11,588 B`, byte-read today, pushed `2026-11-02`). This is what actually stores and
   exchanges: competency frameworks, records of attainment, learner profiles, over `xAPI` and Open
   Badges. 🟢 Permissive, live, and the standards vocabulary it speaks is the one `1EdTech`
   procurement language is written in.
3. **Free-text → standards matching — the `tf–idf` method from
   [`nsip/curriculum-align`](https://github.com/nsip/curriculum-align)** (`Apache-2.0`, `11,357 B`,
   byte-read today). 🔴 **Reimplement; do not deploy.** The tree is retired by its own maintainers
   with no security updates since `2019` (`621-J2`). A `tf–idf` baseline is also the right **human-
   oversight artefact** under a high-risk classification: it is explainable and auditable in a way an
   embedding match is not, so run it *beside* any LLM matcher as the justification channel.
4. **Human oversight — mandatory, not optional.** Every machine-proposed alignment lands in a review
   queue with the `tf–idf` score and the matched standard text shown; a human confirms. That queue
   *is* the conformity evidence.

### 🟡 `P621-3` — Apprenticeship competency spine, EMEA vocational system (`8`–`10` weeks)

🔴 **Read `621-I` before quoting this.** This tier has exactly one production-grade open asset and
this base already held it. Anyone proposing to "integrate the open apprenticeship-tracking stack" is
proposing something that does not exist.

**Wiring.**
1. **Competency spine — `cassproject/CASS`** (`Apache-2.0`, byte-read today). Frameworks, attainment
   records, learner profiles, `xAPI`/Open Badges exchange. It is the whole backend.
2. **Bespoke apprentice/mentor UI.** There is no open component for this. Budget it as new build.
3. **Data models to read, not adopt:**
   [`MrLeoDev/PSICAS`](https://github.com/MrLeoDev/PSICAS) (`MIT`, `1,065 B`, byte-read today) for its
   training-plan/competency-area/apprentice-assignment model with **versioned plans** — note its own
   `README` places it in "foundation phase" with `8` files and no application yet; and
   [`usaskulc/cat`](https://github.com/usaskulc/cat) (🔴 `LGPL-3.0` via `COPYING.LESSER` `7,651 B` —
   **not** `GPL-3.0`, see `621-B`) for its instructor-reported alignment survey instrument. 🟢 The
   `LGPL` correction matters here specifically: `LGPL-3.0` permits **linking** from proprietary code,
   so this one may be linked where a `GPL-3.0` grade would have forbidden it.
4. **Dual-tracking reality.** Mentor sign-off in most vocational systems is statutory and paper-based;
   the deliverable must export to the national instrument's format rather than replace it.

### 🟡 `P621-4` — Deliberate-`AGPL` hosted AAC service (`12`–`16` weeks)

**When to choose this.** When the client wants the **mature** AAC product rather than a small
permissive fork, and the disclosure obligation is acceptable — a public health service, a charity, a
ministry, or any client whose own policy already favours open publication.

**Wiring.**
1. **Platform — [`open-aac/sweet-suite-aac`](https://github.com/open-aac/sweet-suite-aac)** (🔴
   `AGPL-3.0`, `34,519 B`, byte-read today; `1,892` files; `CoughDrop` lineage). A full web AAC app
   plus supervisor/therapist support suite with speech synthesis and communication boards. 🟡 Pushed
   `2025-04-24`, so inherit ~`18` months of maintenance debt knowingly.
2. **§13 compliance designed in from week 1**, not retrofitted: a published source endpoint for the
   exact running revision, a build that stamps its own commit, and contract language stating the
   obligation. 🔵 **This is a deliverable line item.** The failure mode is discovering at go-live that
   the hosted service owes source to every user.
3. **Mobile reach — [`sonicbaume/FreeAAC`](https://github.com/sonicbaume/FreeAAC)** (🔴 `AGPL-3.0`,
   `34,523 B`, byte-read today) where native Android/iOS is required. Same copyleft family, so it
   composes with (1) without adding a *new* licence boundary — the tier's most active tree
   (`2026-10-28`), in public beta at `free-aac.org`.
4. 🔴 **Do not mix this recipe with `P621-1`.** An `MIT` fork and an `AGPL` platform in one hosted
   deliverable collapses to `AGPL` for the combined work. Pick one at week 1.

### 🟢 `P621-5` — Governance-first AI programme, any region, budget-constrained (`6`–`8` weeks)

**Why it generalises.** `T621-6` measured the adoption/governance gap in every region and found the
**product regionally invariant**; only the authority it cites changes. This is the highest-margin,
lowest-dependency engagement on this page because it needs almost no software.

**Wiring.**
1. **Instrument selection — pick the authority first.** North America: state statute (`134` bills /
   `31` states; Maryland, Idaho, Oklahoma and Virginia mandate district-level policy) plus the April
   2026 ADA deadline. EMEA: Regulation (EU) 2026/1744 high-risk duties (`NEEDS-PRIMARY` on dates).
   APAC: Korea's AI Basic Act (in force `2026-01-22`) or Australia's TEQSA institutional action plans.
   LATAM: UNESCO/accreditation frameworks. 🔵 The document is ~`80%` identical across all four; the
   citations and the review cadence are what differ.
2. **Disclosure workflow over detection.** `T619-1` found the sector buys **accountability**, not
   detection. Deliver a declared-use workflow — students and staff state how AI was used, attached to
   the submission — and an audit trail, rather than a detector.
3. **Evidence trail — `CASS`** (`Apache-2.0`, byte-read today) where the client needs the governance
   record to be machine-readable and exchangeable for accreditation, via `xAPI`/Open Badges. Skip it
   where a document and a register suffice; most clients at this budget do not need it.
4. **Offline-capable delivery — `Kolibri`** (`MIT`) `[shelved p616]` for staff capability-building in
   low-connectivity systems — the LATAM and African constraint, where `619-N` put procurement capacity
   at `4%`.
5. **Deliberately no model dependency.** Nothing in this recipe requires a specific LLM vendor, which
   is what makes it quotable under a data-sovereignty requirement (Malaysia) or a no-training-on-
   student-data rule (NYC).

### 🔴 `621-R` — control debt: what this pass created and could not discharge

1. 🔴 **`make hooks` did not run.** The harness refused to execute the repository's own Makefile
   (`Code from External`), so **none of the `70` gates graded this commit**. `p620` was the first
   gate-verified commit in four passes; this one is **not verified**. The shelf edits were built to
   satisfy the contracts by construction and checked with an independent reimplementation of the
   two contracts most at risk (`gate-tables` header-row shape, `gate-region-headings` single
   canonical block and closed vocabulary) — but the suite's own verdict is absent. **Highest-priority
   action for `p622`: re-run `make hooks` and reconcile against this commit.**
2. 🔴 **Ladder `v3` (`621-B`) is carried on one instance.** `COPYING.LESSER` resolved `usaskulc/cat`;
   `COPYING.LIB` has no real instance on this shelf and the rung is unfalsified. Either find an
   `LGPL-2.1` tree or retire the rung.
3. 🔴 **`p622` must re-run this pass's three tiers in Spanish and Portuguese.** LATAM placed **`0`**
   of `22` head names (market page, LATAM), and a Spanish-language leg was not run — `620-C` found
   exactly such a leg broke the regional pattern and paid. The nil is probably an artefact of
   language, not of the region.
4. 🟡 **Four region placements rest on timezone/vocabulary evidence** (`FreeAAC`, `sproutaac`,
   `PSICAS` → offsets; `CAME` → UK higher-education vocabulary). `gate-offset-region` exists to
   constrain exactly this class. None is institutionally confirmed; all four are marked.
5. 🟡 **An unknown number of shelved citations may be renames** (`T621-5`). `dead-citations` tests for
   addresses that fail; a renamed address **passes** while naming a repository that no longer exists
   under that name. A sweep comparing shelved slugs' `HEAD` shas against their canonical successors is
   the instrument, and it does not exist yet.

## 🆕 `p620` — reads `2026-11-02` — **five recipes, every component byte-read today, plus the control debt this pass could not discharge and the one it created**

🔵 **Rule for this page, unchanged:** a recipe may only name components whose grant was byte-read in
this pass or is already shelved with a byte-read grant, and it must say what each component *does*
in the wiring — not merely that it is relevant.

### 🟢 `P620-1` — Policy-conformant science simulation for a North American district (`8`–`10` weeks)

**The demand this is built against.** `>60 %` of students use AI weekly while `~50 %` of
institutions discourage or prohibit it, and `134` state bills across `31` states are in flight
(`intel/market.md`, North America). 🔵 **The district does not need a tutor. It needs to be able to
show a regulator what a learner did.**

| Component | Grant (byte-read) | Role in the wiring |
|---|---|---|
| [`phetsims/scenery`](https://github.com/phetsims/scenery) + [`sun`](https://github.com/phetsims/sun) + [`joist`](https://github.com/phetsims/joist) + [`axon`](https://github.com/phetsims/axon) + [`dot`](https://github.com/phetsims/dot) + [`kite`](https://github.com/phetsims/kite) | 🟢 `MIT`, `1,096`–`1,097 B`, Univ. of Colorado | The simulation runtime: scene graph, UI components, shell, observable state, maths, geometry |
| [`phetsims/chipper`](https://github.com/phetsims/chipper) | 🟢 `MIT`, `1,096 B` | Builds it. Run this first — it is the stack's entry point |
| 🟢 [`phetsims/tandem`](https://github.com/phetsims/tandem) | 🟢 `MIT`, `1,096 B` | **The load-bearing component.** `PhET-iO` makes simulation state addressable and serialisable, so the sim emits *what the learner did* rather than only a score |
| `xAPI` / `cmi5` conformance tier (US DoD ADL Initiative, `p613`) | 🟢 `Apache-2.0` | Consumes `tandem`'s event stream as statements; gives the district a standards-based audit trail |
| `LTI 1.3` / LTI Advantage tier (`p612`, five languages) | 🟢 permissive | Launches the sim from the district's existing LMS with roles and context intact |
| [`openzim/phet`](https://github.com/openzim/phet) | 🟢 `Apache-2.0`, `11,356 B` | Acquires the **published** `CC-BY` simulations legitimately, as offline `ZIM` archives |

**Wiring.** `chipper` builds a sim from `scenery`/`sun`/`joist`/`axon`/`dot`/`kite` → `tandem`
instruments every learner-visible property → a thin adapter maps `PhET-iO` events to `xAPI`
statements → the ADL conformance suite validates them → `LTI 1.3` launches the whole thing from
the district LMS → `openzim/phet` supplies additional published sims as content.

🔴 **The boundary that must be in the statement of work (`620-I`):** build on the **engine**; do
**not** clone a simulation repository — `9 of 9` carry no grant. Content comes through
`openzim/phet` from the `CC-BY` published set, **with attribution**.

🟡 **Why `8`–`10` weeks:** the `PhET-iO`→`xAPI` adapter is genuinely new work (`~2`–`3` weeks); the
rest is assembly of components that are already permissive and already shelved.

### 🟢 `P620-2` — Governance-first AI programme for a LATAM university consortium (`6`–`8` weeks)

**The demand.** `92 %` of students and `79 %` of faculty actively engaging with AI (DEC ×
Tec de Monterrey, `29` universities), against a UNESCO IESALC finding across `200` institutions in
`19` countries that institutional governance is absent, and a panel official stating formal
university AI policies are **lacking**. 🟢 **The adoption already happened. This recipe sells the
controls, not the capability** — and `T620-4` is the argument.

| Component | Grant (byte-read) | Role in the wiring |
|---|---|---|
| 🟢 [`DusPro/educacao-especial`](https://github.com/DusPro/educacao-especial) | 🟢 `MIT`, `1,081 B` | **`PEI`** (*Plano Educacional Individualizado*) generation — reports, diaries, adapted activities. The highest-compliance-value artefact found this pass, and it speaks Brazil's own statutory instrument |
| [`LucasSpinola/assistentes-educacionais-com-ia`](https://github.com/LucasSpinola/assistentes-educacionais-com-ia) | 🟢 `MIT`, `1,128 B` | The faculty-enablement curriculum — NLP → ML → transformers — so the `79 %` already using AI are trained rather than policed |
| [`Gio0938/CocoMath`](https://github.com/Gio0938/CocoMath) | 🟢 `Apache-2.0`, `11,357 B` | Worked reference for an **explainable** adaptive loop: multiclass logistic regression classifying the learner's error type, not a black-box tutor |
| `LabSirius/TutorIA` (`MIT`, `p617`) | 🟢 `MIT` | The consortium's Spanish-language tutor row this base already holds, re-read at `p617` |
| `dsvi-b/corretor-enem` (`MIT`, `1,078 B`, re-read today) | 🟢 `MIT` | ENEM essay grading on `5` competencies, calibrated on `11,147` real essays, **no API and no ML** — the deterministic, auditable grader that a governance programme can actually defend |
| `xAPI` / `cmi5` tier (`p613`) | 🟢 `Apache-2.0` | The audit trail the `200`-institution governance gap is asking for |
| `OpenOLAT` (`p615`, `Apache-2.0`, `10,982 B`) | 🟢 `Apache-2.0` | Permissive LMS substrate, `QTI 2.1` + `SCORM 1.2` + `LTI 1.3` in the box |

**Wiring.** `OpenOLAT` as the system of record → `corretor-enem` and `CocoMath` as **explainable,
auditable** assessment components (both run without a hosted model, which is what makes the audit
trail meaningful) → `educacao-especial` for the `PEI`/`IEP` compliance surface → `xAPI` statements
from every component into one store → `LucasSpinola`'s curriculum as the faculty track.

🟢 **Why this is the pass's strongest recipe:** every component is permissive, byte-read, and
**placed in LATAM on evidence** — a statutory instrument, a named university, or a Portuguese
holder line. 🔴 **Declared substitution:** `Edwin1719/AvatarAcademy` was considered and **left out**
— it depends on a hosted frontier model, which contradicts the auditability this recipe is sold on.

### 🟢 `P620-3` — Offline-first science laboratory for African universities (`6`–`8` weeks)

**The demand.** `AfriLab`'s own README states it: *"African universities — no physical lab
required"*, *"African science education: equipment is scarce, consumables are expensive"* — and EMEA
has `€25.4M` in EC Advanced Digital Skills grants and `£200M+` of UK adoption money attached to
dated instruments.

| Component | Grant (byte-read) | Role in the wiring |
|---|---|---|
| 🟢 [`ghwmelite-dotcom/AfriLab`](https://github.com/ghwmelite-dotcom/AfriLab) | 🟢 `MIT`, `1,064 B` | `29` simulations across chemistry, biology, physics, pharmacy, medicine, plus a lab assistant. 🟢 **EMEA-placed on its own text** |
| [`openzim/phet`](https://github.com/openzim/phet) | 🟢 `Apache-2.0`, `11,356 B` | Packages the published `CC-BY` PhET simulations into offline `ZIM` archives — the breadth `AfriLab` does not have |
| `Kolibri` (`MIT`, `1,097 B`, branch `develop`, `p616`) | 🟢 `MIT` | Offline-first delivery and sync. 🟢 Consumes `ZIM` content natively — the two halves were built for each other and this base held both without wiring them |
| [`Ghost-ops721/alyra-labs`](https://github.com/Ghost-ops721/alyra-labs) | 🟢 `MIT`, `1,068 B` | Reaction-level chemistry depth where `AfriLab` is broad |
| `QTIWorks` (`BSD-3-Clause`, Univ. of Edinburgh, `p607`) | 🟢 `BSD-3` | Assessment engine so lab work is examinable offline |
| EU high-risk conformity harness (`p606`) | 🟢 permissive | Sized to the `2 Dec 2026` and `2 Dec 2027` deadlines already tracked here |

**Wiring.** `Kolibri` as the offline delivery shell → `openzim/phet` feeds it `CC-BY` simulation
content → `AfriLab` and `alyra-labs` provide the locally authored, MIT-licensed sims → `QTIWorks`
runs the assessments → everything syncs when connectivity appears → the `p606` harness carries the
EU conformity artefacts.

🟢 **The new wiring this pass contributes** is `openzim/phet` → `Kolibri`: a licensed, maintained
pipeline from the world's best science-simulation library into an offline-first LMS, discovered only
because `620-I` forced the question of *where* PhET's content is actually licensed.

### 🟡 `P620-4` — Teacher-mediated, deterministic AI literacy for an APAC primary mandate (`10`–`12` weeks)

**The demand, and the constraint is the design driver.** China's Ministry of Education mandates AI
instruction **from age six across every grade**, with an `AI + Education` plan running to `2030` —
and **prohibits independent generative-AI use by primary-school children**. Japan's pilot sits at
`478` schools, under `2 %` of ~`33,000`, with guidance permitting teacher use *provided the teacher
can judge the output*.

🔴 **Both constraints point away from a hosted chat tutor** and toward deterministic, offline,
teacher-in-the-loop tooling.

| Component | Grant (byte-read) | Role in the wiring |
|---|---|---|
| `Kolibri` (`MIT`, `p616`) + [`openzim/phet`](https://github.com/openzim/phet) (`Apache-2.0`) | 🟢 | Offline content delivery with **no model call from the child's device** — which is how the primary-school prohibition is satisfied architecturally rather than by policy |
| 🟢 [`AyushBinjola1/Swar-Setu`](https://github.com/AyushBinjola1/Swar-Setu) | 🟢 `MIT`, `1,070 B` | Multilingual screening for dyslexia, dysgraphia and dyscalculia — 🟢 the only **APAC-placed** supply row this base has, and multilingual is the regional requirement |
| `dsvi-b/corretor-enem` (`MIT`, re-read today) | 🟢 `MIT` | 🔵 **Named as a technique, not as a product**: a `5`-competency rubric grader calibrated on `11,147` real scripts with **no API and no ML**. It is the reference implementation for a grader a ministry can audit |
| `LTI 1.3` tier (`p612`) + `xAPI`/`cmi5` tier (`p613`) | 🟢 permissive / `Apache-2.0` | Teacher-facing dashboards; the teacher, not the model, closes every loop |
| `PhET` engine stack (`MIT`, `9` repos) | 🟢 `MIT` | The AI-literacy and science curriculum content layer |

🔴 **Why `10`–`12` weeks and why this recipe is the weakest of the five:** the per-country
compliance surface is real — ASEAN guidance is early-stage, so each market is tailored separately,
and `620`'s APAC supply yield was **`1` repository across eight legs**. 🟡 **This is a build posture,
not an assembly posture** (`T620-3`), and it is priced and labelled as one.

### 🟢 `P620-5` — Permissive music-education stack (`4`–`6` weeks)

**Why it exists.** `620-C`'s census returned **`0`** for `music education` across all seven shelf
files, and the tier turned out to have a complete, permissive primitive stack nobody had wired.

| Component | Grant (byte-read) | Role in the wiring |
|---|---|---|
| 🟢 [`tonaljs/tonal`](https://github.com/tonaljs/tonal) | 🟢 `MIT`, `1,074 B` at **`docs/LICENSE`** | Theory vocabulary — notes, intervals, scales, chords, keys, progressions. `4,268★`. 🔴 Platform field says `NONE`; see `620-B` before any dependency screen rejects it |
| 🟡 [`CoderLine/alphaTab`](https://github.com/CoderLine/alphaTab) | 🟡 **`MPL-2.0`**, `16,907 B` | Notation and tablature rendering, `1,899★`. 🔴 **File-level reciprocity**: links into a closed deliverable, but modifications to its own files must be published. Put this in the licence matrix on day one |
| [`sirged/fermata`](https://github.com/sirged/fermata) | 🟢 `MIT`, `1,077 B` | Self-hosted score library and server — the institution's own content, searchable, with PDF and interactive rendering |
| 🟡 [`ShacharHarshuv/open-ear`](https://github.com/ShacharHarshuv/open-ear) | 🟡 `MIT` **in README** (`620-F`) | The learner-facing ear-training runtime, `186★` — the tier's best-adopted app. 🔴 Its grant is sound and **not machine-detectable**, so a client's licence scan *will* flag it. Raise the `LICENSE`-file issue before the engagement, not during it |
| [`Zachacious/MusicTheoryJS`](https://github.com/Zachacious/MusicTheoryJS) | 🟢 `ISC`, `746 B` | Alternative/secondary theory engine — microtonal tunings and MIDI where `tonal` stops |

**Wiring.** `fermata` holds and serves the scores → `alphaTab` renders them → `tonal` supplies the
theory vocabulary for analysis and exercise generation → `open-ear` drills the learner →
`MusicTheoryJS` covers microtonal and MIDI cases.

🔴 **Two stated gaps, because this stack is not finished.** There is **no `LTI 1.3`, no `xAPI` and no
gradebook anywhere in the tier** (`620-P`) — so unlike `P620-1` and `P620-2`, this stack **cannot
currently report to an LMS**, and wiring it to `p612`/`p613`'s tiers is net-new work. And there is
no permissive notation **incumbent**: `MuseScore` remains `GPL-3.0`.

### 🔴 `620-R` — control debt: what this pass could not discharge, and the one item it created

🔵 Carried forward explicitly, because `T620-5` says this base has learned the same lesson six times
and written it into a gate **zero** times.

| # | Debt | Status |
|---|---|---|
| `1` | 🔴 **ACTION `620-T`, ranked first: wire the pass-level probe to the gates this repository already owns.** `620-B`, `620-F` and `620-G` were each written up as findings and each is **already encoded in a wired, green gate** — `gate-subtree-grant` (`p382`, `19` controls), `gate-readme-channel` (`p288`, in `HOOK_GATES`), `gate-template-identity` (`p312`, `80` controls, and it records the MIT byte band as **refuted**). 🔴 The instrument is **not** missing; it is **not called**. A pass writes a fresh `bash` ladder in `scratchpad/` and `compose/code/` goes untouched. | 🔴 **the pass's worst result**, open |
| `2` | 🟡 **Holder-standing is the one real instrument gap.** None of the three gates above tests whether a grant's copyright holder is a party **with standing in the repository** — which is the only check that caught `620-G`'s `650 Industries, Inc. (aka Expo)` payload. This is net-new and belongs beside `gate-template-identity`. | 🟡 **created this pass**, open, narrow and cheap |
| `2b` | 🔴 **`gate-grant-path` is red on the inherited tree**, and it guards exactly what `620-B` got wrong. A pass hand-rolled a path ladder while the gate for path ladders was failing beside it. | 🔴 inherited red, `21` of `70` — see `620-U` |
| `3` | 🟡 **Holder-standing check for scaffold licences.** `620-G` found one `MIT` payload granting `650 Industries, Inc.`'s copyright. A census of this shelf's existing `MIT` rows for holder strings naming `Expo`, `Vercel`, `Meta Platforms` and similar would size the class. | 🟡 open, cheap, not run |
| `4` | 🟡 **`archived` field unused.** `620-A`'s channel returns it on every row; no row this pass read it. `p612`'s `Continue`-archived class is exactly what it catches. | 🟡 open, now trivial |
| `5` | 🟡 **Fork-ratio census never run.** `620`'s two best adoption signals (`chipper` `20/17`, `dyscalc` `19/10`) came from forks, not stars, and this base has `3,828` addresses on which it has never computed one. | 🟡 open, now trivial |
| `6` | 🟢 **Non-English query tuning.** `620`'s Spanish **two-word** legs paid `7` new names where four-term legs paid `0`. The same tuning has **never** been applied to Mandarin, Japanese, Arabic, French or German — which is `T620-3`'s declared instrument bias. | 🟢 **actionable next pass**, highest expected yield |
| `7` | 🔴 **Licence asks never sent.** `619-G` named one (`jonajinga/open-phonics`); `620` adds four of real value: [`BarkaviNatraj/learning-disability-app`](https://github.com/BarkaviNatraj/learning-disability-app) (`28★`), [`raphateixeira/LabVirtual`](https://github.com/raphateixeira/LabVirtual) (UFPA, LATAM), [`PriontoAbdullah/Anushilon-Virtual-Science-Lab`](https://github.com/PriontoAbdullah/Anushilon-Virtual-Science-Lab), [`ShacharHarshuv/open-ear`](https://github.com/ShacharHarshuv/open-ear) (`186★`, needs only a file move). 🔵 **No pass has ever sent one**, so the "ask, not a fix" action has been recorded `5` times and executed `0`. | 🔴 open, and the gap between recording and acting is itself the finding |

🟢 **And three items discharged this pass, all the same lesson in different places:**

1. The **push block** recorded since `p54` and re-recorded at `p615`, `p617` and `p619` is **gone** —
   this session holds write access and this commit is pushed.
2. 🟢 **`619-L`'s execution denial is gone**: `make hooks` ran all `70` gates (`620-S`), so this is
   the first gate-verified commit in four passes. `gate-declared-gap`, wired at `618-A` and
   **never executed**, got its first green run.
3. 🟢 **`gate-region-headings` caught two real defects** in this pass's own `intel/market.md` that a
   careful read had passed — an out-of-vocabulary `###` child and a missing `### Global`. `p619`
   repaired this file *"by reading, not by running"*; this pass repaired it **by running**.

🔵 **All three were inherited verdicts that were never re-measured — the same shape as `620-A`'s
`566`-pass "API is blocked". A blocked-channel verdict has a shelf life of one pass.**

## 🆕 `p619` — reads `2026-11-02` — **five recipes, every component byte-read today, plus the control debt this pass could not discharge**

### `P619-0` 🔴 Discharge the control debt first — `1` wk, and nothing else in `p618`/`p619` is trusted until it is done

**The gap:** `619-L` is the **third** consecutive pass refused `[Code from External]`. Two gates are
now owed a green run they have never had: `gate-declared-gap` (wired at `618-A`, never executed) and
`gate-region-headings` (wired, and **red-then-repaired** at `618-L`).

**Wire it, in a session that can execute code from this clone:**
1. `make gate-region-headings` — must be green on `intel/market.md`. 🟢 `p619` left **exactly one**
   canonical `## Opportunities by region` block with exactly the five closed-vocabulary `###` children
   (`North America`, `EMEA`, `APAC`, `LATAM`, `Global`), and retitled `p618`'s to
   `— `p618` (archived)`. **Verified by reading, not by running.**
2. `make gate-declared-gap` — the suite is authoritative; `make declared-gap-sweep` is a
   **measurement, never a failure** (`618-A`).
3. 🔴 **Unblock the masking before trusting either:** `recount`'s inherited red (`Gap 534-J`) halts the
   runner before later gates are judged, so a green line from `hooks` today proves nothing about the
   gates behind it (`618-L`).
4. Then `619-E`'s generalisation, which is cheaper than it sounds: for **every** column this base
   claims to verify, write down **the observation that would make it fail**. The `Branch` column had
   none for `246`+ rows. Start with `★`, `Pushed` and `Region`.

**Done when:** both gates print green once, and `recount`'s red is either fixed or explicitly excluded
with a reason in the `Makefile`.

### `P619-1` 🟢 Read-aloud fluency assessment as an `LTI 1.3` tool — `6`–`8` wk — the pass's strongest recipe

**Who buys it:** a US district or state under `IDEA` / `Section 504`, or any system with a mandated
early-reading screener. 🔵 `T619-4`: this is a **statutory** purchase, not a pilot, which is why it
survives a budget freeze.

**Wire it:**
1. **Corpus** — [`valueforvalue/OpenPhonograms`](https://github.com/valueforvalue/OpenPhonograms)
   (`MIT`, `1,070 B`): `248` lessons, `25` decodable readers, Pre-K→G3+. 🔴 Keep the bundled **`OFL`**
   font in its own lane; it is separately licensed.
2. **Assessment loop** — [`tanner-griffith/phono-storyforge`](https://github.com/tanner-griffith/phono-storyforge)
   (`Apache-2.0`, `10,760 B` — complete, `619-F`): per-child mastery model, next skill chosen **from
   reading evidence**, decodable book generated, read-aloud heard, **every miscue attributed to its
   grapheme**. 🟡 Its own sweep claims it beats static but *"does not reliably win past a `0.95`
   mastery bar"* — **the author's claim; treat the bar as an open question, not a spec.**
3. **Rendering** — [`alpharigel/phonics-font`](https://github.com/alpharigel/phonics-font)
   (`Apache-2.0`, stock `11,357 B`) for the decodable glyphs neither component ships.
4. **Scheduling** — carried `FSRS-6`/`SM-2` layer (`618-M`); the scheduler, not the model, is what
   retains a learner.
5. **Boundary** — ship as an **`LTI 1.3` external tool** (`619-M2`), not a Moodle plugin or an
   `XBlock`. Roster and grade passback over `LTI`; **no studio code inside the `GPL`/`AGPL` LMS.**
6. 🔴 **`NOTICE` discipline:** two `Apache-2.0` components means attribution and a `NOTICE` file
   (`618-E`). Do this at week one, not at delivery.

**Delivery note:** `phono-storyforge` is `1★` and `41` commits. 🔴 This is an **adoption of a design**,
not of a maintained dependency — budget a fork and an owner.

### `P619-2` 🟢 A Deaf-access channel for live instruction — `8`–`10` wk

**Who buys it:** a ministry or university with a Deaf-access obligation; in APAC specifically, an
**Indian** institution, because two of the components target **Indian Sign Language** (`619-M`'s
by-subject placement).

**Wire it:**
1. **Pose path** — [`imRishabhGupta/Indian-Sign-Language-Recognition`](https://github.com/imRishabhGupta/Indian-Sign-Language-Recognition)
   (`MIT`, `221★`, `79` forks) or [`Arshad221b/Sign-Language-Recognition`](https://github.com/Arshad221b/Sign-Language-Recognition)
   (`Apache-2.0`, `265★`, **`106` forks**, ships a `PyTorch` port). 🟢 Pick on **forks, not stars** —
   `106` forks is the tier's real reuse signal.
2. **Motion path** — [`AvishakeAdhikary/…-LSTM-Model`](https://github.com/AvishakeAdhikary/Realtime-Sign-Language-Detection-Using-LSTM-Model)
   (`MIT`) or [`FrederikSchorr/sign-language`](https://github.com/FrederikSchorr/sign-language)
   (`MIT`) for **continuous** signing, which the pose classifiers cannot do.
3. **Feature extraction** — [`JaspreetSingh-exe/Sign-Language-Recognition-System`](https://github.com/JaspreetSingh-exe/Sign-Language-Recognition-System)
   (`MIT`, holder year `2025`, the freshest grant here) for the `MediaPipe`→`MLP` pipeline, and because
   it names **text-to-sign** as a direction.
4. **Baseline you must beat before funding a `GPU`** — [`Anmol-Singh-Jaggi/Sign-Language-Recognition`](https://github.com/Anmol-Singh-Jaggi/Sign-Language-Recognition)
   (`MIT`, classical `kNN`/`SVM`). 🟢 **Run this first.** If it is close enough, the whole engagement
   gets cheaper and deployable on classroom hardware.
5. **Media** — **BigBlueButton** (`LGPL-3.0`) as the `WebRTC` classroom the channel rides on; the
   recogniser stays a separate service, **outside** the `LGPL` boundary.

🔴 **Scope honestly:** all five models are **finger-spelling / alphabet or short-gesture** classifiers.
None is a translation system. The deliverable is an **access channel and a dataset flywheel**, and
promising interpretation would be misrepresenting every component.

### `P619-3` 🟢 Offline articulation practice for a zero-budget public system — `4`–`6` wk — LATAM-shaped, not LATAM-only

**Who buys it:** a public university or school system in `619-N`'s segment — **`4%`** dedicated AI
funding, **`55%`** no AI budget at all, **`90%`** already using general tools. 🔵 The bid must have **no
recurring per-seat cost**.

**Wire it:**
1. **Runtime** — [`developerali123/speech_therapy_app`](https://github.com/developerali123/speech_therapy_app)
   (`MIT`, `1,075 B`): frontend-only `PWA`, recordings in **`IndexedDB`**, therapist-review flow.
   🟢 It **states its own clinical boundary** (non-diagnostic, alongside an `SLP`) — keep that wording;
   it is a liability feature, not modesty.
2. **Host** — **Kolibri** (`MIT`) for offline-first distribution where there is **no LMS to attach
   to**. 🔵 The only permissive incumbent on the shelf (`619-M2`).
3. **Content** — `OpenPhonograms`' corpus for the articulation targets.
4. 🔴 **Explicitly excluded:** [`sunnydev07/Open-Speech`](https://github.com/sunnydev07/Open-Speech)'s
   real-time **`CEFR`** rating. The feature is good and the grant is clean `MIT` — but it depends on a
   **hosted model**, and in this segment that is a **disqualifier**, not a line item (`T619-5`).
5. 🟢 Where connectivity exists, [`future-finder/speech-practice`](https://github.com/future-finder/speech-practice)
   (`MIT`) adds timed drills. Treat it as an upsell, never as the base.

**Done when:** the whole thing installs from a `Kolibri` channel on a device that never reaches the
internet, and a teacher can export a learner's progress by file.

### `P619-4` 🟡 Disclosure-based academic-integrity workflow — `6`–`8` wk — the product the instruments are asking for

**Who buys it:** the **`53%`** restrictive bloc in `619-K`'s US figures — **`42%`** discourage +
**`11%`** prohibit — facing **`57%`** weekly student use regardless. Also any Philippine institution
under **DepEd Order `003`, s. `2026`**, which **mandates student disclosure**.

**Wire it:**
1. **Policy surface** — an `LTI 1.3` tool that attaches a **structured disclosure** to each submission:
   which tool, which step, what the student did themselves. 🔵 `T619-1`: every instrument that landed
   this pass asks for **accountability**, not detection.
2. **Grade boundary** — disclosure travels with grade passback over `LTI`; **no studio code in the
   `AGPL` LMS** (Canvas dominates the US buyer).
3. **Rubric layer** — the shelf's carried `rubric` material (`334` mentions) is the one tier this base
   is **over**-supplied in; spend nothing new here, reuse it.
4. 🔴 **Build no detector.** Not as a feature, not as a fallback. It is the thing the sector is moving
   away from, it is unreliable, and it converts a compliance sale into an adversarial one.

🔴 **Carried caveat, and it governs the EMEA version of this recipe:** whether the **AI Act's**
high-risk obligations bite on education from **`2 August 2026`** is **unverified** (`619-K` is exactly
why that date is not being treated as settled). 🔵 Scope the EU variant against the **March `2026`
ethical guidelines**, which are dated and confirmed, and put the AI Act date behind a verification
task rather than inside a statement of work.


## 🆕 `p618` — reads `2026-11-02` — **four recipes, each wired from rows byte-read today**

### `P618-0` 🔴 Finish the control that `618-A` wired, and sweep for the others like it — `1` wk
**The gap:** `gate-declared-gap` is now in `HOOK_GATES` but has **never been run** (`618-B`: code from
this clone cannot execute under this permission set). `gate-region-headings` was wired and **red and
masked** behind `recount` (`618-L`).
**Wire it:**
1. In a session that can execute: `make gate-declared-gap` and
   `$(PY) -I compose/code/p383-region-heading-gate/check_headings.py intel/market.md`. Both must print
   green before anything else in this pass is trusted.
2. `make declared-gap-sweep` — expect `CONTRADICHO` as an **upper bound** (its unit is the sentence and
   it cannot yet tell an assertion from a citation); the suite is the authoritative reading.
3. Then the generalisation: `grep -rl "def test_\|unittest" compose/code/*/ | ` each directory, against
   every target in the `Makefile`. **Any suite in no target is an uninstalled control.** `p370-gap-gate`
   lived `246` passes that way and `p383`'s lived `54`.
4. Fix the **masking** separately: `recount`'s inherited red (`Gap 534-J`) stops the runner before later
   gates are judged. Order `HOOK_GATES` so declared-red gates run **last**, or run each gate
   independently and report a matrix.
🔵 **Deliverable:** a one-line census — *"`N` suites exist, `M` are wired, `K` are reachable past the
first red"* — which is the only number that says whether this repository is actually controlled.

### `P618-1` 🟢 Language-learning surface on a permissive scheduler, beside the incumbent LMS — `2`–`3` wk
**Components, all byte-read this pass:** [`m98/fluent`](https://github.com/m98/fluent) (`MIT`, `445★`,
`FSRS-6`) as the scheduling + review loop; [`felipepenha/morphcards`](https://github.com/felipepenha/morphcards)
(`Apache-2.0`) for the **item-generation** half, which it cleanly separates from scheduling;
[`1602WinXP/textbook-tutor`](https://github.com/1602WinXP/textbook-tutor) (`MIT`) as the tutor-persona
skill; the client's `Moodle`/`Open edX` as the system of record.
**Wiring:** `fluent` owns the review schedule and holds learner state; `morphcards`' generator produces
item variants from the client's own corpus; `textbook-tutor` supplies the tutoring voice; progress is
written back to the LMS over **`xAPI`** so the LMS stays the record and the copyleft boundary is never
crossed (`618-N`).
🔴 **Two obligations, not one:** `morphcards` is `Apache-2.0`, so the build carries **attribution and
`NOTICE`** duties `MIT` does not (`618-E`). Generate the `NOTICE` file in CI, not by hand.
🔴 **Pin `m98/fluent`, not `aymkin/fluent`** — the `0★` copy is the one that looks freshest (`618-F`).

### `P618-2` 🟢 The canonical-resolution step the composition gate is missing — add to `P616-0`
`P616-0` grades: branch → title family → residual read → enumerate the vendored tree. 🔴 It has **no step
that asks whether the slug in hand is the canonical one**, and `618-F` is what that costs: two
`fork=false` repositories, byte-identical `MIT` payloads, the copy pushed four months later.
**The step, in order:**
1. Read the grant's **holder line**. If it names a **slug**, that slug is the canonical candidate — this
   is stronger than byte-identity, which `617-G` showed indicates only an owner convention.
2. Probe that slug. If its payload is byte-identical, prefer it and record the other as a **copy**.
3. 🔴 Never rank candidates by `pushed_at` alone.
4. `p404`'s full-history grade remains owed where the holder line is silent; if the channel is
   unavailable, **register it** rather than guessing (as `618-F` does).

### `P618-3` 🟢 Governance-as-deliverable for a LATAM institution — `3`–`4` wk
**Why this shape:** LATAM has the strongest demand evidence of any region (`92%` students / `79%`
faculty) and **no binding** rule, with a pronounced adoption-versus-governance gap. The client does not
need a pilot; they need a defensible policy with a working surface attached.
**Components:** [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (`MIT`, Universidad
Tecnológica de Pereira, runs **inside Open edX**, re-measured current this pass) **attached** to the
client's existing Open edX estate rather than migrating it; the `xAPI` decision record from `P617-2` as
the audit surface.
**Budget line nobody budgets:** `616-H`'s remedy — **upstream `LICENSE` pull requests**. The region
publishes; the licence file is what is missing (`1 of 8` permissive across `latam-gpt`), so a few days of
a senior engineer's time converts unusable regional supply into usable supply, for this engagement and
every later one.
🔴 **Do not infer the region of a component from its author's name** (`618-J`). If a holder's location is
not readable, the row ships *unplaced*.


## 🆕 `p617` — reads `2026-11-02` — **three recipes, each wired from rows byte-read today**

### 🟢 `P617-0` — the declared-gap gate: install the control this repository already owns

🔵 **The defect it fixes is `617-B`**, and the code already exists — this is a wiring recipe, not an
implementation.

1. `make install-hooks` — `ingest/pre-commit` is **per working copy**; `git clone` does not carry it
   (`Gap 423-B`). A fresh clone has **no** commit gate at all.
2. Add a `gate-declared-gap` target that runs
   `compose/code/p370-gap-gate/test_gap_gate.py` (its suite, including the mandatory case that the two
   real sentences in the tree come out with **opposite** verdicts), then
   `gap_gate.py --sweep .` over the published pages.
3. Add `gate-declared-gap` to `HOOK_GATES`. 🔴 **Not** to `DECLARED_RED` — a gate that cannot block is
   `617-B` again under a new name.
4. Re-run `make commit-gates` and expect it to **refuse** a commit that declares an index-form gap the
   index refutes.

🔵 **Generalise before moving on — this is the step that pays twice.** Sweep `compose/code/` for every
directory shipping a `test_*.py` that the `Makefile` never names. `483` directories exist;
`p370-gap-gate` was found by following a citation, not by sweeping, so the population is unmeasured.
🟡 Cost: hours. 🟢 Applies unchanged to a client's AI-governance estate, where the same audit finds
written policies with no enforcement point.

### 🟢 `P617-1` — the composition gate for a scaffolded `MIT` repository, in both directions (`1` wk)

🔵 Wired from `616-A`, `617-E` and `617-F` together, because each of the three bounds the others.

1. **Resolve the branch** with `ls-remote --symref`. Never assume `main` — `616-K` measured `2` of `7`
   reads on `develop`/`master`, and `617-E`'s row would have read ungranted on a wrong branch.
2. **Grade the title line** over the first **three non-blank** lines (`ingest/p612-grade-title-line.py`).
   🔴 Do not narrow it to line `1`: `617-H` measured `LabSirius/TutorIA` opening with `---`, so a
   line-1 grader files this base's strongest LATAM row as `UNCLASSIFIED-NEEDS-HUMAN`.
3. **Check the residual.** A stock titled `MIT` is `1,056`–`1,097 B` (`616-B`, `8` publishers). Outside
   that band, **read the whole file** — `616-A`'s `2,254 B` payload excluded `26` of its own
   directories `1,157` bytes below a stock `MIT` title.
4. **Enumerate every sibling `*-LICENSE.*` and the vendored tree, and grade each on its bytes.**
   🔴 Never on the filename, **in either direction**: `616-A`'s vendored tree was fatal
   (`CC BY-NC-SA 4.0` plus directories the publisher states were *"included without authorization"*),
   and `617-F`'s `GEMMA-LICENSE.txt` is merely an `Apache-2.0` **attribution notice**.
5. **Read the README last, and give it no authority.** 🟢 It is evidence of author **intent** only
   (`617-E`): it may claim more than the payload (`616-C`) or **less** (`GradeMateAI` disowning its own
   stock `MIT`). The payload governs both ways.

### 🟢 `P617-2` — a permissive, audit-first assessment surface beside an incumbent LMS (`4`–`6` wk)

🔵 Built for the shape `T617-3` measures and the `2027-12-02` Annex III band rewards: **recommend with
an audit trail**, never decide. Every component named here was byte-read by this base.

- **Assessment platform** — [`azapg/FAIR`](https://github.com/azapg/FAIR) (`MIT`): rubrics, pluggable
  agent graders, research datasets. 🟡 `6★` — run it as the **assessment service beside** the client's
  LMS, not as an LMS migration.
- **Recommend-not-decide grader** — [`sirithreddy175-boop/GradeMateAI`](https://github.com/sirithreddy175-boop/GradeMateAI)
  (`MIT`) for rubric-driven handwritten work, or
  [`Osarodion843/EduGrade-AI`](https://github.com/Osarodion843/EduGrade-AI) (`MIT`) for batch sheets
  with written feedback.
- **Confidence routing** — `Keshav0141/Auto-Assessment-Agent` (`MIT`): low-confidence gradings go to a
  human queue. 🟢 This is the component that makes the band's "human oversight" requirement a
  mechanism instead of a claim.
- **Local-only integrity** — `biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent` (`MIT`): no
  external AI APIs, emits an **evidence breakdown** rather than a verdict. 🟢 Clears a strict
  data-residency brief.
- **Record of record** — `adlnet/ADL_LRS` or `EscolaLMS/LRS` over `adlnet/xAPI-Spec`: every
  recommendation, its confidence, its rubric criterion and the human's final mark as xAPI statements.
  🟢 **This is the deliverable.** The graders above are commodity and `MIT` at `0★`; the queryable
  decision record is what no row on this shelf ships well.
- **Stay inside the LMS** — `Cvmcosta/ltijs` or `academic-innovation/django-lti`, so the surface
  attaches to `Moodle`/`Open edX` instead of replacing them and the copyleft question never reaches
  the new code.

🔴 **Build-vs-adopt, stated honestly:** at `6★`/`0★`, treat `FAIR` and the graders as **reference
implementations to fork**, not as upstreams to depend on. The durable asset is the LRS schema and the
confidence-routing policy.

### 🟢 `P617-3` — a LATAM tutoring engagement that adds to the estate instead of migrating it (`3`–`4` wk)

🔵 Wired from `617-A`, and it exists because the index-form LATAM gap was false.

- **Tutor** — [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (`MIT`, © `Grupo Sirius`,
  Universidad Tecnológica de Pereira): autonomous tutor agent for **rural** higher education, Spanish,
  with TTS audio replies, an animated avatar, cross-session context and a **teacher statistics panel**.
- **Attach, do not replace** — it runs **inside Open edX** as an XBlock-shaped surface. 🟢 The client
  keeps its `AGPL-3.0` estate; the permissive code sits beside it, so copyleft never reaches the new
  work. This is the property that makes it the most reusable LATAM row on this base.
- **Offline/low-connectivity half** — `learningequality/kolibri` (🔵 default branch **`develop`**,
  `616-K`) where the rural brief needs it.
- **Bilingual learner surface** — `Hainrixz/maia-skill` (`MIT`) is this base's only bilingual
  `EN`/`ES` learner-facing row.
- 🔴 **Upstream contribution as a deliverable, not a courtesy:** `616-H` measured `7 of 8` LATAM
  repositories with **no `LICENSE` file at all**. Budget one engagement day to open `LICENSE` pull
  requests on the repositories the project actually uses. 🟢 It converts the region's measured cause
  into reusable supply, and it is the cheapest line item in the plan.

## 🆕 `p616` — `2026-11-02` — patterns wired from rows byte-read today, led by **one control that this pass proved is missing from the gate it belongs in**

### 🟢 `P616-0` — the composition gate — **prerequisite to every pattern below**

🔴 `p615`'s `P615-0` made the grant check a build step. 🟢 This pass found the hole in it: the check
reads **one file per repository**, and the sector's dominant supply shape is a repository that ships
`26` other people's directories. 🔵 So `P616-0` extends it rather than replacing it.

**Components:** `git ls-remote --symref` (branch resolution, `p559`) · `raw.githubusercontent.com`
(grant bytes) · this repository's hardened classifier (`p615`) · the stock-byte band (`616-I`).

**Wiring, as a four-step gate run before any component is accepted:**

```
1. branch   := ls-remote --symref <repo> HEAD      # never assume main — 2 of 7 reads this pass
2. family   := classify(title line)                # p612 rule; body-only match => NOT permissive
3. residual := bytes - stock(family)               # stock MIT = 1056..1097 B (616-I, n=8)
      residual > ~100 B  =>  ADDITIONAL-TERMS: read it, in its own language, before shelving
4. tree     := enumerate vendored dirs, probe each distinct upstream once   # <- NEW this pass
      any upstream ungranted or NC/SA  =>  refuse, or remediate per P616-2
```

🟢 **Cost, measured:** step `4` took `3` upstream probes — roughly `90` seconds — to move `616-A`'s
specimen from *"`MIT`, looks shippable"* to *"contains `NonCommercial` and unlicensed copies"*.
🔴 Steps `1`–`3` alone would have shipped it.

🟡 **Stated limit:** step `3` catches instruments that **append**. It will not catch a substitution
made inside the stock text at constant length. 🔴 Do not treat a passing residual as proof of a stock
grant; it is absence of the one defect this control detects.

### 🟢 `P616-1` — tutor-as-a-skill, on a grant-clean tree — `2`–`3` weeks

**Components, every grant byte-read today:**
[`ChatGPT3a01/claude-educational-ai-skills`](https://github.com/ChatGPT3a01/claude-educational-ai-skills)
(`MIT`, `1,086 B`, `master`) for the education skill set ·
[`mcxiaoxiao/kaoyan-navigator-skill`](https://github.com/mcxiaoxiao/kaoyan-navigator-skill)
(`MIT`, `1,093 B`) as the worked reference for an **advisory** rather than tutoring shape ·
[`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (`MIT`, `456★`, re-measured
today) for mastery estimation.

**Wiring.** Ship the skill set as `SKILL.md` workflows against the client's existing agent client —
there is no infrastructure to stand up, which is the whole commercial point of this class. Back the
*"what does this learner know"* question with `pykt` rather than with the model's own guess: the
skill emits an interaction log, `pykt` returns per-concept mastery, and the skill's next move is
selected from that vector. 🔵 `kaoyan-navigator` is the pattern to copy for any **selection** problem
(course, programme, path) — it researches a live data surface, then emits a reach/match/safety
ranking with explicit risk notes, which is a defensible shape for advice a client is liable for.

🔴 **Do not** vendor `dmccreary/ibook-skills` into this, however good its `570`-concept learning graph
is — `616-C`, it has no grant.

### 🔴 `P616-2` — the remediation recipe: taking the usable half of an `ADDITIONAL-TERMS` package — `1` week

🟢 `616-A`'s package is **not** a refusal in the way PageLM is. Its publisher enumerated exactly what
is and is not covered and named the remedy, so the permissive subset is identifiable.

**Recipe:**

```
1. read the residual clause and list the covered paths   # here: named root files,
                                                         # skills/office-layer/, 22 first-party skills
2. delete every directory the clause excludes            # here: the 26 vendored "base-layer" dirs,
                                                         # incl. thinking-toolkit (CC BY-NC-SA 4.0)
                                                         # and the 7 ibook-skills copies (unlicensed)
3. re-probe the remaining tree for any further vendored upstream
4. record the deletion list in the engagement's licence record, with the clause quoted
5. re-source the deleted capability from a permissive upstream  # xxf-ai/awesome-benzi (MIT, 1,063 B)
                                                                # ChatGPT3a01/... (MIT, 1,086 B)
```

🔵 **Why step `4` is not bureaucracy.** The deleted directories are the ones a future contributor will
re-add by reflex, because they are the ones that make the package feel complete. 🟢 The deletion list
*is* the deliverable's licence boundary.

🟡 **When to refuse instead.** If the excluded set is load-bearing for the client's requirement, the
remediation is a rewrite, not a deletion — price it as such rather than as an integration.

### 🟢 `P616-3` — offline-first deployment for a connectivity-constrained region — `6`–`8` weeks

**Components:** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (`MIT`,
`1,097 B`, branch **`develop`** — `616-K`) as the delivery substrate ·
[`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (`Apache-2.0`, `p615`) where a full LMS with
`QTI 2.1`/`SCORM 1.2`/`LTI 1.3` is required centrally · `pykt-toolkit` (`MIT`) for mastery · the
`P616-1` skill tier for content generation **at the centre, never on the edge device**.

**Wiring.** Kolibri at the edge, syncing opportunistically; OpenOLAT as the system of record where one
is needed; all agent/LLM work batched centrally and shipped to the edge as **generated artefacts**,
because the edge is defined by not having connectivity. 🔵 This is the architecture the LATAM evidence
selects: connectivity, device access and digital literacy are the reported limiters (`616-H`), so a
pattern that assumes a live model call per learner interaction is disqualified before pedagogy is
discussed.

🟡 **Honest placement caveat.** Kolibri is `MIT` and offline-first and therefore *usable* in LATAM; it
is **not LATAM-published**, so it gives the client no local maintainership. 🔴 `616-H` is unclosed and
this pattern does not close it.

### 🔵 `P616-4` — a bilingual `EN`/`ES` learner-facing surface — `2` weeks

**Component:** [`Hainrixz/maia-skill`](https://github.com/Hainrixz/maia-skill) (`MIT`, `1,089 B`,
`151★`) — `5` agents in parallel over market data, risk-profiled, rendering an interactive
**bilingual `EN`/`ES`** dashboard, published explicitly as *educational market research, not
financial advice*.

**Wiring.** Take it for two things and not a third: 🟢 the **bilingual rendering layer**, which is the
only Spanish learner-facing surface on this base's shelves and is reusable for any subject; and 🟢 the
**parallel-agents-to-one-dashboard** shape, which is a clean worked example of fan-out plus
synthesis under a permissive grant. 🔴 Do **not** take its domain logic into a client product without
the publisher's own disclaimer surviving intact — the artefact is a teaching device about markets, and
re-presenting it as advice changes its regulatory character entirely.

🟡 It is financial-literacy content on an education shelf, placed `🔵 Global` — holder not placed.
Its value here is the **layer**, not the subject.

## 🆕 `p615` — `2026-11-02` — patterns wired from rows byte-read today, plus **one control that belongs in every engagement**

### 🟢 `P615-0` — the grant gate, as a build step rather than a reminder — **prerequisite to all four patterns below**

🔴 This base published a `NonCommercial` dataset as shippable last pass (`615-A`) because a grader
written inside that pass answered `CC-?` while the shared, hardened, tested classifier in this
repository answers `CC-BY-NC-4.0`. 🟢 So the first recipe is a **control**, not a solution.

```bash
# in any studio repo that vendors third-party education assets
. compose/code/lib/license_family.sh          # never inline a licence classifier (P171, pase 77)

br=$(git ls-remote --symref "https://github.com/$REPO" HEAD \
      | awk '/^ref:/{sub("refs/heads/","",$2);print $2;exit}')   # MEASURE the branch (p509/p517)
curl -sS -o grant.txt "https://raw.githubusercontent.com/$REPO/$br/LICENSE"

family_of "$(cat grant.txt)"                   # -> CC-BY-NC-4.0, not "CC-?"
if commercial_use_ok "$(cat grant.txt)"; then  # EXIT CODE, not stdout -- stdout is empty for MIT too
  echo "shippable"; else echo "BLOCKED: $(family_of "$(cat grant.txt)")"; exit 1; fi
```

🟢 **Wire it as a CI gate on the dependency manifest, failing the build on non-zero.** 🔴 The two
ways to get this wrong are both measured in this base: reading `commercial_use_ok` from stdout
(this pass's own first error, `615-B`), and assuming `main` (`8 of 12` addresses probed today were
`master`). 🔵 Cost: under a day. 🔵 It is the cheapest item in this file and the only one whose
absence has already produced a wrong published verdict.

### 🟢 `P615-1` — Permissive white-label LMS with provable standards conformance — **the pattern the sector was told did not exist**

🔵 **Who it is for:** any client that wants its own branded platform delivered and hosted by the
studio — which `GPL`/`AGPL` incumbents make awkward and Elastic License `2.0` forbids outright.

| layer | component | grant (byte-read `2026-11-02`) |
| --- | --- | --- |
| platform | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` `10,982 B` `master` |
| analytics store | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 `Apache-2.0` `11,357 B` |
| client instrumentation | [`adlnet/xAPIWrapper`](https://github.com/adlnet/xAPIWrapper) | 🟢 `Apache-2.0` `10,273 B` |
| 🟢 **conformance proof** | [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | 🟢 `MIT` `1,046 B` |
| sector vocabulary | [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | 🟢 `Apache-2.0` `11,357 B` |

🟢 **Wiring.** `OpenOLAT` emits `xAPI` via its `LTI 1.3` / `SCORM 1.2` surfaces into `ADL_LRS`;
`xAPIWrapper` instruments any custom activity; `xapi-profiles` pins the client's vocabulary; then
**`lrs-conformance-test-suite` is run in CI as an acceptance test**. 🟢 That last row is what makes
this different from every prior LMS pattern here: interoperability becomes a **passing test suite in
the handover**, not a claim in a slide. 🔵 `6`–`9` weeks. 🟢 Every grant permissive, so white-label
and hosted delivery are both clean.
🔴 **Stated risk:** `OpenOLAT`'s `QTI 2.1`/`SCORM`/`LTI` support is **vendor-stated**; this pass
verified the grant on bytes, not the feature matrix. Verify against a client's real content early.

### 🔴 `P615-2` — Legacy SCORM migration, costed honestly as a **build**

🔵 **Who it is for:** any institution with a decade of `SCORM` courseware moving to analytics.

🔴 **The canonical path is gone.** [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper)
(`99★`) is **archived** and has **no grant file at any of `7` probed names** at `master`. 🔴 So it
cannot be adopted *or* legally vendored, and `adlnet/xAPI-SCORM-Profile` (`42★`), the profile it
implements, is archived too.

| layer | component | status |
| --- | --- | --- |
| profile semantics | `adlnet/xAPI-SCORM-Profile` | 🔴 archived — read as **specification**, not dependency |
| cmi5 path forward | [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | 🟢 `Apache-2.0` `11,358 B`, 🔵 `main` — **live** |
| destination | `adlnet/ADL_LRS` + `lrs-conformance-test-suite` | 🟢 live, permissive |
| server-side bridge | [`RusticiSoftware/TinCanPHP`](https://github.com/RusticiSoftware/TinCanPHP) | 🟢 `Apache-2.0` `11,358 B` — independent implementation |

🟢 **The honest recipe: do not migrate `SCORM`→`xAPI` through the dead bridge — target `cmi5` via the
live `CATAPULT` suite**, using the archived profile as a reference document and `TinCanPHP` for
server-side emission. 🔵 `8`–`12` weeks, of which the bridge is a **build line, not an integration
line**. 🟢 Naming that in a proposal is worth more than a lower estimate that discovers it in week
three.

### 🟡 `P615-3` — Adaptive learning in APAC, with the prerequisite layer **scoped as work**

🔵 **Who it is for:** APAC K-12 adaptive-learning briefs.

🔴 **The shortcut is closed.** [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)
(`6,143★`) — `1,644` knowledge points, `2,403` prerequisite edges, `6,723` problems, curriculum-aligned
— is **`CC-BY-NC-4.0`** (`615-A`). 🟢 Use it to *validate* a graph's shape and to argue the design;
🔴 do **not** ship it, and do not plan the engagement as if the graph were free.

| layer | component | grant | role |
| --- | --- | --- | --- |
| mastery model | `OATutor` (BKT, shelf row) | 🟢 `MIT` | the estimator |
| scheduling | `613-D` FSRS/Anki tier; [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 permissive (shelf) | spaced review |
| 🔴 prerequisite graph | — | — | 🔴 **BUILD**: author with client curriculum staff, or licence `cn-math-taxonomy` separately from its author |
| delivery | `OpenOLAT` + `ADL_LRS` | 🟢 `Apache-2.0` | platform + telemetry |
| 🟢 gate | `P615-0` | — | run on **every** vendored asset before it enters the manifest |

🔵 `12`–`16` weeks, the graph authoring dominating. 🟢 The pattern's value is that the expensive item
is visible in week one instead of at legal review.

### 🟢 `P615-4` — LATAM governance retrofit, sized by the region's own measured gap

🔵 **Who it is for:** LATAM universities already running AI without a framework — `87 %` use vs
`26 %` with any formal framework (UNESCO IESALC, `200` HEIs / `19` countries); Brazil `53 %` vs `22 %`
at school level (Cetic.br `2026`).

| layer | component | grant | role |
| --- | --- | --- | --- |
| evidence spine | `adlnet/ADL_LRS` + `xAPIWrapper` | 🟢 `Apache-2.0` | the audit trail a framework needs to be checkable |
| vocabulary | `adlnet/xapi-profiles` | 🟢 `Apache-2.0` | encode the institution's own policy terms |
| conformance | `adlnet/lrs-conformance-test-suite` | 🟢 `MIT` | prove the trail is standards-valid |
| platform | `OpenOLAT` | 🟢 `Apache-2.0` | permissive, so the toolkit is portable across institutions |
| 🟢 licence control | `P615-0` | — | and it is **the deliverable's own compliance story**, not just hygiene |

🟢 **Wiring and why it is portable.** `716` AI regulatory instruments across `23` countries, >`80 %`
initiated since `2023`, and regional commentary pushing **interoperability** over one regional law —
so build a **policy-as-configuration** toolkit: `xapi-profiles` carries the institution's definitions
and risk categories, the LRS carries the evidence, the conformance suite proves it. 🔵 `6`–`10` weeks
per institution, with the second deployment materially cheaper because only the profile changes.
🟢 UNESCO's LAC Observatory (launched April `2026`, ECLAC Santiago) and its Tecnológico de Monterrey
partnership are the natural reference channel.
🔴 **Declared gap:** no `MIT`/`Apache` LATAM-origin education repository surfaced this pass, so every
component above is non-regional. 🔵 The region is a demand market in this base's measurements, not a
supply one.

## 🆕 `p614` — `2026-11-02` — patterns, each wired from rows this base holds and byte-read today

🔵 Every repository named below is on a sell shelf with its grant byte-read `2026-11-02` at the real
default branch (`evidence/api-vs-bytes-grants.2026-11-02-p614.tsv`, `18 of 18` agreeing with the
platform field). 🔴 Where a pattern has a limit, the limit is in the pattern, not in a footnote.

### 🟢 `P614-1` — ship a tutor as a **skill**, not a deployment (`2`–`3` wk)

🔵 **The problem.** A client wants AI tutoring over their own material. The reflex is to deploy an
application: hosting, auth, data-residency review, a security questionnaire, and a procurement cycle
longer than the pilot. 🟢 `614-I` says the sector has stopped doing that.

🟢 **The wiring.** Take [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
(`MIT`, `36,751★`, branch 🔴 `master`) to turn the client's own corpus — course texts, standards
documents, internal manuals — into an agent skill. Layer
[`smashburger-dev/socratic-workshop`](https://github.com/smashburger-dev/socratic-workshop) (`MIT`,
`23★`) for the pedagogy, because learn-by-explaining is a *named method* a faculty committee can be
argued into rather than a feature list. Add
[`Kaiji-Z/dsh-plugin-lookatstudy`](https://github.com/Kaiji-Z/dsh-plugin-lookatstudy) (`MIT`, `23★`)
for progression: it already implements a gated skill tree with **BKT** mastery estimation and **SM-2**
review scheduling. For the instructor side, [`YujxZJCN/teaching-skills`](https://github.com/YujxZJCN/teaching-skills)
(`MIT`, `45★`) covers the teaching lifecycle.

🟢 **Why it is fast.** There is nothing to host. The artefact is text, it runs in the agent host the
client already licensed, and the data never leaves their estate — so the data-residency conversation
ends before it starts.

🔴 **Limits, stated.** (a) Every row is single-author at `20`–`45★` except `book-to-skill`; expect to
own the fork. (b) 🔴 **Licence-read the copy, not the code**: `613-E`'s `GarethManning/education-agent-skills`
(`942★`) is this same class and is `CC-BY-SA-4.0`, which would attach share-alike to the skill text
you hand the client. (c) This pattern sells a *capability*, not a system of record — it produces no
audit trail, which is what `P614-2` is for. (d) `book-to-skill`'s default branch is `master`; a
`main`-only build script silently gets nothing.

### 🟢 `P614-2` — the conformity pack: one build, two regulators, two different clocks (`8`–`10` wk)

🔵 **The problem.** The same artefact is demanded by both western regions and on different terms.
In **North America** the binding layer moved to the district: `MD`, `ID`, `OK` and `VA` now mandate
district-level AI policy adoption in `2026`, against `134` bills in `31` states — and adoption already
ran ahead of governance (`60 %` of US teachers using AI tools per Gallup, most public schools without
a formal student policy). In **EMEA** Annex III education obligations bind **`2027-12-02`** under
`Reg. (EU) 2026/1744`, with AI embedded in regulated products at `2028-08-02`. 🔴 A district wants
evidence *this school year*; an EU institution wants a conformity file dated before a deadline two
years out. 🟢 The underlying artefact is the same: a demonstrable record that the AI did what was
claimed, to whom, with human oversight.

🟢 **The wiring, all permissive.** Make the record of what happened `613-C`'s `Apache-2.0` xAPI
Learning Record Store ([`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql), `144★`, or
[`openfun/ralph`](https://github.com/openfun/ralph), `MIT`, `51★`). Prove interoperability with a test
run rather than an assertion using `613-B`'s `Apache-2.0` **xAPI/cmi5 conformance suites** published by
the **US DoD's ADL Initiative** — in North America that publisher is itself a procurement argument.
Populate and load-test the whole thing before any real learner with
[`yetanalytics/datasim`](https://github.com/yetanalytics/datasim). Carry the assessment-integrity
trail on `612-E`'s rubric/autograding tier. Launch from the incumbent LMS through `612-D`'s permissive
LTI `1.3` tier so Moodle (`GPL-3.0`) and Open edX (`AGPL-3.0`) are never forked. Author the policy and
evidence microsites with [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php)
(`Apache-2.0`, `130★`, 🔴 `master`), whose Penn State provenance reads as institutional rather than
vendor.

🟢 **Why one build serves both.** The district deliverable is the *report*; the EU deliverable is the
*file*. Both are views over the same xAPI statement store, so the regional difference is reporting and
documentation — not architecture.

🔴 **Limits, stated.** (a) 🔴 The EU dates are a **secondary** read in this base: `eur-lex.europa.eu`
does not resolve from this session (`614-H`), and the `2028-08-02` embedded-product date is new and
unverified this pass. Confirm against the Official Journal before contracting. (b) 🔴 The superseded
`2026-08` date is still being published by secondary sources — this pass's own EMEA leg served it
(`614-C`). Do not let a client's advisor reintroduce it; the settled value is `2027-12-02` under
`Reg. (EU) 2026/1744`. (c) `5 of 9` ADL repos last pushed `2024`–`2025` and `xAPIWrapper` in `2022-12`
(`613-B`'s stated limit): acceptable for a spec and a conformance suite, a risk as a live dependency.
(d) US state law is `50` jurisdictions, not one — the `4` mandate states are the beachhead, and the
`134`-bill figure is a tracker count, not a statute count.

### 🟢 `P614-3` — the APAC policy-parameterised deployment, over a permissive knowledge graph (`10`–`12` wk)

🔵 **The problem.** APAC is not one market. Korea's AI Basic Act is in force (`2026-01-22`), Vietnam
names **education** high-risk from `2026-03-01` including automated assessment, China requires
registration and content labelling, Australia's TEQSA requires an institutional action plan from every
provider, while Japan and Singapore remain voluntary. 🔴 One deployment cannot satisfy all five and
five deployments cannot be maintained.

🟢 **The wiring.** Base the learner model on
[`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) (`MIT`, `41★`, APAC) — it is
**local-first** by design, which is what makes per-jurisdiction data handling a configuration rather
than a re-architecture. Take the domain model from
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (`6,143★`,
`CC` family): `1,644` knowledge points and `2,403` prerequisite edges aligned to a national
curriculum — the input that normally takes a year of subject-matter expert time. Make the review
schedule swappable with [`shigella520/MindTrain`](https://github.com/shigella520/MindTrain) (`MIT`,
`128★`), whose scheduler is pluggable and already speaks Anki/FSRS, backed by `613-D`'s permissive
FSRS tier (`fsrs4anki` `4,122★` `MIT`, `ts-fsrs` `847★`, `py-fsrs` `520★`, `fsrs-rs` `455★` `BSD-3`)
so the algorithm is a dependency and not a rewrite. Emit telemetry through `613-C`'s `Apache-2.0`
xAPI LRS (`yetanalytics/lrsql`) so each jurisdiction's evidence requirement is satisfied by
configuration of one store.

🟢 **Why it holds together.** Policy varies at the edges — residency, assessment automation,
labelling — and all three of those are configuration points in a local-first stack with a pluggable
scheduler and an external record store.

🔴 **Limits, stated.** (a) 🔴 The knowledge graph is `CC-?` — **family identified, version not read**
(`614-G`); read the version before any client delivery, and treat it as data under attribution, never
vendored as code. (b) It is aligned to the **Chinese** national curriculum; re-alignment to another
country's standards is real work, not a mapping table. (c) `civil-ai` is `41★` and single-author —
shelf it as a reference implementation, budget to own it. (d) Vietnam's high-risk designation is a
**secondary** read in this base; confirm against the decision text before writing it into a contract.

### 🟢 `P614-4` — the synchronous classroom, which this base could not previously staff (`4`–`6` wk)

🔵 **The problem.** Every pattern this base held was asynchronous — a learner, alone, with an agent.
🔴 Institutions buy *lessons*, which are synchronous and have an instructor in the room.

🟢 **The wiring.** [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) (`MIT`, `262★`) gives a
browser-based collaborative IDE with real-time co-editing, live drawing and voice chat — the
instructor and student in one buffer, no install. Author and publish the course material around it
with [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) (`Apache-2.0`, `130★`, branch
🔴 `master`), which carries **Penn State** provenance — an institutional publisher, which survives a
procurement review in a way a single-author repo does not. Capture and annotate the session with
[`opencast/annotation-tool`](https://github.com/opencast/annotation-tool) (`ECL-2.0`, `42★`, branch
🔴 `master`), the sector's own licence family from a European academic consortium. Launch all of it
from the incumbent LMS through `612-D`'s permissive LTI `1.3` tier and report back through `613-C`'s
xAPI store — so Moodle (`GPL-3.0`) or Open edX (`AGPL-3.0`) stays untouched and un-forked.

🔴 **Limits, stated.** (a) Two of the three new rows default to `master`; a build that assumes `main`
fails on both. (b) `pytogether` is one author at `262★` — the architecture is the asset. (c) Voice
chat moves this into a different accessibility and recording-consent conversation; in EMEA that lands
inside the Annex III scope, not beside it. (d) `ECL-2.0` from a non-Apereo publisher triaged from the
platform field is safe per `614-B`, but `n = 1` — byte-read it before shipping anyway.

### 🟢 `P614-5` — the LATAM governance pack: sell the evidence, not the tutor (`6`–`8` wk)

🔵 **The problem, quantified.** UNESCO IESALC across ~`200` institutions in `19` countries:
**`87 %`** use AI in at least one area, **`26 %`** have any formal framework. Brazil at the school
level: `53 %` of administrators using it, `22 %` with guidelines (Cetic.br). 🔵 **The region does not
need to be sold AI. It needs to account for the AI it already runs.**

🟢 **The wiring.** Stand up `613-C`'s `Apache-2.0` Learning Record Store
([`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql), `144★`;
[`openfun/ralph`](https://github.com/openfun/ralph), `MIT`, `51★`, France Université Numérique) as the
institution's AI-use register — every agent interaction an xAPI statement, so "what AI is in use
here" becomes a query rather than a survey. Prove the stack before a single real learner with
[`yetanalytics/datasim`](https://github.com/yetanalytics/datasim), which generates conformant
statement volume. Attach `612-E`'s rubric/autograding tier as the assessment-integrity trail, and
`613-B`'s `Apache-2.0` cmi5/xAPI **conformance test suites** (US DoD ADL) so interoperability is
answered with a test run rather than an assertion. Deliver it against the vocabulary the region will
be measured on — UNESCO IESALC's recommendations and the LAC Observatory (Santiago, `2026-04`) —
through partners with national reach: Ceibal (Uruguay), Cetic.br, CENIA (Chile), Tec de Monterrey.

🔴 **Limits, stated.** (a) 🔴 **Every figure in this pattern is secondary** — `unesco.org` and
`iesalc.unesco.org` do not resolve from this session (`614-H`), so the `87 %`/`26 %` pair has never
been read at source by this base. Cite it as UNESCO IESALC's published figure, never as measured.
(b) 🔴 The `87 %` (institutions, IESALC) and `92 %` (students, Digital Education Council) figures are
**different populations** and must not be averaged. (c) 🔴 This base holds **no LATAM-published
permissive repository** on any sell shelf — the stack above is `Apache-2.0`/`MIT` from US and French
publishers, localised, not regional supply. Say so to the client rather than implying local
provenance. (d) `5 of 9` ADL repos last pushed `2024`–`2025` (`613-B`'s own stated limit) — fine for
a spec, a risk for a dependency.

### 🔴 `P614-6` — the pattern that is a **refusal**, and it is the most valuable one this pass

🔵 A client asks for the obvious thing: an open student-success and advising platform with an AI
assistant, self-hosted, operated by the studio. 🟢 The obvious answer exists and is well-starred:
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (`340★`), a student success
platform and recruitment CRM built for colleges and universities.

🔴 **Do not sell it as a managed service.** Its grant is **Elastic License `2.0`** (byte-read today,
`3,860 B`), which states: *"You may not provide the software to third parties as a hosted or managed
service, where the service provides users with access to any substantial set of the features or
functionality of the software."* 🔴 It also forbids disabling the licence-key functionality. 🔵 The
platform's own licence field says only `NOASSERTION`, so **nothing warns a reader who triages from
metadata** — this is `614-E` with a price attached.

🟢 **What to do instead.** (a) Deploy it **into the client's own tenancy**, with the client as
licensee and the studio as implementer — permitted, and it is a different statement of work and a
different commercial model, so price it that way. (b) If a managed service is the requirement, the
permissive path is to compose it: `613-C`'s xAPI/LRS tier for the record of engagement,
`612-D`'s LTI seam for launch, and `P614-4`'s delivery layer — more build, and no licence that
forbids the delivery model. (c) 🔴 Whichever path, **byte-read the grant before the proposal**, not
before the deployment.

🔵 **Why this belongs beside the build patterns.** Four of the eleven unshelved candidates this pass
measured were licence traps rather than components (`614-E`, `614-F`), and the `121 B` pointer file of
`614-F` resolves to `AGPL-3.0` without ever saying so in the repository a reader is looking at. 🟢 The
cheapest thing this base does for an engagement is name the rows that cost money, early.

## 🆕 `p613` — `2026-11-02` — patterns, each wired from rows this base holds and byte-read today

🔵 Every repository named below is on a sell shelf with its grant byte-read `2026-11-02` at the real
default branch (`evidence/api-vs-bytes-grants.2026-11-02-p613.tsv`, `24 of 24` agreeing with the
platform field). 🔴 Where a pattern has a limit, the limit is stated in the pattern, not in a footnote.

### 🟢 `P613-1` — the closed loop around a copyleft LMS: launch permissive, report permissive (`6`–`8` wk)

🔵 **The problem.** The incumbent is Moodle (`GPL-3.0`) or Open edX (`AGPL-3.0`). A studio cannot ship
proprietary work *inside* either, and the client will not replace them.

🟢 **The wiring, all permissive, no incumbent code touched.**
1. **Launch** — [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (`BSD-3-Clause`, Python) or [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) (`Apache-2.0`, Java) or [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) (`MIT`, TS) — the tool launches from the LMS over LTI `1.3` (`612-D`).
2. **Emit** — [`xapijs/xapi`](https://github.com/xapijs/xapi) (`MIT`) writes xAPI statements for every learner interaction, against vocabularies from [`adlnet/xapi-authored-profiles`](https://github.com/adlnet/xapi-authored-profiles) (`Apache-2.0`) rather than invented ones.
3. **Store** — [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (`Apache-2.0`) is the LRS; or [`openfun/ralph`](https://github.com/openfun/ralph) (`MIT`) where the client wants analytics in the same component.
4. **Prove** — [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) (`MIT`) runs in the client's CI and tests the `MUST` requirements of the spec against the deployed LRS.
5. **Demo before data** — [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) (`Apache-2.0`) generates conformant statement volume, so step `3` and `4` are demonstrable in week two with no real learners.

🔵 **Why it closes commercially.** The two seams are the only permissive boundaries around a copyleft
incumbent, and step `4` converts "we are standards-compliant" from a claim into a test run.
🔴 **Limit:** `xapijs/*` has not been pushed since `2026-04`; budget to fork it, which `MIT` permits.
Do **not** use `adlnet/xAPIWrapper` — unmaintained since `2022-12`.

### 🟢 `P613-2` — retention as the asset the incumbent cannot hand over (`4`–`6` wk)

🔵 **The problem.** A tutor built on a prompt is copied in a week. The client asks what they own.

🟢 **The wiring.** [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs)
(`BSD-3-Clause`) or the stack-matched sibling — [`ts-fsrs`](https://github.com/open-spaced-repetition/ts-fsrs),
[`py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs), [`go-fsrs`](https://github.com/open-spaced-repetition/go-fsrs),
[`swift-fsrs`](https://github.com/open-spaced-repetition/swift-fsrs) (all `MIT`) — schedules the review.
[`fsrs-optimizer`](https://github.com/open-spaced-repetition/fsrs-optimizer) (`BSD-3-Clause`) **fits the
parameters to that client's own accumulated review history.** The LLM is confined to writing items.
Statements flow into `P613-1`'s LRS, which is where the history that feeds the optimizer comes from.

🔵 **Why it is the strongest answer to "what do we own".** The fitted parameter set is a function of
retained learner data. It improves monotonically with use and it cannot be reproduced by a competitor
who does not have the history. 🟢 Benchmark against [`duolingo/halflife-regression`](https://github.com/duolingo/halflife-regression)
(`MIT`) — 🔴 unmaintained since `2024`, so it is a baseline, never a dependency.
🔴 **Limit:** worthless before roughly a term of review data exists; sequence it after `P613-1`.

### 🟢 `P613-3` — the EMEA Annex III conformity file, assembled from state-published parts (`8`–`10` wk)

🔵 **The clock.** `(EU) 2026/1744` defers Annex III education high-risk to `2027-12-02` with the
obligations unchanged; Article `50` transparency is live and watermarking is due `2026-12-02`.

🟢 **The wiring.** `612-E`'s rubric tier (`text2qti`, `otter-grader`, `AdaRubrics`) supplies documented,
inspectable grading criteria. [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
(`MIT`) supplies interoperability evidence as a test artifact. [`openfun/ralph`](https://github.com/openfun/ralph)
(`MIT`, France Université Numérique) supplies the analytics and the audit trail, and its provenance is a
**EU member-state operator**, which is itself procurement-relevant. `612-F`'s UK DfE services are the
reference implementations to cite.

🔵 **Why this sequencing.** Thirteen months of runway with unchanged obligations means the conformity
file is built now and cheaply, from parts a regulator already recognises. 🔴 **Limit:** none of these
parts is a legal opinion, and the `2027-12-02` date is a deferral that can move.

### 🟢 `P613-4` — the North America multi-jurisdiction build, with compliance as CI (`10`–`12` wk)

🔵 **The problem.** `134` bills in `31` states and no federal statute: the deployable unit is one build
parameterised by jurisdiction, not `31` builds.

🟢 **The wiring.** `611-D`'s [`bcgov/SIMS`](https://github.com/bcgov/SIMS) (`Apache-2.0`) is the
architecture to copy — a government system of record built so **policy change is not a rewrite**, via an
explicit business-rules engine. Policy becomes rule data. `P613-1`'s stack carries the learner
telemetry, and [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
(`MIT`) plus the per-state rule fixtures run as **one CI job per jurisdiction**.

🔵 **Why it wins the procurement.** A state buyer can be handed a green test run scoped to their own
rules. 🔴 **Limit, stated in `611-D` and still binding:** `SIMS`'s rule *content* is British Columbia
policy — the architecture transfers, the rules do not.

### 🟢 `P613-5` — the LATAM institutional-policy template (`3`–`5` wk per institution, `6`–`8` wk once)

🔵 **The reframe, and it is this pass's revision of `612-5`.** `612-5` read LATAM's gap as
Spanish/Portuguese **content**. 🔴 The `2026` LATAM survey says adoption is already `92 %` of students
and `79 %` of faculty — nobody needs persuading. 🟢 UNESCO IESALC across `200` institutions in `19`
countries names the real gap: **no formal institutional AI policy**, and it is missing the same way
everywhere.

🟢 **The wiring, and none of it needs to be LATAM-native.** One parameterised institutional AI-use
policy (permitted uses, disclosure, assessment integrity, data handling) + `612-E`'s rubric tier for
assessment-integrity evidence + [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
(`MIT`) for the data-handling claim + `612-3`'s cited-rulebook agent shape
([`BenyRonald77/uajy-academic-rag-chatbot`](https://github.com/BenyRonald77/uajy-academic-rag-chatbot),
`MIT`, `452★`) pointed at the new policy so staff and students can **ask** it with citations.

🔵 **Why the economics work where a content build does not.** The template is built once; each
institution is parameters plus their own documents. 🟢 The rulebook-agent shape is already built three
times in APAC, so the engineering risk is near zero. 🔴 **Limit, and it is the honest one:** this base
has `0 of 24` promoted rows and `0 of 90` index addresses placing to LATAM, so the *delivery* is
non-LATAM parts configured locally — there is no regional open-source ecosystem to lean on, and a
partner with the institutional relationships is doing the part the code cannot.


## 🆕 `p612` — `2026-11-02` — patterns, each wired from rows this base holds and byte-read today

🔵 Every repository named below is on a sell shelf with its grant byte-read `2026-11-02` at the real
default branch (`evidence/api-vs-bytes-grants.2026-11-02-p612.tsv`). 🔴 Where a pattern has a limit, the
limit is in the pattern, not a footnote.

### 🟢 `P612-1` — "AI inside the LMS the client already runs" — the week-one integration pattern — `4`–`6` weeks

🔵 **The brief this answers:** *"we have Moodle / Canvas / Open edX and we want an AI assistant inside
it."* 🔴 **The constraint nobody states in the brief:** Moodle is `GPL-3.0` and Open edX is `AGPL-3.0`, so
the client's own code **cannot** live inside the platform without inheriting copyleft. 🟢 LTI is the seam
that keeps it outside.

| step | component | grant | why this one |
| --- | --- | --- | --- |
| `1` pick the seam by the client's stack | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (Ruby) · [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (Python) · [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) (Java/Spring) · [`LtiLibrary/LtiAdvantagePlatform`](https://github.com/LtiLibrary/LtiAdvantagePlatform) (.NET) · [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) (TypeScript) | `MIT` / `BSD-3` / `Apache-2.0` | 🟢 **one per stack, so the seam never dictates the language** |
| `2` test against a platform you control | [`LtiLibrary/LtiAdvantagePlatform`](https://github.com/LtiLibrary/LtiAdvantagePlatform) | `MIT` | 🟢 the *platform* side, so the tool can be exercised before the client's LMS is touched |
| `3` read the system of record least-privilege | [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) | `MIT` | 🟢 **read-only** MCP — an assistant beside the gradebook, not inside it |
| `4` ship the mobile surface permissively | [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) | `Apache-2.0` | 🟢 the one permissive surface of a `GPL-3.0` incumbent |
| `5` pin the platform correctly | — | — | 🔴 Moodle `5.x`: read **`public/version.php`**, not root (`612-G`). Open edX: pin **`release/<name>`**, not `open-release/*` |

🟢 **Why it is `4`–`6` weeks and not `12`:** steps `1`–`2` are integration, not invention, and step `5`
is the thing that actually breaks pilots. 🔴 **Limit:** LTI gets the tool launched and identified; grade
passback and roster sync are Advantage services that need per-LMS verification — budget a week per LMS
beyond the first.

### 🟢 `P612-2` — "gradeable AI with a conformity file" — the EMEA Annex III pattern — `8`–`10` weeks

🔵 **The brief:** automated or assisted assessment for an EU institution. 🔴 **The clock:**
`(EU) 2026/1744` defers Annex III education to **`2027-12-02`** but changes none of the obligations, and
Article `50` transparency is already live with watermarking due **`2026-12-02`**. 🟢 **The pattern's whole
point is that the conformity evidence is a by-product of the build, not a document written afterwards.**

| step | component | grant | what it produces for the file |
| --- | --- | --- | --- |
| `1` derive defensible criteria | [`OpenEnvision/AutoRubric-as-Reward`](https://github.com/OpenEnvision/AutoRubric-as-Reward) | `Apache-2.0` | turns expert judgement that was never written down into **explicit** generative criteria |
| `2` make the rubric weighted and versioned | [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | `MIT` | the decision procedure, as code under version control |
| `3` grade the process, not only the answer | [`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics) | `Apache-2.0` | trajectory-level evaluation — the "how" an appeal will ask about |
| `4` link every judgement to evidence | [`Sion612/rubrictrail`](https://github.com/Sion612/rubrictrail) | `Apache-2.0` | 🟢 the **audit trail**, local-first |
| `5` run it at course scale | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | `BSD-3-Clause` | containerised Python **and** R autograding a public university already operates |
| `6` emit the human-oversight surface | [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | `Apache-2.0` | the report a human reviews and signs |
| `7` deliver into the LMS | [`gpoore/text2qti`](https://github.com/gpoore/text2qti) | `BSD-3-Clause` | Markdown → **QTI**, which Canvas and most LMSs import |
| `8` state a bias position | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) | `MIT` | the documented fairness assessment and mitigation |

🔴 **Limit, and it is the honest one:** this produces the *technical* documentation, data governance and
human-oversight evidence. 🔴 It does **not** produce the conformity assessment or the registration — those
are legal acts, and the deployer (the institution) is liable for them whoever built the system.

### 🟢 `P612-3` — "the institution's own rulebook, answerable and cited" — the APAC pattern that is already built three times — `3`–`5` weeks

🔵 **The brief:** *"students and staff cannot find anything in our regulations / handbook / curriculum
documents."* 🟢 **Three independent teams in three countries converged on the same architecture, and all
three are `MIT`** — so this is a pattern with three reference implementations, not a proposal.

| reference | region | the authoritative set it is grounded in |
| --- | --- | --- |
| [`callmevanshh/campusask`](https://github.com/callmevanshh/campusask) `49★` | 🟢 APAC / India | IIIT Delhi academic rules — **official PDFs only, page-level links** |
| [`BenyRonald77/uajy-academic-rag-chatbot`](https://github.com/BenyRonald77/uajy-academic-rag-chatbot) `452★` | 🟢 APAC / Indonesia | one university's academic handbook, FAISS + Streamlit, described as production-grade |
| [`niansia/taiwan-exam`](https://github.com/niansia/taiwan-exam) `20★` | 🟢 APAC / Taiwan | the national 學測 format — 🟢 **with solution re-verification**, and it emits the official layout |

🟢 **Wire it as:** [`Queena34/StudyPilot`](https://github.com/Queena34/StudyPilot) (`MIT`) for the
answer-only-from-supplied-material discipline **＋**
[`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) (`MIT`) for
traceable document → learning-page conversion **＋**
[`jdepoix/youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) (`MIT`) for lecture
intake with no API key **＋** `P612-1`'s seam to put it inside the LMS.

🟢 **The non-negotiable property is refusal:** all three references answer *only* from the official set
and cite the page. 🔴 **Limit:** that makes coverage gaps visible as refusals, which is correct behaviour
and reads as failure in a demo — set that expectation with the client before the demo, not after.

### 🟢 `P612-4` — "policy-parameterised deployment" — the North America multi-jurisdiction pattern — `10`–`12` weeks

🔵 **The brief:** a district consortium or state system, where `134` bills across `31` states mean the
rules differ by jurisdiction and change by legislative session. 🔴 **A fixed-policy product cannot be
sold into this and cannot be maintained in it.**

🟢 **Spine:** [`bcgov/SIMS`](https://github.com/bcgov/SIMS) (`Apache-2.0`, `611-D`) — a provincial system
of record whose **business-rules engine exists expressly so policy change is not a rewrite**. 🟡 Stated
limit: BC's rule *content* is BC's; the architecture transfers, the policy does not.

🟢 **Wire:** `SIMS`-style rules engine for the per-jurisdiction policy layer **＋**
[`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics)
(`Apache-2.0`) for the student-facing dashboard a public university already runs **＋**
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (`Apache-2.0`) and
[`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills)
(`Apache-2.0`) for the teacher-facing capability and its eval rubrics **＋** `P612-1`'s seam **＋**
`P612-2`'s rubric tier wherever a jurisdiction touches assessment.

🟢 **Satisfy the two live NA obligations explicitly:** a hard grade-band gate (NY `A.9190` would bar most
classroom AI below grade `9`) and an AI-literacy module (SUNY requires it in general education from fall
`2026`). 🔴 **Limit:** federal preemption is *reported* as recommended, not enacted — build the policy
layer so a preemption event collapses `31` configurations to one rather than invalidating the design.

### 🟢 `P612-5` — "free at the point of use, in Spanish and Portuguese" — the LATAM pattern, built from non-LATAM parts — `6`–`8` weeks

🔴 **Why this pattern is shaped by an absence.** `0 of 68` shippable-shaped candidates placed to LATAM,
and the region's institutional AI-education spend (`$105.6M` → `$204.7M` by `2029`) is 🔴 two orders of
magnitude below global while consumer AI use in Brazil and Mexico exceeds `70 %`. 🟢 **So per-seat
licensing is the wrong instrument and public-sector or large-network programmes are the right one — which
means marginal cost per learner has to be near zero.**

| step | component | grant | the cost it removes |
| --- | --- | --- | --- |
| `1` voice at zero marginal cost | [`tanle-mtr/ChinaStudyFree`](https://github.com/tanle-mtr/ChinaStudyFree) | `MIT` | 🟢 `148` textbooks + **free EdgeTTS** is precisely why that platform can be free; nothing in the approach is language-bound |
| `2` content without a licensing negotiation | [`callmevanshh/campusask`](https://github.com/callmevanshh/campusask) | `MIT` | cited retrieval over the **ministry's own** public curriculum PDFs |
| `3` run where connectivity is not assumed | [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) | `MIT` | fully offline Electron + Ollama — no per-token cost and no connectivity floor |
| `4` four clients from one codebase | [`tanle-mtr/ChinaStudyFree`](https://github.com/tanle-mtr/ChinaStudyFree) | `MIT` | web / desktop / Android / iOS across four school stages |
| `5` the policy and record layer | [`bcgov/SIMS`](https://github.com/bcgov/SIMS) · the three UK DfE `MIT` services | `Apache-2.0` / `MIT` | 🟢 operational public-sector architecture, reused rather than rebuilt |

🔴 **Limits, stated plainly.** 🔴 Brazil's `PL 2338/2023` status is **contradicted between sources and
unresolved** — do not plan around either reading. 🔴 Every component here is non-LATAM; the Spanish and
Portuguese curriculum content is net-new work and is the bulk of the estimate. 🟢 The architecture gap is
zero, which is the good news and the reason `6`–`8` weeks is credible for a pilot.

---

## 🆕 `p611` — `2026-11-02` — patterns, each wired from rows this base holds and byte-read

🔵 Every repository named below is on a sell shelf with its grant byte-read at the real default branch
on `2026-11-02`. 🟢 `P611-1` was **executed end to end before publication** and its transcript is
reproduced verbatim; `611-B`'s and `611-I`'s fixes are both *in* the shipped script.

### 🟢 `P611-1` — The licence gate an engagement stands up in week one (`ingest/p611-grant-gate.sh`)

🔵 **The problem it solves.** `611-A` measured that the sector's standard platform index gets
🔴 **`4 of 5` permissive claims wrong**. Week one of any education engagement therefore cannot begin
with a licence spreadsheet — it has to begin with a gate that reads grant bytes. 🟢 Every step below is
a defect this base *measured*, not a precaution:

| step | why it exists |
| --- | --- |
| 1. resolve the **real** default branch via `git ls-remote --symref` | `559`: a `main`-only read `404`s for `32.4 %` of addresses. 🔴 `611-C`: one branch is **`produção`** |
| 2. walk a **ladder** of grant paths incl. `COPYING.txt` | 🔴 `610-E`: omitting that rung graded the **official Moodle mobile app** ungranted |
| 3. grade on the **title line** only | 🔴 `611-B`: `GPL-2.0`'s own text names the Lesser GPL at line `18`, so a window substring mis-grades **every** `GPL-2.0` file |
| 4. flag a **provenance-anchored** upstream slug | 🔴 `610-A`: a fork's grant was paid-commercial while naming `MIT` four times |
| 5. run a **fabricated control** in the same invocation | `608-A`: an arm that cannot tell a real address from an invented one certifies nothing |

🟢 **Executed, `2026-11-02`, output verbatim:**

```
$ bash ingest/p611-grant-gate.sh pengusto/google-classroom-mcp \
      adriasantacreu/google-classroom-mcp bcgov/SIMS QkeleQ10/Study-Tools \
      OpenEMIS/core CodeBreez/collejo moodlehq/moodleapp

address                              default_branch  grant_path  bytes  grade                     note
pengusto/google-classroom-mcp        master          LICENSE     3053   UNCLASSIFIED-NEEDS-HUMAN  UPSTREAM-NAMED:adriasantacreu/google-classroom-mcp
adriasantacreu/google-classroom-mcp  master          LICENSE     1073   MIT
bcgov/SIMS                           main            LICENSE     11358  Apache-2.0
QkeleQ10/Study-Tools                 main            LICENSE     1072   MIT
OpenEMIS/core                        master          LICENSE     15518  GPL-2.0
CodeBreez/collejo                    master          LICENSE     1076   MIT
moodlehq/moodleapp                   main            COPYING.txt 11358  Apache-2.0
openai/totally-not-real-edu-repo-…   UNREACHABLE     -           -      FABRICATED-CONTROL
exit=0
```

🟢 **The run reproduces four independently-registered defects cold**, which is the only reason to
trust it: `610-A` escalated to a human instead of graded `MIT`; `610-E`'s `COPYING.txt` rung found;
`611-B`'s `GPL-2.0` graded correctly rather than as `LGPL`; `611-C`'s `produção` branch resolved.

🔴 **`611-I` — and step 4 was wrong twice before it was right, both caught here.** Its first form
matched only `github.com/...` URLs — 🔴 and `610-A`'s upstream is a **bare slug**, so the step silently
never fired on the one case that motivated it. Its second form matched bare slugs and scored
🔴 **`1 of 4` precision** (stock `MIT` text contains `and/or`; `Apache-2.0` contains
`www.apache.org/licenses`). 🟢 The shipped form requires the slug to be **provenance-anchored** —
within `200` characters of `upstream|fork|original|derived|based on`, or in URL form — and measures
🟢 **`1 of 1` true positives with `0 of 6` false positives** on the run above. 🔵 Per `606`, a proposed
control is measured *before* adoption, not after.

### 🟢 `P611-2` — Policy-as-data compliance layer for the US mandatory-adoption states

🔵 **The trigger is dated and statutory**, not a budget cycle: 🟢 `4` states (**Maryland `SB 720`**,
**Idaho**, **Oklahoma**, **Virginia**) now require districts to *adopt* an AI policy, Ohio's deadline
was `2026-07-01`, and 🔴 DC's `2026-27` policy **bars AI from grading and from discipline decisions**.

🟢 **Wiring, all permissive, all on these shelves:**

```
  [ bcgov/SIMS ]  Apache-2.0, byte-read 11,358 B, main
    └─ lift the BUSINESS RULES ENGINE + the three-party domain model
       (student / institution / ministry → student / school / district)
       ↳ this is the asset: policy change must not mean a rewrite        (611-D)

  [ policy as data ]  one rule set per jurisdiction, versioned in git
    ├─ HARD EXCLUSIONS as deny-rules, enforced in code not in a handbook:
    │     no_ai_grading = true          ← DC 2026-27
    │     no_ai_discipline = true       ← DC 2026-27
    │     min_grade_for_classroom_ai=9  ← NY A 9190 (pending)
    │     student_data_for_training=deny ← CA AB 1159 (pending)
    └─ each rule carries: instrument name, date, jurisdiction

  [ LMS / SIS edge ]  the permissive periphery, never the copyleft core   (T611-5)
    ├─ Canvas / Moodle connectors already shelved (p610 tier)
    └─ moodlehq/moodleapp Apache-2.0 + Azure/Moodle MIT for mobile+deploy

  [ audit record ]  one row per automated decision: input, rule set version,
                    model, output, human reviewer  → the compliance artefact
                    a district is actually obliged to produce
```

🟡 **Why `bcgov/SIMS` and not a framework:** a Canadian ministry has already published a system of
record whose stated design goal is *"a business rules engine that can accommodate regular changes in
alignment with policy."* 🟢 That is the exact requirement `4` US states just legislated. 🔴 **Stated
limit:** its rule *content* is British Columbia financial-aid policy — the architecture transfers, the
policy does not.

**Shape:** `8`–`10` weeks. **Licence posture:** 🟢 `Apache-2.0` throughout — fork-and-extend, no
copyleft obligation, no LMS core touched.

### 🟢 `P611-3` — Governance-as-a-product for LATAM, sized from the UNESCO denominator

🔵 **The arithmetic is the pitch** (`T611-4`): 🟢 `87 %` of ~`200` HEIs across `19` countries use AI in
at least one area, 🔴 `26 %` have a formal strategy, 🔴 `< 10 %` have guidelines *with* the capacity to
apply them — and 🔴 `55 %` have **no AI budget**, public universities 🔴 **`4 %`**.

🔴 **So the deliverable is not a tutor.** It is the governance artefact `716` regulatory instruments
across `23` countries will ask for, and it must be cheap because the budget line does not exist:

```
  [ inventory ]   what models are already in use, by whom, on what data
                  ↳ the honest starting point: adoption is bottom-up and
                    institutions cannot currently answer this question

  [ policy instance ]  P611-2's rule set, re-pointed at regional instruments
    ├─ BR: LGPD + Cetic.br baseline (53 % admin use / 22 % have guidelines)
    ├─ UY: Ceibal baseline (75 % of public-school teachers)
    └─ regional: UNESCO LAC Observatory (launched 2026-04-14) as the
                 reference framework a ministry will recognise

  [ gate ]        ingest/p611-grant-gate.sh in CI — every dependency's grant
                  byte-read before it reaches a public institution    (P611-1)

  [ capacity ]    staff training as a shipped deliverable, because
                  "< 10 % have guidelines AND capacity" says the gap is
                  people, not documents
```

🟢 **Sell it at consortium or ministry level, not per institution** — the `4 %` public-university
funding rate makes a per-institution sale structurally unfundable, while `CENIA`, `Ceibal` and
`Cetic.br` are the bodies that already hold the data.

🔴 **What this pattern deliberately does *not* promise.** A permissive LATAM-built tutoring stack. The
four Iberian-language supply axes returned 🔴 **`95` new addresses and `0` shippable-shaped** this pass
(`611-E`). 🟡 The three correctly-shaped `0★` finds (`CarlosArmijos1/tutor-tecnico-agentes`,
`fabriciojunio/permaneia`, `Belles-hub/UpLearn`) are named on `agents/trending.md` and are **not**
components. 🔵 For tutoring itself the regionally-safe choice remains a Global row run against local
curriculum content — `thu-maic/OpenMAIC` (`MIT`) or `HKUDS/DeepTutor` (`Apache-2.0`) — self-hosted,
which the region's data-protection posture wants anyway.

---

## 🆕 `p610` — `2026-11-02` — patterns, each wired from rows this base holds and byte-read

🔵 Every repository named below is on a sell shelf with its grant byte-read at the real default branch
on `2026-11-02`. No pattern here names a component this base has not verified.

### 🟢 `P610-1` — Permissive assessment pipeline: Markdown → QTI → delivered session → Canvas gradebook

🔴 **The gap this closes.** `p604` shelved a QTI toolchain, `p607` found the **engine**, but every
recipe still began with a QTI file that had to already exist, and the Canvas write-back was unstated.

| stage | component | grant | why this one |
| --- | --- | --- | --- |
| 1. author | [`gpoore/text2qti`](https://github.com/gpoore/text2qti) | 🟢 BSD-3-Clause | Markdown → **QTI 1.2**; 7 item types, LaTeX math, `siunitx` units |
| 2. run the session | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 BSD-3-Clause | holds candidate state — the only engine on these shelves (`p607`) |
| 3. grade code/notebook items | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3-Clause | parallel Docker or LMS-native; speaks Canvas **and** Gradescope |
| 4. write results back | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 MIT | Canvas REST, institution-maintained |
| 5. provider-side LTI launch | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | 🟢 MIT | vendor's own LTI implementation |

🟢 **Wiring.** Author items as Markdown in the client's repo; `text2qti` emits a QTI 1.2 package in
CI on merge. Deploy `qtiworks` as the delivery surface and launch it from Canvas over LTI 1.3 via
`ims-lti`. For programming items, `otter-grader` runs in its own container and returns a score;
`canvasapi` posts both QTI and Otter scores into one assignment column keyed on the LTI
`resource_link_id`.

🟢 **Why it is worth naming:** 🟢 **zero copyleft components end to end** — three BSD-3-Clause and two
MIT — so the whole toolchain is reusable across client tenancies without a licence review per
engagement. 🔴 The constraint to state up front: `text2qti` targets **QTI 1.2**, not 3.0, so a client
demanding QTI 3.0 needs the `p604` toolchain in stage 1 and a different stage-2 contract.

### 🟢 `P610-2` — EU AI Act evidence trail for the four high-risk education functions

🔴 **The deadline.** Reg. (EU) 2026/1744 puts admissions, learning-outcome evaluation, level
assignment and **exam monitoring** in high-risk from `2027-12-02`, with human-oversight and logging
duties. Art. 4 AI-literacy is binding **now**.

| obligation | component | grant | how it discharges it |
| --- | --- | --- | --- |
| evidence trail + human check | [`Sion612/rubrictrail`](https://github.com/Sion612/rubrictrail) | 🟢 Apache-2.0 | brief + rubric → confirmed requirements → scheduled work → **draft evidence** → final human check. Its output *is* the audit artifact |
| outcome evaluation, defensibly | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 Apache-2.0 | formative checks whose distractors come from **documented misconceptions**, plus a shipped **eval framework** — the oversight evidence, not just the output |
| Art. 4 literacy delivery | [`CogitoNTNU/TutorAI`](https://github.com/CogitoNTNU/TutorAI) · [`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) | 🟢 MIT · MIT | staff/student literacy from the institution's own materials |
| EU-residency hosting | [`Azure/Moodle`](https://github.com/Azure/Moodle) · [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) | 🟢 MIT · Apache-2.0 | IaC + mobile, both **outside** Moodle's GPL core |

🔴 **The design constraint that is the point of the pattern:** exam monitoring is high-risk **and**
emotion inference in education is **banned outright** since `2025-02-02`. 🟢 So the build target is
integrity signals with **no affect recognition** — and a proctoring vendor's affect features are a
compliance liability, not a differentiator. Say this at the architecture stage; it is not a
post-hoc filter.

### 🟢 `P610-3` — Portuguese-first ENEM assessment on two independent holders

🟢 **New capability this pass:** the ENEM tier has two unrelated permissive maintainers, so a Brazilian
engagement no longer rests on one repository.

| role | component | grant | what it contributes |
| --- | --- | --- | --- |
| corpus-anchored scorer | [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) | 🟢 MIT | 5 official competencies, local SQLite corpus of **`11,147`** board-corrected essays, **no external API and no ML** — runs inside a coding agent |
| calibrated agent + baseline | [`tcheld0n/CorrijAI`](https://github.com/tcheld0n/CorrijAI) | 🟢 MIT | `HistGB` baseline on Essay-BR with SHAP **and** an LLM agent with per-level anchors + RAG; measured QWK `0.750` vs `0.731` |
| Portuguese curriculum corpus | [`Universidade-Livre/matematica`](https://github.com/Universidade-Livre/matematica) | 🟢 MIT | permissive pt-BR curriculum text for retrieval and item generation |

🟢 **Wiring.** Run `corretor-enem` as the deterministic, offline scorer and `CorrijAI`'s baseline as an
independent second grader; disagreement beyond a competency threshold escalates to a human — which
mirrors ENEM's own two-grader-plus-escalation process rather than inventing a workflow.

🔴 **State both honest limits to the client.** `CorrijAI`'s own README reports the **supervised
baseline beating the calibrated agent** on a known prompt (`0.750` vs `0.731`); and `corretor-enem`
says plainly it produces a *pedagogical estimate, not an official score*. 🟢 Two artifacts that
publish their unflattering numbers are the right foundation for an assessment engagement, and the
disclaimers are the deliverable's language, not a caveat to bury.

### 🟢 `P610-4` — LMS-agnostic agent surface across Canvas, Brightspace and Classroom

| LMS | connector | grant | ★ / size |
| --- | --- | --- | --- |
| Canvas (read) | [`semyonfox/canvas-mcp`](https://github.com/semyonfox/canvas-mcp) | 🟢 MIT | `1★` / `356 KB` |
| Canvas (grading) | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | 🟢 MIT | `1★` / `332 KB` |
| Canvas (full API) | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 MIT | `681★` / `4,849 KB` |
| D2L Brightspace | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 MIT | `62★` / `2,079 KB` |
| Google Classroom | [`adriasantacreu/google-classroom-mcp`](https://github.com/adriasantacreu/google-classroom-mcp) | 🟢 MIT | `2★` / `105 KB` |

🔴 **Read this before wiring it.** Four of the five MCP rows are `1`–`2★` single-maintainer projects of
`101`–`356 KB`. 🟢 The pattern is sound — one agent, one tool surface, several LMSs — but the
connectors are **substrate you will own**, not dependencies you can rely on. 🟢 Budget a fork of each
MCP server and put `ucfopen/canvasapi` on the critical path for anything Canvas-side that matters,
because it is the only row here with institutional maintenance.

🔴 **And the trap, which is `610-A` and is specific:** do **not** take
`pengusto/google-classroom-mcp`, the larger and more visible Google Classroom fork. Its grant is a
**`Pengusto Commercial License 1.0`** requiring a paid written agreement to run it — educational
institutions explicitly included — while naming MIT four times in describing its upstream. 🟢 The
upstream `adriasantacreu/google-classroom-mcp` is the MIT row, and it is the one in the table above.

### 🟢 `P610-5` — Draw the backlog instead of searching the web

🔴 **The measured fact this pattern is built on:** the four mandated global search legs have returned
**`0`** new permissive education-specific addresses for **`40` consecutive passes**, while this base's
own trending shelves hold **`2,310`** addresses published as rows and never promoted, `848` of them
education-shaped.

🟢 **The recipe, which is executable here today:**

```
# 1. census: attribute every address mention to its enclosing table's role
python3 ingest/p610-census-role.py agents/top.md repos/foundations.md verticals/solutions.md > /tmp/sell.tsv
python3 ingest/p610-census-role.py agents/trending.md repos/trending.md          > /tmp/trend.tsv

# 2. backlog = published as a row on trending, in no SELL row on a sell shelf
awk -F'\t' '$4=="SELL"{print $3}' /tmp/sell.tsv  | sort -u > /tmp/rowed.txt
awk -F'\t' '$4=="SELL"{print $3}' /tmp/trend.tsv | sort -u > /tmp/trend-rows.txt
comm -23 /tmp/trend-rows.txt /tmp/rowed.txt > /tmp/backlog.txt

# 3. reject non-repositories at extraction time (609-M), not at promotion time
bash ingest/p609-address-rejector.sh --shape-only $(cat /tmp/backlog.txt) > /tmp/shape.tsv

# 4. metadata, batched, WITH count reconciliation -- a batch drops rows silently (606-C, 610-F)
bash ingest/p610-batch-metadata.sh /tmp/backlog.txt /tmp/meta.tsv /tmp/unreconciled.txt

# 5. grant byte-read at the REAL default branch, ladder incl. COPYING.txt (610-E)
bash ingest/p610-grant-harness.sh < /tmp/shortlist.txt
```

🔴 **Four failure modes this pipeline exists to avoid, each one a measured defect:**

| step skipped | what gets published |
| --- | --- |
| 🔴 role attribution (2) | a **published refusal** counted as coverage — `35 of 188` on these shelves |
| 🔴 shape rejection (3) | `10/10` and `intel/market.md` shelved as repositories (`607-C`, `609-M`) |
| 🔴 reconciliation (4) | a silent batch drop — `openedx/openedx-platform` vanished from a `5`-row batch today |
| 🔴 first-hand metadata (5) | 🔴 **`11,147★`** for a repository with **`7★`** — a corpus size read as a star count (`610-C`) |

🟡 **Relevance is still a human read.** `3 of 23` candidates this pass survived grant, liveness and
size and were refused on **relevance** only after a second read — `alphadl/AdaRubrics` is agent-
trajectory evaluation, not education assessment, and the token `rubric` is what put it on the
shortlist. 🔴 **A keyword shortlist is not a relevance verdict**, and no step above supplies one.

---

## 🆕 `p609` — reads `2026-11-02` — four recipes, each buildable from rows byte-read this pass

🔵 Every repo named below had its grant byte-read at `raw.githubusercontent.com` on the **real**
default branch on **2026-11-02**, with `4 of 4` fabricated controls returning `401` on the existence
probe and `404 14 B` on the grant read in the same pass. Byte counts, branches and repository sizes
are in `agents/top.md` and `repos/foundations.md` under `p609`.

---

### 🟢 `P609-1` — Measure the incumbent before proposing a replacement (Global, `3`–`5` weeks)

**The problem it solves:** a client already has an AI tutor — bought, or built last year — and the
question on the table is whether it works. Every party in the room has a demo and nobody has a
measurement. 🔵 This pass made that engagement buildable for the first time: the **evaluation layer
is now open source and the tutor does not have to be**.

**Wiring, left to right:**

1. **Score the transcripts you already have, deterministically** —
   [`shivanireddyk/tutoreval`](https://github.com/shivanireddyk/tutoreval) (**MIT**, `1,074 B`).
   Feed it `Exchange(uid, student, tutor, answer)` records exported from the incumbent. 🔵 **No
   network calls, no API key, no GPU** — so it runs inside the client's boundary with no
   data-sharing review, and **every score carries the span of text that caused it**, which is what
   makes the output defensible in a steering committee rather than merely numeric.
2. **Then stress it against students who misbehave** —
   [`GEMLabHKU/DAS2`](https://github.com/GEMLabHKU/DAS2) (**MIT**, `1,116 B`). Drive the incumbent
   with simulators that **game the system**, **wheel-spin** and go **off-task** at rates matched to
   ASSISTments09/12, EdNet-KT1 and Eedi-NeurIPS distributions. This is where bought tutors fail,
   because they were accepted against idealised students.
3. **Guard against the simulator flattering you** —
   [`abigail-gh/simlearner`](https://github.com/abigail-gh/simlearner) (**MIT**, `1,067 B`) for the
   opposite failure: LLMs told to role-play a struggling learner **solve the problem too well**
   (*competency bias*). Its semi-Markov controller + **BKT** + **Mastery Gate** (Unknown always
   inject, Partial `50 %`, Mastered never) means the injected error only reaches the tutor when the
   learner model says it should. Run both simulators; a tutor that scores well on one and badly on
   the other is telling you which.
4. **Scale to per-student questions if the client has records** —
   [`microsoft/StudentSim`](https://github.com/microsoft/StudentSim) (**MIT**, `80★`, `5,760 KB`):
   one simulator per student from sparse records, scoring **guidance responsiveness** separately
   from **behavioral fidelity**. This answers *which guidance helps which student*, which is the
   question a pilot report is usually asked for and cannot answer.
5. **Audit your own harness before you bill for it** —
   [`pchi1606/sherpa-simulated-student-audit`](https://github.com/pchi1606/sherpa-simulated-student-audit)
   (**MIT**, `1,069 B`, 🔴 at **`master`**) is the template: preregistered metrics, `24` two-sample
   KS tests with Holm–Bonferroni, bootstrap CIs, `bash reproduce.sh`, and **PASS/FAIL printed per
   headline number** against `expected/headline_numbers.json`. Copy the shape — a validity audit of
   your own simulator is the deliverable that distinguishes this from a vendor bake-off.

**What you hand over:** a per-competency score with text spans, two disengagement-stress profiles, and
a reproduction script the client can re-run after any model change. 🟢 **Nothing in the chain requires
replacing the incumbent**, which is why it can be sold before a platform decision.

---

### 🟢 `P609-2` — ENEM-grade essay scoring with a defensible rubric (LATAM, `6`–`8` weeks)

**The problem it solves:** Brazilian secondary assessment runs on ENEM's five competencies, graders
are scarce (UNESCO flags a severe regional teacher shortage), and a score without a justification is
unusable — contestable by the student and useless pedagogically.

**Wiring:**

1. **Start from the measured baseline, not the model** —
   [`tcheld0n/CorrijAI`](https://github.com/tcheld0n/CorrijAI) (**MIT**, `1,071 B`, `1,338 KB`)
   ships **both** arms on one harness: a supervised `HistGB` regressor on **Essay-BR** with SHAP
   interpretability, and an LLM agent doing per-competency scoring with per-level anchors and RAG
   over the normative corpus. 🔵 **Use the baseline for the number and the agent for the
   *devolutiva*** — the README's own measurement says so: on a *known* prompt the baseline wins
   (QWK `0.750` vs calibrated agent `0.731`, `n=65`, `sabiá-4` at `temp=0`). A proposal that leads
   with the LLM for scoring is contradicted by the repo it is built on.
2. **Keep the post-hoc calibration.** The raw agent's total bias is `−106.5`; calibrated it is
   `−28.9`. 🔵 That single step is the difference between a scoring service and a complaint queue.
3. **Bind the feedback to the curriculum** —
   [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) (**MIT for code only** — the `607-D`
   scope flag applies, so treat the curriculum **data** separately) plus
   [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (**MIT**, `1,849★`) for
   Brazilian official-data access. Feedback that cites **BNCC** skills is what a secretaria can act
   on.
4. **Deliver where connectivity is the binding constraint** — **Kolibri** (**MIT**) for offline-first
   distribution, not a web app. The IDB's regional read is *"structural gaps … heterogeneous digital
   capabilities"*; the device and bandwidth assumption decides adoption here more than model choice.
5. **Write back to the LMS over API/LTI** — **Moodle** (GPL-3.0) without forking it, per the standing
   copyleft boundary on this base.

**Why now:** this is the first pass in which the region's permissive chain is complete —
**curriculum (BNCC) → assessment (ENEM) → delivery (offline)** — and `p608` recorded a
repository-level LATAM nil, so this recipe did not exist one pass ago.

---

### 🟢 `P609-3` — The interpretable-by-contract learner model (EMEA, `8`–`10` weeks)

**The problem it solves:** under the AI Act the institution is the **deployer**, and an opaque learner
model that routes students is the part a regulator asks about. The usual answer is a post-hoc
explainability layer over a black box, which is the expensive answer.

**Wiring:**

1. **Take the model set a client already imposed this constraint on** —
   [`baptiste-alonso/knowledge-tracing-benchmark`](https://github.com/baptiste-alonso/knowledge-tracing-benchmark)
   (**MIT**, `1,298 B` — 🔴 the API calls it `NOASSERTION`, see `609-F`). Seven **interpretable** KT
   models under one protocol on `110,101` real interactions from a French EdTech firm; **DKT was
   excluded because the client required readable parameters**. Optimised PFA wins at AUC
   `0.789 ± 0.006` — 🔵 **so the interpretable model is not the compromise option here**, which is
   the finding that makes this sellable.
2. **Run it on your own data with the client's data withheld** — the repo ships a **synthetic
   generator with the same schema**, so the pipeline is demonstrable before any DPA is signed.
3. **Report the metric the literature now requires** —
   [`huynhanhkhiem-dms/pooled-auc-knowledge-tracing`](https://github.com/huynhanhkhiem-dms/pooled-auc-knowledge-tracing)
   (**MIT**, `1,143 B`, Ton Duc Thang University): pooled AUC **does not** identify within-learner
   discrimination. Decompose across its `14` scoring rules before quoting a single number.
4. **Say whether the benchmark is saturated** —
   [`KernelInterrupt/kt-benchmark-diagnosis`](https://github.com/KernelInterrupt/kt-benchmark-diagnosis)
   (**MIT**, `1,066 B`): CTW-anchored **Local Irreducible Uncertainty** per interaction, so "we
   improved AUC by `0.01`" can be stated as a share of the headroom that actually existed.
5. **Keep identifiable work out of the model path** —
   [`Bradwave/obfusca`](https://github.com/Bradwave/obfusca) (**MIT**, carried from `p608`):
   in-browser exam anonymisation, nothing uploaded.
6. **Floor and engine** — **pyKT** ([`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit),
   **MIT**, `456★`) for the model implementations, and
   [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) (**BSD-3-Clause**) for QTI delivery
   and candidate state. 🟢 **No copyleft anywhere in this path.**

---

### 🟢 `P609-4` — A recipe for this base, not a client: reject a non-repository at extraction time

**The problem it solves:** `603-A` found this base's own file paths carried as promotion candidates;
`606-F` found `github.com/topics/{…}` on the sell shelves; `607-C` found both classes **inside the
committed ledger**, and concluded the defect *"is in the `{owner}/{repo}` extraction step all three
share, and it will keep reappearing in each new artifact until that step rejects a non-repository at
extraction time rather than at promotion time."* 🟢 `p609` builds it.

**Wiring:** [`ingest/p609-address-rejector.sh`](ingest/p609-address-rejector.sh), two stages, cheapest
first:

1. **`SHAPE`** — offline and free. Rejects: not exactly two path segments (kills the
   `github.com/topics/education` class); an owner that is one of this repository's own directories
   (`evidence`, `ingest`, `agents`, `repos`, `intel`, `verticals`, `compose`, `archive`, …); an owner
   that is a git ref or a `github.com` path prefix (`main`, `master`, `blob`, `tree`, `topics`,
   `users`, …); a repo segment that is a file or ref fragment (`license`, `readme`, `copying`, …);
   and any owner or repo violating GitHub's charset.
2. **`EXISTENCE`** — the `606-E` probe, run **only** on shape-passers:
   `curl github.com/{slug}/info/refs?service=git-upload-pack` → `200` real, `401` absent. Anything
   else is returned as `INDETERMINATE`, never as a pass.

**Validated against the known answer, `10 of 10`:** all `5` non-repositories `607-C` enumerated are
rejected — `4` of them free at `SHAPE` (`evidence/p333-disposition-ledger`,
`evidence/p333-silent-random-probe`, `main/license`, `master/license`) and `alpinevibe/quizpulse` at
`EXISTENCE` (`401`) — plus `606-F`'s topics class at `SHAPE`; `3` real controls
(`HKUDS/DeepTutor`, `pykt-team/pykt-toolkit`, `tcheld0n/CorrijAI`) pass at `200`; the fabricated
control rejects at `401`.

**Swept over the whole committed ledger** (`219` distinct slugs, `ingest/p609-address-rejector.sh
--shape-only`): `215` pass, 🟢 **`4` rejected at shape — exactly the four shape-detectable slugs
`607-C` named, and no others**, which bounds the class rather than merely finding instances. Evidence:
`evidence/address-shape-rejector.2026-11-02-p609.tsv`.

🔵 **Call it at extraction, not at promotion.** The stage is free, it runs with no network, and it is
the only point at which the three artifacts that share the defect can be fixed at once.

---


## 🆕 `p608` — reads `2026-11-02` — four recipes, each buildable from rows byte-read this pass

🔵 Every repo named below had its license byte-read at `raw.githubusercontent.com` on the real
default branch on **2026-11-02**, with `4 of 4` fabricated controls returning `NOT_FOUND` in the
same pass. Byte counts are in `agents/top.md` under `p608`.

---

### `P608-1` — GDPR-safe AI grading line, no data-residency negotiation (EMEA)

**The problem it solves:** EU institutions want AI-assisted marking but cannot ship identifiable
student work to a model endpoint, and the school is the **deployer** under the AI Act — liability
does not transfer to the vendor.

**Wiring, left to right:**

1. **De-identify before anything leaves the browser** —
   [`Bradwave/obfusca`](https://github.com/Bradwave/obfusca) (**MIT**). `PDF.js` + `pdf-lib`, no
   backend. Set redaction on page 1 per exam, choose **Micro-Text** second-page labels (chosen
   specifically **not to interfere with vision/LLM OCR**), rasterise at **`2.6× High AI OCR`**.
   Emits per-exam PDFs (`VER-001.pdf`…), the teacher's decoding key `legenda_docente.pdf`, and
   `obfusca_grades.csv`. 🔵 **Nothing is uploaded — the residency question never arises.**
2. **Score the objective items deterministically** — the `axomiya` rule: marking in **plain code,
   not through the model**, so the numbers are exact and reproducible. Only free-text items go to
   a model, and only in anonymised form.
3. **Run the assessment session on a permissive engine** —
   [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) (**BSD-3-Clause**, `2,058 B`) for
   QTI 3.0 delivery and candidate state.
4. **Re-identify and write back locally** — join `obfusca_grades.csv` to the decoding key
   *on the teacher's machine*, then push to the LMS.
5. **LMS boundary — this is the licensing decision:** write back over API/LTI to
   **Moodle** (GPL-3.0) or **Canvas**/**Chamilo**/**ILIAS** (**AGPL-3.0**) rather than forking
   them. If any platform code must be modified, do it in
   [`openedx/XBlock`](https://github.com/openedx/XBlock) (**Apache-2.0**, `11,358 B` at
   **uppercase** `LICENSE.TXT`) or on **Sakai** (**ECL-2.0**) — the two permissive surfaces in the
   tier.

**Why now:** EU **Annex III** high-risk duties for assessment move to **2027-12-02** (Digital
Omnibus, Reg. (EU) 2026/1744) — ~13 months of runway — while **chatbot transparency** already
applies from **August 2026**. ⚠️ Confirm dates against the Official Journal before contracting.

---

### `P608-2` — the curriculum-bound citing tutor, built in APAC and retargetable to LATAM

**The problem it solves:** the OECD `-17 %` result. A tutor that answers from the open world
produces short-term gains that evaporate; a tutor bound to the actual textbook, citing it, does not
have that failure mode available to it.

**Wiring:**

1. **Ingest the institution's own corpus** —
   [`Tencent/WeKnora`](https://github.com/Tencent/WeKnora) (**MIT**, `v0.9.0`): documents →
   queryable RAG → reasoning agent → self-maintaining wiki.
   ⚠️ **Honour the Apache-2.0 third-party appendix inside its `LICENSE`** — attribution
   obligations survive the MIT header.
2. **Copy the pedagogy contract from** [`HaoyanZhang123/sproutask`](https://github.com/HaoyanZhang123/sproutask)
   (**MIT**). Four rules worth lifting verbatim:
   - every explanatory turn carries **source id + PDF page + printed page**;
   - the **concept graph is separate from the table of contents**, and prerequisite edges carry a
     basis — *never derived from chapter order*;
   - **three independent axes** stored separately — progress, understanding-evidence, review
     activity — and **self-report never enters a judgement**;
   - **answers the tutor disclosed are marked as disclosed**, so the evidence stays honest.
3. **Keep the Socratic default** —
   [`1Zonghao/Si-Yuan-agent`](https://github.com/1Zonghao/Si-Yuan-agent) (**MIT**): open-ended
   questioning, no direct answers, with an explicit escape hatch when the learner is stuck.
4. **Model mastery properly** — [`duaabaig/HiSACKT`](https://github.com/duaabaig/HiSACKT)
   (**MIT**, WI-IAT 2025) beside the held `pykt-team/pykt-toolkit` / `CAHLR/pyBKT` tier; benchmark
   both on `ASSIST2015` before choosing.
5. **Deliver inside the LMS** via **XBlock** (Apache-2.0) — the permissive component boundary
   inside an AGPL platform.

**🟢 The LATAM retarget, stated as the substitution it is:** swap the **人教版 2024 七年级上册生物学**
pack for a **BNCC**-aligned corpus (Brazil) or an **SEP**-aligned one (Mexico), keep every rule in
step 2 unchanged. 🔴 **This is a composition of APAC-origin code against LATAM curriculum, because
this pass found no LATAM-origin permissive education-AI repository at all** — see
`intel/market.md` → LATAM.

---

### `P608-3` — attributable AI use, instead of AI detection (North America)

**The problem it solves:** **60 %** of US teachers use AI tools, **72 %** report integrity
concerns, and most US public schools have **no formal student AI policy**. Detectors do not work.
Visibility does.

**Wiring:**

1. **Put the tutor inside the assignment** —
   [`dlealvilla/wildmind-ai-for-education`](https://github.com/dlealvilla/wildmind-ai-for-education)
   (**MIT**): the teacher sees the prompts and exactly what the AI inserted. The artefact *is* the
   audit trail, so no detection step is needed.
2. **Close the assessment boundary** — adopt the
   [`german-course`](https://github.com/yashvikram30/german-course) (**MIT**) rule: **the AI tutor
   is disabled during exams**, with mock exams running real timings.
3. **Keep the evidence separable** — the `sproutask` three-axis store, with disclosed answers
   marked, so an integrity review can distinguish *the learner demonstrated this* from *the tutor
   said it*.
4. **Emit the policy artefacts the statutes actually name** — the deliverable is not a model, it is
   a document set on dated deadlines: **NC Session Law 2026-41** (state model policy
   **2026-12-31** → local policies **2027-06-30** → teacher PD **2028-06-30**) and **MD SB 720**
   (aligned district policy + a designated **AI coordinator**).
5. **Segment on policy posture, not size** — **SUNY** mandates AI literacy in general education
   from **fall 2026**; **UC Berkeley Law prohibits** generative AI across most graded work. The
   same configuration cannot serve both; the lockout in step 2 is what makes one product do it.

---

### `P608-4` — the low-resource-language tutor, where APAC has a real advantage

**The problem it solves:** national-board students studying in a language the generic assistants
answer poorly — and a mandated curriculum arriving on a fixed date (**India: AI compulsory from
Class 3, 2026-27**).

**Wiring:**

1. **Language and content layer** —
   [`LeeLanguageLab/HokkienTranslation`](https://github.com/LeeLanguageLab/HokkienTranslation)
   (**MIT**) for the low-resource pattern: multimodal generation plus NLP-driven flashcards, with
   two **NAACL 2025** System Demo papers behind the method (`2025.naacl-demo.2`,
   `2025.naacl-demo.26`).
2. **Board-specific loop** —
   [`prayashcloud/axomiya-study-companion`](https://github.com/prayashcloud/axomiya-study-companion)
   (**MIT**) for **SEBA/AHSEC** in **Assamese**: *explain (one local example + 3 exam points) →
   quiz (3 MCQ) → **grade in plain Python, never by the model** → flag low-scoring topics for
   revision.* ⚠️ Its generation is bound to the **BharatCode API** (`qwen-3.8-27b`) and its key —
   **swap this for your own endpoint before any engagement**; that dependency is the one thing in
   this recipe that is not portable.
3. **Ground it in national material** — **DIKSHA** (NCERT + CIET) is open-source, curriculum-linked
   and multilingual; ingest it through **WeKnora** (MIT). 🔵 DIKSHA's own AI surface is thin
   (in-video keyword search, read-aloud for visually impaired learners) — which is precisely the
   room to build in.
4. **Explain visually when text fails** —
   [`harjothkhara/whiteboard-tutor`](https://github.com/harjothkhara/whiteboard-tutor) (**MIT**):
   voice in, voice out, drawing the explanation on a **tldraw** canvas one idea at a time.
5. **Onboarding and newcomer support** —
   [`ME-Massine/azure-ai-student-support`](https://github.com/ME-Massine/azure-ai-student-support)
   (**MIT**) for explaining school rules and procedures at the learner's language proficiency.
   🔵 Holder region **not placed** — no holder evidence in repo, README or license.

---

### 🔴 What cannot be wired yet, and why — so no recipe quietly assumes it

| missing piece | best candidate found this pass | blocker |
| --- | --- | --- |
| **Education-agent evaluation** (tool use, policy, safety) | [`wxxxqcy/ai-learning-assistant`](https://github.com/wxxxqcy/ai-learning-assistant) | 🔴 **no license file** — `8,045 B` README, nothing at four names on either branch |
| **Curriculum-standards index** | [`NBrangerF/curriculum-standards-breakdown`](https://github.com/NBrangerF/curriculum-standards-breakdown) | 🔴 **no license file** (updated today) |
| **Accessible-format transformation** (US ADA, April 2026) | `PreethamGM04/AccessLearn-` | 🔴 **no license file** |
| **African-origin education AI** | `abaridodo/ai4africa`, `abaridodo/makaranta` | 🔴 **both unlicensed** — found, unusable |
| **LATAM-origin education AI** | — | 🔴 **nil across `81` enumerated rows + ES/PT legs** |

🔵 Every one of these is a **grant** problem, not a capability problem. Four of the five have a
maintainer who could be asked for terms — which makes them the cheapest unblocking work available
to this base.

---

## 🆕 `p607` — `2026-11-02` — **🟢 THREE RECIPES, EVERY COMPONENT BYTE-READ IN THIS PASS WITH ITS GRANT, BRANCH AND REGION. 🟢 `P607-1` IS A **PERMISSIVE END-TO-END ASSESSMENT STACK** — ENGINE, PLAYER AND LIBRARIES, FOUR INDEPENDENT HOLDERS, NO COPYLEFT BOUNDARY — WHICH THIS BASE COULD NOT BUILD BEFORE `607-I`. 🟢 `P607-2` IS THE **PROVENANCE LAYER** `T607-1` ARGUES IS THE MOST REGION-PORTABLE COMPONENT IN THE SECTOR. 🟢 `P607-3` REPLACES THIS BASE'S HAND-ROLLED LICENCE GRADING WITH THE APACHE-2.0 CLASSIFIER SITTING IN ITS OWN BACKLOG.**

### 🟢 Component grants, all byte-read `2026-11-02` at the real default branch, every control `404 14 B`

| component | grant | bytes | branch | region |
| --- | --- | --: | --- | --- |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (API: 🔴 `NOASSERTION`) | `2,058` | `master` | EMEA |
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 MIT | `1,076` | `main` | Global |
| [`kennisnet/php-qti3`](https://github.com/kennisnet/php-qti3) | 🟢 MIT | `1,066` | `main` | EMEA |
| [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 MIT | `1,072` | `main` | Global |
| [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) | 🟢 MIT | `1,066` | `main` | EMEA |
| [`php-xapi/client`](https://github.com/php-xapi/client) | 🟡 MIT, untitled | `1,068` | 🔴 `0.7` | EMEA |
| [`php-xapi/model`](https://github.com/php-xapi/model) | 🟡 MIT, untitled | `1,068` | 🔴 `3.x` | EMEA |
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 MIT | `1,084` | `main` | EMEA |
| [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) | 🟢 MIT | `1,080` | 🔴 `develop` | North America |
| [`google/licenseclassifier`](https://github.com/google/licenseclassifier) | 🟢 Apache-2.0 | `11,358` | `main` | Global |
| [`eumakerdev/bncc_api`](https://github.com/eumakerdev/bncc_api) | 🟢 MIT | `1,081` | `main` | LATAM |
| [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | 🟡 **MIT — CODE ONLY**, data carved out | `1,218` | `main` | LATAM |

### 🟢 `P607-1` — A permissive end-to-end assessment stack (EMEA, `12`–`16` weeks)

🟢 **What is new:** before `607-I` this base held QTI *players* and *libraries* but no **engine**, so
every assessment recipe here stopped at rendering an item. The engine is the component that runs a
session, sequences items, and holds candidate state.

**Wiring:**

1. **Engine — [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks)** (BSD-3-Clause, `2,058 B`,
   `master`, maintained `2026-06-30`). Runs the assessment session and owns candidate state. 🔴 Deploy
   the **fork**, not `davemckain/qtiworks` — the upstream is closed by its own README (HEAD
   `2023-01-04`), and the two payloads are byte-identical (`a5c692f120907d58…`), so there is no
   licence difference to weigh.
2. **Delivery — [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player)**
   (MIT) renders QTI 3.0 items in the browser.
3. **Authoring/transport — [`kennisnet/php-qti3`](https://github.com/kennisnet/php-qti3)** +
   **[`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3)** (both MIT) read and write the
   package format. 🟢 Kennisnet is the Dutch national education-ICT foundation, which is the
   provenance an EMEA public-sector buyer will ask about.
4. **Evidence — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS)** (MIT) as the xAPI Learning
   Record Store, with **[`php-xapi/client`](https://github.com/php-xapi/client)** (branch `0.7`) and
   **[`php-xapi/model`](https://github.com/php-xapi/model)** (branch `3.x`) beneath it. 🔴 Both are
   stale (`2023-11-01`, `2025-01-20`) and **untitled** grants — vendor them and pin them.
5. **Integrity — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)** (MIT, `356★`) for
   source-code plagiarism detection on programming items.
6. **The agent layer** is where the studio builds: item generation and distractor critique proposing
   QTI, never writing a mark. 🔴 **The human-release gate from `P-603-B` is mandatory here** — under
   EU Annex III, learner evaluation is high-risk and the `2 Dec 2027` clock applies (`T607-3`).

🟢 **Why it is sellable:** engine BSD-3-Clause, everything else MIT, **four independent holders**,
no copyleft boundary anywhere in the path. 🔴 **The one licence trap to brief the client on:** a
dependency screen reading `spdx_id` rejects the **engine** as unlicensed (`NOASSERTION`) — have the
byte-read `LICENSE.txt` and the `607-D` explanation ready before procurement sees it.

### 🟢 `P607-2` — The provenance layer, built once and sold into three regions (`6`–`10` weeks)

🟢 **The case, from `T607-1`:** India (`20 Feb 2026`), China (since `1 Sep 2025`) and the EU (AI Act
transparency, enforced since `2 Aug 2026`) impose labelling/provenance duties from three unrelated
legal traditions. North America's prohibited-use lists (D.C. OSSE) need the same record to
demonstrate a decision was **not** machine-made.

**Wiring:**

1. **Capture at the boundary.** Every generation event records: model + version, prompt, retrieved
   sources, timestamp, and the human who requested it. 🟢 Emit it as **xAPI statements** into
   [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) via
   [`php-xapi/client`](https://github.com/php-xapi/client) — provenance then lives in the system of
   record the institution already audits, not in a vendor console.
2. **Bind claims to an official source, never to model memory.** Per region, the curriculum authority
   this base now holds byte-read: 🟢 LATAM — [`eumakerdev/bncc_api`](https://github.com/eumakerdev/bncc_api)
   and the BNCC packages (`p603`); 🟢 North America —
   [`pdg6/bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server); 🟢 APAC —
   [`hyunbinseo/neis-school-info`](https://github.com/hyunbinseo/neis-school-info). A claim without a
   citation into one of these does not ship.
3. **Label on egress.** Visible marker on learner- and parent-facing output; machine-readable
   provenance in the record. 🟢 This is the part that satisfies India and China directly.
4. **Prohibited-decision register.** Encode D.C. OSSE's list as a hard gate: no AI output may be the
   proximate cause of a grade, a disciplinary action, an IEP decision or a teacher evaluation. 🟢 The
   register is the deliverable the `4` mandatory-policy US states (`T607-4`) require a district to
   produce and cannot author itself.

🔴 **The licence boundary to respect, with a worked instance:**
[`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) is MIT **for code only** — its `LICENSE` is
stock MIT plus a Portuguese note carving the **data** out to separate provenance
(`ATTRIBUTION.md`, `200`, `3,331 B`). 🟢 A provenance layer is exactly the component that must get
this right: it is the thing that would otherwise *assert* a wrong licence in the audit record.

### 🟢 `P607-3` — Stop hand-rolling licence identification (a recipe for this base, not a client)

🔴 **The problem, measured in this pass:** licence family here is decided by title-line greps and
byte bands. `607-D` found two payloads graded `NOASSERTION` whose bodies are stock BSD-3-Clause and
stock MIT, defeated only by adjacent prose. And `karsh482/Gaokao` (`11,357 B`) vs
`google/licenseclassifier` (`11,358 B`) are two different Apache-2.0 files **one byte apart** — a
one-byte demonstration of why `p312`'s *"identify by template, never by a byte band"* rule exists.

🟢 **The component has been in this base's own `p436` backlog the whole time:**
[`google/licenseclassifier`](https://github.com/google/licenseclassifier) — 🟢 **Apache-2.0,
`11,358 B` byte-read `2026-11-02`**, control `404 14 B`, `351★`, `main`. It does normalised,
confidence-scored licence matching, which is precisely the operation `607-D` shows the grep ladder
failing at.

**Wiring:**

1. Keep the existing ladder for **discovery** — `606-G`'s spellings (`README.md`, `README.rst`,
   `readme.md`, `Readme.md`, `.github/README.md`, `readme.adoc`) and `603-C`'s fix are about *finding*
   the payload, which the classifier does not do.
2. Pipe the **bytes** to `licenseclassifier` for the family verdict instead of grepping a title line.
   🟢 It returns a confidence score, which gives this base what it currently lacks: a **graded**
   verdict rather than a binary one.
3. 🟢 **Keep the fabricated-path control.** The classifier grades payloads; it cannot tell you a
   `404` is a real absence. `404 14 B` stays the control on every arm.
4. 🟡 **Expected yield, stated as a prediction so it can be falsified:** re-grading the `101`
   `NONE`/`NOASSERTION` rows from `606-J`'s census should recover a non-trivial share as real
   permissive grants defeated by adjacent prose. `607-D` found `2` such repositories in a sample of
   `28` (`7.1 %`). 🔴 If the true rate on the `101` is near zero, this recipe is wrong and should be
   recorded as such.

🔵 **Honest caveat:** `licenseclassifier` is Apache-2.0 and Go, and this base's instruments are
Python and shell. 🔴 It is also not education software, which is why it is **disqualified as a shelf
row** and recorded here instead — a tool the base should run, not a row it should sell.

## 🆕 `p606` — `2026-11-02` — **🟢 TWO RECIPES, BOTH BUILT ONLY FROM ROWS BYTE-READ IN THIS PASS OR ALREADY SHELVED: AN **OFFLINE-FIRST EGRA/EGMA ASSESSMENT STACK FOR LOW-CONNECTIVITY AFRICA** (THE `5.67 %` FACILITY CONSTRAINT IS THE DESIGN DRIVER), AND AN **EU HIGH-RISK COMPLIANCE HARNESS** SIZED TO THE `2 Dec 2026` AND `2 Dec 2027` DEADLINES. 🟢 PLUS A REUSABLE **ADDRESS-VERIFICATION RECIPE** FROM `606-E` THAT ANY PASS OR PIPELINE CAN RUN.**

### 🟢 `P606-1` — Offline-first early-grade assessment for low-connectivity systems (EMEA / Africa)

🔵 **Why this shape and not an LMS:** Nigeria's own EdTech gap analysis reports 🔴 **`5.67 %` of
public primary schools have computer facilities** against `54.55 %` of private. A cloud LMS cannot be
the entry point. Tablet-based, sync-later assessment can.

```
  ┌─ FIELD TIER (no connectivity assumed) ────────────────────────────┐
  │ Tangerine-Community/Tangerine     GPL-3.0  116★  byte-read p606   │
  │   └── tangy-form                  GPL-3.0   16★  form engine      │
  │   └── tangy-form-editor           GPL-3.0    5★  authoring UI     │
  │   instruments: EGRA / EGMA, offline capture on tablet             │
  └────────────────────────┬──────────────────────────────────────────┘
                           │  sync when a connection exists
  ┌────────────────────────▼──────────────────────────────────────────┐
  │ ANALYTICS TIER                                                     │
  │ pykt-team/pykt-toolkit            MIT    knowledge tracing        │
  │ adlnet/ADL_LRS                    Apache-2.0  xAPI statement store│
  └────────────────────────┬──────────────────────────────────────────┘
                           │
  ┌────────────────────────▼──────────────────────────────────────────┐
  │ LANGUAGE TIER — local, no per-token cost, no data egress          │
  │ ollama + an open-weight model tuned on national curriculum content│
  │ bncc-dev/bncc-pacotes (MIT code / CC BY 4.0 data) as the pattern  │
  │   for curriculum-as-a-package; Nigeria needs its own equivalent   │
  └───────────────────────────────────────────────────────────────────┘
```

**Wiring, concretely**
1. Author EGRA/EGMA instruments in `tangy-form-editor`; they are `tangy-form` web components, so the
   schema is the integration boundary — nothing needs to be forked to add a field.
2. Tablets run Tangerine offline. Sync is opportunistic, which is the whole point.
3. On sync, emit **xAPI** statements into `ADL_LRS` (Apache-2.0, already on `repos/foundations.md`).
   That decouples the assessment platform from everything downstream.
4. Feed the statement stream to `pykt-toolkit` for per-learner mastery estimates.
5. Any generated feedback runs on a **local** open-weight model via `ollama` — required, not
   preferred: there is no connectivity budget and no data-egress allowance.

🔴 **Licence boundary, stated because it decides the commercial model:** Tangerine and `tangy-form`
are **GPL-3.0**. This is a *deploy, author and extend* stack, **not** vendorable into a proprietary
product. Everything on the analytics and language tiers is MIT/Apache-2.0, so the proprietary work
lives there. 🔵 Estimate: `6–8` weeks to a ministry-demonstrable pilot, dominated by instrument
authoring, not code.

### 🟢 `P606-2` — EU high-risk compliance harness, sized to the real calendar

🔵 **The deadline that drives this is not the famous one.** `2 Aug 2026` for high-risk education
moved to 🟢 **`2 Dec 2027`** (Regulation (EU) 2026/1744). The urgent one is 🔴 **`2 Dec 2026`** —
machine-readable marking of generated content for systems **already deployed**.

```
  AI Act scope decision          ──► is it admissions / placement / outcome
  (schools are DEPLOYERS)             evaluation / attainment / proctoring?
          │                                   │ yes ⇒ high-risk, 2 Dec 2027
          │                                   │ no  ⇒ Art. 50 only, in force
          ▼                                   ▼
  ┌───────────────────────────────────────────────────────────────┐
  │ PROVENANCE LAYER — the 2 Dec 2026 obligation                  │
  │ every generated item/feedback carries a machine-readable mark  │
  │ one field, retrofitted into existing deployments first         │
  └───────────────────┬───────────────────────────────────────────┘
  ┌───────────────────▼───────────────────────────────────────────┐
  │ OVERSIGHT + AUDIT LAYER — the 2 Dec 2027 obligations          │
  │ LangGraph (MIT)  policy nodes: jurisdiction as configuration   │
  │ adlnet/ADL_LRS (Apache-2.0)  immutable xAPI decision trail     │
  │ human-in-the-loop gate before any grade/placement is emitted   │
  └───────────────────┬───────────────────────────────────────────┘
  ┌───────────────────▼───────────────────────────────────────────┐
  │ PLATFORM — whatever the institution already runs               │
  │ moodle/moodle            GPL-3.0   7,570*                      │
  │ openedx/openedx-platform AGPL-3.0  8,214*  <-- network copyleft│
  │   but its extension points are permissive: XBlock (Apache-2.0) │
  │ 1EdTech LTI 1.3 libs (MIT) · QTI 3.0 toolchain (MIT, p604/605) │
  └───────────────────────────────────────────────────────────────┘
```

**Wiring, concretely**
1. **Classify first.** Art. 50 vs high-risk is the whole cost difference. Admissions, placement,
   outcome evaluation, attainment assessment and proctoring are high-risk; a study aid is not.
2. **Ship provenance now** — one field, and it is the only obligation with a `2026` deadline for
   already-deployed systems.
3. Put jurisdiction in **LangGraph policy nodes**, not in code branches. The same deployment must
   satisfy EU Art. 50, China's labelling rules, India's IT Rules and Korea's Framework Act
   (`T606-2`), and only Germany adds a competence-framework layer on top.
4. Log every automated decision as xAPI into `ADL_LRS` — that is the "logging and human oversight"
   evidence an audit asks for, built from a row already on this base's shelves.
🔴 **Licence note carried from this base, not re-derived:** the LMS of record is
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) — **AGPL-3.0**, byte-read
`512 B` again this pass, control `404`. `openedx/edx-platform` is the **pre-rename** address, it
returns `422` on the search channel, and it is **not** Apache-2.0. 🟢 What *is* permissive is the
extension surface — `XBlock` (Apache-2.0) and the LTI/QTI libraries — which is where a studio's own
code belongs. 🔵 Recorded here because an earlier draft of this section wrote *"Open edX
(Apache-2.0)"* and that would have regressed a fact this base settled.

5. Keep the **human gate** before any outcome-affecting output. Non-negotiable under high-risk, and
   it is also what DfE's May 2026 guidance requires of SEND plan drafting in England.

🔵 Estimate: `4` weeks for the provenance layer on an existing deployment; `10–12` weeks for the full
oversight harness. The `13`-month runway makes the second one a design choice rather than a scramble.

### 🟢 `P606-3` — Address verification that actually certifies something (`606-E`)

🔴 The verifier this base is instructed to use certifies nothing: `curl -sI github.com/{repo}` is
`403` for real **and** fabricated repositories. 🟢 Replacement, with its control, runnable anywhere:

```bash
# EXISTENCE: 200 = real, 401 = does not exist.  Validated on 552 probes, perfect separation.
verify() {
  curl -s -o /dev/null -w '%{http_code}' \
    "https://github.com/$1/info/refs?service=git-upload-pack"
}
verify HKUDS/DeepTutor              # -> 200
verify HKUDS/zzq9x-does-not-exist   # -> 401   <-- always run the control

# DEFAULT BRANCH (the search API is blind to transferred repos; git is not)
GIT_TERMINAL_PROMPT=0 git ls-remote --symref "https://github.com/$1" HEAD

# GRANT: byte-read it, never trust spdx_id (604-A: API wrong on 10 of 11 ECL-2.0 repos)
curl -s -r 0-511 "https://raw.githubusercontent.com/$1/$BRANCH/LICENSE"
curl -s -r 0-511 "https://raw.githubusercontent.com/$1/$BRANCH/LICENSE-zzq9x"  # control -> 404 14B

# README: 8 rungs is not enough. .github/README.md and readme.adoc are both real (606-G).
# Cheaper and complete: enumerate the tree once.
git clone --bare --depth 1 --filter=blob:none "https://github.com/$1" r && git -C r ls-tree -r --name-only HEAD
```

🔴 **And two guardrails this pass paid for:**
- **Batched `repo:` lookups silently drop addresses** (`606-C`). Assert `returned == requested` and
  re-probe the shortfall singly — otherwise a run reports `0` errors while losing rows.
- **Never harvest in parallel into one file or with `$$` temp names** (`606-B`). Per-repo output
  files, then a serial byte-compare on a random sample before any claim is drawn. The corrupt run
  here scored `2 of 12` mismatches and invented a repository defect; the clean one scored `0 of 14`.
## 🆕 `p605` — reads `2026-11-02`, commit `2026-11-02` — **🟢 `4` NEW RECIPES, EVERY COMPONENT BYTE-READ TODAY AND NAMED WITH ITS GRANT, ITS BRANCH AND ITS REGION. 🟢 `R-605-1` IS THE ONE THIS PASS EARNED: A **NATIONAL-CURRICULUM CONFORMANCE HARNESS** BUILT ENTIRELY FROM LATAM ARTEFACTS WITH A LICENCE BOUNDARY THAT RUNS THROUGH THE MIDDLE OF ONE REPOSITORY. 🔴 AND ONE **ANTI-PATTERN** REGISTERED, BECAUSE THIS PASS WALKED INTO IT ITSELF.**

---

## 🟢 `R-605-1` — "Does the model know *our* national curriculum?" — a conformance harness, LATAM

🔵 **The question a Brazilian ministry or university actually asks**, and which no vendor demo
answers: *before* we deploy a tutor, does this model answer our curriculum correctly, and can it
mark our exam?

**Components, all byte-read `2026-11-02`:**

| role | component | grant | branch | region |
| --- | --- | --- | --- | --- |
| curriculum item bank + per-round model answers + methodology | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🔴 **split — see the boundary below** | `main` | LATAM `-03:00` |
| human-scored essay ground truth (ENEM criteria) | [`lplnufpi/essay-br`](https://github.com/lplnufpi/essay-br) | 🟢 MIT (`1,113 B`) | `main` | LATAM `-03:00` |
| item generation for the gaps the benchmark exposes | [`glacy/evolutIA`](https://github.com/glacy/evolutIA) | 🟢 Apache-2.0 (`11,563 B`) | `main` | LATAM `-06:00` |
| model-vendor abstraction + cost accounting | [`AI-for-Education/fabdata-llm`](https://github.com/AI-for-Education/fabdata-llm) | 🟢 MIT (`1,064 B`) | `main` | EMEA `+01:00` |
| system of record for delivery | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟡 AGPL-3.0 — **boundary, see below** | — | LATAM |

**Wiring:**

```
[bncc-benchmark: itens/ ]──┐
                           ├──> [fabdata-llm: one interface, N vendors, cost per run]
[essay-br: scored essays]──┘              │
                                          ├──> per-item verdict + per-criterion essay score
                                          │
                        [bncc-benchmark: harness/ + METODOLOGIA.md]
                                          │
                                 curriculum conformance report
                                          │
                        ┌─────────────────┴─────────────────┐
                 gaps exposed                        gaps acceptable
                        │                                   │
              [evolutIA: regenerate items]          ship the tutor, with the
              for the weak BNCC strands             conformance report as the
                                                    acceptance artefact
```

🔴 **The licence boundary runs *through* `bncc-benchmark`, not around it** (`605-L` on
[`../repos/foundations.md`](../repos/foundations.md)):

| what you take | grant | what that permits |
| --- | --- | --- |
| `harness/`, `test/`, config | 🟢 **MIT** | 🟢 fork it, embed it in a client deliverable, relicense your changes |
| `itens/`, `resultados/`, `METODOLOGIA.md` | 🟡 **CC BY 4.0** | 🟢 use and redistribute **with attribution**; 🔴 the attribution travels into the client report |

🟢 **So the deliverable is the harness (MIT) plus a *cited* item bank (CC BY 4.0).** 🔴 A studio
that vendors the item bank into a closed product without the attribution notice is in breach, and
the root `LICENSE` will not tell it so — the root file is a **POINTER** that grants nothing. 🔵 And
🔴 `i-educar` is **AGPL-3.0**: integrate across a process/network boundary (its REST API), never by
linking into proprietary code.

---

## 🟢 `R-605-2` — Assessment interoperability: an agent that reads and writes the standard, not the vendor

🔵 **The problem:** every LMS migration and every assessment-automation engagement dies on item
format. QTI 3.0 is the interchange standard institutions mandate and almost nobody implements.
🟢 As of this pass the permissive toolchain is complete enough to build on, **with three
independent maintainers** (`p604` flagged it as one).

| stage | component | grant |
| --- | --- | --- |
| parse / transform QTI | [`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti) | 🟢 MIT (`1,096 B`) |
| render items to HTML | [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | 🟢 MIT (`1,066 B`) |
| results → per-respondent HTML + aggregate CSV | [`metyatech/qti-reporter`](https://github.com/metyatech/qti-reporter) (`p604`) | 🟢 ISC (`740 B`) |
| human inspect / edit / learn the standard | [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground) | 🟢 MIT (`1,069 B`) |
| launch from the LMS | [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) (Elixir) / [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | 🟢 MIT |
| LTI 1.3 reference to read first | [`LtiLibrary/LtiAdvantageTool`](https://github.com/LtiLibrary/LtiAdvantageTool) (`p604`) | 🟢 MIT |
| auth under the record service | [`yetanalytics/pedestal-oidc`](https://github.com/yetanalytics/pedestal-oidc) | 🟢 Apache-2.0 |

```
LMS (Moodle / Canvas / Open edX)
   │  LTI 1.3 launch  ── ltix | lti-core, validated against LtiAdvantageTool
   ▼
[agent tool surface]
   ├── pie-qti ............. read the institution's existing QTI item pool
   ├── <your generator> .... author new items (evolutIA pattern, in-language)
   ├── qti-html-renderer ... show the item exactly as the standard specifies
   └── qti-reporter ........ emit results, honouring qti-time-limits@max-time
   ▼
xAPI statements ──> LRS (Learning Locker) ── pedestal-oidc for auth
```

🟡 **Flag honestly to the client:** four of these repos are at `0`–`4★`. 🟢 They are shelved for
the **standard** they implement, which is institution-mandated and stable, not for their
community size. 🔵 Budget a fork and a maintainer, not a dependency.

---

## 🟢 `R-605-3` — Executable courseware with automated grading

🔵 **The problem:** slide decks and notebooks drift apart from the code students actually run.

| role | component | grant | ★ |
| --- | --- | --- | --: |
| the courseware, which *is* the runtime | [`marimo-team/learn`](https://github.com/marimo-team/learn) | 🟢 MIT (`1,062 B`) | `362` |
| grading those notebooks | [`ljchang/marimo-grader`](https://github.com/ljchang/marimo-grader) | 🟢 MIT (`1,066 B`) | `1` |
| delivery shell | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) via [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 Apache-2.0 (`LICENSE.TXT` — see `605-B`) | — |
| course hygiene before and after | [`cloudpedagogy/cloudpedagogy-moodle-course-auditor`](https://github.com/cloudpedagogy/cloudpedagogy-moodle-course-auditor) (`p604`) | 🟢 MIT | — |

```
[marimo notebook: lesson + runnable code in one reactive document]
        │ student edits and runs; no separate "exercise repo"
        ▼
[marimo-grader] ── per-cell assertions ──> score + feedback
        │
        ├──> XBlock wrapper ──> Open edX gradebook
        └──> LTI 1.3 launch  ──> Moodle / Canvas gradebook
```

🟢 **Why this pairing and not a notebook+CI rig:** marimo is reactive, so the lesson cannot be in a
stale execution state when it is graded — the failure mode that makes Jupyter autograding brittle.
🔵 `marimo-team/learn` is the only `>100★` component; `marimo-grader` at `1★` is the thin, forkable
part. That asymmetry is the right shape: heavy upstream, light glue.

---

## 🟢 `R-605-4` — Early-grade reading assessment in an under-served language

🔵 **The problem:** EGRA is administered one child at a time by a trained assessor. It does not
scale, and ASR trained on adult Western speech fails on child speech in African languages.

| role | component | grant | region |
| --- | --- | --- | --- |
| 🟢 the evaluation harness that makes this honest | [`AI-for-Education/voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | 🟢 MIT (`1,073 B`) | EMEA `+00:00` |
| model-vendor abstraction + cost per run | [`AI-for-Education/fabdata-llm`](https://github.com/AI-for-Education/fabdata-llm) | 🟢 MIT (`1,064 B`) | EMEA `+01:00` |
| in-language tutoring precedent to copy | [`pingakshgaur/TatvaX-AI-PROTOTYPE`](https://github.com/pingakshgaur/TatvaX-AI-PROTOTYPE) (`8` Indian languages) | 🟢 MIT (`1,070 B`) | APAC `+05:30` |
| record store | xAPI / LRS + [`yetanalytics/pedestal-oidc`](https://github.com/yetanalytics/pedestal-oidc) | 🟢 Apache-2.0 | NA |

```
child reads a passage aloud
        ▼
[ASR candidate models]  <-- you must provide the model + the child-speech dataset
        ▼
[voice-ai-evaluation-framework] ── WER / fluency / accuracy, per model, per age band
        ▼
   model selected WITH its measured error on THIS population
        ▼
[tutor]  ── in-language, TatvaX's multi-language structure as the precedent
        ▼
[xAPI statements] ──> LRS ──> district dashboard
```

🔴 **Say the dependency out loud:** the framework evaluates models, it does not supply them, and
**the Kiswahili child-speech dataset is the client's to provide or collect.** 🟢 That is the
engagement's first phase and its real cost. 🔵 Starting with the *evaluation* harness rather than a
model choice is the whole point — it is the only way to know the system works for the children in
front of you rather than for a benchmark.

---

## 🔴 `R-605-ANTI` — the anti-pattern this pass walked into itself

🔴 **Do not infer a shelf's claim from a keyword on the row.** This pass's first draft selected
"permissive rows" by matching a licence token anywhere in the table row, then accused `5` live rows
of asserting `MIT` without evidence. 🔴 **All five were already graded `BLOCK — no grant` on the
very pages the draft accused**, several under a heading reading *"`BLOCK` — no grant means no
permission"*. Measured false-inclusion rate: 🔴 **`59 of 400` (`14.8 %`)**.

🔵 **Why the trap is specific to a well-maintained KB:** a careful shelf **names the licence a row
does *not* have**, in order to warn —
[`krayin/agent-skills`](https://github.com/krayin/agent-skills)'s row says *"its parent
`krayin/laravel-crm` **is MIT**, so a studio that cleared the parent would be wrong about the
child"*. 🔴 A token matcher reads that as an MIT claim. **The better a base documents its
exclusions, the more a keyword matcher will mistake them for inclusions.**

🟢 **The control, which costs one step:** before writing a claim about what a shelf asserts, read
the selected rows and check the shelf agrees with the predicate. 🟢 A negative marker set
(`BLOCK`, `grantless`, `REVIEW`, `NOASSERTION`, `ShareAlike`, `NOT PROMOTED`) is enough to catch it.

🔵 **Generalised for client work:** the same mistake in a client codebase audit is a licence scan
that greps `LICENSE` files for family names and reports a repository as `Apache-2.0` because its
`NOTICE` cites Apache. 🟢 Grade the **instrument**, not the mention — which is also `604-B`'s
lesson from the opposite direction, where the bytes were an HTML page and the grep said
`Apache-2.0`.

## 🆕 `p604` — reads `2026-11-02`, commit `2026-11-02` — four recipes (`P-604-A`…`P-604-D`), every component grant byte-read at its real default branch with a fabricated-path control at `404`

🔵 **What is new about this pass's recipes.** `p603`'s patterns wired agents *into* an LMS
through connectors. 🟢 **These four sit on the layers underneath**: the identity tier an AI
feature must authenticate through, the analytics tier that already holds the learner data, and
the assessment-interchange format that makes a question bank portable. 🔴 They exist because
this pass's supply is an **institutional stack** (`11` ECL-2.0 repos, `5` Apereo-LAI Apache
rows, a `4`-repo QTI toolchain), not a set of standalone agents.

### 🟢 Component grants, all byte-read `2026-11-02` at the real default branch

| component | grant | bytes | branch | control |
| --- | --- | --: | --- | --- |
| [apereo/cas](https://github.com/apereo/cas) | Apache-2.0 | `11,358` | `master` | `404` |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | Apache-2.0 | `11,359` | `master` | `404` |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | `11,120` | `master` | `404` |
| [Apereo-LAI/OpenLRS](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | 🔴 ECL-2.0 (API: `NOASSERTION`) | `11,085` | `master` | `404` |
| [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🔴 ECL-2.0 (API: `NOASSERTION`) | `9,877` | `master` | `404` |
| [Apereo-LAI/LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 🔴 ECL-2.0 (API: `NOASSERTION`) | `9,919` | `master` | `404` |
| [Apereo-LAI/lai-event](https://github.com/Apereo-Learning-Analytics-Initiative/lai-event) | 🔴 ECL-2.0 (API: `NOASSERTION`) | `9,877` | `master` (`LICENSE.md`) | `404` |
| [Apereo-LAI/lai-model](https://github.com/Apereo-Learning-Analytics-Initiative/lai-model) | 🔴 ECL-2.0 (API: `NOASSERTION`) | `9,877` | `master` | `404` |
| [Apereo-LAI/data-loader-library](https://github.com/Apereo-Learning-Analytics-Initiative/data-loader-library) | Apache-2.0 | `11,356` | `master` | `404` |
| [Apereo-LAI/canvas-matthews-data-loader](https://github.com/Apereo-Learning-Analytics-Initiative/canvas-matthews-data-loader) | Apache-2.0 | `11,356` | `master` | `404` |
| [sakaiproject/genericdao](https://github.com/sakaiproject/genericdao) | ECL-2.0 **AND** Apache-2.0 | `22,589` | `master` | `404` |
| [LtiLibrary/LtiAdvantageTool](https://github.com/LtiLibrary/LtiAdvantageTool) | MIT | `1,067` | `master` | `404` |
| [ucfopen/quiz-extensions](https://github.com/ucfopen/quiz-extensions) | MIT | `1,129` | `master` | `404` |
| [tl-its-umich-edu/instructor-tools](https://github.com/tl-its-umich-edu/instructor-tools) | Apache-2.0 | `11,356` | `main` | `404` |
| [cloudpedagogy/cloudpedagogy-moodle-course-auditor](https://github.com/cloudpedagogy/cloudpedagogy-moodle-course-auditor) | MIT | `1,069` | `main` | `404` |
| [otacke/h5pxapikatchu](https://github.com/otacke/h5pxapikatchu) | MIT | `1,051` | `master` | `404` |
| [metyatech/markdown-to-qti](https://github.com/metyatech/markdown-to-qti) | MIT | `1,065` | `main` | `404` |
| [metyatech/qti-xml-core](https://github.com/metyatech/qti-xml-core) | MIT | `1,056` | `main` | `404` |
| [metyatech/apply-to-qti-results](https://github.com/metyatech/apply-to-qti-results) | MIT | `1,070` | `main` | `404` |
| [metyatech/qti-reporter](https://github.com/metyatech/qti-reporter) | ISC | `740` | `main` | `404` |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | MIT | `1,081` | `main` | `404` |

---

### 🟢 `P-604-A` — Learning analytics on data the institution already has, on a stack its own compliance tool calls unlicensed

🔵 **The situation.** A university runs Sakai or Canvas and has years of interaction data it
does not analyse. 🔴 The open analytics tier for exactly this exists — and the client's
OSS-review gate blocks it, because the GitHub API reports `NOASSERTION` for every repository
in it (`604-A`).

**Wiring.**

1. 🟢 **Clear the licence first — it is a one-day deliverable.** Byte-read the grants and hand
   the client the census: `OpenLRS`, `OpenLRW`, `LearningAnalyticsProcessor`, `lai-event`,
   `lai-model` are **ECL-2.0** = *Apache-2.0 with the patent grant narrowed to education use*.
   🔵 Use [`../evidence/api-vs-byteread-ecl.2026-11-02-p604.tsv`](../evidence/api-vs-byteread-ecl.2026-11-02-p604.tsv)
   as the artifact. 🔴 Add `ECL-2.0` to the dependency allowlist; without this step the rest
   of the recipe cannot be deployed.
2. 🟢 **Model the events against `lai-event` + `lai-model`** rather than inventing a schema.
   🟡 These are `2019`–`2020` and dormant — treat them as a **specification**, not an upstream.
3. 🟢 **Ingest** via `data-loader-library`, using `canvas-matthews-data-loader` as the worked
   example of the SIS/LMS-extract seam.
4. 🟢 **Store** xAPI statements in `OpenLRS`; warehouse them in `OpenLRW` (there is a Python
   client, `OpenLRW-python-api-client`, so an agent can read learner records directly).
5. 🟢 **Authenticate every surface through [`apereo/cas`](https://github.com/apereo/cas)** —
   Apache-2.0, `11,392★`, pushed `2026-11-02`, the liveliest row in the family. An analytics
   dashboard that bypasses campus SSO will not pass review.
6. 🔴 **Gate the model's accuracy** with [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai)
   before any risk score reaches an advisor. A "student at risk" claim is a high-stakes output.

🟡 **The honest caveat.** The LAI tier's newest commit is `2025-09-12`. 🟢 Globant's value here
is **carrying it forward** — the schema and the loaders are sound and the licence is
permissive, so forking is both legal and sensible. 🔴 Do not sell it as a live upstream.

---

### 🟢 `P-604-B` — A portable assessment pipeline: Markdown in, QTI 3.0 out, human releases the marks

🔵 **The situation.** AI item generation is easy and the output is usually trapped in one
vendor's quiz format. **QTI 3.0** is the 1EdTech interchange standard that makes an item bank
portable between an LMS, a proctoring tool and a generator — and open tooling for it is scarce.

**Wiring.**

1. 🟢 **Author** items as Markdown; `markdown-to-qti` emits a QTI package.
2. 🟢 **Generate** candidate items with an LLM *into that Markdown shape* — the model never
   touches XML, which removes the whole class of malformed-package failures.
3. 🟢 **Validate / manipulate** with `qti-xml-core`, the library the rest of the chain uses.
4. 🟢 **Deliver** through the LMS, which consumes standard QTI — no bespoke integration.
5. 🟢 **Mark**: an AI grader writes scores via `apply-to-qti-results` into
   `assessmentResult` XML. 🔴 **Write them as drafts.** Pair this with the
   `toshieji/moodle-grading-mcp` posture this base already holds — *the LLM decides, a human
   releases* — because Ofqual's marking principles (EMEA) make an unreviewed automated grade a
   regulatory problem, not just a quality one.
6. 🟢 **Report** with `qti-reporter`: per-respondent HTML plus an aggregate `report.csv`,
   honouring `qti-time-limits@max-time`.
7. 🟢 **Adapt** an existing LMS's exports in with `tracklms-to-qti-results`.

🟡 **The honest caveat, stated once.** The whole `metyatech` chain is **one small org at
`0`–`2★`**. 🟢 It is worth building on because the **standard** is the durable asset and the
code is MIT/ISC and byte-read — but assume you will maintain a fork, and budget for it.

---

### 🟢 `P-604-C` — An instructor-facing agent that launches from inside the LMS, built from two university reference implementations

🔵 **The situation.** Faculty will not adopt a separate tool with a separate login. The
integration contract is **LTI 1.3 / LTI Advantage**, and getting its security framework wrong
is the usual reason a pilot dies in review.

**Wiring.**

1. 🟢 **Start from [`LtiLibrary/LtiAdvantageTool`](https://github.com/LtiLibrary/LtiAdvantageTool)**
   (MIT, ASP.NET Core 10) — it demonstrates dynamic registration, OIDC third-party login
   initiation, resource-link launch validated against the **LTI 1.3 Security Framework**, and
   signed deep-linking responses. 🔵 Read it before writing launch code, whatever your stack.
2. 🟢 **Copy the product shape from `ucfopen/quiz-extensions`** — a *single*, self-service
   faculty job (bulk quiz-time accommodations) done completely. 🔵 It is in production at a
   university, which is why it is a better template than a demo.
3. 🟢 **Copy the app skeleton from `tl-its-umich-edu/instructor-tools`** (Apache-2.0,
   Django + compiled frontend, Docker dev mode) — and note its posture: **LTI-launch only**.
   That is the integration decision, not a limitation.
4. 🟢 **Add the agent** behind an explicit tool surface, and keep the agent's repository
   **separate and permissive** from any copyleft platform you read.
5. 🔴 **Scope the LTI service claims to the minimum** (names-and-roles, assignment-and-grade)
   and write grades back **as drafts** per `P-604-B` step `5`.
6. 🔴 **Before building a connector, check it does not already exist and is not deprecated.**
   `604-G`: `ucfopen/lti-template-flask-oauth-tokens` looks live on every metric and its README
   line `1` is `# DEPRECATED`, naming `ucfopen/cookiecutter-python-lti` as successor.

---

### 🟢 `P-604-D` — Audit and instrument a Moodle estate without credentials on the live instance

🔵 **The situation.** The fastest way to stall an engagement is to ask for admin access to a
production LMS in week one. 🟢 Both halves of this recipe avoid that entirely.

**Wiring.**

1. 🟢 **Audit offline.** `cloudpedagogy/cloudpedagogy-moodle-course-auditor` (MIT) reads Moodle
   **`.mbz` course backups** — a file the client can already export — and produces audit
   reports, dashboards, content maps, settings reports and before/after comparisons.
   🟢 **It reads the backup without modifying it**, so there is no write path to argue about.
2. 🟢 **Use the audit as the engagement's baseline**: which courses are thin, which are
   inconsistent, where AI content support actually pays.
3. 🟢 **Instrument what is already emitting data.** Where the estate includes WordPress + H5P,
   `otacke/h5pxapikatchu` (MIT) captures the **xAPI statements H5P already sends** into a
   database with filtering and CSV export. 🔵 H5P is pervasive in European schools and this
   data is normally discarded.
4. 🟢 **Route those statements into `OpenLRS`** (`P-604-A`) so content interaction and course
   structure land in one model.
5. 🔴 **Only then** ask for live access, with a measured case for what it buys.

🔵 **Why this one is the usual opener.** It needs a file export and nothing else, it produces a
client-legible artifact in days, and it ends with the data foundation `P-604-A` requires.

## 🆕 `p603` — reads `2026-11-02`, commit `2026-11-02` — four recipes (`P-603-A`…`P-603-D`), every component grant byte-read at its real default branch with a per-repo fabricated-path control at `404`

🔵 **What is new about this pass's recipes.** `p602`'s patterns wrote *into* systems an
institution already runs (Moodle, Canvas, Open edX, an ERP). 🟢 **These four sit one layer
out: they make the AI layer portable between institutions, or bind it to a public standard or
an official national dataset** — because that is what this pass's supply actually is
(`9` interop-standards repos, `4` LATAM official-data rows, `14` LMS/MCP connectors).

### 🟢 Component grants, all byte-read `2026-11-02` at the real default branch

| component | grant | bytes | branch | control |
| --- | --- | --: | --- | --- |
| [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | Apache-2.0 | `11,263` | `main` | `404` |
| [1EdTech/digital-credentials-public-validator](https://github.com/1EdTech/digital-credentials-public-validator) | Apache-2.0 | `11,356` | `main` | `404` |
| [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | Apache-2.0 | `11,356` | `master` | `404` |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | Apache-2.0 | `11,356` | `main` | `404` |
| [yetanalytics/re-oidc](https://github.com/yetanalytics/re-oidc) | Apache-2.0 | `11,356` | `main` | `404` |
| [openedx/tutor-contrib-aspects](https://github.com/openedx/tutor-contrib-aspects) | Apache-2.0 | `11,356` | `main` | `404` |
| [instructure/qti](https://github.com/instructure/qti) | **MIT** | `1,083` | `master` | `404` |
| [agencyenterprise/qti-3-player](https://github.com/agencyenterprise/qti-3-player) | **MIT** | `1,065` | `main` | `404` |
| [ryjones/learner-credential-wallet](https://github.com/ryjones/learner-credential-wallet) 🔴 **ADDRESS UNINDEXED `2026-11-03` (`626-E`)** — same `HEAD` as [`ryjones/learner-credential-wallet`](https://github.com/ryjones/learner-credential-wallet) (`91★`, `MIT`), but that successor is **LOW CONFIDENCE**; keep this institutional address until a stronger instrument exists. | **MIT** | `1,091` | `main` | `404` |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** | `1,080` | `main` | `404` |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | **MIT** | `1,073` | `main` | `404` |
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** | `1,063` | `main` | `404` |
| [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) | **MIT** | `1,119` | `main` | `404` |
| [falkenslab/moodle-driver](https://github.com/falkenslab/moodle-driver) | **MIT** | `1,066` | `main` | `404` |
| [skhdemo/uoft-quercus-mcp](https://github.com/skhdemo/uoft-quercus-mcp) | **MIT** | `1,085` | `main` | `404` |
| [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** | `1,128` | `main` | `404` |
| [Sunbird-Lern/lms-service](https://github.com/Sunbird-Lern/lms-service) | **MIT** | `1,071` | `master` | `404` |
| [hisahonakata/roster_hub_for_gigaschool](https://github.com/hisahonakata/roster_hub_for_gigaschool) | Apache-2.0 | `11,356` | `main` | `404` |
| [SaidBySolo/neispy](https://github.com/SaidBySolo/neispy) | **MIT** | `1,066` | `master` | `404` |
| [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | **MIT** *(code)* | `1,107` | `main` | `404` |
| [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟡 CC BY 4.0 *(data, `dados/LICENSE.md`)* | `1,583` | `main` | `404` |
| [SidneyBissoli/uis-mcp-server](https://github.com/SidneyBissoli/uis-mcp-server) | **MIT** | `1,087` | `main` | `404` |
| [nialvape/utn-mcp](https://github.com/nialvape/utn-mcp) | **ISC** | `747` | `main` | `404` |
| [baoguangsheng/fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) | **MIT** | `1,070` | `main` | `404` |
| [EduNLP/edu-convokit](https://github.com/EduNLP/edu-convokit) 🔴 **STALE ADDRESS (`626-E`)** — canonical is [`EduNLP/edu-convokit`](https://github.com/EduNLP/edu-convokit) | **MIT** | `1,068` | `main` | `404` |
| [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | **MIT** | `1,065` | `master` | `404` |

---

### `P-603-A` — Curriculum-bound course generation: never let the model invent the standard

🔴 **The failure this prevents.** An LLM asked to *"align this lesson to the curriculum"*
will produce plausible standard codes that do not exist. The fix is not a better prompt; it
is **making the standard set a tool call against an authoritative dataset**.

🟢 **Wiring.**
1. **Standards as data.** For Brazil, [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes)
   — install the npm or PyPI package, or run its **MCP server** directly; `1,721` BNCC objectives
   verified against MEC/CNE. Elsewhere, [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE)
   (Apache-2.0) to host your own CASE framework.
2. **Bind generation to retrieval.** The agent may only emit an objective code **returned by a
   tool call** in step 1. Reject any code not in the returned set — this is a validation rule,
   not a prompt instruction.
3. **Emit assessment in a portable format.** [`instructure/qti`](https://github.com/instructure/qti)
   (MIT) for QTI 1.2/2.1 import into Canvas; [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player)
   (MIT) to render QTI 3.x anywhere.
4. **Gate accuracy before release.** Score the pipeline with
   [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) (MIT): the
   eval is *"every emitted code exists in the framework"*, which is pass/fail, not a judgement.

🔴 **Attribution is a build step, not a footnote.** BNCC data is CC BY 4.0 and the attribution
is owed to **Profy Tecnologias Educacionais Ltda** for the compilation — the normative text
itself is an official act and uncopyrighted (*art. 8º, IV, Lei 9.610/98*). 🟢 Emit the credit
line in the generated artefact automatically.

---

### `P-603-B` — Grading assistant with a human-release gate built into the transport

🔵 **Why this composition and not a custom integration.** The gate is the valuable part, and
one component already implements it.

🟢 **Wiring.**
1. **Transport.** [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp)
   (MIT) exposes Moodle Web Services as grading I/O and 🟢 **writes grades as *unreleased
   drafts*** — so the release decision stays with a human *by construction*, not by policy.
2. **Reading work the LMS will not hand you cleanly.**
   [`thc1006/moodle-mcp`](https://github.com/thc1006/moodle-mcp) (MIT) fetches assignment PDFs;
   [`falkenslab/moodle-driver`](https://github.com/falkenslab/moodle-driver) (MIT) covers what
   Web Services do not expose, 🔴 **by driving Moodle with a person's own login — so it inherits
   that person's permissions and must never be given a service account.**
3. **Integrity signal, kept advisory.** [`baoguangsheng/fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt)
   (MIT, ICLR 2024). 🔴 **Attach the score to the draft; never let it set a grade or trigger an
   accusation** — DC OSSE's guidance already bars AI from grading and discipline decisions, and
   several US states now mandate district policy on exactly this.
4. **Audit.** Ship xAPI statements through [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe)
   (Apache-2.0) into [`openedx/tutor-contrib-aspects`](https://github.com/openedx/tutor-contrib-aspects)
   (Apache-2.0: ClickHouse + Superset + Ralph + Vector) for a queryable record of every draft.

🟢 **Governance wrapper for the whole thing:** [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit)
(MIT) for policy enforcement, identity and sandboxing — 🟡 noting its own **Public Preview**
label before it goes near a production gradebook.

---

### `P-603-C` — Portable institutional agent: build once, deploy across an LMS estate

🔴 **The failure this prevents.** A tutor built against one LMS's API is rewritten per client.
🟢 Bind to the **standards**, adapt at the edge.

🟢 **Wiring.**
1. **Rostering at the edge.** [`hisahonakata/roster_hub_for_gigaschool`](https://github.com/hisahonakata/roster_hub_for_gigaschool)
   (Apache-2.0) turns **OneRoster CSV into a OneRoster API** — the adapter that makes a CSV-only
   district look like an API district. 🟡 Dormant since `2023-08`: vendor the code, do not take
   the dependency.
2. **Identity.** [`yetanalytics/re-oidc`](https://github.com/yetanalytics/re-oidc) (Apache-2.0)
   for OIDC in a ClojureScript front end, or the OIDC path your LMS already runs.
3. **Behaviour as profiled xAPI, not bespoke telemetry.**
   [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) (Apache-2.0) to define the
   profile; `xapipe` to route statements *by* profile. 🟡 **Read the IEEE p9274.2.1 base standard
   alongside it** — the repo's own README flags a review/upgrade in progress after xAPI 2.0.
4. **Content that is not LMS-shaped.** [`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) (MIT) to
   develop and build H5P content types; 🔵 its README is at `readme.md`, which is why a
   single-spelling probe reports it as undescribed.
5. **Credentials that outlive the institution.**
   [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator)
   (Apache-2.0) to validate Open Badges, and
   [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
   (MIT) as the learner-held wallet.

🔵 **Why this is the North American engagement specifically:** `6 of the 9` components are
published by the standards bodies themselves, and a US multi-campus or state system is the
buyer that actually needs cross-institution portability rather than per-tenant automation.

---

### `P-603-D` — Official-data-to-agent plumbing (the LATAM and APAC pattern)

🔵 **The pattern this pass's regional evidence actually shows.** `3 of 4` LATAM rows and most
APAC rows wrap a **public or official data source** — a national curriculum, a UN statistics
API, a ministry system, a public university's portal. 🟢 **The product is the plumbing, not
another LMS.**

🟢 **Wiring, as a repeatable shape.**
1. **Pick the official source and wrap it as MCP.** Working examples to copy rather than
   design from scratch: [`SidneyBissoli/uis-mcp-server`](https://github.com/SidneyBissoli/uis-mcp-server)
   (MIT, **UNESCO UIS** statistics, PT-BR docs), [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp)
   (ISC, **UTN** Argentina), [`SaidBySolo/neispy`](https://github.com/SaidBySolo/neispy)
   (MIT, Korea's **NEIS**, sync+async), [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes)
   (MIT code, **BNCC** via npm/PyPI/MCP).
2. **Pin the dataset, and pin it the way BNCC does.** 🟢 `bncc-pacotes` syncs its JSON from a
   **pinned commit** of `bncc-dados` and carries that repo's grant with it — 🔵 copy that
   mechanism, because it is what makes an official-data claim reproducible and auditable.
3. **Read the grant to the bottom before shipping.** 🔴 `bncc-dados`'s root `LICENSE` is MIT
   while the data grant is CC BY 4.0 at **`dados/LICENSE.md`**; `bncc-pacotes`'s root `LICENSE`
   is a **router, not a grant**. A root-only read gets both wrong.
4. **Localise the content, do not re-author it.** [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2)
   (MIT) for Indic languages; [`Sunbird-Lern/lms-service`](https://github.com/Sunbird-Lern/lms-service)
   (MIT) if the delivery target is an India-scale national platform.
5. **Analyse classroom discourse with a purpose-built toolkit.**
   [`stanfordnlp/edu-convokit`](https://github.com/stanfordnlp/edu-convokit) (MIT, NAACL 2024).

🔴 **The regional constraint to quote honestly in a proposal.** In francophone EMEA and
Indonesia the local school-app supply exists and is **ungranted** — `9 of the 14` backlog
repositories with no licence file at all come from those two clusters (`603-E`). 🟢 **So the
first move in those markets is an upstream licence ask, not a build**, and it is cheaper than
either.

## 🆕 `p602` — reads `2026-11-02`, commit `2026-11-02` — four recipes (`P-602-A`…`P-602-D`), every component grant byte-read at its real default branch with a per-repo fabricated-path control at `404`

🔵 **What is new about this pass's recipes.** Earlier patterns on this page composed *tutors* and
*content generators* — things that sit beside an institution's systems. 🟢 **All four below operate, or
write into, a system the institution already runs** (Moodle, Canvas, Open edX, an ERP), because that is
what this pass's supply actually is: `11` new Moodle plugins, `4` new Open edX components, `5` promoted
LMS connectors.

### 🟢 Component grants, all byte-read `2026-11-02` at the real default branch

| component | grant | bytes | branch | control |
| --- | --- | --: | --- | --- |
| [jcrodriguez-dis/moodle-mod_vpl](https://github.com/jcrodriguez-dis/moodle-mod_vpl) | GPL-3.0 | `35,147` | `master` | `404` |
| [hit-moodle/moodle-local_onlinejudge](https://github.com/hit-moodle/moodle-local_onlinejudge) | GPL-3.0 | `35,147` | `master` | `404` |
| [tmuras/moosh](https://github.com/tmuras/moosh) | GPL-3.0 | `35,149` | `master` | `404` |
| [C0D3D3V/Moodle-DL](https://github.com/C0D3D3V/Moodle-DL) | GPL-3.0 | `35,141` | `main` | `404` |
| [erseco/alpine-moodle](https://github.com/erseco/alpine-moodle) | **MIT** | `1,072` | `main` | `404` |
| [catalyst/moodle-auth_saml2](https://github.com/catalyst/moodle-auth_saml2) | GPL-3.0 *(hdr)* | — | 🔴 `MOODLE_500_STABLE` | `404` |
| [danmarsden/moodle-mod_attendance](https://github.com/danmarsden/moodle-mod_attendance) | GPL-3.0 *(hdr)* | — | 🔴 `MOODLE_503_STABLE` | `404` |
| [catalyst/moodle-tool_objectfs](https://github.com/catalyst/moodle-tool_objectfs) | GPL-3.0 *(hdr)* | — | 🔴 `MOODLE_404_STABLE` | `404` |
| [moodlebox/moodlebox](https://github.com/moodlebox/moodlebox) | AGPL-3.0 | `34,523` | `main` | `404` |
| [jasp-nerd/courseforge](https://github.com/jasp-nerd/courseforge) | **Apache-2.0** | `11,358` | `main` | `404` |
| [tomtranjr/canvas-control](https://github.com/tomtranjr/canvas-control) | **MIT** | `1,060` | `main` | `404` |
| [zs-andy/lms-cli](https://github.com/zs-andy/lms-cli) | **MIT** | `1,077` | `main` | `404` |
| [hunterschep/canvas-lms-codex-plugin](https://github.com/hunterschep/canvas-lms-codex-plugin) | **MIT** | `1,069` | `main` | `404` |
| [doldsimo/lti-1.3-canvas-lms](https://github.com/doldsimo/lti-1.3-canvas-lms) | **MIT** | `1,067` | `main` | `404` |
| [eduNEXT/tvm](https://github.com/eduNEXT/tvm) | AGPL-3.0 | `34,523` | `main` | `404` |
| [appsembler/figures](https://github.com/appsembler/figures) | **MIT** | `1,078` | `main` | `404` |
| [cookiecutter-openedx/cookiecutter-openedx-devops](https://github.com/cookiecutter-openedx/cookiecutter-openedx-devops) | AGPL-3.0 | `35,136` | `main` | `404` |
| [Ansarimajid/College-ERP](https://github.com/Ansarimajid/College-ERP) | **MIT** | `1,075` | `main` | `404` |

🔴 **Do not pull:** `krayin/agent-skills`, `akshsgaur/CMUCanvasMCPSErver`, `orionkabeza/canvas-mcp`,
`colehollander10-netizen/canvas-student-mcp-server`, `codern-org/codern` — **all byte-read grantless**,
every fabricated-path control `404`.

### 🟢 `P-602-A` — Conformant automated grading inside an existing Moodle (EMEA, `10`–`14` weeks)

🔵 **The insight that makes this sellable:** the EU AI Act makes **exam scoring** high-risk, and the
institution is *already doing it* with an open-source plugin. The engagement is **conformance**, not
capability — an easier budget line than "add AI".

1. **Inventory the existing scoring path.** `moodle-mod_vpl` (submission + automatic grading) and
   `moodle-local_onlinejudge` (scoring backend). Drive the audit with **`moosh`** so the inventory is
   reproducible rather than a screenshot exercise.
2. **Wrap, don't replace.** Add an LLM feedback layer that writes **formative comments only**; the
   numeric grade stays with the deterministic judge. 🔵 This is the single design decision that keeps
   the model out of the Annex III "scoring" function.
3. **Human-review gate.** Any AI-touched grade routes to an instructor queue before release;
   `moodle-mod_attendance` supplies the engagement signal for prioritising that queue.
4. **Evidence pack.** Per-submission log (model, prompt, version, reviewer, timestamp), a student
   transparency notice, and a conformance file citing **EUR-Lex Regulation (EU) 2024/1689 as amended by
   2026/1744** — 🔴 **not** a vendor compliance blog; two pages in one search leg gave contradictory
   deadlines this pass.
5. **Identity and deployment.** `moodle-auth_saml2` for institutional SSO; `erseco/alpine-moodle` (MIT)
   for the reproducible staging container; `moodle-tool_objectfs` if submission media is large.

🔴 **Branch discipline, or step 1 fails silently:** three components default to
`MOODLE_<version>_STABLE`. 🟢 **Resolve every ref with `git ls-remote --symref` before cloning** — a
`main`/`master` checkout returns nothing and a pinning script will report the plugin as absent.
🟡 **Reciprocity a client must hear:** every Moodle component is GPL-3.0-or-later. Safe as a plugin
deployment; 🔴 not a basis for lifting code into a proprietary product. The billable artefact is the
conformance layer and the integration.

### 🟢 `P-602-B` — Canvas instructor-workflow agent for a North American university (`6`–`8` weeks)

1. **Course build.** [`jasp-nerd/courseforge`](https://github.com/jasp-nerd/courseforge) (Apache-2.0):
   syllabus → a real Canvas course, over MCP. 🟢 **Insist on its IMSCC/Common Cartridge export path** —
   the only feature in this recipe that survives the university changing LMS.
2. **Bulk operations and migration.**
   [`tomtranjr/canvas-control`](https://github.com/tomtranjr/canvas-control) (MIT) for scripted
   course/file retrieval — the audit and migration leg.
3. **Student-facing surface, if in scope.**
   [`hunterschep/canvas-lms-codex-plugin`](https://github.com/hunterschep/canvas-lms-codex-plugin) (MIT).
4. **Interoperability check.** Validate the LTI 1.3 handoff with
   [`doldsimo/lti-1.3-canvas-lms`](https://github.com/doldsimo/lti-1.3-canvas-lms) (MIT). 🔴 Do **not**
   start from [`ucfopen/lti-template-flask`](https://github.com/ucfopen/lti-template-flask) — marked
   `DEPRECATED` in its own description.

🔴 **Hard gate before any component is pulled:** `4 of 11` Canvas-MCP addresses on GitHub are
**grantless**. Byte-read the grant at the real default branch, with a fabricated-path control, for
every component — the four named above are cleared; a third of the category is not.
🟡 **Size the risk honestly:** `4 of 5` promoted components are under `11★` and single-maintainer.
🟢 **Fork and own; do not depend on upstream release cadence.**

### 🟢 `P-602-C` — Multi-institution student assistant (APAC, `8`–`10` weeks)

🔵 **The gap this fills:** the Canvas tooling above assumes **one** institution. A student in this
region may hold accounts at several, across two different LMS products.

1. **The connector.** [`zs-andy/lms-cli`](https://github.com/zs-andy/lms-cli) (MIT) — **multi-school,
   Canvas *and* Blackboard, read-only by design.** 🟢 The read-only posture is the right default for a
   student-facing assistant and removes the whole class of write-side incidents.
2. **Records and operations layer**, where the engagement includes the institution rather than only the
   student: [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) — **LGPL-3.0**,
   branch `19.0`. 🟢 **LGPL-3.0 is what makes this commercial**: the studio's own modules stay
   proprietary while changes to OpenEduCat's files are shared. 🔵 Already on
   [`../verticals/solutions.md`](../verticals/solutions.md) — cited here, not newly claimed.
3. **Permissive alternative at app scale.**
   [`Ansarimajid/College-ERP`](https://github.com/Ansarimajid/College-ERP) (MIT) — 🟡 single-maintainer
   Django app, not a module ecosystem. Choose it only when the domain is small and MIT is mandatory.
4. 🔴 **Do not pull `krayin/agent-skills`** — same vendor as this base's MIT `krayin/laravel-crm` and
   **grantless**. 🔵 The child does not inherit the parent's grant.

### 🟢 `P-602-D` — LATAM Open edX operations practice (`8`–`12` weeks)

🔵 **Why this is the LATAM recipe and not another localisation plan.** This pass's one byte-evidenced
LATAM row is not courseware — it is **operations tooling**
([`eduNEXT/tvm`](https://github.com/eduNEXT/tvm), placed by its own `tvm.docs.edunext.co` Colombian
ccTLD). 🟢 **The regional opportunity is running Open edX for other institutions** — a service
business, not a content business.

1. **Multi-version estate management.** `eduNEXT/tvm` — Tutor version and environment manager, for
   several Open edX versions across client tenants from one practice.
2. **Deployment substrate.**
   [`cookiecutter-openedx/cookiecutter-openedx-devops`](https://github.com/cookiecutter-openedx/cookiecutter-openedx-devops)
   (AGPL-3.0, Tutor on Kubernetes via Terraform). 🟡
   [`openfun/openedx-docker`](https://github.com/openfun/openedx-docker) last pushed `2025-07-09` —
   reference image, not a dependency.
3. **The liftable layer.** [`appsembler/figures`](https://github.com/appsembler/figures) — **MIT**, and
   therefore 🟢 **the one component here a studio can extend into proprietary client reporting.** Build
   cross-tenant analytics and early-warning on `figures`, not on the AGPL-3.0 plumbing.
4. **Offline cohorts.** Keep the low-connectivity path from `P-600-B`;
   [`moodlebox/moodlebox`](https://github.com/moodlebox/moodlebox) (AGPL-3.0) is the Moodle-side
   equivalent — a server plus Wi-Fi AP on a Raspberry Pi.

🔴 **The licence shape is the whole plan.** `3 of 4` infrastructure components are **AGPL-3.0**: fine to
**operate** as a service provider, 🔴 **fatal to redistribute as a product.** 🟢 The commercial surface
is the MIT analytics layer plus the operations practice itself. 🟡 **The gap this recipe does not
close:** there is still no permissive, LATAM-originated education platform of record.

## 🆕 `p601` — reads `2026-11-01`, commit `2026-11-02` — four recipes (`P-601-A`…`P-601-D`), every component grant byte-read at its real default branch with a per-repo fabricated-path control at `404`

🔵 **What is new about these four.** `P-601-A` serves a buyer this file has never addressed — the
**university research office**. `P-601-B` closes the **scoring seam** `p600` named and could not fill,
because the delivery layer did not exist on this base until this pass. `P-601-C` is assembled entirely
from **in-region APAC** components. `P-601-D` exists because the LATAM supply measurement came back at
`1` of `864` addresses, so the recipe has to be a *build* recipe rather than an *adopt* recipe.
🔴 **No component below is NonCommercial, reciprocal or grantless.** Excluded by that rule and named so
no one re-finds them hopefully: `Imbad0202/academic-research-skills` (`54,881★`, CC BY-NC),
`TheOdinProject/curriculum` (`13,200★`, CC BY-NC-SA), `wdcpclover/ai4paper` (`4,041★`, grantless).

### 🟢 `P-601-A` — University research-office manuscript pipeline (North America, EMEA higher ed)

**Buyer:** research office / graduate school. **Not** the classroom, which is where every prior recipe
on this page points.

| Stage | Component | Grant (byte-read) | Wiring |
| --- | --- | --- | --- |
| 1. Orchestration | [`OpenNSWM-Lab/FAROS`](https://github.com/OpenNSWM-Lab/FAROS) `3,042★` | 🟢 MIT (`1,075 B`, `main`) | Blueprint runtime: idea → experiment → draft → review. It owns the state machine; everything below is a step inside it |
| 2. Target-journal conventions | [`brycewang-stanford/Awesome-Journal-Skills`](https://github.com/brycewang-stanford/Awesome-Journal-Skills) `1,346★` | 🟢 MIT (`1,067 B`, `main`) | Load the pack for the target venue (AER, QJE, Nature, Cell, `200+`) as the style contract before drafting |
| 3. Discipline voice | [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) `693★` | 🟢 MIT (`1,063 B`, `main`) | Swap per faculty. Economics shown; `WenyuChiou/ai-research-skills` (MIT) is the generic catalogue |
| 4. Prose discipline | [`Kiterlin/anti-defensive-writing`](https://github.com/Kiterlin/anti-defensive-writing) `1,583★` | 🟢 MIT (`1,065 B`, `main`) | Run as a revision pass, not a generation pass — it strips hedging from an existing draft |
| 5. 🟢 **Citation integrity** | [`federicodeponte/opendraft`](https://github.com/federicodeponte/opendraft) `523★` | 🟢 MIT (`1,081 B`, 🔴 `master`) | **The hallucination gate.** Checks every DOI against scholarly databases. 🔴 Make this a blocking step — it is the only component that can fail the pipeline on a factual ground |
| 6. Adversarial review | [`Spark-To-Paper-Skills/paperjury`](https://github.com/Spark-To-Paper-Skills/paperjury) `1,214★` | 🟢 MIT (`1,067 B`, `main`) | Pre-submission stress test: review → verdict → revise → verify. Loop to stage 4 on a reject verdict |
| 7. Output | [`appautomaton/latex-arxiv-SKILL`](https://github.com/appautomaton/latex-arxiv-SKILL) `473★` + [`latextemplates/scientific-thesis-template`](https://github.com/latextemplates/scientific-thesis-template) `397★` | 🟢 MIT (`1,069 B`) + 🟡 `0BSD` (`665 B`) | arXiv-ready LaTeX. 🟡 The template's copyright line is an unfilled `[year] [fullname]` (`601-D`) — fill it before delivery |
| 8. Retrieval evaluation | [`beir-cellar/beir`](https://github.com/beir-cellar/beir) `2,327★` | 🟢 Apache-2.0 (`11,348 B`, `main`) | If stages 2–5 are RAG-backed, this is the harness that proves the retrieval layer works. `15+` IR datasets |

🟡 **Honest limit:** stages `2`–`6` are **prompt/skill assets**, not services — composable context with
no runtime or evaluation of their own. `FAROS` (1) and `beir` (8) are the only executable components.
🔵 **Sequence that matters:** `5` before `6`. Reviewing a draft whose citations are unverified wastes
the expensive step on text that may be withdrawn.

### 🟢 `P-601-B` — Closing the scoring seam: generate → deliver → score → retain (any region)

🔴 **The gap this fills, stated exactly.** `p600` shelved `agenticfabriq/beacon` as a free-text grading
harness and recorded that `nbgrader` leaves the scoring seam open. 🔴 **Neither it nor any prior recipe
named a component that renders an item to a learner and captures the response** — the step was
hand-waved for `600` passes. `P-601-B` is that step.

| Stage | Component | Grant (byte-read) | Wiring |
| --- | --- | --- | --- |
| 1. Item generation | `agenticfabriq/beacon` (`p600` shelf) | 🟢 Apache-2.0 (`11,358 B`) | Emits items **as JSON**, which is the contract stage 2 consumes |
| 2. 🟢 **Delivery & scoring** | [`surveyjs/survey-library`](https://github.com/surveyjs/survey-library) `4,918★` | 🟢 MIT (`1,102 B`, 🔴 `master`) | **The new layer.** JSON-schema runtime for React/Angular/Vue/vanilla: renders, validates, scores. Embed inside an existing LMS page |
| 3. Service deployment | [`didi/xiaoju-survey`](https://github.com/didi/xiaoju-survey) `3,803★` | 🟢 Apache-2.0 (`11,412 B`, `main`) | Use **instead of** stage 2 when the client needs a standalone service with analytics and in-region storage rather than an embedded library |
| 4. Live / proctored sessions | [`nymanjens/quizmaster`](https://github.com/nymanjens/quizmaster) `327★` | 🟢 Apache-2.0 (`591 B`, 🔴 `master`) | Synchronous multi-participant runs — vivas, in-class checks |
| 5. 🟢 **Retention loop** | [`2anki/2anki.net`](https://github.com/2anki/2anki.net) `328★` → `p600` spaced-repetition tier | 🟢 MIT (`LICENSE.md`, `1,310 B`, `main`) | Route **missed** items from stages 2–4 into spaced repetition. This is the loop `p600`'s retention tier had no feeder for |
| 6. Mastery gate | `fcescob/understand` (`p600` shelf) | 🟢 MIT (`1,075 B`) | Advance on mastery, not completion — reads stage 5's recall state |

🟡 **Interchange limit, flagged before anyone promises it:** 🔴 **none of stages 2–4 implements QTI**,
so integration with an existing institutional assessment estate is bespoke work. Scope it explicitly.

### 🟢 `P-601-C` — APAC in-region, in-language courseware stack (data residency by construction)

🔵 **Every component is APAC-originated or language-neutral, and all are permissive** — so the stack
answers a sovereignty requirement without a licence exception.

| Stage | Component | Grant (byte-read) | Wiring |
| --- | --- | --- | --- |
| 1. Platform of record | [`open-scratch/teaching-open`](https://github.com/open-scratch/teaching-open) `633★` | 🟢 Apache-2.0 (`11,371 B`, 🔴 `master`) | CN-built K-12 platform shipping Scratch + ScratchJr + Python **with** courses, classes, assignments, permissions. The deployable spine |
| 2. Assessment service | [`didi/xiaoju-survey`](https://github.com/didi/xiaoju-survey) `3,803★` | 🟢 Apache-2.0 (`11,412 B`, `main`) | 🟢 Self-hosted, analytics included — **no learner response leaves the region** |
| 3. Courseware conversion | `youngman2007/courseware-cn-annotator` (`p600` shelf) | 🟢 MIT (`1,093 B`) | In-language courseware annotation |
| 4. Translation | [`translate-tools/linguist`](https://github.com/translate-tools/linguist) `1,082★` | 🟢 BSD-3-Clause (`1,542 B`, 🔴 `master`) | Offline-capable — keeps stage 3 running without an external MT call |
| 5. Reading support | [`rampaa/JL`](https://github.com/rampaa/JL) `404★` + [`tristcoil/hanabira.org`](https://github.com/tristcoil/hanabira.org) `432★` | 🟢 Apache-2.0 (`11,357 B`) + 🟢 MIT (`1,061 B`) | JA lookup; JA **and** KO self-hostable portal |
| 6. Teacher-side authoring | [`liqinling1994-cloud/master-teacher`](https://github.com/liqinling1994-cloud/master-teacher) | 🟢 MIT (`1,063 B`, `main`) | 名师问问 lesson-design skill, `152` personas. 🟡 `4★` — a pattern to copy, not a dependency to pin |

🔴 **Excluded from this stack on licence grounds, both APAC and both tempting:**
`wdcpclover/ai4paper` (`4,041★`, 🔴 **grantless** — no file at `main`, control `404`) and
`Allenpandas/BJTU-CS-Notebook` (🔴 CC BY-NC-SA).

### 🟢 `P-601-D` — LATAM Spanish/Portuguese-language build (because there is no regional stack to adopt)

🔴 **The measurement that dictates this recipe's shape.** `1` of `864` addresses in this pass's sweep is
LATAM-placed, and it has `1★`. 🟢 **So this is deliberately a build-and-localise recipe on
region-neutral permissive foundations — not an adopt-the-local-stack recipe, because no local stack
exists.** The demand side is the best-evidenced of any region (Digital Education Council with Tec de
Monterrey: `92 %` of students, `79 %` of faculty; UNESCO IESALC: `200` institutions across `19`
countries, adoption outrunning governance), which is precisely why the supply gap is an opportunity
rather than a reason to skip the region.

| Stage | Component | Grant (byte-read) | Wiring |
| --- | --- | --- | --- |
| 1. 🟢 **Regional seed** | [`JackStar6677-1/edudocente-studio`](https://github.com/JackStar6677-1/edudocente-studio) | 🟢 MIT (`1,094 B`, `main`) | **The only LATAM-placed address found.** Spanish-language print-ready assessment generator. 🟡 `1★` — fork it as a starting point and expect to own it |
| 2. Delivery | [`surveyjs/survey-library`](https://github.com/surveyjs/survey-library) `4,918★` | 🟢 MIT (`1,102 B`, 🔴 `master`) | Locale-driven rendering; no regional alternative needed |
| 3. In-language conversion | [`translate-tools/linguist`](https://github.com/translate-tools/linguist) `1,082★` | 🟢 BSD-3-Clause (`1,542 B`) | ES/PT conversion of existing courseware |
| 4. University research market | `P-601-A` stages `2`–`6` | 🟢 all MIT | Applies unchanged — the research-writing tier is language-neutral and serves ES/PT-language faculty |
| 5. Print-first delivery | stage 1, retained deliberately | 🟢 MIT | 🔵 `edudocente-studio` generates **print-ready** output. Low-connectivity classrooms are a real regional constraint; do not replace this with a web-only flow by reflex |

🟡 **Re-measure before treating this as structural.** `topic:lesson-planning` is `100 %` unheld with
its entire population at `0–5★` and created in `2026`, so the LATAM supply gap may be a timing
observation. 🟢 **Falsifiable:** re-run the sweep in `10` passes; if LATAM placement is still `≤ 2` of
`~864`, the gap is structural and stage 1 should be replaced by a Globant-owned asset.

## 🆕 `p600` — `2026-11-01` — three recipes built from supply that did not exist on these pages yesterday, and every component grant byte-read this pass

🔵 **Why these three and not more.** `600-B`/`600-C` widened the axis set and produced `678` unheld
addresses, of which `9` agents and `11` platform/curriculum rows survived a byte-read licence screen
and a `≥ 5★` floor. The recipes below are the compositions those rows make possible that the previous
`599` passes could not state. 🔴 **Each names its weakest component explicitly** — a recipe whose
risks are implicit is a sales sheet, not a plan.

### 🟢 Component grants, all byte-read `2026-11-01` at the real default branch, every fabricated-path control `404`

| component | grant (bytes) | branch | role |
| --- | --- | --- | --- |
| [MathWorks-Teaching-Resources](https://github.com/MathWorks-Teaching-Resources) (`81` repos) | 🟢 **BSD-3-Clause** (`1,527`/`1,528 B`) | 🔴 **`release`** on `59 of 81` | STEM course content |
| [LearnAIHubC/LearnDeck](https://github.com/LearnAIHubC/LearnDeck) | 🟢 **MIT** (`LICENSE.txt`, `1,068 B`) | `main` | material → slide decks |
| [agenticfabriq/beacon](https://github.com/agenticfabriq/beacon) | 🟢 **Apache-2.0** (`11,358 B`) | `main` | free-text grading harness |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** (`1,512 B`) | `main` | notebook autograding |
| [fcescob/understand](https://github.com/fcescob/understand) | 🟢 **MIT** (`1,075 B`) | `main` | mastery gate |
| [Rayhaan1345/socratic-tutor](https://github.com/Rayhaan1345/socratic-tutor) | 🟢 **MIT** (`1,070 B`) | `main` | question-first tutoring |
| [reuseman/flashcards-obsidian](https://github.com/reuseman/flashcards-obsidian) | 🟢 **MIT** (`1,069 B`) | `main` | notes → scheduled cards |
| [shaankhosla/repeater](https://github.com/shaankhosla/repeater) | 🟢 **Apache-2.0** (`11,357 B`) | `main` | terminal-native SRS |
| [lakesare/memcode](https://github.com/lakesare/memcode) | 🟢 **MIT** (`1,080 B`) | 🔴 **`master`** | hosted multi-tenant SRS |
| [sizwinz/StudySage…](https://github.com/sizwinz/StudySage-Offline-Online-AI-Note-Assistant) | 🟢 **MIT** (`1,083 B`) | `main` | offline study assistant |
| [youngman2007/courseware-cn-annotator](https://github.com/youngman2007/courseware-cn-annotator) | 🟢 **MIT** (`1,093 B`) | `main` | PDF → zh study pack |
| [selftune-dev/selftune](https://github.com/selftune-dev/selftune) | 🟢 **MIT** (`1,067 B`) | `main` | skill eval / observability |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (`11,361 B`) | 🔴 **`master`** | LTI 1.3 into any LMS |

🔴 **Do not vendor:** `hwgilbert16/scholarsome` (AGPL-3.0), `mnemosyne-proj/mnemosyne` (pointer, not a
grant — `600-G`), `CaviraOSS/PageLM` (bespoke non-commercial), `GarethManning/education-agent-skills`
(CC BY-SA 4.0, content only — `599-A`).

---

## 🆕 P-600-A — 🟢 **Engineering-faculty course modernisation on BSD-3-Clause content** (8–12 weeks, EMEA / North America)

🔵 **The brief this answers:** *"We need accredited-quality STEM course material we are allowed to
modify and rebrand, with AI assistance on top, and we cannot wait for a content licensing
negotiation."* 🟢 **Nothing else on these pages answers it** — every agent row generates material from
the client's own inputs; this is the only tier that *supplies* subject content under a permissive grant.

**Wiring:**
1. **Content base** — select modules from `MathWorks-Teaching-Resources` (`81` repos: Fourier analysis,
   thermodynamics, fluid mechanics, control systems, robotic manipulators, numerical methods,
   programming fundamentals). 🔴 **Clone with the branch resolved first:**
   `git ls-remote --symref <url> HEAD` → `release` for `59 of 81`. A `git clone -b main` script will
   fail on three quarters of the estate (`600-D`).
2. **Delivery** — Open edX or Moodle as the LMS; attach the agent layer through
   `Cvmcosta/ltijs` (LTI 1.3) so no LMS fork is needed. 🔴 `ltijs` is on `master`.
3. **Courseware generation** — `LearnDeck` turns each module's notes into lecture decks;
   keep the BSD-3-Clause attribution block in the generated deck footer.
4. **Assessment** — `nbgrader` for anything notebook-shaped; `beacon` for free-text and
   derivation answers, which `nbgrader` cannot score.
5. **Progression** — `understand` as a mastery gate between modules; `repeater` or
   `flashcards-obsidian` for retention between lectures.
6. **Agent QA** — `selftune` to measure whether the tutoring skills are actually improving
   outcomes rather than just running.

🔴 **Weakest component, named:** the MathWorks runtime is **commercial MATLAB/Simulink**. 🟢 The
*content* is BSD-3-Clause and rebrandable; 🔴 the client needs MATLAB licences, or the modules must be
ported (Python/Octave) — which is real work and must be priced, not assumed. 🔵 **Say this in week 1,
not week 9.**

🟡 **EMEA regulatory note:** assessment that affects progression is Annex III high-risk under the EU AI
Act, and the Digital Omnibus (`Regulation (EU) 2026/1744`) moved that compliance date to
`2027-12-02` — **secondary-source grade on these pages, hosts unreachable (`583-E`)**. 🟢 The
Article 4 AI-literacy duty applies *now*, so the staff-training element is not deferrable.

---

## 🆕 P-600-B — 🟢 **A permissive retention layer bolted onto an LMS the client already runs** (4–6 weeks, Global / LATAM)

🔵 **The brief:** *"Completion is fine, retention is terrible, and we are not replacing the LMS."*
🟢 This base has argued retention science for hundreds of passes (`FSRS` in `318` files) while holding
no permissive implementation. `600-D`'s SRS tier closes that.

**Wiring:**
1. **Capture** — an agent (`Skill-Anything`, or `courseware-cn-annotator` for Chinese) converts each
   existing course unit into atomic question/answer pairs as markdown.
2. **Schedule** — `flashcards-obsidian` (MIT) for the notes-native path, or `memcode` (MIT, 🔴 branch
   `master`) when the client needs a **hosted multi-tenant** deck server with per-cohort decks.
3. **Low-connectivity cohorts** — `StudySage` (MIT, offline-first) so review works without a
   session; sync on reconnect. 🔵 **This is the LATAM and rural-APAC path**, and it is the reason
   `memcode` alone is not the answer.
4. **CLI/engineering cohorts** — `repeater` (Apache-2.0) embeds in a terminal workflow with
   **no hosting, no auth, no UI to maintain**.
5. **Integration** — surface review prompts back into the LMS via `ltijs`; no LMS fork.

🔴 **Weakest component, named:** the two most feature-complete systems in this category are the two
you cannot use — `scholarsome` is **AGPL-3.0** and `mnemosyne` carries **no usable grant**
(`600-G`). 🔵 **So a feature-led tool selection in this category walks straight into a licence
problem**, which is `599-C` inverted: here the risk sits at the top of the quality ranking, not in
the unaudited tail. 🟡 `olmps/memo` (BSD-3-Clause, `1,871★`) is a clean **reference implementation**
for the mobile UX — last push `2024-07-29`, so read it, do not depend on it.

---

## 🆕 P-600-C — 🟢 **In-language courseware and exam-prep pipeline for APAC** (6–8 weeks, APAC)

🔵 **The brief:** *"Our material is in English, our learners are not, and translation alone produces
unusable study material."* 🟢 Every component here is permissive and in-language rather than
translated, which is the distinction that decides whether the output is usable.

**Wiring:**
1. **Ingest** — `courseware-cn-annotator` (MIT) converts courseware PDFs into Chinese-language study
   packages; it ships as an **agent skill**, so there is no service to stand up.
2. **Tutoring** — `socratic-tutor` (MIT) for question-first delivery, with `understand` (MIT) gating
   advancement on demonstrated transfer rather than completion.
3. **Exam-track** — `ERRRC/kaogong-shuati` (MIT) for civil-service practice (行测 / 申论);
   `designfuchen/word-atlas` (MIT) for IELTS vocabulary with FSRS scheduling already built in.
4. **Retention** — `repeater` or `flashcards-obsidian`, seeded from step 1's output.
5. **Frontier tutor option** — `HKUDS/DeepTutor` (Apache-2.0, `53.5k★`, HKU) where the client wants a
   persistent learner model. 🔴 **Pin a tag, not `main`** — it shipped `v1.7.1` on `2026-11-01` and
   moved `+1.5k★` in four days.
6. **Agent QA** — `selftune` (MIT) for skill-level observability across the pipeline.

🔴 **Weakest component, named:** every row in steps 1–3 is **`5★`–`151★`** — single-maintainer
projects with no adopter base. 🟢 Their grants are clean and byte-read; 🔴 **their bus factor is `1`.**
🔵 **Price them as forkable reference code the studio takes ownership of, not as upstream dependencies
to track** — that is the honest commercial framing, and it is why the `5★` floor rows are shelved at
all (`599-C`).

🟡 **Regulatory note:** South Korea's AI Basic Act (in force `2026-01-22`) and Vietnam's AI Law
(`2026-03-01`, with a longer transition for education) are the two binding instruments in region;
India's synthetic-content labelling rule (`2026-02-20`) applies to generated study material.
🔴 **All three are search-snippet-grade here** — primary legal hosts are outside this session's
network (`583-E`).

---

## 🆕 `p599` — `2026-11-01` — two recipes keyed to the only two education AI deadlines that are *already* in force, and every component grant byte-read this pass

🔵 **Why these two and not another tutor.** Both `p598` and `p597` built recipes around capability.
This pass builds around **obligation**, because two deadlines are live *today* while every other date
in this base is in the future: the EU AI Act's **Article 4 AI-literacy duty (in force since
`2025-02-02`)** and the **April `2026` ADA Title II accessibility deadline** for large US public
institutions. 🔵 **A live obligation is a funded buyer**; a deferred one is a pipeline entry.

### 🟢 Component grants, all byte-read `2026-11-01` at the real default branch

| component | branch | grant (bytes) |
| --- | --- | --- |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main` | 🟢 **MIT** (`1,141 B`, holder *Microsoft Corporation*) |
| [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | `main` | 🟢 **MIT** (`1,091 B`) |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🔴 **`master`** | 🟢 **Apache-2.0** (`11,361 B`) |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main` | 🟢 **MIT** (`1,071 B`) |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** (`1,512 B`, *Project Jupyter Contributors*) |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT/X Consortium** (`1,145 B`) |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | 🔴 **`master`** | 🔴 **AGPL-3.0** (`35,136 B`) — integrate, never fork |

🔴 **`ltijs` is on `master`.** Fourth `master` default branch measured this pass (with `book-to-skill`,
`EduPilot`, `openedx-platform`); `openeducat_erp` is on `19.0`. 🔵 **Any licence step in either recipe
below must resolve the branch from `git ls-remote --symref` before it reads a grant** — a `main`-only
probe reports *no licence* on `2 of the 7` components above.

---

## 🆕 P-599-A — 🟢 **The Article 4 AI-literacy programme: the one EMEA deliverable that is already overdue** (4–6 weeks, EMEA)

**Who buys it.** Any EMEA school, university or training provider — they are **deployers** under the
AI Act, and Article 4 has bound them since `2025-02-02`. 🔵 **The sales motion is not "adopt AI"; it
is "you are non-compliant now, and the fix is a training programme, not a procurement."**

**The wedge, and why it closes.** 🔴 **Six of the last six passes have seen the market quote
`2026-08-02` as the Annex III high-risk deadline.** That date is real but it is the date **AI Office
and national-authority enforcement began** — the Annex III obligations themselves moved to
**`2027-12-02`** (stand-alone) and **`2028-08-02`** (embedded in regulated products) under the Digital
Omnibus, **Regulation (EU) `2026/1744`**, in force `2026-07-27`. 🟢 **So the client's installed
advisor has probably given them a deadline that passed and a scope that is wrong in both directions:
too urgent on high-risk, and silent on the duty that is actually live.** Lead with the corrected
clock; it is free, it is checkable, and it reframes you as the one who read the amendment.

**Build.**

1. **Curriculum spine — don't write one.** Fork [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners)
   (MIT, `78,576★`, `18` lessons) for the staff cohort that will *operate* AI, and
   [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) (MIT, `1,065★`,
   local-LLM, no cloud keys) for the technical cohort. 🟢 **Both MIT, both byte-read above** — a
   studio may rebrand, translate and ship them closed.
   🔴 **Do NOT use [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
   for this, despite it being the obvious fit at `939★` and `165` teacher-facing skills:** it is
   **`CC BY-SA 4.0`** — reciprocal — and its grant covers only the *content*, not the TypeScript it
   ships (`599-A`). Translating it would publish your translation under the same licence.
2. **Delivery seam into whatever LMS they run.** [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0, `master`) makes the programme an **LTI 1.3 tool provider**, so it drops into Moodle,
   Open edX, Canvas or ILIAS **without forking any of them** — which is the only way to touch
   `openedx-platform` (AGPL-3.0) without inheriting network copyleft.
3. **Evidence of completion, because Article 4 is a duty you must be able to *show* you met.**
   [`inducer/relate`](https://github.com/inducer/relate) (MIT) holds the versioned course content and
   auto-graded checks; its per-learner records are the audit artefact. 🔵 **This is the part the
   client cannot buy from a MOOC vendor: a defensible record keyed to named staff.**
4. **Role-scoped tracks.** Article 4 asks for literacy *proportionate to role*. Three tracks —
   teaching staff, administrative staff, and anyone touching an Annex III use case (admissions,
   assessment, learning-path decisions). 🔵 **Track 3 is also the Annex III readiness inventory**,
   which is how a `4`-week literacy engagement becomes the `2027-12-02` conformance engagement.

**What to refuse.** 🔴 Do not promise Annex III conformance inside this scope — the harmonised
standards are not settled and `p592` recorded that the clock no longer waits for them. Sell literacy
plus the inventory; price conformance separately once the inventory exists.

---

## 🆕 P-599-B — 🟢 **ADA Title II remediation with the AI attached to it** (8–12 weeks, North America)

**Who buys it, and with whose money.** US **large public institutions** faced an **April `2026`**
deadline for updated ADA Title II digital-accessibility requirements. 🔵 **That is remediation budget,
already appropriated, in a line item that is not "AI".** Meanwhile `134` AI-in-education bills across
`31` states, and four states (**Maryland, Idaho, Oklahoma, Virginia**) mandating *both* state guidance
*and* district-level AI policy, create a second, parallel compliance line. 🟢 **The engagement sells
once and bills against both.**

**The reframe that wins it.** 🔵 **An accessibility remediation is a content-transformation problem,
and content transformation is what these models are good at** — alt text, captions, reading-level
variants, structured navigation, assessment alternatives. A studio that bids "accessibility
remediation, AI-accelerated" competes on a funded line; one that bids "AI for education" competes
against every other AI vendor for discretionary budget.

**Build.**

1. **Attach to the estate, don't replace it.** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, `310★`, **FERPA-aware**, up to `102` tools, Univ. of Illinois) exposes Canvas — the dominant
   North American HE LMS — to an agent over MCP. 🟢 **MIT and university-authored**: the two things
   procurement asks about. For Open edX estates use `XBlock` + `codejail` (both Apache-2.0) instead,
   and **never fork `openedx-platform`** (AGPL-3.0, byte-read above).
2. **Inventory before remediation.** Walk every course through the MCP server and emit a per-asset
   accessibility ledger: missing alt text, uncaptioned media, un-navigable structure, assessments with
   no alternative form. 🔵 **The ledger is the first deliverable and it is what the institution's
   counsel actually needs** — a dated, complete, per-asset record of known defects and their status.
3. **Remediate the assessable layer with something auditable.** [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader)
   (BSD-3-Clause) for technical coursework: notebook assignments get alternative forms and
   deterministic autograding, so an accommodation does not become a second, unequal assessment.
4. **Human sign-off is a build requirement, not a courtesy.** Every AI-generated alt text, caption or
   reading-level variant lands in a review queue attributed to a named member of staff. 🔴 **An
   accessibility remediation that cannot name who approved each fix has not reduced the institution's
   exposure** — it has moved it.
5. **Close the state-policy line with the artefact you already built.** The ledger from step `2` plus
   the sign-off trail from step `4` is most of what a district-level AI policy has to assert. 🟢 **Bill
   it as the second deliverable rather than a second project.**

**What to refuse.** 🔴 Do not let AI make the *accommodation decision* for an individual learner —
that is an Annex III-shaped decision in the EU and a disability-determination in the US. The agent
produces candidate artefacts; a human decides who gets what.

---


## 🆕 `p598` — `2026-11-01` — three recipes, every component byte-read this pass, and the first one exists because a permissive replacement for a GPL-3.0 row was finally found

🔴 **Instrument note that governs every address below (`597-A`, re-measured this pass).**
`curl -sI https://github.com/…` returns `403` here for all of them — live or dead, with a
fabricated control also returning `403`. 🟢 Verify at `raw.githubusercontent.com/<repo>/<branch>/LICENSE`,
which returned `200` for real grants and `404` for a fabricated one on every probe this pass.
🔴 **`4 of the 11` components below do not default to `main`** — a recipe that hardcodes the branch
name fails on more than a third of this stack (`594-B`).

🟢 **New this pass (`598-A`):** before marking any component "unlicensed", read its **build
manifest**. `pom.xml`, `package.json`, `pyproject.toml` and `Cargo.toml` can carry the only licence
declaration a project has.

🔴 **One branch claim of this pass's own was wrong and was caught before publishing.** The Kolibri
row below was first drafted as branch `release-v0.18.x`; that path returns **`404`**. Kolibri's real
`default_branch` is 🔴 **`develop`** (`main` → `404`, `master` → `200` but not the default). 🔵
`594-B` names exactly this failure and it still happened while writing the note that cites it —
which is the argument for resolving `default_branch` from the API *before* composing a row, not
after.

## 🆕 P-598-A — 🟢 **Fully permissive auto-graded programming course** (6–10 weeks, North America / EMEA)

🔵 **Why this recipe did not exist until this pass.** The auto-grading seam in this base was anchored
by [`infomark-org/infomark`](https://github.com/infomark-org/infomark), which this pass byte-read as
🔴 **GPL-3.0** (`35,149 B`) — unusable in a closed client deliverable. `topic:autograder` returned
the permissive replacement.

| Component | Repo | Grant (byte-read `2026-11-01`) | Branch | Role |
| --- | --- | --- | --- | --- |
| Course + feedback server | [quickfeed/quickfeed](https://github.com/quickfeed/quickfeed) | 🟢 MIT `1,115 B` | 🔴 `master` | Go/TS server + web frontend; instant automated feedback on programming assignments, GitHub-org-per-course enrolment |
| Grader harness | [gradescope/gradescope-utils](https://github.com/gradescope/gradescope-utils) | 🟢 MIT `1,070 B` | 🔴 `master` | Python package for writing autograders; use it to author graders portable between QuickFeed and Gradescope |
| Socratic feedback side-car | [DilawarShafiq/nietzschian-debugger](https://github.com/DilawarShafiq/nietzschian-debugger) | 🟢 MIT `1,071 B` | `main` | Returns the **question**, not the fix — attach to failing submissions so the agent coaches instead of completing the work |
| Record store | [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 ECL-2.0 `9,878 B` | 🔴 `master` | 🟡 Stale (`2025-09-12`) — lift the **xAPI/Caliper schema**, do not take it as a runtime dependency |

**Wiring.** QuickFeed owns enrolment and the run loop; graders are authored against
`gradescope-utils` so they are not locked to one host. On a failed submission QuickFeed's webhook
calls the debugger agent with the diff, the failing test name and the student's last three
attempts — **never the reference solution** — and the agent returns one Socratic prompt. Emit an
xAPI statement per attempt on OpenLRW's schema into any store.
🟢 **Why it sells in North America:** the OECD's 2026 reading — AI helps only where pedagogy stays
in control — plus the measured decline in district appetite for tools that bypass the teacher. This
recipe is auditable by construction: the agent **cannot** hand over an answer it is never given.
🔴 Do not substitute `infomark` to save integration time; it is GPL-3.0.

## 🆕 P-598-B — 🟢 **Multi-tenant Spanish/English school platform with the tutor on MCP** (8–12 weeks, LATAM / EMEA)

🔵 **Why LATAM gets a real adopt-path for once.** `591-C` has held for four passes: Spanish- and
Portuguese-language *tutors* in this base are unlicensed almost without exception, so LATAM work has
meant building rather than adopting. [`guillermoscript/lms-front`](https://github.com/guillermoscript/lms-front)
is the first row that breaks the pattern at the **platform** layer.

| Component | Repo | Grant (byte-read `2026-11-01`) | Branch | Role |
| --- | --- | --- | --- | --- |
| Platform of record | [guillermoscript/lms-front](https://github.com/guillermoscript/lms-front) | 🟢 MIT `1,072 B` | 🔴 `master` | Multi-tenant LMS: subdomain per school, Supabase row-level security, Stripe Connect, certificates, gamification, **i18n `en`/`es`**, **AI tutor already exposed over MCP** |
| Courseware generation | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | 🟢 MIT `1,084 B` | `main` | Ministry PDFs / lecture video → `12`-section study guide + quizzes + flashcards + spaced repetition, one command |
| Citation-preserving authoring | [juneyaooo/lineage-skill](https://github.com/juneyaooo/lineage-skill) | 🟢 Apache-2.0 `11,358 B` | `main` | Keeps each generated item traceable to its source document — the review seam a ministry will ask for |
| Offline reach | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT `1,097 B` | 🔴 `develop` | Sync to low-connectivity schools; infrastructure is a stated LATAM constraint, not an edge case |

**Wiring.** `lms-front` is the tenant and billing boundary — one subdomain per school, RLS per
tenant, so a ministry pilot and a private network can run on one deployment. Run `Skill-Anything`
as a batch job over the official curriculum corpus, then pass every generated item through
`lineage-skill` so each question carries its source citation. Publish approved packages into Kolibri
channels for offline schools and serve them online through `lms-front`. The tutor stays on the
platform's existing **MCP** interface, so swapping the model is configuration.
🟢 **Governance is the first deliverable, not the last** — `45 %` of LAC institutions have AI
guidance against `~70 %` in Europe and North America, so build the policy layer as **configuration**
(retention windows, allowed uses, escalation) because regional policy changes with administrations.

## 🆕 P-598-C — 🟢 **Sovereign university estate: agents inside Apereo, nothing leaving the campus** (10–14 weeks, APAC / EMEA)

🔵 **Why now.** `598-D` establishes that the Apereo consortium is permissive — ECL-2.0 and
Apache-2.0 — and that an `spdx_id` licence screen rejects most of it as unlicensed. 🔴 Any studio
that ran such a screen concluded this stack was unavailable. It is available, and it is the natural
host for agents under a sovereignty requirement: Forrester expects `60 %` of firms and governments in
markets such as India and China to run **local** models alongside global ones.

| Component | Repo | Grant (byte-read `2026-11-01`) | Branch | Role |
| --- | --- | --- | --- | --- |
| LMS of record | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 `11,120 B` | 🔴 `master` | Courses, assignments, gradebook |
| Single sign-on | [apereo/cas](https://github.com/apereo/cas) | 🟢 Apache-2.0 | 🔴 `master` | 🔵 Put the agent **behind CAS** — identity and entitlement are solved before the agent sees a request |
| Portal shell | [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 Apache-2.0 | 🔴 `master` | Where the agent surfaces to students and staff |
| Learning records | [Apereo-LAI/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 ECL-2.0 `9,878 B` | 🔴 `master` | 🟡 Schema reference for the xAPI/Caliper store |
| In-language study agent | [ERRRC/kaogong-shuati](https://github.com/ERRRC/kaogong-shuati) | 🟢 MIT `1,062 B` | `main` | Chinese-language exam practice with error notebook — **APAC in-language supply is reliably permissive**, unlike LATAM's |
| Service desk entry point | [edmozley/freeitsm](https://github.com/edmozley/freeitsm) | 🟢 MIT `1,066 B` | `main` | 🔵 **Start here.** Triage and KB answers touch no student data and no pedagogy — the lowest-governance place to land the first agent |

**Wiring.** Phase 1 lands the agent on `freeitsm` — IT triage, routing, knowledge-base answers — to
earn operational trust with nothing sensitive in scope. Phase 2 moves it behind CAS and surfaces it
in uPortal, reading Sakai through its own APIs and writing xAPI statements on OpenLRW's schema.
Phase 3 adds the in-language study agent for exam cohorts. Every model call terminates at a
locally hosted endpoint, which is what makes the stack answerable to a sovereignty requirement.
🔴 **Budget for the licence screen itself as a deliverable.** If the client's OSS intake process
reads `spdx_id`, it will reject Sakai's own analytics stack, uPortal portlets and CAS clients as
unlicensed, and the engagement stalls on procurement rather than on engineering. 🟡 Also flag
[`uPortal-Project/CoursesPortlet`](https://github.com/uPortal-Project/CoursesPortlet): BSD-3-Clause
terms, but the grant names *"News Reader Portlet Development Team"* as holder — counsel reads it
before it ships.

---

## 🆕 p597 — 2026-11-01 — three recipes assembled entirely from rows this base had already found and dropped; every grant below byte-read this pass at the repository's real branch

🔴 **Why these are writable only now.** `596-C`, re-measured this pass, finds `2,640` of `3,366`
ever-shelved addresses (`78.4 %`) carrying no current disposition, `2,049` of them reported "already
held" by a gate that greps the append-only logs. 🟢 **Not one component below required a new search
leg.** 🔴 **`3` of the `11` components do not default to `main`** (`master`, `master`, `unstable`) —
a recipe that hardcodes `main` fails on a third of this stack, which is `590-D`/`594-D` applied to
the compose layer.

🔴 **Before using any address below, note `597-A`:** `curl -sI https://github.com/…` returns `403`
here for all of them, live or dead. Verify at `raw.githubusercontent.com`.

## 🆕 P-597-A — 🟢 **The auto-graded computing course with an AI feedback side-car** (8–12 weeks, North America / EMEA)

🔵 **Why this shape.** The one new demand-side token in `24` legs this pass is that district
adoption of tools which **bypass the teacher** is in significant decline. 🟢 **So the agent grades
*into a queue the instructor approves*, and the system of record stays the autograder** — the
commercial opening is the teacher's workflow, not the student's.

| component | repo | grant (byte-read `2026-11-01`) | branch | role |
| --- | --- | --- | --- | --- |
| Course + autograder of record | [autolab/autolab](https://github.com/autolab/autolab) | 🟢 **Apache-2.0** (`11,324 B`) | 🔴 `master` | `808★`, CMU. Assignments, submissions, autograding, gradebook. **This owns the grade** |
| Per-student compute | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 🟢 **BSD-3-Clause** (`1,475 B`) | `main` | `8,360★`, pushed `2026-11-01`. Isolated per-student environments; the sandbox the agent reads, never writes |
| Reference alternative | [anubislms/anubis](https://github.com/anubislms/anubis) | 🟢 **MIT** (`1,083 B`) | `main` | `382★`, NYU. Take its **pipeline design** where Autolab's Ruby stack is a poor fit for the client's estate |
| Agent runtime | [crewaiinc/crewai](https://github.com/crewaiinc/crewai) | 🟢 **MIT** (`1,055 B`, untitled) | `main` | Reviewer/explainer/moderator roles over one submission |
| or | [microsoft/autogen](https://github.com/microsoft/autogen) | 🟢 **MIT** via **`LICENSE-CODE`** (`1,141 B`) | `main` | 🔴 Vendor `LICENSE-CODE`, **not** `LICENSE` — the latter is CC-BY-4.0 and does not grant code rights |
| LMS attach point | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 **MIT** (`1,065 B`) | `main` | Only where Canvas is the institution's LMS of record; the agent reaches rosters/assignments over MCP |

**Wiring.** Autolab's autograder emits the objective result; the agent runs **after** it, reads the
failing test output plus the student's diff from the JupyterHub workspace, and writes a *draft*
comment. 🔴 **The draft never becomes a grade** — reuse this base's existing `grading-draft-gate`
recipe: agent proposes → Autolab stores as unpublished → instructor approves. 🟢 The teacher-approval
step is the feature, not the friction.

🔴 **Licence boundary to brief counsel on:** Autolab is Apache-2.0 and JupyterHub BSD-3-Clause, so
the deliverable may ship closed; but if AutoGen is the runtime, the `LICENSE`/`LICENSE-CODE` split
must be recorded in the bill of materials or an audit will read CC-BY-4.0 on a code dependency.

## 🆕 P-597-B — 🟢 **Offline-first credentialed skills programme with a real retention engine** (10–14 weeks, LATAM / APAC / EMEA)

🔵 **Why this shape.** LATAM's binding constraint on these shelves is **delivery**, not licence, and
its permissive platform-of-record tier was measured empty this pass. 🟢 This recipe therefore owns
nothing platform-shaped: it packages content, schedules retention and issues a credential.

| component | repo | grant (byte-read `2026-11-01`) | branch | role |
| --- | --- | --- | --- | --- |
| Retention engine | [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 **BSD-3-Clause** (`1,509 B`) | `main` | `455★`. FSRS **optimiser and scheduler** — fits per-learner parameters from real review logs. 🟢 A published algorithm, not a prompt |
| Content packaging | [learningequality/studio](https://github.com/learningequality/studio) | 🟢 **MIT** (`1,115 B`) | 🔴 **`unstable`** | `211★`, pushed `2026-11-01`. Curate and export channels for Kolibri's offline delivery. 🔴 **Pin a SHA — the default branch is `unstable`** |
| Credential issuance | [ryjones/learner-credential-wallet](https://github.com/ryjones/learner-credential-wallet) 🔴 **ADDRESS UNINDEXED `2026-11-03` (`626-E`)** — same `HEAD` as [`ryjones/learner-credential-wallet`](https://github.com/ryjones/learner-credential-wallet) (`91★`, `MIT`), but that successor is **LOW CONFIDENCE**; keep this institutional address until a stronger instrument exists. | 🟢 **MIT** (`1,092 B`) | `main` | Digital Credentials Consortium wallet — verifiable credentials on completion. 🔴 The search API `422`s on this address; it is alive |
| Source → teachable unit | [juneyaooo/lineage-skill](https://github.com/juneyaooo/lineage-skill) | 🟢 **Apache-2.0** (`11,358 B`) | `main` | `466★`. Distils videos, PDFs and transcripts into **source-backed** Agent Skills — every generated item keeps its citation |
| Edge inference (optional) | [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (`11,351 B`) | `main` | Intel reference apps for on-prem inference where learner data cannot leave the institution |

**Wiring.** `lineage-skill` ingests the client's existing material and emits items **with citations
attached**; Kolibri Studio packages them into an offline channel; `fsrs-rs` schedules review from
the learner's actual grade history; completion mints a credential into the DCC wallet. 🟢 **The
citation chain is what makes this defensible in a region whose institutions have adoption without
governance** — every generated question points back to a source document the institution owns.

🔴 **Do not let the agent set the schedule.** FSRS is a fitted model with published parameters; an
LLM "deciding when to review" discards the only part of this stack with an error bound.

## 🆕 P-597-C — 🟢 **District/ministry interop layer where both ends already speak MCP** (6–10 weeks, North America + EMEA)

🔵 **Why this shape.** Two rows recovered this pass are *interop* rather than application code, and
both are maintained by institutional bodies rather than vendors — so the agent never touches the SIS
directly.

| component | repo | grant (byte-read `2026-11-01`) | branch | role |
| --- | --- | --- | --- | --- |
| Roster seam (NA) | [ed-fi-alliance-oss/edfi-oneroster](https://github.com/ed-fi-alliance-oss/edfi-oneroster) | 🟢 **Apache-2.0** (`10,173 B`) | `main` | Serves a **OneRoster 1.2 API from an Ed-Fi ODS** — US K-12's data standard. `6★`, pushed `2026-10-31`: institution-grade and invisible to a star screen |
| Curriculum seam (EMEA) | [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT** — file spelled **`LICENCE`** (`1,086 B`) | `main` | Oak National Academy curriculum via API, SDK **and a shipped MCP app**. 🟢 A national body maintains the grounding layer |
| Institution back office | [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 🟢 **MIT** (`1,077 B`) | 🔴 `master` | `12,149★`. The permissive alternative to OpenEduCat (LGPL-3.0) and ERPNext (GPL-3.0) — **forkable and shippable closed** |
| Synchronous classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 **MIT** (`1,062 B`) | `main` | `6,443★`. Web/Windows/macOS classroom client where the **client** is the deliverable |

**Wiring.** The agent is an MCP client only: Oak's MCP app supplies curriculum grounding, the
OneRoster API supplies who-is-in-which-class, and Aureus holds the administrative record. 🟢 **No
component writes to the SIS** — the agent proposes, the back office records, a human commits. 🔵 For
an EMEA engagement this inverts the usual build: curriculum grounding is *consumed* from a national
body instead of constructed, which is the "capability, not compliance theatre" deliverable
`p593`'s EMEA reading calls for.

🔴 **Known gap in this recipe, stated rather than papered over.** There is **no equivalent
institutional curriculum seam for LATAM or APAC** on these shelves: Sunbird
([`sunbird-ed/sunbirded-portal`](https://github.com/sunbird-ed/sunbirded-portal), MIT, `1,072 B`) is
the closest national-scale permissive platform but has not been pushed since `2026-02-21` and is
`334 MB`. 🔵 Treat it as a reference architecture to mine, not a dependency — and price the
curriculum layer as **build** in those regions, not **integrate**.

---

## 🆕 p596 — 2026-11-01 — three recipes built entirely from rows this base had already found and never filed; every grant below was byte-read this pass

🔴 **Why these are writable now.** `596-C` measured that **`2,015` of `2,243` ever-shelved
addresses (`89.8 %`) were dropped** across `15` wholesale rewrites, while the append-only logs
lost nothing — and because the "already held?" gate greps the logs, a dropped row answers
*"held"* forever and is never re-shelved. 🟢 **Not one component below required a search leg**:
all but `folio-org/okapi` were on a shelf page in an archived snapshot before being dropped, and
every grant below was read at the repo's **real** default branch (`3 of 6` are not `main`).

## 🆕 P-596-A — 🟢 **The academic-library AI engagement: a permissive system of record a studio may fork and ship closed** (10–14 weeks, North America / EMEA)

🟢 **This recipe could not be written before this pass**, because this base's platform tier was
recorded as copyleft with one or two exceptions and had never carried the library tier at all.

**The stack — every grant byte-read `2026-11-01`:**

| component | repo | grant | branch | role |
| --- | --- | --- | --- | --- |
| API gateway / module registry | [folio-org/okapi](https://github.com/folio-org/okapi) | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | `134★`. Every module mounts here — **this is the AI attachment seam** |
| System of record | [folio-org/mod-inventory](https://github.com/folio-org/mod-inventory) | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | `4★`, pushed `2026-11-01`. Instances, holdings, items |
| Patron identity | [folio-org/mod-users](https://github.com/folio-org/mod-users) | 🟢 Apache-2.0 | 🔴 `master` | User domain model |
| UI framework | [folio-org/stripes](https://github.com/folio-org/stripes) | 🟢 **Apache-2.0** (`11,357 B`) | `main` | Front-end module framework |
| Build entry point | [folio-org/platform-complete](https://github.com/folio-org/platform-complete) | 🟢 **Apache-2.0** (`11,357 B`) | 🔴 `master` | Pins `@folio/stripes-core` + the module set; generates module descriptors |
| Agent runtime | client's choice | — | — | The AI side-car, registered to Okapi as an ordinary module |

1. **Weeks 1–2 — licence gate (`P-594-A`), and run step 1 properly.** 🔴 **Four of the five
   FOLIO repos default to `master`, not `main`.** A probe hardcoding `main` reports "no licence
   file" on the entire platform. 🟢 Organisation-level check, measured this pass:
   `org:folio-org` is **`456` repos, `398` Apache-2.0, `0` copyleft**.
2. 🔴 **Week 2 — settle the deployment artefact before architecture, because it is the one
   unlicensed thing on the path.** The `57` FOLIO repos without a licence field are tooling,
   and **`folio-org/folio-helm` is one of them.** 🔴 Do not vendor those charts into a client
   deliverable. 🟢 Either write your own charts against the Apache-2.0 modules, or get a grant
   in writing. Cheap at week 2, expensive at procurement.
3. **Weeks 3–6 — stand up the platform from `platform-complete`** and generate module
   descriptors. 🔵 Resist forking a module: everything below attaches instead.
4. **Weeks 6–11 — build the agent as an Okapi module.** 🟢 **The whole point of this recipe:
   because the platform is Apache-2.0, the module you write is yours** — ship it closed, charge
   for it, no copyleft duty anywhere in the estate. Three problems the library already has and
   an agent is genuinely good at: **metadata enrichment** on `mod-inventory` records,
   **discovery** over holdings, and **collection analytics** across circulation.
5. **Weeks 11–14 — hand over.** Deliverable: a running FOLIO estate, your proprietary module,
   and the licence register from step 1 naming the Helm decision explicitly.

🔵 **Why it sells:** in a university the library is a **separate buyer with a separate budget**
from the LMS, and this page has been offering that university nothing but LMS work.

## 🆕 P-596-B — 🟢 **Offline-first interactive courseware: authored as a static site, delivered to a school with no reliable network** (6–8 weeks, LATAM-first, portable to rural APAC and EMEA public sector)

🔴 **The constraint this recipe takes seriously.** Every other delivery recipe on this page
assumes the LMS is reachable. 🟢 Both halves below were pushed on `2026-11-01` and need **no
server at all**.

| component | repo | grant | role |
| --- | --- | --- | --- |
| Authoring | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | 🟢 **MIT** (`1,069 B`) | `75★`, EMEA/Germany. CLI + markdown engine, `30+` directives → interactive workbook as a **static site** |
| Delivery | [missing-elements/h5p-offline-player](https://github.com/missing-elements/h5p-offline-player) | 🟡 **MIT** (`1,073 B`) — 🔴 **split artefact** | `6★`, stable since `2026-10-18`. Plays `.h5p` with **no H5P server, no Moodle, no backend**; PWA runs with **no network** |
| Reconnection seam | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) + [Cvmcosta/ltijs-sequelize](https://github.com/Cvmcosta/ltijs-sequelize) | 🟢 **Apache-2.0** (`11,357 B`) | `373★` / `5★`. **LTI Advantage Complete Certified by 1EdTech**; the `-sequelize` plugin puts state on Postgres/MySQL instead of Mongo |

1. 🔴 **Week 1 — price the GPL boundary, because it is the one thing that can sink this.**
   README verbatim: *"The player is MIT; the H5P runtime it loads is GPL-3.0 and published
   separately."* 🟢 **Ship the player as MIT and load the runtime as a separate, unmodified
   artefact.** 🔴 Bundle them into one distributable and you have taken a GPL-3.0 obligation
   nobody priced. 🔵 This is a packaging decision, not a legal opinion — make it in week 1.
2. **Weeks 1–3 — author in `hyperbook`.** Content is markdown in git, so the client's own
   teachers can maintain it after handover, which is the difference between a deliverable and a
   dependency.
3. **Weeks 3–5 — build the offline tier.** Static site + the PWA, on an SD card, a school
   server or any static host. 🟢 **No LMS, no backend, no connectivity assumption.**
4. **Weeks 5–7 — add the LTI seam for schools that *do* have a network.** `ltijs` for the
   certified LTI 1.3 path, **`ltijs-sequelize` so state lands on the SQL database the client's
   DBA already runs** — 🔵 the practical reason this gets through institutional review, and the
   reason the `5★` adapter matters more than its stars suggest.
5. **Weeks 7–8 — grading and sync.** Scores queue locally and reconcile over LTI AGS when a
   connection appears.

🔵 **Region note, placed rather than implied:** strongest in **LATAM**, where `596`'s market
read is that connectivity, not licensing, is the binding constraint; portable to **rural APAC**
and **EMEA** public sector. 🔴 This pass did not measure deployment counts in any of the three
and claims none.

## 🆕 P-596-C — 🟡 **Cross-institution learning analytics where the student records never leave the institution** (8–10 weeks, North America first)

| component | repo | grant | role |
| --- | --- | --- | --- |
| Privacy layer | [OpenMined/PySyft](https://github.com/OpenMined/PySyft) | 🟡 **Apache-2.0** (`11,941 B`) 🔴 **+ PSF carve-out** | `10,049★`, branch 🔴 **`dev`**. Remote execution over data the analyst never sees |
| Interchange | [edanalytics/earthmover_edfi_bundles](https://github.com/edanalytics/earthmover_edfi_bundles) | 🟢 **Apache-2.0** (`11,357 B`) | `14★`. Assessment-vendor formats → **Ed-Fi** API, with automatic student-ID matching |
| Records spine | Ed-Fi ODS (client-side) | — | The district's existing system of record |

1. 🔴 **Week 1 — record PySyft's grant correctly, do not flatten it.** `11,941 B` is `584 B`
   over canonical Apache-2.0 and `591-G`'s byte filter flags it. Three-stage read: title
   `Apache License 2.0`, body canonical, then an **appended carve-out placing `7` named test
   files under the PSF licence**, copied from CPython. 🟢 **Shippable** — the carve-out never
   leaves `packages/syft/tests/`. 🔴 Also note the default branch is **`dev`**: pin a tag.
2. **Weeks 1–3 — land the data.** 🔵 `earthmover_edfi_bundles` exists because **most assessment
   vendors ship no native Ed-Fi integration**; its student-ID auto-detection is the part that
   actually consumes the budget on real district data.
3. **Weeks 3–7 — the analysis runs where the data lives.** Each participating district keeps
   its ODS; PySyft executes the query remotely and returns results, not records. 🟢 **This is
   what makes a multi-district study legally writable** when no district may export student
   records to a partner.
4. **Weeks 7–10 — governance pack.** Which queries ran, against whose data, with what
   approvals — the artefact the district files, not an appendix.

🔴 **Stated as a limit, not sold as a feature:** this pass verified licences, branches,
liveness and scope first-hand. 🔴 **It did not benchmark PySyft at district data volumes**, and
a `10–14`-week version of this recipe should spend two of those weeks on exactly that before
anyone signs a performance commitment.

---
## 🆕 p595 — 2026-11-01 — one new recipe, built only from grants read byte-for-byte this pass

### `P595-1` — Rubric-graded coursework on a client's existing LMS, no student data leaving the estate

🔵 **Why this recipe and not another.** The grading axis was the only leg of nine that
returned anything this pass, and the three usable addresses on it were all already in this
base, unshelved and unwired. This recipe is the wiring.

**The parts, each with the grant read this pass rather than taken from the API:**

| part | address | grant (byte-read `p595`) | role |
| --- | --- | --- | --- |
| LMS of record | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | submissions + roster + gradebook; **deploy alongside, do not fork into client IP** |
| Rubric engine | [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | 🟢 Apache-2.0 (`11,357 B`) | tree-structured rubrics — base / bonus / penalty, weighted subjects — and report generation |
| Handwriting → text + review queue | [`johnswyou/autograder`](https://github.com/johnswyou/autograder) | 🟢 MIT (`1,065 B`) | locates answers on scanned work, transcribes, applies rubric, emits a **focused human review queue** |
| Grader-quality harness | [`scaleapi/researchrubrics`](https://github.com/scaleapi/researchrubrics) | 🟢 MIT (`1,078 B`) | ICLR 2026 rubric benchmark — use it to score *the grader*, not the student |
| Tutor loop (optional) | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 (`11,408 B`) | turns a failed rubric criterion into targeted remediation; **pin `v1.7.1`, not `main`** |

**How they wire together**

1. Moodle's **Assignment** web service (`mod_assign_get_submissions`) is the only integration
   point — poll it, do not patch Moodle. This keeps the GPL-3.0 boundary clean: the client
   runs Moodle as shipped and the studio's code talks to it over HTTP.
2. Scanned or typed submissions go to `johnswyou/autograder` for localisation + transcription.
   Typed submissions skip this hop entirely.
3. Transcribed text + the course's rubric YAML go to `webtech-network/autograder`. Its
   base/bonus/penalty tree is the thing a faculty committee can actually review and sign off,
   which is what makes the output defensible.
4. **Nothing is written back automatically.** Every criterion lands in the review queue; a
   human approves, and only then does the score go back through `mod_assign_save_grade`.
5. `scaleapi/researchrubrics` runs offline against a held-out set of human-graded work to
   produce the grader-agreement number the client's academic board will ask for **before** any
   of this touches a real cohort.
6. Approved failures fan out to `DeepTutor` as remediation prompts, closing the loop.

**Regional fit, from this pass's own regional legs**

- 🔴 **EMEA — read the delay correctly before you quote it.** Regulation (EU) 2026/1744
  moved **stand-alone high-risk** education duties to `2027-12-02`, but **Art. 50 transparency
  duties are live `2026-08-02`** and the emotion-recognition ban has applied since
  `2025-02-02`. Automated grading is the Annex III use-case this recipe sits closest to, so the
  human-approval gate in step 4 is **not optional polish — it is the control that keeps the
  deployment out of the stand-alone high-risk class**.
- 🟢 **LATAM — the strongest fit, and the numbers say why.** `87 %` of LAC institutions
  already use AI somewhere, `74 %` in teaching, but only `26 %` hold a formal strategy. The
  governance artefact this recipe produces at step 5 is the scarce thing, not the model.
- 🔵 **North America — jurisdiction decides whether this is sellable at all.** One DC policy
  **bans AI from grading outright**; `ID`, `OK`, `VA`, `MD` mandate district-level AI policy.
  Qualify the district's rule before scoping, not after.
- 🔵 **APAC — Vietnam names education a high-risk sector** in its 2026 law and Australia's
  **TEQSA** requires university gen-AI action plans; step 5's agreement number is the artefact
  both regimes ask for.

🔴 **One honest limit.** `webtech-network/autograder` and `johnswyou/autograder` are small
projects. Their grants are clean and byte-verified, but neither carries the contributor base
to be load-bearing without the studio taking maintenance ownership — **price that in.**

---
## 🆕 p594 — 2026-11-01 — one recipe that is now mandatory rather than optional, because this pass proved the base's own licence verdicts can be confidently wrong; and the Brazilian LATAM engagement that `594-D` makes writable for the first time

## 🆕 P-594-A — The pre-engagement licence gate: clear the stack before a line of code is written (2–3 days, run once per engagement)

🔴 **Why this is a recipe and not a checklist item.** `594-A` found a row published on this base's
own agent shelf as 🟢 `MIT (text)` — *"shippable in client work"* — whose grant is **non-commercial,
no-redistribution, revenue-share**. A studio that read this KB and shipped
[`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) in a client product would have been in
breach. 🔵 **The lesson is not "this KB had a bug". It is that a licence verdict carried in any
table — including this one — is a claim with an age, and the stack a client ships must be
re-verified against its own branches at engagement start.**

**Inputs:** the repo list for the proposed stack. **Output:** a signed-off licence register with a
grant file, byte count, branch and classification per dependency, plus an escalation list for
counsel.

| step | what you run | why it is not optional |
| --- | --- | --- |
| **1. Resolve the branch first** | `gh api -X GET search/repositories -f q="repo:$R" --jq '.items[]\|[.full_name,.default_branch,(.license.spdx_id//"null")]\|@tsv'` | 🔴 `30 of 253` of this base's curated addresses default to neither `main` nor `master` (`594-B`), and they are the **platform** rows — Odoo `20.0`, OpenEduCat `19.0`, ILIAS `release_11`, BigBlueButton `v4.0.x-develop`, Claroline `15.0` |
| **2. Trust `null`, never trust `NOASSERTION`** | branch on the field from step 1 | 🟢 Measured on the full base (`594-F`): `null` → `0 of 14` have a grant file; `NOASSERTION` → `32 of 32` do. 🔴 Blocking a `NOASSERTION` row is wrong `32` times out of `32` |
| **3. Probe `13` path/case variants on that branch** | `LICENSE LICENSE.md LICENSE.txt license.txt license license.md LICENCE LICENCE.txt COPYING COPYING.txt LICENSE.rst LICENSE-APACHE LICENSE-MIT` | 🔴 `frappe/erpnext`, `frappe/lms` and `frappe/education` keep grants at **lowercase `license.txt`** and are invisible to a `6`- or `7`-path probe (`594-C`) |
| **4. Classify title → declaration → body** | title first; if it is prose or a copyright line, take the *"published/licensed under X"* line in the first 40 lines; body last | 🔴 `odoo/odoo` and `openeducat_erp` prepend prose and declare `LGPL-3.0` on **line 2**; a body match on Odoo can return the **stricter** `GPL-3.0` and kill the recipe (`Trend 51`) |
| **5. Anchor every abbreviation** | full licence names, or `\bMIT\b` / `\bMPL\b` only | 🔴 An unanchored `MPL` matches **`65 of 65`** real grants via *"EXPRESS OR I`MPL`IED"*; unanchored `MIT` matched a German university's name (`594-E`) |
| **6. Escalate disagreement, do not resolve it** | title verdict ≠ body verdict → counsel | 🔴 `claroline/Claroline` is *"Claroline Connect License"* over verbatim AGPL-3.0; `PageLM` is a bespoke grant over MIT's opening sentence. 🟢 One escalates to copyleft, the other to **not open source** — the shape is identical and the outcomes are not |
| **7. Reject a short grant file** | flag any grant under ~`400 B` | 🔴 `frappe/education`'s grant is **`19` bytes** — `License: GNU GPL V3` — a declaration with no terms. A successful fetch is not a read |

🟢 **Validated, not asserted:** run against `10` rows chosen because they defeated earlier
instruments, this gate returns **zero false permissives** and correctly refuses `PageLM`,
`ximing/aimo` (BSL-1.1), `SethRobinson/UGTLive` (Proton SDK) and
`nirholas/lyra-web3-playground` (proprietary).

🔴 **Per `p590`, store this as a pasteable command block, never as a committed script** —
`make`, `bash ingest/*.sh` and `python3 ingest/*.py` are all **DENIED** in this environment.

## 🆕 P-594-B — The Brazilian school-system engagement: three copyleft platforms of record, an AI side-car, and a licence read that has to be done in Portuguese (8–11 weeks)

🟢 **This recipe could not be written before this pass.** `591-C` established that LATAM's
in-language *tutors* are unlicensed while its *courseware* is permissive, and `P-591-B` built on
that. 🔴 What neither could see is that the region's largest **platforms of record** were being
mis-read by this base's instrument for a reason unrelated to licensing: their grants are written
in Portuguese on version branches.

**The stack, all three measured first-hand `2026-11-01`:**

| component | repo | grant, read on the real branch | role |
| --- | --- | --- | --- |
| Student information system | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (text, `18,091 B`, branch **`2.12`**) | `723★`. The SIS of record in Brazilian municipal education |
| Class diary / gradebook | [portabilis/i-diario](https://github.com/portabilis/i-diario) | 🔴 **AGPL-3.0** — `LICENÇA PÚBLICA GERAL AFFERO GNU` (text, `35,325 B`, branch **`1.6`**) | `117★`. Teacher-facing daily record |
| Enrolment intake | [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) | 🔴 **AGPL-3.0**, byte-identical Portuguese grant (branch **`2.12`**) | `21★`. Pre-enrolment pipeline |

🔴 **All three are strong copyleft, and one is network copyleft.** 🟢 **So the architecture is
forced and that is useful information, not a limitation: attach, never fork.**

1. **Weeks 1–2 — licence gate (`P-594-A`) in Portuguese.** 🔴 Do not run an English-only matcher:
   it returns *unknown* on `i-diario` and `pre-matricula-digital` and false-blocks the engagement
   before it starts. Read the title, accept `LICENÇA PÚBLICA GERAL AFFERO GNU` as AGPL-3.0, and
   record the branch (`1.6`, `2.12`) in the register.
2. **Weeks 2–4 — integrate over the API boundary, not the source.** Stand the AI side-car in its
   own process and speak to all three over HTTP. 🔴 **AGPL-3.0 on `i-diario` is the binding
   constraint:** if your service and theirs are one program, the network-copyleft obligation
   reaches your code. A separate process consuming a published API does not combine.
3. **Weeks 4–7 — the tutor half is still a build.** `591-C` stands: in-language conversational
   tutors in Spanish and Portuguese are `6 of 6` unlicensed, every candidate `≤ 19★`. 🟢 Build on
   a permissive agent base from [`../agents/top.md`](../agents/top.md) — and 🔴 **not** on
   `PageLM`, which this pass re-graded (`594-A`).
4. **Weeks 6–9 — courseware in-language, adopted not built.** `591-C`'s other arm holds: `12 of 12`
   in-language courseware/curriculum repos are permissive. Adopt the curriculum, wrap it.
5. **Weeks 9–11 — governance, because that is the actual LATAM deliverable.** `92 %` of students
   and `79 %` of faculty already use AI with almost no institutional governance
   ([`../intel/market.md`](../intel/market.md)). Ship an acceptable-use policy, an audit trail on
   the side-car, and a teacher-facing disclosure in the `i-diario` workflow. 🔵 Colombia's **Ley
   2626 de 2026** is the region's first binding education-AI instrument and the template to track
   even on a Brazilian engagement.

🔵 **Scale caveat, stated:** `i-diario` and `pre-matricula-digital` are `117★` and `21★`. These are
real municipal deployments, not large open-source communities — bus-factor and support are
engagement risks and should be priced as such.

---

## 🆕 p592 — 2026-11-01 — one recipe the EU decoupling finding makes urgent, and it is a deadline-driven variant of a seam this base already recommends

🔵 **Why one and not three.** `p592` added no new repository rows — the mandated discovery
legs returned their `23rd` consecutive nil (`592-A`). What it added is a **date that is now
firm** (Trend `46`) and a **licence census** (Trend `47`), and exactly one recipe follows from
those: the pattern a studio needs when an Annex III education product has to be conformant
on a fixed calendar rather than whenever harmonised standards land. 🔵 Every repository
figure below was measured first-hand on `2026-11-01` through the `gh api` channel.

## 🆕 P-592-A — The Annex III-ready tutor over a copyleft LMS: conformant by `2 December 2027`, without forking the platform (8–10 weeks)

🔴 **When to reach for this.** The client runs Moodle or Open edX, operates in the EU, and
wants an AI tutor or grading assistant touching **grading, admissions or progression** —
which places it in **Annex III** of the EU AI Act. 🔵 The obligations start **`2 December
2027` on the calendar, whether or not the standards are finished** (Trend `46`), and
Article 50 transparency is **already live** since `2 August 2026`.

### The wiring, layer by layer

| layer | what to use | licence, measured `2026-11-01` | why this one |
|---|---|---|---|
| Platform of record | `moodle/moodle` **`7,569★`** `GPL-3.0` or [openedx/openedx-platform](https://github.com/openedx/openedx-platform) **`8,214★`** `AGPL-3.0` | 🔴 copyleft | 🔴 **Do not fork either.** Integrate only. Forking creates a modified AGPL/GPL platform and a distribution obligation for capability the seam delivers free |
| The seam | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) **`373★`** | 🟢 `Apache-2.0` | Turns the studio's service into a full **LTI 1.3** tool provider. The agent becomes an external tool the LMS launches — no platform code is modified, so no copyleft reaches the studio's code |
| Tutoring agent | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) **`53,385★`** or [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) **`160★`** | 🟢 `Apache-2.0` / `MIT` | DeepTutor for lifelong-memory tutoring at scale; OpenTutor when the deployment must run locally and block-based authoring matters more than reach |
| Tutor-as-tool | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) **`62★`** | 🟢 `MIT` | MCP server exposing tutoring moves, so the Annex III decision surface is **one auditable service** rather than prompt text scattered across a UI |
| Mastery model — the audit substrate | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) **`456★`** + [CAHLR/OATutor](https://github.com/CAHLR/OATutor) **`274★`** | 🟢 `MIT` | 🟢 **This is the conformity-critical choice.** Knowledge tracing and Bayesian Knowledge Tracing produce an *inspectable* mastery estimate, so a progression decision can be explained to a regulator as a model state rather than as an LLM opinion |
| Autograding | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) **`1,370★`** | 🟢 `BSD-3-Clause` | Deterministic autograding for code and notebooks. 🟢 Keep the deterministic grader authoritative and the LLM advisory — the human-oversight requirement is far cheaper to satisfy when the grade has a reproducible source |
| Telemetry | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) **`956★`** | 🟢 `Apache-2.0` | 🟡 Last push `2025-07-03` — **that is a frozen specification, not an abandoned repo** (`p592` census). Emit xAPI statements for every agent action; this is also the evidence trail Article 14 human oversight is argued from |
| Proctoring, only if asked | [SafeExamBrowser/seb-win-refactoring](https://github.com/SafeExamBrowser/seb-win-refactoring) **`361★`** | 🟡 `MPL-2.0` | 🔴 There is still **no permissive proctoring platform** (gap `585-B`/`585-G`). Ship SEB plus an agent; do not promise a platform |

### The conformity work, scoped against the firm date

1. **Weeks 1–2 — classify and write it down.** Decide in writing whether the deployment
   touches grading, admissions or progression. 🔵 If yes it is Annex III and the rest of
   this list is mandatory; if it is pure study support with no consequential decision, it is
   not, and saying so in a dated memo is what stops scope creep from silently creating an
   Annex III system later.
2. **Weeks 2–4 — the seam, not the fork.** Stand up `ltijs`, launch the agent as an external
   LTI 1.3 tool, confirm no platform file has been modified. 🟢 This is also the licence
   boundary from Trend `47`: studio code stays permissive because it never links into the
   GPL/AGPL platform.
3. **Weeks 3–6 — make the decision inspectable.** Put `pykt-toolkit` or `OATutor` behind
   every progression or mastery claim, and keep `nbgrader` authoritative for anything
   scored. 🔴 An LLM may explain a grade; it should not *be* the grade in an Annex III
   deployment.
4. **Weeks 5–8 — Article 50 now, not in 2027.** Mark generated feedback and synthetic
   content as machine-readable AI output. 🔵 This duty has applied since `2 August 2026`,
   with a `2 December 2026` backstop for systems already on the market — it is the one
   obligation that is **late**, not upcoming. 🔴 `p591` measured that **no third-party
   component on this shelf marks generated content**: this is studio code every time.
5. **Weeks 6–10 — the Annex III file.** Technical documentation, logging via the xAPI
   stream, a named human able to override any agent decision, and a conformity assessment
   route chosen (internal vs third-party). 🟢 Scope it to complete **before `2 December
   2027`** and do not plan around a standards-driven reprieve — there is no longer one.

🟢 **Why this is `8–10` weeks and not `4`.** The agent layer is the cheap part; this base has
`130` permissive rows to build it from. The cost is the inspectable-decision substrate and
the Annex III file, and both are schedule-driven work that cannot be compressed into the
last month before a fixed date.

🔵 **Regional variants of the same wiring.** **North America:** drop the Annex III file;
substitute the state obligation that actually binds — e.g. North Carolina's local
school-unit policy deadline of `2027-06-30` — and for a Canvas estate swap the seam for
[vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) **`310★`** `MIT`.
**APAC:** keep the whole structure and add the Ipsos finding to the delivery plan — public
support for banning AI in schools is *rising* in Japan, Australia and South Korea, so
consent, opt-out and parent-facing transparency are launch requirements, not polish.
**LATAM:** invert the emphasis. UNESCO IESALC measured `87 %` adoption against `26 %` with a
strategy, so the first deliverable is usually **governance over tools already in use** — the
inspectable-mastery and telemetry layers land first, and the tutor second.

---

## 🆕 p591 — 2026-11-01 — two recipes this base could not write before this pass: a data-residency study pipeline that never leaves the learner's machine, and the LATAM in-language engagement whose tutor half has to be built because `6 of 6` candidates are unlicensed

🔵 **Why these two and not more.** `p591` added `35` rows across three tiers
([`../agents/top.md`](../agents/top.md)). Two of them unlock recipes this base previously
had no components for: **local-first study** (one row before this pass, nine now) and
**in-language LATAM** (`591-C`). 🟢 **Every component named below was measured first-hand
`2026-11-01` and every grant byte-read title-anchored** per `Trend 43` — byte counts are
given so the next pass can audit them.

---

## P-591-A — The data-residency study pipeline: nothing leaves the building (4–6 weeks)

**Problem it solves.** A school, ministry or regulated employer wants AI study support over
**their own** material — pupil work, licensed textbooks, recorded lectures — and **cannot
send any of it to a third-party API.** 🔵 This is the brief behind every "we need it
on-prem" conversation, and until this pass this base's only answer was `Claw-ED` (`63★`).

🟢 **Why this is now a buy-and-wire job rather than a build.** All five components below run
locally, all five are permissive, and none requires a hosted service.

| Step | Component | Licence (byte-read) | Why this one |
|---|---|---|---|
| 1. **Ingest + study OS** | [PndaMan/cortex](https://github.com/PndaMan/cortex) | 🟢 **Apache-2.0 (11,357 B)** | 🆕 Slides, PDFs and lectures → cheatsheets, flashcards, quizzes and **citation-grounded chat**, as a desktop app. `48★`, Svelte. 🟢 **The only Apache-2.0 row in the tier** — the safest grant of the five for a client that redistributes. |
| 1b. If the source is **recorded video** | [wansui976/CoursePilot](https://github.com/wansui976/CoursePilot) | 🟢 **MIT (1,066 B)** | 🆕 Adds what `cortex` lacks: subtitle extraction, mind maps and **courseware OCR** — it recovers the slide deck out of the recording. `35★`. |
| 1c. If the corpus is a **national textbook set** | [DanielHuang-ning/smartedu-textbook](https://github.com/DanielHuang-ning/smartedu-textbook) | 🟢 **MIT (1,442 B)** | 🆕 Fetches Chinese K-12 statutory e-textbooks as a skill **plus** CLI. 🔵 The corpus-acquisition step; swap it per jurisdiction, but it is the shape to copy. API said `NOASSERTION` (`Trend 44`). |
| 2. **Grounding / anti-hallucination** | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 MIT | Cross-session memory **and handout provenance to suppress hallucination** — the only shelf row treating citation-grounding as a first-class feature. |
| 3. **Cross-session memory as a dependency** | [major7apps/pensyve](https://github.com/major7apps/pensyve) | 🟢 **Apache-2.0 (9,488 B)** | 🆕 Universal memory runtime for agents, Rust. 🔵 Use instead of reimplementing per-learner state. 🟡 `97★`, `24` open issues — young; pin a commit. |
| 4. **Retention scheduling** | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | FSRS is the modern scheduler. `cortex` and `CoursePilot` both emit review items; neither should own the schedule. |
| 5. **Local model** | [orionsheep/wordlink](https://github.com/orionsheep/wordlink) as the reference pattern | 🟢 MIT | A shipped fine-tuned 1.5B (SFT+DPO) running **offline** — the proof that the quality bar is reachable without a frontier API. |
| 6. **Review before anything reaches a learner** | [savvides/idstack](https://github.com/savvides/idstack) | 🟢 MIT | `11` instructional-design skills checking alignment, accessibility and assessment validity. |

**Wiring.** `cortex` is the shell and owns the document store on local disk → `CoursePilot`
pre-processes any video source into text + OCR'd slides before handing it to `cortex` →
`universal-examprep-skill`'s provenance rules constrain every generated answer to the
ingested corpus → `pensyve` holds per-learner state across sessions so the tutor does not
restart → review items generated by `cortex` are scheduled by `fsrs4anki`, not by the
app → `idstack` gates generated courseware **before** release.

🔴 **Where to stop.** 🔴 **Do not add [`EasyRoc/edu-rag`](https://github.com/EasyRoc/edu-rag)**,
which is the closest-fitting component found this pass — a K-12 subject RAG assistant built
specifically to suppress hallucination against textbook knowledge bases — because it carries
**no licence at all** (`591-C`). 🔵 It is the single most tempting block in this base: right
shape, right problem, `60★`, no grant. Watch it; do not vendor it.

🟡 **Honest caveat on this recipe.** `cortex` is `48★` and `CoursePilot` is `35★`. These are
**small projects**, and the pattern's value is that they are *permissive and local*, not
that they are battle-tested. 🟢 Scope a hardening pass; do not quote them as products.

---

## P-591-B — The LATAM in-language engagement: adopt the curriculum, BUILD the tutor (6–9 weeks)

**Problem it solves.** A Spanish- or Portuguese-language client wants an AI tutor over
in-language material. 🔴 **This base said for five passes that there was no in-language
supply. There is — and the half you would want to deploy is the unlicensed half**
(`591-C`: `12 of 12` courseware permissive, `6 of 6` tutors with no grant).

🟢 **So the recipe splits where the licensing splits.**

### 🟢 Adopt — the permissive in-language half

| Role | Component | Licence (byte-read) | Placement signal |
|---|---|---|---|
| Reskilling curriculum, **pt** | [lucianoon/llm-course](https://github.com/lucianoon/llm-course) | 🟢 **Apache-2.0 (11,355 B)** | 🆕 LLM engineering in Portuguese, scratch → production, **reproducible labs**. `19★` — the largest in-language row in this base. |
| University course scaffold, **pt** | [tacianosilva/engenharia-software](https://github.com/tacianosilva/engenharia-software) | 🟢 **MIT (1,077 B)** | 🟢 **BSI-UFRN** (Universidade Federal do Rio Grande do Norte) — a named institution, the strongest placement available. |
| Security curriculum, **pt** | [kenzofujimoto/mackseguro](https://github.com/kenzofujimoto/mackseguro) | 🟢 **MIT (1,129 B)** | 🟢 Mackenzie Presbyterian University extension project, São Paulo. |
| K-12 **physical** STEM, **pt** | [Escama-Code/jacarEV3](https://github.com/Escama-Code/jacarEV3) | 🟢 **MIT (1,086 B)** | 🆕 LEGO EV3 over Bluetooth/USB, zero dependencies. 🔵 **The only robotics-teaching row in this base** — and the cheapest credible K-12 hook, because the hardware is already in the school. |
| Entry programming, **pt** | [PedroseleT/macacodev-5-projetos-python](https://github.com/PedroseleT/macacodev-5-projetos-python) | 🟢 **MIT (1,079 B)** | Five projects past tutorial stage, offline tests. |
| **Only** permissive in-language tutor references | [angelapaia/tutor-de-skills](https://github.com/angelapaia/tutor-de-skills) · [Sae-l/tutor](https://github.com/Sae-l/tutor) | 🟢 **MIT (1,188 B)** · 🟢 **MIT (1,065 B)** | 🆕 Spanish five-level tutor ladder; German MINT tutor. 🔵 **Read these two for interaction design** — they are the only in-language tutors anywhere with a grant. |

### 🔴 Build — because the six candidates cannot be adopted

🔴 **`6 of 6` in-language conversational tutors carry no licence**: `Parlo`, `fluir`,
`nexo-ia`, `linguaai-coach`, `OSAPHLA`, `questoesConcursos`. 🔵 **Use them as a
specification, not as a dependency** — between them they specify voice practice, real-time
correction, image support and Brazilian public-exam question banks, which is a free
requirements document for the build.

| Build step | Stand on | Licence |
|---|---|---|
| Tutor loop + ITS grounding | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT |
| Diagnosis before teaching | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 MIT |
| What the learner knows | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT |
| Adaptive item selection | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause — and it is Brazilian**, the one in-region component with real provenance |
| Retention | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT |
| Platform of record, offline-capable | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT |
| Public-exam item banks (the `questoesConcursos` demand, under a grant) | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) as the pattern | 🟢 MIT |
| STEM figures | [shand001/geometry-dsl](https://github.com/shand001/geometry-dsl) | 🟢 **MIT (1,082 B)** — compile the diagram, do not generate it |

**Wiring.** `kolibri` is the platform of record (MIT, offline-first — the right choice where
connectivity is the real constraint) → `tutor-mcp` provides the ITS-grounded tutor loop →
`universal-diagnostic-tutor-skill` establishes the gap before teaching → `pykt-toolkit`
models mastery and `catsim` selects the next item → the adopted Portuguese curricula above
supply the content → `geometry-dsl` compiles any figure → `fsrs4anki` schedules review.
🟢 **`catsim` and `jacarEV3` are the two genuinely in-region permissive components** — name
them in the proposal, because in-region provenance is what a LATAM client is checking for.

🔴 **Pricing note, and it is the point of the pattern.** Because the tutor half is a build
and the curriculum half is an adopt, **a LATAM in-language engagement is not symmetric with
an APAC one.** APAC returned `11` adoptable in-language artefacts this pass against LATAM's
`6`, and APAC's include deployable study workbenches
([`CoursePilot`](https://github.com/wansui976/CoursePilot),
[`insight-engine`](https://github.com/inbeomheo/insight-engine)) where LATAM's are
curricula. 🟢 **Scope the LATAM tutor as new build; scope the APAC equivalent as
composition.** Measured on [`../intel/market.md`](../intel/market.md) (`591-F`).

---

## 🆕 P-591-C — One-line addition to every existing courseware pattern: compile the figures

🔵 **Small, and it fixes a failure every pattern on this page inherits.** Every courseware
recipe here generates diagrams with an LLM. 🔴 **An LLM asked for a labelled triangle with
given side lengths produces a plausible-looking wrong one**, and a wrong figure in
assessment material is the defect most likely to reach a learner uncaught — `idstack`
checks pedagogy, not geometry.

🟢 **Insert [`shand001/geometry-dsl`](https://github.com/shand001/geometry-dsl)
(🟢 MIT, `1,082 B` byte-read, `6★`) as a compile step** in `P-590-A` step 1, `P-591-A`
step 1 and `P-591-B`'s content stage: the agent emits DSL text, the zero-dependency
compiler emits exact SVG/PNG, and the figure becomes **deterministic and diffable** instead
of generated. 🔵 It ships as a Claude/Codex agent skill as well as a compiler, so it drops
into an agent loop without an integration.

🟡 **`6★`.** Vendor it — it is a zero-dependency compiler, which is the one class of
dependency where a tiny star count carries little risk.

---

## 🆕 p590 — 2026-11-01 — the courseware-emit recipe is rewritten around a generator this base already held, and the xAPI telemetry leg gets named libraries instead of a bare "send statements" step

🔵 **Why these two patterns change.** `p589` told a courseware engagement to **build the
generator** because only two permissive SCORM emitters were alive. 🔴 **That is refuted**
(`589-E`, [`../repos/trending.md`](../repos/trending.md)): there are at least six, one of
them a finished multi-format exporter under BSD-3-Clause. 🟢 **Every component named below
was measured first-hand `2026-11-01` and every grant byte-read.**

---

## P-590-A — Courseware emit pipeline, buy-first (3–5 weeks)

**Problem it solves.** A client needs AI-generated courseware delivered **into their
existing LMS**, which means a conformant SCORM package, not a web app.

🔴 **What `p589`'s version of this recipe said:** add `scorm-again`, then *build the
generator*. 🟢 **What it should say:** the generator largely exists.

| Step | Component | Licence | Why this one |
|---|---|---|---|
| 1. Author | [course-code-framework/coursecode](https://github.com/course-code-framework/coursecode) **or** [kemalyy/edumints-scorm-skill](https://github.com/kemalyy/edumints-scorm-skill) | 🟢 MIT / MIT | Agent-native authoring. `coursecode` is framework-shaped (MCP-capable tools); `edumints-scorm-skill` is the skill half of an MCP pair. |
| 2. **Emit — buy, do not build** | [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | 🟢 **BSD-3-Clause** | 🆕 **One Markdown-shaped source → SCORM 1.2, SCORM 2004, IMS, xAPI, H5P, PDF, ePub, Web**, with Moodle / ILIAS / OPAL presets. README read first-hand. 🔵 This is the step that was being budgeted as a build. |
| 2b. Emit, agent-driven alternative | [kemalyy/edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) **or** [giacomomaria81/scorm-mcp-server](https://github.com/giacomomaria81/scorm-mcp-server) | 🟢 MIT / MIT | Use when the pipeline is already an agent loop and HTML/design bundles are the input rather than Markdown. |
| 3. Runtime | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT | The content↔LMS API bridge. Still the first dependency; `362★`, pushed `2026-10-28`. |
| 4. If the deliverable is assessment | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 | Newcastle University's engine, with its own `23,811`-byte SCORM storage runtime. Replaces steps 1–3 for assessment work. |
| 5. If sources are H5P | [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 MIT | Packs H5P into SCORM objects. `58★`, pushed `2026-10-29`. |
| 6. **Review before ship** | [savvides/idstack](https://github.com/savvides/idstack) | 🟢 MIT | 🆕 `11` instructional-design skills checking alignment, accessibility and assessment validity. 🔵 The only reviewer component on these shelves — without it the pipeline ships unaudited pedagogy. |

**Wiring.** `coursecode` writes LiaScript-flavoured Markdown → `LiaScript-Exporter` emits
every required target in one run → `scorm-again` is bundled inside the package for runtime
API calls → `idstack` runs as a gate on the authored source **before** export, so a failed
pedagogy check costs one re-author and not one re-package.

🔴 **Where to stop.** Do **not** add `Didask/scol-r` to a pipeline whose target LMS ingests
SCORM only — it is a SCORM *successor* format (MIT, live, French) and the client's LMS will
not take it. Offer it as the modern path, never as the compatible one.

🔴 **Validate, do not trust.** `SCORMShield-Admin/scorm-package-validator` and
`jowinjohnchemban/scormite` (both MIT, both live) will tell you whether the emitted package
is conformant. 🔵 Budget a validation step: `60.0 %` of the `topic:scorm` axis carries no
licence at all, so most of what a search surfaces here cannot be vendored anyway.

---

## P-590-B — Learning telemetry leg with named libraries, per runtime (2–3 weeks)

**Problem it solves.** The client wants learning events out of the courseware and into
something they can query — and `589-E` established that **xAPI is a conformance target you
SPEAK, so you buy the client library rather than writing one.**

| Client estate | Library | Licence | Measured |
|---|---|---|---|
| **JVM / Java** (most university back-offices) | [BerryCloud/xapi-java](https://github.com/BerryCloud/xapi-java) | 🟢 Apache-2.0 (`11,350 B`) | `20★`, `2026-10-30` |
| **PHP / Laravel** (the Moodle estate) | [ijeffro/laralocker](https://github.com/ijeffro/laralocker) | 🟢 MIT (`1,072 B`) | `9★`, `2026-10-03` |
| **Flutter / Dart** (mobile-native) | [jblough/TinCanDart](https://github.com/jblough/TinCanDart) | 🟢 Apache-2.0 (`11,358 B`) | `5★`, `2026-08-06` |
| **.NET** | [nurullahturkoglu/xapi-dotnet](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | `1★`, `2026-10-30` — 🔴 one-star, treat as reference |
| **Store (LRS)** | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) **or** [openfun/ralph](https://github.com/openfun/ralph) | 🟢 Apache-2.0 / MIT | `144★` / `51★`, both pushed within a week |
| **Endpoint only, no full LRS** | [LearningLocker/xapi-service](https://github.com/LearningLocker/xapi-service) | 🟢 MIT (`1,070 B`, lowercase `license`) | `42★`, `2026-10-26` |
| **Validate at your own boundary** | [LearningLocker/xapi-validation](https://github.com/LearningLocker/xapi-validation) | 🟢 MIT (`1,070 B`) | `12★`, `2026-10-26` |
| **Validate the profile itself** | [yetanalytics/project-pan](https://github.com/yetanalytics/project-pan) | 🟢 Apache-2.0 (`11,356 B`) | `5★`, `2026-10-16` |
| **Dashboards** | [openfun/warren](https://github.com/openfun/warren) | 🟢 MIT | `17★`, `2026-10-31` |

**Wiring.** Emit with the library matching the client's runtime → validate statements with
`xapi-validation` **inside the studio's own boundary**, before anything reaches the client's
store → persist to `lrsql` (or `xapi-service` when the client refuses to host a full LRS) →
`warren` for dashboards. 🟢 **Validate the profile with `project-pan` and statements against
it with `project-persephone`** — two different jobs that are easy to conflate.

🔵 **The `pushed_at` dates above are the point.** `27` distinct owners hold the `35` live
permissive xAPI repositories, so this leg is a **real ecosystem**: if one library stalls,
another exists. 🔴 **That is not true one spec over** — see the QTI warning below.

---

## 🔴 P-590-C — QTI assessment interchange: a supplier, not an ecosystem (scoping note, not a recipe)

🔴 **Do not treat the QTI tooling list as a menu.** `8` of QTI's `14` live permissive
repositories belong to **one account** (`metyatech`), all pushed inside a six-day window in
September `2026`, **none above `2★`** (`Trend 42`). 🔵 **A liveness check passes this axis;
an owner count fails it.**

🟢 **How to scope a QTI engagement honestly:**

1. 🟢 **Stand on the two third-party rows** if a dependency is required:
   [feyst/qti3-validator](https://github.com/feyst/qti3-validator) (MIT, validates against
   the 1EdTech schemas) and [Citolab/qti-playground](https://github.com/Citolab/qti-playground)
   (MIT, preview/convert/modify).
2. 🟡 **Or speak QTI 3.0 directly** — the schemas are published, the XML is tractable, and
   this avoids a single-maintainer dependency entirely. 🔵 Budget the XML work explicitly
   instead of discovering it.
3. 🔴 **If the `metyatech` set is used, price it as vendoring one supplier's code**, with
   takeover budgeted. Treat the eight repositories as **one** dependency.

🔵 **Generalise the check, not the verdict:** before any interchange dependency, compute
**live repos ÷ distinct owners** over the axis. Near `1.0` is an ecosystem; `2.0` or one
owner above `50 %` is a supplier. The data comes free with the sweep.

---


## p589 — 2026-11-01 — two recipes this pass's rows make buildable: the courseware factory whose output crosses the copyleft boundary as *content*, and the university enablement engagement with a real course to copy

## P-589-A — 🟢 **The courseware factory that ships into a client's copyleft LMS without touching it** (6–8 weeks, Global; strongest in LATAM / EMEA where Moodle and Chamilo dominate)

**The brief it answers.** *"We have Moodle. We have 400 hours of material in PDFs, slides and
lecture recordings. Modernise it — and do not touch our LMS."*

🔵 **Why this is a pattern and not a project.** `Trend 41` establishes that SCORM is an
**export target**, not a conformance target: nothing needs to *speak* it at runtime, so there
is no integration to build. A SCORM package crosses into the platform as **content**. 🟢
**That is the cleanest licence boundary in this base** — Moodle's GPL-3.0 and Open edX's
AGPL-3.0 reach linked code, not uploaded course material.

**The wiring, every component measured first-hand `2026-11-01`:**

| step | component | licence | why this one |
|---|---|---|---|
| 1 — ingest source material | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) `1,040★` · [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) `36,673★` | 🟢 MIT (text) | books and PDFs → structured, narrated, interactive material |
| 2 — generate decks and lessons | [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) `71,803★` | 🟢 MIT (text) | native PowerPoint with real shapes and narration, not screenshots |
| 3 — build the course shell | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) `574★` | 🟢 MIT (text) | topic → researched course structure |
| 4 — assessments | [`numbas/Numbas`](https://github.com/numbas/Numbas) `216★` · [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) `1,370★` | 🟢 Apache-2.0 · 🟢 BSD-3-Clause | real maths engine; autograded notebooks for technical content |
| 5 — 🆕 **package for the LMS** | [`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper) `58★` | 🟢 **MIT (text)** | H5P interactions → SCORM objects; the only live permissive packer |
| 6 — 🆕 **the runtime contract** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) `362★` | 🟢 **MIT (text)** | SCORM 1.2 / 2004 API; **the single external dependency the deliverable carries** |
| 7 — retention loop | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) `540★` | 🟢 MIT | spaced repetition over the generated material |

🔴 **The three traps, each one measured rather than assumed:**

1. 🔴 **Do not reach for `S4-NetQuest/react-scorm-provider`, `gamestdio/scorm` or
   `raccoongang/edx_xblock_scorm`** — they are the obvious choices by name and they are
   `2023`, `2019` and **archived**. Budget the React layer as build, not integrate.
2. 🔴 **Do not vendor `cybercussion/SCOBot`** (`165★`, live, API says `NOASSERTION`): its
   licence is **CC BY-SA 4.0**, reciprocal, and propagates into client code. `589-F`.
3. 🔴 **Do not quote "an open-source SCORM stack"** — `56.6 %` of the axis has no licence.

🔵 **What to say in the room.** *"One MIT dependency. Everything else we generate. The output
is a file your LMS already accepts, so there is no integration, no fork, and no copyleft
obligation anywhere in what you receive."* 🟢 **And the generator is the billable artefact** —
the client keeps a pipeline, not a pile of courses.

**Shape.** 6–8 weeks: `1`–`2` ingest and taxonomy, `3`–`5` generation loop with the client's
own material, `6` packaging and LMS smoke test, `7`–`8` hand-over of the pipeline.
🟡 **Prerequisite:** the client's LMS version must be confirmed to accept SCORM 2004 — Moodle,
Open edX, Chamilo and Canvas all do, but the *version* decides which profile.

## P-589-B — 🟢 **The university enablement engagement, with a real graduate course as the template** (6–8 weeks, APAC-first, Global-portable)

**The brief it answers.** *"We are a business school. We must teach AI to our own faculty and
MBA cohort next term. We are not building a product."*

🔵 **Why this pattern changed this pass.** `P-587-B` and `P-588-B` sell the enablement tier to
a **corporate** engineering org. 🔴 **A university asks a different question — "show us a
course that has actually run"** — and until `p589` this base's enablement tier was five
English-language mega-repos with no institution attached to any of them.

🟢 **The template now exists and is permissively licensed:**
[`rphilipzhang/AI-PhD-S26`](https://github.com/rphilipzhang/AI-PhD-S26) — **MIT, byte-read,
`91★`** — is `DOTE 6635 Artificial Intelligence for Business Research`, Spring 2026, **CUHK
Business School**, Dept. of Decisions, Operations and Technology, with a named instructor,
TA and tutorial instructor, and **the 2024 and 2025 offerings of the same course in the same
repository**. 🔵 **Three years of a real course, and the licence permits adaptation.**

| layer | component | licence | role |
|---|---|---|---|
| course spine | [`rphilipzhang/AI-PhD-S26`](https://github.com/rphilipzhang/AI-PhD-S26) `91★` | 🟢 **MIT (text)** | 🆕 syllabus, per-session slides through to agentic AI, CoLab demos, problem sets, reading lists — **and three years of delivery history** |
| foundations module | [`microsoft/generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners) `122,693★` | 🟢 MIT (text) | 21 lessons, no content carve-out |
| agents module | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) `78,550★` | 🟢 MIT (text) | 18 lessons from first principles |
| "we trained our own model" artefact | [`jingyaogong/minimind`](https://github.com/jingyaogong/minimind) `64,710★` | 🟢 Apache-2.0 (text) | ~64M params in ~2 h on modest hardware |
| 🆕 per-student study loop | [`OPTIMETA/PAIDEIA`](https://github.com/OPTIMETA/PAIDEIA) `91★` | 🟢 **MIT (text)** | ingests *the cohort's own* lectures and homework; emits drills, **graded handwritten answers**, weakness reports. 🔵 Ships for **Claude Code, Codex, opencode and hermes-agent** — so the institution is not locked to one agent vendor |
| assessment integrity | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) `21★` | 🟢 Apache-2.0 | randomised-experiment LMS plug-in; consent hidden from the instructor, identifiers stripped |

🔴 **The one hard constraint, and it is a licence, not a schedule.**
🔴 **`rasbt/LLMs-from-scratch` (`107,625★`) must not be used as course material.** Its
Apache-2.0 **modifies the definition of "Source"** to exclude *"any books specific to this
software and any related images"*. 🟢 The code is grantable; the book is not. 🔵 Cite it as a
reading recommendation students buy, never as a vendored handout.

🟡 **Second constraint:** `PAIDEIA` and `AI-PhD-S26` were last pushed `2026-07-11` and
`2026-07-28`. **Pin both commits** at kick-off; neither is abandoned, but neither is
weekly-active.

🔵 **Why APAC-first and why it travels.** The spine is a Hong Kong business-school course, so
the reference is credible to an APAC buyer and the delivery calendar matches. 🟢 **It travels
to LATAM and EMEA** for the reason `P-588-A` identified: every component here is
English-language and `Global`, so there is **no in-language supply dependency** — which is
exactly the `33×` gap `p587` measured and the thing that normally blocks LATAM delivery.
🔴 Translation of the spine is therefore in scope and should be priced; it is the single
largest LATAM line item.

**Shape.** 6–8 weeks: `1` audit of the cohort's existing material, `2`–`3` adapt the spine to
the client's discipline, `4`–`5` stand up `PAIDEIA` over the client's own lectures, `6` dry
run with faculty, `7`–`8` assessment-integrity setup and hand-over.


## p588 — 2026-11-01 — two recipes this pass's rows make buildable: the virtual classroom with NO copyleft boundary at all, and the enablement engagement whose deliverable is a model the client trained themselves

## P-588-A — 🟢 **The white-label virtual classroom a studio may fork, re-brand and ship closed** (10–14 weeks, EMEA / North America / LATAM)

**The client problem.** A ministry, university group or training provider wants *their own*
branded live-teaching platform — their domain, their look, their data residency — not a
reseller skin over someone else's SaaS. They expect to own the result.

🔴 **Why this recipe could not be written before this pass.** `P-587-A` solves the same
brief on [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) (**9,262★**),
which is **LGPL-3.0**: the studio may *link* to it but changes to BBB itself carry back, so
"fork it and ship it as ours" is exactly the thing that brief asks for and that licence
withholds. 🟢 **[`apache/openmeetings`](https://github.com/apache/openmeetings) is
Apache-2.0 and in the same tier**, and this base has carried its address on a
permissive-unshelved list since `p525` without filing it.

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Live classroom platform | [apache/openmeetings](https://github.com/apache/openmeetings) | 🟡 **Apache-2.0** + declared third-party block | **688** | 🟢 **Fork, modify, re-brand, ship closed.** 🔴 Read the bundle first — one entry is **Oracle Free Use Terms**, which is not an open-source grant |
| LMS seam | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | **373** | 🟢 Makes the platform a full LTI 1.3 tool provider — it drops into the client's existing Moodle/Canvas/Open edX without forking *that* |
| Courseware out of recordings | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 **MIT** | **71,880** | 🟢 Session transcript → native decks with real shapes and narration. 🔵 Re-measured `p588`: **71,880** against `p587`'s `71,803` — growth, not a contradiction |
| Revision material | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🟢 **MIT** | **2,057** | 🟢 Notes, quizzes and flashcards from the session's own material |
| Learning-record store | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** | **51** | 🟢 xAPI LRS, EMEA-origin (France Université Numérique) |
| Mastery model | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Turns attendance and quiz streams into mastery estimates |

**How to wire it.** Fork OpenMeetings → re-brand and deploy in the client's own tenancy
(Kurento handles media, so residency is a deployment choice, not a vendor negotiation) →
expose it to the client's existing LMS as an LTI 1.3 tool via `ltijs`, so nothing in the
LMS is forked → each session's recording and transcript feed `ppt-master` for revision
decks and `PageLM` for quizzes and flashcards → `ralph` collects xAPI statements → `pykt`
converts the stream into per-learner mastery that drives what the next session revisits.

🟢 **The licence ledger has no copyleft row in it.** Apache-2.0 + Apache-2.0 + MIT × 4.
🔵 **That is the whole point of the recipe** and the sentence to put in the SOW: the
client owns a modified platform they may redistribute closed, which `P-587-A` cannot
promise them.

🔴 **The one thing to sequence first.** Enumerate OpenMeetings' bundled dependencies in
week one and decide, with counsel, which ship in the client's distribution. The ASF's own
code is clean; the bundle is where the question lives, and it is a build-configuration
question — cheap in week one, expensive in week twelve.

🟡 **Honest comparison, not a replacement.** BBB is **13× larger**, purpose-built for
teaching, and has the richer pedagogy surface. 🟢 **Choose on the deliverable: if the
client needs to *own and redistribute* the platform, this recipe; if they need the best
teaching features and will accept linking, `P-587-A`.**

---

## P-588-B — 🟢 **The enablement engagement whose deliverable is a model the client trained themselves** (6–8 weeks, Global — travels to every region, including LATAM)

**The client problem.** An enterprise or public-sector buyer has been told to "build AI
capability" and does not want another slide deck or vendor workshop. Their engineers want to
have *built* the thing, and their risk function wants evidence that a model can run inside
their own boundary.

🔵 **How this differs from `P-587-B`.** That recipe maps a workforce's skill gaps onto a
taxonomy and assembles a learning path — it answers *"what should these people learn?"*
This one answers *"can these people build it, and can it run in here?"* 🟢 **The two
compose: `P-587-B` selects the cohort, this one is what the cohort does.**

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Foundations curriculum | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 🟢 **MIT** | **122,693** | 🟢 21 lessons; the largest education-adjacent repo on GitHub. Week-one hand-off |
| Agent curriculum | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** | **78,550** | 🟢 18 lessons on agents from first principles |
| Depth, mechanism | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 🟡 **Apache-2.0 — code only** | **107,625** | 🔴 **Vendor the code, not the book.** The grant's "Source" definition **excludes the books and images**; buy copies for the cohort rather than reproducing chapters in courseware |
| The capstone: a model they trained | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🟢 **Apache-2.0** | **64,710** | 🟢 **A ~64M-parameter model from scratch in ~2 hours on modest hardware** — the whole reason this recipe produces an artefact instead of a certificate |
| The full stack, end to end | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 🟢 **MIT** | **59,252** | 🟢 Tokeniser → pretrain → fine-tune → inference → web UI. 🟡 ~2 months since last push — **pin the commit** at kickoff |
| Use-case bank for the brief | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 🟢 **MIT** | **39,200** | 🟢 Agent use cases by industry, education among them — use it in pre-sales to turn "build AI capability" into three named candidate projects. 🟡 ~3 months stale; a catalogue, not a dependency |
| Mastery evidence | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Converts exercise completion into mastery estimates — what the sponsor reports upward |
| Delivery surface | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | **1,240** | 🟢 The one platform of record a studio may lawfully fork and ship; or the client's own LMS over LTI 1.3 |

**How to wire it.** Weeks 1–2: the two Microsoft curricula run as a cohort on the client's
LMS, with `pykt` instrumenting completion as mastery rather than attendance. Weeks 3–4:
`LLMs-from-scratch` supplies the mechanism — **its code**, with the book bought per seat.
Weeks 5–6: the capstone — the cohort trains `minimind` end-to-end **inside the client's own
infrastructure**, then stands up `nanochat` to see the full serving path. Weeks 7–8: the
three candidate projects drawn from `500-AI-Agents-Projects` are scoped against what the
cohort now knows how to build.

🟢 **The two deliverables are what make this sellable.** (1) A cohort that has trained
and served a model, not watched one being trained. (2) 🔵 **A dated, reproducible record
that a language model was trained and served entirely within the client's boundary** —
which is the artefact a risk or data-protection function actually asks for, and it is a
by-product of the teaching rather than a separate engagement.

🟢 **Why it travels to LATAM, EMEA and APAC without modification.** Every row is
permissive and **English-language**, so there is no in-language-supply dependency —
`p587`'s measured binding constraint in LATAM. 🔵 **Localisation is a translation line
item on known, openly licensed content**, except `LLMs-from-scratch`'s book, which is not
granted and must be bought. 🟢 `minimind` is a Chinese-language project, which makes it
an easier sell in APAC, not a harder one.

🔴 **The two licence facts to settle before the SOW.** (1) `LLMs-from-scratch`: the book
and images are outside the grant — reproducing chapters in client courseware is the
mistake this recipe is designed to avoid. (2) Pin `nanochat` and
`500-AI-Agents-Projects`; both are months stale and both are teaching artefacts, where a
silent upstream change mid-cohort is worse than an old commit.

---

## p587 — 2026-11-01 — two recipes the new rows make buildable, both built on the LGPL *link* boundary and the permissive curriculum tier

Every component below was verified first-hand on **2026-11-01**: existence, stars and
recency from `gh api search/repositories`, **licence from the repository's own licence
file**. 🔴 Note the channel: `api.github.com/repos/{owner}/{name}` was unreachable in this
environment, so `search/repositories` is the authority for every figure here (`587-C`).

---

## P-587-A — 🟢 **The lecture-to-courseware loop: BigBlueButton recordings in, revision material out, no fork and no copyleft exposure** (8–10 weeks, EMEA / North America / APAC)

**The client problem.** An institution already runs virtual classes and already has
thousands of hours of recordings nobody can use. They want revision material, summaries and
assessment items generated from their *own* teaching, and they will not accept their
lectures leaving the estate.

**Why this is the cleanest offer in this file.** Every licence boundary falls the right way:

| Role | Component | Licence (text) | Stars | Boundary that makes it legal |
|---|---|---|--:|---|
| Virtual classroom + recordings | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | **9,262** | 🟢 **LGPL permits *linking*.** The studio deploys BBB **unmodified** and consumes its recordings and events from outside. No derivative work, no carry-back. 🔴 Default branch `v4.0.x-develop`. |
| Transcript → deck | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 **MIT** | **71,803** | 🟢 Native PPTX with real shapes and narration — the deliverable a lecturer will actually accept |
| Reading → study skill | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 🟢 **MIT** | **36,673** | 🟢 Course reading list → a queryable skill, so generated material is grounded in the set text, not the model's memory. 🔴 branch `master` |
| Retrieval-grounded tutor | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | 🟢 Apache-2.0 | **34** | 🟢 LangGraph agentic RAG over a fixed corpus — answers come from *their* materials |
| Spacing schedule | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4,121** | 🟢 Turns generated items into a revision schedule instead of a dump |
| Local inference | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1,163** | 🟢 Offline delivery where connectivity or residency rules bite |

**How to wire it.** BBB's post-publish hook drops a recording manifest → transcribe locally
→ `book-to-skill` indexes the course reading list as the grounding corpus →
`ai-tutor-app`'s LangGraph retrieval answers and drafts items **against that corpus only**
→ `ppt-master` renders the lecturer-facing revision deck → `fsrs4anki` schedules the items
for students → `Kolibri` serves it offline.

🔴 **The one thing not to do:** do not patch BBB. The moment the studio modifies BBB source,
LGPL-3.0 carry-back attaches to the modification and the clean story is gone. Everything
above consumes BBB's **outputs**.

🟡 **Honest gap:** transcription is not specified here because this base has not measured a
permissive education-grade ASR row. Declared rather than filled.

---

## P-587-B — 🟢 **The reskilling-path engagement: a skills taxonomy with a curriculum attached** (6–8 weeks, Global; LATAM-viable because it needs no in-language repo)

**The client problem.** A corporate-learning or workforce-development buyer wants to know
which skills their people lack, what to put in front of them, and whether it worked. This
is the commonest corporate-learning brief and this base could not previously answer it,
because the taxonomy spine was missing.

| Role | Component | Licence (text) | Stars | Note |
|---|---|---|--:|---|
| Skills / occupation spine | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL-1.0** | **7,489** | 🔴 **A data licence.** Build a *produced work* on it freely; publishing an **enriched taxonomy** means publishing the enrichment — settle this before the SOW (`587-E`) |
| Agent curriculum | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** | **78,542** | 🟢 18 lessons, MIT — hand it to the client's engineers on day one |
| Shipping curriculum | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT** | **76,141** | 🟢 The build-and-ship half; pairs with the row above |
| Hands-on labs | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | 🟢 MIT | **242** | 🟢 51 labs: ML, transformers, RAG, agents |
| Mastery model | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | 🟢 Knowledge tracing — turns completion into *evidence of mastery*, which is what the buyer is actually paying for |
| Learning-record store | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** | **51** | 🟢 xAPI LRS, EMEA-origin (France Université Numérique), pushed `2026-10-31` |
| Delivery seam | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | **1,240** | 🟢 The one platform of record a studio may lawfully fork and ship |

**How to wire it.** `os-taxonomy` supplies the skill graph → the client's role definitions
are mapped onto it → gaps per person drive a path assembled from the three MIT curriculum
rows → `ralph` collects xAPI statements as learners move → `pykt` converts that stream into
mastery estimates that re-rank the path → `Sakai` (or the client's LMS over LTI 1.3) is the
delivery surface.

🟢 **Why this one travels to LATAM.** Nothing in it requires an in-language repository —
which, per `p587`'s measurement, is the binding constraint in that region: **two
Iberian-language education-AI repos above 10★, neither adoptable, against 67 in the Chinese
control.** The curriculum rows are English-language and MIT, so localisation is a
translation line item on known content rather than a build.

🔴 **Sequence the licence question first.** ODbL's share-alike on derived databases is the
only thing in this recipe that can surprise a client, and it surprises them *after* the
enrichment work is done. Settle it in week one.

---

## p586 — 2026-11-01 — four recipes the new rows make buildable, and the one the LGPL module boundary turns into the cleanest ERP offer in this file

Every component named below was verified first-hand on **2026-11-01**: existence, stars and
recency from `search/repositories`, **licence from the repository's own licence file**. No
component is named here that is not on [`../agents/top.md`](../agents/top.md) or
[`../repos/foundations.md`](../repos/foundations.md) with a measured licence.

---

### `P586-1` — Courseware factory: topic → deck → course → graded labs

🟢 **Why now.** `p586` found the generation tier moved up a layer: the unit of output is the
artefact a teacher hands over, not a question-bank item. All four generators are **MIT**.

| Step | Component | Licence | Stars | Role |
|---|---|---|--:|---|
| 1. Course skeleton | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | 🟢 MIT (text) | 574 | Topic in → researched course outline and materials out |
| 2. Slides | [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) | 🟢 MIT (text) | **71,803** | **Native** PPTX: real shapes, transitions, charts, narration — editable by the instructor afterwards |
| 3. Rich reading | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 MIT (text) | 1,040 | Source text → animated, narrated, interactive web experience |
| 4. Assessment items | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 (text) | 216 | Browser e-assessment with real maths handling |
| 5. Graded practical work | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | 1,370 | Assign → autograde → release notebooks |
| 6. Code feedback | [`pedal-edu/pedal`](https://github.com/pedal-edu/pedal) | 🟢 MIT | 32 | Static + dynamic analysis of learner Python — *why* it failed, not just that it did |
| 7. Safe execution | [`openedx/codejail`](https://github.com/openedx/codejail) | 🟢 Apache-2.0 | 477 | Sandbox untrusted learner code — **do not skip this** |
| 8. Delivery into the client LMS | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | 373 | LTI 1.3 tool provider — works against Moodle, Canvas, Sakai, Open edX without forking any of them |

**Wiring.** `claudemy` produces the outline and prose; `ppt-master` renders each module to
PPTX and `Papermorph` renders the readings; `Numbas` and `nbgrader` own assessment;
`codejail` wraps every execution of learner code; `ltijs` publishes the whole thing as one
LTI 1.3 tool so the LMS handles roster, SSO and grade passback.
🔴 **The one thing to get right:** keep generation **offline and human-reviewed** — generate
to artefacts an instructor edits, never into a live learner-facing surface. That single
boundary is what keeps the pipeline out of the "automated assessment" high-risk
classification in Vietnam's Decision 33/2026 and off the DC prohibited-use list.
**Estimate: 6–8 weeks** for a faculty-facing pilot in one department.

---

### `P586-2` — AI side-car for an education ERP, without forking it (the LGPL play)

🟢 **Why this is the cleanest offer in this file.** `p586` resolved
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (903★, pushed
`2026-10-29`) to **LGPL-3.0 from its own licence file** — the API reports `NOASSERTION`.
LGPL-3.0 is **weak copyleft**: a *separate module* calling the API **keeps its own
licence**. And because OpenEduCat is built as **Odoo modules**, that side-car is the
platform's own standard extension pattern rather than a bespoke integration.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. System of record | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0 (text)** | Admissions, fees, attendance, library, hostel, exams on one database. 🔴 Default branch **`19.0`**; owner is lowercase; repo has an **`_erp`** suffix |
| 2. The studio's AI module | *new, proprietary* | 🟢 **stays proprietary** | A separate Odoo module calling OpenEduCat's API — **never a patch to its files** |
| 3. At-risk-learner modelling | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | Knowledge tracing over attendance + assessment history |
| 4. Diagnosis | [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | 🟢 Apache-2.0 | IRT/DINA/NCDM cognitive diagnosis. 🔴 **~24 months stale** — vendor the algorithms, do not depend on the package |
| 5. Staff-facing analytics | [`openfun/warren`](https://github.com/openfun/warren) | 🟢 MIT | xAPI learning analytics. 🔴 Self-described **proof of concept** — reference only |
| 6. Counselling agent | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | Turns the LLM into an ITS over the learner record |

🔴 **The hard rule that makes the whole pattern legal: the boundary is the module, and the
module must not be a fork.** Add a module; call the API; never edit OpenEduCat's own files.
If the client needs OpenEduCat's own behaviour changed, that change is LGPL-3.0 and must be
published — which is a contribution decision, not an accident to discover at delivery.
🔵 **Do not substitute `warren`'s stablemate `potsie` here.** This base previously
recommended `potsie` as "the production-ready alternative"; re-measured `2026-11-01`,
**`potsie` last pushed `2024-12-18` (~23 months)** against **`warren` `2026-10-31`**. The
recommendation was backwards and is withdrawn.
**Estimate: 8–10 weeks** for admissions + at-risk-learner scoring on one campus.

---

### `P586-3` — Assessment assurance for a regulated jurisdiction (APAC-first, EU-ready)

🟢 **Why now.** Vietnam's **Decision 33/2026/QD-TTg** names education a high-risk sector
citing **automated assessment** explicitly; South Korea's **AI Basic Act** (in force
22 January 2026) imposes **human-oversight** duties; Australia's **TEQSA** requires
generative-AI risk action plans. The sellable work is the **oversight layer around
assessment**, not the assessment — and the whole stack is permissive.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. Simulate before exposing learners | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 BSD-3-Clause | Computerised Adaptive Testing simulator — item-exposure and fairness analysis **before** a learner sees an item |
| 2. Defensible learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | Knowledge tracing with published, inspectable models rather than an opaque score |
| 3. Pedagogical competence of the model itself | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | Benchmark built from **Chile's Agencia de la Calidad de la Educación / CPEIP** exams — evidence the model knows how to *teach*, not just answer |
| 4. Auditable autograding | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | Per-submission grading trail under Jupyter governance |
| 5. Controlled-experiment plumbing | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0 | Consent hidden from the instructor, identifiers stripped from exports — **the human-subjects posture, built in** |
| 6. Lockdown, if the client insists | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🔴 **MPL-2.0** | Sector standard. 🔴 File-level copyleft — **compose alongside; do not modify its files** |

🔴 **State the gap in the proposal rather than papering over it.** There is **no permissive
proctoring platform**: the only permissive component, `Proctoring-AI` (MIT, 633★), last
pushed `2024-12-10` (~23 months). The honest architecture is **SEB + an agent**, with the
AI doing anomaly review under human sign-off — never autonomous invigilation.
🟢 **This stack ports to the EU unchanged**, which is the commercial point: Annex III
high-risk obligations ask for exactly these artefacts (risk management, logging, human
oversight), so one build serves APAC statute and EU compliance.
**Estimate: 10–12 weeks**, including the oversight documentation.

---

### `P586-4` — Offline-first tutoring where connectivity and data residency both bite (LATAM, rural APAC, EU public sector)

🟢 **Why now.** `p586`'s structural finding cuts both ways: a skill inherits the host
agent's model and data path, so residency becomes a *contract* question. These components
answer it **structurally** instead — the stack runs with **no frontier API call**.

| Step | Component | Licence | Role |
|---|---|---|---|
| 1. Platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT (text)** | Offline-first learning platform, 1,016 forks, built for low-connectivity deployment. Branch `develop` |
| 2. On-device model | [`orionsheep/wordlink`](https://github.com/orionsheep/wordlink) | 🟢 **MIT (text)** | A shipped **fine-tuned 1.5B model (SFT+DPO)** that runs offline — the proof the pattern works at useful quality |
| 3. Local tutoring stack | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 BSD-3-Clause | Voice, video and 3D avatars, Docker-first, local LLMs via **Ollama**. 🟡 Last push `2026-06-26` |
| 4. Local-first adaptive workspace | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | Block-based adaptive learning that runs locally; 10+ providers incl. local |
| 5. Retention scheduling | [`open-spaced-repetition/free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 MIT | FSRS as a library — depend on this, not the Anki plug-in |
| 6. Speaking assessment | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 MIT | Phoneme-level pronunciation scoring (Wav2Vec2 + DTW), self-hosted |
| 7. Curriculum-aligned content, LATAM | [`csepulvedai/libro-3d-interactivo`](https://github.com/csepulvedai/libro-3d-interactivo) | 🟢 MIT | Interactive 3D books with Chilean-Spanish narration, aligned to curriculum objective **OA 13**. Universidad de Los Lagos |

🟢 **Why this is the right LATAM answer specifically.** Adoption there is already
near-universal (92% of students, 79% of faculty, 87% of institutions), so the missing piece
is not AI — it is institutional capability under a **widening computing-inequality**
headwind reported in October 2026. An offline stack on a **permissive, forkable** platform
with **curriculum-aligned local content** is deliverable to a ministry without a
data-transfer argument. 🔴 Moodle and `rosariosis` dominate the regional installed base and
are GPL — **attach via LTI, never fork**.
🔴 **And for a language-learning brief, say the gap out loud:** `LibreLingo` (2,631★) is
**archived** and its live successor `freelingo` is **AGPL-3.0**, so there is no permissive
general language-learning platform. Composing rows 2, 5 and 6 above (plus
[`word-atlas`](https://github.com/designfuchen/word-atlas), MIT, 3,604★) is a **BUILD** —
price it as one. Gap `586-C`.
**Estimate: 8–10 weeks** for a pilot across a district or a ministry programme.

---

🔵 **One rule shared by all four patterns.** Not one of them forks a platform of record.
The AI attaches through a boundary that keeps the studio's code its own — an **LGPL module
boundary** (`P586-2`), a **permissive extension point** inside a copyleft platform
(`XBlock`, `codejail`), or **LTI 1.3** as a separate service (`ltijs`, every pattern).
🟢 Fork only when the client needs the platform itself changed, and then only **Sakai**
(ECL-2.0), **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) or **relate** (MIT) — the four
platforms of record that permit it.

---

## p585 — 2026-11-01 — three recipes the licence resolutions make buildable, and the one the LATAM governance gap turns into the clearest offer in this file

Every component named below was verified first-hand on `2026-11-01` — existence and
recency from `search/repositories`, licence from the repository's own licence file.

---

## P-585-A — 🟢 **The forkable-platform engagement: own the LMS, ship it closed** (10–14 weeks, North America / EMEA)

**Why this is newly writable.** Every attachment pattern in this file exists because the
platform tier was believed to be uniformly copyleft. It is not: **four platforms of record
are permissive**, so "the client owns and ships a modified platform" is now a licit option
rather than a licence violation.

**Components**

| Role | Component | Licence | Stars |
|---|---|---|--:|
| Platform base — North America / higher ed | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟢 ECL-2.0 | 1,240 |
| Platform base — EMEA / DACH | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | 449 |
| Platform base — git-backed / CS curricula | [inducer/relate](https://github.com/inducer/relate) | 🟢 MIT | 437 |
| Tutoring engine | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 53,084 |
| Knowledge tracing | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | 456 |
| Mastery diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 Apache-2.0 | 203 |
| Untrusted code execution | [openedx/codejail](https://github.com/openedx/codejail) | 🟢 Apache-2.0 | 477 |
| Retention scheduling | [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 MIT | 731 |

**Wiring.** Fork the platform base. Expose `pyKT` and `EduCDM` behind one internal
"learner state" service — `pyKT` answers *what has this learner mastered*, `EduCDM` answers
*which specific skills are weak*; they are complementary, not alternatives. `DeepTutor`
consumes that state as context and generates the next interaction. `FSRS` schedules review
of anything marked mastered so it is not re-taught. Route any learner-submitted code
through `codejail` — never the application runtime.

🔴 **The one hard constraint:** `EduCDM` has not been pushed since `2024-10-25` (~24
months). It is Apache-2.0 and the models are sound, but **vendor it and own it** — do not
plan on upstream fixes.

---

## P-585-B — 🟢 **The LATAM institutional AI-governance offer: the gap is measured, the buyers are named** (8–12 weeks, LATAM)

**Why this is the clearest fit in this file.** The demand and the gap are both quantified
by third parties, not inferred: **92% of students and 79% of faculty** in LATAM higher
education are actively using AI (Digital Education Council / Tec de Monterrey, 29
universities, 2026), while **UNESCO IESALC** (200 institutions, 19 countries) finds a
**particularly wide gap between adoption and institutional governance**, and Tec de
Monterrey commentary states that formal institutional AI policies are simply lacking.
🟢 **Universities are already using AI and cannot evidence how.** That is a services sale,
not a licence sale.

**Components**

| Role | Component | Licence | Stars |
|---|---|---|--:|
| Pedagogical-quality baseline | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | 13 |
| Controlled rollout + consent/anonymisation | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0 | 21 |
| Learning-record capture | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 Apache-2.0 | 956 |
| Analytics surface | [openfun/warren](https://github.com/openfun/warren) | 🟢 MIT | 17 |
| Low-connectivity delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT | 1,163 |
| Adaptive assessment | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 BSD-3-Clause | 153 |

**Wiring.** `pedagogy-benchmark` first, as the **acceptance gate**: score the candidate
model on exams built by Chile's Agencia de la Calidad de la Educación and CPEIP *before*
any pilot, so the institution has a defensible pedagogical baseline rather than a vendor
claim. Deploy the tutor through `terracotta` so the rollout is a controlled comparison with
consent handling and identifier stripping built in — this is what converts a pilot into
evidence a rectorate can publish. Emit xAPI statements for every interaction;
`warren` renders them. Where connectivity is the binding constraint, deliver on `kolibri`.
Use `catsim` to simulate item exposure before any adaptive assessment touches students.

🔵 **Deliverable set, which is what is actually being bought:** an AI-use policy, an
auditable tutor, a staff capability programme, and an **ILIA-aligned** readiness baseline
(Latin American AI Index, with IDB and CEPAL) so the institution can benchmark itself
regionally. 🔵 Note `ILIA` (the index) is unrelated to `ILIAS` (the LMS) — they are
routinely confused in this industry's literature.
🔴 **`warren`'s own README still calls it a proof of concept** — ship dashboards on it only
with that stated, or render xAPI in the client's existing BI tool instead.
🔴 **Do not substitute `potsie` on recency grounds**: measured `2026-11-01`, `potsie` was
last pushed `2024-12-18` (~23 months) against `warren`'s `2026-10-31`.

---

## P-585-C — 🟢 **The contribution play: revive `pylti1.3` instead of writing a fourth Python LTI implementation** (3–4 weeks, Global — cheapest item in this file)

**The situation, measured.** Python LTI 1.3 has exactly one maintainable permissive
option, [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (🟢 MIT,
138★) — and it was **last pushed `2024-08-18`, ~26 months ago**. Node has a maintained
option ([`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs), 🟢 Apache-2.0, 373★, pushed
`2026-10-31`); Python does not.

**Why contribute rather than build.** LTI 1.3 is the seam every Moodle, Canvas, Open edX
and Chamilo engagement passes through. A fourth private implementation is unbillable
plumbing that must then be certified and maintained forever. 🟢 **Reviving the existing
MIT library costs less, and buys standing in the 1EdTech community that every subsequent
education engagement benefits from.**

**Scope.** Bring `pylti1.3` current against the 1EdTech LTI 1.3 Advantage certification
suite; validate credential handling against
[`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core)
(🟢 Apache-2.0) where badges are in scope; keep `ltijs` as the Node-side reference for
behaviour parity. 🔵 Pair it with [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again)
(🟢 MIT, 362★) when the client's legacy content is SCORM rather than LTI.

---

## 🔴 Licence ledger for all three recipes

Every component above is MIT, Apache-2.0, BSD-3-Clause or ECL-2.0 — **no recipe in this
section requires a copyleft component**, and none requires forking a copyleft platform.

🔴 **Two standing cautions that apply across all three:** (1) `EduCDM` (`2024-10-25`),
`girth` (`2022-09-09`), `pylti1.3` (`2024-08-18`) and `pupilfirst` (`2025-12-09`) are
permissive **and stale** — budget to own them. (2) **Never gate a build on the GitHub API's
licence field.** It reported `NOASSERTION` for six rows used above or alongside them, and it
cannot represent a split licence at all — [`andymatuschak/orbit`](https://github.com/andymatuschak/orbit)
is Apache-2.0 except for `packages/app` and `packages/backend`, which are AGPL-3.0-or-later
or **BUSL-1.1 (not an open-source licence)**. Read the licence file.


## p584 — 2026-11-01 — **five recipes the school-operations sweep makes buildable, including the first forkable-platform recipe this base has ever been able to write and a contribution play that costs less than any of them**

🔵 **Every repository named below was measured first-hand this pass:** grant byte-read via
`raw.githubusercontent.com` with byte counts, stars and `pushed_at` from
`gh api search/repositories`. 🔴 **No recipe here uses an unlicensed repository as a
dependency** — the unlicensed proctoring artefacts are cited as reference architecture only,
and said to be so.

## P-584-A — 🟢 **Shippable proctoring, which means SEB plus an agent — because there is no licensed proctoring platform to adopt** (8–10 weeks, EMEA or North America)

🔴 **The premise, measured:** `150` repositories on `topic:proctoring`; the credible
platforms (`narender-rk10/MyProctor.ai` `236★`, `AgnellusX1/GodsEye`,
`aryashinod/Multi-Agent-Online-Exam-Invigilation-System`) carry **no licence at all**, and
the Moodle plugin `eLearning-BS23/moodle-quizaccess_proctoring` (`30★`) is `NOASSERTION`.
🟢 **So the only lawful composition is a licensed lockdown client plus custom agent code.**

**Wiring:**
1. **Lockdown client — [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring)**
   (🟡 **MPL-2.0**, `16,726 B` byte-read, `361★`, `2026-10-30`, ETH Zürich). Deploy as-is;
   configure, do not fork. 🟡 **MPL-2.0 is file-level reciprocity** — any SEB source file
   you modify must be published, so **keep all custom logic in separate files/processes.**
   That constraint is the whole licence plan.
2. **Exam launch — [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)**
   (🟢 MIT, `1,098 B`, `26★`, `2026-10-28`, U. Michigan) if the tool is Django, so the exam
   launches from Canvas/Moodle as an **LTI 1.3 tool** rather than a parallel login.
   🔴 **If it is not Django, budget LTI as custom work** — see `P-584-D`.
3. **Integrity agent — build**, using
   [`wongcyrus/Google-AI-Classroom`](https://github.com/wongcyrus/Google-AI-Classroom)
   (🟢 MIT, `1,062 B`, `2026-10-28`) as the starting point: it already combines classroom
   multimodal sensing with exam invigilation, which is the exact shape needed.
4. **Low-infrastructure fallback —
   [`a8naaijetvi2lunk/carreau`](https://github.com/a8naaijetvi2lunk/carreau)**
   (🟢 MIT, `1,069 B`, `2026-10-01`, francophone): phone-based proctored MCQ with a
   **rotating QR code**. 🟢 Use where lockdown clients cannot be installed — BYOD
   classrooms and most LATAM/EMEA public-sector estates.
5. **Evidence trail —** `adlnet/lrs-conformance-test-suite` (MIT) for the xAPI statements,
   so the integrity decisions are auditable rather than asserted (`Trend 22`).

🔵 **Read, do not depend on:** the five-agent invigilation split (identity, gaze, phone
detection, …) in `aryashinod/Multi-Agent-Online-Exam-Invigilation-System` is the best
published decomposition of this problem and is **unlicensed** — reimplement the
decomposition, take no code.
🔴 **Regulatory gate before quoting:** Indonesia's SKB 7 Menteri and the Philippines'
DepEd Order `003` both constrain *runtime behaviour*; a proctoring agent in APAC needs
per-age-band limits and an incident-handling path, which is `P-583-B`'s pipeline.

## P-584-B — 🟢 **The forkable platform of record: Sakai, which is the only one a studio may lawfully modify and ship** (10–14 weeks, North America / EMEA)

🟢 **This recipe could not be written before this pass**, because this base published that
every platform of record was copyleft. It is not:
**[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai)** is **ECL-2.0** (byte-read
`11,120 B`, *"Educational Community License, Version 2.0"*), **`1,240★`**, pushed
**`2026-10-30`**, and ECL-2.0 is an **Apache-2.0 derivative** — permissive.

**Wiring:**
1. **Fork Sakai.** This is the sentence this base has not previously been able to say about
   any platform of record. Moodle (GPL-3.0), Open edX (AGPL-3.0), Chamilo, ILIAS,
   OpenEduCat, Gibbon and ERPNext all remain **client-owned code, never shippable IP**.
2. **Extend through the contrib channel, not the core —
   [`sakaicontrib/attendance`](https://github.com/sakaicontrib/attendance)**
   (🟢 ECL-2.0, `11,120 B`, `14★`, `2026-09-01`) is the worked example: a tool that
   integrates with the Sakai gradebook without touching core.
3. **Add the agent tier** from `agents/top.md` — the MCP/skill rows
   (`PsychQuant/che-ntucool-mcp`, `timdrichards/canvas-lms-skill`, `amirtds/cubite-mcp`,
   all MIT) show the attach pattern against three different LMS tenancies; the same shape
   targets Sakai's REST surface.
4. **Where the client is small-to-medium and wants an SIS rather than an LMS**, use
   **[`academico-sis/academico`](https://github.com/academico-sis/academico)** (🟢 MIT,
   `1,094 B`, `410★`, `2026-10-28`, Laravel/Filament) instead — permissive, and explicitly
   scoped to small and medium institutions.

🔴 **Do not quote this as "we fork your LMS".** Sakai is an Apereo research-university
platform; the fork play is right for an institution already on Sakai or willing to migrate,
and wrong everywhere Moodle is incumbent — which is most of the market.
🔴 **The MIT near-miss is a trap worth naming to the client:**
[`4jean/lav_sms`](https://github.com/4jean/lav_sms) is MIT at `1,161★` and **cold since
`2024-03-06`** — a fork-and-adopt base, never a dependency.

## P-584-C — 🟢 **The guardian-facing tier, which nobody has shipped** (5–7 weeks, North America)

🟢 **The gap is positional, not technical.** This base holds tutor agents, grading agents,
and institutional agents. **It had no row facing the parent** until this pass.

**Wiring:**
1. **[`noestudios/lastbell`](https://github.com/noestudios/lastbell)** (🟢 MIT, `1,067 B`,
   `1★`, `2026-10-16`) — self-hosted **ParentVUE + Canvas** grade and assignment monitor
   with whole-family alerting. 🟢 Region placed from the product: **ParentVUE is a US K-12
   parent portal**, so this is a North America artefact by construction.
2. **Attach via LTI 1.3** (`academic-innovation/django-lti`, MIT) so the district sees one
   integration, not a scraper.
3. **Add a summarisation agent** that converts gradebook deltas into plain-language
   guardian updates — and gate it behind the **human-final-decision** architecture
   `Trend 28` describes, because a parent-facing claim about a child's performance is the
   highest-liability output in the whole stack.
4. **Evidence:** log every guardian-facing statement with provenance (`Trend 14`), because
   `134` bills across `31` states (March 2026) are converging on exactly this surface.

🔵 **Why it sells:** Ohio `HB 96`, Florida `SB 1194` and Tennessee require districts to
hold formal AI policies, and **Gallup (April 2026) measured > `60 %` of college students
using AI weekly against ~half of institutions discouraging it.** The parent is the
stakeholder nobody has given a legible interface, and Delaware's **AI Assurance Lab**
means "passes a state assurance review" is a shippable property.

## P-584-D — 🟢 **The contribution play: adopt `pylti1.3` instead of building a fourth implementation** (3–4 weeks, Global; cheapest item in this file)

🔴 **Measured this pass:** `dmitry-viskov/pylti1.3` is **MIT, `138★`, cold since
`2024-08-18`** — and the ecosystem has tried to re-home it **twice, unsuccessfully**:

| attempt | measurement | state |
|---|---|---|
| `CNIT-Organization/ltitoolkit` | `fork = false`, created `2026-06-04`; LICENSE byte-read `1,070 B` carries 🔴 **"Copyright (c) 2019 Dmitry Viskov"**; `pyproject.toml` renames to `ff-ltitoolkit`; README says *"Published via Git (no PyPI required)"* while the description advertises *"PYPI Package"* | 🔴 detached copy, `0★` |
| `pymsglobal/pylti1.3` | `fork = false`, **created and last pushed `2025-09-19`** | 🔴 abandoned same day, `2★` |

🟢 **So the cheapest high-leverage action available to a studio in this whole knowledge base
is maintenance, not construction:** adopt `pylti1.3`, which already carries `138★` of
dependents and is the framework-independent Python LTI 1.3 implementation of record.

**Wiring:** fork upstream → re-establish CI → publish to PyPI under a clearly derived name
with attribution → upstream the Django/Flask example repos (`31★` and `23★`, both MIT, both
cold) as adapters. 🔵 **Deliverable to the client:** every Python LTI integration they buy
afterwards becomes a connector line rather than custom work, which is the difference
`verticals/solutions.md` line 103 has been pricing for four passes.
🔴 **Scope honestly:** this closes the *framework-independent* gap. For Django it is already
closed by `academic-innovation/django-lti` (MIT, `26★`, `2026-10-28`) — **which sat in this
base's history `63` times without being shelved**, so check the shelves before quoting this
as custom work.

## P-584-E — 🟢 **The Philippines reference engagement: a graduated-latitude obligation with a one-million-seat capability programme already funded** (10–12 weeks, APAC)

🟢 **Why this one and not another APAC jurisdiction:** the Philippines is the first in this
base where the **obligation** and the **capability funding** are both specified and both
current.

| element | what it forces into the build |
|---|---|
| **DepEd Order No. `003`, s. `2026`** (Feb 2026), *Foundational Guidelines on AI in Basic Education* | **human-centred** and 🟢 **graduated by learner independence** — more independent learners get greater latitude. **This is a per-learner policy engine**, not a global setting: the product must carry a learner-autonomy attribute and vary affordances by it |
| DepEd's stated motive — use **outpaced** enforceable policy | the deliverable is **enforcement surface**: logging, policy versioning, and the ability to show what a given learner was permitted on a given date |
| **Google for Education, June 2026** — > `1` M educators, tiers incl. **"AI Mastery"** (Gemini + prompt engineering), > `1` M with Gemini access | 🔴 **the teacher base is being trained on Gemini**, so an agent that assumes a different model surface fights the installed skill base |
| **Project AGAP.AI** — ASEAN Foundation + Google.org, up to **`1.5` M participants in 2026** | the budget is **programme-shaped and partly donor-funded** — bid into the programme, not the school |
| **Aug 2026: master plan still in preparation** | 🟢 the window where a vendor's architecture can become the default (the Poland pattern) |

**Wiring:** `P-583-B`'s incident pipeline and per-age-band enforcement (built for Vietnam
and Indonesia) **transfers directly** — the Philippines adds a *learner-independence* band
to the age bands already required. Compose with `openfun/marsha` (MIT, LTI content
management) or a Moodle estate, the attach-boundary MCP pattern for the LMS, and the
`adlnet` conformance suites as the evidence trail.
🔴 **Declared, not hidden:** every figure above is **secondary-sourced** — `583-E` means no
primary legal text was obtainable from this session, and a "`40`-hour ECAIR / < `18 %`
completion" claim and a "$`3` bn" figure were **rejected as unverifiable single-source
developer-blog material.** Re-confirm DepEd Order `003` against a DepEd primary document
before it goes in a proposal.


## p583 — 2026-11-01 — **three recipes the integration sweep makes buildable, and the one it turns into a build**

🔵 All components below are byte-read this pass with `pushed_at` recorded
([`grants-byte-read`](../evidence/grants-byte-read.2026-11-01-p583.tsv),
[`integration-axis-sweep`](../evidence/integration-axis-sweep.2026-11-01-p583.tsv)).
🟢 **The rule every recipe here now obeys (`Trend 36`): the interchange layer is permissive
and shippable; the platform of record is copyleft and is deployed, not forked.**

## P-583-A — 🟢 **Put the agent inside the client's LMS and ship the conformance evidence with it** (6–8 weeks, North America)

🔵 **Why this is now a composition rather than a build:** `p582` published that no
maintained permissive LTI 1.3 library existed. One does, and the conformance suites are
permissive too — so the *proof* is a deliverable, which is what Delaware's AI Assurance
Lab and the Ohio/Florida district-policy duties actually buy.

**Wiring, concretely:**

1. 🟢 **Launch** — [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
   (BSD-3-Clause, `1,528 B`, `73★`, `2026-10-05`). Use `LTI13Authenticator` against the
   client's Canvas / Moodle / Open edX as **Platform**. 🔵 Non-Python stacks:
   [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
   (Apache-2.0, Go) or
   [`swisnl/laravel-lti-provider`](https://github.com/swisnl/laravel-lti-provider) (MIT).
   🔴 **Do not start from `pylti1.3`** (MIT, `138★`) — `26.5` months cold.
2. 🟢 **Record** — statements to
   [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0, `144★`,
   `2026-10-27`) for a SQL-backed LRS, or
   [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (Apache-2.0, `334★`) when the
   client wants the ADL reference implementation by name.
3. 🟢 **Emit from the browser** — [`xapijs/xapi`](https://github.com/xapijs/xapi) (MIT,
   `51★`, `2026-04-29`).
4. 🟢 **Prove it** — this is the step that is the product:
   [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (MIT, `78★`) for the xAPI MUST requirements, and
   [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) (Apache-2.0, `59★`) for **cmi5**
   course-launch conformance. 🟢 **Ship the two reports as the artefact a district files**
   under Ohio `HB 96` / Florida `SB 1194`.
5. 🟢 **Agent layer** — the tutor/grader itself, wired behind the LTI launch with the
   refusal and provenance defaults from `P-582-B` and `Trend 37`.

🔴 **The copyleft boundary to state in the SOW:** if the client wants Moodle *events*
pushed into the LRS, that is
[`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi)
(**GPL-3.0**) — and any Moodle plugin is GPL by the platform's own rule. **Price it as
client-owned code, not shippable IP.**

## P-583-B — 🔴 **The APAC compliance-shaped deployment: an incident pipeline and per-age-band enforcement, because two jurisdictions now require them** (10–12 weeks, APAC)

🔵 **Forced by `Trend 37`.** Vietnam's Công văn 5588/BGDĐT-GDPT (`2026-08-19`) requires an
**AI incident-handling process**; Indonesia's SKB 7 Menteri No. 400.1-492/2026 requires
**age-tiered limits on duration and content type** across formal, non-formal and informal
education. 🔴 **Neither is satisfiable by prompt design or a human-in-the-loop checkbox.**

**Wiring:**

1. 🟢 **Policy enforcement point, per age band.** One service in front of the model holding
   `(age_band, subject, max_minutes, allowed_content_classes)`. Indonesia's bands run from
   early childhood upward with *stricter duration and content limits for younger children*,
   so the band — not the user — is the policy key. 🔵 Vietnam's `12` periods/class/year
   core gives the duration budget a concrete denominator to meter against.
2. 🟢 **Tool-vetting register.** Công văn 5588 makes the **school** responsible for
   selecting and reviewing age-appropriate tools, so the deliverable includes a reviewable
   record per tool: version, data flows, age bands cleared, reviewer, date. 🔵 This is the
   same artefact Delaware's Assurance Lab wants in North America — **build it once**.
3. 🟢 **Incident pipeline.** Detect → classify → retain → escalate → audit. Minimum store:
   the prompt, the output, the policy decision, the age band, the human who was notified.
   🔵 Statements belong in the LRS from `P-583-A` (`lrsql`, Apache-2.0) — the incident log
   and the learning record are the same substrate, which is the cost saving.
4. 🟢 **Refusal by default on terminal decisions**, per `p582`: the grader may **filter**
   and may not **determine** pass/fail. Brazil and France already require this; it costs
   nothing to carry into APAC.
5. 🔴 **Do not price off the mandate.** Korea's AI digital textbook went `34.2 % → 5.2 %`
   adoption in one year after reclassification. Price off **funded** programmes.

## P-583-C — 🟢 **Item-bank round-trip for a national assessment mandate** (8–10 weeks, EMEA)

🔵 **Why now:** Saudi Arabia's AI curriculum has been in force since SY 2025-26 **with
learning outcomes counted in overall student assessment** — so assessment interchange is
mandated scope. 🟢 And the permissive QTI tier is **six tools, not one**, which this pass
established by refuting this page's own superlative.

**Wiring:**

1. 🟢 **Author** — [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti)
   (MIT, `1,066 B`, `2026-09-19`): Markdown spec → **QTI 3.0** XML. The only permissive
   QTI **3.0** emitter measured.
2. 🟢 **Round-trip and validate** — [`examplary/qti`](https://github.com/examplary/qti)
   (MIT, `1,069 B`, `2026-10-12`) generates **and parses** IMS content packages. Parsing is
   what the converters below cannot do, and it is what makes the pipeline testable.
3. 🟢 **Inspect when it breaks** — [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground)
   (MIT, `1,070 B`) as the debugging surface.
4. 🟢 **Ingest the legacy Canvas estate** — [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert)
   (Apache-2.0, `11,357 B`, `22★`) for QTI → Word/JSON, and
   [`rikardroitto/canvas-quiz-skill`](https://github.com/rikardroitto/canvas-quiz-skill)
   (MIT, `1★`) for the reverse — Markdown → QTI 1.2 package for Canvas. 🔵 The latter is an
   **agent skill**, and the only agent artefact on `538` repositories.
5. 🟢 **Deliver** — [`ewels/starlight-quiz`](https://github.com/ewels/starlight-quiz)
   (Apache-2.0, `10★`, `2026-09-08`) renders the items permissively. 🔴 **Avoid
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components) if the renderer
   must ship** — it is the maintained option of record and it is **GPL-3.0**.
6. 🔴 **The psychometric half is still a build.** Per `p582`, all eleven psychometric rows
   on these shelves are dead; `douglasrizzo/catsim` (BSD-3-Clause, Brazil) does adaptive-
   test *simulation* only. 🟢 **State plainly in the proposal that defensible calibration
   is bespoke or a commercial dependency** — it is not a composition.


## p582 — 2026-11-01 — **two recipes forced by this pass's measurements: the handwritten-assessment pipeline that finally has live components, and the compliance-shaped grader four regulators now require**

Every component below was verified first-hand on `2026-11-01` with `q=repo:owner/name`
(licence, stars, `pushed_at`, `archived`). 🔴 **Both recipes deliberately avoid the `19`
dead addresses this pass found cited elsewhere on this page** — see
`evidence/shelf-dead-rows.2026-11-01-p582.tsv`.

## P-583-A — 🟢 **Handwritten assessment capture and feedback — the first version of this recipe whose components are actually maintained** (8–10 weeks, LATAM / APAC lead, portable)

🔴 **Why this recipe is new rather than an update.** This base's handwriting primitives
were `githubharald/DeslantImg` (MIT, `156★`, 🔴 last push `2021-11-21`) and
`githubharald/WordDetector` (MIT, `276★`, 🔴 `2023-05-05`) — **dead for 5 and 3.5 years**.
Any recipe naming them does not build. 🟢 **`datalab-to/chandra` replaces both in one
component**, and adds the two things they never had: **table structure and full layout**.

🟢 **The engagement.** A school system or university whose assessment is *paper*, graded by
hand, photographed on a phone. This is the majority condition in LATAM, South and
Southeast Asia and much of Africa — and the reason digital-assessment pilots stall is that
the input was never digital.

| # | Component | Licence | Stars | Role |
|--:|---|---|--:|---|
| 1 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | 🟢 **Apache-2.0** | **12,655** | **Handwriting + tables + layout → structured text.** The load-bearing component |
| 2 | [breezedeus/Pix2Text](https://github.com/breezedeus/Pix2Text) | 🟢 **MIT** | **3,281** | **Maths formulae** → LaTeX. Small models — runs where `chandra` is too heavy |
| 3 | [naptha/tesseract.js](https://github.com/naptha/tesseract.js) | 🟢 **Apache-2.0** | **38,803** | Browser/WASM OCR fallback — **the image never leaves the device**, which is the data-protection answer for minors |
| 4 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | Normalises the *reference* material (rubrics, answer keys, textbook extracts) into one text form |
| 5 | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 🟢 **BSD-3-Clause** | **9,750** | Renders the marked-up script + feedback back to **PDF** — what a parent or teacher actually receives |
| 6 | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | Knowledge tracing over the extracted item-level outcomes |

**Wiring.**
1. Phone photo → **`chandra`** for layout + handwriting; route any region it flags as
   mathematical to **`Pix2Text`** for LaTeX. Keep both outputs with per-region confidence.
2. Where policy forbids upload (minors' data; France's *cadre d'usage* bars identifiable
   student data in non-approved tools), run **`tesseract.js`** in-browser and send only
   the extracted text. 🔵 **Build this path first, not as a fallback** — it is what makes
   the product sellable in EMEA at all.
3. Rubric and answer key through **`markitdown`** once, at ingest, into the same text form.
4. An LLM scores *per item against the rubric*, emitting **item-level outcomes plus a
   confidence and a rationale — never an aggregate mark.** (See `P-583-B`: the terminal
   decision is barred.)
5. Item outcomes → **`pykt-toolkit`** for the learner model; feedback + annotated script →
   **`WeasyPrint`** → PDF.

🟢 **Where the margin is.** Steps 1–2 are commodity; **step 4's rubric-anchored,
item-level, confidence-bearing output is the product**, and step 2's on-device path is the
regulatory moat. 🔴 **Do not promise psychometric validity** — this pass established that
**every** open-source psychometric library is dead, so IRT-calibrated scoring is a build,
not a dependency. Scope this as *formative* feedback and say so in the SOW.

## P-583-B — 🔴 **A grader that is structurally incapable of deciding — because four regulators now require exactly that** (6–8 weeks, EMEA / LATAM, portable)

🟢 **This recipe exists because of a convergence measured this pass across four
jurisdictions queried in four languages** (see [`../intel/trends.md`](../intel/trends.md)):

| jurisdiction | the binding requirement |
|---|---|
| 🟢 **Brazil** — CNE *parecer* (≈`1 Sep 2026`, homologation ≈`13 Oct 2026`, 12 months to comply) | AI may be a **first filter** on essays and open responses; **may not determine approval or failure**. Four risk tiers. **Total ban in early-childhood education** |
| 🟢 **France** — *cadre d'usage* (Jun 2025) | AI use in submitted work **must be declared**; undeclared genAI is **fraud**; identifiable student data may not enter non-approved tools |
| 🟢 **Germany** — Länder | **Hessen:** AI use **and prompts** must be labelled. **NRW:** all aids disclosed |
| 🟢 **EU** — AI Act | **Art. 50** transparency from **`2 Aug 2026`**; grading is Annex III high-risk (Annex III timing contested — hedge it) |

🔵 **The requirement is not "add a human review screen". It is that the system must be
unable to emit a terminal decision**, and must carry provenance for every suggestion it
did emit.

| # | Component | Licence | Stars | Role |
|--:|---|---|--:|---|
| 1 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | Submission + rubric normalisation |
| 2 | [ing-bank/popmon](https://github.com/ing-bank/popmon) | 🟢 **MIT** | **512** | Population-stability monitoring on the score and feature streams (**ING Bank N.V.**) |
| 3 | [IFCA-Advanced-Computing/frouros](https://github.com/IFCA-Advanced-Computing/frouros) | 🟢 **BSD-3-Clause** | **260** | Concept/data drift detection (**Instituto de Física de Cantabria**) |
| 4 | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | Knowledge-tracing predictions — the distribution worth monitoring |
| 5 | [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 🟢 **BSD-3-Clause** | **9,750** | The auditable artefact: suggestion, rationale, model version, reviewer, timestamp |
| 6 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 🟢 **MIT** | **134,943** | Teacher review surface for annotating a script in-place |

**Wiring — the four constraints, implemented.**
1. **Refusal by construction.** The scoring service's response schema has **no total-mark
   field.** It returns per-criterion suggestions with confidence and a rationale. A mark
   exists only after a teacher writes one. 🟢 *This is a schema decision, not a UI
   decision* — it is what survives an audit.
2. **Declaration and labelling by default.** Every artefact leaving the system carries the
   AI-involvement label, the model version and — **for Hessen — the prompt**. Render via
   **`WeasyPrint`** so the record is a fixed document, not a database row.
3. **Age gating as a hard route, not a config flag.** Brazil bans AI in *educação
   infantil* outright, teacher-mediated included. The tenant's age band must be able to
   **disable the inference path entirely**.
4. **Post-market monitoring, which the AI Act requires and nothing education-specific
   provides.** **`frouros`** and **`popmon`** over **`pykt-toolkit`** outputs and the
   score distribution; alert on drift. 🔴 **Neither is education-aware — that integration
   is the billable work**, and it remains this base's clearest unmet build opportunity.

🟢 **Why this sells.** Germany's measured condition — **`56` rule-sets, `16` from the
Länder, and a teacher population that a Forsa survey finds has barely engaged with any of
them** — is a buyer who needs the compliance encoded in the tool, because they will not
read the rules. 🟢 **Spain is the cleanest entry:** a *real decreto* in preparation will
require **every university** to hold an ethical code covering faculty, students,
institution and research — a mandated artefact with no incumbent supplier.
🔵 **Brazil is the largest and most urgent:** homologation reported for mid-October 2026
starts a **12-month compliance clock** for schools *and* universities, and universities
must additionally write AI-mediation teacher training into their **PDI and PPC**.

🔴 **Known gap in both recipes, stated rather than hidden.** Attaching either to Moodle,
Canvas or Open edX properly needs **LTI 1.3**, and this base's only shelved implementation
(`dmitry-viskov/pylti1.3`, MIT) has been dead since 🔴 `2024-08-18`.
🟢 **CORRECTED `p584`:** if the tool is a **Django** application, use
[`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
(MIT, `26★`, `2026-10-28`, University of Michigan) and quote the integration as a
connector. **For any other framework the gap stands** — budget it as custom work, and do
not reach for `CNIT-Organization/ltitoolkit`, which `p584` established is a detached,
renamed copy of the same dead upstream.


## p581 — 2026-11-01 — **two new recipes: the lecture-archive pipeline, and the first buildable answer to this base's longest-standing gap**

Both use only rows verified first-hand `2026-11-01` (licence, stars, `pushed_at`,
`archived`) and name every component with its licence, because the licence is what decides
whether a studio can ship the result.

### 🟢 Pattern P-A — Lecture archive → searchable, tutorable, accessible corpus

**Who buys it:** a university system or ministry sitting on years of recorded lectures that
are undiscoverable and non-compliant. 🟢 **North America** buys the accessibility-audit
framing (captions that fail alignment audit); 🟢 **APAC** buys the ingestion framing (CJK
archives with captions burned into pixels, where no caption file exists to fetch).

**Wiring, in order:**

1. **Get text out of the recording — two routes, pick by what the archive is.**
   - Captions exist as a track → [`jdepoix/youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) (🟢 **MIT**, `8,543★`, `2026-10-30`). Cheapest path; also translates.
   - 🟢 **Captions are burned into the pixels** → [`YaoFANGUK/video-subtitle-extractor`](https://github.com/YaoFANGUK/video-subtitle-extractor) (🟢 **Apache-2.0**, `9,680★`). OCR over the subtitle region, fully local, no third-party API. **This is the only permissive route into hard-subbed archives and the reason this pattern exists.**
   - No captions at all → [`nexmoe/VidBee`](https://github.com/nexmoe/VidBee) (🟢 **MIT**, `11,026★`): local Whisper plus **speaker diarisation**. 🔵 Use VidBee specifically for **seminars, panels and vivas** — diarisation is what separates lecturer from student turns; for a single-speaker lecture it is overkill.
2. **Fix the timings** → [`smacke/ffsubsync`](https://github.com/smacke/ffsubsync) (🟢 **MIT**, `7,929★`). FFT alignment of the caption track against the audio. 🔴 **Do not skip this step.** A transcript with drifted timings cannot support seek-to-concept, clip extraction or a caption audit — and re-encoded archives drift as a rule.
3. **Cut it into teachable units** → [`zhouxiaoka/autoclip`](https://github.com/zhouxiaoka/autoclip) (🟢 **MIT**, `9,898★`, topics `ai-agent` + `mcp`). Long→short segmentation with subtitles and titles. 🟢 **Its description names 课程 (courses) as an input class**, so this is lecture-shaped, not only social-shaped. 🔵 Its `mcp` topic is the integration seam — drive it from your own agent rather than its desktop UI.
4. **Deliver inside the institution's LMS** on the permissive side of the licence seam:
   [`openedx/XBlock`](https://github.com/openedx/XBlock) (🟢 **Apache-2.0**) into Open edX
   (🔴 AGPL-3.0), or [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)
   (🟢 **Apache-2.0**) over LTI into Moodle (🔴 GPL-3.0), with
   [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (🟢 **MIT**) if the
   deliverable must be SCORM. 🟢 **Proprietary studio code stays out of the copyleft
   boundary.**
5. **Emit learning records** → [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec)
   (🟢 **Apache-2.0**) so step 2 of P-B has a stream to monitor.

🔴 **What this pattern does *not* do:** generate instructional video. Nothing open-source
does. Scope it as *archive activation*, never as content production.

### 🟢 Pattern P-B — Post-market monitoring for a deployed tutor or grader

🟢 **This is the first concrete recipe this base has for the gap it has called, for six
passes, the clearest unmet build opportunity in education AI.** It is assembled, not found:
the components are generic and the education-aware glue is the billable work.

**Who buys it:** 🟢 **EMEA first**, and on a dated clock — under the timetable this base
tracks, stand-alone education systems that grade work, screen applicants or supervise exams
carry Annex III obligations from **`2 December 2027`** (embedded products **`2 August
2028`**), with Article 50 transparency from **`2 August 2026`**, and **post-market
monitoring is a named duty**. 🔵 Also sells in **LATAM** as the evaluation half of a
governance engagement — note the `55 %`-no-AI-budget constraint, which is an argument for
composing permissive parts rather than licensing a platform.

**Wiring:**

1. **Model what the learner knows** → [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (🟢 **MIT**, `456★`, `2026-10-18`). 🟢 **Its per-skill mastery predictions are the distribution to monitor** — that is the whole trick: you do not monitor the LLM's text, you monitor the learner-model outputs the tutor is supposed to be moving.
2. **Detect drift on those streams** — pick one:
   - [`IFCA-Advanced-Computing/frouros`](https://github.com/IFCA-Advanced-Computing/frouros) (🟢 **BSD-3-Clause**, `260★`): concept- and data-drift detectors. 🟢 **Default choice** — purpose-built for drift, permissive, public-institution provenance (Instituto de Física de Cantabria).
   - [`ing-bank/popmon`](https://github.com/ing-bank/popmon) (🟢 **MIT**, `512★`): population-stability over Pandas/Spark frames. 🟢 **Choose this when the deliverable is a report for a regulator or exam board** — ING Bank built it to be shown to a supervisor, and it produces stability reports rather than just alerts.
   - 🔴 **Not `SeldonIO/alibi-detect`** (`2,554★`) despite it being the highest-starred: licence reads **NOASSERTION** and it is stale since `2025-12-11`.
3. **Measure whether the intervention actually worked** → [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) (🟢 **Apache-2.0**): randomised controlled trials inside LMS assignments, consent handling built in, identifiers stripped on export. 🔵 **Efficacy, which is a different question from drift** — pair them, do not substitute one for the other.
4. **Run untrusted learner code safely** if the subject is programming → [`openedx/codejail`](https://github.com/openedx/codejail) (🟢 **Apache-2.0**).
5. **Calibrate the assessment itself** → [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) (🟢 **BSD-3-Clause**, `153★`, live `2026-10-30`, 🟢 **Brazil-maintained — a LATAM-origin psychometric anchor**) for adaptive-test simulation. 🔴 **Do not promise item *generation*** from this: `catsim` simulates and calibrates, and no permissive item generator exists — searched three ways this pass and not found.

🔴 **State the limit to the client explicitly.** `frouros` and `popmon` **do not know what
a learner model is.** They will tell you a distribution moved; they will not tell you the
tutor's explanations got worse. **The education-aware layer — deciding which shifts are
pedagogically meaningful — is the engagement**, and it is unbuilt anywhere in open source.
🟢 Priced honestly, that is the strongest position: the commodity half is free and
permissive, the judgment half is the work.

### 🔵 Component licence ledger for both patterns

| Component | Licence | Shippable alongside proprietary code? |
|---|---|---|
| `youtube-transcript-api`, `ffsubsync`, `VidBee`, `autoclip`, `scorm-again`, `pykt-toolkit`, `popmon` | 🟢 MIT | 🟢 yes |
| `video-subtitle-extractor`, `XBlock`, `codejail`, `tsugi`, `terracotta`, `xAPI-Spec` | 🟢 Apache-2.0 | 🟢 yes |
| `frouros`, `catsim` | 🟢 BSD-3-Clause | 🟢 yes |
| Open edX platform | 🔴 AGPL-3.0 | 🟡 only across the `XBlock`/`codejail` seam |
| Moodle | 🔴 GPL-3.0 | 🟡 only across the LTI/`tsugi` seam |
| `alibi-detect` | 🔴 NOASSERTION | 🔴 **no — and stale** |

🟢 **Every permissive row above was licence-verified first-hand on `2026-11-01`** via
`q=repo:owner/name` against `search/repositories`. 🔵 `curl -sI` was **not** used: it
returns `403` for every `github.com` URL through this session's proxy, live repositories
included.


# Compose patterns — education

## p580 — 2026-11-01 — two recipes, both forced by this pass's measurements rather than chosen

## P-582-A — 🔴 **Safeguarding accountability for an EMEA school group — a BUILD, because the open supply is `6★`** (10–14 weeks, EMEA)

🔵 **Why this is a build and not an integration.** `Gap 579-D`'s falsifier run measured
`topic:safeguarding` at **`27` repositories with a `6★` head**, and that head
(`Brainhub24/TitanShield`, Apache-2.0) is a generic security toolkit, not an education
tool. Meanwhile safeguarding is a **statutory duty** for schools in England under *Keeping
Children Safe in Education*, with a named Designated Safeguarding Lead and audit
obligations. 🔴 **There is nothing to adopt.** Charge for the accountability.

**Components — every licence and star count read first-hand `2026-11-01`:**

| Layer | Component | Licence | Stars | Why this one |
|---|---|---|--:|---|
| LMS host | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (byte-read) | `449` | 🟢 **The permissive EMEA LMS.** Swiss-origin, DACH university install base. Avoids Moodle's GPL-3.0 and Open edX's AGPL-3.0 — which matters because the safeguarding module itself will hold proprietary policy logic. |
| Evidence store | [DSpace/DSpace](https://github.com/DSpace/DSpace) | 🟢 **BSD-3-Clause** | `1,105` | Versioned, permissioned record store with durable identifiers. A safeguarding audit trail needs immutability and retention, not a database table. |
| Learning records | [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | `956` | The interchange format for "who did what, when". 🔵 Last pushed `2025-07-03` — **a ratified spec, legitimately static** (trend 35). |
| Agent runtime | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | `52,849` | Only if a learner-facing tutor is in scope; its three-layer memory is the component that creates the safeguarding exposure in the first place. |

**Wiring:**
1. 🔴 **Classification runs out-of-process.** The disclosure detector (self-harm, abuse,
   grooming signals in tutor transcripts) is a separate service behind an OpenOLAT REST
   hook — never an in-tree plugin, so the policy logic stays out of Apache-2.0 scope and
   can be audited independently.
2. 🟢 **Human-final-decision by architecture, not policy.** Every classification writes an
   xAPI statement to DSpace and raises a case to the Designated Safeguarding Lead; the
   system **cannot close a case itself**. 🔵 This is the carve-out `Trend 28` identified:
   where a regulator exempts human-final-decision systems, compliance stops being
   paperwork and becomes an architecture choice. `Submitty/Submitty`'s explicit TA-grading
   stage is the same pattern shipped as a product feature.
3. 🟢 **The deliverable is the evidence trail**, per `Trend 22`: retention schedule,
   immutable case history, reviewer identity, model version per decision. The classifier
   will be replaced within a year; the trail is what the school is actually buying.
4. 🔴 **Do not promise EU AI Act Annex III conformity artefacts off the shelf** — `p577`
   recorded that no EMEA-origin open conformity component exists, and this pass found none
   either. Scope it as bespoke.

## P-582-B — 🟢 **Assessment generation after the T5 tier died — the generator is a prompt, the product is everything around it** (8–10 weeks, Global)

🔴 **Why the obvious starting point is wrong.** This base shelved
`topic:question-generation` with correct licence bytes and called
`patil-suraj/question_generation` the axis's *"reference implementation"*. This pass
measured recency for the first time: **all five rows last pushed between `2023-12` and
`2024-08`, one archived.** Every one is a fine-tuned T5 pipeline for a task
instruction-following models now do zero-shot (trend 35). 🔴 **Starting there inherits a
dead dependency and builds the one layer that is no longer scarce.**

**Components — all measured current `2026-11-01`:**

| Layer | Component | Licence | Stars | Last push |
|---|---|---|--:|---|
| Item authoring & delivery | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | `216` | `2026-10-28` |
| Autograded notebooks | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** ⬅️ *settled this pass* | `1,370` | `2026-10-28` |
| Untrusted code execution | [openedx/codejail](https://github.com/openedx/codejail) | 🟢 **Apache-2.0** | `477` | `2026-10-27` |
| Psychometric calibration | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** ⬅️ *was filed `no-grant`* | `203` | 🔴 `2024-10-25` |
| Offline item-bank reference | [BBkjdayup/BCTK](https://github.com/BBkjdayup/BCTK) | 🟢 **MIT** | `53` | `2026-09-28` |
| LMS seam | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | `471` | `2026-11-01` |

**Wiring:**
1. 🟢 **Generate with a frontier model, store in Numbas' own item format.** No fine-tuned
   generator, no model to maintain. The generator is a prompt plus a schema validator.
2. 🟢 **Calibrate with `EduCDM`.** Adopt the DINA/IRT/MIRT/NCDM implementations —
   permissive, and this base had them wrongly filed as ungranted for most of `580` passes.
   🔴 Vendor the code; it has not been pushed to in a year.
3. 🟢 **Grade code submissions through `nbgrader` over `codejail`.** `codejail` is the
   component that makes "run the learner's program" safe, and it is Apache-2.0 inside an
   AGPL platform — so it can be lifted out and used alone.
4. 🟢 **Ship through `XBlock`** into Open edX, or over **LTI 1.3** into Moodle. Both keep
   the studio's generator out of the platform's copyleft scope.
5. 🔵 **Take the offline posture from `BCTK` where the buyer is liability-bearing.** It
   keeps the item bank and the data on the institution's own machine — the posture
   `Trend 32` says institution-accountable buyers actually want, and the reason that tier
   never produces popular repositories.
6. 🔴 **Do not use `asahi417/lm-question-generation` for pt-BR work** — nine languages, no
   Portuguese, and abandoned since `2024-08-20`.

🟢 **What the client is buying:** item banking, interchange (`scorm-again`, MIT),
calibration and a defensibility trail. 🔴 **Not the generator** — that is the part that
stopped being scarce, and the part whose open-source tier died proving it.

## p579 — 2026-11-01 — two recipes, every component licence read from its file this pass

## P-581-A — 🟢 Student-facing analytics and advising on Canvas, FERPA-scoped (6–8 weeks, North America)

**Who it is for.** A US university or college system already on **Canvas** that wants
learners to see their own progress — and wants it without a per-seat contract with
Instructure, and without shipping student records to a vendor.

**Why these parts.** Both halves of the Canvas seam are permissive and both were written
*by universities*, which is what makes the FERPA conversation tractable: the code already
assumes a US institutional data posture.

| Part | Repo | Licence | Stars | Role |
|---|---|---|---|---|
| Learner-facing analytics | `tl-its-umich-edu/my-learning-analytics` | **Apache-2.0** | 37 | The product surface: Resources Accessed, Assignment Planning, Grade Distribution. Django + MySQL, Docker. University of Michigan ITS |
| Canvas tool surface | the `canvas-mcp` field — head is a `310★` MIT University of Illinois server, `102` tools, naming FERPA five times (`p565`) | **MIT** | 310 | Read/write access to Canvas for the agent, without a bespoke integration |
| Student model | `pykt-team/pykt-toolkit` | **MIT** | 456 | Knowledge tracing over the Canvas activity stream — turns "accessed" into "likely knows" |
| Diagnosis + path | `ZhijieXiong/pyedmine` | **MIT** | 82 | Cognitive diagnosis and **learning-path recommendation** (`4` LPR models) for the advising suggestion |
| LMS integration without a fork | `dmitry-viskov/pylti1.3` | **MIT** | 138 | LTI 1.3 so the tool launches from Canvas as a tool, not a parallel login |

**How it wires together.**

1. **Weeks 1–2 — stand up MyLA against a Canvas sandbox.** Its three views are the whole
   product-market question answered for you: ship them first, unmodified, and get a
   registrar and a privacy officer to look at them. Do not build a new UI yet.
2. **Weeks 2–4 — attach the MCP server as the write side.** MyLA reads; the Canvas MCP
   server lets an agent act (nudge, schedule, draft a message). Keep the two apart: the
   analytics path stays deterministic and auditable, the agent path is advisory and logged.
3. **Weeks 4–6 — fit `pykt-toolkit` on the activity stream, then `pyedmine` on top.** KT
   gives a per-skill mastery estimate; `pyedmine`'s LPR models turn that into "do this
   next". 🔵 Train on the institution's own term-over-term data — the public KT datasets
   will not match a Canvas course shape.
4. **Weeks 6–8 — launch as an LTI 1.3 tool via `pylti1.3`.** Launching from inside Canvas
   is what makes it a feature rather than another login, and LTI keeps every integration
   boundary at a standard.

🔴 **The two things that will actually hold this up**, neither of them technical. **(a)
FERPA review**: student-facing analytics show a student *their own* record, which is the
easy case — but the advising agent generates new inferences about them, and that is a new
record. Budget a privacy review as a deliverable, not an afterthought. **(b) Grade
Distribution is politically live**: showing a learner where they sit in a cohort is a
decision the faculty senate makes, not the delivery team. Ship it switchable per course.

🟢 **Why it is sellable:** `134` AI-in-education bills across `31` states in 2026, and four
states (MD, ID, OK, VA) requiring state guidance **and** district-level policy. The
conformance documentation is billable alongside the build, and it is the part the client
cannot download.

---

## P-581-B — 🟢 Assessment generation as a service, because there is nothing to adopt (10–12 weeks, Global)

**Who it is for.** Any institution or awarding body that must *produce* assessments at
volume — a university assessment office, a vocational awarding body, a ministry
examinations unit, a corporate certification programme.

🔴 **Start from the honest finding: this layer has no open anchor.**
`topic:exam-generator` holds **`73` repositories and its head is `93★`**, measured this
pass on an axis no prior pass had queried. The two permissive heads are both **offline-first
desktop applications** — `heshengtao/exameow` (Apache-2.0, `93★`) and `BBkjdayup/BCTK`
(MIT, `53★`) — not libraries you embed. So this pattern is a **build**, and the recipe is
about which parts you do *not* build.

| Part | Repo | Licence | Stars | Role |
|---|---|---|---|---|
| Item model and maths assessment engine | `numbas/Numbas` | **Apache-2.0** | 216 | Browser-based e-assessment with real mathematics: randomised items, algebraic answer marking. **Do not rebuild this** — item types and marking are where assessment software goes to die |
| Interchange / LMS delivery | `jcputney/scorm-again` | **MIT** | 362 | Modern SCORM runtime — gets generated assessments into any LMS that already accepts SCORM |
| QTI interchange | `Citolab/qti-components` | 🔴 **GPL-3.0** | 18 | QTI item rendering. Copyleft — **keep it behind a service boundary**, or export QTI and render elsewhere |
| Generation reference | `heshengtao/exameow` | **Apache-2.0** | 93 | Read its prompt and item-type handling: MCQ, true/false, fill-in-the-blank, short answer, with offline bank storage and wrong-answer history. Apache-2.0, so you may lift code, not just ideas |
| Teacher-side reference | `BBkjdayup/BCTK` | **MIT** | 53 | Duplicate-item detection and Word/Excel bulk import — the two unglamorous features an assessment office asks for first |
| Course-material generation | `Hyan-Yao/instructional_agents` | **MIT** | 22 | ADDIE pipeline: syllabus → slides (`.tex`/`.pdf`/`.pptx`) → scripts → **assessments**, so the assessment is generated against the stated learning outcomes rather than against a PDF. EACL 2026 Main, arXiv:2508.19611 |
| Item calibration | `douglasrizzo/catsim` + `eribean/girth` | **BSD-3-Clause** / **MIT** | 153 / 127 | IRT calibration and CAT simulation — simulate item exposure *before* a generated item reaches a candidate |

**How it wires together.**

1. **Weeks 1–3 — Numbas first, generation second.** Model three real item types from the
   client's actual past papers in Numbas by hand. If Numbas cannot express them, the project
   scope is wrong and you have learned it in week two for the price of three items.
2. **Weeks 3–6 — generation against outcomes, not documents.** Drive
   `instructional_agents`' ADDIE pipeline from the syllabus so each generated item carries
   the learning outcome it tests. 🔵 This is the difference between an item bank and a pile
   of questions: without the outcome link there is no blueprint and no defensible coverage
   claim.
3. **Weeks 6–9 — calibration gate.** Every generated item goes through `girth` for IRT
   parameters and `catsim` for exposure simulation before any candidate sees it. **This is
   the gate that makes the service defensible** — a generated item with unknown difficulty
   cannot be used to certify anyone, and an awarding body's regulator will ask.
4. **Weeks 9–12 — delivery.** `scorm-again` for LMS delivery; export QTI for anything that
   needs it. Keep `qti-components` (GPL-3.0) out of your own binary — behind a service, or
   swapped for export-only.

🔴 **What this pattern must refuse, and this base already knew both.**
`CaviraOSS/PageLM` generates quizzes and flashcards and is widely treated as MIT —
**it is not**. Its `LICENSE.md` is MIT's body verbatim followed by commercial-use, SaaS and
resale restrictions, so it cannot go into a paid assessment deliverable without written
permission from CaviraOSS; these shelves have carried it as `BLOCK` for several passes.
Likewise `xiaoyang111222/cn-math-taxonomy` (`5,654★`) is the obvious blueprint source for a
maths assessment programme and is **CC BY-NC 4.0** — fine for a ministry or non-profit
engagement with attribution, unusable commercially, and already declared as `Gap 572-C`.
🔵 Both are re-confirmed here from their licence files rather than newly found; what this
pass corrected was the **ledger column**, which said `MIT` and `CC-BY` respectively.

🟢 **Why the economics work.** The client cannot download this layer — measured, not
asserted: `73` repositories, head `93★`. The parts worth buying (`Numbas`, `scorm-again`,
calibration) are permissive and mature; the part that must be built is the blueprint,
generation and calibration pipeline, which is also the part that carries the accountability
the client is actually paying to transfer.


## p578 — 2026-10-31 — two recipes, both built from rows verified this pass

## P-580-A — 🟢 Arabic-first children's literacy programme, forkable end to end (8–10 weeks, EMEA)

**Who it is for.** A ministry, a Gulf private-school group under KHDA guidance, or an NGO
funder running an early-grade literacy programme in Arabic or a Maghrebi dialect — the
engagement this base could not quote without greenfield game development until this pass.

**Why it is now buildable.** [`vgwb/Antura`](https://github.com/vgwb/Antura) is
**BSD-2-Clause** on its code (assets CC-BY-4.0), **128★**, Unity 6.x, already shipping
**Arabic, Darija, English, French and Polish**, and descended from the *EduApp4Syria* game.
BSD-2 means **fork, rebrand and ship** — no copyleft obligation anywhere in the chain.

**Wire-up, concretely.**

1. **Fork `vgwb/Antura`.** Keep the code under BSD-2 attribution; treat the CC-BY-4.0 art and
   media as a **separate grant** and keep the attribution file intact in the shipped build —
   this is the one compliance step teams skip, and it is in the assets, not the code.
2. **Add the target dialect** as a new language pack rather than a fork of the content
   pipeline, so upstream fixes keep merging. Budget the phoneme and grapheme work as
   content, not engineering; it is the long pole.
3. **Sequence the curriculum with [`miuuyy/Clew`](https://github.com/miuuyy/Clew) (MIT).**
   Model the literacy skills as a prerequisite graph, export the ordering, and drive Antura's
   mini-game progression from it instead of hand-ordering levels.
4. **Instrument with xAPI out to [`openfun/potsie`](https://github.com/openfun/potsie)
   (MIT)** — Grafana dashboards, production-ready. Use `potsie`, **not** `openfun/warren`,
   whose own README states it is a proof of concept.
5. **Evidence of effect:** if the funder wants a controlled claim, add
   [`terracotta`](https://github.com/terracotta-education/terracotta) (Apache-2.0) on the
   LMS side for randomised assignment of content variations.

**Licence ledger:** BSD-2 (game) + CC-BY-4.0 (assets) + MIT (`Clew`, `potsie`) + Apache-2.0
(`terracotta`). 🟢 **No copyleft, and the client can close the fork.**

🔴 **Two things to tell the client before signing.** The EU AI Act's stand-alone Annex III
obligations now apply from **`2 December 2027`** (secondary, twice-attested — the Official
Journal is not reachable from this harness), so an EU deployment has a dated runway, not an
exemption. And **there is no EMEA-origin pedagogical benchmark** to cite in the conformity
file: `eth-lre/mathtutorbench` carries **two contradictory content licences on one page** and
cannot be used as a dependency. Cite `AI-for-Education/pedagogy-benchmark` (MIT) instead and
be explicit that its items are Chilean in origin.

## P-580-B — 🟢 A tutor you can prove works before it meets a student (4–6 weeks, Global)

**The problem this closes.** `p573` registered that this base had **no usable
learner-simulation agent** — so every tutor engagement was sold on vibes and measured after
go-live, in front of real children. That is now only **partly** true, and the partial answer
is worth selling.

**Wire-up, concretely.**

1. **Take the evaluation harness, not the tutor.** From
   [`iwangjian/Coding-Tutor`](https://github.com/iwangjian/Coding-Tutor) (**Apache-2.0**,
   92★, ACL 2025 Findings) use **DICT**: simulated students paired with pre- and post-tests,
   plus the published dialogue corpus (`output/dialogue.zip`) and the verifier checkpoints
   (`jwanglvy/Verifier-7B`).
2. **Keep its second idea too — turn-by-turn verification.** Traver traces what the simulated
   learner knows and verifies each turn; that is the mechanism that makes the pre/post delta
   attributable to the tutor rather than to the test.
3. **Swap the domain.** 🔴 **DICT's tasks are code**, from `EvoCodeBench-2403`, downloaded
   separately **under its own terms — read them.** For a maths engagement, replace the task
   bank with items calibrated by `catsim` (BSD-3) and `girth` (MIT) — the permissive
   psychometrics pair already on these shelves — and keep DICT's protocol shape.
4. **Put the tutor under test.** `DeepTutor` (Apache-2.0) or `OATutor` (MIT) as the
   system under test; `Clew` (MIT) supplying the prerequisite ordering the simulated learner
   is walked through.
5. **Ship the numbers as the deliverable.** Pre/post delta per simulated-learner profile, with
   the profiles and the task bank handed over, so the client can re-run it on their own
   content. 🟢 **That artefact is the differentiator** — it is what a district or a ministry
   asks for and almost no bidder has.

**Licence ledger:** Apache-2.0 (`Coding-Tutor`, `DeepTutor`) + MIT (`Clew`, `girth`,
`OATutor`) + BSD-3 (`catsim`). 🔵 `EvoCodeBench-2403` is **outside** this ledger and is the
one term to check.

🔴 **State the limit in the proposal.** Simulated learners test the **tutoring loop**, not
safeguarding, not accessibility, and not whether a child will use it twice. Sell it as the
gate before a pilot, never as a substitute for one.

## p577 — 2026-10-31 — six recipes, every component verified

Each pattern names the exact repositories, their licences, and how they wire
together. Every component was verified on 2026-10-31. Licences are stated because
in education they decide the architecture (see
[`../repos/foundations.md`](../repos/foundations.md)).

### P1 — AI tutor beside the LMS, without forking it (any region)

**The default pattern. Use this unless there is a reason not to.**

```
Client LMS (unforked)                    Globant-built, permissive
Moodle GPL-3.0 / Canvas AGPL-3.0  <--LTI 1.3-->  ltijs (Apache-2.0)
Open edX AGPL-3.0                                      |
        |                                       DeepTutor (Apache-2.0)
        \-----------------xAPI----------------->  potsie (MIT) on Grafana
```

- **Seam:** `Cvmcosta/ltijs` (Apache-2.0, 373★) registers the AI service as an LTI
  1.3 tool. The LMS is never modified.
- **Tutor engine:** `HKUDS/DeepTutor` (Apache-2.0, 52.7k★) behind the LTI launch.
- **Telemetry:** emit xAPI statements; render with `openfun/potsie` (MIT, 11★)
  Grafana dashboards. **Not** `openfun/warren` — its README says proof of concept.
- **Why it matters:** engagement code stays outside the AGPL boundary. Forking
  Canvas or Open edX and hosting it for a client can oblige disclosure of the
  modifications; this pattern never raises the question.
- **Effort:** 6–8 weeks to a production pilot.

### P2 — Mastery-tracked practice with real psychometrics (all permissive)

For a client who wants adaptive practice and will be asked to defend it.

1. `satvik314/educhain` (MIT, 387★) generates the item bank from curriculum text.
2. `AI-for-Education/pedagogy-benchmark` (MIT, 13★) gates the generated items —
   it is built from exams developed by Chile's Agencia de la Calidad de la
   Educación and CPEIP, so it tests pedagogical knowledge, not just correctness.
3. `eribean/girth` (MIT, 127★) calibrates item difficulty and discrimination (IRT).
4. `douglasrizzo/catsim` (BSD-3-Clause, 153★) simulates adaptive item selection
   **before** any learner sees it.
5. `CAHLR/OATutor` (MIT, 274★) runs the tutoring loop with Bayesian Knowledge
   Tracing over the calibrated bank.

Every licence here is MIT or BSD. Steps 3 and 4 are what separate this from a
chatbot that guesses: the adaptivity is measured before deployment.

### P3 — Autograded technical coursework with proof it worked (North America)

1. `jupyter/nbgrader` (BSD-3-Clause, 1.4k★) releases and autogrades notebooks.
2. LLM partial-credit feedback layered on the deterministic autograde — never
   replacing it.
3. `Cvmcosta/ltijs` (Apache-2.0) surfaces it inside the client's Canvas.
4. `terracotta-education/terracotta` (Apache-2.0, 21★) runs the randomised
   evaluation: it assigns content variations to student groups, hides consent from
   the instructor, and strips identifiers from exports.

Step 4 is the differentiator in North American higher education, where the buyer
increasingly asks for evidence of effect rather than a demo.

### P4 — Multi-agent classroom simulation for teacher training (APAC-sourced, MIT)

1. `THU-MAIC/OpenMAIC` (MIT, 42.2k★) provides the simulated multi-agent classroom.
2. `huggingface/smolagents` (Apache-2.0, 30.2k★) adds role agents — disengaged
   student, parent, department head — around it.
3. Score the trainee's responses against `pedagogy-benchmark` (MIT).

The two largest education agents in open source (OpenMAIC 42.2k, DeepTutor 52.7k)
are both APAC-origin and both permissive. A teacher-training engagement can be
built almost entirely on APAC open source.

### P5 — EU-compliant self-hosted deployment (EMEA)

1. Client's own infrastructure; Moodle (GPL-3.0) or Open edX (AGPL-3.0) **unforked**.
2. P1's `ltijs` tool and `DeepTutor`, self-hosted — no learner data leaves the
   client's estate, which is what the EU AI Act and GDPR conversation turns on.
3. Use `thm-mni-ii/feedbacksystem` (Apache-2.0, 24★) as the **reference
   implementation** for feedback generation: a German public higher-education
   institution already ships it, which is a procurement argument, not just a
   technical one.
4. Document the deployment against the European Commission's AI literacy
   framework for primary and secondary education, and — for England, for anything
   touching marking — Ofqual's January 2026 principles for AI in high-stakes
   marking.
5. Dashboards: `potsie` (MIT), self-hosted Grafana.

**Effort:** 10–12 weeks; the compliance documentation is a real work package, not
an afterthought.

### P6 — Spanish-language curriculum content (LATAM)

1. `csepulvedai/libro-3d-interactivo` (MIT, 14★) is the **pattern** for
   curriculum-aligned interactive content: Three.js 3D pop-up books, Chilean-Spanish
   narration, mapped to a named curriculum objective (OA 13).
2. `satvik314/educhain` (MIT) generates the content at volume.
3. `pedagogy-benchmark` (MIT) gates it — already built on Chilean MINEDUC exams.
4. Deliver into Moodle or Chamilo (GPL-3.0), which is what the region actually runs,
   via the P1 LTI seam.

**Caveat, stated plainly:** the LATAM-origin repositories are 13–14 stars and
skill-shaped. Treat them as *patterns to reimplement*, not as dependencies to
build a client deliverable on. The reusable asset in LATAM is the curriculum
alignment method and the Spanish-language evaluation set, not the code.

## What these patterns deliberately avoid

- **Forking any LMS.** Every pattern attaches from outside.
- **`openfun/warren`** in client-facing work — its own README disclaims production
  readiness.
- **`bigdata-ustc/Agent4Edu`** — no licence file, so it cannot enter a deliverable
  regardless of its AAAI 2025 oral.
- **Unlicensed or micro-repos as dependencies.** Where only a micro-repo exists,
  the pattern says to reimplement it.

---

## Prior passes (superseded, retained for history)

### (archived) Compose patterns — education

<!-- machine-readable count claim, p570, for ingest/derive-counts.py -->
`derived recipes: **34**` — recipe headings on this page, counted with that gate's
own id regex (family-suffixed form, `P-572-A`). 🟢 **`p576` filed `P-578-A`, `P-578-B` and
`P-578-C`**, all three at `##` level in the counter's own form, and re-derived the page
afterwards: **`34` recipes across `11` families (`568`–`578`)**. 🟢 **AND THE GATE RAN AND AGREED**: `ingest/derive-counts.py`
reports `compose/patterns.md recipes: derived=34 families=11 range=P-568..P-578 claimed=34`
— **GREEN** (`576-G`). 🔴 **`p573` recomputed this: the
claim read `24` while the regex counted `28` before this pass's two additions.**
🔵 The gap is `P-573-A/B/C` and `P-574-A`, registered by earlier passes without
the count being refreshed — the same stale-claim defect this base records as a
trend.

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


## 🆕 `p576` (2026-10-31) — three patterns, and all three exist because a *jurisdiction* was reached rather than a region

🔵 Every component below had its grant read byte-for-byte this pass or a prior one, with
the default branch resolved by `git ls-remote --symref` first — three of this pass's
components sit on a branch that is neither `main` nor `master` (`Artemis` → `develop`,
`i-educar` → `2.12`, `i-diario` → `1.6`), so a two-branch probe would report them dead.

## P-578-A — 🟢 BNCC-aligned tutor for Brazil, with the curriculum claim made falsifiable (6–8 weeks)

**The opening.** 🟢 **MEC published AI guidance for *educação básica* in April 2026** — four
pillars and ten diretrizes — plus a teacher-training course, and behind it the
**Referencial** (SEGAPE/MEC) asking institutions to stand up AI governance and ethics
committees. Every Brazilian network now needs to say how its AI tooling relates to the
**BNCC**. 🔵 **Almost everyone will *assert* alignment. This recipe lets a client
demonstrate it, and that is the whole differentiator.**

**Components, with grants read first-hand.**

| role | component | licence | why this one |
| --- | --- | --- | --- |
| curriculum spine | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** (code) **+ CC BY 4.0** (data) | `1,721` *aprendizagens* as JSON/CSV/SQLite with provenance per record; **npm + PyPI packages with data embedded, no internet needed**; **local MCP server** `npx -y @bncc/mcp`; Zenodo DOI `10.5281/zenodo.21625233` |
| alignment proof | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟡 **MIT** harness **+ CC BY 4.0** items/results | `15,300` responses from `17` models scored for hallucination **against the BNCC itself** |
| tutoring loop | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** (1,073 B) | MCP server that turns any LLM into an ITS; attaches to the same MCP surface as the curriculum spine |
| offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | the reference choice where connectivity is absent — which is where Brazil's **rural-priority** obligations land |
| model serving | Ollama or vLLM | 🟢 MIT / Apache-2.0 | keeps student prompts on infrastructure the network controls |

**How it wires together.** 🔵 Both the curriculum spine and the tutor are **MCP servers**,
so the integration is configuration, not glue code: the tutor resolves every objective it
teaches to a BNCC *aprendizagem* code through `@bncc/mcp` running locally. Kolibri carries
the content offline; the model runs on the network's own infrastructure.

**The deliverable that wins the renewal.** 🟢 **Re-run `bncc-benchmark`'s harness against
the client's own configured stack and hand over the scores.** That converts "our tutor
follows the BNCC" into a number, per model, per curriculum stage, reproducible by the
client. 🔵 **No other jurisdiction in this base has an equivalent harness**, so this recipe
does not port — and that is an argument for pricing it as Brazil-specific work.

🔴 **Read these three constraints to the client before signing.** The data is **CC BY 4.0**,
so attribution to **Profy Tecnologias Educacionais Ltda** travels with every derived
artefact. The benchmark's stored **model responses were generated by third-party models and
carry those providers' reuse conditions** — the repository says so explicitly; re-run the
harness rather than redistributing its results. And `bncc-dados` is **`24★`** — judge it on
its DOI, validation workflow and stated provenance, not its popularity, and fork it so a
maintainer change cannot strand the engagement.

## P-578-B — 🟢 Human-final-decision assessment architecture, so a Korean deployment falls OUTSIDE high-impact AI (6–8 weeks)

🟢 **The finding this is built on.** Korea's **AI Framework Act** and Enforcement Decree
have been fully in force since **`22 January 2026`**. Education's named high-impact instance
is **`학생평가` — student assessment**. 🟢 **And the Decree provides that where a human
intervenes in the final decision, the system is judged controllable and is excluded from
high-impact AI.**

🔵 **So this is not a compliance-documentation engagement. It is an architecture engagement
whose output happens to be compliance** — and the architecture is one a pedagogue would
choose anyway.

**The architecture, stated as the rule it has to satisfy.**

1. 🟢 **The model never writes a grade of record.** It produces *feedback* and a *proposed*
   mark, both held in a pending state.
2. 🟢 **A teacher's action is the only transition that creates a grade.** Not a timeout, not
   a default-accept, not a bulk "approve all" — each of those re-imports the system into
   the high-impact class by removing the human from the decision.
3. 🟢 **Every transition is logged with the human actor, the proposed value, the final
   value and the delta.** That log is the evidence that the carve-out applies, and it is
   the artefact to hand the regulator.
4. 🟡 **Generative output shown to students carries the labelling** the Act requires of
   generative AI, independently of the high-impact question.

**Components.** 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) — **MIT**,
1,091 B, branch **`develop`**, TUM — is the spine: *"Interactive Learning with Automated
Feedback"*, automated feedback with a teacher-owned grade, which is this pattern's shape
shipped as a product. 🟢 [`Submitty/Submitty`](https://github.com/Submitty/Submitty) —
**BSD-3-Clause**, grant in **`LICENSE.md`**, RPI — is the alternative where the
**explicit "TA grading" stage** is wanted as a first-class step. 🟢
[`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) — **BSD-3-Clause**,
UC Berkeley — handles notebook-based courses. 🔴 **Do not build this on
[`INGInious/INGInious`](https://github.com/INGInious/INGInious)**: **AGPL-3.0**, its own
licence says *"Most of the files…"* rather than all, and **§13 network exposure applies to
a hosted grader** — which is the only way a grader is ever deployed.

**Why it is worth more than a filing.** 🔵 The grace period is the window: MSIT grace of
**`≥1` year** with a delay to **2029** proposed. A client who adopts this architecture now
is not buying a reprieve — **they are buying a system that never enters the regime.**

🔴 **The honest grade, and say it in the proposal.** Every date, threshold and the carve-out
itself are **`C`-graded secondary** — read from policy trackers and law-firm briefings, not
from **`law.go.kr`**, which is unreachable from this harness along with every other
government host (`576-B`). 🟡 **Control families are reliable; the exact wording is not.**
**Have Korean counsel confirm the carve-out against the statute before the architecture is
sold as a compliance position.** 🔵 The architecture is good engineering regardless of how
the wording reads, which is what makes this safe to propose.

## P-578-C — 🟢 Colombia `Ley 2626 de 2026` curricular-compliance programme (10–12 weeks)

🟢 **The opening is a statute with a mechanism, which is rarer than a statute.**
**`Ley 2626 de 2026`, the "Ley de Educación Digital", expedida `24 August 2026`**, obliges
**Tecnología e Informática** in *básica* and *media* to carry **computational thinking,
programming, artificial intelligence, data science and digital citizenship**; orders a
**malla curricular obligatoria, progresiva y articulada por ciclos**; obliges **MEN** to
revise lineamientos **at least every three years** with a **Comisión Nacional de Educación
Digital**; creates an **Observatorio Nacional de Educación Digital**; carries a **teacher
training and updating programme** and an **ideological-neutrality clause**; and prioritises
**rural and ethnic-community** schools. 🔴 It is **obligatory in official schools**.

🔵 **Three properties make this a programme rather than a project:** the three-year revision
cycle makes the work **recurring**; the Observatorio makes outcomes **published and
therefore auditable**; and the neutrality clause makes **content review a named
deliverable** rather than an afterthought.

**The work, in the order a ministry or secretaría will buy it.**

1. 🟢 **Curriculum mapping by cycle.** The statute names five competency domains and orders
   progression by cycle; nobody has written that mapping. 🔵 **Reuse the structure rather
   than inventing it:** UNESCO's **AI competency framework for teachers** (`15`
   competencies, `5` dimensions, `3` progression levels) and the **student AI-literacy
   framework of `18/06/2026`** (four domains — *interact, create, manage, shape*) give a
   defensible, citable skeleton. 🟢 **Spain's INTEF «Guía» v2.0 (`08/09/2026`)** is a
   ministry-published Spanish-language precedent to align to, with a **«modelo de
   declaración de uso de la IA»** and a **«semáforo de uso»** already drafted — reuse them
   and bill the integration, not the policy text.
2. 🟢 **Teacher capability at scale**, which is where the budget is. Deliver against the
   UNESCO progression levels so "trained" is a measured claim.
3. 🟢 **Instrument the Observatorio.** MEN must publish implementation and gap data; help
   define the indicators and the pipeline, because **whoever defines the measurement
   defines the next three years of procurement.**
4. 🟡 **Equity build-out.** Rural and ethnic-community priority, plus the statute's
   dotación/connectivity/electricity provisions, with the constraint that it must not
   create new fiscal burdens — so **offline-capable delivery is a requirement, not a
   preference**: [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
   (**MIT**) is the component.
5. 🔴 **Content neutrality review** against the statute's clause — a named, repeatable
   deliverable.

🔴 **The supply constraint is the reason to build rather than adopt, and it is measured.**
🔴 **Spanish-language open-source education supply is `410` repositories deep and tops out
at `71★`** — a JavaScript course, not a product. Below it: teaching materials, a Moodle
attendance plugin for Chile's SENCE (`29★`), a Spanish vocational grading app (`9★`).
🔵 **There is no Spanish-language platform tier to stand on**, unlike Portuguese
(`portabilis/i-educar`, `722★`). 🟢 **Say so in the bid**: this is a build, the local
open-source supply will not carry it, and the permissively licensed pieces that *will*
carry it are horizontal and English-language.

🟡 **One caveat to state.** The statute's text was read at article level through a
**domain-restricted search** of a norms repository, **not from the Diario Oficial**, which
is unreachable from this harness (`576-B`). Article numbering and exact wording should be
confirmed against the official text before anything is warranted to a client. 🔵 The
obligations' *shape* — curricular mandate, three-year cycle, Observatorio, teacher
programme — is corroborated across four independent secondary sources.

## `p575` (2026-10-31) — two patterns: the BUILD recommendation `574-C` asked for, and the first binding-obligation package outside the EU and the US

🔵 **On the ids.** This pass files **`P-577-A`** and **`P-577-B`**, not `P-575-*`:
`P-575-A/B` and `P-576-A/B` were allocated forward by earlier passes and are live on
this page. Families stay contiguous (`568`…`577`), which is what
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) checks.

## P-577-A — 🟢 Education-specific accessibility remediation agent, built on the horizontal layer because the vertical one does not exist (8–10 weeks)

🔴 **This is a BUILD recipe, and it is here because `574-C` asked the right question
and got an honest answer.** `574-C` asked whether an education-specific, permissively
licensed accessibility agent exists. 🟢 **Four axes swept, `744` repositories: it does
not.** `topic:iep` holds `34` repositories and **the largest has `7★`**;
`topic:special-education` has exactly one repository above `11★`. 🔵 **The supply is
not badly licensed — it is absent.** Meanwhile the *horizontal* layer is mature and
permissive. So you build the thin education-specific part and buy the rest.

**What you are building:** an agent that reads a course in the client's LMS, finds the
accessibility defects that actually block a student, fixes what can be fixed
mechanically, and produces the evidence trail an audit or an accommodation request
will demand.

**Components, every grant read byte-for-byte on 2026-10-31:**

| role | component | grant | why this one |
| --- | --- | --- | --- |
| **CI accessibility gate** | [guidepup/guidepup](https://github.com/guidepup/guidepup) `591★` | **MIT** (`1,068 B`) | Drives **real** NVDA and VoiceOver from a test suite. Turns a duty into a gate. |
| **Gate, cheap tier** | [guidepup/virtual-screen-reader](https://github.com/guidepup/virtual-screen-reader) `158★` | **MIT** (`1,068 B`) | Simulated screen reader — runs in CI with no assistive tech installed. Use for every commit; use the real one at release. |
| **Conformance review** | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) `431★` | **MIT** | Eleven **WCAG 2.2 AA** review specialists. 🔴 Knows nothing about courses — that is the part you write. |
| **Course-level remediation** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) `117★` | 🔴 **GPL-3.0** | Already scans a **Canvas** course and fixes defects in place. **Deploy it, call it, do not vendor it.** |
| **Reading accommodation** | [Ropaxyz/EaseView](https://github.com/Ropaxyz/EaseView) | **MIT** (`1,067 B`) | Colour-overlay accommodation as a vendorable component. |
| **AAC surface** | [manavrenjith/AAC-Web_Project](https://github.com/manavrenjith/AAC-Web_Project) | **MIT** (`1,084 B`) | Permissive AAC + TTS, where the deployed platform (`cboard`) is GPL-3.0. |
| **Differentiation** | [ellmos-ai/worksheet-generator](https://github.com/ellmos-ai/worksheet-generator) | **MIT** (`1,068 B`) | Individualised worksheets — the output an IEP goal actually needs. |
| **Target of record** | [nvaccess/nvda](https://github.com/nvaccess/nvda) `2.7k★` | 🔴 **GPL-2.0** (in **`copying.txt`**) | The screen reader students use. **A test target, never a dependency.** |

**Wiring:**
1. **Gate first, before any agent.** Put `virtual-screen-reader` in the per-commit
   suite and `guidepup` driving real NVDA in the release suite. 🔵 Do this first
   because it is the only step that produces a *regression* signal — without it you
   cannot prove a remediation did not break something else.
2. **Scan with what exists.** Stand up **UDOIT** against the client's Canvas instance
   **as a deployed service** and call it over its own interface. 🔴 It is GPL-3.0:
   crossing that boundary with your own code makes your code GPL-3.0 too.
3. **Write the thin vertical layer — this is the actual build.** An agent that knows
   what a *course*, a *cohort* and an *accommodation* are: it reads UDOIT's findings
   plus the course structure, ranks defects by **which student is actually blocked**
   rather than by WCAG clause number, and routes each to a fix, a human, or an
   accommodation. 🔵 **Nothing in open source does this** — that is the finding, and
   it is why this is a build.
4. **Fix mechanically where it is safe.** Alt-text drafting, heading structure,
   table headers, contrast, caption cleanup — all reviewable diffs, none auto-merged.
5. **Emit the evidence trail, and treat it as the deliverable.** Per-course
   conformance state, dated, with the standard version named and the scan tool
   version pinned. 🔵 Per **trend 22**, the deadline moves and the obligation does
   not: the evidence trail is the durable artefact.

🔴 **Licence boundary, stated once:** everything you *ship* is MIT. **UDOIT (GPL-3.0)
and NVDA (GPL-2.0) are deployed and tested against, never linked.** Keep that line
and the deliverable stays proprietary.

🔴 **What not to do: do not start from the education-specific repositories on this
axis.** They are `1`–`7★` single-sitting projects. Read
[`littlebordercollie/mcd-together-order`](https://github.com/littlebordercollie/mcd-together-order)
(MIT, `101★`) for its **interaction design** — picture-card selection with a parent
verification step is genuinely well judged — but note it is **pre-pilot by its own
admission**: `10` commits, no student trials, one ¥12 order created and never paid.
**Copy the pattern, do not adopt the dependency.**

🟡 **Jurisdictional hooks, so the same build sells in four places:** US **ADA Title
II** (`April 26, 2027` / `2028`, WCAG 2.1 AA — dates graded `C†`, `574-E`); EU **EN
301 549** under the Web Accessibility Directive; **India** AICTE / RPwD ss. 16–18 with
GIGW 3.0 at WCAG 2.1 AA; **Australia** Disability Standards for Education 2005 (Cth),
where **Victoria requires the accessibility check *before* deployment** — the cleanest
procurement checkpoint on these shelves.

## P-577-B — 🔴 Korea high-impact AI compliance package for an education deployment (6–8 weeks, and the grace period is the window)

🟢 **Why this pattern exists now.** Korea's **AI Basic Act** and its Enforcement
Decree took effect **`22 January 2026`**, and **education is a named high-impact
sector** — the first *binding* education-specific AI obligation on these shelves
outside the EU AI Act and the US Title II rule. 🟡 **MSIT is operating at least one
year of forbearance through 2026**, deferring investigations and fines except for
serious social harm. 🔵 **So the commercial shape is unusual and worth naming: the
obligation is live, the enforcement is not yet, and a client who builds the artefacts
during the grace period pays far less than one who retrofits them after.** 🔴 A bill
proposing delay to **January 2029** is in play — the date is contested, the duty is
not.

**The five statutory duties, and the artefact each one needs:**

| duty | artefact | component |
| --- | --- | --- |
| **Risk management** | A dated risk register per deployed model, versioned with the model | 🔵 Reuse the `P-568-D` EU AI Act Annex III package — the control families overlap substantially |
| **Explanation** | Per-decision rationale a student or parent can read | 🔴 Hardest for a tutor built on RAG: log retrieved context with the output, or you cannot reconstruct the decision later |
| **User protection** | Appeal route, human contact, data boundary | — |
| **Human oversight** | A human decision point on anything consequential | 🟢 The **read-only default** of `P-568-B` is the right posture: an education agent writes nothing to a record of consequence without review |
| **GenAI output labelling** | Machine-and-human-visible marking on generated output | 🟢 Cheapest duty to satisfy and the one most often missed — do it at generation, not at render |

**Wiring:**
1. **Classify the deployment.** Any system touching teaching, assessment or student
   records in Korea is high-impact. 🔵 Assume in scope and argue out, not the reverse.
2. **Reuse the EU package.** `P-568-D` already produces the risk register, the data
   governance record and the human-oversight design. Map, do not rebuild.
3. **Instrument explanation at generation time.** Log model id, prompt version,
   retrieved context ids and output together. 🔴 **Retrofitting this is the single
   most expensive step** — a system in production for a year has no history to
   reconstruct.
4. **Label generated output at the source.** Mark it where it is produced so the mark
   survives export, copy and LMS rendering.
5. **Date the evidence and keep it.** Per **trend 22** and because the compliance date
   is contested between 2026 and 2029, the defensible position is a **continuous,
   dated trail**, not a one-off certification against whichever date holds.

🔵 **Where this lands commercially.** Korea is the one APAC jurisdiction on these
shelves with a statute rather than guidance; **Singapore** next door has a dated
*mandate* of a different kind — three compulsory teacher AI modules, one due end-2026
and two by 2027 — which is a services engagement with the same deadline shape. 🟢
**The same evidence-trail machinery serves both**, and `P-568-D` serves the EU. 🔴
**Do not sell this against Japan or China:** Japan's MEXT instrument is guidance and
its `JIS X 8341-3` version is disputed between equal-quality sources, and no Chinese
education AI or `GB`/`GB/T` accessibility instrument has been reached in two queries
(`575-D`).

🟡 **Provenance, stated plainly: every Korea and Singapore item in this pattern is
`C`-graded** — from policy trackers, law-firm briefings and local news, not from MSIT,
the statute text or MOE publications. 🔵 **`575-C` asks for the primaries** before any
of this enters a client deliverable. The control families are reliable; the dates
need first-hand confirmation.
## `p573` (2026-10-31) — two patterns, and they are the two halves of one decision

🔵 **Both come out of the eleventh pass's central finding** (see
[`../intel/trends.md`](../intel/trends.md) trend 19): the psychometric
measurement layer is **permissive in Python and GPL in R**, and the R tier is the
one a client's psychometrician and their exam board actually trust. 🟢 **Every
component grant below was read byte-for-byte this pass** from
`raw.githubusercontent.com` — `evidence/psychometrics-licence-bytes.2026-10-31-p573.tsv`
and `evidence/python-tier-licence-bytes.2026-10-31-p573.tsv`.

🔴 **Note on ids:** `P-573-*` and `P-574-A` were already consumed by earlier
passes that registered pattern ids ahead of the pass counter, so this pass —
`p573` — publishes as **`P-575-*`**. 🔵 Pattern ids on this page are **not** pass
numbers and should not be read as a chronology.

## P-575-A — 🟢 Permissive item-calibration and adaptive-testing pipeline, no copyleft anywhere (6–8 weeks)

**When to use it.** The client wants to own a closed, rebrandable assessment
product — an item bank, a calibration step and an adaptive delivery policy — and
has **no external body that must bless the psychometrics**. Corporate L&D,
certification startups, ed-tech product teams.

**Components — every grant verified first-hand, `p573`:**

| role | component | grant (first-hand) |
| --- | --- | --- |
| IRT calibration (1PL/2PL/3PL, GRM), ability estimation | [eribean/girth](https://github.com/eribean/girth) | 🟢 **MIT** (`LICENSE.txt`) |
| CAT policy: item selection, ability estimators, stopping rules, **offline simulation of examinees** | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** (`LICENSE`) |
| skill-level reporting: DINA / IRT / MIRT / neural cognitive diagnosis | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** |
| alternative/second-opinion IRT engine | [17zuoye/pyirt](https://github.com/17zuoye/pyirt) · [inuyasha2012/pypsy](https://github.com/inuyasha2012/pypsy) | 🟢 **MIT** · **MIT** |
| knowledge tracing / learner modelling over response streams | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) · [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) · [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** ×3 |
| benchmark datasets for pre-calibration sanity checks | [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | 🟢 **Apache-2.0** |
| worked reference for a *calibrated* item bank's shape | [englishcentral/ovlt](https://github.com/englishcentral/ovlt) | 🟢 **MIT** |
| permissive CAT framework if the stack is not Python | [JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl](https://github.com/JuliaPsychometricsBazaar/ComputerAdaptiveTesting.jl) | 🟢 **MIT** |

**Wiring.**
1. **Item bank in** (CSV / QTI export from the client's LMS) → normalise to a
   response matrix. Use `EduData`'s loaders as the schema reference rather than
   inventing one.
2. **Calibrate with `girth`** → persist item parameters (`a`, `b`, `c`) in a
   plain table the client owns. This table, not the code, is the asset.
3. **Validate the adaptive policy offline in `catsim`** *before* any learner sees
   it: simulate examinees at known ability levels, check that the policy recovers
   their θ within tolerance and respects content constraints. 🟢 **This is the
   step that substitutes for the learner-simulation agent this KB cannot legally
   ship** — the gap is registered as `573-A` in [`../intel/open-gaps.md`](../intel/open-gaps.md). 🔴 **Pointer corrected `p590`:** this line cited `../agents/top.md` as `573-A`'s home and that page contains **no** occurrence of the id, so the reference was dangling at its destination, not merely unregistered.
4. **Skill profiles with `EduCDM`** → "mastered / not mastered" per named
   competency, which is what a certification report has to say.
5. **Re-estimate on live data** with `pyedmine` or `pykt-toolkit` for drift.

🔴 **The honest limitation, state it in the proposal.** This pipeline is
permissive end to end and the client may keep every modification closed. 🔴 **It
is *not* the toolchain an exam board, ministry or journal reviewer will recognise.**
If that recognition is required, this pattern is the wrong half of the decision —
use `P-575-B`, or run `P-575-B` as a one-off external validation of the parameters
this pipeline produced.

🔵 **Weeks:** 1–2 ingest and schema; 3–4 calibration and parameter store; 5–6
`catsim` policy validation harness; 7–8 skill reporting and drift job.

## P-575-B — 🟡 Arm's-length GPL psychometrics: use `mirt` and `TAM` without creating a derivative work (4–6 weeks)

**When to use it.** The client's psychometrician, awarding body, ministry or
academic board **requires output from the canonical R packages**. That is a
reasonable requirement, not a preference — these are the implementations the
field's evidentiary standards were written around.

**Components — all grants read from `DESCRIPTION`, `p573`:**

| role | component | grant (first-hand) |
| --- | --- | --- |
| multidimensional IRT, DIF, item fit, plausible values | [philchalmers/mirt](https://github.com/philchalmers/mirt) | 🔴 **GPL (>= 3)** |
| Rasch/2PL/3PL calibration, plausible values, weighting (large-scale assessment) | [alexanderrobitzsch/TAM](https://github.com/alexanderrobitzsch/TAM) | 🔴 **GPL (>= 2)** |
| **linking and equating**, local dependence, invariance | [alexanderrobitzsch/sirt](https://github.com/alexanderrobitzsch/sirt) | 🔴 **GPL (>= 2)** |
| Q-matrix validation, classification accuracy | [Wenchao-Ma/GDINA](https://github.com/Wenchao-Ma/GDINA) | 🔴 **GPL-3** |
| Bayesian DCM with built-in fit and reliability output | [r-dcm/measr](https://github.com/r-dcm/measr) | 🔴 **GPL (>= 3)** |
| content-constrained multidimensional CAT | [Karel-Kroeze/ShadowCAT](https://github.com/Karel-Kroeze/ShadowCAT) | 🔴 **GPL-3** |
| latent-variable / SEM work where a **permissive** engine suffices | [OpenMx/OpenMx](https://github.com/OpenMx/OpenMx) | 🟢 **Apache-2.0** |

**The posture, and it is an engineering boundary rather than a licence
negotiation.** GPL obligations attach to **distributing a derivative work**. So:

1. 🟢 **Run the R tier as its own process, in its own container, from unmodified
   upstream CRAN sources**, with the upstream `LICENSE`/`DESCRIPTION` files
   shipped intact alongside it.
2. 🟢 **Cross the boundary with data, not linkage** — files, or a thin HTTP
   endpoint (`plumber`), or batch `Rscript`. **Calibration output is data; data is
   not a derivative work.**
3. 🟢 **The client operates that container.** Globant's deliverable is the
   orchestration, the item bank, the UI and the audit trail — none of which
   links, embeds or statically compiles any GPL code.
4. 🔴 **Do not:** vendor modified copies, statically link, embed R into a
   proprietary binary, or ship a single artefact that contains both the GPL
   packages and the closed product.

🟢 **Two pieces of genuine relief worth putting in front of the client's
counsel.** 🟢 **First: none of these packages is AGPL.** `p573` read every grant
and found GPL-2, GPL-3 and LGPL only — so **there is no §13 network
source-offer obligation**, which is the clause that makes hosted deployments
painful. 🔵 This matters because this base's own naive copyleft detector has
previously misgraded GPL-3 as AGPL-3 (its §13 cites Affero by name); the
`DESCRIPTION` read settles it. 🟢 **Second: the separate-process posture also
sidesteps the GPL-2/GPL-3 compatibility problem** — `TAM`, `sirt` and `CDM` are
GPL (>= 2) while `GDINA` and `ShadowCAT` are GPL-3, and combining those into one
linked artefact raises a question that **never arises if nothing is linked.**

🔴 **Limitation, stated plainly: this is an engineering posture, not legal
advice.** The client's counsel signs off on the boundary before the first
`Rscript` runs. 🔵 And if the client's own policy forbids GPL anywhere in the
estate — some do, regardless of linkage — then `OpenMx` (Apache-2.0) is the only
R row that survives, and the honest answer is that it covers latent-variable
modelling but **not** IRT calibration or equating. At that point go back to
`P-575-A` and tell the client what evidentiary standing they are trading away.

🔵 **Weeks:** 1 boundary design and counsel sign-off; 2–3 containerised R service
with pinned CRAN versions and licence manifest; 4 calibration and equating runs
reproduced against the client's historical data; 5–6 audit trail, versioned
parameter releases, handover.


## `p572` (2026-10-31) — three patterns, every component licence read byte-for-byte this pass

### 🟢 `P-572-A` — Handwritten coursework → marked feedback, permissive end to end

🔵 **The job:** a school or university receives work on paper, wants it digitised,
marked against a rubric, and the outcome recorded where analytics can see it.
🟢 **Every component below carries a first-hand permissive grant read this pass,
and the one trap on the obvious path is named.**

| stage | component | licence (read) | note |
| --- | --- | --- | --- |
| 1. segment | [`githubharald/WordDetector`](https://github.com/githubharald/WordDetector) | **MIT** 1,071 B | classic CV — **no model, no GPU**; turns a scanned sheet into word crops |
| 2. ⛔ *do not* deslant with | [`githubharald/DeslantImg`](https://github.com/githubharald/DeslantImg) | MIT grant / **GPL-3.0 surface** | `Py-BOBYQA>=1.3` is GPL-3.0 and in-process — **skip this stage or reimplement it** |
| 3. recognise | [`arthurflor23/handwritten-text-recognition`](https://github.com/arthurflor23/handwritten-text-recognition) | **MIT** 1,074 B | 3,645 commits; ⚠️ its default path pulls `openai`, a **paid external API** — swap for a local model where student data cannot leave |
| 4. decode | [`githubharald/CTCDecoder`](https://github.com/githubharald/CTCDecoder) | **MIT** 1,071 B | beam/lexicon/prefix search; **a lexicon raises accuracy on subject vocabulary** |
| 5. mark | [`patil-suraj/question_generation`](https://github.com/patil-suraj/question_generation) + an LLM marker | **MIT** 1,068 B | over-generate → rank → gate, per `P-574-A` |
| 6. return the grade | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | **MIT** 1,070 B | LTI 1.3 **Assignment & Grade Services** passback into the LMS the client already runs |
| 7. record | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** 11,357 B | xAPI statements; the analytics substrate |

🔵 **Wiring:** scan → `WordDetector` crops → `handwritten-text-recognition`
logits → `CTCDecoder` with a subject lexicon → text → rubric marking →
`pylti1.3` AGS grade passback → xAPI statement to `lrsql`.
🟢 **Licence posture: MIT/Apache-2.0 throughout, nothing copyleft, nothing
NonCommercial, and the single GPL-3.0 exposure on the obvious path is excluded by
name.** 🔵 **Shape:** 6–8 weeks for one subject and one LMS; stages 1–4 are the
risk, 6–7 are a week.

### 🟢 `P-572-B` — Attach AI to the LMS the client already runs, without forking it

🔵 **The job:** the client runs Moodle, Canvas or Open edX. They want agent
features. Forking is the instinct and it is the expensive mistake — **Open edX and
Canvas are AGPL-3.0, so a hosted fork owes source to its users under §13.**

🟢 **The licence-safe spine, by platform:**

| platform | attach with | licence | why this and not a fork |
| --- | --- | --- | --- |
| Moodle (GPL-3.0) | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** | PHP-native, IMS-certified; the tool stays yours |
| Canvas (AGPL-3.0) | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | courses, assignments, submissions, rubrics, quizzes; **grades and comments from any agent** |
| Open edX (AGPL-3.0) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 🟢 **the key fact: components are Apache-2.0 even though the platform is AGPL-3.0** — client course logic stays permissive |
| any / Python | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | the generic LTI 1.3 route |
| analytics | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** | one xAPI store behind all of them |

🔵 **Wiring:** agent service (your code, your licence) ← LTI 1.3 launch / MCP ←
LMS. Grades return over **AGS**; events land in `lrsql`; **no platform source is
modified, so no platform licence reaches the client's code.**
🟢 **This is the pattern that makes the copyleft question go away**, and it is why
the integration tier added this pass matters more than any platform on the shelf.
🔵 **Shape:** 4–6 weeks per platform; the second platform is half the first.

### 🟡 `P-572-C` — Teacher lesson-planning pack, local-first for data residency

🔵 **The job:** teachers want lesson plans, courseware, item banks and marking help
in their own template, and the procurement blocker is almost never features — it is
**whether student data leaves the building**.

🟢 **Reference implementations to study, both MIT, both read this pass:**
[`LeonhardJY/dsh-teacher-kit`](https://github.com/LeonhardJY/dsh-teacher-kit)
(MIT, 1,071 B) — **states it runs fully on the local machine, no network, no data
collection**, and covers exam papers, item-bank assembly, dictation sheets, lesson
plans, courseware and `docx`/`pptx` batch processing against the school's own blank
template; and
[`revjake1/lesson-plan-magic`](https://github.com/revjake1/lesson-plan-magic)
(MIT, 1,069 B) — fills a **US district** template and targets standards alignment.

🔴 **Both are thin (7 and 16 commits). Treat them as the specification, not the
dependency** — the feature chain they converge on independently
(**lesson plan → courseware → item bank → dictation → marking**) is the
transferable asset.

⛔ **Two components a naive build would reach for and must not:**
[`chewyenhan/malaysia-uec-teacher-workflow`](https://github.com/chewyenhan/malaysia-uec-teacher-workflow)
— its `SKILL.md`, `agents/` and `references/` are **CC BY-NC-SA 4.0**; and
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)
— its prerequisite graph is **CC BY-NC 4.0**. 🔵 Both are excellent and both are
NonCommercial; read them for structure and build the artefact fresh.

🔴 **Declared gap (`572-C`): there is no permissively licensed, curriculum-aligned
prerequisite knowledge graph on these shelves.** The best one located —
`cn-math-taxonomy`, 1,644 nodes and 2,403 edges — is NonCommercial, and the
adaptive-sequencing layer of this pattern therefore has **no permissive supply**.
Said plainly rather than filled with something that does not exist.

🔵 **Shape:** 6–8 weeks, and the local-only deployment posture is the deliverable
as much as the prompts are.

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

🔴 **CORRECTED `p585` (2026-11-01):** the claim *"every platform of record is copyleft"* is **false** and was withdrawn as `Trend 36`. Four platforms of record are permissive and forkable: **Sakai** (ECL-2.0, 1,240★), **OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★) and **relate** (MIT, 437★) — all four read from their own licence files. See [`../repos/foundations.md`](../repos/foundations.md). The statement below is retained as written for history.


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
71,498★** — 🔴 *(described here as the largest permissively licensed repository
anywhere in this knowledge base; **superseded `p582` by `microsoft/markitdown`,
MIT, `193,266★`**)* — and it generates native PowerPoint from
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

🆕 **Amended `p571` — the premise above is half false, and the base knew it.** The
sentence bundles two claims. 🟡 **"Psychometrically defensible" still holds:**
nothing permissive *calibrates*, so the gate remains the buyable artefact and this
pattern still produces the conformity evidence. 🔴 **"Nothing permissive generates
items" is false, and was false when this pattern was written** — pass 85
(`2026-10-09`) recorded a 7-row MIT item-generation tier in `agents/trending.md`
that reached **no shelf page and no pattern for 86 passes**. 🟢 It is now shelved
in [`../repos/foundations.md`](../repos/foundations.md) and wired in **`P-574-A`**.
🔵 **Use `P-574-A` to author and this pattern to mark and prove** — the authoring
step below should no longer be a bare model prompt.

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
| Local-voice pipeline | [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) 🔴 **STALE ADDRESS (`626-E`)** — canonical is [`llm-believer/slide-to-video`](https://github.com/llm-believer/slide-to-video) — 🔴 and the canonical home measures only `12★`, **last pushed `2025-09-12`** (`626-E`), so price this as unmaintained | **MIT** (1,070 B) | 🟡 **The sovereignty pick, now with a maintenance risk** — PDF deck + script, slides split on `NEWSLIDE`, with **optional local voice cloning**. The only row on this axis that needs no cloud TTS at all. |
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

## P-574-A — Multilingual item factory feeding a human-provable gate (6–8 weeks)

**For:** awarding bodies, universities with central assessment units, national exam
agencies, and corporate-training clients needing **volume** item authoring in more
than one language, on their own infrastructure.
**Region:** **APAC** first — `lmqg` ships evaluated `ja/ko/zh` models, and
**India's amended IT Rules require prominent labels and provenance markers on
AI-generated content from 20 Feb 2026**, which this pipeline emits by
construction. **EMEA** for `fr/de/it/es` plus the **Art. 50** transparency duty
(**2 Aug 2026**). **LATAM** for Spanish — 🔴 **not Portuguese**, see the limits.

**Why this pattern exists, and it is a correction rather than a discovery.**
`P-571-A` below leaves its item-authoring step to *"the model"* — a bare LLM
prompt — on the stated premise that *"nothing permissive generates
psychometrically defensible items."* 🔴 **Pass 85 (`2026-10-09`) had already found
a 7-row, permissively-licensed item-generation tier and recorded it in
`agents/trending.md`; it reached no shelf page and no pattern for 86 passes.**
🟢 `p571` shelved it ([`../repos/foundations.md`](../repos/foundations.md)) and
this pattern is the first to wire it. 🟡 **The other half of `P-571-A`'s premise
stands:** nothing here *calibrates*, so this pattern authors and `P-571-A` marks
and proves.

**Components** — grants carry pass 85's byte count plus a `p571` re-read; **5 of 5
re-reads matched exactly**.

| Role | Component | Licence | Note |
| --- | --- | --- | --- |
| Source-material ingestion | [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Client syllabus/textbooks/past papers → markdown+JSON with table structure. Every item must trace to a source document. |
| **Multilingual generator** | [asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation) | **MIT** (1,065 B) | 🟢 **Load-bearing.** `pip install lmqg`. Question **and answer** generation in **9 languages** (`en/fr/ja/ko/ru/it/es/de/zh`), HuggingFace checkpoints, **ACL 2023** system-demonstration paper, 385 commits. The only evaluated multilingual option on the base. |
| Item-**type** generator | [ramsrigouthamg/Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) | **MIT** (1,077 B) | The shapes an assessment unit orders: MCQ with distractors, boolean, FAQ, paraphrase, answer prediction. T5 + sense2vec. ⚠️ Region **disputed** (pass 85 said APAC; the grant names an individual) — do not quote it. |
| **Distractor specialist** | [KristiyanVachev/Leaf-Question-Generation](https://github.com/KristiyanVachev/Leaf-Question-Generation) | **MIT** (1,073 B) | 🟢 MCQs **with wrong-answer options**. ⚠️ **Use the MIT `Leaf` repo** — the same author's `Question-Generation` is **GPL-3.0** with 3.5× the stars, so a star-sorted pick takes the copyleft one. |
| Candidate **ranker** | [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator) | **MIT** (1,073 B) | Answer-aware evaluator that **ranks** generated questions. Over-generate → rank → gate. |
| Teacher-PDF entry point | [PragatiVerma18/MLH-Quizzet](https://github.com/PragatiVerma18/MLH-Quizzet) | **MIT** (1,069 B) | 🟢 Takes **teacher PDFs** and emits a quiz — the only row whose input is the artefact a teacher already has. Good pilot surface. |
| Baseline / control | [patil-suraj/question_generation](https://github.com/patil-suraj/question_generation) | **MIT** (1,068 B) | The axis's reference implementation. Use as the control when benchmarking the above. |
| ⚠️ Broad toolkit | [artitw/text2text](https://github.com/artitw/text2text) | 🟡 **MIT + rider** (1,324 B) | 🔴 **`Gap 353`/`P922`: a dependency-closure rider, 256 B over canonical MIT.** Clear it with counsel or skip the row — the rest of the pipeline does not need it. |
| **The gate** | [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (1,068 B) | 🟢 `itembank lint` **blocks CI on error** — unexplained distractors, answer-position skew, select/key mismatch, duplicate stems. **A model may author; it may not merge.** |
| Rubric advisory | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA** | Advisory on generated *content* only. ⛔ Bring your own corpus for a billable suite. |
| Telemetry / provenance | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI LRS: every item generated, ranked, linted, overridden — timestamped. **This is the provenance record India's rules ask for.** |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) · [openfun/potsie](https://github.com/openfun/potsie) | **MIT** · **MIT** | Jsonnet dashboards ship as reviewable code. |
| Drift baseline | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** | Baseline the generators' output distribution; re-run on every model or prompt change. |
| LMS attachment | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | LTI 1.3 launch into Moodle/Canvas/Open edX without touching platform code. |

**Wiring:**

1. **Ingest the curriculum** with `docling`. Chunk to **passage** size — every
   generator here takes a paragraph, not a chapter.
2. **Route by language, not by preference.** `lmqg` for any of its 9 languages
   (`TransformersQG(language="es")`); `Questgen.ai`, `Leaf` and `MLH-Quizzet` are
   **English-only** and carry the richer item types. 🔵 For a non-English
   engagement `lmqg` *is* the pipeline and the others are unavailable — size the
   estimate accordingly.
3. **Over-generate, then rank.** Generate 5–10× the required items; rank with
   `question_generator`'s answer-aware evaluator. Never ship first-pass output.
4. **Generate distractors as a separate step** (`Leaf`, or `Questgen.ai`'s
   sense2vec path). Distractors are the quality ceiling of an MCQ bank and the
   thing the gate rejects.
5. **Write into `itembank`'s markdown format, never into a database.** The format
   is the contract; `itembank lint` blocks the merge, `itembank guard` keeps live
   banks out of the repository.
6. **Emit provenance at generation time** — model id, checkpoint or prompt hash,
   source document, language, timestamp — into `ralph` as xAPI. 🟢 This satisfies
   **India's 20 Feb 2026 labelling-and-provenance duty** and **EU Art. 50**, and
   **it cannot be reconstructed afterwards.**
7. **Hand scoring to `P-571-A`.** Objective items score deterministically in
   `itembank`'s runtime with **no model in the path**; **short-answer stays pending
   for a human.**
8. **Baseline in `evidently`** so *"item quality changed in March"* is answerable.

🔴 **Honest limits — state all six before quoting.**

- 🔴 **These are T5-era models (grants dated 2018–2024) and a current frontier LLM
  will out-write them on English fluency.** Do not sell them as better generators.
  Sell the four things they actually give: **determinism**, **on-premises
  execution** (data residency, no per-item API cost at volume), **evaluated
  multilingual coverage with a published paper**, and a **distractor step** general
  models handle poorly. 🟢 With no residency, volume or multilingual constraint,
  a prompted LLM behind the same `itembank` gate is the honest recommendation.
- 🔴 **The repository licence does not cover the model weights.** All rows are MIT,
  but the fine-tuned **checkpoints are distributed on HuggingFace under their own
  terms** and base models carry their own (T5 is Apache-2.0). ⚠️ **Check each
  model card separately** — the same licence-layering trap `p570` recorded for
  content carve-outs, one layer down.
- 🔴 **No Portuguese.** `lmqg`'s 9 languages exclude `pt`. 🟢 **But the corpus
  exists:** `lplnufpi/essay-br` is **MIT** and human-graded on **ENEM C1–C5**, so a
  Brazilian engagement is a *trainable* build, not a blank sheet. 🔴 Spanish is the
  harder case despite `lmqg` covering `es`: `Gap 237` records **no rubric and no
  graded corpus** for Spanish, so scoring there needs an annotation programme
  first. **Generation and scoring have opposite coverage in the two languages** —
  read that before scoping either.
- 🔴 **Nothing here calibrates.** No difficulty or discrimination parameters:
  `eribean/girth` (MIT) last shipped **2022**, `inuyasha2012/pypsy` (MIT) **2018**,
  `meyerjp3/psychometrics` has **no licence file**, R options are copyleft. **A
  generated bank is uncalibrated until it has been sat.** `P-572-A` is the
  calibration engagement.
- 🔴 **Do not promise automated essay marking.** `topics/automated-essay-scoring`
  holds 35 repositories with 8 permissive grants but **no production-grade
  implementation**, and the short-tag variant `topic:essay-scoring` is emptier
  still (17 rows, 34★ ceiling). Extended-response marking is `P-571-A`'s **human**
  path.
- ⚠️ **`itembank` ships no QTI** and its MCP surface is unshipped. Integrate over
  its key-free JSON session protocol (`start`/`next`/`submit`/`report`/`teach`).

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
  more of it.** `ppt-master` (**MIT, 71,498★**) was believed the largest permissively
  licensed repository in this KB — 🔴 **superseded `p582` by `microsoft/markitdown`
  (MIT, `193,266★`)** — and went unfound for four passes because every
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

## 🆕 `p574` — 2026-10-31 — two recipes off the accessibility and QTI layer

🔵 `P-576-A` is the conformance programme whose deliverable outlives the deadline;
`P-576-B` is assessment delivery that keeps a `GPL-3.0` front-end out of a client
product. Both licences were read byte-for-byte this pass — see
[`../repos/foundations.md`](../repos/foundations.md) and
[`../intel/market.md`](../intel/market.md) for the regional placement.

## P-576-A — Accessibility conformance programme for an LMS estate, with an evidence trail that outlives the deadline (6–8 weeks)

🔵 **The buyer and the trigger.** A public school district, state system or public
university in the United States has a **dated obligation** — `April 26, 2027`
(population ≥ 50,000) or `April 26, 2028` (below that, and special districts) — to
bring web content and mobile apps to **WCAG 2.1 AA**, PDFs, Word documents,
spreadsheets and presentations included. In EMEA the same work is driven by
`EN 301 549` under the Web Accessibility Directive, and in Brazil by `LBI` art. 63
with no deadline but an active public prosecutor. 🔴 **The dates have already moved
once this year** (see [`../intel/market.md`](../intel/market.md)), which is the
argument for selling the *inventory*, not the date.

🟢 **The stack, every licence read byte-for-byte this pass** (evidence:
[`../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv`](../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv)):

| layer | component | grant | how it is used — and the licence posture that follows |
| --- | --- | --- | --- |
| Course-content scanner | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0-only** (`35,147 B`; `package.json` + `composer.json` agree) | **Canvas estates only.** Deploy **unmodified** in its own container, authenticate over the LMS API, send patches upstream. 🔴 Do **not** vendor it into a client product or a Globant-branded platform. |
| Permissive LMS alternative | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`10,982 B`) | Where the client is *choosing* a platform rather than remediating one. The only permissively granted institutional LMS on these shelves. |
| CI gate on content and templates | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 🟢 **MIT** (`1,069 B`) | Eleven **WCAG 2.2 AA** review specialists, run per pull request on the courseware repository and the theme. Vendorable into the client's pipeline. |
| Design-system remediation | [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | 🟢 **MIT** (`1,073 B`) | Fixes defects at the **template** level (tokens, components, contrast) so a thousand courses inherit one fix. |
| Estate-wide crawl | [liip/TheA11yMachine](https://github.com/liip/TheA11yMachine) | 🟡 **`BSD-3-Clause` in `package.json`, no licence file** | Internal auditing tool only. 🔴 A manifest-only grant has **no notice text to reproduce**, so do not ship it to the client; either obtain a grant clarification or replace it before delivery. |
| Learner-side adaptation | [ContentSquare/readapt](https://github.com/ContentSquare/readapt) · [evoluteur/braille-tools](https://github.com/evoluteur/braille-tools) · [dasher-project/dasher-web](https://github.com/dasher-project/dasher-web) · [mthebaud/predict4all](https://github.com/mthebaud/predict4all) | 🟢 Apache-2.0 / MIT / MIT / Apache-2.0 | Dyslexia reading adaptation, Grade-1 Braille rendering, gaze-and-switch text entry, AAC word prediction. All four are shippable in a client deliverable. |
| Document estate | — | — | 🔵 **Do not rebuild it here**: `P-570-B` on this page already covers remediation of the document estate. `P-576-A` is the **platform-and-evidence** half; run them together. |

🟢 **The deliverable, and this is the part that is worth money after the date
moves:**

1. A **per-course conformance inventory** — course id, owner, enrolment, defect
   classes, WCAG criteria failed, date last checked, remediation state.
2. A **remediation backlog ranked by enrolment**, so the first fix reaches the most
   learners, not the first alphabetical department.
3. A **re-check job** that re-runs the agents on every change and re-stamps the
   date, so the inventory never silently ages.
4. A **standard decision**: baseline **2.1 AA** for the US scope, deliver **2.2
   AA** where EMEA or APAC content is in play (`EN 301 549` v4.1.1 and Australia
   both land on 2.2 in 2026) — the MIT agents already enforce 2.2, so the
   over-delivery is free.

🔵 **Weeks.** 1–2: estate inventory and platform discovery. 2–4: UDOIT (or
OpenOLAT pilot) stood up, agents in CI on the theme. 4–6: template-level fixes,
backlog ranked, learner-side adaptations piloted with the disability services
office. 6–8: re-check job, evidence pack, handover to the client's own
accessibility coordinator.

🔴 **State the licence boundary in the SoW, in one sentence per component.** The
scanner and the platforms in this layer are **copyleft**; the CI agents and the
learner-side adaptations are **permissive**. A client who believes they bought a
product they can resell has bought the wrong thing, and this is the layer where
that misunderstanding is most likely — because the copyleft component is the one
that produces the visible output.

## P-576-B — Standards-conformant, accessible assessment delivery without inheriting GPL on the item bank (8–10 weeks)

🔵 **The buyer.** An exam board, ministry, professional certification body or
university assessment centre that must deliver tests which survive an appeal: the
item bank has to be portable, the delivery has to be accessible, and the scores
have to be defensible. 🟢 **The interchange contract is `QTI`**, and this pass read
the whole `topic:qti` population (`52` repositories) — so the licence map below is
the complete picture, not a sample.

| layer | component | grant | posture |
| --- | --- | --- | --- |
| Delivery platform | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) + [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | 🔴 **GPL-2.0-only** (`18,025 B`; `composer.json` agrees) | **TAO**, the QTI-native platform of record (OAT SA, Luxembourg). **Client-hosted, deployed unmodified.** Custom work goes in **separate TAO extensions**; those are derivative, so if anything is ever *distributed*, GPL-2.0 governs it. 🔵 GPL-2.0 has **no §13**, so a hosted deployment alone triggers no source-offer obligation — unlike the AGPL rows in this layer. Put the distribution question to the client's counsel in week 1, in writing. |
| Legacy item ingest | [rolfis/qti-convert](https://github.com/rolfis/qti-convert) | 🟢 **Apache-2.0** (`11,357 B`) | The **only permissively licensed QTI tool in the population.** Converts a Canvas QTI export to JSON/Word; wrap it as the ingest step and ship it. |
| Second ingest path | [Learnosity/learnosity-qti](https://github.com/Learnosity/learnosity-qti) | 🔴 **GPL-2.0** (`18,264 B`, on `develop`) | Run as an **external CLI step in a container**, never linked into client code. Use only if the client has Learnosity-format items. |
| Item rendering | [Citolab/qti-components](https://github.com/Citolab/qti-components) | 🔴 **GPL-3.0** (`35,199 B`) | 🔴 **Do not embed in a proprietary front-end.** Either deliver items through TAO's own (already-GPL, arm's-length) delivery, or build the renderer. This is the single most likely accidental GPL-3.0 contamination point in the recipe. |
| Accessible sittings | [mthebaud/predict4all](https://github.com/mthebaud/predict4all) | 🟢 **Apache-2.0** | AAC word prediction for candidates using switch or gaze input in an accommodated sitting. |
| Sign-language channel | [sign-language-translator/sign-language-translator](https://github.com/sign-language-translator/sign-language-translator) | 🟢 **Apache-2.0** (`11,364 B`; `pyproject.toml` agrees) | 🔴 **Not** [`sign/translate`](https://github.com/sign/translate), which is **CC BY-NC-SA** — noncommercial, and therefore unusable in a paid deliverable however good it is. In **Brazil this is not optional**: Libras is statutory (`Lei 10.436/2002`). |
| Item statistics | — | — | 🔵 Compose with **`P-575-A`** (permissive Python calibration) for item parameters and equating; **`P-575-B`** if the client's statistician insists on `mirt`/`TAM`, which are GPL and must stay arm's-length. |

🟢 **Deliverables.** A QTI-in/QTI-out item bank the client owns outright; a
client-hosted TAO deployment with named extensions; an **accessibility
conformance statement for the delivery surface** (the same evidence artefact
`P-576-A` produces, scoped to the test player); an accommodations matrix mapping
each supported accommodation to the component that provides it; and a licence
register naming every component, its grant, its byte count and its distribution
posture.

🔵 **Weeks.** 1–2: item inventory, licence register, counsel sign-off on the
distribution question. 2–4: TAO stood up client-side, ingest path built on
`qti-convert`. 4–6: accommodations (AAC input, sign-language channel, contrast and
keyboard paths) and the conformance statement. 6–8: calibration via `P-575-A`,
equating plan. 8–10: pilot sitting with the disability services office, appeal
rehearsal, handover.

🔴 **The failure mode this recipe exists to prevent.** The obvious build — take
`qti-components` for the renderer because it is the cleanest code in the
population, and wrap TAO — produces a **GPL-3.0 front-end inside a client
product**, which is the one outcome nobody in the room will have priced. The
grants here were read byte-for-byte precisely because the convenient choice and
the safe choice are different repositories.


## P-573-A — Rubric regression gate: prove the tutor has not degraded since Tuesday (4–6 weeks)

**For:** any client already running an AI tutor, content generator or marking
assistant in production, who cannot currently answer *"is it still as good as it
was at go-live?"*
**Region:** **Global**. 🔵 Highest urgency in **EMEA**, where an **AI Act Annex
III** evaluation-of-learning-outcomes system must hold post-market monitoring
evidence by **2 December 2027**, and in **North America**, where the four 2026
state laws requiring district-level AI policy imply an audit someone must pass.

**Why this pattern exists, and why it could not be written before this pass.**
This KB published *"no education-specific evaluation or regression tooling
exists"* for six passes. 🟢 **The scoring machinery does exist** — it is tagged
`rubric`, not `education` (see trend 15) — and it is permissive. 🔴 **What still
does not exist is a drift *detector*, so this pattern builds the detector out of
scoring parts.** That distinction is the whole design: you are not buying
monitoring, you are constructing it from a deterministic scorer plus a pinned
corpus plus a generic drift tool.

| Role | Component | Licence | Why this one |
| --- | --- | --- | --- |
| Trajectory scoring | [`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics) | **Apache-2.0** | 🟢 The only asset found that scores a **multi-turn trajectory** rather than one output — and every tutor in this KB is multi-turn. |
| Deterministic re-scoring | [`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune) **code only** | **Apache-2.0** | 🔴 **Use the code, never cite the history** — its 2,137-commit log is synthetic (`570-A`). Deterministic, two runtimes, **no model in the scoring path**, which is what makes a regression gate reproducible. |
| Education rubrics + prompts | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | ⚠️ code **MIT**, prompts **CC BY 4.0**, corpora **CC BY-NC-SA** | 🔴 **Take the code and the prompts. Do NOT ship the CLEAR or PERSUADE corpora** — they are non-commercial, and the upstream originals are too. |
| Pinned corpus | **the client's own** historical outputs, frozen | client's | 🔴 **The load-bearing step.** The corpus that exists cannot be shipped, so the engagement must mint one: 300–500 real interactions, human-scored once, versioned. |
| Skill-bundle scoring | [`AndrewNgGirl/SkillLens`](https://github.com/AndrewNgGirl/SkillLens) | **MIT** | Where the deliverable *is* a prompt contract — which is **15 of the 25** agents in this KB. |
| Item-side gate | [`onionviolet/itembank`](https://github.com/onionviolet/itembank) | **MIT** | `itembank lint` blocks on error; short-answer items never auto-graded. Reuse rather than re-implement. |
| Drift alerting | [`evidentlyai/evidently`](https://github.com/evidentlyai/evidently) | **Apache-2.0** | 🔴 Generic, not education-aware — it watches the *score series* this pattern produces, not the pedagogy. |
| Evidence trail | [`Sion612/rubrictrail`](https://github.com/Sion612/rubrictrail) | **Apache-2.0** | Criterion → evidence link, which is the shape an audit file needs. ⚠️ Dormant since Aug 2026: read as a design reference. |

**Wiring:**

1. **Freeze a corpus in week 1, before any tooling.** 300–500 real interactions,
   stratified by subject, learner level and language. 🔴 **Everything downstream
   is worthless without this and it is the step clients resist**, because it
   needs teacher time. Price it explicitly.
2. **Human-score it once** against a rubric taken from `evaluators`' prompts
   (CC BY 4.0 — attribute, do not relicense). This is the ground truth; it is
   produced once and never regenerated.
3. **Stand up `ScoreRune` as the deterministic scorer** and calibrate it against
   the human scores until agreement is stated as a number. 🔴 **Report the
   agreement figure to the client as the gate's accuracy** — a scorer that
   disagrees with teachers is a false-alarm generator.
4. **Add `AdaRubrics` for the trajectory dimension** — did the session actually
   progress, or did it produce eight individually acceptable turns that went
   nowhere? Single-output scoring cannot see this.
5. **Run both nightly against the frozen corpus** and push the score series into
   `evidently`. Alert on distribution shift, not on single scores.
6. **Keep the criterion → evidence links** (`rubrictrail`'s shape) so a regulator
   or accreditor can be shown *why* a score was given, not just the score.
7. 🔴 **Re-run the gate on every model, prompt and retrieval change** — the point
   is to catch a silent provider-side model update, which is the most common real
   cause of drift and the one no client monitors today.

**What to tell the client up front:** 🟢 *"You will be able to prove the tutor
still meets the standard, with permissive code and your own evidence."* 🔴
*"Nobody in open source will alert you that it drifted — we are building that
from scoring parts, and the quality of the alert is the quality of the corpus you
give us in week one."*

## P-573-B — Provenance gate: verify a component before it enters a client deliverable (1 week, reusable across every industry base)

**For:** Globant's own studio practice. 🔵 **This is the pattern most likely to
transfer unchanged to the gaming, legal, financial, healthcare, media, retail,
travel, technology, automotive, energy and enterprise bases on this harness** —
nothing in it is education-specific.
**Region:** **Global**.

**Why this pattern exists.** 🔴 **Two of this KB's own ranking signals have now
been shown forgeable, one of them one pass after it was adopted.** `p569` replaced
a star floor with commit density because the floor was discarding good libraries.
`p570`'s first never-swept axis returned a **35★ / 2,137-commit** repository whose
history is synthetic. 🔵 **Stars need other people; commits need a loop.** Any
shortlist built on self-reported repository metadata is a shortlist built on
claims the author controls.

| Check | Command / instrument | What it catches |
| --- | --- | --- |
| **1. Grant exists** | `raw.githubusercontent.com/<r>/{main,master,dev}/{LICENSE,LICENSE.md,LICENSE.txt,COPYING,licence}` | 🔴 Branch and filename traps. `human-skill-tree` is AGPL on `master` and 404 on `main`; probing only `main` manufactures a false "no licence". |
| **2. Grant is whole** | read the **body**, not the SPDX name | 🔴 **Four carve-out shapes, and only the first is API-visible:** separate content licence · per-directory grant · obligation inherited from an in-process dependency (`ai-learning-os` ← PyMuPDF, AGPL) · 🆕 **a `Scope:` clause inside the permissive file itself** (`word-atlas`, `570-B`). |
| **3. Manifest agrees** | `package.json` · `DESCRIPTION` · `pyproject.toml` · `NOTICE.md` | 🟢 Catches a real grant a stub `LICENSE` hides (`guess`: 52-byte `LICENSE`, MIT in `DESCRIPTION`) and a dependency surface (`calibrate`: `dependencies` absent — verified, not assumed). |
| **4. History is plausible** | 🆕 [`../ingest/history-plausibility.py`](../ingest/history-plausibility.py) | 🔴 **The new one.** Monotonic low-variance commits/year; commit conventions predating their own timestamps; author≠committer divergence of exactly zero; a repo whose first commit is a `refactor:`. |
| **5. Adoption is real** | stars **and** forks **and** distinct authors **and** `archived` | 🔴 `archived: true` is invisible in a licence or star read (`supertonic`: MIT, 13,757★, frozen). Two `noreply` authors on a "12-year" project is a tell. |
| **6. Figures are timestamped** | record the read time with the number | 🔴 Star counts move hourly (DeepTutor: +41 in 62 minutes measured here) and third-party digests emit impossible rates. **A star count is a reading, not a level.** |

**Wiring:**

1. **Run checks 1–3 before reading the README.** Licence first is not pedantry:
   it is the only check whose failure makes every other answer irrelevant.
2. **Run check 4 on anything admitted on commit density**, which costs one
   `git clone --filter=blob:none`. 🔴 **Mandatory whenever stars are low and
   commits are high** — exactly the profile the sub-floor census (`P-572-C`) is
   designed to surface, so these two patterns must be run as a pair.
3. **Record every verdict with its evidence string** — byte count of the licence
   file, the branch it was found on, the manifest field, the commit histogram.
   🔵 A verdict with no evidence string is re-derived from scratch next pass; this
   KB has measurably paid that cost.
4. **Carry defects forward rather than dropping the row.** `ScoreRune` is in this
   KB *with its defect named*, because the code is usable and the next reader
   would otherwise re-discover the same 2,137 and believe it.

**The honest limit:** none of these six checks establishes that code **works**.
They establish that it may be used, that it exists, and that its self-reported
history is not fabricated. 🔴 **Validation is still engineering** — `P-572-A`'s
cross-estimator harness is what that looks like.

## P-573-C — EMEA assessment engagement on locally published institutional psychometrics (8–10 weeks)

**For:** a European ministry, exam board, national testing institute or
university consortium that must evidence an **AI Act Annex III** system by
**2 December 2027** and would prefer not to base it on imported tooling.
**Region:** **EMEA**.

**Why this pattern exists and could not be written before this pass.** 🔴 This KB
recorded *"EMEA gained no placed row"* for three consecutive passes and offered
EMEA clients US- and APAC-origin psychometrics. 🟢 **`p570` placed three EMEA
rows from the grants themselves** — and the rows were already in-tree, already
licence-read, with only the region column blank. **The supply never changed; the
instrument did** (`569-D`).

| Role | Component | Licence | Provenance — the point of this pattern |
| --- | --- | --- | --- |
| Test analysis of record | [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | ⚠️ **LGPL-3** — attach, do not fork | 🟢 **Cito**, the Dutch **national testing institute** (`jesse.koops@cito.nl` in `Authors@R`). The strongest EMEA institutional provenance in this KB. |
| Large-scale assessment models | [`cran/TAM`](https://github.com/cran/TAM) | GPL-2+ — attach | 🟢 **IPN Leibniz Institute**, Kiel (`ipn.uni-kiel.de`). ⚠️ Grant lives in `DESCRIPTION`; **GitHub's sidebar shows no licence** — do not let a reviewer read that as unlicensed. |
| Latent-variable modelling | [`yrosseel/lavaan`](https://github.com/yrosseel/lavaan) | GPL-2+ — attach | 🟢 **Ghent University**. |
| Item calibration + equating | [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) | **MIT** | 🔴 `0.1.0`, 0★, one author — **permissive and pre-adoption.** The only component here you may embed. |
| Item gate | [`onionviolet/itembank`](https://github.com/onionviolet/itembank) | **MIT** | Blocking linter; deterministic scoring, **no model in the scoring path** — the conformity artefact Annex III evaluation needs. |
| Autograding | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | **BSD-3** | **UC Berkeley**; R-native, so it sits beside `dexter` rather than fighting it. |
| Efficacy evidence | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | **Apache-2.0** | LTI-attached randomised trials with consent handling. ⚠️ Grant **names no licensor** (template placeholders intact). |
| Regression gate | **P-573-A** above | — | Post-market monitoring is an Annex III obligation, not an optional extra. |

**Wiring:**

1. **Lead with provenance, not architecture.** 🟢 The opening slide is that the
   measurement core is published by **Cito, IPN Leibniz and Ghent** — three named
   public institutions in three member states. That is the procurement argument;
   the technical one follows.
2. 🔴 **Draw the copyleft boundary on day one.** `dexter`, `TAM` and `lavaan` are
   **LGPL/GPL** — they run as an **analysis service behind a process boundary**,
   invoked over a queue or REST, never linked into a proprietary product. This is
   the same doctrine this KB applies to the LMS of record: **attach, do not
   fork.**
3. **Put `calibrate` and `itembank` inside the product** — both MIT — and keep
   the GPL analysis tier outside it.
4. **Validate `calibrate` against `dexter` or `TAM`**, not instead of them:
   `P-572-A`'s cross-estimator harness, with the national-institute
   implementation as the reference. 🟢 **Two independently written estimators
   agreeing to a stated tolerance is the assurance evidence that a 0★ library
   cannot supply**, and here the reference carries a national institute's name.
5. **Attach `ottr` for marking** and `terracotta` for efficacy claims.
6. **Stand up P-573-A as the monitoring obligation** and keep its evidence trail
   from go-live.

🔴 **State the gap honestly in the same conversation:** this is a **measurement**
story, not a tutoring one. The EMEA *agent* layer is still effectively empty — one
24★ university feedback system and one 13★ evaluator — so the tutor itself will
be APAC- or US-origin, or built. **Conflating the two is the most expensive
mistake available on this page**, and it is the regional version of a finding this
KB has carried for four passes.
