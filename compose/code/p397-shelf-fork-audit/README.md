# `p397-shelf-fork-audit` — `396-F`'s arm, at shelf scale, with the label corrected

## What `p396` left, and why it stalled

`396-F` built a **root-commit fork arm** and `p396` ranked running it over the existing shelf
**first**: *"200+ addresses have been shelved without any provenance test at all."* It also stated
the blocker plainly — *"it needs a suspected upstream to compare against — discovery of the pair is
still WebSearch's job."* That is what kept it to new addresses: a shelf-wide run needs **551 pairs**,
and WebSearch cannot hand over 551 pairs.

## 1. `candidates.py` — derive the pairs from the shelves, with no network at all

Two shelf addresses that share a repository **name** under different **owners** are a fork
candidate. Over the nine `SHELF_FILES`:

| cifra | valor |
|---|---|
| harvested_folded | 2 694 |
| rejected_non_addresses | 34 |
| **shelf_addresses** | **2 660** |
| distinct_repo_names | 2 457 |
| **name_collision_groups** | **121** |
| **candidate_pairs** | **551** |

🟢 The denominator is **p351's**, imported rather than re-implemented (control `C5`), so it agrees
with the published channel-U census to the address. 🔵 It is channel **U** — p351 harvests URLs;
backticked bare slugs are channel **B** (`p367`), a different instrument. Stated because `p397`'s own
first fixtures were bare slugs, harvested nothing, and looked like a clean tree.

## 2. `lineage.sh` — and the label `396-F` got wrong

`396-F` returns **`SHARED-ROOT -> FORK LINEAGE`**. 🔴 **That is a string matched to a property, the
exact `Trend 25` error the arm was built to fix.** A shared root commit is shared **ancestry**, which
is equally implied by a true fork, an organisation **rename**, a repository **transfer** and a
re-push. `p397`'s shelf run settled it empirically: **8 of 15 shared-root pairs were not forks at
all** — they were one artefact answering at two addresses.

The discriminator is one extra field off the same clone, and needs no HTML:

| root | HEAD | verdict | meaning |
|---|---|---|---|
| shared | **same** | `SAME-REPO-ALIAS` | 🔴 ONE artefact, TWO shelf addresses — a census duplicate |
| shared | **different** | `DIVERGENT-FORK` | two artefacts, one ancestry — a real choice to adjudicate |
| distinct | — | `INDEPENDENT` | same name, unrelated code |
| unresolvable | — | `INCONCLUSIVE-UNRESOLVABLE` | 🔵 never called INDEPENDENT from a failed read |

That last row is deliberate: calling an unresolvable side *independent* would publish a distinctness
claim out of a failed read, which is `p393`'s false-`UNGRANTED` class wearing a different hat.

## 3. What the live run found

21 pairs tested, prioritised by consequence, with `p395`'s catch reproduced blind as a positive
control and two dead addresses as a negative one. Unedited output:
[`../../../evidence/shelf-lineage.2026-10-23-p397.tsv`](../../../evidence/shelf-lineage.2026-10-23-p397.tsv).

- 🔴 **8 `SAME-REPO-ALIAS`** — `1EdTech`/`IMSGlobal` ×3 (the standards-body rename), `edx`/`openedx`
  `ease`, `pytorch`/`meta-pytorch` `opacus`, `kantord`/`LibreLingo`,
  `digitalcredentials`/`openwallet-foundation-labs` `learner-credential-wallet`, and
  `agent0ai`/`frdel` `agent-zero` (already in the alias register — so the arm **agrees with a
  register built by a different method**, which is the control that matters).
- 🟢 **7 `DIVERGENT-FORK`** — including `DavidLMS`↔`ashleycribb` `learnmcp-xapi` (`p396`'s catch,
  reproduced), `dmitry-viskov`↔`ucfopen` `pylti1.3`, and `EleutherAI`↔`latam-gpt`
  `lm-evaluation-harness`.
- 🟢 **4 `INDEPENDENT`** — same name, distinct roots: `OpenLRS`, `qti-convert`, `ims-lti`, `lrs`.
  🔵 The discrimination is real, not an artefact of the method.
- 🔴 **1 dead address surfaced**: `apereo/opencast` **404s** on both the clone and the WebFetch
  channel. The live canonical is `opencast/opencast` (HEAD 0 d, branch `develop`).

## Stated limits

🔴 A **squashed or re-rooted** fork reads as `INDEPENDENT` — no false positives, possible false
negatives (inherited from `396-F`). 🔴 `SAME-REPO-ALIAS` does not say **which** address is canonical;
direction still needs the register (`p349`'s rule: a gate never decides canonicality at run time).
🔴 **551 pairs are derived and 21 are adjudicated.** The remaining 530 are a backlog with a
denominator, not a clean result.

## Running it

```
make shelf-fork-candidates          # the 551 pairs, offline
make gate-shelf-fork                # 11 controls, offline
bash lineage.sh OWNER_A/REPO OWNER_B/REPO   # one pair, needs the clone channel
```
