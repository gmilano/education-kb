# p203 — grant blob reader

Reads a repository's licence **from its own blob** and reports the family, the
**path** the grant was found at, and whether the instrument carries **two scopes**
(content vs code).

## Why it is split in two files

p203 measured the execution seam in this environment and it is a **conjunction**,
not either axis alone:

| | inline command | committed script |
|---|---|---|
| **no network** | — | 🟢 **runs** (`test_classify.sh`, 19/19) |
| **network** | 🟢 **200** (~300 reads this pass) | 🔴 **refused** |

So `classify.sh` holds every decidable rule with **no network**, and
`read_grant.sh` holds the fetch. A pass can always run the suite; the fetches are
performed inline by the pass and this script is the record of method. In CI the
seam does not exist and `read_grant.sh` runs directly.

This refines the note at `compose/code/lib/README.md` (pass 74): *"el seam real no
es librería vs script, es RED vs NO-RED."* Correct about scripts, but incomplete —
inline network calls are allowed, so the predicate is **network AND from-file**.

## Use

    ./read_grant.sh adlnet/ADL_LRS cybercussion/SCOBot swcarpentry/git-novice
    ./test_classify.sh          # offline, no network

## What it is for

Three things a repo-level licence label cannot tell you, each of which cost this
KB a wrong row:

1. **The family, from the title line** — not from a badge, a README claim or a
   package manifest. `cybercussion/SCOBot` labels as a SCORM JS library and its
   `LICENSE` is `CC-BY-SA-4.0`.
2. **The path** — 12 of 202 shelf rows carrying a grant hold it at `LICENSE.md`
   or `LICENSE.txt`, so a bare-`LICENSE` probe reports them as ungranted.
3. **The scope** — the Carpentries `LICENSE.md` grants instructional material
   `CC-BY-4.0` and example code **MIT** in one file. One cell cannot say that.

## Reading the output

`NO-GRANT-AT-PROBED-PATHS` means **this probe did not find one**, over `$REFS`
and `$PATHS`. It is not a finding of "no licence": a repo whose default branch is
neither `main`, `master` nor `gh-pages` returns the same token.
