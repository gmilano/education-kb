---
industry: education
region: Global
updated: 2026-10-22
---

# Compose patterns — education

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

---

## Pattern A — Tutor over the client's existing LMS (no fork, no copyleft exposure)

**For:** a client who already runs Moodle or Canvas and wants a tutor that knows the actual course.

**Wiring:**
1. **Expose the LMS.**
   - *Moodle:* install **`webservice_mcp`** from Moodle's own plugin directory (Moodle 4.5–5.2,
     latest release 23 Jul 2026). It serves Moodle's external functions as **MCP tools over
     JSON-RPC 2.0**, gated on the `webservice/mcp:use` capability. Configured inside Moodle — no
     patch to core, so **no GPL obligation reaches your agent**.
   - *Canvas:* [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for courses,
     assignments, submissions, grading, rubrics, students; or the fork
     [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (**MIT**) which adds office-hour
     appointment groups, syllabus read/write, student groups and course-content copy.
   - 🟡 **Grant status, corrected:** the plugin repo
     [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has **no
     root licence file**, but `version.php` carries the full **GPL-3.0-or-later** header Moodle
     requires of every plugin — so it is granted, and GPL is survivable because you reach it over
     JSON-RPC rather than linking to it.
     [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is
     **manifest-only MIT** (`package.json` declares it; the file it names is absent from the tree).
     🔴 **Do not use** [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp): no licence file
     **and** no `license` field in `pyproject.toml` — genuinely no grant to redistribute.
2. **Ground it in the course material.** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
   (**Apache-2.0**) over the course files, with
   [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
   (**Apache-2.0**) for the PDF/DOCX/PPTX/scan reality. If the client has lecture video,
   [opencast/opencast](https://github.com/opencast/opencast) transcripts are the richest corpus
   available and nobody is using them.
3. **Give it pedagogy and memory.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (**Apache-2.0**) for persistent learner memory plus material-grounded tutoring. If the client
   wants explanation *pitched* to the learner's state rather than merely retrieved, look at
   [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) — but it is **GPL-3.0**, so
   run it as a separate service, not as a library inside the deliverable.
4. **Front it.** [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) — SSO,
   per-user quota, provider routing and the **audit log** that gets the build past a data-protection
   officer. (Not `open-webui`: its `LICENSE` is 2,819 B of BSD-3 text **plus** a branding
   restriction and a CLA.)
5. **Prove it.** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   (**MIT**) with [MMLU](https://github.com/hendrycks/test) (**MIT**) and
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**), scored on the client's own
   subject mix, before and after.

**Licence posture:** client-owned code is MIT/Apache/BSD throughout. The only copyleft component is
the LMS itself, reached over a published protocol. **Deliverable stays closed if the client wants it
closed.**

---

## Pattern B — Autograding that assesses the approach, not just the output

**For:** CS, data-science and engineering programmes drowning in submissions.

**Wiring:** [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (**BSD-3**) for
identical per-cohort compute → [jupyter/nbgrader](https://github.com/jupyter/nbgrader)
(**BSD-3**) for the release/collect/autograde/return lifecycle →
[ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) (**BSD-3**, default ref
`master`) for container-isolated grading at cohort scale →
[microsoft/pybryt](https://github.com/microsoft/pybryt) (**MIT**) to check **how** the student got
there, not only whether the answer matched →
[jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) (**BSD-3**) so the LLM explains
*why* the approach was wrong, inside the notebook the student is already in.

**Why this combination:** pybryt is the piece everyone misses. An LLM that reviews output rewards
the student who guessed; pybryt's annotations let you detect the *intended method* and then have the
model give feedback on the method. **Fully permissive — BSD-3 and MIT only, zero copyleft.**

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer.

---

## Pattern C — Citation-grounded academic assistant (and the EU compliance story that comes free)

**For:** higher-ed research support, library services, graduate programmes.

**Wiring:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa) (**Apache-2.0**) as
the answer engine → [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar)
(**Apache-2.0**) or [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib)
(**Apache-2.0**) for multi-paper synthesis →
[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) (**Apache-2.0**)
for ingest → [LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) as the campus gateway.
For guided-inquiry assignments, [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
(**Apache-2.0**) as the student-facing research scaffold.

**The compliance argument:** paper-qa **declines to answer** without retrieved evidence. Under
**EU AI Act Art. 50** (transparency, live from **2 Aug 2026** — *not* delayed by Regulation (EU)
2026/1744) a system that cites its sources and refuses otherwise is dramatically easier to document
than one that generates fluently. Build the refusal behaviour in, then point at it in the
conformity file. **Fully Apache-2.0/MIT.**

---

## Pattern D — Offline-first deployment for connectivity-constrained regions

**For:** LATAM, African and rural APAC deployments — including the nine countries in the Google.org
AI-literacy rollout (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
Peru, Uruguay).

**Wiring:** [learningequality/kolibri](https://github.com/learningequality/kolibri) (**MIT**,
default ref 🔴 `develop`) as the edge runtime — offline-first by design, not a degraded mode →
a small local model on the same device for the tutoring loop →
[FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for scheduling review, because
retention is the one outcome measurable without a network →
content authored in [H5P](https://github.com/h5p/h5p-php-library) — 🟡 **GPL-3.0, keep it as
runtime content, not linked code** → periodic sync to the central LMS over
[LTI 1.3](https://github.com/1EdTech/lti-1-3-php-library) (**Apache-2.0**) when a link is available.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

---

## Pattern E — Sovereign EMEA public-sector stack

**For:** European public-sector clients demanding both data sovereignty and code ownership.

**Wiring:** **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, default ref `master`)**
as the platform — **the only major open-source LMS a studio can extend with closed code** →
[serlo/serlo.org](https://github.com/serlo/serlo.org) (**Apache-2.0**) or
[oppia/oppia](https://github.com/oppia/oppia) (**Apache-2.0**, default ref `develop`) for structured
content → [openfun/richie](https://github.com/openfun/richie) (**MIT**, default ref `master`) as the
public catalogue → permissive agents over LTI 1.3 → all EU-hosted.

**The alternative, when the client insists on the openDesk lineage:** **ILIAS (GPL-3.0, default ref
`release_11`) + OpenProject behind a single SSO** — the ZenDiS pattern, and ZenDiS co-develops with
France's DINUM (LaSuite). 🔴 **But do not quote "8,600 schools":** that figure traces to a single
news item, and this pass found **no school deployment of openDesk in any source**. Named users are
administrative bodies. Sell the architecture, not the number.

**Dated compliance roadmap to attach to the bid** — this is the part competitors get wrong:
| obligation | when | status |
|---|---|---|
| Art. 4 AI literacy (every organisation using AI) | **since 2 Feb 2025** | 🔴 already binding |
| Emotion recognition in education | **prohibited since 2 Feb 2025** | 🔴 design it out |
| Art. 50 transparency | **from 2 Aug 2026** | 🔴 **not delayed** |
| Stand-alone high-risk education systems (admissions, assessment, proctoring, AI-detection in assessment, path-steering personalisation) | **2 Aug 2026 → 2 Dec 2027** per **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) | 🟢 14 months of runway |

---

## Pattern F — Teacher-facing instructional assistant (the pattern the market and the regulator agree on)

**For:** LATAM and ANZ especially, where student-facing generative AI is either commercially
unproven or politically restricted.

**Wiring:** [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) for lesson plans,
quizzes and question banks → [openedx/edx-ora2](https://github.com/openedx/edx-ora2)
(**AGPL-3.0**, run as the platform's own service) for rubric-based open-response assessment with
the human grade-of-record → [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (**MIT**) so the
prompt pipeline has a metric attached instead of being hand-tuned →
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (**LGPL-3.0**, default ref
🔴 `19.0`) where the administrative record has to move too.

**Why it sells:** HolonIQ's 2026 LATAM EdTech 100 finds regional AI concentrated in **teacher-facing
instructional tools rather than consumer tutoring**; Brazil's PL 2.338/2023 reportedly targets
**student selection**; DC bans AI in grading, discipline, IEP and teacher evaluation; ANZ shows the
highest ban support in the Ipsos 2026 data. **Teacher-facing-only must be an architectural switch,
not a retrofit.**

---

## Pattern G — Provenance and labelling in the generation path (APAC, overdue)

**For:** anything shipped into **India** (amended IT Rules: prominent labels **and provenance
markers** on AI-generated content from **20 Feb 2026**) or **China** (AI-content labelling measures
applicable from **1 Sep 2025**; 988 services filed by 30 Jun 2026).

**Wiring:** label and sign **at generation**, not at display — every artefact an education agent
emits (generated question, feedback text, summary, image) carries a label and a provenance record
from the moment it is created; the LMS stores the record alongside the artefact (Moodle web services
/ MCP, Canvas API) so an audit can reconstruct what was machine-made months later; the student-facing
surface renders the label rather than deriving it.

**Why it is a build, not a memo:** if labelling happens in the UI, every export, API call and
copy-paste strips it. The requirement is on the content, so the marker belongs in the content
record. Most tutoring products shipped into IN/CN today do not do this and are already out of time.

---

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified this pass are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`. A `main`-assuming read reports
   "no licence" for every one of them, and that false negative looks exactly like a real one.
2. **Probe more than one path.** Seven paths, in order: `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
   `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`. Verified instances where the grant is *not* at
   `LICENSE`: **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Treat "no licence" as a hard stop, not a formality.** Three live, functional, actively
   advertised repositories verified this pass have **no grant at any of the seven paths**:
   `loyaniu/moodle-mcp` and `Seechange-edu/act-ai-tutor-backend`. No grant means no right to
   redistribute, whatever the README invites you to do.
8. **But read the manifest and the source headers before you call it ungranted.** 🔴 **This pass's
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json` and the main source file's header
   before rejecting a repository; a file-only read would have wrongly rejected three of five,
   including the plugin Moodle's own directory distributes.
6. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
7. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.
