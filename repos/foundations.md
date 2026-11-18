---
industry: education
region: Global
updated: 2026-11-18
---

# Foundational repos — education

**Pass `p888`, 2026-11-18** (fifth pass of the day). **This shelf gains its first STANDARDS-layer
rows, and they came from a channel this KB had written off. `api.github.com/search/repositories`
answers `200`; `1,342` repositories this KB had never seen were returned; and when the new rows are
sorted by 12-month commit count, the top of the list contains no AI tutors at all — it contains LTI
1.3, SCORM/cmi5 and autograder plumbing.**

- 🟢 **`887-G4` DISCHARGED.** 56 legs, `0` leg errors, **`1,620`** distinct repositories, **`278`**
  already held, **`1,342`** new, **`36` byte-read with `0` fetch failures**
  ([`grants`](../evidence/grant-verify-888.2026-11-18-p888.tsv),
  [`legs`](../evidence/search-discovery-887G4.2026-11-18-p888.tsv),
  [`channels`](../evidence/channel-state.2026-11-18-p888.tsv)).
- 🟢 **`11,357 B / sha256₁₂ c71d239df917` is a confirmed fingerprint for unmodified Apache-2.0** —
  the **same bytes `p887` read on `apereo/phpCAS`**, now seen on three further unrelated repositories
  (`ali-kin4/skillgraph-tutor`, `jasonswrench-beep/openstage-package-doctor`,
  `Vernum-Projecten/eduLIMS`). 🔴 **Its absence proves nothing**: `11,358 B`, `11,354 B` and the
  appendix-stripped `10,174 B` were all read this pass. **A byte-count test for "pristine" would
  have flagged three of six Apache rows as modified.**
- 🔴 **A third arity shape — DISJUNCTIVE.** `ad1-kamath/coursecraft` ships `LICENSE-MIT` **and**
  `LICENSE-APACHE` and declares `license = "MIT OR Apache-2.0"`. **GitHub metadata reports
  `Apache-2.0` alone.** Same `arity=2` as `p887`'s conjunctive rows; **opposite obligation**; and
  invisible to `p887`'s `NOASSERTION` detector, which only fires when metadata abstains.
- 🔴 **This pass mis-read two of its own rows first.** `slp-lab-research/higraph` and
  `ICICLE-ai/curriculum-generator` were reported conjunctive `BSD-2 + BSD-3`. **Both are
  single-family BSD-3-Clause.** `BSD-2`'s signature is **clause 2 of `BSD-3`** — a textual subset.
  **Family detection must test SUBSUMPTION, not presence** (`888-G3`, `9/9` controls green).

## 🆕 Standards & assessment foundations added in `p888` — byte-verified

🔵 **Why these belong on the foundations shelf rather than the agents shelf:** none of them is a
tutor. Each one is **plumbing a client engagement cannot avoid** — launch, roster, grade passback,
package export, autograding — and each has a permissive grant read as bytes.

| Repo | Grant (byte-read `2026-11-18`) | ★ | Commits 12mo | Region | Why it is foundational |
|---|---|---:|---:|---|---|
| [`parler-haut-interagir-librement/lti`](https://github.com/parler-haut-interagir-librement/lti) | **MIT** — `main/LICENSE`, **1,155 B**, `sha256₁₂ 2da07e888147` | 0 | 2 | **EMEA** | **LTI 1.3 for PHP on both sides** — a tool platforms launch *and* a platform that launches tools, from one configuration. 🔵 The both-sides property is what lets a pilot stand in for the client's LMS while that LMS is still being procured. |
| [`parler-haut-interagir-librement/lti-bundle`](https://github.com/parler-haut-interagir-librement/lti-bundle) | **MIT** — `main/LICENSE`, **1,155 B**, `sha256₁₂ 2da07e888147` | 0 | 2 | **EMEA** | Symfony binding of the above. 🟢 **Byte-identical grant to its sibling, confirmed rather than assumed.** |
| [`eddiethedean/lessonkit`](https://github.com/eddiethedean/lessonkit) | **Apache-2.0** — `main/LICENSE`, **10,174 B**, `sha256₁₂ 69849221bfb9` | 2 | **389** | 🔴 REFUSED | React-first framework emitting **xAPI, SCORM and cmi5**, with **accessibility as a stated design goal**. 🟢 **389 commits/12mo — the most actively maintained repository in this pass.** |
| [`jasonswrench-beep/openstage-package-doctor`](https://github.com/jasonswrench-beep/openstage-package-doctor) | **Apache-2.0** — `main/LICENSE`, **11,357 B**, `sha256₁₂ c71d239df917` | 0 | 9 | 🔴 REFUSED | Opens and **validates** any SCORM/xAPI/cmi5 package **without the source file**. 🔵 Turns a content-migration bid from a guess into an estimate. |
| [`ad1-kamath/coursecraft`](https://github.com/ad1-kamath/coursecraft) | 🔴 **DISJUNCTIVE `MIT OR Apache-2.0`** — `LICENSE-MIT` **1,081 B** `66d27c2a9dbf`; `LICENSE-APACHE` **10,174 B** `0d542e0c8804`; `Cargo.toml`: `license = "MIT OR Apache-2.0"` | 1 | 25 | 🔴 REFUSED | Clean-room eLearning **authoring** tool in Rust → SCORM/cmi5. 🔵 **Pick MIT and you owe no Apache `NOTICE`** — the practical consequence of disjunction. |
| [`PrairieLearn/grader-python-v2`](https://github.com/PrairieLearn/grader-python-v2) | **MIT** — `main/LICENSE`, **1,072 B**, `sha256₁₂ 0677c780ae82` | 1 | **110** | **North America** | Next-generation Python **autograder for PrairieLearn** (UIUC). 🟢 **Institutionally maintained under a university org.** |
| [`RichardMcQuiston01/reactive-lms`](https://github.com/RichardMcQuiston01/reactive-lms) | **MIT** — `main/LICENSE`, **1,073 B**, `sha256₁₂ d04e9814dca8` | 0 | **159** | 🔴 REFUSED | TypeScript LMS package, standalone **or** embeddable into an existing app. |
| [`Vernum-Projecten/eduLIMS`](https://github.com/Vernum-Projecten/eduLIMS) | **Apache-2.0** — `main/LICENSE`, **11,357 B**, `sha256₁₂ c71d239df917` | 0 | **112** | **EMEA** | **LIMS for practical teaching laboratories.** 🔵 A vertical this KB had no row for in any shelf. |
| [`ICICLE-ai/curriculum-generator`](https://github.com/ICICLE-ai/curriculum-generator) | **BSD-3-Clause** — `main/LICENSE`, **1,501 B**, `sha256₁₂ 5dbf2c09aee3` | 0 | **114** | **North America** | Curriculum generator from **ICICLE**, an NSF AI institute. 🟢 Institutional, BSD-3, live. |
| [`rendicahya/moodler`](https://github.com/rendicahya/moodler) | **MIT** — `main/LICENSE`, **1,078 B**, `sha256₁₂ 70d2e2219531` | 0 | 53 | 🔴 REFUSED | Browser editor for **Moodle quiz questions**. 🔵 Attaches to the platform already on `verticals/solutions.md`. |

🔵 **The one-line reading for a bid:** the **integration surface has live licensed OSS and the tutor
does not need to**. Build order should start at LTI/SCORM, not at the model.


**Pass `p887`, 2026-11-18** (fourth pass of the day). **`p887` discharged `886-G1` over the 15 rows
`p886` left open — `64,641` paths tree-enumerated, `0` failures — and this file took TWO corrections
from it: one its OWN instruments had been carrying since `p314`, and one that had been hiding one
file over from a row this file already had right.**

- 🔴 **`apereo/phpCAS` (`:465`) was published single-family `Apache-2.0` and is CONJUNCTIVE.**
  Apache-2.0 at `master/LICENSE` (**11,357 B**, `sha256₁₂ c71d239df917`) **and** a complete **New
  BSD** body at `master/NOTICE` (**3,914 B**, `sha256₁₂ 2df146a253fa`), headed *"Requirements for
  sources originally licensed under the New BSD License"*, © 2003-2007 **The ESUP-Portail
  consortium**, no-endorsement clause naming JA-SIG, Inc. 🔵 **This file's own note at `:748` says a
  single-family label on its sibling `java-cas-client` "would be wrong" — and the single-family label
  sat 277 lines above it.** The two repositories differ only in which FILE holds the BSD half.
- 🟢 **`jupyterhub/jupyterhub` (`:533`) corrected from bare `BSD` to `BSD-3-Clause`, and this base's
  own instrument is what caught it.** `compose/code/p314-untitled-payload-arm/README.md:12` has
  recorded `BSD-3-Clause` for this row since `p314`; the metadata channel returned `BSD-3-Clause`
  independently this pass. 🔵 **`p314` also explains the under-specification rather than just fixing
  it:** that payload is a complete, valid grant with **no title line and zero `BSD` tokens anywhere
  in the file**, so any title-matching classifier can only reach the family by inference. This is
  `886-G5`'s **one** finding out of `206` instrument claims.
- 🔴 **`ox-it/wl-roster2` (`:116`) is DORMANT, measured rather than inferred.** `884-G3`'s channel
  came back this pass (`search/commits`, `200` after two passes at `422`) and this row has **`0`
  commits in 12 months** against `pushed_at 2016-06-03`. The shelf said *"zero stars and a
  Sakai-10-era branch"*; it can now say zero commits.
- 🟢 **`yetanalytics/lrsql` (`:295`) CONFIRMED by an independent channel.** This file published
  *"67 commits in the last 12 months"*; `search/commits` returned **`67`**. 🔵 **Recorded because
  this base gets this outcome least often and should say so when it does.** 🔴 **Its `NOTICE` is
  19,985 B and names `21` distinct copyright holders** — the licence cell is `Apache-2.0` and
  correct; the **notice obligation is of 21**.
- 🟢 **Every other licence cell this file publishes for the 15 swept rows survived tree enumeration
  intact**, including the two `LICENSE.TXT` rows (`openedx/XBlock` `:408`, `openedx/codejail`) that
  `p885`'s root-only ladder reported as `NO-GRANT-FILE`. 🔵 **`arity_own = 1` on 14 of 15**; the one
  exception is `deepseek-ai/deepseek-harness` (MIT root, BSD-3-Clause `native/system/`, Apache-2.0
  `packages/experimental/subagent-oar/` — a genuine per-directory grant across 22,127 paths).

**Previous pass (`p886`), retained:** **Pass `p886`, 2026-11-18** (third pass of the day). **`p886` ran `885-G1`'s two-channel test over all
163 shelf rows. This file's cells survived it intact — and the two rows the gate called
`NO-GRANT-FILE` are two rows this file already had right, which is the pass's real finding about the
instrument rather than about the shelf.**

- 🟢 **`885-G1` EXECUTED over 163 rows: `144` AGREE (88.3%), `13` BYTES-ONLY, `4` BOTH-ABSENT, `1`
  DISAGREE, `1` unrecognised; `0` in `885-G1`'s own `FIELD-ASSERTS-PAYLOAD-DENIES` class**
  ([`record`](../evidence/dual-channel-885G1.2026-11-18-p886.tsv)). 🟢 **`0 / 163` default-branch
  disagreements** between `search/repositories` and `git ls-remote --symref` — the symref fix `p885`
  shipped for `884-G2` is confirmed sound on 30× the population it was built on.
- 🟢 **The permissive share of this estate, measured on BYTES rather than on metadata: `128 / 163` =
  78.5%.** Compare the metadata channel's own view of the same 163 rows: it reports `NOASSERTION` or
  `null` on **18** of them, and the bytes carry a real grant in **13** of those, so **a
  metadata-only census would have undercounted the known-grant estate by 13 rows** it cannot see a
  grant for. 🔵 **`T14` is not a curiosity; it is a systematic
  undercount, and this is the first pass to put a number on its size.**
- 🔴 **`LICENSE.TXT` is missing from `p885`'s shipped ladder, and it manufactured an absence on this
  file's own rows.** `repos/foundations.md:408-409` records
  [`openedx/XBlock`](https://github.com/openedx/XBlock) and
  [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) as **Apache-2.0 (`LICENSE.TXT`)**, and
  `:758` already names the uppercase-extension trap. `p885`'s
  `compose/code/p885-symref-grant-ladder/fetch_grants.sh:40` probes eight paths and **`LICENSE.TXT`
  is not one of them**, so it returns `404 / no-grant` on both. Re-read this pass:
  **Apache-2.0, 11,358 B, `sha256₁₂ cfc7749b96f6`, `master/LICENSE.TXT`, byte-identical across both
  repositories.** 🔵 **The shelf was right and the verifier could not reproduce it** — repaired with
  12 controls in `compose/code/p886-dual-channel-grant/licence_paths.sh`.
- 🔴 **A false ABSENCE on this estate, carried for ~611 passes while this KB's own module held the
  refutation.** `OS4ED/openSIS-Classic` is published on three live shelves as having *"no licence
  file at all"* / *"GPL per README; no licence file"*. **Its grant is GPL-2.0, 17,286 B,
  `sha256₁₂ 224ac3d403e3`, at `master/docs/License.txt`** — re-read first-hand this pass and
  confirmed by tree enumeration. 🔴 **`compose/code/pass275-grant-enumeration/`'s README names this
  exact repository and this exact path as the case it was built on.** The gate was right, the shelves
  were wrong, and nothing carried the finding across. 🔵 **`T13` (propagation, not discovery, is the
  binding constraint) demonstrated on a live cell.**
- 🟡 **Tree enumeration is the structural answer to path guessing, and it is ALREADY here** — **91**
  instruments use `--filter=blob:none`, **104** use `ls-tree`, `compose/code/p215-lstree-grant-recovery/`
  exists, `make enumerate` ships since `p275`, and `make ladder-audit` grades **919** ladders with
  **57** already `TREE-ENUMERATED`. 🔴 **`p885` shipped a new 8-path ladder regardless, and it
  regressed against `gate-ladder-case` (`p283`) and `gate-enumeration` (`p275`), both passing.**
- 🔴 **`886-G1`: four rows carry a grant whose arity is greater than one, and three of them scored
  `AGREE`.** `RWTH-OS/eduOS-rs` (`:666`, already correct here) is the only one the test could see,
  because disjunction across two files happens to produce a disagreement. Conjunction and
  per-directory grants do not. Full treatment: `agents/top.md` → **`## Licence arity`**.
- 🟡 **`iiab/iiab` (2,052 ★) is per-FILE, and this file's cell says `GPL-2.0`.** Its `LICENSING.md`
  (914 B, `sha256₁₂ b7ac7e43372f`) states that files **without** an explicit notice are GPL-2.0
  (© 2015-2026 Unleash Kids), while contributors are **encouraged to license their work under the
  GNU Library GPL v2 or later**. 🔵 **The cell is right about the default and silent about the
  rest**; for the offline-first patterns (`P5`, `P20`) the GPL/LGPL distinction is the whole
  linking question, so this row needs a per-file read before it is built against, not a re-read of
  its root `LICENSE`.
- 🔴 **`0` new repositories from the eight prescribed legs for the EIGHTH consecutive pass** — `63`
  facts, `63` held, `0` new ([`record`](../evidence/websearch-legs.2026-11-18-p886.tsv)). The
  platform leg (`open source platform education ERP CRM MIT Apache`) returned Apache OFBiz, Corteza,
  Krayin, iDURAR, iDempiere and Dolibarr and **the source itself states it found no MIT/Apache
  education-specific platform** — independent corroboration of this KB's standing nil, from a leg
  that was trying to refute it.
- 🔴 **`search/commits` `422` for the second consecutive pass → `884-G3` stays BLOCKED**; liveness on
  every row here remains **`HEAD ≥ date`** ([`record`](../evidence/channel-state.2026-11-18-p886.tsv)).

**Previous pass (`p885`), retained:** **Pass `p885`, 2026-11-18** (second pass of the day). **`p885` finished the sweep `p884` started and
the institutional category does NOT grow. It also found that this KB's grant probe was blind to one
repository in nineteen, and fixed it.**

- 🔴 **The institutional estate is fully enumerated now, and it adds `0` rows.** `p884` shelved 13
  LMS/SIS integration rows from a sweep it knew was truncated, and expected more behind the cap.
  `p885` paginated all 33 capped organisations to exhaustion — **`3,186` previously invisible
  repositories** — and the education-classified remainder is **coursework, not estate**: `362`
  TIER-A repositories of which **`327` (90.3%) carry no licence at all** and only `5` are both
  permissive and pushed within 12 months, all five teaching material
  ([`record`](../evidence/resweep-884G1.2026-11-18-p885.tsv)).
- 🟢 **The licence-absence rate is now measured on two independent populations and it AGREES.**
  `p884` measured 76.4% no-grant across 10,365 repositories from the top-100 slice. `p885` measures
  **90.3% no-grant across the 362 TIER-A repositories in the discarded tail**. 🔵 **The tail is
  *worse* licensed than the head**, which is the expected direction for coursework and is the
  clearest single argument for why a university's own GitHub organisation cannot be treated as a
  supply shelf without a grant gate in front of it.

### 🟢 Default-branch census — new in `p885`, and it repaired a real blind spot

Measured over all 6,486 repositories, not sampled:

| Default branch | Repos | Share |
|---|---:|---:|
| `main` | 3,976 | 61.3% |
| `master` | 2,166 | 33.4% |
| **neither** (`gh-pages` 151 · `sakai-10.x` 47 · `develop` 31 · `dev` 22 · `sakai_2-5-x` 14 · `development` 13 · `devel` 6 · `production` 4 · `principal` 4 · `trunk` 2 · 50 others) | **344** | **5.3%** |

🔴 **The two-name grant ladder could not see any of those 344 except by luck.** Narrowing to the
population where it costs something:

```
344 non-standard default branch
└── 201 carry a resolvable licence
    └──  49 are PERMISSIVE
        └──  13 have NO `main` and NO `master` at all   ->  reported NO-GRANT-FILE in error (26.5%)
```

🟢 **`compose/code/p885-symref-grant-ladder/fetch_grants.sh` resolves the default branch over
`git ls-remote --symref` and probes THAT ref first. It recovers 12 of the 13**, each via the symref
arm ([`controls`](../evidence/grant-ladder-controls.2026-11-18-p885.tsv)). The recovered grants are
real licence payloads, not inferred: MIT ×7, `ECL-2.0` ×1, Apache-2.0 ×1, BSD-2-Clause ×2,
SRI-Lab-copyright-first MIT ×1.

🟢 **The one that matters to this KB is a foundation, not a curiosity:**

| Repo | ★ | Licence (byte-read) | Default branch | Role |
|---|---:|---|---|---|
| https://github.com/ox-it/wl-roster2 | 0 | **`ECL-2.0`** — `sakai-10.x/LICENSE`, **11,110 B**, `sha256₁₂ 6001bb8caa76` | **`sakai-10.x`** | **Oxford's Sakai rostering component.** `ECL-2.0` is the Apache-2.0-derived licence written *for* education consortia and is build-safe. 🔴 **Zero stars, a Sakai-10-era branch, and — measured first-hand at `p887`, the first pass in three with a working `search/commits` — `0` commits in the last 12 months against a `pushed_at` of **2016-06-03**. DORMANT, not merely quiet.** This is a reference implementation of institutional rostering, not a dependency to pin. Its value is that it shows how a real university wired roster sync — see `compose/patterns.md` **P26**. |

🔴 **`885-G1`, found while discharging `884-G2`.** The thirteenth case,
[`ox-it/OxfordIDN_Case-Studies`](https://github.com/ox-it/OxfordIDN_Case-Studies), is **not** a
ladder failure: `license.spdx_id` is `MIT` and `license.key` is `mit`, the repository has exactly
**one** branch (`gh-pages`), and **no licence file exists on it at any probed path**. The metadata
channel asserts a grant the byte channel cannot confirm — the mirror image of this KB's Flowise row,
where the roundups claimed MIT and the SPDX field said `NOASSERTION`. 🔵 **Neither channel alone is
sufficient, and this KB has now measured a failure in each direction.** Filed in
`intel/open-gaps.md`.

**Previous pass (`p884`), retained:** **Pass `p884`, 2026-11-18** (first pass of the day). **`p884` rebuilt the owner register from a
PRIMARY source and swept 270 institutional organisations. The new supply is a layer this shelf did
not have — and the headline measurement is about the GRANT, not the code.**

- 🟢 **A new category, 13 rows: institutional LMS/SIS integration estates.** Swept by institution
  **display name** (`search/users`, not a guessed handle), **270 orgs / 10,365 repositories** across
  four regions. The permissive survivors are **not** agents and **not** research code — they are
  production plumbing: SIS importers, gradebook uploaders, Canvas API clients, Sakai/Tsugi tools,
  all at single-digit star counts and therefore invisible to every keyword and star-ranked leg this
  KB has run.
- 🔴 **76.4% of the education code universities publish carries NO GRANT AT ALL** (456 of 597
  education repositories, measured). 🔵 **And it is worst in EMEA (83.7%), best in APAC (54.3%)**,
  with LATAM at 74.4% — which **corrects `T10`**: "no grant" is a property of *university publishing
  practice*, not of the Global South.
- 🟢 **`cilt-uct` (University of Cape Town) is the best-licensed education estate in 884 passes** —
  50 repositories, **48 permissive** (`Apache-2.0` ×30, `ECL-2.0` ×16), a **96%** share against that
  76.4% norm, and it sits in the region with the *worst* regional rate.
- 🟢 **`cmu-db/bustub` — 5,171 ★, MIT, byte-read — is the highest-traction education repository this
  KB has found, and it was never carried.** CMU's teaching RDBMS, 2,085 forks of coursework.
- 🔴 **A new false-absence SHAPE, on this pass's second-highest find.** `RWTH-OS/eduOS-rs` (493 ★)
  reported **`NO-GRANT-FILE`** from a 16-path probe and reports `Apache-2.0` from GitHub's single
  `spdx_id`. It is **dual-licensed**: `LICENSE-APACHE` **and** `LICENSE-MIT`, the Rust two-file
  convention. **One grant field cannot express two grants.** Probe and classifier fixed, 5 controls.
- 🟡 **A third probe limit, declared:** `cilt-uct/sakai-skin-vula`'s default branch is **`r/23.x`**,
  neither `main` nor `master` — the only refs the ladder tries (`884-G2`). 🔵 This is the sibling of
  `p883`'s DSH finding, one step further out: resolving the default branch is necessary and the
  two-name assumption is still not sufficient.

🔵 **Derived figures for this page, graded every pass** (`ingest/derive-foundations.py`,
`Gap 544-E`): **derived shelf rows: **89****, across **18** SHELF-disposition tables, **89**
distinct addresses and **89** systems after declared alias collapse. 🟢 **`p884` added four tables
and declared all four in `ingest/foundations-disposition.tsv` in the same pass** — the gate exited
`2` and named them until it did, which is the manifest working as `p882` rebuilt it to.

Method, the four-region licence table and the full sweep: `repos/trending.md`, this pass.

**Previous pass (`p883`), retained:** **Pass `p883`, 2026-11-17** (thirteenth pass of the day). **`p883` adds the highest-star repository
this shelf has ever carried, and the reason it was never carried is that nobody looked at who owned
it.**

- 🟢 **`deepseek-ai/deepseek-harness` (DSH) — 282,965 ★, 35,072 forks, MIT, created 2026-08-13,
  pushed 2026-11-17.** Licence read as **bytes**: `master/LICENSE`, **1,065 B**,
  `sha256₁₂ ebb4f09972ae`, `MIT License` / `Copyright (c) 2026 DeepSeek`. This KB's trending history
  mentions the name; **no curated shelf has ever carried it.** It becomes an *education* substrate
  because an education distribution of it now exists — `ECNU/EduWork` (`agents/top.md`, `p883`).
- 🔴 **DSH's `main/LICENSE` is `404`. Its default branch is `master`.** A pass that probed `main`
  alone would have published *"no licence file"* on a 283,000-star MIT repository, and this KB's own
  `NOASSERTION` logic would then have shelved it as unusable. 🔵 **Rule: resolve the default branch
  with `git ls-remote --symref` BEFORE probing licence bytes.** `p882` added `default_branch` to the
  measurable fields and did not yet use it for this.
- 🟢 **This shelf now has a liveness column, and `882-G2` was a real defect** — see
  `repos/trending.md`, this pass, for the third metadata limb (`search/commits`, `200`) and the
  three rows whose licence cells are perfect and whose default branches are 13–22 months stale.

**Previous pass (`p882`), retained:** **Pass `p882`, 2026-11-17** (twelfth pass of the day). **`p882` re-measured every row on this
shelf first-hand and found the thing this file has asserted for 882 passes without ever measuring
it: the permissive share RISES as you go down the stack.**

- 🟢 **This shelf is 82.9% permissive** — 63 of 76 resolvable rows MIT, Apache-2.0 or BSD-3-Clause,
  against **50.9%** on `verticals/solutions.md`. The gradient is the *"attach, don't fork"* thesis
  as a number rather than as advice; the table is below.
- 🟢 **The channel that makes it possible:** `api.github.com/search/repositories` is `200` this pass
  while `api.github.com/repos/<slug>` is `403`. `p881` recorded the metadata channel as flatly down
  and could publish no star at all ([`record`](../evidence/channel-state.2026-11-17-p882.tsv)).
- 🔴 **Seven rows on the sell shelves have not been pushed in over twelve months**, one of them
  `stanford-oval/storm` at **31,902 ★**. Named below, because a star count is not a liveness check.
- 🟢 **This shelf can be counted again:** **76 rows across 14 tables**, measured (🆕 `p883` adds `deepseek-ai/deepseek-harness`). It has published no
  row count since the `p871`/`p877`–`p880` rewrites, which `gate-derived-counts` reported as *"no
  table can be located"* (`881-G3`, discharged this pass).


**Previous pass (`p879`), retained:** **Pass `p879`, 2026-11-17** (ninth pass of the day). **`p879` reverses a standing conclusion in
this file.** Discovery by **owner** (`user:<org>`) rather than by subject measured **571
repositories across 19 education organisations**, and the result is that the copyleft platforms
this KB has been routing clients away from **ship substantial, active, permissively licensed
component layers**:

- 🟢 **The permissive periphery** — `openedx/XBlock`, `codejail`, `paragon`, `xblock-sdk` and both
  mobile apps are **Apache-2.0** around an AGPL-3.0 core; `moodlehq/moodleapp` is Apache-2.0
  around a GPL-3.0 core. `compose/patterns.md` **P19** is the recipe.
- 🟢 **`apereo/cas`** — **Apache-2.0, 11,402 ★**, the SSO layer under much of the world's higher
  education, and the highest-star permissive education-infrastructure repository this KB has ever
  carried. It was missing entirely.
- 🟢 **Kolibri's content supply chain** — `studio`, `ricecooker`, `morango`, `le-utils`, all MIT.
  `morango` is multi-peer DB replication for devices that are never online together; **P20**.
- 🟢 **Closed:** the `openedx/edx-platform` "measurement gap" was a stale slug, not a channel hole.

**Previous pass (`p878`), retained:** **Pass `p878`, 2026-11-17** (eighth pass of the day). **`p878` makes discovery first-hand for the
first time, and the first thing it finds is the largest shelving miss in this KB's history.**
`api.github.com/search/repositories` accepts full discovery queries, not only the `repo:` slug
lookups `p875` used; 44 English legs returned **546 measured repositories** and 12 legs in
**Spanish and Portuguese — never run before** returned **304 more**. Three new sections below:

- 🟢 **The TUM stack** — nine MIT repositories from the Technical University of Munich around
  `ls1intum/Artemis` (832 ★), a ten-year-old operated university teaching platform. **It is the
  first permissively licensed assessment platform in this KB**, against AGPL/GPL everywhere else.
- 🟢 **`autolab/Autolab`** (Apache-2.0, 808 ★, Carnegie Mellon) — a second mature permissive
  auto-grader.
- 🔴 **LATAM-origin platforms**, including Brazil's incumbent `portabilis/i-educar` (GPL-2.0,
  726 ★, 13 years old) — found only because `p878` searched in Portuguese. **Every prior
  LATAM-absence claim in this KB is an artefact of English-only keyword legs.**

🟢 **`p877`'s two education-side licence anomalies independently re-confirmed by byte-read:**
`OpenOLAT/OpenOLAT` on `master` is a byte-identical **Apache License 2.0** preamble and
`Gego-K12/gegok12` on `main` is **MIT** — so the `NOASSERTION` note below stands, and its cause is
now exact rather than inferred: **GegoK12's `LICENSE` carries an HTML comment,
`<!-- SPDX-License-Identifier: MIT -->`, on line 3**, defeating the classifier on a file that
states its own SPDX identifier. 🔵 **The rule that covers both of this KB's licence errors —
`p877`'s false permissive and the false negatives here — is one rule: `spdx_id` screens, bytes
decide, in either direction.**

🟢 **Closed by `p879`: this was never a channel gap.** `p878` recorded `openedx/edx-platform` as
**unmeasurable** because `search/repositories` answers `422` for it. The slug is simply **stale**.
The canonical address is **https://github.com/openedx/openedx-platform** — measured first-hand at
**8,240 ★, AGPL-3.0, pushed 2026-11-17, 4,382 forks**. `raw.githubusercontent.com` keeps serving
the old path (byte-identical, 12,381 B) because GitHub honours rename redirects forever, which is
why nine passes of liveness probing never caught it. **The flagship LMS in
this KB has no measured star count, and absence from the sweep is not evidence of absence.**

🔴 **One more licence fact an Open edX engagement needs:** **`overhangio/tutor`**, the Docker-based
Open edX distribution and in practice *the* way Open edX is deployed, is **AGPL-3.0** (byte-read,
`LICENSE.txt`), 1,132 ★, pushed 2026-11-17. An Open edX build is therefore AGPL at the platform
layer **and** AGPL at the operations layer.

**Previous pass (`p877`), retained:** Pass `p877`, 2026-11-17** (seventh pass of the day). **`p877` closes a declared gap that has
stood in this file since `p872`, and adds the largest permissive education repository the KB has
ever failed to shelve.**

> **🟢 THE "NO PERMISSIVE SIS" GAP IS CLOSED. [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12)
> is MIT** — byte-read on `main`, **1,150 B**, `sha256₁₂ b8694396d7dc`, first line `MIT License`.
> A full-featured school management system in **Laravel**, API-first, Dockerised, with companion
> Android parent and teacher apps. **113 commits in the last 12 months.** Every SIS this KB had
> until now (Gibbon GPL-3.0, openSIS GPL-by-README-only, RosarioSIS GPL-2.0) was copyleft.
>
> 🔵 **Why four passes missed it, and this is a new method lesson:** the GitHub API reports
> `NOASSERTION` for this repository, because **line 3 of its `LICENSE` is
> `<!-- SPDX-License-Identifier: MIT -->`** — an added line that breaks stock-text matching. The
> detector was never saying "no grant"; it was saying "not byte-identical to a template".

> **🔴 `NOASSERTION` CARRIES ZERO INFORMATION ABOUT THE GRANT, and `p877` proves it with three
> repositories in one pass that share the signal and share nothing else:**
>
> | Repository | GitHub says | Bytes say | Verdict |
> |---|---|---|---|
> | `Gego-K12/gegok12` | `NOASSERTION` | MIT + an SPDX comment line | 🟢 **Permissive — more usable than it looked** |
> | `wwrwbs/AI_AWE` | `NOASSERTION` | Apache-2.0 short-form + component manifest | 🟢 **Permissive — and the manifest is itself useful** |
> | `CaviraOSS/PageLM` | `NOASSERTION` | bespoke non-commercial "Community License" | 🔴 **Not open source at all** |
>
> Three identical signals, three different commercial answers. **The detector collapses "more
> permissive than it looks", "fine but annotated" and "not open source at all" into one token.**
> Registered as `intel/trends.md` **T14**. This is the mirror image of `p872`'s substring-grep
> lesson: that one produced false *alarms*, this one produces false *absences* — and a false
> absence is worse, because nobody re-checks a repository already written off.

> **🔴 [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
> — Apache-2.0, 43,849★, 4,526 forks, 813 commits in 12 months — appeared in ZERO curated files
> before this pass.** It is the **second-largest education-native repository in this entire KB**,
> behind only DeepTutor, and it sat only in sweep logs and archives. Added below, to
> `verticals/solutions.md`, and wired into `compose/patterns.md` **P5**, whose offline stack was
> built without it.

**Previous pass note (`p876`)** (sixth pass of the day). **`p876` is a propagation audit, not a
discovery pass**, and it closes the gap `p875` opened one pass earlier — *in the same pass that
`p875`'s own sweep had already measured the answer*.

> **🟢 THE LRS GAP IS CLOSED. `p875` wrote "no maintained permissive LRS exists" into four files
> while its own sweep table (`agents/trending.md`, leg `xAPI learning record store stars:>15`)
> listed three.** Two of them are permissive **and** maintained:
> **`yetanalytics/lrsql`** (Apache-2.0, 144★, **67 commits in the last 12 months**) and
> **`openfun/ralph`** (MIT, 52★, from France Université Numérique, with **native Open edX
> tracking-log → xAPI converters in-tree**). Both are now rows in the new *Learning analytics &
> telemetry* section below. 🔵 **The method lesson: this KB's discovery channel is ahead of its
> curated shelf. A finding that is measured and not propagated is not yet knowledge** — it is a
> line in an 84,000-line log that the next proposal will not read.

> **🔴 AND THE DORMANCY WAS UNDERSTATED BY 2.5 YEARS.** `p875` recorded LearningLocker as *"18
> months"* dormant from its `pushed_at` field. **Its default branch's last commit is
> `2021-11-16` — 1,827 days, five years.** `p876` re-measured every address in this file by
> cloning it (`--filter=blob:none --bare`) and reading `git log -1 HEAD`, which is the branch a
> clone actually gives you. **83 of 83 clones succeeded.** See `repos/trending.md` `p876` for the
> full divergence table and two further stale rows this caught.

**Previous pass note (`p875`)** (fifth pass of the day). **`p875` closes the star gap and uses it to
audit this file rather than to decorate it.** 78 addresses measured first-hand via
`api.github.com/search/repositories` — the channel four passes called impossible (see
`repos/trending.md` for how it was found). The measurement produced **three corrections to this
file that no licence check could have produced**:

> **🟡 1. A duplicated address, now collapsed.** This file carried **two rows for the same
> project** — `edx/edx-ora2` and `openedx/edx-ora2` — because `p872` added the current org without
> removing the legacy one. The measurement settles which to keep: **only `openedx/` resolves in
> the GitHub search index** (64 stars, AGPL-3.0, last push 2026-11-13), while `edx/` returns
> nothing, even though both still resolve over the git protocol via redirect. 🔵 *The git protocol
> follows renamed-org redirects, so an existence check passes on a stale address long after it
> stops being canonical — which is exactly how a duplicate survives a licence-and-existence
> audit.* One row now, `openedx/`.

> **🔴 2. The xAPI layer is unmaintained, and it is the one this KB's measurement pitch rests on.**
> 🟢 **`p876`: the second half of this item — "no maintained permissive LRS" — is WITHDRAWN as
> wrong; see the banner above. The first half is CONFIRMED and sharpened: the dormancy is five
> years, not 18 months.** Original `p875` text retained below for the record.
> `LearningLocker/learninglocker` (587 stars) **has not been pushed since 2024-05-30 — 18
> months**. `intel/trends.md` T9 argues that *measurement* is the defensible deliverable in this
> vertical, and the Learning Record Store that every such pattern routes telemetry into is
> dormant. **`p875` did not find a maintained permissive LRS and does not invent one.** Any
> engagement promising measurement must either budget "we operate this fork" into the statement of
> work, or use the LMS's native gradebook and accept the weaker evidence. **This is now the
> highest-value unfilled slot in the education open-source stack.**

> **🟡 3. Two more foundations are quiet.** `1EdTech/openbadges-validator-core` (61 stars, last
> push 2025-11-04) — from the standards body, so more likely *finished* than abandoned, but do not
> present it as actively developed. `stanford-oval/storm` (31,901 stars, last push 2025-09-30) —
> **high stars, 14 months idle; stars and liveness are independent signals** and this file should
> not let one stand in for the other.

A licence mismatch worth carrying to a client conversation: **`OpenOLAT/OpenOLAT` and
`BerriAI/litellm` both return `NOASSERTION` from GitHub's SPDX detector** while their licence bytes
read Apache-2.0 and MIT. The byte-read is authoritative — the cause is almost certainly a modified
licence header — **but a client's counsel will run the automated check and get `NOASSERTION`.
Brief them before they ask.** Full table in `repos/trending.md`.

**Previous pass note (`p874`):** added `moocupv/lti-ai-grader` to the standards layer and
established that star counts had failed across nine routes. `p875` supersedes that diagnosis: the
failure was an egress allowlist for non-GitHub hosts **plus** a wrong generalisation about GitHub
itself. `moocupv/lti-ai-grader` measures **0 stars** — consistent with its listing as a component
to harvest rather than a project to adopt.

`p872` re-resolved every load-bearing address in this file through `git ls-remote --symref` and
found **four of eleven do not default to `main`**. Branch column corrected below where it was
wrong, and `openedx/` recorded as the live org for `edx-ora2`.

These are the load-bearing pieces an education build sits on: the standards plumbing that
makes a tool interoperable with institutional systems, and the AI substrate that makes it
work. The standards layer matters more here than in most verticals — an education tool that
cannot speak LTI, xAPI/Caliper, QTI or Ed-Fi cannot be bought by a school district.

## 🆕 `p882` · 2026-11-17 — what changed on this shelf

### 🟢 The licence gradient, measured per layer for the first time

Every address on the three sell shelves, re-measured this pass by SPDX id as GitHub resolves it
([`record`](../evidence/sell-shelf-measure.2026-11-17-p882.tsv)):

| Shelf | Layer | Rows resolved | Permissive | Copyleft | No resolvable grant |
|---|---|---:|---:|---:|---:|
| `repos/foundations.md` | substrate & libraries | 76 | **82.9%** (63) | 6.6% (5) | 9.2% (7) |
| `agents/top.md` | agents | 42 | **78.6%** (33) | 4.8% (2) | 14.3% (6) |
| `verticals/solutions.md` | platforms institutions run | 55 | **50.9%** (28) | **38.2%** (21) | 10.9% (6) |

🔵 **Why this is the most useful table on this shelf.** The copyleft problem in education is not
spread through the open-source estate — it is **concentrated in the layer a client already owns and
is not going to replace**. Moodle, Canvas, Open edX, Chamilo, ILIAS and Koha are the incumbents and
they are GPL/AGPL; the substrate you *build* on is 83% permissive. 🟢 **So the licence answer and
the architecture answer are the same answer:** leave the platform where it is, attach over LTI 1.3,
xAPI and OneRoster, and keep every line you write in the permissive layer. This file's **P19** and
**P20** are that shape, and `verticals/solutions.md`'s mobile-client row is its cheapest instance.

🔴 **The 9.2% here is not a licence, it is a silence.** Seven rows resolve to `NOASSERTION` — GitHub
declining to classify, not a permission: `BerriAI/litellm`, `opendatalab/MinerU`, `ankitects/anki`,
`apereo/java-cas-client`, `frappe/education`, `instructure/instructure-ui`, `Gego-K12/gegok12`.
Four already carry byte-read grant cells in this file; the other three do not, and a studio must
read the bytes before quoting them.

### 🔴 Liveness: seven sell rows have gone quiet, and stars do not show it

| Repo | Last push | ★ | Licence | Why it matters here |
|---|---|---:|---|---|
| https://github.com/LearningLocker/learninglocker | **2024-05-30** | 587 | GPL-3.0 | ~18 months. The xAPI **LRS** in this file's analytics layer — the one component a learning-analytics engagement cannot route around |
| https://github.com/stanford-oval/storm | **2025-09-30** | 31,902 | MIT | ~14 months at **31,902 ★**. The clearest case that a star count is not a maintenance signal |
| https://github.com/adlnet/ADL_LRS | 2025-11-14 | 335 | Apache-2.0 | the *other* LRS, also quiet — so the xAPI layer has no actively maintained permissive server on this shelf |
| https://github.com/1EdTech/openbadges-validator-core | 2025-11-04 | 61 | Apache-2.0 | credentialing validator; the standard moves faster than the validator |
| https://github.com/kamlendras/OpenProctor | 2025-05-28 | 16 | AGPL-3.0 | reinforces `p875`'s proctoring finding — real demand, no live supply |
| https://github.com/ganesh-786/Proctor | 2025-06-09 | 0 | MIT | same |
| https://github.com/PritK99/WriteRight | 2024-11-19 | 1 | MIT | same class, writing feedback |

🟢 **The actionable one is the LRS.** Both permissive xAPI learning-record stores on this shelf are
quiet, and the live analytics path is therefore *write the LRS boundary yourself behind xAPI* rather
than adopt one. 🔴 Registered as `882-G2`: **this shelf has had no liveness column, so a row could
go eighteen months stale while its licence cell stayed perfectly accurate.** The gradient table
above is a licence measure, not a liveness one, and the two must not be read as each other.

## 🆕 `p881` · 2026-11-17 — what changed on this shelf

🟢 **Two slug corrections, `OpenOlat/OpenOlat` → `OpenOLAT/OpenOLAT`**, discharging `880-G4` on this
shelf ([`record`](../evidence/case-oracle.2026-11-17-p881.tsv)). The **product** is branded *OpenOlat*
and the **addresses** are `OpenOLAT/OpenOLAT`; a blanket replace would have broken the product name, so
only the slug token was changed.

🔴 **No foundation row was added, and that is a measurement, not an omission.** `p881`'s eight WebSearch
legs — global, trending, verticals, trends and four regional — returned **0 new repositories**
([`record`](../evidence/websearch-legs.2026-11-17-p881.tsv)). Three passes running (`p879`, `p880`,
`p881`) this channel has produced no new supply.

🔴 **`gate-grant-path` reads `0` grant claims on this shelf** because the tables now publish
`Licence (byte-read)` with no branch/path column. A zero parse is not a clean shelf; it is in `p881`'s
gate triage as a shelf defect with a named remedy
([`record`](../evidence/gate-triage.2026-11-17-p881.tsv)).

## 🆕 `p880` · 2026-11-17 — what changed on this shelf

🟢 **Four rows** from the full-estate recount: `apereo/java-cas-client` (🔵 **CONJUNCTIVE** —
Apache-2.0 *and* BSD-3-Clause in one payload, notice obligation of two), `instructure/instructure-ui`
(MIT), `instructure/common-cartridge-viewer` (MIT) and `mitodl/ol-infrastructure` (BSD-3-Clause).
🔴 **`NO-PERMISSIVE-PLATFORM` was RETIRED rather than restored to this shelf: the shelf's own rows
disprove it** — Artemis (MIT, `832★`), Autolab (Apache-2.0, `808★`) and Kolibri (MIT) are all
permissive full platforms. 🟡 `2,003` extra repositories of denominator yielded these four rows,
which is `T12` reconfirmed from the denominator side.

## The foundations — 89 rows

🟢 **Derived, not asserted.** `89` distinct repositories across the **18** layer tables below,
and the layering is the value of this file rather than an accident of its history: substrate,
standards, analytics, curriculum, institutional platforms, ingestion, retrieval and evaluation are
different procurement decisions. `ingest/derive-counts.py` grades this heading against the rows on
every pass.

🔵 One repository may legitimately appear in two layers — `frappe/education` sits in both the
Frappe layer and the ERP layer — so the figure counts **distinct subjects**, not table rows
(`p813`'s rule). 🔴 The liveness table in the `p882` section is declared NOT counted: it restates
rows from these tables to flag the seven that have gone quiet.

## The permissive periphery of the copyleft platforms — new in `p879`

🔵 **This is the single most useful thing `p879` measured, and it reverses standing advice in this
KB.** Every pass until now has treated Open edX (AGPL-3.0) and Moodle (GPL-3.0) as unusable for a
client who cannot take copyleft. Measured **per organisation** rather than per flagship, each of
those projects ships a **substantial, actively maintained, permissively licensed component layer**
that can be adopted on its own.

🟢 Method: `search/repositories?q=user:<org> fork:false`, 19 education orgs, **571 repositories
measured** (`evidence/org-estate-census.2026-11-17-p879.tsv`). Licences below were **read from the
repository's own licence file** over `raw.githubusercontent.com`
(`evidence/license-byteread.2026-11-17-p879.tsv`), not taken from the search index.

| Repo | Licence (byte-read) | ★ | Pushed | Created | What it gives you alone |
|---|---|---:|---|---|---|
| 🟢 https://github.com/deepseek-ai/deepseek-harness | 🟢 **MIT** — byte-read **`master/LICENSE`** (⚠️ `main/LICENSE` is `404`), 1,065 B, `sha256₁₂ ebb4f09972ae` | **282,965** | 2026-11-17 | 2026-08-13 | **DeepSeek Harness — "Everything is a Plugin."** An MIT agent runtime with a plugin and skill system, 35,072 forks, three months old. 🟢 **NEW in `p883`, and the highest-star row on this shelf.** It is here because **`ECNU/EduWork` proves the education path**: a university took DSH and shipped a teaching distribution on it under a permissive grant. **For a Globant engagement this is the substrate you can keep** — MIT runtime, your plugins, no copyleft reach, and an existing institutional reference implementation to point a buyer at. |
| https://github.com/apereo/cas | **Apache-2.0** (`LICENSE`) | **11,402** | 2026-11-17 | 2011-09-09 | **Central Authentication Service — the SSO layer under a large share of the world's universities.** 3,954 forks. Protocol support for CAS, SAML2, OAuth2, OIDC, WS-Fed; MFA; delegated auth. 🔵 **The highest-star permissive education-infrastructure repository in this KB, and it was never carried.** |
| https://github.com/apereo/phpCAS | 🔵 **CONJUNCTIVE — Apache-2.0 *and* BSD-3-Clause** — **CORRECTED by `p887`.** Apache-2.0 at `master/LICENSE` **11,357 B** `sha256₁₂ c71d239df917` (the full stock text) **and** a complete **New BSD** body in `master/NOTICE` **3,914 B** `sha256₁₂ 2df146a253fa`, headed *"Requirements for sources originally licensed under the New BSD License"*, © 2003-2007 **The ESUP-Portail consortium**, with a no-endorsement clause naming JA-SIG, Inc. | 802 | 2026-06-30 | — | The PHP client — i.e. how Moodle and other PHP estates attach to CAS. 🔴 **Five months since last push, and `8` commits in the last 12 months** (measured `p887`, `search/commits`). 🔴 **Was published here as single-family `Apache-2.0` (`LICENSE`) — see the note below `:748`, which said a single-family label on its sibling "would be wrong" while this row carried one.** |
| https://github.com/openedx/codejail | **Apache-2.0** (`LICENSE.txt`) | 477 | 2026-11-16 | 2013-04-26 | **Secure sandboxed execution of untrusted code.** The substrate any auto-grader or code-running tutor needs, usable with no Open edX dependency. |
| https://github.com/openedx/XBlock | **Apache-2.0** (`LICENSE.TXT`) | 471 | 2026-11-16 | 2013-03-11 | **The learning-component framework.** Write a component once; it runs inside any Open edX install — **without your component inheriting AGPL**. |
| https://github.com/openedx/xblock-sdk | **Apache-2.0** (`LICENSE.TXT`) | 69 | 2026-11-16 | — | Workbench and worked examples — develop and run an XBlock with no LMS present. |
| https://github.com/openedx/paragon | **Apache-2.0** (`LICENSE`) | 141 | 2026-11-17 | — | **Accessible, theme-ready React design system built specifically for learning applications.** Carries the accessibility work most teams re-do badly; see the accessibility section of `verticals/solutions.md`. |
| https://github.com/moodlehq/moodleapp | **Apache-2.0** (`package.json`) | 1,006 | 2026-11-17 | 2015-03-03 | **The official Moodle mobile app** — Apache-2.0 against a GPL-3.0 server. 2,491 forks: it is routinely white-labelled. |
| https://github.com/moodlehq/wiki-rag | **BSD-3-Clause** (`LICENSE`) | 54 | 2026-06-15 🔴 | — | Moodle HQ's own experimental RAG over MediaWiki content. **Stale by five months — reference implementation, not a dependency.** |
| https://github.com/autolab/Tango | **Apache-2.0** (`LICENSE`) | 49 | 2026-10-21 | 2014-10-26 | **Standalone RESTful autograding service**, separable from Autolab itself. |
| https://github.com/openedx/openedx-app-android | **Apache-2.0** (`LICENSE`) | 38 | 2026-11-09 | — | Official Open edX Android client. An iOS twin exists at `openedx/openedx-app-ios` (Apache-2.0, 31 ★). |
| https://github.com/oppia/oppia-android | **Apache-2.0** (`LICENSE`) | 422 | 2026-11-17 | — | Oppia's offline-capable Android client. |

🟡 **The caveat that has to travel with this table.** Apache-2.0 on a component does **not**
launder the platform. If the client **runs a modified Open edX server over a network**, AGPL-3.0
§13 applies to *that server*. What these licences buy is the right to build, keep and sell **your
components** — XBlocks, a grader, a design system, a mobile client — on permissive terms. 🔵 **The
clean line: permissive for what you write and ship, copyleft for what you fork and host.**

## Kolibri's content supply chain — the offline-first half nobody shelved, new in `p879`

🟢 `learningequality/kolibri` (MIT, 1,178 ★) has been in this file for many passes **on its own**.
The census shows the rest of its estate is MIT too, and the pieces are individually useful.

| Repo | Licence (byte-read) | ★ | Pushed | Role |
|---|---|---:|---|---|
| https://github.com/learningequality/studio | **MIT** (`LICENSE`) | 212 | 2026-11-09 | **Kolibri Studio** — the content curation and channel-authoring application. |
| https://github.com/learningequality/ricecooker | **MIT** (`LICENSE`) | 32 | 2026-11-02 | **Python library for programmatically building Kolibri channels** and pushing them to Studio. This is the automation seam: a pipeline that ingests a ministry's PDFs and emits a Kolibri channel is a `ricecooker` script. |
| https://github.com/learningequality/morango | **MIT** (`LICENSE`) | 15 | 2026-11-13 | **Pure-Python database replication engine for Django** (SQLite **and** PostgreSQL), built for intermittently connected peers. 🔵 **This is the piece that makes offline-first real**, and it is usable outside Kolibri. |
| https://github.com/learningequality/le-utils | **MIT** | 7 | 2026-11-02 | Shared constants and utilities across the three above. |

🔵 **Why this matters more than the star counts suggest.** `morango` at 15 ★ is not a popularity
signal; it is a **15-star solution to the hardest problem in low-connectivity deployment** —
multi-writer sync with conflict resolution across devices that are rarely online together. Writing
that from scratch is a quarter of an engagement. See `compose/patterns.md` **P20**.

## H5P as components rather than as a plugin — new in `p879`

🟡 H5P has been carried in `verticals/solutions.md` as a content-type *framework*. The census shows
the **individual content types are separately MIT-licensed repositories**, which changes how they
can be used: a team can take one interaction type into its own product without adopting H5P's
integration layer.

| Repo | Licence | ★ | Pushed |
|---|---|---:|---|
| https://github.com/h5p/h5p-interactive-video | **MIT** (`package.json`) | 267 | 2026-11-17 |
| https://github.com/h5p/h5p-cli | **MIT** (`LICENSE`) | 79 | 2026-10-31 |
| https://github.com/h5p/h5p-course-presentation | MIT | 57 | 2026-11-11 |
| https://github.com/h5p/h5p-audio-recorder | MIT | 36 | 2026-11-17 |
| https://github.com/h5p/h5p-speak-the-words | MIT | 12 | 2026-11-17 |

🔴 **15 of the 40 sampled `h5p` repositories carry MIT and 23 carry no licence file at all.** Check
each content type individually; **do not generalise H5P's licence from one repository to the next.**


## Education standards & interoperability

This is the layer that gets a Globant build past institutional procurement.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | `master` | **LTI 1.3 / LTI Advantage tool provider in Node.** The single most reusable piece of plumbing in education software: implement it once and your agent launches as a tool inside Moodle, Canvas, Open edX, Blackboard and D2L with grade passback. Permissive — safe to embed. |
| https://github.com/moocupv/lti-ai-grader | Apache-2.0 | `main` | **The first verified permissive AI grader that actually speaks the LTI seam.** From MOOC UPV (Universitat Politecnica de Valencia, Spain — EMEA-origin). An LLM grader that posts grades back to an LMS, *tested with Open edX and Moodle*; configurable grading prompts, Gemini or any OpenAI-compatible API, multi-language templates, and a private/public file split that keeps logic and secrets out of the web root. Tag `excel-v1.0`. **Caveat that governs how to use it: it is LTI 1.1 (OAuth 1.0a), the deprecated generation — not 1.3.** Take its grading core and prompt configuration, and swap the transport for `ltijs` above to get a 1.3/Advantage launch with AGS passback. Added by `p874`; licence byte-read on `main`. |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 | `main` | **Ed-Fi Operational Data Store + API.** The de-facto K-12 data standard in US school districts. Apache-2.0, so a district-facing analytics or early-warning agent can build directly on it. |
| https://github.com/1EdTech/openbadges-validator-core | Apache-2.0 | `develop` | Open Badges validation from the standards body itself (1EdTech, formerly IMS Global). The verification half of any credentialing or micro-credential build. |
| https://github.com/Citolab/qti-components | GPL-3.0 | `main` | **QTI 3 web components** — standards-compliant assessment item rendering. Copyleft: fine for a self-hosted institutional deployment, a problem for a proprietary distributed product. |
| https://github.com/openedx/edx-ora2 | AGPL-3.0 | `master` | **Open-response assessment** — rubrics, peer assessment, self assessment, staff grading. Given that no mature OSS grading *agent* exists (see `agents/top.md` gaps), this is the realistic production substrate for AI-assisted grading. AGPL: network-use triggers source obligations. **64 stars, last push 2026-11-13** (`p875`). **`p875` collapsed the duplicate `edx/` row that stood here:** both org forms resolve over the git protocol via redirect, but only `openedx/` resolves in the GitHub search index, so `openedx/` is the single canonical address this KB carries. |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | `master` | **xAPI Learning Record Store.** 🔴 **SUPERSEDED by `p876` — do not start here.** 587 stars. `pushed_at` reports `2024-05-30`, but the **default branch's last commit is `2021-11-16` — 1,827 days**, and there are **0 commits in the last 12 months**. Copyleft *and* five years cold. Retained in this file only so that a later pass does not re-import it from a listicle. **Use `yetanalytics/lrsql` or `openfun/ralph` below.** |
| https://github.com/openedx/openedx-aspects | Apache-2.0 | `main` | Open edX's learning-analytics stack (Aspects). Apache-2.0 and reusable even outside an Open edX deployment. |
| https://github.com/jupyter/nbgrader | BSD | `main` | Assignment release, collection and autograding for Jupyter notebooks. The standard autograder in university CS and data-science courses. |
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** — 🟢 **CORRECTED by `p887`, and this base's own instrument is what caught it.** Was published as bare `BSD`; `compose/code/p314-untitled-payload-arm/README.md:12` has recorded `BSD-3-Clause` for this row since `p314`, and the metadata channel returned `BSD-3-Clause` independently this pass. 🔵 The under-specification has a cause worth keeping: p314 measured that this payload is a **complete, valid grant with no title line and zero `BSD` tokens anywhere in the file**, so a title-matching classifier can only ever reach the family by inference. | `main` | Multi-user notebook hosting — the substrate for every hands-on technical course delivered in a browser. **8,368 ★, pushed 2026-11-05**; measured `p887`. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | `main` | **FSRS** — the modern free-spaced-repetition scheduler. MIT-licensed, empirically validated memory model. If your product claims retention, this is the algorithm to use instead of inventing a review schedule. |

## Learning analytics & telemetry (xAPI) — new in `p876`

This section exists because `intel/trends.md` **T9** argues that *measurement* is the defensible
deliverable in this vertical, and until this pass the only Learning Record Store this KB carried
was copyleft and five years dead. Every row was verified on four channels this pass: existence and
default branch via `git ls-remote --symref`, licence **bytes** from `raw.githubusercontent.com`,
stars/SPDX via `api.github.com/search/repositories`, and **liveness via a blobless bare clone and
`git log -1 HEAD`** — not the `pushed_at` field, which is what produced the error above.

| Repo | Licence | Branch | Stars | HEAD | Commits/12mo | Why it is foundational |
|---|---|---|---|---|---|---|
| https://github.com/yetanalytics/lrsql | Apache-2.0 (11,357 B) | `main` | 144 | 2026-11-14 | **67** | **Yet Analytics SQL LRS — the maintained permissive LRS, and the default recommendation.** A full xAPI LRS (statements, attachments, documents, per xAPI spec Part 3) over ordinary SQL: **SQLite embedded, Postgres 14–18, MariaDB 10.6–11.8, MySQL 8.0–9.5**. Ships a Docker image, **OIDC support** (with an Auth0 setup guide), a TLS/HTTPS guide, a documented AWS deployment, and a "Reactions" rules engine for triggering on statement patterns. Clojure. Latest tags `v0.9.14`, `v1.0.0-pre_ui_testing`. **This is the row that replaces LearningLocker in P1, P7 and P9.** |
| https://github.com/openfun/ralph | MIT (1,094 B) | `main` | 52 | 2026-10-12 (`v5.1.0`) | 18 | **The EMEA, public-sector, Open edX-native option — and the only MIT one.** From **OpenFUN (France Université Numérique)**, the consortium that operates France's national Open edX platform. Three things in one: an **LRS HTTP API** (FastAPI, `src/ralph/api/`, with **basic *and* OIDC auth** and statement forwarding), a **CLI** for building data pipelines, and a **library**. 🟢 **Verified in-tree, not from the README: `src/ralph/models/edx/` holds event models and `converters/` for Open edX tracking logs, alongside `src/ralph/models/xapi/`** — so Open edX telemetry becomes xAPI without writing the mapping yourself. Ships a **Helm chart** (`src/helm/ralph/`) and a PyPI package (`ralph-malph`). Community support runs through **ESUP**, the French higher-education consortium. |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 (11,357 B) | `master` | 335 | 2025-11-14 | 0 | **The reference implementation, from the body that wrote the specification** — ADL, authors of xAPI. Python/Django. 🟡 **Liveness flag: 0 commits in the last 12 months.** Treat it as the conformance *reference* to test against and read, not as the production substrate: for that, use `lrsql`. Highest star count of the three, which is reputation rather than momentum. |

**How to choose between them.** Take **`lrsql`** by default — it is the most active (67 commits in
12 months against ralph's 18), it speaks four DBMS families so it drops into whatever the
institution already runs, and Apache-2.0 carries an explicit patent grant. Take **`ralph`** when
the deployment is **Open edX** (its converters are the work you would otherwise do by hand), when
the client is **European public sector** and a French public-consortium provenance plus MIT is
worth more than raw commit velocity, or when the pipeline matters as much as the store. **Neither
is a drop-in for LearningLocker's dashboards** — Learning Locker bundled a reporting UI, and these
are stores and pipelines. Budget the visualisation layer explicitly (Aspects/Superset, or Grafana
over Postgres); do not let a statement of work imply dashboards come free.

## Curriculum structure — new in `p875`

The layer that tells a tutoring agent *what comes before what*. Without it, "personalised learning
path" is a prompt, not a data structure.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-1.0** | `main` | **A 1,590-topic children's curriculum graph with 3,221 prerequisite edges** — the prerequisite relation is the part that is hard to build and expensive to buy, and this is the only open one this KB has found. **7,720 stars, last push 2026-11-16** — real traction, actively maintained. 🔴 **Read the licence before you plan around it: Open Data Commons ODbL is a share-alike *database* licence, not a software licence.** Using it to drive a service is fine; **publishing a derived or extended database triggers share-alike obligations on that database.** It is therefore *not* in the MIT/Apache class this KB otherwise prefers and must never be filed as permissive. The safe pattern is to consume the graph as reference data behind a service and keep client-specific curriculum extensions in a separate store you do not redistribute. |

🟡 **Gap this exposes rather than closes:** there is **no permissive** open curriculum graph. If a
client needs to own and redistribute a prerequisite taxonomy, it is bespoke work — and `os-taxonomy`
is still the best thing to read first when scoping it.

## Permissive institutional platforms — new in `p877`

Rows measured first-hand this pass: existence and default branch by `git ls-remote --symref`,
licence by byte-read on `raw.githubusercontent.com`, traction by `search/repositories`, liveness
by blobless bare clone (`git log -1 HEAD`), per the `p876` method.

| Repo | Licence (byte-read) | Branch | ★ | HEAD | Commits/12mo | Why it is here |
|---|---|---|---:|---|---:|---|
| https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** (10,778 B) | `main` | **43,849** | 2026-11-08 | **813** | **Offline-first knowledge and education server** — Wikipedia, thousands of books, courses, maps and **optional local AI**, all served from one box with no internet. Apache-2.0, Dockerised, `collections/`, `admin/`, `install/` in-tree, semantic-release. **4,526 forks** is the number that matters: forks of an appliance repo are deployments, not stars. This is the natural substrate for every ministry equity programme and rural-school bid in `compose/patterns.md` **P5**, and it is permissive where Internet-in-a-Box (LGPL) and Kiwix (GPL-3.0) are not. |
| https://github.com/Gego-K12/gegok12 | **MIT** (1,150 B, `sha256₁₂ b8694396d7dc`) | `main` | 57 | 2026-06-25 | 113 | **The first permissive student-information system in this KB** — closes the standing gap below. Laravel/PHP, **API-first by design** (`api.md` in-tree), `Dockerfile` + `docker-compose.yml`, `lang/` for localisation, plus separate Android **parent** and **teacher** apps. 🟡 **Low stars and HEAD five months cold** — this is a small project, and it should be proposed as *a permissive base you will own and extend*, not as a mature product with a community behind it. Its value is the licence: it is the only SIS here you can fork, rebrand and ship inside a proprietary deliverable. 🔴 GitHub reports `NOASSERTION`; the bytes say MIT. |

## The TUM stack — permissive university teaching infrastructure, new in `p878`

🟢 **The largest shelving miss in this KB's history, and it is institutional, European and MIT.**
`ls1intum` is the Applied Education Technologies group at the **Technical University of Munich**.
It publishes **68 repositories pushed since 2026-01-01**, the great majority MIT, built around a
teaching platform that has existed since **2016** and is operated at university scale. No pass
before `p878` carried any of it, because every previous discovery leg was a search-engine summary
and listicles do not rank university infrastructure.

Rows measured first-hand: licence by **byte-read** on `raw.githubusercontent.com`, traction and
`pushed_at` via `api.github.com/search/repositories`, README read from the repository itself.

| Repo | Licence (byte-read) | ★ | Pushed | Why it is foundational |
|---|---|---:|---|---|
| https://github.com/ls1intum/Artemis | **MIT** (byte-read on `main`) | **832** | 2026-11-17 | 🟡 **Default branch `develop`.**  **The platform.** Interactive exercises (programming, modelling, text, quiz, file-upload) as first-class objects with version control, CI and static analysis built in; **online exams with per-student exercise variants, test runs, plagiarism checks and structured student reviews**; competencies, learning paths and learning analytics; config-gated AI. Java, self-hosted, horizontally scalable. OpenSSF Scorecard and OpenSSF Best Practices (project 14163), Sonar and Codacy gates. |
| https://github.com/ls1intum/Ares | **MIT** | 27 | 2026-11-03 | **Secure sandboxed execution for auto-graded Java**, as a JUnit 5 extension. 🔵 **The single most liftable component found this pass** — running untrusted student code safely is the part of every auto-grader that is easy to get wrong and expensive to get right, and this is a permissive implementation with no platform dependency. (`Ares2`, the second Java implementation, is in progress and reports `NOASSERTION` — byte-read before use.) |
| https://github.com/ls1intum/edutelligence | **MIT** | 17 | 2026-11-17 | The AI microservice suite: **Iris** (learner-facing tutor), **Athena** (feedback *suggestions* for human assessors), **Hyperion**. Python. |
| https://github.com/ls1intum/Pyris | **MIT** | 12 | 2026-06-03 | Standalone LLM microservice behind Iris — the smaller seam if you want the model layer alone. |
| https://github.com/ls1intum/Apollon | **MIT** | 106 | 2026-11-17 | UML modelling editor, TypeScript. Standalone build (`Apollon_standalone`) and a VS Code extension exist. |
| https://github.com/ls1intum/artemis-ansible-collection | **MIT** | 8 | 2026-11-17 | Ansible collection to configure and deploy Artemis. **Deployment automation shipped by the maintainers** — rare in this index and worth real money in a delivery estimate. |
| https://github.com/ls1intum/artemis-ios | **MIT** | 13 | 2026-11-16 | Native iOS client (Swift). |
| https://github.com/ls1intum/artemis-android | **MIT** | 13 | 2026-11-14 | Native Android client (Kotlin). |
| https://github.com/ls1intum/standardized-competency-catalog | **MIT** | 1 | 2026-03-01 | TUM's standardised competency catalogue. 🟡 Tiny, but it is **a permissive competency structure**, and `p875` recorded that no permissive curriculum graph exists (`os-taxonomy` is **ODbL-1.0**). This does not close that gap — it is a catalogue, not a prerequisite graph — but it is the first permissive thing in the category. |

🔵 **What this changes in the licence arithmetic.** Before `p878`, the honest answer to *"can we
build an assessment platform on open source and ship it inside a proprietary deliverable?"* was
no: Open edX is AGPL-3.0, `edx-ora2` is AGPL-3.0, Moodle is GPL-3.0, Canvas is AGPL-3.0, QTI
components are GPL-3.0. **Artemis is MIT.** That is the whole of the difference, and it is the kind
of difference that decides a build-versus-buy conversation.

🟡 **And what it does not change.** 832 stars is a small community for a platform of this size;
Java/Spring is a heavier operational commitment than PHP or Python; and the platform is built
around **university** course structures, so a K-12 or corporate-training engagement will fight it.
Propose it where the shape matches: higher education, technical subjects, assessment at scale.

## The second permissive auto-grader — `autolab/Autolab`, new in `p878`

| Repo | Licence (byte-read) | ★ | Pushed | Created | Why it is foundational |
|---|---|---:|---|---|---|
| https://github.com/autolab/Autolab | **Apache-2.0** (`master/LICENSE`) | **808** | 2026-11-11 | 2014-10-25 | **Carnegie Mellon's course-management service built around auto-graded programming assignments.** Twelve years old, still pushed. Apache-2.0 carries an explicit patent grant, which Artemis's MIT does not — occasionally the deciding factor in an enterprise or public-sector procurement. |

🔵 **Artemis or Autolab?** Take **Artemis** when the engagement needs exams, modelling, text
assessment, competencies and analytics in one system, and when MIT's simplicity is worth more than
a patent clause. Take **Autolab** when the scope is narrow — *auto-grade programming work* — when a
lighter system is an advantage, or when counsel wants Apache-2.0's patent grant. Both are
genuine; neither is a research prototype.

## LATAM-origin education platforms — new in `p878`

🔴 **This section exists because of a method failure, and it should be read as one.** Eight passes
recorded that LATAM produces almost no open-source education software. **None of them had ever run
a discovery query in Spanish or Portuguese.** Twelve such legs returned 304 repositories.

| Repo | Licence (byte-read) | ★ | Pushed | Created | Note |
|---|---|---:|---|---|---|
| https://github.com/portabilis/i-educar | 🔴 **GPL-2.0** | **726** | 2026-11-13 | 2013-01-31 | 🔴 **Default branch `2.12`, not `main`/`master`.**  **Brazil's incumbent free-software school-management system** — *"o maior software livre educacional do Brasil"*. Online administration for school secretaries, teachers, coordinators and managers. Tagged releases, GitHub Actions CI, modular packages, documented upgrade path. |
| https://github.com/portabilis/i-diario | 🔴 **AGPL-3.0** (byte-read: *LICENÇA PÚBLICA GERAL AFFERO GNU*; GitHub says `NOASSERTION` — **T14**) | 117 | 2026-10-14 | 2018-11-30 | 🔴 **Default branch `1.6`.**  Companion **electronic class diary** — attendance, grades, lesson records. |
| https://github.com/Antonio-Neves/Gestao-Escolar | **MIT** | 50 | 2026-10-12 | 2020-12-03 | Complete school-management system, bilingual PT/EN. 🟢 **The only permissive LATAM-origin SIS found.** Small — propose as a base to own, as with GegoK12. |

🔵 **How to use `i-educar` despite the copyleft.** It is GPL-2.0, so it cannot be forked into a
proprietary deliverable — but it is the **incumbent** in Brazilian municipal education, which makes
it an **integration target rather than a base**. Build the AI layer as a separate service with a
clean process boundary and the copyleft stays where it is. This is the posture
`verticals/solutions.md` already prescribes for Moodle, and it applies unchanged here.

## Institutional LMS/SIS integration estates — new in `p884`

🟢 **A university's TEACHING CENTRE is a different publisher from its AI lab, and this KB had only
ever shelved the lab.** `p884` rebuilt the owner register from GitHub's own user index
(`search/users` by institution **display name**, not a guessed handle) and swept **270
organisations / 10,365 repositories** across all four regions
([`sweep`](../evidence/owner-sweep.2026-11-18-p884.tsv)). After machine-learning vocabulary is
removed, the permissive survivors are overwhelmingly **not** agents and **not** research code: they
are **production integration plumbing** — SIS importers, gradebook uploaders, Canvas API clients,
Sakai and Tsugi tools.

🔴 **Every row below carries a single-digit or low-double-digit star count**, which is exactly why
this layer was invisible: every prior discovery leg here was keyword-ranked or star-ranked, and
institutional plumbing is neither popular nor tagged. 🔵 **It is also the layer an education
engagement actually spends its weeks on** — the counterpart to `p879`'s *vendor-built AI
components*.

Licence by **byte-read** on `raw.githubusercontent.com`; existence and the **true** default branch
by `git ls-remote --symref`; traction and `pushed_at` via `api.github.com/search/repositories`
([`grants`](../evidence/grant-verify.2026-11-18-p884.tsv) ·
[`existence`](../evidence/exist-verify.2026-11-18-p884.tsv)).

### 🟢 `cilt-uct` — University of Cape Town, and the best-licensed education estate in 884 passes

🔵 **50 repositories, 48 of them permissive — `Apache-2.0` ×30 and `ECL-2.0` ×16 — with only 2
`NONE` and 2 `GPL-3.0`. A 96% permissive share, against a 76.4% NO-GRANT rate across the
university-published estate as a whole** (`repos/trending.md`, this pass). 🔴 **UCT files under
EMEA per this KB's schema, which is the region with the *worst* no-grant rate (83.7%) — so the
regional average predicts nothing about an individual publisher.** `ECL-2.0` is the **Educational
Community License**, the Apereo/Sakai sector grant, and this is the first estate in this KB where it
is the dominant licence rather than a curiosity.

| Repo | Licence (byte-read) | ★ | Pushed | Why it is foundational |
|---|---|---:|---|---|
| [`cilt-uct/tsugi-request-gradebook-upload`](https://github.com/cilt-uct/tsugi-request-gradebook-upload) | **Apache-2.0** — `main/LICENSE`, **11,357 B**, `sha256₁₂ b40930bbcf80` | 0 | 2026-10-06 | **The single most transferable row here.** Schedules the upload of **Brightspace (Amathuba) gradebook items into PeopleSoft via middleware** — the exact student-record write-back every LMS-adjacent engagement has to build and nobody publishes. A worked, permissive reference for the grade-to-SIS boundary. |
| [`cilt-uct/tsugi-migrate-to-brightspace`](https://github.com/cilt-uct/tsugi-migrate-to-brightspace) | **Apache-2.0** — `main/LICENSE`, **11,357 B**, `sha256₁₂ c71d239df917` | 0 | 2026-10-22 | Invokes the Sakai archive web service from inside a Sakai site and reports completion back to the user. **An LMS *migration* tool written by the institution doing the migration** — the posture a client in the same position needs. |
| [`cilt-uct/qna`](https://github.com/cilt-uct/qna) | **ECL-2.0** — `master/LICENSE`, **11,120 B**, `sha256₁₂ 0688f62d04f1` | 0 | 2024-08-24 | Anonymous student Q&A with popularity ranking and categories, answerable by students, lecturers or tutors — built jointly by **UNISA and UCT**. 🟡 Quiet since 2024; take it as a data model and a moderation design, not a dependency. |
| [`cilt-uct/sakai-skin-vula`](https://github.com/cilt-uct/sakai-skin-vula) | **ECL-2.0** — `master/LICENSE`, **11,120 B**, `sha256₁₂ 0688f62d04f1` | 4 | 2026-06-03 | UCT's Morpheus skin for its Sakai deployment. 🔴 **Its default branch is `r/23.x`** — neither `main` nor `master`. It was byte-read only because the repository *also* still carries `master`; a release-branch default is invisible to this KB's grant ladder (`884-G2`). |

🟡 **The wider estate, not shelved row-by-row but worth naming:** `tsugi-student-allocation`,
`tsugi-student-analytics`, `tsugi-course-level-dashboard`, `tsugi-deliver-student-files`,
`tsugi-explorance-grademark`, `Brightspace-HTML-Templates`, plus an Opencast lecture-capture
operations set (`oc-scripts`, `fallback-capture-agent`, `docker-fallback-orchestrator`, pushed
**2026-11-17**). 🔵 **`Tsugi` is the common thread and it is the reusable idea:** these are LTI apps
mounted into whichever LMS the institution runs, which is how you ship function into an incumbent
platform without forking it.

### 🟢 `UniversityOfHelsinkiCS` — the student-information-system seam, MIT and current

🟡 **63 repositories, exactly half licensed** (`MIT` ×30, `NONE` ×30, one each `NOASSERTION`,
`GPL-3.0`, `Apache-2.0`). The licensed half is the useful half.

| Repo | Licence (byte-read) | ★ | Pushed | Why it is foundational |
|---|---|---:|---|---|
| [`UniversityOfHelsinkiCS/sis-importer`](https://github.com/UniversityOfHelsinkiCS/sis-importer) | **MIT** — `master/LICENSE`, **1,111 B**, `sha256₁₂ c54478a86110` | 1 | **2026-11-16** | Importer against **Sisu**, the Finnish higher-education SIS. The ingestion end of the student-record boundary, MIT, and pushed two days before this pass. |
| [`UniversityOfHelsinkiCS/suoritustarkistin`](https://github.com/UniversityOfHelsinkiCS/suoritustarkistin) | **MIT** — `master/LICENSE`, **1,111 B**, `sha256₁₂ 7b658dd8f1a0` | 1 | **2026-11-17** | *SUOTAR* — helps **graders report course completions**. 🔵 The credit-award step: the one workflow in this whole vertical where an AI system must *not* act autonomously, here implemented as explicit human reporting. Read it before designing any grading automation for an EU client. |
| [`UniversityOfHelsinkiCS/sis-ns-manager`](https://github.com/UniversityOfHelsinkiCS/sis-ns-manager) | **Apache-2.0** — `master/LICENSE`, **11,357 B**, `sha256₁₂ c71d239df917` | 0 | 2026-11-10 | Sisu integration manager for teacher and course administration. |

### 🟢 Canvas and Sakai client libraries from the institutions that run them

| Repo | Licence (byte-read) | ★ | Pushed | Why it is foundational |
|---|---|---:|---|---|
| [`KTH/canvas-api`](https://github.com/KTH/canvas-api) | **MIT** — `master/LICENSE`, **1,098 B**, `sha256₁₂ 5e0ff14e95f0` | 10 | **2026-11-16** | Node.js client for the Canvas LMS API, maintained by **KTH Royal Institute of Technology**. 🔵 **Pair it with `vishalsachdev/canvas-mcp`** (`agents/top.md`): the MCP server gives an agent Canvas *tools*, this gives your own services typed Canvas *calls*. Both MIT. |
| [`KTH/lms-nightly-sync`](https://github.com/KTH/lms-nightly-sync) | **MIT** — `main/LICENSE`, **1,099 B**, `sha256₁₂ f2fa6a58e259` | 0 | 2021-01-12 | Periodic synchronisation of KTH databases into Canvas. 🟡 **Frozen since 2021** — a reference for the batch-sync pattern, not a dependency. |
| [`kyoto-u/comfortable-sakai`](https://github.com/kyoto-u/comfortable-sakai) | **Apache-2.0** — `master/LICENSE`, **11,357 B**, `sha256₁₂ c71d239df917` | 25 | 2023-03-15 | Browser extension improving Sakai's UX, from **Kyoto University**. 🔵 **The only APAC row in this category**, and an instructive posture: when you cannot change the institutional LMS, ship the improvement to the *client side*. 🟡 Quiet since 2023. |
| [`AaltoGIS/classroom-grader`](https://github.com/AaltoGIS/classroom-grader) | **BSD-3-Clause** — `main/LICENSE`, **1,504 B**, `sha256₁₂ d25a8300ad2c` | 1 | **2026-11-09** | Grading automation around **GitHub Classroom**, from Aalto University. 🔴 **Its GitHub description is empty** — exactly the class of repository `p883` proved keyword discovery cannot see. |

### 🟢 Teaching-grade reference implementations — permissive, high-traction, built to be read

🔵 **A distinct role from the plumbing above: these are systems written to TEACH a subject**, at a
scale and quality that makes them credible engineering references in their own right.

| Repo | Licence (byte-read) | ★ | Pushed | Why it is foundational |
|---|---|---:|---|---|
| [`cmu-db/bustub`](https://github.com/cmu-db/bustub) | **MIT** — `master/LICENSE`, **1,075 B**, `sha256₁₂ cea46dcabf9a` | **5,171** | 2026-11-13 | **The highest-traction education repository `p884` found, and new to this KB.** Carnegie Mellon's teaching RDBMS, the backbone of its database course and **2,085 forks** of coursework. 🔵 The reference design for *"a real system, deliberately incomplete, with the gaps as the assignments"* — the single most reusable pattern in technical curriculum design, and directly applicable to a client building an engineering academy. |
| [`RWTH-OS/eduOS-rs`](https://github.com/RWTH-OS/eduOS-rs) | 🔴 **`Apache-2.0 OR MIT`** — a **SPLIT-FILE** grant: `main/LICENSE-APACHE` (**9,722 B**) **and** `main/LICENSE-MIT` (**1,023 B**) | **493** | 2026-10-04 | A teaching operating system in Rust, from RWTH Aachen. 🔴 **This row is also a method finding.** GitHub's single `license.spdx_id` field reports `Apache-2.0` **alone**, and this KB's grant probe reported **`NO-GRANT-FILE`** — it tried 16 single-file paths, none of them the Rust ecosystem's two-file convention. **One grant field cannot express two grants, and a studio told "Apache-2.0" loses the MIT option it is entitled to.** Probe and classifier fixed with 5 controls this pass. |

## 🟢 Rows the full-estate recount surfaced — new in `p880`

🔵 **`p880` re-ran `p879`'s organisation census to EXHAUSTION rather than to the top 40 by stars**
(`2,574` source repositories across `31` owners; method and the sampling correction on
[`repos/trending.md`](trending.md) this pass). 🟡 **The honest yield is small, and that is itself the
result:** paging a census from `571` rows to `2,574` produced **four** rows worth shelving. 🟢 **It
independently reconfirms `T12` from the denominator side** — the reason this index has a short head
and a long tail is not that the base has been looking in the wrong place.

🟢 **Every licence below was byte-read this pass over `raw.githubusercontent.com`, hashed
`sha256`-12, and the record is
[`evidence/licence-byteread.2026-11-17-p880.tsv`](../evidence/licence-byteread.2026-11-17-p880.tsv).**

| Repo | Licence (byte-read) | ★ | Pushed | Role |
|---|---|---:|---|---|
| https://github.com/apereo/java-cas-client | 🔵 **CONJUNCTIVE — Apache-2.0 *and* BSD-3-Clause** (`LICENSE`, `2,321 B`, `6c21b465e3a0`) | **949** | 2026-11-16 | **The Java CAS client** — how a JVM estate attaches to the `apereo/cas` SSO layer `p879` filed. Completes the identity triple with `phpCAS` (PHP) and `cas` (server). 🔴 **Read the licence note below before quoting it as "Apache-2.0".** |
| https://github.com/instructure/instructure-ui | **MIT** (`LICENSE.md`, `1,175 B`, `9773f00c68af`) | 487 | 2026-11-17 | **Canvas's own accessible React component library**, shipped by Instructure. The MIT design-system counterpart to Open edX's Apache-2.0 `paragon` — i.e. a client already on Canvas can be given a UI that matches it without touching the AGPL-3.0 `canvas-lms` core. |
| https://github.com/instructure/common-cartridge-viewer | **MIT** (`LICENSE`, `1,074 B`, `21f8b02800eb`) | 95 | 2026-11-04 | **Renders IMS Common Cartridge packages in the browser.** The content-portability seam: a client's existing courseware can be read and inspected without importing it into any platform first. Pairs with the standards layer below. |
| https://github.com/mitodl/ol-infrastructure | **BSD-3-Clause** (`LICENSE`, `1,529 B`, `88bb0e3a8731`) | 59 | 2026-11-17 | **MIT Open Learning's own production infrastructure automation**, Pulumi/Python. 🔵 A reference deployment topology for an Open edX estate published by an institution that actually runs one at scale — rare, and worth reading before estimating one. |

> 🔵 **`apereo/java-cas-client` is this base's cleanest live example of a CONJUNCTIVE grant, and a
> single-family label on it would be wrong.** The `2,321 B` payload carries **two** grants: an
> Apache-2.0 notice (*"Apereo licenses this file to you under the Apache License, Version 2.0"*)
> **and** a separate `License for Use` section that is a full **BSD-3-Clause** text with a
> `Copyright (c) 2007, JA-SIG, Inc.` holder and a no-endorsement clause.
> 🟢 **Both families are permissive, so the repository is build-safe** — but the **notice obligation
> is of two**, and the BSD no-endorsement term names JA-SIG specifically. 🔴 **`p880`'s own first
> pass at this file classified it `BSD-family` on a first-match grep and would have published a
> single wrong family;** the instrument now detects families cumulatively. A hash and a byte count
> do not save you from a one-family assumption.
>
> 🔴 **`p887` ran a NEW instrument over this row and got it WRONG in exactly the way this note
> already describes.** `compose/code/p887-grant-arity-map/` reused `p228-shelf-gate`'s
> `classify()` — an earliest-title-wins classifier — and returned **`arity_own=1 BSD-3-Clause`**
> for `java-cas-client`, because the Apache-2.0 half of this payload is a grant *by reference*
> (a URL, no body) while the BSD half is a full text. 🟢 **The shelf was right and the new
> instrument was wrong, on a row whose correct answer is written two lines above this one.**
> 🔵 And a third channel agrees with neither: **GitHub's own licence detector returns
> `NOASSERTION`** on this repository (metadata channel, `p887`) — which is the cheapest known
> DETECTOR for this class, and the one reusable rule this pass buys:
>
> > 🟢 **A row whose metadata channel says `NOASSERTION` while its bytes channel returns a
> > family is a CONJUNCTIVE-GRANT CANDIDATE.** `java-cas-client` is the only `NOASSERTION` row
> > among the 15 swept at `p887`, and it is the only single-payload conjunctive grant among
> > them. One API field, no clone.
>
> 🔴 **Its sibling `apereo/phpCAS` (`:465`) carried a single-family `Apache-2.0` label until
> `p887` byte-read its `NOTICE`.** Same consortium, same no-endorsement clause, same two
> families — the only difference is which FILE the BSD half sits in, and that difference was
> enough to hide it for the entire life of this shelf.

## Document & media ingestion — the real bottleneck in education AI

Education content arrives as PDFs, scanned worksheets, lecture video and textbooks. Ingestion
quality, not model quality, is what usually determines whether a tutoring build works.

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/docling-project/docling | MIT | `main` | Document parsing to structured output (IBM-originated, now a Linux Foundation AI project). MIT, strong on tables and layout — the default first choice for curriculum and textbook ingestion. |
| https://github.com/datalab-to/marker | Apache-2.0 | `master` | PDF → markdown with high fidelity on equations and tables. Strong on STEM textbooks where Docling's maths handling is not enough. |
| https://github.com/opendatalab/MinerU | **"MinerU Open Source License"** (Apache-2.0 + additional terms) | `master` | High-quality PDF extraction including formulas. **Flag sharpened by `p872` — the terms were read, not just noted.** `LICENSE.md` is titled *MinerU Open Source License* and states MinerU is Apache-2.0 **"subject to the additional terms below"**. Those terms include: (1) **a separate commercial licence is required** once you and your affiliates, consolidated, exceed **100 million MAU** *or* **USD 20 million monthly revenue**; and (2) an **online-service attribution obligation**. For a normal institutional education deployment neither threshold binds, so MinerU is usable — but the attribution obligation applies immediately to any hosted service, and the thresholds must be checked before embedding it in a product sold at scale. |
| https://github.com/Unstructured-IO/unstructured | Apache-2.0 | `main` | Broad-format ingestion (docx, pptx, html, email). Useful for the long tail of institutional file formats. |
| https://github.com/openai/whisper | MIT | `main` | Lecture and classroom speech-to-text. MIT weights and code. |
| https://github.com/SYSTRAN/faster-whisper | MIT | `main` | CTranslate2 reimplementation — several times faster, materially cheaper for transcribing a full semester of lecture capture. |

## Retrieval, orchestration & serving substrate

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/HKUDS/LightRAG | MIT | `main` | Graph-augmented RAG. Worth naming explicitly: it is the retrieval engine **inside DeepTutor**, so adopting DeepTutor means adopting LightRAG. MIT. |
| https://github.com/infiniflow/ragflow | Apache-2.0 | `main` | Document-understanding-centric RAG engine with a usable ingestion UI — good fit where institutional staff, not engineers, curate the corpus. |
| https://github.com/deepset-ai/haystack | Apache-2.0 | `main` | Mature, composable RAG/agent pipelines. Apache-2.0 and stable API — the conservative choice for a multi-year institutional contract. |
| https://github.com/BerriAI/litellm | MIT | `main` | One OpenAI-shaped API across providers, with per-key budgets and rate limits. In education this is the cost-control and model-swap seam: a ministry that mandates a sovereign model later changes one config, not the application. |
| https://github.com/ollama/ollama | MIT | `main` | Local model serving. The answer to "student data must not leave the building" and to low-connectivity deployments. |
| https://github.com/vllm-project/vllm | Apache-2.0 | `main` | High-throughput serving. What you run when a whole cohort hits the tutor during one lab session. |
| https://github.com/qdrant/qdrant | Apache-2.0 | `master` | Vector store, Apache-2.0, self-hostable. |
| https://github.com/chroma-core/chroma | Apache-2.0 | `main` | Lighter vector store; fast to stand up for a pilot. |
| https://github.com/mem0ai/mem0 | Apache-2.0 | `main` | Persistent memory layer — the difference between a chatbot and a tutor that remembers a learner across a term. |
| https://github.com/temporalio/temporal | MIT | `main` | Durable workflow execution. Education workloads are long-running and bursty (term-long learning paths, overnight batch grading); Temporal is what keeps them correct across restarts. |

## Evaluation & data quality — how an education claim gets defended

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/promptfoo/promptfoo | MIT | `main` | Prompt/model regression testing and red-teaming. Education needs this for safeguarding checks on learner-facing output. |
| https://github.com/EleutherAI/lm-evaluation-harness | MIT | `main` | Standard academic benchmark harness — the credible way to report model capability to an academic buyer. |
| https://github.com/HumanSignal/label-studio | Apache-2.0 | `develop` | Human annotation, including rubric-scoring interfaces for building graded gold sets. |
| https://github.com/argilla-io/argilla | Apache-2.0 | `develop` | Human feedback and dataset curation, oriented to SME review — fits teacher-in-the-loop validation. 🟡 **`p876` liveness flag, new and not caught by any previous pass: `pushed_at` reports `2026-11-16` (yesterday), but the default branch `develop` last moved `2025-08-05` and has `0` commits in 12 months.** It looks maintained in every star-and-push sweep this KB has ever run and is not. Usable — it is a mature tool — but do not promise upstream fixes. |
| https://github.com/wwrwbs/AI_AWE | Apache-2.0 | `main` | **ArguLens** — automated essay scoring with feedback. Enters the foundations layer because its **scorer is a grade-independent LightGBM model over 31 explicit linguistic/discourse features**, not an LLM: a reproducible, inspectable score is the only kind that survives an appeal or a high-risk conformance review. **v0.1.0, research-grade; corpus is US middle-school English (Persuade 2.0)** — re-fitting on local graded essays is required work, not polish. See `agents/top.md`. |

**36 verified foundational repos** — `p876` adds `yetanalytics/lrsql`, `openfun/ralph` and `adlnet/ADL_LRS`.

**Previous count:** 33 (31 from `p871`, plus `openedx/edx-ora2` recorded as the
canonical address and `wwrwbs/AI_AWE` added by `p872`).

## Declared gaps
### 🟢 `p879` — gaps opened, closed and declared

- 🟢 **CLOSED:** *"`openedx/edx-platform` cannot be measured"* — stale slug, not a channel hole.
- 🔴 **OPEN, and named precisely: `user:UCBerkeley-OATutor` returns `422`.** OATutor is carried in
  this KB under an owner the search index does not recognise, so the address is wrong somewhere.
  **Not repaired this pass.** The fix is one `in:name` query plus a byte-read; it is left for the
  next pass rather than guessed at here.
- 🔴 **The census is owner-first, and the owners came from addresses this KB already held** — all
  of them US, EU or APAC. **No LATAM-headquartered organisation could appear**, by construction.
  🟡 That is a limit of this pass's method, **not** a finding about LATAM supply; `p878`'s
  Spanish/Portuguese keyword legs are the channel that answers it.
- 🔴 **No APAC *institutional* estate surfaced** — no university or ministry organisation. The
  region's permissive producers in this census are labs (`HKUDS`, `THU-MAIC`), not institutions.
- 🟡 **The licence probe used here tried six filenames and still produced three false negatives**
  (`LICENSE.TXT` with an uppercase extension on the XBlock repos; `package.json`-only licences on
  `moodleapp` and `h5p-interactive-video`). **A later pass must extend the probe** to `LICENSE.TXT`,
  `package.json`, `pyproject.toml` and `setup.py` before recording any `NOASSERTION` (`T14`).


- **The permissive/copyleft split is the central licence fact of this vertical.** The AI
  substrate above is almost entirely MIT/Apache-2.0, and the standards plumbing is mixed, but
  the *platform* layer (see `verticals/solutions.md`) is overwhelmingly GPL/AGPL. A Globant
  engagement should expect to build permissive AI services that **integrate with** copyleft
  platforms over LTI/xAPI rather than forking them.
- ~~**No open-source student-information system with a permissive licence was found.**~~
  🟢 **CLOSED by `p877`: [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is MIT at the
  bytes** (1,150 B, `sha256₁₂ b8694396d7dc`) — a Laravel, API-first, Dockerised school management
  system with companion Android apps, 113 commits in 12 months. It is **small** (57★) and its HEAD
  is five months old, so the gap closes on *licence*, not on *maturity*: the honest statement to a
  client is "the only permissive SIS base exists and you would be adopting it, not joining it."
  The copyleft options remain what they were — Gibbon GPL-3.0; RosarioSIS GPL-2.0 (default branch
  **`mobile`**); and `OS4ED/openSIS-Classic` has **no licence file in its repository at all**, its
  GPL claim appearing only in the README, so that one is still not a clean grant.
- 🔵 **A `NOASSERTION` from the GitHub licence API is not evidence of anything** — see the T14 table
  at the top of this file. `p877` found one permissive-with-an-added-line, one
  permissive-with-a-manifest and one genuinely proprietary repository behind the same token. **Any
  row this KB ever wrote off as "no licence" on API evidence alone must be re-read at the bytes
  before it is treated as unusable.**
- `apereo/opencast-admin-interface` **does not exist** (`git ls-remote` returned nothing). The
  real address is `opencast/opencast`, and `p872` adds its default branch: **`develop`**, not
  `main`, licence **ECL-2.0**. A clone pinned to `main` fails outright.
- **Non-`main` default branches are the single most productive source of wrong data in this KB,
  and `p873` makes the case worse in kind.** `p872` found four of eleven audited addresses not
  defaulting to `main` — `opencast`, `oppia` and `kolibri` → `develop`; `edx-ora2`, `ltijs`,
  `OpenOlat` and `sakai` → `master`. `p873` adds **`francoisjacquet/rosariosis`, whose default
  branch is `mobile`** — a *feature* name that no heuristic would guess and nothing in the address
  hints at. State it as a hard rule: **never construct a `raw.githubusercontent.com` path from an
  assumed branch; resolve it with `git ls-remote --symref <url> HEAD` first.** A guessed `main`
  404s, the 404 reads as *"no licence file"*, and *"no licence file"* gets published as
  **"no grant — cannot build on it"**. That one shortcut would have libelled RosarioSIS's licence
  this pass and `opencast`'s last pass; phantom licences and phantom absences, the two most
  expensive wrong-data classes here, both come from it.
- **A second class of branch error: the code may not be on the default branch at all.** `p873`'s
  headline find, **`LabSirius/TutorIA`** (MIT, Colombia — see `agents/top.md`), has a default
  branch holding **documentation only**; its backend lives on `feature/refactor-to-v2-requirements`,
  and the address its own README tells you to clone (`Sof1SP/tutorIA`) has **no code in any
  branch**. Existence, licence and default branch can all verify cleanly on a repository that
  would still ship nothing. For any repo proposed as a *build base*, confirm a load-bearing source
  file resolves — not just `LICENSE`.
- **A substring grep cannot characterise a licence.** `p872` tried to automate the
  "Apache-2.0 + additional terms" check and got a **100% false-positive rate** on Apache-2.0,
  because §5 of the licence contains the phrase *"without any additional terms or conditions"*.
  Seven clean repos were flagged; the flag was **discarded rather than published**.
  `opendatalab/MinerU` remains the single genuine case in this KB, because its `LICENSE.md` adds
  substantive terms in prose. Automate existence and branch resolution; read the bytes for
  licence meaning.
- **No permissively licensed proctoring component exists at the foundations layer either.**
  The two real candidates found by `p872` are both AGPL-3.0 — see `verticals/solutions.md`.
