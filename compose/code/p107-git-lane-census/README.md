# `p107-git-lane-census` — release-ladder census via the anonymous git lane

**Pass 107, 2026-10-10.**

## Why this exists

`api.github.com` repo endpoints have returned `403` since pass 93, so every ★ column in this
KB reads `—`. Pass 107 triaged that 403 and found it is **three different failures**, and that
the one that matters is permanent:

| probe | http | bytes | class |
|---|---|---|---|
| `/rate_limit` | 200 | 1 922 | served — reports **limit 15 000, used 0** |
| `/repos/gmilano/education-kb` | 200 | 6 054 | served — **attached** repo, full JSON (positive control) |
| `/repos/moodle/moodle` | 403 | **378** | repo not attached to this session |
| `/search/repositories?q=…` | 403 | **249** | **path class unavailable — no remedy** |
| `/users/…`, `/licenses/…` | 403 | **249** | path class unavailable |

So it is an **authorization boundary**, not an outage and not a rate limit (`P107-A`). Waiting
never clears it. `/search/*` has no remedy at all, so API-side repository discovery is
permanently unavailable from this environment.

**But the metadata was reachable all along.** `git ls-remote` needs no API, no credential and no
clone, and the anonymous git lane serves every public repository.

## What it does

`census.sh` runs `git ls-remote --tags --heads` over `addresses.txt` and emits TSV:

```
slug  rc  heads  tags_raw  tags_uniq  head_sha40
```

- `rc != 0` means **UNREAD**, never "zero tags" (`P1040`).
- `head_sha40` is the **full 40 characters** — never abbreviate (`Gap 380`/`P987`: the 7-character
  form 404s inconsistently and reads exactly like *no licence payload*).

### The load-bearing parsing rule (`P107-C`)

`git ls-remote --tags` emits an **annotated** tag twice — `refs/tags/X` and `refs/tags/X^{}`.
A census counting `refs/tags/` lines double-counts every annotated tag. Shelf-wide:

```
raw=112 457   unique=71 079   overstatement=+41 378  (+58%)
```

The ratio is **not constant** (`canvas-lms` 68 051→34 029 ≈2×; `edx-platform` 6 347→5 896 ≈1.08×),
so no divisor corrects it — the `^{}` lines must be filtered. `tags_raw` is kept so the inflation
stays auditable.

## Result, pass 107

**299 of 299 addresses read, `rc=0` on every one — zero unread**, in 2 m 17 s. The first complete
denominator this shelf has had.

```
0 tags  — UNRELEASED   114   38.1%        25–99  — mature       40   13.4%
1–4     — nascent       37   12.4%        100+   — industrial   63   21.1%
5–24    — shipping      45   15.1%
```

### Validated before it was trusted

Three figures this KB had published from unrelated channels were reproduced **exactly**:
`academico-sis/academico` **0** tags (pass 96 derived this from an npm `"private": true` manifest),
`pupilfirst/pupilfirst` **57**, `UniTime/unitime` **101**.

## Run it

```sh
./test_p107.sh                      # offline, real captured fixtures — 20 passed / 0 failed
./census.sh [addresses.txt] > result.$(date +%F).tsv
```

`test_p107.sh` needs **no network**: `fixtures/*.refs` are real `git ls-remote` payloads captured
this pass.

## Files

| file | what |
|---|---|
| `parse_refs.sh` | parses one ls-remote payload into a census row; owns the `^{}` filter |
| `census.sh` | drives `parse_refs.sh` over an address list |
| `test_p107.sh` | 20 offline assertions, incl. the 2× inflation and the 0-tags-is-not-empty case |
| `addresses.txt` | the 299 shelf addresses, extracted from this KB's six shelf pages |
| `result.2026-10-10.tsv` | pass-107 output |
| `fixtures/*.refs` | real captured payloads: `unitime` (annotated), `academico` (0 tags), `bncc-dados` (all annotated) |

## Known limits

- **No commit dates.** `ls-remote` returns refs, not objects, so "last activity" is not available
  from this instrument. Tag *names* sometimes carry a date (`pupilfirst` `v2024.2.1efffc4`), which
  is how the `ABANDONED-LADDER` tier was detected — but that is a convention, not a guarantee.
- **No per-directory licences.** This instrument reads refs only. `Gap 370`/`P969` and `P107-F`
  (the `PrairieLearn` EE bar) need file payloads; a `--depth 1` clone would give the whole tree and
  is the obvious next step.
- **Address case.** Build any address list with `tr A-Z a-z` before `sort -u`: GitHub owner/repo is
  case-insensitive and this corpus holds **69 collisions / 72 phantom rows** (`P107-E`, `Gap 401`).
