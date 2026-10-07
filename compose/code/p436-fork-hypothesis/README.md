---
industry: education
region: Global
updated: 2026-10-07
---

# `p436-fork-hypothesis` — pass 25's action A: a declared-elsewhere row is not a fork until the head SHAs differ

**Executes pass 24's pre-registered action A**, which was written as:

> Wire `p184-holder-mismatch` to `fork-lineage-audit`: re-run the holder sweep over the whole
> shelf and treat every **holder ≠ account** row as a *fork hypothesis*, resolving each against
> the package registry's declared homepage.
> **Prediction:** two of two LTI picks were cold forks. Expect **more than two** further cold
> forks in the 283-row shelf, concentrated in the interoperability tier.

## What it is

Four stages, each reachable from this environment (`api.github.com` and the rendered
`github.com` page are both **403** here; `raw.githubusercontent.com`, `pypi.org`,
`registry.npmjs.org` and `git` are not):

| Stage | File | Question |
|---|---|---|
| 1 | `sweep_payload.py` | the licence payload of every slug the KB currently cites |
| 2 | `../p184-holder-mismatch/extract_holder.py` | who does the payload name as the holder? |
| 3 | `resolve_homepage.py` | which repository does the **package registry** say this package lives at? |
| 4 | `sha_discriminator.py` | do the two slugs serve the **same head ref**? |

Stage 4 is the finding. Stage 3's `UPSTREAM` class mixes four things and only one is lineage:

```
rename / transfer   github.com redirects the old path; ONE repository, two names
fork / mirror       two repositories, one derived from the other
name collision      the manifest `name` is a common word already taken on the registry
vendoring           the manifest was copied in along with the vendored code
```

`git ls-remote <a> HEAD == git ls-remote <b> HEAD` separates the first from the rest exactly,
in one call, with no API.

## Measured, 2026-10-07, reference date passed explicitly

**Denominator: 503 slugs** — every `github.com/owner/repo` cited in the six non-append-only
shelf files. `p170`'s published denominator was **200**, of which only **62** are still cited;
**441 of the 503 had never been measured by that sweep.** Pass 66 wrote the reservation
*"the sweep is redone when `slugs.input.txt` incorporates this pass's additions"* and it had
stood open since.

| Stage | Result |
|---|---|
| payload sweep | 412 `LICENSED` · 87 `UNLICENSED` · **4 `UNREACHABLE`** |
| holder, over the 412 | 185 `NOT-APPLICABLE` · 166 `HOLDER-MATCH` · **54 `HOLDER-UNRELATED`** · **7 `NO-HOLDER`** |
| registry homepage, over the 503 | 90 `SELF` · **21 `UPSTREAM`** · 68 `NO-PACKAGE` · 56 `PRIVATE-MANIFEST` · 23 `NO-REPO-URL` · 245 `NO-MANIFEST` |
| head SHA, over the 21 | **6 `SAME-REPOSITORY`** · 15 `DISTINCT-REPOSITORIES` |
| head commit date, over the 503 | **501 dated**, 2 unresolvable |

### The 4 `UNREACHABLE` are a calibration result, not four defects

`git` resolves **two of the four**, so the probe list, not the repository, is what failed:

| Slug | Payload sweep | `git ls-remote` | What it is |
|---|---|---|---|
| `planejaia/OpenMAIC-Brasil` | UNREACHABLE | **no ref** | genuinely gone — already recorded as a phantom in this KB |
| `owner/repo` | UNREACHABLE | **no ref** | prose in `agents/top.md`, never a data row |
| `AmericasNLP/americasnlp2024` | UNREACHABLE | 🟢 resolves | exists; no root `README.md` and no licence, so both probe lists miss it |
| `cqm3ron/bromcom-scraper` | UNREACHABLE | 🟢 resolves | same |

The KB's own record already says three of these are false flags. **Two independent channels now
agree with it**, which is the only reason that record can be called verified rather than asserted.

## The controls (`test_resolve.py`, 6/6, offline)

Every fixture is a real payload captured on 2026-10-07. Rule 2 of **P126**: a control set made
only of agreeing pairs never exercises the detection, so each positive is matched by the
false-positive class that would make the output unreadable:

| Control | Why it is there |
|---|---|
| `ucfopen/pylti1.3` → `dmitry-viskov/pylti1.3` | the **positive**: real lineage, resolved from the registry alone |
| `kaorii-ako/Shiori-v1` | **name collision**. `"name": "shiori", "private": true`; npm's `shiori` is *"a lightweight discord library made for NodeJS"* at `shiorijs/shiori`, **a slug that does not resolve over `git`**. Unguarded, this publishes a fork hypothesis against a deleted repository for an unrelated project |
| `langfuse/langfuse` | **multi-repo publisher**, and the control that shows **one rule closes both**: its root manifest is *also* `"private": true`, because the npm name belongs to the sibling SDK repo `langfuse/langfuse-js`. The first build of the test asserted `UPSTREAM` here and the `private` rule failed it — correctly |
| `academic-innovation/django-lti` | **`SELF`**, the negative that forbids an instrument answering `UPSTREAM` always. It also pins the `setup.cfg` probe: this repo's `pyproject.toml` has **no `[project]` table**, so a probe list of pyproject/setup.py/package.json reported `NO-MANIFEST` for a package that is on PyPI — "no channel" and "nothing published" collapsing into one string |
| `CNIT-Organization/ltitoolkit` | **`NO-PACKAGE`**: a manifest the registry 404s under that name |
| npm `shiori` fixture | **negative control**: asserts the collision is still a collision, so control 2 is not a tautology |

## Reservations

- ⚠️ **`UPSTREAM` is a reading list, exactly as `HOLDER-UNRELATED` is.** The SHA discriminator
  removes the renames; separating a vendoring from a collision still needs a human to open
  the README.
- ⚠️ **The holder channel is not a superset of the lineage signal, and that was the premise of
  the action.** Only **4 of the 21** `UPSTREAM` rows are in the 54-row holder list. The other
  17 are Apache-2.0 or GPL rows, where the holder is `NOT-APPLICABLE` *by construction* — so
  the holder channel is structurally blind to them. Running stage 3 over the **whole shelf**
  rather than over stage 2's output is what found them.
- ⚠️ **`git ls-remote` equality proves a shared head, not a shared history.** A mirror pushed
  minutes ago is indistinguishable from a redirect. Every `SAME-REPOSITORY` row here was
  additionally checked against the registry's own declared homepage.

## Run

```sh
python3 -I sweep_payload.py slugs.input.2026-10-07.txt <outdir>
python3 -I resolve_homepage.py slugs.input.2026-10-07.txt > homepage.tsv
python3 -I sha_discriminator.py homepage.tsv > sha.tsv
python3 test_resolve.py                      # 6/6, offline
```

## Files

- `sweep_payload.py` · `resolve_homepage.py` · `sha_discriminator.py`
- `test_resolve.py` + `fixtures/` — real payloads, not excerpts
- `slugs.input.2026-10-07.txt` (503) · `payloads.2026-10-07.tsv` · `holder.2026-10-07.tsv`
  · `homepage.2026-10-07.tsv` · `sha-discriminator.2026-10-07.tsv` · `recency.2026-10-07.tsv`
  — **authoritative**
