---
industry: education
region: Global
updated: 2026-10-14
---

# `p202-grant-scope-reader/` — `ACTION OR`, and the shared preamble does NOT defeat it

`ACTION OR` pre-registered: **limb 1**, the reader emits `(path → grant)` for all `3`
split-scope rows and distinguishes `pupilfirst`→**MIT** from `leemons`→**Fair Code**
despite their identical preamble → split scope becomes mechanical. **limb 2**, the shared
preamble defeats it → the preamble must become a trigger for manual review.

🟢 **Limb `1`. Suite `23`/`23`, offline.**

## 🔵 Why it was never going to be the preamble

p201 recorded that `pupilfirst` and `leemons` *"open with the SAME sentence verbatim"*.
🔴 **They do not — they share a TEMPLATE and differ by two words,** which is a correction
of the same precision class as `Gap 452`:

| repo | the fallback clause, as read |
|---|---|
| `leemonade/leemons` | `Content outside of the above mentioned `**`files or `**`restrictions is available under the "`**`Fair code License`**`" as defined below.` |
| `pupilfirst/pupilfirst` | `Content outside of the above mentioned restrictions is available under the "`**`MIT`**`" license as defined below.` |

🟢 **The discriminator was never the preamble. It is the licence named inside the FALLBACK
clause** — the grant covering everything the exceptions do not, which is exactly the field
a repo-level licence column silently reports as the whole truth.

## 🔴 And reading scope found a third grant on `pupilfirst` the KB did not have

`pupilfirst` is a **three-grant** repository, not a two-grant one:

| scope | grant |
|---|---|
| `docs/` | 🔴 **CC-BY-SA-4.0** |
| client-side JavaScript | **MIT** |
| third-party components | `UPSTREAM-OWN` |
| everything else *(fallback)* | **MIT** |

🔴 **So "pupilfirst is MIT" is true of its code and false of its documentation** — and
documentation is a teaching asset in this industry, not a build artifact.

## 🟢 The dual-grant defect this suite caught in its own reader

The first version read `human-skill-tree`'s `skills/` as plain `AGPL-3.0` by taking the
first licence name in the clause. 🔴 **The clause says `AGPL-3.0` OR `MIT`, at the
licensee's option — and the MIT limb is the ONLY fact that makes those payloads shippable
inside a closed client deliverable.** Collapsing a dual grant to its first name discards
precisely the field that decides the engagement. Now `AGPL-3.0-OR-MIT`, with a regression
case asserting the option does **not** leak to `app/` (`AGPL-3.0` only).

## Files

| file | what it is |
|---|---|
| `scope_reader.py` | `has_split_scope_preamble`, `fallback_grant`, `scopes`, `content_family`, `non_osi_family`, `classify`. **Does not name licence families** — that is `lib/license_family.sh` (`P237`), and the suite asserts the absence |
| `test_scope_reader.py` | **23/23, OFFLINE.** The loaded case is `ACTION OR`'s falsifier |
| `fixtures/PROVENANCE.tsv` | 🔴 **Read this before quoting a byte figure.** Only `leemons.LICENSE.md` is a complete file (copied from `p119`'s committed evidence). The other two are part-verbatim, part-reconstructed from a channel summary, and the table says which lines are which |

🔵 **`silence is never a grant`** is a contract here: a scope line that names no licence
returns `None`, and a notice with no fallback clause returns `None` rather than a guess.
