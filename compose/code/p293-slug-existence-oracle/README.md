# `ACTION p293` — the slug-existence oracle, calibrated

**What it answers:** *is this guessed `owner/name` a repository?* — with the channel's own refusal
signature **measured against controls** rather than assumed.

```
make gate-slug-oracle                      # 45 offline controls, in `make hooks`
python3 -I compose/code/p293-slug-existence-oracle/slug_oracle.py --online \
    tokenaii/Horus-Taleeq-0.2B-Base tokenaii/Horus \
    --out evidence/p293-slug-oracle.$(date +%F).tsv
```

## 🔴 Why it exists: `p292` had the measurement and read it as noise

`p292` probed four guessed `tokenaii/*` slugs with `git ls-remote`, got an anonymous credential
prompt on all four, and wrote the result down as *"**INCONCLUSIVE** and not a negative"*. Measured
against controls in the same session, that verdict is wrong:

| probe | rc | answer |
|---|---|---|
| `moodle/moodle` *(known real)* | `0` | **1 959 ref lines** |
| `tokenaii/Horus-Taleeq-0.2B-Base` *(known real)* | `0` | **2 ref lines** |
| `openedx/this-repo-does-not-exist-zzz9` *(known fake)* | `128` | `fatal: Authentication failed` |
| `thisorgdoesnotexistzzz9/thisrepo` *(known fake owner)* | `128` | `fatal: Authentication failed` |
| `nonexistent-host-zzz9.example.com/a/b` *(dead host)* | `128` | `fatal: unable to access` |

🟢 **The credential prompt discriminates.** It is the channel's answer for *"no repository I will
serve you"*, and it is a **different string** from its answer for *"I could not reach the host"*.
🔴 So three of `p292`'s four probes were real negatives discarded as noise — and the fourth
mattered least, because **no source had named the right path**, which a search leg produced in its
first result the moment one was aimed at the path instead of the licence.

## 🔴 The bound, which is why the token is not `ABSENT`

The same prompt answers for a repository that exists and is **private**. Nothing in this channel
separates those two cases, so the verdict token is **`ABSENT-OR-PRIVATE`** and control `C9`
asserts that a bare `ABSENT` **is not in the vocabulary at all**.

🔵 `p292`'s error was reading a discriminating signal as noise. The opposite error — reading it as
proof of non-existence — is the one this bound refuses, and it is the more expensive of the two in
a client deliverable.

## 🔴 And why it calibrates itself

The signature is a property of **this session's git proxy**, not of git and not of github.com. A
channel that changed its refusal wording would silently turn every `ABSENT-OR-PRIVATE` into a
`CHANNEL-ERROR` — or worse, the reverse. `--online` therefore runs the control pair **first** and
**reports no verdict at all** unless the known-real probe returns refs and the known-fake probe
returns the refusal:

```
🔴 CALIBRATION FAILED — the channel no longer answers as this oracle was built
   against, so NO verdict is reported.
```

🔵 An uncalibrated read of this channel is precisely what produced `p292`'s row, so refusing to
report is the feature.

## The closed vocabulary

| verdict | when |
|---|---|
| `EXISTS-PUBLIC` | `rc=0` and at least one ref line |
| `EXISTS-NO-REFS` | `rc=0` and no ref line — an **empty** repository, which exists |
| `ABSENT-OR-PRIVATE` | the refusal signature. 🔴 **The two are not separable here** |
| `CHANNEL-ERROR` | transport, host, timeout, proxy cap, or any **unrecognised** non-zero message |
| `MALFORMED` | no output, or no returncode to read it against |

🔵 **Transport is checked before the refusal**, because a proxy error can carry the word
*authentication* in an unrelated clause and transport is the weaker claim (`C14`). 🔵 An
unrecognised non-zero message is `CHANNEL-ERROR`, **never** a negative (`C15`).

🔵 **The returncode is load-bearing**, not decoration: without it, an empty answer from a
reachable-but-empty repository cannot be told from a transport failure that printed nothing, and
the oracle would have to guess. It returns `MALFORMED` and says which two outcomes it cannot
separate (`C8`, `C8b`).

## What it does NOT claim

- 🔴 `EXISTS-PUBLIC` is **not a licence claim** (`C35`) — read the grant at the pin, with
  `p228`'s classifier.
- 🔴 It is **not a freshness claim** (`C36`) — no date is parsed and none reaches the detail.
- 🟡 A **HEAD collision is a finding, not a verdict** (`p283`'s rule): two names sharing a HEAD are
  one tree under two names, *or* one forked from the other today. It is reported and adjudicated,
  never auto-merged.

## The fixtures are recorded, not invented

Every payload in the suite is **verbatim from the five live probes** run at `p293` on
`2026-10-18`. 🔴 `p292`'s `C28h` pinned a defect as desired behaviour because it was written from
the gate's *intent* rather than from a real sentence; a fixture invented from what the channel
*should* say would calibrate this oracle against its author's imagination instead of the channel.

🔴 **Two controls in this suite's own first draft were defective, both found by running it:**
`C5` asserted *three* ref lines in a fixture that has two (the symref line is not a ref line), and
`C36` was written as `... or True`, **which cannot fail** — `C28h`'s trap, one pass later. Both
are repaired, and `C5b` now pins the symref-is-not-a-ref distinction that `C5` got wrong.
