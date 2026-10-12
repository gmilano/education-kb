---
industry: education
region: Global
updated: 2026-10-12
---

# `p140-pom-parent-chain` — `ACTION CR`: both "no signal" rows DO declare a licence, two and three levels up

**Executes p139's pre-registered `ACTION CR`**, written as:

> Resolve **parent-POM inheritance** for the two Maven rows reading `NONE_DECLARED`.
> 🔴 *Refuted if either inherits a `<licenses>` block from its parent — which would move it
> out of the "no signal" class and RAISE the declared-but-absent denominator, against this
> pass's own finding.*

## Verdict: **DISCHARGED and 🔴 REFUTED ON BOTH ROWS — and the refutation makes p139's finding WORSE**

| coordinate | own POM | inherits from | inherited licence | depth | verdict |
|---|---|---|---|---|---|
| 🔴 `net.oauth.core:oauth` 20100527 | **NONE** | 🆕 `net.oauth:oauth-parent:20090531` | 🆕 **Apache-2.0** | 3 | 🔴 `INHERITS_FROM_PARENT` |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | **NONE** | 🆕 `org.sakaiproject:oss-parent:1` | 🆕 **ECL-2.0** | 4 | 🔴 `INHERITS_FROM_PARENT` |
| 🟢 `org.sakaiproject.kernel:sakai-kernel-api` 25.2 *(control)* | ECL-2.0 | — | — | 2 | 🟢 `DECLARES_OWN` |
| 🟢 `edu.ksu.ome.lti:lti-launch` 1.4.7 *(control)* | LGPL-3.0 | — | — | 1 | 🟢 `DECLARES_OWN` |

Both controls return p139's verdict unchanged, so a changed verdict on the two targets is a
property of the rows, not of the method. Full walk:
[`chain.2026-10-12-p140.txt`](chain.2026-10-12-p140.txt).

## 🔴 Two corrections p139's prose now needs

`repos/foundations.md` and `verticals/solutions.md` both state, of `net.oauth.core:oauth`:

> *"carries no licence signal at all … No grant and no file is not 'permissive by default' —
> it is **unlicensed**, and sixteen years of use does not change that."*

🔴 **That is wrong.** The artefact inherits **Apache-2.0** from `net.oauth:oauth-parent`, two
levels up — 🔵 **and under a DIFFERENT `groupId`** (`net.oauth`, not `net.oauth.core`), which
is why nobody found it. There is a grant. It is just nowhere a reader would look.

`verticals/solutions.md` also states that the two Sakai kernel artefacts are *"two artefacts
of one kernel, same release line, **opposite licence posture**"*. 🔴 **Also wrong.** Both are
**ECL-2.0**; `api` declares it directly and `impl` inherits it from `org.sakaiproject:oss-parent:1`
three levels up. 🔵 **The posture is identical. Only the declaration DEPTH differs** — and
depth is exactly what an off-the-shelf scanner reading one POM does not traverse.

## 🔴 The denominator rises from 40–67% to 80%

p139 scored Maven as *"2 of the 3 that declare"*. With inheritance resolved, **5 of 5 declare**:

| coordinate | declares | ships licence text in the jar |
|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` 1.2.0 | Apache-2.0 (own) | 🟢 `META-INF/LICENSE` + `NOTICE` |
| 🔴 `edu.ksu.ome.lti:lti-launch` 1.4.7 | LGPL-3.0 (own) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 (own) | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` 20100527 | 🆕 Apache-2.0 (**inherited**) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🆕 ECL-2.0 (**inherited**) | 🔴 **NONE** |

🔴 **4 of 5 (80%)** declare a licence and ship no text for it, against p139's 40–67% and npm's
33%. 🔵 **The falsifier fired and the trend it threatened got stronger, not weaker** — which is
the only outcome that makes a pre-registered falsifier worth writing.

## Method

Walk the `<parent>` chain upward from the artefact's own POM, fetching each level from Maven
Central by coordinate. `<licenses>` is read with an **XML parser**, and only a block that is a
**direct child of `<project>`** counts — a `<licenses>` inside `<profiles>` or
`<pluginManagement>` is not what Maven inherits, and a substring test cannot tell the
difference. The first level carrying one is what the artefact effectively declares.

Central answers `429` under load through this environment's proxy; every fetch retries with
backoff, and a failure is reported as a failure rather than as an absence. One such report
stands: `org.sakaiproject:kernel:25.2` is **404 on Central**, so the `api` row's chain is
incomplete above level 1. It does not matter for that row — it declares its own — and it is
recorded rather than smoothed over.

## Reproduce

```sh
python3 -I pom_chain.py                                   # the four rows above
python3 -I pom_chain.py net.oauth.core:oauth:20100527     # or any coordinate
```
