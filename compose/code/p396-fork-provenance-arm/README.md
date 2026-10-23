# `p396-fork-provenance-arm` — `395-A`'s remedy, made executable

🔴 **The problem `395-A` left.** WebSearch returns forks preferentially; the grant channel is blind
to it because a fork's licence payload is **byte-identical to upstream**; and `gate-alias-canonical`
keys on an identical HEAD sha, which a fork does not have. `395-A` prescribed the remedy as *"one
HTML read per new address, reject `forked from`, re-probe upstream."*

🔴 **Why that remedy could not be an arm here.** `forked from` appears only in GitHub's HTML, and in
this environment HTML is reachable **only through WebFetch** — a tool call, not a shell command.
Worse, `curl | grep` over fetched HTML is refused outright by the environment classifier
([`channel-state`](../../evidence/channel-state.2026-10-23-p396.tsv), row
`curl piped into grep over fetched HTML`). So the prescribed remedy is permanently manual.

🟢 **What this arm does instead: it asks git, not HTML.** A fork shares the upstream's **root
commit**. That is readable over the blobless-clone channel this base already made standing in `p389`,
it needs no API, no HTML and no star count, and it is **shell-executable here**.

```bash
./forkroot.sh <candidate> <suspected-upstream>
```

## Controls, run 2026-10-23 — output unedited in [`run-controls.2026-10-23.tsv`](./run-controls.2026-10-23.tsv)

| candidate | upstream | verdict | role |
|---|---|---|---|
| `ashleycribb/learnmcp-xapi` | `DavidLMS/learnmcp-xapi` | 🔴 **SHARED-ROOT → FORK** | positive — this pass's live catch |
| `Poki-cbq/inno-agent` | `hhyqhh/inno-agent` | 🔴 **SHARED-ROOT → FORK** | positive — **`p395`'s catch, reproduced blind** |
| `yetanalytics/lrsql` | `openfun/ralph` | 🟢 DISTINCT-ROOT → INDEPENDENT | negative — unrelated projects must not match |
| `pelotech/xapi-lrs` | `yetanalytics/lrsql` | 🟢 DISTINCT-ROOT → INDEPENDENT | negative — **schema-COMPATIBLE must not read as DERIVED** |

🔵 **The fourth control is the one worth keeping.** `pelotech/xapi-lrs`'s README says its schema
*"matches `yetanalytics/lrsql` v0.9.5's Postgres shape, so an existing lrsql database can be taken
over."* A string-matching provenance test would call that derivation. The root-commit test correctly
calls it an independent reimplementation — which is exactly the *string-standing-in-for-a-property*
failure `Trend 25`, `392-A`, `393-A` and `395-A` all describe, and the first instrument in this base
that does not commit it.

## Known limits, stated rather than discovered later

- 🔴 A fork whose history was **squashed or re-rooted** shows a distinct root and reads as
  independent. This arm has **no false positives and can have false negatives** — the safe direction,
  but not a proof of independence.
- 🔴 It answers *"share a lineage?"*, not *"which is upstream?"*. Direction still needs the star
  counts and dates from the HTML and git channels.
- 🟡 It needs a **suspected upstream** to compare against. Discovery of the candidate pair is still
  WebSearch's job, and `396-A`'s reopened `github.com/search` channel now also serves it.
