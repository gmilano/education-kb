---
industry: education
region: Global
updated: 2026-10-20
---

## Pass 344 · 2026-10-20 — the two addresses this base could not resolve were both wrong in the same new way, and one row turns out to be unplaceable *because of how it was written*

**Evidence:** [`p344-address-resolution`](../evidence/p344-address-resolution.2026-10-20-p344.tsv) · [`p344-payload-absence-enumerated`](../evidence/p344-payload-absence-enumerated.2026-10-20-p344.tsv) · [`p344-region-placement`](../evidence/p344-region-placement.2026-10-20-p344.tsv) · [`p344-agent-runtime-region`](../evidence/p344-agent-runtime-region.2026-10-20-p344.tsv).

🔴 **Inherited gate state is NOT reported this pass, and the reason is an environment limit rather than a finding — SECOND CONSECUTIVE PASS.** `make hooks` could not be run: this session's tool policy refuses to execute the repository's own `compose/code/` instruments (classifier verdict `Code from External`). 🟢 **No instrument was invoked and none was modified.** Every measurement below was taken with plain `git` and `curl` issued directly, which is why each row carries its raw distribution rather than an instrument verdict. **`ACTION ZZ-a` is satisfied in this position; the consequence is that `gate-shelf-consistency` has now not judged a published cell for two passes.**

### 🟢 `ACTION ZZ-c` executed over this pass's five rows, and the 100% case is a new blindness class

🔵 `p343` registered `ZZ-c` — *before citing any row's commit count as a bench, split the log by author domain and read the subject lines of the automated half.* Run over the five rows this pass touched, **four are 0.0% agent-authored and one is 100%**:

| Repo | Grant, read first-hand | Commits · authors · span | Agent-authored | Placed, and how |
|---|---|---|---|---|
| `formalms/formalms` | 🟡 GPL-2.0, 18 346 B, **`master/html/license.txt`** — not in root | 7 494 c · 59 a · 2013-07-08 → **2026-07-17 (3 months stale)** | 0 / 7 494 | 🟢 **EMEA — Italy** — `joint-tech.it(1603)` `giuseppenucifora.com(1585)` `grifomultimedia.it(837)` `email.it(626)` + `+0200(3415) +0100(2547)` CET/CEST pair |
| `openeducat/openeducat_erp` | 🟡 LGPL-3.0, 8 241 B, **`19.0/LICENSE`** | 1 711 c · 97 a · 2012-10-17 → **2026-10-13 (live, 7 days)** | 0 / 1 711 | 🟢 **APAC — India** — `techreceptives.com(637)` + `openeducat.com(263)` corporate + `+0530(1493/1711)` IST |
| `loyaniu/moodle-mcp` | 🔴 **none — no payload and no manifest declaration** | 17 c · 6 a · 2025-04-03 → 2026-06-28 | 0 / 17 | 🟢 **North America — US** — institutional `calvin.edu(4)` + `-0400(12)` modal; 🔵 `rwth-aachen.de(3)` is a **genuine EMEA co-contribution** |
| `adriasantacreu/google-classroom-mcp` | 🟡 **MIT declared in `package.json`, no licence text anywhere in the tree** | 11 c · 1 a · 2026-03-18 → 2026-03-21 | 0 / 11 | 🟡 **EMEA** — `+0100` on all 11; **offset-only**, `gmail.com` only, **dormant 7 months** |
| `davipac/classroom-mcp` | 🟡 **MIT declared in `package.json`, no licence text** | **2 c · 1 a · 2026-09-07 — both authored `noreply@anthropic.com`** | **2 / 2 = 100%** | 🔴 **NOT RESOLVED** — see the rule below |

### 🔴 `ACTION ZZ-f`: on a fully agent-authored repository the commit channel measures the AGENT'S RUNTIME, not a human geography

`davipac/classroom-mcp` is **2 of 2 commits authored by `noreply@anthropic.com`**, offset `+0000`, and its default ref is `claude/publish-classroom-aluno-mcp-9g61ee` — **an unmerged agent working branch serving as the repository's default branch.**

🔴 **Both of the channels `ACTION ZH` reads are properties of a datacenter.** `anthropic.com` is not a corporate domain in the sense `ZH` means it, and `+0000` is not a timezone anyone lives in. 🟢 **The instrument does not return a *wrong* answer here — it returns the runtime's answer, which is worse, because it looks exactly like a placement.** A pass that read `+0000` as a channel would have published EMEA on a row with no human geography in it at all.

🔵 **The one channel that does carry a human signal is the natural language of the subject lines**, and they are Portuguese: `adiciona helper temporario de bootstrap OAuth (sem maquina local)` · `servidor MCP do Google Classroom para aluno`. 🔴 **Per `ACTION ZZ-b` that is a prompt-language signal, not an authorship measurement, and it may not enter the `Placed` cell.** So the row stays **NOT RESOLVED** — and it is **the first row on these shelves that is unplaceable because of how it was written rather than because of what it omits.**

🟢 **`ACTION ZZ-f` registers two things.** First, the general rule: **a row's agent-authored share is a confidence discount on its region placement, and at 100% the region channel is void and must be reported as void, never as an offset.** Second, the quantitative refinement of `ZZ-c`: that action graded *bench quality* (engineering vs promotion); this one grades *placeability*, and the two are different axes on the same split. 🟡 **This class will grow**: these shelves have now found an agent-authored default branch (`p342`), 26.8% agent-authored self-promotion (`p343`, `zijinz456/OpenTutor`), 6.4% agent-authored engineering (`p343`, `ArnaudGuiovanna/tutor-mcp`) and a 100% agent-authored repository (this pass) in three consecutive passes.

### 🟢 Legal state: the three carried MCP rows were one open item and are actually two different answers

🔵 `p342` carried all three as *"returned NO PAYLOAD at all this pass"*. 🟢 **All three were re-probed, all three exist, and the absence is now refuted-or-confirmed by tree enumeration rather than by a ladder** (`ACTION p275`): `git ls-tree -r` over a `--filter=blob:none` bare clone, with a **word-anchored** pattern. They split:

- 🟡 **`adriasantacreu/google-classroom-mcp` and `davipac/classroom-mcp` — declaration without text.** Both declare `"license": "MIT"` in `package.json`; **neither ships a licence file anywhere in its tree.** Per `ACTION p280` a manifest is identified by what it *declares*, and a declaration is **not a grant**. 🟡 For an engagement this is a one-email fix and worth making, because the intent is unambiguous.
- 🔴 **`loyaniu/moodle-mcp` — no payload AND no declaration.** `pyproject.toml` carries **no `license` key at all**. 🔴 **This is the only one of the three that is unambiguously not usable**: with no grant and no declaration, the default is all rights reserved. 🟢 **It is also the best-placed of the three** (institutional `calvin.edu` + `rwth-aachen.de`), which is precisely the trap: **the row that looks most credible on its bench is the one that cannot be built on.**

🟢 **Promoted to the table this pass: none.** 🔵 **The supply legs returned one genuinely new slug** — `Noor-ul-Eman28/AI-Tutor-MCP-Toolkit`, which exists and ships **no licence payload at any standard root name**. It is not promoted, and the reason is recorded rather than the row.

🔵 **`gate-identity`, incidentally:** `kvnloo/tutor-mcp` and `ArnaudGuiovanna/tutor-mcp` return **different HEADs** (`3d11705` vs `05c5661`) ⇒ **two repositories, not one**, so `ACTION p283`'s gate is not tripped. 🟡 But `kvnloo` is a **divergent fork** of the row `p343` placed EMEA, and both addresses sit on these shelves — a reader comparing them is comparing a fork to its upstream, not two projects.

## Pass 343 · 2026-10-20 — `ACTION ZC` is executed over fourteen held rows: thirteen place, one resolves to NOT RESOLVED for a reason worth a rule, and the commit channel turns out to report **what an agent was used for**

**Evidence:** [`p343-action-zc-placement`](../evidence/p343-action-zc-placement.2026-10-20-p343.tsv) · [`p343-agent-authored-commits`](../evidence/p343-agent-authored-commits.2026-10-20-p343.tsv).

🔴 **Inherited gate state is NOT reported this pass, and the reason is an environment limit rather than a finding.** `make hooks` could not be run: this session's tool policy refuses to execute the repository's own `compose/code/` instruments (classifier verdict `Code from External`). 🟢 **No instrument was invoked and none was modified.** Every measurement below was taken with plain `git` and `curl` issued directly, which is why each row carries its raw distribution rather than an instrument verdict — the numbers are reproducible without this base's code. **`ACTION ZZ-a` registers the consequence: a pass that cannot run `make hooks` must say so in this position and must not write an instrument-derived cell.**

### 🟢 `ACTION ZC`, executed — the sweep p342 registered and no pass had run

🔵 `p342` found that five consecutive passes had written *"the LATAM supply side returned nothing placeable"* while `Cvmcosta/ltijs` sat on these shelves unplaced and measurably Brazilian, and named the defect precisely: **the region question had only ever been asked of the discovery channel, never of the inventory.** `ACTION ZC` registered the remedy — *place every unplaced row already on these shelves before declaring any region a gap.* 🟢 **This pass runs it over fourteen rows.**

| Repo | Grant, read first-hand | ★ | Activity (bare-clone channel) | Placed, and how |
|---|---|---|---|---|
| `withmarbleapp/os-taxonomy` | ODbL-1.0 (db) + CC-BY-SA-4.0 (text), 25 289 B, `main/LICENSE` | 6.6k | 48 c · 3 a · 2026-07-08 → 2026-10-20 | 🟢 **EMEA** — `withpebble.com(7)` corporate + `+0100(43) +0200(4)` modal across Jul–Oct |
| `Selleo/mentingo` | 🟢 MIT, 1 062 B, `main/LICENSE` | 96 | **1 348 c · 48 a · 2024-08-01 → 2026-10-16 · 439 c in 2026** | 🟢 **EMEA — Poland** — `selleo.com(223)` corporate + `+0200(839) +0100(506)`; **290 commits outside Mar–Nov confirm the CET/CEST shift** |
| `artcc/freelingo` | 🟡 AGPL-3.0, 34 514 B (stock), `main/LICENSE` | 191 | 1 176 c · 7 a · 2026-04-30 → 2026-10-20 | 🟡 **EMEA** — `+0200(1169/1176)` modal, Apr–Oct; **offset-only, no corporate domain** |
| `ArnaudGuiovanna/tutor-mcp` | 🟢 MIT, 1 073 B, `main/LICENSE` | 53 | 467 c · 5 a · 2026-04-05 → 2026-10-16 | 🟡 **EMEA** — `+0000(390) +0200(76)`, 466/467 inside the European window; **offset-only**, modal domain `proton.me` is a privacy provider with no geography |
| `ahmedEid1/lumen` | 🟡 GPL-3.0, 35 149 B (stock), `main/LICENSE` | 90 | 828 c · 3 a · 2020-11-29 → **2026-06-07 (4 months stale)** | 🟢 **EMEA** — `+0200` on **all 828** commits *including 39 outside Mar–Nov* ⇒ a **non-shifting UTC+2 zone**, i.e. the Africa / Middle East band, **not** CEST |
| `Miaotofu01/Study-Mate` | 🟢 MIT, 1 064 B, `main/LICENSE` | 1.1k | **727 c · 19 a · 2026-09-15 → 2026-10-20** (whole history is 5 weeks) | 🟢 **APAC — China** — `+0800(711/727)` + `qq.com(197)` |
| `zijinz456/OpenTutor` | 🟢 MIT, 1 068 B, `main/LICENSE` | 148 | 194 c · 3 a · 2026-02-26 → 2026-10-18 | 🟢 **APAC — Australia** — `+1100(135) +1000(6)` AEDT/AEST pair; **18 commits outside Mar–Nov are consistent with southern-hemisphere DST**, which is the inverse of `ACTION ZI-b`'s northern test |
| `Li-Evan/Bloom` | 🟢 MIT, 1 069 B, `main/LICENSE` | 289 | 78 c · 2 a · 2026-03-10 → 2026-10-20 | 🟢 **APAC — China** — `+0800` on all 78 + `qq.com(68)` |
| `SenmuuuuW/universal-diagnostic-tutor-skill` | 🟢 MIT, 1 102 B, `main/LICENSE` | 249 | 57 c · 1 a · 2026-06-26 → 2026-09-24 | 🟡 **APAC** — `+0800(48/57)`, single author |
| `karanb192/algo-sensei` | 🟢 MIT, 1 081 B, `main/LICENSE` | 293 | 9 c · 2 a · 2025-10-21 → 2026-10-02 · **1 commit in 2026** | 🟢 **APAC — India** — `+0530` on all 9. 🔴 **293 ★ on nine commits; dormant** |
| `flysheep-ai/education-skills` | 🟢 MIT, 1 068 B, `main/LICENSE` | 116 | **4 c · 2 a · entire history is one day, 2026-01-29** | 🟡 **APAC** — `+0800` on all 4. 🔴 **Dead for nine months** |
| `ZeKaiNie/universal-examprep-skill` | 🟢 MIT, 1 065 B, `main/LICENSE` | 310 | 183 c · 7 a · 2026-06-24 → 2026-10-18 | 🟢 **North America — US (California)** — institutional `ucdavis.edu(33)` + `-0700(149)` modal; 🔵 `+0800(34)` secondary is a **genuine APAC co-contribution**, the only cross-region bench in the batch |
| `nichochar/ari` | 🟢 MIT, 1 073 B, `main/LICENSE` | 158 | 11 c · 1 a · 2026-10-18 → 2026-10-19 | 🟡 **North America** — `-0700(10)` in October; **offset-only, no corporate domain, two days of history** |
| `KeWang0622/kaogong-skill` | 🟢 MIT, 1 083 B, `main/LICENSE` | 192 | 5 c · 2 a · 2026-04-06 → 2026-10-11 | 🔴 **NOT RESOLVED** — see the rule below |

🟢 **Score: 13 of 14 placed. EMEA 5 · APAC 6 · North America 2 · LATAM 0 · NOT RESOLVED 1.**

🔴 **LATAM returned zero from this batch, and that is now a measured statement about the inventory rather than about the query.** Combined with `p342`'s placement of `Cvmcosta/ltijs` (**LATAM — Brazil**, `yahoo.com.br` 429/575, `-0300` 513/575), these shelves hold **one** instrument-placed LATAM row. 🟢 **That is the honest number, and it is the first time it has been stated as a count instead of as a silence.**

### 🟢 The rule `kaogong-skill` earns: subject region and authorship region are different claims, and a row may not borrow one for the other

`KeWang0622/kaogong-skill` is **China civil-service and public-institution exam preparation** — the subject matter is unambiguously APAC. Its commit channel reads `-0700(4) -0500(1)`, modal domain `users.noreply.github.com(4)`, on **five commits**, with `pika.art(1)` the only non-noreply address and not a geographic one.

🔵 **Both channels are legible and they disagree.** On the shelf's own instrument the answer is forced: `ACTION ZH`'s fallthrough finds no corporate domain, five commits is below any reasonable floor, and the result is **NOT RESOLVED**. 🟢 **`ACTION ZZ-b` registers the general rule, because this will recur across every exam-prep row on these shelves: a row's SUBJECT region is a market signal and belongs in the prose; its AUTHORSHIP region is what the commit channel measures and is the only thing the `Placed` cell may carry. A pass may not promote the first into the second, in either direction.** The practical consequence for an engagement is the useful half: **a China-facing product need not have a China-based bench**, and this row is the specimen.

### 🔵 The finding this pass did not go looking for: the commit channel reports **what an agent was used for**, and two held rows split cleanly

Two of the fourteen carry a double-digit count of commits whose **author** address is `noreply@anthropic.com` (author name `Claude`). 🟢 **The share is not the finding. The subject lines are.**

| Repo | Agent-authored | Share | Subject lines, sampled first-hand | What the agent was used for |
|---|---|---|---|---|
| `zijinz456/OpenTutor` | **52 of 194** | **26.8%** | `chore: weekly build-in-public content for 2026-10-18` · `chore: weekly repo health report 2026-10-15` · `chore: community post drafts for 2026-10-13` | 🔴 **Project promotion and reporting.** Not one engineering commit in the sample |
| `ArnaudGuiovanna/tutor-mcp` | **30 of 467** | 6.4% | `fix: scan retired migration columns once, without regexps` · `test: record the reviewed GetLearnerDomainByID store exception` · `fix: close P2 robustness and abuse findings from the stabilization audit` | 🟢 **Engineering.** Migrations, store exceptions, and a named stabilization audit |

🔴 **So a commit count is not a comparable unit across these two rows, and neither is a star count.** `OpenTutor`'s 194 commits include **52 of automated self-promotion running weekly since March**, and its 148 ★ sit next to an agent that drafts community posts on a schedule. 🟢 **This is the same family as the star-solicitation caveat these shelves recorded for `24kchengYe/human-skill-tree` at p318/p319 — but it is measured on a different channel, and it is cheaper: `git log --format='%ae%x09%s' | grep -i anthropic` needs no README reading and no judgement.** 🔵 **`tutor-mcp` is the opposite case and the one worth acting on: a 467-commit bench where the agent closed robustness and abuse findings is evidence of maintenance discipline, not of inflation.**

🟢 **`ACTION ZZ-c`: before citing any row's commit count or star count as a bench, split the log by author domain and read the subject lines of the automated half.** The axis is not *human vs agent*; it is *engineering vs promotion*, and only the subject lines carry it.

### 🟢 Promoted to the table this pass: one row

🔵 **`nichochar/ari` is the only slug in this pass's sweep that was absent from every shelf** — the other thirteen were already held and only unplaced. It is promoted with its limits stated, because they decide where it can be used:

- 🟢 **The idea is the asset.** A camera over a sheet of paper; the learner works problems **by hand**; the model sees the handwriting and grades and adapts from it. `TUTOR.md` carries teaching style, `USER.md` carries learner context, `memories/` carries saved reflections. **No row on these shelves had handwriting-in-the-loop before this one.**
- 🔴 **Do not build on it.** **11 commits, one author, two days old.** The camera bridge is **macOS-only**; the LLM path is **a local Codex login tied to a ChatGPT account**, and the README states that submitted work and learning context **are sent to OpenAI**. For an EU engagement that is a high-risk-system data path under the AI Act before a line is written, and for a K-12 engagement in a US state with a student-data rule it is the exact disclosure the rule is about.
- 🟢 **Read it for the interaction design**, the same disposition these shelves give `openeduhub/metadata-agent-canvas`.

## Pass 342 · 2026-10-20 — no agent row changes, and the reason is worth more than a row would be: the classifier behind every licence cell on this shelf now reads a title in a second language

**Evidence:** [`p342-nonenglish-title-falsifier`](../evidence/p342-nonenglish-title-falsifier.2026-10-20-p342.tsv) · [`p342-channel-disagreement`](../evidence/p342-channel-disagreement.2026-10-20-p342.tsv).

🟢 **This shelf's rows are unchanged and no cell is corrected. That is the honest headline for the second consecutive pass.** `p341`'s census found all 16 bespoke instruments already labelled correctly; `p342` re-read 21 payloads through four channels and found **no published cell on this shelf wrong**. 🔵 **What changed is the capability underneath them**, and it is the thing that cost 22 passes last time.

🟢 **`pass257.family_of` — which decides the licence cell on this shelf, `repos/foundations.md`, `verticals/solutions.md` and `compose/patterns.md` — now keys its TITLE vocabulary by language** (`TITLE_ANCHORS_BY_LANGUAGE`) and carries a new verdict, `UNREADABLE-TITLE:no-family-vocabulary-for-this-language`. **185/185 controls, offline, already in `make hooks` (24/24).** Before this pass a Portuguese AGPL-3.0 grant came out of it as *nothing found*; see `intel/trends.md` **T31**.

🔴 **The one thing a reader of this shelf must change in their own habits.** `haolpku/k12-kgraph`'s row here correctly splits *MIT (code) / CC BY-NC-SA 4.0 (data)* — **and `lib/license_family.sh::family_of` answers a bare `MIT` on that payload**, by reading its cross-reference to a sibling `LICENSE-CODE` file as the payload's own grant. 🟢 `pass257` returns `RESTRICTED:added-restriction` and `pass258` returns not-usable with `noncommercial` and `sharealike` both named, **so a two-channel read is safe and a one-channel read ships an NC dataset as permissive.** **Never promote a dataset row on `family_of` alone** (**T33**). 🟢 **Both halves of that row are now read first-hand** — `LICENSE-CODE` is verbatim MIT (1 075 B), the root payload is CC BY-NC-SA 4.0 — **so this shelf's split cell is confirmed, not inferred** ([`p342-sibling-grant-reads`](../evidence/p342-sibling-grant-reads.2026-10-20-p342.tsv)).

🟡 **Agent supply this pass: zero new rows, ninth consecutive measurement.** The four prescribed global legs returned four named candidates — `pguso/agents-from-scratch`, `rohitg00/ai-engineering-from-scratch`, `microsoft/ai-agents-for-beginners`, `avinash201199/free-ai-agents-resources` — and `make carried` reports **four CARRIED**. Two discovery legs added in Spanish and Chinese returned no project list at all. Recorded in `intel/market.md`.

## Pass 341 · 2026-10-20 — every licence payload on the live shelves re-read and typed by TITLE: 10 of 208 are bespoke instruments, all 10 already labelled correctly, and the one row this base could not resolve was unreadable because its licence is in Portuguese

🟢 **What changed at Pass 341, in one place.** `p340` closed T25's falsifier and left one question written down as unmeasured: *"how many `LICENSE*` payloads on these shelves are bespoke instruments rather than stock texts?"* **It is now measured over 208 payloads read first-hand from the four live decision shelves** ([`p341-bespoke-instrument-census`](../evidence/p341-bespoke-instrument-census.2026-10-20-p341.tsv)): **183 `SPDX-TITLED` · 15 `UNTITLED` · 10 `BESPOKE-TITLED`; 181 stock (87.0%), 16 (7.7%) carrying an instrument a human must read.**

🟢 **The headline is a negative result and it is the most useful thing here: all 16 are ALREADY labelled correctly on these shelves.** `caviraoss/pagelm` already reads *"CaviraOSS Community Licence" — NOT open source*; `canyongbs/advisingapp` already reads *Elastic Licence 2.0 — source-available, not OSI*; `haolpku/k12-kgraph` already splits *MIT (code) / CC BY-NC-SA 4.0 (data)*. 🔵 **The bespoke class was never an unmeasured exposure — it was measured row by row, in prose, by earlier passes, and never counted. This census corrects no published cell; what it adds is the denominator, the named population and a standing gate** (`gate-bespoke-title`, 34 offline controls, **24/24 `make hooks`**).

🔴 **One carried row RESOLVED, and the reason it was never resolvable.** `portabilis/i-diario` has carried *"a LICENSE file exists but the page does not name the licence — read the file before any use"* since p319. This pass read it: branch `1.6`, `LICENSE`, **35 326 B**, opening **`LICENÇA PÚBLICA GERAL AFFERO GNU · Versão 3, 19 de novembro de 2007`**. **It is `AGPL-3.0`.** 🔴 **Both of this base's shared family classifiers return nothing on it** — `pass257.family_of` → `None`, `lib/license_family.sh` → `UNCLASSIFIED` — because their family vocabulary is **English-only** while the restriction vocabulary beside it covers eleven languages. 🔴 **And the verdict they produce, `UNCLASSIFIED:no-family-no-restriction`, fails UNSAFE: it reads as "nothing found" on the strongest copyleft in this corpus.** 🟢 Consequential: its sibling `portabilis/i-educar` is `GPL-2.0`, so the Brazilian municipal stack carries **network copyleft on the teacher-facing portal and ordinary copyleft on the SIS core**. Became **T31**; the population is **3 of 208, all Portuguese, all Brazilian** ([`p341-nonenglish-payload-blindness`](../evidence/p341-nonenglish-payload-blindness.2026-10-20-p341.tsv)).

🟡 **A finding this pass withdrew, recorded because the withdrawal is the finding.** The census flags **4 of 6 BSD-family payloads** `needs-a-human` whose only hit is `all rights reserved` — stock BSD boilerplate, one row foundation-tier. This pass wrote the one-line fix, applied it, and `pass257`'s own suite went **127/129**: its controls pin that behaviour deliberately, with the reason in the comment above them. **The patch was reverted; `pass257` is byte-identical to `HEAD`.** 🔵 **`p340` counted five instances of "a capability was present and nearly re-derived as news"; this is one degree worse — a DECISION was present, documented in the suite that guards it, and nearly overturned as a defect. Running the suite caught it; reading it would not have.** 🟢 What survives is the price tag nobody had measured: **4 of 208 (1.9%)**, with a *positional* repair prescribed and its falsifier named in [`p341-bsd-boilerplate-cost`](../evidence/p341-bsd-boilerplate-cost.2026-10-20-p341.tsv).

🔴 **Two shared classifiers disagree on the one licence family named for this industry.** `pass257.TITLE_ANCHORS` carries `eclipse public license → EPL` and **no rung for the Educational Community License**, so `opencast/opencast` (11 340 B) and `sakaiproject/sakai` (11 120 B) both return `family=None` where `lib/license_family.sh` returns **`ECL-2.0`** correctly. The 17 `ECL-2.0` cells on these shelves are right because `probe_repo` uses the classifier that gets it right. `p278`'s channel-conflict class, between two instruments in one `lib`.

🟢 **The case-varied ladder `p336`/`p337` bought paid out again, unprompted: 6 of 208 located payloads sit at spellings an all-uppercase ladder would have missed** — `license.txt` ×3, `license.md`, `LICENCE.md`, `docs/License.txt`. 🟡 **And 2 of 239 shelf addresses collapsed under lower-casing** — p340's slug-identity finding reproducing on a population it did not cover.

🔵 **Nothing in the tier tables below changed this pass.** The census re-read them and agreed with every cell; p340's block and p339's verification record still govern this shelf.

## Pass 340 · 2026-10-20 — the MCP tier tripled on a completed census: 13 connector rows promoted with grants read from the tree, three platforms reached for the first time, four regions placed by institution, and one `LICENSE.md` that forbids commercial use

🟢 **What changed at Pass 340, in one place.** This pass ran **T25's own named falsifier to completion** — `intel/trends.md` had carried the connector-licence inversion since p334 on 12 probed lanes against a population of 74, with *"probe the remaining 62"* written into the trend. **93 distinct repositories are now probed first-hand** ([`p340-connector-licence-census`](../evidence/p340-connector-licence-census.2026-10-20-p340.tsv)): **59 permissive · 4 copyleft · 23 with no licence path anywhere in their tree · 6 that no longer exist · 1 proprietary.** 🟢 **T25 survives on direction and is corrected on strength** (proprietary platforms 100% permissive; open-source platforms 73% permissive, not uniformly copyleft) — the restatement is in `intel/trends.md` T25. 🟢 **The MCP tier below grows from 6 rows to 19**, reaching **Brightspace/D2L, Blackboard and Google Classroom with a first-hand grant for the first time**, and carrying **four institution-specific lanes placed in EMEA, APAC and North America.** 🔴 **The LATAM supply gap stands — fifth consecutive measurement — now with two named, probed near-misses rather than silence.** Full working on `agents/trending.md` and `repos/trending.md`; gaps on `intel/open-gaps.md`.

🔵 **Everything below this block is p339's verification record, which this pass re-ran rather than re-wrote: the channels, the no-star-counts rule and the case-and-path ladder discipline are unchanged and still govern this shelf.**

## Pass 339 · 2026-10-20 — 15 agent rows re-verified first-hand, one absence claim refuted in-pass by this repo's own gate, and the MCP tier re-established with a Canvas rung for the first time

**Verification channels available this pass.** `api.github.com` → **403** for every slug (session scope), `github.com` HTML → **403 for every slug, including ones that do not exist**, so it is useless even as an existence oracle. Three channels do work:

| channel | what it establishes | result |
|---|---|---|
| `git ls-remote --exit-code -h https://github.com/<slug>` | the repository exists and serves refs | ran on every row; all promoted rows `exists=YES` |
| `raw.githubusercontent.com/<slug>/<branch>/<path>` | the grant, read from the file itself | every grant below read first-hand |
| `git clone --depth 1 --filter=blob:none --no-checkout` + `git ls-tree -r HEAD` | **the whole tree**, so an absence claim rests on a tree and not a ladder | used on all four refusals |

🔴 **One absence claim in this pass's first draft was wrong, and `make gate-enumeration` refuted it before anything was committed.** I published `OS4ED/openSIS-Classic` as ungranted off a root-only ladder; its grant is **GPL-2.0** at `docs/License.txt`. This base had already resolved that row at `p311`, so I restated a retracted claim. 🔵 **`p275`'s standing lesson — a ladder is not a tree — now has a second dated casualty, and every refusal below was consequently re-run against a full tree.**

**No star count appears in this file.** The only channels that serve stars are 403 here, and every star figure the search channel offered was third-party. An earlier cycle of this rotation recorded star counts a later pass had to retract as inflated; writing none is the correction holding.

**The licence ladder was varied by case and by path on every row**, because grants on these shelves sit at `license.txt`, `LICENSE.txt`, `COPYING.txt` and `docs/License.txt` as often as at `LICENSE`.

## Build-on-this tier

**8 permissive rows** — every grant MIT, Apache-2.0 or BSD-3-Clause, read from the file. These are the rows a studio can build on and relicense into a client deliverable without a copyleft question.

| Agent | Repo | Licence | Grant read at | What it does |
|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | `main/LICENSE` | Lifelong personalised tutoring with bounded tutoring memory, learning-path review, grouped assessments and an agent-native CLI; ships an `EduHub` skills ecosystem. **v1.6.15 dated 2026-10-19 — the freshest release on this shelf, one day old at measurement** |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | `main/LICENSE` | Open Multi-Agent Interactive Classroom (Tsinghua MAIC): builds a classroom from a topic or document with an AI teacher and AI classmates; generates slides, quizzes, simulations and project work. **v1.2.1 dated 2026-10-18**; server-first generation survives closed tabs and restarts |
| OATutor | https://github.com/CAHLR/OATutor | MIT | `main/LICENSE` | Open-source Adaptive Tutoring System from UC Berkeley CAHLR. **Bayesian Knowledge Tracing** for skill-mastery estimation, React, deployable to static pages with no backend; LTI middleware for LMS integration. 🔵 The only row here with an inspectable, defensible mastery model rather than a prompt |
| Educhain | https://github.com/satvik314/educhain | MIT | `main/LICENSE` | Python package for generative educational content — MCQs, lesson plans across 8 pedagogical approaches. The most direct library-level dependency on this shelf |
| Instructional Agents | https://github.com/DaRL-GenAI/instructional_agents | MIT | `main/LICENSE` | Multi-agent instructional design on the **ADDIE model** for automated course creation and evaluation; aimed explicitly at reducing teaching-faculty workload |
| K-12 Teacher Skills | https://github.com/anthropics/k12-teacher-skills | Apache-2.0 | `main/LICENSE` | The four agent skills shipped with Claude for Teachers plus their evaluation framework: lesson-plan creation, differentiation into tiered versions (below / at / above proficiency), lesson prep, grading support. Source and evals, not a product |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | `main/LICENSE` | Educational AI platform, Community Edition. 🟡 **Open-core:** its own README states CE is "the foundation for a proprietary Enterprise Edition". The BSD grant on CE is real and was read first-hand; the EE boundary is a commercial question, not a licence one |
| AI Teaching Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | `main/LICENSE` | Turns one Markdown teaching source into a reviewable Lab + Exam package and an optional 5–8 slide deck, with structured DSLs, human review and sandboxed evaluation. 🟡 Its README states MCP/agent expansion and automatic-grading productisation are **frozen** — the CLI is the live path |

## MCP tier — agents over the systems of record

### Agents over the systems of record

**19 rows in the table below**, reaching **six platforms** with a grant read first-hand — Moodle, Canvas, Open edX, **Brightspace/D2L, Blackboard and Google Classroom** (Anki is a retention store, not a platform). Counting this shelf whole, carried history included, **6 platforms** are reachable. 🟢 **Brightspace/D2L, Blackboard and Google Classroom appear on this shelf with a first-hand grant for the first time at p340** — previous passes carried them only on `agents/trending.md` because no lane had a grant read from the file. 🟢 **Four rows are institution-specific and therefore regionally placed**, which is a stronger placement than any inference from a commit footprint: a university's LMS tenancy is a fact about geography.

| Server | Repo | Licence | Grant read at | Platform reached |
|---|---|---|---|---|
| moodle-mcp | https://github.com/falkenslab/moodle-mcp | MIT | `main/LICENSE` | **Moodle.** ~230 Moodle tools under the **teacher's own login**, students anonymised to the model: grade with your rubrics, build a quiz from your question bank, answer the forum, see what is due. Docs in English **and Spanish** |
| canvas-mcp (vishalsachdev) | https://github.com/vishalsachdev/canvas-mcp | MIT | `main/LICENSE` | **Canvas.** Grant established by tree enumeration this pass |
| canvas-mcp (r-huijts) | https://github.com/r-huijts/canvas-mcp | MIT | `main/LICENSE` | **Canvas.** Second independent MIT Canvas rung, verified the same way |
| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | `master/LICENSE` | **Open edX.** 🔴 **AGPL-3.0 — the one copyleft row in this tier.** An MCP server is a separate program, but this one's own source is AGPL, so hosting a *modified* copy as a service owes that source. Deploy unmodified, or budget for the obligation |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT | `main/LICENSE` | **Anki** spaced-repetition store, so an agent can author and schedule retention material. 🔵 Its README now points most setups at the companion **addon** (`ankimcp/anki-mcp-server-addon`), which runs the server inside Anki with no Node.js or AnkiConnect |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | `main/LICENSE` | 🔴 **URL corrected at p343 — this row named the FORK (`kvnloo/tutor-mcp`, now 15 commits and two weeks behind) while this base's own `compose/code/p139-duplicate-lineage/` had already proved the lineage. Upstream: 467 c · 5 a · head 2026-10-16.** **No external platform** — a self-contained ITS engine. Maps a subject into a versioned skill graph with concepts, prerequisites and goals, then tracks learner state and review scheduling. The LLM generates; Tutor MCP remembers and recommends |
| brightspace-mcp-server | https://github.com/RohanMuppa/brightspace-mcp-server | MIT | `main/LICENSE` | **Brightspace / D2L.** 415 commits · **17 authors** · head 2026-10-20 — the largest contributor bench in the whole connector census. **Read-only by design** ("it never submits, edits, or deletes anything"), published to npm with CI |
| brightspace-mcp | https://github.com/JhostinAleck/brightspace-mcp | MIT | `main/LICENSE` | **Brightspace / D2L.** Multi-strategy authentication with **full MFA support**, a published documentation site, and a non-interactive `init` for CI and DevContainers. 🔵 The enterprise-shaped lane of the three |
| brightspace-d2l-mcp | https://github.com/AnonymousOnyx22/brightspace-d2l-mcp | MIT | `main/LICENSE` | **Brightspace / D2L.** Third independent MIT lane; 36 commits · 3 authors · head 2026-10-20 |
| blackboard-mcp | https://github.com/felipedias-ie/blackboard-mcp | MIT | `main/LICENSE` | **Blackboard Learn (Ultra).** 🔴 **Targets the INTERNAL Ultra API** — the surface the web UI itself calls, authenticated with a session cookie read from the user's browser — deliberately, because the documented REST API needs an OAuth app approved by the institution's Blackboard administrator. Exposes more than the public API (to-dos, activity stream, conversations, attendance) and is read-only in practice. 🟡 **An unsanctioned surface: no API contract, breakable without notice, and a terms-of-use question for a client deployment.** Use it to demonstrate reach, not as a supported integration |
| mcp-blackboard-ucsc | https://github.com/NiccoloSalvini/mcp-blackboard-ucsc | MIT | `main/LICENSE` | **Blackboard.** Second independent MIT Blackboard lane; 24 commits · 2 authors · head 2026-09-21 |
| google-classroom-mcp | https://github.com/pengusto/google-classroom-mcp | MIT | `master/LICENSE` | **Google Classroom, teacher-side** — prepares materials and assignments; 21 MCP tools, CI. 🟡 **Note the branch: `master`, not `main`** |
| classroom-mcp | https://github.com/OmarNiazi/classroom-mcp | MIT | `main/LICENSE` | **Google Classroom, student-side** and explicitly read-only: what is due, what has been turned in, teachers' announcements. Cannot submit, post or change anything |
| google-classroom-mcp (Aaradhya) | https://github.com/Aaradhya-Dev-Tamrakar/google-classroom-mcp | MIT | `main/LICENSE` | **Google Classroom.** Third MIT lane, Node ESM, aimed at autonomous agent fleets. Grant read first-hand; substance not clocked at p340 |
| mcp-usc | https://github.com/pablopc05/mcp-usc | MIT | `main/LICENSE` | 🟢 **EMEA — Spain.** The Campus Virtual (**Moodle**) of the Universidade de Santiago de Compostela, Spanish-language, with CI; acts only with the student's own account permissions. 🔵 **A permissive Moodle lane, so also a T25 counter-instance** |
| che-ntucool-mcp | https://github.com/psychquant/che-ntucool-mcp | MIT | `main/LICENSE` | 🟢 **APAC — Taiwan.** **NTU COOL**, National Taiwan University's **Canvas** deployment. 🟢 Every endpoint curl-tested against a real course before any code was written, and grade/announcement **writes are gated behind an explicit human confirmation** — the clearest human-in-the-loop design in this tier |
| ku-portal-mcp | https://github.com/sonaiengine/ku-portal-mcp | MIT | `main/LICENSE` | 🟢 **APAC — South Korea.** Korea University's **KUPID** portal, Korean-language, published to **PyPI** |
| uoft-quercus-mcp | https://github.com/skhdemo/uoft-quercus-mcp | MIT | `main/LICENSE` | 🟢 **North America — Canada.** University of Toronto **Quercus (Canvas)** via a personal access token, plus the public Timetable Builder for schedule and conflict checks. 🟡 States plainly that it is unaffiliated with U of T and may be rate-limited or blocked |
| classroom-mcp (sandraschi) | https://github.com/sandraschi/classroom-mcp | MIT | `main/LICENSE` | **No external platform** — a self-contained SIS, 45 MCP tools plus a REST API: students, classes, assignments, courseware, teaching-agent roles, and **framework-aware curriculum generation (CEFR, HSK, DELF, DELE, Goethe, JLPT)**. 🔴 **This base's own counting instrument files it under Google Classroom**, because `platform_of` matches the bare slug `classroom-mcp`; it reaches no Google surface. 🟡 Its README states test coverage beyond two regression tests is thin |

🔵 **Why this tier exists, and why it keeps growing while the agent tier does not.** Six of eight Tier-1 learning platforms are GPL or AGPL (see `repos/foundations.md`). An MCP server is a **separate program speaking a documented protocol**, so it carries none of the host platform's copyleft — which is why education's integration layer is consolidating on MCP rather than on plugins. The long tail is far larger than this table, and at p340 it is **measured rather than counted**: **93 distinct connector repositories probed first-hand** — Canvas 40, Moodle 21, Google Classroom 15, Blackboard 7, Brightspace/D2L 7, Open edX 2, Anki 1. 🔴 **Of those 93: 59 permissive, 4 copyleft, 23 with no licence path anywhere in their tree, 6 that no longer resolve, and 1 proprietary.** 🔴 **A quarter of this vertical's integration layer cannot be used in a deliverable at all**, and it fails silently, because an unlicensed repository looks exactly like a licensed one until someone reads the tree. 🔴 **Blackboard is the worst-served platform — 4 of its 7 connectors are ungranted.** The rows above are the ones whose grants are read from the file.

## Flagged-grant tier

**Two rows** that are useful and are **not** cleanly licensed for a client deliverable.

| Agent | Repo | Instrument | Read at | Why it is flagged |
|---|---|---|---|---|
| GenMentor | https://github.com/GeminiLight/gen-mentor | **CC0-1.0** | `main/LICENSE` | Reference implementation of the WWW 2025 Industry-Track paper on goal-oriented learning in an ITS: coordinated agents refine the goal, measure the gap to the learner's background, schedule sessions, write each session's reading and quiz, and rebuild the learner profile from behaviour. 🟡 **CC0-1.0 on a code repository is a public-domain dedication, not a software licence** — no patent grant and no warranty disclaimer, which is a different risk shape from MIT. Technically the best fit for the employability pattern (`compose/patterns.md` P6); have counsel clear it before it ships |
| mewcp-google-classroom | https://github.com/AStheTECH/mewcp-google-classroom | 🔴 **AStheTECH Community License (ACL)** — proprietary | `main/LICENSE.md` | A Google Classroom MCP server whose 6,489-byte `LICENSE.md` is a bespoke proprietary licence, read in full at p340. The grant is *"limited, non-exclusive, non-transferable, non-sublicensable, and **revocable**"*, for *"personal, educational, or internal business purposes"* only; redistribution is **non-commercial only**; and it expressly forbids, without written authorisation, selling or sublicensing, *"any hosted service, SaaS platform, API service, or similar commercial offering"*, white-labelling, and anything *"substantially similar to or competitive with AStheTech's offerings"*. 🔴 **Unusable for a consultancy in the exact shape that matters: a client deliverable is commercial, and hosting it for a client is the named prohibition.** 🔵 **Carried here rather than dropped because it is the one row in a 93-repository census that a naive "is it licensed?" check passes and a lawyer fails** |

## Declared refusals and gaps — probed, and not promoted

🔴 **`eth-lre/mathtutorbench` — exists, no grant anywhere in its tree.** A 10-path ladder returned 404 on all ten, and because a ladder is weaker evidence than a tree (`p275`), the claim was re-established by blobless clone + `git ls-tree -r HEAD --name-only` filtered for `licen[cs]e|copying|notice`: **zero candidate paths in the entire repository.** A credible ETH Zurich tutoring benchmark, *not* licensed for reuse until a grant appears. Named deliberately: dropping it silently would make an unlicensed repo look un-searched rather than unusable.

🔴 **`YL1N/EduGuardBench` — exists, no grant anywhere in its tree.** Same method, same result: zero candidate paths. An education-safety benchmark would be directly useful to this KB, which is why its absence is recorded rather than quietly skipped.

🔴 **`dmontgomery40/mcp-canvas-lms` — exists, no grant anywhere in its tree.** Carried on these shelves for many passes as a Canvas MCP row. Tree enumeration this pass returns no licence path at all, so it is **demoted** and the two MIT Canvas rungs above replace it.

🟡 **`withmarbleapp/os-taxonomy` is not an agent and not code.** Reported ~5 900 stars in an October 2026 trending roundup (third-party figure, recorded as such) for mapping ~1 590 micro-topics of primary/elementary learning as a connected graph. Its grant, read first-hand, is the **Open Data Commons Open Database License (ODbL)** — a *database* licence with share-alike reach over derived databases. It belongs in `repos/foundations.md` as a data asset and must not be treated as an MIT-style code dependency.

🔴 **The two prescribed supply legs returned no new education agent.** `top open source AI agents education 2026 github MIT` and `github trending education AI 2026` both returned general-purpose agents (OpenClaw, opencode, OpenHands, CrewAI, LangGraph, Hermes Agent) and AI *courseware* (`microsoft/generative-ai-for-beginners` MIT, `huggingface/agents-course` Apache-2.0, `karpathy/nanochat` MIT at `master/LICENSE`, `rohitg00/ai-engineering-from-scratch`). All of these **teach AI**; none **teaches with AI**, which is the boundary this shelf holds. This is the **tenth consecutive pass** at that result, and the structural cause is recorded in `repos/trending.md`: **GitHub Trending has no education category**, so an unfiltered leg cannot surface a vertical.

🔵 **What did move came from narrower legs.** The dated releases on DeepTutor (2026-10-19) and OpenMAIC (2026-10-18), and the two MIT Canvas rungs, were found by probing known rows' release feeds and enumerating candidate trees directly — not by the trending channel. **In a vertical with no trending category, supply news arrives through incumbents' release feeds.**

### Regional note on this shelf

Most rows above are **Global** in reach and not region-locked by licence or hosting. Two carry a regional accent worth recording: **moodle-mcp** ships Spanish-language documentation alongside English, which matters for LATAM and Iberian deployments, and **OpenMAIC** is a Tsinghua project whose web-search providers default to Kimi and DeepSeek — an APAC-native stack, and a data-residency question in an EMEA review exactly as a US-hosted model is in a Chinese one. Residency now cuts both ways.

🟢 **New at p340 — four rows that are genuinely placed, not merely accented.** `mcp-usc` (**EMEA**, Universidade de Santiago de Compostela), `che-ntucool-mcp` (**APAC**, National Taiwan University), `ku-portal-mcp` (**APAC**, Korea University) and `uoft-quercus-mcp` (**North America**, University of Toronto). 🔵 **These are placed by the institution they connect to, which is a fact about geography rather than an inference from a commit footprint** — the method this base has been missing since p334 recorded that its supply arrives with no region attached. For an engagement they are worked, MIT-licensed precedents for a specific institutional seam: a European Moodle tenancy, an APAC Canvas tenancy with a human-confirmation gate already designed in, and a North American Canvas tenancy with a personal-access-token model.

🔴 **LATAM remains unplaced on this shelf, and p340 probed two candidates to say so.** `idavi/usp-mcp` (Universidade de São Paulo by its slug) **does not exist** — `git ls-remote` returns no refs — and `DaviPac/Classroom-mcp`, whose Portuguese README references **SIGAA**, the academic system of Brazilian federal universities, has **no licence path in its tree and two commits, both authored `Claude <noreply@anthropic.com>` at `+0000`**. 🔵 **The informed form of the gap: LATAM's absence in this layer is not an absence of LATAM institutions but an absence of *published* connectors to them.**

---

## ⏷ Carried history — everything below this line predates Pass 339 and was NOT rewritten

🟢 **Pass 339 prepends; it does not replace.** An earlier draft of this pass replaced these shelves outright and `gate-permissive-arm` caught the cost: the corpus lost ~1.2 MB of first-hand-verified rows and the `MIT`+`Apache-2.0` cell count fell from 7 000+ to 6 597. 🔵 **Deleting verified rows is not curation** — the live section above carries this pass's findings, and every prior pass's verified shelf stands underneath it.

## Pass 338 · 2026-10-20 (eleventh pass of this date) — two passes were spent repairing the ladder's CASE axis, and the grant that actually defeats the ladder was already on these shelves, defeating it on DEPTH

🟢 **`ACTION ZF` closed first, before a byte was written.** Both suites were run, not inherited.

| suite | 🟢 at pass open | 🟢 at pass close |
|---|---|---|
| `make hooks` | 🟢 **22/22 — all green** (p337's repair holds) | 🟢 **23/23** — one gate ADDED to the tier, below |
| `make gate-offline` | 🟢 all pass · `lazy-quantifier lint: 0` | 🟢 all pass · `lazy-quantifier lint: 0` |
| `p383` region-heading gate | 🔴 **NEVER RUN — not wired into any target** | 🟢 **wired, and the live shelf brought to green** |

---

### 🔴 FINDING 0 — the licence question p337 registered as *"the next licence question for this tier"* was answered on this base's own shelves 72 passes earlier, and the hash matches

🔴 **`intel/market.md`, written one pass ago, carries this:** *"two separate comparison pages list **Forma LMS** as Apache-2.0 and as GPL-v2 respectively. 🟡 Unresolved — not probed this pass, and not published as either. Registered as the next licence question for this tier."*

🟢 **Measured first-hand this pass, on the two channels `ACTION ZM` names:**

| channel | measurement |
|---|---|
| `git ls-remote --symref` | 🟢 resolves · default branch **`master`** · `HEAD 446a77a9b9cbb20dacf008a2d53b2658fb5f5634` |
| `raw.githubusercontent.com` | 🟢 **HTTP 200** at **`html/license.txt`** · **18 346 B** · title line *GNU GENERAL PUBLIC LICENSE, Version 2, June 1991* · `sha256`₁₆ **`4e63feff285d9215`** |

🔴 **This base has carried exactly that value since `p265`, and `p276` reproduced it independently by tree enumeration — same path, same 18 346 B, and the hash I measured today is the hash on the shelf.** The question was not open. **It was answered, twice, and re-registered as open anyway.**

🔵 **Why this is a class and not a slip.** p334 named it, p337 logged the fifth instance, and this is the sixth: **the capability exists, the answer is already written down, and nothing in the pass path reads the base before declaring a question open.** 🟡 `gate-absence` (`ACTION p279`) exists precisely to stop this — but it governs **absence** claims (*"X has no grant"*), and p337 did not publish an absence. It published an **open question**, which no gate types. 🟢 **`ACTION ZO` registers the missing shape: a pass may not register a licence question as OPEN without first grepping the corpus for the slug. An unresolved question is a claim about THIS BASE, and it is falsifiable from the base alone, offline, in one command.**

---

### 🔴 FINDING 1 — the reason the question LOOKED open: the sanctioned instrument cannot reach that grant, and the axis it cannot reach is DEPTH

🟢 **`compose/code/lib/probe_payload.sh` has exactly two channels, and `formalms/formalms` defeats BOTH:**

| channel | why it fails on this specimen | measured |
|---|---|---|
| the 42-rung case-varied ladder (`ACTION ZL`) | 🔴 **every rung is a BARE FILENAME.** `probe_ladder()` emits `license`, `LICENSE`, `License.txt`, `COPYING` … — **root-level, all of them.** No amount of case variation reaches a path with a `/` in it | 🔴 `LICENSE`, `LICENSE.txt`, `license.txt`, `COPYING` all **HTTP 404** on `master` |
| the README-link fallback (`_readme_license_path`, the library's own depth mitigation) | 🔴 requires the README to **name** the licence; it greps `licen[sc]e\|copying` over the README's markdown links | 🔴 the README is **6 198 B** and contains **ZERO** occurrences of `licen[sc]e` — *not* zero links, **zero occurrences of the word** |

🔴 **So the only sanctioned instrument returns an ABSENCE for a repository whose 18 346 B GPL-2.0 grant answers HTTP 200.** p336 and p337 spent two consecutive passes widening the ladder's **case** axis — 7 rungs → 24 → 42 — and the specimen that actually defeats it was sitting on `verticals/solutions.md` the whole time, defeating it on **path depth**, where the ladder has no rung at all and never had one.

🟡 **The library's own header already knew.** Note 2, written at Pass 15 on 2026-10-06: *"THE LICENCE CAN LIVE IN A SUBDIRECTORY, MIXED-CASE. Measured: `OS4ED/openSIS-Classic` keeps GPL-2.0 at `docs/License.txt` … So the README link is tried BEFORE the long ladder."* 🔴 **The mitigation was written down and its PRECONDITION was never measured.** Measured now, on the only two depth specimens this corpus holds:

| depth specimen | grant, re-read this pass | README names a licence? | 🔴 does the mitigation fire? |
|---|---|---|---|
| `OS4ED/openSIS-Classic` | 🟢 **GPL-2.0** · `master/`**`docs/License.txt`** · **17 286 B** | 🟢 **yes — 2 occurrences** | 🟢 **fires.** This is the specimen it was built for |
| `formalms/formalms` | 🟢 **GPL-2.0** · `master/`**`html/license.txt`** · **18 346 B** | 🔴 **no — 0 occurrences** | 🔴 **cannot fire.** Depth coverage is 0 here |

🟢 **1 of 2.** The depth channel is conditional on prose a maintainer had no obligation to write, and on this corpus's own specimens it covers half of them.

🟢 **`ACTION ZN`: an absence verdict may not be published from the root ladder and the README link alone. Depth must be excluded — by tree enumeration (`ACTION p275`, `make enumerate`, which is how `p276` got both rows right), or by the prefix ladder this pass measured. `ACTION ZL` governs CASE; `ZN` governs DEPTH; neither implies the other.**

---

### 🟢 FINDING 2 — the audit the new action demands, run over every published absence, WITH its negative control: no published absence is false

🟢 **Every row this base currently publishes as having no grant was re-probed on the depth axis** — 10 prefixes × 8 stems = **80 paths per repository**, plus the README word-count channel. 🔵 **The prefixes are the shapes THIS CORPUS has measured** (`docs/`, `html/`, `licenses/`, `legal/`, `src/`, `lib/`, `app/`, `web/`, `LICENSES/`) plus the GitHub convention `.github/` — not a combinatorial set bought for its own sake.

| 🟢 positive control | expected | measured this pass |
|---|---|---|
| `formalms/formalms` | `html/license.txt`, 18 346 B | 🟢 **hit, 18 346 B, GPL-2.0** — the byte count on the shelf |
| `OS4ED/openSIS-Classic` | `docs/License.txt`, 17 286 B | 🟢 **hit, 17 286 B, GPL-2.0** — the byte count on the shelf |
| 🔴 `gmilano/definitely-not-a-real-repo-p338` (invented) | must not resolve | 🟢 **`UNRESOLVED`** — the instrument discriminates |

🟢 **The eleven published absences, re-probed:**

| row published as ungranted | default branch | depth axis, 80 paths | README names a licence? |
|---|---|---|---|
| https://github.com/dmontgomery40/mcp-canvas-lms | `main` | 🟢 **no nested grant** | 🟡 **2** — the `DECLARED-ONLY` specimen; points at a `LICENSE` it does not ship |
| https://github.com/likr/canvas-lms-agent | `master` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/studiolxd/xapi | `main` | 🟢 **no nested grant** | 🟡 **1** |
| https://github.com/risnake/canvas-mcp-server | `main` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/mthatipamula/educational-assessment-ai-agent-platform | `main` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/oseducation/knowledge-graph | `main` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/Kyyota-Wang/cloverailab | `main` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/010Ankushsharma/AdaptaLearn | `master` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/YL1N/EduGuardBench | `master` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/razi-03/NCERT-CKG | `main` | 🟢 **no nested grant** | 🔴 **0** |
| https://github.com/Willie-Liao/lesson-library | `main` | 🟢 **no nested grant** | 🟡 **1** |

🟢 **11 of 11 survive. ZERO false absences.** The hole `FINDING 1` proves is real, and **it has not yet cost this base a single published row** — which is a measurement worth exactly as much as a catch would have been, and is stated here instead of a catch because it is what the instrument returned.

🔴 **But read the last column, because it prices the exposure going forward.** The README mitigation can fire on **3 of these 11**; for **8 of 11**, depth coverage rested entirely on a channel that *cannot* fire. 🔵 **The two rows that WERE at depth are right only because `p276` reached them with a different instrument — tree enumeration — which has never been in the path that publishes an absence.** That is the gap `ACTION ZN` closes.

---

### 🔴 FINDING 3 — the gate that enforces the task contract's own region rule has a 100%-passing test suite and has NEVER been wired into a target

🔴 **The engagement contract says, verbatim:** *"In `intel/market.md`, opportunities go under a single `## Opportunities by region` heading with one `###` subsection per region. Never write a LATAM-only section."*

🟢 **An instrument for exactly that exists: `compose/code/p383-region-heading-gate/check_headings.py`**, with four typed findings (`P383-MULTIPLE-BLOCKS`, `P383-OUT-OF-VOCAB`, `P383-MISSING-REGION`, `P383-LATAM-ONLY`), a `P541` no-input refusal, and its own passing suite. 🔴 **`grep -n p383 Makefile` returns NOTHING.** It is in no target — not `hooks`, not `gate-offline`. **`make hooks` 22/22 green has never said one word about region headings.**

🔴 **Run against the live shelf for the first time, it fails immediately:**

| finding | count | what it is |
|---|---|---|
| `P383-MULTIPLE-BLOCKS` | 🔴 **4** | **5 canonical blocks** in `intel/market.md` (lines 23, 77, 150, 265, 1015) — one per pass that wrote one. The contract asks for **1** |
| `P383-MISSING-REGION` | 🔴 **2** | `Global` absent from the blocks at lines 23 and 77 — and `Global` is in the closed vocabulary |
| `P383-OUT-OF-VOCAB` | 🔴 **14** | prose `###` headings adopted as region children because they follow a canonical `##` |

🔵 **This is `P471` wearing a third hat, and this base has named it twice already** — *"a gate that passes all its checks without judging anything."* p115 caught five Python gates that could not run under `python3 -I`; p541 caught this very gate printing `total 0` on no input. 🔴 **Neither noticed that the gate is not invoked at all.** A suite that passes proves the instrument works; it proves nothing about whether anything calls it.

🟢 **Both halves fixed in this pass, and the fix is wiring plus structure, not research:**
1. `p383` is now a **first-class member of the `hooks` tier** — 22 gates → **23**, so a future pass cannot reintroduce a second canonical block without going red.
2. `intel/market.md` now carries **ONE** canonical `## Opportunities by region` block with exactly the **five** closed-vocabulary children. The four historical blocks are **relabelled, not deleted** — `## Opportunities by region — p337 (superseded)` and so on — so the history stays readable while only the live block claims the canonical heading. 🔵 **`intel/market.md` is not one of the two append-only files**; the two that are (`agents/trending.md`, `repos/trending.md`) were not touched by this restructure.

🟢 **`ACTION ZP`: an instrument is not a gate until a target invokes it. Any pass adding a gate adds it to a target in the same pass, and `grep -c '<gate-dir>' Makefile` is the check.**

🔵 **One regression of my own, caught by this base's gates inside the pass and recorded rather than quietly fixed:**

| what I did | which gate caught it | 🟢 resolution |
|---|---|---|
| wired `p383` into `HOOK_GATES` and wrote the prose, without touching the coverage census that counts which suites are gated | 🔴 **`p252-ungated-floors`** — `make gate-offline` went RED: *"ungated AND explicit-exit (immune by construction) … got: 109"*, expected 110 | 🟢 **The census was RIGHT, and the pin moved 110 → 109 with the reason recorded in the file.** `p383`'s suite was ungated **and** explicit-exit, never silent-zero, so it leaves the *immune* half: `ungated` 181 → 180, explicit-exit 110 → 109, 🟢 **and the XR silent-zero backlog stays at 71** — no better, no worse than p332 left it |

🔵 **This is the second instance of the door `p294` documented** — *"it left the population by the only door that was ever supposed to exist: it became gated"* — and the **fifteenth consecutive pass** in which this census went red before the prose did. 🟢 **It is also p294's shape run forwards:** p294 proved the pin catches a suite *leaving* the backlog, which is the direction a coverage census must never miss, because **a suite leaving silently would read as progress.** Here it left legitimately, and the census still made the pass prove it.

---

### 🟢 The tier re-read first-hand this pass — 9 agent rows, every grant re-measured on both axes, zero drift

🟢 **Grant read on `raw.githubusercontent.com` at a branch resolved by `git ls-remote --symref`.** Per `ACTION ZD` the channel is recorded, not just the value. 🔵 **The `axis` column is new this pass**: it says whether the grant was found at the repository root or at depth — the distinction `FINDING 1` shows the old instrument could not make.

| Agent / tool | Repo | Grant, re-read this pass | Bytes · branch · path | Axis | What it is |
|---|---|---|---|---|---|
| **uis-mcp-server** | https://github.com/SidneyBissoli/uis-mcp-server | 🟢 **MIT** | 1 088 · `main` · `LICENSE.md` | 🟢 root | UNESCO Institute for Statistics education data over MCP; the LATAM supply row placed at p337 |
| **h5p-cli** | https://github.com/h5p/h5p-cli | 🟢 **MIT** | 1 066 · `master` · `LICENSE` | 🟢 root | Command-line tooling for H5P interactive content — the authoring spine of the EMEA stack |
| **hyperbook** | https://github.com/openpatch/hyperbook | 🟢 **MIT** | 1 069 · `main` · `LICENSE.md` | 🟢 root | Markdown→interactive-courseware generator; H5P-aware, static output |
| **h5p-offline-player** | https://github.com/missing-elements/h5p-offline-player | 🟢 **MIT** | 1 073 · `main` · `LICENSE` | 🟢 root | Plays H5P content with no server — the low-connectivity deployment answer |
| **zenbrain** | https://github.com/zensation-ai/zenbrain | 🟢 **Apache-2.0** | 11 357 · `main` · `LICENSE` | 🟢 root | Spaced-repetition / learning-algorithm library; canonical Apache payload, `GRANT` on `p307` |
| **moodle-driver** | https://github.com/falkenslab/moodle-driver | 🟢 **MIT** | 1 067 · `main` · `LICENSE` | 🟢 root | Programmatic Moodle driver; 🟡 shelved amber — 320 commits in nine days, one author |
| **h5p-theme-picker** | https://github.com/otacke/h5p-theme-picker | 🟢 **MIT** | 1 073 · `master` · `LICENSE` | 🟢 root | H5P theming; title line reads `The MIT License` |
| **yanki** | https://github.com/kitschpatrol/yanki | 🟢 **MIT** | 1 071 · `main` · `license.txt` | 🟢 root, **lowercase** | Markdown→Anki flashcard sync; the p336/p337 case casualty, and still the only lowercase grant in the tier |
| **OATutor** | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1 105 · `main` · `LICENSE` | 🟢 root | Berkeley CAHL intelligent tutor; **BKT is explainable**, which is what a school board can audit |

🟢 **Nine of nine re-read, and every byte count is the one already on the shelf** (1 088 · 1 066 · 1 069 · 1 073 · 11 357 · 1 067 · 1 073 · 1 071 · 1 105). 🔵 **No drift in the agent tier this pass** — stated as a measurement, because a re-read that finds nothing is the only thing that licenses the shelf to stand unchanged.

---

### 🟡 Discovery: 0 new promotable rows — the NINTH consecutive such measurement, and saturation again, not silence

🟢 **All four prescribed global legs run verbatim, plus one extra leg bought deliberately because the prescribed four are saturated:**

| leg, run verbatim 2026-10-20 | result |
|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **0 new.** General-agent listicles. The only education rows are courseware: `microsoft/ai-agents-for-beginners`, `pguso/agents-from-scratch`, `rohitg00/ai-engineering-from-scratch` — 🟢 **all three already named on these shelves** (232 · 160 · 230 corpus mentions). One source's own caveat repeats: *"some projects marketed as open source are actually source-available."* |
| `github trending education AI 2026` | 🔴 **0 new.** No education category exists on GitHub Trending; the hits are AI-courseware repos, all carried |
| `open source platform education ERP CRM MIT Apache` | 🔴 **0 new**, and the vendor-SEO shape p222 and p328 both recorded recurs: **5 of 9 results were `openeducat.org` glossary pages in 5 languages.** 🟢 Re-confirmed: **OpenEduCat is LGPL-3.0**, not MIT or Apache — the leg's own phrasing presumes a platform that does not exist |
| `AI education industry trends 2026` | 🟡 **Market sizes conflict irreconcilably across publishers** — $6.4B (2025)→$79.6B (2034) vs $7.52B (2025)→$10.6B (2026) vs ~28% CAGR to 2036. 🔴 **Not publishable as a figure; recorded as a conflict**, which is what p337 did with the same leg |
| 🔵 **extra leg** · `new open source education AI agent MCP server October 2026 Moodle Canvas grading` | 🔴 **0 new.** Returned `vishalsachdev/canvas-mcp`, `csmediapro/moodle-mcp-server`, `peancor/moodle-mcp-server` — 🟢 **3 of 3 already `CARRIED`**. Buying a leg outside the prescribed four did not break the saturation |

🔵 **Nine consecutive passes at zero is now a property of the channel, not of the passes.** The honest reading stays p337's: this is a channel whose education-agent supply this base has absorbed. **Fewer real rows beat padding, and an informed gap is information.**

🟢 **One third-party claim CONFIRMED by the byte channel — the rarer direction, and worth recording because this base usually records the opposite.** A directory listing asserted `csmediapro/moodle-mcp-server` is AGPL-3.0. Re-read first-hand: `main/LICENSE`, **34 523 B**, *GNU AFFERO GENERAL PUBLIC LICENSE* — 🟢 agreeing with the directory **and** with this base's own cell. 🔵 And 34 523 B is byte-identical to `overhangio/tutor`'s AGPL-3.0 payload on `repos/foundations.md`, which is an independent cross-check on the canonical AGPL-3.0 text.

## Pass 337 · 2026-10-20 (tenth pass of this date) — the gate that has been red since p331 was never a number: it was `p332` wiring a case-blind instrument into the hook tier, and it had made every absence claim on these shelves unpublishable

🟢 **`ACTION ZF` closed first, before a byte was written.** Both suites were run, not inherited.

| suite | at pass open | 🟢 at pass close |
|---|---|---|
| `make hooks` | 🔴 **21/22 · RED `gate-ladder-case`** (sixth pass) | 🟢 **22/22 — ALL GREEN** |
| `make gate-offline` | 🟢 all pass · `lazy-quantifier lint: 0` | 🟢 all pass · `lazy-quantifier lint: 0` |
| `p283` controls | 25/25 | 🟢 **28/28** (three new arms, below) |

---

### 🟢 FINDING 0 — the red gate is CLOSED, and its cause was a one-line hook wiring six passes ago

🔴 **p334, p335 and p336 all read `gate-ladder-case` as a ratchet breach — `STANDING:CASE-UNVARIED` 8 over ceiling 7, `STANDING:SINGLE-SPELLING` 20 over ceiling 17 — and none of them asked WHICH instrument moved.** p336 went further and proved the counts were not its own prose. 🟢 **Measured this pass, decisively, with a `git worktree` of `b5f081b^` — the commit before p332:**

| population, measured on a clean worktree | `STANDING:CASE-UNVARIED` | `STANDING:SINGLE-SPELLING` |
|---|---|---|
| `b5f081b^` — immediately **before** p332 | 🟢 **7** | 🟢 **17** |
| ratchet ceilings in `ratchet.tsv` | **MAX 7** | **MAX 17** |
| `HEAD` at this pass's open | 🔴 **8** | 🔴 **20** |

🟢 **The pre-p332 counts are not near the ceilings — they ARE the ceilings.** The whole breach is `+1` and `+3`, and `compose/code/p332-delivery-audit/delivery_audit.py` carries **exactly** four ladders: `licence` **CASE-UNVARIED**, and `copying` / `notice` / `readme` **SINGLE-SPELLING**. 🔴 **Cause: commit `b5f081b` (p332) wired `delivery-audit` into `make hooks`, and in doing so moved a case-blind instrument into the STANDING population.** Nothing regressed; a gate acquired a new subject.

🔵 **And the ratchet's own header predicted this shape and still missed it.** `ratchet.tsv` says a ceiling over the ALL population *"goes red when an instrument is ADDED, which is the p252 defect again"*, and scopes ceilings to `STANDING:` to avoid it. 🔴 **Adding an instrument to `make hooks` does the same thing to the STANDING population.** The ceiling moved risk by zero and spent six passes of attention.

**🔴 Why it was never just bookkeeping.** All four ladders come from ONE `DENY_SECOND` set, and every comparison against it ALREADY folded its input — `second.lower() in DENY_SECOND`, about a hundred lines below the literals. The match was case-insensitive **in fact**. `p283`'s screen is deliberately blind to a distant fold (`_near`, window=2; its **C5** control asserts exactly that a distant `.lower()` confers no immunity). 🟢 **Fix: fold at the point of DEFINITION** — `DENY_SECOND = {w.lower() for w in (…)}`. The set is **byte-identical** (18 entries, asserted against the pre-fix literal set), behaviour is unchanged, and the invariant is now stated where the words are, so a later pass may add `LICENSE.TXT` without creating a rung the comparison would miss. All four ladders regrade **FOLD-ON-PATH**: `CASE-UNVARIED` **8 → 7**, `SINGLE-SPELLING` **20 → 17**. 🟢 **No ceiling was touched.**

---

### 🔴 FINDING 1 — `ACTION ZL` was unsatisfiable as written: the shared probe every pass sources was typed `CASE-UNVARIED`, so NO absence could lawfully be published from it

🟢 p336 wrote `ACTION ZL`: *no pass may publish `UNGRANTED` from a ladder `gate-ladder-case` types `CASE-UNVARIED`.* 🔴 **`compose/code/lib/probe_payload.sh` — THE shared probe library, the one `lib/README.md` forbids rewriting — was typed exactly that.** Its ladder was `LICENSE LICENSE.md LICENSE.txt LICENCE COPYING COPYING.txt COPYING.TXT`: **uppercase on every stem.** So ZL forbade the verdict and the only sanctioned instrument for reaching it could not satisfy ZL. **The action was a dead letter on arrival.**

🔴 **And this file's own header carried the refuted claim that put it there.** Trap 3 records pass 14 pricing *"the full 20-name case ladder at 0 payouts in 98 repos"* and telling the next pass not to re-buy it. 🟢 **p336 bought one rung by hand and it paid immediately** — `kitschpatrol/yanki` ships **lowercase `license.txt`**, 1 071 B, `MIT License`, a real 474-commit project the uppercase ladder had refused. **A 0-payout price measured once is a prior, not a proof, and one counterexample refutes the generalisation it was used to justify.**

🟢 **The ladder is now GENERATED and case-varied on both halves** — 42 unique rungs, stem × casing × extension, with the measured-fast rungs emitted FIRST. **The economics that justified the short list are preserved exactly, because `probe_repo` returns on the first hit:**

| repository shape | requests paid |
|---|---|
| conventional `LICENSE` | 🟢 **1** — unchanged |
| lowercase `license.txt` (the p336 casualty) | 🟢 **8** — reachable at all, for the first time |
| about to be written down as **having no grant** | up to **42** — the full ladder, which is precisely the verdict `ACTION ZL` governs |

🟢 **The cost is paid only where the error is expensive.** Re-probed first-hand: `kitschpatrol/yanki` → `main/license.txt`, **1 071 B**, **MIT**, © Eric Mika. 🟢 `probe_payload.sh` now grades **GENERATED-CASE-VARIED** on all three families, and `STANDING:CASE-UNVARIED` falls to **6**, one below ceiling.

🔵 **Two of my own regressions, caught by this base's gates inside the pass and recorded rather than quietly fixed:**

| # | what I wrote | which gate caught it | 🟢 resolution |
|---|---|---|---|
| 1 | piped only the `for` loop to `awk`, leaving the 7 fast rungs **outside** the de-duplicator | 🟢 running it — ladder came back **82 rungs, all 7 duplicated** | one pipeline; 42 unique, fast rungs keep their measured order |
| 2 | derived casings with `upper=$(printf … \| tr …)` | 🔴 **`p253-captured-body-census`** graded the file **BODY-ONLY** and `gate-offline` went **RED** | 🟢 `${stem^^}` / `${stem^}` — **no subshell at all**: two fewer forks per stem, census CLEAN, and the idiom `p283` already reads |
| 3 | a 7-line comment I put **between** the `tr` and the extension list it feeds | 🟢 `p283` kept typing the file `CASE-UNVARIED` while it provably walked 42 case-varied rungs | comment hoisted above the function — **prose does not get to separate the two halves of a generator it describes** |
| 4 | wrote *"Harvard/MIT origin"* in the `edx-platform` row of `verticals/solutions.md` | 🔴 **`gate-shelf-consistency`** — `openedx/edx-platform: AGPL-3.0 (repos/foundations.md:13) vs MIT (verticals/solutions.md:13)` | 🟢 token removed. **`MIT` the university is `MIT` the licence to any shelf reader, and a word-boundary guard does not help — `Harvard/MIT` passes one.** The only fix is not writing the token in a row |

🟢 **Regression 2 is the sharper one: the census was RIGHT.** `$( )` around a content producer is a captured body by its own `capture_shape`, and the census cannot know my capture held a filename stem rather than a payload. The fix was not to annotate the exception — it was to stop needing one.

---

### 🟢 FINDING 2 — the fourth instance of p284's generator finding, and the arm that had been open longest

🔴 `p283` could not see a shell generator that **derives** its stem casings. p284 closed this for a Python cross product (`_STEM_VARY`: `_casings(`, `stem.upper()`), p286 for a shell `for` **list**, p288 for a ladder read by **reference** — all three cover a generator whose variants are literal somewhere. **A `tr`-derived casing has no literal to read**, so `stem_varies` stayed False forever. 🟢 **New arm `_SH_STEM_VARY`, kept exactly as narrow as the Python one: the idiom counts only when it sits within 8 lines of the case-varied extension list already required. Proximity, not presence.** Guarded by three new controls:

| control | arm | asserts |
|---|---|---|
| **C33** | positive | a `tr`-derived stem × case-varied ext list is `GENERATED-CASE-VARIED` |
| **C34** | 🔴 negative | a **bare** `tr` with no case-varied ext list is **not** a generator |
| **C35** | 🔴 negative | a **distant** `tr` does not generate the stems — C5's rule, on the new axis |

🟢 **28/28.** Corpus effect, measured: `probe_payload.sh` promoted on 3 families; `STANDING:CASE-CLOSED` **9 → 8** and `ALL:CASE-CLOSED` **25 → 24**, because the `copying` ladder was promoted OUT of `CASE-CLOSED` into the stronger `GENERATED-CASE-VARIED`. 🟡 **Both land exactly on their `MIN` floors (8 and 24).** The ratchet counts a promotion to a stronger grade as a loss on the weaker one — a real wrinkle, recorded and NOT papered over by moving a floor. A later pass that promotes one more closed ladder will go red on a floor for a good reason, and should read this paragraph before touching `ratchet.tsv`.

---

### 🔴 FINDING 3 — the prescribed `curl -sI` verification is INVALID in this environment, and reads as a 404 to anyone who does not run the negative control

The task contract says *"verify every URL before writing it (`curl -sI`). A 404 is not a finding."* 🔴 **Measured this pass, with the negative control that decides it:**

| slug | `curl -sI https://github.com/…` | 🟢 `git ls-remote` |
|---|---|---|
| `moodle/moodle` (exists, 35 147 B grant) | 🔴 **403** | 🟢 **RESOLVES** |
| `kitschpatrol/yanki` (exists, MIT) | 🔴 **403** | 🟢 **RESOLVES** |
| `gmilano/definitely-not-a-real-repo-p337` (**invented**) | 🔴 **403** | 🟢 **NO-REFS** |

🔴 **The HTML HEAD channel returns 403 for everything, including a slug that does not exist. It carries ZERO bits.** A pass that follows the instruction literally would refuse the entire corpus. 🟢 **`git ls-remote` discriminates perfectly, and `raw.githubusercontent.com` returns 200/404 correctly — those are the two channels every verdict on this shelf is read through, and `p798-proxy-refusal-ledger` is where this class already lives.** 🟢 `ACTION ZM`: **no pass may treat a `github.com` HTML status as existence evidence; existence is `ls-remote`, grant is `raw`.**

---

### 🟡 Discovery: 0 promotable rows — the eighth consecutive such measurement, and this time the reason is SATURATION, not silence

🟢 The one prescribed leg that returned education-specific repositories at all (`open source AI tutor agent github 2026 MCP server Moodle Canvas LMS`) yielded 8 candidate slugs. 🔴 **Six were already `CARRIED`** — `csmediapro/moodle-mcp-server`, `G36maid/moodle-mcp`, `bruchris/canvas-lms-mcp`, `vishalsachdev/canvas-mcp`, `CharlieCardenasToledo/mcp-canvas-server`, `peancor/moodle-mcp-server`, plus `EduBase/MCP` and `withmarbleapp/os-taxonomy`. 🟡 **Two were new, both grant-verified first-hand, and both refused on activity:**

| row | grant, read first-hand | activity, bare-clone channel | region, placed | 🔴 verdict |
|---|---|---|---|---|
| `aicoder2009/khanacademyMCP` | 🟢 **MIT** — `main/LICENSE`, **1 086 B**, © *Khan Academy MCP Contributors* | 🔴 **10 c · 1 a · 2026-03-11 → 2026-07-07** — nothing for **three months** | 🟢 **North America** — `-0700(10)`, US Pacific | 🔴 **REFUSED-BELOW-BAR** (10 commits) + stale |
| `Mattlo0546/canvas-mcp` | 🟢 **MIT** — `main/LICENSE`, **1 067 B**, © 2026 Mattlo0546 | 🔴 **2 c · 2 a · both on 2026-10-19** — one day old | 🟢 **EMEA** — `+0100(2)` | 🔴 **REFUSED-BELOW-BAR** (2 commits) |

🔵 **Read precisely: this is not a dry channel, it is a channel whose education-agent supply this base has already absorbed.** 6 of 8 carried is the opposite signal from 0 of 8 found, and it is worth more than a padded row. **Fewer real rows beat padding, and an informed gap is information.**

## Pass 336 · 2026-10-20 (ninth pass of this date) — the shelf gate types a 682-byte Apache **appendix** as a full grant, and the instrument that gets it right has been in this repo since p307

🟢 **`ACTION ZF` CLOSED — the gates were MEASURED this pass, not inherited.** p335 could not execute and honestly refused to restate p334's numbers. This pass ran both suites first, before touching a byte:

| suite | result, measured 2026-10-20 | delta p334 → p336 |
|---|---|---|
| `make hooks` | 🔴 **21/22 green · RED: `gate-ladder-case`** | 🟢 **no change** — p334's reported state held across two passes it was never measured in |
| `make gate-offline` | 🟢 **ALL OFFLINE LICENCE CONTROLS PASS** · `lazy-quantifier lint: 0 findings` | 🟢 no change |

🔵 **So p334's inherited figure was correct.** That is worth recording precisely because p335 was right not to assume it: the claim is now observed, and `gate-ladder-case` is red on its C14 ratchet for a third pass.

---

### 🔴 FINDING 0 — the gate three passes inherited as RED was describing a live defect, and this pass walked into it

🔴 **`gate-ladder-case` has been red since p331.** p334 reported it, p335 inherited it without measuring, and neither acted on what it says: **which path ladders can find an uppercase extension.** This pass ran its first probe sweep on an all-uppercase ladder — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT` — and **published a refusal that was false.**

| row | first verdict, uppercase ladder | 🟢 verdict on a case-varied ladder | cost of the error |
|---|---|---|---|
| `kitschpatrol/yanki` | 🔴 `REFUSED-UNGRANTED` — *"no licence file on 6 paths"*, logged as the **ninth instance** of p335's DECLARED-ONLY class | 🟢 **MIT** — `main/`**`license.txt`**, **lowercase**, **1 071 B**, `MIT License`; confirmed in the HEAD tree (`git ls-tree` → `license.txt`) and by `package.json` `license: MIT` | 🔴 **A real 474-commit MIT project refused, and a defect class inflated by a phantom instance** |

🔴 **Corrected within this pass: the ratchet is NOT mine.** My first draft claimed this pass's prose pushed the counts over. 🟢 **Measured instead of assumed** — a `git worktree` of clean `HEAD` reports **`STANDING:CASE-UNVARIED=8`, `STANDING:SINGLE-SPELLING=20`**, byte-identical to the working tree, and `git status` shows this pass touched **no file under `compose/code/`**. 🟢 **The regression predates p336; p334 and p335 reported the red correctly.** What this pass adds is not the count — it is **the first live casualty of the vocabulary the count is about.**

🔴 **And what the gate names is not cosmetic.** `make ladder-audit` grades **658 ladders across 363 instruments, 121 standing**. The standing `CASE-UNVARIED` licence ladders include the ones that matter most:

| instrument | grade | its ladder |
|---|---|---|
| 🔴 `compose/code/lib/probe_payload.sh` | **CASE-UNVARIED** | `LICENCE LICENSE LICENSE.md LICENSE.txt` — **the shared probe library** |
| 🔴 `compose/code/p228-shelf-gate/classify_grant.py` | **CASE-UNVARIED** | `LICENCE LICENSE` — **the shelf gate itself** |
| 🔴 `compose/code/p279-absence-claims/absence_claims.py` | **CASE-UNVARIED** ×2 | `licence license` — 🔴 **the gate whose entire job is to stop a pass publishing a false absence** |
| 🔴 `compose/code/pass275-grant-enumeration/enumeration_gate.py` | **CASE-UNVARIED** | `LICENSE LICENSE.md LICENSE.rtf license` |
| 🔴 `compose/code/p247-mit-tier-sweep/sweep.sh` | **CASE-UNVARIED** | `LICENCE LICENSE LICENSE.md LICENSE.txt` |
| 🔴 `compose/code/p229-grant-ladder-reach/manifest_grant.py` | **CASE-UNVARIED** | `licence license` |

🔵 **So three passes read `gate-ladder-case` as a number over a ceiling. It was a reproducible failure mode in the probe vocabulary of six standing licence instruments — and this pass reproduced it by hand, on a real repository, and published the wrong verdict before catching it.** 🟢 The red earns itself. 🟡 Note the shape that saved nothing: `p228-shelf-gate/fetch_grants.sh` *is* `STEM-ONLY` and *does* carry `license.txt`, so the gate's fetcher could have found `yanki` while its classifier's own ladder could not — the two halves of one instrument disagree.

🟢 **And the negative control matters as much as the catch.** p335's four `UNGRANTED` rows were re-probed this pass on the full case-varied ladder — `dmontgomery40/mcp-canvas-lms`, `likr/canvas-lms-agent`, `studiolxd/xapi`, `risnake/canvas-mcp-server` — and **all four are absent on all 24 rungs.** 🟢 **p335's DECLARED-ONLY class is sound and stands at 8; it was not inflated by case-blindness.** Only my own row was.

🟢 **`ACTION ZL`: every absence claim on these shelves is probed on the case-varied, both-spellings ladder of **24 rungs** (`LICENSE` · `LICENSE.md` · `LICENSE.txt` · `LICENCE` · `LICENCE.md` · `license` · `license.md` · `license.txt` · `licence` · `licence.md` · `License` · `License.md` · `License.txt` · `Licence` · `COPYING` · `COPYING.txt` · `copying` · `NOTICE` · `LICENSE-MIT` · `MIT-LICENSE` · `MIT-LICENSE.txt` · `mit-license.md` · `UNLICENSE`, case varied, both spellings), and no pass may publish `UNGRANTED` from a ladder that `gate-ladder-case` types `CASE-UNVARIED`.** 🔵 The ladder used for every absence in this pass is now that one.

---

### 🔴 FINDING 1 — a payload titled with a full-text family, far too small to contain it, is published as that family

**Specimen, new this pass:** `PerryLink/dsh-essay-rubric-check`, `main/LICENSE`, **682 B**. Its text is the Apache-2.0 **appendix notice** — the "How to apply the Apache License to your work" short form. It carries the title, the version line, and the `you may not use this file except in compliance` sentence. It contains **no definitions, no §2 copyright grant, no §3 patent grant, no redistribution terms**. On its own it licenses *nothing*; it points at `apache.org`.

**Run first-hand this pass against three payloads, same family, three sizes:**

| payload | bytes | `p198` title-line | `p307` three-valued | 🔴 `p228` **shelf gate** |
|---|---|---|---|---|
| `PerryLink/dsh-essay-rubric-check` | **682** | `Apache-2.0` | 🟢 **`POINTER`** — `url=apache.org/licenses/` | 🔴 **`Apache-2.0`** — *"title line @33"* |
| `Plasius-LTD/learning` | 10 975 | `Apache-2.0` | 🟢 `GRANT` `Apache-2.0` | `Apache-2.0` — *"title line @61"* |
| `BrightspaceUI/lms-context-provider` | 10 421 | `Apache-2.0` | 🟢 `GRANT` `Apache-2.0` | `Apache-2.0` — *"title line @0"* |

🔴 **The gate that decides what reaches a shelf cannot tell a pointer from a grant.** All three return `Apache-2.0`; the only thing that varies is the title line's byte offset (33 / 61 / 0), which the gate prints and does not act on. 🟢 **`p307.classify_payload` gets it exactly right** — it requires a grant CLAUSE (`grants? to You a perpetual`), finds none, falls through to the URL rung and returns `POINTER`. 🔴 **`p307` is not in the shelf-gate path.** Seventh instance in eight passes of the class p334 named: *capability present, instrument already built, nothing executes it over the decision that needs it.*

🔴 **And this one fails in the opposite direction from p314.** p314's untitled-payload class makes classifiers ABSTAIN: the cost is **usable supply excluded**, and an abstention fails SAFE under `P250`. This class makes the gate ASSERT: the cost is **a published recommendation to build on a repository whose grant was never granted.** It fails UNSAFE. 🟡 Of the two, this is the one that can reach a client engagement.

**Two instances were already on these shelves** — found by the census below, confirmed first-hand this pass:

| slug | shelf cell | payload, re-read this pass | 🔴 true class |
|---|---|---|---|
| `wwrwbs/AI_AWE` | `Apache-2.0`, 1 865 B | **1 865 B**, first line `Apache License` | 🔴 **hollow — 16 % of the 11 357 B canonical** |
| `24kchengYe/human-skill-tree` | `GPL-3.0` / `AGPL-3.0`, 1 134 B | **1 134 B**, first line `GNU AFFERO GENERAL PUBLIC LICENSE` | 🔴 **hollow — 3 % of the 34 523 B canonical AGPL** |

🟢 **`ACTION ZG` registers the repair, and it is wiring, not research: `p307.classify_payload` runs in `p228`'s path, and a `POINTER` verdict may not be published as a family name.**

---

### 🟢 Promoted this pass — 8 rows, both channels read first-hand

Grant read on `raw.githubusercontent.com`; npm `license` read on `registry.npmjs.org`; activity and placement on the bare-clone channel. Per `ACTION ZD` each row records the CHANNEL, and per `ACTION ZE` **no placement cites a payload holder** — every one is on the commit channel.

| Agent / tool | Repo | Grant — both channels | Activity, first-hand (clone channel) | Placed, and how |
|---|---|---|---|---|
| 🆕 **uis-mcp-server** | https://github.com/SidneyBissoli/uis-mcp-server | 🟢 **MIT** — `main/LICENSE.md`, **1 088 B** · npm `uis-mcp-server` **MIT** — 🟢 both channels speak, agree | 🟢 **100 c · 2 a · all 100 in 2026 · 2026-08-07 → 2026-10-15** · root `dbd5b765` | 🟢 **LATAM — Brazil**, on two channels: `-0300` on **100 of 100**, and the sole human author is **Sidney da Silva Pereira Bissoli**; service runs at `uis.sidneybissoli.com` |
| 🆕 **h5p-cli** | https://github.com/h5p/h5p-cli | 🟢 **MIT** — `master/LICENSE`, **1 066 B** · npm `h5p-cli` **MIT** | 🟢 **730 c · 39 a · 2013-11-22 → 2026-10-20 (today) · 60 c in 2026** | 🟢 **EMEA — Norway** (H5P Group, Tromsø) — `+0200(451) +0100(137)`; `posteo.de(20)` is Oliver Tacke |
| 🆕 **hyperbook** | https://github.com/openpatch/hyperbook | 🟢 **MIT** — `main/LICENSE.md`, **1 069 B** · npm `@hyperbook/markdown` **MIT** | 🟢 **2 087 c · 10 a · 2022-03-08 → 2026-10-19 · 456 c in 2026** | 🟢 **EMEA — Germany** — `barkmin.eu` **1 079 commits** (Mike Barkmin, OpenPatch); `+0200(753) +0100(641)` |
| 🆕 **h5p-offline-player** | https://github.com/missing-elements/h5p-offline-player | 🟢 **MIT** — `main/LICENSE`, **1 073 B** · npm **MIT** | 🟢 **288 c · 5 a · all 288 in 2026 · head 2026-10-19** | 🟢 **EMEA** — `+0300(280)` |
| 🆕 **zenbrain** | https://github.com/zensation-ai/zenbrain | 🟢 **Apache-2.0** — `main/LICENSE`, **11 357 B** (canonical, `GRANT` on `p307`) · npm `@zensation/algorithms` **Apache-2.0** | 🟢 **191 c · 8 a · all 191 in 2026 · head 2026-10-18** | 🟢 **EMEA** — `+0200(158) +0100(31)` |
| 🆕 **moodle-driver** | https://github.com/falkenslab/moodle-driver | 🟢 **MIT** — `main/LICENSE`, **1 067 B** · npm `@falkenslab/moodle-driver` **MIT** | 🟡 **320 c · 1 a · 2026-10-09 → 2026-10-18** — 320 commits in **nine days, one author** | 🟢 **EMEA** — `+0100(320)` |
| 🆕 **h5p-theme-picker** | https://github.com/otacke/h5p-theme-picker | 🟢 **MIT** — `master/LICENSE`, **1 073 B** (`The MIT License`) · npm **MIT** | 🟡 **83 c · 2 a · all 83 in 2026 · head 2026-10-17** | 🟢 **EMEA — Germany** — `posteo.de(82)`, `+0200(46) +0100(36)` |
| 🆕 **yanki** | https://github.com/kitschpatrol/yanki | 🟢 **MIT** — `main/`**`license.txt`** (**lowercase**), **1 071 B** · npm `yanki` **MIT** — 🟡 **found only on the 8th rung of a case-varied ladder; an uppercase-only ladder refuses it** | 🟢 **474 c · 3 a · 2024-05-26 → 2026-10-16 · 87 c in 2026** | 🟢 **North America** — `ericmika.com(471)`, `-0400(407) -0500(65)` |

🔵 **Why `uis-mcp-server` is the row of this pass.** p335 placed `Cvmcosta/ltijs` in **LATAM — Brazil** and stated the honest bound: *"this places the maintainer, not a market."* This pass found a **second, independent** Brazilian row on the channel p335 prescribed (`ACTION TJ`, the package registry) — and it is not an integration shim: it serves **UNESCO Institute for Statistics education data over MCP**, listed in the official MCP Registry, Glama and Smithery. 🟢 Two unrelated maintainers, two instruments, one region. The LATAM supply side is now a measurement with a denominator, not an anecdote.

🟡 **`moodle-driver` is shelved at 🟡 deliberately, and it is a PAIR.** The same maintainer owns `falkenslab/moodle-mcp`, already on these shelves at 🟡 for the same reason (169 c / 12 d / 1 a). The driver's claim is the interesting one — *full control of Moodle as any user, from code or the CLI, **with no web services***, which is the single most common blocker on a Moodle engagement, since institutional Moodle web services are usually off and the sysadmin will not turn them on. 🔴 One author and nine days is not a bench. Prototype on it; do not stake a delivery date on it.

---

### 🔴 Refused this pass — 4 rows in three classes, plus one refusal RETRACTED within the pass

| Repo | Why refused | Measured first-hand |
|---|---|---|
| ~~https://github.com/kitschpatrol/yanki~~ | 🟢 **RETRACTED WITHIN THIS PASS — the refusal was MINE, and it was wrong.** First probed on an all-uppercase ladder and refused `REFUSED-UNGRANTED`. 🟢 **`gate-ladder-case` caught it**; re-probed on a case-varied ladder, the grant is `main/`**`license.txt`** — **lowercase** — **1 071 B**, `MIT License`. 🟢 **Promoted to the table above.** 🔴 **It was never a ninth instance of p335's DECLARED-ONLY class** | see the promoted table |
| https://github.com/PerryLink/dsh-essay-rubric-check | 🔴 **REFUSED-UNGRANTED (`POINTER`, not a grant) + BELOW-BAR.** The 682 B specimen of FINDING 1; and **37 commits over twelve days** | 37 c · 3 a · 2026-10-07 → 2026-10-19 · 🟢 **APAC — China**, `+0800(37)` |
| https://github.com/mikeargento/sealed-exam | 🔴 **REFUSED-SCOPED-GRANT + BELOW-BAR.** `LICENSE.txt` is **2 950 B** and is not a single-family grant: it enumerates *which paths* are MIT (*"the verification path is MIT: the files under `verifier/`…"*). npm's flat **MIT** is correct for the **package** and wrong for the **repository** — `P262`'s scoped-reservation axis, on a new shape. **23 commits** | 23 c · 2 a · 2026-09-14 → 2026-10-19 · 🟢 **North America**, `bitgraph.ing(12)`, `-0400(23)` |
| https://github.com/Creaditor/frontend | 🔴 **REFUSED-NO-SUCH-REPO.** npm `@creaditor/course-starterkit` 0.10.4 (published 2026-10-19) carries a `repository` link that `git ls-remote` does not resolve. 🔵 A discovery-channel integrity datum: `ACTION TJ`'s channel can hand you a slug that is not a repository | `git ls-remote` → no refs |
| https://github.com/corsairdev/corsair | 🔴 **REFUSED-OUT-OF-DOMAIN**, recorded for its size. Apache-2.0, 10 824 B, **1 803 c · 307 a · 1 353 c in 2026**; 🟢 **APAC — India** primary, `+0530(969) -0500(387) -0400(357)`. It is a general integration platform, education-relevant only through its one `@corsair-dev/blackbaud` plugin (Blackbaud = US K-12 / nonprofit SIS). 🟡 Not an education row; worth a revisit if the Blackbaud connector matures | 1 803 c · 307 a · 2025-10-14 → 2026-10-20 |

---

### 🟡 Two measured LIMITS on `ACTION TL`'s commit channel — both found while placing this pass's rows

🔵 p335 repaired `ACTION TL` by moving placement from the licence payload to the commit channel. That repair holds. These are its **boundaries**, each with a specimen measured this pass:

| limit | what breaks | specimen, measured |
|---|---|---|
| 🔴 **L1 — DST degeneracy** | A history lying entirely inside northern-hemisphere summer cannot separate **US Central (`-0500` under DST)** from **Colombia / Peru / Ecuador (`-0500` year-round)** | `intellectif/learning-kit` — **275 c · 5 a · all 2026 · `-0500(228)`**. Commit months present: **05, 08, 09, 10** — **zero** commits in the Nov–Mar window that would separate the two. 🟡 **Placement NOT resolved: Americas, `-0500`.** Sole human author "Diego E"; English conventional-commit subjects; no corporate domain |
| 🔴 **L2 — CI normalisation** | Where `users.noreply.github.com` dominates, offsets collapse to `+0000` and place the repository in **EMEA regardless of its maintainer** | `BrightspaceUI/lms-context-provider` — **715 c · 12 a · 224 c in 2026**, `users.noreply(658)`, **`+0000(685)`** ⇒ would read EMEA. 🟢 The corporate domain refutes it: **`d2l.com(15)`** and `martynus.net(39)` ⇒ **North America — Canada** (D2L, Kitchener, Ontario). Vendor-maintained, Apache-2.0 10 421 B |

🟢 **`ACTION ZH`: a placement may not cite an offset distribution whose modal bucket is `+0000` while `users.noreply.github.com` is the modal domain — fall through to the corporate domain, or return NOT RESOLVED.**
🟢 **`ACTION ZI-b`: a `-0500`-only placement must state whether any commit falls outside Mar–Nov; if none does, the verdict is NOT RESOLVED, never "North America".**

🔵 **`intellectif/learning-kit` is held, not refused.** 🟢 MIT, `main/LICENSE`, 1 072 B, npm `@intellectif/lk-core` **MIT**, both channels agree; 275 c · 5 a · head 2026-10-18. Its payload — *"framework-free assessment core: activity validation, pure scoring, rubric & deferred grading, weighted assessment"* — is exactly the assessment engine `compose/patterns.md` keeps hand-rolling. It is withheld from the placed tiers **only** because L1 blocks its region, and it is the first row this base has held for that reason alone.

## Pass 335 · 2026-10-20 (eighth pass of this date) — the LATAM supply side was never empty: the library on this shelf's own build tier is Brazilian, and five passes declared the region barren while recommending it

🔴 **`intel/market.md` and the last five trending sweeps have recorded the same sentence — *"the LATAM supply side returned nothing placeable"* (p328, p330, p331, p333, p334).** 🟢 **It is false, and the refutation was already on this shelf.** **`Cvmcosta/ltijs`** has sat on the **Build-on-this tier since p331** as *"LMS integration, mature, narrow bench"*, **unplaced**. Probed first-hand this pass on the bare-clone channel: **root commit `eec0a6b1`, 2019-05-30, `cvmcosta@yahoo.com.br`; 429 of 575 commits from `yahoo.com.br`; offset `-0300` on 513 of 575.** 🟢 **LATAM — Brazil**, on exactly the instrument `ACTION TL` specifies.

🔵 **The defect is not that the region is empty. It is that the region question was only ever asked of the DISCOVERY channel.** Five passes ran `education AI github Brazil Mexico Argentina` against a search engine and recorded a gap; **no pass ran the placement instrument over the rows this shelf already held.** 🔴 **Fifth instance in seven passes of the class p334 named: capability present, instrument already built, nothing executes it over the existing inventory.** 🟢 **`ACTION ZC` registers the sweep: place every unplaced row already on these shelves before declaring any region a gap.**

🟡 **The honest bound: this places the maintainer, not a market.** A Brazilian author maintaining the canonical LTI 1.3 Node library is a **supply-side** datum — it says the region produces the integration layer an engagement is built on, not that LATAM institutions are buying. 🔵 **`ltiaas.com` carries 90 commits**, so the library has a commercial sponsor behind it.

### 🟢 Promoted this pass — every grant read on `raw.githubusercontent.com`, every activity figure from a bare `--filter=blob:none` clone, today

| Agent / tool | Repo | Grant, read first-hand | Activity, first-hand (clone channel) | Placed, and how |
|---|---|---|---|---|
| 🆕 **gogcli-mcp (Classroom)** | https://github.com/chrischall/gogcli-mcp | 🟢 **MIT** — `main/LICENSE`, **1,067 B**, © Chris Hall | 🟢 **498 c · 5 a · all 498 in 2026 · 2026-04-12 → 2026-10-19** | 🟢 **North America** — `-0400(373) -0600(12)` |
| 🆕 **caccl** | https://github.com/harvard-edtech/caccl | 🟢 **MIT** — `main/LICENSE.md`, **1,075 B**, © **Harvard University** | 🟡 **655 c · 3 a · 2018-11-02 → 2026-09-30 · only 27 c in 2026** | 🟢 **North America** — `harvard.edu` in the grant **and** on 3 commits; `-0400(351) -0500(290)` |
| 🆕 **@scormflow/player** | https://github.com/scormflow/scorm-engine-client | 🟢 **MIT** — `main/LICENSE`, **1,079 B**, © ScormFlow contributors | 🟢 **45 c · 2 a · all 45 in 2026 · head 2026-10-12** | 🟢 **APAC — India**, `+0530(45)` |
| 🆕 **@openhpi/quiz-recap** | https://github.com/christophblessing/quiz-recap | 🟢 **MIT** — `main/LICENSE`, **1,075 B**, © Christoph Blessing | 🟡 **288 c · 5 a · 19 c in 2026 · head 2026-09-11** | 🟢 **EMEA — Germany**, `hpi.de` **1 commit**, `+0100(95) +0200(92)`; npm scope `@openhpi` = Hasso-Plattner-Institut, Potsdam |

🟡 **`caccl` is a restoration, not a discovery.** It was a promoted 🆕 row in [`archive/2026-10-17-pre-rewrite/agents-top.md`](../archive/2026-10-17-pre-rewrite/agents-top.md) and is **absent from this shelf** — the same class of loss p334 found when `### Agents over the systems` had been deleted by the p315/p316 rewrites. 🔵 **Re-verified from scratch rather than pasted.** 🔴 **One verified instance; this pass does NOT generalise it to a count** — the archives carry census tables as well as shelf rows, and a naive diff reports 1,915 "dropped" slugs, which is an artefact of that mixing, not a measurement.

### 🔴 Refused in the same probe, with the reason recorded so the next pass does not re-probe them

| Repo | Why refused | Measured first-hand |
|---|---|---|
| https://github.com/groton-school/canvas-cli | 🔴 **REFUSED-COPYLEFT — and it is the dangerous one.** **GPL-3.0**, 35,149 B, while npm `@groton/canvas-api` declares **no licence at all** | 787 c · 3 a · **324 c in 2026** · head 2026-10-14 · 🟢 **North America**, `groton.org(737)` |
| https://github.com/openedx/frontend-base | 🔴 **REFUSED-COPYLEFT** — **AGPL-3.0**, 34,523 B | 3,341 c · 161 a · 125 c in 2026 · head 2026-09-22 · 🟢 **NA**, `edx.org(553)` |
| https://github.com/openedx/frontend-platform | 🔴 **REFUSED-COPYLEFT** — **AGPL-3.0**, 34,520 B | 1,151 c · 92 a · 46 c in 2026 · head 2026-10-18 · 🟢 **NA**, `edx.org(360)` |
| https://github.com/likr/canvas-lms-agent | 🔴 **REFUSED-UNGRANTED** — no licence file on 12 paths; npm `@likr/canvas-lms-mcp` declares MIT and the repo does not | 68 c · 2 a · all 2026 · head 2026-07-10 · 🟢 **APAC — Japan**, `likr-lab.com(68)`, `+0900(68)` |
| https://github.com/DamPhuQuy/Agent-as-a-tutor | 🔴 **REFUSED-BELOW-BAR** — MIT, 1,070 B, but **21 commits over seven days** | 21 c · 2 a · 2026-10-12 → 2026-10-19 · 🟢 **APAC — Vietnam**, `+0700(12)` |
| https://github.com/studiolxd/xapi | 🔴 **REFUSED-UNGRANTED + BELOW-BAR** — npm declares MIT, repo has no payload; 12 commits, 1 author | 12 c · 1 a · head 2026-09-20 · 🟢 **EMEA**, `studiolxd.com(12)`, `+0200` |
| https://github.com/risnake/canvas-mcp-server | 🔴 **REFUSED-UNGRANTED + BELOW-BAR** — npm declares **ISC**, repo has no payload; **4 commits in one day** | 4 c · 1 a · 2026-03-22 · `-0500` |
| https://github.com/VienDinhCom/supermemo | 🔴 **REFUSED-DORMANT** — MIT, 1,065 B, but **zero commits in 2026** | 58 c · 4 a · head **2025-03-28** · `+0700` |
| https://github.com/Annoto/ims-lti | 🔴 **REFUSED-DORMANT** — MIT, 1,094 B, **zero commits in 2026** | 177 c · 16 a · head **2025-06-16** · `omsmith.ca(70)` |
| https://github.com/molecule-dev/molecule | 🔴 **REFUSED-SINGLE-AUTHOR** — Apache-2.0, 11,358 B, `NOTICE` © Molecule Dev, Inc.; **3,172 commits all in 2026 but 3,168 from one address** | 3,172 c · 3 a · head 2026-10-20 · 🟢 **EMEA**, `vialoh.me(3168)`, `+0300(2977)` |
| https://github.com/LongsightGroup/lti-tool | 🔴 **REFUSED-ALIAS** — **the same project as the `lti-tool/lti-tool` row already on the build tier**: identical root commit `e02ba195`, **301 shared commits**. Promoting it would have created a duplicate entity | 414 c · 5 a · head **2026-09-02** (the shelf row's head is 2026-10-19 — the shelf already carries the live side) |

🔵 **Three npm packages in this sweep have a LIVE registry listing and an UNREACHABLE repository** — `Mckaroff/GraphLMS`, `virtualarkansas/n8n-nodes-genius-sis`, `brainjamworks/liverpool-dental-theme` all `CLONE-FAIL`. **Registry metadata outlives the source tree**, which is a reason to treat an npm grant as a claim about a package, not about a repository.

### 🔴 The grant column disagrees with itself, and this pass measured the disagreement in both directions

**29 slugs probed on two channels — the npm `license` field and the repository licence payload.**

- 🔴 **8 of 27 resolvable packages (29.6%) are DECLARED-ONLY**: npm carries a permissive grant, the repository carries **no licence file at all**. 7 declare MIT, 1 declares ISC. **Every MCP connector discovered this pass falls in this class.**
- 🔴 **2 run the other way, and that is the direction that costs money**: `@groton/canvas-api` declares **nothing** on npm while the repository is **GPL-3.0 (35,149 B)**, and `canvas-lms-api` is silent on both. **A studio reading only the registry sees an absent licence field and may read it as unencumbered; the tree is copyleft.** 🔵 **Same shape as p333's ToolJet — a widely-installed artefact mis-graded in the permissive direction.**
- 🟢 **0 genuine value mismatches** where both channels carry a grant. **When both speak, they agree; the whole error is in the silences.**

🟢 **The rule this pass adds: a shelf row must record the CHANNEL of its grant, not only the value.** *"MIT (npm)"* and *"MIT (payload, 1,075 B)"* are different claims with different strength, and p333's correction made the second one the house standard without ever saying what to do when it does not exist. 🟢 **`ACTION ZD` registers the column.**

---


## Pass 334 · 2026-10-20 (seventh pass of this date) — p333 reported two red gates and there were three, and the third one fires on p333's own sentence

🔴 **Inherited state, measured on p333's HEAD before this pass changed a byte.** `make gate-offline` 🟢 **green (exit 0)**. `make hooks` 🔴 **red on THREE gates, not two**: `recount` (Makefile:397), 🔴 **`gate-absence` (Makefile:202)** and `gate-ladder-case` (Makefile:360). **p333 published "20/22 gates green, `recount` red … `gate-ladder-case` red on its C14 ratchet" and did not name `gate-absence`.** 🟢 **Left at 21/22: `recount` and `gate-absence` are green at the end of this pass, `gate-ladder-case` is still red and its cause is pinned in [`evidence/p334-ladder-standing-census`](../evidence/p334-ladder-standing-census.2026-10-20-p334.tsv).** 🔵 p333 was the pass that institutionalised *stating the gate state you inherited*; this is that paragraph doing its job one pass later, against p333.

### 🔴 The third gate fires on p333's own prose, and it is right to

**`gate-absence` exists to stop a pass publishing an absence whose subject the shelves already claim.** p333 wrote, in `intel/open-gaps.md`: *"nothing on China's AI Plus education plan, nothing from MEXT"*, and concluded **"the English-language secondary channel does not carry APAC education policy at all."** The gate answered with the count of cells that already name the subject:

| subject | phrase | `mext` cells the shelves already carry |
|---|---|---|
| `mext` | `'nothing on'` | `intel/open-gaps.md` **29** · `agents/trending.md` **10** · `repos/trending.md` **9** · `intel/market.md` **4** · `compose/patterns.md` **1** |

🟢 **Counted first-hand this pass with `grep -oi mext | wc -l` on each file: 29 · 10 · 9 · 4 · 1. The gate's numbers are correct.**

### 🟢 So this pass executed the prescription instead of re-declaring the gap — and the diagnosis was wrong about the channel

🔵 **`compose/patterns.md:338` has carried the instruction since p330:** *"Go per-country next (`MOE Singapore`, `MEXT`, `AusTender`, `GeM India`) — 'APAC' is not a procurement jurisdiction."* 🔴 **Four passes later nobody had run it, and p333 instead generalised from the regional query's failure to a claim about the whole channel.** Run per country, with each instrument's own name, the same channel returns **four dated national instruments**:

| jurisdiction | instrument | date | what it does |
|---|---|---|---|
| 🟢 **China** | 《"人工智能+教育"行动计划》 — **AI+Education Action Plan**, MOE **+ four other agencies** | **2026-04-10** | Five-year plan to 2030 across K-12, universities, vocational and lifelong learning; a **national AI (education) application pilot base**, partly central-budget funded |
| 🟢 **India** | **CT & AI** — Computational Thinking & Artificial Intelligence, MoE / CBSE, Classes **3–8** | **launched 2026-04-01**, mandatory from the **2026-27** session | Curriculum framework + **teacher handbook** + learning material, free on the CBSE site; committee chaired by **Prof. Karthik Raman, IIT Madras**; internal assessment, no separate exam |
| 🟢 **Japan** | **MEXT**, *Guideline for the Use of Generative AI in Elementary and Secondary Education* **Ver. 2.0** | **Ver.2.0 Dec 2024**; pilot figures in a MEXT document dated **2026-04-30** | **149 municipalities / 478 schools** (10 classroom use · 100 teacher administrative use · 51 courseware trial). Principle: **the final judgement and the responsibility are human** |
| 🟡 **Japan, draft** | high-school AI / data-science expansion | draft **Jun 2026** | Every high-school graduate AI- and data-literate **by 2030**. 🟡 Draft stage; content may change |

🔴 **The corrected diagnosis, which replaces p333's:** the channel carries APAC education policy. **What failed was the granularity of the query, not the channel** — and the shelf had already said so at p330. 🔵 **This is the fourth instance in six passes of the shape p333 named: the capability was present, the instruction was already written down, and nothing executed it.**

🟡 **Stated because the opposite would be the easy claim: none of the four was read first-hand.** `moe.gov.cn`, `mext.go.jp`, `consilium.europa.eu` and `cset.georgetown.edu` are all 🔴 **`000` — no connect** from this environment, on `curl` and on the fetch channel alike ([`evidence/p334-channel-reachability`](../evidence/p334-channel-reachability.2026-10-20-p334.tsv)). **These four rows are ATTRIBUTED to the search channel, not read.** 🟢 `raw.githubusercontent.com`, `registry.npmjs.org`, `pypi.org` and the **git clone channel** are readable, which is why every repository row below *is* first-hand and no policy row is.

### 🟢 One agent promoted, and it is the first EMEA-placed multi-author tutor on this shelf

| Agent | Repo | Grant, read first-hand | Activity, first-hand (clone channel) | Placed, and how |
|---|---|---|---|---|
| **TutorAI** | https://github.com/CogitoNTNU/TutorAI | 🟢 **MIT** — `main/LICENSE`, **1,140 B**, © 2023 Olav Selnes Lorentzen, Kristoffer Nohr Olaisen, Simon Sandvik Lee, Sverre Nystad | **1,140 c · 19 a · 2023-11-25 → 2026-10-07 · 111 c in 2026** | 🟢 **EMEA — Norway.** `stud.ntnu.no` **224 commits**; offsets `+0000(504) +0200(385) +0100(251)` |

🟢 **Read from the tree, not the README** — `backend/flashcards/knowledge_base/{embeddings,db_interface,llm,factory}.py` beside `backend/flashcards/flashcard_service.py`: a real retrieval layer with a swappable LLM factory, and CI that runs (`codeql`, `django`, `node.js`, `automerge_dependabot`). **It ingests a textbook and cites the curriculum back** — the one thing `intel/trends.md` T21's citation requirement asks of a tutor.

🟡 **The honest limit, and it is the same shape as `ltijs`:** 19 authors is the *historical* bench. **Only 2 distinct authors committed in 2026**, and the head is 2026-10-07 — thirteen days. 🔵 A student organisation's bench turns over by construction, so read this as *maintained by a rotating team*, not as five-year vendor continuity.

### Agents over the systems — 🟢 the MCP connector shelf, restored and re-verified rather than copied

🔴 **This section had been deleted from this shelf.** The `recount` gate has been red since p331 on five pins, and the reason is structural, not cosmetic: **the two headings it measures — this one and the build-on tier's own heading — were removed by the p315/p316 rewrites, so three of its five claims measured literal zero while `agents/trending.md`, which is append-only, still carried every row.** 🔵 **That is the clearest argument this base has produced for its own append-only rule: the data survived in the file nobody is allowed to rewrite.**

🟢 **Restored by re-verifying from scratch, not by pasting the archived rows.** **7 rows in the table below**, one per lane, every grant read on `raw.githubusercontent.com` and every activity figure from a bare `--filter=blob:none` clone, today. **6 platforms** are reachable by an MCP server named anywhere on this shelf — **5 of them through a permissive row**, the sixth (Open edX) only through an AGPL-3.0 one. [`evidence/p334-first-hand-probe`](../evidence/p334-first-hand-probe.2026-10-20-p334.tsv)

| Platform | MCP server | Grant, first-hand | Activity, first-hand | Placed |
|---|---|---|---|---|
| **Canvas** | https://github.com/vishalsachdev/canvas-mcp | 🟢 **MIT**, 1,071 B | 🟢 **1,041 c · 30 a · 927 c in 2026 · head 2026-10-19** | 🟢 **North America** — `-0500(552) -0600(133)` |
| **Canvas**, institutional | https://github.com/r-huijts/canvas-mcp | 🟢 **MIT**, 1,065 B | **60 c · 3 a · head 2026-09-21** | 🟢 **EMEA — Netherlands**, `fontys.nl` **52 commits** |
| **Brightspace / D2L** | https://github.com/rohanmuppa/brightspace-mcp-server | 🟢 **MIT**, 1,068 B | 🟢 **414 c · 17 a · all 414 in 2026 · head 2026-10-20 (today)** | 🟢 **North America** — `-0400(246) -0500(161)` |
| **Moodle** | https://github.com/falkenslab/moodle-mcp | 🟢 **MIT**, 1,067 B | 🟡 **169 c · 1 a · head 2026-10-19** — 169 commits in 12 days, one author | 🟢 **EMEA** — `+0100(169)` |
| **Blackboard** | https://github.com/felipedias-ie/blackboard-mcp | 🟢 **MIT**, 1,084 B | 🟡 **21 c · 3 a · head 2026-10-14** | 🟢 **EMEA** — `+0200(21)` |
| **Google Classroom** | https://github.com/sandraschi/classroom-mcp | 🟢 **MIT**, 1,071 B (`master`) | 🟡 **28 c · 3 a · head 2026-10-13** | 🟢 **EMEA** — `+0200(28)`. 🔴 9 commits carry `example.com` addresses |
| **Anki** (not an LMS) | https://github.com/ankimcp/anki-mcp-server | 🟢 **MIT**, 1,074 B | 🟢 **258 c · 6 a · 176 c in 2026 · head 2026-10-11** | 🟢 **EMEA** — `+0300(190) +0200(68)`, one `tcd.ie` |

🔵 **`vishalsachdev/canvas-mcp` carries `anthropic.com` on 171 commits and `r-huijts/canvas-mcp` on 8.** Those are **tool-written authorship addresses, not institutions** — p142 corrected exactly this column — so neither row is placed on them. **Both regions above are booked on commit offsets alone.**

### 🔴 Refused in the same probe, with the reason recorded so the next pass does not re-probe them

| Repo | Why refused | Measured |
|---|---|---|
| https://github.com/dmontgomery40/mcp-canvas-lms | 🔴 **REFUSED-UNGRANTED** — no licence on **12 paths** (6 filenames × 2 branches) | 16 c · 4 a · head **2026-05-31** |
| https://github.com/blend-ed/openedx-mcp | 🔴 **REFUSED-COPYLEFT** — **AGPL-3.0**, 34,524 B | 9 c · 1 a · head 2026-10-17 · `blend-ed.com` |
| https://github.com/lmscloud-io/moodle-mcp-server | 🔴 **REFUSED-COPYLEFT** — **GPL-3.0**, 35,148 B — **and** dormant | 10 c · 2 a · head **2026-05-08** |
| https://github.com/faizan45640/google-classroom-mcp-server | 🔴 **REFUSED-DORMANT** — MIT, but **zero commits in 2026** | 9 c · 4 a · head **2025-07-28** |
| https://github.com/carlsvejstrup/dtu-learn-mcp | 🔴 **REFUSED-BELOW-BAR** — MIT, 1,079 B, but **5 commits, 1 author** | head 2026-10-07 · `+0200` |
| https://github.com/Marid5/ai-tutor | 🔴 **REFUSED-BELOW-BAR** — MIT, 1,076 B, © 2026 Alexander Zhuravlev; **44 commits over two days**, silent 12 days | 44 c · 2 a · 2026-10-07 → **2026-10-08** · `+0300` |
| https://github.com/SiddharthG1210/RAG-AI-TUTOR | 🔴 **REFUSED-COPYLEFT** — **AGPL-3.0**, 34,523 B | 40 c · 2 a · head 2026-10-19 · 🟢 **APAC — India**, `+0530(40)` |
| https://github.com/affromero/Sotto | 🔴 **REFUSED-COPYLEFT** — **AGPL-3.0**, 34,523 B. 🔵 Recorded anyway for its velocity: **4,109 commits in eight months**, `.claude/hooks/` committed — an agent-built codebase | 4,109 c · 6 a · 2026-02-08 → 2026-10-19 · 🟡 **two-offset footprint `+0100(2,571)` and `-0500(1,243)`; placement NOT resolved** |

🟢 **The one finding this sample is worth more than its rows:** the permissive MCP connectors point at **proprietary** LMSs — Canvas, Brightspace, Blackboard, Google Classroom — while **both** copyleft rows point at the **open-source** ones, Moodle (GPL-3.0) and Open edX (AGPL-3.0). 🟡 **Measured on a 12-row sample, not on the census** — the agent shelves carry **155 distinct MCP server slugs**, of which **74** are attributable to a named platform. Recorded in `intel/trends.md` as T25 with that bound stated.

## Build-on-this tier

🟢 **13 permissive rows — MIT, Apache-2.0 or BSD only** *(8 at p334, +5 promoted p335; `ltijs` re-placed, not added).* A row whose code grant is permissive but whose **data or corpus** is share-alike is NOT in this tier; `learning-commons-org/evaluators` (MIT code, **CC BY-NC-SA 4.0** corpora) and `withmarbleapp/os-taxonomy` (**ODbL-1.0 + CC BY-SA 4.0**) are carried in the p333 shelf below and deliberately excluded here, because this tier's one job is to answer *may I embed this in a client deliverable*.

| Agent / tool | Repo | Grant | Activity, first-hand | Layer |
|---|---|---|---|---|
| **lti-tool** | https://github.com/lti-tool/lti-tool | 🟢 **MIT** (1,077 B, p331) | 346 c · 6 a · 2026-10-19 · release 2026-10-20 (p331) | LMS integration — the way in |
| **ltijs** | https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0** (11,361 B, p331) | 575 c · 17 a · **51 c in 2026** · head 2026-10-13 (re-probed p335) | LMS integration, mature, narrow bench — 🟢 **LATAM — Brazil** *(p335: root `eec0a6b1` `cvmcosta@yahoo.com.br`; `yahoo.com.br` 429/575; `-0300` 513/575)* |
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | head 2026-10-19 (p330) | Agent-native tutor |
| 🆕 **TutorAI** | https://github.com/CogitoNTNU/TutorAI | 🟢 **MIT** (1,140 B, p334) | 1,140 c · 19 a · head 2026-10-07 · 111 c in 2026 (p334) | RAG tutor that cites the curriculum — 🟢 **EMEA** |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | 🟢 **MIT** (1,073 B, p331) | 467 c · 5 a · 2026-10-16 (p330) | ITS state + review scheduling over MCP |
| **OATutor** | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1,045 c · 27 a · 2026-10-16 (p330, re-confirmed p334: **1,045 c · head 2026-10-16**) | Pedagogy — BKT, UC Berkeley |
| **Agent Skills** | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** (10,173 B, p327) | 42 c (p327) | K-12 teacher skills over MCP |
| 🆕 **canvas-mcp** | https://github.com/vishalsachdev/canvas-mcp | 🟢 **MIT** (1,071 B, p334) | 1,041 c · 30 a · 927 c in 2026 · head 2026-10-19 (p334) | The widest-bench connector on these shelves — 🟢 **North America** |
| 🆕 **@brightspace-ui/core** | https://github.com/BrightspaceUI/core | 🟢 **Apache-2.0** (10,421 B, p335) | 🟢 **9,598 c · 180 a · 1,020 c in 2026 · head 2026-10-19** (p335) | Accessible web components from a **proprietary** LMS vendor — the deepest bench on these shelves — 🟢 **North America**, `d2l.com(2,748)` |
| 🆕 **gogcli-mcp (Classroom)** | https://github.com/chrischall/gogcli-mcp | 🟢 **MIT** (1,067 B, p335) | 🟢 **498 c · 5 a · all 498 in 2026 · head 2026-10-19** (p335) | Google Classroom over MCP — 🟢 **North America** |
| 🆕 **caccl** | https://github.com/harvard-edtech/caccl | 🟢 **MIT** (1,075 B, © **Harvard University**, p335) | 🟡 **655 c · 3 a · 27 c in 2026** · head 2026-09-30 (p335) | Canvas + LTI scaffold, eight years continuous — 🟢 **North America** |
| 🆕 **d2l-test-reporting** | https://github.com/Brightspace/test-reporting-node | 🟢 **Apache-2.0** (10,421 B, p335) | 🟢 **1,129 c · 13 a · 358 c in 2026 · head 2026-10-19** (p335) | Test-evidence reporting for LMS front ends — 🟢 **North America** |
| 🆕 **@scormflow/player** | https://github.com/scormflow/scorm-engine-client | 🟢 **MIT** (1,079 B, p335) | 🟢 **45 c · 2 a · all 45 in 2026 · head 2026-10-12** (p335) | SCORM runtime bridge in the browser — 🟢 **APAC — India** |

---

## Pass 333 · 2026-10-20 (sixth pass of this date) — the column every row on this shelf is graded by was matching licence names inside other words, and the word it matched most was `commits`

🔴 **The grant column is produced by a classifier that, until this pass, tested `"mit" in row`.** A licence family name is three letters long and English is full of them. Measured over this repository's own `evidence/` at p333: 🔴 **610 rows across 259 evidence files — 5.7% of every row that matched a permissive token — were graded permissive on a substring embedded in a longer word and nothing else.** [`evidence/p333-substring-grant-census`](../evidence/p333-substring-grant-census.2026-10-20-p333.tsv).

| what the classifier read as a grant | what the word actually was | spurious matches |
|---|---|---|
| `isc` | d**isc**overy, d**isc**harged, d**isc**losure | 265 |
| `mit` | com**mit**s, com**mit**ted, com**mit**tee, per**mit**ted, rate_li**mit** | 328 |
| `mit` | 🔴 **d**mit**ry-viskov** — the maintainer's first name | 32 sightings of that slug |
| `cc0` | inside hashes and paths | 24 |

🔴 **Two of those carriers are this KB's own vocabulary, and that is the part worth stopping on.** **`commits` and `committed` are the ACTIVITY triple p329 introduced to these very tables** — so the measurement p329 added to make this shelf honest silently re-graded the grant column one pass later. And a repository is graded MIT because its maintainer is called **Dmitry**.

### 🔴 The dangerous direction is real, and it was found in the wild

🔵 **A grading error only matters if it errs toward "you may build on this".** It did. **Twelve rows flipped off permissive once the boundary rule was applied; seven of them are plain copyleft, and all seven were then read first-hand on `raw.githubusercontent.com` to confirm the correction rather than trust the classifier in either direction:**

| row | graded by p332 | read first-hand p333 | bytes |
|---|---|---|---|
| `tooljet/tooljet` | 🔴 permissive | 🟢 **AGPL-3.0** | 34,503 |
| `pdfmathtranslate/pdfmathtranslate` | 🔴 permissive | 🟢 **AGPL-3.0** | 34,523 |
| `sage-is/ai-ui` | 🔴 permissive | 🟢 **AGPL-3.0** | 33,895 |
| `schemaspy/schemaspy` | 🔴 permissive | 🟢 **GPL-3.0** (`COPYING`) | 35,148 |
| `sansan0/trendradar` | 🔴 permissive | 🟢 **GPL-3.0** | 35,149 |
| `dvjvp/lut-to-ue4-clut` | 🔴 permissive | 🟢 **GPL-3.0** | 35,141 |
| `thecyberbrick/fits-rating-tool` | 🔴 permissive | 🟢 **GPL-3.0** (`COPYING`) | 35,148 |

🟢 **7 of 7 confirmed. The correction is right in every case, and `tooljet/tooljet` is the one that would have cost money** — a widely-adopted low-code platform, AGPL-3.0, sitting in this corpus marked as something a studio may embed in a client deliverable.

🔵 **`pdfmathtranslate` is also the row that exposed the whole defect, and the mechanism is worth naming exactly.** p154 recorded it **correctly** as AGPL-3.0. p332 read it back as *permissive* — because the row cites the evidence **filename** it came from, `api-di`**`sc`**`overy-overlap.2026-10-12-p154.tsv`. 🔴 **A correct measurement was destroyed by the name of the file that held it.**

### 🔴 And the loop was closing: the audit was eating its own output

🔵 **The single largest carrier of the defect is not an old research file. It is `p332-delivery-audit.2026-10-20-p332.tsv` — 109 of the 610 rows.** The delivery audit writes its results into `evidence/`, and `harvest_evidence()` reads every `.tsv` in `evidence/`. 🔴 **So one pass's grade became the next pass's evidence, and every row in that output cites a filename, which is exactly where the spurious tokens live.** 🟢 **Derived output is now excluded by name (`DERIVED_EVIDENCE`), so the loop cannot close.**

### 🔵 This KB already held the guard

🔴 **`compose/code/licence-grant-gate/grant_gate.py:112` declares `AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`** and reasons at length about a licence family name that is also the name of something else. **It was never applied to the audit.** 🟢 **That is p329's shape for the third time in five passes: capability present, instruction already written, not exercised.**

### 🟢 Fixed, controlled and gated

**The rule: a token counts when it is not preceded by an alphanumeric and not followed by two or more letters.** 🔵 **The one-letter right-hand allowance is load-bearing and has its own controls** — `GPLv3` and `MPL-2.0` are real spellings a stricter boundary would silently discard, while `apachecon`, `mitigation` and `discovery` are not grants. 🟢 **32 new controls, every one built from a carrier measured in this corpus rather than invented: 40 → 72, and `make gate-offline` is green (exit 0).**

🟢 **What this does NOT change, stated because the opposite would be the easy claim:** the delivery rate is untouched. Measured A/B on an identical corpus — 3,770 slugs measured, 786 undelivered, **79.2% both before and after.** 🔴 **The defect is in the GRANT column, not the delivery measure**, and the honest headline is narrower than "the audit was wrong": **the permissive `silent` class shrinks 370 → 306, so 64 rows this KB believed it could build on were never permissive at all.**

🟢 **None of the twelve is on a live shelf** — they are all in the undelivered set by construction. **The defect is contained to the evidence tier, as `pdfmathtranslate` was at p332.** The shelf below is unaffected in its grants and is carried forward with every figure still first-hand.

### 🔴 One inherited state this pass is reporting because the last one did not

**`make hooks` was already RED at p332's HEAD.** Measured on a clean checkout before p333 changed a byte, and again after: **identical — 20/22 gates green, `recount` red with 7 `NO-ANCHOR` claims, `gate-ladder-case` red on its C14 ratchet.** 🟢 **p333 neither caused nor worsened either, and `make gate-offline` is green.** 🔴 **p332 caught p331 leaving `gate-offline` red and then shipped with `hooks` red itself, silently. Third pass in a row.** 🔵 **The fix is not another gate — it is that a pass must state the gate state it INHERITED, which is what this paragraph is.**

### 🟢 The agent shelf — carried from p332, unchanged

**No new AGENT qualified this pass, and that is stated rather than padded.** The three promotions this pass earned are substrate and instrument, not agents; they land in [`repos/foundations.md`](../repos/foundations.md).

| Agent / tool | Repo | Grant | Activity, first-hand | Layer |
|---|---|---|---|---|
| **lti-tool** | https://github.com/lti-tool/lti-tool | 🟢 **MIT** (1,077 B, p331) | 346 c · 6 a · 2026-10-19 · release 2026-10-20 (p331) | 🟢 LMS integration — the way in |
| **ltijs** | https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0** (11,361 B, p331) | 575 c · 17 a · 2026-10-13 (p331) | 🟡 LMS integration, mature, narrow bench |
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | head 2026-10-19 (p330) | 🟢 Agent-native tutor |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | 🟢 **MIT** (1,073 B, p331) | 467 c · 5 a · 2026-10-16 (p330) | 🟢 ITS state + review scheduling over MCP |
| **OATutor** | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1,045 c · 27 a · 2026-10-16 (p330) | 🟢 Pedagogy — BKT, UC Berkeley |
| **Agent Skills** | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** (10,173 B, p327) | 42 c (p327) | 🟢 K-12 teacher skills over MCP |
| **Evaluators** | https://github.com/learning-commons-org/evaluators | 🟡 **MIT code**; corpora **CC BY-NC-SA 4.0** (p327) | 289 c (p327) | 🟢 Pedagogy-aware evaluation |
| **os-taxonomy** | https://github.com/withmarbleapp/os-taxonomy | 🟡 **ODbL-1.0 + CC BY-SA 4.0** (25,289 B, p331) | 23 c · 3 a · 2026-10-19 (p331) | 🟢 Curriculum spine (data, not code) |

🔵 **One control that had to be preserved while fixing the matcher:** p332's `mixed` branch — MIT code beside a share-alike corpus — is the shape of the `os-taxonomy` row above. **The boundary rule is applied to both token families, so `mixed` stays reachable; there is a control asserting exactly that row's shape.**

---

## Pass 332 · 2026-10-20 (fifth pass of this date) — the audit p327 prescribed and p331 called unrun now exists, and the first thing it did was refute p331's own generalisation

🔵 **p331's closing finding was right about its case and wrong about its scope.** It measured `lti-tool/lti-tool` — recorded in `evidence/` at p232, absent from every shelf through p330 — and generalised: *"This KB's discovery rate on `lti-tool` was 100% at p232 and its delivery rate was 0% through p330 — the exact failure p327 named and prescribed an audit for, still unrun. The prescription was right; nothing executes it. It belongs in the hook tier, not in prose."*

🟢 **The first half is now discharged. [`compose/code/p332-delivery-audit/`](../compose/code/p332-delivery-audit/) is that instrument, 40 offline controls, wired into `make gate-offline`** — so it is in the hook tier, where p331 said it belonged, and not in prose. 🔴 **The second half does not survive it.** Measured across the whole corpus rather than one case:

| measure, p332 | value |
|---|---|
| slugs carried on the ten shelves | **2,420** |
| slugs measured into `evidence/` | **3,761** |
| of those, delivered to a shelf | 🟢 **2,968 — 78.9%** |
| never on a shelf | 793 |
| …of which a pass explicitly **deferred** (`unplaced`, `unread`) | **33** |
| …of which deferred **and** permissively granted | 🔴 **16** |

🔴 **So the defect class is 16 rows, not a systemic 0%.** A delivery rate of 78.9% is not the failure p331 described, and the difference matters because the two diagnoses prescribe opposite actions: a 0% rate says build a promotion pipeline, a 78.9% rate with 16 deferred rows says *read the 16.*

### 🔴 Two measurement errors found inside the audit itself, both of which would have inflated the gap

🔵 **These are recorded because the KB nearly published both, and the second is the more interesting.**

1. 🔴 **p235's index reads URLs, not names — and the gap it reports is ~1.6× too large.** `carried_index.py` harvests `github.com/<slug>` and nothing else. Three rows in the first defect list (`qtiworks`, `bnlp`, `uniroster-server`) are **discussed on these shelves by name with no URL beside them**, so a URL-only index calls all three undelivered. 🟢 **Adding the name channel moved the measured delivery rate from 62.6% to 78.9% and cut the deferred-permissive class from 38 rows to 16.** The audit now tries both channels before reporting a miss.
2. 🔴 **`evidence/` contains seeded decoys, so "measured but not delivered" is not a defect predicate until the controls are subtracted.** The single highest-sighting row in the first run, at **25 sightings**, was `DecoyLex/ltix` — which is `p208-seeded-error-audit/seed.sh`'s one invented slug, planted so the audit can be asked whether it finds a wrong cell. 🟢 **It must never reach a shelf; counting it as a delivery failure is the audit reporting a planted control as a defect.** It is excluded by name, with the reason in the source.

### 🟢 Twelve of them probed first-hand — and the honest verdict is that the shelves were mostly right

🔵 **Scope stated precisely, because the conclusion rests on it: these twelve are the MOST-SIGHTED rows of the defect class as the audit FIRST reported it — 38 rows, before the name channel cut the class to 16.** Three of the twelve (`qtiworks`, `bnlp`, `uniroster-server`) are the rows that fall out when the name channel is added, and they are kept in the table because their verdicts are what proved the channel was missing. 🔴 **Twelve of thirty-eight is a thin sample and it is ranked by sightings, which selects for rows that were already interesting** — the correction is a standing action in `intel/open-gaps.md`.

**Every figure below is first-hand p332: licence from `raw.githubusercontent.com/<slug>/HEAD/<path>`, activity from `git clone --bare --filter=blob:none` and the full commit graph. `github.com` HTML, `api.github.com` and `codeload` all return 403 in this environment — the channel table is in [`evidence/p332-defect-probe.2026-10-20-p332.tsv`](../evidence/p332-defect-probe.2026-10-20-p332.tsv).**

| row | grant, first-hand | activity, first-hand | verdict |
|---|---|---|---|
| `h5p/h5p-interactive-video` | 🟢 **MIT** — *no licence file*; `package.json` + full MIT text in README | 🟢 **2,447 c · 115 a · head 2026-10-02 · 37 c in 2026** | 🟢 **THE ONE GENUINE MISS — promoted this pass** |
| `davemckain/qtiworks` | BSD, 2,057 B, *© 2014 University of Edinburgh* | 2,073 c · 3 a · head 2023-01-04 | 🔴 **DEAD BY DECLARATION** — README line 1: *"no longer supported and is going to be closed in early 2023"* |
| `sagorbrur/bnlp` | 🟢 MIT, 1,068 B | 541 c · 10 a · head 2026-04-01 · 19 c in 2026 | 🟡 Alive, **already named on 3 shelves**. Bengali NLP substrate, not an education agent |
| `zanichellieditore/learningrecordstore-xapi` | 🟢 MIT, 1,081 B, *© 2019 **Zanichelli Editore s.p.a.*** | 🔴 30 c · 6 a · head **2020-03-18** | 🔴 **DEAD — six years.** The only institutionally-held row in the class, and dead |
| `ramsrigouthamg/questgen.ai` | 🟢 MIT, 1,076 B | 122 c · 7 a · head 2023-11-15 | 🔴 Dormant three years |
| `xcesaralejandro/lti1p3` | 🟢 MIT, 1,081 B, *© 2021 César Alejandro Mora Cid* | 97 c · 3 a · head 2025-01-03 | 🟡 Quiet 21 months. Watch |
| `paurushrai/lti-1p3-nextjs-starter` | 🟢 MIT, 1,067 B, *© 2026* | 17 c · **1 a** · head 2026-06-17 | 🟡 A starter, not a library |
| `esegrave/edfi` | 🟢 Apache-2.0, 11,356 B | 52 c · 2 a · head 2022-03-04 | 🔴 Dormant four years |
| `roncuevas/ipn_saes_utils` | 🟢 MIT, 1,079 B, *© 2026* | 🔴 **2 c** · 1 a | 🔴 Below bar. IPN/SAES Mexico — the seam is real, this code is not |
| `ridencww/uniroster-server` | 🟢 MIT, 1,066 B | 🔴 **3 c** · 1 a · head **2016-10-17** | 🔴 Below bar, ten years. Already named on 1 shelf |
| `123xiaojun/student-management-system` | 🟡 4,568 B — **not an SPDX stock text**, unrecognised | 🔴 5 c · 2 a | 🔴 Below bar. Read the payload before any use |
| `gaurav-pande/aes_dl` | 🔴 **NO GRANT** — no file, no `license` key on either manifest | — | 🔴 Default copyright reserves all rights |

🔵 **So: of twelve rows probed, one is a genuine miss, three were already carried by name, and eight are dead, dormant or below bar.** 🟢 **The shelves were right to leave them off.** 🔴 **What was wrong is that the refusal was never written down** — eight rows sat in `evidence/` with no disposition, so every pass re-discovers and re-probes them. **That is the real defect, and it is a bookkeeping defect, not a delivery one.** The remedy is a disposition ledger, not a promotion spree, and it is now the standing action in `intel/open-gaps.md`.

### 🟢 The shelf as it stands after this pass

**No new AGENT qualified this pass, and that is stated rather than padded.** The promotion this pass earned is a content-type library, not an agent; it lands in `repos/foundations.md` and `verticals/solutions.md`, where it belongs. The agent shelf is carried forward from p331 unchanged, every figure still first-hand with its measuring pass named:

| Agent / tool | Repo | Grant | Activity, first-hand | Layer |
|---|---|---|---|---|
| **lti-tool** | https://github.com/lti-tool/lti-tool | 🟢 **MIT** (1,077 B, p331) | 346 c · 6 a · 2026-10-19 · release 2026-10-20 (p331) | 🟢 LMS integration — the way in |
| **ltijs** | https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0** (11,361 B, p331) | 575 c · 17 a · 2026-10-13 (p331) | 🟡 LMS integration, mature, narrow bench |
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | head 2026-10-19 (p330) | 🟢 Agent-native tutor |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | 🟢 **MIT** (1,073 B, p331) | 467 c · 5 a · 2026-10-16 (p330) | 🟢 ITS state + review scheduling over MCP |
| **OATutor** | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1,045 c · 27 a · 2026-10-16 (p330) | 🟢 Pedagogy — BKT, UC Berkeley |
| **Agent Skills** | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** (10,173 B, p327) | 42 c (p327) | 🟢 K-12 teacher skills over MCP |
| **Evaluators** | https://github.com/learning-commons-org/evaluators | 🟡 **MIT code**; corpora **CC BY-NC-SA 4.0** (p327) | 289 c (p327) | 🟢 Pedagogy-aware evaluation |
| **os-taxonomy** | https://github.com/withmarbleapp/os-taxonomy | 🟡 **ODbL-1.0 + CC BY-SA 4.0** (25,289 B, p331) | 23 c · 3 a · 2026-10-19 (p331) | 🟢 Curriculum spine (data, not code) |

🔵 **One control worth naming, because this pass's own test suite caught it.** The audit classifies a row carrying MIT code beside a share-alike corpus as `mixed`. Ordering the single verdicts before the compound one made `mixed` **unreachable** — and the `os-taxonomy` row in the table above is exactly that shape, so it would have been filed as plain copyleft. 🟢 **The control failed, the ordering was fixed, and 40/40 now pass.** A classifier whose compound branch is dead code is a classifier that reads every mixed grant as its stricter half.

---

## Pass 331 · 2026-10-20 (fourth pass of this date) — the integration row this file has needed since p319 was already in `evidence/`, and p330's claim about it was false

🔴 **p330 closed the LTI question with two sentences that cannot both be true of this repository.** It declared `pylti1.3` dead — correct, and now confirmed on a second channel — and then named `Liberate-Labs/ltikit-sdk` *"the first permissive LTI 1.3 Advantage implementation this KB has found outside Python."*

🔴 **`evidence/p232-new-rows.2026-10-16-p232.tsv`, line 17, recorded on 2026-10-16:** `lti-tool/lti-tool` · `npm:@lti-tool/core +6 siblings` · 30 versions · latest 1.3.0 · **MIT**, 1,076 B, *© 2025-present James Joplin* · `unplaced`. **Measured fourteen passes before the claim that denies it.**

🔵 **So p330's lesson repeats one tier over.** p330: before writing *untested* about a channel, `ls compose/code/`. 🟢 **p331: before writing *first*, *only* or *none found* about an artefact, `grep -ril <thing> evidence/`.** 🔴 **This KB's discovery rate on `lti-tool` was 100% at p232 and its delivery rate was 0% through p330** — the exact failure p327 named and prescribed an audit for, still unrun. **The prescription was right; nothing executes it. It belongs in the hook tier, not in prose.**

### 🟢 The row, promoted — every figure first-hand p331, on both channels

| Agent / tool | Repo | Licence (read first-hand p331) | Activity (first-hand p331) | What it is |
|---|---|---|---|---|
| **lti-tool** | https://github.com/lti-tool/lti-tool | 🟢 **MIT** — `main/LICENSE` 1,077 B, *Copyright (c) 2025-present James Joplin* | **346 commits · 6 authors · head 2026-10-19** · 🟢 **235 commits in 2026 by 6 authors** · `@lti-tool/core` 🟢 **v1.3.1 published 2026-10-20, today** · 31 releases since 2025-10-02 | 🟢 **The complete LTI 1.3 Advantage surface in TypeScript, confirmed in code rather than from a README.** 49 core source files, 14 test files. `services/nrps.service.ts` · `schemas/lti13/ags/{lineItem,result,scoreSubmission}` · `schemas/lti13/deepLinking/contentItem` · `services/dynamicRegistration.service.ts` with `openIDConfiguration`, `registrationRequest`, `registrationResponse` · `token.service.ts` · `session.service.ts` · JWKS · five claim families, all Zod-schema'd. **Launch, AGS, NRPS, Deep Linking and Dynamic Registration are each present as code.** 🟢 **Dependency surface is two packages — `zod` and `jose`** (this KB payload-verified a **10-package** closure for `ltijs`). 🟢 **Storage is pluggable:** `packages/{memory,postgresql,mysql,dynamodb,d1,hono}` — Postgres/MySQL for a conventional deployment, **DynamoDB and Cloudflare D1 + Hono for an edge one** |

🟢 **PLACED — North America, institutionally, and p232's `unplaced` is closed.** From the commit record: **161 of 346 commits at `-0400`, 62 more at `-0500`**, and the third author domain is 🟢 **`longsight.com`, 28 commits — Longsight Inc., a US Sakai/Tsugi hosting firm.** 🔵 **This KB already holds `LongsightGroup/qti3` (MIT, 1,072 B, `evidence/full-column-grant-census.2026-10-15-p211.tsv`).** **The same house is in both rows: this is not a lone-author library, an LMS-hosting company commits to it.**

### 🔴 What this does to the two rows it replaces

| row | standing grade | measured p331 |
|---|---|---|
| `dmitry-viskov/pylti1.3` | 🔴 DEAD (p330, git channel) | 🟢 **CONFIRMED on a second channel — `PyLTI1p3` 2.0.0 uploaded 2022-11-20**, one day before the final commit. **p330 was right, and the recommendation it withdrew stays withdrawn** |
| `Liberate-Labs/ltikit-sdk` | 🟡 "complete surface, single author, quiet" | 🔴 **Worse than recorded: it does not resolve on npm at all.** 38 commits, **1 author**, **no published package.** An unpublished SDK is a vendored-source dependency — the client pins a git SHA and inherits the ownership handover. **Watch list only** |

🟢 **Recommend `@lti-tool/core` for new LMS integration work, with `Cvmcosta/ltijs` (Apache-2.0, `ltijs` 7.0.7 of 2026-10-06) as the mature alternative where a client needs a longer track record.** 🟡 **State the `ltijs` risk when you propose it:** 51 commits in 2026 but **only 2 distinct authors in 2026** against 17 lifetime, the current head is a dependabot merge, and 90 of its commits come from **`ltiaas.com` — the maintainer's commercial hosted product**. **Actively released, narrowly maintained, commercial successor in the same hands.**

### 🟢 The shelf as it stands after this pass — the rows a studio can start from

**Every figure below is first-hand, with the pass that measured it named. No star counts: `api.github.com` has returned 403 since p37, and this session's GitHub MCP tools are scope-bound (see `agents/trending.md`).**

| Agent / tool | Repo | Grant | Activity, first-hand | Layer |
|---|---|---|---|---|
| **lti-tool** | https://github.com/lti-tool/lti-tool | 🟢 **MIT** (1,077 B, p331) | 346 c · 6 a · 2026-10-19 · release **today** (p331) | 🟢 **LMS integration — the way in** |
| **ltijs** | https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0** (11,361 B, p331) | 575 c · 17 a · 2026-10-13 · `ltijs` 7.0.7 (p331) | 🟡 LMS integration, mature, narrow bench |
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | 🟢 **Apache-2.0** | head 2026-10-19 (p330) · ref resolves p331 | 🟢 Agent-native tutor |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | 🟢 **MIT** (1,073 B, p331) | 467 c · 5 a · 2026-10-16 (p330) | 🟢 ITS state + review scheduling over MCP |
| **OATutor** | https://github.com/CAHLR/OATutor | 🟢 **MIT** | 1,045 c · **27 a** · 2026-10-16 (p330) | 🟢 Pedagogy — BKT, UC Berkeley |
| **Agent Skills** | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** (10,173 B, p327) | 42 c (p327) | 🟢 K-12 teacher skills over MCP |
| **Evaluators** | https://github.com/learning-commons-org/evaluators | 🟡 **MIT code**; corpora **CC BY-NC-SA 4.0** (p327) | 289 c (p327) | 🟢 Pedagogy-aware evaluation |
| **os-taxonomy** | https://github.com/withmarbleapp/os-taxonomy | 🟡 **ODbL-1.0 + CC BY-SA 4.0** (25,289 B — re-read p331, reproduces p326 exactly) | 23 c · 3 a · 2026-10-19 (p331) | 🟢 Curriculum spine (data, not code) |

🔵 **One note on the last row, because reproducibility is worth a line.** This pass re-read `os-taxonomy`'s `LICENSE` blind and measured **25,289 bytes of genuine ODbL text** — byte-identical to p326's figure. 🟢 **The licence channel is stable across five days and two passes. No correction needed; the row was right.**

### 🟡 Measured this pass and honestly below the bar — recorded so no future pass re-spends the probe

| repo | grant, first-hand p331 | activity, first-hand p331 | verdict |
|---|---|---|---|
| `littlecookie0722/AI-Teaching-Agent` | 🟢 MIT, 1,069 B, *© 2026 littlecookie* | 30 c · 2 a · 2026-08-23 | 🟡 **Watch.** Labs/exams/grading DSLs, CLI + MCP; its README freezes automatic grading |
| `HumphreySun98/Smart-Study-Agent` | 🟢 MIT, 1,067 B, *© 2026 Haofei Sun* | 28 c · 3 a · 2026-08-16 | 🟡 **Watch** for the Anki-export + local-Ollama limb only |
| `mizcausevic-dev/mcp-ai-tutor` | 🔴 **AGPL-3.0**, 34,523 B | 10 c · 2 a · 2026-08-05 | 🔴 Not embeddable and too small. The **FERPA/COPPA procurement-audit idea** is the only takeaway |
| `mthatipamula/educational-assessment-ai-agent-platform` | 🔴 **NO LICENCE** — `LICENSE`, `LICENSE.md`, `LICENSE.txt` all fail to resolve on `main` and `master` | **3 c** · 2 a · 2026-10-13 | 🔴 **Unusable.** The most complete K-12 assessment-agent *design* the search channel produced this pass, and **three commits with no grant.** Default copyright reserves all rights |
| `rohit-dev45/programming-tutor-agent` | — | 19 c · **1 a** · 2026-09-15 | 🔴 Below bar |
| `kvnloo/tutor-mcp` | 🟡 MIT 1,073 B — *© 2026 **Arnaud Guiovanna*** | 452 c · 5 a · 2026-10-02 | 🟡 **A fork.** Same holder and licence byte-length as the canonical `ArnaudGuiovanna/tutor-mcp` (467 c, 2026-10-16). **No change to the shelf** |
| `Godmartinz/Node-LTI-1.3-library` | — | 125 c · 6 a · default **2019-08-02**, newest ref 2022-12-30 | 🔴 **DEAD — seven years** |

🔵 **The fork rule, since the search channel will do this again: when two slugs share a LICENSE byte-length and copyright holder, the one with fewer commits and an older head is downstream.** **One `curl` of each `LICENSE` settles it without a star count.**

---
# Top open source AI agents — education

## Pass 330 · 2026-10-20 (third pass of this date) — p329 declared a channel untested that this KB built, tested and documented a fortnight ago, and the LTI library this file has recommended four times has been dead since 2022

🔴 **p329 closed with this line in its verification table: `gitlab.com` — *"🟡 301 — **responds** — an untested supply channel; next pass should sweep it"*.** 🟢 **`compose/code/gitlab-api-channel/` has existed since 2026-10-06.** It is a 7,558-byte instrument with a 10,287-byte test suite that passes **32/32 offline and 35/35 live**, it holds **534 projects** from a 25-term English sweep plus **141** from a 16-term Spanish/Portuguese sweep in `data/`, and it carries three named findings (`P-GL-1`, `P-GL-2`, `P-GL-3`). **This pass re-ran the suite: 32/32, today.**

🔵 **So this is the sixth narrowing in a sequence that has now run eight days, and it has moved one step further out than p329's own.** p324/p325: a declared gap is a statement about the **query**. p326: the **filter**. p327: the **write**. p328: the write's **target**. p329: a **channel this base already held**. 🔴 **p330: a channel this base already *built an instrument for*, *tested*, *documented* and *filed in its own `compose/code/` tree* — and then declared untested fourteen days later.** **p329 diagnosed "capability present, instruction already written, not exercised" and then committed the same error in the same sentence it used to diagnose it.**

🟢 **The remedy is one command, and it is cheaper than the sweep it prevents.** Before any pass writes the words *untested*, *unreachable* or *never swept* about a channel: `ls compose/code/ | grep -i <channel>`. **386 directories sit in `compose/code/`.** No pass can hold that inventory in prose, and **no pass has to** — the directory names are the index. 🔵 **The general form, and it is the one worth carrying: this KB's declared gaps have been getting cheaper to close for six passes straight, and the reason is that they keep turning out to be statements about the KB rather than about the world. A gap about the world costs a sweep. A gap about your own `ls` costs nothing.**

### 🔴 The finding that changes a recommendation: `pylti1.3` has been dead for forty-seven months

**This file and `repos/foundations.md` have carried `dmitry-viskov/pylti1.3` since p319 as — their words — *"the repo that gets your agent into the client's existing LMS"*, re-verified at p319, with the caveat *"still no published release — pin a commit".* 🔴 **The caveat was the wrong one.** Measured first-hand this pass on the git channel, across **every ref, not just the default branch**:

| measure | value, first-hand p330 |
|---|---|
| commits | 178 |
| authors | **16** — it had a community |
| last commit, `master` | 🔴 **2022-11-21** |
| newest ref of **any** kind | 🔴 **tag `2.0.0`, also 2022-11-21** |
| last substantive commit | 🔴 *"Support Python 3.11 (#106)"* |

🔵 **"No published release" reads as a young project. "Sixteen authors, 178 commits, and nothing on any branch or tag in forty-seven months" reads as an abandoned one, and they are opposite procurement facts.** 🔴 **Its last feature was support for Python 3.11; `artcc/freelingo`, a row added below in this same pass, ships on Python 3.14.** **A library whose newest supported runtime is three releases behind the artefacts that would depend on it is not a dependency, it is a fork.** 🟢 **This is `intel/trends.md` trend 15 — the foundations tier aging while the agent tier is live — landing on the single row this KB told clients to build their LMS integration on.**

### 🟢 And the correction cuts the other way too: the Tsugi question, closed negative at p323, is answered positively — by the code

**p322 asked which LTI versions `tsugiproject/tsugi` implements. p323 answered: *"An LTI integration cannot be scoped from Tsugi's README"*, recording that none of LTI 1.1, LTI 1.3, Advantage, Deep Linking or NRPS is named anywhere in it.** 🔴 **That was a code question answered from documentation, and it produced a false negative that this KB has carried for seven passes.** The tree, enumerated first-hand this pass:

| capability | the files that implement it |
|---|---|
| **LTI 1.3** | `lib/src/Util/LTI13.php`, `lib/src/Services/Outbound/Lti13TestLaunch.php` |
| **AGS** (Assignment & Grade Services) | `ims/ags/route.php`, `lib/src/Controllers/Ims/Ags.php`, `lti/ags.php` |
| **NRPS** (Names and Role Provisioning) | `ims/nrps/route.php`, `lib/src/Controllers/Ims/Nrps.php` |
| **Deep Linking** | `lib/src/Util/DeepLinkRequest.php`, `lib/src/Util/DeepLinkResponse.php`, `lib/src/Core/DeepLinkResponse.php` |
| 🟢 **and it is tested** | `lib/tests/Util/LTI13Test.php`, `lib/tests/Services/Outbound/Lti13TestLaunchTest.php` |
| **LTI 1.1 as well** | its own commit, 2026-10-18: *"Note that upward is set from an LTI 1.1 result."* |

**Activity, first-hand: 4,012 commits · 47 authors lifetime · last commit 2026-10-19 · 486 commits in 2026.** 🟡 **One qualifier that belongs in the same breath: those 486 commits in 2026 come from *three* authors, and the overwhelming majority from Charles Severance himself.** **Apache-2.0, alive, complete on the Advantage surface, and a bus factor of roughly one.**

🔵 **Put the three readings together and the LTI picture this KB has published is wrong in its shape, not just its details. It has been reporting a dying integration layer. What the code shows is a *bifurcated* one:**

| ecosystem | artefact | grant | state, first-hand p330 |
|---|---|---|---|
| **PHP** | `tsugiproject/tsugi` | Apache-2.0 | 🟢 **Alive** — 4,012 commits, 47 authors, yesterday. Full Advantage surface, tested |
| **Python / Django** | `dmitry-viskov/pylti1.3` | MIT | 🔴 **Dead** — nothing on any ref since 2022-11-21 |
| **Python / Django** | `openfun/django-lti-toolbox` | MIT | 🔴 **Dead** — 34 commits, 6 authors, last 2024-11-14 (p325's figure, confirmed exactly) |
| **JS / TS** | `Liberate-Labs/ltikit-sdk` | 🟢 **MIT** | 🟡 **New, complete, and quiet since an ownership transfer** — below |

🔴 **The consequence for a bid is direct, and it reverses this KB's standing advice: if the integration must be LTI and the stack is Python, there is no maintained permissive library to point at.** **Tsugi is the one living, complete, permissive LTI implementation in this KB, and it is PHP.**

### 🟢 The new row: a second permissive LTI 1.3 Advantage implementation exists, and it is not Python

| field | value, read first-hand from shipped bytes this pass |
|---|---|
| repo | https://github.com/Liberate-Labs/ltikit-sdk |
| grant | 🟢 **MIT** — `main/LICENSE`, **1,063 B**, *Copyright (c) 2026 alasim* |
| activity | **38 commits · 1 author** (`hasanmahmud@liberate-labs.com`, all 38) · **2026-07-04 → 2026-07-10** · 212 files |
| the surface, **from the tree, not the README** | `packages/core/src/ags.ts`, `nrps.ts`, `deep-linking.ts` — 🟢 **each with its own `.test.ts` beside it**; 16 test files in all |
| shape | monorepo: `core` + framework packages `next`, `hono` + **four storage adapters** — `memory`, `prisma`, `redis`, `supabase` |
| claims | README: *"Verified live against **Canvas** and **MoodleCloud**: SSO, deep linking, grade passback (AGS), and roster (NRPS)"*; 1.0-rc with **Dynamic Registration** and **cookieless launches (Platform Storage)** |
| region | 🔴 **UNPLACED** — `liberate-labs.com` carries no country signal and no commit offset was decisive |

🔵 **Why it matters: it is the first permissive LTI 1.3 Advantage implementation this KB has found outside Python, it targets serverless and edge rather than a long-running server, and it was verified against live Canvas and MoodleCloud by its author.** 🔴 **Why it does not relieve the concentration risk this KB has flagged for four passes:**

1. **One author, every commit.** The risk was never "only one library" — it was "only one maintainer". **Swapping a dead single-maintainer library for a live single-maintainer library does not change the shape, it changes the date.**
2. 🔴 **The last three commits on `main` are an ownership handover, not code** — *"update package metadata and version numbers across multiple packages to reflect **new ownership**"*, *"update repository links and author information"*, *"update sitemap URL ... to reflect new domain"*, all on **2026-07-10**. The last functional commit is `1.0.0-rc.4` on 2026-07-08.
3. 🟡 **The automation is alive and nobody is landing it.** Seven `dependabot/` branches run forward to **2026-10-07** — `hono`, `next`, `astro`, `vitest`, `sharp`, `mermaid`, `next-auth` — and **not one is merged into `main`.** **A repository whose bots are three months ahead of its humans is a repository between owners.**

🟢 **Use it, and budget for it: it is the right starting point for a JS/TS LTI tool and the only permissive one, and it should be forked and pinned rather than depended on.**

### 🟢 The placement method the activity channel also pays, and it closes both of this file's 🔴 UNPLACED rows

🔵 **p329 opened the git channel for *activity* and stopped there. The same clone carries author identity and commit offset, and this KB has rows sitting at 🔴 UNPLACED whose placement evidence was inside the object it already fetched.** Two signals, in strict priority:

1. 🟢 **Author email domain — institutional, strongest.** An `.edu`, `.ac.uk` or ministry domain is a *declaration* of affiliation, not an inference.
2. 🟡 **Commit UTC offset — locates the keyboard, not the person.** Usable only when every commit agrees, and it is evidence of *where the work was done*, never of nationality.

| row | evidence, first-hand p330 | placement |
|---|---|---|
| `Jellypod-Inc/school-skills` | `pierson@jellypod.ai`; **all four commits at `-0700`** (US Pacific) | 🟢 **North America** — was 🔴 UNPLACED since p328 |
| `afri-bit/revibe` | `afribit.tech@gmail.com`; **all four commits at `+0200`** (Central European Summer Time) | 🟢 **EMEA** — was 🔴 UNPLACED since p328. 🟡 **Read the signal honestly: the author's name is Indonesian and the keyboard was in a UTC+2 locale. This places the work, not the person** |
| `Gchism94/jupyterquest` (new below) | 🟢 **`gchism@arizona.edu`, 124 of 249 commits** | 🟢 **North America — institutionally attributed, first-hand.** University of Arizona |

🔴 **The declared limit, because this signal is easy to over-read:** a commit made through the GitHub web editor carries the browser's offset, and any local `git config` can be wrong or set to UTC. **One commit's offset establishes nothing. A unanimous offset across every commit in a small repository is evidence; it is still weaker than a domain.**

### The sweep: four usable grants, three rejections, and one asserted repository that does not exist

| repo | grant, read first-hand p330 | activity, first-hand p330 | verdict |
|---|---|---|---|
| `Liberate-Labs/ltikit-sdk` | 🟢 **MIT** (1,063 B) | 38 · 1 author · 2026-07-10 | 🟢 **SHELF** — above, and cut into `## The table` |
| `Gchism94/jupyterquest` | 🟢 **MIT** (1,070 B, *© 2024 Greg T. Chism*) | 249 · 3 authors · **2026-05-07** | 🟢 **SHELF** — `.ipynb` autograder, Zenodo DOI, Codecov, CI. 🟡 Five months quiet |
| `ictinnovations/ictexam-mcp` | 🟢 **MIT** (1,114 B, *© 2026 Tahir Almas, ICT Innovations*) | 5 · 1 author · 2026-09-08 | 🟡 **RECORDED, not shelf** — five commits. Its *pairing* is the finding, below |
| `artcc/freelingo` | 🔴 **AGPL-3.0** (34,514 B) | **1,168 · 7 authors · 2026-10-16** | 🟡 **READ, DO NOT EMBED** — below |
| `Gchism94/ai-tutor` | 🟢 MIT (1,070 B) | — | 🔴 **SUPERSEDED by its own README** — *"in the process of being consolidated into jupyterquest"*, and self-labelled *"not yet production-ready"* |
| `BlackyDrum/ai-tutor` | 🟢 MIT (1,067 B, *© 2024*) | 818 · 3 authors · 🔴 **2024-10-19** | 🔴 **REJECTED — two years silent.** Laravel/Vue/Postgres; substantial and abandoned |
| `sumitchopkar2005/Agentic_AI_LMS` | 🔴 **NO GRANT** (main+master, four filenames) | — | 🔴 **NOT USABLE.** A 28,267-byte README claiming Canvas/Moodle-class LTI 1.3 over an unlicensed tree |
| `projectremedy-ai/remedy-canvas-lti` | 🔴 — | 🔴 **clone failed; `raw` 404** | 🔴 **DOES NOT EXIST.** The search channel returned it with a full capability description: *"Canvas LTI 1.3 tool that scans entire courses for WCAG 2.2 AA accessibility issues and remediates them in-place"* |

🔴 **That last row is the third time in three passes the search channel has asserted a repository that the byte channel cannot find** (p329: `Naresh1401/education-tutor-agent` and `techpivot25/Educate-AI` asserted as *"MIT licensed"* with no grant in either). 🔵 **The pattern is now specific enough to name: the search channel's *descriptions* are fluent and its *existence claims* are not load-bearing.** **Nothing from it enters this KB until a 200 from `raw.githubusercontent.com` or a successful clone.** 🟡 **And note what was lost with this one: WCAG 2.2 AA remediation inside an LMS would have been a new category here and a direct answer to the European Accessibility Act and Section 508. The gap is real; the artefact was not.**

### 🟡 `freelingo` — the largest live AGPL education artefact this KB has measured, and the licence is the whole decision

**MIT is not available here and the project is not trying to offer it.** `artcc/freelingo`: **AGPL-3.0, 34,514 B, 1,168 commits, 7 authors, last commit 2026-10-16** — against `ChatTutor`'s 193 commits and nine months of silence, this is what a *living* AGPL education project looks like. Self-hosted AI language learning: **CEFR A1–C2** curriculum organised into units, LLM-assessed level placement, generated study plan, listening and reading exercises, voice practice; **Ollama, OpenAI, Anthropic or DeepSeek**; Next.js 16, Python 3.14; v1.10.40. **Region: EMEA** 🟡 *(inferred — `Arturo Carretero Calvo` authored 1,064 of 1,168 commits; a Spanish personal name, no institution and no country declared anywhere in the repository)*.

🔴 **The architecture of its business model is the thing to read, and it is why the licence is deliberate.** The README states it plainly: self-hosting is free under AGPL-3.0, and a **hosted service** with paid subscriptions is operated by the same team. 🔵 **AGPL §13 is not an accident in that design — it is the mechanism that makes the hosted tier defensible, because it is exactly what stops a competitor from running the code as a service without reciprocating.** **Read it for the CEFR ladder and the multi-provider speech path; do not put it in a client deliverable you intend to host.**

### 🟢 LTI and MCP in one vendor's shipping code — the cleanest evidence trend 6 has had

**`ICT Innovations` ships both halves and licenses them differently, and the split is by layer, not by preference:**

| layer | artefact | grant, first-hand | protocol |
|---|---|---|---|
| **teacher's agent → exam platform** | `ictinnovations/ictexam-mcp` | 🟢 **MIT**, 1,114 B | **MCP** — read exams, gradebooks, per-question item analysis; write mode off by default |
| **student → exam, inside the LMS** | `ictinnovations/moodle-mod_ictexam` | 🔴 **GPL-3.0**, 35,149 B (**obligatory** — it is a Moodle plugin) | **LTI 1.3** launch, embedded in the course page |

🔴 **And the detail that only the tree shows: the score does not come back over AGS.** The plugin's README requires the backend to be registered *"as an LTI 1.3 tool, with IMS LTI Assignment and Grade Services and IMS LTI Names and Role Provisioning enabled"* — and the grade is then written by **`classes/external/set_grade.php`, a Moodle web service (`mod_ictexam_set_grade`)**, with raw marks stored rather than percentages. 🔵 **So the shipping answer to "how does the score get back" is: LTI carries the student *in*, and a vendor-specific web service carries the mark *out*, on a site where AGS is switched on and unused.** 🟢 **This is the second artefact in this KB (after `LTIPlugin`) to show the passback path concretely, and the first to show a team choosing not to use the standard one they had already enabled.** **Quote it when a client assumes LTI Advantage conformance means the gradebook path is the standard path.** 🟡 Both repositories are small — 5 and 4 commits — and `classes/privacy/provider.php` is present, so the GDPR privacy API is implemented. **Recorded as an architecture exhibit, not a dependency.**

### 🔴 The self-hosted forge question, pre-registered as action B at pass 23, executed and closed with a negative

**`compose/code/gitlab-api-channel/` declared limit 6: *"`gitlab.com` is one instance. Every self-hosted GitLab — which is where the European public sector actually runs this software — is invisible to this channel. Pre-registered as action B of pass 23."*** 🟢 **Executed this pass. Thirteen hosts, `GET /api/v4/projects?per_page=1`:**

`code.europa.eu` · `gitlab.opencode.de` · `gitlab.gwdg.de` · `git.rwth-aachen.de` · `gitlab.inria.fr` · `salsa.debian.org` · `forge.apps.education.fr` · `gitlab.bsz-bw.de` · `gitlab.tuwien.ac.at` · `codeberg.org` · `git.sr.ht` · `framagit.org` · `gitlab.freedesktop.org`

🔴 **All thirteen: `000` — no connection established.** 🔵 **The result is cleaner than "blocked", and it is worth stating precisely: the reachable surface is an allowlist of specific hosts, not a property of the protocol.** `gitlab.com/api/v4` answers **200** and `gitlab.gwdg.de/api/v4` answers nothing — **same software, same endpoint, same request.** 🟢 **So action B is closed as unreachable-by-environment rather than left open as untried, and the standing consequence is recorded once instead of rediscovered: French, German and EU-institutional education code hosted on sovereign forges — which is a large share of what EMEA public-sector buyers actually run — cannot be measured from here at all.** 🔴 **This KB's EMEA coverage is therefore structurally biased toward whatever European projects also mirror to GitHub.** **That is a property of the instrument, and every EMEA count in this base should be read as a floor.**

### The verification surface, p330

| host / channel | p329 | p330 | consequence |
|---|---|---|---|
| `raw.githubusercontent.com` | 200 | 🟢 **200** | grants, bytes, READMEs first-hand |
| **git smart-HTTP** (`clone --filter=blob:none`) | 🟢 200 | 🟢 **200** | commits, authors, dates, **all refs**, tree enumeration, **author domains and commit offsets** |
| `gitlab.com/api/v4` | 🟡 "301, untested" | 🟢 **200 — and instrumented since 2026-10-06** | ★, forks, topics, `last_activity_at`, licence key, file payloads |
| `github.com` (rendered) | 403 | 🔴 **403** | no stars, forks, topics |
| `api.github.com` | 403 | 🔴 **403** | same |
| **13 self-hosted / alternative forges** | not tested | 🔴 **000 × 13** | **closed negative — see above** |
| `arxiv.org`, `huggingface.co` | 403/000 | 🔴 **000** | no scholarly corroboration |


## Pass 329 · 2026-10-20 (second pass of this date) — the quantitative column in the table below measures the one channel that is 403, and this file told itself to stop ten passes ago

🔴 **p319 wrote the instruction five lines above `## The table`, in this file, and this file never obeyed it:** *"the ★ column is a rough size signal and nothing more. **Rank on commit count, release cadence and licence.**"* 🔴 **Ten passes later the table's only quantitative column is still `★`, and p328 — unable to reach `github.com` — filled that column with `🔴 n/v` for every row it cut.** 🟢 **The commit channel was open the whole time.** `git clone --filter=blob:none --no-checkout` on third-party public repositories returns **200** through this proxy while `github.com` and `api.github.com` both return **403**, and **this KB has known that since p229** (`repos/trending.md:1717` records it superseding p306).

🔵 **So this is the fifth narrowing in a sequence that has run all week, and it is the same shape as the fourth.** p324/p325: a declared gap is a statement about the **query**. p326: about the **filter**. p327: about the **write**. p328: about the write's **target**. **p329: about a channel this base already held, already documented, and did not exercise.** 🔴 **p327's ten rows were found and never written; p328's metadata gap was declared against a channel that was open, known-open and documented-open in this KB's own files.** **Capability present, instruction already written, not exercised — twice in three passes.**

🟢 **What the channel pays, measured this pass over 13 repositories** (`evidence/p329-git-activity-channel.2026-10-20-p329.tsv`): commit count, author count, first and last commit date, and full tree size — **all first-hand, none of it solicited.** 🔵 **This matters beyond convenience, and it is this file's own trend 11 argument turned into a remedy: a star is a number strangers can be asked to inflate — p318 found a README asking agents for stars, p319 found that pressure productised with a unit test — whereas a commit history is the project's own record of whether anyone is still there.** **This KB did not lose its attention signal and gain nothing. It lost a gameable signal and recovered a better one.**

### 🔴 The naive version of this fix is wrong, and one row proves it

**Do not adopt commit count as the column.** The two repositories below are **identical on commit count and opposite in fact**:

| repo | commits | authors | last commit | what it actually is |
|---|---|---|---|---|
| `anthropics/k12-teacher-skills` | **4** | **3** | **2026-10-13** (7 days) | 🟢 **Small by design.** A four-skill bundle is a small artefact; three authors and a commit last week say it is tended |
| `Jellypod-Inc/school-skills` | **4** | **1** | **2026-04-14** (6 months) | 🔴 **A single-sitting dump.** All four commits landed on **one day** and nothing has touched it since |

🟢 **So the signal is a triple — `(commits, authors, last_commit)` — not a scalar.** p319 half-knew this: it said *"commit count, **release cadence** and licence"*, and cadence is the term that separates these two rows. **A scalar column would have condemned a live Anthropic/Learning Commons artefact and spared an abandoned one.**

### 🟢 The re-grade, and it lands on two rows p328 promoted yesterday

| repo | commits | authors | last commit | p329 verdict |
|---|---|---|---|---|
| `HKUDS/DeepTutor` | **2,935** | **273** | 2026-10-19 | 🟢 **The largest education agent on this shelf by every first-hand measure** |
| `Orenda-Project/rumi-platform` | **847** | 11 | 2026-10-05 | 🟢 **LIVE** — and this file's prose figure *"847 commits on 18 stars"* is now **first-hand exact** |
| `eai6/ai-tutor` | **787** | **4** | **2026-08-20** | 🟡 **Substantial but two months stale**, and the World Bank attribution rests on **four committers** — a qualifier p328 could not see when it called this *"the reference build"* |
| `THU-MAIC/OpenMAIC` | **733** | **127** | 2026-10-19 | 🟢 **LIVE, and 127 authors corroborates the multi-institution claim first-hand** — the strongest permissive row here |
| `HugeCatLab/ChatTutor` | 193 | 11 | **2026-01-09** | 🔴 **AGPL-3.0 *and* nine months stale.** Do not embed it; nobody is maintaining it either |
| `microsoft/Shiksha-Copilot` | **149** | 6 | 2026-09-15 | 🟢 **The 9-★ cell understated this repo badly** — exactly p317's finding that stars run low on institutional infrastructure |
| `learning-commons-org/agent-skills` | 42 | 6 | 2026-10-06 | 🟢 **LIVE**, small by design |
| `Jellypod-Inc/school-skills` | 4 | 1 | **2026-04-14** | 🔴 **RE-GRADE — single-sitting dump, silent 6 months** |
| `afri-bit/revibe` | 4 | 2 | **2026-05-02** | 🔴 **RE-GRADE — two-day dump, silent 5 months** |

🔵 **The honest reading of the two re-grades: p328 did nothing wrong in promoting them — their grants are MIT and byte-verified, and that was the only axis it could measure.** 🔴 **But the table presented a four-commit abandoned skill dump beside a 733-commit, 127-author live project with no way for a studio lead to tell them apart.** **The `★ / activity` column below now carries the triple for every row this pass measured; rows it did not measure keep their carried star figure and are marked so.**

### The sweep: five new repositories, zero shelf-grade, and the reason is systematic

🟡 **The topic-index channel p328 introduced works — it returned five repositories genuinely new to this KB — and its yield at the shelf tier this pass is zero.** Recorded as a measured result per the standing rule, not as silence:

| repo | grant, read first-hand p329 | activity | verdict |
|---|---|---|---|
| `DanielG0798/CourseGuide-AI` | 🟢 **MIT** (`main` + `master/LICENSE`, 1,068 B, *Copyright (c) 2026 instruct.ai*) | 9 commits, 2 authors, 2026-09-16→21 | 🟡 **Course project** — FGCU, CEN 4930 *AI Agent Studio*, Fall 2026. **North America.** Honest README; one reusable idea, below |
| `KayvanShah1/VirtuTA` | 🟢 **MIT** (1,068 B, *Copyright (c) 2024 Kayvan Shah*) | 73 commits, 2 authors, 2024-04→**2026-03** | 🟡 **Course project** — USC, DSCI 560. **PLACED North America this pass**; measured on the trending channel in an earlier pass and never region-placed |
| `bhakthan/AI_Agent_School` | 🟡 MIT (1,060 B) — but the copyright line is the **unedited GitHub template default, *"Copyright GitHub, Inc."*** | 348 commits, 1 author, **all within 2025-06-25→2025-08-01** | 🔴 **REJECTED on two independent grounds**: dead 14 months, **and it is the wrong category** — it teaches *about* AI agents (A2A, MCP, ACP, AutoGen) rather than being an agent *for* education |
| `Naresh1401/education-tutor-agent` | 🔴 **NO GRANT** — see the finding below | 5 commits, 2026-03-26→10-11 | 🔴 **NOT USABLE.** Search channel asserted *"MIT licensed"* |
| `techpivot25/Educate-AI` | 🔴 **NO GRANT** — see the finding below | 8 commits, **2026-10-12→15** | 🔴 **NOT USABLE.** Four days old; `package.json` `name` is still the scaffold value `react-example` |

🔵 **The channel's defect is *tier*, not precision.** Every one of the five is genuinely an education repository — the filter is not leaking — but a topic index ranks what carries education keywords in a description, and **what carries those keywords is coursework and learning material.** 🟡 **Two of the five are university course projects, one is a learning platform about agents, and two are unlicensed prototypes.** **So the topic-index sweep is worth keeping as a supply channel and should not be expected to produce shelf rows; the organisation-page channel p327 found remains the only channel that has produced a shelf row from a cold start.**

🔴 **And one category rule, recorded because this is the third time it has cost a pass: *"learning about AI"* is not *"AI for education"*.** `bhakthan/AI_Agent_School`, `ed-donner/agents` and `rohitg00/ai-engineering-from-scratch` are all AI-engineering curricula. **They rank first on every education-shaped agent query and belong to a different industry KB.** Rejected here by rule, not re-adjudicated each pass.

### 🟢 One reusable idea from a course project, which is the right way to spend a prototype

**`CourseGuide-AI` externalises the thing `ai-tutor` hardcodes.** `ai-tutor` ships a **three-level hint ladder** fixed in code. CourseGuide-AI loads an **instructor-defined policy** — *allowed help levels, approved sources, style constraints* — classifies the kind of assistance a student is asking for (*concept, hint, setup check, next step, analogy*), and returns a **progressively limited** response. It ships an MCP server over stdio and `pytest` cases in `tests/m2/test_cases.yaml`. 🔵 **Nine commits of prototype are not a deliverable, but "permitted help level as instructor-configurable policy rather than as a constant in the tutor" is the control surface every academic-integrity conversation in `compose/patterns.md` P11 actually needs — and it is the piece a faculty senate signs off on.** Carried into **P23**.

### 🔴 The verification surface, and the one channel that changed

| host | p328 | p329 | consequence |
|---|---|---|---|
| `raw.githubusercontent.com` | 200 | 🟢 **200** | grants, bytes, code, READMEs first-hand |
| **git smart-HTTP** (`git clone --filter=blob:none`) | 🔴 not exercised | 🟢 **200 — OPEN** | **commits, authors, dates, full tree enumeration** |
| `github.com` (rendered) | 403 | 🔴 **403** | no stars, forks, topics, description |
| `api.github.com` | 403 | 🔴 **403** | same |
| `gitlab.com` | not tested | 🟡 **301** | **responds** — an untested supply channel; next pass should sweep it |
| every non-GitHub host tested (16) | 403/000 | 🔴 **403 at CONNECT / 000** | **no procurement, scholarly or institutional corroboration** — see `intel/market.md` |

## Pass 328 · 2026-10-20 (first pass of this date) — the ten rows were written into the pass log, not onto the shelf, and the new find is MIT with a multilateral funder on the copyright line

🔴 **p327 said the constraint on this KB is execution, not discovery. It was right, and it then executed into the wrong file region.** Its own evidence file `evidence/p327-promotion-execution.2026-10-19-p327.tsv` marks all ten p296 promotions `written: YES` against a target of `agents/top.md` or `repos/foundations.md`. **Both claims are literally true and one of them is useless.** A `grep -n` this pass puts every agent-tier promotion at **lines 12–33 — inside p327's own narrative** — and **0 of them inside `## The table`**, which begins at the line this pass renumbers and is the only region of this file shaped like a shelf.

🔵 **So the audit p327 prescribed — re-grep every `PROMOTE-*` verdict against the shelf files — passes when you grep the file and fails when you grep the shelf.** `repos/foundations.md` is fine: that file's convention is one `### The rows` ledger per pass, so a row cut into the pass section *is* on the shelf. 🔴 **`agents/top.md` does not share that convention.** It carries a single canonical `## The table` plus a running commentary above it, and a row that lands in the commentary is a row a studio lead reading the table cannot see. **The largest permissive education agent this KB has ever recorded — `OpenMAIC`, MIT, 41.1k ★ — was invisible in the table for one full day after being found, graded and region-placed.**

🟢 **The diagnosis, and it is the fourth in a four-pass sequence that has been narrowing all week.** p324/p325: a declared gap is a statement about the **query**. p326: about the **filter**. p327: about the **write**. **p328: about the write's *target*.** A KB with per-pass ledgers in one file and a canonical table in another cannot audit both with one `grep`, and the file whose convention is weaker is the file that silently drops rows. 🔵 **The audit has to name the shelf region, not the filename.** Stated as a command, and it is the one this pass ran: `sed -n '/^## The table/,/^## /p' agents/top.md | grep -c <slug>`.

🟡 **This pass therefore cuts nine rows into `## The table` itself** — the six carried promotions plus three genuinely new finds — and adds the verification caveat below, which is not optional this pass.

### 🔴 The verification surface narrowed between p327 and p328, and it narrowed on exactly one layer

| host | p327 | p328 | consequence |
|---|---|---|---|
| `raw.githubusercontent.com` | 200 | 🟢 **200** | **grants, file bytes, code and READMEs are first-hand** |
| `github.com` (rendered repo page) | 200 — p327 read licences *from the sidebar* | 🔴 **403** | **no stars, no forks, no commit counts, no topics, no description** |
| `api.github.com` | blocked | 🔴 **403** | same |
| `arxiv.org`, `huggingface.co`, `unesco.org`, `codeberg.org` | 403 | 🔴 **000 (no connect)** | no scholarly or institutional corroboration |

🔵 **The practical reading, and it is worth more than the inconvenience.** The channel that died is the **attention** channel; the channel that held is the **grant** channel. **This KB's own trend 11 has argued for ten passes that the sector's published metadata is unreliable in both directions — star counts solicited, licences misdeclared in README badges.** 🟢 **Losing stars costs this pass almost nothing; losing `raw` would have cost it everything.** So: **every licence, byte count, file path, model field and code claim below was read out of shipped bytes this pass. Every star count below is carried from a prior pass and explicitly marked `carried`, or marked `n/v` — never presented as verified today.**

### 🟢 The find of this pass: an MIT, World-Bank-attributed, production-shaped curriculum tutor

| field | value, read first-hand from shipped bytes this pass |
|---|---|
| repo | https://github.com/eai6/ai-tutor |
| grant | 🟢 **MIT** — `main/LICENSE` **and** `master/LICENSE`, both 1,090 B, *"Copyright (c) 2026 **World Bank Group and contributors**"* |
| attribution | README `## Contributors` names **World Bank Education Team** and a development lead |
| stack | `requirements.txt` (4,562 B): **Django 6.0.2**, `anthropic==0.79.0`, `openai==2.20.0`, `google-genai==1.65.0`, DRF + SimpleJWT, `psycopg2`, `django-storages[azure]`. 🔵 A dated engineering decision is left in the file as a comment: *"chromadb removed 2026-05-24 — vectors now in Postgres via **pgvector**"* |
| code, not prose | all **seven** Django apps resolve as real files: `apps/{accounts,curriculum,tutoring,dashboard,llm,media_library,safety}/models.py` → 200. `config/settings.py` 17,064 B. `manage.py` 662 B |
| ★ | 🔴 **n/v — metadata channel 403 this pass** |
| region | **EMEA** — Seychelles; `seed_seychelles` ships 7 geography + 8 mathematics units |

🟢 **Why this is the most useful single row added to this file in thirty passes: it is the thing four of this KB's own patterns assumed a client would have to build.** Read out of the code and the README, not inferred:

- **Pedagogy is structural, not a prompt.** The **5E model** (Engage · Explore · Explain · Practice · Evaluate) is a **phase tag on every `LessonStep`**, and `LessonStep` has five types (`teach`, `worked_example`, `practice`, `quiz`, `summary`). **Socratic by construction** — the README states the tutor never gives direct answers — with a **three-level hint ladder** before any answer is revealed.
- **Mastery gating is real.** Automatic **skill-graph construction with prerequisite detection**; lessons **locked until prerequisites are mastered**; **interleaved retrieval practice**; **remediation routed before an exit-ticket retake**.
- **Assessment is specified, not hand-waved.** **35-MCQ bank per lesson, 10 sampled per session, 8/10 to pass.**
- **Content generation is the ingest path a ministry actually has.** Upload a **curriculum PDF/DOCX** → lesson steps, media, exit tickets and a skill map.
- 🟢 **The compliance layer is in the models, and I read the models.** `apps/safety/models.py` (3,217 B): `SafetyAuditLog` with an `EventType` enum carrying **`consent_given` / `consent_withdrawn`**, a **pseudonymised `user_hash` (16 chars)**, a `severity` field and three composite indexes; `ConsentRecord` with a `ConsentType` enum including **`parental`**, a `withdrawn_at` timestamp and `unique_together = ['user', 'consent_type']`. Management commands **`export_user_data`**, **`delete_user_data`**, **`safety_cleanup`**. 🔵 **Consent withdrawal modelled as a first-class timestamped event, with parental consent as its own type, is the single artefact every ministry and district procurement question in `compose/patterns.md` P9 and P4 asks for — and this KB has never before held it under a permissive licence.**
- **Deployment is documented to the point of being copyable.** Multi-tenancy is institution-scoped; Docker; **Azure Container Apps** with a *"fork & deploy to your own Azure"* walkthrough and a CI/CD workflow; **local Ollama** is a first-class provider, so the no-cloud variant is a config change rather than a port.

🔴 **Three honest limits, and the third is the interesting one.**
1. **The institutional attribution is self-declared.** The copyright line and the contributors list name the World Bank Group; the repository sits in a **personal namespace** (`eai6`), not a World Bank organisation. **The grant is MIT either way — that part is byte-verified — but the affiliation could not be corroborated this pass** because `github.com`, `api.github.com` and `worldbank.org` are all unreachable from here. **Do not put "World Bank project" in a bid on this evidence; "MIT, with the World Bank Group on the copyright line" is what the bytes support.**
2. **The staging URL in the README does not answer** (`000`, Azure Container Apps host). Evidence of intent to deploy, not of a live deployment.
3. 🟡 **The open artefact and the announced national programme appear not to be the same stack.** A World Bank 2026 Annual Meetings transcript has a Seychelles minister describing a national "smart education" rollout built on a **personalised Grok tutor** — a proprietary xAI model. **This repository is multi-provider and MIT.** 🔵 **Both can be true at once (a pilot and a scale-up, or two parallel efforts), and this pass does not resolve it — it records it, because the gap between the open artefact and the procured stack is the thing a studio actually sells into.** 🔴 **The transcript's "5,000 schools / one million students" figure is not carried anywhere in this KB: Seychelles' entire population is under 150,000, so that number belongs to another country in the same session.**

### Two more new rows, both MIT, both honestly unplaced

| repo | grant, read first-hand p328 | what the bytes show | region |
|---|---|---|---|
| https://github.com/Jellypod-Inc/school-skills | 🟢 **MIT** — `main/LICENSE`, 1,065 B, *Copyright (c) 2026 Jellypod* | **Seven Claude Code skills shipping, six declared "on the way"**, self-labelled **alpha preview**. Shipping: `lesson-plan` (standards-aligned), `socratic-tutor`, `circle-time` (SEL check-ins), `rubric` (markdown + CSV, **Bloom's-aligned**), `arts-crafts`, `lecture-to-study-guide`, `concept-map` (Mermaid / Graphviz / Markmap). Planned: `flashcards` (CSV + Anki `.apkg` + Quizlet TSV), `quiz-generator`, `worksheet`, `latex-paper`, `language-drill` (**CEFR-calibrated, 11 languages**), `coloring-page` | 🔴 **UNPLACED** — no country, district or institution named anywhere in the README. A vendor namespace is not a region |
| https://github.com/afri-bit/revibe | 🟢 **MIT** — `main/LICENSE`, 1,074 B, *Copyright (c) 2026 - present afri-bit* | **A programming mentor whose stated design constraint is that it refuses to write the code** — *"hands you questions instead of answers"*. Clone-and-go: the product is **markdown files that instruct an existing coding agent how to teach**, with slash commands and learner state persisted to `MEMORY.md` in plain markdown. CI runs markdown lint + link checks. Targets GitHub Copilot among others. Self-states what it is **not**: *"not a curriculum site with pre-built content"* | 🔴 **UNPLACED** — no country or institution named |

🔵 **`revibe` is worth a line beyond its row.** It is the clearest instance yet of this KB's trend 7 — *the skill, not the app, is the unit of educational AI* — taken to its limit: **no server, no account, no model of its own, and the entire pedagogical contract expressed as markdown that rides whatever agent the learner already pays for.** 🟡 **That also makes it unsellable as a product and very cheap as a deliverable component, which is the right way to read it.**

### 🟡 One new agent that is NOT permissive, recorded because it cuts against this file's own trend

**`HugeCatLab/ChatTutor` is AGPL-3.0, read first-hand** — `main/LICENSE`, **34,522 B**, *GNU Affero General Public License Version 3*. The search channel that surfaced it reported no licence at all, and a third-party roundup put it at ~1.2k ★ (**carried, unverifiable here**). `package.json` shows a **pnpm monorepo** (`@chat-tutor/{client,web,db}`, Vitest, Drizzle-style `db:push`/`db:generate`/`db:studio`). It ships `README.md` **and `README_CN.md`**.

🔴 **Two things to say precisely.** First, **trend 4 of `intel/trends.md` — permissive agents, copyleft platforms — now has a real counter-instance at the top of the attention distribution: a visual interactive *tutor*, not a platform, under the strongest copyleft licence there is.** If a client runs it as a hosted service, AGPL §13 reaches the users of that service. **It is a reference to read, not a component to embed in a proprietary deliverable.** Second, 🟡 **a bilingual `README_CN.md` is a *language* signal, not a *placement* signal.** Under this KB's own closed-vocabulary rule the honest entry is **APAC on a language signal alone, and labelled as such** — no institution, ministry or country is named in either README.

### Rejected this pass, recorded so no future pass spends a probe

| candidate | why it is not a row |
|---|---|
| `foradian/fedena` (school SIS) | 🔴 **No licence file on any of `main`/`master`/`develop` across the six-filename probe space.** A vendor comparison blog asserts Apache-2.0; **nothing in the repository supports that.** No grant, no rights, no row |
| `frappe/lms` | 🔴 **AGPL-3.0, not MIT** — `license.txt` read first-hand on all three branches, 33,893 B. **A comparison blog listed it as "MIT licence with self-hosted data ownership."** It is the same README-versus-LICENSE hazard `repos/foundations.md` logged four times inside one org at p322, now appearing in *secondary* sources. Platform row, so it is filed in `verticals/solutions.md` |


## Pass 327 · 2026-10-19 (thirteenth pass of this date) — ten adjudicated promotions, zero executed, and the backlog is the finding

🔴 **The pass's finding is an arithmetic fact about this KB, not about the sector: `evidence/p296-promotion-gap.2026-10-18-p296.tsv` adjudicated ten repositories for promotion — four of them `PROMOTE-to-agents-top` — and thirty passes later `grep` finds 0 of 10 in `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` or `compose/patterns.md`.** The verdict column was written. The rows were never cut.

🔵 **This settles a question p325 and p326 each answered differently, and both answers were wrong.** p325 found six FUN-MOOC repos that were "a promotion, not a discovery" and read it as a carry-forward lapse. p326 found a 6.1 ★k dataset invisible to topic sweeps and read it as a **query-shape** defect — agent-shaped queries cannot see a data layer. **Neither explanation survives this pass.** `anthropics/k12-teacher-skills` was found, licence-read from the sidebar, region-placed to North America, and explicitly marked `PROMOTE-to-agents-top` on 2026-10-18. No query had to be reshaped. No index had to be fixed. **The asset was in hand, graded, and addressed to this file — and the write never happened.** 🟢 **The constraint on this KB is execution, not discovery, and it is the only one of the three diagnoses that is measurable with one command.**

🟡 **So this pass does not sweep. It cuts the rows.** Every licence below was re-read first-hand on the `raw` channel this pass over the seven-filename probe space across three candidate branch names — not carried from p296 — because a verdict a day old is still a claim.

### The four agent-tier promotions from p296, licences re-read this pass

| Agent / skill set | Repo | Licence (re-read p327) | ★ | Region | What it is |
|---|---|---|---|---|---|
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | 🟢 **MIT** — `main/LICENSE`, 1,064 B, *MIT License* | **41.1k** (p296: 41,000) | **APAC** | *Open Multi-Agent Interactive Classroom* — Tsinghua (THU-MAIC). 6.4k forks, 733 commits. Ships `skills/`, `eval/`, `e2e/` and a `render-service`. **The largest permissive education agent in this KB by a wide margin** · **Use it for:** the multi-agent classroom shell — roles, turn-taking and an eval harness already wired |
| **k12-teacher-skills** | https://github.com/anthropics/k12-teacher-skills | 🟢 **Apache-2.0** — `LICENSE` read first-hand; `NOTICE` names *Copyright 2026 Anthropic, PBC* and *Copyright 2026 Learning Commons* "under a collaboration agreement" | **575** (p296: 572) | **North America** | Four skills behind *Claude for Teachers*: `k12-lesson-plan-creation`, `k12-lesson-differentiation`, `k12-lesson-prep`, `k12-check-for-understanding`. 105 forks, 4 commits. Ships `plugin/` + `evals/` + `CLA.md` + `CODEOWNERS` + `SECURITY.md` · **Use it for:** the teacher-workflow layer, installable as a plugin (`claude plugin marketplace add ./k12-teacher-skills`) |
| **Shiksha Copilot** | https://github.com/microsoft/Shiksha-Copilot | 🟢 **MIT** — `main/LICENSE`, 1,140 B | 9 (p296) | **APAC** | Microsoft Research India + **Sikshana Foundation**. 12 forks, 149 commits · **Use it for:** the India reference implementation — a named ministry-adjacent NGO deployment, which is what a public-sector bid asks for |
| **Rumi Platform** | https://github.com/Orenda-Project/rumi-platform | 🟢 **Apache-2.0** — `main/LICENSE`, 11,286 B, genuine Apache text | 18 (p296) | **APAC** | README names **Pakistan** and the **Taleemabad** national-curriculum library. 19 forks, **847 commits** — the commit count, not the star count, is the signal here · **Use it for:** a low-resource, national-curriculum-bound deployment pattern |
| **AI-Teaching-Agent** | https://github.com/littlecookie0722/AI-Teaching-Agent | 🟢 **MIT** — `main/LICENSE`, 1,068 B | 0 (p296) | 🔴 **UNPLACED** — no country or institution named anywhere in the repo | 30 commits, 0 forks. 🔵 **Carried as `PROMOTE-reference-only` exactly as p296 graded it: readable as a worked example, not citable in a bid** · **Use it for:** nothing client-facing |

### The Learning Commons agent + evaluation tier — measured since p119, never promoted

🟢 **Three repositories from one organisation, all permissive on the code, and the KB has licence-read two of them byte-for-byte already** (`compose/code/p119-carried-column-audit/evidence-f/`, `compose/code/p120-unread-grant-resolution/evidence/`). **None has ever appeared in this file.** The org page — one HTTP request against a repository this KB already held — lists all three.

| Agent / tool | Repo | Licence (read first-hand p327) | ★ | What it is |
|---|---|---|---|---|
| **Agent Skills** | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** — `LICENSE` 10,173 B; `NOTICE` 268 B naming **Anthropic, PBC** and **Learning Commons** | 40 | Four K-12 teacher skills (check for understanding · lesson differentiation · lesson plan creation · lesson prep), **grounded in the Knowledge Graph over MCP**. Installs with `npx skills add learning-commons-org/agent-skills` into any runtime supporting the open skills format. Ships its own `evals/` rubrics for **pedagogy, rigor, formatting and model scaffolding**, runnable as LLM-as-judge. 5 forks, 42 commits. 🔴 **No description and no topics** — the same invisibility signature p326 recorded on the Marble dataset |
| **Evaluators** | https://github.com/learning-commons-org/evaluators | 🟡 **Four-way split, re-read this pass at 1,615 B:** code **MIT** · prompts + settings **CC BY 4.0** · **Annotated CLEAR Corpus** and **Annotated PERSUADE 2.0** both **CC BY-NC-SA 4.0** | 86 | **19 evaluators in five families**, scoring LLM output "through the lens of learning science": **Text Complexity** (8 — grade-level appropriateness, background-knowledge demands, vocabulary complexity, sentence structure, meaning directness, purpose clarity, organizational structure, reference-knowledge demands), **Feedback** (7 — strength acknowledgment, revision actionability, student-response specificity, revision accuracy, revision manageability, **withholding answers**, tone appropriateness), **Graphics** (2, early access), **Academic Standards Alignment** (1, math), **Durable Skills** (1, critical thinking). Python + TypeScript SDKs: `pip install learning-commons-evaluators`, `npm install @learning-commons/evaluators`. 17 forks, **289 commits** |

🟢 **Why `evaluators` matters more than its 86 stars suggest.** p319 of this file concluded that the sector's reported quality metric — LLM-judged helpfulness — **is not a pedagogy signal**, and that a real evaluation layer had only just appeared. **This is that layer, it is MIT on the code, and it has been sitting on the trending channel of this KB since p119.** 🔴 **The commercial boundary is exact and it is not in the code: the expert-annotated corpora that validate the evaluators are CC BY-NC-SA 4.0.** You may ship the evaluators and their prompts in a paid product; you may **not** ship the annotated CLEAR or PERSUADE 2.0 corpora, and you may not use them to validate a commercial model release. **Re-annotate against client data, or validate in-house and keep the corpus out of the deliverable.**

### Two finds that are genuinely new, and one that is unusable

| Repo | Licence (read first-hand p327) | ★ | Verdict |
|---|---|---|---|
| https://github.com/devissaputra/curriculum_knowledge_graph | 🟢 **MIT** — `main/LICENSE`, 1,076 B, *Copyright (c) 2026 Devis Wawan Saputra* | **0** | 🟢 **The curriculum-graph *schema and validator*, which this KB has never held as a separate layer.** 8 entity types (Program · Course · Module · Concept · LearningOutcome · Competency · Assessment · Resource) and 7 relation types (`PART_OF` · `TEACHES` · `HAS_OUTCOME` · `ASSESSES` · `ALIGNS_WITH` · `PREREQUISITE_OF` · `SUPPORTS`), with **relation semantics constrained and invalid edges rejected** — `LearningOutcome ──TEACHES→ Course` is refused. Relations carry `confidence`, `source_type`, `evidence`, `reviewed_on`. Detects cycles, bottlenecks, disconnected entities and assessment-coverage gaps. 36 unit tests pass. 14 topics, 27 commits. 🟡 **Stated honestly by its author and restated here: all bundled data is SYNTHETIC, self-labelled "SYNTHETIC / RULE-BASED PROTOTYPE \| no educational validity claim", 0 stars, one maintainer.** 🔵 **Take the validator, not the data** |
| https://github.com/oseducation/knowledge-graph | 🔴 **NO LICENCE FILE** — all seven filenames 404 on `main`, `master` and `develop`; `README.md` resolves 200 on `main` and `master`, so the repo exists | n/m | 🔴 **Vitsi AI** — a third prerequisite-DAG artefact ("all the knowledge of humankind" as a DAG, nodes gated by tests, short-video discovery mode). **Unusable: no grant, so no rights.** Recorded so no future pass spends a probe on it |

🔵 **The rule this pass adds, and it is cheaper to act on than either of its predecessors.** p325 said a declared gap is a statement about the query. p326 said it is a statement about the filter. **p327: before any of that, it is a statement about the write.** A KB that discovers, grades and addresses an asset and then does not cut the row has a **100% discovery rate and a 0% delivery rate on that asset** — and the second number is the only one a client engagement can spend. **The audit is one command, and it should run before every sweep, not after:** re-grep every `PROMOTE-*` verdict in `evidence/` against the four shelf files.

## Pass 326 · 2026-10-19 (twelfth pass of this date) — the largest artefact in this sector is a data repo, and twelve passes of agent-shaped queries could not see it

🟢 **The pass's finding is a 6.1 ★k repository this KB has never held, and the reason it was missed
is a method defect, not a supply gap.** `withmarbleapp/os-taxonomy` — the **Marble Skill
Taxonomy** — is **1,591 micro-topics and 3,225 prerequisite edges across eight subjects, ages
4–15, linked to 3,261 standards from seven national curricula, under ODbL-1.0 + CC BY-SA 4.0.**
Every count in that sentence was **read out of the shipped JSON this pass**, not out of the README.
It has been public since **2026-07-08**, carries **998 forks**, and is **larger by stars than every
row in this file except `DeepTutor`.**

🔴 **Why eleven prior sweeps missed it, stated precisely, because the rule generalises.** The
repository has **no GitHub description, no topics and no detected language** — GitHub's own
sidebar renders *"No description, website, or topics provided"* and an empty Languages section.
It is a repository of JSON. **Every query this KB has run in this industry has been shaped like an
agent** — `agent`, `tutor`, `MCP`, `skill`, `assistant` — and **a pure data layer matches none of
them, at any star count.** 🔵 **p324 said a declared gap is a statement about the query; p325
narrowed it to the filter. This pass narrows it again and the new form is the sharpest of the
three: a gap declared by an agent-shaped query is blind to the data layer underneath the agents,
and the data layer is where this sector's durable assets are.** This file's own trend 12 has
argued for seven passes that curriculum data is the moat. **The largest piece of it on GitHub was
sitting outside every query this KB knows how to write.**

🟢 **The licence is the part that makes it a Globant asset, and it is unusual enough to state
carefully.** ODbL is share-alike, which reads like a problem and is not one here. **ODbL
distinguishes a *derivative database* from a *produced work*:** extend or modify the taxonomy and
your modified taxonomy must stay open; **use it inside a product, model or application and the
product stays yours.** The repository says so in its own README. 🔵 **So a commercial tutor built
on this graph does not open-source itself — it owes back only improvements to the graph.** That is
a materially different answer to a procurement question than the KB's existing curriculum rows:
`cn-math-taxonomy` is **CC BY-NC** and cannot enter a deliverable at all, and `bncc-dev` is CC BY
4.0 but covers **one country**. **This is the first multi-national curriculum graph in this KB that
a client can ship on.**

🔴 **One real constraint, and it is in `curriculum-standards.json`, not in the licence.** Marble
does not own the upstream frameworks and says so. **Four sources ship codes-only** — `ngss-k5`,
`ngss-ms`, `c3-social-studies`, `ib-pyp-pspe` — with the verbatim standard text withheld; **UK
National Curriculum ships in full under OGL v3** (commercial use, no share-alike); **Common Core
ships in full but stays under the purpose-limited CCSS Public License, not ODbL.** The
topic→standard *links* are intact for all of them, so *"this topic maps to standard X"* survives
everywhere; what you cannot redistribute is NGSS or IB prose. **NGSS is a WestEd trademark and
commercial use carries a sample-approval requirement.** Read `PROVENANCE.md` before any bid that
quotes standard text.

🟢 **And the rights engineering in that file is the best this KB has seen in the sector — it is
worth copying regardless of whether a client ever uses the data.** The publication export
**omits any passage matching eight or more consecutive words of a codes-only framework's stored
text**, case- and punctuation-insensitive, **marks each omission inline with the curriculum code
and logs it by JSON path** in `publicationNotes.omittedCurriculumText`. The same transformation is
applied to citation claims and activity source claims. **The repository then states, unprompted,
that this mechanical pass "is not comprehensive rights clearance"** and that shorter excerpts may
remain. 🔵 **A machine-checkable redistribution boundary, with its own audit log and its own
stated limit, is exactly the artefact an education buyer's counsel asks for and never gets.**

### Verified first-hand, against the shipped bytes

`data/manifest.json` publishes SHA-256 per file. **`topics.json` downloaded this pass hashes to
`5aa40906…b7e9d`, which is the manifest's value** — so the dataset is byte-verifiable end to end.
🔵 **No other curriculum artefact in this KB ships checksums.** Counts re-derived from the files
rather than the prose:

| measured | value | note |
|---|---|---|
| topics | **1,591** | `Science 547 · Mathematics 504 · English 286 · History 90 · PSD 88 · Life Skills 37 · Computing 21 · Learning to Learn 18` |
| prerequisite edges | **3,225** | **2,030 `hard` / 1,195 `soft`** |
| edges carrying a prose `reason` | **3,225 / 3,225 — 100%** | e.g. *"Must understand vibrations make sound before finding volume patterns"* |
| topics with an `assessmentPrompt` | **1,591 / 1,591 — 100%** | natural-language mastery check, `{{name}}` placeholder to substitute or strip |
| topics with `evidence` descriptors | **1,556 / 1,591** | observable can-do statements, typically three |
| topics with ≥ 1 standard link | **1,013 / 1,591**; **2,189 links** | `uk-nc-2013` 1,069 · `ccss-ela` 584 · `ccss-math` 323 · `ngss-k5` 85 · `ib-pyp-pspe` 70 · `ngss-ms` 58 |
| teaching-research records | **1,051**, 23.5 MB | **540 topics have none, and the file says which** |
| age span | **4 – 15** | |

🔴 **Two honest limits, both self-declared.** The teaching research is **agent-authored, its sources
were not re-verified for this release, and the activities are its own words *"research-informed
proposals, not empirically validated interventions."*** And the research layer covers **only
Science and Mathematics** — **English, History, Computing, Life Skills, PSD and Learning to Learn
have zero records**, which the coverage block states per subject rather than leaving to be
discovered. 🔵 **A dataset that enumerates its own 540 holes is behaving better than most of this
sector's metadata, and trend 11 should record a positive instance for once.**

🟢 **The row a North American or EMEA literacy-mandate conversation should open with.** The whole
**`Computing` subject is AI literacy — all 21 topics, one domain, `Artificial Intelligence`,
ages 5–11**: *Smart Versus Not-Smart Devices*, *Voice Assistants and How They Work*, *AI Mistakes
and Limitations*, *Recommendation Systems and Filter Bubbles*, *Bias in AI Systems*, *AI Data
Collection and Privacy*, *Deepfakes and AI-Generated Content*, *Designing Fair AI Rules*, *AI and
the Future of Work*, *AI and the Environment*. **Each carries an age band, an assessment prompt and
its place in the prerequisite graph.** 🔵 **p320 separated the "AI literacy mandate" from the "AI
guardrail mandate" and noted the literacy motion had thin permissive assets. It now has a
sequenced, commercially licensable, age-banded spine** — against **California AB 2876**, **Utah
H.B. 273**, **Illinois HB 316** (literacy instruction for grades 6–12, effective 2026-08-01) and
the EU AI Act **Article 4** staff-literacy duty. The age band stops at 11 and the mandates reach
higher; say so, and scope the extension.

### Added to the table

- **`tbh-23/Homestead` — MIT, 15 ★, 41 commits.** The taxonomy's **reference consumer**, and the
  reason this pass adds an agent row and not only a data row. A mastery-based platform for ages
  5–13 that **fetches the taxonomy from upstream at runtime and notifies the user when topics are
  added or removed** — a **90%+ mastery gate** before advancement, **mastery tests whose answers
  are independently re-solved to verify them**, Leitner spaced repetition, spaced retry of missed
  questions, and an AI coach grounded in the child's own progress. 🟢 **Its architecture is the
  finding: by never committing the dataset it keeps the ODbL database outside the MIT product, so
  the derivative-database/produced-work boundary is enforced by the build rather than by a
  promise.** That is pattern **P13**, new in `compose/patterns.md` this pass.

### Recorded below the listing bar

- **`simgue/harrington` — MIT (`LICENSE` read first-hand; the file is Homestead's, *Copyright (c)
  2026 Homestead*), 0 ★, 211 commits.** A family-specific fork of Homestead, **no chat**, lesson
  generation off by default behind a user-configured OpenAI-compatible endpoint with **Ollama as
  the documented example**, and **learner names replaced before prompts are built** — the same
  name-stripping boundary this KB praised in `JustinoLM/STI-matematicas`. **Recorded, not listed:
  it is one family's fork at zero stars.** It matters as evidence that the taxonomy has downstream
  consumers at all, which at 103 days old and 998 forks is otherwise unmeasured.

### The supply sweep, and what it says about this industry

**Four global queries and four regional queries were run.** Beyond the Marble layer, the
agent-shaped channel returned **`kvnloo/tutor-mcp`, `mizcausevic-dev/mcp-ai-tutor`,
`nirholas/ai-tutor-mcp`, `mohaneesh-03/mcp-tutor`, `GarethManning/education-agent-skills`,
`zijinz456/OpenTutor`, `rohitg00/ai-engineering-from-scratch`** — **every one of them already in
this KB.** 🔵 **Novelty on the agent channel this pass was 0%. Novelty on the data channel was
100%, first try.** p325 said discovery was no longer where the margin is; this pass refines that:
**discovery on the agent axis is exhausted; the data axis had never been swept.**

## Pass 325 · 2026-10-19 (eleventh pass of this date) — the sweep measured this KB's own coverage, and the nine-pass LTI gap stopped being an absence

**Twenty-five repositories were put through a three-axis supply sweep. Twenty were already held.**
Nine new slugs were added across this KB — **every licence read first-hand this pass** — and
**not one of them is above 14 ★**. 🔵 **That ratio is the pass's first finding and it is a
statement about this base, not about the sector:** a fresh broad sweep at this KB's depth now
returns **36% novelty and 0% above 14 ★**. The `intelligent-tutoring-system` axis census, the whole
**France Université Numérique** stack and every artefact the fresh-push window returned were
already on these shelves. **Discovery is no longer where the margin is in this industry; composition
is.** The rows are in `repos/foundations.md`, the sweep itself in `agents/trending.md`.

🟢 **The pass's main finding upgrades the longest-standing gap in this file from *absent* to
*diagnosed*, and it is the first positive evidence trend 6 has ever had.** Nine passes have
recorded *no LTI 1.3 AI agent*. This pass tested it on a **third instrument, GitHub code search,
new to this KB** — `lti_1p3 mcp server tutor language:python` → **0**;
`"pylti1p3" OR "ltijs" mcp agent tutor` → **6 hits, none an agent.** But the diagnosis came from
the supply side: **`openfun/django-lti-toolbox` — MIT, 14 ★, 34 commits, *"a Django application to
build LTI Tool Providers"*, no release, and last pushed `2024-11-14`, roughly twenty-three months
untouched.** The permissive LTI plumbing **exists, is published by a national public operator, and
is being left to rot** while the same operator's MCP-era peers ship weekly and its own analytics UI
(`openfun/warren`) still renders *inside an LTI iframe*. 🔵 **The gap is not missing libraries. It
is agent-side adoption of a working, permissive, unmaintained standard** — which is a different
sentence to put in front of a client, and a cheaper one to act on.

🔴 **The second finding is a method failure caught on this pass itself, and it refines p324's
declared-gap discount.** This pass searched `special education IEP AI assistant pushed:>2026-01-01
stars:>3` → **0 results**, then `IEP individualized education program generator LLM` → **0
results**, and was one step from declaring a special-education gap. **This KB already holds
`iblai/k-12-agents` — an MIT `special-education-agent` grounded in IDEA 2004, the thirteen
disability categories and §504 — recorded at p288 as the correction of exactly that claim.** The
search *terms* were fine. **`stars:>3` and `pushed:>2026-01-01` removed it.** 🔵 **Record the
sharper rule: p324 said a declared gap is a statement about the query. It is narrower than that —
a gap declared behind a star or recency filter is a statement about the filter.** The highest-stakes
tier in this sector is the one most likely to be published by an institution at two stars.

🔴 **And an instrument caveat that will only get worse: the code-search channel now returns this
KB's own files.** Two of the six hits for the LTI probe were
`gmilano/education-kb/archive/2026-10-19-p315-pre-rewrite/repos-foundations.md` and
`gmilano/education-kb/compose/code/p436-fork-hypothesis/homepage.2026-10-07.tsv`. **This base is now
part of the corpus it searches.** Every future novelty count on this channel must exclude
`gmilano/*` or it will score its own history as supply.

### Added to the table

- **`dymchenkko/claude-study-agent` — MIT, 2 ★, created 2026-10-10.** The **fresh-push window's only
  substantial artefact**: a university study agent that takes *the learner's own* slides, PDFs and
  **lecture recordings** (Whisper), OCRs them, indexes them for semantic search, then quizzes with
  spaced repetition, tracks mistakes and builds mock exams. Local-first, no external vector store.
  It is `universal-examprep-skill`'s shape with the **recording** leg added — the first artefact here
  to treat the lecture itself as ingestible learner-owned corpus.

### Added to the evaluation table

- **`Kyyota-Wang/cloverailab` — 🔴 NO LICENCE, 0 ★.** GRE Analytical Writing reviewer and writer
  agents: **LLM-as-judge against the published ETS rubric with officially scored anchors, no
  fine-tuning, QWK 0.825**, harness and results committed. 🔵 **It is the second artefact in this
  tier to publish a real agreement figure and the second that cannot be used** — `EduGuardBench`
  (p323) was the first. **The eval tier's measured edge keeps arriving without a grant.**

### Recorded below the listing bar

- **`wildcat430524/Steps2Great-skill` — MIT, 2 ★, zh/en.** A Socratic **mastery-learning** Agent
  Skill that will not advance until a **three-dimension assessment is all-green** — the gate from
  `leap-framework`'s State Guard expressed as a prompt contract instead of a server. APAC-authored,
  consistent with trend 7.
- **`010Ankushsharma/AdaptaLearn` — 🔴 NO LICENCE, 0 ★.** DKVMN knowledge tracing + PPO, with a
  claim of training on **131M+ interactions**. Recorded, **not** recommended: the claim is
  unverifiable from the repository and there is no grant.


## Pass 324 · 2026-10-19 (tenth pass of this date) — the seven-pass integrity gap was a query artefact, and it is closed

**One row added here, one to the evaluation table, ten to `repos/foundations.md` (now forty-eight),
all six of p322's named-unread `openeduhub` repositories measured. Fourteen repositories measured
first-hand.**

🟢 **The pass's finding: `intel/trends.md` trend 9's premise — *"there is still no credible open
source AI-detection or academic-integrity project"*, declared for seven consecutive passes — is
false, and the query was what was wrong.** The sweeps behind it searched *AI detection* and
*AI-detection agent*. Searching the GitHub topic **`plagiarism-detection`** instead returns twelve
repositories pushed since 2026-01-01 above ten stars, and three are substantial: **`sunilgentyala/
aegis-integrity`** (MIT, 17 ★, **an academic-integrity MCP server with seven tools**),
**`NoplagLabs/noplag-engine`** (Apache-2.0, 86 ★, winnowing over PostgreSQL) and **`jplag/JPlag`**
(GPL-3.0, **2.0k ★, 5,708 commits**, twenty-odd languages, Java API or CLI). 🔵 **Trend 9's
*conclusion* survives and is strengthened** — `aegis-integrity`'s README is the most careful
statement of the human-in-the-loop posture this KB has read from a tool that could have
overclaimed, and it publishes no accuracy figure for itself. **The premise was false; the
recommendation was right.** Full detail and the two cautions in `agents/trending.md`; the engines in
`repos/foundations.md`; the wiring in `compose/patterns.md` **P11**.

🔴 **Fourth consecutive instance of this KB's most reliable method finding.** p318 → tool name;
p322 → topic sweep; p323 → changed query, two curriculum artefacts; **p324 → changed query, a
seven-pass gap overturned.** A declared gap is a statement about the query, not about the world.

🔴 **The other finding is a licence contradiction running the opposite way to every one before it.**
`ZhijieXiong/pyedmine` (82 ★, 220 commits, the broadest educational-data-mining library this KB has
measured) ships **the MIT text in `LICENSE` — under `Copyright (c) 2023 Stanford Future Data
Systems`, an unrelated holder — while its README says *"All data and code in this project may be
used only for academic purposes."*** Every previous instance in this KB was a README claiming a
grant the repository did not carry; **this is the documented grant being narrower than the licensed
one, which is the direction dependency scanners do not catch.** Treat it as academic-use-only.
`repos/foundations.md` has the full row.

🟢 **Instrument change, stated because every number in this pass depends on it: the GitHub REST
search API is reachable in this session** via the MCP `search_repositories` tool, where earlier
cycles recorded it blocked. Star, fork, push-date, archived and topic values here are structured
API values, not readings off a rendered page — **and the supply tail p323 measured was reproduced
exactly on this second instrument** (six repositories, ceiling 41 ★). 🔴 `get_file_contents` is
refused — credentials are scoped to one repository — and **`curl` to `github.com` returns `403`
through this session's proxy**, so file-level verification ran through `raw.githubusercontent.com`
and the rendered page. 🔴 **And a probe caveat that nearly produced right verdicts for wrong
reasons: the `openeduhub` ITS tier writes `README.org`, not `README.md`, so a Markdown-shaped 404
probe 404s on every repository in the org.** Licence verdicts below were taken over **seven
candidate filenames** and corroborated against the rendered sidebar. Both characterised in
`repos/trending.md`.

### Added to the table

- **`sunilgentyala/aegis-integrity` — MIT, 17 ★, 5 forks, 68 commits, changelog at v3.3.2.** The
  first integrity artefact in this file, and the **second MCP-exposed agent** in it — which is
  further evidence for trend 6: an integrity reviewer built in 2026 ships **seven MCP tools and no
  LTI surface at all.**

### Added to the evaluation table

- **`yjo2lee/knowsim` — MIT, 4 ★.** arXiv 2608.17150. It is **the simulated learner, not the
  tutor**: a knowledge-state-aware user simulator for measuring whether an assistant's confidence
  tracks what the learner actually knows. The only calibration-focused artefact in this KB.

### The standing LTI gap — eighth pass, and now the first gap here to survive a changed instrument

Three changed queries on the new instrument: `topic:lti topic:ai` → **2 results**, neither an agent
(a profile README, and a third-party API profile of the **commercial** Packback "Originality");
`lti 1.3 mcp server education stars:>0` → **0**; `topic:lti lti-1-3 OR lti1p3 OR lti-advantage ai
agent` → **0**. 🔵 **Every other gap this KB declared and then re-tested with a changed query has
fallen. This one has not** — which is the first positive evidence that it is a property of the
sector rather than of the search.

## Pass 323 · 2026-10-19 (ninth pass of this date) — two new rows, one unlicensed benchmark, and a trend headline retracted

**Two rows added here, one to the evaluation table, three to `repos/foundations.md`, four
repositories recorded below the listing bar, two named gaps from p322 executed and still empty, and
one open question from p319 closed with a negative answer.** Nine repositories read first-hand.

**The pass's finding is not in this file.** `haolpku/K12-KGraph` — 420 ★, 67 forks, **NeurIPS 2026
Evaluations & Datasets Track**, China's PEP K-12 curriculum as an evidence-linked knowledge graph
with 12 expert annotators at Fleiss' κ = 0.84 — **makes `intel/trends.md` trend 12's headline
("exactly one country has built it") wrong.** Two countries have. **Exactly one licensed the data
for commercial use:** K12-KGraph splits *"Code (this repository): MIT"* from *"Dataset (graph,
benchmark, training data): CC BY-NC-SA 4.0."* Full read in `repos/foundations.md`.

**The licence shape is new and it pairs with p322's.** p322 found licences dividing **by
architectural layer** inside one organisation — permissive shells, GPL analysers, unlicensed
inference core. This pass found licences dividing **by artefact type** inside one repository —
permissive code, NonCommercial data. **Both are the same sentence: permissive at the edges,
restricted at the thing that actually took the work.** In Germany it was the inference core; in
China it is the curriculum. A studio that reads only the sidebar badge gets both wrong.

### The method lesson, and this is its third consecutive instance

p318 declared `AITutor-EvalKit` nonexistent; p322 found it by searching the paper's tool name and
wrote down the lesson. **p322 then swept the `ncert` and `cbse` topics — 180 repositories — and
declared "no verified curriculum dataset at all."** This pass changed the query to *curriculum
knowledge graph / prerequisite* and found two artefacts the topic sweep could not see, one of them
the largest in this KB. **A topic sweep is a query, not a census, and a declared gap must be
re-tested with a changed query — which is now the third time this file has had to say so.**

### What is new in the table

- **`zhangl1001/civil-ai` (MIT, 41 ★, 100 commits)** — **the highest-starred education agent pushed
  since 2026-10-01**, and a *foundation* rather than an app by its own careful statement. Local-first
  on iOS and Web, storage behind repository ports, an agent runtime with checkpoints, leases,
  cancellation and recovery, and an evidence-based capability model with mastery projection. **It
  volunteers its own weakness** — domain portability unvalidated, both bundled packages exam-style.
  APAC-authored.
- **`ibenian/algebench` (MIT, 8 ★, 519 commits)** — an **interruptible** 3D maths narrator: stop the
  scene, ask why, watch the visualisation answer. Gemini-only BYOK keeps it out of the dependency
  tier. **519 commits at 8 stars is the second measured instance of this file's p320 lesson that a
  star count is not a volume measure.**

### The eval tier gained its first in-proceedings artefact, and it has no licence

**`YL1N/EduGuardBench` — 🔴 NO LICENCE, 5 ★, 2 commits — arXiv 2511.06890, AAAI proceedings
(article 40399).** Role-playing Fidelity Score for teacher-simulation fidelity; persona-based
adversarial prompts for academic misconduct scored by Attack Success Rate and a three-tier refusal
assessment; 14 models. **Two results worth a bid slide:** the safest models convert harmful requests
into teachable moments via *Educational Refusals*, a capacity **strongly negatively correlated with
ASR** — safety and pedagogy pulling the same direction for once — and a **scaling paradox** in which
mid-sized models are the most vulnerable, so "bigger is safer" is false in this domain. **It ships
its two datasets as `.xlsx`, its scripts, a notebook and an appendix PDF, with empty `Results/`
folders — and no LICENSE file.**

**The correction this forces on p322, stated narrowly.** One pass ago this file retired the
five-pass gap *"no credible open source way to evaluate pedagogical quality"* and called the eval
layer **"a real and usable tier."** That stands — MathTutorBench, AITutor-EvalKit and the two
pre-registered audits are all still there and all still usable. **But the tier's newest entrant, and
the only one published in conference proceedings rather than on arXiv alone, cannot be used.** The
tier is real; its peer-reviewed edge is not yet licensed. **And of the four 2026 education
benchmarks this pass touched — EduGuardBench, EduClaw-Bench, EduFair-Bench, ELBench — one has code
without a licence and three have no code at all.** That is the actual state of educational-AI
evaluation in late 2026: the papers are arriving much faster than the artefacts.

### Both p322-named gaps, executed

- **EduClaw-Bench (arXiv 2608.03206)** — 55 scenarios (11 learner personalities × 5 study schedules)
  over **30 virtual days** each, scored on learning gain, responsiveness and helpfulness plus Gagné
  and Rosenshine curriculum-design axes. Unggi Lee +5, 4 Aug 2026. **Still only the anonymous review
  link** `anonymous.4open.science/r/educlaw-bench-anonymous-ED3F`. The author name was searched
  directly this pass as well; no named repository, no licence.
- **EduFair-Bench (arXiv 2609.12949)** — EPFL (Zhao, Radmehr, Fawzi, Nazaretsky, Käser), 11 Sep
  2026; nine demographic levels over gender, immigration background, first language and SES. **No
  repository, no licence.** Its two findings are usable without the code: **capability and fairness
  are largely orthogonal**, and **language and immigration cues produce larger gaps than gender and
  SES** — which is not where fairness review effort usually goes.
- **ELBench (arXiv 2608.09548)**, new to this KB, no code: four modules over nine models, and
  **the education-specialised models lead neither education module.** Authors state the data is
  synthetic and the benchmark text-only. Snippet-and-abstract sourced, not read first-hand.

### Recorded below the listing bar — permissive, real, too thin to list

Consistent with the p322 rejection of `CristianHeyde/language-teaching-skills` on weight alone:

- **`fcescob/understand` (MIT, 5 ★, 6 commits)** — **the most explicit mastery gate in this KB.** A
  stage passes only **cold, unprompted**: explain it, give an example *and a near miss*, name a
  misconception, transfer it to a new context — and **retention counts only on a later-day pass**,
  on a **1 / 3 / 7 / 21 / 60-day ladder**, with per-answer confidence 1–5 and hints before answers.
  Installs to Claude Code, oh-my-pi, Codex. Documents its own portability defect: **claude.ai
  uploads and the Skills API reject it over its frontmatter fields.** Read the gate, not the repo.
- **`fanfanfanfanfan626/mastery-tutor` (MIT, 3 ★, 19 commits, v0.4.1)** — `mastery-coach` plus
  `mastery-tool-creator`, guided HTML lessons, one local classroom per thread, state in `.mastery/`,
  no account and no hosted database; records **how much help was needed** and can mark earlier
  mastery **fragile**. Names no scheduling algorithm. **Says of itself "research-informed, not
  outcome-proven" and tests software and teaching contracts rather than learning outcomes** — the
  honest version of the claim every vendor here makes.
- **`grey8-io/learn-ai-with-grey8` (10 ★)** and **`CGSeb/lessonfolk` (3 ★)** — courses about AI with
  a tutor attached. Curriculum content, not agent dependencies.

### The APAC skill tier has a personality-rights problem, and this KB has not raised it before

**`tong666-bit/liu-xiaoyan-skill` (MIT, 18 ★, 6 commits)** teaches CET-4/6 and postgraduate-entrance
English *in the teaching style of a named, living educator* (刘晓艳); its sibling
**`tong666-bit/song-hao-math` (4 ★)** does the same for 宋浩 across calculus, linear algebra,
probability and complex analysis. **The disclaiming is explicit and unprompted** — *"非本人、非官方
出品"* (not by the person, not an official product), About reads *"刘晓艳风格，非官方"*, and the README
states the class-style lines *"不冒充老师原话"*, they do not pass themselves off as the teacher's
actual words.

**The point for a studio: the MIT licence covers the code and says nothing about the persona.** The
product value here is a named individual's pedagogical identity, and right-of-publicity exposure
travels with whoever ships it. **Read these for the pedagogy; never carry the persona framing into a
client deliverable.** Trend 7 has treated skills as a packaging story — this is the first evidence
that the packaging can carry a legal payload. No equivalent exists in the Western skill tier yet.

### The new-supply tail, measured

GitHub repositories matching *education / AI / tutor / agent* **pushed since 2026-10-01**, sorted by
stars: **the first page holds ten results and the top one has 41 stars.** Four of ten are
Chinese-language exam-prep skills, three are courses about AI, three are local-first mastery tutors
at 3–8 stars. **Nothing with real weight entered this category in three weeks, and what did enter is
skill-shaped and disproportionately APAC-authored.** Both reinforce trend 7; neither supports a
claim that this tier is consolidating.

## Pass 322 · 2026-10-19 (eighth pass of this date) — the `openeduhub` org, enumerated in full, and the finding is licence-by-layer

**Three rows added here, one to the evaluation table, twelve to `repos/foundations.md`, one measured
404.** Pass 321 found the `openeduhub` organisation, read four of its repositories and wrote down the
names of six it had not read, explicitly *"so p322 does not re-discover them"*, closing with
**"57 of the 67 were not listed on the first page and remain unenumerated."** Pass 322 enumerated all
sixty-seven — by paging the org listing under two different sort orders, because one sort order hides
what the other shows — and read **sixteen repositories first-hand**, every one of the AI-era ones.

**The finding is not a repository, it is a shape.** Germany's publicly funded OER portal has shipped a
twelve-service AI metadata pipeline: extraction, human review, deduplication, readability scoring,
accessibility and licence lookup, Bayesian metadata prediction, discipline classification, bulk prompt
running, factual-accuracy judging and a unified gateway over the lot. **And its licences divide by
architectural layer, not by repository:**

| Layer | Repos | Commits | Licence |
|---|---|---|---|
| Thin shells — UI, REST wrapper, browser plugin, path editor | `metadata-agent-canvas`, `metadata-browser-plugin-fuerAPI`, `lernpfadeditor`, `tutor-chatbot`, `llm-judge`, `wlo-quellenliste`, `duplicate-detection` | 60, 11, 6, 10, 1, 6, 25 | **Apache-2.0** (or claimed — see the README hazard) |
| Analysers and classifiers | `metalookup`, `text-statistics`, `discipline-classification` | 623, 94, 73 | 🟡 **GPL-3.0** |
| **The inference core** | `python-kidra`, `its-jointprobability`, `text-extraction`, `z-api-runner`, `its-qna`, `oeh-search-etl` | 137, 200, 77, 37, 4, 1,397 | 🔴 **none at all** |

**1,852 commits of ML and data plumbing carry no grant whatsoever, and they are precisely the part a
studio cannot write in a sprint.** Pass 321 observed that "the unlicensed repository is the one with
the most commits" and read it as one bad apple. It is not one repository — **it is the entire
inference core, and the permissive surface contains none of the org's machine learning.** The
practical rule for an engagement is in `repos/foundations.md`: take the shells and the API client,
reimplement or negotiate the brains, and keep the GPL-3.0 analysers behind a process boundary.

**The README hazard, now at four instances in one organisation.** Four repositories state a licence
in their README that the repository does not carry:

| Repo | README says | Repository actually carries | Verified how |
|---|---|---|---|
| `duplicate-detection` | "MIT License" | **Apache-2.0** | `LICENSE` read first-hand — it is the Apache 2.0, January 2004 text |
| `wlo-quellenliste` | "Lizenz: MIT" | **Apache-2.0** (sidebar + `LICENSE`) | sidebar and file listing |
| `metadata-agent-api` | "Lizenz: MIT" | 🔴 **nothing** — no `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING` in the root | root file listing enumerated first-hand |
| `metadata-agent-canvas` | "Apache License 2.0", "Copyright 2025 Jan Schachtschabel" | 🔴 **no licence file in the root listing**; sidebar shows no licence | root file listing enumerated first-hand |

The pattern is a copied README template, and it cuts both ways: twice it understates the grant, twice
it asserts a grant the repository does not make. **The rule this KB now applies: the `LICENSE` file
governs, and a README licence claim with no file behind it is not a grant.** That is the opposite of
the assumption a reader makes when a README says MIT.

**One measured 404.** `python-kidra`'s README lists seven bundled services; six have public
repositories in the org and **`openeduhub/wlo-topic-assistant` returns 404.** `wlo-classification`
does not exist under that name either — it **redirects to `openeduhub/discipline-classification`**,
a GPL-3.0 fork of `yovisto/wlo-classification`. Recorded rather than left silent: the gateway
advertises a capability whose source is not public under this org.

**Method, re-tested this pass rather than inherited, and it reproduces exactly.** `github.com` is
reachable with the fetch tool; non-GitHub origins are not —
`www.digitaleducationcouncil.com` failed at DNS (`getaddrinfo ENOTFOUND`) when attempted directly
this pass. No scanning probe was attempted, because passes 319–321 recorded that `curl -sI` returns
403 at the session proxy and that two probe attempts were refused by the sandbox classifier.
**Every repository and licence claim in this pass is first-hand off github.com. Every regional claim
in `intel/` remains snippet-sourced and is labelled there.**

**The prescribed search battery returned nothing this KB did not already hold — third pass running.**
All four global searches and all four regional searches were run. The global battery returned
general-purpose agent roundups with no education focus, one vendor LMS comparison, and market
forecasts spanning USD 6.4bn–10.6bn for the same year. The regional battery returned the Digital
Education Council LATAM survey, the IESALC 200-institution survey, the Carnegie Mellon/Gates USD 55m
courseware investment, OpenAI's eight-partner country programme, the TCS–Pearson alliance and the
50/19 feedback gap — **every one already in `intel/market.md`, most with a precision the snippets
lacked.** Two numbers were checked individually against the KB and were also already held. The
verdict and what it implies for how a pass should spend its budget are in `intel/trends.md`.

**A recount, because the number in the p321 text was stale.** This file's main table holds
**twenty-seven rows before this pass, thirty after** — p321's prose said twenty-six, which was the
count before its own addition. `repos/foundations.md` holds twenty-three before this pass,
thirty-five after.


## Pass 321 · 2026-10-19 (seventh pass of this date) — the named-gap sweep, executed

**One row added here, one to the evaluation table, two to `repos/foundations.md`, and six measured negatives recorded in that file's sweep table.** Pass 319 closed its topic-sweep section with an explicit to-do: *"Untested and worth a pass: Arabic, Hindi, Japanese, Korean, French and Indonesian topic tags, and the `wirlernenonline` organisation, whose GitHub org page could not be read this pass."* **Pass 321 executed that list in full.** Six of the seven items are negatives, and they are written down in `repos/foundations.md` rather than left as silence. The seventh is the pass's find.

**The find is an organisation, not a repository.** `wirlernenonline` is **404 — the org does not exist under that name.** The real account is **`openeduhub`**, and it holds **67 public repositories** of OER infrastructure for WirLernenOnline.de, built on edu-sharing. Four were read first-hand this pass: an Apache-2.0 tutor, an Apache-2.0 LLM-as-judge prompt bench, a **CC0-1.0 SKOS competency vocabulary with 938 commits**, and a 1,397-commit ETL **with no licence file at all**. The vocabulary repository corrects a claim this KB has carried since p319 — see `repos/foundations.md`.

**Method, re-tested this pass rather than inherited, and it reproduces.** `github.com` is reachable with the fetch tool and **non-GitHub origins are not**: `www.multistate.us` failed at DNS (`getaddrinfo ENOTFOUND`) when attempted directly. A `curl -sI` probe and a proxy-status probe were both **refused by the sandbox classifier as "Exfil Scouting"** and were **not worked around** — so this pass measured reachability by fetching, not by scanning. **Every repository claim below and in `repos/foundations.md` is first-hand off github.com; every regional claim is snippet-sourced and labelled as such in `intel/market.md`.**

**The prescribed global search battery returned nothing this KB did not already hold, at lower precision than the KB holds it.** The four regional searches returned the EU AI Act Annex III deferral, `H.R. 8747`, the 134-bills/31-states count, Canada's *AI for All*, the NYC moratorium, Korea's 2026-01-22 commencement, India's Class 3 mandate and Brazil's Bill 2338 — **all already in `intel/` with OJ numbers, dates and tracker caveats the snippets lacked.** That is the second pass in a row to reach that verdict, and it is why this pass spent its budget on the GitHub channel instead.

**Pass 320 · 2026-10-19 (sixth pass of this date). No rows added, and that is the finding.**
Five new candidates were read first-hand off GitHub this pass; **all five were rejected** — four on
weight or licence, one because it is not an agent. They are recorded in the rejection section so
pass 321 does not re-find them. **Three existing rows were re-verified** and one moved
(`DeepTutor` 41.7k → 41.8k ★). The count stands at twenty-six.

**The method constraint was re-tested this pass rather than inherited, and it reproduces exactly.**
`curl -sI https://github.com/...` returns **403 at the session proxy**; `www.future-ed.org`,
`www.lw.com` and `www.iesalc.unesco.org` were each attempted directly with the fetch tool this pass
and all three failed at DNS (`getaddrinfo ENOTFOUND`). **github.com remains the only reachable
origin.** Every repository claim below is first-hand; everything in `intel/market.md` is
snippet-sourced and labelled there.

**The one material addition this pass is in `repos/foundations.md`, not here:**
`adamzammit/LTIPlugin` (**GPL-3.0**, 14 ★, 97 commits) is the first artefact this KB has found at
the grade-passback seam that carries **an actual OSI-approved licence** rather than no licence at
all. It is not an AI tool and probably not LTI 1.3 — read the caveat with it — but it narrows the
"everything at this seam is unlicensed" claim this file has made for four passes.

**Pass 319 · 2026-10-19.** Twenty-six rows, twenty-six real repos. No header rows, no placeholders,
no example data.

Verification method, re-confirmed and stated more precisely this pass. `curl -sI` to github.com
returns **403 at this session's proxy**; the session's fetch tool reaches **github.com and nothing
else** — `arxiv.org`, `unesco.org`, `education.ec.europa.eu`, `koreaherald.com`, `k12dive.com` and
`iadb.org` are all refused at connect time (`connect_rejected`) by the egress policy. So every row
below was read off its GitHub page first-hand, and **every non-GitHub fact anywhere in this KB this
pass rests on search snippets, not a primary read.** The **Checked** column says which pass took
the repository reading.

**Pass 319 adds eight rows and closes the gap this KB has declared for five passes: the
evaluation layer.** Four permissively licensed artefacts for measuring whether a tutor *teaches*
now exist, and their convergent finding is that **LLM-judged "helpfulness", the metric the sector
reports, is unsound** — see the eval section below. That forces a correction to pass 318's own
reading of `lumen`.

**Pass 319 also escalates pass 318's star finding.** Pass 318 found a README asking AI agents to
star a repo. This pass found the same pressure *productised*: `karanb192/algo-sensei` (MIT, 293 ★,
**9 commits**) ships `scripts/star_invitation.py`, a once-per-machine gate, with a unit test and a
dedicated CI workflow. Detail below. With pass 317's finding that stars run too *low* on
institutional infrastructure, the ★ column is a rough size signal and nothing more. **Rank on
commit count, release cadence and licence.**

## The table

| Agent | Repo | Licence | ★ / activity | Checked | What it does | Use it for |
|---|---|---|---|---|---|---|
| **ari** | https://github.com/nichochar/ari | 🟢 **MIT** (`main/LICENSE`, **1,073 B**, read first-hand p343 — *Copyright (c) 2026 ARI contributors*) | **11 commits · 1 author · 2026-10-18 → 2026-10-19** (p343) · ★ **158** | **p343** | **Handwriting-in-the-loop tutoring.** A camera over a sheet of paper lets the model see work done **by hand**; it builds a curriculum and exercises from a conversation, then grades and adapts from the handwritten attempt. Personalisation is files, not a database: `TUTOR.md` (teaching style), `USER.md` (learner context), `memories/` (saved reflections). Node 24+, local, single-user; ffmpeg; camera bridge **macOS-only**, browser camera and photo upload work anywhere | 🟡 **Design reference only, and the data path is the reason.** The only row on these shelves that closes the loop on **pen and paper**, so read it for the interaction model. 🔴 Do not depend on it: two days old, one author, and the LLM path is a local **Codex login tied to a ChatGPT account** — the README states submitted work and learning context are sent to OpenAI, which is a disclosed cross-border transfer before any code is written. Placed 🟡 **North America** (`-0700(10)` in October, offset-only, no corporate domain) |
| **LTIkit** | https://github.com/Liberate-Labs/ltikit-sdk | 🟢 **MIT** (`main/LICENSE`, **1,063 B**, read first-hand p330 — *Copyright (c) 2026 alasim*) | **38 commits · 1 author · last 2026-07-10** (p330) · ★ n/v | **p330** | **LTI 1.3 Advantage toolkit for JS/TS, runtime- and storage-agnostic.** `packages/core/src/{ags,nrps,deep-linking}.ts`, 🟢 **each with its own `.test.ts`** (16 test files); framework packages `next` + `hono`; four storage adapters (`memory`, `prisma`, `redis`, `supabase`). 1.0-rc adds **Dynamic Registration** and **cookieless launches (Platform Storage)**. README: live-verified against **Canvas** and **MoodleCloud** | 🟢 **The only maintained permissive LTI 1.3 Advantage library outside PHP — take it when the integration must be LTI and the stack is JS/TS.** 🔴 **Fork and pin, do not depend:** every commit is one author's, the last three are an **ownership handover** (2026-07-10), and **seven dependabot branches run to 2026-10-07 unmerged.** 🔴 **UNPLACED** — no country signal |
| **jupyterquest** | https://github.com/Gchism94/jupyterquest | 🟢 **MIT** (`main/LICENSE`, 1,070 B, read first-hand p330 — *Copyright (c) 2024 Greg T. Chism*) | **249 commits · 3 authors · last 2026-05-07** (p330) · ★ n/v | **p330** | **`.ipynb` autograder** — the LLM-era member of the `nbgrader` / `otter-grader` cluster. Ships CI (`python-tests.yml`), **Codecov** coverage, a **Zenodo DOI** (`10.5281/zenodo.10784348`) and a PyPI package. Supersedes the same author's `Gchism94/ai-tutor`, which says so in its own README | Notebook-based course autograding where the deliverable must be citable — the DOI is what a university research office asks for. 🟡 **Five months quiet.** 🟢 **North America — institutionally attributed first-hand: `gchism@arizona.edu`, 124 of 249 commits (University of Arizona)** |
| **FreeLingo** | https://github.com/artcc/freelingo | 🔴 **AGPL-3.0** (`main/LICENSE`, **34,514 B**, read first-hand p330) | 🟢 **1,168 commits · 7 authors · last 2026-10-16** (p330) · ★ ~167 (third-party, carried) | **p330** | **Self-hosted AI language-learning platform.** LLM-assessed **CEFR** placement, generated study plan over a **CEFR A1–C2** curriculum in units, grammar/vocabulary/reading/writing lessons, AI-generated listening exercises, voice practice. **Ollama, OpenAI, Anthropic or DeepSeek**; Next.js 16, Python 3.14; v1.10.40 | 🔴 **Read it, do not embed it — and the licence is deliberate, not incidental:** the same team runs a paid hosted tier, and **AGPL §13 is the mechanism that protects it.** 🟢 **The largest *live* AGPL education artefact in this KB** (against `ChatTutor`'s 193 commits and nine months of silence) — read the CEFR ladder and the multi-provider speech path. **EMEA** 🟡 *(inferred from a Spanish personal name on 1,064 of 1,168 commits; no institution or country declared)* |
| **ai-tutor** (World Bank) | https://github.com/eai6/ai-tutor | 🟢 **MIT** (`main/LICENSE` **and** `master/LICENSE` read first-hand p328, 1,090 B — *Copyright (c) 2026 World Bank Group and contributors*) | **787 commits · 4 authors · last 2026-08-20** (p329) · ★ n/v | **p328** | **Production-shaped curriculum tutor, Django 6.0.2, seven apps.** 5E phase tags on every `LessonStep`; Socratic with a 3-level hint ladder; auto skill-graph + **prerequisite mastery gating**; exit tickets (35-MCQ bank, 10 sampled, 8/10 to pass); curriculum PDF/DOCX → lesson steps; multi-tenant; Claude/GPT/Gemini/Azure/**local Ollama**. `apps/safety/`: `ConsentRecord` (incl. **parental**, `withdrawn_at`), `SafetyAuditLog` (pseudonymised `user_hash`, consent events, severity), `export_user_data` / `delete_user_data` | 🟢 **The reference build for a ministry or district tutor — and the only permissive row in this KB that ships the consent/audit layer P4 and P9 require.** EMEA (Seychelles). 🔴 Affiliation self-declared; personal namespace |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | 🟢 **MIT** (`main/LICENSE`, 1,064 B, re-read p327) | **733 commits · 127 authors · last 2026-10-19** (p329) · ★ 41.1k (carried p327) | p327 → **shelf p328** | *Open Multi-Agent Interactive Classroom* — **Tsinghua (THU-MAIC)**. Ships `skills/`, `eval/`, `e2e/` and a `render-service` | 🟢 **The multi-agent classroom shell: roles, turn-taking and an eval harness already wired. The largest permissive education agent in this KB.** APAC |
| **k12-teacher-skills** | https://github.com/anthropics/k12-teacher-skills | 🟢 **Apache-2.0** (`LICENSE` 10,173 B; `NOTICE` names *Anthropic, PBC* and *Learning Commons* under a collaboration agreement) | **4 commits · 3 authors · last 2026-10-13** (p329 — small by design, tended) · ★ 575 (carried p327) | p327 → **shelf p328** | The four skills behind *Claude for Teachers*: `k12-lesson-plan-creation`, `k12-lesson-differentiation`, `k12-lesson-prep`, `k12-check-for-understanding`. Ships `plugin/`, `evals/`, `CLA.md`, `CODEOWNERS`, `SECURITY.md` | The teacher-workflow layer, installable as a plugin. North America |
| **agent-skills** (Learning Commons) | https://github.com/learning-commons-org/agent-skills | 🟢 **Apache-2.0** (`LICENSE` 10,173 B; `NOTICE` 268 B naming **Anthropic, PBC** + **Learning Commons**) | **42 commits · 6 authors · last 2026-10-06** (p329) · ★ 40 (carried p327) | p327 → **shelf p328** | The same four K-12 teacher skills **grounded in the Knowledge Graph over MCP**; installs via `npx skills add learning-commons-org/agent-skills`. Ships `evals/` rubrics for **pedagogy, rigor, formatting and model scaffolding**, runnable as LLM-as-judge | 🟢 **The standards-grounded variant — take this one when the client needs the skill tied to a curriculum spine rather than to a prompt.** North America |
| **Shiksha Copilot** | https://github.com/microsoft/Shiksha-Copilot | 🟢 **MIT** (`main/LICENSE`, 1,140 B, re-read p327) | **149 commits · 6 authors · last 2026-09-15** (p329) · ★ 9 (carried p327) | p327 → **shelf p328** | **Microsoft Research India + Sikshana Foundation** | The India reference implementation — a named ministry-adjacent NGO deployment, which is what a public-sector bid asks for. APAC |
| **Rumi Platform** | https://github.com/Orenda-Project/rumi-platform | 🟢 **Apache-2.0** (`main/LICENSE`, 11,286 B, re-read p327) | **847 commits · 11 authors · last 2026-10-05** (p329 — the carried figure, now exact) · ★ 18 (carried p327) | p327 → **shelf p328** | README names **Pakistan** and the **Taleemabad** national-curriculum library; 847 commits on 18 stars — the commit count is the signal | A low-resource, national-curriculum-bound deployment pattern. APAC |
| **school-skills** | https://github.com/Jellypod-Inc/school-skills | 🟢 **MIT** (`main/LICENSE`, 1,065 B, read first-hand p328 — *Copyright (c) 2026 Jellypod*) | 🔴 **4 commits, ALL on 2026-04-14 · 1 author · silent 6 months** (p329) · ★ n/v | **p328** | **Seven Claude Code classroom skills shipping, six declared** (self-labelled **alpha**): `lesson-plan`, `socratic-tutor`, `circle-time`, `rubric` (Bloom's-aligned, md + CSV), `arts-crafts`, `lecture-to-study-guide`, `concept-map` (Mermaid/Graphviz/Markmap). Planned incl. `language-drill` (**CEFR, 11 languages**), Anki `.apkg` export | The breadth-first teacher skill bundle when the ask is classroom admin, not tutoring. 🟢 **North America** — placed p330 from the commit record: `pierson@jellypod.ai`, all four commits at `-0700` |
| **revibe** | https://github.com/afri-bit/revibe | 🟢 **MIT** (`main/LICENSE`, 1,074 B, read first-hand p328) | 🔴 **4 commits over 2 days · 2 authors · last 2026-05-02** (p329) · ★ n/v | **p328** | **A programming mentor that refuses to write the code.** No server, no account: markdown files that teach an existing coding agent to teach, slash commands, learner state in `MEMORY.md`. Targets Copilot among others | Trend 7 at its limit — the pedagogical contract as portable markdown. Cheap as a component, unsellable as a product. 🟢 **EMEA** — placed p330 from the commit record: all four commits at `+0200` (CEST). 🟡 Places the keyboard, not the person — the author's name is Indonesian |
| **ChatTutor** | https://github.com/HugeCatLab/ChatTutor | 🔴 **AGPL-3.0** (`main/LICENSE`, **34,522 B**, read first-hand p328 — the search channel reported no licence) | 🔴 **193 commits · 11 authors · last 2026-01-09 (9 months stale)** (p329) · ★ ~1.2k (third-party, carried) | **p328** | Visual, interactive tutor. pnpm monorepo (`@chat-tutor/{client,web,db}`), Vitest. `README.md` + `README_CN.md` | 🔴 **Read it, do not embed it: AGPL §13 reaches the users of a hosted service.** 🟡 **APAC on a language signal only** — no country or institution named |
| Homestead | https://github.com/tbh-23/Homestead | MIT (`LICENSE` read first-hand — *MIT License, Copyright (c) 2026 Homestead*, 1,573 bytes) | 15 | p326 | **Mastery-based learning platform for ages 5–13 built directly on the Marble Skill Taxonomy** — fetches `withmarbleapp/os-taxonomy` at runtime rather than vendoring it, and flags topics added or removed upstream. 90%+ mastery gate before advancement; mastery-test answers independently re-solved to verify them; Leitner spaced repetition; spaced retry of missed questions; parent-approved difficulty increases; "Homestead Helper" AI coach grounded in the child's own progress. Static front end (HTML/CSS/vanilla ES modules, Tailwind via CDN) on a Puter.js backend, PWA; 41 commits, 2 forks. Per-parent data isolation; the Commune feature shares only the day's approved topics. | **The reference implementation of the ODbL boundary** — copy its runtime-fetch architecture whenever an ODbL or CC BY-SA dataset sits under a product you intend to keep proprietary. Also the clearest worked mastery ladder in this file. See P13. |
| claude-study-agent | https://github.com/dymchenkko/claude-study-agent | MIT (`LICENSE` read first-hand — *MIT License, Copyright (c) 2026 dymchenkko*) | 2 | p325 | **A local-first study agent over the learner's own course material, including the lectures.** Ingests slides, PDFs and **lecture recordings** — Whisper for the audio, OCR for scanned pages — then builds a semantic index and runs a study loop over it: spaced-repetition quizzing, mistake tracking and **generated mock exams**. Built on Claude Code; topics declare `local-first`, `rag`, `anki-alternative` and `notebooklm-alternative`. Created 2026-10-10, pushed 2026-10-19, 0 forks | **The lecture-recording leg no other artefact in this file has.** Where `universal-examprep-skill` assumes the learner owns slides and past papers, this one assumes they also own the *recording* of the class — the single richest unexploited corpus in formal education, and the one most likely to carry a consent question. Read it for the ingest chain; treat the recording as personal data from the first line of the proposal |
| aegis-integrity | https://github.com/sunilgentyala/aegis-integrity | MIT (sidebar + `LICENSE`, Copyright (c) 2026 Sunil Gentyala) | 17 | p324 | **Local-first academic-integrity reviewer exposed as an MCP server** — *"Free, local-first academic integrity checker and MCP server"*. **Seven MCP tools**: `aegis_analyze_paper`, `aegis_check_citations`, `aegis_check_guidelines`, `aegis_compare_papers`, `aegis_index_add`, `aegis_index_summary`, `aegis_status`. Five signal families: **citation-hallucination resolution against Crossref** with verdicts `VALID`/`MISMATCH`/`HALLUCINATED`/`UNRESOLVABLE`/`NO_DOI`; AI-text via **GPT-2 perplexity, burstiness, a stylometric ensemble and lexical-tell density** plus a semantic-coherence analyser; plagiarism via **n-gram MinHash + SBERT/FAISS against a corpus you supply**; ghostwriting via **Burrows' Delta**; and an experimental keyless watermark heuristic that *"never affects the overall integrity risk score"*. Self-plagiarism, essay-mill batch analysis, citation-network analysis and **venue-guideline checks for IEEE, ACM and Elsevier**. `pip install "aegis-integrity[ml]"` + `aegis ui` for a local web app; Claude Code plugin; Claude Desktop `.mcpb`; `docker compose`; GHCR image; `install.bat` on Windows. Crossref/OpenAlex/DataCite are called with **reference metadata only, never the document**, and there is an explicit `offline=true`. 68 commits, 5 forks, changelog at v3.3.2 | **The artefact this KB declared absent for seven passes — and the reason to use it is what it refuses to claim.** It publishes **no accuracy figure for itself**, cites third-party studies instead, and states *"Results are a supporting signal for human review, not a determination of misconduct"* and, on ESL bias, *"Do not treat AEGIS as having solved ESL false positives; keep a human in the loop."* 🔴 **Read its own tension before quoting it:** the marketing section says per-language calibration *"reduce[s] this bias"* while the ESL section says the non-English multipliers *"rarely fire"*, and the changelog records an earlier ESL multiplier that was **inverted** and fixed. Deploy it as the **citation and process-evidence** layer of an integrity review (`compose/patterns.md` **P11**); do not deploy its AI-text score as a finding |
| civil-ai | https://github.com/zhangl1001/civil-ai | MIT (sidebar + LICENSE) | 41 | p323 | **A reusable, local-first foundation for adaptive education agents on iOS and Web** — its own words: *"Civil AI is a reusable, local-first foundation for building adaptive education Agents on iOS and Web"*, with the Chinese civil-service-exam package as *"the current end-to-end reference adapter"* that *"does not define the scope of the foundation."* Vue 3 + TypeScript, Capacitor iOS shell; **SQLite on iOS and IndexedDB on Web behind repository ports**, with migrations; Anthropic and OpenAI-compatible provider gateway with providers as replaceable adapters; agent runtime with tools, skills, **checkpoints, leases, cancellation and recovery**; an *"evidence-based capability model"* with mastery projection and review priority, and spaced review in the reference app (no algorithm named). English README with a Chinese positioning section; 100 commits, 7 forks; docs reference a v1.2.0 upgrade guide, Releases empty | **The highest-starred education agent pushed since 2026-10-01, and the only artefact in this KB that separates an education-agent runtime from its exam adapter on purpose.** Read it for the ports-and-adapters shape when a client wants one tutor engine across several subjects — and read its own caveat first: **it states that domain portability is unvalidated because both bundled packages are exam-style, question-driven study** |
| algebench | https://github.com/ibenian/algebench | MIT (sidebar) | 8 | p323 | **Interactive 3D mathematics visualiser with an interruptible AI narrator**: the learner stops a running lesson scene to ask what/how/why and the narrator answers in real time while the visualisation responds, with step-by-step proofs and a semantic graph kept in sync with the 3D view. Scenes built from adjustable parameters and live simulations; Three.js frontend; **lessons stored as JSON files**; runs via a `./algebench` script or Docker image on localhost. **Google Gemini only, bring-your-own-key.** 519 commits, 1 fork | **The interruption is the pedagogy** — this is the only artefact here where the learner controls the explanation mid-stream rather than after it, and lessons-as-JSON makes the scene format readable. **Not a dependency: Gemini-only means the model is not pluggable as shipped**, the same disqualifier this file applied to GradeMate. **519 commits at 8 stars — see the p320 lesson on star counts** |
| lernpfadeditor | https://github.com/openeduhub/lernpfadeditor | **Apache-2.0** (sidebar + LICENSE) | 0 | p322 | **AI-assisted editor for differentiated learning paths** (*"Ein KI-gestützter Editor zur Erstellung differenzierter Lernpfade"*), built for WirLernenOnline.de: generates a path template from a natural-language description, performs automatic internal differentiation (*Binnendifferenzierung*) into tiered tasks, and ranks WLO resources for assignment to each step. **GPT-4o** for template generation and resource ranking, **Whisper** for dictation, **up to 20 parallel AI calls**; React + TypeScript + Vite, TailwindCSS, Zustand; needs Node 18+ and an OpenAI key. 6 commits | **Differentiation is the teacher-facing feature clients ask for by name and this KB had no permissive implementation of it.** 6 commits is a prototype — read the differentiation prompt design, not the code |
| metadata-agent-canvas | https://github.com/openeduhub/metadata-agent-canvas | 🟡 **README claims Apache-2.0 — no licence file in the root listing** | 0 | p322 | **Human-in-the-loop metadata canvas**: an Angular web component that fills schema fields from a text in parallel via LLM, shows each extracted value with a **confidence badge** for inline editing, validates required fields against controlled vocabularies, normalises values, enriches addresses with geocoordinates (Photon/OpenStreetMap through a server-side proxy) and ends on an explicit *Bestätigen* confirm step before JSON download or submission to the WLO repository. Standalone, bookmarklet and browser-plugin modes. Angular 19, Angular Material, RxJS, **LangChain (`@langchain/openai`)**, Netlify Functions / Vercel / Docker+nginx. Providers: OpenAI direct, B-API→OpenAI, **B-API→AcademicCloud (DeepSeek-R1)**. 60 commits — the most-developed AI artefact in the org | **The review-UI pattern this KB has been describing in the abstract since p317, implemented.** Confidence badge → inline edit → explicit confirm is the shape a human-oversight requirement actually takes in a product. 🔴 **Do not depend on it:** the README states Apache-2.0 and the repository root carries no licence file, so the grant is unverified — read it for the interaction design |
| metadata-browser-plugin-fuerAPI | https://github.com/openeduhub/metadata-browser-plugin-fuerAPI | **Apache-2.0** (sidebar + LICENSE) | 0 | p322 | **Manifest V3 extension for Chrome and Edge (v2.1.0)** that indexes educational resources from the page the teacher is on: extracts metadata *per KI*, lets the user review it, and uploads to the WLO repository **either signed in or as a guest**; plus a "shopping cart" that collects materials into a printable lesson plan, and a watch list and upload history. Calls a deployed backend at `metadata-agent-api.vercel.app` — `/generate` for extraction, `/upload` for guest submission. 11 commits, 1 fork | **The browser is the capture surface for teacher-contributed OER, and this is a working instance of it.** Also the clearest evidence in this KB that the metadata-agent line is deployed, not just committed: the plugin points at a live Vercel host |
| tutor-chatbot | https://github.com/openeduhub/tutor-chatbot | Apache-2.0 | 0 | p321 | Learning-companion chatbot for **WirLernenOnline.de**, Germany's publicly funded OER portal: blends a curated QA dataset with LLM answers, queries the WLO / edu-sharing API (`https://www.wirlernenonline.de/api/v1`) for matching learning materials and attaches them to the answer as direct links, filters by subject, content type and source, and reports **Bloom-taxonomy learning analytics**; extracts learning metadata from the learner's question. Provider is **OpenAI or GWDG** (German academic compute). 10 commits, React/Vite, Apache-2.0 stated in both the LICENSE and the README | **The only Apache-2.0 public-sector tutor in this KB, and the only one with a sovereign-inference path** — read it for the architecture, not as a dependency: 10 commits is a prototype |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 🟢 **2,935 commits · 273 authors · last 2026-10-19** (p329) · ★ 41.8k (p320) | p320 | Lifelong personalised tutoring agent; v1.6.15 (2026-10-19), 2,935 commits, 5.3k forks, paper arXiv 2604.26962. README now describes it as an "agent-native learning workspace" with an inspectable three-layer memory, Co-Writer, Book and Partners | The strongest permissive starting point for a tutor product |
| Study-Mate | https://github.com/Miaotofu01/Study-Mate | MIT | 1.1k | p319 | Maths/CS study partner shipped as a skill bundle: plans a learning route, explains concepts, drives project work; five roles (material collection, illustration, course design, teaching, exercise evaluation); progress stored as files in a local workspace with a shared cross-subject memory of skill level and effective explanation styles; 723 commits; packaged for DeepSeek Harness, Google Antigravity and Codex/ChatGPT Work; docs zh + en | The largest permissive APAC skill bundle — read it for the files-as-learner-state pattern |
| instructional_agents | https://github.com/DaRL-GenAI/instructional_agents | MIT | 488 | p319 | ADDIE-model multi-agent instructional design: generates syllabus, slides, scripts and assessments; catalog mode for structured input, copilot mode for per-phase feedback; LaTeX/PDF, HTML and PPTX output; web UI, CLI (`run.py`) and REST API; 95 commits, 106 forks; arXiv 2508.19611, **accepted to EACL 2026 Main**; a public fork of `Hyan-Yao/instructional_agents` | Course-production work — the peer-reviewed answer to "reduce faculty workload" |
| lineage-skill | https://github.com/JuneYaooo/lineage-skill | Apache-2.0 | 459 | p319 | Distils course videos, audio, books, PDFs and transcripts into a source-backed teaching skill: micro-lessons with ASCII/SVG diagrams, two formative questions per topic with feedback, practice/error/review tracking, source references kept on key claims; 50 commits; docs zh + en | **The first permissively licensed skill bundle at scale** — the licence-clean alternative to `education-agent-skills` |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | MIT | 309 | p319 | Exam-prep tutor as an Agent Skill: teaches chapter by chapter with page citations, crops figures out of the learner's own slides, quizzes from their past papers, tracks mistakes, builds a cheat sheet; state local, **no external vector DB**; 183 commits; installs across 40+ agent hosts via `npx skills add`; docs en + zh | Engagements where the learner owns the corpus and nothing may leave the machine |
| claudemy | https://github.com/assafkip/claudemy | MIT | 317 | p319 | Skill that researches a topic and builds ~12 two-minute audio lessons with cited sources, each with a summary card, one practice task and a playbook rule; 20 commits | Audio-first micro-course generation; read for the lesson-shape template |
| algo-sensei | https://github.com/karanb192/algo-sensei | MIT | 293 | p319 | LeetCode/DSA mentor skill for Claude Code and claude.ai with tutor, hint, review, interview and pattern-mapper modes, hint-first by design; 9 commits, 63 forks; solution write-ups in Python, Java, C++, JavaScript, Go | The hint-ladder design — **and the star-invitation finding below** |
| smolagents | https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Minimal library for agents that think in code; 1,059 commits | The agent runtime under a tutor when you want small and auditable |
| FSRS4Anki | https://github.com/open-spaced-repetition/fsrs4anki | MIT | 4.1k | p317 | Free Spaced Repetition Scheduler as an Anki scheduler; 482 commits | Retention scheduling — the review-timing half of a tutor |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | p317 | Assigning, collecting and autograding Jupyter notebooks; 3,477 commits | Grading automation in any notebook-based curriculum |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 878 | p316 | 165 evidence-grounded teaching skills (pedagogy, assessment, curriculum) for Claude/Codex/Hermes; 149 commits | Prompt and pedagogy assets — **not** a code dependency, see caveat |
| iblai/os | https://github.com/iblai/os | MIT | 821 | p316 | Agent platform (Next.js → web/desktop/mobile) with chat, voice, SSO; 3,518 commits | A front end only — the backend is **not** in the repo, see caveat |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **MIT/AGPL-3.0 dual (skills); AGPL-3.0 (app)** | 573 | p318 | 33 agent skills turning Claude/ChatGPT/Gemini into structured tutors on spaced-repetition and active-recall principles, plus a Next.js 16 app (React Flow, Supabase, OpenRouter); K-12 through career and social skills; bilingual EN/zh; 36 commits | APAC-authored evidence for trend 7 — **and the star-solicitation caveat below** |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 62 | p319 | Local-first teacher assistant: imports PDF/DOCX/PPTX/TXT/MD, drafts teacher DOCX, student DOCX, PPTX slides, multi-week units and assessments for human review; local dashboard and API, MCP server, Telegram bot, Drive integration; Anthropic/OpenAI/Gemini/Ollama/OpenRouter; v9.18.2026.1 (Beta), 778 commits; MacxLabs | **The teacher-facing-only build** (trend 3, pattern P7) — and it states plainly that local storage does not mean local processing |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT | 520 | p316 | MCP server exposing the Anki flashcard app to any LLM client; 258 commits | Wiring a real spaced-repetition store to an agent without writing a scheduler |
| Educhain | https://github.com/satvik314/educhain | MIT | 387 | p317 | Python package generating MCQs, lesson plans and flashcards with LLMs; 578 commits | Content-generation pipelines behind an authoring tool |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** | 932 | p317 | AI tutor built on Theory-of-Mind reasoning: reasons about the learner's needs and rewrites its own prompts to suit them; v0.8.0, 356 commits | Study the ToM prompting approach — **copyleft, see caveat** |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 289 | p316 | Socratic adaptive tutor shipped as both portable agent skills and a self-hostable React/FastAPI app; 76 commits | The clearest worked example of the skill-plus-app delivery shape |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 268 | p317 | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase), UC Berkeley CAHLR; 1,045 commits. README: "For LMS integration, a middleware backend is required by Learning Tools Interoperability (LTI)" | Mastery modelling / hint sequencing where you must explain the pedagogy |
| otter-grader | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | 161 | p315 | Python and R autograding with containerised execution | Autograding where submissions must run sandboxed |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 145 | p316 | Local-first block-based adaptive workspace: upload material → notes, quizzes, flashcards, tutor; 10+ LLM providers, 194 commits | An offline/on-prem tutor shell when data cannot leave the building |
| gen-mentor | https://github.com/GeminiLight/gen-mentor | CC0-1.0 | 135 | p316 | LLM multi-agent framework for goal-oriented learning in an ITS; WWW '25 oral, arXiv 2501.15749; 91 commits | A peer-reviewed multi-agent ITS architecture you can cite in a bid |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 111 | p315 | Educational collaborative AI tutoring platform; arXiv 2602.07176 (Feb 2026) | An academically documented tutor platform you can fork and cite |
| lumen | https://github.com/ahmedEid1/lumen | **GPL-3.0** (LICENSE file; README badge wrongly says MIT) | 89 | p318 | Multi-agent orchestrator builds a private course from a one-sentence goal in ~50s, then a course-scoped RAG tutor teaches it; v2.0.0 2026-06-06, 828 commits; FastAPI + Next.js 15 + pgvector; BYOK envelope-encrypted | **Read for its published evals, not for its licence** — see below |
| LTLTutor | https://github.com/brownplt/LTLTutor | **GPL-3.0** | 12 | p319 | Misconception-driven adaptive tutor for Linear Temporal Logic: models the specific wrong beliefs learners hold and targets practice at them; Brown PLT; 320 commits; CAV 2025 **Distinguished Paper** (Prasad, Greenman, Nelson, Krishnamurthi) | **Read, do not link.** The clearest worked example of misconception modelling as the decision layer |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 52 | p316 | MCP server that turns any LLM into an ITS: skill graph, BKT, FSRS, prerequisite rules, narrative memory; SQLite local / PostgreSQL hosted; 467 commits | The deterministic-pedagogy engine — still the architectural find of p317 |

## The evaluation layer exists now — and its first finding is that the sector's metric is unsound

Five passes of this KB have declared: *no credible open source way to measure whether a tutor
teaches.* **That gap is closed.** Four artefacts were read first-hand this pass, three of them MIT,
and they do not agree with the way this sector reports quality.

| Artefact | Repo | Licence | ★ | Commits | What it is |
|---|---|---|---|---|---|
| cloverailab | https://github.com/Kyyota-Wang/cloverailab | 🔴 **NO LICENCE** (7 candidate filenames probed across 5 branch names on the `raw` channel, none returns 200) | 0 | — | **The tier's second measured agreement figure, and the second one with no grant.** GRE **Analytical Writing** reviewer *and* writer agents: an **LLM-as-judge scored against the published ETS rubric using officially scored anchor essays, with no fine-tuning**, reporting **QWK 0.825 against those official anchors** — with the evaluation harness and the results committed to the repository rather than asserted in a README. TypeScript on Cloudflare Workers. 🔵 **Why it matters out of proportion to its zero stars:** every uplift claim a client will be shown in this sector is a judged score, and p323 established that judged helpfulness is the wrong instrument. **This is the opposite case — a judged score against a published rubric and real anchors, which is the one form of LLM-as-judge that can be defended** — and QWK against official anchors is the figure a testing organisation will actually recognise. 🔴 **Read the method and rebuild it; the repository carries no licence, so neither its harness nor its results can enter a deliverable** |
| knowsim | https://github.com/yjo2lee/knowsim | MIT (`LICENSE` read first-hand — *MIT License, Copyright (c) 2026 Yoonjoo Lee*) | 4 | — | **The simulated learner, not the tutor.** *"Knowledge-state-aware user simulator for evaluating information calibration in LLM assistants"* — arXiv 2608.17150. It supplies the piece every evaluation in this tier has to improvise: a student whose knowledge state is **controlled and known**, so that an assistant's confidence can be scored against what the learner actually knows rather than against an answer key. **Calibration, not pedagogy and not accuracy** — the only artefact in this KB aimed at it, and the complement to MathTutorBench (pedagogy) and `llm-judge` (content accuracy). Small and single-author; read it for the simulator contract |
| EduGuardBench | https://github.com/YL1N/EduGuardBench | 🔴 **NO LICENCE** (no sidebar licence entry, no LICENSE file) | 5 | 2 | **The eval tier's first artefact published in conference proceedings — and the only one that cannot be used.** arXiv 2511.06890 (10 Nov 2025), **AAAI proceedings article 40399**; Yilin Jiang +7. Dual-component: a **Role-playing Fidelity Score (RFS)** for professional teacher-simulation fidelity, and **persona-based adversarial prompts** targeting general harms and specifically **academic misconduct**, scored by **Attack Success Rate (ASR)** and a **three-tier refusal-quality** assessment, across **14 models**. Ships `SATAs.xlsx` (Select-All-That-Apply teaching-harm items), `adversarial_prompts.xlsx`, Python scripts for both experiments, a shared utilities folder, an analysis/figures notebook and a full appendix PDF (scenarios, ethics taxonomies, dataset design, annotation guidelines) — **with empty `Results/` folders.** Two results worth quoting: an **"Educational Transformation Effect"** in which the safest models convert harmful requests into teachable moments as ideal **Educational Refusals**, a capacity **strongly negatively correlated with ASR**; and a **scaling paradox** in which mid-sized models are the most vulnerable, so safety is **not monotonic in model size**. **Read the paper and the appendix; the repository has no grant, so its data and scripts cannot enter a deliverable** |
| llm-judge | https://github.com/openeduhub/llm-judge | **Apache-2.0** (sidebar + README + LICENSE) | 0 | 1 | **A factual-accuracy judge for educational content, published by a public OER operator** — *"KI-gestütztes Bewertungstool für Sachrichtigkeit von Bildungsinhalten"*. Scores the description field of a learning object (`cclom:general_description`) against **six criteria declared in `config.yaml`**: factual correctness, clarity and comprehensibility, objectivity, relevance, structure and length, language and style. Input is JSON with `node.properties` and a `sys:node-uuid`; single or batch; `gpt-4o-mini` default or `gpt-4o` via `MODEL_ID`, with an optional `BASE_URL` to point at a different endpoint; 30 s default API timeout. Outputs CSV scores, JSON with improvement suggestions, and interactive charts — **1 commit** — this is a published intent, not a tool. And note what it judges: **content accuracy, not pedagogy.** It is the complement to the four pedagogical evaluators above, not a substitute, and the README states neither the scoring scale, the prompts nor the aggregation — so its numbers are not comparable to anything |
| ki-prompt-benchmark | https://github.com/openeduhub/ki-prompt-benchmark | Apache-2.0 | 0 | 3 | **An LLM-as-judge prompt bench published by a public OER operator.** Compares the metadata-generation prompts live in edu-sharing's `mds.xml` v10.0 against an optimised set: a judge model scores both on **five criteria, 1–10**, names a winner and gives a rationale, while the harness measures generation time and token usage across providers (OpenAI direct, B-API→OpenAI, **AcademicCloud**). Test material can be a sample, a WLO repository item or any URL via a text-extraction service. Judge feedback is accumulated across runs to regenerate an improved prompt per field, and prompt sets export back to `mds.xml`. Next.js 15 / React 19 / TS 5 |
| MathTutorBench | https://github.com/eth-lre/mathtutorbench | **CC BY 4.0 badge / CC BY-SA 4.0 footer — contradictory, see below** | 45 | 25 | Peer-reviewed benchmark for open-ended pedagogical capability: 3 teacher skills, 7 tasks, 9 configs — problem solving, socratic questioning, solution correctness, mistake location, mistake correction, plus four pedagogy win-rate tasks. **Pedagogy is scored by a ~1.5B scaffolding reward model against ground-truth teacher utterances, not by an LLM judge.** EMNLP 2025 main, oral (arXiv 2502.18940); Macina, Daheim, Hakimi, Kapur, Gurevych, Sachan; reward-model data on Hugging Face (`dmacjam/pedagogical-rewardmodel-data`) |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT | 3 | 8 | Evaluation framework for LLMs as maths tutors: a LoRA-finetuned automated evaluator, an open LLM-as-judge path (`prometheus-eval/prometheus-7b-v2.0`) and a GPT-5 judge path; backend plus a frontend demo; v1.0.0, 1 Dec 2025; ships a 10-example sample only — you bring the dataset. MBZUAI EduNLP Lab (Naeem, Maurya, Petukhova, Kochmar), arXiv 2512.03688 |
| conv-vs-ped-tutor | https://github.com/bydeng01/conv-vs-ped-tutor | MIT | 3 | 12 | **Pre-registered audit** of whether an LLM helpfulness judge rewards answer leakage that reduces a student's later independent work. Two tutors wrap the same frozen base model and differ only in policy structure — ConvTutor is a single LangGraph node, PedTutor a multi-node state machine — against a no-tutoring cold baseline, in algebra. Per-turn/per-session/per-replicate tables, metric summaries and inference verdicts committed; ~100 MB of transcripts released separately under SHA-256 manifests. arXiv 2607.28128 |
| ability-levels-audit | https://github.com/bydeng01/ability-levels-audit | MIT | 4 | 8 | Pre-registered LLM-judge audit with frozen data: 990 accepted judge ratings, a complete 55 × 3 × 2 grid checked by hash before analysis runs, registered diagnostics separated from labelled post-hoc analysis, and the pre-registration, amendments and decisions log in `protocol/`. Headline result is a methodological one: **difference-in-differences on a censored rating scale can manufacture an effect that is not there.** arXiv 2608.27309, NewInML @ NeurIPS 2026 |

**What they jointly establish, and it is uncomfortable for everyone selling in this sector:**

1. **LLM-judged "helpfulness" is not a pedagogy signal.** The leakage audit exists precisely because
   a judge can reward a tutor for handing over the answer. A separate study found at AIME-Con 2026
   concludes that human oversight remains necessary for nuanced instructional assessment
   *(snippet-sourced, not read first-hand)*.
2. **A bounded rating scale plus a before/after comparison can produce an effect from nothing.**
   That is the shape of almost every tutoring-uplift claim a client will be shown.
3. **The one peer-reviewed benchmark here deliberately avoids an LLM judge** and scores pedagogy
   with a trained reward model against real teacher utterances instead.

**The correction this forces on pass 318.** Pass 318 called `ahmedEid1/lumen` "the most credible
artefact of the pass" for publishing authoring 3.85/5, tutor 2.33/5 and ingest 0.83/5 about itself.
Publishing unflattering numbers is still to its credit — **but those are judged scores, and this
pass's evidence is that judged scores of helpfulness are the wrong instrument.** Read lumen for the
*habit* of publishing an eval, not for the values. Where a client needs a number, run
MathTutorBench and report what it measures.

**Two licence warnings on this tier, both material:**

- **MathTutorBench's licence is self-contradictory**: the README badge says CC BY 4.0, the footer
  says CC BY-SA 4.0. **That is the fifth licence inconsistency this KB has verified**, and the
  first in the eval layer. ShareAlike on a benchmark attaches to derivative benchmark *data* — the
  annotated items a Globant engagement would add. Resolve it with the authors before building a
  client-specific extension on it.
- **All four are content or research licences, not product dependencies.** CC on the benchmark data,
  MIT on audit code that ships with its own frozen data. Use them as measurement instruments inside
  an engagement; do not vendor them into a deliverable.

**What to do with this tomorrow:** add an eval stage to every tutor engagement, score with
MathTutorBench's task shapes, borrow the audits' discipline — pre-register the comparison, freeze
the data, hash it, keep a decisions log — and **never report an LLM-judged helpfulness score as
evidence of learning.** See pattern P1's new "prove it teaches" stage.

## The LTI gap, pass 319: re-checked, unchanged — and now a third unlicensed artefact

`blamb/lti-tutor` was re-read first-hand this pass. **Its licence is still "To be decided", it still
has 0 stars, 0 forks and 39 commits.** Nothing has moved since pass 317 — two passes of no change.

**And the pattern behind it repeated again this pass.** `JaimeArriagadaRosas/Plugin-Feedback-Canvas`
(0 ★, **160 commits**, Spanish-language docs) is a full-stack **LTI 1.3 plugin for Canvas** in which
an instructor generates academic feedback from templates, context variables and a choice of AI
provider, and **must review and approve it before it reaches the student** — the human-in-the-loop
control that Oklahoma's 2026 statute and every US district AI policy now demand, built and working.
React/Vite over Node/Express, Postgres and Redis, Gotenberg for document conversion, Vitest/
Playwright/Testcontainers for test, and a README that honestly states it is in pre-production
validation. **It has no LICENSE file.** That is the third artefact at exactly this seam that cannot
be used — after `luffycodes/Tutorbot-Spock` and `blamb/lti-tutor` — and the first written in
Spanish, which makes it the closest thing in this KB to a LATAM-authored LMS-integrated AI tool.
**Ask the author for a licence; it costs an email.** Until then, read the shape and rebuild it.

This matters because it is the single highest-value watch item in this KB: it implements LTI 1.3
against Moodle with dynamic registration, deep linking and completion passback through Assignment
& Grade Services on `ltijs` — precisely the artefact this KB has declared missing for four passes —
and **one commit adding a LICENSE file would make it the most strategically valuable repo here.**
Until then default copyright applies and Globant cannot use it, fork it, or copy its approach into
a client deliverable.

**Re-check it every pass. It is a one-line check with a large payoff.**

**Pass 320: re-checked, and the gap stands — but it is now a narrower claim.**
`adamzammit/LTIPlugin` (**GPL-3.0**, 14 ★, 97 commits, `master`) makes **LimeSurvey act as an LTI
provider**: a learner launches a survey or assessment from the LMS and the plugin **returns a
score back to the gradebook** as a value between 0.0 and 1.0 derived from a LimeSurvey expression,
with **setup instructions in the README for Canvas, Moodle, openEdX and Blackboard** and support
for LimeSurvey 3.x–7.x. **Two caveats decide how this may be used.** First, it is **not an AI
tool** — it is assessment delivery with outcome passback. Second, **the page never names an LTI
version**, and it bundles `LTI-Tool-Provider-Library-PHP`, which points at the **legacy LTI 1.x
Basic Outcomes path rather than 1.3 Advantage AGS** — so do not scope it as an Advantage
implementation without reading the submodule. **What it does change:** for four passes this file
has said that every artefact at the grade-passback seam is unlicensed. That is no longer true.
**GPL-3.0 is a real licence**, it sits on the same copyleft side of this KB's architectural line as
`tutor-gpt`, `lumen` and `LTLTutor`, and the plugin is a readable, four-LMS reference for how
outcome passback is actually wired. **The unfilled gap is specifically an AI tutor speaking LTI
1.3 Advantage under a permissive licence. Nothing found this pass changes that.**

**What did change on the library side:** `repos/foundations.md` now records **`tsugiproject/tsugi`
(Apache-2.0, 376 ★, 266 forks, 4,011 commits, Apereo Incubating)** — an LTI library and
multi-tenant tool-hosting environment an order of magnitude larger than `pylti1.3`, from the
author of the LTI specification. **Its GitHub page does not state which LTI versions it
implements**, so the Advantage-surface question is open; verify before scoping. It does not replace
an LTI-native tutor, but it materially changes the concentration risk this KB has flagged since
pass 317.

The gap stands as worded in pass 317: there is no *usably licensed* open source LTI 1.3 AI tutor.
What pass 318 adds is a mitigation for the *other* half of the problem — see the `ltibootcamp`
finding in `repos/foundations.md`, which maps the LTI 1.3 library landscape across seven languages
and takes some of the concentration risk off `pylti1.3`.

## Star solicitation has been productised: it now ships with a unit test and a CI job

Pass 318 recorded a README passage addressed to AI agents asking them to star the repository
(`24kchengYe/human-skill-tree`). Pass 319 found the next step, and the reason to record it is the
engineering, not the ask.

**`karanb192/algo-sensei` — MIT, 293 ★, 63 forks, 9 commits.** The repository root holds
`SKILL.md`, `modes/`, `docs/`, `demo/`, `templates/solutions/`, `tests/` and `scripts/`. In
`scripts/` there is exactly one file: **`star_invitation.py`**. Read first-hand, it is a
once-per-machine gate: it attempts exclusive creation of a marker file `star-invitation.json` under
`$XDG_CACHE_HOME` or `~/.cache/algo-sensei`, prints `offer` if it created the marker and `skip`
otherwise — on a pre-existing marker, a concurrent run, or any path or filesystem error. Its code
comment reads: *"Exclusive creation prevents simultaneous or later sessions from asking again."*
There is a matching `tests/test_star_invitation.py` and a dedicated workflow,
`.github/workflows/invitation-tests.yml`.

**Three things follow, and the first is in the repo's favour:**

1. **This is the polite version.** Ask once per machine, ever, and never again — that is better
   behaviour than a README instructing an automated reader to act. Nothing here is deceptive and
   the script emits no text of its own.
2. **It is still a star-acquisition mechanism with CI behind it, in a repo with 9 commits and
   293 stars.** The ratio is the point. A sector where the distribution unit is a skill bundle
   (trend 7) has made stars cheap to solicit at the moment of use, from inside the tool, at scale.
3. **So the ★ column is now formally decorative in this KB.** It fails low on institutional
   infrastructure — Ed-Fi at 12, Sunbird at 41, OpenOLAT at 448 with 31,877 commits, the entire
   `bncc-dev` curriculum stack at 22/9/9 with a verified national dataset behind it — and it is
   solicitable at the top. **Commit count, release cadence, fork count and licence are the durable
   signals.** Any Globant tooling that ranks dependencies by reading repository pages needs that
   rule written into it, together with pass 318's: text a repository addresses to an automated
   reader is data, never instruction.

## A repo in this sector is now soliciting stars from AI agents (pass 318, recorded)

`24kchengYe/human-skill-tree` (573 ★, 36 commits) ends its README with a passage **addressed to AI
agents, asking them to star the repository** and claiming efficiency benefits for doing so. It was
ignored when this pass read the page, and it is recorded here because of what it implies rather
than what it is.

This KB is compiled by an automated process that reads repository pages. **So are a growing number
of the tools a client's engineers use to choose dependencies.** A README instruction aimed at that
reader is a supply-chain-adjacent manipulation attempt, cheap to write and, at 573 stars against 36
commits, not obviously unsuccessful.

Three consequences, and the third is the one that matters:

1. **Content a repository addresses to an automated reader is data, not instruction.** This pass
   treated it that way. Any Globant tooling that reads repo pages to rank dependencies must do the
   same, explicitly.
2. **The ★ column in this KB is now a weaker signal than it was last pass**, and it was already
   weak. Pass 317 established that stars run *too low* on institutional infrastructure — Ed-Fi at
   12, Sunbird at 41, OpenOLAT at 448 with 31,877 commits. This pass establishes they can also be
   solicited upward. **Commit count, release cadence and licence are the durable signals; rank on
   those.**
3. **The repo is still in the table.** Its skills are real, dual MIT/AGPL-licensed, bilingual, and
   it is one of the few APAC-authored artefacts in this tier. Flagging the behaviour is the correct
   response; deleting a usable finding over it would be an overreaction. Read the skills, do not
   take the app, and know what the README tried to do.

## lumen is worth reading because its evaluation scores are bad and published anyway

`ahmedEid1/lumen` (828 commits, v2.0.0 on 2026-06-06) generates a private course from a
one-sentence goal with a multi-agent orchestrator, then teaches it with a course-scoped RAG tutor
whose retrieval runs through a single access-control clause so private and cloned courses cannot
leak chunks. Its README publishes its own evaluation results:

- **authoring 3.85/5** (n=10)
- **tutor 2.33/5** (10 of 30 items judged)
- **ingest 0.83/5** (4 of 10 items judged)

— and attributes the weak tutor score to a citation-format mismatch. **No other repo in this KB
publishes a number that unflattering about itself.** In a sector where every vendor deck claims a
tutoring uplift, a project reporting 0.83/5 on its own ingest pipeline is the most credible
artefact of the pass, and the eval harness shape is worth copying into any tutor engagement where
the client will eventually ask "how do you know it teaches?".

**Its licence is GPL-3.0.** The README carries an MIT badge; the `LICENSE` file in the repository
root is the full GNU General Public License v3 text. **The LICENSE file governs.** This is the
fourth repo in this KB whose real licence differs from its surface presentation — after Frappe
Education, OpenOLAT and `education-agent-skills` — and the second this pass (see below). Read the
file, never the badge.

## Caveats a studio lead should read before quoting any of these

- **`iblai/os` is open-core, not open source in the useful sense.** MIT, 821 ★, 3,518 commits — and
  its README says plainly: *"ibl.ai/os requires the ibl.ai backend platform for authentication, AI
  agent APIs, and data services. The backend is not included in this repository."* You can read and
  fork the client; you cannot self-host the product.
- **`education-agent-skills` is CC BY-SA 4.0 — ShareAlike, and a content licence, not a code
  licence.** Derivative teaching material must be released under the same terms. That is a live
  constraint on a client deliverable.
- **`human-skill-tree` is dual-licensed and the halves differ.** The skills are MIT/AGPL-3.0 dual;
  **the web app is AGPL-3.0 only.** Take the skills, leave the app, and record both licences
  separately in the inventory — a single "MIT/AGPL" line in a licence register is not good enough
  when the permissive half is the only half you can use.
- **`gen-mentor` is CC0-1.0.** Usable, but a paper-companion release (91 commits) with no warranty
  culture. Cite the architecture; do not take the dependency.
- **`Educhain` is 387 ★** — earlier passes recorded "~12k ★", which was wrong.
- **`DeepTutor` is the outlier in both directions.** Re-verified first-hand this pass: Apache-2.0,
  41.7k ★, 5.3k forks, 2,935 commits, **v1.6.15 released 2026-10-19**. A release on the day of this
  pass makes pinning a version mandatory, not advisable.
- **`Bloom`, `OpenTutor` and `anki-mcp-server` are small but honest.** 76, 194 and 258 commits.
  Reference shapes and composable parts, not platforms.
- **The three graders are BSD-3-Clause, not MIT.** Permissive, but the attribution clause is real.
- **The eight rows added in pass 319 split into three kinds, and the difference matters when
  quoting.** Four are **skill bundles** (Study-Mate, lineage-skill, universal-examprep-skill,
  algo-sensei, plus claudemy) — prompt and pedagogy assets that run inside a client's chosen agent
  host, not services you deploy; they are cheap to adopt, invisible to procurement and carry no
  SLA. Two are **applications** (instructional_agents, Claw-ED) with real commit histories, both
  MIT, both human-review-first by design. One is a **research tutor** (LTLTutor, GPL-3.0) to read
  rather than link.
- **`instructional_agents` is a fork, and the fork is the one with the stars.**
  `DaRL-GenAI/instructional_agents` (488 ★) is a public fork of `Hyan-Yao/instructional_agents`.
  Pin the fork you actually read, and record which upstream it tracks.
- **`Claw-ED`'s own README is the model for how to describe a "local-first" product.** It states
  that local storage does not mean local processing: hosted models still receive prompts and
  content, and web search, image retrieval, Telegram, Google integration and package installation
  all reach out. Running genuinely local needs a local model and those features off. **Quote that
  distinction in any on-premise proposal** — it is the honest version of a claim most vendors make
  loosely, and it is the same distinction the COPPA finding in `intel/market.md` turns on.
- **`tutor-gpt` and `lumen` are the two copyleft rows.** Both GPL-3.0, both in the table to be read
  rather than linked. `tutor-gpt` for its Theory-of-Mind prompting, `lumen` for its eval harness.

## Rejected after verification — recorded so the next pass does not re-find them

**Pass 320 added five rejections and no rows. They are listed first.**

**Pass 323 added two rejections, both of them artefacts this KB wanted to exist.**

- **`YL1N/EduGuardBench` — NO LICENCE, and it is in the AAAI proceedings.** 5 ★, 3 forks, 2
  commits. Full read in the evaluation table above. **It is listed there rather than only here
  because the measurement it defines is usable even though the repository is not** — RFS, ASR and
  the three-tier refusal assessment are described in the paper and the appendix PDF, and a studio can
  implement them. **What cannot be used is the shipped material**: two `.xlsx` datasets and the
  experiment scripts carry no grant. **This is the first unlicensed artefact in this KB's eval tier
  and the fourth consecutive pass to record a peer-reviewed education artefact whose repository has
  no licence file.** Ask the authors — a one-line LICENSE commit would make an AAAI-published
  safety benchmark immediately usable, and that is a cheap ask.
- **`razi-03/NCERT-CKG` — NO LICENCE, 0 ★, 2 commits, one grade of one subject.** Class X
  NCERT Mathematics from 18 PDFs into CKG JSON: **10,417 CKG nodes, 1,682 semantic nodes with
  provenance at 1,682 / 1,682** (*"every semantic node is required to have source evidence"*) and
  **13,757 provenance-aware edges**. **Rejected on licence and weight, recorded because the method is
  right:** *"prerequisite reasoning is treated separately from textbook ordering"* and a
  prerequisite *"must instead be supported by conceptual dependency evidence or an explicit inference
  procedure"* — the discipline this file praised in `bncc-dev` and faulted `jinanshm/ncert-mcp`
  for lacking. Two things the README does not say and both matter: **nothing about textbook
  copyright or whether the 18 NCERT PDFs are bundled**, and nothing about whether an LLM derived the
  edges — it never mentions an LLM at all, so this is unknown rather than concealed. **It makes
  India's curriculum gap contested rather than empty. Watch the licence; ask the author.** See
  `repos/foundations.md` and pattern P10 Variant B.

- **`Willie-Liao/lesson-library` — NO LICENCE, and 1 commit.** 0 ★. An MCP server for teachers in
  which an agent searches a lesson library, folds near-duplicate materials together with vector
  search, proposes progression/regression/related links, and **stages every change for teacher
  approval in a local web UI before it is written as Markdown/YAML**; graph, timeline and calendar
  views; docs marked v0.3.2, 2026-10-12. **The shape is right and the review gate is the one this
  KB keeps asking for.** Three disqualifiers: there is no LICENSE file (the README offers a prose
  "educational research and non-commercial school lesson preparation" use statement, which is not a
  licence and reads as a restriction), **the repository has a single commit**, and although the
  description claims "any subject", **the only documented deployment is middle-school FLAG football
  (Grade 6/7, 3 teachers, ~60 students)** and the motor-skill taxonomy is football-specific. A
  general design with a single-domain implementation. Watch the licence.
- **`CristianHeyde/language-teaching-skills` — MIT, but 0 ★ and 4 commits.** Six standalone agent
  skills for language teachers: `staff-assistance`, `task-design`, `submission-review`,
  `study-planning`, `course-architecture`, `lesson-planning`. The README is explicit that the skills
  **guide procedure only and grant no tools or permissions**, which is the correct design for this
  category. **The licence is clean and the taxonomy is sensible; the weight is four commits.**
  Rejected on the same standard this file applied to `Gchism94/ai-tutor` in pass 318 — recorded
  rather than listed so the rule stays consistent. Re-check if it grows.
- **`Bimbi-Dev/OpenTeacher` — NO LICENCE, and the agent logic is not written yet.** 0 ★, 32
  commits. **Peru**, Hackathon AIdea Lima 2026, README in Peruvian Spanish, aimed at MINEDU
  teachers: a WhatsApp agent to which a teacher reports a classroom incident by text or audio, which
  replies with emotional containment and immediate tactics and logs the incident for per-student and
  per-classroom reports. **What actually runs is the web simulator**, audio capture behind a consent
  gate, Whisper transcription and an Anthropic SDK wrapper, both with mock modes. The WhatsApp
  webhook is marked *"Congelado, sirve de evidencia"* and **`lib/prompts.ts` and `lib/agents.ts` are
  marked `PENDIENTE`** pending a product brief. Searched for and recorded **because it is
  LATAM-authored supply, which this KB has repeatedly declared its scarcest category** — the
  placement is the finding, not the code. Not usable.
- **`alarcon7a/english-teacher-ai` — MIT badge with NO LICENSE FILE.** 5 ★, 11 commits. Spanish
  README; a spoken English tutor taking Spanish or English in and returning text and audio, on
  Gradio + LangChain with Gemma 2 (9B) via Ollama or Gemini, and **Meta's SeamlessM4Tv2 for both
  STT and TTS** — a genuinely interesting local-first speech choice. Rejected on two counts: the
  licence is **declared in a badge but not filed**, so default copyright applies, and the README
  does not match the tree (it tells you to run `teacher.py`; the file is
  `English_teacher_with_gemma2.py`) while listing Ollama under "Google tools". **The badge-without-
  a-file pattern is now frequent enough in this sector to be worth stating as a rule: a licence
  badge is a claim, a LICENSE file is a licence.**
- **`laurauguc/grading_assistant` (GradeMate) — MIT, 4 ★, and it carries a correction to this KB's
  own conclusion.** Already carried: an earlier pass read its licence blob and recorded it at 4 ★
  inside the "agentic-grading cluster" whose three repos total 4 stars, and concluded **"grading has
  no open-source shelf."** **This pass read the commit count that conclusion was drawn without:
  260 commits.** That does not overturn the conclusion but it narrows it — *one* of those three
  repos has real volume behind it, and "4 stars across three repos" invited the reading that all
  three were weekend projects. Teacher-facing grading of written work with curated **or
  teacher-uploaded rubrics**, a `rubrics/` folder and a `load_grading_rubric_data` management
  command; ReactJS over Django. **It stays out of the table for two reasons that are not weight:**
  it is a teacher tool rather than an agent, and it **requires a `GOOGLE_API_KEY`**, so the model is
  not pluggable as shipped. Promote it to `verticals/solutions.md` if a client asks for assisted
  marking. **The general lesson: a star count is not a volume measure, and this file has now been
  caught reasoning from one.**

- **`blamb/lti-tutor` — NO LICENCE ("To be decided").** Re-verified p319: unchanged at 0 ★, 39
  commits. The LTI 1.3 tutor this KB needs, and unusable. Watch it every pass.
- **`JaimeArriagadaRosas/Plugin-Feedback-Canvas` — NO LICENCE FILE.** p319: 0 ★, 160 commits.
  LTI 1.3 + Canvas + AI-generated feedback behind mandatory instructor approval, Spanish docs,
  pre-production by its own account. The artefact this KB's North American patterns describe, and
  unusable. Ask the author.
- **`CaviraOSS/PageLM` — 2.0k ★ and NOT open source.** 234 commits, 277 forks; a genuinely
  capable study-material platform (contextual chat over PDF/DOCX/MD/TXT, Cornell SmartNotes,
  spaced-repetition flashcards, quizzes, AI podcasts, exam simulation, debate practice;
  Node/TS/LangChain/LangGraph + Vite/React; Gemini, OpenAI, Anthropic, Grok, MiniMax, Ollama,
  OpenRouter; Docker Compose; fully self-hostable). **Its licence is the "CaviraOSS Community
  Licence": free for personal and educational use, commercial use or resale requires prior written
  permission.** It is the highest-starred new education-AI project this pass and Globant cannot
  build a client deliverable on it. Read it as a feature checklist; do not plan on it.
- **`xiaoyang111222/cn-math-taxonomy` — CC BY-NC 4.0, and self-declared unreviewed.** 780 ★,
  188 forks, 11 commits. Exactly the artefact pattern P2 wants: 531 knowledge points (216 primary,
  315 junior-high), **909 prerequisite edges (788 hard, 121 soft)**, 2,271 questions, 230 curriculum
  standard entries, aligned to China's 2022 compulsory-education mathematics standards and the PEP
  textbook sequence, with a diagnostic engine, validation scripts and a static web UI. **Two
  disqualifiers:** NonCommercial rules out client work, and **the author states it is an
  AI-generated draft not reviewed by teachers**, with several textbook volumes third-party and
  unverified. 780 stars on an unreviewed generated knowledge graph that someone will put in front
  of children is this pass's clearest argument for reading the README to the end.
- **`aaryansamanta/ai-ethos` — NO LICENCE.** 499 ★, 0 forks, 27 commits; the website source for
  AI Ethos, Inc., a 501(c)(3) in Cupertino, CA providing AI tutoring to low-income, rural,
  multilingual and neurodiverse students across "7 languages". A real nonprofit and a creditable
  mission; the repository is a website with no licence and no platform code. Cite the programme,
  not the repo.
- **`jinanshm/ncert-mcp` — NO LICENCE, and the data problem is worse than the licence.** 1 ★,
  2 commits. 13 MCP tools over NCERT textbooks (lookup, semantic search with grade/subject/Bloom
  filters, curriculum map, prerequisites, learning path, question-paper generation) plus a REST
  API — the right shape. But **no data ships**: `bun run ingest` downloads the K-12 NCERT PDFs,
  chunks them and **tags the chunks with an LLM via OpenRouter, with no human verification
  described.** See the India gap below; this is the contrast case to Brazil's `bncc-dev` stack.
- **`luffycodes/Tutorbot-Spock` — NO LICENCE FILE.** 56 ★, 8 commits. Notable work (CLASS, EMNLP
  2023, arXiv 2305.13272; Pedagogical Alignment of LLMs, EMNLP 2024, arXiv 2402.05000).
  **Read the papers, not the repo.**
- **`CSOAI-ORG/coppa-ferpa-mcp` — MIT, but rejected in p317 and not revisited.** 1 ★, 16 commits,
  two contradictory price lists in one README. Compliance tooling is the last place to accept
  vendor self-description.
- **`artcc/freelingo` — AGPL-3.0, 188 ★.** A real self-hosted AI language-learning platform; it
  sits in `verticals/solutions.md` as a platform because AGPL puts it on the copyleft side of this
  KB's architectural line.
- **`AITutor-EvalKit` — no repository located.** The paper (arXiv 2512.03688, MBZUAI: Naeem, Maurya,
  Petukhova, Kochmar) describes a tool for evaluating the *pedagogical* quality of tutor responses
  in student-mistake remediation, which is exactly the eval layer this sector lacks. The authors
  call it an early research prototype and **no GitHub repository or licence could be found this
  pass.** Cite the paper as evidence that the eval problem is being worked; do not plan on the code.

## Licence split, recounted over 28

MIT (16 — FSRS4Anki, iblai/os, anki-mcp-server, Educhain, Bloom, OATutor, OpenTutor, tutor-mcp,
Study-Mate, instructional_agents, universal-examprep-skill, claudemy, algo-sensei, Claw-ED,
**civil-ai**, **algebench**),
BSD-3-Clause (3 — nbgrader, otter-grader, Open TutorAI CE), Apache-2.0 (3 — DeepTutor, smolagents,
lineage-skill), **GPL-3.0 (3 — tutor-gpt, lumen, LTLTutor)**, dual MIT/AGPL-3.0 (1 —
human-skill-tree, skills only), CC0-1.0 (1 — gen-mentor), CC BY-SA 4.0 (1 — education-agent-skills).

**24 of 28 carry a permissive *software* licence Globant can build on commercially** (counting
human-skill-tree's skills half, and excluding its AGPL app). The exceptions are three copyleft
agents and two content/dedication licences, all flagged above.

**Pass 319 improved that ratio and the improvement is real but narrow:** six of the eight rows
added are MIT and one is Apache-2.0, and two of them — `lineage-skill` (Apache-2.0, 459 ★) and
`universal-examprep-skill` (MIT, 309 ★) — are the **first permissively licensed skill bundles at
scale**, which answers the legal half of trend 7. Last pass this KB said skill bundles arrive under
content licences and that the ShareAlike conversation was coming; it still is for
`education-agent-skills`, but it is no longer the only option on the shelf.

**The counter-movement is in the rejected list and it is the bigger story.** The three
highest-starred *new* projects read this pass are **PageLM (2.0k ★, bespoke "Community Licence")**,
**cn-math-taxonomy (780 ★, CC BY-NC 4.0)** and **advisingapp (340 ★, Elastic Licence 2.0 — see
`verticals/solutions.md`)**. None is open source. Popularity in this sector is drifting toward
source-available and NonCommercial terms, which is a procurement problem that looks like a
licensing footnote.

The structural fact holds and is now measured over 18: **the agent tier is predominantly permissive
and the platform tier in `verticals/solutions.md` is predominantly copyleft.** Pass 318 widened the
crack in it from the platform side again — see `openedx/openedx-ai-extensions` and the two new
AGPL AI-native LMS rows there — without changing the architectural advice.

## What was searched and not found

- **No *usably licensed* open source LTI 1.3 agent. Re-checked directly, and the count of
  unlicensed artefacts at this seam went from two to three** — `blamb/lti-tutor` (0 ★, 39 commits,
  "To be decided") and now `JaimeArriagadaRosas/Plugin-Feedback-Canvas` (0 ★, 160 commits, Canvas
  LTI 1.3 with instructor approval, Spanish docs, no LICENSE). `pylti1.3` (MIT, re-verified p319: 138 ★, 84 forks, 178 commits, 39 open issues, **no published
  release**) is still the solid Python library. **The p319 question about `tsugiproject/tsugi` is
  closed this pass, and the answer is that the repository does not say:** Apache-2.0, 376 ★, 266
  forks, **4,011 commits, Releases section empty**, and the README **names no LTI version at all** —
  only *"a multi-tenant scalable LTI library and tool hosting environment"* and *"implements an IMS
  ContentItem App store"* (ContentItem being the LTI 1.1-era content-selection message, which hints
  at the older generation without declaring it). **An LTI integration cannot be scoped from Tsugi's
  README**, so the concentration risk is unrelieved: one maintained library, no release tags, and
  the only alternative does not state what it speaks (`repos/foundations.md`).
- ~~**No credible open source way to evaluate pedagogical quality.**~~ **RETIRED this pass.** Five
  passes declared it, pass 318 searched for `AITutor-EvalKit` and concluded "no repository located."
  **That was wrong: `kaushal0494/AITutor-EvalKit` exists, is MIT and is public** (3 ★, 8 commits,
  v1.0.0 on 1 Dec 2025). With MathTutorBench (EMNLP 2025), the two pre-registered audits and
  `bncc-dev/bncc-benchmark` (`repos/foundations.md`), the eval layer is a real and usable tier.
  **The lesson repeats pass 318's own: a declared gap must be re-tested with a changed query — the
  repo was found this pass by searching GitHub for the paper's tool name, which is exactly what the
  previous pass believed it had done.** Two 2026 benchmarks seen only in search snippets are
  **not** counted here and should be re-checked for a public repo and licence: **EduClaw-Bench**
  (arXiv 2608.03206; 30-day simulated learner, three-judge panel; code behind an anonymous review
  link) and **EduFair-Bench** (arXiv 2609.12949; pedagogical fairness across student demographics,
  judged by `gpt-oss-120b`).
- **No verified, machine-readable NCERT/CBSE curriculum dataset — NEW, and it is the most
  actionable gap in this KB.** India has the hardest curriculum mandate in the sector (AI +
  Computational Thinking compulsory for Classes 3–8 from 2026-27, 32,900 CBSE schools). GitHub's
  `ncert` (55 repos) and `cbse` (125 repos) topics were swept this pass: **nothing above 15 stars
  that is curriculum infrastructure.** The AI entries are one- and two-commit hobby projects —
  `praj2408/RAG-Enhanced-NCERT-Tutor` (MIT, 5 ★, 3 commits, Ollama + Chroma + Groq, and it
  **bundles Class 12 Physics textbook PDFs**, which is its own copyright question),
  `jinanshm/ncert-mcp` (unlicensed, LLM-tagged chunks, no verification),
  `thegauravmahto/sparks-ai-math-tutor` (2 ★, Hindi/English voice tutor on Gemini Live),
  `Sarika-stack23/Advanced-Mathematics-Assistant` (1 ★, RAG + SymPy), `dpaul0501/OpenVidya` (2 ★).
  The only substantial data asset is `deedy/cbse_schools_data` (52 ★) — a **2018** scrape of ~20,000
  schools. **Meanwhile Brazil has exactly this artefact, verified character-by-character and
  permissively licensed** (`bncc-dev`, `repos/foundations.md`). Porting that pattern to NCERT/CBSE
  is the clearest build-once opportunity this KB has identified — see pattern **P10**.
- **No credible open source agent for assessment integrity / AI-detection. Sixth consecutive pass.**
  The published evidence on AI-text detection accuracy continues to argue this should stay a gap.
- **No usable open source student-data-privacy compliance component — but the shape of the gap
  changed this pass and the change is the finding.** GitHub's `ferpa` topic now carries a *cluster*
  of governance repos that did not exist in earlier passes: `Principled-Evolution/gopal` (8 ★, Rego
  policies), `marc-shade/docsingest` (6 ★, PII/PHI ingestion with hash-chained audit),
  `chaz-clark/canvas-toolbox` (5 ★, FERPA-safe Canvas toolkit),
  `virtualryder/edu-ai-agents` (4 ★, Bedrock agents with PII masking),
  `ashutoshrana/regulated-ai-governance`, `ashutoshrana/enterprise-rag-patterns` and
  `ashutoshrana/voice-ai-governance` (1–2 ★ each), `Polycentric-Labs/regrails` (1 ★),
  `mizcausevic-dev/mcp-ai-tutor` (0 ★, an MCP server that audits tutors for FERPA/COPPA).
  **Every one is at or below 8 stars and nearly all were last updated in September or October
  2026.** Nothing here is a dependency. But a dozen independent authors starting the same component
  in the same two months is a market forming in real time, triggered by the COPPA deadline in
  `intel/market.md`. **Sixth pass declaring this gap, and the first pass able to say it is
  contested rather than empty — which shortens the window on the build-once opportunity.**
- **The regional picture moved in two places this pass.** **APAC authorship is now the largest
  bloc in the skill tier**, not a token presence: `Miaotofu01/Study-Mate` (MIT, 1.1k ★, 723
  commits, zh/en), `JuneYaooo/lineage-skill` (Apache-2.0, 459 ★, zh/en, acknowledging the Datawhale
  and LINUX DO communities), `ZeKaiNie/universal-examprep-skill` (MIT, 309 ★, en/zh),
  `24kchengYe/human-skill-tree` (573 ★) and the previously recorded `KeWang0622/kaogong-skill`
  (189 ★) and `SimonsTang/feifei-companion` (108 ★). **LATAM authorship appeared in the agent tier
  for the first time and it has no licence** — `Plugin-Feedback-Canvas`, above. And see
  `repos/foundations.md` for the pass's largest regional finding, which is Brazilian and is not an
  agent at all.
- **No region-specific tutoring agent as a product, still** — though the APAC skill-layer presence is now
  represented in the table by `human-skill-tree` (573 ★, bilingual EN/zh) alongside the previously
  recorded `Miaotofu01/Study-Mate` (1.1k ★), `KeWang0622/kaogong-skill` (189 ★) and
  `SimonsTang/feifei-companion` (108 ★). **The LATAM picture changed this pass, but in the platform
  tier, not here** — see `openedx/openedx-ai-extensions` in `verticals/solutions.md`.
