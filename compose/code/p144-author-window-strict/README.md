# `p144-author-window-strict` — `ACTION DT`

> Place the 2 remaining `UNMAPPED` connector rows, or declare them unplaceable and say why.
> 🔴 *Refuted if neither row has an author with commits in both DST windows.*

## Verdict: 🔴 **DISCHARGED and REFUTED — neither row qualifies, and one is placed anyway**

🔴 **Neither `nitsuah/bb-mcp` nor `ruud0/aula-virtual-mcp` has a single author with commits in
both DST windows.** The falsifier fires exactly as written.

| row | human authors in both windows | outcome |
|---|---|---|
| 🔴 `nitsuah/bb-mcp` | **0** — all window commits are `SUM`, `-0400` | 🔴 **UNPLACEABLE, declared** |
| 🔴 `ruud0/aula-virtual-mcp` | **0** — no human commit in *either* window | 🟢 **EMEA (Spain)** — placed by institutional host |

## 🟢 `ruud0/aula-virtual-mcp` → EMEA, on a hardcoded base URL

`server.py:19` — `BASE_URL = "https://aula-virtual.unav.edu"`, with `server.py:4` stating
*"Connects to https://aula-virtual.unav.edu for ALL enrolled courses."*

🟢 **`unav.edu` is the Universidad de Navarra**, Pamplona, Spain, whose LMS is *Aula Virtual
ADI*. 🔵 **This is the `ACTION DK` channel, used on a row it was not built for**: the
deployment target is named in shipped source, not inferred from a ccTLD. 🔴 **And the
disambiguation matters** — `MiAulario`/Sakai belongs to the *Universidad Pública de Navarra*, a
different institution in the same city.

🟡 **The author channel disagrees and is the weaker evidence.** `ruud.perez@gmail.com` commits
at `+0200` in May and `-0400` in September; a Spanish resident is `+0200` in both. 🔵 **The
institution is where the software is deployed; the author is wherever they were sitting.**
This row is placed on the former.

## 🔴 `nitsuah/bb-mcp` — unplaceable, and `ACTION DT`'s stated reason is the wrong one

> *"…which would mean the author channel needs a commit volume these rows do not have."*

🔴 **`nitsuah/bb-mcp` has 241 commits.** Volume is not the problem.

| 2026 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---|---|---|---|---|---|---|---|---|
| commits | 35 | 42 | 45 | 59 | 6 | 32 | 14 | 8 |

🔴 **The entire history runs 2026-03 → 2026-10 — eight consecutive months lying wholly inside
one northern DST period.** There is no winter commit to compare against, because the
repository is younger than one DST cycle.

🟢 **So `P23`'s caveat is about CALENDAR SPAN, not commit volume**: the author channel needs a
history that crosses a DST boundary, and no number of commits inside a single summer will do.

🔴 **And it has no institutional host either.** Of its URLs, `developer.blackboard.com` (×9) is
the vendor's own estate and `blackboard.example.edu`, `mcp.example.edu`, `push.example.edu` are
placeholders. 🔵 **Exactly `P143-G`, confirmed on the row that motivated it.**

## 🔴 The window definition is the instrument, and the crude split manufactures LATAM rows

🔴 **This probe's first draft split the year Apr–Oct / Nov–Mar and reported
`nitsuah` as `-0400` in BOTH windows — a year-round `-0400`, i.e. Bolivia, Paraguay or
Venezuela. LATAM.** 🔴 **It was an artefact of the bucket boundary**: all 17 "winter" commits
fall in **March and November**, both DST-transition months, when US Eastern is already
`-0400`.

🟢 **The strict windows are `Dec/Jan/Feb` against `Jun/Jul/Aug`**, and the six transition-
adjacent months are discarded rather than reassigned. Under them the row correctly reports no
winter observation at all.

🟢 **p143's eduNEXT probe was checked and does NOT have this defect.** `dstsplit.py` already
sets `DST_IN = {4..10}`, `DST_OUT = {1,2,12}` and `BOUNDARY = {3,11}` *"reported, never
forced"*. 🔵 **`P143-H` stands** — the crude split was this pass's first draft, not the KB's.

## Discriminator

```
-0400 SUM / -0500 STD  -> US Eastern                 (North America)
-0400 SUM / -0400 STD  -> Bolivia/Paraguay/Amazonas  (LATAM, no DST)
-0300 SUM / -0400 STD  -> Atlantic Canada            (North America)
-0400 SUM / -0300 STD  -> Chile                      (LATAM, southern phase)
```

🔵 **Chile and Atlantic Canada share both offsets and differ only in PHASE**, so the
hemisphere's DST direction has to be read, not the offset set.

## Run

```bash
python3 -I author_window.py <repo-dir> [...]
```
