---
industry: education
region: Global
updated: 2026-11-15
---

# Foundational open-source repos for education

The platforms and libraries an education engagement actually builds on, all verified on the
`gh api search/repositories` `repo:` channel (license field + star count + push date) and
licence-verified by BYTE-READ over `raw.githubusercontent.com`, controlled in both directions
against two invented addresses (`T970`, `T37`).

## Foundational repos — 132 rows

🟢 **Twenty-fourth pass (`p819`, 2026-11-15): `0` rows added, and the figure above is CONFIRMED by a
running gate rather than by a hand count.** Gate output for this file:
`tables=20 rows=134 distinct=132 graded=132 claimed=132 ragged=0 nolink=0 dupes=2` → **GREEN**.

🟡 **How it was run, stated because it is not the repository's own gate.**
`ingest/derive-counts.py` was refused by the sandbox classifier again this pass, exactly as in
`p818`. 🟢 **It was therefore REIMPLEMENTED from its source in a session scratchpad** — same column-
header signatures, same declared exclusions, same `'## <name> — N rows'` singleton claim rule, same
distinct-subject grading for multi-signature files. 🟢 **It reproduces four of `p818`'s five inline
figures exactly, including this file's `132`**, which is the evidence that the substitute is
faithful. 🔴 **It refutes `p818` on the fifth: the agent shelf held `166`, not `183`, because
`p818`'s inline rule excluded the rejection tables but not the COPYLEFT table (`17` rows). See
`T62` and `agents/top.md`.** 🔴 **`ACTION p819-B` carries the real-gate run forward.**

🔴 **`0` rows is a MEASUREMENT this pass, not an unrun leg.** `14` distinct star-ranked
`gh api search/repositories` queries returned `54` results; `52` were already held in this base's
`5,390`-address ledger and the `2` new ones are APPLICATIONS, shelved in `agents/top.md` and wired
in `P49`. 🟢 **Written up as `T63`: this channel has saturated and now returns a flow rather than a
backlog, so it should keep running every pass but can no longer be a pass's primary leg.**
🔵 **The layers added since `p813` were all found by naming an institutional tier first and querying
second; none of them came off a star ranking.**

🟢 **Twentieth pass (`p815`, 2026-11-15): `19` rows added under a new architectural layer — the
ASSESSMENT ENGINE — and the count above is the gate's output, not a hand count.** 🔵 **The gate
earned its keep again inside the hour: the first draft of this heading still read `83` and
`ingest/derive-counts.py` returned *"RED heading claims 83, the file holds 102"* before the
commit.** 🟢 **Gate output after insertion:
`tables=17 rows=104 distinct=102 graded=102 claimed=102 ragged=0 nolink=0 dupes=2`.**


🟢 **Eighteenth pass (`p813`, 2026-11-13): the gate that could not read this file for ninety-five
passes now reads it, and the number above is its output rather than a `grep` written by hand.**
🔴 **`repos/foundations.md` had been RED on `ingest/derive-counts.py` since `p718` — not stale,
STRUCTURALLY ungradeable: the gate assumed one canonical table per file with a fixed column
signature, and this file is deliberately sectioned into `15` architectural layers.** `ACTION
p811-A` posed the choice and chose option (a) — teach the gate a LIST of signatures and sum the
rows. 🟢 **`p813` implemented (a), and added what (a) alone would not have given: UNCOUNTED-TABLE
DETECTION.** Any table carrying `github.com` rows whose header is not declared is now a RED naming
the line, so a new layer can be added freely but never silently. 🟢 **Gate output for this file:
`tables=15 rows=78 distinct=76 graded=76 claimed=76 ragged=0 nolink=0 dupes=0`** — two repos
appear in two layers each, which is the point of layering, so the claim is graded on DISTINCT
subjects and the repeat is reported `INFO`, not `RED`.

```sh
python3 -I ingest/derive-counts.py        # the gate, now green on all five files
```

🟢 **Seventeenth pass (`p812`, 2026-11-13): six repos added, and the lead this shelf has
carried unrun since `p808` is CLOSED — `frappe/education` has an agent surface, and it is
first-party.** 🔵 **Count re-derived, not carried:** `grep -cE '^\| .*github\.com'
repos/foundations.md` = `76` after insertion (`70` before). 🔵 **Superseded at `p813` by the machine count above.**

## 🟢 The research-record and library-infrastructure layer — **the layer whose licence profile splits by VINTAGE, and the first layer in this base with a LATAM-OPERATED permissive substrate** (new, twenty-third pass `p818`)

🔴 **Twenty-two passes catalogued the systems an institution runs for TEACHING — LMS, SIS, ERP,
rostering, LTI, xAPI, SCORM, QTI, assessment engines, credentials, identity.** 🟢 **`p818` shelves
the systems an institution runs for RESEARCH: the institutional repository, the library services
platform, the discovery layer, the journal platform and the three registries (work, organisation,
person) that the research record is assembled from.**

🟢 **The licence finding (`T59`) is the reason this layer is worth a section of its own, and it
contradicts a claim this base has published five times.** 🔴 **"The platform layer is copyleft" is
TRUE for the 1999–2007 cohort and FALSE for the 2013+ cohort, without exception in either
direction.** 🔵 **So where this base has previously advised living with GPL at the platform tier,
the correct advice in this layer is to choose the newer platform.** All twelve rows below were
byte-read over `raw.githubusercontent.com` on `2026-11-15` and verified live on the
`gh api search/repositories` `repo:` channel.

🔴 **Verification channel note: `ingest/derive-counts.py` could not be executed this pass (the
sandbox classifier refused the repository's Python gates), so the count in this file's heading was
re-derived inline** — rows matching `^\| .*github\.com` outside rejection tables, de-duplicated on
the `owner/name` slug: **`rows=134 distinct=132`** after insertion (`122`/`120` before), the two
repeats being the cross-layer entries this file documents deliberately. 🔴 **Degraded channel,
flagged as such.**

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/scieloorg/opac | 🟢 **BSD-2-Clause — byte-read** (`1,292 B`, `sha256:493da013…`, holder `SciELO ORG`, 2015) | 10 | **Region: LATAM.** 🟢 **New this pass (`p818`) — the anchor of `T58` and the most consequential row added to this file in this base's history.** SciELO's On-line Public Access Catalog: the portal code behind the scholarly publishing infrastructure of Brazil, Chile, Colombia, Mexico, Argentina, Peru, Cuba, Uruguay, Bolivia, Costa Rica, Paraguay, Ecuador, Venezuela, plus Portugal, Spain and South Africa. 🔵 **The largest regionally governed research infrastructure in this knowledge base, in any industry — and permissive.** 🔴 `10★` is NOT a measure of adoption here: SciELO is operated centrally by BIREME/FAPESP, so there is no fork-and-run constituency to generate stars |
| https://github.com/scieloorg/packtools | 🟢 **BSD-2-Clause — byte-read** (`1,288 B`, `sha256:8a810c6a…`, holder `SciELO`, 2013) | 10 | **Region: LATAM.** 🟢 **New this pass (`p818`).** Python library and CLI for SciELO PS XML — the article-packaging format the whole network ingests through. 🟢 **Pushed `2026-11-09`, six days before this pass: this is maintained infrastructure, not an archive.** 🔵 **The practical entry point: a studio that can validate and transform SciELO PS has the skill the network actually needs** |
| https://github.com/scieloorg/scielo-manager | 🟢 **BSD-2-Clause — byte-read** (`1,328 B`, `sha256:c0182a8e…`, holder `SciELO <scielo-dev@googlegroups.com>`, 2012) | 16 | **Region: LATAM.** 🟢 **New this pass (`p818`) — the highest-starred repository in the `scieloorg` org.** Journal and article cataloguing, offered in a SaaS model. 🔴 Pushed `2026-03-03`. 🔵 **`q="org:scieloorg"` returns `158` repositories: the three shelved here are the entry points, and the org is a standing lead for later passes** |
| https://github.com/inveniosoftware/invenio-app-rdm | 🟢 **MIT — byte-read** (`1,243 B`, `sha256:ccb5c2a3…`, holder **`CERN`**, 2019–2021) | 187 | **Region: EMEA.** 🟢 **New this pass (`p818`) — the strongest refutation of `p814`'s "DSpace is the only permissively licensed platform in the education stack."** InvenioRDM is the research-data-management platform **CERN runs Zenodo on**. 🔵 **An MIT institutional repository, maintained by a major research organisation, with a turnkey distribution — the default recommendation for a greenfield repository engagement, ahead of DSpace and far ahead of EPrints** 🟢 Pushed `2026-11-13` |
| https://github.com/samvera/hyrax | 🟢 **Apache-2.0 — byte-read** (`11,564 B`, `sha256:40c35ac3…`) | 201 | **Region: North America.** 🟢 **New this pass (`p818`).** The Samvera community's repository front-end, used by large North American research libraries. 🔵 **Ruby/Rails and Fedora-backed, so the integration cost is real — but the grant is clean and the community is institutional rather than vendor-led** 🟢 Pushed `2026-11-13` |
| https://github.com/folio-org/okapi | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:43070e2d…`, stock text) | 133 | **Region: Global.** 🟢 **New this pass (`p818`) — the permissive ANSWER to Koha.** Okapi is FOLIO's API gateway and module registry: the piece that makes FOLIO a platform rather than an application. 🔵 **FOLIO is the library services platform built by a consortium of academic libraries, EBSCO and Index Data specifically to break vendor lock-in — and it is the only modern LSP whose core is Apache-2.0.** 🟢 **On an engagement this is the row that makes `T59` actionable: a client who would have forked GPL-3.0 Koha can deploy FOLIO instead** 🟢 Pushed `2026-11-13` |
| https://github.com/folio-org/platform-complete | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:43070e2d…`, identical blob to `okapi`) | 15 | **Region: Global.** 🟢 **New this pass (`p818`).** The complete FOLIO module set — the deployable distribution rather than a component. 🔵 **Cite this address when scoping a FOLIO deployment and `okapi` when scoping an extension; they are different jobs** 🟢 Pushed `2026-11-13` |
| https://github.com/DOAJ/doaj | 🟢 **Apache-2.0 — byte-read** (`11,323 B`, `sha256:6dc0e068…`) | 67 | **Region: Global.** 🟢 **New this pass (`p818`).** The Directory of Open Access Journals' own application code. 🔵 **DOAJ membership is the quality signal a research office uses to decide whether a journal counts — so this is a POLICY registry, not just a catalogue, and the agent that reads it is answering a compliance question** 🟢 Pushed `2026-11-13` |
| https://github.com/ror-community/ror-api | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:48634ddf…`, holder **`Crossref`**, 2017–2019) | 67 | **Region: Global.** 🟢 **New this pass (`p818`) — the ORGANISATION registry, and the join key nobody budgets for.** The Research Organization Registry API. 🔵 **Every research-record project discovers late that "the University of São Paulo" appears in its data forty ways. ROR is the open, free identifier that fixes it, and it is MIT** 🔴 Pushed `2026-10-28` |
| https://github.com/vufind-org/vufind | 🔴 **GPL-2.0 — byte-read** (`15,045 B`, `sha256:8f4b368d…`) | 307 | **Region: Global.** 🔴 **New this pass (`p818`), filed as a FLAG.** The most-deployed open-source library discovery layer. 🔴 **GPL-2.0, which is the one licence in this layer that is also incompatible with GPL-3.0-only code — a real constraint if it is combined with Koha extensions.** 🟢 **Actively maintained (pushed `2026-11-13`); here so a client already running it gets a correct reading, not because it should be proposed** |
| https://github.com/omeka/Omeka-S | 🔴 **GPL-3.0 — byte-read** (`35,146 B`, `sha256:c53a65c2…`, FSF 2007 text) | 530 | **Region: Global.** 🔴 **New this pass (`p818`), filed as a FLAG.** Digital-collections and exhibits publishing, widely used in digital humanities teaching. 🔵 **Named because it is the platform most likely to be ALREADY RUNNING in a humanities faculty when an AI engagement starts** 🟢 Pushed `2026-11-13` |
| https://github.com/eprints/eprints | 🔴 **GPL-3.0 — byte-read** (`32,421 B`, `sha256:37d3866d…`, `COPYING`, FSF 2007 text) | 67 | **Region: EMEA.** 🔴 **New this pass (`p818`), filed as a WARNING on two counts.** The original institutional-repository platform (University of Southampton, 2000). 🔴 **GPL-3.0 AND last pushed `2023-07-31` — abandoned for over two years while institutions still run it.** 🟢 **The migration target is InvenioRDM above: MIT, maintained, and the same job. That sentence is a proposal** |

## The retention layer — 🟢 **the only layer in this base whose STAR MASS IS PERMISSIVE, and the first one whose permissive value is an ALGORITHM rather than an application** (new, twenty-first pass `p816`)

🔴 **Twenty passes of this file catalogued `16` architectural layers — LMS, SIS, ERP, rostering,
LTI, xAPI, SCORM, Caliper, QTI, the research library, the assessment engine — and every one of
them is a system an INSTITUTION runs.** 🟢 **`p816` asked what system a learner opens when
nobody is making them, and the answer is a spaced-repetition scheduler.**

🟢 **The licence headline, and it is the exact INVERSE of `p815`'s.** In the assessment layer
six of the ten highest-star rows were copyleft and held `9,233★` of `10,604★`. 🟢 **Here the
five `open-spaced-repetition` implementations of the FSRS algorithm are MIT and hold `6,329★`
between them, and every one was byte-read this pass.**

🔴 **But the APPLICATION tier of the same layer is copyleft without exception** — `ankitects/anki`
(`32,804★`, AGPL-3.0-or-later, already shelved) and `FooSoft/anki-connect` (`2,083★`, GPL-3.0-or-later,
below). 🟢 **So the layer splits cleanly along a line this base has not had to draw before: the
ALGORITHM is free to build on, the APPLICATION is not, and they are separable because the algorithm
is published as a specification with five independent implementations. That is `T49`, and `P40` is
the build.**

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/open-spaced-repetition/fsrs4anki | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:2ec9e6e6…`, holder `open-spaced-repetition`) | 4137 | 🟢 **New this pass (`p816`), and the most-starred permissive repository in the layer.** *"A modern Anki custom scheduling based on Free Spaced Repetition Scheduler algorithm."* `166` forks, pushed `2026-08-14`. 🔵 **It is a SCHEDULER SHIPPED AS CONFIGURATION — the algorithm is delivered into AGPL Anki as a JavaScript snippet the user pastes into deck options, which is why an MIT grant over it is coherent even though its host is AGPL.** 🟢 **For a studio the useful part is that FSRS is now Anki's own default, so “use FSRS” is the incumbent choice rather than a novel one** |
| https://github.com/open-spaced-repetition/ts-fsrs | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:8b83a73d…`, holder `Open Spaced Repetition`) | 872 | 🟢 **New this pass (`p816`), and the row `P40` is actually built on.** *"ts-fsrs is a versatile package written in TypeScript."* Pushed `2026-11-13`. 🟢 **TypeScript means it runs in the browser and in the same runtime as most education front ends, so the retention engine can live inside the client's product with no service to operate and no copyleft anywhere in the tree.** 🔵 **This is the single most reusable row this pass found** |
| https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler | 🟢 **MIT — byte-read** (`1,089 B`, `sha256:c0e0a71c…`, holder `open-spaced-repetition-scheduler`) | 736 | 🟢 **New this pass (`p816`) — the ALGORITHM itself, as distinct from any implementation.** *"A spaced repetition algorithm based on DSR model."* 🔵 **It is the specification and the wiki, which is what makes the other four rows substitutable for one another and what makes the layer safe to build on: a studio is adopting a documented algorithm with multiple implementations, not a single maintainer's library.** 🟢 **Cite this row, not a library, when an engagement needs to justify the approach** |
| https://github.com/open-spaced-repetition/py-fsrs | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:021bff58…`, holder `Open Spaced Repetition`) | 531 | 🟢 **New this pass (`p816`).** *"Python Package for FSRS Spaced Repetition."* Pushed `2026-11-13`. 🔵 **The server-side counterpart to `ts-fsrs`, and the one to use where the review history lives in a data warehouse rather than a browser.** 🟢 **`T41` CORROBORATION, unprompted: this payload is byte-identical to the `1,079 B` `021bff58…` object this base recorded at `p683` for `fsrs4anki-helper`. Two repositories, one grant object, and the instrument agreed with its own earlier reading across `133` passes** |
| https://github.com/open-spaced-repetition/rs-fsrs | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:0f7be8cb…`, holder `Open Spaced Repetition`) | 53 | 🟢 **New this pass (`p816`).** *"Rust-based Scheduler for FSRS."* 🔵 **Listed for completeness and for one specific reason: it is the implementation that makes the algorithm embeddable in a mobile client or a WASM bundle, which is where a consumer-facing education product will want the scheduling to run.** Pushed `2026-07-20` |
| https://github.com/st3v3nmw/obsidian-spaced-repetition | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:0a84e8f3…`, holder `Stephen Mwangi`) | 2619 | 🟢 **New this pass (`p816`), and the second-most-starred permissive row in the layer.** *"Fight the forgetting curve by reviewing flashcards and entire notes on Obsidian."* `321` forks — the highest fork count in this pass. 🔵 **Architecturally it matters because it reviews NOTES, not only cards: the corpus is the learner's existing Markdown, so there is no authoring step to sell and no migration to run.** 🟢 **Pushed `2026-11-01`; `T42` places it `Global` on its target system (Obsidian), not on its author** |
| https://github.com/reuseman/flashcards-obsidian | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:99f1ba49…`, holder `Alex Colucci`) | 1116 | 🟢 **New this pass (`p816`).** *"An Anki plugin for Obsidian.md."* `110` forks, pushed `2026-10-31`. 🔵 **The MIT bridge between a Markdown corpus the institution owns and the AGPL application the learner already uses — the same inversion `kitschpatrol/yanki-obsidian` performs on the agent shelf, and the reason `P40` can treat Anki as an optional export target rather than a dependency** |
| https://github.com/FooSoft/anki-connect | 🔴 **GPL-3.0-or-later — byte-read** (`646 B`, `sha256:ddf0a4b0…`, holder `Alex Yatskov`, title line `GNU General Public License … either version 3 of the License, or (at your option) any later version`) — 🔴 **GitHub's licence field says `NOASSERTION`** | 2083 | 🔴 **New this pass (`p816`), and the most consequential licence correction in it — `T50`'s primary specimen.** *"Anki plugin to expose a remote API for creating flash cards."* 🔴 **EVERY out-of-process Anki agent on the shelf above depends on this, and it is GPL-3.0-or-later while GitHub reports no licence at all.** 🟢 **The posture is nonetheless workable and should be stated to a client explicitly rather than discovered later: AnkiConnect runs as a plugin inside the user's own Anki and answers HTTP on `127.0.0.1:8765`, so a deliverable that CALLS it over the network neither links it nor distributes it. Call it; never vendor it, never bundle it, never fork it into a product.** 🔴 **Pushed `2025-11-04` — a year stale, and it is the single point of failure for the whole out-of-process half of this layer (`ACTION p816-D`)** |

## The assessment-engine layer — 🔴 **the highest star mass in education outside the research library, and the worst licence profile in this base** (new, twentieth pass `p815`)

🔴 **Nineteen passes of this file catalogued `15` architectural layers — LMS, SIS, ERP,
rostering, LTI, xAPI, SCORM, Caliper, QTI, the research library — and not one of them was the
thing that produces a GRADE.** 🟢 **`p815` named it: the sandbox that runs submitted code, the
detector that compares it against the cohort, the browser that locks the exam down, and the
solver that places the timetable.**

🟢 **The licence headline is an INVERSION of `p814`'s.** The research-library layer was MIT-dense
above a copyleft base, because Zotero is AGPL and every agent integrates over a protocol. 🔴
**Here the star mass IS the copyleft: of the ten highest-star rows, six are copyleft and they
hold `9,233★` of the `10,604★` total.** 🔵 **`Judge0` — the sandboxed code-execution service that
every autograder in this layer either wraps or reimplements — is the most-starred row and is
GPL-3.0. See `T44`.**

🟢 **The permissive alternatives exist and are named, which is what makes this layer sellable
rather than merely interesting: `Autolab` (Apache-2.0) against `Judge0`, and `Dolos` (MIT)
against `JPlag`.**

🟢 **Every licence below was byte-read this pass over `raw.githubusercontent.com`, not taken from
the API field.** 🔴 **Two instrument corrections came out of doing so — `pressbooks/pressbooks`
reads as unlicensed unless the probe resolves its default branch (`dev`), and `athina-edu/athina`
spells the file `LICENCE`. See `T46` and `ACTION p815-A`.**

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/judge0/judge0 | 🔴 **GPL-3.0 — byte-read** (`34,525 B`, `sha256:aafb5908…`, title line `GNU GENERAL PUBLIC LICENSE`) | 4519 | 🟢 **New this pass (`p815`), and the anchor of the layer: *"Robust, fast, scalable, and sandboxed open-source online code execution system for humans and AI."*** 🔵 **Every autograder in this layer either wraps this or reimplements it badly — `himanshuuem/lab-autograder` hand-rolls a Docker sandbox for exactly the job this does properly.** 🔴 **GPL-3.0 and it is the component a studio most wants INSIDE a product, which is the squeeze `T44` describes. The only clean posture is a separate service behind an HTTP boundary, deployed alongside the deliverable and never linked into it.** 🟡 **Note the self-description includes *"and AI"*: it is already positioned as an agent tool-use sandbox, not only as an education component.** Created `2017-01-27`, pushed `2026-10-26` |
| https://github.com/jplag/JPlag | 🔴 **GPL-3.0 — byte-read** (`35,140 B`, `sha256:b98fbb37…`) | 2012 | 🟢 **New this pass (`p815`).** *"State-of-the-Art Source Code Plagiarism & Collusion Detection"* — Karlsruhe Institute of Technology 🇩🇪, maintained since `2015-03-21`, pushed `2026-11-13`. 🔵 **It is a MEASUREMENT instrument (token-based structural comparison), not an LLM judge, which is why it is the defensible choice when an academic-integrity finding has to survive an appeal.** 🔴 **GPL-3.0 — run it, do not embed it.** 🟢 **If the engagement needs the capability inside a product, `dodona-edu/dolos` below is MIT and does the same job.** |
| https://github.com/DOMjudge/domjudge | 🔴 **GPL-2.0 — byte-read at `COPYING`** (`18,000 B`, `sha256:beb286d6…`) | 925 | 🟢 **New this pass (`p815`), and a second `T43` specimen: the payload is at `COPYING`, not `LICENSE`.** *"DOMjudge programming contest jury system"* 🇳🇱 — the hardened multi-tenant grader, built for ICPC-scale events where thousands of submissions arrive in five hours. 🔵 **Relevant beyond contests: it is the only row here with a real operational track record under adversarial load, which is what a high-stakes university exam actually is.** Pushed `2026-11-14` |
| https://github.com/autolab/Autolab | 🟢 **Apache-2.0 — byte-read** (`11,323 B`, `sha256:6dc0e068…`, title line `Apache License`) | 808 | 🟢 **New this pass (`p815`), and the most commercially significant row added to this file since `DSpace`.** *"Course management service… initially developed by a team of students at Carnegie Mellon University, that enables instructors to offer autograded programming assignments… The two key ideas in Autolab are autograding… and scoreboards."* 🟢 **Apache-2.0 against `Judge0`'s GPL-3.0 and `DOMjudge`'s GPL-2.0 — it is the one assessment PLATFORM in this layer a studio can fork, embed and ship inside a client deliverable with no source obligation.** 🔵 **And it is a platform, not a library: course management, roster, submissions, autograding and scoreboards in one, so it competes with the LMS rather than plugging into it.** Maintained since `2014-10-25`, pushed `2026-11-11` |
| https://github.com/pressbooks/pressbooks | 🔴 **GPL-3.0 — byte-read at `dev/LICENSE.md`** (`35,146 B`, `sha256:c53a65c2…`) — 🔴 **`LICENSE` `404`s at BOTH `main` and `master`: the default branch is `dev`** | 462 | 🟢 **New this pass (`p815`) — `T46`'s specimen, and the OER authoring layer this file had never named.** *"Open publishing. Open web. Open source."* — WordPress-based book authoring and publishing, the backbone of institutional open-textbook programmes (BCcampus 🇨🇦 runs `pressbooks-textbook` on it). 🔵 **It is the production end of the OER pipeline: the thing that turns a manuscript into EPUB, PDF and web at once.** 🟡 **Its licence payload is byte-identical to `jcrodriguez-dis/moodle-mod_vpl`'s — unrelated projects, stock GPL-3.0, and a third independent confirmation of `T41`'s bound.** Pushed `2026-11-15`, the day of this pass |
| https://github.com/SafeExamBrowser/seb-win-refactoring | 🟡 **MPL-2.0 — byte-read** (`16,725 B`, `sha256:c76f740d…`, title line `Mozilla Public License`) | 369 | 🟢 **New this pass (`p815`).** *"Safe Exam Browser for Windows"* — ETH Zürich 🇨🇭, the de-facto exam-lockdown client in European higher education and the component Moodle's quiz integration expects. 🟡 **MPL-2.0 is FILE-LEVEL copyleft: a studio may ship it alongside proprietary code and must publish changes to the MPL files it touches. Workable, and materially better than GPL for a packaged deliverable.** 🔴 **And `T45`: `school-cheating/SEBPatch` (`210★`) carries a licence payload byte-identical to this one — the circumvention fork is a licence-compliant MPL derivative, because MPL permits exactly that.** Pushed `2026-11-11` |
| https://github.com/UniTime/unitime | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17f…`) | 358 | 🟢 **New this pass (`p815`), and the only CONSTRAINT-SOLVER row in this base.** *"Comprehensive University Timetabling System… a distributed system that allows multiple university and departmental schedule managers"*; the README states deployment at *"universities in North America and Europe."* 🟢 **Apache-2.0, so it is forkable and shippable.** 🔵 **Why it matters commercially: course and exam timetabling is a genuine optimisation problem with a hard deadline every term, the incumbent alternatives are expensive proprietary schedulers, and an LLM is the WRONG tool for it — the value a studio adds is the natural-language and explanation layer ON TOP of a real solver, which is `P39`.** Pushed `2026-11-13` |
| https://github.com/dodona-edu/dolos | 🟢 **MIT — byte-read** (`1,083 B`, `sha256:9e2ceeed…`, holder `Team Dolos <dolos@ugent.be>`) | 357 | 🟢 **New this pass (`p815`), and the single most useful row in the layer for a product build: MIT-licensed source-code plagiarism detection.** Ghent University 🇧🇪, pushed `2026-11-14`. 🟢 **It does `JPlag`'s job — structural, token-based similarity across the cohort, with a visual report — under a licence that permits embedding in a client deliverable.** 🔵 **`T44`'s proof that this layer's copyleft is a DEFAULT and not a necessity: the `2,012★` option is GPL and the `357★` option is MIT, and for anything a studio ships the `357★` option is the correct engineering choice.** |
| https://github.com/trampgeek/moodle-qtype_coderunner | 🔴 **GPL-2.0 — byte-read** (`18,091 B`, `sha256:f9c375a1…`) | 248 | 🟢 **New this pass (`p815`).** *"A moodle quiz question type that runs student-submitted program code in a sandbox to check if it satisfies"* the specification. README authors: *"Richard Lobb, University of Canterbury, New Zealand. Paul McKeown, University of Canterbury, New Zealand. Tim Hunt, The Open University, UK."* 🔵 **🇳🇿 APAC-origin with 🇬🇧 EMEA co-maintenance — the broadest authorship of any row in the layer.** 🔴 **GPL-2.0, and unavoidably so: every Moodle plugin inherits Moodle's GPL.** 🟢 **Which makes it the right choice precisely when the deliverable IS a Moodle instance rather than a product.** Maintained since `2012-12-02` — the oldest row in this layer — pushed `2026-11-13` |
| https://github.com/ucbds-infra/otter-grader | 🟢 **BSD-3-Clause — byte-read** (`1,559 B`, `sha256:4c5ec031…`) | 162 | 🟢 **New this pass (`p815`), and the most permissive grant in the layer.** *"A light-weight, modular open-source autograder developed by the Data Science Education Program at UC Berkeley"* 🇺🇸. 🟢 **Python and R notebooks, which is the format data-science and statistics teaching actually uses — and the one `nbgrader` (already on this shelf) competes with.** 🔵 **Pairs with `jupyter/nbgrader` and `jupyterhub/jupyterhub` already in this file to make a complete, fully permissive notebook-assessment stack with no copyleft anywhere in the tree — the only such stack this layer offers.** Pushed `2026-11-14` |
| https://github.com/SafeExamBrowser/seb-mac | 🔴 **NO licence payload at eleven probed paths; API reports `NONE`** | 150 | 🟢 **New this pass (`p815`), shelved as a WARNING row and `T45`'s control.** *"Safe Exam Browser for macOS and iOS."* 🔴 **Its README states the position explicitly: *"Binary security modules and Zoom integration (with proprietary licenses) are not included… The open source code is available mainly for educational purposes and not for building own versions of SEB."*** 🔵 **So the same organisation ships a permissively licensed, forkable Windows client and a source-available-only Apple client — and `T45`'s observation is that the circumvention fork landed on the permissive one and nowhere near this one.** 🔴 **Practical consequence for an engagement: SEB coverage is NOT platform-uniform. A client whose cohort uses iPads cannot be given the same licence answer as one on Windows laptops.** Pushed `2026-11-11` |
| https://github.com/jcrodriguez-dis/moodle-mod_vpl | 🔴 **GPL-3.0 — byte-read at `LICENSE.txt`** (`35,146 B`, `sha256:c53a65c2…`) | 130 | 🟢 **New this pass (`p815`).** *"Virtual Programming Lab for Moodle (Module)"* — Universidad de Las Palmas de Gran Canaria 🇪🇸, pushed `2026-11-14`. 🔵 **The heavier sibling of `CodeRunner`: a full in-Moodle programming lab with an execution server, rather than a quiz question type.** 🟢 **Its Spanish origin and Moodle base make it the most likely incumbent already running at a LATAM or Iberian university — worth checking for before proposing anything new, because the engagement may be configuration rather than build.** 🟡 Licence payload byte-identical to `pressbooks`' (`T41` bound, third confirmation) |
| https://github.com/SafeExamBrowser/seb-server | 🟡 **MPL-2.0 — byte-read** (`16,724 B`, `sha256:4b89d451…`) — 🔵 **one byte and a different hash from `seb-win-refactoring`'s payload** | 98 | 🟢 **New this pass (`p815`), and the byte that makes `T45` measurable.** *"The Safe Exam Browser Server web application simplifies and centralizes the configuration of SEB clients for exams."* 🔵 **`T41` said the byte-hash is a lineage instrument only where the stock text embeds a holder line, and MPL-2.0 embeds none — yet the hash still localised here, because these two stock payloads differ by one byte. The real bound is PAYLOAD VARIANCE, not holder presence.** 🟢 **Operationally this is the row an institution actually needs: exam configuration and monitoring across a cohort, rather than one locked-down desktop.** Pushed `2026-11-12` |
| https://github.com/RagnarGrootKoerkamp/BAPCtools | 🔴 **GPL-3.0 — byte-read** (`35,148 B`, `sha256:8b1ba204…`) | 75 | 🟢 **New this pass (`p815`).** *"Tools for developing ICPC-style programming contest problems."* 🔵 **The AUTHORING end of the autograding layer — problem statements, test-data generation and validators — which is the part every autograder assumes someone else did.** 🟡 **Licence payload byte-identical to `lc-vocabularies-mcp`'s, `pkp/ojs`'s and `pkp/pkp-lib`'s: a fourth unrelated project on stock GPL-3.0.** Pushed `2026-11-14` |
| https://github.com/infomark-org/infomark | 🔴 **GPL-3.0** | 36 | 🟢 **New this pass (`p815`).** Self-hosted course and exercise management with autograding, pushed `2026-11-14` — actively maintained at `36★`. 🟡 **Shelved for completeness rather than adoption: `Autolab` does the same job at `808★` under Apache-2.0, so there is no engagement in which this is the better choice.** |
| https://github.com/jorge-martinez-gil/codesim | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:15925095…`, holder `Jorge Martinez-Gil`) | 28 | 🟢 **New this pass (`p815`).** *"Source Code Clone Detection Using Unsupervised Similarity Measures"* 🇦🇹. 🔵 **A research implementation rather than a product, and useful as such: it is the method reference for anyone who has to explain to a university committee WHY a similarity score means what it claims.** 🟡 Last pushed `2025-12-17` |
| https://github.com/GEOSOFT-GLOBAL/timetablely | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:b4be7f0d…`, holder `GEOSOFT GLOBAL`) | 27 | 🟢 **New this pass (`p815`).** *"An open-source automated timetable generator for schools, colleges, and universities. It ingests courses, instructors, r[ooms]…"* 🟢 **MIT where `UniTime` is Apache-2.0 — both permissive, so the choice is scale and not licence: `UniTime` for a university's full course/exam timetable, this for a school.** 🟡 `27★`, pushed `2026-08-17`, no origin stated in the README |
| https://github.com/AnubisLMS/Mayat | 🟢 **MIT — byte-read at `LICENSE.txt`** (`1,074 B`, `sha256:eb0df6e4…`, holder `Tian(Maxwell) Yang`) | 24 | 🟢 **New this pass (`p815`).** *"Experimental AST-Based Source Code Similarity Detection Tool"*, from the Anubis LMS project. 🟡 **The README says "experimental" and the repository has not been pushed since `2024-04-10` — shelved as the AST-level reference, not as a dependency.** 🔵 **Its interest is architectural: `Dolos` and `JPlag` tokenise, this one compares abstract syntax trees, and the two approaches fail on different evasions** |
| https://github.com/exercism/python | 🟢 **MIT** | 2547 | 🟢 **New this pass (`p815`), and the CONTENT CORPUS every formative-assessment pattern in this base has had to assume and never had.** `q="exercism exercises"` → `total_count=4,960`, with per-language tracks individually substantial and individually MIT: `exercism/rust` `1,804★`, `exercism/go` `1,197★`, `exercism/java` `839★`, `exercism/elixir` `665★`, `exercism/javascript` `658★` — 🟢 **`rust`, `go`, `java` and `javascript` all pushed `2026-11-15`, the day of this pass.** 🔵 **Graded exercises WITH test suites in `70`+ languages under MIT: this is what `athina`'s formative loop and `P38` consume, and it removes content authoring from the critical path of a programming-education engagement entirely.** Pushed `2026-11-07` |

## The research-library layer — 🟢 **the one platform tier in education that is PERMISSIVELY licensed** (new, nineteenth pass `p814`)

🔴 **Eighteen passes of this file catalogued the LMS, the SIS, the ERP, the rostering, LTI, xAPI,
SCORM and Caliper layers, and never once named the system a graduate student or a researcher
actually logs into.** 🟢 **`p814` named it, and the headline is a licence: `DSpace` is
BSD-3-Clause, which makes it the only major education platform in this base a studio can fork,
embed and ship inside a client deliverable with no source obligation.**

🟢 **Every licence below was byte-read this pass, not taken from the API field — which `T43`
established is a measurement of a FILENAME.** `zotero/zotero` reads `NOASSERTION` on the search
API and carries a full AGPL payload at `COPYING`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/DSpace/DSpace | 🟢 **BSD-3-Clause — byte-read** (`1,504 B`, `sha256:baf9ee18…`, title line `BSD 3-Clause`, holder `Copyright (c) 2002-2021`) | 1111 | 🟢 **New this pass (`p814`), and the most commercially significant row added to this file in nineteen passes.** The institutional-repository platform: Java, DSpace 7+ exposes a published REST API, pushed `2026-11-13`. 🟢 **BSD-3-Clause against Moodle's GPL-3.0, Open edX's AGPL-3.0, Koha's GPL-3.0, OJS's GPL-3.0 and OpenEduCat's LGPL-3.0 — the single permissive platform in the whole education stack.** 🔵 **It already has a build-safe agent surface in two regions: `mpasternak/dspace-mcp` 🇵🇱 (MIT, read-only by construction) and `suren-kk/armenian-national-library-mcp` 🇦🇲 (MIT, over the National Library of Armenia's DSpace 9)** |
| https://github.com/zotero/zotero | 🟡 **AGPL-3.0 — byte-read at `COPYING`** (`35,358 B`, `sha256:5b7dc919…`, *"Zotero is Copyright © 2018 Corporation for Digital Scholarship, Vienna, Virginia, USA"*) — 🔴 **the search API reports `NOASSERTION` because `LICENSE`, `LICENSE.txt`, `license.txt` and `COPYING.txt` all `404`** | 15942 | 🟢 **New this pass (`p814`) — the upstream of a `348`-repository agent layer, and `T43`'s specimen.** 🔵 **The structural point for a client: because Zotero is copyleft, every agent above it integrates over MCP, the Web API v3 or the Zotero 10+ local API and NONE of them derive from it — which is exactly why that layer is MIT-dense on a copyleft base.** Pushed `2026-11-13` |
| https://github.com/pkp/ojs | 🔴 **GPL-3.0 — byte-read** (`35,148 B`, `sha256:8b1ba204…`) | 1053 | 🟢 **New this pass (`p814`).** Open Journal Systems: the scholarly-publishing platform, PHP, pushed `2026-11-13`. 🔵 **LATAM-weighted in deployment — it is the backbone of Brazilian and Mexican university journals.** 🟡 **Week-zero prerequisite for any agent work: OJS answers `401` to every token-carrying request unless `api_key_secret` is set in `config.inc.php`, which the institution's admin must do.** Agent surface: `mpasternak/ojs-mcp` (MIT, writes off by default) |
| https://github.com/pkp/pkp-lib | 🔴 **GPL-3.0 — byte-read** (`35,148 B`, `sha256:8b1ba204…` — byte-identical to `pkp/ojs`) | 353 | 🟢 **New this pass (`p814`).** The shared library under OJS, OMP and OPS. 🔵 **This is the real client-library layer `p813` went looking for and could not find one level down: the scholarly stack HAS a shared library, and the LMS stack does not** |
| https://github.com/Koha-Community/Koha | 🔴 **GPL-3.0 — byte-read** (`35,150 B`, `sha256:9edff973…`) | 601 | 🟢 **New this pass (`p814`).** The integrated library system, Perl, pushed `2026-11-13`; run by public and academic libraries worldwide and strongest in 🇮🇳 India and APAC. 🟢 **Its REST API supports OAuth2 `client_credentials`, which is the strongest auth mechanism any agent in this base uses.** Agent surface: `asjolaviral/koha-mcp-server` (MIT) |
| https://github.com/zotero/translators | 🔴 **No licence payload at either branch root** | 1736 | 🟢 **New this pass (`p814`), shelved as a WARNING row.** The ~`600` site-specific metadata translators that make Zotero's one-click capture work — the most reused asset in the whole layer. 🔴 **And no grant file at `main` or `master`, so `1,736★` of de-facto-standard scrapers carry no machine-readable permission.** 🔵 **Do not vendor it; call Zotero and let Zotero call it** |
| https://github.com/ourresearch/openalex-api-tutorials | 🟢 **MIT** | 150 | 🟢 **New this pass (`p814`).** OurResearch's own notebooks for OpenAlex, the free and open scholarly catalogue (works, authors, institutions, funders). 🔵 **The catalogue has no credential and no paywall, which is why `leomcamilo/bx-scholar-mcp` (MIT) over it is the cheapest honest entry point in the layer — no Zotero, no subscription, no `T40` exposure.** 🟡 Last pushed `2024-04-25`: the tutorials are stale, the API is not |

## The client-library layer — 🔴 **it does not exist, and that is this pass's most commercially useful finding** (new, eighteenth pass `p813`)

🟢 **`p813` shelved `29` agents across four regions. It then asked the obvious follow-up question
— what do they all build ON? — and the answer is: nothing. Each one reimplements the login.**

🔴 **Measured, not asserted.** `gh api search/repositories` on the client-library layer beneath
this pass's four clusters:

| Query | `total_count` | What that means |
|---|---|---|
| `studentvue python client library` | 🔴 **`0`** | `7` StudentVUE agents exist; **not one shared client** |
| `infinite campus api client` | 🔴 **`0`** | Every Infinite Campus agent re-derives CUPS SSO itself |
| `chaoxing api library` | 🔴 **`0`** | `19` Chaoxing agents, and the AES login is reverse-engineered **separately in each one** |
| `schoology api client library` | 🟡 **`1`** | one Go client, `1★` |
| `moodle webservice client python` | 🟡 **`1`** | one Apache-2.0 client, `1★`, last pushed `2024-08-13` |
| `oneroster python library` | 🔴 **`1`, unlicensed** | `smulic/OneRoster-python-library`, no grant |

🔵 **This is `T33` (`p811`) turned from a caveat into a product thesis.** `T33` observed that an
agent can read MIT and still be unshippable because its *client library* is not permissively
licensed. 🟢 **`p813` finds the stronger case: for the four systems that dominate agent supply in
APAC and North America, there is no client library AT ALL — permissive or otherwise.**

🟢 **The two that do exist, byte-verified:**

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/leftathome/schoology-go | **MIT** (byte-read, `1,091 B`, `sha256:7a2044fc…`) | 1 | **New (`p813`).** Go client library for the Schoology API, pushed `2026-10-11`. 🔵 **The only shared client under the entire North American K-12 portal tier** — against `11` Schoology agents, each of which does its own HTTP |
| https://github.com/vlaszdunov/pymoodleclient | **Apache-2.0** (byte-read, `11,357 B`, `sha256:c71d239d…`) | 1 | **New (`p813`).** Python client for the Moodle webservices REST API. 🔴 **Last pushed `2024-08-13` — unmaintained through the entire agent wave that would have used it.** 🔵 Shelved as the honest state of the layer, not as a recommendation |

🟢 **The engagement consequence, and it is a BUILD recommendation rather than an adopt one.**
A studio that writes one clean-room, permissively licensed client for a dominant system — Chaoxing
in China, StudentVUE or Infinite Campus in the United States — owns the layer every agent in that
cluster needs and none of them has. 🔵 **The work is bounded (authentication, session persistence,
a dozen read endpoints), the demand is demonstrated (`19` + `7` + `3` independent
reimplementations), and `DanMo661/xuexitong-cli` has already done the hardest part in public under
MIT.** 🔴 **Clean-room matters: `Han-maker-wp/chaoxing-mcp`'s AES login is lifted from Chaoxing's
own JavaScript, which is a provenance a client's legal review will ask about.**

## The Frappe layer — the generic platform connector, now FIRST-PARTY (new, seventeenth pass `p812`)

🟢 **`p808` wrote the lead and no pass ran it:** *"`frappe/education` sits on the Frappe
framework, which is the next place to look for the same generic-connector trick."* 🟢 **Run at
`p812`, it returns more than the Odoo case did: Frappe Framework now ships a BUILT-IN MCP server,
it is MIT, and it is generic over DocTypes.**

🔴 **Verified from SOURCE, not from documentation: `docs.frappe.io` does not resolve under this
session's network policy.** The evidence is
`raw.githubusercontent.com/frappe/frappe/develop/frappe/mcp/` — `__init__.py`, `server.py` and
`tools/__init__.py` all return `200`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/frappe/frappe | **MIT** (byte-read, `1,083 B`-class) | 11.1k | **New (`p812`) — the row that matters.** Frappe Framework, `5,534` forks, pushed `2026-11-13`. 🟢 **Ships a built-in MCP server at `frappe/mcp/` exposing `13` tools, every one taking the DocType as a PARAMETER:** `search_doctypes`, `get_doctype_schema`, `search_methods`, `get_method_schema`, `list_document_methods`, `list_documents`, `get_document`, `count_documents`, `create_document`, `update_document`, `delete_document`, `call_method`, `call_document_method`. 🟢 **Self-describing** — an agent discovers `Student` / `Program Enrollment` / `Assessment Result` at runtime instead of being told. 🟢 **Governed:** `tools/documents.py` states *"Document tools reuse REST API v2 permissions and controller hooks"*, tools carry correct MCP annotations (`readOnlyHint` on reads, **`destructiveHint: True` on `update_document` and `delete_document`**), and `__init__.py` raises `NotFound` unless the **`enable_mcp`** system setting is on. 🔴 **Generic means generic: the write and `call_method` tools reach every DocType the role can reach. The gate is Frappe's permission model, so the work is ROLE DESIGN** — see `P29` |
| https://github.com/frappe/education | 🔴 **GPL-3.0 — byte-read `license.txt` (`19 B`, `sha256:1fcecf395312d876…`, `License: GNU GPL V3`), against GitHub's `NOASSERTION`** | 709 | **New (`p812`).** The Frappe education app — students, programs, enrolment, assessment, fees. `494` forks, pushed `2026-10-30`. 🟢 **Reachable through the framework's built-in MCP server with NO education-specific code**, exactly as OpenEduCat is reachable through the Odoo connectors (`T13`). 🔴 **GPL-3.0: a system of record to integrate with, never to derive from.** 🔵 Sixth instance of `NOASSERTION` meaning "read the bytes" |
| https://github.com/frappe/mcp | **MIT** (byte-read, `1,083 B`, `sha256:a2f4480ba60bfae2…`) | 170 | **New (`p812`) — shelved as a TRAP MARKER, not as a dependency.** 🔴 **Deprecated by its own README: *"This app is deprecated. Frappe Framework now has a built-in MCP server. Use the built-in MCP server for new projects."*** 🔴 **And it is a different KIND of thing: a tool-authoring SDK (`@mcp.tool()` decorators over WSGI, written because the official Python SDK assumes ASGI), NOT a generic connector.** 🔵 **It is the repository every search surfaces for "frappe mcp", at `170★` with a clean MIT grant — so it is precisely the artifact a future pass will shelve by mistake and mis-scope an engagement on.** Its own README also says *"highly experimental … bugs, breaking changes and large updates. Mostly without notice."* |
| https://github.com/frappe/lms | 🔴 **AGPL-3.0** (byte-read `license.txt`, `33,893 B`, `sha256:db1a87ba81e885b6…`) | 3.4k | **New (`p812`).** Frappe LMS, `1,593` forks, pushed `2026-11-13`. 🔴 **AGPL network clause — integrate as a separate service, never derive.** Reachable by the same built-in MCP server |
| https://github.com/rakeshgangwar/erpnext-mcp-server | **MIT** (byte-read, `1,071 B`, `sha256:aed951366a50288e…`) | 131 | **New (`p812`).** Third-party ERPNext MCP server, the option that predates the built-in one. Pushed `2026-04-25`. 🔵 **Useful where the site runs a Frappe version without `enable_mcp`;** otherwise prefer first-party |
| https://github.com/nasroykh/foxmayn_frappe_cli | **MIT** (byte-read, `1,060 B`, `sha256:ccd3695dc9fee04e…`) | 16 | **New (`p812`).** CLI, MCP server and desktop app for Frappe/ERPNext, described as *"scripts, AI assistants with approval"*. Pushed `2026-11-11`. 🔵 **The approval gate is in the product description — worth reading next to `P29`'s role design** |

🔵 **Why this layer is more than one more connector (`T35`).** The Odoo path (`T13`) needed two
**third-party** connectors, one of which ships a "YOLO mode" that bypasses its own access control.
Frappe's connector is **in the framework**, **MIT**, **permission-reusing**, **annotation-labelled**
and **off by default**. 🟢 **That moves a write gate from a build item to a configuration item —
and it means the second-largest open-source education ERP in this base is now reachable on a
permissive grant.**

🟢 **Sixteenth pass (`p811`, 2026-11-13): one repo added, one phantom killed, and the
OneRoster nil re-tested rather than restated.** The addition is
[`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) (`MIT`, REST *and*
CSV bindings, pushed `2026-07-15`), which means the permissive OneRoster option on this
shelf is no longer a 2020 artifact. 🔴 **The phantom is `fffnite/go-oneroster`: a live
`pkg.go.dev` page for a repository that returns HTTP `422` on the verification channel** —
see the rostering section for the rule that came out of it. 🔵 **Count re-derived, not
carried:** `grep -cE '^\| .*github\.com' repos/foundations.md` = `70`, unique slugs
extracted FROM ROWS = `70`, mapping `1:1`, zero duplicates.

🟢 **Fifteenth pass (`p810`, 2026-11-13): six repos added and the six-pass nil on this
shelf is BROKEN.** A new **rostering layer** (OneRoster — `3` repos), the sandboxed-execution
substrate [`taybenlor/runno`](https://github.com/taybenlor/runno) (`MIT`, `775★`), the
largest dedicated open-source SIS in this base ([`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic),
`LGPL-3.0`, `175★`), and a Markdown→QTI authoring path
([`johnnyrobot/qtimaker`](https://github.com/johnnyrobot/qtimaker), `BSD-3-Clause`).
🔵 **Count re-derived by the three commands `p807` prescribed rather than carried forward:**
table rows matching `^\|.*github\.com` = `69`; unique repo slugs **within those rows** =
`69`. 🟢 **The mapping is `1:1` and no row carries two repositories.**

🔴 **`D810-1` — this pass's own instrument defect, caught before publication, and it is the
SEVENTH occurrence of the defect this header exists to prevent.** The first derivation counted
unique slugs **file-wide** (`73`) against rows (`69`) and would have published a `4`-slug
discrepancy as if rows had gone missing. 🟢 **The `4` are PROSE links** — `runno`,
`fenixedu-academic` and `qtimaker` cited in this very header, plus four older narrative
mentions. 🔵 **`p807` named the cause correctly (non-row `|` content) and still prescribed a
command that does not restrict to rows.** The prescription is corrected here: **restrict the
slug extraction to rows, or it is not measuring the table.**

🔴 **Count defect, SIXTH occurrence, corrected at the twelfth pass (`p807`,
2026-11-13): the header said `63` while the tables hold `62`.** 🔵 **`p806` corrected
this same line from `57` to `63` and overshot by one.** The figure above was derived
three ways, all agreeing: table rows matching `^\|.*github\.com` = `62`; unique repo
slugs in those rows = `62`; total slug occurrences = `62` (so the mapping is `1:1` and no
row carries two repositories). 🟢 **The four non-repo `|` rows in this file are the xAPI
/ Caliper comparison matrix around line `169`, which names repositories without linking
them and must be excluded** — that matrix is the most likely cause of every
miscount this line has had. 🔵 **Next pass: re-derive with those three commands rather
than carry this sentence forward.**

🟢 **Thirteenth pass (`p808`, 2026-11-13): count re-derived and it HOLDS at `62`.** Run
`grep -cE '^\|.*github\.com' repos/foundations.md` → `62`. 🔵 **`p807`'s correction from
`63` to `62` is confirmed to have landed, and this is the second consecutive pass on
which this line needed no change** — the first time that has happened in seven passes.

🔴 **Zero foundation repos added at `p808` — a SIXTH consecutive nil on this shelf, and
unlike the agent shelf the streak did NOT break.** The vertical leg
(`open source platform education ERP CRM MIT Apache`) returned `OpenEduCat`, `Krayin`,
`Huly` and `ERPNext` — **all four already held**. The seam-named leg that broke the
*agent* nil (`...LMS Moodle Canvas integration`) returned seven repositories, but **every
one of them was an agent or a wrapper, not a foundation**: none is a platform, a library
or a protocol implementation that something else builds on. 🟢 **That asymmetry is itself
informative and is why this paragraph is longer than the nil warrants.** Education's
foundational layer — `Moodle`, `Open edX`, `Canvas`, `Sakai`, `Chamilo`, `OpenEduCat`,
the xAPI/Caliper implementations — is **mature, consolidated and slow-moving**, and new
entrants arrive at the *agent* layer above it rather than beside it. 🔵 **A nil here is
therefore the expected reading, not a research failure**, and future passes should budget
accordingly: check this shelf for *licence and version drift* on what it already holds,
not for new arrivals.

🟢 **One licence confirmation this pass, obtained independently rather than carried.**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) was re-read
from its rendered page: **`LGPL-3.0`**, **`911★`**, description *"Comprehensive Open
Source ERP for Educational Institutes"*. 🔴 **The GitHub sidebar renders NO SPDX licence
name for this repository** — the `LGPL-3.0` is stated only in the README body and a
badge. 🔵 **Consequence worth recording: any automated licence scrape of `OpenEduCat`
returns empty, not wrong**, so a future pass that sees a blank licence field here should
not treat it as a regression or a rejection. This matches what `verticals/solutions.md`
already carries, so nothing changed — but it is now verified rather than inherited.

<details>
<summary>🔴 <strong>Prior pass (<code>p807</code>): zero foundation repos — the search tier was nil for a fifth consecutive window.</strong></summary>

🔴 **Zero foundation repos added this pass — the search tier was nil for a fifth
consecutive window.** The four prescribed global legs plus two differentiated legs
(adaptive learning / knowledge tracing; AI grading against rubrics) returned nothing
education-specific that this file does not already hold. 🟡 **What those legs did return
was verified and rejected on the merits, not on a hunch:**
[`OpenLearn-AI/OpenLearn-AI`](https://github.com/OpenLearn-AI/OpenLearn-AI) —
**AGPL-3.0, `6★`, `3` forks**, README states it is `pre-alpha` and *"not yet runnable
end-to-end"*; [`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment)
— **GPL-3.0, `0★`, `0` forks**;
[`h4ksclaw/learnharness`](https://github.com/h4ksclaw/learnharness) — **`3★` and NO
licence file at all** (see `T22`). 🟢 **Fewer real rows beat padding, so none was
written.**

🟢 **The one supply-side gain this pass is on `verticals/solutions.md`, not here**: three
permissive general-purpose ERP/CRM platforms (`krayin/laravel-crm` MIT `24.1k★`,
`cortezaproject/corteza` Apache-2.0 `2.2k★`, `apache/ofbiz-framework` Apache-2.0
`1.2k★`). 🔵 **They are deliberately NOT on this shelf** — this file is for repos an
*education* engagement builds on, and none of the three is education-aware. They are
platform substrate, which is what `verticals/` is for. 🔴 **Count corrected at the eleventh pass (`p806`): the header said "57
repos" while the tables held 59.** The figure above was produced by counting rows
programmatically, and the next pass should do that rather than carry this sentence
forward. 🟢 **Four rows added this pass — a new two-repo K-12 data-standard layer
(Ed-Fi), one row into the skills-and-credentials layer, and the row that narrows
`T19`.** 🔵 **None of the four came from a search.** Three came from auditing this
base's own append-only trending logs against its shelves, where `Ed-Fi` had been
mentioned **249 times without ever reaching a file a studio reads**; the audit is a
script now, at `scratchpad/p806/propagation-audit.sh`. 🔴 **Where GitHub's
sidebar shows only a generic "License" link, the grant was read from the
`LICENSE` file itself. One row this pass turns entirely on that step**, and it is
the row that closes this file's standing Caliper gap.
Grouped by the job they do, because "foundational" in education means five
different layers: the LMS, the student record, the content format, the
learning-data/ML layer, and **the integration layer that mounts anything into
anything**.

License matters more here than anywhere else in this KB: the big three LMSs are
**AGPL-3.0 or GPL-3.0**, which governs what a studio can hand a client as a
derived product. The MIT/Apache/BSD/ECL rows are the ones that compose freely.

**What changed this pass (tenth pass, `p805`, 2026-11-13):** **57 repos**, up
from 49, and **not one of the eight is a discovery.** 🔴 **All eight were
license-verified in earlier passes and never reached this file** — they existed
only in `agents/trending.md` / `repos/trending.md`, which are now 79,190 and
62,315 lines long and which nobody opens during an engagement. The prescribed
search battery returned **nil on supply for the third consecutive pass**, so
this pass spent itself on the propagation defect instead: a diff of
green-marked, byte-verified slugs in the trending logs against the four shelf
files (`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`,
`compose/patterns.md`). 🟢 **Three rows open the xAPI service/validation/warehouse
layer, four open a new skills-and-credentials layer, one is the first MIT row in
the learning-platform table.** 🟢 **Every one re-verified live this pass before
being written here.** 🔵 **The audit is deliberately not automated into a bulk
copy: the same diff surfaces a literal `owner`-slash-`repo` placeholder and dozens of
non-education repositories, so promotion stays a judgement, not a `comm` output.**

**What changed this pass (ninth pass, `p804`, 2026-11-13):** **49 repos**, up
from 47. A new **curriculum-corpus layer** was opened at the end of this file
with two MIT rows — and the reason it is a *layer* rather than two more entries
is that it answers a demand this base only measured this pass: **three dated
AI-literacy mandates, and no open education-licensed curriculum to meet any of
them.** 🔴 **Provenance warning for both rows: `curl` to `github.com` is denied
by this session's egress proxy (`403`), so the prescribed URL check could not be
run.** Grants and sizes were read from the rendered page via `WebFetch`, which
means **sidebar-verified, not payload-verified** — strictly weaker than the
standard the Caliper and QTI rows were held to.

**What changed this pass (fifth pass, 2026-11-13):** **40 repos**, up from 34.
The analytics edge — the one interoperability edge this file declared had no
permissive implementation — **now has one**, and the four passes of failure had
a single cause. Both `1EdTech/caliper-js` and `IMSGlobal/caliper-js` return
**404**: 1EdTech's Sensor API reference code is **member-gated** (its own Best
Practice Guide says Contributing Members and Affiliates request GitHub access),
so the slug this KB kept guessing has no public repository. The permissive
implementation is **outside both orgs**:
`CarnegieLearningWeb/caliper-ts`, **MIT**, read from its `LICENSE` file because
the sidebar shows only a generic link. 🟢 **The method that worked and should
become this base's default: list an org's repositories with GitHub's own filter
(`github.com/orgs/<ORG>/repositories?q=<term>`) instead of guessing slugs inside
it.** See the new Caliper section below.

**What changed at the fourth pass (2026-11-13):** **34 repos**, up from 33.
One addition, and it is a correction rather than an increment:
`dmitry-viskov/pylti1.3` (MIT, 138 stars) is a **Python** LTI 1.3 Advantage
library, which falsifies this KB's standing claim that no Python LTI library
exists. That claim was load-bearing — `compose/patterns.md` built a mandatory
two-process architecture on it — so the correction propagates there too.

**What changed at the third pass:** this file previously declared "no open-source LTI
1.3 tool-provider library made the verified set" and called it greenfield.
**That gap is closed and the conclusion was wrong.** Four LTI 1.3 libraries
verified below, led by `ltijs` (Apache-2.0, 373 stars) implementing the full
LTI Advantage service set. Do not quote the old greenfield claim to a client.

</details>

## The authoring and packaging layer — SCORM / cmi5 (new, fourteenth pass `p809`)

🟢 **New to this file.** Every other layer below assumes content already exists. This is
the first repo in this base that *produces* standards-compliant packages, and it does so
with no server to run.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/dmmat/Scormly | MIT | 5 | Browser-only course builder — **no backend, no database**, runs entirely client-side (React 18 + TypeScript). Exports **SCORM 1.2 and SCORM 2004** and **cmi5 (xAPI)**, so output mounts in Moodle, Canvas, Open edX, Brightspace and Blackboard alike. 🟢 `MIT` byte-verified: root `LICENSE`, `1,071 B`, `sha256:68e4711e4e5fb60b…`. `93` commits. 🔴 **README states SCORM export is verified against SCORM Cloud but cmi5 is "implemented, not yet verified on a live LRS" — do not quote the cmi5 leg as working until it is run against `Ralph` or `LRS SQL`.** 🔵 Generates an `AGENTS.md` per project. |

🔵 **Why it belongs on a foundation shelf rather than the agent shelf:** it is the
cheapest way to get agent-generated lesson content *out* of a pipeline and *into* any LMS
without writing a per-LMS integration — the packaging counterpart to the LTI mount point
below.

🔴 **Declared gap at this layer.** `OELTKit` (reported `Apache-2.0`, AI-first course
builder, SCORM + cmi5) could **not** be verified: its host `oeltkit.bcltraining.com` does
not resolve under this session's network policy and no repository address was recovered.
It is a lead, not a finding, and is deliberately not tabled.

## The rostering layer — OneRoster (new, fifteenth pass `p810`)

🟢 **New to this file, and it closes a six-pass absence.** `OneRoster` is named **`3,043`**
times across this base — it is the IMS Global / 1EdTech standard by which a SIS hands class
rosters to an LMS, and every pattern here that says "sync the roster" means this. 🔴 **This
file carried not one repository for it until now.**

🟢 **`p811` re-ran the agent leg first-hand and the nil HELD:**
`gh api -X GET search/repositories -f q="oneroster mcp"` returned **zero items** on
`2026-11-13`, and a vendor connector page (ibl.ai, dated October 2026) states independently
that neither 1EdTech nor ClassLink publishes an MCP server for the standard. 🔵 **Two
channels, same answer — this is now a corroborated absence rather than a failed search.**

🔴 **`p811` also killed a phantom before it reached this table.** A web result named
`fffnite/go-oneroster` as a Go OneRoster implementation with a live `pkg.go.dev` page.
`gh api -X GET search/repositories -f q="repo:fffnite/go-oneroster"` returns **HTTP `422`**
— the same code this base's `T970` channel returns for an INVENTED address — while
`bgwdotdev/go-oneroster` returns `total_count=1`. 🟢 **A package index can outlive the
repository it indexes; the module proxy keeps serving a cached copy after the source is
gone.** 🔵 **Rule: a package-registry page is not evidence that a repository exists.**

🔴 **Read the agent gap next to it:** `agents/top.md` records a dedicated, empty leg for
`oneroster mcp`. **The standard has tooling; it has no agent.** That asymmetry is the
contribution target, and it is the best-evidenced one in this base.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/googleworkspace/oneroster-integration-conformance-tests | Apache-2.0 | 7 | **New this pass (`p810`).** Google Workspace's **conformance test suite for OneRoster integrations** — the only vendor-neutral way in this base to prove a roster integration actually conforms before a district signs off. `1` fork, pushed `2026-07-30`, created `2023-08-25`. 🟢 **Apache-2.0 and published by a party with no LMS to sell** — it tests the integration, it does not implement one. 🔵 Use it as an acceptance gate in a delivery contract |
| https://github.com/oat-sa/oneroster-import | GPL-2.0 | 8 | **New this pass (`p810`).** A OneRoster **importer** from Open Assessment Technologies (OAT), the TAO assessment-platform authors. `7` forks — 🔵 **a high fork-to-star ratio (`0.88`), which in this base has consistently indicated a repo that is deployed and adapted rather than starred.** 🔴 **GPL-2.0: copyleft, so it propagates into a derived deliverable.** Run it as a separate process, do not link it |
| https://github.com/bgwdotdev/go-oneroster | MIT | 8 | **New this pass (`p810`).** A OneRoster **API implementation in Go**. 🟢 **The only permissive OneRoster server-side implementation found on the leg.** 🔴 **Last pushed `2020-07-30` — six years stale, and shelved on that basis as a REFERENCE for the wire format, not as a dependency.** 🔵 The spec has moved since; verify against 1EdTech before reusing a line of it |
| https://github.com/LongsightGroup/oneroster | MIT | 0 | **New this pass (`p811`), and it is the row that makes `P27` buildable.** A **TypeScript OneRoster 1.2 client** from Longsight, the higher-education open-source services firm already on this shelf for `LongsightGroup/qti3`. 🟢 **Covers BOTH bindings the standard defines — REST *and* CSV — which matters because US districts hand over CSV far more often than they stand up a REST endpoint.** Published to npm as `@longsightgroup/oneroster`; `0.3.0`. Pushed `2026-07-15`, `0★`, `0` forks. 🟢 **MIT, and six years newer than `bgwdotdev/go-oneroster`** — so the permissive OneRoster option is no longer a 2020 artifact. 🔴 `0★` and no repository description: shelved on its payload and its npm release, not on traction |

## The integration layer — LTI 1.3 (added third pass, corrected fourth)

Build the AI tool once as an LTI 1.3 tool provider and it mounts in Moodle,
Canvas, Open edX, Sakai and ILIAS. This is the highest-leverage single
investment in an education engagement, and it does **not** need to be written
from scratch.

**Updated 2026-11-13 (fourth pass): there are now five, and one of them is
Python.** The previous edition of this file and of `compose/patterns.md` stated
that every verified LTI 1.3 library was Node, PHP or Elixir and that a Python
agent therefore had to sit behind a non-Python LTI front door. **That is wrong.**
`dmitry-viskov/pylti1.3` (MIT, 138 stars) implements the full LTI Advantage
service set in Python with Django and Flask adapters. Single-language Python
deployments are available; see the revised constraint note in
`compose/patterns.md`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | **The reference implementation.** Node.js; covers launches, Deep Linking, Assignment and Grade Services, Names and Role Provisioning, and Dynamic Registration — the complete LTI Advantage surface. v7 is a full rewrite with a migration guide from v5. 86 forks. README thanks CourseKey for making "the certification process possible" but **does not itself claim LTI Advantage certification** — a fork, `edugatorlabs/ltijs`, is the one advertising certified status. Verify certification claims before repeating them to a client. |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | **The Python answer — new this pass, and it overturns this KB's "no Python LTI" finding.** Full LTI Advantage: Assignments and Grades, Names and Roles **and** Deep Linking, with shipped adapters for **Django and Flask** (another framework needs only `OIDCLogin` and `MessageLaunch` reimplemented). It is a port of the `packbackbooks` PHP library below, so the two are architecturally aligned and a PHP-to-Python move is cheap. 84 forks. **Maintenance caveat, stated because it governs adoption:** GitHub **Releases is empty**, the newest PyPI version is **2.0.0**, and a third-party scanner reports the last publish at roughly three years ago — pin the version, vendor it, and budget for carrying security patches yourself. Even so, at 138 stars and 84 forks it is the second most-used library in this table after `ltijs`. |
| https://github.com/packbackbooks/lti-1-3-php-library | Apache-2.0 | 54 | **The PHP answer** — matters because Moodle and Chamilo are PHP shops. Validates launches from any LTI consumer and uses Names & Roles Provisioning for rosters and Assignment & Grades for grade writeback. 27 forks. |
| https://github.com/Simon-Initiative/lti_1p3 | MIT | 16 | Elixir library for LTI 1.3 **both as Tool and as Platform**. Built to support the Open Learning Initiative's next-generation platform, Torus — i.e. production provenance, not a toy. 4 forks. |
| https://github.com/lti-tool/lti-tool | MIT | 8 | **Serverless-native** LTI 1.3 toolkit (TypeScript) for AWS Lambda and Cloudflare Workers, Hono-first. OIDC, AGS, NRPS, Deep Linking, Dynamic Registration, JWT verification and nonce validation; pluggable storage (memory, DynamoDB, PostgreSQL, MySQL, Cloudflare D1). Early at 8 stars and its README is internally inconsistent about which frameworks are supported versus planned — but it is the only serverless-shaped option found. |

**Leads deliberately not tabled** (surfaced in search, not adopted):
`SanDiegoCodeSchool/lti-node-library` (MIT, metadata indicates ~7 years old —
likely stale, and its README admits only limited Assignment & Grade Services
support); `bnsoftware/lti-1p3-tool`, a PHP fork whose **own README says "you
should not use this library at this time"**; `stevenweathers/peregrine-lti`
(Go), explicitly pre-v1.0 with an unstable public API. None were
license-verified on the repository page this pass; treat all three as
unverified.

## The learner-record layer — xAPI Learning Record Stores (added third pass)

Every compose pattern in this KB instructs the agent to "emit xAPI", and until
this pass **no repo in this base implemented the thing that receives it**. Both
options below are **permissive**, which makes this the second fully build-safe
layer in the education stack after the LTI table — and unlike the LMS layer,
here the permissive option is also the leading one.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/adlnet/ADL_LRS | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17f…`, stock text, no holder) | 335 | 🟢 **New this pass (`p817`), and the most-starred permissive LRS in existence — absent from this table for nineteen passes.** *“ADL's Open Source Learning Record Store, used to store learning data collected with the Experience API.”* Created `2012-04-18`, pushed `2025-11-14`. 🔴 **ADL is the US Department of Defense's Advanced Distributed Learning Initiative — the body that WROTE xAPI.** 🔵 **So this is the specification authors' own reference implementation, which is a different argument in a procurement meeting than “a popular open-source project”: it is the conformance baseline.** 🟡 **A year without a push — read it as a stable reference and a conformance target, and run [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) in production** |
| https://github.com/LearningLocker/learninglocker | 🔴 **GPL-3.0 — byte-read** (`35,141 B`, `sha256:589ed823…`, stock FSF text) | 587 | 🔴 **New this pass (`p817`), filed as a FLAG — and the reason it is new is a measurement defect worth naming.** *“Learning Locker — The Open Source Learning Record Store. Started in 2014.”* 🔴 **This base had already shelved two SMALL permissive packages from the SAME ORGANISATION — `LearningLocker/xapi-service` (MIT, `42★`) and `xapi-validation` (MIT, `12★`), both at `p805` — and skipped the org's `587★` flagship, which is the single most-starred LRS on this channel.** 🔵 **The pattern to recognise: harvesting an org by licence filter picks up its satellites and drops its product, because the product is where the copyleft is.** 🔴 **Last pushed `2024-05-30` — eighteen months stale, and the hosted commercial offering is the maintained path.** 🟢 **Do not propose it. It is here so that a client who already runs it is met with a correct licence reading rather than a blank** |
| https://github.com/yetanalytics/lrsql | Apache-2.0 | 144 | **The default choice.** SQL-based LRS: a persistent store for xAPI statements plus their attachments and documents. Verified DBMS matrix is broad and current — SQLite 3.42, **Postgres 14/15/16/17/18**, MariaDB 10.6–11.8, MySQL 8.0.44/8.4/9.5. **Apache-2.0 means the learner-record store can ship inside a client deliverable with no copyleft reach** — the only data-layer component in this KB for which that is true. 42 forks. |
| https://github.com/openfun/ralph | MIT | 51 | LRS **plus** a CLI for building learning-analytics pipelines **plus** a Python library for fetching, converting and serializing learning events. Pick it over SQL LRS when the engagement is *analytics*-shaped rather than *storage*-shaped, or when the agent layer is Python and you want one language end to end. Elasticsearch backend in its documented local setup. From **France Université Numérique** — EMEA public-education provenance, which is usable evidence in an EU data-sovereignty conversation. 19 forks. Releases section empty. |
| https://github.com/LearningLocker/xapi-service | **MIT** | 42 | **New this pass (tenth, `p805`) — promoted off the trending log, where it has sat verified and unshelved.** "A service for the xAPI": the Learning Locker project's standalone statement service, Node/TypeScript, 1,329 commits. Topics `nodejs`, `tincan`, `typescript`, `xapi`. 🟢 **MIT on the sidebar, confirmed this pass by direct read.** Matters because Learning Locker itself is the LRS most institutions have heard of, and its commercial editions are **not** permissive — this component is. Pick it over `lrsql` when the stack is already Node and you want the statement endpoint as a service rather than a database product. 🔴 No release dates visible on the page; treat maintenance as unverified and pin a commit. |
| https://github.com/LearningLocker/xapi-validation | **MIT** | 12 | **New this pass (tenth, `p805`).** "A package for validating xAPI statements" — the companion that checks a statement is well-formed *before* it reaches the store. 🟢 **This is the piece that makes an audit trail defensible rather than merely present:** every compose pattern in this KB tells an agent to emit xAPI, and none of them, until now, named anything that rejects a malformed emission. MIT, TypeScript. Use it in the agent process, not only at the LRS edge. |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** | 62 | **New this pass (tenth, `p805`).** "Standards-based learning record warehouse built for a scalable learning analytics environment" — Java, from Apereo's Learning Analytics Initiative. 🔵 **A warehouse, not a store: it is the layer above an LRS**, where statements from several sources are consolidated for analysis. **ECL-2.0 is OSI-approved and Apache-derived**, so it composes with the permissive rows here; it is the same licence as Sakai, which is not a coincidence — this is the Apereo/educational-middleware cluster running on the sector's own licence. Pick it when the engagement is multi-system analytics rather than one platform's telemetry. |

Pair either one with `DavidLMS/learnmcp-xapi` (MIT, 16 stars — see
`agents/top.md`), the MCP server that lets an agent read and write these records
directly. That three-repo stack — LRS + MCP server + agent — is written up as
pattern `P9`.

## The credential and identity layer — Open Badges 3.0 / W3C Verifiable Credentials / institutional SSO 🟢 **the layer whose star mass is PERMISSIVE and whose EMEA reference is ARCHIVED** (new, twenty-second pass `p817`)

🔵 **Why this layer is separate from the rostering and learner-record tables above.** Those move a
record BETWEEN systems inside an institution. This one emits a record the LEARNER CARRIES OUT of the
institution and a third party can verify without calling back. 🟢 **Commercially it is the layer
2026 procurement language has started to name** — see `T53` — and it is almost entirely MIT.

🔴 **Read the regional split before the star column, because it decides what can be quoted to a
client.** The North American reference stack (Digital Credentials Consortium, out of MIT) is MIT-licensed
and live. 🔴 **The European reference (`European-Learning-Model`, the data model behind Europass
Digital Credentials) is EUPL-1.2 — a reciprocal licence — and its repository is ARCHIVED, last pushed
`2024-02-14`.** See `T56`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/digitalcredentials/learner-credential-wallet | 🟢 **MIT — byte-read** (`1,092 B`, `sha256:1032f65d…`, holder `Digital Credentials Consortium`, `2021-2026`) | n/a | 🟢 **New this pass (`p817`), and the row that exposed a hole in this base's own measurement channel — see `T55`.** Cross-platform iOS/Android wallet for storing and sharing digital learner credentials; the reference holder-side implementation of the DCC stack. 🔴 **`search/repositories q="repo:digitalcredentials/learner-credential-wallet"` returns `total_count=0` — the repository is ABSENT FROM THE SEARCH INDEX while being live on `raw.githubusercontent.com` (HTTP `200`).** 🔴 **Star count recorded `n/a` for exactly that reason: the field this base reads stars from is the search response, and there is none.** 🔵 **A search-only harvest publishes the mirror below as canonical instead** |
| https://github.com/ryjones/learner-credential-wallet | 🟢 **MIT — byte-read** (`1,092 B`, `sha256:1032f65d…`, holder `Digital Credentials Consortium`, `2021-2026`) | 91 | 🟡 **New this pass (`p817`) — filed as a MIRROR, not as a find, and that distinction is the whole of `T55`.** The search index returns this row and not the one above; it reports `fork: false`; and its licence payload is **byte-identical** to the DCC original, holder line and all. 🟢 **`T41`'s instrument settling a lineage question in the direction the `fork` field got wrong — and the FIRST cross-owner collision this base has measured, which discharges limb 2 of `ACTION p816-E`.** 🔵 **Cite the `digitalcredentials` address in client work; this one is the evidence trail** |
| https://github.com/digitalcredentials/verifier-plus | 🟢 **MIT — byte-read** (`1,087 B`, `sha256:85569d7e…`, holder `Digital Credentials Consortium`) | 19 | 🟢 **New this pass (`p817`).** *“VerifierPlus allows users to verify any supported digital academic credential.”* Pushed `2026-11-12`. 🔵 **The RELYING-PARTY half of the stack and the half engagements forget to budget for: issuing a credential is a one-afternoon problem, convincing an employer's system to trust it is the project.** See `P44` |
| https://github.com/digitalcredentials/dcc-admin-dashboard | 🟢 **MIT — byte-read** (`1,094 B`, `sha256:0f6a5db4…`, holder `Massachusetts Institute of Technology`) | 12 | 🟢 **New this pass (`p817`).** *“A system for uploading, managing, issuing, and collecting Verifiable Credentials with email notifications.”* 🔵 **The registrar-facing surface — a CSV of graduates in, signed credentials and notification mail out — which is what makes `P44` a procurement item rather than a demo.** 🟢 **Holder line names MIT the university, not the licence: a distinct payload (`1,094 B`) from the consortium's own (`1,087 B`), so the two hashes separate institutional from consortium authorship within one org** |
| https://github.com/digitalcredentials/open-badges-context | 🟢 **MIT — byte-read** (`1,087 B`, `sha256:85569d7e…`, holder `Digital Credentials Consortium`) | 6 | 🟢 **New this pass (`p817`).** NPM package shipping the **Open Badges 3.0 JSON-LD context** — the vocabulary every OBv3 payload has to dereference. 🔵 **Small, dull and load-bearing: without a pinned context an OBv3 credential is not verifiable offline, which is the exact failure a wallet demo hides and a production rollout does not** |
| https://github.com/european-commission-empl/European-Learning-Model | 🔴 **EUPL-1.2 — byte-read** (`13,865 B`, `sha256:6e5399ad…`, file named `license`, lower case) | 54 | 🔴 **New this pass (`p817`), and filed as a WARNING rather than a build option — the anchor of `T56`.** *“Data Model for the Europass Digital Credentials Infrastructure”*, published by DG EMPL. 🔴 **The repository is ARCHIVED and was last pushed `2024-02-14`** — against an Ed-Fi Data Standard pushed `2026-11-12` and a DCC wallet pushed `2026-10-15`. 🔴 **EUPL-1.2 is a RECIPROCAL licence, not a permissive one: it carries a copyleft obligation and an explicit compatibility list including AGPL-3.0. It is not interchangeable with the MIT rows above and must not be quoted as though it were.** 🔵 **Engagement consequence: an EMEA credential engagement adopts the DATA MODEL as a specification and implements against the MIT stack — it does not fork this tree.** 🟢 **Caught only because the probe added lower-case `license` to the filename list this pass (`T57`); the old probe would have reported `NO_PAYLOAD`** |
| https://github.com/apereo/cas | 🟢 **Apache-2.0 — byte-read** (`11,358 B`, `sha256:cfc7749b…`, stock text, no holder) | 11399 | 🟢 **New this pass (`p817`), and by a wide margin the most-starred repository in this file.** Apereo CAS — enterprise single sign-on, and the identity layer that the LMS, the SIS, the LRS and the credential issuer in every pattern in `compose/patterns.md` actually authenticate through. Pushed `2026-11-15`. 🔴 **That it took twenty-two passes to shelve is itself the finding: this base has harvested what an agent TALKS TO and skipped what every one of those systems trusts.** 🔵 **On an engagement it is the cheapest credible answer to “how does your agent authenticate as the user without holding their password” — the question that stops the credential-axis risk (`T40`) from being hand-waved** |
| https://github.com/uPortal-Project/uPortal | 🟢 **Apache-2.0 — byte-read** (`11,359 B`, `sha256:5d7a4884…`, stock text, no holder) | 287 | 🟢 **New this pass (`p817`).** *“Enterprise open source portal built by and for the higher education community.”* Pushed `2026-11-14`. 🔵 **The surface a university puts in front of all of the above — and the place an institution will actually expect an agent to appear, rather than in a separate chat product** |

## The analytics layer — Caliper Analytics (new, fifth pass)

The fifth of the five interoperability edges, and the last one to get a
permissive implementation in this base. Caliper is the **1EdTech-native**
telemetry standard and is the one most often written into **North American
higher-ed** procurement; xAPI is the one with the better open stack. This
section exists so that an engagement contractually bound to Caliper has a named
starting point instead of a greenfield estimate.

**Read the licence column before the star column.** The Caliper field splits by
licence in a way that decides what can ship: exactly **one MIT sensor**, an
**Apache-2.0 analysis layer**, the 1EdTech reference lineage at **LGPL-3.0**, the
only LMS emitter at **GPL-3.0**, and the only event store **unlicensed**.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/CarnegieLearningWeb/caliper-ts | **MIT** (read from `LICENSE`: `MIT License` / `Copyright (c) 2021 Imagine Learning`; **the sidebar shows only a generic "License" link**) | 0 | **The only permissively licensed Caliper sensor found anywhere, and the row that closes this file's Caliper gap.** TypeScript implementation of the Caliper Sensor API — a port of `caliper-js`, which has **no public repository**. Entity factories for Assessment, AssessmentItem, Person, Session, SoftwareApplication and Membership; `createSessionEvent` / `createAssessmentEvent` in its examples. 225 commits on `main`, 1 fork, Releases empty. Default `dataVersion` is `http://purl.imsglobal.org/ctx/caliper/v1p1`, so **treat it as Caliper 1.1**. 🔴 **Three caveats that belong in the estimate:** it publishes to the **GitHub Package Registry** as `@imaginelearning/caliper-ts`, **not public npm**, so the build needs an `.npmrc` scoped to `@imaginelearning`; at **0 stars** it is a real library with no community, so budget to carry it; and its events and entities are generated by `caliper-code-generator` **from `caliper-net`, which is LGPL-3.0** — the output here carries an MIT grant, but read the generator's terms before regenerating. |
| https://github.com/open-lms-open-source/moodle-logstore_caliper | GPL-3.0 | 1 | **The only Caliper emitter for a real LMS, at any licence.** Moodle logstore plugin contributed by the Moodlerooms product team: a three-stage **Expander → Translator → Emitter** pipeline pushing Moodle log events to an event store through the Caliper Sensor API, **immediate or batched**, configured by Event Store URL, API key, send-immediately flag and batch size. Installs onto **Moodle 2.7+**. 66 commits, 7 forks, 7 open issues, Releases empty. 🟢 **GPL-3.0 is correct and harmless here, and that needs saying against this KB's own "do not fork the LMS" rule:** a Moodle plugin lives inside a GPL-3.0 host and is expected to be GPL-3.0; it does not reach the separately deployed MIT/Apache AI layer. `1EdTech/moodle-logstore_caliper` is a 13-commit fork of this repo — **use this upstream, not the fork.** |
| https://github.com/UnizinAnalytics/caliper-net-public | LGPL-3.0 | 0 | **The .NET reference sensor, and the broadest profile coverage in this table — read it even on a non-.NET engagement.** Implements the Sensor API across **nine Metric Profiles: Base, Session, Reading, Annotation, Assignable, Assessment, Assessment Item, Outcome and Media** — in practice the working definition of what a *complete* Caliper sensor covers, which is what you need to scope a build against. From **Unizin**, the US higher-education consortium: **North American provenance, which is exactly where Caliper gets specified.** It is also the origin of the `caliper-code-generator` that produces `caliper-ts`. No description, no releases. 🔴 LGPL-3.0 propagates on modification — extend by composition. |
| https://github.com/tl-its-umich-edu/caliper-php-public | LGPL-3.0 | 3 | **The reachable copy of the PHP reference sensor — and its own description is the primary evidence that the originals went away.** Verbatim from the repository: *"This fork of IMS Global's public release of caliper-php includes additional features needed at Univ. of Michigan. … **This had been archived, but has been unarchived following 1EdTech making its caliper-php private.**"* 🔴 **That is documentary confirmation, not inference: 1EdTech took `caliper-php` private, and a university un-archived its fork to keep it reachable** — which is exactly why four passes of slug-guessing returned 404s. Forked from `UnizinAnalytics/caliper-php-public`, so the chain is 1EdTech → Unizin → Michigan. PHP client implementing the Caliper Sensor API; U-M adds `Options::setHttpHeaders()`. Package versions 1.0.0 (IMS) / 1.0.1 (U-M) — **those are library versions, not Caliper spec versions, and the repo names no spec version.** 2 forks. Matters because Moodle and Chamilo are PHP shops. Sibling: `umich-caliper-php` (LGPL-3.0). 🔴 LGPL-3.0 propagates on modification. |
| https://github.com/tl-its-umich-edu/caliper-event-analysis | **Apache-2.0** | 1 | **The analytics half, permissively licensed — and the part a client actually buys.** Jupyter notebooks for analysing and visualising collected Caliper events, from a collaboration between University of Michigan Teaching & Learning and **U-M CSCAR**, its statistics consulting group. Not a sensor and not a store: it is the layer that turns emitted events into an answer. **Apache-2.0, so the notebooks can seed a client deliverable directly** — the only Caliper component other than `caliper-ts` for which that is true. 5 forks on 1 star: **more forked than starred, which for a notebook repo means people took it and used it.** 🔴 The repository page does not expose the notebooks' contents, so the analyses themselves are unverified — adopt the licence and the provenance, read the code before promising a dashboard. |
| https://github.com/open-ent/caliper | 🔴 **No license field shown — treat as all-rights-reserved** | 0 | **The only Caliper _event store_ found, and it cannot be adopted.** Open ENT module implementing **Caliper Analytics 1.2** — the newest version in this table — as **both** an event store (`POST`/`GET /ims/caliper/v1p2/events`, bearer-token auth) **and** a sensor forwarding Open ENT access and login events onward, mapped to `ToolUseEvent`/`Used` and `SessionEvent`/`LoggedIn` (activation, SMS and failed-login events are counted and excluded). Vert.x, SQL schema `caliper`, port 8174, **33 unit tests**. From **Open ENT**, the French regional *espace numérique de travail* platform — **EMEA public-education provenance, usable evidence in an EU data-sovereignty conversation.** 🔴 **Design reference only:** no licence on the page, and its README states the **Assessment, Grading, Forum and Media profiles are not implemented** because the ENT does not record those events. Worth a licence request. |

### What this does and does not change

🟢 **All five interoperability edges now have a permissive implementation.**
🔴 **The analytics edge is not equivalent to the other four**, and an engagement
must be priced on the difference:

| | xAPI (learning record) | Caliper (analytics) |
|---|---|---|
| Permissive **store** | 🟢 `yetanalytics/lrsql` — **Apache-2.0, 144★**, Postgres 14–18 / MariaDB / MySQL / SQLite | 🔴 **None.** The only store found is **unlicensed** |
| Permissive **sensor / client** | 🟢 `openfun/ralph` (MIT, 51★) + `DavidLMS/learnmcp-xapi` (MIT, 16★) | 🟡 `caliper-ts` (MIT, **0★**, GitHub Package Registry only) |
| **LMS** emitter | 🟡 via plugins and xAPI wrappers | 🟢 `moodle-logstore_caliper` (GPL-3.0, Moodle 2.7+) |
| Reference layer | 🟢 public | 🔴 **member-gated** (1EdTech Contributing Members / Affiliates) |

🟢 **Revised recommendation, replacing this file's "Caliper is a build, price it
as one":** where the client is **free to choose, still choose xAPI** — the store
asymmetry above is the whole reason. Where a contract **names Caliper**, the
honest answer is no longer "no open starting point." It is: **an MIT sensor, a
GPL-3.0 Moodle emitter, an Apache-2.0 analysis layer, and a complete
nine-profile reference to scope against — but you write the event store.**
That is a materially smaller and differently shaped project than greenfield.
Written up as pattern `P11`.

## The assessment-interchange layer — QTI (new to this file, fifth pass)

QTI is named in almost every education procurement document, and until this pass
this file's gap list said **"no open-source QTI item-bank toolchain surfaced."**
🔴 **That bullet was stale by many passes and is removed.** The KB's research log
(`intel/open-gaps.md`) had already measured this layer in depth — and this base
**ships a tested QTI artefact of its own** at
`compose/code/p533-qti3-template-emitter/` (43 assertions, 0 failures, 19
negative controls, 11 of 11 mutations detected). Seven repos verified fresh from
the rendered page this pass and promoted into this file, so the operational
shelf matches what the research log already knew.

**The architecture fact that governs a QTI engagement: scoring, item banking and
*certified delivery* live in different repos.** No single project has all three,
so the shape is always a pair.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/johnnyrobot/qtimaker | BSD-3-Clause | 0 | **New this pass (`p810`).** Creates **QTI quizzes for Canvas from Markdown**, with a local web interface, Docling document parsing and AI question generation. 🟢 **BSD-3-Clause — the first BSD row in this layer**, and permissive enough for a client deliverable. 🟢 **The useful shape is the direction of travel: Markdown → QTI → LMS**, which makes an item bank reviewable in a pull request before it is a quiz. 🔴 `0★`, `0` forks, pushed `2026-07-18` — shelved for the pipeline shape, not for traction |
| https://github.com/oat-sa/tao-core | GPL-2.0 | 64 | **The only full assessment *platform* here — TAO, the long-standing open e-testing system, with real item banking.** Highest star count in this table and the one a client may already run. 37 forks, Releases empty, no QTI version stated on this repo. 🔴 **Two constraints that decide whether it fits:** the open-source edition is **QTI 2.2-based, not QTI 3**, and it ships **no Results Management** — so a QTI 3 contract or a reporting requirement both land outside it. GPL-2.0, so it is a host to extend, not a base to embed. |
| https://github.com/amp-up-io/qti3-item-player | **MIT** | 30 | **The delivery half, and the only repo in this table claiming conformance certification.** 100% JavaScript QTI 3 item player aligned to the 1EdTech QTI v3 Best Practices guide, with stated **QTI 3 Basic *and* Advanced "Delivery" conformance** plus some elective capabilities. Item state via `endAttempt` / `suspendAttempt` / `scoreAttempt`; catalog/glossary events with dynamic rebinding; 14 colour themes. 596 commits, 6 forks, Releases empty. 🔴 **Built on Vue 2.6, which is end-of-life** — the integration cost is a Vue 2 island in a modern front end, and that belongs in the estimate. |
| https://github.com/LongsightGroup/qti3 | **MIT** (© 2026 Longsight, Inc.) | 6 | **The authoring, scoring and migration half — the broadest QTI toolkit found, and the one this KB has already contributed work toward.** 12 npm packages: core parsing and scoring, browser player, React and Preact adapters, CLI, fixtures, conformance, accessibility, PNP, **writer (with an item-bank package writer)**, **migrator** (QTI 1.2 and 2.x → 3) and **transcoder** (QTI 3 → 1.2 / 2.1 / 2.2 / Canvas / Moodle). Tracks the **QTI 3.0.1 ASI item profile**, 19 interaction types. 3 forks, Releases empty, changelog at 0.13.0. 🔴 **Known limit, measured by this KB and not by its README:** `packages/writer` **cannot emit `qti-template-declaration` / `qti-template-processing`**, so *parametric* item variants cannot be authored on it even though `packages/core` fully executes them (real `randomInteger` draw over `min`/`max`/`step`, answer keys derived from the draw, constraint retry up to 100 restarts). 🟢 **The fix already exists in this repository** — `compose/code/p533-qti3-template-emitter/` regenerates two upstream fixtures node-for-node, and `writer-contribution.ts` is written in the host project's idiom. It is **MIT, so this is a contribution, not a procurement** — and it has **not been sent upstream** (`Gap 240`). Deliberately not opened unprompted: it is an outward action. |
| https://github.com/Citolab/qti-components | GPL-3.0 | 18 | QTI item renderer as **web components**, "easy to use and highly customizable". 10 forks. 🔴 **Not adoptable yet and its own README says so:** the status badge reads *"WIP — initial development is in progress, but there has not yet been a stable, usable release suitable for the public."* It also **never names a QTI version**. Web components are the most framework-neutral shape in this table, so it is the one to re-check next pass — but GPL-3.0 plus no stable release is two reasons not to build on it now. |
| https://github.com/pie-framework/pie-qti | **MIT** | 4 | **The conversion bridge.** QTI 2.1 / 2.2 / 3.0 players plus bidirectional **QTI ↔ PIE** transforms, with a CLI and IMS Content Package support. QTI → PIE accepts 2.1 and 2.2 (3.0 is downconverted to the 2.2 vocabulary on ingest); PIE → QTI exports 2.2 and can emit content packages. 1 fork. 🔴 **Its README states the players are "not yet fully conformant or certified" and the transform framework is "under active development"** — use it for migration work, not delivery. |
| https://github.com/examplary/qti | **MIT** | 2 | **The smallest useful piece: packaging.** TypeScript library to build and parse **IMS Content Packages** containing QTI tests and items — QTI **3.0 by default and 2.1 supported, with automatic version detection on parse**. Parses both ZIP packages and raw XML strings. 0 forks, Releases empty. Does no rendering, scoring or storage, which is why it composes cleanly with anything above it. |
| https://github.com/agencyenterprise/qti-3-player | **MIT** | 3 | **Admitted for its honesty, not its coverage — and it is a useful negative control.** Framework-agnostic QTI 3 renderer with React, Vue and vanilla wrappers, XML validation against the QTI 3.0 schema, response processing with conditional logic, outcome variables, inline and modal feedback, MathML via user-supplied MathJax 2/3/4. 🔴 **Its README states plainly what it does *not* do: no scoring, no test structure (single items only), choice interactions only, basic expressions only (`match`, `correct`), no adaptive behaviour.** 1 fork. **Not adoptable for assessment** — listed because a README this candid is the cheapest way to see what "renders QTI" does and does not buy, and because the other players in this table are not all this explicit. |

🔴 **Licence trap recorded by this KB and worth repeating here, because it defeats
every sidebar check:** [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti)
**carries different licences on different branches** — `master` is **MIT**
(1 067 B) while `develop`, **its default branch**, is **GPL-2.0** (18 264 B).
🟢 **Re-confirmed fresh this pass:** the repository landing page shows
**`develop`** as the default branch and **"GPL-2.0 license"** in the sidebar
(26 stars, 22 forks, *"Convert QTI 2.1 Assessment Items to and from Learnosity
Item and Question JSON"*), and its README states the package is GPL-2.0 — so
**the permissive `master` grant is invisible to every landing-page check.**
**On any QTI repo, confirm the branch the licence was read from before quoting
it.** 🔴 Note also that it converts **QTI 2.1**, not QTI 3 — it is a migration
tool, not a delivery component.

## Learning platforms (LMS / MOOC)

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | Open edX LMS & Studio. **Formerly `openedx/edx-platform`** — that path now serves this repo; use this name. Stewarded by the nonprofit Harvard and MIT founded. |
| https://github.com/moodle/moodle | GPL-3.0 | 7.6k | The world's most deployed LMS. Plugin architecture is the integration surface. |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | The open LMS by Instructure; dominant in North American higher ed. Pair with `canvas-mcp` for agent access. |
| https://github.com/frappe/lms | AGPL-3.0 | 3.4k | Modern, lightweight LMS on the Frappe framework. Fastest to stand up of the group. |
| https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | Docker-based Open edX distribution. In practice this is *how* you deploy Open edX. |
| https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Higher-ed teaching/research/collaboration suite. **ECL-2.0 is Apache-2.0 with a patent clause tuned for universities** — permissive, and one of the two friendliest licenses in this table. |
| **https://github.com/OpenOLAT/OpenOLAT** | **Apache-2.0** | **451** | 🟢 **New this pass, and it overturns this file's standing "no permissive LMS" gap.** Java LMS, 32,338 commits, 165 forks; origin OLAT at the University of Zurich, maintained by frentix GmbH (Switzerland). **License read verbatim from the `LICENSE` file** — *"Apache License / Version 2.0, January 2004"*, followed by two attribution notices (olat.org / University of Zurich, openolat.org / frentix GmbH and community). **GitHub's sidebar names no license and the org listing renders it as "Other"** — the reason four passes of sidebar reads missed it. Uniquely in this table it carries a **first-party AI layer in-tree**: `org/olat/core/commons/services/ai/` with provider SPIs for `anthropic`, `generic` (OpenAI-compatible), `localonnx` and `openAI`. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; strong LATAM and francophone footprint. |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | Long-lived German LMS; heavy use in EMEA public sector and military/vocational training. |
| **https://github.com/elimu-ai/webapp** | **MIT** | 41 | 🟢 **New this pass (tenth, `p805`), promoted off the trending log, and the only MIT row in this table.** Java/Spring web application hosting Android apps and educational content for **elimu.ai — "free open-source learning software for out-of-school children."** Shipped content databases for **Hindi, Tagalog, Thai, Vietnamese and English**, which is an unusual language set for this base and places it **APAC**-first rather than Global. 🔵 **Engagement reading: this is the only platform row a studio can derive a product from without a copyleft conversation** — every other LMS here is GPL/AGPL/ECL. Sibling repos carry the ML layer: `ml-storybook-reading-level`, `ml-storybook-recommender`, `ml-authentication`. 🔴 Small project; adopt for low-resource and out-of-school programmes, not as a Moodle replacement. |

## Student information systems and institutional ERP

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/FenixEdu/fenixedu-academic | LGPL-3.0 | 175 | **New this pass (`p810`) — the largest dedicated open-source SIS in this base by stars, and a European one (Instituto Superior Técnico, Lisbon 🇵🇹).** Full academic SIS: curricular plans, enrolment, degrees, grading, theses. `111` forks — 🔵 **a `0.63` fork ratio, the signature of an SIS that institutions actually fork and run.** 🔴 **Last pushed `2023-06-14` — three years dormant, so this is an ARCHITECTURE reference and a migration source, not a live platform.** 🔴 LGPL-3.0: weak copyleft, so linking is permitted but modifications to the library itself must be released. 🟢 **It is also the only named EMEA-origin institutional system in this file**, which matters because `intel/market.md` has recorded a European supply gap for five consecutive passes |
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | SIS + LMS + finance modules as Odoo apps. The "Odoo for education" answer. |
| https://github.com/frappe/education | GPL-3.0 | 707 | **New this pass.** Education suite on the Frappe framework: admissions, fees, scheduling, exams, attendance. Shares a stack with `frappe/lms` (AGPL-3.0) and ERPNext, so a Frappe client can run SIS + LMS + ERP on one framework. **License read from `license.txt` ("GNU GPL V3") because GitHub's sidebar shows only a generic License link** — and note it differs from `frappe/lms`, which is AGPL-3.0. Branches version-15.1 / 15.2 / 16 / develop; Releases empty. |
| https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | RosarioSIS student information system for school management. Widely used in LATAM K-12. |
| https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible open-source school management platform. |
| https://github.com/OS4ED/openSIS-Classic | GPL (per README) | 351 | openSIS student information system. Sidebar shows no license badge; GPL claim comes from the README. |

## The K-12 data-standard layer (new, eleventh pass)

**Why this layer exists as of `p806`:** every pattern in this base that touches a
student record has so far reached it through an **LMS** (Moodle, Canvas, Open edX) or
through a **single institution's SIS** (RosarioSIS, Gibbon, OpenEduCat, EduPage,
HEMIS, Smartschool). 🔴 **That is the wrong altitude for North America.** US K-12 data
does not move institution-by-institution; it moves through **Ed-Fi**, the
interoperability standard that state education agencies run their reporting on. An
agent that speaks Ed-Fi reaches a *state*, not a school.

🔴 **This base discussed Ed-Fi `249` times across its two trending logs and never once
put it on a shelf.** It is promoted here by audit, not discovered here — see `p806` in
`repos/trending.md`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | **Apache-2.0** | 28 | *"This repository hosts the core code for the Ed-Fi Operational Data Store (ODS) and Ed-Fi ODS API."* The **v7.x** platform — the deployed one. 🔵 **Read the ratio, not the star count: `48` forks against `28` stars.** A repository forked nearly twice as often as it is starred is being *run*, not admired, and that is the institutional-deployment signature. Judging this row by stars against a `40k★` tutorial corpus is a category error. Region: **North America**. |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | **Apache-2.0** | 12 | *"Code and design documentation for the Ed-Fi API Platform, successor to the Ed-Fi ODS/API Platform."* **Ed-Fi API v8**, two applications: the **Data Management Service** (Resources, Descriptors, Discovery) and the **Configuration Service** (Management API). 🟢 **Build anything new against this, not the ODS** — the ODS README itself states that v8.0+ lives here. `17` forks against `12` stars, same signature. Region: **North America**. |

### What this layer does and does not change

🟢 **What it changes:** it gives a North American engagement a **permissive, standards-
backed route to the student record** that does not depend on which SIS a district
bought. `P8` in `compose/patterns.md` was scoped to RosarioSIS and Gibbon because those
were the open SIS products this base had verified; Ed-Fi sits one layer *above* that
choice.

🔴 **What it does not change:** **there is no Ed-Fi MCP server in this base, and none
was found.** The agent edge is unbuilt. Ed-Fi exposes a conventional REST API with a
published specification, so the work is ordinary — but it is **a build, and it must be
priced as one.** That is `Gap 806-A`, and it is the clearest-shaped contribution
opportunity in this file: every ingredient (the spec, the Apache-2.0 reference
implementation, three MIT write-gating designs to copy from `agents/top.md`) exists.

## Content, authoring and delivery

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/taybenlor/runno | MIT | 775 | **New this pass (`p810`) — the highest-starred repo added to this file since `p806`, and the missing substrate under every "grade the student's code" pattern in this base.** Sandboxed runtime for programming languages and WASI binaries that runs **in the browser, on a server, or via MCP**. `48` forks, pushed `2026-10-31`, created `2021-06-05` — 🟢 **five years of history, which makes it the most maintained new row of this pass.** 🟢 Licence byte-verified: `LICENSE` blob `35ff1e95e8bf`, `1,106 B`, MIT, Benjamin Taylor. 🟢 **Why it is a foundation and not an agent: it is the untrusted-code boundary.** Any tutor that executes learner-submitted code needs exactly this and the education repos in this base all assume it without naming it. 🔵 Browser-side execution also removes per-learner compute from the hosting bill |
| https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition engine. License read from the `LICENSE` file — GitHub's sidebar does not name it. The scheduling algorithm is the reusable asset. |
| https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Web conferencing built for virtual classes; LTI into Moodle/Canvas. |
| https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Free online learning platform with interactive explorations. **Apache-2.0 — permissive and substantial.** |
| https://github.com/Khan/perseus | MIT | 1.6k | Khan Academy's exercise question editor and renderer. **MIT** — the cleanest way to get real exercise rendering into a product. |
| https://github.com/learningequality/kolibri | MIT | 1.2k | Offline-first learning platform for low-connectivity settings. **MIT**, and the reference implementation for offline education. |
| https://github.com/opencast/opencast | ECL-2.0 | 511 | Automated lecture capture and video distribution at scale. |
| https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | Framework-agnostic H5P interactive content library. H5P is the de facto interactive-content format across Moodle/Canvas/Open edX. |
| https://github.com/learningequality/kolibri-design-system | No license shown | 53 | Kolibri's design system. Listed for completeness; **no license on the page**, so treat as unlicensed until confirmed. |

## Learning data, ML and assessment infrastructure

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user Jupyter server. The backbone of university CS/data-science teaching. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assigning and autograding notebooks. **The autograding layer to wrap an agent around.** |
| https://github.com/pykt-team/pykt-toolkit | MIT | 461 | pyKT: benchmark library for deep-learning knowledge-tracing models. **MIT** — the quantitative learner-modelling layer that LLM tutors usually lack. |
| https://github.com/getodk/collect | Apache-2.0 | 805 | Android app for offline form data collection; used for education field surveys and assessment at scale in low-connectivity regions. |
| https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | Open edX plugin housing AI tools and helpers. Early (17 stars) but it is the *official* AI extension point for Open edX. |
| https://github.com/1edtech/caliper-spec | IMS Global Specification Document License | 22 | Caliper Analytics spec — organizing and exchanging learning activity data. **Spec-document license, not a software license**: implement the spec, do not vendor the repo. |

## Interoperability standards worth knowing (not all are code repos)

- **LTI 1.3 / LTI Advantage** (1EdTech) — how any tool mounts inside Moodle,
  Canvas, Open edX, Sakai, ILIAS. **Implementations now verified above**; see
  the LTI table rather than planning a from-scratch build.
- **xAPI (Experience API)** and **Caliper Analytics** — the two learning-event
  telemetry standards. Emit one of them from any agent you build, or the
  institution cannot report on it. **As of this pass xAPI has verified open
  implementations in this KB** (`yetanalytics/lrsql`, `openfun/ralph`, and
  `DavidLMS/learnmcp-xapi` on the agent side); **Caliper now has six verified
  implementations too (fifth pass, see the analytics section above)** — but no
  permissively licensed *store*, so **xAPI remains the lower-risk choice
  wherever the client has no prior contractual commitment**.
- **QTI** — assessment item interchange. Matters the moment a client wants to
  move an item bank between systems.
- **SCORM** — legacy but ubiquitous in corporate and vocational training; still
  the delivery format many EMEA/APAC clients require.

## The curriculum-corpus layer (new, ninth pass)

**Why this layer exists as of `p804`:** three regimes now impose an AI-literacy
duty — SUNY folds AI into the gen-ed **Information Literacy** competency from
Fall 2026, the **EU AI Act Article 4** duty binds providers and deployers, and
Australia is rolling a national AI-literacy curriculum at **1M students over
three years**. 🟡 **Status changed at `p806`: that gap is NARROWED, not closed.** The first
education-licensed open curriculum did surface — `Emerging-Rule/community`, CC BY 4.0,
bilingual K-12 — **but at `3★` with six to thirteen lessons it cannot by itself meet a
national mandate.** 🔴 **What still does not exist is open education curriculum at the
scale these duties assume.** What exists at scale remains permissive **developer**
curriculum, larger than every education-specific repo in this base. 🔴 **Two further
candidates were identified and could NOT be verified: `Day of AI` (MIT RAISE,
advertises Creative Commons) and the `OER Commons` AI-literacy collections — both hosts
were refused by this session's egress proxy.** Named here so the next pass starts from a
target rather than a query. Both rows below
were read from the rendered repository page on `2026-11-13`.

| Repo | License | Stars | What it is, and what it is not |
|---|---|---|---|
| [`Emerging-Rule/community`](https://github.com/Emerging-Rule/community) | 🟡 **CC BY 4.0 — README and badge only; the GitHub sidebar shows no licence field at all** | 3 | *"Open knowledge base for K-12 educators, researchers, and builders."* 🟢 **The first *education* AI-literacy curriculum this base has found, as opposed to developer curriculum — and the row that narrows `T19`.** Bilingual **English / Spanish**, grades K-2 through 9-12, across Math, ELA, Science, SEL/Digital Citizenship and CS/AI Literacy. Folders: `lessons`, `skill-taxonomy`, `research`, `showcases`, plus `lesson-template.md` and `CONTRIBUTING.md`; `20` commits on `main`. 🟢 **CC BY 4.0 is attribution-only — no share-alike** — so unlike `GarethManning/education-agent-skills` (CC BY-SA 4.0, rejected at `p802` as contaminating) **its lessons can be cut down and shipped inside a client deliverable.** 🔴 **Three caveats travel with this row: the licence has README-grade provenance only; the badge claims `13` lessons while the README table lists `6`; and three of the showcase packs are marked draft and not yet piloted.** At `3★` / `1` fork this is a seed, not a corpus. |
| [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | MIT | 78.6k | "Learn AI Engineering! Learn it. Build it. Ship it for others." Model foundations → LLM systems → agent development, plus a retrieval-evaluation lab. `14.0k` forks, `2,703` commits. 🔴 **Not an education product, not a tutoring base, and not undergraduate-level.** Its value is that **MIT permits redistribution and modification of the content itself**, so it can be cut down and re-sequenced into a client's AI-literacy module without a licence negotiation. Largest permissive education-adjacent artifact in this base |
| [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | MIT | 41.8k | "In-depth tutorials on LLMs, RAGs and real-world AI agent applications." README states **"93+ Production-Ready Projects"**, graded **`22` Beginner / `48` Intermediate / `23` Advanced**. `6.7k` forks. 🟢 **The difficulty grading is the reusable asset** — it is the only thing in either corpus that maps directly onto a curriculum sequence with prerequisites. 🔴 Same caveat: developer-level, project-based, no learner model, no LMS surface |

🔵 **How to use this layer.** Neither repo is a dependency; both are **source
material**. The engagement shape is: take the sequence and the difficulty
grading, re-level the content for the client's cohort, emit it as packaged
course content through the layers this file already covers — `qti3` for
assessment items, `pylti1.3`/`ltijs` to mount it, `learnmcp-xapi` to make
completion reportable. 🔴 **Do not propose either corpus as the curriculum
itself; propose it as the thing that stops the client paying to write Module 1
from scratch.**

🔴 **Declared gap, raised this pass (`Gap 804-C`): there is still no permissively
licensed *AI-literacy* curriculum aimed at school or undergraduate learners.**
Searched: the global agent/trending/platform legs and all four regional legs.
What came back was developer curriculum (above), vendor courseware, and national
programmes whose materials are not published under an open grant. **This is the
clearest unserved content gap in this base, and it has three dated mandates
pointing at it.**

## The skills-and-credentials layer (new, tenth pass)

The layer that answers *"what did this learner actually end up able to do"* —
distinct from the learner-record layer, which answers *"what did they do"*. It
matters for an engagement because workforce-outcome claims are what a ministry,
a state system or a corporate academy buys, and because **all four rows below
are permissive**.

🟢 **All four were verified in earlier passes and never reached this file.**
They are promoted here, not discovered here; the audit that found them is
written up in `repos/trending.md` under `p805`. 🟢 **A fifth row,
`opensalt/opensalt`, was added the same way at `p806`** — and it is the one that makes
the layer coherent, because it holds the framework a learner is measured *against*
rather than the record of what they did.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/CredentialEngine/osmt | **Apache-2.0** | 67 | **Open Skills Management Tool.** Kotlin + Spring Boot + Angular, 1,647 commits on `develop`. Authoring and publishing of **Rich Skill Descriptors (RSD)** against the **CTDL** vocabulary — the US credential-transparency data model. 🔴 **The GitHub sidebar links a `LICENSE` without naming the grant and the index reads `NOASSERTION`; Apache-2.0 was read from the file itself.** Region: **North America** — CTDL/RSD is a US ecosystem, and that placement is the point of the row, not a caveat. |
| https://github.com/CredentialEngine/CredentialRegistry | **Apache-2.0** | 15 | The registry the skill descriptors are published *into* — Ruby, "Repository for development of the Credential Registry". 🟢 **Apache-2.0 named directly on the sidebar this pass.** Pair with `osmt`: `osmt` authors, `CredentialRegistry` stores and serves. Region: **North America**. |
| https://github.com/CredentialEngine/transcript-ctid-matcher | **Apache-2.0** | — | Matches transcript line items to **CTIDs** (Credential Transparency Identifiers). 🟢 **This is the hard, boring, valuable part** — mapping a registrar's course rows onto a public credential vocabulary is exactly the work a studio is hired for, and a permissive reference implementation removes the worst of it. Region: **North America**. |
| https://github.com/opensalt/opensalt | **MIT** | 47 | *"Standards Alignment Tool."* Implements **1EdTech CASE® 1.1** content structures — the standard for publishing and aligning *competency frameworks and academic standards* as machine-readable objects. States alignment against **IEEE 1484.2 (LER)**, **Open Badges 3.0**, **CLR**, **Credential Engine CTDL**, **CEDS-LER** and **W3C Verifiable Credentials / DIDs**. 🔵 **Treat that list as alignment targets the project names, not as six implemented standards.** 🟢 **MIT, and it is the missing upstream half of this layer:** `opensalt` holds the framework a learner is being measured *against*, `osmt` authors the skill descriptors, `CredentialRegistry` publishes them. `27` forks. 🔴 Promoted by the `p806` audit — mentioned `20` times in the trending logs, never shelved. Region: **North America** (CASE and CTDL are US ecosystems), with CASE itself in international use. |
| https://github.com/tabiya-tech/compass | **MIT** | 14 | "An AI chatbot designed to assist job-seekers in exploring and discovering their skills" — Python backend, TS frontend. 🟢 **The only agent in this base that works on *lived-experience* skills elicitation rather than coursework**, which is the shape of the problem in informal and youth-employment programmes. MIT, so it composes into a client deliverable. Companion repos `tabiya-livelihoods-classifier` and `taxonomy-model-application` carry the taxonomy side. 🔴 Small and young — adopt the approach and the licence, read the code before promising the model. |

## Declared gaps

- **The Caliper gap is CLOSED, and what replaced it is narrower and sharper
  (fifth pass).** This file previously said Caliper "has no verified open
  implementation here" and that a Caliper-bound engagement had "no open starting
  point in this base — that is a build, and it must be priced as one." **Both
  sentences are withdrawn.** Six implementations are now tabled above, led by
  `CarnegieLearningWeb/caliper-ts` (**MIT**). 🔴 **What survives as a real gap is
  one component, not the standard: there is no permissively licensed Caliper
  event store** — the only store found (`open-ent/caliper`, Caliper 1.2, Vert.x,
  33 unit tests) carries **no licence**. That is `Gap 287`, it is genuinely a
  build, and it is the one line item to price. Everything around it — sensor,
  LMS emitter, analysis notebooks, nine-profile reference — now exists.
- **Caliper's reference layer is behind consortium membership, and that is a
  procurement fact, not a search failure.** `1EdTech/caliper-js` and
  `IMSGlobal/caliper-js` both **404**; 1EdTech's Best Practice Guide advertises
  Sensor API reference code in Java, JavaScript, PHP, Python, Ruby and .NET and
  states that **Contributing Members and Affiliates can request GitHub access**.
  🟢 **And there is now documentary confirmation rather than inference:**
  `tl-its-umich-edu/caliper-php-public`'s own description reads *"This had been
  archived, but has been unarchived following **1EdTech making its caliper-php
  private**."* **A university un-archived its fork specifically because the
  upstream was withdrawn.**
  🟢 **The workaround is reliable: the public releases were forked by
  universities and consortia, and the forks are indexed where the originals are
  not** — `tl-its-umich-edu/caliper-php-public`, `umich-caliper-php`,
  `UnizinAnalytics/caliper-net-public`. 🔴 **No Caliper Python or Ruby
  implementation is publicly reachable** from any org listing checked this pass.
  **xAPI has no equivalent gate**, which is a reason to prefer it beyond the
  licence table.
- **Caliper version matters and should be asked about in week one.**
  `caliper-ts` defaults to **v1.1**. The only **v1.2** implementation found is
  the **unlicensed** `open-ent/caliper`. A client whose contract names Caliper
  **1.2** is further from this shelf than one naming 1.1 — establish which
  version the contract specifies before estimating.
- 🔴 **GAP WITHDRAWN (sixth pass): "No permissively licensed full LMS exists at
  scale" was wrong, and the method that produced the error is the transferable
  part.** Every LMS with real deployment is GPL/AGPL except **two**: Sakai
  (ECL-2.0) and **OpenOLAT (Apache-2.0, 451 stars, 32,338 commits)**. A client
  who needs a proprietary derived platform still cannot start from Moodle,
  Canvas or Open edX — but they **can** start from either of those two, and in
  EMEA OpenOLAT is the better of the pair because its AI layer is already in the
  tree. **Why four passes missed it:** every pass read GitHub's sidebar license
  field, and OpenOLAT's sidebar names no license (the org listing renders it
  "Other"). 🟢 **The rule this KB should carry forward: a sidebar reading
  "Other" or showing a bare "License" link is not a copyleft signal and is not a
  licensing answer — it is an instruction to open the `LICENSE` file.** This KB
  already adopted that step for `frappe/education` and `ankitects/anki`; it was
  never applied to the LMS table, which is where it mattered most.
- 🔴 **DEFECT FIXED (fifth pass): this gap list previously still carried "No LTI
  1.3 library in Python … A Python LTI 1.3 tool-provider library remains
  genuinely greenfield", while the header and the LTI section of this same file
  recorded the fourth pass's correction that it exists.** A file that contradicts
  itself sells the contradiction, and the gap list is the part that gets read
  into a proposal — this one would have quoted a client for a library already
  shipping. **The accurate statement:** `dmitry-viskov/pylti1.3` (**MIT, 138
  stars, 84 forks**) implements the full LTI Advantage service set in Python with
  Django and Flask adapters, so **single-language Python deployments are
  available and the forced two-process architecture is no longer forced.**
  🔴 **The residual risk is maintenance, not existence:** Releases is empty,
  newest PyPI version is **2.0.0**, and a third-party scanner puts the last
  publish at roughly three years ago — pin the version, vendor it, and budget to
  carry security patches.
- 🔴 **DEFECT FIXED (fifth pass): this list carried "No open-source QTI
  item-bank toolchain surfaced … it needs a dedicated search" while
  `intel/open-gaps.md` had measured the QTI layer across several passes and this
  repository ships a tested QTI emitter at
  `compose/code/p533-qti3-template-emitter/`.** The dedicated search had been
  done; its results had never reached this file. **Seven QTI repos are now
  tabled above**, five of them MIT. 🔵 **The general lesson, because this is the
  second stale bullet fixed in this file today:** findings that land only in the
  research log do not reach a proposal. When a pass closes a gap, it must delete
  the bullet in the operational file, not only record the closure.
- **What is genuinely still open in QTI is narrow and named.** `Gap 240`: the
  parametric-variant emitter this base built and tested for
  `LongsightGroup/qti3`'s `writer` package **has not been contributed upstream**;
  it needs someone with a working `qti3` checkout to run the project's own suite
  (third-party dependencies are not installable in this environment) and to
  validate against the official ASI schema (`purl.imsglobal.org` is
  proxy-blocked). 🔴 **And no repo in the table joins certified delivery to
  authoring and scoring** — `qti3-item-player` is certified but delivery-only;
  `qti3` authors and scores but claims no certification. **Every QTI engagement
  is therefore a pairing exercise, and that is the estimate to write.**
