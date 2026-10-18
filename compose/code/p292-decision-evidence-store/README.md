# `ACTION p292` — the append-only decision evidence store

**The component `P45`-`P48` terminate in, built.** `p291` ranked it item 1: *"load-bearing for
four recipes, no network needed, the one item a client would pay for."* It had been deferred
for four passes.

```
python3 test_decision_store.py                    # 106 controls, offline
python3 worked_example.py --out /tmp/demo.jsonl   # 4 surfaces, 8 records, 2 refusals
python3 -I decision_store.py --verify /tmp/demo.jsonl
python3 -I decision_store.py --head   /tmp/demo.jsonl
python3 -I decision_store.py --root ../../..      # the shelf arm
```

Committed run: [`evidence/decision-store-worked.2026-10-18-p292.jsonl`](../../../evidence/decision-store-worked.2026-10-18-p292.jsonl).

## 🔴 The correction this instrument made to its own backlog entry

`p290` wrote *"three recipes … and one evidence store"*; `p291` wrote *"now **four** recipes, one
build"*. Measured against the shelves, **two** recipes terminate in the decision record:

| recipe | what it says it needs | is it this component? |
|---|---|---|
| `P45` admissions | *"the evidence store — you build it"*; *"the append-only decision record"* | 🟢 **yes** |
| `P48` vocational | *"Terminate in the evidence store — the same append-only record"* | 🟢 **yes** |
| `P46` retention | *"the **intervention log** — date, method, response, outcome"* | 🔴 **adjacent** — an outcome log over time, not a decision record |
| `P47` grading | *"a built **deadline-and-evidence** layer"*, *"statutory, calendar-bound"* | 🔴 **adjacent** — a calendar, not a decision record |

🔵 **Why this mattered rather than being a wording quibble.** "One build" sounds like one
thing, so it was costed as one thing and never started. The honest shape is **one substrate,
four schemas**: all four surfaces write into the same chain, each with its own closed act
vocabulary (`SURFACES`), and `P46` and `P47` each additionally need a component this store does
**not** supply. 🟢 That is also why it was buildable in one pass once stated correctly.

🔴 `S2` makes the overclaim standing: no line mentioning the store may assert more
store-bearing recipes than the shelves carry. It fails `p291`'s own sentence.

## What each refusal answers

| control | the refusal | why it is a control and not a schema nicety |
|---|---|---|
| `R1` | the decider must be a **natural person** (`kind == "human"`) | `P45` says *"the prompt is not a control"*. This is where that becomes one: an agent, a service account or an unattributed actor **cannot be written** into the slot an auditor reads as "a human decided" |
| `R2` | **no decision without what was shown**, bound by sha256 over canonical bytes | An oversight record that cannot reproduce the observations the human read answers nothing. `R2c` catches a payload edited after the fact |
| `R3` | the **rubric version in force** is required | *"Apply the rubric consistently"* is auditable only against the rubric in force at decision time |
| `R4` | the operative act comes from a **closed vocabulary per surface** | So *"scored"* can never be recorded in the slot that means *"decided"*. A decision valid on another surface is still refused on this one |
| `R5` | concurrence with the agent is **recorded, never refused** | See below — this is the one place where the obvious control is the wrong one |
| `R6` | **append-only** by hash chain; `verify()` walks it | Catches edit-in-place, deletion and reorder |
| `R7` | monotonic `seq`, unique `decision_id` | A replayed id would let two decisions share one audit trail |
| `R8` | `decided_at` is RFC3339 **UTC**; the chain's clock may not run backwards | One clock or no comparison |
| `R9` | `subject_ref` must be **pseudonymous** | This is the record retained longest. The detector is deliberately narrow — e-mail and national-ID digit runs — because a broad PII classifier that is wrong gets switched off |
| `R10` | a `distress_flag` requires a **named human recipient** | `P45` step 5: *"route it to a named human, not to a queue"* |

### 🟢 `R5`, and why refusing agreement would have been the wrong control

The tempting control is to reject a decision identical to the agent's recommendation as a
rubber stamp. That is wrong twice over: a human who agrees with a correct recommendation **has
still decided**, and a store that rejects agreement teaches its users to stop recording the
recommendation — destroying the only evidence the question can be answered from. So
concurrence is **derived, sealed into the digest, and never refused**, and
`concurrence_rate()` returns `(concurred, comparable, rate)`. 🔵 **A rate near 1.0 over a large
`comparable` is the rubber-stamp finding** — an oversight audit's actual question, measurable
only because the record was kept. The worked example reports `2/6 = 0.33`. Records where the
agent made no recommendation are excluded from the denominator rather than counted as
disagreement.

## 🔴 The boundary — state it in the SOW, not in a footnote

The chain is **tamper-EVIDENT, not tamper-proof.** It catches an edit, a deletion or a reorder
*in place*. It does **not** catch a writer who rewrites the whole file: that writer recomputes
every link and the result verifies clean. **Control `C18` asserts exactly that failure**, so no
reader of this suite can mistake the guarantee.

🟢 What closes the gap is publishing `head()` where the writer cannot reach it — a daily anchor
to a client-external system. **The anchor is the client's**, and `anchor_statement()` prints the
sentence to that effect beside the real head value so it cannot be quietly dropped.

Two further non-features, deliberate: **no query** (put a read model beside the chain, never in
it) and **no retention policy** (jurisdiction-specific; `R9` keeps the long-lived record
pseudonymous so retention is a client decision rather than a breach).

## What is NOT claimed

- 🟡 **The Annex III(3) limb tokens are `ATTRIBUTED`, not quoted.** `p289` measured 12
  authority hosts `POLICY-REFUSED` across 2 egress paths; `p291` did not reach EUR-Lex. The
  tokens are this base's working vocabulary keyed to a conference reproduction plus
  commentary. A client-facing use checks the Official Journal. 🟢 The code does not depend on
  the wording: `ANNEX_LIMBS` is a closed token set and `NONE-DECLARED` is a first-class member
  because `P48` step 2 says the **exclusions** are what an auditor probes first.
- 🔴 **It is not a legal opinion.** It records what was decided, by whom, on what basis. Whether
  that satisfies a given regulator is counsel's call.
- 🔴 **It does not enforce the agent's lack of a write path.** That lives in `auth-profiles.json`
  and the host sandbox policy. `R1` ensures the *record* cannot misattribute the decision; it
  cannot stop a badly-scoped agent from writing elsewhere.
