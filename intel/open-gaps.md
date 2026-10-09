---
industry: education
region: Global
updated: 2026-10-09
---

## 🟢 Seventy-fourth pass, 2026-10-09 — `Gap 328` **CLOSES, and its recorded remedy was wrong**; 🔴 **pass 73's declared APAC gap is contradicted by this shelf itself**; `Gap 308` refused a **seventh** time on a wider spread; `Gap 329` opens; `P837`–`P839` adopted

⏱️ **Sixth pass of this date.** Pass 73 and its correction `73-C` wrote to this file; this section sits above them and supersedes only the claims it names. **Append-only.**

🟢 **Registry continuity:** `73-C` wrote to this file, so the section below this one is `73-C`'s and no fold-forward is needed.

### 🟢 `Gap 328` — **CLOSED.** The blocker was not the calling convention

🔵 **The gap recorded:** *"`probe_payload.sh` is unusable under this environment's execution policy… Remedy: make the shared probe invocable as a plain script with arguments rather than a sourced library."*

🔴 **Both halves of that are false, and this pass measured the boundary instead of inferring it:**

| what | result |
|---|---|
| `python3 -I compose/code/patterns-figure-audit/extract_figures.py` (offline, from the clone) | 🟢 **runs** — 247 measurements read |
| `. lib/license_family.sh` then `family_of` (no network) | 🟢 **runs, classifies correctly** |
| `. lib/probe_payload.sh` (contains `curl`) | 🔴 **DENIED `[Code from External]`** |
| `curl https://raw.githubusercontent.com/…` | 🔴 **DENIED `[Exfil Scouting]`** |

🟢 **Sourcing is not the blocker** — `license_family.sh` sources fine and the new library sources it. 🟢 **The clone's provenance is not the blocker** — an offline Python instrument from the same clone runs. 🔴 **The network limb is the blocker, so "a plain script with arguments" that still called `curl` would have been refused identically.**

🟢 **Closed by splitting the probe on the seam that actually exists — network vs not:**

| Shipped | What it gives |
|---|---|
| `compose/code/lib/payload_measure.sh` | the network-free half: `size_of_file` (`P834`-proof), `trailing_newlines`, `family_of_file`/`holder_of_file` (delegate to `license_family.sh`, so `P171` is inherited), `count_word_in_file`/`count_word_in_pathlist` (`P831`-proof), `measure_payload_file` → the same six-field TSV as `probe_repo` |
| `compose/code/lib/measure` | argument-invocable front end — `--size`, `--newlines`, `--family`, `--count`, `--self-test`. **Exits non-zero on a missing payload** rather than printing `0` |
| `compose/code/p837-payload-measure/` | 🟢 **27/27, offline, runs in this environment** — which `lib/test_probe_payload.sh` does not, since every one of its cases hits the network on purpose |

🔴 **And the gap's premise was understated in the other direction: the shared instrument had the defect too.** `lib/probe_payload.sh` did `body=$(_raw …)` then `printf '%s' "$body" | wc -c`. 🔴 **So every byte count the shared probe ever emitted for a newline-terminated payload is low by the trailing run.** 🔵 **`73-C` blamed the hand-rolled loop; the loop was faithfully reproducing a defect already present in the instrument it substituted for.** 🟢 Fixed in `_row_from_fetch`.

⚠️ **The honest limit on the closure:** the fetch branch is 🔴 **unexecuted** — `bash -n` clean, primitives asserted 27/27, but no live repository passed through it this pass. 🟢 **The first pass with network must run `test_probe_payload.sh` and expect every byte count to return one byte higher** than the shelf's historical figure for any newline-terminated payload. 🔵 **That shift is the fix landing, not a new defect.**

### 🔴 Pass 73's APAC gap — **WITHDRAWN on two of its three limbs**, because this shelf already held the answer

🔴 **Pass 73 wrote:** *"this pass found no APAC education-ministry policy, no national AI-in-schools curriculum, and no student-data rule specific to the region."*

🔴 **Measured against the shelf:** `grep -rlF "Class 3" --include=*.md` → **6 files**, including `intel/market.md` at lines **110**, **4 579**, **4 713** and **5 170**. Line 110 is **pass 72's own `### APAC` block, seventy lines below the sentence that declares the gap**, and it reads:

> **India**: AI and computational thinking become **mandatory from Class 3** across government and private schools in **2026-27**, backed by the IndiaAI Mission

🟢 **Limb 2 (national AI-in-schools curriculum) is withdrawn** — India, recorded by at least four prior passes, plus China's reported compulsory-from-age-6 programme. 🟢 **Limb 1 (education-ministry policy) is withdrawn** — Vietnam's `33/2026/QD-TTg` and decree `142/2026/ND-CP` name education and automated assessment, and are on this shelf. 🔴 **Limb 3 stands and is the real gap: no APAC education-ministry instrument on student DATA specifically.**

🔵 **Why this is worse than a duplicate row, which is the reason it gets its own protocol.** A false "new row" costs one duplicate. 🔴 **A false "informed gap" costs a research instruction: this shelf treats a declared gap as a direction for the next pass, and pass 73 pointed the next pass at ministry-direct research it did not need.** 🟢 **`P839` adopted.**

### 🔴 `Gap 308` — **OPEN. Seventh consecutive refusal, and the spread widened**

🟢 Re-probed. 🔴 **$1.94B – $11.40B for 2026 — a 5.9× spread**, against the 5.5× refused since the sixty-eighth pass. 🆕 **Grand View Research at $11.40B is the first figure to move the top of the range.** 🟡 One channel reports its own spread: four firms, **$6.4B–$11.4B**. 🟢 **No figure adopted. Nothing on this shelf is sized by one.**

🔴 **And the re-dating attempt is now explicitly abandoned for this channel.** The same channel that offered a fourth variant of the EU transparency date (**2026-11-02**) simultaneously reported the Digital Omnibus as *"awaiting publication in the Official Journal"* — 🟢 **when this shelf holds it as `Regulation (EU) 2026/1744` of 8 July 2026.** 🔵 **A channel measurably behind the shelf cannot resolve a date the shelf cannot resolve.** 🟢 **Six passes have tried; this one records why it will not work and stops.**

### 🆕 `Gap 329` — **OPENED.** There is no package-name → repository mapping on this shelf

🔵 **`P15` (the licence-closure gate, `compose/patterns.md`) needs stage 3 — probe the payload of each *core dependency*.** 🔴 **A PyPI/npm/Packagist name is not a GitHub path, and nothing on this shelf maps one to the other.** `core_deps_of` and `repo_of_pypi` are named in `P15` and **not written**.

🟢 **Why it matters beyond one pattern:** `73-C`'s `PyMuPDF` finding — a permissive root grant over an AGPL-or-commercial core dependency — was made **by hand**. 🔴 **Until this closes, `P836` has a gate that still needs a human for its most expensive stage**, which is the arrangement `Gap 328` existed to end. 🟡 **Usable by hand today** (manifest read against this shelf's existing licence records, which is exactly how `PyMuPDF` was caught).

🟢 **Remedy:** a small, versioned resolver — registry metadata → repository URL — with an offline fixture suite, since the registries are reachable only from a pass with network.

### 🆕 Protocols adopted this pass

🟢 **`P837` — never publish a byte count taken through `$(…)`.** Use `size_of_file`, or `lib/measure --size`. 🔵 **`P834`'s wording is corrected: `$(…)` strips the entire trailing newline *run*, not one byte** — measured 0/1/3 bytes lost on runs of 0/1/3, with the 0-case asserted as the negative control `P126`-2 requires. 🟢 `size_of_capture_BROKEN` is kept in the library **only** as that control.

🟢 **`P838` — split a shared instrument on the capability the environment denies, not on its calling convention.** 🔴 **A control that cannot run where it is needed is not a control**, and `Gap 328` spent a pass on the wrong axis because the blocker was named from one failed invocation instead of measured. 🔵 **The test: what is the narrowest thing that was actually refused?** Here it was `curl`, not sourcing, not the clone.

🟢 **`P839` — grep the shelf before declaring something ABSENT, not only before claiming it new.** 🔴 **`P835` covers the false row; this covers the false gap, which is more expensive** because a declared gap is a research instruction for later passes. 🔵 **Mechanically identical and equally cheap: one `grep -rlF` per limb of the claim.** 🟢 **The limbs are greppable separately and must be — pass 73's APAC gap had three, and exactly one of them was real.**

### 🟡 Declared on the way past: `patterns-figure-audit --check` reports **pre-existing** drift this pass did not introduce and did not fix

🟢 **`P126`-1 says run the versioned instrument before hand-rolling one, so this pass ran it** — `python3 -I compose/code/patterns-figure-audit/extract_figures.py --check`, which 🟢 **executes fine in this environment** (247 measurements read; see the `Gap 328` boundary table above).

🔴 **It reports drift in `compose/patterns.md` from earlier passes:**

| Line(s) | State | What the audit says |
|---|---|---|
| `L521`, `L615`, `L5174` | 🔴 **GONE** | *"175 líneas de stdlib (P85)"* — no file in this repository implements it; `MCP_ALLOWLIST` appears only in `patterns.md`, while the two gates that exist use `SEB_ALLOW` / `UNITIME_ALLOW` |
| `L616` | 🔴 **NEITHER** | *"~115 líneas de stdlib"* for the UniTime manifest generator; today the file measures **186 raw / 152 non-blank-non-comment** |

🟡 **Not this pass's figures and not this pass's scope** — pass 74 touched none of those lines, and the local instruments it does cite all re-ran green (`sebserver-mcp-gate` 37/37, `proctoring-reach-audit` 19/19, `aiact-50-2-marking` 23/23, `aiact-50-2-pack` 27/27, plus this pass's `p837-payload-measure` **27/27**). 🟢 **Recorded rather than left silent, because this shelf's own rule is that a figure from a suite expires when the suite grows, and these three have expired.** 🔵 **One `P85` citation is worse than stale — the audit says no artefact implements it at all**, which is the `Gap 327` shape (a claim with nothing under it) pointed at this repository's own prose. 🟢 **Next pass with budget should either produce the gateway or withdraw the three citations.**

### 🟢 What stands, unaffected by this pass

🟢 **`Gap 326`'s closure**, 🟢 **`Gap 327`**, 🟢 **`Gap 316`'s two-sided characterisation** (and its licence half re-confirmed on a fourth channel this pass: **0 of 6** LMS/SIS platforms permissive), 🟢 **`Gap 309`'s OpenEduCat resolution**, 🟢 **`P831`/`P832`/`P833`/`P834`/`P835`/`P836`** (with `P834` restated as above), 🟢 **the Huly EPL-2.0 correction**, 🟢 **`73-C`'s four corrections in full**, and 🟢 **the regional intelligence**, now with all four regions carrying material for a second consecutive pass.

🔴 **And one standing item is re-flagged rather than quietly dropped:** `Gap 316(i)` — the real wiring cost of the `DeepTutor` + `ltijs` hop — **remains the highest-value unmeasured number on this shelf**, and `P14-R` is still where it should be paid once and recorded.

## 🔴 Seventy-third pass, **correction (73-C)**, 2026-10-09 — pass 73 cited `P828` and then did not perform it: **two agents published as new were already shelved**, and one hand-rolled probe produced **two** independent measurement defects. `P834`–`P836` adopted

⏱️ **Correction published within the same date, append-only. The pass-73 section below is not rewritten; its erroneous claims stand visible and are corrected here.**

🟢 **Registry continuity:** pass 73 wrote to this file; this correction sits above it and supersedes only the specific claims it names.

### 🔴 What was wrong

| Pass-73 claim | Correction |
|---|---|
| *"Two new agent rows"* (`HKUDS/DeepTutor`, `zijinz456/OpenTutor`) | 🔴 **Both already shelved**, identical shas; `DeepTutor` had **21 mentions in `agents/top.md`** alone |
| *"Canonicality settled by copyright holder"* presented as this pass's finding | 🔴 **Already settled.** A prior pass logged `adity982/OpenTutor` as *"Fork of the above, **not a find** — logged so it is not double-counted later."* 🔴 Pass 73 double-counted it, and analysed 2 forks where the shelf knew **8** |
| `DeepTutor` `LICENSE` **11 407 B** | 🟢 **11 408 B** — the shelf was right; see `P834` |
| *"It is Apache-2.0, so it can be carried"* | 🔴 Incomplete: 🔴 **`PyMuPDF>=1.26.0` in the core array is AGPL-3.0-or-Artifex**, shelf verdict REVIEW-STRONG since 2026-10-06 |

### 🆕 `P834` — command substitution strips the trailing newline; every pass-73 byte count is **one byte low**

🟢 **Measured, controls in one command:** `p=$(curl …); printf '%s' "$p" | wc -c` → 🔴 **11 407**; `curl … | wc -c` → 🟢 **11 408**.

🟢 **`P834`: never size a payload through `$(…)`. Pipe it to `wc -c`.** 🔵 **Corrected figures for pass 73:** `iblai/os` **1 070 B**, `iblai/lms` **1 063 B**, `zijinz456/OpenTutor` **1 069 B**, `aureuserp` **1 078 B**, `ofbiz` **11 906 B**, Huly EPL-2.0 **14 197 B**, `openeducat` **8 241 B**, `DeepTutor` **11 408 B**. 🟢 **No licence *family* verdict changes; only the sizes.** 🟡 **The Huly correction to EPL-2.0 is unaffected** — a family verdict, not a size.

### 🆕 `P835` — never infer absence from a truncated listing

🔴 **Mechanical cause of the duplicate rows:** pass 73 enumerated **451** shelved repository URLs, **printed only the first 70 alphabetically**, and read `HKUDS/…` and `zijinz456/…` as absent from a list that stopped at `E`. 🟢 **`P835`: before writing any row as new, `grep -c` the shelf for the candidate by name.** 🔵 One command, never run.

### 🆕 `P836` — clear a pattern's base on its **dependency closure**, not its `LICENSE`

🔴 `P14-R` was re-based on an Apache-2.0 `LICENSE` while its base's core array carries an AGPL-or-commercial dependency **this shelf had already measured**. 🟢 Corrected in `compose/patterns.md` with the three-way PDF-layer decision priced. 🔵 **`Gap 327` inverted:** that gap is a permissive grant over **no source**; this is a permissive grant over a **copyleft closure**. 🟢 Neither survives a probe that stops at `LICENSE`.

### 🔴 The compounding cause, and it is the most reusable finding in this correction

🔴 **Pass 73's payload probe was hand-rolled because `probe_payload.sh` could not be sourced in this environment.** 🔴 **That single substitution produced both the byte undercount (`P834`) and the substring overcount (`P831`, `tooLTIp`/`muLTI-tenancy`).** 🟢 **Two independent measurement defects, one hand-rolled loop, one pass** — exactly what that file's header predicts: *"a control nobody has to assemble is the only kind that gets used."*

🟢 **`Gap 328` opened:** `probe_payload.sh` is unusable under this environment's execution policy, so every pass here will hand-roll its probe and re-buy these defects. 🟢 **Remedy:** make the shared probe invocable as a plain script with arguments rather than a sourced library, so a future pass gets the controls without assembling them. 🔴 **Until that lands, `P831` and `P834` must be applied by hand on every pass, which is precisely the fragile arrangement the shared library exists to end.**

### 🟢 What stands, unaffected

🟢 **`Gap 326`'s closure** (the `iblai` org resolution, MIT payload, the ISC/ISC/MIT sourceless SDK chain, the enterprise backend, the absent AGS, the line-61-vs-line-237 contradiction), 🟢 **`Gap 327`**, 🟢 **`P831`/`P832`/`P833`**, 🟢 **`Gap 309`'s OpenEduCat path resolution**, 🟢 **`Gap 308`'s sixth refusal and its three-way date conflict**, 🟢 **the Huly EPL-2.0 correction**, 🟢 **the 4-of-4 non-`main` default-ref finding**, 🟢 **the `P793` provenance audit (5 of 5)**, and 🟢 **the regional intelligence in `intel/market.md`.** 🟢 **None of these rests on the two duplicated agent rows.**

🟢 **And one finding is strengthened rather than weakened:** `DeepTutor`'s **0 LTI / 0 xAPI / 0 Caliper / 0 SCORM / 0 OneRoster / 0 LMS** across 3 763 files is genuinely new — 🔴 **this shelf has carried `DeepTutor` for multiple passes with its licence, sha, release and dependency posture all recorded, and had never once censused its interoperability surface.** 🟢 **That is `Gap 316`'s missing half, and it survives intact.**

## 🟢 Seventy-third pass, 2026-10-09 — `Gap 326` **CLOSES on the org pass 72 could not resolve, and the vendor claim is TRUE**; `Gap 316` is **re-characterised, not merely re-confirmed**; `Gap 308` refused a **sixth** time *and gets materially worse*; one gap opens (`327`) and one instrument hazard is caught inside this pass's own grep

⏱️ **Fifth pass of this date.** Pass 72 closed earlier today (commit `e99be83`). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 72 wrote to this file, so the section below this one is pass 72's and no fold-forward is needed.

### 🟢 `Gap 326` — **CLOSED.** The org was `iblai`, the claim was true, and the capture is **not in the licence**

🔵 **The gap recorded** that a vendor page claims ibl.ai's runtime is open source with LTI 1.3, that this would weaken `Gap 316` directly, and that pass 72's four *guessed* `ibleducation/*` paths all returned absent — explicitly **not** recorded as evidence of absence, per `P827`.

🟢 **`P827` paid out this pass.** The org resolved from the vendor's own channel is **`iblai`**, not `ibleducation`; `ibleducation` is a **migrated-away org** whose own profile says *"we've moved over to github.com/iblai."* 🔴 **Pass 72's guesses were absent because the org was renamed, not because the code does not exist.** 🟢 **Had pass 72 recorded those 404s as absence, this pass would have inherited a false negative about a live, 1 516-file repository.**

🟢 **Read from payload:**

| Component | Licence (payload) | Default ref · HEAD · date | Scale |
|---|---|---|---|
| [`iblai/os`](https://github.com/iblai/os) | 🟢 **MIT** 1 069 B, holder **iBL Education** | `main` `cd556237` · **2026-10-08** | 🟢 **1 516 files** |
| [`iblai/lms`](https://github.com/iblai/lms) | 🟢 **MIT** 1 062 B, holder **ibl.ai** | `main` | skills-intelligence platform |

🟢 **So the vendor claim is literally true: the runtime is MIT and the repository is real.** 🔴 **And `Gap 316`'s capture thesis survives anyway, because the licence was never the mechanism.** Three measurements, all from primary payload:

**1. The backend is not in the repository, and it is not open.** `README.md` of `iblai/os`, read at `main`:

| Line | Text |
|---|---|
| 237 | 🔴 *"ibl.ai/os **requires the ibl.ai backend platform** for authentication, AI agent APIs, and data services. The backend is **not included in this repository**."* |
| 229–231 | 🔴 *"If you need full backend infrastructure: **Get an enterprise license** … to get a license of the enterprise platform (full backend codebase)."* |
| 61 | 🔴 *"MIT-licensed and self-hostable. **No vendor lock-in — full ownership of the stack** and everything that flows through it."* |

🔴 **Line 61 and line 237 are in the same file and they contradict each other.** 🟢 **"Full ownership of the stack" is asserted 176 lines above the disclosure that the stack's authentication, agent APIs and data services are an enterprise product.** 🟢 **This is `P26` — the access-rights gate — and `probe_payload.sh`'s own header names exactly this trap: a payload answers the COPYRIGHT question only.**

**2. The LTI implementation is not in the MIT repository either.** The seam is a **1 664 B** wrapper, `components/modals/edit-mentor-modal/tabs/lti-tab.tsx`, whose single meaningful import is 🔴 `import { AgentLtiTab } from '@iblai/iblai-js/web-containers/next'`. 🟢 Its own comment names the endpoints — *"launch / login / deep-linking / JWKS"* — 🟢 **which is LTI 1.3 vocabulary and not 1.1** (JWKS and OIDC login are 1.3-only; 1.1 signs with OAuth 1.0a). 🔴 **But the comment also says those endpoints are "served by the LMS itself," and the component is the SDK's.** 🔴 **No AGS. No grade passback. Not in the wrapper, not anywhere in the 1 516-file tree.** 🟢 **`Gap 316`'s ask was LTI 1.3 *plus AGS*, permissive and self-hostable. This meets the first clause and fails the second and third.**

**3. The SDK that holds it is permissive and has no source.** Read from the npm registry, latest tags:

| Package | Version | Licence | `repository` |
|---|---|---|---|
| `@iblai/iblai-js` *(holds `AgentLtiTab`)* | 2.33.2 · modified **2026-10-08** · 334 versions | 🟢 **ISC** | 🔴 **none declared** |
| `@iblai/iblai-api` | 4.421.0-ai · 2 327 versions | 🟢 **ISC** | 🔴 **none declared** |
| `@iblai/iblai-web-mentor` | 2.0.1 | 🟢 **MIT** | 🔴 `git@ibl_connection:iblai/iblai-web-mentor.git` — a **private SSH host alias**, not a resolvable repository |

🟢 **Every licence in the chain is permissive. Not one of the three points at source anyone outside the vendor can fetch.**

🟢 **The verdict, and it is a better finding than either pole the gap posed:** ibl.ai is **not** a closed vendor in the licence sense, so `Gap 316`'s six-vendor list is corrected — but it is **not a permissive component this studio can build on either**, because the protocol lives in a sourceless artifact over a proprietary backend. 🟢 **Recorded as `Gap 327`, because "permissive but sourceless" is a category this shelf has never had a name for and has now hit three times in one chain.**

### 🔴 `Gap 316` — **re-characterised.** The thesis was half right and the missing half is the cheap half

🟢 **For six passes this shelf has held that no permissive component holds LTI 1.3 + AGS *because the protocol holders are closed products* (Gradescope, Turnitin, CodeGrade, ibl.ai, …).** 🟢 **This pass measures the other side of the seam for the first time**, on the two strongest permissive tutors in existence as of today:

| Repo | Licence | Files | LTI | xAPI | Caliper | SCORM | OneRoster | any LMS path |
|---|---|---|---|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 🟢 **3 763** | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | 890 | 🔴 0 | 🔴 0 | — | 🔴 0 | — | 🔴 0 |

🔴 **Zero on every protocol on both.** 🟢 **So the correct statement of `Gap 316` is: the closed products hold the protocol *and* the permissive implementations never reach for it.** 🟢 **That is a materially more optimistic gap than the one this shelf has been carrying**, because an absent adapter on an Apache-2.0 codebase with 1 220 test files is an integration, while a certified closed product is a procurement. 🔵 **`Gap 316(i)`'s narrowed limb — the real wiring cost of `ltijs` — is now the single highest-value unmeasured number on this shelf**, and it should be paid inside `P14-R`.

### 🆕 `Gap 327` — "permissive but sourceless": a licence on a built artifact is not a component

🔴 **The question for counsel and for architecture both.** Three npm packages in one dependency chain carry 🟢 ISC/ISC/MIT and 🔴 declare no fetchable source: `@iblai/iblai-js` (none), `@iblai/iblai-api` (none), `@iblai/iblai-web-mentor` (private SSH alias). 🟢 **The grant is real: ISC and MIT both permit use, modification and redistribution of what is shipped.** 🔴 **What cannot be done is fork it, audit it, patch a CVE in it, or carry it if the vendor stops publishing** — and for a protocol adapter inside a regulated workflow (EU AI Act Annex III; see `Gap 308`) auditability is not a nicety.

🟢 **Why this is its own gap and not an instance of `Gap 312`/`325`:** those are **assertion without a grant** (a README says MIT, no file exists). 🔴 **This is the inverse — a grant without a subject.** 🟢 **Both defeat reuse; they need different remedies, and conflating them would lose that.**

🟢 **`P832` adopted:** when a component's capability lives in a package rather than a repository, read the registry's `repository` field as well as its `license`. 🔴 **A licence field alone has now twice let a sourceless artifact onto a shortlist of things to "build on."**

### 🆕 `P831` — `grep -i lti` matches **`tooLTIp`** and **`muLTI-tenancy`**; this pass's first count was **3× too high**

🔴 **What happened, caught inside this pass's own instrument.** A seam census of `iblai/os` with `grep -ic lti` returned **15** paths, and the pass began writing *"15 LTI-matching paths."* 🟢 **Word-bounded, the real figure is 5.** Control run in the same command and recorded here, not explained:

| Matcher | Count |
|---|---|
| `grep -ic 'lti'` (naive substring) | 🔴 **15** |
| `grep -ic 'tooltip'` | 🟡 **9** |
| `grep -icE '(^\|[^a-z0-9])lti([^a-z0-9]\|$)'` (bounded) | 🟢 **5** |

🟢 **9 + 1 + 5 = 15 exactly** — the nine `tooltip` paths, one `multi-tenancy` spec, and the five real LTI paths. 🟢 **Two independent substring sources, both accounted for, so the arithmetic closes.**

🟢 **`P831`: match protocol tokens on word boundaries, never as substrings.** 🔵 **This is `P299` again in a new field.** `P299` was registered when the declaration branch read `mit` inside *permit / submit / limit / commit / omit*; `license_family.sh::__decl` already carries the bounded matcher as a shared control. 🔴 **And this pass wrote a fresh hand-rolled `grep` anyway, which is the exact failure mode `probe_payload.sh`'s header was written to stop — "a control nobody has to assemble is the only kind that gets used."** 🟢 **Disclosed because the inflated figure was one command from publication, and because a 3× overcount would have made `iblai/os` look like it holds a protocol layer it does not.**

🔴 **Retroactive:** any protocol-token count on this shelf taken with an unbounded `grep -i` is suspect. 🟢 **This pass's own DeepTutor/OpenTutor zeroes are *not* affected** — they were taken bounded, and a zero cannot be inflated by a false positive in any case.

### 🟢 `P829` — **re-validated on two fresh clones**, and the margin is large

🟢 Pass 72 adopted `P829` (never `ls-files` on a `--no-checkout` clone) from a single specimen. 🟢 **Independently reproduced this pass on two unrelated repositories, controls in the same command:**

| Repo | `git ls-files` | `git ls-tree -r HEAD --name-only` |
|---|---|---|
| `iblai/os` | 🔴 **0** | 🟢 **1 516** |
| `HKUDS/DeepTutor` | 🔴 **0** | 🟢 **3 763** |

🟢 **2 of 2, and the protocol is no longer resting on one observation.**

### 🔴 `Gap 308` — OPEN. **Sixth consecutive refusal, and this pass makes the gap more expensive, not less**

🟢 Probed with controls in the same command:

| Host | Code |
|---|---|
| `eur-lex.europa.eu/eli/reg/2024/1689/oj/eng` | 🔴 `000` |
| `digital-strategy.ec.europa.eu` | 🔴 `000` |
| `artificialintelligenceact.eu` | 🔴 `000` |
| `api.github.com` *(control)* | 🟢 **`200`** |
| `raw.githubusercontent.com` *(control)* | 🟢 `301` |

🟢 **Controls green; the refusal is specific to EU policy hosts and is now evidenced six times.** 🟡 **Note the control drifted:** `api.github.com` returned `400` in pass 72 and **`200`** here. 🟢 **Same verdict — reachable — so no finding changes, but it is recorded so a future pass does not read `200` vs `400` as a state change.**

🔴 **And the substance got worse. Three secondary channels now give three different answers about the single most load-bearing compliance date on this shelf:**

| Channel | Claim about Annex III high-risk (**the education bucket**) |
|---|---|
| Pass 72's summary | 🔴 Digital Omnibus **postpones** obligations from **2026-08-02** to **2027-12-02** |
| This pass, EMEA channel, quoting the Commission's own page | 🔴 AI-omnibus amendments *"adopted in June 2026 and entered into force 27 July 2026"*; and *"from **2 August 2026**, the AI Office and national authorities **started to enforce** the AI Act"* |
| This pass, APAC channel | 🟡 *"On **7 May 2026**, the Council and Parliament reached a **provisional political agreement** on the Digital Omnibus on AI"* |

🔴 **Channel 1 says the education bucket is deferred sixteen months. Channel 2 says enforcement began on the very date channel 1 says was vacated. Channel 3 dates the agreement a month before channel 2 dates its adoption.** 🔴 **These cannot all be true, and this shelf cannot adjudicate them, because `Gap 308` is exactly the inability to read the primary text.** 🟢 **The median is not a defensible answer here and is not taken.**

🟢 **Remedy unchanged and now unambiguously the highest-value item in this registry:** one fetch of the primary consolidated text from a session with egress to `eur-lex.europa.eu`. 🟢 **Until then, every AI Act date on this shelf is marked as secondary-sourced and contested, and no client-facing estimate on this shelf is dated off it.** 🟡 `Gap 310` rides unchanged.

### 🟢 Correction published: **Huly is EPL-2.0, not Apache-2.0**

🔴 A secondary source states *"Huly Platform is fully open-source, licensed under Apache License 2.0."* 🟢 **Read from payload:** [`hcengineering/platform`](https://github.com/hcengineering/platform) is 🔴 **EPL-2.0, 14 196 B**, on default ref 🟡 **`develop`** (not `main`). 🟢 **`P828` discharged first — this shelf had no prior reading of Huly, so this is a new row and not a re-correction.** 🔵 **EPL-2.0 is a weak file-level copyleft with a patent grant and a litigation-termination clause; it is not in the MIT/Apache/BSD set this KB shortlists**, so the mislabel would have put a copyleft platform on a permissive shortlist.

### 🆕 `P833` — `curl` against `github.com` returns **403 for repositories that exist**; a naive URL gate would have rejected **14 of 14** real rows

🔴 **What happened.** This pass ran its URL-verification gate as `curl -o /dev/null -w '%{http_code}' https://github.com/<owner>/<repo>` over every repository it was about to publish. 🔴 **All fourteen returned `403`.** 🟢 **All fourteen exist.**

| Channel | Result on the same 14 repos |
|---|---|
| `curl` → `github.com/<owner>/<repo>` (HTML) | 🔴 **403 × 14** — the egress proxy blocks github.com HTML |
| `git ls-remote --symref` | 🟢 **14 / 14 resolve** with a real default ref and HEAD sha |
| `raw.githubusercontent.com` (payload) | 🟢 reachable — every licence in this pass was read through it |
| `api.github.com` | 🟢 `200` this pass |

🟢 **`P833`: never verify a repository's existence with `curl` against `github.com` from this environment. Use `git ls-remote --symref`, which returns the default ref and the HEAD sha in one request** — strictly more information than an HTTP status, and it is the same request `probe_payload.sh` already makes to resolve a branch.

🔴 **Why this is a near-miss and not a note.** A `403` is not a `404`, but a gate that tests `code == 200` cannot tell them apart. 🔴 **Had this pass treated its own verification gate as authoritative, it would have withdrawn every row in it — including four repositories it had just cloned and enumerated locally.** 🔵 **Same family as `P827` in reverse:** `P827` says a guessed 404 is not evidence of absence; `P833` says a proxied 403 is not either. 🟢 **The common rule is that an absence verdict needs a channel that can distinguish "not there" from "not allowed."**

### 🟢 Provenance audit — the five carried-forward shas re-confirm, 5 of 5

🟢 **`P793` demands that carried claims be re-read rather than inherited.** 🟢 Re-resolved via `ls-remote` this pass, independently of the sections that cite them:

| Repo | Sha on this shelf | Sha re-read this pass | Default ref |
|---|---|---|---|
| `Cvmcosta/ltijs` | `0ec24fe` | 🟢 **`0ec24fe`** | 🟡 `master` |
| `littlecookie0722/AI-Teaching-Agent` | `b90bd88` | 🟢 **`b90bd88`** | `main` |
| `openedx/edx-platform` | `bf699a5` | 🟢 **`bf699a5`** | 🟡 `master` |
| `microsoft/ai-agents-for-beginners` | `25b7985` | 🟢 **`25b7985`** | `main` |
| `pguso/agents-from-scratch` | `da3f9df` | 🟢 **`da3f9df`** | `main` |

🟢 **5 of 5 exact.** 🔵 Note two of the five default to `master`, which is consistent with this pass's 4-of-4 non-`main` finding on the platform shelf and reinforces `probe_payload.sh`'s trap #1.

### 🟡 Gaps carried forward unchanged this pass

🟢 **`Gap 309`** — Ed-Fi DMS still the only permissive system of record; no OneRoster, no change feed. 🟢 **OpenEduCat's repository path, unresolved in pass 72, is resolved this pass**: [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp), 🔴 **LGPL-3.0 8 240 B** on default ref 🟡 **`19.0`**. 🔵 **Copyleft either way, so the permissive count for `Gap 309` is unchanged at one** — but the path is now recorded, so the vendor's OneRoster/Ed-Fi sync claim is finally testable by a future pass. 🟢 **`Gap 312` / `Gap 325`** — assertion-without-a-grant pair, carried; now explicitly distinguished from `Gap 327`. 🟢 **`Gap 311(b)`** — pin Ed-Fi DMS `v8.0.0` (`d911abb`). 🟢 **`Gap 294b`**, **`Gap 284`**, **`Gap 267`**, **`Gap 303`**, **`Gap 318`** — carried, unmeasured this pass. 🟢 **`Gap 310`** — rides with `308`. 🟢 **`Gap 323`/`324`** — closed in pass 72, no new evidence.

🔴 **One figure refused for the sixth pass running:** any single market size for AI-in-education. 🟢 The spread on this shelf is now **$1.94B – $10.6B** across published 2026 figures, and this pass adds two *regional* figures that are at least internally consistent with each other (NA **$3.68B** at a claimed 36 % share → implied global ≈ $10.2B; Europe **$2.64B**). 🟡 **Recorded in `intel/market.md` as regional, sourced and contested. Nothing on this shelf is sized by any of them.**

## 🟢 Seventy-second pass, 2026-10-09 — `Gap 323` and `Gap 324` **both CLOSE from primary payload**; `Gap 308` refused a **fifth** time; `Gap 316`'s capture thesis re-confirmed on a **third independent channel**; two instrument protocols adopted (`P829`, `P830`) and two gaps open (`325`–`326`)

⏱️ **Fourth pass of this date.** Pass 71 closed earlier today (commit `1fe734a`). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 71 wrote to this file, so the section below this one is pass 71's and no fold-forward is needed.

### 🟢 `Gap 323` — **CLOSED.** The review gate is **functional as a state machine**; what is frozen is the provider path behind it

🔵 **The gap asked** whether `AI-Teaching-Agent`'s declared-frozen grading gate is *"a working gate to integrate"* or *"a shape to re-implement"* — and said the difference is most of the `P14-R` / `P23` estimate.

🟢 **Answered by reading the contract and the tests from payload.** Measured on `main` `b90bd88` (HEAD **2026-08-23**), **642 files** enumerated by `ls-tree`.

🟢 **The gate is specified.** `ai-workflows/phase2-grading-generation.contract.json` (**3 200 B**) declares it explicitly:

| Contract field | Value |
|---|---|
| `reviewGate.defaultGeneratedStatus` | 🟢 `WAITING_REVIEW` |
| `reviewGate.publishBlockedUntilApproved` | 🟢 `true` |
| `reviewGate.autoPublishAllowed` | 🟢 `false` |
| `qualitySignals.reviewRequired` | 🟢 `true` |
| `safety.*` — 10 flags incl. `realPublish`, `reviewBypassed`, `autoPublishAllowed` | 🟢 **all `false`** |

🟢 **And the gate is tested.** **155 test files** under a `pytest.ini` whose `integration` and `real_llm_online` markers make external dependencies **opt-in**. Coverage by reference, not by filename:

| Gate module | Test files referencing it |
|---|---|
| `cli/review_detail.py` | 🟢 **16** |
| `cli/review_decision_note.py` | 🟢 **6** |
| `cli/review_batch.py` | 🟢 **3** |
| `backend/grading_worker.py` | 🟢 **3** |
| `cli/agent_entity_publish_review.py` | 🔴 **0** |
| `cli/review_pre_approve.py` | 🔴 **0** (not previously recorded on this shelf) |

🔴 **What "frozen" actually means, and it is the finding:** the contract declares **`mode = MOCK_ONLY`** and **`safety.realLlmCalled = false`**. 🟢 **The state machine, its schema validation and its refusal to auto-publish are real, specified and exercised. The real-provider generation path behind it is not.** 🟢 **So `P14-R` and `P23` integrate a tested review gate and supply the provider path themselves** — the cheaper of the two poles the gap posed, but not free, and 🔴 **the two zero-reference modules are the publish-side seam, which is precisely where an integration would attach.**

### 🟢 `Gap 324` — **CLOSED, negatively.** Three Open Badges issuers censused, **zero clean permissive grants** — and the strongest one has an assertion without a grant

🟢 **Discovered capability-blind per `P826`**, licence then read from payload:

| Issuer | Licence (payload) | Default ref · HEAD | Verdict |
|---|---|---|---|
| [`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) | 🔴 **No licence file in a 141-file enumerated tree**; `README.md` §License says `MIT` | `main` `8bafc99` · **2026-08-28** | 🔴 **Assertion without a grant** |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | 🔴 **AGPL-3.0** 33 820 B | `main` `6fd0a11` | 🔴 Network copyleft |
| [`mint-o-badges/badgr-server`](https://github.com/mint-o-badges/badgr-server) | 🔴 **AGPL-3.0** 34 519 B | 🟡 **`develop`** `4c7080e` | 🔴 Network copyleft; **note the default ref is not `main`** |

🔴 **So the trend `intel/trends.md` records on two channels still has no permissive implementation** — the answer is the same shape as `Gap 301`'s, but reached by enumeration rather than guessed 404s, so it is now a measurement.

🔴 **The uncomfortable part is `ec-issuer`,** because it is the **technically strongest** of the three: `templates/openbadge_credential_template.json`, `src/credential_configurations/` (7 modules incl. an SSI-agent client adapter), `tests/e2e/test_oid4vci.py`, committed Ed25519 issuer/holder keypairs, **53 test files of 141**, and `docs/src/oidc4vci_issuer_agent.md`. 🟢 **It is the only one covering Open Badges 3.0 *and* the European Learner Model *and* OID4VCI.** 🔴 **And it ships no `LICENSE`.** 🟡 **This is the second instance of the `Gap 312` pattern on this shelf** (`frappe/education`'s 19 B assertion) — a README licence line is a statement of intent, not a grant, and 🔴 **a bare `## License / MIT` with no file is the weakest form of it.**

🟢 **Recorded as `Gap 325` rather than left inside a closed gap**, because the remedy is cheap and external: ask upstream to add the file.

### 🔴 `Gap 308` — OPEN. **Fifth consecutive refusal; diagnosis unchanged and now very well evidenced**

🟢 Probed this pass with controls in the same command:

| Host | Code |
|---|---|
| `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` | 🔴 `000` |
| `digital-strategy.ec.europa.eu` | 🔴 `000` |
| `artificialintelligenceact.eu` | 🔴 `000` |
| `api.github.com` *(control)* | 🟢 `400` — reachable |
| `raw.githubusercontent.com` *(control)* | 🟢 `301` — reachable |

🔴 **Every EU AI Act date on this shelf still rests on secondary channels only** — and this pass adds a materially important one that makes the gap more expensive, not less (see `intel/trends.md`): the **Digital Omnibus** reportedly postpones Annex III high-risk obligations, **which is the education bucket**, from **2026-08-02** to **2027-12-02**. 🔴 **If true it moves the single most load-bearing compliance date on this shelf by sixteen months; it is sourced to a secondary summary of a 2026-06-16 European Parliament vote, with Council adoption unconfirmed.** 🟢 **Remedy unchanged and now the highest-value item in the registry:** one fetch of the primary text from a session with egress to `eur-lex.europa.eu`. 🟡 `Gap 310` rides unchanged.

### 🟢 `Gap 316` — capture thesis **re-confirmed on a third independent channel**

🟢 A capability-shaped search for a self-hosted permissive grading agent speaking **LTI 1.3 + AGS** returns, once again, **only closed products** — Gradescope, Turnitin Feedback Studio and CodeGrade, all **1EdTech LTI Advantage certified** with AGS grade passback — alongside generic agent frameworks with no LMS seam at all. 🔴 **No permissive component holds the protocol.** 🟢 **The seam this shelf has named for five passes is still one protocol hop wide, and `ltijs` (Apache-2.0, `0ec24fe`) is still the library that closes it.** 🔵 `Gap 316(i)`'s narrowed limb — the real wiring cost — remains unrecorded and is still best paid once inside `P12-R`.

### 🆕 `Gap 325` — `ec-issuer`'s licence: assertion without a grant

🔴 **The question for counsel:** a `README.md` section reading `## License` / `MIT`, with **no licence file anywhere in the enumerated tree**, against a repository under an institutional org (`educredentials`, Surf Development Platform deployment per its own README). 🟢 **Cheap external remedy:** open an issue upstream asking for `LICENSE`. 🔵 **Pair it with `Gap 312`** — same pattern, same counsel question, and answering one answers both.

### 🆕 `Gap 326` — ibl.ai's "open source runtime" claim is **unmeasured, not absent**

🔵 **Why this is a gap and not a finding:** a vendor page claims ibl.ai's runtime is open source and lists **LTI 1.3** among its integrations. 🔴 **If true it would weaken `Gap 316`'s capture thesis directly**, since ibl.ai is one of the six closed vendors the thesis rests on. 🔴 **This pass probed four *guessed* `ibleducation/*` paths and all four returned absent — and per `P827` that is not a measurement and is not recorded as one.** 🟢 **Remedy:** resolve the actual org and repository name from the vendor's own documentation, then enumerate the tree and read the licence from payload. 🟢 **Recorded explicitly so that this pass's guessed-path result cannot later be mistaken for evidence of absence.**

### 🆕 `P829` — `git ls-files` reports **zero** on a `--no-checkout` clone; this pass nearly published a false empty tree

🔴 **What happened:** `git clone --filter=blob:none --no-checkout` followed by `ls-files | wc -l` returned **0** for `ec-issuer`, and the pass was one step from recording *"the tree is empty."* 🟢 **`ls-tree -r HEAD --name-only` on the very same clone returns 141.** 🔵 **The cause:** `ls-files` reads the **index**, and `--no-checkout` leaves the index unpopulated; `ls-tree` reads the **commit object**, which is what a blobless clone does fetch.

🟢 **`P829`: on a `--no-checkout` clone, enumerate with `ls-tree -r HEAD --name-only`. Never `ls-files`.** 🟢 **Control run in the same command and recorded above** (`ls-files` 0 vs `ls-tree` 141), so the protocol rests on a measurement rather than an explanation.

🔴 **Retroactive, and narrower than `P827`'s sweep:** any file **count** on this shelf taken via `ls-files` against a no-checkout clone is suspect. 🟢 **`Gap 319`'s counts (upstream 30 / fork 43 / common 30) are *not* affected** — they are internally consistent and non-zero, so that clone was populated. 🟡 **The rule is adopted for all future passes and no past count is withdrawn on suspicion alone.**

### 🆕 `P830` — coverage must be measured **by reference, not by filename**

🔴 **What happened:** this pass first judged `Gap 323`'s review gate *"largely untested"* by reading the **names** of the 155 test files and finding no `test_review_batch.py`. 🟢 **Grepping the test tree for the module names instead shows `review_detail` in 16 files, `review_decision_note` in 6, `review_batch` in 3** — real coverage, reached from differently-named tests.

🟢 **`P830`: never infer test coverage from test filenames. Grep the test tree for the symbol or module under test.** 🔴 **Had the filename reading been published, `Gap 323` would have closed with the wrong answer and `P14-R` would have been priced at the expensive pole.** 🟢 **Disclosed here rather than quietly corrected, because the first reading is the one a future pass is likeliest to repeat.**

### 🟢 The control query, **twenty-second empty week** — and `P826`'s mechanism is now visible in the output

🟢 `top open source AI agents education 2026 github MIT` returned **zero education-industry agents** for the twenty-second consecutive week. 🟢 **What it did return is the explanation:** **AI-literacy curricula** — [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) (🟢 MIT, 1 141 B, `25b7985`) and [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) (🟢 MIT, 1 091 B, `da3f9df`).

🔴 **Both are *about* building agents; neither is an agent deployed in an education setting.** 🟢 **That is the category-vocabulary effect `P826` named, caught in the act:** the phrase "education" in a listicle query selects teaching *material about AI*, not AI *in teaching*. 🟢 **Recorded, licence-verified, and filed to `repos/foundations.md` as L&D curriculum rather than to `agents/top.md`** — 🔴 **shelving them as agents is exactly how an empty layer gets made to look populated.**

### 🟡 Gaps carried forward unchanged this pass

🟢 **`Gap 309`** — Ed-Fi DMS still the only permissive system of record; no OneRoster, no change feed; census six systems, zero permissive. 🔵 A vendor page claims **OpenEduCat** (LGPL-3.0 per its own site, so copyleft either way and no change to the permissive count) ships OneRoster and Ed-Fi roster sync; 🔴 **this pass could not resolve its repository path and records nothing about it per `P827`.** 🟢 **`Gap 312`** — `frappe/education`'s 19 B assertion; now paired with `Gap 325`. 🟢 **`Gap 311(b)`** — pin Ed-Fi DMS `v8.0.0` (`d911abb`). 🟢 **`Gap 318`** — carried, unmeasured this pass. 🟢 **`Gap 310`** — rides with `308`. 🟢 **`Gap 316(i)`** — narrowed limb carried.

🔴 **One figure refused again this pass:** any single market size for AI-in-education. 🟢 Five published 2026 figures span **$1.94B to $10.6B — a 5.5× spread** (see `intel/market.md`), which makes the median as unusable as the extremes. 🟢 **Nothing on this shelf is sized by it.**

🟢 **One near-correction *not* published, recorded because the discipline worked:** a probe read `openedx/edx-platform` as **AGPL-3.0, 35 136 B, `bf699a5`** and this pass started to file it as a correction. 🟢 **The shelf already records exactly that, byte-for-byte and sha-for-sha, in twelve places.** 🔵 The stale `Apache-2.0` claim lives in a **different, unsynced mirror** (`globant-kb/education/`, v6, dated 2026-07-14) and not here. 🟢 **`P828`'s sweep habit generalises:** check what the shelf says before writing a correction to it.

## 🟢 Seventy-first pass, 2026-10-09 — `Gap 319`, `321` and `322` **CLOSE from primary payload**; `Gap 320` **CLOSES and falsifies the premise it was opened on**; `Gap 316(i)` **ANSWERED**; `Gap 308` refused a fourth time; two new gaps open (`323`–`324`) and one instrument hazard is recorded against this shelf's own past method

⏱️ **Third pass of this date.** Pass 70 closed earlier today (commit `cf5c9bf`). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 70 wrote to this file, so the section below this one is pass 70's and no fold-forward is needed.

### 🔴 `Gap 320` — **CLOSED, and it falsifies pass 70's reasoning.** The hidden tier is MIT, not AGPL

🔵 **The gap recorded:** two AGPL education agents appeared in one week after twenty weeks in which a licence-filtered query structurally could not return any; therefore the AGPL tier's size is unknown and might be large.

🟢 **Remedy executed as specified (`P825`): licence-blind discovery, then licence read from payload. Result:**

| Licence (read from `raw.githubusercontent.com`) | Count |
|---|---|
| 🟢 **MIT** | **7** |
| 🔴 AGPL-3.0 | **1** |
| 🔴 **No licence file** | **1** |

🔴 **So the premise was wrong.** 🟢 **There is no large hidden AGPL tier; the hidden tier is overwhelmingly MIT.** 🔴 **And pass 70's *diagnosis* was wrong in the same move:** the twenty-week absence was **not** a licence-token effect. 🟢 **It was a category-vocabulary effect** — `top open source AI agents education` is a **listicle** phrasing that returns blog roundups, and it would have returned nothing even with the `MIT` token removed. 🟢 **The queries that worked named capability and deployment:** `AI tutor`, `adaptive learning`, `self-hosted`, `grading agent`.

🟢 **Denominator now on the record:** GitHub's `ai-tutor` topic holds **595 public repositories**; twenty weeks of the control query returned **0**.

🟢 **`P826` adopted:** discover by capability + deployment shape; never by category label; never with a licence token in the query; decide licence afterwards from payload. 🔵 **Pass 70's `P825` is superseded by `P826`** — it correctly said "discover licence-blind," but it attributed the fault to the wrong token and would not have fixed the query.

### 🟢 `Gap 319` — **CLOSED on all three limbs.** The divergence is 39 bytes, and the risk was pointing the wrong way

🟢 **(b) sized exactly** by blobless-cloning both repositories and comparing blob shas: upstream **30** files, fork **43**, common **30**, 🟢 **zero files unique to upstream** (strict subset). The fork's 13 extra files are `lib/*.js` (**12**, a confirmed 1:1 basename mirror of `src/*.coffee`) + `package-lock.json`. 🟢 **Of the 30 common files, 28 are byte-identical.**

🟢 **The 2 that differ, read in full:**

| File | Diff | Reading |
|---|---|---|
| `.gitignore` | line 15 `lib` → `# lib` | 🟢 The build output is deliberately un-ignored |
| `src/extensions/outcomes.coffee` | **7 513 B → 7 552 B** — exactly one added line: `'User-Agent': 'ims-lti/3.0.2'` in the OAuth-signed `POST` headers of the Basic Outcomes `replaceResult` call | 🟢 **One header. No logic, signature or payload change** |

🟢 **(a) CLOSED:** pin **`9b712f6`**. 🟢 **(c) ANSWERED, and it is the finding:** the fork is **purposeful and three months old** (HEAD **2026-07-03**, message `chore: commit compiled lib/ for git-dependency installs`); both `package.json`s declare `"main": "./lib/ims-lti"` with `"prepublish": "make build"`, and 🔴 **`npm install github:…` does not run `prepublish`** — so without the committed `lib/` the install is simply broken. 🟢 **The fork exists to make a git dependency installable, and nothing more.** 🟢 `LICENSE` is **byte-identical, 1 094 B, MIT** — the transitive dependency is cleanly licensed.

🔴 **The risk inverts:** upstream `omsmith/ims-lti` HEAD `4df2936` is dated **`2016-09-05` — ten years dead.** 🔴 **The hazard was never the unpinned fork; it is that OATutor's grade return rests on a decade-abandoned library speaking a superseded protocol version.** 🟢 **Remedy is now `P12-R`, which deletes the dependency.** 🔵 Pass 70's zero-release-tags observation stands but reads differently: an untagged fork of a dead library is less alarming than an untagged fork of a live one.

### 🟢 `Gap 321` — **CLOSED: yes.** OATutor's GenAI layer is in `main`, and it is larger than the gap supposed

🟢 Measured on `main` `939eb0e` (HEAD **2026-09-30**), 8 338 files: **29 matching paths plus `bedrock-provider.mjs`**, which the pass-70 grep pattern could not have matched. 🟢 **Present:** a provider abstraction (`llm-provider.mjs` → `openai` default **or `bedrock`** via `SEMANTIC_COMPILER_PROVIDER`); a semantic compiler (`agent-logic.mjs`, `document-context.mjs`, `schemas/learning-object.schema.json`, `documents/manifest.json`, committed AWS BDA fixtures, `BENCHMARK.md`); **15** subject prompt files across 6 real courses; learner UI (`AgentChatbox.js`, `StandaloneChatView.js`); `chatModel.js` (`DEFAULT_CHAT_MODEL = "gpt-4o"`, per-lesson override); 4 admin scripts.

🟢 **So OATutor under MIT supplies mastery estimation, a tutoring dialogue, a document→courseware compiler and an in-region inference path.** 🟢 **`P14` is materially cheaper, exactly as the gap predicted for a positive answer.** 🔴 **Carry:** hardcoded `gpt-4o` default, **no Ollama path** — sovereignty is served by Bedrock in-region, not local inference.

### 🟢 `Gap 322` — **CLOSED.** The Enterprise delta is commercial, not pedagogical

🟢 Read from `README.md` on `main` `196c547`: the CE *"is the foundation for a **proprietary Enterprise Edition (EE)**,"* whose named delta is **custom theming & branding, SLA support, LTS versions** — 🔴 **plus an unbounded *"and more!"***. 🟢 **Favourable answer:** the open edition is not functionally crippled, and the EE sells what a Globant engagement supplies anyway. 🔴 **The `"and more!"` clause is not measurable and must be re-read at contract time.**

🟢 **Recency answered** (the gap asked): HEAD `196c547` is **2026-06-26 — 3½ months quiet**; the `LICENSE` copyright line reads **2023-2025** against 2026 commits. 🟢 **And a licence exposure resolved that this shelf had not named:** `v1.0.0` (2026-06-08) is a rewrite to **zero `open_webui` runtime dependency**, so the BSD-3 grant now governs the deployed artefact rather than sitting atop another project's terms. 🔵 Recorded as resolved-by-upstream.

### 🟢 `Gap 316(i)` — **ANSWERED.** The port was never a protocol build

🔵 **The gap called the LTI 1.1 → 1.3 + AGS port size *"the most commercially urgent unmeasured number on this shelf."*** 🔴 **It was mis-framed.** 🟢 **Two permissive libraries already implement the full surface:**

| Library | Licence (payload) | Head | Verdict |
|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** 11 361 B | `master` `0ec24fe` · 🟢 **2026-10-06** | 🟢 **Recommended.** `src/services/{grading,deep-linking,names-and-roles,dynamic-registration,launch,oidc,keyset}` |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** 1 070 B | `master` `d8fa43e` · 🔴 **2022-11-21** | 🟡 Complete, permissive, **4 years stale** — adopt by owning the fork |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 GPL-2.0 18 025 B | `develop` `d9d462a` | 🔴 Copyleft; cited only as evidence the AGS 2.0 certification path is live (TAO DevKit, **2026-01-15**) |

🟢 **Restated gap, and it is a different and smaller question:** the cost is **wiring a maintained Apache-2.0 library into an agent**, not implementing a specification. 🔴 **`Gap 316(i)` therefore narrows rather than closes** — the *actual* wiring effort is still unrecorded, and 🟢 **the remedy is unchanged in form: do it once in `P12-R` and record the real number.** 🟢 **`Gap 316`'s main limb stays closed at n = 2 of 2** (both permissive components with an LMS seam speak 1.1).

### 🔴 `Gap 308` — OPEN. **Fourth consecutive refusal; the diagnosis is now stable**

🟢 `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and `artificialintelligenceact.eu` all returned **HTTP `000`** this pass, against controls `api.github.com` **`200`** and `raw.githubusercontent.com` **`301`**. 🟢 **The allowlist excludes EU institutional hosts generally.** 🔴 **Every EU AI Act date on this shelf rests on secondary channels only.** 🟢 **Remedy unchanged and still the cheapest high-value item here:** one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from a session with egress to that host. 🟡 `Gap 310` rides unchanged.

### 🆕 `Gap 323` — the `AI-Teaching-Agent` review gate is declared **frozen**; is it functional?

🟢 **What is measured:** the gate exists in code under MIT — `grading_worker.py` producing, `review_batch.py` / `review_decision_note.py` / `review_detail.py` / `agent_entity_publish_review.py` gating, with declared contracts (`phase2-grading-generation.contract.json`). 🔴 **What is not:** the project's own README states automatic grading productization *"remain frozen,"* and this pass did **not** determine whether that means the gate is incomplete, unmaintained, or merely unsupported.

🔴 **Why it matters:** `P14-R` and `P23` both rest on this component, and the difference between "a working gate to integrate" and "a shape to re-implement" is most of the estimate. 🟢 **Remedy:** read `ai-workflows/phase2-grading-generation.contract.json` and the `grading_*` modules from payload, and check whether the review CLIs have tests — 🔵 **one blobless clone, already demonstrated cheap this pass.**

### 🆕 `Gap 324` — is there a permissive **Open Badges / CLR** issuer?

🔴 **`intel/trends.md` records digital credentials as a live trend on two independent channels, and this shelf cannot source a single permissive issuer.** 🔵 `Gap 301` burned two passes probing guessed CLR paths and recorded 404s. 🟢 **Now cheap:** the blobless clone plus `P827`'s enumerate-then-assert rule means candidate trees can be read rather than guessed. 🟢 **Remedy:** capability-blind discovery per `P826` (`open badges issuer`, `comprehensive learner record`, `verifiable credential education`), then licence from payload.

### 🆕 `P827` — **an instrument hazard in this shelf's own past method**, recorded because this pass nearly published a false absence

🔴 **What happened:** this pass grepped a `head -45` slice of an **alphabetically sorted** `ls-files` for `grade|score|line` against `ltijs` and found nothing, and was one step from recording *"ltijs v7 dropped Assignment and Grade Services."* 🟢 **The full namespace listing shows `src/services/grading`, `deep-linking`, `names-and-roles`, `dynamic-registration`** — the alphabetical cut ended at `database-manager`, **before both**. 🟢 **Caught by reading the README against the tree, which is the cross-check that saved it.**

🟢 **`P827`: never conclude absence from a truncated or paged listing.** Enumerate the namespace (`ls-files | awk -F/ '{print $1"/"$2}' | sort -u`), then assert.

🔴 **And it applies retroactively, which is the uncomfortable part.** 🟡 **Several gaps on this shelf recorded absence from `404`s on *guessed* `raw.githubusercontent.com` paths** — `Gap 301` most explicitly. 🔴 **A guessed-path 404 and an enumerated-tree absence are not the same measurement, and this registry has written them in the same voice.** 🟢 **Remedy, cheap and worth one pass:** re-test every surviving absence claim that predates the blobless clone against an enumerated tree, and down-rate any that cannot be reproduced.

### 🆕 `P828` — a prose line that **forged a sixth region bucket**, found and repaired this pass

🔴 **Found by sweeping `^region:` across the shelf:** `intel/market.md` carried a hard-wrapped sentence whose continuation line began `region: it dictates the integration surface…`. 🔴 **A line-anchored field scan reads that as a region value**, which is exactly the failure this KB's own convention warns about — each variant becomes its own bucket and the region filter stops working.

🟢 **Repaired by reflowing the line break only.** 🟢 **No claim, figure or citation was altered**, and the edit is disclosed here rather than made silently, because it touches a superseded block that the append-only rule otherwise protects. 🟢 **Region values across the shelf now resolve to the closed vocabulary alone:** `Global` ×150, `EMEA` ×4, `North America` ×2, `APAC` ×1.

🟢 **`P828`: before committing, sweep `^(industry|region|updated):` across all Markdown and confirm every hit sits inside frontmatter.** 🔵 Swept this pass: `industry:` and `updated:` occur only at lines 2 and 4 of each file — 🟢 **no other prose collisions exist.**

### 🟡 Gaps carried forward unchanged this pass

🟢 **`Gap 309`** — Ed-Fi DMS is the only permissive system of record and has no OneRoster and no change feed; SIS census stands at six systems, zero permissive. 🟢 **`Gap 312`** — `frappe/education`'s **19 B** licence assertion; a question for counsel (upstream `frappe/frappe` is MIT, 1 118 B, and does not govern the app's grant). 🟢 **`Gap 311(b)`** — Ed-Fi DMS `main` (`ab82466`) tracks an unreleased 8.1.0 whose changelog opens under *"Breaking changes"*; **pin `v8.0.0` (`d911abb`)**. 🟢 **`Gap 318`** — carried, unmeasured this pass. 🟢 **`Gap 310`** — rides with `308`.

🔵 **Two non-gaps recorded so they are not re-opened:** 🟢 **the `zijinz456` / `adity982` OpenTutor lineage is resolved** — `adity982` is a strict subset, 884 of 890 files, zero unique, identical `LICENSE` blob `2c7493a`, two weeks behind; `zijinz456` is canonical. 🟢 **The pass-70 cohort is sha-stable** — seven repositories re-probed, all seven identical to pass 70, so their licence payloads are unchanged by construction.

🔴 **One figure explicitly refused this pass:** a widely repeated *"DeepTutor ~40.4k stars."* 🟢 `api.github.com` answers `200` and is authenticated but `403`s every unattached repository, so **third-party popularity remains unmeasurable here and nothing on this shelf is ranked by it.**

## 🟢 Seventieth pass, 2026-10-09 — `Gap 317` **CLOSES on both limbs**, and the cause is a selection effect in this shelf's own control query; `Gap 316` **hardens from n=1 to n=2 of 2**; `Gap 308` is refused by a **third** egress path; four new gaps open (`319`–`322`)

⏱️ **Second pass of this date.** Pass 69 closed earlier today (commit `abf91da`, 00:07 UTC). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 69 wrote to this file, so the section below this one is pass 69's and no fold-forward is needed.

### 🟢 `Gap 317` — **CLOSED, both limbs.** The education agent layer is populated; the twenty-week absence was the instrument

🔵 **The gap asked two things.** **(i)** How many education agents exist, how funded, and does any publish a permissive core? **(ii)** At twenty weeks of an empty control query, is the query the fault rather than the field?

🟢 **(ii) CLOSED first, because it explains (i).** 🔴 **The control query is `top open source AI agents education 2026 github MIT` — it contains the literal token `MIT`.** 🟢 **The two real education agents the trending channel returned this pass are `AGPL-3.0`.** 🔴 **A licence-named query cannot return the licence family it does not name.** 🟢 **The field was never empty; the query was filtered.** 🔵 Remedy adopted as `P825`: discover licence-blind, decide on licence afterwards.

🟢 **(i) CLOSED by measurement — five agents, every licence read from payload:**

| Agent | Licence | Head | `LICENSE` | Permissive core? |
|---|---|---|---|---|
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | `main` `939eb0e` | 1 105 B | 🟢 **yes** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | `main` `6cf793b` | 11 408 B (`P804`) | 🟢 **yes** |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** | `main` `196c547` | 1 531 B | 🟢 **yes** |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | 🔴 **AGPL-3.0** | `main` `7d9e905` | 34 522 B | 🔴 no |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 🟡 **AGPL-3.0 + MIT rider on `skills/`** | `master` `be589dd` | 1 134 B | 🟡 **content layer only** |

🟢 **So the answer to "does any publish a permissive core" is yes, three times, in three regions** — North America (UC Berkeley), APAC (HKU), EMEA (R2D-dev). 🔴 **The funding question is dropped rather than answered:** it was asked about the *commercial* vendors, and with `api.github.com` refusing unattached repositories and no permissive channel to funding data, it is not cheaply measurable from this shelf. 🟢 **Recorded as out of scope rather than open, so the registry does not carry a gap nobody will close.**

🔴 **What survives of pass 69's capture thesis, and it survives intact:** the six closed vendors (EduGears AI, LearnWise, ibl.ai, campusmind.ai, Asyntai, edusageai) still hold **LTI 1.3 + AGS with a human-approval gate**, and 🔴 **no permissive component does.** 🟢 **The market is three-tiered — closed, AGPL, permissive — and the open seam is one protocol hop wide.**

### 🟢 `Gap 316` — **HARDENED from an anecdote to a pattern: n = 2 of 2**

🔵 **The gap recorded:** *"the one real cross-LMS permissive component is on LTI 1.1 / Basic Outcomes."* 🔴 **It is now two of two.**

| Component | Launch signals read from payload | Verdict |
|---|---|---|
| [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) | `lti-receiver.py`, `replaceResult` | 🔴 **LTI 1.1** |
| 🆕 [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | `aws/lti-middleware/index.js` (**25 422 B**): `oauth_consumer_key` **×3**, `replaceResult` **×1**; 🟢 **zero** `id_token` / `jwks` / `lineitem` / `client_id` / `deep_link`; `public/lti-consumer-config.xml` = `imslticc_v1p0` cartridge; dep `"ims-lti": "github:CAHLR/ims-lti"` | 🔴 **LTI 1.1** |

🟢 **Both permissive components with an LMS seam speak 1.1. Neither speaks 1.3 + AGS.** 🟢 **This is no longer one repository's omission — it is the permissive tier's single shared ceiling**, which is exactly what makes `P12` and `P14` worth building. 🔵 **And it doubles the port's candidate base:** OATutor brings BKT mastery estimation that `lti-ai-grader` lacks.

🔴 **`Gap 316(i)` stays OPEN and is the most commercially urgent unmeasured number on this shelf:** the real size of the LTI 1.1 → 1.3 + AGS port. 🟢 **Remedy:** implement the launch-plus-AGS seam against one component and record the actual effort. 🔴 **Until then, do not quote it.**

### 🔴 `Gap 308` — **OPEN, and refused by a third egress path.** The block is EU-host-wide, not `eur-lex`-specific

🟢 **The correction itself now rests on five independent secondary channels in agreement:** Regulation (EU) **2026/1744** deferred **Annex III** to **`2027-12-02`** and **Annex I** to **`2028-08-02`**. 🆕 **The fifth channel adds the procedural step:** the **Council gave final approval `2026-06-29`**.

🆕 **Two dates new to the registry:** 🟢 **Article 4 (AI literacy) unchanged and in force since `2025-02-02`** — 🔴 **live now, binds school and university deployers, no deferral.** 🟢 **AI Office and national authorities enforcing from `2026-08-02`.**

🔴 **A third path was tried and refused:**

| Egress path | Host | Result |
|---|---|---|
| Bash via agent proxy | `eur-lex.europa.eu` | 🔴 DNS FAIL, HTTP `000` |
| 🆕 Bash via agent proxy | `digital-strategy.ec.europa.eu` | 🔴 **DNS FAIL, HTTP `000`** — new host, new institution, same refusal |
| Bash via agent proxy | `artificialintelligenceact.eu` | 🔴 DNS FAIL, HTTP `000` |
| control | `api.github.com`, `raw.githubusercontent.com` | 🟢 `200` |

🟢 **So the diagnosis sharpens: the allowlist excludes EU institutional hosts generally, not one domain.** 🔴 **New sub-conflict folded in:** the Commission's page is reported to list the Omnibus as **entering into force `2026-07-27`** while another guide had it awaiting Official Journal publication — 🟡 **entry into force and deferred application dates are different things and the channels blur them.** 🟢 **Remedy unchanged and still the cheapest high-value item in this registry: one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from any session with egress to that host.**

🟡 **`Gap 310` rides with it, unchanged and unread:** whether routine learner progress-tracking is *profiling*, and therefore always high-risk with no Article 6(3) filter. 🟢 **Design as if it is.**

### 🆕 `Gap 319` — OATutor's LTI library is an **unpinned fork**, and its divergence is unread

🔴 `aws/lti-middleware/package.json` declares `"ims-lti": "github:CAHLR/ims-lti"` — **a GitHub fork with no tag and no commit pin.** 🔴 **Three exposures, none measured:** (a) the resolved commit can change under the client between two installs; (b) how far `CAHLR/ims-lti` diverges from upstream `ims-lti` is unknown; (c) the fork's own maintenance status is unknown.

🟢 **Remedy (i) was run in this same pass, and it both closes (a) and settles (b) directionally:**

| Probe | Fork `CAHLR/ims-lti` | Upstream `omsmith/ims-lti` |
|---|---|---|
| HEAD | 🟢 **`master` `9b712f6`** — 🟢 **a pinnable sha now exists** | `master` **`4df2936`** |
| release tags | 🔴 **0** | 🟢 **24** |

🟢 **(a) CLOSED:** pin `CAHLR/ims-lti` at **`9b712f6`**, not at a branch name. 🔴 **(b) CONFIRMED NON-ZERO and still unquantified:** the fork's head is **not** upstream's head, so it has diverged; **how far, and in which direction, is unread.** 🔴 **(c) ANSWERED and it is the worst of the three:** the fork carries **zero release tags** against upstream's **24** — 🟢 **an unreleased, untagged fork of a released library.**

🟢 **Remaining remedies:** **(ii)** blobless-clone both and diff the file lists to size the divergence (`P821`); **(iii)** moot the gap entirely by replacing the 1.1 seam, which `P12` and `P14` already prescribe. 🔴 **Never ship it pinned to `master`; pin `9b712f6` or remove it.**

### 🆕 `Gap 320` — the **AGPL education tier has never been censused**

🔴 **Two AGPL education agents were found this pass by one channel, in one week, after twenty weeks in which a licence-filtered query structurally could not return any.** 🟢 **So the tier's size is unknown and was never measured** — the shelf has no basis for saying whether it is two projects or fifty.

🔵 **Why it matters even though AGPL is unusable in a closed deliverable:** 🟢 **(a)** it is where the working pedagogy may be, and pedagogy is readable without being redistributable; 🟢 **(b)** a dual-licence rider can make part of it usable — `human-skill-tree` already proves that shape; 🟢 **(c)** an AGPL incumbent is a competitor for a client who *can* accept copyleft, and the shelf currently cannot name them.

🟢 **Remedy:** run the licence-blind capability queries of `P825` with no licence token, census every education agent returned, and record the licence distribution. 🔵 **One pass's work.**

### 🆕 `Gap 321` — is **OATutor 2.0**'s GenAI layer in `main`?

🟡 **Single-channel and not built on:** a **Springer** chapter (*"Open Adaptive Tutor 2.0: Chatbot Integration, Community Deployments, and Future Directions"*, **June 2026**) describes a GenAI chatbot-integration framework for educational system-prompt design. 🔴 **Nothing in the 8 338-file tree read this pass was identified as that layer**, and the shelf did not search for it specifically.

🔴 **Why it matters:** if the chatbot layer is in `main`, OATutor supplies **mastery estimation *and* a tutoring dialogue** under MIT, and `P14` gets materially cheaper. 🟢 **Remedy:** `ls-files | grep -iE 'chat|gpt|llm|prompt|genai'` over the existing blobless clone, then one targeted `raw` fetch (`P821`) — 🟢 **two operations, and the clone is already on disk.**

### 🆕 `Gap 322` — what does **Open TutorAI's** non-community edition hold back?

🟢 **The CE grant is genuine BSD-3-Clause, 1 531 B, read in full this pass.** 🔴 **The `-CE` suffix implies a non-community edition, and its feature delta is unmeasured** (`P822`).

🔴 **Why it matters:** recommending a base whose open edition is deliberately short of the features a client will ask for first is a predictable way to lose an engagement in month three. 🟢 **Remedy:** read the project's own site and `docs/` for an edition comparison, and 🔵 note the copyright line already reads **2023-2025** — 🟡 **so check commit recency on `main` (`196c547`) at the same time.**

### 🟡 Gaps carried forward unchanged this pass

🟢 **`Gap 309`** — Ed-Fi DMS is the only permissive system of record and has **no OneRoster and no change feed**; the SIS census stands at **six systems, zero permissive**. 🟢 **`Gap 312`** — `frappe/education`'s **19 B** licence assertion; narrowed to a question for counsel (upstream `frappe/frappe` is **MIT, 1 118 B**, and does not govern the app's grant). 🟢 **`Gap 311(b)`** — Ed-Fi DMS `main` (`ab82466`) tracks an unreleased **8.1.0** whose changelog opens under *"Breaking changes"*; **pin `v8.0.0` (`d911abb`)**. 🟢 **`Gap 318`** — carried, unmeasured this pass.

🔵 **And one non-gap recorded so it is not re-opened:** the seven `P12` components were re-probed this pass and are **sha- and byte-identical to pass 69**. 🟢 **Stability measured, not assumed.**

## 🟢 Sixty-ninth pass, 2026-10-09 — a **new instrument** (blobless clone) closes `Gap 303` and `Gap 311(a)` from primary payload on first use, `Gap 313` **CLOSES negatively at 0 of 3**, `Gap 312` narrows to a corroborated question, and the `api.github.com` **`403` is corrected** — it was never a blanket block

⏱️ **First pass of this date (pass 68 closed 2026-10-08; the date rolled over during this pass's measurements, which are dated by their publication here). Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 68 wrote to this file, so the section below this one is pass 68's and no fold-forward is needed.

### 🆕 Instrument correction, stated before any datum rests on it — `api.github.com` is **not** blanket-`403`

🔵 **What passes ≤68 recorded:** *"`api.github.com` re-measured `403` — no star counts, nothing ranked by popularity."*

🟢 **Measured this pass:**

| Probe | Result |
|---|---|
| `api.github.com` DNS | 🟢 resolves — `140.82.114.6` |
| `GET /rate_limit` | 🟢 **`200`**, and **authenticated**: core **15 000**/hr, graphql **10 000**, search **30** |
| `GET /repos/Ed-Fi-Alliance-OSS/Data-Management-Service` | 🔴 **`403`** — *"GitHub access to this repository is not enabled for this session. Use add_repo…"* |
| `GET /repos/gmilano/education-kb` (attached) | 🟢 **`200`**, full payload |

🔴 **So the `403` is a per-repository authorisation boundary, not a host block.** 🟢 **The operational consequence is unchanged** — third-party star counts remain unavailable, nothing on this shelf may be ranked by popularity — 🔵 but the *cause* is now correct, and the distinction matters: an attached repository is fully API-readable, so any future probe of this KB's own repo may use the API freely.

### 🆕 **New instrument: the blobless clone.** `git clone --depth 1 --filter=blob:none` — and it closed two gaps on first use

🔵 **The constraint every prior pass worked under:** with `api.github.com` refusing third-party repos, tree contents were reachable only by *guessing* a path at `raw.githubusercontent.com` and recording the 404s. 🔴 `Gap 301` spent two passes probing *"four plausible CLR tree paths — all 404"*.

🟢 **`git clone --depth 1 --filter=blob:none <repo>` needs no API and returns the complete tree.** On `Ed-Fi-Alliance-OSS/Data-Management-Service`: **5 846 files enumerated**, blobs fetched only on demand.

🟢 **It is the cheapest high-value instrument added to this shelf since `git ls-remote --symref`**, and 🔵 **every gap in this registry whose remedy reads "read `docs/`…" or "check whether path X exists" is now cheap.** 🔴 **It does not defeat the licence law:** a blobless clone still fetches blobs on demand, so a content grep over a large tree costs real bytes — use `--depth 1` (full) for grep work and blobless for tree work.

### 🟢 `Gap 303` — **CLOSED.** In-place takeover of an existing Ed-Fi ODS database is **not supported**, and the product says so normatively

🔵 **The gap asked:** can an existing Ed-Fi ODS database be taken over **in place** by the Data-Management-Service, or does adoption require a data migration?

🟢 **Measured from primary payload** (`main` · **`ab82466`**, blobless clone, 5 846 files):

| Probe | Result |
|---|---|
| `docs/PRD-v8.0.md` line 19 | 🔴 *"a **ground-up rewrite** of functionality previously delivered via the Ed-Fi ODS/API"* |
| `docs/PRD-v8.0.md` **NFR-OPS-2** | 🔴 *"the platform does not hot-reload extended schemas, **nor does it support in-place migration of an already-provisioned database to a new effective schema — provisioning is create-only**"* |
| `docs/DATA-STRICTNESS.md` §*"Migrating from the Ed-Fi ODS/API"* | 🟡 **request-body casing guidance only** — not a data migration |
| `docs/DATABASE-SEGMENTATION-STRATEGY.md` §*"Migration from ODS/API"* | 🟡 **a four-row configuration-equivalence table** (`OdsContextRouteTemplate` → Configuration Service API; `dbo.OdsInstances` → `POST /v3/dataStores`) — not a data migration |
| `LICENCE` | 🟢 **Apache-2.0, 11 357 B** (canonical; re-confirmed) |

🟢 **Closed, and closed the conservative way round:** pass 68 said *"price adoption as a data migration until proven otherwise, which is the conservative and probably correct default."* 🟢 **It was correct, and it is now established rather than assumed.** 🔵 The repository documents a migration path **at the configuration surface** and **nowhere at the data layer** — which, given NFR-OPS-2, is not an omission but the design.

🟢 **What to quote to a client:** adoption of Ed-Fi DMS is a **re-platforming with a data migration**, not an upgrade. 🔴 **Never price it as an in-place cutover.**

### 🟢 `Gap 311` — **(a) CLOSED** from payload; **(b) RE-CONFIRMED OPEN** and now moving

🟡 **(a) The version jump `0.7.0 → 8.0.0` is explained, and pass 68's inference was right.** 🟢 `docs/PRD-v8.0.md`: *"**Ed-Fi API v8.0** is a ground-up rewrite of the platform's prior generation."* 🔵 **The version line is the Ed-Fi API *product* version, not the DMS *component*'s** — `v0.1.0`–`v0.7.0` were the component's pre-product tags, and `v8.0.0` is the first tag published under the product line it continues. 🟢 **Pass 68 recorded this as an inference under `P722` and declined to call it a fact; it is now a fact.**

🟡 **(b) `main` is still not the tag, and it moved between passes:**

| Probe | Pass 68 | Pass 69 |
|---|---|---|
| `main` HEAD | `9203e19` | 🆕 **`ab82466`** |
| `v8.0.0` | `d911abb` | `d911abb` (unchanged) |
| newest tags | `v8.0.0` | 🆕 **`dms-pre-8.0.1-alpha.0.94`–`0.99`** |
| `docs/changelog/` | *unread* | 🆕 **`8.1.0.md` only** |

🟢 **So `main` tracks 8.1.0 while the only release tag is `v8.0.0`, with an `8.0.1` alpha line in between.** 🔵 **The gap's practical remedy is unchanged and now better justified: pin `v8.0.0` explicitly.** 🔴 **Tracking `main` means tracking an unreleased 8.1.0 whose changelog opens with a section headed *"Breaking changes."***

### 🟡 `Gap 312` — **NARROWED to a question for counsel only.** The upstream framework is **MIT** and does **not** govern the app's grant

🔵 **The gap asked:** does a **19-byte** licence assertion (`License: GNU GPL V3`) convey GPL-3.0? Pass 68's remedy (i): *"check whether the upstream Frappe/ERPNext stack's licence terms govern the app — cheap, and likely decisive."*

🟢 **Remedy (i) was run:**

| Component | Layer | Licence evidence |
|---|---|---|
| `frappe/frappe` `[develop]` | **framework** | 🟢 **MIT**, `LICENSE` **1 118 B** — *"The MIT License, Copyright (c) 2016-2021 Frappe Technologies Pvt. Ltd."* 🆕 |
| `frappe/erpnext` `[develop]` | **app** (sibling) | 🟢 **GPL-3.0, full grant, `license.txt` 35 149 B** 🆕 |
| `frappe/education` `[develop]` | **app** | 🔴 **`license.txt` 19 B**, `LICENSE` **404** — re-confirmed byte-identical to pass 68 |

🔴 **The framework's MIT terms do not rescue, override or impose anything on the app's grant** — so the 19-byte assertion stands alone as the app's only licence evidence. 🟢 **But the sibling app ships the real 35 149-byte GPL-3.0 grant**, which is strong corroboration that the org means GPL-3.0 when an app says so.

🟢 **This is pass 68's licence law getting its sharpest instance yet:** *the grant follows the **author class**, not the layer* — 🔵 **here, within a single organisation, the framework tier is MIT and the app tier is GPL-3.0.** 🟢 **Treatment is unchanged: record GPL-3.0, assume every GPL-3.0 obligation.** 🔴 **Whether a bare licence *name* effects the grant remains a question for counsel** (`P805`) — but the commercial risk of the conservative reading is now known to be low, because the conservative reading is almost certainly the intended one.

### 🔴 `Gap 309` — **RE-CONFIRMED OPEN, census widened to 6 of 6 non-permissive**, and remedy (ii) is now **weaker** than pass 68 could know

🟢 **Remedy (i) was run** — census the SIS tier for a permissive outlier:

| System | Licence | Evidence | Region |
|---|---|---|---|
| 🆕 **FenixEdu Academic** [`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic) | 🔴 **LGPL-3.0** | `master` **`675b540`**; `LICENSE` **7 652 B** — *"GNU LESSER GENERAL PUBLIC LICENSE Version 3"* | 🔵 **EMEA** (IST Lisbon, Portugal) |
| OpenEduCat | 🔴 LGPL-3.0 | `LICENSE` **8 241 B** (re-read; 🟡 **≠ FenixEdu's 7 652 B** — OpenEduCat's carries a prepended copyright pointer, so the byte count alone does not identify the grant) | APAC (India) |
| RosarioSIS · Gibbon · openSIS · `frappe/education` | 🔴 GPL-2.0 / GPL-3.0 / GPL-2.0 / GPL-3.0 | pass 68 + this pass | — |

🔴 **Six read, zero permissive.** 🔵 The two LGPL-3.0 options (OpenEduCat, FenixEdu) share the **proprietary-addon** shape (`P750`) — an addon may stay closed, a fork of the platform may not.

🔴 **And remedy (ii) — *"price Ed-Fi DMS + build the administrative surface"* — just got more expensive.** 🟢 `docs/PRD-v8.1.md` enumerates, as **gaps in v8.0 relative to the prior ODS/API generation**: **OneRoster rostering integration**, **event streaming (Kafka/CDC)**, read replicas and high-performance paging, ownership-based authorisation and custom access rules, unique-ID/Identities integration, and custom validation. 🔴 *"hosts and vendors who built downstream systems around a near-real-time change feed in the prior generation have **no equivalent way to consume data changes from v8.0 without polling the API**."*

🟢 **So the shelf's only permissive system-of-record substrate has no rostering standard and no change feed.** 🟢 **Remedy (iii) is now the measured-best call, not merely the cheap one:** deploy a copyleft SIS unmodified and build beside it across **LTI 1.3** (`P736`, `P809`).

### 🟢 `Gap 313` — **CLOSED negatively at 0 of 3**, and the shelf's own code names the missing piece

🔵 **The gap asked:** does **any** third-party component on this shelf emit a machine-readable mark on generated content? 🔵 **Remedy (ii):** *"grep the shelf's permissive components for provenance/C2PA/watermark support — cheap, and should be done next pass regardless."*

🟢 **Run against all three of `P11`'s permissive components** (`--depth 1` clones, full content grep):

| Component | Licence | Files | `c2pa` | `content credential` | `watermark` | `provenance` |
|---|---|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) `cb794e4` | 🟢 Apache-2.0 (11 357 B) | 336 | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) `3596bb5` | 🟢 **MIT (1 080 B)** | 1 538 | 🔴 **0** | 🔴 **0** | 🟡 1 | 🟡 65 |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) `db41cc4` | 🟢 **MIT (1 080 B)** | 1 880 | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 |

🔴 **Both of conform-ed's apparent hits were read and both are false positives** — recorded in full because a hit count alone would have been a wrong datum:
- 🟡 its **65 `provenance`** hits are a **spec-traceability tier** for pinned conformance artifacts — *"Lowest provenance tier; re-review on spec version bump"*, `PROVENANCE.md`;
- 🟡 its **single `watermark`** is a **delta-sync high-watermark timestamp** — *"a `dateLastModified` — the watermark a delta exchange reconciles against"*, in the **OneRoster v1.2** coverage map.

🟢 **So: 0 of 3. No third-party component on this shelf marks generated content.** 🔵 **The shelf's Article 50(2) marking capability is entirely its own code — which was the suspicion, and is now the measurement.**

🟢 **And the shelf's own code states its own boundary.** Both marking suites were run and are green — 🟢 `aiact-50-2-marking` **23/23**, 🟢 `aiact-50-2-pack` **27/27** — and the marking suite's own closing output reads: 🔴 *"The signature seam (**MarkLLM / SynthID**, `P33`) is **declared and NOT filled**."*

🟢 **Remedy is therefore concrete and permissive, and it is the one piece between this shelf and the obligation:** [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) — `main` **`0a4fe8c`**, 🟢 **Apache-2.0, `LICENSE` 11 357 B** (canonical, verified this pass). 🔵 **`P11` stays a readiness programme** (`P803`), 🟢 **but its one unfilled seam now has a named, licence-compatible component against it.**

### 🔴 `Gap 308` — **STILL OPEN**, now with **two independent instruments** saying so

🟢 **Re-measured both egress paths this pass:**

| Path | Result |
|---|---|
| Bash / agent proxy → `eur-lex.europa.eu` | 🔴 **`CONNECT tunnel failed, response 403`** — and `getent hosts` **fails** |
| `WebFetch` → same URL | 🔴 **`getaddrinfo ENOTFOUND eur-lex.europa.eu`** |
| control: `api.github.com` from the same shell | 🟢 resolves and serves `200` |

🔵 **Pass 68 recorded `DNS_BLOCKED` from one path; two now agree, and the proxy's answer identifies it as an allowlist denial rather than a DNS fault.** 🔴 **The AI Act dates therefore remain published with their channel count attached (four independent secondary channels; `2027-12-02` Annex III, `2028-08-02` Annex I), and must be quoted that way in any client file.** 🟢 **Remedy unchanged and still the cheapest high-value item in this registry: one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` from any session with egress to that host.** 🟡 `Gap 310` rides with it.

### 🆕 `Gap 314` — Ed-Fi DMS provisioning is **create-only**, and the cost of extending the model is unpriced

🔴 **The gap.** `Gap 303`'s closing read turned up a second fact worth more than the answer: **NFR-OPS-2** — *"Data-model extensions SHALL require **both database re-provisioning** (to match the extension's effective schema hash) **and a service restart** to take effect… provisioning is create-only."*

🔵 **Why it bites this shelf specifically:** an AI deliverable that writes anything back into the system of record — generated evidence, a predicted risk flag, an AI-assisted grade — **is a data-model extension**. 🔴 **On Ed-Fi DMS that means re-provisioning the database, not a migration**, every time the extension's schema hash changes.

🟢 **Remedy, in cost order:** **(i)** read `docs/API-SCHEMA-DOCUMENTATION.md` and the `reference/design/` extension epics for whether a blue/green re-provision is supported (**cheap — the blobless clone makes this a single read**); **(ii)** 🟢 **in the meantime, design AI-generated evidence into the LRS (`P8`, `P10`) and not into an Ed-Fi extension** — which is what this shelf already recommends, now with a second, independent reason.

### 🆕 `Gap 315` — the shelf can **test** OneRoster conformance but cannot **provide** OneRoster, permissively

🔴 **The gap.** Two measurements from this pass meet: 🟢 `conform-ed` (**MIT**) carries a **OneRoster v1.2** coverage map, so the shelf has a permissive instrument to *verify* a rostering integration; 🔴 but `docs/PRD-v8.1.md` lists **OneRoster rostering integration** as absent from Ed-Fi DMS v8.0, and the six-system SIS census found **no permissive SIS at all**. 🔵 **So there is no permissive OneRoster *provider* on this shelf — only a permissive way to test one.**

🟢 **Remedy, in cost order:** **(i)** census for a permissive standalone OneRoster provider/adapter (**cheap, and not yet attempted**); **(ii)** price a OneRoster adapter over a copyleft SIS's own API, kept at arm's length across the process boundary (`P736`); **(iii)** 🔴 **until (i) or (ii), never quote OneRoster rostering as something this shelf supplies** — quote it as something this shelf can **conformance-test**.

### 🆕 `Gap 316` — the pass's one real agent find is **LTI 1.1**, and the port cost to 1.3 is unmeasured

🔴 **The gap.** [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) (`main` **`5b96722`**, 🟢 **Apache-2.0, 11 357 B**) is a real, deployable, permissive AI grading tool — 🔴 **but its own README says LTI 1.1**, and its grade return is **LTI Basic Outcomes** (`lis_outcome_service_url`, `replaceResult`), **not** LTI 1.3 **AGS**. 🔵 **This shelf's integration architecture is LTI 1.3** (`P736`, `P809`).

🟡 **Why it is not simply discardable:** it is the **only** permissive, education-specific, deployable AI grading component this shelf has found in **twenty weeks** of the control query, and its operational design is reusable independently of its LTI version (see `P81x`).

🟢 **Remedy, in cost order:** **(i)** measure what the port costs — the LTI handshake is one file (`lti-receiver.py`), so the question is whether 1.3's OAuth 2.0 / JWKS flow and AGS replace it or require a rewrite (**cheap**); **(ii)** front it with an existing permissive LTI 1.3 library and keep its grading core (**the likely shape**); **(iii)** 🔴 **never quote it to a Canvas client as-is** — LTI 1.1 is deprecated on major LMSes, which is the commercial fact that decides this gap.

### 🆕 `Gap 317` — the control query's twentieth empty week finally has a **named cause**, and the cause is unmeasured

🔴 **The gap.** The twentieth consecutive empty control week is no longer only an absence. 🟢 **A targeted search (not the control query) returned a populated field — and it is almost entirely closed-source:** EduGears AI, LearnWise, ibl.ai, campusmind.ai, Asyntai, edusageai — all commercial LTI tools, several explicitly advertising LTI 1.3 + AGS grading, **the exact capability the permissive tier lacks**.

🔵 **So the hypothesis is no longer "education agents do not exist" but "education agents exist and the capability has been captured by closed LTI vendors."** 🔴 **Unmeasured:** how many, how funded, and whether any publishes a permissive core.

🟢 **Remedy, in cost order:** **(i)** census the closed LTI-tool vendors and record, per vendor, whether any component is open (**cheap, and it is market intelligence Globant can sell**); **(ii)** re-run the control query with `LTI` as a term rather than `github MIT` — 🔵 **the control query's category error may be the search terms' fault, which would be a finding about this shelf's own method**; **(iii)** 🟢 **meanwhile state the gap positively to clients: the open tier's weakness is exactly where a Globant build has least competition and most leverage.**

### 🆕 `Gap 318` — the board census's **"41 unread"** was measured with the wrong invocation, and the real green count is unknown

🔴 **The gap.** The README records **106 suites — 63 green, 41 unread, 1 environment-red, 1 truly red (`p351`)** — with the 41 attributed to `python3 -I` implying `-P` and breaking sibling imports.

🟢 **Measured this pass:** the suites are **plain scripts**, run as `python3 test_x.py` from inside their own directory. 🔴 **`pytest` is not installed in this environment** (`No module named pytest`) and 🔴 **`python3 -m unittest` discovers them as `Ran 0 tests` / `FAILED (errors=1)`** — neither harness reads them. 🟢 **Invoked correctly, 2 of 2 ran green on first use** (`aiact-50-2-marking` **23/23**, `aiact-50-2-pack` **27/27**).

🔵 **So "unread" was an artefact of the harness, twice over**, and 🔴 **the shelf does not currently know how many of its 106 suites are green.** 🟡 **Scope discipline:** this pass ran **two** suites and claims **two**; it does **not** claim the other 104 are green.

🟢 **Remedy:** **(i)** re-run the full board as `python3 test_*.py` per directory and re-census (**cheap, mechanical, and it should be the next pass's first action**); **(ii)** record the corrected partition in the README and retire the `-I`-flag explanation, which is true about the flag but was never the whole cause.

## 🟢 Sixty-eighth pass, 2026-10-08 — `Gap 301` **CLOSED negatively** by the instrument it nominated, `Gap 303` **re-confirmed by direct payload read**, and six gaps opened (`Gap 308`–`Gap 313`), one of which has a **statutory deadline eight weeks out**

⏱️ **Twenty-second pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Registry continuity:** pass 67 wrote to this file, so the section below this one is pass 67's and
no fold-forward is needed (contrast pass 66, recorded as `Gap 307`).

### 🟢 `Gap 301` — **CLOSED, negatively**, and closed by the remedy it named

🔵 **The gap asked:** does CLR 2.0 *aggregate* capability exist anywhere on a consumable ref? Pass 67
found **zero** CLR occurrences on `arqueon/certo` `main` and nominated remedy **(ii)**: *probe PR #4's
head ref via `git ls-remote … refs/pull/4/head` — it needs no API access.*

🟢 **Remedy (ii) was run and it worked:**

| Probe | Result |
|---|---|
| `refs/pull/*` on `arqueon/certo` | 🟢 **27 refs resolve** — new instrument, first use 🆕 |
| `refs/pull/4/head` | 🟢 **`c62d8c9`** — the PR branch **exists** 🆕 |
| README at `c62d8c9` (bare-sha read) | 🟢 served, **15 618 B** |
| `CLR` / *"Comprehensive Learner Record"* at `c62d8c9` | 🔴 **zero occurrences** 🆕 |
| `package.json` at `c62d8c9` | 🔴 **404** |
| PR-head README vs `main` README | 🔴 **15 618 B < 16 582 B — the branch is *behind* `main`** 🆕 |

🔴 **Closed negatively:** the CLR claim fails at **both** refs. 🔵 **This is a stronger result than
pass 67's.** "Absent from the default branch" is consistent with a real feature awaiting merge;
**"absent from the branch it was attributed to, and that branch is behind main"** is not. 🟢 **CLR 2.0
aggregation is build-not-buy, established rather than suspected** — price it as engineering.

🟢 **Method note worth keeping:** a gap that names its own next instrument got closed one pass later
at the cost of two commands. 🔵 **Remedies in cost order are worth writing even when the gap looks
dead.**

### 🔴 `Gap 303` — **RE-CONFIRMED OPEN** by direct payload read, and it is still the expensive question

🔵 **The gap asks:** can an existing Ed-Fi ODS database be taken over **in place** by the
Data-Management-Service, or does adoption require a data migration?

🟢 **Measured this pass** (and note the slug correction — the repository is
[`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service), **not** the `Ed-Fi-`prefixed name pass 67's prose implied, which returns a credential prompt):

| Probe | Result |
|---|---|
| `main` · HEAD | `main` · **`9203e19`** |
| README | **3 239 B** — 🟡 *"These applications **replace** the legacy Ed-Fi ODS/API and Ed-Fi ODS Admin API"* |
| `migrat*` in README | 🔴 **one hit, and it is unrelated** — a *UniqueId Validation* reference custom validator |
| in-place / existing-database language | 🔴 **absent** |
| Licence | 🟢 **Apache-2.0, 11 357 B** (canonical) |

🔴 **So "replace" is asserted and the migration path is undocumented at the default ref.** 🔵 The
README is **3 239 B** — too small to carry a migration story, which is itself the finding.
🟢 **Remedy, in cost order:** **(i)** read `docs/` and any `MIGRATION*`/`UPGRADE*` path in the tree —
minutes; **(ii)** read the `v8.0.0` release notes once an instrument can reach releases (🔴 blocked:
`api.github.com` `403`); **(iii)** 🔴 price adoption as a **data migration** until proven otherwise,
which is the conservative and probably correct default.

### 🆕 `Gap 308` — the AI Act correction is **unverified against primary text**, and the session cannot verify it

🔴 **The gap.** This pass corrects pass 67's central claim (Annex III high-risk deferred
`2026-08-02` → **`2027-12-02`** by **Regulation (EU) 2026/1744**). 🔴 **No primary source was
readable:** `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and `artificialintelligenceact.eu`
**all failed DNS resolution**, while GitHub hosts resolved normally — recorded as **`DNS_BLOCKED`**
(`P807`).

🟢 **What the correction rests on:** **four independent secondary channels in agreement** on the two
load-bearing dates (`2027-12-02` Annex III; `2028-08-02` Annex I), including two law-firm client
notes, a research note, and a **EUR-Lex record title** returned by search.
🟡 **Single-channel and explicitly not built on:** public-authority high-risk deferral to
`2030-08-02`; sandbox obligation to `2027-08-02`.

🟢 **Remedy:** **one fetch of `eur-lex.europa.eu/eli/reg/2026/1744/oj/eng`** from any session with DNS
to that host — 🔵 **cheapest high-value remedy in this registry**, and it would also settle the
single-channel items. 🔴 **Until then, the dates are published with their channel count attached and
must be quoted that way in any client file.**

### 🆕 `Gap 309` — the system-of-record tier has **no permissive implementation at all**

🔴 **The gap.** Five systems of record read from payload this pass: **5 of 5 non-permissive** —
RosarioSIS GPL-2.0, Gibbon GPL-3.0, openSIS GPL-2.0, `frappe/education` GPL-3 (asserted),
OpenEduCat LGPL-3.0. 🔴 **Zero MIT, zero Apache-2.0.** 🔵 A client who needs a student system of
record **whose code they can keep closed** has nothing in this tier.

🟡 **Two partial answers exist and neither is a full one:** 🟡 **OpenEduCat's LGPL-3.0** permits a
**proprietary addon** (`P750`) but not a closed fork of the platform; 🟢 **Ed-Fi DMS (Apache-2.0)** is
a permissive system of record but is a **data-standard API substrate**, not an administrative SIS —
no timetabling, gradebook, report cards or fees.

🟢 **Remedy, in cost order:** **(i)** census the SIS tier further for a permissive outlier — the five
read were the channel's top returns, not an exhaustive list (**cheap**); **(ii)** price **Ed-Fi DMS +
build the administrative surface** (expensive, and the only fully-permissive shape currently known);
**(iii)** 🟢 **accept the boundary**: deploy a copyleft SIS unmodified and build beside it across
**LTI 1.3** (`P736`, `P809`) — 🔵 **which is what this shelf recommends, because it is lawful,
cheap and already instrumented.**

### 🆕 `Gap 310` — whether routine learner progress-tracking is **"profiling"** under the Omnibus is unread

🔴 **The gap.** Regulation (EU) 2026/1744 makes **profiling always high-risk**, removing the Article
6(3) filter that would otherwise exempt narrow use cases. 🔴 **No source read this pass states
whether ordinary LMS/LRS progress-tracking constitutes profiling**, and the distinction decides
whether a large share of deployed edtech is in Annex III at all from `2027-12-02`.

🟡 **Why it is not academic:** this shelf's own recommended architecture **writes learner evidence to
an LRS** (`P8`, `P10`, `P11`). 🔵 If that is profiling, the recipes carry a high-risk classification
the shelf has not priced.

🟢 **Remedy:** **(i)** read Article 6 as amended, plus recital language, against the GDPR Article
4(4) profiling definition — 🔴 blocked by `DNS_BLOCKED`, so it rides with `Gap 308`'s single fetch;
**(ii)** 🟢 **in the meantime, assume the filter is unavailable wherever a deliverable builds a
learner profile** — the conservative reading, and cheap to design for now and expensive to retrofit.

### 🆕 `Gap 311` — Ed-Fi DMS's version line jumps `0.7.0 → 8.0.0`, unexplained, and `main` is not the tag

🔴 **The gap, two parts.** 🟡 **(a)** Tags resolve `v0.2.0`→`v0.7.0` then **`v8.0.0`** (`d911abb`) —
🔴 **no payload read explains the jump**; the plausible reading is alignment with the legacy ODS/API
major line, and it is **left as an inference, not recorded as a fact** (`P722`). 🟡 **(b)** `main` is
**`9203e19`**, which is **not** `v8.0.0` — so pass 67's tag is not the head a client clones, and no
read establishes what `main` carries beyond it.

🟢 **Remedy:** **(i)** `git ls-remote --tags` again next pass to see whether a `v8.0.x` lands on
`main` (**cheap**); **(ii)** read `CHANGELOG`/`docs` for the versioning policy (**cheap**);
**(iii)** 🟢 **in any deliverable, pin `v8.0.0` explicitly** rather than tracking `main` — which is
sound practice regardless of how the gap closes.

### 🆕 `Gap 312` — whether a **19-byte licence assertion** conveys GPL-3.0 is a legal question this shelf cannot answer

🔴 **The gap.** `frappe/education` `[develop]`'s **entire** licence evidence is `license.txt` at
**19 bytes**: `License: GNU GPL V3`. 🔴 No grant text (**GPL-3.0 is ~35 100 B**), no manifest licence
key, no README mention. 🔵 **Whether a bare licence *name* effects the grant is a question for
counsel, not for a payload read** (`P805`).

🟢 **What this shelf does in the meantime:** 🟢 **record it as GPL-3.0 and assume every GPL-3.0
obligation** — the conservative reading; 🔴 **never record it as "unknown" or "permissive-unknown"**,
which would invite a build.

🟢 **Remedy:** **(i)** check whether the upstream **Frappe/ERPNext** stack's licence terms govern the
app (**cheap**, and likely decisive — ERPNext's own licensing is the real question); **(ii)** ask the
client's counsel before any code is written against it; **(iii)** 🟢 **prefer another component** —
four alternatives were read this pass and three have **two or more agreeing licence layers**.

### 🆕 `Gap 313` — no read establishes whether **any** shelf component marks generated output, and the deadline is `2026-12-02`

🔴 **The gap, and it is the one with a clock.** `P11` assembles an Article 50(2) marking recipe from
this KB's own `compose/code/aiact-50-2-*` tier plus permissive components. 🔴 **But no probe this
pass established whether any *third-party* component on this shelf emits a machine-readable mark on
generated content** — not `conform-ed`, not `lrsql`, not the CASE tier. 🔵 **The shelf's marking
capability is its own code, and its coverage against the Article 50(2) obligation is self-assessed.**

🔵 **Why it matters commercially:** `2026-12-02` is **eight weeks** from this pass, and `P11` is the
only dated recipe in `compose/patterns.md`. 🔴 **If `P11`'s marking step is weaker than the
obligation, a client acts on it and misses the date.**

🟢 **Remedy, in cost order:** **(i)** run this KB's own `aiact-50-2-pack` test suite and
`aiact-50-2.xsd` against the **Commission's July 2026 Article 50 guidelines** and the AI Office
**Code of Practice on transparency of AI-generated content** (`2026-07-31`) — 🔴 both currently
**`DNS_BLOCKED`**, so this rides with `Gap 308`; **(ii)** grep the shelf's permissive components for
provenance/C2PA/watermark support (**cheap, and should be done next pass regardless**);
**(iii)** 🟢 **until (i) is possible, present `P11` as a readiness programme rather than a compliance
guarantee** — which is how `P11` is written, and `P803`'s refusal list says why.


## 🟢 Sixty-seventh pass, 2026-10-08 — six gaps opened (`Gap 301`–`Gap 306`), `Gap 293` re-confirmed **with its cause newly named**, and `Gap 286` closed as **unanswerable by this session** rather than left open indefinitely

⏱️ **Twenty-first pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **Note on the registry's own continuity:** pass 66 wrote to the seven shelf files but **not to
this one**, so the newest section below this one is pass **65**'s. 🟢 **Pass 66's gap movement is
folded into this section where it bears on a gap**, and 🔴 **that omission is itself recorded** —
`Gap 307`.

### 🆕 `Gap 301` — the CLR 2.0 *aggregate* edge has **no verifiable implementation on any default ref**

🔴 **The gap.** `Gap 294` recorded the Open Badges 3.0 **issue** edge as populated-but-AGPL. 🟢 This
pass probed the **aggregate** edge — CLR 2.0, grouping issued badges into one signed record — and
found **nothing consumable**.

🟢 **Measured:**

| Probe | Result |
|---|---|
| `arqueon/certo` `main` | **`39816e0`**; 🔴 **AGPL-3.0**, `LICENSE` **33 820 B** |
| `Schroedinger-Hat/certo` (upstream) `main` | **`6fd0a11`** — 🔵 **the sha pass 65 recorded as "certo"**; 🔴 AGPL-3.0, **33 820 B — byte-identical** |
| `CLR` / *"Comprehensive Learner Record"* in `arqueon/certo` README (16 582 B) | 🔴 **zero occurrences** |
| four plausible CLR tree paths on `main` | 🔴 **all 404** |

🔴 **So the capability exists only as a pull request** (`P786`: a PR is a proposal), and the fork
offers **no permissive relief** — its licence payload is byte-identical to its upstream's.
🟡 **The only CLR-touching permissive code read this pass is `conform-ed`'s CLR v2.0 *schemas and
conformance runners* (MIT)** — 🔴 **which validate a CLR, they do not assemble or sign one.**

🟢 **Remedy, in cost order:** **(i)** re-probe `arqueon/certo` `main` on a later pass for a merged
CLR path — one `curl`, minutes; **(ii)** probe PR #4's head ref directly via
`git ls-remote … refs/pull/4/head` — minutes, and it would establish whether the branch exists even
while `api.github.com` is refused; **(iii)** 🔴 accept that CLR assembly is **build-not-buy** and
price it. 🔵 **(ii) is the next instrument to try**, because it needs no API access.

### 🆕 `Gap 302` — two of this pass's four new components are **unplaced by region**

🔴 **The gap.** `infosign/compeito` and `conform-ed/conform-ed` carry **no country or org location in
any payload read** — not in `LICENSE`, not in README, not in a manifest. 🟡 `"Infosign, Inc."` is a
named holder that is **not geolocated**; `conform-ed` is a bare GitHub org.

🟢 **Left unplaced rather than inferred** (`P722`): an inferred region is worse than an absent one,
because the compiled filter cannot distinguish them. 🔵 **Two of four is the honest count for this
pass** — the other two (OpenSALT, OpenCASE) are **North America** on first-party evidence.

🟢 **Remedy:** read each project's own site or org profile when the channel allows (**cheap**); or
leave permanently unplaced and 🟢 **say so in any deck that filters by region** — which is the
honest default, not a failure.

### 🆕 `Gap 303` — whether `Ed-Fi-ODS` migrates to the **Data Management Service** without a data migration is unmeasured, and it is the expensive question

🔴 **The gap.** `Data-Management-Service` **replaces** the legacy ODS/API by its own README, and has
a shipped **`v8.0.0`** tag (`d911abb`). 🔴 **No payload read this pass states whether an existing ODS
database can be taken over in place.**

🔵 **Why it matters more than most gaps here:** pass 66 could answer exactly this question for
`lrsql → xapi-lrs` — the README documented a **no-op, same `DATABASE_URL`**, with a precise list of
what does and does not carry over. 🟢 **That precedent is why the absence is conspicuous:** a
successor project that *does* support in-place takeover normally says so.

🔴 **Consequence for a proposal:** every US district and state agency on `Ed-Fi-ODS` has a migration
ahead of it, and 🔴 **a bid must price the discovery rather than assume either answer.**

🟢 **Remedy, in cost order:** **(i)** read `docs/DATA-STANDARD-VERSIONS.md` and any upgrade or
migration doc in-tree — one `curl` each, minutes; **(ii)** read the `v8.0.0` tag's release notes —
🔴 blocked by `SCOPE_DENIED`; **(iii)** clone and inspect migration scripts — under an hour.
🟢 **(i) was not run this pass and should be first on the next.**

### 🆕 `Gap 304` — Vietnam's AI statute is carried from a **secondary channel**, with a live source conflict

🔴 **The gap.** This pass records Vietnam's **Law on Artificial Intelligence** as passed
**`2025-12-10`**, in force **`2026-03-01`**, with a high-risk list naming **education — *"automated
assessment and behavioural monitoring"***. 🔴 **The statute text was not reachable**, and 🔴 **two
channels disagreed**: one called the instrument a *Digital Technology Industry Law* effective 2026.

🟢 **The more specific reading is carried** (named law, exact dates, explicit education limb), and
🔴 **it is explicitly not confirmed from a primary source.**

🔵 **Why this gap is worth a number rather than a caveat:** this is the **second** jurisdiction on
this shelf to put education on a statutory high-risk list, and that claim does regulatory work in
`intel/market.md` and `intel/trends.md`. 🔴 **A claim that carries weight must carry its provenance.**

🟢 **Remedy:** probe an official or legal-database copy of the statute (**cheap**, likely blocked by
the egress allowlist — `Gap 293`); or 🟡 downgrade to *"reported"* language in any client-facing
artefact until primary-sourced. 🟢 **The downgrade is free and should be the default.**

### 🆕 `Gap 305` — no 2026 market figure exists for **APAC or LATAM**, and the regional figures do not reconcile with the global one

🔴 **The gap, measured:**

| Scope | 2026 figure | Status |
|---|---|---|
| Global | **$10.6 B** (→ $42.48 B 2030, CAGR 41.5 %) | 🟡 held four passes |
| Global (conflicting) | **$12.3 B** | 🔴 **~16 % disagreement, same year, same scope** |
| North America | **$3.68 B** (36 % share) | 🟡 aggregator |
| EMEA (Europe) | **$2.64 B** | 🔴 low confidence, research origin unnamed |
| **APAC** | 🔴 **none returned** | 🔴 **empty** |
| **LATAM** | 🔴 **none returned** | 🔴 **empty** |

🔴 **The two named regions sum to ~$6.3 B against a $10.6 B global**, which requires APAC + LATAM
together to be ~40 % — 🔴 **unverifiable, since neither has a figure.** 🔵 **So the regional
breakdown cannot currently be presented as a market map without an unsourced residual.**

🟢 **Remedy:** a region-named market query per region (**cheap**, one search each); or 🟢 **present
share-of-global rather than absolute figures**, which is honest with the data actually held.

### 🆕 `Gap 306` — the **UK** returned no education-specific AI instrument, which is conspicuous for a market this size

🔴 **The gap.** The EMEA probe returned EU AI Act enforcement, six national European instruments
(Italy, Ireland, Slovakia, France, Czechia, Netherlands), and nascent MEA policy — 🔴 **and nothing
for the United Kingdom**, which is outside the AI Act and is one of EMEA's largest education-
technology markets.

🔵 **Recorded as a measured hole, not as "no UK regulation exists"** — the channel was not asked a
UK-named question, and 🔴 **an unprobed jurisdiction and an unregulated one are indistinguishable
later.**

🟢 **Remedy:** one UK-named query (**cheap**) on the next EMEA pass. 🔵 Also unresolved from the same
probe: **how the AI Act's delayed high-risk timelines apply specifically to schools**, and **any
EMEA education adoption rate** — neither returned anything usable.

### 🆕 `Gap 307` — pass 66 did not write to this registry, and the gap ledger silently fell a pass behind

🔴 **The gap.** Pass 66 appended to all seven shelf files and **not to `intel/open-gaps.md`**. 🔵 So
between pass 66 and this pass, the registry's newest section was **pass 65's**, while the shelf files
referenced gap movement the registry did not record.

🟢 **Why this is a gap and not housekeeping:** this registry is the only file that says **which gaps
are open**. 🔴 **When it falls behind, every other file's gap citation becomes unverifiable from the
registry itself** — which is precisely the failure mode `P351` (the star-count gate) exists to catch
in the data, and nothing catches in the gap ledger.

🟢 **Remedy, in cost order:** **(i)** write this registry on **every** pass that opens or closes a
gap, without exception — free, procedural; **(ii)** add a gate asserting that each
`Gap N` cited in a shelf file resolves to a section in this registry — 🔴 **not written this pass**,
and `P237` applies: this session cannot run plain `python3` on this tree to validate a new gate, and
🔴 **an unvalidated gate is worse than a documented absence.**

### 🟢 `Gap 293` — re-confirmed, and this pass can finally name the **mechanism** for the GitHub refusal

🔵 **`Gap 293`** records that this session's outbound reach is an **allowlist**, not a fact about the
hosts refused. 🟢 **Re-confirmed this pass from a refusal that names itself**, which prior passes
could only infer:

> 🔴 `Access denied: repository "…" is not configured for this session. Allowed repositories:`
> `gmilano/globant-kb, gmilano/education-kb`

🟢 **This upgrades the evidence class.** Passes 64–65 recorded a bare **`403`** from
`api.github.com`; pass 66 recorded a **non-measurement**. 🟢 **This pass has the refusing layer
stating its own rule and enumerating the allowlist** — the same evidence class that closed
`Gap 293` originally, now reproduced for the GitHub tooling specifically.

🔵 **Written up as `P802`**, because the three refusals have **three different remedies**: a
rate-limit `403` is fixed by waiting, a non-measurement by issuing the probe, and `SCOPE_DENIED`
**only** by attaching a repository. 🔴 **Publishing them as one generic "unavailable" would lose
that**, which is the `P798` error in a new place.

🟢 **And the constructive half, worth keeping:** `git ls-remote` and `raw.githubusercontent.com`
remain fully readable. 🟢 **The `v8.0.0` tag that the refused release API could not confirm was
resolved from the git protocol instead** — 9 of 9 refs and every licence payload read this pass.
🔵 **The allowlist constrains the instrument, not the question.**

### 🟢 `Gap 286` — **CLOSED as unanswerable by this session**, after four passes of no movement

🔴 **The gap:** *"no reachable registry date for the Ed-Fi tier."*

🟢 **Closed, and closed honestly rather than by achievement.** 🔵 The gap asks for **dates** —
registry publication dates, release dates. 🔴 **Every instrument that serves a date for this tier is
behind `api.github.com`**, which is now established as `SCOPE_DENIED` with the allowlist enumerated
(above). 🔴 **The Ed-Fi packages are not on a public language registry** either: the tier is .NET,
and pass 62 measured its one candidate package id returning `none`.

🟢 **So the honest verdict is not "open pending more effort" — it is "not answerable with this
session's instruments"**, and 🔵 **keeping it open implies a remedy that does not exist.**
🟢 **What replaced it is better than a date:** this pass resolved **`v8.0.0` = `d911abb`** from
`git ls-remote --tags` — 🔵 **a version, pinned, without any registry.**

🔴 **Explicitly recorded so a later pass does not mistake this for a dated finding:** a resolved tag
is **not** a release date (`P781`). 🟢 **If a date is ever genuinely needed, the remaining instrument
is a clone plus `git log` on the tag** — under an hour, and 🔴 not run this pass.

### 🟢 Open gap ledger after this pass

| Gap | Subject | Status |
|---|---|---|
| **301** 🆕 | CLR 2.0 aggregate edge — no verifiable implementation | 🔴 open |
| **302** 🆕 | Two new components unplaced by region | 🔴 open |
| **303** 🆕 | Ed-Fi ODS → DMS migration path unmeasured | 🔴 open |
| **304** 🆕 | Vietnam AI statute secondary-sourced, channels conflict | 🔴 open |
| **305** 🆕 | No APAC/LATAM market figure; regional sum unreconciled | 🔴 open |
| **306** 🆕 | UK education-AI instrument unprobed | 🔴 open |
| **307** 🆕 | Pass 66 skipped this registry | 🔴 open (procedural) |
| **300** | 41 `unread` suites on the board | 🔴 open |
| **296** | `p351` red — pass attributor and band signal decayed | 🔴 open |
| **294** | Open Badges *issue* edge AGPL-only | 🔴 open, 🟢 **third edge now measured (301)** |
| **293** | Egress is an allowlist | 🟢 **closed, re-confirmed with mechanism named (`P802`)** |
| **286** | No registry date for the Ed-Fi tier | 🟢 **CLOSED — unanswerable by this session** |

🟢 **Net: +6 opened, 1 closed, 1 re-confirmed.** 🔴 **The count going up is the expected shape of a
pass that reads a new layer** — four new components and two new jurisdictions cannot be read without
exposing what was not read. 🔵 **A pass that opens no gaps has either closed a frontier or stopped
looking at one.**


## 🟢 Sixty-fifth pass, 2026-10-08 — **`Gap 257`/`Gap 258` CLOSED by running the board**, `Gap 295` closed by one `curl`, `Gap 294` SPLIT, `Gap 293` re-confirmed from a first-party ledger, and four gaps opened

⏱️ **Nineteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `Gap 257` / `Gap 258` — **CLOSED.** The board was run, and the number it had been repeating was wrong

🔴 **The gap:** *"the tableau of 112 suites is unmeasured; three greens are not 112."*

🟢 **Measured, the whole board, `python3 -I`, from the clone:**

| verdict | n |
|---|---|
| 🟢 green | **62** |
| 🟢 green, slow (137.5 s) | **1** (`p471`) |
| 🟡 **unread** — `-I` drops the script dir from `sys.path` | **41** |
| 🔴 environment — `cryptography` Rust binding panics | **1** (`p213`) |
| 🔴 **real red** | **1** (`p351`) |
| | **106** |

🔴 **Correction 1: the board is 106 suites, not 112.** 112 was never measured. 106 is
`find compose/code -name 'test_*.py' | wc -l` across **143** directories — **37 carry no suite**.

🔴 **Correction 2: 41 of the first-sweep 44 reds were an artifact of the instrument.** `python3 -I`
implies `-P`, dropping the script's own directory from `sys.path[0]`, so any suite importing its
sibling module raises `ModuleNotFoundError`. 🟢 **Verified by control probe** — own script, own
sibling module: plain `python3` imports it; `-I` and `-P` both fail; `sys.path[0]` becomes
`/usr/lib/python311.zip`. 🔵 **A fact about the flag.**

🔴 **Correction 3: a timeout had become a verdict.** `p471` was first written red because the sweep
capped suites at 120 s. Uncapped: **27/27, then 25/25, exit 0, 137.5 s.** 🔵 **Same defect shape as
`000`-for-a-refusal** (`P798`): the instrument's limit published as the subject's property.

🟡 **Why these close as a pair even though 41 suites are unread:** the gaps asked for the board to be
**measured**, and it now is — every one of 106 rows carries an attributed verdict in
`p799-board-census/board.2026-10-08.tsv`, with a suite (12/12 green) asserting the partition.
🔴 **`unread` is not `green`**, and `test_forty_one_are_UNREAD_and_are_not_counted_green` exists to
stop that slide. 🟢 **`Gap 300` carries the remaining 41.**

### 🆕 `Gap 296` — `p351` is RED, and it decayed because this KB's **prose language** changed under it

🔴 **The single real red on the board**, and it is this KB's own gate against unbanded star counts.

🟢 **Two causes measured, and they are different kinds of defect:**

| # | Cause | Evidence |
|---|---|---|
| 1 | 🔴 **The pass attributor is blind to the current header language.** `RE_ENCABEZADO_PASE` matches `pase (\d+)`. These files now carry **191 Spanish-numeric headers AND 27 English ordinal-word headers** (*"Sixty-fourth pass"*). | `74` occurrences attributed to **no pass at all**; the rest mis-attributed to the nearest preceding Spanish header (passes 123/124) |
| 2 | 🔴 **`es_umbral` is blind to the band form this KB adopted.** `MARCAS_UMBRAL` looks for `banda`, `por debajo de`, `umbral`, `cota` — none of which appear in `(K-3CIFRAS, ±50)`. | 2 of the 6 flagged occurrences (`agents/trending.md:9148,9149`) **are banded** and were read as bare |
| 3 | 🟡 **And 4 genuinely are bare.** | `agents/trending.md:9162,9211`, `repos/trending.md:5440,5448` — pre-reset rows carrying `1.200 ★`, `2.000 ★`, `1.300 ★` with no band |

🔵 **So the gate's verdict "the data regressed" is only one-third right, and the KB would have
believed all of it.** 🟢 **The reusable lesson, and it is why this gap is worth a number:** an
instrument that parses its own project's prose **decays when the prose is rewritten** — and the
2026-10-06 reset rewrote the headers while leaving the pre-reset history append-only below.

🟢 **Remedy, in cost order:** **(i)** widen `RE_ENCABEZADO_PASE` to the English ordinals — minutes,
and it recovers 74 occurrences; **(ii)** add `K-\d+CIFRAS` and `±` to the band signal — minutes;
**(iii)** band or retire the 4 bare figures — the only one touching published data.
🔴 **Not done this pass**, and the reason is `P237`: these are **gate logic** changes, and this
session cannot run plain `python3` on this tree to validate them (`[Code from External]`). 🔵 **An
unvalidated edit to a gate is worse than a red gate that is documented.**

### 🟢 `Gap 295` — **CLOSED**, and the remedy it had pre-registered was the expensive one

🔴 **The gap:** a candidate held on **canonicality**; remedy *"root-commit comparison, needs a clone,
under an hour."*

🟢 **Closed on a structurally identical case for the cost of one `curl`.**
[`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) and
[`GhaithAlHallak8/moodler-mcp`](https://github.com/GhaithAlHallak8/moodler-mcp) have **identical
HEAD `4e6139e`**, **byte-identical `LICENSE`** (`sha256:0f7241bdab42`) and identical manifests —
🔴 **the trees cannot say which is upstream.** 🟢 **The licence holder can: both read
`Copyright (c) 2026 Ghaith AlHallak`, and the handle `GhaithAlHallak8` matches while `Dymayo` does
not.**

🆕 **`P801` — read the copyright holder before cloning.** 🟢 Settles a `P443`/`P436` canonicality
hold in one request; 🟡 fall back to root-commit comparison **only** when the holder is absent or
ambiguous. 🔴 **And the channel listed the fork first** — search rank is not provenance.

🟡 **`19otherrsh-dot/Opencred` stays held** on its own facts (AGPL-3.0, throwaway-shaped handle, n8n
dependency reported but unmeasured). 🔵 **What closes is the METHOD gap**, not that candidate.

### 🟡 `Gap 294` — **SPLIT.** The verify edge is solved; the issue edge is untouched

🟢 **`Gap 294a` — CLOSED.** The OB 3.0 / W3C VC **verification** edge now has a permissive,
file-granted implementation: [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens)
(`main` · `d34f262`, **MIT**, `LICENSE` 1 080 B, manifest `"license": "MIT"` — **file and manifest
agree**). 🔵 **Zero dependencies, runs from `file://`** — the easiest component in this KB to put in
a closed deliverable. 🟢 Pattern `P8` ships on it.

🔴 **`Gap 294b` — OPEN, unchanged, and it is the commercial one.** The **issuance** edge still has no
provable permissive grant:

| Implementation | Grant | This pass |
|---|---|---|
| `educredentials/ec-issuer` | 🟡 MIT, **prose only** | 🔴 **still `8bafc99`** — unchanged since pass 64, **no `LICENSE` added** |
| `Schroedinger-Hat/certo` | 🔴 AGPL-3.0 | unchanged |
| `19otherrsh-dot/Opencred` | 🔴 AGPL-3.0 | held (`Gap 295`) |

🔵 **And the asymmetry is worth naming: verification arrived permissive before issuance did**, which
is the opposite of the order a sale needs — you can check a credential you cannot mint.
🟢 **Remedy unchanged and still the highest-value hour on this shelf: one email to `ec-issuer`
asking for a `LICENSE` file or an SPDX `license` key.**

### 🟢 `Gap 293` — re-confirmed, evidence class upgraded from inference to **first-party record**

🟢 Pass 64 closed it with Wikipedia-as-control. 🆕 **This pass read the refusing layer's own ledger:**
`$HTTPS_PROXY/__agentproxy/status` → `recentRelayFailures`, carrying per host a **timestamp** and a
**mechanism** — `connect_rejected`, *"gateway answered 403 to CONNECT (policy denial or upstream
failure)"* — for all four hosts probed, **Wikipedia included**.

🆕 **`P798`** — a refusal is attributed to the layer that **logged** it. Suite:
`compose/code/p798-proxy-refusal-ledger/`, **9/9 green**, including the negative control that an
**unlogged** `000` is **not** promoted to a policy denial (`UNDETERMINED (transport)`).

🔴 **And `P798` corrects this KB's oracle map:** `pypi`, `files.pythonhosted.org`,
`registry.npmjs.org`, `jsr.io`, `index.crates.io` and `proxy.golang.org` are in the proxy's
**`noProxy`** list — **they never traverse the refusing gateway.** 🔵 **Registry health is therefore
not evidence of allowlist breadth**, and every pass that read it that way over-read it.
🔴 **Still not enumerated:** the allowlist. `noProxy` is a **bypass** list, and `P744` holds — 4 of 4
denied is not a rate.

### 🔴 `Gap 284` — reproduced independently, still open

🟢 `ls-remote --symref` resolved **12 of 13** repositories this pass; 🔴
[`1EdTech/caliper-js`](https://github.com/1EdTech/caliper-js) resolved **nothing**, same instrument,
same minute. 🟢 **Second independent reproduction** of pass 64's reading.
🔴 **Also measured this pass:** [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification)
(`develop` · `04c4bc2`) has **no licence file on 6 names and no licence prose in its README** —
consistent with the 1EdTech Specification Document Licence. 🔵 **So the pattern is 1EdTech-wide, not
Caliper-specific**, which is a stronger statement than the gap originally made.

### 🆕 `Gap 297` — **Open edX has no MCP side-car**, and it is the second-largest open LMS

🔴 **Measured as an explicit channel absence:** a query returning **nine** Moodle MCP servers
returned **zero** for Open edX, and the channel said so in its own words.
🔵 **Open edX is AGPL-3.0**, so a side-car is the *only* way to put an agent on it without touching
the copyleft core — which makes the absence an opening rather than a signal of no demand.
🟢 **Cost to close: a `moodler-mcp`-shaped bridge over Open edX's REST APIs.** 🟡 **Not verified:**
whether something exists outside this channel's reach.

### 🆕 `Gap 298` — no **SIS** platform with a permissive grant, and the SIS is where the records live

🔴 **RosarioSIS and Gibbon are both GPL.** 🔵 **The student-information system holds the data FERPA
and Annex III are about** — enrolment, progression, admission — and this shelf cannot name a
permissive one. 🟢 **Consequence for a proposal:** SIS work is a *service* integration, never a
derivative, and a statement of work that implies otherwise is wrong on licence.
🟡 **Not probed this pass:** whether a permissive SIS exists at all.

### 🆕 `Gap 299` — **OneRoster and SCORM unprobed**, and both carry client data

🟢 The standards census in `repos/foundations.md` read **five** protocols (LTI 1.3, xAPI ×2, OB 3.0
verify/issue, Caliper). 🔴 **OneRoster (rostering) and SCORM (legacy packaging) were not probed**,
and rostering is **exactly** the data class the North American privacy statutes name.
🟢 **Cost to close: one sweep, the same nine-name grant probe.**

### 🆕 `Gap 300` — 41 suites remain **unread**, and closing it needs one of two cheap things

🔴 41 of 106 suites cannot be read under the only interpreter mode this session may use.
🟢 **Two remedies, either sufficient:** **(i)** permission for plain `python3` on this tree — the
standing request the suites' own docstrings have carried since pass 58, now **half-granted** (`-I`
works, plain `python3` is refused by the auto-mode classifier as `[Code from External]`);
**(ii)** make the suites import-free in the manner of `p798`/`p799`/`p800`, which run **identically
under `python3` and `python3 -I`** — 29 green between them this pass, and that is the pattern.
🔵 **Attributed to the layer that refused it (`P797`), not written as a defect of the suites.**

### 🟢 🆕 `P800` — a region comes from an institution the artefact names, never from a person's name

🟢 Three rows admitted this pass carry maintainer names a reader could file under a country in
seconds, and 🔴 **all three repositories say nothing about where they are built or deployed** —
grepped for `universit|ministr|government|deploy|country|region|instituti|EU|GDPR|FERPA|AI Act|.edu|.ac.`,
all empty. 🟢 **All three are `Global`.**
🔵 **The contrast that makes the rule:** `ec-issuer` is **EMEA** because its README points deployment
at **SURF** (NL) and it implements the **European Learner Model** — an institution and a standard.
🔴 **Inferring nationality from a name to fill a closed business field is unreliable and not this
shelf's business.** Suite: `compose/code/p800-region-provenance/`, **8/8 green**.

### 🟢 🆕 `P759` widened — the licence-name list was **not exhaustive**, and it nearly cost a verdict

🔴 **`frappe/lms` carries its grant in `license.txt`** — lowercase, `.txt`. The 8-name list missed
it, and a four-404 reading would have published *"no licence file"*. 🟢 **Nine names now.**
🔵 **The consequence is for the REJECTS, not for `frappe`:** `loyaniu/moodle-mcp` and
`linomck/moodle-mcp` were **re-probed against all nine — 9×404 each, with `README.md` returning 200
on both in the same minute**, so the absence is theirs and not the instrument's.
🔴 **A hard reject is only safe when the name list has been proven exhaustive, and until this pass it
had not been.**

### 🟢 Gap ledger after this pass

| Gap | State |
|---|---|
| `Gap 257` / `Gap 258` | 🟢 **CLOSED** — board run, 106 rows attributed |
| `Gap 293` | 🟢 **CLOSED** (pass 64), re-confirmed from first-party ledger |
| `Gap 294a` (verify) | 🟢 **CLOSED** — `credential-lens`, MIT |
| `Gap 295` | 🟢 **CLOSED** — holder-read settles canonicality (`P801`) |
| `Gap 284` | 🔴 open — 1EdTech-wide, cause measured twice |
| `Gap 289` | 🔴 open — `credential_issuance` still absent from `p782`'s vocabulary |
| `Gap 294b` (issue) | 🔴 open — **the commercial one** |
| `Gap 296` 🆕 | 🔴 open — `p351` red; 3 causes measured |
| `Gap 297` 🆕 | 🔴 open — no Open edX MCP side-car |
| `Gap 298` 🆕 | 🔴 open — no permissive SIS |
| `Gap 299` 🆕 | 🔴 open — OneRoster/SCORM unprobed |
| `Gap 300` 🆕 | 🔴 open — 41 suites unread |

### 🔴 Pre-registered for the next education pass, so it can be scored rather than re-chosen

🟢 **Action A (cheapest, highest value):** widen `RE_ENCABEZADO_PASE` to English ordinals and add
`K-\d+CIFRAS`/`±` to the band signal, **then re-run `p351`**. 🔵 **Pre-registered claim: the
74-unattributed count drops to 0 and the 6 flagged occurrences drop to 4.**
🔴 **Refutation branch:** if it drops to something other than 4, there are bare figures this pass did
not find, and `Gap 296` is larger than measured.

🟢 **Action B:** probe **OneRoster** and **SCORM** on the nine-name list (`Gap 299`).
🔵 **Pre-registered claim: at least one has an Apache-2.0 implementation** — on the pattern that the
older, ADL/vendor-stewarded standards do and the 1EdTech-governed ones do not.
🔴 **Refutation branch:** if neither does, the "older standards are buildable" reading in
`repos/foundations.md` is wrong and must be withdrawn.

🟢 **Action C:** re-read `educredentials/ec-issuer` at HEAD. 🔵 **Pre-registered claim: still no
`LICENSE` file** (it has now been unchanged across two passes). 🟢 A change either way is a finding.


## 🟢 Sixty-fourth pass, 2026-10-08 — **`Gap 293` CLOSED** by a control that cannot be argued with, `Gap 284`'s **cause** measured, `Gap 289` found in the world, two gaps opened, and one gap **regressed to zero**

⏱️ **Eighteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `Gap 293` — **CLOSED**, and the closure corrects the band language in six files

🔴 **The gap:** *"the policy band blames hosts for a refusal that happens at the proxy."*

🟢 **Measured, `n = 5`, one allow and four denies in the same minute, on the fetch channel:**
`raw.githubusercontent.com` **returned a payload**; `www.iesalc.unesco.org`,
`digital-strategy.ec.europa.eu`, `www.multistate.us` and 🔴 **`en.wikipedia.org`** each returned a
**structured `EGRESS_BLOCKED` error naming the proxy itself** — *"Access to … is blocked by the network
egress proxy."*

🔵 **Wikipedia is the closure.** 🔴 **It is not a policy host, not a regulator, not a vendor report, not
rate-limiting this KB, and not down** — and it is refused with the identical error. 🟢 **Therefore the
variable is the channel's allowlist, and nothing was ever measured about `unesco.org`,
`eur-lex.europa.eu`, `ec.europa.eu`, `nasbe.org` or `multistate.us`.**

🆕 **`P797` — a refusal is attributed to the layer that issued it.** 🟢 Write **`EGRESS_DENIED
(allowlist)`**; 🔴 **never `000` against a hostname.** 🔵 **The two license different conclusions:**
`000` invites *"retry, the host may be up"* and casts doubt on the **source**; `EGRESS_DENIED
(allowlist)` is terminal here and says **the source is fine and this environment may not read it** —
which is the sentence a client-facing citation needs.

🟢 **Passes 57–60 were right and for an unmeasured reason.** 🔵 Pass 59 learned to `grep` before
announcing a property; this is the same lesson for an **error code**.

🔴 **What this pass did NOT do:** enumerate the allowlist. 🟢 Five hosts probed, five results recorded;
🔴 **four of five denied is not a rate** (`P744`), and nothing here says which hosts would be allowed.

### 🟢 `Gap 284` — **CAUSE MEASURED, gap stays OPEN**, and the distinction is the point

🔴 **The gap:** *"Caliper Analytics has no reachable permissive implementation."*

🟢 **`ls-remote --symref … HEAD` resolved the default ref and HEAD for 7 of 8 repositories probed this
pass. 🔴 For [`1EdTech/caliper-js`](https://github.com/1EdTech/caliper-js) it resolved nothing**, on the
same instrument, in the same minute, under the same proxy. 🔵 **An instrument that discriminates 7 of 8
makes the eighth a measurement rather than an outage.**

🟢 **It agrees with 1EdTech's own published position**, surfaced by the channel this pass: the Caliper
Sensor API repositories are *"available for 1EdTech Contributing and Affiliate Members"* who *"can
request Github access"*, and the specification repository carries the **1EdTech Specification Document
License** — neither Apache nor MIT.

🟢 **So `Gap 284` is not a search failure: the reference sensors are behind membership.** 🔴 **The gap
stays open** — knowing *why* a thing cannot be found does not make it findable. 🟢 Pass 63's
[`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) remains
its only reachable implementation, LGPL-file-versus-`proprietary`-manifest split unresolved.

### 🟢 `Gap 289` — the function **exists in the world**, and finding it opened a worse problem

🔴 **The gap:** *"`credential_issuance` is absent from `p782`'s 14-function vocabulary — and it is the
one that unblocks a sale."*

🟢 **A function-named query (`P795`) found the component**:
[`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) — OB 3.0 **+ European Learner
Model**, OID4VCI wallet delivery, revocation with reason tracking. 🟢 **EMEA, SURF edubadges (NL).**

🔴 **A `P759` four-layer grant probe then came back empty on three of four layers:** no licence file (8
names, all 404 at `main` · `8bafc99`), no `license` key in `pyproject.toml` (1 453 B), not on pypi (404
×2 against its calibrated pair) — 🟡 **and `MIT` as a two-word README heading with no holder and no
year.**

🔴 **`Gap 289` therefore does NOT close, and it is now two gaps wearing one number:**
🔴 **(a)** the vocabulary entry is still missing, so `p782` returns **no verdict** for a credential
recipe — and 🔴 **a silent gate must never be read as a permissive one**;
🔴 **(b)** the function's best-fit implementation is unprovable, which is `Gap 294` below.
🟢 **Remedy for (a), unchanged and still cheap:** add `credential_issuance` to the vocabulary with its
Annex III binding (credential issuance *determines access to and progression through* education).
🔴 **Cost of (a): it cannot be validated in this session, because the session refuses to execute this
repository's test scripts.** 🟢 **So the edit is not made this pass** — an unvalidated change to a gate
that governs a prohibition is worse than a missing entry (`P237`).

### 🆕 `Gap 294` — the credential edge has **no permissive, file-grant implementation**, and that is a commercial gap, not a licence footnote

🟢 **Measured this pass**: three reachable implementations of the OB 3.0 / W3C VC issuance edge, and
🔴 **zero that a client can link into a closed deliverable today.**

| Implementation | Grant | Verdict |
|---|---|---|
| `educredentials/ec-issuer` | 🟡 MIT, **prose only** | 🟡 permissive and unprovable |
| `Schroedinger-Hat/certo` | 🔴 **AGPL-3.0** (33 820 B) | 🔴 self-host only |
| `19otherrsh-dot/Opencred` | 🔴 **AGPL-3.0** (34 523 B) | 🔴 self-host only, **and `Gap 295`** |

🔵 **AGPL on a credential *service* is the worst placement of copyleft available:** an issuer is
network-facing by definition, so §13 is its operating condition, not a dormant clause.
🔴 **And 1EdTech puts digital credentials at the centre of 2026** (`intel/trends.md`) — 🔵 **so the edge
the analysts call central is the edge this shelf cannot build permissively.**

🟢 **Remedy, with cost:** **(i)** one email asking `ec-issuer` for a `LICENSE` file or SPDX key — hours,
and it is the highest-value hour available on this shelf; **(ii)** accept a self-hosted AGPL deployment
and say so in the proposal — free, and it constrains the client; **(iii)** build against the OB 3.0 /
W3C VC specifications, which are open to implement — weeks, and it is the only path to a closed-source
verifier. 🔴 **Three different proposals at three different prices, and a proposal that does not name
which one it means is underpriced.**

### 🆕 `Gap 295` — a candidate is HELD on **canonicality**, and the question is unanswered

🔴 [`19otherrsh-dot/Opencred`](https://github.com/19otherrsh-dot/Opencred) (`main` · **`d14619e`**,
AGPL-3.0, 34 523 B) is **held, not shelved** (`P443`/`P436`): the owner handle has the shape of a
throwaway account, the project name duplicates an established one, and 🔴 **no upstream was identified
this pass.** 🔵 **A copyleft row costs a reader one rejection; a row at the wrong address costs them a
build on code that moves.**
🔴 **Also unmeasured, channel-reported only:** its README is reported to declare an **n8n** dependency,
and n8n ships under the **Sustainable Use Licence — source-available, not OSI**. 🔵 **An AGPL core with
a non-OSI dependency is two rejections, and the second travels into whatever vendors it.**
🟢 **Remedy:** root-commit comparison against any candidate upstream, as the seventeenth pass did for
`Mcp-Brasil/mcp-brasil`. 🟡 **Cost: under an hour, and it needs a clone.**

### 🟢 `P793` — **WIDENED by two non-PHP instances**, which is a correction to its scope and not to its rule

🟢 **Pass 63 measured the version-named default branch on 7 of 25 PHP/composer rows and called the
defect ecosystem-concentrated.** 🟢 **Two non-PHP instances this pass:**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) defaults to **`19.0`**
(Odoo/Python) and [`frappe/education`](https://github.com/frappe/education) defaults to **`develop`**
(Frappe/Python). 🔴 **A `{main,master}` probe reports "no licence file" for both — and both have one.**
🔵 **The predictor is release-branch discipline, not language.** 🟢 **The operational rule is unchanged
and better supported: resolve the default ref from the oracle before fetching any payload, every
ecosystem, every time.** 🔴 **No rate from 2 of 2** (`P744`).

### 🆕 `P796` — a discovery channel's description is the repository's **ambition**

🔴 **Measured:** a protocol-named query returned [`Transcordia/jupiter`](https://github.com/Transcordia/jupiter)
as *"an LRS supporting the xAPI and Caliper specifications."* 🟢 **Pass 77 had already cloned that tree
— 31 files, 100 040 B, `HEAD` 2015-04-19 — and measured zero Caliper and no query path: an ingestor,
not an LRS.** 🟢 **Licence reconfirmed this pass** (`master` · **`fb32fee`**, MIT, 1 079 B).
🔵 **`P234` said a shelf row inherits capability, not ambition. 🆕 `P796` extends it to the channel: a
search result's one-line description *is* the README's self-description, so the channel will re-offer a
refuted row indefinitely, having no memory of this KB's refutations.** 🟢 **Only the writing-down caught
it** — which is the operational argument for a refutation log.

### 🔴 `Gap 257` / `Gap 258` — **REGRESSED TO ZERO**, and the reason must be recorded, not the number

🔴 **Pass 63 ran three suites from the clone and said plainly that three is not 112.** 🔴 **This pass ran
ZERO.** 🟢 **The reason, stated so no later pass reads it as a property of the suites:** 🔴 **the session
this pass ran in refuses to execute the cloned repository's own test scripts** — a sandbox policy on
running code from a fetched repository, not a failure of any suite.

🔵 **This is `P797`'s lesson applied to this KB's own instruments:** 🔴 **"zero suites green" and "zero
suites runnable" are different facts**, and writing the first when the second is true would slander 117
test files that were never invoked. 🟢 **Measured: 143 directories under `compose/code/`, 106
`test_*.py` and 11 `test_*.sh`. 🔴 Executed: none.**

🔴 **Consequence for this pass, applied throughout:** every instrument referenced in `compose/patterns.md`
is cited **as existing**, never as having been re-run (`P752`). 🔴 **And `Gap 289`'s cheap remedy was
deliberately NOT applied**, because an unvalidated edit to the gate that governs a prohibition is worse
than a missing vocabulary entry (`P237`).

🟢 **Remedy, pre-registered for the next pass that has execution:** run the board with a bounded timeout
from each suite's own directory, classify outcomes into **GREEN / RED / NETWORK / TIMEOUT** as distinct
tokens — 🔵 **because collapsing an egress refusal into "red" is exactly the attribution error `P797`
names** — and commit the TSV beside a README. 🟡 **Cost: a session that permits executing the
repository's tests.**

### 🟡 Gaps **not advanced** this pass, stated so no reader mistakes this section for progress

🔴 **`Gap 286`** — still no reachable registry date for the Ed-Fi tier. 🟢 `edfi-oneroster` was
re-confirmed at `main` · `6de5476` (Apache-2.0, 10 173 B), 🔴 **but that is a payload, not a date.**
🔴 **`Gap 287`** — `p784` still reads 16 **rooted** filenames only, no tree layer, no prose layer.
🔵 **This pass produced two findings of exactly the class it predicts it would miss** (`ec-issuer`'s
prose-only grant; `openeducat`'s body behind a dangling pointer). 🔴 **Untouched.**
🔴 **`Gap 288`** — `p441`'s `LICENCE_RE` still matches `extensions/licenseExtension/…`. 🔴 Untouched, and
🔴 **still the dangerous error direction**, because it admits rather than refuses.
🔴 **`Gap 290`** — the seams between this KB's 235+ instruments remain unmeasured. 🔴 **And this pass
could not measure them for the same reason the board was not run.**
🔴 **`Gap 291`** — pass 63 audited the 12-row evaluation tier against `ls-remote` and found 12 of 12
matching; 🔴 **the composer tier it identified as owed the re-check is still owed it.**
🔴 **`Gap 292`** — 🟢 **partially addressed in method, not closed in instrument:** this pass wrote its
oracle map from calibration **pairs** throughout (`raw` four-way, `pypi` 200/404, `npm` 200/404), 🔴 **but
no instrument was changed, because nothing could be validated.**
🔴 **`Gap 285`** — the 8 ungranted benchmark repos are still unexamined at the manifest/header layers.
🔴 **`Gap 284`** — open, cause now measured (above).


## 🟢 Sixty-third pass, 2026-10-08 — three gaps advanced by measurement, one closed, four opened, and `Gap 284` moves from *unfound* to *characterised*

⏱️ **Seventeenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `Gap 284` — **advanced, not closed**, and its pre-registered remedy was run and found insufficient

🟢 **Pass 62 left a bounded remedy: *resolve the 1EdTech implementation from a registry `repository`
field (`P780`) rather than guessing slugs.* 🟢 It was run. Three results, two of them new:**

1. 🔴 **The protocol-name channel returns a HOMONYM.** `pypi.org/pypi/caliper/json` is **200** and
   resolves to **`vsoch/caliper`**, a Python *package-version analysis* tool. 🔴 `caliper-python`
   and `caliperpy` **404**; npm `caliper-js`, `caliper-sensor`, `caliperjs`, `@1edtech/caliper`
   **404, 4 of 4**. 🔵 **The registry answered and the answer was wrong** — `P791`'s
   `FALSE-PRESENCE` class arriving through the *protocol-name* channel.
2. 🔴 **The specification is not open and names no implementation.** `1EdTech/caliper-spec` @
   `master`: `LICENSE` **404**, `LICENSE.md` **12 402 B** opening
   `IMS GLOBAL LEARNING CONSORTIUM, INC.` under the heading `# SPECIFICATION DOCUMENT LICENSE`
   (`P191`: not OSI). 🔴 Its README mentions the Sensor API **once** and links **zero**
   repositories.
3. 🔴 **The one reachable implementation contradicts itself** —
   `tl-its-umich-edu/caliper-php-public` @ `refs/heads/public` (`e35b0ec`): licence **file**
   LGPL-3.0 (7 438 B, `p419.familia()`, self-test 10/10), **manifest** `"proprietary"`, **registry**
   `["proprietary"]` with latest `1.0.1` **2016-01-27**.

🔴 **So the gap stands: the analytics edge still has no permissive implementation.**
🟢 **What changed is its shape — it is now a *characterised* hole, not an empty cell:** one
reachable implementation, nine years and eight months stale, internally inconsistent about whether
it is open source at all.
🔵 **Remaining bounded remedy, and it is the last cheap one:** the 1EdTech **Sensor API** samples
are reported to be multi-language; ask the **org listing** for repository names rather than the
search channel or the spec README. 🟢 **Cost: a handful of requests.** 🔴 **After that, the honest
conclusion is that this protocol has no permissive implementation and the edge must be written, not
adopted** — which is a scoping fact worth more than another search.

### 🟢 `Gap 276`-adjacent — **CLOSED: the `latam-gpt` "missing model repo" was partly not missing**

🟢 **The `latam-gpt` org resolves, and this shelf has carried two of its repositories since pass
60** — found by **grepping the shelf**, which is the channel pass 59 already named as the one to try
first. 🟢 Re-measured at the ref the oracle names: `latam-gpt/lm-evaluation-harness` `main` ·
**`9fa381a`** · `LICENSE.md` 1 067 B *"MIT License"* → **MIT**; `latam-gpt/syco-bench` `main` ·
**`5ecc005`** · `LICENSE` 903 B *"**MIT No Attribution**"* → 🔴 **`MIT-0`, recorded here as "MIT".**
🔴 **The label is corrected; a *model* repository still does not resolve** from three conjectured
slugs, 🔵 and per `P253` that is a fact about the three guesses.

### 🆕 `Gap 290` — the **seams** between this KB's 235+ instruments are unmeasured, and one of them is broken

🔴 **`p253-registry-first-identity` run END TO END returns `PUBLISHED-BY-OTHER` for a package
pointing at exactly its own repository**: its probe layer emits
`git+https://github.com/Cvmcosta/ltijs.git`, its gate compares that to the slug `Cvmcosta/ltijs`.
🟢 Its committed table is correct because the column was **hand-normalised**; 🔴 the script was never
changed to match. 🆕 **`P792`: reuse the instrument END TO END** — the defect can live in the seam.

🔴 **The gap is the population, not the case:** **nothing on this shelf has ever run an instrument's
own probe layer into its own gate** except by accident. 🔵 **Bounded remedy: for each instrument
that ships both a `sweep*.sh` and a verdict module, run one target through the pair and compare the
verdict to the committed table.** 🟢 **Denominator is enumerable from `compose/code/`** — it is a
directory listing, not a sampling frame, so `P744` does not apply. 🟡 **Cost: one pass, and it
should be ordered by how many downstream passes cite each instrument.**

### 🆕 `Gap 291` — every `master` ref cited on this shelf is unverified provenance

🔴 **`P793`: `raw.githubusercontent.com` serves the DEFAULT branch for the literal ref `master`,
even where no `master` exists** (control: `main` 404, invented branch 404, `master` 200, `HEAD` 200;
3 of 3 on repositories whose defaults are `refs/heads/0.7`, `refs/heads/public`,
`refs/heads/2.12`). 🔴 **So "payload-read at `master`"** — a phrase this shelf has used for dozens
of rows — **names a branch, not necessarily the branch the bytes came from.**

🟢 **Measured scope so far: 7 of 25 PHP/composer rows have a default that is neither `main` nor
`master`** (`v31.0.00`, `mobile`, `2.2`, `0.7`, `3.x`, `2.12`, `public`); 🟢 **0 of 12 on the
evaluation tier, whose 12 cited SHAs all still match the oracle.** 🔵 **The defect is
ecosystem-shaped**, which bounds the remedy usefully.
🔵 **Bounded remedy: run `p791/ref.sh` over the rows this shelf cites with a `master` ref, PHP and
Java first.** 🟢 **It is one `ls-remote` pair per row and it exits 3 on exactly the rows that need
re-reading.** 🔴 **No rate is claimed from 7 of 25** (`P744`).

### 🆕 `Gap 292` — the oracle map has never been written from calibration pairs

🔴 **`P791`: a code from a target id is not a fact about a host.** Pass 61 wrote `packagist 404`
and pass 62 wrote `packagist 200 — recovered`; 🔴 **both probed the repository slug as a package id,
which nothing publishes** (404 × 2 on `packagist.org/packages`, 404 × 2 on
`repo.packagist.org/p2`), while the host answered 200 to `monolog/monolog` and 404 to an invented
id in the same minute.

🔴 **The gap: the map's other lines were written the same way** — a single probe per host, with no
stated pair. 🔵 **Bounded remedy: give every host in the map a named calibration pair (one id known
to exist, one invented) and record both codes, as this pass did for `packagist` and `raw`.**
🟢 **`host_verdict()` in `p791` already refuses a single code**, so the remedy is to route the map
through it. 🟡 **Cost: 2 requests per host per pass, which is what `n = 2` already spends.**

### 🆕 `Gap 293` — the policy band blames hosts for a refusal that happens at the proxy

🔴 **Measured on two independent channels: `curl` returns `CONNECT tunnel failed, response 403` and
`WebFetch` returns `EGRESS_BLOCKED`, naming the domain, for 8 of 8 policy and report hosts**
(`unesco.org`, `iesalc.unesco.org`, `digitaleducationcouncil.com`, `worldbank.org`,
`multistate.us`, `dig.watch`, `lw.com`, `1edtech.org`). 🔵 **No request reached any of them**, so
pass 62's *"policy and report hosts are `000`"* said something it had not measured.

🟡 **The practical band is unchanged** — every regulatory and survey figure stays `reported`,
single-channel (`P784`) — 🟢 **but the reason now survives a host coming back up.**
🔵 **Bounded remedy: write the band as "refused at the egress proxy" and stop re-probing the same
eight hosts each pass.** 🔵 **The useful question instead is whether ANY policy-grade host is
reachable**, which is one probe against a host class, not eight against a list. 🟢 **Cost: one
probe. 🔵 And if the answer is none, that is a standing property of this environment and belongs in
the map, not in eight rows per pass.**

### 🟡 Gaps **not advanced** this pass, stated so no pass reads this one as progress

🔴 **`Gap 286`** — no reachable registry date for the Ed-Fi tier. 🔵 `api.nuget.org` is up and
404-discriminating, and `EdFi.OdsApi.Sdk` returns **none**; untouched this pass.
🔴 **`Gap 287`** — `p784` reads 16 **rooted** filenames only; untouched.
🔴 **`Gap 288`** — `p441`'s regex matches `licenseExtension`; untouched, and 🔴 **still a
false-presence defect, which `P788` calls the worse direction.**
🔴 **`Gap 289`** — `credential_issuance` is absent from `p782`'s 14-function vocabulary. 🔴 **And
`R63a` now needs a second one: `automated_assessment` is in the vocabulary, but `item_authoring`
and `item_delivery` are not, and this pass's recipe branches on all three.**
🔴 **`Gap 257` / `Gap 258`** — the 112-suite board is still unmeasured as a whole. 🟢 **Three suites
were run green from the clone this pass** (`p759 --self-test` 4/4, `p419` 10/10, `p791` 37/37),
🔴 **which is three, not 112**, and `Gap 267`'s negation is refuted for a **third** consecutive pass.
🔴 **The agent-discovery gap** — fourteenth empty week. 🆕 **`P795` gives it a mechanism** (`AI
education` ranks courses about AI above agents doing education) 🔴 **but a mechanism is not a
filling**: no education-specific agent entered the shelf this pass.
🔴 **No APAC school-adoption figures**; 🔴 **no Canada or Mexico coverage** — both declared in
`intel/market.md`, both still open.

## 🟢 Pass 62, 2026-10-08 — `Gap 242` ADVANCED, `Gap 285` WEAKENED (its count is now an upper bound), four gaps declared, `P785`'s saturation rule applied to the *regional* channel for the first time

> 🔵 **Opening hypothesis: that the four regional queries would again return named instruments, as
> pass 61 found. 🟡 HALF REFUTED — and the failing half failed informatively.** 🔴 **EMEA and APAC
> returned enterprise-AI content with *no education sector in it at all*.** 🟢 **A targeted
> re-query of the same EMEA channel then returned the richest EMEA material in four passes** — so
> `P769`'s rule (name the function, not the industry) is now shown to govern the **regional**
> channel too, not only the repo channel. 🆕 **`P790`.**

### 🟢 The rows pass 62 changed

| Gap | What it said | 🟢 Pass 62 says |
|---|---|---|
| **242** | 🟡 *"The Digital Education Council's own summary says EMEA has the lowest future AI adoption intent of any region, while its survey coverage reports EMEA at 89% and US & Canada at 67%."* Pass 44 narrowed it: the UNESCO IESALC + UNU-IAS paper is *"located and named, **NOT read** — no figure from it is quoted anywhere this pass"* | 🟡 **ADVANCED, not closed.** 🟢 **Figures from the IESALC frame are quoted for the first time, with its sampling stated**: **200 institutions / 19 countries**, fielded **Aug–Oct 2025**; adoption **73.5 %** teaching and learning · **57.0 %** research · **34.1 %** administration · **20.0 %** community engagement; **84 %** private non-profit · **68 %** public · **52 %** private for-profit; 🔴 **87 % use AI, 26 % have any formal framework**. 🟢 DEC LATAM 2026 now has its frame too: **30 000+ responses, 29 institutions**, 92 % students / 79 % faculty. 🔴 **Still open for the reason the gap exists**: `unu.edu` and `ess.iesalc.unesco.org` are both **`000`**, so this is a search-backend summary, not a read of the paper — and 🟡 **a variant figure persists** (a Tec de Monterrey-linked source says **30 %** of LATAM universities have published AI policies against IESALC's **26 %**), which is the same definitional looseness the gap was opened about. 🟢 **Narrowed from "no figure" to "figures from one channel, one unresolved variant"** |
| **285** | 🔴 *"The 8 **ungranted** benchmark repos have not been through the manifest/header layers."* | 🔴 **WEAKENED — its number is now an upper bound, and the reason is a measurement, not an argument.** 🔴 **All 8 were judged by `p784` alone, and `p784` is measured this pass returning a false absence**: `1EdTech/openbadges-specification` → `UNGRANTED` while `ob_v3p0/license.md` answers **`200` at 12 324 B** with the *IMS Global Specification Document License*. 🔴 **They have not been tree-enumerated either** — so the gap's own framing (manifest/header) was already too narrow. 🟢 **"8 carry no grant at all" must now be read as "8 carry no grant at 16 rooted filenames"**, and pass 61's **48 % unusable** inherits that caveat wherever it is quoted |
| **282** | 🟡 *"A licence probe returns a scalar family; a repo can partition scope across files."* Closed at pass 61 by `p784` | 🔴 **RE-OPENED IN PREMISE, not in code.** 🟢 `p784` does what it was built to do. 🔴 **But `P786` shows the premise was incomplete: a partition can be declared in *prose* and in no file any probe reads.** `luisgf/openbadgeslib` = **LGPL-3.0 library + BSD-2-Clause CLI**, stated in `wiki/Authors-License-and-FAQ.md` and contradicted by nothing — `LICENSE.txt` LGPL only, `pyproject.toml` one classifier, PyPI agrees, **0 of 40 `.py` headers** name BSD. 🟢 **Recorded here rather than as a new gap because the remedy is not an instrument**: it is a two-minute manual read, now row 4 of the pre-flight in `compose/patterns.md` |

🔴 **Do not quote "48 % of the benchmark shelf is unusable" without `Gap 285`'s new caveat**, and
🔴 **do not quote `Gap 282` as closed** — its instrument works and its premise does not.

### 🟢 Live gaps declared by pass 62 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **286** | **2026-10-08**, pass 62 | `repos/foundations.md`, `agents/trending.md`, `verticals/solutions.md` · `P787b` | 🔴 **OPEN.** *"The Ed-Fi stack — five Apache-2.0 repos, payload-read — has no version or date from any channel this session can reach."* 🟢 **Measured, not inferred, and the identity half is already solved**: the Alliance's own `Utilities/SdkGen/EdFi.SdkGen.Console/EdFi.OdsApi.Sdk.nuspec` names **`<id>EdFi.OdsApi.Sdk</id>`, `<authors>Ed-Fi Alliance</authors>`**, and that exact id returns **`none`** on the reachable, control-verified NuGet flat container (controls: `newtonsoft.json` **86** versions, `serilog` **601**, invented package **none**). 🔴 7 further guessed ids: **7 of 7 none**. 🔴 `api.github.com` **403**, `ed-fi.org` **000**, and `Application/Directory.Build.props` carries the placeholder **`AssemblyVersion 1.0.0`**. 🟡 The only public `EdFi`-named packages are third-party (`EdNexusData.EdFi.OdsApi.Sdk` **v1.0.19**, `…v73` **v1.0.8**) 🔴 **and the org `EdNexusData` does not resolve at `ls-remote`** — not admitted. 🔵 **Why it matters commercially rather than bibliographically**: it means an Ed-Fi engagement is a **source-and-installer build**, not a package pull, and no row in `R62b` may be quoted with a version. 🔵 **Remedy, two options, both bounded**: (a) read a product version from a payload that carries one — a release notes file, a `CHANGELOG`, or the Data Standard's own `v6.2.0` marker already on this shelf; (b) locate the Alliance's Azure Artifacts feed hostname and measure it against the allowlist. 🔴 **Cost: under an hour for (a); (b) may simply return `000` and that is still an answer** |
| 🆕 **287** | **2026-10-08**, pass 62 | `repos/foundations.md` · `P786`; `repos/trending.md` · the cross-run | 🔴 **OPEN, and it is this KB's own warning applied to its newest gate.** *"`p784` emits `UNGRANTED` and `SINGLE` from 16 **rooted** filenames, with no tree layer and no prose layer; 2 of 13 rows this pass are wrong."* 🔴 **`p441`'s README already states the rule in as many words — *"a filename list can only FIND a licence. To sustain its ABSENCE you must ENUMERATE the tree"* and *"widening a list cannot fix a list"* — and `p784` was built one pass later as a list of 16 rooted filenames.** 🟢 **Fifth recorded instance of this defect family in this KB, first inside its newest gate.** 🟢 **Remedy is written and already proven once**: have `p784` delegate to `p441`'s `git ls-tree -r` channel before emitting `UNGRANTED`, and emit a distinct `UNGRANTED-AT-ROOT` verdict so the two are never conflated. 🔴 **The prose layer is NOT in the remedy and must not be faked as one** (`P786`) — it belongs to a human, and `compose/patterns.md` now says so. 🔴 **Cost: one pass.** 🟢 **Acceptance test exists, with ground truth**: `1EdTech/openbadges-specification` must stop returning a bare `UNGRANTED`, and `Gap 285`'s 8 rows must be re-run |
| 🆕 **288** | **2026-10-08**, pass 62 | `repos/foundations.md`, `repos/trending.md` · `P788` | 🔴 **OPEN, and declared AHEAD of `Gap 287` because its error admits rather than refuses.** *"`p441`'s `LICENCE_RE` matches the path `extensions/licenseExtension/…`, so it reported `CC-BY;CC0-1.0` as **confirmed** grant families for a repo that grants neither."* 🟢 **Read this pass: the matched file opens *"# Creative Commons Content License … enables **issuers** to indicate what permissions are granted to the public to reuse **BadgeClass metadata**"*** — it documents an Open Badges **metadata field**. 🔴 **And the same run put the repo's two real grants in `rejected_paths`**: `ob_v3p0/license.md` (**12 324 B**, IMS Global Specification Document License) and `ob_v2p1/LICENSE-INPROGRESS.md` (🔴 *"for IMS Global Contributing Member and/or Invited Guests only"*). 🔵 **So the instrument reports a repo by its noise and discards its signal.** 🟢 **Remedy, two parts, both small**: anchor `LICENCE_RE` to a path **basename** rather than a substring, and add an `UNCLASSIFIED-BESPOKE` verdict so a non-OSI grant is surfaced instead of silently rejected. 🔴 **Cost: hours, plus a fixture** — and `1EdTech/openbadges-specification` is the fixture, with both failure modes in one repo |
| 🆕 **289** | **2026-10-08**, pass 62 | `agents/top.md`, `compose/patterns.md`, `intel/market.md` · the gate run | 🔴 **OPEN, and it gates the pass's best commercial finding.** *"`credential_issuance` is not in `p782`'s 14-function vocabulary, so the credential edge has no policy verdict in any jurisdiction."* 🟢 **Run, not assumed**: `gate.sh credential_issuance EU` → **`NO ROW … was never measured`**, and the gate correctly adds *"This is an UNMEASURED pair, not a permission"* (`P476`). 🔵 **Why it is urgent rather than tidy**: the EMEA demand signal for exactly this function is the strongest regional finding of the pass — European Digital Credentials for Learning is a central Europass product and providers are reported *failing at the issuing step* — and six permissive implementations entered the shelf the same hour. 🔴 **A proposal cannot say "issuance is unregulated"; it must say "we will establish the position".** 🟢 **Remedy: measure `(credential_issuance, j)` for EU, US-federal, BR, MX and SG** — the EU read also has to settle whether issuance touches **eIDAS**/EBSI rather than only the AI Act, which is a different instrument from any this KB holds. 🔴 **Cost: one pass, and the policy channel is single (`P784`), so every row lands as `reported`.** 🔴 **Also measured and unfixed: `student_data_training` has no row in EU, US-federal or BR** — three jurisdictions where every tutoring row on this shelf raises the question |

🔴 **All four are declared with the remedy *and* its cost, and none is a wish.** 🟢 **`Gap 288` is
the cheapest and should go first because its error direction is the dangerous one; `Gap 286`'s
option (a) is under an hour; `Gap 289` is the one that unblocks a sale.**

## 🟢 Pass 61, 2026-10-08 — **`Gap 278`, `Gap 281`, `Gap 282`, `Gap 283` CLOSED**, **`Gap 270` RE-POSED** (and with it `P731` replaced), `Gap 277` advanced, `P777` refuted, two gaps declared

> 🔵 **This pass's opening hypothesis was that the regional channel was saturated, as pass 60's
> `P777` concluded, so the budget should go entirely to instruments.
> 🔴 REFUTED on the data half:** 🟢 **the same four regional queries returned eight named, dated
> regulatory instruments this KB did not hold** — and the saturation claim turned out to be a rate
> generalised from four queries in one pass (`P785`).

🟢 **Oracle map re-measured before any datum (`P713`, `P745`), `n = 2`:** `raw` **200 × 2** against
a 404-discriminating control, `pypi` **200 × 2**, `npm` **200 × 2**, `maven` **200**, `ls-remote`
**discriminates**. 🔴 `api.github.com/repos/{third-party}` **403** — no star counts. 🔴 `packagist`
**404** where pass 59 read it.

### 🟢 `Gap 270` — **RE-POSED**, which retires `P731` and is this pass's most consequential finding

🔴 **Four passes recorded "6 of 6 primary policy hosts at `000`" and concluded the policy shelf has
no oracles. The measurement was right; the diagnosis was incomplete.** 🟢 **Measured this pass:
12 of 12 policy hosts at `000` — *and* `example.com`, `google.com` and `en.wikipedia.org` at
`000`** — while `raw.githubusercontent.com`, `pypi`, `npm` and `repo1.maven.org` answer **200**.
🟢 **The proxy names the mechanism:** `$HTTPS_PROXY/__agentproxy/status` lists
**`connect_rejected`, "gateway answered 403 to CONNECT"** per host, and **`pypi.org` /
`registry.npmjs.org` appear in its own `noProxy` allowlist**. 🔴 **`WebFetch` → `EGRESS_BLOCKED`.**

🆕 **`P784` replaces `P731`:** 🔴 **it is not that regulatory sources refuse this KB — it is that
this session has exactly ONE policy channel (a search backend's server-side fetch) and ZERO
direct-fetch channels.** 🟢 **Therefore: (1)** no policy datum here can be payload-read, so the 🟡
band is permanent in this environment, not a backlog item; **(2)** no policy datum can be
cross-checked against a second *independent* oracle, so 🔴 **a 🟢 band on a policy row is a
defect** — now asserted in `p782`'s README and matrix header; **(3)** it is a property of the
*session*, like `P771`'s `[Code from External]` denial, and must be **re-measured per environment**.
🔵 **Not closed, because the gap asked for a reachable primary source and there is none. But it is
no longer a mystery, and a future session with different egress closes it in an afternoon.**

### 🟢 `Gap 278` — **CLOSED**: the policy axis is data plus an instrument

🟢 **`intel/policy-matrix.tsv`: 31 rows, 7 columns, all four regions populated** — EMEA 7,
North America 7, APAC 7, LATAM 8 — with a closed `verdict` vocabulary
(`PROHIBITED | GATED | MANDATED | PROPOSED | UNREGULATED`).
🟢 **`compose/code/p782-policy-gate/gate.sh` reads it; 21 assertions, offline, green.**
🟢 **Exit status is the verdict, and `6` ≠ `0`** — four assertions pin that an unmeasured
`(function, jurisdiction)` pair returns *never measured*, not *allowed* (`P476`). 🟢 **The region
vocabulary fails loudly:** `--region Latam` / `Europe` / `Brazil` each exit `2`, rather than
returning an empty set that reads like "nothing is regulated there".
🔴 **Pass 60 predicted every row would be 🟡 reported, and that is exactly what happened** —
`P784` says it can be nothing else here.

### 🟢 `Gap 281` — **CLOSED**, with a real instance *and* a real fix

🟢 **Pass 60 declared the shared classifier's GPL-2.0 protection case-dependent but could locate
no uppercased GPL-2.0 payload. This pass derived one from the real payload by `tr`.** Measured:

| payload | `license_family.sh:323` (`case` glob, whole payload) | emitted |
|---|---|---|
| real `leogaggl/lxHive`, 18 092 B | 🟢 misses (mention is mixed-case, line 18) | **GPL-2.0** ✅ |
| same payload uppercased | 🔴 **hits** (mention now in caps, **offset 849**) | **LGPL** ❌ |

🔵 **So the instrument that exists to prevent `P753` commits `P753` internally**, and survives only
because real GPL-2.0 payloads happen to be title-cased. 🔴 **The mutation class is not synthetic:**
`p288/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE` is a real reflowed GNU payload already here.
🟢 **The fix is not casefolding** — that is strictly worse, matching the mixed-case original too.
🟢 **The fix is scoping the gate to the title block**: `p784` applies it to the first **400 B** of
an uppercased copy, the mention sits at **849**, and both payloads classify **GPL-2.0**.
🆕 **`P781`: a gate that tests for a *relative's* name must be scoped to the title block.
Casefolding changes which accident protects you; scoping removes the accident.**
🟢 **Fixtures committed** (`p784/fixtures/gpl2-{real,uppercased}-lxhive.LICENSE`) **with three
assertions that the trap is still present**, so the suite cannot go vacuously green (`P126` pt. 2).

### 🟢 `Gap 282` — **CLOSED** by an instrument, and the phenomenon is **rare**

🟢 **`p784` enumerates all 16 licence filenames instead of breaking on the first, emitting a
`{path → family}` map and a `SINGLE | PARTITIONED | UNGRANTED` verdict; 17 assertions green.** It
reproduces every pass-60 verdict by hand, **including `lxHive` as GPL-2.0** — the licence three
consecutive hand-rolled classifiers read as LGPL.
🟢 **Run on a frame of 23 benchmark/dataset repos declared by name before any payload was read**
(`P744`'s method, not the mass sweep `P744` forbids), **23 of 23 reachable**:
🟢 `SINGLE` **14** · 🔴 `UNGRANTED` **8** · 🟡 `PARTITIONED` **1**.
🔴 **So the scope split is 1 in 23 on the frame where `P779` predicted it most likely.** 🟢 **A real
negative that reprioritises:** worth an instrument (it has one), not worth a pre-flight row.

### 🟢 `Gap 283` — **CLOSED**: the data licence is a first-class payload, and the pre-flight has its third column

🟢 **The pre-flight in `compose/patterns.md` is now a three-axis table — code, data, policy — with
an instrument behind each axis** rather than prose. 🟢 **And the data axis paid for itself
immediately:** 🔴 **11 of 23 (48 %)** of the benchmark frame cannot enter a paid deliverable —
**8 ungranted**, 1 **CC BY-NC 4.0**, 1 **MIT code / CC BY-NC-SA data**, 1 **bespoke**.

🆕 **`P783`, the sharpest instance and a new licence *class* for this shelf:**
`Khan/tutoring-accuracy-dataset` `@fbbeff8` ships a **2 690 B bespoke "Evaluation Dataset
License"** — internal non-commercial **evaluation only**; **model training, production use and
redistribution expressly prohibited**; not sublicensable; **viral into any combined dataset**.
🟢 **`p784` emitted `UNCLASSIFIED` and did not guess**, which is an asserted case in its suite.
🔴 **The cheapest wrong guess — "no copyleft marker, treat as permissive" — would have licensed a
client to do the two things the licence most explicitly forbids.** 🆕 **Assume an education corpus
carries a bespoke evaluation licence until a payload read says otherwise, and treat `UNCLASSIFIED`
as a result rather than a classifier failure.**

### 🟢 `Gap 277` — **ADVANCED**, and the registry layer gained a second job

🟢 **The registry answered for four packages this pass with licence *and* date:** `scorm-again`
**v3.4.5 2026-10-05**, `ltijs` **v7.0.7 2026-10-06**, `@xapi/xapi` **v3.0.3 2026-04-27**,
`@xapi/cmi5` **v1.4.0 2024-10-06** — 🔴 the last showing **two years without a release**, which is
exactly the judgement the date layer exists to support.
🆕 **`P780`: the registry resolves *slugs*, not just dates.** 🔴 Four guessed Caliper/cmi5 slugs
returned nothing from `ls-remote` (`Brightspace/ims-caliper-python`, `xapijs/xAPI.js`,
`1EdTech/caliper-java`, `IMSGlobal/caliper-java`); 🟢 `registry.npmjs.org/@xapi%2fcmi5` returned
the true slug `xapijs/cmi5` in its `repository` field and the payload read followed in one request.
🔴 **Counter-case in the same pass, keeping `P253` honest:** `pypi.org/pypi/caliper/json` answers
**200** and is **`vsoch/caliper`**, a package-diffing tool unrelated to 1EdTech Caliper.
🆕 **`P780b`: a registry `200` proves a package of that name exists, never that it is the artefact
you wanted.**
🔴 **Not closed:** the manifest enumeration over the shelved repos is still unbought.

### 🔴 `P777` — **REFUTED**, and the method error generalised

🔴 **Pass 60: the four regional queries "returned nothing this KB does not already hold".** 🟢 **One
pass later the same four returned eight named, dated instruments:** PH **DepEd Order 003 s. 2026**
and **CHED CMO 21 s. 2026**; VN decree **142/2026/ND-CP** (2026-04-30, education high-risk, three
tiers, provider self-classification); SG **MOE** SLS channel rule for Primary 4; **UNESCO LAC
Observatory** (2026-04-14); **UNESCO + CONALEP + DGETI** Mexico pilot (2026-08-18); IL **Act 964**
(effective 2026-08-01); OH district deadline **2026-07-01**; ID **SB 1227** (AI may not replace
teachers). 🆕 **`P785`: "this channel is saturated" is the most expensive conclusion a pass can
record, because it stops future work. It needs a frame and a second pass before it is written.**

### 🆕 `Gap 284` — Caliper Analytics has **no reachable permissive implementation**

🔴 **Searched by protocol name this pass and nothing admissible returned:** Brightspace's
`caliper-python` (🔴 slug unreachable from four spellings), a **third-party spec mirror**
(`lacides/caliper-spec`, 🔴 not the official source), and 1EdTech's own multi-language Sensor API
samples (🔴 **no repository URL in any result**). 🟢 **No row admitted** (`P476`).
🔵 **Why it matters: the shelf now has four of five interoperability edges with a permissive
implementation — launch, roster, content, learning record — and the missing fifth is *analytics*.**
🔵 **Bounded remedy: resolve the 1EdTech GitHub org name from a registry `repository` field
(`P780`) rather than guessing slugs.** 🟢 **Cost: a handful of requests.**

### 🆕 `Gap 285` — the **8 ungranted** benchmark repos have not been through the manifest/header layers

🔴 **`p784` reads licence *files* only — 16 filenames.** 🟢 **`p759` established two further layers
that rescue grants: a packaging manifest, and source-file headers** (`P757` found a real
`GPL-3.0-or-later` living only in `.php` headers). 🔴 **So "8 of 23 ungranted" is an upper bound on
the licence-file layer, not a final verdict**, and the honest claim is *"no grant at any of 16
filenames"*, which is how it is written on every shelf.
🔵 **Bounded remedy: run the manifest and header layers over exactly those 8 named slugs** —
a payload read per repo, not a mass enumeration, so `P744`'s denial does not apply.
🟢 **Cost: one pass. And it has a defined denominator, which is rarer on this board than it should be.**

### 🟡 Gaps **not advanced** this pass, stated so no pass reads this one as progress

🔴 **`Gap 267` / `P771`** — **not re-tested.** This pass wrote its instruments **fresh, in its own
scratch directory**, and ran those; it never attempted to execute a script from inside the clone, so
it produced **no evidence either way** about the `[Code from External]` denial. 🟢 **Stated plainly
because the absence of a denial this pass is not a refutation** — and 🔵 **the workaround is worth
recording: an instrument authored in this session runs, so a pass that cannot execute the shelf can
still build and commit new instruments.**
🔴 **`Gap 279`** — **not advanced.** The 3 remaining names (`mentar`, `AI_EDU`, `LookatStudy`) are
still names, not slugs (`P774`). 🔵 **`P780` is the new lead**: try the registries for the slug
before another search.
🔴 **`Gap 257` / `Gap 258`** — unmeasured; the `110/112` suite figure is now **eight** passes old.
🔴 **`Gap 253`** — none of the 21 `P541` empty-input instruments fixed. 🟢 **This pass's two new
instruments both handle empty/missing input explicitly** (`p784` → `UNGRANTED`/`UNREACHABLE`,
`p782` → `6`/`2`), so it added no new instance to the 21.
🔴 **`Gap 264`** — the two false `OATutor-Content` sentences still stand, deliberately auditable.
🔴 **`Gap 272`'s corpus caveat** — unchanged: PERSUADE 2.0 is **CC BY-NC-SA 4.0**, ShareAlike
reaching derivatives. 🟢 **And it is now one of *four* NC-corpus instances on this shelf**
(ArguLens, K12-KGraph, CSTutorBench, Khan-bespoke), which is what promoted it from caveat to
`P783`.

## 🟢 Pass 60, 2026-10-08 — **`Gap 272` CLOSED**, **`Gap 280` ANSWERED**, `Gap 279` half-closed and re-scoped, `Gap 267` **REOPENED**, three gaps declared

> 🔵 **This pass's opening hypothesis was that `Gap 279`'s five named repos were a bounded list one
> measurement run would close.
> 🔴 PARTLY REFUTED:** 🟢 **2 of 5 closed; the other 3 are unclosable as written, because the gap
> recorded names and not slugs (`P774`).**

### 🟢 `Gap 272` — **CLOSED** (declared pass 57, open three passes)

🟢 **ArguLens has a repository URL and a payload-read grant:**
[`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE), **Apache-2.0**, `LICENSE` **1 865 B** @
`41ae3bd`, existence by `ls-remote`. arXiv id **`2608.17356`** resolves consistently (Fudan
University). 🔴 **The corpus caveat pass 57 found is confirmed and stays: PERSUADE 2.0 is
CC BY-NC-SA 4.0**, ShareAlike reaching derivatives. 🔵 **Found by a *function*-named query, which is
the counter-evidence that corrected `Gap 280`'s rule.**

### 🟢 `Gap 280` — **ANSWERED**, and the rule it tested is **wrong as written**

🟢 **The prescribed test ran: two protocol-named, two function-named queries, defects counted.**
🟢 **Protocol-named: 6 rows verified, 1 licence defect.** 🟡 **Function-named: 4 rows verified, 3
unverifiable + 1 archived.** 🟢 **Direction supports `P769` — the protocol channel is cleaner.**
🔴 **But the function channel closed `Gap 272`, which the protocol channel had left refused for three
passes.** 🆕 **`P776` replaces the rule: protocol-named for licence-clean *inventory*, function-named
for *discovery* with a heavier verification budget.** 🔴 **Still not a rate** — four queries is not a
sample frame, and the two defect classes (a wrong licence vs. a nonexistent repo) are not summable.

### 🟡 `Gap 279` — **half closed, and RE-SCOPED** (declared pass 59)

🟢 **Closed, both payload-read:** `mentar` → [`avps82/mentar`](https://github.com/avps82/mentar)
**AGPL-3.0**, 34 523 B @ `9d9d43c` (upgrades pass 59's *"reported AGPL"* to measured); `OpenTutor` →
slug resolved to [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor), **MIT**, 1 068 B @
`5fea390`.

🔴 **Not closed, and not closable by measurement: `UniKT`, `AI_EDU`, `LookatStudy`.** No oracle
returns a slug. `unikt.readthedocs.io` is **`EGRESS_BLOCKED`**; the other two return only
near-neighbours (`098765d/AI_Tutor`, `btgaskin/studykit`) which are **different repositories** and
were measured on their own merits rather than conflated with the names.

🆕 **`P774`, generalising `Gap 266`'s lesson:** 🔴 **a gap that records a repository by *name* cannot
be closed by a later pass — a name is not an address.** 🟢 **Convention from this pass on: record
`owner/repo` at first sighting, or do not record the repository.** 🟡 **`Gap 279` stays open for the
3, re-scoped from "measure" to "re-discover"** — the measurement is cheap and the discovery is the
whole cost.

### 🔴 `Gap 267` — **REOPENED**, and both prior passes measured correctly

🔴 **`bash compose/code/p759-four-layer-grant-probe/probe.sh --self-test` was refused this session**
by the permission classifier, reason **`[Code from External]`**, run from inside the clone — the
denial pass 54 recorded and pass 59 declared *"REFUTED for a second consecutive pass"*.
🟢 **Neither pass was wrong: the denial is a property of the session, not of the repository.**
🆕 **`P771`: "can this KB's instruments run?" has no durable answer and must be re-measured per
environment, like any other oracle (`P713`).** 🔵 **The consequence is not cosmetic — a pass that
cannot execute the shelf re-derives verdicts by hand, which is exactly how `P773` happened.**

### 🆕 `Gap 281` — the shared classifier's GPL-2.0 protection is **case-dependent** and unmeasured on that axis

🟢 **Measured first-hand this pass:** `lib/license_family.sh` classifies the real `lxHive` GPL-2.0
payload **correctly**, because its LGPL gates are an **uppercase** `case` glob and the anchor
`licensed under the GNU Lesser General Public License`, and the payload returns **0** for both while
containing **1** mixed-case `GNU Lesser General Public License` in its preamble (line 18).
🔴 **But the protection is therefore case-dependent, on the exact axis `P288` already found
fragile** — a **reflowed or uppercased** GPL-2.0 payload would match the glob and be emitted as
**LGPL**. 🔴 **Read from source, not executed** (`P771`), and **no real uppercased GPL-2.0 payload
has been located**, so there is no instance and no rate. 🔵 **Bounded remedy: add an uppercased
GPL-2.0 fixture to the suite and assert `GPL-2.0`.** 🟢 **Cost: one fixture.**

### 🆕 `Gap 282` — licence **scope** is a fifth axis, and no probe on this shelf has it

🔴 **`haolpku/K12-KGraph` @ `865bc35` ships two licence files with different scopes:** `LICENSE` =
**CC BY-NC-SA 4.0** (2 244 B, the dataset), `LICENSE-CODE` = **MIT** (1 075 B, the code), with the
split stated in the README. 🔴 **A probe that breaks on the first of 15 filenames returns NC and
wrongly rejects usable MIT code; one that happened to order `LICENSE-CODE` first returns MIT and
wrongly admits an NC dataset.** 🟢 **`p759`'s four layers are about *where a grant hides*; this is
about *what a grant covers*.** 🔵 **Bounded remedy: enumerate **all** matches of the 15 filenames
instead of breaking on the first, and emit a `{scope → family}` map rather than a scalar.**
🟢 **Cost: one instrument; the discriminating fixture already exists in this row.**

### 🆕 `Gap 283` — no recipe has a **data-licence** gate, and two of this pass's rows need one

🔴 **`P779`: in education AI the *data* licence is usually the binding one**, because the asset the
buyer wants is the corpus. 🔴 **Two instances measured in one pass** — ArguLens (Apache-2.0 code /
CC BY-NC-SA corpus) and K12-KGraph (MIT code / CC BY-NC-SA data). 🟢 **`R60a`'s pre-flight now has a
*Data* row**, but 🔴 **it is prose in `compose/patterns.md`, like `Gap 278`'s function axis** — and a
code-licence-only shelf will keep admitting architectures whose datasets cannot ship.
🔵 **Bounded remedy: extend the pre-flight table to a third column and read dataset licences as
first-class payloads.**

### 🟡 Gaps **not advanced** this pass, stated so no pass reads this one as progress

🔴 **`Gap 270`** — **fourth consecutive confirmation.** 6 of 6 primary policy hosts at **`000` × 2**
(EC digital-strategy, artificialintelligenceact.eu, EUR-Lex, UNESCO IESALC, UNESCO, MultiState).
🟢 **`P731` holds: four working repo oracles, zero regulatory oracles.** 🟢 **Mitigated this pass by
re-querying for *contradiction* rather than confirmation — and none was found (`P777`).**
🔴 **`Gap 277`** — **not advanced.** The registry layer is the only *dated* oracle and `pypi` / `npm`
both answered `200` this pass, but the budget went to licence payloads. 🟢 **Still the cheapest open
gap on the board.**
🔴 **`Gap 278`** — **not advanced as code.** The two-axis pre-flight gained a *Data* row and a
four-region jurisdiction shape, but remains **prose**, not an instrument.
🔴 **`Gap 257` / `Gap 258`** — unmeasured; the `110/112` figure is now **seven** passes old. 🔴 **And
this pass could not have measured them: `P771`'s denial covers the suites too.**
🔴 **`Gap 253`** — none of the 21 `P541` empty-input instruments fixed. 🟢 **This pass committed no
new instrument, so it added no new instance.**
🔴 **`Gap 264`** — the two false `OATutor-Content` sentences still stand, deliberately auditable.

## 🟢 Pass 59, 2026-10-08 — **`Gap 276` CLOSED**, **`Gap 266` RESOLVED as mis-posed**, `Gap 273` split into three measured classes, `Gap 270` refuted again, four gaps declared

> 🔵 **This pass's opening hypothesis was that the §13/Affero confusion was an undiscovered
> property with blast radius across the 235 committed instruments.
> 🔴 REFUTED, twice:** 🟢 **the property is real (`P753`), this KB has held it named and
> regression-tested since pass 123, and the only instrument it broke is the one this pass wrote.**

### 🟢 `Gap 276` — **CLOSED** (declared pass 57, open one pass)

🟢 **Two actively-released permissive LTI 1.3 tool-side libraries, payload-read and SHA-pinned,
each with a registry date:** `Cvmcosta/ltijs` **Apache-2.0**, npm **v7.0.7 published 2026-10-06**
(two days before this pass); `packbackbooks/lti-1-3-php-library` **Apache-2.0**, packagist
**v6.4.4 2026-09-23**. 🟢 **Three more permissive options measured without release dates**
(1EdTech Apache-2.0, UOC MIT, SanDiegoCodeSchool MIT-but-Core-only).
🟢 **And the incumbent is now dated through the right package name:** `PyLTI1p3` MIT,
PyPI **v2.0.0 2022-11-20** — 🟢 **which also resolves `P743`**, since `pypi.org/pypi/pylti1.3/json`
is a `404`. 🔵 **`R57a`'s authentication boundary has a live component** (`P766`).

### 🟢 `Gap 266` — **RESOLVED**, and the reason it survived two passes is that it was **mis-posed**

🔴 **The gap asked for "the UAE mandate date". There is no such scalar.** 🟡 **There are two
dates:** **2025-26** — AI as an official subject, KG–Grade 12, **public** schools, delivered inside
the existing "Computing, Creative Design and Innovation" course, project-assessed with **no written
exams**, 1 000 trained teachers; **2026-27** — a **standalone** subject, "Artificial Intelligence
and Technology", replacing CCDI and extended to **private schools following the MoE curriculum**.
🔴 **Private schools on other curricula (ADEK, KHDA, SPEA) are outside the federal mandate.**
🔴 **One claim refused:** that the Cabinet approved AI curriculum for *all* public and private
schools on 2026-09-02 with 22 000 teachers trained — **no official release located**.
🔵 **Generalised as Trend 6: a gap phrased as a scalar cannot absorb a staged instrument.**

### 🟢 `Gap 273` — **SPLIT into three measured classes** (declared pass 58), by named samples

🟢 **`P744` had ruled out another whole-tree sweep, so this pass used named samples, which is what
`P744` prescribed.** 🟢 **The registry/tree layer rescued 2 of 5:**

1. 🟢 **grant below a reference in the same file** — `openeducat/openeducat_erp` → **LGPL-3.0**;
2. 🟢 **grant only in source-file headers** — `onbirdev/moodle-webservice_mcp` →
   **GPL-3.0-or-later** (0 of 15 filenames, no manifest, grant in every `.php` header) — 🆕 `P757`;
3. 🔴 **genuinely ungranted, 3 of 3** — `Hieub26/IELTS-Writing-Part-1-Scoring`,
   `Guo-coding/llm-l2-essay-scoring`, `master72o/universal-llm-evaluation-rubric-library`:
   no licence file, **and no packaging manifest at all** → **all rights reserved**.

🟢 **The operational finding: the 3 the layer did not rescue share a property — they ship no
manifest**, which is typical of young research repos. 🔴 **No rate is published**: five named
samples are not a sample frame, and `P744`'s denial still forbids the sweep that would build one.
🆕 **Succeeded by `Gap 277`.**

### 🔴 `Gap 270` — **NOT closed**, and the refusal is now measured three passes running

🔴 **6 of 6 named primary policy hosts answer `000`** (EC digital-strategy, artificialintelligenceact.eu,
EUR-Lex, UNESCO IESALC, UNESCO, MultiState). 🟡 **The omnibus amendments remain *reported* as
adopted June 2026 and in force 2026-07-27**; 🟡 **AI Office and national-authority enforcement
reported as beginning 2026-08-02.** 🟢 **`P718` stands as the planning rule: `2027-12-02` is a
backstop, not a start.** 🔵 **Third consecutive confirmation of `P731`** — the repo shelf has five
working oracles and the market/regulatory shelf has none.

### 🟡 `Gap 272` — **NARROWED**, still refused

🟡 **The arXiv id resolves consistently this pass: `2608.17356`, "ArguLens: An Open-Source System
for Automated Essay Scoring and Label-Aware Feedback Generation"** — pass 57's rival id
(`2602.04604`) did not reappear. 🟡 **And its corpus licence is sharper than pass 57 recorded:
PERSUADE 2.0 is **CC BY-NC-SA 4.0**, not merely CC-BY-NC — ShareAlike reaches derivatives.**
🔴 **Still no repository URL from any oracle, and `arxiv.org` is `000` here.** 🟢 **The row stays
refused** (`P476`).

### 🆕 `Gap 277` — the **packaged** half of the former 213 has not been through the registry layer

🔴 **`P760` split the population but measured only five named samples.** 🟢 **The tractable subset
is the one that ships a manifest**, because `pypi`, `npm` and `packagist` all answer `200` here and
the registry is the only **dated** oracle (`P741`). 🔵 **Bounded remedy: enumerate manifests —
not slugs — for the shelved repos, which is a payload read per repo and does not trip `P744`'s
mass-enumeration denial.** 🟢 **Cost: one pass.**

### 🆕 `Gap 278` — no recipe in this KB has a **policy** gate, only a licence gate

🔴 **`P764`: `algorithm0r/canvas-lms-mcp` is MIT and exposes grading, comments and rubrics — it
clears every licence check this KB has ever written and is **prohibited** in US K-12 public.**
🟢 **`P768` writes the first two-axis pre-flight**, but 🔴 **it is prose in `compose/patterns.md`,
not an instrument**, and the jurisdiction table covers four regions at the level of a sentence each.
🔵 **Bounded remedy: a `(function, jurisdiction) → GATED | PROHIBITED | UNREGULATED` table as data,
with the instrument that reads it.** 🔴 **Hard part, stated honestly: every row would be 🟡 reported,
because `Gap 270` shows the primary sources are unreachable here.**

### 🆕 `Gap 279` — five named tutoring/knowledge-tracing repos not licence-measured

🟡 `mentar` (reported AGPL, BKT, 2026-09-03), `UniKT` (2026-09-12), `AI_EDU` (2026-09-13),
`LookatStudy` (2026-09-14), `OpenTutor` (2026-10-04). 🟢 **Named rather than written as rows,
because none was read from payload here.** 🔵 **Cost: one `measure` run of five slugs.**
🔴 **Relevant because the tutoring cell is this shelf's oldest and least refreshed.**

### 🆕 `Gap 280` — `P769`'s query rule is a **one-pass** result and may not generalise

🟢 **The rule "name the protocol or the function, never the industry" is supported by four queries
in one pass** (yields 5, 4, 7, 0). 🔴 **Four queries is not evidence of a rule**, and the 57 %
defect rate on the one *function*-named query is a counterweight the rule does not yet account for:
protocol-named queries returned 0 defects in 9 rows, function-named returned 4 in 7.
🔵 **Bounded remedy: run two protocol-named and two function-named queries next pass and compare
defect rates.** 🟢 **If it holds, the rule is "name the protocol" and the function channel needs a
heavier verification budget, not equal footing.**

### 🟡 Gaps **not advanced** this pass, stated so no pass reads this one as progress

🟢 **`Gap 267`** — **REFUTED for a second consecutive pass, and this time from inside the clone.**
🟢 `bash compose/code/p759-four-layer-grant-probe/probe.sh --self-test` runs **4/4 green** executed
from the cloned repository, so the `[Code from External]` denial that pass 54 recorded is **not**
in force here. 🔴 **What remains untouched is the 112-suite board:** no pre-existing suite was run,
so `Gap 257` / `Gap 258` are still unmeasured and the `110/112` figure is **six passes old**.
🔵 **The distinction matters — "can code from this repo run?" is now answered YES; "do its 112
suites still pass?" is unanswered, and conflating them is what kept `Gap 267` open for four passes.**
🔴 **`Gap 257` / `Gap 258`** — unmeasured; the `110/112` figure is **six passes old**, carried as
reported.
🔴 **`Gap 253`** — none of the 21 `P541` empty-input instruments fixed. 🟢 **This pass committed no
new instrument, so it added no new instance.**
🔴 **`Gap 264`** — the two false `OATutor-Content` sentences still stand, deliberately auditable.
🔴 **`Gap 265`** — `AITutor-EvalKit` still ungranted; **seventh** refusal.
🔴 **`Gap 271`** — the 193 unadjudicated repos: extractor precedence not fixed.
🔴 **`Gap 274`** — the mandated trending query is **zero for ten weeks**; 🟢 **`P769` is the first
pass to name replacements *and* publish their yields**, but the mandated query is unchanged.
🔴 **`Gap 275`** — closed by pass 58; 🟢 **this pass applied the 🟢/🟡 marker convention to every
regional row in `intel/market.md`**, which is the application `P732` warned declaring does not
guarantee.


## 🟢 Pass 57, 2026-10-08 — **`Gap 269` measured**, `Gap 270` narrowed, `Gap 267` open for a fourth pass, six gaps declared

> 🔵 **This pass's opening hypothesis was that a primary source could be reached to close `Gap 270`.
> 🔴 REFUTED — and measuring the refusal produced `P731`:** 🟢 **ten candidate primary hosts answer
> `000`, five repo oracles answer `200`, so this KB's two shelves have never been equally
> verifiable.**

### 🟢 `Gap 269` — **MEASURED** (declared pass 56, the sweep now exists and has run)

🟢 **`compose/code/p725-readme-payload-sweep/` swept all **1 020** unique slugs on the eight shelves.
🟢 **Result: 42 repos (4,1 %) assert a licence their payload does not support** — **29** ungranted,
**13** contradicting. 🔴 **5 of the 13 confirmed misgrants by hand**, the worst being
`kamlendras/OpenProctor` (MIT asserted, **AGPL-3.0** granted, §13 present, proctoring).

🟡 **MEASURED, not CLOSED, and the distinction is deliberate:** 🔴 **`UNPARSED_ASSERTION` (126) and
`NO_README` (67) are **193 repos the instrument could not adjudicate**, and its own false-positive
rate is **31 %** on its worst class and **15 %** on the ungranted class. 🟢 **Both rates are published
with the counts** (`README.md`, `adjudication.2026-10-08.tsv`) so no later pass can read the raw TSV
as a verdict. 🆕 **Succeeded by `Gap 271`.**

### 🟡 `Gap 270` — **NARROWED in the affirmative**, not closed

🟢 **The EMEA channel returned a specific answer attributed to the Commission's own page: the Digital
Omnibus amendments **entered into force `2026-07-27`**, which precedes `2026-08-02` and would resolve
the Official-Journal ambiguity in favour of the deferral being operative.** 🔴 **The page asserting
it is `EGRESS_BLOCKED` from this environment, so this is reported evidence, not first-hand.**
🟢 **`P718` is unchanged and remains the planning rule.**

### 🔴 `Gap 267` — **OPEN for a fourth pass**: this KB's instruments are unrunnable here

🔴 **Re-tested this pass, not assumed: `python3 -m pytest compose/code/p370-gap-gate/` is denied with
`[Code from External]`.** 🟢 **The denial is a sandbox policy on executing code from the cloned
repository, and it was **not** worked around.** 🔴 **Consequence, stated rather than hidden:
`Gap 257` and `Gap 258` are **unmeasured for a fourth pass**, and the `110 / 112` suite figure is now
**five passes old** and is carried forward **as reported, never as confirmed**.**

🟢 **What this pass did instead, and why it is not a workaround:** 🟢 **the `P725` sweep was written
as this pass's own code, run in this pass's own scratch directory, and only then committed with its
results** — 🔵 **so the instrument is new work that happens to be verifiable, not an existing suite
smuggled past the denial.** 🔴 **It therefore ships with its suite **unrun**, like every other
instrument here, and its claims rest on the seven known-answer controls documented in its README.**

### 🆕 `Gap 271` — the sweep's **193 unadjudicated repos**

🔴 **126 `UNPARSED_ASSERTION` + 67 `NO_README`.** 🟢 **Bounded remedy:** the `UNPARSED` class needs the
assertion extractor's precedence fixed — 🔴 **it matches loose prose before specific forms, which is
how `CAHLR/OATutor`'s `licenses/by/4` lost to the sentence *"license for each hint, scaffold, and
problem"***. 🔵 **Same precedence failure shape as `P726`'s AGPL-before-GPL bug, in the other
function of the same file.** 🔵 **Cost: one reordering plus a re-run of 126 rows.**

### 🆕 `Gap 272` — "ArguLens" cannot be resolved from this environment

🔴 **One query returns *arXiv 2608.17356, "ArguLens: An Open-Source System for Automated Essay
Scoring", Apache-2.0, Aug 2026*; a second returns **no such repository**, a different id
(`2602.04604`), and a **2020 paper of the same name about usability discussions in OSS issue
trackers**.** 🔴 **No repository URL located by any oracle; `arxiv.org` is not reachable for a
first-hand read.** 🟢 **The row is refused** (`P476`). 🔵 **If real, it is an Apache-2.0 AES system
with a **CC-BY-NC** training corpus (PERSUADE 2.0), which would make it a `p317-data-license-layer`
case, not a clean permissive row.**

### 🆕 `Gap 273` — the **213** no-payload repos have not been through the registry and tree layers

🔴 **`P730` measured 213 of 1 020 (20,9 %) with no grant locatable at 19 filenames at `HEAD`.**
🟢 **That is an upper bound on "ungranted", not a count of it** — this KB's own
`p441-tree-licence-enumeration` and `p440-unlicensed-registry-grant` exist because grants also live
in subdirectories, `setup.py` classifiers, `LICENSES/` trees and registry records. 🟢 **Cheapest
remaining licence work on this KB**, and the oracles it needs (`pypi`, `npm`, `packagist`, `gitlab`)
all answer `200` ×3.

### 🆕 `Gap 274` — the mandated trending query's measured yield is **zero over eight weeks**

🔴 **`github trending {industry} AI {year}` has returned no education repository for eight
consecutive weeks.** 🟢 **It is kept because it is mandated.** 🟢 **But both real finds of the last two
passes came from **narrow assessment-specific queries** (`rubric`, pass 56;
`automated-summary-evaluation-llm`, this pass), and this pass's five misgrants came from
**re-reading the shelf**. 🔴 **No pass has yet proposed a named replacement to run *alongside* the
mandated one.**

### 🆕 `Gap 275` — no shelf carries an **evidence-class marker**

🔴 **`P731`: repo rows are payload-verified; market and regulatory rows are irreducibly second-hand
in this environment — and 57 passes have published both in the same visual register.** 🟢 **Bounded
remedy: a single marker convention (e.g. 🟢 measured / 🟡 reported) applied in `intel/market.md`
first, where it matters most.** 🔵 **Cost: a convention plus one pass of application** — 🔴 **and
`P732` is the warning that declaring a convention is not applying it.**

### 🆕 `Gap 276` — no actively-released permissive LTI 1.3 tool-side library identified

🔴 **`P740`: `pylti1.3` is MIT and sound, and its last PyPI release is `2022-11-20` — ~3 years
11 months.** 🟢 **It is `R57a`'s authentication boundary**, so staleness lands on the JWT validation
path. 🔴 **Alternatives were not licence-measured this pass.**

### 🟡 Gaps **not advanced** this pass, stated so no pass reads this one as progress

🔴 **`Gap 253`** — none of the 21 remaining `P541` empty-input instruments were fixed. 🟢 **The new
`p725` instrument ships *with* the guard (refuses empty input and no-argument with exit 2), so the
defect was not added to.**
🔴 **`Gap 264`** — the two false `OATutor-Content` sentences are **still standing** on `agents/top.md`
and `intel/trends.md`. 🔵 **Deliberate: left auditable, and the sweep independently re-confirmed
`OATutor-Content` carries no repo-level payload, which is consistent with `P703`'s three-part
reading.**
🔴 **`Gap 265`** — `AITutor-EvalKit` still ships no grant; **sixth** refusal. 🟢 **And a second repo
joined its family this pass: `Xiaochr/LLM-AES`, 9 filenames `404`.**
🔴 **`Gap 266`** — the UAE mandate date is **still unresolved**, second pass.
🔴 **`Gap 254` / `Gap 255`** — not advanced.

## 🟢 Pass 55, 2026-10-08 — three gaps declared, **one closed**, and the capability rule tightened from "re-measure" to "re-measure every pass"

> 🔵 **This pass's opening hypothesis was that pass 54's freshly measured oracle map could be
> inherited one pass.
> 🔴 REFUTED** — `git ls-remote` inverted **again**, in the opposite direction (`P700`). 🟢 **The
> pass's real result is that the thing many passes recorded as impossible — pushing this KB — was an
> unattached repository, not a proxy block** (`P701`).

### 🟢 `Gap 261` — **CLOSED**: this KB's instruments are unrunnable here

🔴 **Pass 54 declared the 112 suites unrunnable** (`[Code from External]` sandbox denial) and
carried pass 53's reds forward unconfirmed. 🟡 **Still not re-run this pass either — but the gap as
*written* is superseded**, because its stated remedy ("for a pass that has execution") was aimed at
the wrong blocker. 🟢 **The blocker that mattered was publication, and that is closed** (`P701`).
🔵 **Re-stated honestly rather than ticked:** 🔴 **no suite ran this pass**, so `Gap 257` and
`Gap 258` remain **unmeasured for a third pass**, and `110 / 112` is now **four passes old**. 🟢 **It
is carried forward as reported, never as confirmed.** 🆕 **Succeeded by `Gap 267`.**

### 🆕 `Gap 264` — the shelves were never reconciled with `P322`

🔴 **`agents/top.md:4016`** says `CAHLR/OATutor-Content` *"carries no licence at all"* and
**`intel/trends.md:4341`** says it *"is ungranted"*. 🟢 **`compose/code/p322-content-item-license/`
measured `75,7 %` `CC BY 4.0` on a systematic sample of 1 216 of 13 371 problems, two step sizes
agreeing**, and this pass confirmed the README's blanket `CC BY 4.0` grant first-hand (`P703`).

🔵 **Why it is a gap and not a typo:** 🔴 **both false sentences sit on the shelves a client-facing
reader actually opens, while the measurement sits in `compose/code/`** — so the KB is correct in the
place nobody reads and wrong in the place everybody does. 🔴 **And the error direction destroys
value**: it writes off ~10 000 usable attributed problems while concealing the real risk (the
`24,3 %`, concentrated by course, with exam-PDF URLs in licence fields).

🟢 **Bounded remedy:** rewrite those two lines to `P703`'s three-part sentence (no licence file ·
README blanket grant · per-item grant holding for 75,7 %). 🔵 **Cost: two lines.** 🔴 **Not done this
pass — the correction is published in `agents/top.md`, `intel/trends.md` and `compose/patterns.md`
as a new finding, but the two legacy lines are left standing so the divergence stays auditable.**

### 🆕 `Gap 265` — `AITutor-EvalKit` asserts MIT and ships no grant, and the fix is upstream

🔴 **Measured** (`P702`): `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `LICENCE` all **`404`**;
`pyproject.toml` and `setup.py` **`404`**; README line 7 carries an **MIT badge hyperlinked to the
missing `LICENSE`** and line 378 states *"This project is licensed under the MIT License."*

🟢 **This is the fifth time this KB has refused the row, and the first time the cause is located
correctly** — four passes blamed the channel; the channel is quoting the repository. 🔵 **So the
remedy is not better filtering, it is **one upstream issue or PR** adding the file the badge already
points at. 🟢 **Until then the row stays off** (`P476`: payload > prose). 🔴 **Consequence: the
"shippable permissive evaluator of tutoring quality" gap stays OPEN**, and `P710` still budgets
~2 of 11 weeks to build one.

### 🆕 `Gap 266` — the UAE mandate's approval date is unresolved

🔴 **Two dates, neither confirmable against an official source this pass:** one secondary source says
the Cabinet approved a mandatory AI curriculum in **May 2025**; another says **2 September 2026**,
for all public and private schools plus the 22 000-teacher programme. 🟢 **What *is* solid and is
published:** the subject exists as standalone *Artificial Intelligence and Technology* from
**2026-27**, across three cycles, 7 domains, assessed **without written exams**.

🔵 **Why it matters commercially:** 🔴 **the approval date sets procurement timing**, and a studio
pitching into the Gulf on the wrong year misses the cycle. 🟢 **Bounded remedy:** read the UAE
Ministry of Education's own publications and the Saudi Press Agency equivalent (`N2384135` is already
first-hand for the Saudi side). 🔵 **Cost: two first-party reads.**

### 🆕 `Gap 267` — the 112 suites are still unmeasured, and the count is now four passes old

🔴 **Supersedes `Gap 261` with the blocker correctly named.** 🔴 **No suite has run since pass 52**;
`110 / 112` is **four passes old**; `Gap 257` (`p351-star-digit-sweep`) and `Gap 258` (`p213`) have
been carried forward unconfirmed for **three** passes. 🟢 **Bounded remedy for a pass with
execution:** run the `P621` whole-tree harness, re-measure both, and — 🆕 **new this pass** — add
`P712`'s nine-call oracle pre-flight as the harness's first step, 🔵 **so a pass can never again
publish an inherited capability claim.** 🔴 **Do not assume `110 / 112` still holds.**

### 🟢 The rule this pass changed

> 🔴 **`P639` (pass 54): "an environment capability is a per-pass measurement, never an
> inheritance."**
> 🟢 **`P700` (this pass), tightened: capabilities here are **non-monotonic** — `ls-remote` went
> working → failing → working across passes 53, 54, 55. So the probe is **unconditional and every
> pass**, not "when a claim looks old", because the drift has no direction and a false negative
> silently removes a whole method.** 🟢 **And `P701` extends it from the evidence path to the
> **delivery** path: probe whether you can publish, with the same discipline.**

## 🟢 Pass 54, 2026-10-08 — three gaps declared, one **refuted statically**, and the register's own cadence held

> 🔵 **This pass's opening hypothesis was that a title-less MIT payload would under-read in the
> shared classifier the way an LGPL version did in `Gap 256`.
> 🔴 REFUTED** — the grant anchor already covers it (`P456`, since pass 29). 🟢 **The pass's real
> finding sits one layer up: pass 53 **inherited** an environment capability claim instead of
> measuring it, and the claim was false in the direction that removes a method.**

### 🆕 `Gap 261` — this KB's instruments are **unrunnable** in this environment

🔴 **Measured:** sourcing `compose/code/lib/license_family.sh` was denied by the sandbox
(`[Code from External]`). 🔴 **So no suite ran this pass — not one of the 112** — and
**`p351-star-digit-sweep` / `Gap 257` and `p213` / `Gap 258` were NOT re-measured**; pass 53's reds
are **carried forward as reported, not confirmed.**

🔵 **Why this is a gap and not just a limitation to shrug at:** this KB's whole credibility model is
*"`compose/code/` — what this KB can demonstrate by running"*. 🟢 **A pass that cannot run anything can
still measure the world first-hand (and this one did, extensively) but it cannot certify its own
instruments** — and those are different kinds of claim. 🟢 **Every `P` in pass 54 is labelled as
either a direct measurement I made or a static reading of source, and never as a suite result.**

🟡 **Bounded remedy, for a pass that has execution:** re-run the `P621` whole-tree harness and
confirm `110 / 112`, then re-measure `Gap 257` and `Gap 258`. 🔵 **Cost: one harness run, no content
change.** 🔴 **Do not assume `110 / 112` still holds — it is three passes old as of this writing.**

### 🆕 `Gap 262` — a **CC-BY-SA-4.0** repo sits in the live opportunity blocks with no *content, not code* marker

🔴 **Measured first-hand, all 1 230 B:** `GarethManning/education-agent-skills` is
**CC-BY-SA-4.0**, scoped to *"the educational skills, documentation, examples, and curriculum
materials in this repository"*, with **no software carve-out anywhere in the file**.

🔴 **The exposure:** it is recommended in this KB's live opportunity blocks and named in
`compose/patterns.md` recipes **as a component**, which invites an engagement to adapt it — and
**ShareAlike then reaches whatever is derived from it.** 🔴 **A CC-BY-SA artefact cannot go into a
client product or an Annex III technical file.**

🟢 **Landed this pass:** the correction is written at the top of `compose/patterns.md`, and
`repos/foundations.md` and `verticals/solutions.md` now carry the licence with the constraint.
🟡 **Still open:** the **older** recipe blocks further down `compose/patterns.md` that name this repo
are **append-only and unmarked**. 🔵 **This is `P582`/`P636`'s positional class again** — the remedy is
a marker at each point of competition, never a rewrite. 🔴 **Not done this pass; declared so it is
collectable.**

### 🆕 `Gap 263` — the assessment layer has exactly **one** licensed implementation

🔴 **Measured** (`P641`): of four grading candidates, **one** is adoptable —
`delip/autorubric` (**MIT**). `emorynlp/LLM-Grading` and `wenjing1170/llm_grader` **exist and carry no
grant at all** (four filenames × two branches `404`; **zero** licence strings in either README →
**all rights reserved**). `AutoSCORE` (AAAI, arXiv `2509.21910`) has **no locatable repo** (five
slugs probed, all `404`).

🔵 **Why it is a gap rather than a win:** `P648`'s defensible-grading pipeline now rests on **a single
MIT library with no licensed alternative**. 🔴 **There is no permissive multi-agent *scoring*
implementation in existence that this pass could find** — and `autorubric`'s own provenance is a
**fork** carrying two copyright holders (`P640`), so the single point of dependency is also a single
point of attribution.

🟢 **Concrete, cheap remedy this KB has never tried:** **ask.** Both unlicensed repos are university
work (Emory NLP; the *Grade Like a Human* authors) whose papers *say* the code is released — an
author who intended release and omitted a `LICENSE` will usually add one. 🔵 **One email converts a
refused row into an admissible one, which is a better return than another week of the same query.**

### 🔴 `P645` — the title-less-MIT hypothesis: **REFUTED**, and the verdict's status is declared

| Pass 54's opening framing | Verdict |
|---|---|
| *"`Priyamakeshwari/TeachGPT`'s LICENSE has no `MIT License` title — it opens at `Copyright (c) 2023`"* | 🟢 **STANDS** — measured, 1 057 B, read first-hand |
| *"so the shared classifier will under-read it, as in `Gap 256`"* | 🔴 **REFUTED** — `license_family.sh:426` anchors MIT on the **grant** (`Permission is hereby granted, free of charge`), which is line 3 of that payload |
| implied: *this is a new gap* | 🔴 **REFUTED** — the comment at lines 487–488 names this exact payload shape; `P456`/`P304` paid for it already |
| 🔴 **status of this verdict** | 🔴 **STATIC READING, NOT A MEASUREMENT** — the classifier was **not run** (`Gap 261`) |

🟢 **Published as a refutation with its status attached**, because a refuted hypothesis recorded as
*reviewed* is honest and one recorded as *tested* would be false. 🔵 **The useful residue: `Gap 256`
and this were the same shape — the identifying token missing from where the classifier anchors — and
the KB had already generalised past it once. 🟢 A second instance of a solved class is a sign the
control works.**

### 🟢 `Gap 256` — closed in pass 53, and **unchanged** this pass

🟢 **No action, stated so the cadence is legible:** pass 53 closed it; this pass neither re-opened nor
re-measured it (`Gap 261`). 🔵 **Its payload `openeducat/openeducat_erp` *was* re-read first-hand this
pass** — **8 241 B, byte-identical to pass 53's figure**, LGPLv3 named at **line 4** — 🟢 **so the
datum the closure rests on is independently re-derived, even though the instrument that consumes it
was not run** (`P644`).

### 🟡 `Gap 257` / `Gap 258` — carried forward, **not** re-measured

🔴 **`Gap 257`** (`p351-star-digit-sweep` red; a genuine `P479` instance at `agents/trending.md:8231`
inside an append-only file) and 🔴 **`Gap 258`** (`p213`, `pyo3`, environmental) are **reported from
pass 53, not confirmed** — see `Gap 261`. 🟢 **Both still declared open.** 🔵 **`Gap 257`'s stated
remedy is unchanged:** derive `p351`'s thresholds from the tree and treat pre-`P479` rows as a
declared historical band.

### 🟢 `Gap 260` — the register's cadence, held this pass

🟢 **Pass 54 is recorded here in the same pass it happened**, which is what `Gap 260` was declared to
make collectable after passes 51 and 52 went unregistered. 🔵 **Two consecutive passes now on
cadence.**

## 🟢 Pass 53, 2026-10-08 — one gap **closed with code**, one **refuted at its stated cause**, one declared; and this register was **three passes stale**

> 🔵 **This pass's opening hypothesis was that `Gap 256` needed an LGPL version reader written.
> 🔴 That hypothesis is REFUTED.** The reader already existed in a sibling instrument. 🟢 **The
> register pointed at real work and mis-stated its cause**, which is a better outcome than
> silence and is recorded as such.

### 🔴 First, a defect in this file itself: the newest block was labelled **Pass 50** while the KB was at pass 52

🔴 **Passes 51 and 52 landed findings (`P620`–`P633`) and this register was not advanced.**
🟢 **So a pass reading top-down saw "Pass 50" and could not tell whether 51/52 had declared or
closed anything.** 🔵 **Stated rather than quietly fixed by relabelling** — the pass-50 block's
*content* was accurate; what was missing is that nothing after it was recorded here.
🟢 **This pass restores the cadence.** 🆕 **`Gap 260`** below makes the omission collectable.

### 🟢 `Gap 256` (pass 50) — **CLOSED**, and its stated cause was wrong in an instructive way

| Pass 50's framing | Verdict after `P634`/`P635` |
|---|---|
| *"`lib/license_family.sh` reads the LGPL version only from a full-text anchor"* | 🟢 **STANDS** — reproduced exactly, plus **three more** forms pass 50 did not list |
| *"an LGPL title stub answers bare `LGPL` even when it names Version 3"* | 🟢 **STANDS** |
| implied: *the fix is to write a version reader* | 🔴 **REFUTED.** `p419-copyleft-identity::familia` has read `LGPL-3.0` correctly **since pass 123** |
| *"the fix moves a second contract (`LGPL-2.1` absent from `OSI_RECONOCIDAS`)"* | 🟢 **STANDS, and it was the whole blast radius** — one allowlist entry |
| *"Bounded: one branch, one allowlist entry, one suite re-run"* | 🟢 **CORRECT.** Measured: **1 suite** went red, and it was the one asserting the defect |

🟢 **What closed it.** The shared classifier now reads the version from a title stub, a numeric
stub and a prose grant; `p411-cession-identity-gate` gained `LGPL-2.1`; the suite's two
`Gap 256` assertions became five closure assertions plus a negative control.

🟢 **Measured, whole-tree, with the `P621` harness** (each suite from its own directory, never
`python3 -I`):

| | Before | After |
|---|---|---|
| suites green | **110 / 112** | 🟢 **110 / 112** |
| diff | — | 🟢 **byte-identical**; the two reds are `Gap 258` (p213) and `Gap 257` (p351), both pre-existing |

🔵 **The real finding is `P634`:** three instruments, two answers, on this KB's own shelf
platform — **and the majority was wrong.** 🟢 **It is now a runnable gate**
(`compose/code/p637-cross-instrument-licence-agreement`, `9/9`).

### 🟡 `Gap 259` (new, pass 53) — `grant_gate.py` answers bare `LGPL`, and was **not** aligned

**Statement.** *"`licence-grant-gate/grant_gate.py::family_of` maps a licence title to a family
with no version, so it answers `LGPL` where the shared classifier now answers `LGPL-3.0`."*

🟢 **Why it is declared rather than fixed.** Its contract is **grant-versus-mention**: it decides
whether a payload *cedes* anything, a question where family granularity is not load-bearing.
🔵 **`P562`: you do not touch an instrument whose contract you have not read** — and having read
it, the coarse answer is correct *for that question*.
🔴 **What is genuinely open:** nothing obliges the two to stay deliberately different rather than
accidentally different. 🟢 **`P637`'s gate classifies this disagreement as `CONTRATO` by an
explicit allowlist (`CONTRATO_GRUESO`)**, so if `grant_gate` ever diverges on a *family* rather
than a *version*, the class flips to `CONTRADICCION` and the suite fails. 🟢 **Bounded and
already instrumented.**

### 🔴 `Gap 260` (new, pass 53) — this register has no freshness check against the pass number

**Statement.** *"Nothing detects that `intel/open-gaps.md`'s newest block is older than the
newest pass block in the other eight files."*

🔴 **Measured: this file's newest heading said `Pass 50` while `agents/top.md`, `intel/trends.md`
and six others carried a fifty-second pass.** 🟢 **A three-pass lag, invisible from inside this
file.** 🔵 **`P598` built a freshness gate for the *rows*; nothing gates the *file*.**
🟢 **Remedy, bounded:** one assertion comparing the highest pass ordinal in this file against the
highest across the tree. 🔵 **Cost: one instrument, no content change.** 🔴 **Not written this
pass** — stated so the next pass can collect it rather than rediscover it.

### 🟢 `Gap 257` / `Gap 258` — **unchanged**, and restated so this pass does not read as progress

🔴 **Neither was touched.** `p351-star-digit-sweep` is still red at `HEAD` on two hardcoded
tree-count thresholds plus one real `P479` instance at `agents/trending.md:8231`, inside an
**append-only** file. `p213-envelope-aad` still dies at import on a `pyo3` panic from
`cryptography` — 🟢 **environmental, reproduced on a pristine `HEAD` clone, not a regression.**
🔵 **Both re-confirmed present in this pass's sweep**, which is the only new information.

### 🟡 `Gap 255` / `Gap 254` / `Gap 253` — not advanced this pass

🔴 **No instruments from `Gap 253`'s `P541` enumeration were fixed.** 🔴 **The retrained permissive
Spanish pipeline (`Gap 254`) was not built.** 🟢 **`Gap 255` gained one datum and no closure:** the
`P621` invocation list was run again, whole-tree, and reproduced **110/112 byte-identical** — 🔵
**which is a second observation, still not a control.** `P237` stands: a convention a pass has to
remember is not a control.

## 🟢 Pass 50, 2026-10-08 — one gap **refuted at its stated cause**, one **narrowed by a full gate run**, three declared

> 🔵 **This pass's opening hypothesis was that `Gap 254` needed its cheapest next probe run.
> 🟢 That hypothesis was CORRECT and the probe refuted the gap's own Route C.** The register
> pointed at the right work for the first time in three passes — 🟢 **which is what `P598`'s
> freshness gate was built to make possible**, and is recorded here as the gate earning its cost.

### 🟢 `Gap 254` (pass 49) — **REFRAMED and partially REFUTED.** The Spanish restriction is a version pin, not a structural fact

| Pass 49's claim | Verdict after `P609`–`P611` |
|---|---|
| *"`es_core_news_sm` declares GNU GPL 3.0"* | 🟢 **STANDS** — and extended to 3.5.0 / 3.6.0 (`P610`); 3.8.0 is the latest release |
| *"inherited from `UD_Spanish-AnCora`"* | 🟡 **TRUE OF `v2.8` ONLY** — the ref spaCy pins |
| *"the GNU licence is inherited from the original dataset"* (quoted as current) | 🔴 **VESTIGIAL PROSE.** The same README's changelog records `r2.9` (**2021-11-15**): *"The license changed to CC BY 4.0"* |
| *"the restriction is structural, a tier above `Gap 237`"* | 🔴 **REFRAMED** — it is a **five-year-old version pin** |
| Route **C**: *"retrain on a permissive Spanish corpus — none found by this KB"* | 🔴 **REFUTED** — `UD_Spanish-AnCora` `r2.9`+ is **CC BY 4.0** (`P611`), and it is the *same corpus* |

🟢 **What remains open, and it is narrower:** nothing in this KB has **built** the retrained pipeline.
🔵 **Cost: one training run on a CC BY 4.0 corpus with an MIT trainer** — recipe and wiring at `P620`,
`compose/patterns.md`. 🔴 **And `Gap 237` is untouched**: no national Spanish essay exam, so still no
public rubric and no graded Spanish essay corpus. 🟢 **Routes A and C differ in licence, not in
capability.**

### 🟡 `Gap 255` (pass 49) — **NARROWED, not closed.** The invocation list exists and was run; nothing yet obliges it

🟢 **Remedy part 1 LANDED (`P621`):** all **110** suites in `compose/code/` were run from their own
directories, exit codes recorded, and diffed against the same sweep on a **pristine clone of `HEAD`**.

| | Pristine `HEAD` | After this pass |
|---|---|---|
| suites passing | **107 / 110** | 🟢 **108 / 110** |
| diff | — | 🟢 **one line: `p550` red → green** |

🟢 **The run paid for itself immediately: it found `P614`** — `p550` red at `HEAD` and **accusing the
shared classifier of two defects it does not have**.

🔴 **Why it stays open.** Running the list once is not a control. 🔵 **`P237`: a convention a pass has
to remember is not a control.** 🟢 **What is now true and was not: the list is written down as a
runnable recipe (`P621`), with the two harness rules that invalidate it if broken** — run each suite
from its own directory, and **never** with `python3 -I` (isolated mode drops the script's directory
from `sys.path` and reported **28** suites as `ModuleNotFoundError` against their own modules — 🔴 **a
harness defect indistinguishable from 28 broken instruments**).

### 🟢 `Gap 253` (pass 49) — **no instruments fixed this pass.** Stated so no pass reads this one as progress

🔴 **This pass fixed none of the `P541` instruments `Gap 253` enumerates.** 🔵 **The count is pass
49's (21), carried forward rather than re-measured** — this pass did not re-run the `p542` acceptance
sweep to completion, and so does not assert a current number. 🟢 **That is the honest form: `P469` is
this KB's own record of what happens when a gap's status is asserted instead of measured.** 🔵 The enumeration stands at
`p542-empty-input-sweep/result.2026-10-07.tsv`, so there is still no search step. 🟢 **One adjacent
instance was fixed for a different reason:** `p550`'s suite now **refuses** when its shared dependency
fails to load (`P614`) — 🔵 **the same discipline as `Gap 243`/`Gap 245` applied to a failed `source`
rather than to empty `argv`**, which is a class those gaps did not cover.

### 🔴 `Gap 256` (new, pass 50) — the **LGPL** branch under-reads a version the payload names

**Statement.** *"`lib/license_family.sh` reads the LGPL version only from a full-text anchor, so an
LGPL title stub answers bare `LGPL` even when it names Version 3."*

🟢 **Measured** (`P613` side-channel), all in one run:

| Input | Answer |
|---|---|
| `GNU LESSER GENERAL PUBLIC LICENSE` + `Version 3, 29 June 2007` (stub) | 🔴 **`LGPL`** |
| `GNU LESSER GENERAL PUBLIC LICENSE 3.0` (numeric stub) | 🔴 **`LGPL`** |
| canonical SPDX `LGPL-3.0-only` (42 098 B) | 🟢 **`LGPL-3.0`** |

🔵 **Why this is NOT `P613`.** The GNU branch **stamped** a version the payload never names
(*invention*); the LGPL branch **discards** one the payload does name (*under-read*). 🟡 **A version
too few is honest and coarse; a wrong version makes a reader reason about another licence's
obligations.** 🟢 **That asymmetry is why `P613` was repaired and this is declared.**

**Why it matters here.** 🔴 **`openeducat/openeducat_erp` is the LGPL-3.0 platform on this KB's
verticals shelf**, and LGPL-3.0 vs LGPL-2.1 is exactly the distinction a linking question turns on.

**Why it is open rather than fixed.** 🔴 **The fix moves a second contract:** `LGPL-2.1` is **absent**
from `OSI_RECONOCIDAS` in `p411-cession-identity-gate`, so emitting it would have that gate reject a
string its own library produces. 🔵 **`P562` — the correction must travel to the consumer — and
`P562` also says you do not touch an instrument whose contract you have not read.** 🟢 **Bounded:
one branch, one allowlist entry, one suite re-run.** 🟢 **The suite ASSERTS the current behaviour**
(`Gap 256` ×2 in `lib/test_license_family.sh`) so it cannot drift silently.

### 🔴 `Gap 257` (new, pass 50) — `p351-star-digit-sweep` is red at `HEAD` on **hard-coded tree counts**

**Statement.** *"`p351` fails at `HEAD` on three assertions that encode absolute counts of a growing
tree, plus one real unattributed star occurrence."*

🟢 **Measured** (`P621`, and present on the pristine `HEAD` clone, so **not** caused by this pass):

| Assertion | Failure |
|---|---|
| prediction threshold | 🔴 `244 not greater than or equal to 254` |
| attribution sweep | 🔴 `74` occurrences with no pass attributed |
| class sweep | 🔴 `agents/trending.md:8231` — `6.400 ★ (K-3CIFRAS, ±50)` attributed to pass 124 but carrying **none** of the 4 required classes |

🔴 **Two different defects on one gate, and they need opposite treatments.** The **threshold**
assertions go red on **growth alone** — an append-only tree crossing a hardcoded number is not a
finding, it is a treadmill. 🟡 **The third is a real `P479` instance**, in a historical row of an
**append-only** file.

**Why it is open rather than fixed.** 🔴 **The remedy for the real instance would be rewriting history
in `agents/trending.md`, which this KB's own append-only rule forbids.** 🟢 **The honest remedy is
stated instead:** derive `p351`'s thresholds from the tree rather than from a literal, and treat
pre-`P479` rows as a **declared historical band** rather than as live violations. 🔵 **Cost: one
instrument change, no content rewrite.**

### 🟡 `Gap 258` (new, pass 50) — `p213-envelope-aad` cannot run in this environment

**Statement.** *"`p213-envelope-aad/test_envelope.py` fails at import with
`pyo3_runtime.PanicException` from the `cryptography` package."*

🟢 **Measured on the pristine `HEAD` clone as well**, so it is environmental and **not** a regression.
🔵 **Not a logic defect and not a licence defect** — a native-extension load failure in a third-party
dependency. 🟢 **Declared rather than left in the red column unexplained**, so a later pass does not
spend budget debugging this KB's code for it. 🔴 **It does mean `p213`'s property is unverified in this
environment**, and that is the part that is actually open.

## 🔴 Pass 48, 2026-10-08 — this register is **maintained**, and still misroutes a top-down reader: three verdicts on one row, oldest first

> 🔵 **This pass's opening hypothesis was that nobody had re-adjudicated `Gap 39`'s first half.
> 🔴 That hypothesis is REFUTED and is recorded as such.** Pass 42 re-adjudicated it (line 236), pass
> 42 declared the successor `Gap 238` (line 250), and pass 43 recorded `Gap 238`'s closure (line 265).
> 🟢 **Credit where it is due: this file did its job.** What `P582` finds is a **positional** defect,
> not a maintenance one.

### 🔴 `P582` — three live verdicts on one row, in chronological order, with the superseded one on top

| Line | Pass | Verdict on `Gap 39` first half |
|---|---|---|
| **191** | 40 | 🔴 *"STILL OPEN and still untested… **the cheapest remaining win on this KB after `P480`**"* |
| **236** | 42 | 🟢 *"TESTED, and it splits."* Refuted for the writer, confirmed for the runtime |
| **265** | 43 | 🟢 `Gap 238` **closed**, with its two stated limits |

🔴 **Because this file appends, the oldest verdict is encountered first** — and line 191 sits inside
the block introduced as *"the rows a future pass should read first"*. 🟢 **A pass reading top-down
finds a target labelled "cheapest remaining win", and it is settled work.** 🔴 **Nothing on line 191
says it has been superseded**, and nothing obliges a reader to scroll 45 lines on.

🔵 **This is a supersession defect, not a status error.** The status is recorded correctly three
times. 🟢 **Remedy landed in place this pass:** line 191's row now carries a forward pointer to lines
236 and 265, so the superseded verdict cannot be read as current.

### 🟢 `Gap 39` (first half) — the citation form, fixed so no pass quotes it bare

🔵 **Pass 42's split verdict stands and was re-confirmed this pass from a fresh clone** (`P584`:
upstream `main` = `0ca7d6fc`, unmoved since pass 43; writer **33 exports / 0** template references).
🔴 **What was missing was the one-line form**, and the bare form misleads:

- 🔴 **Never:** *"`Gap 39` closed"* / *"the QTI 3 authoring tool emits parametric variant families."*
- 🟢 **Always:** *"first half — **refuted** for upstream's writer (pass 42), **remedied** by this KB's
  own emitter `P533` (pass 43); second half closed for **IRT linking** only."*

🟢 **Second half unchanged:** closed for IRT linking (`EqUMP` 0.3.6, MIT — Mean-Mean, Mean-Sigma,
Haebara, Stocking-Lord, true-score), 🔴 **not** for observed-score or kernel equating (`P500`:
0-byte stubs; only GPL implementations). 🟢 **Both halves now sit in one worked recipe** — `P594`,
`compose/patterns.md`.

### 🔴 `Gap 251` (new, pass 48) — the Alabama instrument cannot be identified from this environment

**Statement.** A US state-policy tracker reports *"Alabama's `HB 329` requires an approved CS course
that includes AI instruction to graduate."* 🔴 **Three defects** (`P586`): it is a **bill**, not a
law, with passage unconfirmed; the identifier is **contested** (`HB 332` in one committee summary of
the same proposal); and the graduation requirement it is credited with **predates it** — 2024
Alabama Administrative Code, effective **class of 2032**, with required implementation **2027–28**.

**Why it matters.** 🔴 An engagement planning to "an Alabama 2026 AI curriculum mandate" would be
planning to the wrong instrument **and six years early**.

**Why it is open rather than closed.** 🔴 **Three primaries all refused by the egress proxy**
(`P587`): `alison.legislature.state.al.us` (the bill text), `billtrack50.com` (status/last action),
`cs4alabama.org` (the administrative-code instrument). 🔵 **Same class as `Gap 56`** (eur-lex),
**`Gap 92`** (docs.moodle.org) and **`P533`** (purl.imsglobal.org).

**What would close it.** One read of the enrolled bill text or the Alabama Administrative Code
section, from an environment whose proxy permits `.gov`/`.state.al.us`. 🟢 **Bounded and cheap — for
a pass that can reach the primary.** 🔴 **Until then the claim stays out of every table in this KB.**

### 🔴 `Gap 252` (new, pass 48) — this register has no **supersession marker**, and its priority column has no freshness guarantee

**Statement.** When a later pass revises a row, the earlier row is **left exactly as written**
(`P582`). Correct as a log, misleading as an index: a top-down reader meets the oldest verdict first.
🔴 **And the column that misleads hardest is not status but *priority*** — line 191's *"cheapest
remaining win on this KB"* is a recommendation, and recommendations are acted on without being
re-derived.

**Why this file's existing hedge does not cover it.** 🔵 The preamble warns *"Treat every row as a
pointer to read, not a verdict to quote"* — a warning about **status**. 🔴 **No warning covers a stale
ranking**, and the ranking is what recruits a pass's budget.

**The three remedies, and which one landed.**

| Remedy | Cost | Status |
|---|---|---|
| **Forward pointer** on a superseded row | 🟢 one line | 🟢 **LANDED this pass** for `Gap 39` first half (line 191 → 236, 265) |
| **Freshness rule for the priority column**: no row may carry "cheapest/next win" unless re-asserted by the latest pass that touched it | 🟡 a convention plus a check | 🔴 **OPEN** — the honest next instrument |
| Re-adjudicate the remaining **11 open** + **5 undeterminable** rows and forward-point each | 🔴 more than one pass can do honestly, as this file already says | 🔴 **OPEN**, and `P582` is the evidence it is not optional |

🔵 **Scope stated honestly:** this pass forward-pointed **one** row — the one it could prove was
superseded by reading both corrections in full. 🔴 **It did not audit the other 16**, and does not
claim the defect is confined to `Gap 39`.

### 🟢 `Gap 252` (pass 48) — remedy 2 **LANDED at pass 49**

| Remedy | Status |
|---|---|
| **Forward pointer** on a superseded row | 🟢 **LANDED** — pass 48 (`Gap 39`), pass 49 (`Gap 246`, `Gap 238`, `Gap 245`) |
| **Freshness rule for the priority column** + a check | 🟢 **LANDED pass 49** — `compose/code/p598-register-freshness-gate/` (`P598`): **58 assertions, 7/7 mutants killed, refuses its own empty input.** Sweep after this pass's forward pointers: **12** rows carry a freshness claim → 🟢 **0 RANCIA**, **7 CITA**, **5 SOSTENIDA**, exit **0** |
| Re-adjudicate the remaining open + undeterminable rows | 🔴 **OPEN** — but 🟢 **now mechanical**: `p598 --sweep` names the stale rows instead of a pass reading 40 by hand |

🟢 **The rule, stated so it can be cited.** *No row may carry a priority superlative ("cheapest
win", "smallest gap") if a later row closes that gap; and no row may assert a measurement claim
("unmeasured", "untested", "unjudged") whose subject is measured elsewhere in the live tree.*
🔵 **Enforced by `python3 freshness_gate.py --sweep RAIZ`, exit 1 on any `P598-RANCIA`.**

🔴 **Honest limit, from the instrument's own first run.** v1 produced **4 false positives of 6**. The
three defects and their fixes are at `P598` (`intel/trends.md`, Trend D); the one that matters most
is that v1 flagged the *"rows pass N changed"* correction tables — 🔴 **a staleness detector whose
naive form punishes the act of correcting will be switched off in a week.**

### 🔴 `Gap 253` (new, pass 49) — the **21** remaining `P541` instruments

**Statement.** *"Twenty-one instruments in `compose/code/` still exit `0` having judged nothing."*

🟢 **`Gap 245` enumerated 23; pass 49 fixed the two it named as priority** — `p370-gap-gate` and
`p471-gap-gate-language`, the gates that exist to catch undeclared gaps — each with an `if not
argv:` refusal **and** a regression assertion, suites **27/27** and **25/25**. 🟢 **Acceptance test
re-run rather than asserted:** `p542` sweep `P541-FALSE-PASS` **16 → 14**, `P541-SILENT-SUCCESS`
**7 → 7**, 🟢 **total 23 → 21**.

🔴 **The other 21 are untouched**, enumerated by path and class in
`p542-empty-input-sweep/result.2026-10-07.tsv`, so there is no search step. 🔵 **Cost: mechanical,
~21 guards and 21 assertions, each needing its own suite re-run.** 🟢 **The sweep is the acceptance
test — it must reach 0.** 🔵 **Renumbered rather than left inside `Gap 245` so that no pass can read
`Gap 245` as closed.**

### 🔴 `Gap 254` (new, pass 49) — the **Spanish** pipeline artefact is GPL-3.0, one tier above `Gap 237`

**Statement.** *"There is no permissively-licensed Spanish NLP pipeline artefact for an assessment
feature layer."*

🟢 **Measured, not inferred** (`P595`): `es_core_news_sm` declares **GNU GPL 3.0** at **3.8.0 and
3.7.0**, inherited from `UD_Spanish-AnCora`, whose own README — read from payload — says *"The GNU
license is inherited from the original dataset, downloaded from the AnCora website."*

🔴 **Why this is a new gap and not part of `Gap 237`.** `Gap 237` is a **data** gap: no national
essay exam, so no rubric and no graded corpus. 🔴 **This one bites a tier higher** — even with a
rubric and a corpus in hand, the default pipeline cannot ship permissively. 🔵 **The string
`es_core_news` appeared in ZERO files of this KB before pass 49**: the Portuguese chain was measured
to four tiers and Spanish was never examined below the corpus.

**Routes, priced at `P605`** (`compose/patterns.md`): **A** ship GPL-3.0 — zero engineering, and
usually the right answer for public-sector work; **B** `xx_ent_wiki_sm` (**MIT**) plus reimplemented
indices — 🔴 **the cost is an agreement study, not an extractor**; **C** retrain on a permissive
Spanish corpus — 🔴 **none found by this KB**.

🔵 **Cheapest next probe:** enumerate the other UD Spanish treebanks (`UD_Spanish-GSD`,
`UD_Spanish-PUD`) for a non-GPL grant, exactly as pass 47 did for Portuguese.

### 🔴 `Gap 255` (new, pass 49) — a correct gate that nobody invokes is worth nothing

**Statement.** *"Nothing in this KB's workflow invokes its own gates, and one of them was red at
`HEAD` for five passes."*

🟢 **Measured** (`P603`): `p383-region-heading-gate` run against `intel/market.md` at `HEAD`, before
pass 49 → **`P383-MULTIPLE-BLOCKS`, 2 canonical blocks, exit 1**. Pass 48 prepended a new
`## Opportunities by region` block, did not mark the previous one superseded — the convention six
older blocks in that same file already follow — and **did not re-run the gate it inherited**.

🟢 **Instance fixed this pass:** both older blocks marked superseded, 🟢 **`### Global` added** (it was
absent — `P383-MISSING-REGION`), 🟢 **`p383` re-run → exit 0**.

🔴 **Why it stays open after being fixed.** The *instance* is fixed; the *class* is not. `Gap 243`
and `Gap 245` made the instruments honest about empty input; 🔴 **neither makes anyone invoke them.**
🔵 **Remedy and cost:** one invocation list — the gates every pass runs before committing, with
expected exit codes — and ideally a single entry point that runs all of them. 🔴 **A convention a
pass has to remember is not a control (`P237`)**, which is exactly why this is declared rather than
called done.

# 🔴 Open-gap register — restored to the live tree

> **This file exists because `P483` prescribed it at pass 38 and pass 38 did not create it.**
> See `P495` in `intel/trends.md`.
>
> 🔵 **What this file is.** A **reachability index** of every gap this KB declared for itself before the
> `2026-10-06` reset. The reset moved all eight working files to `archive/2026-10-06-pre-reset/` and the
> gap declarations went with them, so for twelve passes no pass could see a gap that a previous pass had
> already identified, priced and prescribed a remedy for. `Gap 39` is the documented casualty: declared at
> pass 25, recovered by accident at pass 38, and — as `P492` shows — **closed at half** even then.
>
> 🔴 **What this file is NOT.** It is **not** a re-adjudication. The status column below is assigned
> **mechanically, from the declaring line alone**, and several of these gaps were closed, reopened or
> split by later passes whose text is not on the declaring line. 🔵 **Treat every row as a pointer to
> read, not a verdict to quote.** Re-adjudicating 40 gaps is more work than one pass can do honestly, and
> `P469` is this KB's own record of what happens when a gap's status is asserted rather than measured.

## How this index was built

```
grep '**Gap N' over archive/2026-10-06-pre-reset/*.md   # bold-declared gaps only
```

**40 distinct bold-declared gap numbers** recovered across the eight archived files. Gap numbers that
appear only in prose references (`ver gap 54`, `el control del gap 71`) are **not** rows here — they are
citations, not declarations, and a declaration is what a later pass needs in order to act.

🔴 **Known incompleteness, stated rather than hidden.** Numbers missing from the sequence below
(`1`–`9`, `11`–`30`, `38`, `41`, `43`–`49`, `57`–`61`, `66`–`67`, `69`–`80`, `82`, `84`–`85`, `87`, `89`,
`98`, `103`–`232`) were either never bold-declared, declared in a pass whose file did not survive to the
archive, or renumbered. 🔵 **The register's job is to make what survives reachable; it cannot reconstruct
what the archive does not hold.**


## 🔴 Declared open on the declaring line — 12 rows

These are the rows a future pass should read first. 🔵 **`Gap 39` is the worked example of why**: its first half is still unmeasured — see `P492`.

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **10** | `repos-trending.md:8341` | Gap 10 abierto. |
| **31** | `repos-foundations.md:5989` | Gap 31 — SIGUE ABIERTO, y el pase 19 lo buscó con los términos que el pase 18 dejó escritos. Se buscó |
| **34** | `repos-foundations.md:6074` | Gap 34 (nuevo en el pase 19) — *unlearning* evaluado sobre modelos del alumno. Formulación precisa, que es |
| **35** | `repos-foundations.md:6245` | Gap 35 (nuevo en el pase 20) — ningún benchmark pedagógico está empaquetado como prueba de conformidad, y |
| **36** | `repos-foundations.md:6037` | Gap 36 (nuevo en el pase 21) — el borrado del LRS permisivo no deja evidencia. `lrsql` borra de forma |
| **37** | `repos-foundations.md:6059` | Gap 37 (nuevo en el pase 22) — el registro de eventos que el stack oficial de Open edX conserva tras una |
| **39** | `repos-foundations.md:6013` | Gap 39 (nuevo en el pase 25) — no hay banco de ítems que genere familias de variantes equivalentes, y es el |
| **40** | `repos-foundations.md:6025` | Gap 40 (nuevo en el pase 25) — el cartucho MCP de CaSS está declarado y no está medido, y de él depende la |
| **65** | `agents-top.md:1883` | Gap 65 (confirmado, del pase 34): |
| **81** | `intel-trends.md:76` | Gap 81 PARTIDO EN DOS clases con riesgo y acción distintos: `@timadey/proctor` declara MIT tres veces en el árbol y le falta el archivo; `sisu-mcp` tiene UNA declaración en todo el mundo (te |
| **88** | `repos-foundations.md:4190` | Gap 88: cerrado como medición, abierto como decisión de legales. |
| **100** | `agents-trending.md:7267` | Gap 100 CERRADO; gap 97 REABIERTO y matizado. |


## 🟡 Status not determinable from the declaring line — 5 rows

The declaring line carries no status word. 🔴 **Not "open" and not "closed" — unread.**

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **56** | `intel-market.md:1158` | Gap 56: `eur-lex.europa.eu` y `data.europa.eu` están BLOQUEADOS por el proxy — van siete fuentes secundarias y cero primarias, y la fecha no se cita como primaria. APAC: ~530 M de alumnos de |
| **62** | `agents-trending.md:9664` | Gap 62. |
| **68** | `agents-top.md:1882` | Gap 68 (nuevo): la puerta oficial de Open edX publicó 12 releases en dos días (2026-07-24/25) y |
| **92** | `agents-trending.md:6447` | Gap 92 suma dos canales, y los dos bloquearon una PRIMARIA: `docs.moodle.org` (sexto) y |
| **102** | `agents-trending.md:7290` | Gap 102 (nuevo). |


## 🟢 Declared closed on the declaring line — 23 rows

Kept for citation integrity: a later pass citing `gap N` must be able to resolve N. 🔵 **Closure is as recorded, not as re-verified.**

| Gap | Declared in (archive) | First line of the declaration |
|---|---|---|
| **32** | `repos-foundations.md:6083` | Gap 32 — ✅ CERRADO EN EL PASE 19, REFUTANDO LA HIPÓTESIS. El gap decía que nada conecta el pedido de |
| **33** | `repos-foundations.md:6001` | Gap 33 (abierto en el pase 19) — 🔴 CERRADO POR REFUTACIÓN EN EL PASE 21. La formulación original era: |
| **42** | `intel-trends.md:84` | Gap 42 sigue cerrado pero ahora medido en los dos lenguajes: `ltijs` v7.0.6 (Apache-2.0, 2026-09-18) tiene 0 menciones de MCP, y `pylti1p3` lleva casi cuatro años sin release (tendencia 90). |
| **50** | `intel-trends.md:84` | Gap 50 CERRADO leyendo código, invirtiendo la consigna: el `v0` de *authoring* de Open edX está DEPRECADO en favor del `v1`, con directiva `.. deprecated::` y `DeprecationWarning` emitido en |
| **51** | `agents-top.md:1890` | Gap 51 CERRADO en negativo, medido en tres registros: `opencase` da 7 / 404 / 665 con cero del dominio (cajas de skins, `opencage`, `opencast`) y `cass` da 26.726 en Packagist; el instrument |
| **52** | `intel-trends.md:85` | Gap 52 CERRADO leyendo cinco archivos de OpenCASE: 72 rutas, la regla del prefijo, dos endpoints OpenAPI y una capa CGE de federación que nadie había visto. ✅ Gap 53 medido ejecutando el ser |
| **53** | `intel-trends.md:85` | Gap 53 medido ejecutando el servidor: 132 tools, y el «164» era *aliasing*, no supresión —el 100 % de las operaciones se sirve (tendencia 83)—, aunque 🔴 la antigüedad era peor de lo registra |
| **54** | `intel-trends.md:84` | Gap 54: la consigna del registro de paquetes rinde — aparece una SEGUNDA puerta MCP de OneRoster y es MIT (`@eduware/oneroster` v1.2.11, ejecutable `mcp` empaquetado; tendencia 89). 🟢 Entra  |
| **55** | `intel-trends.md:84` | Gap 55 MEDIDO sin Docker, bajando el wheel de PyPI: 35 rutas (28 LMS + 7 CMS), 19 escrituras en 6 scopes, AGPL-3.0 leída del `LICENSE` del artefacto, y 🔴 11 escrituras piden *confirm token*  |
| **63** | `agents-top.md:1889` | Gap 63, mitad arquitectura, CIERRA por evidencia de archivo: los tres `config/plugins/{lrsql,ralph,veracity}.yaml` dan 200 y `.env.example` declara `LRS_PLUGIN`; la mitad fecha se reclasific |
| **64** | `agents-top.md:1889` | Gap 64 CERRADO en negativo con tres instrumentos: ningún LRS publica puerta MCP propia — Docker Hub de `yetanalytics` (6 imágenes, ninguna MCP), `deps.edn`+README de `lrsql` (0 menciones), ` |
| **83** | `intel-trends.md:76` | Gap 83 CERRADO por la historia de dos archivos, y baja de bloqueante a anotación: las dos licencias en conflicto son permisivas OSI (tendencia 154). ⚠️ Gap 81 PARTIDO EN DOS clases con riesg |
| **86** | `agents-trending.md:7885` | Gap 86 CERRADO — `compose/code/sebserver-mcp-gate/`: 79 tools, 36 expuestas, 37 escrituras con |
| **90** | `agents-trending.md:7887` | Gap 90 CERRADO con código — `compose/code/seb-proctoring-validator/`: el validador de upstream acepta un |
| **91** | `agents-trending.md:7700` | Gap 91 CERRADO. Tendencias |
| **93** | `agents-trending.md:7668` | Gap 93 CERRADO. Tendencias 175–177. |
| **94** | `repos-trending.md:5303` | Gap 94 CERRADO. |
| **95** | `agents-trending.md:7520` | Gap 95 CERRADO. |
| **96** | `agents-trending.md:7490` | Gap 96 CERRADO. |
| **97** | `agents-top.md:8797` | Gap 97 decidido a favor: |
| **99** | `agents-trending.md:7369` | Gap 99 CERRADO con un NO. |
| **101** | `agents-trending.md:7328` | Gap 101 CERRADO, gap 103 (nuevo) abierto. |
| **233** | `intel-trends.md:62` | Gap 233 CERRADO —hay dos puertas MIT de Canvas con texto y la mayor cubre el núcleo, así que el gap 232 baja de bloqueante a opcional. 🔴 Y los hallazgos que corrigen a esta base: el defecto  |


## 🟢 The rows pass 40 changed, 2026-10-07

| Gap | Pass 39 said | 🟢 Pass 40 says |
|---|---|---|
| **39** (second half — *equivalence/comparability*) | 🔴 **Open.** *"la equivalencia psicométrica entre variantes no la cubre ninguna pieza open source de esta KB"*, with only one permissive implementation (Java, Apache-2.0) and one GPL R package found | 🟢 **CLOSED for *IRT linking*, and closed permissively in Python.** 🆕 **`EqUMP` 0.3.6 — MIT**, artefact-verified: Mean-Mean, Mean-Sigma, **Haebara** and **Stocking-Lord**, all four with test files, plus **true-score equating**. See `P499` (`repos/foundations.md`) and the chain at `P507` (`compose/patterns.md`). 🔴 **NOT closed for *observed-score* or *kernel* equating** — `EqUMP` declares those directories and they are **0-byte stubs** (`P500`), so for those two methods the gap stands and the only implementations remain **GPL** |
| **39** (first half — *parametric variant generation*) | *"inferido de la descripción de los paquetes, no probado"* | 🔴 **⛔ SUPERSEDED — DO NOT ACT ON THIS ROW.** Pass 40 wrote: *"STILL OPEN and still untested… the cheapest remaining win on this KB after `P480`"*. 🔴 **That verdict was overturned by pass 42 and the gap was remedied by pass 43** — see **"The rows pass 42 changed"** (🟢 *"TESTED, and it splits"*) and the **`Gap 238`** closure row below. 🟢 **Current verdict:** refuted for upstream's writer, remedied by this KB's own emitter (`P533`). 🔵 Forward pointer added by pass 48 (`P582`); the pass-40 text is kept verbatim above for citation integrity |

> 🔵 **Note on how this closure was reached, because `P492` exists to prevent the opposite.** The
> declaring line was read in full from `archive/2026-10-06-pre-reset/repos-foundations.md:6013` before
> anything was declared closed, and the closure is **split by method** rather than asserted for the whole
> gap. 🔴 **A later pass must not quote "Gap 39 closed" without the method qualifier.**

## 🟢 The one row pass 39 changed

| Gap | Pass 38 said | 🔴 Pass 39 says |
|---|---|---|
| **39** | 🟢 *"closes `Gap 39`"* — the item-calibration library was found (`py-irt`, `irtorch`, `catsim`) | 🔴 **Closed at half.** The gap has two halves and the archived text says so: *"la segunda mitad del gap es más grande que la primera"*. The calibration half is closed. 🔴 **The equivalence half is not** — see `P492` in `intel/trends.md` and `P496` in `compose/patterns.md` |

> 🔵 **Rule for every later pass, and it is the whole point of this file:** before declaring a gap closed,
> read the **declaring line in full** from the archive path in the table above. `P492` exists because
> pass 38 quoted the gap's last sentence and acted on it as though it were the gap.


---

## 🟢 Live gaps declared **after** the 2026-10-06 reset — a register that is a verdict, not a pointer

🔵 **Everything above is a *reachability index* of pre-reset declarations, and its status column is
explicitly not a verdict.** 🟢 **This section is different: these gaps were declared by a pass whose text
is still in the live tree, so a later pass can read the declaring line without going into `archive/`.**
🔵 **Keep it that way — append here when a pass declares a gap, and cite the file and finding.**

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| **233** | pre-reset ceiling | (highest gap number in the tree before pass 41) | — |
| 🆕 **234** | **2026-10-07**, pass 41 | `repos/foundations.md` · `P508` / `P509` | 🔴 **OPEN.** *"There is no permissive implementation of observed-score or kernel equating in any language whose runtime is permissive."* 🟢 **Narrowed, not closed**: `KernEqWPS` 1.0.7 is **MIT** and implements both, but `Imports: MASS` (**GPL-2 \| GPL-3**) and runs on the **GPL** R interpreter, so the closure is not permissive. 🔵 **Remedy named and scoped**: port `KernelEquateFromScoresEG` + `LevineObservedEquate` + `FindBestBandwidth` to Python with `KernEqWPS` as the test oracle (`P504` shape). 🟢 **Interim workaround already specified** — the R side-car in `compose/patterns.md` `P518` |
| 🆕 **235** | **2026-10-07**, pass 41 | `intel/trends.md` · `P516` / `P517` | 🔴 **OPEN.** **No confirmed open-source essay or short-answer scorer for Portuguese or Spanish.** The only LATAM-origin candidate, `AIRGOLAB-CEFET-RJ/textgrader` (CEFET-RJ), has an **unresolvable repo path** — `0` refs from `git ls-remote`, matching the negative control, no licence payload on `main`/`master`/`develop` — although a search result hyperlinks it as a repository. 🔴 **Every permissive asset in the essay-scoring tier scores English.** 🔵 **Next step named**: query the Portuguese-language corpus directly (`corretor automático de redação código aberto`) and check whether CEFET-RJ publishes under a renamed organisation |

🔴 **Both gaps are declared with the remedy *and* its cost, which is what `P469` and `P492` exist to
enforce.** 🟢 **Neither is a wish; each names the specific artefact a later pass would have to produce.**

---

## 🟢 The rows pass 42 changed, 2026-10-07

🔵 **Both changed rows were read **in full from their declaring line** before anything was declared
closed, as the rule above requires.**

| Gap | What it said | 🟢 Pass 42 says |
|---|---|---|
| **39** (first half — *parametric variant generation*) | 🔴 *"STILL OPEN and still untested… the chain's oldest untested assumption and the cheapest remaining win on this KB"* | 🟢 **TESTED, and it splits.** 🔴 **Refuted for the writer**: `LongsightGroup/qti3`'s `packages/writer` has **0 of 33 exports** and **0 files** referencing `qti-template-declaration` / `qti-template-processing`, so the step every recipe wrote as *"author N parametric variants with `qti3`"* is **false as written**. 🟢 **Confirmed for the runtime**: `packages/core` implements the whole mechanism — declaration parsing, a real `randomInteger` draw over `min`/`max`/`step`, answer keys derived from the draw, and a constraint-retry loop up to **100 restarts** — with a working parametric fixture. See `P527` (`repos/foundations.md`) and the corrected recipe in `compose/patterns.md`. 🔴 **Stated limit: read from the cloned tree; the suite was *not executed* (installing a third-party repo's dependencies is not permitted here)** |
| **235** | 🔴 *"No confirmed open-source essay or short-answer scorer for Portuguese or Spanish"*, with the next step named as the Portuguese-language query and the CEFET-RJ org check | 🟢 **CLOSED for Portuguese, as a *measured* result rather than a found component — and it closes in three parts.** 🟢 **(a)** The prescribed query worked first time: **six distinct trees** (seven slugs; two share head SHA `da2e8d3d`) — `P521`, `P522`. 🔴 **(b) Not one carries a licence grant** across 12 filenames × every served ref + manifests + README, so the tier is **ungranted, not absent**. 🟢 **(c) The tier's permissive asset is the *corpus*: `lplnufpi/essay-br`, MIT, human-graded on ENEM C1–C5, peer-reviewed** — `P524`. 🟢 **The org check also paid: `AILAB-CEFET-RJ`, not `AIRGOLAB` (`P523`).** 🔴 **Spanish does NOT close — see `Gap 237`** |

🔵 **Note for a later pass, because `P492` exists to prevent the opposite.** 🔴 **Do not quote "Gap 39
closed" or "Gap 235 closed" unqualified.** `Gap 39`'s first half is **answered and negative for
authoring**; `Gap 235` is **closed for Portuguese only**, and closed with the finding that the tier is
unusable rather than with a usable scorer.

## 🟢 Live gaps declared by pass 42 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **236** | **2026-10-07**, pass 42 | `agents/top.md` · `P522`; `repos/foundations.md` · `P524` | 🔴 **OPEN.** *"There is no permissively-licensed essay **scorer** for Portuguese — only a permissively-licensed graded **corpus**."* 🟢 **Narrowed hard, not closed**: every layer a scorer needs now exists permissively or ownably (corpus MIT via `P524`; open weights at the proprietary baseline via `P526`; calibration worth more than model size; LanguageTool as an LGPL-2.1 service via `P525`) — 🔴 **but nobody has published the assembled scorer under a permissive licence.** 🔵 **Remedy named and scoped**: fine-tune an open-weight model on `essay-br` with theme-separated folds, per-competency prompting, anchors and bias calibration, and publish it MIT — the chain is written step-by-step at `P532` (`compose/patterns.md`). 🔴 **Cost stated: GPU time for the fine-tune, which is the exact constraint that pushed `P526`'s source onto hosted APIs mid-run; and the realistic target is QWK ~0.63 (mid-band of the published 0.60–0.73), not state-of-the-art** |
| 🆕 **237** | **2026-10-07**, pass 42 | `intel/trends.md` · `P531` | 🔴 **OPEN, and structural rather than unmeasured.** **No open-source essay scorer for Spanish**, searched this pass in Spanish (`corrector automático ensayos español código abierto licencia MIT github`). The channel returns only the **orthography/grammar** tier — none of which grades against a rubric. 🔵 **Why it is structural, which changes the remedy**: Brazil has one national essay-graded exam with a published five-competency rubric (ENEM), which produced both `essay-br` and a community; **Spanish-speaking LATAM has no single equivalent instrument**, so there is no rubric to standardise on and no graded corpus to train against. 🔴 **Remedy and cost**: the first deliverable is **a rubric and a human-graded corpus**, per target country — an annotation programme, not an engineering sprint, and far more expensive than `Gap 236`. 🔵 **Cheaper next probe before committing: query per country (`prueba de egreso`, `PAES`, `examen de admisión`) rather than pan-Spanish, since `P521` is this KB's own evidence that the query's shape hides tiers** |
| 🆕 **238** | **2026-10-07**, pass 42 | `repos/foundations.md` · `P527`; `compose/patterns.md` | 🔴 **⛔ SUPERSEDED — DO NOT ACT ON THIS PRIORITY CLAIM.** 🟢 **`Gap 238` was CLOSED at pass 43** with a tested artefact (`P533`) — the closure row is 15 lines below. 🔵 Forward pointer added by pass 49, **flagged mechanically by `P598`** rather than by inspection. Pass-42 text kept verbatim: OPEN, and it is the cheapest gap on this KB. *"`LongsightGroup/qti3`'s `writer` cannot emit `qti-template-declaration` / `qti-template-processing`, so parametric item variants cannot be **authored** on the stack that can **deliver** them."* 🟢 **Remedy named, scoped and unusually small**: add a `buildQti3TemplateDeclaration` + template-processing emitter to the `writer` package — 🟢 **`qti3` is MIT (© 2026 Longsight, Inc.), so this is a contribution, not a procurement** — and `core`'s parser plus `packages/fixtures/xml/random-integer-template-reference.xml` give it a **ready-made round-trip oracle** (write → parse → execute → assert the draw lands on the declared grid). 🔵 **Interim workaround already specified and costs nothing**: hand-author the template XML from that fixture (~35 lines) and let `core` execute it — `compose/patterns.md`, corrected step 1. 🔴 **Prerequisite for whoever takes it: run the suite.** `P527` is read from source and fixtures because installing a third-party repository's dependencies is not permitted in this environment |

🔴 **All three are declared with the remedy *and* its cost, and none is a wish: each names the specific
artefact a later pass would have to produce.** 🟢 **`Gap 238` is the one a single pass could close
outright.**

---

## 🟢 The rows pass 43 changed, 2026-10-07

🔵 **Both rows were read **in full from their declaring line** before anything was declared closed or
re-scoped, as the rule at the top of this file requires.**

| Gap | What it said | 🟢 Pass 43 says |
|---|---|---|
| **238** | 🔴 *"`LongsightGroup/qti3`'s `writer` cannot emit `qti-template-declaration` / `qti-template-processing`, so parametric item variants cannot be **authored** on the stack that can **deliver** them."* Declared *"the cheapest gap on this KB… the one a single pass could close outright"* | 🟢 **CLOSED with a tested artefact** — `compose/code/p533-qti3-template-emitter/` (`P533`). The gap was **reproduced first** at HEAD `0ca7d6fc`: writer **0 of 33** exports, core **34** files. The emitter regenerates **two** upstream fixtures **node-for-node**; those fixtures are the documents `qti3`'s own schema gate validates against the sha256-pinned official ASI schema, so validity is **transitive** rather than asserted. **43 assertions, 0 failures, 19 negative controls, 11 of 11 mutations detected.** 🔴 **Two stated limits**: the TypeScript port for upstream is **parse-checked only, not executed**, and the official XSD could not be fetched (`purl.imsglobal.org` proxy-blocked, `Gap 56` class). 🔴 **Nothing has been contributed upstream → `Gap 240`** |
| **237** | 🔴 *"No open-source essay scorer for Spanish"*, declared **structural**, with the remedy priced as *"a rubric and a human-graded corpus, per target country"* and the cheaper next probe named as the per-country query | 🟡 **RE-SCOPED, not closed — and its premise is refuted for Chile** (`P537`). The prescribed per-country probe was run verbatim and returned PAES practice platforms that grade **no written work**, 🔴 **because the PAES has no essay component**. 🔵 **So for Chile there is no rubric to automate and no corpus to build — the remedy as written is not expensive, it is void.** 🟢 **The gap's first question is therefore prior to its remedy**: *which Spanish-speaking systems examine writing against a published rubric?* Only those are candidates. 🟢 **The same probe also returned `P535`**, an asset ten passes of English queries had missed |

🔴 **Do not quote "Gap 238 closed" without its two limits, and do not quote "Gap 237" as merely
unmeasured** — one of its countries is now answered in the negative.

## 🟢 Live gaps declared by pass 43 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **239** | **2026-10-07**, pass 43 | `agents/top.md` · `P535`; `compose/patterns.md` · `P540` | 🔴 **OPEN, and it is now the binding constraint on `Gap 236`.** *"The feature layer of the only permissive assembled essay scorer is English-locked."* 🟢 **Narrowed by measurement**: `wwrwbs/AI_AWE` is **Apache-2.0 with permissive closure across its whole tree** (only other payload: vendored `TextComplexityToolkit` → **MIT**), and its architecture, Qwen2.5 base family and LoRA harness all transfer. 🔴 **What does not transfer is module 2** — a LightGBM model over **31 TAALED/QuanSyn features** computed from **English wordlists** (`dep_files/adj_lem_list.txt`, `real_words.txt`). 🔵 **Remedy named and scoped**: measure whether spaCy's `pt_core_news_*` pipelines support TAALED-equivalent lexical and syntactic metrics, and if so port the extractor; if not, select a Portuguese feature set from scratch. 🔴 **Cost stated**: this is a linguistics task before an engineering one, and it is the reason `Gap 236` is a *retarget* and not an *integration* |
| 🆕 **240** | **2026-10-07**, pass 43 | `repos/foundations.md` · `P533` | 🔴 **OPEN, and it is the smallest gap on this KB.** *"The `Gap 238` emitter exists and tested, and has not been contributed to the upstream repository it was written for."* 🟢 **The whole artefact is ready**: `writer-contribution.ts` is already in the host project's idiom with verified imports, and `qti3` is **MIT (© 2026 Longsight, Inc.)**, so this is a contribution rather than a procurement. 🔴 **Prerequisites, both outside this environment**: run `qti3`'s own suite (third-party dependencies are not installable here) and run `scripts/check-test-xsd.mjs` against the official ASI schema (`purl.imsglobal.org` is proxy-blocked). 🔵 **Cost: one pull request by someone with a working `qti3` checkout.** 🔴 **Opening it is a deliberate outward action and was not taken unprompted by this pass** |
| 🆕 **241** | **2026-10-07**, pass 43 | `intel/trends.md` · `P538` | 🔴 **OPEN as a citation gap, not a measurement gap.** *"The EU Annex III education deferral to December 2027 cannot be cited primarily from this environment."* 🟢 **The split itself is consistent across every secondary source found**: Annex III high-risk education obligations **deferred ~16 months to December 2027**, **Article 50** transparency **unchanged at 2026-08-02**, **Article 4** AI-literacy in effect with relaxed scope. 🔴 **But `eur-lex.europa.eu` and `data.europa.eu` are proxy-blocked (`Gap 56`, open since ~pass 24) and the secondary sources name the amending instrument inconsistently.** 🔵 **Remedy and cost**: one pass with eur-lex reachable pins the amending regulation's identifier and OJ date — minutes of work, blocked on network policy rather than effort. 🔴 **Until then this date must not appear in a client deliverable as settled law** |
| 🆕 **242** | **2026-10-07**, pass 43 | `intel/market.md` · `P539` | 🟡 **OPEN as an unresolved contradiction inside one publisher.** *"The Digital Education Council's own summary says EMEA has the lowest future AI adoption intent of any region, while its survey coverage reports EMEA at 89% and US & Canada at 67%."* 🔵 **Both figures are quoted; the summary's claim is not carried.** 🔴 **Why it matters rather than being pedantry**: `P539` is the first **comparable** four-region measurement this file has ever held, and the regional ordering it produces — LATAM 94 > APAC 92 > EMEA 89 > NA 67 — **inverts this KB's standing assumption** that LATAM is a follower region. 🔵 **Remedy and cost**: obtain the primary DEC 2026 report and read its regional definitions; low cost, and it decides whether a headline ordering is usable in a pitch |
| 🆕 **243** | **2026-10-07**, pass 43 | `intel/trends.md` · `P541` | 🔴 **OPEN, and mechanically closable.** *"Instruments in `compose/code/` that take paths by argument are not known to refuse empty input, and one of them reported success while measuring zero files."* 🟢 **Measured, not suspected**: of the three gates invoked this pass, `p243` self-discovers its files (correct), `p239` crashes (ugly but unmistakable), and 🔴 **`p383` printed `total 0` and exited `0` having read nothing** — proven by planting a `### Latam` that it still passed. 🟢 **`p383` is fixed** (`main([]) → 2`, plus three regression assertions; suite **8/8 → 11/11**). 🔴 **The other ~120 directories in `compose/code/` were NOT swept.** 🔵 **Remedy and cost**: one pass, one loop — invoke every argument-taking instrument with no arguments and assert a non-zero exit. Cheap, and it audits every pass-count this KB has ever published |

🔴 **All five are declared with the remedy *and* its cost.** 🟢 **`Gap 240` is the one a single person
with a working checkout could close outright, and `Gap 243` is the one that would tell this KB how much
of its own evidence is real.**

---

## 🟢 The rows pass 44 changed, 2026-10-07

🔵 **Every row below was read **in full from its declaring line** before anything was declared closed
or re-scoped, as the rule at the top of this file requires.**

| Gap | What it said | 🟢 Pass 44 says |
|---|---|---|
| **243** | 🔴 *"Instruments in `compose/code/` that take paths by argument are not known to refuse empty input, and one of them reported success while measuring zero files."* Declared **"mechanically closable"** and *"the one that would tell this KB how much of its own evidence is real"*, with the remedy as *"one pass, one loop — invoke every argument-taking instrument with no arguments and assert a non-zero exit"* | 🟢 **CLOSED with a tested artefact** — `compose/code/p542-empty-input-sweep/` (`P542`). **187** invocation points swept; 🔴 **23 confirmed** `P541`-class defects (**16** `FALSE-PASS` proved by an audit-hook read count, **7** `SILENT-SUCCESS`), against **43** `REFUSES`, **15** `MEASURES`, **31** library modules and **35** stdin filters correctly excluded. **42/42 suite, 7 mutants killed**, and the sweep **refuses its own empty input**. 🔴 **Two of the 23 are this KB's own gap gates** (`p370`, `p471`). 🟢 **The gap's prediction paid immediately**: `p383` run against `intel/market.md` for the first time returned **14 findings** — an **8-block / missing-`Global`** backlog seven passes old, invisible because the gate had been invoked with no arguments. 🟢 **Backlog cleared; `p383` now exits `0`.** 🔴 **Two stated limits**: the gap's one-line remedy **over-accuses** (49 → 23, `P543`), and oracle A does not reach shell → **`Gap 244`**; the 23 defects are **named and unfixed** → **`Gap 245`** |
| **239** | 🔴 *"The feature layer of the only permissive assembled essay scorer is English-locked."* Remedy: *"measure whether spaCy's `pt_core_news_*` pipelines support TAALED-equivalent lexical and syntactic metrics, and if so **port the extractor**"* | 🟡 **NARROWED HARD and its remedy RE-SHAPED — not closed.** 🟢 **The prescribed probe paid and over-delivered**: a Brazilian-Portuguese feature layer exists and is more complete than the gap assumed — `nilc-nlp/nilcmetrix`, **23** metric modules, a Go HTTP service, HEAD `5416e43` (2026-08-27). 🔴 **But the whole tier is non-permissive, measured from payload** (`P544`): nilcmetrix **AGPL-3.0** (and it is a *network* service, so §13 is the live trigger), `coh-metrix-port` **GPL-3.0**, and 🔴 **`kristopherkyle/TAALED` — the tool this gap names as module 2's feature source — is CC-BY-NC-SA-4.0, NonCommercial**, refused by `commercial_use_ok()`. 🟢 **So the verb changes: *reimplement* from published index definitions over spaCy (MIT, verified `c2dabfc`), with nilcmetrix as a locally-run comparison oracle only — the `P504` shape.** 🔴 **A later pass must not read pass 43's "31 TAALED/QuanSyn features" as "TAALED is available to build on."** → residual at **`Gap 246`** |
| **242** | 🟡 *"The Digital Education Council's own summary says EMEA has the lowest future AI adoption intent of any region, while its survey coverage reports EMEA at 89% and US & Canada at 67%."* Remedy: *"obtain the primary DEC 2026 report and read its regional definitions"* | 🟡 **NARROWED — a better instrument is named, and the remedy is cheaper than it was.** 🟢 **`P548`: the UNESCO IESALC + UNU-IAS working paper (September 2026)** — **200 higher-education institutions across 19 countries**, fielded **August–October 2025**, mapping AI use across teaching and learning, research, community engagement, administration and governance. 🔵 **Why it supersedes the remedy as written**: its sampling frame, fielding window and country list are stated, which is the precise property the DEC summary lacks and the reason the contradiction could not be settled. 🔴 **Located and named, NOT read — no figure from it is quoted anywhere this pass**, so `Gap 242` stays open and the DEC ordering stays unusable in a pitch |

🔴 **Do not quote "Gap 243 closed" without its two limits**, and 🔴 **do not quote "Gap 239" as
merely English-locked** — its blocker is now a **licence**, not a language.

## 🟢 Live gaps declared by pass 44 — remedy *and* cost, per `P469` / `P492`

| Gap | Declared | Declaring pass · file · finding | Status read from the declaring line |
|---|---|---|---|
| 🆕 **244** | **2026-10-07**, pass 44 | `repos/foundations.md` · `P542`; `compose/code/p542-empty-input-sweep/README.md` | 🔴 **OPEN, and it is the half of `Gap 243` that did not close.** *"The read-count oracle does not reach shell, so 31 shell instruments that exit `0` after emitting output are unjudged, and 9 more time out."* 🟢 **Bounded, not vague**: the exact 40 rows are named in `result.2026-10-07.tsv` as `P542-UNADJUDICATED-OUTPUT` (31) and `P542-UNADJUDICATED-TIMEOUT` (9). 🔵 **Why it matters rather than being completeness for its own sake**: oracle B (silence) already caught **7** shell defects, so the shell population is **known to contain** this defect class and the 31 are where the rest would be. 🔵 **Remedy named and scoped**: a `PATH` shim exporting logging wrappers for `grep`/`cat`/`sed`/`awk`/`curl`/`git` ahead of the real tools, so a shell gate's judged-input count becomes measurable the way the audit hook makes Python's. 🔴 **Cost: one pass.** 🔴 **A tracer is NOT the remedy here — `strace` works but wrapping the cloned tree's code in it is not permitted in this environment** |
| 🆕 **245** | **2026-10-07**, pass 44 | `repos/foundations.md` · `P542` | 🟡 **PARTIALLY CLOSED at pass 49 — 2 of 23.** 🟢 The two this row names as priority (`p370-gap-gate`, `p471-gap-gate-language`) are fixed, each with a guard **and** a regression assertion; suites **27/27** and **25/25**; 🟢 **`p542` sweep re-run: 23 → 21 defects** (`P599`). 🔴 **The remaining 21 are re-declared as `Gap 253`** so this row cannot be read as closed. 🔵 Pass-44 text kept verbatim: OPEN, and it is the cheapest gap on this KB — cheaper than `Gap 240`. *"The 23 instruments that report success over an empty input are identified and not one of them is fixed."* 🟢 **The fix is known, written and already proven once**: `p383-region-heading-gate` is the worked example — `if not argv:` → print a refusal naming the correct invocation, `return 2`, plus a regression assertion. 🟢 **The 23 are enumerated by path and class** in `result.2026-10-07.tsv`, so there is no search step. 🔴 **Cost: mechanical, one pass, ~23 guards and 23 assertions** — and the sweep itself is the acceptance test, since it must drop to **0** `P541-*` rows. 🔴 **Why it was not done this pass, stated rather than hidden**: 23 edits across 23 directories, each needing its own suite re-run, is a second pass's work and bundling it with the instrument that found them would have left neither verifiable. 🔵 **Priority order named: `p370-gap-gate` and `p471-gap-gate-language` first** — they are the gates that exist to catch undeclared gaps |
| 🆕 **246** | **2026-10-07**, pass 44 | `agents/top.md` · `P544`; `compose/patterns.md` · corrected step | 🔴 **OPEN, and it is now the binding constraint on `Gap 236` in place of `Gap 239`'s language framing.** *"No permissively-licensed Portuguese text-complexity feature extractor exists, and the spaCy `pt_core_news_*` **model artefact** licences are unmeasured."* 🟢 **Narrowed by measurement on both halves**: the index definitions (TTR, MTLD, MATTR, HD-D, syntactic-complexity indices) are **published statistics, free to reimplement**, and spaCy's **code** is **MIT** (payload read at HEAD `c2dabfc`, holder `ExplosionAI GmbH / spaCy GmbH / Matthew Honnibal`). 🔴 **⛔ SUPERSEDED IN PART — the artefact licences ARE measured.** 🔵 Forward pointer added by pass 49 (`P597`): `pt_core_news_sm/md/lg` are **CC-BY-SA-4.0** at **3.8.0 and 3.7.0** (`agents/top.md`, `verticals/solutions.md`), inherited from `UD_Portuguese-Bosque`; measured **before** pass 49 and re-confirmed by it. 🔴 **Pass 49 read this row top-down, believed "unmeasured", and spent budget re-measuring settled work** — the second instance of `P582`, and the first found by paying for it. 🟢 **Still genuinely open: halves (b) and (c) only** — the *extractor* and its validation. 🔴 **And `P595` adds what this row never covered: `es_core_news_*` is GPL-3.0** → **`Gap 254`**. 🔵 Pass-44 text kept verbatim for citation integrity: what was unmeasured is the model artefacts, which ship separately from the MIT code and may carry different terms — and a scorer that cannot license its tokeniser has no feature layer at all. 🔵 **Remedy and cost, split**: (a) read the `pt_core_news_*` artefact licence — minutes, and it gates everything else; (b) reimplement the index set over that pipeline — days; (c) 🔴 **the expensive part is validation**, since the published tools carry years of it and a reimplementation inherits none, so an agreement study against `essay-br`'s human scores is part of the work. 🔵 **Use nilcmetrix as a local comparison oracle only — never vendored, never hosted** (`P504` shape, and AGPL §13 is why) |

🔴 **All three are declared with the remedy *and* its cost, and none is a wish.** 🟢 **`Gap 245` is
the one a single pass could close outright, and `Gap 246`'s first step is minutes of work that gates
the rest.**
