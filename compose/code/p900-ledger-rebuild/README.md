---
industry: education
region: Global
updated: 2026-11-18
---

# `p900-ledger-rebuild/` — `899-G1` discharged, `899-G2` attacked, and the existence test corrected

**Pass 900, 2026-11-18.**

## What is here

| File | What it does |
|---|---|
| `build_ledger.py` | Rebuilds the `logged-not-shelved` ledger with `lib/slug_extract.py` instead of the ad-hoc regex p860 used. Offline. Emits `evidence/logged-not-shelved.2026-11-18-p900.tsv` and the delta against p860 |
| `measure_ledger.sh` | Measures the top N ledger rows via **batched** `repo:` qualifiers against `search/repositories` — existence, stars, SPDX, last push. Emits `evidence/ledger-measured.2026-11-18-p900.tsv` |

## The three findings, in the order they were forced

### 1. The hardened extractor had two live defects, and they were the defect it was written to fix

`886-G3` reserved `search` as an owner because this base quotes
`api.github.com/search/repositories` in method prose. It never reserved
**`api.github.com/repos/<owner>/<repo>`**, which this base quotes **380 times**. The first
ledger rebuild therefore ranked `repos/moodle` **5th** (14 files), `repos/hkuds` 7th and
`repos/openedx` 17th — and `owner/repo`, the literal placeholder in this base's own prose,
**2nd** (22 files). Eighteen `repos/<x>` artefacts and one template, all promotable.

### 2. Reserving `repos` is necessary and NOT sufficient — the obvious fix destroys real data

The API path **contains** the real address one segment deeper. A predicate that rejects
`repos/moodle` consumes the text and `moodle/moodle` is never emitted. **The prefix must be
consumed by the regex AND `repos` must stay reserved**, because `github.com/repos/moodle` with
no third segment backtracks straight into `owner=repos`. Pinned as control `A-1`; the recovery
is visible in the output (`openedx/edx-platform` 24 → 27 files).

`lib/test_slug_extract.py`: **64 → 77 controls**, all passing. `test_region.py` (79) and
`test_licence_identity.py` (47) pass unchanged against the modified module.

### 3. A denylist cannot find the placeholders nobody has seen — existence can

`PLACEHOLDER_SLUGS` caught `owner/repo` because a pass had noticed it. It missed `x/y` (7
files), `a/b` (6), `git_user_id/git_repo_id` (6, an OpenAPI-generator template) and `v3/search`
(5). **All four were found by measuring whether the address resolves**, not by curation. That is
the reusable half of this instrument.

## The correction this pass published against itself

🔴 **`search/repositories` returning nothing is not evidence that a repository does not exist.**
Of 50 ledger rows it reported as absent, **22 (44%) return `200` on `raw.githubusercontent.com`**:

- **renames/transfers** — `Li-Evan/Bloom` → `BloomTutor`, `algorithm0r/canvas-lms-mcp` →
  `bruchris/…`, `aswanth9495/exam-guard` → `Scaler-Opensource/…`, `openedx/edx-platform` →
  `openedx/openedx-platform`. GitHub serves the old address indefinitely; `raw` follows the
  redirect and the search index holds only the canonical name.
- **unindexed but canonical** — `mitodl/open-learning-ai-tutor`,
  `DaRL-GenAI/instructional_agents`, `longsightgroup/qti3`,
  `tokenaii/horus-taleeq-0.2b-base`.
- **genuinely absent** — the four placeholders above, and 24 others.

**`p899`'s "`Li-Evan/Bloom` does not exist" is retracted**: it resolves, and serves a README
byte-identical to `BloomTutor`'s (`sha256₁₂ 8a74e9391a2b`).

🔵 **And the same mechanism bites the other way.** `halleck45/openpronounce` was drafted as a new
`agents/top.md` row and withdrawn: it is a transfer alias of `OpenPronounce/OpenPronounce`,
already shelved (`README.md` `sha256₁₂ a005d079f571` for both). **False absences in the ledger
and false duplicates on the shelf are one defect, and fixing only the first publishes the
second.**

## Known limits — do not read past these

- 🔴 The `raw` fallback tries **nine file keys** (`README.md`, `README.rst`, `README.rdoc`,
  `readme.md`, `README`, `README.txt`, `README.markdown`, `LICENSE`, `package.json`,
  `.gitignore`). A repository carrying none of them at `HEAD` reads as absent. **The 28
  remaining misses are "absent on nine keys", which is weaker than "does not exist."**
  The first run used `README.md` alone and under-counted by four — `openedx/edx-platform`
  is `README.rst`.
- 🔴 **300 of 6,208 rebuilt-ledger rows were measured.** The licence split (49.2% permissive /
  36.4% no readable grant) is a property of the top 300, ranked by how often this base logged an
  address. That ranking is **not** random with respect to licence. Do not transfer it to the tail.
- 🔴 `repos/<owner>/<repo>` on the **REST** API is session-scoped here (`403`), so rename
  direction can only be inferred from byte-identity plus a search hit on the canonical name,
  not read from GitHub's `full_name` field.

## Running it

```sh
python3 -I compose/code/p900-ledger-rebuild/build_ledger.py          # offline
bash compose/code/p900-ledger-rebuild/measure_ledger.sh \
     evidence/logged-not-shelved.2026-11-18-p900.tsv 300 \
     evidence/ledger-measured.2026-11-18-p900.tsv                    # network
python3 -I compose/code/lib/test_slug_extract.py                     # 77 controls
```
