---
industry: education
region: Global
updated: 2026-10-20
---

# `p332-delivery-audit/` — the direction `p235` refuses: did a measured row ever reach a shelf?

**Pass 332, 2026-10-20.** Instrument: `delivery_audit.py`. Controls: `test_delivery_audit.py` — **40, all offline**, wired into `make gate-offline`, so this does not become another prescription that lives in prose.

```sh
make delivery-audit                        # the report
python3 -I delivery_audit.py --tsv         # one row per undelivered slug, ranked
python3 -I test_delivery_audit.py          # the 40 controls
```

## Why it exists

**`p327` prescribed this audit. `p331` measured the cost of its absence and said where it belonged:**

> This KB's discovery rate on `lti-tool` was 100% at p232 and its delivery rate was 0% through p330 — the exact failure p327 named and prescribed an audit for, still unrun. The prescription was right; nothing executes it. **It belongs in the hook tier, not in prose.**

🟢 **`p235-carried-index` answers `carried(slug)` — *is this row on the shelves?* — and deliberately refuses to read `evidence/`.** That exclusion is correct and load-bearing: a measurement is not a published row. 🔴 **But nothing ever asked the symmetric question, which is the one that costs a client a finding.** `p996-promotion-ledger/reconcile_code_shelf.py` asks it of `compose/code/`, not of `evidence/`.

## What it reads

🟢 **The shelf side is `p235`'s `harvest()` BY IMPORT, never reimplemented** — so the two directions cannot drift apart about what *carried* means. The evidence side is every `.tsv`/`.csv` in `evidence/`, `#` comment lines skipped.

A slug counts as **delivered** if a shelf carries its URL **or names it in prose**. 🔴 **That second channel is not a nicety; it is worth 16 points of delivery rate.** `p235` indexes `github.com/<slug>` only, and three rows in the first run's defect list (`qtiworks`, `bnlp`, `uniroster-server`) are discussed on these shelves by name with no URL beside them. **With the URL channel alone: 62.6% delivered, 38 deferred-permissive rows. With both: 78.9% and 16.**

## The two things that make "measured but not delivered" ≠ "defect"

🔴 **1. `evidence/` contains seeded decoys.** The highest-sighting row in the first run, at **25 sightings**, was `DecoyLex/ltix` — `p208-seeded-error-audit/seed.sh`'s one invented slug, planted so the audit can be asked whether it finds a wrong cell. It must *never* reach a shelf. **A metric that does not subtract its own controls reports planted negatives as failures.** It is excluded by name in `CONTROLS`.

🔴 **2. Most undelivered rows were correctly refused — the refusal just was not written down.** `p332` probed the twelve most-sighted first-hand: **one genuine miss** (`h5p/h5p-interactive-video`), three already carried by name, eight dead, dormant or below bar. 🟢 **So `disposition` is the axis that matters, not `undelivered`:**

| disposition | meaning | count p332 |
|---|---|---|
| `pending` | a pass **deferred** it (`unplaced`, `unread`) | 33 |
| `refused` | a pass **wrote it off** (`dead`, `below bar`, …) — ranked LAST, this is the audit working | 43 |
| `silent` | measured, **never disposed of either way** | 🔴 **717** |

🔴 **The `silent` class is the standing finding (`ACTION ZA`): 717 rows measured with no verdict recorded, so every pass re-discovers and re-probes the same corpses.** The remedy is a disposition ledger, not a promotion pipeline.

## The prefix predicate, and why it is a question rather than a rule

`truncations()` flags a slug that is a strict prefix of another at a `.` boundary — the `dmitry-viskov/pylti1` vs `pylti1.3` class.

🔴 **`p250`'s `ACTION XN` proposed refusing every such slug and named its own falsifier: `TouchRefletz/maia` vs `maia.edu`. The probe went unrun for eighty passes.** 🟢 **`p332` ran it on all 27 pairs: 22 are real truncations, 3 have neither spelling resolving, and 2 are DISTINCT LIVE REPOSITORIES** — the named falsifier plus `autolab/autolab` beside `autolab.github.io`. **A refusal rule would have struck two live repositories off these shelves.**

Both exceptions sit in `PREFIX_BUT_DISTINCT` with the measurement beside them, and two controls assert the rule does not fire on either. 🟢 `.git` is normalised away at harvest: there the *longer* spelling is the artefact, the opposite direction, and a rule that "repaired" it would have turned seven correct slugs into clone URLs.

## Limits, stated

- 🟡 **The existence probe behind `PREFIX_BUT_DISTINCT` is a screen, not a proof of absence.** `404` on all ten paths is strong, but a repository with a non-standard default branch and none of `LICENSE`/`README.md`/`.gitignore`/`package.json`/`LICENSE.md` would also `404`. **`p293-slug-existence-oracle` is the calibrated instrument** for a hard negative.
- 🟡 **The name channel is a substring test.** A short repo name that happens to occur in shelf prose reads as delivered. It errs toward *under*-reporting the gap, which is the safer direction for a metric used to justify promotions.
- 🟡 **`CONTROLS` is a hand-maintained set of one.** If a later pass seeds another decoy, it must be added here or the audit will report it.

## Channels available in this environment, measured p332

| channel | result |
|---|---|
| `github.com` HTML | 🔴 `403` (proxy) |
| `api.github.com` | 🔴 `403` — recorded since `p37` |
| `codeload.github.com` | 🔴 `403` |
| `raw.githubusercontent.com` | 🟢 `200`/`404` — **the licence-payload channel** |
| `git clone --bare --filter=blob:none` | 🟢 works — **the activity channel** (commits, authors, head date) |
