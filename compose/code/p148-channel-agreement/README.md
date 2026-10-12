---
industry: education
region: Global
updated: 2026-10-12
---

# p148-channel-agreement — `ACTION ER`: the institution channel on the clone tier

`p147-npm-region` placed **2 of 8** npm rows by institution evidence and narrowed `T59`.
`ACTION ER` moved that probe to the **44 connector clones**, where `P144-V` found its
original instance, and tested it against the channel this KB has been placing rows with.

> 🟢 **`ACTION ER`** — re-run the institution channel over the 44 connector clones.
> 🔴 *Refuted if it disagrees with any region this KB has already placed on the
> commit-timezone channel.*

    python3 channel_agreement.py <institution.tsv> <offset.tsv>
    python3 test_channel_agreement.py    # 11 tests, authored fixtures, offline

## 🟢 Result — sixteen net new placements, and one disagreement

| state | n of 44 | meaning |
|---|---|---|
| 🟢 **`INSTITUTION_ONLY`** | 🟢 **16** | the offset channel declined; the institution channel placed it |
| 🟢 `AGREE` | **10** | both placed it, same region |
| `OFFSET_ONLY` | **10** | the institution channel found nothing |
| 🔴 `INSTITUTION_CONFLICT` | **3** | hosts in 2+ regions |
| `NEITHER` | **4** | no channel placed it |
| 🔴 **`DISAGREE`** | 🔴 **1** | 🔴 **the falsifier's population** |

🟢 **Connector-tier region coverage goes 20 → 36 of 44.** 🔵 **Almost all sixteen gains are
LATAM**, and the mechanism is precise: the offset channel declines `-0300` as `AMBIGUOUS`
(Brazil/Argentina/Uruguay **and** Greenland/St Pierre), while `sigaa.ufpi.br`,
`guarani.unq.edu.ar` and `aulavirtual.upc.edu.pe` are not ambiguous at all. 🟢 **This KB's
LATAM coverage was being suppressed by a timezone, not by a lack of evidence.**

## 🔴 …and the one disagreement is `T67`, one pass after `T67` was adopted

| row | institution | offset | evidence |
|---|---|---|---|
| 🔴 `felipedias-ie/blackboard-mcp` | **North America** | **EMEA** | 🔴 **`bb.edu`, in `test/unit.test.ts`** |

🔴 **Refuted on the literal criterion: one is more than zero.** 🟢 **And the row it fires on
is the exact evidence class `T67` demoted to a lead** — *a bare `.edu` is not a country
signal* — which the probe itself labels `bare .edu (LEAD — grandfathered non-US exist)`.
🔵 **`bb.edu` in a unit test is a placeholder, not a deployment.**

🟢 **Excluding bare-`.edu` leads: `DISAGREE` = 0, and the channels agree 10 of 10 where both
can answer.** 🔵 **So `P144-V`'s precedence rule needs no re-testing; `T67` needs promoting
from an observation into an exclusion** — deferred to `ACTION EZ` on purpose, because
changing the probe this pass would mean comparing a modified instrument against published
figures.

## 🆕 🔴 `T69` and `T70` — two false-positive classes the npm tier structurally cannot have

| population | artefact | placements | false-positive sources |
|---|---|---|---|
| 8 npm rows (p147) | a tarball, **filtered by a `files` allowlist** | **2** | 3, all placeholder hosts in `*.example.json` |
| 🆕 44 clones (p148) | **the whole committed tree** | **26** | 🔴 **test fixtures, mock data, locale files, link collections** |

🔴 **`T70`: `ahmedEid1/lumen` → EMEA on `youtu.be`**, from a video-ingest allowlist at
`apps/backend/app/services/content_ingest.py:70`. 🔵 **No academic-namespace rule catches
it** — `.be` is a plain ccTLD and the probe's ccTLD route worked as designed. 🔴 **The
missing category is "a global platform or URL shortener is not an institution."**
🟢 **Caught before publication**, and `lumen` is an agent-tier row outside the 44 anyway.

🔴 **Two more, in the conflict bucket:** `BetterSEQTA/BetterSEQTA-Plus` conflicts across
**four regions** from `src/seqta/content/links.json` (a link collection), and
`BetterSEQTA/DesQTA` reads `phet.colorado.edu` from `src/mock/data/courseContent.ts` (a
simulation library in mock content).

🔵 **`T69` is the generalisation**: an instrument's precision is a function of how curated
the artefact is, and one validated on a packaged tarball does not transfer to a whole clone
without being re-validated. 🟢 **`T68` is the same observation from the other end.**

## 🔴 The defect this module found in itself, before publishing

🔴 **The first run reported `# population (in both files): 0` and
`DISAGREE 0 → NOT REFUTED`.** The institution TSV had a **leading blank line**, so
`csv.DictReader` took the blank as its header and returned zero rows.

🔵 **That is `T64`'s shape in a new place, with the reassuring value**: a verdict over
nothing, reported as a verdict. 🟢 **The loader now skips blanks as well as comments, and
three of the eleven tests pin it** — including one that asserts the population is **5**, not
`0`, on a fixture whose first byte is a newline.

    11/11 passed
