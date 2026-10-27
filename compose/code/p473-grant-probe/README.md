# `p473` — grant probe and shelf checks

Run outside the KB clone, in the session's own scratchpad, because `make hooks` and the repo's own
gate scripts are refused on this harness (`Code from External`, `Gap 446-A`). Nothing here is
gate-attested; these are the hand-run mitigations and they are **not** a substitute for the gate.

| file | what it does |
|---|---|
| `probe-fixed-ref.sh` | reads a licence payload from `raw.githubusercontent.com` for an `addr<TAB>ref` list, over an 11-path probe set |
| `probe-resolve-then-read.sh` | resolves each address's default branch first-hand with `git ls-remote --symref`, then reads the payload over a **14-path** set including lowercase `license` / `license.txt` / `license.md` (`Gap 472-B`) |
| `shelf_checks.py` | the five checks: frontmatter + closed-vocabulary `region`; table separator / pipe-count / **no header row as data**; append-only containment on both trending shelves against `HEAD`; single canonical `## Opportunities by region` with exactly five region children; digest traceability of every `sha256₁₂` printed this pass |
| `prepend_section.py` | prepends a pass section after the frontmatter and sets `updated:`, asserting the prior body survives verbatim |

Contracts honoured: every payload is written to a file and **the file** is measured, never a shell
variable (`Gap 468-A`). `curl -sI https://github.com/<repo>` is **not** used for verification — it
returns `403` for live and nonexistent addresses alike on this harness (`Gap 472-A`); existence is
proved by `ls-remote` resolution plus a `raw` byte only the origin can serve.
