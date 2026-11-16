---
industry: education
region: Global
updated: 2026-11-16
---

## 🟢 Pattern (`p845`, `2026-11-16`) — **"Sequence the upskilling engagement by measured completeness, not by star count"**

🔵 **The problem this solves.** A Globant workforce-upskilling engagement on AI infrastructure
needs courseware the studio can relicense into a client deliverable. The obvious sourcing move —
rank the candidate repositories by stars, adopt the top ones, author the rest — 🔴 **is wrong in
this category, and `p845` measured how wrong.**

### The recipe

**1. Take the estate, not the repository.** One query enumerates it:

```
https://api.github.com/search/repositories?q=user:ai-infra-curriculum&per_page=100
```

🟢 **Returns `28` repositories, `26` of them `MIT`** — `14` role tracks each published as a
`-learning` / `-solutions` PAIR. 🔵 **The pair split is what makes it teachable by someone other
than its author: hand the learner one, keep the answer key.**

**2. Read each track's published completeness metadata, NOT its stars.**

```
https://raw.githubusercontent.com/ai-infra-curriculum/ai-infra-<ROLE>-learning/main/COMPLETENESS_MATRIX.md
```

🟢 **`13` fetches, no authentication, no rate limit.** Parse the `Learning` row.
🔴 **Ignore `Overall` — it is contaminated by the `Solutions` column (see step 4).**

**3. Sequence the engagement from the measured table.**

| Engagement need | Take | Measured state |
|---|---|---|
| IC onboarding, levels `10`–`45` | `junior-engineer` → `engineer` → `senior-engineer` → `architect` | 🟢 `100%` learning, full exercise sets |
| Specialist tracks | `mlops`, `ml-platform`, `performance` | 🟢 `100%` learning |
| 🟢 **Reliability for model-backed services** | `sre-learning` | 🟢 `14/14` modules, `353,078` words, `0★` |
| 🟢 **Inference serving** | `inference-engineer-learning` | 🟢 `14/14` modules, `0★` |
| Leadership, levels `40`–`60` | `team-lead`, `principal-engineer`, `principal-architect` | 🔴 **Lessons are skeletons** — 🟢 **but take `projects/`: `59k`–`74k` words of reference architectures, step-by-step walkthroughs and rubrics** |
| 🔴 Level `55` | `senior-architect` | 🔴 **The one genuinely thin track — `~21k` words across both halves. Budget authoring here, and ONLY here.** |

**4. Apply the two corrections `p845` established, or the plan misprices.**

🔴 **Correction A — `Overall %` inverts the ranking at the top of the ladder.** It reports
`senior-architect` at `55%` and `principal-architect`, `principal-engineer` and `team-lead` at
`50%`. 🟢 **Measured, the three "`50%`" tracks carry `59k`–`74k` words of capstone material and
`senior-architect` carries `~21k`.** 🔴 **Sequencing on `Overall %` sends the authoring budget to
the three tracks that need it least.**

🔴 **Correction B — `Solutions 100%` can mean a `58`-word pointer.** Verify before promising an
answer key:

```
git clone --depth 1 https://github.com/ai-infra-curriculum/ai-infra-<ROLE>-solutions
find . -name '*.md' -exec wc -w {} + | sort -n | head -20
```

🟢 **A real solution set looks like `ai-infra-sre-solutions`. A stub set looks like
`ai-infra-senior-architect-solutions`: `71` files, `6,170` words, `61` under `200` words.**

**5. Wire the learning path in front of it.** 🟢 **Pair with
[`WenyuChiou/awesome-agentic-ai-zh`](https://github.com/WenyuChiou/awesome-agentic-ai-zh) (`MIT`,
trilingual) for the reading sequence** — it supplies the order, the estate supplies the exercises —
🟢 **and deliver through the permissive LMS tier (`OpenOLAT`, `frappe/lms`), never through the
`GPL`/`AGPL` tier, so the client deliverable stays closed.**

### 🟢 Why this composes

🔵 **Licence coherence end to end:** estate `MIT` (`1,085 B` grant, byte-read), reading path `MIT`,
LMS `Apache-2.0` or `MIT`. 🟢 **No copyleft anywhere on the path, so the assembled curriculum can
be relicensed into a closed client deliverable with attribution only.** 🔴 **Keep `LearnHarness`
(`AGPL-3.0`) and `RosarioSIS` (`GPL-2.0`) off it — they are demand signals, not build inputs.**

## 🟢 Forty-ninth pass (`p844`, 2026-11-16) — `1` recipe (`P96`), and it is `P90` taken from one country to four with the licence boundary drawn where it actually falls

## 🟢 `P96` — THE LATAM NATIONAL EDUCATION DATA SPINE: build the evidence layer a ministry engagement is judged on, and know which country's data you may not keep (forty-ninth pass, `p844`, LATAM)

🔵 **The problem.** A LATAM education engagement is won on evidence — enrolment,
outcomes, equity gaps, school-level trajectories — and every ministry already
publishes it. 🔴 **`P90` could only do this for Chile.** 🔴 **And the naive move —
treat "open government data" as one licence — is wrong in a way that surfaces at
delivery, when a client asks whether the derived dataset can ship inside their
product.**

### 🟢 The wiring

1. **Ingest — Brazil first, because it is the only layer with a maintained SDK.**
   [`basedosdados/sdk`](https://github.com/basedosdados/sdk) (`MIT`, `433★`,
   pushed `2026-07-24`). Python / R / Stata over a BigQuery datalake with INEP
   tables already cleaned and keyed (`br_inep_ideb.municipio` and siblings).
   🔵 **You are not writing a Censo Escolar parser; you are writing queries.**
2. **Shape — steal the table shapes rather than rediscover them.**
   [`sidneisj/censo-escolar-bi-analytics`](https://github.com/sidneisj/censo-escolar-bi-analytics)
   (`MIT`) for the Censo Escolar BI model;
   [`triverao/saber11-brechas-educativas`](https://github.com/triverao/saber11-brechas-educativas)
   (`MIT`) for the Colombian equity-gap model. 🔵 Both are small and
   single-maintainer — read them, do not depend on them.
3. **Gate — the licence check runs ON THE DATA, per country, before ingestion.**
   🔴 This is the step that does not exist in `P90` and is the whole reason `P96`
   is a separate recipe.

| Country | Data licence | 🟢 May a DERIVED dataset ship closed? |
|---|---|---|
| 🇨🇱 Chile | `CC BY 3.0 CL` | 🟢 **Yes** — credit MINEDUC |
| 🇧🇷 Brazil | `CC BY` (INEP via `dados.gov.br`) | 🟢 **Yes** — credit INEP |
| 🇲🇽 Mexico | Términos de Libre Uso MX | 🟢 **Yes** — cite the source |
| 🇨🇴 Colombia | 🔴 **`CC BY-SA 4.0`** (ICFES Saber 11 / Saber Pro) | 🔴 **NO.** The derived dataset inherits `CC BY-SA 4.0` |
| 🇦🇷 Argentina | 🔴 `CC BY 2.5 AR` at SITE level only | 🔴 **Unknown — read the dataset's own licence field first** |

4. **Partition on that table.** 🟢 **Keep the Colombian derivation in its own
   artefact, published `CC BY-SA 4.0`, and join to it at query time** — the
   proprietary application code stays proprietary, because share-alike here binds
   the DATA, not the software that reads it. 🔴 **Do not blend ICFES-derived rows
   into a combined regional table you intend to keep closed: the blend inherits
   the strongest obligation in it.**
5. **Trademark, separately from licence.** 🔴 ICFES requires express authorisation
   for use of its **marks**. 🔵 Licence-clean data can still be brand-encumbered;
   name the institution in prose, do not put its logo in the product.

### 🔵 How to sell it

🟢 **The deliverable is a ministry-grade evidence layer with its rights position
written down per country** — which is the artefact a public buyer's legal review
asks for and which, on the evidence of this base, almost nobody brings.
🔴 **Scope Argentina as a licence READ before it is scoped as engineering**: the
Aprender assessment has no open-source wrapper on this channel at all (`p844`
searched and returned zero), so Argentina is greenfield in both senses.

🔴 **Known limit, stated up front:** all five licence determinations are
`CITED, NOT READ` — the national portals that would confirm them are unreachable
from this session (`T148`). 🟢 **Re-read each dataset's licence field from the
portal before contract, and treat this table as the thing you are verifying, not
the thing you are relying on.**

## 🟢 Forty-eighth pass (`p843`, 2026-11-16) — `1` recipe (`P95`), runnable, tested against a 6-repo fixture and then run over `482` real shelf rows this pass

## 🟢 `P95` — THE FIRST-PARTY METADATA SWEEP: stop quoting the shelf and start measuring it (forty-eighth pass, `p843`, Global)

🔵 **Why this exists.** `P94` gates a candidate at intake. 🔴 **Nothing on this
base gated a row after intake**, and `p843` found out what that costs: two
build-safe rows had ceased to exist, six foundations had been archived
upstream, thirty-nine had not been pushed to in six months, three licence
claims had never been byte-read, and every star count in `repos/trending.md`
was a third-party figure the previous pass explicitly marked unverified — all
three of them wrong, all three low, one by `6,781★`.

🟢 **Code, tested, in this repository:**
[`compose/code/p95-first-party-sweep/`](code/p95-first-party-sweep/) —
`sweep.sh` (stage 1), `grant-bytes.sh` (stage 2), `fixture-repos.txt`,
`fixture-expected.tsv` and a README. Stage 1 exits `0` when every input
resolved, stage 2 exits `1` when any repository has no grant payload, so both
drop into CI unchanged.

```bash
./sweep.sh repos.txt out.tsv          # licence, stars, forks, last push, liveness
./grant-bytes.sh owner/repo [...]     # byte-read whatever stage 1 left unclassified
```

### 🟢 The wiring — why this works here at all

🔴 **The two obvious channels are both closed in this environment**, which is
why forty-seven passes did without:

| Channel | Result, measured 2026-11-16 |
|---|---|
| `gh api repos/{owner}/{repo}` | 🔴 `403` — the session credential is scoped to attached repositories |
| `github.com/<owner>/<repo>` (HTML) | 🔴 `403` through the proxy (`T124`) |
| `huggingface.co`, `arxiv.org`, `aclanthology.org` | 🔴 do not resolve (`curl` exit `56`) |
| **`gh api search/repositories`** | 🟢 **`200` for any public repo, full metadata** |
| **`raw.githubusercontent.com`** | 🟢 `200`/`404` — a real answer |

🟢 **Stage 1** batches ten `repo:` qualifiers per search query as an OR and
reads `license.spdx_id`, `stargazers_count`, `forks_count`, `pushed_at`,
`archived` and `fork`. Three details are not optional, each learned by getting
it wrong first:

1. 🔴 **`fork:true` must be in the query.** GitHub search excludes forks by
   default, so a maintained fork is indistinguishable from a deleted
   repository. Two foundation rows —
   `packbackbooks/lti-1-3-php-library` (Apache-2.0, 54★, pushed 2026-11-13) and
   `tl-its-umich-edu/caliper-php-public` (LGPL-3.0) — were nearly recorded as
   dead for exactly this reason.
2. 🔴 **A batch containing one non-existent repository returns `422` for all
   ten.** The script falls back to one-at-a-time on failure rather than losing
   the batch.
3. 🔴 **Absence from the search index is NOT proof of deletion.**
   `digitalcredentials/learner-credential-wallet` answers `422` even with
   `fork:true`, yet `git ls-remote` resolves it (`HEAD 1c46a82ba384`) and raw
   serves its README. Stage 1 therefore adjudicates every absence with
   `git ls-remote` and prints 🔴 `GONE` or 🟡 `UNINDEXED`, never one for the
   other.

🟢 **Stage 2** byte-reads the grant for everything stage 1 left as
`NOASSERTION` or `NONE`, over 7 filenames × 2 branches via raw, reporting
bytes, `sha256₁₂` and title line — and flags any Apache-asserting file under
`5,000 B` as **`BOILERPLATE-ONLY`** (`T145`), because the full Apache-2.0 text
is `11,357 B` and a `738 B` file is a grant by *reference*, not by text.

### 🟢 What it produced this pass, on this base

| Shelf | Rows swept | Dead | Archived | No push in 6 months | Licence claims corrected or newly evidenced |
|---|---|---|---|---|---|
| `agents/top.md` build-safe | `275` | 🔴 **`2`** | 0 | `21` | 🟢 `3` byte-read for the first time |
| `repos/foundations.md` | `207` | 🟢 **`0`** | 🔴 **`6`** | `39` | — |

🔴 **The single most actionable output**: [`frappe/mcp`](https://github.com/frappe/mcp)
— MIT, 171★, Frappe's own MCP server for the ERPNext stack, the cleanest
example this base had of a *permissive agent seam into a copyleft
administrative core* — **was archived upstream on 2026-10-27** and no row said
so. 🟢 The licence permits a fork, and that is now the recommendation.

🟢 **Evidence:**
[`evidence/first-party-sweep.2026-11-16-p843.tsv`](../evidence/first-party-sweep.2026-11-16-p843.tsv) (273 rows),
[`evidence/foundations-sweep.2026-11-16-p843.tsv`](../evidence/foundations-sweep.2026-11-16-p843.tsv) (206 rows),
[`evidence/grant-bytes.2026-11-16-p843.tsv`](../evidence/grant-bytes.2026-11-16-p843.tsv).

### 🔵 How to sell it

🟢 **A client running an open-source stack has exactly this rot and no
instrument for it.** The engagement is two weeks, not two months: point stage 1
at the dependency manifest, adjudicate the absences, byte-read the
unclassified grants, and hand back a table with four columns a procurement
team can act on — *does it exist, who granted what, is anyone maintaining it,
and what cannot be redistributed*. 🔵 The last column is the one that surprises
people: `wwrwbs/AI_AWE` looks like a single Apache-2.0 asset and is in fact
five grants, one of which — the `Persuade 2.0` corpus — **cannot ship**.

🟢 **Composes with `P94`**, which gates intake. `P94` is the door; `P95` is the
annual inspection. 🔴 **A shelf with only the first is a shelf that decays
silently**, and this one did, for forty-seven passes.

## 🟢 Forty-seventh pass (`p842`, 2026-11-16) — `1` recipe (`P94`), runnable and tested against a `5`-repo fixture corpus this pass measured

## 🟢 `P94` — THE LICENCE-AND-SUBSTANCE INTAKE GATE: reject the candidate that cannot be built on, before it becomes a row (forty-seventh pass, `p842`, Global; EMEA audit note)

🔵 **Why this exists.** `p842` surfaced `3` education repositories genuinely absent from this base's
`5,720`-URL shelf. All three were live. All three were active. **None could be used, and each failed
for a different reason** (`T143`). A pass without this gate would have written three rows, two of
them carrying an **invented** licence — the most load-bearing field a client decision rests on.

🟢 **Code, tested, in this repository:**
[`compose/code/p94-licence-substance-gate/`](code/p94-licence-substance-gate/) — `intake-gate.sh`
plus the fixture corpus and expected output. Exit `0` = all pass, exit `1` = at least one reject, so
it drops into CI unchanged.

```bash
./intake-gate.sh owner/repo [owner/repo ...]
```

### 🟢 The wiring — three gates, in order, short-circuiting

**Gate 1 — liveness, and the REAL ref.** `git ls-remote --symref https://github.com/$repo HEAD`.
🔴 **Do not use `curl -sI`: this session's proxy returns `403` for live repositories** (`T124`), so
an HTTP status tells you nothing. The symref's second job is the one that actually bites: it yields
the **true default branch**.

**Gate 2 — the grant, byte-read at that ref.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`,
`COPYING.txt`, `LICENCE` from `raw.githubusercontent.com/$repo/$branch/`, recording **byte count and
`sha256₁₂`**. 🔴 **Never infer a licence from a badge, a topic tag, an aggregator column or README
prose.** 🔴 **No licence file is all-rights-reserved, not permissive** — the mode that disqualified
two of this pass's three candidates.

**Gate 3 — substance.** `git clone --depth 1` and inventory file types; **reject on `0` executable
source files**. 🔵 This is the gate the base did not have. `thinkmoon/zhihui-teacher` carries a
genuine `MIT` grant (`1,066` bytes, `sha256₁₂` `e936c2bc0ff4`) over a **static marketing site** for a
closed hosted product — `index.html`, `styles.css`, five `mp4`s, no code — and its own `NOTICE.md`
says the product's front- and back-end code is not in the repository. **It passes gates 1 and 2
cleanly.**

### 🟢 Reproduce this exactly — fixture corpus measured `2026-11-16`

| Candidate | Result | Detail |
|---|---|---|
| `Ali627miya/gradeguide-ai` | 🔴 `REJECT gate2-grant` | `main@f6f9238112cb`, no licence file |
| `timothyheeeee/Autonomous-Grading-Engine` | 🔴 `REJECT gate2-grant` | `main@f3518b6c379a`, no licence file; also closed-`GPT-4o`-dependent |
| `thinkmoon/zhihui-teacher` | 🔴 `REJECT gate3-substance` | real `MIT` `1066B` `e936c2bc0ff4`, **`0` source files** |
| `vishalsachdev/canvas-mcp` | 🟢 `PASS` | `MIT` `1071B` `5385a26e2fac` `main@d86ff43925d5`, `212` source files |
| `learningequality/kolibri` | 🟢 `PASS` | `MIT` `1097B` `3c056b34a476` **`develop`**`@fe298f54494c`, `3145` source files |

🟢 **One failure per gate-outcome is the point: it proves no gate is redundant.**

### 🔴 The Kolibri trap — read this before copying the gate

**`learningequality/kolibri`'s default branch is `develop`, not `main`.** A licence probe with a
hardcoded `/main/` path gets `404` and rejects **Kolibri — MIT, `3,145` source files, a foundation
of this entire KB — as "unlicensed".** 🔵 Gate 2 **must** read at the ref gate 1 discovered. This is
the most likely route by which wrong licence data re-enters this base, and it is why the gates are
ordered rather than parallel.

### 🔵 Where it sits in an engagement

| Phase | Use |
|---|---|
| **Discovery intake** | Every candidate passes the gate before being written anywhere. `REJECT`s go to `agents/trending.md` as *flagged, with the gate name*; they never reach `agents/top.md`. This is `T63`/`T140` discipline made executable. |
| **Dependency CI** | Pin the engagement's dependency set and run on a schedule. A dependency that relicenses or goes dark fails the build with the gate that caught it. |
| **Client deliverable (EMEA)** | 🟢 A `PASS` line *is* an audit record — licence family, bytes, content hash, exact ref, source count. Under the EU AI Act, education grading and admissions are high-risk (`intel/market.md`, EMEA), and conformity assessment asks exactly this about third-party components. |

### 🔵 Composing it with what is already on these shelves

🟢 Run the gate over the agent-facing MIT integration tier this base recommends —
`vishalsachdev/canvas-mcp` (and the fork family `harrywang`, `Harikeshav-R`, `NelsonSpencer`,
`r-huijts`, `mdweaver`, `bruchris`, `DMontgomery40`, `admin978`, `JohannsenLum/canvas-api-mcp`),
`loyaniu/moodle-mcp`, `jtayped/sakai-mcp` — **before** picking one. 🔵 Ten near-identical forks are
a *choice*, and `src=` plus the licence hash is the cheapest objective way to make it: the fork with
`212` source files and a current ref is not the fork with four.
🔴 For autograding specifically, the gate rejects both of `p842`'s new candidates, so build from the
shelved `delip/autorubric` + `macsnoeren/genai-open-assessment` pair and treat **`OASIS`**
(arXiv `2609.09180`, **no code released**) as prior art only.
🟢 Upstream of the gate, `P83`'s pedagogical acceptance gate still decides whether a tutor is *good*;
`P94` only decides whether you are **allowed to ship it at all.** Run `P94` first — it is cheaper.

## 🔴 Forty-sixth pass (`p841`, 2026-11-16) — **`0` new recipes (`P93` → `P93`), stated with the reason**

🔴 **A compose pattern is only honest if it is built from components measured in the pass that
writes it. `p841` measured `0` new components, so it writes `0` new recipes.**

🟢 **The two engagement shapes the regional legs pointed at are ALREADY shipped here, and `p841`
re-confirms their demand side rather than duplicating them:**

- **Mandated AI-literacy delivery (APAC).** Vietnam MOET Decision `2422` (`12` periods per class per
  year, grades `1`–`12`, from the `2026-2027` academic year) plus Korea's AI Basic Act →
  🟢 **already wired by `P91`** (vocational AI-literacy programme, two MIT estates for courseware,
  NTNU pedagogy read-only) and **`P75`** (AI-literacy programme that does not license curriculum).
  🔴 **No new recipe needed; the `2422` hour-budget is a sizing input to `P91`, not a new pattern.**
- **High-risk assessment governance (APAC/EMEA).** Vietnam Decision `33/2026/QD-TTg` naming
  automated assessment, and Reg (EU) `2026/1744`'s `2027-12-02` Annex III date →
  🟢 **already wired by `P91`'s compliance notes and the `P92` GPL-boundary line.**

🔵 **The honest statement for a studio reading this file today: the education recipe shelf is
saturated against the current open-source supply. The next genuinely new pattern needs a new
COMPONENT, and `36` consecutive battery nils say the component is not arriving through the mandated
discovery channel** — `T63`, `T140`.


## 🟢 Forty-fifth pass (`p840`, 2026-11-16) — `2` recipes (`P92`–`P93`), both built from rows measured THIS pass

### 🟢 `P92` — Moodle AI assessment + credentialing line, wired so the GPL boundary is explicit and the estimate survives legal review

🔵 **The engagement this answers:** an institution on Moodle wants AI-assisted STEM assessment and
automated credential issuance, and the studio needs to deliver without accidentally putting its own
orchestration layer under GPL.

🟢 **Components, every grant byte-read `2026-11-16`:**

| Step | Component | Grant | Zone |
|---|---|---|---|
| 1. Scaffold | [`moodlehq/moodle-tool_pluginskel`](https://github.com/moodlehq/moodle-tool_pluginskel) `60★` | 🟡 `GPL` (`35,178 B`) | 🔴 Inside |
| 2. Assess | [`maths/moodle-qtype_stack`](https://github.com/maths/moodle-qtype_stack) `173★`, `v4.14.0 for Moodle 4.2+` | 🟡 `GPL-3.0` (`35,146 B`) | 🔴 Inside |
| 3. Issue credential | [`mdjnelson/moodle-mod_customcert`](https://github.com/mdjnelson/moodle-mod_customcert) `115★` / `205` forks | 🟡 `GPL-3.0` | 🔴 Inside |
| 4. Run it | [`aws-samples/aws-refarch-moodle`](https://github.com/aws-samples/aws-refarch-moodle) `150★` | 🟢 `Apache-2.0` | 🟢 Outside |
| 5. Style gate | [`moodlehq/moodle-cs`](https://github.com/moodlehq/moodle-cs) `28★` + [`moodle-local_codechecker`](https://github.com/moodlehq/moodle-local_codechecker) `73★` | 🟡 `GPL-3.0` (`moodle-cs`) · 🔴 **`codechecker` label `NONE` — not grant-verified this pass** | 🔴 Inside (CI only) |
| 6. Dev env | [`moodlehq/moodle-php-apache`](https://github.com/moodlehq/moodle-php-apache) `77★` | 🔴 No licence file found | 🟡 Dev only — do not ship |

🟢 **How to wire it, and the one decision that matters.** 🔴 **Do NOT call STACK in-process from your
agent.** 🟢 **Call it over its web-service API** — STACK's own `doc/en/About` documents an API that
serves questions as a web service, and `p840` verified that page by byte-read. 🔵 **An agent that
reaches assessment over HTTP has not linked to GPL code**, so the orchestration layer, the model
routing and any Globant-authored IP stay outside the copyleft boundary. 🔴 Steps `1`–`3` and `5` are
inside the Moodle tree and their deliverables ship GPL; say so in the SoW rather than discovering it
at handover.

🟢 **Two cautions carried from measurement, not guesswork:** 🔴 the AWS reference architecture has not
been pushed since **`2025-05-07`** (`18` months) — read it as a design reference and re-derive the
templates against current CloudFormation; 🔴 `moodle-php-apache` has **no licence file at its default
ref**, so it is a local development convenience and must not enter a client deliverable.

🟢 **Why STACK and not an LLM grader:** STACK grades a *mathematical expression* with a CAS, so it is
deterministic and auditable — exactly the property an EU high-risk grading system needs
(`intel/market.md`, EMEA). 🔵 **The LLM belongs in feedback and hint generation around a
deterministic grader, never in the score itself.** 🟢 Bonus reach: STACK also runs on **ILIAS**, so
this line is portable across the two copyleft LMSes common in EMEA public education.

### 🟢 `P93` — Curriculum-grounded tutor where the CONTENT licence, not the model, decides what can ship

🔵 **The engagement this answers:** a client wants a tutor that follows a real curriculum with
prerequisite ordering rather than improvising a syllabus per learner. 🔴 **The binding constraint is
never the model — it is whether the curriculum content can be adapted and shipped.**

🟢 **The spine, chosen ON LICENCE, all byte-read `2026-11-16`:**

- 🟢 **USE as the spine: [`ossu/math`](https://github.com/ossu/math) — `MIT`, `9,354★`** — full
  curriculum with prerequisite ordering, adaptable and shippable with attribution only.
- 🟢 **USE as the on-ramp: [`ossu/precollege-math`](https://github.com/ossu/precollege-math) —
  `MIT`, `346★` / `175` forks** — remediation, which is where the actual demand sits.
- 🔴 **DO NOT ship derivatives of [`ossu/data-science`](https://github.com/ossu/data-science) —
  `CC BY-SA 4.0`** (byte-read; GitHub says `NOASSERTION`). 🔵 At `22,420★` it is the obvious thing to
  reach for and **share-alike means the client's derived curriculum must itself ship `CC BY-SA 4.0`.**
  🟢 Reference it, link it, teach from it — do not fold it into proprietary courseware.
- 🔴 **Same trap, different licence family:
  [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — `ODbL-1.0`,
  `7,712★`** — a `1,590`-topic curriculum graph with `3,221` prerequisite edges, 🔴 **share-alike on
  the DATABASE.** 🔵 It is the best-shaped prerequisite graph available and the most likely to be
  copied without reading its grant.

🟢 **Wiring:** curriculum graph → topological prerequisite ordering → mastery state per learner →
tutor loop. 🔵 **Pair it with a learner model rather than a chat history** — `p839`'s
`hhyqhh/inno-agent` (`MIT`, `1,497★`) is the row on these shelves built around exactly that (`L1`
profile / `L2` agent-queryable wiki / `L3` session recall), so `P93` composes with it directly
instead of re-implementing mastery tracking.

🟢 **Regional placement, each stated with its measured limit:**

- 🟡 **APAC / Chinese-language delivery:**
  [`ossu/computer-science-cn`](https://github.com/ossu/computer-science-cn) is `MIT` at `1,603★`,
  🔴 **but last pushed `2023-09-04`** — a translation base to re-verify against English upstream,
  never a live dependency.
- 🔴 **LATAM / Brazil — the gap, and the cheapest fix in this document:**
  [`ossu/math-br`](https://github.com/ossu/math-br) (`181★`) is the only Brazilian-curriculum
  artefact `p840` found and it has **no licence file** (`LICENSE` → `404`, `LICENSE.md` → `404`,
  measured). 🟢 **Rebuilding a BNCC-aligned mathematics curriculum is months of content work;
  asking the author for an `MIT` or `CC BY` file is an email.** 🔵 **Open that conversation before
  quoting the rebuild** — and until a grant exists, run Brazilian engagements off `ossu/math` (`MIT`)
  with localisation as scoped work.
- 🟢 **EMEA:** keep the grader deterministic (`P92`) — personalised learning paths that *steer* the
  learner are inside the reported high-risk scope, so the curriculum graph should be inspectable and
  the ordering explainable, which an explicit prerequisite graph gives you for free.

## 🟢 `P90` — THE LATAM EVIDENCE ENGAGEMENT: build on licence-clean national open data, because the regional agent supply is measurably empty (forty-fourth pass, `p839`, LATAM anchor)

🔴 **Why this recipe exists.** Four consecutive passes declared a LATAM supply gap, and `p839`
proved the agent nil is real at the licence intersection (`T139`). 🟢 **But UNESCO IESALC measured
`87%` of `200` institutions across `19` countries using AI with only `26%` holding a formal
strategy — so the regional buyer is not asking for a tutor. They are asking what their AI is doing
and whether it is working.** 🔵 **That question is answerable TODAY with licence-clean national data,
and it is the only education deliverable in the region that currently is.**

### The substrate, with the grant that makes it shippable

| Layer | What it supplies | Grant, byte-read `2026-11-16` |
|---|---|---|
| [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) `139★` | **`establecimientos_educacionales`** (MINEDUC national establishment register) + **`resultados_educacionales`** (MINEDUC outcomes), annual, joined to normalised `CUT` codes; Parquet for Polars/DuckDB/SQLite, JSON, Excel workbook; per-layer provenance, freshness/coverage badges, drift detection, fail-loud CI, Zenodo DOI `10.5281/zenodo.22968698` | 🟢 Code **MIT** `1,070 B` `sha256:277707dcaa3b…`; 🟢 both education layers **`CC BY 3.0 CL`** — attribution only, **no share-alike, no non-commercial** |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | Knowledge tracing — the model that turns interaction history into a per-learner mastery estimate | 🟢 MIT (already shelved) |
| [`Premshaw23/Learnova`](https://github.com/Premshaw23/Learnova) `96★`/`239`f | Attendance + engagement capture, where no system of record exists to read | 🟢 MIT `1,092 B` `sha256:535250f49c6a…` 🔴 ref `master` |
| [`azapg/FAIR`](https://github.com/azapg/FAIR) `6★` | The assessment half: Interpreters → Graders → Artifacts, with **A/B comparison across grading approaches**; docs in **Spanish and English** | 🟢 MIT `1,068 B` `sha256:3aa6498da2b9…` |
| LangGraph / Grafana / Appsmith | Policy nodes, dashboards, internal tools | 🟢 MIT / AGPL-3.0 (🔴 Grafana AGPL — read `intel/licence-requests`) |

### The wiring

```
chile-hub (pip install chile-hub)
  ├── load_polars("establecimientos_educacionales")   # the register: who, where, dependency type
  └── load_polars("resultados_educacionales")         # the outcomes, annual
            ↓  join on codigo_comuna (CUT, schema-contracted)
      [EQUITY BASELINE]  outcomes × territory × establishment type
            ↓
      client's own data  ──  attendance/engagement (Learnova) or the incumbent SIS
            ↓
      pyKT knowledge tracing  →  per-learner mastery + dropout risk
            ↓
      LangGraph policy nodes  →  WHO gets flagged, to WHOM, under what human-review rule
            ↓
      Grafana / Appsmith      →  the institutional dashboard
            ↓
      FAIR                    →  if assessment enters scope, A/B the graders BEFORE adopting one
```

### What makes this defensible rather than another dashboard

🟢 **1. The national baseline is free and citable.** The client's own numbers mean nothing until
they sit beside the national distribution for comparable establishments. 🔵 **`chile-hub` supplies
that comparison under attribution-only terms with a DOI, so the baseline is both legal to ship and
citable in an accreditation document.**

🟢 **2. The provenance report IS the audit artefact.** Every layer declares source organism, direct
URL, retrieval mode and timestamp, with drift detection on the upstream source. 🔵 **When a
ministry or an accreditor asks where a figure came from, the answer is generated, not reconstructed.**

🟢 **3. The licence posture is the opposite of the usual trap.** `T139`: `CC BY 3.0 CL` carries **no
share-alike**, so a closed client derivative is permitted; the obligation is attribution. 🔴
**Contrast `os-taxonomy` (`ODbL-1.0`), whose share-alike propagates into any derived database —
`T134`.**

🔴 **4. Say the limits out loud, in the proposal.** The education layers refresh **ANNUALLY**: this
answers structural and equity questions and **never** a real-time one. It is **CHILE only** —
Brazil, Mexico, Colombia and Argentina publish national education data whose licence terms `p839`
did NOT verify, so a multi-country version of this recipe starts with that verification, not with
code. `13` forks means early adopter. 🔴 **And `FAIR` is a `6★` MVP: use it to compare graders in a
pilot, never as the system of record for a term's marks.**

🔵 **Sequencing, `8`–`10` weeks:** weeks 1–2 stand up `chile-hub` and reproduce the national
baseline; 3–4 join the client's register and attendance; 5–6 fit `pyKT` and validate against known
outcomes; 7–8 policy nodes and human-review rules with the institution's own staff; 9–10 dashboard
and the provenance/audit pack. 🟢 **Deliverable is the evidence layer plus the audit trail — which is
what `26%`-with-a-strategy institutions are actually missing.**

---

## 🟢 `P91` — THE VOCATIONAL AI-LITERACY PROGRAMME: two MIT estates for the courseware, a university course for the pedagogy you may NOT ship (forty-fourth pass, `p839`, Global; APAC and LATAM delivery notes)

🔴 **Why this recipe exists.** `P86` (`p837`) found the vocational tier had funding rails and **`0`
build-safe software supply**. 🟢 **`p839` found the supply, and it is shaped as organisation-scale
curriculum ESTATES that no keyword leg could see (`T137`).** 🔵 **Meanwhile every regional leg this
pass reported AI literacy becoming a core skill — so the demand and the supply arrived in the same
measurement window.**

### The parts, and the licence that decides each one's role

| Part | Role in the programme | Grant, byte-read `2026-11-16` |
|---|---|---|
| [`ai-infra-curriculum`](https://github.com/ai-infra-curriculum/ai-infra-engineer-learning) — **`28` repos** | 🟢 **THE SPINE.** `14` role tracks (junior → principal engineer, architect → principal architect, team lead, MLOps, ML platform, inference, performance, SRE), **each a `-learning` repo PAIRED with a `-solutions` repo.** Flagship `1,887★`/`324`f; entry track `265★`/`65`f | 🟢 **MIT** `1,081 B` `sha256:67475eade1ef…` |
| [`WenyuChiou/awesome-agentic-ai-zh`](https://github.com/WenyuChiou/awesome-agentic-ai-zh) **`8,782★`** | 🟢 **THE SEQUENCE.** LLM fundamentals → multi-agent systems, market-validated by `1,086` forks; **繁中 / English / 简中** | 🟢 **MIT** `1,068 B` `sha256:1e034229fd46…` |
| [`keyuchen21/agentic-engineering-handbook`](https://github.com/keyuchen21/agentic-engineering-handbook) `589★` | 🟡 The production band: harnesses, MCP, evals, production agent systems | 🟢 **MIT** `1,056 B` `sha256:1126322e2cc8…` |
| [`bigmoumou/AI-Agent-Literacy`](https://github.com/bigmoumou/AI-Agent-Literacy) `55★` | 🔴 **PEDAGOGY REFERENCE ONLY — read it, do not ship it.** NTNU-piloted 2026: weekly microlearning (`39` videos, ~`121` min), browser practice computers, scenario-based Week 6 exam, project homework | 🔴 **SPLIT: code MIT (`1,068 B` `sha256:f8e1c1b97c59…`) / content CC BY-NC-SA 4.0 (`7,877 B` `sha256:8f65175f489e…`)** |
| [`munitkala/selfsemester`](https://github.com/munitkala/selfsemester) `102★` | 🟢 **THE PER-LEARNER RUNTIME.** Issues a scheduled, deadline-enforced, marked course with a transcript; a **readiness report before the learner commits**; course builder runs with no model at all | 🟢 **MIT** `1,081 B` `sha256:f5fe104e348d…` |
| [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) **`1,497★`** | 🟢 **THE LEARNER MODEL.** `L1` profile / `L2` wiki / `L3` session recall, cron scheduler, IM channels, Practice Lab | 🟢 **MIT** `1,080 B` `sha256:f92c6c6a1cc8…` |
| `TutorMoments` (`p837`) · `Drop Project` (`p837`) · `CorrectExam` (`p839`) · `FAIR` (`p839`) | 🟢 Evaluation and assessment: does it teach well, and is the grade defensible | 🟢 Apache-2.0 / MIT |

### 🔴 The licence gate, applied before any content is written

```
AI-Agent-Literacy  ──[READ]──►  pedagogy: microlearning length, practice-machine
   (CC BY-NC-SA)                 design, scenario-exam format, numbered key points
        │
        └──[DO NOT SHIP]──►  ✗ its videos, its site content, any derivative of them
                                 (NC forbids paid engagement; SA propagates)

ai-infra-curriculum + awesome-agentic-ai-zh + agentic-engineering-handbook
   (all MIT)       ──[SHIP]──►  ✓ the courseware, the exercises, the answer keys,
                                   client-branded derivatives, closed deliverables
```

🟢 **This is the whole reason the programme is buildable: the pedagogy that is proven at a national
university is licence-encumbered, and the courseware that is permissive is `28` repositories deep.
Take the shape from one and the substance from the other.**

### The wiring

```
awesome-agentic-ai-zh          → the SEQUENCE (what, in what order)
         ↓
ai-infra-curriculum -learning  → the exercises for the chosen role track(s)
ai-infra-curriculum -solutions → the answer key, held by the studio NOT the learner
         ↓
AI-Agent-Literacy (read only)  → the FORMAT: weekly microlearning, browser practice
                                  machine, scenario exam, human-reviewed scripts
         ↓
selfsemester                   → per-learner delivery: scheduled release, hard
                                  deadlines, auto-marked quizzes, rubric marking,
                                  transcript  ── one instance per learner
   or inno-agent               → where a persistent learner MODEL is wanted instead
                                  of a fixed course (L1 profile, misconception tracking)
         ↓
CorrectExam / Drop Project / FAIR → assessment; TutorMoments → does it teach well
```

### What to tell the client before they sign

🔴 **1. Maturity is not uniform across the spine.** The estate's stars run `1,887`, `265`, `82`,
`16`, `15`, `15`, `11`, `5`, `2`, `2`, `1`, `0`… 🟢 **Scope the engagement to the junior and
engineer tracks, which have real fork counts (`324` and `65`), and treat the senior/architect tracks
as drafts to be finished as part of the work — priced as authoring, not as adoption.**

🔴 **2. `selfsemester` and `inno-agent` are both SINGLE-LEARNER by design.** `selfsemester` is
Windows-only and self-described early (`0.7.0`, "little real-world use"); `inno-agent` declares one
active session, no auth model, no tenant isolation, "run one instance per person". 🟢 **A `200`-seat
cohort is `200` instances plus an orchestration layer. That is a real line item, and pretending
otherwise is how this delivery fails.**

🟢 **3. The evaluation is the differentiator, not the content.** Any vendor can produce a syllabus.
🔵 **`TutorMoments` scores tutoring quality against expert-annotated moments, and `FAIR` A/B tests
grading approaches on the client's own submissions — so this programme can state its instructional
claim as a measurement.**

🔵 **Delivery notes by region.** **APAC:** `awesome-agentic-ai-zh` is trilingual and
`AI-Agent-Literacy`'s site adds Vietnamese, so one programme serves Taipei, Singapore, mainland and
Hanoi cohorts without a translation project — and Vietnam's high-risk education classification plus
Korea's high-impact designation make the evaluation evidence a compliance artefact, not a nicety.
**LATAM:** pair with `P90` — the workforce argument lands where `FAIR`'s Spanish documentation and a
national evidence baseline already exist. **EMEA:** substitute `CorrectExam` for the assessment leg
where paper assessment and data residency dominate. **North America:** the vocational funding rails
in `P86` remain the entry, and North Carolina's `2028-06-30` teacher-training deadline (`p839`) is a
dated hook.

🔵 **Sequencing, `10`–`12` weeks:** 1–2 choose role tracks and audit the `-solutions` repos for
completeness; 3–4 fix the sequence against `awesome-agentic-ai-zh` and write the gap material;
5–6 build the practice environment on the `AI-Agent-Literacy` pattern (MIT half only); 7–8 stand up
`selfsemester` or `inno-agent` per learner plus orchestration; 9–10 assessment and the
`TutorMoments` acceptance gate; 11–12 pilot cohort and instrument the outcomes.

---

## 🟢 `P87` — GROUND THE TUTOR IN A NATIONAL CURRICULUM YOU ARE LICENSED TO SHIP (forty-third pass, `p838`)

🔵 **The engagement this answers.** A ministry, an academy trust, a publisher or an edtech vendor
wants an AI tutor or lesson assistant that is **aligned to the national curriculum** — and wants to
own the result. 🔴 **The usual failure is to paste curriculum text into a prompt: unversioned,
unattributable, and legally undefined. The second usual failure is to build the curriculum graph on
`os-taxonomy`, whose ODbL share-alike makes the client's extended graph non-proprietary (`T134`).**

🟢 **The build, all MIT or OGL-UK-3.0 — every grant byte-read `2026-11-16`.**

| Layer | Component | Grant |
|---|---|---|
| Curriculum ground truth | [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) — RDF/OWL/SKOS/SHACL, SPARQL-queryable | 🟡 **OGL-UK-3.0** (data) + **MIT** (code), `1,867 B` `98ac0c16f708` |
| Runtime query surface | [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) | 🟢 MIT `1,077 B` `0eeb9d32caed` |
| Agent reach | [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) — MCP app + generated TS SDK + semantic search | 🟢 MIT `1,086 B` `02c5a8e84229` |
| Assistant reference | [`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) (Aila) | 🟢 MIT `1,077 B` `d150aadcccd2` |
| Agent-behaviour consistency | [`oaknational/oak-agent-skills`](https://github.com/oaknational/oak-agent-skills) + `oak-ai-plugins` | 🟢 MIT |
| 🔴 **Acceptance gate** | [`allenai/tutormoments`](https://github.com/allenai/tutormoments) (`P83`) | 🟢 Apache-2.0 |

🟢 **How it wires.** The ontology is pinned at a **release tag** (never `main` — it is `v0.1.3` and
declares its URIs subject to change) and loaded into a triple store. `oak-curriculum-api` serves
lookups; the tutor resolves *"which unit, which prior knowledge, which misconception"* **at
runtime** against that graph instead of carrying curriculum in its prompt. The MCP app from the
ecosystem repo exposes the same graph to the assistants teachers already use, so the deliverable
lands inside ChatGPT/Claude/Copilot/Gemini rather than in a new product. `oak-agent-skills` keeps
behaviour consistent across teams. 🔴 **Then `P83`'s gate runs in CI: `TutorMoments` scores the
tutor on Appropriate Scaffolding, Appropriate Rigor and Avoids Over-Scaffolding against
expert-annotated moments, and the build fails if the thing does not teach.**

🔴 **What you must tell the client, in these words.**
1. **Attribution is the price of the data:** every surface carries *"Contains public sector
   information licensed under the Open Government Licence v3.0."* 🟢 There is **no** share-alike —
   the extended graph can be the client's asset (`T134`).
2. **The curriculum is ENGLAND's.** 🔴 The licence travels; the content does not. A Scottish, Welsh,
   Gulf or APAC deployment re-maps to the local framework — pair with `opensalt`/CASE for that.
3. **Aila is not a turnkey deployment.** 🔴 Its README says internal-use-oriented with no
   expectation that outsiders run it. 🟢 Adopt the architecture and prompt corpus, not the installer.
4. **Pin everything.** `v0.1.3`, `early_release`. 🔴 Not an official DfE publication.

🟢 **Sizing: `8–10` weeks** to a grounded, curriculum-aligned assistant with a passing `P83` gate,
assuming the triple store and the API are hosted by the client. 🔵 **The EMEA counterpart of `P85`
(extend India's Sunbird): the incumbent is open, so the pitch is extension of public
infrastructure, not replacement.**

---

## 🟢 `P88` — THE EXPLAINER-ASSET PRODUCTION LINE, WITH THE SUBJECT LEAD AS THE GATE (forty-third pass, `p838`)

🔵 **The engagement this answers.** A publisher, university or training provider must produce
hundreds of short explanatory assets — video, animation, decodable reading, interactive
walk-throughs — and cannot staff it. 🔴 **The thing that gets a generated teaching asset rejected is
almost never production quality. It is that no subject lead can tell where a claim came from.**

🟢 **The line, all MIT, every grant byte-read `2026-11-16`.**

| Stage | Component | Grant |
|---|---|---|
| Cited script → animation → narration | [`LaplacianAI/manimvox`](https://github.com/LaplacianAI/manimvox) | 🟢 MIT `1,068 B` `56fd265bbaea` |
| Hand-drawn progressive SVG + GIF frames | [`liangdabiao/whiteboard-teacher-video-motion`](https://github.com/liangdabiao/whiteboard-teacher-video-motion) | 🟢 MIT `1,068 B` `092d7cba85ea` |
| Lecture/seminar source as markdown | [`natolambert/colloquium`](https://github.com/natolambert/colloquium) | 🟢 MIT `1,071 B` `bce041d216bb` |
| Agents over EXISTING decks | [`pamelafox/presentation-skills`](https://github.com/pamelafox/presentation-skills) | 🟢 MIT `1,067 B` `e6bf682c17c8` |
| Code execution walk-throughs (CS) | [`precious112/code-slowmo`](https://github.com/precious112/code-slowmo) | 🟢 MIT `1,068 B` `0f8451cf2cc9` |
| Decodable early-reading delivery | [`finereli/yarareads`](https://github.com/finereli/yarareads) | 🟢 MIT `1,066 B` `7c4cf856c78c` |
| Embeddable STEM manipulables | [`itkdm/open-lab-components`](https://github.com/itkdm/open-lab-components) | 🟢 MIT `1,091 B` `8e86e6b3ee15` |

🟢 **How it wires.** `manimvox` is the spine *because it is the only component that emits a CITED
script* — research, citation, Manim render, narration. The citation file is the review artefact: the
subject lead approves **the script and its sources**, never the rendered video, and approval is
recorded against the asset before render spend. `whiteboard-teacher-video-motion` is the
alternative renderer where a drawn explanation beats an animated one (and is the one with real
traction — `42★` in eight days). `colloquium` holds lecture source in git so an agent can maintain
it; `presentation-skills` is the harder half — reading the `.pptx` estate the institution already
has. `code-slowmo` covers CS, where the misconception is execution order. `open-lab-components`
drops the interactive piece into an existing LMS page via its JS API.

🔴 **Constraints, stated.** `manimvox` is `6★` and a month old — read the code, budget Manim render
time. 🔴 `whiteboard-teacher-video-motion` and `open-lab-components` are Chinese-language: the
produced asset is language-neutral, the prompts are not. 🔴 **`yarareads` is phonics, and phonics is
orthography-specific** — a Spanish or Bahasa deployment is a new decodability corpus, not a
translation. 🟢 **Pair the output with `P83`/`TutorMoments` only where the asset is interactive; a
video is reviewed by a human, not scored by a simulated student.**

🟢 **Sizing: `6–8` weeks** to a running line with an approval gate and the first `50` assets.

---

## 🟢 `P89` — THE UNIVERSITY LAB-AND-AUTOGRADE ESTATE: grade code by RUNNING it, somewhere disposable (forty-third pass, `p838`, EMEA anchor)

🔵 **The engagement this answers.** A university or vocational provider with programming or
engineering cohorts wants automated assessment. 🔴 **Marking code by reading it is what an LLM does
cheaply and badly. The defensible version runs the student's code against tests — which requires a
disposable machine per student, and that is the half nobody budgets for.**

🟢 **The estate, all Apache-2.0 or MIT, every grant byte-read `2026-11-16`.**

| Layer | Component | Grant |
|---|---|---|
| Disposable execution target | [`netgroup-polito/CrownLabs`](https://github.com/netgroup-polito/CrownLabs) — K8s VMs/containers per student | 🟢 Apache-2.0 `11,356 B` `22f773775976` (ref **`master`**) |
| Submission + evaluation client | [`rage/tmc-cli-rust`](https://github.com/rage/tmc-cli-rust) — TestMyCode, MOOC.fi lineage | 🟢 Apache-2.0 `11,352 B` `5f8dce79b134` |
| JVM/Gradle grading reference | [`RiceComp215-Staff/RiceChecks`](https://github.com/RiceComp215-Staff/RiceChecks) | 🟢 Apache-2.0 `11,357 B` `c71d239df917` 🔴 stale `2023-01-09` |
| Continuous project grading | [`drop-project-edu/drop-project`](https://github.com/drop-project-edu/drop-project) (`P84`) | 🟢 Apache-2.0 |
| Quiz/assessment surface | [`socialsoftware/quizzes-tutor`](https://github.com/socialsoftware/quizzes-tutor) | 🟢 MIT `1,064 B` `c357a77752cd` (ref **`master`**) |
| Commercial-MOOC delivery path | [`coursera/coursera_autograder`](https://github.com/coursera/coursera_autograder) | 🟢 Apache-2.0 `11,337 B` `1332404c1e9f` 🔴 stale |

🟢 **How it wires, and the rule that makes it defensible.** CrownLabs issues a per-student
environment; the grader runs **inside** it, so arbitrary student code executes against a blast
radius of one disposable container. `tmc-cli-rust` or `drop-project` decides the **grade
deterministically** — compiles, student's own tests, coverage threshold, teacher's tests, coding
guidelines, performance. 🔴 **`P84`'s rule holds and is the whole governance story: the MODEL NEVER
SETS THE GRADE. The agent writes only the FEEDBACK NARRATIVE over a deterministic result**, which is
what survives an appeal and what Ofqual-style marking principles expect. `quizzes-tutor` covers the
non-code assessment on the same stack.

🔴 **Constraints, stated.** CrownLabs is a Kubernetes platform — a client without K8s capability is
buying an operating burden; its ref is **`master`**. 🔴 `tmc-cli-rust` is the CLIENT half; the server
estate (`tmc-langs`, `tmc-server`) is separate, so scope which half you run. 🔴 `RiceChecks`
(`2023-01-09`) and `coursera_autograder` (`2026-01-28`) are **stale — mine them, do not depend on
them**; Drop Project needs JDK 17–23 because Java 24+ removed the SecurityManager (JEP 486). 🟢
**Three independent university autograders on the JVM (Helsinki, Rice, ISCTE) is enough to argue
the pattern is institutionally normal rather than one group's habit.**

🟢 **Sizing: `10–12` weeks** for a cohort-scale estate with deterministic grading, generated
feedback and an evidence trail. 🔵 **EMEA anchor (Italy, Finland, Portugal provenance), portable to
any provider that must defend a mark.**

---


## 🟢 `P83` — PROVE THE TUTOR BEFORE YOU SHIP IT: a pedagogical acceptance gate in CI (forty-second pass, `p837`)

🔵 **The engagement this answers.** A client — a ministry, a university system, a publisher, a
workforce programme — wants an AI tutor. 🔴 **What they will be asked for at renewal, by a
procurement office or an evaluator, is not a demo: it is evidence that the thing teaches.**
`intel/market.md` this pass: **only `45%` of the most-used education tools have research meeting an
ESSA evidence tier**; **Ofqual has published principles for AI in high-stakes marking**; the OECD's
position is that AI helps only when pedagogy stays in control. 🟢 **`P83` makes "it teaches" a
BUILD ARTEFACT produced on every commit, instead of a claim defended after delivery.**

**The wiring — every component a row on these shelves with a byte-verified grant:**

```
  [ Tutor under test ]
  HKUDS/DeepTutor (Apache-2.0)  — or the client's own agent, or any tutor row on agents/top.md
            │  exposed behind one provider-agnostic chat endpoint
            ▼
  [ ACCEPTANCE GATE ]  allenai/tutormoments (Apache-2.0, 11,377 B, sha256:b2c7059a9ab4…)
     tutormoments run --tutors <model-or-endpoint> --modes plain scaffolding_rigor --sample N
            │  simulated student × frozen expert-annotated moments
            ├── Appropriate Scaffolding        ── did it scaffold WHERE a teacher would?
            ├── Appropriate Rigor              ── did it raise cognitive demand WHERE a teacher would?
            ├── Avoids Over-Scaffolding        ── did it answer instead of teach?   ◄── the one that matters
            └── Action Taxonomy               ── how do its moves differ from a human tutor's?
            ▼
  [ GATE DECISION in CI ]  fail the build on regression in any of the four, not on an average
            ▼
  [ EVIDENCE ARTEFACT ]  per-release scorecard, retained → the document procurement asks for
            │
            └─► served to the institution through the LMS it already runs:
                  Moodle (GPL-3.0) / Open edX (AGPL-3.0) via LTI 1.3  — see the licence note below
```

**Build order, and the week it belongs in:**

1. **Week 1 — endpoint, not integration.** Put the tutor behind one chat endpoint. 🔴 **Do not
   start with the LMS.** TutorMoments drives a model-under-test; anything that needs a logged-in
   student is out of scope for the gate.
2. **Week 1–2 — baseline, and publish it internally before tuning anything.** Run the harness over
   the released dataset at `--sample 10`, then full. 🟢 **Record the four metrics for a frontier
   model, for the client's chosen model, and for the client's CURRENT product if one exists.** 🔵
   **The third number is the one that sells the engagement.**
3. **Week 2–4 — tune against the gate, and watch the right metric.** 🔴 **Appropriate Scaffolding
   and Avoids Over-Scaffolding move in OPPOSITE directions under naive prompt tuning:** telling a
   model to be more helpful raises one and destroys the other. 🟢 **Report the pair, never a
   composite score.**
4. **Week 4–6 — wire the gate into CI** so a prompt change that makes the tutor more agreeable and
   less pedagogical fails the build. 🟢 **This is the deliverable the client keeps after the
   studio leaves.**
5. **Week 6–8 — the LMS leg**, if in scope: mount through **LTI 1.3**, not a bespoke plugin per
   platform (the standards section of `verticals/solutions.md`).

🔴 **Licence consequence, stated at PROPOSAL time rather than at delivery.** TutorMoments and
DeepTutor are Apache-2.0 — a studio may fork, re-skin and ship both. 🔴 **Moodle is GPL-3.0 and
Open edX is AGPL-3.0, and AGPL's network clause reaches a HOSTED derivative: a client-facing Open
edX fork delivered as a service must offer its source to its users.** 🟢 **Keeping the tutor and
the gate OUTSIDE the LMS and mounting over LTI 1.3 keeps the studio's work on the permissive side
of that line. That is an architectural reason, not a legal preference.**

🔴 **The honest limitation, and it is a priced deliverable rather than a caveat.** The moment set is
cut from **English-language** transcripts. 🟢 **The harness transfers to a LATAM or EMEA
engagement; the DATASET does not.** 🔵 **Building a Spanish- or Portuguese-language moment set with
the client's own expert teachers is `6`–`8` weeks of work, produces an asset no competitor has,
and `T132` records that no open tutoring benchmark exists in either language.**

**Effort:** `6`–`8` weeks for the gate and baseline; `+6`–`8` for a non-English moment set.


## 🟢 `P84` — AUTO-GRADING WHERE THE GRADE IS DETERMINISTIC AND ONLY THE FEEDBACK IS GENERATED (forty-second pass, `p837`)

🔵 **The engagement this answers, and it is `T96`'s gap closed with the right architecture.** A
university department, a bootcamp or a national programme marks thousands of programming
submissions. 🔴 **The pitch they receive is "an LLM grades it". That pitch fails the first appeal:
a model cannot produce a defensible mark, and in England Ofqual has now published principles for AI
use in high-stakes marking.** 🟢 **`P84` puts a DETERMINISTIC grader of record underneath and uses
the model only for the thing models are good at — explaining the result to the student.**

**The wiring:**

```
  [ STUDENT SUBMISSION ]  via the LMS the institution already runs, over LTI 1.3
            ▼
  [ GRADER OF RECORD — deterministic, no model in the loop ]
  drop-project-edu/drop-project (Apache-2.0, 11,357 B, sha256:c71d239df917…, Kotlin/JVM, ghcr image)
    ├── structure + mandatory files present?
    ├── does it COMPILE?
    ├── does it pass the STUDENT's own tests?
    ├── minimum COVERAGE reached?
    ├── does it pass the TEACHER's tests?        ◄── the mark comes from here
    ├── does it meet the teacher's CODING GUIDELINES?
    └── does it PERFORM? (large-dataset timings)
            │   → machine-readable report, student-visible and teacher-visible
            ▼
  [ ENVIRONMENT + TELEMETRY ]  AnubisLMS/Anubis (MIT, 1,083 B, sha256:e36740a2a510…)
     browser IDE + Kubernetes-provisioned per-student environment; collects the WORK, not just the result
            ▼
  [ FEEDBACK LAYER — the only generative component ]
     LLM reads the deterministic report + the diff and writes the NARRATIVE:
       what failed, which concept it maps to, what to read, what to try next
            ▼
  [ INVIGILATION, only where the assessment is high-stakes ]
     shaheeranser/exam-proctor (Apache-2.0) — LTI 1.3, runs inside Moodle
     contract reference: openedx/mockprock  🔴 licence field says Apache-2.0, NO grant payload at root — read it, do not ship it
            ▼
  [ GRADEBOOK ]  back over LTI 1.3 Assignment & Grade Services
```

**The rules that make this defensible, and each one is a rule because its violation is a known
failure:**

1. 🔴 **The model NEVER produces or adjusts the mark.** The mark is "passed the teacher's tests",
   which is reproducible, appealable and explainable to a registrar. 🟢 **The model produces prose
   about a mark that already exists.**
2. 🟢 **Every generated sentence must cite a line of the deterministic report.** An uncited claim
   in feedback is a hallucination with a student's grade attached to it.
3. 🔴 **Scope limits, stated because they bound the sale:** Drop Project handles **Java 8+ and
   Kotlin only**, needs a **JDK 17–23** (Java 24+ removed the SecurityManager, JEP 486; `18`–`23`
   require `-Djava.security.manager=allow`), and needs a relational database. 🟡 **Other languages
   mean another runner behind the same contract — that is the extension point, and it is where the
   build hours go.**
4. 🟢 **Teacher tests are the real artefact.** The engagement's hard work is helping faculty write
   the test suites that encode their rubric. 🔵 **Budget for that explicitly: it is pedagogical
   work billed as engineering, and it is the part that cannot be bought.**
5. 🔴 **Proctoring is opt-in and jurisdictional.** In the EU it is an Annex III high-risk use with
   obligations landing `2027-12-02`, and Article 50 transparency duties apply ALREADY
   (`intel/market.md` this pass). 🟢 **Ship `P84` without the invigilation leg by default.**

**Effort:** `8`–`10` weeks for grader + feedback + LTI mount on one language stack; `+3`–`4` per
additional language runner; `+4` for the invigilation leg where it is lawful and wanted.


## 🟢 `P85` — THE APAC NATIONAL-STACK ENGAGEMENT: extend India's incumbent instead of proposing a replacement (forty-second pass, `p837`)

🔵 **The engagement this answers.** A state board, a national programme or an NGO in India wants AI
on its education platform. 🔴 **The platform already exists, it is deployed to all `36` states and
union territories in `30+` languages, and proposing to replace it loses the engagement.** 🟢 **The
Sunbird estate is MIT almost throughout — `T126` measures it at `196/212 = 92.5%` permissively
licensed, the highest of any education authority in this base — so a studio may legally fork,
extend and ship it. That is the whole opportunity.**

**The stack, every component byte-verified and restored to these shelves this pass:**

```
  [ PORTAL ]      Sunbird-Ed/SunbirdEd-portal        MIT  1,072 B  sha256:7dde06716f25…   41★/318f  master  pushed 2026-02-21
  [ CONTENT ]     Sunbird-Knowlg/knowledge-platform  MIT  1,072 B  sha256:fd3adcd57676…   17★/182f  master  pushed 2026-11-13
                                                     © 2019 Project Sunbird — content, taxonomy, DIAL codes
  [ IDENTITY ]    Sunbird-Lern/userorg-service       MIT  1,072 B  sha256:7dde06716f25…   31★/162f  master  pushed 2026-03-02
                                                     © 2018 Project Sunbird — channel isolation = 36 boards, one deployment
  [ ASSESSMENT ]  Sunbird-inQuiry/editor-v2          Apache-2.0  11,357 B  c71d239df917…   0★/4f   main  pushed 2026-11-11
                  Sunbird-inQuiry/player-v2          Apache-2.0  11,357 B  c71d239df917…   0★/5f   main  pushed 2026-10-06
                                                     QuML authoring + delivery — the only end-to-end assessment
                                                     chain this base holds under permissive grants only
            ▼  the agent layer the studio actually builds and owns
  ├── CONTENT TAGGING agent        → classify incoming material against the NATIONAL taxonomy, not a generic one
  ├── DIAL-CODE resolution agent   → textbook QR → the right digital artefact in the right language
  ├── LANGUAGE ADAPTATION agent    → one lesson, 30+ languages, reviewed by a human per language
  ├── TEACHER ASSISTANT agent      → aligned to the board's own curriculum, grounded in Knowlg
  └── ENROLMENT TRIAGE agent       → over userorg-service's channel model
            ▼
  [ EVALUATION ]  P83's gate, with a Hindi/regional-language moment set built with the board's teachers
```

🔴 **Five delivery facts that decide whether this engagement succeeds, all measured on these
shelves rather than assumed:**

1. 🔴 **There is no such thing as a "Sunbird version". The estate moves at five different
   speeds**, all measured `2026-11-16`: `knowledge-platform` pushed **`2026-11-13`**,
   `inQuiry/editor-v2` **`2026-11-11`**, `inQuiry/player-v2` **`2026-10-06`**,
   `userorg-service` **`2026-03-02`**, the portal **`2026-02-21`**. 🟢 **Pin per repository and
   state the date per repository.** 🔵 **The content and assessment layers are live; the portal and
   identity layers are the stale ones, which is the opposite of what a reader would assume from
   the portal being the famous repository.**
2. 🔴 **Default refs are `master`, not `main`,** across the estate. A clone script that assumes
   `main` gets nothing. 🔵 **This base reproduced that failure twice in one pass on other
   repositories — it is the most common self-inflicted error here.**
3. 🔴 **`SunbirdEd-mobile-app` release branches `release-2.6.0` and `release-2.7.0` carry NO grant
   at `25` root paths, while the project is MIT on `main`.** 🟢 **An engagement that pins an old
   release — which India engagements do — pins a branch with no licence file on it. Resolve the
   grant at the ref you ship, and get it in writing if you ship a pinned release.**
4. 🟡 **The repositories are large — the Sunbird tree was measured at `334 MB`.** Shallow-clone,
   and budget CI accordingly.
5. 🔵 **The fork-to-star ratio is the signal and it holds across the whole estate, not just the
   portal: `41★`/`318` forks = `7.8:1`, `knowledge-platform` `17★`/`182` = `10.7:1`,
   `userorg-service` `31★`/`162` = `5.2:1`, and the two inQuiry repositories have `4` and `5`
   forks against `0★`.** 🟢 **Nobody forks a backend `182` times to read it — these are deployments.
   Star-ranked discovery cannot see any of it, which is exactly why a competitor pitching from a
   trending list will propose building what the client already runs.**

**Effort:** `4`–`6` weeks to stand up and read the estate; `10`–`14` weeks for two agent surfaces in
production against a live state deployment.


## 🟡 `P86` — THE VOCATIONAL ENGAGEMENT, BUILT FROM THE FUNDING RAIL BECAUSE THE SOFTWARE TIER IS EMPTY (forty-second pass, `p837`)

🔴 **This recipe is published with its thinness on the label.** This base declared the vocational
platform tier a measured gap in five languages (`p829`, `T114`, `T118`); `T128` found the
POPULATION is real (`58` MIT + `39` Apache repositories) and `T129` found that **almost none of it
is shippable** — `0`–`2★`, single-author, no releases. 🟢 **So `P86` does not pretend there is a
platform to adopt. It builds from the two things that ARE institutional: the funding rail and the
matching problem.**

```
  [ FUNDING / ELIGIBILITY RAIL — the hard integration, and it is open ]
  hmrc/apprenticeship-levy (Apache-2.0, 11,357 B, sha256:b40930bbcf80…, Scala, pushed 2026-11-12)
    → UK: levy account, eligibility, the money that actually pays for the training
    🔵 the equivalent in each jurisdiction is the FIRST question of the engagement, not the last
            ▼
  [ MATCHING ]  NASWA-OpenUI/naswa-ai-apprenticeship-matcher (Apache-2.0, 11,382 B, sha256:2d915fb4a6ea…)
    → the US National Association of State Workforce Agencies' own POC: read it for the DATA MODEL
      and the institutional provenance, not for the code (2★, self-described POC)
            ▼
  [ CANDIDATE PREPARATION — the agent surface with the clearest value ]
  iatee/Hack-Apertus (Apache-2.0) — apprenticeship INTERVIEW coach running on Apertus,
    Switzerland's sovereign open LLM   🔴 0★, hackathon artefact: proof the wiring exists, nothing more
  Mahmud-Mahi/Seren--Your-IELTS-Tutor (MIT, master) — the same shape scored against a PUBLISHED
    rubric (CEFR), which is the model to copy for any vocational competence framework
            ▼
  [ SIMULATED WORKSHOP — the one thing a general LMS cannot provide ]
  blagojevicboban/GEAR (MIT, 1,073 B, sha256:0ccee16b71b8…) — WebXR built for VET, browser-delivered
    🔴 0★, 0 forks: evidence the browser route works. PRICE THE BUILD; do not quote this as a product.
            ▼
  [ RECORD OF ATTAINMENT ]  the credentialing tier already on these shelves (p817)
            ▼
  [ HOST ]  the client's existing LMS over LTI 1.3
```

🔴 **What to tell the client, in these words.** *The tutor tier of education AI is crowded and the
vocational tier is empty. There is no platform to adopt here — there is a funding API, a public
data model, and three proofs that the pieces work. The build is real and so is the gap, and the
gap is why the engagement is worth doing.* 🟢 **`T129` is the evidence that the category is wanted
and unserved; that is a better opening than a product tour.**

🔵 **Where the sovereign-model leg matters.** `Hack-Apertus` on Apertus is the only row on these
shelves demonstrating a vocational agent end-to-end on a European sovereign model rather than a US
API. 🟢 **For an EMEA public-sector buyer with a data-residency constraint, that is the
architecture diagram the proposal needs — and the EU date for Annex III education uses is
`2027-12-02`, with Article 50 transparency duties already live (`intel/market.md`).**

**Effort:** `4` weeks of discovery dominated by the funding/eligibility rail in the target
jurisdiction; `10`–`12` weeks for matcher + interview coach in production; the simulated-workshop
leg is a separate build, `12`+ weeks, and should be sold separately.

## 🟢 `P76` — the ACCESSIBLE-MATERIALS programme that produces EVIDENCE, not an overlay (forty-first pass, `p836`)

🔵 **The engagement this answers.** A ministry, university system, publisher or district must make
its digital course materials conform — **`WCAG 2.1 AA` under ADA Title II by `2027-04-26`
(entities serving ≥ `50,000`) or `2028-04-26` (below that)**; **Annex I of the European
Accessibility Act, in force since `2025-06-28`, for e-books and reading software**; or
**accessible-format duties under Brazil's Lei `13.146`/2015 art. 28 and Decreto nº `12.686`/2025**.
🔴 **What they are usually sold is an overlay widget and a dashboard. What a regulator, a
procurement office or a plaintiff asks for is a conformance report per artefact.** 🟢 **`P76`
produces the report.**

**The wiring, concretely — every component a row on this base with a verified grant:**

1. **Structural gate — `w3c/epubcheck`** (**BSD-3-Clause**, `2k★`, `v5.4.0`,
   `github.com/w3c/epubcheck`). Run FIRST, over the whole catalogue. 🔴 **An invalid EPUB fails
   before any accessibility criterion can be evaluated**, and a remediation programme that skips
   this step reports accessibility failures that are really packaging failures. Output: pass/fail
   plus error class per file.
2. **Accessibility conformance — `daisy/ace`** (**MIT**, `101★`,
   `github.com/daisy/ace`). Run as the **Node module or behind its HTTP API**, not the CLI
   one-file-at-a-time, so it scales to a catalogue. 🔵 **It runs the `axe` engine internally, and
   `dequelabs/axe-core` is already a row here** — so the HTML-level checks are the same engine the
   studio's web practice already uses. Output: machine-testable `EPUB Accessibility 1.1` findings
   plus the **accessibility metadata** state Annex I asks for.
3. **The human stage, and it is NOT optional — `daisy/ace-gui`** (**MIT**, `25★`, `v1.4.6`,
   `github.com/daisy/ace-gui`, Windows/macOS/Linux). 🔴 **Alt-text adequacy, reading-order sanity
   and described-image quality are not machine-decidable.** A VLM drafts alt text and long
   descriptions at catalogue scale; **a human accepts, edits or rejects each one in this GUI**; the
   accepted text is written back to the package. 🔴 **Do not automate the accept step — a fluent,
   wrong description passes every automated check while misinforming the student who depends on
   it.** 🟢 **MIT means this console can be forked and re-skinned as the client's own tool, so the
   capability stays with them when the engagement ends.**
4. **STEM content — `daisy/mathcat`** (already a row here). Equations are where EPUB remediation
   programmes stall; MathCAT turns MathML into speech and braille so a maths textbook is not
   silently excluded from scope.
5. **Accessible formats — `liblouis/liblouis`** (`354★`, **LGPL-2.1 library / GPL-3.0
   command-line tools**, both grant files byte-read). Required where statute asks for braille
   rather than screen-reader compatibility (**Brazil art. 28**). 🔴 **Licence wiring is specified,
   not left to implementation: DYNAMIC-LINK the LGPL-2.1 library, or run the GPL-3.0 CLI as a
   separate service the deliverable calls over a boundary.** 🟢 **Both keep a proprietary
   deliverable's own source closed; statically linking the CLI's code into the product does not.**
6. **Web surfaces of the LMS — `dequelabs/axe-core`, `pa11y/pa11y`, `ibma/equal-access`,
   `microsoft/accessibility-insights-web`** (all already rows here). 🔵 **Course FILES and the
   PLATFORM that serves them are two separate audits** and both are in scope; the EPUB stack does
   not cover Moodle's or Open edX's own pages.
7. **Delivery estate — Moodle, `frappe/lms`, or Open edX** (rows here). 🔴 **Open edX is
   `AGPL-3.0`** (settled by byte-read in `p833`): **a hosted client-facing fork must offer source
   to its users** — a proposal-time conversation, not a delivery-time surprise.
8. **The deliverable that closes the sale — the evidence pack.** Per artefact: `epubcheck` result,
   `ace` report, the human-review decision log from step 3, and the resulting **conformance
   statement**. 🟢 **This is what a procurement office accepts and what an overlay vendor cannot
   produce.**

**Shape of the engagement:** `6`–`10` weeks for pipeline build plus a pilot slice of the catalogue
(structural gate, automated conformance, review console, evidence template); then a
throughput-priced remediation programme. 🟢 **Licence posture: MIT + BSD-3-Clause for everything
the client keeps, copyleft isolated behind a service boundary at step 5 and declared at step 7.**
🔵 **Sell against the extended dates (`2027-04-26` / `2028-04-26`), which is time to do the
catalogue properly rather than a reason to defer** — and qualify the ≥/< `50,000` population split
in the first meeting, because it decides the delivery year. 🔴 **Anti-pattern to name explicitly:
an accessibility overlay. It is the thing clients buy, and it does not produce evidence.**

## 🟢 `P77` — TIMETABLING where the model elicits and the SOLVER decides (forty-first pass, `p836`)

🔵 **The engagement this answers.** Every school, faculty and university department rebuilds a
timetable each term: cohorts that must not collide, contiguous lab blocks, part-time staff
availability, room capacities, exam spacing per student. 🔴 **It is the most universal operational
problem in education and the one no LMS, SIS or MOOC row on these `147` vertical shelves touches.**
🔴 **It is also where an LLM-first design fails most expensively:** a language model returns a
plausible grid, and the double-booked cohort surfaces in week one in front of students.

**The wiring, concretely:**

1. **Constraint ELICITATION — the agent layer.** An LLM (any row from this base's agent shelves)
   turns the department's prose rules into a **declared, reviewable constraint set**: hard
   constraints (no cohort collision, room capacity, staff availability windows) versus soft ones
   (teacher preference, minimised gaps, balanced load). 🟢 **This is the part a model is good at:
   reading institutional prose and typing it.** 🔴 **It must emit CONSTRAINTS as data for human
   sign-off, never a schedule.**
2. **The model to lift — `sukrutrao/Timetabler`** (**MIT**, `43★`,
   `github.com/sukrutrao/Timetabler`). 🟢 **It encodes educational-institution timetabling as a
   SAT formula solved with a MaxSAT solver** — so it supplies the **constraint vocabulary and the
   hard/soft encoding** worked out for exactly this domain, which is the expensive part to invent.
   🔴 **Maintenance posture, stated: copyright line ends `2018`, two academic authors. Lift the
   model; do not pin a delivery to the dependency.**
3. **The engine that must survive a term — `google/or-tools` CP-SAT** (**Apache-2.0**, stable
   `v9.15`, `2026-01-12`, already a row here), or **`timefoldai/timefold-solver`** (Apache-2.0
   core, already a row), or **`UniTime/cpsolver`** with its **examination-timetabling extension**
   (already a row, and the only one of the three written for this domain natively). 🟢 **All
   permissive; all production-grade.**
4. **The guarantee, which is the reason to use a solver at all.** 🟢 **A solver returns a
   certificate: the hard constraints are satisfiable and here is a witness, or they are UNSAT and
   here is the conflicting core.** 🔵 **That UNSAT core is a deliverable in its own right** — it
   tells a dean *which* rules cannot coexist, which is the conversation that actually resolves a
   term's timetable. 🔴 **A model cannot produce it and cannot be asked to.**
5. **Explanation back to humans — the agent layer again.** The LLM renders the solver's output and
   its UNSAT core into departmental language ("your part-time Friday constraint and the contiguous
   lab block for cohort B cannot both hold"). 🟢 **Model at both ends, solver in the middle.**
6. **Integration surface.** Publish the solved timetable into the existing estate — SIS/LMS rows
   already on these shelves (`frappe/education`, `openeducat/openeducat_erp`,
   `francoisjacquet/rosariosis`, `GibbonEdu/core`, Moodle) — and keep the constraint set in version
   control, because 🟢 **the reusable asset across terms is the CONSTRAINTS, not the grid.**

**Shape of the engagement:** `4`–`6` weeks to a working term timetable for one faculty (elicitation
layer, constraint set under review, CP-SAT model, UNSAT explanation), then per-faculty rollout.
🟢 **Licence posture: MIT + Apache-2.0 throughout — no copyleft anywhere in this pattern.**
🔵 **Why it is a credible first engagement: the outcome is verifiable on day one** (the timetable
either satisfies the declared hard constraints or it provably cannot), 🔴 **which is the opposite
of every tutor-chatbot pilot, where the client cannot tell whether it worked for a semester.**
🔴 **Declared supply gap this pattern is built against: no mature, maintained, education-specific
timetabling PLATFORM under a permissive licence exists** — what exists is general solvers plus
student projects. 🟢 **That is why this is a BUILD offer and not an integration offer.**


## 🟢 `P75` — the AI-LITERACY programme that does not license curriculum (fortieth pass, `p835`)

🔵 **The engagement this answers.** A ministry, university system or corporate academy wants an
AI-literacy programme at scale. The first cost question is always the same: *license a commercial
curriculum per seat, or build one?* `P75` is the third option — **fork a vetted MIT one** — and
every component below is a row on this base's own shelves with a verified permissive grant.

**The wiring, concretely:**

1. **Curriculum spine — `microsoft/AI-For-Beginners`** (MIT, `70.8k★`,
   `github.com/microsoft/AI-For-Beginners`). Fork it. `24` lessons / `12` weeks of notebooks and
   labs become the syllabus of record. 🟢 **MIT is what makes re-sequencing and translation legal
   in a client deliverable** — the alternative is per-seat licensing.
2. **Delivery shell — `frappe/lms`** or an existing **Moodle** estate (see
   `verticals/solutions.md`). Lessons land as courses; the LMS owns enrolment, cohorts and the
   record of completion. 🔴 **Do not rebuild enrolment — it is the one thing the institution
   already has and the one thing procurement will not re-buy.**
3. **Tutor layer — `THU-MAIC/OpenMAIC`** (MIT, `43.6k★`) pointed **at the forked lessons**, so the
   multi-agent classroom teaches the client's syllabus rather than generating its own. 🟢 **This is
   the inversion that matters:** every tutor on these shelves generates content by default, and
   generated content is exactly what an accreditation office will not sign.
4. **Socratic constraint — `janestreet/agent_skills`** `socratic-tutor` (MIT, `7.9k★`). A
   `SKILL.md`, no code, no CVE surface: it forces one-question-at-a-time diagnosis and a final
   assessment over whichever LLM host the client already pays for.
5. **Integrity answer — `cheahhl814/lf-skill`** (MIT). The teach-back debrief is what lets the
   institution claim the learner demonstrably learned rather than offloaded. 🔵 **Ship this with
   the tutor, not after the first complaint.**
6. **Governance gate, by region — NOT optional.** **EMEA:** assessment and grading uses fall under
   Annex III, deferred to **`2027-12-02`**, but **chatbot transparency applies from `2026-08-02`** —
   so the tutor must disclose it is AI *now*, and the grading feature is the one to defer.
   **North America:** route learners through a controlled environment rather than public tools
   (the stated district pattern), and check the **COPPA** position for under-13s.
   **APAC:** a tutor with a persona falls under China's **anthropomorphic AI services** measures
   (`2026-07-15`); India requires **provenance labels** on synthetic output (`2026-02-20`).
   **LATAM:** Brazil's **PL 2338/2023** is not enacted — design to it, do not certify against it.

🟢 **Why this composes rather than merely co-exists:** steps 1–3 share one artifact — the forked
lesson tree — as curriculum, as LMS content and as the tutor's retrieval corpus. 🔴 **The known
limit, stated:** `AI-For-Beginners` teaches **AI itself**. For any other subject the spine must come
from the `p831` mother-tongue or `p833` national-curriculum layers, and `P75` degrades to steps
2–6.


# Compose patterns — education

**Seventy-four** concrete recipes — derived recipes: **74**. 🟢 **Thirty-ninth pass (`p834`, 2026-11-15): `P74` added** — the marking loop with its SUBSTRATE named, and the first recipe in this file whose human-review boundary is justified TWICE, independently. 🔵 **`P73` inherited one agent and still wrote the platform under it; `P74` inherits the platform too (`lsgwr/spring-boot-online-exam`, MIT, `1,695★`) and the closed-portal integration layer as well (`jiajia-jun/catcher`, `Unke-cc/chaoxing-grader-universal`, `mc-dl/ykt-grader`, all MIT), which takes the build to `4`–`6` weeks against `P73`'s `6`–`8` and `P67`'s `12`–`16`.** 🔴 **And its scoring boundary is no longer a compliance concession: `T119` shows at least `8` independent Chinese marking projects converging on `AI 预批 → 教师复核 → 系统记录` in a jurisdiction where EU AI Act Annex III does not apply, so the boundary is sold as teaching practice in APAC and as Annex III conformance in EMEA — the same build, two arguments.** 🟢 **Thirty-eighth pass (`p833`, 2026-11-15): `P73` added** — the marking loop WITH an adoptable base, and the first recipe in this file that AMENDS another: `P67` was written as *the recipe for a capability with NO adoptable base*, and `T114` closed that gap, so `P67`'s from-scratch rubric engine becomes the fallback while its scoring boundary is inherited wholesale — the model PROPOSES a mark and never RECORDS one. 🔵 **`6`–`8` weeks against `P67`'s `12`–`16`, the saving being the error-type taxonomy and the remediation generator.** 🔴 **And it carries `D833-2`'s correction as a build constraint: NOT Open edX unless the client accepts AGPL.** 🟢 **Thirty-seventh pass (`p832`): `P72` added** — the GRANT-CURRENCY harness, and the first recipe in this file whose subject is the knowledge base itself rather than a learner. 🔵 **Premise is `T111`/`T112`: a repaired measuring instrument does not propagate to measurements already published (`38.7%` of this base’s `442` pinned grant figures are unreproducible, mechanism proved `12`/`12`), and an absence verdict that hardened only its FILENAME axis is still wrong on every filename at once when the BRANCH is guessed (`3` false absences found in `38`, one of them a `GPL-3.0` obligation recorded as "no licence").** 🔴 **This is sold, not just used: any client inheriting an open-source stack has the same two defects, and a licence claim nobody can reproduce from the file it names is a procurement finding.** 🟢 **Every component is in this repository or is a standard tool; all figures byte-read `2026-11-15`.** 🟢 **Thirty-sixth pass (`p831`): `P71` added** — the mother-tongue foundational-literacy pipeline, and the first recipe in this file aimed at children aged `5`–`9` learning to read and count at all. 🔵 **Premise is `T108`: this is the only tier in this base where the open-source assets carry real outcome evidence and the newest code is the least usable, so the recipe INHERITS the maintained content and measurement pipelines (Bloom, libpalaso, Kolibri Studio, Tangerine — all pushed this week) and treats the field-trialled XPRIZE apps as a CURRICULUM SPECIFICATION to read rather than a dependency to adopt.** 🔴 **The EU AI Act boundary is drawn before node `1`: Annex III point `3` makes assessing learning outcomes high-risk by construction and the subject is a child, so the pipeline authors, delivers and TRANSCRIBES, and the score stays with a human enumerator inside Tangerine.** 🟢 **All ten components byte-read on `2026-11-15`; every market and regulatory item is `CITED, NOT READ`.** 🟢 **Thirty-fifth pass (`p830`): `P70` added** — the inclusive-delivery pipeline, and the first recipe in this file aimed at the SEN / inclusive-learner population rather than at a mainstream cohort. 🔵 **Premise is `T107`: inclusion COMPLIANCE is funded, deadlined and granted (MIT/Apache across the whole WCAG / Section 508 / EN 301 549 tier) while inclusion PEDAGOGY has a GitHub maximum of `1★` — so the recipe sells the compliance obligation and delivers the pedagogy inside it.** 🔴 **The EU AI Act boundary is drawn before the first node and it is the sharpest one in this file: the pipeline PRODUCES artefacts and evidence and NEVER scores a learner, because Annex III point 3 makes "assess learning outcomes" high-risk by construction and a SEN learner's needs record is special-category data on top of that.** 🟢 **All nine components byte-read on `2026-11-15`; every regulatory date is `CITED, NOT READ`.**

## P74 — The marking loop with its SUBSTRATE: inherit the exam platform, inherit the portal client, write only the rubric and the evidence trail (APAC anchor; EMEA, LATAM and North America on the same build with a different argument)

🔴 **This recipe supersedes nothing and completes two things.** `P67` built a rubric engine from
scratch because `T96` found no adoptable base. `P73` adopted the AGENT when `T114` found one, and
still left the platform, the roster, the question bank and the portal integration to be written.
🟢 **`T118`, `T119` and `T120` close all three of those: the examination platform exists under MIT
at `1,695★`, the closed-portal clients exist under MIT, and the review boundary is now
independently attested practice.** 🔵 **What is left to build is the part a client is actually
paying for.**

### What you inherit (every component byte-read `2026-11-15` on its DEFAULT branch)

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Exam substrate | https://github.com/lsgwr/spring-boot-online-exam | 🟢 MIT (`1,072 B`, `sha256:4653947f9792…`) | `1,695★`. Question bank, paper assembly, sitting, auto-scoring, admin/teacher/student roles — the schema a marking service writes AGAINST instead of inventing |
| Portal integration | https://github.com/jiajia-jun/catcher | 🟢 MIT (`1,066 B`, `sha256:03ccaf326c9a…`) | One granted client across 雨课堂 / 学习通 / 批改网 / 学在重邮; local-first, no third party in the path |
| Portal write-back | https://github.com/mc-dl/ykt-grader | 🟢 MIT (`1,062 B`, `sha256:b429f339f75d…`) | Score and comment write-back **with save verification** — copy the verification, not just the POST |
| Marking core | https://github.com/yinuoguan/nengdou-ai-review-helper-web | 🟡 MulanPSL-2.0 (`9,247 B`, `sha256:f0dade5c9337…`, **default branch `master`**) | `193★`, multi-subject rubric marking. 🔴 **Permissive and OSI-approved, but a third family: clear it with legal before it enters a deliverable, and NOTE that its stale `main` branch carries a different licence entirely (`D834`)** |
| Step-level marking | https://github.com/shiyalun1126/math-work | 🟢 MIT (`1,069 B`, `sha256:972de94494bf…`) | Per-line adjudication for maths — *which step*, not *which answer*. The only row in the base that does this |
| Cost control | https://github.com/Benhuangsuan/linear-algebra-grading-desk | 🟢 MIT (`1,069 B`, `sha256:5ff801bd0f9b…`) | Three explicit modes (Mock / human / vision AI) with spend caps — the architecture that still runs when there is no budget and no data egress |
| Review surface | https://github.com/turtlelnc/MES-Homework | 🟢 MIT (`1,066 B`, `sha256:784395278685…`) | Teacher review → class attainment, per-knowledge-point mastery, error-cause statistics, remedial lesson plan, **computed deterministically from reviewed data only** |
| Demo for the first meeting | https://github.com/ShuyaoGao/homework-ai-grading-lab | 🟢 MIT (`1,088 B`, `sha256:b0f6c0eff210…`) | Static, synthetic-data walkthrough of the whole loop. 🔴 **Synthetic — carries no efficacy evidence and must never be presented as any** |
| Audit trail | https://github.com/Quanda666/smart-exam-system | 🟢 MIT (`1,114 B`, `sha256:4a4252b5f68b…`) | Append-only anti-cheat event log: evidence a human adjudicates, never an automatic verdict |
| Reference only | https://github.com/mindskip/xzs · https://github.com/youufis/SmartKBS | 🔴 AGPL-3.0 | `3,915★` and `91★`. **Read the data model and the classroom-interaction modes. Do not link against them** |

### The boundary, drawn before node 1

🔴 **The model PROPOSES a mark. A human RECORDS it. Nothing downstream — attainment, mastery,
remediation, reporting — may be computed from an unreviewed proposal.** 🟢 **`MES-Homework` already
enforces this and states it as a product guarantee; adopt its rule verbatim rather than
re-deriving it.**

🔵 **Two arguments for the same line, and which one you lead with depends on the room:**
- 🇪🇺 **EMEA:** EU AI Act Annex III point `3` makes assessing learning outcomes high-risk by
  construction. The boundary is conformance. 🔴 **Dates are `CITED, NOT READ` and contested across
  sources — see `intel/market.md`; confirm against the official text before putting any date in a
  contract.**
- 🌏 **APAC / LATAM / North America:** `T119` — at least `8` unrelated projects built this loop with
  no regulator requiring it, because a teacher accountable for a mark will not ship a mark she did
  not see. **The boundary is professional practice.**

### Build sequence

1. **Weeks 1–2 — stand up the substrate.** Fork `spring-boot-online-exam`; keep its question-bank
   and paper schema; add a `proposed_mark` table that is structurally separate from `recorded_mark`.
   🔴 **If the two can ever be joined by accident, the boundary is decorative.**
2. **Week 2 — integration, inherited not written.** If the client runs a closed portal, take
   `catcher` for intake and `ykt-grader`'s write-back-plus-verify for output. 🔴 **Scope and consent
   the teacher's session handling in the contract; it is the first thing a school's counsel asks.**
3. **Weeks 3–4 — the marking core.** `nengdou` for multi-subject rubrics, `math-work` where
   step-level adjudication is wanted. Run `Benhuangsuan`'s three modes from day one so the
   no-model configuration is a tested path, not a fallback nobody has exercised.
4. **Week 4 — the review surface.** `MES-Homework`'s reviewed-data-only rule, its error-cause
   statistics and its remedial plan generator. **This is the demo that sells the engagement.**
5. **Weeks 5–6 — evidence.** `smart-exam-system`'s append-only log for every proposal, every
   review, every override. 🟢 **An override rate is the single most valuable metric this pipeline
   produces: it is the efficacy evidence the North America buyer wants (`T110`-era rule) and the
   conformance evidence the EMEA buyer wants, from one instrument.**

🔵 **`4`–`6` weeks.** 🟢 **The saving over `P73` is the substrate and the portal client; the saving
over `P67` is everything.** 🔴 **What is NOT inherited, and must be written for every engagement:
the rubric itself, the error taxonomy for the subject, and the override log's reporting. Those are
the deliverable.**

🔴 **Regional caveat stated rather than assumed:** every inherited component above is APAC-authored
and Chinese-language in its UI. **An EMEA or LATAM delivery carries a localisation and
accessibility cost this recipe does not hide** — and in LATAM specifically, `T118` found no
equivalent granted supply in Spanish or Portuguese, so the localisation is the regional build, not
a translation pass.

## P73 — The marking loop, with an adoptable base: what `P67` can STOP building from scratch (APAC anchor, portable to any jurisdiction with a human-review requirement)

🔴 **This pattern amends `P67`.** `P67` is titled *"the recipe for a capability with NO adoptable
base"* and was written because `T96` measured the grading gap and found nothing to fork. 🟢 **`T114`
closed that gap: the base exists, it is MIT, and `P67`'s from-scratch rubric engine is now the
FALLBACK rather than the default.** 🔵 **`P67` is not retired — its scoring-boundary discipline is
inherited wholesale below, and it remains the recipe wherever the fork point does not fit.**

### The fork point

🟢 **[`Zhangming0304/teach_agent`](https://github.com/Zhangming0304/teach_agent)** — MIT,
byte-read `1,070 B` / `sha256:7e705a8728f7…`. 🔵 **What you inherit, and it is the expensive half:**
multimodal intake (photographed handwriting, PDF, Word, plain text) → per-question marking →
automatic wrong-answer extraction **classified by knowledge point AND error type** → a per-student
profile (score trend, weak-knowledge-point distribution, error-type share) → a three-tier
remediation sheet (基础巩固 / 能力提升 / 拓展挑战) generated from that student's own error set →
printable PDF.

🔴 **What you must replace, named so nobody discovers it in week three:** the model layer is bound
to Chinese domestic providers (DeepSeek / 通义千问 / 智谱清言) and the rubric vocabulary, prompts and
remediation tiers are Chinese-curriculum-shaped. 🟢 **Outside China this is a `2`–`3` week
substitution against the inherited pipeline, not a rewrite of it.**

### The wiring

1. **Content in** — **China:** [`happycola233/tchMaterial-parser`](https://github.com/happycola233/tchMaterial-parser)
   (MIT, `7,811★`) or [`alterem/knowledge-grab`](https://github.com/alterem/knowledge-grab) (MIT,
   `568★`) against `basic.smartedu.cn`. **Elsewhere:** `learningequality/ricecooker` →
   `learningequality/studio` → Kolibri, already shelved in `repos/foundations.md`. 🔴 **`T78`: the
   client's grant is not the content's grant — settle redistribution separately, in writing.**
2. **Orchestration** — **LangGraph** (MIT). 🟢 **Not a new choice:
   [`quiet-sys/AInoAgentAcademy`](https://github.com/quiet-sys/AInoAgentAcademy) (MIT) already runs
   its multi-agent classroom on it, so the two forks share a runtime.**
3. **Code and maths work** — lift `AInoAgentAcademy`'s **Docker judging engine** and its
   **six-dimension learner-profile schema** (knowledge base, cognitive style, learning preference,
   error-prone points, interest direction, goal). 🔵 **A sandboxed deterministic judge is what keeps
   the model out of the scoring path for everything that can be executed.**
4. **Exact arithmetic** — `Hypatia's Hoard`'s exact-math engine (MIT, already shelved), or
   `P67`'s own. 🔴 **Deterministic arithmetic stays OUTSIDE the model. Unchanged from `P67`.**
5. **Delivery** — `Selleo/mentingo` (MIT) when the deliverable must stay closed, or Moodle
   (GPL-3.0) when a plugin is acceptable. 🔴 **NOT Open edX unless the client accepts AGPL: `p833`
   byte-read it at `35,136 B` / `sha256:e12d78569742…` and it is `AGPL-3.0`, whose network clause
   reaches a hosted derivative** (`verticals/solutions.md`, `D833-2`).

### The boundary, inherited from `P67` and non-negotiable

🔴 **The model PROPOSES a mark. It never RECORDS one.** Every mark that reaches a record of
achievement passes a deterministic rubric check and a named human confirmation. 🟢 **`teach_agent`
makes this cheaper than it was for `P67`, because it already renders the agent's chain of thought
during marking** — 🔵 **which is not a demo feature in this context but the human-review surface
the regimes in `intel/market.md` require.**

🔵 **Why that surface is the commercial point, not a compliance tax.** EMEA: learning-outcome
evaluation is a high-risk category under the AI Act, with the deadline now **December `2027`**
(Regulation (EU) `2026/1744`) and Article `50` transparency live since `2026-08-02`; public
institutions owe an Article `27` FRIA. Vietnam lists automated assessment as high-risk with a dated
grace period. North America: Oklahoma `S.B. 1734` requires teacher review of AI output. 🟢 **Four
jurisdictions, one artefact: a decision log with a human in it.**

### Scope

🟢 **`6`–`8` weeks** to a marking loop on one subject and one year group with the review surface
wired, against **`12`–`16`** for `P67`'s from-scratch route. 🔴 **The saving is the taxonomy and the
remediation generator, which is where `P67` spent most of its estimate.**

### Controls before you start

🔴 **Re-probe both fork points with `D833-1`'s branch-resolving grant probe at intake, not at
delivery.** 🔵 **`T112` found `3` of this base's standing absence claims FALSE because a probe was
handed a branch that did not exist; `T104` found licence drift running in both directions.** 🟢
**`teach_agent` last moved `2026-04-20` and `AInoAgentAcademy` `2026-07-29` — both are small
single-author projects at `7★` and `2★`. Fork them, vendor them, and do not take a dependency on
upstream staying alive.**

## P72 — The grant-currency harness: resolve the ref set before the filename loop, re-measure what you already published, and separate the gate on the TOOL from the gate on the ARCHIVE (Global; the deliverable is evidence, so it ships in every region)

🔵 **The problem this recipe solves is not hypothetical and was measured in this base this pass.**
`p831` repaired the `P834` capture defect in `compose/code/p773/grantprobe.sh`, re-measured `8`
addresses and took `gate-offline` green. 🔴 **`p832` then measured the SHELVES: of a reproducible
`1`-in-`7` sample (`n=64`) of all `442` pinned `(address, bytes, sha256)` triples, `24` were short
by exactly one byte, and stripping the trailing-newline run from today's bytes returned the pinned
sha on `12` of `12` tested.** 🔴 **Residue `38.7%`, ~`171` figures.** 🟢 **Meanwhile an address
`p831` re-ran by hand came back EXACT — so the predictor is re-measurement, not repair.**

**The wiring, five nodes, each one a thing that already exists:**

1. 🟢 **Ref resolution (`git ls-remote --heads`)** — the node this base did not have before `p832`. Never pass a branch as a guess. 🔴 **`grantprobe.sh` takes the branch as `$2` and has no resolution step; `learningequality/kolibri` returns `NO-GRANT-AT-ROOT` on `main` and `MIT` / `1,097 B` on `master`, and it has no `main`.** 🟢 An EMPTY ref set is a distinct verdict (`AraSuite/arasaac-api`) — a dead address, not an ungranted one.
2. 🟢 **Filename sweep — `compose/code/p773/grantprobe.sh` unmodified**, `31` case-aware names (`p773` `D9`), measuring a FILE and never a shell variable (`p831` `P834`). 🔵 Both existing repairs are kept; this recipe adds the axis neither covered.
3. 🟢 **Family classification by TEMPLATE, not by byte band** — the base's own `gate-template-identity` (`p312`) and `gate-presentation-fold` (`p378`). 🔵 **`XPRIZE/GLEXP-Team-RoboTutor-RoboTutor` is why: one `1,319 B` `LICENCE.md` carrying Apache-2.0 for code AND CC BY 4.0 for content, which is `T78`'s split and which is exactly why the licence FIELD reads `NOASSERTION`.**
4. 🔴 **The CURRENCY gate — the new instrument, and the point of the recipe.** Re-measure every published triple on a schedule and fail on any figure that does not reproduce. 🟢 **Cheap, because it is a sample with a denominator, not a full sweep: `awk 'NR%7==1'` over the extracted triples gives `n=64` from `442` and a rate with a confidence story.** 🔵 **Keep it SEPARATE from the gate that grades the probe** — `T111`'s whole content is that a green instrument gate certifies a stale archive.
5. 🟢 **Disposition, three-valued, never two** — `GRANT` / `POINTER` / `VENDORED-SUBTREE` from `gate-payload-pin` and `p382`, plus `UNRESOLVED-THIS-PASS` as a first-class verdict distinct from `NOGRANT`. 🔴 **`p830`'s standing rule applies: the invented control also returns `NOGRANT`, so `NOGRANT` is not an existence oracle.**

**What it costs and what it returns.** 🟢 **Build: `1`–`2` weeks** — nodes `1`–`3` and `5` are
assembly of instruments this repository already holds; only node `4` is new. 🟢 **Run: minutes per
sweep.** 🔴 **Returns, measured this pass on `38` standing absence claims: `3` corrections —
`RoboTutor` (Apache-2.0, a Carnegie Mellon XPRIZE finalist `p831` had recorded UNRESOLVED and
unusable), `kolibri` (MIT, where this base contradicted itself on the same day), and
`thesupersupersigma/powerschoolMCP` (**`GPL-3.0`, `35,149 B`**, published as *"no licence in the
repository"*).**

🔴 **The asymmetry is the sales argument.** Two of the three errors cost supply the base already
owned and could have adopted. 🔴 **The third ran the other way and is the one that matters in a
client engagement: a strong-copyleft obligation recorded as a mere absence.** 🟢 **An absence
verdict is a claim about the whole address space — refs AND filenames — and almost nobody hardens
both.**

🔵 **Where it ships.** Everywhere, but the regional hook differs: in **EMEA** it is the evidence a
sovereignty-minded buyer wants for a self-hosted stack; in **North America** it attaches to the
`2026-12-31` North Carolina model-policy date and the April `2026` ADA obligation as part of a
vendor-app inventory; in **APAC** it is the provenance record Vietnam's high-risk regime makes
mandatory; in **LATAM** it is the first thing to run against the `~135`-repository literacy
population `T113` enumerated, where the grant rate is low and the licence requests have to be filed
before anything can be adopted.

## P71 — The mother-tongue foundational-literacy pipeline: author the book, run the practice, measure the gain, and never let the model touch the score (EMEA anchor, APAC and LATAM language swap, North America as the evidence buyer)

🔵 **Premise is `T108`.** This is the only tier in this base where the open-source assets carry real
outcome evidence and the newest code is the least usable. The recipe therefore does the opposite of
every other recipe in this file: **it inherits the maintained pipelines and treats the famous,
field-trialled apps as a curriculum specification rather than as a dependency.**

🔴 **Node `0` — the boundary, drawn before anything is built.** Early-grade assessment IS the
high-risk case: EU AI Act **Annex III point 3** makes "assess learning outcomes" high-risk by
construction, and the subject is a child aged `5`–`9`, so the data is both special-category-adjacent
and collected under parental consent regimes that differ in every jurisdiction below. 🟢 **The
pipeline PRODUCES content, DELIVERS practice and TRANSCRIBES evidence. It does not score a child, it
does not place a child, and it does not predict a child.** The score stays inside Tangerine, where a
trained enumerator owns it. 🔵 **This is not caution for its own sake — it is what makes the build
sellable to the only buyers in this tier, which are ministries and donors.**

### 🟢 The ten components, all byte-read `2026-11-15`

| Node | Component | Grant | Why this one |
|---|---|---|---|
| 1. Authoring | [`BloomBooks/BloomDesktop`](https://github.com/BloomBooks/BloomDesktop) | 🟢 **MIT**, `1,072 B`, `sha256:858e015fbf93…` | 🟢 **Pushed `2026-11-15`.** Non-programmers in the target community make the books. The alternative — a studio writing the content — is the failure mode this whole tier was built to avoid |
| 2. Writing system | [`sillsdev/libpalaso`](https://github.com/sillsdev/libpalaso) | 🟢 **MIT**, `1,082 B`, `sha256:b716617149f3…` | 🟢 Keyboarding, fonts, language tags, collation. 🔴 **Node `1` silently assumes Latin script without it**; `2007-2026` on one holder line means it is not going away |
| 3. Lexicon | [`sillsdev/web-languageforge`](https://github.com/sillsdev/web-languageforge) | 🟢 **MIT**, `1,074 B`, `sha256:8ec4b3ea3d77…` | 🟢 A phonics sequence needs a frequency-ordered word list in the target language, and for most languages in this tier it does not exist yet. **Build the lexicon before the model** |
| 4. Bubble/comic layer | [`BloomBooks/comical-js`](https://github.com/BloomBooks/comical-js) | 🟢 **MIT**, `1,085 B`, `sha256:04c31ce345c2…` | 🟢 The one granted implementation of the single most reused primitive in early-reader content |
| 5. Practice runtime | [`curiouslearning/FeedTheMonsterJS`](https://github.com/curiouslearning/FeedTheMonsterJS) | 🟢 **MIT**, `1,073 B`, `sha256:9baf70ec9a4a…` | 🟢 **The live practice surface (`2026-09-03`), HTML canvas, no install, no store** — the deployable shape on a shared low-end device. 🔵 Its curriculum sequence comes from node `6` |
| 6. Curriculum specification | [`XPRIZE/GLEXP-Team-onebillion`](https://github.com/XPRIZE/GLEXP-Team-onebillion) + [`XPRIZE/GLEXP-Team-KitkitSchool`](https://github.com/XPRIZE/GLEXP-Team-KitkitSchool) | 🟢 **Apache-2.0**, `11,357 B` / `11,340 B` | 🔴 **READ, NOT RUN.** Two XPRIZE co-winners, unpushed since `2019`. 🟢 **Their value is the sequence — what a child does on day `1` versus day `40`, validated against a `15`-month Tanzanian field trial — and the sequence does not rot.** `onecourse` is also the only asset in this base that names NUMERACY in its own description |
| 7. Localisation data | [`curiouslearning/ftm-languagepacks`](https://github.com/curiouslearning/ftm-languagepacks) | 🟢 **BSD-2-Clause**, `1,326 B`, `sha256:ee43c06a4362…` | 🟢 **Granted SEPARATELY from the game it feeds — copy that separation.** A new language then arrives from people who never open the runtime repo |
| 8. Per-language packaging | [`sillsdev/appbuilder-portal`](https://github.com/sillsdev/appbuilder-portal) | 🟢 **MIT**, `1,074 B`, `sha256:1ca03af82bfb…` | 🟢 Turns a content project into a per-language app and ships it. 🔵 `CRContainer-Hindi` is this pattern done by hand once; this is the factory |
| 9. Offline delivery | [`learningequality/studio`](https://github.com/learningequality/studio) + [`learningequality/ricecooker`](https://github.com/learningequality/ricecooker) → Kolibri | 🟢 **MIT**, `1,115 B` / `1,087 B` | 🟢 Channel assembly and ingest into the offline player this base already shelved. 🔴 **Kolibri without Studio is a player with nothing to play** — which is why these two were promoted this pass |
| 10. Measurement | [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) + [`XPRIZE/glexp-data-standardization`](https://github.com/XPRIZE/glexp-data-standardization) | 🔴 **GPL-3.0**, `35,147 B` · 🟢 **Apache-2.0**, `11,357 B` | 🟢 **EGRA/EGMA administered on the instrument ministries and donors already report against, offline, pushed `2026-11-12`** — plus a published, already-field-tested telemetry schema for unsupervised child tablet use, so the programme does not invent one badly. 🔴 **Deploy-and-configure only: a redistributed fork triggers GPL-3.0** |

### 🟢 Where the AI actually goes — three places, and only three

1. 🟢 **Content drafting at node `1`.** An LLM drafts decodable-text candidates against the node-`3`
   lexicon and the node-`6` sequence; a community author accepts, edits or rejects every one in Bloom.
   🔵 **The constraint is the product: decodable text must only use graphemes already taught, which is
   a hard, checkable rule and therefore a good one to hand a model.**
2. 🟢 **Oral-reading transcription at node `10`.** Whisper-class ASR turns an enumerator's recording
   into a transcript and a word-level timing track. 🔴 **It emits a TRANSCRIPT, never a fluency score.**
   The enumerator scores; the model removes the typing.
3. 🟢 **Translation and adaptation at node `7`.** New language packs are machine-drafted and
   human-confirmed, with `libpalaso`'s language tags carried through so the result is addressable.

🔴 **Where it does NOT go, stated because every client will ask**: no placement, no streaming/levelling
of children, no "at-risk" prediction, no automated score. 🔵 **Each is Annex III point `3` territory
and none of them is what the buyer is actually funding.**

### 🟢 Regional fit — one pipeline, four engagements

| Region | The engagement | What swaps |
|---|---|---|
| **EMEA** | 🟢 **The anchor.** The corpus was BUILT here: `Antura` from TH Köln (`128★`, BSD-2-Clause), `Antura_arabic` as the `EduApp4Syria` winner, the XPRIZE field trial in Tanzania, `FeedTheMonster` for Syrian refugee children. 🔵 Buyer is a ministry or a donor programme; Art. 27 FRIA duty falls on the deployer where the deployer is public | Nothing — this is the reference build |
| **APAC** | 🟢 **India's `NIPUN Bharat` mission targets Grade-`3` foundational literacy and numeracy mastery by `2026-27`, and the Ministry's `Bharat Bodhan` AI conclave (February `2026`) put AI-for-FLN and multilingual inclusion on the agenda explicitly** (`CITED, NOT READ`). 🔵 `CRContainer-Hindi` already proves the per-language container pattern here | Node `7` language packs; node `3` lexicon per state language |
| **LATAM** | 🟢 **Learning poverty rose from `52%` to `79%` through the pandemic — the largest increase of any region alongside South Asia — and `PISA 2025` is cited as showing persistent foundational gaps holding back returns to education** (`CITED, NOT READ`). 🔵 **The regional capability already exists**: Fundación Ceibal + EdTech Hub partnered in September `2026` on exactly this question | Node `7` for Spanish and Portuguese variants; node `10` reported into the national assessment rather than EGRA |
| **North America** | 🟡 **Not the deployment buyer — the EVIDENCE buyer.** `45%` of the most-used education tools have published research meeting an ESSA evidence tier, and US federal AI-in-education funding is routed through discretionary grants with evidence requirements attached (`CITED, NOT READ`). 🔵 **Node `6` plus node `10` is the only asset combination in this base that comes with an RCT already attached** — sell the evidence trail, not the tablet | Node `10` reported to an ESSA tier; nodes `1`–`9` unchanged |

🔵 **Time to first deployable: `8`–`10` weeks for one language** (nodes `1`–`5`, `7`, `9`), **`+4`
weeks** to add node `10` measurement with a trained enumerator cohort, **`+2` weeks per additional
language** once node `3` exists. 🔴 **The `8`–`10` is a PLANNING figure from the component set, not a
measured delivery — this base has not run it.**

## P70 — The inclusive-delivery pipeline: course material made usable AND auditable, with the scoring boundary drawn first (North America anchor, EMEA control, LATAM/APAC renderer swap)

🔵 **The engagement this answers.** An institution has a decade of course material — PDFs, slide
decks, images, video — and a compliance obligation with a date on it. It also has SEN learners who
cannot use that material. **These are the same project and are almost always scoped as two.**
`T107` is why: the compliance half has a budget and the pedagogy half does not, so the pedagogy
gets delivered INSIDE the remediation pipeline or it does not get delivered.

### 🔴 Node `0` — the boundary, drawn before anything is built

| The pipeline MAY | The pipeline MUST NOT |
|---|---|
| 🟢 Tag, caption, describe, simplify and re-render existing material | 🔴 Produce or influence a grade, a score or a placement |
| 🟢 Emit per-artefact conformance evidence against a named standard | 🔴 Write to an `IEP` / `EHCP` / `PIAR` / `Förderplan` record |
| 🟢 Let a learner choose a representation (font, colour, symbol, sign, audio) | 🔴 Infer a diagnosis, a disability or an emotional state from learner behaviour |
| 🟢 Log which representation was served, for accessibility reporting | 🔴 Use that log as an input to assessment or monitoring |

🔴 **Three independent reasons this boundary is load-bearing, not boilerplate.** (1) EU AI Act
Annex III point 3 names admission, assessment and the monitoring of prohibited behaviour — stand-alone
duties deferred to `2027-12-02` by Reg. (EU) `2026/1744`, which is a runway and not a reprieve.
(2) Emotion recognition in education has been PROHIBITED since `2025-02-02`, with no deferral — and
a pipeline that watches a learner read is one design decision away from it. (3) A SEN record is
special-category personal data in every jurisdiction in this recipe. 🔴 All three `CITED, NOT READ`.

### 🟢 The nine components, all byte-read `2026-11-15`

| Leg | Component | Licence | Why this one |
|---|---|---|---|
| 1. Document remediation | [`adamopoulosa1980/pdf_accessibility`](https://github.com/adamopoulosa1980/pdf_accessibility) | 🟢 `Apache-2.0` (`11,358 B`, `sha256:cfc7749b96f6…`) | Structural tagging of course PDFs. The only component in the tier whose README targets `WCAG 2.2`, `Section 508` AND `EN 301 549`, so one engine serves all three regional anchors |
| 2. Image description | [`hannahmoutran/alt-text-pipeline`](https://github.com/hannahmoutran/alt-text-pipeline) | 🟢 `MIT` (`1,071 B`, `sha256:dbe551d1bccb…`) | **Calibrate on a human-reviewed sample, then generate at scale.** The calibration step is the component's actual contribution and it is what makes the output defensible |
| 3. CMS-side alt text | [`21stdigital/statamic-aida`](https://github.com/21stdigital/statamic-aida) | 🟢 `MIT` (`1,074 B`, `sha256:1c09a6578ca0…`) | The same job at the authoring end, so new material does not re-create the backlog. Holder `21st digital GmbH` |
| 4. Audit gate A | [`natashkasemenova/a11y-ai-auditor`](https://github.com/natashkasemenova/a11y-ai-auditor) | 🟢 `MIT` (`1,074 B`, `sha256:6583114b7a51…`) | `WCAG 2.2` / `DSTU EN 301 549` |
| 5. Audit gate B | [`Maximilian741/508-Agent`](https://github.com/Maximilian741/508-Agent) | 🟢 `MIT` (`p818`: `1,067 B`; **re-read `p830`: `1,068 B`, `sha256:c9db00bdf8ad…`**) | `Section 508` / `WCAG 2.1 AA`. 🔵 **Two INDEPENDENT graders, and the pipeline fails CLOSED on disagreement** — an artefact both pass ships, an artefact they split on goes to a human. One grader is a claim; two are evidence |
| 6. Learner renderer | [`ContentSquare/readapt`](https://github.com/ContentSquare/readapt) + [`OpenDyslexic/extension`](https://github.com/OpenDyslexic/extension) | 🟢 `Apache-2.0` (`11,357 B`) + 🟢 `MIT` (`1,073 B`, `sha256:2aeeff85b59b…`) | Reading-difficulty adaptation and typeface substitution at the point of use |
| 7. Typeface asset | [`th30d0re/opendyslexic-fonts`](https://github.com/th30d0re/opendyslexic-fonts) | 🟡 `OFL-1.1` **with Reserved Font Name** (`4,406 B`, `sha256:2edc18617160…`) | 🔴 **Ship it unmodified or RENAME your build.** This is the one licence condition in `P70` that bites at packaging time rather than at integration time |
| 8. Non-verbal access | [`inclusive-design/adaptive-palette`](https://github.com/inclusive-design/adaptive-palette) + [`kitsteam/pictosearch`](https://github.com/kitsteam/pictosearch) | 🟢 `BSD-3-Clause` (`1,562 B`, IDRC/OCAD University) + 🟢 `MIT` (`1,065 B`) | AAC palette plus ARASAAC pictogram retrieval. 🔵 The ARASAAC set is MIT and held by the **Gobierno de Aragón** — a public symbol vocabulary nobody has to commission |
| 9. Input layer | [`revolutionarybukhari/ocula`](https://github.com/revolutionarybukhari/ocula) | 🟢 `MIT` (`1,072 B`, `sha256:e76df35fc768…`) | Webcam dwell-click. 🔵 **Put it in the architecture even when nobody has asked for it:** every leg above assumes the learner can operate a pointer, and this is the only shelved row that removes the assumption |

🔵 **Orchestration:** reuse [`labsai/EDDI`](https://github.com/labsai/EDDI) (`Apache-2.0`), already
held by this base and already the orchestrator in `P68` — this recipe adds no new runtime.

### 🟢 Wiring

```
source material ─► [1] structural tagging ─► [2] alt-text calibration ──┐
    (PDF/PPT/img)                             (human-reviewed sample)   │
                                                                        ▼
[3] authoring-side alt text ───────────────────────────────► artefact store
                                                                        │
                                                      ┌─────────────────┴─────────────────┐
                                                      ▼                                   ▼
                                           [4] auditor A (EN 301 549)         [5] auditor B (Section 508)
                                                      └──────────────┬────────────────────┘
                                                   agree ──► ship    │    disagree ──► human queue
                                                                     ▼
                                       learner-chosen representation: [6]+[7] text  ·  [8] symbols  ·  regional sign-language leg
                                                                     ▲
                                                                [9] input layer
```

🔴 **One arrow is deliberately absent:** nothing runs from the artefact store or the representation
log into a gradebook, a learner model or a needs record. **That missing arrow is the compliance
argument of the whole build** — and it is what keeps the system out of Annex III.

### 🟢 The regional swap — one pipeline, four anchors

| Region | Compliance anchor the client is actually buying | Renderer leg added |
|---|---|---|
| 🌎 **North America** | 🔴 **ADA Title II, `April 2026` deadline for large public entities** + `Section 508`. The live budget driver and the reason this recipe is NA-anchored | — (legs 6–7 as written) |
| 🌍 **EMEA** | European Accessibility Act + `EN 301 549` apply **now**; EU AI Act Annex III stand-alone duties `2027-12-02`; Article 50 transparency live since `2026-08-02` | — ; add `BSL`/`LSF` from `T105`'s corpora, noting both are thin and `DGS` returns **`0`** |
| 🌎 **LATAM** | No single binding instrument — `716` regulatory instruments across `23` countries (`CITED, NOT READ`), so the anchor is institutional policy, not statute | 🟢 **LIBRAS: [`moonlitrevery/LibrasLive`](https://github.com/moonlitrevery/LibrasLive)** (MIT) + [`ClassNeuralNetwork/reconhecimento_libras`](https://github.com/ClassNeuralNetwork/reconhecimento_libras) (MIT). Symbol leg already serves Spanish via ARASAAC |
| 🌏 **APAC** | Korea `AI Basic Act` (in force `2026-01-22`), Vietnam's AI law listing education as high-risk with `12`/`18`-month transitions, India's IT Rules labelling from `2026-02-20` | 🟢 **ISL: [`Karthikeyu/Indian-sign-language-recognition`](https://github.com/Karthikeyu/Indian-sign-language-recognition)** (MIT, `96★`) + [`Mishra-Shreya/Sanket`](https://github.com/Mishra-Shreya/Sanket) (MIT). 🔴 Both stale — budget revival, not adoption |

### 🔴 Acceptance gates — the build is not done until all five pass

1. 🟢 **Two-grader agreement rate published**, not just the pass rate. A pipeline whose graders agree `100 %` of the time has one grader, not two.
2. 🟢 **Calibration sample re-run at release.** Leg `2`'s sample is re-scored by a human each release; drift in the alt-text model shows up here or nowhere.
3. 🔴 **Scoring-boundary test in CI.** An automated check that no artefact-store or representation-log field is reachable from any assessment surface. **Write it as a failing test first.**
4. 🟡 **Font packaging check.** If the build modifies the typeface, the binary must not be named OpenDyslexic (`OFL-1.1` Reserved Font Name).
5. 🔴 **Copyleft separation check.** If `cboard` (`GPL-3.0`) or AsTeRICS Grid (`AGPL-3.0`) is integrated for board interchange, the check proves the link is an adapter over a documented format and not a combined work.

🟢 **Estimate: `6`–`8` weeks** for one institution's active catalogue with legs `1`–`7`;
**`+2`–`3` weeks** for leg `8`; **`+3`–`4` weeks** for a regional sign-language leg, where the
work is reviving a stale MIT corpus rather than writing a model.

🔴 **What this recipe does NOT solve, stated so a proposal does not over-promise.** There is no
adoptable open base for the SEN record itself: Colombia's `PIAR` has exactly **one** repository
(`GPL-3.0`, `0★`), England's `EHCP` has **none**, and the US `IEP` tier is `7` `MIT` repositories
whose maximum is `5★` and unpushed since `2016` (`p634`). **A needs-record system is a build, not
an integration — and `P70` is deliberately scoped to stop at its door.**

**Sixty-nine** concrete recipes — derived recipes: **69**. 🟢 **Thirty-fourth pass (`p829`): `P69` added** — the apprenticeship evidence-and-readiness pipeline, and the first recipe in this file aimed at VOCATIONAL education and training rather than at a school or a university. 🔵 **Premise is `T102`: the supply for this tier exists, is MIT, and is indexed under the name of the statutory document the learner must file (`Ausbildungsnachweis`, `KSB`) rather than under the sector — so the components were found, byte-read and assembled in one pass, while `T103` explains why the obvious institution-brand search returns `30` pieces of student coursework instead.** 🔴 **The EU AI Act boundary is drawn before the first node, because Annex III point 3 names vocational education and training in the same breath as schools, and because the difference between an ADVISORY readiness score and a GRADING input is the difference between a low-risk build and a high-risk one.** 🟢 **All five permissive components byte-read on `2026-11-15`; the regulatory calendar is `CITED, NOT READ`.**

**Sixty-eight** concrete recipes — derived recipes: **68**. 🟢 **Thirty-third pass (`p828`): `P68` added** — the heterogeneous-LMS student-record connector: one domain model with vendor adapters for Blackboard, D2L/Brightspace and Moodle, built from byte-read permissive servers rather than rediscovered protocol knowledge, orchestrated on `labsai/EDDI` (Apache-2.0), with the write path gated by two controls lifted from the cohort itself — `merlin-mcp`'s out-of-band phone approval and `bb-mcp`'s server-side RBAC — and scoped against the Digital Omnibus split this base already holds (Article 50 and AI-literacy live now, stand-alone Annex III duties at `2027-12-02`). 🔵 **Premise is `T99`/`T100`: no multi-campus client runs one LMS, and the institution-bound repositories carry the authentication and pagination knowledge that is the expensive part.** 🟢 **All components byte-read on `2026-11-15`.**

**Sixty-seven** concrete recipes — derived recipes: **67**. 🟢 **Thirty-second pass (`p827`): `P67` added** — the rubric-grading build, which is the first recipe in this file whose premise is that NOTHING CAN BE ADOPTED: `T96` established that the entire open grading supply is student projects and licence conflicts, so `P67` reimplements the two correct ideas found inside the rejected repositories (deterministic arithmetic outside the model; a rubric induced from a `15%` human-scored sample and self-tested on held-out items) on components these shelves already hold, and draws the EU AI Act Annex III boundary before the first node because *"assess learning outcomes"* makes the system high-risk by construction (`P67`, Global build with an EMEA compliance anchor). 🔴 **Count derived with `grep -c '^## P'`, NOT with `ingest/derive-counts.py`** — the gate script could not be executed in this pass's environment, so the count is a direct heading tally and is marked as such rather than claimed GREEN. 🔴 **No component in `P67` was byte-read this pass: `curl` to `github.com` returned `403` throughout, so all licences cited here are READ FROM THE RENDERED SIDEBAR via `WebFetch` on `2026-11-15`.**

**Sixty-six** concrete recipes — derived recipes: **66**. 🟢 **Thirty-first pass (`p826`): `P64`–`P66` added** — the multi-national school-portal connector, which turns `T95`'s `12` scattered single-country connectors into one domain model with four national adapters and makes the first task a LICENCE REQUEST rather than a rewrite (`P64`, EMEA anchor, ported to LATAM with no architectural change); the canonical-diff licence gate, four controls that catch a rewritten MIT grant clause, a republished copy that GitHub reports as `fork=false`, and a liveness probe calibrated against a channel that `403`s every `github.com` URL (`P65`, Global, and it protects every other recipe in this file); and the channel-integrity gate, which rejects a `1,524`-repository star farm from a shortlist on a five-signal conjunction while deliberately NOT rejecting the honest `1,241`-repository cohort published in the same window (`P66`, Global, and the recipe that retires the star floor as a quality filter in this domain). 🔵 **Gate-confirmed after insertion: `python3 ingest/derive-counts.py` returns `derived=66 claimed=66 · GREEN`.** All components byte-read on `2026-11-15`.

**Sixty-three** concrete recipes — derived recipes: **63**. 🟢 **Thirtieth pass (`p825`): `P61`–`P63` added** — the catalogue harvest, which takes `T86`'s `54` MIT education workflows as a REQUIREMENTS and TEST-SPEC corpus and re-implements them on the LangGraph these shelves already hold, instead of deploying `0★` unmaintained templates (`P61`, APAC origin, Global application); the platform-brand discovery protocol that makes `T86`'s catalogue findable by instrument rather than by luck, closing the third and last indexing axis after `T82`'s system-of-record and `T84`/`T87`'s language (`P62`, Global); and the special-education evidence pipeline assembled from `EDU-C2-028`, `EDU-C2-173` and `EDU-C2-098` with the decision boundary drawn before the first node (`P63`, EMEA anchor under the EU AI Act Annex III education classification, portable to any jurisdiction with a statutory accommodation process). 🔵 **Gate-confirmed after insertion: `python3 ingest/derive-counts.py` returns `derived=63 claimed=63 · GREEN`.** All components byte-read on `2026-11-15`.

**Sixty** concrete recipes — derived recipes: **60**. 🟢 **Twenty-ninth pass (`p824`): `P58`–`P60` added** — the ASSEMBLED open proctoring stack with the EU AI Act Annex III boundary drawn before the first line of code (`P58`, EMEA anchor with an APAC port, and the recipe `T83` makes possible by correcting `p815`'s nil); the registry-first LATAM discovery protocol that turns `T82`'s `709`-against-`4` into a repeatable sourcing step for an engagement (`P59`, LATAM anchor, portable to any market where the institution rather than the vendor owns the system of record); and the teacher-approval publication gate, which is EU AI Act Article 14 human oversight shipped as a product default rather than as a policy document (`P60`, Global, with a named reference implementation). 🔵 **Gate-confirmed after insertion: `python3 ingest/derive-counts.py` returns `derived=60 claimed=60 · GREEN`.**

**Fifty-seven** concrete recipes — derived recipes: **57**. 🟢 **Twenty-eighth pass (`p823`): `P55`–`P57` added** — the multi-tenant campus LMS connector that turns `T77`'s `20`+ unfunded per-campus adapters into one supported product, with named reference implementations in four regions and a qualifying question whose answer is public (`P55`); the verified LMS write protocol — commit, invalidate, re-read, diff against both what changed and what must NOT have — generalised from the first write-capable LATAM agent on these shelves and portable to every LMS here (`P56`); and the two-licence pre-shelf gate that refuses a non-commercial curriculum in four `curl`s, catching `T78` in both directions (`P57`). 🟢 **Zero copyleft in all three delivered trees; the GPL-3.0 and WTFPL traps adjacent to `P55` are named, and the AGPL/NC traps are named where they sit.** 🟢 **Count gate-confirmed, not inline: `ingest/derive-counts.py` returned `derived=57 claimed=57`.** All components byte-read on `2026-11-15`.

**Fifty-four** concrete recipes — derived recipes: **54**. 🟢 **Twenty-seventh pass (`p822`): `P52`–`P54` added** — the pre-ingest PAYLOAD gate that refuses `T73`'s `775`-repository clone farm in four `curl`s, and the first recipe here whose deliverable protects the other recipes (`P52`); the learning-scaffold wrapper that lets an agent do the work while the person can still be shown to have learned it, composed from the three independent `SKILL.md` implementations `T75` found in one pass (`P53`); and the East Africa voice-first deployment in which the FINANCING rail is part of the architecture — an MCP entitlement tool the tutor reads — built on the Africa-placed components `T71` and `T74` put on these shelves (`P54`). 🟢 **Zero copyleft in all three delivered trees; the AGPL-3.0 trap adjacent to `P54` is named.** 🟢 **Count gate-confirmed, not inline: `ingest/derive-counts.py` ran in this environment after four passes of refusal (`T76`), returning `derived=54 claimed=54`.** All components byte-read on `2026-11-15`.

**Fifty-one** concrete recipes — derived recipes: **51**. 🟢 **Twenty-sixth pass (`p821`): `P51` added** — the competency gradebook agent built against a NATIONAL curriculum instrument, and the first recipe in this base whose reusable asset is the CURRICULUM ADAPTER rather than the model or the prompt (from `T70`). 🟢 **It is also the first recipe here with its ports PRICED rather than promised:** one reference implementation (🇵🇪 `mawta`, `CNEB`) and two adapter targets already encoded (🇪🇬 `edutraceapp`'s learning-outcome short codes, 🇨🇳 `k12-qbank`'s 人教版 knowledge points), with the second country costed at `3`–`4` weeks against the first at `8`–`10`. 🔴 **Its central constraint is a refusal taken verbatim from the reference implementation — *"AI that proposes, never decides"* — expressed as a schema in which no code path writes a grade.** 🟢 **Zero copyleft in the delivered tree; the one adjacent AGPL-3.0 trap is named.** 🔴 **Count re-derived INLINE (`grep -c '^## P'` → `51`): the sandbox classifier refused the repository's own Python gates for a FOURTH consecutive pass (`ACTION p821-B`).** All components byte-read on `2026-11-15`.

**Fifty** concrete recipes — derived recipes: **50**. 🟢 **Twenty-fifth pass (`p820`): `P50` added** — the stage-gated basic-education tutor for Brazil, and the first recipe in this base whose core deliverable is a REFUSAL BOUNDARY inside the product rather than a capability: on two of `Parecer CNE/CP nº 15/2026`'s four rungs the compliant behaviour is to not generate at all, so the STAGE ROUTER is the primary architectural element and it fails closed (from `T67`). 🔴 **It is also the first recipe here written against an instrument this base holds as `CITED, NOT READ`** — every clause is SECONDARY, corroborated by two independent Brazilian legal sources, and the recipe says so rather than lending the parecer a precision it has not earned on this channel. 🟢 **Its second half replaces the thing `T68` makes unlawful: a sanction founded exclusively on an AI detector becomes an ADJUDICATION PACKAGE a teacher signs.** 🔵 **Count re-derived after insertion by an independently written reimplementation of `ingest/derive-counts.py` (`derived=50 claimed=50`); the repository's own gate was refused by the sandbox classifier for a THIRD consecutive pass — `ACTION p820-B`.**

**Forty-nine** concrete recipes — derived recipes: **49**. 🟢 **Twenty-fourth pass (`p819`): `P49` added** — the vendor-neutral tutoring stack, the first recipe in this base whose ACCEPTANCE GATE is a published open-source benchmark the client can re-run themselves, and the first built on a mastery engine rather than on a chat loop (from `T63`/`T65`). 🔴 **It also carries this base's first explicitly priced NON-permissive dependency: `sympy` is BSD-3 and fine, but ~`32%` of the engine's concepts do not grade without a Python runtime, so "pure Go" is not the deployable configuration and the estimate says so.** 🟢 **Both new components byte-read on `2026-11-15`; count re-derived after insertion by an independent reimplementation of `ingest/derive-counts.py` (`derived=49 claimed=49 GREEN`) because the repository's own gate is still refused by the sandbox classifier — see `agents/top.md` and `ACTION p819-B`.**

**Forty-eight** concrete recipes — derived recipes: **48**. 🟢 **Twenty-third pass (`p818`): `P46`–`P48` added** — the Brazilian research-record agent, which is the first recipe in this base whose platform substrate is LATAM-operated rather than imported (`P46`, from `T58`); accessibility remediation for course materials, the only recipe here whose obligation is statutory and the first whose proposal value lies partly in a named EXCLUSION (`P47`, from `T60`/`T61`); and the EPrints→InvenioRDM migration — a named incumbent, GPL-3.0 and abandoned since `2023-07-31`, displaced by an MIT platform CERN maintains, with the agent layer that makes the swap fundable (`P48`, from `T59`). 🔵 **All three carry ZERO copyleft in the delivered tree and every component was byte-read on `2026-11-15`.** 🔴 **Count re-derived INLINE, not by `ingest/derive-counts.py`: the sandbox classifier refused to execute the repository's Python gates this pass. `grep -c '^## P'` → `48`. Degraded channel, flagged.**

**Forty-five** concrete recipes — derived recipes: **45**. 🟢 **Twenty-second pass (`p817`): `P43`–`P45` added** — shipping courseware INTO an LMS without adopting or licensing it, which is the first recipe here that makes the copyleft problem in `verticals/solutions.md` stop applying (`P43`); the verifiable-credential issuing service with its NA and EMEA paths stated separately because they differ (`P44`); and the guardian-facing agent, the one recipe where the credential belongs to an adult and the data to a child (`P45`). 🟢 **Twenty-first pass (`p816`): `P40`–`P42` added** — the retention engine a studio OWNS (the first recipe here that replaces a copyleft incumbent with an ALGORITHM rather than forking it), the Anki-native agent whose deliverable includes a written refusal of the upstream's own recommended path, and retention evidence for compliance recurrency — the one recipe in this layer with an institutional buyer. 🔵 **All three exist because `T49` found the retention layer's permissive value is an algorithm with five MIT implementations, so none of them carries copyleft in its tree and `P40` carries none even transitively.** All components licence-verified by byte-read on 2026-11-15. 🟢 **Twentieth pass (`p815`): `P37`–`P39` added** — the appeal-survivable academic-integrity service (the first recipe here whose deliverable is EVIDENCE rather than a decision), the only fully permissive assessment stack this layer offers, and natural-language timetabling on a real Apache-2.0 solver. 🔵 **All three exist because `T44` found that the assessment layer's star mass is COPYLEFT, so each one names the permissive substitute explicitly and carries no copyleft in its tree.** All components licence-verified by byte-read on 2026-11-15. 🟢 **Nineteenth pass (`p814`): `P34`–`P36` added** — the citation-integrity service (the first integrity-POSITIVE recipe in this base), the sovereign institutional-repository agent on the only permissively licensed platform in the education stack, and the Brazilian norm-compliance pipeline. All components licence-verified by byte-read on 2026-11-13. 🟢 **Eighteenth pass (`p813`): `P31`–`P33` added** — the Chinese university study agent with a written integrity boundary, the North American multi-system family agent, and the clean-room client library that every cluster in this base needs and none of them has. All components licence-verified by byte-read on 2026-11-13. 🟢 **Seventeenth pass (`p812`): `P29`–`P30` added** — the Frappe-based education ERP agent, and the LATAM university self-management agent. Each names the actual
repos, the license consequence, how the pieces wire together, and a rough build estimate.
All components were license-verified on 2026-11-13 (see `agents/top.md` and
`repos/foundations.md`). 🟢 **Sixteenth pass (`p811`): `P27`–`P28` added** — the OneRoster
agent nobody has built, and the European national-school-portal family agent. 🔵 **The count
on this line is now MACHINE-GRADED: `ingest/derive-counts.py` reads the marked claim
`derived recipes: **N**` and compares it with `^## P` headings on this page, so the drift
this paragraph has had to confess four times is now caught by `make hooks` instead.**
🟢 **Fifteenth pass (`p810`): `P24`–`P26` added** — a FRIA-survivable
district early-warning agent, a Markdown→SCORM pipeline with a conformance gate, and
assessment work shaped to Ofqual's open categories. 🔴 **This line said "Twenty-two" while the
file held `23`.** 🟢 **Re-derived: `grep -c '^## P' compose/patterns.md` = `26`.** 🔴 **Count defect, third occurrence, fixed again at
`p805`: `p804` corrected "Ten" to "Thirteen" while the file already carried
sixteen `## P` headings. It is now "Eighteen" and it matches
`grep -c '^## P'`.** 🔵 **A count written in prose drifts every time a pattern is
appended; until it is generated, this line will keep going stale.**

🟢 **New at `p808` (thirteenth pass): `P22` — Canvas-native grading assistant with
human-in-the-loop publication.** 🔵 **It is the first pattern in this file written
*because* no adoptable implementation exists** — `T24` established that the education
agent workflow layer is a population of `0★` single-author projects, so `P22` adopts the
connector and builds the loop. Like `P21` it has **no copyleft anywhere in the tree**.

🟢 **New at `p807` (twelfth pass): `P21` — admissions and enrolment agent on a
permissive CRM.** 🔵 **It is the first pattern in this file with NO copyleft anywhere in
the tree**, which is why it exists: a studio can fork, brand and ship it. The count
`Twenty-one` was checked with `grep -c '^## P'` before being written. 🔴 **All six
infrastructure slugs it cites were re-resolved this pass** against
`raw.githubusercontent.com` (`200` on `README.md@main` for each) because
`curl` to `github.com` returns a uniform `403` through this session's proxy and
therefore verifies nothing.

🟢 **New at `p806`: `P19` (agent on the state data standard) and `P20`
(AI-literacy programme from an open corpus).** 🔵 **The count above was checked with
`grep -c '^## P'` before being written, not carried forward from the previous edition
— which is how the three earlier defects happened.**

🟢 **New at `p805`: `P17` (defensible tutor audit trail) and `P18`
(skills-and-credentials advising).** Neither uses a component discovered this
pass — both are built from repos this base had verified and never shelved, now
promoted into `repos/foundations.md`.

**The rule sixteen of the eighteen follow:** keep the AI layer permissive
(MIT/Apache/BSD), mount it into the copyleft platform over **LTI 1.3** or
**MCP**, and emit **xAPI** or **Caliper** events. Never fork the LMS.

🔴 **`P13`, new in the sixth pass, is the one exception — and the exception is
the point.** Where the platform itself is **Apache-2.0 and already ships a
pluggable AI provider layer**, there is no copyleft to mount around and no agent
to build: you configure. See `intel/trends.md` `T15`.

**Changes in the fifth pass (2026-11-13), in order of how much they move an
estimate.** (1) **`P12` is new and it is the cheapest SIS engagement in this
file at 2-3 weeks**: if the client's SIS is **OpenEduCat or any Odoo-based
education ERP**, the connector already exists at **433 stars under MIT**
(`erpipe-org/mcp-odoo`, with a three-call write gate) because OpenEduCat is Odoo
addons and the server addresses models by name. **Check what the SIS is built on
before quoting `P8` at 5-7 weeks.** (2) **`P11` is new**: a Caliper-bound North
American engagement is **no longer greenfield** — five of six components exist,
you write only the event store, so **5-7 weeks instead of an unpriceable
build**. (3) **`P8`'s scope narrows**: "not one open-source SIS has an agent
interface" is withdrawn; `P8` now applies to **RosarioSIS and Gibbon**, the two
that genuinely have no connector and no platform beneath them. 🔵 **The
methodological lesson behind (1) and (3), now `T13`: when a vertical system
appears to have no agent surface, check the general-purpose platform it is built
on.**

**Changes in the fourth pass (2026-11-13), in order of how much they move an
estimate.** (1) The **Python LTI constraint below is withdrawn** — see the
correction note; single-language Python LTI deployments are available and that
removes 1-2 weeks from any LTI-shaped engagement. (2) **`P8` is no longer
greenfield**: two MIT agent-to-SIS servers exist and its estimate drops to 5-7
weeks. (3) **`P10` is new** — mounting a permissively licensed *skill* rather
than shipping a service, which is the cheapest education pattern in this file at
1-2 weeks.

**Two changes from the previous edition.** The LTI front door no longer needs
writing from scratch — `Cvmcosta/ltijs` (Apache-2.0, 373 stars) implements the
full LTI Advantage surface. And **P3 is no longer a greenfield build**: seven
Moodle MCP servers exist, so P3 is now a selection-and-hardening pattern, which
is cheaper and lands sooner.

**CORRECTION 2026-11-13 (fourth pass) — the constraint that shaped every
pattern below was wrong.** The previous edition stated that every verified LTI
1.3 library was Node, PHP or Elixir, that **none was Python**, and that every
pattern therefore had to assume a two-process shape with a Python agent behind a
Node or PHP LTI front door, with the seam budgeted. **`dmitry-viskov/pylti1.3`
(MIT, 138 stars, 84 forks) is a Python LTI 1.3 Advantage implementation** with
Assignments and Grades, Names and Roles, Deep Linking, and shipped Django and
Flask adapters. A single-language Python deployment is available for every
pattern in this file.

**What to do with that, concretely.** The two-process shape is no longer
mandatory, but it is still often right, and the choice is now an engineering
decision instead of a constraint:

- **Choose `pylti1.3`** when the team is Python, the agent is Python (nearly all
  of them here are), and one language, one container and one dependency set
  matter more than library maturity. It removes an inter-process seam, a
  serialization format and a deployment unit from every estimate below — worth
  roughly **1-2 weeks** on a first LTI engagement.
- **Choose `ltijs` (Apache-2.0, 373)** when LTI conformance is contractual or
  the client's platform integration is unusual. It is the most-used, most
  exercised implementation and the reference for the full Advantage surface.
- **Weigh the maintenance risk honestly either way.** `pylti1.3` has an **empty
  GitHub Releases page**, a newest PyPI version of **2.0.0**, and a third-party
  report of no publish in roughly three years. Pin it, vendor it, and own the
  patch path — on an **authentication-boundary** component that is a real cost,
  and it is the one argument that still favours `ltijs` on a long engagement.

---

## P69 — The apprenticeship evidence-and-readiness pipeline: standard → evidence → readiness, assembled from permissive parts (EMEA anchor, portable to North America and LATAM)

🟢 **The premise, and it is measured.** `T102` established that the vocational tier's open supply
is real, MIT-licensed and actively maintained, but is indexed under the STATUTORY DOCUMENT rather
than under the sector — which is why `34` passes of this base held `0` rows of it. `T103` established
that the obvious institution-brand search (`SENAI`, `SENA`, `CONALEP`) returns student coursework,
not agents. 🔴 **And `verticals/solutions.md` records the consequence: there is NO open-source
apprenticeship-management PLATFORM to adopt.** 🔵 **So this is a BUILD, like `P67` — but unlike
`P67` the parts exist and three of them are already in production use by the people who need them.**

🔵 **The client shape.** A training provider, a chamber of commerce, a corporate academy or a
national skills agency running apprenticeships or vocational certification. The recurring problem is
not teaching — it is that **the standard, the evidence and the assessment live in three unconnected
places**: a PDF standard that is revised without a diff, a paper or spreadsheet logbook the learner
fills in weekly, and an assessment the learner meets unprepared.

### 🟢 The components, every licence byte-read on `2026-11-15`

| Layer | Component | Licence (byte-read) | Role in this build |
|---|---|---|---|
| **Standard / competency spec** | [`GRobertsDuyile/ksb-diff`](https://github.com/GRobertsDuyile/ksb-diff) | 🟢 MIT (`1,071 B`, `sha256:f1331c0a2569…`) | 🇬🇧 Holds each published version of an apprenticeship standard as DATA, one file per version. **Supplies the competency map and, critically, the DIFF when the standard is revised** |
| **Curriculum binding** | [`dimitrex93-cyber/lernpfad-python-cpp`](https://github.com/dimitrex93-cyber/lernpfad-python-cpp) | 🟢 MIT (`1,094 B`, `sha256:d525e491d703…`) | 🇩🇪 The worked example of a curriculum pinned to a named statutory syllabus (*Ausbildungsrahmenplan für Fachinformatiker*). **Copy the BINDING, not the content** |
| **Evidence capture** | [`SergeyZakh/Ausbildungs-Berichtsheft`](https://github.com/SergeyZakh/Ausbildungs-Berichtsheft) | 🟢 MIT (`1,072 B`, `sha256:04bf792574d5…`) | 🇩🇪 Turns a timesheet export (Clockify, Harvest, Jira+Tempo, Kimai, Toggl) into the statutory IHK record as Word/PDF. **The learner files no new document; the system reads one they already produce** |
| **Learning engine** | [`Agono0/learning-hub`](https://github.com/Agono0/learning-hub) | 🟢 MIT (`1,082 B`, `sha256:7704bac11c1e…`) | Spaced repetition, retrieval practice, interleaving and a curriculum engine, **driveable end-to-end over MCP** — the engine, not a tutor |
| **Readiness / assessment prep** | [`gn02ash/cert-coach`](https://github.com/gn02ash/cert-coach) | 🟢 MIT (`1,064 B`, `sha256:0a649bce619f…`) | Domain-weighted plan that reschedules on a missed day; **RAG with a page citation per claim and an explicit refusal when the documents do not cover the question**; readiness score per domain |
| **Orchestration** | [`labsai/EDDI`](https://github.com/labsai/EDDI) | 🟢 Apache-2.0 (`9,152 B`, byte-read `p828`) | 🇩🇪 Config-driven multi-agent runtime (JSON → running service, MCP/A2A, RAG, persistent state). **Already carried by `P68`; reuse the same runtime rather than standing up a second one** |
| **Feedback contract** | [`JohnBilousov/vocabit-mcp`](https://github.com/JohnBilousov/vocabit-mcp) | 🟢 MIT (`1,070 B`, `sha256:ed0657fb89fe…`) | 🔵 **Copy the SHAPE, not necessarily the component: `create_study_set` writes, `get_set_results` reads back what the learner found hard.** A loop that does not read performance back is an open loop |

🔴 **Zero copyleft in the delivered tree.** 🔴 **The traps adjacent to this recipe, named so nobody
walks into them:** `ApprenticeshipStandardsDotOrg` is `CC0-1.0` over a Rails application (`T78`) — its
DATA is usable, its code is not clean to vendor; `elevate-for-humanity/Elevate-lms` is `NOASSERTION`;
and `polendol/AgenticTeacher`, if used for level-matching, is MIT code over `CC BY-NC-SA 4.0` MODEL
WEIGHTS that must be retrained for a commercial deliverable.

### 🔴 Draw the regulatory boundary BEFORE the first node

🔴 **EU AI Act Annex III point 3 covers vocational education and training explicitly** — not only
schools and universities — and captures a system performing one of four functions: determining
access or admission; **evaluating learning outcomes**; assessing the appropriate level of education a
person will receive; and monitoring prohibited behaviour during tests. (`CITED, NOT READ`, from
WebSearch summaries, `2026-11-15`.)

🔵 **The boundary runs straight through the readiness score, and the design must choose a side:**

| Design | Who reads the score | Annex III point 3 | Verdict |
|---|---|---|---|
| 🟢 **Advisory** — the readiness score is shown to the LEARNER and to nobody else; the assessor never sees it | learner | Not *evaluating learning outcomes* by the provider | 🟢 **Build it this way first** |
| 🔴 **Gating** — the score decides who is entered for assessment, or is shown to the EPAO/assessor | provider, assessor | 🔴 **Yes — high-risk** | 🔴 Full Annex III duties; do not slide into this by adding one dashboard |

🔴 **The calendar (`CITED, NOT READ`):** Annex III high-risk obligations were deferred to
**`2027-12-02`** by Regulation (EU) 2026/1744 / the Digital Omnibus, in force since `2026-07-27`;
**Article 50 transparency and the AI-literacy duty apply NOW.** 🔵 **So the advisory build ships
today with disclosure and literacy obligations only — and the gating build has a dated deadline to
design against rather than a vague future.**

### 🟢 The wiring

1. 🟢 **Ingest the standard as data.** `ksb-diff`'s per-version files become the competency
   map. **Pin the engagement to a VERSION.** When the standard is revised, the diff — which KSBs were
   added, removed or reworded, which grading descriptors moved — is a tool output, not two PDFs and
   an afternoon.
2. 🟢 **Bind the curriculum to the map.** Follow `lernpfad-python-cpp`'s binding: every unit cites
   the KSB it serves. **Coverage then becomes a query** — which KSBs no unit teaches.
3. 🟢 **Capture evidence from what the learner already produces.** `Ausbildungs-Berichtsheft`'s
   route — timesheet export in, statutory record out — is the whole trick. 🔵 **Keep its privacy
   posture as a product property: it runs without an account and the data stays in the browser.**
4. 🟢 **Map each evidence entry to a KSB.** This is the only node that needs a model, and it is a
   CLASSIFICATION with a closed label set (the KSB list from step 1) — which makes it testable against
   a human-labelled sample, exactly as `P67` induces a rubric from a `15%` sample.
5. 🟢 **Run the learning engine on the gaps.** `learning-hub` over MCP, scheduled against the KSBs
   with no evidence behind them.
6. 🟢 **Score readiness per KSB domain, advisory only.** `cert-coach`'s two controls are the ones
   worth keeping verbatim: **a page citation for every claim, and an explicit refusal when the
   documents do not cover the question.** 🔵 A readiness score that cannot cite the evidence behind
   it is exactly what an EPAO will reject.
7. 🟢 **Close the loop.** `vocabit-mcp`'s `get_set_results` shape: what the learner found hard
   feeds step 5's next schedule. 🔴 **Without this the pipeline is a report generator.**
8. 🔴 **Gate the write path.** The moment anything in this pipeline WRITES to the provider's system
   of record, apply the two controls `p828`'s cohort supplied and `P68` already carries:
   **out-of-band approval** (`merlin-mcp`) and **server-side RBAC** (`bb-mcp`). 🔵 The statutory record
   is a legal document; an agent must not be the last writer before submission.

### 🔵 Porting it

🟢 **EMEA is the anchor** because that is where the components are: 🇬🇧 `ksb-diff` for England's
standards and 🇩🇪 three German IHK tools. 🔵 **The architecture is jurisdiction-shaped, not
country-shaped: it needs (a) a published competency standard, (b) a mandated learner evidence record
and (c) a terminal assessment.**
🔴 **North America:** the standards data exists (`ApprenticeshipStandardsDotOrg`) but is `CC0-1.0`
over software — **the first task is a licence request, not a rewrite**, exactly as `P64` begins. The
funding tailwind is dated: Workforce Pell for short-term, workforce-outcome programmes from
**`2026-07-01`** (`CITED, NOT READ`).
🔴 **LATAM:** SENA 🇨🇴, SENAI 🇧🇷 and CONALEP 🇲🇽 run exactly this shape at national scale and the
open supply is **`0` agents against ~`30` pieces of student coursework (`T103`)**. 🔵 **The LATAM
engagement therefore starts from the standard document, not from a repository search** — and the
qualifying question is public: does the national body publish its *competencias laborales* as
structured data, or only as PDFs? 🟢 **If only as PDFs, step 1 IS the deliverable and `ksb-diff`'s
one-file-per-version layout is the specification to copy.**
🔴 **APAC:** `NSDC`/Skill India 🇮🇳 and SMK/Dapodik 🇮🇩 returned `0` build-safe supply this pass; the
same standard-first opening applies.

## P68 — The heterogeneous-LMS student-record connector: one domain model, four vendor adapters (Global build, EMEA control anchor)

🟢 **The premise, and it is a measured one.** `T99` established that the open agent supply for
Brightspace, D2L and Blackboard exists at `147` repositories and was almost entirely unmapped
here, while `T100` established that the usable artefacts are **institution-bound** and carry the
authentication and pagination knowledge that is the expensive part of any LMS integration.
🔴 **No national or multi-campus education client runs one LMS.** A ministry, a university group
or a private HE operator typically runs two to four — and the usual response is four
point-integrations that drift.

🟢 **This recipe builds ONE domain model and mounts vendor adapters under it**, taking the
protocol knowledge from permissively-licensed, byte-read servers rather than rediscovering it.

### Components — all byte-read permissive on `2026-11-15`

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Orchestration | [`labsai/EDDI`](https://github.com/labsai/EDDI) | Apache-2.0, `394★` | Config-driven: a JSON definition becomes a running multi-agent service, 19+ providers, MCP/A2A and persistent state. Avoids writing an orchestration layer at all |
| Blackboard adapter | [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) | MIT | Wraps the **official Blackboard Learn REST API** and already carries **RBAC middleware** — the authorisation shape an institutional deployment needs |
| Blackboard fallback | [`UKplus8HRS/bb-mcp`](https://github.com/UKplus8HRS/bb-mcp) | MIT | **Playwright-driven**, configurable institutions + SSO. Use where the institution issues no REST credentials — which is the common case |
| D2L adapter | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | MIT, `67★` | The largest independent D2L server; explicitly *"works with any school"*, so it is the one written against the product rather than one campus |
| D2L (compiled) | [`micho911/brightspace-mcp`](https://github.com/micho911/brightspace-mcp) | MIT | Go — ship as a single binary where a campus will not host a Python runtime |
| Moodle adapter | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | MIT, `29★` | Operates Moodle broadly (courses, assignments, forums, grades, files-as-markdown) |
| SGA↔Moodle bridge (🇧🇷) | [`suap-ava-suite/djangoapp-integrador_ava`](https://github.com/suap-ava-suite/djangoapp-integrador_ava) | MIT | Where the client is Brazilian: joins SUAP/SIGAA/Q-Acadêmico to Moodle. 🔴 Declared development-use-only — read it as a specification, do not deploy it |
| Write control | [`simonseifert/merlin-mcp`](https://github.com/simonseifert/merlin-mcp) | MIT | Copy its **phone-approved send**: out-of-band human confirmation on every write |
| Auth control | [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp) | MIT | Copy its **credential non-possession**: the human logs in, the service inherits the session; the service never holds the password |

### How to wire it

1. **Define the domain model first, from the intersection, not the union.** Course, enrolment,
   assessment item, due date, submission, grade, announcement. Every one of the four vendors has
   these; almost nothing else is common. 🔴 **Model the union and the adapters become the
   product.**
2. **Each adapter implements read-only first** and is accepted against the vendor's own
   documentation, not against the reference server — the reference server is where you learn the
   protocol, not what you certify against.
3. **The write path is a separate, later interface** and is gated by the two controls above:
   out-of-band human confirmation (`merlin-mcp`) and server-side role enforcement (`bb-mcp`'s
   RBAC). 🟢 **Per `T101` this is the default, not a hardening phase.**
4. **Mount the adapters in EDDI** as tool surfaces behind one conversational service; EDDI's
   persistent state carries the student context across vendors, which is the thing none of the
   single-LMS servers can do.
5. **Vendor the adapter code into the client's repository.** 🔴 `T100`: these are
   single-maintainer, `0–2★` repositories against portals that change without notice. The licence
   lets you fork; the risk profile requires you to.

### Compliance anchor — EMEA

🔴 **The write path is the regulated path.** Where the connector is used for **grading, steering
learning, admissions or exam monitoring**, it is an Annex III use under the EU AI Act. 🟢 **This
base already records the Digital Omnibus — `Regulation (EU) 2026/1744` — moving stand-alone
Annex III duties to `2027-12-02`, while the Article 50 transparency duties and the AI-literacy
duty are live now.** 🔵 **Practical reading for a 2026 engagement: the read-only connector ships
under transparency and literacy obligations today, and the write path is the deliverable to
scope against the `2027-12-02` date — which is a procurement argument, not a delay.**

### Shape of the engagement

🟢 **`8`–`10` weeks** for the domain model plus two adapters read-only; **`+4`–`6` weeks** per
further adapter; **`+4` weeks** for the gated write path. 🔵 **The reusable asset is the domain
model and the acceptance suite, not the adapters** — the adapters are the part that will be
rewritten when a vendor changes a portal.

## P67 — The rubric-grading build: the recipe for a capability with NO adoptable base (Global build, EMEA compliance anchor)

🔴 **Premise, and it is the opposite of every other recipe in this file.** `P55`–`P66` all start
from something you can adopt. `T96` established that grading does not have one: nine repositories
searched, all student- or course-scale, the two with real architecture rejected on a licence
conflict (`GPL-3.0` vs a README claiming MIT) and on no licence file at all. 🟢 **So this recipe
BUILDS, and its value is that it does not build blind — the rejected repositories contain two
correct design decisions, and both are cheap to reimplement from their descriptions.**

### What to take from the rejected work (ideas, not code — neither repository is usable)

1. 🟢 **Keep the arithmetic OUT of the model.** `timothyheeeee/Autonomous-Grading-Engine` routes
   rubric interpretation through a multimodal model but hands every calculation to a deterministic
   Python stage. 🔵 An LLM that sums weighted criteria will occasionally sum them wrong, and a
   grading system that is wrong about addition is unshippable regardless of how good its judgement
   is. **Model produces per-criterion judgements; code produces the score.**
2. 🟢 **Induce the rubric from a small human-scored sample, then self-test.** `shafaq2019/Rubric_Agent`
   has a reviewer score a random **`15%`** sample, drafts explicit *Do's & Don'ts* from that
   scoring, **self-tests on held-out samples**, and only then scores the remainder. 🔵 This converts
   *"does the model agree with our rubric?"* from an assumption into a measured, per-engagement
   number — which is the question an academic board actually asks.
3. 🟢 **Run each item three times and flag instability.** Same source. 🔵 Divergence across runs is
   the cheapest available proxy for *"this item needs a human"*, and it costs two extra inferences
   on a task where inference is not the expensive part.

### The build, on components already on these shelves

| Stage | Component | Licence | Role |
|---|---|---|---|
| Orchestration | [`LangGraph`](https://github.com/langchain-ai/langgraph) | MIT | The graph: induct → self-test → score ×3 → stability check → route |
| Rubric induction | your own node | — | `15%` human-scored sample → explicit Do's & Don'ts, held-out self-test, **agreement number reported to the board** |
| Scoring | your own node, model-agnostic | — | Per-criterion judgement + evidence span. 🔴 **No arithmetic in this node** |
| Calculation | plain Python | — | Weighted roll-up. Deterministic, unit-tested, auditable |
| Stability gate | your own node | — | 3 runs; divergence → route to human, never to a score |
| Human oversight | **`P60`'s teacher-approval publication gate** | — | 🟢 Already specified in this file; no grade publishes without an approving human |
| Delivery | `Moodle-MCP` / `canvas-mcp` connector tier | MIT | Grades land in the system of record the institution already runs |
| Provenance | 🇮🇳 see below | — | Labels and provenance markers on generated feedback |

### 🔴 Draw the compliance boundary BEFORE the first node, not after the demo

🔴 **Under the EU AI Act, Annex III covers education systems that *"determine access, ASSESS
LEARNING OUTCOMES, or influence educational paths."*** 🟢 **A rubric grader is high-risk by
construction in EMEA — there is no configuration of it that is not.** Consequences, all of them
design inputs rather than paperwork:

- 🟢 **`P60`'s approval gate is NOT optional here.** Article 14 human oversight is the product
  default: the system proposes a grade, a human publishes it. 🔵 Build it that way from the first
  commit; retrofitting an approval step into a pipeline that already auto-publishes is a rewrite.
- 🔴 **Do not add emotion recognition to the marking of a recorded or proctored assessment.**
  Banned in education since February 2025, and the ban is settled where the Annex III start date is
  not.
- 🔴 **The Annex III start date is CONTESTED in secondary sources** — `2027-12-02` in one guide,
  August 2026 in others (see `intel/market.md`, EMEA). 🟢 **Design to the obligation and do not quote
  the date to a client until the consolidated text is read.** The obligation is certain; the
  calendar is not.
- 🇮🇳 **APAC provenance requirement, and it is a BUILD item.** From **`2026-02-20`** India requires
  AI-generated content to carry prominent labels and provenance markers. 🔵 Generated feedback is
  AI-generated content. Emit provenance from the feedback node by default rather than adding it for
  one market.
- 🇺🇸 **North America:** the obligation lands on the school board (Virginia) or on a state model
  policy (North Carolina Session Law `2026-41`, model policy due `2026-12-31`). 🟢 **The deliverable
  that sells is an audit trail the board can show** — per-criterion evidence spans, the induction
  agreement number, and the approval log from `P60`.

### Sequencing

🟢 **`6`–`8` weeks to a defensible pilot on one course.** Weeks 1–2: rubric induction node and the
`15%` sampling protocol with a named academic owner. Weeks 3–4: scoring node, deterministic
calculator, unit tests on the arithmetic. Week 5: stability gate and `P60` approval gate. Weeks 6–7:
connector into Moodle or Canvas. Week 8: the agreement number, the audit trail and the Annex III
classification memo — 🔵 **which is the actual deliverable to the board, and the reason the pilot
converts.**

🔴 **The one thing not to do:** do not propose any of the nine repositories from `T96` as a starting
point. Two are licence-blocked and all nine are course-scale. 🟢 **Cite them as evidence that the
category is open, which is a selling point, not as a shortcut through the build.**

## P64 — The multi-national school-portal connector: one domain model, four national back ends, and a licence conversation instead of four rewrites (EMEA anchor, portable to LATAM)

🟢 **`T95` as a product.** Four European countries run four incumbent school systems with no public API; `12` open connectors exist across them; `10` are independent; **`4` are build-safe.** 🔵 **Nobody has built the one thing a studio can sell: a single connector with a single domain model, deployed per country, per school board or per white-label client.**

### The components — every grant byte-read on `2026-11-15`

| Role | Component | Grant | Why this one |
|---|---|---|---|
| 🟢 **Domain model + architecture** | https://github.com/ljarochowski/librus-mcp | 🟢 MIT (`1,079 B`, `sha256:be00e61b6328…`) | Ports-and-adapters already: `domain/models` (`Child`, `Grade`, `Homework`, `CalendarEvent`), `domain/services` (`GradeAnalyzer`, `HomeworkTracker`, `CalendarAnalyzer`), `ports/`, `adapters/`. **Take the domain layer; the Librus scraper is already a swappable adapter** |
| 🟢 **Multi-back-end proof** | https://github.com/jujukingg/edu-mcp | 🟢 MIT (`1,080 B`, `sha256:2ede3d997023…`) | Already runs Pronote (+ENT), ÉcoleDirecte and Skolengo behind one server. **The shape is proven; it is proven in one country** |
| 🟢 **DACH adapter** | https://github.com/toughIQ/webuntis-mcp + https://github.com/DenizCiger/untis-mcp | 🟢 MIT both | Two independent lineages — one Python/parent-facing, one Rust with output schemas on every tool. Port the Rust tool contracts, take either client |
| 🟢 **Credential pattern** | https://github.com/heiko-schabert/webuntis-cli | 🟢 MIT (`sha256:2c0b8069fc10…`) | 🔵 **The only no-password design in the tier**: the Untis Mobile JSON-RPC endpoint with a per-request TOTP. **Adopt this before anything else — a school connector that stores parent passwords is unsellable in EMEA** |
| 🟢 **NL adapter** | https://github.com/israelroldan/unofficial-magister-mcp | 🟢 MIT (`1,069 B`) | The tier's only Magister implementation (`T94`) |
| 🟢 **Provenance envelope** | https://github.com/bsayres/heronhex-highered | 🟢 MIT | `source` + `source_url` + `as_of` + `retrieved_at` on every response; missing data as explicit `null` with a reason |

### How it wires together

1. **Lift the domain layer from `librus-mcp`** — `Child`, `Grade`, `Homework`, `CalendarEvent`, plus the three analyzer services. These names are already country-neutral; nothing in them is Polish.
2. **Define one `SchoolPortalPort`** with the read operations every one of the four systems supports: timetable for a date range, changes/cancellations, homework due, grades, absences with the allowed maximum, messages. 🔴 **Nothing else. The intersection is the product; a union forces per-country branching into the domain layer, which is the mistake this recipe exists to avoid.**
3. **Write one adapter per back end**, each lifted from the shelved implementation above rather than from scratch. `edu-mcp` already gives you three.
4. **Make credentials a port too**, and implement the TOTP pattern from `webuntis-cli` first. 🔵 Password-storing adapters are a separate, clearly labelled tier that a client opts into.
5. **Wrap every response in the `heronhex` envelope.** For a school portal `as_of` is not decoration: a timetable read at `07:40` and a cancellation posted at `07:55` are a support incident unless the answer carries its own retrieval time.
6. **Expose it as MCP, and as a REST surface behind it.** Every shelved implementation here is MCP-first, which is correct for the parent-with-an-assistant case and insufficient for the school-board case.

### The licence step, which is the actual first task

🔴 **`7` of the `12` connectors found carry no `LICENSE` file.** 🟢 **Before writing an adapter for a country, open an issue asking the author to add one.** Two of the unlicensed WebUntis servers are school-specific (`leo-hhg`, `Ida-Untis`) and one is a WebUntis+Moodle toolbox — all three are a licence away from being usable, and a licence request costs an hour against a connector's weeks.

### Why it survives review

🟢 Every adapter is unofficial, so **each one names its non-affiliation in its own documentation, as `unofficial-magister-mcp` already does.** 🟢 Read-only by default, with writes a separately-scoped, separately-priced tier governed by `P56`. 🔴 **The data is children's data in every one of these countries. The guardian-credential boundary of `P45` is not optional here, and GDPR applies to all four jurisdictions.**

### Estimate

🟢 **`6`–`8` weeks** for the domain layer, the port, two adapters (DACH + France, the two largest markets) and the envelope. **`1`–`2` weeks per further country**, because the domain layer does not move. 🔵 **Port to LATAM with no architectural change:** `Petri-Hub/fam-mcp` (🇧🇷, MIT) is already the same shape, and `KaioBorgesDev/siga-mcp` covers São Paulo's state technical network — 🔴 but SIGA carries no licence, so that adapter starts with the same licence request.

### Three disqualifiers — check these first

🔴 **The client wants writes in v1.** Submission and enrolment writes against a scraped portal need `P56`'s commit-and-re-read protocol and a different risk conversation; do not fold them into the connector milestone.
🔴 **The client wants one country only.** Then buy or fork the single national connector and skip this recipe entirely — the domain layer only pays back across borders.
🔴 **The incumbent vendor offers an official API under contract.** Take it. Every component here exists because no such API is available.

## P65 — The canonical-diff licence gate: four controls that catch a rewritten grant, a silent republish and a hash that lies (Global, and it protects every other recipe in this file)

🔴 **`p826` nearly shelved a repository whose MIT permission clause had been rewritten, and nearly published a two-implementation population that is one implementation at two addresses.** 🟢 **Both were caught by controls that this base did not previously run. This recipe is those controls.**

### Control 1 — Diff against canonical, do not read the header (`T93`)

🔴 A `LICENSE` that opens `MIT License` and carries a plausible copyright line can still have its **grant clause** rewritten. `gangula-karthik/ntulearn-mcp` replaces *"to permit persons to whom the Software is furnished to do so"* with *"to furnish it to whom it is furnished to do so"* — the only sentence that grants onward distribution, altered into something that does not grant anything.

🟢 **The control:** keep canonical SPDX texts locally; normalise whitespace and strip the copyright line; `diff` the candidate against the canonical of the licence it claims. 🟢 **Zero diff → shelve. Any diff in the grant, conditions or warranty clauses → reject and route to a human.** 🔵 **Byte LENGTH is a usable pre-filter — canonical MIT bodies on this shelf run `1,062`–`1,085 B`, and the rewritten one is `1,055 B` — but length alone is noise, because the copyright line's length varies by holder name.**

### Control 2 — Treat `NOASSERTION` as a QUESTION, never as an answer (`T50` → `T52` → `T93`)

🔴 This base has now held three positions on `NOASSERTION`: *leans copyleft* (`T50`, retracted), *the matcher failed* (`T52`, true but incomplete), and now **the matcher failed, and one of the reasons it fails is that the grant was edited** (`T93`). 🟢 **So `NOASSERTION` routes to Control 1, and Control 1 decides. It is never shelved on the field, and never rejected on the field either** — `ntulearn-mcp` is genuinely good code whose licence is one commit away from correct.

### Control 3 — De-duplicate a population by licence hash AND README hash before counting it (`T94`)

🔴 **GitHub's `fork` flag reported `false` on a repository carrying another developer's `LICENSE` bytes and 2024 copyright line.** 🟢 **The control:** hash `LICENSE` and `README.md` for every member of a population. On a licence-hash collision, **read the README**:

| Signal | Disposition |
|---|---|
| README declares the port and links upstream, holder retained | 🟢 Honest port — count as ONE lineage, both usable |
| README near-identical, no attribution, later creation date, `fork=false` | 🔴 Silent republish — count as ONE implementation, shelve only the original |
| Different READMEs, different licence hashes | 🟢 Independent implementations — count each |

🔵 **This matters wherever a count becomes an argument** — `T77`'s per-campus population, `P55`'s consolidation case, `T95`'s regional yield. A supply figure inflated by republished copies makes a market look better served than it is.

### Control 4 — Byte-read on the branch that exists, and record the probe

🔴 A `main`-only probe records a false `NO_LICENCE_FILE` on any repository whose default branch is `master` — this base already lost a row to it (`langchain`). 🟢 Probe `main` then `master`, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`. 🔴 **And record the CHANNEL: this pass could not use `curl` against `github.com` at all — the proxy returned `403` for every URL including `torvalds/linux`, so a naive liveness check would have reported the entire shelf dead.** 🟢 `raw.githubusercontent.com` worked; `search/repositories` with a `repo:` qualifier worked; `repos/{owner}/{repo}` and `users/{u}/repos` were refused. **Calibrate a liveness instrument against a known-good URL before trusting a single `404`.**

### What it costs, and what it is worth

🟢 **Half a day to implement, and it runs in the ingest path.** 🔵 **Its value is not caught defects per pass — it is that every row on these shelves becomes a statement a procurement lawyer can rely on. One rewritten grant shipped into a client tree costs more than every run of this gate combined.**

## P66 — The channel-integrity gate: reject a mass-publication farm before it reaches a shortlist (Global, and the recipe that makes star-ranked discovery usable again)

🔴 **`p826` measured a `1,524`-repository farm carrying `~102,000` stars that took `45%` of the first page of this base's own prescribed `tutor` query.** 🟢 **Its signature is mechanical and cheap to detect. This is the detector.**

### The measured signature — five signals, any three of which convict

| Signal | Farm (`apimart`, `1,524` repos) | Honest cohort (`AGENTIC STAR`, `1,241` repos) |
|---|---|---|
| **Owner clustering** | 🔴 `580` accounts, all one prefix + random suffix, `~2.6` repos each | 🟢 `13` named individuals |
| **Stars without forks** | 🔴 mean `67.3★`, `0` forks on `99` of `100` | 🟢 `0★`, consistent with age |
| **Identical payload sizes** | 🔴 four buckets (`174`/`1,292`/`1,329`/`6,096 KB`) repeated across the corpus | 🟢 sizes vary with content |
| **Licence** | 🔴 `1,000` of `1,000` `NOASSERTION` | 🟢 `1,211` of `1,241` MIT |
| **Publication window** | 🔴 `1,524` in `6` days | 🟡 `1,210` in `10` days — **a burst is NOT by itself a farm signal** |

🔵 **The last row is the point: both populations were mass-published within days. Burst detection alone would have rejected the MIT cohort too.** 🟢 **It is the conjunction — throwaway owners + stars without forks + repeated payload sizes + blanket `NOASSERTION` — that separates them.**

### How to run it

1. **Before shortlisting from any star-ranked query**, pull `owner.login`, `size`, `stargazers_count`, `forks_count`, `license.spdx_id` and `created_at` for every result. All of it comes back from `search/repositories` in the same call; no extra requests.
2. **Cluster owners by longest common prefix.** Three or more results sharing a prefix of ≥`6` characters with random suffixes is signal one.
3. **Compute stars ÷ (forks + 1).** On this farm it is `67`; on real repositories on these shelves it is in single digits. 🔵 **Stars are purchasable and forks are not, so their RATIO is the cheapest forgery detector available.**
4. **Histogram `size`.** Exact repeats across unrelated owners are signal three.
5. **Quarantine, do not delete.** A quarantined cluster is a finding worth recording — `T73`'s clone farm and `T91`'s relay farm are both intelligence about the channel.
6. **Re-run the query with no star floor** and rank by `pushed_at`. 🟢 **This is `T70`'s channel, and it is the one that has produced every non-nil discovery pass this base has had.**

### The standing instruction this replaces

🔴 **Stop treating a star floor as a quality filter in this domain.** 🟢 **On these shelves the genuinely new education supply sits at `0`–`50★` — `untis-mcp` `0★`, `edu-mcp` `0★`, `heronhex-highered` `0★`, `TeachMeCoding` `50★` — while the farm sits at `~67★` per repository.** 🔵 **Any floor that excludes the farm excludes the entire shelf. Use the licence byte-read of `P65` as the quality filter and recency as the ranking; stars are a popularity signal about the past and, as `T73` and `T91` both show, a forgeable one.**

## P61 — Harvest the catalogue as REQUIREMENTS, not as a codebase: `54` specified education workflows into your own LangGraph tree (APAC origin, Global application)

🔴 **The mistake this recipe exists to prevent.** `T86` found `74` MIT education agents. The obvious move is to fork and deploy them. 🔴 **Do not:** all `74` are `0★`, none pushed since October, each refuses to start without a SoftBank AGENTIC STAR deployment (`PlatformRequired` at graph compile), and the framework under them is a single-release binary wheel whose source repository has zero commits (`T89`).

🟢 **What they are actually worth, and it is more than the code.** Every repository ships, under MIT:

| Asset | File | Why it is the valuable part |
|---|---|---|
| A specification | `docs/02_design.md` (`7`–`16 KB`) | A named education workflow decomposed into graph nodes by someone who had the domain in front of them |
| 🟢 A test specification | `docs/03_test_spec.md` (`5`–`8 KB`) | **The acceptance criteria, written before you own the problem** |
| 🟢 Boundary proofs | `tests/proof_of_boundary/` | `test_import_isolation`, `test_pb_invoke_order`, `test_state_safety`, `test_pb7_hitl_interrupt_propagation`, `test_pb_s1_s2_gates`, `test_pb_s3_s4_gates` |
| A deployment contract | `config/agent.yaml` | Declares `required_trust_level`, every secret used, and the generation mode |
| A catalogue id | `EDU-C2-NNN` in the README `H1` | Lets you tell a client *which* of `173` numbered workflows you are quoting for |

🟢 **And the READMEs state the decisive fact: `python -m pytest tests/ -v` runs WITHOUT a platform connection.** 🔵 **So the tests are executable the moment you clone, while the agent is not — which is precisely the asymmetry that makes this a spec corpus rather than a product.**

**The recipe, concretely:**

1. 🟢 **Enumerate.** `gh api -X GET search/repositories -f q='"agentic star" education' -f sort=updated -f per_page=100`, repeated for `university school student curriculum academic teacher exam training learning`; union and de-duplicate by `full_name`. Expect `~74`.
2. 🟢 **Extract the id map.** `curl -sS https://raw.githubusercontent.com/<addr>/main/README.md | grep -m1 '^# '` → `EDU-C2-NNN — <Workflow name>`. This is your catalogue. Sort by id and the gaps tell you what the vendor specified but did not publish.
3. 🟡 **Gate the licence on BYTES, per `P57` as extended by `T88`.** `curl -sS https://raw.githubusercontent.com/<addr>/main/LICENSE` → expect `~1,07x B`, title `MIT License`, and record the `sha256` — `T90` shows the hash clusters by AUTHOR, so it also gives you your counterparty list for free.
4. 🟢 **Clone blobless and take only the four assets.** `git clone --filter=blob:none --no-checkout --depth 1 https://github.com/<addr> d && git -C d ls-tree -r HEAD`, then `git -C d show HEAD:docs/03_test_spec.md`. 🔵 **Never `pip install -e .` — that is what pulls the pinned framework in.**
5. 🟢 **Re-implement on the stack you already hold.** The graphs are LangGraph (`langchain-ai/langgraph`, MIT, `44,985★`, now on `repos/foundations.md`). The node decomposition transfers verbatim; only `AgentBaseGraph` and the platform client are replaced.
6. 🟢 **Keep the boundary tests.** They are MIT, framework-light, and they encode the HITL-interrupt and state-safety properties that an education deliverable has to demonstrate anyway.

🔵 **What a client buys.** Not "we found some open source". **"Here are `54` specified education workflows with acceptance criteria, we have mapped your `6` against them, and the test spec predates our estimate."** 🟢 **Zero copyleft in the delivered tree: templates MIT, LangGraph MIT, LangChain MIT.**

## P62 — The platform-brand discovery protocol: close the third indexing axis (Global)

🟢 **`P59` enumerates SYSTEMS OF RECORD (SIGAA, SIU Guaraní, Moodle) because `T82` showed LATAM supply is named after the registry.** 🔴 **`T86` showed a second, independent naming law that `P59` does not cover: supply is also named after the PLATFORM BRAND that commissioned it — `agentic-star-*` — and `29` passes of star-ranked and pedagogy-ranked search never touched it.** This recipe closes that axis.

**Run it at the start of any education engagement, in this order:**

1. 🟢 **Harvest brand tokens from prose, not from your own vocabulary.** Take the `20` most recent repositories in the vertical via `sort=updated` with NO star floor (`T70`), and extract every capitalised multi-word proper noun from their descriptions and README `H1`s. 🔵 **The tell is the phrase *"built with X"* — in this catalogue, *"built with Agentic Star"* appears in all `74` descriptions and is the single highest-yield string in the entire sweep.**
2. 🟢 **Re-query each token as a quoted phrase, crossed with the vertical's nouns.** `q='"<brand>" education'`, `"<brand>" university`, `"<brand>" school`, … 🔴 **Quote it: unquoted, `agentic star` tokenises to `agentic` + `star` and returns `2,660` unrelated repositories — this pass made that exact error first and the brand was invisible in the noise.**
3. 🟡 **Expect `0★` and do not filter it out.** A vendor-programme cohort is published once, by developers who never promote it. 🔴 **Any star floor ≥ `1` deletes `100%` of this catalogue.**
4. 🟢 **Look for a catalogue id in the README `H1`.** An id scheme (`EDU-C2-NNN`) means you have found a SPECIFICATION SET, not a scatter — and the id range tells you the true size against the published fraction (`54` of `173` here, `~31%`).
5. 🟡 **Author-census it before you price it** (`T90`): `cut -d/ -f1` over the addresses. One author with `40` repositories is one person's weekend; `13` authors with `74` is a programme, and the two have different survival odds.
6. 🔴 **Then, and only then, read a nil.** 🟢 **The rule `T87` cost this base a published error to learn: a nil is a property of the QUERY until at least two orthogonal axes — pedagogy, jurisdiction/language, system of record, platform brand — have been run.**

🔵 **Portable across this estate.** The channel is `1,430` repositories across all verticals, of which `74` are education. 🟢 **Financial, healthcare, legal and retail KBs in this estate can run step `2` with their own nouns against the same brand token today.**

## P63 — The special-education evidence pipeline, with the decision boundary drawn before the first node (EMEA anchor, portable)

🟢 **Now buildable for the first time on these shelves, because `p825` ended the IEP nil.** Three catalogue workflows compose into the pipeline a special-education office actually runs, and each one stops short of the decision:

| Stage | Component | Licence | What it does — and what it refuses |
|---|---|---|---|
| 1. Intake audit | [`EDU-C2-098`](https://github.com/tvcuong1802/agentic-star-learning-resource-accessibility-gap-brief-agent) | 🟢 MIT (`1,068 B`) | Finds which learning resources cannot answer an accessibility question. 🔵 Reports MISSING METADATA, never "inaccessible" |
| 2. Package validation | [`EDU-C2-173`](https://github.com/KaitoYokomizo/agentic-star-student-accommodation-review-agent) | 🟢 MIT (`1,070 B`) | Validates the evidence in an accommodation review package. 🔴 **Explicitly pre-decision: establishes whether the package is DECIDABLE, does not grant or deny** |
| 3. Drafting | [`EDU-C2-028`](https://github.com/sbdnakashima/agentic-star-iep-section-drafting-agent) | 🟢 MIT (`1,074 B`) | Drafts the four statutory IEP sections from assessment input. 🟢 Ships `regulatory_compliance_node` and `review_flag_node` as SEPARATE nodes from the generator |
| 4. Human decision | — | — | 🔴 **Not automated. Not automatable here** |

🔴 **Why the boundary is drawn at stage `4` and not negotiated afterwards.** Under the EU AI Act, education is an Annex III high-risk category, and this base carries the Omnibus date (`Regulation (EU) 2026/1744`, stand-alone Annex III duties from `2027-12-02`, `CITED, NOT READ`, now confirmed a third time at `p825`). 🟢 **An agent that DRAFTS a statutory document and an agent that DECIDES a child's entitlement are on opposite sides of that line.** 🔵 **The three components above were each written, independently, to stop on the safe side — `EDU-C2-173` says so in its own description. Build on that property rather than removing it.**

**Wiring:** stages `1`–`3` are LangGraph graphs with compatible `src/schemas/state.py` shapes, so compose them as sub-graphs behind one supervisor; harvest per `P61` rather than deploying the templates. 🟡 **Add a durable audit record at every stage boundary** — `EDU-C2-028`'s `review_flag_node` emits the flag, but the pipeline must persist WHO saw it and WHEN, which is the half the templates do not ship and the half an appeal turns on (`P37`'s argument, and `p824`'s `AI-Smart-Proctoring-System` row made the same point for integrity evidence).

🟢 **Where it ports.** Any jurisdiction with a statutory individualised-support process and an appeal right: 🇺🇸 IDEA/IEP (North America — note the US instrument is what `EDU-C2-028` is literally named for), 🇬🇧 EHC plans (EMEA), 🇯🇵 個別の教育支援計画 (APAC). 🔴 **LATAM: this base has found no open supply at this layer in any pass — an explicit, still-open gap, and `P62` step `2` is the first thing to run against it.**

## P58 — The assembled open proctoring stack, with the Annex III boundary drawn BEFORE the first line of code (EMEA anchor, APAC port, and the first recipe here whose main deliverable is a documented REFUSAL to build three features)

🟢 **Why this recipe exists now and could not exist at `p815`.** `p815` measured the proctoring
layer at `12` repositories and concluded *"build, or decline"*. `T83` re-measured it at `101` and
`63` on two different queries and found **six permissive components and no permissive product**.
🔵 **That is precisely the shape an assembly engagement is for: the client is not buying code that
exists, they are buying the integration, the evidence trail and the regulatory boundary.**

### The components — every grant byte-read at `p824`

| Component | Repo | Licence | What it contributes |
|---|---|---|---|
| Browser exam environment | [`amaanwarsi/Proctora`](https://github.com/amaanwarsi/Proctora) | 🟢 MIT (`1,055 B`, `sha256:26e0d192…`) | Flask + OpenCV + **MediaPipe** fullscreen browser session. MediaPipe matters: the gaze and pose primitives are Apache-2.0 upstream, so the stack stays build-safe to the bottom |
| Evidence layer | [`ENGABHAY/AI-Smart-Proctoring-System`](https://github.com/ENGABHAY/AI-Smart-Proctoring-System) | 🟢 MIT (`1,075 B`, `sha256:4e2a4004…`) | YOLO prohibited-object detection with **evidence logging and integrity reports** — the only open implementation of the evidence side in the layer |
| Lockdown | `SEB` `seb-win-refactoring` (already shelved, `p815`) | 🟡 MPL-2.0 (Windows only; macOS/iOS payload absent) | Kiosk/lockdown browser from ETH Zürich 🇨🇭. Not an AI proctor and must not be sold as one |
| Physical-device check | [`epoko77-ai/examguard`](https://github.com/epoko77-ai/examguard) | 🟢 MIT (`1,078 B`, `sha256:963f8f22…`) | BLE and advertising-packet screening for smart glasses in a physical hall, plus a device catalogue. **The APAC port's anchor** |
| Appeal package | `P37` (this file) | — | The adjudication artefact. A detection without an appeal-survivable record is a liability, not a control |
| Deployment registry | `P14` (this file) | — | The Article 49/registry obligation, already built in this base |

### The three features this recipe REFUSES to build, and why that is the deliverable

🔴 **1. Emotion or affect recognition. Banned.** The EU AI Act's prohibition on emotion recognition
in education has applied since `2025-02-02` — not postponed, not risk-managed, prohibited.
🔴 **2. Biometric categorisation of candidates.** Same prohibition family; and it adds a GDPR
Article 9 special-category processing problem that no proctoring business case survives.
🔴 **3. Automated sanction.** The decision stays with a human examiner. 🔵 **`T68` already records
that Brazil's parecer prohibits detector-only sanction outright; the EMEA and LATAM rules converge
here, so one product posture serves both.**

🟢 **Write these three refusals into the SOW as scope exclusions on day one.** They are the cheapest
differentiator available: every proprietary incumbent in this category sells at least one of them.

### How it wires together

1. **Lockdown** (`SEB`, Windows) or plain fullscreen (`Proctora`) establishes the session.
2. **`Proctora`'s** MediaPipe pipeline emits *behavioural events* — gaze off-screen, second face in
   frame, window blur. 🔴 **Events, never scores, and never an affect label.**
3. **`ENGABHAY`'s** YOLO pass emits *object events* — phone, second screen, paper — each with the
   frame reference that will become the evidence.
4. Both streams land in the **`P37` evidence store**: timestamped, hash-chained, candidate-visible.
5. 🔴 **No automated verdict.** A human examiner opens the `P37` package and decides.
6. The deployment is registered in the **`P14` registry** with its Annex III classification, its
   conformity artefacts and its retention period.
7. **APAC port:** add `examguard` as a pre-session physical check of the hall. 🟢 **It watches the
   room and the devices and never the candidate — the one proctoring shape the Article 5 ban
   cannot reach, and the shape a 🇰🇷 or 🇻🇳 invigilated-hall client actually needs.**

### Why it survives review

🟢 **Annex III**: the deployment is classified, registered and human-decided, so the conformity
question is answerable rather than argued. 🟢 **Article 5**: the three banned feature families are
absent by design and documented as absent. 🟢 **Article 14**: the human examiner is the decision
point, not a reviewer of an automated decision. 🔵 **🇻🇳 Vietnam**: the same architecture answers a
law in force since `2026-03-01` that names automated assessment as high-risk — and per `T84` there
is no in-country permissive base, so this is the import.

### Estimate

`10`–`14` weeks. Session + lockdown `2`; event pipelines `3`; `P37` evidence store `3`; `P14`
registry `1`; conformity documentation and the refusal memo `2`; APAC physical-check port `+2`.

### Three disqualifiers — check these first

1. 🔴 **The client wants a score, a flag or an automatic fail.** Decline, or re-scope to `P37` alone.
2. 🔴 **The exam is in a jurisdiction that mandates a specific accredited proctoring vendor.** Several
   professional-certification regimes do; the assembly cannot be accredited retrospectively.
3. 🔴 **The client expects an incumbent's detection accuracy.** The permissive ceiling in this layer is
   `6★` of single-developer code (`T83`). This is an engineering build, and the honest pitch is the
   evidence trail and the boundary, not the model.

## P59 — The registry-first discovery protocol: find a market's real agent supply by enumerating the systems of record, not the pedagogy (LATAM anchor, portable to every institution-owned market)

🟢 **Why this is a recipe and not a note.** `T82` measured `4` results for Spanish and Portuguese
pedagogical vocabulary against `709` for one registry name, on the same channel on the same day.
🔵 **A studio starting a LATAM engagement with the obvious queries will conclude the market is
empty, and will be wrong by two orders of magnitude.** This is the protocol that stops that, and
its deliverable is a sourcing artefact the engagement keeps.

### Step 1 — Enumerate the registries, not the concepts

For the target country, list the systems an institution actually logs into. For 🇧🇷 Brazil that is
**SIGAA** (federal universities), **Moodle**, **CAPES Periódicos** (national journal licence),
**SciELO**, **Lattes**, **BDTD**; for 🇦🇷 Argentina **SIU Guaraní** and Moodle; and so on.
🟢 **Every one of these is already named on this base's shelves** — `agents/top.md` carries
`periodicos-capes-mcp`, `pesquisador-br-skill`, `sigaa-agente`, `Sigaa-UFRPE-MCP`, `utn-mcp`,
`UniMCP`, `ufsc-moodle-mcp`, and `p824` added `ufc-mcp`, `2026-2-Followw` and `sigaa-faltas`.

### Step 2 — Query the registry name on the recency channel, with no star floor

```
gh api -X GET search/repositories -f q='sigaa' -f sort=updated -f order=desc
gh api -X GET search/repositories -f q='moodle agente' -f sort=updated -f order=desc
```

🔴 **No star floor.** `T70`/`T82`'s rows sit at `0`–`15★` and a floor of `10` removes most of them.
🟢 **`sort=updated`** is what surfaces the live ones: four of `p824`'s LATAM rows were pushed inside
`48` hours.

### Step 3 — Classify each hit by WHO it is pinned to

🔵 **This tier is single-host by construction** (`T77`): the institution's hostname is in the code.
Sort hits into **(a)** one-campus adapters, **(b)** national-system agents — CAPES, SciELO, KCI —
which have one buyer and hundreds of institutions, and **(c)** university-course orgs such as
`unb-mds`, which ship a **new cohort every semester**. 🟢 **(c) changes the staleness arithmetic for
the whole tier and is the channel most worth subscribing to.**

### Step 4 — Byte-read before shelving anything

Run `P52`'s payload gate and `P57`'s two-asset gate as extended by `T81`. 🔴 **On `p824`'s LATAM
sweep the pedagogical-vocabulary hits were `4`-for-`4` unlicensed; the registry-name hits were
mostly MIT. The grant distribution differs by CHANNEL, so neither channel's licence profile may be
assumed from the other.**

### Step 5 — Ship the enumeration as a deliverable

🟢 **The registry list, the queries, the dated counts and the classified hits are a market map the
client can re-run.** It is the cheapest credible first artefact of a LATAM engagement and it dates
itself, which is what makes it re-runnable.

### Where it ports

🔵 **Any market where the INSTITUTION rather than a vendor owns the system of record.** `T31`
already found EMEA's supply attached to ministry and *Länder* portals; `p824` added 🇩🇪
`ferien-mcp` (school holidays per *Land*) and 🇵🇭 `ph-data-mcp-server` (national scholarships and
schools) through exactly this shape. 🔴 **It does NOT port to North America, where the registries
are vendor-owned and closed: `p824` measured `q="powerschool clever district mcp"` → `0`,
`q="infinite campus schoology skyward"` → `0`. There the equivalent protocol enumerates STANDARDS
bodies — Ed-Fi, OneRoster, Caliper, 1EdTech — and that is `P19`.**

### Estimate

`1`–`2` weeks as a standalone market map; `3`–`5` days when folded into the discovery phase of a
larger engagement.

## P60 — The teacher-approval publication gate: Article 14 human oversight shipped as a product default (Global, with a named reference implementation)

🟢 **Why it is separate from `P56`.** `P56` makes a WRITE auditable after the fact — commit,
invalidate, re-read, diff. 🔵 **`P60` is the control BEFORE the write: nothing an agent generates
reaches a learner until a named human approves it.** The two compose; neither replaces the other.

### The reference implementation, byte-read at `p824`

🟢 **[`balejosg/tiza`](https://github.com/balejosg/tiza)** — MIT (`1,064 B`, `sha256:7a3a02ea…`),
pushed `2026-11-15`. A Spanish-language CLI and agent skill that drives Claude Code, Codex,
opencode or GitHub Copilot to prepare Moodle pages, labels, assignments, auto-marking quizzes and
**H5P** activities. 🟢 **Its stated contract is the pattern:** *"el agente prepara… tú los revisas
y decides qué llega a tu alumnado"* — the agent drafts, the **teacher** approves, and only then is
anything published. 🟢 **It also ships its own boundary notice: independent, unofficial, "use it
respecting your centre's rules."**

### The gate, generalised

1. **Draft into a staging namespace**, never into the live course. In Moodle that is a hidden
   section; in Canvas an unpublished module; in any LMS, content whose visibility flag is `false`.
2. **Render a diff a teacher can read** — not JSON. What will appear, where, to whom, and when.
3. **Require a named approval**, recorded with the approver's institutional identity (`P9`'s
   learner-record spine already carries the identity layer; `p817`'s Apereo CAS row is the EMEA
   instance).
4. **Publish only on approval**, then run `P56`'s verified write — commit, cache-invalidate,
   re-read, diff — so the approved artefact is proven to be the published one.
5. **Log the pair**: what was approved and what was published, hash-linked. 🔵 **That pair is the
   whole evidentiary content of "a human was in the loop".**

### Why it survives review

🟢 **EU AI Act Article 14** asks for human oversight that is *effective*, which means the human
must be able to understand and to refuse. A readable diff plus a blocking approval is the minimum
implementation of both; an "AI suggestion" banner is not. 🟢 **Article 50 transparency** (applying
from `2026-08-02`) is satisfied at the same point: the approval record names the generated
artefact, so marking it is a lookup rather than a classification problem (`P17`, and the
`aiact-50-2-*` instruments already in `compose/code/`). 🔵 **🇧🇷 Brazil**: `T68` records that AI
pre-correction is admitted only as a *preparatory* step — which is this gate, stated by a
regulator.

### Estimate

`3`–`5` weeks on an LMS this base already holds a connector for (`P3`, `P55`); `2` weeks if the
client is adopting `tiza` and the work is hardening plus the approval log.

### Three disqualifiers — check these first

1. 🔴 **The client's goal is throughput — "the agent publishes, the teacher spot-checks".** That is
   the inverse of this gate and it fails Article 14. Say so before the SOW.
2. 🔴 **No institutional identity to bind the approval to.** An unauthenticated approval is not a
   human-oversight record. Solve identity first (`p817`).
3. 🔴 **The LMS has no staging state.** Some hosted configurations publish on write; without a
   hidden/unpublished state the gate has nowhere to stand.

## P55 — The multi-tenant campus LMS connector: turn `20`+ unfunded per-campus adapters into one supported product (Global, with named reference implementations in four regions)

🔵 **`T77` found a population: university-pinned LMS agents across `14` jurisdictions, each one a
student or staff member routing around an integration their institution never built. Every one is
single-maintainer, `0–2★`, and pinned to one hostname. This recipe is the product that population
is asking for, and the engagement sells it to the institution rather than to the learner.**

**The stack:**

- 🟢 [`jpss2004-bot/neyvu-connectors`](https://github.com/jpss2004-bot/neyvu-connectors) (MIT) —
  **the architecture, and the only component here that already generalises.** One read-only
  `LmsConnector` interface with **four methods**, three implementations — Canvas (REST API v1),
  Brightspace (Valence API), Moodle (page capture) — behind a single MCP server exposing
  `list_courses`, `list_assignments`, `list_documents`, `get_document` for all three. 🔴 Self-described
  prototype: **take the interface and the provenance model, re-implement the adapters.**
- 🟢 [`CloudDown/student-mcp`](https://github.com/CloudDown/student-mcp) (MIT) — **the auth and
  consent tier.** Real-browser sign-in with MFA, **only a token or private browser profile stored,
  never the password**, per-account assistant-access switches, multiple accounts per platform.
  🔵 **This is the piece institutions will test hardest and the piece most adapters get wrong.**
- 🟢 **Host adapters to read before writing your own**, each pinned to a live production system:
  [`do-2k25-28/moodle-um`](https://github.com/do-2k25-28/moodle-um) 🇫🇷 (MIT) for **ENT/CAS SSO**,
  [`Raindancer118/nak-api`](https://github.com/Raindancer118/nak-api) 🇩🇪 for a **two-system join**
  (CIS + Moodle in one answer), [`Waldo0926/monash-study-kit`](https://github.com/Waldo0926/monash-study-kit) 🇦🇺 (MIT)
  for **LMS + forum (Ed)**, [`jeanmartina/ufsc-moodle-mcp`](https://github.com/jeanmartina/ufsc-moodle-mcp) 🇧🇷 (MIT)
  for **writes** (see `P56`).
- 🟢 **Generic Moodle base to fork:** [`rahul069/moodle-mcp`](https://github.com/rahul069/moodle-mcp) (MIT),
  read-only and not host-pinned.
- 🔴 **Do NOT vendor:** [`Sun-sunshine06/bupt-anything`](https://github.com/Sun-sunshine06/bupt-anything)
  (**GPL-3.0**, propagates) and [`mahmutmft/courses-mcp`](https://github.com/mahmutmft/courses-mcp),
  [`corixien/Website-MCP`](https://github.com/corixien/Website-MCP),
  [`daniilnikhaev534-art/moodle-mcp-server`](https://github.com/daniilnikhaev534-art/moodle-mcp-server)
  (**no grant file at all — all-rights-reserved**). Read them; ship none of them.
  🔴 [`Raindancer118/nak-api`](https://github.com/Raindancer118/nak-api) is **WTFPL** — permissive in
  effect, but not OSI-approved and with no warranty or patent language. **Legal sign-off before it
  enters a tendered deliverable.**

🟢 **Wiring.** `neyvu-connectors`' `LmsConnector` is the only interface the agent sees. Each campus
is a **tenant record**, not a build: `{host, platform, auth_method, adapter_version}`. Auth follows
`student-mcp` — browser-based institutional SSO, token or profile at rest, never a credential in the
model context. Every record returned carries `neyvu`'s provenance triple (source URL, API path or
capture, provider version), which is what lets the institution answer *"where did this number come
from"* without re-running the agent.

🔵 **The tenancy decision that makes or breaks it:** capture-based adapters break when the
institution restyles its Moodle. 🟢 **So ship adapter health as a product feature** — a nightly
contract test per tenant against the four read methods, and a per-tenant RED that routes to support
rather than to the student. **That recurring obligation is the reason this is a service and not a
one-off integration, and it is what the unfunded per-campus repos structurally cannot offer.**

🔴 **What this recipe REFUSES to do: start with writes.** `T77`'s population is overwhelmingly
read-only, the institutional objection is always about writes, and `P56` is a separate, later,
separately-governed phase.

**Scope:** `8`–`10` weeks for the interface, the auth tier and **three** host adapters against live
systems; `2`–`3` weeks per additional campus thereafter. 🔵 **Price the adapter fleet as
maintenance, not as delivery.**

**Buyer:** the university CIO or digital-learning director. 🟢 **The qualifying question has a
public answer: search GitHub for the institution's own LMS hostname. If a student has already built
and published an adapter for it, demand is demonstrated and the procurement conversation starts from
evidence rather than from a pitch.**

## P56 — The verified LMS write: commit, invalidate, re-read, diff — the protocol that makes an agent writing to a system of record auditable (LATAM anchor, portable to every LMS on these shelves)

🔵 **Every LMS write agent this base has shelved fires and reports success. `T79` found the one that
does not, and this recipe generalises its protocol — because the protocol, not the repository, is
the asset.**

**The reference implementation:**
🟢 [`jeanmartina/ufsc-moodle-mcp`](https://github.com/jeanmartina/ufsc-moodle-mcp) (MIT, byte-read
`1,064 B`), against **UFSC** 🇧🇷 Moodle in production.

**The protocol, as four obligations:**

1. 🟢 **Commit through the system's OWN form, not a side channel.** The reference drives Moodle's
   `/course/modedit.php` with a resilient `<select>` parser and an explicitly mapped submit button
   (`submitbutton2`, *"Salvar e voltar ao curso"*). 🔵 **Mapping the right button is not a detail: the
   wrong one silently discards the edit.**
2. 🟢 **Invalidate before you verify.** The reference clears `assignmentIndexCache` *before* the
   post-commit re-read. 🔴 **A read-back that can be served from the writer's own cache verifies
   nothing** — this is the step to copy even if you copy nothing else.
3. 🟢 **Diff against BOTH `expectedChanges` and `expectedPreserved`.** Assert what you meant to
   change *and* what you meant to leave alone. 🔵 **The second list is where silent collateral edits
   are caught** — the reference publishes `dueDate` never moving `cutoffDate` as a guarantee, which
   is the most common silent deadline bug in LMS automation.
4. 🟢 **Return a failure TAXONOMY, not a boolean.** `form_rejected` (validation) is distinguished
   from an expired session. 🔵 **That distinction decides whether a retry is safe**; collapsing both
   into "failed" produces either duplicate writes or abandoned ones.

**Compose it with:**

- 🟢 **Human authorship of the standard:** [`lby749/smart-marking`](https://github.com/lby749/smart-marking) (MIT)
  takes the **teacher's own rubric** as input rather than inventing one. 🔵 **Keep that ordering** —
  it is the side of the line Ofqual and Florida Rule `6A-14.0719` leave open (`T30`): the human
  authors the standard, the agent applies it, the human confirms.
- 🟢 **Batch with an overview:** the reference's `commit_grading_batch` +
  `get_assignment_grading_overview` make a batch inspectable before and after.
- 🟢 **Privacy posture when the artefacts are minors' work:**
  [`Bhuvantejakomera/Agentic-Assignment-Evaluator.`](https://github.com/Bhuvantejakomera/Agentic-Assignment-Evaluator.) (MIT)
  scores with **local LLMs** — nothing leaves the institution. 🔴 **Note the literal full stop at the
  end of that address; it resolves, and naive link-stripping breaks it.**
- 🔴 **The contrast case, shelved in this same pass:**
  [`do-2k25-28/moodle-um`](https://github.com/do-2k25-28/moodle-um) submits assignments on the
  learner's behalf and publishes **no equivalent read-back**. Same tier, same window, opposite
  assurance posture — exactly the comparison to put in front of a committee that is nervous about
  writes.

🟢 **The governance payoff.** Across `T30`'s six jurisdictions the rule is consistent: AI may not be
the sole decider of an academic outcome. **A two-phase commit with a stored diff is how you evidence
that a human decided** — the diff is the audit record, per assignment, per grade, per batch.

🔴 **What this recipe REFUSES: no code path writes a grade the human has not confirmed.** Inherited
verbatim from `P51`'s constraint — *"AI that proposes, never decides"* — and expressed here as a
schema in which the commit tool requires a confirmation token the review step issues.

**Scope:** `4`–`6` weeks against one LMS, including the contract tests. 🔵 **Port cost to a second
LMS is in the form driver, not the protocol: budget `2`–`3` weeks.**

**Buyer:** the registrar, the academic-integrity office, or the pro-vice-chancellor who has to sign
that the institution's AI use is compliant.

## P57 — The two-licence pre-shelf gate for courseware: probe the CONTENT grant before the code grant decides anything (Global, and the cheapest refusal in this base)

🔵 **`T78` is four `curl`s' worth of prevention against shipping a client a curriculum nobody is
allowed to sell. This recipe is those four `curl`s, plus the rule that fires them.**

**The trigger.** The candidate repository's description or README names any of: *course, classes,
curriculum, curso, clases, currículo, lesson, syllabus, rubric, rúbrica, assessment, question bank,
教学设计, 课程标准*. 🟢 **If it does, the deliverable is PROSE and the code licence is not the
governing grant.**

**The probe, after the ordinary `LICENSE` byte-read succeeds:**

```bash
REPO=owner/name; BRANCH=main
for p in LICENSE-CONTENT.md LICENSE-CONTENT CONTENT-LICENSE.md LICENSE-DOCS.md LICENSE-CC.md \
         content/LICENSE docs/LICENSE COPYRIGHT-CONTENT.md; do
  code=$(curl -sL --max-time 20 -o "/tmp/$$.$p" -w "%{http_code}" \
    "https://raw.githubusercontent.com/$REPO/$BRANCH/$p" 2>/dev/null)
  [ "$code" = 200 ] && echo "=== $p ($(wc -c <"/tmp/$$.$p") B, sha256:$(sha256sum <"/tmp/$$.$p" | cut -c1-8))" \
    && head -c 400 "/tmp/$$.$p" | tr -d '\r' | tr '\n' ' '
done
```

🟢 **Grade what comes back, and the grading is binary for a commercial deliverable:**

| Content grant | Verdict |
|---|---|
| none found | 🟢 the code licence governs; proceed |
| CC BY / CC BY-SA / CC0 | 🟢 usable; **SA propagates to derivative content** — track it |
| 🔴 **CC BY-NC / CC BY-NC-SA / any NC** | 🔴 **REFUSE for a paid engagement.** Not negotiable by attribution |
| 🔴 CC BY-ND | 🔴 refuse — you cannot adapt it to the client's curriculum |

🔴 **The worked example, byte-confirmed this pass:**
[`modern-software-engineering-program`](https://github.com/vladimiracunadev-create/modern-software-engineering-program)
— `LICENSE` is Apache-2.0 (`11,345 B`), GitHub's field says `Apache-2.0`, and
`LICENSE-CONTENT.md` (`3,523 B`, `sha256:fd781b0e…`) puts all `540` classes under **CC BY-NC-SA
4.0**. 🟢 **The gate costs four `curl`s and refuses it before it reaches a proposal.**

🟢 **Run the mirror check too, and it is one line:** if the repository's *only* grant is a Creative
Commons or other content licence and the deliverable is **software**, refuse on instrument —
[`birkanyavuz/educational-tools`](https://github.com/birkanyavuz/educational-tools) ships an
A2A + MCP classroom-tool server under **CC BY-4.0**, which grants no patent rights and makes no
source provision. 🔵 **Both failure directions, one gate.**

🟢 **Where it belongs:** in front of the existing pre-ingest payload gate (`P52`), because it is
cheaper — a licence refusal needs no clone. 🔵 **And the upstream action is usually trivial:** in
both cases this pass found, a single corrected licence file would move the repository onto the
build-safe shelf, so **file the issue rather than only recording the rejection.**

**Scope:** `2`–`3` days to wire into an existing ingest, as a pre-commit hook over any row whose
description matches the trigger vocabulary.

## P52 — The pre-ingest payload gate: four controls that refuse a `775`-repository clone farm, and the one that actually does the work (Global, and the first recipe here whose deliverable protects the OTHER recipes)

🔵 **Why this recipe exists.** Every other recipe in this file starts *"clone these repositories"*.
`T73` measured what that instruction now costs: GitHub's search index returns `775` repositories
that are relicensed, codeless copies of one real MIT project, created inside `48` hours, each
carrying `650`–`680` stars and a Dropbox `.rar` download as its only call to action.
🔴 **They are not marked as forks, so fork filters miss them. They carry a valid Apache-2.0 FILE,
so licence filters pass them. They out-star their own upstream `8.5:1`, so a "top N by stars"
ingest PREFERS them.** 🟢 **This recipe is the gate that refuses them, and it is four `curl`s.**

**The controls, in the order that fails fastest and cheapest:**

1. 🟢 **EXISTENCE, two-directional.** `GET raw.githubusercontent.com/{repo}/{main,master}/README.md`
   must return `200` on at least one branch, AND a deliberately fabricated sibling path must return
   `404` in the same run. This base has run the negative control since `p812`; without it a
   uniformly broken channel reads exactly like a uniformly absent one.
2. 🟢 **PAYLOAD.** From `search/repositories`, read `size` and `language`. 🔴 **Refuse anything under
   `~500 KB` that carries no build manifest** — probe `package.json`, `requirements.txt`,
   `pyproject.toml`, `setup.py`, `go.mod`, `Cargo.toml`, `composer.json`, `pom.xml`. The clone farm
   dies here: `118 KB`, zero manifests, against the original's `22,029 KB`.
   🔵 **Do NOT probe guessed subdirectory paths as the control — `p822` probed `backend/`,
   `frontend/` and `charts/` on four REAL repositories and got `404` on all of them while
   `size` + `language` correctly reported `13,633 KB` of Python and `37,653 KB` of TypeScript. The
   metadata is the control; the path guess is a false negative generator.**
3. 🟢 **LICENCE LINEAGE, by byte-hash (`T37`).** `sha256` the licence payload. A stock MIT body is
   `~1,060`–`1,130 B`; a stock Apache-2.0 body is `~11,340`–`11,360 B`; AGPL-3.0 is `~34,520 B`.
   🔴 **Compare the SPDX id against the upstream the project resembles: a copy whose licence
   differs from its original is a relicensing, and a relicensing without a holder line is the
   clone-farm signature.**
4. 🟢 **LURE SCAN.** Grep the README for `dropbox|mediafire|mega\.nz|\.rar|bit\.ly` plus a
   download-badge shape. 🔴 **A hit is a REFUSAL, never a follow.** `p822` ran this over all `20`
   education candidates it verified: zero hits, which is what makes the clone farm's hit meaningful.

🟢 **Wiring.** The repository already ships the parts: `ingest/p645-existence-oracle.sh` for (1),
`ingest/p765-licence-byteread.sh` and `ingest/p612-grade-title-line.py` for (3). (2) and (4) are new
and are ~`40` lines of `bash` + `jq`. Run them as a pre-ingest filter over the `search/repositories`
result set BEFORE any row is drafted, and emit a TSV of `repo, verdict, reason` so a refusal is
recorded rather than silently dropped — `agents/top.md`'s rejection table is the publication
surface, and `p822` filed the farm's exemplar there.

🔵 **Effort: `1`–`2` days to wire, and it runs in the time one sweep already takes.**
🟢 **Licence posture: everything here is this base's own code plus `curl`/`jq`; nothing copyleft
enters the delivered tree.**
🔵 **Sell it as this:** any client building an internal catalogue of open-source AI components has
this exposure today, their ranking is almost certainly stars-first, and the control is a day's work.

## P53 — The learning-scaffold wrapper: let the agent do the work and still be able to PROVE the person learned it (Global, and the first recipe here whose buyer is the academic-integrity office or corporate L&D)

🔵 **The problem, in the client's words rather than ours.** Universities have stopped trying to ban
assistants and cannot evidence learning; employers say juniors cannot work without the assistant.
`T75` found three independent repositories implementing the same answer in one pass, and this
recipe composes them.

**The stack, all MIT, all `SKILL.md`-shaped so the pieces are interchangeable:**

- 🟢 [`cheahhl814/lf-skill`](https://github.com/cheahhl814/lf-skill) — the wrapper. Pre-flight basics
  quiz before the agent runs, Socratic checkpoints DURING the run where a defensible learner
  parameter choice is the one actually used, and a teach-back debrief after.
- 🟢 [`Hang-GaoZu/ai-learning-skills`](https://github.com/Hang-GaoZu/ai-learning-skills) — the state.
  `course-state.md` carries the progression, self-tests and dashboard; the HTML variant emits a
  self-contained OFFLINE learning site, which is the artefact to hand a learner who loses access.
- 🟢 [`decolla/tuttor-kit`](https://github.com/decolla/tuttor-kit) — the refusal. For the coding case,
  it guides with questions and hints and does NOT write the code.
- 🟢 [`fcedf/interruptible-ai-tutor`](https://github.com/fcedf/interruptible-ai-tutor) — the delivery
  loop, when the scaffold needs to EXPLAIN rather than quiz: segmented explanation with barge-in,
  live code execution and incremental charts, reachable over CLI, REST + SSE or `SKILL.md`.
- 🟡 [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, `16★`) — the
  institutional record, IF the client has an LRS. 🔴 **This base's `p817` gap stands: it is the only
  licensed xAPI agent surface and it is stale. When it is out of scope, `course-state.md` is the
  fallback record and the engagement should say so in writing rather than imply an integration.**

🟢 **Wiring.** The scaffold is a skill that wraps the client's EXISTING agent, so nothing about
their assistant changes: `lf-skill` gates entry, the work runs, checkpoints fire mid-run, the
teach-back writes to `course-state.md`, and a nightly job maps completed states to xAPI statements
if an LRS exists. 🔵 **The acceptance test is the one the buyer cares about and it is cheap to
state: for a sampled task, the learner can reproduce the REASONING without the agent in the room.**

🔴 **Risks, stated.** All three scaffolds are `0`–`1★` and unproven; treat them as reference
implementations to be re-written in the client's own skill format if they go stale.
🔵 **Effort: `4`–`6` weeks for one faculty or one engineering function, most of it in writing the
checkpoint content, not in code.** 🟢 **Zero copyleft in the delivered tree.**

## P54 — The East Africa voice-first learning deployment, with the FINANCING rail treated as part of the architecture (EMEA anchor, and the first recipe here whose blocking constraint is payment rather than pedagogy)

🔵 **`T71` and `T74` put three Africa-placed, permissively licensed components on this base's
shelves in two passes. This recipe is what they build when composed, and it is shaped by a
constraint the other `53` recipes never face: the learner cannot pay, and the person who CAN pay is
on another continent.**

**The stack:**

- 🟢 [`marthanp/sautika`](https://github.com/marthanp/sautika) (MIT) — the learner surface.
  Voice-first, native-language (Swahili), dyslexia-inclusive, *"designed for learners across East
  Africa"*. 🔵 **Voice-first is not an accessibility nicety here; it is what works at low literacy
  and low bandwidth.**
- 🟢 [`OmarAxis/meska-brain`](https://github.com/OmarAxis/meska-brain) (Apache-2.0) — the learner
  model. An MCP server plus a LangGraph agent holding a longitudinal map that shows a teacher where
  a struggle STARTED, not just where it is. 🔴 **Prototype on synthetic data by its own statement:
  take the schema and the consent gate, re-implement the service.**
- 🟡 [`nafkunasefa1-hub/EthioLearn`](https://github.com/nafkunasefa1-hub/EthioLearn) (MIT) — the
  financing rail, as a REFERENCE not a dependency: a PayPal MCP server through which a diaspora
  sponsor funds a NAMED learner's access, against a named national exam (`EUEE`).
  🔴 **It is a hackathon submission; what transfers is the architecture — an MCP payments tool
  invoked by the same agent that holds the learner record, so sponsorship is an entitlement the
  tutor can read, not a separate billing system.**
- 🟢 [`CentraleSupelec/mydocker`](https://github.com/CentraleSupelec/mydocker) (MIT) — the practical
  tier, when the programme is vocational: Docker lab environments launched from Moodle, scheduled
  on cloud resources, with student data kept off third-party infrastructure.
- 🔴 **Avoid in the delivered tree:** [`DIRA-HUB-LTD/DIRA`](https://github.com/DIRA-HUB-LTD/DIRA)
  solves the same learner-profile problem from the same design challenge but is **AGPL-3.0**, which
  propagates over a hosted service. Read it for the data model; ship `meska-brain`'s tree.

🟢 **Wiring.** `sautika` is the channel; `meska-brain`'s MCP server is the record every component
reads and writes; the sponsorship tool is a third MCP server exposing `entitlement(learner_id)` so
the tutor degrades gracefully to offline content when funding lapses rather than failing closed;
`MyDocker` is attached only for practical modules. 🔵 **Build the consent gate FIRST — a
longitudinal record about a minor is the part that will be audited.**

🔵 **Effort: `10`–`12` weeks for a single-region pilot**, of which the payments rail and its
compliance review are `3`–`4` and are the schedule risk.
🔴 **Known gaps to state in the proposal rather than discover later:** none of the three
Africa-placed components is proven in production, the sponsorship rail's provider terms vary by
corridor and are not this base's finding, and the `p817` learner-record gap applies here too.

## P51 — The competency gradebook agent, built against a NATIONAL curriculum instrument and portable across three of them (LATAM first, with EMEA and APAC ports priced — and the first recipe here whose reusable asset is the CURRICULUM ADAPTER rather than the model)

🔵 **Why it exists.** 🟢 **`T70` found that every place-bound repository `p821` shelved is bound to
a named national instrument, not to a subject** — Peru's `CNEB`, Egypt's STEM Learning Outcomes
with a short code per outcome, China's 人教版 knowledge-point taxonomy. 🔴 **Every tutoring recipe
in this file so far has treated the curriculum as content. In this one it is the SCHEMA**, and
that inversion is what makes the build defensible: the model is swappable, the adapter is not,
and the client already owns the ground truth the adapter encodes.

🟢 **The buyer is a ministry, a regional education authority or a school network — not a learner**,
and the thing bought is a teacher's statutory output: the competency judgement and the written
conclusion that justifies it.

| Role | Component | Licence (byte-read this pass) | Region | Why this one |
|---|---|---|---|---|
| Reference implementation + data model | [`amaru-one/mawta`](https://github.com/amaru-one/mawta) | 🟢 **MIT** (`1,074 B`, `sha256:34142d07…`) | LATAM | 🟢 **The whole recipe already exists once, for one country.** Competency assessment against `CNEB`, achievement levels `AD/A/B/C`, the descriptive conclusion per level, one Python service per school. 🔵 **Its rule is the product rule: *"AI that proposes, never decides"* — nothing saved on the teacher's behalf, every claim pointing at the data it rests on.** |
| Agent runtime | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 **MIT** | Global | Already the runtime `mawta` uses, so the reference implementation and the port share a graph model. 🔵 **Each drafting step is a node with an inspectable input set — which is what "points at the data it rests on" means operationally.** |
| Curriculum adapter — EMEA port | [`mohanvd/edutraceapp`](https://github.com/mohanvd/edutraceapp) | 🟢 **MIT** (`1,065 B`, `sha256:88765a78…`) | EMEA | 🟢 **The 🇪🇬 port's schema, already encoded:** Learning Outcomes for STEM Grades 10–11 with a stable short code (`/PH.1.01`) per outcome and MDX content behind it. 🔵 **A short code is exactly the join key `mawta` lacks for a non-Peruvian deployment.** |
| Curriculum adapter — APAC port | [`wisdom-km/k12-qbank`](https://github.com/wisdom-km/k12-qbank) | 🟢 **MIT** (`1,066 B`, `sha256:03e6e939…`) | APAC | 🔴 **Design only — no web surface and no database, by its own README** (see the rejection row in `agents/top.md`). 🟢 **Cited for its knowledge-point taxonomy over 人教版 七年级上册 and its teacher-verification order, which is the same order this recipe enforces.** Not a dependency; a specification to copy. |
| Longitudinal layer (optional) | [`AI-Native-Ventures/jemma`](https://github.com/AI-Native-Ventures/jemma) | 🟢 **MIT** (`1,075 B`, `sha256:888e10dd…`) | EMEA | 🟢 **Where the buyer asks for multi-year tracking, take `jemma`'s three rules rather than writing new ones (`T71`):** profile-not-label enforced in the save path, a pattern surfaced only after three terms, parent visibility gated on an explicit teacher action. |
| Evidence transport | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | North America | *"Learner `L` produced evidence `E` for competency `C` at `t`"* and *"teacher `T` accepted/edited draft `D`"* as statements, so the audit trail survives the gradebook being replaced. |

**Wiring.**
1. **Model the instrument before the agent.** 🟢 **One table of competencies/outcomes keyed by the
   national short code, one table of achievement levels with their official labels, one table of
   evidence rows pointing at both.** 🔴 **Do not let the LLM invent either vocabulary** — the labels
   are statutory (`AD/A/B/C` in Peru) and a paraphrase is a defect, not a style choice.
2. **Split the adapter from the engine on day one.** Everything country-specific lives behind one
   interface: `competencies()`, `levels()`, `evidence_schema()`, `conclusion_template()`. 🔵 **This
   is the line along which the EMEA and APAC ports are priced, and it is the reason the second
   country costs a fraction of the first.**
3. **Drafting is a proposal, and the schema must make that literal.** Every generated conclusion
   is written to a `draft` row with `status`, `generated_from[]` (the evidence ids) and
   `accepted_by` **null**. 🔴 **No code path writes a grade. If one exists, the product is
   unsellable to a ministry** — and `mawta`'s README is the plain-language statement of that
   constraint to put in front of the client.
4. **Make the teacher's edit the training signal, not a correction.** Store the diff between the
   draft and the accepted text per competency. 🟢 **After one term that diff set is the most
   valuable asset in the deployment**, and it belongs to the client.
5. **Emit xAPI at acceptance, not at generation.** The statement that matters to an auditor is the
   teacher accepting, with the evidence ids attached.
6. **Port by swapping the adapter, and prove it with the EMEA fixture.** 🟢 **Acceptance test for
   the port: resolve `/PH.1.01`, attach two evidence rows, draft a conclusion, have a reviewer
   accept it, and read the xAPI statement back** — no engine code changed.

**Licence position.** 🟢 **Zero copyleft in the delivered tree**: MIT, MIT, MIT, MIT, Apache-2.0.
🔴 **The one trap is adjacent and named in `agents/top.md` this pass:**
[`fotedev/Masar-x-next`](https://github.com/fotedev/Masar-x-next) is the nearest Arabic-first
study platform and it is **AGPL-3.0** — §13 reaches users served over a network, so it cannot be
folded into a hosted deployment of this recipe without a separate grant.

**Estimate.** 🟢 **First country, on `mawta` as the reference: `8`–`10` weeks** — `2` weeks on the
instrument model with a curriculum specialist, `3`–`4` on the drafting graph and the
proposal/acceptance split, `2` on the teacher surface, `1`–`2` on xAPI and reporting.
🟢 **Each additional country: `3`–`4` weeks**, almost all of it in the adapter and in validating
the official vocabulary. 🔴 **The estimate assumes the client supplies the curriculum in machine
-readable form. Where it exists only as PDF — which is the common case outside the three countries
above — add `2`–`3` weeks and say so in the proposal rather than discovering it in week four.**

🔴 **What this recipe does NOT claim.** `mawta` is `2★`, `0` forks and three weeks old; it is cited
as a reference implementation and a data model, not as a dependency with a maintenance guarantee.
🟢 **Vendoring it, or re-implementing its schema, is the honest posture, and the MIT grant permits
both.**

## P50 — The stage-gated basic-education tutor for Brazil: a compliance router keyed on `6º ano`, and an adjudication package that replaces the detector verdict (LATAM, and the first recipe here whose core deliverable is a REFUSAL BOUNDARY inside the product)

🔵 **Why it exists.** 🔴 **`T67` moved the boundary every Brazilian basic-education proposal is
scoped against.** The press framing of `Parecer CNE/CP nº 15/2026` put the restriction on ages
`0`–`5`; the instrument actually bars generative and conversational AI **through `5º ano`, the whole
of primary**, and admits it from `6º ano` only in teacher-mediated activities. 🟢 **So the
deliverable is not a tutor with a content filter. It is a tutor whose STAGE ROUTER is the primary
architectural element, because for two of four rungs the compliant behaviour is to not generate at
all.** 🔴 **And `T68` removes the fallback every integrity vendor reaches for: a sanction founded
exclusively on an AI-detection tool is prohibited, so the detector cannot be the product.**

| Role | Component | Licence (byte-read, as held) | Region | Why this one |
|---|---|---|---|---|
| Guardrail design | [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | 🟢 **MIT** | Global | 🟢 **The three controls this recipe needs already written down: a Socratic hint ladder with a configurable cap, an ANSWER-LEAK GUARD that regenerates and substitutes a safe hint, and rubric grading whose per-criterion scores are validated and TOTALLED IN CODE, not by the model.** 🔴 `0★` — take the control design, not the repository |
| Stage/enrolment source | [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp) | 🟢 **MIT — byte-verified against GitHub's `NOASSERTION`** (`1,275 B`, `sha256:cd14675817b2c618…`) | LATAM | 🟢 **The router must read the learner's STAGE from the system of record, never from a profile field the learner can edit.** SIGAA is the federal-institute incumbent; `GallegoSz/sigaa-mcp` and `EduardoBidese/sigaa-agente` (both MIT, byte-verified) are the alternates |
| Model router | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | 🟢 **MIT** | Global | 🔵 **The `1º`–`5º` rung needs a configuration in which NO generative model is reachable at all — that is a gateway policy, not a prompt instruction** |
| Mediation + mark evidence | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | North America | 🟢 **"Teacher `T` mediated activity `A` for learner `L` at `t`" and "mark set by `T`, model output was input `n` of `k`" are the two statements the `12`-month clock actually requires an institution to be able to produce** |
| Academic-norm surface | [`PedroSmaxY/abnt-mcp`](https://github.com/PedroSmaxY/abnt-mcp) | 🟢 **MIT — byte-read** (`1,086 B`, `sha256:1cdab623…`) | LATAM | Used only on the `ensino superior` rung, where the parecer admits AI as content and as research support |

**Wiring.**
1. **Build the stage router first, and make it fail CLOSED.** 🟢 **Resolve stage from the SIS on
   every session, cache it with a short TTL, and default to the most restrictive rung when the
   lookup fails.** 🔴 **A router that defaults open is the one defect in this recipe that converts a
   compliance product into a liability, because the failure is silent and the logs look normal.**
2. **Make `1º`–`5º` a different DEPLOYMENT, not a different prompt.** 🟢 **Point that cohort at a
   LiteLLM configuration with no generative model in it and serve the *"IA desplugada"* path the
   parecer sanctions — screen-free AI-concept activities, teacher-planned, generated OFFLINE as
   printable material.** 🔵 **This is the rung most proposals will try to satisfy with a system
   prompt; a system prompt is not a control an auditor can inspect.**
3. **On `6º`–`9º`, gate on MEDIATION, not on age.** Every generative turn is bound to a
   teacher-opened activity with a teacher identity on it. 🟢 **Emit the xAPI mediation statement at
   activity open and close** — autonomous use is the thing prohibited, so the evidence that matters
   is the binding, not the content.
4. **Reserve the mark in CODE.** 🟢 **Take `ai-tutor-agent`'s rubric pattern exactly: the model
   proposes per-criterion evidence, the criteria are validated against the rubric, and the total is
   computed in code and written only after a teacher action.** 🔴 **AI pre-correction of redações and
   dissertative exams is admitted ONLY as a preparatory step (`T68`) — a workflow in which the
   model's number can reach a transcript without a teacher event is non-compliant even if a teacher
   later agrees with it.**
5. **Replace the detector verdict with an ADJUDICATION PACKAGE.** 🔴 **Sanction founded exclusively
   on a detection tool is prohibited.** 🟢 **Ship the teacher a bundle — draft history, revision
   timeline, retrieval trail, and the detector score explicitly labelled as one non-dispositive
   input — and make the UI require a written teacher determination before any academic consequence
   is recorded.** 🔵 **This is the half of the build a Brazilian institution cannot buy off the
   shelf: this base's own sweep found `proctoring exam open source` returning `12` repositories at a
   `4★` ceiling with modal licence `NONE`.**

🔴 **What this recipe is NOT.** 🔴 **It is not a tutoring engine** — pair it with `P49` for the
`6º ano`-and-above rungs, which is where a mastery engine is lawful and useful. 🔴 **And it does not
make an institution compliant**: the parecer's `12`-month clock runs on policies, governance
instruments and CONTRACTS, and only the last of those is touched by software.

🟡 **Sourcing, carried from `T67`/`T68` and not re-asserted here as fact.** Every clause of the
parecer used above is **SECONDARY** — `www.gov.br` refuses at `CONNECT`, the instrument is
`CITED, NOT READ`, and `abmes.org.br` is the cheapest primary route for the first pass with egress.
🔴 **Do not put a clause number in a client deliverable off this recipe until the text has been
read.** The stage ladder and the two assessment rules are corroborated by two independent Brazilian
legal sources; the clause numbering is not.

**Estimate.** 🟢 `7`–`9` weeks: stage router with SIS integration and fail-closed semantics (`2`–`3`),
the two-deployment LiteLLM split and the offline *desplugada* generator (`2`), mediation binding and
xAPI emission (`1`–`2`), rubric-in-code and the adjudication package (`2`). 🔴 **Plus a legal review
this base cannot substitute for.** 🟢 **Zero copyleft in the tree — MIT and Apache-2.0 only.**

## P49 — The vendor-neutral tutoring stack: a mastery engine, a whiteboard transport and a benchmark the client re-runs as the acceptance gate (Global)

🔵 **Why it exists.** 🔴 **Every tutoring proposal this base has written before now priced a model
vendor into the architecture, because the visible capabilities — explaining on a whiteboard, adapting
to a learner — looked like model capabilities.** 🟢 **`T65` showed the whiteboard is a transport
protocol and `T63` surfaced an MIT mastery engine with a real prerequisite graph. Put together, the
model becomes the one swappable part of the stack, and the defensible assets — the concept DAG, the
scheduler, the evidence trail — are all permissively licensed and all owned by the client.**

| Role | Component | Licence (byte-read) | Region | Why this one |
|---|---|---|---|---|
| Mastery engine | [`chuma-beep/mathua`](https://github.com/chuma-beep/mathua) | 🟢 **MIT** (`1,074 B`, `sha256:6bd7c2a3…`, first line `MIT License`) | Global | 🟢 **A checked prerequisite DAG of `3,015` concepts with FSRS-6 review and SPEED-AWARE mastery gating, not a chat loop.** Go + Next.js, Postgres via `pgx/v5`, CSV transcript export over the API |
| Whiteboard transport | [`molly554/whiteboard-ai-tutor`](https://github.com/molly554/whiteboard-ai-tutor) | 🟢 **MIT** (`1,089 B`, `sha256:ed7406a6…`, first line `MIT License`) | Global | 🟢 **The JSON drawing-instruction protocol plus the browser player and the interruption path.** Take the protocol and the benchmark runner; the hosted app is explicitly not the deliverable |
| Model router | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | 🟢 **MIT** | Global | 🔵 **The swap has to be a config change, or the vendor-neutrality claim is rhetorical.** One gateway, per-model cost accounting, and the fallback chain the `~15×` spread in `T65` is there to exploit |
| Learner telemetry | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | North America | 🟢 **The mastery events must leave the engine in a standard the institution's LRS already accepts** — otherwise the stack is a silo and the renewal conversation is lost |
| Symbolic grading | [`sympy/sympy`](https://github.com/sympy/sympy) | 🟢 **BSD-3-Clause** | Global | 🔴 **Not optional: ~`32%` of the engine's concepts grade `symbolic`/`polynomial`/`expression`/`complex` answers through it, and the production image FAILS THE BUILD without it** |

**Wiring.**
1. **Stand the mastery engine up FIRST, with no model attached at all.** 🟢 **The DAG, the generators
   and FSRS-6 are deterministic and testable; they are the part of the system a client can audit.**
   🔴 **A tutoring build that starts at the model always ends up with the pedagogy encoded in a
   prompt, where nobody can inspect or version it.**
2. **Put the router in before the second model, not after.** Every call goes through LiteLLM from day
   one. 🔵 **`T65`'s leaderboard shows `11/11` at `$0.0277` against `9/11` at `$0.0019` — a stack that
   can route by scenario captures that spread; one wired to a single vendor cannot.**
3. **Treat the whiteboard as transport.** The model emits drawing JSON; the player renders it; the
   interruption path returns BOARD STATE, not a chat transcript. 🔴 **Sending the transcript instead
   of the board is the mistake that makes interruption feel broken, and it is the one thing in this
   recipe that is not configuration.**
4. **Emit xAPI on mastery transitions, not on clicks.** 🟢 **"Learner reached mastery on concept `X`
   at attempt `n`, elapsed `t` against threshold `T`" is a statement an institution can act on.**
   🔴 **Click-level telemetry fills the LRS and answers nothing.**
5. **Make the benchmark the acceptance gate, and write it into the SOW.** 🟢 **Re-run the frozen-prompt
   harness against the CLIENT's own scenarios and their own blind reviewers, with the boards committed
   to their repository.** 🔵 **This is the first recipe in this base whose acceptance criterion is a
   published method the buyer can execute without the studio in the room — which is exactly why it
   survives a procurement challenge.**

🔴 **What this recipe is NOT, stated so it is not oversold.** 🔴 **`mathua`'s `3,015` concepts are
MATHEMATICS.** The engine, the scheduler and the gating generalise; the content does not. 🔵 **A
non-maths subject needs its own concept DAG authored, and that is the long pole — budget it
separately and do not let it hide inside "configuration".** 🔴 **And both new components are young:
`mathua` has `43` forks and `0` open issues, `whiteboard-ai-tutor` was four days old at shelving.
🟢 **Fork both at a pinned commit and vendor them; do not take a floating dependency on either.**

🟡 **Region.** `Global`. 🔴 **Neither new component states an origin and this base does not infer one
(`T42`)** — `whiteboard-ai-tutor`'s bilingual EN/zh-CN README and DeepSeek coverage are an APAC
signal, not an APAC attribution.

**Estimate.** 🟢 `6`–`8` weeks for the maths vertical end to end: engine deployment with Postgres,
router, whiteboard transport, xAPI emission and the re-run benchmark as the gate. 🔴 **Plus `6`–`10`
weeks per additional subject, dominated by authoring the concept DAG, not by engineering.** 🟢 **Zero
copyleft in the tree — MIT, Apache-2.0 and BSD-3 only; the two new components byte-read on
`2026-11-15` and the rest carried from this base's existing verifications.**

## P46 — The Brazilian research-record agent, built on a LATAM-OPERATED and permissively licensed substrate (LATAM, and the first recipe in this base whose platform is not an import)

🔵 **Why it exists.** 🔴 **Every LATAM recipe in this base before this one — `P29`, `P30` — proposed
building against a foreign platform and localising it, because this base believed the region had no
system of record of its own.** 🟢 **`T58` refuted that: SciELO is operated from São Paulo for sixteen
countries, ships `158` repositories, and its core is BSD-2-Clause. This recipe is the inverse of
every previous one — the substrate is regional, and the localisation is not the work.**

| Role | Component | Licence (byte-read) | Region | Why this one |
|---|---|---|---|---|
| Publishing substrate | [`scieloorg/opac`](https://github.com/scieloorg/opac) | 🟢 **BSD-2-Clause** (`1,292 B`, `sha256:493da013…`, holder `SciELO ORG`) | LATAM | 🟢 **The network's own catalogue code, permissive, operated centrally — no fork needed to integrate** |
| Article packaging | [`scieloorg/packtools`](https://github.com/scieloorg/packtools) | 🟢 **BSD-2-Clause** (`1,288 B`, `sha256:8a810c6a…`) | LATAM | 🟢 **SciELO PS XML validation and transformation. Pushed `2026-11-09` — this is the maintained skill the network actually needs** |
| Federal journal portal | [`damarals/periodicos-capes-mcp`](https://github.com/damarals/periodicos-capes-mcp) | 🟢 **MIT** (`1,064 B`, `sha256:d7d8972d…`) | LATAM | 🟢 **CAPES is licensed centrally by the MEC for every federal university — one integration, ~`400` institutions** |
| Brazilian research stack | [`DevAlissu/pesquisador-br-skill`](https://github.com/DevAlissu/pesquisador-br-skill) | 🟢 **MIT** (`1,080 B`, `sha256:589081fc…`) | LATAM | 🟢 **ABNT + Qualis CAPES + Lattes + SciELO + BDTD in one surface — the only row in this base that composes five Brazilian systems** |
| Organisation identity | [`ror-community/ror-api`](https://github.com/ror-community/ror-api) | 🟢 **MIT** (`1,078 B`, `sha256:48634ddf…`, holder Crossref) | Global | 🔴 **Non-optional: "Universidade de São Paulo" appears in Brazilian research data dozens of ways. ROR is the join key** |
| Person identity | [`cyanheads/orcid-mcp-server`](https://github.com/cyanheads/orcid-mcp-server) | 🟢 **Apache-2.0** (`11,317 B`, `sha256:7915fc5b…`) | Global | An agent that writes to a research record without an ORCID produces unattributable output |
| Citation existence | [`Hylouis233/bibverify`](https://github.com/Hylouis233/bibverify) | 🟢 **MIT** (`1,064 B`, `sha256:ae682216…`) | Global | 🟢 **Verifies a citation EXISTS before it reaches a Qualis submission** |

**Wiring.**
1. **Resolve identity first, not last.** Every record is keyed `ROR` (institution) × `ORCID`
   (person) before any content is read. 🔴 **Skipping this is the failure mode of every research-data
   project; it is cheap at the start and unaffordable at month four.**
2. **Read through published protocols only.** CAPES via `periodicos-capes-mcp`; SciELO content via
   `packtools` against SciELO PS XML. 🔴 **No scraping — a public-sector Brazilian buyer will ask,
   and `dergipark-mcp`'s *"official OAI-PMH, keyless"* is the posture that survives the question.**
3. **Normalise to SciELO PS, not to an internal schema.** 🟢 **The network's format is the
   interoperability target; inventing an internal one re-creates the lock-in the client is paying to
   avoid.**
4. **Gate every generated citation through `bibverify` before it is persisted.** 🔴 **A fabricated
   reference in a Qualis-assessed submission is a research-integrity incident, not a bug.**
5. **Deliver the evidence trail, not the judgement.** Which registry answered, which identifier
   matched, which citation verified. 🔵 **`Parecer CNE/CP nº 15/2026` gives Brazilian institutions a
   `12`-month clock on governance instruments and CONTRACTS — the trail is the deliverable that
   satisfies it.**

🔴 **The adjacent build this recipe does NOT include, and should be quoted separately.**
`q="lattes mcp"` → `total_count=1`, ungranted. 🟢 **A clean-room MIT Lattes client is the single
widest opening in Latin America in this base** — Lattes is the CV every CNPq grant and CAPES
programme evaluation is assessed from. 🔵 **Scope it as its own deliverable and a durable asset,
exactly as `P33` scoped the PRONOTE clean-room client.**

**Estimate.** 🟢 `8`–`10` weeks for the CAPES + SciELO + registry read path with the evidence trail.
🔴 **Plus `4`–`6` weeks if the Lattes client is in scope.** 🟢 **Zero copyleft anywhere in the tree —
BSD-2, MIT and Apache-2.0 only, all seven components byte-read on `2026-11-15`.**

## P47 — Accessibility remediation for course materials, with the proprietary trap named and avoided (Global, and the only recipe here whose obligation is statutory rather than contractual)

🔵 **Why it exists.** 🔴 **`p815` published this layer as `total_count=0`. `T61` corrected it to
thin-but-real, and `T60` found that its most capable component is proprietary while reading
`NOASSERTION` and carrying `-public` in its name.** 🟢 **So the recipe's value is as much in what it
refuses as in what it assembles — and the obligation behind it (EAA in Europe, Section 508 in the
United States) is the one review in education that cannot be waived.**

| Role | Component | Licence (byte-read) | Region | Why this one |
|---|---|---|---|---|
| Document remediation | [`Maximilian741/508-Agent`](https://github.com/Maximilian741/508-Agent) | 🟢 **MIT** (`1,067 B`, `sha256:b48cc408…`) | Global | 🟢 **Section 508 + WCAG 2.1 AA on DOCUMENTS — course materials are PDFs and decks, so this is the education-shaped half** 🔴 `1★`: expect to harden it |
| Scan + remediation tracking | [`jesseslone/wcag-guide`](https://github.com/jesseslone/wcag-guide) | 🟢 **MIT** (`1,067 B`, `sha256:9ddae494…`) | Global | 🟢 **The TRACKER is the point: a regulator asks what you found and what you FIXED, not what you scanned** |
| Authoring target | [`coursecode`](https://github.com/course-code-framework/coursecode) | 🟢 **MIT** | Global | 🔵 **Remediate at the SOURCE and recompile to SCORM/cmi5/LTI, instead of patching exported artefacts forever** |
| Content platform | [`inveniosoftware/invenio-app-rdm`](https://github.com/inveniosoftware/invenio-app-rdm) | 🟢 **MIT** (`1,243 B`, `sha256:ccb5c2a3…`, holder CERN) | EMEA | Where remediated materials are deposited with a persistent identifier |
| Evidence store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | Global | Records the remediation events as a dated, queryable trail |

🔴 **Explicitly EXCLUDED, and say so in the proposal.**
[`dequelabs/axe-mcp-server-public`](https://github.com/dequelabs/axe-mcp-server-public) — licence
field `NOASSERTION`, bytes read `Proprietary License`, *"No license is granted to use, modify, or
distribute"*, use conditioned on a paid Axe DevTools subscription. 🟢 **Naming the exclusion is
worth more than the component would have been: it demonstrates the licence discipline the rest of
the engagement is being bought for.** 🔴 **Also excluded:
[`AIScientists-Dev/AI-Powered-PDF-Accessibility`](https://github.com/AIScientists-Dev/AI-Powered-PDF-Accessibility)
(`10★`) — it does exactly this job and has no licence file at all.** 🟢 **That one is a LICENCE
REQUEST, not a rewrite: one email could unblock the best-fitting component in the layer, and the
request should be sent before the build is scoped.**

**Wiring.**
1. **Inventory before remediation.** `wcag-guide` scans the live estate and opens a tracked finding
   per artefact. 🔵 **The inventory is itself a billable deliverable and usually the first thing a
   compliance officer has ever been given.**
2. **Remediate documents with `508-Agent`, source with `coursecode`.** 🔴 **Two different jobs:
   the first clears the backlog, the second stops it regenerating.**
3. 🔴 **Never let the agent close its own finding.** A named human accepts each remediation; the
   agent proposes and evidences. 🔵 **Six independent sources in `intel/market.md` converge on this
   control point, so it is the defensible posture rather than a cautious one.**
4. **Write every event to `lrsql`** — found, proposed, accepted by whom, when.
5. **Deposit the remediated artefact in InvenioRDM** with a persistent identifier, so the compliant
   version is the citable one.

**Estimate.** 🟢 `6`–`8` weeks for inventory + document remediation + the evidence trail on a
single faculty's estate. 🔴 **Both remediation components are `0`–`1★`: budget hardening explicitly
and do not present them as products.** 🟢 **Zero copyleft, all five components byte-read
`2026-11-15`.**

## P48 — EPrints → InvenioRDM: the migration with a named incumbent, a named date and an agent layer that pays for it (EMEA anchor, Global applicable)

🔵 **Why it exists.** 🟢 **`T59` found that the research platform tier splits by vintage, and this is
the sharpest instance: the incumbent is GPL-3.0 and ABANDONED, and the replacement is MIT and
maintained by CERN.** 🔴 **This base has `47` recipes and almost none of them names an incumbent
being displaced on a dateable fact. This one does.**

| Role | Component | Licence (byte-read) | Region | Why this one |
|---|---|---|---|---|
| 🔴 Incumbent (to leave) | [`eprints/eprints`](https://github.com/eprints/eprints) | 🔴 **GPL-3.0** (`32,421 B`, `sha256:37d3866d…`, `COPYING`) | EMEA | 🔴 **Last pushed `2023-07-31` — unmaintained for over two years while institutions run it in production** |
| 🟢 Target platform | [`inveniosoftware/invenio-app-rdm`](https://github.com/inveniosoftware/invenio-app-rdm) | 🟢 **MIT** (`1,243 B`, `sha256:ccb5c2a3…`, holder **CERN**) | EMEA | 🟢 **The platform Zenodo runs on: MIT, maintained, DOI minting and RDM built in** 🟢 Pushed `2026-11-13` |
| Content extraction | [`mpasternak/oai-pmh-mcp`](https://github.com/mpasternak/oai-pmh-mcp) | 🟢 **MIT** (`1,073 B`, `sha256:900b820e…`) | EMEA | 🟢 **Speaks OAI-PMH to dLibra, DSpace AND EPrints — so the migration reads the incumbent through a published 2002 protocol rather than its database** |
| Library services platform | [`folio-org/platform-complete`](https://github.com/folio-org/platform-complete) | 🟢 **Apache-2.0** (`11,356 B`, `sha256:43070e2d…`) | Global | 🟢 **If the same client is also leaving GPL-3.0 Koha, this is the permissive LSP — one licence conversation, two systems** |
| Organisation identity | [`ror-community/ror-api`](https://github.com/ror-community/ror-api) | 🟢 **MIT** | Global | Affiliations normalised during migration, not after |
| Person identity | [`cyanheads/orcid-mcp-server`](https://github.com/cyanheads/orcid-mcp-server) | 🟢 **Apache-2.0** | Global | Authors reconciled to ORCID as records move |
| Author disambiguation | [`drAbreu/alex-mcp`](https://github.com/drAbreu/alex-mcp) | 🟢 **MIT** (`1,088 B`, `sha256:50f067fd…`) | Global | 🔴 **Pushed `2025-08-11` — stale. Use it, pin it, and own the fork; disambiguation is the half that fails in production** |
| Quality/policy registry | [`DOAJ/doaj`](https://github.com/DOAJ/doaj) | 🟢 **Apache-2.0** (`11,323 B`, `sha256:6dc0e068…`) | Global | 🔵 **Lets the migrated record answer a POLICY question — does this venue count — not just a search one** |

**Wiring.**
1. **Harvest the incumbent over OAI-PMH, never over its database.** 🟢 **`oai-pmh-mcp` reads EPrints
   through the protocol it already publishes, so the migration never depends on a schema the
   abandoned codebase might change — and the same connector later reads any DSpace or dLibra
   instance the client also runs.**
2. **Reconcile identity in flight.** Each record gets a ROR for its institution and an ORCID for its
   authors as it moves; `alex-mcp` proposes disambiguations and 🔴 **a librarian accepts them.**
3. **Load into InvenioRDM and mint persistent identifiers.** 🟢 **The licence changes from GPL-3.0 to
   MIT at this step, which is the line to put in the proposal: the client's platform stops being a
   copyleft obligation.**
4. **Enrich against DOAJ** so the repository can report which deposits sit in indexed open-access
   venues. 🔵 **That is the report a research office asks for and the incumbent cannot produce.**
5. **Agent layer last, on the migrated record** — deposit assistance, metadata completion,
   affiliation correction, each one proposing and a named human accepting. 🔵 **The agent layer is
   what makes the migration fundable: a platform swap alone is a cost line, while a platform swap
   that arrives with a working assistant is a capability.**

🔴 **The honest caveat to state up front.** 🟢 **InvenioRDM is MIT and maintained, but it is a
different stack from EPrints' Perl — this is a migration, not an upgrade, and the content model
mapping is the real work.** 🔵 **Quote the harvest-and-reconcile phase separately from the platform
stand-up, because the first is predictable and the second depends on how much the institution
customised EPrints over twenty years.**

**Estimate.** 🟢 `10`–`14` weeks for harvest, identity reconciliation and InvenioRDM stand-up on a
single institutional repository; 🟢 `+4` weeks for the agent layer; 🔴 `+6`–`8` weeks if FOLIO is in
scope alongside. 🟢 **Zero copyleft in the DELIVERED tree — the GPL-3.0 row is the system being
left, and it is read over a protocol rather than linked against.**

## P43 — Ship courseware INTO the client's LMS without adopting, forking or licensing it (Global, and the recipe that makes `verticals/solutions.md`'s copyleft problem stop applying)

🔵 **Why it exists.** `T54` found four independent `2026` projects that author courseware as SOURCE
IN A REPOSITORY and treat SCORM 1.2 / SCORM 2004 / cmi5 / LTI as COMPILE TARGETS. 🔴 **Every
LMS-customisation engagement in this base inherits a licence: Moodle is GPL-3.0, Open edX is
AGPL-3.0, Sakai is ECL-2.0.** 🟢 **Compiling to an interchange format means no LMS code enters the
deliverable at all — the client's LMS becomes a render target the studio never touches, and the same
artefact runs on every LMS in the estate.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Authoring framework (agent-driven) | [`course-code-framework/coursecode`](https://github.com/course-code-framework/coursecode) | 🟢 **MIT** (`1,069 B`, `sha256:055ad2b2…`) | 🟢 **The only one that names the agent surface explicitly — *“for Claude Code, Codex, and MCP-capable AI tools”* — and already emits all four targets** |
| Non-developer authoring surface | [`course-code-framework/coursecode-desktop`](https://github.com/course-code-framework/coursecode-desktop) | 🟢 **MIT** (`1,069 B`, `sha256:055ad2b2…`) | 🔵 **What an instructional designer opens. Without it this is an engineering tool and faculty development cannot buy it** |
| Source format + validator + compiler | [`aureliendossantos/elabora-core`](https://github.com/aureliendossantos/elabora-core) | 🟢 **Apache-2.0** (`11,358 B`, `sha256:cfc7749b…`) | 🟢 **The most complete statement of the shape — read it for the FORMAT design.** 🔴 One month old, `2★`: take the design, pin nothing |
| Interactive course runtime | [`redmodd/tessera`](https://github.com/redmodd/tessera) | 🟢 **MIT** (`1,078 B`, `sha256:a7b3b71f…`) | Where the deliverable is interactive rather than page-based. Pushed `2026-11-15` |
| Package player + record capture | [`scormflow/scorm-engine`](https://github.com/scormflow/scorm-engine) | 🟢 **MIT** (`1,079 B`, `sha256:7cdfc153…`) | 🟢 **Bundles its own LRS — collapses player+store into one dependency for small engagements** |
| Learning record store (production) | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | 🔴 **Use this, not `scorm-engine`'s built-in, wherever the record must survive an audit.** `144★`, pushed `2026-11-14` |
| Conformance baseline you cite | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** (`11,357 B`, `sha256:58d1e17f…`) | 🔵 **ADL WROTE xAPI. Citing the spec authors' own implementation as the conformance target is a different argument in procurement than citing a popular project** |
| cmi5 into Moodle, if the client insists | [`adlnet/Moodle-mod_cmi5launch`](https://github.com/adlnet/Moodle-mod_cmi5launch) | 🟢 **Apache-2.0** | 🟢 **Apache-2.0 plugin, so the bridge itself is clean even though Moodle is not** |
| LTI 1.3 mount | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | `373★`, pushed `2026-11-11` — the established choice, already in `repos/foundations.md` |
| Agent write-back of activity | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** | The agent's own actions become reportable institutional records rather than invisible ones |
| Identity | [`apereo/cas`](https://github.com/apereo/cas) | 🟢 **Apache-2.0** | 🟢 **`11,399★`. The answer to “how does the agent act as the user without holding their password”** |

**Wiring.**
1. 🟢 **Define the SOURCE FORMAT first and put it under the client's version control.** Read
   `elabora-core` for the design. 🔵 **This is the load-bearing decision: the source format is the
   asset the client keeps, and SCORM/cmi5/LTI are disposable build outputs regenerated on demand.**
2. 🟢 **Put the agent behind the authoring framework, not behind the LMS.** `coursecode` already
   defines the tool surface; the agent drafts, restructures and localises SOURCE FILES, and every
   change is a reviewable diff.
3. 🔴 **Gate the build with a conformance check before export, not after.** `elabora-core` ships a
   validator; `P26`'s conformance gate is the same control and should be reused rather than rebuilt.
4. 🟢 **Compile to the target the client's LMS actually ingests.** SCORM 1.2 for the oldest estates,
   cmi5 or xAPI where the client wants records beyond completion, LTI 1.3 where the content must stay
   hosted by the studio.
5. 🟢 **Point every build at one LRS.** `lrsql` in production; cite `ADL_LRS` as the conformance
   baseline in the statement of work.
6. 🔵 **Only then discuss the LMS.** By this point the LMS is a render target and its licence is the
   client's problem, not the deliverable's.

**Licence consequence.** 🟢 **Clean: every component above is MIT or Apache-2.0, and NO GPL/AGPL code
enters the tree.** 🔵 **That is the entire commercial point of the pattern — compare with any recipe
in this file that customises Moodle or Open edX directly.**

🔴 **Honest limit.** The four authoring projects total `16★` and the most complete is one month old.
🟢 **Carry the SHAPE into the studio's own repository and read these as reference implementations.
Do not pin them as dependencies and do not present them to a client as mature supply.**

**Estimate.** 6–8 weeks for a first course family with a conformance gate and an LRS;
add 3–4 weeks if the source format has to cover interactive assessment rather than pages.


## P44 — The verifiable-credential issuing service a university can actually put into procurement (North America anchor, with the EMEA path stated because it is DIFFERENT)

🔵 **Why it exists.** `T53` found interoperability and credential portability becoming buying
criteria in 2026; `T56` found the supply split sharply by region. 🟢 **North America has a complete,
live, MIT-licensed reference stack. EMEA has a specification whose repository is archived.** 🔴 **A
studio that quotes the same stack to both clients will be wrong in one of them.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Registrar-facing issuing surface | [`digitalcredentials/dcc-admin-dashboard`](https://github.com/digitalcredentials/dcc-admin-dashboard) | 🟢 **MIT** (`1,094 B`, `sha256:0f6a5db4…`, holder `Massachusetts Institute of Technology`) | 🟢 **Upload, manage, issue, collect, notify — the workflow a registrar already has, rather than an API a registrar cannot use** |
| Holder wallet | [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 **MIT** (`1,092 B`, `sha256:1032f65d…`) | 🔴 **Cite THIS address, not the `91★` mirror the search index returns — see `T55`** |
| Verification / relying party | [`digitalcredentials/verifier-plus`](https://github.com/digitalcredentials/verifier-plus) | 🟢 **MIT** (`1,087 B`, `sha256:85569d7e…`) | 🟢 **The half engagements under-budget. Issuing is an afternoon; being TRUSTED is the project** |
| OBv3 vocabulary | [`digitalcredentials/open-badges-context`](https://github.com/digitalcredentials/open-badges-context) | 🟢 **MIT** (`1,087 B`, `sha256:85569d7e…`) | 🔵 **Pin the context or offline verification silently fails — the exact gap a demo hides** |
| Trust registry | [`digitalcredentials/dcc-known-registries`](https://github.com/digitalcredentials/dcc-known-registries) | 🟢 **MIT** (`1,060 B`, `sha256:abbc361f…`, holder `DCC`) | Which DIDs the wallet and verifier will trust. 🔴 **Decide this in week one; it is governance, not code** |
| Student-record source | [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | 🟢 **Apache-2.0** (`10,173 B`, `sha256:a6cba85b…`) | 🔴 **Default branch is `v6.2.0`, not `main` (`T57`)** — K-12; for higher ed the SIS is the source |
| Roster bridge | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** | Serves OneRoster 1.2 from an Ed-Fi ODS — the join between the record system and the credential |
| Agent surface over the record | [`Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants) | 🟢 **Apache-2.0** | 🔵 **`1★`. Use as a SANCTIONING SIGNAL in procurement, not as a dependency (`T53`)** |
| Identity | [`apereo/cas`](https://github.com/apereo/cas) | 🟢 **Apache-2.0** | The institution almost certainly already runs it |
| 🇪🇺 **EMEA conformance target** | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🔴 **EUPL-1.2 — reciprocal, and ARCHIVED** | 🔴 **Conform to the MODEL; implement with the MIT stack above. Do NOT fork this tree (`T56`)** |

**Wiring.**
1. 🟢 **Start at the relying party, not the issuer.** Name the employers, registries or institutions
   that must accept the credential, and confirm what they verify today. 🔴 **An engagement that issues
   first produces credentials nobody checks.**
2. 🟢 **Fix the trust registry and the signing key custody before any code.** `dcc-known-registries`
   is the artefact; key custody is an institutional decision with a legal owner.
3. 🟢 **Wire the record source.** Ed-Fi ODS → `edfi-oneroster` → issuing dashboard for K-12; the SIS
   directly for higher ed.
4. 🟢 **Issue into the wallet, verify through VerifierPlus, pin the OBv3 context, and test OFFLINE** —
   the failure mode that only appears away from the demo network.
5. 🔵 **Where an agent belongs, and where it does not.** 🟢 **Agent: assembling evidence, drafting
   competence descriptions, mapping outcomes to a framework.** 🔴 **Never: deciding whether a credential
   is awarded, or holding the signing key. The award is a registrar's act with an audit trail.**
6. 🔴 **EMEA divergence.** Conform the payload to ELM/Europass and say in writing that the EU reference
   repository is archived at `2024-02-14`, so the specification is stable and the codebase is not
   maintained. 🔵 **Clients hear this as diligence; discovering it in month three is a different conversation.**

**Licence consequence.** 🟢 **The buildable stack is wholly MIT/Apache-2.0.** 🔴 **The single
reciprocal component, ELM, is used as a SPECIFICATION and never vendored — keep it that way and the
deliverable stays permissive.**

🔴 **Regional honesty, carried from `T56`.** 🟢 **Quote this pattern for North America today and for
EMEA with the archived-reference caveat.** 🔴 **Do NOT quote it for APAC or LATAM as an adoption
play: `q="academic bank of credits india"` → `1` unlicensed `0★` repo, and
`q="credencial digital educacion verificable"` → `0`. In those regions this is a BUILD, and the
estimate roughly doubles.**

**Estimate.** 10–12 weeks North America for issuing + verification + one record-system integration;
14–16 weeks EMEA with ELM conformance; a build in APAC/LATAM, not an adoption.


## P45 — The guardian-facing agent, and the one place in this base where the credential belongs to an adult and the data belongs to a child (North America + EMEA)

🔵 **Why it exists.** `ACTION p816-F` asked what system someone OTHER than the learner logs into about
the learner. 🟢 **The answer is the parent portal, and this base had already shelved two of the six
repositories that exist without naming the layer** — which is why this recipe is written now rather
than another harvest being run.

| Role | Component | Licence (byte-read) | Region | Why this one |
|---|---|---|---|---|
| 🇺🇸 Portal access | [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | 🟢 **MIT** (`1,067 B`, `sha256:17dd0009…`) | North America | 🟢 **`Multi-district` by design — the tenancy problem solved in the architecture rather than by the integrator** |
| 🇳🇴 Portal access | [`kristoffervp/vigilo-mcp`](https://github.com/kristoffervp/vigilo-mcp) | 🟢 **0BSD** (`640 B`, `sha256:b5eaf2ff…`) | EMEA | 🟢 **No attribution obligation at all — the only grant on this shelf a studio can vendor with no notice. `T52`** |
| 🇳🇱 Portal access | [`barzoj/somtoday-mcp`](https://github.com/barzoj/somtoday-mcp) | 🟢 **MIT** (`1,082 B`, `sha256:47056e02…`) | EMEA | 🟢 **Read-only declared in the repository's own description** |
| Identity | [`apereo/cas`](https://github.com/apereo/cas) | 🟢 **Apache-2.0** | Global | Delegated auth instead of storing a guardian's portal password |
| Activity record | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | Global | 🔵 **Record what the AGENT did, not what the child did — see wiring step 4** |

**Wiring.**
1. 🔴 **Settle the data question before the architecture one.** The credential is a guardian's; the
   data is a minor's. 🟢 **Both US (FERPA, COPPA where applicable) and EU (GDPR, and Annex III of the
   AI Act where the system touches access or evaluation) treat that asymmetry as the regulated fact.**
2. 🟢 **Read-only by construction for v1.** All three servers above are read-only or read-dominant;
   keep it that way. 🔴 **A write path into a child's school record is a different product with a
   different approval chain.**
3. 🟢 **Keep the portal credential LOCAL.** `vigilo-mcp` is explicitly a local server. 🔵 **Design so
   the guardian's credential never reaches studio or client infrastructure — this is the single
   control that makes the data-protection conversation short.**
4. 🟢 **Log the AGENT's actions to the LRS, not the child's behaviour.** 🔵 **The institution needs to
   know what the assistant read and when; it does not need a new surveillance surface over a minor,
   and building one converts a useful product into an Annex III problem.**
5. 🔵 **Summarise, do not advise.** 🔴 **A guardian-facing agent that interprets grades, predicts
   outcomes or recommends interventions is evaluating a learner — which is the high-risk use.
   Summarising messages, deadlines and attendance is not.**

**Licence consequence.** 🟢 **Entirely clean — 0BSD, MIT and Apache-2.0, with the 0BSD row carrying no
obligation whatsoever.**

🔴 **Honest limit.** `6` repositories exist on this channel in total, ceiling `5★`, and two of the six
carry no licence. 🟢 **This is a pattern for ADAPTING a known-good shape to the client's own portal,
not a shelf to assemble from — the portal is different in every country and usually in every district.**

**Estimate.** 4–6 weeks per portal for a read-only guardian assistant with local credential custody;
the second portal is roughly half the first.


## P40 — The retention engine the studio OWNS (Global, and the only recipe in this base that replaces a copyleft incumbent with an algorithm instead of a fork)

🔵 **Why it exists.** `T49` found that the retention layer splits into a copyleft APPLICATION
tier (`34,887★`) and a permissive ALGORITHM tier (`6,329★`), and that they are separable because
FSRS is a published specification with five independent MIT implementations. 🟢 **This recipe is
the consequence: when a client asks for spaced repetition, you do not integrate Anki — you
implement the scheduler and own it.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Scheduling core (browser / Node) | [`open-spaced-repetition/ts-fsrs`](https://github.com/open-spaced-repetition/ts-fsrs) | 🟢 **MIT** (`1,079 B`, `sha256:8b83a73d…`) | 🟢 **`872★`, pushed `2026-11-13`. TypeScript, so it runs in the same runtime as the client's front end — no service to operate, no copyleft, no network hop for a scheduling decision** |
| Scheduling core (server / analytics) | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | 🟢 **MIT** (`1,079 B`, `sha256:021bff58…`) | 🟢 **`531★`. Use where review history lives in a warehouse and the scheduling is recomputed in batch rather than per-click** |
| Scheduling core (mobile / WASM) | [`open-spaced-repetition/rs-fsrs`](https://github.com/open-spaced-repetition/rs-fsrs) | 🟢 **MIT** (`1,079 B`, `sha256:0f7be8cb…`) | Only if the deliverable is a native or WASM client |
| The SPECIFICATION you cite | [`open-spaced-repetition/free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 **MIT** (`1,089 B`, `sha256:c0e0a71c…`) | 🔵 **Cite THIS in the SOW, not a library. It is what makes the three rows above substitutable and the approach defensible as a documented algorithm rather than a dependency on one maintainer** |
| The EVIDENCE you cite | [`open-spaced-repetition/srs-benchmark`](https://github.com/open-spaced-repetition/srs-benchmark) | 🔴 **NO GRANT — `32` paths + `16` manifests, measured** | 🔵 **Cite it, link it, reproduce its method; 🔴 do NOT vendor its code.** It is the published comparison that turns “use FSRS” into an evidence-based recommendation |
| Card authoring surface | Plain Markdown in the client's own repository, per [`kitschpatrol/yanki-obsidian`](https://github.com/kitschpatrol/yanki-obsidian) | 🟢 **MIT** (`1,071 B`, `sha256:1d5701eb…`) | 🟢 **The inversion that makes the whole recipe work: the corpus is diffable text the institution owns, so Anki is an optional EXPORT TARGET rather than the system of record** |
| Optional Anki export | [`reuseman/flashcards-obsidian`](https://github.com/reuseman/flashcards-obsidian) | 🟢 **MIT** (`1,069 B`, `sha256:99f1ba49…`) | For learners who already live in Anki. 🔴 Export only — see `P41` before any read/write integration |
| Generation | Any LLM, behind the client's existing gateway | — | 🔵 **`T49`: the model picks WHAT to show and may be approximate; FSRS picks WHEN and must be right. Only the second is a correctness claim, and it is already solved** |
| Mount into the LMS | **LTI 1.3** + **xAPI** events | — | The standing rule of this file: permissive AI layer, mounted over a standard, never a fork |

**Wiring.**
1. 🟢 **Model the review log first, not the cards.** `card_id`, `user_id`, `reviewed_at`,
   `rating`, `state`, `stability`, `difficulty`, `due`. 🔵 **FSRS is a pure function over that
   row — given a card's state and a rating it returns the next interval — so the schema IS the
   integration and everything else is replaceable.**
2. 🟢 **Call `ts-fsrs` in the client on each rating** and persist the returned state. No
   scheduling service, no queue, no cron.
3. 🟢 **Generate candidate cards from the course corpus with an LLM, and gate them.** Cards are
   content, so a wrong one is a content defect, not a grading defect — 🔵 **which is why this
   recipe is far lower risk than anything in the assessment layer: nothing here writes to an
   academic record, so neither `T36`'s integrity axis nor the EU AI Act's high-risk grading trigger
   is engaged.**
4. 🟢 **Author in Markdown in the client's repository.** Subject-matter experts review cards in
   the pull-request flow they already use.
5. 🟢 **Emit `xAPI` statements** on each review so the retention data lands in the institution's
   Learning Record Store rather than in a product silo. That is what makes `P42` possible later.
6. 🔴 **Do not integrate Anki to get started.** It is `32,804★` of AGPL-3.0 and it solves a
   problem — the scheduling arithmetic — that `ts-fsrs` solves in the client under MIT.

🟢 **No copyleft anywhere in the tree, and no GPL dependency even transitively — the only recipe
in this base that can say that about a layer whose incumbent is AGPL.**
**Estimate: 4–6 weeks** for the review loop and schema; **+3 weeks** for LLM card generation with
the review gate; **+2 weeks** for the LTI 1.3 mount.


## P41 — Anki-native study agent with a DOCUMENTED process boundary (Global, and the first recipe here whose main deliverable includes a written refusal)

🔵 **Why it exists.** Some clients already have the cohort inside Anki — language schools,
medical exam preparation, professional certification — and `P40`'s “implement it yourself” does not
apply, because the decks and the review history already exist. 🔴 **`T48` is then the whole
engagement risk: the path the upstream RECOMMENDS is AGPL-3.0, installs in one click, and a
developer setting up a laptop will reach for it.**

| Role | Component | Licence (byte-read `2026-11-15`) | Posture |
|---|---|---|---|
| Agent surface | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** (`1,074 B`, `sha256:0ef87fdb…`) | 🟢 **`558★`, pushed `2026-11-07`. Adopt. Runs OUT of process** |
| 🔴 The refusal | [`ankimcp/anki-mcp-server-addon`](https://github.com/ankimcp/anki-mcp-server-addon) | 🔴 **AGPL-3.0-or-later** (`227 B`, `sha256:34b58d89…`) | 🔴 **REFUSE, in writing, and say why.** Same org, same function, `102★`; AGPL because it runs INSIDE Anki |
| The bridge | [`FooSoft/anki-connect`](https://github.com/FooSoft/anki-connect) | 🔴 **GPL-3.0-or-later** (`646 B`, `sha256:ddf0a4b0…`) — 🔴 GitHub says `NOASSERTION` | 🟡 **CALL, never vendor.** The user's own Anki runs it and answers HTTP on `127.0.0.1:8765`; a deliverable that calls it neither links nor distributes it |
| Measurement verbs | [`nietus/anki-mcp`](https://github.com/nietus/anki-mcp) | 🟢 **MIT** (`1,063 B`, `sha256:58f1e901…`) | 🔵 Topology reference for *"track retention, find leeches"* — the reporting half, which is what an institution pays for |
| Scheduling, if you change it | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** (`1,079 B`, `sha256:2ec9e6e6…`) | 🟢 **`4,137★`. Delivered as deck-options CONFIGURATION, not code — so tuning the schedule touches no licence at all** |

**Wiring.**
1. 🟢 **Write the boundary into the SOW before any code.** *"The agent runs as a separate
   process and reaches Anki over AnkiConnect's local HTTP API. We do not install the vendor's
   recommended MCP addon, because it is AGPL-3.0 and would reach your deliverable."* 🔵 **This is
   the deliverable clients remember, and `T48` is the argument for it.**
2. 🟢 **Pin the topology in the dev environment, not in a README.** The AGPL addon is one click
   in Anki's add-on browser. 🔴 **A convenience risk is only controlled by making the correct path
   the one already set up** — ship the `ankimcp` server in the project's own toolchain.
3. 🟢 **Build the reporting half, not the card half.** Retention curves, leech identification and
   cohort comparison over the review log. 🔵 **The cards already exist; the reporting does not,
   and `nietus/anki-mcp` shows it is only a few queries away.**
4. 🟢 **Tune scheduling with `fsrs4anki` configuration**, which is pasted into deck options and
   is therefore a settings change rather than a code dependency.
5. 🔴 **Second-order check, and it is not hypothetical:** AnkiConnect was last pushed
   `2025-11-04`, a year stale, and the entire out-of-process half of this layer depends on it. 🟢
   **Budget for the possibility that the client's Anki version outruns it, and keep `P40`'s
   schema as the exit — the review log is portable even when the application is not.**

🟡 **Copyleft in the tree: NONE. Copyleft called over a local HTTP boundary: one (`anki-connect`,
GPL-3.0-or-later), deliberately, documented.**
**Estimate: 3–4 weeks** for the agent and the reporting loop; **1 week** for the licence
documentation and environment pinning, which is not optional here.


## P42 — Retention EVIDENCE for mandatory training and certification recurrency (Global, the workforce half of `T23`, and the one recipe in this layer with an institutional buyer)

🔵 **Why it exists.** `T23` found assessment splitting into institutional and workforce halves,
and the retention tier (`verticals/solutions.md`, `p816`) found that every platform in it is
adopted by LEARNERS and bought by NOBODY. 🟢 **The gap is the opportunity: a regulated employer
must prove its people still know something they were certified on months ago, and no system it
operates can tell it that. Retention is the measurement it is missing, and compliance is a budget
line that already exists.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Scheduling core | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | 🟢 **MIT** (`1,079 B`, `sha256:021bff58…`) | 🟢 Server-side: recurrency is computed per cohort in batch, not per click |
| Front-end scheduling | [`open-spaced-repetition/ts-fsrs`](https://github.com/open-spaced-repetition/ts-fsrs) | 🟢 **MIT** (`1,079 B`, `sha256:8b83a73d…`) | For the review widget itself |
| Telemetry of record | **xAPI** into the employer's Learning Record Store | — | 🔵 **The whole deliverable is an auditable record, so it must land in the system the auditor already reads** |
| Internal review UI | [`appsmith/appsmith`](https://github.com/appsmith/appsmith) | 🟢 Apache-2.0 — already on this base's shelves | Compliance officers need a dashboard, not an app |
| Corpus authoring | Plain Markdown in the employer's repository, per `P40` | 🟢 **MIT** tooling | Training content is already controlled documentation; keep it there |
| Topology reference | [`nietus/anki-mcp`](https://github.com/nietus/anki-mcp) | 🟢 **MIT** (`1,063 B`, `sha256:58f1e901…`) | 🔵 Its *"track retention, find leeches"* verbs are exactly the compliance report, written for an individual learner |

**Wiring.**
1. 🟢 **Define the claim the artefact supports, first.** *"As of this date, `N%` of certified
   staff demonstrated retention of control `X` within the last `M` days."* 🔵 **Everything else
   follows from that sentence, and without it this is a flashcard app with a compliance label.**
2. 🟢 **Derive the card corpus from the controls**, one prompt per testable assertion in the
   existing training material — which is where an LLM earns its place, since the material is long
   and the assertions are buried in it.
3. 🟢 **Schedule with `py-fsrs` per learner per control**, and treat a lapsed interval as a
   RECURRENCY TRIGGER rather than a failure. 🔵 **That reframing is the sale: the employer stops
   retraining everyone annually and retrains the people whose retention actually decayed.**
4. 🟢 **Emit `xAPI` on every review and every lapse**, so the record is the auditor's, not the
   vendor's.
5. 🔴 **State the limit in the report itself.** Retention of a prompt is evidence about that
   prompt, not about competence. 🔵 **`P37`'s lesson, carried: an evidence deliverable survives
   challenge only where it does not overclaim — and an over-claimed compliance artefact is worse
   than none, because someone will rely on it.**
6. 🟢 **No copyleft, and no Anki.** The employer will not install a consumer flashcard
   application on managed devices, which is another reason `P40`'s algorithm-first shape is the
   only viable one here.

🟢 **No copyleft anywhere in the tree.**
**Estimate: 6–8 weeks** for one control family end to end including the xAPI record and the
compliance dashboard; **+2 weeks** per additional family.


## P37 — The appeal-survivable academic-integrity service (Global, and the first recipe in this base whose deliverable is EVIDENCE rather than a decision)

🔵 **Why this and not better detection.** `T45` measured the arms race and a studio cannot win
it: on `q="safe exam browser"` the bypass (`nxvvvv/safe-exam-browser-bypass`, `400★`) outstars
the client it defeats (`SafeExamBrowser/seb-win-refactoring`, `369★`), and
`school-cheating/SEBPatch` (`210★`) is a licence-compliant MPL fork of that client with a
byte-identical licence payload. 🟢 **What an institution is actually exposed on is not detection
rate — it is whether a finding survives a student appeal.** That is a record-keeping and
human-review problem, and it is buildable today, permissively, end to end.

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Similarity measurement | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** (`1,083 B`, `sha256:9e2ceeed…`) | 🟢 **MIT, so it ships inside the deliverable. Structural token comparison, NOT an LLM judge — the property that survives an appeal.** `jplag/JPlag` does the same at `2,012★` and is GPL-3.0 (`T44`) |
| Second-opinion method | [`AnubisLMS/Mayat`](https://github.com/AnubisLMS/Mayat) | 🟢 **MIT** (`1,074 B`, `sha256:eb0df6e4…`) | 🔵 AST-level rather than token-level: the two approaches fail on different evasions, so agreement between them is a far stronger finding than either alone. 🟡 Experimental, unpushed since `2024-04-10` — vendor the method, not the dependency |
| Method defensibility | [`jorge-martinez-gil/codesim`](https://github.com/jorge-martinez-gil/codesim) | 🟢 **MIT** (`1,074 B`, `sha256:15925095…`) | 🔵 The reference for explaining to a university committee WHY a similarity score means what it claims |
| Submission source | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **MIT** (`1,069 B`, `sha256:187d52a3…`) | 🟢 The only Canvas surface in this base that reaches **rubrics** as well as submissions. 🔴 **It also grades and comments — see step 4** |
| Evidence spine | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | 🟢 Already on this shelf via `P9`. An xAPI LRS is an append-only, timestamped, standards-shaped record — exactly what an appeal needs, and the institution can read it without the studio |
| Review UI | [`appsmith`](https://github.com/appsmithorg/appsmith) or the institution's own | 🟢 Apache-2.0 | The human-review queue; the point is that a human decides |

**Wiring.**
1. 🟢 **Submissions in, via `canvas-lms-mcp`'s read tools only.** Pull the assignment, the
   submission set and the rubric.
2. 🟢 **Measure twice — `Dolos` (token) and `Mayat`'s AST method — and record BOTH scores plus
   the pair-level evidence.** Agreement and disagreement are each informative; never collapse
   them to one number.
3. 🟢 **Write every step to the LRS as xAPI statements**: what was compared, with what version of
   what detector, at what time, against what cohort. 🔵 **Version the detector in the statement.
   A finding from a build nobody can identify is not evidence.**
4. 🔴 **NOTHING is written back to Canvas automatically.** `canvas-lms-mcp` can grade and comment,
   and that is precisely the capability to gate: a human reviewer opens the queue, reads the
   evidence pack, and decides. 🔵 **This is `P6`/`P22`'s publication gate, and `expeditto`'s
   `rascunho` principle, applied to the highest-stakes write in education.**
5. 🟢 **The deliverable is the evidence pack**: side-by-side extracts, both scores, the cohort
   distribution, the reviewer's identity and the decision, exportable as a single document.

🔴 **What NOT to sell.** Better lockdown, AI-based behavioural proctoring, or any claim of
detection accuracy. 🔴 **`q="proctoring exam open source"` → `total_count=12`, ceiling `4★`,
modal licence `NONE` (`T47`): there is no adoptable base, and the category is also the one the EU
AI Act names explicitly under Annex III.** 🟢 **An evidence-and-review layer, by contrast, is what
Annex III's human-oversight and record-keeping obligations actually ask for — so this pattern
reads as compliance work rather than as surveillance.**

🟢 **No copyleft anywhere in the tree.** Licence posture: shippable.
**Estimate: 6–8 weeks**, of which roughly two are the evidence schema and the appeal export.

## P38 — Permissive notebook-and-code assessment stack with a formative loop (Global, and the only fully permissive assessment stack this layer offers)

🔵 **Why it exists.** `T44` found that the assessment layer's star mass is copyleft and that the
component a studio most wants inside a product — `Judge0`, `4,519★` — is GPL-3.0. 🟢 **This recipe
is the proof that a complete assessment stack can be assembled with NO copyleft at all, which is
the thing to be able to say in a procurement conversation.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| Notebook autograding | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** (`1,559 B`, `sha256:4c5ec031…`) | 🟢 The most permissive grant in the layer. Python **and R** — the formats data-science and statistics teaching actually uses. UC Berkeley 🇺🇸, pushed `2026-11-14` |
| Alternative / incumbent | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | Already on this shelf. Check which the institution runs before proposing either |
| Notebook hosting | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause | Already on this shelf; the cohort-scale execution environment |
| Formative feedback loop | [`athina-edu/athina`](https://github.com/athina-edu/athina) | 🟢 **MIT, byte-read at `LICENCE`** (`1,098 B`, `sha256:dd7ad247…`) | 🟢 **Explicitly *"a formative assessment microservice for programming assignments"* — repeated feedback DURING the work, no record written.** 🔵 Maintained since `2019`, pushed `2026-11-13` |
| Exercise corpus | [`exercism/python`](https://github.com/exercism/python) + sibling tracks | 🟢 **MIT** | 🟢 **`q="exercism exercises"` → `total_count=4,960`. Graded exercises WITH test suites in `70`+ languages under MIT — `rust`, `go`, `java`, `javascript` all pushed `2026-11-15`.** 🔵 Removes content authoring from the critical path entirely |
| Integrity check | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** | Chain `P37` behind this rather than duplicating it |
| Platform, if one is needed | [`autolab/Autolab`](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** (`11,323 B`, `sha256:6dc0e068…`) | 🟢 **The permissive answer to `Judge0`: roster, submissions, autograding and scoreboards in one.** 🔴 It competes with the LMS for the assessment job — a procurement conversation, not a technical one |

**Wiring.**
1. 🟢 **Start FORMATIVE, not summative.** `athina` gives feedback while the student works; no
   grade is written. 🔵 **This is the lowest-risk shape in the entire assessment layer: with no
   record written, neither `T36`'s integrity axis nor the EU AI Act's high-risk grading trigger
   is engaged** — which makes it the right first phase of any engagement here.
2. 🟢 **Source the exercises from `exercism` tracks** rather than authoring them. They arrive with
   test suites, which is what the autograder consumes.
3. 🟢 **Grade with `otter-grader` on JupyterHub** for notebook work; add `Autolab` only if the
   institution needs roster, submission handling and scoreboards it does not already have.
4. 🟡 **Put an agent in front, not inside.** `himanshuuem/lab-autograder` (MIT, `1★`) is the only
   result on `q="autograder mcp"` (`total_count=1`) and hand-rolls its own Docker sandbox — 🔵
   **take its topology as the reference and point it at `otter-grader`, which already solved the
   execution problem properly.**
5. 🔴 **Phase 2 only, and explicitly: summative grading writes to a record.** Gate it with
   `P37`'s human-review step. Do not let phase 1's low risk posture carry over by default.

🟢 **No copyleft anywhere in the tree, and no GPL dependency even transitively.**
**Estimate: 4–6 weeks** for the formative phase; **+4 weeks** for summative with the review gate.

## P39 — Natural-language timetabling on a real solver (Global, cheapest credible "AI" engagement in this file because the hard part is already Apache-2.0)

🔵 **Why it is a good engagement and an easy sell.** Course and exam timetabling is a genuine
constraint-satisfaction problem with a hard deadline every single term, the incumbents are
expensive proprietary schedulers, and 🔴 **an LLM is the WRONG tool for the solve** — it will
produce a plausible timetable that violates constraints. 🟢 **`UniTime` already solves it, is
Apache-2.0, and is deployed at *"universities in North America and Europe"* per its own README.
The value a studio adds sits strictly ON TOP of the solver.**

| Role | Component | Licence (byte-read `2026-11-15`) | Why this one |
|---|---|---|---|
| The solver | [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** (`11,357 B`, `sha256:58d1e17f…`) | 🟢 **The only constraint-solver platform in this base, forkable and shippable. `358★`, pushed `2026-11-13`.** Course, exam and student scheduling with multiple departmental managers |
| Schools-scale alternative | [`GEOSOFT-GLOBAL/timetablely`](https://github.com/GEOSOFT-GLOBAL/timetablely) | 🟢 **MIT** (`1,070 B`, `sha256:b4be7f0d…`) | 🟡 `27★`. For a school rather than a university — the choice is scale, not licence |
| Roster / enrolment in | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) or Ed-Fi `Data-Management-Service` | 🟢 Apache-2.0 | Already on this shelf via `P27`/`P11`. Courses, sections, staff and enrolments are the solver's input |
| Constraint capture + explanation | 🔵 **Build** — `pydantic-ai` or `LangGraph` over the solver's API | 🟢 MIT | 🔵 **This is the whole deliverable; see wiring** |
| Audit record | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | Who asked for what, what the solver said, what was overridden |

**Wiring, and the division of labour is the point.**
1. 🟢 **The LLM NEVER places a class.** It translates a human request — *"Dr Okafor cannot teach
   Friday afternoons and the two first-year labs must not clash"* — into `UniTime` constraint
   objects, and validates them against the schema before submitting.
2. 🟢 **`UniTime` solves.** Deterministic, explainable, and the same answer twice for the same
   input — none of which an LLM provides.
3. 🟢 **The LLM explains the REFUSAL, which is where the actual human pain is.** When a request
   cannot be satisfied, the solver reports an infeasibility; the agent turns that into *"your
   request conflicts with the Tuesday lab because room B210 is the only one with the equipment,
   and moving it would break three other sections"* — and proposes the two or three relaxations
   that would make it feasible.
4. 🟢 **Every request, solve and override goes to the LRS**, because timetable disputes are
   political and the record is what settles them.
5. 🔵 **Phase it to the academic calendar.** The engagement has a natural deadline the client
   already feels, which is the easiest kind of engagement to scope and the easiest to renew.

🟢 **No copyleft anywhere in the tree.** 🔵 **And an unusually honest pitch: the studio is not
claiming to have invented the scheduler. It is claiming that a twenty-year-old Apache-2.0 solver
plus a language layer beats a proprietary licence renewal — which is checkable, and therefore
credible.**
**Estimate: 6–8 weeks**, dominated by constraint-schema mapping, not by the language layer.

## P34 — Citation-integrity service for a university (Global, and the first integrity-POSITIVE recipe in this base)

🔵 **Who buys it.** A graduate school, a research office or an academic-integrity office that has
no mechanical way to tell an invented citation from a real one, and is currently reading theses
by hand. 🟢 **Every other recipe in this file reduces an agent's capacity for harm. This one sells
a capability that DETECTS harm, which is a different conversation with a different budget.**

**Components, all licence-verified by byte-read on 2026-11-13:**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Integrity engine | [`oscardvs/zoteus`](https://github.com/oscardvs/zoteus) | **MIT** (`1,067 B`, `sha256:c20cd2f8…`) | `zotero_check_citations` reads a Markdown/LaTeX/plain-text draft, finds every citation form (pandoc, `\cite`, author-year, numeric, DOI, `[@ITEMKEY]`), reports which are in the library, ambiguous or absent, then looks up each direct quotation in the cited PDF — found with its page, close (with the source's real wording), or not found. It is read-only and checks wording, not meaning |
| Reference store | [`zotero/zotero`](https://github.com/zotero/zotero) | 🟡 **AGPL at `COPYING`** | The library itself. 🔴 **Integrate over the Zotero 10+ local API or Web API v3 — never derive** |
| Catalogue verification | [`leomcamilo/bx-scholar-mcp`](https://github.com/leomcamilo/bx-scholar-mcp) | **MIT** (`1,071 B`, `sha256:af97dd08…`) | OpenAlex + CrossRef with no credential and no paywall, to resolve a DOI the local library does not hold |
| Norm layer (🇧🇷 only) | [`PedroSmaxY/abnt-mcp`](https://github.com/PedroSmaxY/abnt-mcp) | **MIT** (`1,086 B`, `sha256:1cdab623…`) | ABNT NBR 6023/10520:2023 reference and citation conformance on top of existence |

**How it wires together.**

1. 🟢 **Ingest the draft, not the student's account.** The service takes a file. 🔵 **No learner
   credential enters the system at all, which clears `T36` axis (a) by construction rather than
   by configuration.**
2. 🟢 **Resolve every citation against the supervisor's or department's Zotero library** via
   `zoteus`, running against the local API so nothing leaves the institution.
3. 🟡 **Anything unresolved goes to `bx-scholar-mcp`** for an OpenAlex/CrossRef lookup — an open
   catalogue, so axis (c) stays 🟢 **clean**. 🔴 **Do NOT add a full-text retriever here. That is
   where `T40`'s structural grade enters a design, and it is not needed: existence and wording
   are checkable from metadata plus the PDFs the library already holds.**
4. 🟢 **Quotation verification is the differentiator** — `zoteus` looks the quotation up in the
   cited PDF and reports *found with page / close with the source's real wording / not found*.
   🔵 **"Close, and here is what the source actually says" is the output an integrity office
   cannot currently produce at all.**
5. 🇧🇷 **In Brazil, chain `abnt-mcp` after step 4** so the same pass returns norm defects
   (NBR 10520:2023 mixed-case author-date, 4 cm long quotations, NBR 6023 reference layout)
   alongside integrity findings.
6. 🟢 **Deliver as a report, never as a verdict.** The output names the finding and the evidence;
   a human adjudicates. 🔵 **Under the EU AI Act this keeps the deployment out of the
   access/admission/evaluation high-risk triggers — see `P2` — and it is the right design
   everywhere else too.**

**Licence consequence.** 🟢 **The whole chain is MIT and forkable. Zotero is AGPL and stays
behind its protocol boundary.** **Rough build: 4–6 weeks** for the pipeline, the report format
and the institutional Zotero integration; add 1–2 weeks for the ABNT chain.

🔵 **The honest limitation to state in the proposal:** it checks wording, not meaning. A correctly
quoted source that does not support the claim will pass.

## P35 — Sovereign institutional-repository agent (EMEA, and the only permissive platform fork in the education stack)

🔵 **Who buys it.** A European university, national library or research institute that wants
discovery and summarisation over its own holdings, cannot send unpublished work to a SaaS, and
has an AI Act `deployer` obligation to discharge. 🟢 **This is the recipe where the licence is the
differentiator.**

**Components, all licence-verified by byte-read on 2026-11-13:**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Platform | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | 🟢 **BSD-3-Clause** (`1,504 B`, `sha256:baf9ee18…`) | 🟢 **The ONLY major education platform that is permissively licensed — forkable, embeddable, shippable inside a deliverable. DSpace 7+ ships a published REST API** |
| Agent surface | [`mpasternak/dspace-mcp`](https://github.com/mpasternak/dspace-mcp) | **MIT** (`1,073 B`, `sha256:900b820e…`) | *"Read-only by construction, not by promise"*; env-var-first credentials with keychain guidance; restricted files require `get_download_link` rather than the raw `download_url` |
| Rights-check pattern | [`suren-kk/armenian-national-library-mcp`](https://github.com/suren-kk/armenian-national-library-mcp) | **MIT** (`1,072 B`, `sha256:b47a07d3…`) | 🟢 **Copy its sequence: rights review BEFORE retrieval. Writes are not implemented; links and redirects must stay HTTPS on the exact host; bounded text extraction with MIME verification; hardened Compose profile (`127.0.0.1` only, read-only rootfs, dropped capabilities)** |
| Journal arm (optional) | [`mpasternak/ojs-mcp`](https://github.com/mpasternak/ojs-mcp) | **MIT** (`1,096 B`, `sha256:56a6229a…`) | The university's own journals, with `OJS_ALLOW_WRITES=1` off by default |
| Catalogue arm (optional) | [`asjolaviral/koha-mcp-server`](https://github.com/asjolaviral/koha-mcp-server) | **MIT** (`1,084 B`, `sha256:a8be4d3f…`) | Koha via OAuth2 `client_credentials` — the only non-password auth in this base |

**How it wires together.**

1. 🟢 **Deploy against the institution's existing DSpace.** Nothing is migrated. 🔵 **The
   institution is the rights holder for its own theses, datasets and open-access output, so axis
   (c) is 🟢 **clean by ownership** — the strongest position any recipe in this file has.**
2. 🟢 **Front it with `dspace-mcp`, read-only.** 🔵 **"Read-only by construction" is a sentence an
   AI Act conformity file can carry; "read-only by promise" is not.**
3. 🟢 **Insert the Armenian server's rights gate before any file retrieval**, including for
   material the institution hosts but does not own the rights to (deposited third-party work).
4. 🟡 **Week-zero prerequisites the studio does NOT own:** OJS needs `api_key_secret` in
   `config.inc.php`, Koha needs its REST API enabled plus an OAuth2 key pair. 🔵 **Both are
   institutional admin actions — put them in the kick-off checklist or the first sprint stalls.**
5. 🟢 **Keep it off the high-risk triggers.** Discovery and summarisation over holdings does not
   determine access, admission or evaluate learning outcomes. 🔴 **The moment someone asks for
   "assess this thesis", the deployment changes category — refuse or re-scope.**

**Licence consequence.** 🟢 **DSpace BSD-3-Clause plus four MIT agents: the entire stack can be
forked, modified and shipped with attribution only.** **Rough build: 6–8 weeks**, plus 2 weeks per
optional arm.

## P36 — Norm-compliance pipeline for Brazilian academic writing (LATAM, and the norms do the selling)

🔵 **Who buys it.** A Brazilian university, federal institute or graduate programme whose staff
check ABNT conformance by hand on every TCC, dissertation and thesis, every term. 🟢 **The norms
are published, numbered and mechanically checkable, which makes this the most concretely scoped
recipe in this file.**

**Components, all licence-verified by byte-read on 2026-11-13:**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Norm engine | [`PedroSmaxY/abnt-mcp`](https://github.com/PedroSmaxY/abnt-mcp) | **MIT** (`1,086 B`, `sha256:1cdab623…`) | Implements NBR 14724 (structure, typography, `3-3-2-2` pagination), NBR 10520:2023, NBR 6023, 6022, 6024, 6027, 6028 and IBGE tabular rules, and flags revoked practice (*"prática formalmente extinta pela atualização da ABNT NBR 10520:2023"*) |
| Authoring | [`trahloff/Aldine`](https://github.com/trahloff/Aldine) | 🔴 **AGPL-3.0** (`34,522 B`, `sha256:4df3c306…`) | Self-hosted collaborative LaTeX. 🔵 **Self-hosting IS the pitch for unpublished research.** 🔴 **Offering it to students triggers the network-use source obligation: deploy it, never fork it into a product** |
| Citations | [`oscardvs/zoteus`](https://github.com/oscardvs/zoteus) | **MIT** | CSL formatting into the draft, plus `zotero_check_citations` — chain `P34` behind this |
| Publication | [`pkp/ojs`](https://github.com/pkp/ojs) | 🔴 **GPL-3.0** (`35,148 B`, `sha256:8b1ba204…`) | The university's journals; agent surface `mpasternak/ojs-mcp` (MIT), writes off by default |
| Translation (optional) | [`PDFMathTranslate/PDFMathTranslate`](https://github.com/PDFMathTranslate/PDFMathTranslate) | 🔴 **AGPL-3.0** (`34,522 B`, `sha256:20b067f8…`) | Layout-, formula- and table-preserving translation of English-language literature for a Portuguese-language cohort. 🔴 **Separate service only** |

**How it wires together.**

1. 🟢 **The student writes in Aldine, self-hosted inside the institution.**
2. 🟢 **`abnt-mcp` audits the manuscript against the norms by number**, returning defects with the
   NBR clause attached. 🔵 **A defect that cites "NBR 10520:2023" is actionable; "citation style
   looks wrong" is not.**
3. 🟢 **`zoteus` formats the references and then checks them** — chain `P34` here so norm
   conformance and citation integrity arrive in one report.
4. 🟡 **On submission, `ojs-mcp` reads the journal's requirements**; 🔴 **leave
   `OJS_ALLOW_WRITES` off — a human submits.**
5. 🔴 **Draw the licence boundary at process edges:** Aldine (AGPL), OJS (GPL) and
   PDFMathTranslate (AGPL) each run as their own service. 🟢 **Only the MIT components —
   `abnt-mcp`, `zoteus` — are forked into the deliverable.**

**Why it passes the integrity grade.** 🟢 **`abnt-mcp`'s capability set is *auditoria, formatação
formal, consulta em bases indexadas e compilação para PDF*: it audits and formats a document the
student wrote. It is not a ghostwriter, and the proposal should say so in those words** — because
the first question any Brazilian graduate programme will ask is whether this writes the thesis.

**Rough build: 6–8 weeks** for the audit-plus-integrity pipeline on an existing Aldine or Overleaf
install; add 3–4 weeks for the OJS submission arm. 🔵 **Adjacent open slot, measured this pass:
`q="enem vestibular mcp agente"` → `total_count=0`. Brazil's national admissions system has no
agentic surface of any licence.**

## P1 — Compliance-safe practice tutor (North America, restrictive states)

**Problem:** the client wants an AI tutor, but Texas HB 2400 bars AI from
delivering direct classroom instruction, New York limits classroom AI to grade
9+, and Chicago-style district rules bar AI as the sole basis for high-stakes
decisions.

**Wiring:**
1. **Mastery/progression engine — outside the model.**
   `pykt-team/pykt-toolkit` (MIT) for knowledge tracing, or `CAHLR/OATutor`
   (MIT) if Bayesian Knowledge Tracing over an existing item bank is enough.
2. **Item bank and renderer.** `Khan/perseus` (MIT) for real exercise
   rendering and authoring.
3. **Agent role, scoped deliberately to practice and feedback.** Adapt
   `HKUDS/DeepTutor` (Apache-2.0) — use its learner-model and learning-path
   machinery, disable instruction delivery; the human teacher instructs.
4. **LMS mount.** `Cvmcosta/ltijs` (Apache-2.0) as the LTI 1.3 tool provider
   into Canvas; for agent-side access use `vishalsachdev/canvas-mcp` (MIT).
5. **Telemetry.** Emit Caliper (`1edtech/caliper-spec` — implement the spec, do
   not vendor the repo) plus an audit log of every agent action with the grade
   level and state policy applied.
6. **Policy gate.** A configuration layer keyed to state and district: grade
   floor, instruction-delivery off, human-in-the-loop gate on anything
   decision-shaped, logging retention, FERPA/COPPA posture. NYC's
   green/yellow/red tiers map directly onto a tool allowlist per tier.

**License outcome:** entire AI layer MIT/Apache; Canvas stays separate behind
LTI, so AGPL does not reach the deliverable.

**Estimate:** 8–10 weeks. **Sells because** it is the tutor that is legal where
a general tutor is not.

---

## P2 — EU AI Act high-risk conformity layer for assessment AI (EMEA)

**Problem:** the institution already runs AI touching assessment or admissions.
Under the AI Act that is high-risk in principle (Annex III covers access,
allocation, assessment and monitoring of pupils during tests). Obligations for
stand-alone Annex III systems are set at **2027-12-02** by Regulation (EU)
2026/1744 (published in the OJ 2026-07-24), with transparency duties from
August 2026 and **2028-08-02** for AI embedded in regulated products. Emotion
recognition in education has been banned since February 2025. Some vendor
guides still assert August 2026 for high-risk obligations — **verify on EUR-Lex
before committing to a timeline**, and expect clients who believe they are
already late.

**Wiring:**
1. **Inventory and classify.** Enumerate every AI touching admissions,
   assessment, progression or monitoring; classify against Annex III; record
   the low-risk exception argument where it applies.
2. **Human oversight layer.** A review queue in front of every consequential
   output: no automated decision without a named human decision-maker. The
   `EDUKAI-LONGVIEW` framing — "agent recommends, teacher decides" — is the
   right interaction model even though the repo itself is a prototype.
3. **Logging and traceability.** Append-only event log of inputs, model
   version, prompt, output, reviewer and outcome. Emit **xAPI** for the
   institution's own reporting.
4. **Mastery state outside the model**, so assessment decisions are explainable
   from `pykt-toolkit` (MIT) outputs rather than from model text.
5. **Sovereign deployment.** Self-hosted open weights, institution-controlled
   infrastructure — Council of the EU document ST-14902-2026 (2026-10-29) makes
   reduced dependence on non-European AI explicit for education and training,
   so this is procurement-relevant, not ideological.
6. **Platform mount without forking.** `ltijs` (Apache-2.0) into Moodle/ILIAS,
   plus `Faixiang/Moodle-MCP` (MIT, read-only) for agent read access — the
   read-only surface is an asset in a conformity story.
7. **Documentation pack.** Risk management file, data governance,
   instructions-for-use, post-market monitoring plan.

**License outcome:** Moodle/ILIAS untouched (no fork); all added components
MIT/Apache.

**Estimate:** 12–16 weeks. **Highest-value regulated education work globally.**

---

## P3 — Pick and harden a Moodle MCP server (Global, reusable asset)

**Problem:** the client runs Moodle — the most-deployed LMS in the world and
the incumbent across EMEA, LATAM and APAC public education — and wants agents
to work inside it. **Previously this KB called this greenfield. It is not.**
Seven servers exist; none is production-hardened, and they disagree on
everything that matters.

**The selection matrix (all verified 2026-11-13):**

| Server | License | Stars | Surface | Auth | Pick when |
|---|---|---|---|---|---|
| `Faixiang/Moodle-MCP` | MIT | 206 | 10 tools, **read-only** | Web-service token | Default. First engagement, security review pending, or read-only is genuinely enough |
| `G36maid/moodle-mcp` | MIT | 29 | Courses, assignments, forums, grades, files-as-markdown (Rust) | Token | Widest version coverage (verified 3.7 / 4.5 / 5.2); single-binary deployment |
| `falkenslab/moodle-mcp` | MIT | 2 | **~260 tools** incl. grading, quiz building | **Interactive browser login, SSO + 2FA, no token, no plugin** | The institution refuses to issue web-service tokens, or SSO/2FA is mandatory |
| `MarcosNahuel/moodle-mcp` | MIT | 1 | 40 tools + `ws_raw`, **idempotent upsert-by-`idnumber`** | Token + companion plugin `local_italiciamcp` | Agents must *publish* course content repeatedly without creating duplicates |
| `csmediapro/...` | AGPL-3.0 | 2 | 10 core + paid premium tools | Token | Avoid for client deliverables: copyleft plus commercial upsell |
| `lmscloud-io/...` | GPL-3.0 | 1 | Unstated | Token | Avoid for client deliverables |

**Wiring:**
1. **Fork the MIT server whose auth model matches the client's security
   posture** — this is the decision, not the star count. Token-issuance policy
   usually decides it.
2. **Harden:** pin Moodle version compatibility, add structured errors,
   rate-limit, scope the token or session to least privilege, add an audit log
   of every tool call with the acting user.
3. **Add write safety.** If writes are in scope, port `MarcosNahuel`'s
   upsert-by-`idnumber` idempotency pattern regardless of which server you
   started from. Generated content gets republished; duplicates are the default
   failure mode.
4. **Emit xAPI** for every agent action so the institution can report on it.
5. **Pair with `ltijs`** (Apache-2.0) when the same engagement needs a
   student-facing tool surface, not just agent access.

**License outcome:** MIT server, reusable across every Moodle engagement in
EMEA, LATAM and APAC.

**Estimate:** **3–5 weeks** to harden a chosen MIT server (down from the 5–7
weeks a from-scratch build was estimated at). **Build once, bill many.**

---

## P4 — Institutional AI governance package (LATAM, productized)

**Problem:** UNESCO IESALC across 200 institutions in 19 countries — 87% use
AI, 26% have a framework, 55% have no AI budget, 9% evaluate. Brazil's Cetic.br
— 53% of administrators use AI, 22% of schools have a guideline. The
institution is already exposed and cannot afford a frontier-API product.

**Wiring:**
1. **Policy artifact first**, mapped to the national instrument that applies
   (Brazil PL 2.338/2023 risk tiers; Colombia CONPES 4144; OECD AI Principles
   where adopted) and to UNESCO IESALC's framework categories.
2. **Cheap-to-run inference.** Self-hosted open weights. Where connectivity is
   the constraint, `learningequality/kolibri` (MIT, offline-first) as the
   delivery platform.
3. **Evaluation harness — the differentiator, because 9% evaluate.**
   🔴 `kaushal0494/AITutor-EvalKit` (**NO licence file — not adoptable; `p801`
   refuted the `MIT` claim and `p802` re-verified the absence at `HEAD`
   `a71078456a90`. Read it, do not ship it**) for pedagogical effectiveness,
   `pykt-team/pykt-toolkit` (MIT) for mastery measurement, xAPI/Caliper
   telemetry into a dashboard. Thin upstream; say so, and own the gap.
4. **Teacher enablement** in Spanish/Portuguese — the one intervention every
   framework mandates.
5. **Content localization.** `satvik314/educhain` (MIT) and `oppia/oppia`
   (Apache-2.0) against national curricula (ENEM, ICFES, PAES, SEP). Shortcut:
   `THU-MAIC/OpenMAIC` (MIT) **already ships pt-BR and es-MX locales**.
6. **Platform mount.** Moodle or Chamilo (both PHP → `packbackbooks/lti-1-3-php-library`,
   Apache-2.0), plus `Faixiang/Moodle-MCP` (MIT) for agent read access.

**License outcome:** fully permissive AI layer; platforms untouched.

**Estimate:** 6–8 weeks per institution after the first; **the first build is
the product.** Ceibal (Uruguay) is the template for the ministry-scale version.

---

## P5 — Multi-jurisdiction compliance architecture (APAC)

**Problem:** a regional university group or edtech vendor faces Korea's AI Basic
Act (in force 2026-01-22, education = high-impact), Vietnam's binding AI law
(education high-risk, **pre-deployment registration and human oversight**,
implementing decree April 2026, compliance runway reported as late as September
2027), Australian TEQSA generative-AI risk management plans, Chinese content
labelling and algorithm registration, and the EU AI Act for anything sold into
Europe — simultaneously.

**Wiring:**
1. **One policy-enforcement layer, per-jurisdiction configuration.** Model
   obligations as declarative policy (allowed uses, registration state, human
   oversight requirement, logging retention, labelling duty), evaluated per
   request with the jurisdiction as an input.
2. **Policy as graph nodes, not prompt text.** Route every agent action through
   the policy evaluator; deny-by-default on unconfigured jurisdictions.
3. **Registration and evidence store.** Vietnam requires pre-deployment
   registration — keep the artifacts (system description, oversight design,
   test evidence) as first-class records, versioned with the deployed model.
4. **Human oversight queue** satisfying Vietnam and TEQSA in one mechanism.
5. **Content labelling** for China-facing deployments, emitted at generation
   time rather than retrofitted.
6. **Agent layer.** `HKUDS/DeepTutor` (Apache-2.0) or `THU-MAIC/OpenMAIC` (MIT)
   — regionally built, permissively licensed, already multi-locale.
7. **Sovereign deployment** per data-residency mandate; self-hosted weights.

**License outcome:** MIT/Apache throughout.

**Estimate:** 12–14 weeks. **The compliance layer is the product**; the tutor is
the demo. Note the politics: Ipsos Education Monitor 2026 shows support for
banning AI in schools **rising in Japan and South Korea** — lead with P7's
teacher-augmenting framing in those two markets.

---

## P6 — Agent-assisted grading and feedback (Global, still the open field)

**Problem:** grading is the highest-volume teacher workload and there is no
dominant open-source grading agent anywhere in the world. This remains the
clearest build opportunity in this KB.

**Wiring:**
1. **Start from the one real open system.** `wwrwbs/AI_AWE` (Apache-2.0 per
   README/LICENSE, 2 stars) is a complete pipeline worth copying structurally:
   fine-tuned Qwen2.5-7B LoRA **discourse-move classifier** → **LightGBM
   scorer over 31 linguistic/discourse features** → **label-aware feedback
   generator**, with a Gradio UI for single and batch scoring, locally
   deployable. **Citation trap:** the arXiv paper calls this "ArguLens"; the
   repository never uses that name.
2. **Why that shape matters:** the score comes from an interpretable feature
   model, not from model text. That is what makes it defensible to a regulator
   and auditable to a department — the same principle as keeping mastery state
   outside the model.
3. **Code and notebook assignments.** `jupyter/nbgrader` (BSD-3-Clause) is the
   autograding substrate; the agent adds feedback on top of deterministic test
   results, never replaces them.
4. **Rubric as data, not prompt.** Version rubrics; bind every score to a
   rubric version and keep the mapping explicit.
5. **Human-in-the-loop by construction.** Agent proposes score + evidence +
   feedback; teacher confirms. Required outright by Chicago-style district
   rules and by the EU high-risk oversight duty, and it is the only posture
   that survives an appeal.
6. **Calibration harness.** Hold back human-scored work and report
   agreement (quadratic weighted kappa against human raters) per cohort. Without
   this the client cannot defend the system, and only 9% of LATAM institutions
   evaluate anything today.
7. **LMS writeback.** Grades go back through **LTI Assignment & Grade
   Services** — supported by `ltijs` (Apache-2.0) and
   `packbackbooks/lti-1-3-php-library` (Apache-2.0). Do not write to the
   gradebook out of band.

**License outcome:** BSD/MIT/Apache throughout.

**Estimate:** 8–10 weeks for one discipline. **Still open space** — the entire
field is one 2-star Apache-2.0 prototype, notebook autograding infrastructure,
and Kaggle-era coursework.

---

## P7 — Teacher distillation (APAC and Global, politically safest shape)

**Problem:** the institution wants AI leverage without student-facing autonomy
— because policy forbids it (Texas HB 2400), because public opinion is turning
(Ipsos 2026: ban support rising in Japan and South Korea), or because the
faculty will not accept a tutor that replaces them.

**Wiring:**
1. **Distil the teacher, not the subject.** `JuneYaooo/teacher-to-skills`
   (Apache-2.0, 475 stars) converts a named teacher's own materials — lecture
   video, notes, marked-up feedback — into a source-backed agent Skill that
   teaches to *that teacher's* standard and tapers support as the learner
   improves.
2. **Two properties to preserve when adapting it:** conclusions are tied back
   to source material, and **material without evidence is flagged rather than
   filled in**. That is the anti-hallucination contract that makes faculty sign
   off, and it is worth keeping even if you rewrite everything else.
3. **Learner progress stored outside the generated Skill** — as the upstream
   project already does. Same principle as P1/P2/P6.
4. **Lesson and material drafting for the teacher.** `SirhanMacx/Claw-ED` (MIT,
   65 stars) drafts lessons, student materials and slides from the teacher's
   existing plans, local-first. **Read its limits before promising anything:**
   single-teacher per instance, not multi-tenant, student-facing features
   experimental, and hosted models still receive prompt content even though
   storage is local — so a data-residency client needs local weights.
5. **Content generation node.** `satvik314/educhain` (MIT) for questions,
   lesson plans and flashcards.
6. **Classroom simulation for teacher training.** `THU-MAIC/OpenMAIC` (MIT)
   turns a topic into a multi-agent classroom — useful for rehearsing a lesson
   or training new teachers, which is a sale to the institution rather than to
   students.
7. **Mount and measure.** `ltijs` (Apache-2.0) into the LMS; emit xAPI; keep
   the teacher as the named decision-maker on anything consequential.

**License outcome:** Apache-2.0/MIT throughout.

**Estimate:** 6–8 weeks. **Sells because** the deliverable augments the people
who would otherwise block it — and because it is the one tutor shape that is
legal and politically survivable in every region in this KB.

---

## P8 — Agent on the student record (Global, topology proven; now scoped to RosarioSIS and Gibbon — check `P12` first)

**Problem:** advising, retention and early-warning are the use cases
institutions ask for most, and they all need the **student information
system** — not the LMS.

**Status changed 2026-11-13 (fourth pass).** This pattern was titled "nothing
exists" through three passes. It is no longer greenfield: **two MIT MCP servers
reach a real SIS** — `oliverhruby/edupage-mcp` (4 stars, **31 tools** over
EduPage, the SIS used across Slovakia and Czechia, including role-aware student
switching and 2FA) and `sukhrobyangibaev/mcp_hemis_student` (0 stars, over
HEMIS, used by Uzbek universities). Both are single-developer projects against
**national proprietary platforms**, and EduPage's runs on **undocumented
endpoints** through a community library.

**Status changed again 2026-11-13 (fifth pass) — read this before the paragraph
below it.** The sentence *"not one open-source SIS has an agent interface"* is
**withdrawn**. **OpenEduCat (LGPL-3.0, 911 stars, 789 forks) is reachable
today** by a generic Odoo MCP server, because it is Odoo addons and those
servers address models by name. **If the client runs OpenEduCat — or any
Odoo-based education ERP — do not use this pattern; use `P12`, which is a
configuration exercise rather than a build.** `P8` below remains the right
pattern for the two cases that are still genuinely unserved: **RosarioSIS**
(GPL-2.0, 654, PHP/Postgres, LATAM K-12) and **Gibbon** (GPL-3.0, 638,
PHP/MySQL, international K-12), neither of which has a general-purpose platform
underneath to inherit a connector from. 🔴 **`frappe/education` is unresolved —
check for a generic Frappe MCP server before quoting this pattern for it.**

**What that changes for the engagement:** the topology is proven, so this is a
**selection-and-build** pattern rather than a bet — cheaper to sell and faster
to de-risk, because `edupage-mcp` is a working reference for the tool surface
(31 tools over timetable, grades, homework, attendance) and
`zavora-ai/mcp-education` (Apache-2.0) is a working reference for **gating
writes in the tool contract**: 9 read-only tools plus 3 writes that require
approval. 🔴 **Superseded sentence, kept visible rather than deleted so the
correction is auditable:** this pattern used to continue *"What has not changed:
not one open-source SIS — OpenEduCat, RosarioSIS, Gibbon, openSIS,
`frappe/education` — has an agent interface."* **OpenEduCat has one** (see the
fifth-pass note above and `P12`), so the unserved list is now **RosarioSIS,
Gibbon, openSIS**, with `frappe/education` **unresolved pending one search for a
generic Frappe connector**. For those, the build below is still the work —
**quote the proven topology, not a solved problem.**

**Wiring:**
1. **Pick the SIS by region.** `openeducat/openeducat_erp` (LGPL-3.0) where
   Odoo is already in place; `francoisjacquet/rosariosis` (GPL-2.0) for LATAM
   K-12; `GibbonEdu/core` (GPL-3.0) for international K-12;
   `OS4ED/openSIS-Classic` for existing openSIS estates.
2. **Build the MCP server as a separate MIT/Apache process against the SIS
   API** — never as a fork or an in-tree plugin, because all four SIS options
   are GPL-family. The license boundary is the whole architecture here.
3. **Read-only first**, and probably read-only permanently. The student record
   is the most sensitive data in the institution; `Faixiang/Moodle-MCP`'s
   read-only design is the precedent to copy. **If writes are unavoidable**, copy
   `zavora-ai/mcp-education`'s contract instead of inventing one: declare the
   read-only and approval-required tools as **separate, labelled sets in the
   server itself**, so the boundary survives a change of host and shows up in an
   audit. Leaving write-gating to the agent host is the failure mode.
3b. **Steal the tool surface rather than designing it.** `edupage-mcp`'s 31
   tools are a worked answer to "what does an agent need from a school SIS"
   (timetable, grades, homework, attendance, daily summary, role-aware student
   switching, 2FA), and `EdyVision/student-services-mcp` — **license
   unverified, synthetic data, do not adopt** — sketches the retention surface
   an advising agent needs: `fetch_student_dropout_risk`,
   `fetch_high_risk_students`, `fetch_attrition_statistics`,
   `fetch_attrition_feature_importance`. Two free references for the hardest
   design question in this pattern.
4. **Longitudinal framing.** `Keitous/EDUKAI-LONGVIEW` (ISC, 0 stars, Guinea)
   is the only project found that models a learner **across academic periods**
   with evidence retrieval and recurring-difficulty detection, under "agent
   recommends, teacher decides". It is a prototype on synthetic data — take the
   design, not the code.
5. **Join to learning data — now with named implementations.** Mastery
   estimates from `pykt-toolkit` (MIT) plus xAPI events give the agent
   behavioural signal the SIS does not hold. As of 2026-11-13 the xAPI side is
   no longer abstract: stand up `yetanalytics/lrsql` (Apache-2.0) or
   `openfun/ralph` (MIT) as the Learning Record Store and read it through
   `DavidLMS/learnmcp-xapi` (MIT) — see `P9`, which is the buildable half of
   this pattern. **Keep the distinction explicit in the SOW: the LRS holds
   learning activity, the SIS holds the student record.** P9 ships today; this
   pattern still requires the SIS MCP server to be built.
6. **Human-in-the-loop, hard.** Chicago's rule — no AI as the sole basis for
   discipline or special-education placement — is the floor, and the EU treats
   access and allocation decisions as high-risk. Every output is a
   recommendation with evidence attached, routed to a named human.
7. **FERPA/GDPR posture** stated up front: self-hosted inference, no student
   data to model training (and if California AB 1159 passes, that becomes a
   statutory requirement, not a preference).

**License outcome:** MIT/Apache agent layer; GPL-family SIS untouched behind
its own API.

**Estimate:** **5-7 weeks** for a read-only advising surface on one SIS, revised
down from 6-8 now that the tool surface and the write-gating contract both have
working references to copy rather than needing design from scratch. Still
**nothing to compete with on any open-source SIS**, and it is the layer the ask
actually requires.

## P9 — The learner-record spine (Global, buildable today, permissive end to end)

**New 2026-11-13.** This is `P8`'s buildable half. `P8` needs an SIS MCP server
that does not exist; **P9 needs nothing that does not exist**, and every
component is MIT or Apache-2.0.

**Problem:** every other pattern in this file tells the agent to "emit xAPI so
the institution can report on it", and until this pass no repo in this KB
implemented the receiver. The practical consequence in delivery is familiar: the
tutor works in the demo, and the institution cannot answer "what did the cohort
actually learn?" — so the pilot does not renew. The missing piece was never the
model. It was the record.

**Wiring:**

1. **Learning Record Store.** `yetanalytics/lrsql` (**Apache-2.0**, 144) by
   default — Postgres 14–18 in production, SQLite for development. Choose
   `openfun/ralph` (**MIT**, 51) instead when the engagement is analytics-shaped
   rather than storage-shaped, when the team wants one Python toolchain end to
   end, or when **EU provenance matters** (France Université Numérique).
2. **Agent interface.** `DavidLMS/learnmcp-xapi` (**MIT**, 16) as the MCP
   server. Three tools — record statement, retrieve progress, manage activity
   vocabulary — and the `practiced` / `mastered` / `experienced` / `achieved`
   verbs are built in, so the pedagogical vocabulary is not something you
   invent. Separate learners by `ACTOR_UUID`; one server serves a cohort.
   Verified against SQL LRS, Ralph and Veracity. **It is 16 stars: read it,
   pin the commit, and expect to maintain your own fork.**
3. **Tutor.** Any agent from `agents/top.md`. `HKUDS/DeepTutor` (Apache-2.0)
   where a learner model is wanted out of the box; `ArnaudGuiovanna/tutor-mcp`
   (MIT) where auditable progression state governed outside the model is the
   priority — it already holds learner state, so the two state stores must be
   reconciled deliberately rather than both left running.
4. **Mastery estimation, quantitative.** `pykt-team/pykt-toolkit` (MIT, 461)
   over the accumulated xAPI statements. This is the step that separates the
   build from a chat log: the LRS gives you the events, pyKT turns them into
   knowledge-tracing estimates the institution can defend.
5. **Platform integration across the network boundary.** LTI 1.3 via
   `Cvmcosta/ltijs` (Apache-2.0, 373) to launch inside Moodle/Canvas/Open edX,
   with grade writeback through AGS. **Never fork the LMS.** The copyleft stays
   on the far side of its own API; everything you ship stays permissive.
6. **Reporting surface.** The LRS is the source of truth for every
   institutional question — cohort mastery, time-on-task, evidence per claim.
   Build the dashboard against the LRS, not against the agent's transcript.

**Why it is defensible:** the LMS belongs to the client and is copyleft; the
model is a vendor's and is substitutable within a quarter. The **learner
record** — mastery state, progression, evidence — is the asset, and this is the
first configuration in this KB where it can be owned, shipped and
Apache-2.0-licensed inside a deliverable.

**Compliance fit by region, at no extra cost:**
- **EMEA** — the Commission's May 2026 draft guidelines place tutoring and
  practice feedback **outside** Annex III high-risk. Keep P9 on practice and
  formative feedback with no grade of record, and it stays out of scope. Pair
  with `openfun/ralph` for EU-origin data infrastructure. The moment it writes
  a grade of record, switch to `P2`.
- **North America** — answers the 85/18 governance gap directly: the LRS *is*
  the audit log, so "what did the AI do with my students" has a queryable
  answer on day one. Self-hosted satisfies FERPA posture.
- **LATAM** — self-hosted on `lrsql` with no learner data leaving the country
  is a direct answer to Mexico's "technological sovereignty" framing, and the
  governance artifact the 87%/26% gap is asking for.
- **APAC** — emits the record needed for Korea's AI Basic Act disclosure and
  India's provenance-marking rules without a separate compliance build.

**License outcome:** Apache-2.0 / MIT end to end. No copyleft in the
deliverable. This is the only pattern in this file for which that is true.

**Estimate:** **3–4 weeks** for LRS + MCP server + one tutor emitting a
governed xAPI statement stream, plus 2 weeks for the pyKT mastery layer and the
reporting surface. The cheapest credible first engagement in this KB, and the
right wedge ahead of `P8`.

## P10 — Mount a licensed skill, not a service (Global, cheapest entry in this file)

**New 2026-11-13 (fourth pass).**

**Problem:** a client wants a credible tutoring capability in weeks, not a
platform in quarters — and the usual answer, "stand up a tutor service," buys
them a deployment, an inference bill, a security review and a maintenance
burden before any teaching happens.

**The opening:** `janestreet/agent_skills` (**MIT, 7.9k stars, 510 forks, 2
commits**) is a *skill*, not software — a `SKILL.md` instruction set that turns
any SKILL.md-compatible host (Claude Code, Codex, OpenClaw) or even a plain
chatbot into a strict Socratic tutor: a 3-5 question diagnostic, a 4-10
sub-skill map rated 0-5, **one question at a time**, spaced review, final
assessment. It ships no code, so there is **no dependency tree, no CVE surface
and no container**. It is also the first artifact of its class this KB can
actually use: `education-agent-skills` (977 stars) is the same shape under **CC
BY-SA**, which is a content license with share-alike and the wrong instrument
for a deliverable. This one is MIT.

**Wiring:**
1. **Start from the skill, fork it in-repo.** Take `socratic-tutor` and adapt
   the rubric and sub-skill map to the client's curriculum. This is prompt and
   pedagogy work — subject-matter experts can own it, which is the point.
2. **Add the guardrails the skill does not enforce.** A `SKILL.md` *asks* the
   model to behave; it cannot *prevent* it from answering. Port the three
   controls from `vulinh1704/ai-tutor-agent` (MIT): the **hint ladder** with a
   configurable escalation cap, the **answer-leak guard** that regenerates a
   draft which gives away the answer, and **rubric scoring whose totals are
   computed in code rather than by the model**. Without these, "strict Socratic
   tutor" is an instruction, not a property.
3. **Host it where the learner already is.** Mount as an LTI 1.3 tool with
   `dmitry-viskov/pylti1.3` (MIT) — now a **single-language Python** path, see
   the correction at the top of this file — or reach into the LMS over
   `vishalsachdev/canvas-mcp` (MIT, 324) or `Faixiang/Moodle-MCP` (MIT, 206,
   read-only).
4. **Make it reportable.** Emit xAPI through `DavidLMS/learnmcp-xapi` (MIT) into
   `yetanalytics/lrsql` (Apache-2.0), using the skill's own 0-5 levels as the
   `practiced` / `mastered` progression. The sub-skill map is already the shape
   an LRS wants, which is why this composes cleanly with `P9`.
5. **Measure it, with the caveat stated — and the caveat is now a licence, not
   just coverage.** `kaushal0494/AITutor-EvalKit` (🔴 **no licence file; the `MIT`
   claim is refuted on bytes, re-verified `p802` at `HEAD` `a71078456a90`**, 4
   stars, mathematics only) is still the only pedagogy-specific eval harness in
   this KB. 🔴 **It cannot go into a client deliverable.** Use it as an internal
   reference, tell the client what it does not cover, and request a grant upstream.

**Why this is the cheapest pattern here:** steps 1-2 are the deliverable and
steps 3-5 are reuse. There is no model to train, no service to scale, and the
licensing question — normally the longest conversation in an education
engagement — is settled in one line: **MIT end to end**.

**Regional read:**
- **North America** — the 85%-of-educators-use-AI / 18%-have-guidance gap is a
  governance gap, and a reviewable `SKILL.md` plus a code-enforced rubric is an
  artifact a district can actually approve. Nothing leaves the host if the host
  is self-hosted.
- **EMEA** — no grade of record means no Annex III high-risk classification;
  stay on practice and formative feedback and the EU AI Act high-risk
  obligations (now dated **2 December 2027** on the Digital Omnibus reading) do
  not bind. The moment it grades, switch to `P2`.
- **LATAM** — the lowest-cost route to the governance artifact the UNESCO
  IESALC 87%/26% gap is asking for; translation and curriculum adaptation are
  the work, and both are local-team work.
- **APAC** — a skill file is reviewable text, which is the cheapest way to
  satisfy Korea's AI Basic Act disclosure duties and India's provenance-marking
  rules without a compliance build.

**License outcome:** MIT end to end, including the pedagogy artifact itself.

**Estimate:** **1-2 weeks** for an adapted, guardrailed skill mounted in one
LMS, plus 1 week to wire the xAPI stream. The cheapest credible engagement in
this KB — and the right thing to sell when the client's real question is "can
you show us something that teaches by March."

**The trap, stated plainly:** 7.9k stars on **two commits** measures attention,
not maturity. This is a well-designed prompt from a firm with a strong
engineering reputation, not a maintained product, and it will not be patched for
you. Fork it and own it from day one.

## P11 — Caliper-bound analytics layer (North America, newly priceable)

**Problem:** a North American higher-ed client's procurement document names
**Caliper Analytics**, not xAPI, as the learning-analytics standard. Through
four passes this KB answered that with "no open starting point in this base —
that is a build, and it must be priced as one." **That answer was wrong and cost
money.** Five of the six components now exist.

**When to use this instead of `P9`.** `P9` (the learner-record spine) is the
default and is permissive end to end on xAPI. **Use `P11` only when a contract
names Caliper.** Where the client is free to choose, choose xAPI — the reason is
the single asymmetry in the table below, and it is decisive.

**Step 0 — ask which Caliper *version* the contract names. Do this in week one.**
The only verified permissive sensor defaults to **v1.1**
(`http://purl.imsglobal.org/ctx/caliper/v1p1`). The only **v1.2** implementation
found anywhere is **unlicensed**. A 1.2 client is materially further from this
shelf than a 1.1 client, and no procurement document this KB has seen
distinguishes them. **If the answer is 1.2, the sensor is also a build and this
estimate doubles.**

**The stack, with what you get and what you write:**

| Layer | Repo | License | You |
|---|---|---|---|
| Sensor / client | `CarnegieLearningWeb/caliper-ts` | **MIT** | **Adopt.** TypeScript Sensor API, 225 commits. Entity factories for Assessment, AssessmentItem, Person, Session, SoftwareApplication, Membership |
| LMS emitter (Moodle) | `open-lms-open-source/moodle-logstore_caliper` | GPL-3.0 | **Install.** Expander → Translator → Emitter, immediate or batched, Moodle 2.7+ |
| Event store | 🔴 **nothing permissive exists** | — | **BUILD. This is the line item.** |
| Analysis / dashboards | `tl-its-umich-edu/caliper-event-analysis` | **Apache-2.0** | **Adopt and extend.** U-M + CSCAR notebooks |
| Profile reference | `UnizinAnalytics/caliper-net-public` | LGPL-3.0 | **Read, do not link.** Nine Metric Profiles = the scope definition for your store |
| PHP reference | `tl-its-umich-edu/caliper-php-public` | LGPL-3.0 | **Read** if the client is a PHP shop (Moodle, Chamilo) |

**Wiring, concretely.**

1. **Install the Moodle logstore plugin** and point it at your store: it needs
   an Event Store URL, an API key, a send-immediately flag and a batch size.
   Start batched; switch to immediate only if a dashboard needs sub-minute
   latency. 🟢 **GPL-3.0 here is correct and harmless — a Moodle plugin lives
   inside a GPL-3.0 host and does not reach your separately deployed agent
   layer.** Say this to any client who has internalised "do not fork the LMS":
   the rule is about forking the platform, not installing a plugin.
2. **Build the event store against the nine-profile list** from
   `caliper-net-public` — Base, Session, Reading, Annotation, Assignable,
   Assessment, Assessment Item, Outcome, Media. Accept
   `POST /ims/caliper/v1p1/events` with bearer-token auth and persist the
   envelope whole. **`open-ent/caliper` is the shape to copy** (it implements
   exactly this as an event store **and** a sensor, with 33 unit tests) — 🔴
   **read it, do not vendor it: no licence on the page.**
3. **Emit from the agent layer with `caliper-ts`**, so the agent's tutoring and
   assessment activity lands in the same store as the LMS's. 🔴 **Build caveat
   that will surprise a dev team: `caliper-ts` publishes to the GitHub Package
   Registry as `@imaginelearning/caliper-ts`, not public npm** — the build needs
   an `.npmrc` scoped to `@imaginelearning`. Budget an hour of CI plumbing and
   **vendor it**: 0 stars means no community will patch it for you.
4. **Stand up dashboards from `caliper-event-analysis`.** Apache-2.0, so the
   notebooks can seed the client deliverable directly. **This is the layer the
   client actually buys** — events nobody reads are a cost centre.
5. **Keep the agent layer MIT/Apache and separately deployed**, per this KB's
   standing rule. Nothing in the GPL-3.0 or LGPL-3.0 rows above is linked into
   it: the plugin runs inside Moodle, and the LGPL-3.0 repos are read, not
   imported.

**Regional fit.** 🟢 **North America is the reason this pattern exists** — and
the provenance helps in procurement: the nine-profile reference comes from
**Unizin**, the US higher-education consortium, and the analysis layer from the
**University of Michigan**. 🟡 **EMEA** gets one bonus: `open-ent/caliper` is a
French public-education platform's module, usable as design evidence in an EU
data-sovereignty conversation (and the highest-value licence request on this
board). 🔴 **APAC and LATAM: do not sell this pattern.** Nothing in those
regions' procurement specifies Caliper; `P9` on xAPI is strictly better there.

**License outcome:** MIT/Apache in everything you ship. GPL-3.0 confined to the
Moodle plugin inside Moodle; LGPL-3.0 read-only.

**Estimate:** **5-7 weeks** — 1 week plugin + sensor wiring, **3-4 weeks event
store** (the whole variable), 1-2 weeks dashboards. 🔵 **Compare honestly in the
proposal: `P9` on xAPI is 3-4 weeks because `yetanalytics/lrsql` (Apache-2.0,
144★, Postgres 14–18 / MariaDB / MySQL / SQLite) *is* the store.** The entire
Caliper premium is one missing component. **A client free to choose should see
that number.**

**The trap:** quoting the old "Caliper is greenfield" line. It overprices the
work by a factor and loses the deal to someone who has read the shelf.
**The second trap:** reading licences off GitHub's sidebar. `caliper-ts` shows a
bare "License" link and **is MIT** — the grant is in the `LICENSE` file
(`MIT License / Copyright (c) 2021 Imagine Learning`). A sidebar-only check
records this whole pattern as impossible.

## P12 — Agent on an Odoo-based education ERP (Global, configuration not build, cheapest SIS engagement in this KB)

**Problem:** the client wants advising, retention or early-warning on the
**student record**, and runs **OpenEduCat** or another Odoo-based education ERP.

**Why this is separate from `P8`, and why it is the first thing to check.**
`P8` is a 5-7 week build. **This is a configuration exercise, because the
connector already exists at 433 stars and the SIS is just Odoo addons.**
OpenEduCat (LGPL-3.0, **911 stars, 789 forks**, branch `19.0`) ships
`openeducat_core`, `_admission`, `_exam`, `_fees`, `_attendance`, `_timetable`,
`_parent`, `_library` — and the Odoo MCP servers address models **by name**, so
`op.student`, `op.admission`, `op.exam.attendees` and `op.fees` need no new code.
🔵 **Ask "what is your SIS built on" before "does your SIS have an API."**

**Step 1 — choose the connector by who must own the write policy.** This is the
only real decision in the pattern.

| | `erpipe-org/mcp-odoo` | `ivnvxd/mcp-server-odoo` |
|---|---|---|
| License | **MIT** | MPL-2.0 (file-level weak copyleft) |
| Stars / forks | **433** / 198 | 415 / 190 |
| Tools | 41 | 17 |
| Odoo | 16–19 (smoke-tested 16.0/17.0/18.0/19.0) | 16.0+ standard mode; JSON-2 + API key on 19+ |
| Write gate lives in | **the agent** | **the institution** |
| Mechanism | `preview_write` → `validate_write` → `execute_approved_write`; single-use, same-process, expiring token; `confirm=true`; `ODOO_MCP_ENABLE_WRITES=1`; `ODOO_MCP_ELICIT_WRITES=1` adds a native prompt; direct `create`/`write`/`unlink` **blocked**; `execute_method` allowlisted only | Companion Odoo module: per-model allowlist with separate read / write / create / delete, layered on Odoo's own access rights and record rules |
| Pick it when | the studio operates the deployment | the client's Odoo admin must hold the control — **most institutional engagements** |

🔴 **Never ship `ivnvxd`'s "YOLO mode".** It requires no companion module,
bypasses **all** MCP-level access control, exposes 200+ models, and in full form
permits delete; its own README restricts it to development and testing. **Grep
for it in any deployment you inherit.**

**Step 2 — scope the model allowlist to the education models and nothing else.**
This is the whole security posture of the engagement, and it is the reason to
prefer `ivnvxd` + companion module in an institutional setting: an Odoo instance
running OpenEduCat is usually **also** running finance and HR. An agent that can
read `op.student` must not be able to read `hr.employee` or `account.move`.
🟢 **Inherited governance is the selling point: "your agent inherits Odoo's
access rights and record rules" is a stronger story than anything a bespoke
education MCP server offers** — of the three proprietary-SIS servers in this KB,
none gates writes and one replays the student's own credentials.

**Step 3 — read-only first, always.** Ship advising and early-warning on reads
(`search_records`, `read_record`, `aggregate_records`, `get_model_fields`) and
leave writes disabled. `aggregate_records` is what makes cohort-level retention
questions answerable without exporting student rows.

**Step 4 — add writes only behind the gate, and only for one model.** Typical
first write is an advising note or a flag on the student record, never grades or
fees. On `erpipe-org`, writes stay off until `ODOO_MCP_ENABLE_WRITES=1`; on
`ivnvxd`, until the companion module grants write on that one model.

**Step 5 — emit xAPI so the institution can report on the agent.** Pair with
`P9`: `DavidLMS/learnmcp-xapi` (MIT) into `yetanalytics/lrsql` (Apache-2.0).
The SIS holds the student record; the LRS holds what the agent did. 🔴 **Keep
them separate** — this KB's most expensive available mistake is scoping an
advising engagement against the wrong one of the two.

**Regional fit.** Odoo's education footprint is heaviest in **India, LATAM and
EMEA SMB/private education**, so this is one asset serving three regions.
🟢 **LATAM and APAC private-education groups are the best first targets**:
Odoo is common in both and the connector is free. 🔴 **It does not help a LATAM
K-12 public engagement on RosarioSIS, or an international-school engagement on
Gibbon** — those are `P8`, and that distinction is worth getting right in the
first call because it is the difference between 2 weeks and 7.

**License outcome:** MIT end to end with `erpipe-org`. With `ivnvxd`, MPL-2.0 is
**file-level** weak copyleft — publish changes to its own files, combine freely
with proprietary code; it needs a licence note in the deliverable, not a
redesign. OpenEduCat itself stays LGPL-3.0 and **is not forked** — you connect
to it, which is this KB's standing rule applied to the SIS layer.

**Estimate:** **2-3 weeks** for read-only advising on an existing OpenEduCat
instance, plus 1 week for the gated first write, plus 1 week for the xAPI
stream. **The cheapest SIS engagement in this KB by a wide margin**, and the
right answer when a client with Odoo asks for the thing `P8` prices at 5-7
weeks.

🔴 **The trap, and it must be in the proposal, not just here.** This path is
**architecturally verified and has not been run** (`Gap 286`): the connectors'
tools are model-generic and OpenEduCat is Odoo addons — both read off the
repository pages — but **no Odoo instance has been stood up, OpenEduCat
installed, and a tool called against `op.student`.** Say *"the connector is
generic and the SIS is Odoo addons"*, never *"we have run it."* 🟢 **Do that run
first: it is a day of work and it converts this pattern's entire estimate from
inferred to demonstrated.** **Second trap:** `erpipe-org/mcp-odoo` was formerly
`tuanle96/mcp-odoo`, which is still what search results return — and its
maintainer sells a hosted product (ERPipe) built on it. The MIT grant is real;
the roadmap has a commercial owner. Pin a commit.

## P13 — Sovereign LMS-native AI on OpenOLAT (EMEA, configuration not build — and the only pattern here with no agent in it)

**When to use.** Greenfield or German-speaking-EMEA platform choice, where the
client has a **stated data-sovereignty or EU AI Act requirement** and the usual
answer ("mount a permissive agent into a copyleft LMS over LTI") either cannot
clear data protection or cannot be licensed the way the client needs the derived
product licensed. **This is the cheapest pattern in this file when it fits, and
it fits rarely — check the three disqualifiers below before pricing it.**

**Why it exists.** Every other pattern here assumes the platform is copyleft and
AI-less. [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is
**Apache-2.0** (451 stars, 165 forks, 32,338 commits, Java; University of Zurich
origin, maintained by frentix GmbH, Switzerland) **and carries a first-party
pluggable AI layer in-tree**. So the derived product can be licensed however the
client wants, and the AI work is configuration plus a provider, not a build.

### The components — all verified in-repo this pass

| Piece | Where | License |
|---|---|---|
| The platform | `github.com/OpenOLAT/OpenOLAT` | **Apache-2.0** (read from `LICENSE`, not the sidebar) |
| Provider SPI | `org/olat/core/commons/services/ai/` — `AiSPI`, `AiEmbeddingSPI`, `AiApiKeySPI` | Apache-2.0 |
| The provider slot you use | `spi/generic` — **any OpenAI-compatible endpoint** | Apache-2.0 |
| In-process embeddings | `spi/localonnx` — `LocalOnnxSPI`, `QwenOnnxEmbeddingModel` | Apache-2.0 |
| Self-hosted inference | `vllm-project/vllm` (Apache-2.0) or `ollama/ollama` (MIT) — from `repos/foundations.md` | Apache-2.0 / MIT |
| Telemetry out | `yetanalytics/lrsql` (Apache-2.0) or `openfun/ralph` (MIT) over **xAPI** | Apache-2.0 / MIT |

### How it wires together

1. **Deploy OpenOLAT** as the LMS. No fork, no plugin, no LTI tool — but also
   **no copyleft reaching the derived product**, which is the whole reason to be
   here rather than on Moodle.
2. **Stand up a self-hosted OpenAI-compatible endpoint** — vLLM for throughput,
   Ollama for a small install — **inside the institution's own network
   boundary.**
3. **Configure the `generic` provider** to point at that endpoint. Per-function
   provider and model selection means `essay-grading` and
   `mc-question-generator` can run on different models, and a function can be
   left switched off entirely.
4. **Leave `localonnx` serving embeddings in-process** — these never leave the
   JVM, so the retrieval and `taxonomy-matching` side needs no network boundary
   argument at all.
5. **Turn on the features you can defend, one at a time**, from the five in
   `AiFeature`: `mc-question-generator`, `image-description-generator`,
   `essay-generation`, `essay-grading`, `taxonomy-matching`.
   `image-description-generator` is the easiest first win — it is an
   **accessibility** feature, which changes the conversation from "AI in the
   classroom" to "WCAG compliance", and it is user-controlled.
6. **Emit xAPI to an LRS** (`lrsql` or `ralph`) so the institution can report on
   learning activity independently of the LMS — the spine from `P9`, unchanged
   and fully compatible with this pattern.

### Why it survives an EU AI Act review

Mapped against the deployer obligations in `intel/market.md` → EMEA:

- **Article 50 transparency (applies 2 August 2026, *not* postponed by the
  Digital Omnibus):** learners must be told they are dealing with an AI system.
  `AiFeature` carries a **learner-facing name and a one-sentence description per
  feature** (`getI18nUserNameKey`, `getI18nDescriptionKey`) as part of the data
  model — the disclosure surface is built in, not bolted on.
- **Human oversight and per-learner control:** `AiFeature.isUserControlled()` —
  *"a person can switch this feature on or off in the user settings, on top of
  the system default of the administrator"*. **Opt-out is a platform primitive.**
- **Logging:** `AiUsageLog` / `AiUsageLogStatus` / `AiUsageLogSearchParams`
  record every AI call with token/cost attribution — this is simultaneously the
  audit artifact and the FinOps artifact.
- **Article 27 FRIA** (public bodies deploying high-risk systems) and the
  **2 December 2027** high-risk deadline for stand-alone education systems:
  running inference inside the institution's boundary removes the third-country
  transfer question from the assessment entirely.
- **Emotion recognition in education has been prohibited since 2 February 2025.**
  Nothing in `AiFeature` goes near it — confirm no custom provider adds it.

### Estimate

**3–5 weeks**, and it is mostly not AI work: deployment and SSO (1–2 weeks),
self-hosted endpoint plus `generic` provider configuration and model selection
(1 week), feature-by-feature enablement with the data-protection sign-off that
each one needs (1–2 weeks). **Compare with 8–12 weeks for the equivalent
mount-an-agent-into-Moodle shape, which then still owes the client a
data-protection story for the inference hop.**

### Three disqualifiers — check these first

1. 🔴 **An existing Moodle / Canvas / Open edX estate.** This pattern is a
   platform choice, not a migration plan. With an incumbent LMS, use `P3`, `P6`
   or `P9`. The installed base is overwhelmingly on the copyleft three.
2. 🔴 **"It all runs locally" is not true and must not be proposed.** The only
   local model class is `QwenOnnxEmbeddingModel` — **embeddings**. Essay grading
   and question generation call a provider. The defensible claim is *"inference
   runs on infrastructure you control"*, which the `generic` provider delivers
   and which is what a data-protection reviewer actually asks for.
3. 🔵 **An external agent may not be able to reach these features.** The AI
   services are Java interfaces; **nothing read this pass shows HTTP exposure**,
   and no MCP server for OpenOLAT exists. If the engagement needs an *external*
   agent orchestrating across systems, this pattern does not yet reach it —
   resolve that open question (`agents/trending.md`, sixth pass) before
   committing. **As scoped above, P13 is LMS-native AI, not agentic AI.**

### The contribution opportunity, stated because it is unusually well shaped

**There is no MCP server for OpenOLAT**, while Moodle has three and Canvas two.
The platform is **Apache-2.0**, so a `openolat-mcp` is a contribution rather
than a procurement, and it is the missing piece that would make this pattern
composable with every agent pattern in this file. 🔴 **Not opened unprompted —
it is an outward action**, and this KB's standing rule (see `Gap 240`) is that
outward actions are proposed, not taken.

## P14 — The AI deployment registry (Global, compliant in four regimes at once, and the cheapest first engagement in this file)

**New `p802` (seventh pass, 2026-11-13).** Built from `T16`. 🔵 **This is the only pattern in this
file whose output is an inventory rather than a capability** — and it is the input every other
pattern here silently assumes.

🔴 **State the unusual thing first: there is no repository to adopt for the registry itself.** A
search of this pass found no open-source education AI deployment registry. The registry is ~300 lines
of schema and CRUD; **the value is in what it is wired to**, and every one of those components is
already byte-verified in this KB.

### The components — all verified in this base

| Component | Repo | Grant | Role in this pattern |
|---|---|---|---|
| Learner-record spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | The **only** agent↔learner-record write path in this KB. xAPI 1.0.3 statements make agent activity *reportable*; `ACTOR_UUID` separation is what makes **per-learner opt-out** mechanically enforceable rather than a policy sentence |
| LRS target | SQL LRS / Ralph / Veracity | — | Verified targets of `learnmcp-xapi`. The registry stores *which* LRS a deployment writes to; the LRS stores the activity |
| Review gate | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | MIT | Its shape, not its code: **nothing publishes automatically**, a human decision gates export. This is Oklahoma's "teacher review of AI output" implemented rather than asserted |
| Write-boundary reference | [`zavora-ai/mcp-education`](https://github.com/zavora-ai/mcp-education) | Apache-2.0 | `9` read-only + `3` approval-gated write tools. The **server declares** the read/write boundary — copy this contract for any registry-registered tool that touches a gradebook |
| Governed platform connector | [`ivnvxd/mcp-server-odoo`](https://github.com/ivnvxd/mcp-server-odoo) | MPL-2.0 | Where the institution must own the policy: per-model allowlist in a **companion Odoo module**, so the client's administrator — not an env var — decides agent reach. 🔴 Ban "YOLO mode" in the registry's own policy text |
| Permissive LMS host | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 (`10,982 B`, affero×`0`, payload-verified) | The EMEA sovereignty-compatible host. See `P13` |

### How it wires together

1. **Enumerate.** One row per *deployment*, not per product: tool, version, vendor, which cohort,
   which subject, who approved it, what it writes to, and **whether its output is the sole basis for
   any decision**. That last field is not optional ceremony — it is the exact predicate that decides
   Vietnam's high-risk tier and the EU's profiling question.
2. **Tier.** Apply the Philippines' DepEd Order `003` risk tiers. **Grading and admissions are the
   high-stakes tier everywhere**; a reading-practice tutor is not.
3. **Bind each row to telemetry.** A registered deployment must name its LRS endpoint. Agent
   activity lands as xAPI statements through `learnmcp-xapi` under an `ACTOR_UUID`.
4. **Enforce opt-out at the identifier, not in prose.** Parent opt-out (Oklahoma) = suppress that
   learner's `ACTOR_UUID`. The registry holds the flag; the spine honours it.
5. **Gate the high-stakes tier behind review.** Anything in the grading/admissions tier adopts
   `AI-Teaching-Agent`'s no-automatic-publication shape and `mcp-education`'s declared write boundary.
6. **Emit the compliance artifact.** The same table renders an EU **Article 27 FRIA** input, a UK
   **DfE Generative AI Product Safety Standards** conformance list, a Philippine registry return, and
   a district policy appendix for **Ohio / Maryland / Idaho / Oklahoma / Virginia / Tennessee**.

### Why it survives review in four regimes at once

🟢 **It does not depend on the contested EU date.** Whether education high-risk obligations bite in
**August 2026** or **2 December 2027** under **Regulation (EU) 2026/1744**, the registry is identical
work and is compliant under both — this base's standing advice to plan to the earlier date, with no
rework if the later one holds. 🟢 **Article 50 transparency applies from 2026-08-02 regardless**, and
the registry is where the disclosure obligation per deployment is tracked.

### Estimate

**`3`–`5` weeks** for the registry and one bound telemetry path, against an institution that already
has an LMS. **`8`–`10` weeks** with the review gate and a governed platform connector in the
high-stakes tier. 🔵 **Deliberately small** — this is the engagement that *qualifies* the larger ones
by producing the inventory they need.

### Three disqualifiers — check these first

1. 🔴 **No LMS or SIS the client actually controls.** Without one, there is no deployment population
   to register, and `learnmcp-xapi` has nothing to bind to.
2. 🔴 **The client wants detection of student AI use.** `T953` settled this: UI-driving agents are
   near-undetectable server-side and Instructure marked the request **`Will not consider`**. That is
   an assessment-**design** engagement, not a registry.
3. 🔴 **The client expects the registry to be bought.** No open-source implementation exists (`T16`).
   If procurement requires an off-the-shelf product, this pattern does not apply this quarter.

---

## P15 — The tutor-efficacy gate (Global, build-not-adopt, and the answer to the question every regulator is about to ask)

**The question.** A client deploys a tutoring agent. A ministry, an accreditor
or a procurement officer asks: *does it teach, and how do you know?* 🔴 **As of
`p803` there is no open-source instrument a studio can ship to answer this** —
`T17` establishes that the four credible education benchmarks are ungranted,
contradictorily granted, or `0★`. This pattern builds the gate instead, from
components whose grants this base has read **at the byte level**.

### The components — every grant payload-verified

| Component | Repo | Grant (how established) | Role |
|---|---|---|---|
| Harness shape | [`Kobby-Adjei/ai-tutor-benchmark`](https://github.com/Kobby-Adjei/ai-tutor-benchmark) | 🟢 **MIT** — `LICENSE`, `1,351 B`, `affero×0`, title `MIT License`, `HEAD` `23fc97462c8f` | **Template, not dependency** (`0★`). Three-stage structure + simulated-learner cards + the split code/data grant to copy |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **Verified on this base's shelf** | Bayesian Knowledge Tracing — the ground truth the gate scores *against*. Mastery movement, not answer accuracy |
| Learning-record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0**, `144★` | Holds the xAPI statements the gate reads. **Already the spine in `P9`** |
| Agent → record edge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT**, `16★` | Lets the tutor under test write its own activity, so the gate needs no bespoke instrumentation |
| Methodology (read, do not vendor) | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) · [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) | 🔴 **Ungranted / contradictory — cite, never copy** | Task decomposition and rubric structure. **Papers are citable; the repos are not shippable** |

### How it wires together

1. **The tutor under test writes to the LRS, not to a log.** Mount
   `learnmcp-xapi` against `lrsql`. Every hint, every attempt, every scaffold
   becomes an xAPI statement with a learner and a timestamp. 🔵 **This is the
   step that makes the gate reusable across clients** — it measures the record,
   not the product.
2. **OATutor's BKT supplies the outcome variable.** A tutor "teaches" when
   posterior mastery rises on *subsequent unaided* items. Scoring the tutored
   turn itself measures compliance, not learning.
3. **Three stages, after `ai-tutor-benchmark`'s shape.** (a) Static rubric pass
   over held-out dialogues; (b) simulated learners with declared personas —
   including the struggling and the disengaged, which is `TutorCaseBench`'s
   contribution; (c) live A/B against an unaided control arm.
4. **Split the grant at the repository level, on day one.** MIT on the harness,
   CC BY 4.0 on the learner cards and the dialogue data. 🔴 **This is the single
   thing four institutional benchmarks got wrong**; it costs one `LICENSE` file
   and one README section to get right.
5. **Emit the result into the deployment registry from `P14`.** The registry row
   for the tutor gains an efficacy field with a date and a method. That is the
   artifact the regulator actually wants.

### Why it survives review

- **EU AI Act, Annex III.** Assessment and admissions AI is high-risk, and
  Article 27's Fundamental Rights Impact Assessment presupposes evidence about
  the deployed system. A dated efficacy measurement **is** that evidence.
- **Vietnam.** Automated assessment is named high-risk and status turns on
  whether output is *the sole basis for a decision* — a per-deployment property
  the gate records per deployment.
- **Oklahoma, DC, Texas `HB2400`.** Each restricts what AI may decide unaided.
  🟢 A control arm is the only way to show a human-in-the-loop design did not
  degrade learning — which is the argument that wins the exemption.

### Estimate

**6–8 weeks** for the first client, **2–3 weeks** for each one after. Stage (a)
is a week. Stage (b) is most of the cost — persona design is the skilled part
and is **the reusable asset across the whole studio**. Stage (c) needs a cohort
and a term, so it is sold as a follow-on, not bundled.

### Three disqualifiers — check these first

1. 🔴 **No unaided post-test is possible.** If the client will not hold out items
   or a control arm, stages (a) and (b) are all you can deliver — sell those, and
   say plainly that they measure dialogue quality, not learning.
2. 🔴 **The tutor is a closed third-party product with no record egress.** Without
   xAPI out, step 1 fails and the gate becomes bespoke per vendor.
3. 🔴 **The client wants a benchmark *number* for marketing.** This produces a
   dated, scoped, method-bound finding. It is evidence for a regulator, not a
   league-table score, and promising the latter will end badly.

🔵 **Why this is `build`, not `adopt` — stated plainly.** It is the only pattern
in this file besides `P14` with no adoptable upstream, and for the same reason:
the artifact that is needed is the one the field publishes as a paper and
forgets to license.

## P16 — The 64-campus policy pack (North America, deadline-driven, and the only pattern here with a date already set)

**Why this pattern exists.** `T18`: SUNY's systemwide AI policy requires each of
**64 campuses** to publish or update an AI policy **no later than 2026-12-31** —
**48 days from the pass that found it** — supported by a total of **31** AI for
the Public Good Fellows. 🔵 **Every other pattern in this file sells against a
trend. This one sells against a calendar**, and the same shape recurs wherever a
system or ministry sets a campus-level deadline (Ohio's July 2026 district
mandate is the K-12 analogue already recorded in `intel/market.md`).

🔴 **Provenance: the SUNY facts are search-tier** (`suny.edu` unreachable from the
pass that recorded them; `ACTION p804-V`). **Confirm the date and scope with the
client before pricing against it** — the pattern holds regardless, the deadline is
what must be checked.

**The insight that makes it a product rather than 64 consulting engagements.** A
campus can write policy prose from a template in an afternoon. 🔴 **What no campus
can produce from a template is an accurate statement of what it actually runs** —
and a published AI policy that cannot name the systems it governs fails on first
audit. 🟢 **So the deliverable is one policy template plus one inventory instrument,
and the inventory is the part that is worth money and the part that is reusable.**

### What to build

| Layer | Use | Grant |
|---|---|---|
| Deployment registry | **`P14`'s registry, unchanged** — the schema already satisfies four regimes at once; here it also becomes the evidence annex to the published policy | Per `P14` |
| LMS discovery (Canvas) | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — read the courses, external tools and LTI placements actually installed, rather than asking the registrar | MIT |
| LMS discovery (Moodle) | [`Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) — **read-only by construction**, which is the right property for a discovery pass across campuses that have not yet agreed a policy | MIT |
| Mount point for the literacy module | [`ltijs`](https://github.com/Cvmcosta/ltijs) (Node) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) — LTI 1.3, so the module mounts into Canvas, Moodle, Blackboard and D2L without per-LMS work | Apache-2.0 / MIT |
| Literacy content | Re-levelled from [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) — take the **`22`/`48`/`23` difficulty grading as the prerequisite sequence**, discard the developer framing (`T19`) | MIT |
| Assessment items | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) to author and score; pair with `qti3-item-player` for certified delivery — 🔴 **still a pairing exercise, per `repos/foundations.md`** | Per that file |
| Completion reporting | [`learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) against SQL LRS, Ralph or Veracity — so "the campus delivered AI literacy" becomes an institutional record, not an assertion | MIT |

### Sequence

1. **Week 1 — one campus, end to end.** Run the registry (`P14`) plus `canvas-mcp` /
   `Moodle-MCP` discovery against a single willing campus. Output: a populated
   inventory and a policy draft whose every claim cites a registry row.
2. **Weeks 2–3 — make it a kit.** Freeze the registry schema, the policy template
   and the discovery scripts. 🟢 **Hand it to the Fellows, not to the campuses** —
   31 people are the distribution channel, and training them is a smaller, better
   engagement than selling 64 times.
3. **Weeks 4–6 — the literacy module.** Re-level the corpus, emit items as QTI,
   mount over LTI 1.3, wire xAPI. 🔵 **This half is not deadline-bound and should be
   priced separately** — the policy must ship by December 31; the curriculum serves
   Fall-entry cohorts and can land after.
4. **Ongoing — the registry is the renewable.** It is what `T16` says every regime
   will ask for next, and it is already built.

### Scope and risk

- **Effort:** 2–3 weeks to the first campus artifact and the kit; 4–6 further weeks
  for the literacy module. 🔴 **Do not propose a 64-campus rollout inside the
  deadline** — propose the kit plus the Fellows' enablement, which is deliverable.
- 🔴 **Pitch AI *inside* the existing Information Literacy competency, not a
  standalone AI course.** The standalone reading is the contested one (`T18`) and
  the expensive one.
- 🔴 **Do not let the discovery pass acquire write access.** `Moodle-MCP` is
  read-only by design; keep `canvas-mcp` to read scopes. A governance engagement that
  writes to a gradebook before the policy exists is the one failure that ends it.
- 🟢 **Everything in the table is MIT or Apache-2.0** — the kit is deliverable to the
  client as a derived product with no copyleft propagation.

## P17 — The defensible tutor audit trail (Global, and the only pattern here that survives an EU AI Act Article 50 question)

**When to use.** Any engagement where an AI tutor or grader touches learners and
**someone will eventually ask what it did**. That is now most of them: EU
Article 50 transparency duties apply from **2026-08-02** and were *not*
postponed by the Digital Omnibus; FERPA binds any US tool handling personally
identifiable student data; South Korea's AI Basic Act names education a
high-impact sector. 🔵 **Every other pattern in this file tells the agent to
"emit xAPI". This one is the pattern that receives, validates, stores and
consolidates it — and until `p805` this base named no component that could
reject a malformed emission.**

### The components — all permissive, all re-verified live at `p805`

| Piece | Where | License |
|---|---|---|
| Statement validation, in the agent process | `github.com/LearningLocker/xapi-validation` | **MIT** (12★) |
| Statement service / LRS endpoint | `github.com/LearningLocker/xapi-service` | **MIT** (42★) |
| Or the database-shaped LRS | `github.com/yetanalytics/lrsql` | **Apache-2.0** (144★) |
| Record warehouse, multi-source | `github.com/Apereo-Learning-Analytics-Initiative/OpenLRW` | **ECL-2.0** (62★) |
| Agent↔record bridge | `github.com/DavidLMS/learnmcp-xapi` | **MIT** |
| The LMS it hangs off | Moodle (GPL-3.0) over LTI 1.3, or OpenOLAT (Apache-2.0) natively | — |

### How it wires together

1. **Validate before you emit.** The agent builds an xAPI statement and runs it
   through `xapi-validation` **in its own process**. A malformed statement is
   rejected at the source, where there is still a stack trace, rather than
   silently accepted by a lenient store.
2. **Emit to `xapi-service`** (Node stacks) **or `lrsql`** (when the client
   wants a database product with a verified Postgres/MariaDB/MySQL matrix).
   Both are permissive, so the store ships inside the deliverable.
3. **`learnmcp-xapi` gives the agent read access back** — the tutor reads the
   learner's own record before deciding what to do next, which is what makes
   the trail *useful* rather than merely compliant.
4. **Consolidate into `OpenLRW`** when more than one system emits — LMS, tutor,
   assessment tool. ECL-2.0 is Apache-derived and OSI-approved, so it composes
   with everything above it.
5. **Point the Article 50 answer at the warehouse**, not at the model: what the
   regulator wants is *which learner, which interaction, disclosed as AI, when*
   — which is a query, once the trail exists.

**Licence consequence.** MIT + MIT + Apache-2.0 + ECL-2.0 — **no copyleft
anywhere in the trail.** The GPL stays in the LMS, on the far side of LTI.

**Estimate.** **4–6 weeks** to a working trail against one LMS and one tutor;
**+3–4 weeks** for the OpenLRW consolidation and a regulator-facing query layer.

🔴 **Caveats.** `xapi-service` and `xapi-validation` show no release dates on
their pages — **pin commits and budget to carry them**. `OpenLRW` is Apereo
middleware: Java, institutional, and not a quick install. And an audit trail is
a *record*, not a defence — if the tutor's behaviour is wrong, the trail proves
it precisely.

## P18 — Skills-and-credentials advising (North America, and the only pattern here whose buyer is a workforce agency)

**When to use.** State systems, community colleges, workforce boards and
corporate academies — buyers who are not asking "did the learner engage" but
**"what is this person able to do, and what does that credential actually
certify"**. 🔵 **This is the one engagement shape in this KB whose data model
is a public vocabulary rather than a vendor schema**, which is why it is cheap
to be interoperable and expensive to be proprietary.

### The components — all permissive, promoted to the shelf at `p805`

| Piece | Where | License |
|---|---|---|
| Skill authoring against CTDL/RSD | `github.com/CredentialEngine/osmt` | **Apache-2.0** (67★) |
| The registry skills publish into | `github.com/CredentialEngine/CredentialRegistry` | **Apache-2.0** (15★) |
| Transcript line → CTID matching | `github.com/CredentialEngine/transcript-ctid-matcher` | **Apache-2.0** |
| Lived-experience skills elicitation | `github.com/tabiya-tech/compass` | **MIT** (14★) |
| Taxonomy side | `tabiya-tech/taxonomy-model-application`, `tabiya-livelihoods-classifier` | **MIT** |
| Learner record in / out | `lrsql` or `xapi-service` (see `P17`) | Apache-2.0 / MIT |

### How it wires together

1. **`transcript-ctid-matcher` maps the registrar's course rows to CTIDs.**
   This is the unglamorous core of the engagement and the reason a studio gets
   paid — a permissive reference implementation removes the worst of it.
2. **`osmt` authors Rich Skill Descriptors** for what the institution teaches;
   **`CredentialRegistry` publishes them** so employers and other institutions
   can resolve them.
3. **`compass` runs the learner-facing half**, eliciting skills from lived
   experience rather than coursework — the only agent in this base that does.
   Its output is a skills profile, not a transcript.
4. **Join the two.** The advising agent answers *"given what you have done, here
   is the credential nearest to the job you want, and here is the gap"* — with
   both sides expressed in the same public vocabulary.
5. **Emit the advising session over xAPI** into `P17`'s trail.

**Licence consequence.** Apache-2.0 + MIT throughout — **fully derivable**.

**Estimate.** **8–10 weeks** for transcript→CTID matching plus a published skill
set against one institution; **+4 weeks** to add the `compass` elicitation front
end.

🔴 **Caveats, and they are real.** **CTDL/RSD is a US ecosystem** — this pattern
does **not** transfer to EMEA, APAC or LATAM without replacing the vocabulary,
and there is no equivalent permissive stack in this base for those regions
(**declared gap, `p805`**). `osmt`'s grant had to be read from the file because
the index says `NOASSERTION`. All four repos are under 70 stars: adopt the
vocabulary and the licence with confidence, read the code before promising the
pipeline.


## P19 — Agent on the state data standard (North America, the highest-ceiling pattern in this file)

🔵 **Why this pattern exists and why it is new at `p806`:** every other student-record
pattern here — `P8`, `P9`, `P12` — reaches the record through **one institution's**
system. This one reaches it through **Ed-Fi**, the interoperability model US **state
education agencies** run K-12 reporting on. 🟢 **Same engineering, one altitude up, and
the buyer changes from a district to a state.**

### The components — all Apache-2.0 or MIT, all verified at `p806`

| Component | Repo | Licence | Role |
|---|---|---|---|
| Data platform | [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** | **Ed-Fi API v8.** Data Management Service (Resources, Descriptors, Discovery) + Configuration Service (Management API). 🔴 **Build here, not against the v7 ODS** — the ODS README says v8.0+ lives in this repo |
| Legacy target | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** | v7.x ODS/API — what the client is probably **actually running today**. Plan for it; do not design new work onto it |
| Write-gate design | [`PsychQuant/che-ntucool-mcp`](https://github.com/PsychQuant/che-ntucool-mcp) | **MIT** | 🟢 **Copy the protocol, not the code** (it is Swift / macOS): elicitation dialog **plus a single-use token bound to the previewed payload** |
| Write-gate alternative | [`12dora/waseda-moodle-mcp`](https://github.com/12dora/waseda-moodle-mcp) | **MIT** | `prepare_*` → `confirm_action` / `cancel_action`. Simpler; the right choice where there is no grade-write path |
| Telemetry | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Emit xAPI for anything the agent does, so the activity is reportable |
| Governance | `P14` deployment registry | — | 🟢 **Mandatory here, not optional** — see below |

### How it wires together

1. **Stand up the Ed-Fi API** (v8 DMS) against a copy of the client's data, or point at
   their existing v7 ODS/API. Both speak a published REST specification.
2. **Write an MCP server over it.** 🔴 **This does not exist and is the build** — see
   `Gap 806-A`. Scope it by Ed-Fi **resource**: enrollment, attendance, assessment
   results, discipline. Start **read-only**.
3. **Gate every write before you ship one.** Adopt `che-ntucool-mcp`'s two-layer design:
   a `preview_*` call returns the exact payload and a single-use token; the `post_*` call
   refuses anything whose token does not match the previewed payload byte-for-byte.
4. **Emit xAPI** through `learnmcp-xapi` for every agent action.
5. **Register the deployment** (`P14`) before go-live.

### Why the write gate is not negotiable here

🔴 **A state longitudinal data system is the highest-consequence write surface in this
entire knowledge base.** An attendance or discipline record that an agent changed
silently is a legal problem for the agency, not a bug report. 🟢 **Ship read-only first
and sell the write path as phase two** — it is also an easier procurement conversation.

### Estimate

🟢 **Read-only MCP server over Ed-Fi v8, four resource families, xAPI emission,
deployment registry: 6–8 weeks.** Add **3–4 weeks** for the gated write path. 🔵 **The
discovery cost is the variable** — which Ed-Fi version the agency runs, and which
optional Ed-Fi extensions their state profile adds, decides more of the timeline than
the agent work does. **Scope a 1-week assessment first.**

### Three disqualifiers — check these first

- 🔴 **The client is a district, not a state or a regional service agency.** Then this is
  over-engineered: use `P8` or `P12` and sell a SIS-level integration.
- 🔴 **The agency is not on Ed-Fi.** Not every state is. Confirm before proposing —
  **this is a one-question disqualifier and it is free to ask.**
- 🔴 **The engagement needs writes in phase one.** Then the timeline and the compliance
  surface both roughly double; re-scope or re-price.

## P20 — AI-literacy programme from an open corpus (Global, and the only pattern here with three dated mandates pointing at it)

🔵 **Why this pattern exists:** `T19` records three regimes imposing a dated AI-literacy
duty — SUNY's gen-ed Information Literacy competency from Fall 2026, **EU AI Act Art.
`4`**, and Australia's national rollout at **1M students over three years** — against a
supply side that was empty. 🟡 **`p806` narrowed that: the first open-licensed education
curriculum exists, and it is a seed a studio can grow rather than a product that
competes with one.**

### The components

| Component | Repo / standard | Licence | Role |
|---|---|---|---|
| Curriculum seed | [`Emerging-Rule/community`](https://github.com/Emerging-Rule/community) | 🟡 **CC BY 4.0 (README + badge; no sidebar licence field)** | Bilingual **EN / ES** K-12 lessons, K-2 → 9-12. 🟢 **Attribution-only, no share-alike — shippable inside a client deliverable** |
| Difficulty sequence | [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | **MIT** | 🟢 **Take the `22`/`48`/`23` three-tier grading as the prerequisite spine**, then cut the developer assumptions. Content for the upper secondary / tertiary end |
| Framework alignment | [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **MIT** | 🟢 **The piece that makes this saleable to a ministry.** Publishes the AI-literacy competency framework as machine-readable **1EdTech CASE® 1.1**, so every lesson is aligned to a stated competency rather than asserted to be |
| Credential | [`CredentialEngine/osmt`](https://github.com/CredentialEngine/osmt) | **Apache-2.0** | Rich Skill Descriptors against CTDL — for the North American workforce-outcome claim |
| Delivery | `pylti1.3` / `ltijs` + Moodle / Canvas / Open edX | MIT / copyleft host | Mount the sequence as an LTI tool so it runs inside whatever LMS the client already has |
| Assessment | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** | QTI 3 items, so the item bank is portable off the project |
| Reporting | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Completion and mastery as xAPI — 🟢 **this is what turns "we ran training" into evidence of discharging the duty** |

### How it wires together

1. **Model the duty as a competency framework in `opensalt`** — Art. `4`, the SUNY
   competency or the Australian curriculum, whichever binds the client. 🔵 **Do this
   first:** it is what the auditor reads and it decides everything downstream.
2. **Map the seed lessons onto it.** `Emerging-Rule/community` for K-12,
   `ai-engineering-hub`'s tiers for upper secondary and tertiary.
3. 🔴 **Write the lessons that do not exist.** At six to thirteen lessons the seed covers
   a fraction of any mandate. **This is the actual work and the actual line item.**
4. **Author assessment as QTI 3 items**, delivered through the item player.
5. **Mount via LTI 1.3**; emit **xAPI** on completion and mastery.
6. **Contribute the new lessons back upstream.** 🟢 **Not altruism:** CC BY 4.0 lets the
   studio keep and ship them, and a studio that authors the reference corpus in a field
   with three mandates and no incumbent owns the category.

### Why the licence chain holds

🟢 **CC BY 4.0 (content) + MIT (sequence, player, telemetry) + Apache-2.0 (skills) is
attribution-only end to end.** Nothing here is share-alike, so the client's derived
curriculum stays theirs. 🔴 **The one weak link is provenance, not terms:**
`Emerging-Rule/community` shows **no licence field on its GitHub sidebar** — CC BY 4.0
is from the README and a badge. 🔵 **Confirm the grant in writing with the maintainer
before building a priced deliverable on it.** `20` commits and `3` stars means there is
a person who will answer an email.

### Estimate

🟢 **Framework modelling in `opensalt`, mapping the existing seed, LTI mount, QTI
assessment and xAPI reporting: 5–7 weeks.** 🔴 **Curriculum authoring is separate and
dominates the budget** — price per unit, not per project, and scope it against the
specific mandate.

### Three disqualifiers — check these first

- 🔴 **The client needs Portuguese.** The seed is English and Spanish only. **For Brazil,
  the largest education market in LATAM, the corpus does not exist** — that is an
  authoring project from zero, and it must be priced as one.
- 🔴 **The client wants accredited or certified courseware.** None of these components
  carries accreditation; it is a separate, slow, jurisdiction-specific process.
- 🔴 **The mandate is already met by a national programme.** Australia's rollout has
  materials and a funder (Code for Schools, AWS support). 🔵 **Check what the ministry
  already bought before proposing to build it.**


## P21 — Admissions and enrolment agent on a permissive CRM (Global, and the only pattern here that touches no copyleft at all)

🟢 **New at the twelfth pass (`p807`, 2026-11-13).** Every other pattern in this file
either integrates with a copyleft platform or accepts one in the tree. 🔵 **This is the
first end-to-end recipe a studio can fork, rebrand and ship as a product**, and it exists
because `p807` finally read the vertical leg's eight-pass nil instead of logging it: the
education-specific ERP/CRMs are all copyleft, so the permissive base has to be a
general-purpose CRM with the education domain built on top.

**The problem it solves.** Admissions and enrolment is **CRM-shaped work** — enquiry →
application → offer → acceptance → enrolment, with campaigns, attribution, document
chase and nurture. 🔴 **This base had been implicitly routing it to the SIS shelf, which
is entirely copyleft and structurally wrong anyway**: an SIS records students who are
already students. The pipeline before that is a sales funnel with a prospectus.

### Components — all permissive, all verified `2026-11-13`

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| CRM base | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | **MIT** (`24.1k★`, `1.7k` forks) | The largest permissively licensed CRM found. Lead → opportunity → stage maps onto enquiry → application → offer with no structural violence |
| Alternative base | [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | **Apache-2.0** (`2.2k★`) | Swap in **only** where the admissions process is unusual (multi-intake, competitive, ministry-reported) — it is a modeller, not a CRM to bend |
| Agent runtime | [`pydantic-ai`](https://github.com/pydantic/pydantic-ai) or [`LangGraph`](https://github.com/langchain-ai/langgraph) | **MIT** | Typed tool-calling; `LangGraph` where the offer path needs an explicit approval node |
| Model serving | [`vllm`](https://github.com/vllm-project/vllm) or [`ollama`](https://github.com/ollama/ollama) | **Apache-2.0** / **MIT** | Self-host where applicant PII cannot leave the institution — the usual EMEA and public-sector constraint |
| Gateway | [`litellm`](https://github.com/BerriAI/litellm) | **MIT** | One endpoint, per-programme cost attribution |
| Durable workflow | [`temporal`](https://github.com/temporalio/temporal) | **MIT** | Admissions runs for **months**; document chase and deferrals are long-lived timers, not request/response |
| Handoff to SIS | `OpenEduCat` via `erpipe-org/mcp-odoo`, or `Ed-Fi` (`P19`) | *integration only* | 🔴 **Copyleft stays on the far side of an API boundary — nothing is derived** |

### How it wires together

1. **Model the education domain in Krayin first, before any AI.** Add `Programme`,
   `Intake`, `Application`, `Qualification` and `Document` as custom entities; map
   Krayin's native `Lead` → `Applicant` and its pipeline stages → the admissions funnel.
   🔵 **This is configuration plus migrations, and it is the bulk of the schedule.**
2. **Wrap an admissions subset of Krayin's REST API as an MCP server.** 🔴 **No MCP
   server exists for Krayin, Corteza or OFBiz — this is net-new**, but all three are
   conventional API-first web apps, so it is days, not a connector project. 🟢 **Expose
   reads broadly and writes narrowly:** `search_applicants`, `get_application`,
   `list_outstanding_documents` read-side; `request_document`, `advance_stage`,
   `log_interaction` write-side.
3. **Apply `T20`'s preview-then-confirm discipline to every write.** Three independent
   LMS agent projects in three jurisdictions converged on it. 🔴 **An agent that advances
   an applicant's stage or issues an offer without an explicit human confirm is the
   failure mode that ends the engagement** — offers are contractual.
4. **Put Temporal behind anything with a clock.** Document chase, conditional-offer
   deadlines, deferral windows, clearing. 🔵 **The agent decides; Temporal remembers** —
   an LLM loop cannot be trusted to still be running in six weeks.
5. **Hand off at enrolment, do not absorb.** When an applicant converts, write to the SIS
   over its API — `OpenEduCat` through the Odoo MCP connectors, or a state system through
   `P19`'s Ed-Fi path in North America. 🟢 **The copyleft SIS is never in your tree.**

### Build estimate

🟢 **`8`–`10` weeks** for a single-intake institution: ~`3` weeks domain modelling in
Krayin, ~`2` weeks MCP server, ~`2` weeks agent plus preview-then-confirm, ~`1` week
Temporal workflows, ~`2` weeks SIS handoff and UAT. 🔴 **Add `3`–`4` weeks for Corteza
instead of Krayin** — more modelling, less out of the box.

### Why the licence position is the selling point

🟢 **Every component above is MIT or Apache-2.0.** 🔵 **A studio can fork this, brand it,
host it multi-tenant and sell it as a product** — which is true of no other pattern in
this file. 🔴 **The moment the SIS enters the tree rather than sitting behind an API,
that stops being true**, and the usual way it happens is a developer deciding it is
simpler to patch OpenEduCat than to call it.

### Three disqualifiers — check these first

- 🔴 **The institution already runs a commercial admissions CRM** (Slate dominates US
  higher ed; Salesforce Education Cloud is common). 🔵 **Then this is a displacement sale
  against an entrenched incumbent, which is a different and much harder motion** — pitch
  an agent layer on *their* CRM instead.
- 🔴 **Admissions is statutorily centralised.** UCAS in the UK, and national
  clearing-house systems elsewhere, mean the institution does not own the top of the
  funnel. 🟡 **The pattern still works below the centralised step — check where the
  boundary falls before scoping.**
- 🔴 **The client expects an education-ready product out of the box.** 🔵 **Krayin knows
  nothing about education**; there is no applicant, programme or intake entity until you
  build one. **If the client is comparing against OpenEduCat's admissions module on
  features, they will not like the first demo** — sell the licence position and the
  product ceiling, or do not sell this.

## P22 — Canvas-native grading assistant with human-in-the-loop publication

🟢 **Why this pattern exists.** `T24` established that education's agent supply is
atomised: this base found **seven** Canvas/Moodle grading agents in one window with a
**median of `0★`**, three of them unlicensed or AGPL. 🔴 **There is no mature grading
agent to fork.** 🟢 **But the connector layer is mature and permissive**, so the right
move is to adopt the connector and write the loop. This is the most-requested education
engagement shape and the one where a studio most often wastes a sprint looking for a base
to fork.

### Components — all MIT, no copyleft anywhere in the tree

| Role | Component | Licence | Stars | Why this one |
|---|---|---|---|---|
| LMS connector | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT | 324 | The only Canvas agent surface in this base with real traction. Includes a bulk-grading skill. 🔴 Tool count is inconsistent on its own page (README `128`, sidebar `102`) — pin the profile you enable. |
| Moodle variant | [`Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) | MIT | 206 | Swap in for Moodle estates. 🟢 **Read-only (10 tools)** — so for Moodle the write path must be built separately, which is a scoping fact, not a defect. |
| Orchestration | [`LangGraph`](https://github.com/langchain-ai/langgraph) | MIT | 44.9k | Explicit state machine. The approval gate must be a *graph node*, not a prompt instruction. |
| Content / rubric generation | [`educhain`](https://github.com/satvik314/educhain) | MIT | 388 | Generates questions, rubrics and feedback scaffolds as a library node. |
| Learner-path checkpoints | [`interactive-learning`](https://github.com/geekjourneyx/interactive-learning) | MIT | 52 | 🔵 **Optional, and read it as a design not a dependency (`52★`, `4` commits).** Supplies the verifiable-checkpoint card for returning remediation to a student who failed a rubric line. |
| Learning-activity record | [`learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | (held) | Writes what was practised and mastered to an LRS, so grading produces evidence rather than only a number. |

🔴 **Explicitly NOT in this tree, and each exclusion is deliberate:**
`canvas-pilot` (`AGPL-3.0` — network clause kills a hosted deliverable),
`AI-Grading-Tool` (**no grant at all**), `tutor-gpt` (`GPL-3.0`),
`PageLM` (source-available, not OSI).

### Wiring

```
      instructor rubric (Markdown, version-controlled)
                        │
                        ▼
   canvas-mcp ──► fetch submissions + roster  ──► LangGraph state
                        │
                        ▼
              grade node (LLM + educhain rubric scaffold)
                        │
                        ▼
        ┌───── PROPOSED grades + per-line feedback ─────┐
        │        (written to a staging store,            │
        │         NEVER to the Canvas gradebook)         │
        └────────────────────┬───────────────────────────┘
                             ▼
                  instructor review UI  ◄── the gate
                             │  approve / amend / reject
                             ▼
   canvas-mcp ──► publish approved set only ──► Canvas gradebook
                             │
                             ▼
              learnmcp-xapi ──► xAPI statements to the LRS
```

🟢 **The architectural rule, and it is the whole pattern:** the agent writes to a
**staging store**, never to the gradebook. Publication is a separate, explicitly
authorised action over an approved set. 🔵 **This is not a preference — it is the
convergent design of every credible implementation found.** `mini-homework-agent`
(review-then-publish), `canvas-pilot` (`scan -> approval -> execute`),
`waseda-moodle-mcp` (`prepare_* -> confirm_action`) and `mcp-odoo`
(`preview_write -> validate_write -> execute_approved_write`) all independently arrived
at it. 🔴 **Four unrelated projects converging on the same gate is the strongest design
evidence in this base.**

### Why the gate is also the compliance artefact

🟢 **The review step is what makes this sellable under every regime in `T25`
simultaneously.** EU AI Act Annex III treats evaluation of learners as high-risk and
requires **human oversight** (duties from `2027-12-02`); Korea's AI Basic Act requires
human oversight and a pre-deployment impact assessment for in-scope K-9 assessment; US
state and district policies increasingly bar AI from being the **sole basis** for a
high-stakes decision, and D.C.'s `2026-27` guidance bars AI from grading outright.
🔵 **A human-approval gate that is logged satisfies the common core of all of them**, and
the staging store is where the audit trail lives. 🟢 **Build the log as a first-class
output, not a debug artefact:** proposed grade, model version, rubric version, reviewer
identity, decision, timestamp.

🔴 **Scope check before selling this anywhere:** if the learners are K-9 in Korea it is
high-impact and needs the impact assessment; if the institution is a US district, check
whether local policy bars AI grading entirely — in which case this pattern is sold as
**feedback drafting**, with no grade path at all, which is still most of the value.

### Build estimate

🟢 **`5`–`7` weeks** for a single-course pilot on Canvas with a real instructor:
`1` week connector + rubric schema, `2` weeks grading loop and staging store,
`1`–`2` weeks review UI, `1` week xAPI/logging, `1` week hardening.
🔴 **Add `2`–`3` weeks for Moodle**, because `Moodle-MCP` is read-only and the write path
is yours to build. 🔵 **Add `2` weeks if the client needs the conformity pack**
(impact assessment, oversight design, model/data documentation) — and per `T25`, build it
once and reuse it across jurisdictions.

🔴 **The risk that actually kills these pilots is not technical.** It is that instructors
do not trust the proposed grades and review every line by hand, at which point the agent
has saved nothing. 🟢 **Mitigate by measuring agreement rate from week one** — proposed
vs. published grade, per rubric line — and by shipping the highest-agreement rubric lines
first. 🔵 **That metric is also the client's ROI story**, and per the LATAM finding that
there are roughly ten times more institutions using AI than measuring it, it is the thing
almost nobody builds.


## P23 — Brightspace/Blackboard study agent with an auditable write gate (Global; the first pattern here that serves D2L and Blackboard institutions)

🟢 **Why this pattern exists.** Until `p809` this KB could not serve a Brightspace or
Blackboard client at all — both are incumbents, neither had a connector on any shelf.
Five verified agents now exist, and they split cleanly into a **read tier** and a
**single gated write tier**, which is exactly the shape a safe engagement wants.

**Who it is for:** a university on D2L Brightspace or Blackboard Learn that wants a
student-facing study assistant (deadlines, course material, grade context) and, later, a
*narrow* ability to act — without handing an agent the power to submit coursework by
accident.

### The stack, by named repository

| Role | Repo | Licence | ★ | Why this one |
|---|---|---|---|---|
| **Brightspace read plane** | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | MIT | 67 | `29` tools, **read-only by declaration**; SSO + 2FA, password in OS keychain, session state AES-256-GCM. The most-starred and best-secured of the five. |
| **Brightspace write plane** *(optional, phase 2)* | [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp) | MIT | 16 | The only agent in this base that can write to Brightspace, behind **two opt-ins + `dry_run` + idempotency key + audit log**. |
| **Blackboard read plane** | [`Mattlo0546/blackboard-mcp`](https://github.com/Mattlo0546/blackboard-mcp) (vendor-neutral Ultra) or [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, far more mature) | MIT / ISC | 1 / 13 | Pick by tenant: `campus-cli` has `851` commits but is UPC/UPN-shaped; `blackboard-mcp` is generic but `4` commits. |
| **Learner-record write path** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | 16 | Writes what the learner **did** to any xAPI 1.0.3 LRS. 🟢 **This is where progress belongs — not in the LMS.** |
| **Orchestration + policy nodes** | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | MIT | — | Explicit graph: the write gate is a node you can show an auditor. |
| **Content packaging** *(if the agent generates material)* | [`dmmat/Scormly`](https://github.com/dmmat/Scormly) | MIT | 5 | Browser-only, no backend; exports SCORM 1.2/2004 so output mounts in either LMS. 🔴 cmi5 leg unverified upstream. |

### How to wire it

1. **Phase 1 is read-only, and ships on its own.** Stand up the Brightspace or Blackboard
   read plane. Every tool is a retrieval; there is nothing to gate. 🟢 **Most of the
   perceived value — "what is due, what did I miss, what does this rubric mean" — is
   entirely in this phase**, which is why it is worth shipping before any write exists.
2. **Put progress in the LRS, not the LMS.** Route every "learner practised / mastered /
   attempted" signal through `learnmcp-xapi` into the institution's LRS. 🔵 The LMS stays
   the system of record for *grades*; the LRS becomes the system of record for
   *learning*, and only the second one is safe for an agent to write.
3. **Phase 2 adds writes only if the client asks, and only through the gate.** Swap in
   `JhostinAleck/brightspace-mcp` with `writes.enabled: false` **and** no
   `--enable-writes` flag. Turn on `dry_run` first and run a full week in preview,
   diffing proposed writes against what staff would have approved.
4. 🔴 **Decide `submit_assignment` explicitly, in writing, with the registrar — not in
   config review.** It is the one tool in this stack that can commit academic work on a
   student's behalf. The default in this pattern is **off, permanently**, and the other
   two write tools (`post_discussion_reply`, `mark_announcement_read`) are the ones
   actually enabled.
5. **Keep the audit trail from day one.** `JhostinAleck` emits a warning-level log entry
   and requires an idempotency key per write. Ship those into the client's SIEM in phase
   2, and feed the same artefacts into `P17`'s EU AI Act Article 50 evidence pack.

### Effort and the honest caveats

🟢 **Phase 1: 3–4 weeks.** Phase 2 (gated writes + audit plumbing): **a further 4–6
weeks**, most of it governance rather than code.

🔴 **Four things to price, not discover:**
- **No vendor publishes an MCP server.** Every path here is unofficial — REST API, SSO
  session, or a scraped cookie. Confirm with the institution's IT that API access is
  sanctioned **before** quoting, or the integration is a policy violation wearing an
  architecture diagram.
- 🔴 **`campus-cli` brokers its tools through a remote relay (`mcp.campuscli.com`).** For
  an institution, **fork it and terminate the relay in-tenant** — the `ISC` grant allows
  exactly that. Do not deploy it as-is.
- 🔴 **`kingdonkatsu/ntulearn-mcp` is deliberately NOT in this stack** despite being
  verified `MIT`: it authenticates by auto-reading the `BbRouter` cookie out of the
  user's browser. Excellent reference, unacceptable dependency.
- 🔴 **`Mattlo0546/blackboard-mcp` has `4` commits.** If the client is on Blackboard
  Ultra and wants a supported path, budget to maintain a fork rather than to adopt.

## P24 — District early-warning agent that survives a FRIA (North America first, EMEA-portable)

**The ask this serves.** *"Which of my students are at risk, and why?"* — asked by a teacher,
answered from the SIS, in a form a data-protection officer will sign off.

**Why it is now buildable.** The reference implementation exists and comes from the standards
body: [`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)
(`Apache-2.0`). 🔴 **Its own README says "demonstration purposes only; not intended to be a
robust production solution" — so this pattern ships the ARCHITECTURE and re-implements the
code.**

**Wiring.**

| Layer | Component | License | Role |
|---|---|---|---|
| Source of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | `Apache-2.0` | The district's existing Ed-Fi ODS/API |
| Semantic layer | `datamart/` from the prototype | `Apache-2.0` | PostgreSQL data mart; descriptor mapping; time-travel views. **Agents query the mart, never the ODS** |
| Access control | `datamart/sql/mcp-reader.sql` | `Apache-2.0` | `CREATE ROLE mcp_reader LOGIN`; `ALTER ROLE mcp_reader SET default_transaction_read_only = on`; `REVOKE ALL ON SCHEMA public`; `GRANT SELECT ON ALL TABLES IN SCHEMA analytics` |
| Identity | **Keycloak** (OAuth) | Apache-2.0 | Educator signs in; server takes the user from the token's **verified email** |
| Agent surface | `mcp-server/` — `get_my_scope`, `list_my_sections`, `find_students`, `list_students_at_risk`, `get_student_summary`, `get_attendance_trend` | `Apache-2.0` | Streamable HTTP on `:3000/mcp`; every tool read-only, returning compact JSON **naming the tables used** |
| Evidence trail | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | Records what the agent surfaced and what the human then did — the FRIA artifact |

**The three controls, and why each is where it is.**
1. 🟢 **Read-only at the DATABASE ROLE**, not in the prompt. A prompt restriction is defeated
   by the next jailbreak; `default_transaction_read_only` is defeated by nothing the model emits.
2. 🟢 **`get_my_scope` makes authorisation ANSWERABLE.** The agent can state what this educator
   may see before it answers — which is what turns "it only shows your students" from a claim
   into a demonstrable property.
3. 🟢 **Table-level provenance in every response** gives the FRIA its data-flow section
   for free.

**Regulatory fit.** 🟢 EU **Art. `27` FRIA** for public deployers (education is Annex III
high-risk, standalone deadline `2027-12-02`); 🟢 **Oklahoma's teacher-review requirement** and
🟢 the **Philippines' DepEd AI registry** are all satisfied by the scope tool plus the xAPI
trail. 🔴 **The agent must never rank, score or flag as the sole basis of a decision** — it
surfaces, a named teacher decides (`T30`).

**Estimate.** `8`–`10` weeks against an existing Ed-Fi ODS; `14`+ if the district's SIS is not
Ed-Fi-conformant and the mart must be built from a vendor export.

🔴 **Do not attempt on PowerSchool.** The three PowerSchool MCP servers found at `p810` carry
`NONE`, `NONE` and `GPL-3.0` — there is no permissive client to build on (`agents/top.md`,
Declared gaps).

## P25 — Markdown-to-SCORM course pipeline with a conformance gate before delivery (Global; APAC-sized)

**The ask this serves.** A training programme that must land in an LMS the client already runs,
at volume, with content reviewable before it ships. 🔵 **India's CBSE mandate — `10`M+ teachers
to train through NISHTHA against a fixed curriculum and a dated academic year — is this pattern
at national scale** (`intel/market.md`, APAC).

**Wiring — all permissive, no copyleft anywhere in the chain.**

| Step | Component | License | Role |
|---|---|---|---|
| 1. Write | Markdown in the client's own repo | — | 🟢 **Content reviewable in a pull request before it is a course** |
| 2. Assemble | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) | `MIT` | Agent-driven assembly of interactive SCORM-compliant courses |
| 3. Package | [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | `MIT` | HTML / design bundles → **SCORM 2004 / 1.2**, offline |
| 4. **Gate** | the same repo's **zip validator** | `MIT` | 🟢 **Validates ANY SCORM zip without an LMS** — a pre-delivery gate rather than a post-upload surprise |
| 5. Assess | [`johnnyrobot/qtimaker`](https://github.com/johnnyrobot/qtimaker) | `BSD-3-Clause` | Markdown → **QTI** item bank, same review path |
| 6. Code exercises | [`taybenlor/runno`](https://github.com/taybenlor/runno) | `MIT` | 🟢 **Sandboxed WASI execution in the browser** — the untrusted-code boundary, and it moves per-learner compute off the hosting bill |
| 7. Deliver | [`Faixiang/Moodle-MCP`](https://github.com/Faixiang/Moodle-MCP) (`MIT`) · [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) (`MIT`) · [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | permissive | Into the LMS the client already runs |
| 8. Record | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | xAPI completion records |

🟢 **Step 4 is the one that earns its place.** Every other SCORM pipeline in the wild discovers
conformance failures on upload, per-LMS. 🔵 **A validator that runs without an LMS turns a
delivery risk into a CI check.**

🔴 **Licence trap, and it is the one that actually bites at this scale.** If an item bank is
retrieved rather than authored — e.g. [`weishao2/tizhuang-agent-skills`](https://github.com/weishao2/tizhuang-agent-skills)
(`MIT`, `39★`, 20M+ K-12 items) — 🔴 **the MIT grant covers the SKILL CODE and grants nothing
in the QUESTION BANK behind it.** 🟢 **Clear the corpus separately from the tooling** — the
same split as `P800-3`.

🔴 **`boyuchengz/canvas-mcp` is read-only by construction**, so step 7 into Canvas needs a
separate authenticated write path; do not assume the agent can publish.

**Estimate.** `6`–`8` weeks for the pipeline; content volume is the cost driver, not the code.

## P26 — Assessment assistance that is regulator-shaped: QA and moderation, never the sole marker (EMEA first)

**The ask this serves.** An awarding body or university wants AI in marking and has been told
it cannot have it. 🟢 **Ofqual's rule names the open territory as precisely as the closed one**
(`T30`): **closed** — AI as sole marker in regulated qualifications, extended to non-exam
assessment; **open and explicitly endorsed** — **quality assurance, marker training,
moderation, second-marking.**

🔵 **So do not sell marking. Sell the four open categories, and build so that the closed one is
structurally unreachable.**

**Wiring.**

| Component | License | Role |
|---|---|---|
| [`erictrainnlpinxihu/Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent) | `MIT`, `94★` | Five-phase loop `perceive→plan→act→observe→respond`. 🟢 **The model decides only intent and confidence; routing, tool set and risk level are pinned in CODE** — which is the auditable separation a regulator asks to see |
| [`johnnyrobot/qtimaker`](https://github.com/johnnyrobot/qtimaker) | `BSD-3-Clause` | QTI item bank from Markdown, reviewable before use |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 `GPL-2.0` | Full assessment platform **only if** the client can carry GPL; otherwise keep it out of the deliverable and integrate at the process boundary |
| [`VIABLE-Learning-Lab/viable`](https://github.com/VIABLE-Learning-Lab/viable) | `MIT` | A harness that wraps any agent to keep teaching policy outside the model — same control shape, arrived at independently |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | `MIT` | The audit record: what the agent proposed, which human decided, when |

**The four sellable products, in order of regulatory ease.**
1. 🟢 **Marker training** — generate calibration scripts with known marks from the item bank.
2. 🟢 **Quality assurance** — agent re-marks a sample; **disagreement with the human marker is
   the output**, not a grade. 🔵 **The deliverable is a flag for human review, which is the
   regulator's own stated use.**
3. 🟢 **Moderation** — surface cross-marker drift across a cohort.
4. 🟡 **Second-marking** — agent as one of two markers, human reconciles. 🔴 **Only where the
   human reconciliation is recorded and binding.**

🔴 **The structural guarantee matters more than the policy.** 🟢 **Build so no agent output
reaches a candidate record without a named human write** — `Grader-agent`'s code-pinned
routing plus `P22`'s human-in-the-loop publication gate already give this; the xAPI trail
proves it after the fact. 🔵 **Then "AI is not the sole marker" is a property of the system,
not a promise in the contract.**

🔴 **Do not cite the reported DfE "progressive disclosure" standard in a bid** — `p810` could
not confirm it against any government source (`T30`).

**Estimate.** `6`–`8` weeks for QA and moderation on an existing item bank; second-marking adds
a reconciliation UI and a conversation with the regulator.

---

## P27 — The OneRoster agent nobody has built (North America first, Global-portable)

🟢 **This is the best-evidenced contribution target in this base, and `p811` re-tested the
evidence rather than restating it.** `OneRoster` — the 1EdTech standard by which a student
information system hands class rosters, enrolments and gradebook data to everything else —
is named over `3,000` times across this KB. 🔴 **And there is no agent for it.**

### Why the gap is real, with the evidence

| Check | Result (`2026-11-13`) |
|---|---|
| `gh api -X GET search/repositories -f q="oneroster mcp"` | 🔴 **zero items** |
| Vendor connector documentation (ibl.ai, dated October 2026) | 🔴 States that neither **1EdTech** nor **ClassLink** publishes an MCP server; its own "OneRoster agent skill" is a `SKILL.md` that assumes **you** host the server |
| Tooling that DOES exist | 🟢 a conformance suite, an importer, two server implementations and a client library — see below |

🔵 **Two independent channels, one answer. The standard has libraries and no agent.**

### The components — every one verified on the `repo:` channel this pass

| Component | Repo | Licence | State |
|---|---|---|---|
| **OneRoster client (REST + CSV)** | [`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) | 🟢 MIT | pushed `2026-07-15`, `0★`, npm `@longsightgroup/oneroster` `0.3.0` — **new to this base at `p811`** |
| **Conformance gate** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 Apache-2.0 | `7★`; vendor-neutral, published by a party with no LMS to sell |
| **Reference server (wire format only)** | [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) | 🟢 MIT | 🔴 stale since `2020-07-30` — read it, do not depend on it |
| **Importer (separate process)** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) | 🔴 GPL-2.0 | run as its own process; never link it |
| **The control topology to copy** | [`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP) | 🟢 Apache-2.0 | read-only enforced at the **database role**, six tools, OAuth scope check |

### How it wires together

1. **Ingest.** Point `LongsightGroup/oneroster` at the district's OneRoster endpoint *or* its
   CSV export. 🔵 **Support the CSV binding first** — US districts hand over a CSV far more
   often than they stand up a REST service, and the MIT client covers both bindings, which is
   the specific reason it is the base of this pattern.
2. **Land it read-only.** Load into Postgres under a role pinned
   `default_transaction_read_only = on` with `GRANT SELECT` on the roster schema only.
   🟢 **Copy this from the Ed-Fi prototype: the read-only property is enforced by the database
   role, not asked for in a prompt.** That is the difference between a control and a convention.
3. **Expose few tools.** Six, after Ed-Fi's example — `get_my_scope`, `list_my_sections`,
   `find_students`, `get_section_roster`, `get_enrolment_changes`, `get_sync_health` — each
   returning the tables it read. 🔴 **Do not build a 77- or 137-tool surface; this base has
   two of those already and both are governance objects rather than features.**
4. **Gate the identity.** The agent's scope is the signed-in educator's scope, resolved
   server-side at every call. Never a shared service account.
5. **Prove conformance before delivery.** Run the Google conformance suite against the
   district's endpoint and **attach its output to the acceptance criteria**. 🟢 **This is the
   commercially clever part: the suite turns "the integration works" from an opinion into a
   contractual artifact, and it is Apache-2.0 so it can ship with the deliverable.**

### Why it survives review

🔵 **It reads rosters and writes nothing**, so in the EU it is outside Annex III's assessment
category, and in the US it is a FERPA *scope* question rather than a decision-making one.
🟢 **Every component is MIT or Apache-2.0 except the GPL importer, which runs as a separate
process by design.**

### Estimate

**5–7 weeks** for the ingest + read-only store + six-tool server + conformance run, assuming
the district can produce either a OneRoster endpoint or a conformant CSV export.
🔴 **Add 2–3 weeks if the "OneRoster export" turns out to be a bespoke CSV**, which is the
most common surprise on this seam.

### Three disqualifiers — check these first

1. 🔴 **The district's SIS is PowerSchool and they want the agent to talk to it directly.**
   PowerSchool has three MCP servers in this base and none with a usable grant (`NONE`,
   `NONE`, `GPL-3.0`). Go through OneRoster, or the pattern changes into a licence negotiation.
2. 🔴 **They want write-back of grades.** That is the gradebook service, it is a decision
   surface, and it moves the engagement into `P24`'s FRIA territory. Scope it separately.
3. 🔴 **They have no OneRoster export at all.** Then the first deliverable is the export, not
   the agent, and `oat-sa/oneroster-import` (GPL-2.0, run standalone) is where to start.

---

## P28 — The national school portal family agent (EMEA first, and the only pattern here whose buyer is a ministry)

🟢 **`p811` found that European education agent supply is attached to state-operated portals
rather than to LMS platforms (`T31`).** 🔵 **This pattern is what to do with that: one agent,
one portal, a family as the user, and a public body as the buyer.**

### The seam, with the reference implementations found in one five-day window

| Portal | Operator | Country | Reference implementation | Licence |
|---|---|---|---|---|
| Schulportal Hessen (Lanis) | the federal state of Hesse | 🇩🇪 | [`udondan/lanis`](https://github.com/udondan/lanis) | 🟢 MIT |
| DSBmobile (timetables, substitutions) | the DSB service | 🇩🇪 | [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) | 🟢 MIT |
| Admentum | Swedish platform vendor | 🇸🇪 | [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) | 🟢 MIT |
| iPasen / Séneca | Junta de Andalucía | 🇪🇸 | [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) | 🟢 MIT |
| Greek School Network (`sch.gr`) | Greek Ministry of Education | 🇬🇷 | [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) | 🟢 MIT |
| `edu.by` constructor | Belarusian national school-web service | 🇧🇾 | [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) | 🔴 GPL-3.0 |
| PRONOTE + EduConnect | Index Éducation + French state IdP | 🇫🇷 | [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) | 🔴 GPL-3.0-or-later (`T33`) |

### How it wires together

1. **Pick the portal, not the LMS.** The system a family logs into daily is the one worth an
   agent. 🔴 **A proposal offering "an agent for your Moodle" is answering a question the Land
   did not ask.**
2. **Read the reference implementation for the SEAM, then write your own client.** Every row
   above is `0–2★`, single-maintainer and self-declared unofficial. 🟢 **What they give you is
   which verbs the portal exposes and which auth path works** — normally the most expensive
   unknown in a public-sector bid. 🔴 **For France, `T33` applies: the GPL comes from the
   `@blockshub/pawnote-lts` client, so a permissive deployment needs a clean-room PRONOTE
   client as its own funded deliverable.**
3. **Adopt the two controls the field converged on without coordination.**
   🟢 **Preview-then-confirm on every write** — stated independently by
   [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) 🇪🇸,
   [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) 🇧🇾 and three earlier
   jurisdictions in this base (`T20`, now five).
   🟢 **Rate-shape the context** — [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) 🇸🇪
   serves messages **one item per call**, which bounds how much of a minor's correspondence
   can enter a model context in a single tool call. 🔵 **That is a quantitative limit rather
   than a prompt instruction, and it is the single most copyable idea in this pass.**
4. **Default to read-only for anything touching a minor's record**, and keep writes to the
   family's own actions (absence notes, meeting confirmations) behind the confirm step.
5. **Ship the FRIA with it.** 🟢 **Four of these seven portals are operated by a public body,
   so the EU AI Act Art. `27` fundamental-rights impact assessment falls on the DEPLOYER
   because the deployer is public.** 🔵 **Pair this pattern with `P14`'s deployment registry
   and `P2`'s conformance layer: the integration and the compliance artifact arrive in the
   same proposal, which is what actually unblocks a ministry purchase.**

### Estimate

**8–11 weeks** per portal for a read-mostly family agent with a confirm-gated write path, the
one-item-per-call context limit, and an Art. 27 FRIA pack. 🔵 **The second portal is roughly
`60%` of the first** — the controls, the FRIA template and the confirm gate are portable; only
the client changes.

### Three disqualifiers — check these first

1. 🔴 **The portal has no documented API and its terms forbid automated access.** Every
   reference above is "unofficial"; a ministry engagement needs the operator's written
   permission, and that conversation comes before any code.
2. 🔴 **The buyer wants it to speak to pupils directly.** Then the learner's AGE changes the
   regulatory category (`T25`) and child-safety law binds before education law does.
3. 🔴 **France, without funding for a clean-room PRONOTE client.** The permissive position
   cannot be reached by relicensing (`T33`), so a fixed-price permissive deliverable is not
   available on the French seam this quarter.

## P31 — Chinese university study agent on Chaoxing / 学习通 (APAC first, and the only pattern here whose core deliverable is a REFUSAL)

**Who it is for.** A Chinese higher-education institution, or an ed-tech serving one, that wants a
study agent over the LMS students actually use: timetable, deadlines, chapter progress, lecture
materials and replay transcripts.

**Why it exists as a separate pattern.** 🔴 **Because the dominant open-source implementation in
this market crosses the academic-integrity line by default (`T36`), a Chaoxing engagement cannot
be scoped as "adopt the best repo".** 🟢 **The selection criterion is not capability — it is which
tools the server declines to implement.**

### The components — all verified at `p813`, licences byte-read

| Component | Repo | Licence | Role |
|---|---|---|---|
| LMS surface (the anchor) | [`DanMo661/xuexitong-cli`](https://github.com/DanMo661/xuexitong-cli) | **MIT** (`1,065 B`, `sha256:3486ae61…`) | 🟢 **Read-only by declaration — *"所有工具均为 GET/查询语义，不提交任何表单"*.** Timetable (+`.ics`), deadlines, exams, chapter task-points, notices, materials, cloud disk. `24★` |
| Lecture transcripts | [`ILLENIUM-25/chaoxing-subtitles`](https://github.com/ILLENIUM-25/chaoxing-subtitles) | **MIT** (`1,068 B`, `sha256:4b8fa2fc…`) | Exports course-replay subtitles — 🟢 **the retrieval corpus; without it the agent has metadata and no content** |
| Session-holding variant (optional) | [`Cyoung-Van/chaoxing-mcp`](https://github.com/Cyoung-Van/chaoxing-mcp) | **MIT** (`1,067 B`, `sha256:6aa62f5f…`) | 🟢 Reaches Chaoxing **through Chrome CDP**, so the browser holds the session and no password is handled at all |
| Vector store | [`qdrant/qdrant`](https://github.com/qdrant/qdrant) | **Apache-2.0** | Transcript + material index, self-hosted |
| Model gateway | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | **MIT** | 🔴 **Required, not optional: route to a domestically hosted model.** Data residency is the gating constraint, not a preference |
| Audit spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Records what the agent did, per `P17` |

🔴 **Explicitly NOT in the build:**
[`DeliciousBuding/chaoxing`](https://github.com/DeliciousBuding/chaoxing) (Apache-2.0). Its
architecture is the best in this base and its scopes include automated attendance sign-in and
coursework submission. 🟢 **Cite its security design in the proposal; do not take the dependency.**
🟡 **And read `xiny8127-glitch/xuexitong-plus`'s tool list before adopting it — "question text
extraction" sits one step from the same line.**

### How it wires together

1. **Pin the tool surface to reads, and write the refusal down.** 🟢 **The deliverable's first
   artifact is a tool allowlist: timetable, deadlines, materials, transcripts, notices.**
   🔴 **Sign-in, answer generation and submission are not unimplemented — they are DECLINED, in
   writing, with the refusal behaviour specified** (the agent states it cannot do this and why).
   🔵 **`DanMo661/xuexitong-cli`'s README already does exactly this; the engagement inherits its
   posture rather than inventing one.**
2. **Prefer CDP for credential handling.** Use `Cyoung-Van/chaoxing-mcp`'s Chrome-CDP route, or
   the anchor's env-var path (`凭据不落盘` — credentials never hit disk). 🔴 **Do NOT take
   `Han-maker-wp/chaoxing-mcp`'s reverse-engineered AES login into a client deliverable: it is
   lifted from Chaoxing's own JavaScript and legal review will ask about the provenance.**
3. **Build the corpus before the agent.** Export replay subtitles, chunk by chapter, index in
   Qdrant alongside the material files. 🟢 **The agent's value is "explain week 7 from the lecture",
   which needs content, and every other repo in the cluster returns only metadata.**
4. **Gate the model.** Route through LiteLLM to a domestically hosted endpoint; no transcript
   leaves the deployment.
5. **Ship the integrity boundary as a signed document**, not a config comment — the institution's
   academic-integrity office is the approver, and it is a different approver from IT.

**Rough estimate.** `6–8 weeks` for a faculty pilot. 🔵 **Two of those weeks are the integrity
boundary and its approval, and that is not padding: it is the part of this engagement that cannot
be bought from the open-source cluster.**

**Risks.** 🔴 **Chaoxing publishes no API; every component scrapes or replays an undocumented
login, so a platform change breaks the pilot.** 🔴 **`17` of the cluster's `19` repositories were
created since `2026-09-11` and none has an institutional owner — maintenance is yours from day
one.** 🟡 Star counts are low; this is a BUILD-with-components pattern, not an adopt pattern.

## P32 — The multi-system family agent (North America first, and the only pattern here whose user is a PARENT)

**Who it is for.** A US district, or a consumer product serving its families, where one household
tracks several children across **different systems that do not talk to each other** — an SIS
portal, an LMS, and often a different SIS per district after a boundary change or a move.

**Why it exists as a separate pattern from `P27`.** `P27` builds on the **state data standard**
(OneRoster/Ed-Fi) and its buyer is a district IT office. 🟢 **`P32`'s buyer is the family, the
integration point is the parent portal login, and the whole supply in this tier was written by
parents and students** (`T31`'s North American instance).

### The components — all verified at `p813`, licences byte-read

| Component | Repo | Licence | Role |
|---|---|---|---|
| SIS portal, **multi-district** | [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | **MIT** (`1,067 B`, `sha256:17dd0009…`) | 🟢 **The spine. `20` tools; linked districts AUTO-DISCOVERED via CUPS SSO from a single account** — the only repo in the tier that handles more than one district. Exactly one write/IO-gated tool (`ic_download_document`) |
| LMS, parent role | [`chrischall/canvas-parent-mcp`](https://github.com/chrischall/canvas-parent-mcp) | **MIT** (same author) | The Canvas observer surface |
| Second SIS (Edupoint districts) | [`coolcrazycid/studentvue-mcp`](https://github.com/coolcrazycid/studentvue-mcp) | **MIT** (`1,069 B`, `sha256:60fe23fd…`) | 🟢 Read-only; headless browser against the student site, so it survives districts that disabled the legacy app API |
| Schoology, **no credential at all** | [`obfuscated-tm/dewey`](https://github.com/obfuscated-tm/dewey) | **MIT** (byte-read `900 B`, vs GitHub `NOASSERTION`) | 🟢 **Reuses the Schoology session Chrome already holds — *"no account · no passwords · nothing leaves your computer"*.** The posture to copy |
| Client library (if you build) | [`leftathome/schoology-go`](https://github.com/leftathome/schoology-go) | **MIT** (`1,091 B`, `sha256:7a2044fc…`) | The only shared client under the whole tier |
| Orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** | Fan-out across systems, one answer per child |

### How it wires together

1. **Model the household, not the account.** 🔴 **Every repo in this tier assumes one student and
   one district.** 🟢 **`infinitecampus-mcp` is the exception and its `student: "<name> (<district>)"`
   addressing is the convention to adopt across the other connectors.**
2. **Copy `dewey`'s credential posture wherever the system allows it.** 🟢 **Browser-session reuse
   removes the stored password entirely** — and the stored-password defect is the single most
   repeated finding across every cluster this base has measured, in four regions.
3. **Keep it read-only and say so.** Every component here is read-only by design; 🟢 **preserve
   that as a product property rather than quietly adding writes later** (`T20`).
4. **Fan out, then summarise per child.** One LangGraph node per system; the answer a parent wants
   ("what is due this week, for both kids") never exists in any single portal.

**Rough estimate.** `5–7 weeks` for a two-system, multi-district pilot.

**Risks.** 🔴 **No component has an institutional owner and most have `0–5★`;** treat all of them
as reference implementations you will fork and maintain. 🔴 **Portal terms of service frequently
restrict automated access — this is a district-permission conversation before it is a build**, and
`coolcrazycid/studentvue-mcp` says so in its own README. 🔴 **PowerSchool, the largest SIS in the
tier, has exactly ONE agent and it is unlicensed** — if the district runs PowerSchool, this pattern
starts with a build, not an adopt.

## P33 — The clean-room client library as the durable asset (Global method, APAC/North America first)

**Who it is for.** A studio that expects more than one engagement against the same education
system — Chaoxing in China, StudentVUE or Infinite Campus in the United States — and wants the
second engagement to be cheaper than the first.

**Why it exists.** 🟢 **`p813` shelved `29` agents and then asked what they build on. The answer
was nothing:** `studentvue python client library` → `0`, `infinite campus api client` → `0`,
`chaoxing api library` → `0`, `schoology api client library` → `1` (at `1★`),
`moodle webservice client python` → `1` (unmaintained since `2024-08-13`). 🔵 **`19` Chaoxing
agents each reverse-engineer the same AES login, separately.** 🟢 **`T33` warned that an agent's
client library can make it unshippable; the stronger finding is that for the systems that dominate
agent supply, the library does not exist at all.**

### The recipe

| Step | What you build | Why it is defensible |
|---|---|---|
| 1 | **Pick the system by cluster density, not by star count.** Chaoxing (`19` agents), Schoology (`11`), StudentVUE (`7`) | Density measures demand that already exists |
| 2 | **Write the client clean-room, from observed HTTP** — authentication, session persistence, ~`12` read endpoints | 🔴 **Not from `Han-maker-wp/chaoxing-mcp`'s lifted JavaScript: provenance is the first thing a client's legal review asks about** |
| 3 | **Grant it MIT or 0BSD** | 🟢 **`kristoffervp/vigilo-mcp` shows the 0BSD option: no attribution obligation at all, so a client can vendor it without a notice file** |
| 4 | **Publish it, then build the agent on top** | The agent is the engagement; the library is the asset that makes the next one cheaper |
| 5 | **Instrument it** with [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (**MIT**) | Per `P17` |

🟢 **The cheapest variant of this pattern is not a build at all.** 🔴
[`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) is the most-starred Moodle MCP server
in existence (`57★`, `17` forks) and carries **no licence file at either branch root**, while
`README.md` returns `200` — so it exists and is simply ungranted (`T37`). 🟢 **One issue asking the
author to add a `LICENSE` converts the tier's anchor into a build-safe dependency.** 🔵 **Ask
before you build; the same question is owed to the `5` TronClass repositories 🇹🇼, which are a
complete unlicensed tier.**

🔵 **And where the system's operator is a ministry, there is a third option that beats both.**
🇰🇷 **`arapodcho/mcp_server_neis_api` needs no scraping, no reverse-engineered login and no learner
credential — because NEIS publishes an open-data API.** 🟢 **It is the only row in this pass's
harvest with that property, and it is what every other row would look like if the system published
one. "Ask the ministry to publish the API" is a real engagement option** (`P28`'s buyer is the same
ministry).

**Rough estimate.** `4–6 weeks` for the library plus `4` weeks for the first agent on it.
🟢 **The second engagement on the same system is then a `2–3 week` build.**

## P29 — Agent on a Frappe-based education ERP (Global, configuration not build, and the first pattern here whose connector is FIRST-PARTY)

**Who it is for.** An institution running **Frappe Education** (or ERPNext alongside it) that
wants an agent over the student record — enrolment, programs, assessment results, fees — without
commissioning a bespoke integration.

**Why it exists as a separate pattern from `P12`.** `P12` reaches OpenEduCat through two
**third-party** Odoo connectors, one of which ships a "YOLO mode" that bypasses its own access
control. 🟢 **Frappe's connector is in the framework itself.** See `T35`.

### The components — all verified at `p812`, licences byte-read

| Component | Repo | Licence | Role |
|---|---|---|---|
| Framework + **built-in MCP server** | [`frappe/frappe`](https://github.com/frappe/frappe) | **MIT** | 🟢 **The agent surface. `13` DocType-generic tools, verified in source at `frappe/mcp/tools/__init__.py`** |
| Education app | [`frappe/education`](https://github.com/frappe/education) | 🔴 GPL-3.0 | The system of record — `Student`, `Program Enrollment`, `Assessment Result`, fees |
| Approval-gated client (optional) | [`nasroykh/foxmayn_frappe_cli`](https://github.com/nasroykh/foxmayn_frappe_cli) | **MIT** | CLI/MCP/desktop with *"AI assistants with approval"* |
| Audit spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Per `P17`, records what the agent did as xAPI statements |

### How it wires together

1. **Enable the endpoint.** The built-in server raises `NotFound` until the **`enable_mcp`**
   system setting is turned on — 🟢 **so the default state is closed, and turning it on is a
   dated, auditable change.**
2. **Design the role, because the role IS the gate.** `frappe/mcp/tools/documents.py` states that
   document tools *"reuse REST API v2 permissions and controller hooks."* 🔴 **`create_document`,
   `update_document`, `delete_document` and `call_method` are generic over every DocType the
   authenticated role can reach.** 🟢 **So create a dedicated agent role with `SELECT`-equivalent
   permissions on the education DocTypes and nothing else** — this is the deliverable's core, and
   it is configuration, not code.
3. **Use the annotations in the client.** Tools ship `readOnlyHint: True` on reads and
   **`destructiveHint: True` on `update_document` and `delete_document`.** 🟢 **Bind the client's
   confirmation dialog to `destructiveHint`** rather than to a hand-maintained verb list.
4. **Let the agent discover the schema.** `search_doctypes` + `get_doctype_schema` mean no
   hard-coded field maps, so the pattern survives a Frappe Education version bump.
5. **Record every call** to the LRS per `P17`, so the institution can answer "what did it touch."

### Why it survives review

🟢 **The permission boundary is the institution's own, already audited, already staffed.** No
parallel allowlist to drift. 🟢 **The connector is MIT**, so nothing copyleft enters the
deliverable: `frappe/education` is GPL-3.0 but it is the system being *integrated with*, not
derived from.

### Estimate

**3–5 weeks.** Role design and permission testing `1–2`; client wiring to annotations `1`; xAPI
audit spine `1`; UAT against a staging site `1`.

### Three disqualifiers — check these first

1. 🔴 **A Frappe version without the built-in server.** Probe
   `frappe/mcp/__init__.py` on the deployed version before quoting; fall back to
   [`rakeshgangwar/erpnext-mcp-server`](https://github.com/rakeshgangwar/erpnext-mcp-server)
   (MIT) and re-price, because that is a third-party dependency again.
2. 🔴 **The client wants the agent to WRITE marks.** Then `T25`, `P26` and the EU AI Act
   assessment rules bind before this pattern does: the agent drafts, a human posts.
3. 🔴 **Someone quotes [`frappe/mcp`](https://github.com/frappe/mcp) (`170★`) as the connector.**
   🔴 **It is deprecated by its own README and is a tool-authoring SDK, not a generic connector.**
   Scoping on it turns a configuration job into hand-written tools per DocType.

## P30 — Agent on a LATAM university self-management system (LATAM first; Argentina and Brazil only)

**Who it is for.** An Argentine or Brazilian university, institute or edtech that wants a student-
facing assistant over the system students actually log into — **SIGAA**, **Sysacad** or
**SIU Guaraní** — none of which publishes an API.

🔴 **Read this disqualifier before anything else: this pattern is ARGENTINE AND BRAZILIAN, not
regional.** `SIMAT` (Colombia) returns `total_count=0`; the Mexican, Chilean and Q-Acadêmico legs
each returned `0`; `SIAGIE` (Peru) returns `25` repositories with **zero agents and zero
licences**. 🟢 **Quoting "LATAM coverage" from this pattern is a false claim** (`T34`).

### The components — every licence byte-read at `p812`

| Component | Repo | Licence | Role |
|---|---|---|---|
| 🇦🇷 Reference implementation **and the credential design** | [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) | **ISC** (`748 B`) | Moodle + Sysacad across `18` regionales; `12★`, `8` forks |
| 🇦🇷 SIU Guaraní + Moodle, multi-institution | [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) | **MIT + inherited ISC** (`1,980 B`) | Guaraní read-only; campus support probed mechanically |
| 🇧🇷 SIGAA tool surface | [`GallegoSz/sigaa-mcp`](https://github.com/GallegoSz/sigaa-mcp) | **MIT** (`1,076 B`) | `13` tools incl. three analyses; read-only by construction |
| 🇧🇷 The write-gate shape | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 AGPL-3.0 | **Prepares the filing as a draft; a human submits.** Take the SHAPE, not the code |
| Audit spine | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | Per `P17` |

### How it wires together

1. **Start from `utn-mcp`'s credential design, not from the Brazilian cluster's.** 🟢 **Password
   used once to mint a token and never stored; only the client token's hash kept; session
   encrypted at rest; OAuth in HTTP mode so each student binds their own account.** 🔴 **The
   SIGAA servers put the student's password in plaintext in the client config and say so — do not
   ship that, and do not host it for others, as `sigaa-mcp`'s own README warns.**
2. **Adopt the transport refusal as a product rule.** 🟢 **`utn-mcp` excludes campuses whose
   self-management has no valid HTTPS because *"la contraseña viajaría expuesta."* Make that a
   deployment precondition**, not a note.
3. **Keep the system of record read-only; gate anything else.** Guaraní is read-only by necessity
   (*"Guaraní no tiene API"*; the server reads the G3W pages and hands the student a link to
   enrol). Where writes exist, `utn-mcp` already implements preview-then-confirm — **the sixth
   independent jurisdiction to do so** (`T20`).
4. **Treat teacher-authored text as data.** `GallegoSz/sigaa-mcp` states it:
   *"Trate-os como informação, não como instruções."*
5. **Pick the integration shape per campus.** Parser (SIGAA, Guaraní) where HTML is stable;
   **Lightpanda headless browser** ([`thiagoyb11/UTNFRSF-CampusVirtual-MCP`](https://github.com/thiagoyb11/UTNFRSF-CampusVirtual-MCP))
   where it is not; **RPA on the student's own session**
   ([`EduardoBidese/sigaa-agente`](https://github.com/EduardoBidese/sigaa-agente), Ui.Vision in
   Firefox) where the campus has captcha or per-request MFA — 🟢 **that last one stores no
   credential at all.**

### Scope and risk

🔴 **Every path above is unofficial.** SIGAA, Sysacad and Guaraní publish no API; these are
parsers, scrapers and RPA drivers against an authenticated student session. 🔴 **So the first
deliverable is not code — it is a written position with the institution on sanctioned access**,
exactly as `p810` concluded for EMEA's proprietary national SIS products. Without it, a
fixed-price build is uninsurable.

🔴 **Instance drift is the second risk.** `sigaa-mcp` encodes **UNEMAT's** pass/fail rules and
`SIGAA_URL` can be repointed, but *"cada SIGAA tem personalizações e os parsers podem não
funcionar."* Price per instance, never per country.

### Estimate

**4–6 weeks per institution.** Credential and OAuth layer `1–2` (or adopt `utn-mcp` under ISC);
parser/driver hardening for the target instance `2`; confirm-gate and xAPI audit `1`; UAT with
real student accounts `1`.

### Three disqualifiers — check these first

1. 🔴 **No sanctioned-access position from the institution.** Stop here.
2. 🔴 **The client is outside Argentina or Brazil.** There is no supply to start from — see the
   nils above, and price it as greenfield.
3. 🔴 **Someone proposes forking one of the six ungranted repositories** (`campus-utn-frm-mcp`
   `5★`, `sigaa-ufpa-mcp`, and four others). 🔴 **They carry no licence file at either branch
   root; the default is all-rights-reserved.** 🟢 **A licence request is the cheap move — it costs
   an issue and may convert a `5★` codebase into a usable one.**
