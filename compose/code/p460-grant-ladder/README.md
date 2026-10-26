# `p460-grant-ladder` — `P460-A`, the case-insensitive grant ladder

Resolves a repository's default ref with `git ls-remote --symref`, then walks grant-file paths
**case-insensitively on both stem and extension**, gating every read on `%{http_code}`.

Emits exactly one of four verdicts and never conflates the last two:
`GRANTED` · `POINTER_OR_STUB` · `REPO_LIVE_NO_GRANT` · `ADDRESS_DEAD`.

## Why it exists

`openedx/XBlock` serves **no** grant at ten lowercase root paths and serves **Apache-2.0** at
`LICENSE.TXT`. A ladder that stops at the lowercase forms publishes a **false ungranted** for a
permissively licensed dependency — `Gap 455-A`'s expensive direction, reached by filename **case**
rather than by ref.

## Controls (run, not asserted)

| address | verdict |
|---|---|
| `openedx/XBlock` | `GRANTED LICENSE.TXT 11358B cfc7749b96f6` |
| `HKUDS/DeepTutor` | `GRANTED LICENSE 11408B cd2f54e1e506` — reproduces `p458` |
| `CAHLR/OATutor` | `GRANTED LICENSE 1105B 5baaaf977a28` |
| `Selleo/mentingo` | `GRANTED LICENSE 1062B ceb97717de1f` |
| `mwasifanwar/eduadapt-ai` | `REPO_LIVE_NO_GRANT (ref=main)` |
| `nope-p460-fabricated/nope-p460`, `zzz-not-real-p460/zzz` | `ADDRESS_DEAD (no ref)` |

## Retraction carried with the code

The first draft built its extension list as a string expanded with `eval echo`, including `''` for
the bare stem. An unquoted empty word is **dropped by word-splitting**, so the bare `LICENSE` was
never probed and the draft reported `REPO_LIVE_NO_GRANT` for `HKUDS/DeepTutor` and
`Selleo/mentingo`. The extension list is now a literal bash array with an empty first element.
Caught by running the controls, not by reading the code.

Usage: `./p460a.sh owner/repo`
