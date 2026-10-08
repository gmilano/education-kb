---
industry: education
region: Global
updated: 2026-10-08
---

# `p791-registry-id-provenance` — a code returned by a TARGET is not a fact about the HOST

**Pass 63 of 2026-10-08.** This instrument exists because of two lines in this shelf's own oracle
map, written one pass apart:

> pass 61 — `packagist` **404**
> pass 62 — `packagist` **200 × 2 — recovered from pass 61's `404`**

🔴 **Neither was a measurement of packagist.** Both probed
`packbackbooks/lti-1-3-php-library` — the **repository slug**, shaped like a package id. Nothing
publishes that id. Measured here in the same minute, on the same host:

| Probe | n = 2 | What it licenses you to say |
|---|---|---|
| `packagist.org/packages/monolog/monolog.json` | 🟢 **200 · 200** | the host answers |
| `packagist.org/packages/zzz-invented-p791/zzz-nope.json` | 🟢 **404 · 404** | the host *discriminates* |
| `packagist.org/packages/packbackbooks/lti-1-3-php-library.json` | 🔴 **404 · 404** | **that id is absent** |
| `repo.packagist.org/p2/packbackbooks/lti-1-3-php-library.json` | 🔴 **404 · 404** | and absent on the second host too |

🟢 **The host never moved.** 🔵 **`P791`: reachability is read off a CALIBRATION PAIR — one id
known to exist and one known not to. A single code from a target id is a fact about that id.**
`P787` cut reachability by host; this cut runs underneath it, because one host serves both answers.

🟢 **And pass 62's datum survives, which is the point worth keeping:** the repo's own
`composer.json` **at `master`** declares `packbackbooks/lti-1p3-tool`, that id answers **200**, and
its newest non-dev release is **`v6.4.4`, `2026-09-23T21:17:20Z`, `Apache-2.0`**, with
`repository` pointing back at `packbackbooks/lti-1-3-php-library`. 🔵 **Pass 62 was right about the
package and wrong about the host, and only the second half went into the map.**

## What runs

| File | What it does | Network |
|---|---|---|
| `slugs.input.2026-10-08.txt` | the **25** composer-layer slugs this shelf cites | — |
| `sweep_composer.sh` | the probe layer `p253` never had: `composer.json` at `{main,master}`, then packagist for the **declared** id *and* for the slug-shaped **guess** | yes |
| `verdict.py` | three verdicts per row. Imports `p253/identity.py` **unchanged** | no |
| `test_provenance.py` | **37/37 offline**, including the three seam defects below as named regressions | **no** |
| `result.2026-10-08.tsv` | the committed measurement | — |

```sh
sh sweep_composer.sh < slugs.input.2026-10-08.txt > result.2026-10-08.tsv
python3 verdict.py result.2026-10-08.tsv        # per-row verdicts + provenance census
python3 test_provenance.py                      # 37/37, no network
python3 -I test_provenance.py                   # same, isolated
```

## 🔴 Two defects in the SEAM, neither of them in either half

### 🆕 `P792` — a gate and its own probe layer can disagree about the shape of the field they share

🔴 **Measured end to end, not inferred.** `sh p253-registry-first-identity/sweep_identity.sh ltijs`
emits `pub_repo = git+https://github.com/Cvmcosta/ltijs.git`. `identity.py`'s `_norm()` lowercases
and strips a trailing slash, then compares that string to the slug `Cvmcosta/ltijs`:

```
pub_repo as emitted : 'git+https://github.com/Cvmcosta/ltijs.git'
verdict             : ('PUBLISHED-BY-OTHER',
                       'ltijs existe pero apunta a git+https://github.com/Cvmcosta/ltijs.git,
                        no a Cvmcosta/ltijs')
```

🔴 **`PUBLISHED-BY-OTHER` for a package that points at exactly its own repository** — and npm
spells `repository.url` that way for nearly everything, so the misfire is the *common* case, not
an edge. 🟢 **`p253`'s committed `result.2026-10-04.tsv` is NOT wrong:** its `pub_repo` column
holds slugs (9 slug-like, 8 `-`) and its one `PUBLISHED-BY-OTHER`
(`algorithm0r/canvas-lms-mcp` → `bruchris/canvas-lms-mcp`) is a real mismatch. 🔵 **The
normalisation was done by hand and never written into the script, so the committed table is right
and a re-run of the same two files is wrong.**

🟢 **Fixed HERE, not there:** `sweep_composer.sh` normalises `repository` to `owner/repo` before
the gate sees it, for `git+https`, plain `https` and `git@…:` spellings, and leaves a non-GitHub
URL untouched. 🔵 **The gate is not edited** — it is another pass's instrument and its logic is
correct; what was missing is a probe layer that honours its contract.

🔵 **The precedent that generalises, and it is the complement of `P713`:** *reuse the instrument*
is not enough — **reuse it END TO END**, because the defect can live in the seam. Pass 59 learned
to `grep` the instruments before announcing a property; pass 63 is the same lesson for an
**interface**.

### 🆕 `P792a` — a field whose CONTENTS do not match the shape its reader assumes

🔴 **The first run of this very script shifted two columns of `krayin/laravel-crm`,** reporting
`latest = Jitendra Singh,devansh.bawari419@webkul.com` and `latest_time = 2.2.x-dev`. 🔵 Cause:
`set -- $(python3 …)` splits on **whitespace**, and that maintainer string contains a space.
🟢 Fixed by emitting TAB and reading with `IFS=$(printf '\t')`; re-measured, the row is
`MIT`, maintainer `Jitendra Singh,devansh.bawari419@webkul.com`, `2.2.x-dev`,
`2026-10-07T05:55:14Z`. 🔵 **Same class as `P792`: a reader that assumes a shape its writer never
promised.** 🔴 **Both defects were found by RUNNING the thing, not by reading it.**

## 🆕 `P793` — `master` is a PSEUDO-REF, so "read at `master`" is not provenance

🔴 **Measured, 3 of 3, against a 404-discriminating control:** `raw.githubusercontent.com` serves
the **default branch** for the literal ref `master` even when the repository has **no `master`**.

| Repository | `ls-remote --symref` default | `main` | `master` | `HEAD` | invented |
|---|---|---|---|---|---|
| `php-xapi/client` | 🔴 `refs/heads/0.7` (`b39735b`) | 404 | 🔴 **200** | 200 | 404 |
| `tl-its-umich-edu/caliper-php-public` | 🔴 `refs/heads/public` (`e35b0ec`) | 404 | 🔴 **200** | 200 | 404 |
| `portabilis/i-educar` | 🔴 `refs/heads/2.12` (`cd1da68`) | 404 | 🔴 **200** | 200 | 404 |

🟢 **`P714` warned about this; this is the measurement, with a control.** 🔵 The cut is the same as
`P791`'s on the other axis: **a ref name is not provenance, exactly as a target's code is not a
host verdict.** 🟢 So `sweep_composer.sh` resolves the default ref with `ls-remote --symref … HEAD`
and probes **that** first, recording `default_ref`, `head_sha` and `served_at` separately.

🟢 **And it cuts both ways.** `francoisjacquet/rosariosis` showed **no manifest at all** under a
`{main,master}` probe; its real default ref **`mobile`** (`899f6da`) carries a `composer.json`
declaring `GPL-2.0-or-later`, published as `francoisjacquet/rosariosis` **`12.9.x-dev`,
2026-09-02**. 🔵 **A false provenance and a false absence from one cause.**

🟢 **Defaults that are neither `main` nor `master`: 7 of 25** — `v31.0.00` (a *tag-shaped branch*,
`GibbonEdu/core`), `mobile`, `2.2`, `0.7`, `3.x`, `2.12`, `public`.

## 🟢 Measured, 2026-10-08, over all 25

| `id_provenance` | n | What it is |
|---|---|---|
| 🔴 **`FALSE-ABSENCE-RISK`** | **8** | the declared id answers **200** and the slug-shaped guess **404s** — a probe on the guess reports the package, and (as passes 61–62 did) the host, as absent |
| `ID-EQUALS-SLUG` | 8 | declaration and guess coincide: no misread possible |
| `AGREES` | 5 | both ids give the same code (5 of 5 are `404`/`404`: genuinely unpublished) |
| `NO-DECLARATION` | 4 | no `composer.json` at the default ref — the guess is the only id there is |

| `p253.package_identity` (imported) | n |
|---|---|
| `PUBLISHED-AT-ROOT` | 16 |
| `DECLARED-NOT-PUBLISHED` | 5 |
| `UNDETERMINED` | 4 |

| Manifest-layer licence | n |
|---|---|
| 🟢 **MIT** | 8 |
| 🟢 **Apache-2.0** | 2 |
| 🔴 GPL-3.0 | 3 |
| 🔴 GPL-2.0-only | 2 |
| 🔴 GPL-2.0-or-later | 2 |
| 🔴 GPL-3.0-or-later | 1 |
| 🔴 `proprietary` | 1 |
| no manifest | 6 |

🟢 **8 of 21 rows with a declaration would be reported ABSENT by a slug-shaped probe** — and that
is a **count over this named population**, never a rate (see below).

## 🆕 `P794` — two layers can land in opposite BANDS, not merely differ in precision

🔴 `tl-its-umich-edu/caliper-php-public` @ `refs/heads/public` (`e35b0ec`), the only reachable
Caliper Analytics implementation this shelf has found (`Gap 284`):

| Layer | Read | Verdict |
|---|---|---|
| licence **file** | `LICENSE`, 7 438 B, title line `GNU LESSER GENERAL PUBLIC LICENSE / Version 3`, 0 Affero mentions | 🔴 **LGPL-3.0** (`p419.familia()`, self-test 10/10 green) |
| **manifest** | `composer.json` → `"license": "proprietary"` | 🔴 **`proprietary`** |
| **registry** | packagist `umich-its-tl/caliper-php` 200, `repository` → this repo | 🔴 **`["proprietary"]`**, latest `1.0.1` **2016-01-27** |

🔵 **The divergences this shelf had on the board were `-or-later` suffixes and version reads. This
one is open vs not open**, and a one-layer pre-flight publishes whichever layer it reads first.
🟢 **Neither reading is permissive, so `Gap 284` is unaffected in substance** — and it is now a
*characterised* hole rather than an empty cell.

🟡 **The `-or-later` class, also measured here:** `portabilis/i-educar`'s licence file at `2.12` is
bare **GPL-2.0** while its manifest says **`GPL-2.0-or-later`**; `moodle/moodle` shows the same
split in the same direction. 🔵 **A licence file structurally cannot express `-or-later`** — the
bare GNU text is byte-identical either way, and the suffix lives in the manifest or the headers
(`P620`).

## The gate, in one paragraph

`host_verdict(good, bad)` takes **no target id at all** — a caller that wants to write a host line
has to produce a calibration pair, which is exactly what passes 61 and 62 never produced. A
single-code call raises `TypeError`, and the suite asserts that. `id_provenance(row)` compares the
**declared** id's code with the **guessed** id's code and names the disagreement:
`FALSE-ABSENCE-RISK` when the declaration answers and the guess does not — `P788` already called
that the worse direction — and `FALSE-PRESENCE-RISK` for the reverse. Everything about *package
existence* is delegated to `p253`'s `package_identity()`, imported and not copied.

## 🔴 What this instrument does NOT establish

🔴 **No rate is published.** 25 slugs chosen because this shelf already cites them is not a
sampling frame for "how often a PHP package id differs from its repo slug", and `P744`'s denial
still forbids the sweep that would build one. 🔴 **The population is one ecosystem.** npm, PyPI,
Maven and NuGet each spell `repository` their own way; only composer was measured here.
🔴 **A `404` on a declared id is an absence of THAT id, never of the project** — the tree may
publish under a name no manifest at depth 0 carries, which is precisely `p253`'s subdirectory
finding and is not probed here.
