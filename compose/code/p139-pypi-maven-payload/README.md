---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-pypi-maven-payload` — `ACTION CM`: it is not an npm habit and not an open-source one. It is a **toolchain** property

**Executes p138's pre-registered `ACTION CM`**, written as:

> Probe the **PyPI and Maven** payload layers with the same method
> (`p138-npm-payload-licence` generalised). 🔴 *Refuted if the declared-but-absent rate is
> under 10% there — which would make the defect an npm packaging habit rather than an
> open-source one.*

## Verdict: **SPLIT — REFUTED on PyPI, NOT REFUTED on Maven**

| registry | artefacts measured | 🔴 declare a licence and ship no licence file | rate | against 10% |
|---|---|---|---|---|
| 🟢 **PyPI** | **11** (+1 absent from the registry) | 🟡 **1** — and it ships **nothing at all** | **9%** | 🟢 **REFUTED** |
| 🔴 **Maven Central** | **5** (+1 absent) | 🔴 **2 of 3 that declare; 2 of 5 overall** | **40–67%** | 🔴 **NOT REFUTED** |
| *(npm, p138)* | *21* | *7* | *33%* | *not refuted* |

🔵 **One number would have been the wrong answer.** The defect is not "open source" and not
"npm": it tracks the **default behaviour of each ecosystem's build tooling**.

- 🟢 **Python's backends put the licence in the artefact for you.** Under PEP 639, setuptools
  and hatch copy declared licence files into `<dist>.dist-info/licenses/`. **10 of 11** PyPI
  packages carried a licence file in *both* the wheel and the sdist, including every Open edX
  row probed. A maintainer gets this right by doing nothing.
- 🔴 **Maven's jar plugin puts nothing in for you.** A POM's `<licenses>` block is metadata in
  a *sibling file*; the jar on the classpath is unaffected. Shipping `META-INF/LICENSE`
  requires deliberate configuration, and **2 of the 3 declaring artefacts had not done it**.
- 🔴 **npm's `files` array names what to pack, and silently omits what is not there** — p138's
  `canvas-mcp-server` listed `LICENSE` and shipped 8 paths containing none.

## `P139-D1` — the Maven rows, and the copyleft one again

| coordinate | version | POM declares | jar paths | licence in jar |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` | 1.2.0 | Apache-2.0 | 70 | 🟢 `META-INF/LICENSE`, `META-INF/NOTICE` |
| 🔴 `edu.ksu.ome.lti:lti-launch` | 1.4.7 | 🔴 **LGPL-3.0** | 43 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | 25.2 | 🔴 **ECL-2.0** | **578** | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` | 20100527 | 🔴 **nothing** | 32 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing** | **524** | 🔴 **NONE** |
| — `uk.ac.ox.ctl:spring-lti13` | — | — | — | not on Central (**404**) |

All five resolvable jars were **sha1-verified against the repository's own `.sha1`**; no
mismatches.

🔴 **`edu.ksu.ome.lti:lti-launch` is p138's worst-case shape in a second ecosystem.** It is the
artefact built from [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) — the
LGPL-3.0 Kansas State library that **p137 identified as the LTI→OAuth-subject mapping `P13`
depends on** (`P137-A`). It declares the strongest obligation of the five and ships no text to
satisfy it, exactly as `moodle-mcp-server-aql` does with AGPL-3.0 on npm. 🔵 **The one
library this KB tells clients to build on is itself in the defect class.**

🔴 **`sakai-kernel-api` declares ECL-2.0; `sakai-kernel-impl` declares nothing.** Two artefacts
of one kernel, same release line, different licence posture — and the one with **578 paths**
is the one making the copyleft-adjacent claim with no text. ECL-2.0 is education's own
licence (an Apache-2.0 derivative with a patent clause written for universities), and it is
the kind of identifier a client's tooling will not recognise.

🔴 **`net.oauth.core:oauth` carries no licence signal at all, and is from 2010.** It is still a
transitive dependency of LTI 1.1 integrations. An artefact with no grant and no file is not
"permissive by default"; it is unlicensed, and 16 years of use does not change that.

## `P139-D2` — 🔴 the PyPI hit is not a licence defect. `openedx-learning` ships **no code**

The single PyPI row that declares a licence and ships no licence file is
**`openedx-learning` 0.33.1** — *"Open edX Learning Core (and Tagging)"*. It declares
`AGPL 3.0` by legacy field **and** classifier. Its wheel contains **4 paths**, all metadata:

```
openedx_learning-0.33.1.dist-info/METADATA
openedx_learning-0.33.1.dist-info/WHEEL
openedx_learning-0.33.1.dist-info/top_level.txt     ← 1 byte: empty
openedx_learning-0.33.1.dist-info/RECORD            ← lists only the four dist-info files
```

🔴 **The package is empty, and it became empty between releases:**

| version | wheel | sdist |
|---|---|---|
| 0.31.0 | 268 554 B | 192 313 B |
| 0.32.0 | 257 553 B | 189 430 B |
| 🔴 **0.33.0** | 🔴 **1 479 B** | 🔴 **1 748 B** |
| 🔴 **0.33.1** *(latest)* | 🔴 **1 479 B** | 🔴 **1 742 B** |

🔵 **`pip install openedx-learning` resolves to 0.33.1 and installs no modules.** Across **79
releases** the two most recent are the empty ones, so this is not an old artefact: it is the
current state of a core library of the dominant open-source higher-education platform. The
collapse from 257 KB to 1.4 KB between 0.32.0 and 0.33.0 is the signature of a packaging
regression — a build whose `top_level.txt` came out empty — shipped twice.

🟡 **It is therefore counted honestly in two ways.** As a licence row it is a hit, which is why
the PyPI rate is 9% rather than 0%. As a *finding* it belongs to a different class entirely,
and if it were excluded as degenerate the PyPI rate would be **0 of 10** and the refutation
even cleaner. 🔵 **The licence probe found a release defect, which is the second time this pass
that an instrument answered a question it was not asked.**

🟡 **One more PyPI row worth carrying forward**: `xblock-sdk` 0.15.2 ships **two vendored
`MIT.LICENSE` files from Jasmine 1.3.1** inside `sample_xblocks/*/static/js/lib/`, alongside
its own AGPL-3.0 `LICENSE.TXT`. That is `ACTION CJ`'s foreign-holder class, in a payload rather
than a repository tree — the two instruments of this pass meeting on one artefact.

🔵 **And a false-signal caution**: `moodle-dl` declares `GPL-3.0` with `license_files` **absent**
from its metadata, yet **ships** `LICENSE` in both distributions. A missing `License-File` field
does not imply a missing file — which is the mirror image of npm's `files` naming a file it does
not ship.

## 🔴 Two instrument errors caught before publication

1. 🔴 **The POM licence read was a greedy regex and returned developer names as licences.**
   The first run published `Braden Anderson` as the licence of `org.imsglobal:basiclti-util`,
   `Toby Murray` for `edu.ksu.ome.lti:lti-launch` and `Sakai Core Team` for
   `org.sakaiproject.kernel:sakai-kernel-api`. Flattening the XML and matching
   `.*<licenses>.*<license>.*<name>` runs past `</licenses>` into `<developers>`. 🔵 **All three
   "licences" were people.** Replaced by `pom_license.py`, an `ElementTree` read of
   `project/licenses` only, with **7 tests** including that exact POM shape, a profile-nested
   `<licenses>` that must not count, and dual licensing.
2. 🔴 **`curl` without `--fail` parsed PyPI's 404 body as metadata and crashed** on `codejail`,
   which is not a PyPI package. The row now reads `NOT_ON_PYPI`, which is a measurement.

## Channel state — recorded, because it bounds this result

| channel | state |
|---|---|
| 🟢 `pypi.org/pypi/<pkg>/json` + file downloads | **200**; sha256 published and verified for every distribution |
| 🟢 `repo1.maven.org` | **200**, with `.sha1` beside each artefact |
| 🔴 `search.maven.org/solrsearch`, `central.sonatype.com/api` | **403** through this proxy — **there is no Maven search** |
| 🔴 `repo1.maven.org` rate limit | **429** *"Your ip has exceeded rate limits"* on a shared egress IP; the probe sleeps 4 s between requests and retries once |
| 🔴 `pypi.org/search/?q=…` | **200** but a 3 038-byte page with **no results** — the HTML search is not usable as a channel |

🔵 **The absence of a Maven search is why the Maven n is 5 and not 21.** Coordinates had to be
*named*, and every one named here is tied to a repository this KB already cites — which also
means the Maven sample is **not random** and is biased toward LTI and Sakai.

## Files

| file | role |
|---|---|
| `scan_pypi_payload.sh` | PyPI: registry metadata, both distributions, sha256 verify, path enumeration |
| `scan_maven_payload.sh` | Maven: `maven-metadata.xml` → release version → POM + jar + `.sha1`, with backoff |
| `pom_license.py` | the POM read, as XML. `NONE_DECLARED` when there is no grant |
| `test_pom_license.py` | **7 tests**; fixtures are the real POM shapes, including the regression. `python3 -I test_pom_license.py` |
| `result-pypi.2026-10-12-p139.tsv` | 22 rows: 11 packages × wheel + sdist, plus the absent one |
| `result-maven.2026-10-12-p139.tsv` | 6 rows, as published above |

## 🔴 What this probe does NOT establish

- 🔴 **n = 5 on Maven.** Two of them are the same Sakai kernel. A 40% rate on five named,
  non-randomly chosen artefacts is a **signal, not a census**, and it must not be quoted to a
  client as "40% of Maven".
- 🔴 **Only the main jar was read.** `-sources` and `-javadoc` classifiers, and `war`/`pom`
  packaging, were not probed. A licence could be in a sibling artefact.
- 🔴 **No parent-POM resolution.** Maven inherits `<licenses>` from a parent, and
  `pom_license.py` reads only the artefact's own POM by design. 🟡 **So `NONE_DECLARED` may
  mean "declared in a parent I did not fetch"** — which would move `net.oauth.core:oauth` and
  `sakai-kernel-impl` out of the "no signal" class and make the *declaring* denominator larger.
  The direction of that error is known and is against this pass's own finding.
- 🔴 **No region measured for any artefact.** `edu.ksu.ome.lti` is Kansas State (**North
  America**) and `uk.ac.ox.ctl` is Oxford (**EMEA**) by their group ids alone; neither is booked
  as region evidence. The LATAM-ownership gap is at **nine consecutive passes**.
- 🔴 **`openedx-learning`'s emptiness was not reported upstream**, and this pass did not check
  whether an issue already exists.
