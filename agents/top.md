---
industry: education
region: Global
updated: 2026-10-28
---

# Education AI agents — build-on-able shelf

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file to its
specified table shape; `p491` **extends** it and does not rewrite it. The p490 tables below stand
unchanged — every p490 SHA was re-resolved this pass and came back **identical**
(`DeepTutor a31d82624c27`, `mentingo e137ca47cbec`, `oppia bc73ecf9cf71`), so there is no upstream
drift to reconcile. The 57 pre-p490 pass-sections remain in
[`archive/2026-10-27-p490-pre-rewrite/top.md`](../archive/2026-10-27-p490-pre-rewrite/top.md).

**New this pass:** an **evaluation-instruments** table (below), which changes the standing claim
that no education-AI evaluation instrument exists — they exist, and **none of them carries a
license**. Evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

## How every cell here was verified

| step | channel | result |
|---|---|---|
| repo exists + default branch | `git ls-remote --symref` | works; authoritative |
| license text | `raw.githubusercontent.com/<repo>/<SHA>/<path>` **at the pinned SHA** | works |
| stars + sidebar license | `github.com` repo page via page fetch | works |
| ~~existence~~ | `curl -sI https://github.com/<repo>` | **403 on every repo — do not use** |
| stars for arbitrary repos | `api.github.com` | **403, per-repository authorisation only** |

License family is anchored on the **first 200 bytes (the title block)**, never on a body scan —
see the reader defect recorded below. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## Permissive — Globant can build on these

Nine rows, MIT / Apache-2.0, each license read from bytes at the SHA shown. 🔵 **`p492` added no row
here** — the one new permissive education agent it found has **0★** and is listed under *reference
designs* below, deliberately outside this shelf.

| Agent | Repo | License | ★ | SHA read | What it does |
|---|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | **45,900** | `a31d82624c27` | Lifelong personalised tutoring; graph-enhanced RAG over course material. Largest education-AI repo on GitHub. 🟢 **`p492`: HEAD unchanged for a third pass; `v1.6.15` released `2026-10-19`.** Its own repo page links a design paper at `arxiv.org/abs/2604.26962` (upstream News item dated `2026-04-10`). 🔵 **Unverified — `arxiv.org` does not resolve from this session's network**, so this is an upstream-asserted identifier, not a read. **See license caveat below.** |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | 30,100 | `96f33faaf028` | Minimal code-writing agent loop. Not education-specific; the usual substrate for a custom tutor agent. |
| educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | **387** | `38adb1e9459d` | Python package generating educational content (MCQs, lesson plans, flashcards) from an LLM. |
| Skill-Anything | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | 344 | `3cdc1c1f11dc` | Any source (PDF, video, web, audio) → interactive package with quizzes, flashcards, spaced repetition. |
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 309 | **`830bc2ef8389`** | MCP server over Canvas LMS. 🔴 **`p492`: HEAD drifted from `32e5d1ca0175`; licence byte-identical at both SHAs (1 071 B, `sha1 491fb891a4cf`) so the drift is code-only. `v1.16.0` lists FOUR advisories, not one** — `GHSA-7mj9-4mcg-hvhv` (Canvas token handling), `GHSA-7pp5-29mw-9jq3` (local code sandbox), `GHSA-hmr8-mvr2-mvw5` (file content fencing), `GHSA-qf6c-jv93-38gv` (Windows download permissions). Tool count self-inconsistent upstream (description 102, README 128) — **stop quoting a number**. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | **274** | `e24c8456e5f7` | Intelligent tutoring system with Bayesian Knowledge Tracing; ReactJS + Firebase. UC Berkeley CAHLR. |
| KSoR | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | 232 | `b50f28926fae` | SDK for governed, authoritative knowledge systems for humans and agents. Names education institutions as its target. |
| mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | 100 | `e137ca47cbec` | Self-hostable LMS with AI mentoring and role-play. Tenant isolation enforced in Postgres RLS, not app code. |
| AI Agents for Beginners | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT | 78,000 | `dd0f080d07d2` | 18-lesson agent course. **A curriculum, not a deployable agent** — listed because it is the most-starred thing in this space and is routinely miscatalogued as a product. |

## Copyleft — usable, but not for a hosted commercial derivative

| Agent | Repo | License | ★ | SHA read | Constraint |
|---|---|---|---|---|---|
| ChatTutor | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | **AGPL-3.0** | 1,300 | `7d9e9052bc5a` | Visual/interactive AI tutor, whiteboard + math canvas. AGPL reaches across the network: hosting it for a client triggers source obligations. |
| tutor-gpt | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | **GPL-3.0** | 932 | `5c2f92416c04` | Theory-of-Mind tutoring agent. GPL, not permissive — several public listicles call this one "open source" without naming the family. |

## Corrections this pass — figures this KB published that were wrong

Each confirmed against two independent channels (license bytes at a pinned SHA, and the
repository's own sidebar).

| row | this KB published | measured `p490` | error |
|---|---|---|---|
| `satvik314/educhain` | `~12,000★` since cycle 2 | **387★** | **31×** overstated |
| `CAHLR/OATutor` | `~1,300★` (cycle 2), `~1,500★` (cycle 3) | **274★** | ~5× overstated |
| `frappe/lms` | `MIT` (and still claimed MIT by current web sources) | **AGPL-3.0** | wrong family; permissive→network copyleft |
| `oat-sa/tao-core` | `GPL-2.0-or-later` | **GPL-2.0** per bytes *and* sidebar; the `or-later` election is **not** readable from the payload | overclaimed |
| `RosarioSIS/RosarioSIS` | cited as a path | **404** — the repo is [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | dead URL |
| `microsoft/autogen` | `MIT` | root `LICENSE` is **CC BY 4.0**; the code grant is **MIT at `LICENSE-CODE`** | right answer, reached without reading |

### The AutoGen split, stated plainly

`microsoft/autogen` serves **two** grants and a root-`LICENSE` reader gets the wrong one:

- `LICENSE` → `Attribution 4.0 International` (Creative Commons, 18,650 B) — the docs/content grant.
- `LICENSE-CODE` → `MIT License` — **the code grant.**

Any sweep on this KB that probes only `LICENSE` will file Microsoft agent repos as Creative
Commons. That is a false negative that removes a usable MIT row from the shelf.

### A defect in this pass's own reader, recorded rather than quietly fixed

The first reader run this pass graded [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) as
`LGPL-2.0`. It is `GPL-2.0`. Cause: the reader scanned the first 3,000 bytes, and **the GPLv2
preamble names the Lesser GPL** ("…the GNU Lesser General Public License instead…"), so a
body scan matches `LGPL` before it reaches the real family. The reader was re-anchored on the
200-byte title block and all 28 rows re-read; `tao-core` and `rosariosis` moved to `GPL-2.0`,
and the two genuine LGPL rows (`bigbluebutton` 7,652 B, `openeducat_erp` 8,241 B) held.

**Rule for later passes: anchor the family on the title block. A GNU preamble cross-references
the sibling licenses, so any body scan is a family false-positive generator.**

## The DeepTutor license caveat — carried forward, still true

`HKUDS/DeepTutor` is 88% of this shelf's star mass and its Apache-2.0 payload (11,408 B) is
**not** canonical Apache-2.0 (10,015 B operative span). Three function-word substitutions sit in
the operative body:

| § | canonical | DeepTutor |
|---|---|---|
| §1 *Contribution* | "submitted to Licensor" | "submitted to **the** Licensor" |
| §1 *Contributor* | "received by Licensor" | "received by **the** Licensor" |
| §4(d) NOTICE | "excluding **those** notices" | "excluding **any** notices" |

**Legal effect: nil** — "the Licensor" is "Licensor"; both NOTICE phrasings are the same
restrictive clause. No hunk touches the grant, patent or disclaimer sections.
**Supply-chain signal: not nil** — the appendix is replaced with an instruction to apply an
"Alarm" trademark header unrelated to the licensor (Data Intelligence Lab, University of Hong
Kong), and the same edited payload appears byte-identically in the derivative
[`3yangyang9/DeepTutor-AILearning`](https://github.com/3yangyang9/DeepTutor-AILearning) (136★),
which is how a copied license travels. Treat it as a provenance flag, not a license risk.

## Evaluation instruments — they exist, and none of them is licensed

`p490` recorded "no open-source education-AI evaluation harness above 60★ exists" and treated the
tier as empty. Measured this pass, the finding is **sharper and worse**: the instruments exist and
are academically serious, but **not one of them ships a license grant**, so none can be used in
client work at all.

| Instrument | Repo | Grant at SHA | ★ | What it measures |
|---|---|---|---|---|
| MathTutorBench | [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 🔴 **no license file** (`6faed173ec2b`) | 45 | Open-ended *pedagogical* capability of LLM tutors — 3 teacher skills, 7 tasks. EMNLP 2025 Oral (arXiv 2502.18940). |
| TutorCaseBench | [kixlab/TutorCaseBench](https://github.com/kixlab/TutorCaseBench) | 🔴 **no license file** (`6b9ac34262c7`) | 0 | Tutor behaviour with students showing challenging behaviours; 923 dialogues, 5 challenge types. KAIST. |
| lm-evaluation-harness | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT**, 1,066 B (`d6de81643928`) | 14,300 | Not education-specific — the general runtime. **The only permissive piece in this tier.** |

🔴 **MathTutorBench's own README contradicts itself on the license**: the badge reads
`License: CC BY 4.0` and the closing line of the same file says
*"Creative Commons Attribution-**ShareAlike** 4.0"*. The sidebar shows no license at all. Those
are two different licenses, **one of them copyleft**, and neither is a software grant — Creative
Commons licenses are content licenses and CC itself advises against using them for code.

**Consequence for an engagement:** the benchmark *tasks* are publishable research you may read and
reimplement from the papers; the **repository code and data cannot be taken**. No grant means no
rights, not permissive-by-default. So the harness remains a **build** — see
[`compose/patterns.md`](../compose/patterns.md) `P491-1`, which rebases that build on
`lm-evaluation-harness` (MIT) instead of on nothing.

## Declared gaps — searched, nothing found

Stating these because silence looks identical to coverage.

- **No permissive education-specific agent above 1,000★ other than DeepTutor.** Everything
  between 387★ and 30,000★ on this shelf is either general-purpose (smolagents) or copyleft
  (ChatTutor, tutor-gpt). The permissive education tier is genuinely small.
- **No LATAM-origin or Africa-origin education agent reached this shelf's star floor.** Searched
  globally and per region; the regional supply is in deployments and national programmes
  (see `intel/market.md`), not in starred repositories.
- **No *usable* open-source education-AI evaluation harness exists — but the instruments do.**
  Restated this pass: `mathtutorbench` (45★) and `TutorCaseBench` (0★) are real and serious, and
  **neither carries a license grant**, which is a harder blocker than scarcity. A star-ordered
  sweep is still structurally blind to this tier, and a license-ordered sweep finds nothing in it
  either. See the table above.
- ~~**Commit recency is not on this table.**~~ 🟢 **Partly closed `p492` — a *release* date is
  readable even though a commit date is not.** The page-fetch channel does expose tagged releases
  with dates: `canvas-mcp v1.16.0` (Oct 2026), `DeepTutor v1.6.15` (`2026-10-19`),
  `education-agent-skills v3.1.0` (`2026-10-22`), `openmeetings v9.1.0`. That is a **real liveness
  signal** for any repo that tags releases, and this KB had been declaring it unavailable.
  **Remaining limit:** repos that do not tag releases still have no maintenance signal, and
  `api.github.com` is still 403 for unattached repos. Rows still carry a pinned SHA, which proves
  content; a release date now proves *liveness* where one exists.


## 🆕 `p492` — `2026-10-28` — reference designs, and why they are not shelf rows

Full reads and channel notes:
[`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv);
narrative in [`agents/trending.md`](trending.md).

**Three corrections landed in the tables above, not here:** `canvas-mcp`'s drifted SHA and its
**four** advisories, `DeepTutor`'s star count plus its previously-unrecorded arXiv paper, and the
partial closure of the commit-recency gap via release dates.

### Reference designs — read these, do not depend on them

A repo with no community is not supply. It can still be the clearest statement of an architecture,
and this KB has been arguing for the architecture below without ever pointing at code.

| repo | licence @ SHA | ★ | read it for |
|---|---|---|---|
| [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | **MIT**, 1 071 B, `sha1 2a558a4b5980` (`5511bf6dc707`) | 🔴 **0** (13 commits, one author) | **Rubric totals computed in code, never by the model** — per-criterion structured output validated against the rubric, arithmetic in Python. Plus an **answer-leak guard** (a hint that reveals the answer is regenerated under a stricter instruction, and replaced by a safe hint if it still leaks) and **session memory as an explicit LangGraph thread** (in-memory or SQLite). FastAPI + LangGraph + Pydantic; CI on Python 3.11–3.14; deterministic fake model for offline tests. |

🟢 **Why this is worth a row in a KB that refuses to pad.** Point 1 is the **human-oversight shape
the EU AI Act requires of a *provider*** of a high-risk assessment system — and
[`intel/market.md`](../intel/market.md) establishes that *for a Globant-built education AI system,
Globant is the provider*. "Do not let the model do the arithmetic" has been this KB's advice for
several passes; this is the first MIT implementation of it we can hand an engineer.

🔴 **Do not propose it as a dependency.** Zero stars, 13 commits, one author, no security process.
It is a **1 071-byte MIT grant over a design worth copying**, which is the entire claim.

### Not an education agent, recorded so it stops resurfacing

| repo | licence @ SHA | ★ | why it is excluded |
|---|---|---|---|
| [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT**, 1 082 B, `sha1 b3428e1f52c0` (`2be1800d141e`) | **67,600** | 60+ annotated PyTorch paper implementations. **CS-education teaching material, not a deployable agent** — the same miscatalogue this shelf already flags for `microsoft/ai-agents-for-beginners` (78,000★). It would top this table on stars and teach a client nothing about tutoring. 🔵 Its licence file is lowercase **`license`**; probes trying only `LICENSE`/`LICENSE.md` would report "no licence" on an MIT repo. **Add lowercase `license` to every future probe list.** |

### 🔵 Gap restated, now with a reason rather than a silence

**Learning Commons' "Claude for Teachers" agent skills** (Lesson Plan Generation, Lesson
Differentiation; launched July 2026, publicly described as open-source) are **not listed** because
their licence could not be read: no repository resolved under the obvious paths, and
`learningcommons.org` **does not resolve from this session's network**. An unverified licence is not
a finding. Recorded as a lead for the next pass.
