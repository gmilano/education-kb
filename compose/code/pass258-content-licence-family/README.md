# `pass258-content-licence-family` — the licence class these shelves carry MOST is the one the gate could not name

**The measurement**, taken `2026-10-17` against the seven canonical Creative Commons
payloads fetched first-hand from
[`spdx/license-list-data`](https://github.com/spdx/license-list-data) and run through
[`pass257-restriction-scan`](../pass257-restriction-scan/) in the same hour:

| payload | bytes | `p257` family | `p257` verdict | hits |
|---|---|---|---|---|
| `CC0-1.0` | `7 048` | `NONE` | 🔴 `UNCLASSIFIED:no-family-no-restriction` | `[]` |
| `CC-BY-4.0` | `17 023` | `NONE` | 🔴 `UNCLASSIFIED:no-family-no-restriction` | `[]` |
| `CC-BY-SA-4.0` | `18 375` | `NONE` | 🔴 `UNCLASSIFIED:no-family-no-restriction` | `[]` |
| `CC-BY-ND-4.0` | `16 830` | `NONE` | 🔴 `UNCLASSIFIED:no-family-no-restriction` | `[]` |
| `CC-BY-NC-4.0` | `17 649` | `NONE` | 🟢 `RESTRICTED:added-restriction` | `noncommercial` |
| `CC-BY-NC-SA-4.0` | `19 018` | `NONE` | 🟢 `RESTRICTED:added-restriction` | `noncommercial` |
| `CC-BY-NC-ND-4.0` | `17 452` | `NONE` | 🟢 `RESTRICTED:added-restriction` | `noncommercial` |

🟢 **The `NC` half is already caught, and that is said first.** `p257` built its
vocabulary for commercial source-available licences, and it fires correctly on
Creative Commons `NonCommercial` without having been designed for it. Nothing
non-commercial was ever published from these shelves as permissive.

🔴 **The hole is rows 1–4.** `CC0-1.0` is a public-domain dedication — the most
permissive grant that exists — and `CC-BY-ND-4.0` forbids distributing an adaptation
at all, which is exactly what a studio does with material. **The live gate reports
them identically.** The cause is measurable rather than arguable:

```
>>> [t for t in restriction_scan.RESTRICTION_TERMS if "deriv" in t]
[]
```

`ND` is not a near-miss. There is no term for a derivative restriction in the
vocabulary, so `ND` is out of scope.

## Why it matters more in education than it would elsewhere

**Instructional material is licensed as content, not as software.** The census this
instrument publishes — `content_licence.py --census` — found, across the ten shelves:

| class | tokens | share |
|---|---|---|
| `CONTENT-PERMISSIVE` *(`CC-BY`, `CC0`)* | `421` | `50.8 %` |
| `CONTENT-COPYLEFT:share-alike` | `216` | `26.1 %` |
| 🔴 `CONTENT-RESTRICTED:non-commercial` | **`191`** | **`23.1 %`** |
| **total** | **`828`** | |

`828` Creative Commons tokens is the single largest licence class on this base, and
🔴 **`191` of them cannot ship in a paid client deliverable.**

🟢 `is_usable_permissive` was never wrong — `p257`'s `USABLE_VERDICTS` is closed on
`{MIT}`, so no CC payload was ever published as a usable permissive grant. **The
defect is in the EVIDENCE**, which is `p257`'s own lesson repeating one layer out, on
a population two orders of magnitude larger than the one `p257` found it on.

## What it answers

| call | question |
|---|---|
| `family_of_content(text)` | an SPDX-shaped identifier, or `None` for anything that is not a CC **grant** |
| `content_verdict(text)` | one of six verdicts; strictest axis wins |
| `is_usable_in_deliverable(text)` | the studio question, closed-set and failing closed |
| `coverage(root)` | 🔵 `p256`'s lesson built in: the **size** of the covered population, beside the claim of covering it |

## Three things measured rather than assumed

🔴 **`CC0`'s identifier is on line 2.** Its line 1 is the generic heading
`Creative Commons Legal Code`. A line-1-only title anchor grades `CC0-1.0` — the most
permissive grant there is — as `CC-BY`. `TITLE_WINDOW = 6`, and the mutation to `1`
fails four controls.

🔴 **The title window is the right test for a GRANT and the wrong test for a
POINTER.** This instrument's own first draft graded the real Carpentries pointer
([`datacarpentry/r-socialsci`](https://github.com/datacarpentry/r-socialsci)'s
`LICENSE.md`, `3 357` B) as `NOT-A-CONTENT-LICENCE`, because that file opens with YAML
frontmatter and an `## Instructional Material` heading and does not say *"Creative
Commons"* until line `8`. A pointer buries the name in prose; a legal text puts it
first. Hence two predicates — and `names_content_licence` is body-wide, which is safe
**only** because it is never used to assign a family. 🔵 `p257` established that
family anchors cannot be matched body-wide, since `GPL-3.0` §13 quotes the Affero
licence's name.

🔴 **A closed set can be decorative in one direction.** This suite's own mutation run
deleted `CONTENT-RESTRICTED:non-commercial` from `UNUSABLE_VERDICTS` and produced
`72` controls and `0` failures: `is_usable_in_deliverable` ends with a closed positive
list, so the mutant stayed behaviourally identical while the set *looked*
load-bearing. 🔵 Two guards, one carrying the weight and the other assumed to — this
base's recurring shape, met inside the instrument written to close another instance of
it. Three controls now pin the set itself and the census total computed over it, and
that mutant fails all three.

## Controls

`76`, run by `make hooks`. **Proven able to fail:** four mutants of the subject were
run and the control count held at `76` for every one of them — no silent skip.

| mutant | failures |
|---|---|
| `ND` dropped from `content_verdict` | `2` |
| `TITLE_WINDOW = 1` | `4` |
| `NC` removed from `UNUSABLE_VERDICTS` | `3` *(`0` before this run's own fix)* |
| pointer branch removed | `1` |

Every fixture in `fixtures-p258/` is a payload read first-hand at `p258` — the seven
SPDX texts, the real Carpentries pointer, the real `CC-BY-4.0` payload from
[`microsoft/AI-System`](https://github.com/microsoft/AI-System) (`18 653` B), and an
`MIT` payload as the negative control.

## Scope, stated so a later pass does not over-read it

This instrument grades **content** licences. It does not replace
[`pass257-restriction-scan`](../pass257-restriction-scan/), which grades software
grants; the two are complementary and control `10` asserts the boundary, so that if a
later pass teaches `p257` a CC family this suite fails and whoever did it is told to
re-scope rather than leave two overlapping instruments.

`classify_token()` grades a licence **identifier as written on a shelf**, with no
payload behind it. That is weaker evidence than a payload read first-hand and is
labelled as such wherever it is used: a shelf cell is a claim a previous pass made,
not a grant this pass read. 🔴 **The `828`-token census is therefore a census of
CLAIMS, not of verified grants** — re-reading those payloads first-hand is registered
as `ACTION YV`.
