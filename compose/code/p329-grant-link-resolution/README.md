---
industry: education
region: Global
updated: 2026-10-20
---

# `p329-grant-link-resolution` — the licence claim that points at its own missing grant

**What it measures.** For a single repository: whether a licence **claim made inside the repository**
resolves to a **grant file the repository actually ships**.

- `declared` — every SPDX identifier the README asserts;
- `claim_links` — the **repo-relative** paths by which the README points at its own grant;
- `grants` — the grant-shaped paths present in the **full enumerated tree**;
- `verdict` — one of `GRANT_PRESENT` · `DEAD_LINK_GRANT` · `CLAIM_WITHOUT_GRANT` ·
  `NO_CLAIM_NO_GRANT` · `UNKNOWN_NO_README`;
- `usable` — **the only field a sourcing decision should read.**

## 🔴 Read this first: why p328's rule did not catch this

**This base's licence ladder, in order, so the novelty claim is auditable:**

| pass | the case |
|---|---|
| **p322** | README declares X, the shipped `LICENSE` says Y. **Two files present, disagreeing** (four times inside one org) |
| **p314** | a complete MIT grant that never says *"MIT"*; and one repo declaring a different licence on every channel it has |
| **p324** | **the licence file is not the grant — in either direction** |
| **p328** | a third-party **comparison blog** asserts a licence the repo does not ship (`foradian/fedena`). Rule: *"a licence asserted by anything other than the repository's own grant file is a **lead**, not a fact"* |
| **p329** | **the repository's own README declares MIT, links to its own `LICENSE` by relative path, and that path does not exist on any branch** |

🔴 **p328's rule sends the reader to "the repository's own grant file". That is exactly where these
READMEs send you, and the file is not there.** A reader obeying the rule clicks the README's own
link, gets a 404, and may read a 404 as a transient fetch error rather than as an **absent grant**.

🟢 **One word changes in the rule, and this instrument is that word:** the test is **not** whether a
claim is *in* the repository. The test is whether the claim **is the grant**.

🔴 **And the badge is structurally incapable of helping.**
`https://img.shields.io/badge/License-MIT-yellow.svg` is a **static image URL** — a string the
author typed, not a licence lookup. **It renders a green *License: MIT* forever, including for a
repository with no licence at all.** Both p329 cases carry one. So `has_static_badge()` exists to
record the badge **as a claim** and the instrument never treats it as evidence.

## 🔵 The nearest existing instrument, and why this is not it

[`compose/code/p254-scoped-grant-reference/`](../p254-scoped-grant-reference/) already states
**`P1065`: *a POINTER to a licence is not a GRANT*** — and its subject looks like this one's until
you read it. 🔴 **p254's pointer RESOLVES.** `steveyeow/Feynman` ships a root `LICENSE` (canonical
MIT) whose last 150 bytes point at `app/pro/LICENSE`, **and that file exists and is a real BSL 1.1**:
the repository is genuinely **dual-scope**, and p254's finding is about a *family misclassification*
over two real grants.

🟢 **p329's pointer resolves to nothing, and the pointer is not in a grant file at all — it is in the
README.** So the two instruments sit on opposite sides of the same principle: **p254 asks *which*
grant governs which path when several real grants exist; p329 asks whether a grant exists at all
when a claim says one does.** 🔵 **Kept apart deliberately** — p254's discriminant is BSL's four
mandatory parameters read out of licence text, and this file never reads licence text at all.

## The two controls that are not optional

**P275 / P278 — an absence must be ENUMERATED.** *"To sustain an absence in a tree you must
enumerate it"*; *"a count of ZERO over a path that does not exist in that ref measures the PATH, not
the content."* 🔴 **So `classify()` takes the full `git ls-tree -r --name-only` output across every
branch, and passing an empty tree RAISES** — because "no paths" means *you did not enumerate*, not
*there is no grant*. A 404 on `LICENSE` proves nothing about `LICENSE.md`.

**P126 / P151 — a missing input is `UNKNOWN`, never a convenient default.** A repository with no
README is **not** an unlicensed repository; it is one this instrument cannot speak about. Hence
`UNKNOWN_NO_README`, with `declared = None` rather than `[]`. **`[]` means "asked and found none";
`None` means "could not ask"** — and a `0`/`[]` that should have been `None` is exactly the P151
defect: an implausible output that enters a diff without anyone looking at it.

## The p329 measurement, with its invocation beside it (P107)

```bash
./capture.sh techpivot25/Educate-AI            # -> capture/techpivot25_Educate-AI/{README.md,tree.txt,activity.txt}
./capture.sh Naresh1401/education-tutor-agent
PYTHONPATH=. python3 test_grant_link.py        # 33 assertions
```

| repo | declared | claim link | grant files in FULL tree | verdict | usable |
|---|---|---|---|---|---|
| `techpivot25/Educate-AI` | `MIT` (badge + `## License` + `[MIT License](LICENSE)`) | `LICENSE` → **404** | **0** of 42 enumerated files | 🔴 `DEAD_LINK_GRANT` | 🔴 **False** |
| `Naresh1401/education-tutor-agent` | `MIT` (badge + `## License`) | `LICENSE` (badge href) → **404** | **0** of 22 enumerated files | 🔴 `DEAD_LINK_GRANT` | 🔴 **False** |

🔵 **Both were returned by the search channel as *"MIT licensed"*.** Both are **all-rights-reserved
by default** and **not usable by Globant**. `Educate-AI` additionally has **no `license` field in
`package.json`** and a `name` still set to the unedited scaffold value **`react-example`**.

## What this instrument deliberately does NOT do

🔵 **It resolves the POINTER; it does not compare the TEXT.** A README claiming MIT over an
AGPL-3.0 grant file returns `GRANT_PRESENT` here — **that mismatch is p322's question** and belongs
to a different instrument (see `repos/trending.md`, p322 and p328). **Keeping the two separate is
the point:** mixing them produces a single verdict that cannot say which half failed, which is the
defect `description-drift-audit` was written to avoid in its own domain.

🔵 **`NOTICE` is held apart from the grant.** An Apache-2.0 `NOTICE` is an attribution file, not a
licence grant — the shape the Learning Commons repositories ship — so it is reported in
`attribution_only` and never satisfies `usable`.

🔵 **A remote licence link is not a grant by this repository.** A link to `opensource.org` or
`choosealicense.com` points at the licence **text** on the web; it grants nothing. Only
repo-relative targets are collected.

## Channel note (p329)

`github.com` → **403**. `api.github.com` → **403**. `raw.githubusercontent.com` → **200**.
🟢 **`git clone --filter=blob:none` on third-party public repos → OPEN**, which is what makes full
tree enumeration possible at all this pass. `capture.sh` therefore also writes `activity.txt` with
the **`(commits, authors, last_commit)`** triple — free once the history is local, and p329's other
finding. See `evidence/p329-git-activity-channel.2026-10-20-p329.tsv`.

## 🟢 How this instrument's own gates went, recorded because it is the useful part

**This base's ratchets caught this instrument twice before it shipped, and both times the fix was
the cause rather than the pinned number.**

| gate | what went red | the fix |
|---|---|---|
| `p252-ungated-floors` | a new suite arrived **ungated** — `ungated AND explicit-exit` rose **110 → 111** | 🟢 **Gated it in `make hooks`**, which is this base's stated convention: *"+1 file and +1 gated — written and gated in one pass… the `ungated` figure does NOT move"* |
| `p283-ladder-case-audit` (1st) | gating moved it into the **STANDING** population, where `grant_link.py`'s private `licen[cs]e\|copying` regex graded **`CASE-UNVARIED`** — ceiling **7 → 8** | 🟢 **Imported `lib/licence_identity.LICENCE_NAMES`** instead (P441: *a PATH predicate is not rewritten as a name list*; P237: the question is asked once) |
| `p283-ladder-case-audit` (2nd) | `capture.sh` spelled the readme filename by hand across three branches — the same defect in a different family | 🟢 **Looked it up in the enumerated tree** (`git ls-tree --name-only` on the default branch, matched case-insensitively). **This also removed a real false negative**: any other readme spelling would have produced `NO-README`, and `classify()` would then have returned `UNKNOWN_NO_README` over a repository that ships a perfectly good readme |

🔵 **Neither ceiling was bumped.** The ratchet's own notes say that a ceiling over the wrong
population is what *"trained eight passes to bump a number"* — **so the point of this episode is
that the gate was allowed to win twice, and the instrument is better for both.**
