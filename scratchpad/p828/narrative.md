## Thirty-third pass (`p828`, 2026-11-15) — the LMS tier this base had named `1,100` times and shelved five rows of, and a README that contradicts its own shelves

🟢 **`61` build-safe rows filed (`54` agents `270` → `324`, `6` foundations `142` → `148`,
`1` vertical platform `131` → `132`), `3` trends (`T99`–`T101`), `1` recipe (`P68`), `2` `T27`
licence rescues, `3` regulatory instruments new to this base, and `5` dated regional blocks in
`intel/market.md`.** 🔴 **One defect found in this repository itself and fixed.**

### 🟢 Channel conditions — the best in several passes, and both directions controlled

| Channel | `p827` | `p828` | Control run |
|---|---|---|---|
| `gh api search/repositories -f q="repo:OWNER/NAME"` | blocked | 🟢 **LIVE** | 🟢 **Bidirectional:** `repo:moodle/moodle` → `total_count=1` with licence/stars/pushed; `repo:gmilano/invented-control-t970-xyz` → **HTTP `422`**. A `1` and a `422` are distinguishable |
| `raw.githubusercontent.com` byte-read | 🔴 `403` throughout | 🟢 **LIVE** | 🟢 Positive control: `moodle/moodle` `COPYING.txt` returns GPLv3 text |
| `curl -sI https://github.com/…` | useless | 🔴 **useless, re-confirmed** | 🔴 Returns `HTTP/1.1 200 Connection Established` for a LIVE address **and for an invented one** — that line is the PROXY's `CONNECT` response, not an origin status. `T923`/`T970` hold |
| `gh api repos/OWNER/NAME` | — | 🔴 **BLOCKED** | *"GitHub access to this repository is not enabled for this session"* — session scope. 🔵 **New channel note: the `search/repositories` `repo:` form works where the direct repo endpoint does not; it is the narrowest working existence oracle here** |

🟢 **Consequence: EVERY licence filed in `p828` is BYTE-READ on `raw.githubusercontent.com`, not
field-read.** 🔴 **Every market and regulatory item is `CITED, NOT READ` from WebSearch summaries
and says so at the point of use.**

### 🔴 `D828-1` — the README contradicts the shelves, and has since `p812`

🔴 **`README.md` (pass `p811`, `2026-11-13`) still states: `Global 49 · EMEA 9 · North America 4 ·
APAC 3 · 🔴 LATAM 0`, and calls the LATAM zero *"the hardest number this base has produced about
the region."*** 🟢 **That zero was broken at `p812` and has been false for `17` passes.** Measured
on the shelf this pass, before `p828`'s own additions: **`Global 145 · APAC 48 · EMEA 41 ·
North America 18 · LATAM 18`.**

🔴 **This cost real work.** `p828` opened by re-running a LATAM sweep against a nil the base had
already closed, and re-"discovered" the SIGAA cluster — `GallegoSz`, `heitorsDev`, `Pedromaia0`,
`vintatri`, `erickmsms`, `unb-mds` — every one of which was already on the shelf. 🔵 **The defect
class is `p543`'s, one level up: A COUNT WRITTEN IN PROSE BESIDE THE ROWS IT COUNTS, except here
the prose is in a DIFFERENT FILE from the rows, so `ingest/derive-counts.py` — which grades
headings against their own page — structurally cannot see it.**

🟢 **Fixed in this pass:** `README.md`'s region tally is replaced with the derived figures and
dated. 🔴 **Prescription for the next pass, NOT executed here:** extend the gate to grade
`README.md`'s region tally against `agents/top.md`, or stop publishing a tally in the README at
all. **A cross-file count has no gate, and this base now has evidence that ungated counts go
stale and get quoted.**

### 🔵 What the broad sweep actually proved about this base

🔵 **Most of what a wide sweep surfaced this pass was ALREADY HELD here** — `alejooroncoy/campus-cli`,
`pengusto/google-classroom-mcp`'s proprietary grant, `Regulation (EU) 2026/1744`, the staleness of
`GeovaneSchmitz/sigaa-api`, and the whole SIGAA cluster. 🟢 **That is a good result for a base at
its thirty-third pass: the generic channels are saturated against it.** 🔴 **It is also the
argument for `T99`'s method — the yield came from running the BRAND axis against vendors the base
had never enumerated, not from searching harder for "education AI agents."**

### 🟢 `T27` confirmed twice more, in the rescue direction

| Repository | GitHub field | Bytes read this pass | Disposition |
|---|---|---|---|
| [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 🔴 `NOASSERTION` | 🟢 **MIT** (`sha256:3f0e907830ac…`) | 🟢 **Rescued and filed** |
| [`RobertLMcCrary/D2L-MCP`](https://github.com/RobertLMcCrary/D2L-MCP) | 🔴 `NOASSERTION` | 🟢 **MIT** (`sha256:e3fdd2a6e7ff…`) | 🟢 **Rescued and filed** |

🔴 **And `T93` independently re-confirmed, against this pass's own method.**
[`gangula-karthik/ntulearn-mcp`](https://github.com/gangula-karthik/ntulearn-mcp) reads
`NOASSERTION`, and `p828`'s classifier — which matches the MIT grant line and the warranty
clause — passed it as MIT. 🔴 **`p827` had already diffed it against canonical MIT text and found
the GRANT CLAUSE REWRITTEN.** 🟢 **It is therefore NOT filed.** 🔵 **A header-and-hash read is not
a licence read; only a canonical diff is. `p828`'s harness has the same defect `T93` named, and
recording that is more useful than quietly excluding the row.**

### 🔴 Rejections and declared limits

- 🔴 [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) — field
  `NOASSERTION`; bytes are a **"Pengusto Commercial License 1.0"**, *"All rights reserved except
  as expressly granted"*. **Commercially prohibited. Already held in `agents/trending.md`;
  re-confirmed here by byte-read, not newly found.**
- 🔴 Unlicensed and therefore NOT filed, though real and relevant: `joaosnet/sigaa-ufpa-mcp`,
  `DaviPac/Sigaa-UFRPE-MCP`, `sebassg/sia-unal-mcp`, `KaioBorgesDev/siga-mcp`,
  `Anggelie/mcp-local-server-uvg`, `JuancitoCozzeti24/santa-rita-escolar`,
  `u-hashmi/desire2learn-mcp`, `falkenslab/moodle-sandbox`, `kkauaon/qaluno`.
- 🔴 `csmediapro/moodle-mcp-server` is **AGPL-3.0** (byte-confirmed) — copyleft, not filed to the
  build-safe shelf.
- 🔴 `NiccoloSalvini/mcp-blackboard-ucsc` is filed `Global`: the institution behind `ucsc` was
  **not resolved and deliberately not guessed**.
- 🔴 **`agents/trending.md` and `repos/trending.md` were APPENDED to, not rewritten.**
