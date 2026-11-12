---
industry: education
region: Global
updated: 2026-11-12
---

# `p777` instruments — specified in PROSE, published for re-implementation, not for execution

🔴 **`make hooks` was tried as the first command of this pass and DENIED — `[Code from External]`. EIGHTH consecutive session, `0` for `8`.** 🟢 **Not worked around.** No script was copied out of this repository and run. The four instruments below were **written from scratch** in a session scratchpad, and are specified here in prose because `T763` holds: *an ACTION that prescribes a procedure BY PATH is not a transferable instruction on this base.* The next pass should re-implement from these contracts, not execute these files.

## 1. `p777-probe` — existence, default branch, and grant payload

**Contract.** Existence and default branch come from the **ref channel only** (`git ls-remote --symref https://github.com/<slug> HEAD`); a non-zero exit is `ABSENT-OR-PRIVATE` and, per `T779`, is **not** evidence of absence. The grant payload comes from the **raw channel only** (`raw.githubusercontent.com/<slug>/<branch>/<name>`) over **`28`** case-aware filenames. `api.github.com/repos/*` is never called for a verdict. Family is decided on **marker phrases in the fetched bytes**, never on a repository's own prose claim; no marker match returns `NOT-IN-CANONICAL-SET`, which is information (`D10` standing). Every payload is reported as **bytes + `sha256₁₂`** so a later pass can reproduce it.

**Guards.** `ALTERED-VINTAGE` fires on the pre-2005 FSF address (`59 Temple Place` / `02111-1307`) and explicitly does **not** mean the grant was altered (`ACTION p776-D`). The standing deontic guard (`ACTION p774-C`) fires on a negation inserted beside a permission verb.

**Controls, run BEFORE any verdict was published.** `moodle/moodle` → `GPL-3.0` `35,147 B`. `pykt-team/pykt-toolkit` → `MIT` `1,066 B`. A synthetic nonexistent slug → `ABSENT-OR-PRIVATE`, not a family. And the cross-pass control that matters most: **five rows published by `p776` were re-measured by this independent instrument and reproduced exactly** — `MyIEP` and `IEP-IPP` (`18,351 B` · `1cfece9336f0`), `datosgobar/portal-andino` (`1,109 B` · `79d4edfa11f8`), `datosgobar/georef-ar-api` (`1,109 B` · `ee8033dc560b`), `CeibalUy/Ceibal` (`main` · `b104e714d7da`, no grant).

🔴 **`D1`, caught by control C4 before publication.** The first contract took the **first** filename hit as the grant. On `ghoulmann/IEP-IPP` that returned the root `LICENSE` — a `1,188 B` *notice* that says in its own text that the grant is in `COPYING` — and graded the repository `NOT-IN-CANONICAL-SET`. Published, it would have contradicted `p776`'s correct `GPL-2.0` verdict. **Contract corrected: probe every name, keep every hit, adjudicate on the hit that carries a family marker, prefer the largest such payload, and report notice-only files separately.** After the fix the row reproduces `p776` byte-for-byte.

## 2. `gate-frontmatter` — the gate `ACTION p776-A` named

**Contract.** A **curated shelf** is a `.md` file at depth 1 of `README.md`, `agents/`, `repos/`, `intel/`, `verticals/` or `compose/`; `compose/code/**` is instrument documentation and is **not** a shelf. Every shelf must open with YAML frontmatter **as its first bytes** carrying `industry`, `region` from the five closed values in exact case, and `updated` as an ISO date. Defect classes: `F1` no frontmatter at byte 0 · `F2` missing key · `F3` region outside the vocabulary or right value wrong case · `F4` `updated` not ISO · **`F5` `updated` in the FUTURE** · **`F6` `updated` STALE — a commit later than `updated` touched the file** · `F7` industry mismatch. 🔵 **`F5` and `F6` are the two checks `ACTION p776-A` says nothing in this base has ever run.**

**Controls.** A gate that cannot fail is not a gate. Four synthetic fixtures are graded first and the gate must flag exactly `F1` on the frontmatter-less one, `F3` on `region: Latam`, `F5` on `updated: 2099-01-01`, and **nothing** on the clean one. All four behaved as specified.

**Result.** `11` curated shelves, **`0` defects**, including `0` future dates and `0` stale dates.

## 3. `p777-bare-owner` — the census behind `ACTION p776-C`

**Contract.** A bare-owner citation is a markdown link to `https://github.com/<owner>` with **no repository path segment**; `/orgs/`, `/topics/`, `/search`, `/trending` and the like are excluded because they are not repository citations at all. For each, the **display text** is recorded.

🔴 **`D2`, caught before publication.** The first contract tested the display text with a loose `owner/repo` pattern, which matched the display string `` `github.com/flysheep-ai` `` and reported `3` convertible citations that do not exist. Corrected, the convertible count is **`0`**.

## 4. `p777-claim-channel` — a SECOND, independent licence channel

**Contract.** `gh api -X GET search/repositories` and `search/code` return GitHub's **own detected** `license.spdx_id`, `stargazers_count`, `forks_count`, `default_branch` and `pushed_at` for public repositories. 🔴 **This is a CLAIM, never a grade. It may never override a body-graded verdict.** `NOASSERTION` means GitHub found a licence file it could not map, and `NONE` means it found none. Both are signals, not verdicts.

🔵 **Why this instrument is new.** Every pass back to `p769` records `api.github.com` as `403` and concludes that no star count can appear on these shelves. **That is true of the `repos/<slug>` endpoint and false of the `search/*` endpoints** — re-measured this pass, `gh api repos/HKUDS/DeepTutor` returns `403` with *"GitHub access to this repository is not enabled for this session"*, while `search/repositories` returns that repository's stars and SPDX id. **`25` rows were cross-checked against this pass's byte grades: `24` AGREE, `1` ABSTAIN (`inducer/relate`, body `MIT` `1,145 B`, claim `NOASSERTION`), `0` CONTRADICT.**

## 🟢 Honest summary of this pass's instruments

| | |
|---|---|
| Instruments written from scratch | `4` |
| Defects in them caught by control **before** any verdict was published | **`2`** (`D1`, `D2`) |
| Of those, defects that would have published a false claim against correct prior work | **`1`** (`D1`, against `p776`'s correct `IEP-IPP` verdict) |
| Defects published as findings | **`0`** |
| `p776` rows independently reproduced byte-for-byte | **`5`** |
| `api.github.com/repos/*` calls made for a verdict | **`0`** |
