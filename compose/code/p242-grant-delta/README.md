# `p242-grant-delta` — what the ADDITION DOES, and the question `ACTION VU` asked wrong

**Pass 242 · 2026-10-16 · 23/23 controls · every fixture a payload read first-hand**

## What it detects

Given a licence payload, whether its departure from a canonical licence text

- **DISCLOSES** more (upstream attribution, a third-party component notice),
- **NARROWS** the grant (a field-of-use clause),
- **TRANSITIONS** it (a relicensing, bound to an effective date),
- is a **STANDARD** licence text with nothing added at all, or
- cannot be read — in which case it is **not cleared**.

## Why it exists

Two instruments on these shelves answered a question they were not asked, and both
were wrong in the same direction: they read *any* departure from a canonical payload
as a change to the **grant**.

### 1 — `p1054` marked a usable row unusable

`p1054` returns `MIT-BODY-PLUS:unclassified-addition` and `is_usable_permissive() ==
False` for [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp)
(`1 200` B · `main`). Its `50` bytes of excess, read first-hand:

> Portions of this software are derived from brightspace-mcp-server,
> Copyright (c) 2026 Rohan Muppa, used under the MIT License.

That is an **upstream attribution**. It grants no less than MIT — it discloses where
the code came from. And the upstream it names,
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server),
was read first-hand in the same pass (`1 068` B · `a6fa134d2a13`) and classifies `MIT`.

🔴 **So the downstream row is MORE informative than a bare MIT file, and `p1054`
marked it unusable.** 🔵 Three channels, three answers on one payload — GitHub's API
says `NOASSERTION`, `lib/license_family.sh` says `MIT`, `p1054` says
`MIT-BODY-PLUS`. That is `P255`'s shape again.

### 2 — `ACTION VU`, implemented literally, found nothing and cried wolf four times

`p241` registered `ACTION VU`: sweep for relicensing by keying on *"a `LICENSE`
payload that names TWO licences and a DATE"*. Implemented exactly as written and
swept over this pass's `46` first-hand payloads, that shape fires on `4` and is
**wrong on all `4`**, with **`0` true positives**:

| payload | why it fired | what it actually is |
|---|---|---|
| `purysho/EduBoard` | names GPL-3.0; dates `19 Nov 2007`, `28 Mar 2007` | an ordinary `AGPL-3.0` grant |
| `fentas/lani` | same | an ordinary `AGPL-3.0` grant |
| `TouchRefletz/maia.edu` | same | an ordinary `AGPL-3.0` grant |
| `rosshd/openlearn` | same | an ordinary `AGPL-3.0` grant |

The standard AGPL-3.0 text **names GPL-3.0** — its section 13 is the cross-reference
to it — and carries **the FSF's own publication dates**. Every AGPL payload in
existence matches "two licences and a date".

🔵 **That is `P171`'s defect class one level up.** `P171`: do not read GPL's
section-13 *title* as evidence of Affero. This: do not read a licence's own standard
*cross-reference* as evidence of a second licence.

Meanwhile the real relicensing — [`snflwr-ai/snflwr.ai`](https://github.com/snflwr-ai/snflwr.ai),
`AGPL-3.0` → proprietary on `2026-09-18`, which `p241` found by reading it — is
detected by a **transition narrative** (*"was published under … from `2026-02-27`
until `2026-09-18`"*, *"Effective `2026-09-18`"*, *"PRIOR RELEASES REMAIN UNDER
AGPL-3.0"*) bound to a date **the FSF did not print in the licence**. That is the
half `ACTION VU` left out, and it is the half that decides.

## The shared root

Both instruments measure that a payload DIFFERS from a template and infer that the
GRANT differs. Those are different questions. A payload may differ because it
discloses more, grants less, or grants different things at different times — and only
the last two change what a studio may do.

## 🔴 The defect this module found in ITSELF

On its first full sweep, `delta_of` returned `NARROWING` on **all 8** GPL-3.0 /
AGPL-3.0 payloads. The reason: `p1054`'s restriction vocabulary contains
`noncommercial`, and the **standard GPL-3.0 text uses that very word in its section
6**. The matcher was reading a word belonging to the licence's *own terms* as
evidence of an added restriction.

🔴 **That is `P171`'s class a THIRD time — committed by the instrument written to
stop it.** Recorded here rather than quietly fixed, because the pattern is now three
for three: every classifier on these shelves that greps a licence body for a token
eventually reads the licence's own text as foreign matter.

**The structural fix, not a deleted token:** a payload that *is* a canonical licence
text has no delta to read. Its usability is `lib/license_family.sh`'s answer, never
this module's. Such a payload is reported `STANDARD` and this module declines to
grade it. `test_the_offending_token_is_still_present_in_the_payload` proves the
control is load-bearing: the word is still there, and is no longer read as an
addition.

**MIT is held to a stricter test, deliberately.** MIT's canonical text is short,
fully enumerated and carries no restriction vocabulary at all, so *any* restriction
term in an MIT-body payload is an addition — whatever the byte count. Size alone
would not do: `graspful`'s clause 2 is **shorter** than `p1054`'s size headroom, and
on a size-only test it would be reported `STANDARD` and never graded.

## The rule that is NOT relaxed

🔵 **`p241`'s rule holds: the absence of a known restriction vocabulary is NEVER
permission.** An addition this module cannot read stays `UNRESOLVED-addition-unreadable`
and is **not** cleared. Clearing is positive-evidence-only — an addition is cleared
when it *matches* a disclosure shape, never because it failed to match a restriction
one. `test_unreadable_addition_stays_unresolved` feeds it a German-law education
carve-out appended to canonical MIT; it is refused.

## Reuse, not re-listing (`P237`)

The restriction vocabulary is **`p1054`'s**, imported by absolute path, never copied —
a licence vocabulary living in two files is one that will diverge, and this base has
paid for that three times (`P255`, `P237`, `p241`'s cross-instrument table).
`test_p1054_vocabulary_is_imported_not_copied` asserts object identity, so a copy
cannot be slipped in later.

Imported **by path** and not by name because `make hooks` runs these suites under
`python3 -I`, which strips the script's own directory from `sys.path`
(`p355-cwd-portability`); the Makefile's `cd`-into-the-folder recipe fixes the
suite's own directory, never its sibling's.

## The sweep, over 50 first-hand payloads

| kind | n | note |
|---|---|---|
| `STANDARD` | `43` | canonical licence texts — `lib/license_family.sh` grades these |
| `DISCLOSURE` | `3` | `brightspace-d2l-mcp` + both `fedena` root `NOTICE`s |
| `CLEAN` | `3` | 🟡 **all three are MANIFESTS**, not licence bodies — see the limit below |
| `TRANSITION` | `1` | `snflwr-ai/snflwr.ai` |
| `NARROWING` | `0` | none in this harvest once the standard-text guard was in place |

## 🟡 Limits, stated

- **Do not feed it a manifest.** The `3` `CLEAN` rows above are `package.json` /
  `pyproject.toml` payloads recovered by the ladder's Tier C. A manifest carries a
  *declaration*, not a grant body, and `p222-ecosystem-bound-grammar` is its reader.
  `CLEAN` on a manifest means "this module found no delta", not "this is permissive".
- **`DISCLOSURE` asserts no family.** `fedena`'s root `NOTICE` reads `DISCLOSURE`
  and is still not a grant body; the shelves record it as `STATED`-not-`BODIED`
  (`p210` / `P214-2`). `resolve_mit_plus` speaks only about MIT bodies and returns
  `NOT-MIT-BODY` for it.
- **`TRANSITION` does not say which side you are on.** It says the grant changed on
  a date. Which licence governs a given copy depends on when that copy was obtained —
  a due-diligence question, not a verdict.
- `NARROWING` at `0` in this harvest is **not** evidence that added clauses are rare.
  It is one harvest, and the vocabulary is `p1054`'s finite list.

## Run it

```sh
cd compose/code/p242-grant-delta && python3 test_grant_delta.py   # 23 controls
python3 -I compose/code/p242-grant-delta/test_grant_delta.py      # from the repo root
```

Wired into `make hooks` (offline, no egress) alongside `p1054` and `p241`.
