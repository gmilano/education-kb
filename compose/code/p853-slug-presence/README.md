# `p853-slug-presence` — `852-G3` / `T174`, built: a presence check that is correct in BOTH directions

`852-G3` asked for *"one instrument that compares `owner/repo` at a word boundary in BOTH the URL
and bare-slug forms, rejects prefix matches, and is wired into `hooks`"*. This is it.

## What it is for

A pass must know, before it writes a row, whether this base already holds an address. `p852`
measured its own presence check failing in both directions in the same hour:

| Direction | Instance measured at `p852` | Cost |
|---|---|---|
| 🔴 **UNDER-report** — a URL-keyed index | `weizhenFrank/AutoGrader` reported absent; it sat in `agents/trending.md` as a bare `owner/repo` slug with no URL | a false NEW ⇒ a duplicate shelf row |
| 🔴 **OVER-report** — a substring check | `UOC/java-lti-1.3` reported present because `UOC/java-lti-1.3-provider` — a different, dead repository (`772-K31`) — contains it as a prefix | a false PRESENT ⇒ a live permissive row suppressed |

## The contract

An address is PRESENT when this corpus names **that** repository, in URL form or bare-slug form,
at a word boundary no longer repository name can satisfy.

* `.git` terminates a slug (`owner/repo.git` IS that repository); `owner/repo.js` is not.
* A path under the repository still counts (`…/owner/repo/blob/main/LICENSE`).
* Matching is case-insensitive, because GitHub resolves owner and repository names that way.
  🔴 **This is NOT true of `raw.githubusercontent.com` PATHS** — `852-G2`'s defect — and that is a
  different instrument's problem (`ingest/`'s probe lists), deliberately not conflated here.
* `raw.githubusercontent.com`, `api.github.com/repos` and `codeload.github.com` are URL hosts too,
  so the check can see this base's own byte-read evidence lines.

## Two findings from its first hour, neither of which the gap text predicted

🔴 **(1) The two arms are complementary, not nested.** The obvious repair — "match the bare slug,
a URL contains it" — is wrong: the bare arm's look-behind must reject a preceding `/`, or
`foo/owner/repo` matches `owner/repo`. So a URL-only line is invisible to the bare arm *by
construction*, and an instrument that keeps one arm re-opens `852-G3` in the other direction.
Both arms are asserted separately in the suite, and `classify()` returns the FORM (`url`, `bare`,
`both`, `absent`) because collapsing the form is what hid `p852`'s failure.

🔴 **(2) It polluted its own measurement.** On its first run over the live corpus it reported
three never-before-seen candidates as PRESENT; their only hits were in this directory's own test
fixtures. Hits therefore carry a TIER, and the verdict vocabulary is `p852`'s taxonomy:

| Verdict | Means | What a pass should DO |
|---|---|---|
| `SHELVED` | on `agents/top.md`, `repos/foundations.md` or `verticals/solutions.md` | nothing; it is graded |
| `UNGRADED` | written down in trending / evidence / gaps, on no shelf | **promote it** — `p852` found `13` of `17` here |
| `FIXTURE-ONLY` | named only inside `compose/code/` | treat as NEW; it is test data |
| `NEW` | absent from the whole non-archive corpus | research yield |

🔵 `853-G4` carries the generalisation: every OTHER index in this base walks the same tree with no
fixture tier, so the published address census is inflated by an unmeasured number of fixtures.

## Use

```sh
# one or more addresses, URLs accepted
python3 -I compose/code/p853-slug-presence/presence.py --root . owner/repo https://github.com/a/b
# with the matching lines
python3 -I compose/code/p853-slug-presence/presence.py --root . --evidence owner/repo
```

## Controls

`35` offline controls, no network, and they pass BOTH from the repository root under
`python3 -I` and from inside this directory — `p355-cwd-portability`'s requirement, which is the
documented reason a working gate stayed a one-off in this base before.

```sh
make gate-slug-presence
```

Every case in the suite is a measured one: `p852`'s two failures, the `772-K31` family collapse in
both directions, the `.git` and sub-path terminators, case variance, a same-name repository under
a different owner, and the fixture tier.
