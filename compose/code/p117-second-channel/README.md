---
industry: education
region: Global
updated: 2026-10-11
---

# `p117-second-channel` — ACTION A, and the channel that changed under us

**Pass 117, 2026-10-11.** ⏱️ **Fourth pass of this date** (p114 23:54→00:25, p115 01:13→01:25,
this one **02:45 → 03:0x UTC**).

🔵 **This pass has an axis it did not choose. p115 recorded `api.github.com` as refused and
every pass since p107 has worked around it. It answers now — through a different transport —
so the first authoritative read of the figures this shelf PUBLISHES became possible, and that
is worth more than the ninth refinement of a placement layer.**

## 🟢 `P117-A` — three transports, three outcomes, one API

🔵 **Probed live this pass, same host, same moment:**

| transport | result |
|---|---|
| `curl https://api.github.com/...` | 🔴 **403** at the CONNECT layer (`P798`'s ledger, unchanged) |
| `gh api repos/...` | 🔴 **403** — *"GitHub access to this repository is not enabled for this session"*, repo-scope gated |
| 🟢 **MCP relay (`search_repositories`)** | 🟢 **200, full API objects, arbitrary public repositories** |

🔴 **`curl` also still refuses `github.com` HTML (403), `codeload.github.com` (403).**
🟢 **`raw.githubusercontent.com` answers 200, as it did for p115.** 🟢 **`git` reads trees, as
it did for p115.**

🔵 **`P798`'s rule was "two tools, two mechanisms, same allowlist". The rule is now weaker and
more useful: a refusal is a property of the TRANSPORT, not of the host. A pass that records
"`api.github.com` is blocked" has recorded one transport's answer and should say which.**

🟡 **Caveats on the new channel, measured rather than assumed:**
- 🔴 **`user:` qualifier returns `total_count: 0`** for owners that exist (`user:openedx`,
  `user:frdel`). `org:` works, and repeated `org:` qualifiers OR together — which is how this
  pass read nine orgs in two calls.
- 🔴 **The index is not complete.** [`LAION-AI/Desktop_BUD-E`](https://github.com/LAION-AI/Desktop_BUD-E)
  is **absent** under two query forms (`Desktop_BUD-E in:name`, `org:LAION-AI BUD`) while
  `git ls-remote` reads it `rc=0`. **A search miss is not a 404** (`P117-G`).
- 🟡 The relay's compact mode omits `license`, so every licence below is read from the TREE.

## 🔴 `P117-B` — ACTION A: the remedy is near-empty, and the gap is not refuted

🔵 **p115 pre-registered it exactly: validate layer R's 34 unsettled rows against
`CODEOWNERS` / `.github/FUNDING.yml` / `AUTHORS`, and treat layer R as REFUTED if the second
channel contradicts it on ≥ 3 of 34.**

**594 requests (34 rows × 9 paths × 2 branches): 589 × `404`, 5 × `200`.**

| | |
|---|---|
| rows the channel REACHES | 🔴 **4 of 34 (12 %)** |
| rows it CORROBORATES | 🟡 **2** — `ls1intum/Artemis`, `numbas/Numbas` |
| rows it reaches but which place nothing | 🟡 **2** — a username, and two personal names |
| 🔴 **rows it CONTRADICTS** | 🟢 **0 of 34** |

🟢 **The refutation clause is NOT triggered: layer R survives its own pre-registered test.**
🔴 **It survives on 2 corroborations out of 34, so `Gap 405` stays OPEN and its substance —
"25/25 measured on 42 % of its own output" — is unchanged.** 🔵 **This is the second
pre-registered remedy in two passes to come back nearly empty (`Gap 403`'s yielded 12 of 193).
Two for two is a pattern worth naming: on this shelf, the cheap structural channels are
exhausted, and what is left is not reachable by adding another filename to a probe list.**

### 🟢 The two corroborations are worth more than their count, because of HOW they placed

🟢 **`ls1intum/Artemis` placed on a REVERSE-DNS JAVA PACKAGE PATH** —
`/src/main/java/de/tum/cit/aet/artemis/...` in `CODEOWNERS`. The leading label `de` is a
ccTLD, structurally, in a namespace convention that exists precisely to be globally unique.
🔵 **No pass has read this channel. It is not a URL, not a README and not metadata.**

🟢 **`numbas/Numbas` placed on a CONTRIBUTORS heading — `## For Newcastle University`** — an
institution the artefact names about itself, which is exactly what `P800` asks for.

## 🔴 `P117-C` — the headline: the one column this KB CARRIES instead of measuring is the one that rotted

🔵 **`agents/top.md` publishes a fourteen-row recommendation table whose own preamble reads
*"Licences carried from this page's prior passes; p113 changed none of them"*. p117 re-read all
fourteen from the tree.**

| | |
|---|---|
| rows whose published licence is CORRECT | 🔴 **5 of 14** |
| rows whose published licence is WRONG | 🔴 **9 of 14** |
| 🔴 **published PERMISSIVE, actually COPYLEFT** | 🔴 **4** |
| rows wrong but harmless (permissive ↔ permissive) | 🟡 3 |
| rows wrong by OMISSION (a second, stricter licence on content) | 🟡 2 |

🔴 **The four dangerous ones, each read from the licence file's title line:**

| row | published | 🔴 actually |
|---|---|---|
| [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🟢 MIT | 🔴 **AGPL-3.0** |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🟢 MIT | 🔴 **AGPL-3.0** |
| [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🟢 MIT | 🔴 **GPL-3.0** |
| [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | 🟢 MIT | 🔴 **GPL-3.0** |

🔴 **The table's published conclusion — *"Eleven of the fourteen are permissive (MIT /
Apache-2.0 / BSD-3) — a client can ship a closed derivative"* — is RETRACTED. Measured: eight
of fourteen are permissive for CODE, and two of those eight carry non-code content under CC
terms (one of them NON-COMMERCIAL).** 🔵 **For six of the fourteen rows the sentence was not a
rounding error; it was the opposite of the licence in the tree.**

🟡 **The two omissions matter commercially and are not footnotes:**
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) is MIT
for code, **CC BY 4.0** for prompts/settings and 🔴 **CC BY-NC-SA 4.0 for the annotated CLEAR
and PERSUADE 2.0 corpora** — the corpora are the part a client would want, and they are
non-commercial. [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) is MIT
for `harness/` + `test/` and CC BY 4.0 for the item bank and results.

## 🔴 `P117-D` — the same failure, once, on the foundations page

| row | published | 🔴 actually |
|---|---|---|
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟢 Apache-2.0 | 🔴 **AGPL-3.0** |

🔵 **This one is a REGRESSION with a date. The same file publishes `AGPL-3` for this row under
p110, p111, p112 and p93, and `Apache-2.0` under p114 and p115.** 🔴 **The KB had it right for
twenty passes and a licence column carried forward silently overwrote it.**
🟢 **Eight of the nine foundations are correct — the eight that were measured.**

## 🔴 `P117-E` — the star figures, read authoritatively for the first time

| row | this KB has published | 🟢 API, 2026-10-11 | error |
|---|---|---|---|
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🔴 "~9k★" (c2), "~12k★" (c3) | 🟢 **389** | 🔴 **31× overstated** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🔴 "~22k★" (c2), "~24k★" (c3) | 🟢 **41 100** | 🔴 **1.7× understated** |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | "~30k★" | 🟢 **29 775** | 🟢 right |
| [`moodle/moodle`](https://github.com/moodle/moodle) | — | 🟢 **7 473** | — |

🔵 **Both directions, from the same line of the same ledger. A figure being plausible is not a
figure being read, and the shelf's own rotation ledger had already flagged "pipeline-inflated"
star counts without being able to prove it. Now it is provable.**

## 🔴 `P117-F` — the agent tier, measured on size and licence together

| # | row | 🟢 stars | 🟢 licence (tree) |
|---|---|---|---|
| 1 | [`huggingface/transformers`](https://github.com/huggingface/transformers) | 167 302 | 🟢 Apache-2.0 |
| 2 | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | 76 867 | 🟢 MIT |
| 3 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 41 100 | 🟢 Apache-2.0 |
| 4 | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 29 775 | 🟢 Apache-2.0 |
| 5 | [`agent0ai/agent-zero`](https://github.com/agent0ai/agent-zero) ※ | 19 420 | 🟢 MIT |
| 6 | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 1 127 | 🔴 AGPL-3.0 |
| 7 | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | 1 040 | 🟢 MIT |
| 8 | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 389 | 🟢 MIT |
| 9 | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 108 | 🟢 BSD-3-Clause |
| 10 | [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 62 | 🔴 **no licence file** |
| 11 | [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) | 15 | 🟢 MIT |
| 12 | [`marc-shade/docsingest`](https://github.com/marc-shade/docsingest) | 6 | 🟢 MIT |
| 13 | [`eai6/ai-tutor`](https://github.com/eai6/ai-tutor) | 0 | 🟢 MIT |
| 14 | [`LAION-AI/Desktop_BUD-E`](https://github.com/LAION-AI/Desktop_BUD-E) | 🔴 search-absent | 🔴 **no licence file** |

🔵 **※ published by this KB as `frdel/agent-zero`; the API's canonical `full_name` is
`agent0ai/agent-zero` and `git ls-remote` returns the SAME head SHA for both.**

🔴 **Two of the fourteen commit NO LICENCE FILE AT ALL — Globant cannot build on them, and
"MIT" must never be inferred for them.** 🔴 **Five of fourteen are under 110 stars; three are
under 20.** 🟢 **The tier's top four are real and large; the bottom half is single-maintainer
work whose presence on a recommendation page needs a reason other than existing.**

## 🟡 `P117-G` — three addresses this shelf publishes are not canonical, and none is broken

🔵 **Verified by SHA equality, not by assumption — `git ls-remote` on both spellings:**

| published | canonical | evidence |
|---|---|---|
| `frdel/agent-zero` | `agent0ai/agent-zero` | same head `983fc50a…` — a rename redirect |
| `openedx/edx-platform` | `openedx/openedx-platform` | same head `e6d65a85…` — a rename |
| `dspace/dspace` | `DSpace/DSpace` | same head `9d355068…` — case only |
| `apereo-…/larissa` | `Apereo-…/Larissa` | API `full_name`; **fixed, `P117-ACTION-B`** |

🟢 **A rename is not a break: all four resolve today.** 🔴 **They are still wrong to publish,
for the reason `p443-canonical-spelling` exists — one artefact under two spellings is two
entities to any compiler that keys on the string.**

## 🔴 `P117-H` — a foundation row that says, in its own description, that it is unsupported

🔴 [`atutor/ATutor`](https://github.com/atutor/ATutor), 180★, published on `repos/foundations.md`.
Its API description opens: **"NO LONGER USER LEVEL SUPPORTED. CONTRIBUTING DEVELOPERS
INTERESTED IN MAINTAINING ATUTOR, SHOULD REQUEST COLLABORATOR ACCESS."** 🔴 **It also commits
no licence file** (checked `LICENSE`, `LICENCE`, `COPYING`, `COPYING.txt`, `LICENSE.md`,
`docs/LICENSE`, `README.md` on `master`). 🔵 **Last push 2026-09-09, so it is not dead — it is
explicitly unmaintained, which is a different and more useful fact.**

## 🔴 `P117-K` — this instrument's own fault, found before it published

🔴 **v1 of the licence classifier matched the PHRASE `"GNU Affero General Public License"`.
GPL-3 section 13 is titled *"Remote Network Interaction; Use with the GNU Affero General Public
License"* — so the GPL-3 text contains the AGPL's name, and v1 reported
`OtterDen-Lab/Autograder`, `ahmedEid1/lumen` and `ILIAS-eLearning/ILIAS` as AGPL-3.0 when all
three are GPL-3.0.**

🟡 **A second fault, caught in the same check: I inferred licence identity from FILE SIZE
(~34.5 kB = AGPL, ~35.1 kB = GPL). It is wrong — `openedx/edx-ora2` is 35 135 B and AGPL —
and had I published it, this pass would have replaced one wrong licence with another.**

🟢 **FIXED: `title.sh` reads the licence file's TITLE LINE — the first non-blank line that is
not a copyright, a version or a preamble marker — and every copyleft verdict above was
re-derived from it.** 🔵 **This is `P471`'s shape a third time: a probe that matched a
CROSS-REFERENCE rather than a GRANT. The rule to hand on: a licence is identified by its title,
never by a phrase that one licence may use to name another.**

## 🟢 Pre-registered for p117, each with a refutation clause

🟢 **`ACTION C` — layer P, the reverse-DNS package namespace.** Census `src/main/java/<cc>/...`
and equivalents (`android`, `kotlin`, `gradle` group ids, `pom.xml` `<groupId>`) over all 296
addresses. The leading label is a ccTLD by convention. 🔴 **Refuted if layer P places fewer
than 5 rows beyond layers 0 and R, or contradicts a settled org on ≥ 2.**

🟢 **`ACTION D` — layer D, the API `description` field, newly readable (`P117-A`).**
[`eai6/ai-tutor`](https://github.com/eai6/ai-tutor)'s description reads *"…for secondary schools
in **Seychelles**"* — a country token in a structured field that layers 0, 1 and R all missed.
🔴 **Refuted if layer D places fewer than 10 of 296, or if ≥ 2 of its placements name a country
the repository only SERVES rather than is built in — which is the `P800` trap this layer is
most exposed to, since "schools in X" is a market, not an affiliation.**

🟢 **`ACTION E` — re-read every licence this KB publishes, not just the two tables p117
reached.** `P117-C` measured 14 rows and found 9 wrong; `verticals/solutions.md`'s rows were
spot-checked and were RIGHT (`PageLM`'s custom licence, `advisingapp`'s Elastic-2.0 and
`classroomio`'s AGPL-3.0 are all correctly published). 🔵 **The difference between the two
pages is that one measured and one carried.** 🔴 **Refuted as unnecessary if a full sweep finds
fewer than 3 further wrong licences.**

## Files

| file | what it is |
|---|---|
| `fetch.sh` | ACTION A's probe; keeps every byte in `streams/` |
| `title.sh` | the licence reader, title-line based (`P117-K`) |
| `licence.sh` | v1, kept **deliberately** as the fixture for `P117-K`'s fault |
| `figures.2026-10-11.tsv` | 37 rows: published vs verified, stars and licences |
| `actionA.2026-10-11.tsv` | ACTION A's 4 reached rows and the 30 it cannot see |
| `streams/` | the 5 files the second channel returned, verbatim |
| `slugs34.txt` / `shelf-rows.txt` / `p113rows.txt` | the exact inputs, so this is re-runnable |
