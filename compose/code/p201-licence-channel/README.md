# p201-licence-channel

Resolve a repository's grant from **bytes**, not from a licence field.

## What p201 measured, and why this directory exists

| measurement | result |
|---|---|
| `curl api.github.com` / `curl github.com/<slug>` / `curl github.com/trending` | `403` — sixth dated entry in the series |
| `curl raw.githubusercontent.com/<slug>/<branch>/<path>` | **`200`** — the blob channel is open and is authoritative for licence |
| GitHub REST `license.spdx_id` coverage over `topic:lms stars:>200` (32 rows) | **23/32** (`72`%) |
| + blob read (`NOASSERTION` rows resolved **6/6**) | **29/32** (`91`%) |
| genuinely ungranted on every channel | **3/32** — `LMS-Laravel` (505★), `OLD-LMS-Laravel` (288★), `LearnPress` (275★) |
| repos whose default branch is neither `main` nor `master` | **11 of 35** (`31`%): `release_11`, `15.0`, `release`, `dev`, `v2`, `mobile`, `develop` |

`NOASSERTION` means *GitHub could not match the licence text*, not *there is no licence*.
A **missing** field is the one that means what it says.

## The finding that produced this script (`Gap 454`)

p200 declared `polimediaupv/paella` *"declared, ungranted"* after probing five capitalised
path forms across three branches — **in the same pass in which it discovered a lowercase
`license.txt` on `frappe/erpnext`**. The grant is at `license.txt` on `develop`: `9 915` B,
`Educational Community License, Version 2.0 (ECL-2.0)`, with the § 3 narrowing to *"the needs
of the education communities"* on line 7. `polimediaupv/paella-core` is byte-identical
(`sha256` `15efd2f640ed…`).

A path vocabulary is a shared instrument, not a per-row habit.

## What this script does NOT do

It does not classify. Classification belongs to `../lib/license_family.sh` (`family_of`),
whose suite passes `207/207` and which was correct on **65/65** of p201's blobs — including
the five GPL-3.0 rows a naive detector calls AGPL, both `ECL-2.0` rows, and `leemons`'
non-OSI `FAIRCODE`.

A pass that writes its own classifier re-earns the § 13 defect: **the GPL-3.0 text contains the
phrase "GNU Affero General Public License" in its own section 13**. That is `P237`, recorded
four times now (p77, p200 among them).

Two further cautions p201 measured:

- **Bytes are an integrity check on one blob, never a family test.** GPL-3.0 spans
  `35 146`–`35 193` B and AGPL-3.0 spans `33 893`–`35 136` B over 19 blobs — a 10-byte gap at
  the closest. `ECL-2.0` spans `9 915`–`12 322` B across four copies of the same licence.
- **A mention count is not a threshold.** p200 published *"count of `affero` = 15"* for
  AGPL-3.0; that is the **line** count, and the **occurrence** count is `16`. And
  `24kchengYe/human-skill-tree` is genuinely AGPL-3.0 with a count of `4`, because its notice
  is a 1 134 B header rather than the full text. Classify on the **title line**.

## Usage

```
bash probe_licence_blob.sh polimediaupv/paella ILIAS-eLearning/ILIAS
bash test_probe_licence_blob.sh     # 12 offline checks, no network
```

Output is TSV: `slug  branch  path  bytes  sha256_12`, or
`slug  branch  NO-BLOB-IN-<n>-PATHS  -  -`.

## Evidence

- `evidence/paella-grant-found.2026-10-14-p201.tsv`
- `evidence/topic-lms-licence-coverage.2026-10-14-p201.tsv`
- `evidence/default-branch-census.2026-10-14-p201.tsv`
- `evidence/licence-blob-crosscheck.2026-10-14-p201.tsv`
- `evidence/split-scope-notices.2026-10-14-p201.tsv`
