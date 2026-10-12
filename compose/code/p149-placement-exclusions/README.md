---
industry: education
region: Global
updated: 2026-10-12
---

# `p149-placement-exclusions` — two registered exclusions, and the host neither of them named

🔵 **`ACTION EZ` and `ACTION FA` are implemented here together and measured separately**, because
they share a code path and have different falsifiers. 🔴 **One is refuted, and it is refuted by
a host that the other action was written to catch and does not.**

    python3 placement_exclusions.py --exclude none|edu|platform|both|noninst <clone-root>...
    python3 test_placement_exclusions.py     # 26 tests, authored fixtures, offline

## The measurement

🟢 **50 clones, 50 of 50 `git clone` OK.** The 44-row column is `ACTION ER`'s population, so it
is the one the falsifier is judged on.

| mode | what it excludes | 44: placed / CONFLICT / UNPLACED | 50: placed / CONFLICT / UNPLACED | `ER` **DISAGREE** |
|---|---|---|---|---|
| `none` | nothing — 🟢 **the reproduction control** | 27 / 3 / 14 | 28 / 4 / 18 | **1** |
| `edu` | 🟢 **`ACTION EZ`** — bare `.edu` | 28 / 1 / 15 | 30 / 1 / 19 | 🔴 **1** |
| `platform` | 🟡 **`ACTION FA`** — its six named hosts | 27 / 3 / 14 | 27 / 4 / 19 | 🔴 **1** |
| `both` | `EZ` + `FA` | 28 / 1 / 15 | 29 / 1 / 20 | 🔴 **1** |
| `noninst` | 🔵 **+ dev-tooling — beyond both actions** | 27 / 1 / 16 | 28 / 1 / 21 | 🟢 **0** |

🟢 **`--exclude none` reproduces `p147-npm-region` row for row on all 44**, region and host
alike, and that is pinned as a test rather than asserted in prose. 🟢 **The pre-exclusion probe
is not modified**, so its published figures stay reproducible; this module substitutes its host
classifier for the duration of a call and restores it, including on exception.

## 🔴 `ACTION EZ` — REFUTED, and the refutation is the pass's finding

> 🔴 *Refuted if `DISAGREE` is still non-zero after the exclusion.*

🔴 **It is still 1.** The exclusion did what it was supposed to do — `felipedias-ie/blackboard-mcp`
stops being placed on `bb.edu` and becomes `OFFSET_ONLY` — 🔴 **but a second row took its place**:

| row | institution | offset | the host |
|---|---|---|---|
| `BetterSEQTA/DesQTA` | **EMEA** | **APAC** | 🔴 **`sh.rustup.rs`**, from `docs/development/build-deployment.md` |

🔴 **`sh.rustup.rs` is the Rust toolchain installer.** Its `.rs` is Serbia's ccTLD; the subject is
Australian; the line it was read from is a `curl … | sh` install instruction. 🔵 **The row was
`INSTITUTION_CONFLICT` before the exclusion, so the bad placement existed and the `CONFLICT`
state was masking it** — removing the bare `.edu` did not create the disagreement, it
*uncovered* one. 🟢 **That is precisely what `EZ`'s consequence clause said a refutation would
mean**: *"the institution-versus-offset conflict is real on some row this pass attributed to a
placeholder."*

## 🟡 `ACTION FA` — NOT refuted, but its boundary is wrong

> 🔴 *Refuted if no placement changes.*

🟢 **One placement moves**: `ahmedEid1/lumen`, **EMEA → UNPLACED**, on `youtu.be`. So `FA` stands.
🔴 **But the exclusion it specifies does not catch `sh.rustup.rs`**, and five of its six named
hosts could never have placed a row in the first place:

| host | suffix | in `CCTLD`? | could it ever place? |
|---|---|---|---|
| `youtu.be` | `.be` | 🔴 **yes → EMEA** | 🔴 **yes — this is `T70`** |
| `youtube.com` | `.com` | no | 🟢 never |
| `bit.ly` | `.ly` | no | 🟢 never |
| `t.co` | `.co` | no — deliberately omitted as repurposed | 🟢 never |
| `goo.gl` | `.gl` | no | 🟢 never |
| `github.io` | `.io` | no — deliberately omitted as repurposed | 🟢 never |

🟢 **So `CCTLD`'s decision to omit repurposed suffixes was load-bearing and nobody had measured
it.** `FA` is a guard against a future shortener on a mapped ccTLD, not a correction of five
live defects — and it is still worth having, because `.be`, `.me`, `.ly`, `.gl`, `.co` and `.to`
are sold as vanity suffixes *precisely because they read as words*. 🟢 **The rule names hosts,
not suffixes**, so it cannot cost a real `.be` or `.rs` institution its placement — pinned by
`test_a_real_serbian_institution_is_not_dev_tooling` and `test_a_real_institution_is_not_a_platform`.

## 🔵 `noninst` — the class, measured past both actions

Adding the two dev-tooling hosts (`rustup.rs`, `sh.rustup.rs`) 🟢 **takes `DISAGREE` to 0** and
🟢 **lifts two-channel coverage from 37 to 39 of 44**:

| row | `none` | `noninst` |
|---|---|---|
| `BetterSEQTA/DesQTA` | `INSTITUTION_CONFLICT` | `OFFSET_ONLY` |
| `MartinSA04/ntnu-mcp` | `INSTITUTION_CONFLICT` | 🟢 **`INSTITUTION_ONLY`** (EMEA, `www.ntnu.no`) |
| `felipedias-ie/blackboard-mcp` | 🔴 `DISAGREE` | `OFFSET_ONLY` |

🔴 **This is reported as a diagnostic, not as a discharged action.** It is not what `EZ` or `FA`
registered, and a mode invented in the same pass that measures it is not evidence the register
can spend. 🟢 **What it does establish is the cause, by name**, so the next action can be written
against a measured class rather than a hunch.

## 🔴 The class is larger than two kinds, and here is the count

🟢 **One `CONFLICT` survives every mode** — and it is not ambiguity:

`BetterSEQTA/BetterSEQTA-Plus` carries **12** placing hosts. 🟢 **3 are the subject's own and
all say APAC** (`www.seqta.com.au`, `other.seqta.com.au`, `apps.sace.sa.edu.au`). 🔴 **9 are news
media**, spanning four regions: `feeds.bbci.co.uk`, `www.nrc.nl`, `www.dutchnews.nl` (EMEA),
`www.cbc.ca` (North America), `www3.nhk.or.jp`, `rthk9.rthk.hk`, `news.ltn.com.tw` (APAC),
`critica.com.pa`, `www.panamaamerica.com.pa` (LATAM). 🔵 **The row's `CONFLICT` is an RSS fixture
list**, and the offset channel's APAC is right.

🔵 **And a fourth kind, which costs nothing here but is the same defect**: `alejooroncoy/campus-cli`
carries **17** Peruvian government-portal hosts under `.gob.pe`. 🟢 **Its LATAM placement is
correct** — Peru — and it is correct *by the strongest channel*, a hardcoded
`aulavirtual.upc.edu.pe`. 🔴 **The government hosts are not institutions either**, and on a
subject without that hardcoded host they would have decided the row.

🔵 **The honest statement of `T70` after this pass**: the institution channel has no notion of
*whether a host is an institution*. It asks only whether the host carries a nationally-bound
suffix. 🟢 **Four non-institutional kinds are now measured on this shelf** — platform/shortener,
developer tooling, news media, government portal — 🔴 **and only the first two are excluded.**

## 🟢 What a bare `.edu` is now

🔴 **Never a placement.** 🟢 **Always reported**, in a `lead` column, so the evidence survives the
demotion. Six subjects carry bare-`.edu` leads; `alejooroncoy/campus-cli` alone holds five, and
they are 🔴 **not one country**: `dspace.mit.edu`, `utsystem.edu`, `advising.yalecollege.yale.edu`
and `www.artic.edu` are US, 🔴 **`cv.uoc.edu` is Universitat Oberta de Catalunya, Barcelona.**
🟢 **A single row containing both is the cleanest demonstration `T67` has produced** that the
suffix carries a registration date and not a country — and the old rule would have called all
five North America without raising a `CONFLICT`, because it mapped every bare `.edu` to one region.

## Files

| file | what it is |
|---|---|
| `placement_exclusions.py` | the module; five modes, one of them the reproduction control |
| `test_placement_exclusions.py` | **26 tests**, authored fixtures, offline |
| `result.44.<mode>.2026-10-12-p149.tsv` | placements over `ACTION ER`'s 44, per mode |
| `result.50.<mode>.2026-10-12-p149.tsv` | placements over all 50 clones, per mode |
| `agreement.44.<mode>.2026-10-12-p149.tsv` | `p148-channel-agreement` re-run, per mode |
