# p211 — full-column grant audit

Reads the licence blob of **every** repository on the four client-facing shelves
first-hand, classifies it, and adjudicates it against what each table cell says.

## Why this is new

Every prior pass audited a *sample*: p209 and p210 hand-read ten rows each.
The blocker was believed to be the channel — p210 recorded *"curl is refused at
CONNECT for every host including GitHub (403); WebFetch resolves github.com
only."*

**That is too strong.** `raw.githubusercontent.com` answers `200` to a plain
`curl GET` from this environment. 494 licence blobs were read this way in one
pass. `api.github.com` and `github.com` really are `403`, and `example.com`
really is `000`, so the *general* egress statement stands — but the one host
that serves licence bodies is reachable, and that is the host this audit needs.

Second simplification: the ref **`HEAD`** resolves a repository's default
branch. The branch axis disappears, and with it most of the "90-form locator".
8 path forms served 100% of the 494 findable blobs; plain `LICENSE` served 86%.

## Order of operations (each step is a lesson an earlier pass paid for)

1. **Riders before the title walk** (p207). A Commons Clause *amends* the
   licence beneath it, so a title walk that finds the inner licence returns a
   clean permissive answer on a source-available grant.
2. **Title window only** (p205 / `Gap 466`). `GPL-3.0`, `MPL-2.0` and `ECL-2.0`
   quote the AGPL and Apache inside their own text; a whole-body matcher
   misclassifies them.
3. **STATED vs BODIED** (p210). A 19-byte `License: GNU GPL V3` names a family
   without granting it. Recorded as its own state.
4. **Per-cell adjudication** (p208). A row is judged against its own cell, not
   against the union of every value printed for that repository.

## Validation

Run against the 20 rows p209 and p210 read by hand: **20/20**. The classifier
was *wrong twice* during development and both were caught by this ground truth
— it missed `CC-BY-NC-SA` and the bare `Attribution 4.0 International` title
form. Both are fixed; without the ground-truth set both would have shipped as
five false "corrections".

## Usage

```sh
python3 -I extract_rows.py <shelf.md>... > rows.json
cat repos.txt | xargs -P 14 -I{} ./fetch_one.sh {} blobs/ > fetch_results.tsv
python3 -I classify.py blobs/ fetch_results.tsv > classified.json
python3 -I compare.py rows.json classified.json mismatches.json
```

Offline after the fetch step.
