---
industry: education
region: Global
updated: 2026-10-20
---

# `p348-fold-identity` — fold the slug before comparing it, and over the RIGHT denominator

Discharges `ACTION ZZ-x`, both halves, and the discharge found a defect in the
measurement that motivated it.

## 🔴 The denominator was the finding

p347 ran the HEAD-equality test and declared it done *"over EVERY address on these
shelves"*: **257 distinct addresses extracted from the five LIVE shelf files.**
Re-harvested over all **nine** published shelves:

| set | distinct addresses |
|---|---|
| p347's declared set (5 live shelf files) | **440** casings |
| appearing ONLY on `agents/trending.md` + `repos/trending.md` | **2 091** casings |
| the COMPLETE shelf set | **2 531** casings / **2 462** folded |

**So the shelf-wide run covered 440 of 2 531 = 17.4 %**, and its verdict column reads
*"unique HEAD across the shelf set"* — a true statement about the set it measured and a
false one about the shelves. The two excluded files hold **74 076 of 122 217** shelf
lines. They were excluded because they are append-only HISTORY; **the addresses on them
are the addresses a reader copies.**

The specimen proves it:

```
digitalcredentials/learner-credential-wallet          HEAD 1c46a82ba384  on agents/trending.md
openwallet-foundation-labs/learner-credential-wallet  HEAD 1c46a82ba384  in p347's set,
                                                                        graded "unique HEAD"
```

ONE repository, published twice, under owners sharing no characters — the MIT Digital
Credentials Consortium having moved the project to the OpenWallet Foundation. **A case
fold is blind to it; only HEAD equality sees it.**

## Three identity classes, and this base had one instrument in `hooks`

| class | example | folding | HEAD equality | payload digest |
|---|---|---|---|---|
| same address, different CASE | `CAHLR/OATutor` / `cahlr/OATutor` | 🟢 | 🟢 | 🟢 |
| different OWNER, one repository | `digitalcredentials/…` / `openwallet-foundation-labs/…` | 🔴 | 🟢 | 🟢 |
| different repository, IDENTICAL payload | `anthropics/k12-teacher-skills` / `learning-commons-org/agent-skills`, `SKILL.md` sha256 `152e3272fbd108fe` | 🔴 | 🔴 | 🟢 |

The third class has no instrument here: `ACTION ZZ-ad`.

## 🟢 Folding is wired as a gate because its precision was MEASURED

All **65** folded-collision groups on the complete set (the `OWNER/REPO` command template
dropped) were resolved first-hand with `git ls-remote --symref`. **64 answered and all 64
are SAME-HEAD** — one repository under two or three casings. **Zero different-HEAD
groups**, so folding produced no false positive anywhere on this corpus. One group
answers under neither casing (`gegok12/gegok12`). Two of the 65 were already reported by
p347; **63 are new, and 63 were invisible to `gate-identity`.**

## The contract, and why it is forward-looking

An append-only shelf cannot be repaired backwards — p347 established that the only move
which ever clears an inherited finding is to satisfy the contract **by construction** in
the successor's own text. A gate failing on all 65 historical collisions would be
permanently red and would teach nothing. So this gate judges the **live pass section**,
exactly as `gate-absence` does:

```
P348-NEW-CASING   the current pass section publishes an address whose fold already
                  exists on these shelves under a DIFFERENT casing.
```

Citing the casing already published passes. A genuinely new address passes — **the gate
blocks a second spelling of held supply, never supply.** The 65 inherited groups are a
census: a backlog with a denominator, never a failure, which is the `p308`
`shelf-census` / `gate-shelf-consistency` split applied to the identity axis.

## Usage

```sh
make gate-fold-identity   # 21 controls + P348-NEW-CASING over the nine shelves
make fold-census          # the inherited backlog, with its denominator
make hooks-online         # ZZ-x's second half: gate-identity-online, finally in a target
```
