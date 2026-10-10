---
industry: education
region: Global
updated: 2026-10-10
---

# Education — foundational repos

**Pass 92, 2026-10-10.** ⏱️ **Second pass of this date.** Resolved with
`compose/code/grant-ladder-v4/ladder.sh`: existence by `git ls-remote --symref`, **licence read from
the payload** pinned to the resolved SHA, **24 candidate filenames at a 1-byte floor** — and, the
change that matters this pass, **classified by the shared `compose/code/lib/license_family.sh`
instead of a classifier of the instrument's own** (`P237`). Two-sided control passed:
`moodle/moodle` → `COPYING.txt` **35 147 B** (tenth reproduction), two invented slugs `ABSENT`.
`—` in ★ means not read this pass.

🔴 **One row on this page was WRONG for a pass, and it was the licence row of a platform.**
[`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) was published here as *"**LGPL-3.0** ·
18 025 B — **LGPL: linkable**"*. **Its payload's title block reads `GNU GENERAL PUBLIC LICENSE,
Version 2, June 1991`. It is GPL-2.0, and GPL-2.0 is not linkable that way.** 🔵 **And this KB
already knew**: `repos/trending.md` recorded *"the row that decides a project: `oat-sa/tao-core` is
GPL-2.0"* in an earlier pass, derived by reusing the shared classifier. Pass 91 re-derived it with a
forked classifier and regressed it. 🟢 Corrected below, mechanism in
`compose/code/grant-ladder-v4/README.md` (`P960`), and the check that catches the class in
`compose/code/p963-shelf-licence-agreement/`.

A *foundation* here is a repo a studio can standardise on **across clients**, independent of which LMS any one
client runs. The useful property of this tier is that it sits on spec boundaries (SCORM, xAPI, cmi5, QTI,
Open Badges, LTI), and spec-boundary code is permissive far more often than product code.

## Tier 1 — content and learner-data interoperability

This is the tier to own. Every education engagement eventually has to move content *into* a platform the client
already runs and get learner data *out* of it.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** · 1 072 B · `master` · `882f3b8` | 354 | 🔵 unplaced | The runtime shim. SCORM 1.2 / 2004 API surface for any content in any LMS. |
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | **Apache-2.0** · 11 324 B · `master` · `ea17c40` | 42 | **North America** (US DoD / ADL) | The authoritative SCORM → xAPI statement mapping. The audit-trail spec. |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** · 11 357 B · `master` · `efa045e` | — | **North America** (US DoD / ADL) | Reference Learning Record Store — the canonical implementation to test against. |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` | — | **North America** (Yet Analytics, US) | **A production SQL LRS.** Apache-2.0 and backed by a real database — this is the one to deploy, where `ADL_LRS` is the one to conform to. |
| [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | **MIT** · 1 077 B · `master` · `b5ac7dd` | — | 🟡 **EMEA** (Tunapanda, Kenya lineage) | 🟢 **The MIT escape hatch from H5P's GPL core.** Plays H5P content with no LMS and no GPL server-side library. |
| [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | 🟡 **LGPL-3.0** · 7 651 B · `master` · `1f47c93` | — | **EMEA** (UK) | LTI 1.3 tool provider. 🟡 LGPL — link, do not fork into a closed binary. |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** · 13 185 B · `develop` · `0a66b52` | — | **North America** (1EdTech) | Open Badges validation. The credentialing tier's conformance gate. |
| 🆕 [`edly-io/pxc`](https://github.com/edly-io/pxc) | **Apache-2.0** · 11 358 B · `main` · `01114d3` | 9 | 🔵 unplaced (publisher is the Open edX commercial vendor **edly.io**) | 🟢 **Watch this one.** A **proposed standard for learning activities explicitly intended to replace SCORM, H5P *and* LTI** — the three specs this entire tier is built on — published permissively by the vendor that packages Open edX. 🔵 **Nine stars and strategically larger than anything else on this page.** Not a dependency yet; a reason to keep the interop layer behind an interface you own. |

## Tier 2 — assessment and automated feedback

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` | 215 | **EMEA** (Newcastle University, UK) | Browser-native e-assessment with real mathematics; SCORM-packageable. The strongest permissive assessment engine on this shelf. |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | **BSD** · `LICENSE.md` 1 542 B · `main` · `80d7d66` | — | **North America** (RPI, US) | Full course-management + autograding platform, **BSD**. Permissive and production — rare in this tier. |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | **BSD** · 1 560 B · `master` · `190c1a4` | — | **North America** (UC Berkeley, US) | Notebook autograding; the standard in data-science teaching. |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD** · 1 512 B · `main` · `f9915da` | — | **North America** (Project Jupyter) | Assignment release/collect/grade for notebooks. |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | **Apache-2.0** · 11 357 B · `main` · `04bee3e` | — | 🔵 unplaced | Rubric-driven autograding with report generation; release 0.4.0 (May 2026). |

## 🆕 Tier 2b — the learner model — **`Gap 335` discharged after eight passes untouched**

🔴 **`Gap 335` (knowledge tracing) was the oldest untouched item on this shelf**, named openly in
`agents/top.md` for eight passes: *"only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma)
carry an explicit learner model. Everything else relies on the context window, which is not a mastery
estimate."* 🟢 **The canonical library exists, it is MIT, and it was found on the first query that
named the technique instead of the industry** — `P955` holding for a second pass running.

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| 🆕 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | ~430 | 🔵 unplaced | 🟢 **The reference deep-knowledge-tracing benchmark library** (NeurIPS 2022 datasets-and-benchmarks track, `pykt.org`). Standardised preprocessing plus a model zoo — **DKT, DKVMN, SAKT, SAINT, AKT, GKT, LPKT** — over 7 datasets. 🔵 **This is the missing layer, not another tutor:** it turns "the agent remembers the conversation" into **a per-skill mastery estimate you can threshold on**, which is what adaptive sequencing and mastery-gated progression actually need. MIT, so it can sit inside a paid deliverable. |
| 🆕 [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) | **MIT** · 1 065 B · `main` · `2bef7e9` | — | 🔵 unplaced | 🔴 **Name collision, and the weaker of the two.** A separate PyTorch reference implementation whose own README warns *"not all the implemented models have achieved comparable performance to that of the original implementations"*. 🔵 **Read it as a reference, never as the benchmark** — and note it is reachable by the same search string as the row above. |

🔴 **And the third candidate carries no grant:**
[`weiwei1392/knowledge-tracing`](https://github.com/weiwei1392/knowledge-tracing) → **no licence
payload in 24 filenames** · `main` · `136efef`.

🆕 🔵 **`P968` — two repos sharing a project name is a licence-and-quality trap, not a trivia item.**
`pykt-team/pykt-toolkit` and `JonathanSilver/pyKT` are both MIT, so a licence probe cannot separate
them; only reading the README does. This is the same shape as `Gap 368`'s acronym collision on
`topics/lms` (**LMS = Least Mean Squares**, **LMS = Library Management System**) — 🔵 **in this
industry, name collision is a recurring property of the search space, so the canonical slug belongs
in the shelf row and not just the project name.**

## Tier 3 — delivery, runtime and agent substrate

| repo | grant (payload · bytes · ref · SHA) | ★ | region | role in a build |
|---|---|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · 1 097 B · `develop` · `d4fea9c` | — | **North America** (Learning Equality, US) | **Offline-first learning delivery.** MIT. The correct substrate wherever connectivity is the binding constraint — which, per UNESCO, is most of APAC's and LATAM's deployment reality, not an edge case. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · 11 358 B · `develop` · `ad22e91` | — | **North America** (Oppia Foundation) | Structured, explanation-driven interactive lessons; a real pedagogy model in code. |
| [`oppia/oppia-android`](https://github.com/oppia/oppia-android) | **Apache-2.0** · 11 357 B · `develop` · `25e3860` | — | **North America** | The offline Android client for the above. |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD** · 1 475 B · `main` · `f02ec3c` | — | 🔵 unplaced | Multi-tenant notebook serving — the per-learner compute boundary. |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` | — | **North America** | Stateful agent orchestration. The graph, not the agent. |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · 11 357 B · `main` · `96f33fa` | — | **EMEA** (Hugging Face, FR lineage) | Minimal agent loop; the low-ceremony option when LangGraph is too much machinery. |
| [`huggingface/agents-course`](https://github.com/huggingface/agents-course) | **Apache-2.0** · 11 357 B · `main` · `3c469e7` | — | **EMEA** | 🟢 The permissive **teaching** counterpart to `smolagents` — see the AI-literacy tier in `agents/top.md`. |

## Licence flags in this tier — the traps

| repo | grant | why it matters |
|---|---|---|
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `LICENSE.txt` 35 146 B · `master` · `cb64a1f` | 🔴 **H5P's core is GPL.** The interactive-content ecosystem everyone reaches for is copyleft at the library level. Use `tunapanda/h5p-standalone` (MIT) for playback instead of linking this. |
| [`lumieducation/H5P-Nodejs-library`](https://github.com/lumieducation/H5P-Nodejs-library) | 🔴 **GPL-3.0** · 35 146 B · `master` · `ac2d6aa` | 🔴 The Node port is GPL too. There is no permissive H5P *authoring* server. |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** · 35 141 B · `master` · `5fec948` | 🔴 The best-known LRS is GPL. `yetanalytics/lrsql` (Apache-2.0) is the permissive substitute, and it is the better-maintained one. |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **AGPL-3.0** · 36 983 B · `master` · `d1e44b4` | 🔴 Excellent adaptive-assessment engine (UIUC), AGPL — network copyleft, so hosting it for a client triggers reciprocity. |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · 34 764 B · `main` · `8f90cc8` | 🔴 UCLouvain autograder, AGPL. |
| [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | 🔴 **GPL-3.0** · `LICENSE.md` 35 191 B · `master` · `3be3278` | 🔴 |
| [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0** · 35 147 B · `main` · `61b5d8f` | 🔴 The LMS-integrated accessibility checker. GPL, and not AI-driven. 🆕 **But it is no longer the only option** — three permissive AI WCAG checkers are now shelved in `agents/top.md`. |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 **GPL-2.0** · 18 025 B · `develop` · `d9d462a` | 🔴 **CORRECTED this pass — it was published here as "LGPL-3.0 · linkable" and it is not.** TAO (Open Assessment Technologies, Luxembourg) is the serious QTI assessment platform and **the most mature one in this inventory**, so this is the row most likely to be costed. **GPL-2.0 is full copyleft: a fork shipped to a client carries reciprocity, and there is no LGPL linking exception to rely on.** Integrate across a process or network boundary, or budget for the obligation. 🔵 Also **GPL-2.0-only** — one-way incompatible with GPL-3.0 code. |

## 🆕 ADL leaves its own specs ungranted — now measured at three of five

🔴 **The US DoD's Advanced Distributed Learning initiative *authored* SCORM. Three of its repos carry no
licence payload in 24 filenames, while two carry Apache-2.0.** This was one row in pass 89's `Gap 354`; it is
now a pattern inside a single publisher:

| ADL repo | grant | ★ |
|---|---|---|
| [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) | 🟢 **Apache-2.0** · 11 324 B | 42 |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** · 11 357 B | — |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **no payload / 24** · `master` · `3e532b8` | 99 |
| 🆕 [`adlnet/SCORM-2004-4ed-Test-Suite`](https://github.com/adlnet/SCORM-2004-4ed-Test-Suite) | 🔴 **no payload / 24** · `master` · `050f1b4` | 18 |
| 🆕 [`adlnet/SCORM-to-TLA-Roadmap`](https://github.com/adlnet/SCORM-to-TLA-Roadmap) | 🔴 **no payload / 24** · `master` · `da1b9a2` | 7 |

🔵 **Why this is worth a table.** Pass 89 read the single `SCORM-to-xAPI-Wrapper` negative as *"one missing
file, not a policy"*, on the reasoning that its Apache-2.0 sibling proved intent. 🔴 **Three of five says the
opposite: inside this publisher, grants are applied to the *profile and the server* and omitted from the
*wrapper, the conformance test suite and the roadmap*.** The omission tracks a category — reference
implementations and documents — not an oversight. 🔴 **Practical effect: the official SCORM 2004 conformance
test suite cannot be redistributed in a client deliverable.** Conformance must be demonstrated against
`ADL_LRS` (Apache-2.0) instead, which is what `P91-B` does.

## Other no-grant rows in this tier

| repo | status |
|---|---|
| [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) | 🔴 **No payload / 24** · `develop` · `04c4bc2`. The *specification* carries no grant while the *validator* is Apache-2.0. Cite the validator. |
| [`eecs-autograder/autograder.io`](https://github.com/eecs-autograder/autograder.io) | 🔴 **No payload / 24** · `master` · `5af4960`. 🔵 Consistent with its own README — a docs/issue tracker, not the code. Not a defect, but not a dependency either. |

## Slugs that do not exist

🔴 Re-confirmed `ABSENT` this pass. Recorded so they are not re-tried:

- `apereo/opencast` → 🟢 the real slug is [`opencast/opencast`](https://github.com/opencast/opencast)
- `tutor-dev/tutor` → 🟢 the real slug is [`overhangio/tutor`](https://github.com/overhangio/tutor)
- `h5p/h5p-standalone` → 🟢 the real slug is [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone)

## Count, stated plainly

**22 foundational rows above the flag line; 21 of them permissive (MIT / Apache-2.0 / BSD), 1 LGPL.**
The interoperability, assessment and learner-model tiers really are the permissive heart of this
industry — that finding survives a fourth measurement, on a larger sample and a **repaired** instrument.

🔴 **One honest subtraction from last pass's count.** Pass 91 reported *"19 of 20 permissive, 1 LGPL"*.
That line was true of the page as it stood **only because `oat-sa/tao-core` was misfiled as LGPL-3.0**;
it sits below the flag line either way, so the headline count is unchanged by the correction — but the
LGPL row it referred to is `celtic-project/LTI-PHP`, and **`tao-core` was never one of the 20.** Stated
rather than silently re-tallied.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
