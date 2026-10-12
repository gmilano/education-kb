---
industry: education
region: Global
updated: 2026-10-12
---

# Education — vertical platforms you can customise

**Pass 141, 2026-10-12.** 🔴 **Two of this page's platform rows change character.** Sakai's
`org.sakaiproject:kernel` aggregator is added to the inheritance ledger — it declares nothing
and inherits ECL-2.0 at depth 3, like its `impl` sibling. 🆕 **And a platform category this page
has never carried arrives through a connector: WordPress + Tutor LMS**, measured at 31 tools and
17 writes, with no licence.

### 🆕 🔴 The platform layer this page was missing: WordPress + Tutor LMS

[`hesham0-0nasser/tutor-lms-mcp`](https://github.com/hesham0-0nasser/tutor-lms-mcp) is not a
standalone MCP server. It is a **WordPress plugin** that exposes **Tutor LMS** — the WordPress
LMS plugin — to an agent over a hand-rolled JSON-RPC router mounted on `register_rest_route`,
with its own OAuth class. 🔵 **That makes WordPress an education platform tier on this page, and
it is the only one whose attachment point is a CMS plugin rather than an LTI launch or a REST
API.**

| measure | value |
|---|---|
| tools | **31**, from one static `TLMS_MCP_Tools::list_tools()` array — **0 conditionals**, so the surface is fixed by the build |
| 🔴 writes | 🔴 **17 of 33 distinct names** — `tutor_create_course`, `tutor_update_course`, 🔴 **`tutor_delete_course`**, plus topic and lesson writes |
| 🔴 licence | 🔴 **no file at `HEAD`** — 7 commits, HEAD **2026-05-26** |
| region | 🟢 **EMEA** — `+0300` on 7 of 7 commits |
| files | 6 PHP: `class-mcp-router.php`, `class-mcp-tools.php`, `class-mcp-auth.php`, `class-mcp-oauth.php`, `class-mcp-admin.php` |

🔴 **The missing licence is a harder stop here than elsewhere on this page.** WordPress's own
distribution terms assume GPL-compatibility for plugins, so the *"permissive by omission"*
reading that a reader might attempt on a bare npm package is not available — and p140's `T26`
cuts the other way too: there is no parent manifest to inherit from in a WordPress plugin.
🔴 **Unusable as shipped**, and worth watching precisely because the shape is right: a
course-authoring write surface on a platform with an enormous installed base.

🔵 **The architectural point for a studio is the attachment pattern, which is reusable
regardless of this row's licence**: WordPress already solves authentication, roles and REST
routing, so an MCP surface over a WP LMS is a router class plus a tool table. The licence is a
one-file fix the maintainer has not made.

### 🔴 Sakai: the aggregator declares nothing either, and now the whole family is measured

p140 corrected this page's claim that `sakai-kernel-api` and `sakai-kernel-impl` have *"opposite
licence posture"* — both are **ECL-2.0**, one by inheritance at depth 4. 🆕 **`ACTION DC` adds
the third member.**

| coordinate | own POM | inherits from | licence | depth |
|---|---|---|---|---|
| 🟢 `org.sakaiproject.kernel:sakai-kernel-api:25.2` | ECL-2.0 | — | ECL-2.0 | 2 |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl:23.3` | **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | 4 |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:master:23.3` → `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |

🟢 **So Sakai's grant is consistent — ECL-2.0 throughout — and 2 of 3 artefacts state it
nowhere in their own files.** 🔵 **The whole family's licence rests on a single POM,
`org.sakaiproject:oss-parent:1`**, and `org.sakaiproject:master:23.3` between them declares
nothing, so a walk that stops at the first silent ancestor finds no grant at all. 🟡 A European
university's review burden on Sakai is therefore procedural rather than legal: the licence is
fine, the paperwork proving it is three fetches away, and **none of the jars ships the text**.

🟡 **p140's `org.sakaiproject:kernel:25.2` is 404 on Central, confirmed again** — Central holds
60 versions of that coordinate, latest **23.3**. 🔵 **So `sakai-kernel-api:25.2`'s parent chain
is genuinely broken upstream: its POM names a parent version that was never published**, and no
amount of walking fixes it. The row survives only because it declares its own licence. 🟢 A
clean example of why the walker reports a fetch failure as a failure rather than as an absence.

### 🔴 Open edX: the licence is impeccable at the wheel and absent in everything inside it

`ACTION DA` measured the six top-level packages inside `openedx-core` **1.9.1**: 🔴 **zero
licence files, zero SPDX headers and zero copyright lines across 237 Python files**, against a
distribution that declares `AGPL-3.0-only` and ships **35 139 bytes** of licence text in
`dist-info/licenses/`.
[`p141-package-grant-layer`](../compose/code/p141-package-grant-layer/README.md).

🔵 **For this page the consequence is concrete and routine.** The normal way a studio uses Open
edX's learning core is not `pip install` — it is lifting `openedx_tagging/` or
`openedx_content/` into a service. 🔴 **A subtree lifted out of that wheel carries no grant, no
holder and no notice, and the obligation it silently carries is the most reciprocal on this
page.** 🟢 **The fix is one file per package and it costs nothing**: `P17`'s notice-injection
step already exists for exactly this, and this is the clearest case on the shelf for running it.

🟢 **And `openedx_learning` is confirmed alive as a package name** even though the *distribution*
`openedx-learning` is a retired shim: 29 files of live code at 1.9.1. 🔵 **Demoted from
distribution to subpackage, not killed** — the distinction `T27` exists to catch.

### 🟡 No platform row was added or removed from the ERP/LMS tier this pass, and that is stated rather than padded

Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, OpenEduCat, BigBlueButton, H5P, Tutor and
the national K-12 systems below are unchanged. 🔴 **Four global searches and four regional ones
returned no new platform**, and the single addition above arrived through the connector shelf
rather than the market channel — 🔵 **the third consecutive pass in which the artefact channel
produced what the demand channel did not.**


**Pass 140, 2026-10-12.** 🔴 **Two claims this page made about Sakai last pass are wrong, and the
correction is published here rather than quietly dropped.** 🆕 **A third platform row changes
identity entirely**: the package Open edX's learning core ships under has been renamed, and this
page has been pointing at the retired name.

### 🔴 CORRECTION — Sakai's two kernel artefacts have the SAME licence posture, not opposite ones

p139 wrote, on this page:

> *"Two artefacts of one kernel, same release line, **opposite licence posture**. The `api` jar
> declares **ECL-2.0** … and ships no text for it. The `impl` jar declares nothing at all."*

🔴 **`impl` does declare ECL-2.0** — inherited from `org.sakaiproject:oss-parent:1`, three levels
up its parent-POM chain, resolved by `ACTION CR`:

| coordinate | own POM | inherits | from | licence in jar |
|---|---|---|---|---|
| `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 | — | — | 🔴 **NONE** |
| `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🔴 nothing | 🆕 **ECL-2.0** | 🆕 `org.sakaiproject:oss-parent:1` | 🔴 **NONE** |

🔵 **Both are ECL-2.0. Only the declaration DEPTH differs** — and depth is exactly what an
off-the-shelf scanner reading one POM does not traverse. 🟢 **The sentence to put in front of
Sakai's maintainers is unchanged and now better supported**: `org.imsglobal:basiclti-util` 1.2.0
ships `META-INF/LICENSE` *and* `META-INF/NOTICE` for its Apache-2.0 grant, so 🔵 **this is
fixable build configuration, not a Maven law.**

🔴 **And the review burden on a Sakai integration is HIGHER than p139 said, not lower.** With
inheritance resolved, **5 of 5** Java artefacts on this shelf declare a licence and **4 of 5
(80%)** ship no text for it. A client doing classpath licence review gets `ECL-2.0` — *education's
own licence*, an Apache-2.0 derivative with a university patent clause that off-the-shelf scanners
do not recognise — from a **sibling POM three levels up**, and nothing whatsoever from the jar.
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🆕 🔴 Open edX: the learning-core package has been RENAMED, and this page tracked the retired name

`openedx-learning` **0.33.1** is not a broken release — it is a deliberate rename shim.
Its `setup.py`: *"Builds a final shell release of openedx-learning which simply 'redirects' to
openedx-core"*, with `packages=[]`, `install_requires=["openedx-core==0.34.1"]` and
`Development Status :: 7 - Inactive`.

| | retired | 🆕 current |
|---|---|---|
| package | `openedx-learning` 0.33.1 | 🆕 [`openedx-core`](https://pypi.org/project/openedx-core/) **1.9.1** |
| uploaded | 2026-02-18 | 🟢 **2026-10-09** |
| wheel | 🔴 1 479 B, 4 metadata paths | 358 188 B, **261 paths** |
| licence | AGPL 3.0 (legacy field) | 🔴 **AGPL-3.0-only** as a PEP 639 `License-Expression` |
| 🟢 licence payload | 🔴 none — it ships nothing | 🟢 `dist-info/licenses/LICENSE.txt`, **35 139 B** |

🔵 **For an institution customising Open edX, the practical consequence is a dependency rename,
not a licence change** — AGPL-3.0 either way, and the platform's copyleft posture on this page is
unaffected. 🟢 **What improves is auditability**: `openedx-core` ships its grant in the artefact
automatically under PEP 639, which is the cleanest licence payload this KB has measured, and
consolidates six top-level packages into one distribution.

🔴 **What a procurement conversation needs to know is the contact, and there are three of them.**
`openedx/XBlock` routes notices to `oscm@edx.org`; its sibling `openedx/codejail` routes to
`oscm@openedx.org`; the live PyPI artefact names `dave@axim.org`. 🟢 **The holder itself is
continuous** — edX Inc. was *renamed* Axim Collaborative, same trustees and tax ID, after Harvard
and MIT sold the edX brand to 2U. 🔴 **But `edx.org` is now operated by 2U**, a different company
from the steward, so one of those two repositories is routing its notice obligation to the wrong
organisation.

### 🔴 The attachment layer: a connector's tool surface moves with the DEPLOYMENT, not the version

p139 told this page that attachment review must *"enumerate `tools/list` against the live server,
not read the README"*. 🟢 **That instruction survives `ACTION CP` and the reason has changed.**

🟢 **On the npm connector shelf the README is not the problem the enumeration solves** — all eight
downloadable rows register literal tool names on a single server instance with no gate, so the
static count provably equals the live list. 🔴 **The enumeration is needed because of two shapes
that defeat any payload read:**

- 🔴 **Deployment-flag gating.** `ArnaudGuiovanna/tutor-mcp` registers **55** tool names and its
  own CI test asserts a live `tools/list` of **46**, gated on `deps.Institution`,
  `REGULATION_GOAL` and `deps.OAuthGranularScopes`. 🔵 **An institution that buys the
  institutional tier enables precisely the nine tools the vendor's documentation does not
  cover — three of them writes that author the curriculum a cohort is assessed against.**
- 🔴 **Two server instances in one package.** `@owen-x-tech/canvas-mcp` 1.1.0 exposes a different
  code path under `--http` than on stdio. Both happen to serve 62 tools, but the HTTP path names
  only **1** of them as a literal and registers 61 through a loop.

🔵 **So the line for an attachment review is: enumerate every transport the institution will
connect on AND every flag its contract enables, and record the flag set beside the count.** A
tool count with no configuration attached is not a measurement. `P18` step 5 is amended
accordingly.

### 🆕 🟢 Two connector rows place themselves on a hostname — and one of them is a misconfiguration

| row | evidence | region |
|---|---|---|
| 🟢 `eth-moodle-mcp` 1.3.3 | `moodle-app2.let.ethz.ch` (4×), `safari.ethz.ch` | 🟢 **EMEA** — ETH Zürich |
| 🟢 `mcp-canvas-lms` 1.0.5 | `canvas.ust.hk` (2×) | 🟢 **APAC** — HKUST, Hong Kong |

🔴 **For a platform owner, `mcp-canvas-lms` is the row with an operational defect, not just an
origin.** It reads `CANVAS_BASE_URL` in `dist/common/utils.js:4` and then hardcodes
`https://canvas.ust.hk/api/v1/courses` in `dist/operations/canvas.js:58`. 🔵 **One of its three
tools queries a different university's Canvas tenant regardless of configuration** — which is a
data-egress question for any institution that installs it, and it is invisible from the README.

🔴 **Host reachability could not be confirmed**: all three institutional hosts answer `403` at
`CONNECT` through this environment's proxy, which this pass established refuses **university**
hosts as well as the government hosts p139 diagnosed. The evidence is the compiled-in hostname,
not the host's liveness.

### 🟡 No platform row was added or removed this pass, and that is stated rather than padded

🔵 **The platform shelf below is unchanged.** Moodle, Open edX, Canvas, Sakai, BigBlueButton,
H5P, Kolibri and OpenEduCat are where p139 left them; the mandated vertical-platform search
returned only rows this page already carries (OpenEduCat LGPL-3, `frappe/education`, ERPNext,
RosarioSIS). 🔴 **Everything above is a correction to how an existing row should be READ**, which
is the kind of movement this page should expect once its shelf is saturated.

**Pass 139, 2026-10-12.** 🟡 **No platform row changed this pass either, and it is again stated
rather than padded.** But two measurements this pass land *on* the platform layer rather than beside
it, and one of them is about Sakai itself.

### 🔴 Sakai's own published artefacts do not carry the licence Sakai declares

`ACTION CM` probed Maven Central, where the Java platforms on this page actually ship. Two Sakai
kernel artefacts, **sha1-verified against the repository's own `.sha1`**:

| coordinate | version | POM declares | jar paths | licence file in jar |
|---|---|---|---|---|
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | **25.2** | 🔴 **Educational Community License 2.0** | **578** | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing declared** | **524** | 🔴 **NONE** |

🔵 **Two artefacts of one kernel, same release line, opposite licence posture.** The `api` jar
declares **ECL-2.0** — *education's own licence*, an Apache-2.0 derivative with a patent clause
written for universities — and ships no text for it. The `impl` jar declares nothing at all.
🔴 **A client doing classpath licence review on a Sakai integration gets `ECL-2.0` from a sibling
POM file and nothing from the jar**, and ECL-2.0 is exactly the identifier an off-the-shelf scanner
does not recognise. Detail and method:
[`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

🟢 **The contrast row matters as much**: `org.imsglobal:basiclti-util` 1.2.0 ships
`META-INF/LICENSE` **and** `META-INF/NOTICE` for its Apache-2.0 grant. 🔵 **So this is fixable
configuration, not a Maven law** — which is the sentence to put in front of a platform's maintainers.

### 🔴 The attachment layer: what `install` actually gives an institution

This page's standing claim is that AI attaches to these platforms through connectors rather than by
forking platform source. Pass 139 measured what those connectors contain, and two results change how
an attachment should be reviewed:

- 🔴 **A connector's tool list is not its documentation.** Across the nine npm connector rows,
  **411** tools are registered and **249** documented; **62** of the 162 undocumented ones **write**
  to the LMS. For Canvas specifically, `@imazhar101/mcp-canvas-server` registers **227** tools with
  **61 undocumented writes**, including `bulk_update_grades`, `grade_submission`, `create_user`,
  `update_user_login` and 🔴 **`update_sso_settings`** — a tool that changes how the tenant
  authenticates. 🔵 **Attachment review must enumerate `tools/list` against the live server, not
  read the README.**
- 🔴 **An npm connector may not contain the connector.** `@exhabition/brightspace-mcp` is an
  **82-line loader** that downloads a Rust binary from GitHub Releases on first run, `chmod 0o700`s
  it and executes it, with **no checksum or signature verification**. 🔵 **For a Brightspace
  institution that is a procurement question, not a packaging detail.**

Both measured in [`p139-tool-count-drift`](../compose/code/p139-tool-count-drift/README.md).

### 🟢 The brokered-identity seam was executed against a live server, and it works

p138 read `canvas-lms-mcp`'s `OAuthStore` interface and called it sufficient for pattern `P13`.
`ACTION CL` ran it. 🟢 **With a grant pre-seeded into the store, `POST /oauth/token` returned
HTTP 200 with a Bearer access token, the seeded scopes (`canvas:read canvas:write`), a rotated
single-use refresh token — and ZERO contacts with Canvas**, measured by a sentinel listener rather
than inferred.

🔴 **But the documented embedder entry point cannot be imported.** `dist/http.js` calls `main()` at
module top level with no `import.meta.main` guard, so importing `canvas-lms-mcp/http` parses the
*importer's* `process.argv` and calls `process.exit(1)`. 🔵 **So the attachment shape for an
institution that already holds Canvas tokens is: seed the encrypted grant store, run `serve` as a
managed process.** Not an in-process embed — which is cheaper on protocol work and dearer on
plumbing. Full transcript:
[`p139-oauthstore-adapter`](../compose/code/p139-oauthstore-adapter/README.md).

### 🔴 One platform-adjacent library of this page is currently an empty package

🔴 **`openedx-learning` ("Open edX Learning Core (and Tagging)") ships no code in its two most
recent releases** — 0.33.0 and 0.33.1 are **1 479-byte** wheels containing only `dist-info`
metadata, down from **257 553 B** at 0.32.0, across 79 releases. `pip install openedx-learning`
resolves to the empty one. 🔵 **Anyone pinning Open edX's learning core from PyPI right now should
pin `0.32.0`**, and this is the kind of state a studio should verify at the payload layer before an
engagement rather than after.


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟡 **No platform row changed this pass either, and it is stated rather
than padded for the second consecutive time.** `ACTION CH` was spent on the **attachment** layer —
the connector packages that bolt onto the platforms below — and it produced a finding that changes
how the platforms are *integrated* rather than which ones are listed: 🔴 **per-file licence notice
is practised by 1 of the 21 published connectors, so a developer who lifts one file out of an
attachment into a client codebase carries no holder and no grant with it.** 🟢 **The platform table
below is p137's, unchanged.** 🔵 **The four regional searches returned no new platform**, and the
one new regulatory item they surfaced (Texas HB 149, in force 2026-01-01) could not be read in this
channel and is registered rather than published.

**Pass 138, 2026-10-12.** 🟡 **No platform row changed this pass, and that is stated rather than
padded.** `ACTION CD`, `CE`, `CF`, `CG` and part of `CI` were spent on the **connector** layer that
attaches to these platforms, not on the platforms themselves — so the platform table below is
p137's, unchanged, and this page's own measurement this pass is about what happens when a client
*installs* one of the attachments.

🔴 **The attachment layer has a distribution defect this page must flag, because it lands on the
copyleft platform.** Of **21** education-LMS connector packages probed at the payload layer,
**9 ship no licence file**, and the worst is the one attached to Moodle:
`moodle-mcp-server-aql` **0.1.7** declares **AGPL-3.0** across **141 shipped paths** with no licence
text, while its repository
([`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)) carries the
canonical **34 523-byte** grant. 🔵 **For this page the consequence is specific**: a studio that
attaches an AGPL-3.0 connector to a GPL-3.0 platform inherits the strongest obligation on the shelf
and is handed none of the text that states it.
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🟢 **One attachment-point fact worth adding to this page.** Moodle now has **three independent
connectors in three different languages**, sharing no implementation —
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) (**AGPL-3.0**,
Node workspace monorepo), [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server)
(**MIT**, **Go**, with a committed `go vet` / `staticcheck` / `-race` / coverage harness) and
`GhaithAlHallak8/moodler-mcp` (**MIT**, **Python**, `playwright`-driven session) — plus at least six
more Moodle packages on npm that this KB's slug-first method never surfaced. 🔵 **For the
permissive-side route this page recommends (`P7`), the Go row is the only one that ships its own
test-and-lint discipline, and the only permissive one whose canonical address is not in question.**

**Pass 137, 2026-10-11.** 🔴 **The licence column on this page is a ROOT licence column, and for the
platforms a client actually runs that is now a measured understatement.** `ACTION BY` enumerated the
trees of the twenty largest rows across this KB's platform and foundation layers: **10 of 20 carry a
licence file whose holder is not the project** (`compose/code/p137-foreign-holder-tree`). The
platforms on this page are the worst of it, because they are the biggest:

| platform | root licence | what the tree adds |
|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | 🔴 **96 non-root licence files, 87 real grants, 66 of them somebody else's** — Fonticons, CKSource, OTPHP (Florent Morselli) under `admin/tool/mfa/factor/totp/extlib`, the QUAIL accessibility library, and more |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | ECL-2.0 | 🔴 **76 / 58 / 13**, including **The Trustees of Columbia University** (`delegatedaccess/NOTICE`), the Apache Software Foundation and AOL LLC |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 🔴 **28 / 22 / 17** — d3, highlight.js, the Harmattan font, Symfony contributors |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 *(payload-read, p135)* | 🔴 **17 / 13 / 10** — Bootstrap, Font Awesome, Tiny Technologies' editor, Adobe cmaps, Dailymotion |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 🟢 **`gems/lti-advantage/LICENSE.txt` is MIT, held by a named individual.** The LTI Advantage implementation inside the dominant North-American LMS is the **permissive** part of it |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 🔴 **18 / 11 / 9** — pdf.js with Adobe's cmaps, the PDFium Authors, Google's Liberation data, Mozilla |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 LGPL-3.0 *(payload-read, p131)* | 🟡 **14 licence-shaped non-root paths and not one readable grant** — no family anchor, no dated notice. A measured *unreadable* class, not a measured absence |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | 🟡 one foreign holder, and it is a **Debian packaging** copyright under `platforms/debian-server/debian/copyright` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor), [`frappe/lms`](https://github.com/frappe/lms), [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | AGPL-3.0 / AGPL-3.0 / GPL-3.0 | 🟢 **`ROOT_ONLY` — the root file is the whole story.** The cleanest licence position of any platform here |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 Apache-2.0 | 🔴 **`ROOT_ONLY` and that is misleading**: it composes Kiwix, Kolibri and Ollama **as container images**, so its third-party obligations exist and are not in its tree at all |

🔵 **What to do with this on an engagement.** The licence cell still decides whether a *derivative*
can ship. 🟢 **The tree decides what goes in the NOTICE file**, and for a Moodle or Sakai derivative
that is now a countable task with a number next to it rather than a vague caution.

## 🆕 The procurement route into these platforms, EMEA — `ACTION CC`

🔴 **p136 recorded European procurement data as "does not exist on this KB's pages", measured as an
empty probe.** 🟢 **It was a vocabulary problem**: the words that work are *framework agreement*,
*tender* and *catalogue*, not *procurement*.

| route | what it is | the date that matters |
|---|---|---|
| **Jisc digital assessment tools framework** | market engagement for digital assessment solutions across UK further and higher education | 🟢 **Responses closed 2026-03-13; contract runs 2026-11-01 → 2029-10-31** — a four-week window at the time of this pass |
| **Jisc Google for Education reseller framework** | single-lot, multi-supplier framework; 🟢 **the published scope names Gemini for Education**, with Google pricing under a separate Jisc–Google agreement | published **April 2026** |
| **Jisc Chest** | catalogue/purchasing service: members buy **without running their own tender** (LearnWise AI is listed on it) | standing route |
| **Jisc VR/AR framework** | immersive-technology procurement vehicle | standing route |

🟢 **Why this belongs on a platforms page**: an AI layer sold into a UK institution does not need a
new tender if it arrives through a framework the institution already calls off. 🔴 **SURF — the Dutch
equivalent — returned nothing**, so the Netherlands remains a hole, and it is now a *measured* one.

---

**Pass 135, 2026-10-11.** 🟢 **This page's longest-standing unresolved licence cell is resolved by
payload read, and the answer promotes a platform the page had written off.** `OpenOLAT` has sat in
*Declared gaps* as *"survives as unresolved — its own documentation describes an Apache-2.0 basis
that GitHub's matcher does not recognise, and no payload read is on record here."* 🔴 **A payload
read is now on record, and the matcher was defeated by something neither side guessed.**

🟢 **Two platforms are added**, both permissive, both pushed the day before this pass:
**OpenOlat** (a full LMS with QTI and SCORM built in) and **Mentingo** (an AI-native LMS under MIT).
🟢 **One authoring platform is added** — **Adapt Framework**, the largest repository in the entire
standards stack at 630★.

🔵 **Licence cells added or corrected this pass were established by sha256 identity against
canonical SPDX texts**, not by GitHub's badge — `compose/code/p135-licence-sha-identity`, which
discharges `ACTION BP`.

**Pass 132, 2026-10-11.** p131's structure and rows retained; 🔴 **a whole category of platform is
ADDED below — the national K-12 school platforms, which carry more AI connectors than Moodle and
which no previous pass of this KB had listed at all** (see `README.md` → Pass 132, `P132-A`). The
Kolibri row is also corrected. This page answers one question: *the client runs X — where does AI
attach, and what does the licence let us ship?* Repo-level verification lives in
`repos/foundations.md`; this page is about the attachment, the integration standard and the
constraint.

## The attachment points, before the platforms

Four ways to put AI into an existing education platform, in increasing order of coupling:

1. **LTI 1.3 / LTI Advantage** — the external tool is launched from inside the LMS with signed
   identity and grade passback. Touches no platform source, so **no copyleft reciprocity at all**,
   and works across Moodle, Canvas, Open edX, Sakai, Blackboard, D2L and ILIAS. Library:
   [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (MIT). **This is the default
   recommendation** and the one most engagements under-use.
   🟢 **Corrected by p134 — the library to reach for is not the one this page has been naming.**
   `ims-lti` (MIT, 203★) is Instructure's library. The platform-independent reference implementation
   is [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — **Apache-2.0, 373★, pushed 2026-10-06**,
   with OIDC launch, Deep Linking, **AGS grade passback** and NRPS rosters, plus first-party database
   plugins. In Python, [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT,
   138★) — 🔴 **but dormant since 2024-08-18, which is the weak link for an agent build.** For a PoC,
   [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter)
   (MIT) is a template over `ltijs`. 🟢 **And for the first time this page can name a conformance
   test:** [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests)
   (Apache-2.0) for the rostering side.
2. **MCP against the platform's REST API** — the agent gets tools, the platform stays untouched.
   Connectors on the shelf in `agents/top.md`.
3. **Plugin / XBlock inside the platform** — deepest UX integration, inherits the platform's
   licence obligations for the plugin.
4. **Fork the platform** — only defensible when the licence is permissive and the client wants to
   own the product.

## Platforms and where AI goes

| platform | licence | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **Moodle** — [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Moodle plugin types, or the AI subsystem introduced in the 4.5+ line; LTI for anything you want to keep out of GPL | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) (GPL-3.0, 222★ — tutoring, quiz generation, RAG over course materials); [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) (GPL-3.0, 16★ — Saylor Academy's "SOLA" learning coach, a real institutional deployment); [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) (17★, **unlicensed** — MCP as a web-service plugin, listed on marketplace.moodle.com). 🟢 **CORRECTED BY p131 — the permissive route exists and p130 denied it:** a *standalone* MCP server against Moodle's web-service API needs **no in-tree plugin and inherits no GPL obligation**. [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) is **MIT** (43★, verified at pass 30 of this KB as the licence-boundary exemplar), with [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) (**MIT**, assessment + gradebooks, writes gated), [`1alexandrer/moodle-mcp`](https://github.com/1alexandrer/moodle-mcp) (**MIT**, template) and [`Deeptanshuu/mydy-lms-helper`](https://github.com/Deeptanshuu/mydy-lms-helper) (**MIT**, single-institution worked example). Avoid [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) (40★, **no licence**). Build help: [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) (MIT). **Delivery note:** GitHub is a mirror; contribution goes to git.moodle.org. |
| **Open edX** — [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **XBlock** ([`openedx/XBlock`](https://github.com/openedx/XBlock), Apache-2.0) is the clean route — the component framework is permissive even though the platform is not. Operations go through **Tutor** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (AGPL-3.0, 2★, experimental) is the only MCP path. Sandboxing for generated/learner code: [`openedx/codejail`](https://github.com/openedx/codejail) (Apache-2.0). Analytics: `tutor-cairn`. |
| **Tutor** (Open edX distribution) — [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | Write a Tutor plugin (cookiecutter provided) to ship AI services as containers alongside the platform | Plugin family is first-party and broad: `tutor-mfe`, `tutor-cairn`, `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. A Tutor plugin is how an AI service gets deployed and upgraded with the platform rather than beside it. |
| **Canvas** — [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | Canvas's REST API is the richest of any LMS — hence MCP first, LTI second. Avoid forking | The deepest connector ecosystem in education AI: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 288★, canonical) and [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT, 9★). Avoid [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) (103★ but **no licence**). |
| **Kolibri** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Fork freely, or extend the Python app directly; content pipeline via [`learningequality/studio`](https://github.com/learningequality/studio) (MIT). 🟢 **Or do not integrate at all — orchestrate it** | 🔴 **CORRECTED BY p132. The claim that this was "the most valuable unfilled slot in the whole KB" is false.** [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) (**Apache-2.0, 39 444★**) already runs **Kolibri as its education container** beside **Kiwix** (library) and **Ollama** (AI assistant), as a Docker orchestration layer. It is the second-largest repo in this KB. Also [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) (20★, macOS port) and [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) (2★, Indian Class-10 curriculum, claims Kolibri integration). 🟢 **The surviving slots are narrower: nothing builds AI *inside* Kolibri** (NOMAD attaches from outside), **and nothing offline targets LATAM.** See pattern P2 in `compose/patterns.md`. |
| **Sakai** — [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** (permissive) | Java tool/provider model, or LTI | No notable AI-on-top found. Attractive because the licence is permissive and the installed base is institutional Java estate. |
| **Chamilo** — [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | Plugin API, or LTI | No notable AI-on-top found. Matters for engagement reach: real adoption in Francophone Europe and Spanish-speaking LATAM, where Moodle/Canvas assumptions do not hold. |
| **ILIAS** — [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | Plugin slots, or LTI | No notable AI-on-top found. Chosen in EMEA public-sector procurement for standards and accessibility compliance — the same reasons that make AI features there a documentation exercise as much as an engineering one. |
| **OpenOLAT** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** — verify | Java extension model, or LTI | No notable AI-on-top found. Swiss/German university base. |
| **OpenEduCat** — [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read; the API's `NOASSERTION` is a matcher artefact) | Odoo module (it is an Odoo app), so the whole Odoo module ecosystem applies. **LGPL permits linking without reciprocity** — so an AI service calling it from outside is clean | No notable AI-on-top found. **The ERP slot** — admissions, records, timetabling, fees. This is where "80% of routine administration automated" claims would have to land. 🟢 **And the tier is wider than p130 said:** `frappe/education` (662★), `academico` (MIT, 404★), RosarioSIS, Gibbon, openSIS, Fedena — see `repos/foundations.md`. |
| **BigBlueButton** — [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Use the API/webhooks and the recording pipeline; LGPL permits linking without reciprocity | No notable AI-on-top found. The live-classroom surface: transcription, session summarisation, participation analytics, post-session question generation. Install and front-end: `bbb-install`, `greenlight`. |
| **Oppia** — [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | Fork or extend directly — no reciprocity | No notable AI-on-top found. Its lesson model already encodes misconceptions explicitly, which is exactly the structure an LLM tutor needs and usually lacks. Permissive + pedagogically structured is a rare combination. |
| **Frappe LMS** — [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | Frappe app; inherits the Frappe/ERPNext data model | No notable AI-on-top found. Pick when the client already runs ERPNext and wants learning next to HR and finance data. |
| **H5P** — [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | Content type authored once, embedded into any host LMS (`moodle-mod_hvp` for Moodle) | The standard delivery vehicle for generated interactive content: have an agent produce H5P content types and they render in every platform above. |
| **Richie** — [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | Django/React CMS in front of Open edX | The catalogue/portal layer. MIT, so the public-facing surface can be customised freely even when the LMS behind it is AGPL. |
| **SCORM/xAPI** — [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | Runtime shim | How legacy courseware a client already paid for keeps working, and how learner interaction data gets out of it for analytics. |
| **Blackboard** (proprietary) | n/a | API only | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, 11★, Peru) is the only open connector found. Blackboard retains significant higher-ed share, especially in LATAM, and is almost entirely unserved by open source. |

## The category this page was missing: national K-12 school platforms

🔴 **Every platform above is an LMS or an ERP, and in most of EMEA and APAC that is not what a
school actually runs.** A Polish school runs **Librus**. A Slovak or Czech school runs **EduPage**.
A French school runs **Pronote**. A German one runs **IServ**. These are the systems of record for
grades, attendance, homework and parent communication for millions of pupils — and this KB had
never listed one.

🟢 **Extended by p133 to LATAM and ANZ, and the same rule holds with different nouns.** A Brazilian
federal university runs **SIGAA**; a Brazilian federal institute runs **SUAP**; an Argentine
university runs **SIU-Guaraní**; an Australian school runs **SEQTA**; a New Zealand school runs
**KAMAR**. 🔴 **None of these five was on this page before p133, and together they carry 12 of the
category's connectors — including every teacher-facing one this KB has found.**

🟢 **They are also, by connector count, better served by open-source AI than Moodle is.** The
connectors are tiny and unofficial, but they exist and they map the API surface.

| platform | country | proprietary? | the attachment point | open connectors that exist |
|---|---|---|---|---|
| **Librus Synergia** | Poland | yes | portal login; no public partner API found | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) — 🟡 **MIT (2.x)**, `legacy_reference/` **GPL-3.0-only**, 10★. The largest connector of the tier. 🔴 Unofficial, *"not affiliated with Librus"*, and **no 2FA support** |
| **EduPage** | Slovakia / Czechia | yes | portal login | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) (**MIT**, 3★ — timetables, grades, homework, **meal ordering**, multi-school discovery, 2FA) and an independent second implementation [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) (**MIT**, 1★). 🟢 **Two independent implementations is the strongest demand signal in the tier** |
| **Pronote** | France | yes | portal login | [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) (**MIT**, 1★) — grades, timetables, homework, absences |
| **IServ** | Germany | yes | portal login | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) (**MIT**, 0★) — parent letters, timetables, **sick notes**. 🔵 The only connector in this KB whose user is a **parent** |
| **Sisu (Funidata)** | Finland (higher ed) | yes | institutional SIS API | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) (🔴 **no licence**, 1★) — written for **any** Sisu deployment, so the broadest reach of the tier, and unusable as published |
| **uSaint** | South Korea (higher ed) | yes | via `rusaint` | [`yourssu/soongpt-plugin`](https://github.com/yourssu/soongpt-plugin) (**MIT**, 3★) — course search, timetable planning, **graduation requirements**. Org-owned |
| **VTOP** | India (VIT) | yes | portal login | [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) (**Apache-2.0**, 4★) — attendance, marks, timetable, exams |
| **QLDT** | Vietnam (Hanoi Univ.) | yes | portal login | [`qxbao/qldt-hanu-mcp`](https://github.com/qxbao/qldt-hanu-mcp) (**GPL-2.0**, 1★). 🔴 **Jurisdiction warning:** Vietnam's Decision 33/2026/QD-TTg names education, including automated assessment and behavioural monitoring, as high-risk |
| **SIGAA** | Brazil (federal universities) | yes (SIG/UFRN-derived) | portal login | 🟢 **The deepest connector shelf of any platform on this page — 5 rows.** [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0, 20★ — deadlines → Google Tasks), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**, 19★), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**, 16★ — UI modernisation), [`MatheusMach/QuantoFalta`](https://github.com/MatheusMach/QuantoFalta) (🔴 no licence, 9★ — absence counter), and 🔴 **the teacher-facing one:** [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) (**MIT**, 9★ — grade entry from a spreadsheet) |
| **SUAP** | Brazil (federal institutes / IFs) | yes | portal login + institutional API | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**, 0★) and [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 no licence, 0★) — 🟢 two independent MCP implementations. Plus [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) (🟡 **AGPL-3.0**, 1★), **org-owned**, which drafts a lecturer's **RIT** workload report |
| **SIU-Guaraní** | Argentina (university consortium) | yes | portal login | [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) (**MIT**, 17★), [`despedite/siu-guarani`](https://github.com/despedite/siu-guarani) (🟡 GPL-3.0, 8★ — seat watcher), [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) (🔴 no licence — **teacher** grade upload). 🟢 **Uniquely, the vendor consortium is itself on GitHub:** [`SIU-Toba/docker-guarani`](https://github.com/SIU-Toba/docker-guarani) (🔴 no licence, 4★, dormant since 2017) |
| **SEQTA** | Australia | yes (TheSchoolBox) | portal login | 🟢 **The best-licensed and only product-shaped corner of this category.** [`BetterSEQTA/BetterSEQTA-Plus`](https://github.com/BetterSEQTA/BetterSEQTA-Plus) (**MIT**, **40★**, org-owned, 25 forks, Chrome Web Store, pushed 2026-10-06) and [`BetterSEQTA/DesQTA`](https://github.com/BetterSEQTA/DesQTA) (**MIT**, 16★ — native desktop port) |
| **KAMAR** | New Zealand | yes | portal login | 🔴 **One row, archived.** [`st22209/Parent-Portal`](https://github.com/st22209/Parent-Portal) (**MIT**, 2★) — README: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. 🔵 **Keep this row on the page precisely because it is dead: it is this category's only measured example of what a vendor API change does to an unsanctioned connector.** |
| **Visual Schedule Builder (VSB)** | Canada | yes | institutional API | [`luca-dupont2/mcgill-vsb-mcp`](https://github.com/luca-dupont2/mcgill-vsb-mcp) (**MIT**, 2★ — conflict checks and schedule generation **without browser automation**) and [`SleepyPandas/UofT-MCP`](https://github.com/SleepyPandas/UofT-MCP) (**MIT**, 1★) |

🔴 **The attachment point for this whole category is the problem, not the opportunity.** There is no
LTI here, no MCP-friendly partner API, and no vendor programme — the connectors log in **as the
pupil or the parent, with their password**, against a platform that has not sanctioned it. For the
four K-12 platforms that is children's attendance and grade data under GDPR with no processing
agreement, and `librus-mcp` only works where **two-factor authentication is switched off**.

🟢 **How to use this category in an engagement anyway, which is the genuinely valuable part:**

1. **As integration intelligence.** The expensive, slow work — mapping each platform's undocumented
   API surface — is done and published under MIT. Read it, keep the surface map, rebuild the auth.
2. **As the opening for a sanctioned integration.** None of these vendors has an agent story. A
   studio that brings one a properly authenticated, logged, DPA-backed connector is not competing
   with open source; it is replacing a password-scraper the vendor would rather did not exist.
3. **Never deploy one as-is.** See the credential-model blocker in `agents/top.md`.

### 🆕 Four more national academic systems, and one national dataset *(p134)*

p133 added SIGAA, SUAP, SIU-Guaraní, SEQTA and KAMAR. 🟢 **p134's `ACTION BJ` sweep adds four more
and records two hard zeros with their probes named** — because an unprobed platform and an empty one
are different findings, and only one of them is information.

| platform | country | what it is | open-source AI/connector supply found | probe |
|---|---|---|---|---|
| **Q-Acadêmico** | 🟢 **Brazil** | The academic system of Brazil's **federal institutes** (IFs) — a fourth Brazilian national system alongside SIGAA, SUAP and the SAE family | 🟡 **~7 real rows out of 85 hits, topping out at 6★.** Best-licensed: [`adiel-calixto/IFAcademico`](https://github.com/adiel-calixto/IFAcademico) (**Apache-2.0**, 6★, 2026-04-26, Android). Also [`WKolodziejski/QMobile`](https://github.com/WKolodziejski/QMobile) (no licence, 6★, IFSul), [`MuriloCalegari/Ifes-Academico`](https://github.com/MuriloCalegari/Ifes-Academico) (GPL-3.0, 4★ — syncs grades, so **staff-adjacent**), [`kkauaon/qaluno`](https://github.com/kkauaon/qaluno) (no licence, 4★, IFCE), [`AlexandreL0pes/q-scraper`](https://github.com/AlexandreL0pes/q-scraper) (no licence — self-declared scraping) | `q-academico` |
| **SAES** (*Sistema de Administración Escolar*) | 🟢 **Mexico** | The academic portal of the **Instituto Politécnico Nacional** and other Mexican institutions | 🔴 **19 hits and effectively nothing usable.** Only 3 carry a permissive licence; the rest are unlicensed student scrapers. 🟢 **Two are conversational agents** — [`DanieelRC/SAES-R`](https://github.com/DanieelRC/SAES-R) (*"incluye un agente conversacional"*) and [`DanieelRC/AgenteConversacional-SAES-R`](https://github.com/DanieelRC/AgenteConversacional-SAES-R) (answers questions on the IPN academic regulations, *"para profesores"*) — 🔴 **both unlicensed, both 0★.** The one MIT row is a utility library, [`roncuevas/ipn_saes_utils`](https://github.com/roncuevas/ipn_saes_utils). [`pekochu/SAES2GO`](https://github.com/pekochu/SAES2GO) (GPL-3.0, 4★) **declares itself obsolete** | `saes escolar` |
| **SIMAT** (*Sistema Integrado de Matrícula*) | 🟢 **Colombia** | The national school-enrolment system run by the Ministry of National Education | 🟢 **One row, and it is a different species from everything else on this page:** [`juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia`](https://github.com/juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia) (🔴 **no licence field**, 1★, pushed **2026-10-10**) — a CRISP-DM pipeline joining **C-600, SIMAT and IPM** with territorial variables to raise **explainable dropout-risk alerts for a Secretaría de Educación**. 🔵 **Not a portal connector and not a chatbot: a government-facing early-warning model.** The only row in this KB aimed at a ministry rather than a student | `simat colombia` |
| **SIAGIE** | **Peru** | The national school information system (MINEDU) | 🔴 **NO EVIDENCE FOUND FOR THIS PLATFORM.** `siagie peru in:name,description` → **`total_count: 0`**. Reported per `agents/top.md` clause 4 as a platform-level absence with its probe named — **not** as a Peruvian zero, since Peru's one row ([`campus-cli`](https://github.com/alejooroncoy/campus-cli), ISC, 11★) targets Blackboard | `siagie peru` |

🔵 **What the four of them together say, and it is the most useful sentence on this page for a LATAM
engagement:** **Brazil has four national academic systems and a real builder community around each;
Mexico has one with a scraper community and no licences; Colombia's activity is aimed at the
ministry rather than the portal; and Peru's national system has no open-source footprint at all.**
Four countries, four different market shapes — which is why "LATAM" is not a strategy.

## 🟢 The category this page has been missing in the other direction: vendors that publish their own integration *(new, p134)*

🔴 **Every platform section above this one describes something a client runs and we attach to from
outside, usually unsanctioned.** These are the opposite: **the vendor ships the integration path
itself, under a permissive licence.** That makes them the shortest route to a defensible engagement,
and this KB had never listed one.

| platform | vendor / region | what the vendor publishes | licence |
|---|---|---|---|
| **WISEflow** | 🟢 **UNIwise ApS — EMEA (Denmark)** | [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) — user creation, flow setup, **assessor allocation** and **grade passback** against the WISEflow API. 🟢 **Licence payload-read and the holder is the vendor company itself.** WISEflow is a digital-assessment platform used across Nordic and UK higher education — so this is an **assessment** counterparty, the segment `intel/trends.md` records as the fastest-growing | **MIT** |
| **Blackboard Learn** | **Anthology — North America** | Two LTI 1.3 Advantage reference tools in Blackboard's own org: [`BBDN-lti-1p3-tool-example`](https://github.com/blackboard/BBDN-lti-1p3-tool-example) (Python/Flask, **Apache-2.0**) and [`BBDN-LTI-Adv-Node`](https://github.com/blackboard/BBDN-LTI-Adv-Node) (Node/React, 🔴 **no licence field**). 🟢 **Plus a public REST API that four of the seven Blackboard connectors in `agents/top.md` actually use** | **Apache-2.0** (one of two) |
| **TAO** | **Open Assessment Technologies — EMEA (Luxembourg)** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) — OneRoster import into the TAO assessment platform | 🟡 **GPL-2.0** |
| **Ed-Fi ODS** | 🟢 **Ed-Fi Alliance (standards body) — North America** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) — serves a **OneRoster 1.2 API from an Ed-Fi ODS**, pushed 2026-10-09 | 🟢 **Apache-2.0** |
| **Google Classroom estate** | 🟢 **Google — North America** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) — conformance tests proving a OneRoster integration correct | 🟢 **Apache-2.0** |
| **Aeries SIS + Edgenuity** | **North America (Fresno, California)** | [`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback) — keeps an **Aeries** gradebook current from **Edgenuity**. 🔴 **No licence field**, 0★. 🔴 **And its content could not be reached:** repo search returns it with metadata, but the raw lane returned 404 for 15 candidate paths across `HEAD`/`main`/`master`, so **this pass verified that the repository exists and did not verify that it contains anything.** 🟢 **Listed because of who owns it: a US school-district-adjacent org publishing its own passback job** — the K-12 integration need, in public, from the buyer's side | 🔴 **none** |
| 🆕 **TKAWEN OS** *(p136)* | 🟢 **TKAWEN — EMEA (Algeria)** | [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) — an **OpenAPI v1 spec, a TypeScript SDK and an MCP server** for an academy's live catalogue, instructors, certificate verification and, with a learner token, that learner's own dashboard, courses and transcript. 🟢 **Read-only by construction: the repo states it ships no write tool of any kind** — no cart, checkout, review, discussion or progress write. 🟢 **Auth is a learner bearer token, never a password**, and its `whoami` returns the token's abilities and expiry *"never the token itself"*. 🔴 Carries topics `lti`, `scorm`, `xapi` and implements none of them — in the SDK those are **lesson-type enum values**. 🔵 **The first North-African supply row on this page**, and 0★ | 🟢 **MIT** *(payload-read, 1 063 B)* |
| **Agilix Buzz** | **North America (Idaho Digital Learning Alliance)** | [`RyanGravetteIDLA/qualtrics-lti-connector`](https://github.com/RyanGravetteIDLA/qualtrics-lti-connector) — LTI 1.3 bridge from Buzz LMS to Qualtrics with automated grade passback. 🔴 **ARCHIVED** | **MIT** |
| **Virtual Arkansas** | **North America (state virtual school)** | [`virtualarkansas/jupyterlite-zestables`](https://github.com/virtualarkansas/jupyterlite-zestables) — JupyterLite notebooks packaged as Canvas content with assessment and state persistence. 🔴 No licence field | 🔴 **none** |

🔵 **The pattern across this table is the sales argument.** 🟢 **Where a vendor or a public body
publishes its own integration, the licence is usually permissive and the auth is sanctioned.**
🔴 **Where a school district or state agency publishes one, it is usually unlicensed** — not out of
hostility but because nobody asked them to add a `LICENSE` file. **That is a conversation, not a
blocker: an unlicensed repo from an institutional owner is the one case where asking for a grant is
likely to succeed**, unlike the 20-odd unlicensed student scrapers elsewhere in this KB.

### 🆕 The open-source education ERP field, named properly *(p134)*

`repos/foundations.md` carries `openeducat_erp` (LGPL-3.0, 886★) and `frappe/lms` (AGPL-3.0). The
surrounding product field, for when a client asks what else exists:

| product | licence | what it covers | note for an engagement |
|---|---|---|---|
| **OpenEduCat** | LGPL-3.0 (payload-read, per `repos/foundations.md`) | Admissions, attendance, exams, fees; **73+ modules**; built on **Odoo**/Flectra, so it sits beside Odoo finance and HR | 🟢 **The Odoo base is the point** — an AI module attaches as an Odoo addon, and the client's non-education ERP data is already in the same schema. 🟡 Vendor lists a paid tier from ~US$575/yr alongside the free community edition; treat vendor TCO claims as marketing |
| **Frappe Education** | AGPL-3.0 | Student enrolment, class assignments, assessments, fee collection, on the Frappe framework | Same reasoning as `frappe/lms` — adjacency to Frappe/ERPNext finance and HR. 🔴 AGPL: fine inside a client estate, a problem if offered as a hosted service |
| **RosarioSIS** | 🟡 **GPL-2.0** | K-12 student information system; PHP + PostgreSQL/MySQL | 🔴 **Still zero agent coverage** — one of the open-source systems of record this KB has flagged as unserved for several passes. `compose/patterns.md` → **P9** |
| **openSIS** | varies by edition — **verify** | K-12 and higher-ed school information system | 🔴 **Community/commercial split: do not assume the public edition's licence covers the feature a client saw in a demo.** Unverified by this pass |
| **Gibbon** | not verified this pass | School platform | 🔴 **Named in listicles with no detail.** This pass found no primary evidence; it remains an unexamined row, recorded so a later pass does not mistake absence of evidence for evidence of absence |

🔴 **Instrument note on this subsection, because it is weaker than the rest of the page.** These
five rows come from **vendor pages and listicles via web search**, not from repo search or a payload
read. One review source was ~656 days old. 🟢 **Everything else on this page is repo-verified;
this table is not, and a client-facing claim should be re-verified against each project's own
repository first.**

## 🟢 Platforms added by p135 — and one licence cell finally resolved

| platform | licence *(hash-verified this pass)* | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **OpenOlat** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), **447★**, pushed 2026-10-09 | 🟢 **Apache-2.0 + 2 attribution statements** (payload read, 10 982 B, Apache-2.0 core verbatim) | 🟢 **The richest attachment surface of any permissive LMS here**: QTI assessment, SCORM content, curriculum management, lecture management and course templates are all first-party, so AI attaches to a *standard* inside the platform rather than to a bespoke API. LTI for anything kept at arm's length | 🔴 **Nothing.** This KB has found no AI project targeting OpenOlat — and now that the licence is permissive and the surface is standards-native, 🟢 **this is the cleanest unclaimed platform slot on the page**, especially for a German-speaking-Europe engagement |
| **Mentingo** — [`Selleo/mentingo`](https://github.com/Selleo/mentingo), 92★, pushed **2026-10-10** | 🟢 **MIT** | Not an attachment at all — **the AI is the platform.** Fork it, white-label it, self-host it | 🟢 **It ships its own:** AI mentor, role-play scenarios, compliance/corporate training flows, SCORM and xAPI. Positioned explicitly as a self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX. 🔵 Small and vendor-led (Selleo, Poland), so read it as a **reference architecture and a fork base**, not as a mature platform |
| **Adapt Framework** — [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework), **630★**, pushed **2026-10-10** | 🔴 **GPL-3.0** | A **content authoring** platform rather than an LMS: it produces responsive, accessible, multi-language course packages that emit **SCORM and xAPI**, which any LMS above can then consume | Generation of course structure and items into Adapt's JSON authoring format, then export as a tracked SCORM package. 🔴 **Copyleft matters here in a specific way:** the client *runs* Adapt as a tool and owns the course output, so GPL-3.0 constrains redistribution of Adapt itself and not the courses it authors |

### 🟢 The OpenOLAT `NOASSERTION`, explained — and it is a general lesson

p132 recorded that GitHub's matcher does not recognise OpenOlat's licence and that its own
documentation claims Apache-2.0. **Both were right, and the reason is now measured.** The file is
Apache-2.0 **to the character** through all nine sections of the terms — and then, where
`END OF TERMS AND CONDITIONS` and the boilerplate appendix belong, it carries instead:

> `* * *` *Additional license statement for the original olat.org code base:* … *originally created
> by the OLAT Zentrum at the University of Zurich* … `* * *` *Additional license statement for the
> openolat.org code base:* … *OpenOLAT is initiated by frentix GmbH and is initially based on the
> OLAT 7.1 release.*

🟢 **Consequence for a client engagement: this is a permissive licence.** The grant, the patent
clause and the disclaimer are unmodified Apache-2.0. 🔴 **The obligation is the attribution:** both
statements must be carried into any redistribution, which is an ordinary Apache-2.0 `NOTICE`-style
duty stated in an unusual place.

🔵 **The general lesson, and it applies to every `NOASSERTION` on this page.** A licence matcher
answers *"are these bytes a template I know?"* A client needs the answer to *"what may we ship?"*
Those differ whenever a project appends institutional attribution — which **well-governed,
institution-derived projects are the most likely to do.** 🔴 **So `NOASSERTION` is biased towards
exactly the platforms an education engagement most wants to use**, and that is the second time this
KB has recorded that bias (`P134-F`).

## 🆕 Platforms and platform-adjacent rows added by p136

| platform | licence *(payload-read)* | the attachment point | what exists today |
|---|---|---|---|
| **Brightspace / D2L** — proprietary, **not** open source | n/a (the platform) · 🟢 **MIT** (the connector) | 🟢 **A platform tier this page did not have.** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) (**56★**, 27 forks, pushed **2026-10-11**, published to npm) reads grades, due dates, assignments, announcements, rosters, syllabus and course content over the **Brightspace API** and states it *"works with any school"* | 🟡 **A read connector, individually owned.** Brightspace is the third major commercial LMS after Canvas and Blackboard, and this is the first row this KB has for it. 🔴 **Not source-read this pass** — its write surface is unknown, and D2L publishes no vendor agent programme this pass could find |
| **Lextures** — [`StudyDrift/lextures`](https://github.com/StudyDrift/lextures), **62★**, pushed 2026-10-10 | 🔴 **AGPL-3.0** *(payload, 34 520 B)* | Not an attachment — another **AI-native** platform, self-described as *"the learning environment that adapts"* | 🔴 **The licence is the finding.** AGPL-3.0 means a **hosted** deliverable for a client's students triggers network-copyleft source provision. Compare `Selleo/mentingo` (MIT) for the same architectural slot: 🟢 **when two AI-native platforms sit side by side, the licence decides which one a studio can host** |

### 🔵 A vendor-page caution, measured rather than asserted

This pass re-ran the open-source-platform probe that produced the ERP table above, and **every one
of the ten results came from a single vendor's own domain** (`openeducat.org`, in nine languages).
🔴 **That vendor's pages contradict each other**: its Moodle comparison table marks Moodle as *not*
open source, while another of its own pages describes Moodle as *"GPL PHP"*. 🟢 **Useful facts do
come out of it**, and they are recorded as **vendor self-reported**: the Community Edition is
**LGPLv3**, needs **Python 3.10+** and **PostgreSQL 14+**, and the vendor claims **3M+ users across
90+ countries since 2014**. 🔵 **The lesson for this page is the channel, not the product:** a
query naming a product returns that product's marketing, so the ERP table's weakness is structural
and will not improve by re-running the same query.

## The licence decision, stated plainly

| client intent | platforms that permit it |
|---|---|
| Ship a **closed derivative** the client owns | Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Academico (MIT), Richie (MIT), H5P (MIT) |
| Run a **hosted service** for third parties | Anything, **via LTI or MCP only**. Forking an AGPL platform (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse, ClassroomIO) triggers network-copyleft source release |
| Deepest **in-platform UX**, client keeps the estate | Moodle plugin (GPL-3.0) or Open edX XBlock (Apache-2.0 component in an AGPL host) |
| Touch **no platform source** | LTI 1.3 everywhere — the safe default |

## Declared gaps

- **Eight of the fifteen platforms above have no AI-on-top project at all.** 🟢 **SURVIVES.** The AI
  work has concentrated almost entirely on Canvas (five-plus MCP servers) and Moodle (three plugins
  **plus eight standalone MCP servers, five of them MIT** — p131). Sakai, Chamilo, ILIAS, OpenOLAT,
  Oppia, Kolibri, Frappe LMS and OpenEduCat are open ground. 🆕 **p136 adds a platform to the
  numerator and the denominator at once**: Brightspace/D2L now has a connector (MIT, 56★) and had
  none here before — and it is **proprietary**, so it joins Canvas and Blackboard in the column a
  studio cannot fork.
- ~~**Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to an OSI identifier.**~~
  🟢 **FULLY RESOLVED BY p135 — both halves.** `openeducat_erp` resolves to **LGPL-3.0**, read from
  an 8 241-byte `master/LICENSE` by an earlier pass. 🟢 **`OpenOLAT` resolves to Apache-2.0 with two
  attribution statements replacing the appendix** — payload read this pass, core terms verbatim,
  permissive in effect (see *The OpenOLAT `NOASSERTION`, explained* above). **Rule, now with two
  instances behind it:** `NOASSERTION` means "GitHub's matcher did not recognise the file", never
  "no grant" — and it is **biased towards institution-derived projects**, because they are the ones
  that append attribution.
- ~~**No open-source proctoring or academic-integrity system** was found.~~ 🔴 **REFUTED.** Four
  **MIT** proctoring projects are now on the shelf (`agents/top.md` → academic-integrity tier), one
  of which this KB already held. 🟢 **The surviving gap is grade, not existence:** the largest is
  18★, all four are individually owned, and three do affect-adjacent inference — which is
  **prohibited** in EU education settings under AI Act Art. 5, not merely high-risk. Assessment
  integrity remains the top institutional concern and the shelf still cannot answer it at
  production grade.
- **No AI-on-top for any *open-source* system of record.** 🟢 **NARROWED, and the distinction is
  now the whole point.** p132 found **21 SIS/student-portal agents** (`agents/top.md`), so the
  blanket claim *"no AI-on-top for any system of record"* is **refuted** — but every one of the 21
  connects to a **proprietary or institution-hosted** portal (Librus, EduPage, Pronote, IServ,
  Sisu, uSaint, VTOP, QLDT, VSB, Quercus). 🔴 **The open-source systems of record —
  `openeducat_erp`, `frappe/education`, `academico`, RosarioSIS, Gibbon, openSIS, Fedena — still
  have exactly zero agent coverage between them.** That is the sharper and more useful gap: the
  connector effort has gone to the platforms a studio *cannot* fork, and avoided the ones it can.
- 🆕 **The national K-12 platforms have no sanctioned integration path at all.** Nine proprietary
  platforms (above) with real open connectors and **no LTI, no partner API and no vendor agent
  programme** between them. Every existing connector is an unofficial password-scraper. This is
  simultaneously the clearest unmet need and the clearest compliance hazard on this page.
- 🆕 **p136: the national-platform gap now has a counter-example, and it is 8 000 km from Europe.**
  [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) is a vendor publishing
  a read-only MCP server with **token** auth for its own academy platform — exactly the shape the
  nine national K-12 platforms do not publish. 🔵 It is 0★ and serves one small vendor, so it is a
  **proof that the shape is cheap**, not evidence that the gap is closing.
- 🆕 **This page's licence cells are root-level, and p136 found a root licence hiding a vendored
  third-party grant** (`numbas/Numbas`, Apache-2.0 at the root, an MIT-style `pipwerks` header four
  levels down — `repos/foundations.md`). **None of the platforms on this page has had its vendored
  subtrees read.** For a platform of Moodle's or OpenOlat's size that is a material unknown, not a
  footnote.
