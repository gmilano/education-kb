# `p725-readme-payload-sweep` — README licence **assertion** vs LICENSE **payload**

Closes the measurement half of **`Gap 269`** (declared pass 56): *"no systematic
README-vs-payload sweep exists across the shelved repos."*

## What it does

For every `https://github.com/owner/repo` on this KB's eight shelves, it reads
**first-hand**:

1. the README (`HEAD/README.md`, then `readme.md`), and extracts any licence
   **assertion** (badge form, `licensed under …`, `License: …`, CC deed URL);
2. the licence **payload**, trying 19 filenames, and classifies its family from
   the **title window**.

It then compares the two and emits one of seven verdicts per repo.

## Oracles

`raw.githubusercontent.com` only, plus `git ls-remote` for existence. `github.com`
and `api.github.com` are **`403` in this environment** (`P713`), so no star counts,
no API metadata, no sidebar licence field. Every transient `000` is retried; per
`P713` any success counts as success.

## Two defects this instrument had, and why they matter beyond it

**`P726` — the family discriminator must be the title window, not the body.**
GPL-3.0 names *"GNU Affero General Public License"* **three times in section 13**
(lines 552/556/559 of the canonical text). An AGPL-first match over the whole body
therefore reads **every GPL-3.0 payload as AGPL**. Caught by a control whose answer
this KB already held (`Dmoayad/essay-grader-llm` = GPL-3.0, `P715`).

**`P727` — `COPYING.txt` is the GNU convention, and omitting it biases the blind
spot into the copyleft family.** The first run reported `moodle/moodle`,
`nvaccess/nvda` and `languagetool-org/languagetool` as **ungranted**. All three ship
a grant as `COPYING.txt` / `copying.txt` (35 147 B, 53 408 B, 26 432 B). The
false-negative direction is the expensive one (`P701`): it tells a team a copyleft
repo has *no* grant, which reads as *unencumbered*.

## Byte convention

**Stored**, per `P704` — measured with curl's `%{size_download}`, never from a
shell command substitution, which strips the trailing newline and produces the
off-by-one `P724` diagnosed. This instrument independently reproduced that
off-by-one and then eliminated it: it confirms pass 56's corrected stored figures
(OATutor **1 105**, rubric **1 077**, AITutorAgent **1 072**,
open-learning-ai-tutor **1 069**, OpenTutor **1 068**, essay-grader-llm **35 149**).

## Guards

Refuses no-argument and empty-input invocation with a message naming the correct
call and **exit 2** (`P541` / `Gap 253` discipline).

## Invocation

```
./readme_vs_payload.sh <file-of-github-urls> [<same-file>] [jobs]
```

Writes TSV to stdout: `slug · readme_assert · payload_family · payload_file · bytes · verdict`.

## Results, 2026-10-08 (pass 57)

`result.2026-10-08.tsv` — all **1 020** unique slugs on the eight shelves.
`recheck-corrected-filenames.2026-10-08.tsv` — the 101 `UNGRANTED`/`NO_README`
rows re-run with the corrected filename list.
`adjudication.2026-10-08.tsv` — **every one of the 13 `MISGRANTED` rows read by
hand**, with the verdict and the reason.

| Verdict | n | % |
|---|---|---|
| `NO_ASSERTION` — README makes no licence claim | 558 | 54,7 % |
| `AGREE` | 225 | 22,1 % |
| `UNPARSED_ASSERTION` | 126 | 12,4 % |
| `NO_README` | 67 | 6,6 % |
| 🔴 `UNGRANTED` — README claims a licence, **no payload exists** | **29** | 2,8 % |
| 🔴 `MISGRANTED` — README claims one family, payload grants another | **13** | 1,3 % |
| `DUAL_LAYER` — CC asserted, code licence granted | 2 | 0,2 % |

**The raw counts are not the finding.** Hand-adjudicated, the 13 `MISGRANTED` are
**5 confirmed misgrants, 4 real defects of another class, and 4 artefacts of this
instrument** — a **31 % false-positive rate on its own most dangerous class**. The
29 `UNGRANTED` carry a measured **15 %** artefact rate (5 of the original 34).
Treat any row here as a claim to verify, never as a verdict.
