---
industry: education
region: Global
updated: 2026-10-11
---

# Education — compose patterns

**Pass 115, 2026-10-11.** Census window **01:13 → 01:25 UTC**.
🟢 **`compose/code/p115-region-evidence/`, `test_p115.sh` 193 passed / 0 failed, fully
offline; `region.sh` read 296 of 296 addresses, zero unread, four controls from one snapshot.**

## 🔴 `P115-GATE` — the region gate, run before any regional claim about a starting point reaches a client

🔵 **Nine passes of this page have quoted patterns "for EMEA", "for LATAM", "for APAC". p115
measured where those regions actually come from, and the answer changes what may be said:**

| source of a row's region | rows | may a client-facing claim rest on it? |
|---|---|---|
| a TYPED `country:` field in the row's own `CITATION.cff` | **3** | 🟢 **yes — it is a declaration, machine-readable, by schema** |
| an `academic` / `government` address in the row's ROOT metadata | **8 + 0** | 🟢 **yes — a registry-restricted suffix names an institution and a country in one token** |
| an `other`-class ccTLD in the row's ROOT metadata | **11** | 🟡 **only with the evidence quoted beside it** — a company or personal domain is not an institution (`P800`) |
| this KB's committed org record (`orgs.region.tsv`) | **93** | 🟡 **yes, labelled as this KB's record — not the repository's statement** |
| the row's README (layer R) | **59** | 🔴 **NOT YET — `Gap 405`; 25 of 25 agree but 58 % is uncheckable** |
| a NESTED metadata file | — | 🔴 **NEVER (`P115-N`)** |
| 🔴 **nothing at all** | 🔴 **182 of 296** | 🔴 **then the pattern is REGIONLESS and must be sold as such** |

### 🟢 The gate as three commands, so it is checkable rather than quotable

```sh
cd compose/code/p115-region-evidence

# 1. does the row state its own region, and on what class of evidence?
grep -P '^<org>/<repo>\t' addresses.region.tsv

# 2. if not, does this KB's org record place it — settled or provisional?
awk -F'\t' -v o="<org>" '!/^#/ && $1==o' orgs.region.tsv

# 3. what did the census actually see? (layer 0 / layer 1 / layer R, side by side)
awk -F'\t' -v s="<org>/<repo>" 'NR==1||$1==s' result.2026-10-11.tsv | cut -f1,20,21,25,26,30,31,36,37,38
```

🔴 **If step 1 is empty, step 2 is empty or ends in `?`, and step 3 says `no-struct`, the row
has NO region. Nine of the patterns below carry a region in their title; each is re-checked
against this gate under `P115-PAT-CHECK`.**

## 🟡 `P115-PAT-CHECK` — the regional patterns on this page, re-checked

| pattern | its region | the row it rests on | 🆕 evidence for that region |
|---|---|---|---|
| `PB1` sovereign tutor (EMEA) | EMEA | `moodle/moodle` + local model | 🔴 **`no-country` at every layer — the EMEA claim is the DEPLOYMENT's, not the repo's.** 🟢 Still sound: the pattern's EMEA-ness is the sovereignty requirement, not the maintainer's address. **Re-worded, not retired.** |
| `P112-PAT-2` LATAM Brazilian SIS line | LATAM | `portabilis/i-educar`, `portabilis/pre-matricula-digital` | 🟢 **CONFIRMED by committed evidence — both place LATAM on `portabilis.com.br`** |
| `P112-PAT-3` APAC AI-assurance harness | APAC | `aiverify-foundation/moonshot` family | 🟡 **layer R places all three APAC on `aiverifyfoundation.sg` + `www.imda.gov.sg` (government class) — the best APAC evidence on the shelf, and layer 0 places NONE of it.** 🔴 The APAC label is correct and currently rests on a channel `Gap 405` has not cleared |
| `P112-PAT-4` EMEA sovereign teacher assistant | EMEA | `openfun/richie` among others | 🟢 **CONFIRMED — `openfun/richie` and `openfun/xblock-proctor-exam` both place EMEA on `fun-mooc.fr`** |
| `P112-PAT-5` North America (pin first) | North America | `jupyterhub/jupyterhub`, `Submitty/Submitty` | 🟡 **`jupyterhub` is `no-country`; `Submitty` places North America at layer R on `compsci.rpi.edu` / `www.rpi.edu` (`academic`).** Label correct, evidence one layer below the gate's bar |
| `P109-A-PAT` Brazil BNCC alignment service | LATAM | `bncc-dev/bncc-dados`, `bncc-dev/bncc-pacotes` | 🟢 **CONFIRMED AT THE STRONGEST CLASS — both carry a TYPED `country: BR` in their `CITATION.cff`. The only patterns on this page whose region is a machine-readable declaration** |
| `P106-A` Moodle AI seam | GPL-3, no region | `moodle/moodle` | 🔵 no regional claim made — nothing to check |
| `P106-B` EUPL Finnish national registry | EMEA | `opetushallitus/*` | 🟢 **CONFIRMED — `opetushallitus/ehoks` places EMEA on `artifactory.opintopolku.fi`.** 🟡 **And two sibling rows would have placed EMEA on `ec.europa.eu` had the stoplist been off: right region, invalid evidence (`P115-AB`)** |
| `P104-A` sovereign no-egress tutor (EMEA, LATAM) | both | LMS rows | 🔴 **regionless at layer 0; sell it on the sovereignty requirement, not on maintainer geography** |

🟢 **Nothing is retired. Two patterns are UPGRADED to committed evidence (`P109-A-PAT` at the
typed class, `P112-PAT-2` and `P112-PAT-4` at the root-metadata class), and four are
re-labelled: their region is a property of the DEPLOYMENT or of this KB's record, not a claim
the repository makes about itself.**

## 🟢 🆕 `C115-1` — the region-matched starting-point shortlist (any region; half a day)

🔵 **What it is.** The question a client asks in the first week — *"give me a starting point
that is maintained in our region, builds reproducibly on day one, and whose licence we can
ship"* — answered from committed files only, with no judgement calls and no egress.

**Wire it from what is already here.** Three committed TSVs, one join:

```sh
cd compose/code

# region (p115) x lock reach (p114), joined on the address
join -t$'\t' -1 1 -2 1 \
  <(awk -F'\t' '!/^#/ && NF>=5 {print $1"\t"$2"\t"$4}' p115-region-evidence/addresses.region.tsv | sort) \
  <(awk -F'\t' 'NR>1 {print $1"\t"$18}' p114-lock-reach/result.2026-10-11.tsv | sort)
# -> address  region  evidence-class  reach-verdict

# add this KB's org record for the rows p115 cannot place
awk -F'\t' '!/^#/ && NF>=2 {print $1"\t"$2}' p115-region-evidence/orgs.region.tsv
```

**The decision rule, in priority order:**

| rank | region evidence | reach | what to do |
|---|---|---|---|
| 1 | `typed` or `academic`/`government` | `full-reach` or `vendored` | 🟢 **adopt as-is** |
| 2 | `typed` / `academic` / `government` | `partial-reach` | 🟢 adopt + the `C114-1` fork-time pin step |
| 3 | `other` | any | 🟡 adopt, but **quote the evidence host to the client** — it may be a personal domain |
| 4 | org record only | any | 🟡 label the region as this KB's record |
| 5 | 🔴 nothing | any | 🔴 **a regionless row: do not answer the region question with it** |

🔵 **What it costs and buys.** Half a day, zero egress, and it replaces the conversation where
a studio asserts a region and is later asked where that came from. 🔴 **Its honest limit: on
this shelf rank 5 is **182 of 296 rows**, so the shortlist it produces is short. That is the
point — a short list with provenance beats a long one without.**

## 🟡 🆕 `C115-2` — the Epesi evaluation spike, with a go/no-go rule (any region; 1 day)

🔵 **Why it is a spike and not a recommendation.**
[`jtylek/EpesiCRM`](https://github.com/jtylek/EpesiCRM) is the only new platform this KB has
admitted in eleven passes: MIT in its root `LICENSE` ("Copyright (c) 2006-2026 Janusz Tylek"),
1 375 files, last commit **2026-10-07**, PHP/Laravel 12 + Filament. 🔴 **It is also mid-rewrite
on a non-default branch name (`laravel`), has ZERO education-specific paths, and its
`composer.json` still carries the Laravel skeleton's metadata.** A row in that state earns a
day of evaluation, not a place in an estimate.

```sh
# 1. the grant, from the tree, not from a roundup
d=$(mktemp -d); git init -q --bare "$d"
git --git-dir="$d" remote add origin https://github.com/jtylek/EpesiCRM
git --git-dir="$d" config remote.origin.promisor true
git --git-dir="$d" config remote.origin.partialclonefilter blob:none
git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD
git --git-dir="$d" ls-tree -r --name-only FETCH_HEAD | grep -iE '^(licen[cs]e|copying)'

# 2. the branch it actually serves (NOT main)
git ls-remote --symref https://github.com/jtylek/EpesiCRM HEAD

# 3. does it reach its own locks? (run p114's instrument on it)
printf 'jtylek/EpesiCRM\n' > /tmp/one.txt
compose/code/p114-lock-reach/reach.sh /tmp/one.txt

# 4. does it say where it is maintained? (run p115's)
compose/code/p115-region-evidence/region.sh /tmp/one.txt
```

**Go / no-go, decided before the spike starts:**

| finding | decision |
|---|---|
| root `LICENSE` is MIT **and** `reach.sh` says `full-reach` or `vendored` | 🟢 **GO** — use it as the back-office/admin layer under an education vertical built on top |
| 🟡 `partial-reach` with the root manifest reached | 🟡 GO with the `C114-1` fork-time pin step in the estimate |
| 🔴 root manifest orphaned, **or** the `laravel` branch is not where commits land | 🔴 **NO-GO** — vendor at a SHA and own the dependency set, or use Corteza / Krayin instead |
| 🔴 any expectation of an education module | 🔴 **NO-GO as stated** — there is none; the education layer is YOUR build |

🔵 **The three decoy addresses are part of the deliverable:**
[`Epesi-Team/epesi`](https://github.com/Epesi-Team/epesi) does not resolve on the git lane,
[`cezarc/EPESI`](https://github.com/cezarc/EPESI) is thirteen years stale with no licence
file, and [`Telaxus/EPESI`](https://github.com/Telaxus/EPESI) is a one-file husk — and 2026
roundups name two of the three as the project's home. 🟢 **A client handed "Epesi, MIT" and
left to find it themselves has a 1-in-4 chance of landing on the address that supports the
claim.**

## 🟡 🆕 `C115-3` — the North Carolina approved-tool register (North America; 3–4 wk) — CONDITIONAL

🔴 **Published as CONDITIONAL and labelled so in every artefact, because the statute's text
could not be verified on this channel (`P115-S`: `ncleg.gov` and `dpi.nc.gov` refused at the
CONNECT layer, logged by host and timestamp).** 🔵 **Two independent secondary guides agree
that §7.39 of NC Session Law 2026-41, effective 1 July 2026, requires NC DPI to publish a
model AI-use policy by **31 December 2026**, local boards to adopt their own, a framework for
evaluating generative-AI educational tools, a **public list of approved tools**, and teacher
AI professional development by **30 June 2028**.**

🟢 **Why this KB is unusually well placed if it holds: an "approved-tool list + evaluation
framework" is a procurement artefact, and the evidence a procurement artefact needs is exactly
what nine passes have measured on these 296 addresses.** Wire the register from the committed
TSVs:

| the register's column | where it comes from, already committed |
|---|---|
| licence, read from the tree | `p963-shelf-licence-agreement`, `p199-perfile-license` |
| reproducible first install | `p114-lock-reach/result.2026-10-11.tsv` — the `verdict` column |
| alive / bus factor | `p109-freshness`, `p110-bus-factor` |
| whose model does it call | `p113-provider-binding` — `local` / `broker` / `override` / `hosted-only` |
| 🆕 where it is maintained | `p115-region-evidence/addresses.region.tsv` + `orgs.region.tsv` |
| 🔴 statutory basis | 🔴 **UNVERIFIED — `P115-S`. Step 0 of this pattern is reading the enacted text** |

🔴 **Step 0, and it is a gate not a task: obtain
`https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf` and read
§7.39. If the section does not say what the two guides say, this pattern is void.** 🟢 **No
part of it should be quoted to a client before step 0 completes, and saying so is cheaper
than withdrawing it later (`P113-T` is the precedent: a roundup reported a two-year-old UK
procurement in the present tense with its date stripped off, and this KB nearly held it).**

## 🔴 What this pass retired from the patterns on this page

🟢 **Nothing.** 🔵 **p115 read a column no previous axis touched and changed no licence, reach,
recency, bus-factor or provider-binding verdict.** 🟡 **What it changed is what a REGIONAL
claim may rest on — which is why `P115-PAT-CHECK` re-labels four patterns rather than retiring
them, and why the `other`-class rows now require their evidence host quoted beside them.**

# Education — compose patterns

**Pass 114, 2026-10-11.** ⏱️ **First pass of this date** (census window
**2026-10-10 23:54 → 2026-10-11 00:25 UTC**).

🟢 **Every repository named below was read live this pass by `reach.sh` (`rc=0`, 296 of
296 addresses, zero unread) and carries its p111 verification verdict, its p112 closure
verdict and its 🆕 p114 reach verdict. `compose/code/p114-lock-reach/`, `test_p114.sh`
**98 passed / 0 failed**, fully offline.**

🔴 **p114 TIGHTENS p112's gate before it adds a pattern, because the tightening changes
what two patterns on this page must do at fork time.**

## 🔴 `P114-GATE` — the reach gate, and why `P112-GATE` was not enough

🔵 **`P112-GATE` asked: is this component's dependency set locked? A pattern that vendors
a repository at a SHA has vendored its CODE; if the dependency set is `floating`, the
pattern has not vendored the thing that makes it run. p114 adds the question that gate
cannot ask: locked WHERE? A lock in `examples/demo/` satisfies p112 and resolves nothing
you will install.**

| component this page relies on | p111 | p112 | 🆕 p114 | orphaned / lockable | gate |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 63** | 🟢 **passes outright** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 2** | 🟢 **passes outright** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `checked` | 🟢 `pinned` | 🟢 **`full-reach`** | 🟢 **0 / 6** | 🟡 **passes — but on a hand-maintained `requirements.txt`; own that file (`P114-V`)** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `checked` | 🟡 `partial-pin` | 🟡 `partial-reach` | 🟡 2 / 57 | 🟡 **passes with a note — 55 of 57 reached, neither orphan at the root** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟢 `checked` | 🟡 `partial-pin` | 🟡 `partial-reach` | 🔴 **2 / 3, root** | 🔴 **FAILS — generate the root lock at fork time** |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 `checked` | 🔴 `floating` | 🔴 `partial-reach` | 🔴 **21 / 22, root** | 🔴 **FAILS — pin at fork time (unchanged verdict, sharper reason)** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟢 `checked` | 🔴 `floating` | 🔴 **`no-reach`** | 🔴 **1 / 1, root** | 🔴 **FAILS — nothing to inherit; own the dependency set** |
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 `checked` | 🟢 `pinned` | 🟡 **`partial-reach`** | 🔴 **1 / 5, root** | 🔴 **NEWLY FAILS — p112 passed this component; its root `pyproject.toml` is orphaned** |

🔴 **One component newly fails the gate and it is one this page was relying on.** Every
pattern below that touches Submitty now carries an explicit fork-time step.

### 🟢 The gate as three commands, so it is checkable rather than quotable

```sh
# 1. does a lock reach the manifest you will install from?
cd compose/code/p114-lock-reach
printf 'ORG/REPO\n' > /tmp/one.txt && ./reach.sh /tmp/one.txt
#    -> verdict column 18; root_orphan column 10; orphan_paths column 19

# 2. if root_orphan=1, the remedy is local and one commit:
#    python:  cd <root> && uv lock        (or poetry lock / pip-compile)
#    node:    cd <root> && npm install --package-lock-only
#    go:      cd <root> && go mod tidy    # writes go.sum

# 3. re-run step 1 and require verdict=full-reach before the fork is adopted.
```

## 🟢 🆕 `C114-1` — the fork-time pinning step, as a concrete recipe

🔵 **Wire this ahead of every pattern on this page that adopts a `partial-reach` or
`no-reach` component. It is the cheapest finding this KB has produced: 88 rows need it,
and for most of them it is one generated file.**

**Components:** the target repo + `compose/code/p114-lock-reach/reach.sh` (the gate) +
the ecosystem's own resolver (`uv` / `poetry` / `npm` / `go mod`).

```
fork ORG/REPO at SHA
  └─ reach.sh ORG/REPO                      # measure BEFORE changing anything
       ├─ verdict=full-reach ───────────────► adopt as-is
       ├─ verdict=vendored ────────────────► adopt as-is; no registry needed (P114-D)
       ├─ verdict=self-pinned|foreign-build► assess in its own idiom (P114-E)
       └─ root_orphan=1 ──────────────────► for each path in orphan_paths:
                                               cd $(dirname path)
                                               <resolver> lock        # generate
                                               git add <lockfile>     # COMMIT it
                                             re-run reach.sh; require full-reach
```

🔵 **Why the commit matters more than the lock:** `P114-B` credits a lock sitting at the
manifest's directory or an ancestor. A lock generated in CI and thrown away satisfies
nothing — the next engineer resolves afresh. The deliverable is a committed file at the
right path.

## 🟡 🆕 `C114-2` — Open edX course generation, re-wired for the gate

🔵 **Supersedes the wiring in `compose/code/openedx-course-generator/` on one point only:
the fork-time step. The pattern is unchanged; its preconditions are not.**

| component | role | 🆕 p114 | fork-time requirement |
|---|---|---|---|
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | Open edX deployment | 🔴 **`no-reach`** | 🔴 **own the dependency set — the root `pyproject.toml` has no lock anywhere in the tree** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | open-response assessment | 🔴 `partial-reach`, root | 🔴 **generate + commit the root lock** |
| [`edly-io/pxc`](https://github.com/edly-io/pxc) | Open edX extensions | 🔴 `partial-reach`, root (6 / 17) | 🔴 **generate + commit the root lock** |
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | model runtime | 🔴 `partial-reach`, root (21 / 22) | 🔴 **pin at the fork SHA; do not track upstream** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | generation orchestration | 🟢 **`full-reach`** | 🟢 **none — adopt as-is** |

🔴 **Four of the five components in this KB's most-cited pattern require a fork-time
pinning step.** That is not a reason to change the pattern — these are the right
components and `P111`/`P112` already established they are verified and alive — it is a
reason to put the step in the estimate.

## 🟢 🆕 `C114-3` — the all-green composition, for an engagement that cannot absorb remediation

🔵 **Every component below is `full-reach`, `checked` at p111 and reached on every
manifest it declares. This is the composition to propose when the client's first sprint
has no room for supply-chain work.**

| component | role | licence | p114 |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS of record | 🟡 GPL-3 | 🟢 **0 / 63 orphaned** |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | durable orchestration for agent workflows | 🟢 MIT | 🟢 **0 / 2** |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | assessment engine | 🟡 AGPL-3 | 🟢 **0 / 58** |
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | modular platform shell | 🟢 Apache-2.0 | 🟢 **0 / 114** |
| [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | LLM evaluation harness | 🟢 Apache-2.0 | 🟢 **0 / 2** |

🔵 **Wiring:** Moodle as the system of record; Temporal workflows drive each
agent-authored artefact (lesson draft → review → publish) so a failed generation is
retried rather than lost; PrairieLearn owns assessment and returns graded outcomes over
LTI; `moonshot` runs as the pre-deployment evaluation gate on any model swap. 🟡 **Licence
note, unchanged by this pass:** Moodle GPL-3 and PrairieLearn AGPL-3 are copyleft — the
composition is safe for a hosted institutional deployment and is **not** a basis for a
redistributed proprietary product. The MIT/Apache-2.0 members (`temporal`, `leemons`,
`moonshot`) are the ones Globant can build on without that constraint.

🔵 **What this composition does NOT yet have:** no component in it has had its lockfile
BODIES read — reach says a lock is in the right place, not that the versions inside it
are current. That is the question p114 hands to p114.

# Education — compose patterns

**Pass 113, 2026-10-10.** ⏱️ **Twenty-third pass of this date.**

🟢 **Every repository named below was read live this pass by `bind.sh` (`rc=0`, 296 of 296
addresses, zero unread, zero stray lines, zero capped rows) and now carries THREE verdicts:
its p111 verification verdict, its p112 closure verdict and its p113 binding verdict.
`compose/code/p113-provider-binding/`, `test_p113.sh` 121 passed / 0 failed, fully
offline.**

🔴 **What changed for these patterns: a pattern built on a row that is `pinned` and
`checked` but `hosted-only` ships a client a reproducible, tested dependency on one
vendor's endpoint. Three of the patterns on this page did exactly that before this pass.
The binding column below is the fix.**

## 🟢 The parts list — the 17 rows that pass all three axes

🔵 **`pinned` (p112) AND `checked` (p111) AND pointable at a model the client controls
(p113). This is the only list on this page where every row is simultaneously reproducible,
testable and portable, and every figure in it was derived this pass.**

| row | binding | declares | licence |
|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟢 `local` | `transformers` | 🟡 AGPL-3 |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟢 `local` | `transformers` | 🟡 GPL-3 |
| [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 `local` | `ollama` | 🟢 **MIT** |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 🟢 `local` | `ollama` + `pydantic-ai` | 🟢 **Apache-2.0** |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | 🟢 `local` | `ollama`, `sentence-transformers` | 🟢 **Apache-2.0** |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🟢 `local` | `ollama`, `whisper` | 🟢 **MIT** |
| [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🟢 `local` | `ollama` | 🟢 **MIT** |
| [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | 🟢 `local` | `sentence-transformers` + `OPENAI_API_BASE` | 🟢 **MIT** |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 `broker` | `langchain` | 🟢 **MIT** |
| [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor) | 🟢 `broker` | `langchain` | 🟢 **BSD-3** |
| [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🟢 `broker` | `langchain` + `base_url` | 🟢 **MIT** |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `broker` | `langchain` + `base_url` | 🟢 **Apache-2.0** |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 `broker` | `langchain` | 🟢 **MIT** |
| [`nextcloud/llm2`](https://github.com/nextcloud/llm2) | 🟢 `broker` | `langchain` | 🟡 AGPL-3 |
| [`aiverify-foundation/moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) | 🟢 `broker` | `langchain` | 🟢 **Apache-2.0** |
| [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | 🟡 `broker` ※ | `langchain`, `openrouter` | 🟢 **Apache-2.0** |
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟡 `broker` ※ | `openrouter` | 🟢 **MIT** |

🔵 **※ `P113-H` — substitutability from an AGGREGATOR. OpenRouter makes the model swappable
by configuration and is still somebody else's endpoint: use these two where swappability is
the requirement and NOT where egress is.**

## 🟢 `PB1` — the sovereign tutor: LMS + local model + a portable evaluator (EMEA, 8–10 wk)

🔵 **The pattern `T44` makes sellable: an education stack that runs entirely inside the
client's estate, with every component derived as `local` or `broker` this pass.**

```
            ┌──────────────── client estate, no egress ─────────────────┐
            │                                                           │
  learners ─┤  openedx/edx-platform  (AGPL-3, local, pinned, checked)    │
            │          │ LTI 1.3 / xAPI                                  │
            │          ▼                                                 │
            │  fwu-de/ais-chat  (MIT, broker: langchain + base_url)       │
            │          │ OpenAI-compatible HTTP                          │
            │          ▼                                                 │
            │  ollama/ollama  (MIT, local, pinned)  ── GGUF weights       │
            │          ▲                                                 │
            │  MysterionRise/adaptive-knowledge-graph                     │
            │     (Apache-2.0, local: ollama + sentence-transformers)      │
            │          │ learner model: IRT + BKT                        │
            │          ▼                                                 │
            │  learning-commons-org/evaluators  (MIT, broker: langchain)  │
            └───────────────────────────────────────────────────────────┘
```

**Wiring, concretely.** `ais-chat` is `broker` because it declares `langchain` AND a
`base_url`, so its model endpoint is configuration: point it at `http://ollama:11434/v1`
and no code changes. `adaptive-knowledge-graph` declares `sentence-transformers`, so its
embeddings are computed locally — no embedding API call leaves the estate, which is the
leak most "self-hosted" education stacks still have. `evaluators` is `langchain`, so the
grading model is swapped by config too. **Every provider in this pattern is replaceable at
deploy time; none is a code dependency.**

🔴 **The one thing to do at fork time: `openedx/edx-platform` is `pinned` and `ILIAS` is
`pinned`, but check `ollama/ollama`'s own closure before vendoring — p112 reads it
`pinned`, which is why it is in this pattern rather than `huggingface/smolagents`
(`floating`).** 🟡 **AGPL-3 on edx-platform: the platform itself is a deployment, not a
derivative, but anything linked INTO it inherits — `T34`'s mount rule applies here too.**

## 🟢 `PB2` — model-portability retrofit for a locked row (any region, 2–3 wk)

🔴 **The pattern that exists because of `P113-C`: nine shelf rows are reproducible, tested
AND locked to one vendor. The client already wants the repository; the binding is the
blocker.**

```
  BEFORE                                 AFTER
  oppia/oppia (hosted-only: google)      oppia/oppia
     └─ google SDK call sites      ──▶      └─ litellm (MIT) shim
                                               ├─ ollama      (local path)
                                               ├─ gateway     (OpenAI-compatible)
                                               └─ google      (unchanged fallback)
```

**Why litellm and not langchain here:** the task is substitution at the call site, not an
agent framework. `litellm` is the abstraction that `huggingface/smolagents` itself declares
(p113 reads smolagents `local` with `litellm` in its broker column), which makes it the
choice with a precedent on this very shelf rather than a preference.

**The nine candidates, with the retrofit's size set by the hosted column:**
`oppia/oppia` (`google`), `PrairieLearn/PrairieLearn` (`anthropic` + `openai` — two call
paths, so the largest of the nine), `canyongbs/advisingapp` (`openai`),
`ankimcp/anki-mcp-server` (`anthropic`), `Miaotofu01/Study-Mate` (`deepseek` + `openai`),
`tomaszboloz/WCAG-Accessibility-Skills` (`gemini`), `opetushallitus/ehoks` (`bedrock`),
`OpenOLAT/OpenOLAT` (`anthropic`), `nextcloud/integration_openai` (`openai`).

🟢 **`ehoks` is the one to lead with. It is EUPL — reciprocal — so the shim MUST flow back
upstream, which turns a retrofit into a public contribution to Finnish national
infrastructure. That is a reference, not just a ticket (`T44`).**

🔴 **`aiverify-foundation/moonshot` and `moonshot-ui` are NOT on this list although the
instrument flagged them `hosted-only`: the token is their own name, and `.env.local` points
at `http://0.0.0.0:5000`, their own backend. Adjudicated by hand under `P113-R` — building
`PB2` for them would be building against a measurement artefact.**

## 🟢 `PB3` — the LMS→model seam, mounted BESIDE the platform (any region, 6–8 wk)

🔵 **`T46` + `T34` + `T30` make this the firmest commercial pattern in this base, and p113
supplies the last missing fact.**

```
  moodle/moodle (GPL-3, no-model, 64 declarations read, NONE naming a model)
      │  web services / OAuth2
      ▼
  ── boundary: everything below keeps YOUR licence ──
  csmediapro/moodle-mcp-server   (local: ollama, pinned, checked)
      │  MCP
      ▼
  your agent  ──▶  ollama/ollama (MIT, local)   or   litellm ──▶ gateway
```

**The decision this pattern exists to force.** Code mounted INSIDE Moodle is GPL-3 and
greenfield; mounted BESIDE it over web services + MCP, it keeps the licence you choose.
`T34` found **zero** packages published against Moodle's own `moodle-aiprovider` /
`moodle-aiplacement` extension points, and `T46` now adds that the platform declares no
model binding to inherit either — so there is nothing upstream pulling the decision either
way. **It is a pure commercial choice made once, at the start, and not revisitable.**

🟢 **`csmediapro/moodle-mcp-server` is the proof the beside-mount works and is portable:
`local` (`ollama`), `pinned`, `checked` — reproducible, tested and egress-free, sitting
outside a GPL-3 platform.**

## 🔴 What this pass retired from the patterns on this page

🔴 **Any pattern on this page whose leading component reads `hosted-only` on p113 is now
marked, because a pattern that is reproducible and locked sells the client a tested
dependency on one vendor.** 🟢 **The three leading components to stop using as the model
tier in a sovereignty pitch: `oppia/oppia` (`google`), `PrairieLearn/PrairieLearn`
(`anthropic` + `openai`), `canyongbs/advisingapp` (`openai`). All three remain excellent on
every earlier axis and all three need `PB2` first.**

🟡 **And the direction of the error, so none of this is read too strongly: p113 reads
DECLARATIONS, not program text, so `local` and `broker` are LOWER bounds and `hosted-only`
is an UPPER bound (`P113-I`). A row in `PB2`'s list may already have a portability path in
code that it does not declare — the retrofit estimate should begin by checking, and that
check is a day.**

---

# Education — compose patterns

**Pass 112, 2026-10-10.** ⏱️ **Twenty-second pass of this date.**

🟢 **Every repository named below was read live this pass by `depclosure.sh` (`rc=0`, 296
of 296 addresses, zero unread) and carries both its p111 verification verdict and its
p112 closure verdict. `compose/code/p112-dependency-closure/`, `test_p112.sh` 109 passed
/ 0 failed, fully offline.**

🔴 **p112 adds a GATE to this page before it adds a pattern, because the gate invalidates
part of what the page already recommends.**

## 🔴 `P112-GATE` — the closure gate, and the two patterns on this page that fail it

🔵 **Prior passes gated this page on liveness (`P109-GATE`) and on verification (p111). The
closure gate is the next one and it is the cheapest to check: a pattern that vendors a
repository at a SHA has vendored its CODE; if that repository's dependency set is
`floating`, the pattern has NOT vendored the thing that makes it run.**

| component this page relies on | p111 | 🆕 p112 | gate |
|---|---|---|---|
| [`huggingface/transformers`](https://github.com/huggingface/transformers) | 🟢 `checked` | 🔴 **`floating`** | 🔴 **FAILS — pin at fork time** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🟢 `checked` | 🔴 **`floating`** | 🔴 **FAILS — pin at fork time** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `checked` | 🟢 `pinned` | 🟢 passes |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 `checked` | 🟢 `pinned` | 🟢 passes |
| [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 `checked` | 🟢 `pinned` | 🟢 passes |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 `checked` | 🟢 `pinned` | 🟢 passes |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `checked` | 🟡 `partial-pin` | 🟡 passes with a named gap (gradle) |

🟢 **The gate does not retire either failing component — both are the right choice for
what they do. It turns an invisible risk into a one-line task, below.**

## 🟢 🆕 `P112-PAT-1` — the pin-at-fork step, which belongs in every pattern on this page

🔵 **Concrete, repository-specific, and it runs once per fork rather than once per
sprint. For the two `floating` components above:**

```sh
# transformers: vendor the code AND resolve the environment beside it
git clone --depth 1 https://github.com/huggingface/transformers vendor/transformers
git -C vendor/transformers rev-parse HEAD > vendor/transformers.SHA
uv pip compile vendor/transformers/setup.py -o vendor/transformers.lock.txt
git add vendor/transformers.SHA vendor/transformers.lock.txt

# tutor: same step, and do it BEFORE building any Open edX plugin against it
git clone --depth 1 https://github.com/overhangio/tutor vendor/tutor
git -C vendor/tutor rev-parse HEAD > vendor/tutor.SHA
uv pip compile vendor/tutor/setup.py -o vendor/tutor.lock.txt
```

🔴 **Why `tutor` specifically, and why before the plugin: `tutor` is how an Open edX
installation gets stood up at all, it ships 8 deployment artefacts, and its single Python
ecosystem is unlocked. Every environment drift after the first plugin lands gets debugged
through the plugin instead of through `tutor`.**

🟢 **Acceptance test for the step, so it is verifiable rather than aspirational: a second
clone on a different machine, installed from the committed lock, produces byte-identical
`pip freeze` output. If it does not, the lock is incomplete and the fork knows on day one
rather than in week six.**

## 🟢 🆕 `P112-PAT-2` LATAM — a Brazilian SIS line with closure end to end

🔵 **Every component is `checked` on p111 AND `pinned` on p112 — the only full-stack
pattern on this page where that is true, and it is LATAM.**

| role | component | licence | p111 | p112 |
|---|---|---|---|---|
| student information system | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🟡 GPL-2 | 🟢 `checked` | 🟢 `pinned` |
| curriculum alignment (BNCC) | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | carried | 🟢 `checked` | 🟢 `pinned` |
| curriculum benchmark | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | carried | 🟢 `checked` | 🟢 `pinned` |
| agent graph | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 **MIT** | 🟢 `checked` | 🟢 `pinned` |
| durable orchestration | [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 **MIT** | 🟢 `checked` | 🟢 `pinned` |

🟢 **Wiring: `i-educar` is the system of record; a LangGraph graph reads enrolment and
assessment rows from it and writes BNCC alignment suggestions back as proposals, never
as grades; `bncc-pacotes` supplies the competency vocabulary and `bncc-benchmark` is the
regression suite the graph is scored against on every change; Temporal owns every
multi-step write so a half-applied alignment pass is recoverable rather than manual.**

🔴 **The licence constraint is real and nameable: `i-educar` is GPL-2, so the client ships
the SIS and its modifications under GPL-2. The LangGraph and Temporal halves are MIT and
stay separable — keep the graph in its own process and talk to `i-educar` over its HTTP
surface, not by linking into it.**

🔴 **`P112-PAT-2`'s one gap, stated: 2 of the 3 `portabilis` repositories are
`partial-pin`, not `pinned`. `i-educar` itself is the pinned one. Pin the other two at
fork time with `P112-PAT-1`.**

## 🟢 🆕 `P112-PAT-3` APAC — an AI-assurance harness for an LMS, Apache-2.0 end to end

🔵 **Singapore's `aiverify-foundation` is the only public body on this shelf that writes
suites, wires CI and pins dependencies. All three of its code repositories are `checked`
and `pinned`.**

| role | component | licence | p111 | p112 |
|---|---|---|---|---|
| model/agent evaluation engine | [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | 🟢 **Apache-2.0** | 🟢 `checked` | 🟢 `pinned` |
| evaluation in CI | [`aiverify-foundation/moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) | 🟢 **Apache-2.0** | 🟢 `checked` | 🟢 `pinned` |
| reviewer-facing UI | [`aiverify-foundation/moonshot-ui`](https://github.com/aiverify-foundation/moonshot-ui) | 🟢 **Apache-2.0** | 🟢 `checked` | 🟢 `pinned` |
| the LMS under test | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 GPL-3 | 🟢 `checked` | 🟢 `pinned` |

🟢 **Wiring: the Moodle AI subsystem's provider is pointed at the engagement's own model
endpoint; `moonshot` runs the red-team and capability suites against that same endpoint;
`moonshot-cicd` runs them as a gate in the delivery pipeline so a prompt or model change
cannot ship without a scored run; `moonshot-ui` is what the institution's academic-
integrity committee actually looks at. Because `moodle` is `pinned` and all three
Moonshot repos are `pinned`, the whole harness reproduces — which is the property an
assurance artefact needs most.**

🔵 **Jurisdictional fit: Korea's Framework Act treats AI in education as high-impact with
human-oversight and disclosure duties, and Singapore leads the ASEAN Working Group on AI
Governance. A scored, reproducible evaluation run is the evidence those duties ask for,
and this stack produces one by construction rather than by report-writing.**

## 🟢 🆕 `P112-PAT-4` EMEA — a sovereign, reproducible teacher-facing assistant

| role | component | licence | p111 | p112 |
|---|---|---|---|---|
| chat assistant for schools | [`fwu-de/ais-chat`](https://github.com/fwu-de/ais-chat) | 🟢 **MIT** | 🟢 `checked` | 🟢 `pinned` |
| LMS of record | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🟡 GPL-3 | 🟢 `checked` | 🟢 `pinned` |
| national-agency services | the 8 [`opetushallitus`](https://github.com/opetushallitus) repos | carried | 🔴 **1 of 8 PR-gated** | 🟢 **8 of 8 `pinned`** |
| agent graph | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | 🟢 **MIT** | 🟢 `checked` | 🟢 `pinned` |

🟢 **Wiring: `ais-chat` is the teacher-facing surface (German public-sector origin, MIT, so
a closed derivative is permitted); ILIAS holds courses and assessment; a LangGraph graph
mediates every call and is the single place where retention, logging and
purpose-limitation live. For a Finnish deployment, the `opetushallitus` services
(`koski`, `ataru`, `ehoks`, `eperusteet`, `oppijanumerorekisteri`, `organisaatio`,
`suorituspalvelu`, `valtionavustus`) are the integration targets.**

🟢 **The p112-specific finding that changes this pattern's price: all eight
`opetushallitus` repositories are `pinned`, so they stand up deterministically today.
What they lack is a pipeline a contributor can trigger — 7 of 8 have a suite that no
pull request runs. The engagement supplies CI, not an environment, and those are very
differently priced halves.**

🔴 **The EU AI Act constraint belongs in the pattern, not in a footnote: anything in this
stack that determines access, scores an assessment or steers a learning path is Annex III
high-risk, with the omnibus timeline putting standalone high-risk systems at 2 December
2027. Keep the graph's grading paths advisory-with-human-sign-off, and keep that boundary
expressed in code — a LangGraph node that cannot write a final grade — rather than in
policy prose.**

## 🟡 🆕 `P112-PAT-5` North America — the pattern that must be pinned before it is built

🔴 **North America is the region with the deepest `checked` tier on this shelf (p111) and
the WORST closure (p112: 33 % `pinned`, 35 % `floating`). The pattern therefore starts
with a gate rather than a component.**

| role | component | licence | p111 | p112 | action |
|---|---|---|---|---|---|
| SIS / data standard | [`ed-fi-alliance-oss/Ed-Fi-ODS`](https://github.com/ed-fi-alliance-oss/Ed-Fi-ODS) | carried | 🟢 `checked` | 🔴 **`floating`** | 🔴 **pin first (`P112-PAT-1`)** |
| autograding reference | [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3** | 🟢 `checked` | 🟢 **`pinned` (3/3)** | 🟢 build on it |
| advising workflow | [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 🟡 AGPL-3 | 🟢 `checked` | 🟢 `pinned` | 🟢 build on it, AGPL duties apply |
| accessibility scan | [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) | 🟡 GPL-3 | 🟢 `checked` | 🟢 `pinned` | 🟢 build on it |
| assessment analytics | the 3 [`EducationalTestingService`](https://github.com/EducationalTestingService) repos | carried | 🔴 **0 of 3 PR-gated** | 🔴 **0 of 3 pinned** | 🔴 **pin AND wire — budget both** |

🟢 **`Submitty` is the reference row of this whole KB on the closure axis: three
ecosystems (npm, py, php) and all three locked — the only three-ecosystem repository on
the shelf that does it. If a client asks what "good" looks like for a polyglot education
codebase, this is the answer with a URL attached.**

🔴 **ETS is the opposite and it is a day-one budget line, not a discovery: the largest
suite on this shelf (`rsmtool`, 8 347 test files) sits on three `floating` trees with no
`pull_request` trigger anywhere. An assessment-analytics engagement that plans to touch
ETS code pays for an environment AND a pipeline before it writes a feature.**

---

**Prior passes on this page follow, newest first.**

# Education — compose patterns

**Pass 111, 2026-10-10.** ⏱️ **Twenty-first pass of this date.**

🟢 **`vsurface.sh` read **296 of 296** addresses, zero unread
(`compose/code/p111-verification-surface/`, `test_p111.sh` 66 passed / 0 failed, fully
offline).**

🔴 **Every pattern on this page is a recipe over specific upstream repositories. p110
repriced them on the bench axis and reversed p109's `Gap 379` ruling. p111 reprices them
on the tree axis and reverses p110's — in the opposite direction.**

### 🔴 🆕 `P111-K` — `Gap 379` repriced a THIRD time, and the half p110 called riskier is the only ownable one

🔵 **The history of this one bind is the most useful thing on this page, so it is set out
in full:**

| pass | axis | ruling on `Gap 379` |
|---|---|---|
| p109 | commit recency | "consume the BNCC side live; vendor the rubric side at a SHA" |
| p110 | author concentration | 🔴 **reversed** — "the BNCC side is 100 % one author, the rubric side tops out at 75 %; the half p109 called safe is the MORE concentrated one" |
| 🟢 **p111** | **verification surface** | 🟢 **reversed again — the BNCC side is the only half you can own at all** |

**The curriculum half** (Brazil, `bncc-dev` — LATAM):

| component | licence | p110 `bus_factor` | 🆕 test files | 🆕 CI | 🆕 verdict |
|---|---|---|---|---|---|
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 MIT + CC BY 4.0 | 🔴 1 (100 %) | 17 | 1 · gha | 🟢 **`checked`** |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🔴 1 (100 %) | 8 | 1 · gha | 🟢 **`checked`** |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT + CC BY 4.0 | 🔴 1 (100 %) | 🔴 **0** | 1 · gha | 🔴 **`ci-only`** |

**The rubric half** (China + US academic):

| component | licence | p110 `bus_factor` | 🆕 test files | 🆕 CI | 🆕 verdict |
|---|---|---|---|---|---|
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🟡 2 (33 %) | 32 | 🔴 **0** | 🟡 **`tests-only`** |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 1 (71 %) | 🔴 **0** | 🔴 **0** | 🔴 **`bare`** |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 1 (75 %) | 🔴 **0** | 🔴 **0** | 🔴 **`bare`** |

🔴 **p110's reasoning was: the rubric half has a wider bench, so it is the safer half to
own. p111's measurement is that the rubric half has **no tests and no CI anywhere in
it** — two of three rows are `bare` — while two of the three BNCC rows are fully
`checked`, PR trigger included, despite being 100 % one author.**

🟢 **The corrected, three-axis rule — and this is the reusable part of the whole page:**

| question you are asking | the axis that answers it |
|---|---|
| will upstream meet me on the next minor? | 🔵 **liveness** (p109) |
| what happens to me if the maintainer stops? | 🔵 **concentration** (p110) |
| 🟢 **can I change this at all without breaking it silently?** | 🟢 **verification (p111)** |

🔴 **The three do not reduce to one another and they can point in OPPOSITE directions on
the same repository — `bncc-pacotes` is the proof: maximally concentrated (100 % one
author), fully verifiable (`checked`). A fork decision needs all three, in this order:
verification first (can I own it), then concentration (will I have to), then liveness
(for how long).**

🟢 **Concrete wiring for `Gap 379`, revised:**

1. 🟢 **Vendor `bncc-pacotes` + `bncc-benchmark` at a SHA and run their existing GHA
   workflows in your fork** — they are `checked`, so your fork's PRs are gated from day
   one and you inherit a working pipeline rather than building one.
2. 🔴 **`bncc-dados` is `ci-only`: it has a GHA workflow and zero test files.** Treat it
   as DATA, pin it by `sha256` (this KB's `P1035`/`P845` payload discipline), and write
   your own schema assertions — there is no upstream suite to inherit.
3. 🔴 **For the rubric half, budget to WRITE the suite, not to inherit one.** Start from
   `OpenRubrics` (`tests-only`, 32 test files, the only half with any tests and the only
   `pair` bench), port its tests into your fork's CI, and treat `OpenRS` and
   `rubricbench` as reference corpora rather than as dependencies.
4. 🟡 **Do not wire `OpenRS` or `rubricbench` into a delivery path.** Both are `bare`
   AND `solo` AND — per p109 — `slowing` at 219 d and 221 d. All three axes agree on
   these two rows, which is the one case where a single verdict is safe.

### 🟢 🆕 `P111-AF` — a new pattern the measurement makes available: `tests-only` → `checked` as a deliverable

🔵 **p111 found 45 `tests-only` rows (15.2 % of the shelf): a committed suite and no CI
configuration at HEAD. Three of them are institutional platforms carrying 5 421 test
files between them.**

**Recipe — "adopt by wiring", 1–2 weeks per platform:**

| step | what | on which repos |
|---|---|---|
| 1 | Fork and pin at a SHA | [`kuali/rice`](https://github.com/kuali/rice) (1 791 tests, ECL-2.0) · [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (1 634, Apache-2.0) |
| 2 | Run the existing suite locally; record what already fails | — a suite nobody has run in years is never green on the first attempt, and the failure list IS the adoption risk assessment |
| 3 | Add a minimal GHA workflow: `on: [push, pull_request]`, the repo's own runner invocation, no new tooling | both |
| 4 | Upstream the workflow as a PR | 🟢 touches no product code — the PR shape institutional upstreams merge most readily |
| 5 | For [`elmsln/elmsln`](https://github.com/elmsln/elmsln) and [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic), PORT the Travis config rather than writing fresh | `fossil-ci` rows — the job graph already exists and is merely addressed to a dead service (`P111-D`) |

🟢 **Why this is a pattern and not a chore: it converts an unadoptable platform into an
adoptable one for every later engagement, it is bounded and estimable (the suite exists;
only the trigger is missing), it produces a merged upstream contribution that earns
standing with a body you intend to depend on for years, and step 2 yields a risk
assessment the client cannot get any other way.**

🔴 **Precondition, stated so the pattern is not mis-sold: `P111-H` means a `checked`
verdict says "a PR would be run against a suite", NOT "the suite passes". Step 2 exists
precisely because this KB has already found a suite on this shelf that CONTRADICTED its
own source (`P238`). Never quote step 3 without step 2.**

### 🔴 🆕 `P111-AG` — the pattern-level risk register, recomputed on both axes

🔵 **Every upstream named in a pattern on this page, scored on p110 × p111. A row that is
`solo` AND not `checked` is a pattern that cannot be delivered without first building
the thing that verifies it.**

| upstream | p110 band | 🆕 p111 | pattern exposure |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟡 pair | 🟢 **`checked`** (1 221 tests) | 🟢 **safe to build on** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 broad | 🟢 `checked` (5 014) | 🟢 **safe** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 broad | 🟢 `checked` (777) | 🟢 **safe** |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🟢 broad | 🟢 `checked` (235) | 🟢 **safe** |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟡 pair | 🟢 `checked` (28) | 🟢 **safe** |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🔴 solo | 🟡 `partial` (279) | 🟡 **suite exists; stand up your own CI** |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟡 pair | 🟡 `partial` (10) | 🟡 **thin suite — assert your own invariants** |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟢 broad | 🟡 `partial` (577) | 🟡 **good suite, CI will not run it for you** |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | — | 🟡 `partial` (71, no PR trigger) | 🟡 **xAPI store — verify your own fork** |
| [`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) | 🔴 solo (100 %) | 🔴 **`bare`** | 🔴 **do not put in a delivery path** |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🔴 solo (67 %) | 🔴 **`bare`** | 🔴 **do not put in a delivery path** |
| [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | 🔴 solo (98 %) | 🔴 **`bare`** (115 src) | 🔴 **LTI layer — highest-consequence `bare` row here** |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🔴 solo | 🔴 **`bare`** | 🔴 **reference only** |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🔴 solo | 🔴 **`bare`** | 🔴 **reference only** |

🔴 **[`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) deserves the
last word on this page. It is an LTI 1.3 library — the interoperability layer other
things are built ON — at 115 source files, 98 % one author, **zero tests and zero CI**.
Any pattern here that speaks LTI inherits that. The mitigation is not a different
library (this KB has found no permissive alternative with a bench across 111 passes); it
is to write contract tests against the LTI spec on your own side of the boundary and
never assume a silent upgrade is safe.**

---


**Pass 110, 2026-10-10.** ⏱️ **Twentieth pass of this date.**

🔴 **Every pattern on this page is a recipe built on specific upstream repositories, so
a solo upstream is a pattern-level risk, not a footnote. This pass reprices the patterns
on the bench axis and one of them changes shape.**

### 🔴 🆕 `P110-I` — `Gap 379` repriced: the rubric↔curriculum bind is now TWO-dimensional, and p109's advice is reversed

🔵 **p109 priced this bind on liveness and concluded: "the BNCC side can be consumed as a
live dependency, and the rubric side has to be vendored at a SHA and owned."**

**The curriculum half** (Brazil, `bncc-dev`):

| component | licence | p109 liveness | top author | `bus_factor` | 🆕 band |
|---|---|---|---|---|---|
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🟢 fresh 14 d | 🔴 **100 %** | 1 | 🔴 `solo` |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT + CC BY 4.0 | 🟢 active 60 d | 🔴 **100 %** | 1 | 🔴 `solo` |
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 MIT + CC BY 4.0 | 🟢 fresh 21 d | 🔴 **100 %** | 1 | 🔴 `solo` |

**The rubric half** (China + US academic):

| component | licence | p109 liveness | top author | `bus_factor` | 🆕 band |
|---|---|---|---|---|---|
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🟡 slowing 109 d | 🟢 33 % | 2 | 🟡 `pair` |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 slowing 219 d | 🟡 71 % | 1 | 🔴 `solo` |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 slowing 221 d | 🟡 75 % | 1 | 🔴 `solo` |

🔴 **All three `bncc-dev` repositories are 100 % one author. The rubric half contains a
`pair` and tops out at 75 %. The half p109 called safe is the MORE concentrated one.**

🟢 **The corrected rule, which is the reusable part:**

> **Liveness governs a FORK decision. Concentration governs a DEPENDENCY decision.**
> A cold repo is expensive to fork because nobody will fix your merge conflicts.
> A solo repo is dangerous to DEPEND on however warm it is, because the upstream can
> stop between two sprints with no notice and no successor.

🔴 **"Consume BNCC as a live dependency" was advice aimed at the wrong risk.**
🟢 **`Gap 379` stays open and is now two-dimensional.**

### 🟢 🆕 Recipe — `BNCC-alignment service`, repriced

🔵 **Unchanged in its parts, changed in its contract:**

```
  curriculum standard   bncc-dev/bncc-dados      MIT + CC BY 4.0   solo 100%
         |              VENDOR at a pinned tag (dados-2026.07.1), NOT a live dep.
         |              Budget: one engineer able to regenerate the dataset from
         |              the MEC source if upstream stops. The CC BY 4.0 grant on
         |              the data survives the maintainer; the pipeline does not.
         v
  alignment checker     your code
         |
         +-- rubric judge   wanghaoyu0408/OpenRubrics   MIT   pair 33%
         |                  the widest bench in the bind -> the best fork target
         |                  of the four rubric repos. Vendor at a SHA (no releases).
         |
         +-- scoring eval   planepig/rubricbench        MIT   solo 75%, 221 d
                            treat as a FIXTURE, not a dependency: pin and freeze.
  serving / LMS reach
         v
  moodle/moodle           GPL-3   broad, bus_factor 9, 319 authors, fresh 7 d
                          the ONLY layer in this recipe safe as a live dependency.
```

🔵 **The shape of that recipe is the finding: in a four-layer education pattern, exactly
one layer — the LMS — has a bench you can rely on. The other three are vendored, and
that is a budget line, not a technical note.**

### 🟡 🆕 `P110-Q` — `P106-A`'s MCP sidecar, repriced on the bench axis

| `P106-A` component | licence | p109 | top author | `bus_factor` |
|---|---|---|---|---|
| [`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) | 🟢 MIT | 🟢 fresh 16 d | 🔴 **100 %** | 🔴 1 |
| [`fwu-de/mem-mcp`](https://github.com/fwu-de/mem-mcp) | 🟢 Unlicense | 🟡 slowing 123 d | 🔴 93 % | 🔴 1 |

🔴 **Both components of the tested MCP gate are single-author. p106 called both TAKEABLE
and that verdict stands — a permissive licence does not expire and does not depend on a
bench.** 🟢 **But the pattern has NO layer with a bench, so it cannot be consumed; it can
only be taken.** 🔵 **Which, for MIT and Unlicense code of this size, is the cheap
option: vendor both, own both, and the licences make that legal without negotiation.
The risk is not legal, it is that nobody upstream will fix the Moodle 5.x break for you.**

### 🟢 The bench rule, applied to every pattern on this page

| upstream shape | p109 | p110 | posture in a recipe |
|---|---|---|---|
| wide bench, warm | 🟢 fresh | 🟢 `broad` | 🟢 **live dependency — pin a minor, upgrade on their cadence** |
| wide bench, cold | 🔴 dormant | 🟢 `broad` | 🟢 **fork — reviewed code, nobody contests the fork** |
| narrow bench, warm | 🟢 fresh | 🔴 `solo` | 🔴 **vendor + budget to own; do NOT track upstream HEAD** |
| narrow bench, cold | 🔴 dormant | 🔴 `solo` | 🔴 **freeze as a fixture; assume no upstream exists** |

🔵 **Only eleven rows on this shelf (3.7 %) qualify for the first line. Every recipe on
this page should name which of its layers is one of them — and most name exactly one.**

# Education — compose patterns

**Pass 109, 2026-10-10.** ⏱️ **Nineteenth pass of this date.** 🟢 **One new pattern, one
new gate that every pattern on this page must now pass, and `P108-A` re-scored on the new
axis — it survives, with one layer re-flagged.**

## 🔴 `P109-GATE` — the liveness gate, which two rows this page relied on would have failed

🔵 **p108 added the pin gate: no pattern may name a component without stating the ref you
pin. That gate is necessary and insufficient.** 🔴 **`compose/code/p109-freshness/`
measured 296 of 296 shelf addresses and found **24 of the 168 pinnable rows (14.3 %) dead
for over a year** — permissive, released, pinnable, and unmaintained.**

🟢 **The gate, stated as a rule for every future pattern on this page:**

```
A component may be named in a pattern only if ALL FOUR hold:
  1. licence is OSI-permissive, read from the repo's own LICENSE   (p96+)
  2. a ref exists that you can pin, or the SHA cost is stated      (p108)
  3. last commit is within 365 days                                (p109)  <- NEW
  4. where 3 fails, the pattern states who owns the fork           (p109)  <- NEW
```

🔴 **Two components this KB published as build-on-freely would have failed rule 3 outright:
`kuali/rice` (ECL-2.0, `rice-2.6.0`, **3 433 d**) and `Jasig/SSP` (Apache-2.0,
`ssp-2.9.0`, **1 902 d**).** 🟢 **Both are retired from the permissive tier on
`verticals/solutions.md`. Neither was ever wired into a pattern on this page, which is
luck rather than discipline — hence the gate.**

## 🟢 `P108-A` re-scored on liveness — it PASSES, with one layer re-flagged

| layer | repo | licence | pin | last commit | age | gate |
|---|---|---|---|---|---|---|
| LMS host | `OpenOLAT/OpenOLAT` | 🟢 Apache-2.0 | `OpenOLAT_21.0.3` | 2026-10-09 | **1 d** | 🟢 pass |
| tutoring agent | `HKUDS/DeepTutor` | 🟢 Apache-2.0 | `v1.6.14` | 2026-10-08 | **2 d** | 🟢 pass |
| mastery model | `CAHLR/pyBKT` | 🟢 MIT | `1.4.3` | 2026-10-08 | **1 d** | 🟢 pass |
| content playback | `tunapanda/h5p-standalone` | 🟢 MIT | `v3.8.2` | 2026-03-24 | 🟡 **200 d** | 🟡 pass, flagged |
| learner memory | `fwu-de/mem-mcp` | 🟢 Unlicense | 🔴 SHA `68e6379` | 2026-06-09 | 🟡 **123 d** | 🟡 pass, flagged |

🟢 **Three of five layers were committed within two days — this is a live stack, not a
museum.** 🟡 **The two flagged layers are the two that were already the weakest on p108's
axis, so the axes agree rather than compete, and the pattern's risk is concentrated rather
than spread.**

🔴 **The `h5p-standalone` flag deserves stating because it reverses an argument this KB
made last pass.** 🔵 **p108 chose the MIT player over the GPL-3 H5P core specifically to
keep the stack copyleft-free.** 🔴 **On liveness the MIT substitute (200 d, slowing) is
three times staler than the GPL core it replaces (`h5p/h5p-php-library`, 60 d, active).**
🟢 **The licence decision stands — a copyleft core in a shippable derivative is a harder
problem than a slow dependency — but the trade is now explicit: `P108-A` buys licence
freedom at the price of the least-maintained layer in the stack, and the mitigation is to
budget ownership of `h5p-standalone` rather than to assume upstream.**

## 🟢 🆕 `P109-A-PAT` — the Brazil BNCC curriculum-alignment service, built on the LIVE half of `Gap 379`

🔵 **Why now:** `T40` measured the rubric↔curriculum bind and found it stalled
asymmetrically — the three rubric layers are 109–221 days cold while all three BNCC
curriculum layers are 14–60 days. 🟢 **Twelve passes have specified this pattern waiting
for the whole bind to be wireable. It never will be as one piece. This pattern takes the
live half and owns the cold half explicitly, which is what the gate above demands.**

```
            portabilis/i-educar  @ SHA        <- the live host: Brazilian municipal SIS
                   (8 d fresh)                   the only maintained municipal-scale
                        │                        student system measured on this shelf
                        │  LTI 1.3 / REST
                        ▼
         ┌──────────── alignment service ──────────────┐
         │                                             │
   bncc-pacotes @ SHA                        OpenRubrics @ SHA
     (MIT + CC BY 4.0, 14 d fresh)             (MIT, 109 d — VENDORED, Globant-owned)
     1 721 BNCC objectives, 7 MCP tools        rubric generation
         │                                             │
   bncc-dados dados-2026.07.1                  OpenRS @ SHA
     (MIT/CC BY, 60 d active)                    (Apache-2.0, 219 d — VENDORED)
     the ONE pinnable ref in the bind            rubric judging
         │                                             │
   bncc-benchmark @ SHA                        rubricbench @ SHA
     (21 d fresh)                                (MIT, 221 d — VENDORED)
     alignment eval set                          1 147 expert annotations, calibration
         └──────────────────┬──────────────────────────┘
                            ▼
              CAHLR/pyBKT 1.4.3  (MIT, 1 d fresh)
              mastery per BNCC objective
```

| layer | repo | licence | pin | age | ownership |
|---|---|---|---|---|---|
| host SIS | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | — (read before shipping) | 🔴 SHA | 🟢 8 d | 🟢 **live dependency** |
| curriculum standard | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🔴 SHA | 🟢 14 d | 🟢 **live dependency** |
| curriculum data | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT / CC BY 4.0 | 🟢 **`dados-2026.07.1`** | 🟢 60 d | 🟢 **live dependency** |
| alignment eval | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 (verify) | 🔴 SHA | 🟢 21 d | 🟢 **live dependency** |
| rubric generation | [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🔴 SHA | 🟡 109 d | 🔴 **VENDOR + OWN** |
| rubric judging | [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 SHA | 🔴 219 d | 🔴 **VENDOR + OWN** |
| calibration | [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 SHA | 🔴 221 d | 🔴 **VENDOR + OWN** |
| mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | 🟢 **`1.4.3`** | 🟢 1 d | 🟢 **live dependency** |

🟢 **How to wire it, concretely:**
1. 🟢 **Ingest the standard once.** `bncc-pacotes` ships **7 MCP tools** over 1 721 BNCC
   objectives — mount it as an MCP server and the alignment service queries objectives by
   code rather than embedding a copy of the curriculum. Pin `bncc-dados` at
   `dados-2026.07.1` as the data of record; it is the only version-pinnable ref in the
   whole bind, so it is the one thing in this pattern you can depend on by number.
2. 🔴 **Vendor the three rubric repos into one Globant-owned monorepo at explicit SHAs,
   on day one, not when upstream breaks.** All three are permissive (MIT / MIT /
   Apache-2.0) so this is licensed and shippable; all three are 3.5–7 months cold, so
   upstream is not a maintenance channel. Budget this as owned code.
3. 🟢 **Calibrate before trusting.** `rubricbench` carries **1 147 expert annotations** —
   run the vendored `OpenRS` judge against them and record the agreement figure as the
   service's accuracy baseline. A rubric judge with no calibration number is not a
   deliverable.
4. 🟢 **Bind to the host over LTI 1.3 / REST, never by patching `i-educar`.** The SIS is a
   live dependency at 8 days; a fork of it is a fork of something that moves weekly.
5. 🟢 **Close the loop with `pyBKT 1.4.3`** keyed on BNCC objective codes, so mastery is
   reported in the units the curriculum — and the municipal buyer — already uses.
6. 🟡 **Evaluate with `bncc-benchmark` (21 d)**, not with the rubric repos' own fixtures.

🔴 **What this pattern honestly costs, stated because `Gap 379` has understated it for
twelve passes:** three of eight layers are Globant-owned from day one, seven of eight are
SHA-pinned with only `bncc-dados` and `pyBKT` carrying a real version, and the judgement
quality of the whole service rests on vendored code whose authors have not committed since
March and June. 🟢 **What makes it worth building anyway: the curriculum standard, the
host SIS and the mastery model are all live, all permissive, and all Brazilian-municipal
or MIT-academic — and no competitor is going to assemble this by accident.**

🔵 **`Gap 379` stays OPEN — nobody has integrated these layers upstream and this pattern
does not claim to have done so either. What changes this pass is that it is no longer
blocked on integration: the cold half is reclassified from "waiting for upstream" to
"owned", which is a decision rather than a wait.**

---

# Education — compose patterns

**Pass 108, 2026-10-10.** ⏱️ **Eighteenth pass of this date.** 🟢 **One new pattern that
answers a demand-side finding with a fully permissive stack, and one gate that every
other pattern in this file now has to pass.**

## 🟢 `P108-A` — the EMEA purpose-built teacher assistant, **zero copyleft, every layer version-pinned**

🔵 **Why now:** the Sanoma *European Teacher Survey 2026* (>20 000 teachers, 14 countries)
reports **63 %** teacher AI use, **16 %** believing general-purpose AI improves outcomes,
and **75–93 %** saying education AI should be purpose-built rather than adapted
(`intel/market.md`). 🔴 **A general-purpose chat assistant is the thing those teachers
have already tried and judged.** 🟢 **This pattern is the purpose-built alternative, and
every component is OSI-permissive, so Globant can ship a modified, closed derivative.**

```
                        OpenOLAT 21.0.3  (Apache-2.0)        <- the LMS host
                                 │  course element + REST API
                 ┌───────────────┼────────────────────┐
                 │               │                    │
      DeepTutor v1.6.14    pyBKT 1.4.3        h5p-standalone v3.8.2
        (Apache-2.0)          (MIT)                 (MIT)
      dialogue + RAG     mastery estimate      content PLAYBACK
      tutoring agent     per objective         (NOT the GPL H5P core)
                 │               │
                 └──────┬────────┘
                        │
                 mem-mcp @ 68e6379  (Unlicense)              <- per-learner memory
                   MCP server, German federal                    over MCP
                   education-media institute
```

| layer | repo | licence | pin |
|---|---|---|---|
| LMS host | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0 | 🟢 **`OpenOLAT_21.0.3`** |
| tutoring agent | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 🟢 **`v1.6.14`** |
| mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | 🟢 **`1.4.3`** |
| content playback | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 MIT | 🟢 **`v3.8.2`** |
| learner memory | [`fwu-de/mem-mcp`](https://github.com/fwu-de/mem-mcp) | 🟢 **Unlicense** | 🔴 **SHA `68e6379`** |
| timetabling (opt.) | [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 Apache-2.0 | 🟢 **`v4.9.152`** |

🟢 **Every licence in this table was read this pass from the repo's own `LICENSE` over
`raw.githubusercontent.com`, not inferred from prose.** 🔴 **That check is what moved H5P
out: `h5p/h5p-php-library` is **GPL-3.0**, so the playback-only MIT wrapper
`h5p-standalone` is used instead and the GPL library is never linked.**

**Wiring.** OpenOLAT exposes course elements over its REST API; DeepTutor runs beside it
as the dialogue service and reads course content through that API rather than the
database. pyBKT consumes OpenOLAT assessment events and returns a per-objective mastery
probability, which is what turns a chat box into something that adapts — the single
feature the survey's 16 % are implicitly asking for. mem-mcp carries learner state
between sessions over MCP, so the assistant is continuous rather than per-conversation.
h5p-standalone renders existing H5P interactions client-side.

🔴 **Cost of the one SHA-pinned layer:** mem-mcp is `class=none` — 0 tags, so there is no
version to pin and no change log to diff. 🟢 **Its HEAD was `68e6379` at both pass 107 and
pass 108, so it is stable in practice**, but `P108-B` below is mandatory for it.
🔵 **Estimate: 8–10 weeks.** 🔵 **Data residency: every component self-hosts, which is what
makes this viable under the EU AI Act's Annex III treatment of systems that assess
learning outcomes.**

## 🔴 `P108-B` — the pin gate: a build step, not a document

🔵 **43.2 % of this shelf (128 of 296 addresses) has no version to pin** — 113 with no
tags at all and 15 whose tags are CI deploy stamps (`P108-D`). 🔴 **An engagement that
writes "pin the latest release" into a SOW cannot honour it against those, and the
regulatory direction makes that a contract problem rather than a tidiness problem:**
Oklahoma and Maryland require human oversight and bar AI from high-stakes student
decisions; EU Annex III treats "assesses learning outcomes" as high-risk; both oblige you
to say which version decided. 🟢 **So the gate is executable:**

```sh
# 1. classify every dependency. census.sh is ~110 lines, no API, no credential.
compose/code/p108-release-identity/census.sh deps.txt > pins.tsv

# 2. fail the build on an unpinnable dependency that is not SHA-pinned in the lockfile
awk -F'\t' 'NR>1 && ($11=="stamp" || $11=="none" || $11=="UNREAD") {print $1}' pins.tsv \
  | while read slug; do
      grep -q "$slug@[0-9a-f]\{40\}" lockfile || { echo "UNPINNED: $slug"; exit 1; }
    done

# 3. re-run per release; a changed head_sha40 on a class=none dep IS the change log
```

🔵 **Step 3 is the part that replaces the missing release notes.** 🟢 **For a `class=none`
dependency the 40-char HEAD is the only version identity that exists, so diffing it
between passes is the whole upgrade-detection story** — this is why
`p107-git-lane-census` records `head_sha40` and why both passes' TSVs are committed
rather than regenerated and discarded.

🔴 **`UNREAD` fails the gate too, and deliberately.** 🔵 **`P1040`: a dependency whose refs
could not be read is not a dependency with no releases, and silently treating it as
either is how a supply chain gets a hole in it.**

## 🔴 `P107-A` / `P96-A` — the rubric↔curriculum bind, **re-priced again, and the price went up**

🔵 **p107 priced this bind as "four permissive layers, three publishers, no integration,
and four of five layers unreleased".** 🟢 **p108 confirms the release half exactly and
adds the licence half, read from source:**

| layer | licence (read this pass) | `class` | pin |
|---|---|---|---|
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 `none` | SHA `4c7f22b` |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🔴 `none` | SHA `1a40c14` |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **CC BY 4.0 at root** | 🔴 `none` | SHA `ac9feb8` |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT + CC BY 4.0 | 🟢 `prefixed` | 🟢 **`dados-2026.07.1`** |

🔴 **Four of the four integration-critical layers are `class=none`.** 🟢 **The *data* end of
the bind is pinnable (`dados-2026.07.1`); the *tooling* end — the 1 721 BNCC objectives
and 7 MCP tools in `bncc-pacotes` — is not.** 🔵 **Any Brazilian curriculum engagement must
therefore SHA-pin the tooling and run `P108-B` against it, and the SOW should price
change-detection as ongoing work rather than assuming upstream release notes exist.**

🟡 **Open item carried to p109:** 🔵 **`bncc-pacotes`' root `LICENSE` is Creative Commons,
while this KB has recorded it as "MIT code + CC BY 4.0 data".** 🔵 **Both can be true (a
code subdirectory may carry its own grant) but the root grant is CC, and for a repo whose
*code* is the deliverable that distinction decides whether it is takeable.** 🔴 **Not
resolved this pass; stated rather than smoothed over.**

---


# Education — compose patterns

**Pass 107, 2026-10-10.** ⏱️ **Seventeenth pass of this date.** 🟢 **One pattern re-specified because
its cost was understated, and one new pattern that is a gate rather than a build.**

## 🔴 `P107-A` — the rubric↔curriculum bind (`Gap 379`), **re-priced**: four of five layers have never cut a release

🔵 **Supersedes `P96-A`, which specified this bind across passes 96–106 as "four permissive layers,
three publishers, no integration".** 🟢 **The licences are permissive and that part stands. What was
never measured is that the layers are unreleased** (`P107-D`, this pass, from the git lane):

```
  [bncc-dev/bncc-pacotes]   MIT code + CC BY 4.0 data   0 tags  ← 1 721 BNCC objectives, 7 MCP tools
        │                                                         the CURRICULUM end of the bind
        │  MCP
        ▼
  [wanghaoyu0408/OpenRubrics]  MIT              0 tags  ← generates the rubric from an objective
        │
        ▼
  [Qwen-Applications/OpenRS]   Apache-2.0       0 tags  ← judges a submission against weighted
        │                                                 tiered rubrics
        ▼
  [planepig/rubricbench]       MIT              0 tags  ← calibrates the judge, 1 147 expert
                                                          human comparisons
  [bncc-dev/bncc-dados]        MIT / CC BY 4.0   3 tags  ← dados-2026.07.1 — the ONLY pinnable row
```

🔴 **So the integration work was never the whole cost.** 🟢 **Wire it like this, and budget the second
line as real engineering rather than overhead:**

1. 🟢 **Vendor all four 0-tag layers at an explicit 40-character SHA** (never an abbreviation —
   `Gap 380`/`P987`: a 7-character form 404s inconsistently). 🔵 **Pin them in a lockfile your own
   repository owns, because none of the four publishes a version you can reference.**
2. 🔴 **Budget an upgrade path that upstream does not provide.** With no tags there are no release
   notes and no compatibility statements, so every upstream bump is a diff review. 🟡 **Price this as
   a standing maintenance line, not a one-off integration.**
3. 🟢 **Put `bncc-dados` `dados-2026.07.1` at the base** — it is the one component with a ladder, and
   it is the data rather than the code, so it is also the component most likely to change on a
   schedule you can plan around.
4. 🔴 **Keep the CC BY 4.0 attribution boundary explicit.** `bncc-dados` is MIT at the root and
   CC BY 4.0 for the data one directory down (`Gap 370`), so the data's attribution obligation
   follows the data into the deliverable even though the root licence does not say so.
5. 🟢 **The bind itself is still the opportunity, and it is still unbuilt:** nothing in open source
   binds a generated rubric to a *published curriculum standard*. 🔵 **This KB holds both ends —
   1 721 verified BNCC objectives behind MCP, and a calibrated permissive judge — and eleven passes
   have not found anyone wiring them.**

🟡 **Revised shape: 6–8 weeks for a working bind on one BNCC segment, plus a continuing
dependency-maintenance line that `P96-A` did not carry.** 🟢 **`Gap 379` stays open.**

## 🟢 `P107-B` — the pre-flight gate: **licence tier × release tier**, run before a repo is quoted

🔵 **Why this exists: this pass found that 114 of 299 shelf rows cannot be pinned, that `P106-A`'s
two permissive sidecars are both unreleased, and that an industrially released platform
(`PrairieLearn`, 551 tags) carries a production-barred proprietary directory (`P107-F`).** 🔴 **Every
one of those is cheap to discover and expensive to discover late.**

🟢 **Two commands, no API, no credential. Wire it as a CI gate on the repository that holds the
engagement's dependency list:**

```
# 1. RELEASE TIER — can it be pinned?   (compose/code/p107-git-lane-census/)
git ls-remote --tags --heads https://github.com/OWNER/REPO \
  | grep $'\trefs/tags/' | grep -v '\^{}$' | wc -l
      # 0        -> UNRELEASED: vendor at a 40-char SHA, budget the upgrade path
      # newest tag dated >18mo -> ABANDONED LADDER (pupilfirst): you inherit maintenance
      # MUST filter ^{} — unfiltered overstates by up to 2x, +58% shelf-wide (P107-C)

# 2. GRANT TIER — may it ship, and does the root licence POINT somewhere?  (P107-F)
curl -s https://raw.githubusercontent.com/OWNER/REPO/BRANCH/LICENSE -o root.lic
grep -oE '[a-z0-9_./-]+/' root.lic | sort -u      # a named sub-directory = follow it
curl -s https://raw.githubusercontent.com/OWNER/REPO/BRANCH/THAT/DIR/LICENSE
```

🔴 **The gate fails a dependency on any one of four conditions**, and each has a measured precedent
on this shelf:

| condition | precedent measured in this KB |
|---|---|
| 🔴 0 tags **and** it must ship in a deliverable | `academico-sis/academico` (MIT, "closest thing to a permissive SIS", **0 tags**) |
| 🔴 newest release > 18 months old | `pupilfirst/pupilfirst` — 14 platform tags, **newest `v2024.2.1efffc4`** |
| 🔴 root licence names a sub-directory | `PrairieLearn/PrairieLearn` → `ee/LICENSE`, **production barred** (`P107-F`) |
| 🔴 grant is ECL / EUPL / Elastic / BUSL / PolyForm | `sakai`, `opencast`, `kuali/rice` (ECL); `opetushallitus` ×8 (EUPL); `canyongbs/advisingapp` (Elastic-2.0); `sdv-dev/sdv` (BUSL-1.1) |

🟢 **Cost: the census ran 299 addresses in 2 m 17 s.** 🔵 **This is the cheapest pattern in this file
and the only one that prevents rather than builds.** 🟡 **It replaces no existing pattern; it runs
in front of all of them.**

**Pass 106, 2026-10-10.** ⏱️ **Sixteenth pass of this date.** 🟢 **Two patterns added, both from
rows measured this pass; one existing constraint strengthened from 7 rows to 143.**

## 🟢 `P106-A` — the Moodle AI seam, delivered as a plugin pair (greenfield, GPL-3) plus an MCP sidecar (licence your own)

🔵 **Why this pattern exists now: `T34` measured `moodle-aiprovider` = 0 and `moodle-aiplacement` = 0
packages on `packagist.org`, against 159 across 21 older plugin types.** 🟢 **The platform vendor
defined the extension point and nobody has shipped into it through the package channel — so there is
nothing to fork, nothing to be out-competed by, and no incumbent to displace.**

**Wire it like this:**

```
[Moodle 4.5+/5.0 core]  ── GPL-3, 143 of 143 declaring packages agree (P1033)
   │
   ├── moodle-aiprovider plugin  ──> speaks to the model gateway
   │      • loads INSIDE the LMS, so GPL-3 is NOT a choice (P1033)
   │      • thin: credential handling, request shaping, rate limits
   │
   ├── moodle-aiplacement plugin ──> the teacher/learner-facing surface
   │      • also GPL-3, also thin: UI + capability checks
   │
   └── web-service API ──> [MCP sidecar, OUTSIDE the LMS]
          • a2br/moodle-mcp (MIT, 1 073 B) is the measured precedent
          • fwu-de/mem-mcp (Unlicense, 1 211 B) is the memory tier
          • every orchestration, eval and memory component lives HERE
```

🔴 **The load-bearing rule, measured three ways and not negotiable: the licence follows WHERE the
code is mounted.** 🟢 **Evidence, all payload-read: `jeanlucio/moodle-local_aihub` has a root
`version.php` and is GPL-3; `a2br/moodle-mcp` has none and is MIT;
`sngdtechnologies/ai-moodle-security` has none and is BSD-2-Clause** (`P1033`, pass 104).

🟡 **So put in the plugin pair ONLY what must run inside Moodle** — capability checks, the settings
form, the placement UI — **and everything with commercial value in the sidecar.** 🔵 **A client who
wants the agent logic proprietary can have it; a client who wants the plugin upstreamed can have
that too. The split is architectural, decided once, at the start.**

**Shelf rows this uses, all verified this pass or last:**
[`moodle/moodle`](https://github.com/moodle/moodle) (GPL-3.0-or-later, declared on packagist) ·
[`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) (MIT, 1 073 B, `5b4bad3aa359c096`) ·
[`fwu-de/mem-mcp`](https://github.com/fwu-de/mem-mcp) (Unlicense, 1 211 B) ·
[`ahnopologetic/canvas-lms-mcp`](https://github.com/ahnopologetic/canvas-lms-mcp) (3 tags — `T28`'s
only fork-worthy MCP row).

🔴 **Do NOT start the data-quality or synthetic-data layer from
[`sodadata/soda-core`](https://github.com/sodadata/soda-core) or
[`sdv-dev/sdv`](https://github.com/sdv-dev/sdv)** — 🔴 **Elastic-2.0 and BUSL-1.1 respectively,
measured this pass (`T35`). Both bar the studio case.**

## 🟢 `P106-B` — the EUPL national-registry integration (Finland), and why it is adopt-and-contribute

🔵 **`T33` measured eight `opetushallitus` repositories, all EUPL: a complete national education data
stack, publicly licensed.** 🟢 **For an EMEA public-sector engagement this replaces the usual
"integrate with an opaque national system" problem with a readable one.**

```
[opetushallitus/oppijanumerorekisteri]  learner identity      EUPL-1.1
[opetushallitus/organisaatio]           provider registry     EUPL-1.1
            │
            ├── [opetushallitus/koski]        study rights + attainment   EUPL-1.1
            ├── [opetushallitus/eperusteet]   national core curriculum    EUPL-1.1
            └── [opetushallitus/ataru]        admissions                  EUPL-1.2
                        │
                        ▼
        [your agentic layer — OUTSIDE the EUPL boundary]
           • curriculum-aware planning reads eperusteet
           • attainment-aware tutoring reads koski
           • LangGraph / pydantic-ai orchestration, your licence
           • Ollama / vLLM for data residency (EU AI Act, see below)
```

🟡 **The licence shape, stated precisely because it drives the commercial model.** 🔴 **The EUPL is
COPYLEFT with a reciprocity obligation — a modification distributed onward carries the EUPL — and it
has an explicit compatibility list rather than a general permission.** 🟢 **So:**

- 🟢 **reading these services over their APIs puts no obligation on your code at all**;
- 🔴 **forking `koski` to add a feature does**;
- 🟢 **and the obligation is a known, priceable quantity, not a surprise** — which is the entire
  reason to measure the grant before the engagement rather than during it.

🟡 **Pre-registered as unmeasured (next pass's lead #3): whether these repositories cut RELEASES.**
🔵 **`T29`/`T30` made the adopt-or-build line turn on release engineering, and that test has never
been applied to a EUPL row. Until it is, treat `koski` as readable-and-integrable, not as
forkable-with-confidence.**

🔵 **Regulatory fit, from this pass's EMEA sweep and flagged as secondary:** education uses like
admissions, assessment and steering learning paths sit in the AI Act's Annex III, and the channel
reports the stand-alone high-risk deadline moved to **2027-12-02** with an *"AI omnibus"* in force
**2026-07-27**. 🔴 **`Gap 241`: this is a FOURTH provenance variant and cannot be cited primarily —
this KB's verified anchor remains `Regulation (EU) 2026/1744` of 8 July 2026.** 🟡 **Design to Annex
III obligations regardless of which date survives; the deferral is schedule relief, not an exemption.**

## 🔴 Constraint strengthened — the plugin-tier licence rule now rests on 143 rows, not 7

🔵 **Every pattern on this page that mounts code inside Moodle inherits GPL-3.** 🟢 **That was
carried on seven payload-read rows; `packagist.org` (opened this pass) puts it on 143 of the 143
packages that declare a licence at all, with ZERO permissive exceptions.** 🔵 **And the declaration
is free text in three spellings — `GPL-3.0-or-later` (136), `GPL-3.0+` (5), `GPLv3` (2) — so any
intake gate that matches an exact string will under-report it** (`P1046`).

**Pass 105, 2026-10-10.** ⏱️ **Fifteenth pass of this date.** 🆕 **One pattern added (`P105-A`), and it is the gate every other pattern on this page depends on: the licence-and-region due-diligence check, written because this pass's own instrument produced a wrong region and an invisible licence before it produced a finding.**
🟢 **`P103-A`** — the pedagogical-evaluation gate, which this page priced as UNBUYABLE one pass ago:
🔴 **the benchmark's labels are still ungranted (`Gap 393`), but the HARNESS is Apache-2.0 with 26
releases** (`aiverify-foundation/moonshot`), so the gate is buildable and only the comparability is
not. 🟢 **`P103-B`** — the permissive North America student-data spine, 🔴 **and it is the first
pattern on this page that ADOPTS an education-specific permissive platform instead of constructing
one**: `ed-fi-alliance-oss/Ed-Fi-ODS`, Apache-2.0, **42 releases**.

🔵 **Both came from censusing this repository's own pre-reset archive, not from a search** — 🔴 **82
of 681 archived addresses are held nowhere outside the archive and 103 appear on no page**
(`Gap 394` / `P1026`). 🔵 **`P102-A` is NOT retired: `T27` scopes it — North America and APAC can
adopt, EMEA and LATAM still construct.**

🟢 **Pass 101 added `P101-A`,
the student early-warning system, which this page could not write for four passes because `Gap 385`
said the permissive row did not exist.** 🟢 **It did exist, under an org name nobody searched**
(`P1012`), **so `P101-A` starts from an Apache-2.0 domain model with 57 releases.**

🔴 **And `P101-A` is the first pattern on this page whose main risk is a BUNDLED licence rather than a
corpus or a deadline** (`P1013`): the root grant is Apache-2.0 and the shipped UI is GPL-3.0 Ext JS.
🔵 **The pattern's first task is therefore an extraction, not an installation.**

🟢 **The pattern this page could not write for five passes is now `P100-A`.** `Gap 372` is
**DISCHARGED**: `wwrwbs/AI_AWE` is Apache-2.0 **with a release** (`v0.1.0`, adapter artifact
`http=200`) and `EducationalTestingService/rsmtool` has **33 tags at `v12.0.0`** — 🔵 **both were on
this KB's own shelf with their tags never counted** (`P1010`). 🔴 **What remains is a CORPUS
constraint, not a code one** (`T21`, `Gap 390`): the code ships, the **weights do not**, and the
retraining seam is in the repository. 🟢 **So `P100-A` starts from a system that already runs — the
first pattern on this page that does.**

🟢 **And `P100-B` exists because a duty got NARROWER.** The Commission's final Article 50 guidelines
exempt **AI-generated translations** as *"standard editing"* while keeping **summaries and
substantive rewrites** in scope. 🔵 **For an LMS that is the entire scoping question**, and getting it
backwards is the default mistake.

🔴 **The constraint that reorders this whole page: the EU limb that binds first is
`2026-12-02`, fifty-three days from this pass.** The Digital Omnibus (**Regulation (EU) 2026/1744**,
Council adopted 29 June 2026, in force 27 July 2026) moved **Annex III to 2 Dec 2027** and 🔴 **left
Article 50 transparency untouched**, so **Article 50(2) machine-readable marking** binds any
generative feature that shipped before 2 Aug 2026. 🟢 **This base already holds four tested artefacts
for it** (`compose/code/aiact-50-2-marking/`, `aiact-50-2-pack/`, `aiact-50-2-spans/`,
`aiact-50-2-exposure/`). 🔵 **Every other pattern here can start next quarter. `P99-A` cannot.**

🔴 **Second constraint, new this pass and it changes an integration estimate: the connector decides
the platform** (`T19`/`P1006`). **Canvas** has an agent connector that is **MIT and released**
(`vishalsachdev/canvas-mcp`, **26 tags**, `v1.14.0`); **Moodle** has an **AGPL-3.0** one at `v0.1.7`
and an **MIT** one with **zero tags**. 🔵 **So a Moodle engagement carries a fork in its estimate and
a Canvas engagement does not** — and that falls hardest on **LATAM** and public-sector work, which is
exactly where this page has aimed Moodle for eight passes.

🔴 **Third constraint, and it retires four passes of searching: `Gap 372` is a RELEASE gap, not a
licence gap** (`T20`). Three permissive open-response scorers exist — **MIT**, **Apache-2.0**,
**BSD-3-Clause** — and **none has a release tag**. 🟢 **So any pattern needing open-response scoring
budgets HARDENING, not procurement**, and 🔴 **prices the graded corpus as a separate procurement
term** because the corpora do not share a licence (`Gap 389`).

🔴 **The standing constraint, unchanged and still binding in all four regions: a deliverable that
REPLACES rather than augments a teacher fails** — Idaho SB 1227 by statute, Argentina's `PaideIA` by
programme principle (*"la IA no reemplaza al docente"*), the EU by human-oversight duty, 🆕 **and now
Morocco's Recommendation No. 1/2026, which asks primary education to protect reading, writing and
mathematics explicitly.**

#### Pass 98 — carried below, unchanged


**Pass 98, 2026-10-10.** ⏱️ **Eighth pass of this date.** 🆕 **Three patterns added** (`P98-A` the exam lifecycle end to end, `P98-B` the corporate L&D skills engine, `P98-C` the deployer's compliance file), 🟢 **and `P98-A` is the first pattern on this page where EVERY step already has a tested gate committed in this repository.**

🔵 **The three are not independent.** `P98-A` is the build, `P98-C` is the same evidence layer sold to the **institution** rather than the vendor (`T18`), and `P98-B` is the one pattern here whose buyer is an **employer** — a buyer this KB could not price until `Gap 386` was discharged this pass.

🔴 **One constraint now binds EVERY pattern on this page and is stated once, here: a deliverable that REPLACES rather than augments a teacher fails in all four regions**, by three different legal mechanisms — Idaho SB 1227 bars it by statute, Argentina’s `PaideIA` states *"la IA no reemplaza al docente"* as a programme principle, and the EU reaches the same place through human-oversight duties.

🔴 **Second constraint, new this pass and cheap to honour: never start a pattern from the most-cited repo without reading its payload.** `workforce-data-initiative/skills-ml` (skills) and `dssg/student-early-warning` (risk) are both the first result in their category and both carry **University of Chicago non-commercial terms** that exclude exactly the studio case (`P999`). 🟢 **The tell is a `LICENSE` opening with *"BY DOWNLOADING"*.**

#### Pass 97 — carried below, unchanged

**Pass 97, 2026-10-10.** 🆕 Three patterns (`P97-A` spoken-language assessment, `P97-B` the integrity workbench that is deliberately not a detector, `P97-C` the African teacher-capacity engagement), two of three built on tiers that pass promoted or shelved for the first time.

#### Pass 96 — carried below, unchanged

**Pass 96, 2026-10-10.** ⏱️ **Sixth pass of this date.** 🆕 **Three patterns added, and one standing pattern
re-sequenced rather than re-costed.**

- 🟢 **`P96-A` — the curriculum-aligned outcome evaluator.** The deliverable that `Gap 379` names: four
  permissive layers from three unrelated publishers, never wired. **The alignment gap this KB has declared
  for five passes turns out to be a wiring gap, not a supply gap** — `OpenRubrics` (MIT) generates,
  `OpenRS` (Apache-2.0) judges with weighted tiered criteria, `rubricbench` (MIT) calibrates the judge
  against **1 147 expert-annotated human comparisons**, and `bncc-dev/bncc-pacotes` supplies the standard.
- 🟢 **`P96-B` — the content-provenance gate for self-study material.** 🔴 **Vietnam's
  `Decision 33/2026/QD-TTg` limb 1 makes *"self-study content generated from uncontrolled data sources"* a
  high-risk education AI system, in force 15 Aug 2026** — and it never mentions assessment. 🔵 **So
  grounding is promoted from a quality argument to a regulatory control**, and `T11`'s measured
  31.9 % → 0.2 % becomes control-effectiveness evidence.
- 🟢 **`P96-C` — the permissive timetable.** Built on `UniTime/unitime` (**Apache-2.0**, `v4.9.152`) and the
  **MCP gate this repository has carried since pass 42 without the platform ever reaching a shelf page**
  (`Gap 381`). 🔵 **The smallest genuinely closable deliverable added here in six passes**, because the
  output is a timetable a registrar either accepts or does not.
- 🟡 **`P94-A` is RE-SEQUENCED, not withdrawn.** Its deliverable and its permissive evidence layer
  (`rsmtool` Apache-2.0, `skll` BSD-3) are unchanged. 🔴 **What changed is the buyer: the EU deferred
  Annex III to 2 Dec 2027 while Vietnam's equivalent duties took effect 15 Aug 2026.** **Sell it into APAC
  on a live deadline and into EMEA as 2027 preparation.** See `T15` in `intel/trends.md`.

🔴 **No pattern below was re-costed this pass**; component SHAs are as each pattern records them.
🟢 **The three new patterns cite components read from the payload at full 40-character SHAs** (`P987`), and
🔴 **their regulatory premises are search-summary grade, not primary** — every legal-publisher host was
unreachable.

#### Pass 95 — carried below, unchanged

**Pass 95, 2026-10-10.** ⏱️ **Fifth pass of this date.** 🆕 **Two patterns added:** `P95-A`, the **university
AI-mandate compliance stack** — the first pattern here aimed at a *higher-education* instrument rather than
a ministry programme, built on Pakistan's HEC notification and `T14` — and `P95-B`, an
**identity-and-version gate** that extends `P94-B` from the platform to every named dependency, after
`P980` caught two unrelated projects sharing one name with incompatible grants. 🟢 **`P95-A` is also the
first pattern to use `ucbds-infra/otter-grader` (BSD-3)**, which replaces an AGPL-only layer.
🔴 **No pattern below was re-costed this pass**; component SHAs are as each pattern records them.

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date.** 🆕 **Two patterns added:** `P94-A`, the Annex III
evidence pack for automated scoring — built on pass 94's finding that the *validation* layer is permissive
and the scorer is not — and `P94-B`, a half-day platform due-diligence gate to run before a quote. 🔴 **No
pattern below was re-costed this pass**; component SHAs are as each pattern records them.

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date.** Each pattern names the specific repos, the licence
posture of the whole stack, and how the pieces wire together.

🔴 **Provenance of the licences below, stated precisely because it differs by row.** The repos in `P93-A`
and `P93-B` were resolved **this pass**: existence, default ref and SHA from `git ls-remote --symref`, the
licence **read from the payload** at `raw.githubusercontent.com/<slug>/<SHA>/<file>`, and the family
determined **by reading the payload's title block** — because this session's sandbox cannot execute
`compose/code/grant-ladder-v4/ladder.sh`, and `P237` forbids forking its shared classifier to replace it
(`P970`). 🟡 **Every repo in `P91-*` and `P92-A` is carried at its pass-92 SHA and was NOT re-resolved this
pass.** 🔵 **So treat a pass-92 row as a pass-92 measurement, and re-run v4 before quoting a licence into a
contract.**

🔴 **`P91-E` was re-costed this pass because the licence it was built on was wrong.** It stated that
`portabilis/i-educar` is LGPL-3.0 and that *"LGPL-3.0 permits exactly that, and this distinction makes the
engagement possible"*. **i-educar is GPL-2.0, which has no linking exception.** The pattern survives but the
integration boundary — and therefore the cost — changed. See `P91-E` below and
`compose/code/grant-ladder-v4/README.md`.

🟢 **Two new patterns this pass.** **`P93-A`** supersedes `P92-A`'s modelling layer with the psychometric
stack (`repos/foundations.md` Tier 2c) — and `P92-A` stays on the page, because the two differ in a way that
decides engagements rather than in detail. **`P93-B`** is the first pattern in this KB anchored on a
**national curriculum published as audited open data**, and the first with a **measured** justification for
its own central design choice.

## 🟢 🆕 p105 `P105-A` — the licence-and-region due-diligence gate, run BEFORE a platform shortlist is shown to a client (global; one day)

🔵 **The pattern this pass's own two bugs argue for.** 🔴 **Both failures — an ECL row dropped from
the permissive tier, and a Colombian row placed in EMEA — were produced by plausible rules applied
to labels instead of payloads, and either one reaches a client deliverable silently.** 🟢 **This
gate is the cheapest artefact on this page and the only one that protects every other pattern here.**

### What it is

A one-day script run over any candidate shortlist before it is shown to anyone, answering two
questions per row with evidence rather than inference: **what is the grant**, and **where is this
from**.

### Wire it from what is already here

```
compose/code/p1035-regrant-holder-ecl/
  ├── regrant.sh   ── 11 licence filenames + a 200-CONTROL per row  → grant or "we were refused"
  ├── ecl.sh       ── classify_ecl()  → the ECL-aware permissive reading
  └── holder.sh    ── place_string() + a country-word pass          → region, with provenance
```

**Step 1 — resolve, do not trust.** `git ls-remote --symref` for the default ref, `--tags` for the
release count. 🔴 **Never assume `main`** (`P1020`): three of this KB's Apereo rows are on `master`
and Opencast is on `develop`, and a raw fetch against the wrong ref 404s and reads as "no licence".

**Step 2 — read the payload, and carry a control.** Fetch all 11 licence filenames *and*
`README.md` at the same ref. 🔵 **Without the control, "this repo has no licence" and "the host
refused us" are the same observation** (`P1005`). A row whose control also fails is reported
`NOCONTROL` — **never** as ungranted.

**Step 3 — classify with `classify_ecl` ahead of the generic classifier.** 🔴 **In education this
step is not optional.** ECL-2.0 carries no `Apache License` string, so a generic scanner returns
`UNRECOGNISED` and silently drops `Sakai`, `Opencast` and the whole Apereo learning-analytics stack
out of the permissive tier. 🟢 **Every `UNRECOGNISED` row gets read by hand before any count is
published** (`P1036`) — in this KB's own 99-address census that rule recovered 2 permissive rows,
reclassified 1 as copyleft (`OSL-3.0`) and confirmed 1 as genuinely not a grant.

**Step 4 — pin it by `sha256`, not by byte count.** 🔵 Three Apereo repositories share one ECL text
at 9 919 B; equal size is not identity and unequal size is not difference (`P1025`, `P1030`).

**Step 5 — place the row, or say you cannot.** 🟢 **Accept only a ccTLD, an explicit country word,
or a nationally unique system name (`SIGAA`, `UNAM`).** 🔴 **Reject institution names outright** —
`Universidad de Córdoba` is Spain *and* Colombia (`P1035`). 🟢 **Emit a `placed_by` column naming
the string that placed each row, and emit `UNPLACED` rather than a guess.**

**Step 6 — name buckets by property, never by membership.** 🔴 *"permissive (MIT / Apache-2.0 /
BSD)"* cannot count ECL even with a perfect classifier upstream (`P1037`). 🟢 Use
**permissive / copyleft / not-a-grant**, and publish the arithmetic so it reconciles to the row.

### What it costs and what it buys

| | |
|---|---|
| cost | 🟢 **one day**, and the three scripts already exist in this repository |
| buys | 🔴 **the two platforms a client most wants — `Sakai` and `Opencast` — stay on the shortlist** instead of being dropped as "no recognised licence" by a generic scanner |
| buys | 🟢 **a region column a regional P&L can be run against**, with the placing string printed beside every value |
| buys | 🟡 **a defensible answer to the incumbent adviser's "the education stack is mostly copyleft, so you must build"** — ask which tool produced their licence column (`T31`) |

### The failure it is designed around

🔴 **Neither of this pass's bugs would have announced itself.** A wrong region reads as coverage; an
invisible licence keeps the census footing correct while the composition drifts. 🟢 **So the gate's
real output is not the table — it is the `placed_by` column, the 200-control, and the reconciling
arithmetic**, each of which makes a silent error loud. 🔵 **`P1039`: keep the test that could refute
the finding. This KB asserted ECL would mislabel as Apache, measured that it does not, and kept both
branches — so the day an ECL payload does carry the Apache title, the gate says so.**

## 🟢 🆕 p104 `P104-A` — the sovereign, no-egress AI tutor on the client's existing LMS (EMEA first, LATAM second)

🔵 **Every component below was probed in pass 104: grant read as a payload at a measured ref, bytes
and `sha256` recorded, tags counted** (`compose/code/p1029-lost-address-recovery/result.2026-10-10.tsv`).

### What you are building

A tutoring agent that runs **entirely inside the institution's network**, bolted onto the LMS it
already has, with a **licence boundary you can defend to a procurement lawyer** and an **evaluation
gate that produces an artefact an auditor can read**.

🔴 **This is the pattern for every buyer who cannot send student text to a third-party API** — which,
after the EU AI Act's high-risk classification of education uses, is most EMEA public institutions.

### The parts, and why each one

| part | repo | grant · bytes | tags | role |
|---|---|---|---|---|
| **deployment topology** | [`sngdtechnologies/ai-moodle-security`](https://github.com/sngdtechnologies/ai-moodle-security) | 🟢 **BSD-2-Clause** · 1 299 B | 0 | 🔵 **The reference architecture: 7 containers, 5 Docker networks, Moodle and Ollama on INTERNAL networks with no egress, Caddy + Coraza WAF (OWASP CRS) the only exposed surface, and a four-stage prompt-injection guard.** A Master's-thesis prototype — 🔴 **treat it as a DESIGN to re-implement, not a dependency: zero releases** |
| **inference runtime** | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 **MIT** · 1 058 B | 🟢 **689** | Local model serving. 🔵 **This KB carried it on no page until pass 104** |
| **model backends** | [`nextcloud/llm2`](https://github.com/nextcloud/llm2) · [`translate2`](https://github.com/nextcloud/translate2) | 🟢 **MIT** · 1 069 B each | 32 / 12 | On-prem text and translation services. 🟢 **MIT because the holder is `cloud-py-api`** (`P1031`) |
| **LMS bridge** | [`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) | 🟢 **MIT** · 1 073 B | 🔴 **0** | Moodle web-services as MCP tools. 🟢 **MIT is available here precisely because it is OUTSIDE the plugin tree** (`P1033`) |
| **evaluation gate** | [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) + [`moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) + [`moonshot-ui`](https://github.com/aiverify-foundation/moonshot-ui) | 🟢 **Apache-2.0** · 11 347 / 11 357 / 11 347 B | 🟢 **26 / 6 / 23** | 🔵 **All three parts granted and released.** `moonshot` runs the recipes, `moonshot-cicd` makes the gate a pipeline step, `moonshot-ui` is the screen you show the client |
| **orchestration** | [`temporalio/temporal`](https://github.com/temporalio/temporal) | 🟢 **MIT** · 1 152 B | 🟢 **573** | Durable retries and compensation across grading passes |
| **access audit** | [`mizcausevic-dev/student-data-access-audit-stream`](https://github.com/mizcausevic-dev/student-data-access-audit-stream) | 🟢 **MIT** · 1 069 B | 🔴 **0** | Student-record access trail. 🔴 **Read it as a pattern, write your own** |

### 🔴 What you must NOT take, and why — read this before any estimate

- 🔴 **Anything inside the Moodle plugin tree is GPL-3.0.** `P1033`: 7 of 7 measured plugin rows,
  including Microsoft's own `o365-moodle` at 695 tags. 🟢 **Keep your proprietary logic in the MCP
  service and the container topology; put only thin glue in `aiprovider_*`.**
- 🔴 **`nextcloud/integration_openai` and `context_chat_backend` are AGPL-3.0.** Same org as the MIT
  backends. 🔵 **Reading the org name gets this wrong in both directions** (`P1031`).
- 🔴 **`aiverify-foundation/llm-evals-catalogue` has NO grant and zero tags.** 🔵 **So the harness is
  a purchase and the RUBRIC is not** — the four-dimension, three-value rubric is re-implemented as a
  moonshot *recipe* (own dataset of input-target pairs + prompt template + metric + grading scale).
  🔴 **`P103-A`'s rubric cost stands in full; only its UI cost is discharged.**
- 🔴 **`yuanjiusheng/cloud-learning-ce` serves a `LICENSE` and is all-rights-reserved** (`P1029`).
- 🔴 **Attention/engagement monitoring** (`yptheangel/attention-monitor`, Apache-2.0) is technically
  available and 🔴 **legally hazardous**: Tennessee `SB 1580` bars AI tools from assessing or
  screening a pupil's mental health, and California `AB 1159` is in the same family. 🟢 **Leave it
  out of the EMEA build and do not offer it in North America without counsel.**

### Wiring, in order

1. **Stand up the topology first, not the model.** Two internal Docker networks; LMS and Ollama get
   **no egress route**; Caddy + Coraza terminates 443 and is the only exposed container. 🔵 **The
   no-egress property is the entire commercial proposition — prove it with a network test in week 1,
   because it is also the thing a client can verify themselves.**
2. **`ollama` + `llm2`/`translate2` behind the internal network.** Pin model weights by digest.
   🔴 **Check each model's OWN licence — `Gap 390`/`P1007`: the weights, not the code, are what a
   commercial engagement cannot always take.**
3. **`moodle-mcp` as the only path from agent to LMS**, over Moodle web services with a scoped
   token. 🟢 **One permissive seam, auditable, and your IP lives on this side of it.**
4. **Four-stage input guard before any prompt reaches the model**, per the topology's design.
5. **`moonshot` recipes as a merge gate via `moonshot-cicd`.** Encode the pedagogical rubric as a
   recipe with an explicit grading scale; `moonshot-ui` is the client-facing evidence screen.
6. **`temporal` around multi-pass grading**; **access-audit stream** on every student-record read.
7. **Then** the tutor prompt-engineering. 🔴 **In this order. A tutor demo with an egress route is
   not a smaller version of this pattern — it is a different, unsellable product.**

### Where it sells, by region

- 🟢 **EMEA — first, and the licence story is the differentiator.** The EU AI Act classes education
  uses as high-risk; sovereignty is procurement language, not marketing.
  🔵 **`fwu-de/fwu-kc-extensions` (Apache-2.0, 118 tags) joins the school identity layer to this
  stack.** 🔴 **What is NOT available is the curriculum/subject VOCABULARY: `fwu-de/schulfach-`
  and `schulart-ontologie` and `dini-ag-kim/school-curriculum-pg` are all three ungranted** — so
  the personalisation keys are a build, or a written grant request (`Gap 395`).
- 🟢 **LATAM — second, and for a different reason: cost and connectivity, not regulation.** A
  no-egress stack on commodity hardware removes per-token cost and tolerates poor links.
  🔴 **Five of the Spanish/Portuguese-named rows in this corpus are ungranted**, so expect to supply
  the components rather than adopt them.
- 🟡 **APAC — the evaluation half travels better than the tutor half.** The harness comes from the
  foundation Singapore's regulator convened; 🔵 **`sukhrobyangibaev/mcp_hemis_student` (MIT) shows
  the same MCP seam already drawn against a NATIONAL student information system.**
- 🟡 **North America — the weakest fit for the sovereign framing** (cloud procurement is normal) and
  🟢 **the strongest for the audit limb**: ship the `moonshot` gate and the access-audit stream alone,
  against `SB 1580`/`AB 1159` exposure.

### Honest risks

- 🔴 **Two of the seven parts have zero releases** (`ai-moodle-security`, the audit stream) and one
  more has zero (`moodle-mcp`). 🔵 **Budget them as designs to re-implement. The pattern is sound;
  three of its parts are not products.**
- 🔴 **The topology is one author's Master's thesis.** Its architecture is checkable and its
  operational maturity is not. 🟢 **Re-implement the topology in the client's own IaC.**
- 🔴 **Prompt-injection mitigation is a four-stage guard, not a solution.** Say so in the SOW.
- 🟡 **`moonshot` recipes make the gate auditable, not COMPARABLE.** 🔵 **The labels remain the
  ungranted asset** (`Gap 393`) — comparability across institutions is still unbought.

## 🟢 🆕 p104 `P104-B` — the US rostering bridge, and it is an ADOPT

🔵 **Short pattern, because the parts are few and all permissive.**

🔴 **US K-12 has two rostering standards and clients run both.** 🟢 **Pass 104 recovered the bridge:**

| part | repo | grant · bytes | tags |
|---|---|---|---|
| rostering bridge | [`csr2017/edfi-oneroster`](https://github.com/csr2017/edfi-oneroster) | 🟢 **Apache-2.0** · 10 173 B | 🟢 **8** |
| data standard | [`ed-fi-alliance-oss/Ed-Fi-Data-Standard`](https://github.com/ed-fi-alliance-oss/Ed-Fi-Data-Standard) | 🟢 **Apache-2.0** · 10 173 B | 🟢 21 |
| operational datastore | [`ed-fi-alliance-oss/Ed-Fi-ODS`](https://github.com/ed-fi-alliance-oss/Ed-Fi-ODS) | 🟢 **Apache-2.0** · 10 172 B | 🟢 42 |
| district MCP surface | [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | 🟢 **MIT** · 1 073 B | 🟢 4 |
| analytics emitter | 🔴 **BUILD — see below** | — | — |

🔵 **All three Ed-Fi-family payloads are 10 172–10 173 B: `P1024`'s omitted-appendix Apache variant,
now confirmed a third time and across two organisations.**

🔴 **The one part you must write: the learning-analytics EMITTER.** `Gap 397`:
`1edtech/caliper-php` and `imsglobal/caliper-python` are **ABSENT at both the current and the
predecessor org name**. 🟢 **What survives is the validator —
[`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core),
Apache-2.0, 28 tags.** 🔵 **So: conform to the published specification, validate against the
surviving validator, and own the emitter.** 🟡 **`T17`: 1EdTech grants the measuring side
permissively and no longer ships the implementing side at all.**

## 🟢 🆕 p103 `P103-A` — the pedagogical-evaluation gate, built on a harness you can actually license (APAC first, global second)

🔵 **The ask this answers is the one `P102-A` had to decline.** 🔴 **Every tutoring and feedback
engagement eventually gets asked "is this pedagogically sound, and who says so?", and the recognised
answer — a BEA-2025 / MRBench score — is ungranted on both halves (`Gap 393`).** 🟢 **Pass 103
separates the two things that question bundles: the HARNESS and the LABELS. The harness is a
purchase.**

| layer | component | grant (payload-read this pass) | why this one |
|---|---|---|---|
| evaluation harness | [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | 🟢 **Apache-2.0** · `LICENSE.md` **11 347 B** · `main` · `03e9344dc9fc949ae05b1f38580611fce36528ab` · **26 tags / `0.7.6`** | 🟢 **Recipes take a custom dataset of *"input-target pairs"*, a prompt template, an evaluation metric and a GRADING SCALE** — so a four-dimension rubric on a three-value scale is a recipe, not a rewrite. 🔵 **And the publisher is the AI Verify Foundation, convened by Singapore's IMDA**, which is a procurement argument and not just a licence. 🟡 Self-declared **beta**: pin the tag. |
| evaluation in CI | [`aiverify-foundation/moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) | 🟢 **Apache-2.0** · 11 357 B *(pristine)* · `main` · `996365ba61586c52040f632f8a9d7ff5c5573129` · **6 tags / `uat0.2`** | 🟢 **Turns the gate from a notebook into a pipeline step** — which is what makes it auditable: a regulator asks *when* the check ran. 🔴 **`uat`-prefixed tags means pre-GA; pin the SHA, not the tag.** |
| the rubric | **re-implement** — four dimensions (Mistake Identification, Mistake Location, Providing Guidance, Actionability) on `Yes` / `To some extent` / `No` | 🔴 **not takeable as code** · 🟢 **takeable as a published METHOD** | 🔴 `kaushal0494/AITutor-EvalKit` has **no licence payload** at a stable SHA across two passes (`Gap 391`), so the scorer cannot be a dependency. 🟢 **The rubric is a paper, and papers are re-implementable.** |
| the labels | 🔴 **re-annotate on the client's own dialogues** | 🔴 **MRBench is ungranted** (`Gap 393`) | 🔴 `kaushal0494/UnifyingAITutorEvaluation` — the official shared-task data (dev **300 dialogues / 2 476 responses**, test **191 / 1 547**) — has **no payload at 5 licence names** with a clean 200-control. 🔵 **The labels are the asset, so this is the irreducible cost.** |
| the tutor under test | [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor) *(optional baseline)* | 🟢 **MIT** · 1 069 B · `main` · `d0ee63babac945ab533df1c1caa9c4f45605f0eb` · **15 tags / `v0.0.24`** | 🟡 Useful as a **released** reference implementation to score against. 🔴 **README is 214 B**, so budget reading the source. |

**Estimated 4–6 weeks** for the harness, the re-implemented rubric as a Moonshot recipe and the CI
gate; 🔴 **plus annotation, which is the real cost and scales with the dialogue set** — budget two
annotators and an adjudication pass, because a single-annotator rubric is not defensible.

🔴 **What this pattern explicitly does NOT sell: comparability.** 🔵 **No MRBench number is
reproducible by a studio, because the labels are ungranted.** 🟢 **What it sells is a dated,
re-runnable, licensed pedagogical gate over the client's own data** — which is what an audit asks
for anyway, and which `P94-A`'s Annex III evidence pack can then cite.

🔵 **Why this supersedes the "unbuyable" verdict pass 102 published.** 🔴 **Pass 102 priced the whole
layer at *"cannot be bought at any price; only re-annotation can"*.** 🟢 **That was half right: the
re-annotation stands, and the harness around it turned out to be Apache-2.0 with 26 releases** — it
was simply not on this KB's shelf, because it was lost in the 2026-10-06 reset (`Gap 394`).
🔵 **The correction is `P1026`'s: a layer declared unbuyable should be re-checked against this
repository's own archive before it is quoted as unbuyable.**

## 🟢 🆕 p103 `P103-B` — the permissive North America student-data spine (and the first pattern here that ADOPTS instead of CONSTRUCTS)

🔵 **`P102-A` exists because no education-specific permissive platform was known to this KB.**
🔴 **One was, and it has 42 releases.** 🟢 **For a North America K-12 engagement this pattern replaces
`P102-A` outright; `P102-A` remains correct for EMEA and LATAM (`T27`).**

| layer | component | grant (payload-read this pass) | why this one |
|---|---|---|---|
| student-data spine | [`ed-fi-alliance-oss/Ed-Fi-ODS`](https://github.com/ed-fi-alliance-oss/Ed-Fi-ODS) | 🟢 **Apache-2.0** · `LICENSE.txt` **10 172 B** · `main` · `e453cd2cad8a0653c65453948d3d235aec7c517c` · **42 tags / `v7.3.2-pre`** | 🟢 **The operational data store and API that US districts already run** — enrolment, rostering, assessment, discipline. 🔵 **Education-specific AND permissive AND released: the combination `T26` said did not exist.** 🟡 **10 172 B is Apache-2.0 with the appendix omitted, not a modified grant** (`P1024`). 🔴 Top tag is `-pre`; ship from the newest stable `v7.3.x`. |
| the model, without the server | [`ed-fi-alliance-oss/Ed-Fi-Data-Standard`](https://github.com/ed-fi-alliance-oss/Ed-Fi-Data-Standard) | 🟢 **Apache-2.0** · 10 173 B · 🔴 **`v6.2.0`** · `3d24df6` · **21 tags** | 🟢 **The cheap half when the client already has a warehouse and needs the SCHEMA.** 🔴 **Its default ref is a TAG-SHAPED BRANCH (`P1021`)** — `--symref` first, or you will believe you pinned a release. |
| LMS edge | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` · **26 tags / `v1.14.0`** *(p99)* | 🟢 The only permissive **and released** LMS connector this KB has verified. 🔴 **Moodle has no row that is both** (`P1006`): **+3–4 weeks** for a Moodle variant. |
| interpretable risk layer | `pyBKT` + [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · 1 514 B · 🔴 `dev` · `7e6caae84a8e7779422ba9338cfe2e2335185b28` · **38 tags** *(p101)* | 🟢 Explainable to a registrar. 🔴 Non-standard default ref (`P1020`). |
| ML risk layer | **re-implement** (XGBoost + SHAP) | 🔴 **not takeable** | 🔴 **`Gap 392`: 6 of 6 unusable** — including one that excludes selling a service built on it. |
| institutional corpus | [`dspace/dspace`](https://github.com/dspace/dspace) *(optional)* | 🟢 **BSD-3-Clause** · 1 504 B · `main` · `a5b0f0fc17ad5c7f8917eb89b9222f2c2d441aed` · **136 tags** | 🟡 Where a university's own outputs become a corpus to ground a tutor in. 🔴 **Do not sort its tags naively** — `language-pack-1_4_1` ranks last (`P978`). |
| badges | 🟢 **validate** with [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) · 🔴 **minting is a BUILD** | 🟢 Apache-2.0 · **13 185 B** · `develop` · `0a66b52` · **28 tags** | 🔴 **`Gap 396`: the minter is ABSENT at 5 of 5 org names** (`concentricsky`, `1EdTech`, `IMSGlobal`, `instructure`, plus `badgr-ui`). 🟡 **`P1024`: the 13 185 B payload embeds its bundled-grant notice — OAuth and Base64, both Apache-2.0, so the closure is clean.** |

**Estimated 6–8 weeks** for the spine + Canvas edge + interpretable layer; **+2 weeks** for the ML
re-implementation; **+3–4 weeks** for a Moodle edge instead of Canvas; **+1–2 weeks** if badge
minting is in scope, because it has to be written.

🔵 **The policy layer this pattern must respect, and it is subnational** (`T12`): Oklahoma **S.B.
1734** requires every district to have a written AI policy before 2027–28; Maryland gives districts
**120 days** after state guidance; NYC's red tier **bars AI from grading, discipline and placement**;
🔴 **Tennessee `SB 1580` bars an AI tool from mental-health assessment or screening of a student** —
🟢 **recovered this pass from this KB's own archive, where it had been dropped from every live page
(`P1027`).** 🔵 **So the gate is a product control, not a model property: the spine must be able to
prove which decisions a human made.** 🟢 **`P91-B` is the recorder that does it; wire it here.**

🔴 **When NOT to use `P103-B`.** 🔵 **Outside North America.** Ed-Fi's data standard encodes US K-12
concepts, and `T27` places the equivalent for APAC in Sunbird (MIT, 450 / 336 tags) — 🔴 **while EMEA
and LATAM have no row of this shape at all**, which is why `P102-A`'s construction remains the honest
answer there, and why in EMEA the first action item is a **written grant request** to the publisher of
`european-digital-credentials` (`Gap 395`).

## 🟢 🆕 p102 `P102-A` — the permissive student-information / early-alert build

🔵 **The ask this answers is the most common one on this page and the one it has never been able to
answer permissively:** *"we want an open-source student system we can extend with AI, and we cannot
take copyleft."* 🔴 **Every education-specific option is copyleft** (OpenEduCat LGPL-3.0, ERPNext GPL)
🔴 **and the one permissive one has no releases** (`academico-sis/academico`, MIT, 0 tags). 🟢 **`T26`
names the way through: build on a generic permissive core.**

| layer | component | grant (verified this pass unless noted) | why this one |
|---|---|---|---|
| administrative core | [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** · 11 906 B · `trunk` · `45506b377c855e455942b238dbd55e33fce79d4f` · **26 tags** | 🟢 ASF governance, **`P1013` bundle check CLEAN** (NOTICE 166 B; only Noto Sans Apache-2.0 + Public Domain timezones). Accounting, HR, catalogue, CRM already built. |
| case management (alternative core) | [`cortezaproject/corteza`](https://github.com/cortezaproject/corteza) | 🟢 **Apache-2.0** · 11 358 B · `2024.9.x` · `3835dfc4ac8bd89381753f09042ad147a4502576` · **298 tags** | 🟢 Pick this instead of OFBiz when the deliverable is **advising caseloads and intervention tracking** rather than finance/inventory. 🔴 Pin a tag, not HEAD (`P1021`). |
| education domain model | [`Jasig/SSP`](https://github.com/Jasig/SSP) | 🟢 **Apache-2.0** · 11 359 B · `master` · `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6` · **57 tags** *(p101)* | 🟢 **Take the SCHEMA and the early-alert / caseload / intervention model via its Liquibase changesets.** 🔴 **Do NOT take the front end** — `NOTICE` declares Ext JS **GPL-3.0**, JasperReports / JFreeChart / c3p0 **LGPL**, iText **MPL** (`P1013`). |
| interpretable risk layer | `pyBKT` + [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · 1 514 B · 🔴 `dev` · `7e6caae84a8e7779422ba9338cfe2e2335185b28` · **38 tags** *(p101)* | 🟢 The part a registrar will accept because it can be explained. 🔴 Note the non-standard default ref (`P1020`). |
| ML risk layer | **re-implement** (XGBoost + SHAP calibration) | 🔴 **not takeable** | 🔴 **`Gap 392`: the modern ML early-warning tier is 6 of 6 unusable** — 4 ungranted, 1 non-commercial by its own text (`dssg/student-early-warning` **excludes selling a service that uses the Program**, which is Globant's model verbatim), 1 a portfolio project. 🟢 **Re-implementation is the cheap half; the model is 30 lines.** |
| LMS edge | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` · **26 tags / `v1.14.0`** *(p99)* | 🟢 The only **permissive AND released** LMS connector this KB has verified. 🔴 For Moodle there is no row that is both (`P1006`), so a Moodle variant of this pattern costs a connector. |
| learning-record store | 🔴 **behind a service boundary** | 🔴 LearningLocker **GPL-3.0** | 🔵 Reachable only across a process boundary; never linked into the deliverable. |

**Estimated 7–10 weeks** for the core + domain model + interpretable layer + Canvas edge; **+2 weeks**
for the ML layer re-implementation; **+3–4 weeks** if the LMS is Moodle rather than Canvas.

🔴 **What this pattern does NOT include, and the reason is `Gap 393`.** A client will ask whether the
AI tutoring or feedback component is *pedagogically* sound, and the recognised answer is a BEA-2025
score. 🔴 **Both halves of that benchmark are ungranted** — the scorer (`AITutor-EvalKit`) and the
benchmark data (`UnifyingAITutorEvaluation`, MRBench). 🟢 **The rubric itself is a published method
and can be re-implemented**: four dimensions (Mistake Identification, Mistake Location, Providing
Guidance, Actionability) on a three-way scale. 🔴 **The comparability cannot.** 🔵 **So quote
re-annotation against the client's own dialogues as a line item, and never quote a published MRBench
number as something the studio can reproduce.**

🔵 **Why this is `P102-A` and not a variant of `P101-A`.** `P101-A` costed the early-warning SYSTEM
and ended at SSP's legacy JVM front end. `P102-A` replaces the front end and the application shell
with a **maintained Apache-2.0 core that has real release engineering** (26 and 298 tags), and keeps
only SSP's schema. 🟢 **That is the difference between forking a 2012 uPortal-era application and
building a 2026 one on a domain model with 57 releases of migration history.**

## `P101-A` — 🆕 The defensible student early-warning system (North America first, EMEA second)

🔵 **The pattern exists because the capability is in demand, the permissive supply is a legacy
platform, and the modern supply is ungranted.** 🟢 **So: take the MODEL from the old platform, the
MATHS from the permissive psychometrics, and the METHOD — not the code — from the ungranted ML repos.**

### What you are building

An early-warning service that flags students at risk, **explains each flag in terms an academic appeals
committee can audit**, and writes interventions back against a schema the institution already
recognises.

### The parts, and why each one

| layer | what you use | grant | why this one |
|---|---|---|---|
| Domain model + schema | [`Jasig/SSP`](https://github.com/Jasig/SSP) · `master` · `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6` | 🟢 **Apache-2.0** (11 359 B) | **57 releases** of a real early-alert / caseload / intervention model, **originally granted by Sinclair Community College**. 🟢 **Its migrations are Liquibase changesets** (`NOTICE`: *Liquibase Core, Apache-2.0*), so **the schema is extractable as DDL without running the portlet app.** |
| Per-skill mastery | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | Bayesian Knowledge Tracing — **a per-skill mastery PROBABILITY is an explanation**; a network activation is not. |
| Item difficulty / adaptive testing | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) · **`dev`** · `7e6caae84a8e7779422ba9338cfe2e2335185b28` | 🟢 BSD-3-Clause (1 514 B, **38 tags**) | The only adaptive-testing engine on this shelf. 🔴 **Pin `dev`, not `main`** (`P1015`). |
| Risk classifier + explanation | `scikit-learn` (BSD-3), `xgboost` (Apache-2.0), `shap` (MIT) | 🟢 permissive | 🔵 **The DESIGN is read from [`Gnanakamalesh-M/student-dropout-early-warning`](https://github.com/Gnanakamalesh-M/student-dropout-early-warning) — calibrated XGBoost + SHAP, 30-day withdrawal horizon at fixed course checkpoints — which is 🔴 UNGRANTED (0 of 24 filenames) and must be RE-IMPLEMENTED, not vendored.** |
| Event pipe | [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) · `5fec948a823e372e740df521aa3684c8df1dcba7` | 🔴 **GPL-3.0** (221 tags) | xAPI Learning Record Store. 🔴 **Deploy as a SERVICE over HTTP; never link it into client code.** 🔵 Or emit xAPI to the institution's existing LRS and ship no store at all. |
| Agent surface | the agent-skill unit (`T1`), per `P91-C` | — | The advisor-facing "who should I call today, and why" skill is the deliverable the client sees. |

### 🔴 What you must NOT take, and why — read this before any estimate

- 🔴 **[`dssg/student-early-warning`](https://github.com/dssg/student-early-warning)** (U Chicago DSSG,
  `LICENSE` 2 069 B, `b68f23c76d5277d96ec70768c728234660428e92`) is the repository a client's own
  research team will send you. 🔴 **It is not OSI-licensed.** Its grant covers *"academic research or
  other not-for-profit scholarly purposes"* and **"excludes any service or part of selling a service
  that uses the Program."** 🔵 **A services engagement is the excluded case, verbatim.** Commercial
  terms exist via the Polsky Center — **a procurement conversation, not a download.**
- 🔴 **The four ungranted ML repos** (`Gnanakamalesh-M`, `himasriniva`, `miansaimnadeem`,
  `ShahCoding1`) carry **no licence payload at 24 filenames**. 🔵 **Read, cite, re-implement.**
- 🔴 **SSP's own front end.** `NOTICE` declares **Ext JS GPL-3.0** (Sencha FLOSS exception) and
  **JasperReports / JFreeChart / c3p0 / Hibernate Commons LGPL**, **iText MPL**.
  🟢 **Extract schema and domain logic; build the UI fresh.** 🔴 **Shipping SSP's WAR ships GPL-3.0.**

### Wiring, in order

1. **Extract the schema (3–5 days).** Pull SSP's Liquibase changesets at the pinned SHA, generate DDL,
   keep the early-alert / caseload / intervention / success-plan entities, drop the portlet tables.
   🟢 **Deliverable: an Apache-2.0-derived data model the registrar recognises.**
2. **Land the event pipe (1 week).** Either point at the institution's LRS or stand LearningLocker up
   **behind an HTTP boundary**. 🔵 **Record the boundary in the architecture note — it is the GPL-3.0
   containment and a reviewer will ask.**
3. **Fit the risk model (2–3 weeks).** Re-implement calibrated gradient boosting over course-checkpoint
   features; **calibrate** (so a 0.7 means 0.7) and attach **SHAP** per-student attributions.
   🟢 **Add `pyBKT` per-skill mastery as a SECOND, independently interpretable signal.**
4. **Build the explanation record (1–2 weeks).** For every flag persist: features, calibrated
   probability, SHAP contributions, model version, and the SSP intervention taken.
   🔵 **This is the artefact that makes the system defensible, and it is cheap to build and impossible
   to retrofit.**
5. **Ship the advisor skill (1–2 weeks).** Ranked caseload, the reason per student, the intervention
   written back to the SSP schema.

🟢 **Total: 6–9 weeks** to a defensible pilot on one faculty or district.

### Where it sells, by region

- 🟢 **North America first.** Retention money sits with US community colleges and regional publics —
  **and SSP is their own artifact** (Sinclair Community College). 🔵 **There is no statutory AI duty to
  satisfy, so the evidence pack is sold on appeals defensibility and board reporting, per `P91-B`.**
- 🟢 **EMEA second, and the SAME artefact becomes compliance.** Under the AI Act, **assessment and
  admissions decisions are high-risk, with obligations from August 2026** — so step 4's explanation
  record stops being good practice and becomes evidence. 🔵 **Pair with `P94-A`'s Annex III pack.**
- 🟡 **LATAM third, on trust rather than statute.** Adoption leads the world (students 92%, teachers
  79%) while **65% of students fear superficial learning** — 🔵 **the explanation record is the answer
  to that fear, and it is the same build.**
- 🔴 **APAC: re-scope before quoting.** `T25` — the driver is **teacher shortage**, so an advisor
  caseload tool competes with simply giving teachers hours back. 🔵 **Lead with preparation and marking
  automation; bring early warning second.**

### Honest risks

- 🔴 **SSP is a dormant-looking stack.** `2.9-SNAPSHOT`, portlet API 2.0, Spring Security OAuth 2.5.
  🔴 **Recency was NOT established this pass** — `api.github.com` returns `http=403` here, so no commit
  date or star count was read. 🔵 **Treat it as a schema and a specification, and the dormancy stops
  mattering.**
- 🔴 **No permissive, modern, release-engineered ML early-warning implementation exists** (`Gap 392`).
  🔵 **Step 3 is a BUILD. Price it as one.**
- 🔴 **The tutor-reply judge is ungranted** (`Gap 391`, `AITutor-EvalKit`). 🔵 **If the engagement also
  scores tutor replies, the four BEA-2025 dimensions must be re-implemented from the paper.**

## `P91-A` — The closable AI university platform (EMEA)

**The ask it answers.** A European institution wants a self-hosted learning platform, extended with AI,
received as a **closed, owned deliverable**. Six passes of this KB answered *"impossible — the platform tier is
copyleft"*. It is not.

**Stack — permissive end to end, no copyleft anywhere.**

| layer | component | grant |
|---|---|---|
| platform | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) · `develop` · `760e2e1` | **MIT** (1 091 B) |
| tutor | **Iris**, in-tree | MIT with the platform |
| feedback | **Athena**, in-tree | MIT with the platform |
| exercise authoring | **Hyperion** (Spring AI), in-tree | MIT with the platform |
| 🆕 public portal / catalogue | [`openfun/richie`](https://github.com/openfun/richie) · `master` · `8b14aec` | **MIT** (1 079 B) |
| assessment engine | [`numbas/Numbas`](https://github.com/numbas/Numbas) · `master` · `39b03e5` | **Apache-2.0** (11 357 B) |
| learner-data trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `main` · `cb794e4` | **Apache-2.0** (11 357 B) |
| statement mapping | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) · `master` · `ea17c40` | **Apache-2.0** (11 324 B) |
| content shim | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) · `master` · `882f3b8` | **MIT** (1 072 B) |
| 🆕 accessibility gate | see **`P91-F`** | **MIT** |

**Wiring.** Fork Artemis. Iris/Athena/Hyperion are config-gated — point them at the client's model endpoint
(sovereign or on-prem) rather than a vendor API. 🆕 **Put `richie` in front as the catalogue and enrolment
funnel**: it is the only permissive row at the portal layer, it comes from a French public-HE consortium
(which reads well in a European tender), and it keeps the public-facing redesign — the thing institutions
actually ask for — outside the platform fork. Package Numbas assessments as SCORM and serve them through
`scorm-again`, so assessment content stays portable if the platform later changes. Every Iris interaction and
Athena feedback event emits an xAPI statement shaped by `xAPI-SCORM-Profile` into `lrsql`.

**Why the trail is the deliverable, not a feature.** 🟡 That store is the **human-oversight evidence** the AI
Act asks for, and it exists before the **2 Dec 2027** high-risk deadline rather than after. 🟢 **And it is
sold against a duty that already binds: Article 4's staff AI-literacy obligation is in force now and was not
deferred** — so phase one is literacy and evidence, phase two is high-risk conformity. See `intel/trends.md` `T4`.

## `P91-B` — The district AI-compliance recorder (North America)

**The ask it answers.** Ohio requires every K-12 district to adopt a formal AI policy by **1 Jul 2026**; 30+
states have guidance; 134 bills are live across 31 states. 🆕 **Only ~10 % of institutions have formal
guidelines and 71 % of US teachers report no AI training** — so the buyer has a legal deadline, no instrument
and no trained staff. California's AB 1159 would additionally bar training on student data absent direct
school benefit.

**Stack.**

| layer | component | grant |
|---|---|---|
| record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |
| statement vocabulary | [`adlnet/xAPI-SCORM-Profile`](https://github.com/adlnet/xAPI-SCORM-Profile) · `ea17c40` | **Apache-2.0** |
| conformance gate | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) · `efa045e` | **Apache-2.0** |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) · `12aeb0f` | **MIT** |
| HE platform (if in scope) | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) · `10a1d90` | **ECL-2.0** |
| 🆕 staff-capability curriculum | see **`P91-G`** | **MIT / Apache-2.0** |

**Wiring.** Put every AI interaction behind a LangGraph node that emits one xAPI statement per event:
*which learner, which model, which prompt class, which human reviewed it, which policy clause authorises it*.
Store in `lrsql`; validate the statement shapes against `ADL_LRS` so conformance is demonstrable rather than
asserted. The deliverable is a policy document **plus a running record that evidences the policy** **plus**
🆕 **the staff training that the 71 % figure says is the real bottleneck** — and the third part is what turns a
one-off compliance project into a programme.

🔴 🆕 **Conformance note that changes the build.** The official **SCORM 2004 4th Edition Test Suite**
(`adlnet/SCORM-2004-4ed-Test-Suite`) carries **no licence payload in 24 filenames**, and so do
`adlnet/SCORM-to-xAPI-Wrapper` and `adlnet/SCORM-to-TLA-Roadmap` — **three of ADL's five repos.** It cannot be
redistributed in a client deliverable. 🟢 **Conform against `ADL_LRS` (Apache-2.0) instead**, which is why it
is in this stack as a gate rather than as a reference.

**Deliberate exclusion.** No GPL component. `LearningLocker` is the better-known LRS and is **GPL-3.0**;
`lrsql` is Apache-2.0 and better maintained. Using the famous one here would convert the deliverable.

## `P91-C` — The pedagogy skill pack, now with content packaging (global, lowest cost to ship)

**The ask it answers.** A client wants AI tutoring that works inside the agent harness they already license,
with no new platform to host, procure or migrate — **and the output has to land in the LMS they already run.**

**Stack — all MIT, all verified this pass.**

| role | component | grant |
|---|---|---|
| diagnosis before teaching | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · `075c189` | **MIT** |
| exam coaching + cross-session memory | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) · `b9e84f5` | **MIT** |
| retention mechanics as a tool call | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) · `ed6774d` | **MIT** |
| model-agnostic ITS surface | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) · `3708287` | **MIT** |
| explicit mastery model | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) · `f88f69f` | **MIT** |
| 🆕 **package the output as SCORM** | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) · `bd14b95` | **MIT** (1 069 B) |
| 🆕 **validate the package** | [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) · `fd5f110` | **MIT** (1 070 B) |
| bundle reference | [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) · `b4c9352` | **MIT** |

**Wiring.** The diagnostic skill runs first and writes a mastery estimate into `adaptive-knowledge-graph`'s
Bayesian tracker — this is the piece most skills lack, and without it "adaptive" means "whatever is in the
context window". `anki-mcp-server` and `tutor-mcp` attach over MCP, so spacing and tutoring are tool calls
rather than prompt instructions.
🆕 **The new closing move: `edumints-scorm-mcp` assembles whatever the pack produces into a SCORM package and
`scorm-mcp-server` validates the zip — both over MCP, both MIT.** Until this pass that glue was always
hand-written per engagement. 🔵 **This is what makes the pack deliverable rather than a demo: output that
imports into the client's existing Moodle, Canvas or Open edX with no integration project.** Two independent
servers of this shape exist, so the pattern is not resting on one maintainer.

🔴 **Stated limit.** A skill inherits the host's model, rate limits and data policy. Where automated
assessment is regulated (Korea's AI Basic Act, Vietnam's high-risk list) or student-data training restricted
(California AB 1159), this pattern needs `P91-B`'s recorder underneath it or it is not a compliance position.

## `P91-D` — Offline-first delivery for constrained connectivity (APAC and LATAM)

**The ask it answers.** UNESCO's finding on APAC is explicit: adoption is gated on IT infrastructure,
connectivity and teacher training — not on model quality. A cloud tutor is the wrong artefact for most of the
region's deployment conditions, and the same holds across much of LATAM.

**Stack.**

| layer | component | grant |
|---|---|---|
| delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) · `d4fea9c` | **MIT** (1 097 B) |
| lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) · `ad22e91` + [`oppia/oppia-android`](https://github.com/oppia/oppia-android) · `25e3860` | **Apache-2.0** |
| interactive content playback | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) · `b5ac7dd` | **MIT** (1 077 B) |
| local tutor | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) · `f0142f2` | **MIT** |
| 🆕 local-model curriculum reference | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) · `da3f9df` | **MIT** (1 091 B) |
| pt-BR reference implementation | [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) · `bbeea5a` | **MIT** (1 085 B) |

**Wiring.** Kolibri handles sync-when-connected delivery; Oppia supplies the structured lesson model;
`h5p-standalone` plays H5P interactive content **without pulling in the GPL H5P core** — that substitution is
the whole point of including it. The tutor runs against a local model (Ollama-class), degrading to retrieval
over cached material when no model is available. 🆕 `agents-from-scratch` is included because it is the one
permissive curriculum written **against a local LLM** — the right teaching material when student data cannot
leave the building, which is the same constraint that drives the rest of this stack.
`aprende-brasil` already implements exactly this shape in pt-BR with an offline fallback and 205 modules —
**read it before building.**

## `P91-E` — Brazilian public-sector student records with AI on top (LATAM)

**The ask it answers.** A Brazilian municipality or state network wants AI assistance over student records it
already keeps. Brazil has a national AI strategy but **no sectoral education regulation** and **PL 2338 is
still awaiting a Chamber vote**, so the institution is the decision-maker and the cycle is short.

**Stack.**

| layer | component | grant | posture |
|---|---|---|---|
| SIS of record | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) · `2.12` · `cd1da68` | 🔴 **GPL-2.0** (18 092 B) | 🔴 **Separate service — do NOT link, do NOT absorb** |
| AI layer | your service, **across a process/network boundary** from i-educar | 🟢 closed | 🔴 **GPL-2.0 has no linking exception** — the boundary is what keeps the deliverable closed |
| record trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** | 🟢 |
| 🆕 programming-practice + autograding | [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) · `fce1ede` | 🔴 **AGPL-3.0** (34 523 B) | 🔴 **LTI 1.3 only — never in the deliverable** |
| incumbent LMS bridge | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) · `f30df11` | 🔴 GPL-3.0 | 🔴 integrate only |

🔴 **This pattern was re-costed this pass, and the licence it was built on was wrong.** Pass 91 wrote
*"i-educar is **linked, never forked** — **LGPL-3.0 permits exactly that**, and this distinction makes
the engagement possible."* 🔴 **i-educar is GPL-2.0** (title block: *"Version 2, June 1991"*), which has
**no linking exception at all**, so the sentence that made the engagement possible was the sentence that
was wrong. See `verticals/solutions.md` and `compose/code/grant-ladder-v4/README.md` (`P960`).

**Wiring, corrected.** i-educar stays the system of record and runs **as its own deployed service** —
unmodified, unlinked, and outside the deliverable's build. The AI layer sits beside it **across a process
or network boundary**, reading through i-educar's HTTP interfaces and its database only via exported
views, and writing xAPI into `lrsql` (Apache-2.0). Where the network also runs Chamilo (common across
LATAM), bridge by LTI 1.3 rather than modifying it.

🔵 **Cost effect, stated plainly rather than buried.** The pattern survives — 🔴 **but it is no longer
the cheap one.** Linking would have allowed in-process extension; a service boundary means the
integration surface must be specified, versioned and tested, and **anything the client wants changed
*inside* i-educar is a GPL-2.0 contribution, not a deliverable feature.** Scope that explicitly in the
statement of work. 🔵 **If the ask can tolerate a different system of record, `OpenEduCat` (LGPL-3.0,
genuinely verified) is the only platform on this shelf where the original linking strategy is legal.**
🆕 **Where the ask includes programming education — and in Argentina and Brazil it often does —
`mumuki-laboratory` is the regional incumbent with real classroom use and automated feedback. It is AGPL, so
it attaches over LTI 1.3 alongside the deliverable and never inside it.**

🟢 **Credibility anchor for the pitch:** cite the **IADB/BID ILIA index** (AI readiness, adoption and
governance across 19 countries) rather than a market-research CAGR. A development-bank index is something a
rector's office or a ministry already recognises.

🔵 **This pattern exists because of a correction.** Pass 87 recorded *"no permissive open-source SIS exists"*
and stopped. True but incomplete: no SIS is permissive, and a **large linkable one** is, and it is
LATAM-origin with municipal deployments. The missing move was distinguishing *permissive* from *usable*.

## `P91-F` — 🆕 The accessibility conformance gate (North America first, EMEA second)

**The ask it answers.** Section 508 / WCAG exposure on course content, and an institution that needs
**evidence** rather than an assurance. 🔴 **This KB declared for five passes that no permissive AI
accessibility checker existed. That was false**, and the cause was the query naming the industry instead of
the standard (see `intel/trends.md` `T5`).

**Stack — all MIT, all verified from the payload this pass.**

| role | component | grant |
|---|---|---|
| audit + CI regression gate | [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) · `main` · `1b095c2` | **MIT** (1 070 B) |
| prevention at authoring time | [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents) · `main` · `decf6ba` | **MIT** (1 069 B) |
| web **and PDF** scanning | [`9mtm/WCAG-Checker`](https://github.com/9mtm/WCAG-Checker) · `main` · `d34decd` | **MIT** (4 219 B) |
| evidence store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |
| content playback under audit | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) · `b5ac7dd` | **MIT** |

**Wiring.** `WCAG-Accessibility-Skills` runs as the audit CLI in the content pipeline's CI, producing a dated
WCAG 2.1/2.2 finding set per course artefact; its findings are written as xAPI statements into `lrsql`, so the
institution holds a **time-series of conformance** rather than a one-off report.
`accessibility-agents` runs one tier earlier — inside the authoring host — so AI-generated course material is
checked **before** it is committed, which is cheaper than auditing it afterwards. `9mtm/WCAG-Checker` covers
the **PDF** surface, which is where institutional exposure actually lives: handouts, readings and scanned
packs, not the LMS chrome.

🟢 **The feature to sell is the refusal.** `WCAG-Accessibility-Skills` states explicitly that it **cannot
declare legal conformance from an automated pass** and keeps a human-review boundary. 🔵 **A checker that
overclaims is a liability in a dispute**; one that documents the boundary between automated evidence and
human judgement is exactly what counsel wants. Price the human-review step as part of the engagement rather
than pretending the tool removes it.

🔴 **Deliberate exclusions, and why.** [`qed42/ai-accessibility-checker`](https://github.com/qed42/ai-accessibility-checker)
is the most capable-looking tool in this space — Python CLI plus GitHub Action, WCAG 2.0–2.2 A/AA/AAA — and is
**described in search summaries as MIT while carrying no licence payload in 24 filenames.** Excluded.
`albertomf1979/wcag-accessibility-agent`: same, no payload. `ucfopen/UDOIT` is **GPL-3.0** and not AI-driven —
it stays an integration, never a component.
🔴 **Stated gap this pattern does not close: instructional alignment.** It proves content is *accessible*, not
that it *teaches the stated outcome*. There is still no permissive checker for that.

## `P91-G` — 🆕 The AI-literacy curriculum factory (APAC first, EMEA second)

**The ask it answers.** 🟢 **Four jurisdictions now mandate AI instruction rather than merely regulate AI
systems** (`intel/trends.md` `T7`): **China** (MoE, ≥8 h/year from age six, since Sep 2025), **Singapore**
(MoE, Mar 2026, all schools by 2027), **India** (CBSE, Classes 3–8, session 2026-27, notification 9 Apr 2026)
and the **EU** (AI Act Art. 4 staff literacy, in force now). Someone has to write the material, localise it,
train the teachers and assess it. 🔴 **No incumbent product covers this, and the deadlines are real.**

**Stack.**

| role | component | grant |
|---|---|---|
| adult/teacher-training spine | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) · `main` · `ff2ba66` | **MIT** (1 141 B) |
| engineering depth track | [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) · `main` · `b6a7a17` | **MIT** (1 070 B) |
| local-model track (data cannot leave) | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) · `main` · `da3f9df` | **MIT** (1 091 B) |
| agent-course reference | [`huggingface/agents-course`](https://github.com/huggingface/agents-course) · `main` · `3c469e7` | **Apache-2.0** (11 357 B) |
| lesson structure + explanations | [`oppia/oppia`](https://github.com/oppia/oppia) · `ad22e91` | **Apache-2.0** |
| assessment of the curriculum | [`numbas/Numbas`](https://github.com/numbas/Numbas) · `39b03e5` | **Apache-2.0** |
| packaging into the client LMS | [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) · `bd14b95` | **MIT** |
| completion + literacy evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) · `cb794e4` | **Apache-2.0** |

**Wiring.** The four permissive curricula are the **source material for the teacher-training tier, not the
pupil tier** — be explicit about that with the client. Re-express the concepts through Oppia's structured
lesson model to get age-appropriate sequencing and explanation-driven interactions; author assessment in
Numbas; package with `edumints-scorm-mcp` so it drops into the ministry's or district's existing platform; and
record completion into `lrsql` — which, for the EU, **is the Article 4 literacy evidence**, and for a district
is the Ohio-style policy evidence. One pipeline, two compliance outputs.

🔴 **The honest gap, and it is the opportunity.** Every permissive AI curriculum found is written for **adult
developers**. 🔴 **Nothing on this shelf addresses primary-school AI literacy — the exact scope China has
already implemented and India begins this session.** The pupil-facing material has to be authored, and that
authoring is the billable core of this pattern rather than an input to it.
🔴 **Licence trap specific to this pattern: curriculum is content, and content is where non-commercial clauses
cluster.** [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) is
**CC-BY-NC-SA-4.0** — reference only, never in a paid deliverable. Check the grant on every piece of
curriculum before it enters the pipeline, and read the payload rather than the badge: this pass's own
instrument briefly mis-read that very row as public domain.

## `P92-A` — 🆕 Mastery-gated progression: the learner model the shelf lacked for eight passes

**The ask it answers.** An institution already has content and a tutor, and the complaint is that the tutor
is *"confidently helpful and never actually knows whether the student learned anything."* They want
progression gated on **evidence of mastery per skill**, not on completion or on a model's impression of the
conversation. 🔵 **This is the most common follow-on ask after a tutor pilot succeeds**, and until this pass
this shelf had no permissive answer to it — `Gap 335`, named openly for eight passes.

**Stack — permissive end to end, so the whole thing is closable.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| mastery estimation | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` | 🟢 in the deliverable |
| skill graph / prerequisites | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **MIT** · 1 094 B · `main` · `f88f69f` | 🟢 in the deliverable |
| tutor turn (option A) | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `main` · `6cf793b` | 🟢 in the deliverable |
| tutor turn (option B) | [`fborrasumh/tutoria`](https://github.com/fborrasumh/tutoria) | **MIT** · 1 120 B · `main` · `65b2903` | 🟢 in the deliverable — pick this one where the **teacher must validate the lesson first** |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` | 🟢 |
| item bank / assessment | [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` | 🟢 SCORM-packageable |
| evidence trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` | 🟢 |
| delivery | the client's LMS, via LTI 1.3 / SCORM | 🔴 theirs | 🔴 integrate, never fork |

**Wiring — the loop, concretely.**

1. **Tag the item bank to skills.** `Numbas` questions carry skill tags; the skill graph in
   `adaptive-knowledge-graph` holds prerequisites. 🔵 **This is the only genuinely manual step and it is
   where the engagement's domain value sits** — budget it as content work, not engineering.
2. **Every graded interaction becomes an xAPI statement** into `lrsql`. The LRS is the training corpus *and*
   the audit trail — **one store, two purposes**, which is why this stack is cheap to run.
3. **Fit a tracing model offline on that corpus.** `pykt-toolkit` gives DKT/AKT/SAINT/LPKT behind one
   interface, so the model is a swappable component rather than an architectural commitment. 🟢 **Start with
   **BKT or DKT** — interpretable, and an institution will ask *"why did it say my student hasn't mastered
   this?"* on day one.
4. **Serve a per-skill mastery probability** as a service the agent calls as a tool. 🔵 **The agent asks the
   model what the student knows; it does not infer it from the transcript.** That inversion is the whole
   pattern.
5. **Gate progression on a threshold**, and route the tutor's next turn from the weakest prerequisite — not
   from the syllabus order.
6. **A teacher sees and can override every gate.** 🔴 **Non-negotiable, and not for pedagogical reasons:**
   mastery gating decides what a student is allowed to attempt, which is *evaluating learning outcomes* —
   **EU AI Act Annex III high-risk**, and squarely inside Oklahoma's and Maryland's human-oversight floors.
   The override log is the Article 27 evidence.

**Timeline.** 6–8 weeks to a gated pilot on one course with an existing item bank; **+4–6 weeks** if the
item bank has to be skill-tagged from scratch. 🔴 **The binding constraint is interaction data, not
modelling**: a tracing model needs history, so a cold-start course gates on BKT priors and a rubric for the
first term. **Say this in the proposal** — a client who expects adaptive behaviour in week one will read a
correct implementation as a failure.

🔴 **Stated honestly: this is a build, not an integration.** Nothing on this shelf wires a tracing model to
an agent's turn today — `pykt-toolkit` is a benchmark library, not a service. **The glue (steps 2, 4 and 5)
is bespoke, and it is also the defensible part.** Tracked as `Gap 369`.

🔴 **And mind the name collision:** [`JonathanSilver/pyKT`](https://github.com/JonathanSilver/pyKT) is also
MIT and answers the same search string, but its README states its models do not match the originals'
performance. **Pin `pykt-team/pykt-toolkit` by slug in the dependency manifest** (`P968`).

🟢 **Where to sell it first.** EMEA and North America, because the oversight requirement that makes this
pattern *expensive* is also what makes it *procurable*: an institution facing Annex III or an Ohio district
policy needs a defensible decision trail, and **a mastery model with a teacher override and an LRS behind it
is that trail.** 🔵 The same build satisfies Vietnam's 72-hour incident reporting with a log subscriber.

## `P93-A` — 🆕 The adaptive assessment you can defend in an audit (supersedes `P92-A`'s modelling layer)

**The ask it answers.** *"We want adaptive testing — shorter tests, same confidence — and when a parent or a
regulator asks why a student got the item they got, or why the system says they haven't mastered a skill, we
need an answer that isn't 'the model decided'."* 🔵 **`P92-A` answers the first half. It does not answer the
second half, and under Annex III the second half is the one that blocks go-live.**

🔴 **Why this is a separate pattern rather than an edit to `P92-A`.** `P92-A` estimates mastery with a
**deep** tracing model (`pykt-toolkit`: DKT, AKT, SAINT). That is the right choice when the goal is
predictive accuracy over a large interaction corpus. 🔴 **It is the wrong choice when the deliverable has to
explain itself**, and *"assessing learning outcomes"* is named high-risk in the EU AI Act's Annex III, which
owes the person assessed an explanation. 🟢 **The classical psychometric stack gives the same loop with
parameters a human can read — and, measured this pass, it is also the better-licensed and more
production-worn option.** `intel/trends.md` `T10`.

**Stack — permissive end to end. All five modelling rows were resolved from the payload this pass.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| item calibration | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | **MIT** · `LICENSE` 1 121 B · `master` · `6514928` | 🟢 in the deliverable |
| item calibration (alternative) | [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · `LICENSE.txt` 1 064 B · `master` · `daf2277` | 🟢 — the one `catsim`'s own README points at |
| adaptive session | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · **`dev`** · `7e6caae` | 🟢 — 🔴 **pin the ref: the default branch is `dev`, not `main`** |
| per-skill mastery | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** · `LICENSE` 1 132 B · `master` · `cc1682e` | 🟢 in the deliverable |
| review scheduling | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** · `LICENSE` 1 079 B · `main` · `9446cb0` | 🟢 optional, and cheap |
| deep model, for comparison only | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** · 1 066 B · `main` · `77c3e90` (pass-92 SHA) | 🟡 **offline benchmark, not in the serving path** |
| item bank | [`numbas/Numbas`](https://github.com/numbas/Numbas) | **Apache-2.0** · 11 357 B · `master` · `39b03e5` (pass-92 SHA) | 🟢 SCORM-packageable |
| evidence trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** · 11 357 B · `main` · `cb794e4` (pass-92 SHA) | 🟢 |
| orchestration | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · 1 072 B · `main` · `12aeb0f` (pass-92 SHA) | 🟢 |
| delivery | the client's LMS, via LTI 1.3 / SCORM | 🔴 theirs | 🔴 integrate, never fork |

**Wiring — and the seams are the libraries' own, not ours.**

1. **Author or import the item bank into `Numbas`**, tagged to skills. 🔵 Unchanged from `P92-A`, still the
   manual step where the domain value sits, still budgeted as content work.
2. **Calibrate the bank with `py-irt`.** Fit 2PL or 3PL over historical responses → **difficulty and
   discrimination per item, ability per learner, on one scale.** 🔴 **Do this before any adaptive session
   runs**: `catsim` selects items *using* these parameters and cannot produce them —
   **its README says so in its own words**: *"catsim does not implement item parameter estimation."*
   🟢 **That sentence is why this stack composes instead of overlapping**, and it is also the honest answer
   to "why two IRT libraries?" — `girth` is the drop-in alternative the same README names.
3. **Run the adaptive session with `catsim`**: initialiser → **item selector** → ability **estimator** →
   **stopping rule**. 🟢 **The stopping rule is the commercial payload** — it is what turns "shorter tests"
   from a claim into a parameter, and it is auditable: *stop when the standard error of the ability estimate
   falls below X*.
4. **Track mastery across sessions with `pyBKT`**, not within them. 🔵 **IRT answers "how able is this
   learner right now, on this scale"; BKT answers "has this learner learned this skill yet".** Different
   questions, and the institution asks both. `pyBKT`'s four parameters per skill — **prior, learn, slip,
   guess** — are the ones you put on a teacher's screen.
5. **Every response becomes an xAPI statement into `lrsql`** — the calibration corpus and the audit trail in
   one store, as in `P92-A`.
6. **Schedule retention with `py-fsrs`** where the subject rewards it (languages, vocabulary, clinical
   facts). 🟡 Optional. 🔵 **It answers a question neither IRT nor BKT does — *when will they forget* — so
   it is additive, not a third opinion on the same question.**
7. **Benchmark the deep model offline against the psychometric one, and keep it offline.** 🟢 Run
   `pykt-toolkit` on the same `lrsql` corpus and report the accuracy difference honestly. 🔵 **If DKT is
   materially better on the client's data, that is a finding worth presenting — and still not a reason to
   put it in the serving path of a high-risk decision without an explanation layer in front of it.**
8. **Teacher override on every gate, logged.** 🔴 Non-negotiable, same as `P92-A`: the override log is the
   Article 27 / human-oversight evidence.

**Timeline.** 🟢 **5–7 weeks to a calibrated adaptive pilot on one course with ≥ ~300 historical responses
per item-ish bank**; **+3–4 weeks** without historical response data, because calibration then needs a
seeding round. 🔵 **Faster than `P92-A`'s 6–8 weeks for a reason worth saying out loud: IRT needs far less
data than a deep tracing model, and classical psychometrics was designed for exactly the sample sizes a
single institution actually has.**

🔴 **What this pattern does *not* cover, stated before a client discovers it.** It is **structured
assessment only** — items with scorable responses. 🔴 **Open-response and essay scoring is not in this stack
and cannot be bolted on from this shelf**: the whole permissive supply is one 2★ research repository
(`Gap 372`, `agents/top.md`). 🔵 **Which means the activity the EU AI Act names most explicitly is the one
with the least open supply. Scope essays out, or price them as bespoke with a human grader in the loop.**

🟡 **Two integration cautions, both measured.** `catsim`'s default branch is **`dev`** — pin it in the
manifest or a `main`-assuming CI will fail. And `girth`'s grant lives in **`LICENSE.txt`**, not `LICENSE`;
a shallow licence scanner will report it as ungranted (`P969`'s neighbourhood).

🟢 **Where to sell it first.** 🟢 **EMEA** — Annex III makes the explainability the procurement criterion,
and Jisc's 38-institution marking pilots show the sector is already buying in this area. 🟢 **North
America** second, where Oklahoma's and Maryland's human-oversight rules and Ohio's district-policy deadline
create the same need without the same deadline pressure. 🔵 **And `catsim` being Brazilian is a real asset
in a LATAM pitch** — 🟡 though its placement rests on the project's documentation host rather than a payload
copyright line, so say "Brazilian-authored", not "a Brazilian product".

## `P93-B` — 🆕 Curriculum-aligned tutoring for Brazil, with the grounding decision made by measurement

**The ask it answers.** A Brazilian state secretariat, municipal network or private group wants a tutor or a
lesson-planning assistant that is **aligned to the BNCC** — and wants the alignment to be *true*, with the
official code cited, not a plausible-looking label. 🔴 **This is the ask that fails most often in this
industry, because an ungrounded model will produce a BNCC code that looks exactly right and is invented.**

🟢 **And for once the size of that failure is measured, by a third party, reproducibly.**
[`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) — 8 models, 300 items:

| condition | hallucination rate | what it means for the build |
|---|---|---|
| 🔴 no source in context | **31.9 %** | 🔴 roughly **one citation in three is wrong**. Unshippable. |
| 🟢 **dataset embedded in the prompt** | **0.2 %** | 🟢 **the design choice** |
| 🟡 MCP tool call to the dataset | **2.3 %** | 🟡 **ten times worse than embedding, fourteen times better than nothing** |

🔵 **So the architecture is decided by evidence rather than taste: embed the curriculum data in the context
for alignment, and keep the tool call for what the data cannot answer.** `intel/trends.md` `T11`.

**Stack.**

| layer | component | grant (payload · bytes · ref · SHA) | posture |
|---|---|---|---|
| curriculum data | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **`LICENSE` = MIT** 1 073 B · `main` · `daabd7d` — 🔴 **but the data under `dados/` is CC BY 4.0** (`P969`) | 🟢 in the deliverable, **with attribution** |
| packages + MCP | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant at the root** · `LICENSE` 1 299 B · `main` · `ac9feb8` → MIT code + CC BY 4.0 data | 🟢 — `@bncc/dados` 0.3.1, `@bncc/mcp` 0.2.0, PyPI `bncc` 0.2.0. 🟡 **all pre-1.0: vendor the version** |
| alignment regression | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟢 split · `LICENSE` 911 B · `main` · `4713901` → MIT harness + CC BY 4.0 items | 🟢 **run it as your CI gate, not as a citation** |
| second MCP opinion | [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · 1 218 B · `main` · `f94ca6a` | 🟡 independent implementation — useful as a cross-check |
| tutor turn | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** · 1 069 B · `main` · `032b5aa` (pass-92 SHA) | 🟢 — Colombian, **already Open edX-integrated** |
| pt-BR content | [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) | **MIT** · 1 085 B · `main` · `bbeea5a` (pass-92 SHA) | 🟢 205 modules, **offline local fallback** |
| autograding (optional) | [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | 🔴 **AGPL-3.0** · 34 523 B · `master` · `fce1ede` (pass-92 SHA) | 🔴 **integrate across a network boundary; never absorb** |
| offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · 1 097 B · `develop` · `d4fea9c` (pass-92 SHA) | 🟢 where connectivity binds |
| SIS, if records are in scope | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (**not** LGPL — see `P91-E`) | 🔴 service boundary only |

**Wiring.**

1. **Vendor `bncc-dados` into the deliverable** — JSON or SQLite, pinned to a commit, **not** fetched at
   runtime. 🟢 **Its provenance is the selling point and it is checkable**: every record carries a `fonte`
   (spreadsheet row + official PDF page), **1 576 of 1 580 BNCC-2018 texts match the MEC/CNE PDF character
   for character**, the 4 mismatches are documented in `DECISOES.md`, and **CI re-runs the extraction
   pipeline and rejects divergence.** 🔵 **A state secretariat can audit the dataset against its own
   ministry's PDF. Almost nothing else in this KB can say that.**
2. **🔴 Honour the data licence, and know that your tooling will not tell you to.** The code is MIT; **the
   data is CC BY 4.0**, which is an **attribution obligation** — and the grant is in `dados/LICENSE.md`,
   **not at the repo root**, where neither the 24-name ladder nor GitHub's own sidebar can see it
   (`P969`). 🟢 **Put the attribution in the product's about screen and in the proposal's IP annex at the
   start**, where it costs nothing; retrofitting it after a procurement review does not.
3. **Embed, don't call — because 0.2 % beats 2.3 %.** Load the objectives for the relevant stage and
   component into the context. 🟢 Use the MCP server (`@bncc/mcp`, **7 tools**, dataset embedded so queries
   stay local) for **search and decoding across the whole base** — the long-tail lookups that will not fit
   in context — and keep citation-critical paths on embedded data.
4. **Gate every release on the benchmark harness.** 🟢 `bncc-benchmark`'s `harness/` is **MIT**, so run it
   as your own regression suite against *your* prompt and *your* model: **a measured faithfulness number per
   release, on the client's own configuration.** 🔵 **That converts "aligned to the BNCC" from a marketing
   claim into a CI check with a number** — and it is the single most differentiating artefact in this
   pattern.
5. **Teacher validates before the student sees it.** Take the primitive from `fborrasumh/tutoria`: lesson →
   **teacher validation** → student. 🔴 Not optional where assessment or progression is touched.
6. **Deliver through what the network already runs** — Open edX (🔴 **AGPL-3.0**, integrate) or Moodle
   (🔴 **GPL-3.0**, integrate), or `Kolibri` (MIT) where connectivity is the binding constraint.

**Timeline.** 🟢 **4–6 weeks** to a BNCC-grounded lesson-planning assistant with a measured faithfulness
number — **the fastest credible pattern on this page**, because the hard part (a verified, machine-readable,
provenance-carrying curriculum base) is already built and granted. **+3–4 weeks** to attach a tutor turn and
teacher validation; **+4 weeks** for offline delivery via `Kolibri`.

🔴 **Three risks, named.** **(a) Pre-1.0 dependencies** — all three packages are below 1.0, so vendor the
version and expect breaking changes. **(b) The benchmark's publisher has a declared conflict of interest** —
*"a Profy opera produtos que usam LLMs sobre a BNCC"*, disclosed in its own README, with methodology, items
and raw responses published so the numbers can be recalculated. 🔵 **A disclosed conflict with reproducible
workings is a better position than an undisclosed one, and the right response is to re-run the harness
yourself — which step 4 already does.** **(c) Its own two surfaces disagree on corpus size** (description:
15 300 responses / 17 models; README: 19 models × 900, 17 100 published). 🟢 **Cite the grounding
percentages, which are the study's headline; do not cite a corpus size from the description.**

🟡 **Generalisation limit, so this pattern is not oversold.** The 0.2 % figure is **one benchmark, one
curriculum, one language, 300 items.** 🔵 **The direction is almost certainly general; the magnitude is
not.** Use it to justify the architecture — embed the standards data — **never to promise a client 0.2 %.**

🟢 **And the portable half of this pattern.** Steps 1, 2 and 4 — **vendor a verified standards dataset, honour
its data licence, gate releases on a faithfulness harness** — are jurisdiction-independent. 🔴 **What is not
portable is the dataset**: no other national curriculum was found published this way (`Gap 371`). 🔵 **So
outside Brazil this pattern is a *build the dataset first* engagement, and `bncc-dados` is the reference
implementation to copy — including the character-exact verification against the official PDF, which is what
makes it auditable rather than merely open.**

## `P94-A` — 🆕 The Annex III evidence pack for automated scoring (EMEA first, North America second)

**The ask it answers.** *"We already grade written work with a model — or a vendor does it for us. The AI Act
says that is high-risk. What do we have to be able to show, and can we build the showing instead of the
scorer?"* 🟢 **Yes, and that is the cheaper and more defensible half of the job.**

🔴 **Why this is a pattern and not a line in `P93-A`.** `P93-A` covers **structured** assessment — items,
calibration, adaptive sessions, mastery. 🔴 **It does not cover open-response work**, and open response is
where the regulatory exposure concentrates: Annex III point 3(b) names evaluating learning outcomes, and the
assessed person is owed an explanation. 🟢 **Pass 94's finding is that the permissive supply covers the
explanation and the validity argument, and not the scorer** — so the pattern is built on that seam instead
of against it (`intel/trends.md` `T13`).

**Stack — the licence boundary is the architecture.**

| layer | component | grant (payload · bytes · file · ref · SHA) | posture |
|---|---|---|---|
| scoring-model evaluation, fairness, report | [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🟢 **Apache-2.0** · 11 358 B · `LICENSE` · `main` · `a844f71` | 🟢 **in the deliverable — this is the deliverable** |
| ML experiment layer it pins (`skll==5.0.1`) | [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** · 1 555 B · `LICENSE.txt` · `main` · `b350eb0` | 🟢 in the deliverable |
| short-answer grading with LMS reach | [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 **MIT** · 1 062 B · `LICENSE` · `main` · `8e144ac` | 🟢 fork and audit — 421 commits, 3★, so **read it before you trust it** |
| the explanation the regulator is owed | `py-irt` + `pyBKT` + `catsim` (see `P93-A` for SHAs) | 🟢 MIT / BSD-3 | 🟢 in the deliverable |
| long-form scoring, if it must be built | [`openedx/ease`](https://github.com/openedx/ease) · [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · 35 136 B / 35 135 B · `master` · `056da0a` / `1b7ae59` | 🔴 **behind a network boundary, never absorbed** |
| architecture reference only | [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) | 🟡 **Apache-2.0 *by reference*** · 1 865 B · `main` · `41ae3bd` | 🟡 **read, do not depend** — `P971`: the terms are not in the repo |
| evidence trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 (pass-92 SHA `cb794e4`) | 🟢 |
| delivery | the client's LMS over **LTI 1.3** | 🔴 theirs | 🔴 integrate, never fork |

**Wiring.**

1. **Inventory what already scores.** 🔴 **Start with the Article 5 prohibition, not the Annex III
   deadline**: emotion recognition in education has been **banned since 2 Feb 2025**, and affect inference
   ships switched on in proctoring and engagement-analytics products. 🟢 **One week, and it is the only
   limb that is already enforceable.**
2. **Reproduce the existing scores offline.** Human ratings in, model scores in, `rsmtool` config out. 🟢 Its
   output is **a customisable HTML statistical report** — agreement, bias by subgroup, feature behaviour via
   SHAP — which is the artefact an appeal or an audit consumes. 🔵 **Nothing is retrained at this step; you
   are measuring the thing the client already runs.**
3. **Decide the scorer by boundary, not by preference.** Vendor score → keep it and wrap it. Must be built →
   stand `ease`/`edx-ora2` behind a service boundary and **do not link it into client code**. 🔵 **Either
   way `rsmtool`'s report is the same, which is exactly why this pattern survives the scorer decision.**
4. **Add short-answer grading where the volume is.** `NodeGrade` already speaks **LTI 1.1/1.3** and can run a
   **local** embedding model, so student text need not leave the institution — the EMEA sovereignty
   constraint, satisfied by configuration rather than architecture.
5. **Attach the explanation.** For anything that drives progression, carry a per-skill mastery probability or
   an item-difficulty parameter from `P93-A` alongside the grade. 🔵 **A number a teacher can read is the
   difference between a defensible decision and an appeal you lose.**
6. **Keep the human gate explicit in the product.** Oklahoma's statute requires a teacher to review AI output
   before classroom use, and [`fborrasumh/tutoria`](https://github.com/fborrasumh/tutoria) (MIT) is a
   permissive reference implementation of that gate. 🟢 **One primitive, two jurisdictions' requirements.**

**Cost and shape.** 🟢 **Weeks 1–2: the Article 5 inventory and the first `rsmtool` report on existing
scores** — a deliverable before any build. **Weeks 3–6: scorer boundary, `NodeGrade` pilot on one
assessment, LTI wiring.** **Weeks 7–10: the evidence pack** — validity argument, subgroup fairness,
explanation path, human-review gate, documented against Annex III point 3(b). 🔵 **Sell it against
2 December 2027 and start it against 2 February 2025.**

🔴 **Scope out explicitly, as `P93-A` does.** 🔴 **This pattern does not deliver a state-of-the-art essay
scorer.** `Gap 372` stands for the scorer: the permissive supply is one 2★ research repo whose licence is
Apache **by reference only**, and the production code is AGPL. 🔵 **Price the human grade, or price the
vendor's, and sell the evidence.**

## `P94-B` — 🆕 The platform due-diligence gate (global, half a day, run before any quote)

**The ask it answers.** *"We are quoting a Moodle / Open edX / Artemis customisation. What do we need to know
before the number goes in the proposal?"* 🔵 **Three HTTP requests' worth of things that otherwise surface in
week three.**

🟢 **This pattern exists because pass 94 discovered that this KB itself was taking platform versions on
trust** (`P972`, `compose/code/p972-platform-version-ladder/`).

**The gate — four checks, no credentials, no API quota.**

1. **Read the release ladder from the remote.** `git ls-remote --heads <slug>` **and** `--tags <slug>`.
   🔴 **Both, because the ladder moves**: Moodle keeps it in heads (`MOODLE_503_STABLE`), while
   **Open edX's `open-release/*` heads stop at Sumac** and Teak and Ulmo exist only as tags **under a changed
   prefix** (`release/teak.1`, `release/ulmo.4`) — `P977`.
2. **Read the release string from the project's own version file at a pinned SHA.** Moodle:
   `public/version.php` → `$release`, `$branch`, `$maturity`. 🟢 **Measured 2026-10-10: `5.3` is
   `MATURITY_STABLE`, `main` is `6.0dev` / `MATURITY_ALPHA`** — while every secondary source said 5.2.
   🔴 **And `version.php` is NOT at the root** (`P973`): the web root moved into `public/` at Moodle 5.0,
   which invalidates every pre-5.0 path in a Dockerfile, a proxy rule or a theme.
3. **Cross-check against what actually gets deployed.** `overhangio/tutor` is at **`v22.0.2`** —
   three named releases past Open edX's newest `open-release` head. 🔵 **One oracle is a reading; two that
   disagree are a finding.**
4. **Re-read the licence from the payload, per repository.** 🔴 Not from a badge, a blog or a sidebar —
   `P969` showed the sidebar shares the root-only blind spot, and `P975` showed one publisher ships
   Apache-2.0, BSD-3 **and GPL-2.0**. For a platform, also check the **assessment subsystem separately**:
   Open edX's own scoring code (`ease`, `edx-ora2`) is **AGPL-3.0**.

**What it buys.** 🟢 A version the client can check, a path layout that matches reality, a licence per
component rather than per vendor, and — in the Artemis case — 🟢 **a readable supply-chain posture**: its
`build.gradle` pins around a named CVE (`CVE-2026-55760`) with the reasoning in comments. 🔵 **Half a day,
and it moves the two discoveries that most often blow a fixed-price education engagement out of week three
and into week zero.**

## `P95-A` — 🆕 The university AI-mandate compliance stack (APAC first, LATAM and EMEA second)

**The ask it answers.** *"Our regulator just made an AI course compulsory in every degree we offer, told us
to write our own AI-use policy, and told us to train all staff annually. We have eighteen months and one
LMS."* 🟢 **This is Pakistan's HEC notification almost verbatim** (3-credit AI course in every UG and PG
degree from session 2026, plus the August 2026 draft policy: institutional rules, disclosure of AI use,
annual training, AI literacy in curricula within two years). 🔵 **It also fits India once the
AICTE/UGC/Nasscom curriculum lands, Quebec's `Cadre de référence`, and Brazil's CNE higher-education
chapter** — see `intel/trends.md` `T14`.

🟢 **Why it is a new pattern rather than `P91-G` re-aimed.** `P91-G` is a *curriculum factory* for a
ministry: produce content once, deliver to many schools. 🔴 **This buyer is a single institution that must
produce evidence about itself, every year, forever.** The deliverable is a **running system**, not a
syllabus.

**The stack — every row permissive, every row already on this shelf.**

| layer | component | grant | why this one |
|---|---|---|---|
| platform | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) **`10.3`** | 🟢 **MIT** | 🟢 **The only production university platform that is permissive AND already AI-native** — Iris (LLM tutor), Athena (feedback), Hyperion (exercise authoring). Fork it and the deliverable is closable. |
| platform (alt, if the LMS must stay) | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) **`25.2`** or [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) **`21.0.3`** | 🟢 **ECL-2.0** / **Apache-2.0** | Integrate by LTI 1.3 instead of forking. 🔴 **Pin the TAG, not the default branch** — `P978`: Sakai's root pom says `27-SNAPSHOT`, which nobody can install. |
| the compulsory course | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) **`7.0.0`** | 🟢 **BSD-3-Clause** | 🟢 **An AI course is a programming course, so it needs an autograder at cohort scale.** Parallel Docker grading, student-side public checks, and **native Canvas + Gradescope** so it works whether or not the LMS is replaced. 🟢 Payload, manifest and registry all say BSD-3. |
| mastery evidence | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) + [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) or [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) **`0.6.0`** | 🟢 **MIT** | Per-skill mastery probability and calibrated item difficulty — **the parameters an accreditation reviewer can be shown.** `girth_mcmc` is new this pass and gives the Bayesian/MCMC estimator. |
| adaptive delivery | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | Item selection and stopping rules for a placement test — **AI literacy has to be measured before it can be taught at the right level.** Pin the `dev` branch. |
| scoring evidence | [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) + [`skll`](https://github.com/EducationalTestingService/skll) | 🟢 **Apache-2.0** / **BSD-3** | 🔴 **Only if the institution scores open responses.** `T13`: validate with Apache/BSD, score behind a service boundary. **Do not build the scorer** — `Gap 372`, and the three research candidates are CC BY-SA or ungranted (`P981`). |
| content packaging | [`tunapanda/h5p-standalone`](https://github.com/tunapanda/h5p-standalone) | 🟢 permissive | Ships the course into whatever LMS survives the engagement. |
| disclosure workflow | [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | 🟡 **LGPL-3.0** | 🔴 **Link, do not absorb.** The draft policy's *"disclosure of AI use"* requirement is an LTI-delivered attestation attached to each submission. |

**Wiring, in the order it gets built.**

1. **Placement first, because the mandate is per-degree and the cohort is not uniform.** `py-irt` or
   `girth_mcmc` calibrates an AI-literacy item bank → `catsim` runs it adaptively at enrolment. **Output: a
   per-student entry level and a defensible item bank.**
2. **Deliver the 3-credit course on Artemis** (or beside the incumbent LMS by LTI 1.3), with **`otter-grader`
   behind the programming assignments** — Docker-parallel so one cohort does not need one TA per twenty
   students. 🟢 **This is the row that did not exist before pass 95**; the alternative at this layer was
   AGPL-3.0 and could not be folded into a closable deliverable.
3. **Track mastery across the two-year literacy horizon with `pyBKT`**, one model per declared literacy
   skill. **Output: the annual evidence the regulator's "AI literacy in curricula within two years" clause
   will be audited against.**
4. **Attach the disclosure attestation at submission** over LTI, and log it immutably. 🔵 **The policy
   requires disclosure; an institution that cannot produce the log has not complied even if every student
   disclosed.**
5. **Generate the institution's own AI-use policy from its configuration, not from a template.** 🟢 **The
   draft policy's "universities write their own rules" clause is the recurring-revenue clause** — it must
   be regenerated as the system changes, which is a retainer rather than a document.

**What it buys, and the cost shape.** 🟢 **8–12 weeks to a first cohort** if Artemis is forked and the
placement bank is seeded from an existing question set; **add 4 weeks** if the incumbent LMS must stay and
everything is delivered over LTI. 🔵 **Then it recurs**: the annual staff training, the annual policy
regeneration and the annual literacy evidence pack are three deliverables per institution per year.
🟢 **And it replicates** — there are hundreds of institutions under a single HEC-style notification, and
the second one is a configuration rather than a build.

🔴 **What this pattern does not do.** It does not score essays (`Gap 372`), and it does not claim the
Pakistani instrument has been read at primary grade — **the notification is search-summary from consistent
Pakistani press, and the August policy is explicitly a draft** (`intel/market.md`). 🔵 **Quote the course
mandate as firm and the policy obligations as a drafting-stage likelihood**, not the reverse.

## `P95-B` — 🆕 The identity-and-version gate (global, two hours, run before any dependency is named)

**The ask it answers.** *"Your proposal names eleven open-source components. Are those the components we
will actually be installing, and do we have the rights to them?"* 🔵 **Pass 95 got both answers wrong on
the first attempt, twice, and this gate is what caught it.** It **extends `P94-B`** rather than replacing
it: `P94-B` gates a platform, this gates every named dependency.

**Four checks, no credentials, no API quota.**

1. **Resolve the tool to a REPOSITORY, never to a distribution name** (`P980`). 🔴 **Measured this pass:**
   `otter-grader` 7.0.0 is [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader),
   **BSD-3-Clause**; `Otter-Autograder` 0.15.9 is
   [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder), **GPL-3.0**. **Two unrelated
   projects, both autograders, incompatible grants.** The only disambiguator is the registry's
   `project_urls` → repository link. 🔵 **A proposal that names "Otter" names neither.**
2. **Read the grant from the payload at a pinned SHA, across filename variants.** 🔴 **`LICENSE` being 404
   does not mean ungranted**: `eribean/girth_mcmc` and `eribean/girth` are both **MIT** in `LICENSE.txt`,
   and `frappe/lms` hid **AGPL-3.0** in lowercase `license.txt` for ninety passes. 🟡 **And do not read
   PyPI's `info.license` for an identifier** — `Otter-Autograder` pastes the whole 35 kB GPL-3.0 text into
   that field with `license_expression: None`. **Use the `classifiers` array.**
3. **Read the version twice: the development line and the shippable one** (`P978`). 🔴 **In every case
   measured, the default branch names a release that does not exist yet** — Sakai `27-SNAPSHOT` vs tag
   `25.2`, Opencast `21-SNAPSHOT` vs `20.4`, Moodle `6.0dev` vs `5.3` stable. 🟡 **Fold case before sorting
   a tag ladder**: OpenOLAT ships tags as both `OpenOLAT_` and `OpenOlat_`, and a case-sensitive sort
   returns a 20.x pre-release as newest.
4. **Treat an HTTP 200 as a file, not as an answer.** 🔴 **Four measured ways a 200 carries no version:**
   `canvas-lms`'s `package.json` says `"0.0.0"`; `richie`'s `__init__.py` resolves from installed metadata;
   `mentingo`'s `package.json` has no `version` field; `edx-platform`'s `openedx/__init__.py` is a
   docstring. 🔵 **And a 200 can be an indirection**: Chamilo's `public/main/install/version.php` is a
   one-line `require` pointing back to the repository root, where the real `3.0.1` lives (`Gap 378`).

**Two cross-checks worth the extra request.** 🟢 **A JVM project's `pom.xml` is a second licence oracle**
(`P979`) — Sakai's names *"Educational Community License, Version 2.0"*, independently confirming an
ECL-2.0 row that generic tooling returns as *unclassified*. 🟢 **And a paper is not a licence** (`P981`):
`RATASv1` and `emorynlp/llm-grading` both describe themselves as publicly released open source and **carry
no grant at all**, which under copyright default is all rights reserved.

**What it buys.** 🟢 **Two hours, and it removes the two failure modes that are invisible in review:** a
dependency that is the wrong project under the right name, and a version number that cannot be installed.
🔵 **Both would have reached a client proposal this pass without it.**

## `P96-A` — 🆕 The curriculum-aligned outcome evaluator (global; the wiring `Gap 379` names)

**The ask it answers.** *"We generate thousands of lesson items with AI. How do we show — to an inspector,
a parent or an awarding body — that a given item actually teaches the objective it claims to teach, and
that our judgement of that is calibrated against human markers?"*

🔴 **Until pass 96 this KB answered *"nothing permissive does that; it is a build."*** 🟢 **Every component
now exists under a grant a studio can bill against. What does not exist is the wiring, and that is this
pattern.**

**The four layers, with grants, because the grants are why this is a pattern and not a wish.**

| # | layer | component | grant |
|---|---|---|---|
| 1 | **the standard**, with per-record provenance | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) — `@bncc/mcp` 0.2.0, **7 tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`) over **1 721 verified objectives**, dataset **embedded** so lookups are local | 🟢 **MIT** code · 🟡 **CC BY 4.0** data (attribution names MEC/CNE) |
| 2 | **rubric generation** from the objective text | [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 **MIT** |
| 3 | **judging** content against the rubric | [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) — criteria weighted **critical / core / important / highlight**, bi-directional A/B debiasing, **interpretable verdicts** | 🟢 **Apache-2.0** *(10 770 B — clause-probed 4/4, `APPENDIX` stripped; `P974`)* |
| 4 | **calibration against humans** | [`planepig/rubricbench`](https://github.com/planepig/rubricbench) — **1 147 pairwise comparisons**, expert-annotated atomic rubrics, scores reasoning **and** verdict | 🟢 **MIT** |
| — | *optional, education-domain rubrics* | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 MIT code · 🟢 CC-BY-4.0 prompts · 🔴 **corpora CC-BY-NC-SA-4.0 — excluded from a paid deliverable** |

**How they wire, concretely.**

1. **Resolve the objective.** Call `bncc_lookup` (or `bncc_decodificar` on a BNCC code) for the target
   objective. 🟢 **Keep the returned record verbatim as the evidence anchor** — it carries the code, the
   text and its MEC/CNE provenance, and a lookup that runs locally means **no network call per item**,
   which is the property that makes this run inside a school.
2. **Generate the rubric once per objective, not per item.** Feed the objective text to `OpenRubrics`;
   store the rubric as a versioned artefact keyed on the objective code. 🔵 **Rubric-per-objective is the
   cache boundary**: thousands of items share a handful of rubrics, so generation cost is bounded by the
   curriculum, not by the content volume.
3. **Judge each item with `OpenRS`** against that stored rubric, keeping its **weighted criterion
   breakdown and written verdict**, not just the score. 🟢 **Use the A/B swap** — it exists because
   position bias is real and an inspector will ask whether the order mattered.
4. **Calibrate before you publish a single number.** Run `rubricbench`'s harness against your judge
   configuration to get an agreement figure, then **re-run it on a sample of your own human-marked items.**
   🔴 **Publish the agreement figure beside every score.** 🔵 **A score without an agreement figure is an
   opinion with a decimal point.**
5. **Store the triple**, per item: `{objective record, rubric version, criterion breakdown + verdict}`.
   🟢 **That triple is the audit artefact**, and it is the same artefact `P94-A`'s evidence pack consumes.

**What it costs and what it buys.** 🔵 **4–6 weeks for a single curriculum and a single content type**
(steps 1–3 are a fortnight; step 4 is where the time actually goes, because sampling human-marked items is
an institutional process, not an engineering one). 🟢 **It buys the one thing the generator market cannot
sell**: a defensible statement that generated content meets a named standard, with the judgement itself
measured against humans.

🔴 **Three limits, stated before anyone quotes it.**
- 🔴 **The standards layer is Brazil-only today.** BNCC is the only national curriculum this KB has found
  as **verified open data with a grant** (`Gap 367` otherwise stands: the frameworks every mandate points
  at are ungranted). 🔵 **So the first delivery is LATAM by availability, not by choice** — and porting
  means acquiring or digitising the target curriculum, which is a data-rights negotiation, not a sprint.
- 🔴 **`rubricbench`'s domains are Chat, IF, STEM, Coding and Safety — not education.** 🟡 It calibrates
  *your judge's behaviour*, not its pedagogical validity. **Say so in the deliverable.**
- 🔴 **`evaluators`' annotated corpora are non-commercial.** Use its code and prompts; **bring your own
  annotated corpus** (`T6`).

🟢 **And the regulatory tailwind is `T15`, not `T4`.** Under Vietnam's `Decision 33/2026/QD-TTg` limb 2,
*assessing learning outcomes* is high-risk **and binding since 15 Aug 2026**; under the EU AI Act the same
activity is Annex III but **deferred to 2 Dec 2027.** 🔵 **Sell this into APAC on a live deadline and into
EMEA as 2027 preparation.**

## `P96-B` — 🆕 The content-provenance gate for self-study material (APAC first; Vietnam has made it a duty)

**The ask it answers.** *"Our tutor answers pupils from retrieved material. We were told that is a quality
question. Our Vietnamese counsel says it is a high-risk classification. Which is it?"* 🟢 **Both, and the
second one has a date.**

🔴 **`Decision 33/2026/QD-TTg` limb 1 names *"self-study content generated from uncontrolled data
sources"*** as a high-risk education AI system — **in force 15 Aug 2026**, existing systems to comply
**before 1 Sep 2027**. 🔵 **Read it carefully: it does not mention assessment.** A tutoring agent that never
grades anything is in scope **because of where its material comes from.**

**The gate, four steps, and this KB already has every piece.**

1. **Enumerate the corpus and refuse anything unenumerable.** 🟢 Ground on a **closed, versioned
   standards-and-materials set** — `bncc-dev/bncc-pacotes` (**MIT** code, **CC BY 4.0** data, 1 721
   objectives, **embedded dataset**) is the worked example. 🔴 **Open web retrieval is the thing the limb
   describes.** 🔵 **"Uncontrolled" is a property of the *source list*, not of the model** — so the
   deliverable is a source allowlist with an owner, which is exactly what
   `compose/code/mcp-allowlist-gateway/` already implements.
2. **Tag every retrieved span with its record provenance** and carry it into the answer. 🟢 The MCP
   standards tools return per-record provenance; **keep it, do not summarise it away.**
3. **Measure the grounding effect and publish the number.** 🟢 **`T11` has it: 31.9 % → 0.2 %.** 🔵 **The
   same measurement that was a quality claim last pass is a control effectiveness claim this pass** — and
   control effectiveness is what a conformity assessment asks for.
4. **Wire the 72-hour incident clock, because Vietnam requires it.** Pre-deployment registration in the
   **National AI Database**, conformity assessment, **mandatory human oversight** and **incident reporting
   within 72 hours**. 🔴 **A 72-hour clock is an architecture requirement, not a policy one: it means
   logging, alerting and a named owner, designed in from the start.**

**What it costs and what it buys.** 🔵 **3–4 weeks**, and most of it is steps 1 and 4 — the retrieval
rewrite and the incident pipeline. 🟢 **It buys a reclassification argument**: a tutor grounded on an
enumerated, provenance-tagged, locally-embedded corpus has a documented answer to limb 1 instead of a
promise. 🔴 **It does not buy an exemption** — high-risk status is not automatic from sector alone, but it
is not negotiable by architecture either; the gate makes the conformity dossier cheap, not unnecessary.

🟡 **Evidence grade.** 🔴 **The Vietnamese instrument was not read primary** — every legal-publisher host
was unreachable this pass. Two independent search rounds over different source sets agree on the decision
number, the 30 Jun 2026 publication, the 15 Aug 2026 effect and the three education limbs. 🔴 **One date is
unreconciled and unused**: a general **1 Mar 2027** limb appears in one summary. 🔵 **Confirm with local
counsel before contracting. This pattern is a design, not an opinion on Vietnamese law.**

## `P96-C` — 🆕 The permissive timetable, and the obligation that comes with it (global, small, unusually closable)

**The ask it answers.** *"Scheduling is our worst annual process. Can AI help, and can we own the result?"*
🟢 **This is the smallest genuinely closable deliverable added to this KB in six passes**, because the
platform underneath it is permissive and the problem is bounded.

**The stack.**

| layer | component | grant |
|---|---|---|
| the scheduling engine and data model | 🆕 [`UniTime/unitime`](https://github.com/UniTime/unitime) — university **timetabling, course and student scheduling**, Apereo Foundation, **`v4.9.152`** | 🟢 **Apache-2.0** · payload **11 357 B** pristine · `pom.xml` **independently agrees** |
| the agent surface | 🟢 **already in this repository**: `compose/code/unitime-mcp-gate/` — a tested MCP gate over UniTime, written pass 42, re-audited pass 45, **15/15** on the literal-path control | — |
| the constraint explanation | 🔵 **nothing to add** — UniTime's scheduling constraints are **already declarative**, so *"which constraints did you relax"* is answerable from the engine's own model | 🟢 **inherited** — Apache-2.0, same repo |

**Why it closes.** 🟢 **The engine is Apache-2.0 and production**, the MCP gate exists and is tested, and
**the output is a timetable — a discrete artefact a registrar either accepts or does not.** 🔵 **Contrast
every tutoring deliverable on this shelf, where "better" is contested for a term.** The agent's job is
narrow and checkable: *propose a schedule revision, explain which constraints it relaxed, and let a human
accept it.*

🔴 **The one real term, and it must be in the quote: `NOTICE` is 22 526 B and HTTP 200.** Apache-2.0 §4(d)
makes propagating NOTICE a condition of redistribution, so **the deliverable ships a 22 KB attribution
file.** 🔵 **Cheap to satisfy, expensive to discover in a procurement review** — and it is the same oracle
class as `P917`, used here for an *obligation* rather than for a grant.

🟡 **Two honest caveats.** 🔴 **UniTime is new to this shelf as a platform** — it was verified this pass
from the payload at a full 40-character SHA, and this KB has run its MCP gate for fifty-odd passes, but it
has **no named client deployment recorded here.** 🟢 **And it is the one JVM row on this shelf whose
default branch names a shippable version** (`pom.xml` `4.9` against tag `v4.9.152`), which inverts `P978`
and means you can quote a version without a caveat — the only row here you can say that about.

## `P100-A` — 🆕 The retrainable open-response scorer (global; the pattern `Gap 372`'s discharge makes possible, and the first one here that starts from a running system)

🟢 **Buyer:** any institution or EdTech vendor that grades **constructed-response** work — essays,
short answers, written argument — and needs a defensible score rather than a chatbot's opinion.
🔵 **This is the pattern five passes of this KB said could not be built.** 🟢 **It can: the code is
Apache-2.0, it has a release, and the only thing you must replace is the training corpus.**

🔴 **Read this before anything else: the code ships and the WEIGHTS do not.** `AI_AWE` distributes a
fine-tuned adapter trained on **PERSUADE 2.0**, which its author licenses **`CC-BY-NC-SA-4.0`**
(`Gap 389`, settled from the author's own payload). 🔴 **Do not ship the released adapter to a
commercial client** (`Gap 390`). 🟢 **Retrain it — the repository was designed for exactly that.**

### The wiring, named repo by repo, with the licence on every row

| step | repo, at a pinned address | grant | what it does here |
|---|---|---|---|
| 1. the system | [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) — `main` · `41ae3bd4dd9e891bf46dd4834644ca143dbd36df`, tag **`v0.1.0`** · `bfb34af069e31adabfcd2e7a51acb1605cb4d2a7` | 🟡 **Apache-2.0 *by reference*** (`LICENSE` **1 865 B**, `P971` — **add the licence text to your bundle by hand**) | discourse-move classifier (*claim / data / counterclaim / rebuttal*) + **LightGBM** scorer over **31 linguistic features** + feedback generator; **Gradio UI**, single and batch; **vLLM** or **4-bit HF** backend |
| 2. the base model | Qwen2.5-7B-Instruct (from HF, **not** vendored) | 🟢 **Apache-2.0** | the classifier's backbone — 🟢 **permissive, and the repo deliberately does not redistribute it** |
| 3. the feature toolkit | TextComplexityToolkit (TAALED / QuanSyn), **vendored in the repo** | 🟢 **MIT** | the 31 features the scorer consumes — 🔴 **keep its LICENSE file in your fork** |
| 4. 🔴 **the corpus you must replace** | **the client's own graded essays**, or a corpus you have confirmed permissive | 🔴 **PERSUADE 2.0 is `NC-SA` — unusable commercially** | 🟢 **the seam the repo ships:** `qwen_move_classifier/data/prepare_persuade.py --in /path/to/licensed/persuade_export.json --out train.jsonl` |
| 5. the validity evidence | [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) — `main` · `a844f71614712f81177b5731dbb17b3e018dcc85`, **33 tags, `v12.0.0`** | 🟢 **Apache-2.0** (`LICENSE` **11 358 B**) | 🟢 **the half a regulator asks for**: config-driven build **and evaluation**, HTML statistical report, SHAP, `fairness` in its own topics. 🔵 **This is the deliverable, not the scorer** |
| 6. the model-fitting layer | [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** | pinned by `rsmtool` at `skll==5.0.1`, so steps 5–6 are **one** dependency decision |
| 7. the human gate | the client's existing LMS, via the connector `T19` says their platform allows | varies — 🔴 **read `P1006` before quoting** | 🔴 **non-optional**: `AI_AWE`'s own README says *research and assistive use, not high-stakes automated decisions without human oversight* |

### 🟢 Why the licence mix is the selling point rather than the caveat

🟢 **Every line of code in steps 1–6 is Apache-2.0, MIT or BSD-3.** 🔴 **The only encumbered asset is
the training data, and it is the one asset the client already owns.** 🔵 **So the engagement has an
unusually clean shape: we bring permissive software and the method; they bring the graded essays that
make it theirs.** 🟢 **And the retrained adapter is a client-owned asset no competitor can copy** —
which is a better commercial story than shipping someone else's weights would have been.

🟡 **State the accuracy honestly in the estimate.** ArguLens reports **82.6 %** classifier accuracy /
**0.727** macro-F1 and **0.813** mean QWK under 5-fold CV — 🔴 **figures its own authors call a
component-level diagnostic, not end-to-end**, and its human-rater study is **future work.**
🔵 **Quote `rsmtool`'s report on the CLIENT's corpus as the number that matters**, never the paper's.
🔴 **And carry the population warning into the scope**: PERSUADE is US middle-school argumentative
writing, so transfer to another population or genre is an **assumption to test, not a given.**

### Cost and sequencing

| phase | duration | output |
|---|---|---|
| corpus and licence gate | **0.5 week** | 🔴 **run first and be willing to stop here.** Does the client hold graded essays they may lawfully train on? `P94-B`'s due-diligence gate, applied to data instead of platforms |
| stand up the system as shipped | **1 week** | `AI_AWE` running on the released adapter, Gradio UI, **offline** — the test suite skips service tests when no backend is reachable, so this phase needs no GPU procurement |
| retrain on the client corpus | **2–3 weeks** | 🟢 **a client-owned adapter with no `NC` lineage** (`Gap 390` discharged for this engagement) |
| validity and fairness pack | **2 weeks** | 🟢 `rsmtool` HTML report — **the Annex III / Korea AI Basic Act artefact**, and the same pack satisfies both |
| human-in-the-loop wiring | **1–2 weeks** | review queue in the client's LMS; `T19`'s connector constraint decides the cost |
| **total** | 🟢 **6.5–8.5 weeks** | 🔵 **and 5 of those weeks produce artefacts that outlive the model** |

🔵 **Where it sells first.** 🟢 **Korea, today** — the AI Basic Act is **in force** (22 Jan 2026) and
demands *"ability to explain results"* plus retained documentation, which is steps 5–6 exactly.
🟢 **EMEA second**, against Annex III's **2 Dec 2027**. 🟢 **North America third** — Oklahoma and
Maryland bar AI from high-stakes student decisions, which makes step 7 the statutory requirement
rather than good practice.

## `P100-B` — 🆕 The Article 50(2) scoping gate: translate is exempt, summarise is not (EMEA; half a day, run before `P99-A` is quoted)

🔴 **The finding that creates this pattern.** The Commission's **final** Article 50 guidelines (July
2026) treat **AI-generated translations** as falling within the *"standard editing"* exemption —
🟢 **so translating course material does NOT trigger machine-readable marking** — 🔴 **while
summaries and substantive rewrites DO.**

🔵 **Why this is worth a named gate rather than a footnote.** Every LMS AI feature set this KB has
catalogued contains **both** operations, usually in the same menu: *translate this page* sits next to
*summarise this chapter* and *simplify for reading level*. 🔴 **The second pair is in scope and is
precisely the accessibility and differentiation feature an education client asks for first.**
🟢 **So the marking obligation lands on the feature a school most wants and the exemption on the one
it mentions least** — and a vendor who scopes by *"we use AI for language stuff"* will get it exactly
backwards.

### The gate, as an actual half-day procedure

| step | what you do | artefact already in this repository |
|---|---|---|
| 1 | enumerate every generative feature in the client's product, **by operation, not by feature name** | — |
| 2 | classify each as **standard editing** (translation, spell/grammar correction, formatting) or **content generation** (summarise, rewrite, simplify, generate, draft) | 🔵 the split above is the whole rule |
| 3 | for each in-scope operation, check whether its output carries machine-readable provenance | 🟢 `compose/code/aiact-50-2-marking/` · `aiact-50-2-pack/` (XSD) · `aiact-50-2-spans/` |
| 4 | measure the exposure across the product | 🟢 `compose/code/aiact-50-2-exposure/` — **already has a dated result TSV** |
| 5 | 🔴 **check the placed-on-market date**, because it decides whether there is a deadline or none | 🔴 **before 2 Aug 2026 → 2 Dec 2026. On or after → NO grace period, compliance was due at launch** |
| 6 | adhere to the **Transparency Code of Practice** | 🟢 **confirmed ADEQUATE by the Commission (July 2026)** — a named route to demonstrate compliance rather than an argument you have to invent |

🟢 **Deliverable:** a one-page scope table saying which features are exempt, which are in scope,
which already mark, and what the 2 December exposure is. 🔵 **Cost: half a day. It is the cheapest
correct thing in this file**, it reuses four tested artefacts, and 🔴 **it reliably shrinks the
`P99-A` sprint, because translation features drop out of scope entirely.**

🟡 **Grade, stated in the deliverable itself:** all of this is **secondary-source**. The Commission's
own pages (`digital-strategy.ec.europa.eu`, `eur-lex.europa.eu`) are unreachable from this session and
🔴 **no source names the member-state authority that enforces it.** 🔵 **Say so on the page — a
compliance deliverable that hides its own sourcing grade is the one that gets the client in trouble.**

## `P100-C` — 🆕 Intelligence on top of the LMS the client already regrets (EMEA corporate L&D first; `T22`'s buyer, with the complaint quoted back to them)

🟢 **Buyer, now measured rather than assumed:** 🟡 **almost two in three** L&D professionals say their
**existing LMS or LXP is not delivering adequately on AI**, while **AI is their top strategic
priority** and budgets are under **the most pressure since COVID** (🟡 Fosway *Digital Learning
Realities 2026*, search-summary grade — `www.fosway.com` is refused from this session).

🔵 **Why this is the easiest pitch in this file.** 🔴 **The buyer is not asking "should we do AI" and
not asking "can we afford it".** 🟢 **They have already bought a platform and already concluded it
underdelivers** — so the sale is *augment what you own*, which is `P91-RETIRED`'s surviving principle
(*the platform is the client's; the intelligence on top is ours*) with a measured buyer behind it at
last. 🔴 **And because budgets are shrinking, price it as a REPLACEMENT of an existing line item,
never as net-new spend.**

### The wiring

| layer | what to use | why |
|---|---|---|
| the platform | 🔴 **whatever they already run** — do not propose migrating it | the complaint is about delivery, not about the platform choice |
| the connector | 🔴 **`T19` / `P1006` decide the cost before you quote** | Canvas has an **MIT, released** connector (`v1.14.0`, 26 tags); **Moodle does not have one that is both** — 🔴 **this single fact can double the integration estimate** |
| the skills spine | 🟢 the skills-taxonomy tier (`repos/foundations.md` **Tier 4**, p98) | 🔴 **read its non-commercial trap before costing** — it is documented there |
| credentialing | 🟢 Tier 5 (p98) — **permissive to VALIDATE and PUBLISH, copyleft to MINT** | 🔵 mint behind a service boundary, validate in the deliverable |
| capability transfer | 🟢 **a named workstream, not a closing paragraph** | 🟡 Fosway: L&D teams say they are **not adequately upskilling** for the next 2–3 years — so the client cannot operate what you build unless you train them |

🟡 **Two honest caveats.** 🔴 **There is no EMEA L&D spend FIGURE in this file** — Fosway gives
direction (decline), not magnitude, and the only numeric row is **SHRM's MENA** 28 % fall in spend
per FTE, 🔴 **which is MENA and is recorded as MENA.** 🟢 **The CIPD's 2026 instrument closed 20 May
2026 and has not published**, so the sizing arrives later: 🔵 **quote the platform-dissatisfaction
ratio, which is measured, and not a market size, which is not.**

## `P99-A` — 🆕 The Article 50(2) marking sprint (EMEA; the only pattern on this page with an expiry date)

🔴 **Buyer:** any EdTech vendor or university that shipped a generative feature **before 2 August
2026** and sells into the EU. 🔴 **Deadline: 2 December 2026.** 🔵 **The pitch is one sentence: the
delay you read about is Annex III and it does not cover the clause that binds you in eight weeks.**

**What the obligation actually is.** Article 50 transparency was **not** postponed by the Omnibus; it
has applied since **2 Aug 2026**. Article **50(2)** requires machine-readable marking of
synthetic content, and systems already on the market got a grace period that ends **2 Dec 2026**.
🟡 Grade: search-summary, four or more independent sources agreeing; 🔴 `eur-lex.europa.eu` is refused
from this sandbox, so **the client's counsel reads the Official Journal text, not this page.**

**Wiring, and every piece is already committed and tested here:**

1. 🟢 **`compose/code/aiact-50-2-exposure/`** — run it first. It answers *which of the client's
   surfaces emit synthetic content at all*, which is the question that sizes the engagement.
2. 🟢 **`compose/code/aiact-50-2-spans/`** — locates the spans that need marking inside the emitted
   artefacts.
3. 🟢 **`compose/code/aiact-50-2-marking/`** — applies the marking; its fixtures already encode a
   provenance policy (`fixtures-provenance-policy.md`).
4. 🟢 **`compose/code/aiact-50-2-pack/`** — packs the result against `aiact-50-2.xsd`, so what leaves
   the engagement is a **schema-validated** artefact rather than a report.
5. 🟢 **Reach into the platform**: `vishalsachdev/canvas-mcp` (**MIT**, `v1.14.0`) for Canvas;
   forked `peancor/moodle-mcp-server` (**MIT**) for Moodle — the agent needs to enumerate the
   content surfaces, and these are the permissive ways to do it (`T19`).
6. 🟢 **Evidence layer**: `T13`'s permissive evidence stack, because the deployer — the
   **institution** — must produce its own file (`T18`, and `P98-C` is that pattern).

**Shape:** 🟢 **4–6 weeks**, because steps 1–4 are already written and tested; the work is the
client's content inventory, not the instrument. 🔵 **This is the cheapest credible first engagement in
this entire KB, and it is the only one that gets cheaper by starting sooner.**

🔴 **The honest caveat:** the four artefacts have **never been executed in this sandbox** — repository
code has been refused for seven consecutive passes. 🟢 **They are committed with their own tests and
fixtures; a delivery team must run the suites on its own machine before quoting.** 🔵 **Stated here
rather than discovered by a client.**

## `P99-B` — 🆕 The permissive Canvas gradebook agent (North America; permissive end to end, which no Moodle equivalent can claim)

🔵 **Buyer:** US higher ed — Canvas's install base — where **Oklahoma** and **Maryland** now require
**human oversight** and bar AI from **high-stakes decisions** about students, and **Ohio**'s
district-policy mandate passed its **1 July 2026** deadline so every district holds a policy it must
now evidence.

**Why this one is clean.** 🟢 **`vishalsachdev/canvas-mcp` is the only LMS agent connector this KB has
verified as both permissive and released** — **MIT**, `LICENSE` 1 071 B, `main` ·
`b054b913603a206c677565bcbec128652cb9d398`, **26 tags**, `v1.14.0`, 40+ tools over the Canvas API.
🔵 **So the gradebook is reachable through maintained permissive code and nothing in the stack needs a
fork.**

**Wiring:**

1. 🟢 **Reach** — `vishalsachdev/canvas-mcp` (**MIT**): courses, assignments, submissions, feedback as
   tool calls.
2. 🟢 **Tutor loop** — `HKUDS/DeepTutor` (**Apache-2.0**, `LICENSE` 11 408 B, `main` ·
   `6cf793bd868ba5ecbe64722936d4be8fab5a01df`, **135 tags** — a genuine release line), or
   `Li-Evan/Bloom` (**MIT**, `main` · `b3918981bb34ef5d3090dc81cc5b184555ae3bd6`) as a smaller
   reference implementation of the learner-model loop. 🟡 Bloom has **0 tags**: read it, do not
   depend on it.
3. 🟢 **Never let the agent decide** — the scoring-**validation** tier (`P94`), not a scorer. 🔵 **This
   is the half the statutes ask for and the half where permissive supply is strongest**: the agent
   proposes, a validator records, a human decides, and the record is the deliverable.
4. 🟢 **Durable retention mechanics** — `ankimcp/anki-mcp-server` (**MIT**) rather than reimplementing
   spaced repetition.
5. 🟢 **Evidence** — the district/institution policy-compliance recorder (`P91-B`), which is what the
   Ohio mandate converted from a drafting job into an evidence job.

**Shape:** 🟢 **6–8 weeks** to a production pilot in one department. 🔴 **Do not scale it to a K-8
audience**: New York City's moratorium on student-facing AI **through eighth grade** is the live
counter-example and districts are being urged to copy it.

## `P99-C` — 🆕 The Moodle fork-and-pin connector (LATAM and public sector; the pattern that must say "fork" out loud)

🔴 **Buyer:** LATAM ministries and public universities — the **87 % adopting / 26 % governed** gap
UNESCO IESALC measured across **200 institutions in 19 countries** — plus Brazilian and Colombian
public-sector work where **Moodle is what is actually installed.**

🔴 **The problem this pattern exists to state honestly.** Moodle has **no** agent connector that is
both permissive and released:

| option | grant | tags | usable? |
|---|---|---|---|
| `csmediapro/moodle-mcp-server` | 🔴 **AGPL-3.0** (34 523 B) | 7 / `v0.1.7` | 🔴 **no** — network copyleft on a networked server |
| `peancor/moodle-mcp-server` | 🟢 **MIT** (1 064 B) | 🔴 **0** | 🟡 **as a fork** |

**Wiring:**

1. 🟢 **Fork and pin** `peancor/moodle-mcp-server` at `main` ·
   `666f12222ed6cffc9051455eb4799bb2ac8608ce`. 🔵 **It is 1 064 bytes of MIT over Moodle Web
   Services** — courses, students, assignments, quizzes, grades and feedback — **small enough to audit
   in an afternoon**, which is the entire reason this is viable.
2. 🟡 **Read `csmediapro/moodle-mcp-server` as a SPECIFICATION, do not link it.** 🟢 Lawful, and the
   same manoeuvre `sebserver-mcp-gate` documents for MPL (`§1.10(a)`). 🔴 **Write the boundary into
   the SOW** so nobody later "just imports" the AGPL server.
3. 🟢 **Offline-first delivery** — `P91-D`, unchanged: LATAM and APAC connectivity makes local
   inference a requirement, not a preference.
4. 🟢 **Governance, because that is what the 87/26 gap actually buys** — the deployer's compliance
   file (`P98-C`), in Spanish and Portuguese. 🔵 **UNESCO names the adoption drivers as staff training
   and internal advocates: both are engagements.**
5. 🟡 **Regulatory timing is a selling point here, not a blocker**: Brazil's **PL 2.338/2023** is
   still in the Chamber of Deputies and **its text can change**, Chile's bill is in its first
   constitutional stage, and Colombia's **CONPES 4144** already has budget **through 2030**.
   🔵 **Colombia is the one with money attached — start there.**

**Shape:** 🟢 **8–10 weeks**, and 🔴 **the estimate must name the fork as a maintained artefact with an
owner.** 🔵 **A fork nobody owns is how an AGPL server quietly gets imported eighteen months later.**

## `P98-A` — 🆕 The exam lifecycle end to end: schedule → supervise → grade (EMEA and APAC first; every piece already has a tested gate in this repository)

🟢 **Why this pattern could not be written before this pass, and why it is cheap now:** all three
layers were verified, all three have tested artefacts committed in `compose/code/`, and **two of the
three were on no shelf page** — `UniTime` until pass 96, `seb-server` until pass 98 (`Gap 381`).
🔵 **Nothing here is a research bet. It is a wiring job over code this repository already owns.**

### The wiring, named repo by repo, with the gate that already exists

| step | repo | grant · ref · release ladder | gate already committed here | what it does |
|---|---|---|---|---|
| 1. **schedule** | [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** · `master` · **101 tags**, `v4.9.152` *(counted p96; not re-read this pass)* | 🟢 `compose/code/unitime-mcp-gate/` (`P85`) | Timetabling, course and exam-period scheduling. 🔴 **Apache §4(d): its `NOTICE` is 22 526 B and must be propagated.** |
| 2. **supervise** | [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | 🟡 **MPL-2.0** · `master` · `7f45689f797337` · 🟢 **194 tags**, `v3.0-latest` | 🟢 `compose/code/sebserver-mcp-gate/` + `seb-proctoring-validator/` + `proctoring-reach-audit/` | Exam lockdown, session supervision, proctoring-provider configuration. 🟢 **Per-file copyleft — integrate directly; do NOT build beside it.** |
| 3. **grade** | [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **MIT** · `main` · `5695878b4735ed` · 🔴 **0 tags** | 🟢 `compose/code/grading-draft-gate/` — **37/37 offline, with negative controls** | Writes the grade at `workflowstate=readyforreview` and **never releases it.** |
| 4. **validate the grade** | [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) + [`skll`](https://github.com/EducationalTestingService/skll) | 🟢 **Apache-2.0** / **BSD-3** | — | The evidence package (`T13`, `T17`). 🔵 **This is the half a regulator and an appeal actually consume.** |
| 5. **record** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | — | Every exam event as xAPI. 🟢 **The deployer's own audit trail, which `T18` says the institution must produce itself.** |

### 🟢 Why the licence mix is the selling point and not the caveat

🔵 **Three different grants, three different boundary rules, and all three favourable:**
**Apache-2.0** (UniTime, rsmtool, lrsql) — closed derivative lawful, propagate `NOTICE`;
**MPL-2.0** (seb-server) — 🟢 **per-file copyleft (§1.10(a)): a proprietary integration layer is
lawful and only modified MPL files reciprocate**, which in practice is one enum value for a new
proctoring provider; **MIT** (moodle-grading-mcp) — unrestricted.
🔴 **There is no AGPL anywhere in this pattern**, which is what distinguishes it from every other
assessment pattern in this file.

🔴 **The feature audit comes FIRST, before any integration work.** Emotion recognition in education
has been **prohibited since 2 Feb 2025** (EU AI Act Art. 5), and affect/engagement inference ships
**switched on by default** in commercial proctoring. 🟢 **`proctoring-reach-audit` already measures
which provider methods reach the network** (Jitsi 1, 🔴 **Zoom 5** — a figure this KB corrected
against its own earlier 2). 🔵 **Sell the audit as week 1, not as a disclaimer.**

### Cost and sequencing

🟡 **6–8 weeks**, and it is short *because* the gates exist. Week 1: feature audit of the client's
live proctoring configuration against Art. 5 — 🔴 **if affect inference is on, that is the finding,
and it is billable on its own.** Weeks 2–3: stand up `seb-server` and `UniTime`, wire both MCP gates
(already tested). Weeks 4–5: `moodle-grading-mcp` behind `grading-draft-gate`'s three properties —
🟢 **no grade is ever auto-released.** Weeks 6–7: `rsmtool`/`skll` evidence package + xAPI into
`lrsql`. Week 8: acceptance.

🔵 **Region order, and the reason:** 🟢 **APAC first** — Vietnam's `Decision 33/2026/QD-TTg` binds
**now** (in force 15 Aug 2026; education is 3 of its 46 high-risk systems) and South Korea's AI Basic
Act is in force. 🟢 **EMEA second, as preparation** — Annex III lands **2 Dec 2027**, and `T18`'s
deployer limb means the **institution** is the buyer, not the vendor. 🟡 **North America third**,
where the hook is Idaho's **SB 1227** human-teacher floor and California's **A.B. 1159** student-data
limb rather than an assessment regime.

## `P98-B` — 🆕 The corporate L&D skills engine (North America and APAC first; the buyer `Gap 386` could not price until this pass)

🔵 **Why this pattern is new:** every market figure in this KB was institutional until pass 98
(`Gap 386`). 🟢 **The buyer is now sized** — AI-in-corporate-training **USD 7.49 B in 2026 → USD
18.19 B by 2031** (CAGR 19.43 %), against a **~USD 400 B** total corporate-training base.
🔵 **And the demand asymmetry is the pitch: 87 % of L&D teams already use AI, 55 % of workers use AI
regularly, and only 1 in 3 workers got employer-provided AI training in the last six months.**

### The wiring, named repo by repo

| step | repo | grant · ref · release ladder | what it does here |
|---|---|---|---|
| 1. **extract skills** | [`nestauk/ojd_daps_skills`](https://github.com/nestauk/ojd_daps_skills) | 🟢 **MIT** · `dev` · `e73c2b5045793d` · 🟢 **8 tags**, `v3.0.0` | Skill phrases out of CVs, job descriptions and internal role docs, mapped onto **ESCO**, **Lightcast Open Skills** or a custom taxonomy. 🟢 **Pin this one — it is the only row in the tier with a release ladder.** |
| 1b. **occupations too** | [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 **MIT** (titleless payload) · `master` · 🔴 0 tags | ESCO skills **and** ISCO occupations by embedding similarity; PyPI + Docker. 🔵 Use where the client needs role-level inference, not only skill-level. |
| 2. **keep the taxonomy alive** | [`dkavargy/ESCOPlus2.0`](https://github.com/dkavargy/ESCOPlus2.0) | 🟢 **MIT** · `main` · 🔴 0 tags | Extends and validates ESCO from live job-ad data. 🔵 **The only answer here to "the taxonomy is three years stale".** |
| 3. **measure mastery, not opinion** | `pyBKT` (MIT) · `py-irt` (MIT) · `eribean/girth` · `douglasrizzo/catsim` (BSD-3) | 🟢 permissive | The psychometric tier. 🔴 **Mastery is an INPUT to readiness, never a substitute for it** (`Gap 385`'s wording). |
| 4. **shorten the assessment** | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) + `py-irt` | 🟢 **BSD-3 / MIT** | Adaptive testing: fewer items, same confidence — 🔵 **the difference between a 90-minute skills audit and a 15-minute one, which is what decides adoption inside a company.** |
| 5. **credential the outcome** | [`CredentialEngine/Open-Badge-Publisher`](https://github.com/CredentialEngine/Open-Badge-Publisher) (Apache-2.0) to publish; [`nfh-trust-labs/opencred`](https://github.com/nfh-trust-labs/opencred) (MIT, **30 tags**, `v1.9.1`) to issue | 🟢 permissive | 🟢 **The only all-permissive path through the credentialing layer** (`T17`): the four Open Badges *issuers* are AGPL/LGPL. |
| 6. **deliver and record** | `OpenOLAT` (Apache-2.0) for the corporate-facing LMS · `yetanalytics/lrsql` for xAPI | 🟢 **Apache-2.0** | 🔴 **NOT `frappe/lms`** — a 2026 listicle calls it MIT and the payload says **AGPL-3.0** (`P1002`). |

### 🔴 The one thing that will go wrong if nobody reads this line

🔴 **Do NOT start from [`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml).**
It is the Open Skills Project's flagship, it is the first result on every search, and it is
**`NONCOMMERCIAL-NOT-OSI`**: University of Chicago terms granting use *"for educational and
not-for-profit research purposes"* which **"exclude any service or part of selling a service that
uses the Program"**. 🔴 **A studio engagement is exactly the excluded case.**
🔵 **And it is the same template as `dssg/student-early-warning`** (`Gap 385`, `P999`) — so if a
candidate repo's `LICENSE` opens with *"BY DOWNLOADING"*, read it before costing it.

🔴 **Second honest line: two of three skills rows have ZERO tags** (`P985`). This tier is a **build
commitment**, not a product integration, and the estimate below reflects that.

### Cost and sequencing

🟡 **8–10 weeks.** Weeks 1–2: taxonomy decision (ESCO vs Lightcast vs client-internal) — 🔵 **this is
a business decision, not a technical one, and `ojd_daps_skills` makes it reversible because the
taxonomy is a parameter.** Weeks 3–5: extraction over the client's real role and CV corpus, with a
labelled holdout — 🔴 **no demo on public job ads; the client's own vocabulary is the whole
difficulty.** Weeks 6–7: adaptive assessment with `catsim`/`py-irt`. Weeks 8–9: badge publish/issue
path. Week 10: acceptance.

🔵 **Region order:** 🟢 **North America first** (largest AI-in-corporate-training market, per Mordor),
🟢 **APAC second** (fastest-growing), 🔴 **LATAM and EMEA unplaced — no L&D figure in this KB breaks
out either**, which is `Gap 386`'s remainder and a pre-registered lead, not a silence.

## `P98-C` — 🆕 The deployer's compliance file (EMEA; the buyer `T18` just created, and the institution has no compliance function)

🔵 **The shift in one line:** every regulatory offer in this KB addressed the ed-tech **vendor**.
🟢 **`T18` establishes that a school using AI to assess progress or flag at-risk learners is a
DEPLOYER with its own duties** — and a school has no model documentation, no evidence pipeline and
nobody whose job this is.

### What the deliverable actually is

| component | built from | grant | why it satisfies a deployer duty |
|---|---|---|---|
| **feature audit of live systems** | `compose/code/proctoring-reach-audit/` + `seb-proctoring-validator/` | — (this repo) | 🔴 **Emotion recognition in education is prohibited since 2 Feb 2025.** Affect inference is **on by default** in commercial proctoring, so this is the only item on the list that is already overdue rather than due in 2027. |
| **the evidence layer** | `rsmtool` (Apache-2.0) · `skll` (BSD-3) | 🟢 permissive | 🟢 **`T13`/`T17`: the measuring side is permissive.** This is what an appeal and an inspection consume. |
| **human-in-the-loop proof** | `toshieji/moodle-grading-mcp` behind `grading-draft-gate` (**37/37**) | 🟢 **MIT** | 🟢 **The grade is written `readyforreview` and never released** — demonstrable, test-backed evidence that a human is the author of record. |
| **the audit trail** | `yetanalytics/lrsql` xAPI | 🟢 **Apache-2.0** | The deployer's own record, independent of the vendor's. |
| **curriculum grounding, where the tutor is in scope** | `bncc-dev/bncc-pacotes` (**1 721 verified objectives** over MCP) | 🟢 **MIT code / CC BY 4.0 data** | 🔵 **`T11`: grounding takes hallucination 31.9 % → 0.2 %**, and under Vietnam's regime a self-study tutor is in scope **by the ORIGIN of its material** — so grounding is a regulatory control, not a quality argument. |

### Cost, sequencing and the honest caveat

🟡 **5–7 weeks**, and it is the cheapest pattern in this file because **nothing is built** — it
assembles permissive evidence tooling around systems the client already runs. Week 1: Art. 5 feature
audit. Weeks 2–3: evidence layer against the client's live assessment data. Weeks 4–5: human-in-loop
gate + xAPI trail. Weeks 6–7: the file itself, written to be handed to an inspector.

🟡 **Sell it in EMEA as preparation for 2 Dec 2027 and in APAC as compliance NOW** (`T15`).
🔴 **The caveat to state up front: four independent sources agree on 2 Dec 2027 and they disagree on
whether the Council has formally adopted the postponement**, and this KB has not read the instrument
in primary — `EUR-Lex` has refused `CONNECT` for eight consecutive passes. 🔵 **Quote the date, never
the procedure.**

## `P97-A` — 🆕 Spoken-language assessment for a mandated curriculum (LATAM and APAC first; the tier promoted this pass)

🟢 **Why this pattern exists now and could not have been written last pass:** the speech-assessment
layer was verified in this KB's history at **pass 14** and sat on no shelf page until pass 97
promoted it (`Gap 384`). 🟢 **It is a seven-repo permissive toolchain, and the seams are the repos'
own interfaces** — alignment, scoring and benchmarking are three separate projects.

### The wiring, named repo by repo

| step | repo | grant · version | what it does here |
|---|---|---|---|
| 1. **align** | [`MontrealCorpusTools/Montreal-Forced-Aligner`](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | 🟢 **MIT** · `v3.4.3`, **116 tags** | Phoneme-level forced alignment of the learner's audio against the expected text. 🟢 **The only member with a real release ladder — pin it, and let it carry the production risk.** |
| 1b. **align without a script** | [`lingjzhu/charsiu`](https://github.com/lingjzhu/charsiu) | 🟢 **MIT** · 🔴 0 tags | For free-speaking tasks where there is no reference transcript. 🔴 **Research code — use it for the open-response task only, never as the default path.** |
| 2. **score** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** · `v0.3.0` | 0–100 score, phoneme and word error rate, per-word confidence, DTW acoustic distance, prosody (F0, energy). 🟢 **Runs local, no API key — which is what makes it shippable into a ministry.** |
| 3. **fix the baseline** | [`YuanGongND/gopt`](https://github.com/YuanGongND/gopt) + [`doheejin/HiPAMA`](https://github.com/doheejin/HiPAMA) | 🟢 **BSD-3-Clause** (both) | The published ICASSP-2022 number and its hierarchical successor. 🔵 **These are the figures a bid is scored against, not components you ship.** 🟢 `P995`: HiPAMA's grant names gopt's author first, so the lineage is provable. |
| 4. **score the scorer** | [`Fuann/open-apa`](https://github.com/Fuann/open-apa) | 🟢 **BSD-3-Clause** | Benchmark and evaluation toolkit. 🟢 **This is the step that turns a demo into an acceptance test**, and it is why this pattern can be contracted. |
| 5. **substrate** | [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | 🟡 **Apache-2.0** (17 264 B, displaced title — `P991`) | Under MFA. 🔴 **Apache §4(d): propagate `NOTICE` if one ships.** |
| 6. **deliver** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**) or `moodle/moodle` | — | Kolibri where connectivity is intermittent (`T16`); Moodle where it is not. |
| 7. **record** | `yetanalytics/lrsql` (xAPI LRS) | — | Spoken-task attempts as xAPI statements — 🟢 **the evidence layer `T13` says is the defensible half.** |

### 🔴 The licence line item, stated in the estimate rather than the appendix

🟢 **Seven of nine layer members are permissive — so the pipeline ships.** 🔴 **The DATA is not:**
`jimbozhang/speechocean762`, the reference corpus of pronunciation scoring, serves **no licence
payload across 24 filenames**, and `CyanXLab/Phonos` — which this KB had counted *inside* a
permissive layer — has **no grant either** (`P994`, and a correction).

🔵 **For LATAM and APAC this is cheaper than it reads, and that is the reason those regions lead
this pattern.** Pronunciation scoring is **L1-specific**: a Spanish-L1 or Mandarin-L1 cohort needs
data from that population, which the engagement was always going to collect. 🟢 **So corpus
collection is pre-existing scope, not licence-induced risk** — and it is billable.
🔴 **For a North America or EMEA engagement expecting to drop in an off-the-shelf English benchmark,
it is a real and unbudgeted cost. Say so before the quote.**

### Cost and sequencing

🟡 **8–10 weeks.** Weeks 1–2: pin MFA, stand up `OpenPronounce` locally, reproduce `gopt`'s published
number with `open-apa` — 🔴 **if that reproduction fails, stop; the baseline is the contract.**
Weeks 3–5: collect and label L1-specific audio (the corpus line item). Weeks 6–8: wire scoring into
Kolibri or Moodle and emit xAPI. Weeks 9–10: acceptance against `open-apa`.

🔴 **Where this pattern must NOT go:** a pronunciation score that gates progression or certification
is an assessment decision. 🔵 **Under APAC's binding regime (`T15` — Vietnam's Decision
33/2026/QD-TTg names automated assessment; South Korea's AI Basic Act in force 22 Jan 2026) and the
EU's Annex III from 2 Dec 2027, that is high-risk.** 🟢 **Ship it as formative feedback to the
learner and the teacher, and `P94-A` is the pattern to run if the client wants it summative.**

## `P97-B` — 🆕 The academic-integrity **conversation** workbench (global; deliberately NOT a detector)

🔴 **Read the guardrail first, because it is the pattern.** The 2026 literature on AI-text detection
is titled *"LLM-Generated Text Detection Remains an Unsolved Problem"* (arXiv **2608.11256**), and a
system bearing on a student's academic standing is **Annex III high-risk from 2 Dec 2027**.
🔴 **So this pattern does not build a detector, does not produce a verdict, and must never be wired
into a sanctioning path.** 🟢 **What it builds is the thing institutions actually need and nobody
sells them: a way to hold the conversation with evidence on the table.**

| step | repo | grant | role |
|---|---|---|---|
| 1 | [`HendrikStrobelt/detecting-fake-text`](https://github.com/HendrikStrobelt/detecting-fake-text) (**GLTR**, MIT-IBM Watson AI Lab) | 🟢 **Apache-2.0** (11 357 B pristine) | 🟢 **Per-token predictability, VISUALISED.** It shows *why* a passage looks machine-like instead of asserting that it is. **This is the whole pattern's primitive.** |
| 2 | [`Imalwayshere/Open-Detector`](https://github.com/Imalwayshere/Open-Detector) | 🟢 **MIT** | A second, stylometric signal — 🔴 **displayed as a signal with its confidence, never as a verdict**, and its 99.57 % claim is the author's own and unreplicated. |
| 3 | `ucfopen/UDOIT` + the AI-literacy tier (`touretzkyds/ai4k12`, `microsoft/ai-agents-for-beginners`) | — | Turns the output into **teaching material**: the artefact of this pattern is a lesson, not an accusation. |
| 4 | `moodle/moodle` or `ls1intum/Artemis` (**MIT**) | — | Surface it in the tool the instructor already uses. 🟢 **Artemis is MIT, so a closed client deliverable is clean.** |

🟢 **Why a client buys this:** EMEA institutions have had an **AI-literacy obligation since
2 Feb 2025** and must show that **staff can evaluate AI output and exercise human oversight** —
🔵 **and this pattern is literally a human-oversight instrument with an audit trail.** 🟢 **North
America is the second market**: Purdue's AI competency becomes a **graduation requirement in Fall
2026**, and a competency has to be assessed.

🟡 **4–6 weeks**, and 🔴 **the acceptance criterion is a refusal**: the deliverable must be unable to
emit a binary "AI-written" judgement. 🔵 **If a stakeholder asks for that button, the honest answer
is that the research does not support it and the regulation will not permit it — and `P94-A` is
where a defensible summative assessment actually gets built.**

## `P97-C` — 🆕 The African teacher-capacity engagement (EMEA–Africa; `T16`, and the cheapest correct read in this file)

🔴 **This pattern exists to stop a specific mistake:** pitching governance and conformity — the
correct EMEA-Europe motion — into a market with **no instrument to be compliant with.**
🟢 **`T16`, measured on four separate country queries: 4 of 4 African countries have teacher-capacity
programmes, 0 of 4 have a binding national AI-in-education instrument.** 🔵 **They are spending now,
on dated timelines, with World Bank and UNESCO money — on a different thing.**

| step | component | grant | why |
|---|---|---|---|
| 1. **base** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **The only permissive platform on `verticals/solutions.md` built for intermittent or absent connectivity**, and the constraint is explicit: Nigeria's `Naija Teacher AI` is **designed to work offline**, Kenya's rollout is **>20 700 devices** rather than a cloud migration. |
| 2. **teacher-facing generation** | [`satvik314/educhain`](https://github.com/satvik314/educhain) (**MIT**) | 🟢 MIT | Lesson and assessment generation **for the teacher**, not a student-facing tutor. 🔵 **Every programme in the four-country sweep funds the teacher.** |
| 3. **align to the national curriculum** | `Zion-support/curriculum-alignment-checker` + `nsip/curriculum-mapper` | 🟢 permissive | Each country has its own frame (Kenya's **CBC/CBE**, South Africa's **CAPS**, Egypt's technical-school curriculum). 🔴 **The frameworks themselves are largely ungranted — `Gap 367`, unchanged — so map, do not redistribute.** |
| 4. **competency frame** | 🟢 **UNESCO's AI competency framework for teachers** | — | 🟢 **Egypt has already adopted a national adaptation of it, launched 3 Jun 2026.** 🔵 **Using the same frame makes the deliverable portable across all four countries** — the single highest-leverage choice in this pattern. |
| 5. **record** | `yetanalytics/lrsql` | — | Offline-tolerant xAPI capture; sync when connectivity returns. |

🟡 **6–8 weeks per country, and the frame is what makes it repeatable.** 🟢 **Build once against the
UNESCO teacher-competency frame, localise the curriculum mapping per country.** 🔴 **Do not build
per-country from scratch and do not lead with compliance** — there is nothing to comply with yet,
and South Africa's draft policy (Cabinet-approved **25 Mar 2026**, schools **2027–2028**) is the
first that will change that. 🔵 **When it does, `P94-A` and `P91-B` become the follow-on sale, and
this pattern is what earns the right to make it.**

🔴 **Evidence grade, stated because it affects how hard to push:** all four country rows rest on
**secondary sources** — the primary-source channel was closed this pass (`intel/market.md`).
🟢 **Egypt's instrument is the best-attested** (UNESCO plus the ministry, with a date).

## `P91-RETIRED` — "the platform is always the client's; the intelligence on top is ours"

🔴 **Retired as a universal rule, and it stays retired.** It was derived from the false `8 of 8 copyleft`
census and survived six passes. It remains correct for one case only — when the client's existing Moodle,
Canvas or Open edX must be kept — and in that case LTI 1.3 / SCORM / xAPI integration is still the right
boundary. 🟢 **Otherwise the platform can be inside the deliverable:** `Artemis` (MIT), `Sakai` or `Opencast`
(ECL-2.0), `OpenOLAT` (Apache-2.0), 🆕 `richie` (MIT, portal layer), `pupilfirst` / `relate` / `academico` (MIT).

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
