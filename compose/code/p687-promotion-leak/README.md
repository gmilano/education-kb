# p687 — promotion leak audit

`leak.py` extracts every `github.com/<owner>/<repo>` slug from `agents/trending.md` and
`repos/trending.md` and differences it against all shelf pages. Run from the repository root:

    python3 -I compose/code/p687-promotion-leak/leak.py /tmp/absent.txt

Result on 2026-11-07 at p687:

| quantity | value |
|---|--:|
| distinct slugs in the two trending files | 4,162 |
| distinct slugs on any shelf page | 782 |
| mentioned in trending, absent from every shelf | 3,472 |

Most of the 3,472 are legitimately out of scope. The audit's value is the ranking: ordering the
absent set by **how many times this base has written the slug down** surfaced
`virgiliojr94/book-to-skill` (37,173 stars, MIT, 26 mentions, 0 rows),
`classroomio/classroomio` (28 mentions), `PrairieLearn/PrairieLearn` (15) and
`judge0/judge0` — which p354 declared filed and never filed.

`absent-top120.2026-11-07-p687.txt` is the head of that ranking as it stood at p687.

## verify.sh

`verify.sh OUT slug...` resolves each slug's **real default ref** with
`git ls-remote --symref` and then reads the grant payload at that ref, trying `LICENSE`,
`LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT` in order. Emits
slug / ref / file / bytes / sha256(12) / title line. Output for this pass is
`grants.2026-11-07-p687.tsv`.

> **Two defects this script had at p687, both recorded in the published pages rather than
> silently patched here.**
>
> 1. It uses `curl -sSL` **without `--fail`**, so a missing file returns GitHub's 14-byte
>    `404: Not Found` body with exit status 0. That is how `SafeExamBrowser/seb-server` was
>    measured as having a "14 B README". See `intel/trends.md` **T92**. Any reuse should add
>    `--fail` and treat payloads under ~64 B as probe failures.
> 2. Resolving the ref first is not ceremony: `virgiliojr94/book-to-skill` defaults to
>    `master`, and every licence filename 404s at `main`. A `/main/LICENSE` probe reads a
>    37,173-star MIT repository as ungranted.
