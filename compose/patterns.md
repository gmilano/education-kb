---
industry: education
region: Global
updated: 2026-10-24
---

## 🆕 `p419` · 2026-10-24 — **`Pattern AJ` Amendment 8 enumerates paths in ONE tree, and this pass found a repository whose ungranted code is on another BRANCH. 🟢 Amendment 9 makes the audit enumerate refs first. 🟢 Plus `Pattern AR`: the proctored-assessment build, with the branch boundary priced at step 2 instead of found at legal review.**

🔴 **Gates did not run** — `make hooks` executes code from this cloned repository and the host's
auto-mode classifier refused it (`[Code from External]`). Contracts honoured by hand;
`Gap 419-D` registers the un-run suite. **No recipe below was validated by a gate this pass.**

### 🟢 `Pattern AJ` — **Amendment 9**: enumerate REFS before paths; a grant is resolved at `(ref, path)`

🔴 **Why it is forced.** Amendment 8 (`p418`) replaced step 1 with *enumerate every licence-shaped
path, digest each, cross-check every subtree manifest* — correct, and still single-ref. Run that
procedure perfectly against [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU) and it
returns **"MIT, one grant, enumerated, two channels agreeing"** — and it is **wrong about two
thirds of the shipped product**:

| ref | app *(per the project's own `README.md:50-54`)* | tracked paths | licence-shaped paths | manifest `license` |
|---|---|---|---|---|
| `main` *(default)* | Student site — Next.js 16 / React 19 | 199 | 🟢 `LICENSE` — MIT `1 065` B `10e6b9c80b1b` | 🔴 absent, `"private": true` |
| `teacher` | Teacher studio — Next.js 16 + BullMQ worker | 55 | 🔴 **NONE at any depth** | 🔴 absent, `"private": true` |
| `admin` | Admin portal — Vite + React 18 | 43 | 🔴 **NONE at any depth** | 🔴 absent, `"private": true` |

🟢 **Amendment 9, as executable steps:**

1. **`git ls-remote --heads <url>`** — the authoritative ref set. 🔴 **Not a `raw.githubusercontent.com`
   probe:** that channel serves `master` and `HEAD` as **aliases** for the default branch even when no
   such ref exists, so a `200` proves a file and says nothing about a branch. Measured on three
   repositories today with `trunk`/`develop`/bogus-ref controls at `404`.
2. **For each ref that ships a shipped component** — identified from the project's own docs, its
   manifest `name`, or a distinct tree — run Amendment 8's enumeration **on that ref**:
   `git ls-tree -r --name-only <ref> | grep -iE '(^|/)(licen[cs]e|copying|notice)'`.
3. **Digest every payload with `wc -c` on raw bytes.** 🔴 **Never a line-based pipeline** — `T102`:
   `grep -v`-style accounting re-adds a terminal newline the payload may lack, which is exactly the
   `1 065`/`1 066` confusion `p418` had to correct.
4. **The verdict is the set, and the operative cell is the most restrictive member paired with the
   refs and subtrees it governs.** 🔴 **An unlicensed ref is not "MIT by inheritance"** — absence of a
   grant is absence of permission, and it is the strictest member there is.
5. **Record the per-ref table, not a single licence value.** A one-value cell cannot express this
   repository and will be wrong about it.

🔵 **Cost: one `ls-remote` plus one `ls-tree` per shipped ref** — seconds, no API, no HTML, no new
channel. 🔴 **`gate-subtree-grant` (`p382`) is the natural home and cannot express it today**: its
unit is a path inside one tree. `Gap 419-A`.

### 🟢 `Pattern AR` — proctored assessment with the branch boundary priced at step 2

**Problem.** A client wants browser-proctored assessment and syllabus-to-course generation on a
self-hosted stack, permissively licensed, on a system of record they already run.

**Why the obvious answer fails.** `GradeU` is the only readable permissive reference these shelves
carry for *both* capabilities — and its teacher studio and admin portal are **ungranted**. 🔴
Building on the student app and assuming the other two come with it is the failure this pattern
exists to prevent.

**The wiring, with what is granted at each step.**

1. **System of record — copyleft, and that is settled.** [`Moodle`](https://github.com/moodle/moodle)
   (GPL-3.0) or [`openedx/edx-platform`](https://github.com/openedx/edx-platform) (AGPL-3.0, and
   🔴 **NARROWED** per `p413` — read the grant, not the badge). 🔴 **Sixth channel this pass
   confirmed no major education SIS or LMS is permissive** (`Gap 298` / `Gap 405-A`), so stop
   shopping for one.
2. **Proctoring reference — `GradeU` `main` ONLY.** 🟢 MIT, `1 065` B `10e6b9c80b1b`.
   Read `src/features/student/components/Proctoring/ProctoringEngine.tsx`,
   `ProctoringVideoFeed.tsx`, `src/shared/hooks/useProctoring.ts`,
   `src/lib/models/ProctoringLog.ts` and `src/app/api/student/track/proctor/ingest/route.ts`;
   in-browser face detection is `@tensorflow-models/blazeface`, so **no video leaves the client** —
   which is the property that makes it viable under GDPR and under the US state student-data bills
   (CA `AB 1159`, ID `SB 1227`). 🔴 **Do not take the teacher studio or admin portal:** `teacher`
   and `admin` carry no grant. 🟢 **Either ask the maintainers to extend `LICENSE` to those refs**
   (four humans, active this week, already chose MIT once) **or build those two surfaces yourself.**
3. **Course generation.** 🟢 `GradeU` `main`'s approach is a raw `fetch` to an OpenAI-compatible
   endpoint — `src/app/api/student/ai-tutor/route.ts:47` → `https://api.groq.com/openai/v1/chat/completions`,
   model `openai/gpt-oss-120b`, key `GROQ_API_KEY` — and **no AI SDK in `package.json`**. 🟢 **That
   is the portable choice, not a shortcut:** an OpenAI-compatible URL swaps for a self-hosted
   endpoint (vLLM, Ollama) by changing a base URL, which is what an EMEA data-residency requirement
   needs. 🔵 It also means a manifest-only licence audit sees no AI dependency at all — record the
   provider from the **source**, not the manifest.
4. **Packaging to the system of record.** [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph)
   for **SCORM 1.2 / 2004** emission — still the only permissive emitter these shelves carry
   (`p416`, and `p418` confirmed `exelearning` is AGPL-3.0, so it is not a second one).
5. **Conformity artefacts, built with the product and not after it.** A technical file naming
   **every component's licence with its `(ref, path)`**; an Article 50 disclosure on the student-facing
   tutor (**live since 2026-08-02**); and 🔴 **no emotion inference anywhere in the proctoring
   pipeline** — prohibited in education institutions since **2025-02-02**. Annex III bites
   **2027-12-02**.

**What this costs and what it buys.** Steps 1–4 are integration work on granted code. 🔴 **Step 2's
boundary is the whole point:** found at step 2 it is a licence request or two surfaces to build;
found at a client's legal review it is a re-platform. 🟢 **And step 5's artefacts are the same ones
`Trend 41` says the public sector will now insist on** — the South African withdrawal is the worked
example of what their absence costs.

🟡 **Stated limits.** `GradeU` is **3 ★**, `"version": "0.0.0"`, four humans and one bot, with
MongoDB (`mongoose`) still live beside Supabase mid-migration
(`src/shared/utils/migrateLabsToSupabase.ts`). 🔴 **It is a readable reference and a licence
specimen, not a platform to adopt** — this pattern reads it and does not deploy it.

## 🆕 `p418` · 2026-10-24 — **`Pattern AJ` audits a grant at ONE path and this pass found a repository with nine. 🟢 Amendment 8 makes the audit enumerate subtrees. 🟢 Plus `Pattern AQ`: the generated-classroom deployment, with the LGPL boundary priced instead of discovered.**

### 🟢 `Pattern AJ` — **Amendment 8**: a repository's grant is a SET, enumerated, never a value read at one path

🔴 **Why it is forced.** `Pattern AI`/`AJ` resolve a grant by reading `LICENSE` *(or the ladder of
root-ish paths `p384` extended to eight)* and cross-checking the manifest. Run against
[`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) that procedure returns **`MIT`, resolved
on two channels** — its strongest verdict — and it is **wrong about the repository**. The repository
carries **nine** licence-shaped paths and one of them is **LGPL-3.0**.

🟢 **Amendment 8, as a step that replaces step 1 of `Pattern AJ`:**

```sh
# 1a. enumerate — never guess a path, and never stop at the first hit
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> /tmp/probe
git -C /tmp/probe ls-tree -r --name-only HEAD \
  | grep -E '(^|/)(LICEN[CS]E(\.(md|txt))?|COPYING(\.(txt|LESSER))?)$' > paths.txt

# 1b. digest EVERY path — a length is not an identity (T101)
while read -r p; do
  git -C /tmp/probe cat-file -p "HEAD:$p" > b
  printf '%s\t%s\t%s\t%s\n' "$p" "$(wc -c <b)" "$(sha256sum <b | cut -c1-12)" "$(head -1 b)"
done < paths.txt

# 1c. cross-check EVERY manifest beside its own subtree, not just the root one
for m in $(git -C /tmp/probe ls-tree -r --name-only HEAD | grep -E 'package.json$|composer.json$'); do
  echo "$m -> $(git -C /tmp/probe cat-file -p "HEAD:$m" | grep -oE '"license"[^,]*')"
done
```

🔴 **The verdict rule changes with it.** If `paths.txt` has more than one entry, the repository's
licence cell is **a set**, and the audit's answer is the **most restrictive member plus the subtree
it governs** — not the root value. 🔵 Worked on `OpenMAIC`: `{MIT × 8 @ 1 065 B ba2525637432,
LGPL-3.0 × 1 @ 7 652 B e3a994d82e64}` → **"MIT, except `packages/mathml2omml` which is
LGPL-3.0-or-later and is a direct root dependency."**

🟢 **Amendment 8 also subsumes a trap `Pattern AJ` could not see.** A `pnpm`/`npm` workspace declares
vendored third-party code as `"<pkg>": "workspace:*"`, which is **visually identical** to a
first-party package in the dependency list. 🔴 On `OpenMAIC`, `package.json:118` is
`"mathml2omml": "workspace:*"` beside `@openmaic/renderer` — the only distinguishing evidence is a
`LICENSE` two directories down and an `"author"` that is not the project's. 🔵 **So step 1c reads the
subtree manifests, and a manifest whose `"name"`/`"author"`/`"repository"` points off-project marks a
vendored component regardless of what its licence says.**

### 🟢 `Pattern AQ` (new) — the generated-classroom deployment, with the copyleft boundary priced up front

🔵 **For:** a university, ministry or corporate L&D buyer who wants course material turned into
taught, assessed lessons, and who will be asked for a technical file (EU Annex III from
**`2027-12-02`**) or a district AI policy attestation (Maryland's **AI Ready Schools Act**, 24
districts).

| step | component | grant, measured | why this one |
|---|---|---|---|
| 1 | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — generation + delivery | 🟢 **MIT** `1 065` B `ba2525637432` (root + 7 subtrees) | 41.3k★; **named model slots** in `openmaic.yml`, **forbid-user-supplied-keys**, `video: null` to switch a capability off — the only governance surface of its kind on these shelves. Pin **`v1.2.1`** (2026-10-18): the head is `v1.3.0-rc.1` with breaking upgrade conditions and **no rollback below it** |
| 2 | 🔴 **the boundary** — `packages/mathml2omml` | 🔴 **LGPL-3.0-or-later** `7 652` B `e3a994d82e64` | **Decide here, in writing, before the build.** It is a **direct root dependency** built **first** by `build:packages`, and it is what makes Office-math / PPTX export work |
| 3 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) — lifelong tutoring beside it | 🟢 **Apache-2.0** | 42.3k★, `v1.6.15` (2026-10-19) — **larger and more permissive**; use it for the persistent-learner-memory half rather than extending OpenMAIC's |
| 4 | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) or [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) — mastery estimation | 🟢 **MIT** / 🟢 **MIT** | BKT (OATutor) or deep knowledge tracing (pyKT). 🔴 OpenMAIC auto-grades quizzes and does **not** model mastery — this is the gap, not an upgrade |
| 5 | delivery into the client's LMS | [`exelearning/exelearning`](https://github.com/exelearning/exelearning) 🔴 **AGPL-3.0**, or [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) 🟢 **MIT** `1 069` B `41857092247a` | **SCORM 1.2 / 2004 packaging.** `exelearning` is verified in-tree this pass (**774** of **9 756** paths, `ImsManifest.ts`, `imscp_rootv1p1p2.xsd` fixtures) and is state-backed; 🔴 **but §13 network copyleft applies to a hosted service**, so `Papermorph` is the permissive route. 🔴 **Neither offers xAPI** — `exelearning` retired it (`ADR-2302-02-xapi-retirement.md`) |
| 6 | admissions / records substrate | [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) 🟢 **MIT** `1 077` B `c6dca3b0db5b` | 🔴 **No permissive education SIS exists** (`Gap 298`, five channels) — graft a generic MIT ERP/CRM onto the academic model. 🔴 Same vendor as `krayin/laravel-crm`, so picking both is not diversification |
| 7 | the attestation | — | 🟢 Emit the step-1a/1b table **as a build artefact**, per component. This is the document the conformity assessment and the district policy both ask for, and it costs one command per repository |

🔴 **The two honest options at step 2, stated because a proposal must choose one:**

1. 🟢 **Keep `packages/mathml2omml` unmodified** and record it as an unmodified LGPL-3.0-or-later
   dependency with its digest. LGPL is library-scoped; consuming it unchanged is satisfiable, and
   §4's relink/replacement obligation is met by the fact that it is a separate workspace package the
   client can swap.
2. 🟢 **Excise the PPTX / Office-math export path** and ship HTML-only export, which is MIT
   end-to-end.

🔴 **What is NOT an option:** writing *"OpenMAIC, MIT, PPTX export"* in a statement of work. That
prices a copyleft component as permissive in the one document an audit will read.

🔵 **Regional note that changes step 5's economics.** Vietnam's clock gives an **installed-base**
education system until **`2027-09-01`** and a greenfield one until **`2027-03-01`** — so for an APAC
engagement this stack is cheaper to **retrofit beside** an existing LMS than to stand up as a
replacement. 🟢 That is six months of arbitrage, and it points the opposite way from the usual
modernisation pitch.

## 🆕 `p417` · 2026-10-24 (reads 2026-10-23) — **`p411` graded a CORRECT source as carrying "the wrong Vietnamese date" — and the row's OWN QUOTED TEXT contains the clause that makes the source right. 🟢 Plus the first genuinely new state-backed EMEA supply in several passes: `exelearning/exelearning`, AGPL-3.0 at `p413`'s canonical digest, led by Spain's Ministry of Education. 🔴 AND the gap register is THREE passes stale.**

🔵 **Dating note, and this pass is the first in the run that has to SPLIT it.** Every search leg,
licence read, payload read, digest and gate run below was executed on **2026-10-23**; **the commit
lands 2026-10-24**, because the work crossed **00:00 UTC** before it was written out. 🟢 **The two
dates are therefore recorded separately rather than collapsed to one**, and the frontmatter
`updated:` field carries the **commit** date while every `evidence/*.tsv` filename carries the
**read** date — which is why they disagree by one day, deliberately. 🔵 `p395`–`p416` were all
dated **2026-10-23**, twenty-two passes; **this is the first pass dated 2026-10-24**, and the first
whose reads and commit fall on different days. 🔴 `p223`'s date gate is satisfied by the split, not
by rounding either date toward the other.

🟢 **Gates ran BEFORE the first research leg — `p412`'s standing rule, which `p416` admitted
breaking: 50 / 51 green on arrival**, equal to `p413`–`p416`. 🔵 The lone red is
`gate-census-union` control 24 — **`Gap 400-B`**, carried deliberately red since `p398`. `p387-G`
forbids closing it by weakening a control and this pass did not try.

🔵 **Channel note, in agreement with `p414`–`p416`.** `raw.githubusercontent.com` serves **`200`**
and is how every byte-level grant read below was taken; `github.com` HTML reads cleanly through
`WebFetch`. `p414`'s `AUTHZ-REFUSED` class holds a fourth consecutive pass.

### 🟢 `Pattern AO` (new) — the publicly-governed OER authoring stack, for a ministry or a public university

🔵 **When to reach for it:** a public-sector education client that must own its content pipeline, is
comfortable with copyleft, and wants authoring plus delivery without a proprietary authoring licence.
🟢 **The point of the pattern is the governance, not the code:** every layer is either state-led or
has a state-led reference deployment, which is the argument that survives a procurement review.

| layer | what | grant, measured | why |
|---|---|---|---|
| **1 — authoring** | [`exelearning/exelearning`](https://github.com/exelearning/exelearning) | 🟡 **AGPL-3.0** — `34 523` B, `sha256:0d96a4ff68ad` | 🟢 **Spain's MEFPD via Cedec-INTEF**; real-time collaborative editing, Moodle export, offline installers. The reference deployment *is* a ministry |
| **2 — system of record** | **Moodle** (GPL-3.0), or **OpenOlat** (Apache-2.0) / **Kolibri** (MIT) where copyleft is refused | 🟢 carried, 0%-decay tier (`T83`) | `exelearning` exports to Moodle natively, so layer 1 → 2 needs no adapter |
| **3 — integration** | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) *(MIT, npm)* or [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(MIT, crates.io)* | 🟢 MIT | 🔴 the 5%-decay tier — **pin a version and vendor the client**, per `Pattern Z` |
| **4 — agent** | compose over layer 3: LangGraph or CrewAI | 🟢 MIT | the volatile layer stays replaceable |
| **5 — packaging** | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) *(MIT)* for SCORM 1.2/2004, [`scormflow/scorm-engine`](https://github.com/scormflow/scorm-engine) *(MIT)* for the runtime/LRS | 🟢 MIT | 🔴 **do NOT use `exelearning` for SCORM** — unverified (`ACTION p417-B`) |

🔴 **The one hard constraint, and it decides the commercial model.** Layer 1 is **AGPL-3.0**, and
its network clause reaches a **hosted** authoring service. 🟢 **Deploy it on the client's
infrastructure and the pattern is clean.** 🔴 **Wrap it into a studio-hosted multi-tenant product and
the obligation attaches to the studio's service** — counsel before, not after. 🔵 Where that is
refused outright, drop layer 1 to **H5P (MIT)** — 🔴 **but see the split:** H5P's SCORM export runs
through the separate **`Lumi` desktop** application, so H5P is in-LMS interactive content, *not* a
server-side packaging step. Layer 5 stays as it is either way.

🟡 **Bound:** `exelearning`'s export modules were **not** read in-tree this pass. The Moodle export is
stated on the repository page; SCORM is **not**. Read the modules before step 1 is priced.

### 🟢 `Pattern C` — APAC education compliance pack: the date is unchanged, the GRADING RULE is corrected

🟢 **No re-pricing this pass.** `p406` already moved this pattern onto the right date and
`compose/patterns.md:1128` states it correctly: **`2027-09-01`** for an education system live before
**2026-08-15**; **`2027-03-01`** for one deployed after; the cutoff has passed, so a new engagement
runs under the six-month-from-go-live clause.

🔴 **What is corrected is how to grade a source that states `2027-03-01`.** `intel/market.md:577`
(`p411`) counted such a source as *"the wrong Vietnamese date"*. 🟢 **It is not wrong if it carries the
education grace clause** — and the source `p411` quoted did carry it, on the same line. 🔵 **For
delivery this matters in one concrete way:** when counsel or a client cites `2027-03-01`, the right
response is *"that is the all-other-sectors date; education's is `2027-09-01` if the system was live
before 2026-08-15"* — **not** *"your date is wrong"*. The second answer is false and costs
credibility in the room.

🟡 **Bound, carried from `p281` and unchanged:** no primary Vietnamese text has been read on this
channel — every policy host answers `ENOTFOUND` / `http=000`, which `Gap 488-R` records as a property
of the **channel**. This rests on concurring law-firm readings. **Counsel confirms before it goes in a
proposal.**

### 🟡 `Pattern AP` (new, and deliberately small) — the ungranted-upstream ask

🔵 **The situation:** a capability you want exists at an address with **no licence** — this pass found
two, including a Brazilian federal-institute grading agent whose README carries an **MIT badge over a
nonexistent `LICENSE` file**.

🔴 **What not to do:** treat a badge, a README sentence, or a package manifest as a grant. `p411`
recorded a manifest that *agrees* with the grant and proves nothing; `savinoo/ai-grading-system`
is the inverse — a manifest that **disagrees with the absence**.

🟢 **The recipe, three steps and cheap:**
1. **Probe the payload, not the page** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` on every
   default branch. Eight `404`s is a finding; a green badge is not.
2. **Open an issue asking for a `LICENSE` commit**, naming the licence you need (MIT or Apache-2.0)
   and why. An academic author who already *believes* the project is MIT will usually commit it —
   the badge is evidence of intent, just not of grant.
3. **Until that commit lands, reuse the DESIGN, not the code.** Both addresses found this pass
   document their architecture well enough to reimplement: a 7-node LangGraph workflow, conditional
   divergence arbitration, AI-against-human-marks calibration. 🟢 **An architecture is not
   copyrightable the way an implementation is**, and reimplementing on `LangGraph` + `FAISS`/`Chroma`
   is days, not weeks.

🔵 Recorded as `ACTION p417-A` for the Brazilian address specifically, because its region makes it
worth the ask.


## 🆕 `p416` · 2026-10-23 — **Sixty-eight addresses read across four discovery legs returned exactly ONE unshelved in-domain repository — and it closes a scarcity this base declared BY NAME. `DozenTwelve/Papermorph` is MIT, readable and emits SCORM 1.2/2004, where the shelf's only prior SCORM emitter is source-CLOSED. 🔴 AND `p415`'s headline — "the agent field has one hub and no middle" — is refuted by four middle-tier addresses already recorded in `agents/top.md` itself.**

🔵 **Dating note.** Every search leg, licence read, payload read and gate run below was executed on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twenty-second pass dated
today**, after `p395`–`p415`.

🟢 **Gates ran three times, and the middle run is the one worth recording: 50 / 51 → 48 / 51 →
50 / 51.** Green on arrival, equal to `p413`–`p415`. 🔴 **Then this pass's own shelf writes turned
`gate-census-currency` and `gate-union-currency` red** — the published census triple no longer
matched the live shelves. 🟢 Re-derived with `make address-shape-census` / `make union-currency` as
the last act before the commit and **restated rather than back-dated**, per `p352` and `p376`; back
to 50 / 51. 🔵 The lone remaining red is `gate-census-union` control 24, **`Gap 400-B`**, carried
deliberately red since `p398`; `p387-G` forbids closing it by weakening a control and this pass did
not try. 🔴 **Honest deviation from `p412`'s standing rule:** the first gate run was started *in
parallel with* the first research leg, not strictly before it. Nothing below depends on a gate
result — but the rule says *first*, and this pass did not obey it to the letter.

🔵 **Channel note, re-measured and in agreement with `p414`–`p415`.**
`curl -sS https://github.com/GeminiLight/gen-mentor` → **`http=403`, 378 B**, and the body is the
*session's own* refusal (*"GitHub access to this repository is not enabled for this session. Use
`add_repo`…"*), **not** GitHub's; `https://api.github.com/repos/CaviraOSS/PageLM` returns the
**identical 378-byte body**. The same addresses read cleanly through `WebFetch`, and
`raw.githubusercontent.com` serves **`200`** — which is how the byte-level grant read below was
taken. 🟢 `p414`'s `AUTHZ-REFUSED` class, confirmed a third consecutive pass, on a third pair of
addresses.

### 🟢 P7 (new) — "Textbook in, SCORM course out, into the LMS the client already runs"

🔵 **The brief this answers.** A ministry, publisher or university has book-shaped source material
and an LMS already in production. They want AI-assisted courseware, and they will not install a new
platform, and their procurement cycle for a new plugin is measured in months.

🟢 **Every component is MIT or Apache-2.0 and every grant below was read first-hand on 2026-10-23.**

| Layer | Component | Licence | Role |
|---|---|---|---|
| Content build | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 **MIT** (`1 069` B, `sha256:41857092247a`) | Textbook → narrated, interactive lesson on a static shared player; `scripts/scorm.py` packages it as **SCORM 1.2 / 2004** |
| Maths rendering | MathJax, vendored at `engine/vendor/mathjax` | 🟢 **Apache-2.0** | 🔵 declared in `Papermorph`'s README — a second grant on a subtree, named with its path |
| Package QA | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | Run the package **outside** any LMS in CI and assert the SCORM API calls before it is ever uploaded |
| Mastery, alongside | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** (🟡 self-declared alpha; `v0.6.1`) | **BKT + FSRS** sequencing and durable learner state, over **MCP** — the layer SCORM cannot carry |
| Scheduling parameters | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** (**4.1k★**) | Fit FSRS parameters to the cohort's real review history instead of shipping defaults |
| Item generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** | MCQs and lesson plans, including Spanish/Portuguese, feeding the question banks |
| Platform | Moodle · Canvas · OpenOLAT | 🔴 GPL / 🔴 AGPL / 🟢 Apache-2.0 | 🟢 **Unchanged.** The client keeps their LMS; nothing is forked |

**Wiring, in order:**

1. **Ingest** the source book through `Papermorph`; pin the engine tag (`engine-v2.1`) in the build,
   because a new major engine number can require a book-level change.
2. **Build twice** from the same source: a static web bundle for preview and review, and a SCORM
   package for delivery. Same content, two artefacts, one pipeline.
3. **Gate the package in CI with `scorm-again`** — load it headless, assert `cmi.completion_status`
   and score reporting, fail the build on a bad manifest. 🔵 This is the step most SCORM projects skip
   and most SCORM projects then debug inside the client's LMS, which is the expensive place to do it.
4. **Upload** the package. Moodle takes it as a core SCORM activity; Canvas and OpenOLAT import it.
   🔴 **Open edX is the exception** — it needs a community `scormxblock` installed first, so on Open
   edX this is an integration project again and should be priced as one.
5. **Run the mastery layer beside it, not inside it.** `tutor-mcp` holds per-skill BKT state and FSRS
   review scheduling and speaks MCP to whatever assistant the learner uses; `fsrs4anki`'s optimiser
   fits the parameters from the cohort's own history.
6. **Report from both.** SCORM gives the LMS completion, score and time. Per-skill mastery and review
   trajectory come from the MCP side. 🟢 Two sources, one dashboard, and the division stated to the
   client up front.

🔴 **The boundary, stated plainly.** **SCORM carries completion, score and time — and nothing about
mastery, affect or trajectory.** Anyone who promises per-skill mastery reporting "through SCORM" is
promising something the standard does not define. 🟢 That is precisely why the mastery layer in this
recipe is a sibling of the package rather than a payload inside it.

🔴 **Two procurement notes before this pattern reaches a proposal.**
- `Papermorph`'s MIT copyright line reads **`Copyright (c) 2026 TedKaczynski`** — a handle, not a
  legal entity. The grant text is stock MIT and clean; the **assignor is unattributable**, and a
  conservative legal review will raise it. Budget the conversation, or vendor the generator and ship
  only its output.
- `tutor-mcp` is **self-declared alpha**. Pin `v0.6.1`, and treat the mastery layer as the part of
  this pattern that carries engineering risk.

🔵 **Why P7 is distinct from P1–P6.** All six existing recipes put **MCP** at the boundary between a
permissive agent layer and a copyleft platform. P7 adds the **second** boundary this base can now
compose across: **the package format**. It is the only pattern here whose primary deliverable
installs into the client's existing system with no code review on their side.

## 🆕 `p415` · 2026-10-23 — **The agent tier re-measured FIRST-HAND against the live GitHub sidebars, and three figures this base carried are refuted — one of them by a factor of 31.** 🟢 Fifteen agent addresses and nine foundations read today, every licence taken from the repository's own sidebar. 🔴 AND the read channel matters: `curl` and `api.github.com` are REFUSED for every repository not attached to this session, so a pass that reports "unreachable" from `curl` alone is reporting a fact about the CHANNEL.

🔵 **Dating note.** Every search leg and every licence read below was executed on **2026-10-23**, and the
commit lands **2026-10-23**. This is the twenty-first pass dated today, after `p395`–`p414`.

🔵 **Channel note, measured this pass.** `curl -sI https://github.com/CAHLR/OATutor` → **403**, and
`curl -s https://api.github.com/repos/HKUDS/DeepTutor` returns the session's own refusal body
(*"GitHub access to this repository is not enabled for this session"*), **not** GitHub's. The same
addresses read cleanly through `WebFetch`. Both instruments were run side by side before any address
below was written down. Every licence, star count and date in this pass came through `WebFetch`.

### 🟢 Six recipes, each naming its components, its licences and its boundary

Every component below was licence-verified first-hand on **2026-10-23**. 🔵 The rule all six follow:
**permissive agent layer, copyleft platform underneath, MCP as the boundary between them.**

#### P1 — Canvas-native tutoring copilot · **North America** · 8–10 weeks

- [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (**MIT**, 307★) — the tool
  layer: courses, assignments, submissions over the Canvas API.
- [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (**MIT**, 53★, alpha
  `v0.6.1`) — durable learner state: BKT mastery, FSRS review scheduling, misconception tracking.
- [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (**MIT**, 269★, UC Berkeley) — the BKT reference
  to calibrate against, and a provenance that survives procurement review.

**Wiring:** one MCP client holds both servers. `canvas-mcp` answers *what is assigned*; `tutor-mcp`
answers *what this learner knows and what comes next*; the model only composes. Canvas stays stock
(AGPL never reaches client code). 🔴 **Ship the audit log as a deliverable** — state policy asks who
approved the tool and where the human is. 🔴 **Never frame it as replacing an instructor:** Idaho
SB 1227 prohibits that by name.

#### P2 — AI Act-conforming tutor on a permissive LMS · **EMEA** · 10–12 weeks

- [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**, 448★) — the LMS you are
  allowed to modify.
- [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (**BSD-3**,
  112★) — the tutoring surface. 🟡 Read the CE/EE boundary before depending on anything.
- EU-resident open-weight inference (Teuken-7B today; OpenEuroLLM when it ships).

**Wiring:** inference inside the client's EU tenancy, OpenOLAT as system of record, the tutor as a
separate service over OpenOLAT's API. **Article 50 disclosure rendered in the chat surface itself,
not in a policy page.** 🔴 **No emotion recognition anywhere in the design** — prohibited in education
institutions since February 2025 — and say so explicitly in the dossier. 🔵 The deferral of the
stand-alone high-risk deadline to **2027-12-02** is the window: deliver the conformity dossier with
the build.

#### P3 — Offline-first tutoring for connectivity-constrained deployments · **LATAM** · 6–8 weeks

- [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**, 1.2k★) —
  offline-first delivery and content sync.
- [`satvik314/educhain`](https://github.com/satvik314/educhain) (**MIT**, 387★) — Spanish/Portuguese
  item and lesson-plan generation, run **ahead of time**, not at request time.
- [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) (**BSD-3**,
  451★) — review scheduling, which needs no network at all.
- Local open-weight inference on school hardware.

**Wiring:** generation happens centrally and in batch; the school receives *content packs plus a
scheduler*, and the only thing that runs on-site is Kolibri and a small local model.
🔴 **Do not reach for [`freelingo`](https://github.com/artcc/freelingo) here** — its CEFR + FSRS
design is the best reference on these shelves and it is **AGPL-3.0**, so shipping a modified copy to
a client is the trigger. Read it; do not fork it.

#### P4 — Instructional-design factory · **Global** · 4–6 weeks

- [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) (**MIT**,
  488★ — 🔴 *this base previously recorded Apache-2.0; corrected today*) — ADDIE multi-agent: syllabus
  → slides → script → assessment.
- [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (**BSD-3**, 1.4k★) — autograded notebook
  assignments for anything CS or data.
- [`oppia/oppia`](https://github.com/oppia/oppia) (**Apache-2.0**, 6.9k★) — interactive explorations
  with feedback, as the delivery target for generated material.

**Wiring:** `instructional_agents` produces the course skeleton; a human instructional designer
reviews at the syllabus gate (not at the end); `nbgrader` and Oppia receive the artefacts. 🔵 The
review gate is the pattern — generation is cheap, and a syllabus error propagates into every
downstream artefact.

#### P5 — Knowledge-tracing service behind any tutor · **APAC / Global** · 4 weeks

- [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (**MIT**, 451★) — train deep
  knowledge-tracing models on the institution's own interaction logs.
- [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (**MIT**) — the classical BKT baseline you must
  beat before claiming the deep model is worth its cost.
- [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (**MIT**) — serve the
  resulting mastery estimates to any agent through MCP.

**Wiring:** mastery estimation is a *service*, not a feature of one tutor. 🟢 Benchmark DKT against
BKT on the client's own data first; on small cohorts the classical model frequently wins, and finding
that out in week two is worth more than the model.

#### P6 — Pilot as a skill, productionise as a server · **Global** · 1 week + 6 weeks

- [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (**MIT**, 292★) — the pattern: one repository
  shipping the same pedagogy as a Claude Code skill *and* a self-hostable web app.
- [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (**MIT**, 149★) — local-first
  workspace shape for the productionised half.
- [`Selleo/mentingo`](https://github.com/Selleo/mentingo) (**MIT**, 96★) — reference for an LMS where
  the AI mentor is a first-class feature rather than a bolt-on.

**Wiring:** week one is a skill in the stakeholders' own client — zero infrastructure, real
pedagogy, a decision made on evidence instead of a deck. 🔴 **The skill is never the deliverable:**
no tenancy, no learner-state store, no data boundary, no audit trail. The moment it is approved, the
same pedagogy moves behind an MCP server with a state store, and that is the thing that ships.

## 🆕 `p414` · 2026-10-23 — **`34 501` is NOT the AGPL-3.0 `http` form — it is ONE repository's de-indented title line, and the spread is a 2×2 lattice over `34 520` whose four cells are all now measured. 🔴 `education-agent-skills`' grant is a POINTER on BOTH its subtrees and its operative text is unreachable here. 🔴 AND the egress refusal has TWO classes these shelves record as one.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twentieth pass
dated today**, after `p395`–`p413`.

🟢 **Gates FIRST, per the standing rule `p412` set and `p413` kept.** `make hooks` ran **before** any
research: **50 of 51 gates green on the FIRST run** — equal to `p413`'s best-ever first-run state and
again against `47` for both `p409` and `p412`. 🔵 The lone red is `gate-census-union` control 24,
**`Gap 400-B`**, carried deliberately red since `p398`; `p387-G` forbids closing it by weakening a
control and this pass did not try. 🟢 **`p413` left the base clean** — the currency gates were green
on arrival for the second consecutive pass.

🔵 **Channel note, and it CORRECTS `p413`'s largest finding rather than repeating it.** `p413`
concluded the egress channel is an **allowlist** and recorded its evidence as *"`http=000` —
connection never established, **not a `403`**, not a `404`"*. 🔴 **There is a `403`, and it is at the
`CONNECT` layer**: `curl` prints `CONNECT tunnel failed, response 403` and the proxy names
`connect_rejected` — *"the host is not allowed for this session"*. 🟢 **`p413`'s conclusion was right
and its evidence was under-read**, and reading it properly splits what these shelves record as one
refusal into **two classes with different remedies**:

| class | http | body | what it means | remedy here |
|---|---|---|---|---|
| 🟢 **SERVED** | `200` | yes | `pypi.org`, `raw.githubusercontent.com`, `registry.npmjs.org` | — |
| 🟢 **SEMANTIC-404** | `404` | yes (21 B) | the registry **answered**; the absence is a fact | — |
| 🔴 **AUTHZ-REFUSED** | `403` | **yes, 378 B** | tunnel opens; the body names the **session's repository scope** (`api.github.com`, `codeload.github.com`) | a scope grant — **not** a host problem |
| 🔴 **TUNNEL-REFUSED** | `000` | **no** | `CONNECT` 403 + `connect_rejected`; host **not on the session allowlist** | 🔴 **none on this environment** |

🔵 Fifteen URLs, control pair first, in
[`evidence/refusal-taxonomy.2026-10-23-p414.tsv`](../evidence/refusal-taxonomy.2026-10-23-p414.tsv);
the probe is [`compose/code/p414-refusal-taxonomy/refusal.sh`](../compose/code/p414-refusal-taxonomy/refusal.sh).
🟢 **Why the split pays:** an `AUTHZ-REFUSED` host is reachable and merely unauthorised, so a figure
behind it is *obtainable in principle*; a `TUNNEL-REFUSED` host is not, so a figure behind it is
**unverifiable on this channel, permanently**, and `p413`'s standing register rule applies. 🔴 This
base's own [`p798-proxy-refusal-ledger`](../compose/code/p798-proxy-refusal-ledger/README.md) records
refusals **without** this class split — successor item 1.

### 🟢 `Pattern AJ` — **Amendment 7**: the AGPL-3.0 denominator is selected on TWO axes, and `34 501` is not one of them

🔴 `p413`'s **Amendment 6** maps `grep -c 'https://'` to a reference byte count and sets
**`n=0 → ref=34501`**. 🟢 It reproduces `p412`'s instrument faithfully and it is **wrong on this
family**, because `34 501` is `acanas/swad-core`'s **de-indented title line**, not the `http` form.
🔴 **Cost of leaving it in place:** on `mastodon/mastodon` it under-reads by **19** B and on
`openedx/edx-platform` by **20** B, so a pass grading the Open edX flagship would compute a `635`-byte
rider where the rider is `615` — and then look for 20 bytes of narrowing that are not there.

🟢 **Amendment 7 selects on both measured axes and refuses rather than guesses:**

```sh
# Step 4a (AGPL-3.0) — pick the denominator from the payload on BOTH axes.
# Lattice (p414, four cells measured first-hand):
#   bytes = 34520 + 3*(scheme == https) + 1*(line 662 present)
n=$(grep -c 'https://' LICENSE)          # 3 = https revision, 0 = http revision
l=$(wc -l < LICENSE)                     # 661 or 662 — INDEPENDENT of the scheme
i=$(head -1 LICENSE | sed 's/[^ ].*//' | wc -c); i=$((i-1))   # title indent, canonically 20

if [ "$i" -ne 20 ]; then
  echo "DE-INDENTED-TITLE: ${i}sp (canonically 20) — subtract $((20-i)) B before comparing"
fi

case "$n:$l" in
  0:661) ref=34520 ;;   # http  + 661   sha256 57c8ff33c9c0  (mastodon/mastodon)
  0:662) ref=34521 ;;   # http  + 662   sha256 432d251a78db  (the Open edX flagship, rider stripped)
  3:661) ref=34523 ;;   # https + 661   sha256 0d96a4ff68ad  (grafana/grafana + 5 carried)
  3:662) ref=34524 ;;   # https + 662   sha256 8d56b405468a  (blend-ed pair, byte-identical)
  *) echo "UNRESOLVED-AGPL-DENOMINATOR: n=$n lines=$l" ; exit 2 ;;
esac
ref=$((ref - (20 - i)))                  # fold a de-indented title into the denominator
rider=$(( $(wc -c < LICENSE) - ref ))
echo "ref=$ref rider=$rider B"
```

🔵 **Checked against the one address that has a rider:** `edx-platform` gives `n=0`, `l=671`. 🔴 `671`
is in no cell — **correctly**, because the rider moved it — so step 4a exits `2` and the operator
strips the append first (`head -n 662`), which yields `n=0 l=662 → ref=34521` and `rider=615`,
matching the first-hand read to the byte. 🟢 **That is the right failure mode**: the selector refuses
an unknown shape rather than silently picking the nearest constant, which is what Amendment 6 did.

🟢 **And `swad-core` exercises the de-indent limb:** `n=0 l=662 → ref=34521`, `i=0`, so
`ref = 34521 − 20 = 34501` and `rider=0`. 🔵 One payload, one correct answer, no special case.

### 🔴 A compliance step every recipe on these shelves now needs: is the grant even IN the tree?

🔵 Recipes here cite components by `(FILE, digest)` and that has been enough. 🔴
`GarethManning/education-agent-skills` breaks it: **both** its in-tree payloads are `POINTER`s — a
*"human-readable notice"* at the root and a scope-less variant under `mcp-server/` — and the operative
CC BY-SA 4.0 legalcode is on `creativecommons.org`, which is **`TUNNEL-REFUSED`** here. 🟢 So a recipe
that vendors or references this component cites a file that **is not the licence**.

🟢 **The step, inserted before any component is composed:**

```sh
# Step 0c — classify the grant's LOCATION before trusting its family (p307 / p254 / p414).
for p in LICENSE LICENSE.md LICENCE COPYING; do
  [ -f "$p" ] || continue
  if grep -qiE 'full (legal )?(licence|license)( text)? (is )?(are )?(available )?at|human-readable notice|legalcode' "$p"; then
    echo "POINTER: $p names an EXTERNAL operative text — resolve it before composing"
    grep -ohE 'https?://[^ )]+' "$p" | sort -u | while read -r u; do
      code=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 12 "$u" 2>/dev/null)
      [ -z "$code" ] && code=000
      [ "$code" = "000" ] && echo "  UNRESOLVABLE-HERE: $u (TUNNEL-REFUSED)" || echo "  $code $u"
    done
  else
    echo "GRANT: $p carries operative terms in-tree"
  fi
done
# And never read the root alone — p382. Enumerate every LICENSE in the tree:
#   the root and mcp-server/ payloads of education-agent-skills differ by 252 B,
#   and the deleted 4 lines are the SCOPE sentence, absent from the SOFTWARE subtree.
```

🔴 **What a studio does with a `POINTER` + `UNRESOLVABLE-HERE` result:** keep the component at
*reference, do not vendor* — which is where these shelves already put this one on ShareAlike grounds
— and record that the terms a deliverable would be held to were **not read**. 🟢 The posture is
unchanged; what changes is that the recipe now says so instead of implying a payload was verified.

## 🆕 `p413` · 2026-10-23 — **AGPL-3.0 IS a revision family, and `Pattern AI`'s AGPL reference is a SUBTRACTION rather than a measurement. 🟢 `openedx/edx-platform`'s grant is NARROWED and this base carried the bytes without the consequence. 🔴 AND THE EGRESS CHANNEL IS AN ALLOWLIST — every "proxy-refused" note on these shelves is a fact about the CHANNEL, not the host.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the nineteenth pass
dated today**, after `p395`–`p412`.

🟢 **Gates FIRST, per `p412`'s successor item 1.** `make hooks` ran **before** any research:
**50 of 51 gates green on the FIRST run** under `p300`'s no-masking runner — **the best first-run
state this base has recorded**, against `47` for both `p409` and `p412`. 🔵 The lone red is
`gate-census-union` control 24, **`Gap 400-B`**, carried deliberately red since `p398`; `p387-G`
forbids closing it by weakening a control and this pass did not try. 🟢 **`p412` left the base
clean** — `gate-census-currency` and `gate-union-currency` were **green on arrival**, the first time
a pass has inherited a current census rather than a stale one.

🔵 **Channel note, and it is this pass's largest finding.** The egress channel was probed with
`p293`'s control pair FIRST: `pypi.org` **200**, `raw.githubusercontent.com` **200**. Then **10 of
10** other hosts answered `http=000` — *connection never established*, not a `403`, not a `404`:
`moodle.org`, `openeducat.org`, `education.ec.europa.eu`, `gov.uk`, `tum.de`, `uni-siegen.de`,
`kimadu.de`, `lernen-digital.nrw`, `bildungsserver.de`, `diariodarepublica.pt`. 🔴 **Two of those
are this industry's own flagship project domains.** 🟢 So the refusal is a property of the
**channel**, not of any host, and it is an **allowlist** rather than a geography filter — a
conclusion no single-host observation could reach.

### 🟢 `Pattern AJ` — **Amendment 6**: the AGPL-3.0 denominator is selected in-tree, never by subtraction

🔵 `p412`'s **Amendment 5** made the GPL-3.0 denominator selectable in-tree by `grep -c 'https://'`
because the FSF ships two revisions. 🟢 **The same instrument works on AGPL-3.0 unchanged, and this
pass measured it on ten payloads**:

```
# Step 4a (AGPL-3.0) — pick the denominator from the payload, not from a constant.
n=$(grep -c 'https://' LICENSE)
case "$n" in
  3) ref=34523 ;;   # https form: 661 lines, sha256 0d96a4ff68ad
  0) ref=34501 ;;   # http  form: 662 lines, sha256 884b434957ba  (n=1 instance measured)
  *) echo "UNRESOLVED-AGPL-DENOMINATOR: $n https:// occurrences" ; exit 2 ;;
esac
```

🔴 **And Amendment 6 FORBIDS the figure `Pattern AI` step 4 carried.** Its `~34 522 B` AGPL
reference is **`openedx/edx-platform`'s `35 136` B minus this base's own `614` B edX-block figure** —
a subtraction, not a measurement. 🔴 It matches **neither** form (1 B below `https`, 21 B above
`http`), and it could not have matched, because `edx-platform`'s base text combines `http://` URLs
with an **indented** title, a presentation neither measured form has. 🟢 **Rule: never derive a
licence denominator by subtracting an addendum from a narrowed payload.**

🟢 **Amendment 7 — the ratio floor is computed on the FOLD, not on the bytes.**
`idurar/idurar-erp-crm` serves the AGPL at **34 230 B**, **293 B** short of canonical at the **same
661 lines**, and `diff` shows **318 changed lines, every one a stripped indent or a collapsed double
space**. 🔴 A byte-ratio test reads it at **99.15 %** — harmless against a 50 % floor, and **wrong at
three significant figures**, which is the defect `p411`'s Amendment 3 exists to prevent. 🟢 So: fold
with `p378`'s `presentation_digest()` first, then compare; `p312`'s `template_digest()` **must not**
be used as an AGPL identity oracle, because it reports **6 templates where `p378` reports 3 texts**
over the same ten payloads, and `identify()` returns `UNKNOWN-TEMPLATE` on **all ten**.

### 🟢 `Pattern AM` — the Open edX RPC side-car, built on a grant that was read but never quoted

🔵 **Built because this base carried `openedx/edx-platform` as `AGPL-3.0`, `35 136` B, for a dozen
passes without recording what its last nine lines SAY.** 🔴 The usual reading — *"the LMS of record
is AGPL, so anything we build near it is at network-copyleft risk"* — is **wrong on this payload**,
and it has been closing off the cheapest Open edX engagement shape there is.

🟢 **The licence fact, measured at `master` on 2026-10-23** (`master/LICENSE`, `35 136` B, sha256
`e12d78569742`): EdX Inc. appends a clarification that a **public, independently available web
service** communicating with the work **by any inter-service mechanism including RPC** is **not a
work based on** it, and that **"Corresponding Source" excludes** source for programs used solely to
provide such services.

**The recipe.**

| step | what | why this component |
|---|---|---|
| 1 | Stand up **Open edX** unmodified, via **`tutor`** | 🟢 The clarification protects a service *beside* the platform. It says nothing about a fork — so **the one thing this pattern forbids is patching `edx-platform`** |
| 2 | Put the AI service in **its own process, reached only over HTTP/RPC** | 🔴 This is the load-bearing step. An in-process XBlock or a monkey-patched module is **inside** the work; a network service is explicitly outside it |
| 3 | For the read path, take [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (`master/LICENSE`, **AGPL-3.0**, `34 524` B) as the **reference implementation, not the dependency** | 🔴 It is **AGPL and so is its Tutor plugin** ([`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp), byte-identical licence) — `Gap 297-R`'s absence is exactly this: **no permissive Open edX side-car exists**. 🟢 Read the tool surface — **33** tool definitions were read first-hand at `p189`, on the **Tutor plugin** half of the pair — then write your own against the same Open edX REST endpoints, and the clarification covers *your* service |
| 4 | Authenticate through **LTI 1.3**, with [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (**MIT**) or [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (**MIT**) | 🟢 Both read **MIT** on PyPI this pass. 🔴 **`django-lti` declares its licence ONLY in its OSI classifier** — no `license`, no `license_expression` — so a procurement scan that reads one field will report it **unlicensed**. Record the classifier read in the engagement's licence register |
| 5 | Emit learning telemetry as **xAPI**, keeping the statement store outside the platform too | 🟡 [`tincan`](https://pypi.org/project/tincan/) is Apache-2.0 **in substance** but declares it as the prose string `Apache License 2.0` — **not an SPDX identifier** — and was last uploaded **2020-09-03**. Use it as a format reference; do not take it as a maintained dependency |
| 6 | Ground the agent in curriculum, by region | 🟢 **North America**: [`pdg6/bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (MIT). **LATAM**: [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) — `bncc` `0.5.1` declares **`MIT`** in `license_expression` and names **four** repository URLs, splitting code from data (`bncc-dev/bncc-dados`). 🟢 **Global/K-6**: [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — 🔴 **ODbL** (`main/LICENSE`, `25 289` B, re-read this pass with **zero drift**), a share-alike **database** licence with **no code grant**, so it constrains the data you redistribute, not the service |
| 7 | Audit the result with **`Pattern AJ` as amended** before shipping | 🔴 Steps 3 and 6 put an AGPL payload and an ODbL payload in the same engagement. Amendment 6 selects each denominator in-tree; Amendment 7 folds before comparing |

🔵 **Scope boundary, stated because it is the whole value of the pattern.** The clarification is
**EdX Inc.'s appended statement of intent**, measured in the payload served at `master` on
**2026-10-23** — strong enough to design against, and not a substitute for counsel on a specific
deployment. 🟢 **Cite the payload, the ref and the date**, which is why all three are in this
pattern rather than a footnote. 🔴 And it protects **your** service only: it does not make
`openedx-mcp` redistributable under other terms, and it does not survive a fork of the platform.

### 🟡 `Pattern AN` — adopting a ministry's prompt assets, where the upstream publishes documents rather than a repository

🔵 **Built because EMEA's clearest new supply this pass has no version control.** **KIMADU**
(Universität Siegen with NRW's Ministerium für Schule und Bildung) publishes **eleven** didactic
German-subject agents as OER under **`CC BY-SA 4.0`** — downloadable, adaptable, explicitly
transferable into one's own environment, and delivered as **HTML and PDF** for pasting into ChatGPT
or fobizz.

| step | what | the trap it avoids |
|---|---|---|
| 1 | **Vendor the prompt into your own repository on day one**, with the retrieval date and source URL in the commit | 🔴 There is **no repository, no package, no version and no digest** upstream. A pass that cites "the KIMADU prompt" without pinning bytes is citing something that can change silently |
| 2 | **Read the per-file licence notice, not the project's**, before reusing anything | 🔴 The `KIM` document scopes the grant to *"ausschließlich den Prompt und unsere Informationen zur Nutzung"* — **only the prompt and the usage notes.** The **three knowledge-base libraries** the agent runs with are **outside** it. `gate-grant-scope`'s subject, on a prompt asset |
| 3 | Treat `CC BY-SA 4.0` as **share-alike on the prompt text** | 🟡 Adaptations of the prompt carry the same licence. That is workable for a delivery asset and **wrong for a product differentiator** — so put client-specific pedagogy in the libraries you supply, not in the forked prompt |
| 4 | Supply the knowledge files yourself, from sources you hold | 🟢 Turns step 2's gap into the engagement: the ministry supplies the pedagogy, the client supplies the corpus, Globant supplies the pinning and the retrieval layer |
| 5 | Label every claim about this asset **search-channel** in the client's register | 🔴 `kimadu.de`, `lernen-digital.nrw`, `uni-siegen.de` and `bildungsserver.de` all answer **`http=000`** here against a control pair that returned `200`. 🔴 The same leg that found this asset also asserted KIMADU had open-sourced *a platform* — it has not; that claim fused two items from one newsletter issue |

## 🆕 `p412` · 2026-10-23 — **`make hooks` RUNS**, the pass that declared it unrunnable is the pass that **broke a gate**, **“5 authors” is `%an` and collapses to 3**, and the GPL-3.0 denominator spread is **two FSF revisions, not noise**

🔵 **Dating note.** Every search leg, clone, licence read, registry probe and gate run below was
executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the eighteenth pass
dated today**, after `p395`–`p411`.

🟢 **Channel note — and the headline is a channel REFUTATION.** `make hooks` **RAN TO COMPLETION
this pass: 47 of 51 gates green** under `p300`'s no-masking runner. 🔴 **`Gap 410-C` (“`make hooks`
unrunnable”) is therefore REFUTED, not closed** — and this is the **second** time this base has had
to refute it: `p397` already disposed of the identical belief as `Gap 396-C`, recording that *“the
repository's python runs here, `make hooks` runs here, and three gates had drifted red with nobody
looking.”* 🔴 **`p410` and `p411` re-acquired a belief this base had already disproved**, and the
cost was **three consecutive passes of gate blindness**. Measured this pass:

| channel | `p411` reading | `p412` reading | note |
|---|---|---|---|
| `make hooks` | 🔴 declared unrunnable | 🟢 **47/51 green on the first run, 50/51 after repair** | 🔴 **the central claim of the last two passes, refuted by running it.** The lone remaining red is `gate-census-union` control 24 = **`Gap 400-B`**, carried deliberately red since `p398` |
| `api.github.com` | `403` | 🔴 `403` | unchanged for a third pass |
| `github.com` HTML | `403` | 🔴 `403` | reproduces `p411` |
| `git` smart-HTTP | works | 🟢 works | `ls-remote moodle/moodle HEAD` = `46c042e7da65f8cb2ec7dc19f46566ce61a393e1`; every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second registry channel |
| **PyPI** | `200`, recorded as **unused** | 🟢 **`200`, and USED this pass** | 🆕 `p411` noted the channel and did not spend it; this pass does — see the PyPI rows |
| `gnu.org` | `000` — `connect_rejected` | 🔴 `000` | 🆕 **mechanism refined:** `curl (56) CONNECT tunnel failed, response 403` — the **proxy** refuses the tunnel; the host never answers |
| `oecd.org`, `eur-lex.europa.eu` | `000` | 🔴 `000` | same proxy mechanism; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | **third** consecutive pass reproducing the exact byte count |

🔴 **This is a GATE-AND-CORRECTION pass, and the supply brief is exhausted on BOTH halves.** Eight
legs ran — four global, four regional. 🔴 **The four global supply legs returned seven addresses and
this base already carries every one of them** (`withmarbleapp/os-taxonomy`, `karpathy/nanochat`,
`frappe/education`, `Gego-K12/gegok12`, `ashishpatel26/500-AI-Agents-Projects`,
`luongnv89/claude-howto`, Nous Research's `hermes-agent`); the only unshelved shape was
`HuggerHustle/ai-radar`, a general AI-trend issue tracker and **not education supply**. 🔴 **The four
regional legs returned ZERO unshelved facts for a FOURTH consecutive pass.** 🔵 So `p409`–`p411`'s
regional reading now holds four passes deep, and `p411`'s *“supply is exhausted only in the wording
`p408` used”* does **not** reproduce: the ERP/CRM/SIS wording that paid at `p410` and `p411` returned
nothing new this pass.

**Evidence:** [`gate-suite-result`](../evidence/gate-suite-result.2026-10-23-p412.tsv) (5 rows) ·
[`author-key-rederivation`](../evidence/author-key-rederivation.2026-10-23-p412.tsv) (3 rows) ·
[`gpl3-revision-pair`](../evidence/gpl3-revision-pair.2026-10-23-p412.tsv) (4 rows) ·
[`pypi-channel-probe`](../evidence/pypi-channel-probe.2026-10-23-p412.tsv) (8 rows) ·
[`channel-reachability`](../evidence/channel-reachability.2026-10-23-p412.tsv) (10 rows) ·
[`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p412.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **`make hooks` runs, and the two passes that said otherwise left a gate RED behind them.** 47/51 green. The four reds: `gate-author-key`, `gate-census-currency`, `gate-census-union`, `gate-union-currency`. 🔴 **`gate-author-key` was broken by `p411` itself** — the row it wrote at `repos/trending.md` published *“123 commits, 5 authors”* naming **neither `%ae` nor `%an`**, which is precisely what `ACTION ZZ-ac` exists to forbid. 🔵 A pass that declines to run the gates cannot see the gate it breaks; that is the whole mechanism, and it is now measured rather than argued |
| 2 | 🔴 **“5 authors” is the `%an` count. By `%ae` it is 3 — and `p411` published the list that refutes it.** `Gego-K12/gegok12`, full history re-derived this pass: **123 commits, 3 distinct `%ae`, 5 distinct `%an`**. `karthick@gegosoft.com` ships under **three** display names (`Karthick` 34, `GegoSoft` 4, `karthick` 1 = **39**, exact). 🔴 `devteam@gegok12.com` is a **shared ROLE account carrying 83 of 123 commits (67.5 %)**. 🔵 **No new probe was needed:** `repos/foundations.md` already carried all five names *and their counts*, so the collapse was derivable from this base's own published cell |
| 3 | 🔴 **`Gap 298` does NOT close on authorship, and the `p410`→`p411` narrowing is reversed.** `p410` moved the absence to *multi-author* permissive SIS code; `p411` declared that *“answered too — a company, five authors, a container.”* 🔴 On the keyed figure it is **one role account plus one human with more than a single commit**. 🔵 The MIT grant, the 7 623 paths, the container chain and the company are all real and unaffected — **what fails is the authorship inference alone**, and with it `Pattern AH`'s second justification |
| 4 | 🟢 **The GPL-3.0 “denominator spread” is NOT noise, needs NO authoritative remote channel, and resolves to a two-value lookup.** `p411` measured 35 141 / 35 147 / 35 149 B and concluded that with `gnu.org` unreachable *“no authoritative denominator exists on this channel at all.”* 🟢 **Measured in-tree this pass: `moodle/moodle` `COPYING.txt` = 35 147 B and `frappe/erpnext` `license.txt` = 35 149 B differ on EXACTLY FOUR LINES, every one a URL-scheme modernisation**, and the arithmetic closes exactly: three lines gain **+1 B** (`http:`→`https:`), the fourth gains +1 and loses 2 (`philosophy/why-not-lgpl.html` → `licenses/why-not-lgpl.html`) ⇒ **35 147 + 2 = 35 149** ✔. Both are **674 lines** with **zero CR bytes**, so neither line count nor line endings discriminate — **the URL scheme does, and one grep reads it** |
| 5 | 🔴 **`Pattern AI` step 4's own `~35 141 B` reference matches NEITHER measured revision.** It sits **6 B below** the `http` revision, and its provenance is unrecorded. 🔵 So the gate's denominator was never the FSF text at either revision; it is a third value this base has been quoting as canonical. 🟢 Repaired as **`Pattern AJ` Amendment 5** — which *sharpens* `p411`'s Amendment 3 rather than replacing it: two significant figures is the right floor, but the denominator is now **selectable in-tree** instead of unsourced |
| 6 | 🟢 **PyPI worked, and it re-dates `Gap 297-R` through a channel that answers while GitHub is `403`.** `blend-ed/openedx-mcp` on PyPI: **v0.1.9, 9 releases, last upload 2026-10-22 · 1 d**, **AGPL-3.0** on *both* PyPI sub-channels (`license` field and OSI classifier). 🔴 This base reads it at **v0.1.5, 5 releases**, from `p190` evidence dated **2026-10-14**. 🟢 **`Gap 297-R` STAYS OPEN — the licence has not moved** — but **`ACTION NL`'s scope (`0.1.1`–`0.1.5`) is stale by four releases** |
| 7 | 🔴 **A PyPI record that names NO repository at all — `p280`'s unattributable class, second instance, now on a second registry.** `openedx-mcp` publishes **no `project_urls` and no `home_page`**, so PyPI alone cannot link the package to `blend-ed/openedx-mcp`; that linkage comes entirely from another channel. 🔵 `p411` recorded the same class on npm (`repos/trending.md` — *“no `repository` field … live, recent and unauditable”*). 🟢 `canvas-mcp` is the well-formed control in the same probe: MIT on both sub-channels **and four URLs naming its repository** |
| 8 | 🔵 **A third channel agreeing with an absence — recorded as a corroboration, not a discovery.** `loyaniu/moodle-mcp` on PyPI (**v0.2.1, 3 releases, last upload 2026-06-29**) has an **empty `license` field and zero License classifiers**. 🟢 This base already carries it `UNGRANTED` by full-tree enumeration (13 files) *and* by an absent `pyproject.toml` licence field; PyPI is now the **third** independent silent channel. 🔵 Marked as corroboration because `gate-absence` exists to stop exactly this being re-published as a find |
| 9 | 🔵 **`gate-census-union` control 24 is red, and it is NOT a new gap — this pass’s first draft nearly re-registered it.** The control wants both rejection arms to fire on the live shelves; `NAME-REF-OR-PATH` fires and `NAME-DOT-RUN` does not. 🟢 **That is `Gap 400-B`, diagnosed at `p398`** (`p382` duplicated `p375`’s rule upstream and made the audited arm unreachable) and **carried deliberately red ever since** — `p409` recorded it as *“a sixth pass”*. 🔴 Writing it up as `Gap 412-A` would have been exactly the restated-absence defect `gate-absence` exists to catch; caught here before the commit, and recorded because the near-miss is the useful part |
| 10 | 🔴 **`p411` left NO entry in the gap register.** `intel/open-gaps.md`'s newest pass section is **`p410`**, so the register has been one pass stale all day while three of this base's own gates were red. 🟢 Repaired below: `p412` registers its own gaps **and** `p411`'s |

### 🟢 `Pattern AJ` Amendment 5 — the GPL-3.0 denominator is SELECTABLE IN-TREE, and step 4's constant is wrong

🔵 **This sharpens `p411`'s Amendment 3 rather than replacing it.** Amendment 3 prescribed two
significant figures and naming where the denominator was read — both correct, and both retained.
🔴 **What Amendment 3 got wrong is the premise:** it concluded that, with `gnu.org` refused,
*“no authoritative denominator exists on this channel at all,”* treating the spread as irreducible.

🟢 **The spread is two FSF revisions, and one grep tells them apart:**

| revision | bytes | discriminator | measured on |
|---|---|---|---|
| `http` scheme | **35 147** | `grep -c 'http://'` → **4**; carries `philosophy/why-not-lgpl.html` | `moodle/moodle` `COPYING.txt` |
| `https` scheme | **35 149** | `grep -c 'https://'` → **4**; carries `licenses/why-not-lgpl.html` | `frappe/erpnext` `license.txt` |

🟢 **The arithmetic closes exactly**, which is what makes this a revision pair and not two
corrupt copies: three lines gain +1 B (`http:`→`https:`), the fourth gains +1 and loses 2
(`philosophy`→10 chars → `licenses`→8) ⇒ **35 147 + 3 − 1 = 35 149** ✔. Both are **674 lines**
with **zero CR bytes**.

🟢 **Insert step 4a, one command, before the ratio is computed:**

```sh
# GPL-3.0 only: choose the denominator by revision, do not average and do not guess
scheme_hits=$(git cat-file -p "HEAD:$P" | grep -c 'https://')
case "$scheme_hits" in
  4) DENOM=35149 ;;   # https revision  (licenses/why-not-lgpl.html)
  0) DENOM=35147 ;;   # http  revision  (philosophy/why-not-lgpl.html)
  *) DENOM=UNKNOWN ;; # report the count; do NOT compute a ratio
esac
```

🔴 **And replace step 4's `GPL-3.0 ~35,141 B`.** That constant matches **neither** revision — it
is **6 B below** the `http` one and its provenance is unrecorded, so every GPL-3.0 ratio this base
has published was taken against a number no measured payload reproduces. 🔵 The published
conclusions survive anyway, because the error is **0.017 %** against a **50 %** floor — but a gate
whose reference nobody can re-derive is a gate that cannot be audited.

🔴 **`UNKNOWN` is a real branch, not a formality:** a payload with 1–3 `https://` hits is a
*partially modernised* copy, i.e. an edited FSF text, and the correct report is
`NOTICE-OR-STUB`-adjacent — **name the count and refuse the ratio**, never interpolate.

🔴 **Not verified this pass, and registered rather than assumed:** step 4's **AGPL-3.0**
reference (`~34 522 B`) was not re-measured and may carry the same defect (`Gap 412-B`).

### 🟢 `Pattern AK` — an author figure is resolved by `%ae`, and `%an` is reported beside it

🔴 **Built because `Pattern AI`/`AJ` audit the GRANT and say nothing about the people**, and this
pass showed that an unkeyed author count can carry a client-facing risk claim that is simply false.
`Gap 298` was declared closed on *“five authors”*; the keyed figure is **three**, two thirds of the
history is **one shared role account**, and the difference is a bus-factor statement.

**Wiring, concretely — three commands on a full clone:**

```sh
git clone --filter=blob:none --no-checkout https://github.com/OWNER/REPO r && cd r
git rev-list --count HEAD                              # commits
git log --format='%ae' | sort | uniq -c | sort -rn     # IDENTITIES  <- the load-bearing figure
git log --format='%an' | sort | uniq -c | sort -rn     # display names, reported BESIDE it
```

🔴 **A `--depth 1` clone cannot answer this** — it has one commit — so this is the one step in the
adoption gate that needs full history. It is still cheap: blobless and checkout-less, `gegok12`'s
123 commits cost one clone.

**The four rules, each earned by a measurement on this pass's row:**

1. 🟢 **Publish `%ae` as *the* count and `%an` beside it, always keyed.** `gegok12` is
   **3 `%ae` / 5 `%an`**. `ACTION ZZ-ac` already requires the key; this fixes *which key leads*.
2. 🔴 **Never assume a direction between the two.** `gate-author-key`'s own header says `%an`
   *“runs BELOW `%ae` on every row measured”*; on `gegok12` it runs **above** (5 > 3), because one
   email ships three display names including a **case variant** (`Karthick`/`karthick`). 🔵 That is
   `p283`/`p348`'s case-fold class on the author axis — the base already knows the class, just not
   on this field.
3. 🔴 **Flag any identity holding >50 % of commits as a ROLE ACCOUNT and treat it as bus-factor 1
   until refuted.** `devteam@gegok12.com` = **83/123 = 67.5 %**. A role address is an
   *organisation*, not a contributor, and it is the opposite of the de-risking a reader infers
   from a high author count.
4. 🟢 **Report contributors with >1 commit separately.** `gegok12`: **one**
   (`abinaya@gegosoft.com` has a single commit). 🔵 “5 authors” (`%an`) and “one sustained human
   contributor plus a team account” are both true of the same repository, and only the second is
   usable in a risk register.

🔵 **Where this changes an existing recommendation:** `Pattern AH` (build beside, do not fork)
has now survived **three** different justifications — no permissive SIS (`p409`), authorship
(`p410`), open-core scope (`p411`) — and `p412` **restores the authorship reason it lost**, because
the refutation that removed it was unkeyed. 🔴 A conclusion that survives every change of
justification should still be re-read for whether it is load-bearing; it is kept here because the
**scope** reason (open-core, premium modules withheld) is independent of all of this and holds on
its own.

### 🟢 The census, RE-DERIVED — and `p411`'s predicted delta is refuted

🟢 **For the first time in three passes the census is derived rather than carried**, because
`make` runs. 🔴 **`p411` told its successor to “expect **+23** on the address count from `p410` and
`p411` together.” The measured delta is less than half that:**

| cifra | published (`p409`, carried by `p410`–`p411`) | derived `p412` | delta | verdict |
|---|---|---|---|---|
| `harvested_folded` | 2 730 | **2 740** | **+10** | 🔴 was STALE |
| `rejected_non_addresses` | 35 | **35** | 0 | 🟢 MATCH |
| `addresses_corrected` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_u` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_b_survivors` | 3 157 | **3 170** | **+13** | 🔴 was STALE |
| `union_addresses` | 3 529 | **3 541** | **+12** | 🔴 was STALE |

🔴 **So `p411`'s `+23` prediction is refuted by measurement: the address count moved `+10` and the
union `+12`.** 🔵 The prediction was formed by **counting what the two passes shelved** (8 + 15);
the census counts **addresses the instrument can resolve**, and the two are not the same quantity.
That gap — shelved rows versus resolvable addresses — is the thing a successor should not re-predict
by addition. 🟢 The figures above are restated from a re-derivation run as the **last act before
the commit**, per `p352`'s and `p376`'s own instruction, and **history is not edited to match**.

## 🆕 `p411` · 2026-10-23 — a **19-byte “GNU GPL V3”**, a manifest that **agrees with the grant and proves nothing**, and a fork pair separated by **commit-subset** where byte-identical licences could not

🔵 **Dating note.** Every search leg, clone, licence read and registry probe below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the seventeenth pass dated today**,
after `p395`–`p410`.

🔴 **Channel note, re-derived first-hand rather than inherited — and the channel has MOVED since
`p410`.** `make hooks` **COULD NOT BE RUN** again: this session will not execute code from the
cloned repository, so the ~50 gates are unscored for a second consecutive pass and the address
census is **carried forward unchanged and marked NOT re-derived**. Measured this pass:

| channel | `p410` reading | `p411` reading | note |
|---|---|---|---|
| `api.github.com` | `403` | 🔴 `403` | unchanged |
| `github.com` HTML | *not recorded* | 🔴 `403` | 🆕 **`p410` recorded only the API.** The HTML surface is refused too, so "read it on the repo page" is not a fallback on this channel |
| `git` smart-HTTP | works | 🟢 works | every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second channel |
| **PyPI** | *not recorded* | 🟢 **`200`** | 🆕 a **third** registry channel this base has not been using |
| `gnu.org` | `403` | 🔴 **`000` — `connect_rejected`** | 🆕 **degraded**: `p410` got a refusal *from* the host, this pass the proxy will not open the connection at all |
| `oecd.org`, `eur-lex.europa.eu` | ENOTFOUND | 🔴 `000` — `connect_rejected` | primary policy hosts still unreadable; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | 🟢 re-fetched and byte-counted — **independently reproduces `p410`'s reference** |

🔴 **Because `gnu.org` is now unreachable, the GPL-3.0 denominator is read IN-TREE** — and reading it
in three places is what produced finding 5.

🟢 **This is a RESEARCH pass. Supply saturation broke for a second consecutive pass; the REGIONAL
layer is saturated for a third.** Nine legs ran — four global, four regional, one phrased in
Portuguese. 🟢 **The supply legs returned 15 addresses this base does not carry.** 🔴 **The four
regional legs returned ZERO unshelved facts** — every instrument, figure and date came back already
on these shelves. 🔵 That is `p409`'s and `p410`'s reading re-confirmed on the regional half and
refuted on the supply half, and the split is now stable enough to act on: **the regional brief is
exhausted; the supply brief is exhausted only in the wording `p408` used.** The two legs that paid
this pass were the **ERP/CRM/SIS** wording (again, as at `p410`) and the **Portuguese** phrasing
(again, as at `p410`) — a phrasing effect that has now replicated.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p411.tsv)
(15 rows) · [`fork-subset-resolution`](../evidence/fork-subset-resolution.2026-10-23-p411.tsv)
(5 rows) · [`gpl3-reference-spread`](../evidence/gpl3-reference-spread.2026-10-23-p411.tsv)
(4 rows) · [`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p411.tsv) (5 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A 19-byte grant — the thinnest on these shelves by two orders of magnitude.** [`frappe/education`](https://github.com/frappe/education), default ref **`develop`**, HEAD `73ce33e` **2026-10-13 · 10 d** — live code. Its **entire** grant is a one-line `license.txt` reading `License: GNU GPL V3`, **19 B** against GPL-3.0's **35 147 B** read in-tree this pass = **0.054 %**. It is the **only** licence-shaped path at any depth, and there is **no `license` field in any manifest**. 🔵 `p410`'s thinnest specimen was 874 B at 7.7 %; this is **142× thinner** |
| 2 | 🔴 **A manifest that AGREES with the grant and is worth nothing — a channel defect `Pattern AI` does not cover.** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) carries root `LICENSE` **MIT, 1 150 B**, and `composer.json` `"license": "MIT"`. 🔴 **But that manifest's `"name"` is `laravel/laravel` and its `"description"` is *“The skeleton application for the Laravel framework.”*** — it is the **unedited Laravel skeleton**, and its MIT is *Laravel's*, not GegoK12's. 🔴 **`Pattern AI` step 5 handles a manifest that DISAGREES in either direction; it has no rule for one that agrees because nobody edited it.** A gate counting channels scores this address **“MIT resolved on 2 channels”** — its strongest verdict — on **one** real channel |
| 3 | 🟢 **`Gap 298` moves again, and the axis `p410` moved it to is the one that now closes.** `Gego-K12/gegok12`: **MIT**, Laravel 12 / PHP 8.4, **7 623 tracked paths**, **123 commits across 5 distinct authors**, and a complete build-and-deploy chain (`composer.json`, `package.json`, `Dockerfile`, `docker-compose.yml`, `.env.example`, `artisan`, `phpunit.xml` — all present and byte-counted). 🔵 `p410` closed `Gap 298` on `shrikrishna-lab/StudentManagement` and restated the absence as **authorship** — 156 paths, one author, no build file. 🟢 **This address beats it on every axis `p410` named.** 🔴 **Except currency: HEAD is 120 d stale**, and the free core is **open-core** — the vendor withholds premium modules |
| 4 | 🟢 **A fork pair resolved by COMMIT-SUBSET where byte-identical licences could not — `Gap 395-A`'s discriminator, demonstrated working.** [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) and [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) share root `baea09f77545`, first commit **2026-05-01**, an **identical `LICENSE` blob `7f7f7a2…`** and an identical copyright line. 🟢 **`kvnloo`'s 452 commits are a strict SUBSET of upstream's 469** — so the fork direction is decided, and the fork is **17 commits / 21 days behind**. 🟢 **The forker retained attribution** (`Copyright (c) 2026 Arnaud Guiovanna`), which is the opposite of `p408`'s specimen |
| 5 | 🔴 **The ratio test's DENOMINATOR is not a constant, and this base quotes it as one.** GPL-3.0 measured in three places this pass: **35 141 B** (the figure `Pattern AI` step 4 itself carries), **35 147 B** (`moodle/moodle` `COPYING.txt`), **35 149 B** (`frappe/erpnext` `license.txt`). 🔵 An **8-byte spread**, 0.023 % — harmless against a 50 % floor, **fatal to any ratio quoted to three significant figures**. 🔴 And `gnu.org` being `connect_rejected` this pass means there is **no authoritative denominator available on this channel at all** |
| 6 | 🟡 **`CC0-1.0` is a FOURTH licence class on these shelves, and it splits deed-vs-legalcode exactly as the payload instrument predicts.** Two repositories, **the same name**, both declaring CC0-1.0: [`ARUNAGIRINATHAN-K/awesome-ai-agents-2026`](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) at **5 875 B / 98 lines / 4 statutory sections** (the legalcode) and [`caramaschiHG/awesome-ai-agents-2026`](https://github.com/caramaschiHG/awesome-ai-agents-2026) at **2 207 B / 46 lines / 3 statutory sections** — **37.6 %**, with section 4 (*Limitations and Disclaimers*) **absent**. 🔵 This base's licence vocabulary is permissive/copyleft/ECL-2.0; **a public-domain dedication sorts into none of them** |
| 7 | 🔴 **The search layer asserted a FORK the repository does not declare — the inverse of `Gap 395-A`.** The Portuguese leg returned [`perazzogringa-coder/plataforma-agentes-ia`](https://github.com/perazzogringa-coder/plataforma-agentes-ia) (**MIT, 1 073 B**, HEAD `e5a42a7` **6 d**) and stated *“trata-se de um fork de outro repositório.”* 🔴 **Neither channel supports it:** the README says only that the public distribution ships neutral branding to be replaced, and the history is a clean root at **2026-08-01, 6 commits, one author**. 🔵 `Gap 395-A` says a licence read cannot tell a fork from an original. **This is the other failure mode: the search layer inventing provenance**, and a 6-commit squashed-looking tree cannot refute it either |
| 8 | 🔴 **This base carries the AILit publication date twice-right and once-wrong, and this pass's EMEA leg settles which is which.** `p386` enters the OECD/EC *Empowering Learners for the Age of AI* framework at **18 Jun 2026**, twice, with its full substance (4 domains, 19 competences, 3 levels). 🔴 **`p405`'s regional-leg table at `intel/market.md:524` carries it as `2026-06-17`.** 🟢 This pass's EMEA leg returned **18 June 2026** independently. **`2026-06-17` is the outlier and is corrected below** — a one-day drift introduced by a later pass's leg summary, into a date this base sells an EMEA compliance deliverable against |

### 🟢 `Pattern AJ` — `Pattern AI` amended: three defects found by running it against 15 addresses

🔵 **`Pattern AI` (`p410`) is the grant-resolved adoption gate. This pass ran it against 15 new
addresses and it mis-scored three of them.** `Pattern AJ` is not a replacement — it is the three
steps that change, stated so a successor patches rather than re-derives.

#### 🔴 Amendment 1 — step 2's vendored-path list misses BUILD OUTPUT and project-local vendor dirs

🔴 **Defect found on `Gego-K12/gegok12`:** 17 licence-shaped paths, **16 vendored**, and
`Pattern AI` step 2's prefix list (`vendor/`, `node_modules/`, `third_party/`,
`native/*/packages/`) catches **none** of them. The real paths are
`custompackages/brozot/laravel-fcm/LICENSE` and **fifteen `public/js/<chunk>.js.LICENSE.txt`**
webpack banners sitting in the **public web root**.

🟢 **Replace the prefix list with a prefix list PLUS a suffix rule:**

```
# subtree grants - discard
  (^|/)(vendor|node_modules|third_party|bower_components|custompackages|packages)/
  (^|/)native/[^/]+/packages/
# BUILD OUTPUT grants - discard (new)
  \.(js|css|mjs|cjs)\.LICENSE\.txt$
  (^|/)(dist|build|public/(js|css)|static/(js|css)|out)/
```

🔵 A compiled PHP/JS platform ships its dependency notices inside its own served directory. **Any
platform-tier audit hits this; `gegok12` is simply the first one measured.**

#### 🔴 Amendment 2 — step 5 must check that the manifest IDENTIFIES THE PROJECT before counting it

🔴 **Defect found on `Gego-K12/gegok12`:** payload MIT, `composer.json` `"license": "MIT"` — and
that manifest is the **unedited `laravel/laravel` skeleton**, `"description": "The skeleton
application for the Laravel framework."` 🔴 **`Pattern AI` step 5 anticipates a manifest that is
wrong; it has no rule for one that is RIGHT ABOUT SOMETHING ELSE.** The gate scores its strongest
verdict — *resolved on 2 channels* — on one channel.

🟢 **Insert step 5a, two commands, before the manifest counts:**

```bash
git cat-file -p HEAD:composer.json | grep -m1 '"name"'      # or package.json / pyproject.toml
git cat-file -p HEAD:composer.json | grep -m1 '"description"'
```

🔴 **If `name` is a framework scaffold slug — `laravel/laravel`, `symfony/skeleton`, `my-app`,
`create-react-app`, the cookiecutter default — the `license` field is the SCAFFOLD's and is NOT a
channel.** Report `resolved on 1 channel`, not 2.

🔵 **Why this matters more each year:** scaffolds ship a populated `license` field. Every
unedited generated project is a false second channel, and **it fails in the direction that produces
confidence** rather than doubt.

#### 🟡 Amendment 3 — step 4's denominator needs a source, and the ratio needs two significant figures

🔴 GPL-3.0 measured at **35 141 / 35 147 / 35 149 B** in three places this pass; `gnu.org` is
`connect_rejected`, so no authoritative value exists on this channel. 🟢 **Quote every ratio to
two significant figures and name where the denominator was read.** `0.054 % (vs moodle/moodle
COPYING.txt, 35 147 B)` is a re-testable claim; `0.0541 %` is a false precision.

#### 🟢 Amendment 4 — a failed ratio triggers a SIBLING read before it is reported as a defect

🔴 `frappe/education`'s 19 B fails step 4 and has no manifest, so the gate reports a two-channel
failure on a live, maintained repository. 🟢 **One extra command resolves it:**

```bash
# for org/repo, read the grant shape of the org's other repositories
for sib in frappe/frappe frappe/erpnext frappe/lms; do
  git clone --depth 1 --filter=blob:none --no-checkout -q https://github.com/$sib /tmp/$RANDOM
  # ls-tree -r | grep -iE '^(licen[cs]e|copying)' ; cat-file -s
done
# -> 1 118 B MIT / 35 149 B GPL-3.0 / 33 893 B AGPL-3.0, all with agreeing manifests
```

🟢 **Three siblings shipping full payloads mean the org knows how; the thin file is a shortcut, not
a concealment.** 🔵 **Verdict vocabulary gains one value:**
`UNDER-DOCUMENTED (corroborated by N siblings)` — distinct from `NOTICE-OR-STUB`, which should be
reserved for a thin payload **that disagrees with another channel**.

#### 🟢 Amendment 5 — fork direction is settled by commit SETS, not by HEADs or dates

🔴 The `tutor-mcp` pair defeats every channel the gate currently has: identical licence **blob**,
identical copyright line, same root, and the fork's HEAD is *older* — which on its own says nothing.

🟢 **Add this as step 8, and it is two commands:**

```bash
git -C A rev-list HEAD | sort > /tmp/a   # after: git fetch --depth=2000
git -C B rev-list HEAD | sort > /tmp/b
comm -12 /tmp/a /tmp/b | wc -l
```

| reading | meaning |
|---|---|
| shared == count(B) < count(A) | 🟢 **B is a fork of A**, `count(A) - count(B)` commits behind |
| shared == 0 | 🟢 **Independent projects** — a name collision only |
| shared > 0, neither is a subset | 🟡 **Diverged fork** — both have unique commits; neither is canonical |

🔵 Verified both directions this pass: `kvnloo/tutor-mcp` ⊂ `ArnaudGuiovanna/tutor-mcp` (452 of
452), and the two `awesome-ai-agents-2026` repositories at **zero** shared commits.

### 🟢 `Pattern AK` — the SIS engagement, now that the permissive-or-copyleft choice is REAL

🔵 **Why this is new.** Every prior pass recorded that education's SIS layer was copyleft-only, so
there was no choice to pattern. 🟢 **`p411` shelves a maintained MIT occupant**, so the decision
exists — and it is **not** decided by the licence.

**Step 0 — establish the deployment mode, because it decides everything after it.**

| client intent | base | why |
|---|---|---|
| Client self-hosts their own estate | 🟢 [`frappe/education`](https://github.com/frappe/education) **GPL-3.0** | 🟢 Copyleft costs a self-hosting institution **nothing**, and this is the complete, 10-day-current option. 🔵 `p401`'s plugin-boundary rule governs studio code on top |
| Studio ships a closed multi-tenant product | 🟢 [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) **MIT** | 🟢 The only permissive rung with a real build chain. 🔴 Then **step 1 is mandatory** |
| Client needs registrar depth and will own the schema | 🟡 [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement) **MIT** | 🔵 `p410`: read it **for the schema** — transcripts, clearance, certificate requests. 🔴 Bus factor of one; do not inherit it as a dependency |

**Step 1 — price the open-core gap BEFORE the licence discussion (only for `gegok12`).**
🔴 The vendor states the public repository is the **free core** and that premium modules (online
quiz, private chat, bus management) are outside it; vendor pages also disagree with each other on
module counts (**38 total / 26 free** on one page, **23+** on another). 🟢 **Enumerate the client's
required modules against `app/` and `custompackages/` in the tree — `git ls-tree`, not the
marketing page — and put the unmet ones in the SOW as build items.** The gap between the demo and
the repository is the vendor's revenue, and it is a **scope** risk, not a licence risk.

**Step 2 — run `Pattern AJ`, not `Pattern AI`, on whichever base is chosen.**
🔴 Both candidates trip an amendment: `gegok12` trips **1** (16 vendored grants, 15 of them build
output) and **2** (the Laravel skeleton manifest); `frappe/education` trips **4** (19 B payload,
no manifest, resolved only by sibling read).

**Step 3 — the assistant layer goes on MCP, and it is MIT on both routes.**
🟢 [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (**MIT**, HEAD
today) supplies the learner-state machine — mastery, review scheduling, misconceptions — **outside**
the SIS, so the copyleft question never reaches the studio's own code. 🔴 **Pin the upstream, not
[`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp)**, which is 17 commits behind. 🔴 It is
**alpha v0.5.0** — pin a commit in the SOW, and say "alpha" in the proposal.

🔵 **This composes with `Pattern AH` (`p409`, the LMS-of-record assistant) and changes its premise
a second time.** `Pattern AH` was written *“where there is no permissive SIS to fork.”* `p410`
found one and kept the pattern on an **authorship** reason. 🔴 **`p411` claimed to refute the authorship
reason; `p412` refutes the refutation** — `gegok12` has a company and **3 `%ae` identities**, one of them a shared role account with 67.5 % of commits *(the `5` was `%an`)*. 🔴 **`Pattern AH` still holds, and the
reason has moved a third time: to open-core SCOPE.** A pattern that has survived three different
justifications should be re-read for whether the conclusion is actually load-bearing, and a
successor is asked to do exactly that rather than inherit it a fourth time.

### 🔴 The census, carried forward and marked NOT re-derived

🔴 `p409`'s **2 695 addresses / 3 529 over both channels**, `STALE` for a third consecutive pass.
**`p411` shelves 15, `p410` shelved 8 — a successor with an executable `make` should expect +23.**

## 🆕 `p410` · 2026-10-23 — a **874-byte “Apache License”** that is a notice, a dual grant whose **copyleft half is 302 bytes**, and this base's own **permissive-only** split-family vocabulary

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the sixteenth pass dated today**,
after `p395`–`p409`.

🔴 **Channel note, and it is this pass's first finding.** `make hooks` **COULD NOT BE RUN.** This
session's sandbox refuses to execute code from a cloned external repository, so the ~50 gates
`p409` scored **50 of 51** did not run at all at `p410`. Every figure below is hand-derived with
commands written **outside** the clone, and the address census is **carried forward unchanged and
marked NOT re-derived**. 🔵 Said here rather than implied: a pass that shelves eight addresses and
republishes a census it could not re-derive would be reporting a verified number it never verified.

🔵 **`api.github.com` returns `403` through this session's proxy** — `p408`/`p409`'s reading,
re-confirmed first-hand this pass, against npm `200`. Every licence, ref and date below is read from
**git itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`ls-tree -r` / `cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second
channel. 🔴 **`gnu.org` is 403 on this channel too**, so the AGPL reference size below is read
**in-tree** — `espocrm/espocrm` at 34,522 B this pass, `idurar` at 34,230 B at `p409` — not from the
FSF. 🟢 The Apache reference *was* fetchable and **was byte-counted: 11,358 B.**

🟢 **This is a RESEARCH pass, and the saturation broke.** `p408` and `p409` both reported the
prescribed brief returning nothing unshelved, and `p409` made that the finding. 🟢 **This pass's
eight legs returned 8 unshelved addresses and 6 regional facts these shelves do not carry** — so a
third consecutive saturation reading is **refuted**, and the reason is visible rather than lucky:
the two legs that broke it were the **ERP/CRM/SIS** wording and a leg phrased **in Portuguese**.
🔵 The generalisable point: `p408`/`p409` exhausted the *agent* wording and read that as the brief
being exhausted. **Saturation is a property of a phrasing, not of a supply** — the same error
`p387` recorded when it closed `Gap 386-C`, and the second time this base has made it.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p410.tsv)
(10 rows) · [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p410.tsv) (6 rows) ·
[`pt-supply-probe`](../evidence/pt-supply-probe.2026-10-23-p410.tsv) (4 rows) ·
[`gap-retest`](../evidence/gap-retest.2026-10-23-p410.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A licence path whose payload is a NOTICE, caught by byte size.** [`addex12/School-CRM`](https://github.com/addex12/School-CRM) — default ref **`develop`**, HEAD `011a98c` **2025-05-10 · 531 d**. Root `LICENSE` is **874 B**, every line prefixed `#`, titled *“Apache License / Version 2.0”* and carrying `SPDX-License-Identifier: Apache-2.0`. 🔴 **Apache-2.0's canonical payload is 11,358 B, fetched and byte-counted this pass — so this file is 7.7 % of the licence it names.** It is the ~175-word per-file appendix, pasted at the grant path. 🔴 **And `composer.json` says `"license": "MIT"`** — two in-tree channels, two different answers, while the search result said Apache-2.0 |
| 2 | 🔴 **The byte-size tell cuts both ways, and here it cuts the wrong way.** 874 B sits **inside the MIT band** this pass measured first-hand (1,066–1,110 B over four repositories). 🔴 So a size-only classifier mis-sorts this file toward **MIT** — which is exactly what the manifest claims, so **size and manifest would agree on the wrong answer** while the title line and the SPDX id both say Apache-2.0. 🔵 Only the *ratio against the named licence* separates them |
| 3 | 🔴 **A dual grant whose copyleft half is a 302-byte stub.** [`ivan-my-wong/flowclass`](https://github.com/ivan-my-wong/flowclass) — `main`, HEAD `bdbc79b` **2026-09-20 · 33 d**. Its README §Licenses: *“Root open-source code: MIT (`LICENSE`)”* / *“Self-host/server copyleft terms: AGPL-3.0 (`LICENSE-AGPL`)”*. 🟢 `LICENSE` is a real MIT payload, **1,066 B**. 🔴 **`LICENSE-AGPL` is 302 B — 0.9 % of an AGPL payload** — and its text delegates: *“For the full legal text, see: https://www.gnu.org/licenses/agpl-3.0.txt”*. 🔴 **`package.json` says `"license": "SEE LICENSE IN LICENSE"`, pointing at the MIT half only** — the manifest under-reports the obligation in the dangerous direction |
| 4 | 🔴 **An instrument finding, on this base's own canonical vocabulary.** [`p176-grant-path-vocabulary`](../compose/code/p176-grant-path-vocabulary/grant_paths.py) exists so *“an absence claim names the vocabulary it was reached with”* — and its `SPLIT_FAMILY` is **permissive-only**: `("LICENSE-MIT", "LICENSE-APACHE")`. **`is_grant_path("LICENSE-AGPL")` is `False`.** 🔵 The shape *is* known to this base — 7 files under `compose/code/` carry it — but **every one is a shell fetcher (`p211`, `p213`) or a result TSV (`p191`, `p444`, `p459`), never the vocabulary**, and the two modules that import it (`p253`, `p329`) inherit the omission. 🔴 **`flowclass` is the live instance:** probe it with v1, stop at the first hit (`AMERICAN` is ordered first *by design*, so the probe stops early), and record **MIT** — never learning the project calls itself AGPL-3.0 when self-hosted. 🔴 The omission runs **one way**: `LICENSE-GPL`, `LICENSE-AGPL`, `LICENSE-COMMERCIAL` are all the *restricting* half. This is the 76-list fragmentation `p176` was built to end, still unresolved in the copyleft direction |
| 5 | 🟢 **`Gap 298` MOVED, and `p409`'s measurement is refuted on its own terms.** `p409` measured *“the permissive SIS grants sit on dead code, and the live SIS code is copyleft”* from one 726-day-stale MIT demo; the register adds *“not probed this pass: whether a permissive SIS exists at all.”* 🟢 It does: [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement) (“EduTrack ERP”) — **MIT, 1,077 B, HEAD `e75afa5` 2026-10-04 · 19 d**, 156 tracked paths, three tiers (`frontend/` React 18/19 + Vite 6 · `server/` Express 4.21 + WebSocket · `backend/` Java 21 DAO layer), `database/student_management.sql`, `.env.example`, `DESIGN.md`, `CONTRIBUTING.md`. 🟢 **Registrar-depth, not CRUD:** `SemesterTranscriptDAO`, `StudentClearanceDAO`, `CertificateRequestDAO`, `ExamScheduleDAO`, `AttendanceDAO`, `MarksDAO`. 🟡 **Not closed — restated:** single author (`com.krrish`), a vendored `mysql-connector-j-8.4.0.jar` built from a hand-written `backend/sources.txt` with **no `pom.xml` or `build.gradle`**, `data/students.txt` as a flat file, and a README trading in superlatives. **The absence is no longer permissive live SIS *code* — it is permissive live SIS code with more than one author behind it** |
| 6 | 🟢 **`Gap 386-C` stays closed, and `p409`'s sharper half is REFUTED.** `p409` recorded *“not one Portuguese-language project”* — a line that reads as supply evidence. 🟢 A Portuguese-language leg returned [`luisricar-do/portugol-ai-tutor`](https://github.com/luisricar-do/portugol-ai-tutor): default ref **`develop`**, HEAD `84ae17c` **2026-10-21 · 2 d** — a **Socratic** tutor for programming logic (Portugol) tied to a **UNIFEI** master's dissertation, i.e. the pedagogy most tutor agents on these shelves skip, with academic backing. 🔴 **Licence `GPL-3.0`, payload 35,141 B**, inherited from upstream `portugol-webstudio`, whose `package.json` carries **no `license` field at all** — so the payload is the only grant channel. 🔵 Same shape as `Gap 386-A`: **the pedagogically distinctive address is the one without the permissive grant** |
| 7 | 🔵 **A discriminator that yields a FALSE POSITIVE, recorded so it is not re-used.** Grepping a ~35 KB payload for `Affero` to separate AGPL-3.0 from GPL-3.0 **does not work**: `portugol-ai-tutor`'s **GPL-3.0** payload contains *“Affero”* **3 times**, because GPL-3.0 **§13** is titled *“Use with the GNU Affero General Public License”*. 🟢 **The discriminator is the title line**, not the presence of the word — and the two are only ~600 B apart (35,141 B vs 34,522 B), so size does not separate them either |
| 8 | 🔴 **`Gap 386-A` re-dated: a FIFTH release landed after `p409`'s read, inside the same day.** `p409` read npm `brightspace-mcp-server` at **5.0.12** earlier on 2026-10-23. An independent read this pass: **`5.0.13`, published 2026-10-23**, `license: MIT`, `repository: git+https://github.com/RohanMuppa/brightspace-mcp-server.git`. 🔴 **5.0.8 → 5.0.13 inside one day.** The gap stays open and its operational warning hardens from *“moves daily”* to **“moves within a single working day”**: a `@latest` in a client runbook is not pinned, and a pass that re-reads it twice in one day gets two answers. 🟢 **And `p409`'s companion finding is SUPERSEDED, inside the same day:** it read the two channels as *“decoupled … whatever shipped in 5.0.9–5.0.12 is not visible at the default ref”* and advised *“read the tags, not `main`.”* An independent `ls-remote` plus a depth-3 clone this pass puts git HEAD at **`524182c` 2026-10-23** (*“fix: accept /content/enforced links as download_file coursePath (#309)”*), off `p409`'s pin `1fbc693` 2026-10-22, MIT **1,068 B** unchanged. 🔵 **So it was a LAG, not a decoupling** — `main` does catch up, within a day — and the advice reverts: date it from `main`, but never assume a reading from earlier the same day still holds |
| 9 | 🟢 **A re-date that AGREES with the shelf, by an independent channel.** `p393` enumerated [`henriquebotelhogomes/educacao`](https://github.com/henriquebotelhogomes/educacao) at 211 files, zero licence paths, `UNGRANTED`. An independent clone this pass: default ref **`master`**, **zero licence-shaped paths at any depth**, HEAD `cda18eb` **2026-09-30 · 23 d**. 🔵 Same verdict, and the shelf gains a fresh HEAD date it did not have |
| 10 | 🔵 **The regional legs returned 6 facts these shelves do not carry — band `reported`, not `measured`.** Singapore's **National AI Impact Programme** (40,000 technology professionals over three years) and baseline AI training mandated for **all higher-education students from 2027**; **AI Verify** functioning as a de-facto vendor requirement; **Beijing's ≥8 hours** of AI instruction per student per year; India's **₹500 crore** centre of excellence and **₹10,372 crore** IndiaAI mission behind mandatory AI from **Class 3 in 2026–27**; Mexico's **Estado de México** education-law reform (April 2026) on graduated AI use in *media superior* and *superior*; Colombia's **PL 043/2025 Senado · 324/2025 Cámara**. 🔴 **Every one is from a secondary source** — vendor blogs, trackers and aggregators — so all six enter at band `reported` and none supersedes `p406`'s statute-level detail |
| 11 | 🔴 **Negative and adjacent rows, published with their reasons.** [`asadbekme/education-crm`](https://github.com/asadbekme/education-crm) — **zero licence-shaped paths at any depth**, HEAD `4202d7e` 2025-08-08 · **441 d**: ungranted *and* stale. [`willianangelomn-spec/curupiracode`](https://github.com/willianangelomn-spec/curupiracode) — MIT 1,110 B, HEAD `e17b37b` 2026-09-01 · 52 d, Brazilian and live, but a **general-purpose** local-agent harness, **not education**. [`ishandutta2007/Awesome-Higher-Education-CRM`](https://github.com/ishandutta2007/Awesome-Higher-Education-CRM) — MIT 1,068 B, HEAD `e74cee2` 2026-10-13 · 10 d: an **index**, not software. 🔵 All three shelved so the same legs do not re-return them as supply |

### 🟢 `Pattern AI` — the grant-resolved adoption gate, built because three of eight addresses this pass would have passed a first-line check

🔵 **The problem this solves, measured rather than imagined.** Of the eight addresses this pass
read, **three** carry a grant path whose *content* does not support the grant its *metadata* claims.
A studio that reads the first line of `LICENSE`, or the `license` field of the manifest, adopts all
three — and in the one case that matters most (`flowclass`), the deployment mode the client wants
(self-hosting) is precisely the mode the **copyleft half** governs.

🔴 **This is not a pattern for composing agents. It is the gate that runs before one is composed** —
and it is wired from instruments this base already has.

**Wiring, concretely:**

1. **Enumerate, do not probe** — `git clone --depth 1 --filter=blob:none --no-checkout <url>`, then
   `git ls-tree -r HEAD --name-only`. 🟢 A blobless, checkout-less clone costs almost nothing and
   returns **every path at every depth**, which is a claim no path list can make.
   🔵 `p176`'s [`enumeration_beats_probing()`](../compose/code/p176-grant-path-vocabulary/grant_paths.py)
   sets the boundary at **200 tracked files** — `StudentManagement` is 156, so it is enumerable;
   `espocrm` is not, and there a path list plus `p176`'s vocabulary is the honest second best.
2. **Collect EVERY grant-shaped path, then discard the vendored ones.** 🔴 `addex12/School-CRM` has
   **five**, and **four** are dependency grants (`PhpSpreadsheet/`, `vendor/cboden/ratchet/`,
   `vendor/composer/`, `vendor/composer/pcre/`). A first-hit reader attributes **Composer's** licence
   to the project. 🔵 Rule: a grant path under `vendor/`, `node_modules/`, `third_party/` or
   `native/*/packages/` is a **subtree** grant, and the base already has `gate-subtree-grant` for it.
3. **Match `LICENSE-<FAMILY>` siblings too — and do NOT stop at the first hit.** 🔴 `flowclass`
   carries `LICENSE` **and** `LICENSE-AGPL`; the second is the one with teeth. 🔴 Until `Gap 410-A`
   is fixed, `p176`'s v1 vocabulary **cannot see it** — so until then, match
   `(^|/)(LICEN[CS]E|COPYING|NOTICE)([-._][A-Za-z0-9]+)*$` and treat **two hits as two grants**.
4. **Identify the licence by its TITLE LINE, and verify it by its SIZE.** 🟢 Title line:
   `git cat-file -p HEAD:<path> | grep -m1 -v '^[[:space:]]*$'`. Size:
   `git cat-file -s $(git rev-parse HEAD:<path>)`. Then **ratio against the canonical size of the
   licence the title names** — Apache-2.0 **11,358 B**, GPL-3.0 ~**35,141 B**, AGPL-3.0 ~**34,522 B**,
   MIT **1,066–1,110 B**. 🔴 **Below ~50 % of the named licence, report `NOTICE-OR-STUB`, never a
   licence** (`Gap 410-B` — the floor is unmeasured, so treat 50 % as a placeholder and say so).
   🔴 **Never grep for `Affero` to tell AGPL from GPL:** GPL-3.0 §13 is *“Use with the GNU Affero
   General Public License”*, so `portugol-ai-tutor`'s **GPL-3.0** payload matches it three times.
5. **Read the manifest as a THIRD channel that may be wrong in either direction.** 🔴
   `School-CRM`: payload Apache-2.0, `composer.json` **MIT**. 🔴 `flowclass`: `"SEE LICENSE IN
   LICENSE"` — names the **permissive half only**. 🔴 `portugol-ai-tutor`: **no `license` field at
   all**, on a fork, so the inherited payload is the *only* channel. 🟢 `p409`'s `idurar` is the
   worst case already on the shelf: `"Fair-code License"`, which is **not an SPDX identifier**, and
   a reader who checks the manifest ends up **worse off than one who checked none**.
6. **Add the registry as a fourth channel where one exists, and pin an EXACT version.** 🟢 npm
   `brightspace-mcp-server` publishes `license: MIT` *and* a `repository` field, and the two agree.
   🔴 But it went **5.0.8 → 5.0.13 inside 2026-10-23**, read **twice on the same date with two
   answers** — so a runbook saying `@latest` has no fixed meaning. **Pin the version in the SOW.**
7. **Emit a verdict with its channels, never a bare SPDX id.** The row a proposal can stand on is
   `slug · default_ref · grant_path · payload_bytes · ratio_vs_named · manifest · registry ·
   HEAD · age · verdict` — the shape of
   [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p410.tsv). 🔵 A verdict
   without its channels cannot be re-tested, and a verdict that cannot be re-tested is inherited
   rather than known.

🟡 **Where the gate lands on this pass's eight addresses — the output a studio would act on:**

| address | gate verdict | what a proposal may say |
|---|---|---|
| `shrikrishna-lab/StudentManagement` | 🟢 **MIT, resolved on 2 channels** (payload 1,077 B; no manifest field) | 🟢 Fork, modify, ship, attribute. 🔴 Add the bus-factor-one risk and the missing build file to the risk register — **a clean grant is not a clean dependency** |
| `espocrm/espocrm` | 🔴 **AGPL-3.0, resolved** (payload 34,522 B) | 🟢 Fine as the **client's own** self-hosted system. 🔴 Not as a studio-hosted multi-tenant product without the source offer |
| `luisricar-do/portugol-ai-tutor` | 🔴 **GPL-3.0, resolved on 1 channel only** (payload; manifest silent, fork) | 🟢 Host it. 🔴 Do not embed modified code in a proprietary deliverable. 🟡 Confirm the fork's grant with upstream before it is contractual |
| `ivan-my-wong/flowclass` | 🔴 **UNRESOLVED — dual, copyleft half is a stub** | 🔴 **Blocked pending a written grant.** The self-hosting the client wants is the mode AGPL-3.0 governs |
| `addex12/School-CRM` | 🔴 **UNRESOLVED — 3 channels, 3 answers; 531 d stale** | 🔴 Do not adopt, and do not spend another probe |
| `asadbekme/education-crm` | 🔴 **UNGRANTED — 0 grant paths at any depth; 441 d stale** | 🔴 Unusable on either count alone |
| `willianangelomn-spec/curupiracode` | 🟢 **MIT, resolved** (1,110 B + `NOTICE.md` + 3 subtree grants) | 🟡 Usable, but **not education** — a general agent harness. Scope it honestly |
| `ishandutta2007/Awesome-Higher-Education-CRM` | 🟢 **MIT, resolved** | 🔵 It is an **index**. Cite it as a place to look, never as a dependency |

🔵 **`Pattern AH` (the LMS-of-record assistant, `p409`) composes on top of this and its premise
CHANGED:** it was written *“where there is no permissive SIS to fork.”* 🟢 There is one now — and
`Pattern AH` still holds, because the reason moved from **licence** to **authorship**. 🔴 A pattern
whose premise is refuted but whose conclusion survives should say so in writing, or the next pass
inherits the old reason and defends the wrong thing.

### 🔴 The census, carried forward and marked NOT re-derived

🔴 **`p409` published 2 730 harvested shapes → 35 not addresses → 2 695 addresses**, and
**3 529 addresses over both channels**. 🔴 **This pass shelves 8 new addresses, so by this base's own
`gate-census-currency` rule those figures are `STALE` — and `p410` cannot re-derive them**, because
`make address-shape-census` is code in this clone and this session will not execute it.

🟢 **So they are left standing as `p409`'s figures, labelled stale, rather than re-stated as
`p410`'s.** 🔵 `p409`'s own note applies unchanged: *history is not edited to match.* A successor
with an executable `make` should run `make address-shape-census` and `make union-currency` as the
**last act before its commit**, and should expect **+8** on the address count from this pass alone.

## 🆕 `p409` · 2026-10-23 — a search result that says **MIT** over AGPL, the repository behind this base's own *unattributable* npm row, and four declared absences re-tested rather than re-asserted

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fifteenth pass dated today**,
after `p395`–`p408`.

🟢 **This is a RESEARCH pass.** The prescribed brief ran in full — four global legs and one leg per
region, eight in all. 🔴 **It returned ~20 candidate addresses, of which 6 were unshelved against a
base of 2,702** — and not one of the regional policy or adoption facts it surfaced was new. `p408`
reported the same eight legs returning nothing; **this is the second consecutive pass where the
prescribed brief is saturated, and that is now the finding rather than the preamble.**

🟢 **So the legs that would have been spent padding were spent re-testing this base's own declared
absences** — `Gap 297`, `Gap 298`, `Gap 386-A`, `Gap 386-C`. A declared absence is the one thing a
saturated brief can still move: either it has been filled since it was declared, which is a real
finding, or it has not, which re-dates the gap and makes it checkable instead of inherited.

🔵 **Channel note.** `api.github.com` returns **403** through this session's proxy — `p408`'s
reading, re-confirmed first-hand. Every licence, ref and date below is therefore read from **git
itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second channel.
Evidence: [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p409.tsv) (7 rows) and
[`channel-disagreement`](../evidence/channel-disagreement.2026-10-23-p409.tsv) (10 rows).

### 🆕 `p409` — Pattern AH: the LMS-of-record assistant, built where there is no permissive SIS to fork

🔵 **When to reach for it.** A school, district or university engagement in **North America** (or
anywhere under a human-oversight mandate) where the client already runs **Brightspace/D2L**, Open edX
or Moodle plus a copyleft or commercial SIS, and the ask is an AI assistant over their own records.
🔴 **The constraint that shapes the whole build is measured on these shelves and not negotiable:
there is no permissive SIS to fork** (`repos/foundations.md`, `Gap 298` — the MIT SIS grants sit on
dead code, the live SIS code is GPL/LGPL), and the regulatory layer in Oklahoma, Maryland and
California bars AI from high-stakes student decisions and from training on student data.

🟢 **So the pattern is: never ingest, never decide. Integrate read-only against the system of record,
and put a named human on every write.**

**Step 0 — the licence gate, before a single dependency is chosen.** 🔴 Three channels, in this
order, for every candidate:
1. `git clone --depth 1 --filter=blob:none --no-checkout <url>` then
   `git symbolic-ref --short HEAD` — **read the default ref first**; `idurar/idurar-erp-crm` is
   `master`, and a `main`-only probe reports "no licence file" on a repository that has one.
2. `git cat-file -p HEAD:LICENSE | head -1` and `git cat-file -s HEAD:LICENSE` — **the payload and
   its byte count**, not a badge. Try `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `license.txt`,
   `COPYING` before concluding absence (`frappe/lms` is lowercase `.txt`).
3. `git ls-tree -r --name-only HEAD | grep -iE 'licen|copying|notice'` — **whole tree, every depth**,
   because `openSIS-Classic` keeps its grant one directory down.
🔴 **Never accept a manifest's `"license"` field as the answer** — iDURAR's says `"Fair-code
License"`, which is not a licence, over a payload that is AGPL-3.0.

**Step 1 — the LMS leg.** 🟢 **Brightspace/D2L:**
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) — MIT
(1,068 B payload-read), HEAD `1fbc693` 2026-10-22, **472 commits, 6 tags**, root of an eight-member
fork family, npm `brightspace-mcp-server` **5.0.12** published 2026-10-23. 🔴 **Pin the exact
version** — it shipped four patch releases inside one day, and `@latest` in a client runbook moves
under you. 🔴 **Do not reach for [`n35da/brightspace-mcp`](https://github.com/n35da/brightspace-mcp)
however well it fits** — read-only, every tool a `GET`, straight against D2L's JSON API, and
**ungranted on four channels**: no licence at any depth in the tree, no manifest field, README
silent, npm record silent. 🟡 It is the right shape and you have no permission to use it; **write
that server yourself** if read-only-by-construction is a client requirement, and treat `n35da` as
the design sketch you may read but not copy.
🟢 **Open edX:** [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) +
[`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) —
**AGPL-3.0**, `v0.1.5`, 2★. 🔵 Costs nothing extra in licence terms if the client is already inside
Open edX's own AGPL; the risk is **maturity**, so budget for hardening, not for relicensing. Native
`openedx-platform` APIs only, and authorisation rests on the platform's **own** staff/superuser
flags, re-checked live per request — which is exactly the property a human-oversight mandate wants.

**Step 2 — leave the SIS alone.** 🔴 No fork, no migration, no ingest. Read it through whatever
interface it already exposes (OneRoster where present), and **keep the records where the registrar's
authority already sits**. 🟢 This is what makes AB 1159 answerable: student data never enters a
training set because it never leaves the SIS.

**Step 3 — the oversight layer, which is the deliverable.** 🟢 Every AI action lands as a
*proposal* against a named human approver, with the model slot pinned to one provider —
`OpenMAIC`'s `openmaic.yml` governance model is the shelf's working reference (named slots,
user-supplied keys forbiddable, a capability switchable off with `video: null`). 🔴 In Oklahoma and
Maryland this is not a feature, it is the thing that makes the deployment lawful.

**Step 4 — teacher-facing first.** 🟡 NYC's one-year moratorium on student-facing AI through grade 8
is being copied. Ship the teacher workflow (drafting, grading support, communications) and keep the
student-facing surface behind a flag you can turn off per jurisdiction.

🟢 **Shape and timing.** 6–8 weeks to a governed pilot on one LMS: 1 week on Step 0 and the
read-only integration surface, 2–3 weeks on the LMS MCP leg and its auth, 2 weeks on the
oversight/approval layer, 1–2 weeks hardening. 🔵 **The whole pattern is permissive except the Open
edX leg**, which is AGPL by the platform's own choice — so quote D2L and Moodle engagements as MIT
all the way down, and Open edX engagements with the AGPL stated up front.

## Pattern AG

### 🆕 `p408` — the India DPI engagement: MIT the whole way down, with the fork check as step 0

🔵 **When to reach for it.** An APAC/India engagement where the client is a state education
department, a DIKSHA-adjacent programme or a CBSE/NCERT-aligned private network, and the
requirement is in-country inference plus a permissive grant the client can extend without
publishing the extension. 🟢 This is the one stack on these shelves that is **MIT at every layer**.

**Step 0 — the fork-provenance check, and it is not optional here.**
🔴 `p408` found a fork of Sunbird documentation carrying **AGPL-3.0** while upstream is **MIT**,
returned *above* upstream by search. Before any Sunbird address enters a proposal, pin the grant to
the ref:
```bash
git ls-remote --symref https://github.com/<slug> HEAD          # the REAL default ref (Sunbird docs = dev, portal = master)
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> r
git -C r cat-file -s HEAD:LICENSE                               # 1,072 B ≈ MIT · 34,520 B ≈ AGPL-3.0
git -C r fetch -q --depth=1000 origin "$(git -C r symbolic-ref --short HEAD)"
git -C r log --format='%h %cI %s' --follow -- LICENSE            # did the grant CHANGE, and in which direction?
```
🟢 The last line is the one `p404`'s gate exists for: **direction is only establishable from full
history**, and a byte-identical blob sha against upstream's pre-relicence blob proves *frozen*
rather than *re-licensed*.

**Step 1 — the platform.** [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
(`master`, 🟢 MIT) as the content-and-delivery spine, with
[`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (`main`,
🟢 MIT) where a handset is the real client. 🔴 **Budget the staleness, do not discover it:** 311 d
and 399 d since HEAD respectively. Fork at a pinned SHA, run the client's own dependency and CVE
sweep before week 1 ends, and price a maintenance line. 🔴 Do **not** name
`Sunbird-Ed/sunbird-learning-platform` in a deliverable — it does not resolve.

**Step 2 — the offline edge.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
(🔴 `develop`, 🟢 MIT) for low-connectivity districts, which is most of the addressable footprint
and already this shelf's most important repo for that constraint.

**Step 3 — the assessment layer.** [`Naitik-xd/CurriculumCraft-AI`](https://github.com/Naitik-xd/CurriculumCraft-AI)
(`main`, 🟢 MIT, HEAD **2026-10-03**) for CBSE/NCERT Grades 9–12 item generation. 🟢 Take its
*constraint* as the requirement, not just its code: it is built to generate without reproducing
verbatim NCERT text, which is the copyright exposure a client's counsel will actually ask about.
🔴 It is **public beta** and says so — wire it behind human review, never as the graded instrument.

**Step 4 — inference, in country.** `CurriculumCraft-AI` already targets **open-weight Gemma**, so
serve it locally rather than re-architecting: this is the APAC data-residency posture without a
sovereign-cloud contract.

**Step 5 — grounding, and the licence trap to avoid.** Use
[`crpf-mitadt/Indian-AI-for-Education`](https://github.com/crpf-mitadt/Indian-AI-for-Education) as
the **discovery index** for Indian ASR/TTS/OCR and translation assets. 🔴 **It is CC0-1.0 over the
document only** — every asset it names keeps its own grant, so each one re-enters at Step 0. Never
cite the index as the licence for anything inside it.

**Shape of the engagement.** 10–12 weeks: 1 week for Step 0 across every address plus the CVE
sweep; 4 weeks portal fork, pin and deploy; 2 weeks Kolibri edge sync; 3 weeks assessment layer
behind review; 1–2 weeks local-inference hardening.
🟡 **What this pattern does NOT give you:** multi-tenancy (no Sunbird row here claims it), a current
upstream to pull from, or a compliance story. For the last of those, Vietnam's Decision 33 and
Korea's `AI Basic Act` are the APAC instruments — see [`intel/market.md`](../intel/market.md) — and
India's own posture is a separate read this base has not closed.

## 🆕 `p406` — a standing existence check becomes a step in every pattern, and `Pattern C` gets a dated APAC variant

### 🟢 `Pattern Z` — the pre-engagement address audit, now a command rather than a habit

🔴 **Every pattern on this shelf names repositories, and 1.94 % 🔵 *(`p407`; `p406` published 2.20 %, counting 7 non-repositories as decay)* of the addresses this base carries do
not resolve.** Two of them are **inside a recipe on this very file**. 🟢 The check is now one command
and it needs no clone budget:

```bash
# offline: what the shelves name (no network)
make carried-existence-census                 # -> 2 682 addresses over nine shelves

# online: does each one still answer?  p293's control pair gates every verdict
make carried-existence-sweep                  # ~2.5 min at 12 workers, ~17 probes/s
WORKERS=6 make carried-existence-sweep        # throttling is retried serially, never
                                              # counted as decay
```

🔵 **Wire it as the first step of an engagement, before a single repo is cloned.** The channel is
`git ls-remote --symref`, so it costs **no object transfer** — which is why this is affordable where
`api.github.com` answers `403` on a scoped session and a clone-per-address does not fit any budget.

| what it returns | what to do with it |
|---|---|
| `EXISTS-PUBLIC` | 🟡 the address answers **today**; maintenance is a separate question (`p173`) |
| `EXISTS-NO-REFS` | 🔴 **an EMPTY repository.** It EXISTS and ships nothing — a 404 check passes and the dependency is still vapour |
| `ABSENT-OR-PRIVATE` | 🟡 absent, private **or MOVED** — probe a guessed successor before deleting a row |
| `CHANNEL-ERROR` | 🔵 says nothing about the slug. Retry serially; never read as decay |

🔴 **And the step this pattern must NOT skip: adjudicate by reading the sentence, not the verdict.**
All 12 unresolvable addresses on `agents/top.md` turned out to be **already documented as dead** —
cited as warnings and as specimens, not as recommendations. A sweep reads addresses, not prose
(`Gap 406-A`). 🟢 The realised loss on this base was **zero**; the instrument's value is that the
**next** one is caught the same hour rather than whenever a pass happens to clone it.

### 🟢 `Pattern AA` — repair a dead address instead of deleting the row

**Worked example, verified this pass end to end.**

```bash
# 1. the sweep flags it
grep -P '\tABSENT-OR-PRIVATE\t' evidence/carried-existence.2026-10-23-p406.tsv
#    apereo/opencast   ABSENT-OR-PRIVATE   -   agents/top.md;repos/foundations.md;...

# 2. probe guessed successors — the ORG move is the common shape
python3 -I compose/code/p293-slug-existence-oracle/slug_oracle.py --online \
        opencast/opencast apereo-opencast/opencast
#    EXISTS-PUBLIC   opencast/opencast        153d1b15c93afa5bf915ee31cdfec75ecfc5284e

# 3. read the grant at the pin — a successor's licence is NOT inherited from the row
git clone --depth 1 https://github.com/opencast/opencast /tmp/oc && head -3 /tmp/oc/LICENSE
#    Educational Community License, Version 2.0 (ECL-2.0)
```

🟢 **Result: a dead foundation row became a live one with its grant re-read**, and `repos/foundations.md`
already carried both the successor and a redirect row — so the repair was a **confirmation**, which is
the cheapest possible outcome. 🔴 **Step 3 is not optional:** `apereo/opencast` and `opencast/opencast`
are different licensors as far as this base is concerned, and ECL-2.0 is **not** on the MIT/Apache
shortlist a proposal usually prices against.

### 🟡 `Pattern C` variant — the APAC education compliance pack, priced to the RIGHT date

🔴 **This file's `Pattern C` and `intel/market.md`'s opportunity 5 both priced an education
engagement against Vietnam's `2027-03-01`. That is the all-other-sectors date.** 🟢 Education's is
**`2027-09-01`** for a system live before **2026-08-15**, and **`2027-03-01`** only for one deployed
inside the six months after Decision 33 took effect.

**The recipe, unchanged in parts and re-dated in one:**

| layer | what | why |
|---|---|---|
| **1 — system of record** | **Moodle** (GPL-3.0) or **Open edX** (AGPL-3.0); **OpenOlat** (Apache-2.0) or **Kolibri** (MIT) where copyleft is refused | 🟢 the **0 %-decay** tier — see `T83` |
| **2 — integration** | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) *(MIT, npm)* or [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(MIT, crates.io)* — 🟢 **both re-probed `EXISTS-PUBLIC` this pass** | 🔴 the **5 %-decay** tier: pin a version and vendor the client, per `Pattern Z` |
| **3 — agent** | compose, don't adopt: LangGraph/CrewAI over the layer-2 tools | the volatile layer stays replaceable |
| **4 — conformity** | the **Annex III** pack from the EMEA engagement, re-mapped | 🟢 **portable** — EU → Vietnam → Mexico, adapts far cheaper than it rebuilds |

🔵 **The dated argument to a client, stated correctly:** a system **already live before 2026-08-15**
has until **2027-09-01**; a **new** one has **six months** from go-live under the post-Decision-33
clause. 🔴 **The cutoff has already passed**, so for any engagement starting now the six-month clause
governs — which is a *tighter* deadline than the one the old row quoted, reached by getting the law
right rather than by rounding toward urgency. 🟡 **Bound:** no primary text was read — every policy
host answers `ENOTFOUND` on this session — so this rests on five concurring law-firm readings.
Counsel confirms before it goes in a proposal.

### 🔵 One recipe step retired

🔴 `compose/patterns.md`'s step *"8. Re-check dead addresses. Four in common circulation do not
resolve…"* named **four** addresses and asked the reader to re-check them **by hand**. 🟢 Superseded
by `Pattern Z`: the population is **2 682**, not four, and the check is a make target.

---

## 🆕 `p405` — the layer-2 Moodle MCP choice was a GPL-or-vendor-a-commit decision, and it is not any more

🔴 **`p404` wrote this file's layer-2 decision tree and closed it with:** *"`peancor` is the only
permissive option measured here, and its **0 tags** means the pattern vendors a pinned commit rather
than tracking a release."* 🟢 **Refuted, with two addresses, both read first-hand from full clones on
2026-10-23.** 🔵 The reason `p404` could not see them is a method fact worth keeping: it measured the
slug **`moodle-mcp-server`**, and these are **`moodle-mcp`** — a different slug for the same
engagement question.

```
layer 2 of Pattern I (the network boundary), Moodle side — REVISED, pick by DEPLOYMENT not by grant:

  no Moodle-side install possible (no admin, no token, SSO/2FA in the way)
      -> falkenslab/moodle-mcp                MIT  1,067 B   npm @falkenslab/moodle-mcp
         Node + Playwright; drives a REAL BROWSER SESSION as the teacher
         + nothing to install in Moodle: no web-service token, no plugin, no administrator
         + ~230 tools; works on any Moodle 4.5 / 5.x the user can already log into
         + students pseudonymised to the model (A-7KQ2XM), de-aliased only on the operator's box
         + 6 tags v0.1.0..v0.5.0, 194 commits, HEAD 1 d        <- A PUBLISHED RELEASE
         - a browser session is a seat, not a service: it acts AS one teacher, not as the site

  Moodle Web Services available, and IT wants one binary to deploy
      -> G36maid/moodle-mcp                   MIT  1,064 B   crates.io moodle-mcp
         Rust (rmcp 3.5, edition 2024, Rust 1.88); single static binary, stdio
         + Moodle 3.7 -> 5.x via the mobile-app web service; CI + Codecov
         + 7 tags v0.1.0..v0.2.1, 163 commits, HEAD 3 d       <- A PUBLISHED RELEASE
         + SSO driver for NTUST, credentials mode verified at NTNU (Taiwan)
         - student-first tool surface: a teacher-side workflow needs the option above

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server        GPL-3.0  35,148 B   Python/fastmcp
         + 3 tags; root commit by Marina Glancy (Moodle core provenance)
         - copyleft: it cannot sit inside a proprietary layer-3

  same Node runtime as ltijs / lti-tool, and MIT required
      -> peancor/moodle-mcp-server            MIT  1,064 B   TypeScript/Node
         - 0 tags: still vendor a pinned commit.  NO LONGER the only permissive option

  wire-up, all cases, unchanged:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The decision axis changed, and that is the useful part.** `p404`'s tree branched on **grant**,
because grant was the only thing that distinguished the two addresses it had. 🔴 **With four options,
grant stops discriminating** — three of the four are MIT — and the question becomes *what can you
actually install on the client's Moodle?* 🔵 **Ask the client's LMS administrator one question before
choosing:** *can we have a web-service token?* A `no` eliminates two of the four options and makes
`falkenslab` the answer; a `yes` opens the Rust binary, which is the one a school IT department will
sign off on.

🟡 **A config line this pattern needs, same class as `p404`'s.** `falkenslab` runs a **browser session
as a real user**, so it inherits that user's permissions and **nothing narrows them server-side**.
🔴 The limits are enforced in the MCP server's own config, which means **the agent's blast radius is a
client-side setting**. 🟢 Pin it in the engagement's config, enable read-only or course-scoped mode
explicitly, and treat *"students are pseudonymised"* as a property to verify in the deployment rather
than to quote from the README.

### 🟢 New, concrete: picking an LMS MCP server when the client's LMS is NOT Moodle

🔴 **This file and [`verticals/solutions.md`](../verticals/solutions.md) have cited LMS MCP servers by
bare slug, and the slug is a name-collision group of up to 20 addresses.** 🟢 Measured
2026-10-23 — 42 addresses, 269 pairs — the heads are:

```
pick by the client's LMS; each line is a MEASURED family head, not the first search result:

  Canvas      -> vishalsachdev/canvas-mcp          MIT 1,071 B  1,089 commits  23 tags  1 d
                 + root-commit author of ELEVEN of the 20 Canvas addresses
                 ! do NOT clone bartmassey-upstream/canvas-mcp: the slug says upstream and
                   the root commit says fork (1,001 commits, DIVERGED-FORK)
                 ! r-huijts/canvas-mcp is a SEPARATE project (root 2024-12-12, Fontys NL),
                   61 commits, 3 tags, npm - keep it if you want the npm package, and know
                   that mdweaver/canvas-mcp is its 3-commit superset with 0 tags

  Blackboard  -> alanwtom/blackboard-mcp           MIT 1,065 B     26 commits   1 tag   1 d
              or felipedias-ie/blackboard-mcp      MIT 1,084 B     21 commits   3 tags  9 d
                 ! the largest Blackboard address is 28 commits: READ these, do not depend
                   on them.  Budget writing your own.
                 ! bibo242/blackboard-mcp shows 28 commits and is the ANCESTOR of
                   felipedias-ie - its extra commits are on refs unreachable from its HEAD

  Brightspace -> RohanMuppa/brightspace-mcp-server MIT 1,068 B    472 commits   6 tags  1 d
                 ! THREE of the four Brightspace addresses are this one author's lineage.
                   Price it as a single-maintainer dependency and say so in the SOW.
                   The only independent address is 7 commits, Apache-2.0, 374 d.

  Moodle      -> see the revised layer-2 tree above: TEN independent implementations,
                 the only genuinely uncollapsed supply of the four platforms.
```

🔵 **Why the "!" lines are the valuable part of this recipe.** Each one is a wrong clone a studio would
otherwise make from the search index: a fork named `upstream`, a 28-commit repository that looks newer
than its own descendant, and a four-address "ecosystem" that is one person. 🟢 Instrument, 12 controls
and all 269 graded pairs:
[`compose/code/p405-group-lineage/`](code/p405-group-lineage/README.md) ·
[`group-lineage.2026-10-23-p405.tsv`](../evidence/group-lineage.2026-10-23-p405.tsv).

---


## 🆕 `p404` — two recipes on this file named the wrong address, and the fix is one line each

🟢 **Both corrections come from full-history clones read on 2026-10-23**, with the instrument and its
9 controls at [`code/p404-fork-direction/`](code/p404-fork-direction/README.md).

| recipe cell | was | 🟢 **is** | why it matters to a build |
|---|---|---|---|
| **`Pattern I` layer 1** — the `core_ai` provider plugin | *"cloned from `ADORSYS-GIS/…` **or** `lmscloud-io/…`"*, described as two independent vendors | 🟢 **Clone [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** — **8 d**, Moodle 5.0+ CI matrix, listed in the Moodle Plugins directory. `lmscloud-io` is its **origin** and is **93 d** | 🔴 *"Either"* sends half of engagements to a dormant address. The two are **one lineage** — `CONTENT-COPY`, direction `lmscloud-io` → `ADORSYS-GIS` — not a choice between vendors |
| **`Pattern` LTI/Go-JVM** — the Go options | `peregrine-lti` **679 d** and `macewan-cs/lti` **1,918 d** | 🟡 Add [`astiusa/lti`](https://github.com/astiusa/lti) — **794 d**, MIT, a **strict superset** of `macewan-cs` (89/89 commits reachable) | 🟢 The *conclusion* is unchanged — **do not put a client's identity flow on any of them** — but the file was 1,125 days out on the freshest permissive Go option, and that number is what a client challenges |

🟡 **A config line `Pattern I` now needs.** `ADORSYS-GIS` **dropped** `$plugin->supported = [500, 502]`
when it republished, keeping only `$plugin->requires = 2025041400`. 🔴 So the live plugin declares **no
Moodle upper bound** and Moodle will not warn on an untested major. 🟢 **Pin the Moodle version in the
engagement's own config** and treat the plugin's compatibility as unstated rather than open.

### 🟢 New, concrete: choosing a Moodle MCP server, which is an MIT / GPL-3.0 decision, not a name

🔴 **`moodle-mcp-server` is two independent implementations** — **0 shared commits AND 0 shared trees**
— and this base has cited the bare plugin name. The two differ in **language and in grant**, so the
name alone cannot carry a recommendation:

```
layer 2 of Pattern I (the network boundary), Moodle side — pick by grant, not by name:

  proprietary or MIT/Apache deliverable
      -> peancor/moodle-mcp-server          MIT  1,064 B 845ac6ac9e57   TypeScript/Node
         + same runtime as ltijs / lti-tool, so one Node service carries LTI *and* MCP
         - 0 tags: vendor a commit, do not "install" it; 243 d, so budget maintenance

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server      GPL-3.0 35,148 B 8b1ba204bb69  Python/fastmcp
         + 3 tags v1.0.0..v1.0.2 - the ONLY published artefact of the two
         + root commit by Marina Glancy (Moodle core provenance) - read it either way
         - copyleft: it cannot sit inside a proprietary layer-3

  wire-up, both cases:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The boundary is what makes this a free choice**: GPL-3.0 is not network copyleft, so a GPL layer-2
MCP server still leaves layer 3 ownable — 🔴 but only if the client accepts shipping a GPL component at
all. 🔵 Where they will not, `peancor` is the only permissive option measured here, and its **0 tags**
means the pattern vendors a pinned commit rather than tracking a release.

---

## 🆕 `Pattern I` — 🆕 `p403` The India engagement: an in-language tutor you can actually *prove*, with a deterministic eval gate

🔵 **The engagement this answers.** India's mandate makes **AI and computational thinking compulsory
from Class 3 from the 2026–27 academic year** (see [`intel/market.md`](../intel/market.md) → APAC). A
ministry or large-group client will ask for a tutor in Hindi and at least one other state language. 🔴
**The thing that sinks these pitches is not the tutor — it is being unable to demonstrate that the
tutor is correct in a language the buyer's own reviewers read.** An English benchmark plus
*"the model is multilingual"* is not evidence, and an LLM-judge score is not evidence a reviewer can
re-run.

🟢 **What `p403` makes newly possible:** the eval half is now available, permissive, in-language and
**rule-based**, so it runs in CI and returns the same number to the client as it does to you.

### The stack, with the grant on every piece

| role | component | grant | why this one |
|---|---|---|---|
| **Tutor runtime** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | Lifelong learner memory + RAG grounded in the learner's own uploaded materials; the largest education-native permissive base on these shelves. Apache-2.0 keeps the patent grant a government buyer's counsel will look for. 🔵 Swap in [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (🟢 **MIT**) instead **if** the client wants generated whole-classroom delivery and central model governance — see `Pattern Q`. |
| **🆕 Eval gate (the new piece)** | [`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) | 🟡 **MIT** code · **`CC-BY-4.0`** dataset | **14 Indic languages + English**, verifiable **rule-based** constraints, bundled `lm-evaluation-harness`. 🟢 **Deterministic — no LLM judge** — so it belongs in CI, and the client can re-run it themselves. |
| **🆕 In-language ground truth** | [`AI4Bharat/Anudesh-Backend`](https://github.com/AI4Bharat/Anudesh-Backend) | 🟢 **MIT** | `projects → tasks → users/review` workflow with organizations and workspaces: the machinery for getting teachers to author and review in-language rubrics and answer keys, with an audit trail. 🔴 Default ref **`master`**, **0 tags** — vendor a pinned commit. |
| **Mastery model** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) + [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** | Bayesian Knowledge Tracing the client can inspect and **re-estimate on their own logs** — "adaptive" as a parameterised model, not a prompt. |
| **Retention** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | FSRS spaced repetition + knowledge graph, and runs on local open-weight models with no key — the data-residency path. |
| **LMS surface** | client's **Moodle** | 🔴 **GPL-3.0** | Reach it through the plugin API, **do not fork** — `Pattern A` and the GPL-adapter sandwich in `Pattern Q`. |
| **Teacher AI-literacy material** | [`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi) | 🔴 **NO GRANT** | 🔴 **Reference only — do not vendor, do not redistribute, do not quote into deliverables.** Read it for *sequencing*: it is U Tokyo Matsuo Lab's `AIE2026` localised Hindi-first, and students build a learning agent progressively across the course. 🟢 That progression is the useful artefact; re-author it yourself. |

### How it wires together

1. **Ingest and ground.** Client curriculum (NCERT / state board) → DeepTutor's RAG store. 🔵 There is
   no permissive **Indian** curriculum graph on these shelves — `os-taxonomy` is NGSS/Common Core and
   its data is `ODbL-1.0 AND CC-BY-SA-4.0`. 🔴 **State that as a build item in the SOW**; `Pattern H`'s
   *"ground on a curriculum graph you must not fork"* rule applies, and `p388`'s BC and BNCC servers are
   the shape to copy, not reuse.
2. **Author ground truth in Anudesh.** One `project` per subject-grade; `tasks` are prompt +
   expected-constraint sets written **by the client's own teachers**; reviewers approve. 🟢 Output is a
   constraint set in `IndicIFEval`'s verifiable form, not free-text opinions.
3. **Gate the build in CI.** Run `IndicIFEval` (`indicifeval-ground` for native items,
   `indicifeval-trans` for translated) per target language on every model or prompt change. 🔴 **Fail
   the build on per-language regression, not on an aggregate** — an aggregate hides Odia collapsing
   while Hindi improves, which is precisely the failure a state buyer will find first.
4. **Adapt and retain.** OATutor/pyBKT fit mastery on the client's real logs; OpenTutor's FSRS
   schedules review. Both MIT, both inspectable.
5. **Deliver through Moodle's plugin API.** No fork, so no GPL obligation on the client's own IP.

### 🔴 The three things that will bite, named up front

- **`CC-BY-4.0` on the benchmark data.** Commercial use is fine; **attribution is not optional**. 🟢
  Put the AI4Bhārat attribution in the eval report and in any published score — the deliverable is the
  report, so the obligation travels with it. The MIT grant on the harness does **not** cover the data
  (`T36`, fourth instance).
- **These are research assets, not products.** `IndicIFEval` has **6 refs**; `Anudesh-Backend` has **0
  tags** and a `master` default ref. 🟢 Pin commits, vendor, and own the maintenance — that *is* the
  billable value, and it should be priced as such rather than discovered in month three.
- **14 languages is the benchmark's reach, not the tutor's.** 🔴 Scoring in Marathi does not mean
  teaching in Marathi. 🟢 Use the gate to **decide which languages to promise** — ship the three that
  pass and name the rest as phase two, rather than promising fourteen and failing in public.


**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🟢 **One new pattern, and it exists because
the licence census forced its shape.**

## 🆕 `Pattern Q` — the GPL-adapter sandwich: Arabic-first AI on a Moodle base without surrendering the IP

🔵 **Why this pattern and not a tutor demo.** Two measurements from this pass fix the architecture
before any product decision: the Gulf mandates are **statutory and dated** (`SA` and `AE`
`curriculum_mandate` `MANDATED`, 2025/26), and **every one of the 51 readable grants in the Moodle
plugin family is `GPL-3.0-or-later`**. 🔴 So the obvious build — put the clever part in a Moodle
plugin — gives the clever part away. 🟢 The pattern puts the GPL boundary where it costs nothing.

### The three layers, with the licence of each stated

| layer | component | licence | why it is here |
|---|---|---|---|
| **1 · in-platform adapter** *(GPL, thin, contributed back)* | A `core_ai` provider plugin, 🆕 🟢 **cloned from [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** *(`p404`: the live address, **8 d**; [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) is its origin and is **93 d** — `CONTENT-COPY`, direction established)* | 🟡 **GPL-3.0-or-later** *(read from `version.php`; **no licence file** at any ladder path)* | Moodle's own supported extension point, so no core patching and no upgrade debt. 🟢 Both vendors' `classes/provider.php` is **byte-identical at 3,963 B** — a de-facto standard shim. 🔵 Keep it thin: auth, request shaping, error mapping. Nothing proprietary crosses into it. |
| **2 · the boundary** | An **MCP server** the plugin calls over the network | 🟢 **Yours — MIT/Apache or closed** | 🔵 GPL-3.0 is **not** network copyleft. Code the plugin merely *calls* across a process boundary is not a derivative work of it, which is what makes layer 3 ownable. 🔴 This boundary is the entire point of the pattern; collapse it and layer 3 becomes GPL. |
| **3 · the grounding and the IP** | Arabic curriculum corpus + retrieval + evaluation | 🟢 **Yours**, seeded from **MIT** sources | Seed content from [`openaziz00-sudo/Arab-Artificial-Intelligence`](https://github.com/openaziz00-sudo/Arab-Artificial-Intelligence) (**MIT**, 1,650 Arabic prompts / 17 categories) and teacher-facing scaffolds from [`kazoya/build-your-own-agent-ar`](https://github.com/kazoya/build-your-own-agent-ar) (**MIT**). 🔴 **Do NOT seed from** [`sartaj1995/arabic-tutor`](https://github.com/sartaj1995/arabic-tutor) (100 levels, 1,367 exercises — **no grant at the ladder**) or [`michaelsboost/ArabEngo`](https://github.com/michaelsboost/ArabEngo) (**CC-BY-NC-4.0**, NonCommercial). |

### Wiring it, concretely

1. **Fork the provider plugin** and point its endpoint at your gateway, not at a model vendor.
   🔵 Read the grant from `version.php`, not from the GitHub sidebar — 27 of this family's 51
   grants have **no licence file to read**.
2. **Stand the MCP server up outside the LMS**, exposing exactly the tools the curriculum needs
   (retrieve-objective, generate-practice, grade-free-text, explain-in-Arabic). 🔵 The parent- and
   teacher-facing MCP servers already on [`agents/top.md`](../agents/top.md) are the shape to copy.
3. **Ground on the corpus you own**, aligned to the UAE MoE's **seven curriculum areas** for an
   AE engagement and to the National Curriculum Center's scope for `SA`.
4. **Keep the evaluation harness on your side of the boundary.** 🟢 It is the deliverable the EU AI
   Act's Annex III conformity assessment will want evidence of for any EMEA client whose system
   touches assessment — and the same artefacts serve a Gulf ministry procurement.
5. **Contribute layer 1 upstream.** 🔵 It is GPL anyway; contributing it buys maintenance you would
   otherwise owe, and credibility with the one platform the client already runs.

### 🔴 What this pattern does NOT claim

🔴 **There is no Arabic-first platform to start from.** The entire permissive Arabic education
supply found on 2026-10-23 is **three repositories, 4 ★ at best, all created within six weeks**
([`arabic-supply-leg`](../evidence/arabic-supply-leg.2026-10-23-p401.tsv)). 🟢 Layer 3 is **built,
not assembled**, and the pattern says so rather than implying a stack exists. 🔵 That is also the
argument for moving now: the demand is statutory and the supply is not yet anybody's.

🔴 **And the one component that would make this cheap is the one that is unlicensed.**
`sartaj1995/arabic-tutor`'s 1,367 structured exercises are the single richest Arabic content asset
this base has found, and with **no grant at any ladder path** they cannot be used. 🟢 **An email to
that maintainer asking for an explicit MIT grant is a lower-cost first move than building the
corpus** — and it is the kind of ask that succeeds, because the repository already reads as
intended-open.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🔴 **No pattern
was added: the one unshelved address this pass found is unlicensed, and there is nothing to
compose with an unlicensed repository.** 🟢 **Both axes of the two-axis pre-flight got sharper
anyway, and one of them got sharper in the dangerous direction.**

🟢 **The jurisdiction axis — APAC is no longer a blank.** Every recipe here is gated on
*(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every APAC teaching-mandate query with a single `NOT_ESTABLISHED` row** — and in a pre-flight a
blank reads as *"no rule"*, which is the dangerous direction to be wrong in. 🟢 It now answers
with **seven** rows. The two that change a build:

- 🟢 **`CN-BJ | curriculum_mandate | MANDATED | 2025-09-01`** — **≥ 8 class-hours per academic
  year across all Beijing primary and secondary schools.** 🔵 Any recipe here that ships a
  tutoring or courseware surface into Beijing acquires a **contact-hour accounting**
  obligation: the deliverable must be able to *evidence* hours delivered per learner per year,
  which is an LRS/record-layer requirement, not a model requirement. 🔵 This base already holds
  the record-layer supply problem (`p396`: one 15 ★ MIT MCP bridge, 419 days dead, is the whole
  agent↔LRS supply) — 🔴 **so the obligation now has a named instrument and the stack to satisfy
  it is still the thinnest tier on these shelves.** That pairing is the pattern-relevant fact.
- 🟡 **`IN-CBSE | curriculum_mandate | MANDATED | 2026-27`, with `IN | NOT_ESTABLISHED`** — a
  recipe aimed at Indian Classes 3–5 must deliver **into Mathematics and "The World Around
  Us"/EVS**, because that is where the curriculum puts it; a standalone "AI for Class 3" surface
  is **mis-shaped for the only instrument that binds**, and AI proper does not begin until
  Class 6. 🔴 There is **no board exam**, so no assessment-integration pressure — which removes
  a requirement most recipes here would have assumed.

🟢 **The licence axis — the gate that admits candidates to a recipe now exists as code.**
Patterns here compose named repositories, so a pattern is only as good as the claim that its
parts are real and carried. 🔴 **That claim was being made with a bare-name grep**, which is a
substring match (`400-C`). 🟢 [`p400-candidate-membership`](code/p400-candidate-membership/README.md)
answers it by exact address over **both** of this base's address channels, and reports
`NAME-SUBSTRING-ONLY` as its own class so a candidate can no longer be dropped silently.
🔵 **Use it before adding a repository to any recipe below:**

    python3 -I compose/code/p400-candidate-membership/membership.py classify owner/name

🔴 **And the honest limit, stated so the pre-flight is not oversold:** the licence axis can be
settled first-hand from this session (`raw.githubusercontent.com` → **301**, payloads served);
the jurisdiction axis **cannot** (every policy host → **000**). 🔵 So every row in
`policy-matrix.tsv` is band `reported` by construction, and a recipe gated on jurisdiction is
gated on a single-channel claim. **Say so in the engagement, and re-read the instrument from a
session with egress before a deliverable depends on it.**

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No pattern
was added, because no new supply arrived to compose with** — the supply legs returned seven
candidate addresses of which six were shelved and the seventh is not education-native.

🟢 **The two-axis pre-flight gets materially better without a single pattern changing.** Every
recipe here is gated on *(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every LATAM teaching-mandate query with a blank** — 11 rows across `ai_literacy_instruction` and
`curriculum_mandate`, none of them LATAM — 🔴 **and a blank in a pre-flight reads as "no rule",
which is the dangerous direction to be wrong in.**

🟢 **It now answers with six rows.** The one that changes a build:

- 🔴 **`CO` · `Ley 2626 de 2026` · MANDATED · binding on official schools.** Any pattern here
  delivering curriculum or AI-literacy content into Colombian **public** education now has a named
  statute to conform to, and 🔴 **a `Feb 2027` deadline for the curricular guidelines** — which is
  the date an engagement plans against, not the **2026-08-24** sanction date.
- 🔵 **`AR`, `CL`, `MX`, `BR`, `UY` · ADVISORY_NONBINDING · `PE` · ADOPTED.** These bind nothing and
  must not be pitched as compliance drivers; they are **adoption** signals, and the honest use is
  scoping a pilot's ministry alignment, not selling a compliance deliverable.

🔵 **Recorded here as a change to how the existing recipes are gated, not as a new recipe** — the
same judgement `p398` made for the `OpenMAIC` commit-pinning rule. `Gap 399-A`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No pattern was
added or amended, because no new supply arrived to compose with.** Eight search legs returned one
address this base did not hold, and 🔴 **it is archived** — which disqualifies it as a pattern
component outright. 🔵 **The one recommendation change is a pinning rule, not a new recipe:** every
pattern here that names [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) should pin a
**commit**, not a tag — `v1.3.0-rc.1` (2026-10-22) opened while `v1.2.0-rc.1` (2026-10-04) had still
not reached stable, so a tag-based dependency on this project has nothing stable to point at. 🔵
Recorded here rather than as a new pattern because it changes **how** the existing ones are built,
not **what** they are. `Gap 398-C`.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **`p396` ranked
re-running the xAPI 2.0 bake-off second, on the grounds that *"three claimants at 1 star between them
will move fast or die; either outcome changes the recommendation."* They moved — and they did not
move together.** One new pattern, and `Pattern AE` amended rather than restated. Evidence:
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) ·
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

## 🟢 `Pattern AE` AMENDED — the xAPI 2.0 bake-off now has an activity ranking

🔵 `Pattern AE` told a studio to adjudicate three zero-star LRS claimants itself, because *"reputation
cannot decide this."* That still stands. 🟢 **What `p397` adds is the one signal that was missing:
which of them is actually being built.** Dated on the git channel, never on the HTML "Updated" column
(`396-G`):

| candidate | stack | `p396` | `p397` HEAD | days | reading |
|---|---|---|---|---|---|
| [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | ASP.NET Core | "under 75 d" | `0d47d65` 2026-10-21 | 🟢 **1** | 🟢 **under active daily development** |
| [`codetakt/kiva`](https://github.com/codetakt/kiva) | Rust, F\* proofs | "under 75 d" | `addf100` 2026-10-21 | 🟢 **2** | 🟢 **also moving**; 🔵 still the only one whose README *withdraws its own conformance claim* |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | TypeScript/Hono/Postgres | "under 75 d" | `4d18e0c` 2026-08-08 | 🔴 **75** | 🔴 **has not moved at all** since `p396` measured it |

🟢 **So the "all three are under 75 days" sentence has split into two live projects and one
stalled one**, and the bake-off order changes accordingly: 🟢 **run `xapi-dotnet` and `kiva` first**,
and treat `xapi-lrs` as the control rather than a contender until it commits again.

🔴 **The tooling half of `Pattern AE` is the part that has aged, and it matters more than the
candidates.** [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
is 🟢 MIT, 78 ★ — and **`5bc232d`, 2025-09-04, 413 d**, unchanged. 🔵 **You are asked to certify
2.0 conformance with a suite that has not been touched in fourteen months**, while the implementations
it judges change weekly. 🟢 [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner)
(Apache-2.0, **6 d**) and [`yetanalytics/xapi-schema`](https://github.com/yetanalytics/xapi-schema)
(**6 d**) are both live, so the **CI harness around the suite is maintained even though the suite is
not.** 🔴 **Quote that asymmetry to a client before you quote a pass rate.**

## 🆕 `Pattern AF` — prove provenance BEFORE you prove the licence, in two commands

**When.** Any engagement that is about to adopt, fork or warrant an open-source education component
— and especially when the candidate came out of a search result rather than a standards document.

🔴 **Why it goes first.** A licence read **cannot** tell a fork from its upstream: the payload is
usually byte-identical, so the grant channel is blind by construction (`395-A`). A star read cannot
tell a rename from a fork either: GitHub answers on the old organisation path indefinitely and shows
the same stars. 🔴 **On these shelves, 8 of 15 shared-root pairs were renames and 7 were real
forks** — and nothing short of comparing commits separates them.

**The recipe, and it needs no API, no HTML and no credentials.**

1. **Root commit** — shared root means shared ancestry:
   `git clone --filter=blob:none --no-checkout -q https://github.com/OWNER/REPO d && git -C d rev-list --max-parents=0 HEAD`
2. **HEAD** on the same clone: `git -C d rev-parse --short=12 HEAD`
3. **Adjudicate**: same root + same HEAD → **one artefact, two addresses** (fold them, cite the
   current path); same root + different HEAD → **a real fork** (now decide which side to carry);
   distinct roots → **unrelated** despite the shared name; either side unresolvable → **inconclusive**,
   never "independent".
4. 🟢 **Then date both sides**, because step 3 tells you the fork is real and nothing about whether
   anyone maintains it. `T40` is the cautionary case: `ucfopen/pylti1.3` is a genuine institutional
   fork of `dmitry-viskov/pylti1.3`, and **both are over 1 370 days dead.**
5. **Only now read the grant**, and read it by enumerating the tree
   (`git ls-files | grep -iE '(licen[cs]e|copying)'`) rather than guessing filenames — that is how
   this pass found [`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples)
   ungranted at root with vendored third-party MIT two directories down.

🟢 **Wired and runnable:** `bash compose/code/p397-shelf-fork-audit/lineage.sh OWNER_A/REPO OWNER_B/REPO`,
with `make shelf-fork-candidates` deriving the candidate pairs from the shelves themselves and
`make gate-shelf-fork` holding 11 controls. 🔴 **Stated limit:** a squashed or re-rooted fork reads as
independent — no false positives, possible false negatives.

🔵 **Cost: two blobless clones per pair, a few seconds each.** `p397` ran 21 pairs inside one pass.

### 🆕 `p402` AMENDMENT — a cheaper front door, and the missing step 3b

🟢 **Front door: `git ls-remote` needs NO clone.** Comparing the **full ref set** of two addresses
answers the identity question for the price of one network round-trip each:

```sh
git ls-remote https://github.com/OWNER/REPO | sort | sha256sum   # ref-set fingerprint
```

Identical ref set → **one repository**. 🔴 **Identical HEAD alone is NOT identity** — `p370` demoted
five pairs from `STALE` to `DISTINCT` on exactly that, because *a redirect serves ONE repository, so
a different ref set is a different repository*. `sharziki`↔`rohanmuppa` `purdue-mcp` share HEAD
`6922f1f301dd` and have **5 vs 3** refs; `Halleck45`↔`chinobv` `openpronounce` share HEAD
`74bc17ea406e` and have **10 vs 4**. 🔵 Use the clone arm (steps 1–2) when you need the **root**, to
separate a rename from an unrelated repo that merely shares a name.

🔴 **Step 3b, which this pattern was missing.** Step 3 says *"fold them, cite the current path"* and
gives **no way to find that path**. The ref set proves *one repository*; it never says *which
address is canonical*. 🟢 **The channel that does: fetch EITHER address over HTTPS and read the
header/breadcrumb of the page you LAND ON.** GitHub serves a rename or transfer as a redirect, the
fetcher follows it, and the page names the canonical owner — plus the archive banner, the licence
and any `forked from` parent in the same read.

🔴 **The trap, stated because it cost this base ~52 passes.** The redirect is followed **silently**,
so two stale addresses both report *"not a fork"* with **identical star counts** — indistinguishable
from two independent repositories. *Same stars · no fork line · two owners* is the signature.
🟢 It is how `p402` found that `ease`'s canonical address is **neither** candidate in the register
but a third owner, [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease), and
closed `ACTION ZZ-al`.

🔵 **Engagement rule.** Warrant the **canonical** address, not the one in the search result — and
when the canonical owner is named `*-unsupported` or carries an archive banner, that **is** the
stewardship finding. Read it before promising a client a maintained dependency.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Two patterns, both built on grants and dates
read first-hand this pass:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

## 🆕 `Pattern AD` — the agent that writes to the institution's record, not just its own memory

**When.** The client needs to show *someone else* — an accreditor, a regulator, a district board, a
parent — what the AI did and what the learner actually demonstrated. This is every North America K-12
engagement under Oklahoma-style teacher-review and opt-out rules, every EU deployer under Article 26
logging, and the governance sale that `intel/market.md` identifies as the LATAM entry point.

🔴 **Why you cannot just use the agent's memory.** `DeepTutor`, `inno-agent` and every other tutoring
agent on this shelf keep private, vendor-shaped memory designed for conversational continuity. It is
not an evidence record, it does not survive replacing the agent, and no registrar will read it
(`T37`).

**Components, all dated this pass.**

| Role | Component | Licence | Age | Note |
|---|---|---|---|---|
| Record store (Python shop) | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT | 🟢 10 d | France Université Numérique; Open edX Aspects' own LRS |
| Record store (JVM shop) | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | 🟢 21 d | 144 ★; SQLite/Postgres/MariaDB/MySQL |
| Record store (.NET shop) | [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | 🟢 1 d | 🔴 0.x, 1 ★ — gate on a conformance run |
| Platform emitter (Moodle) | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 GPL-3.0 | 🟢 2 d | 82 ★; GPL because every Moodle plugin is |
| Agent ↔ LRS bridge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT | 🔴 **419 d** | **the weak link — see below** |
| Launch into the LMS | `packbackbooks/lti-1-3-php-library` / `ltijs` / `lti-tool` (`p395`) | 🟢 permissive | 🟢 1–9 d | pick by runtime |

**Wiring.** Agent → MCP (`learnmcp-xapi`) → LRS (`ralph` or `lrsql`); LMS → emitter
(`moodle-logstore_xapi`) → *the same* LRS; agent launched from the LMS over LTI 1.3 so the learner
identity on both paths is the same subject. 🔵 **The single design decision that makes this worth
building:** the agent's statements and the platform's statements land in **one** store against **one**
identity, so "what did the AI do for this student" and "what did this student do" are one query.

🔴 **Scope this honestly at estimate time.** `learnmcp-xapi` is 15 ★ and has not moved in fourteen
months. 🟢 It is MIT, it is small, and the xAPI statement shapes it needs are specified — so treat it
as **a reference to fork and own, budgeted as build, not as a dependency**. Anyone quoting it as
maintained third-party infrastructure will be wrong by about a year.

**Effort.** 6–8 weeks for a single-LMS, single-agent deployment on an existing Moodle or Open edX;
add 3–4 weeks to own the MCP bridge properly rather than vendoring it.

## 🆕 `Pattern AE` — choosing an xAPI 2.0 LRS when every candidate has zero stars

**When.** The client specified xAPI 2.0 / IEEE 9274.1.1 — increasingly common in defence, aviation,
regulated corporate training and any procurement written against the current standard.

🔴 **The situation, measured.** No adopted open-source LRS implements 2.0. `lrsql` (144 ★) and Ralph
(51 ★) are both 1.0.3. The three claimants hold **one star between them**: `pelotech/xapi-lrs` (0 ★,
TypeScript/Hono/Postgres), `codetakt/kiva` (0 ★, Rust, F* proofs) and `nurullahturkoglu/xapi-dotnet`
(1 ★, ASP.NET Core). 🔴 **Reputation cannot decide this**, and each project's own conformance claim
is self-reported — `kiva`'s README goes so far as to withdraw its own repository blurb, saying
equivalence with the 2025 edition *"has not been established"* and that source traceability *"does
not establish implementation conformance."*

🟢 **So adjudicate it yourself, with permissive tooling that already exists.**

1. Stand up each candidate against a **throwaway** Postgres — the suite persists data and its README
   warns it *"should not run against a production LRS endpoint."*
2. Run [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (🟢 MIT, 78 ★, Node) with `--xapiVersion 2.0.0`, then again with `1.0.3` — a conformant 2.0 LRS
   must still accept 1.0.x statements.
3. On the JVM, drive the same suite from CI with
   [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) (🟢 Apache-2.0,
   6 d) so the result is a build artefact rather than a screenshot.
4. 🟡 Read failures with judgement: a .NET implementer reports the suite *"sometimes expects more
   than the standard requires"* *(secondary)*, and the suite is **413 days old** while all three
   candidates are under 75 days. A failure is a conversation, not a disqualification.

🟢 **Hedge the choice structurally.** `pelotech/xapi-lrs` states its schema matches `lrsql` v0.9.5's
Postgres shape, so an `lrsql` database can be taken over. 🔵 This pass's fork arm confirms the two are
**independent codebases, not a fork** (distinct root commits `b1bfc0f67292` vs `f9e81c891b9a`) — so
this is genuine schema compatibility between rivals, which is the rare case where a client can start
on the 144 ★ 1.0.3 store and migrate to the 0 ★ 2.0 store without a data conversion.

**Effort.** 2–3 weeks for the bake-off and a reproducible CI conformance job; the result is reusable
across every later engagement on this layer, which is the main reason to do it once properly.


# Compose patterns — education

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Two patterns, both built on grants and **dates**
read first-hand this pass: [`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv) ·
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).

## 🆕 `Pattern AC` — the JVM-or-Go client's LTI edge (the one this base could not quote before)

**When.** The client's platform team owns **Java** or **Go**, and an agent has to launch from their
Moodle, Canvas, Blackboard or D2L. This is most enterprise work and much of European public sector.

🔴 **Why the obvious route is closed.** The only permissive **Java** LTI 1.3 core is
[`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) (MIT) — **1,193 days dead**. The
Go options are [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
(Apache-2.0, **679 d**, pre-1.0 API), [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (MIT,
**1,919 d**, self-declared unstable, **deep linking unimplemented**) and 🆕
[`astiusa/lti`](https://github.com/astiusa/lti) (MIT, **794 d**, a `p404`-measured **strict superset**
of `macewan-cs` — which inherits the same instability warning, untouched by its two extra commits). 🔴 An unmaintained library doing
**OAuth 2 / JWT signing and key rotation** is a *security* dependency — the same argument that
demoted `1EdTech/lti-1-3-php-library`. Do not put a client's identity flow on any of the three.

**Wire it like this.**

1. **LTI edge — [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool)** (🟢 MIT, HEAD **1 d**,
   `@lti-tool/core` v1.3.2). Serverless-native: Lambda, Workers, Hono, with OIDC, **Assignment and
   Grade Services**, Names and Role Provisioning, Deep Linking and Dynamic Registration all
   implemented, and the session store chosen at deploy time. 🟡 Prefer
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 Apache-2.0, **9 d**, 207 npm releases)
   instead when the client wants a long-running Node process and already runs Mongo.
2. **The hop.** The edge validates the launch, then forwards a **signed, short-lived internal token**
   carrying only `sub`, context, roles and the resource link to the JVM/Go service. 🔵 The agent never
   parses an LTI message, which is the whole point: the standards surface stays in the runtime where
   it is maintained.
3. **The agent** stays in Java or Go — the client's own service, unchanged.
4. **Grades back** through the edge's AGS client, never direct from the agent. One component holds the
   platform credentials.

🟢 **Why this beats forking a dead library:** `lti-tool` is 1 day old and `ltijs` 9, so key rotation
and spec drift are somebody's job. 🔴 **Cost to state in the proposal:** one extra deployable and one
extra network hop — *and* `lti-tool` is **8 ★ with no production claim** (its README's
*"Production-ready security features"* heading is about the security section, not the project), so
pilot it; `ltijs` is the safer default for a ministry. 🔵 Note this is the architecture `p391`
recommended for Python and `p392` correctly withdrew when `django-lti` turned up live at 2 days. **It
stands for Java and Go because the dating says so, not because it is the usual advice.**

## 🆕 `Pattern AD` — a learner-facing agent shell with a curriculum you are actually allowed to ship

**When.** The client wants a personal tutor that remembers a learner across months, and the
deliverable must survive a legal review.

1. **Shell — [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent)** (🟢 MIT, **1.3k ★**, HEAD
   **10 d**). You get the parts that are expensive to build: **L1** learner profile, **L2** a native
   wiki knowledge base, **L3** session records with cross-conversation retrieval, a **cron scheduler**
   for proactive check-ins, and a workspace-scoped **Practice Lab** with an in-browser terminal.
   🔵 It sits on the Pi coding-agent SDK (MIT) *without modifying its kernel*, so the upgrade path is
   npm, not a fork.
2. 🔴 **Do NOT ship its skill library.** The companion
   [`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) — skills and
   workspace presets — is **ungranted on every arm** (no licence file, no manifest field, no README
   grant, all three enumerated). Read it for shape; author your own.
3. **Curriculum — granted sources only.** [`oppia/oppia`](https://github.com/oppia/oppia)
   (🟢 Apache-2.0) for misconception-aware lesson structure, and
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) when the
   deployment is offline-first. 🔴 **Avoid grounding the tutor on
   [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) without legal sign-off**
   — `ODbL-1.0 AND CC-BY-SA-4.0`, and the **CC-BY-SA half reaches generated content**, so a curriculum
   document produced from it can inherit share-alike. That is `Pattern H`'s warning, and it is the
   trap this pattern is most likely to fall into.
4. **Launch from the LMS** with `Pattern AC`'s edge, so the tutor is reachable where students already
   are.
5. 🔴 **Regulatory stop, before any design work.** The moment this agent **grades**, **assigns a
   learner to a programme**, **assesses their appropriate level**, or **monitors behaviour during a
   test**, it is **Annex III ¶3 high-risk** in the EU and needs the human-in-the-loop and
   documentation posture. 🔴 And **no emotion inference, ever, in an EU educational setting** — that is
   prohibited outright, not assessable. Keep the memory layers descriptive (what was practised, what
   was missed) and never affective.

🟡 **Honest limits.** `inno-agent` is a **single-learner companion** — there is no cohort, roster or
teacher dashboard in it, so an institutional pilot needs that built. Its IM channels ship as **Feishu
and WeChat**, so a non-APAC deployment replaces the messaging layer. And at **10 days old with a June
2026 technical report**, it is a strong pilot base, **not** a ministry platform this quarter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** Two new patterns, both built on grants
read at the payload this pass. 🟢 **`Pattern AB`** — the **R statistics course graded automatically**,
closing the hole `p393` named when it pointed out that this base's most-adopted *maintained*
autograder grades R
while the shelves held no R components; its delivery layer is permissive (`gradethis` MIT, `learnr`
Apache-2.0, `ottr` BSD-3) and its measurement layer is GPL behind a process boundary, and its last
step is **the only offline assessment loop in this base** (`cran/exams` NOPS: printed, scanned, marked
automatically, paper audit trail). 🟢 **`Pattern AC`** — **give teachers an assistant builder instead
of building their assistants**, on **LAMB** (GPL-3, UPC Barcelona + UPV/EHU, peer-reviewed), which
publishes each teacher-authored assistant into Moodle as an **LTI external tool** so the LMS is never
forked. 🔴 Both patterns carry a hard stop at grading: under the EU AI Act, systems that grade
learners or influence access to qualifications are **high-risk and require conformity assessment
before deployment**, so the grading step is scoped as a separate assessed workstream rather than sold
in the same phase.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

🆕 **`p389`** adds **`Pattern Q`** (the generated classroom, the greenfield answer when there is no
LMS to bolt onto), gives **`Pattern B`** a maintained mastery model, and gives **`Pattern D`** two
components that remove its server. Every repository named in those changes was **dated** this pass —
last commit at the real default ref:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Read a date as a cost line:**
a permissive repository nobody has touched in eight months is something you *vendor and maintain*, not
something you *integrate* — which is why `Pattern B` vendors `pybryt` and why `Pattern Q` pins a ref.

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
   - 🆕 `p390` *Open edX:* skip the MCP hop and run **inside** the platform as an **XBlock** — and the licence maths
     works out better than it looks. The platform is **AGPL-3.0**, but the component API your plugin imports,
     [`openedx/XBlock`](https://github.com/openedx/XBlock), and the [`xblock-sdk`](https://github.com/openedx/xblock-sdk)
     you develop against are both **Apache-2.0** (`LICENSE.TXT`, both dated 2026-10-22). **So the XBlock you write can stay
     MIT or proprietary while running in an AGPL host** — no fork, no LTI hop, and full access to course state.
     [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia) is the working proof.
     🔴 **Check the boundary per package, not per org:** [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning)
     and the `frontend-app-*` MFEs are **AGPL-3.0**, so an import from those pulls network copyleft straight back in.
     Keep the plugin's dependency list to `XBlock` plus your own code and audit it in CI.
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

🔴 🆕 `p387` **Vendor pybryt; do not install it.** PyPI `pybryt` has shipped nothing since
**v0.7.0, 2022-04-28** — four and a half years — so a client support contract cannot rest on it as a
dependency. The pattern does not change: copy the annotation approach (and, licence permitting under
its MIT grant, the code) into the deliverable and maintain it there, with the maintained BSD-3
halves of this stack (`nbgrader`, `otter-grader`) carrying the running infrastructure. Dates:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

🟢 🆕 `p388` **And the notebook-tutor half now has a maintained component, which changes what you
vendor.** [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) (**BSD-3**,
`main` · `139bb11`, **v0.3.2, 7 releases, → 2026-09-25**, from a known Jupyter-ecosystem maintainer)
replaces the ad-hoc "wire `jupyter-ai` into the grading loop" step with a component built for exactly
this job:

- A per-cell **Explain Code** button sends the cell source, the kernel language, **the error
  traceback**, and the preceding cells up to the last markdown cell **as the exercise statement** —
  so the model sees the task, not just the broken line.
- 🟢 **The tutor persona lives in a `TUTOR.md`, discovered by walking up from the notebook's
  directory to the server root.** Each course, module or folder carries its own pedagogy **in version
  control**. This is the single most useful thing on this shelf for a client engagement: *"AI must
  not give the answer"* stops being a prompt someone pasted and becomes a reviewable file in the
  course repository, diffable and auditable per cohort.
- 🟢 **`reference_solution` and `evaluation_criteria` ride in cell metadata, ROT13-encoded** so they
  are not casually readable by a student holding the notebook — the same instinct as `pybryt`'s
  annotations, shipped in a maintained package.

**Revised wiring:** `jupyterhub` → `nbgrader` → `otter-grader` for the lifecycle and
container-isolated grading (all BSD-3, all maintained) → **`jupyter-ai-tutor`** for the in-notebook
explanation layer, configured by a per-course `TUTOR.md` → **vendored `pybryt` annotations** for
approach assessment, maintained inside the deliverable as `p387` requires. 🔵 Note the division of
labour this produces, and it is the one the guardrail below wants anyway: `jupyter-ai-tutor` **explains
and never grades**, `nbgrader`/`otter-grader` grade and never explain. 🟡 It requires
`jupyter-ai-jupyternaut` (<0.1) for the agent, so pin that bound.

🟢 🆕 `p389` **And the missing third component: the mastery model.** Everything above assesses a
*submission*. Nothing in it answers the question a programme director actually asks — **which skills
has this student mastered, and what should come next** — and this base has carried that gap while
recommending a dependency that stopped shipping in 2022. The maintained answer is
[**CAHLR/pyBKT**](https://github.com/CAHLR/pyBKT) (**MIT**, real ref `master`, **last commit
2026-10-21 — 1 day**), from UC Berkeley's CAHLR, who also maintain
[**OATutor**](https://github.com/CAHLR/OATutor) (**MIT**, `main`, **1 day**) as the tutoring front end
built on it.

- **What it adds to this wiring:** fit **Bayesian Knowledge Tracing** on the client's *own*
  `nbgrader`/`otter-grader` outcome logs — one row per (student, skill, attempt, correct) — and you get
  per-skill **learn, guess, slip and forget** parameters plus a running mastery probability per student.
- 🟢 **Why it is the defensible choice and not just the available one:** those four parameters are
  **inspectable numbers a client can argue with**, re-estimated on their own cohort. "The model thinks
  Ana has not mastered partial fractions, with these parameters fitted on this data" survives a
  procurement review; "the LLM judged her weak" does not. North American and Maryland-style rules that
  bar AI from high-stakes decisions about students are satisfiable here precisely *because* the
  decision rule is a published model rather than a generation.
- **Revised wiring, end to end:** `jupyterhub` → `nbgrader` → `otter-grader` (lifecycle + isolated
  grading) → **`pyBKT`** fitted on the outcome log (mastery per skill) → **`jupyter-ai-tutor`** with a
  per-course `TUTOR.md` for in-notebook explanation → **vendored `pybryt` annotations** for approach
  assessment. 🟢 **Still fully permissive: BSD-3 and MIT only, zero copyleft.** 🔵 The sequencing
  matters: `pyBKT` decides *what to work on*, the tutor explains *why the attempt failed*, and the
  graders remain the only components that produce a grade.
- 🟡 **Cold start is the real constraint**, not the licence: BKT needs interaction history. For a new
  cohort, serve `OATutor`'s scaffolds with default parameters, log, and re-fit at the end of the first
  module — and say so in the estimate rather than discovering it in week three.

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer. 🆕 `p389` The same rule governs the mastery model: a BKT mastery
probability is **advisory input to a human decision**, and the moment it auto-finalises anything
consequential it is the "sole basis for a decision without meaningful human review" that Vietnam's
Decision 33/2026 and EU Annex III both reach.

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
[LTI 1.3](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**) when a link is available. 🆕 `p392` **Use a maintained implementation, and pick it by language — all three majors have one.** **Python:** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT, PyPI v0.10.1, HEAD 2026-10-20) **in-process** for a Django agent, or [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 BSD-3) for a JupyterHub. **Node:** `ltijs` (Apache-2.0, npm v7.0.7, 2026-10-06), or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT, npm `@lti-tool/core` v1.3.2) when the target is **Lambda or Cloudflare Workers**. **PHP:** `packbackbooks/lti-1p3-tool` (Apache-2.0, packagist v6.4.4). 🔴 **Not** the standards-body copy `p390` cited (2,333 days stale) and **not** `pylti1.3` (1,431 days) — but `p391`'s conclusion from that second fact, *"a Python agent sits behind a Node or PHP edge rather than speaking LTI itself"*, is **withdrawn**: `Gap 391-A` is closed and the extra service comes out of the budget.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

🟢 🆕 `p389` **Two components that remove a server from this pattern, which is the cost line that
actually kills offline deployments.**

1. **Lesson delivery with no application server at all.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, committed **0 d**) exports a
   finished classroom as **one self-contained offline HTML file that plays the lesson** (or as a PPTX
   that keeps every scene). 🔵 **So the authoring server and the delivery target separate cleanly:**
   generate lessons once where there is power and bandwidth — a ministry office, a regional hub, a
   studio — and ship HTML files to the edge, where they need nothing but a browser. That is a
   fundamentally cheaper edge than "a Kolibri server per school", and the two compose: Kolibri remains
   the catalogue, progress store and sync layer; the exported HTML is the content it serves. 🟡 The
   export is a *playback* artefact — the agentic mid-lesson chat needs the server — so scope it as
   narrated, interactive courseware, not as a tutor that answers back offline.
2. **Notebook exercises with no per-student compute.**
   [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) (**BSD-3**, 6 d) runs the
   kernel **in the browser via WebAssembly**: no container, no install, no server, and it works offline
   once the page is cached. For a CS or data-science module this deletes the single largest
   infrastructure line in `Pattern B` at the edge. 🟡 No server also means no server-side autograding —
   collect the notebook and grade it with `nbgrader` when a link is available.

🔵 **What this pattern now says to a ministry.** The old answer was "a server per school, syncing when
it can." The 2026 answer is **generate centrally, deliver as files, compute in the browser, sync
progress when a link exists** — and every component in it is MIT or BSD-3, so the ministry owns the
deliverable outright. 🔴 One licence caution unchanged: H5P content stays **runtime content** under
GPL-3.0, never linked code.

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

## Pattern H — 🆕 `p384` Prerequisite-aware tutoring, grounded on a curriculum graph you must **not** fork

**For:** the adaptive-learning engagement everyone pitches and nobody can substantiate — "the tutor
knows what the learner is missing". The missing ingredient was never the model; it was a
machine-readable map of what must be mastered **before** the next topic. One now exists.

🔴 **Read this first.** [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
is licensed **ODbL** (`main/LICENSE`, 25,289 B), a **share-alike database licence**, and it has
**no code grant**. The whole pattern is built around keeping it on the right side of §4.4:

| what you do | ODbL clause | obligation |
|---|---|---|
| Tutor **output** grounded in the graph — next-topic choice, lesson plan, explanation, diagnosis | **§4.3** *Produced Work* | 🟢 **Attribution notice only.** Nothing to release. ODbL supplies the wording: *"Contains information from DATABASE NAME, which is made available here under the Open Database License (ODbL)."* |
| Shipping the graph **extended or merged** — client topics added, standards remapped, graph re-cut | **§4.4** *Derivative Database* | 🔴 **Share-alike.** Must be publicly used only under ODbL / a later ODbL / a compatible licence. §4.4(b): extracting *"the whole or a Substantial part of the Contents into a new database"* **is** a Derivative Database. |

🟢 **So the architectural rule is one sentence: join, never merge.** The client's curriculum data
stays in the client's own store; the taxonomy stays a read-only input resolved at query time. Break
that rule and the client's curriculum map becomes an ODbL obligation.

**Wiring:**
1. **Load the graph read-only, in its own store.** `data/topics.json` (1,930 micro-topics, each with
   a plain-language description, mastery **evidence** criteria, a type — conceptual / procedural /
   representational / language / meta — subject, domain and an approximate age range) and
   `data/dependencies.json` (4,102 edges, `topicId` → `prerequisiteId`, each tagged `hard`/`soft`
   with a one-line reason). 🔵 Keep it in a **separate schema or database** from anything client-
   specific, and never write client rows into it — that separation *is* the §4.4 firewall, and it
   should be visible in the deployment diagram so counsel can see it.
2. **Map the client's own curriculum to it by reference, not by insertion.** A join table
   `client_objective_id → topicId` in the **client's** store. The taxonomy's standards alignments
   (**NGSS, Common Core, UK National Curriculum**, Australian curriculum — Mathematics 442
   alignments across 325 topics, English 630/267, Science 245/131, HASS 210/124) usually give you
   the hook. 🟡 Unmapped client objectives are a **finding to report**, not a gap to paper over.
3. **Diagnose with the graph, not with the model's intuition.** Walk the DAG backwards from the
   failed topic over `hard` edges to find unmet prerequisites. This is a **graph traversal, not a
   generation** — deterministic, inspectable, and the reason the pattern can survive an audit that
   a pure-LLM "diagnosis" cannot. Treat `soft` edges as ranking hints only.
4. **Attach the tutor.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**) for
   persistent learner memory plus RAG over the learner's materials, with the traversal result from
   step 3 injected as the lesson objective. Teacher-facing variant: feed the same unmet-prerequisite
   list to [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) to draft the
   remediation worksheet — which is the side of the market that is actually growing (Trend 5).
5. **Schedule the retention.** [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)
   (**MIT**) over the mastered topics. The graph says *what* to review next; FSRS says *when*, with
   published parameters. 🟢 Together they make "personalisation" two measurable quantities instead
   of a claim.
6. **Deliver it through the client's existing LMS**, per **Pattern A** — `webservice_mcp` for
   Moodle, [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for Canvas. For
   K-12 student records, [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (**GPL-2.0**,
   ref `master`) over its API — never linked.
7. **Prove it on the prerequisite claim specifically.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**) for the multi-step maths chain.
   🟢 The honest measurement here is not a headline score: it is **whether remediating the
   prerequisite the graph identified improves the dependent topic**. That is an A/B the client has
   never been offered, and it is the whole value of the pattern.
8. **Ship the attribution notice.** §4.3 costs one line in the product's about page and the
   documentation. Put it in at step one; retrofitting a notice after a client review is avoidable
   embarrassment.

🟡 **Scope the research claim honestly.** The taxonomy's teaching-research payload
(`data/teaching-research.json`, ~24 MB) covers **1,049** topics — Science and Mathematics — and the
maintainers state that **881 topics have no research in this release**. "Research-backed guidance"
is true for roughly half the graph. Check which half a client's subject mix lands in **before** the
claim reaches a deck.

🔵 **Coverage note:** `v1` is primary/elementary and strongest on the Australian and US/UK
standards. Secondary and vocational curricula are not covered — for those, this pattern is the
*shape* to build, with the client's own map in place of the taxonomy.

**Licence posture:** client-owned code is MIT/Apache throughout. Two non-permissive components, both
held at arm's length: the **taxonomy** (ODbL, read-only input, joined never merged — §4.3 notice
only) and the **LMS/SIS** (GPL, reached over a published protocol). **Deliverable stays closed.**

---

## Pattern M — 🆕 `p385` The agent-native classroom (when the client has **no** LMS to bolt onto)

**Pattern A inverts the usual build: an agent over the client's existing LMS. Pattern M is for the
engagement where there is no LMS worth integrating** — corporate L&D, a bootcamp, a professional body,
a ministry pilot — and the deliverable is the learning loop itself, not a Moodle plugin.

**The shape.** The classroom is an **MCP server**; the agent is bring-your-own and replaceable. That
inversion is what makes it worth a pattern: the client is not buying a model, so a model swap (or a
provider outage, or a procurement decision two years out) does not invalidate the asset.

| layer | component | licence | why this one |
|---|---|---|---|
| Classroom / state | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 AGPL-3.0 (`main`) · 🟢 MIT at `v0.1.0` | ~50 MCP tools over courses, lessons, graded exercises and a persistent learner memory. Read **Pattern L step 10 before you pick a ref** — this decision is the whole procurement question |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | learn-shell schedules flashcards with FSRS already; use the upstream parameters so retention is a published model, not a vendor claim |
| Course material ingest | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🟢 Apache-2.0 | the client's PDFs, DOCX and slide decks are the corpus |
| Grounding | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 🟢 Apache-2.0 | document-aware retrieval over that corpus |
| Measurement | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT | the before/after on the client's own subject mix, which `intel/trends.md` Trend 2 makes a procurement precondition |
| Gateway / audit | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | per-user quota and an audit log, which is what gets it past a DPO |

**Wiring.** The agent reaches learn-shell over MCP (JSON-RPC), exactly the boundary Pattern A uses to
stay clear of Moodle's GPL — so the agent code and the prompt/curriculum assets stay the client's.
`unstructured` → `ragflow` builds the grounding index; the agent writes lessons, exercises and
flashcards **into learn-shell** so the evidence of teaching outlives the context window; FSRS decides
what comes back and when; `lm-evaluation-harness` runs the before/after.

🔴 **Three things to say out loud in the pitch, because they are real:**
1. **AGPL reaches hosted use.** If you deploy `main` for the client as a service, the AGPL obligations
   attach to the deployment. The MIT `v0.1.0` tag avoids that and costs you every fix since
   2026-08-16. There is no third option, and this is the decision, not a detail.
2. **v1 is single-machine and unauthenticated by the maintainer's own description.** It is a pilot
   substrate. Multi-tenant auth, isolation and backup are *your* scope — budget them, do not discover them.
3. **It is one maintainer's project.** Weigh that against what it replaces: the alternative is building
   course/lesson/exercise/memory state from scratch, which is the part of this pattern nobody costs correctly.

🔵 **When NOT to use this.** If the client already runs Moodle, Canvas or Open edX, **Pattern A is
strictly better** — the learner records, rostering and gradebook already exist and integration beats
migration. Pattern M is for a greenfield loop, and its honest competitor is not an LMS but a spreadsheet.

## Pattern N — 🆕 `p386` Harden a student-side LMS MCP server into one an institution can deploy

**When to use it.** The client runs **Blackboard, D2L/Brightspace, Canvas or Moodle** and wants an
agent over it. As of `p386` there is a granted community MCP server for **every** one of those
platforms (see [`agents/top.md`](../agents/top.md#the-blackboard-and-d2l-supply-measured)) — so this
is never a greenfield build. 🔴 But **11 of the 12 granted Blackboard/D2L servers authenticate as the
signed-in student**: they ride the user's own browser SSO session, hold whatever rights that user
holds, and have no audit trail. **Licence-clean and still undeliverable.** This pattern is the gap
between the two.

**The parts.**

| role | pick | licence | why this one |
|---|---|---|---|
| Blackboard, institution-grade start | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 MIT | The only server on these shelves that targets the **official Blackboard Learn REST API** and claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrub and a JSON audit log. 🟡 Self-claims — **verify by execution before you quote them** |
| D2L start | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 MIT | Multi-strategy auth (TOTP/OAuth/browser), retry + circuit-breaker + cache, **opt-in** writes. The nearest thing to a hardening base on D2L |
| Canvas start | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 MIT | The clean default; [mdweaver](https://github.com/mdweaver/canvas-mcp) fork adds office hours and syllabus write |
| Moodle start | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 🟡 GPL-3.0-or-later, header-granted | First-party route: it is in **Moodle's own plugin directory**, and the agent reaches it over JSON-RPC so GPL never reaches the agent — **Pattern A**'s boundary |
| Identity / gateway | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | SSO, per-user quota and the audit log that gets a deployment past a DPO |
| Jurisdiction gate | [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) | — | A granted licence does not make **grade write-back** lawful where you are deploying it |

**The work, in order — this is the whole deliverable.**

1. **Replace the session with a service identity.** Swap browser-session auth for the platform's
   own OAuth2 / API-key flow against a **service account scoped to the courses in scope**. If the
   chosen server cannot do this (most cannot), this step is a fork, and it is the reason the
   engagement exists.
2. **Scope by role, server-side.** Student / instructor / admin tool sets, enforced in the server,
   never in the prompt. A model that *can* call `update_grade` and is *asked not to* is not a
   control.
3. **Split read from write, and default write off.** Ship read-only first; put every mutation behind
   an explicit per-deployment flag. `JhostinAleck/brightspace-mcp`'s opt-in-writes design is the
   shape to copy.
4. **Gate grade write-back on the jurisdiction, before any code.** Several jurisdictions in the
   policy matrix gate or prohibit automated grading outright — Oklahoma and Maryland bar AI from
   high-stakes student decisions, the EU AI Act puts assessment in Annex III high-risk, Vietnam
   names automated assessment explicitly, and Illinois SB 2909 reaches *teacher* evaluation. 🔴 This
   gate decides the product's tool list, so run it in week one, not at security review.
5. **Add an audit trail that answers a DPO's actual question**: who (service identity + end user),
   which tool, which course, which record, when, and what the platform returned. Structured JSON to
   the client's existing log sink.
6. **Pin the contract, not the login page.** Pin the vendor API version and put contract tests
   around the tools you use; a student-side server breaks silently when the vendor restyles SSO.
7. **Carry the attribution the payload actually requires** — per **Pattern L step 11**. If you
   started from a fork-family server, the NOTICE file may owe **two** credits.
8. **Prove it before handover.** Execute the maintainer's claims rather than quoting them: run the
   role gate against an under-privileged token, confirm the audit record exists for every mutation,
   and confirm the PII scrub on a real transcript.

🟢 **Why this sells.** It is small, bounded, and the client can show the output to their
data-protection officer — and it is available on every major LMS today, because the licences are
already clear. 🔴 **Say the honest part too:** on D2L all six granted servers are student-side, so
step 1 there is a genuine build and should be costed as one, not as a configuration.

## Pattern O — 🆕 `p387` The LATAM engagement, built on what the region already shipped

**For:** a Brazilian or Spanish-speaking LATAM client — ministry, municipality, university or
school network — where the deliverable has to be in the local language, aligned to the *national*
curriculum, and deployable by an institution rather than demoed to one.

**The premise this pattern corrects:** the LATAM supply is not empty. Every component below is a
real address with a grant read first-hand on 2026-10-22.

**Wiring, Brazil (the fully-specified case):**

1. **Start from the national curriculum, not from a prompt.**
   [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
   (**MIT**, `main`) already anchors generation to **BNCC** skill codes and **discards an invented
   code before the teacher sees it**. Keep that gate and extend it: the gate *is* the trust story,
   and it is the same mechanism `Pattern H` specifies against a curriculum graph.
2. **Deliver through the LMS the client runs, never a new portal.** On **Moodle**, the
   `webservice_mcp` plugin per **Pattern A**; on **Open edX**, start from
   [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, `main`), which is already an
   XBlock/plugin with a teacher statistics panel, TTS and cross-session context.
   🔴 **Licence boundary, non-negotiable:** TutorIA's MIT grant covers *the plugin*. Open edX is
   **AGPL-3.0** and hosting it is hosting AGPL software. Keep the agent a **separate service** the
   plugin calls over HTTP, keep the plugin thin, and the client's AGPL obligations stay exactly
   where they were before you arrived.
3. **Integrate the student-record system over its API.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (**GPL-2.0-or-later**, real default
   ref **`2.12`**) is what a Brazilian municipality is running. Read rosters and write results
   through its API; **do not fork it** — the fork pulls GPL into the deliverable and buys nothing.
   (Its sibling `i-diario` is AGPL-3.0; check per repository, not per organisation.)
4. **Make it multi-tenant before anyone calls it a pilot.** A school network is many tenants. On
   Moodle, [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
   (**GPL-3.0-or-later**, in `version.php`) supplies exactly this — per-role provider routing, rate
   limits, per-tenant enable/disable, usage monitoring — and it reaches the agent over its own API,
   so the copyleft stays on the Moodle side. On Open edX, build the tenant boundary per
   **Pattern N** steps 1–5.
5. **Run it where connectivity is the constraint**, which is the actual deployment profile for
   TutorIA's own users (rural Risaralda) and for most of the nine Google.org rollout countries:
   [Kolibri](https://github.com/learningequality/kolibri) (**MIT**, default ref `develop`) per
   **Pattern D**, with a local open-weight model behind the AI manager's **Ollama** tool rather than
   a metered API.
6. **Schedule retention, in the local language.**
   [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for the scheduler; the
   content language is a data property, not a code property, so this layer ports unchanged.
7. **Measure in the language of instruction, and publish the baseline.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   Portuguese/Spanish task sets built from the client's own past assessments. 🔴 Do **not** ship an
   English benchmark number as evidence for a Portuguese deployment.
8. **Say out loud what you are adding.** The agents exist and are MIT; **tenancy, support,
   governance and curriculum QA are the deliverable.** That is a defensible studio pitch and an
   honest one — and it is cheaper for the client than the rebuild a "no LATAM supply" story implies.

**Spanish-speaking variant:** swap step 1's BNCC grounding for the client's national curriculum
standard, keep TutorIA (Spanish-first) at step 2, and use
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) where no SIS/LMS is in place.

🟡 **Two addresses this pattern deliberately does not use, and why.**
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru) is the
offline-first PWA tutor with explainable difficulty selection that step 5 would otherwise want — it
has **no grant at any of eight probed paths**, so it cannot enter a deliverable, and asking its
author to add a licence is the cheapest possible contribution to the region's supply.
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref `master`) is ungranted for the same reason.

---

## Pattern P — 🆕 `p388` The parent and guardian surface (and the FERPA line that splits it in two)

**For:** a K-12 district, school group or education provider that is being asked — by statute, by
families, or by its own board — to make a student's progress legible to parents, and an engagement
that wants a real deliverable rather than another policy PDF.

🔴 **Read this first: this is two different products, and conflating them is how the engagement
fails.** The code is the same; the obligations are not.

| | **P-1 · parent-side** | **P-2 · district-side** |
|---|---|---|
| Who holds the credential | the **parent**, for their own child | the **institution** |
| What a read is | a parent exercising their own access | a **FERPA-governed disclosure of an education record** |
| Tenancy | none needed — single user, single family | **full multi-tenant**, per-district, per-role |
| Who buys | a provider bundling it, or nobody (it is a tool, not a sale) | the district, through procurement |
| Build cost | days | the real engagement |

**Components (all verified first-hand 2026-10-22 — [`verified-repos`](../evidence/verified-repos.2026-10-22-p388.tsv)):**

- **Infinite Campus (SIS):** [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
  — `main` · `971d58f`, 🟢 **MIT** (1,067 B), **47 npm releases → 2026-10-19**. 20 tools over **Campus
  Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent window, **attendance
  events with codes and comments**, behavior, food service, documents, standardized **assessment
  scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via
  **CUPS SSO**; `FeatureDisabled`-aware, so a district with a module switched off degrades instead of
  erroring — which is what makes it deployable across a group of districts rather than one.
- **Canvas (LMS):** [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
  — `main` · `428b78b`, 🟢 **MIT** (1,067 B), **43 releases → 2026-10-16**. 18 `canvas_*` tools held
  to the **read-only observer scope** (`canvas_list_observees` is the hinge), plus student
  self-access. Four auth modes in priority order. 🟢 Copy its download hardening rather than
  re-inventing it: host-pinned to the Canvas origin, confined to a download directory, never writes
  through a symlink, new files `0600`.

### Wiring P-1 (parent-side) — days, not weeks

1. Parent installs the MCP server locally against **their own** portal credential (token, OAuth, or
   session). Nothing is hosted; no institutional agreement is needed because no institutional
   credential is used.
2. Keep it **read-only**. Both servers are already scoped that way; do not add write tools. A parent
   agent that can submit work on a child's behalf is an academic-integrity incident waiting to be
   filed.
3. Add a **digest** rather than a chat surface: *"what changed this week, what is missing, what is
   due."* 🔵 The persona's actual job is **noticing**, not conversing — the portal already answers
   questions, badly, and nobody logs in.

### Wiring P-2 (district-side) — the real engagement

1. 🔴 **Do not host the parent-side tool for the district.** The moment the credential is
   institutional, every read is a FERPA disclosure. Build the institutional path deliberately:
2. **Put the district's own identity in front of it.** Parent identity comes from the district IdP,
   and **the parent↔student relationship is authoritative from the SIS** — never from a claim the
   agent accepts. `ic_list_students` / `canvas_list_observees` define the blast radius of the whole
   system, so that relationship check is the security boundary, not a feature.
3. **Borrow the tenancy layer that already exists.** This is the same problem `p386` identified for
   student-side LMS servers, and `Pattern A`'s answer applies unchanged: per-tenant configuration,
   per-role rate limits and usage monitoring — on Moodle,
   [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) is the
   worked example to copy the *shape* of.
4. **Log every read as a disclosure, not as a request.** Who asked, for which student, which fields,
   under which relationship, at what time. 🔵 This log is the deliverable a district's counsel signs
   off on, and it is cheap to build on day one and near-impossible to retrofit.
5. **Keep the model away from the record where you can.** Fetch and render deterministically;
   use the model for **summary and prioritisation over data already authorised**, not as the thing
   that decides what to fetch. Smaller surface, smaller disclosure, cheaper review.
6. **Ship the translation layer — it is the actual product.** Gradebook rows are not an answer to
   *"is my kid okay?"* Convert to plain language, in the family's language, at a reading level the
   district specifies, with **no inference about the child beyond what the record states**. A tool
   that volunteers *"your child seems disengaged"* has invented an education record.

**Guardrails:**
- 🔴 **No predictions, no risk scores, no labels.** A parent-facing risk score about a student is
  the high-stakes automated decision Oklahoma and Maryland's frameworks are written to restrain, and
  under the EU AI Act Annex III it is squarely high-risk. Report the record; do not score the child.
- 🔴 **Attendance, behavior, food-service and fee data are the sensitive tail.** `infinitecampus-mcp`
  exposes all four. Free-lunch status and behavior records are the fields a district will refuse last
  and worry about most — scope them out explicitly unless the district asks for them in writing.
- 🟡 **Both servers authenticate as a person.** Treat credential custody as the top risk in the
  design review; a stored parent credential in a studio-hosted service is the worst of both worlds.
- 🔵 **Multiple children, multiple districts.** `ic_list_districts` + CUPS SSO exist because families
  span districts. Test the two-children-two-districts case before a demo; it is the common case and
  the one that breaks naive implementations.

**Why this pattern is worth having at all:** it is the only education surface this base has found
with **granted, maintained components and no incumbent vendor** — the parent portal is a feature of
the SIS, not a market. And **family transparency is already in the statutes** (Oklahoma SB 1734
names it; Maryland's Chapter 634 is built on guidance districts hand down), so the buyer has an
obligation and no product. 🔵 See `Trend 10` in [`intel/trends.md`](../intel/trends.md).

---

## Pattern Q — 🆕 `p389` The generated classroom, governed (and what it supersedes in `Pattern M`)

**For:** a client with **no usable LMS** — a corporate academy, a ministry training programme, a
vocational provider, a new institution — who needs **teachable lessons in weeks, not a platform in
quarters**. Also the fastest credible answer to the EMEA teacher-training demand recorded in
[`intel/market.md`](../intel/market.md): the UAE has **22,000 teachers and education professionals**
to train on a curriculum that became compulsory by Cabinet decision.

**The base:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT** (read from the
payload at `main` @ `269fde2d991f`; `package.json` agrees), Tsinghua University, **committed
2026-10-22**, ~41.3k ★, **JCST 2026** paper, grown out of the internal **MAIC** system and validated
on **700+ students**. 🔴 **Pin `v1.2.1` (2026-10-18), not head.** Head is `v1.3.0-rc.1`, and the
project states breaking upgrade conditions with **no rollback below that release** — a pilot does not
want to be the first to find that out.

### Wiring

1. **Stand up the authoring server.** Node ≥ 22.19, pnpm ≥ 10, **PostgreSQL 16**, a long-running
   server (🔴 **not Vercel** — Vercel deployments are capped at the 1.1.x line, so "we'll host it
   serverless" is a downgrade). Generation is **server-first** from v1.2.0: it survives closed tabs and
   restarts, which is what makes it usable by teachers rather than by engineers.
2. **Write the governance file first, before any content.** `openmaic.yml` declares **providers** and
   assigns every AI use — a named **slot** (`llm`, `course.outline`, slide content, TTS, web search,
   `video`) — to one of them, with keys referenced as `${VAR}` from `.env.local`. 🟢 **Three settings
   are the compliance deliverable, not configuration:** pin each slot to the provider under the
   client's own contract; set the server to **forbid user-supplied keys**, so no teacher can route
   student work through an unvetted account; and set unused capabilities to `null` rather than leaving
   them available. 🔵 **This file is the artefact that answers a district's or ministry's AI policy
   question** — *which model saw student input, under whose contract* — in one reviewable, diffable
   page. Almost nothing else in this base can answer it at all.
3. **Ground the content in the client's curriculum, not in the model.** Feed the jurisdiction's own
   material through the **knowledge base** (v1.3.0 line) or as per-course uploads — parsed once and
   reused — and where a standards graph exists, drive the lesson plan from it rather than from a
   prompt: [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (🔴 **ODbL-1.0 — a database
   licence; reach it over a service, do not fork it into the deliverable**, per `Pattern H`), or
   [`bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) for a
   North American engagement — 🟡 whose crawl is **209 days** old, so budget the re-crawl its MIT grant
   permits.
4. **Keep the record of record outside it.** 🔴 OpenMAIC has **no enrolment, no gradebook of record,
   no transcripts and no stated LTI story**. Pair it with the administration base the client already
   runs or should: [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API),
   [academico](https://github.com/academico-sis/academico) (**MIT**) at SME scale,
   [i-educar](https://github.com/portabilis/i-educar) (ref `2.12`) for Brazilian municipal work, or
   [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) where an ERP is wanted.
   **Completion and scores flow out of OpenMAIC into that system; identity and enrolment flow in.**
5. **Add the mastery model it does not have.** Quiz results are events, not a mastery estimate. Fit
   [`pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 d) on the quiz log per skill, as in the
   revised `Pattern B`, and use it to choose the next lesson. 🟢 This is also what keeps the
   high-risk-assessment line on the right side: the progression decision becomes **a published model
   plus a human review step**, not a generation.
6. **Deliver to the edge as files.** Export each finished classroom as **one offline HTML file** (or
   PPTX). See `Pattern D` — authoring stays central, delivery needs only a browser.
7. **Run the models where the data has to stay.** **Lemonade** for local inference and **FunASR** for
   local ASR are supported paths, not forks — so a deployment that may not send audio or text
   off-premises is a configuration change.

### Why this supersedes `Pattern M` for institutional delivery

`Pattern M` is built on [learn-shell](https://github.com/sf-shenfeng/learn-shell), whose v1 is
explicitly **single-machine and unauthenticated**, and whose grant is **AGPL-3.0 at `main`** (MIT only
at tag `v0.1.0`). That is a fine shape for an individual learner and an impossible one for an
institution. OpenMAIC is **MIT at head**, server-first, multi-user, with central model governance and
a published security practice — five releases since September 2026 carrying SSRF, DNS-rebinding,
token-expiry and provider-redirect fixes under **GHSAs**. 🔵 **Keep `Pattern M` for the
bring-your-own-agent, one-learner case; use `Pattern Q` whenever a client is the buyer.**

### Guardrails

- 🔴 **Auto-graded quizzes are the regulated surface.** Assessment is **Annex III high-risk** in the
  EU and named explicitly in **Vietnam's Decision 33/2026/QD-TTg**. The trigger in both is a decision
  taken on the system's output **without meaningful human review**, so ship the human review step for
  anything consequential and keep its audit trail. A practice score is not consequential; a module
  pass that gates progression is.
- 🔴 **Simulated classmates must be labelled.** An AI teacher with a voice and AI peers in a classroom
  is exactly the surface **EU AI Act Art. 50** transparency and China's labelling rules address, and
  `Pattern G` already covers the mechanics. Label in the UI, not in the terms of service.
- 🟡 **Generated content is a draft until a teacher signs it.** The 2026 procurement trend is evidence
  of instructional benefit; a lesson nobody reviewed cannot be put in front of a class at a client's
  reputational risk. Make teacher review a workflow state, and bill it — it is the part of the
  engagement that is actually about teaching.
- 🟡 **Language and regional fit:** interface is **EN + zh-CN** and the provider catalogue is built for
  a market that includes DeepSeek and Kimi. For a Gulf or LATAM engagement, **localisation of the
  teaching surface is a line item**, and there is no Arabic-first alternative in the open-source supply
  (see `intel/market.md`, EMEA).

---

## Pattern V — 🆕 `p390` The spoken tutor, and the two things that make or break it

**For:** learners who cannot or will not type their way through a lesson — early grades, low typing
fluency, shared-device households, visually impaired learners, and language learning where
*pronunciation is the skill being assessed*. This is also the pattern that reaches the LATAM and
APAC households `Trend 10` describes, where the phone is the only device.

**Why it is a separate pattern:** a voice tutor is not a text tutor with TTS bolted on. Two
properties decide whether a child keeps talking to it, and neither is in the LLM:

1. **Turn-taking.** The tutor must know when the learner has stopped speaking, tolerate a
   four-second pause while a 9-year-old thinks, and **stop talking the moment it is interrupted**.
2. **Latency budget.** Past roughly a second of silence the learner starts talking over it, and the
   session degrades into collision recovery.

**Wiring:**

1. **Do not write the voice loop.** [`livekit/agents`](https://github.com/livekit/agents)
   (🟢 **Apache-2.0**, dated 2026-10-22) is the substrate: full-duplex WebRTC transport, pluggable
   STT/LLM/TTS, **turn detection, interruption and barge-in handling**. All three legs are
   provider-swappable, which is what makes step 4 possible.
2. **Start from the working reference.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
   ("Manu", 🟢 **MIT**, dated 2026-10-07) is a pt-BR maths tutor on exactly that substrate, scaling
   its explanation from 1st grade to university. 🔴 Its README says **"in development" with no public
   deployment** — take the pipeline and the prompt-scaffolding, not a production claim.
3. 🔴 **Put a symbolic checker behind any arithmetic.** Manu's correctness layer is the LLM itself.
   For a maths tutor that is the one unacceptable gap: route every numeric or algebraic claim through
   SymPy (or the client's own CAS) and have the agent *read back* the verified result. A spoken wrong
   answer is harder for a learner to catch than a written one — there is no transcript to re-read.
4. **Localise the ASR, not just the prompt.** Accent and dialect coverage is where regional voice
   tutors fail. [`mozilla/common-voice`](https://github.com/mozilla/common-voice) ships **CC0-1.0**
   corpora across ~130 language variants (pt-BR, es-419 variants, Hindi, Bengali, Kiswahili) — use
   them to *evaluate* candidate ASR models on the client's actual learner population before picking
   one, and to fine-tune where the gap is real. 🟢 CC0 means no attribution and no share-alike, so
   this is safe in a commercial deliverable. 🟡 MPL-2.0 covers the **platform code**, not the corpora.
5. **Keep the mastery model outside the voice path.** Voice is an I/O channel, not a pedagogy.
   [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (🟢 MIT, dated 2026-10-22) holds the Bayesian
   Knowledge Tracing state so "what comes next" survives a dropped call and stays inspectable — which
   is also what makes the decision auditable under step 6.
6. 🔴 **Voice raises the compliance stakes, so settle three things before the pilot.**
   - **Biometrics.** A voice recording is biometric data under GDPR Art. 9 and most LATAM regimes
     (Brazil's LGPD included). Default to **transcribe-and-discard**, keep no audio unless the client
     has a lawful basis and a retention policy, and write that down.
   - **Emotion inference is prohibited in EU education** (AI Act, in force since 2 Feb 2025) — and
     voice is the modality vendors are most tempted to infer affect from. Do not ship it in EMEA,
     and strip it from any upstream SDK feature you enable.
   - **Disclosure.** AI Act Art. 50 applies from **2 Aug 2026**: a synthetic voice must be
     disclosed as synthetic. Say it in the first turn, in the learner's language, every session.
7. **Measure it as a tutor, not as a demo.** Score the *transcripts* with
   [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
   (🟢 MIT) on the client's own item bank, and track interruption rate and mean response latency
   alongside learning gain — a tutor that is pedagogically right and 1.5 s slow will still be
   abandoned.

**Licence position:** Apache-2.0 substrate + MIT reference + CC0 data + MIT mastery model — the whole
chain is permissive, so this pattern can ship as a closed client deliverable with attribution only.

**What this pattern does not solve:** there is **no granted, maintained open-source voice tutor for
an African or South Asian language** on these shelves. See `Gap 390-A`.

## Pattern W — 🆕 `p391` Qualify the district *before* the pitch (North America)

**For:** a North America K-12 engagement, at the stage before anyone has written code — choosing
which districts to approach, and pricing a pilot against a budget that actually exists. Every other
pattern here answers *what to build*; this one answers *for whom, and with whose money*.

**Why it is a pattern and not a sales note:** US school AI spending is not discretionary in the way
enterprise AI spending is. It comes from identifiable federal, state and local lines, and the
largest flexible federal line — **Title I** — is allocated on **Census child-poverty counts**, not
on enrolment. A pilot proposed without that number is priced blind, and a district with a high
poverty count and a low per-pupil spend is a different conversation from the inverse.

**Wiring:**

1. **Pull the universe.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data)
   (🟢 **MIT**, HEAD 2026-10-21) — `education_find_districts` for a state returns every local
   education agency with its **LEA id**, school count, enrolment and teacher counts. The `leaid` is
   the join key for everything below.
2. **Add the budget.** `education_district_finance` on that `leaid` returns revenue split
   **federal / state / local** and expenditure by function, with **per-pupil spending computed**.
   🔴 **The survey lags the directory by 1–2 years** — quote it as "FY-whatever per-pupil", never as
   current-year, or the first CFO in the room ends the meeting.
3. **Add the federal lever.** `education_child_poverty` returns Census **SAIPE** counts and rates of
   children 5–17 in poverty by district — the figures Title I formulas run on. High poverty rate plus
   low per-pupil spend identifies districts with *federal* money and *no* incumbent vendor: the
   cheapest pilot to land and the hardest to displace later.
4. **Add the surface.** `education_find_schools` carries **charter/magnet status, grade range and
   free/reduced-price lunch counts** per school, so the pilot can be scoped to named schools rather
   than to a district abstraction.
5. **Then pick the build.** Hand the shortlist to whichever pattern fits the client's platform —
   `Pattern F` (teacher-facing, the one the market and the regulator agree on) is the usual answer at
   this budget, `Pattern N` if they run an LMS already.

🔴 **Three things to decide before the first call, not after.** The integration is **unofficial** and
not affiliated with the upstream provider — fine for your own targeting, not something to resell as a
data product. The default path is a **hosted gateway** (`gateway.pipeworx.io`): the underlying data is
public federal data, but the **query pattern is not** — which districts a studio is sizing up is
commercially sensitive, so self-host before running this against a named client list. And a scoped
endpoint lists roughly **30 shared gateway meta-tools** alongside the four that matter, so budget the
context or connect once to the full gateway rather than to several pack endpoints.

🔵 **Regional honesty.** This is a **North America–only** instrument: it is NCES/Census data and has
no EMEA, APAC or LATAM analogue on these shelves. The equivalent question in those regions is still
answered by hand — recorded as `Gap 391-B` rather than left to look like coverage.

## Pattern X — 🆕 `p391` Keep the client's pedagogy as a separate, reviewable artefact

**For:** any tutoring engagement that will be audited, handed over, or argued about — which, under
EU AI Act high-risk obligations and most North American district procurement, is all of them. Also
the pattern for a studio that wants the *teaching* it built to outlive the *runtime* it shipped on.

**Why it is a separate pattern:** in nearly every tutor on these shelves, the pedagogy is diffused
through the application — prompt fragments, conditional branches, UI copy. That makes two things
expensive that clients ask for routinely: *show me the teaching policy* and *change the teaching
policy without a release*. [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor)
(🟢 **MIT**, HEAD 2026-10-21) is the first row here built the other way round, and it is worth copying
even where the repository itself is not used.

**The split, which is the whole point:**

| | owns | where it lives |
|---|---|---|
| [`universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, → 2026-09-24) | **what to teach next**: diagnosis, teaching moves, pacing, when a check is passed, what the next step is | its own repository, versioned independently |
| [`dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🟢 **MIT**) | **where it is kept**: learner state, the diagnosis map, structured lessons, the UI | the runtime, which contains **no teaching logic at all** |

**Wiring:**

1. **Put the pedagogy in a versioned repository of its own**, as prose and rules rather than code:
   diagnosis strategy, teaching moves, mastery criteria, escalation. This is the artefact a client
   reviews, a subject expert edits without a developer, and an auditor reads **without reading the
   application**. It is also the thing a studio can hand over at the end of an engagement.
2. **Make the runtime record decisions, never make them.** The runtime stores what the teaching layer
   decided and renders it; every pedagogical choice arrives from the policy artefact. Test this by
   grepping the runtime for teaching rules — if `if blocked, explain the prerequisite` lives in the
   application, the separation has already leaked.
3. **Put the assessment behind a pure function.** [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)
   (🟢 **MIT**, HEAD 2026-10-18) — `@intellectif/lk-core` gives schemas, a **pure scoring engine**,
   **rubric and deferred grading**, attempt plans and redaction, with no runtime dependency beyond
   Zod. Scoring that is a pure function is unit-testable by the client and readable by a regulator;
   **deferred grading keeps a human marker in the loop by construction**, which is what high-risk
   assessment obligations ask for rather than something to retrofit.
4. **Emit evidence, do not hoard it.** `lk-core`'s **xAPI builder** sends statements to the client's
   own LRS — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) where one is needed — so the learning
   record stays the client's property and the tutor stays replaceable.
5. **Launch it from the LMS over a maintained LTI edge — in the agent's own language.** 🆕 `p392`
   For a **Django** agent, [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
   (🟢 **MIT**, PyPI `django-lti` v0.10.1, HEAD **2026-10-20**): one installed app, one middleware,
   one migration, **no second service**. For a **JupyterHub**,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**).
   For **Node**, [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 **Apache-2.0**, npm v7.0.7)
   or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 **MIT**) if the deployment is
   serverless. 🔴 `p391`'s *"the edge is Node or PHP regardless of what the agent is written in"* is
   **withdrawn** — `Gap 391-A` is closed. The constraint that remains is a **licence** one: the
   best-maintained Python implementation, `openedx/xblock-lti-consumer`, is **AGPL-3.0**.

🔴 **What this pattern does not give you.** `dsh-diagnostic-tutor` is **v0.1.1 and early by its own
account**: no PDF or document ingestion, no RAG, no flashcards, no analytics, and **a route never
marks knowledge as mastered**. It also **requires DeepSeek Harness** — it is a harness extension, not
a standalone application, so an engagement that cannot adopt that harness should copy the *structure*
(steps 1–2) onto a tutor it can deploy, not adopt the repository. 🟢 Take the separation; shop for the
runtime.

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified in `p383` are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`; `p384` adds **openSIS-Classic
   → `master`**. A `main`-assuming read reports "no licence" for every one of them, and that false
   negative looks exactly like a real one.
2. **Probe more than one path — eight, not seven.** In order: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`, and 🆕 **`docs/License.txt`**
   (with `doc/LICENSE` as its variant). Verified instances where the grant is *not* at `LICENSE`:
   **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**, and 🆕 **openSIS-Classic → `docs/License.txt`** (17,286 B, stock
   GPL-2.0, *"Version 2, June 1991"*, corroborated by `"version 2 of the License"` headers in
   `index.php` and `Modules.php`). 🔵 `p384` added the eighth path because the seven-path read
   returned "ungranted" for **the most widely deployed open-source SIS in K-12** — a repository with
   a perfectly ordinary grant sitting one directory down.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
   Conversely, confirm a split grant is **absent** before assuming one:
   [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) has **no** code grant —
   `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE` and `licenses/LICENSE` all **404** — so its ODbL
   is the only grant on offer, for the tooling as well as the data.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Read the manifest and the source headers before you call anything ungranted.** 🔴 **`p383`'s
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json`, the `README`'s licence section and the
   main source file's header before rejecting a repository;
   🆕 `p385` — **but read what that section *says*, not that it *exists*.** Two failure modes, both on
   these shelves: [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) has a `## License` heading whose
   entire body is *"This project is experimental and intended for educational and research purposes"* —
   which grants **nothing**, while satisfying any check that asks "is there a licence section?";
   [h9-tect/AI-Roadmaps](https://github.com/h9-tect/AI-Roadmaps) states *"provided under the
   [MIT License](LICENSE)"* and **that `LICENSE` link 404s**. A prose assertion is weaker evidence than a
   manifest field, which is weaker than the text itself — grade them separately and never as "MIT"; a file-only read would have wrongly
   rejected three of five, including the plugin Moodle's own directory distributes.
6. **Only now treat "no licence" as a hard stop — and it is a hard stop.** Two live, functional,
   actively advertised repositories survive every check above with no grant anywhere:
   `loyaniu/moodle-mcp` (no `license` field in `pyproject.toml` either) and
   `Seechange-edu/act-ai-tutor-backend` (no manifest at all). 🔵 Both were **re-probed at the new
   eighth path in `p384` and remain ungranted.** No grant means no right to redistribute, whatever
   the README invites you to do.
7. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
   🟢 🆕 **This step was written abstractly in `p383`. `p384` gave it its first real instance** —
   `os-taxonomy`, ODbL, no code grant — and the concrete reading is now **Pattern H** below. The
   step was right in advance, which is reason to trust it on the next data artefact: education runs
   on standards, item banks and curriculum maps, so this will not be the last one.
8. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).
9. 🆕 **Confirm there is a *tree*, not just a *ref*.** `git ls-remote` on
   [projectfedena/fedena](https://github.com/projectfedena/fedena) returns two heads — and every
   content path at `master` (`README`, `README.md`, `LICENSE`, `Gemfile`, `app`) returns **404**.
   **`ls-remote` proves a ref, not a payload**, so step 1 can pass on a repository that has nothing
   in it to licence. A vendor article lists this slug as an Apache-2.0 SIS; the correct record is
   **"nothing read"** — neither granted nor ungranted. Any address census built on resolution alone
   over-counts the supply.

10. 🆕 **Read the grant at the ref you are shipping — the licence is a property of the *ref*, not of the
    repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is **AGPL-3.0** at
    `main` (`LICENSE`, 34,523 B, stock) and **MIT** at tag **`v0.1.0`** (`LICENSE`, 1,081 B,
    *"Copyright (c) 2026 Learn Shell contributors"*). Both were read first-hand in `p385`; the project
    relicensed on **2026-08-16**. 🔵 This base already knew relicensing happens —
    `snflwr-ai/snflwr.ai` went AGPL-3.0 → proprietary (`p241`), `AIHawk` went MIT for releases after a date.
    What `p385` adds is the **direction that favours the buyer**: permissive → copyleft, with the permissive
    grant **still retrievable at a tag**. 🔴 The trap in both directions is a cached audit. "We cleared that
    repo as MIT last quarter" is a statement about a ref that has moved. Record **slug + ref + licence +
    date-read**, never slug + licence — and re-read before each release, not once per engagement.
    🟡 And when you pin a tag to keep a permissive grant, say out loud what it costs: a frozen tree, no
    upstream fixes, and a maintainer who has signalled they do not want that code used on those terms.

11. 🆕 `p386` **Classify a byte-length anomaly before you judge it — "longer than stock" has two
    opposite meanings.** Step 4 says a non-stock length means the text was edited. True, and `p386`
    found the benign half of that read, which a length check alone cannot distinguish from the
    hostile one:

    | repo | bytes | the excess is | what you do |
    |---|---|---|---|
    | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2,819 (BSD-3 ≈1,500) | 🔴 **added restriction** — branding clause + CLA | walk away, or get written permission |
    | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1,200 (MIT ≈1,065) | 🟢 **added attribution** — inline notice, *"Portions … derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License"* | ship it, carry the extra notice |
    | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | 2,181 | 🟢 **two complete MIT grants concatenated** — its own plus `d2l-cli`, © 2026 Aaryan Kapoor | ship it, carry **both** notices |
    | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 11,906 (Apache-2.0 ≈11,358) | 🟢 **ASF's appended notice text** | ship it, keep `NOTICE` |

    🔵 **So the test is not "is the length stock?" but "does the delta add a condition or a
    credit?"** Added conditions are procurement stops. Added credits are NOTICE-file entries — and
    they are *obligations you inherit silently*: ship `D2L-MCP` and you owe attribution to a project
    you never chose, which no SBOM built from a licence **identifier** will tell you.
    🟡 Record the delta's content, not just the byte count.

12. 🆕 `p386` **Count grants, not addresses — and never let a count of zero reads print as
    "ungranted".** For four passes [`agents/top.md`](../agents/top.md) said *"Blackboard has nine
    servers and not one verified grant; D2L has six and the only one checked is ungranted"*, and
    concluded both platforms needed a permissive server built. `p386` probed all fifteen: **6 MIT on
    Blackboard, 6 MIT on D2L**. 🔴 The grants existed; the reads did not. A harvest column headed
    *"distinct slugs"* answers **how many addresses exist**; `LIVE-GRANTED` / `LIVE-NOGRANT` answers
    **how many were read**. When the second number is zero the honest word is **unread**, and the
    cost of the wrong word here was a false build recommendation on two platforms.
    🔵 Before any shelf states a supply gap, state which census it is quoting.

13. 🆕 `p387` **Date the artefact you are about to ship, in the registry.** A grant tells you whether
    you *may* use it; a publish date tells you whether anyone is still there. Read the package name
    from the manifest at the real default ref, then:
    `curl -s https://registry.npmjs.org/<name>` → `dist-tags.latest`, `time.created`,
    `time.<latest>`, `versions.<latest>.license`, `.repository`; or
    `curl -s https://pypi.org/pypi/<name>/json` → `info.version`, `info.license`,
    `releases[*].upload_time`. 🟢 Three usable outputs: a **second, independently published grant**
    (a manifest-only MIT becomes an MIT published to a registry); a **maintenance date** that
    survives `api.github.com` being 403; and the discovery that an address ships **no artefact at
    all**, which is a different conversation with a client than "it is old". 🔴 `p387` found a
    four-and-a-half-year-stale dependency inside a pattern on this page, a 16-month-stale server
    recommended for its tool count, and an "institution-grade" server with no release.

14. 🆕 `p387` **A manifest's package name is not proof of a publication — match the registry back to
    the slug.** [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
    declares the npm name **`class`**, and npm's `class` is an unrelated **2013** package by
    `deadlyicon`. Keyed on the name alone, a recency sweep would have printed *"MIT, published
    2013-08-15"* onto a Google Classroom row. 🟢 **The check:** accept a registry row only when its
    `repository` field — or the links in its description — point back at the same slug; otherwise
    record `NOT PUBLISHED` and say so. The same check collapses fork families for free: four
    Blackboard addresses declare `blackboard-mcp` and **one** publication exists, its `repository`
    naming `felipedias-ie`; `mdweaver/canvas-mcp` carries upstream's scoped name
    `@r-huijts/canvas-mcp`. **Count the artefact, not the slug.**

11. 🆕 `p388` **If the repository is unreadable, read the *artefact*. The manifest is a claim; the
    tarball is the evidence.** `git ls-remote` distinguishes two states a 404 conflates: a
    **credentials prompt means the repository exists and is closed**, not absent. For such a package
    — and **6 of 32 addresses probed in `p388` are in this state while publishing to npm
    normally** — the published tarball is still readable and is **the licence that actually ships**:
    ```
    curl -s https://registry.npmjs.org/<pkg> | jq -r '.versions[.["dist-tags"].latest].dist.tarball'
    curl -s <tarball> | tar -tz | grep -i -E 'license|copying'      # is a grant shipped at all?
    ```
    🔴 **This is how `p388` established that a major publisher's tutoring SDK is ungranted.**
    `@santillana-ai/typescript-tutor-sdk` — **115 published versions** — has **no `license` field in
    `package.json`**, **no licence file anywhere in its 896,006-byte tarball**, and **no `repository`
    field at all**; its sibling scaffolder claims `"license": "MIT"` in the manifest while shipping
    **no licence file either**. Neither the repo (private) nor the badge (absent) could have settled
    it; the artefact did.
    🔵 **Three sub-rules:**
    **(a)** A manifest reading **`"SEE LICENSE IN LICENSE"` that points into an unreadable
    repository is not a grant** — it is a circular reference
    — [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) is the worked example, and 🆕 `p390` re-confirmed its repository is **still unreadable**, so the circle is still closed.
    **(b)** Steps 1–10 clear a repository **by subtree**; when there is no readable subtree, *this*
    step is the only one available, and it can only ever yield 🟡 manifest-only or 🔴 ungranted —
    **never a clean clearance**.
    **(c)** 🔴 Check **which** package in a scope carries the grant. Here the MIT claim sits on the
    *scaffolder* and the **dependency a client's code would actually import carries nothing**. Read
    the licence of the package you will `import`, not of the one you will `npx` once.

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.

🟢 🆕 `p389` **Step 11, and it makes steps 1–10 one command.** A **blobless shallow clone** does the
whole gate in ~1.2 s, from the payload, with no API and no credentials:

```bash
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the real default ref (step 1)
git -C r ls-tree --name-only HEAD     # is there a LICENSE at all, and where (steps 2-3)
git -C r show HEAD:LICENSE            # the grant text itself (step 4)
git -C r show HEAD:package.json       # the manifest that must agree with it (step 5)
git -C r log -1 --format='%H %cI'     # ← NEW: who still works on this, and when
```

🔵 **Why the last line belongs in a procurement gate and not just in a research note.** The gate has
only ever answered *may we use this*. It now also answers *will we be alone on it* — and the two
produce different estimates. **A permissive grant plus an eight-month-old HEAD is a vendoring
decision with a maintenance line**, which is precisely the call this base made for `pybryt` after
reading a *registry* date; the clone reads it for any repository, published package or not. 🟡 Read
the date against the artefact: a release branch can trail a default ref
([instructure/canvas-lms](https://github.com/instructure/canvas-lms), `master` **175 days** behind its
moving `stable/*` branches), and a finished specification is not decaying. 🔴 And the limit, **re-measured at `p392` and narrower than it was**: the `git` channel itself gives no
stars, forks or releases — but `github.com/{owner}/{repo}` answers **200 via WebFetch** (403 via
curl), so **stars, forks, commit counts and release tags are readable again**, and `api.github.com`
answers **200** while refusing **by scope** rather than outright (`/search/*` is closed by design).
**Discovery** remains web search and package registries; **verification** is first-hand; and
**popularity** is back, per tool. See [`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

## Pattern Y — 🆕 `p392` Exam integrity the client can defend, without becoming a high-risk deployer

**For:** a client — a university, a certification body, a bootcamp — who asks for proctoring, and
whose actual requirement is *"we must be able to defend a result if it is challenged"*.

🔴 **Read this first, because it is the whole pattern.** For four passes these shelves said proctoring
had *"no credible permissive open-source option"*. That was wrong (`Gap 391-C`, closed this pass). But
the granted supply covers **deterministic lockdown and event telemetry**, while the **inference**
layer — identity matching, gaze, multi-face, behavioural scoring — is absent, roadmapped, or the
proprietary service an AGPL workflow brokers (`Trend 20`). 🟢 **That asymmetry is a gift, not a
shortfall:** the half you can build permissively is the half that is explainable in an appeal, and the
half you cannot is the half that makes the client a **deployer of an Annex III high-risk system** with
standalone obligations from **2 Dec 2027**.

**Wiring:**
1. **Signals in the browser, permissively.**
   [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
   manifest agrees, HEAD **2026-09-28**, npm v0.5.1): tab-switch, right-click, DevTools shortcuts,
   clipboard events, camera state, **faces**, audio loudness, and **virtual-camera / loopback /
   screen-share detection**. Face detection is `@vladmandic/face-api` 1.7.15 on TF.js, **in the
   browser**. 🔴 **Two things to change before a pilot:** self-host the model weights (it loads
   face-api **and** its weights from jsDelivr by default — a supply-chain and data-residency defect in
   any EU or public-sector deployment, and the README documents the self-hosted path), and read all
   46 commits — this is **1 ★ and one maintainer**, so vendor it and own it.
   🟡 *Alternative when you need lockdown rather than detection:*
   [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) — 398 commits,
   HEAD **2026-10-13** — blocks copy/paste/cut, right-click, selection and shortcuts and reports eight
   named violation types. 🔴 Its grant is a **CONFLICT** (Apache-2.0 in the payload, `ISC` in
   `package.json` and on npm): both readings are permissive, so it is usable, but get the two files
   reconciled before a client depends on it. 🔴 And its AI features are marked *"(To be Done)"* — do
   not quote them.
2. **Keep the record, not the video.** Both components POST to an endpoint **you** build. Store the
   **event trail** (what happened, when, on which element) and resist storing webcam frames: snapshots
   are off by default in `proctoring.js`, and leaving them off is a defensible default, not a
   limitation. Audio is analysed in memory and discarded — say so in the privacy notice.
3. **Put the decision in a human's hands, in the workflow.** The attempt/review state machine already
   exists: [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) (🔴 **AGPL-3.0**,
   253 releases, `master` HEAD **2026-10-22** — re-read first-hand this pass) if the client runs Open edX — brokered over the platform boundary, not forked — or
   [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)'s (🟢 **MIT**)
   **deferred grading** when you are building the assessment surface yourself. **No automatic
   flagging decides anything**; a flagged attempt opens a review task.
4. **Launch and report over LTI 1.3, in the agent's own language.**
   [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT) for a
   Django service, [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT) for a
   serverless one — so the integrity result lands in the gradebook of record as an **LTI AGS score**
   with a reviewable note attached, rather than in a side system nobody audits.
5. **Write the Art. 50 and Annex III position down before you build.** Students are told, in advance,
   which signals are collected and what a flag does; the review path and the appeal path are named; the
   retention period is set. 🟢 This is cheap here **because** step 1 does no inference — the honest
   disclosure is short.

**Effort:** 4–6 weeks for steps 1–4 on an existing assessment surface; step 5 is a day of writing and
the thing that gets the deployment approved.

🔴 **What this pattern refuses to build, and tell the client why:** automated cheating *verdicts*,
identity verification from a webcam, and gaze or emotion scoring. The permissive supply does not have
them, the obligations land on the client rather than on us, and a flag that cannot be explained in an
appeal is a liability dressed as a feature.

## Pattern Z — 🆕 `p392` Size and price a Brazilian education engagement before the first meeting

**For:** a LATAM pitch — a municipal or state network, a private group — where the honest answer to
*"how big is this?"* has until now been *"we will need to scope it."* `Pattern W` does this for a US
district; this is the Brazilian instrument, and it is the closure of `Gap 391-B` for one country.

**Wiring:**
1. **Install the access layer.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil)
   (🟡 **MIT — code only**, 1,072 B; PyPI **`mcp-brasil` v0.14.0**, 18 releases; HEAD **2026-08-18**):
   an MCP server over **70 Brazilian public sources**, 533 tools, **66 of them keyless**, with large
   datasets cached locally and queried through embedded **DuckDB**. No procurement, no API key, no
   vendor.
2. **Query the school census.** `censo_escolar` (INEP) is the per-school base: network, enrolment,
   infrastructure. Build the target list — how many schools, which bands, which municipalities — and
   put a **per-school number** in the proposal instead of a range. `enem` adds outcome context where
   the engagement is secondary-level.
3. **Match it to the platform the client already runs.**
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🔴 GPL-2.0-or-later, real default
   ref **`2.12`**) is the municipal SIS a Brazilian engagement actually meets;
   [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) for Portuguese/Spanish
   course delivery. Integrate **over the boundary** — web services or LTI 1.3 — so the copyleft stays
   on their side of it (`Pattern A`).
4. **Put the agent in Portuguese, from the shelf.** Tier 4 of [`agents/top.md`](../agents/top.md)
   holds the LATAM-native, Portuguese-first granted agents; `Pattern O` is the full regional build.
5. 🔴 **State the three limits in the proposal, in writing.** The bundled INEP data is a **2023
   snapshot** — currency is the risk, not the licence; the project's own `SOURCES.md` asks you to
   **validate a sample to confirm anonymisation**; and `mcp-brasil` is **not an official government
   service**, so a ministry-facing document cites **INEP** as the source and this as the access path.
   🟢 Its LGPD handling is genuinely documented: education is graded *RISCO ALTO*, the 2022 withdrawal
   and 2024 anonymised resumption are recorded, and `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate
   columns only — no `NU_INSCRICAO`, name or CPF.

**Effort:** 2–3 days to a priced, school-level proposal; the integration in step 3 is the engagement.

🔴 **And know what you are walking into.** `Trend 21`: five live 2026 LATAM tenders, **none asking for
open source** — they buy subscriptions and licences. This pattern makes the *total-cost* argument
possible; it does not make the procurement ask for it.

## Pattern AA — 🆕 `p393` The LATAM SME delivery stack, entirely permissive, with billing already in it

**When to reach for this.** A LATAM client — a training provider, a professional body, a private
school group, a corporate academy — needs to **deliver and sell courses in Spanish** and wants to own
closed extensions. Every incumbent regional base is copyleft: **Chamilo** GPL-3.0, **i-educar**
GPL-2.0-or-later, **Moodle** GPL-3.0, **frappe/lms** AGPL-3.0. Until `p393` this shelf had to answer
either *"take the GPL"* or *"build a platform."*

🟢 **The base, and it is new to these shelves:**
[`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) — **Apache-2.0**, payload read
first-hand (10,915 B, `sha256`₁₆ `a9c4042d767d`, © 2021–2024 BMO Moreno Berroteran Ortiz Soluciones,
**S.A., Nicaragua**), `main` · `53dcb60`, HEAD **2026-08-31 — 52 d**, **676 files, 505 commits, 57
releases**, PyPI `now-lms` v2.0.4. Flask/Python; courses, delivery, certificates and **monetisation**
in the box.

### The stack

| layer | component | grant | why this one |
|---|---|---|---|
| **Platform** | [`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | The only Spanish-language LMS on these shelves you can fork, extend and **ship closed**. Flask — a studio reads the whole thing in a day. |
| **Tutor / agent** | the LATAM-native agent tier on [`agents/top.md`](../agents/top.md) | 🟢 MIT | Three granted regional options; one ships as an Open edX plugin, so prefer the standalone ones here. |
| **Interop edge** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) 🟢 MIT, + [`…/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) 🟢 MIT | 🟢 MIT | 🔴 **Django, and `now-lms` is Flask** — see the honest caveat below. Needed only when the client must appear **inside someone else's LMS**. |
| **Autograding** (technical courses) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) 🟢 BSD-3 (**161 ★**, 197 releases) + [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) 🟢 MIT | 🟢 permissive | Grading and submission halves respectively. Both Python, both beside the platform's own runtime. |
| **Assessment import** | [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) | 🟡 **LGPL-3.0** | Ingest existing question banks as QTI. 🟡 **Link it, do not fork it** — LGPL permits the first and not the second. |
| **Public-data sizing** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 MIT (code only) | For a **Brazilian** engagement, size the market from INEP `censo_escolar` before the first meeting — `Pattern Z`. |

### Wiring it

1. **Fork `now-lms`, pin the Apache-2.0 payload into the delivery record.** Record bytes and
   `sha256`, per `Pattern L` step 1. The appendix is **filled in**, not narrowed — that is the benign
   non-stock case, and worth noting in the record so a later reviewer does not re-raise it.
2. **Keep the agent out of the platform process.** The tutor talks to `now-lms` over HTTP and holds
   its own store. 🔵 This is `Pattern A`'s rule and it survives here for a different reason: not
   copyleft containment, but so the platform fork stays rebaseable onto a 57-release upstream.
3. **Add autograding only for the courses that need it.** `otter-grader` runs containerised; invoke
   it as a job, not in the request path.
4. **Decide the interop edge explicitly, and this is where the caveat bites** (below).
5. **Bill through the platform's own monetisation**, which is the reason to pick this base over
   `academico`. Verify it against the client's local payment rails before promising it — Nicaraguan
   defaults are not Brazilian or Mexican ones.

### 🔴 The caveats, because this base's own history says to write them next to the recipe

- 🔴 **21 ★, and that is the real risk, not the licence.** One company, 505 commits, no multi-tenancy
  claim. **Fork it and plan to own it** — budget maintenance as if upstream may stop. Do not put a
  ministry on it; `Pattern O` and Chamilo remain the public-sector answer.
- 🔴 **The LTI edge is Django and `now-lms` is Flask.** All five Python LTI implementations
  (`p393`, refuting `Gap 391-A` a second time) are **Django** apps or JupyterHub authenticators. If
  the client must launch from a third-party LMS, the edge is a **separate Django service** beside the
  Flask app. 🔵 Note what this is and is not: `p391` published *"the interop edge must be a separate
  runtime"* as a **language** claim and was wrong; here it is a **framework** claim about one specific
  pairing, and it is a deployment line to cost, not an architecture verdict.
- 🟡 **Three of the four non-platform components are copyleft or weak-copyleft** once assessment import
  enters. Keep QTI conversion (`Citolab`, GPL-3.0) and packaging (LGPL-3.0) as **arm's-length tools**
  invoked by a pipeline; nothing copyleft links into the delivered fork.
- 🔴 **Do not reach for the `timeback-*` OneRoster/QTI clients**, however well they fit on paper:
  147 releases, MIT **declared**, and a **source repository that does not resolve** (`Gap 393-B`,
  `Trend 23`). You cannot warrant a grant you cannot read.

🟢 **What the client gets that they cannot buy:** a Spanish-language delivery platform they own
outright, with billing, autograding and an AI tutor — assembled from **four permissive grants read at
the payload**, on a base whose entire source a studio can audit in an afternoon.

## Pattern AB — 🆕 `p394` The statistics and data-science course, graded automatically, including where the network is not

**When to reach for this.** The client teaches **R** — statistics, biostatistics, econometrics,
data science, any quantitative methods course — and wants automated feedback at cohort scale.
🔵 `p393` flagged that this base's most-adopted *maintained* autograder **grades R** while the shelves held no R
components at all; this pattern is the hole closed. 🟢 **And its last step is the only offline
assessment loop in this entire base**, which is what makes it worth reaching for in LATAM and APAC
rather than only in a well-connected university.

**The components, and the licence boundary runs between steps 3 and 5.**

| # | step | component | grant |
|---|---|---|---|
| 1 | Serve identical compute to the cohort | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause |
| 2 | Author the tutorial the student works inside | [`rstudio/learnr`](https://github.com/rstudio/learnr) | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* |
| 3 | Grade the exercise and answer back | [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | 🟢 **MIT** *(1,078 B, `48c18e68ffed`)* |
| 4 | Batch-autograde submitted scripts and notebooks | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) + [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3-Clause both |
| 5 | **Generate the exam** in the LMS's own format | [`cran/exams`](https://github.com/cran/exams) | 🔴 **GPL-2 \| GPL-3 — service boundary** |
| 6 | Calibrate the items after the fact | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) · [`cran/catR`](https://github.com/cran/catR) · [`ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) | 🔴 **GPL — service boundary** |
| 7 | Carry the generated exam into the LMS | QTI 2.1 / Moodle XML, per `p393`'s **Tier 8** standards layer | per that tier |

**Wiring it.**

1. **Steps 1–4 are your product and they are permissive.** `learnr` renders the tutorial, `gradethis`
   supplies the per-exercise predicate (`grade_this_code()` against a model solution for mechanical
   exercises; `grade_this()` where you must inspect the student's actual object), `ottr` handles
   batch submission. 🟢 A closed-source product may embed all four.
2. **Steps 5–6 run as a separate service, invoked over a process boundary.** 🔴 `cran/exams`, `mirt`,
   `catR` and `ShinyItemAnalysis` are **GPL**; call them as a job — stdin/stdout, a queue, an HTTP
   worker — and never link them into the product. 🔵 Same discipline `Pattern A` and `Pattern O` apply
   to Moodle and Open edX, applied here for the same reason.
3. **Record the disjunctive choice once, in writing.** `cran/exams` is **GPL-2 *or* GPL-3 at the
   licensee's election**. Pick a rung, write down which and why, and keep it with the engagement's
   licence register — downstream compatibility differs between the two, and "GPL" alone is not an
   answer a client's counsel will accept.
4. **Step 5's output is the integration point, and it is wide.** `exams2qti21()`, `exams2moodle()`,
   `exams2canvas()`, `exams2blackboard()`, `exams2ilias()`, `exams2openolat()` — verified from the
   `R/` source filenames in the clone. 🟢 So one authored item bank feeds **whichever** LMS the client
   already runs, which is the opposite of the usual per-platform rewrite.
5. 🟢 **Then NOPS, which is the step nothing else here can do.** `cran/exams` emits a standardised PDF
   that is **printed, sat on paper, scanned, and marked automatically**. 🔵 Use it where the network
   is unreliable, where invigilation must be physical, or where the institution needs a **paper audit
   trail** it can produce years later. 🔴 It is also the honest answer to the finding on
   [`intel/market.md`](../intel/market.md) that **assessment is the lowest-adoption AI use case among
   LATAM faculty**: if the reluctance is about connectivity, invigilation and auditability rather than
   about AI, NOPS addresses the actual objection instead of arguing with it.

🔴 **Two things this pattern does not claim.** **(1)** `ottr` has **3 ★** — the adoption sits on the
Python parent, so you are deploying a lightly-used component and should budget to read its source.
**(2)** `learnr`'s HEAD is **343 days** old. That reads as stable rather than abandoned — the movement
is in `gradethis` (**126 d**) — but it is a dependency whose maintenance a studio should check before
year three, not a vendor commitment.

🔴 **And a provenance warning that will bite at review.** `cran/exams`, `mirt`, `catR`, `TAM` and
`ShinyItemAnalysis` carry **no licence file at any path** — their grant is the `License:` field in
`DESCRIPTION`, which is what CRAN enforces. 🔵 **GitHub's sidebar therefore shows no licence for any of
them**, so a reviewer checking the UI will report five granted GPL packages as unlicensed. Put the
`DESCRIPTION` line in the licence register, not a screenshot of the repository page (`Gap 394-B`).

## Pattern AC — 🆕 `p394` Give teachers an assistant builder instead of building their assistants (EMEA, Moodle)

**When to reach for this.** The client is a **university or school group already running Moodle**,
their teachers keep asking for subject-specific AI assistants, and a studio cannot profitably build
one assistant per course. 🟢 **LAMB inverts the unit of delivery**: the studio delivers the *builder*
and governs it; teachers author the assistants themselves, with no code.

**The components.**

| # | step | component | grant |
|---|---|---|---|
| 1 | The assistant builder and manager | [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb) | 🔴 **GPL-3.0** *(35,349 B, `17fe6d0ffa96`)* |
| 2 | Publish each assistant into the LMS | **LTI external tool** — LAMB's own publishing path | 1EdTech LTI |
| 3 | Graded assignments against an assistant | [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) | 🔴 **GPL** |
| 4 | The LMS itself | Moodle | 🔴 GPL-3 |
| 5 | Models, where sovereignty is required | open-weights served locally — LAMB states it shares no user information with model providers and can run on *"open source and open weights models running on your compute"* | per model |

**Wiring it.**

1. **The whole stack is copyleft and that is fine here**, because nothing in it is a product a studio
   resells. 🟢 Moodle is GPL-3, LAMB is GPL-3, LAMBA is GPL — the engagement is **deployment,
   integration, governance and training**, not licensing. 🔵 This is the one shape where the copyleft
   frontier on [`repos/foundations.md`](../repos/foundations.md) costs nothing.
2. **Step 2 is why this is a pattern and not a tool.** Assistants arrive in Moodle as **LTI external
   tools**, so the LMS stays untouched: no plugin to maintain against Moodle's upgrade cycle, no
   fork, and the assistant can be withdrawn without a migration. 🟢 Same architecture `Pattern A`
   prescribes for every agent going into a copyleft LMS, except here the upstream project already
   did it.
3. **Read the tree before you read the badge.** 🔴 LAMB carries **three grants**: root GPL-3,
   `lamb-kb-server-stable/` with its own stock GPL payload, and a **vendored `open-webui/` under
   verbatim BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). `Pattern L` is the procedure; this repository is
   why `Pattern L` exists. 🔵 Check the vendored Open WebUI copy's licence **at the pin you deploy** —
   upstream Open WebUI added branding restrictions in later releases, and the copy vendored here is
   the plain BSD-3 one.
4. **Sovereignty is a configuration, not a port.** Step 5 is the reason to shortlist LAMB for an
   EMEA engagement at all: it is designed to run against locally-served open-weights models and
   states that no user information reaches a model provider. 🟢 That answers the EU AI Act data
   questions in the architecture rather than in a DPA annex.
5. 🔴 **Size it as a high-risk deployment the moment it touches grading.** `lamba` grades assignments.
   Under the EU AI Act, systems that **grade learners, assign them to programmes or influence access
   to qualifications** are **high-risk and need a conformity assessment before deployment** (see
   *EMEA* on [`intel/market.md`](../intel/market.md)). 🟢 So: ship step 2 (assistants that tutor and
   explain) first and get it in front of teachers; treat step 3 (assistants that grade) as a
   **separate, later, assessed workstream**. Selling them as one phase is how an integration project
   becomes a compliance project mid-delivery.

🔴 **The maturity caveat, stated here and not only in the evidence file.** LAMB's own Moodle.org thread
(Feb 2026) describes it as *"at a very beta stage"* with *"a few universities running pilots"*, and the
repository is **one squashed commit** with HEAD **2 d**. 🟢 It is university-authored, peer-reviewed in
*Computer Standards & Interfaces*, and visibly active — **a strong pilot base**. 🔴 It is **not** a
ministry-scale platform, there is no multi-tenancy claim this base has verified, and an engagement
that needs one should read `Pattern O`'s tenancy discussion first. 🔵 Propose it as a pilot with a
named exit, and say so to the client in the first meeting rather than the third.
