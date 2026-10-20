---
industry: education
region: Global
updated: 2026-10-20
---

# Current trends — education

**Pass 328 · 2026-10-20 (first pass of this date). Three trends added, two corrected, and one of
this file's own conclusions retracted outright.** The pass set out to execute p327's prescribed
audit and found that p327's fix had been written into the wrong region of the right file — so the
declared-gap discount is refined a **fourth** time, and the new form is about the write's *target*
rather than the write. 🔴 **p327's conclusion that "the prescribed query set is exhausted for this
industry" is RETRACTED**: the same channel, with four extra words, returned four new agents, three
of them MIT. The two new sector trends are that **multilateral development finance has started
producing permissively licensed, production-shaped education software** — which qualifies p325's
reading of public funding — and that **copyleft has appeared at the top of the *agent* tier**,
which is the first real counter-instance to trend 4's permissive-agent / copyleft-platform split.


**Pass 327 · 2026-10-19 (thirteenth pass of this date). Two trends added, one corrected, and the
correction is to this file's own method.** The pass found no new sector trend on the prescribed
channels — **all eight queries returned already-held material** — and found instead that ten
region-placed artefacts had been discovered, licence-read, graded and addressed to this KB's shelf
files at p296 and **never written**. **The declared-gap discount, which p324 measured and p325 and
p326 each refined, is corrected a third time and the new form is the narrowest: before a gap is a
statement about the query or the filter, it is a statement about the write.** The second new trend
is a licensing one with a name: **the licence is becoming a row-level data field rather than a
repository attribute**, and this file's licence column cannot represent that.

**Pass 326 · 2026-10-19 (twelfth pass of this date). Three trends added, one corrected.** The
pass's finding is a 6.1 ★k curriculum dataset that eleven prior sweeps could not see, and it
touches this file three times: as a **method** trend (the sweeps were agent-shaped and the asset
is a data layer), as a **licensing** trend (ODbL's derivative-database / produced-work split makes
share-alike data commercially usable, and the boundary is architectural), and as a **provenance**
trend (the sector's best rights documentation came from a consumer app, not a ministry).
**Trend 12's headline is corrected a second time** — the commercially usable curriculum artefact
count goes from one to two, and the second one is multi-national.

**Pass 320 · 2026-10-19 (sixth pass of this date). One trend reading is reinforced and one is
newly separable.**

**Reinforced — governance has displaced experimentation as the thing buyers are actually procuring.**
Four independent 2026 sources converge on it this pass: institutions are building **policies, data
rules and oversight** rather than running pilots; the clearest realised gains are in **course
design, teacher productivity and administrative workflow** rather than in personalisation; buyers
increasingly want **evidence a product improves learning, persistence or job-relevant skills**; and
the move is **away from generic chatbots toward purpose-built education platforms with pedagogy
embedded in the system**. **This is the same conclusion `agents/top.md` reached from the opposite
direction in pass 319** — that the sector's reported quality metric (LLM-judged helpfulness) is
unsound and a real evaluation layer has only just appeared. **Demand-side scepticism and
supply-side measurement arrived in the same quarter, and that coincidence is the sellable
observation:** a studio that can *evidence* instructional effect is selling into a market that has
started asking for exactly that. Sources are vendor blogs and analyst notes — **the qualitative
convergence is credible, the statistics in them are not, and several specific figures were rejected
outright in pass 319's gap list.**

**Newly separable — "AI literacy mandate" and "AI guardrail mandate" are two different buying
motions, and this KB has been better at the second.** Pass 320 added **California AB 2876** (AI
literacy into K-12 curriculum) and **Utah H.B. 273** (AI into state CS standards) to
`intel/market.md` alongside Georgia, Mississippi and Alabama. **A literacy mandate buys content,
curriculum alignment and teacher training; a guardrail mandate buys governance tooling, audit logs
and consent handling.** They land with different budget holders on different timelines. The
permissively licensed assets for the literacy motion already sit in this KB and have not been
framed this way before — **`smashburger-dev/argmin`** (MIT + CC BY 4.0, German, 50 lessons, offline
via Pyodide) is a literacy-mandate asset, not a platform component, and the EU AI Act's **Article 4
staff-literacy duty** is the same motion in EMEA.

**Unchanged and worth repeating:** the sector's **copyleft lives entirely in the LMS/platform tier**
while everything you would put *under* a product is permissive — and pass 320 records the **first
exception in `repos/foundations.md`** (`adamzammit/LTIPlugin`, GPL-3.0), which is a constraint on
deployment rather than a bar on use.

**Pass 319 · 2026-10-19.** Twelve trends. Each names the evidence behind it and, where the evidence
is vendor marketing, says so.

**Pass 319 adds trend 12 — curriculum-standard data is the moat, and exactly one country has built
it** — and rewrites two others against first-hand evidence. **Trend 9's four-pass "no evaluation
layer" verdict is retired**: the layer exists, it is mostly MIT, and its convergent finding is that
the metric this sector reports is unsound, which forces a correction to pass 318's own reading of
`lumen`. **Trend 11 is extended twice**: star solicitation has been productised with a unit test
and a CI job, and the licences themselves — not just the descriptions of them — are drifting out
of open source at the popular end of the market.

## The declared-gap discount, fourth mechanism — the write's TARGET, not the write — NEW in p328

🔴 **Measured, with one command, and the command is the point.** p327 prescribed: *"re-grep every `PROMOTE-*` verdict in `evidence/` against the four shelf files."* Run literally — `grep -c <slug> agents/top.md` — **it passes: all ten p296 promotions are present.** Run against the **shelf region** — `sed -n '/^## The table/,/^## /p' agents/top.md | grep -c <slug>` — **it returns 0 for every one of them.** The rows were written into p327's own narrative commentary at lines 12–33, **above** the file's single canonical `## The table`.

🔵 **So the sequence now has four terms, and each one is narrower than the last.** p324/p325: a declared gap is a statement about the **query**. p326: about the **filter**. p327: about the **write**. **p328: about the write's *target*.** 🟢 **And the fourth term is the only one that is a defect in the KB's *structure* rather than in its *behaviour*, which is why it survived a pass that was explicitly looking for it.**

🔴 **The structural cause, stated so it generalises past this KB.** Two shelf files, two incompatible conventions. `repos/foundations.md` keeps **one `### The rows` ledger per pass** — so a row cut into a pass section *is* on the shelf, and that file passed this audit. `agents/top.md` keeps **a single canonical table plus running commentary above it** — so a row cut into a pass section is invisible to anyone reading the table. 🟡 **A per-file-name audit cannot distinguish these two cases, and the file with the weaker convention is the one that silently drops rows.** **The largest permissive education agent this KB has ever recorded — `OpenMAIC`, MIT, 41.1k ★ — was absent from the table for a full day after being found, graded and region-placed.**

🟢 **The rule, and it is one line of shell.** **An audit must name the shelf *region*, not the file.** A KB that mixes ledger-per-pass and single-canonical-table conventions must either normalise them or audit each by its own shape. **This pass cut nine rows into `## The table` and verified the cut with the region-scoped command above** — which is the first time in four passes that a prescribed fix was checked by the instrument that would have caught it failing.

## 🔴 RETRACTION — "the prescribed query set is exhausted for this industry" (asserted p327) is false, and the error class is this file's own

**p327 ran four global and four regional queries, got zero novelty, and concluded the query set was exhausted for education.** 🟢 **p328 ran the same eight channels. The agent channel returned four new repositories — `eai6/ai-tutor`, `Jellypod-Inc/school-skills`, `afri-bit/revibe`, `HugeCatLab/ChatTutor` — three MIT and one AGPL-3.0, none previously held.**

🔵 **The difference was four words.** `github trending education AI 2026` ranks SEO roundup blogs, which recycle the same twenty general-purpose agents every month. `github trending education AI 2026 **new repository tutor curriculum**` ranks **GitHub's own topic indexes** — `ai-tutor`, `education-ai`, `ai-in-education`, `study-assistant`, `programming-tutor` — **which are the actual supply surface.**

🔴 **Why this is worse than an ordinary wrong call: it is the exact error this file had already named, one level up.** p324 through p327 each established that a declared gap is a statement about the instrument rather than about the world. **p327 then declared a gap across an entire industry and attributed it to supply.** 🟢 **The generalised rule, which now has two independent confirmations: when a query channel returns nothing across several passes, change the query's *landing surface* before concluding anything about the market.** Roundup prose and index pages are different surfaces, and only one of them contains repositories that nobody has blogged about yet.

🟡 **The honest residue of p327's claim.** The *bare* `top open source AI agents {industry} {year} github MIT` query has now returned nothing education-specific for **five consecutive passes**, and that is a real finding about *that query* — it ranks general-purpose agent roundups, permanently. **It should be retired from the prescribed set and replaced with a topic-index sweep.**

## Multilateral development finance is now producing permissively licensed, production-shaped education software — NEW in p328

🟢 **The instance, with the grant read first-hand:** `eai6/ai-tutor` — **MIT**, `main/LICENSE` and `master/LICENSE` both 1,090 B, *"Copyright (c) 2026 **World Bank Group** and contributors"*, README contributors naming the **World Bank Education Team**. Django 6.0.2, seven apps all resolving as real files, `config/settings.py` 17,064 B.

🔵 **Why it is a trend rather than an anecdote: it is the first artefact in this KB where the *funder* is a development bank and the *output* is permissive and complete at once.** This sector's publicly funded code has a long record in this file of being **permissive at the edges and unlicensed or restricted at the core** (trend: p322, extended p323). **This one is MIT all the way through, and the core is the part a client needs most** — the consent and audit models, the skill graph, the mastery gating.

🟡 **It qualifies p325's trend rather than overturning it.** p325 concluded: *public funding does not predict a licence posture — the operator's engineering maturity does.* **That still holds, and this instance is consistent with it:** the repository shows dated engineering decisions left in the source (*"chromadb removed 2026-05-24 — vectors now in Postgres via pgvector"*), a CI/CD workflow, a fork-and-deploy walkthrough, and a seven-app separation of concerns. 🟢 **The refinement is that development-bank-funded work has started clearing that maturity bar, which it previously did not — and when it does, the licence has been permissive.** **Two more instances would make it a reliable sourcing channel; one makes it a channel worth sweeping, which no pass of this KB has ever done.**

🔴 **The caveat that must travel with the trend.** The institutional attribution is **self-declared**: the repository sits in a **personal namespace**, and `github.com`, `api.github.com` and `worldbank.org` were all unreachable this pass, so **the affiliation is uncorroborated**. 🔵 **And the announced national programme in the same country appears to run on a different, proprietary stack** — a World Bank 2026 Annual Meetings transcript has a Seychelles minister describing a **Grok**-based national tutor. **The gap between the open artefact and the procured stack is this trend's most commercially interesting feature, and this pass does not resolve it.**

## Copyleft has reached the agent tier — trend 4's permissive-agent split has its first real counter-instance — NEW in p328

🔴 **`HugeCatLab/ChatTutor` is AGPL-3.0**, read first-hand: `main/LICENSE`, **34,522 B**, *GNU Affero General Public License Version 3*. A third-party roundup puts it near **1.2k ★** (carried; unverifiable this pass). It is a **visual interactive tutor** — an agent-tier artefact, not a platform — on a pnpm monorepo with Vitest.

🔵 **Trend 4 of this file has held for ten passes: agents are permissive, platforms are copyleft.** The split was never a coincidence — platforms inherit the installed base's licence (Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0), while agents and skills are new code written by people who want adoption. 🔴 **An AGPL tutor near the top of the attention distribution breaks the second half of that explanation**, and the practical consequence is sharper than the taxonomy: **AGPL §13 reaches the users of a hosted service, so an AGPL *tutor* is a licence event for exactly the deployment shape this sector uses — a web app students log into.**

🟡 **Two passes of this is a trend; one is a warning.** Recorded now so the next pass checks whether it is the start of a pattern or an outlier. 🟢 **What is already actionable: the agent tier can no longer be treated as permissive-by-default during sourcing.** Every agent row in `agents/top.md` carries a first-hand grant read for this reason, and **this is the first time that discipline has caught something at the top of the distribution rather than in the tail.**

## 🟡 Correction to trend 11 — the unreliable-metadata finding now extends to secondary sources, and it skews permissive

**Trend 11 has held since p318: this sector's published metadata is unreliable in both directions — stars solicited, licences misdeclared in README badges.** p322 logged the README-versus-LICENSE hazard **four times inside one organisation**.

🔴 **p328 extends it one layer out, to the third-party comparison blogs a studio lead actually reads.** Three platform licence claims from 2026 comparison articles, probed against the repositories' own grant files:

| platform | blog claim | **first-hand p328** |
|---|---|---|
| `frappe/lms` | *"MIT licence with self-hosted data ownership"* | 🔴 **AGPL-3.0** — `license.txt`, 33,893 B, on all three branches |
| `foradian/fedena` | *Apache 2.0* | 🔴 **No licence file at all** — six filenames × three branches, all 404 |
| `OpenOLAT/OpenOlat` | *Apache 2.0* | 🟢 **Apache-2.0 confirmed** — `master/LICENSE`, 10,982 B |

🔵 **Both errors ran in the permissive direction, which is the dangerous one.** A copyleft platform mislabelled MIT is how an AGPL obligation enters a deliverable without anyone deciding to accept it. 🟢 **The probe that settles it is one HTTP request against the repository's own grant file. This pass ran eighteen of them, and the two falsifications cost about ninety seconds.**

## 🔴 The verification channel narrowed this pass, and which layer it narrowed on is itself the finding — NEW in p328

| host | p327 | p328 |
|---|---|---|
| `raw.githubusercontent.com` | 200 | 🟢 **200** |
| `github.com` (rendered repo page) | **200 — p327 read licences off the sidebar** | 🔴 **403** |
| `api.github.com` | blocked | 🔴 **403** |
| `arxiv.org`, `huggingface.co`, `unesco.org`, `codeberg.org` | 403 | 🔴 **000 — no connect** |

🔵 **The channel that died is the *attention* channel; the channel that held is the *grant* channel.** Stars, forks, commit counts, topics and descriptions were unobtainable this pass; licences, byte counts, file paths, code and README text were all first-hand.

🟢 **And by this file's own trend 11, that is the better of the two losses by a wide margin.** Star counts in this sector are **solicited** — p319 recorded a repository shipping star solicitation with a unit test and a CI job — and README licence badges are **wrong often enough to have been logged four times inside one organisation.** 🔵 **So a pass that can read grants but not stars can still do the rights analysis a client pays for, and cannot do the popularity analysis that was never reliable.** 🟡 **The operational rule: a KB in this sector should state claims in grant-verifiable terms wherever it has the choice, because the grant channel is the one that survives environment changes.** Every star figure written this pass is marked `carried` with its source pass, or **`n/v`** — never presented as verified today.

## The declared-gap discount, third mechanism — the WRITE, not the query or the filter — NEW in p327

🔴 **Measured, with one command.** `evidence/p296-promotion-gap.2026-10-18-p296.tsv` carries ten
adjudicated verdicts — four `PROMOTE-to-agents-top`, four `PROMOTE-to-foundations`, one
`PROMOTE-to-foundations-with-grade-note`, one `PROMOTE-reference-only`. **Grepping each slug
against `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` and
`compose/patterns.md` returns 0 of 10 present.** Thirty passes elapsed, twelve of them on
2026-10-19 alone.

🔵 **Why this supersedes rather than joins the previous two readings.** p325 found six FUN-MOOC
repositories that were "a promotion, not a discovery" and read it as a carry-forward lapse. p326
found a 6.1 ★k dataset with no description, no topics and no detected language, and read it as a
**query-shape** defect — agent-shaped queries cannot see a data layer. **Both explanations are
about *finding*. Neither applies to a row that was found, graded, region-placed and addressed.**
`anthropics/k12-teacher-skills` was marked `PROMOTE-to-agents-top` with region `North America` and
the note "Claude for Teachers, co-developed with Learning Commons." **No query needed reshaping.
No index needed fixing. The write did not happen.**

🟢 **The two failures were wearing the same clothes, and separating them is the trend.** Of the
three Learning Commons repositories promoted this pass, **`agent-skills` has no description and no
topics — p326's signature exactly — while `knowledge-graph` carries eight topics including
`education`, `edtech` and `ai-in-education`, and `evaluators` carries nine including `education`
and `evaluation`.** The latter two were perfectly indexed, had been on this KB's trending channel
since **p119–p120**, had their licences read **byte-for-byte** into evidence files, and still never
reached a shelf file. 🔵 **An index hole and an unexecuted write produce the same observable — an
absent row — and only one of them is fixed by changing how you search.**

🟡 **The generalisation, and it is uncomfortable because it is about process rather than supply.**
A knowledge base that discovers, grades and addresses an asset and then does not cut the row has a
**high discovery rate and a zero delivery rate on that asset** — and delivery is the only number an
engagement can spend. 🟢 **The audit is cheap, deterministic and repeatable: re-grep every
`PROMOTE-*` verdict in `evidence/` against the four shelf files, and run it *before* the sweep
rather than after.** This pass promoted all ten, re-reading every licence first-hand rather than
carrying p296's reads — **nine of the ten are MIT or Apache-2.0, so the backlog was never blocked
on licensing.**

🔵 **One corollary for the sweep itself.** Four consecutive passes of eight prescribed queries —
four global, four regional — have added nothing to this KB. **The queries are not broken; they
return correct, relevant, already-held material. They are exhausted for this industry.** The two
channels that returned anything this pass were **an audit of this KB's own evidence directory**
(ten artefacts) and **reading the GitHub organisation behind a repository already held** (four
artefacts, one HTTP request). **Neither is a query.**

## The licence is becoming a row-level data field, not a repository attribute — NEW in p327

🔴 **Three artefacts read first-hand this pass cannot be represented by this KB's licence column,
and the reason is structural rather than sloppy.** `learning-commons-org/knowledge-graph` publishes
**MIT code and data licensed per dataset *and in some cases per download***, across three access
types — **Open** (typically CC BY 4.0, some CC0), **Open + Gated**, **Gated**. Its `CHANGELOG.md`
for **v1.10.0** records that for ELA Learning Components, *"License and attribution statement
values have been updated for each individual row."* 🔵 **The licence is a field in the data, not a
property of the repository — and GitHub agrees, because its sidebar names no licence at all and
its Languages panel is empty.**

🟢 **The clause that makes this a procurement issue rather than a curiosity, quoted from
`LICENSE.md`:** compiling datasets into your own build means you *"take on the licensing and
attribution obligations of every dataset and download you include,"* and the distributor's role
*"doesn't consolidate those into a single license for your build."* **Attribution travels to each
original source, not to the distributor.** 🔴 **So the obvious move — export the full graph, call
the result CC BY 4.0 — is precisely the one the licence forbids.**

🔵 **This is the third distinct shape of the same trend and the shapes are converging.** p322 and
p323 recorded *permissive at the edges, restricted at the core.* p326 recorded ODbL's
**derivative-database / produced-work** split, where share-alike binds the database and not the
product. **p327 records the finest grain yet: a four-way split inside a single 1,615-byte licence
file** — `learning-commons-org/evaluators` licenses **code MIT, prompts and settings CC BY 4.0, and
the Annotated CLEAR and PERSUADE 2.0 corpora CC BY-NC-SA 4.0.** 🟢 **Read together, these three
passes describe a sector that has learned to license *layers* rather than repositories — and the
layer boundary is almost always drawn between the machinery and the expert-authored content.**

🟡 **The operating rule this yields, and it is directly billable.** In every one of these artefacts
the **permissive part is the part that runs** and the **restricted part is the part that was
expensive to author** — the curriculum text, the publisher's materials, the expert annotations.
🟢 **Which means the reusable asset is the architecture and the harness, and the client-specific
work is re-authoring the restricted layer against their own content.** That is the correct shape
for a studio engagement: take the MIT evaluator, re-annotate on client data, and ship. 🔴 **It is
also why "is this repo MIT?" has stopped being a sufficient licence question, and this KB should
stop asking it as if it were.**

## 🟡 Correction to trend 12 — the commercially usable curriculum-artefact count goes from two to three, and the third is American

**p326 corrected this trend's headline from one to two: `bncc-dev` (Brazil, CC BY 4.0) and
`withmarbleapp/os-taxonomy` (ODbL + CC BY-SA, multi-national).** 🟢 **Add
`learning-commons-org/knowledge-graph`: US academic standards at state granularity with state↔CCSS
crosswalks, Open-tier datasets typically CC BY 4.0, v1.15.0 released 2026-10-14, and a published
erratum stream.** 🔵 **The moat argument this trend has made for eight passes is intact — curriculum
data is the durable asset — but the scarcity claim is now wrong in three jurisdictions rather than
one.** 🔴 **What remains scarce, and the next pass should test it rather than assume it, is
**EMEA**: this KB still has no commercially usable national-curriculum graph for any European
state, and the Learning Commons data tier is CCSS-shaped and does not port.**

## The data layer under the agents has never been swept, and it is where the sector's largest open assets are — NEW in p326

🔴 **This is a method trend and it is the third consecutive refinement of the same defect, so the
sequence is the finding.** p324: *a declared gap is a statement about the query.* p325: *a gap
declared behind a star or recency filter is a statement about the filter.* **p326: a gap declared
by an agent-shaped query is a statement about the shape of the query — and every education query
this KB has ever run has been agent-shaped.**

**The evidence is a single repository.** `withmarbleapp/os-taxonomy` — **6.1 ★k, 998 forks, public
since 2026-07-08** — is larger by stars than every artefact in `agents/top.md` except `DeepTutor`,
and **eleven passes of sweeps across three instruments never returned it.** The reason is
mechanical rather than mysterious: the repository has **no GitHub description, no topics and no
detected language.** GitHub renders *"No description, website, or topics provided"* and an empty
Languages panel. **It is a directory of JSON.** Keyword sweeps on `agent`, `tutor`, `MCP`,
`skill` and `assistant` cannot reach it; topic sweeps cannot reach it; a language filter removes
it. **At 6.1 ★k.**

🟢 **Why this is a trend about the sector and not only about this KB's hygiene.** The assets that
survive a model generation in education are **not** the agents. An MCP tutor written this quarter
is replaced next quarter. **A verified prerequisite graph over a national curriculum is replaced
when the curriculum changes — which is a decade.** This KB has been arguing that in trend 12 since
p319 while searching exclusively on the axis that *cannot see it*. 🔵 **The practical rule for
every industry KB, not just this one: sweep the agent axis and the data axis separately, with
different vocabulary — `dataset`, `taxonomy`, `graph`, `standards`, `corpus`, `benchmark`, `JSON`
— and never let a language or topic filter near the second.**

🟡 **And the counterpart risk, which this pass can state because it measured both channels in one
run.** Novelty on the agent channel this pass was **0 of 7**. Novelty on the data channel was
**1 of 1, first query**. **Neither number is stable enough to forecast from** — one pass is one
pass — but the asymmetry is large enough to change where the next pass spends its budget.

## The share-alike dataset is a commercial asset, and the boundary is architectural — NEW in p326

**This KB has treated share-alike as a near-synonym for unusable, and on code that is roughly
right.** `cn-math-taxonomy` is CC BY-NC and cannot enter a deliverable at all; K12-KGraph's data
is CC BY-NC-SA; the LMS tier's GPL and AGPL drive the integration boundary that pattern P8 exists
to manage. 🟢 **ODbL is a different instrument and the difference is worth money.**

**ODbL distinguishes a *derivative database* from a *produced work*.** Modify the dataset and your
modified dataset must be published under ODbL. **Use the dataset inside a product, a model or an
application and the product is yours.** So a commercial tutor built on an ODbL curriculum graph
**does not open-source itself** — it owes back only improvements to the graph.

🔵 **Which makes the obligation an architecture question rather than a legal one, and
`tbh-23/Homestead` (MIT, 15 ★) has already answered it.** It **fetches the taxonomy from upstream
at runtime, caches it outside the repository, instructs that it must never be committed, and
notifies when upstream topics are added or removed.** The ODbL database is therefore never inside
the MIT product — **the licence boundary is enforced by the build, not by a policy document.**
Client-specific extensions belong in an overlay keyed by topic ID, not in edits to the graph.
That is **P13**.

🟢 **The commercial reading for a public-sector buyer inverts the usual objection.** Share-alike on
a client's jurisdiction extension means **the client's curriculum work becomes a public asset with
their name on it** — which is what a ministry wants and what a procurement officer can defend.
**Lead with it in public-sector bids; design around it in private edtech ones.**

## Public-sector provenance is not the predictor of data quality either — NEW in p326

**p325 retired the idea that public funding predicts a licence posture, and found the operator's
engineering maturity predicted it instead. This pass extends the same correction to data
quality.** The best-documented rights provenance this KB has seen in the sector was published by
**a venture-backed consumer app**, not by a ministry or a university.

`os-taxonomy`'s `PROVENANCE.md` does per-source licence analysis across seven curricula, ships
**codes-only** for the four it cannot redistribute, and enforces that mechanically: the export
**omits any passage matching eight or more consecutive words of a codes-only framework's stored
text**, case- and punctuation-insensitive, **marks every omission inline with the curriculum code
and logs it by JSON path** in `publicationNotes.omittedCurriculumText`. It then states, unasked,
that the pass *"is not comprehensive rights clearance"* and that shorter excerpts may remain.

🟢 **Two more things this KB has asked of every curriculum artefact and received from none until
now:** **SHA-256 per shipped file in a manifest** — `topics.json` verified against its published
hash this pass — and **a dataset that enumerates its own holes**, naming the **540 of 1,591
topics** with no teaching research and breaking the absence down by subject rather than leaving it
to be discovered. 🔵 **Trend 11 has recorded unreliable metadata in both directions for eight
passes. This is its first clean positive instance, and the discipline — codes-only export, logged
omissions, per-file checksums, declared coverage — is a checklist to put to every other data
supplier in this sector.**

🔴 **Keep the limits in the same breath, because the same README states them.** The teaching
research is **agent-authored**, its sources **were not re-verified for this release**, and its
activities are **"research-informed proposals, not empirically validated interventions."** Good
provenance on rights is not evidence of instructional effect, and this file should not let the
first be read as the second.

## Public funding does not predict a licence posture — the operator's engineering maturity does — NEW in p325

**p322 found, inside one publicly funded German organisation (`openeduhub`), licences dividing by
architectural layer: permissive shells, GPL-3.0 analysers, and an unlicensed inference core — the
grant getting weaker the closer you got to the work.** p323 found the same sentence by artefact type
in China (MIT code, NonCommercial curriculum data). **Both readings invited an inference that this
pass can now retire: that public funding produces a defensive licence posture at the valuable
layer.**

🟢 **It does not.** p325 measured the complete repository stack of **France Université Numérique /
GIP FUN-MOOC — the operator of France's national public MOOC platform — and found MIT on every
layer there is**, each licence file read first-hand:

| layer | repository | licence |
|---|---|---|
| portal CMS | `openfun/richie` (316 ★) | **MIT** |
| headless education ERP | `openfun/joanie` (30 ★) | **MIT** |
| LTI content management | `openfun/marsha` (150 ★) | **MIT** |
| xAPI Learning Record Store | `openfun/ralph` (51 ★) | **MIT** |
| analytics visualisation | `openfun/warren` (17 ★) | **MIT** |
| dashboards-as-code | `openfun/potsie` (11 ★) | **MIT** |
| LTI tool-provider plumbing | `openfun/django-lti-toolbox` (14 ★) | **MIT** |
| course forum | `openfun/ashley` (12 ★) | **MIT** |
| Open edX packaging | `openfun/openedx-docker` (142 ★) | 🟡 **AGPL-3.0** |

🔵 **The one copyleft row is the one that proves the rule: `openedx-docker` is AGPL-3.0 because
Open edX is AGPL-3.0.** The copyleft is **inherited from the platform it packages, not chosen by the
operator** — which is trend 4's permissive-agent / copyleft-platform split appearing *inside a
single organisation's repository list*, and the cleanest instance of it this KB has recorded.

**So two publicly funded European education operators, same decade, same kind of mandate, opposite
licence hygiene. What actually distinguishes them is visible before you sign anything:**

| signal | FUN-MOOC | openeduhub (ITS tier) |
|---|---|---|
| published engineering practice | 🟢 a `handbook` repository, and a `handbook.openfun.fr` its READMEs cite | 🔴 none found |
| distribution | 🟢 PyPI packages, Docker Hub images, **Helm charts**, `make bootstrap` | 🔴 nix-run scripts, no HTTP surface on several repos |
| licence consistency | 🟢 same grant on every layer; `LICENSE.md` vs `LICENSE` is the only inconsistency | 🔴 four READMEs claim grants the repository does not carry |
| conventions | 🟢 uniform | 🔴 **`README.org` in one tier, `README.md` in another** |

🟢 **The instruction for due diligence, and it is cheap to run:** when a public buyer offers an
existing codebase as the base of an engagement, **read the organisation's engineering artefacts, not
its funding source.** Helm charts, a published handbook and a consistent licence across layers
predict a clean grant; inconsistent README filenames predict an unlicensed core. **This is a
twenty-minute check that changes what you can promise.**

🔴 **The caveat that keeps this from being a procurement free pass.** Two of FUN's seven permissive
segments are not load-bearing: `warren` **declares itself** *"a Proof Of Concept not suitable for
production yet"*, and `django-lti-toolbox` has **no release and no push since `2024-11-14`.**
**Uniform licensing is not uniform maintenance**, and the maintenance question has to be asked
per repository even when the licence question has been answered once.

## The declared-gap discount, second mechanism — the FILTER, not only the query — NEW in p325

**p324 recorded, on four instances, that a declared gap is a statement about the query rather than
about the world. p325 adds the narrower and more dangerous mechanism, and caught it on itself.**

This pass searched **`special education IEP AI assistant pushed:>2026-01-01 stars:>3` → 0 results**,
then changed the terms completely — **`IEP individualized education program generator LLM` → 0
results** — and was one step from declaring a special-education supply gap on *two* empty queries.

🔴 **This KB already holds the answer, and has held it since p288: `iblai/k-12-agents`, MIT, shipping
a `special-education-agent` grounded in IDEA 2004, the thirteen disability categories and §504** —
recorded at p288 as the correction of an earlier *"zero permissive for special education"* claim —
plus `eakarsu/ai-special-education-iep-compliance` in the grading/compliance sweep.

🔵 **The terms were never the problem. `stars:>3` and `pushed:>2026-01-01` deleted the answer.**

🟢 **And the bias is systematic, not random, which is what makes it worth a trend entry.** The tiers
where a filtered sweep fails are **predictably** the high-stakes ones:

- **special education, IEP compliance, assessment integrity, rostering, safeguarding** — published
  by an institution, a district contractor or a single practitioner, typically **at 0–5 stars**;
- **institutional infrastructure** — p317 already recorded that stars run *too low* on it;
- **finished work** — a thesis system, a ministry pilot or a completed grant deliverable stops being
  pushed, so a recency filter reads *completion* as *abandonment*. **`JustinoLM/STI-matematicas`,
  which carries the only measured classroom outcome in this KB, is tagged `v1.0-tesis` and
  deliberately finished** — `pushed:>2026-01-01` happens to keep it, a tighter window would not.

**Operating rules, for every future pass:**
1. **Never declare a gap from a filtered query.** Re-run it with **no `stars:`, no `pushed:`** before
   the word "gap" is written.
2. **Check the base first.** This pass's two empty searches cost less than the retraction would
   have; `grep` over this KB is the cheapest instrument available and it is not being used first.
3. **A star filter screens for popularity and therefore screens against regulated subject matter.**
   In this sector that is an inverse correlation with commercial importance.

## Sovereign and academic inference shows up in publicly funded edtech code — p321

**The trend, stated from code rather than from a vendor claim.** Both AI tools in Germany's
publicly funded OER organisation name a **non-US-hyperscaler inference path as a first-class
option**: `openeduhub/tutor-chatbot` offers **OpenAI or GWDG** (Gesellschaft für wissenschaftliche
Datenverarbeitung Göttingen — German academic compute), and `openeduhub/ki-prompt-benchmark` lets
the operator route through **AcademicCloud** and compare it head-to-head with OpenAI on output
quality, generation time and token cost. Both are **Apache-2.0** and both were read first-hand at
p321.

**Why this is a trend and not a configuration detail.** The benchmark exists to answer "which
provider, at what quality and what token cost" **as an operator decision, repeatedly** — judge-scored
on five criteria with a stated winner and rationale. That is procurement tooling. A public buyer
that has to defend where inference happens now has a reference implementation that treats the
provider as a swappable, measured variable instead of a fixed dependency.

**What it changes in a bid.** This KB has recorded the EU AI Act obligations and the Article 50
transparency duty that has applied since `2026-08-02`. Those create the compliance question;
`openeduhub` is the first artefact in this KB that answers the adjacent *infrastructure* question in
public code. **For a European public-sector engagement, assume the provider must be pluggable and
the comparison auditable, and say so unprompted** — the buyer's own sector has already published
the pattern, so proposing a single hard-wired US API now reads as behind the reference
implementation rather than as a default.

**Limits, so this is not over-read.** Ten commits and three commits respectively: these are
prototypes, and one organisation in one member state is one data point, not a European consensus.
The claim here is narrow — **that sovereign inference has moved from policy language into
publicly funded, permissively licensed code** — and it rests on two repositories, both named.

## The evaluation layer now has an operator-grade instance, not only academic ones — p321

Pass 319 opened this KB's evaluation shelf with peer-reviewed artefacts: `MathTutorBench`,
`AITutor-EvalKit`, and two pre-registered LLM-judge audits. **All four are research outputs.**
`openeduhub/ki-prompt-benchmark` (Apache-2.0, 3 commits, read first-hand at p321) is the first one
published by **an organisation that actually runs a service** — it benchmarks the prompts live in
its own platform's `mds.xml` v10.0, accumulates judge feedback across runs into a regenerated prompt
per field, and exports the winning set back into the platform's own schema.

**The shape worth copying is the loop, not the tool.** Research benchmarks score a model against a
frozen dataset. This scores **your current production prompt against a candidate replacement, on
your own content, and then writes the improvement back into the system of record.** For any
engagement where an agent generates metadata, feedback or assessment text, that closed loop is the
thing a client can be shown and will understand — and the KB's own caution applies: it is three
commits, so take the design and expect to rebuild it.

## The public sector tried the chatbot, archived it, and built a metadata pipeline instead — NEW in p322

**This is the clearest evidence in this KB for where institutional AI money actually goes, and it
comes from a complete organisational history rather than a survey.** `openeduhub`, the GitHub
account behind Germany's publicly funded OER portal WirLernenOnline, was enumerated in full at p322
— all 67 repositories, sixteen read first-hand. The sequence is legible in the dates:

- **August 2023:** `wlo-chat-gpt-block`, a WordPress ChatGPT block. **Archived.**
- **2024–2026:** a twelve-service metadata pipeline, still being pushed — LLM extraction into
  eleven schemas, a human-review canvas with per-field confidence badges, MinHash deduplication,
  Flesch/Wiener readability, Lighthouse accessibility and licence lookup, a Pyro Bayesian metadata
  predictor, a Keras discipline classifier, bulk prompt running, a factual-accuracy judge and a
  unified API gateway.
- **The conversational artefact that survives is a 10-commit prototype** (`tutor-chatbot`, p321),
  against **60 commits** on the metadata review UI and **1,852 commits** across the inference core.

**The reading: for an institutional buyer, the first AI product that pays is cataloguing, not
tutoring.** Extraction, enrichment, deduplication, readability and accessibility scoring are
measurable, low-risk, do not touch a child, and attach to a backlog the institution already knows
it has. This converges from the opposite direction with trend 1 (institutional deployment is not
landing) and the p320 reading that governance has displaced experimentation — but it is stronger,
because it is not what a buyer *said* in a survey, it is what a public operator **spent three years
of engineering on after shutting down its chatbot.** For a studio pitch: lead with the catalogue,
not the tutor, and the tutor becomes a later phase with cleaner data under it.

**The caveat that keeps this honest.** This is one operator in one country. The pattern is
suggestive, not measured across jurisdictions, and this KB has no equivalent organisational history
for a North American, APAC or LATAM public operator — **Ed-Fi (p316) is the nearest comparable and
it is a data-standard body, which is itself consistent with the reading.** Treat it as a strong
hypothesis with one deep instance, and look for a second instance before putting a number on it.

## Permissive at the edges, unlicensed at the core — the licence pattern inside publicly funded AI — NEW in p322

Trend 4 records a permissive-agent / copyleft-platform split across the sector. **Pass 322 found a
third shape inside a single organisation, and it is the one that actually blocks delivery.** In
`openeduhub` the licence tracks the architectural layer:

| Layer | Commits | Licence |
|---|---|---|
| Interaction shells (review UI, browser plugin, path editor, tutor, judge, dedup, registry) | 119 | Apache-2.0, or claimed as such |
| Analysers (accessibility/licence lookup, readability, discipline classifier) | 790 | 🟡 GPL-3.0 |
| **Inference core** (gateway, Bayesian predictor, text extraction, bulk prompt runner, QA generation, harvester) | **1,852** | 🔴 **none at all** |
| Generated API client | 519 | Apache-2.0 |

**The permissive surface contains none of the organisation's machine learning.** Pass 321 saw one
unlicensed repository and read it as an oversight; across sixteen reads it is the rule. The
mechanism is mundane and therefore likely general: licence files get added when a repository is
published *as a thing other people should use*, and research and plumbing code is never published
that way, even when it is where the effort went.

**Two consequences for how this KB should be read.** First, **"the org is permissive" is not a
property an org has** — ask which layer. Second, and this is the measured hazard: in this
organisation **four repositories state a licence the repository does not carry** — two say MIT while
shipping an Apache-2.0 `LICENSE`, and two claim a licence with no file in the root at all. That is a
copied README template, and it means **a licence column built from READMEs would have been wrong
four times out of sixteen in a single org.** It is the second independent confirmation of trend 11
(the sector's published metadata is unreliable in both directions), now reproduced inside one
account rather than across vendors.

## Permissive at the edges, restricted at the core — second instance, and the core moved — NEW in p323

p322 recorded a licence pattern inside Germany's publicly funded OER organisation: **permissive
shells, GPL-3.0 analysers, and an unlicensed inference core.** It named the shape *licence by
architectural layer*. **Pass 323 found the same sentence in a different structure, and the pairing
is now a rule worth carrying into due diligence.**

| | p322 — `openeduhub` (Germany, public sector) | p323 — `K12-KGraph` (China, academic) |
|---|---|---|
| Divides by | **Architectural layer**, across 16 repositories | **Artefact type**, inside one repository |
| Permissive part | UI shells, REST wrappers, browser plugin, judge | **The whole pipeline — MIT** |
| Restricted part | Analysers **GPL-3.0**; inference core **no licence at all** | **The curriculum, benchmark and training data — CC BY-NC-SA 4.0** |
| What a sidebar badge tells you | Apache-2.0, four times wrongly | *"MIT licenses found"* — and the data is not MIT |

**The rule: in educational AI, the permissive licence covers the part that was cheap to build.** The
expensive part — the verified curriculum, the trained inference, the annotated corpus — is where the
restriction sits, whether that restriction is NonCommercial, copyleft, or simply the absence of any
grant. **This is not cynicism about the authors**; both projects are public goods and both are
candid in their README text. It is a statement about where to look. **A licence check that reads the
sidebar badge and stops will clear both of these projects for client work, and both would be
wrong.**

**What to do with it tomorrow:** on any educational-AI dependency, resolve the licence **separately
for code, for data, and for model weights**, and record the answer per artefact rather than per
repository. This KB has now verified **six licence inconsistencies** and two licence-split shapes;
the split is more dangerous than the inconsistency, because nothing about it looks like an error.

## The education-benchmark literature is outrunning its artefacts — NEW in p323

p322 retired a five-pass gap and declared the evaluation layer *"a real and usable tier."* **That
holds. But pass 323 touched four 2026 education benchmarks and the supply picture is worse than the
publication picture:**

| Benchmark | Venue / date | Code | Licence |
|---|---|---|---|
| **EduGuardBench** | arXiv 2511.06890, **AAAI proceedings** (art. 40399) | **Yes** — 2 datasets, scripts, notebook, appendix | 🔴 **none** |
| **EduClaw-Bench** | arXiv 2608.03206, 4 Aug 2026 | **Anonymous review link only** | n/a |
| **EduFair-Bench** | arXiv 2609.12949, 11 Sep 2026 (EPFL) | **none found** | n/a |
| **ELBench** | arXiv 2608.09548, 10–11 Aug 2026 | **none found** | n/a |

**Four papers, one repository, zero licences.** The one artefact that shipped is the one published
in conference proceedings — and it has no LICENSE file, so it cannot enter a deliverable.

**Three findings from these papers that a studio can use without any of the code:**

1. **Capability and fairness are largely orthogonal** (EduFair-Bench). A stronger model is not a
   fairer tutor, so model upgrades are not a fairness remediation. **And the gaps are largest on
   language and immigration cues, not gender and SES** — the opposite of where fairness review
   effort usually goes. For any EMEA or North American public-sector bid, this reorders the test
   plan.
2. **Safety is not monotonic in model size** (EduGuardBench). Mid-sized models were the most
   vulnerable to persona-based academic-misconduct prompts. **"We used a bigger model" is not a
   safety argument.** The same paper's *Educational Transformation Effect* is the useful positive:
   the safest models convert a harmful request into a teachable moment, and that capacity is
   **strongly negatively correlated with attack success rate** — pedagogy and safety aligned, which
   is rare enough to design toward.
3. **Education-specialised models lead neither education module** (ELBench, over nine models). The
   premise that a domain-tuned education model beats a frontier general model on education tasks did
   not hold in the one multi-module comparison published this year. **Authors' own caveats: the data
   is synthetic and the benchmark text-only.**

**The practical read:** evaluation in this sector is still something an engagement *builds*, using
MathTutorBench's task shapes and the pre-registered audits' discipline (freeze the data, hash it,
keep a decisions log). **The 2026 benchmark literature is a source of test design, not a source of
tooling** — and anyone claiming an off-the-shelf pedagogical eval suite should be asked which
repository and which licence.

## The skill tier can carry a personality-rights payload — NEW in p323

Trend 7 has read the skill-as-unit shift as a packaging and licensing story. **Pass 323 found a
sub-pattern it had not anticipated: permissively licensed skills whose product value is a named,
living educator's teaching persona.**

`tong666-bit/liu-xiaoyan-skill` (**MIT**, 18 ★) teaches CET-4/6 and postgraduate-entrance English
*in the style of* 刘晓艳; its sibling `tong666-bit/song-hao-math` (4 ★) does the same for 宋浩.
**Both disclaim clearly and unprompted** — *"非本人、非官方出品"* (not by the person, not an official
product), *"刘晓艳风格，非官方"*, and an explicit statement that the class-style lines *"不冒充老师
原话"*, they do not pass themselves off as the teacher's actual words.

**The structural point: an MIT licence grants rights in code and grants nothing in a persona.** Name,
likeness and teaching identity are personality / right-of-publicity interests held by the
individual, and they do not travel with the repository's licence. **A permissive badge therefore
clears the code and leaves the actual exposure untouched**, which makes this a third variety of the
licence-split problem above — code permissive, the valuable thing not licensed at all, and in this
case not licensable by the repository author.

**Guidance:** read these skills for the pedagogy — the attributed-style framing is a genuinely
effective engagement device and the exam-prep structure is well built. **Never reproduce the persona
framing in a Globant deliverable**, and treat any client request to "make it teach like
[named person]" as a legal question before a technical one. **Currently an APAC-only pattern**
(four of the ten repositories on the first page of the new-supply sweep are Chinese-language
exam-prep skills). Watch for its arrival in Western skill registries; it has not appeared there yet.

## The licence file is not the grant — in either direction — NEW in p324

Three consecutive passes have found licences fragmenting, and each pass found a different seam:

| pass | the seam | instance |
|---|---|---|
| p322 | **by architectural layer**, across an organisation | `openeduhub`: Apache-2.0 shells, GPL-3.0 analysers, **unlicensed** inference core — extended in p324 to the data substrate *and the public UI* |
| p323 | **by artefact type**, inside one repository | `haolpku/K12-KGraph`: *"Code (this repository): MIT"*, *"Dataset (graph, benchmark, training data): CC BY-NC-SA 4.0"* |
| p324 | **by channel, with the restrictive channel being the prose one** | `ZhijieXiong/pyedmine`: the MIT text in `LICENSE` — under `Copyright (c) 2023 Stanford Future Data Systems`, an unrelated holder — and a README reading *"All data and code in this project may be used only for academic purposes."* |

🔵 **The first two reduce to one sentence: permissive at the edges, restricted at whatever took the
work.** p324's does not reduce to anything reassuring. **It means the `LICENSE` file is not
sufficient evidence of the grant in either direction**, and the direction matters commercially:

- **File more permissive than the prose** (`pyedmine`) — **a dependency scanner returns MIT and
  the repository clears procurement**, while the author's own specific sentence forbids the use.
  This is the dangerous direction, because the automated control reports *pass*.
- **Prose more permissive than the file** (`openeduhub/metadata-agent-api`, `metadata-agent-canvas`,
  `duplicate-detection`, `wlo-quellenliste`; `classroomio` declaring three licences on three
  channels) — **the scanner catches it**, and the cost is a conversation rather than an exposure.

🔴 **Two corollaries worth a line each in a diligence checklist.** A licence file can carry
**somebody else's copyright line** and still be a valid grant from nobody in particular —
boilerplate copied without editing is now observed often enough to look for. And a manifest can
state a licence **that is not a valid SPDX identifier** (`openeduhub/skohub-vocabs-oeh-patched`:
`"license": "Apache License 2.0"` where `Apache-2.0` is the identifier), which an SPDX-strict
scanner reads as *unknown* rather than as Apache — a false negative in the opposite direction.

**What a studio should do with this:** read **every** channel a repository publishes — `LICENSE`,
the README, the package manifest, and per-directory licence files — and when they disagree, **plan
against the most restrictive one and get the contradiction resolved in writing before the grant
matters.** On this KB's own shelves that rule moves 4 of 48 foundational repositories out of the
usable set that a scanner would have waved through.

## The declared-gap discount — a method trend, measured four times — NEW in p324

This is a trend about this KB rather than about the sector, and it has now been measured often
enough to be a policy. **Four consecutive passes have overturned a gap this KB had declared, each
time by changing the query rather than by the world changing:**

| pass | gap as declared | what changed | outcome |
|---|---|---|---|
| p322 | *"no repository located"* for AITutor-EvalKit (p318) | searched the **tool name** from the paper | exists, MIT, public |
| p323 | *"no verified curriculum dataset at all"* after sweeping 180 `ncert`/`cbse` repositories (p322) | searched **curriculum knowledge graph / prerequisite** instead of the country topic | **two** artefacts, one NeurIPS-accepted |
| p324 | *"no credible open source AI-detection or academic-integrity project"*, 7 passes | searched the topic **`plagiarism-detection`** instead of *AI detection* | three substantial artefacts, two permissive |
| p324 | the LTI 1.3 agent gap, 8 passes | **three** changed queries on a **changed instrument** | **held** — the first gap here with positive evidence behind it |

🔵 **The rule: a declared gap is a statement about the query, not about the world, until the query
has been varied — and a topic sweep is a query, not a census.** Every "searched and not found" line
in this KB should be read with that discount applied, and the only gap currently exempt is the LTI
one, because it is the only one that has survived both a changed query and a changed instrument.
🔴 **For a client conversation this cuts both ways:** it is the reason this KB's gap claims are
worth something (they are re-tested, and they fall when they should), and the reason a gap should
never be quoted as *"nothing exists"* — the honest phrasing is **"nothing was found by these
queries, which are named."**

## 1. Institutional AI deployment is not landing — and that, not adoption, is the gap

Earlier passes framed this sector as "usage is ahead of governance". The Digital Education Council
AI in Higher Education Global Survey 2026 (**45,398 responses — 27,284 students, 18,114 faculty —
across 35 countries**) supports a sharper reading:

- **88% of students use AI; 77% of faculty do, up 16 points year on year.**
- **43% of students report no AI integration in their courses at all.**
- Among students who *have* experienced institutional AI integration, **only 5% say it transformed
  how they learn.**
- **Only 29% think their instructors are equipped to guide them — 17% in the US and Canada.**
- **64% of faculty have had AI literacy training; 31% feel involved in shaping AI policy.**

**Pass 319 adds the hard case, and it is a national one.** South Korea mandated AI digital
textbooks, then retreated to voluntary adoption after teacher and parent resistance, and on
**2025-08-04** the National Assembly removed them from the statutory definition of a textbook
altogether, withdrawing funding with it. Usage had already decayed inside a single year: **~37% of
eligible classes in the first semester of 2025 to 19% in the second; schools from ~4,190 to
2,095**; overall adoption roughly 30% of schools, ranging from 98% in Daegu to 8% in Sejong.
*(Snippet-sourced; the primary reports were unreachable this pass. Note the date — this KB was
carrying it as August 2026, which was wrong.)*

**That is this trend's thesis at national scale**: the technology was available, the mandate was
real, the money was spent, and the deployment did not land — because preparation, teacher
capability and consent were treated as rollout details rather than as the project.

Adoption is solved. Institutional deployment is near-absent, and where present it is judged
worthless by 95% of the students exposed to it. **Implication:** the sellable work is not
"introduce AI" and not only "govern AI" — it is making an institutional deployment that students
can tell apart from the chatbot they already use. Training exists (64%) and is not working; that is
a programme-design problem, not a content-sourcing problem.

## 2. Procurement is policy-gated, and the US volume has gone up again

**134 AI-in-education bills across 31 states in 2026**, inside a wider wave NCSL counts at ~1,390
AI bills across 49 states. Ohio requires an AI framework in every public/community/STEM school by
2026-07-01; North Carolina's model policy is due 2026-12-31 with local policies by 2027-06-30;
Idaho SB 1227 mandates a statewide framework plus a human-teacher guarantee; California AB 1159 on
student data; Oklahoma and Maryland reported to require human oversight and bar AI from high-stakes
student decisions. Federally, H.R. 8747 (K-12 AI Literacy and Readiness Act of 2026) cleared
committee markup on 2026-07-21. **Pass 319: four states now have *enacted* education-specific AI statutes** — **Idaho, Maryland,
Oklahoma and Virginia** — each requiring state-department guidance **and** aligned local school
board policies, with Oklahoma adding educator supervision, human review, a bar on high-stakes
AI decisions and parent disclosure. **Guidance coverage is now ~33–35 states plus Puerto Rico**,
and curriculum mandates have started arriving alongside the guardrails (Georgia and Mississippi CS
credits including AI; **Alabama requires an approved CS course with AI instruction to graduate**).
Bill counts across trackers disagree — one source found this pass says "around 100" bills in the
2026 session against this KB's 134 across 31 states — **so cite the tracker and the date.**

**The RFP question has shifted from "what can your tutor do" to
"show me the audit trail."**

**Revised this pass: the binding constraint in US K-12 is not a bill, it is a rule already in
force.** Full compliance with the **amended COPPA Rule has been required since 2026-04-22**
(published 2025-04-22, effective 2025-06-23). **§312.5(a)(2) requires separate verifiable parental
consent before a child's personal information is disclosed to a third party**, with the exception
limited to disclosures *integral* to the service; the Rule also adds retention limits, a written
published retention policy, and biometric identifiers to the definition of personal information.
**Forwarding a K-6 pupil's prompts to a third-party model provider is such a disclosure.** State
bills set deadlines for *policies*; COPPA sets a live federal obligation on *architecture*, and
every K-12 AI deployment shipped before April 2026 should be assumed non-compliant until audited.
That is the most concrete near-term revenue line in this KB — see `intel/market.md`, North America.

## 3. Restriction is now a design requirement, not a market loss

New this reading of North America: **New York City runs a one-year moratorium on student-facing AI
through eighth grade**, and **Katy ISD (Texas) is banning generative AI chatbots for K-6.** These
are not outliers to wait out — they are the shape of K-12 procurement. A product that cannot
enforce **grade-band gating** and a **teacher-facing-only mode** is unbiddable in those districts,
and the gate is cheap to build. Treat restriction as a feature spec.

**Pass 319 adds the enforceable version of this, and it is a statutory feature rather than a
sentiment.** Per one tracker, Oklahoma's 2026 law gives **parents an opt-out from student-facing
AI tools together with a duty to provide alternative access to core instruction** *(single-tracker
claim, not read against the statute — verify, but build for it)*. That turns restriction from a
market-sizing question into three concrete components: **a per-pupil opt-out flag that degrades
gracefully**, an **approval queue** so nothing AI-written reaches a student or a record without a
named educator signing it, and a **decision log** proving no high-stakes determination was AI-made.
All three are cheap; all three are now bid-qualifying in parts of the US. See pattern P7.

**Quantified by country this pass, and it does not follow the regulatory map** (Ipsos Education
Monitor 2026, support for banning AI in schools): **Indonesia 23%, India 26%, Japan 29%, South
Korea 31%**, with **Australia and New Zealand above all of them.** So the market with the region's
only binding AI statute (Korea) has middling public appetite for restriction, while the markets
with *no* AI statute (Australia, New Zealand) have the highest. **Restriction sentiment and
regulation are separate variables and must be scoped separately** — the gating feature is sold on
public and parental sentiment, the audit trail is sold on statute, and a bid can need one without
the other.

## 4. The permissive-agent / copyleft-platform split is holding — recounted again in p319

**Recounted in pass 319 over 26 agents and 27 platforms, and the split is holding.** **22 of 26
agents** carry a permissive software licence — the pass added six MIT rows and one Apache-2.0 —
while **15 of 27 platforms** are GPL-2.0/GPL-3.0/LGPL-3.0/AGPL-3.0, with the AGPL count rising
from 7 to 8 (`ClassroomIO`). **Two qualifications pass 319 forces, and both matter more than the
ratio:**

- **The two permissive platforms added this pass are dead code.** `menthorlabs/menthor`
  (Apache-2.0, 582 ★) was archived on 2024-12-12; `edrys-org/edrys` (MPL-2.0, 334 ★) states it is
  no longer under active development. The *usable* permissive platform set has not grown.
- **A fourth category now exists and it is not copyleft at all.** `PageLM` (bespoke Community
  Licence) and `advisingapp` (Elastic 2.0) are **source-available, not open source**, and
  `i-diario` and `ipti/br.tag` could not be resolved from their pages. **"Permissive vs copyleft"
  no longer describes this market; "shippable vs readable-only" does.**

The architecture advice is unchanged and now covers more cases: permissive agents across a network
boundary from a platform you do not modify — copyleft, source-available or unresolved alike.

**But "the platforms are all copyleft" is no longer an accurate sentence**, and pass 317 found the
crack widening from both sides at once:

- **`OpenOLAT/OpenOLAT` — Apache-2.0, 448 ★, 31,877 commits.** A mature LMS from frentix GmbH
  (Switzerland), built on the University of Zurich's OLAT 7.1. Unlike mentingo this is not a
  promising young project; it is institution-grade software under a permissive licence, and it means
  there now exists a real LMS where Globant can link agent code into the platform instead of paying
  the LTI-boundary tax. **6 of 16 platforms are now permissive.**
- **`plastic-labs/tutor-gpt` — GPL-3.0, 932 ★.** Copyleft arriving in the *agent* tier, going the
  other way. One row, but the first.

**What has not changed is the advice**, and this is the important part: for a client already running
Moodle, Canvas or Open edX — which is nearly every client — the copyleft platform is a given and the
LTI boundary is still mandatory. The softening matters only for greenfield and sovereignty
engagements. Do not let it loosen the architecture discipline in the other 90% of cases.

**The deeper lesson is about method, not licences.** OpenOLAT has 31,877 commits and was missed by
316 passes because it has 448 stars. With Ed-Fi (12 ★) and Sunbird (41 ★) that is three
confirmations that **a star-ranked search cannot see this sector's institutional infrastructure** —
it is adopted through procurement, not GitHub. Treat the remaining declared gaps in this KB as
search-method artefacts until proven otherwise.

## 5. Deterministic pedagogy under a generative surface is now a shipped architecture

This KB has argued for three passes that the LLM should explain while a deterministic engine
decides. `ArnaudGuiovanna/tutor-mcp` (MIT, 467 commits) ships exactly that — skill graph, Bayesian
Knowledge Tracing, FSRS scheduling, prerequisite gating and cross-session narrative memory — under
the stated principle **"Generative teaching. Deterministic pedagogy."** DeepTutor's own framing is
"lifelong personalised tutoring" (41.7k ★, v1.6.15 on 2026-10-19, now with arXiv 2604.26962), and
gen-mentor's multi-agent ITS architecture was a WWW '25 oral.

The argument has moved from position to implementation. **A 2026 tutor needs a learner model that
persists across sessions and a non-LLM component that decides what comes next** — and that is now
something to integrate rather than build.

## 6. MCP, not LTI, is where agent integration is actually happening (added p317, revised p319)

### 🟢 Pass 325 — this trend's first POSITIVE evidence, after nine passes of arguing from absence

**Nine passes recorded *no LTI 1.3 AI agent* and every one of them argued from an empty search.**
p325 tested the gap on a **third instrument — GitHub code search, new to this KB** (`lti_1p3 mcp
server tutor language:python` → **0**; `"pylti1p3" OR "ltijs" mcp agent tutor` → **6 hits, none an
agent**) and then found the explanation on the **supply** side, which is where this trend finally
gets a measurement instead of an absence:

🔴 **`openfun/django-lti-toolbox` — MIT, 14 ★, 34 commits, *"a Django application to build LTI Tool
Providers"*, NO release, last pushed `2024-11-14`.** Roughly **twenty-three months untouched**,
published by the operator of France's national public MOOC platform, whose MCP-era peer repositories
ship weekly — and whose own learning-analytics UI, `openfun/warren`, **still renders inside an LTI
iframe.**

🔵 **The reframing, and it is the version to use with a client.** The LTI plumbing is **permissive,
institutional, functional and abandoned.** The absence of LTI agents is therefore **not a tooling
gap** — the library exists under MIT — **it is agent-side non-adoption of a live standard whose
maintenance has stopped.** So the sentence changes from *"nobody has built an LTI agent"* (which
invites the client to ask why you cannot) to: **"the LTI integration layer is permissively licensed
and effectively unmaintained, so either budget the maintenance or integrate over MCP."** Both are
answerable; only the second is cheap.

🟡 **And note what this does NOT say.** LTI is not dead as a *delivery* surface — `marsha` (150 ★,
MIT) is an LTI content-management system and `warren` is delivered through an LTI iframe, both from
the same operator. **Institutions still mount tools via LTI. Agents are not being written to be
mounted that way**, which is a statement about who is building, not about what schools can accept.

Every integration artefact found this pass speaks **MCP**: `tutor-mcp` (an entire ITS as an MCP
server), `ankimcp/anki-mcp-server` (520 ★, spaced repetition exposed to any LLM client), Canvas
MCP servers in the wild, `iblai/api`. None of them speaks LTI 1.3, SCORM or xAPI.

This is a genuine fork in the road. MCP gets an agent to *tools*; LTI gets an agent into the
*institution* — launch context, roster, identity, gradebook passback. **A tutor that is MCP-native
and LTI-absent works beautifully for an individual learner and cannot be deployed by a university.**

**Revised in pass 319: a third unlicensed artefact at the same seam, and the first real library
alternative.** `JaimeArriagadaRosas/Plugin-Feedback-Canvas` (0 ★, **160 commits**, Spanish docs) is
a full-stack **LTI 1.3 plugin for Canvas** in which AI-generated academic feedback must be reviewed
and approved by the instructor before it reaches the student — the human-in-the-loop control US
district policy now demands, built and working, **with no LICENSE file.** Three for three: the work
closest to institutional integration is written by instructors and university staff solving their
own course, and it is the least likely work in the sector to carry a licence.

**What did change is the library floor.** `tsugiproject/tsugi` — **Apache-2.0, 376 ★, 266 forks,
4,011 commits, Apereo Incubating**, maintained around the co-author of the LTI specification — is
an order of magnitude larger than `pylti1.3` (178 commits, 39 open issues, no published release,
re-verified p319). It is PHP, and **its page does not state which LTI versions it implements**, so
the Advantage-surface question is open and is pass 320's highest-value one-page-load check. Add
`jcputney/scorm-again` (MIT, 356 ★, 1,229 commits, SCORM 1.2 and 2004) and the integration tier is
no longer a single 138-star dependency.

**Carried from pass 318 and still true: the LTI-native tutor exists and has no licence.** `blamb/lti-tutor` implements LTI 1.3 against Moodle with dynamic registration, deep
linking (each tutorial placed as its own External tool activity) and completion passback through
Assignment & Grade Services, on `ltijs`. **Its README states the licence as "To be decided." 0 ★,
39 commits.** Default copyright therefore applies and Globant cannot use it.

That is the second unlicensed repo this KB has had to reject at exactly this point in the stack
(after `luffycodes/Tutorbot-Spock`), and together they suggest something structural rather than
coincidental: **the work closest to the institutional integration problem is written by instructors
and university staff solving their own course, not by labs or vendors with legal review — so it is
the least likely work in the sector to carry a licence.** Expect to find the answer to an
integration problem in an unlicensed repo, and budget to rebuild it.

The glue therefore remains yours to write. `pylti1.3` (MIT, 138 ★, 178 commits) is still the only
solid library, and pass 317 confirmed it covers the full Advantage surface — Deep Linking, AGS,
Names and Roles, Course Groups, Submission Review, Data Privacy Launch. **"MCP server inside, LTI
tool outside" stays the integration shape to standardise on**, with one caveat now named: every
pattern in this KB crosses the LMS boundary through that single 138-star, single-maintainer library.
That concentration belongs in the risk section of any SOW.

## 7. The skill, not the app, is becoming the unit of educational AI (added p317, measured p319)

Among the highest-starred repos under GitHub's `ai-tutor` topic, a striking share are **agent
skills rather than applications**: `GarethManning/education-agent-skills` (878 ★, 165
evidence-grounded teaching skills), `ZeKaiNie/universal-examprep-skill` (309 ★),
`SenmuuuuW/universal-diagnostic-tutor-skill` (247 ★), `KeWang0622/kaogong-skill` (189 ★),
`flysheep-ai/education-skills` (116 ★). `Li-Evan/Bloom` (MIT, 289 ★) ships **both** a skill bundle
and a self-hostable web app.

**Pass 319 measured this trend and it is bigger than the `ai-tutor` topic suggested.**
`virgiliojr94/book-to-skill` — a converter that turns a technical book into a structured agent
skill — has **35.3k stars and 3.7k forks on 228 commits**, which makes it one of the largest
education-adjacent repositories in this KB. `Miaotofu01/Study-Mate` is **MIT, 1.1k ★, 723
commits**, shipped as plugin packages for three different agent hosts. `JuneYaooo/lineage-skill`
(Apache-2.0, 459 ★) distils videos, PDFs and transcripts into a **source-backed** teaching skill.
`ZeKaiNie/universal-examprep-skill` (MIT, 309 ★, 183 commits) installs across **40+ agent hosts**
through one command and keeps all state local with no vector database.

Two consequences, and the legal one has flipped. **Commercially:** the distribution unit is
shrinking, and a client's "AI tutor" may arrive as a prompt bundle their faculty installed below
procurement's line of sight — a shadow-IT problem that governance work (trend 2) has to cover. It
now arrives through `npx skills add` across dozens of hosts, so there is no single gate to watch.
**Legally: the "skill bundles come under content licences" claim is no longer generally true.**
`education-agent-skills` is still **CC BY-SA 4.0** and the ShareAlike obligation on derivative
teaching material is still a live constraint — but **`lineage-skill` is Apache-2.0,
`universal-examprep-skill`, `Study-Mate`, `claudemy`, `algo-sensei` and `book-to-skill` are MIT**,
and `book-to-skill` draws the right line explicitly: **its MIT licence covers the converter and
pointedly not the books processed with it.** That distinction — permissive tooling over
third-party content whose rights you must clear separately — is the real licence conversation in
this tier, and it lands on day one of any "turn our textbooks into a tutor" engagement.

## 8. Retrieval-grounded tutoring is table stakes — and the incumbent is shipping it free

LightRAG (MIT, 40.2k ★) alongside DeepTutor from the same lab made curriculum-grounded answering
the default architecture. **Instructure's Project Athena, announced 2026-07-22, is course-context
grounding built natively into Canvas**, positioned as coaching "toward mastery, not answers".

**Pass 319 put a number on it, and the number argues for data over models.**
`bncc-dev/bncc-benchmark` measured curriculum hallucination on Brazil's BNCC across 8 models and
300 items: **31.9% with no source, 0.2% with the curriculum pasted into the prompt, 2.3% querying
the verified dataset over MCP** — a 30.6-point average drop — while **faithful-text rates across
the models tested ranged from 88% down to 3%.** Model selection cannot close a 30-point grounding
gap, and the MCP route costs about two points against pasting the data in. See trend 12.

**Grounding in the client's own material is no longer a differentiator against Canvas.** What
remains defensible: the **verified** data layer underneath the grounding (trend 12 — the thing
Canvas cannot ship for a jurisdiction it does not own), the deterministic pedagogy layer (trend 5),
the governance and audit layer a US district must buy anyway (trend 2), a defensible efficacy
measurement (trend 9), and anything on-premise or offline. Price and pitch accordingly.

## 9. Assessment integrity has settled on process evidence — and the "no open source integrity project" premise is RETRACTED in p324

Institutions continue moving to oral defence, process-based work and "use it, cite it" disclosure.
**57% of students say their assessments come with inadequate AI guidance** (DEC 2026) — the gap is
guidance, not detection.

~~Searched again this pass: there is still **no credible open source AI-detection or academic-
integrity project.**~~ 🔴 **RETRACTED in p324, and the retraction is about the query, not the
sector.** That sentence stood for **seven consecutive passes** on sweeps for *AI detection* and
*AI-detection agent*. The GitHub topic **`plagiarism-detection`** — same sector, different query —
returns **twelve repositories pushed since 2026-01-01 above ten stars**, three of them
substantial, all three measured first-hand in p324:

- 🟢 **`sunilgentyala/aegis-integrity` — MIT, 17 ★, 68 commits, v3.3.2.** A **local-first academic-
  integrity checker exposed as an MCP server with seven tools**, over citation-hallucination
  resolution against Crossref, AI-text signals (GPT-2 perplexity, burstiness, stylometric
  ensemble), corpus-based plagiarism (n-gram MinHash + SBERT/FAISS), ghostwriting detection
  (Burrows' Delta) and venue-guideline checks for IEEE, ACM and Elsevier.
- 🟢 **`NoplagLabs/noplag-engine` — Apache-2.0, 86 ★.** Winnowing fingerprints in GIN-indexed
  PostgreSQL with seed-and-extend alignment to exact character ranges, behind five REST endpoints.
- 🟡 **`jplag/JPlag` — GPL-3.0, 2.0k ★, 376 forks, 5,708 commits.** Source-code plagiarism **and
  collusion** detection over twenty-odd languages, CLI or Java API, local report viewer.

🟢 **What survives, and it survives stronger: the recommendation.** The *judgement* this trend
reached — process evidence over detection, and that the gap "should stay a gap" for AI-text
*verdicts* — is now **corroborated by the tools themselves rather than by their absence**.
`aegis-integrity` publishes **no accuracy figure for itself**, cites third-party studies instead,
and states *"Results are a supporting signal for human review, not a determination of
misconduct"* and, on ESL bias, *"Do not treat AEGIS as having solved ESL false positives; keep a
human in the loop."* `noplag-engine` puts *"paraphrase, semantic, and AI-writing detection"* on the
roadmap rather than in the product, and warns against reading its plagdet figure as general
accuracy. **The best-engineered artefacts in this category refuse to make the claim this trend
warned about.** Published work still finds AI-text detectors inaccurate and unreliable, and the
proctoring posture (YOLO/OpenCV/MTCNN pipelines, Electron kiosk browsers, much of it stale or
unlicensed) still carries privacy and fairness exposure.

🔵 **So the sentence to use with a client changes shape.** Not *"there is no open source for
this"* — there is, and it is good — but: **the credible open source in this category is a
citation, provenance and similarity layer that produces evidence for a human, and the thing that
does not exist is an AI-authorship verdict anyone should act on.** The process-evidence stack
(nbgrader, otter-grader, JupyterHub provenance) is the foundation; `aegis-integrity` is the
citation and prose layer on top of it; JPlag or `noplag-engine` is the similarity engine; and
`compose/patterns.md` **P11** wires the three together. **Sell the evidence chain, never the
verdict.**

**The adjacent gap, however, is closed — and this is the substantive change in pass 319.** For four
passes this KB said there was no credible open source way to measure whether a tutor *teaches*.
There now is, in four pieces (detail and licences in `agents/top.md`):

- **`eth-lre/mathtutorbench`** — EMNLP 2025 main-conference benchmark, 3 teacher skills and 7
  tasks, **scoring pedagogy with a ~1.5B scaffolding reward model against ground-truth teacher
  utterances rather than an LLM judge.** Its licence is self-contradictory (CC BY 4.0 badge, CC
  BY-SA 4.0 footer) — the fifth licence inconsistency this KB has verified and the first in the
  eval layer.
- **`kaushal0494/AITutor-EvalKit`** — MIT, MBZUAI EduNLP Lab, v1.0.0. **Pass 318 searched for this
  and concluded "no repository located". It exists.**
- **`bydeng01/conv-vs-ped-tutor`** — MIT, pre-registered audit of whether an LLM helpfulness judge
  **rewards answer leakage that reduces the student's later independent work**, with two tutors
  wrapping the same frozen base model and differing only in policy structure.
- **`bydeng01/ability-levels-audit`** — MIT, pre-registered, hash-verified frozen data, 990 judge
  ratings, finding that **difference-in-differences on a censored rating scale can manufacture an
  effect that is not there.**

**The convergent finding is the trend: LLM-judged "helpfulness" is not a pedagogy signal, and the
standard before/after presentation of it can invent results.** A study found at AIME-Con 2026
reaches the same place from the judge-validation side — human oversight remains necessary for
nuanced instructional assessment *(snippet-sourced)*. **This forces a correction to pass 318**,
which called `ahmedEid1/lumen` the most credible artefact of its pass for publishing authoring
3.85/5, tutor 2.33/5 and ingest 0.83/5 about itself. The *habit* is still admirable; **the numbers
are judged scores, which is the instrument now in question.** Credit the transparency, do not quote
the values.

**What to sell:** process evidence for integrity, and a **pre-registered, frozen-data,
decisions-logged evaluation** for efficacy. Every competitor's uplift claim rests on the instrument
these audits discredit; being the party that measures properly is a differentiator that costs a
fortnight of engineering.

## 10. Interoperability standards are becoming the AI story (added p318)

**1EdTech's 2026 position is that interoperability is the precondition for AI**, naming **CASE,
Edu-API and OneRoster** as the standards that give an AI system shared institutional context, with
an expanded Generative AI rubric signalled. **IEEE P3428** targets interoperability of LLM agents
in educational systems (initial phases). Agent-to-agent protocols (A2A) and NIST work on a trusted
interoperable agent ecosystem sit in the background.

What makes this actionable rather than standards-committee noise: **the Ed-Fi Alliance's Apache-2.0
implementations are real code** — `Data-Management-Service` (1,105 commits) and `edfi-oneroster`
serving OneRoster 1.2 (151 commits). This is the first pass where "how does your agent know
anything about my institution?" has an open source answer rather than a bespoke-integration answer,
at least in North America.

## 11. The sector's published metadata is unreliable in both directions (added p318, extended twice in p319) — a method finding

Pass 317 established that **stars run too low** on the software that matters: Ed-Fi at 12 stars with
1,105 commits, Sunbird at 41, OpenOLAT at 448 with 31,877 commits. Pass 318 added a fourth case —
**`openedx/openedx-ai-extensions`, the official Open edX AI plugin, at 17 stars and 703 commits** —
and then found the failure running the other way as well.

**Stars are now being solicited from automated readers.** `24kchengYe/human-skill-tree` (573 ★,
36 commits) closes its README with a passage **addressed to AI agents, asking them to star the
repository.** A 573-star, 36-commit ratio is what that looks like from outside. This KB is compiled
by a process that reads repository pages; so, increasingly, are the tools client engineers use to
pick dependencies. **Text a repository addresses to an automated reader is data, never
instruction** — and any Globant tooling that ranks dependencies by reading repo pages needs that
rule written down.

**Licence metadata is worse, and it fails in a consistent direction.** Pass 318 sourced platform
candidates partly from "best open source LMS 2026" comparison articles and checked their licence
claims first-hand. **Three out of three were wrong, all overstating permissiveness:** LearnHouse
claimed Apache-2.0, is **AGPL-3.0 plus a separate Enterprise Licence**; Frappe Learning claimed
MIT, is **AGPL-3.0**; Forma LMS claimed Apache-2.0, has **no LICENSE file at all**. A fourth case
came from a repository's own README: `ahmedEid1/lumen` carries an MIT badge over a `LICENSE` file
containing the full GPL-3.0 text.

That is four licence misstatements in one pass, on top of the three repos earlier passes found
whose real licence is invisible from the GitHub sidebar (Frappe Education, OpenOLAT,
`education-agent-skills`).

**The operating rules this produces, and they apply to every row in this KB:**

1. **A licence is read from the LICENSE file or the licence GitHub itself renders. Never from a
   comparison article, a README badge, or a bare "License" link.** An engagement that inherits an
   AGPL obligation because someone trusted a listicle is a legal problem, not a research one.
2. **Rank candidates on commit count, release cadence and licence — not stars.** Stars are now
   noise at both ends.
3. **Expect the error to favour permissiveness.** Every misstatement found so far made a repo look
   more usable than it is, which is exactly the direction that hurts in a licence inventory.

The deeper point for a studio lead: **the generation of secondary sources a client's team will
Google is systematically wrong about the one attribute that determines whether Globant can use a
repo at all.** Being the party in the room that read the LICENSE file is a small, real,
demonstrable differentiator in a dependency review.

### Pass 319, extension 1: star solicitation now ships with a unit test and a CI job

Pass 318 found a README asking AI agents to star a repository. Pass 319 found the engineered
version. **`karanb192/algo-sensei` (MIT, 293 ★, 63 forks, 9 commits)** ships exactly one file in
`scripts/` — **`star_invitation.py`** — plus `tests/test_star_invitation.py` and a dedicated
workflow, `.github/workflows/invitation-tests.yml`. Read first-hand, the script is a
once-per-machine gate: exclusive creation of a marker file under `$XDG_CACHE_HOME` or
`~/.cache/algo-sensei`, printing `offer` on first run and `skip` on every subsequent run, concurrent
run or error, with the comment *"Exclusive creation prevents simultaneous or later sessions from
asking again."*

**In fairness: this is the polite version** — ask once per machine, ever, with no text aimed at an
automated reader and no deception. **And it is still star acquisition with CI behind it in a
repository with nine commits and 293 stars.** When the distribution unit is a skill bundle
(trend 7), the moment of use *is* the distribution channel, and asking there is cheap and scales.
**Treat the ★ column as decorative.** It fails low on institutional infrastructure — Ed-Fi 12,
Sunbird 41, OpenOLAT 448 with 31,877 commits, the whole `bncc-dev` curriculum stack at 22/9/9 — and
it is solicitable at the top.

A smaller datapoint in the same direction: the German-language `bildung` topic carries **a
13-repository, single-author cluster of near-identical "tech evangelism" pages at one star each.**
**Topic pages can be padded**, so a topic sweep needs reading, not counting.

### Pass 319, extension 2: the licences themselves are leaving open source

Pass 318's finding was that *descriptions* of licences are wrong. Pass 319's is worse: among the
projects read first-hand this pass, **the three highest-starred new ones are outside open source**
— `CaviraOSS/PageLM` (2.0k ★, bespoke **"CaviraOSS Community Licence"**, commercial use by written
permission only), `xiaoyang111222/cn-math-taxonomy` (780 ★, **CC BY-NC 4.0**) and
`canyongbs/advisingapp` (340 ★, **Elastic Licence 2.0**, source-available, Gates-Foundation
supported). Add the open-core structures — LearnHouse's separate Enterprise Licence, ClassroomIO's
`LICENSE_KEY`-gated SSO and no-tracking — and five of the most capable systems in this KB are
commercially unavailable or partially withheld. **Two more were simply unresolvable from the page:
`portabilis/i-diario` shows no licence name, and `ipti/br.tag` claims BSD-3-Clause in its README
while its sidebar links GPL-2.0.**

**The rule to add: "open source" in this sector is a claim to check, not a category to filter on.**
Keep a two-column inventory per engagement — *what we can ship* and *what we may only read* — and
expect the second column to hold the best material. That is not a complaint; a reading list of
PageLM's feature set, cn-math-taxonomy's prerequisite graph, advisingapp's student-success data
model, lumen's eval harness and LTLTutor's misconception modelling is genuinely valuable. It is
just not a bill of materials.

## 12. Curriculum-standard data is the real moat — it has now been built three times, licensed for commercial use twice, and the moat has moved from the graph to the evidence — NEW in p319, **headline corrected in p323 and again in p326**

> **🟢 SECOND CORRECTION, pass 326 — the count goes to two, and the new one is not a country.**
> This trend has counted *national* curricula and asked which of them Globant can ship.
> `withmarbleapp/os-taxonomy` **does not fit the question**, which is why eleven passes of sweeps
> shaped by the question never returned it. It is **one dataset spanning seven curricula across
> three jurisdictions** — UK National Curriculum 2013, Common Core ELA and Math, NGSS K-5 and MS,
> C3 Social Studies, IB PYP PSPE — **1,591 micro-topics, 3,225 prerequisite edges (2,030 hard /
> 1,195 soft, every one carrying a prose reason), ages 4–15, 2,189 topic→standard links**, under
> **ODbL-1.0 + CC BY-SA 4.0 at 6.1 ★k.** Full read in `repos/foundations.md`; licence reasoning in
> *"The share-alike dataset is a commercial asset"* above.
>
> **So the sentence changes again: the artefact has now been built three times and licensed for
> commercial use twice** — Brazil's `bncc-dev` (MIT pipeline, CC BY 4.0 data, one country) and
> Marble's taxonomy (ODbL + CC BY-SA, seven curricula, share-alike). K12-KGraph's CC BY-NC-SA data
> still cannot enter client work.
>
> 🔵 **And the moat claim survives in a changed form, which is the part to carry into a bid.** The
> graph is now free, so **nobody can sell a client a curriculum spine any more.** What is still
> scarce — and what `os-taxonomy` explicitly does *not* provide — is **evidence that teaching it in
> this order works.** Its own teaching-research layer is agent-authored, unverified for this
> release, covers **1,051 of 1,591 topics** and is, in its own words, *"research-informed
> proposals, not empirically validated interventions."* **The moat moved from the graph to the
> evidence**, which is exactly where trend 9 and the evaluation tier in `agents/top.md` have been
> pointing, and where this KB's one measured classroom outcome (Panama, pattern P12) sits.
>
> 🔴 **Two limits before quoting it in a jurisdiction bid.** The age band stops at **11** while the
> literacy mandates it serves — Illinois HB 316 at grades 6–12 among them — run higher. And
> **four of the seven curricula ship codes only** (NGSS K-5, NGSS MS, C3, IB PYP PSPE) because
> their upstream terms forbid redistribution; **Common Core ships in full but stays under the
> purpose-limited CCSS Public License rather than ODbL.** The topic→standard links are intact
> throughout, so alignment claims survive everywhere; verbatim standard text does not.

> **🔴 CORRECTION, pass 323.** This trend's headline read *"exactly one country has built it"* for
> four passes. **It was wrong, and the artefact that disproves it has 420 stars and a NeurIPS 2026
> acceptance.** `haolpku/K12-KGraph` (`repos/foundations.md`) publishes **China's PEP K-12
> curriculum** as an evidence-linked knowledge graph: **10,685 nodes and 23,278 edges across 9 edge
> types over 48 textbooks**, **every edge carrying an `evidence` field linking back to textbook
> source text**, verified by **12 subject-qualified expert annotators at Fleiss' κ = 0.84** with
> **DAG validation of the `is_a` and `prerequisites_for` subgraphs** and a 3-expert spot-check at
> **98.4% fully correct**, plus a **23,640-question benchmark**, 2,267 training pairs and three
> released checkpoints. **That is the `bncc-dev` discipline, peer-reviewed, in a second
> jurisdiction.**
>
> **What survives, and it is the part that matters commercially.** K12-KGraph's README splits the
> grant: *"Code (this repository): MIT"* and *"Dataset (graph, benchmark, training data):
> CC BY-NC-SA 4.0."* **The pipeline is reusable and the curriculum is not** — NonCommercial rules
> out client work, and ShareAlike would attach to any derivative graph. **Brazil's `bncc-dev`
> remains the only verified national curriculum in this KB whose *data* Globant can ship**
> (MIT pipeline, **CC BY 4.0 data**). So the moat is real and the sentence changes: **the artefact
> has been built twice and licensed for commercial use once.**
>
> **Two further claims in this trend are retired by the same finding:**
>
> - ~~*"At 22 stars, nobody is competing for this yet."*~~ **Someone is.** 420 stars, 67 forks and a
>   NeurIPS Evaluations & Datasets acceptance, with academic backing, in China. The build-once
>   window is narrower than p319 priced it — see `compose/patterns.md` P10.
> - ~~*"India … hold no verified curriculum dataset at all."*~~ **Contested, not empty.**
>   `razi-03/NCERT-CKG` exists (Class X Mathematics, 18 NCERT PDFs, 10,417 CKG nodes, **1,682 / 1,682
>   semantic nodes with provenance**, 13,757 provenance-aware edges) and separates prerequisite
>   reasoning from textbook ordering, which is the right method. **It has no LICENSE file, 0 stars
>   and two commits**, so it does not close the gap — but p322 declared the gap empty after sweeping
>   180 repositories in the `ncert` and `cbse` topics, and **a changed query found this in one
>   search.**
>
> **The method lesson, now on its third consecutive instance:** p318 declared `AITutor-EvalKit`
> nonexistent and p322 found it by searching the tool name; p322 declared the Indian curriculum
> artefact nonexistent and p323 found one by searching the *artefact type* instead of the country
> topic. **A topic sweep is a query, not a census.** And note which sweep was *not* needed: p319's
> rule was to search GitHub topics in the region's own language, and p319's untested list named
> Arabic, Hindi, Japanese, Korean, French and Indonesian — **Chinese was never on that list, and the
> Chinese artefact was found this pass in English.** The language rule holds; it is not the only
> binding constraint.


Every pattern in this KB grounds a tutor in "the client's curriculum" and quietly assumes the
curriculum is available as data. **Pass 319 checked that assumption across five languages of
GitHub topics and it is false almost everywhere.**

**Where it is true: Brazil.** The `bncc-dev` organisation (Profy Tecnologias Educacionais) publishes
the **BNCC — Brazil's national curriculum — as 1,721 verified learnings** in JSON, SQLite, SQL and
CSV under JSON Schema, **MIT for the pipeline and CC BY 4.0 for the data**, with the 1,580 BNCC-2018
texts checked **character by character against the homologated PDF**, 30 contract checks in CI, a
decisions log for every source inconsistency, **an MCP server with seven tools and a hosted keyless
endpoint**, and a **published benchmark** of what grounding on it is worth:

| Condition | Curriculum hallucination |
|---|---|
| No source | **31.9%** |
| Data pasted into the prompt | **0.2%** |
| Model queries the MCP server | **2.3%** |

**That is the first quantified grounding claim in this KB**, and it reframes the economics. The
model matters less than the data layer: faithful-text rates across the models the benchmark tested
range from **88% down to 3%**, so no model choice closes a 30-point grounding gap.

**Where it is not true: everywhere else swept.** India has the sector's hardest curriculum mandate —
AI and Computational Thinking compulsory for **Classes 3–8 from 2026-27 across 32,900 CBSE
schools** — and the `ncert` and `cbse` topics (180 repositories between them) hold **no verified
curriculum dataset at all**: the one MCP server is unlicensed and **LLM-tags its chunks with no
human verification described**, the tutors are one- and three-commit projects, and the only
substantial data asset is a **2018** school scrape. Germany's attempt was **archived in 2021**. The
Dutch and Spanish-language topics produced course materials, not data. The English `oer` topic —
419 repositories — produced textbooks and **nothing describing curriculum or competency metadata.**
Ed-Fi (`repos/foundations.md`) covers North American **rostering**, which is a different artefact.

**Three implications, in order of how soon they bite:**

1. **Stop promising curriculum grounding as a configuration step.** Outside Brazil it is a data
   engineering project with a verification burden, and the verification is what makes it worth
   anything — an unverified, LLM-tagged curriculum index is a hallucination source with a schema.
2. **The build-once opportunity has a template and a deadline.** Port the `bncc-dev` pattern to
   NCERT/CBSE: verified extraction against the official source, schema, contract checks in CI,
   permissive code with attribution-licensed data, an MCP server. Named buyers: a board, a
   ministry, a national edtech. Pattern **P10**.
3. **It is a procurement moat, not a technical one.** Whoever holds the verified curriculum layer
   for a jurisdiction is in every bid in that jurisdiction, because the alternative is each vendor
   re-deriving it badly. ~~At 22 stars, nobody is competing for this yet.~~ **Retired in p323: at
   420 stars and a NeurIPS acceptance, someone is competing — in China, and with the data licensed
   NonCommercial.** The jurisdictions still uncontested are the ones to pick.

**The method behind the trend, worth copying on its own:** this was found by sweeping GitHub topics
**in the region's own language** (`educacao`, `educacion`, `bildung`, `onderwijs`, plus `ncert` and
`cbse`). Every regional absence this KB has declared was declared from English-language searches.
One Portuguese topic page produced a verified national curriculum, an MCP server, a published
benchmark and a 34,948-commit school-management system. **Before declaring a regional gap, sweep
the topic in the region's language — and record which languages you swept.** Untested: Arabic,
Hindi, Japanese, Korean, French, Indonesian.

## Trends asserted elsewhere that this pass could NOT verify

- **"Nearly two-thirds of European education systems have an AI strategy, guidance or policy
  framework."** Searched directly this pass against Commission sources and **not found.** The two
  Commission reports of 22–23 September 2026 are real and their conclusions are well attested; this
  fraction is not. **Do not quote it.**
- **A November 2026 date for the European Commission's education package.** Commission texts say
  "later this year" and name a **2030 Roadmap on the Future of Digital Education and Skills** as
  its content. The month came from a secondary summary. Likewise the **AI Literacy Framework
  (AILit)** and the **2026 ethical-use guidelines for educators** exist in search results, but
  their status — draft or final, voluntary or expected — could not be read because
  `education.ec.europa.eu` was unreachable.
- **A Q3 2026 edtech-specific venture funding figure.** Not found. Crunchbase's **$159B Q3 2026**
  is **all sectors** — repurposing it for edtech would be a serious error. Also rejected: a
  circulating "EdTech funding fell 89%" headline and an undated "$410M invested in 2026" figure,
  both inconsistent with HolonIQ's ~$1B H1 2026 (−26% YoY) and Crunchbase's just-under-$1.8B for
  the same period.
- **"South Korea spent $850M on AI textbooks."** Low-quality blog source; the de-officialisation
  (2025-08-04), the adoption decay and the funding withdrawal are well attested across multiple
  independent summaries, **the dollar figure is not.** One EU-based source attributes part of the
  unwinding to the Korean privacy regulator — also unverified.
- **Two 2026 pedagogical benchmarks seen only in snippets**, not counted in trend 9 until a public
  repository and licence are confirmed: **EduClaw-Bench** (arXiv 2608.03206; 30-day simulated
  learner, three-judge cross-family panel; code behind an anonymous review link) and
  **EduFair-Bench** (arXiv 2609.12949; pedagogical fairness across student demographics, judged by
  `gpt-oss-120b`).
- **Oklahoma's parent opt-out and alternative-access duty.** Reported by one tracker, not read
  against the statute. **Scope for it anyway** — the feature is cheap and the downside of missing it
  is a disqualified bid — but do not cite the statute until someone has read it.
- **"EdTech moving from pilots to mainstream deployment in 2026", including VR/AR.** Vendor and
  consultancy marketing. The DEC survey's 43%-no-integration figure argues directly against it.
  Do not put it in a client deck as fact.
- **"Language learning is the fastest-growing segment."** Single vendor blog. Unverified.
- **"European Commission published AI-in-education ethics guidelines on 2026-08-17."** Low-authority
  blog, unconfirmed against any primary source. Treat as false until verified.
- **APAC growing at ~48% CAGR.** A clear outlier against every other estimate in this KB.
- **Hinds Community College deploying Project Athena to 7,000 students.** Auto-generated news brief,
  not confirmed against Instructure's own release.
- ~~**South Korea's AI Data Protection Act imposing strict edtech privacy protocols**~~ —
  **RESOLVED AND CORRECTED this pass: there is no such act.** Korea's instrument is the **Framework
  Act on AI (Law No. 20676), in force 2026-01-22**, which reaches education through its high-impact
  category — the definitions name **student evaluation in early childhood, elementary and secondary
  education**. It is a real and dated compliance trigger, just not the one this KB was repeating.
  Details in `intel/market.md`. **The Australia/Japan data-governance claims came from the same weak
  source and remain unverified**; what is supportable for Australia is the opposite — no AI-specific
  statute, mandatory guardrails paused.
- **"The EU AI Act has been delayed."** A misreading this KB should be ready to correct, because
  clients will arrive holding it. **Enforcement began on schedule: the AI Office and national
  authorities started enforcing the Act from 2026-08-02.** What moved, under Regulation (EU)
  2026/1744 (in force 2026-07-27, Parliament 2026-06-16, Council 2026-06-29), is the **Annex III
  high-risk obligations, to 2027-12-02** — and nothing else. At least one major law firm's public
  AI-Act tracker still carries pre-adoption text calling the deferral "proposed", so the bad version
  has authoritative-looking sources behind it.
- **Corporate reskilling as a primary driver.** Named across several sources but never with
  education-sector-specific figures. Directionally credible, not quotable.
- **Moodle's AI "placements".** Secondary sources report two core placements (text editor, course
  support) in the 5.x AI subsystem. The **providers** list for 5.1 was confirmed from the official
  docs (Azure AI, DeepSeek, Ollama, OpenAI; DeepSeek new in 5.1); the **placements** claim was not.
  Verify before it enters a proposal.
- **The IDB's "193 AI solutions in LAC" figure and the DEC LATAM survey's sample size.** Both rest
  on search snippets: `www.iadb.org`, `www.digitaleducationcouncil.com` and
  `www.iesalc.unesco.org` all failed DNS resolution at this session's proxy. Brief on them;
  do not put them in a client document unconfirmed. **An unreachable source is not a verified one.**
- ~~**"No EMEA AI-in-education market size exists."**~~ — **RETIRED this pass. This KB was wrong.**
  Five passes concluded the figure was unpublished and advised abandoning the search. Two
  commercial houses publish Europe-specific figures (Marketdataforecast, SNS Insider); they
  disagree by ~9% on the 2025 base and publish no methodology. **"Weak" and "absent" are different
  findings, and this KB recorded the wrong one for five passes.** The lesson generalises: a
  declared gap should be re-tested with a changed query, not inherited.
