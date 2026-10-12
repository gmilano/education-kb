---
industry: education
region: Global
updated: 2026-10-12
---

# `p141-pom-chain-sweep` — `ACTION DC`: 🔴 REFUTED on three rows. `T26` is Maven's shape, not two artefacts'

## The action, as p140 wrote it

> Apply the `ACTION CR` parent-chain walk to **every** Maven coordinate this KB cites, not just
> the five on the LTI shelf. 🔴 *Refuted if no further row changes verdict — which would make
> `T26` a property of these two artefacts rather than of Maven's inheritance model.*

🔵 **The walker is p140's `pom_chain.py`, re-used unchanged and on purpose.** A sweep that
reimplements its instrument cannot distinguish a changed verdict from a changed method. Only
the population is new.

## Verdict: 🔴 **DISCHARGED and REFUTED. Three further rows change verdict.**

[`result.2026-10-12-p141.tsv`](result.2026-10-12-p141.tsv),
[`chain.2026-10-12-p141.txt`](chain.2026-10-12-p141.txt):

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util:1.2.0` | Apache-2.0 | — | — | 1 |
| 🆕 🔴 **`org.verapdf:verapdf-library:1.30.3`** | 🔴 **NONE** | `org.verapdf:verapdf-parent:1.30.1` | 🔴 **GPL-3.0 *or* MPL-2.0** | **3** |
| 🆕 🔴 `org.jasig.ssp:ssp:2.8.0` | 🔴 **NONE** | `org.jasig.parent:jasig-parent:39` | Apache-2.0 | **3** |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |
| 🆕 🟢 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` | Apache-2.0 | — | — | 1 |

## 🔴 The row that matters: veraPDF is dual GPL-3.0 / MPL-2.0 and says nothing in its own POM

`org.verapdf:verapdf-library` is the PDF/UA accessibility validator — in an education
engagement, the component you reach for to check whether course material meets an
accessibility obligation. 🔴 **Its own POM carries no `<licenses>` block. The grant is two
levels up, and it is a dual GPL-3.0 / MPL-2.0 offer** — simultaneously the strongest reciprocal
licence this KB has found on a Maven row and, via MPL-2.0, the escape hatch from it.

🔴 **A scanner that reads the named coordinate's POM reports "no licence" and a reviewer
concludes "permissive by default" — the exact error p140 corrected on `net.oauth.core:oauth`,
on a component whose licence actually constrains redistribution.** 🟢 Choosing MPL-2.0 is
available and is the obvious choice for a studio; you cannot choose it without knowing it is
offered.

🔵 **And there is nothing to inspect for a second opinion.** `verapdf-library` is
`<packaging>pom` with two modules (`core`, `xmp-core`) — 🔴 **`verapdf-library-1.30.3.jar` is
404 on Central**, because no jar is published under that name. Consumers resolve
`org.verapdf:core`. So the coordinate a dependency declaration names has **no own grant and no
payload**: the licence lives in a parent and the bytes live in siblings.
`org.jasig.ssp:ssp:2.8.0` is the same class — `<packaging>war`, no jar.

## 🔴 Cumulatively, inheritance is now the MAJORITY shape on this shelf

Nine coordinates walked across p140 and p141:

| verdict | rows |
|---|---|
| 🔴 `INHERITS_FROM_PARENT` | 🔴 **5** — `net.oauth.core:oauth`, `sakai-kernel-impl`, `verapdf-library`, `jasig.ssp:ssp`, `sakaiproject:kernel` |
| 🟢 `DECLARES_OWN` | 4 — `sakai-kernel-api`, `lti-launch`, `basiclti-util`, `spring-security-lti13` |

🔵 **5 of 9 (56%) do not declare their own licence.** `T26` is not about two artefacts; it is
how Maven works, and any licence audit of a Java education stack that reads one POM per
coordinate is wrong more often than right.

🔵 **`org.sonatype.oss:oss-parent:7` is the shared grandparent of both the veraPDF and JASIG
chains and declares nothing** — so the walk has to continue *past* a silent ancestor rather
than stop at it. p140's walker already does; a hand audit would not.

## 🟢 And the cleanest Maven row on the shelf is EMEA, by its own groupId

🆕 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` — **Apache-2.0, declared in its own POM at depth
1**. 🔵 **The `groupId` itself is the origin evidence**: `uk.ac.ox` is the University of
Oxford's reverse-DNS namespace, and `.ac.uk` maps to 🟢 **EMEA** with no inference. A Maven
groupId is a stronger origin signal than an npm author field — it is a namespace the
organisation had to control to publish — and this is the first row this KB has placed that way.

🔴 **It still ships no licence text**: `META-INF` carries no `LICENSE` or `NOTICE` across the
jar's 72 entries. So `T21`'s Maven figure firms up on a sixth row: **5 of 6 declare and ship
nothing — 83%**, against npm's 33% and PyPI's 0%.

🟡 **A KB citation confirmed as correct:** `uk.ac.ox.ctl:spring-lti13` is **404 on Central**,
and `repos/foundations.md` already records it as such. The real artefact is
`spring-security-lti13`; the shorter name has never existed. 🟢 Recorded as a confirmation, not
republished as a finding.

## 🔴 A method note on Maven Central through this proxy

Central answered **429** on two of the six metadata fetches this pass and on the
`basiclti-util` jar, clearing after 8–24 s of backoff. 🔵 **A `429` is not a `404`, and an
earlier draft of this sweep recorded `uk.ac.ox.ctl:spring-security-lti13` as "not on Central"
off a single un-retried `429`** — which would have deleted the cleanest row in the table. Every
fetch retries with backoff and a failure is reported as a failure.

## Reproduce

```sh
./sweep.sh                                              # the five rows above
python3 -I ../p140-pom-parent-chain/pom_chain.py GROUP:ARTIFACT:VERSION
```
