# `p782` — the policy gate (`Gap 278`'s remedy)

**Declared** pass 58 · **written as prose** passes 59–60 · **written as an instrument** pass 61.

## The defect it closes

🔴 **`P764`:** [`algorithm0r/canvas-lms-mcp`](https://github.com/algorithm0r/canvas-lms-mcp) is
**MIT** and exposes grading, comments and rubrics. It clears **every licence check this KB has
ever written**, and the *function* it exposes is gated or prohibited in several jurisdictions
regardless of its licence. 🟢 **A licence gate and a policy gate are different gates**, and
until this pass the shelf only had the first.

🔴 **Why prose was not enough.** Passes 59 and 60 wrote the two-axis pre-flight into
`compose/patterns.md`. 🟢 It was correct; 🔴 it was also unreadable by an instrument and
covered four regions "at the level of a sentence each" — pass 60's own words. `Gap 278`
asked for *a table as data, with the instrument that reads it*. This is that.

## Usage

```sh
bash gate.sh assessment_grading            # strictest verdict across all jurisdictions
bash gate.sh assessment_grading EMEA       # scoped to a region …
bash gate.sh emotion_recognition EU        # … or to a jurisdiction
bash gate.sh --region LATAM                # everything measured for one region
bash gate.sh --functions                   # the closed function vocabulary
bash test_gate.sh                          # 21 assertions, offline
```

Exit status **is** the verdict: `0` clear · `3` GATED · `4` PROHIBITED · `5` PROPOSED ·
`6` **no row** · `2` fatal (bad region).

## Three properties worth more than the table

🟢 **1. `6` is not `0`.** An unmeasured `(function, jurisdiction)` pair exits **6**, never
`0`. `P476`: silence is not permission. Four assertions pin this, because it is the single
most expensive way to misread the file.

🟢 **2. The strictest row wins.** An unscoped query returns the harshest verdict present,
not the friendliest — a deployment ships to the jurisdictions it ships to.

🟢 **3. The region vocabulary is closed and fails loudly.** `--region Latam` exits **2**
with a message, rather than returning an empty set that reads exactly like *"nothing is
regulated there"*. `Europe`, `Brazil` and `Latam` are each asserted to fail.

## 🔴 The band, which is the honest part

🟡 **Every row is `reported`. None is payload-read, and none can be.** Measured pass 61:
**12 of 12** primary policy hosts answer `000` to `curl` — *and so do `example.com`,
`google.com` and `wikipedia`*, while `raw.githubusercontent.com`, `pypi` and `npm` answer
`200`. The proxy names the mechanism: **`connect_rejected`, "gateway answered 403 to
CONNECT"**. `WebFetch` against the same hosts returns **`EGRESS_BLOCKED`**.

🟢 **So this session has exactly ONE regulatory channel** — a search backend's server-side
fetch — **and zero direct-fetch channels.** 🔴 **A second *independent* oracle for any
policy row is therefore unobtainable here**, so a `verified` band on a policy row in this KB
would be a **defect**. 🔵 That is a property of the channel, not a limit of the research —
and it is why `Gap 270` is **re-posed** rather than closed.
