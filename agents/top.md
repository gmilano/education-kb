---
industry: education
region: Global
updated: 2026-10-27
---

# Education AI agents — build-on-able shelf

**Pass `p490` — reads of 2026-10-27.** This file was rewritten this pass. The 57 prior
pass-sections it carried are preserved in
[`archive/2026-10-27-p490-pre-rewrite/top.md`](../archive/2026-10-27-p490-pre-rewrite/top.md).

**Why the rewrite:** this file is specified as *the agents table*. It had grown to 7,510 lines
of pass-to-pass audit narrative with no consumable table anywhere in it. An engagement lead
could not read a license off it. The table is below.

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

Nine rows, MIT / Apache-2.0, each license read from bytes at the SHA shown.

| Agent | Repo | License | ★ | SHA read | What it does |
|---|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 45,800 | `a31d82624c27` | Lifelong personalised tutoring; graph-enhanced RAG over course material. Largest education-AI repo on GitHub. **See license caveat below.** |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | 30,100 | `96f33faaf028` | Minimal code-writing agent loop. Not education-specific; the usual substrate for a custom tutor agent. |
| educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | **387** | `38adb1e9459d` | Python package generating educational content (MCQs, lesson plans, flashcards) from an LLM. |
| Skill-Anything | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | 344 | `3cdc1c1f11dc` | Any source (PDF, video, web, audio) → interactive package with quizzes, flashcards, spaced repetition. |
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 309 | `32e5d1ca0175` | MCP server over Canvas LMS; self-described as up to 102 tools + 8 agent skills. Ships a published advisory (GHSA-hmr8-mvr2-mvw5) naming its prompt-injection path. |
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

## Declared gaps — searched, nothing found

Stating these because silence looks identical to coverage.

- **No permissive education-specific agent above 1,000★ other than DeepTutor.** Everything
  between 387★ and 30,000★ on this shelf is either general-purpose (smolagents) or copyleft
  (ChatTutor, tutor-gpt). The permissive education tier is genuinely small.
- **No LATAM-origin or Africa-origin education agent reached this shelf's star floor.** Searched
  globally and per region; the regional supply is in deployments and national programmes
  (see `intel/market.md`), not in starred repositories.
- **No open-source education-AI evaluation harness above 60★ exists.** Every instrument found
  sits below that floor, so any star-ordered sweep is structurally blind to the whole tier.
- **Commit recency is not on this table.** The page-fetch channel does not expose per-file commit
  dates, and `api.github.com` is 403 for arbitrary repos. Rows carry a pinned SHA instead, which
  is a stronger claim than a date.
