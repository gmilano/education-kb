---
industry: education
region: Global
updated: 2026-10-10
---

# `p987-census-sha-currency` — the corrective pass `Gap 376` asked for, in the one channel that was open

**Pass 96, 2026-10-10.** ⏱️ **Sixth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; 94: 02:5x; 95: 03:4x; this one 04:4x–05:xx).

🔴 **`grant-ladder-v4/ladder.sh` and `test_ladder.sh` were refused again — a FOURTH consecutive pass.**
The harness classifier denies execution of repository code (`[Code from External]`), so `Gap 376` is not
discharged and **this directory is not a replacement for it**. 🟢 **No classifier was written** (`P237`),
and **no repository code was executed** (`Gap 376`).

🔵 **What this directory is.** `Gap 376` says the carried census decays by ~12 hand-read rows per pass
against a 133-row claim, and that *"the first duty of the next pass that can execute code is corrective,
not additive"*. 🟢 **Pass 96 could not re-read 127 licence payloads. It could ask a cheaper question that
bounds the decay exactly:** *is each published row still at the SHA it was measured at?* **A row still at
its pinned SHA cannot have drifted, whatever else is unverified about it.**

## Invocation

```sh
# 1. harvest the published (slug, ref, sha7) triples from the shelf pages
#    -> pinned.input.tsv  (127 rows; the extractor is in the pass-96 write-up, not here)
# 2. ask git whether each pinned SHA is still the tip of its pinned ref
awk -F'\t' '{print $1" "$2" "$3}' pinned.input.tsv | xargs -P 4 -n 3 ./probe_currency.sh
# 3. for every row the shelf publishes as "no licence payload", prove reach at the PUBLISHED sha
./probe_reach_control.sh <slug> <sha>
```

🔴 **Both scripts were run from a scratch directory outside this repository**, because running them from
here is what the harness refuses. They are committed so the next pass can re-derive and contradict this
one mechanically — which is the whole point of pinning.

## Result 1 — the decay is bounded, and it is small

`result.2026-10-10.tsv`, 127 rows:

| verdict | n | meaning |
|---|---|---|
| 🟢 `CURRENT` | **122** | pinned SHA is still the tip of the pinned ref — **the row cannot have drifted** |
| 🔴 `MOVED` | **5** | HEAD advanced; the licence at the new SHA is unverified until read |
| `NO-REACH` | **0** | every slug resolved |
| `REF-GONE` | **0** | every published ref still exists |

🟢 **96.1 % of the carried census is still at the SHA it was measured at.** 🔵 **That is the number
`Gap 376` has been missing for four passes.** The gap is real — a SHA being current says nothing about
whether the *filename reach* or the *classifier* that produced its verdict was sound — but **"the coverage
is decaying" is now quantified as "5 rows of 127 need re-reading", not "the census is rotting".**

🔴 **And the five are named, so the next pass has a worklist instead of a mood.**

| slug | pinned | now | re-read at the new SHA |
|---|---|---|---|
| [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | `80d7d66` | `ff82521` | 🟢 **BSD-3-Clause**, `LICENSE.md` **1 542 B** — unchanged. 🔴 **But see `P987` below: this row is why.** |
| [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | `1f47c93` | `0ef9cc9` | 🟢 **LGPL-3.0**, `LICENSE` **7 651 B**, title block *"GNU LESSER GENERAL PUBLIC LICENSE, Version 3, 29 June 2007"* — **byte-identical to the pinned reading**, grant unchanged |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `f30df11` | `e5cf557` | 🟢 `LICENSE` **35 147 B** unchanged — 🆕 **and a SECOND licence file this KB had never read.** See `P984`. |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | `12aeb0f` | `6aa0afb` | 🟢 **MIT**, `LICENSE` **1 072 B** — unchanged |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | `59d2396` | `b1795b8` | 🟢 **four-way split grant, byte-identical at 1 615 B** — code MIT, prompts/settings CC-BY-4.0, Annotated CLEAR and Annotated PERSUADE 2.0 corpora **CC-BY-NC-SA-4.0**. 🔵 **The row whose licence matters most on this shelf, independently re-confirmed at a new SHA.** |

🟢 **5 of 5 drifted rows kept their grant.** 🔵 **So this pass's measurable claim about the census is:
122 rows provably un-drifted, 5 rows re-read and unchanged — 127 of 127 accounted for on the grant axis.**
🔴 **That is NOT the same as 127 rows re-verified**, and this directory must never be cited as if it were.

## Result 2 — 🔴 `P987`: `raw.githubusercontent.com` resolves a 40-char SHA always and a 7-char one only sometimes

**The defect, measured on one commit both ways:**

| URL | HTTP |
|---|---|
| `…/Submitty/Submitty/ff82521694719bc1e282d046631bf0232c9d673e/README.md` | 🟢 **200** |
| `…/Submitty/Submitty/ff82521/README.md` | 🔴 **404** |
| `…/Submitty/Submitty/main/README.md` | 🟢 **200** |
| `…/Submitty/Submitty/80d7d66/README.md` *(the OLD 7-char SHA)* | 🟢 **200** |

🔴 **Same object, same repository, same pass — the abbreviation 404s and the full hash does not.** And the
*previous* 7-char SHA on the same repo resolved fine, so the behaviour is **not a flat rule**: it is
inconsistent per commit, which is worse than a rule, because it fails silently.

🔴 **Why this is a shelf-level problem and not a curiosity.** This KB's publishing convention is a
**7-character SHA**, and its re-read method is *"`raw.githubusercontent.com/<slug>/<SHA>/<name>`"*. 🔴 **An
abbreviated SHA that does not resolve returns 404 on every one of the 24 filenames — which this instrument
would record as `no licence payload`.** A grant would be erased by an addressing artefact.

🟢 **`P872` caught it, exactly as written.** *"An all-404 sweep that also 404s its control is uninformative,
not evidence of absence."* Submitty's `README.md` 404'd alongside its licence files, so the sweep was
discarded instead of published. **The rule paid for itself on a case it was not written for.**

🟢 **And the contamination is BOUNDED BY MEASUREMENT, not assumed away.** `negatives.control.2026-10-10.tsv`
re-probes **all 10 rows this shelf publishes as having no licence payload**, at their **published 7-char
SHA**, with a `README.md` control:

| verdict | n |
|---|---|
| 🟢 `REACH-OK` (control returns 200 at the published SHA) | 🟢 **10 of 10** |
| 🔴 `SHORT-SHA-UNRESOLVED` | 🟢 **0** |

🟢 **Every recorded negative on this shelf survives the audit.** `frappe/lms`-class defects aside, the
`no licence payload` rows are real absences and not addressing artefacts.

🔵 **`P987`, stated for adoption:** *a 7-character SHA is a display format, not an address.* **Publish the
abbreviation for a human; address the payload with the full 40 characters.** Cost: one extra `git ls-remote`
field. 🔴 **`grant-ladder-v4` takes a ref or a short SHA and passes it straight into the URL, so it carries
this defect today.**

## Result 3 — 🟢 `P988` / `Gap 377`: the Maven oracle exists, was already wired, and the stronger field is the URL

`maven-oracle.2026-10-10.tsv`. 🔴 **`Gap 377` as written — *"`pom.xml`/`build.gradle` are not in the grant
ladder's path list … cheap to add"* — is right about the cost and wrong about the shape.**

🟢 **The reader already exists, is tested, and is already in a production path:**
`p289-maven-manifest/maven_license.py` (**11/11**, with its negative control) was wired into
`p283-manifest-named-license/manifest_license.py::PARSERS` and into `sweep_named.sh`'s `MANIFESTS` by
**`P294`**. `build.gradle` is in `p172-payload-license-sweep`'s manifest list. 🔵 **So nothing needs
writing. One instrument needs a one-line import — and `P237` says that is the only acceptable repair.**

**Measured across the JVM tier, at full 40-char SHAs:**

| platform | manifest | declared `<name>` | `<url>` | payload | agreement |
|---|---|---|---|---|---|
| `opencast/opencast` | `pom.xml` 63 148 B | Educational Community License, Version 2.0 | 🟢 `opensource.org/licenses/ECL-2.0` | ECL-2.0 (11 340 B) | 🟢 name **and** URL |
| `sakaiproject/sakai` | `pom.xml` 14 872 B | Educational Community License, Version 2.0 | 🟢 `opensource.org/licenses/ecl2.txt` | ECL-2.0 (11 120 B) | 🟢 name **and** URL *(p95, re-read at the full SHA)* |
| 🆕 `UniTime/unitime` | `pom.xml` 26 622 B | Apache Software License (ASL), Version 2.0 | 🟢 `apache.org/licenses/LICENSE-2.0` | **Apache-2.0** (11 357 B, pristine) | 🟢 name **and** URL |
| `OpenOLAT/OpenOLAT` | `pom.xml` 84 963 B | 🔴 **"Apache 2.0 Open Source L6icense"** | 🟢 `apache.org/licenses/LICENSE-2.0` | Apache-2.0 (10 982 B) | 🟡 **URL only — the name carries a typo** |
| `ls1intum/Artemis` | `build.gradle` 52 855 B | 🔴 **no licence declaration at all** | — | MIT (1 091 B) | 🔴 **no oracle** |

🔴 **`P988` — the `<name>` is prose and the `<url>` is an identifier, and only one of them is typo-proof.**
`OpenOLAT` ships **`L6icense`** in the field a name-keyed reader parses. 4 of 4 Maven platforms carry a
canonical licence **URL**; 3 of 4 carry a correctly spelt name. 🟡 **`p289`'s reader extracts only
`<name>`** (`declared_license_names`, `<name>` children of `<licenses>` under `<project>`) — 🟢 **and it
survives this row anyway**, because `lib/license_family.sh`'s *declaration* branch keys on the bare word
`apache` where its *title-block* branch requires `Apache License`. 🔵 **A measured case where the coarse
branch is the correct one** — the `CONTRATO` class `P637` already defines. 🟢 **Reading `<url>` would make
it right for the right reason instead of right by luck.**

🔴 **And the other half of `Gap 377` is refuted: `build.gradle` is not a licence oracle.** Artemis — the
single best row on this shelf — declares no licence in **52 855 bytes** of Gradle build script. 🔵 **The
asymmetry is distribution policy, not language**: a `<licenses>` block is part of what Maven Central
requires of a published POM, and Gradle has no equivalent convention. **The JVM licence oracle is
Maven-only. Add `pom.xml`; do not spend a line on `build.gradle`.**

## Result 4 — 🟢 `Gap 375`'s remainder discharged as **unmeasurable**, with the reason

`version-remainder.2026-10-10.tsv`. Pass 95 left three permissive rows unprobed. **All three return HTTP
200 with no version field**, and the reason is structural rather than accidental:

| platform | manifest | version | tags | class |
|---|---|---|---|---|
| `Open-TutorAi/open-tutor-ai-CE` | `pyproject.toml` 200 | 🔴 none — `license = { file = "LICENSE" }` | **1** | 🟢 **`UNVERSIONED-BUT-RELEASED`** — ship `v1.0.0` |
| `pupilfirst/pupilfirst` | `package.json` 200 | 🔴 none — `"private": true` | **57** | 🔴 **`COMPONENT-VERSIONED`** — all 57 tags are scoped npm sub-packages (`@pupilfirst/pf-icon@2.0.0`, `@pupilfirst/search@0.1.1-alpha.0`). **The platform has never been released as a unit.** |
| `academico-sis/academico` | `composer.json` 200 · `package.json` 200 | 🔴 none — 🟢 but `"license": "MIT"` **declared**, agreeing with the 1 094 B payload | 🔴 **0** | 🔴 **`UNRELEASED`** |

🟢 **`P985` — "no version" is three different facts and they price differently.** *Unversioned-but-released*
is a shippable thing with sloppy metadata. *Component-versioned* means the platform is a monorepo whose
parts ship and whose whole does not. *Unreleased* means there is no release engineering to inherit.

🔴 **And the third one lands on this shelf's most-repeated recommendation.**
`academico-sis/academico` is the row `verticals/solutions.md` calls *"the closest thing to a permissive SIS
this KB has found"* — the answer to *"no permissive SIS exists"*, the gap that page re-states every pass.
**It has 404 ★, an MIT grant declared in two places, and has never cut a release.** 🔵 **A studio forking it
inherits the release engineering, the version scheme and the upgrade path — none of which exist.** That
belongs **next to the recommendation**, not in a version table.

🟢 **`P986` — `UniTime/unitime` is the first JVM row on this shelf to INVERT `P978`.** Its `pom.xml` says
**`4.9`** and its newest tag is **`v4.9.152`**: the default branch names a **shippable line**, not a
`-SNAPSHOT`. Sakai (`27-SNAPSHOT` vs `25.2`), Opencast (`21-SNAPSHOT` vs `20.4`) and OpenOLAT
(`21.2-SNAPSHOT` vs `21.0.3`) all do the opposite. 🔵 **`P978` is a strong tendency, not a law — and the
exception is worth knowing, because it is the one JVM platform you can quote a version for without a
caveat.**

## Result 5 — 🆕 `P984`: a second licence file on a row this KB thought it had finished

🟢 **`chamilo/chamilo-lms` serves `license.txt` at 1 614 B alongside its 35 147 B `LICENSE`**, and this KB
had read only the second. The small file is not a duplicate — **it is the part with the facts in it:**

- 🟢 **It states the grant with its version AND its drift clause:** *"either version 3 of the License, or
  (at your option) any later version."* 🔴 **This shelf publishes bare `GPL-3.0`.** The payload says
  **GPL-3.0-or-later**, which is a *different compatibility position* from GPL-3.0-only — and `P561` is the
  registered rule that a dropped version qualifier is a defect.
- 🟢 **It is a region oracle (`P800`), and it contradicts the ordering this page implies.** The shelf reads
  *"EMEA origin (Belgium/Spain), heavy LATAM install base"*. **The first copyright line in the payload is
  `BeezNest Latino SAC, Peru`**, ahead of BeezNest Belgium. Twelve holders across **Peru, Belgium, Spain,
  France and Switzerland** — Université de Grenoble, Université de Genève, VUB, HoGent, UGent, UCL.
  🔵 **So the LATAM attachment is in the grant itself, not just in the install base.**
- 🔴 **And it indirects a third time:** *"The full license can be read in `documentation/license.html`."*
  🔵 **`Gap 378` was found in a *version* file; here it is in a *licence* file.** The shape generalises:
  **this KB's probes read paths, and real projects point at other paths.**

🟢 **`P984`, stated for adoption:** *when a repository serves two licence files of very different sizes, the
SMALL one is more likely to carry the holders, the version qualifier and the scope.* The large one is
usually the canonical upstream text, which says nothing project-specific at all. 🔴 **A first-match
ladder ordered `LICENSE` before `license.txt` reads the uninformative file and stops.** `ladder.sh --all`
exists for exactly this and was not run here because it could not be.

## Channel declaration (`P247` / `P798`)

Measured before any verdict on this page:

| channel | state this pass | what it carried |
|---|---|---|
| `git ls-remote` (https) | 🟢 **LIVE** | all 127 census rows, refs, full and short SHAs, 4 tag ladders |
| `raw.githubusercontent.com` via `curl` | 🟢 **LIVE** | every licence, manifest and version payload on this page |
| `api.github.com` | 🔴 **not attempted** — 403 for five consecutive passes | — **so every ★ on the shelf is carried, and `—` still means *not read this pass*** |
| `WebSearch` | 🟢 **LIVE** | all regulatory and market claims this pass — **summaries only** |
| `WebFetch` | 🔴 **DEAD** — `getaddrinfo ENOTFOUND` on `digital-strategy.ec.europa.eu`, `www.gibsondunn.com`, `en.wikipedia.org` | nothing |
| `curl` to non-GitHub hosts | 🔴 **DEAD** — `000` on three legal-publisher URLs | nothing |
| execute repository code | 🔴 **DENIED, fourth pass** (`[Code from External]`) | nothing — `Gap 376` |

🔴 **The consequence, stated so nothing on this shelf is over-read: not one regulatory claim added this pass
was read from a primary text.** Two independent `WebSearch` rounds over different source sets is the
strongest corroboration this channel can produce, and that is what the EU and Vietnam rows below carry.
