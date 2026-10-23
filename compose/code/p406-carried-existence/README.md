---
industry: education
region: Global
updated: 2026-10-23
---

# `p406-carried-existence` — `Gap 405-C`, closed over the WHOLE population

**Pass 406 of 2026-10-23** (the twelfth pass of this date). Instrument:
`carried_existence.py`. Controls: `test_carried_existence.py` — **29, all offline**,
mutation-verified twice, wired into `make hooks` as `gate-carried-existence`.

```
make gate-carried-existence        # 29 offline controls, in `make hooks`
make carried-existence-census      # the population, offline — no probe
make carried-existence-sweep       # ONLINE: every carried address probed
```

## 🔴 What `Gap 405-C` said, and why the fix was not a new channel

> *no instrument re-checks a carried address's EXISTENCE. Four addresses this base carries
> went unresolvable and only a pass that happened to clone them noticed … This is the
> THIRD measurement of the same decay* — `p332`'s 22 truncations and `p397`'s six
> non-existent carried slugs being the first two.

🟢 **The channel already existed and was already calibrated.** `p293-slug-existence-oracle`
measured this proxy's refusal signature against a control pair, fixed the verdict
vocabulary, and established the bound that makes the token `ABSENT-OR-PRIVATE` rather than
`ABSENT`. 🟢 **The population instrument already existed too:** `p351-address-shape`
separates *cannot be an address* from *may be an address* — and its own docstring hands
this question on **by name**:

> *whether an address answers is `p293-slug-existence-oracle`'s question*

🔴 **So the gap was never a missing channel. It was a missing SWEEP.** `p293` judges slugs
a pass **guesses** (argv); `p400-candidate-membership` judges candidates a pass is **about
to shelve**. Neither asks the question over the rows this base **already carries** — the
only population whose decay can make a published recommendation point at nothing. This
module is the composition of the two, plus the three things a sweep needs that a one-off
does not: **concurrency, a resumable cache, and a retry rule.**

## 🔴 The defect this module is built not to commit

A sweep is concurrent, and github.com answers a throttled probe with a transport error.
`p293`'s `CHANNEL_RE` already carries `Too many concurrent`, so the **verdict** is
correctly `CHANNEL-ERROR` — but a census that divides unresolvable-by-total turns every
throttled probe into **decay**, and the published rate then **climbs with the worker
count**.

🟢 **So `CHANNEL-ERROR` and `MALFORMED` are excluded from BOTH sides of the rate**, each
one is retried **serially** before it is reported, and `C12` is the mutation control: it
constructs the population where the three readings differ —

| reading | rate on `C12`'s population |
|---|---:|
| 🟢 graded half only *(this module)* | **10.00 %** |
| 🔴 inconclusive counted as decay | 55.00 % |
| 🔴 inconclusive counted as live | 5.00 % |

🔵 This is `p293`'s own bound one layer out: *reading a transport failure as a statement
about the slug* is the expensive error, and **a denominator is where a sweep commits it
silently.**

## 🟢 The measurement, 2026-10-23

Evidence: [`carried-existence.2026-10-23-p406.tsv`](../../../evidence/carried-existence.2026-10-23-p406.tsv)
— 2 682 address rows, 5 columns.

| cifra | valor |
|---|---:|
| addresses carried, over the nine shelves | **2 682** |
| `EXISTS-PUBLIC` | **2 620** |
| `EXISTS-NO-REFS` *(an empty repository, which EXISTS)* | **2** |
| `ABSENT-OR-PRIVATE` | **59** |
| `CHANNEL-ERROR` *(after one serial retry)* | **1** |
| graded | **2 681** |
| **decay rate, over the graded half** | **2.20 %** |

### 🔴 `p405`'s 10.6 % was a SAMPLE ARTEFACT

`p405` measured **5 of 47 = 10.6 %** and wrote that down as *"the number a standing gate
would be sized against."* 🔴 **It is 4.8× the population rate.** The mechanism is
selection: `p405`'s 47 were the addresses it had **cloned for a lineage question**, i.e.
the `canvas-mcp`/`moodle-mcp` name-collision groups — precisely the crowded,
hobby-project end of this base, where decay concentrates. 🟢 **A gate sized against
10.6 % would have been sized against the wrong base rate**, and this is the second time a
figure derived from that group has been read as a statement about the shelves as a whole
(`p405`'s own `27 projects` is the first, and it says so).

## 🟡 THE BOUND THAT MATTERS MOST: this instrument reads ADDRESSES, NOT SENTENCES

**59 unresolvable addresses, and 12 of them sit on `agents/top.md`** — the build-on tier a
client engagement reads first. 🔴 **This pass's own draft published that as "12 broken live
recommendations." It is wrong, and every one of the 12 refutes it.** Adjudicated by hand:

| the 12, adjudicated | state on the shelf that carries them |
|---|---|
| `apereo/opencast` | 🟢 already recorded **DEAD since `p230`**, with the live successor `opencast/opencast` **and** a redirect row at `repos/foundations.md:747` |
| `e9x/blackboard-mcp` · `parkseokjune/unist-blackboard-mcp` | 🟢 already **"DEAD / private"** in writing (`agents/top.md:1469`) |
| `eastarctica/canvas-mcp` | 🟢 already `UNRESOLVED` at `p402`, restated by `p405` |
| `nmaaalhawary/mcp-moodle` · `superbuilders/timeback-dev-python` | 🟢 **deliberately unlinked** as absent addresses, per `gate-dead-citation` I2 |
| `santillana-ai/tutor-sdk` | 🟢 carried 🔴 inside a licence-unauditable row |
| `thanh01pmt/interactive-quiz-kit` · `mckaroff/graphlms` · `ale-alejandro/beadkit` · `ai-matrix-engine/aidream` · `yokowasis/autograder` | 🟢 the **five "published-but-unreadable"** specimens — cited *as* examples of a package that ships from a source nobody can read, which is the finding, not a recommendation |

🟢 **So the realised loss is ZERO: not one live recommendation on any build-on tier points
at nothing.** 🔴 **And that REFUTES `Gap 405-C`'s premise** — the decay was not noticed
*"only by a pass that happened to clone"*; it was adjudicated and written down, every
time. What was missing is not the noticing, it is the **standing** check.

🟡 **The generalisable bound, and it is why the adjudication above is by hand:** a sweep
over addresses **cannot distinguish a recommendation from a warning**, because the
distinction lives in the prose around the address and this instrument reads neither. An
address recorded *as dead* and an address recommended *while dead* are the same row here.
🔵 So `gate-carried-existence` ships the **offline controls** as the standing check and the
**sweep stays out of `hooks`** — a red sweep is a pass's work to adjudicate, never a
gate's verdict. Registered as `Gap 406-A`.

## 🟡 A THIRD state the token conflates, measured

`p293`'s bound names two inseparable cases: **absent** and **private**. 🔴 This sweep found
a third. `apereo/opencast` is `ABSENT-OR-PRIVATE`; `opencast/opencast` is `EXISTS-PUBLIC`
at `153d1b1` with a commit dated **2026-10-22** and an **ECL-2.0** title line read
first-hand. The repository did not die — **it MOVED**, and nothing in this channel says so.

🟢 **`C7c` therefore forbids inventing a `MOVED` token from a sweep.** A move is only
establishable by probing a *guessed successor*, which is `p293`'s question again and is
evidence about the guess, not about the original address. 🔵 Of the 11 remaining dead
addresses, guessed successors were probed and **all 11 returned the refusal** — weak
evidence, and recorded as weak.

## 🟢 By-product: 40 HEAD collisions, which is `p283`'s question answered at scale

`--symref` carries the HEAD sha, so a sweep adjudicates *"two names, one tree"* for free.
**40 collision groups** over the live population.

🔴 **This pass's draft published all 40 as findings, and `gate-alias-canonical` caught it.**
Graded against [`alias-register`](../../../evidence/alias-register.2026-10-21-p370.tsv) (45
addresses over three files) the 40 are **20 already fully held · 1 partial · 19 not in the
register**. 🔴 The draft also named a **stale** address beside its canonical one
(`learner-credential-wallet`), which re-opens a double-count `p349` closed — so only
canonical addresses are published and only the 19 are open.

🆕 Among the 19: `project-sunbird/sunbird-portal` ↔ `sunbird-ed/sunbirded-portal` (India's
national stack), `edificeio/entcore` ↔ `opendigitaleducation/entcore`,
`meta-pytorch/opacus` ↔ `pytorch/opacus`, `ki-campus/lrs` ↔ `openhpi/openlrs`, two further
`1edtech`/`imsglobal` pairs beyond the six the register holds, and **four that do not read
as aliases at all** — `openedx/openedx-core` ↔ `openedx/openedx-learning`,
`os4ed/opensis-classic` ↔ `…-responsive-design`, `openstax/osbooks-college-physics` ↔
`…-bundle`, `ls1intum/iris` ↔ `ls1intum/pyris`. 🔵 A shared HEAD is an **identical tree**, so
those four are either mirrors or one forked from the other **today**, and the two cases carry
opposite consequences for a dependency. `p283` owns the verdicts; every group is recoverable
from the evidence TSV's `head_sha` column.

## What this does NOT claim

- `ABSENT-OR-PRIVATE` is **not** `ABSENT` (`p293`'s `C9`, re-asserted as `C7a`/`C7b`).
- `EXISTS-PUBLIC` says the address **answers today**, not that the artefact is maintained
  — that is `p173-dormancy-bands`'s question.
- The **1** `CHANNEL-ERROR` is `torvalds/linux`, which timed out twice on a 30 s budget.
  It is a statement about the probe budget against a very large repository, **not** about
  the slug.
