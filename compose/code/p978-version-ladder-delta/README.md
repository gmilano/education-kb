# `p978-version-ladder-delta` — the default branch names a release you cannot install

**Pass 95, 2026-10-10 (fifth pass of this date).** Evidence directory.

🔴 **No executable here, deliberately — and for the THIRD pass running.** This session's sandbox declines
to run repository code: `bash compose/code/grant-ladder-v4/ladder.sh --reach` was refused before it
started, exactly as in passes 93 and 94. 🟢 **No replacement classifier was written** — `P237` forbids
forking the shared classifier to fix it, and `P970` says the correct response is to run the *oracle map* by
hand and print payloads instead of matching on them. **What is committed here is measurement, not an
instrument.**

🔴 **And that is now a registered risk in its own right (`Gap 376`).** `grant-ladder-v4` has not executed
since pass 92. Passes 93, 94 and 95 each hand-read ~12 rows on top of a published 133-row census, so the
coverage claim on these pages is decaying while the method stays sound. **The first duty of the next pass
that can execute code is corrective, not additive.**

## The finding (`P978`)

Pass 94 read Moodle's `main` as `6.0dev (MATURITY_ALPHA)` against `MOODLE_503_STABLE`'s `5.3`, and recorded
it as a Moodle quirk. 🟢 **Pass 95 measured three more platforms and it is the normal case, not a quirk.**

| platform | default branch | newest tag | delta |
|---|---|---|---|
| `moodle/moodle` | `6.0dev` *(p94)* | `5.3` stable | 1 major |
| `sakaiproject/sakai` | `27-SNAPSHOT` | `25.2` | **2 majors** |
| `opencast/opencast` | `21-SNAPSHOT` | `20.4` | 1 major |
| `OpenOLAT/OpenOLAT` | `21.2-SNAPSHOT` | `OpenOLAT_21.0.3` | 1 minor line |
| `ucbds-infra/otter-grader` | `7.0.0` | `v7.0.0` | **0 — the only agreeing row** |

🔴 **In every platform case measured, the version on the default branch is a release that does not exist
yet.** 🔵 For a KB whose platform tier answers *"what will we be deploying"*, publishing `27-SNAPSHOT` is
worse than publishing nothing — **it is a number that will never appear in a procurement document.**

🟢 **`P978`, stated mechanically:** *read the version file for the development line and the tag ladder for
the shippable one, and publish both.* One oracle is a reading; two disagreeing oracles are the finding.

## 🟡 The instrument's own limit, measured again (tag-namespace case collision)

`OpenOLAT/OpenOLAT` ships release tags under **two capitalisations of its own project name** —
`OpenOLAT_21.0.3` and `OpenOlat_20.0.pre2`. 🔴 **A case-sensitive `sort -V` therefore ranks a 20.x
pre-release above the newest 21.x release.** 🟢 **Fold case before sorting a tag ladder.** Same defect class
as `p288-agpl-casefold` and `p439-case-collision-gate`, found this time in a tag namespace rather than a
filename.

## 🟢 The second finding (`P979`) — `pom.xml` is also a licence oracle

Reading Sakai's root `pom.xml` for a version string returned something unasked for:

```xml
<name>Educational Community License, Version 2.0</name>
```

🟢 **An independent, payload-grade confirmation of the ECL-2.0 grant** that `verticals/solutions.md`
carries from `LICENSE` (11 120 B). 🔵 **ECL is precisely the family generic tooling returns as
*unclassified*** — the reason Sakai and Opencast were nearly dropped from the permissive tier in pass 89 —
**so a second concurring oracle is worth more here than anywhere else.** Recorded as `Gap 377`: add
`pom.xml` / `build.gradle` to the ladder's path list for JVM projects.

## 🔴 The third finding (`P973`'s second form, `Gap 378`) — the `public/` migration leaves a 404 **or** a shim

Moodle moved its web root into `public/` at 5.0 and left the root `version.php` as a **404**.
🟢 **Chamilo made the same migration and handled it the opposite way:**

- `main/install/version.php` → **404**
- `public/main/install/version.php` → **200**, whole body:
  `return require dirname(__DIR__, 3).'/version.php';` — **a shim pointing back to the repository root**
- root `version.php` → **200**, carrying the real `3.0.1`

🔴 **A path list alone cannot resolve this — the probe has to be willing to follow a one-line `require`.**
Same shape as `Gap 370` (per-directory licences): **this KB's probes read paths, and real projects
indirect.**

## 🔴 The fourth finding (`P980`) — resolve a tool to its repository, never to its distribution name

| what you cite | PyPI | repository | grant |
|---|---|---|---|
| `otter-grader` | `otter-grader` **7.0.0** | `ucbds-infra/otter-grader` | 🟢 **BSD-3-Clause** · 1 560 B |
| `Otter-Autograder` | `Otter-Autograder` **0.15.9** | **`OtterDen-Lab/Autograder`** | 🔴 **GPL-3.0** · 35 149 B |

🔴 **Two unrelated projects, both autograders for programming coursework, incompatible grants, seven major
versions apart.** A search summary reporting *"Otter-Autograder is GPL-3.0-or-later"* was reading the
**other** project. 🟢 **Only `project_urls` → Repository disambiguates them.**

🟡 **Secondary defect in the same read:** `Otter-Autograder`'s PyPI `license` field holds the **entire 35 kB
GPL-3.0 text**, with `license_expression: None`. Reading it for an SPDX id returns a licence *document*.
**Prefer the `classifiers` array — it was correct for both packages.**

## 🔴 A 200 is a file, not an answer — four measured ways

| slug | file | HTTP | what it carries |
|---|---|---|---|
| `instructure/canvas-lms` | `package.json` | 200 | `"version": "0.0.0"` — placeholder |
| `openfun/richie` | `src/richie/__init__.py` | 200 | `from importlib_metadata import version` — resolved at install |
| `Selleo/mentingo` | `apps/web/package.json` | 200 | no `version` field |
| `openedx/edx-platform` *(p94)* | `openedx/__init__.py` | 200 | docstring, 417 B |

🟢 **Instrument rule: a version channel must report `NO-VERSION-IN-PAYLOAD` as a value and never fall
through to the HTTP code.**

## Files

| file | what it holds |
|---|---|
| `pass95-versions.tsv` | 19 version-file reads: slug, ref, path, HTTP, version string, verdict |
| `pass95-ladders.tsv` | default-branch version vs newest release tag, with the delta and the case collision |
| `pass95-identity-collision.tsv` | `P980` — the two Otter projects across payload, manifest and registry layers |
| `pass95-scorer-grants.tsv` | `Gap 372`'s three measured negatives, plus the two permissive rows added this pass |

## What a pass that *can* execute code should do with this

1. **Re-derive the full 133-row census first** (`Gap 376`). Everything else here is additive; this is the
   only corrective item, and it has been deferred three times.
2. Add a **version channel** to `grant-ladder-v4`'s oracle map with **two readings per slug** — ladder from
   `ls-remote --tags` (case-folded), release string from the project's own version file — and
   `NO-VERSION-IN-PAYLOAD` as a first-class value. Fixtures ready above: `otter-grader` (agreeing),
   `sakai` (2-major delta), `canvas-lms` (placeholder), `richie` (install-time), `edx-platform` (docstring).
3. Add `pom.xml` / `build.gradle` to the **licence** path list for JVM projects (`Gap 377`), with Sakai as
   the fixture.
4. Teach the probe to follow a **one-line `require`/`include` indirection** (`Gap 378`), with Chamilo's
   shim as the fixture and Moodle's 404 as the control.
5. Add a **registry-identity check** (`P980`): resolve every named dependency through `project_urls` to a
   repository before reading any grant, with the two Otter packages as the fixture pair.
6. Do **not** build a classifier branch on `info.license` free text. `P237` exists because pass 91 forked a
   classifier on thin evidence and it cost two platform licences and one client recommendation.
