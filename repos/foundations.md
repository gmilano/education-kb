---
industry: education
region: Global
updated: 2026-10-22
---

## 🟡 2026-10-22 · `p376` — one row in the **credentialing / interop** tier, published WITH its staleness, and one withheld for having no grant at all

**Evidence:** [`credentialing-layer-grade`](../evidence/credentialing-layer-grade.2026-10-22-p376.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-22-p376.tsv)

| Repo | Licence | Grant read at | HEAD | Tier | Why foundational — and the caveat |
|---|---|---|---|---|---|
| [`digitalcredentials/lti-issuer`](https://github.com/digitalcredentials/lti-issuer) | **MIT** (1 076 B, sha256₁₂ `5ea29d532cac`, **untitled** payload) | `master/LICENSE` | `75a3c5d` · 🔴 **2024-04-22** | credentialing / interop | 🟢 the only **permissively granted** code this base has located that joins **LTI** to **W3C Verifiable Credentials** — an LTI producer that issues a VC, which is the exact seam `p371` named as unshelved. 🔴 **Read it as a REFERENCE, not a dependency:** HEAD has not moved in two and a half years |

🟢 **Verified first-hand this pass.** `git ls-remote --symref` gives `ref: refs/heads/master`,
HEAD `75a3c5d8b5470e1101c6559b8bb981e53e18c5d4`; the grant payload was read at **1 076 B** and
digested from a **file**, never through command substitution — `p178`'s one-byte channel defect.
🔴 **No star count** — `api.github.com` and `github.com` HTML are both `403` here.

### 🔵 The grade, and the two instruments that answer differently about it

🟡 **The payload is the MIT body verbatim and carries NO TITLE.** It opens on
`Copyright 2020 Center for 21st Century Universities` — note the holder is **Georgia Tech's
C21U**, not MIT the institution, despite the `digitalcredentials` org being the **MIT Digital
Credentials Consortium**. A successor reading "MIT" in both senses on one row should not
conflate them.

🔵 **Two of this base's own instruments give different answers, and they are NOT in conflict:**

| Instrument | Answer | What it was asked |
|---|---|---|
| `p228-shelf-gate` `classify` — **the grade of record for a shelf cell** | 🟢 **`MIT`**, "title line @53" | *which family is this grant?* |
| `p312-template-identity` `identify` | `UNKNOWN-TEMPLATE`, form `FILL-IN`/`HOLDER`, normalised 1 025 | *is this payload one of the templates I have PINNED?* |

🟢 **`p312` is documented to behave exactly this way** — *"An unrecognised payload returns
`UNKNOWN-TEMPLATE`, never a nearest match"* — and its registry is built from its own 17 pinned
fixtures. 🔴 **So `UNKNOWN-TEMPLATE` is not evidence of a bespoke or irregular grant**, and a
successor must not read it as one: run `p312`'s identifier over `p314`'s committed fixtures and
it returns `UNKNOWN-TEMPLATE` for **10 of 11** payloads that `p314` committed *with declared
families*, including three MIT ones. 🔵 That is the registry's coverage, not a defect in those
payloads — but it does mean the two instruments must be quoted for the question each answers.
**`ACTION p376-C`**: pin this payload as a `p312` fixture, so the untitled-MIT template the
credentialing tier actually ships becomes identifiable rather than merely classifiable.

### 🔴 Withheld, deliberately: `open-ent/openbadges`

🔴 **No grant on any channel** — ladder, enumerated tree, `pom.xml`, README — so it is **not
usable for client work** and gets no foundational row. 🟢 It is maintained (`a978850`,
**2026-10-16**) and is the most complete Open Badges 3.0 / VC-JWT issuer this pass saw; the
reasoning is in `agents/trending.md` and its design constraints are built into `Pattern 16`.
**`Gap 501`.**

### 🔵 What the tier looks like once the maintenance axis is measured

🟢 **Permissive AND maintained, both already carried:** [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
(Apache-2.0, `2026-10-13`) and [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens)
(MIT, `2026-10-05`).
🔴 **Maintained but copyleft:** `Schroedinger-Hat/certo` and `edubadges/edubadges-server` (both
AGPL-3.0), `luisgf/openbadgeslib` (LGPL-3.0).
🔴 **Permissive but stale:** this pass's own new row, and `w3c-ccg/edu_occ_verifiable_credentials`
(HEAD **2020-12-28**, and a reports repository rather than software).

🟢 **The build consequence, which is the point of the tier:** a studio can assemble a
standards-conformant credential path **entirely from permissive, maintained code** —
`Cvmcosta/ltijs` for the LTI 1.3 boundary and `credential-lens` for offline verification — but
there is **no permissive, maintained ISSUER**. The issuer is the piece that must be written,
and `Pattern 16` is the recipe for writing it against a specification rather than forking an
AGPL one.

## 🟢 2026-10-22 · `p375` — one foundational row added, in the **curriculum** tier, grant read first-hand

| Repo | Licence | Grant read at | HEAD | Tier | Why foundational |
|---|---|---|---|---|---|
| [`mlabonne/llm-course`](https://github.com/mlabonne/llm-course) | Apache-2.0 (11 357 B, sha256₁₂ `c71d239df917`) | `main/LICENSE` | `7abd96e` | curriculum / practitioner upskilling | 🟢 the most-adopted open LLM curriculum in this window's legs, and **permissively granted**, so a studio can fork it into client enablement material rather than linking out to it |

🟢 **Verified this pass, both channels, first-hand:** `git ls-remote --symref` gives
`ref: refs/heads/main`, HEAD `7abd96e8284bfae232048fdb77b52397a2114847`; the grant was read from
its payload at **11 357 B**, the canonical Apache-2.0 body, byte-identical on `main` and
`master`. 🔴 **No star count** — `api.github.com` and `github.com` HTML are both `403` here.

🔵 **Why it belongs on this shelf.** `p371` named **curriculum and credentialing** as this
base's unshelved layer. The LMS, knowledge-tracing and tutoring tiers below are well covered;
the layer that turns a studio's own people into deliverers was represented only by material
this base already carried and never graded as foundational.

🔴 **Zero other foundational rows this pass, with the reason.** The vertical-platform leg
returned one vendor's own multilingual pages plus a listicle; every platform they name
(Open edX, Moodle, Chamilo, Sakai, ILIAS) is **already carried**, and the one new name —
**OpenEduCat** — has **no GitHub address in any source retrieved**, so none is shelved.
`verticals/solutions.md` carries it with its licence channel and `Gap 500` carries the address.

## 🟢 🆕 `p374`: the human-grading system of record this shelf had no row for — **MIT**, and read first-hand

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p374.tsv) ·
[`gap490-product-name`](../evidence/gap490-product-name.2026-10-22-p374.tsv)

| Repo | Licence | Grant read at | HEAD | Why it is foundational here |
|---|---|---|---|---|
| [`MarkUsProject/Markus`](https://github.com/MarkUsProject/Markus) | **MIT** (1 076 B, *"Copyright (c) 2008-2022 by the authors"*) | `master/LICENSE` | `86395e8` · **2026-10-21** | 🟢 A **human** grading application (Ruby on Rails) for code and written assignments, maintained by a university project. It is the piece `Pattern 14` needs as the **system of record for marks**, so that an AI component can return comments while a human holds the grade. |

🔵 **Found as a by-product of `Gap 490`, not by a discovery leg** — the search for `IBM MARK`
returned MarkUs as its *"closest match"*, which it is not. 🟢 The mis-match was worth more than
the match would have been: this shelf had assessment-generation rows and no row for the place a
mark is actually recorded.

🔴 **Do not merge it with [`ibm-skills-network/mark`](https://github.com/ibm-skills-network/mark)**
(Apache-2.0, AI assessment, IBM Skills Network). Two unrelated tools, one near-identical name —
the collision is declared on `agents/top.md` and in the `Gap 490` evidence.
🔵 `benjaminvialle/Markus` is a **distinct fork** (HEAD `664ca8a` ≠ `86395e8`), not a casing.

🔴 **No star counts this pass** — `api.github.com` and `github.com` HTML both **403**.
## 🔴 🆕 `p372`: the learning-record and credentialing rows on this shelf are LIVE — and the REFERENCE IMPLEMENTATIONS behind the standards they speak are not

**Evidence:** [`successor-probe`](../evidence/successor-probe.2026-10-21-p372.tsv) ·
[`dead-citation-reprobe`](../evidence/dead-citation-reprobe.2026-10-21-p372.tsv)

🔵 All probes **2026-10-21**, first-hand `git ls-remote`. 🟢 Artefacts are dated by MEASUREMENT.

🟢 **The good news first, because it bounds the finding.** Nine learning-record and
standards-layer rows carried on this shelf and on `repos/foundations.md` were probed
first-hand and **all nine are live**: `apereo-learning-analytics-initiative/sakaixapi-provider`
(20 refs), `adlnet/xAPI-Spec` (904), `adlnet/SCORM-to-xAPI-Wrapper` (13),
`LearningLocker/learninglocker` (1 385), `openfun/ralph` (589), `jeffyding/OpenLRW` (2),
`digital-learning-gmbh/educa-lrs` (15), `pawelkn/xapi-rs` (17), `peterszombati/xapi-node` (277).
🔵 **And the apereo ORGANISATION is not defunct** — only `apereo/opencast` moved, to
`opencast/opencast`. 🟢 `gate-dead-citation`'s `I2` separately proves that **none** of the 34
absent addresses `p372` adjudicated is a linked row on any live shelf.

🔴 **What IS missing is one layer down: the runnable reference implementations of the
standards these rows speak.** Probed first-hand this pass, every candidate address:

| Standard | Reference implementation probed | Result | Maintained sibling |
|---|---|---|---|
| **Caliper Analytics** | `caliper-java`, `caliper-js`, `caliper-php`, `caliper-python` across `1EdTech/` and `imsglobal/` | 🔴 **absent — ALL FOUR bindings, BOTH org spellings** | 🟢 [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) (400 refs) |
| **Open Badges** | `concentricsky/badgr-server`, `1EdTech/badgr-server` | 🔴 **absent at both** | 🟢 [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) (182 refs) |
| **xAPI** | `yetanalytics/lrspipe`, `yetanalytics/lrs-pipe` | 🔴 **absent at both** | 🟢 [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (764 refs) |
| **LTI 1.3** | `UOC/java-lti-1.3-provider` | 🔴 absent | 🟢 [`UOC/java-lti-1.3`](https://github.com/UOC/java-lti-1.3) (38), [`…-provider-example`](https://github.com/UOC/java-lti-1.3-provider-example) (17) |

🔴 **Ten of ten candidate reference-implementation addresses are unretrievable, while every
one of those standards has a maintained spec or validator sibling** — enumerated so the figure
is checkable: `1EdTech/caliper-java`, `imsglobal/caliper-java`, `1EdTech/caliper-js`, `1edtech/caliper-php`, `imsglobal/caliper-python`, `concentricsky/badgr-server`, `1EdTech/badgr-server`, `yetanalytics/lrspipe`, `yetanalytics/lrs-pipe`, `UOC/java-lti-1.3-provider`. 🟢 **The engagement
consequence is a budgeting one:** for education's interoperability layer, cost
**implement-from-spec**, not **adopt-a-library** — and treat *"there is a reference
implementation"* in a 2026 roundup as a claim to probe. 🔵 This is the operational edge of
`p371`'s finding that credentialing is the layer these shelves were missing: the layer is thin
everywhere, not just here, and the reason is that its runnable starting points are gone.

🟡 **A cross-current recorded rather than resolved.** A 2026 edtech trends roundup rates
skills-based **microcredentials as growing** while listing **blockchain credentialing among
the trends fading fast** — which cuts against the Blockcerts-shaped part of the credentialing
supply `p371` recovered. 🔴 One secondary source against first-hand payload evidence: recorded
as a tension, not as a refutation. See `intel/trends.md` **Trend E**.


## Start here — what to build the platform on

🟢 **This is the answer this file exists to give.** The tiers below it are the full
graded inventory; everything above `## Learning platforms (LMS / VLE)` other than this
section is the audit trail of how those grants were read.

🔴 **The one fact that drives every platform choice in education: the big LMSs are
copyleft.** Open edX and Canvas are AGPL-3.0, Moodle and Chamilo GPL-3.0. That is not a
blocker — it decides *where your code lives*, not whether you can do the work. Reach them
from outside (LTI 1.3 / MCP / web services) and your deliverable stays yours; fork them or
write an in-process plugin and it does not.

| Layer | Permissive pick | Licence | ★ | Copyleft incumbent you will actually meet |
| --- | --- | --- | ---: | --- |
| LMS / VLE | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | — | Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas (AGPL-3.0) |
| Offline-first LMS | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 159 | — |
| LTI 1.3 tool (Node) | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | — |
| LTI 1.3 tool (Python) | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | 138 | — |
| SCORM runtime | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 356 | — |
| LTI tool host | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | Apache-2.0 | 376 | — |

🔵 **The rest of the file by tier:** learning platforms · national school portals (ENT) ·
interoperability (LTI/SCORM/xAPI/Caliper) · learning records and rostering ·
psychometrics · assessment, integrity and accessibility · code execution and autograding ·
deployment components · content authoring · SIS/ERP/credentials · curriculum corpora ·
research corpora. Each row carries the path its grant was read at, because in education
the grant is often *not* in `LICENSE` — Moodle keeps it in `COPYING.txt`, Frappe LMS in
lower-case `license.txt`.


# Education — foundational repos

**Pass 367 · 2026-10-21.** 🔴 **Every "absent from N addresses" figure this base has ever
published was tested against a corpus missing 496 live repositories. `p367` built the
second channel `ACTION ZZ-bv` prescribed, and the corpus-level error is 16.3% — twice the
8.2% `p366` measured on its own population.**

🔵 **Why the two numbers differ, stated so neither is quoted as the other.** `p366` asked a
*lookup* question — of 330 companions already known to be absent, how many does this base
hold as a bare slug? Answer **8.2%**. `p367` asks the *corpus* question — how many live
repositories does this base hold that the URL channel cannot see at all? Answer **496**,
against 2 542 URL-channel live addresses:

| The true live corpus | Count | Share |
|---|---:|---:|
| channel **U** live (`p348`'s URL form) | **2 542** | 83.7% |
| 🔴 channel **B** net-new live — invisible to every instrument here | **496** | **16.3%** |
| **true live corpus** | **3 038** | 100% |

🟢 **The 496 is a NET figure and the netting is first-hand.** Channel B returned **522**
live addresses; **26** of them share a `HEAD` sha with a channel-U address and are therefore
not new repositories. Those 26 were then split by a sharper test than `p366` had:

| Identity class | Count | What it means |
|---|---:|---|
| 🟡 `SAME-REF-SET` — identical fingerprint over **all** refs | **23** | one repository at two addresses, or a fork nobody has pushed to |
| 🟡 `SAME-HEAD-ONLY` — same `HEAD`, ref sets differ | **3** | a fork that has diverged somewhere other than `HEAD` |

🔴 **`SAME-REF-SET` still cannot separate a rename-redirect from a pristine fork, and the
specimen that proves it is in the table.** [`treeverse/dvc`](https://github.com/treeverse/dvc)
and [`iterative/dvc`](https://github.com/iterative/dvc) have identical full ref sets —
but `treeverse` is lakeFS's organisation, so a DVC *rename* is implausible and a never-touched
fork is not. 🟢 `ls-remote` cannot tell them apart and this pass does not pretend otherwise.
🔵 This is `ACTION ZZ-bw` advanced, not closed: `p366` could only compare `HEAD`, `p367` can
compare every ref, and **neither can read a redirect**.

🟢 **What the ref-set test DOES settle: eight organisation migrations this base writes both
ways.** `imsglobal/` → [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library)
(the IMS Global → 1EdTech rename), `edx/` → [`openedx/frontend-platform`](https://github.com/openedx/frontend-platform),
`all-hands-ai/` → [`openhands/openhands`](https://github.com/openhands/openhands),
`project-sunbird/` → `sunbird-knowlg/` and `sunbird-lern/`, `firebase/php-jwt` ≡
`googleapis/php-jwt`, `data-privacy-stack/presidio` ≡ [`microsoft/presidio`](https://github.com/microsoft/presidio),
`openedx/openedx-core` ≡ [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning).

### 🔴 `p366` published that the live row shelves were CLEAN. This base's own gate had been red since, and `p367` fixed the row

🔵 **`p366` wrote:** *"the four live row shelves are CLEAN… every row uses the current
canonical slug"*, with the pre-rename spellings surviving *"only in the APPEND-ONLY trend
history."* 🔴 **`make gate-alias-canonical` disagreed on the day it was written**, and has
been failing since, and `p367` found the defect on **two** shelves rather than the one the
gate names: `agents/top.md` and `repos/foundations.md` each carried a live row addressed
**`INGInious/INGInious`** (which `p367` believed was the pre-rename spelling of the pair
`p366` itself had just identified).

🔴 **`p370` CORRECTION — `p367` had the direction backwards and the shelves were right.**
Fetching `github.com/UCL-INGI/INGInious` **lands on `INGInious/INGInious`** (243 ★, breadcrumb
`INGInious / INGInious`, no rename notice), so `UCL-INGI/INGInious` is the **STALE** address and
`INGInious/INGInious` is canonical. `p367` therefore discharged a red gate by rewriting two
correct live rows into the stale spelling, and the gate went green only because the register it
reads (`p349`’s) carries no `INGInious` row at all. See the `p370` section of `intel/open-gaps.md`.

🟡 **`p367` wrote, and it is superseded by the correction above**: *"the row now cites `UCL-INGI/INGInious`"* — the **STALE** spelling;
🟢 `p370` restores [`INGInious/INGInious`](https://github.com/INGInious/INGInious) on both rows,
the pair is entered in `p283`'s alias ledger — established on the ref-set fingerprint, which
is the *"more than the HEAD"* that ledger's own header requires — and the gate is **green**.
🔵 **The lesson is about the claim, not the row.** `p366` asserted cleanliness from a
hand-read of the shelves while a standing gate built to answer exactly that question was
sitting red in the same repository. Checking a claim against the gate that owns it costs
one `make` invocation.

### 🟢 The offline arms, and the control that proves they are not eating anything

🔵 **Channel B over-collects by construction, because markdown prose is full of
`owner/repo`-shaped things that are not repositories.** Four arms reject them, each named
for the string that prompted it:

| Arm | Rejects | Specimen | Count |
|---|---|---|---:|
| `REF-OR-PATH-SEGMENT` | a first segment that is a ref or a directory | `main/LICENSE` (483 occurrences), `agents/top.md` (504) | **404** |
| `DOC-PATH` | a second segment that is a file | `openedx/__init__.py` | **101** |
| `NUMERIC-PAIR` | a ratio or a date | `47/47`, `2026/1744` | **46** |
| `GRANT-ID-PAIR` | a licence pair | `MIT/Apache-2.0` | **3** |
| `p351`'s shape and namespace arms, **imported not reimplemented** | illegal owners, nav namespaces, placeholders | `topics/ai-tutor`, `yourusername/SUMRY` | **1 173** |

🟢 **The arms are measured rather than trusted: 120 of the 1 727 rejected candidates were
probed with `ls-remote` and 0 are live.** 🔴 **The first run of that control reported 2 —
and both were artefacts of the control itself**, which split space-containing tokens on
whitespace and probed the fragments. Both "finds" are already carried as URLs. 🔵 Recorded
because a control that manufactures findings is worse than no control, and because the same
broken run is what exposed the `GLUED-SLUG` class (159 candidates, **4** live, **2.5%**
precision — included, with its precision stated).

### 🔴 Arm 1's grant-family words are load-bearing, and `p283`'s audit was right for the wrong reason

🔵 `make gate-ladder-case` graded this pass's instrument `SINGLE-SPELLING` on the `licence`
family the moment it entered `HOOK_GATES`, breaching `p286`'s ratchet (17 → 18). 🟡 **Two
remedies were tried and measured before the cause was found:**

1. 🟡 Case-closing the words in the literals — `p352`'s and `p354`'s remedy. Moved the
   reason from `no-upper-ext` to `UPPER-EXT` and **did not clear the grade.**
2. 🔴 Deleting the grant-family words. **Refuted by measurement**: six non-addresses leaked
   straight into the live population (`license/license`, `license/disclaimer`,
   `license/license.code`, `license/license.original`, `license/license.output`,
   `licenses/license-mit`).

🟢 **The cause was the instrument's own identifiers.** `p283`'s `BARE` pattern is
case-sensitive and unquoted, so it read the constant `LICENCE_TOKEN` and the status value
`"LICENCE-PAIR"` as licence *path* spellings — `p286`'s `_METHODS` defect arriving through a
constant and a status string instead of an attribute. Renamed `GRANT_ID_TOKEN` and
`GRANT-ID-PAIR`; the grade clears and the ratchet returns to 17. 🔵 **The channel-B
population was re-measured after each of the three attempts and is byte-identical at all
four points — 823 candidates.** A gate fix that moves the measurement is a different
instrument wearing the same name.

🔵 **What `p367` deliberately did NOT do, and why it is a declaration rather than an
omission.** Channel B is a **separate module**; `p348`'s `slugs_in` is untouched. Wiring it
into the canonical harvester would change **every** denominator this base has ever
published in a single commit, with no pass able to verify the result. Registered as
`ACTION ZZ-ca`, with the 496 named by address in
[`net-new-addresses`](../evidence/net-new-addresses.2026-10-21-p367.tsv) so the re-statement
has no search step.

**Pass 366 · 2026-10-21.** 🟢 **`p366` added no repository to this shelf and swept it for the
first time.** `ACTION ZZ-bu` named this shelf and `agents/top.md` as the two `p364`'s
companion sweep never read. 🔵 **Both are now swept: 199 addresses from this file, 159 from
`agents/top.md`, 329 deduped — all 329 live on `ls-remote`, 326 with a readable README, 484
companion edges.** Full mechanism and every number in `agents/top.md`.

🔴 **What this shelf should take from it: a named companion is usually NOT a dependency.**
Only **86 of 484 edges (17.8%)** are declared in the host's own manifests. **266 (55.0%)** are
a bare mention, **32 (6.6%)** are adopters pointing the other way, and for **100 (20.7%)** the
host ships no manifest at all, so direction has **no answer** rather than a negative one. 🟢
A README-derived dependency set is therefore an over-estimate of exposure by roughly **5.6×**,
and the manifest test — one request per host — is what separates the two.

🟢 **The payoff is concrete for this shelf: the grading backlog fell from 330 absent
companions to 58** (`ABSENT` ∩ `DEPENDENCY`), a **5.7×** reduction, and all 58 were graded
from payload: **36 MIT, 10 Apache-2.0, 4 BSD-3-Clause, 2 LGPL, 1 AGPL-3.0, 4 with no grant at
24 rungs, 1 a template placeholder that is not a repository.**

🔴 **The one AGPL-3.0 in that set is a declared dependency and belongs on this shelf's
radar:** [`openedx/frontend-build`](https://github.com/openedx/frontend-build) — **AGPL-3.0**
at `main/LICENSE`, declared by an Open edX host, i.e. the build tooling under a platform this
shelf recommends reaching **over a boundary** and not forking. 🟢 The boundary rule in
`compose/patterns.md` already covers it; it is now named rather than implied.

### 🔴 Two methodological warnings for every grant and absence cell on this shelf

🔴 **1. An absence is only as good as the ladder, and `p366` caught itself twice.** Three
BSD-3-Clause payloads were graded `RESERVED` because *"All rights reserved"* appears in the
BSD body and was tested **before** the grant text; `rails/rails` (MIT at `MIT-LICENSE`) and
`systemd/systemd` (LGPL at `LICENSE.LGPL2.1`) were graded *"no grant"* because those rungs
were missing. 🟢 **5 of 58 cells — 8.6% — changed on repair.** Any cell on these shelves
produced by a grader that tested a reservation phrase first, or that stopped at 14 rungs, is
exposed to the same two defects. Evidence:
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p366.tsv).

🔴 **2. The absence DENOMINATOR itself is wrong, by a measured 8.2%.** The corpus every
absence claim here is tested against is built from **`github.com/`-prefixed** strings, so a
repository this base discusses as a bare backticked slug reads as absent. **27 of `p366`'s
329 `ABSENT` verdicts were wrong on that account** — among them `CAHLR/OATutor-Content`,
which this base mentions 7 times and whose missing licence it already records. 🟡 True
absent count: **302, not 330.** Registered as `ACTION ZZ-bv`;
[`bare-slug-absence`](../evidence/bare-slug-absence.2026-10-21-p366.tsv).

🟢 **One row on this shelf is annotated for identity, not for grant.**
[`meta-pytorch/opacus`](https://github.com/meta-pytorch/opacus) (**Apache-2.0**) and
`pytorch/opacus` are **ONE repository** — identical `HEAD` `df040e4a15`, an organisation
migration. 🟢 This shelf's row uses the current canonical slug and is correct; the old slug
survives in the append-only trend history. Same for
[`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
≡ `digitalcredentials/learner-credential-wallet` (`1c46a82ba3`) and `INGInious/INGInious` ≡ `UCL-INGI/INGInious` (`b423828c02`). 🔵 **Slug equality cannot see any of the three** — only
the `HEAD` sha can. `ACTION ZZ-bw`.

🟢 **`p366` evidence:** [`companion-closure-unswept`](../evidence/companion-closure-unswept.2026-10-21-p366.tsv) ·
[`edge-direction`](../evidence/edge-direction.2026-10-21-p366.tsv) ·
[`exposure-grants`](../evidence/exposure-grants.2026-10-21-p366.tsv) ·
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p366.tsv) ·
[`bare-slug-absence`](../evidence/bare-slug-absence.2026-10-21-p366.tsv) ·
[`slug-identity-head`](../evidence/slug-identity-head.2026-10-21-p366.tsv)

🔴 **Gate state `p366`: NOT RUN.** `make hooks` could not execute in this pass's environment
(the runner declined to run the repository's own Python and shell instruments). 🔵 No claim in
this section was checked by the gate suite; everything was derived from first-hand
`ls-remote` and `raw.githubusercontent.com` reads. A successor should re-judge it.

---

**Pass 365 · 2026-10-21.** 🟢 **`p365` added no repository to this shelf and measured a
property *of* it:** whether the rows here can be **pinned** at all. 🔴 **Of the 191
permissive-claimed addresses across this file, `agents/top.md` and
`verticals/solutions.md`, 61 — 31.9% — have never cut a stable release tag.** A row with no
tag cannot be consumed at a version; it is consumed at a **moving branch**, and its grant
cell is true of the commit at which it was read and of nothing else. 🟡 **The LTI
interoperability tier is over-represented in that 61** — the layer this shelf recommends
building integrations on is the layer least able to offer a pinnable release.

🟢 **Of the 130 rows that CAN be pinned, 128 carry the same licence family at both pins**,
and every mismatch sits in the 11-row class that has tagged exactly once. Two rows on this
shelf are now annotated for it: **`harvard-edtech/caccl`** (MIT at `main/LICENSE.md`, **no
grant at `1.0.59`, its only tag**) and **`muhammedalakbarli/imparo`** (MIT at `main`,
**"All Rights Reserved" at `pilot-v1.0`**).

🟢 **`p365` evidence:** [`version-axis-frequency`](../evidence/version-axis-frequency.2026-10-21-p365.tsv) ·
[`single-tag-risk`](../evidence/single-tag-risk.2026-10-21-p365.tsv) ·
[`caccl-tag-probe`](../evidence/caccl-tag-probe.2026-10-21-p365.tsv) ·
[`probe-reliability`](../evidence/probe-reliability.2026-10-21-p365.tsv) ·
[`transport-enumeration`](../evidence/transport-enumeration.2026-10-21-p365.tsv)

🔴 **Methodological warning for every grant cell on this shelf.** `p365`'s first sweep
produced **four false "no grant" verdicts in 191 rows** — one from treating any non-200 as
absence, three from a probe ladder missing the **lowercase `license.txt`** rung. All four
named repositories whose grants this base had already read correctly. 🟢 Re-run with retry
and a 13-rung case-varied ladder, **zero probe failures**. 🔵 Any cell on these shelves
produced by a probe that retried nothing is exposed to the same defect.

**Pass 364 · 2026-10-21.** The systems an education engagement starts *from*, rather
than the agents it adds on top. 🆕 **`p364` adds the tier below them** — the components a
platform's own README tells you to install, graded by payload, in
*"`p364`: the DEPLOYMENT tier"* below. Every row verified first-hand **2026-10-21**: liveness
and default branch via `git ls-remote --symref`, licence **read from the payload**.

🔴 **`p362` corrects two grants in the code-execution tier, and both corrections change
what an engagement may do with the row.** [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger)
is **not MIT** — its payload is the Star And Thank Author License — and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) is **GPL-3.0, not
AGPL-3.0**. 🔵 The first narrows what was published as permissive; the second *widens*
what was published as network copyleft. Full mechanism in `agents/top.md`; the sweep that
found the first is [`mit-body-sweep`](../evidence/mit-body-sweep.2026-10-21-p362.tsv) and
the corrections are in
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p362.tsv).

🟢 **Gate state `p362`:** `make hooks` ran — **28/32 green on arrival, 32/32 on exit**.
RED on arrival: `gate-absence`, `gate-shelf-consistency`, `gate-author-key`,
`gate-census-currency`.
🟢 **`gate-shelf-consistency`'s RED is what found the `Sharif-Judge` defect**: it reported
the slug carrying `AGPL-3.0` on `verticals/solutions.md` and `MIT` on this shelf, and both
cells turned out to be wrong in different ways — the `MIT` was an **adjacency** read of a
sentence about `QingdaoU/Judger`, and the `AGPL-3.0` was a real mis-grading of the
payload.

🟢 **`p361` is the first pass since `p355` with a working GitHub index, and it did not
arrive through `curl`.** `api.github.com` still answers **403** on every path; the
session's GitHub MCP search tool answers in full. 🔵 The five passes that recorded "no
index" were recording one transport. See `agents/top.md` for the full channel finding.

🟢 **Gates run before this pass wrote:**

| Gate | Result |
|---|---|
| Whole-corpus liveness (`ls-remote --symref`, 16-way parallel, 277 addresses) | 🟢 **277 of 277 live, 0 dead** |
| Star re-derivation (index, batched `repo:` queries) | 🟢 **273 of 277 measured at their published spelling; 78 blind cells filled; 89 published figures re-derive, 78 within ±2** |
| 🆕 **Archived sweep** (`archived:true fork:true`, all 277) | 🔴 **1 hit — and it was published on this shelf unflagged** |

🔴 **`p361` corrects two rows on this shelf, and both corrections come from the index
rather than from any channel this base already had.**

**1. `zmievsa/autograder` is archived.** Read-only upstream: no commits, issues or PRs
ever again. 🔴 **It answers `ls-remote` exactly like a healthy repository**, which is
precisely why 360 passes of liveness sweeps never caught it. Flagged in the autograding
table below.

**2. The OneRoster row was pointed at a fork, and the fork's death date was published as
the project's.** `p359` shelved [`jeffyding/OpenLRW`](https://github.com/jeffyding/OpenLRW)
as *"the only address that carries OneRoster"* and dated it **January 2018**. 🔴 **That
address is a fork** — `fork: true`, **0 ★**, created and last touched the same day,
2018-01-19. 🟢 **The canonical upstream is
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
— 62 ★, 25 forks, different HEAD SHA, ECL-2.0 read from `master/LICENSE`.** 🔵 **This
base already held the same organisation's `Larissa` and still shelved a fork of its other
project**, because the fork was what a non-ranked search surfaced. Corrected below.

🟡 **The conclusion survives the correction, and that is worth saying plainly.** The
canonical's last commit is **2020-02-06**, not 2026 — two years later than the fork, and
still six years ago. 🔴 **So "read the schema, do not take the dependency" stands; the
*address* and the *date* were wrong, the *advice* was right.**

**Read the default-branch column.** Education infrastructure is old software. Of the
grants on this shelf, a large share live on `master`, `develop`, `release` or a
version branch — not `main`. A tool that assumes `main` will report a live,
correctly-licensed repository as grantless. That has happened on this base before, and
`p361` adds a fresh instance from a national curriculum body — Oak National Academy
spells its grant **`LICENCE`**, and `LICENSE` 404s (see `agents/top.md`).
---

## 🟢 🆕 `p371`: the regional supply map, **placed from each repository's own payload** — 450 of 1 859 addresses carry geography, and APAC and North America are where the production-scale platforms are

🔵 **Why this tier is different from every other region claim on this base.** The regional
*demand* side — regulation, market size, ministry programmes — has always been
snippet-sourced here, and `intel/market.md` says so on every line. 🟢 **This tier is the
SUPPLY side and it is first-hand**: each row below was placed by reading an institution or
a jurisdictional standard out of the repository's own README, at a pinned sha, in the same
blobless clone that enumerated its tree. 🔴 **A maintainer's name never placed a row**
(`P800`), a language never placed a row, and a filename never placed a row — the last of
those only because the placer's first run placed five rows in Paraguay on `server.py` and
`main.py`, which is `gate-region-place`'s `D2`.

| the question | the answer, `2026-10-21` |
|---|---:|
| addresses graded this pass | **1 859** |
| 🟢 placed in a region from their own payload | 🟢 **450 (24.2 %)** |
| of those, by channel: a committed institutional owner | **122** |
| an academic or government host | **82** |
| any other country host | **246** |
| 🟡 reported as `SPLIT` — two regions, so placed `Global` | 🟡 **20** |
| 🟢 placed by the **jurisdiction they implement** (FERPA / GDPR / LGPD / DPDP) | 🟢 **125** |

🔵 **`ORIGIN` and `SERVES` are separate cells and are never merged.** `p115`'s stoplist
header is right that *"a repository that CITES the EU AI Act is not a European
repository"* — and an engagement still needs to know which regime a tool implements. Two
claims, two columns.

### 🟢 In-domain supply by region, and the licence mix inside each

| Region | permissive | copyleft | content | restricted | no grant | total in domain |
|---|---:|---:|---:|---:|---:|---:|
| **North America** | 🟢 **84** | 17 | 2 | 2 | 🔴 11 | **118** |
| **EMEA** | 🟢 **46** | 17 | 8 | 1 | 🔴 12 | **86** |
| **APAC** | 🟢 **42** | 4 | 1 | 1 | 🔴 8 | **58** |
| **LATAM** | 🟢 **17** | 6 | 0 | 0 | 🔴 5 | **30** |
| *unplaced (`Global`)* | 592 | 119 | 7 | 6 | 199 | 946 |

🟢 **The permissive share is remarkably flat across the four regions** — 71 %, 53 %, 72 %,
57 % — which is the fourth independent corroboration of §22 of
[`intel/trends.md`](../intel/trends.md): **the licence variable is producer type, not
geography.** 🔴 **What is NOT flat is volume.** North America and EMEA carry 204 of the 292
placed in-domain addresses; LATAM carries 30. 🔵 That is a real asymmetry and it is not the
one the trade press reports — see the LATAM note below, where the 30 turn out to reach
something no other region's supply reaches.

### 🟢 North America — the **state data standard** is the tier, and it is Apache-2.0 end to end

| Component | Repo | Licence | Grant, at the pin | refs | Placed by |
|---|---|---|---|---:|---|
| The Ed-Fi ODS, the US K-12 operational data store | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | 🟢 **Apache-2.0** | `HEAD/LICENSE.txt` @ `b6b72e594bc4` | **1 651** | owner (Ed-Fi Alliance) |
| Its admin API | [`Ed-Fi-Alliance-OSS/ODS-Admin-API`](https://github.com/Ed-Fi-Alliance-OSS/ODS-Admin-API) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `6bcf500a186e` | **831** | owner |
| The data standard itself | [`Ed-Fi-Alliance-OSS/Ed-Fi-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Standard) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `3d24df6675c5` | **467** | owner |
| Its modelling toolchain | [`Ed-Fi-Alliance-OSS/MetaEd-js`](https://github.com/Ed-Fi-Alliance-OSS/MetaEd-js) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `a7f3c6986c05` | **1 827** | owner |
| Learning analytics running in a real university | [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `44dbf906f7c8` | **1 032** | `its.umich.edu` |
| The xAPI specification | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `ca782a1129bc` | **904** | owner (US DoD ADL) |
| Open edX analytics, deployable | [`openedx/tutor-contrib-aspects`](https://github.com/openedx/tutor-contrib-aspects) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `d60eef009420` | **1 421** | owner |

🔵 **Why this matters commercially and not just technically:** an Ed-Fi engagement is the
one US K-12 integration whose target schema is **published, versioned and Apache-2.0**, so
the integration work is specification work rather than reverse-engineering a vendor API.

### 🟢 EMEA — a **national government service** is shelvable here, which is new

| Component | Repo | Licence | Grant, at the pin | refs | Placed by |
|---|---|---|---|---:|---|
| 🆕 The UK Department for Education's teacher-training register, in production | [`DFE-Digital/register-trainee-teachers`](https://github.com/DFE-Digital/register-trainee-teachers) | 🟢 **MIT** | `HEAD/LICENCE` @ `a210ba1a13b4` | **6 593** | its own service host |
| The University of Helsinki's MOOC platform | [`rage/secret-project-331`](https://github.com/rage/secret-project-331) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `d198c94c8084` | **1 383** | `www.mooc.fi` |
| France Université Numérique's course-commerce service | [`openfun/joanie`](https://github.com/openfun/joanie) | 🟢 **MIT** | `HEAD/LICENSE` @ `21f6bfe29953` | **1 213** | owner (FUN) |
| FUN's learning-analytics service | [`openfun/warren`](https://github.com/openfun/warren) | 🟢 **MIT** | `HEAD/LICENSE.md` @ `839fcbb411d1` | **295** | owner (FUN) |
| 🆕 The LLM tutor inside TUM's Artemis | [`ls1intum/Iris`](https://github.com/ls1intum/Iris) | 🟢 **MIT** | `HEAD/LICENSE` @ `d7b2c095204e` | **245** | `artemis.cit.tum.de` |
| A courseware platform used in real university courses | [`inducer/relate`](https://github.com/inducer/relate) | 🟢 **MIT** | `HEAD/LICENSE` @ `7030dd609545` | **1 139** | `documen.tician.de` |
| A German university LMS | [`geli-lms/geli`](https://github.com/geli-lms/geli) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `02ae52087e74` | **1 250** | `demo.geli.fbi.h-da.de` |
| Gamified CS teaching, assets licensed separately | [`Dungeon-CampusMinden/Dungeon`](https://github.com/Dungeon-CampusMinden/Dungeon) | 🟢 **MIT** (code) | `HEAD/LICENSE.md` @ `5856a782a8e0` | **1 836** | `www.hsbi.de` |

🔴 **`Dungeon` is `gate-grant-scope`'s specimen and it is why this pass added `D6` to the
census rule.** It carries **five** grant files — `LICENSE.md` **MIT** (the code),
`LICENSE-ASSETS.md` **CC0-1.0**, `LICENSE-ICONS.md`, `LICENSE-NOTICE.md` **LGPL** and
`LICENSE-PAPER.md` **CC-BY-SA-4.0** — and the first draft of this census ranked by
permissiveness, so the repository's licence cell came from its **asset** grant. 🟢 An
unscoped root file is the code grant; `LICENSE-<SCOPE>` describes something else. **160 of
these 1 859 addresses carry more than one grant file**, so this is not a corner case.

### 🟢 APAC — the **production-scale national platforms** are here

| Component | Repo | Licence | Grant, at the pin | refs | Placed by |
|---|---|---|---|---:|---|
| 🆕 India's national learning platform (Sunbird / DIKSHA) — portal | [`project-sunbird/sunbird-portal`](https://github.com/project-sunbird/sunbird-portal) | 🟢 **MIT** | `HEAD/LICENSE` @ `9efc8b5819c6` | **11 606** | owner |
| 🆕 Its LMS middleware | [`project-sunbird/sunbird-lms-mw`](https://github.com/project-sunbird/sunbird-lms-mw) | 🟢 **MIT** | `HEAD/LICENSE` @ `fc470e0bec49` | **1 068** | owner |
| 🆕 NUS Singapore's course platform, in production | [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 🟢 **MIT** | `HEAD/LICENSE` @ `6310c973a303` | **7 723** | `www.comp.nus.edu.sg` |
| 🆕 Education data mining toolkits (USTC) | [`bigdata-ustc/EduData`](https://github.com/bigdata-ustc/EduData) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `7efdbc04711c` | **104** | `base.ustc.edu.cn` |
| 🆕 Cognitive diagnosis models (USTC) | [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** | `HEAD/LICENSE` @ `c610e6ae7f45` | **66** | `staff.ustc.edu.cn` |
| 🆕 Singapore IMDA's AI-testing corpus | [`aiverify-foundation/moonshot-data`](https://github.com/aiverify-foundation/moonshot-data) | 🟢 **Apache-2.0** | `HEAD/LICENSE.md` @ `30fac1237547` | **260** | owner |
| 🆕 Korea's NEIS school-information API client | [`SaidBySolo/neispy`](https://github.com/SaidBySolo/neispy) | 🟢 **MIT** | `HEAD/LICENSE` @ `ef50b19caba9` | **63** | `open.neis.go.kr` |
| 🆕 New Zealand's CS curriculum field guide | [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **MIT** | `HEAD/LICENCE` @ `7e323930cf6f` | **2 827** | `csfieldguide.org.nz` |

🟢 **Sunbird at 11 606 refs is the largest in-domain repository this pass placed anywhere**,
and it is the platform behind India's DIKSHA. 🔵 Fifth independent corroboration of §15 of
`intel/trends.md`: APAC's supposed gap is in the trade press, not in the supply.

### 🟢 LATAM — only 17 permissive addresses, and they reach **the incumbent university SIS**, which no other region's supply does

| Component | Repo | Licence | Grant, at the pin | refs | Placed by |
|---|---|---|---|---:|---|
| 🆕 A reach into **SIU-Guaraní**, the Argentine university SIS | [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) | 🟢 **MIT** | `HEAD/LICENSE` @ `6962638adbdd` | **42** | `documentacion.siu.edu.ar` |
| 🆕 A reach into **SIGAA**, the Brazilian federal-university SIS | [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) | 🟢 **MIT** | `HEAD/LICENSE` @ `7373c6abac62` | **8** | `sigaa.ufpb.br` |
| 🆕 A second SIGAA reach, timetable repair | [`luthierycosta/ConsertandoHorariosSIGAA`](https://github.com/luthierycosta/ConsertandoHorariosSIGAA) | 🟢 **MIT** | `HEAD/LICENSE` @ `5a6106ed9ce2` | **8** | `unb.br` |
| 🆕 Chile's open-data hub, education datasets included | [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🟢 **MIT** | `HEAD/LICENSE` @ `940a63783461` | **353** | `datos.gob.cl` |
| 🆕 A pedagogy benchmark for LLMs, Chilean teacher-training source | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | `HEAD/LICENSE` @ `21a43a395ab4` | **11** | `www.cpeip.cl` |
| 🆕 Brazilian federal open-data MCP server | [`dasgltd/mcp-brasil`](https://github.com/dasgltd/mcp-brasil) | 🟢 **MIT** | `HEAD/LICENSE` @ `2efb258370b1` | **51** | `portaldatransparencia.gov.br` |
| 🆕 An Argentine open-education lab | [`fhleonardi/openredlab`](https://github.com/fhleonardi/openredlab) | 🟢 **MIT** | `HEAD/LICENSE` @ `c507d0b56aac` | **108** | `opentecnologia.ar` |
| 🆕 A Brazilian CS curriculum corpus | [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao) | 🟢 **MIT** | `HEAD/LICENSE` @ `b995c118fdb3` | **101** | `books-sol.sbc.org.br` |

🟢 **This is the most useful thing `p371` found for a LATAM engagement, and it is a shape
finding rather than a count.** `p370` graded the **incumbent-LMS** bridge class — Moodle,
Canvas, Blackboard, Brightspace, PowerSchool, Banner — and that class is overwhelmingly
North American and European software. 🔴 **The LATAM supply does not reach those systems.
It reaches SIGAA and SIU-Guaraní**, the SIS platforms that Brazilian federal and Argentine
national universities actually run, and which do **not** appear anywhere in `p370`'s
ten-platform bridge table. 🔵 **A LATAM higher-education engagement that plans a Canvas or
Banner integration is planning for the wrong incumbent**, and the two reaches above — 8
and 42 refs, small and MIT — are the only published starting points this base has found in
371 passes.

🟡 **The honest limit on all four tables.** A ref count is not a star count: `api.github.com`
answers `403` at this proxy, so popularity is unavailable and `refs` (branches plus tags
plus pull refs) is a proxy for activity, not for adoption. It is reported because it was
measured in the same request as the grant.

## 🟢 🆕 `p370`: the permissive **standards layer** under the bridge tier — LTI 1.3, OneRoster, xAPI and QTI, every grant enumerated from the git tree

🔵 **Why a standards layer is a foundations question and not an agents question.** The
bridge tier on `agents/top.md` is 71 % ungranted, so for most client platforms the
engagement answer is *write your own connector*. 🟢 **That answer is only affordable if
the protocol libraries underneath are permissive** — and this pass establishes that they
are, from payload, at a pinned sha.

🟢 **Evidence for §`p370`:** [`git-tree-run`](../evidence/git-tree-run.2026-10-21-p370.tsv) · [`tree-grant-domain`](../evidence/tree-grant-domain.2026-10-21-p370.tsv) · [`transport-matrix`](../evidence/transport-matrix.2026-10-21-p370.tsv)

| Standard | Component | Licence (payload) | Grant read at | ★ 2026-10-21 | Region | Layer |
| --- | --- | --- | --- | ---: | --- | --- |
| **LTI 1.3 / Advantage** | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0**, 11 361 B | `HEAD/LICENSE` @ `41f150c0693b` | **373** | Not placed | Node.js tool provider — *"turn your application into a fully integratable LTI 1.3 tool provider"*. 🟢 **The strongest permissive row in this layer** |
| **LTI 1.3 / Advantage** | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 **Apache-2.0**, 11 343 B | `HEAD/LICENSE.md` @ `66d8e4e4b9bd` | **54** | Not placed | PHP, **IMS-certified** tool providers. 🟢 Resolves `p369`'s index artefact — 224 refs answered the git protocol |
| **LTI 1.3** | [oxctl/spring-security-lti13-demo](https://github.com/oxctl/spring-security-lti13-demo) | 🟢 **Apache-2.0**, 11 358 B | `HEAD/LICENSE.txt` @ `ee38b2f202` | — | **EMEA** (UK) | Spring Security LTI 1.3 wiring, from Oxford's `oxctl` org. 🟡 **A demo tool by its own first line** — read it as a reference, not a dependency |
| **LTI 1.3** | [kaiofelps/lti-consumer-poc](https://github.com/kaiofelps/lti-consumer-poc) | 🟢 **MIT**, 1 068 B | `HEAD/LICENSE` @ `eab0649dd8` | — | Not placed | Consumer-side proof of concept. 🟡 A PoC by its own name — the consumer half, which the two libraries above do not cover |
| **OneRoster** | [vossenv/oneroster-python](https://github.com/vossenv/oneroster-python) | 🟢 **MIT**, 1 073 B | `HEAD/LICENSE.txt` @ `fe578a2e01` | **11** | **North America** | Python client for the **Clever** and **Classlink** rostering vendors. 🟡 *"This library is in beta, and changes often. Use at your own risk."* — its own words, carried |
| **xAPI (Experience API)** | [apereo-learning-analytics-initiative/sakaixapi-provider](https://github.com/apereo-learning-analytics-initiative/sakaixapi-provider) | 🟡 **ECL-2.0**, 558 B | `HEAD/LICENSE_HEADER` @ `59da726edd` | — | **North America** | Sakai xAPI event provider, Apereo. 🔴 **558 B is a per-file HEADER TEMPLATE, not a full grant text** — the family is right, the artefact is a stub, and a client's legal review will ask for the full licence |
| **Open edX components** | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0**, 11 358 B | `HEAD/LICENSE.TXT` @ `5693f681ff7c` | **471** | Not placed | 🟢 **`p369`'s unresolved grant, resolved.** The component framework, and the permissive entry point into AGPL Open edX |
| **Curriculum data** | [ayrtonmoura1/conectabncc](https://github.com/ayrtonmoura1/conectabncc) | 🟢 **MIT**, 1 070 B | `HEAD/LICENSE` @ `37cb447f0a` | — | **LATAM** (Brazil) | Brazil's **BNCC** as a graph — `competencias_bncc.json`, `bncc_progressao_pre_requisitos.json`, `relacoes_bncc_final.json`. 🔵 **Shipped with no README at all**: its file names are the only domain evidence it has, and they were enough |
| **Classroom discourse** | [ddemszky/classroom-transcript-analysis](https://github.com/ddemszky/classroom-transcript-analysis) | 🟢 **MIT**, 1 069 B | `HEAD/LICENSE` @ `ff63e97873` | **46** | **North America** | Analysis code for Demszky & Hill (2023); a Stanford contact address in the README. Teacher-talk measurement, the layer above a transcript |

### 🔴 The grant that was never 404 — and why the tree channel, not the next transport, was the answer

🔴 **`p369` reported `openedx/XBlock` as *"404 on every branch and filename probed"* and
nominated the PyPI sdist as the next transport to try.** 🟢 The file is **`LICENSE.TXT`**.
🔵 **Every HTTP licence probe on this base is a filename guess**, because
`raw.githubusercontent.com` cannot list a directory — it can only confirm or deny a name
you already hold. A blobless partial clone enumerates the tree, so the name is not
guessed; it is read.

🟡 **The same mechanism, shown positively on a second row this pass.**
`raw.githubusercontent.com/openfun/ralph/HEAD/LICENSE` is a **404** and
`…/LICENSE.md` is a **200** — the grant was never missing, only differently spelled. Both
probes are in [`transport-matrix`](../evidence/transport-matrix.2026-10-21-p370.tsv).

🔴 **And the part that is about this base rather than about GitHub:**
`compose/code/p1057-licence-path-case` was built at `p189`, *about this exact repository
and this exact file*, with 16 passing controls and a published correction. It never became
a gate. 🔵 **An instrument that is not standing is an instrument that will be paid for
twice** — and `ACTION ZZ-cd` now carries wiring it, beside the backlog it belongs to.

### 🟢 The transport matrix, measured, because two passes in a row disagreed about it

| Channel | This pass | What it can do |
|---|---|---|
| `github.com` (HTML) | 🔴 **403** at the proxy | nothing |
| `api.github.com/repos/…` | 🔴 **403** at the proxy | nothing — 🟡 and `api.github.com/rate_limit` answers **200**, so an availability check on the host is not an availability check on the endpoint |
| `raw.githubusercontent.com` | 🟢 **200** | fetch a path **you can already name**; cannot list |
| **`git` over https** | 🟢 **200 — 63 of 63 slugs** | 🟢 `ls-remote` (existence, default ref, full ref set) and a blobless partial clone (**the root tree enumerated**, then the exact blobs) |

🔵 `p368` lost the payload channel to a 403 and substituted metadata. `p369` had `raw`
and used it. 🟢 **`p370` has `raw` too and still does not probe it first**, because the
git channel answers a question `raw` cannot be asked: *what licence files does this
repository actually contain?*

---

## 🟢 🆕 `p369`: the infrastructure half of the promotion backlog — fifteen components, every licence read from payload

🔵 **Same instrument as `agents/top.md` §`p369`.** Of the 66 most-cited addresses this base
had never shelved, these fifteen are **components**, not products: the measurement,
interoperability and records layers a tutoring or grading deliverable sits on. 🟢 Licence =
payload read on `raw.githubusercontent.com`; ★ = GitHub API, 2026-10-21.

| Component | Licence (payload) | ★ | Region | Layer it serves |
| --- | --- | ---: | --- | --- |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** | **585** | 🟡 EMEA (UK, inferred) | Learning Record Store — the original xAPI LRS, since 2014 |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🔴 **unresolved** | **471** | North America (Open edX) | Component framework for custom learning objects inside Open edX |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** | **288** | North America (UC Berkeley) | **Bayesian Knowledge Tracing** — mastery estimation, C++ core with a Python API |
| [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | **153** | 🟡 LATAM (Brazilian author, inferred) | **Computerised adaptive testing** simulator: IRT item selection, ability estimation, stopping rules |
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🟡 **Apache-2.0 (README only)** | **99** | North America (ADL) | Emits xAPI statements from legacy SCORM content. 🔴 **ARCHIVED** — read it, do not depend on it |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 **LGPL** | **64** | EMEA (OAT, Luxembourg) | TAO assessment platform core — QTI item banking and delivery |
| [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** | **51** | EMEA (France Université Numérique) | **LRS and learning-analytics pipeline** (FastAPI, pydantic, xAPI). 🟢 The only permissively-licensed LRS on this shelf |
| [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🟡 **Creative Commons (README only)** | **45** | EMEA (ETH Zurich) | Benchmark for **open-ended pedagogical capability** of LLM tutors, EMNLP 2025 oral |
| [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | 🟡 **LGPL** | **37** | EMEA (OAT, Luxembourg) | LTI 1.3 / LTI Advantage, as platform **and** as tool, in PHP |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **Creative Commons** | **9** | **LATAM (Brazil)** | The **BNCC** national curriculum as an npm/PyPI package **and an MCP server** — one line to make a tutor curriculum-aligned |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** | **6** | North America (Ed-Fi Alliance) | Serves a **OneRoster 1.2** API from an Ed-Fi ODS — the US district rostering bridge |
| [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) | 🟢 **MIT** | **6** | Not placed | OneRoster API client for .NET estates |
| [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** | **5** | Not placed | Dependency-light, framework-neutral **QTI 3** reference implementation in TypeScript |
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | 🟡 **MIT (README only)** | **3** | Not placed | Evaluation framework for the **pedagogical** effectiveness of LLM tutors in maths |
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** | **1** | North America (Intel) | Reference apps, microservices and **hardware benchmarking** for education AI workloads. Created 2026-09-30 |

🟢 **The row that closes a standing gap: `openfun/ralph`.** This shelf has carried
`LearningLocker` as the LRS answer in trending for passes without shelving it — and it is
**GPL-3.0**. `Ralph` is **MIT**, maintained by France Université Numérique, and speaks xAPI
over a FastAPI pipeline. 🔵 For any engagement where learning records must be collected and
the deliverable must stay closed, Ralph is the row; Learning Locker is the one to quote when
the client already runs it.

🟢 **`CAHLR/pyBKT` + `douglasrizzo/catsim` are the measurement pair this base kept
describing and never shelved.** Between them they cover both halves of adaptive assessment —
*what does the learner know* (BKT) and *what should we ask next* (IRT / CAT) — under MIT and
BSD-3-Clause respectively. 🔵 Neither is an LLM project, which is precisely why they are the
defensible part of an adaptive-learning claim: the mastery estimate comes from a
peer-reviewed algorithm with a citation, not from a prompt.

🔴 **`openedx/XBlock` is shelved with its grant unresolved, and that is the honest cell.**
Four branch/filename combinations were probed on `master` (`LICENSE`, `LICENSE.txt`,
`LICENCE`, `COPYING`) and all returned 404. Open edX publishes XBlock as Apache-2.0 in its
documentation, but **this base did not read that grant from the repository**, and §14 ("a
badge is not a grant") applies to a doc page as much as to a shield. 🔵 `ACTION`: resolve it
from the PyPI sdist metadata next pass — a transport this base has not yet enumerated.

🟡 **Three rows carry a grant that exists only in a README** — `SCORM-to-xAPI-Wrapper`,
`mathtutorbench`, `AITutor-EvalKit`. 🔵 That is weaker than a `LICENSE` file and stronger than
nothing: it is evidence of intent that a client's counsel can ask the maintainer to
formalise. All three are *reference* material — a wrapper to read, two benchmarks to run —
so none of them needs to be redistributed, which is what makes the weak grant tolerable
here and would not elsewhere.

🔴 **`bncc-dev/bncc-pacotes` is Creative Commons, and for curriculum data that is normal
rather than alarming.** CC is a *content* licence; the BNCC text is a government curriculum
document, and the package is a distribution of it. 🟢 The engagement reading: the **data** can
be used under its CC terms, the **MCP server** around it should be treated as unlicensed code
until the repository says otherwise. See Pattern 28.

## Learning platforms (LMS / VLE)

| Platform | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Open edX LMS + Studio | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | `master/LICENSE` | **8 205** | North America |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `main/COPYING.txt` — 🔴 no `LICENSE` file exists | **7 508** | Global |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | `master/LICENSE` | **6 879** | North America |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `develop/license.txt` — 🔴 (lower-case) | **3 329** | APAC |
| ClassroomIO | [classroomio/classroomio](https://github.com/classroomio/classroomio) | AGPL-3.0 | `main/LICENSE` | **1 726** | Global |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `develop/LICENSE` | **1 159** | Global |
| Tutor (Open edX distro) | [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | `release/LICENSE.txt` | **1 128** | Global |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `master/LICENSE` | **1 016** | EMEA |
| Moodle App (mobile) | [moodlehq/moodleapp](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** | 🔴 `main/COPYING.txt` | **1 002** | Global |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | `master/LICENSE` | **1 239** | North America |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | `master/LICENSE` | **448** | EMEA |
| ELMS Learning Network | [elmsln/elmsln](https://github.com/elmsln/elmsln) | GPL-3.0 | `master/LICENSE.md` | **253** | North America |

🟢 **The two permissive platform rows matter disproportionately.** `OpenOLAT`
(Apache-2.0) and `kolibri` (MIT) are the only full platforms here that can be
embedded in a closed client deliverable without copyleft reach. And
`moodlehq/moodleapp` is **Apache-2.0 while Moodle core is GPL-3.0** — the mobile
client can be forked into proprietary work where the server cannot.

## 🆕 National school portals — the ENT tier, and the first platform family placed in EMEA by its own vendor's commit channel

🟢 **What this shelf was missing.** It carried the *interchange* layer in depth — LTI,
SCORM, xAPI, Caliper, LRS, OneRoster — and every platform row above is an LMS. A **school
portal** is a different system: identity, messaging, timetable, attendance, the statutory
lesson log and the competency record, procured by a region for every school in it. France
has standardised on one since 2003 and it is open source.

**ENT** — *Espace Numérique de Travail* — was launched by the Ministry of Education with
the Caisse des dépôts in 2003 and is procured per *région* and per *département*.
`entcore` is its modular kernel, and it implements both *premier degré* (primary) and
*second degré* (secondary) from the same core.

| System | Repo | Licence (read from payload) | Grant read at | Default ref | Region |
| --- | --- | --- | --- | --- | --- |
| **entcore** — ENT kernel | [edificeio/entcore](https://github.com/edificeio/entcore) | 🟡 **AGPL-3.0** | `master/LICENSE` | `master` | EMEA |
| Cahier de textes | [OPEN-ENT-NG/cahier-de-textes](https://github.com/OPEN-ENT-NG/cahier-de-textes) | 🟡 **AGPL-3.0** | `dev/LICENSE` | 🔴 `dev` | EMEA |
| Présences (attendance) | [OPEN-ENT-NG/presences](https://github.com/OPEN-ENT-NG/presences) | 🟡 **AGPL-3.0** | 🔴 `dev/LICENCE` | 🔴 `dev` | EMEA |
| Compétences (competency record) | [OPEN-ENT-NG/competences](https://github.com/OPEN-ENT-NG/competences) | 🟡 **AGPL-3.0** | 🔴 `dev/LICENCE` | 🔴 `dev` | EMEA |
| Exercizer (interactive exercises) | [open-ent/exercizer](https://github.com/open-ent/exercizer) | 🟡 **AGPL-3.0** | 🔴 `master/LICENCE` | `master` | EMEA |
| Blog module | [edificeio/blog](https://github.com/edificeio/blog) | 🟡 **AGPL-3.0** | `develop/LICENSE` | 🔴 `develop` | EMEA |
| Mindmap module | [OPEN-ENT-NG/mindmap](https://github.com/OPEN-ENT-NG/mindmap) | 🟡 **AGPL-3.0** | `develop/LICENSE` | 🔴 `develop` | EMEA |

🔴 **Not one row in this tier defaults to `main`**, and **three of seven grants are spelled
`LICENCE`.** 🟢 This is the single strongest case on this shelf for the warning three
paragraphs up and for `ACTION ZZ-q`'s orthography axis: a tool keyed on `main/LICENSE`
reports an entire national platform family, currently serving millions of pupils, as
unlicensed.

🟢 **It is alive, and the evidence is the commit log rather than a badge.** `entcore` at
**2026-10-20** — the day before this pass — with **21 distinct authors** in a 200-commit
window and modal commit domains `edifice.io` (128) and `web-education.net` (29). Édifice is
the vendor's current brand; Open Digital Education and `web-education.net` are its former
ones, which is why all three appear in one author set.

🟡 **Three addresses, two repositories, and one is stale.** `edificeio/entcore` and
`opendigitaleducation/entcore` serve an **identical 158-ref list** — one repository under
two names. `OPEN-ENT-NG/entcore` is a **single-branch live mirror**, one commit behind.
🔴 `open-ent/entcore` last moved **2026-06-01** and should not be cloned. 🟢 **Use
`edificeio/entcore`.**

🔴 **The documentation hazard, stated because it changes an estimate.** The `entcore`
README specifies **JSE 7** and a clone URL at `code.web-education.net`. The code is current;
the README is roughly a decade old. 🟢 Price discovery from the source tree. 🔴 An estimate
built by reading the README will be wrong in the expensive direction.

🟡 **Licence reach is the architectural constraint.** The whole tier is **AGPL-3.0**, so
a fork carries network-copyleft into whatever a client deploys. 🟢 `entcore` is a *modular
kernel with its own HTTP API and module boundary*, which is the boundary to build on — see
`compose/patterns.md` for the ENT pattern. 🔴 Forking a module is the expensive mistake here.

## Interoperability — LTI, SCORM, xAPI, Caliper

The layer that lets an agent talk to a client's existing LMS without a bespoke
connector. Almost entirely permissive, which is why this tier is the cheapest place
to start.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Tsugi (LTI tool host) | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | `master/LICENSE` | **376** | North America |
| scorm-again (SCORM runtime) | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | `master/LICENSE` | **356** | Not placed |
| Marsha (LTI LCMS) | [openfun/marsha](https://github.com/openfun/marsha) | **MIT** | `master/LICENSE` | **150** | EMEA |
| ltijs (LTI 1.3, Node) | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | `master/LICENSE` | **373** | Not placed |
| pylti1.3 (LTI 1.3, Python) | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | `master/LICENSE` | **138** | Not placed |
| lti-tool | [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) | **MIT** | `main/LICENSE` | **8** | Not placed |
| ltikit-sdk | [Liberate-Labs/ltikit-sdk](https://github.com/Liberate-Labs/ltikit-sdk) | **MIT** | `main/LICENSE` | **0** | Not placed |
| django-lti-toolbox | [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | **MIT** | `master/LICENSE` | **14** | EMEA |
| CACCL (Canvas app framework) | [harvard-edtech/caccl](https://github.com/harvard-edtech/caccl) | **MIT** at `main` — 🔴 **and NO grant at `1.0.59`, its only tag** (`p365`) | `main/LICENSE.md` | **35** | North America |
| ltiauthenticator | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | BSD-3-Clause | `main/LICENSE` | **73** | North America |
| Caliper analytics spec | [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS specification licence — NOT OSI** | `master/LICENSE.md` | **22** | North America |
| 🆕 lti-core (LTI 1.3, TypeScript) | [iamlucasb/lti-core](https://github.com/iamlucasb/lti-core) | **MIT** (holder *Lucas Bossard*, 2026) | `main/LICENSE` | **1** | Not placed |
| 🆕 Ltix (LTI 1.3, **Elixir**) | [DecoyLex/ltix](https://github.com/DecoyLex/ltix) | **MIT** (holder *Alex Wilson*, 2025) | `main/LICENSE` | **2** | Not placed |
| 🆕 lti-node-library | [SanDiegoCodeSchool/lti-node-library](https://github.com/SanDiegoCodeSchool/lti-node-library) | **MIT** (holder *San Diego Code School*, **2019**) | `master/LICENSE` | **30** | North America |
| 🆕 ltijs — **fork** | [edugatorlabs/ltijs](https://github.com/edugatorlabs/ltijs) | Apache-2.0 | `master/LICENSE` | **0** | Not placed |

### 🟢 Choosing an LTI library is a four-way decision, and this pass can finally make it

🔵 **The standard is not one thing.** "LTI 1.3 support" can mean the OIDC launch alone,
or it can include **Deep Linking** (the tool puts content back into the LMS course),
**AGS** (the tool writes grades) and **NRPS** (the tool reads the roster). A library that
does launches only cannot submit a grade, and that is the capability an education
engagement almost always needs.

| Library | Runtime | Grant | Beyond launch | When to reach for it |
|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Node | Apache-2.0 | Deep Linking, grades, roles | 🟢 **The default.** The most complete permissive tool provider on this shelf. 🟡 Its README describes v7 as a full rewrite — pin a version |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | Python | MIT | Deep Linking, AGS, NRPS | 🟢 The default when the agent is Python, which on this base it usually is |
| 🆕 [`iamlucasb/lti-core`](https://github.com/iamlucasb/lti-core) | TypeScript, framework-agnostic | MIT | Deep Linking **2.0**, JWKS | 🟢 When the deliverable is typed end-to-end. 🟡 **RS256 keys only**, and its own docs say the library *"never decides who may configure content"* — the tool must enforce that authorisation itself |
| 🆕 [`DecoyLex/ltix`](https://github.com/DecoyLex/ltix) | **Elixir** | MIT | Deep Linking + other Advantage services | 🔵 Narrow but genuinely new ground: the first BEAM-runtime LTI row on this base. Relevant where a client already runs Phoenix |
| 🆕 [`SanDiegoCodeSchool/lti-node-library`](https://github.com/SanDiegoCodeSchool/lti-node-library) | Node | MIT (2019) | 🔴 **none** — its README states NRPS and Deep Linking are **not supported** | 🔴 **Launch-only, and seven years old.** Published as a row so a successor finding it in the same leg does not mistake it for an alternative to `ltijs` |

🔴 **Two LTI addresses in this pass's leg are on the flag table instead, and neither for
a reason the landing page shows.**
[`GSU-CETLOE/lti1p3Library-php`](https://github.com/GSU-CETLOE/lti1p3Library-php) is the
cleanest *small* library found — tool-side Deep Linking 2.0, AGS and NRPS, no framework
dependency, published by a university — and its MIT holder line is the **unfilled
template**, `Copyright (c) 2026 [Your Name / Organization]`. There is nobody to
attribute, and attribution is MIT's only condition.
[`oat-sa/lib-lti1p3-deep-linking`](https://github.com/oat-sa/lib-lti1p3-deep-linking) is
**IMS-certified** and **GPL-2.0**.

🔴 **An instrument defect in this pass, published because the error ran in the safe
direction only by luck.** `p358`'s probe first classified the OAT library as **LGPL**.
The payload's first line is `GNU GENERAL PUBLIC LICENSE / Version 2, June 1991` — it is
GPL-2.0 — and the misread happened because **GPL-2.0's own preamble names the Lesser
GPL** (*"use the GNU Lesser General Public License instead"*), which a grep ordered to
test for "LESSER" before "GENERAL" matches first. 🔵 The consequence is the wrong
direction for an engagement: on a **library**, LGPL permits dynamic linking and GPL-2.0
does not, so a false LGPL **understates** copyleft reach on exactly the component type
where the distinction decides the architecture. Fixed by reading the version line rather
than the preamble, and recorded as **`ACTION ZZ-bg`**: any payload classifier on this
base must key on the licence's **title and version line**, never on a keyword that can
appear in another licence's prose.

🟡 **`edugatorlabs/ltijs` is a fork of `Cvmcosta/ltijs`, same Apache-2.0 grant.** Apache
boilerplate carries no holder field, so the `ZZ-bc` holder test cannot separate fork from
upstream here — 🔵 a measured limit of that test, not a result: **the divergent-holder
check works on MIT and BSD rows and is blind to Apache ones.** Use `Cvmcosta/ltijs`.

## 🆕 Learning records and rostering — where the data lands

🔵 **The gap this fills.** The tier above lets an agent *reach* a client's LMS. It said
nothing about where learning events are **stored**, which is what an analytics,
adaptivity or evidence-of-impact deliverable actually reads from — and §2 of
`intel/trends.md` records evidence becoming a procurement gate. 🟢 **Every row below was
read from the payload this pass**, and 🟡 **all but one are permissive** — `p362`'s
addition, `educa-lrs`, is **AGPL-3.0** and is shelved anyway because it is the first LRS
on this base placed in **EMEA by its own vendor's commit channel** (`+0100` on 26 of 31
commits; `schule-plus.com` ×27 and `digitallearning.gmbh` ×1 on the `%ae` limb). 🔴 Read
it as an **API to reach, never a fork**: the network clause is the whole point of an LRS,
which is a service. 🔴 **And state its dormancy, because the tier's other rows are
active:** last commit **2025-11-13**, roughly eleven months cold.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| lrsql (SQL xAPI LRS) | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | `main/LICENSE` | **144** | North America |
| xapi-lrs (xAPI 1.0.3 **and 2.0**) | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | Apache-2.0 | `main/LICENSE` | **0** | Not placed |
| ADL_LRS (reference LRS) | [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | `master/LICENSE` | **334** | North America |
| Larissa (Apereo LRS) | [Apereo-Learning-Analytics-Initiative/Larissa](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa) | Apache-2.0 | `master/LICENSE` | **8** | North America |
| learnmcp-xapi (the MCP bridge) | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | `main/LICENSE` | **15** | Not placed |
| 🆕 OpenLRW (**OneRoster** + Caliper + xAPI) — 🟢 **canonical, corrected `p361`** | [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🟢 **ECL-2.0** (payload; 🔴 index classifier says `NOASSERTION`) | `master/LICENSE` | **62** | North America |
| 🔴 OpenLRW — *the fork `p359` shelved by mistake* | [jeffyding/OpenLRW](https://github.com/jeffyding/OpenLRW) | ECL-2.0 (inherited) | `master/LICENSE` | **0** | — |
| 🆕 educa LRS (xAPI, Laravel) — `p362` | [digital-learning-gmbh/educa-lrs](https://github.com/digital-learning-gmbh/educa-lrs) | 🔴 **AGPL-3.0** (33 889 B) | `main/LICENSE.md` | **4** | **EMEA** (Germany) |

### 🟡 Pick by conformance and maturity, because the licences do not separate these rows

🟢 **`pelotech/xapi-lrs` is the one to start from** — it is the only row whose README
claims conformance to **both xAPI 1.0.3 and xAPI 2.0**, it ships an admin UI and
OpenTelemetry metrics, and it is Apache-2.0 on `main`. 🟢 **`yetanalytics/lrsql` is the
safer choice where the client wants a boring datastore**: SQLite or Postgres, and its
copyright notice runs to 2026.

🔴 **Two rows carry their own disqualifiers in their own READMEs, and a successor should
not re-discover them.** `adlnet/ADL_LRS` — the *reference* implementation, updated to
**xAPI 2.0 / IEEE 9274.1.1** — scopes itself to proof-of-concept use with few users.
`Larissa` states it has **no OAuth and no attachment support**. 🔵 Both are correct
things to read a standard against and wrong things to put under a client's traffic.

### 🔴 OneRoster has one project, two addresses, and `p359` shelved the wrong one — corrected `p361`

🟢 **OpenLRW is the only project found that carries OneRoster, IMS Caliper and xAPI in a
single warehouse**, and its grant is clean: **ECL-2.0**, read from `master/LICENSE` —
Apache-2.0 with §3's patent grant narrowed to education use, which for redistribution
purposes behaves as Apache-2.0.

🔴 **`p359` shelved the wrong address for it, and `p361`'s ranked search is what caught
that.** The canonical upstream is
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
(**62 ★**, 25 forks). [`jeffyding/OpenLRW`](https://github.com/jeffyding/OpenLRW) is a
**fork at 0 ★**, created and last touched on the same day — 2018-01-19 — and the two
carry **different HEAD SHAs**. 🔵 **A non-ranked search cannot tell a fork from an
upstream; a ranked one puts 62 ★ above 0 ★ and the question answers itself.**

🔴 **And the index's own "recency" fields would have misled in the other direction.** On
the canonical: `updated_at` **2026-08-04**, `pushed_at` **2025-09-12**, 🟢 **last commit
on `master` 2020-02-06.** Three fields, three answers, a 6½-year spread, and only the
last one is a commit.

🔴 **Both addresses are stale, and every non-commit surface says otherwise.** A GitHub
**topic page** reports *"updated September 2025"*; the index reports `updated_at`
**2026-08-04**. 🟢 **Commit channel, first-hand: the fork ends 2018-01-16 (92 commits, 7
authors, from 2016-10-17); the canonical ends 2020-02-06.** 🔵 **A date that is not a
commit date is not a maintenance signal** — and `p361` widens that rule from topic pages
to the API's own `updated_at` and `pushed_at` fields, which are *metadata* and *any-ref
push* respectively, not commits.

🟢 **So the shelf gains a schema and not a dependency — and the correction does not
change that advice, only the address it points at.** The OneRoster↔Caliper↔xAPI
mapping in the canonical tree is the artefact worth reading. 🔴 **And the connector gap is
real and stated:** **no OneRoster MCP server exists** — `p359` probed the rostering leg
and found none — so an engagement that needs *"who is in this class"* writes that
connector. 🔵 It is the one interoperability standard on these shelves with no agent
connector at all, and it is the one every roster-aware deliverable needs first.

## 🆕 Psychometrics — the measurement layer, permissive and never shelved until now

🔵 **Why it belongs on a foundations shelf.** Every adaptivity and mastery claim on
these shelves — Bayesian Knowledge Tracing in `OATutor`, FSRS in `Smart-Study-Agent`,
"adaptive difficulty" in half the assessment tier — rests on item-response theory.
🔴 **This base had found these libraries at earlier passes and left them on
`agents/trending.md`.** `p359` promotes them, re-verified.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| 🆕 🟢 **irtorch** (IRT on PyTorch, GPU) | [joakimwallmark/irtorch](https://github.com/joakimwallmark/irtorch) | **MIT** | 🟡 `main/LICENSE.txt` | **18** | **EMEA** — `+0200`/`+0100` |
| 🆕 girth (IRT for Python) | [eribean/girth](https://github.com/eribean/girth) | **MIT** | 🟡 `master/LICENSE.txt` | **127** | **North America** — `-0500`/`-0400` |
| 🆕 girth_mcmc (Bayesian / MCMC IRT) | [eribean/girth_mcmc](https://github.com/eribean/girth_mcmc) | **MIT** | 🟡 `main/LICENSE.txt` | **19** | **North America** — `-0400`/`-0500` |
| 🆕 variational-IRT | [mhw32/variational-item-response-theory-public](https://github.com/mhw32/variational-item-response-theory-public) | **MIT** | `master/LICENSE` | **82** | **North America** — `-0700` |

### 🔴 Three of the four are abandoned, and the live one is not the one this base was pointing at

🟢 **The commit channel separates these rows where the licence does not.** Last commit,
read first-hand:

| Repo | Last commit | State |
|---|---|---|
| [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **2026-10-19 — two days before this pass** | 🟢 **Live. The only maintained permissive IRT engine found** |
| [`eribean/girth`](https://github.com/eribean/girth) | 🔴 2022-01-30 | 🔴 ~5 years stale |
| [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | 🔴 2021-11-10 | 🔴 ~5 years stale |
| [`mhw32/variational-item-response-theory-public`](https://github.com/mhw32/variational-item-response-theory-public) | 🔴 2020-05-28 | 🔴 ~6 years stale; paper companion code |

🔴 **This corrects a recommendation shape this base was carrying.** `girth` is the row
earlier passes named — it is the oldest, best-known and most-cited — and it has not been
touched in five years. 🟢 **`irtorch` is the row to build on**: MIT, PyTorch-backed with
GPU support, actively committed this week, and **EMEA-origin**, which makes it the only
psychometrics row that places in a region other than North America.

🔵 **Both halves of that matter to an engagement.** A stale MIT library is still legally
safe to vendor and *is* a defensible choice for a stable algorithm — IRT estimation is
not a moving target, and `girth` is a reasonable thing to pin. 🔴 **What it cannot do is
carry a client's security-patching expectations**, and a studio that lists it as a
"maintained dependency" in a proposal has mis-described it.

### 🔴 Three of the four put the grant at `LICENSE.txt`, and `girth`'s `LICENSE` is a 404

🟢 **Read first-hand this pass:** `eribean/girth` serves **404 at `master/LICENSE`** and
**200 at `master/LICENSE.txt`**. 🔵 **The whole permissive psychometrics family shares
that shape** — `girth`, `girth_mcmc` and `irtorch` all carry `LICENSE.txt` — so a probe
that tries `LICENSE` alone reports **the entire tier as grantless**, and every one of
them is stock MIT. 🟢 This is the shelf's existing default-branch warning in its other
form: **the filename is as load-bearing as the branch.**

### 🔴 What is NOT here: a licensed IRT-calibrated LLM grader

🔴 **Three 2026 papers pair IRT calibration with LLM short-answer grading** — including
*"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer
Grading via Item Response Theory"* — and `p359` could not find a usable implementation
behind any of them. The nearest code, [`mainlp/llm-psychometrics`](https://github.com/mainlp/llm-psychometrics),
is **live with no licence file at seven probed paths**. 🔴 The standard R package,
[`philchalmers/mirt`](https://github.com/philchalmers/mirt), carries **no root
`LICENSE`** at all — its grant is `License: GPL (>= 3)` in `DESCRIPTION`, the CRAN shape,
and it is copyleft when found.

🟢 **So the four rows above are calibration engines with no grading layer, and that is
the opportunity:** the join is **unbuilt**, both halves are MIT, and an engagement that
needs defensible difficulty estimates on AI-marked items builds it rather than buying
it — on **`irtorch`**, per the maturity table above, not on `girth`. 🔵 See §17 of `intel/trends.md` — AI marking has acquired a disclosure duty and a
measured anchoring bias, and an IRT-calibrated item is the evidence that answers both.

## Assessment, integrity and accessibility

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Judge0 (code execution API) | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | `master/LICENSE` | **4 492** | EMEA |
| Dolos (plagiarism detection) | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | `main/LICENSE` | **353** | EMEA |
| INGInious (exercise assessment) | [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 (*"most of the files"*) | `main/LICENSE` | **243** | EMEA |
| UDOIT (accessibility inspection) | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | GPL-3.0 | `main/LICENSE` | **117** | North America |
| Ares2 (secure grading runner) | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | **MIT** | `main/LICENSE` | **5** | EMEA |
| autograder — 🔴 **ARCHIVED** (`p361`) | [zmievsa/autograder](https://github.com/zmievsa/autograder) | GPL-3.0 | `main/LICENSE` | **48** | Not placed |

## Code execution, online judges and autograding — 🆕 a whole tier this base did not have

🟢 **This tier is `p356`'s finding and it is the largest single supply discovery on
this base.** `p354` recovered [`judge0`](https://github.com/judge0/judge0) by aiming a
leg at a **function** instead of at "AI education". `ACTION ZZ-ay` asked for that leg
shape to be run across nine functions. The `"online judge"` leg alone returned **62
repositories, 12 of them verified here, and all 12 absent from this base's entire
corpus** — `archive/` and `evidence/` included — with **7 137 ★** at the head.

🔵 **Why twelve passes of agent-shaped queries could not see it.** This software is
not called an AI tool and does not describe itself as one. It is the **grading
execution substrate** underneath every programming course: a sandbox, a queue, a
verdict. An education engagement that has to run student code needs exactly this and
would otherwise build it.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Hydro (multi-tenant judge) | [hydro-dev/Hydro](https://github.com/hydro-dev/Hydro) | AGPL-3.0 | `master/LICENSE` | **7 140** | APAC |
| QingdaoU OnlineJudge | [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | 🟢 **MIT** | `master/LICENSE` | **6 552** | APAC |
| HUSTOJ | [zhblue/hustoj](https://github.com/zhblue/hustoj) | GPL-2.0 | `master/LICENSE` | **3 813** | APAC |
| DMOJ (judge + contest platform) | [DMOJ/online-judge](https://github.com/DMOJ/online-judge) | AGPL-3.0 | `master/LICENSE` | **1 194** | North America |
| online-judge-tools | [online-judge-tools/oj](https://github.com/online-judge-tools/oj) | 🟢 **MIT** | `master/LICENSE` | **1 172** | APAC |
| DMOJ judge-server | [DMOJ/judge-server](https://github.com/DMOJ/judge-server) | AGPL-3.0 | `master/LICENSE` | **980** | North America |
| NOJ | [ZsgsDesign/NOJ](https://github.com/ZsgsDesign/NOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| HOJ | [HimitZH/HOJ](https://github.com/HimitZH/HOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| SYZOJ | [syzoj/syzoj](https://github.com/syzoj/syzoj) | 🟢 **MIT** | `master/LICENSE` | **922** | APAC |
| SDUOJ (microservices) | [SDUOJ/OnlineJudge](https://github.com/SDUOJ/OnlineJudge) | AGPL-3.0 | `main/LICENSE` | **556** | APAC |
| QingdaoU Judger (seccomp sandbox) | [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | 🔴 **SATA — MIT body + added obligations, NOT permissive** (1 823 B), corrected `p362` | 🔴 `newnew/LICENSE` | **496** | APAC |
| Sharif Judge (course-oriented) | [mjnaderi/Sharif-Judge](https://github.com/mjnaderi/Sharif-Judge) | **GPL-3.0** (35 146 B, no Affero title), corrected `p362` | 🔴 `Version-1/LICENSE` | **395** | EMEA |
| Otter-Grader (notebook autograder) | [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** | `master/LICENSE` | **161** | North America |
| webtech autograder | [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** | `main/LICENSE` | **62** | Not placed |
| OK client (Berkeley autograder) | [okpy/ok-client](https://github.com/okpy/ok-client) | 🟢 **Apache-2.0** | `master/LICENSE` | **57** | North America |
| 🆕 CodeSense (programming-education platform) — `p362` | [XiaoCow666/CodeSense](https://github.com/XiaoCow666/CodeSense) | 🟢 **MIT** (1 067 B) | `main/LICENSE` | **4** | APAC |

🟢 **Read the licence column as the engagement decision.** **Five** of the fifteen are
**MIT, BSD-3-Clause or Apache-2.0** — [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
at 6 552 ★ is a **complete, MIT-licensed, Docker-deployable judge**, re-read from payload
this pass at **1 085 B**. 🔵 Against this, `judge0` (GPL-3.0) has to be consumed over its
API to keep the boundary. **The permissive option in this tier is still the bigger one**,
which remains the reversal of the assumption the `judge0`-only shelf implied.

### 🔴 `p362`: the MIT judge everybody reaches for cannot execute code under an MIT grant

🔴 **The correction above is a row. This is the stack, and it is the finding.**
`QingdaoU/OnlineJudge` is a **multi-repository system**, and its own README names the
companions: *"Judger Sandbox(Seccomp)"* and *"JudgeServer(A wrapper for Judger)"*. 🔴
**Three of the five components were absent from this entire corpus** — this base had
shelved the two it had found by name and never asked what runs the code.

🟢 **All five read first-hand this pass, at their real default refs:**

| Component | Role | Licence (payload) | Bytes | Grant read at | ★ 2026-10-21 |
| --- | --- | --- | ---: | --- | ---: |
| [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | Django backend, contests, problem bank | 🟢 **MIT** | 1 085 | `master/LICENSE` | **6 552** |
| 🆕 [QingdaoU/OnlineJudgeFE](https://github.com/QingdaoU/OnlineJudgeFE) | Vue front end | 🟢 **MIT** | 4 334 | `master/LICENSE` | **330** |
| 🔴 🆕 [QingdaoU/JudgeServer](https://github.com/QingdaoU/JudgeServer) | the wrapper that actually executes submissions | 🔴 **SATA** | 1 823 | `master/LICENSE` | **209** |
| 🔴 [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | the seccomp sandbox | 🔴 **SATA** | 1 823 | `newnew/LICENSE` | **496** |
| 🔴 🆕 [QingdaoU/OnlineJudgeDeploy](https://github.com/QingdaoU/OnlineJudgeDeploy) | the documented `docker compose` deployment | 🔴 **no grant at any probed path** | — | `2.0` — none found | **591** |

🔴 **So the halves split by function, and the split is exactly the wrong way round for a
studio.** The components that **render pages** are MIT. The components that **run
untrusted student code** are SATA. And the manifest a client's ops team will actually
`git clone` — 591 ★, more than the sandbox — carries **no licence at all**, on `2.0`,
which is not `main` or `master` either.

🔵 **Measured, not inferred:** `JudgeServer`'s `Dockerfile` does `COPY Judger/ /app/` and
builds `libjudger.so` into `/usr/lib/judger/`, so the SATA sandbox is **vendored into**
the SATA wrapper; `OnlineJudgeDeploy`'s compose file runs that wrapper as the `oj-judge`
service from a published `judge:1.6.1` image. 🟢 `OnlineJudgeFE`'s 4 334 B is benign and
was read too: **three concatenated MIT notices** — its own, Vue's, and one more — which is
the fourth "excess explained" of this pass.

🟡 **What this changes for an engagement, concretely.** *"Fork `QingdaoU/OnlineJudge` into
a closed client deliverable"* remains true **of the web tier** and says nothing about
grading. A client that needs to run code gets one of three positions, and should pick
deliberately rather than discover it at review:

1. 🟡 **Honour SATA.** Its obligations are cheap — star the project, thank the authors in
   your notices, leave its copyright and project-url block intact — but it is **not OSI
   open source**, an SPDX scanner returns `NOASSERTION`, and a procurement checklist that
   says *"permissive only"* fails it.
2. 🟢 **Replace the executor.** `judge0` (GPL-3.0, over its API),
   [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (BSD-3-Clause,
   notebooks) and 🆕 [`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)
   (MIT, restricted execution + code evaluation, 554 commits) are all genuinely
   permissive — 🔴 none of them is a drop-in for a seccomp sandbox, so this is a build,
   not a swap.
3. 🟢 **Keep the execution tier outside the deliverable entirely**, reached over HTTP,
   which is the boundary `compose/patterns.md` Pattern 9 already uses for `judge0`.

🔴 **The general form, and it is why this is on the foundations shelf rather than in a
footnote: in this sector a platform's LICENSE file is a statement about one repository,
and the thing that does the dangerous work usually lives in another one.** Published as
`T30` on `intel/trends.md` and registered as `ACTION ZZ-bo`.

🔴 **The count fell from six to five this pass, and the row that left is the one the
permissive path leaned on.** [`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) was
published here as *"its seccomp sandbox on its own MIT grant"*. 🔴 **There is no MIT
grant.** Its payload at `newnew/LICENSE` is the **Star And Thank Author License**: MIT's
permission paragraph, then *"you shall star/+1/like the project(s) ... and then thank the
author(s)"*, plus a clause forbidding modification of the copyright and project-url
sections. 🔴 GitHub's own classifier reads the repository as **`NOASSERTION`**, so **no
channel ever said MIT** — the grant was inherited from the sibling `OnlineJudge`, which
really is MIT. 🟡 **What an engagement may still do:** the obligations are cheap to honour
(star the project, thank the authors in your notices, leave its copyright block intact)
and the sandbox is 292 KB of C. But it is **not OSI open source**, so it cannot go into
the permissive column, and a client whose counsel runs an SPDX scanner will get
`NOASSERTION` back. 🟢 **The permissive substitute measured this pass is
[`XiaoCow666/CodeSense`](https://github.com/XiaoCow666/CodeSense)** — MIT, 554 commits,
restricted execution plus code evaluation — shelved below.

🟡 **Two of the three non-contest rows matter most for a client.**
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) is built for
**programming courses** rather than contests — assignments, deadlines, per-student
feedback — and [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
grades **Python *and* R notebooks**, which is where this base's prior autograder
([`nbgrader`](https://github.com/jupyter/nbgrader), Jupyter-only) stopped.

🔴 **Two default branches in this tier are neither `main` nor `master`.**
`QingdaoU/Judger` defaults to **`newnew`** and `Sharif-Judge` to **`Version-1`**. A
licence sweep that probes `main` and `master` reports both as grantless.

🔵 **`p362` found the sharper version of that warning, and it is the opposite shape.**
Both of those odd refs *were* probed, and both cells recorded the right **path** and the
wrong **family** — `Judger` as MIT when the payload is SATA, `Sharif-Judge` as AGPL-3.0
when the payload is the plain GPLv3 text (*"GNU GENERAL PUBLIC LICENSE, Version 3, 29
June 2007"*, 35 146 B, identical at `master`). 🔴 **So finding the grant is not reading
it**, and a path column that says `200` says nothing about the family in the bytes.

## 🆕 `p364`: the DEPLOYMENT tier — components named by a platform's own README, graded by payload

🔴 **Every other tier on this shelf grades a platform. This one grades what a platform
makes you install.** `ACTION ZZ-bo` (opened `p362` on the `QingdaoU/OnlineJudge` specimen)
asked a question no instrument here had asked: *does the headline grant govern the
components?* `p364` read the README of all **60** addresses on `verticals/solutions.md`,
extracted the **91** GitHub addresses they name, and graded the **69** this base did not
hold. Full population in
[`companion-population`](../evidence/companion-population.2026-10-21-p364.tsv); grants and
the per-row verdict against the host's published cell in
[`companion-grants`](../evidence/companion-grants.2026-10-21-p364.tsv).

### 🟢 JupyterHub's spawner and authenticator tier — 11 components, all BSD, none previously held

🟢 **A class cluster is never just `jupyterhub`.** It is the core plus a **spawner** (how a
student's notebook process is started) plus an **authenticator** (how the LMS signs them
in). All eleven are permissive, which makes this the one platform family on these shelves
where a closed client deliverable survives the deployment and not just the core.

| Component | Repo | Licence (payload, `2026-10-21`) | Default ref | What it decides |
|---|---|---|---|---|
| **kubespawner** | [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | one Kubernetes pod per student — the shape of every cohort-scale teaching cluster |
| **dockerspawner** | [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | one container per student on a single host; the cheap classroom |
| **systemdspawner** | [jupyterhub/systemdspawner](https://github.com/jupyterhub/systemdspawner) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | per-student resource limits with no container runtime at all |
| **batchspawner** | [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | submits to Slurm/PBS — the route onto a university HPC allocation |
| **yarnspawner** | [jupyterhub/yarnspawner](https://github.com/jupyterhub/yarnspawner) | 🟢 **BSD** (`LICENSE`, 1 492 B) | `master` | Hadoop/YARN clusters; data-engineering curricula |
| **sudospawner** | [jupyterhub/sudospawner](https://github.com/jupyterhub/sudospawner) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | privilege separation without running the hub as root |
| **wrapspawner** | [jupyterhub/wrapspawner](https://github.com/jupyterhub/wrapspawner) | 🟢 **BSD** (`LICENSE`, 1 557 B) | `master` | lets a student *choose* a profile at launch |
| **oauthenticator** | [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | Google/Azure/GitHub sign-in — the usual institutional identity route |
| **ldapauthenticator** | [jupyterhub/ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `main` | the on-premise directory most schools actually run |
| **kerberosauthenticator** | [jupyterhub/kerberosauthenticator](https://github.com/jupyterhub/kerberosauthenticator) | 🟢 **BSD** (`LICENSE`, 1 492 B) | `main` | Kerberos estates, common in HPC and older universities |
| **jupyterhub-tutorial** | [jupyterhub/jupyterhub-tutorial](https://github.com/jupyterhub/jupyterhub-tutorial) | 🟢 **BSD** (`LICENSE`, 1 528 B) | `master` | 🟡 teaching material, not a component — shelved for completeness of the README's population |

🔵 **A payload-identity observation, free from the measurement:** **7 of these 11 ship a
byte-identical 1 528 B payload**, with the remaining four at 1 492/1 557 B. That is
`gate-payload-digest`'s axis (`ACTION ZZ-ad`) answering in the affirmative on a tier nobody
pointed it at — one organisation-wide grant, reproduced, rather than eleven decisions.
🟡 **The classifier returns the family UNVERSIONED (`BSD`, not `BSD-3-Clause`)** and this
shelf publishes what was read; the core row on `verticals/solutions.md` carries
`BSD-3-Clause` from an earlier pass, so the version is asserted there and not here.

### 🟡 Permissive components under a copyleft platform — the direction that is safe

🟢 **Worth stating because it is the opposite of the Marsha finding and equally useful:** a
copyleft platform can ship permissive pieces, and those pieces are reachable on their own.

| Component | Repo | Licence (payload) | Host platform (published grant) | Why it matters alone |
|---|---|---|---|---|
| **frappe-ui** | [frappe/frappe-ui](https://github.com/frappe/frappe-ui) | 🟢 **MIT** (`license.md`, 1 101 B) | `frappe/lms` **AGPL-3.0**, `frappe/erpnext` **GPL-3.0** | the Vue component library — usable in a closed front end against either platform's REST API |
| **payments** | [frappe/payments](https://github.com/frappe/payments) | 🟢 **MIT** (`license.txt`, 1 118 B) | `frappe/lms` **AGPL-3.0** | course-fee collection, detachable from the AGPL core |
| **frappe_docker** | [frappe/frappe_docker](https://github.com/frappe/frappe_docker) | 🟢 **MIT** (`LICENSE`, 1 086 B) | `frappe/erpnext` **GPL-3.0** | the supported deployment path, permissively granted |
| **judge0-js / judge0-python** | [judge0/judge0-js](https://github.com/judge0/judge0-js) · [judge0/judge0-python](https://github.com/judge0/judge0-python) | 🟢 **MIT** (1 070 B / 1 063 B) | `judge0/judge0` **GPL-3.0** | 🟢 the official clients are MIT, so the *API boundary* this base already recommends for Judge0 is now granted on both sides rather than only on the server's |
| **elearning-module-parser** | [jcputney/elearning-module-parser](https://github.com/jcputney/elearning-module-parser) | 🟢 **Apache-2.0** (`LICENSE`, 11 314 B) | `jcputney/scorm-again` **MIT** | parses SCORM/AICC/cmi5 packages on the server; pairs with the MIT browser runtime |
| **openedx/.github** | [openedx/.github](https://github.com/openedx/.github) | 🟢 **Apache-2.0** (`LICENSE.txt`, 11 359 B) | `openedx/openedx-platform` **AGPL-3.0** | 🟡 org metadata, not code — shelved so the AGPL tier's population is complete |

🔴 **And the ones that run the other way,** each verified from payload:
`frappe/press` **AGPL-3.0** (`develop/license.txt`, 34 523 B) under a **GPL-3.0** platform —
it is the hosting control plane, so a studio *operating* ERPNext as a service is the exact
case AGPL is written for; `openfun/xblock-configurable-lti-consumer` **AGPL-3.0** under an
**MIT** platform (the Marsha correction, in `verticals/solutions.md`);
`dmoj/runtimes-docker` **AGPL-3.0**; `inginious/demo-tasks` **AGPL-3.0**;
`overhangio/indigo`, `overhangio/openedx-scorm-xblock`, `overhangio/tutor-android` all
**AGPL-3.0** at `LICENSE.txt`, consistent with Tutor's own grant.

### 🔴 `ioi/isolate` — the sandbox under the sandbox, GPL-2.0, 583 B

🔴 **Judge0's README names 20 third-party repositories and 19 of them are adopters, not
dependencies.** The twentieth is [`ioi/isolate`](https://github.com/ioi/isolate) —
**GPL-2.0**, `master/LICENSE`, **583 B** — the IOI's process isolator and the thing that
actually confines student code underneath Judge0. 🔵 It does not change this base's Judge0
advice (reach it as a service over HTTP and the boundary holds) but it does extend it: the
boundary has **two** copyleft layers behind it, and a studio that chooses to *vendor* the
execution tier rather than call it inherits GPL-3.0 **and** GPL-2.0.

---

## Content authoring, media and delivery

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| JupyterHub | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause | `main/LICENSE` | **8 361** | North America |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `v4.0.x-develop/LICENSE` | **9 249** | North America |
| pytogether (collaborative IDE) | [SJRiz/pytogether](https://github.com/SJRiz/pytogether) | **MIT** | `main/LICENSE` | **261** | Not placed |
| Opencast (lecture capture) | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** | `develop/LICENSE` | **509** | EMEA |
| H5P core | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | `master/LICENSE.txt` | **151** | EMEA |
| H5P CLI | [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | 🟢 **MIT** | `master/LICENSE` | **78** | EMEA |
| Hyperbook | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | **MIT** | `main/LICENSE.md` | **74** | EMEA |
| yanki (markdown → Anki) | [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | 🟡 **MIT, `package.json` only** | `main/package.json` — 🔴 *no licence file in tree* | **61** | Not placed |

🟢 **H5P is a split grant worth knowing:** the core library is GPL-3.0 but
[`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) is **MIT**. Tooling built against
the CLI carries no copyleft; code linked into the library does.

## Administration — SIS, ERP, credentials

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| OpenEduCat (education ERP) | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `19.0/LICENSE` | **893** | APAC |
| RosarioSIS (student info system) | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | `mobile/LICENSE` | **647** | EMEA |
| Learner Credential Wallet | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | **MIT** | `main/LICENSE` | **89** | Global |
| Terracotta (in-LMS experiments) | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | Apache-2.0 | `development/LICENSE` | **21** | North America |
| 🆕 openSIS Classic (K-12 SIS) | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 | 🔴 `master/docs/License.txt` — **root carries no grant file** | **346** | Not placed |
| 🆕 FenixEdu Academic (HE SIS) | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | `master/LICENSE` | **175** | EMEA |
| 🆕 🟢 **Academico** (school management / SIS) | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** | `main/LICENSE` | **408** | EMEA |
| 🆕 ERPNext (institution-wide ERP) | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** | 🔴 `develop/license.txt` — **lower-case path on a non-`main` default branch** | **40 419** | APAC |

### 🔴 `ERPNext` fails both of this base's grant hazards at once, and it is the row most likely to be reached for

🟢 **`p357` adds it because `frappe/lms` is already on the LMS tier and ERPNext is the
other half of that stack** — an institution running Frappe LMS for teaching and ERPNext
for finance, HR and procurement is a single-vendor deployment a studio will meet.

🔴 **It is also a clean reproduction of the two hazards this base keeps measuring.** Its
default branch is **`develop`**, not `main`, and its grant sits at **`license.txt`**,
lower-case. A probe assuming `main/LICENSE` reports this repository — one of the
largest open-source ERPs in existence — as **grantless**. 🔵 That is the
`frappe/lms` shape exactly, from the same organisation, which is the useful part: the
hazard is an **organisational convention**, not a per-repository accident. Where one
Frappe repository hides its grant this way, assume all of them do.

🔴 **And the licence is the engagement constraint.** GPL-3.0, not the AGPL of
`frappe/lms` and not the LGPL-3.0 of `openeducat_erp`. 🟢 So an institution-wide Frappe
stack spans **three different copyleft strengths**, and a deliverable's obligations
depend on which component it links — which is why
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0,
linking permitted) remains this shelf's recommended ERP base for closed work.

### 🔴 The permissive education ERP this leg promised does not exist at the address given

🟢 **The leg was run because a permissive ERP would be the single most valuable row on
this tier** — every ERP and SIS this base carries is copyleft (LGPL-3.0, GPL-2.0,
GPL-3.0, AGPL-3.0), so an engagement that must ship a closed admin deliverable has no
base to fork. A vendor comparison in this pass's leg named two:

| Claimed | Claimed licence | What `p357` found |
|---|---|---|
| **Fedena** ([`foradian/fedena`](https://github.com/foradian/fedena)) | Apache-2.0, Ruby on Rails | 🔴 **Live on `master` and empty.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license.txt`, `LICENCE`, `LICENSE-MIT`, `README.md` and `Gemfile` **all 404**. The claim is unverifiable at this address |
| **GegoK12** (`gegok12/gegok12`) | MIT, *"twenty-six modules free forever"* | 🔴 **No such repository** — `ls-remote` returns nothing. The claim traces to a vendor website, not to a public tree |
| **SchoolTool** (`schooltool/schooltool`) | GPL-2.0, per a comparison table | 🔴 **Dead.** No substitute found under that owner |

🔵 **Published as a refutation rather than omitted, for one reason.** All three claims
sit in roundups that rank well and read authoritatively, and a later pass searching
"permissive education ERP" will meet them again. 🟢 **The honest finding is the
absence:** on this base's evidence there is **no verified permissive education ERP**, so
a closed admin deliverable is a **build**, not a fork — and that is a costing input, not
a gap in the research.

🟢 **`openSIS-Classic`'s grant was RECOVERED this pass, and `p354` predicted the exact
shape.** Six root rungs (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`,
`license.txt`, `GNU-AGPL-3.0.txt`) all answer **404**; the README names
`docs/License.txt`, and that path returns **17 286 bytes of GPL-2.0, BOM-prefixed**.
🔴 **Two corrections ride on reading it rather than the README:** the README says only
*"the GNU General Public License"* with no version, and the payload is **Version 2, not
Version 3** — which decides compatibility — while the leading **UTF-8 BOM** means a
classifier anchored on `^GNU` sees no match at all.

## Curriculum corpora and open courseware

| Asset | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| freeCodeCamp | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | BSD-3-Clause | `main/LICENSE.md` | **457 613** | North America |
| Open Source Society CS | [ossu/computer-science](https://github.com/ossu/computer-science) | **MIT** | `master/LICENSE` | **210 188** | Global |
| MCP for Beginners | [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | **MIT** | `main/LICENSE` | **17 486** | North America |
| openunivcourses | [kabartay/openunivcourses](https://github.com/kabartay/openunivcourses) | **MIT** | `main/LICENSE` | **253** | Not placed |
| elimu.ai literacy webapp | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | **MIT** | `main/LICENSE` | **41** | EMEA |
| UIUC systems coursebook | [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | 🔴 **NCSA** (code) + **CC-BY-4.0** (built PDFs) | `master/LICENSE/README.md` — 🔴 🔴 **`LICENSE/` is a DIRECTORY** — see `LICENSE/README.md` | **3 849** | North America |

🔴 **`cs341-illinois/coursebook` is this shelf's sharpest grant trap.** `LICENSE` is
not a file, it is a **directory**. Inside, `LICENSE/README.md` states three different
grants: NCSA for code contributions (`LICENSE.code`), CC-BY-4.0 for the generated
PDFs, and the original wikibook's licence for remixed material (`LICENSE.original`).
A previous pass on this base published this row as **MIT**. It is not MIT. NCSA is
permissive and usable, but it must be named correctly.

---

## 🆕 Research corpora and simulated learners — the substrate a tutoring claim is tested against, `p363`

🔵 **This tier is not software to deploy; it is what you measure a deployment with.** A
tutoring engagement that cannot say *"this tutor was evaluated against N learners on
move-level pedagogy"* has no evidence to put in front of a client, and `p363` found the
permissive substrate for exactly that claim.

| Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | Role in a build |
|---|---|---|---:|---|---|
| [microsoft/StudentSim](https://github.com/microsoft/StudentSim) | MIT (`LICENSE`, 1 074 B, `sha256:7df20dcdf919`) | `main/LICENSE` | **77** | North America | **Simulated learner.** Iterate tutoring policy without a human cohort per experiment; recruit humans once, to confirm |
| [iwangjian/Coding-Tutor](https://github.com/iwangjian/Coding-Tutor) | Apache-2.0 (`LICENSE`, 11 357 B, `sha256:c71d239df917`) | `main/LICENSE` | **91** | APAC | **Turn-level verifier.** Scores the tutor's *next move*; ACL 2025 Findings |
| [yale-nlp/LLM-Metacognition](https://github.com/yale-nlp/LLM-Metacognition) | MIT (`LICENSE`, 1 065 B, `sha256:5ea7fdc0c957`) | `main/LICENSE` | **80** | North America | **Calibration / "I don't know".** Gates a tutor from asserting into a gap |
| [eth-nlped/mathdial](https://github.com/eth-nlped/mathdial) | 🟡 **CC-BY-SA-4.0 — README prose only, no `LICENSE` file** | `main/README.md` L96–97 | **95** | EMEA — Switzerland | **Pedagogically annotated dialogue corpus.** The only source on this base for *which teaching move was made*. 🟡 Share-alike binds derived datasets |
| [eth-nlped/socratic-generation](https://github.com/eth-nlped/socratic-generation) | 🟡 **CC-BY-4.0 — `rel="license"` markup only** | `main/README.md` L67 | **25** | EMEA — Switzerland | **Scaffolding-question generation** (REINFORCE), EMNLP 2022 |

🔴 **Three sibling repositories from the same lab carry no grant at all** —
[`mathworld`](https://github.com/eth-nlped/mathworld) (ACL Findings 2023),
[`dialog-tutoring`](https://github.com/eth-nlped/dialog-tutoring) (EACL 2023),
[`textbook-enrichment`](https://github.com/eth-nlped/textbook-enrichment) — probed at 11
licence paths each, all `404`
([`no-grant-path-sweep`](../evidence/no-grant-path-sweep.2026-10-21-p363.tsv)).
🟢 **One email to a named lab is the cheap fix; rebuilding `MathDial` is not.**

## Carried inventory — re-verified this pass, not promoted to the tiers above

🟢 **72 addresses, every one re-probed first-hand 2026-10-21 and every one ALIVE.** These
were held on this base's shelves from earlier passes. This pass's rewrite of the curated
tiers would have dropped them, and the `fold-identity` gate caught it — so rather than
lose verified work, they are restored here with their grants **re-read from the payload
today**, not carried on trust.

🔴 **20 of the 72 carry no grant file at the repository root on the default branch.**
Absent a licence, the default is all-rights-reserved: these are **not** usable in client
work however public the code is. Most are research artefacts from the OpenEduHub estate.

**OpenEduHub / WirLernenOnline — the largest single open-education engineering estate found on this base (EMEA, Germany)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openeduhub/duplicate-detection](https://github.com/openeduhub/duplicate-detection) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/edu-sharing-python-client](https://github.com/openeduhub/edu-sharing-python-client) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/its-data](https://github.com/openeduhub/its-data) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-jointprobability](https://github.com/openeduhub/its-jointprobability) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-prep](https://github.com/openeduhub/its-prep) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-qna](https://github.com/openeduhub/its-qna) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/ki-prompt-benchmark](https://github.com/openeduhub/ki-prompt-benchmark) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/lernpfadeditor](https://github.com/openeduhub/lernpfadeditor) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/llm-judge](https://github.com/openeduhub/llm-judge) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/mappings](https://github.com/openeduhub/mappings) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/metadata-agent-api](https://github.com/openeduhub/metadata-agent-api) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-agent-canvas](https://github.com/openeduhub/metadata-agent-canvas) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-browser-plugin-fuerapi](https://github.com/openeduhub/metadata-browser-plugin-fuerapi) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/metalookup](https://github.com/openeduhub/metalookup) | GPL-3.0 | `main/LICENSE.txt` |
| [openeduhub/oeh-metadata-vocabs](https://github.com/openeduhub/oeh-metadata-vocabs) | CC | `master/LICENSE` |
| [openeduhub/oeh-search-etl](https://github.com/openeduhub/oeh-search-etl) | 🔴 **no grant at root** | `master/` — none found |
| [openeduhub/oeh-search-frontend](https://github.com/openeduhub/oeh-search-frontend) | 🔴 **no grant at root** | `develop/` — none found |
| [openeduhub/python-kidra](https://github.com/openeduhub/python-kidra) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/skohub-vocabs-oeh-patched](https://github.com/openeduhub/skohub-vocabs-oeh-patched) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/text-extraction](https://github.com/openeduhub/text-extraction) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/text-statistics](https://github.com/openeduhub/text-statistics) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/topic-statistics](https://github.com/openeduhub/topic-statistics) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/tutor-chatbot](https://github.com/openeduhub/tutor-chatbot) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/wlo-quellenliste](https://github.com/openeduhub/wlo-quellenliste) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/z-api-runner](https://github.com/openeduhub/z-api-runner) | 🔴 **no grant at root** | `master/` — none found |

**Open edX ecosystem (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openedx/frontend-base](https://github.com/openedx/frontend-base) | AGPL-3.0 | `main/LICENSE` |
| [openedx/frontend-platform](https://github.com/openedx/frontend-platform) | AGPL-3.0 | `master/LICENSE` |
| [openedx/openedx-proposals](https://github.com/openedx/openedx-proposals) | CC | `master/LICENSE` |

**France Université Numérique (EMEA, France)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openfun/ashley](https://github.com/openfun/ashley) | **MIT** | `master/LICENSE` |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** | `main/LICENSE.md` |

**D2L Brightspace, first-party (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [Brightspace/test-reporting-node](https://github.com/Brightspace/test-reporting-node) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/core](https://github.com/BrightspaceUI/core) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/intl](https://github.com/BrightspaceUI/intl) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/labs](https://github.com/BrightspaceUI/labs) | **Apache-2.0** | `main/LICENSE` |

**LTI libraries, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [adamzammit/ltiplugin](https://github.com/adamzammit/ltiplugin) | GPL-3.0 | `master/LICENSE` |
| [annoto/ims-lti](https://github.com/annoto/ims-lti) | **MIT** | `master/LICENSE` |
| [godmartinz/node-lti-1.3-library](https://github.com/godmartinz/node-lti-1.3-library) | 🔴 **no grant at root** | `master/` — none found |
| [longsightgroup/lti-tool](https://github.com/longsightgroup/lti-tool) | **MIT** | `main/LICENSE` |
| [scormflow/scorm-engine-client](https://github.com/scormflow/scorm-engine-client) | **MIT** | `main/LICENSE` |

**Curriculum knowledge graphs**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [mizcausevic-dev/curriculum-knowledge-graph](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** | `main/LICENSE` |
| [oseducation/knowledge-graph](https://github.com/oseducation/knowledge-graph) | 🔴 **no grant at root** | `main/` — none found |
| [razi-03/ncert-ckg](https://github.com/razi-03/ncert-ckg) | 🔴 **no grant at root** | `main/` — none found |

**Privacy, de-identification and synthetic data — the compliance toolkit for education data**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [arx-deidentifier/arx](https://github.com/arx-deidentifier/arx) | **Apache-2.0** | `master/LICENSE` |
| [greenmaskio/greenmask](https://github.com/greenmaskio/greenmask) | **Apache-2.0** | `main/LICENSE` |
| [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) | **Apache-2.0** | `main/LICENSE` |
| [meta-pytorch/opacus](https://github.com/meta-pytorch/opacus) | **Apache-2.0** | `main/LICENSE` |
| [OpenMined/PyDP](https://github.com/OpenMined/PyDP) | **Apache-2.0** | `dev/LICENSE` |
| [rizzo-ai-academy/rizzo-pii](https://github.com/rizzo-ai-academy/rizzo-pii) | **MIT** | `main/LICENSE` |
| [securitybunker/databunker](https://github.com/securitybunker/databunker) | **MIT** | `master/LICENSE` |
| [synthetichealth/synthea](https://github.com/synthetichealth/synthea) | **Apache-2.0** | `master/LICENSE` |
| [thoughtbot/top_secret](https://github.com/thoughtbot/top_secret) | **MIT** | `main/LICENSE.txt` |

**Courseware and curriculum corpora, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [freeCodeCamp/curriculum-helpers](https://github.com/freeCodeCamp/curriculum-helpers) | **BSD** | `main/LICENSE` |
| [h5p/h5p-interactive-video](https://github.com/h5p/h5p-interactive-video) | 🔴 **no grant at root** | `master/` — none found |
| [openki/openki](https://github.com/openki/openki) | AGPL-3.0 | `dev/LICENSE` |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | **MIT** | `main/LICENSE` |
| [weecology/forecasting-course](https://github.com/weecology/forecasting-course) | CC | `main/LICENSE.md` |

**Learning agents, tutors and tooling, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [010ankushsharma/adaptalearn](https://github.com/010ankushsharma/adaptalearn) | 🔴 **no grant at root** | `master/` — none found |
| [chrischall/gogcli-mcp](https://github.com/chrischall/gogcli-mcp) | **MIT** | `main/LICENSE` |
| [christophblessing/quiz-recap](https://github.com/christophblessing/quiz-recap) | **MIT** | `main/LICENSE` |
| [damphuquy/agent-as-a-tutor](https://github.com/damphuquy/agent-as-a-tutor) | **MIT** | `main/LICENSE` |
| [dymchenkko/claude-study-agent](https://github.com/dymchenkko/claude-study-agent) | **MIT** | `main/LICENSE` |
| [groton-school/canvas-cli](https://github.com/groton-school/canvas-cli) | GPL-3.0 | `main/LICENSE` |
| [ibenian/algebench](https://github.com/ibenian/algebench) | **MIT** | `main/LICENSE` |
| [kyyota-wang/cloverailab](https://github.com/kyyota-wang/cloverailab) | 🔴 **no grant at root** | `main/` — none found |
| [lucasspinola/assistentes-educacionais-com-ia](https://github.com/lucasspinola/assistentes-educacionais-com-ia) | **MIT** | `main/LICENSE` |
| [molecule-dev/molecule](https://github.com/molecule-dev/molecule) | **Apache-2.0** | `main/LICENSE` |
| [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | 🔴 **no grant at root** | `main/` — none found |
| [muhammedalakbarli/imparo](https://github.com/muhammedalakbarli/imparo) | **MIT** at `main` — 🔴 **and `pilot-v1.0` is "All Rights Reserved", proprietary** (`p365`) | `main/LICENSE` |
| [nichochar/ari](https://github.com/nichochar/ari) | **MIT** | `main/LICENSE` |
| [risnake/canvas-mcp-server](https://github.com/risnake/canvas-mcp-server) | 🔴 **no grant at root** | `main/` — none found |
| [smashburger-dev/argmin](https://github.com/smashburger-dev/argmin) | **MIT** | `main/LICENSE` |
| [viendinhcom/supermemo](https://github.com/viendinhcom/supermemo) | **MIT** | `master/LICENSE` |

---

## 🟢 Alias correction applied this pass

[`openedx/edx-platform`](https://github.com/openedx/edx-platform) and
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) return the
**identical HEAD** `7f01c42157d30cc273c06d62448b6d5a26624495`. They are one
repository. The authenticated index returns **`openedx/openedx-platform`** as the
canonical name; this base has been publishing the stale one. The table above now
carries the canonical address.

## 🔵 Grant-path distribution, re-derived AFTER this pass wrote — which is what `gate-census-currency` is for

🟢 Derived over the curated tiers of **this** tree, as the last act before the commit,
not carried from `p355`'s sentence:

| Grant filename | Rows on this shelf |
|---|---:|
| `LICENSE` | 51 |
| `LICENSE.md` | 5 |
| 🔴 `COPYING.txt` | 2 — `moodle/moodle`, `moodlehq/moodleapp` |
| `LICENSE.txt` | 2 |
| 🔴 `license.txt` (lower-case) | **2** — `frappe/lms`, 🆕 `frappe/erpnext` |
| 🔴 a **directory** | 1 — `cs341-illinois/coursebook` |
| 🔴 `package.json` field only | 1 — `kitschpatrol/yanki` |
| 🔴 🆕 **`docs/License.txt`** | 1 — `OS4ED/openSIS-Classic` |

**14 of 65 grants (21.5 %) are not at `LICENSE`.** 🔴 **The share went UP again** —
`p355` published 6 of 41 (15 %), `p356` 13 of 64 (20.3 %), and `p357`'s single addition
raises it once more, which is the direction `T13` predicts.

🟢 **And `p357`'s one addition is the most instructive row on this table, because it
makes the hazard organisational rather than accidental.** The lower-case `license.txt`
bucket now holds **two rows and both are Frappe** — [`frappe/lms`](https://github.com/frappe/lms)
and 🆕 [`frappe/erpnext`](https://github.com/frappe/erpnext), each on a non-`main`
default branch (`develop` for both). 🔵 A grant path is not a per-repository quirk to
be rediscovered one repository at a time; **it is a house style**, and the operational
rule follows directly: when one repository in an organisation hides its grant, probe
that organisation's convention rather than the next repository's root.

### 🔴 And the default branch is the larger hazard

| Default branch | Rows |
|---|---:|
| `master` | **31** |
| `main` | 23 |
| `develop` | 3 |
| 🔴 each of `release`, `newnew`, `Version-1`, `v4.0.x-develop`, `19.0`, `mobile`, `development` | 1 |

🔴 **A probe that assumes `main` reports 41 of 64 grants (64.1 %) as absent**, and a
probe that tries `main` then `master` still misses **10**. Two of those ten are
[`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) (`newnew`) and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) (`Version-1`), both
added at `p356` — and `QingdaoU/Judger` was then the sandbox at the centre of Pattern 9's
permissive path. 🔴 **Corrected `p362`: that sandbox is SATA, not MIT**, so the clause
that used to read *"the MIT sandwich"* has been rewritten to name the repository instead
of leaving a licence token next to the wrong slug. 🔵 One cause explains copyleft
prevalence, grants at `COPYING.txt` and `docs/License.txt`, and non-`main` defaults
alike: **this sector's infrastructure is older than the conventions the tooling
assumes.** Published as `T13`.

🔵 **Why that rewrite is a gate repair and not a style edit.** `gate-shelf-consistency`
read the old sentence as this shelf publishing **`MIT` for `mjnaderi/Sharif-Judge`** —
the nearest slug to the token — and reported a disagreement with the `AGPL-3.0` cell on
`verticals/solutions.md`. 🟢 **The gate was right to fire and wrong about which cell was
broken**, which is `ACTION ZZ-av`'s shape (a figure or a family bound to a slug by
proximity) reproduced on the **licence** axis for the first time. 🟢 Both underlying cells
were wrong anyway, so the gate earned its RED twice over.

## 🔵 Regional placement, counted over this shelf's own cells

🟢 **Derived as the last act before the commit, and it corrects the sentence it
replaces.**

| Region | Placed rows (`p358`) | `p357` published | `p356` published |
|---|---:|---:|---:|
| **North America** | **20** | 19 | 19 |
| **EMEA** | 16 | 16 | 16 |
| **APAC** | 12 | 12 | 🔴 11 |
| Global | 7 | 7 | 7 |
| 🔵 Not placed | **14** | 🔴 11 | 🔴 11 |
| **LATAM** | 🔴 **0** | 0 | 0 |

🟢 **Derived on `p358` with the `ZZ-bd` guard actually implemented**, not merely
registered: the census skips any table whose `Region` header sits in column 0, and
reports `rows excluded by the ZZ-bd self-table guard: 6` — the exact six-row inflation
the paragraph below predicted for this file. 🟢 `p358`'s four additions move
`North America 19 → 20` (`SanDiegoCodeSchool/lti-node-library`) and
`Not placed 11 → 14` (`lti-core`, `ltix`, `edugatorlabs/ltijs`).

🔴 **LATAM is still a hard zero on this shelf, and `p358` is the first pass that can say
why rather than that it is.** This pass ran sixteen LATAM-origin addresses and found the
tooling exists; **three of thirteen live ones carry a licence**, and all three are agents
or applications rather than *foundations* — a tutor inside Open edX, a statutory PIAR
manager, an offline test runner. 🔵 So the zero here is not the same finding as the zero
on `agents/top.md` was: there is **no LATAM-origin LMS, SIS, interop library or judge** on
this shelf because none was found licensed, and the full measurement is on
`agents/top.md` under *"What changed on `p358`"*.

🟢 **`p356`'s figures reproduced exactly on `p357`'s independently-written census
script**, and the only movement is `APAC 11 → 12` from this pass's one addition
(`frappe/erpnext`, India-origin). 🔵 **Two passes' censuses agreeing is worth
recording given the right-hand column**: `p355`'s figures were wrong in four of five
buckets, so agreement here is evidence the derivation is now sound rather than merely
repeated. 🔴 **The same self-counting trap found on `agents/top.md` applies to this
table** — a census that counts every table with a `Region` column counts this one, and
its six rows inflate all six buckets by one. `ACTION ZZ-bd` covers both files.

🔴 **Every figure in the right-hand column was wrong, and only the LATAM zero was
right.** Four of the five gaps predate this pass: before `p356` added a single row this
shelf carried **15** North American and **14** EMEA rows against published figures of
11 and 12. 🔵 **This is `ACTION ZZ-aw` on a third and fourth quantity** — a
*distribution* in prose, unbound by any gate, wrong on both shelves this pass audited
(`agents/top.md` was off by one on North America). The remedy is not care; it is a gate.

- **North America** leads at 19, concentrated in platforms, standards and — new this
  pass — **university autograding**: `otter-grader` (BSD-3-Clause, UC Berkeley, named in
  its own licence payload), `okpy/ok-client` (Apache-2.0, Berkeley) and the two DMOJ
  rows, placed by **`dmoj.ca` appearing ten times in their README**.
- **EMEA** holds 16: European universities built most of the open assessment, media and
  interoperability tooling (Belgium ×2, Croatia, France, Germany, Italy, Norway,
  Switzerland, Spain, Tanzania) and now **Iran** (`Sharif-Judge`, Sharif University of
  Technology) and **Portugal** (`fenixedu-academic`, Instituto Superior Técnico).
- **APAC** rises from 2 to **11** in one pass, and all nine new rows are **online judges
  and sandboxes** from Chinese and Japanese universities. 🔵 This is the repository-side
  half of `T15`: the region the prose legs cannot measure is the region building the
  infrastructure.
- **Global** holds 7 — the genuinely multi-region platforms (Moodle, Kolibri, Tutor).
- **LATAM** places **0 rows on this shelf**, for the *n*th consecutive pass and now with
  a sharper account of why. The function legs run this pass in Spanish and Portuguese
  returned **exam-content archives, not tooling** — FAMAF/UNC (Argentina), Instituto
  Tecnológico de Costa Rica. 🟢 So the regional supply that exists is **content**, and the
  platform layer genuinely has no LATAM-origin project this base can verify. An
  engagement there builds on EMEA or North American platforms with local curriculum data
  on top (`bncc-dados`, `mcp-brasil` — see `agents/top.md`), and that remains a pattern
  rather than a deficiency — see `compose/patterns.md`.
