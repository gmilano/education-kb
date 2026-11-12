# `p781` instruments

🟢 **`make hooks` ran as the FIRST command of this pass and SUCCEEDED** — exit `0`, in `/home/user/globant-kb`,
the repository `CLAUDE.md` names. `1` for `12`.

🔴 **And the eleven-pass "environment block" was a working-directory error.** Both arms were measured:

| Arm | Command | Result |
|---|---|---|
| 🟢 `/home/user/globant-kb` | `make hooks` | 🟢 ALLOWED, exit `0` |
| 🔴 `/tmp/education-kb` (the clone) | `make hooks` | 🔴 DENIED `[Code from External]` |
| 🔴 `/tmp/education-kb` | `python3 compose/code/p779/gate_refs_cohort.py .` | 🔴 DENIED, identical reason |

🔵 **`T818`: the denial is scoped to executing code that came from the cloned EXTERNAL repository.**
🔴 **Consequence for every future action list: an instruction to "reuse `p779`'s gate" is UNEXECUTABLE.**
`ACTION p780-A` ordered exactly that, so the cohort gate below was written from scratch **under duress**,
not by preference.

## 1. `rename-sweep` — `T810` at scale, as a SET-DIFFERENCE detector

🟢 **A cheaper instrument than `p780-B` specified, found by measuring the channel instead of assuming it.**
`p780-B` ordered one `repo:` call per slug: `5,817` calls, ~`3` hours at `30`/min.

**Measured behaviour:** a `search/repositories` query carrying `N` `repo:` qualifiers returns **exactly the
slugs that exist** and **silently DROPS** the dead ones. HTTP `422` fires **only when every slug in the batch
is dead**. 🟢 **So requested-minus-returned is the dead set: `146` calls at `batch=40`.**

🔵 `40` qualifiers is `1,060` characters and is served — **the documented `256`-character query ceiling does
not bind `repo:`-qualified search.**

**Four controls, all blocking, all run before any target:**

1. `C1` an all-alive batch returns `4`/`4` (`DeepTutor`, `moodle`, `oppia`, `frappe/education`).
2. `C2` a batch carrying exactly one known-dead slug **isolates that slug** (`openedx/edx-platform`).
3. `C3` an all-dead batch is detected as `422` and **sub-probed by bisection**, never recorded as alive.
4. `C4` `total_count` must equal `len(items)` or the batch is **truncated** and is re-split.

🔴 **Fails SAFE: any unrecognised error marks the batch ALIVE.** A sweep must never manufacture a death.

🟢 **It found `2` deliberate `this-repo-does-not-exist` control slugs the base already carried, and flagged
both** — a positive control nobody had to plant.

🔴 **This instrument's own defect, caught by control and reported:** the slug extractor matched
`github.com/<a>/<b>` inside **API-path and placeholder prose**, manufacturing `15` dead "repositories".
**Rule stated so the next pass does not re-find them:** a slug whose owner is a GitHub API path segment
(`repos/HKUDS`, `search/repositories`) or whose halves are both metasyntactic (`owner/repo`, `a/b`, `X/Y`)
is prose, not an address. 🟢 **`378` published, not `393`.**

## 2. `split-dead` — the two-channel death classifier

🔵 `git` follows GitHub's rename redirect; the claim channel does not. **That disagreement is the instrument.**

| `repo:` search | `git ls-remote` | Class |
|---|---|---|
| miss | 🟢 OK | **RENAMED-OR-UNINDEXED** — content alive, address stale |
| miss | 🔴 FAIL | **DELETED-OR-PRIVATE** — gone |

🟢 **Both controls passed:** `openedx/edx-platform` → RENAMED; the planted `this-repo-does-not-exist` slug →
DELETED. 🟢 **Result: `268` / `110`.** 🔵 **`71%` of this base's address rot is repairable by rewriting an
address rather than re-researching a repository.**

## 3. `grant-read` — `L56`, bytes on disk, title-line grading

`L56` = **`7` stems × `4` extensions × `2` cases = `56`**, asserted in code (`assert len(L56) == 56`).

- **stems:** `LICENSE` `LICENCE` `COPYING` `COPYRIGHT` `NOTICE` `LICENSE-CODE` `LICENSE-MIT`
- **extensions:** *(none)* `.md` `.txt` `.rst`
- **cases:** the stem as written, and the stem lower-cased

🔴 **`p780`'s lesson obeyed: bytes are measured on the file ON DISK**, never through command substitution,
which strips trailing newlines and under-counts by `>=1`. (`p780` retracted its `v1` for exactly this.)

🔴 **An absence verdict always carries the count of names tried** — `NO-GRANT-AT-ROOT-after-56-names`.

**Control:** `HKUDS/DeepTutor` must reproduce `11,408 B` · `cd2f54e1e506`. 🟢 It did, exactly, for the third
consecutive pass, at a `HEAD` that had moved.

🔴 **TWO defects in this instrument, both caught by control, both corrected before publication:**

| Defect | Caught by | Cause |
|---|---|---|
| 🔴 `frappe/erpnext`'s **GPL-3.0** graded as **AGPL-3.0** | The title line, and the claim channel, which both say `GPL-3.0` | 🔴 **GPL-3.0's own §`13` contains the literal string *"GNU Affero General Public License"***, so ANY substring test for "Affero" mis-grades every GPL-3.0 print |
| 🔴 `CaviraOSS/PageLM` graded **MIT** | `p779`'s published non-OSS grade, whose bytes this pass reproduced EXACTLY (`8,563 B` · `c834209c5f33`) | 🔴 A substring test for the MIT permission sentence fires on *"PageLM Community License"*, `8,563 B`, `13` restriction-bearing lines. **`p779` was right** |

🔵 **`T822`, recorded from both: grade on the TITLE LINE — never a body substring, never length.**
🔴 **The length evidence is severe: GPL-3.0 prints measure `35,147`–`35,149 B`; `openedx/openedx-platform`'s
AGPL-3.0 print measures `35,136 B`. `11` bytes apart.**

## 4. `gate_refs_p781` — the AMENDED `T809` cohort gate

🔴 **Written from scratch because `p779`'s is unrunnable (`T818`), not because `p780-A` permitted a rebuild.**

**Amended test, exactly as `p780` specified it:** a row is **PRIMARY** only if it is the **FIRST assertion**
of a given grade for a given repository, in **pass order**. A row restating an established grade is
**DERIVED** however much evidence it quotes.

- A row is considered only if it is a table row (starts with `|`) and is not a `|---|` separator.
- The `p778-F` institution list (`mitodl`, *"MIT Media Lab"*, *"MIT Sloan"*, …) is masked **before** licence
  matching, so `MIT`-the-institution is never read as `MIT`-the-licence.
- 🔴 **A ref is `` `<branch-NAME>` · `<12-hex>` `` where the first token carries LETTERS.** A byte count
  followed by a `sha256₁₂` has the identical shape and is **rejected**; so is a `hex · hex` pair.
- Cohort is the nearest preceding `## ` heading containing a `` `pNNN` `` token.

🔴 **Result, and it REFUTES the finding `p780` used `T809` to establish:** cohort `p770`–`p780` PRIMARY
`85` rows / `61` with a ref = **`71.8%`**; DERIVED `426` rows / `314` with a ref = **`73.7%`**.
🔴 **`p780` published *"DERIVED: `0` with a ref — `0.0%` in EVERY cohort pass without exception"*. Under the
amendment `p780` itself ordered, DERIVED rows carry refs slightly MORE often than PRIMARY rows do.**
🟢 **So the split never measured falsifiability; `p780`'s `0.0%` was an artefact of a definition that
classified every ref-carrying row as PRIMARY by construction.**

🟡 **Honest limit: this gate's row definition is not `p779`'s or `p780`'s, so none of the three aggregate
figures are comparable, and no claim is made that any reproduces another.**

### `ACTION p780-G`, carried here as ONE added check

The newest `## ` section of each shelf must **name the current pass**, and the shelf's YAML `updated:` must
**equal the date in that heading**.

🔴 **This check found its first defect IN ITSELF, for the third consecutive pass.** Its first run after
`p781`'s writes reported `intel/market.md` as `heading-date 2027-12-02 != updated: 2026-11-12`. **FALSE:**
`2027-12-02` is the **EU AI Act deadline quoted in that shelf's headline prose**, and the date regex had
taken the first date-shaped string anywhere in the heading. 🟢 **Fixed: the date is read only from the
heading's PASS-MARKER zone — the text before the first bold marker. All `10` shelves then return `0`
defects.** 🔵 `p779-G` found its first defect in `gate-refs`, `p780-G` in the pass-detector, `p781` in the
date-extractor: **a check that walks headings keeps being defeated by the headings' own prose.**

🟢 All `10` shelves pass after this pass's writes. 🔴 **And the heading-date arm is only ENFORCEABLE on `3` of
`10` shelves** — `agents/trending.md`, `repos/trending.md` and `README.md` put a date in the heading; the
other `7` do not, so for them the check is **vacuous**. 🔵 **A check that cannot fail on `70%` of its
population is not yet a gate** → `p781-G`.

## 5. `walk-attw` and `walk-estate` — bounded licence-history walks

🔴 **`T813` obeyed: default branch only.** Generated publication refs carry licence files as build output.
🔴 **`T814` obeyed: a bounded walk reports UNFINISHED, never `0`.**

`git clone --filter=blob:none --no-checkout --single-branch`, then
`git log --diff-filter=AMDR --name-status` over `*LICENSE*` `*LICENCE*` `*COPYING*` and lower-case forms.

🟢 **`apply-for-teacher-training` (`34,516` commits — reproduces `p780` exactly) FINISHED** where `p780`'s
walk had not: `0` licence events since `2026-01-01` **at exit `0`, a genuine zero**, and exactly `1` event in
the entire history (`98f407766` · `2020-03-16` · *"Create LICENSE"* · adds `LICENCE`).

🟢 **`openfun`, `8` repositories, `0` unfinished.** 🔵 **`T813` extended by this run: the
publication-artefact class is not confined to generated refs — `openfun/edx-theme`'s only licence events are
`templates/static_templates/theme-licenses.html`, a Django template that RENDERS a licences page, and
`openfun/richie`'s are a Django licence DATA MODEL (indexers, viewsets, migrations, tests).** 🔴 **A walker
that globs `*licence*` across a web application finds pages, views and tests instead of grants.**

## 6. Canonical-corpus comparison (`ACTION p780-C`)

🔴 **`cecill.info` and `www.gnu.org` are blocked.** 🟢 `www.apache.org` and `spdx/license-list-data` work.

**Method that resolved the `learnharness` print:** compare raw bytes, then compare again with **all
whitespace stripped**. `34,523 B` vs `34,020 B` is `503 B`; whitespace-stripped it is `28,156` vs `28,153` —
**exactly `3` bytes**, the three `http://`→`https://` scheme updates. `0` CR bytes (**not CRLF**, the same
negative `p779` found for CECILL); `661` newlines vs `235` (**hard-wrapped**); `0` deontic operators differ.

🔵 **`T817`: a canonical byte count is CHANNEL- and FORMATTING-specific, not merely language-specific.**
`Apache-2.0` is `11,358 B` · `cfc7749b96f6` at `www.apache.org` and `10,280 B` · `074e6e32c86a` at SPDX —
`1,078 B` apart in the same language. 🔴 **So a corpus holding one canonical per licence manufactures false
bespoke-licence alarms, and `p780-C`'s prediction that the cause would be TRANSLATION failed.**
