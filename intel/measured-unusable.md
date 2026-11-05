---
industry: education
region: Global
updated: 2026-11-05
---

## 🆕 `p662` — `2026-11-05` — **🔴 A CURRENTLY PUBLISHED LMS COMPARISON TABLE PUTS `LearnHouse` IN THE "MIT/Apache … maximum flexibility" COLUMN. IT IS `AGPL-3.0`, AND THIS BASE HAS HELD THAT VERDICT SINCE `p11`.**

🔵 **Why this page and not `verticals/solutions.md`.** `learnhouse/learnhouse` is real, live and maintained — `2,448★`, pushed `2026-11-05`. It is unusable *for the model this base recommends*: start from something that works and add a proprietary agent layer on top. `AGPL-3.0`'s network-use clause reaches a hosted deployment, so a client-branded fork carries a source-disclosure obligation. That is a licence fact, not a quality judgement.

### 🔴 `662-G` — the claim, and the four channels it fails on

The claim, from an open-source-LMS comparison returned by the global verticals leg: *"MIT/Apache (LearnHouse, OpenOlat) offer maximum flexibility."*

| Channel | Reading `2026-11-05` |
| --- | --- |
| `git ls-remote --symref` | 🟢 resolves — **real default branch is `dev`**, not `main`. A licence check run against `/main/` by habit is checking a branch that is not the project's head |
| grant payload at the **resolved** default ref (`dev`) | 🔴 `LICENSE` · **`34,523 B`** · `sha256₁₂ 8486a10c4393` · *"GNU AFFERO GENERAL PUBLIC LICENSE / Version 3, 19 November 2007"* |
| grant payload at `main` | 🔴 identical bytes, identical digest — **the claim does not survive on either ref** |
| `gh api search/repositories` | 🔴 `spdx = AGPL-3.0` · **`2,448★`** · pushed **`2026-11-05`** |

🟡 **The base's own verdict is HELD and is not claimed as new.** `evidence/address-ledger.tsv` has carried `learnhouse/learnhouse → AGPL-3.0` since `p11`, and both append-only logs name it. What is new at `p662` is that a **current, confidently worded, publicly indexed** source contradicts it.

🔵 **The generalisable shape.** This base's verification discipline — resolve the default ref, byte-read the grant, state the digest — is aimed at its own rows. `662-G` is the first instance of a mandated leg returning a published licence table that is wrong in the **commercially dangerous direction**: permissive-when-actually-copyleft. The leg's value here is adversarial, like `661-F`'s TEQSA reproduction: not supply, but a false claim in circulation that a client or a colleague may arrive carrying, already believing it.

🟢 **The same table's `OpenOlat` claim is substantively correct** — sections 1–9 of its grant are byte-identical to canonical Apache-2.0, re-verified at `p662`. One entry being right is what makes the other entry dangerous.

## 🆕 `p651` — `2026-11-04` — **🔴 A MANDATED WEB LEG PRODUCED ITS FIRST USEFUL NEGATIVE: A DATED REGULATORY CLAIM TESTED, FALSIFIED, AND KEPT OUT OF `intel/market.md`. PLUS `6` LICENCE-NIL SUPPLY ROWS, `1` BESPOKE SPANISH GRANT, `1` SHAREALIKE AT `949★`, AND `1` TRUNCATED `MIT` PAYLOAD WITH ITS LIABILITY CAP DELETED.**

🔵 **Why this entry matters to the leg-scoring argument.** Fifteen consecutive passes have scored the mandated web legs as effectively nil, on the grounds that the facts they return are already held at HEAD. `p651` records a different kind of value: a leg returned a **wrong** fact, plausible and specific, and the cost of testing it was one search. Had it been adopted, `intel/market.md` would now publish three false statutory deadlines for a US state. **A leg that stops a wrong fact is not nil, and the nil-scoring convention has no column for it.** Recommend the scorer gain one.

### 🔴 `651-A` — North Carolina `SL 2026-41`: a plausible, specific, dated claim that does not survive one check

The North America regulation leg returned, with confidence: *"North Carolina has the most concrete timeline I found: a state model policy due December 31, 2026, local policies due June 30, 2027, and teacher training due June 30, 2028. Its Session Law 2026-41 requires AI-literacy standards along with those deadlines."*

| channel | reading `2026-11-04` |
| --- | --- |
| `SL 2026-41` identity | 🔴 **the 2026 Appropriations Act (Senate Bill 257)** — a budget act, per the General Assembly's own summary pages |
| AI content actually in `SL 2026-41` | 🟡 Sec. 7.50 amends the **AI Pilot Program** created in the 2023 Appropriations Act, requiring DPI to make a directed grant to **Alamance-Burlington Schools**; Sec. 7.39 carries further AI provisions not detailed in the available excerpt |
| AI-literacy content standards | 🔴 attributed by the legislature's summary to a **different session law — `2026-61` (House Bill 268)** — requiring the State Board to adopt AI content standards in the computer-science standard course of study |
| the "model policy" | 🔴 appears in **bill drafts only** (DPI *shall develop* a model AI policy; local boards *shall adopt* a policy). Carolina Public Press reports it as pending legislation, not enacted law |
| the three dates (`2026-12-31`, `2027-06-30`, `2028-06-30`) | 🔴 **not located in any enacted instrument.** The nearest dated item found is `SB 981`'s proposed AI in Education Task Force reporting by `2028-03-15` — also a proposal |
| 🟡 metadata anomaly worth recording | the General Assembly's own summary pages label `SL 2026-41` under **"Session Year 2024"**, which conflicts with its 2026 designation and is a trap for anyone verifying by URL path |

🔴 **Disposition: NOT PUBLISHED.** `intel/market.md`'s North America block names the claim, states that it does not verify, and points here. The enacted North Carolina facts that *did* survive — the Alamance-Burlington directed grant, and AI content standards under `2026-61` — are too thin to carry an opportunity and are not promoted either.

🔵 **The generalisable shape, and it is not "secondary sources are unreliable".** The leg's error was **attribution, not invention**: every component of the claim exists somewhere in North Carolina's 2025–26 session, and the error was binding them to one session law and presenting proposals as enacted. 🔴 That is the hardest class of regulatory error to catch, because the claim is *checkable and nearly right* — and it is the class most likely to reach a client slide, since a statute number reads as a citation. **Rule: a dated statutory obligation enters this base only against the instrument's own text or its legislature's summary of that instrument, never against a roundup that names the number.** Three further dated claims adopted this pass (Korea `2026-01-22`, Vietnam `2026-03-01`, India `2026-02-20`) rest on legal-practice sources that cite the statute directly and agree with one another, and are flagged in `intel/trends.md` as unverified against primary text.

### 🔴 `651-B` — six supply rows carrying no grant at all, two of them squarely on this base's declared gap

Probed `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENSE.TXT`, `COPYING`, `COPYING.txt`, `LICENCE` and `license` on each repository's **real** default branch (resolved by `ls-remote --symref`, per this base's standing rule):

| repo | stars | what it is | disposition |
| --- | --- | --- | --- |
| [`mthatipamula/educational-assessment-ai-agent-platform`](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | — | K-12 assessment: standards-aligned item authoring with RAG and self-review, rubric scoring with human review, sandboxed code grading, persistent-memory tutor | 🔴 **no grant.** The closest match this base has ever found to its own declared assessment gap |
| [`virtualryder/edu-ai-agents`](https://github.com/virtualryder/edu-ai-agents) | 4 | 8 governed Bedrock workflows, FERPA/COPPA/IDEA-504/ADA-aligned | 🔴 grant present but defective — see `651-D` |
| [`luffycodes/Tutorbot-Spock`](https://github.com/luffycodes/Tutorbot-Spock) | 56 | learning-science-grounded tutoring chatbot, with a physics variant | 🔴 **no grant** |
| [`minicoohei/ai-agent-camp`](https://github.com/minicoohei/ai-agent-camp) | 347 | non-engineer AI-agent training curriculum | 🔴 **no grant**, and out of scope anyway (developer upskilling, not education-sector software) |
| [`Micel357/Edu-mentor-AI`](https://github.com/Micel357/Edu-mentor-AI) | — | Portuguese-language multi-agent pedagogical system — **LATAM-placed on documentary evidence**: Residência Tecnológica at Porto Digital, Recife, Accenture-mentored, named in its own README | 🔴 **no grant** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 349 | PHP/MySQL student information system | 🟢 **FALSE POSITIVE — see `651-C`** |

🔴 **The finding that changes a gap's category.** This base has recorded "no permissive assessment or grading agent" for several passes and treated it as **absent supply**. It is not: the supply exists and is **unlicensed**. That is a different problem with a cheaper fix — one upstream commit adding a licence file moves either the `mthatipamula` platform or the `edu-ai-agents` assessment workflow onto the shelf. 🔵 Worth an actual approach to the maintainers rather than another pass of searching.

### 🟢 `651-C` — the root-filename probe called a `349★` platform licence-nil, and it was wrong

`OS4ED/openSIS-Classic` returned `404` on **fifteen** root filenames and its repository page names no licence in the sidebar. Under this base's probe it is licence-nil. It is not:

| channel | reading |
| --- | --- |
| 15 root filenames × `master` | 🔴 all `404` |
| repository page sidebar | 🔴 no licence named |
| 🟢 README `## License` section | 🟢 *"openSIS is an Open Source Project licensed under the GNU General Public License, the full license can be found [here]"* — linking **`docs/License.txt`** |
| 🟢 `docs/License.txt` | 🟢 serves `GNU GENERAL PUBLIC LICENSE / Version 2, June 1991`, BOM-prefixed |

🔵 **This is `p288`'s `gate-readme-channel` arriving from the opposite direction.** That gate exists because a README-only grant *claim* is not no channel. Here the README does not merely claim — it **resolves**, to a real payload at a non-root path. 🔴 The probe's filename set is the defect: it enumerates root names and never follows the README's own link. `609-I` is the inverse case (README grants MIT, links a `LICENSE` that does not exist), and the two together specify the correct procedure: **read the README's licence link and fetch what it points at, then judge.** A probe that stops at root filenames mis-calls both directions — it called `openSIS` unlicensed when it is GPL-2.0, and would have called `609-I`'s `AIM-SCU/GRADE` MIT had the link resolved to anything.

🟢 **Registered as `ACTION 651-C`:** extend the grant probe with a README-link-resolution arm before any row is recorded licence-nil. Cost is one extra fetch on rows that would otherwise be rejected.

### 🔴 `651-D` — `virtualryder/edu-ai-agents`: an `MIT`-shaped payload with the liability cap deleted

`832 B` at `LICENSE`, branch `main`, byte-read in full this pass.

| paragraph | status |
| --- | --- |
| holder line (`Copyright (c) 2026 David Ryder`) | 🟢 present |
| permission grant ("to deal in the Software without restriction …") | 🟢 **verbatim MIT** |
| notice-retention clause | 🟢 **verbatim MIT** |
| warranty disclaimer | 🟡 **truncated** — `THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.` then **stops**, where MIT continues into the specific warranties |
| 🔴 limitation of liability | 🔴 **ABSENT.** `IN NO EVENT SHALL THE AUTHORS … BE LIABLE` appears **nowhere in the file** |
| in its place | 🔴 a bespoke sentence: *"This accelerator is decision-support tooling, not a validated student-information system, certified accessibility product, or autonomous decision-maker."* |

🔴 **Why this is a new class and not `p649`'s presentation noise.** `649-R1` and `647-E` concern payloads that are byte-identical to canonical except for a terminating newline — **presentation**. This payload's divergence is **substantive and asymmetric**: it keeps every clause that benefits the licensee and removes the clause that protects the licensor. Whatever the author intended, a grant that confers broad rights and then omits its own liability cap is not MIT, must not be filed as MIT, and should not be accepted on a client's behalf without counsel. 🔵 Note the direction of the hazard: this is the one deviation class where the *licensee* is advantaged on the face of the text, which is exactly why nobody downstream has an incentive to notice it.

🔵 **And a measurement note:** at `832 B` against MIT's `~1,070 B`, the residual is `≈ −240` — far outside the `±1` band `p646`'s predictor treats as presentation. The predictor would have flagged this correctly **as a body anomaly**, which is `647-E`'s positive-sign discriminator working as specified, on a real repository, for the first time.

### 🔴 `651-E` — `949★` and ShareAlike: the week's largest novel find, excluded on terms

[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) — 165 skills across 20 domains in Agent Skills format, plus an MCP server exposing 157 tools and 165 prompts; `v3.1.0` retired the library-operated public MCP service in favour of self-hosting. **949 ★ / 130 forks** — higher adoption than six of the ten rows on `agents/top.md`.

| channel | reading |
| --- | --- |
| grant payload (`LICENSE`, `main`) | **`1,230 B`**, title `Creative Commons Attribution-ShareAlike 4.0 International` |
| repository page sidebar | names no licence |
| README licence section and badge | **CC BY-SA 4.0** for skills, documentation, examples and curriculum |

🔴 **Disposition: NOT PROMOTED to `agents/top.md`, and the reason is not quality.** CC BY-SA 4.0 is **ShareAlike**: a derivative skill library must itself be CC BY-SA, which forecloses folding these skills into a proprietary deliverable — the test this base applies to every row. It is also **content and prompts, not software**, so the MIT/Apache framing does not transfer: there is no patent grant and no warranty structure to reason about. 🟢 It is fully usable *as-is with attribution*, which is worth saying plainly rather than burying, and it is recorded on `agents/top.md`'s not-filed table with that distinction.

🔵 **Pattern across `651-E` and `646-H`:** the highest-starred novel candidate in a window has now twice been unusable for a reason a star-ranked read cannot see. `646-H` found a screen-brightness daemon topping an education topic; `651-E` finds a genuine, excellent education asset on terms that fail the base's licence test. **Rank by adoption, decide by grant** — and never by adoption alone.

### 🟡 `651-F` — a bespoke Spanish-language grant, recorded so "free" is not read as "permissive"

[`jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada`](https://github.com/jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada) — Spanish-language agents-and-skills environment for teachers (activity preparation, explanation adaptation, tutoring organisation).

| channel | reading |
| --- | --- |
| grant file | `LICENSE.md`, **`1,262 B`** |
| title | 🔴 **`# Licencia Comunitaria de Uso Profesional`** — a custom community licence authored by the maintainer |
| OSI status | 🔴 not an OSI licence; no SPDX identifier applies |

🔴 **Disposition: REJECTED on terms.** Recorded for two reasons. First, so a later pass does not re-spend the search. Second, and more useful: the project presents as **free to use**, and this base's filter is **permissive**, which is a different property. 🔵 A bespoke grant in a language other than English is the shape most likely to be waved through by a reviewer skimming for the word "MIT" — and it is the second non-English-titled payload this base has had to classify by reading rather than by matching.

## 🆕 `p609` — `2026-11-02` — `4` dispositions, and the first **dangling** grant this base has recorded

🔵 **`598-A`'s rule earned its keep this pass.** It requires that a row is only called *"no grant"*
once its **build manifest** has been read as well as its grant filenames. Applied to this pass's one
apparent no-grant row, it did not confirm the absence — it **reclassified** it into a category this
base has not held before.

### 🔴 `609-I` — `AIM-SCU/GRADE`: a README that grants MIT and links a file that does not exist

[`AIM-SCU/GRADE`](https://github.com/AIM-SCU/GRADE) — *Generalizable Reasoning-Aware Dialogue
Evaluation for AI Tutors*.

| channel | reading `2026-11-02` |
| --- | --- |
| existence (`606-E`) | 🟢 `200` — the address is real |
| `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` × `main` **and** `master` | 🔴 **`404 14 B` on all ten** |
| build manifests — `pyproject.toml`, `setup.py`, `setup.cfg`, `package.json`, `requirements.txt` × both branches | 🔴 **`404 14 B` on all ten** (`598-A` satisfied: there is no manifest channel to read) |
| 🔴 **README, `16,117 B`, final section** | 🔴 *"## License — **MIT** — see [LICENSE](LICENSE)."* |

🔵 **This is not `608-D`'s class.** `608-D` recorded `13` repositories with **no grant claim anywhere**.
This one makes an explicit MIT claim **and points at a file that is not in the repository on either
branch**. `p288`'s `gate-readme-channel` holds that a README-only grant claim *"is not no channel"* —
🔴 but a README that *delegates* to a `LICENSE` file is weaker than one that states terms inline: it
asserts the operative text lives elsewhere, and elsewhere is empty. There is no copyright holder line,
no year and no warranty text anywhere in the repository.

🟡 **Verdict: NOT PROMOTED — recoverable.** A single commit adding the file the README already links
would make this shelvable, because the rest of the row is strong: a BEA 2025 shared-task pipeline
scoring tutor responses on four dimensions (**Mistake Identification**, **Mistake Location**,
**Providing Guidance**, **Actionability**, 3-way labels plus a joint multitask head), **`184` logged
runs** in `master_metrics.csv` across Llama-3.1-8B, Mistral-7B, Qwen3-14B, Gemma3-12B and Gemma3-27B,
with **per-run CodeCarbon kWh/CO₂ tracking** joined to the results table. 🔵 On capability it belongs
in `609-B`'s eval tier; on terms it cannot be built on.

🟡 **And its region is disclosed only inside an HTML comment.** `**Affiliation:** Santa Clara
University — CSEN-346, Spring 2026`, with three named authors, sits in a commented-out block that
renders nowhere. 🔵 Recorded because this base places rows on holder evidence and declines to infer
region from usernames (`608`): had the row been promotable, **North America** would have been
evidenced — by a string no reader of the rendered page can see.

### 🔴 `609-J` — `zty552252kevin-code/holdfast`: a conjunctive grant, non-commercial on both arms

| | reading |
| --- | --- |
| grant | 🔴 **"HoldFast 执迷 — License (v1.0)"**, `1,711 B`, byte-read today — custom, not OSI |
| arm 1 | material derived from `MalruleLib` (scaffolds, rendered dialogues, probe sets, DPO pairs, generator/probe code, evaluation outputs) **inherits MalruleLib's terms: non-commercial, share-alike, attribution**, pinned to commit `8ddedfb` |
| arm 2 | all other original content — *"released for non-commercial research use"* |
| API `spdx_id` | `NOASSERTION` — 🟢 **right, for once** (see `609-F`, where it was wrong on the other two) |
| 🔴 verdict | 🔴 **REJECTED — non-commercial on every arm.** Out of scope for the MIT/Apache/BSD build surface |

🔵 Worth the entry for its *shape*: this is `p427`'s `gate-conjunctive-grant` class — **one payload,
two licence regimes, and a notice obligation under both** — and the two regimes happen to agree on the
boundary that disqualifies it. Attribution is also an **academic** citation (Chen, Liu & Sonkar,
arXiv:2601.03217, ACL Main 2026), not a copyright notice, so satisfying it is a paper citation rather
than a `NOTICE` file. Capability-wise it is relevant: Qwen3 student simulators (`0.6B`–`14B`) trained
to **hold an assigned maths misconception**, which is `609-B`'s cluster exactly.

### 🔴 `609-D` — `mkhomytsya/MuckeligAgentLMS`: a valid Apache-2.0 grant on a `10 KB` repository

Full entry in `verticals/solutions.md` and `agents/top.md` under `p609`. Summary: claims *"the first
cloud-native LMS powered by autonomous AI agents"*, autonomous course generation, **built-in xAPI
LRS**, *"Kubernetes-Native, scalable, production-ready"*; carries a **stock Apache-2.0**,
`11,366 B`, byte-read today; probe `200`. 🔴 **`10 KB` total, created and last pushed `2026-02-12`,
`0` issues, `0` topics.** Verdict: 🔴 **NOT PROMOTED — the grant is real and the software is not.**
🟢 The axis that caught it (**repository size**, free on the search channel) is now run before the
grant on platform candidates.

### 🟡 `609-K` — `Nadia1160/cognitive-student-simulator-tutor`: permissive, relevant, and not yet a project

| | reading |
| --- | --- |
| grant | 🟢 **Apache-2.0**, `11,357 B` — stock body, byte-read today |
| relevance | 🟢 on-topic: *"LLM-Based Intelligent Tutoring System with Error-Aware Feedback for Math Education"* — would sit inside `609-B`'s tier |
| size · history | `277 KB` · 🔴 created `2026-03-02`, pushed `2026-03-02` — a single day, nothing since |
| 🔴 README | 🔴 **Docker boilerplate only** — prerequisites, a PowerShell launcher menu, and a build path reading `D:\Nadia\Nadia\Python\Python Projects\…`. It documents **how to start a container**, and says nothing about the simulator, its student model, or how it is evaluated |
| 🟡 verdict | 🟡 **NOT PROMOTED — unassessable on its own documentation.** The grant is clean and the topic is wanted; there is no described evaluation surface to compose against, and a leaked local build path is the signature of a repository published once rather than maintained |

🔵 **Why this is a disposition and not a rejection.** Nothing here is wrong — it is a permissive,
relevant, under-documented repository. It is recorded so that a later pass searching this exact tier
finds the **prior assessment** instead of re-deciding it, which is the function `608-D`'s unlicensed
list is already serving.

---


## 🆕 `p598` — `2026-11-01` — `4` dispositions, and one of them is a repository this base would have called unlicensed that is in fact permissively licensed

🔵 **The rule this pass changes (`598-A`).** A row is only "no grant" once its **build manifest** has
been read as well as its grant filenames. Probing `13`–`16` filename variants and `0` manifests is
not a finished measurement. 🟢 The full re-audit of every 🔴 BLOCK row on these pages is at
[`../evidence/manifest-channel-audit.2026-11-01-p598.tsv`](../evidence/manifest-channel-audit.2026-11-01-p598.tsv):
**`15 of 16` survived**, so the rule changes without the shelf changing.

| Repo | ★ | Measured `2026-11-01` | Disposition |
| --- | --: | --- | --- |
| [infomark-org/infomark](https://github.com/infomark-org/infomark) | 36 | 🔴 **GPL-3.0**, byte-read `35,149 B`, `main`, live `2026-10-31` | **BLOCK** for a closed deliverable. 🟢 A permissive replacement now exists — [`quickfeed/quickfeed`](https://github.com/quickfeed/quickfeed) (MIT, `1,115 B`) — so the auto-grading seam no longer depends on a copyleft row |
| [uPortal-Project/CoursesPortlet](https://github.com/uPortal-Project/CoursesPortlet) | 12 | 🟡 **BSD-3-Clause** (`1,529 B`) — 🔴 copyright holder reads *"News Reader Portlet Development Team"*, a different project; byte-identical to [`NewsReaderPortlet`](https://github.com/uPortal-Project/NewsReaderPortlet)'s grant | **REVIEW** — permissive terms, mismatched holder. Not a licence screen's call; counsel reads it |
| [Apereo-LAI/SakaiXAPI-Provider](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) | 11 | 🟢 **ECL-2.0** via `pom.xml` `<licenses>`; 🔴 no grant file on `16` variants; last push `2021-03-25`; `42 KB` | 🟢 **NOT UNUSABLE — and not supply either.** Filed here because it is the evidence for `598-A` and the counter-example to `591-B`. `5` years stale and effectively empty: cite the finding, do not depend on the code |
| [s64965264-code/nexo-ia](https://github.com/s64965264-code/nexo-ia) | **0** | 🟡 `"license": "MIT"` in `package.json`; 🔴 no grant file, no licence text, no named holder | **REVIEW, NOT PROMOTED.** The only one of `16` BLOCK rows the new manifest channel recovered — and a manifest string is intent, not a grant. `0★` fails the star floor regardless |
| [speedyapply/2026-AI-College-Jobs](https://github.com/speedyapply/2026-AI-College-Jobs) | — | 🟢 **live** (`README.md` `200` on `main` and `master`); 🔴 **no grant file** (`404` both branches); 🔴 **`422`s on the GitHub search channel** | **BLOCK — and the explanation for `41` sightings with no shelf row.** 🔵 Second confirmed instance of `597-F`: a search-channel `422` is not a dead address. It is a job-listing index rather than education software, and it is ungranted |

🟢 **Instrument note governing all four rows (`597-A`, re-measured and unchanged).** None of these
dispositions could be reached with the verifier this run prompt mandates: `curl -sI
https://github.com/<owner>/<repo>` returned **`403`** for every address above **and** for a
fabricated control. Liveness and grant were established at `raw.githubusercontent.com`
(`200` real / `404` fabricated) and, for `SakaiXAPI-Provider`, in its `pom.xml`.

---

## 🆕 `p597` — `2026-11-01` — `9` dispositions registered (a tenth was drafted and **withdrawn** — see `597-F`), so the `596-C` backlog shrinks by refusal as well as by promotion

🔵 **Why these are filed here rather than left in a log.** `596-C` established that a row sitting
only in an append-only trending log reads as *"already held"* to the gate and is therefore never
re-examined **or** rejected — it is simply invisible. 🟢 Re-measured this pass: `2,049` addresses are
in exactly that state. 🔴 **A promotion is only half the fix.** A measured refusal is also a
disposition, and without one the same dead or ungranted address costs a future pass its legs again.
Each row below was measured `2026-11-01` and is now greppable on a **shelf-class** page.

| repo | ★ | measured `2026-11-01` | class | disposition |
| --- | --: | --- | --- | --- |
| [formalms/formalms](https://github.com/formalms/formalms) | 37 | 🔴 **no licence file**; live `2026-07-17`; `112 MB`; branch `master` | ungranted platform | 🔴 **BLOCK** — a complete, live LMS with no grant whatever. The largest unlicensed platform measured here |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | 54 | 🔴 **no licence file**; live `2026-06-29` | ungranted component | 🔴 **BLOCK** |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 18 | 🔴 **no licence file**; live `2026-07-23` | ungranted component | 🔴 **BLOCK** |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 1 | 🔴 **AGPL-3.0**; live `2026-10-22` | copyleft | 🔴 **BLOCK** for a closed deliverable; usable only as a hosted service with source offer |
| [anonymousonyx22/brightspace-d2l-mcp](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 29 | 🔴 `NOASSERTION` — custom terms; live `2026-11-01` | non-standard grant | 🟡 **REVIEW** — genuinely useful (the only Brightspace MCP found) but counsel must read the terms before any engagement |
| [1edtech/caliper-spec](https://github.com/1edtech/caliper-spec) | 22 | 🔴 `NOASSERTION`; pushed `2025-10-07` — **stale `>12` months** | spec, no open grant | 🟡 **READ-ONLY REFERENCE** — cite it, never vendor it |
| [menthorlabs/menthor](https://github.com/menthorlabs/menthor) | 582 | 🟢 Apache-2.0 — 🔴 **ARCHIVED**; last push `2024-04-21`; `26 MB` | abandoned | 🔴 **DEAD.** The largest LATAM-origin *permissive* education platform this base has found; read-only for `2.5` years |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | 4,393 | 🟢 MIT — 🔴 pushed `2025-10-26`, **`13` months stale**; `213 MB` | frozen curriculum | 🔴 **DEMOTED.** This base's `cycle 2` and `cycle 3` summaries carried it as live supply; it is course material, not a maintained dependency |
| [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **490** | 🟢 **MIT** (`1,067 B`, byte-read `2026-11-01`); `106` forks; EACL'26 Main; 🔴 absent from the GitHub search index | 🟢 **NOT UNUSABLE — ENTRY WITHDRAWN.** Listed here earlier in this pass as a dead address on a `total_count 0`. It is live, permissive and peer-reviewed; promoted to [`../agents/top.md`](../agents/top.md). See `597-F` |
| [littlecookie0722/ai-teaching-agent](https://github.com/littlecookie0722/ai-teaching-agent) | **0** | 🟢 MIT `1,064 B`-class grant; live `2026-08-23` | real but unadopted | 🟡 **NOT SHELVED** — `0★`, no adopters, no third-party validation. Recorded so it is not re-found; **fewer real rows beat padding** |

🔴 **Two of these were demotions of rows this base previously presented as supply**
(`panaversity/learn-agentic-ai`, and `menthorlabs/menthor` as a LATAM permissive example). 🔵 **A
register of refusals has to be able to demote**, or a stale shelf row outlives the measurement that
contradicts it.

🟢 **Instrument note (`597-A`), which governs every row above.** None of these dispositions could be
reached with the verification this harness's run prompt prescribes: `curl -sI
https://github.com/<owner>/<repo>` returns **`403`** here for every repository not attached to the
session, live or dead. Liveness and grant were established by byte-read at
`raw.githubusercontent.com` (`200` + full licence bytes), with the GitHub search API used only for
stars, push date, size and the `archived` flag — and it 🔴 **`422`s on at least one live repository**
([`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet)),
so a `422` must never be recorded as "dead".

---

# Measured / Unusable — the ungranted-domestic-supply register

**Opened at `p544` · 2026-10-30, closing [`Gap 543-D`](../agents/trending.md#-gap-543-a--gap-543-f-registered).**

🔵 **Why this file exists.** An artefact can be **real, live, education-specific
and still unusable**, because it carries **no grant at all**. Such an artefact is
neither a shelf row (nothing licenses us to build on it) nor a reject (it is not
mis-described, mis-licensed or off-sector — it is *correctly* described and
*genuinely* absent a licence). `Gap 543-D` was registered because the class had
no published home: three Vietnamese agents had been found, filed only in a
trending entry, and were on course to be **re-discovered a fourth time**.

🔴 **The rule this register encodes:** *supply is not the same as usable supply.*
A region can have domestic AI-in-education engineering and offer Globant nothing
to build on. Counting artefacts without reading grants overstates every regional
supply claim on this base.


## `p572` (2026-10-31) — six additions, three of them high-star repositories that read as open source

| address | ★ | what the grant actually says | verdict |
| --- | --: | --- | --- |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 2,100 | **"PageLM Community License"**, 8,563 B, bespoke and non-OSI. Grant is for *"personal, educational, or non-commercial research purposes"* only. **"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"** without written permission. Commercial use requires a **revenue-sharing agreement executed in advance**; absent one, use is *"material breach and immediate termination"*. The licence is **revocable**. | ⛔ **HARD BLOCK.** Cannot be shipped, redistributed, hosted commercially, or bundled. 🔴 Seen **59×** in this base's history with its licence never recorded. |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 5,600 | **CC BY-NC 4.0** (19,347 B). Covers the asset that *is* the product: 1,644 knowledge points, 2,403 prerequisite edges, 6,723 curriculum-aligned items. | ⛔ **BLOCK for commercial delivery.** NonCommercial. 🔵 Usable as a *reference schema* for a graph built from scratch; the edges themselves cannot ship. Seen **36×**, never shelved. |
| [`chewyenhan/malaysia-uec-teacher-workflow`](https://github.com/chewyenhan/malaysia-uec-teacher-workflow) | 2 | `LICENSE.md`, **2,876 B**, is a **path table**, and the first line says "MIT". `SKILL.md`, `README.md`, `agents/`, `references/`, `evals/`, `examples/` → **CC BY-NC-SA 4.0**. Only `scripts/`, `tests/` → MIT. Explicitly grants no rights to textbooks, school templates or student data, and reserves separate commercial licensing. | ⛔ **BLOCK on the substance**, MIT on the glue. 🔴 **Fifth distinct split-grant mechanism in this KB — a path table — and it defeated the scope-clause regex while the byte count caught it.** |
| [`githubharald/DeslantImg`](https://github.com/githubharald/DeslantImg) | 156 | `LICENSE.md` is a clean **MIT**, 1,071 B. `requirements.txt` pins **`Py-BOBYQA>=1.3`**, verified first-hand as **GPL-3.0** (35,147 B, title "GNU GENERAL PUBLIC LICENSE", Version 3). Imported in-process. | ⚠️ **LINK-ONLY / avoid in distributed work.** Distributing a combined work triggers GPL-3.0. No §13, so hosting alone is not the trigger. 🟢 Substitute: `WordDetector` + `CTCDecoder`, same author, permissive throughout. |
| [`deepseek-harness-java/teacher-workbench`](https://github.com/deepseek-harness-java/teacher-workbench) | 2 | **No grant at 40 probes** — 4 branches (`main`, `master`, `develop`, `trunk`) × 10 filenames including case variants, all 404. | ⛔ **UNGRANTED** → exclusive copyright. Read the feature taxonomy; ship nothing. |
| [`0x454447415244/HandwritingRecognitionSystem`](https://github.com/0x454447415244/HandwritingRecognitionSystem) | 465 | **No grant at 40 probes.** A 465★ CNN-RNN handwriting system with no licence file on any probed branch. | ⛔ **UNGRANTED** → exclusive copyright. The most-starred ungranted row in this KB. |

### 🟡 Held back from the shelf on provenance, not licence

- [`abmarkguo/medical-exam-teacher-toolkit`](https://github.com/abmarkguo/medical-exam-teacher-toolkit) —
  **MIT**, 1,098 B (body read: the `+28 B` over standard is only a longer copyright
  line, no carve-out). 🔴 **`41` commits, every one dated `2026-07-27`, and the
  repository's first commit is `Add CITATION.cff`.** Not `570-A`-grade synthetic —
  the dates are not internally contradictory — but a repository does not begin with
  its citation file, and 41 same-day commits is an import, not a history.
  **Licence clean, provenance unestablished.**

### 🔵 A convention worth recording

- [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) — 355★, **ARCHIVED**,
  `LICENSE` is **570 B**. 🔵 **The Apache-2.0 licence text is 11,358 B; a ~570 B
  "Apache" file is the boilerplate *header notice*, not a grant.** Treat an
  Apache claim under ~1 kB as an assertion to verify, not a licence to rely on.
  (Compare this pass's genuine Apache grants: 11,340 / 11,343 / 11,357 / 11,358 B.)

## The register

| Address | Origin (region) | What it is | Grant, probed at the resolved default ref | Head read at (pass · ref · sha) |
|---|---|---|---|---|
| 🆕 [`ceanjonnube-negra/docente-ia`](https://github.com/ceanjonnube-negra/docente-ia) | 🟢 **LATAM (Mexico)** — *stated*, but **not in the README**: `ESTADO_PROYECTO.md` describes a *"Herramienta de consulta oficial **SEP**"* restricted to **`.gob.mx`** domains (calendar, `planes y programas`, `acuerdos SEP/DOF`) and `PROJECT_MAP.md` carries the schema flag `es_sep` | **245 commits** — the most substantial artefact `p547` found, and architecturally the most interesting: **two tool mechanisms held deliberately apart**, *"el Tool Registry determinista … **nunca pasa por Claude**"* beside Claude's native function-calling. 🔴 **Its `README.md` is 1 450 B of untouched `create-next-app` boilerplate** — the concrete instance of `Gap 544-B`'s README-only limit doing damage (`Gap 547-D`) | 🔴 **`UNRESOLVED`** — nothing licence-shaped in the tree at `HEAD` and **no grant declared** in `README`, `package.json` or any `*.md` | `main` · `p547`, last commit `2026-10-28` |
| 🆕 [`jrsaguas/DocenteAgent`](https://github.com/jrsaguas/DocenteAgent) | 🔴 **UNPLACED** — no country evidence read first-hand. Commit timezone `-06:00` is a **hint, not evidence**, and `p545`'s rule forbids placing an `es` artefact on its language | Teacher-administration agent (syllabus, planning, attendance, exams, grades) with a stated human gate — *"Acciones externas sensibles requieren autorización humana **inicialmente**"*. 🔴 **Read `inicialmente`:** the gate is declared provisional, and `biometría después` is on the roadmap, with `docs/ATTENDANCE_BIOMETRICS_ROADMAP.md` and `docs/MOODLE_AUTH_SECURITY.md` in tree. 🔵 Biometric attendance in schools is the one function that would move an engagement from Annex III high-risk into the AI Act's **prohibited** tier if it drifted into emotion inference | 🔴 **`UNRESOLVED`** — nothing licence-shaped in tree, none declared in `README` (1 231 B) | `master` · `p547`, last commit `2026-09-29` |
| 🆕 [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) | 🟢 **EMEA (Germany)** — *stated* in the tree itself: `rahmenlehrplan.md` for **all 16 Bundesländer** plus their school law and `Verwaltungsvorschriften` | 🔴 **A different class from the rows above, filed here so it is not re-discovered.** The best regional fit `p547` found — 16-Länder curricula, `Förderschwerpunkt` differentiation (ESE · Hören · Lernen) × five subjects, `.docx`/OMML output, 103 files — and **unusable twice over**: 🔴 *declared-but-unserved* (`"license": "MIT"` in `plugin.json` **and** `## Lizenz` in README, **no licence file at any path**, holder `{"name": "anonym"}` so MIT's notice clause cannot be satisfied even in principle — `Gap 547-A`); 🔴 *circumvention-blocked* (`bin/bibox` decrypts **AES-256-CTR**, `bin/cornelsen` **AES-128-CBC** — UrhG § 95a / InfoSoc Art. 6, `Gap 547-B`). 🟢 **`bin/klett` performs no decryption** and is the one reusable third | 🔴 **`DECLARED_UNSERVED`** — not `UNRESOLVED`: a bare `UNRESOLVED` would lose the fact that the author asserted MIT twice | `main` · `3ddcfbbabc56`, last commit `2026-04-06`. 🔴 Mirror: [`NikolasSchaeffner/lehrer-agent`](https://github.com/NikolasSchaeffner/lehrer-agent) is the **same tree at the same sha** |
| [`MaiQuangPhuoc/edu_agents`](https://github.com/MaiQuangPhuoc/edu_agents) | 🟢 **APAC (Vietnam)** — *stated*: grade-10 **GDPT 2018** national curriculum | Grade-10 curriculum agent. 🟢 **Architecturally the most interesting artefact four language legs returned:** it chooses a **deterministic pipeline over ReAct** for the education domain and **bounds the LLM to the textbook** to suppress invention. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`, plus sidebar and README at `p543` | `main` · `03e43219c66a` |
| [`dungptt-dng/smart-ict-classroom`](https://github.com/dungptt-dng/smart-ict-classroom) | 🟢 **APAC (Vietnam)** — *stated*: **Vietnam AI in Education Pioneer Award 2026** entry | A computer lab with **fewer machines than groups**: fair turn scheduling and four rotating in-group roles. A constraint a LATAM or APAC public-school engagement meets constantly and no shelf row addresses. | 🔴 **`UNRESOLVED`** — as above | `main` · `a9c56b3b7496` |
| [`minhdevtry/AI-Teacher-Assistant-Agent`](https://github.com/minhdevtry/AI-Teacher-Assistant-Agent) | 🟢 **APAC (Vietnam)** — *stated*: Vietnamese, **Zalo** Bot | *ZaloAgent* — class management over Zalo, the domestic messenger, with fee capture by text **and image OCR**. | 🔴 **`UNRESOLVED`** — as above | `main` · `f3bcc636da1d` |
| 🆕 [`fairyofmiracle/edu_course_agent`](https://github.com/fairyofmiracle/edu_course_agent) | 🟡 **EMEA (Russia)** — *inferred, and the inference is named*: README and UI are **Russian**, the LLM gateways are **Cloud.ru** and **GigaSchool** (both Russian services), and the output is Russian **ДПО** professional-development paperwork. The page itself states no country. | A methodologist's workstation: builds a professional-development programme from an **ACR template**, and exports **DOCX / PPTX / JSON**. 🟢 **It refuses to invent the order number (`наказ`/приказ) and the labour-function code** — the artefact's whole value is that two legally-load-bearing identifiers are *not* generated. 196 commits, **0★, 0 forks**. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`; sidebar shows no licence and does not say "no licence" | `main` · `c425a51c2512` |

🔴 **Four artefacts, two languages of origin, zero grants.** The Vietnamese trio
came off `p543`'s `vi` leg; the Russian row came off `p544`'s **`uk`** leg. The
class is now **stable across two unrelated origins**, which is what makes it a
class rather than a Vietnamese peculiarity.

## 🟢 What a studio may still do with a row here

🔵 Nothing in this register may be **vendored, forked or shipped** — there is no
licence to do so. What it is legitimately good for:

1. **Read the architecture, write your own.** `MaiQuangPhuoc/edu_agents`'s
   deterministic-pipeline-over-ReAct choice and textbook-bounded generation are
   *design* findings. A design is not a derivative work.
2. **Name the requirement.** `smart-ict-classroom`'s fewer-machines-than-groups
   scheduling is a **real constraint of public-school delivery** that no granted
   shelf row covers.
3. **Ask.** 🟢 The cheapest action available: open an issue requesting an
   explicit licence. `ACTION p417-A` already prescribes this for a LATAM address;
   the same move applies to all four here, and a single `LICENSE` commit would
   move a row onto the shelf.

🔴 **What must not happen:** a row here being quoted as regional "supply" in a
market slide. It is supply that cannot be used, and the register exists so the
distinction survives the next pass.
