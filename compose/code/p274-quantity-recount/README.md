---
industry: education
region: Global
updated: 2026-10-17
---

# `p274-quantity-recount` — `T37` as code, because an amendment that is not built gets violated by the next pass

> New in **pass 274 of `2026-10-17`**. Discharges `p273`'s backlog item 7 (*"apply `T37` as a standing
> re-count … a `grep -c` over the rows is cheaper than the next defect"*).

## Why it exists

`T37` (`p272`) wrote the rule: **a quantity inside a gap statement is a carried datum — re-count it from
the rows, on every shelf that states it.** `p273` ranked building it seventh and nobody ran it. 🔴 **In
the two passes between the amendment and its implementation, three more stale quantities were
published.**

## Run it

```sh
python3 -I compose/code/p274-quantity-recount/recount.py --root .
```

No network. Prints one row per registered claim — `published`, `measured`, `MATCH`/`STALE`, and where the
published number lives — plus the MCP-server-by-platform tally it derives. Ledger committed as
[`evidence/quantity-recount.2026-10-17-p274.tsv`](../../../evidence/quantity-recount.2026-10-17-p274.tsv).

## First run: `3 STALE of 5`

| claim | published | measured |
|---|---|---|
| MCP server slugs on `agents/top.md` | **13** *(prose)* · **12** *(`T21`)* | **15** |
| **LMS platforms reachable by MCP** | **3** on both shelves | 🔴 **6** |
| permissive rows in the build-on tier | 23 | 23 🟢 |

🟢 **And then it caught `p274` itself** — after that pass shelved five of the missing servers it read
**20** against the **15** the pass had just written down, and flagged the pass's own prose `STALE` before
it was committed. 🔵 **A pass cannot hand-maintain a count it is simultaneously changing.**

## Three defects in its own first draft, recorded because each is the thing it exists to catch

| defect | fix | cost of the fix, stated |
|---|---|---|
| Classified a slug by its **row text**, filing `felipedias-ie/blackboard-mcp` under **Canvas** because the row mentions Canvas in prose | read the **slug first**, the line only as fallback | none |
| Accepted a slug whose **line** mentioned MCP, letting `chamilo/chamilo-lms` and `huggingface/transformers` into a per-platform tally | require the marker **in the slug** | the count is now a **FLOOR**: a server whose slug does not say `mcp` is missed |
| A **word-boundary** pattern silently dropped `AStheTECH/mewcp-google-classroom` and `blend-ed/tutor-contrib-openedxmcp` | match `mcp` as a substring, plus `mewcp` explicitly | slightly looser slug matching |

⚠️ **A counting instrument's own false negatives are invisible in its output.** The only reason these
surfaced is that it **prints the per-platform lists** it counts. **Keep that output; it is the audit.**

## One finding that came out of writing it

🟢 **GitHub `owner/repo` is case-insensitive, and `p274` proved it first-hand:** `ahmedEid1/Lumen` and
`ahmedEid1/lumen` return the **identical HEAD SHA**, which also settles the collision `p196` recorded
between them — **one repository, not two.** ⚠️ **So a case-sensitive census double-counts**, and this
base had at least three such pairs (`Lumen`/`lumen`, `RohanMuppa`/`rohanmuppa`,
`AStheTECH`/`asthetech`). **This instrument folds case before counting.**

## What it does NOT fix

The claim register is **hand-maintained**, so a quantity nobody registers is still uncounted. 🔵 **That
moves the failure from *"the number is stale"* to *"the number is unregistered"*, which is strictly
better** — an unregistered number can be found by grepping for digits; a stale one cannot be found at
all.
