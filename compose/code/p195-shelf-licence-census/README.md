---
industry: education
region: Global
updated: 2026-10-14
---

# `ACTION P195` — the shelf licence census, and the control that was already here

**Pass `195` of `2026-10-14`.** p194 pre-registered four experiments. This directory holds the
two instruments the third one needed, and the honest accounting of a fourth that should never
have been written.

## What was pre-registered, and what came back

> *"Read licences from bytes for the remaining ≈`430` shelf slugs via the raw lane. **Limb 1:**
> the lane scales → this KB's whole shelf gets a byte-verified licence column. **Limb 2:**
> rate-limited or `404`-noisy at volume → the lane is a spot tool, not a census tool."*

🟢 **Limb `1`, decisively.**

| | measured |
|---|---|
| LIVE slugs probed | **`468`** |
| HTTP probes | **`2 167`** *(`4.6` per slug — `337` of `380` hits are a plain `LICENSE`)* |
| 🔴 `429` / `403` / `5xx` | 🟢 **`0`** |
| rows `INDETERMINATE` | 🟢 **`0`** |
| licence FOUND at root | `380` |
| 🔴 no licence at root | `88` — `18.8`% |

## `shelf_licence_census.sh` — the census

`--one <slug>` emits one TSV row; `--self-test` runs `9` offline assertions.

Doctrine observed, each because this KB has already paid for it:

| rule | what it forces here |
|---|---|
| **`P237`** / `lib/README.md` | the classifier is **sourced, not forked**. `. ../lib/payload_measure.sh` brings in `license_family.sh` *(`P171` title-block classification; **`207`/`207` when the suite is run FROM `lib/` — see the cwd note below**)*. **No inline classifier** |
| **`P834`** | **no byte count from `$(…)`**. `size_of_file` over a file on disk, always |
| **`P126-2`** | 🔴 **a negative verdict needs a negative control.** `NONE` is emitted **only** when the full `19`-filename ladder returned `404` and **nothing** returned a refusal or throttle. Any `403`/`429`/`5xx` makes the slug `INDETERMINATE`. p194 read *"all `404`"* as *"no licence"* over `19` probes on `4` slugs; **at census volume that inference is exactly what throttling would forge** |

🔴 **The status gate is not cosmetic.** `raw.githubusercontent.com` answers a miss with a
**`14`-byte body reading `404: Not Found`** — valid text that a classifier will happily process.
This script gates on `%{http_code}`; 🔴 **p195's own manual spot-check did not, classified that
body, and had to retract a verdict mid-pass.** 🔵 `lib/probe_payload.sh:96` has guarded exactly
this since before p195 existed.

### Controls that reproduce known values

| slug | expected | got |
|---|---|---|
| `microsoft/ML-For-Beginners` | `LICENSE` · `1 141` · `MIT` *(p194)* | 🟢 exact |
| `moodle/moodle` | `COPYING.txt` · `35 147` · **`GPL-3.0`** *(p194's own correction)* | 🟢 exact |
| `frappe/lms` | `license.txt` · `33 893` · **`AGPL-3.0`** *(p193's costliest finding)* | 🟢 exact |
| `JushBJJ/Mr.-Ranedeer-AI-Tutor` | `NONE` after `19` probes *(p194)* | 🟢 exact |

## `continue_ladder.sh` — the repair for this instrument's own defect

🔴 The census ladder is frequency-ordered and stops at the **first** `200`. For
`shmercer/writeAlizer` that was `LICENSE` at **`47` B**, reading only `YEAR:` /
`COPYRIGHT HOLDER:` — the `usethis` **template stub**. 🟢 The real grant is `LICENSE.md`,
`1 076` B, `MIT`.

🟢 **What did NOT fail:** `license_family.sh` returned `UNCLASSIFIED` on the stub rather than
inventing `MIT` from the word `COPYRIGHT`. **The classifier guard held; the LADDER was the
defect.** 🔵 Run over all `5` `UNCLASSIFIED` rows: **`writeAlizer` is the only row of `468`
affected**, and the other four carry exactly one licence-shaped path each.

## `delivery_verdict.sh` — honest accounting of a control that already existed

`--self-test` runs `9` offline assertions. Its premise is sound and cheap: licence boilerplate
is boilerplate, so a payload claiming a family from far outside that family's byte band has been
**modified**. Bands are derived from this pass's own census, not from belief — **`218` `MIT`
rows: median `1 071` B, p25 `1 067`, p75 `1 080`, a `13`-byte interquartile spread.**

| | result |
|---|---|
| permissive rows re-read | `281` |
| 🟢 `IN-BAND` → `GO` | `265` |
| 🔴 flagged `MUST-READ-BODY` | **`16` — `5.7`%** |
| 🔴 of those `16`, already published by this KB | 🔴 **`16` of `16`** |

### 🔴 The finding it reaches, and why it is not a discovery

`osi_family_of` returns **`MIT`** and `commercial_use_ok` returns **ALLOWED** for all of:

| repo | bytes | real title | the body |
|---|---|---|---|
| `CaviraOSS/PageLM` | `8 563` | *"PageLM Community License"* | non-commercial + revenue-share |
| `GautamVhavle/learner-verse` | `2 594` | **BUSL 1.1** | bars *"direct or indirect commercial activity"* |
| `willwearing/graspful` | `1 439` | *"O'Saasy License Agreement"* | anti-SaaS non-compete |
| `MoKangMedical/digital-sage` | **`46`** | `MIT License` | 🔴 **a title and a copyright line. No permission clause** |

🟢 **The mechanism is worth carrying forward: `P171` widened the title window to `40` lines so a
REFLOWED `AGPL` would be caught, and that window swallows MIT's canonical *"Permission is hereby
granted, free of charge"* sentence out of licences that are not MIT. `P250`'s gate —
*"an identified OSI family permits commercial use BY DEFINITION"* — then trusts the family and
never reads the body. Two hardened controls, each correct in isolation, composing into the one
wrong answer that costs a delivery.** `learner-verse` proves it: `commercial_use_ok` **has** a
`BUSL` branch returning PROHIBITED and it never fired, because the family answered `MIT` first.

🔴 **And every one of those classes was already registered in this repository before p195 ran:**

| class | already registered as |
|---|---|
| MIT's body with a clause bolted on | **`P1054`** · [`p1054-mit-plus-clause`](../p1054-mit-plus-clause/) |
| a split-scope grant | **`P1056`** · [`p1056-split-scope-licence`](../p1056-split-scope-licence/) |
| sub-`1`kB non-grants | **`Gap 421`** |
| the `404: Not Found` body | `lib/probe_payload.sh:96` |
| a grant that is a reference, not a body | **`p742-grant-body-vs-reference`** |
| root-only ladder reach | **`p969-root-only-licence-reach`** |
| owner-case slug variants | `repos/foundations.md:325` |

🔴 **`compose/patterns.md:867` even states the conclusion in advance: *"Both pass a body-matching
classifier as `MIT`."*** 🟢 **So the contribution is TRIAGE, not discovery** — the band reaches
these classes from a number the census already holds, with no extra fetch, at `0` false
negatives against ground truth this KB built by hand. 🔴 **p194 registered the cause of this
waste one pass ago — *"it read p193's summary table as the state of knowledge"* — and p195 read
its own census TSV the same way. Second consecutive recurrence.**

🟢 **`P0a` in [`compose/patterns.md`](../../patterns.md) is the gate that would have stopped it,
and it now runs before any instrument is written.**

## 🆕 🟡 The shared suite's score is cwd-dependent, and the number must be quoted with its cwd

🔵 Measured this pass, because p195 ran the suite from two directories and got two answers:

| invocation | result |
|---|---|
| `cd compose/code/lib && bash test_license_family.sh` | 🟢 **`207`/`207`** |
| `bash compose/code/lib/test_license_family.sh` *(from the repo root)* | 🔴 **`179`/`181`** |

🔴 **Two fixture-presence guards fail from the root** — `P854 fixtures-p854 presente` and
`T232 fixtures de p173 presentes` — because they resolve fixture directories relative to `cwd`.
🟡 **And the total itself moves, `181` against `207`: the `26` assertions those fixtures feed
never run at all.**

🟢 **This is NOT a classifier regression, and the guards are the reason we know:** they failed
**loudly** on absent fixtures instead of passing silently on an empty corpus, which is exactly
what `P126-2` requires of a negative control. 🔵 The shape is already registered as
[`p355-cwd-portability`](../p355-cwd-portability/); this is a measured instance of it **in the
shared library's own suite**.

🔴 **Rule for the passes that follow: never quote `207`/`207` bare.** Quote it as
*"`207`/`207`, run from `lib/`"*, or run the suite from `lib/` and say so. An unqualified score
is an inherited figure, and this pass exists partly to stop inheriting figures.

## Declared limits

| limit | detail |
|---|---|
| 🔴 **root only** | `19` filenames at the repository root. `OS4ED/openSIS-Classic` returns `NONE` here and carries `GPL-2.0` *(`17 286` B)* at `docs/License.txt`. **`18.8`% is an upper bound on absence** |
| 🔴 **permissive only** | `band_of_family` returns `NO-BAND` for `AGPL-3.0`, `GPL-3.0`, `ECL-2.0`, so the delivery column says `GO-SUBJECT-TO-FAMILY`, **not `GO`**. The **`77` copyleft rows are unchecked for `P1054`-style narrowing** |
| 🔴 **the denominator is inherited and wrong** | the population comes from p192's `472`-slug extraction. **Four rows on p193's own ranked `30` are absent from it**, all four marked 🆕 NEW by p193, and `ShuyunYuan/talentcoach` ≡ `shuyunyuan/talentcoach` is one repository, so the distinct count is `467` |
| 🟡 **stars are not here** | the raw lane returns file contents, not `stargazers_count`. Star figures came from `mcp__github__search_repositories` in two batched calls |
