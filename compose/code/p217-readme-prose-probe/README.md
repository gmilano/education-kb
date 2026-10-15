# p217 — `ACTION QN`: the README prose channel over the 67 ungranted rows

## What this measures

The `67` rows this KB carries as ungranted, probed through the one channel p215 and p216 left
unread: **the repository's own `README`, read as text**.

p215 read licence files and manifests through `git ls-tree`. p216 established that `0` of `69`
serve a plain root `LICENSE`, closing the filename-guess axis. `README` prose was what remained.

## Method

```sh
for form in README.md readme.md README.MD README.rst README.txt README; do
  curl -sSL --max-time 25 "https://raw.githubusercontent.com/$slug/HEAD/$form"   # first 200 wins
done
```

then grep the body for a licence-shaped statement and **classify from the section BODY, never the
heading**. `9` of the `19` hits matched only `## License`; the grant sat `1`–`3` lines below, and
in two of those cases the body was a *refusal*.

Dangling pointers were then confirmed through p215's channel — `git clone --filter=blob:none
--no-checkout --depth 1` + `git ls-tree -r HEAD --name-only` — a complete file inventory with zero
blob transfer, grepped for `licen[sc]e|copying|notice`.

## Result

`64` of `67` served a `README`; `3` do not resolve at all. **`19` carried a licence-shaped
statement**, against `ACTION QN`'s limb-`1` threshold of `3`. They fall into eight classes, and
the classes are the finding — not the count:

| class | rows |
|---|---|
| `PROSE-CLAIM-DANGLING` — names MIT, points at a `LICENSE` that is not in the tree | `4` |
| `PROSE-CLAIM-BARE` | `8` |
| `PROSE-CLAIM-QUALIFIED` — *"MIT — demo use only"* | `1` |
| `PROSE-CLAIM-SCOPED` — MIT on curation, not on linked content | `1` |
| `PROSE-CLAIM-CONFLICT` — `CC BY 4.0` badge vs `CC BY-SA 4.0` prose, one file | `1` |
| `PROSE-THIRD-PARTY` — dependencies only, no own grant | `1` |
| **`GRANT-REFUSED`** — affirmatively closed, **not an absence** | `2` |
| `DOMAIN-NOUN` — false positive (`spdx/license-list-data`) | `1` |

**`4` of `4`** tested `LICENSE` pointers are dangling: `SpeakGenie-AI-Tutor` (`180` files),
`LearnFlow-AI` (`179`), `vidyamind` (`76`), `ScholarMate` (`36`) — `0` licence-shaped paths in any
of them.

## What it changes

`67` is confirmed as a count of rows with **no readable grant**. It is **not** a count of
unknowns, which is how this KB has been reading it. The genuine unknowns are **`47`**
(`45` no-prose + `1` domain-noun + `1` third-party-only).

**Nothing here is promoted to a usable licence.** A prose claim is a lead with a named channel;
`mcp-powerschool` is the archived precedent. `compose/patterns.md` `P217-A` encodes the rule as
`grant_state()`: the `licence` field stays `None` unless a blob was read.

## Files

- `slugs.txt` — the `67`, derived set-verified from
  `evidence/ungranted-after-18-forms.2026-10-15-p211.tsv` minus
  `evidence/lstree-grant-recovery.2026-10-15-p215.tsv`, minus the `hesham0-0nasser` owner-case
  pair and the `os4ed/openSIS-Classic` case-variant p215 recovered.
- `raw-results.tsv` — the unclassified probe output, one row per slug.
- Classified output: `evidence/readme-prose-grant-probe.2026-10-15-p217.tsv`.
