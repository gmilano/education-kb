---
industry: education
region: Global
updated: 2026-10-11
---

# Education — current trends

**Pass 117, 2026-10-11.** ⏱️ **Fourth pass of this date** (window **02:45 → 03:1x UTC**).

## 🟢 🆕 `P117-Q` — the five trends this pass can actually evidence, each with its channel named

| # | trend | evidence class | state |
|---|---|---|---|
| 1 | 🟢 **Purpose-built beats general-purpose, and procurement moves from TEACHER to DISTRICT** | converging: 4 US state bills + Schola Europaea all demand an *approved-tool* process | 🟢 **settled by convergence** |
| 2 | 🟢 **Copyleft dominates the platform layer; permissive lives in assessment + plumbing** | 🟢 **measured** — 20 platforms, licences read from trees (`P117-L`) | 🟢 **measured** |
| 3 | 🟡 **Governance lags usage badly** — near-universal adoption, most institutions without policy | aggregator blogs, no primary | 🟡 candidate |
| 4 | 🟡 **Faculty enthusiasm is DECLINING in North America while flat elsewhere** (76 %→67 % intent, US/CA) | one survey, regionally split | 🟡 candidate, 🟢 notable |
| 5 | 🟡 **Funding is consolidating** — EdTech VC $1 B in H1 2026, −26 % YoY | vendor report | 🟡 candidate |

🔵 **Trend 1 is the one worth building for, and it is the only one this pass can call settled
without a primary source — because it is settled by CONVERGENCE rather than by any single
claim. Georgia (governance framework), Florida (statewide standards), Maryland (evaluation
rubric), North Carolina (evaluation framework + public approved-tool list), Ohio (mandatory
district policy) and the European Schools network (approved tools, written rules, staff
guidance) all independently describe the same artefact. Six jurisdictions converging on one
deliverable is stronger evidence than any of the six.**

🔴 **Trend 4 deserves more attention than its candidate status suggests, because it cuts against
every vendor narrative on this page: if North American faculty INTENT is falling 9 points while
other regions hold steady, the 2026 North American sale is to ADMINISTRATORS and compliance
owners, not to enthusiastic instructors. 🟢 That matches trend 1's district-level procurement
shift exactly, from an unrelated source.**

## 🔴 🆕 `P117-R` — the counter-trend inside this KB, and it is the pass's real finding

🔵 **A trends page should record when the instrument changed, not only when the world did.**

🔴 **`api.github.com` has been recorded as blocked since p107. It answers through the MCP relay
while `curl` still gets `403` at CONNECT and `gh api` is repo-scope gated (`P117-A`). Nine
passes of workarounds were built around one transport's answer.** 🟢 **The first use of the
channel immediately found: a 31× star overstatement, a 1.7× understatement, 9 wrong licences in
14 rows, 5 non-canonical addresses and a foundation row that declares itself unmaintained.**

🔵 **The generalisable trend, stated for whoever reads this KB next: the binding constraint on
this knowledge base has not been what is true about education AI. It has been which channel
this KB could reach, and it mistook that for what was knowable.**

## 🟡 What this page searched and did NOT find — stated, not hidden

🔴 **No new APAC policy token.** The region's picture (China's MoE curriculum, India's Class-3
mandate from 2026-27, Singapore's Student Learning Space, Japan's deliberate caution) was
already held in full — saturation of holdings, not absence of activity.
🔴 **No primary source reachable for any 2026 market-size figure.** Two aggregators give
mutually inconsistent numbers ($12.3 B for 2026 vs ~$32 B by 2030 from ~$6 B in 2024); both are
marked **do not quote** in `intel/market.md` rather than averaged.
🔴 **`topic:education topic:llm` returns `total_count: 0` above 400★.** The topic pair is unused
on GitHub; the zero is a tagging artefact and must not be read as absence of work.
🔴 **No LATAM education-specific AI trend source.** A dedicated regional query returned
enterprise-AI, data-centre and IP-law material; the four LATAM items this pass holds are the
entire usable yield.

# Education — current trends

**Pass 116, 2026-10-11.** ⏱️ **Second pass of this date** (census window
**2026-10-11 02:18 UTC → 02:33 UTC**; p114 ran 23:54 on the 10th → 00:25 UTC on the 11th).

🟢 **Instrument this pass: `compose/code/p116-lock-agreement/` — `test_p116.sh`
**113 passed / 0 failed** (fully offline: real git repositories committed on disk and
served to the real `agree.sh` over `file://`, no mocks, no `api.github.com`);
`agree.sh` read **134 of 134** addresses, `rc=0` on every one, **zero unread**, plus
**two** control runs over the same 134.**

🔵 **On the pass number, stated because it affects how every cross-tab below reads:**
a SECOND instrument also numbered itself p115 — `compose/code/p115-region-evidence/`,
measuring regional placement and `Gap 403` — and it landed in the window 01:13–01:25 UTC,
while this pass's own work was in progress. **The two are independent reads of the same
shelf, not a sequence.** That pass holds the number 115 and the trend ids `T50`–`T52`;
this one is therefore **pass 116**, its rules are `P116-*` and its trends `T53`–`T55`.
This pass cross-tabulates against **p114**, which is the axis its question comes from, and
**does not incorporate the concurrent p115's regional channel** — it could not have,
because that channel was not on the shelf when `agree.sh` started.

🔵 **Tenth axis in ten passes, sixth read from the TREE. It answers the question p114
wrote into its own trend table and left open:** p114 published 34.5 % `full-reach` and
said what the figure still hid — *“whether the pinned versions are any good”*. Of that,
version currency and known vulnerabilities need a registry and an advisory feed, and
neither is on this channel (`P116-D`). But whether the lock and the manifest describe the
**same dependency set** is decidable from committed bytes — and it is the half with a hard
failure mode: **`npm ci` does not install a stale lock, it exits 1 and installs nothing.**

### 🟢 🆕 `T53` — trend: the tightening sequence breaks, and what breaks it is a defect class the first eight axes could not see

🔵 **Ten passes have now measured this shelf on ten independent axes. p114 published
the sequence and named a property of it: *"no axis has yet reversed the direction of the one
before it. Each has been a tightening."* That property ends this pass.**

| axis | pass | what the shelf looks like | what the figure hides |
|---|---|---|---|
| releases | p108 | pinnable | the pin may be from 2019 |
| liveness | p109 | alive | one person is keeping it alive |
| bench | p110 | 🔴 67.6 % one person | nobody can tell if a fork broke it |
| verification | p111 | 🔴 38.9 % `checked` | the check runs on GitHub's machines |
| closure | p112 | 🔴 36.1 % `pinned` | the lock may not reach the manifest |
| provider binding | p113 | parallel axis | — |
| reach | p114 | 🔴 34.5 % `full-reach` → 🟢 **34.8 % restated** | whether the pinned versions are any good |
| region evidence | p115 | measured concurrently, different axis | — (independent of this read) |
| 🟢 🆕 **agreement** | 🟢 **p115** | 🟢 **64 / 64 `agree`; 3 100 / 3 100 deps** | 🔴 **whether those versions are current or safe (`P116-D`)** |

🟢 **The shelf is clean on this axis, and the cleanliness is informative precisely because
the defect is invisible to the other eight.** A row can be tagged, alive,
bus-factor-survivable, CI-verified, dependency-closed, pinned AND reached and still fail the
first command a client team types. 🔵 **That failure mode is now checked and it is absent —
so the eight pessimistic figures above are not measuring a shelf that is sloppy in general.
They are measuring eight specific things that are missing, on a shelf whose maintainers keep
the files they DO commit internally consistent.** That is a meaningfully different reading of
p108–p114 than those passes could support on their own.

### 🔴 🆕 `T54` — trend: the supply-chain gate a studio would most naturally build reports false defects on the best repositories

🔴 **This is the pass's most transferable finding and it did not come from the shelf — it
came from getting the instrument wrong three times.** "Compare the manifest to the lock by
name" is the obvious gate, it is a dozen lines, and run naively it reports drift on
`PrairieLearn`, `oppia` and `canvas-lms` — three of the shelf's largest and best-maintained
rows — because of three mutually inconsistent ecosystem conventions:

| convention | the false finding it produces |
|---|---|
| yarn keys an aliased dependency under the **alias** | every aliased dep reads as missing |
| pnpm keys the same thing under its **target**, recording the alias only under `importers:` | the *opposite* parse is needed for the same fact |
| a workspace-local package is absent from the lock **by design** | monorepo-internal deps read as missing |

🔴 **The false positives are not randomly distributed: they concentrate on monorepos,
which means they concentrate on the mature, multi-package platforms a studio is most likely
to adopt.** 🔵 **A gate that flags Canvas and PrairieLearn on day one is a gate the client
turns off in week two**, and the trend worth naming is that supply-chain tooling bought or
built in 2026 should be evaluated against an aliased, workspace-using monorepo before it is
evaluated against anything else.

### 🔵 🆕 `T55` — trend: the undecidable half is where the risk actually sits

🔵 **Of 134 rows with a lock that reaches the root, only 64 can be checked for agreement.
The other 70 are python, maven, go and ruby at the root** — ecosystems with no committed
lockfile grammar to compare a manifest against.

🔴 **The overlap is the finding: the ecosystems p112 and p114 found WORST at pinning are
the same ones where agreement is undecidable.** python rows dominate both lists. So the two
halves of this shelf fail differently and neither failure is visible from the other half:
the npm/composer half is pinned, reached and internally consistent; the python/JVM half is
weakly pinned and **cannot be audited by this method at all**.

🔵 **For an engagement this means a single supply-chain gate is not enough.** The npm and
composer components can be gated on committed bytes. The python and JVM components need a
resolver actually run in a controlled environment, which is a different kind of check with a
different cost — and on this shelf it is the majority of rows.

### 🟢 🆕 `P116-P` — `Gap 404` CLOSED, and p114's sizing was exact

🔵 **p114 found that the anchored requirement-file rule — carried in TWO copies, p112's
`manifests.awk` and p114's `positions.awk` — refuses the prefixed half of its own
convention (`dev_requirements.txt`, `latest_requirements.txt`, `system_requirements.txt`).
It sized the gap (198 files seen, 8 missed, 5 rows affected, exactly ONE verdict),
declared it, and deliberately did not fix it, because `P237` forbids forking a shared
classifier.**

🟢 **Fixed where the rule lives.** [`lib/reqname.awk`](../compose/code/lib/reqname.awk)
now holds **one** definition, widened to
`^([a-z0-9._-]+[-_.])?requirements([-_.][a-z0-9._-]+)?\.txt$`, loaded by both passes with
a second `-f`. `lib/test_reqname.sh` — **22 passed / 0 failed** — pins every case,
including the `myrequirements.txt` exclusion that stops the prefix group swallowing any
word that merely ends in the literal string. Neither consumer regressed:
**`test_p114.sh` 98 / 0**, **`test_p112.sh` 109 / 0**.

| p114 figure | as published | 🆕 restated | delta |
|---|---|---|---|
| rows at `full-reach` | 102 (34.5 %) | 🟢 **103 (34.8 %)** | **+1** |
| lockable manifests | 2 135 | **2 143** | **+8** — the 8 missed files, exactly as sized |
| manifests reached | 1 625 (76.1 %) | **1 633 (76.2 %)** | +8 |
| manifests orphaned | 510 (23.9 %) | **510 (23.8 %)** | 🟢 **0** |
| rows whose ROOT manifest is orphaned | 88 | 🟢 **87** | **−1** |
| rows that moved | — | 🟢 **[`sdv-dev/sdv`](https://github.com/sdv-dev/sdv) `no-reach` → `full-reach`** | exactly one |

🔵 **The orphan count does not move at all — all 8 newly-visible files are pins that ADD
coverage, so numerator and denominator rise together.** That is the direction the widened
rule predicts in its own header, and it is why no row lost a verdict it held.

### 🔴 🆕 `Gap 406` — OPENED: there is a FOURTH npm lock flavour on this shelf, and it is sized at exactly one row

🔵 **`P116-I` widened this axis from one npm lock flavour to three. The shelf has
four.** Of the 70 rows this axis could not decide, **69** are rows whose root manifest is
in an ecosystem with no lock grammar here at all (python 28, `npm,py` 12, maven, go,
ruby). **The seventieth is not:**

| row | root tree | why undecided |
|---|---|---|
| [`mietiainvestigacion-creator/api-eduadapt`](https://github.com/mietiainvestigacion-creator/api-eduadapt) | `package.json`, **`bun.lock`**, `bunfig.toml` | 🔴 **`bun.lock` is a fourth npm lock flavour this axis does not read** |

🔵 **Sized, not guessed:** exactly **1 of 134** rows. The file is JSON-shaped — a
`workspaces` map keyed by path, each entry carrying its own `dependencies` — so it is
very likely parseable, which is precisely why it is **declared rather than parsed on a
hunch**: adding a grammar without a fixture and a control is how the three false
positives above were produced in the first place.

🔵 **Error direction:** one-way and benign. A flavour this axis cannot read makes a row
**undecidable**, never `agree` and never `drift`, so no published figure here is wrong
because of it — the decidable denominator is 64 rather than 65.

🔵 **How it ends:** a `bun.lock` grammar with its own fixtures in the suite, the census
re-run, and the decidable denominator restated from 64 to 65.

### 🔵 Regional: no story in the verdict, a real story in the coverage

🟢 **No region drifts — 9/9 North America, 7/7 EMEA, 4/4 APAC, 3/3 LATAM, 41/41
unplaced.** 🔴 **But North America and EMEA can be read on fewer than half their rows
(40.9 % and 41.2 %)**, because their rows are disproportionately the python and JVM
ecosystems `T55` describes. 🔵 **LATAM's 3/3 is a denominator of three, not a lead.** The
regional conclusion is a coverage statement, not a quality ranking, and the detail is in
`repos/trending.md`.

# Education — current trends

**Pass 115, 2026-10-11.** ⏱️ **Second pass of this date** (census window
**01:13 → 01:25 UTC**).

🟢 **Measured over **296 of 296** addresses, zero unread
(`compose/code/p115-region-evidence/`, `test_p115.sh` **193 passed / 0 failed**, fully
offline), with four controls re-derived from the same token snapshot.**

### 🟢 🆕 `T50` — placeability is INVERSELY related to project maturity, and this is now measured rather than suspected

🔵 **The nine `checked` foundational repositories on `repos/foundations.md` place **ZERO**
rows on region. The agent tier places **0 of 14**. The rows that DO place are small academic
repositories whose maintainer still uses a university address.**

| tier | rows examined | place at layer 0 |
|---|---|---|
| the nine `checked` foundations | 9 | 🔴 **0** |
| p114's named agent-side rows | 14 | 🔴 **0** |
| the eighteen platform rows | 18 | 🟡 **2** |
| 🟢 the whole shelf | 296 | 22 |

🟢 **The mechanism, and it is a deliberate choice by those projects rather than neglect:** a
project at the scale of `moodle.org`, `oppia.org`, `temporal.io`, `dspace.org` or
`huggingface.co` registers a generic or vanity TLD **because a country code in the domain of
a global project is a liability**. 🔴 **So the rows a studio is most likely to build on are
exactly the rows that will never tell it where they are built** — and any regional claim
about them is this KB's inference, which must be labelled as one.

🔵 **`T50` is a trend about the ARTEFACTS, not the market, and it is the first one on this
page in that class. It predicts that this gap will widen: as an education project succeeds it
migrates from `uni.edu` to `project.org`, which moves it from placeable to unplaceable.**

### 🟢 🆕 `T51` — the structured-metadata channel is being replaced by the AI-agent channel, and both are committed files

🔵 **Two observations from this pass's tree reads, which point the same way:**

🔴 **Only 175 of 296 rows commit a structured metadata file at the ROOT, and 82 commit none
anywhere.** The ecosystem's "declare yourself in a machine-readable file" layer —
`CITATION.cff`, `codemeta.json`, `.zenodo.json` — is thin on this shelf: **3 rows** carry a
typed `country:` field in a CFF, total.

🟢 **Meanwhile the newest platform row this KB has admitted in eleven passes,
[`jtylek/EpesiCRM`](https://github.com/jtylek/EpesiCRM) (MIT, last commit 2026-10-07), commits
`AGENTS.md`, `CLAUDE.md` and an `AI-shared/` directory at its root.** 🔵 **A vertical platform
being rewritten in the open with coding agents, with the agent instructions versioned beside
the code, is the shape of 2026 maintenance this KB has asserted in prose for several passes.
Here it is as a committed file at a named, verified address.**

🟡 **What to do with it: `AGENTS.md` / `CLAUDE.md` at a repository root is a cheap, structural
signal of how a project is maintained, it is as machine-readable as `CITATION.cff`, and
nothing in this KB measures it. Named here as a candidate axis rather than claimed as a
figure.**

### 🟢 🆕 `T52` — "from experimentation to governance" is now a DATED statutory deadline in a US state, not a theme

🔵 **1EdTech, HolonIQ and the OECD all described 2026 as the year AI in education shifts from
experimentation to governance, and this KB has held that as a theme for several passes. This
pass found it with dates attached:**

🟢 **North Carolina §7.39 of Session Law 2026-41 — effective 1 July 2026 — requires a DPI
model AI-use policy by **31 December 2026**, local board policies, a framework for evaluating
generative-AI educational tools, a **public list of approved tools**, and teacher AI
professional development by **30 June 2028**, with AI literacy entering the K-12
computer-science standards in **2028-29**.**

🔴 **Verification of the section's text is BLOCKED on this channel: `ncleg.gov` and
`dpi.nc.gov` are refused at the CONNECT layer, logged by host and timestamp in the proxy's own
ledger (`P115-S`, extending `P798`). Two independent secondary guides agree on every
particular. The item is published as `candidate · unverified-at-primary` with the exact URL
that would settle it.**

🔵 **Why it is a trend and not just a regulation: an "approved-tool list" plus an "evaluation
framework" is a procurement artefact, and a procurement artefact needs exactly the evidence
this KB has spent nine passes measuring — licence, dependency closure, lock reach, provider
binding, and now region. `T52` is the first trend on this page that the shelf's own axes were
already built for.**

### 🟡 `T47`–`T49` (p114) and the earlier trends: unchanged

🔵 **p115 read a different column and retired nothing.** 🟡 **One qualification it does add,
to every trend on this page that carries a region: the regional attribution of a trend
observed in REPOSITORIES now has a measured provenance — 22 rows from the repositories' own
root metadata, 59 from their READMEs, 93 from this KB's org record, and **182 of 296 with no
region at all**. A trend stated "in APAC" on the strength of this shelf is resting on 13 rows,
every one of them placed by the org map and none by the repositories themselves.**

# Education — current trends

**Pass 114, 2026-10-11.** ⏱️ **First pass of this date** (census window
**2026-10-10 23:54 → 2026-10-11 00:25 UTC**).

🔴 **The eight mandated searches produced ZERO new trend items for the TENTH consecutive
pass. 49 candidate tokens extracted, **49 of 49 already held** — this pass did not even
produce a claim that FAILED verification, which p112 did. The query set and the token
ledger are in `intel/market.md` under `P114-M`.**

🟢 **The pass's contribution is again a trend this KB can state because it MEASURED it:
the open-source education supply is not merely unpinned — the pinning it does have is
positioned where it does not help, and the published figure for it was an upper bound
that nobody had tested.**

### 🟢 🆕 `T47` — trend: every generation of supply-chain signal on this shelf has been retired by the next, and "has a lockfile" is the latest to go

🔵 **Eight passes have now measured this shelf on eight independent axes. Read as a
sequence they are one story: each signal a buyer would reasonably ask for turns out to
be satisfiable without the property it is supposed to evidence.**

| axis | pass | what the shelf looks like | what the figure hides |
|---|---|---|---|
| releases | p108 | pinnable | the pin may be from 2019 |
| liveness | p109 | alive | one person is keeping it alive |
| bench | p110 | 🔴 67.6 % one person | nobody can tell if a fork broke it |
| verification | p111 | 🔴 38.9 % `checked` | the check runs on GitHub's machines |
| closure | p112 | 🔴 36.1 % `pinned` | 🔴 **the lock may not reach the manifest** |
| provider binding | p113 | measured in parallel, different axis | — (independent of this read) |
| 🆕 **reach** | 🟢 **p114** | 🔴 **34.5 % `full-reach`; 76.1 % of manifests reached** | whether the pinned versions are any good |

🔵 **The sequence has a property worth naming: no axis has yet reversed the direction of
the one before it.** Each has been a tightening. That is weak evidence that the shelf is
genuinely in the state these figures describe rather than being measured badly — and
`P114-H` is the first time one pass has re-run its predecessor's exact rule to prove the
movement is the rule and not the week.

### 🔴 🆕 `T48` — trend: the repository root is where open-source education projects stop pinning

🔵 **This is the finding that generalises beyond this shelf, and it is the one to take
into a client conversation.** Across 296 addresses:

| | |
|---|---|
| lockable manifests | **2 135** |
| reached by a lock | 🟢 **1 625 (76.1 %)** |
| 🔴 orphaned | 🔴 **510 (23.9 %)** |
| rows whose **ROOT** manifest is orphaned | 🔴 **88 of 296** |
| of those, rows where **nothing** is reached | 🔴 **65** |

🔴 **Three quarters of the declared dependency surface on this shelf is reachable by a
lock, but on 88 repositories the single manifest a team installs from first is not.** The
shape recurs: a project pins the subtree it iterates on — the service, the front end, the
package it publishes — and leaves the top-level `pyproject.toml` or `setup.py` that
defines the project itself unpinned, because that file is the *library's* declaration and
the maintainers are not installing from it. That is defensible behaviour for a library
(`P112-G` carved the distinction out, and p114 keeps it). It is a problem the moment a
studio forks the repository and becomes the installer.

🔵 **python is where it concentrates: 86 of the orphan rows are python**, against 21 npm,
11 php, 6 gradle, 5 R, 5 dotnet, 4 ruby, 4 go, 1 swift. On an education-and-AI shelf
python is the dominant ecosystem, and it is also the ecosystem whose idiom —
`requirements.txt` maintained by hand — produces a pin that is positional rather than
generated.

### 🟡 🆕 `T49` — trend: the regional ranking on a supply-chain axis depends on the weighting, and nobody states the weighting

🔴 **North America reads 81.2 % on manifests and 36.1 % on repositories: second-best and
last on the same census.** One repository — `instructure/canvas-lms`, 596 manifests —
carries 59 % of the region's denominator. APAC's 92.3 % similarly rests on
`moodle/moodle` (63 of 91).

🔵 **The trend worth recording is not the ranking but the fragility of regional
supply-chain claims at these denominators.** Six LATAM rows and nine APAC rows carry a
lockable manifest. Any vendor report quoting a regional open-source "maturity" percentage
on a base like that is reporting one or two projects' engineering habits. This KB states
both figures, the concentration behind each, and the 192 rows it still cannot place —
see `repos/trending.md` and `intel/market.md` `P114-R`.

### 🔵 What p114 hands to p114

🔵 **A `full-reach` lock is still only as good as the versions inside it.** Seven axes
have now characterised the shelf's supply chain from the outside — refs, releases,
recency, authorship, CI, closure, reach — and **not one has opened a lockfile and read
what it pins.** `p437` / `p438` / `p442` (pre-reset) dated *resolved specifiers* against
the registries, which is the adjacent question, not this one. The open question is
narrower and now well-posed: of the 1 625 reached manifests, how old are the versions
their locks actually hold?

# Education — current trends

**Pass 113, 2026-10-10.** ⏱️ **Twenty-third pass of this date.**

🔴 **The eight mandated searches produced ZERO new trend items for the NINTH consecutive
pass. 33 tokens extracted, **32 of 33 already held**, and the single exception turned out
to be a UK procurement from August 2024 with its date stripped off (`P113-T`,
`intel/market.md`).** 🟢 **So the trends this pass adds are DERIVED from a 296-address
census, not read off a roundup — which is the only kind of trend this base can still
produce until `Gap 402`'s query set is replaced.**

## 🟢 `T44` — the sovereignty pitch finally has a number, and the number favours EMEA

🟢 **Measured: of the 87 shelf rows that bind a model at all, **67 (77.0 %) can be pointed
at a model the client controls** and 20 cannot. By placed region, EMEA leads at 7 of 10
model-bearing rows, with **five declaring a LOCAL inference runtime** — more local rows in
absolute terms than North America, on a smaller slice of the shelf.**

🔵 **Why this is a trend and not a statistic: it inverts which region gets the
sovereignty conversation.** 🔴 **The EU AI Act puts education systems in the high-risk
tier, and the standard reading is that EMEA buyers face a compliance BURDEN. The supply
says the opposite — the EMEA slice of this shelf is the slice that can be stood up without
egress at all, so for EMEA the pitch is *"here is the stack that already runs inside your
estate"*, not *"here is how we will make a hosted stack compliant"*.**

🔴 **And the one exception is the sharpest row in this base: `opetushallitus/ehoks` — the
Finnish National Agency for Education's personal-competence-plan service, EUPL-licensed
public infrastructure — declares `bedrockruntime`, `bedrock` and `bedrockagentruntime` in
its `pom.xml`. VERIFIED against the payload.** 🟢 **A national public education service
with a US hosted model layer, under a licence (EUPL) whose reciprocity makes a contributed
provider abstraction flow back automatically. That is a named, scoped, fundable
deliverable, not a defect to point at.**

🟡 **What would refute `T44`:** a count of the 193 rows `Gap 403` leaves unplaced that
moved EMEA's share below North America's — the unplaced remainder holds 50 of the 67
controllable rows, so the regional ordering is the least robust part of this trend and the
next pass can overturn it cheaply by extending `orgs.region.tsv`.

## 🔴 `T45` — "reproducible" and "usable" have come apart, and the gap is the whole engagement

🔵 **Four passes of axes, read as a ladder:**

| the shelf can… | rows of 296 | share |
|---|---|---|
| tell you when you broke it (p111 `checked`) | 115 | 38.9 % |
| …and resolve to the same bytes twice (p112 `pinned`) | 63 | 21.3 % |
| 🟢 **…and talk to a model you own (p113 controllable)** | 🟢 **17** | 🟢 **5.7 %** |
| 🔴 …and talk only to one vendor's endpoint | 🔴 **9** | 🔴 **3.0 %** |

🔴 **Each axis roughly halves the shelf, and the third one halves it again. `oppia/oppia`
is the case to carry into a conversation: Apache-2.0, `broad` bench, 2 959 test files,
`pinned`, `checked` — best-in-class on every axis measured before this pass, and
single-vendor on this one.** 🟢 **The trend for a studio is that "pick good open source"
has stopped being a sufficient technical answer: the model-portability layer is now the
differentiating line item, and 9 rows show it is needed exactly where the repository
quality is highest.**

🟡 **What would refute `T45`:** reading program text instead of declarations. `local` and
`broker` are LOWER bounds here (`P113-I`), so a code-level read could only move rows
UPWARD — if it moved enough of the 209 `no-model` rows into `local`, the 5.7 % would rise.
🟢 **That is a bounded, offline, named follow-up and the honest statement of this trend's
weakness.**

## 🔴 `T46` — the LMS tier declares no model at all, and that is the opportunity rather than the problem

🟢 **Read in FULL this pass, uncapped: `instructure/canvas-lms` (551 declarations),
`sakaiproject/sakai` (498), `moodle/moodle` (64), `kuali/rice`, `leemonade/leemons` — every
one `no-model`. 79 of 94 platform addresses on `verticals/solutions.md` likewise.**

🔵 **Three findings now meet at the same seam, from three different instruments:**

- `T30` / `P1033` — the copyleft frontier IS the plugin tree (143 of 143 Moodle packages GPL-3)
- `T34` — Moodle DEFINED `moodle-aiprovider` / `moodle-aiplacement` and **zero packages exist for either**
- 🟢 **`T46` — and the platforms themselves carry no model binding to inherit**

🟢 **So the model layer of an LMS engagement is greenfield in all three senses at once:
nothing published against the extension point, nothing declared in the platform, nothing
to inherit.** 🔴 **And `T34`'s rule still decides the licence — INSIDE Moodle it is GPL-3,
BESIDE it it keeps the licence you choose — which makes *where it mounts* the first
commercial decision of the engagement and the one that cannot be revisited later.**

🟡 **What would refute `T46`:** a model declaration inside any of the five platforms'
trees. 🟢 **The claim is now falsifiable cheaply and precisely, because the read was
uncapped and the per-row declaration counts are published; the instrument's own cap was
caught truncating these exact five rows TWICE before the figure was published (`P113-D`).**

## 🟡 `P113-U` — on an MCP-and-skills shelf, "no model declared" is usually correct architecture

🔵 **35 of the 209 `no-model` rows have a README that names a model. That looked like a
prose-versus-tree gap; 23 of the 35 are not one:**

| | rows | reading |
|---|---|---|
| 🟢 host-delegated by design — MCP servers, skill packs, lists, courses | 20 | 🟢 an MCP server does not choose the model; its host does |
| 🟡 Moodle plugins — binding lives in the LMS's AI subsystem config | 3 | 🟡 correct for the same reason, one layer up (`T34`) |
| 🔴 a genuine gap — README sells a model, no declaration names one | 🔴 **12** | 🔴 the README is the sales document and the tree does not support it |

🟢 **The trend worth naming: the MCP and skill-pack layer has made "which model" a
DEPLOYMENT-time choice rather than a repository-time one for 20 rows of this shelf.**
🔵 **That is a genuine architectural shift and it is good news for portability — but it
also means a buyer evaluating these repositories on "which model does it use" is asking a
question the repository is deliberately refusing to answer.**

## Instrument note carried forward

🟢 **Anonymous `git fetch` / `git ls-remote` and `raw.githubusercontent.com` discriminate;
`curl` on `github.com` and `api.github.com` return 403 for real and invented slugs alike
and must not be used.** 🔵 **`api.github.com` = 403 for the nineteenth consecutive pass.**

🟢 🆕 **p113 adds a channel detail worth keeping: a depth-1 blob-filtered fetch plus ONE
batched lazy blob fetch per repository reads 296 trees and their declaration bodies in
7 m 10 s with zero failures. The batch stream must be parsed BY BYTE COUNT, not by the
40-hex header pattern p111/p112 used — a payload whose own content holds a header-shaped
line desynchronises the pattern-based reader, and a payload with no trailing newline
desynchronises it too (`P113-E`, `P113-M`; `learningequality/kolibri` reported 474 stray
lines until that was fixed).**

---

# Education — current trends

**Pass 112, 2026-10-10.** ⏱️ **Twenty-second pass of this date.**

🔴 **The eight mandated searches produced effectively ZERO new trend items for the EIGHTH
consecutive pass. 26 tokens extracted, **25 of 26 already held**, and the single exception
FAILED its own verification search (`P112-P`).**

🟢 **The pass's contribution is again a trend this KB can state because it MEASURED it:
the open-source education supply is not merely unverifiable — the verified part of it is
not reproducible, and the two defects do not overlap the way a buyer would assume.**

### 🟢 🆕 `T41` — trend: "has CI" has become a lagging indicator of buildability

🔵 **Six passes have now measured this shelf on six independent axes. Read as a sequence
they are a story of each generation of signal being retired by the next:**

| axis | pass | what the shelf looks like | what the figure hides |
|---|---|---|---|
| releases | p108 | pinnable | the pin may be from 2019 |
| liveness | p109 | alive | one person is keeping it alive |
| bench | p110 | 🔴 67.6 % one person | nobody can tell if a fork broke it |
| verification | p111 | 🔴 38.9 % `checked` | 🔴 **the check runs on GitHub's machines** |
| 🆕 closure | 🟢 **p112** | 🔴 **36.1 % `pinned`** | whether the pinned versions are any good |
| 🆕 **both** | 🟢 **p111 ∧ p112** | 🔴 **21.3 % verifiable AND reproducible** | — |

🔴 **The trend to carry into a client conversation: in open-source education, a green CI
badge now certifies LESS than a buyer assumes. 115 of 296 addresses have a suite, a live
runner and a `pull_request` trigger; **52 of those 115 cannot reproduce the environment
the suite was green against**. The badge is a statement about a hosted pipeline, and the
engagement happens somewhere else.**

🟢 **The honest size of the buildable base behind a category growing at ~40 % a year is
**63 of 296 addresses (21.3 %)**, and the staffed-and-verifiable-and-reproducible core is
**12 repositories**.**

### 🟢 🆕 `T42` — trend: the defect is polyglot count, and it is a sector characteristic rather than a discipline problem

🔵 **Pinning falls monotonically with the number of lockable ecosystems in a tree — 54.5 %
at one ecosystem (n=134), 42.3 % at two (n=78), 12.5 % at three (n=8), zero at five and
nine. Mean ecosystems rise with bench size (`broad` 1.64 → `solo` 1.30), which is why
p110's bands appear to invert on this axis.**

🔴 **This matters as a TREND because education software is structurally polyglot: an LMS
is a PHP or Ruby monolith with a JavaScript front end; a learning-analytics stack is
Python plus JVM; a mobile learning app adds Gradle. The sector's architecture produces
two- and three-ecosystem trees as a matter of course, and each added ecosystem is another
lockfile someone has to own. The unreproducibility on this shelf is therefore not mostly
carelessness — it is the predictable arithmetic of the sector's own shape.**

🟢 **The commercial consequence is a pricing rule rather than a warning: count the
lockable ecosystems in a candidate repository before quoting. One is routine, two is
where pinning work actually lands, three or more should be priced explicitly.**

### 🔴 🆕 `T43` — trend: public-sector education code is now measured on three axes, and the three sets are disjoint

| body | region | writes suites | wires CI | pins deps |
|---|---|---|---|---|
| `opetushallitus` (FI) | EMEA | 🟢 yes (70–1 428 each) | 🔴 **1 of 8** | 🟢 **8 of 8** |
| `EducationalTestingService` (US) | North America | 🟢 yes (130–8 347) | 🔴 **0 of 3 PR-gated** | 🔴 **0 of 3** |
| `aiverify-foundation` (SG) | APAC | 🟢 yes | 🟢 **yes** | 🟢 **yes** |
| `portabilis` (BR) | LATAM | 🟢 yes | 🟢 yes | 🟡 1 of 3 |
| `project-sunbird` (IN) | APAC | 🟢 yes | 🟡 2 of 3 | 🟡 maven, resolved not locked |
| `Apereo-Learning-Analytics-Initiative` ※ | EMEA? | 🟢 yes (3–46) | 🔴 3 dead (Travis) | 🟡 maven, resolved not locked |

🟢 **One body on this shelf is in all three sets: Singapore's `aiverify-foundation`,
Apache-2.0. For an AI-assurance or assessment engagement in APAC that is the single
lowest-friction public-sector starting point this KB holds, and it is a statement about
engineering practice rather than about market size.**

🔴 **The trend worth stating to a public-sector buyer: national education agencies produce
code whose WEAKNESSES ARE INSTITUTION-SPECIFIC AND PREDICTABLE, not sector-wide. Finland
pins everything and wires nothing. ETS wires nothing and pins nothing while shipping the
largest suite on the shelf. Those are different procurement risks with different prices,
and a single "is this open-source project any good" question cannot distinguish them.**

### 🔴 🆕 `P112-P` — the eighth zero, and the one token that failed verification

🔵 **Eight queries were run in extended mode (four global, four regional). 26 candidate
tokens were extracted and checked one at a time against the live pages of this KB. 25 are
already held: the `134`-bills/`31`-states count, California `AB 1159`, Idaho `SB 1227`,
the Oklahoma and Maryland human-oversight duties, `H.R. 8747`, Ohio's July-2026 district
policy mandate, the NYC moratorium, Katy ISD, Microsoft's Education AI Toolkit, the AASA
*STUDENTS FIRST* framework, the `36 %`/`$3.68 B` NA share, the EU AI Act omnibus and its
`2 December 2027` date, Annex III, the Apply AI Alliance, Korea's Framework Act,
Vietnam's Law `134/2025/QH15`, `AI Verify`, the Ipsos Education Monitor, the UNESCO
IESALC `87 %`/`26 %` figures, the Digital Education Council's `7,319`-faculty survey, the
UNESCO LAC Observatory, `CENIA`, `Ceibal`, Colombia's `CONPES 4144` and the Council of
Europe Framework Convention.**

🔴 **The single exception was a market report's claim that **Baidu's ERNIE has entered the
Indonesian and Thai education markets through partnerships**. It was given its own
dedicated verification search. **No corroborating report exists** — the search surfaced an
Indonesia–Thailand education MoU with no Baidu involvement, a Baidu Education company
profile covering China only, and the 2023 ERNIE Bot launch release. It is therefore
recorded here as a FAILED VERIFICATION and is NOT published as a finding anywhere on this
KB.**

🟢 **The standing instruction is confirmed for an eighth pass: the unexhausted channel in
this environment is measurement of the shelf this KB already holds, not search.**

---

**Prior passes on this page follow, newest first.**

# Education — current trends

**Pass 111, 2026-10-10.** ⏱️ **Twenty-first pass of this date.**

🔴 **The eight mandated searches produced effectively ZERO new trend items for the
seventh consecutive pass. 24 tokens extracted, 23 of 24 held, and the exception is a
corroborating detail on a held player (`P111-R`, `intel/market.md`).**

🟢 **The pass's contribution is a trend this KB can state because it MEASURED it rather
than read it: the open-source education supply has a verification problem, and its shape
is regional.**

### 🟢 🆕 `P111-AB` — trend: the category's open-source supply is maintained but not verifiable

🔵 **Five passes have now measured this shelf on five independent axes. Read together
they describe a supply side that looks much healthier from the outside than it is from
the inside:**

| axis | pass | what the shelf looks like |
|---|---|---|
| releases | p108 | pinnable — most rows cut tags |
| liveness | p109 | alive — most rows committed recently |
| bench | p110 | 🔴 **67.6 % is one person** |
| 🆕 verification | p111 | 🔴 **only 38.9 % can tell you when you broke it** |

🔴 **The trend worth carrying into a client conversation: in open-source education the
commit graph and the release ladder are both LAGGING indicators of whether a project can
be adopted. Activity is abundant and cheap; a bench and a PR-gated suite are neither.
38.9 % `checked` across 296 addresses, and 9 to 12 repositories with both a real bench
and a real suite, is the honest size of the buildable base behind a category growing at
~40 % a year.**

### 🔴 🆕 `P111-AC` — trend: public-sector education code is well tested and badly wired

🔵 **This is the most actionable pattern p111 found, and it is a public-sector pattern
specifically.**

| body | region | repos on shelf | suites | verdict |
|---|---|---|---|---|
| `opetushallitus` (Finnish National Agency for Education) | EMEA | 8 | 🟢 70 – 1 428 tests each | 🔴 **7 of 8 `partial`** |
| Apereo Learning Analytics Initiative | EMEA | 6 | 🟢 3 – 46 tests | 🔴 **3 `fossil-ci` (Travis), 2 `tests-only`, 1 `bare`** |
| `EducationalTestingService` | North America | 3 | 🟢 130 – **8 347** tests | 🔴 **3 of 3 `partial`, none PR-triggered** |
| `aiverify-foundation` (Singapore) | APAC | 3 | 🟢 35 – 190 tests | 🟢 **3 of 3 `checked`** |
| `portabilis` (Brazil) | LATAM | 3 | 🟢 166 – 616 tests | 🟢 **3 of 3 `checked`** |
| `project-sunbird` (India) | APAC | 3 | 🟢 73 – 250 tests | 🟡 **2 `checked`, 1 `partial` (144 CI configs)** |

🔴 **The public bodies that WRITE tests and the public bodies that WIRE them are
different sets, and the split is not along a development-maturity line: Finland's agency
ships eight repositories with real suites and leaves seven of them unreachable from a
pull request, while Brazil's `portabilis` and Singapore's `aiverify-foundation` are
perfect on this axis.**

🟢 **The consultable trend: "we have tests" and "a contributor's change is tested" have
decoupled in public-sector education software. For a studio this is the difference
between a fixed-price engagement and a discovery phase, and it is measurable from outside
the client's walls before a contract is signed — which is the part worth selling.**

### 🔵 🆕 `P111-AD` — trend: Travis is a dating mechanism for abandoned education code

🔵 **Seven rows on this shelf are `fossil-ci`: a committed test suite whose only CI is a
service that no longer runs free open-source builds.**

🔴 **[`elmsln/elmsln`](https://github.com/elmsln/elmsln) is the extreme case — **1 996
test files and 34 Travis configuration files**, a pipeline investment larger than most
`checked` rows on this shelf, and not one of those configs can execute. Three Apereo LAI
repos and [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (306 tests)
are the same shape.**

🟢 **Because the free tier ended in 2021, `.travis.yml` as the ONLY CI is a reliable date
stamp: it says the project's last serious infrastructure work predates that. p109 reached
"graveyard" for the Apereo LAI org from commit dates; p111 reaches it from CI vendor
choice. Two independent channels agreeing is worth more than either, and the second one
is readable in a single file.**

### 🔴 🆕 `P111-AE` — the methodological trend: this pass's own biggest error pointed the WRONG WAY

🔵 **`P111-I`: the first draft of this instrument piped the CI body into `grep -q` under
`set -o pipefail`. `grep` exits at the first match, the writer takes `SIGPIPE`, and
`pipefail` makes that the pipeline's status — **so a signal that matches EARLY reads as
ABSENT**.**

🔴 **Measured, not reasoned about: [`oppia/oppia`](https://github.com/oppia/oppia)
contains `pull_request` 39 times, first in the opening workflow. The piped form reported
`ci_on_pr=0`, and the runner probe — whose term appears LATE in the same bytes —
reported `1`. The draft graded one of the best-tested repositories on this shelf
`partial`.**

🟢 **The transferable half: a measurement bug that is silent AND directionally biased AND
worst where the signal is strongest will survive casual review, because the rows it
corrupts are the rows a reviewer is least suspicious of. That is the third time in five
passes that this KB's own instrument carried a bias pointing at its best rows —
`P110-A` (merge commits made healthy repos read concentrated) and `P111-S` (substring
`test` matching misses `spec/`, so Rails suites read half-size) are the other two.**

🔵 **And once this pass, one of this KB's own documented traps caught its author: an
edit to `intel/market.md` matched the string `## Opportunities by region` inside a PROSE
sentence elsewhere on the page and cut live p110 content. **The pass-104 banner on that
same file records the identical trap** — "line 102 was a broken prose line whose stray
backtick made it match `^## Opportunities by region`, so a compiler reading headings saw
TWO region blocks". The edit was reverted from git and redone with line-exact anchors
(`^## Opportunities by region$`), which is the fix in both directions: the trap is that
the heading text is also ordinary prose, so neither a reader nor a writer may match it
loosely.**

🟢 **One standing gate finding was resolved as a side effect, and the cause is worth
recording: pass 104 asserted the block should have "exactly four `###` region children",
while `p383-region-heading-gate` validates against the CLOSED FIVE-VALUE vocabulary and
so reported `P383-MISSING-REGION: Global` from then until now. p111 has genuine
Global-scope content — the 203 shelf rows it could not place — so `### Global` now
exists and carries it. The gate reports **total 0** across all eight pages, which it did
not at the start of this pass.**

---


**Pass 110, 2026-10-10.** ⏱️ **Twentieth pass of this date.**

🔴 **The eight mandated searches produced ZERO new trend items for the sixth consecutive
pass — and this pass closes the question of why from the remaining side (`P110-L`).**

### 🔴 🆕 `P110-L` — the query set is exhausted in BOTH search modes, so the zero is now mode-independent

🟢 **All eight mandated searches ran: four global, one each for North America, EMEA,
APAC, LATAM.** 🔵 **p109 ran the same eight in **extended** mode — a deeper, fresher,
several-times costlier channel — and got zero new items. p110 ran them in **standard**
mode and got zero new items.**

🔴 **21 candidate tokens were extracted and checked one at a time against every page of
this KB. **21 of 21 are already held**:**

| token | where it came from | status |
|---|---|---|
| `IESALC`, `Digital Education Council`, Tec de Monterrey | LATAM query | 🔴 held |
| `73.5 %` (teaching), `92 %` (students), `79 %` (faculty), `26 %` (formal frameworks) | LATAM query | 🔴 held |
| `ILIA` index, `ANUIES`, Chile National AI Policy | LATAM query | 🔴 held |
| Gates Foundation + Carnegie Mellon `$55 M`, the `$169 M` commitment, Colorado/Texas | North America query | 🔴 held |
| `LearnUpon`, `Pearson`/TCS, `Brent Thomas` (OpenAI ANZ) | APAC query | 🔴 held |
| EU AI Act education = high-risk | EMEA query | 🔴 held |
| `ai-engineering-from-scratch`, `ai-agents-for-beginners`, `agents-from-scratch`, `Hermes` | global queries | 🔴 held |

🔵 **`P109-A` showed the expensive channel returns the same zero as the cheap one. This
pass shows the cheap channel returns the same zero as the expensive one. The two
together retire the competing explanation entirely: the result is a property of the
QUERY SET, not of search depth, and not of this pass's budget.**

🟢 **Standing instruction, CONFIRMED rather than merely repeated: a future pass should
not spend its budget re-running these eight queries expecting novelty. Every pass since
p106 that produced a finding produced it by MEASURING the shelf this KB already holds.**

### 🔴 🆕 `P110-P` — the trend this pass found is in the shelf, not in the news

🔵 **The open-source education stack is consolidating onto a very narrow institutional
base, and the measurement is new this pass:**

🔴 **Of 296 addresses this KB tracks, **200 (67.6 %) are `solo`** — one author holds more
than half the recent commit window — and **49 (16.6 %) have exactly one human in the
window**. Only **11 (3.7 %)** are both `broad` (≥ 6 authors) and `fresh`.**

🟢 **Read against the market numbers this file already carries — AI-in-education at
roughly $9.6–10.6 B in 2026 on a ~40 % CAGR — the gap is the finding: capital is
compounding at 40 % a year on a buildable open-source base of eleven repositories with
a real bench. That asymmetry is a sourcing risk for every vendor in the category, and it
is not visible from any market report.**

### 🟡 🆕 `P110-K` — "actively maintained" has been doing work it cannot do

| p109 band | rows | `solo` | share |
|---|---|---|---|
| 🟢 fresh | 144 | 84 | 🟡 **58 %** |
| 🟢 active | 34 | 27 | 🔴 79 % |
| 🟡 slowing | 52 | 39 | 🔴 75 % |
| 🔴 dormant | 18 | 14 | 🔴 78 % |
| 🔴 abandoned | 48 | 36 | 🔴 75 % |

🔴 **Freshness buys ~17–21 points of breadth and nothing more. 58 % of the repos that
committed this month are still one person.** 🔵 **So "actively maintained", the phrase
every due-diligence checklist in this category ends on, is close to uninformative about
the risk it is used to rule out.**

### 🟢 Trends carried forward unchanged from p109 and earlier

🔵 **This pass revised no prior trend. The eight trends this file carries — agent-native
tutoring, curriculum-standard machine-readability, the MCP gate into the LMS, rubric
automation, proctoring reach, the L&D/corporate buyer, sovereign-AI procurement in
education, and offline-first delivery — are unchanged, with their prior evidence.**

# Education — current trends

**Pass 109, 2026-10-10.** ⏱️ **Nineteenth pass of this date.** 🟢 **Two trends added, both
from the supply side and both measured first-hand over 296 of 296 shelf addresses
(`compose/code/p109-freshness/`, `test_p109.sh` 32 passed / 0 failed).** 🔴 **The eight
mandated searches added nothing — see `P109-A`, and note that this pass ran them in
extended mode, so that zero now carries information it did not before.**

## 🔴 `T38` — the open-source education shelf is smaller than any previous axis showed: **40 %**, not 57 %, and not 100 %

🟢 **Three axes now exist, and only the intersection is usable:**

```
                     pinnable (p108)    SHA-only (p108)
  fresh    <= 30 d         99                 45
  active   31- 90 d        20                 14
  slowing  91-365 d        25                 27
  dormant   1-  2 y         7                 11
  abandoned  > 2 y         17                 31
                          ---                ---
                          168                128     = 296
```

🔴 **p107 implied the shelf was 296 rows. p108 narrowed it to the 168 that can be
version-pinned. p109 narrows it again: **119 of 296 (40.2 %)** are both pinnable AND still
worked on.**

🔴 **The decisive number is that **24 of p108's 168 pinnable rows (14.3 %) have not been
touched in over a year**, and 17 of those in over two.** 🟢 **Those rows score clean on
every axis this KB had before today — permissive, released, pinnable — and two of them
were on the live recommendation page.** 🔵 **So this is not a refinement of p108; it is the
discovery that p108's axis is insufficient on its own in a specific, nameable way.**

🟡 **The mirror quadrant matters as much: **45 rows are fresh with no version to pin**.
Motion without shipping. Vendoring at a SHA and owning the upgrade path.**

🟢 **The two rows that prove why both axes are required, side by side:**

| repo | tags | pinnable? | alive? |
|---|---|---|---|
| `kuali/rice` | ECL-2.0, `rice-2.6.0` | 🟢 **yes** | 🔴 **3 433 d dead** |
| `opetushallitus/valtionavustus` | 4 468 tags, never a release | 🔴 **no** | 🟢 **0 d — committed today** |

🔵 **Either axis alone gets one of these exactly backwards. An engagement plan needs both
columns or it will reach for the wrong one.**

## 🟡 `T39` — the health of the open education stack is REGIONAL, and the standing assumption about which region is strong is inverted

🔵 **This KB has carried, since roughly pass 93, a working assumption that LATAM is the
thin region and North America the deep one, and `intel/market.md` has repeatedly recorded
LATAM as returning negatives.** 🔴 **On the liveness axis the ordering reverses, and it is
not marginal.**

```
EMEA    strongest.  opetushallitus 8/8 fresh (0-4 d); OpenOLAT 1 d; Artemis 0 d.
                    One casualty, and it is a loud one: the European Commission's own
                    european-digital-credentials, 981 d abandoned.
LATAM   second.     portabilis i-educar/i-diario 1-8 d; bncc-dev 14-60 d; academico 3 d;
                    chamilo 0 d. One casualty: mumuki (Argentina), 1 380 d.
APAC    mixed.      project-sunbird knowledge-platform 10 d but sunbird-devops 1 263 d
                    abandoned; Qwen OpenRS 219 d slowing.
N.AM    weakest.    Apereo LAI 6/6 abandoned (2 406-4 330 d); adlnet 4/5 abandoned
                    (3 273-4 233 d); ETS 3/3 dormant (627-652 d); kuali/rice,
                    Jasig/SSP, LearningLocker, IMSGlobal/caliper-spec all abandoned.
                    Live: CAHLR 1-10 d, ed-fi-alliance-oss 32-43 d, 1EdTech 2 d.
```

🔵 **The reading is not "North America does less education software" — it plainly does
more. It is that **North America's open education stack is OLDER**, so more of it has
already completed its lifecycle: SCORM, xAPI, Caliper, OpenLRS, Kuali and Apereo are
2000s–2010s institutional consortium projects whose funding ended.** 🟢 **The newer
national stacks — Finland, Brazil, India — are live because they are current government
programmes with current budgets.**

🔴 **Commercially this inverts a default instinct. In a North America engagement the
mature-looking standards-and-analytics layer is largely unmaintained, and the work is
implementing specifications rather than adopting implementations. In EMEA and LATAM there
are live national codebases to integrate with.** 🔵 **Stated as a measurement of 296
repositories, not as a claim about regional capability, and it is a supply-side figure
only — it says nothing about budget, which `intel/market.md` sizes separately.**

## 🟡 `T40` — `Gap 379`'s stall is asymmetric, and the asymmetry is geographic

🔵 **The rubric↔curriculum bind has been this KB's flagship open pattern for twelve
passes. Liveness splits it along its publisher boundary:**

```
RUBRIC half   (China + US academic)      CURRICULUM half  (Brazil, bncc-dev)
  OpenRS        219 d  slowing             bncc-pacotes    14 d  fresh
  rubricbench   221 d  slowing             bncc-dados      60 d  active
  OpenRubrics   109 d  slowing             bncc-benchmark  21 d  fresh
```

🔴 **Every rubric layer is 3.5–7 months cold; every curriculum layer is current.**
🟢 **That changes the engagement plan rather than just the risk note: the BNCC side can be
consumed as a live dependency, the rubric side must be vendored and owned.** 🔵 **It is
also a second instance of `T39` — the live half is LATAM-published.**

---

# Education — current trends

**Pass 108, 2026-10-10.** ⏱️ **Eighteenth pass of this date.** 🟢 **Two trends added: one
from the demand side (a survey, EMEA) and one from the supply side (a census, global).**

## 🟢 `T36` — teachers have adopted AI and rejected the general-purpose kind, and they say so in the same survey

🔵 **Source: Sanoma Learning *European Teacher Survey 2026*, >20 000 teachers, 14
countries, fieldwork by GfK/NIQ, published 24 September 2026. Full figures in
`intel/market.md`.**

```
teachers using AI                                63%   (was 49% in the 2023-25 waves)
believe GENERAL-PURPOSE AI improves outcomes     16%
want tools PURPOSE-BUILT for education        75-93%
```

🔴 **These three numbers in one sample are the trend.** 🟢 **Adoption is no longer the
question in EMEA; fitness is.** 🔵 **A 47-point gap between "I use it" and "it helps my
students learn" is a market telling a vendor exactly what to build, and the thing it
names — education-specific rather than adapted-general — is the definition of a vertical
engagement.**

🔵 **Corroboration across regions, from items this KB already holds:** LATAM's Digital
Education Council survey finds **79 %** faculty use but **88 %** describing their own
engagement as minimal-to-moderate, with the **lowest** uptake in assessment; UNESCO
IESALC finds **87 %** of institutions using AI but only **26 %** holding a formal
strategy. 🟢 **Three independent channels, three regions, one shape: wide shallow
adoption, thin institutional depth.** 🔴 **The pattern is now cross-regional enough that
it should be treated as the baseline assumption of an education engagement rather than a
finding about any one market.**

## 🔴 `T37` — the open-source education shelf cannot be version-pinned as often as it appears, and tag counts hide which way

🟢 **Measured over 296 of 296 distinct shelf addresses, zero unread
(`compose/code/p108-release-identity/`):**

```
semver     159  53.7%   pin a version
prefixed     9   3.0%   pin a version (under a project prefix)
stamp       15   5.1%   NO version exists  <- 4 of the 5 most-tagged repos on the shelf
none       113  38.2%   NO version exists
                        ------------------------------------------------
                        version-pinnable 168 (56.8%) / SHA-only 128 (43.2%)
```

🔴 **`T35` (pass 107) read this axis as a release *ladder* and binned repos by tag count.
`T37` supersedes that reading.** 🔵 **Tag count and release discipline are not merely
imperfectly correlated — on this shelf they invert at the top.** 🟢 **The four
`opetushallitus` repositories hold **4 468**, **4 225**, **1 134** and **726** tags, more
than any other addresses measured, and not one has ever cut a versioned release: those
refs are CI deploy stamps.** 🔵 **Meanwhile `kolibri`, with 16 tags, is clean semver at
`v0.19.5`.**

🟢 **Why it is a trend and not a measurement artefact:** 🔵 **the stamp pattern clusters in
**government-operated** education infrastructure (Finland's national agency), where the
deployment pipeline *is* the release process and a public version number serves no
internal purpose. 🔴 **As more state education stacks open their source — a direction
every regional section of `intel/market.md` documents — the share of the shelf that is
real, production, nationally-deployed AND unversionable will grow.** 🟢 **A 2026-era
education integrator needs a SHA-pinning and change-detection practice, not just a
dependency file.**

---


# Education — current trends

**Pass 107, 2026-10-10.** ⏱️ **Seventeenth pass of this date.** 🟢 **Two trends added, both from
measurement; the eight mandated searches produced no new item and that negative is stated in
`agents/trending.md` rather than left as silence.**

## 🔴 `T35` — the open-source education shelf is **permissive at the licence layer and unreleased at the supply layer**, and only one of those has ever been measured

🟢 **Measured this pass over **299 of 299** shelf addresses, every one read, zero unread
(`compose/code/p107-git-lane-census/`):**

```
0 tags — UNRELEASED   114   38.1%        25–99  — mature       40   13.4%
1–4    — nascent       37   12.4%        100+   — industrial   63   21.1%
5–24   — shipping      45   15.1%
```

🔴 **38 % of what this KB offers a client cannot be pinned to a version.** 🔵 **This is not a licence
problem and the licence work was not wrong — `P107-D`: a licence probe answers *may I use it*, a ref
probe answers *can I pin it*, and 107 passes asked only the first.**

🔴 **The trend bites hardest exactly where the industry is newest.** The agentic education layer —
rubric judges, MCP sidecars, tutor orchestration — is the youngest code on the shelf and therefore
the least released: **`Qwen-Applications/OpenRS`, `wanghaoyu0408/OpenRubrics`, `planepig/rubricbench`,
`bncc-dev/bncc-pacotes`, `a2br/moodle-mcp`, `fwu-de/mem-mcp` are all at 0 tags.** 🟡 **Meanwhile the
platforms underneath them are industrially released (Canvas 34 029, Open edX 5 896, Moodle 591).**

**Signal**: 🟢 **The 2026 integration risk in education AI is not model quality or licence
compatibility. It is that the agent layer is pre-release code sitting on top of
release-engineered platforms** — so the seam carries all of the version risk. 🔵 **That is what
`P107-A` in `compose/patterns.md` prices.**

## 🟢 `T36` — the metadata an API withholds is mostly available from the git protocol, and that is a durable procurement fact

🔴 **`api.github.com` repo endpoints have returned 403 for fourteen consecutive passes.** 🟢 **Triaged
this pass into three classes (`P107-A`), and the important one is that this is an **authorization
boundary**, not an outage: `/rate_limit` returns 200 reporting **15 000 remaining, 0 used**, and
attached repositories return complete JSON.** 🔴 **Waiting never clears it. `/search/*` has no remedy
at all, so API-side repository discovery is permanently unavailable here.**

🟢 **But `git ls-remote` — no API, no credential, no clone — read 299 of 299 addresses in 2 m 17 s and
yields the release ladder, the branch count and a full 40-character HEAD sha.** 🔵 **It reproduced
three previously published figures exactly (`academico` 0, `pupilfirst` 57, `UniTime` 101), so it
was validated before it was trusted.**

🟡 **Generalised, because the trend is not about this environment:** ★ is a popularity signal that a
vendor API can withhold; **release cadence is a maintenance signal carried by the protocol itself**
and no intermediary can withhold it. 🟢 **For due diligence on an open-source dependency, the second
is both more informative and more robustly available than the first.** 🔵 **This KB spent fourteen
passes recording the absence of the weaker signal while the stronger one was one command away.**

**Signal**: 🟢 **`Gap 376`'s corrective duty is discharged in part, not by regaining the API but by
no longer needing it.** 🔴 **`T36` also carries a caution: `P107-C` — annotated tags appear twice in
ref output, and an unfiltered count overstates by up to 2× (shelf-wide +58 %).**

**Pass 106, 2026-10-10.** ⏱️ **Sixteenth pass of this date.** 🟢 **Three trends added, each from a
measurement made this pass rather than from a channel.**

## 🔴 `T33` — the licence of EMEA's public education infrastructure is the EU's own, and permissive-first tooling is blind to it

🟢 **Measured: eight repositories from `opetushallitus` — the Finnish National Agency for Education —
and all eight are EUPL (six at 1.1, two at 1.2).** 🔴 **Every one of them read `UNRECOGNISED` to this
KB until this pass, because the EUPL had no branch in the classifier and is named by REFERENCE in a
296–654 B payload rather than carried as a licence body** (`P742`).

🔵 **What is behind those eight addresses is not a side project: `koski` is the national
study-rights and completed-studies registry, `eperusteet` the national core-curriculum service,
`ataru` national admissions, `oppijanumerorekisteri` the national learner-number registry.** 🟢 **A
complete national education data stack, publicly licensed.**

🔴 **The trend is not "Finland publishes code". It is that the grant tier of EMEA public education
is a family that MIT/Apache/BSD tooling cannot see** — so a scan built on a permissive allow-list
reports EMEA as grant-less and is wrong in the most expensive direction. 🟡 **The EUPL is copyleft,
with reciprocity and an explicit compatibility list, so the tier is adopt-and-contribute rather than
embed-and-keep. That is a pricing input, not a disqualification.**

**Signal**: 🟢 **`Gap 395` answered from an angle it never considered.** Pass 104 read EMEA public
supply as *"ships releases and does not grant"*; it grants, under the EU's own licence.

## 🔴 `T34` — Moodle's AI subsystem has **zero** package-channel presence

🟢 **Measured on `packagist.org`, a channel opened this pass (`moodle.org` remains `http=000`):**
🔴 **`moodle-aiprovider` = 0 packages and `moodle-aiplacement` = 0 packages** — the two plugin types
Moodle's **own** AI subsystem defines — against **159 packages across 21 older types**
(`moodle-local` 33, `moodle-tool` 27, `moodle-block` 24, `moodle-mod` 22).

🔵 **And the licence composition of those 159 is uniform: all 143 that declare a licence at
all declare the GPL-3 family. Not one is permissive.** 🟢 **`P1033`/`T30` — the copyleft frontier is
the plugin tree — was carried on seven rows and now rests on 143 without exception.**

🟢 **The commercial reading, and it is the firmest in this file: the LMS→agent seam is a Globant
DELIVERABLE, not a dependency.** 🔵 **`T28` said so from the MCP layer's licence scarcity; `T34` says
it from the opposite direction — the platform vendor defined the extension point and nobody has
shipped into it through the package channel.** 🔴 **An AI capability mounted INSIDE Moodle is
greenfield and will be GPL-3; one mounted beside it keeps whatever licence is chosen. Where the code
is mounted decides the licence, and that is not negotiable** (`verticals/solutions.md`).

## 🔴 `T35` — the restricted tier of education software is real, named, and clusters on exactly the high-value layers

🟢 **The whole-corpus census gave the classifier a bucket it never had — `NON-GRANT`, for a payload
that resolves 200 and grants nothing — and found 13 rows.** 🔵 **They are not a long tail of hobby
projects. They sit on the layers a studio reaches for first:**

| layer | row | terms |
|---|---|---|
| student advising | [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic-2.0** |
| synthetic data | [`sdv-dev/sdv`](https://github.com/sdv-dev/sdv) | 🔴 **BUSL-1.1** |
| data quality | [`sodadata/soda-core`](https://github.com/sodadata/soda-core) | 🔴 **Elastic-2.0** |
| early warning | [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | 🔴 **click-through terms of use** |
| skills extraction | [`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml) | 🔴 **click-through terms of use** |
| tutoring evaluation | [`khan/tutoring-accuracy-dataset`](https://github.com/khan/tutoring-accuracy-dataset) | 🔴 **bespoke dataset licence** |
| RAG for teaching | [`digillab-lmu/smart-rag`](https://github.com/digillab-lmu/smart-rag) | 🔴 **PolyForm Noncommercial** |

🔵 **Two properties make this a trend rather than a list.** 🟢 **First, all 13 were sitting in
`UNRECOGNISED` BESIDE real grants, so a census that reports an unreadable payload as merely unknown
puts a commercial bar and a permissive grant in the same bucket.** 🔴 **Second, the restriction is
increasingly NOT a licence a tool recognises: Elastic 2.0, BUSL and PolyForm are source-available
rather than open source, and two of the 13 are bare click-through terms with no licence identity at
all.**

🟢 **Mitigation, and it is cheap: the restriction check must run BEFORE any grant branch and must be
challenged by a declared-grant test** (`P1041`). 🔵 **Measured consequence of getting that order
wrong, in this very pass: a generic "All rights reserved" branch demoted `huggingface/transformers`,
`mlflow/mlflow` and `masakhane-ner` — three real Apache-2.0 rows — to non-grant.**

**Pass 105, 2026-10-10.** ⏱️ **Fifteenth pass of this date.** 🆕 **31 trend sections — `T1`–`T32`, with `T26` refuted in pass 103, `T28`–`T30` added in pass 104 and `T31`–`T32` added here.** 🔴 **`T29` is flagged for re-measurement by `T31`: it was derived with a classifier that cannot see this industry's own licence.**
🟢 **`T27` is new.** 🔴 **`T26` is AMENDED — half of it is refuted, and the refutation is regional.**

- 🟢 **`T27`** — **the permissive, education-specific, release-engineered platform exists exactly
  where a NATIONAL PROGRAMME built one, and nowhere else.** Measured this pass: **North America** has
  `Ed-Fi-ODS` (**Apache-2.0**, `LICENSE.txt` 10 172 B, **42 tags**) and `Ed-Fi-Data-Standard`
  (Apache-2.0, **21 tags**); **APAC** has Sunbird — `sunbird-lms-service` (**MIT, 450 tags**),
  `knowledge-platform` (**MIT, 336 tags**), `sunbird-devops` (**MIT, 702 tags**) — plus the evaluation
  harness its own regulator's foundation publishes, `aiverify-foundation/moonshot` (**Apache-2.0, 26
  tags**, AI Verify Foundation / IMDA Singapore). 🔴 **EMEA's institutional output of the same period
  ships RELEASES WITH NO GRANT**: the European Commission's `european-digital-credentials` is at
  **`2.0.6`** with no payload at seven licence names and a clean control, and `fwu-de/schulfach-ontologie`
  ships `1.0.0` the same way (`Gap 395`). 🔴 **LATAM has no row of this shape at all** — what it has
  is the CURRICULUM layer (`bncc-pacotes`, MIT + CC BY 4.0, 1 721 verified objectives).
  🔵 **So "can we adopt an open platform?" has a different answer per region, and the answer is set by
  whether a public programme chose to license its own code.** 🟢 **Operationally: North America and
  APAC engagements can ADOPT; EMEA and LATAM engagements CONSTRUCT (`P102-A`) — and in EMEA the
  cheapest first action item is a written grant request to the publishing body.**

- 🟢 **`T26`** — **in education the PERMISSIVE administrative supply is GENERIC and the
  EDUCATION-SPECIFIC administrative supply is COPYLEFT, so a permissive SIS is a BUILD, never an
  ADOPT.** Measured across the whole tier this pass: education-specific and copyleft — **OpenEduCat
  (LGPL-3.0)**, **ERPNext / `frappe-education` (GPL)**; permissive and generic — 🆕 **Apache OFBiz
  (Apache-2.0, 26 tags)**, 🆕 **Corteza (Apache-2.0, 298 tags)**; education-specific and permissive but
  🔴 **unreleased** — `academico-sis/academico` (MIT, **0 tags, no version scheme**, `P985`).
  🔴 **— AMENDED p103: "no row is all three" is REFUTED for the student-data layer.** `Ed-Fi-ODS`
  (Apache-2.0, **42 tags**) and `Ed-Fi-Data-Standard` (Apache-2.0, **21 tags**) are
  education-specific, permissive AND released, as are Sunbird's `sunbird-lms-service` (MIT, **450
  tags**) and `knowledge-platform` (MIT, **336 tags**). 🔵 **`T26` was measuring this KB's coverage
  and reporting it as an industry property — all four rows were already in this repository, in the
  pre-reset archive or an instrument worklist (`Gap 394`).** 🟢 **What SURVIVES of `T26` is the
  regional half, now stated as `T27`: those rows belong to national programmes, so the generic-core
  construction is still the path in a region without one.** 🟢 **The defensible offer, where no
  national platform exists, is a generic Apache-2.0 core plus the education domain model** — and `Jasig/SSP` (Apache-2.0, **57 releases** of schema history) is that
  model. 🔴 **The failure mode this names: "adopt an open-source SIS" is a copyleft decision disguised
  as a procurement one**, and the two permissive cores that avoid it were in this KB's history for
  passes without ever being shelved (`Gap 384`).
- 🟢 **`T24`** — **in education the PERMISSIVE open-source supply predates the AI wave, and the
  AI-era supply is ungranted.** The permissive student-success platform on this KB's shelf is a **2012
  consortium artifact** (`Jasig/SSP`, Apache-2.0, 57 releases); the **2024–2026 ML implementations of the
  same capability are 4-of-6 ungranted, 1-of-6 non-commercial, 1-of-6 a portfolio project.**
  🔵 **Consortium-era code was licensed deliberately; AI-era repos are published without a licence at
  all.** 🔴 **So "newer" is systematically less takeable than "older" in this industry.**
- 🟢 **`T25`** — **in APAC the stated demand driver is TEACHER SHORTAGE, not cost reduction**, and the
  public money follows training rather than infrastructure: South Korea's AI-textbook programme pairs
  **~$70M of infrastructure with ~$760M of teacher training**, and Singapore's 2026 commitment is
  **training teachers at all levels**. 🔵 **Which re-ranks the offer: automate PREPARATION and MARKING
  before learner-facing chat.**

- 🔴 **`T20` is RETRACTED.** It claimed *"`Gap 372` is a RELEASE gap — none of the three permissive
  open-response scorers has a single release tag."* 🟢 **Two scorers on this KB's own shelf DO have
  releases** — `wwrwbs/AI_AWE` (`v0.1.0`, adapter artifact `http=200`) and
  `EducationalTestingService/rsmtool` (**33 tags, `v12.0.0`**) — and neither had ever had its tags
  counted, because `tags` became a measured column only at pass 98. 🔵 **`T20` measured the three
  rows pass 99 had just added and generalised to a tier containing two it did not re-measure.**
  🟢 **The replacement statement is `T21`.**
- 🟢 **`T21`** — **the binding constraint on regulated open-response scoring is the CORPUS, not the
  code and not the release.** The code is Apache-2.0 and runs; the **training corpus** (PERSUADE 2.0)
  is **`CC-BY-NC-SA-4.0`** by its own author's payload, so **the distributed weights, not the
  software, are what a commercial engagement cannot take.**
- 🟢 **`T22`** — **in corporate L&D the blocker is the PLATFORM, and it is measured in EMEA for the
  first time.** 🟡 Fosway (12th year, search-summary grade): **AI is the top strategic priority**,
  budgets under the **most pressure since COVID**, and **almost two in three** L&D professionals say
  their **LMS/LXP is not delivering adequately on AI**. 🔵 **That is a replacement market with a
  stated reason, not a greenfield one.**
- 🟢 **`T23`** — **in a regulated education activity the best permissive tooling comes from the
  TESTING INCUMBENT, not the AI community.** The most release-engineered permissive assessment
  repository in this industry is **ETS's**, and nine passes of this KB searched AI-community
  repositories to find it.
- 🔴 **The duty that binds FIRST is unchanged and now has a NARROWING and a safe harbour.** Article
  50(2) machine-readable marking binds GenAI already on the market on **2 December 2026** (**53
  days** at pass 99, 🔴 **now 53 → 8 weeks → `2026-12-02`, i.e. 53 days from 10 October**).
  🟢 **New this pass:** the Commission **confirmed the Transparency Code of Practice as adequate** and
  published the **final** Article 50 guidelines (July 2026), and 🟢 **AI-generated TRANSLATIONS are
  now exempt** as *"standard editing"* — 🔴 **while summaries and substantive rewrites are not.**
  🔵 **See the `T4` amendment below: for an LMS that is the whole scoping question.**
- 🔴 **And one duty needs no planning at all:** emotion recognition in education, **prohibited since
  2 Feb 2025**, unpostponed.

🔴 **Zero primary-source reads, TENTH consecutive pass.** 🟢 Reachable: the WebSearch backend,
`github.com` git smart-HTTP, `raw.githubusercontent.com` and `release-assets.githubusercontent.com`.
🔴 Refused, each probed individually this pass (error 56 / `403 CONNECT tunnel failed`): `arxiv.org`,
`the-learning-agency-lab.com`, `www.fosway.com`, `www.cipd.org` — and, carried from pass 99,
`www.iesalc.unesco.org`, `digital-strategy.ec.europa.eu`, `eur-lex.europa.eu`, `www.kaggle.com`.
🔵 **Every regulatory and market row added this pass is search-summary grade and says so.**

## T31 — 🆕 p105 The permissive supply in this industry is **systematically undercounted**, and the cause is that education's own licence is unreadable to generic tooling

🔵 **ECL-2.0 — the Educational Community License — is the only OSI-approved licence written FOR
education. It is the Apache-2.0 text with section 3's patent grant narrowed to education
communities, and it is permissive.**

🔴 **Measured this pass: the ECL-2.0 payload contains ZERO occurrences of the string
`Apache License`.** It names the *"Apache 2.0 license"* in lower case. 🟢 **So every licence
classifier keyed on the Apache title — including the one this KB's own census runs — returns
`UNRECOGNISED` for it.**

**Why this is a trend and not a bug report:** 🔵 **the undercount is directional.** Generic
open-source tooling is tuned to the nine common families, and the one family that is
education-specific is the one it cannot see. 🔴 **So any market scan of education open source
performed with generic tooling will systematically understate permissive supply, and it will
understate it exactly at the institutional-platform layer — Sakai, Opencast, the Apereo learning-
analytics stack — where the mature, procurement-friendly, North-American-HE-governed code lives.**

| measure, this KB's 99-address census | pass 104 | 🟢 **corrected** |
|---|---|---|
| permissive | 38 | 🟢 **40** |
| 🔴 the error | — | 🔴 **5.3 % of permissive supply, from 6 repositories in ONE lineage** |

🟡 **Commercial reading.** When a client's incumbent adviser reports *"the open-source education
stack is mostly copyleft, so you will have to build"*, 🔵 **ask which tool produced the licence
column.** 🟢 **If the answer is a scanner rather than a reader, the permissive tier is larger than
the report says, and `Sakai` and `Opencast` are the two rows most likely to be missing from it.**
🔴 **`T29` (released supply is copyleft, permissive supply is runtime) is now partly an ARTEFACT of
this blindness and must be re-measured with an ECL-aware classifier before it is cited again.**

## T32 — 🆕 p105 A repository's LANGUAGE is not its region, and neither is its university's name

🔵 **Pass 104 found eight Spanish/Portuguese-named repositories and refused to call them LATAM
supply, because three were demonstrably EMEA. This pass resolved the remaining five by reading
their trees, and the result is a method, not just five rows.**

| placed | by what string | count |
|---|---|---|
| 🟢 **LATAM** | `SIGAA` (Brazilian federal university system) · `uan.edu.co` · the country word `Colombia` | 🟢 **3** |
| EMEA | — | **0** |
| 🔴 **UNPLACED** | 🔴 no marker anywhere in the tree | 🔴 **2** |

🔴 **And the instrument got one of them WRONG first.** `mietiainvestigacion-creator/api-eduadapt`
names **Universidad de Córdoba** — which exists in Córdoba, **Spain** and Córdoba, **Colombia**.
🟢 **A rule placing `universidad de …` in EMEA does not read a region; it invents one.** The row is
LATAM, and the string that establishes it is the word **Colombia** elsewhere in the same README.

**Why this is a trend:** 🔵 **education supply is published in national languages far more than
most industries' is, because the buyer is a national ministry or a public university.** 🔴 **That
makes language the most AVAILABLE regional signal and one of the least reliable — Spanish and
Portuguese each span two regions, and university names collide across them routinely (`Universidad
de Córdoba`, `Universidad de Granada`, `Universidad de Santiago`).** 🟢 **The reliable signals are
narrow: an academic ccTLD, an explicit country word, or a nationally unique system name.**

🟡 **Consequence for this KB, and it cuts against its own history:** 🔴 **`P1035` invalidates
org-name regional reasoning in BOTH directions.** The three German rows pass 104 called
"demonstrably EMEA" (`fwu-de`, `dini-ag-kim`) were placed on exactly the reasoning this pass has
just refuted, and re-reading them is the second lead pre-registered for the next pass.
🔵 **Two of five rows staying `UNPLACED` is the honest output, and it is the point: an informed gap
beats a plausible guess, because the guess becomes typed regional data downstream.**

## T28 — 🆕 p104 The education MCP layer is the LEAST licensed layer this KB has measured

🔵 **Measured, not sampled: 15 of the 99 addresses probed in pass 104 are MCP servers for an
education system** — Moodle, Canvas, a US school district, a national SIS.

| | n | |
|---|---|---|
| 🟢 **MIT** | 6 | `ahnopologetic/canvas-lms-mcp` (3 tags) · `jibberswrld/fcps-school-mcp` (4) · `sukhrobyangibaev/mcp_hemis_student` (1) · `ait0u5hi/canvas-scholar-mcp` (1) · `a2br/moodle-mcp` (0) · `jorickpepin/campus-mcp` (0) |
| 🔴 **no payload, clean 200-control** | 🔴 **6** | `ink-waffle/moodle-mcp` · `ink-waffle/sisu-mcp` · `dddanielliu/nccu-moodle-mcp` · `git-pratap-shrey/uniai_mcp` · `poorvika12-hub/student_mcp` · `hocphi-info/hocphi-info-mcp` |
| 🔴 **ABSENT** | 🔴 **2** | `owentaylor/canvas-mcp` · `imazhar101/mcp-canvas-server` |
| 🟡 copyleft | 1 | `hefi002/tfg-mcp-moodle-server` (GPL-3.0) |

🔴 **Eight of fifteen — 53 % — cannot be used commercially.** 🔴 **Canvas is the sharpest case: four
Canvas MCP servers, two MIT and two that no longer resolve.**

🔵 **Why this matters more than the raw ratio: the MCP server is the LMS-to-agent seam, and it is the
one part of every education agent architecture that is currently written by individuals.** 🟢 **The
trend to plan around is that this layer is a Globant DELIVERABLE, not a dependency — and the two rows
with release engineering (`canvas-lms-mcp`, `fcps-school-mcp`) are the only sensible forks.**

## T29 — 🆕 p104 In education the RELEASED supply is copyleft, and the permissive supply is runtime

🔵 **Across the 99 probed addresses, sorted by release engineering rather than by licence:**

| | permissive (MIT/Apache/BSD) | copyleft (GPL/AGPL/LGPL/OSL) |
|---|---|---|
| rows | 🟢 **38** | 22 |
| rows with **≥ 50 tags** | 5 | 🔴 **11** |
| rows with **zero** tags | 🔴 **19 of 38** | 4 of 22 |

🔴 **Half the permissive rows have never cut a release. The copyleft side ships.** 🟡 **And the claim
has to be stated precisely, because two rows contradict the lazy version: of the five permissive rows
above 50 tags, three are general-purpose runtime (`ollama` 689, `temporal` 573, `transformers` 291)
and 🟢 **two ARE education-specific and released** — `dspace/dspace` (BSD-3-Clause, 136) and
`fwu-de/fwu-kc-extensions` (Apache-2.0, 118).**

🔵 **Both of those sit at the INFRASTRUCTURE end — institutional repository and school identity —
never at the teaching-and-learning end.** 🟢 **So `T29` reads: the ADOPT/BUILD line in education runs
between LAYERS, not between regions.** 🔴 **It is the correction `T27` needed: `T27` placed ADOPT in
North America and APAC and BUILD in EMEA and LATAM; `T29` says the layer decides first and the region
second.**

## T30 — 🆕 p104 The GPL boundary is the plugin tree, and it is checkable with one HTTP request

🔴 **Every Moodle-plugin row in the corpus that carries a grant carries GPL-3.0 — 7 of 7**, including
Microsoft's own `o365-moodle` at **695 tags**, the most-released row this KB has measured.
🟢 **And both permissive Moodle-adjacent rows are permissive because they sit OUTSIDE that tree —
verified by probing for the root `version.php` that makes a directory a Moodle plugin:**

| row | root `version.php` | grant |
|---|---|---|
| `jeanlucio/moodle-local_aihub` | 🔴 **200 — a plugin tree** | 🔴 GPL-3.0 |
| `a2br/moodle-mcp` | 🟢 404 | 🟢 **MIT** |
| `sngdtechnologies/ai-moodle-security` | 🟢 404 | 🟢 **BSD-2-Clause** |

🔵 **`P1033`: code that loads INSIDE the LMS inherits its licence; code that speaks to it across its
API, or wraps it in infrastructure, does not.** 🟢 **A vendor with every incentive to stay proprietary
— Microsoft — shipped under GPL-3.0 anyway, because the platform's licence is what reaches the
installed base. Plan the IP boundary at the API seam, and the question stops being a negotiation.**

## 🔴 🆕 p104 `P1023` holds a THIRD pass — the public web is saturated for this industry

🔵 **All six mandated query families plus all four regional sweeps ran this pass. Not one returned an
item this repository did not already hold**, each checked by `grep` against the live corpus rather
than by impression: the market bands ($6.4–10.6 B), the 92 % student-use figure, UNESCO IESALC's
87 %/26 %, the Digital Education Council's 92 %/79 %, OpenEduCat's LGPL-3.0, the TCS–Pearson
alliance, the Council of Europe's 2024 conference.

🟢 **Every finding in pass 104 came from probing this repository's own archive. None came from
searching.** 🔵 **Read `P1023` as a standing property of this industry's public web and not a bad
week: the marginal value is now in MEASURING what the KB already names, and `Gap 394` returned three
trends, one corrected gap, one new gap and five principles from 99 addresses this KB already had.**

## T27 — 🆕 p103 The permissive education-specific platform exists where a NATIONAL PROGRAMME built one, and the answer changes by region

🔵 **This is the trend that makes the region field load-bearing rather than decorative.** 🔴 **Four
passes of this KB have asked "is there a permissive platform for this layer?" as if it had one
answer. It has four.**

### 🟢 The measurement, all payload-read this pass (`P1005`)

| region | permissive · education-specific · released? | evidence |
|---|---|---|
| **North America** | 🟢 **YES** | `ed-fi-alliance-oss/Ed-Fi-ODS` — **Apache-2.0** (`LICENSE.txt` **10 172 B**), `main` · `e453cd2cad8a0653c65453948d3d235aec7c517c`, **42 tags** (`v7.3.2-pre`); `ed-fi-alliance-oss/Ed-Fi-Data-Standard` — Apache-2.0 (10 173 B), **21 tags**. 🔵 A US K-12 alliance, not a vendor. |
| **APAC** | 🟢 **YES, and twice over** | Sunbird: `sunbird-lms-service` **MIT, 450 tags**; `knowledge-platform` **MIT, 336 tags**; `sunbird-devops` **MIT, 702 tags** — India's public digital-education stack. 🟢 **Plus the EVALUATION harness: `aiverify-foundation/moonshot` Apache-2.0, 26 tags, from the body Singapore's IMDA convened.** |
| **EMEA** | 🔴 **NO — and the failure mode is a missing GRANT, not missing code** | `european-commission-empl/european-digital-credentials`: **4 tags, top `2.0.6`**, 🔴 **no payload at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `NOTICE`, `LICENCE`, `license`**, clean 200-control. `fwu-de/schulfach-ontologie`: **`1.0.0`**, 🔴 no payload, clean control. 🔵 **`Gap 395`.** |
| **LATAM** | 🔴 **NO row of this shape measured** | 🟢 **But the CURRICULUM layer is `P800`-grade and adoptable**: `bncc-dev/bncc-pacotes` (MIT code + CC BY 4.0 data, **1 721 verified BNCC objectives**, 7 MCP tools, dataset embedded so lookups are local) and an independent second implementation, `dfdb76/bncc-mcp` (MIT). |

### 🔵 Why this is a trend and not a regional note

🟢 **The common cause is visible in all four rows: a public programme that intends its code to be
re-used licenses it, and one that publishes code as a deliverable does not.** 🔴 **Ed-Fi and Sunbird
exist to be deployed by third parties — districts, states, other countries — so the grant is part of
the product.** 🔴 **The EDC implementation and the FWU ontologies exist as the output of a
programme, so the release is a milestone and the licence was nobody's deliverable.** 🔵 **That
predicts where to look: ask whether the publisher's mandate includes OTHERS running the software,
not whether the publisher is public.**

### 🟢 What it changes in the offer

| region | the sentence that goes in the proposal |
|---|---|
| **North America** | 🟢 **"We adopt Ed-Fi for the student-data spine."** Permissive end to end with `canvas-mcp` (MIT, 26 tags) at the LMS edge — costed as **`P103-B`**. |
| **APAC** | 🟢 **"We adopt Sunbird and evaluate on the harness your own regulator's foundation maintains."** 🔵 A procurement argument no other region can make — `moonshot` + `moonshot-cicd`, **`P103-A`**. |
| **EMEA** | 🔴 **"We construct on a generic Apache-2.0 core"** (`P102-A`), 🟢 **and the first action item is a written grant request to the publishing body** — cheap, dateable, and it either unblocks the EDC route or documents that it is closed. |
| **LATAM** | 🟢 **"We adopt the curriculum spine and construct the platform."** `P102-A` with a BNCC tool at the alignment edge. 🔵 **A different engagement SHAPE, not a discounted version of the North America one.** |

### 🔴 What would refute `T27`

🟢 **Any one of these, and each is a concrete next-pass query:** a permissive, education-specific,
released platform from a **vendor** rather than a programme; a **grant appearing** on
`european-digital-credentials` (which would make EMEA an adopt region overnight); or a **LATAM
national programme** publishing a licensed platform — Uruguay's **Ceibal** and Brazil's **RNP /
MEC** are the obvious places to look, and neither has been probed by this KB.

🟡 **And the honest limit: `n = 2` on the YES side.** 🔵 **Two programmes in two regions is a shape,
not a law** — the same `n=2` test this KB applied to MCP × SCORM at pass 92 and to the BNCC servers
at pass 93.

## T24 — 🆕 p101 The permissive supply predates the AI wave; the AI-era supply is ungranted

🔵 **This is the most commercially consequential pattern measured in 101 passes, because it inverts
the usual assumption that newer code is easier to adopt.**

🟢 **The evidence is one capability measured end to end — student early warning.**
- 🟢 **The 2012 consortium artifact is permissive and release-engineered**: `Jasig/SSP`, **Apache-2.0**,
  **57 tags**, `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6`, with a `NOTICE` that enumerates every bundled
  grant. 🔵 **Someone was paid to get the licensing right.**
- 🔴 **The 2024–2026 ML implementations of the SAME capability are not takeable**: 4 of 6 carry **no
  licence payload at 24 filenames**, 1 is **non-commercial by its own text** (`dssg/student-early-warning`
  — *"excludes any service or part of selling a service"*), and 1 is **MIT with 0 tags and one author**.
- 🔴 **The pedagogical judge repeats it**: `kaushal0494/AITutor-EvalKit` is an EACL 2026 system demo
  whose **paper claims MIT** and whose **repository carries no licence payload** (`Gap 391`, `P1014`).

🔵 **Why it happens, stated as a mechanism rather than a mood:** consortium software (JA-SIG/Apereo,
Sakai, 1EdTech) was published by institutions with counsel and procurement obligations, so a grant was a
deliverable. 🔴 **AI-era education repos are overwhelmingly research artefacts and portfolio projects,
where the paper is the deliverable and the licence is an afterthought.**

🟢 **What a studio does with it:**
1. 🟢 **Search the consortium era FIRST for any administrative or records capability** — and search it
   under its **predecessor org names** (`P1012`: `apereo/*` is ABSENT where `Jasig/*` exists).
2. 🔴 **Treat AI-era repos in this industry as papers until a payload says otherwise.** Read the
   method, re-implement, cite the paper. 🔵 **`Gnanakamalesh-M`'s calibrated-XGBoost-plus-SHAP design is
   worth more as a READ than as a dependency.**
3. 🔴 **And check what the old code BUNDLES** (`P1013`): Apache-2.0 at the root, GPL-3.0 Ext JS and LGPL
   reporting inside. 🟢 **The schema is the asset; the UI is the liability.**

## T25 — 🆕 p101 In APAC the driver is teacher shortage, and the budget goes to training

🟢 **Measured, not inferred, from this pass's country-named sweep** (the regional sweep alone returned
nothing education-specific — `P1017`).

- 🟢 **South Korea**: AI digital textbooks for maths, English and computing (March 2025) with
  **~$70M for digital infrastructure against ~$760M for teacher training** — 🔵 **an order of magnitude
  more on people than on platform.**
- 🟢 **Singapore**: by **2026**, AI-in-education training offered to **teachers at all levels**,
  including pre-service, under the Digital Education Blueprint and National AI Strategy.
- 🟢 **China**: a **General AI Education Guide** for primary and secondary schools plus a guide on
  students' generative-AI use (May 2025), and **Beijing mandating ≥8 hours of AI instruction per year**.
- 🟢 **Regional market framing names teacher shortages explicitly** as a demand driver, alongside large
  student populations — **~$591.6M (2024) → ~$1.85B (2029), ~20.9% CAGR**, the fastest-growing region.
- 🔴 **India: no national school AI policy surfaced in either sweep** — an open question, recorded
  rather than filled.

🔵 **Consequence for the offer: where the buyer's problem is a shortage of teachers, the product that
sells is the one that gives hours back** — preparation, marking, reporting, scheduling — **not the one
that puts a chat window in front of a student.** 🔴 **And a multi-country APAC rollout cannot carry one
compliance story**: Singapore runs mature responsible-AI guidelines, China legislates against algorithmic
misconduct, and the **ASEAN Guide on AI Governance and Ethics is still early-stage.**

## T21 — 🆕 p100 The binding constraint on regulated open-response scoring is the CORPUS, not the code

🔵 **Three passes have each named a different blocker for the same activity, and each was the previous
one's correction:**

| pass | the blocker it named | why it was wrong or incomplete |
|---|---|---|
| 93 | *"there is no production-grade permissive AES library in this industry"* | 🔴 One existed on the shelf the same pass (`AI_AWE`), classified as *"a reference for the architecture, never a dependency"* |
| 95 | *"the permissive supply is the VALIDATION layer; the scorer is copyleft or ungranted"* | 🟢 True of `openedx/ease` and `edx-ora2` (AGPL-3.0), 🔴 but the permissive scorer was already tabled |
| 99 | *"not a licence gap — a RELEASE gap, 0 of 3 tagged"* | 🔴 `tags` was never counted for the two rows that had them (`P1010`) |
| **100** | 🟢 **the CORPUS** | — |

🟢 **Why the corpus is the real one, and why it is more durable than the other three.** The code can
be forked, the release can be cut, the validation layer is Apache-2.0 and has **33 tags** — but a
scoring model is only as transferable as the licence of the essays it was trained on, and the largest
open student-essay corpus in existence carries **NonCommercial**:

| corpus | licence, and where it was read | usable commercially? |
|---|---|---|
| **PERSUADE 2.0** (>25 000 essays, grades 6–12) | 🔴 **`CC-BY-NC-SA-4.0`** — the **author's own** repo README, payload-read (`persuade_corpus_2.0`, **2 159 B**, line 29) | 🔴 **no** |
| **PERSUADE 1.0** | 🔴 **`CC-BY-NC-SA-4.0`** — same author, superseded repo (**3 557 B**, line 51) | 🔴 **no** |
| the same corpus per its **funder's** page | 🟡 *`CC BY 4.0`* — and that page describes **14 000** essays, a **different, smaller release** | 🟡 **unresolved, and not the operative term** |
| the same corpus per **`AI_AWE`'s own asset table** | 🔴 *"academic-use, attribution"* — **drops ShareAlike** (`Gap 390`) | 🔴 **no** |
| **ASAP 2.0** (≈24 000 essays) | 🟡 reported **`CC BY`**, snippet-only, **not payload-confirmed** | 🟡 **the lead worth running** |
| [`anaistack/cefr-asag-corpus`](https://github.com/anaistack/cefr-asag-corpus) | 🔴 **`CC-BY-NC-SA-4.0`**, payload-read (p99, `LICENSE.txt` **20 863 B**) | 🔴 **no** |

🔵 **So the industry's permissive supply for this activity is: code yes, validation yes, release yes,
corpus NO.** 🟢 **And that is a *procurement* problem rather than an engineering one, which makes it
cheaper to solve than any of the three blockers it replaces** — the client's own graded essays are
the asset, and `AI_AWE` ships the retraining seam
(`prepare_persuade.py --in /path/to/licensed/persuade_export.json`).

🔴 **What would refute `T21`:** a payload-confirmed `CC BY` or Apache/MIT graded essay corpus at
scale. 🟢 **ASAP 2.0 is the one candidate and it is pre-registered.** 🔵 **Note the asymmetry that
makes this trend sharp: `NC` on code would be unusual and loud; `NC` on data is the DEFAULT in
education research, and it is quiet.**

## T22 — 🆕 p100 In corporate L&D the blocker is the PLATFORM, and EMEA is finally placed

🔵 **`Gap 386` was discharged at pass 98 for SIZE and left open for PLACEMENT**: every L&D figure
this KB held was global or US. 🔴 **Pass 98 and pass 99 both failed to place EMEA, because they
queried the region.** 🟢 **Pass 99's own remedy was the fix — query the PUBLISHER, not the region —
and it paid immediately.**

🟡 **All figures in this trend are search-summary grade; `www.fosway.com` and `www.cipd.org` were
both probed this pass and both refused.**

| finding | source, and its grade | why it matters to an engagement |
|---|---|---|
| **AI is the top strategic priority** for learning teams | 🟡 Fosway *Digital Learning Realities 2026*, 12th year, European analyst — snippet | the budget conversation is already won; the delivery one is not |
| L&D budgets under **the most pressure since COVID**; stagnation with an underlying **decrease** | 🟡 Fosway — snippet | 🔴 **price for replacement of an existing line, not for net-new spend** |
| **almost 2 in 3** say their **LMS/LXP is not delivering adequately on AI** | 🟡 Fosway — snippet | 🟢 **the single most useful sentence in this file for an L&D pitch** |
| L&D teams believe they are **not adequately upskilling** for the next 2–3 years | 🟡 Fosway — snippet | the buyer needs capability transfer in the statement of work, not just software |
| 🔴 **MENA: L&D spend per FTE DOWN 28 %** in 2026, training hours flat | 🟡 SHRM, carried from p99 — 🔴 **recorded as MENA, not EMEA** | same direction as Fosway's budget finding, different sub-region |

🔴 **And the honest gap, with a date on it.** The CIPD's instrument was **renamed** for 2026 — it is
the **Skills and Learning at Work Survey**, fielded by **Censuswide**, and it **closed on 20 May
2026**. 🔴 **No 2026 findings were published as of this pass.** 🟢 **Baseline for when they land**
(2023 edition, YouGov, **1 108** respondents): only **59 %** of L&D staff felt able to respond to
changing skills needs, **down from 69 % in 2021**. 🔵 **Pre-registered: re-query after publication —
a third consecutive fall would make "L&D cannot keep up" a measured trend rather than a vendor
talking point.**

🟢 **Why this is a trend and not a market row.** The complaint is **not** *"we have no AI"* and
**not** *"AI is too expensive"*; it is *"the platform we already bought does not deliver it"*.
🔵 **That names the engagement precisely: AI on top of an incumbent LMS/LXP, replacing a line item
rather than opening one** — which is exactly the shape of `P91-RETIRED`'s surviving principle, *the
platform is the client's and the intelligence on top is ours*, now with a measured buyer behind it.

## T23 — 🆕 p100 In a regulated education activity, the permissive supply comes from the TESTING INCUMBENT

🔵 **The observation.** The most release-engineered permissive repository in educational assessment is
[`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) —
**Apache-2.0**, **33 tags**, **`v12.0.0`**, conda channel, two CI systems — published by **ETS**, the
organisation that scores **TOEFL** and the **GRE**. 🔴 **This KB spent nine passes searching
AI-community repositories and found it only when it stopped looking for *"AI"* and started looking
for *"scoring"*.**

🟢 **Why this is structural rather than a coincidence.** A regulated activity's obligations —
validity evidence, fairness analysis, an explanation owed to the person assessed — are **operational
necessities for an incumbent long before they are regulation for anyone else.** 🔵 **An organisation
that has been audited on score validity for decades has already built, and has reason to open-source,
exactly the artefact Annex III demands.** 🟢 **The AI community builds the scorer; the incumbent
builds the defensibility.** 🔵 **And the defensibility is the half a regulator asks for** — `T13`,
re-confirmed from a direction `T13` did not anticipate.

🔴 **The constraint on generalising it, and it is firm.** `P975`: **licence is a property of the
repository, never of the publisher.** The same ETS organisation ships
`EducationalTestingService/factor_analyzer` under **GPL-2.0** — a dependency-shaped library a scoring
pipeline would import without reading. 🟢 **So `T23` is a rule about where to LOOK, never about what
you will find when you get there.**

🟡 **What would refute `T23`:** an AI-community repository in a regulated education activity with
comparable release engineering, or a testing incumbent whose open-source output is uniformly
copyleft. 🔵 **Adjacent incumbents worth probing next, and pre-registered:** Cambridge Assessment,
Pearson's research arm, ACT, and the IMS/1EdTech reference implementations.

## T19 — 🆕 p99 The CONNECTOR decides which platform a studio can serve permissively, and it splits by platform

🔵 **Every pattern in this KB assumes an agent can reach the LMS the client already runs.** 🟢 **Pass
99 read the three repos that provide that reach and found they do not share a licence — and the split
falls across PLATFORMS, not across repos.**

| platform | connector | grant | tags / latest |
|---|---|---|---|
| **Canvas** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B | 🟢 **26 / `v1.14.0`** |
| **Moodle** | [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · 34 523 B | 🟡 **7 / `v0.1.7`** |
| **Moodle** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · 1 064 B | 🔴 **0** |

🔴 **Canvas has a connector that is permissive AND released. Moodle has one of each and neither is
both.** 🔵 **So the licence of a 1 KB glue repo — not the licence of the platform — decides whether an
engagement is permissive end to end.**

🔴 **And the consequence is regional, which is why this is a trend and not a row.** Moodle is what
ministries and public universities run, and it is the platform this KB has aimed at **LATAM** and the
public sector for eight passes. **North America**'s dominant higher-ed platform ships the permissive,
released connector. 🔵 **The region with the greater public-sector need inherits the worse integration
licence.**

🟢 **The manoeuvre, already documented here for MPL:** fork and pin the **1 064-byte MIT** server and
read the AGPL one as a **specification** rather than linking it (`sebserver-mcp-gate`'s move,
`§1.10(a)`). 🟡 **It is lawful and it is still a fork — an estimate must say so.**

🔵 **Falsifiable.** Three queries would break `T19`: a released permissive Moodle connector appearing
(`moodle mcp server MIT release`), the AGPL one relicensing, or a platform-neutral connector covering
both. 🟢 **Any of the three retires this trend, and that is the point of stating it this way.**

## T20 — 🆕 p99 The permissive supply is RELEASE-blocked, not LICENCE-blocked — and that is a different purchase

> 🔴 🆕 **p100 — RETRACTED IN ITS CONCLUSION. Read `T21` instead.** The measurement below is correct
> for the three rows it covers; the generalisation to the tier is not. 🟢 **Two permissive scorers on
> this KB's own shelf were already released** — `wwrwbs/AI_AWE` (`v0.1.0`, adapter artifact
> `http=200`) and `EducationalTestingService/rsmtool` (**33 tags, `v12.0.0`**) — and neither had had
> its tags counted, because `tags` became a measured column only at pass 98 (`P1010`).
> 🔵 **`Gap 372` is DISCHARGED; the real blocker is the CORPUS (`T21`, `Gap 390`).**

🔵 **Four passes carried `Gap 372` as "no permissive production-grade corrector for open response".**
🔴 **The premise was wrong in a way that cost four passes of searching for the wrong thing.**

| scorer | grant | tags |
|---|---|---|
| `KamalEzzo/automated-essay-grading-system` | 🟢 **MIT** | 🔴 **0** |
| `shibing624/judger` | 🟢 **Apache-2.0** | 🔴 **0** |
| `doheejin/ProTACT` | 🟢 **BSD-3-Clause** | 🔴 **0** |

🟢 **The control is from the same pass, same industry, same instrument:** `canvas-mcp` **26 tags**,
`HKUDS/DeepTutor` **135 tags**, `SafeExamBrowser/seb-server` **194 tags**. 🔵 **So "0 tags" is a real
signal here and not an artefact of how this industry publishes.**

🔵 **`T20`, stated generally: in education the permissive grant is abundant and the RELEASE is scarce**
— and the two are easy to confuse because both show up as "nothing usable found". 🟢 **The studio
offer that follows is harden-and-release, not search-and-adopt**, and `ProTACT`'s **cross-prompt**
property is the one worth hardening because transfer to an unseen prompt is what a client's next
assignment needs on day one.

🔴 **What moved instead of the code: the corpus.** The graded corpora do **not** share a licence — one
**CC-BY-NC-SA-4.0** read from payload, one reported **CC BY**, and one 🔴 **stated differently by its
distributor and its originator** (`Gap 389`). 🔵 **So the open term in an open-response engagement is
now a DATA licence, and it is a procurement term.**

## T17 — 🆕 p98 The permissive grant sits on the side that MEASURES; copyleft sits on the side that becomes the RECORD

🔵 **Two independent layers of this industry have now been measured end to end, and they have the same
seam in the same place.**

| layer | the MEASURING side | the RECORD side |
|---|---|---|
| **Open-response scoring** (`Gap 372`, p94) | 🟢 **Apache-2.0 / BSD-3** — `EducationalTestingService/rsmtool` (Apache-2.0, 2 916 commits), `skll` (BSD-3) | 🔴 **AGPL-3.0** — `openedx/ease`, `openedx/edx-ora2` |
| **Credentialing** (p98) | 🟢 **Apache-2.0** — `1EdTech/openbadges-validator-core` (validate), `CredentialEngine/Open-Badge-Publisher` (publish) | 🔴 **AGPL-3.0 / LGPL-3.0, 4 of 5** — `19otherrsh-dot/Opencred`, `Schroedinger-Hat/certo`, `LongsightGroup/credtrail-app`, `CoopCodeCommun/pyopenbadges` (mint) |

🔵 **The rule, stated so a later pass can break it: in education open source, the permissive grant
sits on the side that MEASURES and copyleft sits on the side that becomes the AUTHORITATIVE RECORD.**
🟢 **Two layers, four publishers, independently sampled seven passes apart.**

🔴 **Why it is an engagement-shape rule and not trivia.** It predicts the boundary before the
diligence is done: **build the measuring side, draw the licence boundary at the record, and let the
client own the record.** 🔵 **`P94-A` reached exactly that conclusion for scoring from first
principles** — T17 says it generalises, and says where to look for the next instance.

🟢 **The one permissive exception proves the shape rather than breaking it.**
`nfh-trust-labs/opencred` (MIT, **30 tags**, `v1.9.1`) **does** mint credentials — and it is a
**generic W3C Verifiable Credentials** toolkit, not an Open Badges product. 🔵 **The permissive
minting option is the one that is not education-specific**, which is the same observation
`repos/foundations.md` makes about spec-boundary code at a different altitude.

🟡 **Falsification tests a later pass should run**, each a `P955`-style technique query:
**rostering/SIS write-back**, **transcript and record-of-study**, **attendance of record**. 🔵 **If
the writing side of any of those is permissive, T17 is wrong and should be retired loudly.**

## T18 — 🆕 p98 The EU AI Act's education duties fall on the SCHOOL as deployer, which moves the buyer

🟢 **New limb this pass, and it is the one with a sales consequence** *(search-summary)*: a school
using a commercial AI tool to assess progress or flag at-risk learners is a **deployer** under the
Act and carries **its own** obligations, separate from the provider's.

🔵 **Every regulatory row in this file until now implicitly addressed the ed-tech VENDOR.** 🟢 **T18
says the institution is a compliance buyer in its own right** — and institutions have no compliance
function, no model documentation and no evidence pipeline. 🔵 **That is a services engagement, and
`T13`'s finding is what fills it**: the permissive supply for regulated assessment is the **evidence
layer** (`rsmtool` Apache-2.0, `skll` BSD-3), which is precisely what a deployer must produce and
cannot buy from the vendor.

🔴 **And one duty already binds, with nothing to wait for:** emotion recognition in education has
been **prohibited since 2 Feb 2025** (Art. 5). 🔵 **Affect and engagement inference ship switched on
by default in proctoring and engagement-analytics products**, so for an existing deployer this is a
**feature audit of live systems**, not a 2027 planning item. 🟢 **And as of this pass the platform
layer for it finally exists on the shelf:** `SafeExamBrowser/seb-server` (**MPL-2.0**, 194 tags) with
three tested artefacts already in `compose/code/` — 🔴 **which this KB had held since pass 43 while
publishing the exposure and offering nothing to address it** (`Gap 381`).

🟡 **The date is unchanged and now carries a FOURTH independent confirmation** — Annex III high-risk
obligations postponed to **2 Dec 2027** — 🔴 **but this pass's sources conflict with pass 94's record
on whether the Council has formally adopted the postponement**, and `EUR-Lex` refused `CONNECT` for
an eighth consecutive pass. 🔵 **Quote the date; do not quote the procedure.**

## T1 — The unit of delivery is the *agent skill*, not the application

🟢 **Holds on a second measurement.** `topics/ai-tutor` holds **664 repos** — unchanged from pass 90, so the
denominator is stable rather than inflating. Roughly a quarter of the first two pages are **skills for agent
harnesses** rather than web applications: markdown-plus-scripts packages with no UI, no hosting, no database
and no migration. `universal-examprep-skill` (303★), `universal-diagnostic-tutor-skill` (242★), `Bloom` (285★,
explicitly *"self-hostable AI tutor **and** Claude Code skill"*), `kaogong-skill` (166★), `education-skills`
(107★).

🟢 **Near-uniformly MIT** — every skill row verified this pass read MIT from the payload.
🟢 🆕 **And the shape has now crossed into a second tier.** `tomaszboloz/WCAG-Accessibility-Skills` (MIT) is
**both** an agent skill **and** an accessibility checker, and `Community-Access/accessibility-agents` (MIT)
ships eleven review agents for coding hosts. **The skill is becoming the delivery vehicle for compliance
tooling, not just for tutoring** — which is a more defensible sale, because it attaches to a standard.
🔴 **The counter-risk is unchanged:** a skill inherits the host's model, limits and data policy. Where
automated assessment is regulated (Korea, Vietnam) or student-data training restricted (California AB 1159),
"it is just a skill" is not a compliance position.

## T2 — A vertical with its own licence family gets undercounted as copyleft by generic tooling

🟢 **Pass 90's finding, now fixed in code rather than only described.** `Sakai` and `Opencast` are
**ECL-2.0** — the Educational Community License, OSI-approved, Apache-2.0-derived, **permissive**. v2's
classifier returned `OTHER/unclassified`; unclassified reads as risk and gets dropped, which is part of how
*"8 of 8 copyleft"* survived six passes. 🟢 **The shared classifier `lib/license_family.sh` tests ECL *before* Apache** (ECL is
Apache-derived, so an Apache test swallows it) and both rows now classify. `OTHER/unclassified` across the
92-slug shelf went **2 → 0**.

🟢 🆕 **The same reasoning extended, pre-emptively, to the licences this industry will meet next:**
**EUPL-1.2** (the European Union Public Licence — the grant EU public bodies are steered toward, so it will
appear in EMEA public-sector education tenders) and three **source-available, non-OSI** families now named
rather than dropped: **BSL-1.1**, **Fair Code** and the **Sustainable Use License**. 🔴 That last group
matters because `leemonade/leemons` (292★, listed on `topics/lms`) is **Fair Code License v1.0 — not open
source**, and v2 would have shown it as merely "unclassified".

🔵 **The transferable rule: name the family, including the families that are not open.** Silence and a
refusal are both "unclassified" to a reader, and only one of them is a warning.

## T3 — Adoption is near-universal; governance is the market

Consistent across every region measured. 🆕 The LATAM governance figure is now a *measured* one rather than a
paraphrase.

| region | adoption | governance |
|---|---|---|
| North America | 86 % of orgs; 60 % of K-12 teachers | 🔴 134 bills / 31 states; 🆕 **only ~10 % of institutions have formal guidelines, and 71 % of teachers report no AI training** |
| LATAM | 🟢 87 % of institutions (UNESCO IESALC, 200 institutions / 19 countries, fieldwork **Aug–Oct 2025**); 92 % of students, 🆕 **79 % of faculty** | 🔴 🆕 **26 % have any formal framework** (UNESCO's own figure); no sectoral regulation anywhere in the region |
| APAC | fastest growth, 28.1 % CAGR | 🟡 the world's most advanced *and* most fragmented law — **plus three curriculum mandates** (see `T7`) |
| EMEA | 🟡 🆕 **first numbers ever recorded here** — UK: 36 % feel encouraged by their institution, 38 % are provided AI tools (HEPI, n=1 054) | 🟢 the most defined calendar: AI Act high-risk **2 Dec 2027**, 🆕 **Art. 4 literacy duty in force now** |

🟢 **The number to carry into a pitch has changed, and it is stronger than pass 90's.** Not "92 % use against
30 % effective" — which rested on a figure this pass found mis-stated — but **92 % of LATAM students using AI
against 26 % of institutions having any framework at all**, both from named instruments with stated sample
sizes. 🔵 **The purchasable artefact is governance plus capability: policy, disclosure, assessment redesign,
staff training, and an audit trail.** North America's 71 %-untrained figure says the capability half is the
bigger one.

## T4 — The EU AI Act has **two** deadlines, and the one that binds now is the one nobody cites

🟡 High-risk obligations — education among them — moved to **2 December 2027** (Digital/AI Omnibus, Council
approval 29 Jun 2026); embedded high-risk systems to 2 Aug 2028. Enforcement *powers* still begin 2 Aug 2026.
🔴 **A large share of vendor and consultancy guidance still states August 2026 for high-risk duties, and this
pass found that exact error again in a current source.**
🔴 🆕 **p93 found it a fifth time, and in a source that is otherwise *correct and current*** — a commentary
on the European Commission's **March 2026** ethical-guidelines update (see `T9`) which states that
*"obligations for Annex III high-risk AI systems apply from 2 August 2026, and education is expressly a
high-risk area."* 🔵 **The second half is right and the date is wrong by sixteen months.**
🟢 **Five independent instances across five passes is no longer an anecdote about sloppy blogs: the wrong
date is the majority reading of this regulation in the market.** That is a commercial fact, not a
correction — it means **a client's incumbent adviser is more likely than not to have given them the wrong
deadline**, and arriving with the dated Council decision is a differentiator rather than a pedantry.

🟢 🆕 **The addition that changes the pitch: Article 4's staff AI-literacy duty is already in force and was
not deferred.** So the EMEA conversation is not "prepare for a 2027 deadline" — which invites delay — but
"there is a duty you are already subject to, and a 14-month window on the larger one". 🔵 **Two deadlines, two
sales: literacy now, high-risk conformity by Dec 2027.** The first funds the second.



### 🔴 🆕 p99 amendment to T4 — the procedure is CLOSED, the regulation has a number, and the near deadline is **53 days** out

🟢 **Pass 98 left exactly one thing open here: whether the Council had formally adopted the
postponement. It had.** The full chain, from a query aimed at the **procedure** rather than the date:

| step | date |
|---|---|
| trilogue fails | 28 April 2026 |
| provisional political agreement | **6 May 2026** (one source: 7 May) |
| Member State representatives confirm in Council | 13 May 2026 |
| European Parliament formally endorses | 🟢 **16 June 2026** |
| 🟢 **Council formally adopts** | 🟢 **29 June 2026** |
| published as 🟢 **Regulation (EU) 2026/1744**, Official Journal | 24 July 2026 |
| 🟢 **in force** | 🟢 **27 July 2026** |

🔴 **And this is where `T4`'s thesis earns its fourth confirmation.** The Omnibus moved the **far**
deadline and **left the near one standing:**

| limb | applies from | postponed? |
|---|---|---|
| prohibitions (🔴 **emotion recognition in education**) + AI literacy | **2 Feb 2025** | 🟢 **no** |
| **Article 50 transparency** | **2 Aug 2026** | 🟢 **no** |
| 🔴 **Article 50(2) machine-readable marking** — GenAI already on the market before 2 Aug 2026 | 🔴 **2 December 2026** | 🟢 **grace period only** |
| **Annex III high-risk** — admissions screening, **remote exam proctoring**, assessment | **2 Dec 2027** | 🔴 **yes** |
| Annex I embedded | 2 Aug 2028 | 🔴 yes |

🔵 **So the limb that binds an EMEA education engagement FIRST is `2026-12-02`, fifty-three days from
this pass — and it is not the date the market is discussing.** 🟢 **This base holds four tested
artefacts for exactly that limb**: `compose/code/aiact-50-2-marking/`, `aiact-50-2-pack/`,
`aiact-50-2-spans/`, `aiact-50-2-exposure/`.

🔴 **The conflation `T4` has tracked since pass 94 is now worse, not better:** every source discussing
"the delay" points at **Dec 2027**, which is correct and irrelevant to a vendor whose generative
feature shipped before August 2026. 🔵 **The sales sentence is: the delay you read about does not
cover the clause that binds you in eight weeks.**

🟡 **Grade: search-summary, four or more independent sources agreeing on the dates and the regulation
number.** 🔴 **`eur-lex.europa.eu` remains refused from this sandbox, so the Official Journal text was
NOT read** — recorded as a refusal, per pass 98's own instruction not to re-confirm the date a fifth
time in place of reading the instrument.

### 🟢 🆕 p94 amendment to T4 — the wrong date is a **conflation**, and that changes the sales motion

🔴 **Sixth instance, and pass 94 stopped counting and found the mechanism.** 2 August 2026 **was** the
Annex III date. The **Digital Omnibus on AI — `Regulation (EU) 2026/1744`** (European Parliament 16 Jun
2026, Council 29 Jun 2026, signed 8 Jul 2026; 🔴 **sources conflict on OJ publication, 24 Jul vs entry into
force 27 Jul 2026, and neither was read primary**) moved it to **2 December 2027**, with Annex I to
2 Aug 2028. 🟢 **But 2 August 2026 did not become an empty date — it became an Article 50 date.**

| limb | date | so what |
|---|---|---|
| Annex III high-risk, education included (point 3(b)) | **2 Dec 2027** | the big build, 14 months out |
| **Article 50** transparency | 🔴 **conflicting**: from **2 Aug 2026**; Art. 50(2) synthetic-content marking **2 Dec 2026**; **2 Feb 2027** for systems already on the market | **live or nearly live** |
| **Article 4** staff AI-literacy duty | **already in force** | 🟢 sells now |
| **Article 5** — **emotion recognition in education** | 🟢 **prohibited since 2 Feb 2025** | 🔴 **enforceable today** |

🔵 **So the market's "August 2026" is a stale date that collides with a live one, which is why correcting it
flatly has never worked.** 🟢 **The move is a question, not a correction:** *which article do you mean?*
Annex III → they are 16 months early and will under-build; Article 50 → they are right, and probably
unprepared.

🔴 **And the obligation none of the six sources mentioned is the only one already enforceable: emotion
recognition in education is prohibited outright.** 🔵 **That is not a 2027 planning item — it is a feature
audit of whatever the client already runs**, because engagement detection, attention tracking and affect
inference ship switched on in proctoring and "engagement analytics" products. **It is also the cheapest
possible opening deliverable in EMEA: a one-week inventory against a prohibition that is already law.**

### 🟡 🆕 p96 amendment to T4 — a seventh instance, one conflict narrowed 4-to-0, and one conflict that got worse

- 🔴 **Seventh independent instance of the wrong date.** A current EU-AI-Act-for-education guide returned
  this pass states *"requirements for high-risk AI systems apply from August 2026."* 🟢 **Seven instances
  across seven passes. The claim that the wrong date is the market's majority reading survives another
  independent sample** — and it is now the longest-running empirical claim in this file.
- 🟡 **The OJ-vs-entry-into-force conflict narrows 4-to-0.** Pass 94 flagged *"24 Jul vs entry into force
  27 Jul 2026, and neither was read primary"*. 🟢 **Two independent search rounds over different source
  sets returned `in force 27 July 2026` four times and `24 Jul` zero times.** 🔴 **Still not primary** —
  `digital-strategy.ec.europa.eu` and `EUR-Lex` are unreachable from this environment.
- 🔴 **The Article 50(2) conflict got WORSE, and that is worth saying rather than smoothing.** This file's
  table reads *"Art. 50(2) synthetic-content marking **2 Dec 2026**; **2 Feb 2027** for systems already on
  the market"*. 🔴 **This pass's sources assign 2 Dec 2026 TO systems already on the market** — the
  opposite allocation of the same date. 🔵 **Two readings, opposite assignments, neither primary. Recorded
  as unresolved and sharper, not resolved** — and 🔴 **Article 50 is the limb that actually binds in EMEA
  today, so the ambiguity sits on the live obligation rather than the deferred one.**
- 🟢 **And the sales consequence of T4 is now a different sentence, because of `T15`.** The EMEA
  conversation was *"literacy now, high-risk conformity by Dec 2027"*. 🟢 **It is still that — but the
  high-risk conformity work has a buyer with a live deadline, and that buyer is in APAC.** See `T15`.


### 🟢 🆕 p100 amendment to T4 — the duty got a SAFE HARBOUR and its first NARROWING, and one of them scopes LMS work exactly

🟡 **All four rows below are search-summary grade; `digital-strategy.ec.europa.eu` and `eur-lex.europa.eu`
remain refused and were not re-probed this pass.**

| what landed | date | why it changes the offer |
|---|---|---|
| 🟢 Commission **confirmed the Transparency Code of Practice as adequate** | July 2026 | 🟢 **There is now a named route to demonstrate Article 50 compliance** — voluntary, but it converts *"prove you marked it"* into *"adhere to this and show you did"* |
| 🟢 **Final** Commission guidelines on Article 50 transparency published | July 2026 | the guidance is no longer draft, so scoping decisions taken against it are defensible |
| 🟢 **AI-generated TRANSLATIONS exempt** as *"standard editing"* | July 2026 guidelines | 🔵 **This is the LMS scoping question answered**: translating course material does **not** trigger marking |
| 🔴 **Summaries and substantive rewrites are NOT exempt** | same | 🔴 **And this is the other half**: an LMS feature that *summarises* a reading, or rewrites it for a reading level, **does** trigger it |
| 🔴 Enforcement sits with **national market surveillance authorities** | Art. 50 applicable **2 Aug 2026** | 🔴 **No specific national body was named by any source this pass** — recorded as a measured zero, re-registered as a lead |

🔵 **Why the translation/summary split is the most commercially useful line in this file right now.**
Every LMS AI feature set this KB has catalogued contains both operations, usually in one menu.
🟢 **Translate-a-course is out of scope; summarise-a-chapter and simplify-for-reading-level are in
it** — and the second pair is precisely the accessibility and differentiation feature an education
client asks for first. 🔴 **So the marking obligation lands on the feature a school most wants, and
the exemption lands on the one it mentions least.** 🟢 **Costed as `P100-B`.**

🔴 **The clock, restated because it is the only item in this file that expires:** GenAI **already on
the market** before 2 Aug 2026 must satisfy Article 50(2) machine-readable marking by
🔴 **2 December 2026 — 53 days from this pass.** 🔴 **Systems placed on the market on or after
2 Aug 2026 have NO grace period at all**, which is the half that four passes of this file never
stated.

## T5 — Generators are saturated; the checker gap is now **half closed**, and the remaining half is sharper

🔴 **What this KB published for five passes:** *"a targeted search for AI accessibility/alignment checkers in
education returned nothing usable"* and *"the only accessibility checker found is `UDOIT` — GPL-3.0, and not
AI-driven."* 🟢 **The accessibility half is FALSE and was falsified on the first targeted query this pass.**
Three permissive, AI-driven WCAG checkers verified from the payload: `tomaszboloz/WCAG-Accessibility-Skills`
(MIT), `Community-Access/accessibility-agents` (MIT), `9mtm/WCAG-Checker` (MIT, covers **PDF** as well as web).

🔵 **Why the shelf missed them, and this is the transferable part: the query named the industry.** Searching
*"accessibility checker **education**"* returns LMS plugins, and the LMS plugin in this space is GPL. Dropping
the industry term and searching the **standard** — WCAG — returns permissive, AI-driven tools immediately.
🟢 **A compliance tool is named after the standard it enforces, not the sector that buys it.** This is `P870`
(re-point the vocabulary) in a new guise, and it is the second time this pass that changing the query word
rather than the query target discharged a long-standing gap — the other being **CBSE** for India.

🔴 **What still does not exist: an instructional-alignment checker under a permissive grant with usable
evidence.** The narrowed specification, which is more useful than the old blanket claim:

| candidate | why it does not close the gap |
|---|---|
| `nsip/curriculum-mapper` (Apache-2.0, Australia) | 🔴 **archived, read-only**, keyword-based not semantic |
| `learning-commons-org/evaluators` | 🔴 **the corpora that make it evidence-backed are CC-BY-NC-SA** — see `T6` |
| `Zion-support/curriculum-alignment-checker` | 🔴 no licence payload in 24 filenames; self-describes as batch-generated |
| `lovejzzz/CourseMapper` | 🔴 no licence payload in 24 filenames; own README logs attribution failures |

🔵 **A checker remains the easier enterprise sale** — it does not displace the educator, it evidences
compliance. With North America at ~10 % guideline coverage and WCAG/508 exposure, **the accessibility half can
now be composed rather than built, and the alignment half is a clean, specified build.**

### 🟢 🆕 p96 amendment to T5 — the remaining half is not a supply gap, it is a **wiring** gap, and that is a cheaper problem

🔴 **T5's remaining half has been stated five times as a supply absence:** *"nothing permissive audits
whether content meets a learning outcome with usable evidence."* 🟢 **Pass 96 found the technique, fully
permissive, published in 2026 — on the first query that named *rubrics* instead of education** (`P955`, a
fourth consecutive pass):

| layer | repo | grant |
|---|---|---|
| **generate** a rubric from an instruction | [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) *(ACL 2026 long)* | 🟢 **MIT** |
| **judge** against weighted, tiered criteria with an interpretable verdict | [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) — 50+ rubric sets, criteria **critical / core / important / highlight**, A/B-swap debiasing | 🟢 **Apache-2.0** |
| **calibrate the judge against human markers** | [`planepig/rubricbench`](https://github.com/planepig/rubricbench) — **1 147 pairwise comparisons**, expert-annotated atomic rubrics, scores reasoning as well as verdict | 🟢 **MIT** |

🔴 **What none of them does is bind a rubric to a published curriculum standard.** 🟢 **And this KB holds
that end already:** `bncc-dev/bncc-pacotes` (MIT code + CC BY 4.0 data) exposes **1 721 verified BNCC
objectives** through **7 MCP tools** with per-record provenance, and `learning-commons-org/evaluators`
ships **MIT** judging code against research-backed educational rubrics.

🔵 **So T5's remaining half is restated, and the restatement halves the cost.** A supply gap means *find or
build the capability*. 🟢 **A wiring gap means the capability exists under grants a studio can bill
against, and the deliverable is an integration** — which is a scoped engagement, not a research bet.
**`Gap 379`; specified and costed as `P96-A` in `compose/patterns.md`.**

🟢 **One subsidiary result worth carrying into T6.** `rubricbench`'s **1 147 expert-annotated comparisons
are MIT** — **the first permissive annotated comparison corpus this KB has found.** 🔴 **T6's finding
stands for education corpora** (`evaluators`' annotated CLEAR and PERSUADE 2.0 are **CC-BY-NC-SA-4.0**, and
they are the valuable part). 🔵 **But for *calibrating a judge* rather than *scoring a student*, the domain
mismatch costs less than the NC clause does** — so `rubricbench` is the row that lets a paid deliverable
show its marker agrees with humans without licensing someone else's student essays.


## T6 — 🆕 In the checker and dataset tier, the grant splits along code / prompt / corpus lines — and the permissive part is not the valuable part

🟢 **The most commercially consequential finding of this pass.**
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) ships **one**
`LICENSE.md` granting **four different things**:

| layer | grant | usable in a paid deliverable? |
|---|---|---|
| evaluator **code** | **MIT** | 🟢 yes |
| **prompts and settings** | **CC-BY-4.0** | 🟢 yes, with attribution |
| **Annotated CLEAR Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |
| **Annotated PERSUADE 2.0 Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |

🔴 **The non-commercial clause sits precisely on the annotated corpora — which are what make it an
evidence-backed rubric evaluator rather than a prompt template.** 🔵 **So the question in this tier is not
"is it permissive" but "is the permissive part the valuable part". Here it is not.**

🟢 **A second shape, same lesson:** `learning-commons-org/knowledge-graph` licenses **per dataset and per
download** — `Open` / `Open + Gated` / `Gated` — through a platform catalogue, and states in terms that its
gated content is **not** covered by the CC licences the same file references. **A repo-root licence read
cannot resolve a data-layer grant.**

🔵 **Generalisation worth carrying to every other industry KB: as AI work moves from code to
code-plus-evaluation-data, licence risk migrates from the repository to the corpus, and corpora are where
non-commercial clauses live.** Pass 90 found a 2-way split (`microsoft/autogen`: docs CC-BY, code MIT) and it
was benign. This is a 4-way split and it is binding.

## T7 — 🆕 The regulatory frontier has moved from *regulating AI systems* to *mandating AI instruction* — and that is a services market, not a compliance cost

🟢 🆕 **p93: FIVE jurisdictions now compel AI *teaching* — and the fifth one resolves a misattribution this
KB recorded rather than used.**

| jurisdiction | instrument | from | reach |
|---|---|---|---|
| 🇨🇳 China | Ministry of Education — compulsory from **age six**, tiered primary→secondary | **Sep 2025** | **≥ 8 hours per year, nationwide** |
| 🇸🇬 Singapore | Ministry of Education — AI literacy across curriculum, co-curriculum and self-directed learning, with developmental milestones | announced **Mar 2026** | **all schools by 2027**, via Student Learning Space + IMDA modules |
| 🇮🇳 India | CBSE — *Computational Thinking and AI*, **Classes 3–8**, notification **9 Apr 2026** | session **2026-27** | CBSE-affiliated schools; aligned to NEP 2020 / NCFSE 2023 |
| 🇪🇺 EU | **AI Act Article 4** — staff AI-literacy duty | 🟢 **in force now** | every institution deploying an AI system |
| 🆕 p93 🇦🇪 UAE | **Cabinet-approved AI curriculum**, compulsory **kindergarten → Grade 12** in government schools; seven strands (foundational concepts · data and algorithms · software use · ethical awareness · real-world applications · innovation and project design · policies and community engagement) | announced **May 2025** (Sheikh Mohammed bin Rashid Al Maktoum); taught inside *Computing, Creative Design and Innovation* in **2025-26** | 🟢 **All government schools.** 🟡 Standalone-subject timing (*"Artificial Intelligence and Technology"*, 2026-27) and **private-school scope are contradicted between sources** and are **not** recorded as settled; one report of a **Sep 2026** cabinet approval extending it to private schools with **22 000 teachers trained** is **single-source and not used.** |

🔵 **Why this is a different business from everything else in this file.** A risk-classification regime
creates work that is defensive, legal-led and priced as compliance. A **curriculum mandate creates work that
is constructive, educator-led and priced as delivery**: someone must write the material, localise it to each
jurisdiction's scope and hours, train the teachers who have never taught it, and assess it.
🔴 **And the supply is thin where it matters.** The permissive AI-literacy curricula that exist
(`microsoft/ai-agents-for-beginners`, `rohitg00/ai-engineering-from-scratch`,
`pguso/agents-from-scratch`, `huggingface/agents-course` — all MIT or Apache-2.0) are written for **adult
developers**, not for **eight-year-olds in Class 3**. 🟢 **Nothing on this shelf addresses the primary-school
mandate that China has already implemented and India starts this session.**
🔴 **And curriculum is content, so it is where NC clauses cluster** — `cccareers/open-source-curriculum` is
**CC-BY-NC-SA**, unusable in a paid deliverable.

🔵 **This also corrects a sentence this KB carried for several passes.** The shelf said *"Singapore and Japan
stay deliberately voluntary"*. 🟢 **True of Singapore's position on regulating AI systems; false of its
position on AI in schools.** Voluntary regulation and mandated curriculum are different axes, and conflating
them understated the region's most purchasable commitment.

## T8 — 🆕 APAC's AI statutes name education **high-risk by sector**, and that is a different market from the curriculum mandates

🟢 **Three binding instruments arrived or took effect in APAC and two name education explicitly:**
**South Korea's AI Basic Act** (in force **22 Jan 2026**, with a signalled **one-year penalty grace
period**), **Vietnam's standalone AI statute** — the first in Southeast Asia — which puts **education
alongside finance and healthcare as high-risk**, with **pre-deployment registration in a National AI
Database**, conformity assessment, mandatory human oversight and **72-hour incident reporting**, compliance
due **Sep 2027**; and **Taiwan's AI Basic Act** (Dec 2025).

🟢 🆕 **p93 — the non-convergence claim is now corroborated by an independent analyst, in stronger words
than this KB used.** Pass 92 wrote that *"APAC compliance" is not a product* because the region does not
converge. Forrester's 2026 outlook states that a common APAC-wide AI legislative framework **"will remain a
distant dream"**, noting Singapore promoting responsible AI through mature *guidelines* while China
legislates against algorithmic misconduct, and that regional instruments such as the **ASEAN Guide on AI
Governance and Ethics** are still early-stage. 🔵 **A finding this KB derived from counting statutes is
the same finding a research house derived from watching legislatures. The sell is per-jurisdiction, and it
will stay per-jurisdiction.**

🔵 **Why this is a separate trend from `T7` and not an extension of it.** `T7` is about jurisdictions
*mandating that AI be taught* — a **content and curriculum** market. This is about jurisdictions *regulating
the AI an institution runs* — a **governance, logging and audit** market. 🔴 **Same region, different buyer,
different deliverable, different skill set.** A studio that reads them as one offer will mis-staff both.

🔴 **And the region does not converge, so it cannot be priced as one.** Korea and Vietnam are
comprehensive-and-binding; **Japan is deliberately voluntary and innovation-first**; Singapore's frameworks
are largely voluntary; India and Australia still lean on sectoral and privacy law. 🔵 **"APAC AI
compliance" is not a product.** Per-jurisdiction scoping is the product.

🟢 **The one transferable design constraint, and it is an architecture decision rather than a policy one:**
**72-hour incident reporting** means logging, alerting and a named owner have to be in the system from the
first sprint. 🔵 **It converges with the EU's Article 27 FRIA and with Oklahoma's and Maryland's
human-oversight floors** — three regions, three instruments, **one engineering requirement: a human-decision
gate with an audit trail.** 🟢 **Build that once and it sells in all three.** That is the single most
reusable finding in this file.

## T9 — 🆕 The regulated activity is **assessment**, and it is being adopted at sector scale right now

🟢 **Jisc reported early findings in May 2026 from year-long AI marking-and-feedback pilots across 38 UK
colleges and universities** *(search-summary)*, and analysts name assessment and grading the
fastest-growing AI-in-education category — driven, circularly, by student AI use.

🔴 **The EU AI Act's Annex III catches exactly this**: evaluating learning outcomes, screening applicants,
and monitoring candidates during examinations. 🔴 **So the fastest-growing category is the regulated
category**, and the shelf should be read accordingly:

- 🟢 The permissive assessment tier is unusually strong — **`Numbas` (Apache-2.0)**, **`Submitty` (BSD)**,
  **`otter-grader` / `nbgrader` (BSD)**, **`webtech-network/autograder` (Apache-2.0)**.
- 🔴 **The best full QTI platform is copyleft, and this pass corrected its family**: `oat-sa/tao-core` is
  **GPL-2.0**, not the LGPL this KB published last pass. The licence question on an assessment engagement is
  therefore sharper than it looked a day ago.
- 🟢 **`fborrasumh/tutoria` (MIT, Spain)** makes the teacher validate the lesson before the student sees it.
  🔵 **Human oversight expressed as a product step rather than a policy document is the most saleable
  compliance primitive in this industry** — and `AyudantIA` at UC Chile is the same idea bought at scale.
- 🔴 **Trust, not capability, is the stated barrier**: learners and parents remain sceptical of automated
  marking, and high-stakes assessment still needs teacher review. 🔵 **So "AI marks it" is not the product.
  "AI drafts it, a teacher signs it, and the trail proves it" is.**

### 🆕 p93 amendment to T9 — the EMEA instrument that landed is **guidance for teachers**, and it is dated March 2026, not June

🟢 🆕 **p93 adds the instrument, and corrects a date before it entered this file.** A newsletter summary
reported that the European Commission updated its *ethical guidelines on AI in education* **"on 9 June"**.
🔴 **It did not.** The update was published **5 March 2026**, as one of **four** Digital Education Action
Plan guideline sets released together (the others covering digital literacy and disinformation, selecting
digital content, and teaching informatics).

| property | the 2026 update |
|---|---|
| date | 🟢 **5 March 2026** |
| supersedes | the **2022** version, written by the Expert Group on AI and Data in Education and Training |
| author | the **Working Group on the Ethical Use of AI and Data in Education**, convened through the **European Digital Education Hub** |
| structure | three parts — founding principles and legal framing · guiding questions with scenarios · support resources — plus an **updated AI and data glossary** |
| audience | 🟢 **teachers and school leadership**, not ministries |
| stated driver | the growth of AI use in schools after generative AI, **and the AI Act entering into force** |
| languages | English first, with translation into all official EU languages during spring 2026 |

🔵 **Why the audience is the finding.** The Commission's answer to Article 4 is **a document for
teachers**, which is a statement about where the obligation lands: **on the institution's staff, as
capability.** 🟢 **That is purchasable** — the duty is on the deployer, the deadline is now, and the
official material is guidance rather than a product. 🔴 **And the same commentary stream that reported
this update is where `T4`'s wrong date showed up for the fifth time**, which is the practical shape of this
market: correct subject, wrong deadline, confident tone.

### 🟢 🆕 p95 amendment to T9 — the buyer has now said it out loud

🟢 **`T9` has argued for five passes that assessment is the regulated activity, from the regulator's side.
Pass 95 found the same claim from the buyer's side.** Brazil's **MEC** published **「Inteligência Artificial
na Educação Básica」** on **2026-04-08** (with UNESCO cooperation, project **914BRZ1157**), and among the
teacher-support uses it names explicitly is **`correção automatizada e detecção de plágio`** — automated
correction and plagiarism detection.

🔵 **A national education ministry putting automated correction on its own list of endorsed teacher uses is
a procurement signal, not a policy observation.** 🟢 **It converts the scoring stack from a technical thesis
into a line item**, and it lands in the region where this KB already holds the deepest curriculum open-data
rows (`bncc-dev`) and a classroom-proven automated-feedback platform (`mumuki`, AGPL-3.0, Argentina).
🔴 **And it sharpens `Gap 372` rather than easing it**: the demand is now explicit while the permissive
production scorer still does not exist.

🟡 **Evidence grade: search-summary** — `www.gov.br` is egress-blocked, so the two official PDFs are
identified and unread. **The document is orientative, not binding.**

## T10 — 🆕 In the learner-model tier, the **permissive** option and the **explainable** option turn out to be the same one

🟢 **Pass 92 opened this tier with one library** (`pykt-team/pykt-toolkit`, deep knowledge tracing) and
wrote that the learner model had arrived. 🟢 **Pass 93 found the rest of the stack by naming three more
techniques, and the structure inside it is the trend:**

| technique | repo | grant | ★ | what it emits |
|---|---|---|---|---|
| Bayesian Knowledge Tracing | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** | 282 | 🟢 four interpretable parameters per skill — prior, learn, slip, guess |
| Item Response Theory | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) · [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · **MIT** | 173 · 126 | 🟢 item difficulty and discrimination, learner ability, on one scale |
| Computerized Adaptive Testing | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** | 153 | 🟢 the next item, and a defensible stopping rule |
| review scheduling | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** | 506 | 🟢 when the learner will forget |
| deep knowledge tracing | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | ~430 | 🟡 a predicted probability from a trained network |

🔵 **The trend is the coincidence of three properties that usually trade off against each other.** The
classical psychometric layer is simultaneously (a) **permissive** — MIT and BSD throughout, (b) **more
production-worn** — `catsim` carries 877 commits against `pykt-toolkit`'s research-benchmark posture, and
(c) **the only part of the tier that produces an artefact you can put in front of a regulator.**

🔴 **And (c) is the one that decides an engagement.** Under the EU AI Act's Annex III, assessing learning
outcomes is high-risk and owes an explanation to the person assessed. **A 2-parameter logistic item curve
is an explanation. A per-skill slip-and-guess probability is an explanation. An LSTM activation is not.**
🟢 **So the advice inverts the usual instinct to reach for the newest model: in this tier, the older
mathematics is the compliant choice, and it is also the cheaper and better-licensed one.**

🟢 **The seams are named by the tools, not by this KB** — `catsim`'s README states outright that
*"catsim does not implement item parameter estimation"* and points at `py-irt` and `girth`. 🔵 **A stack
whose boundaries its own authors document is a different risk than one an integrator invents.** Costed as
`P93-A`.

🔴 **What is still missing, and it is not a library.** Nothing found this pass wires any of this into an
agent's turn (`Gap 369`), and there is **no permissive production-grade automated essay scorer at all**
(`Gap 372`) — so the tier covers **structured** assessment well and **open-response** assessment not at
all. 🔵 **Which is to say it covers the part the EU names high-risk least well.**

## T11 — 🆕 Grounding a curriculum-aligned tutor in verified standards data is now **measured**, and the number is 31.9 % → 0.2 %

🟢 **This KB has argued for ninety passes that the interoperability and standards tier is where the value
is. It has never had a number for it. It does now, and the number is somebody else's, published,
reproducible and adversarial to its own publisher's interest.**

[`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) measures LLM hallucination against
Brazil's national curriculum base. Its grounding study — **8 models, 300 items**:

| condition | hallucination rate |
|---|---|
| 🔴 no source in context | **31.9 %** |
| 🟢 **dataset in the prompt** | **0.2 %** |
| 🟡 **querying the MCP server** | **2.3 %** |

🔵 **Three readings, in descending order of how much they should change what a studio builds.**

1. 🟢 **Grounding is worth ~160× on this task.** Not "improves accuracy" — **31.9 % → 0.2 %**. For any
   deliverable that cites curriculum codes to a teacher, the standards dataset is not an enhancement, it
   is the product's correctness boundary.
2. 🔴 **The MCP route is ten times worse than embedding the data** (2.3 % vs 0.2 %), while still ~14×
   better than nothing. 🔵 **That is an architecture decision with evidence behind it: for curriculum
   alignment, ship the dataset in the context, and keep the tool call for what the dataset cannot
   answer.** It also explains why `bncc-dev/bncc-pacotes` embeds the data inside its MCP server rather
   than calling home.
3. 🔴 **Ungrounded faithfulness varies from 88 % to 3 % across models**, so "which model" is a much weaker
   lever than "is the source in the context". 🔵 **Model selection is the cheap question; grounding is
   the expensive one, and only one of them is usually on the agenda.**

🟡 **Two reasons to cite this carefully, both from the repository itself.** 🟢 **Its README declares a
conflict of interest in its own words** — *"Vale declarar o conflito de interesse: a Profy opera produtos
que usam LLMs sobre a BNCC"* — and publishes methodology, items, raw responses and judgments so the
numbers can be recalculated. 🔵 **A disclosed conflict with reproducible workings is a better evidentiary
position than most vendor benchmarks on this shelf.** 🔴 **But its own two surfaces disagree on the
corpus size:** the repository description says **15 300 responses from 17 models**, while the README
describes the official round as **19 models × 900 = 17 100 published raw responses**.
🔵 **Cite the grounding percentages, which are the study's own headline, and do not cite a corpus size
from the description** — this is `compose/code/description-drift-audit/`'s shape appearing inside a source
this pass otherwise rates highly.

🔴 **Generalisation limit, stated.** One benchmark, one curriculum, one language, 300 items. **The
direction is almost certainly general and the magnitude is not.** Use it to justify the architecture, not
to promise a client 0.2 %.

## T12 — 🆕 p94 In a federal system the instrument is **subnational**, and this is now a predictive rule rather than an observation

🟢 **Pass 93 observed it in Canada. Pass 94 used it to find Mexico's instrument on the first attempt. That
is the difference between a note and a method.**

| federation | national instrument | where the instrument actually is |
|---|---|---|
| **Canada** | 🔴 none | BC (ministerial guidance, K-12 resources to May 2026, Jan 2026 post-secondary principles) · Alberta (three-year agreement with **Amii**) · 🔴 **Ontario: none, and its largest board publicly asked the ministry for one** |
| **Mexico** | 🔴 none; a **PT bill of 29 Apr 2026** sits in the Education Committee | 🟢 **Estado de México: reform to Art. 61 of the state `Ley de Educación`** — upper-secondary and higher education must promote *responsible, ethical and gradual* use of AI. 🔴 Promulgation date unresolved (Apr 2026 per one source; a 31 Jan–15 Jul 2026 window per another) |
| **United States** | 🟡 **two bills of the same shape** — `H.R. 8747` (reported, not enacted) and `S. 5225` — both make AI instruction an **eligible use of existing federal K-12 funds** | 🟢 **State law**: Idaho SB 1227, Oklahoma, Maryland SB 720; plus NYC's district-level Traffic Light Framework |

🔵 **Three consequences, all operational.**

1. 🔴 **A national query reports an empty world.** Five passes of this KB recorded "Mexico: no AI law" and
   every one of them was accurate and useless. 🟢 **The fix is `P955` applied to jurisdictions: name the
   instrument and the level, not the country.**
2. 🟢 **A federal market is a repeatable one.** A deliverable built for one state or province fits the next,
   because the instruments converge in content — *responsible use*, *teacher review*, *local policy*, *a
   designated coordinator* — even when they differ in form.
3. 🔵 **And the US federal shape tells you who signs.** When the federal lever is **fund eligibility**
   rather than mandate, 🟢 **the buyer is the district administrator with a Title IV-A line, not a federal
   programme office** — and Maryland has already named that person: **an AI coordinator per local school
   system**.

🟡 **The limit, stated:** three federations, one of them (the US) known since pass 90. 🔴 **Quebec, Brazil's
states and India's states are untested**, and Brazil is the interesting one — it has a national curriculum
base as audited open data (`T11`) **and** 26 states, so the rule predicts state-level AI instruments there
that this KB has never looked for.

## T13 — 🆕 p94 The permissive supply for regulated assessment is the **evidence layer**, not the scorer

🟢 **This trend exists because `Gap 372` was stated too broadly for one pass and is now stated correctly.**

Pass 93: *"there is no production-grade permissive AES library in this industry"* — one 2★
Apache-by-reference research repo was the whole supply, for the activity the AI Act names high-risk most
explicitly. 🟢 **Pass 94 read the payloads and the picture inverted along a seam nobody had drawn:**

| layer | what a regulated deliverable needs it for | permissive supply |
|---|---|---|
| **the scorer** | producing a grade | 🔴 **absent.** The production code is AGPL-3.0 — `openedx/ease`, `openedx/edx-ora2` |
| **the validation and fairness harness** | 🟢 **the artefact the regulator and the appeal process actually consume** | 🟢 **present and mature** — `EducationalTestingService/rsmtool` (Apache-2.0, 2 916 commits), `skll` (BSD-3) |
| **open-response grading with LMS reach** | getting a grade back into the platform the client runs | 🟢 **`HASKI-RAK/NodeGrade`** (MIT, LTI 1.1/1.3, 421 commits) |
| **the explanation** | 🟢 Annex III owes the assessed person a reason | 🟢 the psychometric tier — BKT / IRT / CAT, all MIT or BSD (`T10`) |

🔵 **The commercial reading is the opposite of the obvious one.** The scorer is the part a client can buy
from a vendor, and the part that is cheapest to replace. 🟢 **The validity argument, the fairness analysis
and the explanation are the parts nobody sells as a product, that every regulated deployment needs, and
that are available under Apache and BSD from the house that runs TOEFL and the GRE.** 🔴 **Which is why
"we cannot do automated scoring, there is no open scorer" was the wrong conclusion**: the open supply
covers the defensible half, and the half it does not cover is the half with a market price.

🔴 **And a caution that belongs in this trend rather than a footnote.** The same publisher ships
**GPL-2.0** in `factor_analyzer` — a factor-analysis library of exactly the kind a scoring pipeline imports
without reading (`P975`). 🔵 **In this tier the licence audit is a per-dependency job, not a per-vendor
one.**

### 🟢 🆕 p95 amendment to T13 — the claim is unchanged in direction and three measurements stronger

🔴 **Pass 94 asserted that the research scoring supply was thin. Pass 95 probed it and it is worse than
thin — it is ungranted.** The three open-response candidates the literature names:

| candidate | claim | payload |
|---|---|---|
| [`edgresearch/code-automaticgrading-2022`](https://github.com/edgresearch/code-automaticgrading-2022) (**GradeAid**) | published ASAG framework, code released | 🔴 **CC BY-SA 4.0**, 20 130 B — **a content licence with a ShareAlike obligation, applied to software.** No patent or linking language; CC advises against CC for code |
| [`datalab912/RATASv1`](https://github.com/datalab912/RATASv1) | *"the authors publicly release all code"* | 🔴 **no licence payload in 8 filenames** |
| [`emorynlp/llm-grading`](https://github.com/emorynlp/llm-grading) | *"an open-source auto-grading toolkit"* | 🔴 **no licence payload in 8 filenames** |

🔴 **`P981`: "we publicly release our code" in a paper is not a grant** — and an ungranted repository is, by
copyright default, **all rights reserved**. 🔵 **Because this industry's scoring supply is overwhelmingly
academic, the defect is systematic**: the sentence that signals openness in a paper and the legal position
of the artefact point in opposite directions.

🟢 **So `T13` holds in its strong form.** The permissive supply for regulated open-response scoring is the
**validation** layer (`rsmtool` Apache-2.0, `skll` BSD-3); the **production** scoring code is copyleft
(`openedx/ease`, `openedx/edx-ora2`, AGPL-3.0); the **research** code is ungranted or CC-licensed.
**Score behind a service boundary; validate with Apache/BSD.**

🟢 **And one genuine addition at an adjacent layer, which `T13` must not be read as covering.**
[`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) is **BSD-3-Clause**, `v7.0.0`, UC
Berkeley, Canvas- and Gradescope-native. 🔴 **It grades code against tests, not constructed responses**, so
it leaves `Gap 372` exactly where it was. 🟢 **What it changes is that the automated-feedback layer's only
classroom-proven row is no longer AGPL-only** — which moves a programming-assessment deliverable from
*integrate across a service boundary* to *fork and own*.

## T14 — 🆕 p95 The curriculum mandates split by education LEVEL, and the higher-education limb is a different market

🟢 **Every curriculum mandate this KB has recorded until now binds schools.** China, Singapore, the UAE's
K→G12 programme, Mexico's Edomex reform, the EU's Article 4 literacy duty — **the buyer is a ministry of
education, the unit is a school system, and the procurement cycle is a national programme.**

🟢 **Pakistan's HEC notification (February 2026, effective academic session 2026) binds universities**: a
**3-credit AI course in every undergraduate and postgraduate degree**, public and private, deliverable as
an elective, interdisciplinary or supporting subject. 🔵 **That is the same regulatory instrument type
pointed at an entirely different market.**

| | the K-12 limb | 🆕 **the higher-education limb** |
|---|---|---|
| buyer | ministry / national programme office | 🟢 **the institution itself** — provost, registrar, faculty development |
| unit of sale | one programme, many schools | 🟢 **one institution, repeated** — and there are hundreds |
| procurement | public tender, multi-year | 🟢 **institutional budget, annual** |
| the artefact | curriculum, teacher training, content packaging | 🟢 **syllabus + LMS delivery + disclosure workflow + faculty training** |
| the platform | whatever the ministry runs | 🟢 **the university's own LMS — Moodle, Canvas, Sakai, OpenOLAT, Artemis** |
| examples here | China, Singapore, UAE, Edomex, EU Art. 4 | 🟢 **Pakistan (binding)**; India (in drafting); Quebec & Brazil (higher-ed frameworks) |

🟢 **Why this is a trend and not a single data point.** Three other jurisdictions in this KB already carry a
higher-education-specific instrument: **Quebec's `Cadre de référence` on deploying AI in higher education
(Aug 2025)**, **Brazil's CNE draft guidelines, which include a higher-education chapter (March 2026)**, and
**India's AICTE/UGC undergraduate AI curriculum, in drafting with Nasscom and a stated ~6-month horizon**.
🔵 **Pakistan is the first to make it binding, not the first to aim at the level.**

🟢 **And the recurring-revenue shape is in Pakistan's draft policy rather than its mandate.** The **August
2026 draft** asks universities to **write their own institutional rules**, **requires disclosure of AI
use**, **requires annual AI training for faculty, students and staff**, and **directs AI literacy into
curricula within two years**. 🔵 **A 3-credit course is one syllabus delivered once. "Annual training for
all staff" and "write your own policy" are deliverables that recur per institution per year** — which is
the difference between a content engagement and a retained one.

🔵 **What this changes in the shelf.** The K-12 limb pulled this KB toward curriculum data and content
packaging (`P91-G`, the `bncc-dev` rows, `Gap 367`'s missing K-5 curriculum). 🟢 **The higher-education limb
pulls toward the university platform tier this KB is already strongest in** — `Artemis` (MIT, with Iris,
Athena and Hyperion already built), `Sakai` (ECL-2.0), `OpenOLAT` (Apache-2.0) — **plus the disclosure and
assessment-integrity workflow the draft policy names.** 🟢 Costed as `P95-A` in `compose/patterns.md`.

🔴 **The honest limit.** Pakistan's mandate is **read at search-summary grade** from Pakistani press
(APP, The News, ProPakistani, Digital Pakistan) with consistent dates and content across outlets; **the HEC
notification itself was not read**, and the August draft is explicitly a **draft**. 🟡 **And a vocabulary
note: Pakistan is bucketed APAC here under this task's five-value region field**, which hides that it is a
South Asian market adjacent to India's, not an East Asian one.

## T15 — 🆕 p96 The binding high-risk regime for automated assessment is now **APAC's, not EMEA's** — and the date the EU vacated, Vietnam occupied thirteen days later

🔴 **This KB has priced EMEA as the compliance region for three passes.** `P94-A` — *"The Annex III
evidence pack for automated scoring (EMEA first, North America second)"* — rests on Annex III high-risk
obligations binding an education deployment. 🟢 **They no longer bind in 2026, and equivalent obligations
now do bind elsewhere.**

| jurisdiction | instrument | names automated assessment? | binds from |
|---|---|---|---|
| 🇪🇺 **EU** | AI Act **Annex III / Art. 6(2)**, as amended by the **Digital Omnibus on AI** (`Regulation (EU) 2026/1744`) | 🟢 yes — *evaluating learning outcomes*, Annex III point 3(b) | 🔴 **2 Dec 2027** *(deferred from 2 Aug 2026)* |
| 🇻🇳 **Vietnam** | **`Decision 33/2026/QD-TTg`** under **Law 134/2025/QH15**; duties in **Decree 142/2026/NĐ-CP** | 🟢 **yes, explicitly** — *"automatically conduct examinations, assess learning outcomes or rank learners"* | 🟢 **15 Aug 2026** — existing systems **before 1 Sep 2027** |
| 🇰🇷 **South Korea** | **AI Basic Act** — education is a *"high-impact AI"* area | 🟢 yes | 🟢 **22 Jan 2026**, penalty grace through 2026 |

🔵 **The timing is the finding, and it is almost comic.** The EU vacated **2 August 2026**. Vietnam's list
took effect **15 August 2026**. 🟢 **Thirteen days.** 🔴 **A studio that read the deferral as "the
assessment-compliance market slipped to 2027" misread it: the market moved regions.**

### 🟢 What actually changes in the offer

| limb | EMEA | APAC |
|---|---|---|
| **urgency** | 🔴 **gone until late 2027** for Annex III. 🟢 **What binds *now*: Art. 4 staff AI-literacy (in force, not deferred), Art. 50 transparency (2 Aug 2026), and the Art. 5 emotion-recognition prohibition in education (enforceable since 2 Feb 2025)** | 🟢 **live.** Vietnam requires **pre-deployment registration in a National AI Database**, conformity assessment, **mandatory human oversight** and **72-hour incident reporting** |
| **what the buyer is buying** | literacy, transparency copy, and a feature audit against a prohibition | 🟢 **an architecture**: a registration dossier, an oversight boundary and an incident pipeline |
| **who owns the budget** | the institution's compliance function | the system owner — because a **72-hour clock is an engineering requirement, not a policy one** |

🟢 **`P94-A` is not withdrawn — it is re-sequenced.** The Annex III evidence pack is the *same deliverable*,
and `rsmtool` (Apache-2.0) + `skll` (BSD-3) are still the permissive evidence layer that produces it
(`T13`). 🔵 **The change is which jurisdiction will pay for it this year.** **Sell the pack into Vietnam and
Korea on a live deadline; sell literacy and the emotion-recognition audit into EMEA; sell the pack into
EMEA from mid-2027.**

### 🔴 The limb nobody was looking at — and this KB already has the answer

🔴 **Vietnam's education list has THREE limbs and the first one is not about assessment at all:**
*self-study content generated from **uncontrolled data sources***.

🔵 **That catches a tutoring agent that never grades anything.** A RAG tutor answering a pupil from
un-curated web retrieval is a high-risk system in Vietnam **because of where its material comes from**, not
because of any judgement it makes. 🟢 **And `T11` already measured the control**: grounding a
curriculum-aligned tutor in **verified standards data** moved hallucination **31.9 % → 0.2 %**, and
`repos/foundations.md` Tier 1b carries `bncc-dev/bncc-pacotes` — MIT code, CC BY 4.0 data, **1 721 verified
objectives behind 7 MCP tools, embedded so lookups run locally.**

🟢 **So grounding is promoted from a quality argument to a regulatory control.** 🔵 **This matters
commercially out of proportion to its size:** *"it hallucinates less"* is a feature claim a buyer
discounts; *"the corpus is controlled, enumerated and provenance-tagged, which is the condition limb 1
imposes"* is a compliance artefact a buyer must have. 🟢 **Same architecture, different budget line.**
Costed as `P96-B` in `compose/patterns.md`.

🟡 **Evidence grade, stated because this trend is consequential.** 🔴 **Nothing here was read from a primary
text** — `WebFetch` returned `getaddrinfo ENOTFOUND` for every host attempted and `curl` returned `000` on
three legal-publisher URLs. 🟢 **The EU dates and the Vietnam instrument were each returned by two
independent search rounds over different source sets**, which is the strongest grade this channel produces.
🔴 **One date is unreconciled and is not used**: a general **1 Mar 2027** compliance limb appears in one
Vietnamese-law summary and could not be matched to the decision text.

## T16 — 🆕 p97 Each region leads with a different INSTRUMENT, and Africa's is **capacity**, not regulation or mandate

🔵 **This file has carried regional detail for many passes without naming the pattern that organises
it.** 🟢 **Pass 97's Africa sweep — four countries, four separate queries, four returns — made it
visible, because all four came back with the SAME SHAPE and it is not the shape of any other
region.**

| region | the instrument that comes FIRST | what a buyer there is actually procuring |
|---|---|---|
| **EMEA** (Europe) | 🔴 **Regulation.** EU AI Act: AI-literacy duty live since **2 Feb 2025**, Annex III high-risk from **2 Dec 2027**, emotion inference **banned**, deployer duties reaching schools directly | **Governance and evidence.** Conformity, audit trails, human-oversight proof. |
| **APAC** | 🔴 **Mandate.** South Korea's AI Basic Act **in force 22 Jan 2026**; Vietnam's Decision 33/2026/QD-TTg **15 Aug 2026**; China AI compulsory from age six, ~8 h/yr in Beijing; India mandatory from **Class 3 in 2026–27** | **Curriculum and scale.** Content, teacher certification, delivery to very large cohorts. |
| **North America** | 🟡 **State product requirements.** Idaho SB 1227 **bars AI replacing teachers**; California AB 1159 would bar student data for model training; Purdue's AI competency a **graduation requirement from Fall 2026** | **Compliant product plus assessment instrumentation.** |
| **LATAM** | 🟡 **Statute, newly.** Colombia's **`Ley 2626 de 2026`** with lineamientos due **Feb 2027**; Mexico's Edomex reform; Brazil's MEC statement; Argentina's `PaideIA` programme | **Curriculum lineamientos and teacher capability.** |
| 🆕 **EMEA (Africa)** | 🟢 **CAPACITY.** 🔴 **4 of 4 countries have teacher-capacity programmes. 0 of 4 have a binding national AI-in-education instrument.** | 🟢 **Teacher training at scale, and offline-capable delivery.** |

### 🟢 The African evidence, because 4-of-4 is the whole claim

| country | capacity programme (present) | binding instrument (absent) |
|---|---|---|
| **Egypt** | 🟢 UNESCO × MoETE **national AI competency framework for teachers, launched 3 Jun 2026**; AI+programming into technical schools **2026/27**; >236 000 enrolled in general secondary | 🟡 **Closest to an exception** — a national *framework*, but for teacher competency, not a curriculum rule |
| **Kenya** | 🟢 **CEMASTEA training 5 400 teachers** before the **Jan 2026** CBE senior-school rollout; >20 700 devices via the World-Bank-backed Kenya Digital Economy Acceleration Project | 🔴 **CBE not tailored for AI; a national AI-literacy framework is still being *called for*** |
| **Nigeria** | 🟢 **Experience AI** 2026 rollout (Raspberry Pi Foundation × Google DeepMind curriculum, 1 142 educators, 5 states); **Naija Teacher AI** (TRCN × GMind AI), 🟢 **offline by design** | 🔴 **NERDC curriculum still under revision**; 2025 reform introduced AI but no AI framework published |
| **South Africa** | 🟡 Thinner — the commentary is about absence | 🟡 **Draft National AI Policy Cabinet-approved 25 Mar 2026**; 🔴 **DBE's education framework not published**; AI literacy has no fixed CAPS place |

### 🔵 Why this is a trend and not a regional note

🔴 **Because it inverts the sales motion, and getting it backwards wastes the engagement.** 🔴 **A
governance-and-conformity pitch — the correct EMEA-Europe pitch — has nothing to attach to in
Nairobi or Abuja, because there is no instrument to be compliant with.** 🟢 **What those buyers are
funding, with World Bank and UNESCO money and on dated timelines, is teacher capability and device
reach.** 🔵 **And the binding technical constraint is named explicitly by the delivery programmes
themselves: `Naija Teacher AI` is built to work OFFLINE.**

🟢 **That maps onto this KB's shelf precisely, and it is the one place where an old row becomes the
lead row:** `learningequality/kolibri` (**MIT**) is an offline-first learning platform, and this
file has carried it for many passes as a footnote to the LMS tier. 🟢 **For the African capacity
market it is not a footnote — it is the correct base**, because it is the only permissive platform
on the shelf designed for intermittent connectivity. 🔵 **Teacher-facing content generation on top
of it is the deliverable**, not a student-facing tutor.

🔴 **The failure mode this trend exists to prevent:** reading "no AI regulation yet" as "market not
ready". 🟢 **4 of 4 countries are spending now, on timelines with dates (Kenya Jan 2026, Egypt
2026/27, Nigeria 2026) — they are simply buying a different thing.**

### 🟡 What would refute T16

🟢 **Stated so the next pass can kill it cheaply:** a **published, binding** national AI-in-education
curriculum instrument from Kenya, Nigeria or South Africa would move that country into the LATAM
column and weaken the 0-of-4. 🔵 **South Africa is the likeliest to flip** — its draft policy was
Cabinet-approved in March 2026 with school implementation reported for 2027–2028. 🔴 **Egypt is
already the partial exception and should be re-read first**, since a teacher-competency framework is
one step from a curriculum rule. 🟡 **And all four rows rest on secondary sources: the
primary-source channel was closed this pass** (see `intel/market.md`).

## Instrument note carried forward

🟢 **`git ls-remote --symref` and `raw.githubusercontent.com` discriminate; `curl` on `github.com` and
`api.github.com` return 403 for real and invented slugs alike and must not be used.**
🆕 **Newly recorded: `WebFetch` on `https://github.com/topics/<t>` renders the page, its star counts and the
topic total, while `curl` on the identical URL is 403.** That is where star counts and topic denominators come
from.
🔴 🆕 **p93: the sandbox adds a second limit on top of the egress one — repository code cannot be
executed.** `compose/code/grant-ladder-v4/ladder.sh` could not be run, so this pass ran its *oracle map* by
hand and **printed each payload's title block rather than classifying it** (`P970`). 🔵 **Declining to
classify is the correct failure mode here; forking the shared classifier is the one `P237` forbids and the
one that cost pass 91 two platform licences.** Every row added this pass carries bytes, filename, ref and
SHA so v4 can re-derive it and contradict this pass on the record.
🟢 🆕 **p93 oracle addition: `WebFetch` on `https://github.com/<owner>/<repo>` renders star counts, fork
counts and the sidebar licence**, which is where this pass's ★ figures come from. 🔴 **And it exposed a
blind spot shared with the ladder** — the sidebar reports the **root** licence only, so
`bncc-dev/bncc-dados` reads *"MIT license"* while the data it exists to publish is CC BY 4.0 one directory
down (`P969`).

🔴 **Re-confirmed (`P944`/`P950`): the policy-source block is an EGRESS ALLOWLIST, not DNS.** Four primary
hosts needed this pass — `cbse.gov.in`, `digitaleducationcouncil.com`, `hepi.ac.uk`, `unu.edu` — returned
`000`/0 B under `curl` and `ENOTFOUND` under `WebFetch`. Not retried per host.
🆕 **p93 adds three to the blocked list:** `www.marketsandmarkets.com`, `bncc.dev` and `profy.com.br`, all
`ENOTFOUND` under `WebFetch`. 🟢 **The `bncc.dev` block cost nothing, because its repositories are on
GitHub and the payloads were read there directly** — but the `marketsandmarkets.com` block is why the
regional-versus-global arithmetic in `intel/market.md` cannot be closed against that firm's own global
figure. Figures from them are labelled
*search-summary* in `intel/market.md`.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
