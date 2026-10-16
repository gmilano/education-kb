---
industry: education
region: Global
updated: 2026-10-16
---

# `p244-absence-states` — the four states a probe collapses into *"there is nothing there"*

**Pass 244 · 2026-10-16 · 61/61 controls · every fixture a payload read first-hand this pass**

## Why it exists

`ACTION WC` (p243) asked for a sweep of these shelves for `0`-byte grant payloads, *"carried as
`FOUND` with an unclassifiable body"*.

🔴 **The sweep was run over all `33` carried rows in the two ungranted censuses, and `ACTION WC`'s
premise is false.** Not one carried row is a `0`-byte payload — and the reason is not luck.
`lib/probe_payload.sh::_row_from_fetch` gates on `[ -s "$tmp" ]`, which is **false for a zero-byte
file**, so the ladder walks *past* a `200` and the row lands in the README-dangling-link branch:

```
rine77/meineschule-digital  main  DANGLING-README-LINK:LICENSE  0  DECLARED-NOT-GRANTED  -
```

🔴 **That verdict asserts the file is not there. The file is there, it answers `200`, and it is
empty.** It is also the *same cell* the probe writes for `HAZA-AIOS/HAZA-SMS`, whose README names
`LICENSE` and whose `LICENSE` genuinely `404`s. Two facts, one cell — and **opposite remedies**:

| row | probe says | truth | remedy |
|---|---|---|---|
| `rine77/meineschule-digital` | no file | `200`, **`0` bytes** | upstream **commit** — the maintainer thinks it shipped |
| `HAZA-AIOS/HAZA-SMS` | no file | `404`, genuinely absent | upstream **ask** |

## The class, stated once

p241 named the dual of this on the licence side:

> *every one of these matchers enumerates ways of saying "restricted" and treats the absence of its
> own vocabulary as permission.*

🔵 **`p244`'s class is that sentence with the terms swapped: every one of these PROBES enumerates
ways of finding a thing and treats the absence of its own vocabulary as the absence of the THING.**
Three channels, three independent instances, all measured in this one pass:

| channel | the probe's answer | what was actually true |
|---|---|---|
| **PAYLOAD** | `DECLARED-NOT-GRANTED` *(= no file)* | `200`, `0` bytes — the file exists |
| **ADDRESS** | `UNRESOLVED` *(= no such repo)* | `rc=0`, `0` refs — the repo **exists** and is **empty** |
| **QUERY** | `total_count: 0` *(= axis exhausted)* | the query **shape is void**; the axis has `124` rows |

## What it detects

| verdict | channel | what it means |
|---|---|---|
| `GRANTED` | payload | `200` with bytes — the only state that is a readable grant |
| `EMPTY-DECLARED` | payload | `200` with **`0`** bytes; never a family, and the maintainer believes otherwise |
| `ABSENT-DECLARED` | payload | `404` at a path the README names — a dangling claim |
| `ABSENT-UNDECLARED` | payload | `404` and no claim either |
| `NOT-FOUND-BODY` | payload | the `14`-byte `404: Not Found` body, which a code-blind probe sizes as a grant |
| `LIVE` / `EMPTY-REPO` | address | `rc=0` with refs / `rc=0` with **none** — both EXIST |
| `UNREACHABLE-AUTH` | address | `rc=128` + an auth demand; on github.com that *is* the 404 |
| `VOID-OR-BETWEEN-QUALIFIERS` | query | `OR` between `topic:`-style qualifiers; returns `0`, not an error |
| `TRUNCATED-AFTER-WARRANTY` | text | MIT whose **liability paragraph** is missing |
| `CARVEOUT-NON-HOLDER:<x>` | text | a split-scope note assigning a path to an entity that cannot own it |

### The address channel, measured

```
cdweaver1992/edfi-mcp-server                 rc=0    refs=0   -> EMPTY-REPO        (exists!)
openfresno/edgenuity-aeries-grade-passback   rc=0    refs=0   -> EMPTY-REPO        (exists!)
jakerains/scormplayer                        rc=128  auth     -> UNREACHABLE-AUTH
```

🔴 **Two of the three are live repositories.** They have no commits, so `--symref … HEAD` prints
nothing, so `probe_default_branch` returns empty, so `probe_repo` emits `UNRESOLVED` — which an
existence sweep reads as a dead address. 🟡 `p230` declared `26` dead addresses on these shelves;
any reached by this path is **unconfirmed**.

### The query channel, measured minutes apart in one session

```
topic:deped OR topic:nigeria school management -> total_count 0      <- void shape
topic:deped                                    -> total_count 10
topic:cbse OR topic:ncert school AI            -> total_count 0      <- void shape
topic:cbse                                     -> total_count 124
```

🔴 **`134` rows across the two axes were invisible, and `topic:deped` is the axis that produced BOTH
APAC rows of this pass.** 🟢 `zero_result_is_absence()` is the gate: a `0` may not be published as
*"there is no X on this axis"* until the shape is checked.

### The duals: a payload read *completely* that is not complete

🟢 **`belentani7/aprende-brasil`** — `814` B, `7d9e6170085b`. Grant verb present, warranty disclaimer
present, **liability paragraph absent** (the text stops at `NONINFRINGEMENT.`). `family_of` answers
`MIT`, correctly, and says nothing about it. This is `p243`'s `webuntis-ha` defect (`797` B, cut off
mid-paragraph) for the **second** time, on another continent. The grant is intact, so the row is
usable; what is missing is the clause that protects **the author**.

🟢 **`Lukas1120987/Schul-System`** — `1 324` B, `LICENSE.md`, `9c208c271ef2`. A complete canonical
MIT, then an `# Anmerkung:`

> *"Alle Bilder in dem Ordner `/icons` sind KI generiert und gelten daher **nicht unter dem
> Urheberrecht von Lukas1120987**. Das Urheberrecht der Bilder liegt bei **Chat-GPT von OpenAI**."*

🔴 **The author disclaims the asset path and assigns it to an entity that cannot hold a copyright
and does not claim one, so `/icons` has no identifiable rights holder.** The carve-out subtracts a
scope without granting it to anybody. 🔵 Not one of `p1054` (added restrictions),
`p242-grant-delta` (additions to a canonical text) or `p1058.grant_qualifier` (a restriction before
the grant verb) asks this, because all three read the **software** grant — which here is clean.
🟢 Contrast `T243-E`'s `oga-veve`: three scopes, each with a real grant and a real holder.

## Scope — what it deliberately does not do

⚠️ This instrument answers **"what did the probe actually learn?"**. It does **not** re-ask the
family question; `lib/license_family.sh` owns that and is not reimplemented here (`P237`, `P171`).
Two controls assert that: `family_of` is never defined in this module and no family classifier is
imported. 🟢 `test_gpl3`-style loopbacks are therefore unnecessary — the token window is never read.

## Invocation

🟢 Runs **both** ways, which is itself a control — `p241` found `p1058`'s suite died under
`python3 -I` (the invocation its own docstring prescribed) and that a working gate consequently
stayed a one-off for `53` passes. This file fixes its own `sys.path` rather than asking the
Makefile to `cd` for it.

```
python3 -I compose/code/p244-absence-states/test_absence_states.py   # from the repo root
cd compose/code/p244-absence-states && python3 test_absence_states.py
```

Wired into `make hooks`.
