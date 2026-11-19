# `p923` offline fixtures — the grant authority's family detector

Two classes of file, and they are **not** the same kind of evidence.

## `apache-1.1.payload`, `apache-1.0.payload` — REAL, primary, first-hand

Fetched `2026-11-19` from the ASF's own published texts
(`https://www.apache.org/licenses/LICENSE-1.1`, `.../LICENSE-1.0`), with apache.org's prose
preamble stripped so the file begins where a repository's `LICENSE` would begin. These are the
fixtures `922-G2` asked for and could not obtain.

They exist because `923-F1` measured both as **`BSD / BODY-BSD`** on the unfixed instrument:
neither contains the string `apache license`, which is the name the ASF only adopted at 2.0.
Apache-1.1 is titled *"The Apache Software License, Version 1.1"*; Apache-1.0 carries **no
licence title at all**, only `Copyright (c) 1995-1999 The Apache Group`.

🔵 Note while reading them: apache.org serves **both** files under the heading
*"=== An example Apache Software License 1.1 file ==="*, including the 1.0 one. The heading is
wrong on the ASF's own page; the licence bodies below it differ and are correct. The 1.0 body
carries the **advertising clause** (clause 3) that 1.1 removed — which is the structural
discriminator `923-F3` grades on.

## `*.titletest` — SYNTHETIC, and they are NOT evidence about any repository

Four constructed title lines exercising the Creative Commons **element ordering** fixed in
`923-F5`. They are a grader unit test and nothing else.

🔴 They are synthetic because **no real `CC-BY-NC-SA` payload was obtainable through either
channel available to this base**: `creativecommons.org` returns **HTTP 403 at the proxy**
(a third host joining the `920-G5` no-primary-legal-text class), and GitHub's licence search
rejects `license:cc-by-nc-sa-4.0` as an unindexed key (**HTTP 422**). The ordering fix is
therefore *reasoned and unit-tested*, not *measured* — declared as `923-G2`.

The real CC fixtures this pass did measure are two live repositories, in
`../../evidence/catalogue-grant-census.2026-11-19-p923.tsv` and
`../../evidence/grant-authority-controls.2026-11-19-p923.tsv`:
`bilalabic/awesome-turkish-datasets` (18,657 B `9ba9550ad484`, **CC-BY-4.0**) and
`jwasham/coding-interview-university` (20,130 B `da89f9867822`, **CC-BY-SA-4.0**).

## Running them

    ingest/p923-adjudicator-harness.sh ingest/fixtures-p923/*.payload ingest/fixtures-p923/*.titletest

The harness extracts `adjudicate()` from `p913-grant-authority.sh` **by its own delimiters**, so
it cannot drift out of date the way a line-range extract did on this pass's first cut.
