---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-duplicate-lineage` — `ACTION CN`: git settles it, and the same instrument settles a second pair for free

**Executes p138's pre-registered `ACTION CN`**, written as:

> Resolve the `moodler-mcp` duplicate by a channel that is not the manifest: commit history,
> release dates, or a fork marker. 🔴 *Refuted if neither address is derivable as the
> original, in which case this KB carries both and says so.*

## Verdict: **DISCHARGED, NOT REFUTED — `GhaithAlHallak8/moodler-mcp` is the original**

| field | `GhaithAlHallak8/moodler-mcp` | `Dymayo/moodler-mcp` |
|---|---|---|
| commits | 75 | 75 |
| HEAD | `4e6139e` (2026-09-19) | `4e6139e` (2026-09-19) |
| root commit | `f3da2b7` | `f3da2b7` — **same** |
| 🟢 **shared commit shas** | 🟢 **75** | 🟢 **75** |
| unique commits | 0 | 0 |
| 🟢 **remote refs** (`ls-remote`) | 🟢 **17** | 🔴 **2** |
| account in author addresses | 🟢 **`59054736+GhaithAlHallak8`** | 🟢 **`59054736+GhaithAlHallak8`** |

🔵 **Three non-manifest signals, all pointing one way:**

1. 🟢 **One history, not two.** All **75** commit shas match, in order, including the root
   commit `f3da2b7`. A sha hashes content, parents, author and timestamp together, so a shared
   sha cannot be coincidence — this is a fork or mirror, **not** a re-authoring.
   🔵 **This is the opposite of p136's `ACTION BW` result**, where the ENEM repositories had an
   identical root *tree* and **zero** shared commits. Those two cases are indistinguishable in a
   file listing and are opposites in provenance; only the sha comparison separates them.
2. 🟢 **17 refs against 2.** `GhaithAlHallak8` carries the branches and release tags; `Dymayo`
   carries essentially the default branch. Release history accumulates where the releases are cut.
3. 🟢 **The committing account is in the history.** Every GitHub-side commit is authored by
   `59054736+GhaithAlHallak8@users.noreply.github.com` — the noreply form embeds the account's
   **numeric id (59054736)** and **login**. `Dymayo` appears nowhere in either history.
   🔵 **This is the strongest of the three, because it is an account identity rather than a
   convention**, and it is present inside the object store rather than asserted by a file.

🟢 **p138's manifest-based call was right.** It is now corroborated by a channel independent of
the thing being checked, which is what the action asked for.

## `P139-E2` — the instrument immediately earned its keep on a pair p138 never saw

The same two-search sweep that fed `agents/top.md` this pass turned up **`ArnaudGuiovanna/tutor-mcp`
and `kvnloo/tutor-mcp` carrying a byte-identical description** — *"An open-source MCP server that
turns any LLM into an Intelligent Tutoring System. 50 years of cognitive science, MIT licensed."*
The same shape as `moodler-mcp`, found the same way, and resolved in one command:

| field | `ArnaudGuiovanna/tutor-mcp` | `kvnloo/tutor-mcp` |
|---|---|---|
| commits | **459** | 452 |
| HEAD | `368d637` (**2026-10-10**) | `3d11705` (2026-10-02) |
| root commit | `baea09f` | `baea09f` — **same** |
| head tree | `373d3fab…` | `675a9a9e…` — **differs** |
| shared commits | **452** | **452** |
| 🔵 **unique commits** | 🔵 **7** | 🔵 **0** |
| remote refs | 16 | 14 |

🟢 **Verdict: `kvnloo/tutor-mcp` is a fork 7 commits behind `ArnaudGuiovanna/tutor-mcp`.** Every
commit of the fork is in the trunk and none of the trunk's last 7 are in the fork; the root
commit is Arnaud Guiovanna's. 🔵 **Unlike the `moodler-mcp` pair, this one is decidable on
ancestry alone** — the ref count and the account id merely agree. Only `ArnaudGuiovanna/tutor-mcp`
is carried on `agents/top.md`; the fork is recorded here and not promoted.

🟡 **An incidental observation on the trunk**: 30 of its 459 commits are authored by `Claude`.
An MCP tutoring server substantially written by an agent is a 2026-shaped provenance fact; it is
noted, not graded.

## `P139-E3` — 🔴 the `moodler-mcp` history is partly synthetic, and that is worth recording

While reading the history for lineage, a pattern appeared that nobody asked about. The first
~20 commits are spaced at **7 316–7 317 seconds** — two hours, one minute, fifty-six seconds —
**apart, every time**, all at `+04:00`, starting at exactly `09:00:00`:

```
f3da2b7  2026-04-08T09:00:00+04:00  init moodler
deb7471  2026-04-08T11:01:56+04:00  feat: enhance file content headers …
be181bd  2026-04-08T13:03:53+04:00  fix: remove default Moodle URL prev …
7af1bcb  2026-04-08T15:05:50+04:00  feat(config): add CACHE_DB and CACHE_DISABLED …
```

🔴 **Human work does not land on a 7 316-second metronome.** The opening stretch of this history
was generated or back-dated, with conventional-commit messages attached. The later history is
organic — 13 `dependabot[bot]` commits, 10 `github-actions[bot]` commits, a release-please
`chore(main): release 1.1.2 (#44)` — so the repository became real after it was staged.

🔵 **The consequence is narrow and specific: commit count and commit dates are not evidence of
elapsed development effort on this row.** The grant, the code and the releases are all genuine.
This is a caution about using history depth as a maturity signal, which is a thing this KB's
`p110-bus-factor` and `p109-freshness` instruments do.

## 🔴 `ACTION CO` could not be discharged, and this pass can finally say why

`ACTION CO` asked for **one of the five MEA instruments read in primary source**, naming SDAIA's
framework as the most likely to be fetchable. 🔴 **It is not fetchable here, and neither is any
other government or legal primary source tried this pass:**

| target | result |
|---|---|
| `sdaia.gov.sa` (AI Adoption Framework PDF) | 🔴 **proxy gateway answered `403` to `CONNECT`** |
| `eur-lex.europa.eu` (Regulation (EU) 2026/1744) | 🔴 **`403` to `CONNECT`** |
| `digital-strategy.ec.europa.eu` | 🔴 **`403` to `CONNECT`** |
| *(p138)* `congbao.chinhphu.vn` | 🔴 `ENOTFOUND` |

🔵 **This is a diagnosis, not another complaint.** `curl -sS "$HTTPS_PROXY/__agentproxy/status"`
lists the refusals explicitly as `connect_rejected — gateway answered 403 to CONNECT (policy
denial or upstream failure)`. p138 recorded the symptom as a DNS failure and said "primary
source, secondary transport, third pass running". The cause is the **environment's network
policy**, which permits package registries and `github.com` and refuses government hosts.
🔴 **No amount of retrying will fix it, and the next pass should not spend a probe on it** —
what it should spend is a request to widen the policy, which is a decision outside this KB.

🟡 **On the substance, the premise is nonetheless not met, by secondary evidence.** The
refutation condition was *"refuted if none mentions education at all"*, and SDAIA publishes an
instrument whose entire subject is education: the **Saudi Academic Framework for AI
Qualifications**, a reference for designing, evaluating and **accrediting AI higher-education
programmes**, mapped to the **8-level National Qualifications Framework** — plus a **Data and AI
Academic Program Standards Framework** developed with the **Education and Training Evaluation
Commission (ETEC)**, setting minimum learning outcomes per qualification level.
🔴 **Both are cited from search results, one of which labels the document a "Project Draft", and
neither was read.** So `P138-J` stays a **region gap** rather than becoming a region absence —
but it is not upgraded to a measured finding either, and nothing here is quotable to a client.

## Files

| file | role |
|---|---|
| `lineage.sh` | the instrument: blobless clones, sha-set comparison, ancestry, ref count, noreply account ids |
| `result.2026-10-12-p139.tsv` | both pairs, as published above |

### Reproduce

```sh
./lineage.sh GhaithAlHallak8/moodler-mcp Dymayo/moodler-mcp
./lineage.sh ArnaudGuiovanna/tutor-mcp kvnloo/tutor-mcp
```

## 🔴 What this probe does NOT establish

- 🔴 **`fork: true` was never read.** `api.github.com` answers **403** here, so GitHub's own fork
  marker — the one authoritative field — is unavailable. The verdict rests on three proxies for
  it. For the `moodler-mcp` pair, where histories are *identical*, those proxies are **ref count
  and account identity only**; ancestry cannot separate them.
- 🟡 **A mirror maintained by its own owner would look like `Dymayo`.** Nothing here shows intent:
  "fork", "mirror" and "copy" are not distinguished, and no claim is made that the copy is
  improper.
- 🔴 **Neither pair's CODE was compared this pass.** p138 established byte-identity for
  `moodler-mcp` from READMEs; the `tutor-mcp` pair's head trees **differ**, as they must at 7
  commits apart, and what those 7 commits change was not read.
- 🔴 **`Dymayo/moodler-mcp` has no payload layer** — p138 recorded it as **not on PyPI (404)** —
  so the registry channel that answered `ACTION CD` and `ACTION CM` cannot speak to this row.
- 🔴 **No region measured for either pair.** The `+04:00` timestamps and the author name on
  `moodler-mcp` suggest the Gulf, which would place it in **EMEA**; that is an inference from a
  timezone and a name and is **not booked**. The LATAM-ownership gap is at **nine consecutive
  passes**.
