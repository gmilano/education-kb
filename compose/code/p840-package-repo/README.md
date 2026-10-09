---
industry: education
region: Global
updated: 2026-10-09
---

# `P840`–`P843` — package name → repository, so `P15` stage 3 stops needing a human

Artefacts and suite of the **seventy-fifth pass (2026-10-09)**, closing `Gap 329`.
🟢 **37/37 green**, offline, single file on purpose.

## What the gap was

🔴 **`P15`** (the licence-closure gate) **needs stage 3 — probe the payload of each CORE
DEPENDENCY** — and `core_deps_of` / `repo_of_pypi` were **named in `P15` and never written**.
🔴 A PyPI/npm/Packagist name is not a GitHub path, so the most expensive stage of the gate was
blocked on a human: `73-C`'s `PyMuPDF` catch (an Apache-2.0 root over an AGPL-or-commercial
core dependency) was made **by hand**.

## The seam, per `P838`

🟢 Split on the capability the environment **denies**, not on the calling convention.
Measured this pass rather than inferred:

```
pypi.org/pypi/<name>/json                  200
registry.npmjs.org/<name>                  200
repo.packagist.org/p2/<vendor>/<pkg>.json  200
eur-lex.europa.eu                          403 to CONNECT   (Gap 308, eighth refusal)
```

🔵 All three registries sit in the proxy's `noProxy` list, so **the network limb works here** —
unlike `Gap 328`'s payload probe. 🟢 **The seam is kept anyway**: every parse lives in
`lib/package_repo.sh` and is asserted offline, so this suite stays green in a session whose
egress differs. 🔴 An instrument that only works where it was written is the failure `P838`
names.

## The verdict vocabulary, and why absence has to be loud

| verdict | meaning |
|---|---|
| `owner/repo` | 🟢 resolved — the only verdict stage 3 can probe |
| `NO-REPO` | 🔴 metadata exists, declares **no source** → **`Gap 327`'s category** |
| `UNRESOLVABLE-HOST` | 🔴 declared at an **SSH-config alias** — an address only the publisher resolves |
| `NON-GITHUB` | 🟡 real source elsewhere — not probeable by this shelf's instruments |
| `NO-METADATA` | 🔴 the registry has no such package |

🔴 **Never collapse `NO-REPO` into `NO-METADATA`.** One is a package that publishes no source,
the other a name that does not exist; they license opposite next actions, and this shelf has
written both in the same voice before (`P827`, `Gap 301`). 🟢 Asserted as a test, not a rule.

## 🔴 The finding this suite exists to remember

🔴 **The suite was 32/32 green and the instrument was still wrong.** Pass 74 wrote the honest
limit on its own closure — *"the fetch branch is **unexecuted** … the first pass with network
must run it"* — and that warning landed within four commands of running this one:

🔴 `@iblai/iblai-web-mentor` declares `git@ibl_connection:iblai/iblai-web-mentor.git` under
`"license": "MIT"`. **`ibl_connection` is not a host** — it is an SSH-config alias resolvable
only on the publisher's own machine. 🔴 The parser emitted `ibl_connection:iblai/iblai-web-mentor`
**and exited 0**, so a caller would have probed a GitHub path **that was never declared**, which
is exactly what `P827` forbids.

🟢 Fixed (`UNRESOLVABLE-HOST`), with the real `git@github.com:owner/repo` form asserted
alongside so the fix cannot swallow the good case, and **five live-found cases folded back as
regressions (32 → 37)**.

🟢 **`P841`: an offline suite green on fixtures is not evidence the fetch limb is correct.**
🔵 The fixtures encode the formats the author already knew; the registries hold the ones they
did not.

## The other two protocols this folder carries

🟢 **`P842` — resolve by DISTRIBUTION name, never by import name.** PyPI `fitz` is version
`0.0.0` with `license: null` and no URLs, and `fitz` is PyMuPDF's *import* name. 🔴 **The
danger is the direction of the error:** the audit does not fail, it returns *reassurance* about
the wrong package, while the real dependency `pymupdf` is the AGPL-or-commercial core.

🟢 **`P843` — a licence declaration in metadata and a licence file in the shipped artefact are
two different measurements; name which one you took.** 🔴 `sprightly@2.0.1` is MIT in
`package.json` and ships **no `LICENSE` and no copyright notice in any of its 8 files**, so it
cannot satisfy the MIT condition that the notice travel with all copies. Mechanism:
`files: ["dist"]`.

🟢 **And the third measurement, which settles it:** the *repository* carries
`main/LICENSE` — **1 070 B, MIT, Copyright (c) 2024 Obada Khalili**. 🟢 **So the grant exists
and only the packaging loses it**: a one-line upstream PR, not a counsel question. 🔵 That read
was possible because `raw.githubusercontent.com` answers **200** in this session, against a shelf
record that said it was refused — **`P844`**.

## Running it

```sh
bash compose/code/p840-package-repo/test_package_repo.sh      # 37/37, offline
bash compose/code/lib/pkgrepo --self-test                      # same suite, via the front end
bash compose/code/lib/pkgrepo --closure npm ./package.json     # P15 stage 3, needs network
```
