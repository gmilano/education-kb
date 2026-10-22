---
industry: education
region: Global
updated: 2026-10-22
---

## 🟢 2026-10-22 · `p380` — **two recipes added, and both are built on the same discovery: what three legal systems regulate is the DECISION, so the human-review boundary is the architecture. 🟢 `Pattern 34` makes one assessment pipeline lawful in Brussels, Hanoi and New York. 🟢 `Pattern 35` builds the evidence buyers started asking for in 2026.**

**Evidence:** [`regional-legs`](../evidence/regional-legs.2026-10-22-p380.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-22-p380.tsv) ·
[`payload-upgrade`](../evidence/payload-upgrade.2026-10-22-p380.tsv)

## 🟢 🆕 `Pattern 34` (`p380`) — **One assessment pipeline that is lawful in Brussels, Hanoi and New York, because no grade reaches a student without a human decision record**

🔵 **The problem it solves.** A client wants AI grading across three regions. The EU makes
assessment **Annex III high-risk** from **2 December 2027** (`Regulation (EU) 2026/1744`);
**Vietnam** (Law **134/2025/QH15**, in force **1 March 2026**) makes it high-risk **only when AI
output is the sole basis for a decision without meaningful human review**; **NYC** bars AI from
grading outright in its red tier. 🔴 **Three regimes, one boundary — and a studio that implements
it per region ships three products.** Build the boundary once, in the write path.

| Layer | Component | Licence — **and the channel it was read on** | Grant path | Why this one |
|---|---|---|---|---|
| System of record | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** — 🟡 payload read **this pass**, title line *"GNU GENERAL PUBLIC LICENSE"* verbatim; **bytes not pinned** | `main/COPYING.txt` | The LMS the client already runs; **not vendored** — reached over its API, so the copyleft never touches the deliverable |
| Read boundary | [`AnonymousOnyx22/moodle-student-mcp`](https://github.com/AnonymousOnyx22/moodle-student-mcp) | 🟢 **MIT** `1 072 B`, `ed912ca72d9e` | `main/LICENSE` | 🟢 **Read-only by construction** — *"It can never submit, edit or delete anything"*. The agent physically cannot write a grade |
| Grading proposal | [`Keshav0141/Auto-Assessment-Agent`](https://github.com/Keshav0141/Auto-Assessment-Agent) | 🟢 **MIT** `1 069 B`, `68977affb141` | `master/LICENSE` | Emits a **0–1 confidence per decision** (sampling-based consistency, no logprobs) and flags anything under **0.85** as *needs human review* |
| Write path | [`ibm-skills-network/mark`](https://github.com/ibm-skills-network/mark) | 🟢 **Apache-2.0** `11 357 B` — 🟡 **`p374`'s first-hand read, NOT re-read this pass** | `master/LICENSE` | The only component on these shelves that **returns grades over LTI 1.3** — institutional-grade, and the write is auditable at the standard |
| Rubric reference | [`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment) | 🔴 **grant NOT read on any pass** — `CARRIED` as an address only | — | Rubric-driven grading whose design point is an **audit trail**: prompts, criteria, inputs and outputs all retained |

🟢 **The wiring, and the one rule that makes it lawful in all three.**
1. The agent reads coursework **only** through the read-only MCP boundary. Scope is enforced by
   the component, not by a prompt.
2. The grader produces a **proposal plus a confidence**, never a grade. It writes nothing.
3. **The gate:** a proposal under the threshold goes to a human queue. A proposal over it still
   goes to a human **sign-off that is recorded** — because Vietnam's test is not *"was a human
   available"* but *"was the AI output the sole basis"*.
4. Only `mark` writes, and only on a **human decision record** carrying the reviewer, the
   timestamp, the proposal and the confidence. That record is the compliance artefact in all
   three regimes and the thing an auditor asks for.
5. Retain the rubric audit trail from `genai-open-assessment` beside the decision record.

🔵 **Why it travels.** Switching region changes the **threshold and the queue policy** — not the
architecture. 🔴 **And the inverse is the trap:** a system where the model writes the grade and a
human *reviews afterwards* fails Vietnam's test and NYC's red tier simultaneously, however good
the review is, because the AI output *was* the sole basis at the moment of decision.
🟡 **Estimate: 6–8 weeks** for the pipeline against one LMS, plus 2 weeks per additional region
for threshold and queue policy. 🔴 **A dated legal premise, per `Gap 523`:** every date above was
read on **2026-10-22** and is `ATTRIBUTED-UNVERIFIED`; the Official Journal and Vietnam's
gazette are the checks, and `Pattern 32` exists because this base once steered an engagement on
a legal premise that had moved eleven months earlier.

## 🟢 🆕 `Pattern 35` (`p380`) — **Ship the evidence the 2026 buyer asks for: an eval harness beside the tutor, not a dashboard after it**

🔵 **The problem it solves.** Every trends leg this pass agrees buyers now want proof that a
product improves **learning**, not engagement. 🔴 **And this base's own shelf is the evidence of
the gap:** `agents/top.md` carries a dozen tutor rows and almost none ships a way to tell whether
it teaches. A studio that demos a tutor and promises measurement later has nothing to sell to a
procurement officer who has read the 2026 guidance.

| Layer | Component | Licence — **and the channel it was read on** | Grant path | Role |
|---|---|---|---|---|
| Tutor + harness | [`abhijeetgupta23/ai-agent-to-learn-faster-and-better`](https://github.com/abhijeetgupta23/ai-agent-to-learn-faster-and-better) | 🟢 **MIT** `1 071 B`, `decdac964835` | `main/LICENSE` | 🟢 Adaptive modality from a **learning-science knowledge graph** with a **first-class eval harness** — the harness is the reason it is here |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟡 **MIT per this base's earlier rows; NOT re-read this pass** | — | **Bayesian Knowledge Tracing** from UC Berkeley: a defensible mastery estimate rather than a completion count |
| Curriculum spine | [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | 🔴 **ODbL-1.0** + **CC-BY-SA-4.0** (`25 289 B`, `77d2692c3d64`) | `main/LICENSE` | 1 590 topics and 3 221 prerequisite edges against NGSS / Common Core. 🔴 **Share-alike — reference it, do NOT vendor it into a client deliverable** |
| LATAM spine | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** code / **CC BY 4.0** data — 🟡 `p343`'s first-hand read; the **sidebar** corroborated MIT this pass | per its shelf row | 1 721 Brazilian basic-education objectives verified against MEC/CNE — attribution only, so it **can** ship |
| Grade boundary | `Pattern 34` | — | — | If the harness ever gates a path, `Pattern 34`'s rule applies and this becomes high-risk |

🟢 **The wiring.**
1. Pin the curriculum spine **by reference** and resolve topics to prerequisite edges — Marble
   for NGSS/Common Core, BNCC for Brazil. 🔴 Keep the ODbL arm out of the deliverable's tree.
2. Instrument the tutor's sessions against **BKT** mastery per topic, not time-on-task.
3. Run the eval harness as a **CI job on the engagement**, so every model or prompt change
   produces a before/after on the same cohort definition.
4. Report mastery **per prerequisite edge** — which is what *"did it teach"* means operationally,
   and what a completion dashboard cannot answer.
5. 🔴 The moment a mastery estimate **gates** a student's path, it is an access decision:
   `Pattern 34`'s human decision record becomes mandatory.

🟡 **Estimate: 4–6 weeks** to a first defensible before/after, assuming the client can define a
cohort. 🔴 **Stated honestly: the tutor at the centre of this recipe has 4 stars and a HEAD of
2026-10-20.** It is recommended for its **harness design**, which is checkable, and a successor
should re-read the row before quoting it — `ACTION ZZ-au`: a shape-based reason has a shelf life.

## 🔴 2026-10-22 · `p379` — **`Pattern 32`'s Quebec default is CORRECTED HERE, not noted elsewhere: the suspension it defaults to was lifted ELEVEN MONTHS AGO and the regime that replaced it has a compliance deadline four and a half months in the past. 🟢 And `Pattern 33` is added: the three-channel address check a pass must run before it publishes a row.**

**Evidence:** [`quebec-talis`](../evidence/action-p378e-quebec-talis.2026-10-22-p379.tsv) ·
[`channel-mix`](../evidence/carried-index-channel-mix.2026-10-22-p379.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-22-p379.tsv)

### 🔴 `Pattern 32` — CORRECTED

🔴 **The defect.** `Pattern 32` defaults a Quebec school engagement to a **prohibition** on
generative AI, resting on the Ministère de la Cybersécurité et du Numérique's suspension of
**13 March 2025**. `p378` flagged it as *"last confirmed in force ten months ago on a TIER-2
outlet"* and registered `ACTION p378-E` to re-confirm it.

🔴 **It is not stale. It is wrong.**

| What `Pattern 32` assumes | What the French leg established, 2026-10-22 |
|---|---|
| A suspension is in force | 🔴 **Lifted.** A **December 2025** directive repealed indication `IA-RI-2025-001-OP` and replaced it with a structured governance framework |
| The posture is *"you may not"* | 🟢 The posture is **"you may, with governance"** — a formal structure, defined roles, named approvers of generative-AI systems, alignment with the government digital-governance framework |
| No deadline is in play | 🔴 Covered bodies had to be **fully compliant by 5 June 2026** — **four and a half months before this pass** |
| Schools inherit the public-body rule | 🟡 The **Ministère de l'Éducation** published a **2026** edition of its pedagogical/ethical/legal generative-AI guide, in force from the **late-August 2026** school year, which **delegates tool authorisation to school bodies** |

🟢 **CORRECTED DEFAULT for a Quebec school engagement.** Arrive assuming the client **is already
past a compliance deadline** and that **the school body, not the ministry, authorises the
tool**. The deliverable a Quebec engagement needs first is a *governance and approver map*, not
a permission argument. 🔵 The confidentiality rule survives the change: client data must not be
entered into the tool.

🔵 **Primary channel for a successor, and it is the one to read first:** a `gouv.qc.ca`-domain
directive, *"123-02 Directive visant à baliser l'utilisation de l'intelligence [artificielle
générative]"*, at `csspb.gouv.qc.ca`, uploaded **2026-10**. 🔴 **Not readable from this
sandbox** — see `Gap 524` — so it is pointed at, not quoted.

🔴 **What is still open:** the exact repeal date (sources say *"December 2025"* with no day),
and whether the school-sector guide operates as *lex specialis* over the public-body directive.
`Gap 523`.

🔵 **And the general lesson, which is bigger than Quebec.** A moratorium is the most perishable
fact in this industry and the most likely to end up on a slide. **No instrument on this base
dates a pattern's legal premise.** `Pattern 32` was not wrong when written; it was never given
an expiry.

### 🟢 `Pattern 33` — the three-channel address check, before publishing any row

🔵 **Why it exists:** this pass probed **fifteen** addresses as new supply that this base had
already **proven dead**, and it took a grep of the shelves to find that out. The instrument
that prevents it already existed and was not run.

**Recipe, in order. Each step is a command this repository already carries.**

1. 🟢 **Ask what the shelves already say** — before anything online:
   `make claims TOKEN=owner/repo`
   Non-zero means **STOP and read the cells**. A hit may be a row, or it may be a published
   refutation. 🔴 This is the step `p379` skipped.
2. 🟢 **Grade the address across BOTH channels** — new at `p379`:
   `make verdict SLUG=owner/repo`
   `CARRIED` channel U has it, a new row duplicates · `MENTIONED-B` only the bare-slug channel
   has it, **go read the cell** · `NEW` neither channel does.
   🔵 `make carried` is **unchanged** and still two-valued; it cannot tell you the middle case.
   🔴 **Read the printed verdict, not make's exit code.** GNU make exits **2** for any failed
   recipe, so it collapses `CARRIED` (1) and `MENTIONED-B` (3) into one status — `p379`'s own
   error, found by running the recipe. At the make layer the contract is only **STOP / GO**.
   For the three-way, call the script:
   `python3 -I compose/code/p235-carried-index/carried_index.py verdict owner/repo .`
3. 🟢 **Prove the address exists**, which no offline step can:
   `git ls-remote --symref https://github.com/owner/repo HEAD`
   Note the **default branch** — this pass found `telekom/ki-in-schulen` on `master` and
   `52north/wps` on `dev`, and a `main/LICENSE` guess returns `404` on both.
4. 🟢 **Read the grant payload first-hand**, on the branch step 3 reported:
   `curl https://raw.githubusercontent.com/owner/repo/<branch>/LICENSE`
   🔴 Record **bytes and sha256**, not just a family name. A **653-byte, title-block-free**
   payload found this pass is the bare **ISC** body, which a title-block classifier calls
   `UNKNOWN-TEMPLATE`; a **1 228-byte** MIT is MIT with an added URL line.
5. 🟡 **Date it:** `git clone --filter=blob:none --no-checkout --depth 1` then `git log -1`.
   Six of this pass's fourteen graded addresses are **over nine months stale**.
6. 🔴 **Do not expect star counts.** `api.github.com` and `github.com` HTML answer **403** —
   now across **four** independent sandboxes. A GitHub MCP server is mounted in this one and is
   **scoped to one unrelated repository**, so it is not a way around it either. `Gap 527`.

🔵 **Composes with:** `Pattern 32` (corrected above) for the jurisdictional default, and
`p364`'s companion closure for what else a deployment needs. 🔴 **Does not** compose with any
market figure on `intel/market.md` — four passes have failed to source a defensible 2026 level,
and `Pattern 33` is about addresses, not sizing.

## 🟢 🆕 `Pattern 32` (`p378`) — **One codebase into four Canadian provinces that disagree, defaulting to the narrowest live rule — and a grant bill of materials that survives a provincial procurement review**

🔵 **Why `32`:** `Pattern 31` is `p377`'s and `1`–`30` belong to the older series. `Gap 506`'s
collision is **not** widened here.

🔴 **The problem this solves, measured at `p378`.** Canada has **no national K-12 AI position
and cannot have one** — K-12 is provincial — and the four live provincial positions span the
entire range: **Quebec** suspends AI assistants, **British Columbia** publishes a decision
framework, **Ontario's** ministry is silent so **boards** and the ECNO consortium set the rule,
and **New Brunswick** writes AI into the curriculum. 🔴 A product built to BC's framework
**fails Quebec**. One built to Quebec satisfies all four and sells in none without
configuration. Evidence: [`northamerica-legs`](../evidence/northamerica-legs.2026-10-22-p378.tsv).

### 🟢 The components, every grant read FIRST-HAND at `p378` through `family_of()`

| Layer | Build on | Grant, read this pass | Why this one |
|---|---|---|---|
| Host LMS, GPL route | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **GPL-3.0** — `main/COPYING.txt`, 35 147 B, sha256₁₂ `8ceb4b9ee5ad` | 🟡 A **plugin** is a derivative work → GPL-3.0. An **external** agent over web services / LTI is not |
| Host LMS, AGPL route | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🔴 **AGPL-3.0** — `master/LICENSE`, 35 136 B, sha256₁₂ `e12d78569742` | 🔴 **Network copyleft.** Cite this address, not `openedx/edx-platform`: `p378` proved them one repository (ref-set `e8bd3fa5967f5181`) and this is the canonical name |
| Open edX deployment | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** — `release/LICENSE.txt`, 34 523 B, sha256₁₂ `0d96a4ff68ad` | 🔴 The deployer carries the **same** copyleft as the platform — `p364`'s companion-grant class |
| Tutor engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** — `main/LICENSE`, 11 408 B, sha256₁₂ `cd2f54e1e506`, HEAD **2026-10-19** | 🟢 Permissive, maintained, patent grant — the one component safe to embed in a closed deliverable |
| Classroom orchestration | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** — `main/LICENSE`, 1 065 B, sha256₁₂ `ba2525637432`, HEAD **2026-10-22** | 🟢 Multi-agent classroom; MIT confirmed on the bytes at `p377` and re-read here |
| Grade 1–9 RAG tutor | [`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) | 🟢 **MIT** — `master/LICENSE`, 1 068 B, sha256₁₂ `695941afdd1f`, HEAD **2026-10-21** | 🟢 Closest fit to a K-12 cohort; both `main` and `master` serve the grant |

### 🟢 How to wire it: policy is CONFIGURATION, and the default is the strictest live rule

1. **Put the policy outside the model.** A per-province profile — not a prompt — with three
   switches the four regimes actually differ on: **(a)** is a generative assistant reachable by
   a student at all, **(b)** may it produce a draft the student submits, **(c)** must each
   interaction be logged against a curriculum outcome.
2. **Default every switch to Quebec**: assistant **unreachable** by students, staff-facing only.
   🔵 Same construction as `p377`'s Norway finding — Udir bars **access**, regjeringen.no bars
   **use**, and a product satisfying one fails the other, so **build the narrower one**.
3. **BC** turns (a) on behind a board-level decision record, because BC's instrument is a
   *decision framework*: the artefact it wants is the **documented decision**, not a setting.
4. **Ontario** inherits the **board** as the unit, not the province. Ship the profile per board
   and name ECNO's *English Generative AI Guidelines v1.3* as the default template.
5. **New Brunswick** turns (c) on and binds every interaction to a curriculum outcome, in both
   the Anglophone and Francophone streams — the province writes AI **into curriculum**, so the
   deliverable is traceability, not restraint.
6. **Keep the agent EXTERNAL to the LMS** and talk to it over web services / LTI. On the Moodle
   route this is what keeps the agent out of GPL-3.0 derivative scope; on the Open edX route it
   is what keeps your own code outside **AGPL-3.0's network clause**. 🔴 On that route the
   deployer (`tutor`) is AGPL too, so "we only deploy it" is not an exemption.
7. **Ship the grant bill of materials as a deliverable, not an appendix.** Every row above
   carries its path, byte count and `sha256₁₂` because a provincial procurement review asks
   which licence, from which file, at which commit.

### 🔴 Three checks `p378` learned the hard way — run them before the BOM leaves the building

| Check | Why |
|---|---|
| Classify every grant with `family_of()` from `compose/code/lib/license_family.sh`, **never your own grep** | 🔴 `p378`'s inline ladder read **Moodle as AGPL-3.0**: GPL-3.0 §13 is titled *"Use with the GNU Affero General Public License"*, so a body grep for *affero* labels every GPL-3.0 payload AGPL. GPL vs AGPL decides whether you may host without publishing your source |
| Run `identify()` from `p312` **as well**, and publish any disagreement | 🔴 A 137-byte **paraphrase** of CC0 read this pass classifies as clean `CC0-1.0` on the title block and `UNKNOWN-TEMPLATE` on the text. One instrument answers *what is it named after*, the other *is it the real text*. A permissive cell needs both |
| Cite the **canonical** address, checked against `aliases.tsv` | 🔴 Six pairs on these shelves were one repository published as two until `p378`. `openedx/edx-platform` and `imsglobal/openbadges-validator-core` are **dead names** — citing one names an owner that no longer holds the code |

### 🟡 What this pattern does NOT solve, stated so it is not oversold

🔴 **Quebec's suspension — the default this whole pattern is built around — was last confirmed
in force in December 2025**, on a TIER-2 outlet, with no 2026 update found. It is the strictest
fact on the Canadian leg and the **least currently evidenced**. Re-check it before a proposal
quotes it. 🔴 And **Mexico needs a different pattern**: there is no binding national rule to
configure against, 🟢 but **76.7 % of public-institution students do not know whether their own
school has guidelines** — so the artefact there is the **governance layer** (policy templates,
disclosure workflows, teacher-facing audit trails), not a tutor, and the window closes when the
SEP's consultation reaches Congress.


## 🟢 🆕 `Pattern 31` (`p377`) — **Prove you met the age floor, against two issuers who disagree about what the floor restricts**

🔴 **NUMBERING DEFECT, found by this pass while choosing a number, and recorded rather than
repeated.** `compose/patterns.md` carries **two overlapping series**: an older
`## 🆕 Pattern N` run that already occupies **1–30**, and a newer `` ## 🟢 🆕 `Pattern N` (pNNN) ``
run that **restarted at 15**. 🔴 **So `Pattern 15`, `16`, `17`, `18` and `19` each name TWO
DIFFERENT patterns on this shelf** — `p375`'s stage gate collides with an older `Pattern 15`,
and `p376`'s revocable credential collides with *"A special-education IEP deliverable"*.
🟢 **This pattern therefore takes `31`, the first free number in the single series**, and the
collision is filed as `Gap 506` instead of being widened by a third instance. 🔵 Every
`Pattern 15`/`Pattern 16` reference written by `p375`, `p376` and this pass means the **newer**
one; nothing is renamed here, because retro-editing the older headings would break every
historical citation — which is the same reason `p376` refused `p375`'s repoint.

🔵 **Nearest neighbour, named so a reader can tell them apart:** the older **`Pattern 18` —
*Curriculum-bound exam generation for a national curriculum*** is the closest existing work.
This pattern is not that one: its subject is **proving a cohort was never given access**, and
curriculum-bound generation is the component it uses to replace the thing it removes.

🔴 **The problem this pattern exists for, and it is new to these shelves this pass.** The
six-jurisdiction age band converges on **who** (roughly end-of-primary) and **diverges on
what**. Norway's two TIER-1 issuers, read through the index this pass, say different things:

| Issuer | Restricts | Operative test |
|---|---|---|
| **Udir** (directorate) | 🔴 **ACCESS** — *"skal i all hovedsak ikke **gis tilgang til** generativ KI"* | Was the pupil **given access to** the surface? |
| **regjeringen.no** (government) | 🟡 **USE** — *"skal i all hovedsak ikke **brukes** i barneskolen"* | Did the pupil **use** it? |

🟢 **A deployment that discourages use satisfies the government and FAILS the directorate.**
🔵 So the build target is the narrower one — **absence of the surface** — and the deliverable
is an artefact that demonstrates *which* reading was met, per cohort, on a date.

### 🟢 The components, every grant read first-hand on 2026-10-22

| Role | Component | Licence | HEAD | Why this one |
|---|---|---|---|---|
| **The gate itself** | `Pattern 15`'s per-stage virtual key at the gateway | — | — | The capability is **absent** for the gated cohort, not refused at the prompt. This is what satisfies Udir's *access* test |
| **Teacher-facing generation** (the gated cohort's replacement) | [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT** (1 074 B, `2121152fdef1`) | `79793ee` · **2026-10-21** | 🟢 **The key move.** Grades 1–7 get no generative surface; the **teacher** does. Material reaches the pupil having passed through an adult, which is inside both readings |
| **Curriculum anchor** | the client's national standard — **BNCC** in the shipped case | the ministry's | — | Codes and their literal text come from the standard, never the model. Swap BNCC for the local equivalent; the architecture is the transferable part |
| **LMS boundary** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (11 361 B) | `41f150c` · 2026-10-13 | LTI 1.3 launch from Moodle, Open edX, Canvas, Blackboard. The LMS already knows the pupil's **grade**, which is the gate's input |
| **The artefact** | a per-cohort decision log emitted by the gateway | the client's own | — | 🔴 The thing an inspector actually reads. Small: cohort, stage, capability set, date, policy version |

### 🟢 How to wire it, and the one decision that matters

1. 🟢 **Take the stage from the LMS launch claim, not from a profile field.** `ltijs` surfaces
   the LTI context; the pupil's grade arrives with the launch and cannot be self-asserted.
2. 🔴 **Issue a DIFFERENT gateway key per stage, and give the grades 1–7 key no generative
   model at all.** Not a lower quota, not a stricter system prompt — **no route**. A key that
   cannot reach a model is the only configuration that answers *"were they given access?"*
   with evidence rather than with intent.
3. 🟢 **Point the teacher-facing generator at the same cohort.** `agente-bncc-professores`
   produces the lesson plan and the assessment for that class, grounded in the standard, with
   invented curriculum codes discarded before the teacher sees them.
4. 🟢 **Emit the decision log on every launch**, including the refusals. A log that records
   only what was allowed cannot demonstrate a floor.
5. 🔵 **Mark the output.** EMEA's **Article 50** has been live since **2 August 2026** and is
   independent of the Annex III deferral to **2 December 2027**: synthetic content needs
   marking now, in the teacher-facing path too.

### 🔴 What to check before quoting this

🔴 **`agente-bncc-professores` is single-author**, no release tags were read by this pass, and
its embeddings (`gemini-embedding-2`, 768-dim) ship inside a committed SQLite file — a client
on a different embedding provider re-indexes **1 580** rows. Minutes, but not zero.

🔴 **BNCC is Brazilian.** The grounding **architecture** transfers; the **data** does not. For
any other jurisdiction, budget the curriculum extraction as its own work item — it is the
expensive part, and it is the part the client's ministry can supply.

🔴 **The Norwegian cell is corroborated at TIER-1 but is still not a byte-level read**:
`udir.no` and `regjeringen.no` are NXDOMAIN from this environment and were reached **through
the search index**. 🟢 12 outlets, 2 of them the issuers. 🔴 **And `Gap 503` is open** — Udir
undertook to elaborate these recommendations by **1 October 2026** and no outlet, including
Udir's own page, reports publication. 🔵 **Re-check before a Norwegian engagement quotes the
detail; the headline rule is safe, the exceptions regime is not yet written.**

🟢 **Where this sells today, with no legislative dependency:** a **US district** (NYC's
moratorium through grade 8, Katy ISD's K-6 ban) has already written the policy and cannot
currently prove it holds. 🔵 The decision log is a board-meeting artefact, and the district —
not the state — is the buyer.


## 🟢 🆕 `Pattern 16` (`p376`) — **A credential that still verifies after the issuer is gone**, assembled from permissive code with the issuer written rather than forked

🔵 **The problem this solves, and why the obvious build is wrong.** A client wants verifiable
credentials — badges, micro-credentials, completion records — issued from the LMS they already
run. The obvious move is to fork the most complete open-source issuer. 🔴 **Measured this pass,
that move is unavailable on permissive terms:** the credentialing/interop tier's complete
issuers are `AGPL-3.0` (`Schroedinger-Hat/certo`, `edubadges/edubadges-server`) or carry **no
grant at all** (`open-ent/openbadges`), and the one permissively granted LTI-to-VC bridge
(`digitalcredentials/lti-issuer`, MIT) has not moved since **2024-04-22**.
([`credentialing-layer-grade`](../evidence/credentialing-layer-grade.2026-10-22-p376.tsv))

🟢 **So the recipe inverts the usual shape: fork nothing at the issuer, and buy the hard parts
— the LMS boundary and the verifier — off the permissive shelf.**

### 🟢 The components, every grant read first-hand on 2026-10-22

| Role | Component | Licence | HEAD | Why this one |
|---|---|---|---|---|
| **LMS boundary** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (11 361 B) | `41f150c` · 2026-10-13 | LTI 1.3 tool provider; launches from Moodle, Open edX, Canvas and Blackboard without per-LMS work. **Permissive and maintained** |
| **Offline verifier** | [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) | 🟢 **MIT** (1 080 B) | `d34f262` · 2026-10-05 | validates Open Badges 3.0 / W3C VC with **zero dependencies, offline**. The acceptance test a relying party can run without the issuer |
| **Issuer** | 🔴 **written, not forked** — to the 1EdTech OB 3.0 + W3C VCDM 2.0 specs | the client's own | — | the only piece with no permissive maintained option. Scope is small: sign a VC-JWT, serve five URIs |
| **Signing** (optional) | [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🟡 **LGPL-3.0** (7 650 B) | `598a57b` · 2026-10-21 | OB 2.0 JWS + OB 3.0 VC-JWT signing. **Take it only if weak copyleft is acceptable**; dynamic linking keeps the client's code separate. Otherwise RS256 over a JWKS is ~200 lines |
| **Reference design** | [`open-ent/openbadges`](https://github.com/open-ent/openbadges) | 🔴 **RESERVED — read, never linked** | `a978850` · 2026-10-16 | the most complete OB 3.0 issuer seen; its README is the specification source for the three constraints below |
| **Reference bridge** | [`digitalcredentials/lti-issuer`](https://github.com/digitalcredentials/lti-issuer) | 🟢 MIT (1 076 B) | `75a3c5d` · 🔴 2024-04-22 | the LTI→VC seam, as a **reading**. MIT means you may lift code; the HEAD date means you should not depend on it |

### 🔴 The three constraints that decide whether this works, read first-hand from a primary text

🔵 These are not design preferences. They come from `open-ent/openbadges`'s own README — the
best primary engineering text this pass retrieved on any channel — and each one, if missed,
produces credentials that are **worthless rather than merely imperfect**.

1. 🔴 **The public verification routes must carry NO authentication.** JWKS, badge, issuer,
   revocation list and credential endpoints bear *"aucun `@SecuredAction`"*, because *"si elles
   exigeaient une session, l'attestation serait invérifiable, c'est-à-dire sans valeur"*. A
   credential that a third party must log in to check is not a credential. **This is the single
   most common way this build fails**, because every other route in an LMS integration *should*
   be authenticated and the pattern looks like a security defect to a reviewer.
2. 🔴 **The signing key cannot be rotated casually.** Changing the `kid` without continuing to
   publish the old key *"rend invérifiables toutes les attestations déjà délivrées"* — every
   credential ever issued silently stops verifying. 🟢 Budget key *retention*, not key rotation:
   the JWKS is append-mostly and old keys are served indefinitely.
3. 🟢 **Holder identity goes in as a salted digest, with the salt travelling inside the
   credential**, and the subject id is a `urn:uuid:` rather than a URL — because a subject URL
   of the form `/subjects/<id>` tells every future reader that this person holds an account on
   the platform. 🔵 Showing a credential must not disclose the learner's address.

🟡 **A fourth constraint, from the same text, worth pricing:** every URI the credential carries
must keep answering **for as long as the credential is meant to be believed** — credential,
badge, issuer, revocation list and JWKS. 🔴 **None is decorative.** That is a hosting commitment
measured in years and it belongs in the SOW, not in the architecture diagram.

### 🟢 Shape of the engagement

🔵 **8–10 weeks**, and the sequence matters because the verifier is the acceptance test:

1. **Week 1–2** — stand up `Cvmcosta/ltijs` against the client's actual LMS. 🔴 Do not assume
   "LTI support" is one capability; that is the standing warning of this base's earlier
   LTI-reach pattern.
2. **Week 2–3** — wire `credential-lens` into CI **first**, as the oracle. A credential the
   verifier rejects is a failing test rather than a discovery in month three.
3. **Week 3–6** — write the issuer: VC-JWT (RS256), JWKS published, the five URIs served, the
   `1EdTechRevocationList` served publicly. Constraints 1–3 are acceptance criteria, not notes.
4. **Week 6–8** — key-retention runbook, and an **external** verification rehearsal: a relying
   party with no account verifies a credential, offline, with the issuer's service stopped.
5. **Week 8–10** — hand over the hosting commitment for the credential's URI set, explicitly.

🟢 **Why a studio can defend this on licence grounds:** the LMS boundary is Apache-2.0, the
verifier is MIT, the issuer is the client's own code written against a public specification, and
**nothing AGPL-3.0 is linked**. 🔵 The one component that would have saved weeks — a complete
issuer — is exactly the one that cannot be taken without either a copyleft obligation or a
missing grant, and that is the whole reason this pattern is shaped the way it is.

🔴 **Where it does NOT apply.** If the client will accept AGPL-3.0, fork `edubadges-server`
(`cd31fdd`, **2026-10-20**, SURF, LTI 1.3 already present) and finish in half the time. This
pattern is for clients who will not.

## 🟢 🆕 `Pattern 15` (`p375`) — **Stage-gated generation**: the open-ended surface is ABSENT for the youngest cohort, not merely discouraged

🟢 **The constraint this exists for is measured in `intel/trends.md` this pass: four
jurisdictions across three legal systems independently set an AGE FLOOR on autonomous pupil use
of generative AI** — China (no independent open-ended generation in primary), Brazil (prohibited
to end of 5th grade), France (from classe de quatrième), New York `A.9190` (would bar most
classroom AI below grade 9). 🔴 **A policy document does not satisfy any of them**, and
`Pattern 14`'s permission boundary is about *marks*, not about *who may prompt*.

🔵 **The design rule, stated so it is checkable rather than aspirational:** for a learner below
the configured stage, the generation endpoint is **not reachable from that learner's session** —
not hidden in the UI, not guarded by a prompt instruction, not filtered after the fact.

### The composition, with the specific repositories

| Role | Component | Licence | Why this one |
|---|---|---|---|
| Learner record + stage | [`moodle/moodle`](https://github.com/moodle/moodle) cohorts, or [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | GPL-3.0 / Apache-2.0 | the stage must come from the **system of record**, never from a self-declared profile |
| Interop boundary | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (LTI 1.3) | Apache-2.0 | the LTI launch already carries role and context claims; the stage travels with the launch |
| Tutoring surface | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | its mode set is the natural gate: Socratic / quiz / flashcard modes are **retrieval and dialogue over fixed content**, not open-ended generation |
| Stage-aware routing | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | MIT | one place to bind a **virtual key per stage**, so the youngest cohort's key has no generation model attached at all |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) or [`vllm-project/vllm`](https://github.com/vllm-project/vllm) | MIT / Apache-2.0 | France's framework **recommends open-source tools** and tolerates consumer services only with no personal data: self-hosting is the compliant configuration, not the thrifty one |
| Evidence | [`ibm-skills-network/mark`](https://github.com/ibm-skills-network/mark) | Apache-2.0 | returns comments and never a mark — `Pattern 14`'s boundary, carried through |

🔴 **One address in the table above was WRONG in this pass's first draft, and recording it is
cheaper than a successor finding it.** `p375` first wrote the LTI component as `1EdTech/ltijs`,
reasoning from the standards body's name. 🔴 **`ls-remote` says `rc=128`: it does not exist.**
The live address is [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (HEAD `41f150c069`,
read **2026-10-22**), which this base already carried — 🔵 **and `gate-fold-identity` then caught
`p375` publishing it as `cvmcosta/…`, a second casing of the spelling these shelves already use.
Two gates, two catches, one address, all before the commit.** 🟢 **This is the signature defect's tenth
instance and the FIRST caught before the commit rather than by the next pass** — `ACTION
p374-E`'s rule ("before constructing an address, re-read the source for the owner") worked, but
only because every address in this table was probed before publication rather than after.

### How the gate is actually enforced, and why it is a permission rather than a prompt

🟢 **The load-bearing step is that the stage-gate lives in the KEY, not in the application.**
LiteLLM issues a **virtual key per stage**; the primary-stage key is provisioned with
**retrieval and classification models only and no generative completion model**. A request for
generation on that key fails at the gateway with a 4xx — which is a log line an auditor can
read, and which no amount of prompt injection from the learner's side can reach around.

🔴 **The failure mode this avoids, and it is the one `p374` found in the Open edX advisory.** A
gate implemented as *configuration inside the learning tool* is only as strong as the tool's own
boundary; `p374` recorded that **any** LTI tool on an Open edX platform can post a grade back for
**any** XBlock given the `resource_link_id`. 🟢 The same reasoning applies here: hold the
capability outside the component that the learner can talk to.

### What to tell the client, per region

🟢 **France / EMEA** — the gate plus self-hosting answers the framework's open-source
recommendation and its data condition in one architecture; pair it with the
**evidence-production** posture `ACTION p374-B` requires (training records, a register of who
operates which system) rather than with *"ensure a sufficient level"*, which was **rewritten**.
🟢 **Brazil / LATAM** — build to the **prohibitions now** and to adequacy on the 12-month clock,
and add the **AI-use declaration** that Mexico, Colombia and Chile all require of pupils: that is
an attribution feature, not a policy.
🟢 **China / APAC** — the three-tier spiral (primary / junior / senior) maps directly onto three
stage keys; 🔴 the *mandatory weekly class* claim circulating commercially is **not corroborated
by any MOE document** (`Gap 497`) and must not be quoted to a client.
🟢 **North America** — the gate is the artefact that makes a district's statutory AI policy
**demonstrable** rather than declared, which is the gap behind the 19 % figure.

🔴 **Stated limit.** Every jurisdictional cell behind this pattern is **secondary**; no primary
instrument text was retrieved for any of the four floors. 🔵 The pattern is sound as an
architecture regardless, because it is strictly more conservative than any of the four readings —
but the **specific grade boundary** per country must be confirmed against the instrument before
it goes in a statement of work.

## 🟢 🆕 `Pattern 14` (`p374`) — **Assessment that returns comments and never a mark**, with the boundary enforced as a permission an auditor can check

**Evidence:** [`gap490-product-name`](../evidence/gap490-product-name.2026-10-22-p374.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-22-p374.tsv)

🟢 **Why this pattern and not another.** `intel/trends.md` Trend 1 measures three legal systems
converging on one boundary — **an AI system may inform an assessment and may not decide one**
(Brazil's *excessive* tier, the US district statutes' human-oversight shape, EU Annex III).
🟢 One architecture therefore sells in **LATAM, North America and EMEA** without redesign.
🔵 It also targets the widest measured demand gap this base carries: **50 %** of LATAM students
want AI-assisted feedback against **19 %** of faculty providing it.

🔴 **And the reason it is built this way rather than configured this way.** A GitLab advisory on
`lti-consumer-xblock` reports that **any** LTI tool integrated with an Open edX platform can post
a grade back for **any** LTI XBlock if it knows the `resource_link_id` — a missing-authorisation
issue. 🔴 So *"the AI only suggests"* is **not deliverable by policy, by contract, or by
configuration** on that platform. It is deliverable only by the AI component **having no
grade-write scope to begin with.**

### 🟢 The components, every one verified first-hand on 2026-10-22

| Role | Component | Licence | Verified |
|---|---|---|---|
| **Feedback engine** | [`ibm-skills-network/mark`](https://github.com/ibm-skills-network/mark) | **Apache-2.0** | grant read at `master/LICENSE` (11 357 B); HEAD `ecd5915`, **2026-10-21** |
| **System of record for marks** | [`MarkUsProject/Markus`](https://github.com/MarkUsProject/Markus) | **MIT** | grant read at `master/LICENSE` (1 076 B); HEAD `86395e8`, **2026-10-21** |
| **LTI 1.3 consumer / courseware** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | AGPL-3.0 | `ls-remote` LIVE, HEAD `229f7e1`; **LTI Advantage Complete** since Sumac |
| **Learning-record sink** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | carried | 764 refs (`p372`) — the maintained xAPI sibling |

🔵 **Licence note for a client deck:** the two components a studio *modifies* are **Apache-2.0**
and **MIT**. 🔴 Open edX is **AGPL-3.0** — fine as the platform you deploy and extend through its
own plugin surfaces, and a decision to review before you fork it.

### 🟢 How to wire it

1. 🟢 **Register `mark` as an LTI 1.3 tool in Open edX with NO grade scope.** Omit
   `https://purl.imsglobal.org/spec/lti-ags/scope/score` from the tool's registered scopes.
   🔴 This is the whole pattern. If the scope is present, the advisory above applies and nothing
   downstream restores the boundary.
2. 🟢 **Point `mark` at the submission and let it return comments only** — its own README
   describes automated grading, intelligent feedback and multilingual support; you are using the
   **feedback** half and deliberately not the grading half.
3. 🟢 **Route every comment into MarkUs as an annotation on the submission**, where a human
   grader accepts, edits or discards it and **enters the mark**. MarkUs holds the grade; nothing
   else can write one.
4. 🟢 **Emit an xAPI statement per AI suggestion and per human decision** into `lrsql` — actor,
   verb (`suggested` / `accepted` / `overrode`), object, timestamp. 🟢 This is the artefact that
   satisfies Brazil's *"marks are given by teachers"*, the US statutes' human-oversight
   requirement, and an Annex III audit trail **from one log**.
5. 🟢 **Produce the Article 4 evidence pack from the same system**, since
   Regulation (EU) 2026/1744 now asks a deployer to **show the measures it took** for staff
   operating the system: the operator register is the list of graders with MarkUs accounts, and
   the training record attaches to it.

### 🔴 What to check before quoting this

🔴 **The scope omission must be verified on the deployed tool, not in the design document** — it
is the one control the whole pattern rests on, and it is checkable in minutes.
🔴 **`mark`'s HEAD is one day old at the time of writing.** It is maintained; it is also young
on this base, which has carried it for zero passes. Pin a sha.
🔴 **Brazil's prohibitions are live on publication but the parecer has no normative force until
MEC homologates**, which had not happened as of **2026-10-22**. Build to the prohibitions; do
not tell a client the adequacy clock has started.
🔵 **Effort: 5–7 weeks** for a single-institution pilot on an existing Open edX deployment, most
of it in step 3 — MarkUs annotation ingest is the only component with no off-the-shelf path.

## Start here — pattern index

🟢 **Pick the pattern that matches the engagement, then read only that section.**
Each one names the specific repos and how to wire them.

| # | Pattern | Use when |
| ---: | --- | --- |
| 1 | LMS-native tutor without touching the LMS | Client has Moodle/Canvas/Open edX and the deliverable must stay yours |
| 2 | BNCC-aligned lesson planner for Brazil | LATAM K-12, Portuguese, national curriculum binding |
| 3 | EU AI Act high-risk conformity wrapper | EMEA, anything touching admissions, assessment or proctoring |
| 4 | Assessment integrity for the agent era | Client's detector has stopped being credible |
| 5 | Offline-first delivery for low-connectivity regions | Rural LATAM, Sub-Saharan Africa, remote APAC |
| 6 | Modernising a legacy SCORM corporate estate | Enterprise L&D with years of SCORM content |
| 7 | Curriculum knowledge graph from raw textbooks | No structured curriculum data exists yet |
| 12 | 🆕 AI over an existing lecture-video estate | Client has years of recordings and wants search, captions and chapters |
| 8 | Verifiable credentials for skills-based hiring | Employability / workforce engagements |
| 9 | Licence-clean programming-assessment stack | Coding academy, deliverable must be closed |
| 10 | Add retention to a tutor that already works | Tutor exists, outcomes do not stick |
| 13 | 🆕 Assistive feedback that returns comments and never a mark | LATAM HE, Brazilian K-12, or any no-automated-decision statute |
| 11 | England-curriculum tutor, client keeps the curriculum model | UK engagements |
| 12 | Process-evidence assessment | Detection-based integrity has failed |
| 13 | Statutory inclusion deliverable, Colombian school system | LATAM public sector, legal mandate |
| 14 | Reaching a client's LMS when "LTI support" is not one capability | Integration scoping before you quote |
| 🆕 30 | Reaching the incumbent LMS when 71 % of the community bridges cannot be used | Client runs Canvas/Moodle/Blackboard/Brightspace/PowerSchool/Banner and the deliverable must stay yours |


# Education — composition patterns

**Pass 367 · 2026-10-21.** Concrete recipes. 🆕 **Pattern 27 is `p367`'s**, and it closes the
last axis in the Pattern 24 → 25 → 26 chain: those three grade the right noun, at the right
pin, in the right direction — over a **population built from one spelling of an address**.
🔴 On this base that population was missing **16.3%** of the repositories it was meant to
cover.

**Pass 366 · 2026-10-21.** Concrete recipes. 🆕 **Pattern 26 is `p366`'s**: it sits one step
*before* Patterns 24 and 25, because both of those grade whatever a README named and only
**17.8%** of README-named companions are declared dependencies — so it enumerates the closure
from the build with `syft`, grades it with `scancode-toolkit`, enforces the boundary with
`ort`, and resolves identity by commit sha rather than by slug. 🆕 **Patterns 23 and 24 are `p364`'s**: the
first is the only stack on these shelves that is permissive *through the deployment* and
not merely at the core; the second turns `p364`'s own instrument into a deliverable. Each names the specific repos, the licence
boundary that makes the composition safe, and what the engagement actually delivers.
Every repo referenced is verified live with its grant read from payload on
**2026-10-21** — see `agents/top.md` and `repos/foundations.md`.

**The rule that governs all of these.** Most education platforms are GPL or AGPL.
Reaching them **over a protocol boundary** — LTI 1.3, web services, or MCP — keeps a
client's proprietary work on its own side of the licence. Forking them does not.
Every pattern below is built on a boundary, deliberately.

---

## Pattern 1 — LMS-native tutor without touching the LMS

**Problem.** A university runs Canvas or Moodle. They want an AI tutor grounded in
their actual courses. They cannot accept AGPL obligations on their own code, and IT
will not approve a fork.

**Recipe.**
1. **Reach the LMS over MCP**, not code: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) for Canvas, [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) (MIT) for Moodle, [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) for Open edX.
2. **Tutoring logic** from [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) — Bayesian Knowledge Tracing gives defensible mastery estimates instead of vibes.
3. **Pedagogical behaviour** loaded as skills from [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (Apache-2.0) or [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) (Apache-2.0).
4. **Surface it in the LMS** as an LTI 1.3 tool via [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0, Node) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT, Python). On Canvas specifically, [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) (MIT) removes most of the boilerplate.
5. **Quality-gate the output** with [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (MIT code).

🟢 **Licence boundary:** every component is MIT or Apache-2.0. The AGPL platform is
reached over MCP and LTI, so its copyleft never touches client code.

---

## Pattern 2 — BNCC-aligned lesson planner for Brazil

**Problem.** A Brazilian ministry, network or EdTech needs lesson planning provably
aligned to the national BNCC curriculum. Generic AI output cannot be defended to a
regulator or a school board.

**Recipe.**
1. **Ground in official standards:** [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (MIT) — **1 721 BNCC learning objectives** as JSON/SQLite/CSV. Load it as the retrieval corpus so every generated plan cites a real objective code.
2. **Generate the courseware** with [`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT) for course structure, or [`SYuan03/Skill-Anything`](https://github.com/SYuan03/Skill-Anything) (MIT) to turn existing material into quizzes and flashcards.
3. **Render as interactive content** teachers can still edit: [`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) (**MIT** — note the core library is GPL-3.0, the CLI is not) or [`openpatch/hyperbook`](https://github.com/openpatch/hyperbook) (MIT).
4. **Deliver into the school's system:** [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) (GPL-2.0) for K-12 SIS, or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — both with mature Portuguese/Spanish localisation. Integrate over web services to keep the boundary.
5. **Pull supporting public data** via [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (MIT).

🟢 **Why this is defensible:** the alignment claim is checkable against a public MIT
dataset, objective by objective. 🔴 **And why it does not yet port:** no equivalent
open dataset exists for Mexico's SEP, Colombia's or Argentina's standards. Building
one is the regional asset play — see `intel/market.md` → LATAM.

---

## Pattern 3 — EU AI Act high-risk conformity wrapper

**Problem.** A European institution uses AI in admissions or assessment. That is a
**high-risk** system under EU AI Act **Annex III point 3**, and the obligations — risk
management, data governance, logging, human oversight — bind from **2 December 2027**,
postponed from 2 August 2026 by the Digital Omnibus (**Regulation (EU) 2026/1744**, in
force 27 July 2026). Their current tooling has none of it.

🔵 **Scope the engagement on the real date.** Telling this client they are bound *now*
is wrong by sixteen months and in the expensive direction. What binds them today is the
**prohibitions**, the **AI-literacy duty** and **Article 50 transparency**. The
high-risk work is a **readiness programme with a fixed, non-extendable deadline** — a
better engagement than emergency remediation, and an honest one.

**Recipe.**
1. **Instrument every decision.** Wrap the model call so each inference writes an
   immutable record: inputs, model version, output, the human who reviewed it. Emit
   it on the **Caliper** event vocabulary — implement [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) 🔴 (an **IMS specification licence**: implement the standard, do not vendor the document).
2. **Force human oversight structurally**, not by policy: the agent proposes, a named
   human disposes, and the gate is in the data model. [`byerlikaya/Septum`](https://github.com/byerlikaya/Septum) (MIT) is a working reference for the approval-gate shape — local PII detection → approval → de-anonymisation.
3. **Evidence of efficacy and non-discrimination:** run the model as a randomised
   experiment inside the LMS with [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) (Apache-2.0). This produces the outcome data the Act's risk-management file needs, and the efficacy proof procurement now demands (see `intel/trends.md` §2).
4. **Accessibility obligations in the same pass:** [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) (GPL-3.0) inspects course content; have the agent generate remediations rather than only flagging.
5. **Host on a permissive platform** so the conformity layer can be a closed
   deliverable: [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**) is the only full HE platform where this is clean.

🟢 **This is the strongest opportunity in the KB.** Obligations are live, and a survey
of 450+ institutions put formal AI guidelines at ~10 %.

---

## Pattern 4 — Assessment integrity for the agent era

**Problem.** Students submit agent-assisted work. Detection-by-vibes is both unfair
and indefensible, and most "AI detectors" do not survive scrutiny.

**Recipe.**
1. **Measure similarity, not "AI-ness":** [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT, Ghent University) does structural source-code plagiarism detection. It makes a claim you can show a student.
2. **Execute submissions safely:** [`judge0/judge0`](https://github.com/judge0/judge0) (GPL-3.0) sandboxes 60+ languages — consume it **as a service over its API** so the GPL boundary holds.
3. **Grade deterministically:** [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) (MIT, TU Munich) for secure test execution, or [`INGInious/INGInious`](https://github.com/INGInious/INGInious) (AGPL-3.0, 🟡 *"most of the files"* — mixed grant, diligence it) as a full assessment platform.
4. **Shift the assessment design itself.** Pair the above with process evidence —
   version history, in-editor telemetry from [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) (MIT) — so the artefact is no longer the only evidence.
5. **Model the mastery signal:** [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT) and [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) (MIT) for knowledge tracing over the resulting data.

🔵 **Position it honestly:** this detects *similarity and process anomalies*, not
authorship. Say so to the client; the alternative is a product that fails its first
appeal.

---

## Pattern 5 — Offline-first delivery for low-connectivity regions

**Problem.** Rural LATAM, Sub-Saharan Africa, remote APAC. Intermittent or no
connectivity, shared low-end devices, and no frontier-model budget per learner.

**Recipe.**
1. **Platform:** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**) — purpose-built offline-first, syncs when a link appears. MIT means the deployment can be a closed, branded client deliverable.
2. **Precompute, do not infer live.** Generate the full adaptive content tree
   server-side with [`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT) or 🆕 [`heshengtao/exameow`](https://github.com/heshengtao/exameow) (Apache-2.0, local-first exam generation), then ship it as a Kolibri channel. Inference cost becomes a one-time build cost. 🔴 **`CaviraOSS/PageLM` was REMOVED from this step at `p362`:** it was carried here as *(MIT)* and its payload is the **"PageLM Community License"** — non-commercial, plus a revenue-sharing requirement that applies to the software *"in whole or in part"*. **It cannot be in a paid deliverable at all**, so this is a removal rather than a boundary note.
3. **Local mastery model:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) — BKT runs on-device with no network call.
4. **Spaced repetition instead of generation:** [`HumphreySun98/Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent) (MIT) pairs RL action-selection with FSRS scheduling; [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) (MIT) where Anki is already in use.
5. **Literacy-specific base:** [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) (MIT) for early-grade literacy in African deployments.
6. **Mobile client:** fork [`moodlehq/moodleapp`](https://github.com/moodlehq/moodleapp) (**Apache-2.0** — permissive, unlike Moodle core) for a branded learner app.

🟢 **Every component is MIT or Apache-2.0** — re-verified component by component at
`p362` after one of them turned out not to be. This whole pattern can ship as a closed
deliverable, which matters for ministry and NGO procurement. 🔵 **The removal is the
lesson:** this pattern's value is the licence claim in this sentence, so a single wrong
grant in step 2 invalidated the whole recipe for exactly the buyers it is written for.

---

## Pattern 6 — Modernising a legacy SCORM corporate estate

**Problem.** An enterprise has thousands of hours of SCORM content, an LMS that
serves it, and no appetite to re-author any of it. They want AI on top.

**Recipe.**
1. **Keep the content, wrap the runtime:** [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT) is a modern SCORM 1.2/2004 JS runtime. It replaces the player, not the courseware, and its MIT grant lets you instrument it freely.
2. **Harvest the signal.** The SCORM runtime already emits completion, score and
   interaction data. Route it to a learning-record store on the **xAPI/Caliper**
   vocabulary — this is where the AI gets its training and personalisation signal,
   and it costs nothing to collect.
3. **Layer an agent over the catalogue:** [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) (MIT) is the closest working pattern for turning static documents into agent-loadable skills; apply the same shape to course PDFs and manuals.
4. **Fill gaps rather than rebuild:** generate only the missing modules with [`assafkip/claudemy`](https://github.com/assafkip/claudemy) (MIT) or [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) (AGPL-3.0 — 🔴 keep it a separate service if the client needs closed code).
5. **Corporate-academy platform** where a new one is needed: [`classroomio/classroomio`](https://github.com/classroomio/classroomio) (AGPL-3.0) or [`frappe/lms`](https://github.com/frappe/lms) (AGPL-3.0) — both copyleft, so run them as deployed services, not embedded code.

---

## Pattern 7 — Curriculum knowledge graph from raw textbooks

**Problem.** A client has textbooks and syllabi but no machine-readable curriculum
model, so nothing can be sequenced, diagnosed or aligned.

**Recipe.**
1. **Extraction pipeline:** [`clownjee/knowledge-import-pipeline`](https://github.com/clownjee/knowledge-import-pipeline) (Apache-2.0) does exactly this — PDF parsing → concept extraction → vector retrieval → prerequisite-edge construction → **MCP query service**. It is the only verified end-to-end implementation of this shape.
2. **Skeleton to align against:** [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0 — 🟡 share-alike binds a derivative *database*, not a produced work) or [`aclascollege/polymath`](https://github.com/aclascollege/polymath) (ODbL-1.0 + CC-BY-SA-4.0) for disciplines, courses, prerequisites, skills and careers.
3. 🔴 **Do not seed from [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy)** despite it being the best Chinese K-12 graph available (1 244 nodes, 5 123 items). It is **CC-BY-NC-4.0** and cannot be used in paid work. Use it to validate your own graph's shape, never as an ingredient.
4. **Serve it to agents over MCP** so the graph is a boundary-crossing asset reusable
   by every downstream tutor, planner and diagnostic.
5. **Diagnose against it:** [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT) for knowledge tracing over the prerequisite structure.

🟢 **Why this is the durable play.** Agents are commoditising fast; the curriculum
graph underneath them is proprietary, defensible and compounding. See
`intel/trends.md` §9.

---

## Pattern 8 — Verifiable credentials for skills-based hiring

**Problem.** A client wants to issue credentials employers can verify without calling
the registrar, and tie them to demonstrated skills rather than seat time.

**Recipe.**
1. **Wallet and issuance:** [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) (MIT, OpenWallet Foundation) — the open reference implementation for verifiable learner credentials.
2. **Skills vocabulary to issue against:** [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0) maps skills to careers, which is what makes a credential legible to an employer.
3. **Evidence behind each claim:** assessment results from Pattern 4, carried as
   Caliper/xAPI records so a credential points at verifiable evidence rather than a
   grade letter.
4. **Issue from the LMS** over LTI via [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (Apache-2.0) or [`openfun/marsha`](https://github.com/openfun/marsha) (MIT).

🔵 1EdTech names credentials a core 2026 mechanism for skills-based learning and
hiring; this is the open stack for it.

🔴 **`p372` CORRECTION to step 3, and it changes the cost of this pattern.** Step 3 says to
carry evidence *"as Caliper/xAPI records"*, which reads as though a reference implementation
were available to adopt. **It is not.** Probed first-hand **2026-10-21**: Caliper Analytics is
absent in **all four** language bindings (`caliper-java`, `caliper-js`, `caliper-php`,
`caliper-python`) across **both** org spellings (`1EdTech/`, `imsglobal/`), and the Open Badges
reference server is absent at **both** of its (`concentricsky/badgr-server`,
`1EdTech/badgr-server`). 🟢 **What IS maintained is the specification and the validators** —
[`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) (400 refs) and
[`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core)
(182 refs) — plus a working xAPI store,
[`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (764 refs). 🔴 **So step 3 is an
IMPLEMENT-FROM-SPEC task, not an adopt-a-library task**, and it should be estimated as one.
🟢 **The cheapest licence-clean route is xAPI, not Caliper:** `lrsql` exists and runs, whereas
Caliper has no retrievable client at all — this base's own earlier measurement found that the
one live Caliper client, `npm:@timeback/caliper`, ships **no grant and no source**. See
`intel/trends.md` **Trend E**.

## 🆕 Pattern 9 — A licence-clean programming-assessment stack for a coding academy

**Client shape.** A bootcamp, CS department, certification body or developer academy
that must run untrusted student code, grade it, detect copied submissions and report
results into an LMS the client already owns — and the deliverable has to ship inside a
closed engagement.

**Why this pattern did not exist one pass ago.** The only execution component this base
carried was `judge0` (GPL-3.0), so every version of this build had a copyleft component
at its centre. `p356`'s function legs found a **larger MIT alternative**.

**The stack, every grant read from the payload on 2026-10-21:**

1. **The platform and the web tier** — [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
   (🟢 **MIT**, `master/LICENSE`, 1 085 B, 6 552 ★) with
   [`QingdaoU/OnlineJudgeFE`](https://github.com/QingdaoU/OnlineJudgeFE) (🟢 **MIT**,
   330 ★). Submissions, problem bank, contests, admin. **Fork and brand both** — their MIT
   grants reach nothing.
2. 🔴 **The execution tier, and `p362` CORRECTED it: it is not MIT.** The components that
   run student code — [`QingdaoU/JudgeServer`](https://github.com/QingdaoU/JudgeServer)
   (209 ★) and [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) (🔴 branch
   **`newnew`**, 496 ★) — both ship the **Star And Thank Author License** (1 823 B each),
   and [`QingdaoU/OnlineJudgeDeploy`](https://github.com/QingdaoU/OnlineJudgeDeploy)
   (591 ★, ref `2.0`) has **no grant at any probed path**. 🟢 **Pick one of three
   positions, deliberately:**
   - 🟡 **honour SATA** — star the project, thank the authors in your notices, keep its
     copyright and project-url block intact. Cheap, and 🔴 still not OSI: an SPDX scan
     returns `NOASSERTION` and a *"permissive only"* procurement rule fails it;
   - 🟢 **keep execution outside the deliverable**, reached over HTTP — the same boundary
     this pattern already uses for `judge0`, and the position that needs no legal call;
   - 🟢 **build on a permissive executor instead** — 🆕
     [`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense) (**MIT**, 1 067 B,
     554 commits, 7 authors (`%ae`)) does code evaluation and restricted execution, and
     [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) covers
     notebooks. 🔴 Neither is a drop-in for a seccomp sandbox — this is a build.
3. **Notebook and data-science courses** — [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
   (🟢 **BSD-3-Clause**, 161 ★, UC Berkeley) for **Python *and* R** notebooks, behind
   [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) (BSD-3-Clause) with
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
   (BSD-3-Clause) for LMS single sign-on.
4. **Integrity** — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
   (🟢 **MIT**, 353 ★, Ghent University) for source-code plagiarism. 🔵 **Choose this over
   proctoring:** of the five proctoring rows verified this pass, one has no grant, one has
   no identified licensor and two are AGPL plugins to AGPL hosts. Detect what the
   submission *is* rather than surveil the student.
5. **Rubric-bound human-in-the-loop grading** — [`erictrainnlpinxihu/Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent)
   (🟢 **MIT**, 101 ★) for the written parts. Its four write actions are **absent from the
   tool table**, so the agent can only emit proposals, and every `GradingDraft` binds to a
   rubric line and a paragraph hash. That is a **structural** approval boundary, which is
   what the EU AI Act's high-risk regime wants for exam scoring (`intel/market.md`, EMEA).
6. **Report back into the client's LMS** — an **LTI 1.3 tool** with
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT). Never a
   fork of Canvas or Open edX — both are AGPL.

🟡 **Every component EXCEPT the execution tier is MIT, BSD-3-Clause or Apache-2.0**, and
🔴 **the sentence that used to stand here — *"every component is MIT, BSD-3-Clause or
Apache-2.0"* — was wrong for six passes.** The web tier, the notebook path, the integrity
check, the grading agent and the LTI bridge all ship inside a closed deliverable with no
copyleft reach. 🔴 The thing that executes untrusted code does not, and step 2 above is
how to resolve that. 🔵 **The pattern is still sound; what changed is that the licence
boundary now falls between the platform and its sandbox rather than around the whole
stack.**

🟡 **When to pick the copyleft alternatives instead.** If the client will host it
themselves and publish nothing of their own, [`hydro-dev/Hydro`](https://github.com/hydro-dev/Hydro)
(AGPL-3.0, 7 137 ★) is better engineering for many courses at once, and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) (**GPL-3.0**, branch
`Version-1` — 🔴 corrected `p362` from AGPL-3.0) is the only row actually built for
**courses** — assignments, deadlines, per-student feedback — rather than contests. 🔵 The
correction matters here: `Hydro` is AGPL and must stay the **client's** deployment, while
🟢 **`Sharif-Judge` is plain GPL and a studio MAY host it as a service** — only
distributing a modified build triggers the obligation.

🔴 **The three branch traps in this pattern, named because they will bite.**
`QingdaoU/Judger` defaults to **`newnew`**, `Sharif-Judge` to **`Version-1`**, and
`QingdaoU/OnlineJudgeDeploy` to **`2.0`**. A CI licence check or a vendoring script that
assumes `main` or `master` reports all three as **unlicensed**.

🔴 **And `p362`'s sharper warning: finding the grant is not reading it.** Both odd refs
*were* probed by the pass that shelved them, and both cells recorded the right path and
the wrong family — the sandbox as MIT when it is SATA, `Sharif-Judge` as AGPL when it is
GPL. 🟢 **Run the payload through
[`p1054-mit-plus-clause`](code/p1054-mit-plus-clause/), not through a path check:** on
the sandbox's bytes it returns `is_usable_permissive: False`, and it has done since
`p187`.

## 🆕 Pattern 10 — Add retention to a tutor that already works

**Client shape.** A client already has a tutor, courseware or study app that generates
good material and cannot show that anyone **remembers** it. Procurement is starting to
ask for evidence of learning rather than evidence of output (`intel/trends.md` §2), and
"the model explained it well" is not an answer.

**The insight.** Every tutoring agent on `agents/top.md` decides *what* to teach next.
Almost none decides *when to come back to it* — and scheduling, not generation, is what
moves retention. The sector has a standard for this, it is small, and it is MIT.

**The stack:**

1. **The scheduler** — [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
   (🟢 **MIT**, 514 ★). A few hundred lines; takes a review outcome and returns the next
   due date. Drop it beside the existing content pipeline without touching it.
2. **The algorithm, to justify it to the client** — [`free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler)
   (🟢 **MIT**, 729 ★) is the published DSR-model specification, so the scheduling
   decisions are **explainable to a procurement committee** rather than opaque.
3. **Verification, not self-report** — [`nagisanzenin/engram`](https://github.com/nagisanzenin/engram)
   (🟢 **MIT**, 1 458 ★) does free-recall checking *with receipts*: the learner is
   measured recalling, and the evidence is kept. This is the row that produces the
   artefact an evidence-based procurement wants.
4. **Reach the learner where their cards already are** — [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server)
   (🟢 **MIT**) over MCP, or [`kitschpatrol/yanki`](https://github.com/kitschpatrol/yanki)
   (🟡 MIT, declared only in `package.json`) to push markdown into Anki. 🔵 Anki has the
   installed base; do not rebuild it.
5. **Instrument the claim** — [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
   (Apache-2.0) runs the A/B inside the client's LMS: same content, scheduled versus
   unscheduled, retention measured. **That comparison is the deliverable**, not the
   scheduler.

🟢 **Licence reach: none.** Every component is MIT or Apache-2.0.

🟡 **Two rows to leave out, and why.** [`trane-project/trane`](https://github.com/trane-project/trane)
(848 ★) and [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) (4 222 ★) are
the most interesting designs in this tier — a mastery dependency graph and a full
listening/speaking trainer — and **both are AGPL-3.0**. Study them; do not embed them in
a hosted client deliverable.

---

## 🆕 Pattern 11 — An England-curriculum tutor whose curriculum model stays the client's

**Problem.** A UK education client — an academy trust, a tutoring provider, a publisher —
wants a tutor aligned to the **National Curriculum for England**, and wants the enriched
curriculum model it builds (their sequencing, their question mappings, their mastery
thresholds) to remain **their closed asset**. 🔴 Pattern 7 cannot deliver this: it starts
from [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy), whose **ODbL-1.0**
share-alike reaches a *derivative database* — exactly what the client's enriched model
is.

**Why this pattern exists now.** `p357` verified
[`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology):
the Oak National Academy curriculum as **OWL/SKOS**, aligned to the National Curriculum
for England, with `ontology/`, `data/` and `docs/` under **OGL-3.0** and `scripts/` plus
workflows under **MIT**, both read at `main/LICENSE.md`. 🟢 **OGL-3.0 permits commercial
exploitation on attribution alone and imposes no share-alike.** That single difference is
what makes this pattern possible and Pattern 7 unsuitable.

**Recipe.**
1. **Curriculum spine:** the `ontology/` and `data/` trees of
   [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology)
   (OGL-3.0). Load the OWL/SKOS directly; its CI already validates the ontology and
   generates distribution files, so the client inherits a tested artefact rather than a
   parse job.
2. **Typed prerequisite reasoning over it:**
   [`devissaputra/curriculum_knowledge_graph`](https://github.com/devissaputra/curriculum_knowledge_graph)
   (**MIT**). It gives `PREREQUISITE_OF`, `TEACHES`, `ASSESSES` and `ALIGNS_WITH` with
   entity-type constraints enforced per relation — so "this lesson assesses an objective
   it never taught" is a **constraint violation**, not a review opinion. Its alignment
   diagnostics and provenance are what an inspection conversation needs.
3. **Mastery estimates:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) —
   Bayesian Knowledge Tracing, so progression claims are defensible.
4. **Scheduling:** [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
   (MIT) for review timing, as in Pattern 10.
5. **Reach the LMS over a boundary**, per Pattern 1: Moodle via
   [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) or
   [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (both **MIT**), Canvas
   via [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) or
   [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (both **MIT**).

**The licence boundary.** 🟢 **Every component is MIT except the curriculum data, which
is OGL-3.0 with no share-alike.** The client's enriched graph is theirs; the only
obligation that travels is one attribution string:

> *"Contains public sector information licensed under the Open Government Licence v3.0."*

🔴 **Two constraints to put in the statement of work, not discover later.** The ontology
covers **England** — not Scotland, Wales, Northern Ireland or any EU curriculum — and it
is **`v0.1.3`, early release**, so pin a commit and expect schema movement. 🟡 Neither is
a reason not to build; both are reasons to scope and version deliberately.

**Delivers.** A curriculum-aligned tutor whose alignment is *checkable against a
statutory curriculum* rather than asserted, and whose curriculum model is a closed
client asset. 🔵 Alignment-to-standard is what §2's evidence gate actually asks for in a
UK procurement.

## 🆕 Pattern 12 — Process-evidence assessment, for when the client's detector stops being accepted

**Problem.** A university or faculty has been running AI-detection scores in
academic-misconduct cases, and that has stopped working. `intel/trends.md` §16: Yale,
Cornell and UW–Madison now **discourage or bar detection scores** in misconduct
proceedings, after a Stanford study found detectors flagged **61 % of essays by
non-native English speakers** as machine-written. 🔴 **A better detector does not fix
this** — the failure is an equity failure across language backgrounds, not a model-quality
one — so the engagement is a **replacement**, not an upgrade.

**What replaces it.** The sources name the substitution: oral examination, proctored
assessment, and **grading the writing process**. Only the third is a software build, and
it is a **telemetry** build.

**Recipe.**
1. **Instrument the process, not the artefact.** Draft history, revision sequence,
   time-on-task and paste events are learning-analytics events. Emit them as **Caliper**
   events against [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec).
   🔴 **Implement the standard; do not vendor the document** — its grant is an IMS
   *specification document* licence, not a software grant (`agents/top.md`, licence
   flags).
2. **Carry the events over an LTI boundary**, so nothing forks the AGPL LMS:
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) for Node or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) for
   Python. Both carry the **role claims** that decide who may see a process trace — and
   a process trace is more intrusive than a grade, so that boundary is a privacy control,
   not plumbing.
3. **Keep supervision and similarity, which §16 does *not* retire.**
   [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) or
   [`eLearning-BS23/moodle-quizaccess_proctoring`](https://github.com/eLearning-BS23/moodle-quizaccess_proctoring)
   for supervised assessment; [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
   (**MIT**) for code similarity. 🟢 **Neither claims to know what produced the text**,
   which is exactly why both survive the reversal.
4. **Evidence it, because evidence is the procurement gate.**
   [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
   (Apache-2.0) runs a randomised comparison **inside** the LMS: process-evidenced
   assessment against the status quo, on the client's own cohort.
5. **If marking is automated anywhere in this, apply §17's three rules:** blind the
   human reviewer to AI provenance on the first pass (a labelled grade **anchors** the
   reviewer — measured across 1 339 teachers), build the **student opt-out as a routing
   path** the LTI role claims can actually serve, and keep the **rubric** as the artefact
   of record.

**The licence boundary.** Apache-2.0 and MIT throughout; the LMS is reached over LTI 1.3
and never forked. 🟢 Nothing in this pattern obliges the client to open anything.

**Delivers.** An assessment-integrity posture that survives the objection that killed
the detector — defensible across language backgrounds, with the evidence to prove it on
the client's own students. 🔵 **And it is a budget conversation the client is already
having:** the money is currently committed to a detection line item that their own
academic board is moving away from.

## 🆕 Pattern 14 — A credential a regulator will accept, assembled from the standards bodies' own code

**Problem.** A client — a university, a ministry skills programme or a corporate academy —
wants to issue digital credentials that a third party can verify, and wants them to still
verify in five years. Their procurement will not accept a proprietary badge platform, and
their legal team will not accept a copyleft obligation on the issuing service.

**Why this pattern did not exist here until `p371`.** 🔴 §6 of
[`intel/trends.md`](../intel/trends.md) has called credentials *"the skills-based hiring
substrate"* since early in this base's life, and these shelves carried almost no
credentialing rows — because the instrument that decides what may be shelved had no word
for `open badge` or `verifiable credential`. The out-of-sample run that found the gap is in
[`agents/trending.md`](../agents/trending.md); the tier it produced is on
[`agents/top.md`](../agents/top.md).

**Recipe.**
1. **Validate against the standard before writing an issuer.** [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) (Apache-2.0, `HEAD/LICENSE` @ `6bf38234c7cb`) is the **standards body's own** validator, and [`IMSGlobal/openbadges-validator-core`](https://github.com/IMSGlobal/openbadges-validator-core) (Apache-2.0, `HEAD/LICENSE` @ `0a66b52a8a0b`) covers Open Badges. Run both in CI from day one: conformance is the deliverable, not a late check.
2. **Issue and sign** with [`digitalcredentials/sign-and-verify`](https://github.com/digitalcredentials/sign-and-verify) (MIT, `HEAD/LICENSE` @ `6be5b41815b7`) over the data model in [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) (BSD-3-Clause, `HEAD/LICENSE` @ `15fb01872c49`), with subject identifiers resolved by [`digitalcredentials/did-io`](https://github.com/digitalcredentials/did-io) (BSD-3-Clause, `HEAD/LICENSE` @ `7040fac9167b`). 🔵 All three are **MIT Digital Credentials Consortium** code, which is the reference implementation a sceptical registrar is most likely to already know.
3. **Verify in the browser, with no backend**, using [`digitalcredentials/verifier-core`](https://github.com/digitalcredentials/verifier-core) (MIT, `HEAD/LICENSE.md` @ `e86bb791f7c5`), and give the client something to look at on day three with [`digitalcredentials/verifier-plus`](https://github.com/digitalcredentials/verifier-plus) (MIT, `HEAD/LICENSE` @ `2378d988ab2b`).
4. **Bind each credential to a competency**, not a course title, with [`cassproject/CASS`](https://github.com/cassproject/CASS) (Apache-2.0, `HEAD/LICENSE` @ `30929d303659`) — the competency-and-standards framework store. This is what makes the credential mean something to an employer.
5. **Where immutability is a procurement requirement**, anchor with [`blockchain-certificates/cert-issuer`](https://github.com/blockchain-certificates/cert-issuer) (MIT, `HEAD/LICENSE` @ `199cd8be7c1d`) rather than building it; treat it as optional and justify the cost.
6. **For an EMEA client, map to the European Learner Model** with [`impierce/credential-converter`](https://github.com/impierce/credential-converter) (OpenBadges v3 ↔ ELM/Europass). 🔴 **Do NOT cite [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) as a live dependency** — its README's first line is *"Archived Repository — no longer updated."* The model is live; that repository is not.

🟢 **Licence boundary:** every component is MIT, Apache-2.0 or BSD-3-Clause, so the issuing
service can ship closed. 🔴 **The diligence step that is not optional:** 235 of the 1 859
addresses graded at `p371` carry **no licence file at all**, and the credentialing class is
no cleaner than the rest — check the payload, at a pin, before any address enters the build.

**Effort.** 6–8 weeks to a conformant issuing and verification service with competency
binding; add 2–3 weeks for the ELM mapping on an EMEA engagement.

---

## 🆕 Pattern 15 — A LATAM university engagement that integrates the incumbent the client actually runs

**Problem.** A Brazilian or Argentine university wants AI support for students —
advising, timetable help, progress and risk signals. The proposal template says "integrate
with the LMS and the SIS."

**🔴 The mis-specification this pattern exists to prevent.** `p370` graded the
incumbent-LMS bridge class and reached ten platforms: Moodle, Canvas, Blackboard Learn,
D2L Brightspace, Schoology, PowerSchool, Ellucian Banner, Khan Academy, India's NCERT and
Norway's UDIR. **Every one is North American, European or Asian software.** 🔴 **Brazilian
federal universities run `SIGAA`. Argentine national universities run `SIU-Guaraní`.
Neither appears in that table, and neither has a published API contract on these shelves.**
A proposal that budgets a Canvas or Banner connector for a LATAM higher-education client
has specified the wrong incumbent before any licence question arises.

**Recipe.**
1. **Start from the three permissive reaches that exist**, and size them honestly as
   starting points rather than platforms: [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) (MIT, `HEAD/LICENSE` @ `6962638adbdd`, placed on `documentacion.siu.edu.ar`) for SIU-Guaraní; [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (MIT, `HEAD/LICENSE` @ `7373c6abac62`, `sigaa.ufpb.br`) and [`luthierycosta/ConsertandoHorariosSIGAA`](https://github.com/luthierycosta/ConsertandoHorariosSIGAA) (MIT, `HEAD/LICENSE` @ `5a6106ed9ce2`, `unb.br`) for SIGAA. 🟡 **8, 8 and 42 refs** — read them as documentation of the integration surface, not as libraries to depend on.
2. **Budget the connector as discovery work**, because it is. Scope a two-week spike to
   establish what each installation exposes before committing to an integration estimate;
   `SIGAA` is deployed per-university and the surface differs between them.
3. **Ground the pedagogy in the regional corpus**, not a translated US one:
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT, `HEAD/LICENSE` @ `21a43a395ab4`, sourced from Chilean teacher-training material)
   gives a measurable baseline, and the BNCC alignment path is Pattern 2.
4. **Add the public-data layer the region does publish openly**:
   [`dasgltd/mcp-brasil`](https://github.com/dasgltd/mcp-brasil) (MIT, `HEAD/LICENSE` @
   `2efb258370b1`) for Brazilian federal open data and
   [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) (MIT, `HEAD/LICENSE` @
   `940a63783461`) for Chile's. 🟢 This is where LATAM supply is genuinely strong.
5. **Keep the compliance surface explicit.** 🔴 **Brazil's PL 2338 is still a bill**; the
   binding instrument is **LGPD**, and Brazil's AI regulatory sandbox runs to **December
   2026**. Design for LGPD now and for the framework later.

🟢 **Licence boundary:** every component named is MIT. 🔵 **The deliverable that makes this
engagement defensible** is the integration specification for the client's own SIGAA or
SIU-Guaraní installation — on this base's evidence, nobody has published one, which makes
it an asset rather than overhead.

**Effort.** 2 weeks of integration-surface discovery, then 8–10 weeks to a grounded
advising assistant against one installation. 🟡 Do not quote a fixed connector price before
the spike.

---

## 🆕 Pattern 13 — A statutory inclusion deliverable for a Colombian school system

🔵 **The shape that makes this different from every other pattern on this file:** it is
not a capability a client might want, it is **a document Colombian law obliges a school
to produce.** `Decreto 1421 de 2017` makes the **PIAR** — *Plan Individual de Ajustes
Razonables* — mandatory for educational provision to students with disabilities, and
`Ley 2216 de 2022` extends inclusive-education duties to specific learning disorders
(dyslexia, ADHD, dyscalculia). The budget line is **CONPES 4144**, Colombia's national AI
policy, funded to 2030.

**Components**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| PIAR system of record | [`Dramoscuello/openpiar`](https://github.com/Dramoscuello/openpiar) | 🔴 **AGPL-3.0** | Already models the PIAR workflow and emits the documents the decree requires. Its AI assistant proposes DUA adjustments from the student profile, the institution's PEI, the subject and teacher-declared barriers |
| Tutoring layer | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | 🟢 **MIT** | Autonomous tutor agent already running **inside Open edX** against real courses at Universidad Tecnológica de Pereira. TTS replies, animated avatar, teacher statistics panel, context persisted across sessions |
| Host platform | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) + [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | `TutorIA` is built for it, so the integration is proven rather than designed |
| Offline assessment | [`Riskbreaker2077/open-test`](https://github.com/Riskbreaker2077/open-test) | 🟢 **MIT** | Local server, school intranet, **every student a different paper**. No connectivity required |
| Oversight record | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) pattern | 🟢 MIT | Copy its **preview-first write protocol**: no grade or adjustment is written without an explicit confirmation step |

**Wiring**

1. Deploy `openpiar` **for the client, as the client's system** — 🔴 AGPL-3.0 means this
   is a deployment, not a product Globant folds into an offering. Price it accordingly.
2. Run `TutorIA` as the learner-facing agent inside the client's Open edX. 🟢 Its MIT
   grant means **the tutor customisations can stay closed** even though the platform under
   it is AGPL — the boundary is Open edX's plugin/XBlock edge, exactly as this file's
   governing rule requires.
3. Feed the PIAR's declared barriers into `TutorIA`'s prompt context, so the reasonable
   adjustments the decree records are the adjustments the tutor actually applies.
   🔵 **This is the whole value of the pattern**: elsewhere the PIAR is a filed PDF.
4. Use `open-test` for assessment in schools without reliable connectivity, with its
   per-student randomisation standing in for invigilation.
5. Gate every write — adjustment, grade, PIAR revision — behind a **recorded teacher
   confirmation**. 🟢 No Colombian statute compels this yet; the EU AI Act and Vietnam's
   Law 134/2025/QH15 both do, so building it now makes the same deliverable exportable
   (see `intel/trends.md` §20).

**What the engagement delivers.** A funded, statutory compliance system — not a pilot —
with the tutoring layer as the part that stays proprietary. 🔴 **Licence boundary to
hold:** `openpiar` is network copyleft; any Globant modification to *it* is the client's
under AGPL. Keep Globant IP in the `TutorIA` layer and in the oversight record.

## 🆕 Pattern 14 — Reaching a client's LMS when "LTI support" is not one capability

🔵 **The failure this prevents.** An engagement scopes "we'll write grades back to the
client's LMS over LTI", picks an LTI library from a roundup, and discovers at integration
time that the library does **launches only** — no AGS, so no grade can be submitted.
`p358` found exactly that row:
[`SanDiegoCodeSchool/lti-node-library`](https://github.com/SanDiegoCodeSchool/lti-node-library)
is MIT, live, and its own README states NRPS and Deep Linking are not supported.

**Decide in this order, and the first question is not technical**

| Need | Component | Licence | Note |
|---|---|---|---|
| Node, full Advantage | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | 🟢 **The default.** Launches, Deep Linking, grades, roles. 🟡 Pin a version — its README describes v7 as a full rewrite |
| Python agent | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT | Deep Linking, AGS, NRPS. The default when the agent is Python, which on this base it usually is |
| Typed end-to-end | [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | 🟢 MIT | Deep Linking 2.0, JWKS. 🟡 **RS256 only**, and its docs are explicit that the library *"never decides who may configure content"* — the tool must enforce that authorisation itself |
| Client runs Phoenix/Elixir | [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) | 🟢 MIT | The only BEAM-runtime option on this base |
| Canvas specifically | [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl) | 🟢 MIT | Canvas app framework; pairs with `ltijs` |
| 🔴 **Never** | [`oat-sa/lib-lti1p3-deep-linking`](https://github.com/oat-sa/lib-lti1p3-deep-linking) | 🔴 **GPL-2.0** | IMS-certified — a conformance claim, not a grant. Strong copyleft **on a library** |
| 🔴 **Never** | [`GSU-CETLOE/lti1p3Library-php`](https://github.com/GSU-CETLOE/lti1p3Library-php) | 🔴 MIT, **no licensor named** | Holder line is the unfilled template `[Your Name / Organization]`. Nobody to attribute, and attribution is MIT's only condition |
| 🔴 **Never** | [`blackboard/BBDN-LTI-Tool-Provider-Node`](https://github.com/blackboard/BBDN-LTI-Tool-Provider-Node) | 🔴 **no grant** | A vendor-org reference sample with no `LICENSE` is as unusable as a student project with none |

**Wiring**

1. **Write down which of the four services you need before choosing** — launch, Deep
   Linking, AGS, NRPS. 🔵 If the deliverable writes grades, AGS is non-negotiable and it
   is the service most small libraries omit.
2. Stand the tool up against the client's LMS as an **LTI 1.3 tool**, never a fork — this
   is what keeps Canvas's and Open edX's AGPL on their own side of the boundary.
3. Where MCP is also available, prefer it for *agent* access and keep LTI for
   *platform* integration. 🔵 They are not alternatives: LTI is how the LMS launches your
   tool; MCP is how your agent reads the LMS. A complete engagement usually needs both.
4. 🔴 **Before vendoring any connector, read its `LICENSE` copyright holder.** If it names
   someone other than the repository owner it is a fork, and on `p358`'s evidence a fork
   is **18 to 27 tools behind** its upstream. Install by registry identifier instead — it
   resolves upstream regardless of which page you found (`intel/trends.md` §21).

**What the engagement delivers.** A grade-writing, roster-aware LMS integration whose
licence position is defensible, chosen on capability rather than on a roundup's ranking.

## 🆕 Pattern 15 — A Kenyan K-12 administration deliverable that can stay closed

🔵 **Why this pattern exists now and could not before.** `verticals/solutions.md` has
carried one of this base's most expensive findings — **there is no permissive education
ERP**, so a closed administration deliverable must be priced as a build. 🟢 `p358` found
the first permissive row on that tier, and it is narrow enough that the finding still
holds for institution-wide ERP while no longer holding for K-12 school administration.

**Components**

| Role | Repo | Licence | Note |
|---|---|---|---|
| Administration base | [`Moha-abshir/SMS`](https://github.com/Moha-abshir/SMS) | 🟢 **MIT** | Multi-role school management built against **Kenya's CBC**. TypeScript 5.3, React 18, Node 20, Drizzle ORM, PostgreSQL 16. 🟡 Single author, 2026, no deployment evidence — see `ACTION ZZ-bh` |
| National-data connector | [`gabrielmahia/elimu-mcp`](https://github.com/gabrielmahia/elimu-mcp) | 🟢 MIT | Kenya school registry, KCSE/KCPE, HELB loans, TVET. 🔴 **Its README states the shipped data is DEMO and "not suitable for operational decisions"** — this supplies the tool surface and schema; real endpoints and credentials are the engagement's to obtain |
| Offline learning | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | Offline-first by design. The licensed answer to the connectivity constraint |
| Offline assessment | [`Riskbreaker2077/open-test`](https://github.com/Riskbreaker2077/open-test) | 🟢 MIT | Local server over school intranet, per-student randomised papers |

**Wiring**

1. Fork `Moha-abshir/SMS` as the administration base. 🟢 MIT means the fork and every
   customisation **can stay in a closed client deliverable** — the one place on this base's
   administration tier where that is true.
2. Add `elimu-mcp` as the agent's read surface over Kenyan national education data, 🔴 with
   its demo data replaced by real endpoints before anything operational depends on it.
   🟡 Note its README also states **pull requests are not accepted**: an engagement that
   patches it owns a fork from that day.
3. Serve learning content through `kolibri`, which assumes no connectivity rather than
   degrading without it.
4. Assess with `open-test` on the school's own intranet.

**What the engagement delivers.** A closed, CBC-aligned school administration system with
an AI layer over national data, deliverable in a market where connectivity cannot be
assumed. 🔴 **The honest caveat to carry into the proposal:** the administration base is a
**young single-author project**, not a vendor-backed platform. For an *institution-wide*
ERP the recommendation is still `openeducat_erp` (LGPL-3.0) or a priced build — one school
management system is not an ERP, and `verticals/solutions.md` sets out the comparison.

## 🆕 Pattern 16 — A special-education IEP deliverable, built because it cannot be adopted

🔴 **Why this pattern is a build and not an integration.** `p359` measured the
special-education tier first-hand: **seven addresses, one permissive grant.** Two of the
seven — including the only genuinely mature one, at **1 281 commits and 12 authors (`%ae`)**, corrected `p362` — are
**explicitly noncommercial** (`CC-BY-NC-4.0` and `PolyForm Noncommercial 1.0.0`), and
four carry **no licence file at all**. 🟢 This is the clearest build-rather-than-adopt case
on these shelves, and §23 of `intel/trends.md` explains why it is likely to stay that way.

🔵 **And why it is worth building anyway.** An IEP is a **statutory document** — under
IDEA in the United States, with binding analogues across `intel/market.md`'s
jurisdictions — which means the deliverable has a compliance budget, a named owner at the
client, and an audit trail requirement. Those are the three things that make an
engagement fundable.

**Components — every grant read from payload, `2026-10-21`**

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Records, assessments, IEP workflow | [`dg13788/iep-system`](https://github.com/dg13788/iep-system) | 🟢 **MIT** (`main/LICENSE`) | **The one permissive row on the tier.** Student records, assessment capture, a five-step IEP wizard, e-signatures. React / PHP / MySQL. 🟡 Chinese-language UI, 38 commits, 4 authors (`%ae`) — take the **data model and workflow**, expect to rewrite the presentation layer |
| Goal drafting over client documents | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0** | Already carried on `agents/top.md`. Skills as the packaging for pedagogical instructions — §8 of `intel/trends.md` — so goal-drafting guidance stays **the client's content**, not vendored code |
| Compliance + specialist agents | [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | 🟢 **MIT** (`main/LICENSE`) | Already held. School Assistant **plus 12 specialists**, including a **`special-education-agent`**, `assessment`, `curriculum-alignment` and `student-safety`, with PowerSchool skills. 🟢 **This is the row that corrected `T-p288b`, and it is the only permissive special-education *agent* on this base** |
| Progress evidence store | [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | 🟢 **Apache-2.0** | 🆕 `p359`. xAPI **1.0.3 and 2.0** conformant, admin UI, OpenTelemetry. **An IEP's legal weight is its progress record** — this is where goal-progress statements land in a standard format rather than a bespoke table |
| Mastery / difficulty calibration | [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** (`main/LICENSE.txt`) | 🆕 `p359`. **The only maintained permissive IRT engine** — committed 2026-10-19. Turns "the student is progressing" into a calibrated estimate a hearing officer can be shown. 🔴 Not `eribean/girth`: same licence, untouched since 2022 |
| Reaching the client's LMS | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) or [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 MIT | Read coursework and grades across the protocol boundary. 🔴 **Never** `openedx-mcp` or `csmediapro/moodle-mcp-server` — copyleft connectors sit *inside* the deliverable |

**Wiring**

1. **Fork `dg13788/iep-system` for the data model, not the UI.** MIT means the fork and
   every customisation stay in a closed client deliverable. 🟡 Budget the presentation
   layer as a rewrite: the workflow is the asset, the Chinese-language React surface is
   not reusable in an English-, Spanish- or Portuguese-language engagement.
2. **Put goal drafting behind a skill pack, not in code.** Package the client's own
   jurisdictional guidance — IDEA goal grammar, the state's required fields, the
   district's templates — as skills on the `k12-teacher-skills` pattern. 🟢 **The
   client's pedagogy stays the client's**, and the same deliverable re-targets to another
   jurisdiction by swapping a skill directory.
3. **Write every goal-progress observation to `xapi-lrs` as an xAPI statement.** This is
   the step that makes the deliverable defensible: a standard, queryable, timestamped
   record rather than rows in the application's own database. 🟢 It is also what §2's
   evidence-of-impact procurement gate asks for, already in a portable format.
4. **Calibrate with `irtorch` where the client's goals are measured by assessment
   items.** Progress on an uncalibrated item set is not evidence. 🔵 The join of a
   permissive IRT engine to an LLM-assisted grader is **unbuilt** — `repos/foundations.md`
   §Psychometrics records the gap — so this step is engineering work, not configuration.
5. **Read coursework over MCP; never fork the LMS.** Standard boundary rule.
6. 🔴 **Put a human in the loop at the decision, by construction.** Oklahoma and Maryland
   now **require human oversight and bar AI from high-stakes decisions about students**
   (`intel/market.md` §North America); Korea's AI Basic Act names education a high-impact
   sector; Vietnam's Decision 33/2026 lists education as high-risk where output drives
   decisions without meaningful human review; and Annex III of the EU AI Act names
   education assessment by type. 🟢 **The model drafts and the case manager signs** —
   which is also exactly what `HernanDiaz/moodle-local_aigrader` demonstrates on the
   grading side, and a working reference worth reading even though its GPL-3.0-or-later
   grant keeps it outside the deliverable.

**What the engagement delivers.** A closed, jurisdiction-targeted IEP drafting and
progress-evidence system: statutory fields enforced, goals drafted under the client's own
pedagogical guidance, every progress observation in a standard xAPI record, calibrated
mastery estimates behind the progress claims, and a human signature at every decision
point.

🔴 **The honest caveats to carry into the proposal.**

- **The permissive base is a 38-commit project.** `dg13788/iep-system` is the *only*
  permissive option measured, not a safe one. Price the data-model fork as a read-and-
  reimplement, not as an adoption.
- 🔴 **Do not reach for the mature alternatives.** `The-Burnes-Center/a-iep` is the best-
  maintained special-education codebase this base has found and it is **CC-BY-NC-4.0**;
  `boktoday/iep-agent-hermes-agent` is **PolyForm Noncommercial**. Both read as "free" and
  neither can be used in paid work. 🟢 This is the single most likely way this engagement
  goes wrong.
- 🔴 **Four of the seven addresses have no grant** — including the one with the closest
  architecture to this pattern, `omerpanay/special-education-rag` (agentic teacher
  assistant with IEP draft generation over RAG). 🔴 **And the same is true of a row this
  base has held for far longer:** `eakarsu/ai-special-education-iep-compliance` covers
  evaluation timelines, service delivery and annual reviews — exactly this pattern's
  compliance surface — and carries **no grant in 21 files**, re-confirmed at `p359`. 🟢 It
  is a **requirements document**, not a component. 🟢 **Ask for the grant before designing
  around any of them.** Per §22 of `intel/trends.md`, these authors are not withholding a licence;
  they have never been asked for one, and a two-line email is the whole intervention.
- 🟡 **The data is special-category under every privacy regime that matters.** An IEP
  contains disability and health information: **GDPR Art. 9** in EMEA, FERPA plus state
  student-privacy statutes in the US (California **AB 1159** restricts using student data
  to train models at all), and LGPD Art. 11 in Brazil. Settle the lawful basis and the
  training-data position **before** the architecture, not after.

## 🆕 Pattern 17 — An AI layer on a French ENT, built beside the portal because AGPL reaches a fork

**Client shape.** A French *région*, *département* or académie — or the integrator holding
its contract — running an **ENT** (*Espace Numérique de Travail*) for every school in its
territory. One regional deployment reports **2.7 M users across 5 790 institutions**. They
want AI on top of data that already exists in the portal — the *cahier de textes*, the
competency record, attendance — and the deliverable must stay the integrator's property.

**Why this pattern did not exist one pass ago.** This base held the *interchange* layer
(LTI, SCORM, xAPI, Caliper, OneRoster) and a row of LMSes, and had **no row for a national
school portal**. `p360`'s French function legs shelved the ENT stack.

**The licence boundary, decided before anything else.** The entire ENT tier is
**AGPL-3.0**. 🔴 Forking `entcore` or any module carries network copyleft into whatever the
client deploys. 🟢 `entcore` is *a modular kernel with its own HTTP API and a module
boundary* — that boundary is the pattern.

**The stack, every grant read from the payload on 2026-10-21:**

1. **The portal, left alone.** [`edificeio/entcore`](https://github.com/edificeio/entcore)
   (🟡 **AGPL-3.0**, `master/LICENSE`, default ref 🔴 `master`). 🟢 **Deploy or extend it as
   a module, and keep your own service out of its process.** Use this address: 🔴
   `open-ent/entcore` is five months stale, `OPEN-ENT-NG/entcore` is a single-branch mirror
   one commit behind, and `opendigitaleducation/entcore` is the *same repository* under the
   vendor's former name.
2. **The statutory data you are reasoning over.**
   [`OPEN-ENT-NG/cahier-de-textes`](https://github.com/OPEN-ENT-NG/cahier-de-textes)
   (AGPL-3.0, `dev/LICENSE`) is the lesson log — per-session lessons, homework,
   attachments. [`OPEN-ENT-NG/competences`](https://github.com/OPEN-ENT-NG/competences)
   (AGPL-3.0, 🔴 `dev/LICENCE`) carries the *livret scolaire* competency model, which is
   the mastery signal this build needs and the reason not to invent one.
   [`OPEN-ENT-NG/presences`](https://github.com/OPEN-ENT-NG/presences) (AGPL-3.0, 🔴
   `dev/LICENCE`) is attendance.
3. **Read them over the API, from your own service.** The AI service is a separate process
   that authenticates to `entcore` and reads those modules' endpoints. 🟢 **This is the
   whole licence argument**: AGPL-3.0's network clause binds the portal's own source, which
   is already published, and does not reach a separate program that talks to it.
4. **Mastery estimates that survive a *conseil de classe*.**
   [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (🟢 **MIT**) for Bayesian Knowledge
   Tracing over the competency records — a defensible per-competency estimate rather than a
   model's opinion, which is what a French teachers' council will actually interrogate.
5. **Exercises, if the client wants them inside the portal.**
   [`open-ent/exercizer`](https://github.com/open-ent/exercizer) (AGPL-3.0, 🔴
   `master/LICENCE`) already does MCQ, cloze and ordering with auto- and hand-marking.
   🟢 Extend it as an ENT module and the copyleft stays on the portal side where it already
   is; 🔴 do **not** lift its code into the closed service.
6. **Paper, because French assessment is still largely paper.**
   [`ajjalti/EvalStudio`](https://github.com/ajjalti/EvalStudio) (🔴 **AGPL-3.0**) does
   computer-vision marking of **scanned copies**. 🔴 Run it as its own service behind a
   queue — not linked into the deliverable — or reimplement the step; it is the one
   component here whose licence would otherwise reach the client's code.
7. **Disclosure, because this is the EU.** The EU AI Act treats education uses as
   high-risk and its obligations bite from **2 Aug 2026**. Wrap the whole thing in
   **Pattern 3**'s conformity layer; the competency record makes this an assessment system,
   not a chatbot.

**What the engagement delivers.** A closed AI service beside an AGPL portal the client
already owns, reading statutory data in place, with per-competency mastery estimates and an
Act-ready disclosure and oversight record.

🟡 **Price discovery from the source tree, not the documentation.** `entcore`'s README
still specifies **JSE 7** and a clone URL on a decommissioned host, while the code took a
commit on **2026-10-20** from **139 authors (`%ae`)** over 11 714 commits — corrected `p362` from the published `21`. 🔴 An estimate built by reading that README will
be wrong in the expensive direction.

🟢 **The market note that makes this a migration pattern rather than a greenfield one.**
The IGÉSR inspectorate (15 Jul 2025) puts ENT in **62 %** of French public primary schools
and records that one family can face **three different ENT solutions** across école,
collège and lycée, recommending territorial harmonisation and ÉduConnect. 🔵 Harmonisation
work is the near-term budget; the AI layer is what makes it worth doing twice.

## 🆕 Pattern 18 — Curriculum-bound exam generation for a national curriculum, with the generator swapped out

**Client shape.** A ministry, publisher, school group or teacher co-operative in a country
with a prescribed national curriculum, where teachers hand-write assessments. The
Indonesian case is measured: **4–8 hours a week** per teacher producing exams in a word
processor.

**Why the obvious build is wrong.** The tempting move is a prompt plus a PDF template.
🔴 It fails on the thing that actually matters, which is **curriculum binding** — an item
that does not map to a declared learning objective is unusable to the teacher who has to
justify the paper, and a model will produce plausible items that map to nothing.

**The reference implementation to start from, and the part to replace.**

1. **The orchestration** — [`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam)
   (🟢 **MIT**, `main/LICENSE`, © *Naufaldi Rafif*; **435 commits, 4 authors (`%ae`)**, live
   deployment). One sentence in, an A4 print-ready paper out: mixed item types, answer key,
   and a teacher-facing *pembahasan* per item, bound to **Kurikulum Merdeka** CP/TP by an
   explicit review step. 🟢 **MIT, so fork it into the deliverable.**
2. 🔴 **The part that must be replaced.** Its core generation calls a **hosted proprietary
   model**. For a ministry deployment that is usually the blocker — data residency,
   procurement, or simply cost per paper. 🟢 **The curriculum binding and the print
   pipeline are the valuable, reusable parts**; the generator is a swap.
3. **Swap in an item bank with a review workflow** —
   [`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) (🔴 AGPL-3.0,
   run as its own service) or [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
   (🟢 MIT) where the subject is programming. 🟢 **Generate once, review, then reuse** —
   which converts a per-paper model cost into a one-off authoring cost and is what makes
   the economics work at ministry scale.
4. **Keep a human gate on free text, and say so.**
   [`nvaes/CEB`](https://github.com/nvaes/CEB) (🟢 MIT, 🇧🇪) is the posture to copy: it
   auto-marks **only** the checkbox items and states that automatic marking of free text
   would be unreliable. 🔵 That sentence in a ministry proposal is worth more than a
   benchmark.
5. **Paper in, paper out.** [`ajjalti/EvalStudio`](https://github.com/ajjalti/EvalStudio)
   (🔴 AGPL-3.0, own service) marks the scanned copies back. 🟢 The loop closes without the
   school needing a device per pupil, which is the constraint in most of the countries this
   pattern is for.
6. **Report into whatever the school runs**, over LTI or the portal's API — Pattern 14 for
   the LMS case, Pattern 17 where the client runs a national portal.

🔴 **The licensing warning this pattern exists to carry.** Of **20** live Indonesian
addresses `p360` probed, **one** carries a usable, author-attributed permissive grant over
actual software. The best-built one — `sira313/rapkumer`, **203 commits** — is under a
bespoke licence whose §3 prohibits commercial use *in any form*, explicitly including paid
installation, configuration or support. 🟢 **Read the payload before the README, and in
this market expect to ask the author.** Three other grant files in that leg did not survive
scrutiny: one is a marketing site, one names a **framework vendor** as copyright holder,
and one is the non-commercial licence above.

## Boundary cheat-sheet

| If the host platform is… | Reach it by… | Never |
|---|---|---|
| Canvas, Open edX, Frappe LMS, ClassroomIO (**AGPL**) | LTI 1.3 tool · MCP server · web services | Forking, or linking client code |
| Moodle, Chamilo, ELMSLN, Judge0, UDOIT, 🆕 HUSTOJ, 🆕 openSIS Classic (**GPL**) | Web services · the plugin API as a *separate* deployed plugin · the API over HTTP | Statically linking into proprietary code |
| 🆕 Hydro, DMOJ, the AGPL item banks, 🆕 **educa-lrs** (**AGPL**) | The client's own deployment, reached over HTTP | Hosting it as the studio's service |
| 🆕 **Sharif Judge** (**GPL-3.0** — 🔴 moved out of the AGPL row, `p362`) | The client's deployment **or** a studio-hosted service — GPL has no network clause | Distributing a modified build without its source |
| BigBlueButton, OpenEduCat (**LGPL**) | Dynamic linking · API | Forking into closed source |
| OpenOLAT, Sakai, Kolibri, Moodle App, Opencast, QingdaoU OnlineJudge **+ OnlineJudgeFE**, Otter-Grader, py-fsrs, LectureLab, `bruchris/canvas-lms-mcp`, `G36maid/moodle-mcp`, 🆕 **XiaoCow666/CodeSense**, 🆕 **tura-learn/Dhee**, 🆕 **nuwa-skills/montessori-skill** (**permissive**) | Anything, including forking | — |
| 🔴 🆕 **QingdaoU/Judger**, **QingdaoU/JudgeServer** (**SATA** — MIT body **plus obligations**; 🔴 removed from the permissive row, `p362`) | Honouring the notice: star the project, thank the authors, keep its copyright and project-url block intact — or keeping execution outside the deliverable, over HTTP | Shipping it as *"MIT"*, or into any engagement whose procurement rule says OSI-permissive only |
| 🔴 🆕 **QingdaoU/OnlineJudgeDeploy** (**no grant**, ref `2.0`) | 🔴 **Reading it as documentation** for how the services wire together | Vendoring the compose files into a deliverable |
| 🔴 🆕 **CaviraOSS/PageLM** (**PageLM Community License**), 🆕 **Samkarya/online-exam-questions** (**ENCOSL**) | 🔴 **Nothing in paid work** — both are non-commercial; PageLM also requires a revenue-sharing agreement, and applies itself *"in whole or in part"* | Any commercial use. 🔴 Both were published on these shelves as **MIT** until `p362` |
| 🆕 ERPNext (**GPL-3.0**) | Its **REST API**, as a separate service | A Frappe app in-process, or linking client code |
| 🆕 Cap, CaptureFlow (**split: AGPL app, MIT engine**) | Vendoring the **MIT engine only** — `licenses/LICENSE-MIT`, `packages/engine/` | Forking the repository; the combined distribution is AGPL |
| 🔴 🆕 `csmediapro/moodle-mcp-server` (**AGPL-3.0 connector**) | 🔴 **Nothing.** Use a permissive Moodle MCP instead | Any use — a copyleft *connector* sits inside the engagement, not across the boundary |
| 🔴 🆕 `mrgutierrezmario/lecture-note-app`, 🆕 `boktoday/iep-agent-hermes-agent` (**PolyForm Noncommercial**) | 🔴 **Nothing in paid work** | All commercial use without a separate licence from the holder |
| 🔴 🆕 `The-Burnes-Center/a-iep` (**CC-BY-NC-4.0**) | 🔴 **Nothing in paid work.** Read it as a reference for parent-facing IEP explanation, build the deliverable from `dg13788/iep-system` | Any commercial use — and note it is the *best-maintained* special-education codebase on this base, which is what makes it dangerous |
| 🆕 `HernanDiaz/moodle-local_aigrader` (**GPL-3.0-or-later**) | Deploy it as a **plugin inside the client's own Moodle** | Vendoring it into a studio deliverable |
| 🟢 🆕 `Apereo-Learning-Analytics-Initiative/OpenLRW` (**ECL-2.0** — permissive) | Anything, including forking — ECL-2.0 is Apache-2.0 with a narrowed patent grant | 🔴 Depending on it: **last commit 2020-02-06.** Read the OneRoster↔Caliper↔xAPI schema, deploy `pelotech/xapi-lrs`. 🔵 **Corrected `p361`** — `p359` cited the 0 ★ fork `jeffyding/OpenLRW` and dated it 2018; that was the fork's date, not the project's |
| 🔴 🆕 `shaheeranser/exam-proctor` (**Apache-2.0** — permissive) | Reading its LTI 1.3 wiring and AGS grade passback as a **reference architecture** | 🔴 Deploying it into an EU engagement as it stands: GDPR Art. 9 biometrics, and clear of the Art. 5(1)(f) prohibition only because one MediaPipe default is unset |

**One-line version:** in education, the licence picks the architecture. Decide the
boundary before the stack.

🔴 **🆕 And `p357` found the one case where that rule inverts.** Every row above assumes
the copyleft component is the **platform**, which a protocol boundary holds at arm's
length. When the copyleft component **is the connector** — an AGPL MCP server — the
boundary is on the **wrong side of it**: the client's agent talks to it over exactly the
network interface AGPL's clause is written about, and it sits inside the deliverable
rather than across from it. 🟢 **So check the licence of the connector before the
licence of the platform.** It is the smaller component and the larger risk.

---

## 🆕 Pattern 19 — Sweden's curriculum from the regulator itself — and the access layer Pattern 11 was missing

**Problem.** `Pattern 2` works for Brazil because the BNCC is published as open data, so
an alignment claim is checkable objective by objective. `Pattern 11` works for England
because Oak National Academy publishes the curriculum as an **ontology** under OGL-3.0.
🔴 **Neither gives the agent a retrieval surface, and no third country had either.**
`p361` closes both gaps.

### 19a — Sweden, where the source is the regulator

1. **Curriculum, schools and statistics** from 🆕 [`isakskogstad/Skolverket-MCP`](https://github.com/isakskogstad/Skolverket-MCP) — **MIT**, read from 🔴 `master/LICENSE` (**not** `main`). It fronts **Skolverket**, Sweden's National Agency for Education, across three public API endpoints and is tuned for LLM queries.
2. **Pedagogical behaviour** as skills: [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (Apache-2.0) or [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) (886 ★).
3. **Mastery estimates that survive a review:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) for Bayesian Knowledge Tracing, or [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT) to get BKT behind an MCP boundary.
4. **Quality-gate the output:** [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (MIT).
5. **Surface it in the LMS** over LTI 1.3: [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT).

🟢 **Why this is defensible to a Swedish client:** the curriculum provenance is the
national agency's own API, not a vendor dataset and not a scrape. 🔵 That is a stronger
provenance story than anything else on this base outside Brazil's BNCC.

### 19b — England: the access layer that `Pattern 11` names no component for

🔴 **`Pattern 11` gives the client a curriculum *model* (OWL/SKOS under OGL-3.0) and
leaves them to build retrieval over it.** 🟢 🆕 [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem)
is that retrieval layer from the same publisher: API, SDK and an **MCP app** over the Oak
Open Curriculum data, **MIT**, read at 🔴 **`main/LICENCE`** — and `main/LICENSE`
**404s**.

🔵 **Compose them, do not substitute.** The ontology is what the client enriches and
keeps as a closed asset (Pattern 11's whole point); the ecosystem is how the agent
*reaches* it at run time. 🟢 Both are permissive enough that the enriched model stays
the client's.

🔴 **Read that grant path twice.** A national curriculum body spells its licence file
`LICENCE`, and a scanner that probes `main/LICENSE` and stops reports England's open
curriculum programme as unlicensed. 🔵 This base warns about exactly that on
`repos/foundations.md`, and `p361` is the pass that produced a first-party instance.

### What is still missing, stated

🔴 **Three countries now, and the list of absences is unchanged:** no equivalent open,
machine-readable national curriculum exists for **Mexico's SEP**, **Colombia**,
**Argentina**, or for **India's NCERT** at national scale. 🟢 Building one remains the
highest-leverage regional asset play on this base. `p361` did not change that — it only
showed, twice, what the finished article looks like.

## 🆕 Pattern 20 — Student-facing LMS agent for a campus nobody has written a connector for

**Problem.** The MCP layer on `agents/top.md` covers Canvas, Moodle, Open edX and
Brightspace. A client's institution runs none of those, or runs a national portal with
its own SSO. The engagement cannot start by writing a connector from scratch and cannot
reach the LMS without one.

**Recipe.**
1. **Start from the closest shaped connector, not from zero.** 🆕 [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (**ISC** — 🔵 first ISC grant in this corpus, BSD-family, functionally MIT for a client deliverable) wraps **Peru's UPC Aula Virtual (Blackboard Learn)** as CLI + MCP. It is the reference implementation for *"unofficial portal, real SSO, MCP surface"*.
2. **For D2L/Brightspace, take the one that models state:** 🆕 [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) (MIT) reconciles against **what the student has already submitted**, so it reports what is actually outstanding rather than every assignment. 🟢 That reconciliation is the hard part and it is already written.
3. **For Google Classroom estates:** 🆕 [`kaorii-ako/Shiori-v1`](https://github.com/kaorii-ako/Shiori-v1) (MIT, 🔴 grant on `master`) — Classroom sync plus SRS plus an MCP server.
4. **Record the learning events** through [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT) into [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) or [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql).
5. **Scheduling** from [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) (MIT) — decide *when*, not only *what*.

🔴 **The one to refuse, and why it is on this list.** [`plyght/canvas-mcp`](https://github.com/plyght/canvas-mcp)
has **14 ★** and **no grant**: nothing at ten probed paths, no `license` field in
`package.json`, and a README whose `## License` section says only *"this project uses
permissive open-source dependencies"*. 🟢 **A statement about dependencies is not a grant
on the work.** Without a licence the default is exclusive copyright, and it cannot enter
a client deliverable at any price. 🔵 It is named here because it is the most plausible
near-miss on the shelf — right category, reasonable stars, nothing behind the heading.

## 🆕 Pattern 21 — A coding academy's grading stack with a permissive execution path, built because `p362` removed the old one

**Client shape.** The same client as `Pattern 9` — a bootcamp or CS department that must
run untrusted student code inside a closed deliverable — but with a procurement rule that
says **OSI-permissive only**. 🔴 `Pattern 9`'s execution tier cannot satisfy that rule any
more: `QingdaoU/JudgeServer` and `QingdaoU/Judger` are **SATA**, and
`QingdaoU/OnlineJudgeDeploy` has no grant at all. This pattern is what is left when the
rule is absolute.

**Recipe.**

1. **Execution and evaluation** — 🆕 [`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)
   (🟢 **MIT**, 1 067 B at `main/LICENSE`, 554 commits · 7 authors (`%ae`) · 640 files ·
   last commit 2026-10-09). Flask/Python: code evaluation, guided learning, **restricted
   execution** and learning analytics in one permissive platform. 🔴 **Read the honest
   bench before quoting it:** 4 ★. The commit stream, not the star count, is the argument
   — and the restricted-execution layer is **not** a seccomp sandbox, so a client running
   genuinely hostile submissions still needs an OS-level boundary (a container per
   submission, `gVisor`, or `judge0` over HTTP).
2. **Notebook courses, unchanged and genuinely permissive** —
   [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
   (BSD-3-Clause) behind [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub)
   with [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
   (both BSD-3-Clause).
3. **Integrity** — [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT) on the
   submissions themselves, rather than proctoring the student.
4. **Written answers** — [`erictrainnlpinxihu/Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent)
   (MIT), whose write actions are absent from its tool table, so the agent can only
   propose and a human disposes.
5. 🆕 **Retention, so the deliverable can show learning rather than output** —
   [`tura-learn/Dhee`](https://github.com/tura-learn/Dhee) (🟢 **MIT**, 1 071 B, 198
   commits · 3 authors (`%ae`) · APAC/India) is **memory built for tutor agents**, which
   is the layer `Pattern 10` had to assemble from `py-fsrs` plus glue. Pair it with
   [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
   (MIT) for the scheduling half: Dhee decides what the tutor **remembers about the
   learner**, FSRS decides **when** to come back to a skill.
6. **Report into the client's LMS** — an LTI 1.3 tool via
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) or
   [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT).
7. **Pedagogical behaviour as skills** — [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)
   (Apache-2.0), and 🆕 [`nuwa-skills/montessori-skill`](https://github.com/nuwa-skills/montessori-skill)
   (🟢 **MIT**, 72 ★) where self-directed practice is the pedagogy. 🔵 **Prefer these over
   `GarethManning/education-agent-skills` for a closed deliverable**: that pack is far
   larger (165 `SKILL.md` against 5) and it is **`CC-BY-SA-4.0`**, so ShareAlike reaches
   every curriculum artefact derived from it. 🔴 The permissive skill supply in education
   is *small*, and saying so is more useful than pretending the choice is even.

🟢 **Licence boundary: every component is MIT, BSD-3-Clause or Apache-2.0, and each grant
was read from its payload on 2026-10-21.** Nothing in this pattern carries a notice
obligation, a non-commercial clause or a copyleft reach.

🔴 **What this pattern costs against `Pattern 9`, stated plainly so the choice is real.**
`QingdaoU/OnlineJudge` is a 6 552 ★ complete judge with contests, a problem bank and an
admin UI; `CodeSense` is a 4 ★ platform with 554 commits behind it. 🟡 **If the client can
accept a non-OSI notice, `Pattern 9` with SATA honoured is less work and more mature
software.** This pattern exists for the client who cannot, and for the engagement where
*"permissive only"* is in the contract rather than in the slide.

## 🆕 Pattern 22 — Evidence that a tutor works, produced before it meets a student

**Problem.** Every tutoring pattern on this base ships a tutor. 🔴 **None of them ships
the evidence that the tutor teaches**, and §2 of [`trends`](../intel/trends.md) records
that evidence is becoming a procurement gate — buyers increasingly want proof of effect
on learning, not a demo. 🔴 **The two ways teams currently answer this both fail a
review:** a benchmark score measures the *model*, not the tutoring, and a classroom pilot
costs a term and needs ethics approval before anyone knows whether the policy is even
sane. 🟢 `p363` found the permissive substrate for a third answer.

**The idea.** Evaluate the tutor against a **simulated learner** first, score it on
**pedagogical moves** rather than final answers, and keep the human pilot as
confirmation of a result you already have.

### 22a — The harness

1. **Simulated learners** from 🆕 [`microsoft/StudentSim`](https://github.com/microsoft/StudentSim) — **MIT**, read at `main/LICENSE` (1 074 B, `sha256:7df20dcdf919`). It trains and evaluates models that simulate how a student responds to material; its stated purpose is to give a tutoring researcher *"a realistic stand-in for a student"* before involving humans per experiment. 🔵 Created 2026-05-28 and pushed on the day of this pass — **young**: pin the commit (`HEAD=73005fd8c` at `p363`), do not float on `main`.
2. **Move-level scoring** from 🆕 [`iwangjian/Coding-Tutor`](https://github.com/iwangjian/Coding-Tutor) — **Apache-2.0**, `main/LICENSE` (11 357 B). **ACL 2025 Findings**: turn-by-turn verifiers that judge the tutor's *next move*. 🟢 **This is the component that makes the pattern defensible** — it scores "did the tutor scaffold or did it answer", which is the thing a teacher is actually buying.
3. **Ground the rubric in human teaching** with 🆕 [`eth-nlped/mathdial`](https://github.com/eth-nlped/mathdial) — **CC-BY-SA-4.0**, declared at `main/README.md` L96–97, 🔴 **no `LICENSE` file**. Teacher–student math dialogues annotated with the pedagogical move the teacher made. 🟡 **Share-alike: a derived corpus must ship under the same terms** — so use it to *calibrate* the verifier and keep the derivative out of the client's proprietary data estate, or accept CC-BY-SA on that artefact deliberately.
4. **Gate the tutor from asserting into a gap** with 🆕 [`yale-nlp/LLM-Metacognition`](https://github.com/yale-nlp/LLM-Metacognition) — **MIT**, `main/LICENSE`. Calibrated "I don't know" is the prerequisite for diagnosis: a tutor that cannot represent its own uncertainty cannot tell a misconception from a gap.
5. **Mastery estimates a reviewer already trusts:** [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT) for Bayesian Knowledge Tracing, or [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (MIT) if the client wants deep knowledge tracing benchmarked against standard datasets.
6. **Quality-gate the generated turns:** [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (MIT).
7. **Deliver into the LMS** over LTI 1.3 once the evidence exists: [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT).

### 22b — The licence boundary, which is the whole reason to write this down

🟢 **Steps 1, 2, 4, 5, 6 and 7 are MIT or Apache-2.0** — they compose into a studio
deliverable with no copyleft and no share-alike reaching the client's code.

🔴 **Step 3 is the only encumbered component, and it encumbers *data*, not code.** Keep
`MathDial` and anything derived from it on the **evaluation** side of the boundary — the
rubric, the calibration set, the test fixtures. 🔵 Nothing from step 3 needs to enter the
runtime, so nothing from step 3 needs to enter the deliverable.

🔴 **Do not reach for [`brucewlee/lftk`](https://github.com/brucewlee/lftk) to add
readability features here.** GitHub reports `NOASSERTION`; the payload at
`main/license.txt` is **CC-BY-NC-4.0** (13 319 B, `sha256:c2ca2f08eac6`) and a build that
links it **cannot be sold**. 🟢 It is the obvious library for this job, which is exactly
why it is named in a pattern that tells you not to use it.

### 22c — What this is worth per region

🟢 **EMEA — this is the compliance artefact, not a nice-to-have.** From **2026-08-02** the
EU AI Act is enforced and **education assessment is high-risk**: a documented evaluation
of the system against a defined population, with human oversight and a decision log, is
work the regulation *requires*. Pattern 22 produces most of it as a by-product.

🟢 **North America — this is the K-8 workaround.** Where student-facing AI is barred
(New York City's one-year moratorium through eighth grade), **the simulated learner is
the only cohort available**, and OK/MD's human-oversight statutes make the move-level
log a selling point.

🟢 **LATAM — this is the 87%/26% offer with teeth.** UNESCO IESALC found 87% of
institutions using AI and 26% holding a formal strategy; an institution with no strategy
cannot evidence anything. Pattern 22 is the smallest concrete deliverable that turns
"we use AI" into "we measured it".

🔵 **APAC — add labelling before shipping generated turns into China**, per §33: AI-content
labelling is a product feature there, and Vietnam's Law on AI (2026-03-01) reaches foreign
vendors directly.

---

## 🆕 Pattern 23 — A cohort-scale notebook teaching cluster that stays permissive through the DEPLOYMENT

🔵 **Why this pattern is new when JupyterHub has been on these shelves for passes.** Every
earlier recipe that reached JupyterHub cited **the core**, which is BSD-3-Clause. 🔴 **But
nobody deploys the core alone** — a teaching cluster is the hub **plus a spawner** (how a
student's process is started) **plus an authenticator** (how the institution signs them
in), and until `p364` read them, **none of those 11 components was in this base** and their
grants were unknown. 🟢 All eleven read **BSD** from payload on **2026-10-21**, so this is
the one stack here where *"fork into a closed client deliverable"* survives contact with
the deployment.

**The stack, every grant read first-hand:**

| layer | component | grant | why this one |
|---|---|---|---|
| hub | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 **BSD-3-Clause** | multi-user notebook server |
| spawner (cohort scale) | [`jupyterhub/kubespawner`](https://github.com/jupyterhub/kubespawner) | 🟢 **BSD** (`main/LICENSE`, 1 528 B) | one pod per student; the only spawner that survives a 500-seat course |
| spawner (single host) | [`jupyterhub/dockerspawner`](https://github.com/jupyterhub/dockerspawner) | 🟢 **BSD** (1 528 B) | the cheap classroom, when there is no cluster |
| spawner (university HPC) | [`jupyterhub/batchspawner`](https://github.com/jupyterhub/batchspawner) | 🟢 **BSD** (1 528 B) | submits to Slurm/PBS — reaches an existing research allocation instead of buying compute |
| identity (cloud IdP) | [`jupyterhub/oauthenticator`](https://github.com/jupyterhub/oauthenticator) | 🟢 **BSD** (1 528 B) | Google/Azure/GitHub — what most institutions actually have |
| identity (on-premise) | [`jupyterhub/ldapauthenticator`](https://github.com/jupyterhub/ldapauthenticator) | 🟢 **BSD** (1 528 B) | the directory a school runs when there is no cloud IdP |
| **LMS SSO** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (`main/LICENSE`) | **LTI 1.3 launch from Moodle/Canvas/Open edX — the boundary that keeps the LMS's GPL on its own side** |
| autograding | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** (`master/LICENSE`) | grades Python **and R** notebooks, containerised, with LMS export |
| integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** | source-code similarity — the layer that matters now students submit agent-assisted code |

**How it wires together.** The LMS launches the hub over **LTI 1.3** via
`ltiauthenticator`, so the student never sees a second login and **the LMS stays on the far
side of a protocol boundary** — which is what keeps Moodle's GPL or Open edX's AGPL off the
client's own code. `kubespawner` gives each student an isolated pod from a course image
the studio builds. `otter-grader` runs inside that image and writes grades back to the LMS
gradebook. `dolos` runs over the collected submissions out of band.

🟢 **What the studio may keep closed:** everything it writes — the course image, the AI
feedback layer, the dashboards, the grading policy. **Every grant in the table is
permissive, so there is no copyleft reach into the deliverable at all** — this is the
*only* pattern on these shelves that can say that about a full deployment.

🔴 **The one trap, and it is `§36`'s:** every grant above was read at a **branch**
(`main`/`master`), not at a **tag**. Pin the versions in the course image and re-read the
grants **at those pins** before the deliverable ships — see Pattern 24.

🔵 **Where the AI goes.** The feedback agent sits beside `otter-grader`, reading the
notebook and the grader's output, never inside the grader. Agents from `agents/top.md`
apply unchanged; nothing in this stack constrains the model choice.

---

## 🆕 Pattern 24 — A grant-closure audit, sold as a deliverable, because the client's licence register is a list of front pages

🔴 **The problem, measured rather than asserted.** `p364` read the README of **60**
education platforms, graded the **69** components they name that this base did not hold, and
found: **19 carry copyleft or source-restricted grants**, **12 carry no grant at any probed
path**, and the single most dangerous row was a platform published as **MIT** whose own
organisation's component is **AGPL-3.0** (`openfun/marsha` →
`openfun/xblock-configurable-lti-consumer`). 🔴 **A client's licence register, which is
almost always a list of top-level repositories, is blind to all of it.**

**The deliverable, in four steps, each of which this base has an instrument for:**

1. **Enumerate the closure.** For every platform in the client's estate, resolve the
   default ref (`git ls-remote --symref`), fetch the README over a **case- and
   extension-closed** ladder, and extract every GitHub address it names, tagged
   `SAME-OWNER` / `THIRD-PARTY`.
   → `compose/code/p364-companion-closure/` (16 offline controls, in `make hooks`).
2. **Grade every grant from PAYLOAD, never from a badge or a classifier.**
   → `compose/code/lib/probe_payload.sh`, which walks ~36 real filename spellings and
   returns family + holder + byte count. 🔴 It exists because this base twice re-wrote a
   classifier from scratch and twice re-imported the GPL-3.0-§13-reads-as-AGPL defect.
3. 🆕 **Re-read each grant AT THE PIN, not at the branch.** Take the versions from the
   client's lockfile and read the `LICENSE` at *that tag*. 🔴 This step is the one nobody
   does and it is where the money is: `iframe-resizer` is **GPL-3.0-or-commercial** at
   `master` and **MIT** at `v3.5.13`.
4. **Separate dependency from dependent before reporting anything.** 🔴 `judge0/judge0`'s
   README names **20** third-party repositories and **19 are adopters, not components**. A
   report that lists them as the client's exposure is noise, and noise is how a licence
   report gets ignored. **The manifest settles it, not the README.**

🟢 **What the client gets:** a per-component table of *address · pinned version · grant at
that pin · grant at HEAD · divergence*, plus a named list of ungranted components to either
replace or write to upstream. 🔵 **The `grant at HEAD` column is the forward-looking half**
— it is the upgrade that will relicense under them, and it is the reason the audit has to
be re-run rather than filed.

🔵 **Scoping note, honestly stated:** `p364` measured **41.7 %** of platform rows as naming
at least one companion. So roughly **three in five** platforms will produce a short report,
and the audit's value is concentrated in the other two — which is why step 1 is cheap and
automated and step 3 is where the hours go.

## 🆕 Pattern 25 — A pin-aware grant audit, because Pattern 24 audits the wrong noun

**For:** the same client as Pattern 24 — one whose licence register is a list of front
pages — after `p365` showed that a grant read at a branch and a grant read at the version
they actually ship are **not the same claim** in 1.5% of cases, and that for 31.9% of
permissive supply the shipped version **has no name at all**.

🔴 **Why Pattern 24 is not sufficient on its own.** Pattern 24 closes the *component* axis:
it finds the companion repositories a platform's README makes you install and grades each
one's grant. It reads every one of them **at a branch**. 🔵 `p365` measured the second axis
and found two live defects in this base's own supply — one that **revokes** a grant at the
pin and one that **erases** it.

### Step 1 — Resolve what the client actually ships (not what the register says)

- Take the dependency manifests from the build that shipped: `package-lock.json`,
  `poetry.lock`, `composer.lock`, `go.sum`, vendored submodule shas.
- For each dependency resolve the **pin that shipped** — a tag, a sha, or 🔴 *"a branch"*,
  which is the finding, not a gap.
- 🟢 **One request per address, unauthenticated:**
  `curl "https://github.com/OWNER/REPO/info/refs?service=git-upload-pack"`.
  It returns `symref=HEAD:refs/heads/*`, the `HEAD` sha and **every** `refs/tags/*`.
  🔵 Use this rather than `git ls-remote`: `p365` recorded the git CLI refusing
  unattached repositories under credential scoping while this path answered 200.

### Step 2 — Triage on the tag count, which is free and which is the whole saving

- 🟢 **`n_tags` ≥ 2 → read the grant at the shipped pin only.** On `p365`'s 119-row
  measurement of this class, **zero** mismatched the branch.
- 🔴 **`n_tags` == 1 → read the grant at BOTH pins.** This class ran at **18.2%**. Both of
  this base's known failures live here: [`harvard-edtech/caccl`](https://github.com/harvard-edtech/caccl)
  (MIT at `main/LICENSE.md`, **nothing** at `1.0.59`, its only tag, titled *"Initial
  Version"*) and [`muhammedalakbarli/imparo`](https://github.com/muhammedalakbarli/imparo)
  (MIT at `main`, **"All Rights Reserved"** at `pilot-v1.0`).
- 🔴 **`n_tags` == 0 → the deliverable is a sentence, not a licence.** *"This component has
  no release; you ship commit `abc1234` of branch `main`, and the grant stated here is true
  of that commit only."* On this base that is **61 of 191 addresses** — and the LTI
  interoperability tier is over-represented, so an integration-heavy client will land here
  disproportionately.

### Step 3 — Read the payload, with a ladder and a classifier that cannot fail silently

- 🟢 `curl https://raw.githubusercontent.com/OWNER/REPO/PIN/PATH` — it accepts a **tag** as
  `PIN`, which is what makes any of this measurable.
- 🔴 **Walk a case-varied ladder.** `p365` lost three grants to a ladder missing lowercase
  `license.txt`: `yanki` (1 071 B), `exampro` (1 069 B), `ThisRaport` (1 114 B). Include at
  minimum `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `license.txt`, `license.md`,
  `LICENCE`, `COPYING`, `COPYING.txt`, `LICENSE-MIT`, `COPYRIGHT`.
- 🔴 **Retry, and treat only a 404 as absence.** One non-200 under concurrency produced a
  false *"no grant"* on a row whose first rung was present. **Absence is a verdict; earn it.**
- 🔴 **Give the classifier a proprietary rung and an `ECL-2.0` rung.** Without the first it
  renders *"All Rights Reserved"* as `UNKNOWN` — the most consequential verdict available,
  reported as a parsing nuisance. Without the second it mis-reads **Sakai** and **OpenLRW**,
  whose Educational Community License is OSI-approved and permissive.

### Step 4 — What the client receives

1. A register keyed on **(address, shipped pin, grant at that pin, path the grant was read
   from, bytes, sha256)** — not on project names.
2. 🔴 A **short list of revocations**: components whose shipped pin grants less than the
   branch the register assumed. Expect ~1.5% of pinnable components, ~18% if they pin
   single-tag repositories.
3. 🔴 An **unpinnable list** with the commit shas substituted, which is the artefact that
   makes an EU AI Act technical-documentation duty, or a Korean or Vietnamese record-keeping
   duty, answerable at all.
4. 🟢 A re-runnable harness: two `curl` shapes, no API key, no authentication, no rate-limit
   exposure — `p365` swept 191 addresses at two pins each with zero probe failures.

🔵 **Scoping note, honestly stated:** on `p365`'s population the triage in step 2 sends
only **11 of 130** pinnable addresses to a double read, so the audit is cheap. Its cost is
concentrated in step 1 — resolving what shipped — and in step 3 for clients whose
components are young. 🔴 **The 31.9% unpinnable share is the part that cannot be made
cheaper**, because the work there is writing down an uncomfortable fact rather than reading
a file.

---

## 🆕 Pattern 26 — A direction-aware dependency closure, because Patterns 24 and 25 grade the right noun on the wrong population

**For:** the same client as Patterns 24 and 25 — but at the step *before* either of them, when
the question is still *which repositories are actually in scope*.

🔴 **Why Patterns 24 and 25 are not sufficient on their own.** Pattern 24 closes the
**component** axis (a platform's grant does not govern what it makes you install). Pattern 25
closes the **pin** axis (a grant is true of a commit, not of a repository). 🔴 **Both then
grade whatever the README named** — and `p366` measured that population: of **484** companion
edges harvested from 326 READMEs, only **86 (17.8%)** are declared in the host's own
manifests. **266 (55.0%)** are bare mentions and **32 (6.6%)** are *adopters* pointing the
other way. 🔵 **So a README-derived closure over-states exposure by roughly 5.6×**, and an
audit sold on it bills a client for reading other people's projects.

**Recipe.**

1. **Enumerate the closure from the BUILD, not the README.** Run
   [`anchore/syft`](https://github.com/anchore/syft) (**Apache-2.0**, `main/LICENSE`, 11 357 B)
   against the built artefact or image to emit an SBOM. This is the step that replaces the
   link list: syft reports what is *resolved*, so the 55% of README mentions that are not
   dependencies never enter the audit.
2. **Grade every grant from payload, with a ladder that does not lie.** Use
   [`aboutcode-org/scancode-toolkit`](https://github.com/aboutcode-org/scancode-toolkit)
   (**Apache-2.0** — and note **its own grant sits at `apache-2.0.LICENSE`**, which a
   conventional `LICENSE`-first ladder misses entirely) or
   [`google/licenseclassifier`](https://github.com/google/licenseclassifier)
   (**Apache-2.0**, `main/LICENSE`). 🔴 **Pin two defects `p366` caught in its own grader
   as test cases before trusting any tool:** a BSD-3-Clause payload contains the words
   *"All rights reserved"* (three repositories were graded `RESERVED` for it), and
   `rails/rails` ships MIT at `MIT-LICENSE` while `systemd/systemd` ships LGPL at
   `LICENSE.LGPL2.1` (both were graded *"no grant"* for want of a rung). **5 of 58 cells —
   8.6% — changed on repair.**
3. **Apply policy as code, not as a spreadsheet.** Feed the graded closure to
   [`oss-review-toolkit/ort`](https://github.com/oss-review-toolkit/ort) (**Apache-2.0**,
   `main/LICENSE`) and express the engagement's actual rule — *AGPL and GPL may be reached
   over a protocol boundary and never linked* — as an ORT policy, so the boundary this file's
   opening rule describes becomes a build failure rather than a promise. Emit CycloneDX with
   [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) (**Apache-2.0**) for
   the client's own register.
4. **Resolve identity sha-to-sha, never name-to-name.** Before de-duplicating the register,
   run `git ls-remote <url> HEAD` on each address and compare **shas**. 🔴 **`p366` found 15 of
   30 name-matched pairs to be one repository** — five by owner rename, among them
   `meta-pytorch/opacus` ≡ `pytorch/opacus` (`df040e4a15`) and
   `openwallet-foundation-labs/learner-credential-wallet` ≡
   `digitalcredentials/learner-credential-wallet` (`1c46a82ba3`). A rename redirects silently,
   so a slug comparison reports two components where there is one, and an inherited register
   two years old is full of them.
5. **Name the unmeasurable share instead of scoring it zero.** For the **20.7%** of hosts that
   publish **no manifest at any of 16 rungs**, the direction question has no answer on this
   channel. Fall back to `p364`'s method — read the platform's own documented install or build
   step, which is how the `Marsha` exposure was established (`yarn copy-iframe-resizer` copying
   JS into LMS pages). 🔴 **Report that share as unmeasured**, exactly as Pattern 25 reports
   its 31.9% unpinnable rows.

**Where this lands in an education engagement, concretely.** The platforms this base
recommends reaching over a boundary are the copyleft ones —
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) (**AGPL-3.0**),
[`moodle/moodle`](https://github.com/moodle/moodle) (**GPL-3.0**),
[`INGInious/INGInious`](https://github.com/INGInious/INGInious) (**AGPL-3.0**, *"most of the
files"*). 🔴 **Step 1 is what finds the AGPL that is NOT the platform:**
[`openedx/frontend-build`](https://github.com/openedx/frontend-build) is **AGPL-3.0** at
`main/LICENSE` and is a **declared** dependency — the only AGPL in `p366`'s 58-repository
exposure set, and invisible to an audit that reads platform front pages.

🟢 **Licence boundary:** every instrument in this pattern is **Apache-2.0**, so the audit
tooling itself imposes nothing on the client's estate — which is the whole point of auditing
with permissive tools.

🔵 **Sizing it honestly, from `p366`'s own numbers.** The direction step is what makes this
affordable: it cut the set worth grading from **330** candidate repositories to **58**, a
**5.7×** reduction, for one manifest read per host. 🔴 **The two costs that do not shrink** are
step 5's unmeasurable 20.7% and step 2's requirement that a human confirm the ladder — because
`p366`'s grader was wrong about **8.6%** of its cells on first run, and an audit that reports
a clean closure it has not re-read is worth less than no audit at all.

## 🆕 Pattern 27 — A two-channel dependency inventory, because Patterns 24–26 grade a population that one regex built

**For:** the same client as Patterns 24, 25 and 26 — one whose licence register is a list of
front pages — at the point where the audit is about to be **signed**. 🔵 Patterns 24–26 make
the audit *correct*; this pattern makes it **complete**, and it is the cheapest of the four.

🔴 **Why Patterns 24–26 are not sufficient on their own.** Pattern 24 closes the *component*
axis (a platform's grant does not govern what it makes you install). Pattern 25 closes the
*pin* axis (a grant is a function of the ref, not the branch). Pattern 26 closes the
*direction* axis (a README names adopters as well as dependencies). 🔴 **All three take their
population from a scan for `github.com/owner/repo`** — and a dependency named in a design
doc, a ticket, a wiki page or an architecture diagram as a bare `owner/repo` is **invisible to
all three at once**. 🟢 Measured on this base, where the convention is identical: **496 live
repositories, 16.3% of the true corpus**, and the two worst omissions were the subjects of its
own open gaps.

### The recipe

1. 🟢 **Harvest both channels over the client's own documents** — repository READMEs, ADRs,
   design docs, runbooks, ticket exports, wiki dumps.
   - channel **U**: `github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`, folded, `.git` stripped.
   - channel **B**: every **backticked** one-slash token.
   Instrument: `compose/code/p367-bare-slug-channel/bare_slug_channel.py census <files…>`.
   🔴 **Require the backticks.** Unticked prose `owner/repo` cannot be told from an English
   word pair (`pass/fail`, `spanish/portuguese`) by any rule you can defend to a client.

2. 🟢 **Reject the four prose classes offline**, each one a thing a document writes that is
   not a repository: a ref or directory first segment (`main/LICENSE`, `docs/license`), a
   file second segment (`openedx/__init__.py`), a ratio or date (`47/47`, `2026/1744`), a
   licence pair (`MIT/Apache-2.0`). 🔵 Import a shape filter rather than writing a second
   one; `p351-address-shape` is this base's.

3. 🔴 **Adjudicate online, never offline.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   Instrument: `probe_slugs.sh adjudicate <candidates>`. 🟢 On this base the offline arms were
   **62.9%** precise — and that is acceptable *because the online leg decides*. An offline-only
   channel at an unmeasured precision is the instrument you cannot sign.

4. 🟢 **Publish the precision, and run the false-rejection control.** Sample ~120 of the
   rejected candidates and probe them with the same instrument; report how many are live. On
   this base: **0 of 120**. 🔴 **Delimit the control's input by newline, not whitespace** —
   rejected candidates legitimately contain spaces, and `p367`'s first control run split them
   into fragments and reported two findings that did not exist.

5. 🟡 **De-duplicate by identity, not by slug.** For each new address, compare its `HEAD` sha
   against the known population; for every collision, compare the **fingerprint over all
   refs** (`probe_slugs.sh refset`). Identical ref sets mean one repository *or* an untouched
   fork — 🔴 `ls-remote` cannot separate those, so say so rather than calling it a rename. On
   this base this step removed **26** of 522 addresses and surfaced eight real organisation
   migrations, `imsglobal/` → `1edtech/` among them.

6. 🔴 **Check the DOMAIN before the licence, not after.** Read each new repository's README
   first line. 🟢 Two of the five permissively-licensed rows `p367` graded were a different
   domain wearing an education name: `google/caliper` is a **Java microbenchmark harness**
   (not 1EdTech Caliper Analytics) and `python-adaptive/adaptive` is **parallel sampling of
   mathematical functions** (not adaptive learning). Both would have passed a licence gate and
   a liveness gate and been wrong. **A 40% trap rate on the permissive subset.**

7. 🟢 **Then run Patterns 26 → 25 → 24 over the UNION**, in that order: direction first (the
   manifest, which cuts the grading backlog ~5.7×), then the pin, then the grant.
   🔵 Steps 1–6 are a day's work and they decide what the other three patterns are even
   looking at.

### What to quote, and what not to

🟢 **Quotable:** the corpus size by channel, the survivor precision, the false-rejection
control result, the net-new count after ref-set de-duplication.
🔴 **Not quotable:** *"we found every dependency."* The channel requires a backtick, so a
dependency named in running prose or inside an image is still invisible, and **a bare-slug
channel cannot be proven complete** — it can only be proven to have found more than the URL
channel did. 🔵 Say the number it added and the control that bounds its error; that is the
claim the evidence supports.

### Cost and prerequisites

🟢 **Cost:** one engineer-day for steps 1–6 on a corpus of this size; the online legs here
were ~50 s for 823 addresses at 6-way parallelism and ~160 s for 2 628.
🔴 **Prerequisite:** egress to `github.com` for `git ls-remote` and to
`raw.githubusercontent.com` for payload. 🔵 Both answered in this environment where **0 of 16
other hosts did**, so this pattern is runnable in restricted networks where a web-research
pattern is not — which is a genuine reason to prefer it as the first deliverable.

## 🆕 Pattern 28 — A Brazilian municipal education deliverable whose three layers are each licence-read

🔵 **The engagement.** A Brazilian municipal *secretaria de educação* runs, or is replacing,
a school-management system, must report against the **BNCC** national curriculum, and wants
adaptive practice for students. Until `p369` this base could not name a stack for it whose
layers had each been graded.

**The stack, all three rows promoted off the trending backlog this pass:**

| Layer | Repository | Licence (payload) | ★ | Role |
| --- | --- | ---: | --- | --- |
| Administration / SIS | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟡 **LGPL** | 720 | Enrolment, attendance, grades, *software público*, already familiar to Brazilian municipalities |
| Curriculum | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **CC** (data) | 9 | BNCC competences as an npm/PyPI package **and an MCP server** |
| Psychometrics | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | 153 | IRT item selection, ability estimation, stopping rules |
| Mastery | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** | 288 | Bayesian Knowledge Tracing over practice attempts |
| Tutor surface | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | 148 | Local-first adaptive workspace, 10+ LLM providers |

**Wiring.**
1. Stand `i-educar` up as the system of record. 🔴 **Do not fork it into the deliverable** —
   LGPL reaches a modified library, so integrate over its interfaces and keep Globant code in
   a separate service.
2. Mount `bncc-pacotes`' **MCP server** next to the tutor. Curriculum alignment becomes a tool
   call — `competência` → `habilidade` → objective — instead of a scraping project, and the
   alignment claim in the proposal becomes checkable against a dataset the client can read.
3. Run `pyBKT` over practice attempts for *what the student knows*, `catsim` for *what to ask
   next*. 🟢 Both are peer-reviewed algorithms with citations: the adaptivity claim survives a
   procurement question that "the model decides" does not.
4. Put `OpenTutor` (MIT, local-first) in front. Its provider abstraction is what lets the
   municipality run a local model where connectivity or data residency demands it.

🔴 **Licence discipline, stated once.** Only `catsim`, `pyBKT` and `OpenTutor` may be
*vendored*. `i-educar` is integrated-with, never forked into the product. `bncc-pacotes` is
CC: the **curriculum data** is usable under its terms, the **server code** around it should be
treated as unlicensed until the repository files a grant — 🔵 so re-implement the handful of
MCP tool wrappers rather than vendoring them, and use the package only as a data source.

**Shape:** 8–10 weeks. Weeks 1–2 `i-educar` stand-up and data model; 3–4 BNCC MCP + alignment
tests; 5–7 `pyBKT`/`catsim` loop against real attempt data; 8–10 tutor surface and
teacher-facing evidence views.

🟡 **Honest risk.** `bncc-pacotes` is at **9 ★** and created 2026-07-09 — small, and the
single point of fragility in this stack. Mitigation is cheap because the dependency is *data*:
pin the dataset version and cache it locally, and the pattern survives the package being
abandoned.

## 🆕 Pattern 29 — The watchlist sweep: sell the client the pass this base just ran on itself

🔵 **The engagement.** A client — an innovation group, a platform team, a CTO office — has
been *collecting* open-source candidates for two years in a wiki, a Notion board or a
Slack channel. They have hundreds of addresses and no decision. They ask for more research.

🔴 **They do not need more research.** `intel/trends.md` §46: when this base measured its own
collection, **89.9 %** of the addresses it had recorded were on no shelf, and one pass of
grading the most-cited **66** produced **43** usable rows while the outward discovery legs
returned **zero**.

**The deliverable, fixed scope.**
1. **Extract** every repository address from the client's own history (wiki, tickets, chat
   exports). One regex; expect noise — drop `search/`, `topics/` and other non-repository
   paths explicitly.
2. **Rank by citation count**, not by recency. Repeated mention is the client's own revealed
   interest, already paid for.
3. **Grade the top N from payload.** For each: `raw.githubusercontent.com/{slug}/{branch}/{file}`
   across `main`, `master`, the default branch from the API, and the release branch, crossed
   with `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `license.txt`. 🔴 §47:
   a one-path probe scores a **21 %** false-absence rate.
4. **Separate three verdicts** and never merge them: *granted* (a licence file), *declared*
   (a manifest field or README sentence — fixable with one upstream issue), *absent*.
5. **Return a decision per row**, not a summary: adopt / integrate-with / reference-only /
   excluded, with the copyleft reach spelled out for each AGPL and GPL row.

🟢 **Why it closes.** The output is a decision table against a list the client assembled
themselves, so there is no argument about relevance, and the cost is roughly one HTTP request
per repository. 🔵 **Prerequisite:** egress to `raw.githubusercontent.com`. Measured in this
environment at **200 for 66 of 66** on a proxy where `github.com` answered **403 to every
probe** — so the pattern runs inside restricted client networks where a web-research
engagement cannot.

## 🆕 Pattern 30 — Reaching the client's incumbent LMS when 71 % of the community bridges cannot be used

**Use when** the client runs **Canvas, Moodle, Blackboard Learn, D2L Brightspace,
Schoology, PowerSchool or Ellucian Banner** — i.e. almost always — and week one asks
whether an agent can read it without a connector being written. 🔴 **This pattern exists
because the obvious answer fails a licence review**: of the 21 in-domain LMS/SIS MCP
servers `p370` graded straight out of the backlog, **15 (71.4 %) ship no licence file at
all**, and an unlicensed repository cannot be forked into a client deliverable at any
price.

### Step 1 — gate the candidate before you scope it (one command per address)

🟢 Run this base's own instrument instead of reading README badges. It needs **git over
https only** — measured at **200 for 63 of 63** addresses on a proxy where `github.com`
and `api.github.com/repos/…` both answered **403**:

```bash
# enumerate the tree, then read the bytes it lists — nothing is guessed
git clone --depth 1 --filter=blob:none --no-checkout --single-branch \
    https://github.com/<owner>/<repo> /tmp/cand
git -C /tmp/cand ls-tree --name-only HEAD | grep -iE '^(licen[cs]e|copying|notice)'
git -C /tmp/cand cat-file -p HEAD:<the file it listed>   # the grant, pinned at HEAD
git -C /tmp/cand rev-parse HEAD                          # record the pin
```

🔴 **And check the industry, not the name.** `compose/code/p370-domain-check` reads the
README payload, never the slug: on `p370`'s run it stopped `pawelkn/xapi-rs` and
`peterszombati/xapi-node` (**xStation5, a forex broker's trading API** — in education
`xAPI` is the Experience API) and `cern-qti/quask` (**CERN's Quantum Technology
Initiative**, not IMS QTI). All three are permissive, live, and would have passed every
other check.

```bash
make gate-domain-check      # 43 offline controls
make gate-refset-register   # 32 — is this address the repository, or a fork of it?
```

🟡 `gate-refset-register` is not optional here. The backlog offered
[`kristofb/ltijs`](https://github.com/kristofb/ltijs) (33 refs) where the repository is
[`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (114 refs, **373 ★**) — same grant,
same byte count, **diverged history**.

### Step 2 — pick the reach by what the client actually runs

| Client platform | 🟢 Use | Grant, read from payload |
|---|---|---|
| **Blackboard Learn (Ultra)** | [bibo242/blackboard-mcp](https://github.com/bibo242/blackboard-mcp) | 🟢 MIT, 1 084 B @ `1fd96db037` |
| **Canvas LMS** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (**302 ★**, 80+ tools) or [mattlo0546/canvas-mcp](https://github.com/mattlo0546/canvas-mcp) where SSO rather than an API token is the only way in | 🟢 MIT both |
| **D2L Brightspace** | 🔴 **no granted community bridge.** Use the vendor's own [brightspaceui/lms-context-provider](https://github.com/brightspaceui/lms-context-provider) for in-platform UI, and write the read-side yourself against the shape of [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | 🟢 Apache-2.0, 10 421 B @ `52bc4bd5e2` (vendor component only) |
| **Moodle** | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) or [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) (Rust) — 🔴 **not** `hefi002/tfg-mcp-moodle-server`, which is GPL-3.0 | 🟢 MIT |
| **Open edX** | [openedx/XBlock](https://github.com/openedx/XBlock) for in-platform components; [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) for the Tutor distribution | 🟢 Apache-2.0, 11 358 B @ `LICENSE.TXT`, and MIT |
| **Schoology · PowerSchool · Banner** | 🔴 **nothing granted exists.** Build against the standards layer below |

### Step 3 — when nothing granted exists, build on the standards layer, not the platform

🟢 **All four protocol libraries are permissive, and `p370` read every grant from payload:**

| Standard | Repo | Grant |
|---|---|---|
| LTI 1.3 / Advantage (Node) | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0, 11 361 B @ `41f150c0693b`, **373 ★** |
| LTI 1.3 (PHP, IMS-certified) | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 Apache-2.0, 11 343 B @ `66d8e4e4b9bd` |
| LTI 1.3 (Java / Spring Security) | [oxctl/spring-security-lti13-demo](https://github.com/oxctl/spring-security-lti13-demo) | 🟢 Apache-2.0 — 🟡 a **demo**, read as reference |
| OneRoster (Clever / Classlink) | [vossenv/oneroster-python](https://github.com/vossenv/oneroster-python) | 🟢 MIT — 🟡 *"in beta… use at your own risk"* |
| xAPI / LRS | [openfun/ralph](https://github.com/openfun/ralph) | 🟢 MIT (`LICENSE.md`) |

🔵 **LTI is the reach that is contractually safest**, because it is a standard the client's
platform already certifies against, and the copyleft of Moodle or Open edX does not cross a
protocol boundary — which is `intel/trends.md` §7's argument, now with §7's `p370` addendum
attached to it.

### Step 4 — the conversation that is not about licences, and arrives first

🔴 **Most of this class authenticates as the student**, through the institution's SSO, in a
real browser. [`general-mudkip/d2l-mcp-server`](https://github.com/general-mudkip/d2l-mcp-server)
opens its own README with a warning against using it for academic misconduct, and
[`bibo242/blackboard-mcp`](https://github.com/bibo242/blackboard-mcp) and
[`mattlo0546/canvas-mcp`](https://github.com/mattlo0546/canvas-mcp) both work by riding the
user's session rather than an institutional token.

🟢 **Scope it explicitly in week one**, using the shape this base measured on the Moodle
write-path rows: separate read from write, default every write to **off**
(`MOODLER_ALLOW_STUDENT_WRITES` / `MOODLER_ALLOW_TEACHER_GRADING` are the published
precedent), **fail closed** on a missing variable, and require `confirm=true` on anything
destructive. 🔵 A bridge that cannot submit, grade or delete is a procurement
conversation a registrar will have; one that can is one they will stop.

🟢 **Why this pattern closes.** Steps 1–3 cost one partial clone per candidate and two
offline gate runs, and they replace the artefact a client's counsel will otherwise reject:
a scoping document whose integration assumption rests on an unlicensed repository.
🔴 **Prerequisite:** git over https. It needs **no** GitHub API and **no** HTML — both of
which were 403 in this environment on the day this pattern was written.

## 🆕 Pattern 12 — AI over an existing lecture-video estate, on a permissive base

**Problem.** A university has years of lecture recordings in a capture system and wants
transcription, search-inside-video, auto-chaptering and captions for accessibility
compliance. 🔴 **The usual blocker is that the capture vendor is proprietary**, so the
deliverable either locks the client in further or cannot be built at all.

🟢 **Why this pattern exists now.** `p372` recovered the platform tier this base had no row
for: [`opencast/opencast`](https://github.com/opencast/opencast) — **ECL-2.0**, **7 870 refs**,
HEAD `9767932b7902` dated **2026-10-19**, read from payload. ECL-2.0 is an Apache-2.0
derivative and **permissive**, so a closed deliverable is available. 🔵 It is the same grant
family as **Sakai**, already on `verticals/solutions.md`.

**Recipe.**
1. **The video platform itself:** [`opencast/opencast`](https://github.com/opencast/opencast)
   (ECL-2.0) — ingest, processing, distribution. Build with the repo's own Maven wrapper
   (`./mvnw`), which its in-tree `AGENTS.md` makes a hard requirement; a system `mvn` breaks
   `${opencast.basedir}` resolution.
2. **Transcription as an Opencast workflow operation, not a bolt-on.** Opencast's processing
   model is workflow operations over a media package, so ASR belongs **inside** it — the
   output lands as a track on the same media package and inherits its access control.
   🟢 That is the difference between a captioning pilot and something a registrar can run.
3. **Search and chaptering:** index the transcript segments with their timecodes into
   [`qdrant/qdrant`](https://github.com/qdrant/qdrant) (Apache-2.0) and serve retrieval over
   it; chapter boundaries come from the same segments, so no second model is needed.
4. **Reach the LMS over LTI, never by integration into it:** [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)
   (Apache-2.0), exactly as Pattern 1 does. 🟢 Moodle's GPL-3.0 and Canvas's and Open edX's
   AGPL-3.0 then never touch your code.
5. **Learning records, if the client wants them:** [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql)
   (764 refs) as the xAPI store. 🔴 **Not Caliper** — see the `p372` correction on Pattern 8:
   Caliper has no retrievable reference client in any language.

🔴 **The licence line that decides the engagement.** Opencast (ECL-2.0), Tsugi
(Apache-2.0) and Qdrant (Apache-2.0) are all permissive, so **steps 1–4 can ship closed**.
🟢 Nothing in this chain is copyleft, and the only copyleft in the picture — the LMS — is
reached across an LTI boundary.

🟡 **What is NOT established, stated so it is not assumed.** This pass read Opencast's
`LICENSE`, `NOTICES`, `README.md`, `pom.xml` and root file list from a blobless partial clone.
🔴 It did **not** enumerate the grants of Opencast's **own dependencies**, and this base has a
standing finding (`p364`) that a permissive headline can carry a copyleft deployment
component. 🟢 Before quoting this pattern, run `p364-companion-closure` and
`dependency-licence-closure` over the Opencast tree. **Cost: one partial clone plus two
offline gate runs** — the same price Pattern 9 and Pattern 11 pay, and for the same reason.

## Pattern 13 — Assistive feedback that returns comments and never a mark

🔵 **Use when** the engagement is LATAM higher education or Brazilian K-12, or anywhere a
statute bars automated high-stakes decisions — Oklahoma and Maryland in the US, Annex III in
the EU from `2027-12-02`. 🟢 **It is also the pattern that fits the widest measured demand gap
on this base:** DEC's 2026 LATAM survey has **50 %** of students wanting AI-assisted feedback
and **19 %** of faculty providing it.

🔴 **The constraint that shapes the whole build.** Brazil's `Parecer CNE/CP nº 15/2026`
(approved `2026-09-01`, DOU summary `2026-10-06`, 🔴 **not yet homologated** — no force until
the homologating act publishes, art. 2 of Lei nº 9.131/1995) is reported to require that
**marks be given only by teachers**, to **bar AI from deciding pass/fail**, and to prohibit
**unsupervised AI below the 5th year**. 🔴 **Its prohibitions bite immediately on publication;
only the adequacy requirements get the 12-month window.** 🟢 **So the mark-writing path must be
architecturally incapable of being driven by the model — not merely configured not to.**

### The wiring

| Role | Repo | Grant, read first-hand `2026-10-22` |
|---|---|---|
| LMS of record | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `master/COPYING.txt` · `35 147 B` · `8ceb4b9ee5ad` · 1 959 refs |
| Feedback generation | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `11 408 B` · `cd2f54e1e506` · 1 493 refs |
| Who needs feedback first | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · `1 066 B` · `f5f955194636` · 187 refs |
| Audit trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** · `11 357 B` · `c71d239df917` · 764 refs |

🔵 **Licence note, and it decides the deliverable's shape.** Moodle is **GPL-3.0**: stay on the
**plugin boundary** and keep the feedback service a **separate process behind its own API**, so
your work is not a derivative of the LMS. 🟢 Everything doing the actual work is **MIT or
Apache-2.0**.

### How it goes together

1. **`pykt-toolkit` ranks, it does not judge.** Train a knowledge-tracing model on the LMS's
   existing attempt history and use it to order students by predicted struggle. 🟢 This is the
   queue, and it is also the learning-gain instrument you will need for `Trend 2`'s procurement
   gate.
2. **`DeepTutor` drafts comments against a rubric** for the top of that queue. 🔴 **Prompt and
   schema constrain the output to prose and rubric-dimension notes — no numeric field exists in
   the response object.** A mark it cannot emit is a mark it cannot leak.
3. **Every draft lands in your own `feedback_draft` table, never in the gradebook.** 🔴 **The
   service account holds NO grade-write scope in Moodle.** This is the compliance claim, and it
   is a permissions fact rather than a policy promise — which is what an auditor can check.
4. **A teacher accepts, edits or rejects each draft in the LMS**, and the teacher's action is
   what writes the mark. 🟢 **`lrsql` records the xAPI statement for each accept/edit/reject**,
   so the audit trail shows a human in the loop per mark — the artefact Oklahoma's and
   Maryland's human-oversight language asks for, and the evidence of teacher authorship the
   Brazilian rule requires.
5. **Below the 5th year, the student-facing surface is switched off entirely** and the drafts go
   only to the teacher. 🟢 One flag, set from the LMS's own year-of-study field.

### What this pattern deliberately does not do

🔴 **It does not score, rank or gate a student, and it does not touch proctoring.** 🟢 That
keeps it outside EU **Annex III point 3** (which applies `2027-12-02`, **not** August 2026 —
see `intel/trends.md`) and outside the Brazilian prohibitions. 🔵 **The day a client asks for
the numeric field, the pattern changes category** and `Pattern 3`'s conformity wrapper and a
high-risk assessment become the scope, not an add-on.

🟡 **One tool considered and left out, with the reason:**
[`agentscope-ai/openjudge`](https://github.com/agentscope-ai/openjudge) (🟢 Apache-2.0 ·
`11 357 B` · `c71d239df917` · 208 refs) auto-generates rubrics from a task description, which
is tempting at step 2. 🔴 **It is built to judge AI agents, not learners**, and nothing in it is
education-specific. 🟢 **Usable offline to draft a rubric a human then owns; not in the
request path.**

---
