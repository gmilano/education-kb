# `p393-pypi-index-channel` — the Python DISCOVERY channel `Gap 392-C` asked for

`Gap 392-C`, opened by `p392`, is the reason `Gap 391-A` was ever published:

> There is no Python package DISCOVERY channel … `pypi.org/search` serves a JavaScript
> bot-challenge page (3,038 B). npm search has carried every registry sweep this base has
> run, so **the discovery channel's language bias became a supply claim** — the one
> asymmetry that would hide exactly the finding `p391` got wrong. A successor should look
> for a mirror, an index dump, or accept that Python supply is found through GitHub and
> papers only.

**The index dump exists, is unauthenticated, and is not challenged.** PEP 691 renders the
simple index as JSON at `https://pypi.org/simple/` under
`Accept: application/vnd.pypi.simple.v1+json`.

| measured 2026-10-22 (`p393`) | |
|---|---|
| HTTP | 🟢 **200** |
| bytes | **45,189,043** |
| projects | **920,784** |
| wall clock | **1.4 s** |
| `meta.api-version` | `1.4` |
| auth | none |

## Why this is a channel and `pypi.org/search` is not

`search` is a rendered page behind a bot challenge; the dump is a static artefact. The
dump cannot rank, score or match descriptions — and it does not need to, because the whole
920,784-name space fits in memory and a token match over it costs nothing.

## 🔴 The channel's one structural limit, stated before its yield

**The dump carries NAMES ONLY.** No summary, no classifier, no licence, no repository.
So this channel discovers by *name*, and **a name is not a capability** — which is
`Gap 392-A`'s defect arriving from the other direction. `p393`'s first sweep produced two
name collisions in fifteen candidates:

| name | matched on | what it actually is |
|---|---|---|
| `proctor-ai` | `proctor` | a structured **prompt-engineering** library |
| `xapi-python` | `xapi` | the **xStation5 broker API** — not Experience API / Tin Can |

Both are fixtures in [`test_fixtures.tsv`](test_fixtures.tsv). A discovered name is
therefore a **candidate only**; `verify` must read the per-package JSON, and a first-hand
payload read must follow that, before anything reaches a shelf.

## 🔴 And a second limit, learned by this instrument's author getting it wrong

`p393`'s first licence read of [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker)
returned **UNGRANTED**, from a closed six-name filename list
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.LESSER`, `LICENCE`). The grant
is real and sits at **`LICENSE.LGPL-3.0`** — 7,652 B, `sha256`₁₆ `e3a994d82e64`, LGPL-3.0.
**Enumerate the tree; do not guess the filename.** `git ls-files | grep -i licen` is the
check, and it is why the row is published as LGPL-3.0 rather than as a false absence.

## Token-exact, not substring

Substring matching is unusable at this scale: `lti` as a substring returns **3,608** names
(`multi`, `split`, …) against **20** by token. Names are split on `[-_.]+` and matched as
whole tokens.

## Usage

```sh
python3 -I pypi_index_channel.py fetch                      # cache the dump
python3 -I pypi_index_channel.py sweep --vocab vocab.education.txt
python3 -I pypi_index_channel.py verify django-lti now-lms  # per-package JSON
```

`verify` keeps the **three licence channels apart** — `license_expression`, the free-text
`license` field, and the `License ::` classifiers — because `Gap 392-B` is precisely a
conflict between such channels, and collapsing them would hide the class.

🔵 **Lane.** This instrument needs egress, so per this tree's convention it is **not** in
`make hooks`. It is `make pypi-index-sweep`.
