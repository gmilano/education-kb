# `p253-settled-fact-regression` — a pass may not re-open what this base already settled

**What it answers.** Not whether a claim is true. Whether a pass is re-litigating a
question an EARLIER pass of this same base closed, without citing what closed it.

## The regression it was built from

| pass | what the shelves say |
|---|---|
| `p233` | 🟢 *"The Digital Omnibus on AI is `Regulation (EU) 2026/1744` — OJ `2026-07-24`, in force `2026-07-27`, Parliament `2026-06-16`, Council `2026-06-29`"* |
| `p241` | 🟢 Annex III education high-risk applies **`2027-12-02`**; `2026-08-02` is Article `50` transparency. Begins COUNTING re-services of the superseded date — *"at least the FIFTH"* |
| 🔴 `p251` | re-publishes it as a live disjunction *"pending formal adoption"*, and records **NOT ESTABLISHABLE** in `intel/open-gaps.md` |
| 🔴 `p252` | re-publishes *"the EU high-risk date is STILL a disjunction"* on three shelves |

🔴 **The cost was commercial, not cosmetic.** `compose/patterns.md` told the studio *"do
not sell an Annex III readiness programme this quarter"* on the grounds that the date was
unknown. The date was known, on these shelves, ten passes earlier.

🔵 **Why prose could not prevent it.** The shelves are append-at-top and run to ~160 000
lines. The settled reading sits `500`–`6 900` lines down; the carried ACTION ledger is
what a new pass reads, and once the re-opened form entered the ledger it propagated under
its own momentum. `p252` met the mirror image from the supply side — it checked candidate
slugs against the carried index rather than treating them as new supply — and recorded
that `make carried` could not be run from the session. **A base that cannot query what it
already knows pays for the same knowledge twice.**

## The rule

For each pinned fact in [`settled.tsv`](settled.tsv): a scope naming the subject AND
hedging about it is a `REGRESSION`, unless the scope also cites the authority that settled
it, in which case it is `ANNOTATED`.

Hedge vocabulary: `disjunction`, `pending formal adoption`, `not establishable`,
`not closable`, `unresolved`, `two candidates`, `cannot be closed`.

**The falsifier, and it is the one that matters:** correcting a re-service REQUIRES quoting
the wrong date, so a gate that flags `p241` is useless. `p241`'s row is pinned verbatim as
a control and grades `CLEAR` — by a second road, since it carries no hedge vocabulary at
all. A hedge that cites `Reg. (EU) 2026/1744` grades `ANNOTATED` by the exemption. Both
roads are asserted separately.

## Scope, and `ACTION XT`

A scope is a blank-line block, EXCEPT that a contiguous run of `|`-prefixed lines is one
scope. That is `ACTION XT`'s ask — *"give the exemption a TABLE-BLOCK scope"* — landed
here rather than in `p250`'s lint, because a hedge in a table row is argued by its
neighbouring rows and not by the paragraph above it. Three controls pin the scoping.

## Run

`settled_fact.py` prints the findings; `--verify` exits non-zero on any and is what
`make hooks` runs; `--all` grades the whole history instead of each shelf's newest section.
🔵 On the shelves as `p252` left them, `--verify` returns `3` findings — which is the point:
this instrument is checked in RED and `p253`'s own edits are what turn it green.

🔴 **A pinned fact that is WRONG will be defended by this gate until the pin changes.**
That is deliberate. `--pin` is a visible edit; silent re-litigation is not.

**Proven able to fail:** the `ANNOTATED` exemption stubbed to `if False` in a throwaway copy
→ `exit 1`, the exemption control named. `17/17` restored.

**And the defect this instrument shipped first:** `REPO` resolved two directories up,
landing on `compose/`, where every shelf is absent — so the gate reported **OK** while
scanning nothing. `p355-cwd-portability`'s class, and the silent-pass class `p250` and
`p251` both paid for. Two controls now pin the resolved root and the existence of every
shelf it claims to scan.
