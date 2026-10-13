---
industry: education
region: EMEA
updated: 2026-10-13
---

# `p172-aiact-shelf19` — Article 50(2) over the CURRENT shelf, 50 days out

**Pass 172, 2026-10-13. `ACTION JQ`.** Pass 45 measured Article 50(2) exposure over a 66-row shelf
that no longer exists. p172 re-ran the same two measurements, with the same regexes, over the shelf
this KB actually publishes: the **12** agent rows of `agents/top.md` and the **7** platform rows of
`repos/foundations.md`.

The deadline is **`2 December 2026`** — Article `50(2)` marking under
`Regulation (EU) 2024/1689`, unmoved by the Digital Omnibus (`ACTION JL`, p171). **`50` days.**

## Exposure: 13 of 19 rows put synthetic content in front of a person

| verdict | rows |
|---|---|
| `gen` — the row itself generates | **9** |
| `gen-ind` — packaged pedagogy, generated through the host agent | **3** |
| `pack` — where generated content BECOMES the course (`scorm-again`) | **1** |
| `no` — moves, records, grades, enrols | **6** |

All `6` of the `no` rows are the institutional platforms. **Every agent row is exposed.** That is
the framing number for an engagement: the LMS is not the Article 50(2) problem, the agent on top
of it is.

## Marking: 0 of 13, over 18 360 files

| magnitude | value |
|---|---|
| repos swept | **13** (13 of 13 reachable) |
| files listed | **18 360** |
| marking artefacts (`c2pa`, `watermark`, `synthid`, `content-credentials`, `imwatermark`) | 🔴 **0** |
| root manifests read | **11** |
| marking **dependencies** in them | 🔴 **0** |
| provenance artefacts (**not** the same thing) | **12, in 4 repos** |

**The first falsifier limb is SILENT: not one row emits a conformant marking.** Pass 45's finding
holds on a shelf with no rows in common with the one it measured.

## The distinction that matters to a client (`T233`)

The `12` provenance artefacts are about **INPUT** provenance — where source material came from — and
Article 50(2) asks about **OUTPUT** marking: telling the person that what they are reading or
watching was machine-generated. Those are different obligations and the shelf satisfies neither,
but it is closer on the one nobody asked about.

The sharpest case is the highest-exposure row.
[`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator)
emits synthetic **audiovisual** output and carries the most provenance machinery on the shelf — a
real `services/pipeline/src/alystria/security/provenance.py`, a `test_provenance_gates.py`, and
per-asset `*-provenance.json` for its demo media. **It still marks nothing it produces.** A
repository that built provenance gates and no output marking is not negligent; it answered the
question it was asked.

## The second falsifier limb FIRED: this is not an offline asset

`ACTION JQ` was registered with *"refuted if the instrument cannot run offline, in which case it is
not the asset this KB has been treating it as."* **It cannot.** `scan_marking.sh` needs
`git ls-remote` plus a blob-filtered `git clone` per repo, and `curl` to `raw.githubusercontent.com`
per manifest. The *verdict table* (`rows.tsv`) is offline data and genuinely reusable; the
*measurement* is a network instrument. Half the asset, and the half a client cannot run in an
air-gapped review is the measuring half.

## Files and how to run

```sh
sh scan_p172.sh rows.tsv /tmp/aiact502-p172
```

`rows.tsv` carries the exposure verdict and the reason for each of the 19 rows; the scan reads only
rows whose verdict is not `no`.

Result: [`../../evidence/aiact-50-2-exposure-shelf19.2026-10-13-p172.tsv`](../../evidence/aiact-50-2-exposure-shelf19.2026-10-13-p172.tsv)
