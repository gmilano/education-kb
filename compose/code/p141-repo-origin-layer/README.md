---
industry: education
region: Global
updated: 2026-10-12
---

# `p141-repo-origin-layer` — `ACTION CY`: 🔴 REFUTED. The repository layer places nothing, and for four of six it does not exist

## The action, as p140 wrote it

> Run the `p140-origin-evidence` probe over the **repository** layer of the rows it could not
> place: `git log` author email domains and any `FUNDING.yml`, for the six npm rows that
> yielded no origin signal in their payloads. 🔴 *Refuted if the repository layer places no
> additional row — which would mean `T29`'s "origin is in the code" is specifically about
> compiled-in hosts, not about code generally.*

## Verdict: 🔴 **DISCHARGED and REFUTED. 0 of 6 placed.**

[`result.2026-10-12-p141.tsv`](result.2026-10-12-p141.tsv), control verified on the run
(`definitely-not-a-real-repo-p141` readable=`False`):

| row | declared repository | readable | institutional email domains | funding file | verdict |
|---|---|---|---|---|---|
| 🔴 `@imazhar101/mcp-canvas-server` 2.1.3 | 🔴 **NONE** | n/a | — | — | `NO_REPOSITORY_FIELD` |
| 🔴 `@ink-waffle/moodle-mcp` 0.2.0 | 🔴 **NONE** | n/a | — | — | `NO_REPOSITORY_FIELD` |
| 🔴 `@n35da/brightspace-mcp` 0.4.0 | 🔴 **NONE** | n/a | — | — | `NO_REPOSITORY_FIELD` |
| 🔴 `@owen-x-tech/canvas-mcp` 1.1.0 | `owentaylor/canvas-mcp` | 🔴 **NO** | — | — | `REPO_UNREADABLE` |
| `canvas-mcp-server` 2.2.3 | `DMontgomery40/mcp-canvas-lms` | 🟢 YES | `jobot.com`(14) | 🔴 **NONE** | 🔴 `UNMAPPED` |
| `moodle-mcp-server-aql` 0.1.7 | `csmediapro/moodle-mcp-server` | 🟢 YES | `csmediapro.com`(114) | 🔴 **NONE** | 🔴 `UNMAPPED` |

🔴 **3 of 6 declare no `repository` field in ANY published version** — 13, 1 and 5 versions
inspected respectively, zero repository pointers among them. Not stale, not private: absent.
🔴 **A fourth declares one that is not publicly readable.** 🔴 **Neither of the two reachable
rows ships a funding file**, and neither email domain carries a country.

🔵 **So `T29` narrows exactly as the falsifier said.** Origin is in the code *when the code
has to reach a named host to work*. It is not in "code generally" and it is certainly not in
repository metadata. `T29` is rewritten to say so on `intel/trends.md`.

## 🔴 Two refusals this probe made on purpose

Both reachable rows have an offset that a careless instrument would book:

* `canvas-mcp-server` — **13 of 16 commits at `-0600`**, 2 at `-0700`. 🔴 `-0600` is
  US/Canada Central **and** Mexico City, Guatemala, Costa Rica, Honduras, El Salvador,
  Nicaragua and Belize. North America and LATAM share it.
* `moodle-mcp-server-aql` — 48 at `+0000` and **9 at `-0400`**. 🔴 `-0400` is US Eastern DST
  and Atlantic Canada **and** Bolivia, Paraguay, Chile and Amazonas.

🔵 **Both are left `UNMAPPED`.** This KB has recorded nine consecutive passes with no
LATAM-owned row and p140 measured that emptiness rather than assuming it. Booking a row
"North America" off an offset that LATAM shares would corrupt the one regional claim this
shelf has earned the right to make — and would do it in the direction of the gap. `jobot.com`
and `csmediapro.com` are organisational signals and are recorded as such; neither is a
country, and this probe does not convert outside knowledge of a company's headquarters into
artefact evidence. That is the `T24` discipline, applied against the convenient answer.

`test_repo_origin.py` pins it: every Americas offset is refused, and **no entry in the
bookable table maps to LATAM at all** — so a future pass that wants to place one has to change
that test first, in the open.

## 🆕 The timezone channel works — on rows that are not the six

Author email domains were the registered instrument and they are nearly empty: 6 of 8
maintainer addresses on the npm shelf are free-mail and the other 2 are vendor `.com`s. So
this probe added one — the **UTC offset each commit records**, written by the author's machine
at commit time, unreviewable by a later reader, and reported only where it is unambiguous
across the five regions.

Run over the agent tier ([`agent-tier.2026-10-12-p141.tsv`](agent-tier.2026-10-12-p141.tsv)),
it places **6 of 7**:

| repository | dominant offset | region | basis |
|---|---|---|---|
| 🟢 `MisterCommand/mcp-canvas-lms` | `+0800` **20 of 20** | 🟢 **APAC** | 🔵 **independently corroborates p140's `canvas.ust.hk` booking** |
| 🆕 🟢 `zijinz456/OpenTutor` | `+1100` 135 of 191 *(+`+1000` ×6)* | 🟢 **APAC** | AEDT — Australia |
| 🆕 🟢 `ahmedEid1/lumen` | `+0200` **828 of 828** | 🟢 **EMEA** | single offset, whole history |
| 🆕 🟢 `mohaneesh-03/mcp-tutor` | `+0530` 5 of 5 | 🟢 **APAC** | India / Sri Lanka only |
| 🆕 🟢 `hesham0-0nasser/tutor-lms-mcp` | `+0300` 7 of 7 | 🟢 **EMEA** | — |
| 🟢 `ArnaudGuiovanna/tutor-mcp` | `+0200` 76 of 459 | 🟢 **EMEA** | 383 at `+0000`, which is no signal |
| 🔴 `nirholas/ai-tutor-mcp` | — | 🔴 `UNMAPPED` | both commits at `+0000` |

🔵 **That asymmetry is the honest shape of the result, and it is the same shape p140 reported
for LATAM: the instrument works and the subjects are out of reach.** The npm connector tier
does not publish a repository; the agent tier does, and every one of its readable rows but one
places. 🔴 **None places in LATAM — a tenth consecutive pass, now measured on two channels.**

## 🆕 🔴 An unasked-for finding: a measurable AI-authorship share

The email histogram surfaced `noreply@anthropic.com` as a committer, which this probe's
`PERSONAL_MAIL` list does not exclude — so it is reported as "institutional" in the TSV.
🔵 **It is a tooling signal, not an origin signal, and reading it as origin would be an error
of the same class this probe refuses elsewhere.** Recorded here rather than silently filtered,
because the measurement is interesting on its own:

| repository | commits authored `Claude <noreply@anthropic.com>` | commits with a `Co-Authored-By: Claude` trailer | of total |
|---|---|---|---|
| `zijinz456/OpenTutor` | 49 | 🔴 **151** | of **191** — 🔴 **79%** |
| `ArnaudGuiovanna/tutor-mcp` | 30 | **51** | of **459** — 11% |

🔵 **This is `T25` upgraded from inference to declaration.** p139 inferred synthetic history
from commits spaced 7 316 seconds apart; here the projects *say so themselves* in their commit
trailers. 🟢 It is not a defect — `tutor-mcp` ships 286 test files against 279 source files and
a database-enforced audit log — but a studio reading commit count as a proxy for human
engineering effort, or for bus factor, now has a number that says not to.

## 🔴 A method warning worth more than the action

`curl -sI https://github.com/<owner>/<repo>` answers **403 for every repository through this
environment's proxy** — live, private or nonexistent alike — because the allowlist covers git
smart-HTTP and the package registries but not github.com HTML. 🔵 **An HTTP status from that
channel carries no information about existence**, and an earlier draft of this pass nearly read
four `403`s as four dead repositories. The only valid probe here is `git ls-remote`, read
against a deliberately nonexistent control. That control runs on every invocation and its
result is printed to stderr.

## Reproduce

```sh
python3 -I repo_origin.py "pkg=owner/repo=/path/to/clone" ...   # empty clone path = unreadable
python3 -I test_repo_origin.py                                  # 14 tests
```
