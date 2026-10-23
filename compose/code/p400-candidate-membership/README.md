# `p400-candidate-membership` — the ACCEPTANCE test, which no instrument owned

`ACTION p400-C`.

## The defect

Every census on this tree asks **"which addresses does the shelf hold?"** — `p351`
(shape), `p367` (channel B), `p375` (the union), `p371` (the promotion backlog),
`p332` (delivery). 🔴 **Not one asks the opposite question** — *"is THIS candidate on
the shelf?"* — which is the question every pass actually answers before it writes
anything, and which was answered **by hand, with a grep**.

`p398` and `p399` both certified their declines with the phrase *"each checked by
**grep** rather than by memory"*. 🔴 A grep for a bare repository **name** is a
**substring match over the shelf text**, so it answers *"already shelved"* whenever any
carried name merely **contains** the candidate's.

**The specimen is live and it is `p400`'s own.** The supply leg returned
`andres-tovar-purdue/ai-grader`. A bare `grep ai-grader` over this tree returns hits —
every one of them from [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader),
a different owner and a **different name**. 🔴 `p400`'s first check read that as
"already shelved" and nearly dropped the address.

### The nearest owner, named so this is not re-sold as new

`p332-delivery-audit` already reports this **shape**: its `PREFIX PAIRS` arm finds
`eecs-autograder/autograder` against `eecs-autograder/autograder.io`. 🔴 **But `p332`
looks inside the harvested corpus**, pairing slugs the shelves already hold. An incoming
candidate is not in the corpus yet, which is exactly why the shape survived there and was
never caught at the door. Same family as `T80`: a defect one layer out from the
instrument that owns its shape.

## What it does

    membership.py classify <candidate...>     -> one verdict per candidate, TSV
    membership.py audit <file> [root]         -> one candidate per line, TSV + a summary

| verdict | meaning |
|---|---|
| `SHELVED-EXACT` | the folded address is carried, in **either** address channel |
| `NAME-OTHER-OWNER` | the **same name** under an owner this base does not carry — a true collision |
| `NAME-SUBSTRING-ONLY` | 🔴 **the defect's class**: the text says yes, every address channel says no |
| `UNSHELVED` | neither, and not in the prose either |
| `NOT-AN-ADDRESS` | `p351`/`p375` shape rejection, asked **first** |

`NAME-OTHER-OWNER` and `NAME-SUBSTRING-ONLY` are deliberately **not** merged. Both mean
"unshelved as an address", but one is a genuine same-name collision (this base carries
NINE distinct `*/ai-tutor` owners) and the other is an artefact of the measuring
instrument. 🔴 Collapsing them hides the defect inside a legitimate class — which is how
it survived this long.

## Reuse, not restatement

- the address set comes from **`p375.union_harvest`** — channel U ∪ channel B with both
  shape filters applied. **Not** re-implemented.
- the shelf list is **imported from `p235`'s committed index** (`p286`'s ratchet, and
  `p371`'s own remedy for this exact temptation).
- shape rules are **`p351.classify`** and **`p375.name_reject`**, called rather than
  re-spelled. No vocabulary is copied into this file.

## Why BOTH channels, and the mutation that proves it

`p374`/`p375` established that a bare backticked `owner/repo` is invisible to the
`github.com/` harvester. A membership test keyed on URLs alone therefore answers
**UNSHELVED** for `dymchenkko/claude-study-agent` and `i-ninte/grad-agent` — both fully
carried on `agents/trending.md` **with their grants read**, neither written as a link.

**16 controls, 0 failures** — and a suite that has never failed on its author has not
been tested, so the channel-B half was deliberately mutated to key on channel U alone:

    4 of 16 controls FAILED
    🔴 4. dymchenkko/claude-study-agent  got: NAME-SUBSTRING-ONLY (prose-only)  want: SHELVED-EXACT
    🔴 5. i-ninte/grad-agent             got: NAME-SUBSTRING-ONLY (prose-only)  want: SHELVED-EXACT
    🔴 9. mattpocock/skills              got: NAME-OTHER-OWNER                  want: SHELVED-EXACT

🔴 **Control 4 is the one to read twice: the two defects COMPOSE.** Under a URL-only
membership test, a fully-shelved address whose grant has been read grades as a *substring
artefact* — a verdict wrong in a direction neither defect produces alone. Both addresses
are pinned as controls so no successor can narrow this back to one channel.

Control 3 pins the **direction** of containment (`lti-ai-grader` contains `ai-grader`,
never the reverse), so a substring rule applied the wrong way round fails there and only
there. Group 5 forbids pinning a live derived total — `p376`'s rule: a census figure is
derived, never compiled in. Group 6 is `P541`: an empty population is a refusal (exit 2),
not an empty answer.

## `400-H` — the suite's own ordering defect, caught by its author's own write

The first suite graded its specimen against the **live shelves**. `p400` then wrote that
address onto `agents/trending.md` as a census address, and three controls went red —
correctly, because over the live tree the verdict had become `SHELVED-EXACT`.

🔵 That is `gate-census-currency`'s defect inside a test fixture. `p352`: *"a census whose
input is the shelves, published in the pass that then writes to the shelves, is stale the
moment it is written."* 🔴 **A control whose input is the shelves is stale the same way** —
so `p376`'s group-5 rule (*no fixture may pin a live derived total*) is a special case of a
wider one: **no control may pin a live derived verdict either.**

🟢 Fixed structurally rather than by updating the expected value: the rule controls read
[`fixture/shelf-a.md`](fixture/shelf-a.md), a committed synthetic population carrying the
containing name and not the contained one. Two live-tree controls remain, asserting only
what a pass cannot invalidate by writing (`11b`, `11c`). 🔴 The specimen's live verdict is
deliberately asserted **nowhere**. 14 → 16 controls.

## What it does NOT claim

`UNSHELVED` is **not** "new to the world" and **not** "worth promoting". `p400`'s own
specimen graded `NAME-SUBSTRING-ONLY`, was recovered, read, found **unlicensed**, and
stayed off every build-on tier. 🔵 **A membership verdict is an input to a licence read,
never a substitute for one.**

## Not yet wired into `make hooks`

Deliberately. This module is a **tool a pass runs on its candidates**, not a standing
assertion about the tree, and `hooks` holds gates that judge committed state. Wiring it
would require a committed candidate population to judge, which this base does not keep.
🔵 `p338`'s `ACTION ZP` is the cautionary precedent in the other direction — a gate with a
passing suite that sat in **no target** from `p383` to `p337` and judged nothing — so the
choice is recorded here rather than left implicit.
