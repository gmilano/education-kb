# `p795` evidence — column definitions

Both TSVs are **headerless on purpose**: a header row written into a data file
has been compiled into a KB entity more than once in this project's history.
The columns are defined here instead.

## `maintenance-sweep.2026-11-12-p795.tsv` — `167` rows
`gh api search/repositories`, batched `10` × `repo:` per call.

1. `full_name` — owner/repo, **owner casing normalised by GitHub**
2. `stargazers_count` — exact
3. `archived` — `true` / `false` (the `LIVE-ARCHIVED` discriminator, `T901`)
4. `pushed_at` — `YYYY-MM-DD` (the staleness discriminator, `p795`)
5. `license.spdx_id` — GitHub's own verdict, `NONE` where absent
6. `fork` — `true` / `false`

`6` of `173` corpus addresses are absent from this file: they are missing from
GitHub's search index, not from GitHub (`T903`). All `6` are LIVE on the git channel.

## `rider-gate.2026-11-12-p795.tsv` — `155` graded licence files
Blobless bare clone + `git cat-file`. One row **per licence file**, so a
repository with four of them has four rows (`T912`).

1. `full_name`
2. `path` — the root licence file, or `NO_ROOT_LICENCE`
3. `family` — graded from the **first non-blank line of the bytes**, never a body
   substring (`T910`); `UNRECOGNISED` is a real verdict and the strongest rider signal
4. `bytes` — `git cat-file -s`, the primary anchor
5. `clauses` — count of numbered clauses (`N.` / `(N)` / `N)` + capital)
6. `restrictions` — `NC` / `ND` / `SA` / `BRANDING` / `FIELD-OF-USE`, or `none`.
   🔴 **Unscoped by family in this file: the `27` `NC` hits on GPL/AGPL rows are
   FALSE POSITIVES from those licences' own permissive text (`T911`).** Scope by
   family before using column 6.
7. `title` — first `70` chars of the body, for eyeballing

`sha` values are **git blob shas** (`git rev-parse HEAD:<path>`), labelled as such
per `T905`; they are recorded in the prose rows, not in this file.
