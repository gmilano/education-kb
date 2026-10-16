# `p240-grant-language` — the axis `239` passes of grant reading never recorded

**Why this exists.** `p228`–`p239` spent twelve passes establishing that a licence must be
**read first-hand** from `raw.githubusercontent.com` rather than taken from the GitHub API
field. That instrument is sound, and `p240` ran it over `40` repositories. What none of
those passes recorded is the **language** of the payload it read.

🔴 **Measured on `p240`'s own `35` first-hand grant reads:**

| | payloads |
|---|---|
| Latin-script | 🟢 `34` *(MIT / Apache / GPL / AGPL template texts, `511`–`35 149` B)* |
| **non-English** | 🔴 **`1`** |

The one is [`heronerar/OpenGaokao`](https://github.com/heronerar/OpenGaokao) — `LICENSE`,
`15 992` B, `main` · `a75b65aaa494`, **`4 466` of `4 807` letters CJK (`92.9`%)**. Its
first operative clause is **禁止商业使用** — *commercial use is prohibited* — and the
payload states in its own text that it is **not an OSI-approved licence**.

🔴 **`lib/license_family.sh` before `p240`: `commercial_use_ok` → `ALLOWED`.**

## The defect, and why it is not a typo

`commercial_use_ok` ends in a token match, and **every token in it was English**:
`non-commercial`, `noncommercial`, `not-for-profit`, `obtain a commercial license`. A
payload that prohibits commercial use in Chinese returned the same verdict as one that
grants it.

🔵 **This is `P312`'s shape in another language.** `P312` found `CC-BY-NC` — a family whose
*name* says NonCommercial — returning `ALLOWED` because the family gate short-circuited the
token match. 🟡 Here the family gate correctly declines (`UNCLASSIFIED`, since the licence
is bespoke) and hands the payload to the token match, **which cannot read it**.

🟡 **And it is the same shape as this pass's other two findings:** the control was adequate
for the shelf that existed. The supply channel was anglophone until `p239` recorded that
EMEA, APAC and LATAM were **not measured**; `ACTION VJ` sent `p240` to measure them, and
measuring them produced the first non-English payload these shelves have ever read.

## Why the token list is not the fix

`p240` did extend the list — `zh`, `ja`, `ko`, `es`, `pt`, `fr`, `de`, `it`, `35` phrases
across `9` languages — and that closes this specimen. 🔴 **But a token list is a closed
vocabulary over an open world.** The next restriction arrives in a language the list does
not carry, and it is **invisible** rather than wrong.

🟢 **So this instrument asks the other question, and answers it with no vocabulary at all:**

> is this payload in a script the token match cannot be trusted over?

| verdict | meaning |
|---|---|
| `LATIN-SCRIPT` | 🟢 the English/Latin token match applies; nothing to add |
| `NON-ENGLISH-GRANT-RESTRICTED` | 🔴 non-Latin **and** a known restriction phrase fires |
| `NON-ENGLISH-GRANT-UNREAD` | 🔴 non-Latin and **no** known phrase fires — **a refusal to clear**, not a verdict of permissive |

🔵 **`UNREAD` is the whole point.** It converts a silent `ALLOWED` into an explicit *"no
vocabulary this KB owns has read this grant"*. An unread grant stops being
indistinguishable from a permissive one.

## Thresholds, and what sets them

`NON_LATIN_PCT = 20.0`, measured over **letters**, never bytes — a UTF-8 byte count
inflates every non-Latin script by 2–3× and would make the threshold a function of the
encoding. 🟡 **Separation measured on this pass's `35`: the one non-English payload sits at
`92.9`% and the next highest at `0.0`%, so the interval `(0, 92.9)` is UNMEASURED** and is
stated as such rather than implied to be calibrated.

`20.0` is set low deliberately, because this gate's error cost is asymmetric: a false
`UNREAD` costs one human read; a false `CLEAR` costs the deliverable.

## A measurement that justifies the family gate

Run over the same `35` payloads, the restriction tokens alone fire on **`15`** of them —
`en:noncommercial` — because the body of `GPL-3.0` contains the word. 🟢 **None of the `15`
changes verdict**, because `commercial_use_ok` consults the FAMILY first and only an
unidentifiable family reaches the token match. 🔵 **The token list would be a bad gate on
its own; it is a usable last resort behind a family gate. Both measurements are from this
pass's own payloads.**

## Usage

```bash
python3 -I compose/code/p240-grant-language/grant_language.py <payload-path>
python3 -I compose/code/p240-grant-language/grant_language.py --reach   # the vocabulary
python3 -I compose/code/p240-grant-language/test_grant_language.py      # 29 controls
make gate-offline                                                       # standing check
```

Exit `0` when the payload is clearable without a human read of a foreign text, `1`
otherwise. No network. Runs from its own directory and under `-I` from the repository root
(`p355-cwd-portability`).

## What it does not do

🔴 It cannot translate. `RESTRICTED` and `UNREAD` both mean *a human must read this*; only
the first one says what to look for. 🔴 It classifies **script**, not language, so Latin-script
Turkish, Vietnamese or Polish restrictions pass as `LATIN-SCRIPT` and are caught only if the
token list carries them. 🟡 **`ACTION VP`: a Latin-script non-English grant is the hole this
gate does not cover, and it is the likelier next specimen, not the rarer one.**
