# `ACTION p288` — the third channel

`p278` grades a row by reading **two** channels: the licence **payload** and the package
**manifest**. The **README is not one of them**. For a row whose payload is absent and whose
manifest declares nothing, `p278/sweep.sh` therefore returns

```
NO-CHANNEL   GREY   "neither channel read — this row carries no grade"
```

## What made the cost visible

Pass 288's population is six new rows. **Five** have no payload and no manifest declaration,
so all five graded `NO-CHANNEL/GREY`. For **two** of them a third channel was readable on the
resolved ref and said something decisive — **in opposite directions**:

| slug | README | what it says | correct verdict |
|---|---|---|---|
| `anastasasenov/bbmcps` | `readme.md`, 1 582 B, line 84 | *"This project is open-source and available under the MIT License."* Tree is **9 files**, `NONE_IN_TREE` | `DANGLING-CLAIM` → **ASK** |
| `hdronamraju/sped-agent` | `README.md`, 12 689 B, line 53 | *"© 2026 hdronamraju. All rights reserved. … please ask before reusing the code."* | `RESERVED-NO-PAYLOAD` → **STOP** |

One is a grant **claimed and not served**; the other is a grant **refused**. `GREY` is the
wrong word for both, and it is the *same* wrong word for both — which is the real defect.

## The lowercase rung

`bbmcps` serves **`readme.md`**, not `README.md`, and answers **404** at the uppercase
spelling on `main`, `master` *and* `HEAD`. This pass's own first reading of it was the false
absence *"no README on any ref"*. The claim was recovered only because the **tree** was
enumerated and showed the real spelling — `p261`'s rule again: a 404 cannot distinguish a
missing path from a missing channel, but a tree can.

🔵 `T-p283`'s shape for the **fourth** time: **the class reached one instrument and never
reached the one beside it.** `pass262-scoped-reservation-audit/sweep.py` already fetches the
README over five spellings *including* lowercase `readme.md` — but it runs only over slugs the
shelves **already** grade `RESTRICTIVE-GRADE`, so a *new* row can never reach it. The reach
existed in this codebase; the gate that grades new rows did not have it.

Not every `CASE-UNVARIED` readme ladder is a defect: `p283`'s audit flags the one in
`p279-absence-claims`, and that one is **harmless**, because it opens *this KB's own*
`README.md` at a known local path. This one was not harmless. The audit measures the shape;
whether the shape costs anything depends on whether the path is remote.

## Files

| file | what it is |
|---|---|
| `readme_claim.py` | **offline.** `readme_claim(text)` → `RESERVATION` / `CLAIM:<family>` / `NO-CLAIM`; `channel_verdict(claim, payload_family)` → the eight verdicts; `posture(verdict)` → `BUILD-ON` / `ASK` / `STOP`. Also `README_PATHS`, the printable ladder (T272). |
| `test_readme_claim.py` | **32 controls**, in `make hooks`. Controls 1–4 are this pass's four real fixtures, quoted verbatim. |
| `probe.sh` | **online.** Resolves the ref with `ls-remote --symref`, walks the ladder to the first 200, records path/bytes/claim. No classifier (P237). |

## Collision, measured before the anchors were trusted

A family name alone is **not** a grant claim, so both arms are anchored on an assertion verb
and the institution names are stripped first. The controls that forced this:

- **`MIT RAISE`** — appeared in this pass's *own* North America search leg. An institution.
- `MIT Media Lab`, `MIT OpenCourseWare` — the same shape, and both are entirely ordinary in an
  *education* README specifically, which is why this base needs the guard more than most.
- `See LICENSE for details.` — a **pointer**, not a claim. The payload channel answers that.
- `ui/node_modules/react/LICENSE` — `p280`'s vendored class, which must not reach a verdict
  through the README either.

A **reservation outranks** any family token in the same body: a README that says *"Available
under the MIT License"* and *"All rights reserved"* grades `RESERVATION`, because the refusal
is the sentence the studio has to obey.

## The gap a control in this suite found

The first version matched only the **prefix** form (*"licensed under the MIT License"*). Its
own control `conflict/AIProf` failed, because `p287`'s `MeetYourAI/AIProf` writes the claim
as **`This project is [MIT](./LICENSE) licensed.`** — family **first**, verb **second**, and
the family token wrapped in a markdown link. A claim this base has already published a
correction about is the last one that should go ungraded, so a second arm and a markdown-link
reduction were added, and `collision/postfix-institution` pins the strip-before-match order.
