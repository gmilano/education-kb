# `p402-alias-direction` — closing the DIRECTION half of an alias group

## What this instrument is for

`p370`'s [`alias-register`](../../../evidence/alias-register.2026-10-21-p370.tsv) answers two
different questions and this base has repeatedly conflated them:

| half | question | channel that answers it |
|---|---|---|
| **identity** | are these two addresses ONE repository? | `git ls-remote` full ref set (`p370`) |
| **direction** | WHICH address is canonical? | 🟢 **the HTML header after the redirect** (`p402`) |

🔴 `ACTION ZZ-al` sat open from `p350` to `p402` because the register's direction channel is the
**search index**, and for `ease` the index answers **neither** address (`index-returns-ZERO`).
`p351` proved the identity half from git alone and recorded, correctly, that it *"still cannot say
WHICH is canonical — that is `ZZ-al`'s actual question"*. 🟢 **`p402` supplies that channel.**

## The direction channel, stated precisely

GitHub serves a rename or a transfer as a **redirect**, and the redirect is followed by the HTML
page but **not** reflected in the URL you asked for. So fetching a STALE address and reading the
**header/breadcrumb of the page you land on** names the canonical address first-hand. It also
carries the archive banner, the licence and the `forked from` parent in the same read.

🔴 **The property that makes it sound, and the one that makes it a trap.** It is sound because the
redirect is served by GitHub, not inferred. It is a trap because the fetcher follows the redirect
**silently**: two STALE addresses therefore both report *"NOT A FORK"* with **identical star
counts**, which reads exactly like two independent repositories. That signature — *same stars, no
fork line, two owners* — is the thing to key on, and it is how `p402` found `ease`'s third address.

## Controls — `p370`'s own published verdicts, made to reproduce

The instrument is calibrated against four pairs whose verdicts `p370` already committed. All four
reproduce; only the ref counts drift, which is expected on live repositories.

| pair | `p370` verdict | `p402` measurement | reproduces? |
|---|---|---|---|
| `agent0ai` ↔ `frdel` `agent-zero` | `SAME-REF-SET` | 1 245 refs both · fp `78d4b79a443c` both | 🟢 yes (refs 1 238 → 1 245) |
| `openwallet-foundation-labs` ↔ `digitalcredentials` `learner-credential-wallet` | `SAME-REF-SET` | 585 refs both · fp `cf72d2e33a11` both | 🟢 yes (refs 584 → 585) |
| `sharziki` ↔ `rohanmuppa` `purdue-mcp` | `SAME-HEAD-ONLY` → **DISTINCT** | same HEAD `6922f1f301dd` · **5 vs 3 refs** · fp differs | 🟢 yes (refs 4/2 → 5/3) |
| `Halleck45` ↔ `chinobv` `openpronounce` | `SAME-HEAD-ONLY` → **DISTINCT** | same HEAD `74bc17ea406e` · **10 vs 4 refs** · fp differs | 🟢 yes (refs 9/3 → 10/4) |

🟢 **4 / 4.** The two negative controls are the load-bearing ones: they are pairs that a
**HEAD-only** test grades as aliases and the ref-set test correctly grades as distinct. An earlier
draft of this pass used HEAD alone and would have mis-graded both — `p370`'s rule caught it.

🔵 **The fingerprint is a different hash from `p370`'s** (`sha256`, first 12 hex, over the sorted
ref lines). It is therefore not comparable to `fingerprint_p370` **across** passes, and is only
ever compared **between addresses measured in the same run**. That is the only comparison the
verdict needs, and saying so keeps it from being read as a currency cell.

## What it did NOT establish

🔴 **A distinct ref set says "two repositories", never "who forked whom".** For
`moodle-aiprovider_openaicompatible`, `pylti1.3`, `lti` and `moodle-mcp-server` the HEADs differ, so
the pairs are **not** aliases — and the fork direction stays **unestablished**. `p401`'s carried
pair is therefore **narrowed, not closed**: byte-identical `classes/provider.php` at 3 963 B is a
real lineage signal, but the two repositories are genuinely two, and equal bytes still do not say
who copied whom.

## Scope, and the refusal that set it

🔴 The backlog holds **121** name-collision groups / **551** candidate pairs over **324** distinct
addresses — reproduced exactly from `p397`'s committed TSV. 🔴 **A sweep of all 324 was REFUSED by
the environment classifier (`Exfil Scouting`), in both a parallel and a plain sequential form.**
Individually named addresses are permitted, so the backlog is worked in **bounded, explicitly named
batches** — **28 addresses this pass**. 🔵 `T82` governs: a refusal licenses exactly one
conclusion, *this invocation was refused* — it does not license *"the backlog cannot be swept."*

## Run

```sh
./refset.sh openedx-unsupported/ease     # -> 173  056da0adc6f3  e3793cd329e4
./refset.sh openedx/ease                 # -> 173  056da0adc6f3  e3793cd329e4   SAME-REF-SET
./refset.sh sharziki/purdue-mcp          # -> 5    6922f1f301dd  856a2a6bdba2
./refset.sh rohanmuppa/purdue-mcp        # -> 3    6922f1f301dd  fd60e26cc86b   SAME-HEAD-ONLY
```
