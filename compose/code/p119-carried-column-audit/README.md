# `p119-carried-column-audit` — ACTIONS F, G, H, I

**Pass 119, 2026-10-11.** Discharges all four actions p118 pre-registered. Two
are **refuted on their own clauses**, and both refutations located a defect
worth more than the action would have been.

`./test_p119.sh` → **43 passed / 0 failed**, fully offline against captured
evidence (`stars.2026-10-11.tsv`, `evidence-f/`, and p118's own `evidence/`).

## Channels, measured this pass

| channel | state | what it carried |
|---|---|---|
| `git ls-remote` (anonymous) | 🟢 OPEN | default branch + HEAD SHA; **follows renames silently** |
| `raw.githubusercontent.com` | 🟢 OPEN | the ACTION F sibling licence files |
| MCP relay `/search/repositories` | 🟢 OPEN | star counts, `archived`, `fork`, `default_branch`, 90 + 160 addresses |
| MCP relay `/repos/{owner}/{repo}` | 🔴 refused | unchanged from p118 |
| `curl api.github.com` from the shell | 🔴 `http=403` | *"sessions are bound to their configured repositories"* — scoped, not rate-limited |

🔴 **The two open channels disagree about what exists, and that disagreement is
this pass's main instrument.** `git` follows a rename and a fork without
comment; the search index answers only on the canonical, non-fork name. An
address that `git` resolves and search does not is therefore *evidence*, not a
failure — which is why every such address was classified rather than dropped.

## `ACTION I` — 🟢 DISCHARGED, **not refuted**

Clause: *refuted if a carried non-licence column is wrong on fewer than 3
addresses.* Three separate carried columns are wrong on **14 addresses** in all.

### The star column — 130 claims, 90 addresses, 7 cells wrong

| verdict | rows | meaning |
|---|---|---|
| `EXACT` | 95 | claimed == measured |
| `DRIFT` | 28 | within `max(2, 2 %)` — consistent with growth since the claim |
| 🔴 `WRONG` | **7** | outside that band, on **5** addresses |

🔴 **Every one of the 7 sits at ≥ 78 % page depth. Not one is above it.** The
head of each page (re-measured every pass) is `EXACT` or small `DRIFT`; the
tail carries figures no pass has touched since it wrote them. Four of the seven
were written in **k-form** — `1.2k`, `1.1k`, `1.3k`, `~430` — which is the
signature of a figure that was *never* a measurement.

🟡 **Stated plainly, because the letter of the clause flatters it: this is a
weaker finding in kind than `ACTION E`'s.** A wrong licence is categorical — MIT
versus GPL is a different obligation. A star count 4.3 % stale is the same fact,
slightly out of date, and 6 of the 7 understate rather than overstate. The
column is wrong; it is not dangerous.

All 7 are repaired by `repair.py` and the repair is verified by re-extracting
and re-scoring: **102 `EXACT`, 28 `DRIFT`, 0 `WRONG`.**

### The liveness column — 5 archived repositories, never recorded as archived

🔴 **This one *is* dangerous, and it is the column nobody had looked at.**

| address | ★ | what the KB said |
|---|---|---|
| `adlnet/SCORM-to-xAPI-Wrapper` | 99 | no archived flag anywhere |
| `adlnet/xAPI-SCORM-Profile` | 42 | *"the authoritative SCORM → xAPI profile"*, and `intel/market.md` sold it as **permissive substrate for a compliance build** |
| `adlnet/SCORM-to-TLA-Roadmap` | 7 | no flag |
| `moodlehq/moodle-tool_dataprivacy` | 8 | no flag; default branch `MOODLE_34_STABLE` |
| `nsip/curriculum-mapper` | 1 | no flag |

An archived repository is read-only: it cannot take a patch, ship a CVE fix, or
answer an issue. Recommending one as a build dependency is a different class of
error from a stale star count. 🔵 Three more declare themselves dead **in their
own description** while GitHub still reports them live — `kuali/rice`
(*"DEPRECATED"*), `Apereo-.../OpenDashboard-legacy` (*"(Deprecated)"*),
`atutor/ATutor` (*"NO LONGER USER LEVEL SUPPORTED"*).

🟢 **`Gap 354` has an answer it never looked for.** The gap records
`adlnet/SCORM-to-xAPI-Wrapper` as an *"upstream-askable negative"* — a project
that will not answer. It is archived. Nobody is going to answer.

### The identity column — 4 forks, 3 stale addresses, and 2 double-counts

🔴 **`249 addresses` is at most `247` repositories.** Two pairs are one
repository each, proven by **identical HEAD SHA**, with both spellings held:

| held address | held address | HEAD SHA |
|---|---|---|
| `openedx/edx-platform` | `openedx/openedx-platform` | `2e46ebdf508c` |
| `frdel/agent-zero` | `agent0ai/agent-zero` | `e3051fb584b1` |

🔴 **4 addresses are FORKS** (`fork:true`), carried as if canonical:
`mitodl/open-learning-ai-tutor` (**1★**, published on the agent shelf as *"MIT
Open Learning's tutor"*), `GEMLab-HKU/Unlearn_and_Relearn` (5★, an AIED 2026
full paper), `mlx-cassio/awesome-eu-ai-act` (0★, a fork of
`GenAI-Gurus/awesome-eu-ai-act` at 106★ — **both held**), `CSR2017/edfi-oneroster` (0★).

🟢 **3 more are stale addresses that redirect**, each proven by SHA:
`project-sunbird/knowledge-platform` → `Sunbird-Knowlg/...`,
`project-sunbird/sunbird-lms-service` → `Sunbird-Lern/...`, `openedx/ease` ≡
`edx/ease`. 🔵 **1 is unexplained and stays that way**:
`garethmanning/claude-education-skills` resolves over `git`, is not a fork, and
has no rename target this pass could find.

### `P119-B` — and this retracts a sentence `intel/market.md` has carried for nineteen passes

🔴 The page said `api.github.com http=403` was *"the cause of every `—` in a ★
column"*. **For 4 addresses the cause is that the address is a fork**, and the
search channel excludes forks unless `fork:true` is passed. One query flag
turned 4 permanent dashes into numbers. Both the explanation and the dash were
carried, never tested — `ACTION I`'s thesis demonstrated on `ACTION I`'s own
evidence channel.

## `ACTION G` — 🔴 **REFUTED**

Clause: *refuted if the two append-only pages' CURRENT-section claims disagree
with the tree on fewer than 5 addresses.* Ran p118's own extractor and verdict
layer over the current sections only (`agents/trending.md` L1–73,
`repos/trending.md` L1–71): **27 claims, 17 addresses, 23 `AGREE`, 4 `UNREAD`,
0 `WRONG`.** Zero is fewer than five.

🟢 **The refutation confirms the depth finding from the opposite direction.**
The append-only pages' current sections are written fresh from measurement each
pass and they are clean. The format is not the problem — *carrying* is. An
append-only page is honest about which pass believed what; a "live" page
presents a four-passes-stale tail as current.

## `ACTION H` — 🔴 **REFUTED**, and the refutation is the finding

Clause: *refuted if the residual `WRONG` count does not fall to the 14
split-licence rows exactly.* Implemented the retraction-context skip
(`extract-h.sh`) and held **p118's own verdict layer fixed**, changing only the
extractor. Residual fell **21 → 19**. Not 14.

🔴 **First, p118's residual accounting is off.** Its README reports *"17 residual
`WRONG` rows"* and *"2"* for `advisingapp`; its own `verdict2.2026-10-11.tsv`
holds **21** and **5**. The prose undercounts its own evidence file by 4.

🔴 **Second, the survivors are not retraction cells. `advisingapp` can never
score `AGREE`.** Its measured grant is `ElasticLicense-2.0-NOT-OSS`, and the
extractor's token alternation contains **zero** entries for Elastic
(`grep -c Elastic extract.sh` → `0`). So the only matchable token on each row is
the `AGPL-3` in the *explanatory* prose, and all 5 rows were guaranteed `WRONG`
whatever the page said. Three of them publish **Elastic-2.0 correctly**.

🔴 **`ElasticLicense-2.0-NOT-OSS` is the only measured grant in the whole census
that no possible claim can match** (`unmatchable.sh`) — and it accounts for
**5 of p118's 21 `WRONG` rows, 24 %.** p118 added the token to the MEASURED
side when it discovered the licence class and never to the CLAIM side.

🔵 This is `F5`'s shape a **fifth** time — *an alternation missing an entry* —
and `P471`/`P117-K`'s a sixth. The lesson now has a sharper form: **when a sweep
learns a new token, it must learn it on BOTH sides, or every row that adopts the
new token is scored wrong for adopting it.**

## `ACTION F` — 🟢 DISCHARGED, **not refuted**, and it found the costliest cell in the KB

Clause: *refuted as unnecessary if fewer than 3 of the 5 resolve to a grant that
differs from what the KB publishes.* **3 of 5 differ.**

| address | KB published | resolved from the sibling file it names | differs |
|---|---|---|---|
| `leemonade/leemons` | 🟢 **Apache-2.0** | 🔴 **"Fair Code License" v1.0, built on the Sustainable Use License.** Zero occurrences of "apache" in the file | 🔴 **yes, severely** |
| `learning-commons-org/evaluators` | 🟢 **MIT** | 🟡 MIT code + CC BY 4.0 prompts + 🔴 **CC BY-NC-SA 4.0** on the annotated CLEAR and PERSUADE 2.0 corpora | 🔴 **yes** |
| `learning-commons-org/knowledge-graph` | `MULTI-GRANT-FRAMEWORK` | CC BY 4.0 / CC0 / MIT **plus an "Open + Gated" and "Gated" tier covered by no open licence at all** | 🟡 incomplete |
| `bncc-dev/bncc-pacotes` | split grant, MIT for code | `LICENSE-CODIGO.md` = MIT, `LICENSE-DADOS.md` = CC BY 4.0 | 🟢 no |
| `bncc-dev/bncc-benchmark` | split grant, MIT for code | identical structure | 🟢 no |

🔴 **`leemonade/leemons` is the most commercially consequential error this KB has
held.** The licence restricts use to managing *the User's own* educational
services, permits redistribution only *free of charge and non-commercial*, and
bills **€100 000** once the platform passes **1 000 users or profiles** or €1 M
annual revenue, plus a **5 % royalty** after year one. The KB published it as a
green permissive Apache-2.0 on the foundations shelf and in a compose pattern.

## 🔴 `P119-A` — why p118's 957-claim sweep could not have caught `leemons`

This is the mechanism, and it generalises.

1. `leemons`' root grant is a prose index, so p118 measured it `UNKNOWN`.
2. `UNKNOWN` → verdict `UNREAD`, which p118's layer correctly refuses to fold
   into `AGREE`: *"not contradicted, not corroborated."*
3. `repair.py` is driven by the verdict file, so — also correctly — it *cannot
   touch an unmeasured row*.
4. Therefore the stale 🟢 Apache-2.0 survived a 957-claim whole-KB sweep **by
   design**, and nothing followed up on the `UNREAD` pile.
5. An earlier pass had **already found the right answer** and published it on
   `verticals/solutions.md` and `intel/trends.md` — so this is `P118-D`'s
   page-local correction, one layer deeper: the correction was page-local *and*
   the sweep built to catch page-local corrections was blind to this row.

🔴 **The dangerous cell is `UNREAD` + a permissive claim, and there are 42 of
them across 22 addresses** — 76 % of p118's 55 `UNREAD` rows claim MIT,
Apache-2.0 or BSD against a grant the sweep could not read. p118's own `P118-K`
wrote the reason down: *absence of a licence reads as permission.* It applied
that lesson to the measurement and not to the verdict.

## Repaired in this commit

| cells | what |
|---|---|
| **7** | star counts, driven by `verdict.2026-10-11.tsv`; re-scored to 0 `WRONG` |
| **2** | `leemonade/leemons` 🟢 Apache-2.0 → 🔴 Fair Code v1.0, with the €100k / 5 % trigger named where a builder reads it |
| **2** | `learning-commons-org/evaluators` 🟢 MIT → 🟡 MIT code · 🔴 corpora CC-BY-NC-SA-4.0 |
| **6** | 🔴 **ARCHIVED** markers on the 5 archived repositories' rows |
| **1** | `mitodl/open-learning-ai-tutor`: `—` → `1 (fork:true)` |
| **1** | `intel/market.md`'s nineteen-pass claim that the 403 explains every `—` |
| **1** | `intel/market.md`'s compliance-build recommendation now names the archived upstream |

## Pre-registered for p120, each with its refutation clause

🟢 **`ACTION J` — resolve the remaining 20 `UNREAD` + permissive-claim addresses
by following each one's prose index, as `ACTION F` did for 5.** `leemons` was 1
of 22 and cost the most; 20 are unexamined. 🔴 **Refuted if fewer than 3 of the
20 resolve to a grant that is not permissive.**

🟢 **`ACTION K` — add `Elastic-2.0`, `Fair-Code`, `SustainableUse`, `BUSL` and
`SSPL` to the extractor's CLAIM-side alternation, then re-run `ACTION E`.** The
claim side cannot express the licence classes this KB has already discovered.
🔴 **Refuted if the residual `WRONG` count does not fall below 19.**

🟢 **`ACTION L` — re-measure the TAIL of every live page, below 78 % depth,
where all 7 wrong star cells sat and no pass has been since.** 🔴 **Refuted if
the tail's non-licence columns are wrong on fewer than 5 further addresses.**

🟢 **`ACTION M` — de-duplicate the census to 247 and re-derive every per-address
percentage published against a denominator of 249.** 🔴 **Refuted if no
published figure moves by more than one percentage point.**
