# `p314-untitled-payload-arm` — the first arm on this base keyed to a payload SHAPE

Every dynamic arm before this one was keyed on a licence **family**: `p311` on `MIT` and
`Apache-2.0`, `p312` on five, `p313` on the noncommercial four. This one holds the family **constant**
and varies the payload's shape, because that turned out to be the variable that decides whether a
classifier can read a grant at all.

## What it answers

`ACTION p313-R` item 5 asked for a `BSD-3-Clause` fixture, and said why: `301` published cells (now
`331` — the shelves moved between two passes of the same day), and
[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) serves a complete, valid grant
with **no title line and zero `BSD` tokens anywhere in the file**. `p313` wrote that *"no automated
channel here can read it"* — honestly flagged as inference, because the code channel was refused in
that session.

**The code channel runs here, so this arm measures it instead. The inference was wrong.**

| reading | classifiers | mechanism |
|---|---|---|
| reads BOTH shapes, both families | `p198`, `p228`, `p306`, `p211` | the family is read off the **CLAUSE STRUCTURE** |
| **TITLE-ONLY** on `MIT` | `p419`, `p191`, `p153`, `p150` | reads the titled payload, **abstains** on the untitled one |

The discriminator is **whether the instrument kept a body fallback underneath its title ladder** —
not the family, and not the ladder. The sharpest instance is `p198-title-line-family`, whose entire
thesis is *"classify on the TITLE LINE, not on a window"*: it is one of the four that survives,
because two lines at the bottom of it fall through to the grant clause. It is title-line-**first**,
not title-line-**only**.

## The class is bigger than one family, and it reaches the vertical

Three untitled payloads, found in a single hour:

| payload | family | bytes · sha | note |
|---|---|---|---|
| `crewAIInc/crewAI` | `MIT` | `1 055` · `28868731966f` | the complete `MIT` grant; the token `MIT` is **not in the file** |
| `jupyterhub/jupyterhub` | `BSD-3-Clause` | `1 475` · `7069c7e8d60e` | `p313`'s payload, replicated to the byte |
| `open-tutorai/open-tutor-ai-ce` | `BSD-3-Clause` | `1 531` · `57c341d09920` | **zero tokens of ANY family**, and an education-native platform |

`MIT` is the family holding **more than a third of every licence cell this base publishes**. And the
third row is the one that costs something: a permissive, education-specific tutoring platform whose
grant is invisible to every title-keyed channel, so `P250` turns the abstention into `PROHIBITED` and
**usable supply is discarded**. The loss always runs that way — supply excluded, never a wrong
licence shipped.

## The accident channel

`crewAI`'s payload contains no `MIT` token, and the substring form `"mit" in low` returns `True` on
it anyway: it matches inside `permit`, `limitation` and `LIMITED`. This base's most-repeated defect
class (`p306`'s `"affero" in low`, `"cc0" in low`) has until now only ever been a *possibility*.
Here is the payload that makes it a measured false friend, so the arm reports the token channel
beside the verdict — **a classifier that is right on this file may be right by accident, and the two
must never be counted together.**

## Also discharged here

- **`ACTION p313-R` item 2a** — `same_grant()` returned `False` on a single document because of an
  `http`/`https` difference in the `MPL-2.0` *Exhibit A* notice. Step `0c` in
  `p311/payload_identity.py` normalises the scheme, bounded by controls asserting it is not a URL
  eraser (host, path and query must each still separate two documents). The pair also supplies the
  control item 2a asked for in its own words: **two payloads of EQUAL length that are different
  files** (both `16 726` B, shas `fab3dd6bdab2` / `3f3d9e0024b1`) — the converse of `p311`'s rule,
  and an equality that is pure compensation coincidence.
- **`ACTION p313-R` item 4** — `is_this_a_grant()`, asked **before** `is_this_the_same_grant()`.
  All four of `p313`'s noncommercial payloads grade `NOT-A-GRANT`: a deed summary caught by its own
  disclaimer, a paraphrase and two bare citations caught by a per-family length floor. The verdict is
  deliberately **asymmetric** — `GRANT` is the absence of a refutation, never a certification.
- **`ACTION p313-R` item 5** — both `BSD-3-Clause` shapes pinned, with a control that they are
  genuinely two documents so the item cannot be satisfied by pinning one file twice.

## Two repairs this arm forced in other passes' files

- `p310`'s `COARSE` map gained `bsd-family`, which `p211` declares in its own source as its answer
  for the BSD redistribution clause absent a clause-count title. It graded `DEFECT` for one reason
  only — absence from that dict — which is *verbatim* what the dict's own `p311`-era comment says it
  must never do again. **Third instance of that one mechanism in that one dict.**
- `p311`'s `test_the_two_noncommercial_families_are_still_uncovered` was **inverted**, as its own body
  instructed and as item 3 asked. The inversion is *not* "now covered": `CC-BY-NC-ND-4.0` is covered
  **by payload and by no grant**, which the coverage census cannot see because it counts payloads.
  That is `p311`'s own conflation one storey up → `ACTION p314-R` item 1.

## Running it

```
make gate-untitled-payload   # 21 controls + the arm, wired into `make hooks`
make untitled-arm            # the dynamic arm alone
```

## The naming note that cost a ratchet

`is_this_a_grant()`'s second verdict is spelled `NOT-A-GRANT` and not the obvious English word for a
distribution notice. That word is `p283-ladder-case-audit`'s **path vocabulary**, and putting it in a
code string rather than a comment regraded `payload_identity.py` from `COMMENT-ONLY` to
`SINGLE-SPELLING`, moving the standing ratchet for a module that probes no paths at all. This is
`ACTION p311-R` item 4's class, met a third time — and the first time the ratchet caught it within
the hour. **The token was renamed, not the ceiling raised**, and a control keeps it renamed.
