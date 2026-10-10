# grant-ladder-v3 — licence verification instrument (pass 91, 2026-10-10)

Resolves a GitHub slug to **(existence, default branch, HEAD SHA, licence read from the payload, bytes)**.

⏱️ **Measurement window: 2026-10-09 23:0x → 2026-10-10 00:00 UTC.** The pass crossed midnight, so the
SHAs below were resolved on 2026-10-09 and the pass is dated 2026-10-10. Stated because this shelf pins SHAs
and a date that straddles a boundary is exactly the kind of thing that later reads as a contradiction.

```sh
./ladder.sh moodle/moodle ls1intum/Artemis     # first-match verdict, one line per slug
./ladder.sh --all microsoft/autogen            # EVERY licence file found, and SPLIT-GRANT detection
./ladder.sh --count                            # how many filenames this instrument actually probes
./ladder.sh --names                            # which ones
```

Output is TSV: `slug \t EXISTS|ABSENT \t ref \t short-SHA \t licence \t file:bytes`.

## Why v3 exists: two measured defects in v2

### Defect 1 — v2 probed **12** filenames while the shelf published "17" (and, in five other rows, "16")

🔴 **Measured, not inferred.** `grep '^NAMES=' ladder.sh | tr ' ' '\n'` on v2 returns **12** names. Six shelf
rows asserted *"no licence payload in 17 candidate filenames"*; five more asserted *"16 names"*. Three numbers
for one instrument, and **none of them was the instrument's.**

🔴 **It was not a cosmetic error. It produced a false negative on a live row.**
[`frappe/lms`](https://github.com/frappe/lms) carries its grant at **`license.txt`** — lowercase, with the
extension — a name v2 **never tried**. v2's own saved run (`../grant-ladder-v2/pass90-results.tsv`) records
`frappe/lms → NO-LICENCE-PAYLOAD`, while pass 90's `verticals/solutions.md` published it, correctly, as
**AGPL-3.0 at `license.txt`, 33 893 B** — found by hand, outside the instrument.

🟢 **v3 probes 24 names and prints the count on demand**, so the claim can never again drift from the code.
Re-measured under v3, `frappe/lms` resolves **AGPL-3.0 · `license.txt` · 33 893 B** automatically — the same
answer the human got.

🔵 **The transferable rule: every "absent" verdict is a statement about the instrument's reach, so the reach
must be printable.** A negative whose denominator is not machine-readable is not a measurement.

### Defect 2 — the classifier did not know **ECL-2.0**, and two permissive platforms read as `unclassified`

Pass 90 recorded: *"any future version must recognise ECL by name."* This is that version. ECL-2.0 is tested
**before** Apache-2.0, because ECL is Apache-derived and an Apache test swallows it.

| slug | v2 | v3 |
|---|---|---|
| `sakaiproject/sakai` | 🔴 `OTHER/unclassified` | 🟢 **ECL-2.0** · `LICENSE` · 11 120 B |
| `opencast/opencast` | 🔴 `OTHER/unclassified` | 🟢 **ECL-2.0** · `LICENSE` · 11 340 B |

## What the two fixes did to the published numbers

Both runs are over **the same 92 slugs**, same day, same SHAs. Only the instrument changed.

| verdict | v2 (12 names) | v3 (24 names) |
|---|---|---|
| `NO-LICENCE-PAYLOAD` | 🔴 **6** | 🟢 **5** |
| `AGPL-3.0` | 11 | **12** |
| `OTHER/unclassified` | 🔴 **2** | 🟢 **0** |
| `ECL-2.0` | — (invisible) | 🟢 **2** |

🟢 **So pass 90's published "6 of 92 carry no grant — ~1 in 15" corrects to 5 of 92, ~1 in 18**, and the five
survivors are now negatives against **24** names instead of 12 — a materially stronger claim, not just a
smaller number. `pass91-results.tsv` holds all **120** slugs resolved this pass.

## A defect v3 found **in itself**, mid-pass — and the ordering rule that fixes it

🔴 **v3's first draft classified [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum)
as `Unlicense/PD`. It is CC BY-NC-SA 4.0.** The cause: a Creative Commons human-readable summary contains the
words *"public domain"* in its notices, and the draft tested for public domain **before** testing for CC.

🔵 **This error runs in the dangerous direction and the ECL error did not.** `unclassified` → a row gets
dropped → a studio loses an option. `NC-copyleft` → `public domain` → **a studio ships non-commercial content
in a paid client deliverable.** 🟢 **Rule adopted: order licence tests from most-constrained to
least-constrained, never alphabetically or by convenience.** CC and CC0 now resolve before the
public-domain fallback, and `--all` output distinguishes `CC-BY`, `CC-BY-SA`, `CC-BY-NC`, `CC-BY-NC-SA`, `CC0-1.0`.

## `--all`: why first-match is not "the grant"

🔴 **A first-match ladder returns *a* grant, never *the* grant.** On `microsoft/autogen` it returns `CC-BY`,
because `LICENSE` (CC-BY-4.0, 18 650 B) sorts before `LICENSE-CODE` (MIT, 1 141 B). **For anyone deciding
whether they can ship the code, that is the wrong answer.** `--all` probes every name and labels the row:

```
microsoft/autogen   EXISTS  main  027ecf0  SPLIT-GRANT[CC-BY,MIT]  2 file(s): LICENSE=CC-BY:18650B LICENSE-CODE=MIT:1141B
```

🔴 **Stated limit: `--all` detects only the multi-FILE split.** The in-file split is invisible to filename
probing by construction — `learning-commons-org/evaluators` ships **one** `LICENSE.md` that grants **four**
different things (code MIT · prompts CC-BY-4.0 · two annotated corpora CC-BY-NC-SA-4.0) and `--all` reports
`SINGLE[CC-BY-NC-SA]`. **Two split-grant shapes exist; this instrument sees one.** Read the payload prose for
any row in the checker/dataset tier.

🔴 **A second structural limit, newly measured.** [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress)
(275★) returns `NO-LICENCE-PAYLOAD/24`: WordPress plugins declare their grant in a **PHP header comment**, not
a file. `gocodebox/lifterlms`, same ecosystem, ships a GPL-3.0 `LICENSE`. **Grant location varies by project
convention inside a single ecosystem, so filename probing has an ecosystem-shaped blind spot.**
Likewise [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
licenses **per dataset and per download** through a platform catalogue, and says in terms that its
`Open + Gated` and `Gated` content are *not* covered by the CC licences the same file references. **A
repo-root read cannot resolve a data-layer grant.**

## Licence families this instrument knows by name

Permissive: **MIT · Apache-2.0 · BSD · ISC · ECL-2.0 · Zlib · MPL-2.0 (weak) · CC0-1.0**
Copyleft: **GPL-3.0 · AGPL-3.0 · LGPL-3.0 · EUPL-1.2**
Content: **CC-BY · CC-BY-SA · CC-BY-NC · CC-BY-NC-SA**
🔴 Source-available but **not OSI**: **BSL-1.1 · Fair Code · Sustainable Use License** — named explicitly so
they can never be reported as open source. `leemonade/leemons` (292★, listed under `topics/lms`) is
**Fair Code License v1.0**, and v2 would have shown it as `OTHER/unclassified`.

🟢 **EUPL-1.2** is carried for the same reason ECL is: the **European Union Public Licence** is the grant EU
public bodies are steered toward, so an EMEA public-sector education engagement is where it will appear.

## The oracle map — what discriminates under this session's egress proxy

| probe | real slug | invented slug | discriminates? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | prints only the proxy's `200 Connection Established` | same | 🔴 **no** |
| `curl -o /dev/null -w '%{http_code}' https://github.com/<slug>` | **403** | **403** | 🔴 **no** |
| `curl .../api.github.com/repos/<slug>` | **403** | **403** | 🔴 **no** |
| `git ls-remote --symref https://github.com/<slug> HEAD` | ref + SHA | empty | 🟢 **yes** |
| `raw.githubusercontent.com/<slug>/<SHA>/<file>` | `200` + bytes | `404` (14 B) | 🟢 **yes** |
| 🆕 **`WebFetch` on `https://github.com/topics/<t>`** | 🟢 **renders the page, stars and the topic total** | — | 🟢 **yes — and `curl` on the same URL is 403** |

🆕 **Recorded this pass:** `github.com` HTML is reachable through **`WebFetch`** while `curl` on the identical
URL is 403. Star counts and topic totals come from there; `--all` and the two bottom rows do the grants.

🔴 **Also re-confirmed (`P944`/`P950`): the policy-source block is an EGRESS ALLOWLIST, not DNS.** Four primary
sources needed this pass — `cbse.gov.in`, `digitaleducationcouncil.com`, `hepi.ac.uk`, `unu.edu` — all returned
`000`/0 B under `curl`, and `WebFetch` on the same host returned `ENOTFOUND`. **Per `P950` these were not
retried per-host.** Every figure drawn from them in `intel/` is therefore labelled *search-summary, primary
source unreachable* — never as a primary read.

## Rules it enforces

1. **Pin the SHA.** The payload is fetched at the resolved commit, never at a branch name.
2. **Classify from the text, not a badge, and not a blog.**
3. **Two-sided control every run.** An invented slug must return `ABSENT`; `moodle/moodle` must return
   `COPYING.txt` at **35 147 B**. 🟢 **Held 4 of 4 and 9 of 9 respectively this pass**, byte-identical to the
   seven prior passes that measured it.
4. **Order tests most-constrained first** (see the self-caught defect above).
5. **The probe count is printable** (`--count`), so no document can publish a reach the code does not have.
