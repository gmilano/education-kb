# `p241-blanket-denial` — the axis `p240` diagnosed one language short

**Pass 241 · 2026-10-16 · 104/104 controls · every fixture a payload read first-hand**

## What it detects

A grant payload that **reserves rights and grants nothing** — detected without knowing
how its author chose to phrase the refusal.

## Why it exists

`p240`, nine hours earlier on the same date, found `commercial_use_ok` returning
**ALLOWED** on [`heronerar/OpenGaokao`](https://github.com/heronerar/OpenGaokao), whose
first operative clause is 禁止商业使用 — *commercial use is prohibited*. It read the
defect as **language** and fixed it with `35` restriction phrases across `9` languages,
then built [`p240-grant-language`](../p240-grant-language/) to refuse to clear a payload
written in a script the token match cannot read. That was right, and it holds.

🔴 **`p241` measured the same function on two payloads written in ENGLISH, and it returned
ALLOWED on both.** Both were read first-hand from this pass's `topic:ferpa` harvest:

| slug | bytes | ref · head | the operative clause |
|---|---|---|---|
| `Samielakkad/AI-EdTech-Sovereign-School-OS` | `688` | `main` · `520bbd2e806f` | *"**NO PERMISSION is granted** to use, copy, modify, merge, publish, distribute, sublicense, sell, train machine-learning models on, or create derivative works from any part of this repository — for personal, academic, or **commercial** purposes"* |
| `snflwr-ai/snflwr.ai` | `2 833` | `main` · `7feea47e4759` | *"snflwr.ai — **Proprietary Software License** / All rights reserved."* |

Neither contains `non-commercial`, `noncommercial`, `not-for-profit` or `obtain a
commercial license`. The first uses the word *commercial* **inside a denial**; the token
list only knows it inside the compound. The second never uses it at all.

🔴 **And `p240-grant-language` returns `LATIN-SCRIPT` on both** — it affirmatively
certifies that *"the English/Latin token match applies"*, on the two payloads that
defeat the English/Latin token match.

> **So the defect class is not the language of the restriction. It is that every one of
> these matchers enumerates ways of saying "restricted" and treats the absence of its own
> vocabulary as permission.** A denial it has not seen before reads as a grant.

## The predicate

It does not enumerate restrictions. It asks the question a licence exists to answer:

    DOES THIS PAYLOAD GRANT ANYTHING AT ALL?

`MIT` says *permission is hereby granted*; `BSD` says *redistribution and use … are
permitted*; `Apache-2.0` says *hereby grants*; `GPL` says *this program is free
software*. A payload that reserves rights and grants none is not an unrecognised licence
— it is a refusal, and it is detectable without reading the refusal's own wording.

| verdict | meaning |
|---|---|
| `GRANT-PRESENT` | 🟢 a grant verb is present — the token matchers may be trusted over this payload |
| `BLANKET-DENIAL` | 🔴 an explicit denial fired, **or** rights are reserved with no grant anywhere |
| `NO-GRANT-LANGUAGE` | 🔴 neither — **a refusal to clear**, never a permission |

`may_publish()` is true on `GRANT-PRESENT` alone. `NO-GRANT-LANGUAGE` is `p240`'s
`UNREAD` on the other axis: *no vocabulary this KB owns has found a grant in this
payload*, which is not the same as the payload granting something.

🔵 **The two axes are complementary, and the control that shows it is `p240`'s own
headline payload.** `OpenGaokao` is `NO-GRANT-LANGUAGE` here — refused correctly, by an
instrument that cannot read a word of Chinese.

## 🟡 The one false-positive mode, and the discriminator

`All rights reserved.` is a line in `BSD-2-Clause`, `BSD-3-Clause` and many `MIT`
headers — **followed by a grant**. A gate that convicted on it would downgrade most of
this KB's permissive estate.

So **`all rights reserved` alone never convicts.** It convicts only in the *absence* of
any grant verb. That is [`p238`](../p238-lure-signature/)'s self-host-exemption shape:
keep the cheap signal, and put a second predicate in front of the honest case.

Positive control, read first-hand: `scipy/scipy` `LICENSE.txt` (`1 531` B, `main` ·
`5363aec376a7`) carries the reserved line **and** grants — `GRANT-PRESENT`, and still
`ALLOWED` through the shared classifier.

## Where the fix landed

- `compose/code/lib/license_family.sh` — `commercial_use_ok` gained the branch, mirrored
  phrase for phrase. Gated on `UNCLASSIFIED` so no recognised family is touched.
  `217` → `238` controls.
- `holder_of` was fixed in the same pass for a sibling defect — see `ACTION TQ` below.
- `make hooks` runs this suite and, for the first time, `p1054-mit-plus-clause`.

## What the census found (`ACTION VO`)

`p240` registered: *"when a defect is found in a matcher, the discharge is a census of
every matcher in `compose/code/`, not a fix of the one that fired."*

| measurement | value |
|---|---|
| matchers deciding a **permission** question | `122` |
| of those, carrying a restriction **vocabulary** | `67` |
| of those, with a **default-permit** exit | `10` |
| 🔴 **BOTH — the defect shape** | **`7`** |
| of the `7`, in `make hooks` | 🔴 **`1`** — `lib/license_family.sh`, the shared classifier, the one that fired |

🔵 **And the census's real finding is not in that table.** This KB already owned a
correct classifier for the carve-out case — [`p1054-mit-plus-clause`](../p1054-mit-plus-clause/),
written at pass `188` — and it **was not in `make hooks`**, because its suite died under
the very invocation its own docstring prescribed (`python3 -I`, which strips the script's
directory from `sys.path` — `p355-cwd-portability`). Measured over this pass's `25`
payloads: `1` verdict-changing disagreement and `5` where the shared classifier's bare
family silently drops what `p1054` recovers. Both are fixed; both are now in the gate.

## Files

| file | what |
|---|---|
| `blanket_denial.py` | the predicate; `--reach` prints the vocabulary (`T272`) |
| `test_blanket_denial.py` | `104` controls, incl. cross-instrument agreement against the shell branch (`p637`) |
| `fixtures/` | `7` payloads, every one read first-hand at a pinned SHA |
