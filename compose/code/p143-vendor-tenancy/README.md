---
industry: education
region: Global
updated: 2026-10-12
---

# `p143-vendor-tenancy` — `ACTION DK`: the falsifier FIRED, and the channel is retired after placing the one row it was built for

🔴 **Falsifier fires: 2 rows, not 3.** The channel is not worth a standing instrument.
🟢 **And it resolved `karkarkins/BlackboardAssistantMCP`, which has been `UNMAPPED` since
p142** — so p142's three unplaced rows are now two.

## What was registered

> 🟡 **`ACTION DK`** — build the vendor-tenancy host channel: extract `*.blackboard.com`,
> `*.instructure.com`, `*.brightspace.com` subdomains across the 44-row population and
> resolve only where the subdomain is an institution's own registered abbreviation.
> 🔴 **Refuted if fewer than three rows yield a tenancy subdomain that is not a
> placeholder** — which makes this a one-row channel not worth an instrument, and `ncat`
> should be hand-noted instead.

## Four things live under a vendor domain and only one places anything

| class | examples | places? |
|---|---|---|
| 🔴 **`VENDOR_INFRA`** | `developer.blackboard.com` ×19, `files.blackboard.com`, `basic-doc-viewer.eu.api.blackboard.com`, `notif-websockets-eu-central-1.prod.notifications.api.blackboard.com`, `community.canvaslms.com` | 🔴 **nothing** |
| `PLACEHOLDER` | `example.blackboard.com`, `your-instance.blackboard.com`, `school.instructure.com`, `myuni.blackboard.com` | nothing |
| `OPAQUE` | `alt-5f0d0e6d23ee0.blackboard.com`, `alt-0123456789abc.blackboard.com` | nothing — a real tenancy whose label names nobody |
| 🟢 **`TENANCY`** | `ntnu.blackboard.com`, `ncat.blackboard.com` | 🟢 **an institution** |

🔴 **`developer.blackboard.com` is the single most common match in the whole population —
19 occurrences — and it is the vendor's own developer portal.** 🔵 **That is
`your-institution.instructure.com` one layer up:** the most frequent host-shaped string
under a vendor domain is the one that places least.

## Results over the 44-row population

| | |
|---|---|
| rows scanned | **44** |
| rows with any vendor-domain host | **6** |
| 🟢 rows placed by a resolved tenancy | **2** |
| rows with an unresolved tenancy label | **0** |
| 🔴 rows whose only vendor hosts are the **vendor's own estate** | **4** |

| row | tenancy host | institution | region | evidence sits in |
|---|---|---|---|---|
| 🟢 **`karkarkins/BlackboardAssistantMCP`** | `ncat.blackboard.com` | North Carolina A&T State University | 🟢 **North America** (United States) | `README.md`: `BB_LOGIN_URL=https://ncat.blackboard.com/` |
| `MartinSA04/ntnu-mcp` | `ntnu.blackboard.com` ×8 | Norwegian University of Science and Technology | **EMEA** (Norway) — 🔵 already placed by the offset channel, so this is corroboration | 🟡 `tests/fixtures/course_page_*.html` |

🔴 **Rows carrying only the vendor's estate:** `alejooroncoy/campus-cli`,
`felipedias-ie/blackboard-mcp`, `nitsuah/bb-mcp`, `skhdemo/uoft-quercus-mcp`.

## Why the falsifier firing is the right answer

🔴 **Two rows is below the registered threshold, so the channel does not become a standing
instrument.** And the detail is worse than the count: of the two,

* `ntnu-mcp` was **already placed**, and its tenancy evidence sits in a **test fixture** —
  a captured NTNU course page — not in shipped source. 🔵 **Weaker than a hardcoded host a
  connector must reach**, which is the standard `T29` sets.
* so exactly **one** row gains a placement from this channel, which is what the
  pre-registration predicted when it said `ncat` *"should be hand-noted instead"*.

🟢 **The hand-note, made:** `karkarkins/BlackboardAssistantMCP` is **North America (United
States)**, on a login URL its own README configures. 🔵 **That is not an inference from
three letters** — the repository tells you where it points.

🔴 **A tenancy label is resolved only against the hand-checked table in `tenancy.py`.**
There is no rule deriving institutions from strings, and an unrecognised single-label
tenancy is reported `TENANCY_UNRESOLVED` and places nothing. 🔵 **Guessing an institution
out of an abbreviation is how a region field gets poisoned**, and this population happened
to contain zero unresolved labels — so the table was never under pressure, and that is
luck, not design.

## The one judgement call, shown rather than buried

`myuni.blackboard.com` is classified `PLACEHOLDER`. 🟢 **Checked rather than assumed:** it
occurs in `felipedias-ie/blackboard-mcp/test/auth.test.ts:145`, in a list beside
`blackboard.example.edu` and `learn.university.edu`. 🔵 **Its neighbours settle it.**

## Net effect on p142's unplaced rows

| row | p142 | now |
|---|---|---|
| `karkarkins/BlackboardAssistantMCP` | `UNMAPPED` (`NO_HOST`) | 🟢 **North America** |
| `nitsuah/bb-mcp` | `UNMAPPED` (`NO_HOST`) | 🔴 still `UNMAPPED` — `developer.blackboard.com` only |
| `ruud0/aula-virtual-mcp` | `UNMAPPED` (`EDU_ONLY`) | 🔴 still `UNMAPPED` |

So the 19-row American-ambiguous population now stands at 🟢 **13 LATAM, 4 North America
(3 Canada + 1 United States), 2 UNMAPPED.**

## Run it

```
python3 -I tenancy.py subject=clone [...]   # result.2026-10-12-p143.tsv
```
