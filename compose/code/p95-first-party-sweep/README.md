# `P95` — First-party metadata sweep (`p843`, 2026-11-16)

Two stages. Stage 1 asks GitHub what it holds about every repository on the
shelf; stage 2 byte-reads the grant for everything stage 1 could not classify.

```bash
./sweep.sh repos.txt out.tsv          # stage 1 — licence, stars, push, liveness
./grant-bytes.sh owner/repo [...]     # stage 2 — byte-read the grant
```

## Why it exists

Up to `p842` this base recorded star counts as 🟡 *third-party, unverified* and
said so explicitly, because the two obvious channels are both closed here:

| Channel | Result in this environment | Measured |
|---|---|---|
| `gh api repos/{owner}/{repo}` | `403` — the session credential is scoped to attached repositories | 2026-11-16 |
| `https://github.com/<owner>/<repo>` (HTML) | `403` through the proxy (`T124`) | 2026-11-16 |
| `gh api search/repositories` + `repo:` qualifier | 🟢 **`200`, full metadata, any public repo** | 2026-11-16 |
| `raw.githubusercontent.com/<repo>/<branch>/LICENSE` | 🟢 `200`/`404`, a real answer | 2026-11-16 |

The search endpoint is not repository-scoped, takes ten `repo:` qualifiers per
query as an OR, and returns `license.spdx_id`, `stargazers_count`, `pushed_at`,
`archived` and `fork`. That is the whole sweep.

## Reading the output

- **A repo missing from `out.tsv` did not resolve.** Deleted, renamed or made
  private. Stage 1 prints these; confirm with
  `git ls-remote --symref https://github.com/<repo> HEAD`, which asks for
  credentials when the repository is not there.
- **`NOASSERTION` is not "no licence".** It means GitHub's detector could not
  match the text to a template. On this shelf it has meant an MIT grant with an
  extra clause, an MIT grant plus a vendored ISC grant, and — the class named at
  `p843` — the Apache-2.0 *appendix boilerplate* standing in for the 11,357-byte
  text. **Run stage 2 before touching the row.**
- **`NONE` is stronger evidence**: GitHub found no licence file at all. Stage 2
  still confirms it, because GitHub only looks at the repository root.

## Fixture

`fixture-repos.txt` holds six repositories that between them exercise every
path, and `fixture-expected.tsv` is stage 1's output over them as measured
`2026-11-16`:

- `AgentTeam-TaichuAI/ScienceClaw` — `NONE`, 681★, the unlicensed half of a
  name collision this base already carries.
- `eth-lre/PedagogicalRL` — `NONE`, 55★, EMNLP 2025 Oral, no grant payload.
- `kingdonkatsu/ntulearn-mcp` — `NOASSERTION` that stage 2 resolves to a clean
  MIT grant (`1,055 B`).
- `wwrwbs/AI_AWE`, `zavora-ai/mcp-education` — `NOASSERTION` that stage 2
  resolves to Apache-2.0 **boilerplate-only** (`1,865 B`, `738 B`).
- `Nordup/askaboard` — does not resolve; it is also the batch that proves the
  `422` fallback, because one dead repository fails the whole ten-repo query
  and the script then re-runs those ten one at a time.

Stage 1 exits `0` when every input resolved and `1` otherwise; stage 2 exits `1`
when any repository has no grant payload. Both drop into CI unchanged.
