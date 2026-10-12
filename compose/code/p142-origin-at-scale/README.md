---
industry: education
region: Global
updated: 2026-10-12
---

# `p142-origin-at-scale` — `ACTION DH`: the offset channel is additional, and it cannot place either American region

**Population:** the **44** GitHub rows in the four SIS / portal-connector tables of
`agents/top.md` — *Generic / platform-independent*, *Institution- and nation-bound portal
connectors*, *Staff- and teacher-facing administrative agents*, and the Blackboard tier under
*The credential model is a tier-wide blocker*. 🔵 **p141 called this population 43 rows; the four
tables now hold 44.** The list is derived from the page by script and committed, so the
denominator is checkable rather than quoted.

All 44 were cloned `--filter=blob:none --no-checkout`. 🟢 **44 of 44 are publicly readable**,
against a nonexistent control that fails — worth stating next to the npm tier, where
`ACTION CY` found 4 of 6 with no reachable repository at all.

## Verdict on the action: 🔴 **DISCHARGED, NOT REFUTED**

p141's falsifier: *"Refuted if the offset channel places no row that the payload channel could
not."* 🟢 **It places 23 rows the payload channel could not even be pointed at** — none of these
44 is npm-published, so there is no payload layer to read. `T29`'s second clause is earned.

| region | rows placed |
|---|---|
| 🟢 EMEA | **12** |
| 🟢 APAC | **11** |
| 🔴 **North America** | 🔴 **0** |
| 🔴 **LATAM** | 🔴 **0** |
| UNMAPPED | 21 — of which **19** are refused bookings and 2 are UTC-only |

## 🔴 The finding p141 asked for, and the one it did not expect

p141 asked for the LATAM count *"explicitly, including when it is zero"*, reasoning that
*"an eleventh null on 43 rows is a far stronger statement than a tenth on eight."*

🔴 **The null is 0 of 44 — and it is not a statement about LATAM.** Every one of the 19 refusals
is an American offset: **11 at `-0300`**, **6 at `-0400`**, **1 at `-0500`**, plus two rows whose
every commit is UTC. p141's table refuses an offset shared across regions, and the offsets of
Brazil, Argentina, Peru, Mexico, the United States and Canada are *precisely* the shared ones.

🔵 **The North America zero is the proof.** No one reading a shelf that holds `UofT-MCP`,
`uoft-quercus-mcp` and `mcgill-vsb-mcp` would accept "no North American row" as a measurement —
and it comes out of the same rule, for the same reason. 🔴 **So this channel is structurally
incapable of placing a row in either American region, and this KB has published its LATAM zero
for ten passes as though the channel had looked.** The resolution is
[`p142-americas-disambiguation`](../p142-americas-disambiguation/README.md).

## Two corrections to p141's instrument, both in its columns rather than its verdicts

🔴 **`anthropic.com` was being reported as an institutional email domain.** p141's agent-tier TSV
carries `anthropic.com(59)` for `tutor-mcp` and `anthropic.com(98)` for `OpenTutor` in a column a
reader uses to place a repository — while the same pass measured, from the other end, that *"151
of 191 commits carry a `Co-Authored-By: Claude` trailer"*. 🟢 **Nothing was ever booked off it**,
since the region column is driven by offsets alone, so this corrects a misleading column and no
published region. Tool addresses now have their own `tool_mail` column.

🔴 **`git ls-files` reads the index, which a `--no-checkout` clone does not have.** Left
unchanged it would have reported every one of these 44 rows as shipping no funding file,
silently and uniformly. `git ls-tree -r --name-only HEAD` is used instead, and vendored
`node_modules/**/FUNDING.yml` is excluded — p141's own `mcp-canvas-lms` row listed 18 of those,
none of them the project's.

🟢 **The offset table itself is imported from p141 and not redefined**, and
`test_origin_scale.py` asserts object identity on `book`, `offsets` and `PERSONAL_MAIL`: a sweep
that retypes its instrument cannot tell a changed verdict from a changed method.

## Reproduce

```sh
python3 -I origin_scale.py "owner/repo=/path/to/clone" ...   # TSV on stdout, totals on stderr
python3 -I test_origin_scale.py                              # 9 tests
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv) (44 rows),
[`detail.2026-10-12-p142.txt`](detail.2026-10-12-p142.txt) (the totals as run).
