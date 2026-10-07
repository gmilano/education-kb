---
industry: education
region: Global
updated: 2026-10-07
---

# `p443-canonical-spelling` — pass 25's action C: ask every repository how IT spells its own name

**Executes pass 25's pre-registered action C**, written as:

> Re-run `p439`'s canonical resolution as a **positive** sweep, not a collision gate: ask the
> registry or the self-link for the canonical spelling of all 494 repositories, not only the 9 that
> collided.
> **Prediction:** expect **more than 9** slugs to be spelled differently from their own publisher's
> spelling — a collision needs two spellings *in this KB*, and one wrong spelling used consistently
> is invisible to the gate.

The prediction's reasoning is the point. `p439` fires when the KB contains `X/y` **and** `x/y`. A
repository this KB has only ever miscapitalised **one** way produces no collision and no finding,
while a compiler still keys it under a spelling its publisher does not use.

## 🔴 There is no case oracle on this host, and that was measured on five channels, not assumed

GitHub resolves `owner/repo` case-insensitively, and every channel reachable here inherits that:

| Channel | Wrong case | Verdict |
|---|---|---|
| `raw.githubusercontent.com/{learningequality,LearningEquality,LEARNINGEQUALITY}/…` | 🟢 200 · 200 · 200 | no signal |
| `git ls-remote https://github.com/LEARNINGEQUALITY/KOLIBRI HEAD` | 🟢 resolves | no signal |
| `github.com/<slug>/info/refs?service=git-upload-pack` | 🟢 **200, no `Location` header** | no signal |
| `github.com` rendered (would 301 to the canonical path) | 🔴 **403** | unreachable |
| `codeload.github.com` | 🔴 **403** | unreachable |

🔵 **So the oracle has to be the publisher's own declaration**, which is exactly the order `p439`
wrote — and this sweep now runs it over the whole shelf instead of over nine rows.

## Measured, 2026-10-07, over all 496

| Verdict | n | |
|---|---|---|
| `SPELLING-MATCH` | 296 | every channel that answered agrees with this KB |
| 🔴 `NO-ORACLE` | **186** | neither channel answers. **This KB's spelling is unverifiable from this host for 37.5% of its shelf** |
| `SPELLING-DIFFERS` | **11** | every channel that answered disagrees |
| `CHANNELS-DISAGREE` | 3 | the registry and the self-link contradict each other |

🟢 **Prediction confirmed: 11 differ, or 14 counting the disagreements — more than 9 either way.**

🔴 **And `NO-ORACLE` at 186 is the larger finding.** For more than a third of this shelf there is no
reachable way to check the spelling, so `p439` can only ever gate the 310 with an oracle, and the
rest are unverified assertions. That is a gap, and it is declared rather than papered over.

### The 11

| This KB writes | The publisher writes | Channel |
|---|---|---|
| `NVIDIA/NeMo` | `nvidia/nemo` | PyPI |
| `elisaado/somtoday.js` | `elisaado/SOMtoday.js` | npm |
| `longsightgroup/qti3` | `LongsightGroup/qti3` | `package.json` |
| `microsoft/generative-ai-for-beginners` | `microsoft/Generative-AI-For-Beginners` | README |
| `microsoft/o365-moodle` | `Microsoft/o365-moodle` | README |
| `Kennisnet/phpNLLOM` · `Kennisnet/pylom` · `Kennisnet/py-eduterm-client` | `kennisnet/…` | README |
| `ninocss/UntisPlus` | `ninocss/untisplus` | README |
| `OpenStudy-dev/OpenStudy` | `openstudy-dev/OpenStudy` | README |
| `AI-for-Education/Luganda-linguistic-benchmarks` | `AI-for-Education/luganda-linguistic-benchmarks` | README |

### `CHANNELS-DISAGREE`, which is why a single dissenting channel is not evidence

| Slug | Registry says | Self-link says | Agrees with this KB |
|---|---|---|---|
| `GoogleChrome/lighthouse` | `googlechrome/lighthouse` | `GoogleChrome/lighthouse` | 🟢 the **self-link** |
| `OHF-Voice/piper1-gpl` | `OHF-voice/piper1-gpl` | `OHF-Voice/piper1-gpl` | 🟢 the **self-link** |
| `RohanMuppa/brightspace-mcp-server` | `rohanmuppa/brightspace-mcp-server` | `RohanMuppa/brightspace-mcp-server` | 🟢 the **self-link** |

🔴 **The first build collapsed these three into `SPELLING-DIFFERS` and would have published a
correction on the weaker of two sources.** In all three the registry's URL is the lowercased one and
the repository's own README agrees with this KB.

## 🔴 The action's premise is only partly sound, and that is this instrument's main result

A publisher's declaration is evidence of the spelling **that publisher typed, in that artefact**. It
is not proof of the canonical spelling, because no channel here can serve the canonical spelling at
all. So a disagreement is **real** and still cannot say which side is wrong.

🟢 **The control that makes the measurement readable: each channel CAN carry mixed case.** Among the
`SPELLING-MATCH` rows, **18** came from npm, **23** from PyPI and **95** from a self-link with
*mixed-case* spellings. So a lowercase answer is the publisher's own, not an artefact of the channel
— without this control every `DIFFERS` row would be indistinguishable from a channel that normalises.

⚠️ **Consequence for `p439`:** its resolution order puts *"the package registry's declared homepage"*
first, and it decided **3 of its 9** collisions that way (`kolibri`, `ricecooker` by PyPI homepage).
Those decisions rest on a channel that is **sometimes** lowercased and carries no canonical
authority. 🟢 **The gate's collision DETECTION is unaffected and still sound** — it compares this
KB's own strings — but its canonicalisation for registry-decided rows is a **preference**, not
evidence, and is now recorded as such.

🔵 **Nothing is rewritten on this evidence.** Nine of the 11 rest on a hand-written README, and this
KB does not renumber 11 entities on a capitalisation in prose. The 11 are published as a reading
list with the deciding channel on every row.

## Reservations

- ⚠️ **A self-link is weaker than a registry URL** — a README is hand-written; a registry URL was
  emitted by the publisher's tooling at publish time. The TSV names the channel on every row.
- ⚠️ **`NO-ORACLE` is not evidence of a misspelling.** It is evidence that this host cannot check.
- ⚠️ **The append-only files are out of scope**, as in `p439`: history records the spelling that was
  published, and editing it is the error this KB forbids elsewhere.

## The controls (`test_canonical.py`, 15/15, offline)

The denominator and `normalise` are **imported from `p439`**, not re-derived, so a change to the
reserved-path list or the `.git` rule moves both instruments together — and a control asserts the
live-file list is still exactly the six `p439` gates.

5 positives (plain self-link, case-insensitive match returning the text's case, a shields.io badge, a
codecov badge, a `.git` clone URL); 6 negatives including **the prefix trap** — `owner/repo-two`
must not answer for `owner/repo`, without which a sweep over 495 slugs silently cross-matches
siblings — a link to a genuinely different repository, a site path, a topic page, and an empty
document; and a wrong shelf root exits **2** rather than printing a clean sweep (**P355**).

## Run

```sh
python3 test_canonical.py                              # 15/15, offline
python3 -I canonical.py /home/user/education-kb > result.tsv
```

## Files

- `canonical.py` — the two oracle channels, in `p439`'s priority order, over the whole shelf
- `test_canonical.py` — 15 controls, no network
- `result.2026-10-07.tsv` (496) — **authoritative**
