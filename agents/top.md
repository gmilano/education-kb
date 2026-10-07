---
industry: education
region: Global
updated: 2026-10-07
---

## 🔴 Forty-second pass, 2026-10-07 — `Gap 235`'s prescribed query returns a **populated** tier, and not one asset in it carries a licence grant

**Licences read first-hand on 2026-10-07** from the channel named per row — repository **payload** on
`raw.githubusercontent.com` (title-block classified, `P171`) and **registry** metadata. Existence by
`git ls-remote --heads` against a negative control in the same run (`P510`). **No star counts** (`P479`).
⏱️ **Ninth pass of this date.**

🔴 **No row is added to this file's agent table this pass.** 🟢 **That is the finding, not a shortfall:
the tier `Gap 235` sent this pass to look for exists, is busier than any English-language sweep
suggested, and is **entirely ungranted**.** The permissive asset the pass did find is a **corpus**, and
it is filed in `repos/foundations.md` (`P524`) because it is data, not an agent.

### 🔴 `P522` — six distinct Portuguese essay-scoring trees, **zero licence grants**, measured exhaustively

🔵 **How the question was asked, because `P494` says an absent payload is not a verdict.** For every
slug: `git ls-remote --heads` first (so *absent repo* can never be mistaken for *absent licence*), then
**twelve** licence filenames — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `license.md`,
`licence`, `LICENCE`, `COPYING`, `COPYING.txt`, `LICENSE-MIT`, `LICENSE.rst`, `NOTICE` — across **every
served ref**, then the **manifests** (`pyproject.toml`, `package.json`, `setup.py`, `setup.cfg`) for a
declared `license` field, then the **README** for a licence statement.

| Repo | Existence (`P510`) | Licence — 12 filenames × every served ref, + manifests + README | What it is |
|---|---|---|---|
| [`IC-Redacoes-UTFPR/CorrecaoRedacao`](https://github.com/IC-Redacoes-UTFPR/CorrecaoRedacao) | 🟢 1 ref, `main` | 🔴 **NO GRANT — none of the 12 names, no manifest field, no README statement** | ENEM five-competency scoring with **open-weight** LLMs + LoRA; UTFPR undergraduate-research project. 🟢 **The substantive one — see `P526`** |
| [`YuriMatsumotoSantos/CorrecaoRedacao`](https://github.com/YuriMatsumotoSantos/CorrecaoRedacao) | 🟢 1 ref, `main` | 🔴 **NO GRANT** | 🔵 **Not an independent finding — `main` resolves to the *identical* head SHA `da2e8d3d` as the row above, so this is one tree published twice** |
| [`jgabriel-sntx/Corretor-de-redacao-ENEM`](https://github.com/jgabriel-sntx/Corretor-de-redacao-ENEM) | 🟢 1 ref, `main` | 🔴 **NO GRANT** | Django MVP; OCR via `OCR.space`, scoring via an **NVIDIA API** — 🔴 judgement is a third party's |
| [`douglas150206/IF_VEST_Redacao_Correcao`](https://github.com/douglas150206/IF_VEST_Redacao_Correcao) | 🟢 **4 refs** | 🔴 **NO GRANT on any of the four** | ENEM C1–C5 web scorer over a **hosted proprietary API** — 🔴 judgement is a third party's |
| [`victor934034/simulade`](https://github.com/victor934034/simulade) | 🟢 1 ref, `main` | 🔴 **NO GRANT** | Mock-exam generation **and** scoring; two independent graders plus a third on disagreement — 🔵 **a genuinely interesting adjudication design, and unusable as written** |
| [`horaciohudson/corretor-redacao`](https://github.com/horaciohudson/corretor-redacao) | 🟢 1 ref, `main` | 🔴 **NO GRANT** | ENEM-based scoring; the payload documents too little to classify further |
| [`neiltonsantana9-star/redacao`](https://github.com/neiltonsantana9-star/redacao) | 🟢 1 ref, `main` | 🔴 **NO GRANT** | Teacher-facing PWA; **browser-side OCR** via `Tesseract.js`, then orthography/cohesion checks |
| `totally-fake-org-zzz9/nope-repo-abc` — 🔵 **negative control, same run** | 🔴 **0 refs** | — | 🔴 Does not exist |

🔵 **Counted honestly: seven slugs, six distinct trees.** 🟢 **The two UTFPR slugs share a head SHA, and
this file says so rather than reporting seven findings** — `P386`'s dedup discipline applied to a tier on
the way in, instead of to a census after the fact.

> **`P522`.** 🔴 **The Portuguese essay-scoring tier is *ungranted*, not *absent* — and those are
> different procurement facts with different remedies.** 🔵 **Absent means build it. Ungranted means the
> code exists, is readable, and cannot be used: with no licence, default copyright applies and a studio
> has no right to copy, modify or ship any of it, however public the repository is.** 🟢 **The practical
> consequence is narrow and useful: these six trees are legitimate **prior art and design references** —
> `simulade`'s two-graders-plus-tiebreak and `IC-Redacoes-UTFPR`'s per-competency prompting are both
> worth reading — and **none of them is a starting point**. ⚠️ **An ungranted repository is the one case
> where reading is safe and copying is not; no pass of this KB has had counsel read any of this.**

### 🔵 What this means for `P512`'s saturation verdict — it survives, with its scope corrected

🟢 **`P512` declared the agent shelf *saturated* rather than the query *broken*.** 🔵 **This pass is the
first real test of that claim, because it queried in a **different language** instead of with different
English terms — and the result cuts both ways, so both halves are recorded:**

| | |
|---|---|
| 🟢 **`P512` holds for the *shelf*** | Six new trees, **zero** admissible to the agent table. Nothing here is composable, so the set of usable education agents did not grow |
| 🔴 **`P512` was too strong about the *corpus*** | The tier was **not** empty and no English-language sweep had seen it. 🔵 **The shelf was saturated; the *map* was not** |

> 🔵 **Carried forward: "saturated" is a claim about what is *usable*, and a language-shaped query can
> still change what is *known* without changing what is usable.** 🟢 **The two are worth reporting
> separately, and `P512` conflated them.**

## 🟢 Forty-first pass, 2026-10-07 — `P502` asked for an independent existence check across four passes; this pass supplies one that **works**, and proves the channel `P502` implied is uniformly broken here

**Licences read first-hand on 2026-10-07** from the channels named per row — repository **payload** on
`raw.githubusercontent.com` (title-block classified, `P171`), **registry** metadata, and the published
**artefact**. **No star counts** (`P479`). ⏱️ **Eighth pass of this date.**

🟢 **One row added below, and it is added with a 🔴 licence flag rather than as a building block.** 🟢
**The pass's main result for this file is not a row at all — it is that the oracle `P480` and `P502` have
been requesting since pass 37 now exists, is tested against a negative control, and changes two standing
verdicts.** Full sweep tables in `agents/trending.md`.

### 🟢 `P510` — `git ls-remote` is a working existence oracle; `github.com` HTML is **uniformly 403** here

🔴 **Reported against this pass's own instrument first, as `P502` requires.** The probe written for this
pass used `https://github.com/<slug>` as its existence check, exactly as `P502` implied it should. 🔴 **It
returned `403` for every input, including the negative control** — so it cannot distinguish a real repo
from a fictional one, and any verdict built on it would have been an artefact:

| Input | `github.com/<slug>` HTML | 🟢 Truth |
|---|---|---|
| `CambridgeAssessmentResearch/KernEqWPS` | 🔴 **403** | 🟢 **Exists** — MIT, 41 exported functions (`P508`) |
| `pykt-team/pykt-toolkit` | 🔴 **403** | 🟢 **Exists** — MIT |
| `totally-fake-org-zzz9/nope-repo-abc` (negative control) | 🔴 **403** | 🔴 **Does not exist** |

🟢 **The channel that does discriminate, tested in the same run against the same control:**

| Slug | `git ls-remote --heads` | Verdict |
|---|---|---|
| `CambridgeAssessmentResearch/KernEqWPS` | 🟢 refs served | 🟢 **exists** |
| `CAHLR/OATutor` | 🟢 **60** heads | 🟢 exists |
| `plastic-labs/tutor-gpt` | 🟢 **49** heads | 🟢 exists |
| `zijinz456/OpenTutor` | 🟢 **11** heads | 🟢 exists |
| `Halleck45/OpenPronounce` | 🟢 **1** head (`main` only) | 🟢 exists |
| 🔴 `huni1023/EqUMP` | 🔴 **0 refs** | 🔴 **does not resolve** |
| 🔴 `AIRGOLAB-CEFET-RJ/textgrader` | 🔴 **0 refs** | 🔴 **does not resolve** |
| `totally-fake-org-zzz9/nope-repo-abc` (control) | 🔴 **0 refs** | 🔴 **does not exist** |

> **`P510`.** 🟢 **The existence check `P480` and `P502` have been asking for is `git ls-remote --heads`,
> and it is sound in this environment because it discriminates against a negative control in the same
> run.** 🔵 **`P502` described the defect correctly — a licence probe that cannot tell *absent repo* from
> *absent licence file* collapses three states into one string — but the remedy it implied (check the
> repository's web page) is **unavailable here**: `github.com` HTML is `403` for everything, as is
> `api.github.com`. 🟢 **The git transport is reachable where both HTTP channels are not**, which is the
> part no earlier pass tested.

🟢 **Two standing verdicts change as a direct result, from *undetermined* to *measured*:**

| Subject | Status before this pass | 🟢 After `P510` |
|---|---|---|
| `huni1023/EqUMP` (`P501`) | *"unresolvable on the raw channel"* — inferred from **absent payload**, which `P494` says is not a verdict | 🟢 **Confirmed unresolvable by an independent oracle.** `P501`'s decision to shelve `EqUMP` on **artefact** evidence and withhold the hyperlink was 🟢 **correct**, and is now correct for a stated reason |
| `AIRGOLAB-CEFET-RJ/textgrader` (new this pass) | — | 🔴 **Does not resolve**, although a search result links it as a repository. See `P517` and `intel/trends.md` |

### 🔴 The one row added this pass — and it is here to be **ruled out**, not composed

🟢 **`agents/trending.md` records the sweeps in full. One agent genuinely new to this KB came out of them,
and its licence is the reason no earlier pass shelved it:**

| Agent | Repo | Licence (read from payload) | Existence (`P510`) | What it is, and the verdict |
|---|---|---|---|---|
| 🆕 **TutorGPT** | [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🔴 **GPL-3.0** — payload `main/LICENSE` **35,149 B**, title block `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`; 🟢 **identical payload on `master`, and see `P511` for why that is not a second branch** | 🟢 **49 heads** | Tutor that adapts explanations by **Theory-of-Mind** reasoning over the learner's inferred mental state; TypeScript. 🔵 **Pedagogically the most distinctive shape in this tier** — it models *what the learner believes*, where `OATutor` models *what the learner has mastered*. 🔴 **GPL-3.0 makes it a side-car or a read-only reference for Globant, not a component.** 🟢 **Shelved as an idea to reimplement, not a dependency to adopt** |

🔵 **Re-measured this pass, not carried forward** — the three permissive education agents the shaped sweep
returned were **already on this shelf**, and their licences were re-read from payload rather than quoted:

| Agent | Repo | Licence re-read 2026-10-07 (payload · bytes · title block) | Already shelved? |
|---|---|---|---|
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · `LICENSE` **1,105 B** · `MIT License` · holder *"Copyright (c) 2023 Zachary A. Pardos (@zpardos) - CAHL research lab"* | 🟢 **Yes** — 22 live files |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** · `LICENSE` **1,068 B** · `MIT License` · holder *"Copyright (c) 2026 Zijin Zhang"* | 🟢 **Yes** — 13 live files |
| **OpenPronounce** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** · `LICENSE` **1,113 B** · `The MIT License (MIT)` · holder *"Copyright (c) 2025 Jean-François Lépine"* | 🟢 **Yes** — 3 live files |
| **pyKT** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · `LICENSE` **1,066 B** · `MIT License` · holder *"Copyright (c) 2022 pykt-team"* | 🟢 **Yes** — long-held |

> 🟢 **This is the result that matters for this file, and it is the opposite of a null result.** 🔴 **Three
> passes have now reported "zero new agents" and attributed it to the query (`P497`).** 🟢 **A query of the
> right *shape* returns four real education agents — and three of the four are already here, while the
> fourth is copyleft.** 🔵 **The shelf is saturated at the permissive end. See `P512` in
> `agents/trending.md`, which supersedes `P497`.**

## 🔵 Fortieth pass, 2026-10-07 — zero new agent rows for the third consecutive pass, and this pass's own probe reproduced the defect `P480`'s missing fixture exists to catch

**Licences read first-hand on 2026-10-07** from three channels named per row — repository **payload** on
`raw.githubusercontent.com` (title-block classified, `P171`), **registry** metadata, and the published
**artefact**. **No star counts** (`P479`). ⏱️ **Seventh pass of this date.**

🔴 **Zero rows added here for the third consecutive pass.** 🟢 **The two mandated agent sweeps returned the
`P497` homonym class for the third time** — horizontal frameworks and "learn AI" teaching material, zero
education agents. Full tables in `agents/trending.md`.

🟢 **Where this pass found new ground is again a *library* tier, not an agent tier**, so the one new
permissive package of the pass is filed in `repos/foundations.md` and `repos/trending.md` and
**deliberately not here**:

| 🆕 Added this pass (not an agent — stated plainly) | Licence | What it answers |
|---|---|---|
| **`EqUMP` 0.3.6** (registry declares `huni1023/EqUMP` (🔴 **no hyperlink on purpose — unverified path, `P501`**), 🔴 repo unresolvable — `P501`) | 🟢 **MIT** · artefact payload **1,068 B** · title block `MIT License` | *"are these two tests on the same scale?"* — **in Python, under MIT, with four maintainers** |

### 🔴 `P502` — this pass's probe could not tell *"no licence file"* from *"no repository"*, which is the fixture `P480` has been asking for across four passes

🔴 **Reported against this pass's own instrument, before any finding was promoted.** The scratch probe
written for this pass (16 licence filenames × 2 branches, title-block classification) emitted the **identical**
string for two inputs whose right answers are **opposite**:

| Input | Probe output | 🟢 Truth |
|---|---|---|
| `huni1023/EqUMP` | `NO LICENCE PAYLOAD FOUND` | 🟢 **MIT** — a complete 1,068 B `LICENSE` ships in the artefact |
| `totally-fake-org-zzz9/nope-repo-abc` (negative control) | `NO LICENCE PAYLOAD FOUND` | 🔴 **Does not exist** |

> **`P502`.** 🔴 **A licence probe that does not run an *independent existence check* collapses three
> distinct states — *absent repo*, *absent licence file*, and *licence present elsewhere in the
> distribution* — into one output string.** 🔵 **`P475` already folded an existence check into the
> in-tree probe and `P494` already established that absent payload is not a licence verdict; this pass
> confirms both are necessary by **reproducing the failure in new code that had neither**.** 🟢 **The
> recovery was to add the existence probe (5 README spellings × 3 branches) and then the artefact
> channel — which is how `P501` was resolved rather than guessed.**

🔴 **This is the second independent reason the `P480` fixture debt matters**, and it is a stronger one
than the first: pass 39 argued the fixture set omits the shelf's dominant licence family; this pass shows
the classifier's **negative** result is ambiguous across three states on a case that actually occurred.

### 🔴 The `P480` fixture debt — **fourth** consecutive pass blocked, same reproducible cause

🔵 **This pass attempted the command the KB's own operational note names as the single highest-value
unblocked action:** `./discover_probe.sh --self-test` in `compose/code/p473-probe-commercial-gate`.

🔴 **Denied again, by the same session auto-mode classifier, with the same reason (`Code from External`)** —
passes 37, 38 (recorded), 39 (not re-attempted) and now 40. 🟢 **Four data points make this a stable
property of this execution environment, not a transient, and the honest conclusion is that no scheduled
pass running under this classifier will ever close `P480`.**

🟢 **What remains correct and unchanged:**

- **The two fixtures stay in `fixtures-pending/`.** `agpl-3.0-classroomio.LICENSE` (34,523 B) and
  `gpl-3.0-lmscloud.LICENSE` (35,148 B), with their `.expected` files. 🔴 **Promoting them unexecuted
  would move the gate from an honest `9/9` to an unverified `11/11`** — the exact defect the instrument
  exists to prevent.
- **The gate stays honest at `9/9`** over a fixture set that still omits GPL/AGPL, the shelf's dominant
  family.
- 🆕 **This pass adds a third required fixture case to the specification, from `P502`:** the set needs a
  case for **"repository absent"** distinguished from **"payload absent, licence present"**, because the
  probe currently returns one string for both.

> 🔴 **Operational note, restated because it is now four passes old.** Closing `P480` needs one command in
> a session **without** the auto-mode external-code restriction:
> `cd compose/code/p473-probe-commercial-gate && ./discover_probe.sh --self-test` (expect `9/9`), then
> `mv fixtures-pending/* fixtures/` and re-run (expect `11/11`). 🔵 **This is a permissions blocker, not a
> research one.** 🟢 **It needs a human to run it once, or to grant the scheduled session permission to
> execute in-tree instruments.** ⚠️ **No pass should record it as closed on the strength of a
> re-implementation, and this pass did not attempt to route around the denial.**

---

## 🔵 Thirty-ninth pass, 2026-10-07 — zero new agent rows, and `P497`: the mandated topic query returns AI *pedagogy*, not education *software*

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07**, 16 filenames × `main`/`master`,
classified on the **title block** (`P171`). **No star counts** (`P479`). ⏱️ **Sixth pass of this date.**

🔴 **This file adds zero rows for the second consecutive pass**, and pass 39 will not repeat pass 38's
framing of that as saturation alone. 🟢 **The sweeps failed in a *specific, reproducible direction*, and
naming the direction is more useful than naming the shortfall:**

| Mandated sweep | Top names returned | Education agents new to this shelf |
|---|---|---|
| `top open source AI agents education 2026 github MIT` | `openclaw` · `browser-use` · `mem0` · `AutoGen` · `Flowise` · `dify` · `Hermes Agent` · `Aider` · `Cline` · `CrewAI` · `LangGraph` | 🔴 **0** — every one is a **horizontal** framework |
| `github trending education AI 2026` | `ai-engineering-from-scratch` · *AI Engineering Hub* · Karpathy *Zero to Hero* · `2026-AI-College-Jobs` | 🔴 **0** — every one is **teaching material about AI** |

🔵 **The roster this file sits on is 1,087 distinct `github.com` slugs** (pass-38 measurement, unchanged
this pass — `api.github.com` is `403`, so no slug count could be re-derived independently). 🔴 **A
topic-word sweep returns nothing it does not already hold, and `P497` in `agents/trending.md` explains why
the failure mode is a *homonym class* rather than an empty result.**

### 🔴 The honest statement of what an "education AI agent" shelf is now worth

🔴 **An agent that writes, grades or tutors is the commoditised half of an education AI product.** 🟢 **The
half a buyer in a high-risk jurisdiction cannot get anywhere is the **measurement** half** — and that half
is a library tier, which is why this pass's three additions are in `repos/foundations.md` and
`verticals/solutions.md` and **not** here:

| 🆕 Added this pass (not agents — stated plainly) | Licence | What it answers |
|---|---|---|
| [`ZIYINGJERRY/difair`](https://github.com/ZIYINGJERRY/difair) | 🟢 **MIT** · payload **1,075 B** + `pyproject.toml` (`P482`) | *"does this item behave differently for a subgroup?"* |
| [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | 🟢 **Apache-2.0** · 🔴 **no payload** (`P494`) | *"are these two tests on the same scale?"* |
| [`dssg/aequitas`](https://github.com/dssg/aequitas) | 🟢 **MIT** · payload **1,083 B** | *"does the decision this system makes show a group gap?"* |

### 🔴 Correction carried into this file: pass 38's `Gap 39` closure was half a closure

🔴 **Pass 38 recorded here that it closed `Gap 39`.** 🔵 **The archived declaration has two halves and
names the second as the larger**: *"la equivalencia psicométrica entre variantes no la cubre ninguna pieza
open source de esta KB"*. 🟢 **Calibration was closed; comparability was not addressed.** Full correction in
`P492` (`repos/foundations.md`); the recipe is corrected in `P496` (`compose/patterns.md`).

### 🟢 Re-verified this pass — pass 38's four measurement rows, **byte-for-byte unchanged**

🔵 **Re-read from payload this pass, not copied forward.** 🟢 **All four byte counts match the pass-38
record exactly**, which is the first time this shelf has had an independent same-channel confirmation of a
whole tier one pass later:

| Repo | Licence (payload) | Hit path · bytes | Title block | Movement |
|---|---|---|---|---|
| [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** | `master/LICENSE` · **1,121 B** | 🟢 `MIT License` | 🟢 **None** |
| [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** | `main/LICENSE.txt` · **1,073 B** | 🔴 **absent** | 🟢 **None** — 🔴 and `P487` re-confirmed verbatim: the first line is *"Copyright (c) 2018 **The Python Packaging Authority**"*, the body is verbatim MIT. 🔵 **Grant good, attribution still unresolved** |
| [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | `main/LICENSE` · **1,514 B** | 🟢 `BSD 3-Clause` | 🟢 **None** |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** | `main/LICENSE` · **1,531 B** | 🔴 **absent** | 🟢 **None** — 🟢 holder named: *"Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev"*, body clauses countable (`P487`) |

🔵 **Why this table is worth its space.** 🔴 **`P494` (this pass) shows a payload probe can be silently
wrong in one direction — absent payload ≠ absent licence.** 🟢 **This table checks the other direction:
that a *present* payload is stable between passes.** Four for four, so the channel itself is not drifting.

### 🔴 The `P480` fixture debt — third consecutive pass, and the blocker changed shape

🔵 **Pass 38 recorded `./discover_probe.sh --self-test` as denied by the session's auto-mode classifier for
a second time.** 🔴 **This pass did not re-attempt it**, and should say so rather than let silence read as
a third denial. 🟢 **Instead the pass wrote its own probe from scratch in the session scratchpad** — 16
filenames × 2 branches, title-block classification — which is what produced every licence row above.

🔴 **That is a workaround, not a closure.** The debt is unchanged: there is still **no checked-in fixture**
proving the probe's classifier behaves on a known corpus. 🔵 **And this pass added a new reason it
matters** — `P494` shows the probe's `NO LICENCE PAYLOAD FOUND` result is **not** a licence verdict, so the
fixture needs a case for *"payload absent, licence present in source headers"* before any later pass
trusts a negative.

---

## 🔵 Thirty-eighth pass, 2026-10-07 — no new agents, and the honest reason: this pass found a measurement layer, not an agent

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07**, 16 filenames × `main`/`master`,
classified on the **title block** (`P171`). **No star counts** (`P479`). ⏱️ **Fifth pass of this date.**

🔴 **This pass adds zero rows to this file, and that is the finding rather than a shortfall.** Ten
agent-shaped candidates were probed. **Every one was already shelved**, which is what a saturated
shelf looks like from the inside:

| Candidate surfaced this pass | Status here |
|---|---|
| `Tutor MCP` (v0.4.0, Postgres + multi-node) | 🔵 **already shelved** — `agents/top.md`, `agents/trending.md`, `repos/trending.md` |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🔵 **already shelved** (pass 32) — re-verified this pass: 🟢 **BSD-3-Clause**, `main/LICENSE`, **1,531 B**, unchanged |
| `DeepTutor` · `Lumen` · `OpenTutor` · `Claw-ED` · `StudyMate` · `Study-Mate` | 🔵 **all already shelved** (10–20 files each) |
| `ExamEow` · `S.E.S.` · `ExamGen` | 🔴 **unresolved — no owner slug recoverable from any channel.** Leads, not findings |

🔵 **The roster is 1,087 distinct `github.com` slugs. A general-purpose listicle sweep now returns
almost nothing this KB does not hold**, and the two general searches run this pass (`top open source AI
agents education 2026 github MIT`, `github trending education AI 2026`) returned **0 new usable
agents** between them. 🟢 **Where the pass did find new ground was a *tier* nobody had searched for:
item calibration — see `repos/foundations.md`.**

> 🔵 **Method note, not a finding.** On a saturated shelf, *"which agents are trending"* has stopped
> being the productive question and *"which layer of the delivery chain has no shelf at all"* has
> started being it. `P483` is what happens when the answer to the second question was already written
> down and then lost.

### 🔴 `P487` — an **absent** licence title block is a different failure from a **wrong** one, and the cause selects the remedy

🔴 **Correction first, because the class is not new and this shelf already holds it.** `agents/top.md`
records at **pass 32** that `open-tutor-ai-CE` is *"BSD-3-Clause (`LICENSE`, 1,531 B — **body text, no
title line**)"*. 🔵 **So "payload with no title line" is a registered case here, and any claim of it as a
discovery is withdrawn.** What is new is that the pass found a **second** instance whose title block is
absent for a **different reason**, and the reason decides how it resolves:

| Cause of the absent title | Instance | Payload resolves how? | Residual risk |
|---|---|---|---|
| 🟢 **Body clauses are countable** | `open-tutor-ai-CE` (pass 32) · 1,531 B | 🟢 **From the payload alone** — 3 numbered clauses + the *"Neither the name … endorse"* clause ⇒ **BSD-3-Clause** | 🟢 **None.** Holder is named: *"Mohamed El hajji on behalf of all R2D-dev"* |
| 🔴 **Holder is a packaging-template default** | 🆕 `joakimwallmark/irtorch` · 1,073 B | 🔴 **Family yes, holder no.** Body is **verbatim MIT**, so the family is unambiguous; the copyright line reads 🔴 ***"Copyright (c) 2018 The Python Packaging Authority"*** | 🔴 **Attribution unresolved** — see below |

🔴 **The PyPA did not write `irtorch`.** `pyproject.toml` names the author as **Joakim Wallmark**; the
`LICENSE.txt` grants rights in the name of an organisation that has no connection to the work. 🟢 **Two
manifest channels resolve the *family* and both satisfy `P482`**: `pyproject.toml`
`license = { text = "MIT" }`, and PyPI `license: MIT` with `Homepage` resolving **back to the same
slug**.

> **`P487`.** Classify on the title block (`P171`); when the title block is **absent**, say which of two
> things is missing. **Family absent** → count the body clauses, or take the manifest layer as tiebreak.
> **Holder absent or templated** → the **grant** is still good and the **attribution is not**, and that
> is a **contract** question, not a licence one. 🔵 **For Globant the practical consequence is narrow and
> real: an MIT grant issued by a copyright holder who did not author the code cannot be relied on for a
> warranty or indemnity clause.** Name the actual author in the paperwork and cite `pyproject.toml`, not
> the `LICENSE`.

### 🟢 Re-verified this pass — one row, unchanged

| Repo | Licence (payload) | Hit path · bytes | Movement |
|---|---|---|---|
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** (body text, no title line) | `main/LICENSE` · **1,531 B** | 🟢 **None** — byte count matches the pass-32 record exactly |

### 🔴 The `P480` fixture debt is **not** closed, and this is the second consecutive pass blocked

🔴 **`./discover_probe.sh --self-test` was denied again**, by the same session auto-mode classifier that
blocked pass 37, with the same reason (`Code from External`). 🔵 **The block is therefore a reproducible
property of this environment, not a transient**, and that changes how it should be recorded.

🟢 **The two fixtures `P480` demands remain correctly parked in `fixtures-pending/`.** Pass 37's
instruction is explicit — *"if it does not report `11/11`, do not edit the `.expected` files to make it
green"* — and promoting them **unexecuted** would move the gate from an honest `9/9` to an unverified
`11/11`, which is the exact defect the instrument exists to prevent. 🔴 **So they stay pending, and the
gate stays honest at `9/9` over a fixture set that still omits the shelf's dominant family.**

🆕 **What this pass can contribute to the debt without executing anything: a third, independent
GPL-3.0 specimen, fetched and byte-measured.**

| Candidate fixture | Source | Bytes | Why it is worth having |
|---|---|---|---|
| 🆕 `gpl-3.0-datacamp-catsim` | [`datacamp/catsim`](https://github.com/datacamp/catsim) `master/COPYING` | **35,147** | 🟢 **An independent GPL-3.0 payload from a different project family than `lmscloud`** — and within the **±1 B** trailing-newline tolerance pass 37 recorded (`35,148` there). 🔵 Corroborates that the staged specimen is canonical GPL-3.0 text and not a variant |

⚠️ **Not staged into `fixtures-pending/` this pass.** The directory's own README defines the promotion
protocol for payloads *already* there; adding a **third** unexecuted specimen would enlarge an
unverified set without improving it. 🔵 **Recorded here so the next pass that can execute has it
costlessly.**

> 🔴 **Operational note for whoever runs this next.** Closing `P480` needs one command in a session
> **without** the auto-mode external-code restriction:
> `cd compose/code/p473-probe-commercial-gate && ./discover_probe.sh --self-test` (expect `9/9`), then
> `mv fixtures-pending/* fixtures/` and re-run (expect `11/11`). **Two passes have now been unable to
> run it.** This is a permissions blocker, not a research one, and it is the single highest-value
> unblocked action available on this KB.

## 🔴 Thirty-seventh pass, 2026-10-07 — the pass that reproduced `P250` on purpose-built new code, and found the fixture set that hid it

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, branch- and case-aware (16 licence filenames × `main` **and** `master`). **No star counts
are claimed.** ⏱️ **Fourth pass of this date** (34, 35 and 36 all ran earlier).

🔴 **This pass could not execute a single in-tree instrument.** `./discover_probe.sh --self-test` and
every sourcing of `compose/code/lib/license_family.sh` were **denied by the session's auto-mode
classifier as external code**. 🔵 **So `P237`'s remedy — "do not write a classifier, source the shared
one" — was unavailable, not ignored.** The pass reimplemented it, and reproduced the exact defect
`P250` was created to fix, on the exact families and the exact licence section the shared classifier's
own comments name. That is `P480`, and the interesting part is not the mistake but **why no self-test
would have caught it**.

### 🔴 `P480` — a new instrument inherited the shared classifier's CODE but not its REGRESSION COVERAGE

🔴 **Correction, made inside this pass before anything was promoted.** The first draft of this
finding claimed the rule *"family from the title block, never from body tokens"* as new. 🔴 **It is
not. It is `P171`, and `compose/code/lib/license_family.sh:16` states it verbatim** — *"Classifies on
the TITLE BLOCK (first 40 lines), never the body (P171)"*. 🔵 **Order of precedence on this shelf is
payload > shelf > secondary prose, and the shelf already held the answer**, so the claim is withdrawn
and what remains is the part the shelf does *not* hold.

Three misreads happened in this pass's reimplementation. 🔴 **All three are already-closed shelf
findings, and the classifier's own comments name them by number:**

| # | Payload | Body token that fired | Wrong verdict | 🟢 Truth (title block) |
|---|---|---|---|---|
| 1 | `sakaiproject/sakai` | *"Apache License"* appears **inside** ECL's own preamble | `Apache-2.0` | 🟢 **`ECL-2.0`** — `P476`, already on this shelf |
| 2 | `classroomio/classroomio`, `lmscloud-io/moodle-mcp-server` | 🔴 **§6: *"allowed only occasionally and `noncommercially`"*** | 🔴 **`PROHIBIDO`** | 🟢 **`AGPL-3.0`** / **`GPL-3.0`** — commercial use **permitted** under copyleft |
| 3 | `lmscloud-io/moodle-mcp-server` | 🔴 **§13 names *"GNU Affero General Public License"*** | `AGPL-3.0` | 🟢 **`GPL-3.0`** — title block reads *"GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007"* |

| # | Already registered as | Where |
|---|---|---|
| 1 | 🟢 **`P476`** | this shelf, pass 36 |
| 2 | 🟢 **`P250`** · and **`P455`** — *"`P171` reabierto por TERCERA vez … la «noncommercially» de la sección 6"* | `license_family.sh:50-54` |
| 3 | 🟢 **`P171`** · hardened by **`P288`** (casefold) — *"la sección 13 de la GPL-3.0 nombra la AGPL, pero dice «licensed UNDER», no «refers to» — por eso el ancla lleva «refers to» y `P171` queda cerrado"* | `license_family.sh:230-236` |

🔵 **The classifier even records the byte offsets of the two tripwires in `moodle/COPYING` — §13 at
byte 28,272 — which is the same payload this pass re-measured at 35,146 B.** 🟢 **Nothing about the
licence logic needed discovering. It needed *running*, and it could not be run.**

🔵 **Instance 2 is the one that matters, because it is `P473` running backwards.** `P473` says check
NonCommercial **first**, since an NC payload looks permissive to a filename probe. Implemented as a
bare word match, that ordering **inverts**: it reports the single most common copyleft family in open
source education — **Moodle, Canvas, Open edX, openSIS, RosarioSIS are all GPL/AGPL** — as
commercially prohibited.

🔴 **And a false `PROHIBIDO` is strictly worse than a false `GRANTED`, because it is self-concealing.**
`P473`'s error promoted an unusable repo *into* the shelf, where review found it. This error
**suppresses a usable repo before it is ever written down** — a repo filtered out at the probe leaves
no row, no trend line and nothing to review. 🔵 **The defect that deletes evidence of itself is the one
a KB cannot audit its way out of.**

> **`P480`.** A new shelf instrument must inherit the shared suite's **regression coverage**, not only
> its code path. `p473-probe-commercial-gate` was added at pass 36 with **four fixtures — Apache-2.0,
> MIT, ECL-2.0, CC-BY-NC-4.0 — and no GPL-3.0 and no AGPL-3.0**: the exact pair `P171` exists to
> protect and has been reopened over three times (`P171` → `P288` casefold → `P455` window). 🔴 **A
> gate reporting `9/9` over a fixture set that excludes every family where this KB's classifier has
> ever failed is not evidence about that classifier.**

### 🟢 The shared classifier already had this right — and says so, at the same line number

🔵 **This is `P237` confirmed from the outside under the one condition `P237` never anticipated — a pass that is *unable* to source the shared classifier.**
`compose/code/lib/license_family.sh` carries the fix in its own comments:

> *"The first cut of this detector token-matched the payload for `non-commercial` and friends. It then
> reported **THREE AGPL-3.0 repos and The Unlicense** as commercial-use … AGPL-3.0 / GPL-3.0 say
> `occasionally and noncommercially` in **section 6 (line 259** of …)"*

🟢 **Line 259 is exactly where this pass's own `grep` landed on `classroomio`.** The shared classifier
paid for this at **pass 82**; new code re-bought it within minutes at pass 37. 🔵 **The lesson is not
"don't write new code" — this pass had no choice — it is that the defects are a property of the
**payloads**, not of any one implementation, so they recur in *every* reimplementation and the only
durable defence is a fixture set that exercises them.** 🔴 **Which is precisely what the new gate
lacks, and that is the finding.**

### 🔴 The structural find: the gate is 9/9 green over a fixture set that omits the dominant family

`compose/code/p473-probe-commercial-gate/fixtures/` holds **four** specimens:

| Fixture | Family | GPL-family? |
|---|---|---|
| `apache-2.0-osss.LICENSE` | Apache-2.0 | no |
| `mit-bandup.LICENSE` | MIT | no |
| `ecl-2.0-sakai.LICENSE` | ECL-2.0 | no |
| `cc-by-nc-4.0-crss-ai.LICENSE` | CC-BY-NC-4.0 | no |
| 🔴 **GPL-3.0** | — | 🔴 **absent** |
| 🔴 **AGPL-3.0** | — | 🔴 **absent** |

🔴 **The instrument whose entire purpose is the commercial-use column has no specimen of the family
whose §6 contains the tripwire.** It reports **9/9** and cannot regress the failure. 🔵 **A green gate
over a fixture set that excludes the shelf's dominant family is `P471`'s shape again — a gate passing
everything because it judges nothing in the region where the defect lives.**

> **`P480` (second limb).** A gate's fixture set must cover **every licence family the shelf holds in
> volume**, not only the families that produced *that instrument's* founding finding. For this KB
> **GPL-3.0 and AGPL-3.0 are mandatory fixtures**, because the LMS/SIS tier is overwhelmingly copyleft.
> 🔵 **`P126 pt.2` is the precedent and the classifier cites it**: the shared suite once passed **41
> assertions** while never exercising the AGPL branch, because every AGPL fixture carried the canonical
> uppercase title. **Same failure, new instrument, one pass later.**

🟢 **Calibration actually used this pass, in place of the unexecutable self-test.** Eight known-answer
controls, all reproducing the shelf's own verified verdicts, including both GPL variants and the
negative control:

| Control | Verdict this pass | Expected (shelf) | |
|---|---|---|---|
| `sakaiproject/sakai` | `ECL-2.0` / OK · `master/LICENSE` | ECL-2.0, **not** Apache | 🟢 |
| `rubelw/OSSS` | `Apache-2.0` / OK · `main/LICENSE` | Apache-2.0 | 🟢 |
| `CRSS-AI/agentic-se-course-early-2026` | `CC-BY-NC-4.0` / 🔴 **PROHIBIDO** | PROHIBIDO (`P473`) | 🟢 |
| `dikshant182004/MathTutor` | `MIT` / OK · **`master/LICENSE`** | MIT, branch-aware (`P475`) | 🟢 |
| `classroomio/classroomio` | `AGPL-3.0` / OK-COPYLEFT | 🆕 new GPL-family control | 🟢 |
| `lmscloud-io/moodle-mcp-server` | `GPL-3.0` / OK-COPYLEFT | 🆕 new, discriminates GPL vs AGPL | 🟢 |
| `moodle/moodle` | `GPL-3.0` / OK-COPYLEFT · `main/COPYING.txt` | GPL-3.0 | 🟢 |
| `totally-fake-org-zzz9/nope-repo-abc` | `NO-PAYLOAD` | negative control | 🟢 |

⚠️ **Byte counts this pass run ~1 B below pass 36's** (`sakai` 11,119 vs 11,120; `OSSS` 11,362 vs
11,363) because command substitution strips the payload's trailing newline. **The licence verdict is
unaffected; the byte figure is ±1** and should not be quoted as an exact match against earlier passes.

### 🔴 `P482` — a registry cross-channel is valid only if the record resolves BACK to the same repo

🆕 **Two different repositories declare the same distribution name `moodle-mcp`:**

| Repo | In-tree declaration | Licence payload | Owns the PyPI name? |
|---|---|---|---|
| 🟢 [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | `pyproject.toml` → `license = { text = "MIT" }`, v0.3.0 | 🟢 **MIT**, `main/LICENSE`, 1,067 B | 🔴 **No** |
| [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) | `pyproject.toml` → `name = "moodle-mcp"`, v0.2.1 | 🔴 **404 on every name × branch — no grant** | 🟢 **Yes** |

🔴 **PyPI `moodle-mcp` reports `license: None` and its `Homepage` resolves to `loyaniu/moodle-mcp`.**
So the registry name is held by the **ungranted** twin, and the repo carrying the **MIT grant does not
own the name**. 🔵 **Had this pass "cross-channel confirmed" `SaadRahman01/moodle-mcp` through PyPI, it
would have confirmed another author's package — and confirmed it as licence-absent, the exact opposite
of the payload.**

🟢 **`p253` already set the rule and this is its next case class.** `p253` found *declaration without
publication, resolution landing correctly*. This is **two declarations, one publication, and the
publication belongs to the ungranted one** — resolution lands, and lands on the wrong grant.

> **`P482`.** A registry record corroborates a repo **only** when its `repository` / `Homepage` field
> resolves **back to that same slug**. Same package name is **not** identity. Where it does not resolve
> back, the repo has **one** channel, and the row says so.

### 🟢 Agents added this pass — 4 permissive, every one payload-verified

| Agent | Licence (payload) | Region | Why it earns a row |
|---|---|---|---|
| 🆕 [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** — `main/LICENSE`, 1,064 B | 🟢 **APAC** (Tsinghua University **MAIC** team, Beijing) | 🟢 **The headline agent find of this pass: a multi-agent *classroom*, not a tutor.** AI teachers **and AI classmates** that speak, draw on a shared whiteboard and hold real-time discussion; one-click generation of slides, quizzes, interactive simulations and project-based activities from any topic or document. **LangGraph 1.1** state-machine orchestration on **Next.js 16 / React 19 / TypeScript 5**. Provider-plural by design — OpenAI, Azure OpenAI, Anthropic, Amazon Bedrock, Gemini, DeepSeek — plus **Lemonade** local inference and **FunASR** local ASR, so the whole classroom can run on-premise. Peer-reviewed (**JCST'26**, `10.1007/s11390-025-6000-0`), live demo `open.maic.chat`, **11 releases since 2026-03-26** with `v1.2.0-rc.1` on **2026-10-04** |
| 🆕 [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | 🟢 **MIT** — `main/LICENSE`, 1,067 B; `pyproject.toml` agrees | ⚠️ **Unplaced** — platform-bound, not jurisdiction-bound | 🟢 **The first Moodle MCP on these shelves that treats a live LMS as a hostile surface.** Ten tools over `moodledev.io` (BM25 + trigram-cosine rerank, synonym expansion, version filters), the Hooks API index, capability/`RISK_*` lookups, XMLDB search and the Moodle **Jira tracker** — then two tools against a *real* instance (`list_ws_functions`, `call_ws_function`) that are **SSRF-guarded, function-name allowlisted, and refuse private/loopback hosts unless explicitly overridden**. Ships MCP **resources**, 8 **prompts**, and `readOnlyHint` / `destructiveHint` **tool annotations** for client-side safety. 🔴 **Subject of `P482` — it does not own its PyPI name** |
| 🆕 [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) (**GradeMate**) | 🟢 **MIT** — `main/LICENSE`, 1,071 B | ⚠️ **Unplaced** — 🔵 **rubric-agnostic by design** (see `T1` in `intel/trends.md`) | 🟢 **The counter-example that sharpens pass 36's `T1`.** Teachers apply curated rubrics **or upload their own**, so the rubric is an **input at runtime** rather than an encoding in the repo. React frontend + **Django** backend as an API endpoint; Gemini via `GOOGLE_API_KEY`. 🔵 **Useful precisely because it is the opposite architecture to `bandup`/`MathTutor`** — and the two shapes sell differently |
| 🆕 [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) | 🟢 **MIT** — `main/LICENSE`, 1,071 B | ⚠️ **Unplaced** — no jurisdiction or locale binding in the tree | **Reference-tier, honestly labelled.** LangGraph orchestration with state management across tutorial → Q&A → knowledge-evaluation, SQLite conversation persistence, Streamlit **and** CLI surfaces, OpenRouter-backed. ⚠️ **Subject-agnostic "teach any topic"** — the breadth-first shape earlier passes shelved as commodity. Shelve as a **small clean LangGraph reference**, not a delivery base |

### 🟢 Also verified this pass — two copyleft platform agents, both commercially usable

🔵 **Both were the `P480` false positives, and both are real finds once classified correctly.**

| Repo | Licence (payload) | Note |
|---|---|---|
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🟢 **AGPL-3.0** — `main/LICENSE`, 34,522 B | Course/LMS platform positioned against Moodle, EdX, Thinkific and Teachable, **with an MCP server published as `@classroomio/mcp` on npm (🟢 MIT, v0.0.9 — second channel confirmed)**. ⚠️ **AGPL-3.0 on the platform**: network-use copyleft, so a hosted client deployment triggers source obligations. 🔵 **The MIT MCP layer and the AGPL core are two different licence conversations** — name both in any deck |
| [`lmscloud-io/moodle-mcp-server`](https://github.com/lmscloud-io/moodle-mcp-server) | 🟢 **GPL-3.0** — `main/LICENSE`, 35,148 B | Executes Moodle web services from an MCP client. ⚠️ GPL-3.0, so it is a **side-car**, not an in-product component |

### 🔴 Not usable / not resolved this pass — stated so the denominator closes

**10 candidates probed. 4 permissive · 2 copyleft-usable · 2 real-but-ungranted · 2 unresolved = 10.**

| Repo | Verdict |
|---|---|
| [`shrutika00/StudyMate`](https://github.com/shrutika00/StudyMate) | 🔴 **UNGRANTED** — real (`main/README.md` 200), **no licence payload at 16 names × 2 branches**. LangGraph + Gemini + RAG + SQLite adaptive tutor; **cannot be built on until a licence appears** |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🔴 **UNGRANTED** — real, no payload |
| [`Aditya7808/AI-Powered-Adaptive-Curriculum-…-Agent`](https://github.com/Aditya7808/AI-Powered-Adaptive-Curriculum-Assignment-Generator-Agent) · [`Aryan6238/EduAgent`](https://github.com/Aryan6238/EduAgent) | 🔴 **UNGRANTED** — both real, both no payload. 🔵 **Multi-agent curriculum/assignment generation with rubrics is an actively populated niche in which almost nothing is licensed** |
| [`EastArctica/canvas-mcp`](https://github.com/EastArctica/canvas-mcp) | 🔴 **NO-PAYLOAD** — nothing resolved on any existence filename; treat as **may not exist at this slug** |
| `slm-socratic-tutor-ptbr` (Brazilian-Portuguese Socratic tutor benchmark, 8 open SLMs ≤3.8B, offline) | 🔴 **Unresolved — named in secondary prose, no owner slug recoverable.** 🔵 **Recorded as an unverified lead, not a finding** — it would have been this pass's LATAM placement and it is not one |

### 🔵 `P479` — "no star counts" was never a fact about GitHub. It is a fact about this session's repo scope

🔴 **Thirty-six passes recorded `api.github.com` → 403 as an environmental wall.** Measured this pass,
reading **bodies** and not only status codes:

| Probe | Result | What it proves |
|---|---|---|
| `api.github.com/rate_limit` | 🟢 **200** — `core` limit **15,000**, **used 0**, `graphql` 10,000 | 🔴 **Not a rate limit, and not a blocked host.** The quota is intact and untouched |
| `api.github.com/repos/sakaiproject/sakai` | 🔴 **403** | 🔴 **Body is the session proxy's own text**: *"GitHub access to this repository is not enabled for this session. Use `add_repo` to request access."* — **not** a GitHub error |
| `api.github.com/repos/gmilano/education-kb` (attached) | 🟢 **200**, full JSON **including `stargazers_count`** | 🟢 **The endpoint class works. The gate is per-repository authorization** |
| `add_repo(rubelw/OSSS, access:"read")` | 🟢 served, 🔴 **"Nothing was attached … GitHub API tools do not cover unattached repositories"** | 🔴 **The documented remedy does not open the API.** Only `access:"push"` attaches with credentials, and that is not appropriate for third-party repos |

> **`P479`.** `403` is a statement about **authorization**, not about **availability**. A census that
> records a status code without reading the body cannot tell a blocked host from a **gated** one, and
> this one has been reporting the wrong layer for thirty-six passes.

🟢 **The operational consequence is narrow and should be stated narrowly: star counts remain
unavailable for third-party repos here**, so this shelf's no-stars discipline **stands unchanged**.
🔵 **What changes is the reason, and the reason is what a deliverable repeats.** Any Globant artefact
saying *"the GitHub API is blocked"* is wrong; the accurate sentence is *"this session is scoped to
named repositories, and popularity metrics are therefore out of scope by construction."*

🆕 **Channel census, re-measured 2026-10-07:**

| Channel | This pass | Note |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 **200** on payload paths | the licence route, unchanged |
| `pypi.org` · `registry.npmjs.org` | 🟢 **200** | both used this pass (`P482`; `@classroomio/mcp`) |
| 🆕 `repo.maven.apache.org` | 🟢 **200** — `org/sakaiproject/` and `org/olat/` both resolve | 🆕 **Newly measured. The second channel the Java LMS tier has been missing** — Sakai, OpenOLAT and Opencast publish POMs whose `<licenses>` block is a manifest-layer cross-check (`p289`, `p294`) |
| `search.maven.org` | 🔴 **403** | the Solr search API is blocked; **browse by groupId path instead** |
| `gitlab.com` | 🟡 **301** | reachable, not yet exercised for payloads |
| `api.github.com` | 🟡 **200 host / 403 per unattached repo** | `P479` — gated, not blocked |
| `github.com` | 🔴 **403** | no HTML, no stars |
| `huggingface.co` · `arxiv.org` · `aclanthology.org` · `eur-lex.europa.eu` · `codeberg.org` | 🔴 **000** (CONNECT tunnel refused) | 🔴 **No model-weights licence, no paper and no Official Journal text is first-hand verifiable here.** The `JCST'26` DOI for `OpenMAIC` and every regulatory date in `intel/` are **secondary** |

### 🔵 `P481` — the finding numbers are a global sequence, and this pass collided with it

🔴 **This pass first published its fixture-coverage finding as `P477`. That number was already taken**
— by an earlier pass, defining *"never divide a figure from one market series by a figure from
another"*, cited live at `intel/market.md:248` and `intel/trends.md:228`. 🟢 **Renumbered to `P480`
inside this pass; the legacy `P477` text was left untouched.**

🔴 **And the collision happened twice, which is the part worth recording.** `P482` below was first
published as **`P478`** — also taken by pass 36, for *AITutor-EvalKit*'s licence claim, defined at
`compose/patterns.md:203` and cited at `intel/trends.md:166`.

🔴 **The measured cause of the second collision was the check itself, not the lookup.** The ceiling
sweep was run as `grep -rn '\bP478\b' --include=*.md . | grep -v … | head -3`, and 🔴 **`head -3` cut
the output after three `agents/top.md` hits — the pass's own new lines — before it ever reached
`compose/patterns.md`.** 🔵 **The number looked free because the evidence that it was taken was
truncated by the pipeline measuring it**, which is `P471`'s shape yet again: an instrument that
returned a confident answer about a region it never examined.

🔵 **The numbers are global across every file**, but a pass works in one file's newest section and the
natural check — *"is this number in the section I'm writing?"* — returns the wrong answer. 🟢 **Real
ceiling for this pass, measured without truncation: `P479` was the first genuinely free number**; the
repository's commit history claims `P473`–`P478`.

⚠️ **Two dangling citations surfaced while measuring the ceiling**, and they are logged rather than
fixed: **`P593`** and **`P679`** are cited in `compose/code/p357-hint-layer-cession/README.md` and
**defined nowhere** in `intel/`, `agents/` or `repos/`. 🔵 **`compose/code/pattern-citation-audit/` is
the instrument that exists for exactly this** — a cited-but-undefined number — and it is not catching
these two.

> **`P481`.** Before defining a finding, take the ceiling from **the whole tree**, not from the file
> being written: `grep -rhoE '\bP[0-9]+\b'` over every `.md` **and** `git log --format='%B'`, with
> 🔴 **no `head`, no `| head -n`, and no filter that can hide a hit in a file you have not read** —
> then verify the chosen number has no existing **definition** line. 🔴 **A duplicate definition is
> worse than a gap**: it makes every prior citation of that number ambiguous, retroactively. 🔵 **And
> truncating the check is how the number looks free.**

## 🔴 Thirty-sixth pass, 2026-10-07 — the probe that found the agents misread one of their licences

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, branch- and case-aware (16 filenames × `main` **and** `master`), then **re-classified
through this KB's shared classifier** `compose/code/lib/license_family.sh`. **No star counts.**

🔵 **Channel census, re-measured this pass.** `api.github.com` → **403**, `github.com` → **403**,
`huggingface.co` → **000**, `arxiv.org` → **000**, `aclanthology.org` → **000**. 🟢 **Two channels are
open and both were used: `raw.githubusercontent.com` (200) and `pypi.org` (200).** 🆕
**`registry.npmjs.org` → 200, newly measured and not previously recorded as reachable here** — a
second-channel route for the JS/PHP tier that future passes should use.

### 🔴 `P473` — the discovery probe said "GRANTED" about a licence that forbids commercial use

This pass wrote a fresh probe to sweep candidates, because sweeping is what a discovery pass does. It
reported `CRSS-AI/agentic-se-course-early-2026` as **`GRANTED … UNKNOWN`** on a 822-byte `main/LICENSE`.
🔴 **The payload is Creative Commons Attribution-**NonCommercial**-4.0.** Read verbatim:
*"NonCommercial — You may not use the material for commercial purposes."*

| Classifier | Family | Commercial use |
|---|---|---|
| This pass's ad-hoc probe | `UNKNOWN` | — **not asked** |
| 🟢 `compose/code/lib/license_family.sh` (shared, hardened) | 🟢 **`CC-BY-NC-4.0`** | 🔴 **`PROHIBIDO`** |

🟢 **The control was already correct and already in the tree.** Sourcing it returns the right answer on
the first call — it was never run, because the probe was new code. 🔴 **`P250` is explicit that
`UNKNOWN` is indistinguishable from "commercial use is PROHIBITED", which are opposite answers to the
only question this KB exists to answer**, and `P237` is explicit that a classifier written from scratch
reintroduces defects the shared one already paid for. **Pass 36 proved both at the discovery stage
rather than the instrument stage** — a layer neither finding had been tested on, because `P237`/`P250`
hardened the *shelf* instruments and said nothing about the throwaway script that feeds them.

> **`P473`.** A discovery probe is a shelf instrument. It must emit the **commercial-use column** from
> the shared classifier, or its `GRANTED` rows are **not shelf-ready** and must not be written as
> findings. "Has a `LICENSE` file" is a statement about a filename, not about a grant.

🔵 **And this is where it bites hardest in *this* industry, which is why it surfaced here and not in
gaming or financial.** Education KBs shelve **curricula, lesson plans, item banks and courseware**, not
only code — and **the OER tier is where `CC BY-NC` actually lives**. A Creative Commons NC licence sits
at `LICENSE` in the ordinary place, at an ordinary size, and is **invisible to a filename-based probe**.
Every pass that widens this KB toward courseware raises the prior on meeting one. 🔵 **The shelf already
had the right shape for it: `P250`'s two-column rule (family *and* commercial use) is what makes an NC
row representable at all.**

### 🟢 Agents added this pass — 5 granted, each placed in a region

| Agent | Licence (payload → shared classifier) | Region | What it is |
|---|---|---|---|
| [`rubelw/OSSS`](https://github.com/rubelw/OSSS) | 🟢 **Apache-2.0** — `main/LICENSE`, **11,363 B** → `Apache-2.0` / commercial **OK**. **Three channels**: 🟢 `pyproject.toml` `license = { text = "Apache-2.0" }`; 🟢 **PyPI `open-schools`** → `License :: OSI Approved :: Apache Software License`, `repository` resolving back to this repo | 🟢 **North America** | 🆕 **Open Source School Software — a K-12 SIS with the agent tier inside the tree.** FastAPI + Keycloak SSO + SQLAlchemy + PostgreSQL, Next.js front end, polyglot monorepo; **Ollama + MetaGPT + A2A** named in the architecture. Covers governance, student info, accounting, activities and **transportation**. ⚠️ **Self-declared "active development"** — README, 7 Nov 2026: *"working to on step machine and logic for workflows, gates, boundaries"*. **Pilot-tier, not production-tier** |
| [`BaijayantaRoy/bandup`](https://github.com/BaijayantaRoy/bandup) | 🟢 **MIT** — `main/LICENSE`, **1,071 B** → `MIT` / **OK**. 🟢 README badge agrees; 🔴 PyPI `bandup` **404** (not published) | 🟢 **APAC** | 🆕 **Rubric-bound marking for named Singapore papers.** PSLE composition (Content /20 + Language /20 = **/40**) and A-Level General Paper (Content /30 + Language /20 = **/50**); O-Level /30 declared as coming. **Local-first by default via Ollama**, no account and no telemetry, with a **persistent on-screen warning the moment a non-local model is selected**. Handwriting/OCR as a **separately chosen** model (phone photos, scans, multi-page PDF, transcribed verbatim with mistakes preserved). Tracked-changes word-level diff, per-error explanations, next-band rewrite from the pupil's own words. English + **Hindi** with script detection. ⚠️ **Bands are explicitly unofficial**, SEAB/Cambridge-*style* descriptors |
| [`dikshant182004/MathTutor`](https://github.com/dikshant182004/MathTutor) | 🟢 **MIT** — `master/LICENSE`, **1,068 B** → `MIT` / **OK** | 🟢 **APAC** | 🆕 **A JEE (India) maths tutor that is a reference architecture, not a prompt.** **14-node LangGraph** pipeline: intent routing → ReAct tool loop → **a dedicated critic agent that verifies its own answer** → explanation generation. **Episodic + semantic + procedural long-term memory in Redis**, tracking which topics a student struggles with and which strategies work for them across sessions. **Hybrid CRAG retrieval: BM25 + Cohere dense + reciprocal rank fusion.** SymPy calculator, Tavily MCP web search, FAISS RAG. Text / image (OCR) / audio (ASR) input. 🔵 **The self-verification and memory layers are the transferable parts** |
| [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | 🟢 **MIT** — `main/LICENSE`, **1,065 B** → `MIT` / **OK**; © **Fab Data** | 🟢 **EMEA** | 🆕 **Sierra Leone's national lesson plans turned into structured data.** Parses the **MBSSE** (Ministry of Basic and Senior Secondary Education) Maths and Language Arts lesson-plan PDFs — **all grades across Primary, JSS and SSS** — into structured JSON, then cleans the text for human consumption. 🟢 **Ships the corpus, not just the code**: raw input plus parsed and cleaned outputs as public `.json.gz`. 🔵 **Most steps are rule-based; LLMs are used only for the cleaning pass** — the cheap, auditable division of labour |
| [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT** — `main/LICENSE.md`, **1,067 B** → `MIT` / **OK** | 🟢 **LATAM** | 🆕 **The evaluation suite behind the Open Portuguese LLM Leaderboard.** Fork of EleutherAI's `lm-evaluation-harness` adapted for Portuguese, backed by **CEIA at the Federal University of Goiás (UFG), Brazil**. Portuguese task suite; **direct-response** evaluation (not log-probs only) so instruction-tuned chat models are measurable; automatic chat-template detection; **vLLM** and **LiteLLM** backends; F1-macro and Pearson to match each benchmark's original metric; reasoning extraction; UTF-8/accent handling. 🔵 **This is how a Portuguese-language tutor deployment justifies its model choice with evidence instead of vendor claims** |

🔴 **Not added — and the row exists so no later pass promotes it off its name:**
[`CRSS-AI/agentic-se-course-early-2026`](https://github.com/CRSS-AI/agentic-se-course-early-2026) —
**`CC-BY-NC-4.0`, commercial use `PROHIBIDO`** (`P473`). A 5-session inverse-classroom agentic-SE
curriculum; **readable, teachable, and unusable as a Globant delivery base.**

### 🔴 Ungranted this pass — 4 of 10, each real and each named

[`AI-for-Education/fabdata-llm-retrieval`](https://github.com/AI-for-Education/fabdata-llm-retrieval)
(exists via `main/README.md` — 🔵 **an end-to-end RAG platform from an org whose other seven repos this
KB already shelves, and it carries no licence payload**) ·
[`shakyanaitik0-bot/Agentic_AI_Tutor`](https://github.com/shakyanaitik0-bot/Agentic_AI_Tutor)
(`main/README.md`) ·
[`DeaY01/Essay-Marker-Bot`](https://github.com/DeaY01/Essay-Marker-Bot) (`main/README.md`) ·
[`ZeydSaeed/SIS`](https://github.com/ZeydSaeed/SIS) (`main/package.json`).

**Census closes: 5 granted + 1 granted-but-NonCommercial + 4 ungranted = 10 real repositories probed.**
Negative control in the same run, `totally-fake-org-zzz9/nope-repo-abc` → **no licence payload *and*
unresolved on all existence filenames**, correctly separated from the 4 ungranted-but-real rows.

### 🔴 `P474` — place a region from the artifact's domain model, never from the maintainer's name

`rubelw/OSSS` is tagged 🟢 **North America** above. 🔴 **The tempting evidence was the maintainer's
name in `pyproject.toml`, and that evidence is inadmissible** — a name is not a nationality, and this
KB's own frontmatter rule says the region is a closed-vocabulary *field* with the country in prose.

🟢 **What places it is the data model.** OSSS encodes **school districts** as the top-level tenant, with
**district transportation**, **district accounting**, and **board governance** as first-class modules.
That is the **US district structure**, not a generic school model: an EMEA or APAC deployment does not
have a yellow-bus transportation department or an elected district board to govern. 🔵 **The schema is
payload; the surname is not.**

> **`P474`.** Place a region on **what the artifact models or states it serves** — a named national
> curriculum (`lesson-plan-parse-mbsse` → Sierra Leone), a named national exam (`bandup` → PSLE/A-Level
> GP; `MathTutor` → JEE), a named institution (`lm-evaluation-harness-pt` → UFG), or an encoded
> administrative structure (`OSSS` → US districts). **Never on maintainer identity.** When nothing in
> the payload places it, **leave it unplaced and say so** — this KB has done exactly that for
> `Eloom-LMS-International` and that row is honest.

🔵 **Why this pass is unusually well placed: 5 of 5 granted rows carry a region, and four different
placement grounds are represented.** Contrast the standing problem that a finding with no region
attached is worth less than one that is placed.

### 🔴 `P478` — this pass reproduced the false MIT claim a fifth time, in a recipe, having just written the rule against it

🔴 **`P476` was written earlier in this same pass: "a secondary source's licence string never overwrites a
payload-verified shelf; order of precedence is payload > shelf > secondary prose." Then this pass drafted
`P47` in `compose/patterns.md` with `kaushal0494/AITutor-EvalKit` labelled 🟢 MIT — on the authority of a
search summary, with no probe.**

| Channel | Says |
|---|---|
| 🔴 Search summary (the source actually used) | *"available at MIT-licensed python repository"* |
| 🔴 Its EACL 2026 demo paper | *"released under an MIT license"* |
| 🟢 **Payload, probed this pass, 19 filenames × `main`/`master`** | 🔴 **`UNGRANTED` — no licence payload.** Repo exists (`main/README.md`) |
| 🟢 **This KB's own `agents/top.md:518`** | 🔴 **"Fourth reproduction of the false claim … The paper says MIT; the repo does not. The correction holds."** |

🔴 **So the shelf had already caught this four times, named it a recurring false claim, and the fifth
reproduction came from the pass that wrote the precedence rule.** It would have shipped a **recipe whose
CI gate was an unlicensed dependency** — the error class with the worst blast radius here, because a
pattern is *instructions to build something*, and a mislabelled licence inside one propagates into client
deliverables rather than sitting on a shelf.

🔵 **Why the rule did not protect the recipe, and this is the generalisable part.** `P473` put the
commercial-use gate in the path of **discovery** — the sweep that finds *new* repos. 🔴 **`AITutor-EvalKit`
is not a new repo. It was already shelved, so it entered `P47` by *recall*, and nothing gates recall.**
The probe ran on 10 candidates and on none of the four already-known repos the recipe composed.

> **`P478`.** A repo cited in a **compose pattern** is a dependency of a client build, so it is gated like
> one **whether or not this pass discovered it**. Re-probe every component of every recipe at write time;
> **a licence is a fact about today, not a property the shelf owns forever.** `P473`'s gate belongs in the
> recipe path, not only the discovery path — 🟢 **and `compose/code/p473-probe-commercial-gate/` is now
> cited as step 0 of both recipes for exactly this reason.**

🟢 **What the correction produced is a better recipe than the wrong one was.** The fix is not a relabel:
`P47`'s quality gate is now **MIT-verified `AI-for-Education/pedagogy-benchmark`** (payload **1,064 B**,
re-read this pass) plus the four dimensions **reimplemented from the published paper as a
specification** — because a scoring rubric described in a paper is an idea, while the repository is code
you may not vendor. 🔵 **And it makes this KB's standing gap honest where the draft had silently
"closed" it: "no shippable permissive evaluator of tutoring quality" is STILL OPEN**, and the subfield is
unlicensed as a whole — `AITutor-EvalKit` no payload, `eth-lre/mathtutorbench` self-contradictory inside
one README, `UnifyingAITutorEvaluation` silent, Open TutorAI **CC BY-NC-SA 4.0**. 🔴 **A recipe that
pretends a gap is closed is worse than one that names it and budgets for it** — `P47` now budgets ~2 of
its 11 weeks for building the evaluator.

### ⚠️ `P475` — the existence probe was case-aware on licences and careless on everything else

`dikshant182004/MathTutor` resolved its licence at **`master/LICENSE`** immediately. Its README then
returned **404 on `README.md` and `readme.md` × both branches**. 🔴 **The file is
`master/Readme.md`** — capital `R`, lowercase `e`. Had the licence not been found first, the repo would
have been logged **`NOPAYLOAD` — "unresolved on all existence filenames"**, the same verdict the
negative control earns. 🔵 **A fabricated repository and a real one with an unusual capitalisation would
have been reported identically.**

> **`P475`.** Asymmetric rigor is a defect, not a saving. This probe tried **16 licence filenames × 2
> branches** and only **3 README spellings**. The existence check decides whether a repo is **real**;
> it deserves at least the case-variation the licence check gets. Minimum: `README.md`, `readme.md`,
> `Readme.md`, `README.rst`, `README.txt`, `README`.

## 🔴 Thirty-fifth pass, 2026-10-07 — a three-pass-old gap claim that this KB's own shelves disprove

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, branch- and case-aware (12–19 filenames × `main` **and** `master`), **cross-checked
against the registry the project publishes to** where one exists. **No star counts.**

🔵 **Star counts, inherited not re-derived (`P465` discipline).** `api.github.com` → **403** and
`github.com` → **403**, re-measured this pass. The GitHub MCP route an earlier pass used stays
outside this session's repository scope (`gmilano/globant-kb`, `gmilano/education-kb`). **"Not read
this pass" means genuinely unobtainable here, not skipped.**

### 🔴 `P469` — the EMEA permissive gap was never a gap. It was a shelf-membership check reported as an industry finding

`repos/foundations.md` has asserted for **three consecutive passes** (`P467` and its two
predecessors) that this KB can find **"no EMEA-origin permissive education foundation."** 🔴 **That
claim is false, and the disproof was already inside this repository the whole time.** Both rows
below were re-read from payload **this pass**:

| Counter-evidence | Licence (payload, 2026-10-07) | Second channel | EMEA origin | Already on which shelf |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`master/LICENSE`, **10,982 B**, verbatim Apache preamble) | 🟢 `master/pom.xml` `<licenses>` → `Apache 2.0 Open Source L6icense` + `apache.org/licenses/LICENSE-2.0` | 🟢 **Switzerland** — OLAT originated at the **University of Zurich**; maintained by **frentix GmbH**. `README` and `pom` both resolve to `openolat.org` / `openolat.com` | `repos/trending.md:1349`, `:2617`; `verticals/solutions.md`; `agents/top.md:3118` |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (`master/LICENSE.txt`, **2,058 B**, *"distributed under the 3-clause BSD license… This license is famously liberal"*) | — not published to a registry | 🟢 **United Kingdom** — QTI 2.1 delivery engine + **JQTI+** + **MathAssess**, University of Edinburgh | `agents/trending.md:9124`, where it is **already tagged `🟢 EMEA`** |

🔴 **`repos/trending.md:2617` calls OpenOLAT "the most permissive full LMS in this KB" — on the same
shelf-set where `repos/foundations.md` says no such asset exists.** A single `grep -ri openolat`
surfaces both in under a second.

🔴 **A second claim falls with it.** `P467` states the Dutch GPL-3.0
[`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment) is *"the
first EMEA-origin higher-education assessment framework on any shelf here."* **`qtiworks` — Edinburgh,
BSD-3-Clause, a higher-education assessment engine — precedes it on this KB's own shelf.** The phrase
*"on any shelf here"* is what makes this an error rather than a scoping choice.

🔵 **Root cause, and it is not carelessness.** The gap was true *of `repos/foundations.md`* —
OpenOLAT lives on the verticals and trending shelves and was never promoted to foundations. The
defect is the **restatement**: a shelf-local absence was rewritten as a claim about what this
instrument could *find*, and `P467` then spent a pass hardening the wrong claim with nine forge
probes. **The forge probes are sound and remain valid; the conclusion they were attached to is not.**

🟢 **Fixed this pass, not just flagged:** both repositories are promoted to `repos/foundations.md`
with payload evidence, and the EMEA-gap language is withdrawn there.

🔵 **Transferable rule — `P469`.** *A gap claim is an assertion about every shelf, so it must be
tested with a cross-shelf `grep` before it is written, and it must name the shelf it was measured on.*
The cost of skipping that grep here was three passes of telling a reader that an Apache-2.0 Swiss LMS
and a BSD-3 Edinburgh assessment engine did not exist, in a file sitting beside the rows that record
them.

### 🔴 `P471` — and the check already existed. It passed 27/27 while judging nothing

🔴 **The uncomfortable part of `P469`: this KB had already built the instrument.**
`compose/code/p370-gap-gate/` exists precisely to falsify a declared gap against the KB's own index,
its suite passes **27/27**, and the pass that introduced it caught exactly this class of error
(a four-pass *"CERO repositorios de origen LATAM"* claim against 12 placed LATAM rows).

Swept against the live tree this pass, it reports **5 gap sentences with a region → 0 CONTRADICHOS,
all 5 `NO-CLAIM` / `SIN-ALCANCE`**. 🔵 **Not because the KB stopped declaring gaps — `P467` is right
there — but because the KB started writing them in English, and two independent filters in the gate
are Spanish-only.** Measured on the verbatim `P467` sentence:

| | Result |
|---|---|
| `GAP_SENTENCE` (the `--sweep` extractor: `hueco`, `cero repositorios`, `sigue abierta`) | 🔴 **extracts nothing** — the sentence is never even presented for judgement |
| `INDEX_MARKERS` / `CHANNEL_MARKERS` (the scope classifier) | 🔴 `SIN-ALCANCE` → verdict **`NO-CLAIM`** |
| `region_in_prose` | 🟢 **`EMEA`, correctly** — the region names are identical in both languages |
| Rows in the tree naming EMEA beside a GitHub URL | 🟢 **94**, of which **77 placed** |

🔴 **So the gate resolved which region the claim was about, had 94 candidate contradictions on the
shelf, and still declined to judge it.** With English markers added, the same sentence returns
**`CONTRADICHO`, scope `INDICE`, 94 rows**; and the channel-scoped wording of the *same* gap still
returns **`SOSTENIDO`**, which is the control proving this is an extension of the gate and not a
counter of the word "no".

🔵 **The real lesson, and it is sharper than `P469`'s: `NO-CLAIM` must not be the same verdict as
"unparseable."** The gate gave a claim it could not read the identical verdict it gives prose that is
not a claim — so the sweep read as *"nothing to judge."* **A passing suite measures the cases you
wrote, never the class you stopped writing**, and the only visible symptom was a denominator falling
from **29 to 5** with nothing reporting it.

🟢 **Instrument shipped this pass:** `compose/code/p471-gap-gate-language/` — **25/25**, nesting the
gate's own 27/27 — measures that gate's coverage over a corpus, ships `MARKERS_EN` as the patch, and
found **12 language-blind gap claims among 58**, including a second false English index claim nobody
had flagged: *"…rested on **no LATAM-origin permissive education project**."* Recipe: `P45` in
`compose/patterns.md`.

### 🔴 `P472` — and then the fixed gate failed the build 11 times, all 11 wrong

Running the repaired gate over this tree produced **11 `CONTRADICHO` index-scoped claims and not one
of them was a live assertion**: **9** are **quotations** and **2** are narrowed by a **maturity
qualifier**.

🔴 **The quotation class is the one that matters, because it is caused by doing the right thing.**
The correct way to retract a false gap is to **quote it in the retraction** — `repos/foundations.md`
now carries `> **Superseded text:** *"no EMEA-origin permissive education foundation."*` — so **a
naive gate fires forever on a corpus that has already been fixed**, and an instrument that punishes
the fix teaches people to fix things quietly.

🔵 **The qualifier class is the honesty check.** *"No LATAM-origin permissive education product **at
production maturity**"* is a claim about **maturity**, not existence. Placed rows prove assets exist
and say nothing about whether any is production-grade — **so the gate must not refute a claim
quantified on a dimension it never measured.**

🟢 **Fixed, with tests:** `assertion_class()` → `QUOTED` / `QUALIFIED` / `ASSERTED`, and
`build_verdict()` fails only on `INDICE` + `CONTRADICHO` + `ASSERTED`. Quotation wins over qualifier.
On this tree: **0 build failures**, `CONTRADICHO-but-QUOTED=9`, `CONTRADICHO-but-QUALIFIED=2`.

🔵 **`P471` and `P472` are the same defect at two levels: `P471` is "the gate could not *read* the
claim"; `P472` is "the gate could not tell *what the sentence was doing*." A contradiction detector
needs a speech-act classifier in front of it** — asserting X, quoting X, and asserting X under a
qualifier are three different acts and only the first is refutable by the corpus.

### 🟢 New verified rows this pass

| Agent / repo | Licence (payload) | Cross-channel | What it does | Region |
|---|---|---|---|---|
| [`eloompty/Eloom-LMS-International`](https://github.com/eloompty/Eloom-LMS-International) | 🟢 **MIT** (`main/LICENSE`, **1,062 B**) | 🟢 `README` MIT badge agrees; 🔴 not on Packagist | Laravel **13** LMS covering the **full student lifecycle** — agent-sourced application → offer letter → enrolment → intake scheduling → attendance → assessment → fees → certificates → alumni. **42 `nwidart/laravel-modules` modules**, **five web portals over one codebase**, token-authenticated REST API for mobile. 🟢 **An MIT full LMS is genuinely rare** — this industry's platform tier is overwhelmingly copyleft (Moodle GPL, Open edX AGPL, Chamilo GPL, ILIAS GPL, OpenEduCat LGPL). | ⚠️ **not determinable** — `README` states no country or governing body. Vocational/HE framing, no ASQA/Ofqual anchor. Recorded as unplaced rather than guessed. |
| [`AgenticAiLabs/Ai-Engineering-Roadmap`](https://github.com/AgenticAiLabs/Ai-Engineering-Roadmap) | 🟢 **MIT** (`main/LICENSE`, **1,067 B**) | — not on any registry | An **OSSU-style open curriculum** for self-taught AI engineering, explicitly modelled on [`ossu/computer-science`](https://github.com/ossu/computer-science): guided path, curriculum overview, learning philosophy, project structure. 🔵 Belongs to the **OER/curriculum tier**, not the agent tier — it is a structured reading path, not software that runs. | 🌍 Global |
| [`CodeWithJV/ai-tutor`](https://github.com/CodeWithJV/ai-tutor) | 🟢 **MIT** (`main/LICENSE`, **1,068 B**, © 2023 Joshua Vial) | — not on any registry | ⚠️ **Downgraded on reading it.** Search surfaced this as an AI tutor; the `README` is explicit that the repository *"provides you with a prompt"*, tested mainly on **GPT-3.5**. It is a **prompt artefact, not a tutoring system** — no code path, no retrieval, no assessment. Recorded at its true weight so a later pass does not promote it off its title. | 🌍 Global |

### 🔴 Repositories that exist and ship no licence grant at all

Probed with the same 12–19-filename × `main`/`master` sweep, then re-probed for **existence** so
"ungranted" is separated from "unresolved" (`P461`):

| Repo | Licence sweep | Existence control | Consequence |
|---|---|---|---|
| [`Jeremiah0067/Ai_Rubric`](https://github.com/Jeremiah0067/Ai_Rubric) | 🔴 **no payload**, both branches | 🟢 **exists** — `main/package.json` → 200 | Handwritten-answer capture → marking guide → AI-suggested grade with teacher override. **Unusable for a client deliverable without an upstream grant.** |
| [`OpenLLM-Europe/European-OpenLLM-Projects`](https://github.com/OpenLLM-Europe/European-OpenLLM-Projects) | 🔴 **no payload**, both branches | 🟢 **exists** — `main/README.md` → 200 | 🔵 **Painful one.** A curated catalogue of European open-source LLM projects for **medium- and low-resource European languages** — exactly the EMEA discovery channel this KB has been missing, and it carries **no licence on its own content**. Usable as a **lead source**, never as a redistributable asset. |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 **no payload** — 19 filenames × `main`/`master`, incl. `LICENSE.TXT`, `gpl.txt`, `COPYING.txt` | 🟢 **exists** — `master/README.md` → 200 | See `P470` below. |

### 🔴 `P470` — a listicle's licence claim is not a licence, and this one survived three channels of checking as unverifiable

Secondary sources this pass state plainly that **Forma LMS** (the Italian fork of Docebo from before
Docebo went commercial) is **Apache-2.0**, and recommend it *specifically* for teams that need
permissive licensing. This KB cannot confirm that from any channel it has:

| Channel | Result |
|---|---|
| Payload — 19 licence filenames × `main` + `master` | 🔴 **nothing** |
| `packagist.org/packages/formalms/formalms.json` | 🔴 **404** — not published |
| `master/composer.json` | 🔴 **absent / unparseable** |

⚠️ **So Forma LMS is recorded as `licence unverified`, not as Apache-2.0** — even though a
recommendation article asserts the permissive licence as its headline reason to choose it. 🔵 **This
is the sharpest form of `P468`: the failure mode is not a missing licence but a *confidently stated*
one with nothing behind it.** A client-facing dependency manifest that copied that listicle would
have shipped an unverifiable permissive claim about a platform tier.

### 🔵 Rejected this pass — licence clean, wrong industry

[`WhenWen/AC2`](https://github.com/WhenWen/AC2) — 🟢 **Apache-2.0** (`main/LICENSE`, 11,358 B), and
**not an education asset**. It is Stanford's *Trust the Critic More* actor-critic-with-action-chunking
RL method for language models (`arxiv.org/abs/2609.39247`), benchmarked on **IMO-ProofBench**. It
surfaced in a rubric/grading search purely on the word "grading". 🔵 **Recorded as a rejection rather
than dropped silently**, because the IMO-ProofBench association makes it exactly the row a later pass
would mistake for a maths-tutoring asset.

### 🟢 Channel census, pass 35 — cumulative instrument record

Per `P465`, this **inherits** the full census and marks what pass 35 re-measured; it does not
redefine the census as the subset probed today.

| Channel | Pass-35 result | Role |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 **200** | **Channel A — payload.** The primary licence evidence |
| `api.github.com` | 🔴 **403** | no stars, no metadata |
| `github.com` (HTML) | 🔴 **403** | no scraping fallback |
| `pypi.org/pypi/{pkg}/json` | 🟢 **200** | re-read `canvasapi` → **MIT + OSI MIT classifier**; `kolibri` → **MIT + OSI MIT classifier** |
| `registry.npmjs.org` | 🟢 **200** | LTI/JS tier |
| `packagist.org` | 🟢 **200** | PHP tier — and the channel that **404**s on `formalms` (`P470`) |
| `repo1.maven.org/maven2` | 🟢 **200** | 🔵 **still structurally unused, but no longer idle**: OpenOLAT's licence was cross-checked via its `pom.xml` **through `raw`**, which is the same declaration Maven would serve |
| `huggingface.co/api` | 🔴 **000** | **no model-weights licence is verified anywhere in this KB** |
| `eur-lex.europa.eu` | 🔴 **000** | **every AI Act date in `intel/` is secondary-sourced** |
| `codeberg.org`, `joinup.ec.europa.eu` | 🔴 **000** | EU public-sector forges (`P467`'s probes stand) |
| `gitlab.com` | 🟢 **301** (reachable, redirect) | the second host that confirmed OpenOLAT |
| 🆕 `crates.io/api/v1/crates/{crate}` | 🔴 **403** | 🆕 **first measured this pass.** The Rust registry is **closed** here — so `raif-s-naffah/xapi-rs` and any future Rust row stays **payload-only**. Recorded so no later pass counts Rust as an available second channel |

## 🟢 Thirty-fourth pass, 2026-10-07 — the census in the freshest layer contradicts itself, and the Canvas client was never on the shelf

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, branch- and case-aware (13 filenames × `main` and `master`), **and cross-checked
against the registry the project publishes to** where one exists. **No star counts.**

🔵 **On star counts, stated once so later passes stop re-deriving it.** `api.github.com` is **403**,
as every pass records. An earlier pass obtained counts through the session's **GitHub MCP server** —
that route is **not available to this pass**: this session's GitHub scope is restricted to
`gmilano/globant-kb` and `gmilano/education-kb`, and reaching third-party repositories through
account-wide search tools is outside it. 🔵 **So "not read this pass" below means genuinely
unobtainable here, not skipped.**

### 🔴 `P465` — the pass-33 channel census says `raw` is "the only licence channel", and its own next row disproves it

In `agents/trending.md`, the thirty-third pass's six-channel census contains these two rows, four
lines apart, in the same table:

| Channel | Result | Note (verbatim) |
|---|---|---|
| `raw.githubusercontent.com` | **200** | *"**the only licence channel**"* |
| `pypi.org` | **200** | *"still open, as pass 41 used it for `edx-proctoring`"* |

🔴 **Both cannot be true.** And the error is not confined to that table: **"six channels"** and
*"`raw.githubusercontent.com`, the only licence channel"* were carried into the pass-33 headers of
**`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` and `compose/patterns.md`** —
four shelves telling the reader the instrument is narrower than this KB's own earlier passes proved.

⚠️ **This is not a discovery of new channels.** Earlier passes used `pypi.org`, `registry.npmjs.org`,
`packagist.org` and `repo1.maven.org` extensively, and verified that they discriminate. **The defect
is that the freshest layer forgot them** — the exact failure pass 33 itself named in its T2 trend,
*"the freshest layer of a knowledge base is where stale claims live"*, committed in the same pass
that named it. 🔵 **Rule: a census is a cumulative instrument record, not a re-derivation from
whatever this pass happened to probe.**

### 🔵 Channel census, consolidated — 20 channels, measured this pass with both HEAD and GET

| Channel | HEAD | GET | Usable for | Status |
|---|---|---|---|---|
| `raw.githubusercontent.com` | **200** | **200** | licence payload, README, manifests | 🟢 open — primary |
| `pypi.org/pypi/{pkg}/json` | **200** | **200** | `license_expression`, OSI classifier, release dates | 🟢 open |
| `registry.npmjs.org` | **200** | **200** | `license`, latest version + date | 🟢 open |
| `packagist.org/packages/{v}.json` | **200** | **200** | PHP licence — the Moodle tier | 🟢 open |
| `repo1.maven.org/maven2` | **200** | **200** | JVM tier | 🟢 open, **unused** |
| `gitlab.com` (raw) | **200** | **200** | payload off GitHub | 🟢 open |
| 🆕 `bitbucket.org` | **200** | **200** | payload off GitHub | 🟢 **open — never named in this KB before** |
| `github.com` landing | 403 | 403 | — | 🔴 blocked |
| `api.github.com` | 403 | 403 | star counts, topics | 🔴 blocked |
| `sourceforge.net` | 403 | 403 | — | 🔴 blocked |
| `crates.io` | 403 | 403 | — | 🔴 blocked |
| `github.com/.../archive/{sha}.zip`, `codeload.github.com` | 403 | 403 | **pinned source archives** | 🔴 blocked — see `P466` |
| `eur-lex.europa.eu` | 000 | 000 | primary legal text | 🔴 egress-blocked |
| `huggingface.co` | 000 | 000 | **model-weights licences** | 🔴 egress-blocked — oldest standing limit |
| `zenodo.org` | 000 | 000 | research artefact DOIs | 🔴 egress-blocked |
| `codeberg.org` | 000 | 000 | EU-hosted forge | 🔴 egress-blocked |
| `code.europa.eu` | 000 | 000 | European Commission forge | 🔴 egress-blocked |
| `gitlab.opencode.de` | 000 | 000 | German public-sector forge | 🔴 egress-blocked |
| 🆕 `forge.apps.education.fr` | 000 | 000 | **French Ministry of Education forge** | 🔴 **egress-blocked — first measured here** |
| 🆕 `invent.kde.org`, `salsa.debian.org`, `gitlab.gnome.org`, `framagit.org`, `git.fsfe.org` | 000 | 000 | EU-centred community forges | 🔴 egress-blocked |

🔵 **Discrimination re-confirmed before use:** `pypi.org` → **404** for a package that does not exist;
`gitlab.com` raw → **302 to sign-in** for a path that does not exist; `packagist.org` → **404** for
`chamilo/chamilo-lms`. They answer *no* when the answer is no.

### 🟢 Cross-channel licence audit — 10 existing shelf rows, 0 disagreements

Re-verification, not a new method. The point of running it is that a **zero** is only informative if
the test could have returned non-zero:

| Package | Registry declaration | This KB's payload verdict | Agreement |
|---|---|---|---|
| `kolibri` | MIT + OSI MIT classifier | MIT | 🟢 |
| `xblock` | Apache-2.0 | Apache-2.0 | 🟢 |
| `openedx-learning` | AGPL 3.0 + OSI AGPLv3+ | AGPL-3.0 | 🟢 |
| `edx-proctoring` | AGPL 3.0 + OSI AGPLv3+ | AGPL-3.0 | 🟢 |
| `nbgrader` | OSI BSD classifier | BSD-3-Clause | 🟢 |
| `otter-grader` | BSD-3-Clause | BSD-3-Clause | 🟢 |
| `frappe` | OSI MIT classifier | MIT | 🟢 |
| `deeptutor` | Apache-2.0 | Apache-2.0 (`HKUDS/DeepTutor`) | 🟢 |
| `ltijs` (npm) | Apache-2.0, v7.0.7 | Apache-2.0 | 🟢 |
| `moodle/moodle` (Packagist) | **`GPL-3.0-or-later`** | GPL-3.0 | 🟢 |

🆕 **One new row fell out of the audit:** `edx-opaque-keys` declares **`AGPL-3.0-only`** on PyPI — a
core Open edX key library, network-copyleft, **not previously recorded anywhere in this KB.** It
extends the Open edX asymmetry (`XBlock` Apache-2.0 against an AGPL platform tier) by one more brick.

### 🟢 Agents added this pass

| Agent | Repo | Licence (read from payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| Adaptive AI Tutor | [`soumics/adaptive-ai-tutor`](https://github.com/soumics/adaptive-ai-tutor) | 🟢 **MIT** (`main/LICENSE`, 1,070 B) | not obtainable | Global | Curriculum-grounded tutor: upload a PDF/Markdown syllabus and **the material's own structure becomes the topic graph** (PDF bookmarks → numbered headings → Markdown headings), with prerequisites taken from the material's explicit cross-references rather than guessed. Cited explanations, Socratic mode, generated practice graded against a rubric, **SM-2 spaced repetition**. Runs **fully local on Ollama**; cloud LLM optional. ⚠️ **The author states plainly it is a prototype with no measured learning outcomes** — a credibility signal, not a defect. 🔴 **See `P466`: licence-clean, not installable from this environment.** |
| genai-open-assessment | [`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment) | 🟡 **GPL-3.0** (`main/LICENSE`, 35,149 B) | not obtainable | **EMEA** | Rubric-driven automated grading of **open-ended** higher-education questions, built as a *constrained* assessor: fixed grading scale, explicit criteria, formative feedback, and **every prompt, criterion, input and output stored for review** so the human educator remains accountable. Apache + PHP + SQLite, one-command Docker start, role-separated UIs for teacher / assessor / admin / student. 🔵 **Netherlands-origin** (Dutch interface text, `@school.nl` seed accounts). 🟡 **GPL-3.0 — standalone or side-car, never embedded in a permissive deliverable.** |

### 🟡 A data asset, not an agent — recorded because L&D engagements keep asking for it

| Asset | Repo | Licence | What it is | The catch |
|---|---|---|---|---|
| Promptster AI-fluency rubric | [`promptster-ai/rubric`](https://github.com/promptster-ai/rubric) | 🟢 **MIT** (`main/LICENSE`, 1,067 B); npm `@promptster/rubric` **0.7.0** also MIT | A published rubric for grading **how an engineer drives an AI coding tool** — five dimensions, behavioural anchors, five tiers, each grounded in cited research. Ships as `src/rubric.json`. | 🔴 **Open rubric, closed calibration** — the repo says so outright: per-prompt criteria and **scoring weights are deliberately not published**. Adopt the vocabulary and anchors for a client AI-enablement scorecard (`P6`, `P10`); **it is not a scoring engine and cannot reproduce their result.** |

### 🔴 Rejected this pass — 8 of 15 candidates cannot enter a deliverable

Stated in full, because an unexplained absence looks identical to coverage:

| Repo | Probe result | Why it cannot enter |
|---|---|---|
| [`jadrianlg16/learning-tutor`](https://github.com/jadrianlg16/learning-tutor) | **no `LICENSE` payload** (13 filenames × `main`+`master`) | No grant. Genuinely interesting design — *a learner model the LLM is never allowed to edit* — still unusable. |
| [`samrathreddy/Tutor-multi-ai-agent`](https://github.com/samrathreddy/Tutor-multi-ai-agent) | **no `LICENSE` payload** | No grant. |
| [`omerbbbb/ai-graded-assessment-platform`](https://github.com/omerbbbb/ai-graded-assessment-platform) | **no `LICENSE` payload** | No grant, despite describing real assessment-day use. |
| [`spal740/GradeScribe`](https://github.com/spal740/GradeScribe) | **no `LICENSE` payload** | No grant. |
| [`natiworldclass/adaptive-tutor`](https://github.com/natiworldclass/adaptive-tutor) | **no `LICENSE` payload** | No grant. |
| [`RutujaDeshmukh29/Adaptive-AI`](https://github.com/RutujaDeshmukh29/Adaptive-AI) | **no `LICENSE` payload** | No grant. |
| [`Sujal-Shejwal/adaptive-ai-tutor`](https://github.com/Sujal-Shejwal/adaptive-ai-tutor) | **no `LICENSE` payload** | No grant. 🔴 **Name-collides exactly with the MIT `soumics/adaptive-ai-tutor` above — match on owner, never on repo name.** |
| [`parcheesime/rubric-agent`](https://github.com/parcheesime/rubric-agent) | 🟢 **Apache-2.0** (`main/LICENSE`, 11,357 B) | **Licence is fine; there is no implementation.** The README states the project "begins with research before implementation"; dependencies are `boto3` + `beautifulsoup4` + `requests` — a corpus collector. 🔵 **Watch, do not compose.** |

🔵 **7 of 15 shipped no grant at all.** That ratio is itself the finding: the long tail of education-
agent repositories surfaced by search is overwhelmingly ungranted, and any sweep that does not probe
the payload will recommend them.

### 🟢 Re-confirmations — three shelf rows re-read from payload, none moved

| Repo | Where read | Verdict |
|---|---|---|
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `main/LICENSE`, 1,065 B | 🟢 **MIT**, unchanged |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main/LICENSE`, 1,531 B | 🟢 **BSD-3-Clause**, unchanged — byte count still matches the body-text-no-title-line record from pass 32 |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `main/LICENSE`, 11,408 B | 🟢 **Apache-2.0**, unchanged — **and independently confirmed** by PyPI `deeptutor` → Apache-2.0 |

### 🔵 An install-name trap worth one line

The canonical Python LTI 1.3 library is [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3), **but the installable
distribution is `pylti1p3`** — dots are not legal where the repo name puts them. Both read **MIT**.
`pip install pylti1.3` fails. The shelf row carried the repo and not the install name.

### 🔴 `P466`–`P468`

- **`P466` — a licence-clean repo that cannot be installed here, and no manifest scan could catch it.**
  `soumics/adaptive-ai-tutor` is MIT and its RAG core `soumics/llm-rag-assistant` is **also MIT**
  (`main/LICENSE`, 1,070 B) — the closure is clean. But `requirements.txt` pins that core as a
  **GitHub archive zip at an exact commit**, and `github.com/.../archive/<sha>.zip` returns **403**
  here, as does `codeload.github.com`. 🔵 **Licence-resolvable and install-resolvable are different
  properties**, and this KB's dependency-closure tooling reads manifests without testing that pins
  resolve. The row stands with the limitation on it.
- **`P467` — the EMEA forge blind spot, re-measured and extended.** This KB already records Joinup/
  OSOR and Codeberg as unreachable. Re-measured this pass and **extended with three forges never
  named here**: `forge.apps.education.fr` (**French Ministry of Education**), `invent.kde.org` and
  `salsa.debian.org` — all **000**, alongside `code.europa.eu`, `gitlab.opencode.de`, `framagit.org`
  and `git.fsfe.org`. See `repos/foundations.md` for what this does and does not do to the EMEA gap.
- **`P468` — the registry channel's miss rate, with two fresh instances.** `crewai` publishes to PyPI
  with **no licence metadata at all** (empty `license`, no classifier); `chamilo/chamilo-lms` is
  **404 on Packagist** despite being a major PHP LMS on this shelf; **8 of 20** PyPI rows carried
  only a free-text string with no OSI classifier. 🔵 **A registry silence is not a licence finding.**

## 🔴 Thirty-third pass, 2026-10-07 — a declared gap was wrong, and the repo it rested on has been MIT all along

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07.** Channel census re-measured this pass, **six channels**: `curl -sI` on a github.com
landing page → **403**; `curl` **GET** on the same page → **403**; `api.github.com` → **403**;
`raw.githubusercontent.com` → **200**; 🆕 `eur-lex.europa.eu` → **000**; 🆕 `huggingface.co` → **000**.
So **no star counts were read this pass** and every `★` cell says so. Negative control
(`totally-fake-org-zzz9/nope-repo-abc`) returned **404** on both `main` and `master` in the same runs
that returned these 200s.

🔴 **The headline is a self-correction, not a discovery.** Pass 7 declared *"there is no permissive
open-source exam proctoring agent"* and ranked building one as this KB's **second-best build
opportunity**. The gap rested on a single repo's licence verdict. **That verdict was wrong.** The repo
is **MIT**, and a second permissive proctoring agent turned up in the same run. The gap and the
ranking derived from it are **withdrawn**.

### 🟢 Exam proctoring — the shelf the KB recorded as empty

| Agent | Repo | License (read from payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| Autonomous Exam Proctoring & Grading Agent | [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | 🟢 **MIT** (`master/LICENSE`, 1068 B, © 2026 Prem Biswal) | not read this pass | Global | 🔴 **Recorded in four places in this KB as "No `LICENSE` payload" / "NONE" / "Do not use". It is MIT.** Fully local proctoring + grading: OpenCV + MediaPipe face detection on-device, **22-dimension behavioural feature vector**, logistic regression and anomaly detection **implemented from scratch**, risk-decay and risk-fusion formulas, TF-IDF text scoring, SQLite storage. **Zero external AI APIs**; camera frames are processed and discarded. Explainable by construction — it emits an evidence breakdown, not a bare *"87% cheating probability"*. 🟢 **This is the exact shape EU Annex III point 3 and Vietnam's Decree 33 leave sellable: local, explainable, human-gated** — and it is permissively licensed. |
| AI-Proctored Examination System | [`SuyashMore/AI-Proctored-Examination-System`](https://github.com/SuyashMore/AI-Proctored-Examination-System) | 🟢 **MIT** (`main/LICENSE`, 1068 B, © 2020 Suyash More) | not read this pass | Global | Second independent permissive proctoring implementation, and an older one (2020 copyright). Its existence is what turns the correction above from *"one row was mis-probed"* into **"the shelf was never empty"**. |

⚠️ **Both are small-team projects, and neither is a product.** The correction is about the **licence
and the gap**, not about maturity: the KB was telling readers this space was legally unavailable and
commercially unclaimed, and it was neither. Audit before use — the smaller surface is the point.

### 🟡 The proctoring *platforms* are copyleft, and that is the whole architecture argument

| Layer | Repo | Licence (payload) | Bytes | Commercial consequence |
|---|---|---|---|---|
| Open edX proctoring subsystem | [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🟡 **AGPL-3.0** | 35119 (`master/LICENSE.txt`) | Network copyleft — re-confirms this KB's existing record |
| Online proctoring platform | [`kamlendras/OpenProctor`](https://github.com/kamlendras/OpenProctor) | 🟡 **AGPL-3.0** | 34523 (`main/LICENSE`) | 🆕 Licence measured this pass; previously shelved without one |

🟢 **Fifth independent instance of this KB's best-evidenced architectural rule.** The proctoring
*platforms* are AGPL-3.0 and the proctoring *agents* are MIT. Same shape as `peancor/moodle-mcp-server`
and `Jawadh-Salih/moodle-mcp-server` (MIT side-cars outside GPL-3.0 Moodle) and Apache-2.0 `XBlock`
against AGPL-3.0 `edx-platform`. **When the platform is copyleft and the deliverable must not be, the
agent lives outside the tree and talks over an API.**

### 🟢 LATAM — the Latam-GPT tooling layer, and what "open source" actually covers

Three repos in the [`latam-gpt`](https://github.com/latam-gpt) organisation, probed first-hand:

| Repo | License (read from payload) | ★ | Region | What it is |
|---|---|---|---|---|
| [`latam-gpt/anonymization-filter`](https://github.com/latam-gpt/anonymization-filter) | 🟢 **MIT** (`main/LICENSE`, 1072 B, © 2025 GonzaloFuentes1) | not read this pass | LATAM | PII anonymisation filter from the Latam-GPT corpus pipeline. 🟢 **The most directly reusable of the three for education work** — a Spanish/Portuguese-language scrubber is exactly what a student-data pipeline needs before any model sees it. |
| [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) | 🟢 **MIT** (`main/LICENSE.md`, 1067 B, © 2020 **EleutherAI**) | not read this pass | LATAM | ⚠️ **A fork of EleutherAI's harness, not original work** — the copyright holder in the payload says so. Useful as the regional evaluation entry point; cite upstream. |
| [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) | 🟢 **MIT-0** — *MIT No Attribution* (`main/LICENSE`, 903 B, © 2025 Tim Duffy) | not read this pass | LATAM | ⚠️ **A different licence from MIT**, and a third-party holder. Sycophancy benchmark; MIT-0 drops even the attribution requirement. |

🔴 **`P463` — "Chile launches open source Latam-GPT" is true at the code layer and not at the model
layer, and not one of the three code grants is held by the project.** The holders read **Tim Duffy**,
**EleutherAI** and an **individual contributor** — none of them CENIA, and none of them any of the
60+ institutions across 15 countries the project is coordinated through. Two of the three are
**upstream projects re-hosted** under the org. ⚠️ **And the model layer could not be verified at all
from this environment:** `huggingface.co` returns **000**, so the widely-reported **Llama 3.1
Community Licence** on the 70B weights is a **secondary-source claim in this KB, not a measurement**.
That licence is **not OSI-approved** and carries acceptable-use and naming conditions.

🟢 **So the usable reading for a LATAM engagement:** the *tooling* around Latam-GPT is permissive and
vendorable today; the *weights* are not open source in the sense this KB uses the term, and must be
read against the Llama community terms before any client deliverable depends on them. **The
pedagogy layer on top of the regional sovereign model is still unbuilt** — that part of the gap the
KB recorded stands.

### 🟢 Re-confirmations — four gap repos re-probed with the branch-corrected prober, none moved

Re-measured because `P461` showed the instrument could produce a false `ABSENT`. All four still
carry **no licence payload** (13 filenames × 2 branches, with `.rst` and `pyproject.toml` existence
fallbacks):

| Repo | Verdict 2026-10-07 | Consequence |
|---|---|---|
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | 🔴 **No licence payload** (repo exists) | ⚠️ **Fourth reproduction of the false claim.** Search summaries again assert it is *"released under an MIT license"*. The paper says MIT; the repo does not. **The correction holds.** |
| [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🔴 **No licence payload** (repo exists) | Secondary sources now say **CC-BY-4.0**; the in-file self-contradiction this KB recorded is unresolved upstream |
| [`kaushal0494/UnifyingAITutorEvaluation`](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | 🔴 **No licence payload** (repo exists) | unchanged |
| [`aisingapore/sealion`](https://github.com/aisingapore/sealion) | 🔴 **No licence payload** (repo exists) | **"No education agent layer on an APAC sovereign model" — STILL OPEN**, and still for a licence reason |

🟢 **"No shippable permissive evaluator of tutoring quality" — STILL OPEN**, now re-confirmed with an
instrument known to err the other way. That matters: a gap re-confirmed by a prober that has just
been caught producing false absences is worth more than one asserted by a prober nobody had tested.

### 🔴 `P461`–`P464` — four defects, and the first one destroyed a declared gap

| ID | Defect | Proof | Cost if unfixed |
|---|---|---|---|
| **`P461`** | 🔴 **A `main`-first probe files a `master`-default repo as absent.** The existence fallback inherits the same bias, so the repo looks like it does not exist | `biswal-prem-5677/…`: `main/LICENSE` **404**, `main/README.md` **404**, `master/LICENSE` **200** (1068 B, MIT), `master/README.md` **200** (26560 B) | 🔴 **Fifth instance of this KB's "errs toward deleting a true row" family — and the first to delete an entire declared gap.** `P453` was case; this is branch |
| **`P462`** | 🔴 **A declared gap that rests on one repo's negative verdict inverts when that verdict does.** The gap was quoted for 26 passes and ranked as a build opportunity | *"No permissive open-source exam proctoring agent"* rested on exactly one licence probe. Re-probing it refuted the gap, and a second MIT agent appeared in the same run | a studio declines or mis-prices work in a space it believes is legally unavailable |
| **`P463`** | **A sovereign-model "open source" claim must be read by *layer* and by *holder*.** Both can differ from the headline | `latam-gpt`: 3 MIT/MIT-0 code grants held by Tim Duffy, EleutherAI and an individual — **none by the project**; model weights under the non-OSI Llama 3.1 Community Licence | a client deliverable built on "the open source regional model" inherits terms nobody read |
| **`P464`** | 🆕 **`huggingface.co` is unreachable from this environment (000), so no model licence in this KB is payload-verified** | `huggingface.co/` → **000**; model-card and `LICENSE` raw paths → **000** | every weights-licence statement in this KB is a secondary-source claim; **say so rather than implying measurement** |

🟢 **`P462` is the finding that pays for this pass.** `P453`–`P458` were defects that deleted *rows*,
where the cost is one missing option. This one deleted a **conclusion**: the KB did not merely omit
two MIT repositories, it published the inference *"nobody holds this space, go build it"* and ranked
it. **A gap is a measurement too, and it decays faster than a row** — a row is wrong only if the repo
changes, while a gap is wrong the moment *any* repo anywhere acquires a licence. 🔵 **The rule this
pass adds: a declared gap must carry the probe scope that produced it and must be re-measured before
it is quoted, not merely restated.** The row beside the mis-probed one in the same table recorded
its scope (*"2 branches × 6 filenames"*); the one that mattered recorded none, which is why the
correction above cannot distinguish *"the licence was added later"* from *"the probe was too
narrow"* — and that undecidability is itself the defect.

## 🟢 Thirty-second pass, 2026-10-07 — 14 agents added, and four defects found in this shelf's own prober

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07.** Three verification channels were re-measured this pass and **all three are closed**:
`curl -sI` on a github.com landing page → **403**, `curl` **GET** on the same page → **403**,
`api.github.com` → **403**. So **no star counts were read this pass**; every `★` cell says so rather
than carrying a stale or inferred number. A negative control
(`totally-fake-org-zzz9/nope-repo-abc`) returned `ABSENT` in the same run that returned these 200s.

🔴 **Before trusting any `ABSENT` verdict in this KB's history, read `P453`–`P458` below.** Four
defects in the prober were found this pass by running it against repos whose correct answer was
already known, and **every one of them errs toward deleting a true row.**

### Tutoring agents

| Agent | Repo | License (read from payload) | ★ | What it does |
|---|---|---|---|---|
| TutorIA | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** (`main/LICENSE`, 1068 B, © 2026 Grupo Sirius) | not read this pass | 🟢 **The only LATAM-origin education agent on this shelf with a verified licence.** Autonomous tutor for **rural** higher education in Risaralda, **Colombia** (Universidad Tecnológica de Pereira). Runs **inside Open edX**, Claude API as the language engine, TTS voice replies, animated avatar, teacher statistics panel, context persistence across sessions. Bilingual ES/EN README. First subjects: Programación I (Python), Introducción a la Matemática. |
| OpenTutor | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** (`main/LICENSE`, 1068 B, © 2026 Zijin Zhang) | not read this pass | Block-based adaptive learning workspace that runs **locally**: upload material → notes, quizzes, flashcards, adaptive tutor. **FSRS** spaced repetition, knowledge graph, cognitive-load detection, 10+ LLM providers, no API key required. 🔵 **Canonical** — two forks circulate, one of them renamed (`P457`). |
| OpenTutor (LEARNable) | [`LEARNableLabs/opentutor`](https://github.com/LEARNableLabs/opentutor) | **MIT** (`main/LICENSE`, 1079 B, © 2026 OpenTutor Contributors) | not read this pass | 🔵 **A different project that shares the name.** One topic a day, **Socratic** — asks before explaining, targets what the learner keeps getting wrong, re-surfaces concepts days later in new contexts. Local-first; learning history stays on the machine. |
| Education AI Suite | [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | **Apache-2.0** (`main/LICENSE`, 11350 B) | not read this pass | Intel's education suite: reference applications, libraries, microservices and **benchmarking** tools, with audio/video pipelines accelerated by **OpenVINO** on Intel CPU / iGPU / NPU. Two workflows: **Smart Classroom** (multimodal session processing and summarisation) and **Teaching Assistant** (voice-first study help). 🔵 The only row on this shelf that ships **hardware-selection tooling** — the question an on-prem school deployment actually has to answer. |
| DeepTutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** (`main/LICENSE`, 11408 B) | not read this pass | Agent-native lifelong tutoring with persistent per-learner memory and proactive Heartbeat check-ins. 🟢 **Licence re-read from payload this pass, unchanged.** ⚠️ Its 🔴 `PyMuPDF` AGPL-or-Artifex dependency warning recorded on this shelf on 2026-10-06 **still stands and was not re-measured this pass.** |

### Agents over the LMS gradebook (MCP)

🔵 **Six independent MIT implementations — not a fork tree.** Each carries a **different copyright
holder**, so six people built the same bridge in the same window: *an agent that reads and writes a
real gradebook*. That is the clearest demand signal in this pass — the surface schools want agents
pointed at is **the LMS gradebook API**, not a chat window. ⚠️ **It also means none of them is a
standard.** Tool counts differ by more than 3× (51 / 102 / 165) and nothing certifies what a grade
*write* does. Pick one, pin the version, and test the write path against a staging course.

| Agent | Repo | License (read from payload) | ★ | What it does |
|---|---|---|---|---|
| canvas-mcp (Sachdev) | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** (1070 B, © 2025 Vishal Sachdev) | not read this pass | Canvas LMS MCP server: ~102 tools + 8 agent skills, targets Claude, Cursor, Codex and 40+ clients. Includes **bulk grading** of 10+ submissions. |
| canvas-lms-mcp (Bru) | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** (1069 B, © 2026 Christian Bru) | not read this pass | TypeScript MCP server, ~165 tools: courses, assignments, submissions, **gradebook history**, rubrics, quizzes and Canvas admin workflows. The widest of the cluster. |
| mcp-canvas-server | [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | **MIT** (1080 B, © 2025 Charlie Cárdenas Toledo) | not read this pass | ~51 tools to query, grade, audit and manage Canvas. Two transports: `stdio` and Streamable-HTTP with interactive Swagger docs. 🔵 **Ships a `README.es.md`** — the most ready for a Spanish-speaking delivery team. ⚠️ **Filed Global, not LATAM:** a Spanish README and a Spanish personal name are not evidence of origin, and no repo metadata was readable this pass. |
| canvas-mcp (self-hosted) | [`caleb-media-studio/canvas-mcp`](https://github.com/caleb-media-studio/canvas-mcp) | **MIT** (1065 B, © 2026 Caleb Mau) | not read this pass | Self-hosted Canvas MCP for students and educators. |
| canvas-lms-mcp (mtgibbs) | [`mtgibbs/canvas-lms-mcp`](https://github.com/mtgibbs/canvas-lms-mcp) | **MIT** (1063 B, © 2025 mtgibbs) | not read this pass | Connects an agent to Canvas for grades, assignments and academic data. The smallest of the cluster and therefore the cheapest to audit line-by-line before it touches a gradebook. |
| moodle-mcp-server | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** (1062 B, © 2026 Jawadh) | not read this pass | **Moodle**, not Canvas: courses, grades, assignments, deadlines, notifications. 🔵 A side-car outside Moodle's **GPL-3.0** tree — the same licence boundary this shelf recorded for `peancor/moodle-mcp-server`. |

### Assessment and rubrics

| Agent | Repo | License (read from payload) | ★ | What it does |
|---|---|---|---|---|
| rubric | [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | **MIT** (1076 B, © 2025 The LLM Data Company) | not read this pass | Python library for LLM evaluation against **weighted rubrics**, provider-agnostic. 🔵 The primitive this shelf was missing: a rubric as a **data structure**, not a prompt. That is what makes a grading decision auditable after the fact. |
| prometheus-eval | [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) | **Apache-2.0** (`main/LICENSE`, 10141 B) | not read this pass | Rubric-conditioned LLM-as-judge with open evaluator weights. Pairs with `rubric` above: one holds the rubric, the other scores against it **without sending student work to a frontier API** — which is the whole compliance argument under EU AI Act Annex III and US state student-data rules. |
| automated-summary-evaluation-llm | [`baker-jr-john/automated-summary-evaluation-llm`](https://github.com/baker-jr-john/automated-summary-evaluation-llm) | **MIT** (1070 B, © 2026 John Baker Jr.) | not read this pass | Rubric-aligned **formative** feedback on middle-school informational summaries using **Llama 3.1 8B**. Proof-of-concept scale — but the only row here validated against actual K-12 student writing, and formative-only output keeps it out of the high-risk Annex III band. |

### Teaching substrate

| Agent | Repo | License (read from payload) | ★ | What it does |
|---|---|---|---|---|
| IA-PARA-TODOS | [`0xnavarro/IA-PARA-TODOS`](https://github.com/0xnavarro/IA-PARA-TODOS) | **Apache-2.0** (`main/LICENSE`, 11470 B) | not read this pass | Spanish-language open-source AI collection: applications, tutorials, resources. Enablement substrate for Spanish-speaking cohorts, not a runtime. Pairs with the Microsoft and Hugging Face courses already on this shelf for a Spanish-first track. |

### 🔴 Rejected this pass — 11 of 33 repos cannot enter a deliverable

**10 of 33 repos probed have no licence payload at all, and 1 has a `LICENSE` file that explicitly
refuses to grant a licence.** Being public is not a grant. Listed so a later pass does not re-spend
the search or, worse, shelve one of them.

| Repo | Verdict | Note |
|---|---|---|
| [`murderszn/open-tutor`](https://github.com/murderszn/open-tutor) | 🔴 **NON-GRANT, with `LICENSE` serving 200** | Payload (869 B) reads: *"This repository has not declared a project-wide reuse license… A public GitHub repository is not itself a declaration of an open-source or open-content license."* See **`P455`**. |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 **NO LICENCE PAYLOAD** | A secondary source called it *"Apache 2.0 … without the copyleft obligations GPL and AGPL carry"*. The only "Apache" in its README is **`- Apache (recommended) with mod_rewrite enabled`** — the **web server**. See **`P456`**. |
| [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) · [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🔴 **NO LICENCE PAYLOAD** | These two refute the blanket claim that the whole Canvas-MCP cluster is MIT: **2 of 8 are not.** |
| [`Johnson1662/OpenTutor`](https://github.com/Johnson1662/OpenTutor) | 🔴 **NO LICENCE PAYLOAD** | A third distinct project called "OpenTutor" (AI-native adaptive learning with a living knowledge graph). No grant. |
| [`a-bobadilla/Asistente-Pedagogico-IA`](https://github.com/a-bobadilla/Asistente-Pedagogico-IA) · [`henriquebotelhogomes/educacao`](https://github.com/henriquebotelhogomes/educacao) · [`virginiandujar/educa-ia`](https://github.com/virginiandujar/educa-ia) | 🔴 **NO LICENCE PAYLOAD** | ⚠️ **All three are LATAM.** With `TutorIA`, that is **1 of 4** LATAM repos found this pass carrying a grant. The regional constraint is not absence of work — it is **absence of licences**, and it is cheap to fix upstream. |
| [`EnvCommons/RubricHub`](https://github.com/EnvCommons/RubricHub) · [`omerbbbb/ai-graded-assessment-platform`](https://github.com/omerbbbb/ai-graded-assessment-platform) · [`lakshya85664/Assessment_Agent_LLM`](https://github.com/lakshya85664/Assessment_Agent_LLM) | 🔴 **NO LICENCE PAYLOAD** | `RubricHub` is the costly one: ~364k tasks with 2–67 rubric criteria each, and no grant permitting use. |

### 🔴 `P453`–`P458` — the prober was wrong four ways, and all four delete true rows

| ID | Defect | Proof | Cost if unfixed |
|---|---|---|---|
| **`P453`** | `raw.githubusercontent.com` paths are **case-sensitive**; a probe list without `LICENSE.TXT` misses real licences | `pykt-team/pykt-toolkit`: `LICENSE` **200**, `license` **404**, `LiCeNsE` **404**. `openedx/XBlock`'s licence is at **`master/LICENSE.TXT`** | 🔴 XBlock — real, Apache-2.0, **already on this shelf** — came back `ABSENT`. A pass trusting that deletes a good row |
| **`P454`** | existence fallback probed only `README.md`, so `.rst` projects look non-existent | `openedx/XBlock`: `master/README.rst` **200**, `README.md` **404** | the same false delete by a second independent route |
| **`P455`** | 🔴 **a `200` on a `LICENSE` path is not a grant** | `murderszn/open-tutor` — file present, 869 B, and its text declares **no licence** | an all-rights-reserved repo is filed as licensed and reaches a client deliverable |
| **`P458`** | a repo's own README can link a licence path that **404s** | XBlock's README links `…/blob/master/LICENSE.txt`; the file is `LICENSE.TXT`. `pyproject.toml` settles it: `license = "Apache-2.0"`, `license-files = ["LICENSE.TXT"]` | a link-following verifier reports "licence missing" on a correctly licensed repo |

🟢 **`P455` is the finding that pays for this pass.** Every previous licence correction in this KB
moved a row between two *real* licences, where the worst case is a wrong **degree** of freedom. Here
the file exists, is named `LICENSE`, serves `200`, and says **no**. **Existence was never the test —
the grant is the test.**

🔴 **`P456` — a licence family in a README may be a web server, not a licence.** *Apache*, *nginx*,
*MIT* and *BSD* are each simultaneously the name of a licence and the name of something that is not
one. A licence family appearing in a README's **requirements** section is not a licence claim, and
in the `formalms` case a secondary source converted exactly that into the precise commercial
conclusion the error produces. 🔵 Combined with pass 30's subject-model note, the rule is now:
**a licence claim has a subject *and* a role — check both before believing it.**

### 🟢 Re-confirmations — four shelf rows re-read from payload, none moved

| Repo | Payload | Verdict |
|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `main/LICENSE`, 11408 B | 🟢 **Apache-2.0**, unchanged |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `master/LICENSE`, 11120 B | 🟢 **ECL-2.0** — payload opens *"consists of the Apache 2.0 license, modified…"*, corroborating pass 30's lineage reading |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `master/LICENSE`, 8241 B | 🟢 **LGPL-3.0**, genuinely LGPL — **independently corroborates pass 28's negative half** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | `master/LICENSE.TXT`, 11357 B | 🟢 **Apache-2.0** — the row was right; the **instrument** was wrong |

⚠️ **`openedx/edx-platform` is `AGPL-3.0`** (`master/LICENSE`, 35136 B, read this pass). Open edX's
*core platform* is network-copyleft while **`XBlock` — the extension point an agent plugs into — is
Apache-2.0.** 🔵 **That asymmetry is the architecture argument for all Open edX work:** build the
agent as an XBlock or as an external service against Apache-2.0 surfaces, and the AGPL stays where it
already is — on a platform the client self-hosts rather than redistributes. `LabSirius/TutorIA`
above is a working instance of exactly this shape, which is part of why it is the strongest new row
in this pass.

# AI Agents — Education

Open source AI agents and agent-adjacent tooling for education. Focus on MIT /
Apache-2.0 / BSD, the licenses Globant can build on and redistribute to clients.

**Verification method (2026-10-06):** every license below was read from the
repository's own `LICENSE` payload via `raw.githubusercontent.com`, not from a
listing sidebar, a badge, or a blog post. Star counts and descriptions were read
from the repository page the same day. `api.github.com` is not reachable from
this environment (403, session-scoped), so star counts come from the rendered
page; where a count was not read this pass, the cell says so rather than
carrying a stale or inferred number.

## 🟢 How to read a licence cell on this shelf — thirtieth pass, 2026-10-07

**Pass 28 flagged 29 rows of this KB as the corpus contradicting itself about a licence. Pass 29
adjudicated 14 of them first-hand and found 0 contradictions.** Read that before you distrust a cell
below.

🔵 **A licence claim in this file has a SUBJECT, and the flagging instrument had no subject model.**
In all 13 rows read, the "competing" family belonged to something else named in the same sentence:

| What you will see in a cell | What it means | Example |
|---|---|---|
| two families, one of them a **successor or fork** | one sentence, two repositories — both correct | `rhasspy/piper` **MIT but archived**, development moved to `OHF-Voice/piper1-gpl` **GPL-3.0** |
| two families, one scoped to **deps** | the repo's own licence is the first one | `learningequality/kolibri` is **MIT** with *two LGPL dependencies* |
| two families in an **either/or** | a recommendation, not a conflict | *Fairlearn (**MIT**) **or** `Trusted-AI/AIF360` (**Apache-2.0**)* |
| **ECL-2.0** named next to **Apache-2.0** | a lineage statement; ECL-2.0 *is* an Apache-2.0 derivative, and permissive | `sakaiproject/sakai`, `opencast/opencast` |
| code family + **`LICENSE-docs`** family | two real licences on two layers | `yongsoojoo/esd2026-agent-workflow` — **MIT** code, **CC BY 4.0** docs |
| an **in-tree vs side-car** pair | the licence boundary *is* the architecture point | `peancor/moodle-mcp-server` is **MIT** *because* it sits outside the **GPL-3.0** Moodle tree |
| a family inside **WRONG / "not MIT" / "mis-reported"** | the prose is refuting it — it is not a claim | `frappe/lms` is **AGPL-3.0, not MIT**; `rosariosis` detector said `agpl-1.0`, payload is **GPL-2.0** |
| a family inside a **`license:` filter** | a query string, not a licence | `aryankeluskar/canvas-mcp` is **ISC**, *"rejected by a `license:mit OR license:apache-2.0 OR license:bsd` filter"* |
| 🔴 a **`CC-BY`** on a data or corpus row | ⚠️ **check the full string before you rely on it** — the qualifier may have been normalised away | `Llamacha/IWSLT2023_Quechua_data` is filed `CC-BY` but is **CC BY-NC-ND 3.0**: no commercial use, no derivatives |

⚠️ **Three of these cost money if misread.** A family that appears only to be marked wrong, and a
family that appears only inside a search filter, are **not** licences of the repository on that row —
those are the prose doing its job. 🔴 **The last row is the opposite case and the dangerous one:**
there the *data* is wrong, not the prose. A flattened `CC-BY` reads as "commercial use permitted"
when the real grant is **CC BY-NC-ND**, which permits neither commercial use nor derivatives. Run
**`P22` check 4** (`compose/patterns.md`) on any CC-licensed corpus before it enters a deliverable,
and record the **full licence string**, never the normalised family.

⚠️ **Scope of this note:** 14 of 29 flagged rows adjudicated first-hand; 3 more presumed
`CORRECTION-TRAIL` by signature; 12 unexamined. Execution of this tree's suites was **denied** this
pass, so nothing here is a re-measurement — it is a reading. Full detail in `agents/trending.md`,
2026-10-07, thirtieth pass.

## 🔴 Licence corrections — twenty-eighth pass, 2026-10-07

**21 of the 412 licensed rows on this shelf carried the wrong licence family**, and the cause was
three defects in the classifier rather than three bad readings. Read this before using any licence
cell below as a commercial answer.

| Correction | n | Direction |
|---|---|---|
| `UNKNOWN` → **EUPL** | 9 | the EMEA public-sector tier became machine-readable for the first time |
| `LGPL` → **GPL** (`P452`) | 7 | 🔴 **a commercial answer inverts** — the LGPL permits linking from proprietary code, GPL-2.0 does not |
| `GPL` → **MPL-2.0** | 5 | 🟢 less restrictive than filed; pass 26 published this correction in prose and never in the data |

🔴 **`P452` — the GNU family must be read from the payload's TITLE, not from a window.** The three
GNU licences name each other inside their own texts. Probing LGPL before GPL over `text[:4000]`
therefore returned **LGPL for every GPL-2.0 payload** (its Preamble recommends the LGPL at
character 784) and the correct answer for every GPL-3.0 payload (whose closing notes do so at
34,143). Nothing but the constant separated them. The seven affected rows are `OpenEMIS/core`,
`openemis/core`, `portabilis/i-educar`, `oat-sa/qti-sdk`, `oat-sa/lib-lti1p3-core`,
`inepdadosabertos/api` and `yunger7/enem-api`; the four rows that are genuinely LGPL did not move.

🔴 **`P449` — the `CC-BY` label here covers three different commercial answers**, and 5 of the 7
rows carrying it are commercially unusable or mislabelled:

| Row | Published | Actually | Commercial |
|---|---|---|---|
| `EbookFoundation/free-programming-books` · `microsoft/autogen` | CC-BY | Attribution 4.0 | 🟢 permitted |
| `Yunfeng-Wan/CSTutorBench` · `facebookresearch/seamless_communication` | CC-BY | Attribution-**NonCommercial** 4.0 | 🔴 prohibited |
| `Jona-Zwetsloot/Somtoday-Mod` · `openstax/osbooks-biology-bundle` | CC-BY | Attribution-**NonCommercial-ShareAlike** 4.0 | 🔴 prohibited |
| `sign/translate` | CC-BY | 🔴 **a paid dual-tier licence, not Creative Commons** | 🔴 **paid** |

🔴 **`sign/translate` is the row to remember**, and this file already described it correctly as
"Non-OSI, dual-tier" while the data layer said `CC-BY`. Its `LICENSE.md` (17,404 B, © 2022 Nagish
Inc.) grants a free tier under CC BY-NC-SA 4.0 to *"individuals, non-profit organizations, and
educational institutions"* and requires *"a separate license … for for-profit commercial
organizations."* **Globant is the latter.**

🔵 **`microsoft/autogen` is the clean example of the opposite trap.** Its root grant is **CC-BY** —
the *documentation* licence — and its code is **MIT**, in `LICENSE-CODE`. A rooted licence probe
reports CC-BY for an MIT codebase. Full-tree enumeration of all 412 rows found this pattern in four
repositories and found **zero** cases of the reverse (a permissive root hiding a reciprocal grant
below it), so on this shelf the rule is: **check `LICENSE-CODE` or `docs/LICENSE` before writing off
a CC- or AGPL-rooted repository.**

🟢 **Where the licence facts came from: this file.** Every one of the corrections above was already
stated correctly in this KB's prose; what was wrong was the machine-readable layer. Measured over
six published files, prose and data disagree on **15 of 431** repositories and **the prose is right
in 14 of 15** (`p449`). The fifteenth is a correct archived finding that a defective classifier
overwrote — see `repos/trending.md` for the full account.

## Agents and tools

**50 rows, all verified.** The 12 recorded in the morning pass of 2026-10-06, 2
added in the second pass, **17 added in the third pass** from the `ai-tutor`
GitHub topic page and a stars-sorted repository search, and **5 added in the
fourth pass** by tracing academic papers to their repositories and sweeping a
GitHub organisation, and **4 added in the fifth pass** by searching on funding
body, ministry and university name in English and Spanish instead of by topic or
star count, and **3 added in the eighth pass** from an
**institutional-event channel** — a university hackathon whose rules make an OSI
licence a condition of evaluation — and **3 added in the twenty-ninth pass** from the
mandatory query set itself, which had produced nothing for seventeen consecutive passes
before it — six distinct channels, each new to this KB when it was used. One of the 17, OpenTutor, is a **reinstatement** of an entry this KB wrongly
withdrew earlier the same day; see the corrections section. The fourth pass added
the largest single asset in this KB (**OpenMAIC, MIT, 40.0k★**) and the first
**Africa-placed** repositories it has ever recorded. The fifth pass added the first
**India-, LATAM- and ASEAN-placed** permissive projects — and found all three at
**0–9★**, which is the finding, not a footnote.

The third-pass rows sit in their own table below the core shelf, because most of
them are **Agent Skills rather than applications** and that distinction decides how
you deliver them.

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (`LICENSE`) | 40.8k | Agent-native lifelong tutoring. Two-layer plugin model (single-shot Tools + multi-stage Capabilities), exposed via CLI, WebSocket API and Python SDK. Per-learner TutorBot workspaces with persistent memory. Latest release v1.6.13 (2026-10-04). Python. |
| AI Agents for Beginners | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 76.5k | 18-lesson course on building AI agents; code samples now target Microsoft Agent Framework. The default enablement asset for client-staff upskilling. |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | 29.7k | Barebones library for agents that think in code. Small surface area makes it the cheapest framework to audit for a high-risk education deployment. |
| Microsoft Agent Framework (MAF) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | 14.0k | Building, orchestrating and deploying agents and multi-agent workflows, Python and .NET. Ships migration guides *from* AutoGen and Semantic Kernel. |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 (`LICENSE`) | 6.8k | Online learning platform for authoring interactive lessons ("explorations") with built-in misconception handling. One of only three permissively licensed full platforms in this KB. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT (`LICENSE`) | 278 (95 forks) | Canvas LMS MCP server: **up to 103 tools** and 8 agent skills for students, educators and learning designers. Includes a 20-check WCAG accessibility scanner and bulk-grading tools. Works with 40+ MCP clients. Latest release v1.13.0 (Sep 2026). The canonical repo — pin it against its forks. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT (`LICENSE`) | 264 | Intelligent tutoring system with Bayesian Knowledge Tracing, from CAHLR at UC Berkeley. Published at CHI '23 with a follow-up in PLOS ONE. ReactJS + Firebase. The auditable mastery model in this list. |
| Educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT (`LICENSE`) | 388 | Python package for generating educational content with generative AI — MCQs, open-ended items, lesson plans, flashcards. |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT (`LICENSE`) | 1.1k | Offline-first learning platform for teaching and learning without an internet connection. The only fully permissive end-to-end platform here; the basis of the equity-deployment pattern. |
| Moodle MCP Server | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | MIT (`LICENSE`) | not read this pass | MCP server exposing Moodle data to agents from *outside* the Moodle tree — which is why it is MIT while in-tree Moodle plugins are GPL-3.0 (see the license-boundary note below). |
| Hugging Face Agents Course | [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | not read this pass | Open course on building agents with Hugging Face tooling. Pairs with the Microsoft course for a two-track enablement curriculum. |
| learn-agentic-ai | [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | not read this pass | Agentic-AI curriculum used at large scale by the Panaversity / GIAIC programme in Pakistan — a rare APAC-origin education asset in this space. |
| lineage-skill | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | Apache-2.0 (`LICENSE@main`) | 448 | Distils videos, PDFs, transcripts and notes into **source-backed teacher Agent Skills**: keeps source attribution, extracts instructor methodology, orders practice tasks progressively. Python. The highest-starred project on the `education-ai` topic, and the clearest example of Agent Skills used as a distribution format for pedagogy rather than for tooling. |
| Claw-ED | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | MIT (`LICENSE@main`) | 60 | Local-first AI teaching assistant for lesson drafts and classroom materials. Python. Small and early, but local-first + MIT is exactly the shape EMEA data-residency rules and LATAM cost constraints ask for. |

### Added in the third pass of 2026-10-06 — the `ai-tutor` channel

Stars as displayed 2026-10-06; licences read from each repo's own `LICENSE`
payload. Note how many are **skills, not applications**: that is the packaging
shift recorded as trend 12 in `intel/trends.md`, and it is now the majority shape
in this category.

| Project | Repo | Licence (payload) | ★ | Shape | What it does |
|---|---|---|---|---|---|
| StudyMate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT (`LICENSE`) | 624 | app | Chinese-language study partner for maths and CS (linear algebra, calculus, probability, C++, Python, ML, DL) on a "learn with doing" principle. Python; ships a DeepSeek harness and an Antigravity multi-agent plugin. The maintainer's README openly documents a vibe-coded origin and a manual rewrite in progress — read it before adopting. **The highest-starred permissive education agent found outside DeepTutor.** |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT (`LICENSE`) | 506 | MCP side-car | **53 tools** (42 essential + 11 GUI) over Anki, v0.27.0 beta, TypeScript. An agent can present cards, explain concepts and create or edit notes mid-session. Requires the Anki **desktop app plus the AnkiConnect plugin** — plan for that dependency. The highest-starred education MCP server in existence; see the shelf note below. |
| universal-examprep-skill | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT (`LICENSE`) | 300 | skill | "Exam Cram Coach" with **cross-session memory** and **citation-sourced** answers. Python. Memory + citations is the combination the high-risk regimes reward. |
| algo-sensei | [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | MIT (`LICENSE`) | 285 | skill | LeetCode / DSA mentor packaged for Claude Code and claude.ai. CS-education pedagogy shipped as a skill rather than an app. |
| universal-diagnostic-tutor-skill | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | MIT (`LICENSE`) | 238 | skill | **Diagnosis-first** tutor for STEM and CS: establishes the misconception before explaining. Pedagogically the strongest shape on this list, and the one closest to OATutor's mastery logic without the Bayesian machinery. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT (`LICENSE`) | 156 | skill | Chinese civil-service exam tutoring with **authority citations** — high-stakes prep with provenance attached. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT (`LICENSE`) | 130 | app | **Block-based local-first adaptive learning workspace.** 12 composable blocks (notes, quiz, flashcards, knowledge graph, study plan, analytics), **FSRS 4.5** spaced repetition with proactive review, **LOOM** concept-mastery/prerequisite graph generating learning paths, 10+ LLM providers **defaulting to Ollama**, FastAPI + Next.js, 27 forks. Runs entirely on the user's machine with no cloud transmission. **Reinstated this pass** — see corrections. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT (`LICENSE`) | 106 | skill **pack** | A curated collection of teaching-and-learning skills rather than a single skill. Shell. The first *pack* found in education — the distribution unit above the individual skill. |
| feifei-companion | [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) | Apache-2.0 (`LICENSE`) | 105 | app | "Trinity K12 AI Education System" for Chinese students. Permissive, China-origin, K-12. |
| mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT (`LICENSE`) | 91 | **full LMS** | Self-hosted AI-mentor LMS for enterprise L&D: voice and chat role-play scored automatically, **automated grading of open-ended behavioural and problem-solving answers**, AI course generation from existing documentation, Langfuse tracing of every model call, multi-tenant and white-label. TypeScript, Poland-origin. **This is the row that narrows this KB's standing "no permissive auto-grader" gap** — full entry in `verticals/solutions.md`. |
| Studivexa | [codeXsidd/Studivexa](https://github.com/codeXsidd/Studivexa) | MIT (`LICENSE`) | 72 | app | AI productivity workspace for students and developers. JavaScript. |
| AI_Tutor_Release | [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release) | MIT (`LICENSE`) | 57 | app | Open-source **RAG** tutor for K-9, adapted to the Chinese grade 1–9 curriculum. JavaScript. A rare **curriculum-aligned** permissive tutor — directly relevant to the curriculum-mandate demand recorded in `intel/market.md`. |
| civil-ai | [zhangl1001/civil-ai](https://github.com/zhangl1001/civil-ai) | MIT (`LICENSE`) | 43 | reference impl | **Local-first adaptive tutoring agent foundation reference implementation** for iOS and Web, with a civil-service-exam application on top. TypeScript. Earns a row at 43★ because it is explicitly a reference architecture, and a local-first one. |
| ai-tutor-app | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | Apache-2.0 (`LICENSE`) | 31 | app | Agentic-RAG tutor for applied AI/LLM/RAG/Python: **LangGraph agent + FastAPI + Next.js**, grounded in a curated course and library. The closest production-shaped reference for the P2 retrieval-tutoring pipeline. |
| feynman-tutor | [koukekoukej-glitch/feynman-tutor](https://github.com/koukekoukej-glitch/feynman-tutor) | MIT (`LICENSE`) | 29 | skill | Inverts the roles: **the learner teaches the AI** (Feynman technique) to expose gaps. Python. |
| anything-to-course | [lowwwbank/anything-to-course](https://github.com/lowwwbank/anything-to-course) | MIT (`LICENSE`) | 18 | skill | Turns any material into a **learning-science-based** self-study course with retrieval practice and spaced repetition. The skill-shaped sibling of pattern P2. |
| nanobot-study | [WangyiNTU/nanobot-study](https://github.com/WangyiNTU/nanobot-study) | MIT (`LICENSE`) | 18 | enablement | Guided 3-day study plan built on nanobot (~3k lines of Python) with a Socratic tutor. Small enough to read end-to-end, which is exactly what an enablement asset needs to be. |
| Scientific-learning-skills | [hwl668/Scientific-learning-skills-](https://github.com/hwl668/Scientific-learning-skills-) | MIT (`LICENSE`) | 15 | skill | Diagnosis-first skills that turn an assistant "from answer machine into learning tutor". |

### The dependency closure — added in the twenty-first pass of 2026-10-06

⚠️ **Read this table before quoting any row above as "permissive, safe to build on".** Every licence
in this file answers *"what is this project?"*. This table answers **"what does it install?"** —
and for two rows the two answers disagree in a way that reaches a client contract.

Measured first-hand on 2026-10-06 from `pypi.org/pypi/<name>/json` and
`registry.npmjs.org/<name>`, depth 1 (**declared direct runtime dependencies only**). Instrument,
method and limits: `compose/code/dependency-licence-closure/`.

| Project | Its licence | Deps | Verdict | The dependency that decides it |
|---|---|---|---|---|
| **DeepTutor** | Apache-2.0 | 43 | 🔴 **REVIEW-STRONG** | **`PyMuPDF>=1.26.0`**, core array — `Dual Licensed - GNU AFFERO GPL 3.0 or Artifex Commercial License` (v1.28.2). **AGPL, or pay Artifex, or replace the PDF layer** |
| **Oppia** | Apache-2.0 | 152 | 🔴 **REVIEW-STRONG** | **`mutagen`** → `GPL-2.0-or-later`. Also `certifi` (MPL-2.0), `orjson` (`MPL-2.0 AND (Apache-2.0 OR MIT)`), `azure-cognitiveservices-speech` (`Other/Proprietary License`) |
| **Kolibri** | MIT | 32 | ⚠️ **REVIEW-WEAK** | `json-schema-validator` (LGPL), `zeroconf-py2compat` (LGPL). ⚠️ Measurable **only** via `[dependency-groups] base` — see the note below |
| **A11y MCP** | MIT | 5 | ⚠️ **REVIEW-WEAK** | **`axe-core` + `@axe-core/puppeteer` → MPL-2.0.** This file already named both deps and omitted the grant |
| **Canvas MCP** | MIT | 7 | 🔴 **REVIEW-UNKNOWN** | `python-dateutil` publishes the string `"Dual License"`, naming neither half |
| **OATutor** | MIT | 36 | 🔴 **REVIEW-UNKNOWN** | declares **`@common/global-config`**, which **404s on npm** — a declared name the registry does not serve |
| **smolagents** | Apache-2.0 | 6 | 🟢 **CLEAN** | — |
| **anki-mcp-server** | MIT | 24 | 🟢 **CLEAN** | — |
| **ai-tutor-app** | Apache-2.0 | 20 | 🟢 **CLEAN** | — |
| **Claw-ED** | MIT | 14 | 🟢 **CLEAN** | — |
| **mcp-tutor** | — | 10 | 🟢 **CLEAN** | — |
| **Moodle MCP Server** | MIT | 2 | 🟢 **CLEAN** | — |
| **MAF** | MIT | 1 | ⚠️ **CLEAN, and uninformative** | one dep, `agent-framework-core[all]==1.20.0`; the closure is a level down |
| **WCAG Accessibility Skills** | MIT | **0** | 🟢 **CLEAN, genuine zero** | 🟢 **Confirms this file's own claim of "no production dependencies"** through an independent channel |

**Totals: 13 measurable targets, 352 declared direct dependencies — 337 permissive (95.7%), 7
weak-copyleft, 6 unreadable, 2 strong-copyleft.**

🟢 **The shelf is overwhelmingly clean, and that is the headline, not a hedge.** 95.7% permissive at
depth 1 means twenty passes of licence curation worked. What this channel adds is that *"probably
fine"* is now **two named rows in two named projects**, each fixable before a proposal goes out.

⚠️ **Three limits, because a verdict quoted past them becomes wrong data:**

1. **Depth 1 is not the closure.** Transitive dependencies are not measured. `certifi` (MPL-2.0) sits
   in nearly every Python deployment and surfaced here only in Oppia, which declares it directly.
2. **Linkage is not analysed.** `REVIEW-*` means *"a lawyer should look at this specific row"*, not
   *"this is a violation"*. Whether importing an AGPL library makes the importer a derivative work
   depends on how it is used and shipped.
3. 🔴 **Three rows above are not yet measured at all** — `Selleo/mentingo` and `zijinz456/OpenTutor`
   are pnpm **workspace roots** whose runtime deps live in `apps/*`, and `Miaotofu01/Study-Mate`
   carries a vestigial `package.json`. ⚠️ **"Not measured" is not "clean" and this table does not
   list them as clean.**

### 🔴 The Kolibri trap, recorded because it generalises

🔴 **Kolibri serves `requirements.txt` at HTTP 200 and the file declares nothing** — its header says
it exists *"only as the sink for any EXTRA_REQUIREMENTS injected at build time"* — **and its
`pyproject.toml` declares `dependencies = []`, literally empty.** The real runtime set is in
**`[dependency-groups] base`** (PEP 735), resolved by `make staticdeps`.

⚠️ **So both canonical places answer "nothing", and both answers are wrong.** A sweep keyed on
filename reports *"Kolibri has zero dependencies"*, which is not a missing measurement but a
confident wrong one. 🔵 **The general rule this leaves: a 200 on a manifest is evidence the file
exists, never evidence it declares anything** — and in this KB, Kolibri is the only fully permissive
end-to-end platform and the basis of the equity-deployment pattern, so a wrong zero there would have
travelled into every offline engagement.

### Measured rejections from the same sweep

High stars, unusable for reusable studio IP. Recorded so the next pass does not
re-probe them.

| Repo | ★ | Licence (payload) | Verdict |
|---|---|---|---|
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 563 | **AGPL-3.0** | Reject for reusable IP. Skill tree for lifelong learning, 30+ skills K-12 to career. Useful as a competency-graph *reference*. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | 156 | **AGPL-3.0** | Reject for reusable IP. Self-hosted AI language learning, local or cloud LLMs. |
| [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | 88 | **GPL** | Reject for reusable IP. Builds a private course in about a minute; take the idea, not the code. |
| [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | 71 | **AGPL-3.0** | Reject for reusable IP. Turns material into a game-based course. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 61 | **NONE** | **Do not use.** 6 specialised agents, adaptive roadmaps, quizzes, RAG — no `LICENSE` at root, and its README licence section reads only *"This project is open source and available for educational purposes."* |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | 24 | **NONE** | **Do not use.** 21-step Socratic-tutor workflow, no `LICENSE` and **no licence mention anywhere in the README**. |

**A third failure mode for the catalogue: the unenforceable prose grant.**
"Open source and available for educational purposes" names no licence, no copyright
holder and no grant to modify or redistribute, and "for educational purposes" would
*restrict* commercial use if it meant anything. It is worse than silence because it
reads like permission and survives a casual review. This KB's licence-failure
catalogue now has three entries: **no licence file at all**
(`DMontgomery40/mcp-canvas-lms`), **a licence hidden outside the root**
(`OS4ED/openSIS-Classic` at `docs/License.txt`, `frappe/*` at lowercase
`license.txt`), and **prose that imitates a grant** (the two rows above).

### Added in the fourth pass of 2026-10-06 — the OpenMAIC upstream, and the first Africa-placed shelf

**New channel this pass: paper-to-repository tracing** (arXiv and the ACL
Anthology demo track) plus a **GitHub-organisation sweep**. Neither had been used
by any earlier pass of this KB. Both licence columns below were read from the
repository's own `LICENSE` payload via `raw.githubusercontent.com` on 2026-10-06.

The headline is not a new discovery — it is the **resolution of a gap this KB has
carried through three passes**. See the corrections section.

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** (`LICENSE`, © 2026 THU-MAIC) | **40.0k** | Open Multi-Agent Interactive Classroom, from **Tsinghua University**. Turns a topic or an uploaded document into a generated lesson in one click: slides, quizzes, HTML simulations and project-based-learning scenes, delivered by AI teacher *and* AI classmate agents over a shared whiteboard with text-to-speech. Exports PPTX and interactive HTML. v1.2.0-rc.1 (2026-10-04) moves to a **server-first architecture with PostgreSQL persistence**, so a course generation survives a closed browser tab or a server restart. Integrates with agent workbenches (OpenClaw), so a classroom can be generated from a chat client or an IDE. TypeScript / Next.js / React. |
| AI-Teaching-Agent | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** (`LICENSE`, © 2026 littlecookie) | **0** | Turns Markdown teaching sources into **linked lab, exam and grading artefacts** through a structured DSL validated against JSON Schema. Three properties matter more than its star count: a **`WAITING_REVIEW` human-approval gate** before anything is published, **sandboxed grading execution with evidence generation**, and a **candidate-facing exam preview that strips answers and internal grading references**. CLI/JSON plus an MCP server; local-first, offline demo needs no API key. Python. |
| pedagogy-benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** (`LICENSE`) | 12 | Benchmarks the **pedagogical knowledge** of LLMs using real **teacher-qualification exam questions** — not task accuracy, but whether the model knows how to teach. Python. The only pedagogy-specific model-selection instrument on this shelf. |
| edu-qurating | [AI-for-Education/edu-qurating](https://github.com/AI-for-Education/edu-qurating) | **MIT** (`LICENSE`) | 3 | Educational content curation / quality-rating tooling. Python. |
| voice-ai-evaluation-framework | [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | **MIT** (`LICENSE`) | 1 | Evaluation harness for **voice-based** AI systems — the modality that matters where literacy and device constraints bind. Python. |

**Read the star counts honestly.** OpenMAIC at 40.0k is a flagship. The other four
are **1–12★ research-grade code**. They earn their rows because they are the only
permissive assets this KB has found for *pedagogical model selection*, *voice
evaluation* and *gated grading* — three functions the shelf had no entry for at
all. Treat `AI-Teaching-Agent` (0★, no releases) as a **reference architecture to
read and re-implement**, not a dependency to pin.

#### Why `AI-for-Education` is the most strategically placed find in this KB

It is a GitHub organisation whose stated mission is to **democratise access to AI
in education in low- and middle-income countries**, and its repositories are
**placed in named countries**: a lesson-plan parser built for **Sierra Leone's
MBSSE** (Ministry of Basic and Senior Secondary Education), and
**Luganda linguistic benchmarks** for **Uganda**. Through three passes this KB
recorded Africa as "almost entirely uncovered, greenfield, no deployed open source
African education AI shelf to recommend from." **That gap is now narrowed to a
specific, MIT-licensed, ministry-engaged starting point** — small, but real and
placed. See `intel/market.md`.

#### Licence flags from this pass — two assets you cannot ship

| Asset | Claim | What the payload actually says |
|---|---|---|
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | Its **EACL 2026 demo paper** describes it as "the first open-access, open-source model for pedagogical quality evaluation of AI tutor responses, released under an **MIT** license" | **No `LICENSE` payload exists.** `README.md` returns 200 on both `main` and `master`; `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` all **404 on both branches**. The repository is real and the paper is peer-reviewed, but **the grant is in the PDF, not in the repo** — so it is legally unlicensed, which is the worst state for client work. Its evaluation framework (MI = Mistake Identification, ML = Mistake Location, PG = Providing Guidance, AC = Actionability) is worth re-implementing; the code is not worth shipping until a `LICENSE` lands. **Ask the author to add one** — this is a cheap, high-value upstream contribution. |
| Open TutorAI (arXiv 2602.07176) | "An open-source platform for personalised and immersive learning with generative AI" — LLM tutoring with customisable 3D avatars | **CC BY-NC-SA 4.0** — **non-commercial and share-alike.** Not usable in a client engagement at all, under any architecture. "Open source" in a paper abstract is not a licence. |
| [AI-for-Education/Luganda-linguistic-benchmarks](https://github.com/AI-for-Education/Luganda-linguistic-benchmarks) | sits in an organisation whose other five repos are all MIT | **No `LICENSE` payload** (`README.md` 200, `LICENSE` 404). **Per-repo probing is not optional even inside a uniformly-licensed org** — five MIT siblings do not license the sixth. |

**This is the fourth distinct failure mode the catalogue has recorded**, after the
unlicensed repo, the AGPL-plus-paid-tier side-car and the unenforceable prose
grant: **the licence that exists only in the paper.** A peer-reviewed claim of MIT
is evidence about intent, never about rights.

### Added in the fifth pass of 2026-10-06 — the first India-, ASEAN- and LATAM-origin permissive projects

**Channel new to this KB this pass:** **institution-first search** — searching by
funding body, ministry and university name in English and Spanish rather than by
GitHub topic or star count. Four passes of topic sweeps had concluded that India-,
ASEAN- and LATAM-origin permissive education projects did not exist. They do. They
were invisible to topic sweeps because **none of them has a single star**, and
three were created in 2026.

Every licence below was read from the repository's own `LICENSE` payload via
`raw.githubusercontent.com`. Star and commit counts were read from the repository
page the same day. **Read the maturity column before the licence column** — this
pass's finding is that region coverage is now achievable and that almost nothing on
it is production-grade.

| Agent | Repo | License (read from payload) | ★ / commits | Origin | Maturity | What it does |
|---|---|---|---|---|---|---|
| Shiksha Copilot | [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) | **MIT** (`main/LICENSE`, Microsoft Corporation) | 9★ / 149 commits | **India** — Microsoft Research India, VELLM initiative; classroom validation with the **Sikshana Foundation** | Working full-stack system; GPT-4o dependency acknowledged in its own README | Teacher-side lesson planning: select curriculum, grade, subject and chapter, then generate lesson plans, real-world examples, analogies, hands-on activities, and formative and summative assessments. Compiles reviewed output to **DOCX, PPT and student handouts**, and generates **multi-chapter question banks against standard blueprint formats**. React + FastAPI + Azure durable functions; textbook ingestion pipeline with **human curator oversight** |
| CurriculumCraft AI | [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) | **MIT** (`main/LICENSE`, 2026) | 0★ / 7 commits | **India** — individual, Hacktoberfest 2026 | Public beta, real TypeScript codebase | **CBSE / NCERT grades 9–12** assessment engine: tests, lesson plans and marking keys. Runs on **open-weight Gemma only** (`gemma-4-26b-a4b-it`, failover `gemma-4-31b-it`), temperature 0.2, no Gemini. Model calls routed through backend endpoints so API keys never reach the browser; IP rate limit of 30 requests per 5-hour window. Ships an explicit **copyright analysis**: no NCERT text is stored or reproduced, syllabi are treated as public standards, all items synthesised on demand |
| TutorIA | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | **MIT** (`main/LICENSE`, Grupo Sirius) | 0★ / 4 commits | **LATAM** — Universidad Tecnológica de Pereira, Sirius research group, **Colombia**; funded under Colombia's **SNCTI** | **Specification published, code not — corrected in the eighth pass.** `docs/` holds a **13-page MIT requirements spec (v1.0, April 2026)** and a 5-layer architecture diagram; the six code directories hold only `.gitkeep`. Earlier passes read this as "scaffold only" because they probed code filenames and never `docs/` | Specified as an autonomous tutor agent for **rural higher education in Risaralda**, delivered as an **Open edX XBlock/plugin** with Claude API, TTS audio replies, animated avatar, teacher statistics panel and cross-session context. Initial subjects: Programación I (Python) and Introducción a la Matemática. Named team includes a **dedicated pedagogical director** |
| Tutor Agente Local | [DannyAvilaL/agente_clases](https://github.com/DannyAvilaL/agente_clases) | **MIT** (`main/LICENSE`, 2026) | 0★ / 5 commits | Spanish-language, individual; **no institution or country stated in the repository** | Working single-author system | **100% offline** programming-class preparation: Ollama **Phi-3 (2 GB)** generates per-student explanations and exercises in Markdown, synthesises `.csv` datasets and injects them as tables into local **PostgreSQL**. Syncs Google Calendar into a **local Radicale CalDAV** server and keeps working with no internet. Streamlit dashboard; `cron` autopilot prepares classes a week ahead |
| EduFlow | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **see the holder warning below**) | 1★ / 41 commits | **LATAM** — Pontificia Universidad Católica de **Chile**, Centro de Alumnos de Ingeniería; HaCAIthon 2026, *Educación pública* track | **8-hour hackathon build with working code** — not a product; the only CAi UC education repo verified to contain a running backend and frontend | **Offline-first maths practice for schools with no reliable signal.** Teacher opens a room and shares a 6-character code; student downloads the assignment while in signal (**~8 KB for 10 exercises**), solves it **entirely offline** with immediate correction via **IndexedDB** + Service Worker app-shell cache, and answers **sync automatically** when connectivity returns. FastAPI backend (routers `auth`, `rooms`, `activities`, `answers`) + Next.js PWA + Supabase. Its README names **Kolibri** and **RACHEL** as prior art. **The concrete implementation of the constraint TutorIA's RNF-04 specifies and has no code for** |
| CPU-Benchmark | [caiuc/equipo-6-haCAIthon-2026](https://github.com/caiuc/equipo-6-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **holder warning below**) | 0★ | **LATAM** — PUC **Chile**, HaCAIthon 2026, *Educación y brecha digital* track | 8-hour build; `README.md` and devcontainer verified, no application code confirmed in-tree | Classifies **donated computers** by measuring their real performance, so a school receiving a hardware donation can tell what each machine is actually fit to run. The triage step in front of any low-resource deployment — the question TutorIA's **2 GB RAM / 3G** envelope assumes someone has already answered |
| OnlyUs | [caiuc/equipo-16-haCAIthon-2026](https://github.com/caiuc/equipo-16-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **holder warning below**) | 0★ / 50 commits | **LATAM** — PUC **Chile**, HaCAIthon 2026, *Educación y orientación* track | 8-hour build; `README.md` and `frontend/package.json` verified in-tree | Simulates the Chilean university application and suggests degree programmes the applicant's score actually reaches. Guidance and admissions rather than tutoring — the one education function in this KB with **no** other permissive entry |

#### TutorIA: read this before you cite it

TutorIA is the **first LATAM-origin permissive education project this KB
found**, and it is institutionally real — a named university, a named research
group, a named pedagogical director, and public science funding.

**⚠️ CORRECTED IN THE EIGHTH PASS (2026-10-06). Earlier passes described this
repository as "a README and a licence" with "every code path 404". The first
half was wrong.** The code claim holds — and is now explained — but the
repository also publishes a **complete requirements specification** that five
passes never probed, because every probe used a *code* filename.

| Probed path | Result | What it is |
|---|---|---|
| `backend/`, `frontend/`, `openedx/`, `data/`, `infra/`, `tests/` | **`.gitkeep` only** | Deliberately placeholder-reserved — which is *why* the code paths 404 |
| `backend/main.py`, `frontend/package.json`, `openedx/setup.py`, `docker-compose.yml`, `.env.example` | 404 | Unchanged from earlier passes |
| **`docs/TutorIA_Requerimientos.pdf`** | **200** | **13-page requirements specification, v1.0, April 2026** — RF-01…RF-20, RNF-01…RNF-10, actors, use cases |
| **`docs/tutoria_architecture.svg`** | **200** | **5-layer architecture**, 19 KB: Usuarios → Open edX LMS → API → Servicios Core → IA & Media |
| **`CONTRIBUTING.md`** | **200** | Contribution guide — also missed by the code-path sweeps |

**The four requirements worth lifting, all under MIT:**

- **RNF-05** — *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with **TLS**
  in transit and **AES-256** at rest as the acceptance criterion. This KB's
  **first Colombian data-protection anchor**; `Ley 1581` appeared nowhere in it
  before the eighth pass.
- **RNF-04** — *"mínimo **2GB de RAM**; funcional con conectividad de **3G**"*.
  A testable low-resource envelope, where this KB previously had adjectives.
- **RNF-09** — agent responses must pass pedagogical review by **at least 2
  subject-expert teachers per subject before launch**. Not an automated
  evaluator, so the standing evaluator gap is unchanged — but it is a **written
  human quality protocol with a quorum**, which is the thing an engagement can
  actually ship.
- **RF-02** (priority *Alta*) — *"**Todo** el código fuente, configuraciones y
  documentación base … deben publicarse en un repositorio de acceso público"*.
  **Unmet as of 2026-10-06.** This reframes TutorIA from an abandoned-looking
  repository into a **tracked commitment**: watch RF-02, and make RF-02 the
  subject of any approach to the Sirius group.

**RNF-10** specifies Colombian Spanish for v1.0 *"con posibilidad futura de
soportar lenguas nativas"* — the layer the eighth pass found is almost entirely
**unlicensed** (see the LATAM substrate shelf in `repos/trending.md`).

Its own quickstart tells you to clone a **different repository**
(`Sof1SP/tutorIA`) from the one the README lives in — MIT © **Sofia Soto
Parra**, containing only `README.md` and `LICENSE`. Two locations, two
copyright holders, zero code. So: **cite TutorIA for its specification, which is
genuinely reusable and the most complete LATAM education-AI design document in
this KB; cite it as a partnership lead; and do not present it as a codebase you
can fork.** The
architecture it specifies — Open edX XBlock, side-car agent, teacher analytics —
is exactly pattern **P1** in this KB, which is the useful part: a Colombian public
university has independently specified this KB's default engagement shape and has
not built it.

#### What these four rows change, and what they do not

- **Three declared gaps move from "open" to "open at a different size."** This KB
  has recorded "no India-origin", "no ASEAN-origin" and "no LATAM-origin"
  permissive education project as its firmest findings, across four independent
  channels. All three were **artefacts of star-ordered discovery**. An
  institution-first search found all three in one pass.
- **Nothing here is a product shelf.** Three of the four rows have **0★**. The
  India row with institutional weight — Shiksha Copilot — has **9★ and 12 forks**.
  Globant cannot shop from this shelf; it can **partner** (MSR India, UTP
  Colombia, NUS) or **re-implement**.
- **Curriculum alignment is no longer China-only.** Before this pass,
  `Zenglian990/AI_Tutor_Release` (Chinese grade 1–9) was the only
  curriculum-aligned permissive tutor in this KB. CurriculumCraft AI adds
  **CBSE/NCERT grades 9–12**, and does it on **open-weight models only** — which
  makes it the first curriculum-aligned permissive asset here that is also
  deployable in a sovereignty-constrained engagement.
- **Two of them are built against the copyright problem, not around it.**
  CurriculumCraft's synthetic-generation argument and Shiksha Copilot's
  human-curator ingestion gate are both answers to the question every ministry
  engagement asks in week one. Reuse the arguments even where you do not reuse the
  code.

#### Measured rejections from the same sweep

Recorded so the absence is visible rather than silent.

| Candidate | Why it is not in the table |
|---|---|
| [vitorr2101/Projeto-Agente-IA-Educacional](https://github.com/vitorr2101/Projeto-Agente-IA-Educacional) | **Brazil-origin and therefore the row this KB most wanted** — and it has **no `LICENSE` payload** on `main` or `master` across five filenames. No rights, no row |
| "K.A.L.I." (described in search results as a sovereign AI learning engine with 3D logic visualisation) | **Could not be located.** A targeted search returned ten unrelated `sovereign`-named repositories and no K.A.L.I. Not recorded — an unverifiable name is not a finding |
| AICET's Codaveri, Softmark, ScholAIstic (NUS / AI Singapore) | **Closed source.** See the ASEAN note below — the mature ASEAN education AI is not open, but its host platform is |

#### The ASEAN finding is a platform, not an agent

Singapore has the most operationally mature education AI in APAC and almost none
of it is open. **AICET** — the AI Centre for Educational Technologies, hosted by
AI Singapore, funded by the Smart Nation and Digital Government Office, working
with Singapore's **Ministry of Education** — ships three products at real scale:
**Codaveri** (programming tutor, 30,000+ pieces of personalised feedback since
2024), **Softmark** (exam-script digitisation and concurrent team marking, 70,000+
scripts in 2025, now with computer-vision grouping of similar answers) and
**ScholAIstic** (multi-agent platform for educator-authored specialised chatbots,
deployed across Social Work, Law and Nursing at NUS since June 2024). **None has a
public repository.**

What is open is the platform underneath Codaveri:
[**Coursemology/coursemology2**](https://github.com/Coursemology/coursemology2) —
**MIT, read from `master/LICENSE` (Coursemology.org)**, 158★, 78 forks, 15,802
commits, Rails 8 + React, NUS-origin and "currently supported by the AI Centre for
Educational Technologies." It is recorded in `repos/foundations.md` and
`verticals/solutions.md` rather than here, because it is an LMS and that decides
how you deliver it. **The ASEAN gap was never that ASEAN lacks education AI. It is
that ASEAN's mature education AI is closed and its substrate is MIT** — which is a
much better commercial position than the gap this KB had recorded.


### Added in the sixth pass of 2026-10-06 — no new agents, and the layer that unblocks a whole class of them

**State the negative first: this pass added no new education agent to the table
above.** It swept the **speech and low-resource-language substrate** instead — 26
repositories probed, 26 resolved — and that shelf lives in
`repos/foundations.md`, not here, because none of it is an agent.

What it changes for this file is **what the agents above can now be composed
into.** Every tutor in the table is text-only and English-first by default. With
the sixth-pass shelf, three agent shapes stop being blocked on a proprietary API:

- **The speaking tutor.** [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)
  (**Apache-2.0**, 15.1k★) delivers STT, TTS, diarization and VAD **in one
  permissive tree, with no Internet connection**, on Android, iOS, Raspberry Pi
  and RISC-V. Voice tutoring on classroom-grade hardware is now a permissive
  build, not a vendor dependency.
- **The mother-tongue tutor, in two regions only.** India via
  [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) (**MIT**, 22 scheduled
  languages), [Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) (**MIT**, 13
  languages) and [IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec)
  (**MIT**, ASR); Uganda and Africa via [SunbirdAI/salt](https://github.com/SunbirdAI/salt)
  (**Apache-2.0**, studio-recorded TTS in six Ugandan languages) and
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**).
  **Outside those two, the permissive language layer does not exist** — see
  `intel/market.md`.
- **The human-in-the-loop stage, finally with a tool.** Every pattern in this KB
  specifies teacher review; [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya)
  (**MIT**) is the first shelved implementation of it — *"an open source platform
  to annotate and label data at scale."*

**Three traps on that shelf are recorded here because they will be proposed as
agent components.** Full write-ups in `repos/foundations.md`:

| Component | Why it gets refused |
|---|---|
| [rhasspy/piper](https://github.com/rhasspy/piper) | **MIT** but **archived read-only 2025-10-06**; development moved to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl), which is **GPL-3.0**. The obvious offline-TTS pick is **either frozen or copyleft, never both permissive and maintained** |
| [facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication) | **CC BY-NC-4.0** in `main/LICENSE` — **non-commercial. Hard reject** for anything billable, and it is the top result for "open source multilingual speech" |
| [aisingapore/sea-lion](https://github.com/aisingapore/sea-lion) | **No `LICENSE` payload at all.** Its README defers the grant to each HuggingFace **model card** because terms *"may vary depending on the underlying base model's restrictions"*. **A sixth licence failure mode: the licence belongs to the checkpoint, not the project** |

### Declared gap, sixth pass — the oral reading fluency agent does not exist

Searched specifically for a permissive **oral reading fluency** assessor — a child
reads aloud, the system returns words-correct-per-minute. It is the
highest-volume literacy measurement in primary education and the most natural
application of the shelf above.

**Nothing permissive was found.** The category is entirely proprietary: **FLORA**,
**Literably** (IES-funded), Amplify **Text Reading Online**, **SoapBox Labs** — no
public repository for any of them; an Italian ASR fluency app implementing the
Cornoldi MT battery exists only as a paper. What *is* public is the **Ghana ORF
Dataset** — 130 students aged 9–18, passages, audio and human transcriptions, with
**Whisper V2 measured at 10.3% WER** on Ghanaian students reading aloud (*IJAIED*,
[10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)).

**This is the sharpest build opportunity in the KB:** permissive components all
present ([whisperX](https://github.com/m-bain/whisperX), BSD, for the word-level
timestamps that make fluency measurable; [faster-whisper](https://github.com/SYSTRAN/faster-whisper),
MIT, for the transcript), a public dataset, a published accuracy baseline to beat,
and no open competitor. Wired up as **P17** in `compose/patterns.md`.

### Added in the seventh pass of 2026-10-06 — a shelving audit, and the first Korea-origin permissive asset

**Channel new to this KB this pass: native-language search** (Japanese, Korean,
Arabic, Bahasa/Thai/Vietnamese). Earlier passes searched English, then Spanish
and Portuguese. The language substrate it turned up is in
`repos/foundations.md`; what it changes *here* is smaller and more awkward.

**The awkward part first: this file was behind its own trending log.** Five
permissive education MCP servers had been probed and verified by earlier passes
and recorded in `agents/trending.md` — and **never added to the shelf table
below**, which was still the Canvas/Moodle/Anki set. They are now in it, each
re-probed from payload this pass rather than trusted from history. One of them,
`toshieji/moodle-grading-mcp`, **refutes a gap this file was still asserting two
sections above** (see the gap updates at the end).

**The lesson is a maintenance one, and it has now bitten twice.** `repos/trending.md`
recorded the same failure in the sixth pass — *"a 38,046-commit MIT platform this
KB found and then forgot to shelve."* A finding recorded only in an append-only
log is **discoverable but not usable**: nobody scoping an engagement reads 13,000
lines of pass history. **A pass is not finished when the trending entry is
written; it is finished when the shelf, the gap list and the patterns agree with
it.** This pass added a consistency sweep across those four surfaces, and it
found two contradictions in this file alone.

#### The Korea finding, stated at its real size

[yongsoojoo/esd2026-agent-workflow](https://github.com/yongsoojoo/esd2026-agent-workflow)
— **MIT for code, CC BY 4.0 for documentation** (`main/LICENSE` read from
payload, © 2026 Yongsoo Joo), **0★ / 0 forks / 4 commits**, HTML static site.
Course material for *임베디드시스템설계 2026-2* (Embedded Systems Design) at
**Kookmin University**, Seoul: an AI-agent configuration-management tutorial
covering git, AI tooling and Raspberry Pi setup, written by the instructor
jointly with an AI coding agent.

**This is the first Korea-origin permissive education asset in seven passes, and
it is not an agent.** It is an enablement artefact — the same category as the
Microsoft and Hugging Face courses, at 1/10,000th the scale. Recording it
honestly:

- **Closed:** "no Korea-origin permissive education *asset*." One exists, from a
  named university, with a clean dual grant.
- **Still open:** "no Korea-origin permissive education *agent*." Nothing
  changed. And Korea is the jurisdiction with the **AI Framework Act in force
  since 22 January 2026**, so the mismatch between regulatory maturity and open
  supply is the widest of any market in this KB.
- **Worth noting for enablement work:** the **code/docs split grant** (MIT + CC
  BY 4.0) is the correct licensing shape for a teaching artefact, and almost
  nothing else in this KB's teaching-content shelf gets it right.

#### Measured rejections from the native-language sweep

| Candidate | Channel | Why it is not in a table |
|---|---|---|
| [781991937/TOFAN-AI-2026](https://github.com/781991937/TOFAN-AI-2026) | Arabic | **No `LICENSE` payload** (2 branches × 6 filenames). The most substantial Arabic-language education agent found in any pass — *"مساعد تعليمي ذكي"*, ingests lesson files, extracts and analyses content, generates summaries and interactive tests; FastAPI backend with a PWA/Web-App front end, explicitly not a Telegram bot. **Real, well-shaped, and legally unusable.** The single highest-value upstream ask in this KB right now |
| [biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | function-scoped (proctoring + grading) | 🔴 **THIS VERDICT WAS WRONG — corrected in the thirty-third pass, 2026-10-07. The repo is `MIT`**, read from payload at **`master/LICENSE`, 1068 B, © 2026 Prem Biswal**, and its README carries an `MIT` badge on line 5. The repo has **no `main` branch at all** (`main/README.md` → 404, `master/README.md` → 200, 26560 B), so a `main`-first probe files it as absent. It is now shelved as a live row above. The original verdict, left standing so the correction is legible, read: **No `LICENSE` payload.** *"A fully local, mathematics-driven AI exam system for autonomous proctoring, explainable cheating-risk prediction, automated grading and student performance analysis — with no external AI APIs."* Fully local and explainable is exactly the shape Annex III and Vietnam's Decree 33 reward. No grant, no row |
| [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | GitHub weekly trending | 🟢 **NCSA** (code) **+ CC-BY-4.0** (generated PDFs) — grants live in a `LICENSE/` **directory**, so the rooted probe that first reported **"No `LICENSE` payload"** here was looking at the wrong level (`p441`, pass 26). ⚠️ **And the family is NCSA, not MIT** (corrected in the twenty-seventh pass): the University of Illinois/NCSA licence **contains MIT's grant sentence verbatim**, so a classifier probing for that sentence returns MIT. The repository's own `LICENSE/README.md` says *"licensed under the University of Illinois NCSA license under LICENSE.code"*. 🔵 **NCSA is a licence family new to this KB.** An open systems-programming textbook from **UIUC** that gained **~1,626★ in one week** — the highest-velocity education repository seen in any pass of this KB. A university's own trending course text, with no grant attached |

**The Arabic result is the one to act on, and it is a regional finding.** MEA is
the only region in this KB with **zero shippable permissive education assets**:
the fourth pass's Africa shelf (`AI-for-Education`, MIT, Sierra Leone and Uganda)
is research-grade at 1–12★, `Luganda-linguistic-benchmarks` is unlicensed, and
now the one real Arabic-language education agent is unlicensed too. **The MEA gap
is not an interest gap and not a build gap — it is a licensing-hygiene gap**, and
that is the cheapest kind to close. Three `LICENSE` files would change the
regional answer.

### Added in the ninth pass of 2026-10-06 — permissive proctoring, a gap this KB asserted for two passes

Channel: the **funder and procurement channel**, and a **licence-filtered
re-probe** of a gap the seventh pass declared and the eighth carried forward
explicitly marked *"not re-probed."* It was re-probed. **It was wrong.**

A search for `exam proctoring license:mit` returns **204 repositories**. Four,
licence read from payload:

| Agent / tool | Repo | Licence | ★ | What it does |
|---|---|---|---|---|
| exam-cheating-detection | [AarambhDevHub/exam-cheating-detection](https://github.com/AarambhDevHub/exam-cheating-detection) | **MIT** (`main/LICENSE`) | 47 | Computer-vision detection of suspicious exam behaviour: eye-movement tracking and face detection |
| Proctored-MCQ-Exam-Platform | [vincenzo-afk/Proctored-MCQ-Exam-Platform](https://github.com/vincenzo-afk/Proctored-MCQ-Exam-Platform) | **MIT** (`main/LICENSE`) | 36 | Browser-based MCQ exam platform with camera monitoring and certificate generation |
| MyProctorAI | [hemantkarekar/MyProctorAI](https://github.com/hemantkarekar/MyProctorAI) | **MIT** (`main/LICENSE`) | 22 | Flask portal: AI anti-cheating proctoring and invigilation system |
| Exam_Intellect | [RakeshBabuGajula/Exam_Intellect](https://github.com/RakeshBabuGajula/Exam_Intellect) | **MIT** (`master/LICENSE`) | 18 | Live exam observation dashboard; CV + speech recognition with automated feedback |

#### Read this shelf at its real size

**Existence is refuted; maturity is not.** The set tops out at **47★**, all four
are individual- or student-scale projects, **none has an institutional
maintainer**, and the only framework-grade implementation in the sweep —
[lebmatter/exampro](https://github.com/lebmatter/exampro), **72★**, *Proctored
Exams for Frappe Framework* — has **no licence payload** across 8 filenames × 2
branches. That is the sixth consecutive pass in which the most-adopted asset of
a sweep turned out to be the ungranted one.

**So the claim to make to a client is narrow and true:** a permissive proctoring
core exists and can be vendored and hardened, but there is no permissive
proctoring *product*, and anything client-facing is a build on top of a 20–50★
starting point. **Do not quote these as production components.** And before
proctoring enters any proposal, read the regional constraint: proctoring is
biometric processing, which puts it in scope for Annex III in the EU, for the
state-level rules in the US recorded in `intel/market.md`, and for age-gating in
the UAE/China shape of pattern P9.

#### Measured rejections from the same sweep

| Repo | ★ | Why rejected |
|---|---|---|
| [lebmatter/exampro](https://github.com/lebmatter/exampro) | 72 | **No licence payload** — `LICENSE{,.md,.txt}`, `COPYING`, `LICENCE{,.md,.txt}`, `COPYRIGHT` × `main`/`master` all 404 |
| [AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) | 33 | **No payload.** Chinese K12 LLM education-evaluation benchmark — APAC's own evaluation asset, ungranted |
| `ubco-db/LLM_education_benchmark` | 2 | **No payload** |
| `OpenEduTech/EduPerf` | 6 | **No payload**; last updated November 2022 |
| `National-Tutoring-Observatory/National-Tutoring-Observatory.github.io` | 0 | **No payload** — and it is a *funded grantee's* only substantive repo (see gap updates below) |

## The education MCP shelf — a side-car is permissive by choice, not by construction

The licence-boundary note below says an external MCP side-car keeps its permissive
licence while an in-tree plugin inherits copyleft. True of the canonical servers,
but it is the *author's* choice, not a property of the architecture. Every Canvas
and Moodle MCP server that surfaces in search was probed on 2026-10-06:

| Repo | ★ | Licence (read from payload) | Verdict |
|---|---|---|---|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 278 | MIT (`LICENSE@main`) | **Canonical Canvas side-car. Use this.** |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | ~42 | MIT (`LICENSE`) | **Canonical Moodle side-car. Use this.** |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 103 | **NONE** | **Do not use.** 54 working tools, v2.3.0, no `LICENSE` on any branch and no licence statement in the README. |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | 38 | **NONE** | **Do not use.** No `LICENSE` on any branch, none in README. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 1 | **AGPL-3.0** (`LICENSE@main`) | Avoid: AGPL **and** a paid premium-plugin upsell. |
| [CharlieCardenasToledo/mcp-canvas-server](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | 0 | MIT (`LICENSE@main`) | Usable, unproven. README claims 117 tools / 21 categories while the repo description says 51 — its own numbers disagree. |
| [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | 0 | MIT (`LICENSE@main`) | Usable, unproven. Only Go implementation found. |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **506** | MIT (`LICENSE`) | **The biggest one, and it is not an LMS server.** 53 tools (42 essential + 11 GUI), v0.27.0 beta, TypeScript. Added third pass 2026-10-06. Needs the Anki desktop app **plus AnkiConnect**. |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 43 | MIT (`main/LICENSE`, © 2026 Arnaud Guiovanna) | **The pedagogy engine as a side-car — the most architecturally significant row in this table.** Go, v0.6.1, 456 commits, 6 forks. Its own description: *"An open-source MCP server that turns any LLM into an Intelligent Tutoring System. 50 years of cognitive science, MIT licensed."* Implements **BKT** mastery estimation, **FSRS** spaced repetition, prerequisite-based paths, assessment-evidence tracking, misconception memory and session narrative, exposed through `get_next_activity` / `record_interaction`. **Added to this shelf in the seventh pass — see below.** |
| [Yuanpeng-Li/gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) | 8 | MIT (`main/LICENSE`, © 2026 Yuanpeng Li) | **The only MCP over a real production grading system.** Python, 82 commits, 6 forks. **39 tools** (24 read-only, 11 write-enabled, 4 local-cache), 3 resources, 7 prompts: batch grading with preview-first safety, rubric CRUD, answer-group clustering, regrade review, extension management, Canvas/Brightspace gradebook export. Small, and the strategic point is the direction — **orchestrate the proprietary incumbent, do not promise to replace it.** |
| [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) | 0 | MIT (`main/LICENSE`, © 2026 **Web Analytics Consultants Association (WACA)** and Toshiaki Ejiri) | **The human-gate reference implementation, and the row that refutes this KB's Japan gap.** 9 tools, Python, stdio. Its own description: *"The LLM client decides the grades; this server only fetches submissions and writes grades as unreleased drafts."* Writes `workflowstate=readyforreview` and **never releases a grade**; writes require `MOODLE_ALLOW_WRITE=1` **and** a non-empty `MOODLE_WRITE_COURSE_ALLOWLIST` (empty list = fail-closed, no write); every attempt, denial and success appended to a **JSONL audit log**; AI-disclosure footer appended if missing; draft state means **no student notification**. |
| [woodstocksoftware/student-progress-tracker](https://github.com/woodstocksoftware/student-progress-tracker) | — (not read this pass) | MIT (`main/LICENSE`, © 2026 Jim Williams) | Learning-analytics side-car: learner profiles and enrolments, assessment results, **mastery computed per topic**, learning-gap detection, focus-area recommendation, question-level telemetry. The analytics stage P3 specifies. |
| [54yyyu/school-mcp](https://github.com/54yyyu/school-mcp) | — | **NONE** — MIT claimed in the README only | **Do not use as-is.** Canvas **and** Gradescope in a single server, which is the shape a student-facing agent actually wants. **Independently re-probed this pass: no `LICENSE` payload on 2 branches × 6 filenames**, confirming an earlier pass's flag. The README's "MIT" is not a grant. **Cheapest high-value upstream contribution on this shelf: ask for a `LICENSE` file.** |

**The shelf above was scoped wrong, and the third pass of 2026-10-06 proves it.**
It was assembled by sweeping *Canvas and Moodle* MCP servers — a scope defined by
LMS vendor name. The highest-starred education MCP server in existence is
`ankimcp/anki-mcp-server` at **506★**, which is **1.8× `vishalsachdev/canvas-mcp`**
and was invisible to every earlier sweep because it serves the **retention** layer
rather than the LMS layer.

It also confirms the licence boundary on a second, unrelated platform family:
**Anki itself is AGPL-3.0, and its MCP side-car is MIT.** The side-car keeps its
permissive licence across an AGPL host exactly as it does across GPL-3.0 Moodle.

**Scope the next sweep by learning *function*, not by vendor name:** LMS, SIS,
retention and spaced repetition, assessment, library, proctoring, video. Each is a
separate MCP shelf and this KB has now swept two of them.

**Seventh pass of 2026-10-06 — that instruction was carried out, and the table
above grew by five rows.** Sweeping by function rather than vendor name returned
the **tutoring-engine** function (`tutor-mcp`), the **grading** function
(`gradescope-mcp`, `moodle-grading-mcp`) and the **analytics** function
(`student-progress-tracker`) — three shelves no vendor-name sweep could have
reached, because none of those servers is named after an LMS. **Four of the five
are MIT from payload; the fifth claims MIT in a README and has no grant.** Still
unswept: **library** and **video**. And the function with the sharpest commercial
edge, **proctoring**, was swept and came back empty of anything licensed — see
the new declared gap at the end of this file.

**An unlicensed repo is worse than a copyleft one.** AGPL-3.0 is a constraint you
can architect around. No licence at all means default copyright — all rights
reserved, no grant to use, modify or redistribute. `DMontgomery40/mcp-canvas-lms`
is the trap: 103★ and 54 tools make it look mature, and it cannot legally ship in
a client deliverable. Probe the licence before the feature list.

Two further forks of the canonical Canvas server carry byte-identical
descriptions and the same MIT licence with none of the history:
[abr-Projects/canvas-mcp](https://github.com/abr-Projects/canvas-mcp) and
[BartMassey-upstream/canvas-mcp](https://github.com/BartMassey-upstream/canvas-mcp).
Pin `vishalsachdev/canvas-mcp`.

## The license boundary that decides your architecture

This is the single most reusable finding in this KB, and it is measured, not
inferred:

| Piece | Where it runs | License read from payload |
|---|---|---|
| [Limekiller/moodle-block_openai_chat](https://github.com/Limekiller/moodle-block_openai_chat) | in-tree Moodle plugin | GPL-3.0 |
| [yedidiaklein/moodle-local_aiquestions](https://github.com/yedidiaklein/moodle-local_aiquestions) | in-tree Moodle plugin | GPL-3.0 |
| [cgrevisse/moodle-qbank_genai](https://github.com/cgrevisse/moodle-qbank_genai) | in-tree Moodle plugin | GPL-3.0 |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | external process, talks to Moodle over its web API | **MIT** |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | external tool provider | **Apache-2.0** |

**Consequence:** AI built *inside* a copyleft LMS inherits that LMS's license.
The same capability built as an external service reached over LTI 1.3 or MCP
stays permissive and stays reusable across client engagements. Prefer the
side-car. This drives pattern P1 in `compose/patterns.md`.

## Corrections to earlier passes

- **RESOLVED: `OpenMAIC-Brasil` was a phantom, and the real OpenMAIC is a
  40.0k★ MIT project from Tsinghua.** Through three passes this KB recorded
  [planejaia/OpenMAIC-Brasil](https://github.com/planejaia/OpenMAIC-Brasil) as "a
  confident search result for a repository that genuinely does not exist" and used
  it as the lead evidence for the **no-LATAM-origin-education-agent** gap. Both
  halves of that now have a better answer.

  **Re-probed 2026-10-06 (fourth pass), the Brazilian repo is still gone:**
  `README.md` and `LICENSE` return **404 on all four** candidate branches
  (`main`, `master`, `develop`, `v1.0.0`). That claim stands, now on a fourth
  independent probe.

  **But the name was never Brazilian.** The upstream is
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — *Open Multi-Agent
  Interactive Classroom* — **MIT, 40.0k★, from Tsinghua University**, v1.2.0-rc.1
  dated 2026-10-04. The "Brazil-origin multi-agent classroom with a v1.0.0
  release" that search results kept asserting was almost certainly a **vanished
  fork or mirror of a Chinese project**, mis-attributed by its `-Brasil` suffix.

  **Two lessons, and the second is the expensive one.** First: when a probe 404s,
  search for the *upstream of the name* before recording a gap — this KB spent
  three passes treating an absence as evidence while a 40k★ MIT implementation of
  the same thing sat one query away. Second: **a repository name is not a
  provenance claim.** A `-Brasil`, `-India` or `-LATAM` suffix is a string an
  author chose; regional attribution has to come from the owner, the commit
  history or the README, never from the slug. This KB's LATAM gap was argued
  partly from a suffix.
- **AutoGen is no longer a starting point.** [microsoft/autogen](https://github.com/microsoft/autogen)
  (61.3k★) is explicitly in **maintenance mode**: *"AutoGen is now in maintenance
  mode. It will not receive new features or enhancements and is community managed
  going forward. New users should start with Microsoft Agent Framework."* Its
  `LICENSE` at HEAD is now **CC-BY-4.0** (the repo is dual CC-BY-4.0 / MIT), not
  the plain MIT recorded in earlier cycles. Earlier education cycles listed
  AutoGen as a top agent at ~60k★ — that recommendation is withdrawn in favour of
  MAF.
- **OpenTutor is REINSTATED. The withdrawal recorded earlier on 2026-10-06 was
  itself wrong, and this is the most important correction in this KB.**
  Cycle 3 recorded *"OpenTutor (MIT, ~900★, FSRS6 + KG + 12 blocks)"*. The second
  pass of 2026-10-06 withdrew that entry after probing
  [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) — 8★, 5 commits,
  no `LICENSE` on three branches across eight filename variants and none in its
  README — and concluded the project did not exist as described.

  **It does.** The project cycle 3 meant is
  [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor), probed directly on
  2026-10-06: **MIT** (read from `LICENSE`), **130★ / 27 forks**, Python,
  **12 composable learning blocks**, a **LOOM** concept-mastery and prerequisite
  graph, **FSRS 4.5** spaced-repetition scheduling, local-first with 10+ providers
  and an Ollama default, FastAPI + Next.js. Cycle 3 was right about every
  architectural claim — 12 blocks, knowledge graph, FSRS, MIT — and wrong only on
  the star count (~900 claimed, 130 actual) and the FSRS version (6 claimed, 4.5
  actual).

  **The lesson is new and it cuts the other way from every other licence lesson
  here.** The rest of this KB's probe discipline guards against *false positives* —
  a repo that looks licensed and is not, or looks MIT and is AGPL. This was a
  **false negative that deleted a true finding**, and it cost more than any false
  positive recorded here: a correct entry was removed and replaced with a confident
  denial. A 404, or an unlicensed verdict, on `owner/name` is evidence about **that
  owner's repository only** — never about the project. `OpenTutor` resolves to at
  least three distinct things: `zijinz456/OpenTutor` (MIT, 130★), `tutornew/OpenTutor`
  (unlicensed, 8★) and the unrelated Open TutorAI arXiv work.

  **Therefore: a withdrawal requires a stronger probe than an addition.** Before
  removing an entry, enumerate the owners publishing under that project name. An
  addition that is wrong wastes a probe next pass; a withdrawal that is wrong
  destroys knowledge and is believed. OATutor
  ([CAHLR/OATutor](https://github.com/CAHLR/OATutor), MIT, 264★, UC Berkeley)
  remains a separate project from all of them.
- **DeepTutor's canonical repo is `HKUDS/DeepTutor`.** Searching for it surfaces
  forks and mirrors first: `cloudtoolbox/deeptutor` (7★), `lucadeg/DeepTutor` and
  `q-qp-p/HKUDS-DeepTutor` all carry the same description and the same Apache-2.0
  license but none of the history. Pin the HKUDS origin.

## Declared gaps — searched this pass, nothing found

An informed gap is information; silence looks exactly like coverage.

- **NARROWED AGAIN (fourth pass, 2026-10-06): the gated-grading architecture now
  has a permissive reference implementation — with 0 stars.**
  [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
  (MIT) implements exactly the shape every regulator in this KB demands: a
  `WAITING_REVIEW` human-approval gate, sandboxed grading with evidence output,
  and an answer-stripped candidate view. **What is still missing is adoption, not
  design** — 0★, no releases, one author. So the gap changes character: it is no
  longer "nobody has built this", it is **"nobody has built this at production
  maturity"**. Read it, re-implement the gate, do not pin it.
- **NEW GAP, precisely sized (fourth pass): pedagogical evaluation is published but
  unlicensed.** `AITutor-EvalKit` (EACL 2026) is the one purpose-built instrument
  for scoring *tutoring quality* rather than answer accuracy, and it has **no
  `LICENSE` payload**. There is therefore **no shippable permissive tutor-quality
  evaluator** on this shelf. `AI-for-Education/pedagogy-benchmark` (MIT, 12★)
  covers the adjacent question — which model knows how to teach — but it scores
  **models against exam questions, not live tutor dialogue**. The evaluation gap
  is now split in two, and only the model-selection half is closed.
- **STILL OPEN after a fourth channel: no LATAM-origin permissive education
  project.** This pass searched in Spanish and Portuguese (`Brazil Mexico Chile
  open source educación IA agente github repositorio tutor 2026 MIT`) — a
  **language channel no earlier pass had used** — and returned **zero
  LATAM-origin projects**; the results were the same China-, India- and
  US-origin repositories already recorded. Four independent channels (the
  `education-ai` topic, the `ai-tutor` topic, a stars-sorted search, and now a
  Spanish/Portuguese-language search) agree. **And the single strongest piece of
  evidence for this gap has been withdrawn as unsound** — `OpenMAIC-Brasil` was a
  name, not a Brazilian project (see corrections). The gap survives its own best
  evidence being removed, which is what makes it the firmest finding in this KB.
- **No India-, Japan-, Korea- or ASEAN-origin permissive education project —
  unchanged, and now searched by name.**
  **⚠️ ALL FOUR CLAUSES NOW SUPERSEDED. India and ASEAN were refuted in the
  fifth pass (table at the end of this file); Japan and Korea in the seventh.**
  This bullet is left standing because it was wrong on all four and the shape of
  the error is worth keeping: every refutation came from a **new channel**, never
  from a deeper sweep of the old one.
  Original text follows. This pass queried those four
  jurisdictions explicitly and surfaced only China/Hong-Kong-origin assets plus
  the US- and Europe-origin research code above. OpenMAIC (Tsinghua) **widens the
  China lead rather than closing this gap**: the APAC shelf is still
  China-plus-Hong-Kong, now with a 40k★ flagship at its centre.
- **NARROWED on 2026-10-06 (third pass): a permissive auto-grader exists, but not
  a standalone academic one.** Every earlier pass recorded a flat "no permissive
  open source auto-grader exists". That claim is now too broad.
  [Selleo/mentingo](https://github.com/Selleo/mentingo) — **MIT**, read from
  payload, 91★ — states in its own README: *"Grade open-ended answers without an
  L&D queue. Behavioural and problem-solving tasks are analysed automatically and
  returned with actionable feedback."* It also traces every model call through
  **Langfuse**, so the grading decisions are inspectable for cost, latency and
  actual output.

  The precise state of the gap:
  - **Exists:** MIT-licensed automated grading of open-ended *behavioural and
    problem-solving* tasks, inside a full self-hosted LMS built for **corporate
    L&D** — plus a traced audit path over it.
  - **Still missing:** a standalone permissive grader for *academic* assessment,
    and anything curriculum- or rubric-aligned for K-12 or higher-ed exams.
  - **Unchanged:** the oversight requirement. EU AI Act Annex III, the Oklahoma and
    Maryland statutes and Korea's high-impact classification do not care what
    licence the grader carries. **Keep the human gate on any consequential score.**
    What moved is the build-vs-adopt answer for L&D work, not the compliance
    answer — and in an engagement that distinction is worth stating out loud,
    because a client who hears "an open source auto-grader exists" will hear
    "we can skip the review step".
- **No LATAM-origin open source education agent found — re-probed 2026-10-06 with
  evidence.** Chamilo has deep Spanish-language and LATAM deployment but is
  EU-origin and GPL-3.0. The regional opportunity is deployment and localisation,
  not upstream code. Two probes this pass:
  - A search surfaced `planejaia/OpenMAIC-Brasil` ("Open Multi-Agent Interactive
    Classroom", described as v1.0.0 released 2026-08-27). It is **unreachable**:
    `raw.githubusercontent.com` 404s for `README.md`, `LICENSE`,
    `requirements.txt` and `package.json` across `main`, `master`, `dev` and
    `develop`, and the repository page returns **HTTP 404**. Deleted, renamed or
    private. A search hit is not a repository.
  - The `education-ai` GitHub topic, swept in full, contains **no LATAM-origin
    project at all**. Its long tail is Chinese (`ASEpochs/ai-digital-teacher`,
    `SimonsTang/*`, `upstream1119/Traceable-Ideological-Education-RAG`), Indian
    (`brahm-ai-official/brahm-ai`, 5★) and German (`awesome-german/ai-tools`,
    4★), and nothing on the topic exceeds 448★.

  **Confirmed a third time by a new channel on 2026-10-06 (third pass):** the
  `ai-tutor` topic page and a stars-sorted education repository search — 30 repos
  read between them, 17 net new — returned **not one LATAM-origin project**. The
  permissive education shelf is now measured across three independent channels and
  is China-, US- and Europe-origin. This is the most firmly established gap in this
  KB.

  Latam-GPT (Chile-led, Spanish and Portuguese, published on Hugging Face and
  GitHub) is regional *foundation* infrastructure — the same shape as the APAC
  gap below: a base model with no pedagogy layer on top.
- **PARTLY REFUTED on 2026-10-06 (third pass): APAC-origin education agents do
  exist, and several are permissive and well-starred.** Earlier passes recorded
  `panaversity/learn-agentic-ai` as "the one APAC-origin education asset found".
  The `ai-tutor` topic sweep returned a China-origin cluster that contradicts this
  outright: [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) (MIT,
  **624★** — the highest-starred permissive education agent in this KB after
  DeepTutor), [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill)
  (MIT, 156★), [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion)
  (Apache-2.0, 105★) and
  [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release)
  (MIT, 57★, **aligned to the Chinese grade 1–9 curriculum**). DeepTutor itself is
  HKUDS — Hong Kong. The APAC shelf is the *strongest* regional shelf in this KB,
  not the weakest, and the earlier claim was an artefact of sweeping only the
  `education-ai` topic.

  **What survives of the gap, stated precisely:** no education agent layer built on
  top of an APAC **sovereign** model. The China-origin cluster above runs on
  commercial and open-weight models (StudyMate ships a DeepSeek harness) — none of
  it targets Sarvam, SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think, BharatGen,
  Fugaku-LLM or NTT Sarashina. And no India-, Japan-, Korea- or ASEAN-origin
  permissive education agent surfaced in either sweep; the APAC shelf is
  **China-plus-Hong-Kong**, which is a narrower finding and a more useful one.

- **APAC sovereign models are base models, not education agents.** Sarvam AI,
  SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think and NTT Sarashina are
  foundation models; none ships an education agent layer. Re-probed 2026-10-06
  and the list only grew: **BharatGen** (IndiaAI Mission), Japan's
  **Fugaku-LLM**, and South Korea's National Sovereign AI Initiative champions
  (LG AI Research, SK Telecom, Naver Cloud, NC AI, Upstage). Still all base
  models. `learn-agentic-ai` remains the one APAC-origin education asset found;
  the APAC long tail on the `education-ai` topic is individual-scale
  (`brahm-ai-official/brahm-ai`, 5★). The pedagogy layer on top of a sovereign
  model is still unbuilt, and that is the opportunity.
- **No open source EU AI Act compliance toolkit specific to education** surfaced
  this pass. The compliance work in pattern P4 is assembled from general-purpose
  parts (typed outputs, checkpointed audit trails, explainable mastery models).

## Gap updates from the fifth pass of 2026-10-06

The institution-first channel refuted three of this KB's firmest regional gaps.
They are left standing above, rather than deleted, so the correction is legible.

| Gap as recorded above | State after the fifth pass |
|---|---|
| "No India-origin permissive education project found in any channel" | **REFUTED.** [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) (MIT, 9★, Microsoft Research India / VELLM, validated with the Sikshana Foundation) and [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) (MIT, 0★, CBSE/NCERT grades 9–12 on open-weight Gemma only) |
| "No ASEAN-origin permissive education project found in any channel" | **REFUTED, and reframed.** [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) (MIT, 158★, 15,802 commits, NUS, supported by AICET) is a mature ASEAN-origin permissive platform. What is actually missing is ASEAN's **agent** layer: AICET's Codaveri, Softmark and ScholAIstic run at ministry scale and are **closed** |
| "No LATAM-origin permissive education project — the firmest finding in this KB" | **REFUTED on existence, confirmed on substance.** [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (MIT, Universidad Tecnológica de Pereira, Colombia, SNCTI-funded) exists and specifies this KB's P1 architecture — and **every code path in its own documented tree 404s**. The gap is a build gap, not an interest gap |
| "No education agent layer on an APAC **sovereign** model" | **STILL OPEN, and now with a licence reason.** [aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no `LICENSE` payload**; its README §Licensing states terms "may vary depending on the underlying base model's restrictions" — Llama3-based variants carry commercial-use restrictions, Gemma-based variants differ — and directs you to each **Hugging Face model card**. Anyone building an education layer on a SEA sovereign model must clear rights **per model, not per repository**. Related, verified this pass: **MaLLaM** (Malaysia's sovereign LLM, built with NVIDIA, 3M+ users via YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL** (March 2026) |
| "No open source EU AI Act compliance toolkit specific to education" | **RE-SIZED, and much smaller than recorded.** The generic toolkit now exists and is permissive — [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) (**MIT**, 8★, TypeScript, six risk tiers, 61 conformity checklist items, 8 document templates, CLI + SDK + client-only web UI) and [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) (**Apache-2.0**, ETH Zurich). Neither mentions education or **Annex III point 3**. The missing piece is an education **profile** on an MIT base, not a toolkit from scratch — see pattern **P13** |
| "No shippable permissive evaluator of tutoring quality" (declared NEW in the fourth pass) | **STILL OPEN — and the reason is now structural, not accidental.** See the licence finding below |

### The licence pattern in pedagogy evaluation — four instruments, zero permissive software licences

The fourth pass found that `AITutor-EvalKit` claims MIT in a peer-reviewed paper
and has no `LICENSE` payload, and called it "a fourth licence failure mode." The
fifth pass searched for alternatives and found that **this is how the whole
subfield is licensed**:

| Instrument | Venue | Licence as claimed | `LICENSE` payload |
|---|---|---|---|
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | EACL 2026 | "released under an MIT license" (in the paper) | **None** — probed both branches |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) (43★, 14 forks, ETH Zurich LRE, EMNLP 2025 oral) | EMNLP 2025 | **Contradicts itself inside one file**: README line 3 badge says **CC BY 4.0**, README line 199 says **CC BY-SA 4.0** | **None** — probed 10 filenames on `main` |
| [kaushal0494/UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | NAACL 2025 | not stated | **None** — probed both branches |
| Open TutorAI (arXiv 2602.07176) | arXiv | "open-source" | **CC BY-NC-SA 4.0** — non-commercial |

**The fifth failure mode, and the one most likely to catch a delivery team: the
licence that contradicts itself inside one file.** A reviewer who reads the badge
gets a permissive answer; a reviewer who reads to the bottom gets a ShareAlike
answer; a reviewer who probes the payload gets no answer at all. All three
reviewers are reading the same commit.

**So what.** MathTutorBench is the most useful of the four and the one you still
cannot vendor: 7 tasks across 3 skills (problem solving, Socratic questioning,
solution correctness, mistake location, mistake correction, scaffolding
generation, pedagogy following with hard variants), a **1.5B pedagogical reward
model** that scores win rates of a generated teacher utterance against ground
truth, and a published leaderboard over 20+ models. **Read the task design,
re-implement the harness, and do not vendor any of the four.** The cheapest
high-value upstream contribution available in this industry remains unchanged
and now applies to three repositories instead of one: **file an issue asking for
a `LICENSE` file.**

## Gap updates from the seventh pass of 2026-10-06

The native-language channel and a consistency sweep of this file against
`agents/trending.md`. **Two of the three corrections below are this file
disagreeing with its own trending log, not new research** — which is the finding.

| Gap as recorded above | State after the seventh pass |
|---|---|
| "No **Japan**-origin permissive education project found in any channel" | **REFUTED, and it was already refuted before this pass ran.** [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) is **MIT**, read from payload, © 2026 **Web Analytics Consultants Association (WACA)** and Toshiaki Ejiri — a named Japanese professional body, with a Japanese operations manual (`OPERATIONS-ja.md`) in-tree. It was probed and recorded in `agents/trending.md` by an earlier pass. **This file kept asserting the gap for several passes after its own KB had disproved it.** |
| "No **Korea**-origin permissive education project found in any channel" | **REFUTED on assets, STILL OPEN on agents.** [yongsoojoo/esd2026-agent-workflow](https://github.com/yongsoojoo/esd2026-agent-workflow) — MIT code + CC BY 4.0 docs, **Kookmin University**, 0★ / 4 commits — is course material, not an agent. See the seventh-pass section above for why the distinction is kept rather than smoothed over |
| "Mother-tongue AI is a **two-region** capability" (`intel/trends.md` trend 21, sixth pass) | **FALSIFIED. It is at least three.** ASEAN has a permissive language layer across **Vietnamese, Thai, Malay and Indonesian** — see `repos/foundations.md`, seventh pass. The sixth pass searched for sovereign **models** (and correctly found SEA-LION unlicensed); it never searched for language **toolkits** |
| "No shippable permissive evaluator of tutoring quality" (fourth pass) | **STILL OPEN, and unchanged.** `tutor-mcp` (MIT, 43★) is now shelved and implements BKT + FSRS + misconception memory, but it **drives** tutoring; it does not **score** it. The four pedagogy-evaluation instruments remain licensed as content or not licensed at all |
| "No LATAM-origin permissive education project" | **Unchanged this pass** — the native-language channel added Japanese, Korean, Arabic and Bahasa/Thai/Vietnamese, not Spanish or Portuguese, which the fourth pass had already used. `LabSirius/TutorIA` (MIT, Colombia, every code path 404) remains the state of the art |

### A new declared gap, from the function-scoped channel

> 🔴 **REFUTED on 2026-10-07 by the thirty-third pass. Read this before quoting the gap below.**
> The single candidate this gap rested on is **`MIT`** — read from payload at
> **`master/LICENSE`, 1068 B, © 2026 Prem Biswal** — and a second permissive proctoring agent
> ([`SuyashMore/AI-Proctored-Examination-System`](https://github.com/SuyashMore/AI-Proctored-Examination-System),
> MIT, 1068 B, © 2020 Suyash More) was found in the same run. **There are at least two permissive
> open-source exam proctoring agents.** The gap, and the build-opportunity ranking derived from it,
> are withdrawn. Root cause in `P461`; the structural lesson in `P462`. The original text is left
> standing below so the correction is legible.

**There is no permissive open-source exam proctoring agent.** This pass searched
the proctoring-plus-grading function directly — the one function-scoped shelf
the third pass had flagged as unswept — and the single substantial candidate,
[biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent),
has **no `LICENSE` payload**. The shelf otherwise holds only **Safe Exam Browser**
(recorded in `repos/trending.md`), which is a lockdown browser rather than an
agent.

**This gap now has a regulatory edge that makes it commercially sharp.**
Vietnam's **Decree 33** (in force 2026-08-15) classifies AI that *"monitors and
analyses learner behaviour with biometric data"* as high-risk, and EU Annex III
point 3 covers exam and behaviour monitoring. So the only category of proctoring
that is sellable in either regime is one whose decisions are **local, explainable
and human-gated** — which is precisely what the unlicensed candidate above
describes itself as being. **The design is right, the grant is missing, and no
competitor holds the space.** Ranked second to P17 (oral reading fluency) as a
build opportunity.

### The method note for this pass

The fifth pass's lesson was *change the channel when a gap persists*. The sixth
pass's was *change the layer*. This pass adds a third, and it is not about
discovery at all: **audit the shelf against the log before searching for anything
new.** Two of this pass's three corrections cost nothing but a `grep` — the
evidence was already in the tree, written by an earlier pass, and contradicted by
the file a reader would actually open. **A KB that only grows forward accumulates
contradictions at exactly the rate it accumulates findings.**

## The CAi UC holder warning — read this before vendoring EduFlow, CPU-Benchmark or OnlyUs

The three Chilean rows added in the eighth pass come from **HaCAIthon 2026**, run
by **CAi UC** (*Centro de Alumnos de Ingeniería*, Pontificia Universidad
Católica de Chile). The event's rules require, as a condition of being eligible
for evaluation:

> All projects must be released under an **OSI licence** (MIT, Apache 2.0 or
> GPLv3 recommended), with a **`LICENSE` file at the repository root**.

That rule worked: **20 team repositories, 19 MIT and one AGPL-3.0**, created in a
single eight-hour event. As a **channel** that is the most valuable thing the
eighth pass found — see `intel/market.md` and `repos/trending.md`.

**But every team repo's MIT payload reads `Copyright (c) 2026 CAi UC`** — the
organiser, not the authoring team. The grant is **inherited from the base
template**, not issued by the people who wrote the code. By this KB's own
`p184` rule — *the holder is the cheapest signal that a licence was inherited
rather than granted* — all 20 are flagged.

**What that means in practice.** Whether a student federation's template
copyright validly covers code written by independent teams during an event is a
**question for counsel, not for a probe.** So:

- ✅ **Read them, benchmark them, and copy the design** — EduFlow's offline-sync
  core in particular.
- ✅ **Cite them** as evidence that the LATAM licensing gap is fixable by rule.
- ❌ **Do not vendor them** into a client deliverable until the holder is
  cleared with CAi UC and the authoring team.

The organisers' own showcase repository, `caiuc/proyectos-hacaithon-2026`, has
**no `LICENSE` payload at all** — the mandate bound the teams and not the
vitrine, which is worth knowing before citing the event as a model of hygiene.

## Gap updates from the eighth pass of 2026-10-06

Channels: the **`docs/` directory** as a probe target, and the
**institutional-event channel**. **34 repository targets probed; 31 resolved** — `AngelitUX/EstudiaUni`, RACHEL and Latam-GPT did not resolve and are recorded as unverified rather than as findings.

| Gap as recorded above | State after the eighth pass |
|---|---|
| "No LATAM-origin permissive education project" — *the firmest finding in this KB* | **FULLY REFUTED, and now precisely resized.** Origin, licence and design are all refuted: **EduFlow** (MIT, PUC Chile) has **running code**; **TutorIA** (MIT, UTP Colombia) has a **13-page requirements specification**; **BERTimbau** (`neuralmind-ai/portuguese-bert`, MIT, **886★**, NeuralMind, Brazil) is a real Brazil-origin language asset with adoption. **What survives is maturity alone** — see the replacement gap below |
| "TutorIA is scaffold only / every code path 404s" | **CORRECTED — see the block above.** The code claim holds and is explained (`.gitkeep` in six directories); the `docs/` directory was never probed and holds the deliverable. **Third instance of the probe-vocabulary failure mode**, after the sixth pass's layer error and the seventh pass's noun error |
| "No shippable permissive evaluator of tutoring quality" (fourth pass) | **STILL OPEN on automated evaluation, PARTLY ANSWERED on protocol.** TutorIA's **RNF-09** specifies pedagogical review by **≥2 subject-expert teachers per subject before launch**, under MIT. That is a human quality gate, not an evaluator; the gap as written is unchanged, but the thing an engagement needs *first* now exists in citable form |
| "Mother-tongue AI is a two-region capability" (trend 21, falsified to three in the seventh pass) | **FOUR regions on capability, TWO on licensing.** LATAM has the capability — AmericasNLP corpora for Aymara, Nahuatl and Quechua, ASR for Quechua, Guaraní, Bribri, Kotiria and Wai'khana, MT for Peru, T5 for 10 indigenous languages — and **ten of twelve probed repositories in that layer carry no `LICENSE` payload**, including **all four probed AmericasNLP editions (2021, 2022, 2023, 2024)** — whose 2024 edition includes a shared task called *"Creation of Educational Materials for Indigenous Languages"*. The claim must now be split: *capability* is four regions, *redistributable* capability is still two |
| "MEA is the only region with zero shippable permissive education assets, and the constraint is licensing hygiene" (seventh pass) | **The diagnosis is confirmed and is no longer unique to MEA.** LATAM's indigenous-language layer has the identical shape: funded, published, benchmarked, ungranted. **And the eighth pass found the remedy** — a submission rule in an event's terms produced 20 licensed repositories in 8 hours (see the CAi UC block above). Cheaper and more prospective than filing `LICENSE` issues one repository at a time |
| "No permissive open-source exam proctoring agent" (seventh pass) | **Unchanged — not re-probed this pass.** The seventh pass's function-scoped sweep stands |

### The replacement LATAM gap, stated so it can be falsified

**There is no LATAM-origin permissive education product at production maturity.**
Not origin, not licence, not architecture — **maturity**, and nothing else:

- `LabSirius/TutorIA` — MIT, institutionally backed, **specification only**, 4 commits.
- `caiuc/equipo-19` (EduFlow) — MIT, **running code**, but an 8-hour build at 1★ with a flagged holder.
- `neuralmind-ai/portuguese-bert` — MIT, **886★ and genuinely adopted**, but a language model, not an education product.
- Four further LATAM education repositories found this pass and confirmed to exist (`Dreathward/sistema-de-aprendizaje-en-linea`, `InkuA-Pasantia/Proyecto-web-educativa`, `luisllacuaperez/PROYECTO-IA`, `AprendizajeProfundo/Diplomado`) — **none has a `LICENSE` payload.** A fifth search hit, `AngelitUX/EstudiaUni` (Chile), **did not resolve on any probe** and is excluded from the count rather than reported as unlicensed.

**So the LATAM engagement posture changes.** For four passes the honest line to a
client was *"nothing exists upstream in the region; we build."* The accurate line
now is: **"the region has published the design and the licence, not the
product"** — which makes a LATAM engagement a *productionisation* engagement with
citable local provenance, and makes the Universidad Tecnológica de Pereira and
PUC Chile named partnership leads rather than absences.

### A new declared gap, from the licence-scope channel

**The `LICENSE` payload — this KB's verification standard for eight passes — is
necessary and not sufficient for any repository whose value is data, audio,
corpus or model weights.**

[Llamacha/IWSLT2023_Quechua_data](https://github.com/Llamacha/IWSLT2023_Quechua_data)
serves a complete **Apache-2.0** text from `main/LICENSE`. Its README's licence
section says the audio is *"property of Siminchikkunarayku and Llamacha"* and
that the work is licensed **CC BY-NC-ND 3.0** — **NonCommercial and NoDerivs**,
which is unusable in commercial client work. The Apache file plausibly covers
the scripts; the data, which is the only reason to clone it, does not.

This is a **third distinct licence trap**, after `p184` (holder foreign to the
project) and the seventh pass's self-contradicting file: **a correct, complete,
unambiguous licence file applied to the wrong scope.** A reviewer following this
KB's own documented method gets a permissive answer and ships a violation.

**Verification method, updated to three points:** read the **payload**, read the
**asset-scope statement** in the README, and check the **holder**. Treat the
asset-scope statement as controlling for the asset. All three are cheap; any one
alone is wrong somewhere in this pass's findings.

### Also recorded: the regional flagship is not open source

**Latam-GPT** (CENIA Chile, launched February 2026, 60+ institutions across 15
countries, Llama-3.1-70B base, ~8 TB of regional data, ≈US$550k) is released
under the **Llama 3.1 Community License Agreement, © Meta Platforms** — **not
OSI-approved**, carrying an Acceptable Use Policy and the 700-million-MAU clause
that requires a separate licence at Meta's sole discretion. The EC's Open Source
Observatory, Brookings and the trade press all describe it as *"open source"*.
**It is open-weights under a bespoke corporate licence**, which is a different
commercial object: usable and valuable for Spanish and Portuguese grounding,
**not relicensable, not presentable to a client as open source**, and it inherits
Meta's AUP into the client's product.

**Provenance caveat.** The licence-to-Latam-GPT link is **single-source** —
`huggingface.co`, `latamgpt.org`, `interoperable-europe.ec.europa.eu` and
`opensourceforu.com` are all **EGRESS_BLOCKED** here (4/4), so the model card
was **not read**. The Llama 3.1 licence's properties are independently confirmed
from the OSI's published position. **Confirm the model card before any client
deliverable.**

### The method note for this pass

Seven passes probed repositories for **code** and for **licences**. This pass
probed one for a **specification** and found a 13-page document in a repository
this KB had written off — the fourth version of the same lesson: **change the
channel, change the layer, change the noun, and now change the file type.** A
project that publishes its design before its code is invisible to a code-shaped
probe, and in academic and ministry-funded work that is the *normal* publication
order.

The harder correction is to this KB's own standard. **The payload channel is not
ground truth.** It is wrong about `Llamacha` in the permissive direction, silent
about `caiuc`'s inherited holder, and it says nothing at all about the
label-versus-grant gap that makes Latam-GPT look open. Eight passes of
"read it from the payload" bought real accuracy and has now been shown to have a
ceiling.

## Gap updates from the ninth pass of 2026-10-06

Channel: the **funder and procurement channel** — philanthropic RFPs, state
education-agency procurement rubrics, district solicitations — which the eighth
pass declared necessary and which this KB had never swept. Plus the
**education-ministry engineering org** as its government twin.

**Evidence tiering applies to this block.** Repository and licence facts are
**Tier 1 (payload-verified)**. Every funder, dollar and procurement fact is
**Tier 2 (corroborated search summaries)** — 14 of the hosts carrying the primary
documents are **EGRESS_BLOCKED** here, including `k12-ai-infrastructure.org`,
`digitalpromise.org`, `unu.edu`, `arxiv.org` and `cosn.org`. **No RFP document
was read.** Confirm before any client deliverable.

| Gap as recorded above | State after the ninth pass |
|---|---|
| "No permissive open-source exam proctoring agent" (seventh pass, carried unchanged through the eighth) | **REFUTED on existence, RESIZED to maturity.** 204 MIT-licensed repositories match; **four verified from payload** (47★/36★/22★/18★ — see the shelf above). The framework-grade one, `lebmatter/exampro` (72★), is **ungranted**. The true gap is **no permissive proctoring agent at production maturity** |
| "No shippable permissive evaluator of tutoring quality" (fourth pass; re-declared in the eighth) | **STILL OPEN TODAY — and now funded, dated and licence-floored.** Measured: `tutoring quality evaluation benchmark license:apache-2.0` returns **0 repositories** (6 Oct 2026). But the **$26M K-12 AI Infrastructure Program** (Digital Promise + Gates Foundation) has **twelve named funded projects** under a floor of **"at least as permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)"**, and at least three land directly on this gap. **The gap now has an arrival window (2027), not just an absence** |
| "The oral reading fluency agent does not exist" (sixth pass) | **UNCHANGED today, and specifically funded.** Cohort 1 of the programme includes **National Tutoring Observatory / Cornell University** (PI Allison Koenecke) — *"Open Leaderboards for Benchmarking Automated Speech Recognition in Educational Contexts"*, 6–12 months from 29 Jun 2026. Measured: the org has **no code** — two repos, the substantive one a website at **0★ with no payload** |
| "RACHEL — repository path not established" (eighth pass) | **RESOLVED, and the verdict is: not shippable.** The org is **`rachelproject`**; `contentshell` **is** the RACHEL CMS. **No licence payload** across 8 filenames × 2 branches; the README's only grant statement is **"Creative Commons - BY, SA, NC"** — a **content licence applied to PHP software, with NonCommercial.** Kolibri (**MIT**, re-confirmed from payload) remains the platform answer; RACHEL is prior art to cite, not code to ship |
| "MEA/LATAM/APAC: built, published, benchmarked, ungranted" (seventh and eighth passes) | **Now confirmed in a third region from a fourth channel.** `AI-EDU-LAB/E-EVAL` (**33★**, Chinese K12 education evaluation benchmark) has **no payload**. The failure mode is not regional — it is what unfunded published work looks like everywhere |
| "North America's general-language channel is saturated; the next trend must come from district RFPs, state procurement portals or vendor filings" (eighth pass) | **TWO OF THREE SWEPT, and the channel paid immediately** — see `intel/market.md` (North America) for the procurement rubrics and `intel/trends.md` trends 25–26. **Vendor filings remain unswept** and are a distinct channel |

### The headline: this KB's oldest gap is being bought

**The K-12 AI Infrastructure Program** — **$26M**, multi-year, led by **Digital
Promise** with **Learning Data Insights**, **DrivenData**, the **Massive Data
Institute at Georgetown** and **Catalyst @ Penn GSE**; funded by the **Gates
Foundation**, which manages review and monitoring directly. Launched **3 Nov
2025**, first cycle opened **4 Feb 2026**.

Its licence condition is the reason it belongs in this file:

> All funded developments must be released under a licence **at least as
> permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)** — with
> **Apache-2.0** recommended for software and code *including evaluations, models
> and applications*, and **CC-BY** for datasets and knowledge products.

**Twelve projects are already funded.** Cohort 1 (29 Jun 2026): **Learning
Equality** (science-misconception benchmark), **Princeton** (simulated student
models), **National Tutoring Observatory / Cornell** (ASR leaderboards for
education), **Stanford** (KB-TutorBench, multimodal formative-assessment
dataset). Cohort 2 (21 Sept 2026): **eight** awards focused on **formative
assessment** plus math, literacy and writing, outputs stated to be **openly
licensed**; one named at Tier 2 — **MMSA & TERC** (*A Multimodal Dataset for
AI-Enhanced Formative Assessment*).

Separately, the **EDU AI** RFP — **up to $8M**, one award, closed **31 Jul
2026**, work from **Nov 2026** over 30–36 months — funds open-source
education-specific model(s) for **K-12 math tutoring as effective as human
experts**.

**One grantee is already this KB's recommendation. Learning Equality maintains
Kolibri** (`learningequality/kolibri`, **MIT**), the offline-first platform the
eighth pass selected. The organisation holding this KB's platform answer is now
funded to produce an openly-licensed benchmark — **a named partnership lead with
an existing permissive track record**, not a cold approach.

### A new declared gap: the funded pipeline is not a shelf yet

**Nothing from the twelve funded projects is publicly available.** Measured on
6 Oct 2026: `KB-TutorBench` → **0 repositories**; `learningequality` filtered on
`benchmark` → **0 repositories**; the National Tutoring Observatory org → a
website at 0★ with no payload.

So the engagement line changes shape without closing: **"the permissive
evaluation layer is funded and lands through 2027; today you build the harness,
and you design it so Apache-2.0 benchmarks drop in as they ship."** Pattern
**P23** in `compose/patterns.md` is that design. The highest-value single lookup
for the next pass is **the seven unnamed cohort-2 grantees** — each is an
Apache-2.0-or-better artefact with a named owner arriving inside twelve months.

### The method note for this pass — the probe set had a spelling bug

**Three of the six MIT grants on the new DfE shelf are in a file named
`LICENCE`**, the British spelling.

**The precise failure is worse than a missing filename: the check existed and was
never run.** Pattern **P22**'s licence gate, written in the eighth pass, *does*
list `LICENCE` in check 1. But every sweep this KB has recorded — including the
eighth pass's own 34-target probe — enumerates only `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING` and `license.txt`. **The gate documented the British
spelling; the sweeps never executed it.**

With the old set, this pass would have recorded
`DFE-Digital/apply-for-teacher-training` (38★),
`get-into-teaching-app` (25★), `register-trainee-teachers` (12★) and
`get-information-about-schools` (9★) as **four ungranted government
repositories**, and written another paragraph about ministries that publish code
without licensing it. **All four are MIT.**

That is the **seventh** instance of one failure mode: wrong channel → wrong layer
→ wrong noun → wrong file type → wrong scope → wrong assumption that a payload
exists at all (RACHEL) → **wrong spelling**. Every one produced a false negative
that read as a regional or categorical absence.

**Two corrections follow.** The probe set now includes `LICENCE`, `LICENCE.md`,
`LICENCE.txt` and `COPYRIGHT`; every negative in this pass was re-run against
them and all seven survived. And **earlier passes' "ungranted" conclusions were
produced by a query that could not have found a British-spelled grant** — they
are suspect until re-probed, which matters most for the MEA, Commonwealth and
ministry-adjacent repositories where that spelling is the norm.

## Gap updates from the tenth pass of 2026-10-06

This pass did not sweep outward for new agents. It **re-probed the 41
repositories this KB has recorded as ungranted**, because the ninth pass ended
by declaring its own back catalogue suspect:

> *"Earlier passes' 'ungranted' conclusions were produced by a query that could
> not have found a British-spelled grant — they are suspect until re-probed."*

They have now been re-probed. **41 repositories × 10 filenames × 2 branches**
(`LICENCE`/`LICENSE`/`licence`/`license`/`COPYING`, with `.md` and `.txt`
variants, on `main` and `master`), all via `raw.githubusercontent.com`, and the
probe was validated on **6 known-payload controls first — 6 of 6 resolved**,
including two British-spelling controls and three repositories whose licence sits
on `master`.

### The result: 1 flip in 41, and the spelling was not the cause

| Re-probe outcome | Count |
|---|---|
| Repositories re-probed | **41** |
| Flipped to granted | **1** |
| Confirmed ungranted under all 20 URLs | **40** |
| Flips attributable to the British `LICENCE` spelling | **0** |

**The ninth pass's correction generalised to nothing.** `LICENCE` is a house
style at one UK government organisation, not a defect in this KB's reach. It
stays in the probe set — it costs one URL per repository and two controls prove it
works — but it is a **special case, and this KB recorded it as a general
discovery.** That is corrected here.

**The defect that was general is the branch name.** The single flip resolved on
`master/LICENSE`: American spelling, non-default branch. Three of six controls sit
on `master` too. No pass before this one varied the branch. **Eighth failure
mode: wrong branch.**

### The correction to the catalogue

| Repo | Was | Is | Read from |
|---|---|---|---|
| [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) | recorded ungranted | **MIT** | `master/LICENSE` |

Caveat that travels with it: the MIT text names **`theopenem`** as copyright
holder, and [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET)
serves a byte-identical `README.md` (md5 `110b2e3439d86b6055821de382d90d61`) and
byte-identical licence. **One asset, two addresses** — pin the `theopenem` copy,
whose owner matches its copyright line. The fork direction is **not established**:
`github.com` returns 403 to `curl` here and the fork banner is absent from the
rendered page this environment receives.

### The row this pass adds — one, and why only one

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| prosody | [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody) | **MIT** (`main/LICENSE`, **full text read**) | 0 | Oral reading assessment from speech. Aligns recorded audio to reference text at word level; reports accuracy and word error rate, speaking rate in WPM, misread/omitted/inserted words, and a fluency score from pause pattern and pace. Whisper for ASR (`PROSODY_ASR_MODEL`), Levenshtein alignment, Groq API for transcription. Python, **1 commit**, 0 forks, not a fork. Targets language learning and speech-language pathology. |

**One row, and the reason is the finding.** `oral reading fluency assessment
speech` returns **two repositories on all of GitHub**. The other,
[mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2)
(TypeScript, 0★), has **no payload under any of the 20 URLs** — the repository
exists, the grant does not. That is the entire denominator, and padding it would
destroy the only useful thing about it.

### The method finding: GitHub's licence field manufactures absences

`prosody` is listed in GitHub's repository search as **"License: Not
specified."** Its payload is a **complete, unmodified MIT licence**, read in full
this pass, body unqualified, `Copyright (c) 2026 Justin`.

This is the **ninth failure mode**, and it is the most consequential one yet
because it attacks the instrument this KB uses to *declare gaps*. A
licence-filtered search cannot return a repository GitHub believes is unlicensed.
Three such searches were run this very pass and all three returned zero. Those
zeros remain the best available measurement, but their meaning has changed:
they are **absence as GitHub's licence index sees it**, not absence.

Every gap in this file that rests on a `license:` filter inherits that caveat.

### What this does to the oral reading fluency gap (sixth pass)

Restated, because the old wording was wrong in the expensive direction:

- **Old:** *"an oral reading fluency agent does not exist."* Refutable by one
  repository, and now refuted by one.
- **New:** **two repositories exist in the whole of GitHub; one is MIT with a
  single commit; neither has a single star.** The *capability* gap is real and
  the shelf is empty for practical purposes — but it is empty in a way a client
  engagement can price, and `prosody` is a starting point rather than nothing.

And the funded answer now has a name. **Harvard University (Ying Xu)** is a
Cohort 2 grantee of the $26M K-12 AI Infrastructure Program for **"OpenLiteracy:
An Open-Source AI Infrastructure Suite for Advancing Speech Foundation Models for
Early Word Reading Assessment and Instruction"** (Tier 2, search-summary
corroborated). It lands on this gap exactly. **GitHub returns 0 repositories for
`OpenLiteracy`** (Tier 1, measured this pass) — funded, named, not shipped.

### The method note for this pass

Nine passes looked outward; this one audited the KB against itself, and the audit
cost it two of its own conclusions — the generality of the spelling fix, and the
wording of the oral-reading gap. Both corrections came from re-running rejections
rather than from new search, which is a cheaper channel than any this KB has used
and the only one that can find a **false negative**.

The limit is worth stating: **no primary document was read this pass either.**
Nine further hosts were attempted and all nine returned `EGRESS_BLOCKED`
(`digitalpromise.org`, `www.coe.int`, `rm.coe.int`, `www.prnewswire.com`,
`www.gse.upenn.edu`, `www.eunews.it`, `www.sec.gov`, `ess.iesalc.unesco.org`,
`openai.com`) — including three **syndicated mirrors** tried specifically to route
around a blocked primary host. With the ninth pass's fourteen, that is **23
distinct hosts, zero reachable.** `github.com` and `raw.githubusercontent.com` are
the only origins this environment serves, which is why this pass spent its budget
on payload work.

## Added in the eleventh pass of 2026-10-06 — the evaluation tier, and three ITS agents

New channel this pass: **the GitHub REST search API**, reachable through this
session's GitHub MCP server. Ten previous passes probed it with an HTTP client
(`curl https://api.github.com/search/repositories` → **403**, *"sessions are bound to
their configured repositories"*) and concluded it was blocked. It is not — the MCP
path returns `total_count`, `stargazers_count`, `default_branch`, `fork`, `archived`
and `license.spdx_id`. Every licence below was still read from the repository's own
payload on `raw.githubusercontent.com`; the API supplied the metadata and, crucially,
**the real `default_branch`** to probe.

**8 rows added. 7 are reinstatements of assets dropped by this repository's reset
earlier the same day** (see the gap-update section below) — which is why the count is
high and why none of them is a discovery.

### The evaluation tier — permissive, government-built, and what P23 was told to wait for

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| Inspect | [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** (`main/LICENSE`) | **2,945** | LLM evaluation framework from the **UK AI Security Institute** (`aisi.gov.uk`). Prompt engineering, tool use, multi-turn dialog and **model-graded evals**; scorers and elicitation techniques extend from separate Python packages. 779 forks, 348 open issues, pushed 2026-10-06. **The harness every evaluation pattern in this KB needs, and the single highest-starred MIT asset on the evaluation shelf.** |
| Moonshot | [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** (`main/LICENSE.md`) | 355 | Modular tool to **evaluate and red-team any LLM application**, from the **AI Verify Foundation** (the Singapore IMDA AI-testing community). Benchmarking + red-teaming in one surface. 72 forks, pushed 2026-10-06. **The APAC-origin half of the evaluation tier, and the only permissive red-teaming harness here.** |
| tutoreval | [shivanireddyk/tutoreval](https://github.com/shivanireddyk/tutoreval) | **MIT** (`main/LICENSE`, 1,074 B) | 0 | *"Measuring whether an AI tutor teaches, rather than whether it answers."* Deterministic pedagogical evaluation with a hand-labelled benchmark. **The only MIT-licensed pedagogical benchmark found — and it is one author's project.** Listed because the licence is the scarce thing here, not the stars. |

### Intelligent tutoring system agents

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| GenMentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | ⚠️ **CC0-1.0** (`main/LICENSE`, 7,048 B, read in full) | **131** | *"LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System"* — **WWW 2025 Industry Track, Oral.** Skill-gap identification → learner modelling → tailored content generation. TypeScript, 22 forks, updated 2026-10-04. **Highest-starred purpose-built ITS agent framework in this KB.** See the CC0 warning below — it is permissive on copyright and **silent on patents**. |
| Open Learning AI Tutor | [mitodl/open-learning-ai-tutor](https://github.com/mitodl/open-learning-ai-tutor) (live **fork**) · upstream [MIT-OL-AI-Tutoring/Open_Learning_AI_Tutor](https://github.com/MIT-OL-AI-Tutoring/Open_Learning_AI_Tutor) | **MIT** (`main/LICENSE`, md5 `cb5f766beb2db853d5b69328279ccb1b` on **both**, © 2024 Romain Puech) | 1 (fork) · 0 (upstream) | **MIT Open Learning's** AI tutor backend — the pedagogical engine behind `learn-ai.ol.mit.edu` (paper: arXiv 2410.03781). **Use the `mitodl` fork**: it was pushed 2026-10-03 and its README points at MIT's production domain, while the upstream has been still since 2025-02-26. ⚠️ The maintained copy is a **fork**, so fork-excluding search cannot see it. |
| MITS | [Siesher/MITS](https://github.com/Siesher/MITS) | **MIT** (`main/LICENSE`) | 3 | Math ITS: **Socratic** multi-agent STEM tutor over an RL-trained Qwen3.5-9B. FastAPI + Next.js. The clearest small example of Socratic-constraint-as-architecture rather than as a prompt. |
| Intellicode | [Redomic/intellicode-backend](https://github.com/Redomic/intellicode-backend) | **MIT** (`main/LICENSE`) | 5 | Adaptive learning platform **bridging a classical ITS with coordinated LLM agents** — the hybrid, not a chat wrapper. Python. Frontend at `Redomic/Intellicode-frontend` (MIT per payload probe pending; 1★). |

### The Python LTI 1.3 row this KB declared missing eight hours earlier

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| PyLTI1p3 | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (`master/LICENSE`, 1,070 B) | **138** | LTI 1.3 Advantage tool implementation for Python with **Django and Flask** adapters. **The canonical Python LTI 1.3 library.** ⚠️ Last push **2024-08-18** — stable and widely used, not actively developed. Branch is `master`. |

### Measured this pass and NOT usable — read this before quoting a benchmark in a proposal

Four tutoring-evaluation instruments exist and are real work by serious
institutions. **Not one carries an OSI-approved licence.** This table is the whole
reason pattern **P27** exists.

| Repo | ★ | What the payload actually says | Verdict for client work |
|---|---|---|---|
| [Khan/tutoring-accuracy-dataset](https://github.com/Khan/tutoring-accuracy-dataset) | **57** | Custom **"Evaluation Dataset License"** (`main/LICENSE`, 2,690 B, read in full). Grants internal use/copy/modify/merge **solely to evaluate AI models**. Prohibits **re-distribution, publication, use for model training, and any production use**; no sublicensing; clause 4 makes it **viral** over any combined dataset. Clause 3 expressly permits evaluating **products intended for commercial use** and **commercial use of the insights gained**. | ⚠️ **Borrow, never ship.** Usable to measure a client's tutor; the findings are yours. It must not enter a deliverable, a training set, or any dataset you hand over. |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 43 | **No licence payload** under 10 filenames × 2 branches. README carries a **CC BY 4.0 badge** *and* body text saying **CC BY-SA 4.0**. Two incompatible claims, nothing authoritative to adjudicate. **ETH Zurich**, EMNLP 2025 Oral. | 🔴 **Treat as ungranted.** The ShareAlike reading would attach to derivatives. |
| [Yunfeng-Wan/CSTutorBench](https://github.com/Yunfeng-Wan/CSTutorBench) | 2 | **CC BY-NC-4.0** (`main/LICENSE`). 2,970 multi-turn QA dialogues from real university forums. | 🔴 **NonCommercial — out.** |
| [ScottDaniels/labaaoom](https://github.com/ScottDaniels/labaaoom) | 1 | **BSD-2-Clause body** (`master/LICENSE`, 2,266 B) behind a preamble: *"Contributions to this source repository must be published with the same license."* Android oral-reading-fluency app, © 2017, last touched 2024-12-12. | ⚠️ **Usable.** The reciprocity clause binds **contributions back**, not derivatives; the two-clause body governs redistribution. Flag it in the licence register and do not vendor it as "BSD" without the qualifier. |

### Measured and still ungranted

| Repo | Probe | Result |
|---|---|---|
| [mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) | re-probed on its **real** `default_branch` — `deployment/playstore`, not `main` or `master` | **No payload.** The tenth pass's verdict was right; its two-branch method could not have established it. |
| [Kaylazagelbaum/ORF_Calculator_6th](https://github.com/Kaylazagelbaum/ORF_Calculator_6th) | `main`, 6 filenames | **No payload.** 0★, HTML, created 2026-08-25. |
| `imsglobal/caliper-python` · `concentricsky/badgr-server` | `README.md` on `main` and `master`; search index | **404 / invisible.** 1EdTech moved Caliper to **private repositories on 2023-06-17** (notice preserved in a surviving fork). Public forks are 0★ and unmaintained. |

### ⚠️ The CC0 warning — read before vendoring GenMentor

**CC0-1.0 is a public-domain dedication, not a software licence.** For copyright it is
broader than MIT. But the instrument states that **no patent or trademark rights held
by the Affirmer are waived.** Apache-2.0 grants patent rights expressly; MIT's
"deal in the Software without restriction" is generally read as implying them. CC0
does neither.

**The rule:** CC0 components are fine in a deliverable and must be recorded in the
licence register **as CC0, not as "MIT-equivalent"**. For anything patent-sensitive —
assessment scoring methods, adaptive-sequencing algorithms, anything a client may
want to defend — prefer an Apache-2.0 component for the same function if one exists.

## Gap updates from the eleventh pass of 2026-10-06

### The reset of 2026-10-06 dropped 172 repository addresses, and the tenth pass re-declared one of them as a gap

This repository was reset earlier on 2026-10-06; the previous estate is preserved in
`archive/2026-10-06-pre-reset/`. Measured by extracting every
`github.com/{owner}/{repo}` address from the eight live KB files and from the nine
archived ones:

| Address set | Distinct `owner/repo` |
|---|---|
| The eight live KB files | **627** |
| The nine pre-reset archive files | **678** |
| In the archive, absent from the live KB | **179** |
| of those, not real repositories (placeholders and negative controls) | 7 |
| **Real repository addresses dropped** | **172** |

The cost is not hypothetical. The tenth pass declared, eight hours before this one:

> *"**No Python LTI 1.3 library exists on the permissive shelf.** [...] Most AI
> tutoring code is Python. Searched, not found, recorded as a gap — and as a
> candidate contribution."*

`archive/2026-10-06-pre-reset/` contains `dmitry-viskov/pylti1.3` — **MIT, 138★** —
with a note that the KB *"already had it registered from an earlier pass."*
**The gap was refuted by this repository's own archive before it was declared.**

**The rule this adds, and it needs no external instrument:** after a reset, a gap
claim is not publishable until it has been diffed against `archive/`. This is the
**eleventh failure mode** in this KB's list.

**Reinstated this pass: 17 addresses**, 8 of them as rows above (`inspect_ai`,
`moonshot`, `pylti1.3`, `gen-mentor` is new, `mitodl/open-learning-ai-tutor`,
`tutoreval`, `MITS`, `intellicode-backend`) and 9 in `verticals/solutions.md` and
`repos/foundations.md`. **~155 remain unrecovered**, in clusters a later pass should
take one at a time: the **Ed-Fi** stack, **LibreTexts** and **OpenStax**, the
**Nextcloud** AI apps, the **xAPI/LRS** tier, the ~16-plugin **Moodle AI** cluster,
and the ~20-server **education MCP** cluster.

### The method note for this pass — three kinds of zero, all of them wrong

| What produced the zero | Why it was not an absence |
|---|---|
| A **ranked web surface** (`WebSearch`, `github.com/search` rendering) | Ranked, truncated and cached. The REST API returns `total_count`, which is a count. Ten passes measured absences without it. |
| A **`repo:` qualifier** | **GitHub repository search excludes forks unless `fork:true` is passed.** `repo:mitodl/open-learning-ai-tutor` → 0; the same query with `fork:true` → 1, and that fork is MIT Open Learning's production tutor. **Twelfth failure mode.** |
| A **keyword-heavy or licence-filtered query** | `tutoring quality evaluation benchmark` → 0. Drop the single word *quality*: **20 results**, led by Khan Academy and ETH Zurich. The zero described the filter. |

And one correction to the probe set itself: the tenth pass fixed `main`-only probing
by adding `master`. **Two guesses is still a guess.** Read `default_branch` from the
API and probe *that*: this pass found `dev` (`learnhouse`, 2,320★), a version number
(`portabilis/i-educar`, 718★, branch `2.12`) and `deployment/playstore`
(`ReaDirect-V2`). A `main`+`master` probe reports "ungranted" about Brazil's largest
free education platform, which is **GPL-2.0**.


## Added in the twelfth pass of 2026-10-06 — the instrument that needs no API, and 4 agent rows

**New instrument this pass, and it is the durable contribution:** the eleventh pass's
method note ends *"Read `default_branch` from the API and probe *that*."* Correct — but
this pass the HTTP API answered **403** again
(*"sessions are bound to their configured repositories"*), so that instruction was not
executable through the path the note assumed. It does not need an API at all:

```
git ls-remote --symref https://github.com/{owner}/{repo} HEAD
# → ref: refs/heads/{default_branch}	HEAD
```

`ls-remote` is **plain git over HTTPS**, reachable wherever `github.com` is, and it
returns the default branch **authoritatively** rather than by guess. It also doubles as
an existence check: a repository that no longer resolves returns nothing at all. Every
branch and licence in the tables below was obtained this way and then read from
`raw.githubusercontent.com`. **Four default branches found this pass that neither
`main` nor `master` would have caught:**

| Repo | Real default branch | What a `main`+`master` probe reports |
|---|---|---|
| `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` | **`v6.2.0`** | ungranted — it is **Apache-2.0** |
| `moodlehq/moodle-tool_dataprivacy` | **`MOODLE_34_STABLE`** | ungranted — it is **GPL-3.0** |
| `datakind/student-success-tool` | **`develop`** | ungranted — it is **MIT** |
| `mendezjerick/ReaDirect-V2` | **`deployment/playstore`** | ungranted (as the eleventh pass found) |

A **version number**, a **vendor release-branch convention** and **`develop`** are all
in that list. The guess-set is not two names wide, and it is not enumerable — read it.

### The agent rows

| Agent | Repo | Licence (read from payload) | ★ (2026-10-06) | Branch | What it does |
|---|---|---|---|---|---|
| AI-Powered-Video-Tutorial-Generator | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | **MIT** (`main/LICENSE`, **1,070 B**) | **313** (65 forks) | `main` | Generates **illustrated video lessons** with expressive presenters, distinct voices and lip-sync, on a native timeline editor. Desktop app (Tauri/Rust + Python + React) that runs **local models** as well as cloud providers. **New to this KB** — it appears in no earlier pass. The only permissive **video-lesson generator** on this shelf, and the local-model path is what makes it usable where per-seat inference cost is the binding constraint. |
| Edu-ConvoKit | [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | **MIT** (`main/LICENSE`) | **117** (16 forks) | `main` | Stanford NLP's framework for **education conversation data**: pre-process (with participant anonymisation), annotate (talk time, student reasoning, teacher uptake), analyse. Python. This is the **measurement instrument for trend 10** — "human connection is becoming the measured outcome" — and the anonymisation step is what makes classroom audio usable under the privacy regimes in all four regions. |
| Student Success Tool | [datakind/student-success-tool](https://github.com/datakind/student-success-tool) | **MIT** (`develop/LICENSE.md`) | 8 (2 forks) | **`develop`** | DataKind's predictive-advising pipeline: identifies students at risk of not graduating and routes advisor interventions. Ships automated ML pipelines, EDA, feature engineering and explicit **bias-reduction** steps, built around transparency of model variables and an advisor **in the loop**. Python. Funded by **Google.org**; named partner **John Jay College** reports a 32% rise in senior graduation rates over two years. **North America**-placed, and the clearest permissive answer to a retention engagement. |
| EduCoder | [EduNLP/EduCoder](https://github.com/EduNLP/EduCoder) | **MIT** (`main/LICENSE`) | 3 (1 fork) | `main` | Annotation system for **classroom transcript data**: human annotation workspaces, admin assignment, and side-by-side comparison of **human versus LLM-generated** annotations with evidence notes tied to individual transcript lines. Next.js/Prisma/PostgreSQL. Pairs with Edu-ConvoKit as the labelling front end to its analysis back end. |

**Read the placement honestly.** One of these four is a traction asset (313★); the
other three are 3–117★ research-grade code. They earn rows because *classroom discourse
measurement* and *permissive predictive advising* were functions with no entry on this
shelf, and because the Stanford and DataKind rows come with named institutional
backing rather than a star count.

### The 13th failure mode — the licence filename is case-sensitive

`raw.githubusercontent.com` is case-sensitive, and a licence-filename probe is a
case-sensitive guess. This pass probed nine lowercase-conventional names
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, …) across every
recovered address and reported **13 repositories as ungranted**. Re-probed with
case variants:

| Repo | Name of the actual licence file | Real licence | What the first probe said |
|---|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **`LICENSE.TXT`** (uppercase extension) | **Apache-2.0**, 470★ | ungranted |
| [european-commission-empl/European-Learning-Model](https://github.com/european-commission-empl/European-Learning-Model) | **`license`** (lowercase, **no extension**) | **EUPL-1.2** | ungranted |

This KB's licence-failure catalogue already held *a licence hidden outside the root*
(`OS4ED/openSIS-Classic` at `docs/License.txt`, `frappe/*` at lowercase `license.txt`).
The new entry is narrower and nastier: **the right directory, the right word, the wrong
case.** `LICENSE.TXT` is two characters away from a name the probe already tried.

**`openedx/XBlock` is the row that makes this failure mode expensive.** Open edX's
platform core is **AGPL-3.0** and this KB has priced it as copyleft for eleven passes.
`XBlock` — the component and plugin SDK, the surface a studio actually writes against —
is **Apache-2.0** at 470★. A `main`+`master`+lowercase probe reports the plugin SDK of
the most widely deployed LMS in this KB as ungranted. It is permissive, and it is the
seam that lets a client-specific component be built and redistributed without
inheriting the platform's AGPL obligations. Full entry in `repos/foundations.md`.

### An independent reproduction, and a size floor that holds

This pass's payload classifier read `CaviraOSS/PageLM` (**2,000★**, 277 forks) as
**MIT** — exactly the misclassification `P411` predicted on 2026-10-05. The payload
opens with the literal MIT grant and is titled *"PageLM Community License"*:
**non-commercial only**, **redistribution prohibited**, a **revenue-sharing agreement
required** before any commercial deployment, and the licence is **revocable**. Nothing
new is claimed here — the finding is pass 123's. What this pass adds is that an
independently written classifier fell into it the same way, so the **size tell is the
load-bearing check, not the grant phrase**: this pass measured a real MIT at
**1,070 B** (`AI-Powered-Video-Tutorial-Generator`, and `pylti1.3` at the same figure)
against PageLM's 8,563 B. 🔴 **PageLM remains DO-NOT-VENDOR for any Globant
engagement**, at any star count.

### Measured this pass and genuinely ungranted — 11 addresses, after 30+ filename variants

Each probed on its **real default branch** from `ls-remote`, against both the
conventional names and the case variants above. These are absences of a grant, not
absences of a probe:

| Repo | Branch | Note |
|---|---|---|
| [CAHLR/OATutor-Content](https://github.com/CAHLR/OATutor-Content) | `main` | ⚠️ **Read this before deploying OATutor.** The *engine* (`CAHLR/OATutor`) is **MIT** and sits on this KB's core shelf. Its **content repository — the problem bank and hint trees — carries no licence at all.** The pedagogy is the asset; it is the part that is not granted. |
| [FWU-DE/schulfach-ontologie](https://github.com/FWU-DE/schulfach-ontologie) · [FWU-DE/schulart-ontologie](https://github.com/FWU-DE/schulart-ontologie) | `main` | **Germany**, FWU (the federal states' media institute). School-subject and school-type ontologies — the vocabulary a German curriculum alignment needs. Ungranted. |
| [european-commission-empl/european-digital-credentials](https://github.com/european-commission-empl/european-digital-credentials) | `master` | **EU Commission**, DG EMPL. Ungranted, while its sibling `European-Learning-Model` carries EUPL-1.2 in a file named `license`. |
| [dini-ag-kim/school-curriculum-pg](https://github.com/dini-ag-kim/school-curriculum-pg) | `main` | **Germany**, DINI-AG-KIM metadata group. Curriculum vocabulary. Ungranted. |
| [aiverify-foundation/LLM-Evals-Catalogue](https://github.com/aiverify-foundation/LLM-Evals-Catalogue) | `main` | **Singapore**, IMDA. Ungranted — while `aiverify` and `moonshot-data` in the same organisation are **Apache-2.0**. Organisation-level licence inference is unsafe even inside a government foundation. |
| [marcusgreen/moodle-tool_aiconnect](https://github.com/marcusgreen/moodle-tool_aiconnect) · [jeanlucio/moodle-local_aihub](https://github.com/jeanlucio/moodle-local_aihub) · [alvarogregori/moodle-ai-graded-assignment](https://github.com/alvarogregori/moodle-ai-graded-assignment) | `main` | 3 of the ~16-plugin Moodle AI cluster. The other 8 probed this pass are **GPL-3.0** (correct for in-tree plugins); these 3 are ungranted. `moodle-ai-graded-assignment` is the painful one — AI-graded assignments is the regulated function this KB has been hunting since the seventh pass. |
| [Kaiman-p/tutor-adaptativo-ia](https://github.com/Kaiman-p/tutor-adaptativo-ia) · [mietiainvestigacion-creator/API-EduAdapt](https://github.com/mietiainvestigacion-creator/API-EduAdapt) | `main` | **LATAM**, Spanish-language. Both ungranted. Consistent with the regional finding in `intel/market.md`: the LATAM constraint is licence hygiene, not absence of code. |

### Gone, not merely unfound — 5 addresses that no longer resolve

`ls-remote` returns nothing for these. They were live when the archive recorded them:

| Address | What it was | Consequence |
|---|---|---|
| `IMSGlobal/caliper-python` | Caliper reference implementation, Python | Confirms the eleventh pass's declared gap, with a second instrument. |
| **`1EdTech/caliper-php`** | Caliper reference implementation, **PHP** | 🆕 **Extends that gap.** The eleventh pass established that the Python implementation went private on 2023-06-17. The **PHP** one is gone too. There is no surviving public reference implementation of Caliper in any language this KB has checked. **Do not promise Caliper emission without pricing a 1EdTech membership or a clean-room build** — and now there is no second language to fall back to. |
| `concentricsky/badgr-server` | Open Badges server | Confirms the eleventh pass. The verifiable-credential half of trend 8 has no permissive server. |
| **`Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP`** | An **MCP server for the Ed-Fi SDK** | 🆕 Recorded in this repository's own archive; does not resolve now. The rest of the Ed-Fi stack is alive and **Apache-2.0** (see `repos/foundations.md`); the MCP side-car is what disappeared. If an engagement needs Ed-Fi over MCP, that is a **build**, not an adoption. |
| `junjie1005/Plataforma-IA-Educativa-Rutas-Personalizadas` | LATAM Spanish-language adaptive platform, 0★ | 🆕 **The search index still lists it; `ls-remote` cannot reach it.** A repository can be in `total_count` and not exist. The index is a snapshot, so a count from it is an upper bound — worth remembering before quoting one as a measurement. |

### The method note for this pass

| What this pass used | Result |
|---|---|
| `git ls-remote --symref … HEAD` | **The default-branch instrument.** No API, no key, reachable wherever `github.com` is. 4 non-obvious default branches found, 5 dead addresses identified. |
| `curl` on `api.github.com/search/*` | **403** — *"sessions are bound to their configured repositories"*. Same as passes 1–10. |
| `curl` on `api.github.com/repos/{owner}/{repo}` | **403**, for repositories outside this session's scope. |
| GitHub **MCP** `search_repositories` | **200 with `total_count`.** Reproduces the eleventh pass's finding: the MCP path works where the HTTP path does not. Both statements in this KB about the API are true, of different clients. |
| Payload reads from `raw.githubusercontent.com` | **200** throughout, on every branch `ls-remote` named. |

**The honest summary of the archive recovery:** of the ~155 addresses the eleventh pass
left unrecovered, this pass probed **66** and resolved **every one** of them to a real
default branch and a licence state — **28 permissive** (12 MIT, 10 Apache-2.0,
3 ECL-2.0, 1 ISC, 1 BSD, 1 MPL-2.0), **17 copyleft** (10 GPL-3.0, 4 AGPL-3.0,
2 GPL-2.0, 1 EUPL-1.2), **11 ungranted**, **3 CC** content licences, **3 non-OSI**
source-available, and **4 dead**. Seven further addresses were probed from outside the
archive, from the search index. The clusters
now closed are the **xAPI/LRS tier**, the **Ed-Fi stack**, **LibreTexts**, **OpenStax**,
the **Nextcloud AI apps**, the **Moodle AI plugin cluster** and the **interoperability
tier**. The **~20-server education MCP cluster remains the largest untouched block**,
and the next pass should take it: two of this pass's five dead addresses were MCP
servers, so that cluster is the one most likely to have decayed.

---

## Added in the thirteenth pass of 2026-10-06 — the non-English-language channel, and a platform promoted out of trending

**Channel used this pass:** search in the **language of the country**, not in English or
Spanish. Passes 1–12 searched in English and (from the fifth pass) Spanish. This pass ran
the mandatory queries again in **Japanese, Korean, Arabic and Portuguese**. That is a new
channel for this KB, and the measured yield is in `agents/trending.md`.

**One row is promoted, not discovered.** `Open-TutorAi/open-tutor-ai-CE` was already
recorded in `repos/trending.md` by the twelfth pass, with the correct licence and star
count. It had never been shelved in `agents/top.md` or `verticals/solutions.md`. It is the
most capable permissive AI-native education platform in this KB and it was sitting in a
trending log. That is a shelving failure, and this pass fixes it.

| Agent | Repo | Licence (read from payload) | ★ / forks (2026-10-06) | What it does |
|---|---|---|---|---|
| Open TutorAI (Community Edition) | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** (`LICENSE`, 1,531 B — **body text, no title line**) | 108 / **192** | Personalised tutoring platform: multi-model conversation, **local RAG**, **voice / video / 3D-avatar modes**, structured learner onboarding that configures a per-learner assistant, and **role-based access control**. Serves **Ollama** local models as well as OpenAI / Groq / Mistral APIs. Python, 380 commits on `main`. **Morocco** — see provenance below. Open core: a paid Enterprise Edition adds theming, SLA and LTS. |
| SAEP 2026 — Agentes de IA e Ferramentas | [armandokeller/SAEP2026-Agentes-IA-e-Ferramentas](https://github.com/armandokeller/SAEP2026-Agentes-IA-e-Ferramentas) | **MIT** (`LICENSE`) | 0 / 0 | Eight-step agent-engineering curriculum (`ex0`–`ex8`): environment check, chat, conversation memory, tool calling, agentic loop, LangGraph, **MCP integration**, **human-in-the-loop approval**, then an exercise implementing custom MCP tools. Runs on a **small local model (Qwen 3.5-4B via LM Studio)** with **no cloud dependency**. Workshop material from the Escola Politécnica academic week at **Unisinos, Brazil**. Python. |

### Provenance of Open TutorAI, which this KB had not recorded

The twelfth pass recorded the repository, its licence and its fork inversion. It did not
record **who stands behind it**, and that is the part a client conversation turns on.

- **Origin: Agadir, Morocco.** The **IRF-SIC Laboratory, Ibn Zohr University**, with the
  **Regional Centre for Education and Training Professions (CRMEF) Souss-Massa**. Authors
  El Hajji · Ait Baha · Dakir · Fadili · Es-Saady (`arXiv:2602.07176`).
- **It is state-funded.** The work is supported by Morocco's **Ministry of Higher
  Education, Scientific Research and Innovation**, the **Digital Development Agency (DDA)**
  and the **CNRST**.

Both facts were absent from this KB: `Agadir` and `Ibn Zohr` returned **zero** matches
across every file before this pass. The consequence is a market fact, not a trivia fact:
**the most capable permissive AI-native education platform on this shelf is an African,
government-sponsored project**, which is a reference a public-sector buyer in EMEA or
LATAM can be pointed at directly.

### The licence warning on the row above — the holder is not identifiable

The payload reads:

```
Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev
All rights reserved.
```

**`R2D-dev` appears nowhere else.** Not in the README, not in the repository
documentation, and not in any search result this pass could reach. The licence is a clean
BSD-3-Clause and the grant is real; the **legal entity named as the holder is
unidentifiable from any public artefact of the project**. For an engagement that
redistributes this code to a client, the holder is the party a warranty or indemnity
question routes to — so this is the diligence item to raise upstream before it is proposed.

Two further details on the same payload:

- **`All rights reserved.` sits directly above a permissive grant.** The phrase contradicts
  nothing legally — it is vestigial — but it is exactly the string that makes a
  procurement reviewer stop. Expect to explain it.
- **The copyright range ends at 2025** while the repository is active in 2026, and the
  repository is **published as Apache-2.0 in third-party catalogues** while the payload is
  BSD-3-Clause. The twelfth pass caught the catalogue error; this pass confirms it from the
  payload independently, at the **same 1,531 bytes**.

### The 14th failure mode: a permissive body with no title line reads as unclassified

This pass's probe classified licence family by matching the **title line** of the payload
(`MIT License`, `Apache License`, …). `open-tutor-ai-CE` returned **HTTP 200 with a
payload that matched nothing** — because BSD-3-Clause is frequently distributed as the
**bare three-condition body with no heading at all**. A title-line classifier reports that
as *unclassified* and an automated gate would reject a genuinely permissive component.

This KB already knew the shape — `crewAIInc/crewAI` is recorded as *"MIT (`LICENSE`, body
text — no title line)"* — but it had not been written down as a **failure mode of the
instrument**. It is one: **classify on the operative clauses, not on the heading.** The
three-condition BSD body is identifiable by its third clause (*"Neither the name of the
copyright holder nor the names of its contributors may be used to endorse"*) with no
heading present anywhere.

### Recorded and excluded: ClawTeam

[HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) — **MIT** (`LICENSE`), **5.5k★**,
Python, v0.2.0 (Mar 2026). Agent-swarm orchestration: agents spawn sub-agents, divide
tasks, communicate over a file and P2P transport, isolated per-agent workspaces via git
worktrees. **It is not education software** and it is not shelved as one.

It is recorded because of **how it was found**: `HKUDS` is the organisation that publishes
**DeepTutor**, the largest agent in this KB. An **organisation sweep** — a channel this KB
used in its fourth pass — pulls ClawTeam in on the strength of the org name alone, and a
5.5k★ MIT repository from a known-good education org is precisely the kind of row that
gets shelved without being read. **The org is not the subject.** Logged here so the next
org sweep does not re-find it as a discovery.

## Added in the fourteenth pass of 2026-10-06 — the platform-name channel, and 24 verified rows

The thirteenth pass closed with four instructions. This pass took the first three and the
first one came back with a different answer than the pass that ordered it expected.

**Instruction 1 was: "take the ~20-server education MCP cluster from `archive/`."** The
cluster is **98 addresses**, not ~20 — the estimate was low by a factor of five. Every one
was probed: `git ls-remote --symref` for existence and real default branch, then up to
**20 licence filenames** on `raw.githubusercontent.com` against that branch, then
`package.json` / `pyproject.toml` / `setup.py` for a manifest declaration.

### Finding 1 — the archive MCP cluster is not decayed, and it is not ungranted

| Verdict | Count of 98 | Detail |
|---|---|---|
| **Licence payload read** | **76** | 68 MIT · 2 Apache-2.0 · 2 Unlicense · 2 GPL-3.0 · 2 AGPL-3.0 |
| No payload under 20 filenames | 17 | of which **7 declare a licence in a manifest only** |
| 🔴 **Gone — `ls-remote` cannot reach them** | **5** | listed below |

🟢 **72 of 98 addresses (73%) carry a permissive payload.** The pass that ordered this work
predicted decay ("expect decay and record it as supply data") on the strength of 2 dead MCP
servers in a sample of 4 dead addresses. Measured across the whole cluster, **decay is 5%**,
and the cluster is the most uniformly permissive block this KB has ever censused — 68 of 76
payloads are a plain 1.0–1.1 KB MIT. **The prediction was wrong, and it was wrong because a
2-of-4 ratio was read as a rate.**

🔴 **The 5 that no longer resolve:**

| Address | What it was |
|---|---|
| `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` | MCP server for the Ed-Fi SDK. Confirms the thirteenth pass. The rest of Ed-Fi is alive and Apache-2.0; Ed-Fi-over-MCP remains a **build**. |
| `appliedrelevance/frappe_mcp_server` | Frappe/ERPNext MCP server. The KB's note on its 3-byte PyPI licence field now has no upstream to re-read. |
| `imazhar101/mcp-canvas-server` | Canvas MCP server. |
| `owentaylor/canvas-mcp` | Canvas MCP server. |
| `radhepa/Teacher-MCP` | Teacher-facing MCP server. |

**Three of the five are Canvas or teacher-facing servers** — the densest, most duplicated
part of the cluster. Decay here concentrates in the tier where many authors built the same
thing, not in the tier that is hard to build.

### Finding 2 — the case-variant hypothesis does not reproduce, and that is worth as much as if it had

The thirteenth pass's instruction 2 was to re-probe ungranted verdicts with case variants,
because `LICENSE.TXT` had turned a 470★ Apache-2.0 repository into a false absence. This
pass probed all 98 addresses with the full case ladder — `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `LICENSE.TXT`, `LICENSE.MD`, `License`, `License.md`, `License.txt`,
`license`, `license.md`, `license.txt`, `LICENCE`, `LICENCE.md`, `LICENCE.txt`, `COPYING`,
`COPYING.txt`, `LICENSE-MIT`, `LICENSE.rst`, `docs/LICENSE`.

🔵 **76 of 76 payloads were at plain `LICENSE`.** Not one case variant, British spelling or
`COPYING` fallback paid out across 98 repositories.

**So the 13th failure mode is real but rare, and this is the number to carry:** the case
ladder costs ~19 extra requests per ungranted repository and buys, in this cluster, nothing.
Keep it in the gate for a **single high-value asset** whose absence would change a
recommendation; do not pay it across a census. The 470★ Apache-2.0 repository remains the
exception that justified finding the mode, not evidence of a systematic bias.

### Finding 3 — one default branch is an agent-generated branch, and `main` would have lied

`DaviPac/Classroom-mcp` resolves, and its default branch is:

```
claude/publish-classroom-aluno-mcp-9g61ee
```

🔴 **There is no `main`.** A probe hardcoding `main` or `master` — which is what this KB's
earlier passes did — returns 404 on every filename and writes the repository down as
ungranted. It is not: its `package.json` declares MIT (see Finding 4 for what that is
worth).

🟢 **This is the concrete vindication of instruction 3.** `ls-remote --symref` is now the
standing first step not because it is tidy but because **an agent-published branch is a
default branch in the wild**, and that is a new fact about the supply this KB measures.

### Finding 4 — 7 of the 17 "ungranted" repositories are *declared and ungranted*, which is worse than silent

Of the 17 addresses with no licence payload under 20 filenames, 7 carry a licence
**identifier in a build manifest** and nothing else:

| Address | Declares | Where | ★ |
|---|---|---|---|
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | MIT | `package.json` | **103** |
| [`DaviPac/Classroom-mcp`](https://github.com/DaviPac/Classroom-mcp) | MIT | `package.json` | not read |
| [`SalShah20/classroom_mcp`](https://github.com/SalShah20/classroom_mcp) | MIT | `package.json` | 1 |
| [`ink-waffle/moodle-mcp`](https://github.com/ink-waffle/moodle-mcp) | MIT | `package.json` | not read |
| [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | MIT | `package.json` | not read |
| [`pnp-v/bo-google-classroom-mcp-server`](https://github.com/pnp-v/bo-google-classroom-mcp-server) | ISC | `package.json` | not read |
| [`vnschneider/suap-mcp`](https://github.com/vnschneider/suap-mcp) | AGPL-3.0-or-later | `pyproject.toml` | not read |

🔴 **`DMontgomery40/mcp-canvas-lms` is the second-highest-starred Canvas MCP server on
GitHub at 103★, and it ships no licence text.** The GitHub API returns
`license: null` for it; the `package.json` says MIT. This KB has already established the
rule (a manifest identifier is an **identifier**, not a grant) — what is new is its **cost**:
the rule disqualifies the most-starred asset in the second-largest platform tier.

**This is a one-commit fix for the maintainer and it is worth asking for.** 7 of 17 is not a
licensing culture problem; it is a packaging default — `npm init` writes a `license` field
and no file. For a Globant engagement the practical rule stands unchanged: **no payload, no
deliverable.** `vnschneider/suap-mcp` is the one to read twice — it declares **AGPL-3.0**,
so if the payload ever lands it is a copyleft constraint, not a permissive win.

### Finding 5 — the platform-name channel: 80% licensed, against 25% for the language channel

**Instruction 4's channel question, answered.** The thirteenth pass varied the *language* of
the query and concluded the language was the wrong variable (3 licensed of 12, and only 1 was
education software). This pass varied the **platform name** instead — Canvas, Moodle,
Brightspace, Blackboard, Google Classroom, Skolverket, Smartschool, KUPID, NTU COOL — and ran
each one **alone**.

| Channel | Candidates | Licensed | Rate | Education software |
|---|---|---|---|---|
| Language (13th pass) | 12 | 3 | **25%** | 1 of 3 |
| **Platform name (this pass)** | **20** | **16** | **80%** | **16 of 16** |

🟢 **Every licensed find is education software, because the platform *is* an education
platform** — the channel cannot drift into the generalist agent layer the way a topic or
star-count query does. And it **places each find by region for free**: a platform is an
institution in a country. That is the property this KB has been missing, and it is the
answer to its own standing complaint that findings arrive unplaced.

### The rows — 24 verified assets, 22 of them new to this KB

Licences read from each repository's own payload on the real default branch, 2026-10-06.
Stars from the GitHub REST search API the same day.

#### The platform tier — Brightspace and Blackboard, which this KB had never recorded

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **Brightspace MCP Server** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** (`LICENSE`, 1,068 B) | **57** (27 forks) | **North America** | **The fourth major LMS arrives on this shelf.** D2L Brightspace: grades, due dates, assignments, announcements, rosters, syllabus, course content. Published to npm (`npx brightspace-mcp-server@latest`), CI green, Node ≥ 20, "works with any school". Author at Purdue; D2L is Canadian. **The reference row for any Brightspace engagement.** |
| Brightspace MCP (multi-auth) | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | **MIT** (`LICENSE`, 1,070 B) | 12 | Global | The **engineering** reference rather than the feature reference: multi-strategy authentication (TOTP, OAuth, browser), retry / circuit-breaker / cache tiers, and **opt-in write operations**. Read this one before designing a write path into any LMS. |
| Brightspace MCP (Purdue) | [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) | **Apache-2.0** (`LICENSE`, 11,357 B) | 6 | North America | Python. The only **Apache-2.0** asset in the Brightspace tier — relevant where a client's policy prefers an explicit patent grant over MIT. |
| Blackboard Learn MCP + RBAC | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | **MIT** (`LICENSE`, 1,063 B) | 2 | Global | Blackboard Learn REST API over HTTP or stdio, with **RBAC middleware for role-based access control**. 2★ and the most governance-aware design in the whole 98-address cluster: role separation is the control an education deployment is actually audited on. |
| Blackboard Learn Ultra MCP | [NiccoloSalvini/mcp-blackboard-ucsc](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) | **MIT** (`LICENSE`, 1,073 B) | 0 | EMEA | Blackboard Learn Ultra over the public REST API. Python. |

#### The ministry and national-platform tier — the first of its kind in this KB

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **Skolverket MCP** | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP) | **MIT** (`LICENSE`, 1,093 B) | 12 | **EMEA** (Sweden) | 🟢 **A national curriculum as an agent-callable surface.** Exposes *all* of Skolverket's (Swedish National Agency for Education) open APIs: the **Läroplan / syllabus API**, the **Skolenhetsregistret** school-unit register, and the Planned Educations API. Published in the **official MCP Registry** (`io.github.isakskogstad/Skolverket-MCP`). ⚠️ The copyright line reads *"Skolverket Syllabus MCP Contributors"*, **not the agency** — this is a third-party wrapper of a public API, so the MIT covers the wrapper and the agency's own terms govern the data. |
| Udir MCP (Norway) | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** — no payload under 20 filenames, no manifest field | not read | **EMEA** (Norway) | Norwegian Directorate for Education (Udir) school (NSR) and kindergarten (NBR) registry data. **Found in the MCP Registry, and ungranted.** Recorded as the EMEA counter-case to Skolverket: two Nordic education-ministry wrappers, one usable, one not. |
| Smartschool MCP | [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP) | **MIT** (`LICENSE`, 1,069 B) | 5 | **EMEA** (Belgium) | Smartschool, the dominant LMS in Flemish education. Python ≥ 3.10, on **PyPI** (`smartschool-mcp`), with CI, codecov and a published MCP name (`io.github.MauroDruwel/smartschool-mcp`). Small star count, real release engineering. |
| KUPID portal MCP | [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp) | **MIT** (`LICENSE`, 1,068 B) | 13 | **APAC** (Korea) | Korea University's KUPID portal: notices, library seat availability, weekly assignments. On **PyPI** (`ku-portal-mcp`). Korean-language README. **The thirteenth pass's Korean-language query did not find this; the platform name did** — see the method note below. |
| NTU COOL | [kc0506/ntucool](https://github.com/kc0506/ntucool) | **MIT** (`LICENSE`, 1,066 B) | 10 | **APAC** (Taiwan) | National Taiwan University's COOL platform: a single `cool` binary that is CLI, MCP server (`cool mcp`) and SDK, **plus a Claude Code plugin** (`/plugin marketplace add kc0506/ntucool`) shipping skills and commands. ⚠️ Its own README states it is **unofficial**. The first asset in this KB to ship a Claude Code plugin as a distribution channel. |

#### Assessment, study and tutoring agents

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **ICTExam MCP** | [ictinnovations/ictexam-mcp](https://github.com/ictinnovations/ictexam-mcp) | **MIT** (`LICENSE`, 1,114 B) | 16 | **APAC** (Pakistan) | 🟢 **A vendor shipping MIT into the assessment gap.** MCP server for **ICTExam**, a commercial AI exam authoring, delivery and **auto-grading** platform: read exams, gradebooks and per-question item analysis; parse a question paper into a structured exam with AI and publish to students — **only when writes are explicitly turned on**. On npm. Holder is a company (ICT Innovations), so the grant is corporate, not a student project. **The write gate is the design this KB has been asking for in trend 7.** |
| SmartStudy Agent | [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | **MIT** (`LICENSE`, 1,067 B) | 57 | Global | A **reinforcement-learning policy** chooses what to study next, an **FSRS** memory model schedules review, an LLM generates the quizzes between. Browser, terminal and MCP. The second auditable mastery instrument in this KB after OATutor's Bayesian Knowledge Tracing — and a different family (RL + FSRS vs BKT), which matters when a client asks why a sequencing decision was made. |
| Shiori (栞) | [kaorii-ako/Shiori-v1](https://github.com/kaorii-ako/Shiori-v1) | **MIT** (`LICENSE`, 1,073 B) | 45 | Global | Study companion: Google Classroom sync, SRS flashcards, weighted grade calculator with GPA prediction, syllabus-to-study-plan, quiz generation, MCP server. React/Vite + Supabase, PWA, Docker, self-hostable. **Bring-your-own Gemini key** — the cost model, not a subscription. The highest-starred asset in the Google Classroom tier. |
| OpenStudy | [OpenStudy-dev/OpenStudy](https://github.com/OpenStudy-dev/OpenStudy) | **MIT** (`LICENSE`, 1,068 B) | **75** | EMEA | Self-hostable personal study dashboard — courses, schedule, lectures, topics, deliverables, tasks — reachable by an agent from browser, phone, desktop or Claude Code. FastAPI + React 19 + Postgres 16. Bilingual DE/EN README. The cleanest **self-hosted + agent-reachable** reference stack on this shelf. |
| mydy LMS helper | [Deeptanshuu/mydy-lms-helper](https://github.com/Deeptanshuu/mydy-lms-helper) | **MIT** (`LICENSE`, 1,070 B) | 7 | APAC (India) | LMS assistant for the mydy platform. |

#### The Canvas and Moodle tiers — the duplicated middle, with the licensed ones named

| Agent | Repo | Licence (payload) | ★ | What it does |
|---|---|---|---|---|
| canvas-ed-mcp | [r1ckyIn/canvas-ed-mcp](https://github.com/r1ckyIn/canvas-ed-mcp) | **MIT** (`LICENSE`, 1,056 B) | 15 | Canvas LMS MCP server. ⚠️ Its MIT copyright line carries **a year and no holder name** — valid, but name the holder before vendoring. |
| canvas-mcp (Huijts) | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | **MIT** (`LICENSE`, 1,065 B) | 12 | Canvas LMS MCP server, © 2024 R. Huijts — the earliest copyright year in this pass's set. |
| canvas-mcp (Keluskar) | [aryankeluskar/canvas-mcp](https://github.com/aryankeluskar/canvas-mcp) | **ISC** (`LICENSE`, 746 B) | 11 | Canvas LMS MCP server. **The second ISC asset in this KB** — functionally MIT, OSI-approved, and still rejected by a `license:mit OR license:apache-2.0 OR license:bsd` filter. Reinforces the thirteenth pass's allow-list finding. |
| moodle-mcp (Ribeiro) | [1alexandrer/moodle-mcp](https://github.com/1alexandrer/moodle-mcp) | **MIT** (`LICENSE`, 1,074 B) | **18** | Moodle MCP server. The highest-starred **permissive** Moodle MCP server found this pass after `peancor/moodle-mcp-server` (43★), which this KB already carries. |
| moodle-mcp (Lefebvre) | [Snaw80/moodle-mcp](https://github.com/Snaw80/moodle-mcp) | **MIT** (`LICENSE`, 1,072 B) | 4 | Moodle MCP server. |
| Google Classroom MCP | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** (`LICENSE`, 1,063 B) | 6 (9 forks) | 🔵 **The highest-starred *dedicated* Google Classroom MCP server on GitHub.** 6★ — and that is the finding, not the row; see Finding 6. More forks than stars, which is what a utility people deploy rather than watch looks like. |
| Google Workspace for Education MCP | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** (`LICENSE`, 1,087 B) | 1 | Docs, Sheets, Slides, **Forms**, Drive and Classroom in one server. TypeScript. The Forms surface is the one the others lack, and Forms is where K-12 assessment actually lives. |
| AI School (course catalogue) | [Lilly-Tech-Collab/ai-school-mcp](https://github.com/Lilly-Tech-Collab/ai-school-mcp) | **MIT** (`LICENSE`, 1,405 B) | not read | Search and read 550+ free AI course tracks and 21,000+ lessons. Found in the **MCP Registry**. An enablement-content surface, not a platform integration. |
| Moltline Educator | [GarphenGate/moltline-mcp](https://github.com/GarphenGate/moltline-mcp) | **MIT** (`LICENSE`, 1,072 B) | not read | 8 skills across curriculum, classroom, **accommodations** and exam prep. Found in the MCP Registry. Accommodations is a vocabulary no other asset in this KB covers, and it is a legal requirement in both US and EU school systems. |

### Finding 6 — the supply map, and the hole is K-12 administration

Measured with GitHub REST `total_count`, one platform name per query, 2026-10-06:

| Platform tier | `total_count` | Highest ★ | Highest-starred **permissive, payload-backed** asset |
|---|---|---|---|
| Canvas LMS | **117** | 278 | `vishalsachdev/canvas-mcp`, MIT (already shelved) |
| Moodle | **86** | 43 | `peancor/moodle-mcp-server`, MIT (already shelved) |
| **Brightspace / D2L** | **23** | 57 | `RohanMuppa/brightspace-mcp-server`, MIT 🆕 |
| **Google Classroom** | **17** | 45 (Shiori) | `faizan45640/...`, MIT, **6★** 🆕 |
| **Blackboard Learn** | **5** | 2 | `nitsuah/bb-mcp`, MIT 🆕 |
| Open edX | **1** | 1 | — (AGPL-3.0; already recorded) |
| 🔴 **PowerSchool (US K-12 SIS)** | **0** | — | **none — the tier does not exist** |

🔵 **Open-source MCP coverage tracks the higher-education install base and ignores K-12.**
Canvas and Moodle together hold **203 of the 249** repositories measured. Blackboard, with a
large global university estate, has **5**. Google Classroom — the widest K-12 reach of any
platform on this table — has **17**, and its best dedicated server has **6★**. PowerSchool,
the dominant US K-12 student information system, measures **`total_count: 0`**.

**This is the clearest build-versus-adopt signal in this KB.** For a higher-ed engagement on
Canvas or Moodle, adopt: the shelf is deep, permissive and duplicated. For **K-12
administration**, there is nothing to adopt and nothing to compete with — a Globant-built
Google Classroom or PowerSchool MCP server enters an empty tier, and the governance surface
(student records, guardians, accommodations) is exactly the regulated part.

### Finding 7 — a bespoke "Community License" in the education MCP tier, and it is unusable

[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom)
carries **`LICENSE.md`, 6,489 B**, titled **"AStheTECH Community License (ACL)"**. Read in
full. It is not OSI-approved and it is not near-miss permissive:

- Grant: *"limited, non-exclusive, non-transferable"*; *"All rights not expressly granted are reserved."*
- Prohibited without written authorisation: **sell, license, sublicense, lease or otherwise commercially exploit**; **offer the software as part of any hosted service, SaaS platform or API service**; **rebrand or white-label**; build anything *"substantially similar to or competitive with"* it.
- Distribution permitted only where *"strictly non-commercial in nature."*
- **Termination is automatic and immediate on any breach**, with destruction of derivatives.

🔴 **Verdict: unusable in client work, under every clause that matters.** A Globant
deliverable is commercial, is usually hosted, and is usually rebranded. The word
*"Community"* in the title is doing the opposite of what a reader skimming a repository
listing would assume, and GitHub's sidebar shows such a file as a generic "License".

**This is trend 23's label-versus-grant finding at its sharpest**: not a mislabelled
permissive licence, but a **bespoke proprietary licence whose name reads as an open one**.
The gate is unchanged and it caught this: read the payload, and when the first line is not a
known licence title, read all of it.

### Finding 8 — 11 addresses measured this pass and genuinely ungranted

Probed with the full 20-filename ladder on the real default branch, plus manifests. No grant
of any kind:

| Address | Platform | ★ |
|---|---|---|
| [`lucanardinocchi/canvas-mcp`](https://github.com/lucanardinocchi/canvas-mcp) | Canvas | **22** |
| [`plyght/canvas-mcp`](https://github.com/plyght/canvas-mcp) | Canvas | 14 |
| [`joshuasoup/d2l-mcp`](https://github.com/joshuasoup/d2l-mcp) | Brightspace | 13 |
| [`haanhtuandev/vgu-mcp`](https://github.com/haanhtuandev/vgu-mcp) | Vietnamese-German University (APAC) | 10 |
| [`zainf2327/mcp-classroom`](https://github.com/zainf2327/mcp-classroom) | Google Classroom — **auto-grades submissions** | 6 |
| [`kesaruhasun/mcp-sliit-courseweb`](https://github.com/kesaruhasun/mcp-sliit-courseweb) | SLIIT, Sri Lanka (APAC) | 6 |
| [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) | Blackboard, Univ. of Queensland + Okta SSO | 0 |
| [`shimahikojin/google-classroom-mcp`](https://github.com/shimahikojin/google-classroom-mcp) | Google Classroom | 0 |
| [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | Udir, Norway (EMEA) | not read |
| [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | US school districts (North America) | not read |
| [`710git/course-drift-oracle`](https://github.com/710git/course-drift-oracle) | course-drift reports | not read |

⚠️ **`zainf2327/mcp-classroom` auto-grades student submissions and carries no licence.** Of
everything ungranted in this pass, that is the one whose function is most regulated and
whose grant is most needed.

### The method note for this pass

**Four instrument facts, three of them cautionary.**

1. 🔴 **Boolean `OR` in GitHub repository search destroys specificity.** The LATAM probe
   `sigaa OR suap OR siga mcp server` returned **`total_count: 160,659`** — the generalist
   MCP layer (`awesome-mcp-servers` 95.9k★, `headroom`, `private-gpt`, `playwright-mcp`).
   The same platform names queried **one at a time** return tiers in the single and double
   digits. **Never OR platform names.** Every count in Finding 6 was measured with one name
   per query for exactly this reason.
2. 🔵 **`minimal_output: true` on the search API returns stars, forks, topics and the real
   default branch, and omits the licence.** That is the right shape for this KB: the licence
   must come from the payload anyway, and the full objects overflow a single tool result at
   ten rows.
3. 🟢 **`ls-remote --symref` first, every time** — it answers existence and default branch in
   one call with no API dependency, and Finding 3 is what happens without it.
4. ⚠️ **A language channel and a platform channel answer different questions.** The Korean
   asset `SonAIengine/ku-portal-mcp` (MIT, 13★) existed when the thirteenth pass ran its
   Korean-language query and that query did not surface it. The platform name **KUPID** did.
   The thirteenth pass's conclusion — *"the language was the wrong variable"* — holds and
   gets sharper: **what places an asset is the institution, and the institution's name is
   usually searchable in English even when its README is not.**

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS tier, and the first non-licence blocker in this KB

The fourteenth pass handed this pass two instructions. This section answers the second:
*"run the platform-name channel against the SIS and ministry tiers, which this pass only
sampled."* It was the right instruction and it overturns the finding that produced it.

**Every licence below was read from the repository's own payload** on 2026-10-06, on the real
default branch confirmed by `ls-remote --symref`. 44 addresses probed, 36 carried forward.

### Finding 1 — "the tier does not exist" is wrong, and this KB already held the refutation

The fourteenth pass's Finding 6 recorded `powerschool` at **`total_count: 0`** and concluded
**"none — the tier does not exist"**. Measured again today, four query shapes:

| Query | `total_count` |
|---|---|
| `powerschool` | **590** |
| `powerschool in:name` | **354** |
| `powerschool mcp` | **3** |
| `powerschool mcp server` | **1** |

🔴 **The minimum over four shapes is 1, not 0.** The zero is not reproducible as a
query-shape artifact; it was an instrument error written down as a property of the world.

🔴 **And the refutation was already inside this KB before the claim was made.** An earlier
pass had shelved [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool)
and [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) under
*"MCP over SIS"*. The fourteenth pass wrote "the tier does not exist" over its own record.

🔵 **The method rule this adds:** a zero from a search channel is a claim about the channel.
Before it is written as a property of the supply, **grep this KB for the thing claimed
absent.** That check costs one command and would have caught this.

### Finding 2 — the headline: MIT is granted, and the tier is still not deployable

[`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) — MIT,
`LICENSE`, 1,067 B, holder *"Chris Hall"*, 20 tools over Infinite Campus — is the one
payload-backed MCP server on a US K-12 SIS. Its own README quotes the vendor's Terms of Use:

> Users may not access, use, or search the Services by any means other than our publicly
> supported interfaces (for example, scraping or using the content to train artificial
> intelligence software).

And then states, of itself:

> This server uses Infinite Campus's mobile-app JSON endpoints (`/campus/api/oneRosterCampus`,
> `/portal/api/...`) which are not "publicly supported interfaces" — IC may treat this as a
> ToS violation.

It further restricts itself to **"personal, parent/student use only"**, is *"not affiliated
with, endorsed by, sponsored by, or in partnership with Infinite Campus, Inc. or any school
district"*, says **"do not use it to bulk-extract student data … or train AI models on
student records"**, and invokes **FERPA and COPPA** on the output.

🔴 **This is a new axis, and it is the first blocker in this KB that is not a licence.**
Twenty-three recorded licence failure modes all answer one question: *may we copy and
redistribute this code?* Here the answer is **yes, MIT, unambiguously** — and the component
is still not shippable, because a different grant is missing: **the right to reach the data.**
The copyright holder gave us the code. The SIS vendor did not give us the API.

⚠️ **The two grants are orthogonal, and only one of them is in the repository.** No licence
audit, however rigorous, detects this. It is not in `LICENSE`; it is in a third party's ToU.

⚠️ **Provenance of the quotation, stated precisely.** The ToU text above was read today from
**the repository's own README**, where the maintainer records having read the vendor's terms
on **2026-05-23**. The vendor's page itself — `infinitecampus.com/terms/terms-of-use` — is
**blocked by this environment's egress proxy** (`connect_rejected`), so this KB has **not**
verified it first-hand, and a ToU can change without notice. 🔵 **The finding does not
depend on the quotation being current**: the maintainer's own statement that the server
calls non-public endpoints and may violate the vendor's terms is first-hand evidence from
the party best placed to know. **Next pass: re-read the vendor page from an unblocked
network and date it.**

🔵 **What it does to the fourteenth pass's conclusion.** That pass said *"for K-12
administration there is nothing to adopt… a Globant-built PowerSchool MCP server enters an
empty tier."* The tier is **not** empty — and the build recommendation **survives anyway, for
a stronger reason**: what you cannot adopt is not the code but the access path. Building your
own MCP server does not fix it either. **What fixes it is a contract and the vendor's official
API** (PowerSchool and Infinite Campus both publish OneRoster endpoints; this KB's
interoperability tier already carries the permissive OneRoster/Ed-Fi implementations).

### Finding 3 — the access-legitimacy axis, read from the repositories' own words

This is not one maintainer being unusually careful. The tier is built on unofficial access and
says so:

| Asset | What it says about itself |
|---|---|
| [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | *"Unofficial — not affiliated with Infinite Campus. AI-maintained."* + the ToU quotation above |
| [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api) | *"Uma biblioteca de **Web Scraping**, para acessar o SIGAA"* — and it is **archived** |
| [`kc0506/ntucool`](https://github.com/kc0506/ntucool) | *"This is an **unofficial** project. Use it at your own risk, and responsibly."* |
| [`elisaado/somtoday-api-docs`](https://github.com/elisaado/somtoday-api-docs) | repository topic: **`reverse-engineering`** |
| [`Underlyingglitch/SomtodaySSOLogin`](https://github.com/Underlyingglitch/SomtodaySSOLogin) | topics `reverse-engineering`, `sso-authentication` — **archived** |
| [`cqm3ron/bromcom-scraper`](https://github.com/cqm3ron/bromcom-scraper) | *"a python script to host an API to get bromcom homework assignment data"* |

🔴 **And a cookie-bridge architecture, which is the mechanism the ToS language targets.**
`infinitecampus-mcp`'s no-password auth path installs a browser extension
([`nullnet-app/contextmint-bridge`](https://github.com/nullnet-app/contextmint-bridge), the
former `fetchproxy`), which reads the HttpOnly `JSESSIONID` and `XSRF-TOKEN` from a
logged-in tab and hands them to the MCP server, which then calls the API directly. It is an
elegant answer to *"the vendor has no agent API"* — and it is precisely *"means other than
our publicly supported interfaces."*

🔵 **Record it as an anti-pattern for client work and a signal for roadmaps.** A cookie bridge
in a repository is evidence that the install base wants agent access the vendor does not yet
sell. That is a product opportunity, not a deliverable component.

### Finding 4 — the PowerSchool grant is one layer down from where you want it

| Layer | Asset | ★ | Payload |
|---|---|---|---|
| MCP server | [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) | 2 | 🔴 **none** (6 filenames, `main`) |
| MCP server | [`zuvy/ps-mcp-server`](https://github.com/zuvy/ps-mcp-server) | 1 | 🔴 **none** (6 filenames, `main`) |
| API client (Node) | [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **34** | 🟢 **MIT**, 1,072 B — *Ayden Panhuyzen* |
| API client (PHP) | [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | 20 | 🟢 **MIT**, 1,101 B |
| API client (Python) | [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | 16 | 🟢 **MIT**, 1,082 B |
| API client (Python) | [`TEAMSchools/powerschool`](https://github.com/TEAMSchools/powerschool) | 23 | ⚠️ **GPL-3.0**, 35,149 B — **archived** |

🔴 **Both PowerSchool MCP servers are ungranted. Every PowerSchool API client but one is MIT.**
The grant exists exactly one layer below the layer an agent engagement wants.

🟢 **So the recipe writes itself, and it is the opposite of "build the integration":** take an
MIT client, write the thin MCP wrapper yourself, and spend the saved effort on the access
contract. Shipped as **P25** in `compose/patterns.md`.

### The rows — 36 addresses, placed by country, licence read from the payload

**North America** — US K-12 and higher-ed SIS

| Repo | ★ | Licence (payload) | What it is |
|---|---|---|---|
| [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | 34 | **MIT** (1,072 B) | Node.js client, PowerSchool SIS API |
| [`TEAMSchools/powerschool`](https://github.com/TEAMSchools/powerschool) | 23 | GPL-3.0 (35,149 B) | Python client — **archived** |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | 20 | **MIT** (1,101 B) | PHP client |
| [`shinyquagsire23/InfiniteCampusAPI`](https://github.com/shinyquagsire23/InfiniteCampusAPI) | 20 | ⚠️ **WTFPL v2** (474 B) | Java Infinite Campus client |
| [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | 16 | **MIT** (1,082 B) | Python client |
| [`sas-fossdev/saspes`](https://github.com/sas-fossdev/saspes) | 13 | AGPL-3.0 (34,522 B) | PowerSchool browser extension |
| [`NCSIS/InfiniteCampus-Vendor-Integration`](https://github.com/NCSIS/InfiniteCampus-Vendor-Integration) | 13 | 🔴 none | PowerShell vendor integration |
| [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | 4 | **MIT** (1,067 B) | **MCP server, 20 tools** — ⚠️ see Finding 2 |
| [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) | 2 | 🔴 none | MCP server |
| [`zuvy/ps-mcp-server`](https://github.com/zuvy/ps-mcp-server) | 1 | 🔴 none | MCP server |
| [`bnnadi/Sky`](https://github.com/bnnadi/Sky) | 1 | 🔴 none | React Native **demo** — not an integration |

**EMEA** — placed by country

| Repo | ★ | Licence (payload) | Country / system |
|---|---|---|---|
| [`SapuSeven/BetterUntis`](https://github.com/SapuSeven/BetterUntis) | **300** | ⚠️ GPL-3.0 (35,149 B) | DE/AT — WebUntis, Kotlin Android |
| [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **241** | 🟢 **MIT** (1,062 B) | FR — PRONOTE, Python wrapper |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **214** | 🔴 **none** (6 filenames, `master`) | DE/AT — the costliest absence in this tier |
| [`Litarvan/pronote-api`](https://github.com/Litarvan/pronote-api) | 192 | 🔴 none | FR — PRONOTE |
| [`JonasJoKuJonas/homeassistant-WebUntis`](https://github.com/JonasJoKuJonas/homeassistant-WebUntis) | 148 | 🟢 **MIT** (1,062 B) | DE/AT |
| [`delphiki/hass-pronote`](https://github.com/delphiki/hass-pronote) | 105 | 🔴 none | FR |
| [`elisaado/somtoday-api-docs`](https://github.com/elisaado/somtoday-api-docs) | 87 | 🔴 none | NL — SOMtoday API documentation |
| [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | 81 | 🟢 **BSD-2-Clause** (1,505 B) | DE/AT — *Markus Unterwaditzer* |
| [`magister-api/magister`](https://github.com/magister-api/magister) | 49 | 🟢 **MIT** (1,085 B) | NL — Magister 6, PHP |
| [`ninocss/UntisPlus`](https://github.com/ninocss/UntisPlus) | 44 | 🟢 **MIT** (1,064 B) | DE/AT — Flutter, **on-device AI assistant** |
| [`untisapi/untis4j`](https://github.com/untisapi/untis4j) | 33 | ⚠️ LGPL-3.0 (7,378 B) | DE/AT — Java |
| [`Jona-Zwetsloot/Somtoday-Mod`](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | 16 | 🔴 **CC BY-NC-SA 4.0** (17,056 B) | NL — **NonCommercial: unusable** |
| [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | 15 | 🟢 **MIT** (1,066 B) | NL — SOMtoday REST client |
| [`sikkepitje/TeamSync`](https://github.com/sikkepitje/TeamSync) | 9 | ⚠️ GPL-3.0 (35,149 B) | NL — Magister → MS School Data Sync |
| [`RichardSlater/bromcom-timetable-formatter`](https://github.com/RichardSlater/bromcom-timetable-formatter) | 1 | 🟢 **MIT** (1,071 B) | UK — Bromcom, Rust |
| [`DPlazma/assessapp`](https://github.com/DPlazma/assessapp) | 0 | 🟢 **MIT** (1,064 B) | UK — Arbor MIS + **AI tagging**, Django |

**APAC** — and the whole tier is one university

| Repo | ★ | Licence (payload) | Country / system |
|---|---|---|---|
| [`AkizumiFox/NTU-COOL-Assignment-Status-Viewer`](https://github.com/AkizumiFox/NTU-COOL-Assignment-Status-Viewer) | 19 | 🟢 **MIT** — at **`LICENCE`** (1,056 B) | TW — NTU COOL |
| [`kc0506/ntucool`](https://github.com/kc0506/ntucool) | 10 | 🟢 **MIT** (1,066 B) | TW — **Rust CLI + MCP server** |
| [`kuang-che/NTU-COOL-Preview-Tool-extension`](https://github.com/kuang-che/NTU-COOL-Preview-Tool-extension) | 8 | 🟢 **MIT** (1,066 B) | TW |

🔵 **NTU COOL is Canvas-based**, which is why this is the one APAC institution with a tier:
the asset authors inherit Canvas's documented API. The platform channel found an institution;
the *reason* it had something to find is the LMS underneath it.

**LATAM** — Brazil, and it is the deepest national tier in this pass

| Repo | ★ | Licence (payload) | Institution / system |
|---|---|---|---|
| [`aquario-ufpb/aquario`](https://github.com/aquario-ufpb/aquario) | 84 | 🟢 **MIT** (1,070 B) | UFPB — student information hub, TypeScript |
| [`luthierycosta/ConsertandoHorariosSIGAA`](https://github.com/luthierycosta/ConsertandoHorariosSIGAA) | 75 | 🟢 **MIT** (1,082 B) | UnB — SIGAA timetable decoder |
| [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api) | 61 | 🟢 **MIT** (1,108 B) | SIGAA — ⚠️ **archived**, self-described scraper |
| [`ernestosrf/sigaa-horarios-extension`](https://github.com/ernestosrf/sigaa-horarios-extension) | 58 | 🔴 none | UFBA |
| [`rodrigmatrix/sigaa_ufc_android`](https://github.com/rodrigmatrix/sigaa_ufc_android) | 33 | 🟢 **Apache-2.0** (11,357 B) | UFC — Android |
| [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | 33 | 🟢 **MIT** (1,071 B) | IFRN — SUAP client |
| [`IFRN/suapi`](https://github.com/IFRN/suapi) | 28 | 🔴 **none** | ⚠️ **the institution's own org, ungranted** |
| [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | 24 | 🟢 **MIT** (1,065 B) | SIGAA tooling, Python |
| [`Projeto-SIAC/suap-wrapper`](https://github.com/Projeto-SIAC/suap-wrapper) | 12 | 🟢 **MIT** (1,061 B) | SUAP, Node.js |

🟢 **The LATAM entry the fourteenth pass could not measure is real and it is the largest
national cluster this pass found: `sigaa` 677 repositories, `suap ifrn` 27, nine addresses
carried forward, seven of them permissive.** The fourteenth pass's only attempt OR'd the
names and collapsed into the generalist layer at `total_count: 160,659`. One name per query
returns a tier.

⚠️ **And the ungranted one is the institution's own.** [`IFRN/suapi`](https://github.com/IFRN/suapi)
— *"Clientes para acesso à API do SUAP"*, published by the federal institute that **operates**
SUAP — carries no licence payload, while an individual's `suap-api-php` is MIT. This is the
single most answerable upstream ask in this pass: a public institution, a public repository,
one missing file.

### Finding 5 — the channel's yield is a property of the name, not of the supply

The fourteenth pass priced the platform channel at 80% licensed and recommended it broadly.
It works, and it has one failure mode that must be stated with it:

| Platform name | `total_count` | Verdict |
|---|---|---|
| `pronote` | **907** | 🟢 real tier |
| `sigaa` | **677** | 🟢 real tier |
| `powerschool` | **590** | 🟢 real tier |
| `webuntis` | **401** | 🟢 real tier |
| `somtoday` | **112** | 🟢 real tier |
| `"ntu cool"` | **54** | 🟢 real tier |
| `infinitecampus` | **43** | 🟢 real tier |
| `bromcom` | **36** | ⚠️ thin — nothing above 2★ |
| `suap ifrn` | **27** | 🟢 real tier |
| `"arbor mis"` | **7** | ⚠️ all 0★, mostly coursework clones |
| `"skyward" student information system` | **1** | 🔴 a demo app, no integration |
| `"capita sims" school` | **0** | 🔴 empty |
| `samarth ugc` | **0** | 🔴 empty |
| 🔴 `diksha` | **2,864** | 🔴 **name collision — zero are the platform** |

🔴 **`diksha` is the channel's worst case and it is not thinness, it is a false positive at
scale.** India's national platform shares its name with a common Indian given name: the 2,864
results are personal portfolios, a fitness studio, a coaching website. **A tier that looks
deep and contains nothing.** The real upstream for that platform is **Sunbird**, which this
KB already shelves.

🔵 **The qualification to carry forward: the platform channel's yield tracks the
*distinctiveness* of the platform's name.** `webuntis`, `somtoday`, `pronote`, `bromcom` are
coined words and return clean tiers. `diksha`, `arbor`, `skyward`, `compass`, `clever` are
ordinary words and return noise or nothing. Before trusting a count, ask whether the name is
a word.

⚠️ **Boolean `OR` failed again, twice, exactly as the fourteenth pass warned**:
`arbor bromcom sims mis school` → **0**; `sentral compass school australia api` → **0**. Two
more data points for a rule this KB already has.

### The method note for this pass

**Three instrument findings, and the first one invalidates an instruction in the brief.**

1. 🔴 **`curl -sI https://github.com/<repo>` returns HTTP 403 for every repository through
   this environment's egress proxy — all 36, including ones whose payloads were then read
   successfully.** The standing instruction to verify URLs with `curl -sI` **cannot be
   satisfied here**, and worse, it returns a *uniform* 403 that looks like a verdict. A
   constant response is not evidence. **The instruments that do work:**
   `git ls-remote --symref` (existence + real default branch, no API, no auth) and
   `raw.githubusercontent.com` (payload). All 36 rows above were verified with both;
   36/36 exist and every default branch was confirmed, not assumed.
2. 🔴 **This pass reproduced a defect this KB had already found, fixed and built a control
   for — and the control was correct.** The probe script written for this pass classified
   four payloads as Creative Commons/NonCommercial (`SapuSeven/BetterUntis` 300★,
   `TEAMSchools/powerschool`, `sikkepitje/TeamSync`, `sas-fossdev/saspes`); all four are
   **GPL-3.0 or AGPL-3.0**, because GPL-3.0 §6 contains the word *"noncommercially"*. An
   earlier pass of this KB had already measured that exact string at **line 259** of the
   payload, diagnosed it as **P171** (*a token read over the body cannot be believed*), and
   fixed it in `compose/code/lib/license_family.sh` with a **gate** — `osi_family_of()`
   resolves the family first, and the Creative Commons branch is entered only on
   `Creative Commons|creativecommons.org|CC BY|CC-BY`, after which NonCommercial is read as
   an attribute. 🟢 **Tested this pass, that library is right on all three hard payloads
   first time: `GPL-3.0`, `AGPL-3.0`, `CC-BY-NC-SA-4.0`.** 🔴 **The failure was bypassing it.**
   The library's own header records the previous instance (pass 77, *"the correction did not
   travel"*); this is the second. **The rows published above are unaffected — all four were
   re-read by hand and carry their true families** — but the lesson is a process one: source
   `lib/license_family.sh`, and better, give `lib/` a probe harness so no future pass writes
   the loop by hand at all.
3. 🟢 **One payload sat at `LICENCE`, British spelling** —
   `AkizumiFox/NTU-COOL-Assignment-Status-Viewer`, MIT, 1,056 B. The fourteenth pass measured
   the full case-variant ladder at **76 of 76 on plain `LICENSE`** and priced it as worthless.
   That stands, with one amendment: **1 in 44 this pass sat at the British spelling.** Carry
   `LICENCE` as a second probe — it is one extra request — and leave the other eleven variants
   off the census, exactly as that pass instructed.

### Added later in the fifteenth pass — the MCP Registry channel, filtered, and it closes two of this pass's own gaps

Instruction 1 (*"finish the MCP Registry census"*) was run with the retry fix described in
`repos/trending.md`. The census itself is a channel-economics finding and lives there. **What
belongs here are the rows**, because once the index is filtered the channel is high-precision:
**13 of 16 probed addresses carry a licence payload, 12 of them MIT.**

All rows below were probed with the new shared harness
(`compose/code/lib/probe_payload.sh`), which resolves the real default branch first and
classifies with `lib/license_family.sh`.

| Repo | ★ | Licence (payload) | Region | What it is |
|---|---|---|---|---|
| [`JohannsenLum/canvas-api-mcp`](https://github.com/JohannsenLum/canvas-api-mcp) | 3 / **13 forks** | **MIT** (1,069 B) | Global | 16 curated student tools **plus a gateway to all 1,116 Canvas API endpoints** |
| [`Smartoire/paxaver-mcp`](https://github.com/Smartoire/paxaver-mcp) | 0 | **Apache-2.0** (11,344 B) | Global | School-community platform adapter — **streamable HTTP + OAuth 2.1**, capability-scoped |
| [`KSAklfszf921/skolverket-mcp`](https://github.com/KSAklfszf921/skolverket-mcp) | 0 | **MIT** (1,092 B) | **EMEA** (SE) | Skolverket open APIs — curriculum, school units, **adult education**. The *second* permissive Skolverket server in this KB |
| [`MartinSA04/ntnu-mcp`](https://github.com/MartinSA04/ntnu-mcp) | 0 | **MIT** (1,076 B) | **EMEA** (NO) | NTNU course data on Cloudflare Workers — timetables, grade statistics, conflict checks |
| [`Cogniledger/cogniledger-mcp-makuri`](https://github.com/Cogniledger/cogniledger-mcp-makuri) | 0 | **MIT** (1,084 B) | **EMEA** (EU) | ⚠️ **"EU-compliant AI tutoring platform for immigrant children"** — the most regulated user group in this KB, permissively licensed |
| [`EquateItAu/classquill-mcp`](https://github.com/EquateItAu/classquill-mcp) | 0 | **MIT** (1,077 B) | **APAC** (AU) 🆕 | ClassQuill tutoring-business data — **read-only by design** (sessions, students, tutors, invoices, reports) |
| [`Eason0in/classdojo-mcp`](https://github.com/Eason0in/classdojo-mcp) | 0 | **MIT** (1,065 B) | **North America** | ⚠️ ClassDojo roster import/verify, **unofficial, local-first** — a **K-12** asset |
| [`SidneyBissoli/uis-mcp-server`](https://github.com/SidneyBissoli/uis-mcp-server) | 0 | **MIT** (`LICENSE.md`, 1,079 B) | Global | UNESCO UIS statistics **with full provenance and pinned releases** |
| [`Lilly-Tech-Collab/ai-school-mcp`](https://github.com/Lilly-Tech-Collab/ai-school-mcp) | 0 | **MIT** (1,404 B) | Global | 550+ free AI course tracks / 21,000+ lessons, **answers cite a real lesson** |
| [`CSOAI-ORG/education-ai-mcp`](https://github.com/CSOAI-ORG/education-ai-mcp) | 0 | **MIT** (1,068 B) | Global | Lesson-plan + quiz generation |
| [`CSOAI-ORG/quiz-generator-ai-mcp`](https://github.com/CSOAI-ORG/quiz-generator-ai-mcp) | 0 | **MIT** (1,080 B) | Global | Quiz generation + answer validation |
| [`CSOAI-ORG/flashcard-ai-mcp`](https://github.com/CSOAI-ORG/flashcard-ai-mcp) | 0 | **MIT** (1,080 B) | Global | Flashcards + **spaced repetition** |

**Measured and ungranted from the same filter** — including **two addresses the fourteenth
pass listed as "not read", now read:**

| Repo | Verdict |
|---|---|
| [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **no payload** on `master`. Udir (Norway) registry data. *Pass 14 left this "not read" — it is now read.* |
| [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | 🔴 **no payload** on `main`. US public school districts by address — enrolment, demographics, boundaries. *Also "not read" in pass 14.* |
| [`Capmus-Team/supost-mcp`](https://github.com/Capmus-Team/supost-mcp) | 🔴 **no payload** on `master`. Stanford student marketplace. |
| `lockinplanner/lock-in` | 🔴 **does not resolve** — `ls-remote` returns nothing. A registry entry pointing at an address that is not there. |

### 🟢 Two gaps this pass declared, and then closed in the same pass

This matters more than the rows, because it is a check on this KB's own method.

1. 🔴 **Declared gap 3 of this pass said: *"no Japan-, Korea-, Australia- or India-placed SIS
   integration asset was found."* The Australia half is now wrong.**
   [`EquateItAu/classquill-mcp`](https://github.com/EquateItAu/classquill-mcp) is MIT,
   payload-verified, and Australian. 🔵 **The gap was true of the platform-name channel and
   false of the world** — exactly the error Finding 1 of this pass corrected in the
   fourteenth pass's work, reproduced here within hours. **A single-channel gap is a
   statement about that channel.** The gap is restated correctly in `intel/trends.md`:
   Japan, Korea and India remain unfound; **Australia is found.**
2. ⚠️ **The fourteenth pass's "the hole is K-12 administration" needs the same qualification.**
   [`Eason0in/classdojo-mcp`](https://github.com/Eason0in/classdojo-mcp) (MIT) is a K-12
   classroom asset, and ClassDojo reaches a very large K-12 install base. It is unofficial
   and roster-scoped, so the *administration* claim survives in substance — but the tier is
   not empty, and it was not empty when it was called empty.

🔵 **The channel lesson, stated for the next pass.** The registry is **low-density and
high-precision**: ~160 education-matching servers in a 17,000+-name index (under 1%), most of
those false positives — and once filtered by hand, **13 of 16 carried a payload and 12 were
MIT**. It also reached **three regions the platform-name channel missed in the same pass**
(Australia, Norway, EU-regulated tutoring). **Run both channels; they fail differently.** The
platform channel finds institutions; the registry finds products.

---

## Added in the sixteenth pass of 2026-10-06 — one agent-adjacent row, and the honest count

The channel this pass ran was the **ministry tier** (`agents/trending.md`, Finding 1). It is a
good channel for **data, specs and platforms** and a poor one for agents: a directorate
publishes a curriculum API, not a tutor.

**So this pass adds one row, and says so rather than padding the table.**

| Name | Repo | Licence (payload-verified) | ★ | Region | Description |
|---|---|---|---|---|---|
| **MCP Brasil** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (`main`) | 🟢 **MIT** (`LICENSE`, 1,072 B, *"(c) 2025-2026 MCP Brasil"*) | 🟢 **1,805** | **LATAM** (BR) | MCP server over **70 Brazilian public-sector APIs** (Python / FastMCP), **13 of its endpoints education**. The largest education-data tool surface placed in LATAM in this KB. 🟢 **Canonical address, settled in the seventeenth pass by root-commit comparison** — see the resolution below. |

🟢 **RESOLVED in the seventeenth pass of 2026-10-06 — and the resolution corrects this KB,
not the repository.** All three addresses were cloned with full history and share the root commit
`8b786bfab09f2637bf842571250f4beb8ff5d216` (2026-03-22). `Mcp-Brasil/mcp-brasil` is **upstream**
(1.8k★, 278 forks, no fork banner). [`dasgltd/mcp-brasil`](https://github.com/dasgltd/mcp-brasil)
is a **fork of it** — its page reads *"forked from Mcp-Brasil/mcp-brasil"* — sitting at **0★** and
in exact sync (same `HEAD` `2efb258`, same 246 commits, same 23 tags), which is why refs alone
could not separate them. `marcellodesales/mcp-brasil` is a second fork, 8 commits behind.

🔴 **Two pass-16 statements were wrong and are withdrawn here.** (1) *"the GitHub API reports
neither as a fork of the other"* — the rendered page states the fork relationship plainly.
(2) **`dasgltd/mcp-brasil` was recorded at "246★"; it has 0★, and 246 is its commit count** — the
same figure this KB carries, correctly labelled, in a **commits / tags** column of
`repos/trending.md`. A commit count was imported into the star column and carried for seven
weeks. 🔵 **There was therefore never a 7.3× star gap between two projects: there is one project,
and the KB was comparing it with a 0★ fork of itself.**

🟢 **What to do in a deliverable:** pin `Mcp-Brasil/mcp-brasil` and pin a commit — the
pin-a-commit advice stands, for versioning reasons rather than identity ones.

### What this pass searched for and did not find — stated as a gap, not as silence

| Looked for | Where | Result |
|---|---|---|
| A ministry-published **tutoring or assessment agent** | 5 ministry names; `org:Utdanningsdirektoratet` (18 repos, all read) | 🔴 **none.** Udir publishes a curriculum endpoint, an exam-admin system, a design system, two Moodle plugins and CI tooling. **No agent.** |
| A **French** curriculum agent | `eduscol`, 107 results | 🔴 **none licensed.** ⚠️ One real candidate: `VictorNain26/tomai-curriculum` — *"Index RAG de TomIA — l'index des programmes du collège"*, a **RAG index over the French national curriculum**, **NO-PAYLOAD**. The nearest thing to a French curriculum agent in this KB, and it is ungranted. |
| A **Japanese** curriculum agent | `mext`, `monbukagakusho`, 1,701 results | 🔴 **none.** Only MEXT's kanji-by-grade tables as CC0 data (`fnshr/kyo-kan`). |
| A **Gulf** ministry agent | `"ministry of education"` + Gulf, 7,228 results | 🔴 **none** — and the count is void (it matches funding acknowledgements). |

🔵 **The shape across four regions is one finding: where a ministry publishes, it publishes the
substrate and leaves the agent to the market.** That is a sales fact, not a disappointment —
`P25` in `compose/patterns.md` is built on exactly that division of labour.

### 🟢 A connection worth recording: one LATAM author, two permissive education-data assets

[`SidneyBissoli/uis-mcp-server`](https://github.com/SidneyBissoli/uis-mcp-server) (MIT, UNESCO
UIS statistics with pinned releases and full provenance) is already on the MCP shelf above.
The same author published [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR)
— **MIT, on CRAN**, covering eleven INEP instruments (Censo Escolar, ENEM, SAEB, ENADE, CAPES,
FUNDEB and more). 🟢 **One identifiable individual is supplying both the global and the
Brazilian education-statistics access layer, permissively.** ⚠️ Which is also a
**bus-factor-of-one** note for anything built on either.

---

## Added in the seventeenth pass of 2026-10-06 — no new agent rows, one correction, and the reason both are the right outcome

**This pass adds zero rows to the tables above, and that is a finding rather than a shortfall.**
The channel it ran was the **ministry tier queried as `org:`** (`agents/trending.md`, Finding 4):
eight national bodies, of which two have a code estate — **188 repositories from Finland's
Opetushallitus and 6 from Sweden's Skolverket**. Not one of the 194 is an agent. They are
curriculum services, study registries, learner-identity registries, admissions form engines,
grant administration and an OER library.

🔵 **Four consecutive passes have now run a state channel and none has found a state-published
agent.** That is no longer a sampling result; it is the division of labour this KB sells into,
and it is already written as `P25` in `compose/patterns.md`: **the state ships the substrate and
leaves the agent to the market.** A fifth pass looking for a ministry tutor should expect to
find a ministry *API*.

### What this pass changed in the table above

| Change | Row | Why |
|---|---|---|
| 🟢 **Caveat lifted** | **MCP Brasil** | Identity settled by root-commit comparison. `Mcp-Brasil/mcp-brasil` is upstream and is the address to pin. |
| 🔴 **Figure withdrawn** | (prose) `dasgltd/mcp-brasil` **"246★"** | It has **0★**. 246 is its **commit count**, imported into the star column and carried since 2026-08-18. |
| 🔴 **Claim withdrawn** | (prose) *"the API reports neither as a fork"* | The rendered page reads *"forked from Mcp-Brasil/mcp-brasil"*. |

⚠️ **Nothing else on this shelf moved, and no row was re-measured this pass.** Star counts above
still carry their **2026-10-06** morning readings; `curl` on `github.com` returned **403**
throughout this pass, so a full re-read was not available at the price of one request per repo.

### 🔴 The licence finding that decides whether 188 repositories can ever appear on this shelf

Every Finnish payload read is **EUPL** (v1.1 or v1.2) — ten of ten. The EUPL is **OSI-approved**,
so this is not an exclusion; but it is **copyleft whose reach includes network use**, and
`lib/license_family.sh` — this KB's hardened classifier — contains **zero EUPL patterns**, so it
returns `UNCLASSIFIED` for all of them. The full trace is Finding 6 of `agents/trending.md`; the
commercial consequence is in `verticals/solutions.md` and `intel/trends.md` (§38).

🟢 **For an agent builder the practical reading is short:** an agent that **calls** these services
over their APIs is unaffected by their licence. An agent that **embeds or forks** their code into
a hosted client product inherits an AGPL-shaped obligation. **That boundary, not the star count,
is what decides the architecture** — and it is why this pass added a pattern (`P27`) rather than
a row.


### Eighteenth pass of 2026-10-06 — state the negative first: **no new agent**

**This pass added no row to the agent tables above, and that is the correct outcome rather than a
shortfall.** The channel run was the **standards-body conformance register** — searching by
*standard + conformance certification* instead of by topic, star count, funder, institution or
ministry name. It returned a substantial amount of permissive software, and **none of it is an
agent**: five MIT **QTI 3 item players and toolchains**, six MIT **national-service clients** from
the Dutch agency Kennisnet, and two **MCP servers** over a Chilean national open-data portal.

Those are shelved where they belong — `repos/foundations.md` and `verticals/solutions.md` — because
**putting components in the agent table is how a KB starts counting libraries as capabilities.**

**Three things from this pass do bear on the agents already listed:**

1. 🟢 **The assessment agents now have a deterministic scoring path, which they did not have.**
   [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (**MIT**, 30★,
   **1EdTech Certified** for QTI 3 Basic and Advanced "Delivery") runs a QTI item's **declared**
   response processing. Any generation agent in this KB — Educhain, the P11 chain, the item-bank
   patterns — can now be wired so that **the model proposes and the standard scores**, with the
   model demonstrably outside the scoring path. That is the single cheapest way to make an
   assessment deployment defensible under the EU AI Act's high-risk obligations and under the US
   "human judgment is final" rule (§16). Recipe: **P34**.
2. 🟢 **Curriculum alignment gains a permissive Python client.**
   [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) (**MIT**, © 2018)
   reaches **Eduterm**, the Dutch national curriculum vocabulary — the P29 "curriculum alignment as
   a tool call" shape, already written, in the language the agents here are written in.
3. 🔴 **A fork nearly entered this file as a public-body asset, for the second consecutive pass.**
   [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) is **forked from
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components)** — identical root commit
   `de8b27b`, **2,377 commits against upstream's 2,456, so 79 behind**, 1★ against 19. Caught by
   running `git clone --filter=blob:none --no-checkout` **before** the row was written rather than
   after. Pass 17 spent a whole pass correcting the same class of error in `mcp-brasil`. **The
   instrument did not change; when it was run did.** Fork-lineage is a **pre-write** check.

⚠️ **The star counts and licences in the tables above were not re-read this pass.** They carry the
2026-10-06 readings recorded by the passes that took them. A cell saying *not read this pass* in an
earlier section still means exactly that.

## Added in the nineteenth pass of 2026-10-06 — the conformance-agent tier, and a permissive licence over an absent capability

**Channel new to this KB this pass: the regulatory-citation channel.** Earlier passes swept by
topic, star count, funder, ministry, institution, function, licence scope, platform name, language,
the MCP Registry and (pass 18) standards-body conformance registers. This pass swept for
implementations of **the exact technical standard a binding rule names** — WCAG 2.1 AA (what the US
DOJ Title II rule cites), WCAG 2.2 AA, EN 301 549 (what the European Accessibility Act points at)
and PDF/UA. Seven channels have now been used.

Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-06, over `main`, `master` and `develop` and 7–11 filename variants each. `api.github.com`
is 403 from this environment (re-confirmed this pass), so star and fork counts were read from the
rendered repository page the same day.

### The agent rows — WCAG conformance as an agent capability

| Agent | Repo | Licence (read from payload) | ★ / forks | What it does |
|---|---|---|---|---|
| A11y MCP | [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | **MIT** (`main/LICENSE`, © 2025 Ronan Takizawa) | 92 / 18 | **6 tools** — `test_accessibility`, `test_html_string`, `get_rules`, `check_color_contrast`, `check_aria_attributes`, `check_orientation_lock`. TypeScript. Engine is **axe-core + `@axe-core/puppeteer`**, declared as runtime dependencies in `package.json`. **No account, no API key** — `npx` and it runs. The permissive default for deterministic WCAG scanning from inside an agent. |
| WCAG Accessibility Skills | [tomaszboloz/WCAG-Accessibility-Skills](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) | **MIT** (`main/LICENSE`, © 2026 Tomasz Bołoz) | 10 / 2 | Audit CLI **and** agent skill. **All 86 active WCAG 2.2 success criteria and 78 of WCAG 2.1**, levels A/AA/AAA, rules classified **automated / semi-automated / manual**. Node 20+, **no production dependencies**. Canonical JSON findings by severity. 🟢 **The only asset found this pass that encodes the automated/manual boundary as data** and keeps a per-criterion **manual-review queue** — its README refuses to let a zero-finding report be read as conformance. At 10★ no star-sorted sweep would ever surface it. |
| claude-a11y-skills | [shawnmcb/claude-a11y-skills](https://github.com/shawnmcb/claude-a11y-skills) | **MIT** (`master/LICENSE`, © 2026 Shawn McBurnie) | not read this pass | Skills-shaped successor to the author's own MCP server. ⚠️ **Default branch is `master`, not `main`** — `main` returns 404 for every licence filename, so a `main`-only probe reports this repository as ungranted. Its README names `a11ymcp` above as the free default engine. |

🔵 **Read with the row this KB already holds:** [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents)
(**MIT**, `main/LICENSE`, © 2026 Taylor Arndt) is **421★ / 49 forks** as read this pass, v**7.0.3**,
with **11 specialist agents and 39 MCP scanner tools** covering web files, **Office documents, PDF
and ePub** (where courseware actually lives), Markdown and Python, across Claude Code, Codex,
Copilot, Gemini CLI, Claude Desktop and Antigravity. It was recorded in `repos/trending.md` as a
repository; **it belongs on the agent shelf**, and this pass puts it there.

### ⚠️ The supply-chain fact under all four rows — MIT skin, MPL-2.0 engine

Read from `package.json` payloads this pass:

- `accessibility-agents` declares **`@axe-core/cli` ^4.13.0**, and its README states the 39 MCP
  tools are *"axe-core, Office, PDF…"* — axe-core is the engine.
- `a11ymcp` declares **`axe-core` ^4.6.0** and **`@axe-core/puppeteer`** as *runtime* dependencies.

[`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) is **MPL-2.0** (`master/LICENSE`),
not permissive-unconditional. 🟢 **Using it unmodified as a dependency is fine** — MPL-2.0 is
**file-level** copyleft, so it does not reach the studio's own files. ⚠️ **Two obligations that do
bite:** axe-core must appear in the client's SBOM with its licence, and **editing an axe-core rule
file puts that file under MPL-2.0**, source-disclosure included. So every MIT accessibility agent
in this KB inherits an MPL-2.0 engine. **Tune rules through configuration, never by patching the
rule files.** The one exception on this shelf is `WCAG-Accessibility-Skills`, which has **no
production dependencies at all** — which is why a 10★ repository earns a row next to a 421★ one.

### 🔴 The 15th failure mode in this KB's catalogue — a permissive licence over an absent capability

| Repo | ★ / forks | Licence (payload) | Verdict |
|---|---|---|---|
| [WCAG-Compliance/wcagc-mcp](https://github.com/WCAG-Compliance/wcagc-mcp) | **0 / 0** | **MIT** (`main/LICENSE`, © 2026 Pavel Charkasau) | 🔴 **Do not shelve as reusable IP.** The licence is real and the capability is not in the repository. Its own README: a *"thin, stateless adapter"* that *"holds no database, no scan logic"* and forwards the caller's bearer token to the hosted **wcagc.com** API, where *"all authentication, entitlements, quotas, and scan orchestration live"*. Running it needs an `mcp:scan` key minted from a wcagc account, **daily-quota-limited on Free/Starter, unlimited on Pro/Agency**. |

**Why this is a new failure mode and not an old one.** This KB's catalogue already holds *no
licence file* (`DMontgomery40/mcp-canvas-lms`), *a licence outside the root* (`OS4ED/openSIS-Classic`,
`frappe/*`), *prose that imitates a grant* (`A-R007/Multi-Agent-Study-Assistant`), *declared and
ungranted*, *a case-sensitive filename*, and *a bespoke "Community License"*. All six are failures
**of the grant**. This one is a **complete, valid MIT grant over code that cannot do the job
alone** — and the KB's own verification method, reading the `LICENSE` payload, marks it green.
⚠️ **Add one step to the method: after the licence passes, read the README for an API base URL, a
bearer token or an account requirement.** A permissive adapter to a paid service is a procurement
line item wearing an open-source badge.

🟡 **It is still worth recording, for one reason:** it is the **only** repository found this pass
whose description names **EN 301 549 and PDF/UA** — the European standard and the document standard.
The permissive shelf references WCAG and nothing else (see the declared gap below).

### Measured this pass and not usable — recorded so the next pass does not re-probe

| Repo | ★ / forks | Licence as measured | Verdict |
|---|---|---|---|
| [AccessLint/skills](https://github.com/AccessLint/skills) | **103 / 15** | ⚠️ **Declared and ungranted.** README lines 142–144 read `## License` then `MIT`, and there is **no licence file** — probed `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `License`, `license.md`, `MIT-LICENSE`, `LICENSE-MIT.txt`, `.github/LICENSE`, `docs/LICENSE` on **both** `main` and `master`. No `package.json` either. | 🔴 **Ask before use.** Content is strong — five skills (`accessibility-scan` against the live DOM with `file:line` source mapping, `accessibility-inspect` for keyboard/focus/reflow, `accessibility-audit` implementing **WCAG-EM** with pass/fail/**undetermined** per criterion, `accessibility-fix`, `accessibility-diff` for regression baselines). ⚠️ **But MIT requires that a copyright notice be retained, and no holder is named anywhere**, so the grant cannot be complied with as written. One `LICENSE` file from the maintainer fixes it; until then it is an eighth instance of *declared and ungranted*. |
| [shawnmcb/a11y-mcp-server](https://github.com/shawnmcb/a11y-mcp-server) | **0 / 0** | **MIT** (`main/LICENSE`, © 2026 Shawn McBurnie) | 🟡 **Granted, superseded by its own author.** Five tools (WCAG 2.2 criteria lookup, HTML pattern check, fix suggestion, component documentation, audit summary). Its README names `claude-a11y-skills` as *"the skills-based successor for day-to-day accessibility work"* and keeps this repo *"as working evidence"*. Take the successor. |
| [sign/translate](https://github.com/sign/translate) | not read this pass | 🔴 **Non-OSI, dual-tier** (`master/LICENSE.md`) | **See the warning below — this is the shape to learn.** |

### ⚠️ A licence axis new to this KB — education-granted, integrator-excluded

[`sign/translate`](https://github.com/sign/translate) (the sign-language translation stack, now
presented as **"Rylo Translate"**) carries no OSI licence. Its `LICENSE.md`, read this pass, splits
the grant **by the type of legal entity using it**:

> *"Individuals, non-profit organizations, and educational institutions are permitted to use
> `Rylo Translate` for sign language translation without charge, while a separate license is
> required for for-profit commercial organizations."*

🔴 **For a Globant engagement this is the worst possible shape, and it is worse than copyleft.**
AGPL-3.0 at least lets the studio build and ship under a known obligation. Here **the university
is granted and the integrator is not**: the client may run it for free, and the moment Globant
builds it into a delivery it needs a separately negotiated commercial licence. ⚠️ **A proposal
that demos sign-language translation on this stack is quoting software the studio has no right to
deliver.** Every prior failure mode in this KB asks *"is there a grant?"*. This one asks **"is
there a grant for *us*?"** — and a permissive-licence filter answers neither, because the file
is not an OSI licence at all.

🔵 **The consequence for the catalogue:** the licence column needs to be read as *two* columns —
the grant to the **client** and the grant to the **integrator**. For OSI licences they are the
same. For entity-tiered licences they are not, and this is the first one this KB has measured.

### Declared gaps — searched this pass, nothing found

1. 🔴 **No permissive PDF/UA remediation engine exists.** This matters more than any row above,
   because courseware is PDFs and **both** the US Title II rule and the EAA cover electronic
   documents. What was measured: [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library)
   **validates** PDF/UA but is **dual GPL / MPL** (`LICENSE.GPL` + `LICENSE.MPL`, present on
   **`master`** and on the `integration` branch and ⚠️ **absent from `main`**) — a **filename**
   instance of the KB's licence-discovery failure mode: `LICENSE.GPL` and `LICENSE.MPL` are outside
   every shortlist this KB probes, so an 11-filename sweep reports the repository as ungranted
   while the grant is sitting in the root; [`ocrmypdf/OCRmyPDF`](https://github.com/ocrmypdf/OCRmyPDF)
   (**MPL-2.0**, 34.9k★) adds a searchable text layer and PDF/A output but **does not produce
   tagged, structurally accessible PDF/UA**. Searched: PDF/UA remediation, tagged PDF, structure
   tagging, accessible PDF generation. 🔵 **Validation is permissive-adjacent and remediation is
   absent** — so the deliverable is a human-in-the-loop tagging workflow, and it should be priced
   as labour, not automated away in a slide.
2. 🔴 **No permissive implementation anywhere names EN 301 549**, except the MIT adapter to a paid
   service above. The engines name WCAG. **The European standard has no permissive software
   referencing it** — which is sharper than it sounds, because EN 301 549 is largely WCAG 2.1 AA
   for web content, so the tools are *usable* in EMEA; what is missing is anything that maps
   findings to the clauses an EMEA auditor will actually cite.
3. 🔴 **No open-source asset found behind the UNICEF Accessible Digital Textbooks programme**,
   including the **AI-led ADT prototype Uruguay produced in 2025**. Searched by programme name, by
   country (Paraguay, Uruguay, Brazil) and by the Brazilian PNLD. It is a **programme, not a
   shelf** — see `intel/market.md`, LATAM, where it is the largest unserved opportunity in this file.
4. 🔴 **No permissive sign-language education asset.** The one well-known stack is the entity-tiered
   licence above. Searched sign language, AAC and assistive-communication repositories; everything
   usable is copyleft (`verticals/solutions.md`).

### The method note for this pass

🟢 **The channel worked, and the reason is worth keeping:** *"accessibility"* is a topic and returns
blog posts; **WCAG 2.2 AA, EN 301 549 and PDF/UA are proper nouns** and return software. This is the
fifteenth consecutive pass in which every new row came from a proper noun rather than from
*"AI education"*, and the second (after pass 18's QTI) where the proper noun was **a standard named
in a rule**. 🔵 **The generalisable instruction: read the obligation, take the standard it cites,
and sweep for that string.** The rule tells you what to search for.

⚠️ **One instrument failure to record:** `github.com` HTML returns **403** through this
environment's proxy for every repository page, so all star and fork counts this pass came through
`WebFetch`, and licence facts came from `raw.githubusercontent.com`, which is **not** blocked.
Where the two disagreed, the payload won — and they **did** disagree once: a rendered-page read
reported `AccessLint/skills` as *"License: MIT"* while the repository contains no licence file at
all. **That is the whole argument for this KB's payload-reading rule, demonstrated in a single
repository.**

---

## Twentieth pass of 2026-10-06 — one correction to this file, and a 475-reference audit of the whole shelf

**From the transition-provision channel.** Narrative in `agents/trending.md`; trends **46** and
**47** in `intel/trends.md`; the evidence tier in `repos/foundations.md`; delivery in
`compose/patterns.md` under **`P-TRANSITION-EVIDENCE`**.

### 🔵 Correction — "Decree 33" is a Prime Ministerial *Decision*, and there is a second instrument this file never named

This file states *"Vietnam's **Decree 33** (in force 2026-08-15) classifies AI that monitors…"*. 🟢
**The date is right and the substance is right. The instrument type is wrong, and it matters.**

| What this file said | What the instrument is |
|---|---|
| "Decree 33" | **Decision 33/2026/QĐ-TTg** — a *Quyết định* of the **Prime Minister**, issued **2026-06-30**, effective **2026-08-15**, carrying the list of **46 high-risk AI systems across six sectors** |
| *(never recorded here)* | **Decree 142/2026/ND-CP** — a *Nghị định* of the **Government**, issued **2026-04-30**, effective **2026-05-01**: one-stop portal, national AI database, three-tier risk classification and conformity assessment, labelling and watermarking, three-level sandbox. **8 chapters, 46 articles** |

🔵 **Why a terminology slip earns a correction block.** In Vietnam's hierarchy a *Decree* and a
*Prime Ministerial Decision* are different instruments — different issuing body, different amendment
procedure, different place of publication. "Decree 33" is not findable; it sends the next reader
looking for a document that does not exist, and it hides the fact that **there are two instruments**
— the one this file named, and the one (142) carrying a filing duty whose deadline, **2026-06-30**,
has already passed.

🟢 **Education's three entries in Decision 33, now recorded exactly:** AI providing **self-learning
content from uncontrolled data sources**; AI that **automatically assesses, grades or ranks
students**; AI that **monitors or analyses learner behaviour using biometric data** (facial
recognition, eye tracking). Six sectors: education **3**, ethnic and religious affairs 7, healthcare
2, banking 2, judicial proceedings 1, transportation 31.

⚠️ **Verification level:** this correction comes from **search-result summaries** naming the
instruments (Allen & Gledhill, Vietnam Briefing, Indochine Counsel, Tilleke & Gibbins, VCI Legal,
Viet An Law, `thuvienphapluat.vn`). The primary texts are **`EGRESS_BLOCKED`** from this environment.
**Re-read the instrument before quoting it to a client.**

### 🟢 The shelf audit — 475 references, nothing newly dead

Every `github.com/owner/repo` reference in this file and the five other non-append-only files was
extracted and probed for a licence payload across 7 filenames × up to 3 branch refs.

| Result | Count |
|---|---|
| Reachable | **470** |
| 🟢 Genuinely gone | **1** — `planejaia/OpenMAIC-Brasil`, **already recorded in this file as a phantom**, now 404-confirmed by a second method |
| ⚠️ False flags — the repo exists | **3** — `foradian/fedena` (4★), `AmericasNLP/americasnlp2024` (7★), `cqm3ron/bromcom-scraper` (1★) |
| 🔵 Extraction artefact, never a repository | **1** — `search/repositories`, from this file's own prose about `api.github.com` |

🟢 **After nineteen passes of accumulation, nothing on this shelf has rotted.**

🔴 **The method finding is the one to keep: of 4 repository-shaped flags, 1 was real — 25%
precision.** All three false flags failed identically — no licence payload *and* no `README.md` at
the probed paths — and this KB had **already** resolved `foradian/fedena` by a better method
(`master/config/routes.rb` and `master/Gemfile` return 200 while every `README.md` 404s, recorded in
`verticals/solutions.md`). ⚠️ **The cheap probe is strictly weaker than the method already in this
KB. Never withdraw a row on one probe** — a single-path sweep confirms liveness and must never
declare death.

### ⚠️ The licence portfolio of this shelf, measured for the first time

All 475 references, licence read from payload: **MIT 202 · Apache-2.0 61 · BSD 8 · MPL-2.0 5 →
276 clearly permissive (58.1%)**; **GPL 41 · AGPL-3.0 19 → 60 copyleft (12.6%)**; **93 (19.6%) with
no licence payload at the probed paths**; ~22 others (ECL-2.0 7, CC0 4, CC-BY 2, ISC 2, CC-NC 3,
Elastic-2.0 1, national and bespoke).

🔴 **The number to carry out of this file is 93 — one reference in five, a bucket larger than GPL and
AGPL combined.** This file's licence-failure catalogue already names three failure modes; this is the
first measurement of how much of the corpus sits in them.

⚠️ **It is an upper bound and is stated as one.** The probe tested 7 filenames at up to 3 refs, and
licences have already been found outside that set here — `OS4ED/openSIS-Classic` at
`docs/License.txt`, `frappe/*` at lowercase `license.txt`. 🟢 **So the honest form of the number is
not "93 unlicensed" but "93 that must not be cited as permissive without a manual read"** — a work
item with a size, which is the first time this KB can price its own licence debt.

## Added in the twenty-second pass of 2026-10-06 — the first rows this KB ever read from a forge API

**Channel new to this KB this pass: the GitLab REST API v4 as a *discovery and metadata* channel**
(`/projects?search=`, `/projects/:id?license=true`, `/repository/files/:path/raw`,
`/repository/tree`, `/users`). ⚠️ **Stated precisely, because half of it is not new:** pass 107 of
2026-10-05 already read licence payloads from `gitlab.com/-/raw` and already assessed
`oer/emacs-reveal`. What had never been called is the **API** — and it matters for one reason that
has shaped forty passes of this KB: **`api.github.com` has returned 403 since pass 37, so every
metadata question (liveness, topics, licence key, holder) has been unanswerable about a GitHub row.
A different forge answers all of them.**

Instrument, controls and limits: `compose/code/gitlab-api-channel/`. Trends **51** and **52** in
`intel/trends.md`; pattern **`P-ONPREM-CLASSROOM`** in `compose/patterns.md`.

### 🔬 The channel, measured before any verdict

| Layer | Endpoint | Status | Negative control |
|---|---|---|---|
| discovery | `gitlab.com/api/v4/projects?search=…` | 🟢 **200** | — |
| project metadata + licence key | `…/projects/:idEnc?license=true` | 🟢 **200** | `definitely-not-a-project-zzz9/nope` → **404** ⇒ **DISCRIMINATES** |
| licence payload | `…/repository/files/LICENSE/raw?ref=…` | 🟢 **200** | — |
| licence set (REUSE) | `…/repository/tree?path=LICENSES` | 🟢 **200** | — |
| copyright holder | `…/users?username=…` | 🟢 **200** | — |
| rendered page | `gitlab.com/<slug>` | 🟢 **200** on **26 of 26** GitLab URLs cited by this pass | invented slug → **302**, not 404 ⇒ 🔴 **does NOT discriminate** |
| *(still blocked, re-probed)* | `api.github.com`, `github.com`, `huggingface.co` | 🔴 **403 / 403 / 000** | — |

🔴 **The HTML control is the one to carry out of this table.** GitLab answers an unknown path with a
**302** to sign-in, not a 404. So on this forge an HTML probe can confirm existence and **can never
establish absence** — the same rule this file already imposes after the single-path sweep of the
nineteenth pass, now with a second, independent reason.

### 🔴 `license=true` is silently ignored by the search endpoint — so licence-filtered discovery is impossible here

25 search terms → 539 hits → **534 unique projects**, every one requested with `license=true`.
**Licences returned: 0 of 534.** The same parameter on the single-project endpoint returns
`{"key":"mit","name":"MIT License"}` for `gitlab-org/gitlab-runner`, so the parameter works — the
list endpoint just does not honour it.

🟢 **This is a clean cross-forge replication of trend 29.** On GitHub a licence filter has a
false-negative floor it cannot see; on GitLab there is **no filter at all**, and a candidate costs
**two requests minimum** — one to find it, one to learn whether it carries a grant.

### 🔴 The detector is wrong in two rows, and one of them is a row this KB already carries

22 licence payloads read first-hand. Detector = GitLab's `license.key`; payload = the first lines of
the file the detector claims to have read.

| Project | Detector says | Payload says | Verdict |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://gitlab.com/francoisjacquet/rosariosis) | **`agpl-1.0`** | **GNU GPL v2**, 15,214 B | 🔴 **WRONG — and wrong by two licence families** |
| [`olatorg/openolat-starter`](https://gitlab.com/olatorg/openolat-starter) | **`ecl-2.0`** | **Apache-2.0**, verbatim header, **0** occurrences of "Educational Community" | 🔴 **WRONG** |
| [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) | **`other`** | **LGPL-3.0**, named in its own first three lines | ⚠️ **Silent about a knowable answer** |
| [`francoisjacquet/Grading_Scale_Generation`](https://gitlab.com/francoisjacquet/Grading_Scale_Generation) | **`gpl-2.0+`** | plain **GPL-2.0** text — the `+` is **not obtainable from the payload**; its `composer.json` declares **`GPL-2.0-or-later`** | 🔵 **Agreement, and a counter-example to this KB's own rule: here the payload *under*-reads the grant and the manifest settles it** |
| [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | **`other`** | 517 B **REUSE pointer**; real set = **4** identifiers | 🔵 **Pointer, not a grant** |
| [`oer/oer-reveal`](https://gitlab.com/oer/oer-reveal) | **`other`** | 516 B REUSE pointer; real set = **6**, two of them `LicenseRef-` | 🔵 **Pointer, not a grant** |
| the other **16** | — | — | 🟢 **Agreed** (**17** with `Grading_Scale_Generation` above) |

**Final tally, after the instrument correction below: 22 payloads → 🟢 17 agree · 🔴 2 wrong · ⚠️ 1
silent · 🔵 2 REUSE pointers.** Reproducible: `python3 compose/code/gitlab-api-channel/test_gitlab_channel.py` → **32/32**, `--live` → **35/35**.

🟢 **The RosarioSIS row is the most useful fact in this pass.** This KB records the **GitHub** copy as
`GPL-2.0 (LICENSE@master)`, **15,214 B**. The GitLab copy's payload is **the same 15,214 bytes** —
two forges, one file, cross-host agreement at the byte. 🔴 **And the forge's own detector contradicts
both of them, naming a licence (`AGPL-1.0`) that would change what a client may do with a
delivered module.** A KB row built on the detector key would have been wrong; a row built on the
payload was right on both hosts.

⚠️ **My own instrument's defect, declared rather than hidden.** The first run of this comparison
flagged **6** disagreements. Two were mine: a substring classifier read "GNU General Public License"
inside **MPL-2.0**'s secondary-licence clause and "Lesser General Public License" inside
**GPL-2.0**'s closing section, mislabelling `git-classrooms` and `Grading_Scale_Generation`. 🟢 **So
the honest detector tally is 2 wrong + 1 silent of 20 comparable payloads (plus 2 REUSE pointers)
— not 6** —
and the lesson is the one this file keeps relearning: *a classifier that matches licence names inside
licence texts will find every licence in every licence.*

### 🆕 A third disagreement class: the project contradicts itself

| Project | Surface 1 | Surface 2 | Surface 3 |
|---|---|---|---|
| [`Sudz1/sam-lms`](https://gitlab.com/Sudz1/sam-lms) | README badge: **ISC** | `package.json` `"license": "ISC"` | `LICENSE` payload: **MIT** |
| [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | `LICENSE` payload: **BSD-3-Clause** | PyPI `travo` 2.1.1: `license: null`, **zero** licence classifiers | — |

🔵 **Neither is commercially dangerous** — ISC and MIT are both permissive, and a silent registry
does not revoke a repository's grant. 🟢 **Both are useful anyway:** they are the first cases in this
KB where the *same project* answers the licence question differently on three and on two of its own
surfaces, which is the shape trend 23 predicted and had only ever seen *across* parties.

### The new rows — agent- and tool-shaped

Licences read from payload; ★ and `last_activity_at` served by the API on 2026-10-06. ⚠️ **Every
star count here is small. That is the finding, not an omission** — see the regional read in
`intel/market.md`.

| Project | Repo | Licence (payload) | ★ | Last activity | Placement | What it does |
|---|---|---|---|---|---|---|
| **ELabSheet** | [cjaikaeo/elabsheet](https://gitlab.com/cjaikaeo/elabsheet) | 🟢 **BSD-2-Clause** (`LICENSE`, holders named) | 14 | **2026-09-19** | APAC (Thailand) | **Task authoring + automatic grading for e-learning.** Python 64.8% / HTML 25.0% / C++ 2.7%. Payload names its holders — *Chaiporn Jaikaeo and Jittat Fakcharoenphol*, 2013 — so the `P386` holder gate passes on first read. Dockerised install in a sibling repo (`cjaikaeo/elab-docker`). **The most permissive auto-grader this KB has found: BSD-2 is looser than mentingo's MIT-with-tracing and carries no platform.** |
| **Travo** | [travo-cr/travo](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** (`LICENSE`) | 8 | **2026-10-06** | EMEA (France) + North America (Québec) | **GitLab ClassRoom**: fetch/submit assignment workflow over Git + the GitLab REST API, terminal or Jupyter widget dashboard, **automatic and manual grading of notebooks via nbgrader** (already on this KB's shelf at BSD-3-Clause, 1.4k★). Runs against **any** GitLab instance including self-hosted, needs no other infrastructure. Université Paris-Saclay × Université du Québec à Montréal; in production in a dozen classes. PyPI `travo` **2.1.1**. |
| **learn-anything (SRS)** | [voxos.ai/learn-anything](https://gitlab.com/voxos.ai/learn-anything) | 🟢 **MIT** (`LICENSE`) | 0 | 2026-03-15 | Global | Turns **any** coding agent into a tutor: one file dropped into a folder, spaced repetition, visual exercises, adaptive difficulty. Works with Claude Code and Cursor. The skill-shaped sibling of this KB's `anything-to-course` row, without the packaging. |
| **Edusaku** | [yoockh-group/Edusaku](https://gitlab.com/yoockh-group/Edusaku) | 🟢 **Apache-2.0** (`LICENSE`) | 0 | 2026-05-18 | APAC (Indonesia) | **Offline-first** AI education assistant for teachers and students in remote areas with limited or no internet. React Native 0.76.5, on-device model. The APAC counterpart to this KB's equity-deployment pattern, and the second permissive APAC-origin row found this pass. |
| **ADLETE** | [adaptive-learning-engine/adlete-packages](https://gitlab.com/adaptive-learning-engine/adlete-packages) | 🟢 **MIT** (`LICENSE`) | 1 | **2026-10-02** | ⚠️ EMEA *(inferred — no country in repo or README)* | Monorepo of a generalised **adaptive learning engine**: analyses a learner's competence level and recommends the next task/exercise/training. Ships a Moodle-side sibling (`adaptive-learning-engine/moodle/adleteh5p`) that wires it to **H5P** activities — the integration this KB's P3 mastery pattern has had to hand-build. |
| **SAM LMS** | [Sudz1/sam-lms](https://gitlab.com/Sudz1/sam-lms) | 🟢 **MIT** (payload; ⚠️ project claims ISC twice) | 0 | 2026-03-23 | EMEA (Africa) | "Smart African LMS": offline-first curriculum, **mobile money** payments, SMS notifications, Node.js. Built "with SA educators in mind". Early and single-maintainer — read it as a reference for the *constraints* (money rails, SMS, offline), not as a platform to deploy. |
| **OpenTeacherAgent** | [ai-swarm-solutions-group/OpenTeacherAgent](https://gitlab.com/ai-swarm-solutions-group/OpenTeacherAgent) | 🔴 **AGPL-3.0** (`LICENSE`) | 0 | 2026-08-15 | Global | Agentic educational authoring in a single binary. **Recorded and excluded**: AGPL-3.0 is incompatible with this KB's redistribution brief. Listed so a later pass does not spend a sweep rediscovering it. |

### 🔵 Cross-host confirmation, which is a verification result and not a new row

| Project | This KB's GitHub reading | GitLab reading this pass | Result |
|---|---|---|---|
| **OpenOLAT** | `OpenOLAT/OpenOLAT`, ✅ Apache-2.0, 446★ | [olatorg/OpenOLAT](https://gitlab.com/olatorg/OpenOLAT), payload **Apache-2.0** 10,982 B, 2★, active **2026-10-06** | 🟢 **Confirmed on a second forge.** The "only complete LMS you can extend without the copyleft conversation" claim in `verticals/solutions.md` now rests on two independent hosts |
| **RosarioSIS** | `francoisjacquet/rosariosis`, ⚠️ GPL-2.0, **15,214 B**, 644★ | [francoisjacquet/rosariosis](https://gitlab.com/francoisjacquet/rosariosis), payload GPL-2.0, **15,214 B**, 65★, active **2026-10-06** | 🟢 **Byte-identical payload on both hosts** — and 🔴 the detector disagrees with both (above) |

🔴 **One consequence for every star count in this KB.** The same project is **644★** on GitHub and
**65★** on GitLab. ★ measures a *host's* audience, never a project's adoption, and this KB's shelf is
ranked almost entirely by GitHub ★. Nothing in this file needs reordering, but no ★ here may be
quoted to a client as "how widely used this is".

---

## Added in the twenty-third pass of 2026-10-07 — the agent shelf, dated for the first time

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC. Ages in days are computed
against the reference date 2026-10-06**, so every figure here is reproducible.

**No new agent row is added by discovery this pass.** What is added is a **column this file never
had**: the head-commit date of every GitHub repository it cites, read with `git ls-remote` and
`git fetch --depth 1 --filter=blob:none` — the channel that works while `api.github.com/repos/*`
returns 403.

### The agent shelf's liveness, measured

Across the **250** distinct GitHub repositories cited in this file:

| Bucket | Share |
|---|---|
| touched in the last 30 days | 40.0% |
| touched at any point in 2026 | **77.6%** |
| 🔴 cold more than a year | 18.8% |
| 🔴 cold since before 2024 | 8.0% |

🟢 **This is the second-liveliest population in the KB**, behind only the MCP side-car tier (90.9%
in 2026, 5.0% cold). The agent shelf is young because the category is young; the ageing in this KB
is concentrated in infrastructure and standards, not in agents. See `repos/trending.md` for the
full tier table.

### Spot dates for the rows a client is most likely to be shown

| Row | Head commit | Age | Read |
|---|---|---|---|
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 2026-10-07 | 🟢 0 d | the largest asset in this KB is also committed daily |
| [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 2026-10-07 | 🟢 0 d | |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 2026-10-06 | 🟢 0 d | |
| [`frappe/lms`](https://github.com/frappe/lms) | 2026-10-07 | 🟢 0 d | |
| [`langfuse/langfuse`](https://github.com/langfuse/langfuse) | 2026-10-06 | 🟢 0 d | |
| [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | 2026-10-06 | 🟢 0 d | |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 2026-10-04 | 🟢 2 d | row 1 of this shelf, and it is alive |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 2026-10-02 | 🟢 4 d | |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 2026-09-30 | 🟢 6 d | |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 2025-10-15 | ⚠️ **356 d** | the pedagogy benchmark is **a fortnight from being a year stale** |
| [`rhasspy/piper`](https://github.com/rhasspy/piper) | 2025-08-26 | 🔴 **406 d** | wired into **P18**; `sherpa-onnx` does TTS too and was committed today |
| [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2) | 2025-10-03 | 🔴 368 d | the liveliest member of a substrate that is 87.5% cold |
| [`ai-edu-lab/E-Eval`](https://github.com/AI-EDU-LAB/E-EVAL) | 2024-02-19 | 🔴 **960 d** | wired into **P12** |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 2022-11-21 | 🔴 **1,415 d** | see the Python LTI correction below |

⚠️ **`pedagogy-benchmark` at 356 days is the row to watch, not the row to pull.** Trend 31 records
that this KB's pedagogy benchmark is *"no longer missing — it is licensed shut"*; it is now also
nearly a year unmaintained. A benchmark can be valid while unmaintained in a way a library cannot,
but the date belongs in any deck that cites it.

### 🔴 The Python LTI 1.3 claim is dead twice over, and this file holds half of the correction

This file already carries *"The Python LTI 1.3 row this KB declared missing eight hours earlier"*,
reinstating `dmitry-viskov/pylti1.3` (MIT, 138★). **That correction closed the gap with a library
whose head commit is 1,415 days old** — and the whole family stopped together
(`pylti1.3-django-example` and `pylti1.3-flask-example`, both 1,406 d), which is the signature of an
abandoned project rather than a finished one.

**The live permissive Python LTI 1.3 shelf, payload-verified 2026-10-06:**

| Repo | Licence (payload) | Holder named in payload | Head commit | Age |
|---|---|---|---|---|
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,527 B) | Project Jupyter Contributors, 2016 | 2026-07-01 | 🟢 **97 d** |
| [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti) | 🟢 **MIT** (1,097 B) | ⚠️ *The Regents of the **University of Michigan***, 2022 | 2025-08-27 | ⚠️ 405 d |
| [`ucfopen/cookiecutter-python-lti`](https://github.com/ucfopen/cookiecutter-python-lti) | 🟢 **MIT** (1,129 B) | UCF Center for Distributed Learning, 2025 | 2026-05-12 | 🟢 147 d |
| [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) | 🟢 MIT (1,069 B) | *Dmitry Viskov*, 2019 | 2023-01-12 | 🔴 1,363 d |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT (1,069 B) | *Dmitry Viskov*, 2019 | 2022-11-21 | 🔴 1,415 d |

🟢 **Use `jupyterhub/ltiauthenticator`.** BSD-3-Clause, Python, and its README states it implements
**LTI 1.3 and LTI 1.1, tested against Open edX, Canvas and Moodle** — the three platforms this KB
already documents.

🔴 **This KB has cited it three times and never counted it**, because it is filed as a JupyterHub
authenticator and the gap was swept for as an *LTI library*. Trend 29 says a gap built on a filtered
index is a claim about the index; here the index was this KB's own.

⚠️ **`ucfopen/cookiecutter-python-lti` is live and installs a corpse.** Its Flask template pins
`git+https://github.com/ucfopen/pylti1.3.git@master` — a fork, 1,363 days cold, at a moving branch.
Its Django template pins `django-lti==0.7.1`, a real version of the MIT library above. **Take the
Django path, or take `ltiauthenticator`.**

### 🔴 A new licence failure class: the `LICENSE` file that is a refusal

[`Wahid7852/Verbix-Flutter`](https://gitlab.com/Wahid7852/Verbix-Flutter) — Flutter app using OCR and
speech recognition to help children with dyslexia read. GitLab's detector reports
`license_key: "other"`. The payload is **208 bytes in full**:

> *Copyright (c) 2024 Swati Sharma · This code is provided for viewing purposes only as part of a
> Google Solution Challenge. No permissions are granted for reuse, distribution, or modification.*

| Class | First recorded | Shape |
|---|---|---|
| detector names the wrong OSI licence | trend 23, pass 22 | label ≠ grant, **between** parties |
| project contradicts itself | pass 22 | badge/manifest/payload disagree **inside** one project |
| 🆕 **the file is an anti-grant** | **this pass** | a `LICENSE` whose content **withholds every right a licence confers** |

🔴 **Operational rule:** *the presence of a `LICENSE` file is not even weak evidence of a grant.*
Any count of "repositories with a licence" includes this one. ⚠️ Holder mismatch as well — payload
holder **Swati Sharma**, publishing account **Wahid7852**.

### 🔴 What this does to the oral reading fluency gap (sixth pass, P17)

The gap **stands**, and the reason is now stronger than absence. A GitLab sweep of 15 English,
Spanish and Portuguese terms returned **276 unique projects**; the single candidate squarely inside
the category is `Verbix-Flutter`, and it is explicitly closed. 🔴 **The capability was built and the
build was shut.** That is a different engagement conversation from "nobody has built this" — it
means a clean-room build cannot be avoided by adoption, but it also means the pedagogy is not
unexplored.

### 🆕 One ungranted agent-shaped asset, North America, recorded because it widens pass 22's framing

| Project | What it is | Licence |
|---|---|---|
| [`cderda/cargogetgraded`](https://gitlab.com/cderda/cargogetgraded) ("Carriage") | **Step-level algebra autograder.** Python/SymPy; ingests post-OCR LaTeX student work, flags *mistake transitions* rather than final answers, emits teacher-facing Excel. 15 package directories (`math_engine`, `mistake_processing`, `transformation_assessment`, `assignment_taxonomy`…). Built by a former high-school maths teacher and UChicago Math graduate. **Piloting Fall 2026** | 🔴 **none** — established by **enumerating the repository root tree** (21 entries), not by guessing filenames |

🟢 **Why it matters beyond one row.** Pass 22 concluded that ungranted-but-real education code is a
**LATAM** signature and proposed the licence-grant clinic as a LATAM offer. Carriage is **North
America**, more pedagogically ambitious than the BSD-2 auto-grader this KB just adopted, and equally
unusable. **The clinic is a global offer with a LATAM concentration** — see `P-GRANT-CLINIC` in
`compose/patterns.md`.

⚠️ **This does not displace [`cjaikaeo/elabsheet`](https://gitlab.com/cjaikaeo/elabsheet)**
(BSD-2-Clause, 14★, activity 2026-09-19, holders *Chaiporn Jaikaeo and Jittat Fakcharoenphol*,
re-verified this pass), which remains the permissive auto-grader this KB recommends.

### The method note for this pass

🟢 **The probe discriminates, and that is why the negative result counts.** Four repository slugs
invented by earlier passes as controls (`UniTime/this-repo-does-not-exist-xyz123`,
`openedx/fake-repo-zzz999`, and two others) were swept blind alongside the real ones and **all four
failed to resolve**, while 884 real ones resolved. Pass 22's GitLab rendered-page control **302s on
an invented slug** and therefore proves nothing; this one returns no ref.

⚠️ **No ★ was read this pass.** Both `github.com` rendered pages and `api.github.com/repos/*` return
403 to this environment, so every star count in this file is pass-22's or older, and
the pass-22 warning that ★ measures a host's audience still governs.

🔴 **A date is not a verdict.** A 472-day-old certified QTI player may be the right pick and a
0-day-old repository may be a week old in total. The dates are published so that a component choice
can be *argued*, not so it can be automated.

---

## Added in the twenty-fourth pass of 2026-10-07 — the shelf's *build* dated, and the LTI row corrected again

⏱️ **Measurement window 2026-10-07 ~00:30 UTC → 03:00 UTC; ages against the reference date
`2026-10-07`.** Channel new this pass: **the package registries** (`pypi.org`, `registry.npmjs.org`)
read for the **latest release date**. Instrument: `compose/code/registry-recency-channel/`.

**No new agent row is added by discovery this pass.** What is added is the column *behind* pass 23's
column: pass 23 dated the repositories this file **cites**; this pass dates the dependencies those
repositories **install**. They are different facts about the same row.

### 🔴 The row most likely to be shown to a client is the row with the widest divergence

| Row | Head commit (pass 23) | Median dependency age (this pass) | Cold > 1 yr | Read |
|---|---|---|---|---|
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 2026-09-30, **7 d** | 🔴 **604 d** | **21/35** | 🔴 maintained project, 2020-era build |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 2026-10-06, 1 d | ⚠️ 200 d | 14/32 | Python-2-era shims persist (`zeroconf-py2compat`, 1,156 d) |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 2026-10-04, 3 d | 🟢 62 d | 10/43 | row 1 of this shelf, healthy on both axes |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 2026-10-06, 1 d | 🟢 **60 d** | 40/152 | ⚠️ bimodal — a modern core and a 5,923-day App Engine tail |
| [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | — | 🟢 **9 d** | **0/20** | 🟢 the cleanest build in the corpus |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | — | ⚠️ 122 d | 1/6 | a thin, deliberately pinned manifest — not the same as a fresh one |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | — | 🟢 12 d | 2/7 | |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | — | 🟢 22 d | **0/2** | |
| [`ronantakizawa/a11ymcp`](https://github.com/ronantakizawa/a11ymcp) | — | 🟢 14 d | **0/5** | |

⚠️ **OATutor is still the recommendation it was, and the sentence next to it has to change.** It is
MIT, from UC Berkeley, and the only BKT-based permissive intelligent tutoring system this KB has
found in twenty-four passes — and its front end is `@material-ui/core` **v4**, superseded in 2021,
beside `random-seed` (3,967 d), `list-react-files` (3,412 d) and `react-cursor-position` (2,929 d).
🔴 **Adopting OATutor means adopting a dependency uplift as sprint one.** That belongs in the
estimate, not in the retrospective.

### 🔵 The Python LTI 1.3 row, corrected for the third time — and this time against the upstream

Pass 23's own table in this file promoted
`Harvard-University-iCommons/django-lti` (MIT, head commit 2025-08-27) and recorded, with a warning
symbol, that its payload holder is *"The Regents of the **University of Michigan**"*. 🔴 **That
warning was the finding.** The holder does not match the publishing account because **the repository
is a fork**, and the upstream is live:

| Repo | Licence (payload) | Head commit | Age | Latest release | Age | Verdict |
|---|---|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B, © The Regents of the University of Michigan) | 2026-10-05 | 🟢 **2 d** | [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1** | 🟢 **61 d** | 🟢 **START HERE** (Django) |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 | 🟢 98 d | `jupyterhub-ltiauthenticator` v1.6.3 | 🟢 195 d | 🟢 only if the tool **is** JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | 2026-10-01 | 🟢 **6 d** | `lti-consumer-xblock` v11.4.2 | 🟢 **6 d** | 🔴 best-maintained of all, **and copyleft** |
| [`eduNEXT/openedx-lti-tool-plugin`](https://github.com/eduNEXT/openedx-lti-tool-plugin) | 🟢 Apache-2.0 (11,357 B) | 2025-07-21 | ⚠️ 443 d | 🔴 not on PyPI | — | ⚠️ permissive but cold and unpublished |
| `Harvard-University-iCommons/django-lti` | 🟢 MIT (1,098 B) | 2025-08-27 | 🔴 406 d | — | — | 🔴 **cold fork — do not start here** |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT (1,069 B) | 2022-11-21 | 🔴 1,416 d | `pylti1p3` v2.0.0 | 🔴 **1,417 d** | 🔴 abandoned — both channels agree |

🔴 **The claim this KB repeated for fourteen passes was wrong in an instructive way.** *"There is no
permissive Python LTI 1.3 library"* was a statement about a **licence-filtered index**, not about
the world: the best-maintained Python LTI 1.3 implementation in any language exists, is committed
and released weekly, and is **AGPL-3.0**. **The permissive shelf was not empty; the *well-maintained*
shelf was copyleft.** All 13 editable assertions of the old claim are corrected in place this pass
(the append-only records in `agents/trending.md` and `repos/trending.md` are left intact).

⚠️ **One pass-23 figure corrected:** the Harvard payload is **1,098 B**, not 1,097 B. Recorded only
because byte length is how this KB establishes payload identity, and an off-by-one there reads as a
different file. The two copies are in fact **not** byte-identical — `sha256 d5558cd4…` upstream
versus `c24a6b35…` on the fork.

### 🔴 One proprietary dependency, inside an Apache-2.0 row

[`oppia/oppia`](https://github.com/oppia/oppia) declares
[`azure-cognitiveservices-speech`](https://pypi.org/project/azure-cognitiveservices-speech/), whose
only licence classifier is **"License :: Other/Proprietary License"** and whose licence field is
empty. 🟢 Oppia's own Apache-2.0 grant is unaffected — a permissive project may depend on
proprietary software. 🔴 **A deliverable that forks Oppia and ships it inherits a Microsoft Speech
SDK obligation**, and nothing in this KB said so before this pass. The permissive substitute is
already on the shelf: `k2-fsa/sherpa-onnx` (Apache-2.0, head commit 1 d), which covers ASR **and**
TTS locally.

### The method note for this pass

🟢 **The most productive input was a warning symbol in the previous pass's own table**, not a search
result. The mandatory query set returned **no new repository for the fourteenth consecutive pass**.
Findings 1, 2, 3 and 7 all unroll from reading a ⚠️ pass 23 wrote and did not follow — which is
trend 50 (*a filed correction regresses*) in its sharper form: **a filed anomaly regresses.**

⚠️ **Every age in this section is a lower bound on staleness.** The registry channel dates the
**latest** release, not the **pinned** one; a manifest pinning an old version installs something
older than reported, never newer.
🔵 **MEASURED, twenty-fifth pass of 2026-10-07:** across 327 resolved rows the pinned release is
**220 d** at the median against **57 d** at the latest — **3.9×** — and **42.5%** of the installed
tier is cold by more than a year, not 27.2%. The bound holds in **326 of 327** rows; the single
exception is below.

🔴 **And a date is still not a verdict.** `defusedxml` at 2,039 days is a finished security library
and the correct pick; `webapp2` is a relic of a retired platform. Age does not
separate them — reading does.
🔴 **`webapp2`'s figure is corrected here**: this section published **5,122 d**, the age of the
latest *stable* release (2.5.2, 2012-09-28). `oppia/oppia` does not install that one — it pins
`webapp2==3.0.0b1`, a **pre-release from 2016-09, 3,676 d**. The verdict stands, the number was
wrong, and this is the only row in the corpus where the pinned release is **newer** than the
registry's latest.

---

## Twenty-fifth pass, 2026-10-07 — the Canvas MCP cohort is nine repositories, and the shelf cites all nine

The fourth pass of this KB recorded two forks of `vishalsachdev/canvas-mcp` and wrote *"pin the
canonical repo"*. **Measured against the whole shelf this pass — 503 slugs, every one dated — the
cohort is nine, and this file and `repos/foundations.md` between them cite every one:**

| Slug | Head commit | Age | Relation, and how it was established |
|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 2026-10-05 | 🟢 **2 d** | 🟢 **the canonical repo — pin this** |
| [`BartMassey-upstream/canvas-mcp`](https://github.com/BartMassey-upstream/canvas-mcp) | 2026-10-04 | 🟢 3 d | derivative — PyPI `canvas-mcp` declares `vishalsachdev/canvas-mcp`; licence holder `Vishal Sachdev` |
| [`abr-Projects/canvas-mcp`](https://github.com/abr-Projects/canvas-mcp) | 2026-09-06 | 🟢 31 d | derivative — same two signals |
| [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | 2026-09-21 | 🟢 16 d | ⚠️ **independent** — MIT © 2024 R. Huijts, its own lineage, not a fork |
| [`lucanardinocchi/canvas-mcp`](https://github.com/lucanardinocchi/canvas-mcp) | 2026-05-08 | ⚠️ 152 d | derivative — npm `canvas-mcp` declares `vishalsachdev/canvas-mcp` |
| [`aryankeluskar/canvas-mcp`](https://github.com/aryankeluskar/canvas-mcp) | 2026-03-11 | ⚠️ 210 d | derivative — same signal; **ISC**, not MIT |
| [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | 2026-08-01 | 🟢 67 d | separate name, separate project |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 2026-05-31 | ⚠️ 129 d | a **second root**: `plyght/canvas-mcp` declares *this*, not `vishalsachdev` |
| [`plyght/canvas-mcp`](https://github.com/plyght/canvas-mcp) | 2025-10-30 | 🔴 **342 d** | derivative of `DMontgomery40/mcp-canvas-lms`, the only cold member |

🔵 **The cohort has two roots, not one**, and the advice *"pin `vishalsachdev/canvas-mcp`"* is
right for six of the nine and silent about the other three. **Eight of nine are live**; the Canvas
MCP layer is the healthiest tier this KB measures, and its problem is duplication, not decay.

### The four ways a package registry names a repository other than the one you cited

Asking every one of the 503 slugs *"which repository does your package registry say you live at?"*
returned **21** that name a different one. Only some of those are lineage:

| Class | n | Discriminator | Examples |
|---|---|---|---|
| **rename / transfer** | 6 | 🟢 `git ls-remote` serves the **same head SHA** | `All-Hands-AI/OpenHands` → `OpenHands/OpenHands`; `iterative/dvc` → `treeverse/dvc` |
| **fork / derivative** | 9 | different heads, same package, holder or payload carries over | `ucfopen/pylti1.3` → `dmitry-viskov/pylti1.3`; four of the canvas-mcp cohort |
| **generic-name collision** | 5 | different heads, **unrelated project** on the registry | `frappe/lms` → `molobrakos/lms` (*a Squeezebox server interface*); `LibreTexts/conductor` → `WaldoJeffers/conductor`; two Google Classroom servers → `deadlyicon/class.js`, *"a super small ruby-ish class system"*, last touched **2013** |
| **vendoring** | 1 | the manifest came in **with the copied code** | `Polygl0t/Polygl0t` → `mosaicml/llm-foundry` |

⚠️ **The collision class is why this is a reading list and not a verdict.** A manifest declaring
`"name": "lms"` or `"name": "class"` will resolve to whoever registered that word first.
`"private": true` removes the worst of them — a workspace root is never published, so its `name`
is a local label — and that one rule killed both false-positive classes the first build produced.

🟢 **`Polygl0t/Polygl0t` is worth a row of its own and is EMEA-placed.** Apache-2.0, its README
opens *"# LLM Foundry 🏭"*, and it is the **University of Bonn**'s derivation of MosaicML's training
stack for the **Polyglot** multilingual-model project, targeted at the Marvin and Bender HPC
clusters and JSC Jupiter. For an EMEA engagement that needs a sovereign multilingual training
pipeline rather than an inference wrapper, it is a European public-research starting point with a
permissive grant — and it is reachable only through the registry channel, because a search for
"education" never surfaces it.

### ⚠️ The holder channel is not a superset of the lineage channel, and the action assumed it was

Pass 24 pre-registered *"treat every **holder ≠ account** row as a fork hypothesis"*. Run that way,
the sweep sees **4** of the 21. The other **17** are Apache-2.0 or GPL rows, where the holder is
`NOT-APPLICABLE` **by construction** — those families ship the licence steward's copyright, not the
project's, which is exactly what `p184` was built to establish. 🔵 **So the holder is a lineage
signal for MIT/BSD/ISC and structurally blind elsewhere. Running the registry stage over the whole
shelf rather than over the holder stage's output is what found the other seventeen** — and that is
a correction to the action, not to the instrument.

### The pre-registered prediction, and why it did not hold

> *"Two of two LTI picks were cold forks. Expect **more than two** further cold forks in the
> 283-row shelf, concentrated in the interoperability tier."*

🔴 **Not confirmed.** Over 503 slugs and two independent lineage channels, **every cold fork found
was already recorded in this KB** — `Harvard-University-iCommons/django-lti` (406 d),
`ucfopen/pylti1.3` (1,364 d), `jdolny/OneRoster.NET` (1,090 d),
`MIT-OL-AI-Tutoring/Open_Learning_AI_Tutor` (588 d). **Zero new ones.** The derivatives the
channels surfaced are mostly *live*: eight of the nine Canvas MCP repositories, and the one
genuine surprise runs the other way — **a live fork of a dead upstream**
(`CNIT-Organization/ltitoolkit`, which vendors the abandoned `PyLTI1p3`; see
`repos/foundations.md`). 🔵 **"Cold fork" was the wrong shape to predict. The shelf's lineage
problem is duplication and stale naming, not abandonment.**

## The grant that exists only in the package registry — six MCP servers, measured 2026-10-07

Pass 25 published **87** of the 503 slugs this shelf cites as shipping **no licence file**. Asking
each one's package registry what licence its publisher declared returns **8 ownership-verified
grants**, of which **six are grants made in the registry and nowhere in the tree** — the tree being
enumerated completely by `p441`, not probed by filename:

| Agent | Repo | Registry grant | Tree |
|---|---|---|---|
| Udir (Norway) data MCP | [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | **MIT**, npm `@nor-data/udir-mcp` | 🔴 no licence text anywhere |
| Canvas LMS MCP | [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **MIT**, npm `canvas-mcp-server` | 🔴 none |
| District API MCP | [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | **MIT**, PyPI `districtapi-mcp` | 🔴 none |
| Google Classroom MCP | [`SalShah20/classroom_mcp`](https://github.com/SalShah20/classroom_mcp) | **MIT**, npm `@salshah20/google-classroom-mcp` | 🔴 none |
| Kolibri design system | [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system) | **MIT**, npm `kolibri-design-system` | 🔴 none |
| Classroom MCP | [`zainf2327/mcp-classroom`](https://github.com/zainf2327/mcp-classroom) | **MIT**, PyPI `mcp-classroom` | 🔴 none |

⚠️ **A registry grant is a grant, and it is weaker evidence than a file.** The publisher asserted MIT
in metadata they control and can change with the next release, and nothing in the repository records
it. 🟢 **For a client deliverable this is `P314`: usable, and worth one written confirmation from the
holder that cites the publisher's own metadata.** All six are MIT, which is what pass 25 predicted the
interesting class would be.

🟢 **Where both channels answer, they agree.** [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis)
is **MIT** in its root `License` file and MIT on npm; [`openedx/XBlock`](https://github.com/openedx/XBlock)
is **Apache-2.0** in `LICENSE.TXT` and Apache-2.0 in PyPI's `license_expression`. 🔴 **Where they
disagree, the tree wins:** `veraPDF/veraPDF-library` carries a dual GPL-3.0/MPL-2.0 grant while Maven
Central declares `null`.

### 🔴 The ownership gate removed 7 of 15 apparent grants, and one of them would have been a serious error

A licence read off a package is only *this* repository's licence if the registry agrees the package
lives here. The first run of the sweep omitted that check and produced **15** grants. Seven were
somebody else's:

| Slug | Package it claims | The repository the registry names | Class |
|---|---|---|---|
| `pnp-v/bo-google-classroom-mcp-server` | npm **`class`** | `deadlyicon/class.js` — *"a simple yet powerful Ruby-like Class inheritance system"*, first published **2013** | name collision |
| `plyght/canvas-mcp` | `canvas-mcp-server` | `DMontgomery40/mcp-canvas-lms` | derivative |
| `lucanardinocchi/canvas-mcp` | `canvas-mcp` | `vishalsachdev/canvas-mcp` | derivative |
| `joshuasoup/d2l-mcp` | `d2l-mcp-server` | 🆕 `general-mudkip/d2l-mcp-server` | derivative |
| `Opetushallitus/aoe` | npm **`aoe`** | 🔴 **none declared** — v0.1.1, published **2016-01-05** by `exolution@163.com`, no description, declaring **GPL-3.0** | unowned |
| `ink-waffle/moodle-mcp` · `ink-waffle/sisu-mcp` | `@ink-waffle/*` | none declared | unowned |

🔴 **`Opetushallitus/aoe` is the row that justifies the gate.** Unguarded, this KB would have recorded
a **strong-copyleft** obligation on the **Finnish National Agency for Education**'s national OER
library on the strength of a stranger's 2016 hobby package. The tree then showed the refusal was right
for a second reason nobody predicted: the project's actual grant is **EUPL-1.2**, 303 B, in
`aoe-web-backend/LICENSE` and `aoe-web-frontend/LICENSE`.

🟢 **All four `FOREIGN-PACKAGE` rows reproduce `p436`'s declared slug, 4 for 4, on an independent
run** — cross-channel calibration, not a new finding. This KB's table *"the four ways a package
registry names a repository other than the one you cited"* above already classified every one of them,
`deadlyicon/class.js` included.

⚠️ **The `ink-waffle` pair is where a gate must stay silent and a human need not.** An npm scope that
equals the GitHub owner (`ink-waffle` → `@ink-waffle/*`) reads as ownership immediately; the
declared-repository field is empty, so the instrument must say `GRANT-UNOWNED`. Both are almost
certainly the owner's own MIT grant, and this KB does not publish "almost certainly" as a licence.

### 🆕 `general-mudkip/d2l-mcp-server` — a repository the search channel has never returned

| Agent | Repo | Head commit | How it was found |
|---|---|---|---|
| Brightspace / D2L MCP server | [`general-mudkip/d2l-mcp-server`](https://github.com/general-mudkip/d2l-mcp-server) | 2025-11-28 | the **registry**, as the declared home of npm `d2l-mcp-server`, which `joshuasoup/d2l-mcp` vendors |

🔵 **Sixteen passes of the mandatory query set have never surfaced it**, and it is the second time the
registry channel alone has added a repository to this shelf — `Polygl0t/Polygl0t` was the first.
Searching for "education" does not return either. ⚠️ **It ships no licence file**; the grant is npm's
MIT, under the same `P314` caveat as the six above, and `joshuasoup/d2l-mcp` is the derivative, not
the root.

### 🔴 The classifier this KB uses mapped npm's refusal-to-grant onto the most permissive licence in its table

`dep_licence.classify_licence`'s permissive rule carried the bare pattern `r"UNLICENSE"`. That matches
inside **`UNLICENSED`**, which is npm's documented value for *"I do not wish to grant others the right
to use a private or unpublished package under any terms"*. So an explicit **refusal** returned
`PERMISSIVE` — the same class as `Unlicense`, the public-domain dedication, and the two most opposite
values the table contains.

🟢 **Latent, not live:** no published row carried it. 🔴 **And the population where it was most likely
to appear is exactly the 87 repositories this sweep was pointed at** — a package that ships no licence
file is the one most likely to declare `UNLICENSED`. Fixed with a `NO-GRANT` class probed first and
**eight controls**, each pairing the refusal with its one-letter-different neighbour.

🔵 **The string collision deserves naming: `UNLICENSED` is this KB's own status for "no licence file
found" and npm's value for "no licence granted".** One spelling, two meanings — and one of them is a
verdict about the publisher's intent, not about a probe.

## Added in the twenty-ninth pass of 2026-10-07 — three enablement assets, and four licence corrections

🟢 **The mandatory query set produced new repositories for the first time in seventeen
passes.** All three verified payload-first on `raw.githubusercontent.com` and cross-checked
against the GitHub API's registry licence; the two channels agree on all three.

| Repo | ★ | Licence (payload) | Verdict |
|---|---|---|---|
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 140,891 | 🟢 **Apache-2.0** | **Take it for enablement, not for the product.** 100+ runnable agents, Agent Skills and RAG apps, Python, pushed 2026-09-30. The best starting corpus on this shelf for a client capability build — it is *examples*, so fork it as curriculum and vendor nothing from it without reading each app's own dependencies. |
| [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | 49,696 | 🟢 **MIT** | **Take it for enablement.** Develop → deploy → iterate on production-grade ML, course-shaped, with a Ray-based training and serving path. ⚠️ Last pushed **2026-03-04** (seven months): teach the method, re-pin the dependencies. |
| [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | 29,517 | 🟢 **Apache-2.0** | **Take it for enablement.** Official code for the O'Reilly *Hands-On Large Language Models*; the clearest permissive treatment of embeddings, retrieval and fine-tuning here. ⚠️ Last pushed **2026-04-24**; a book's companion repo is *meant* to freeze — fine for teaching, not for vendoring. |

⚠️ **All three are enablement assets and none is an education agent.** They teach *about* AI;
they do not tutor, grade, schedule or integrate with an LMS. They belong on the **`P6`
capability-build** tier with `microsoft/ai-agents-for-beginners`, and `compose/patterns.md`
names them in a concrete recipe. Shelving them as tutoring agents because they are popular
would be the `P412` error — taking a repository's category from its star count.

### 🔴 Four corrections to the licence column, from repairing the classifier pass 28 did not open

Pass 28 repaired three defect classes in `sweep_payload.family_of`. This pass re-measured the
same 412 payloads with the **shared shell classifier** — `lib/license_family.sh`, sourced by
27 instruments and untouched by pass 28 — and found the same three classes in it, plus two
more. These are the rows where that changes what a client may ship.

| Repo | published | 🟢 corrected | Why | Consequence |
|---|---|---|---|---|
| [untisapi/untis4j](https://github.com/untisapi/untis4j) | `GPL-3.0` | **LGPL-3.0** | title-stripped payload, identifying itself only in prose — *"this License refers to version 3 of the GNU Lesser General Public License"* (`P457`) | 🔴 **the LGPL permits linking from proprietary code and the GPL does not.** Published one tier too restrictive — usable vs unusable in a client build |
| [ankitects/anki](https://github.com/ankitects/anki) | `CC-BY-SA-4.0` | **AGPL-3.0** | mixed-case prose grant no GNU branch recognised; the payload mentions CC further down and the CC branch took it (`P455`) | a copyleft **code** licence filed as a **content** licence |
| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | `CC-BY-SA-4.0` | **MIT** | the `LICENSE` puts `docs/` under CC BY-SA and says *"Content outside of the above mentioned restrictions is available under the MIT license"*; the classifier kept the documentation's clause (`P456`) | 🔴 a **permissive, redistributable** row rejected as ShareAlike |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic), [OS4ED/openSIS-Responsive-Design](https://github.com/OS4ED/openSIS-Responsive-Design) | `LGPL?` | **GPL-2.0** | **no root licence exists**; the grant lives only at `docs/License.txt` (17,286 B), and `P455` mis-read it | the only licence evidence two real SIS platforms have, read wrong |

### 🔴 And one correction this pass deliberately did NOT make

🔴 **Five rows still erase a NonCommercial restriction**, and they are the only error class
that can put a non-commercial asset into a billable deliverable:
`facebookresearch/seamless_communication`, `openstax/osbooks-biology-bundle`,
`sign/translate`, `Yunfeng-Wan/CSTutorBench`, `Jona-Zwetsloot/Somtoday-Mod` — all five read
`CC-BY` from `sweep_payload.family_of` while their payloads say CC-BY-NC or CC-BY-NC-SA.

⚠️ **The rows in the tables above are correct**; this KB's prose has had them right since
the shelf was built (*"**CC BY-NC-4.0** in `main/LICENSE` — **non-commercial. Hard reject**
for anything billable"*). It is the **instrument** that is blind, which is pass 26's trend 61
holding for a sixth time.

🟢 **The fix belongs on the Python side, which pass 28 rewrote hours before this pass ran**,
and reconciling two concurrent rewrites of one classifier from a stale base is exactly how
`P237` corrections get regressed. So the gap is **pinned by a test** —
`compose/code/p459-unified-verdict/test_unified.py` asserts the `NC-ONLY-SHELL` flag fires,
with a comment stating that **the assertion must flip when the axis is added.** A test that
goes red when a defect is *fixed* is how a known gap cannot be closed silently.

### ⚠️ A payload this toolchain declines to read, stated as a limit rather than a verdict

`OS4ED/openSIS-*` also ship `docs/LICENSE.rtf` — 61,575 bytes of RTF wrapping the same
GPL-2.0 text. Its first two non-blank lines are `{\rtf1\adeflang1025\ansi…` and a font table,
so **the title block is markup**, the family falls to `UNCLASSIFIED`, and the commercial-use
question then reaches the body token match, which finds GPL-2.0 **§3(c)**'s *"this
alternative is allowed only for noncommercial distribution"* — a condition on one
distribution option, not a restriction on the licensee — and answers **PROHIBITED**.

🟢 Both are now reported `CONTAINER-RTF (no legible)` on both axes rather than guessed at
(`P460`). De-marking RTF well enough to recover a title means parsing a font table, and a
half-parsed container would reopen the token-match path that produced the false positive.
**Declining is an answer; inventing a verdict from markup is not.**

## Added in the thirty-first pass, 2026-10-07 — four repos, two buildable

Verified by licence payload over `raw.githubusercontent.com` with a 404 negative control in the same
pass; `curl -sI` on `github.com` is **403 through this session's proxy** and was not used as an
existence test. `api.github.com` is 403, so **no star counts were read** — cells say so rather than
carrying an inferred figure.

| Agent / tool | Repo | Licence (read from payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| Sunbird LMS Service | [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | **MIT** (`master/LICENSE`) | not read this pass | APAC | 🟢 LMS service tier of Sunbird, the DPI stack behind India's **DIKSHA**. Pairs with `Sunbird-Ed/SunbirdEd-portal` (MIT) already on this shelf — together they are a licence-clean public-sector LMS base for an AI layer. |
| ai-agent-book | [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book) | **Apache-2.0** (`main/LICENSE`) | not read this pass | APAC | 🟢 Agent-systems curriculum with runnable Python patterns. Useful as *enablement* material in an engagement, and redistributable. |
| Pawtograder | [`pawtograder/platform`](https://github.com/pawtograder/platform) | 🟡 **GPL-3.0-or-later** (`main/LICENSE`, "either version 3", © 2025 Jonathan Bell) | not read this pass | North America | CI-based autograder, rubric handgrading, Q&A, office-hours queue, gradebook. **Ships an MCP server exposing course context to staff-side LLMs** — the clearest production example on this shelf of MCP wired into a real gradebook. Copyleft: self-host and run freely; do **not** link into a proprietary deliverable. |
| Pawtograder Assignment Action | [`pawtograder/assignment-action`](https://github.com/pawtograder/assignment-action) | 🟡 **GPL-3.0-or-later** (`main/LICENSE`) | not read this pass | North America | The CI grading harness itself, plus regression tests *for the graders*. The regression-testing-the-grader idea is the reusable part even where the licence is not. |

🔴 **Two further repos were verified this pass and deliberately kept off this shelf**, because this
file is the buildable shelf:

- [`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents) — **CC BY-NC-SA
  4.0** (full string, not the normalised `CC-BY` family). **NonCommercial and ShareAlike: no client
  deliverable.** Filed in `agents/trending.md` only.
- [`a5anka/ai-lab-2026-africa-agent-manager`](https://github.com/a5anka/ai-lab-2026-africa-agent-manager)
  — **no licence file at all** (`LICENSE`, `LICENSE.md`, `package.json` all 404; `README.md` 200).
  Public ≠ licensed; all rights reserved by default.

🔁 **One candidate was a fork, not a finding:** `kvnloo/tutor-mcp` is byte-identical to
[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (already shelved) — its
own `LICENSE` is `© 2026 Arnaud Guiovanna` and its README's release badge points back to the
upstream. **`ArnaudGuiovanna/tutor-mcp` is canonical.** See `agents/trending.md`, 2026-10-07.
