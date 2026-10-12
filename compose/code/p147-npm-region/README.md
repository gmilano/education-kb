---
industry: education
region: Global
updated: 2026-10-12
---

# p147-npm-region — `ACTION EK` discharged: 2 of 8 npm rows ARE placeable

`T59` found that **16 of 35** traversing instruments read only `git ls-tree`/`ls-files`, and
that **the entire region-placement lane is among them** — so this shelf's 8 npm rows were
called *structurally unplaceable on the region axis*.

> 🔴 **`ACTION EK`** — can any npm row be region-placed by **non-git** evidence?

    python3 npm_region.py <extracted-package-root>...
    python3 test_npm_region.py          # 15 tests, authored fixtures, offline

## 🟢 Result — `T59` is too strong and is NARROWED

| row | region | host | evidence |
|---|---|---|---|
| 🟢 **`eth-moodle-mcp@1.3.3`** | 🟢 **EMEA** | `moodle-app2.let.ethz.ch` | **strong** |
| 🟡 **`mcp-canvas-lms@1.0.5`** | 🟡 **APAC** | `canvas.ust.hk` | **a lead** |
| `@imazhar101/mcp-canvas-server`, `@ink-waffle/moodle-mcp`, `@n35da/brightspace-mcp`, `@owen-x-tech/canvas-mcp`, `canvas-mcp-server`, `moodle-mcp-server-aql` | 🔴 `UNPLACED` | — | none |

🔵 **The instrument lane is git-only; the evidence is not.** `P144-V` already settled the
rule — *"the institution is where it deploys; the author is wherever they were sitting"* —
and that rule needs no history, only the shipped payload.

### 🟢 Why ETH Zürich is strong and HKUST is a lead

🟢 **`eth-moodle-mcp` commits ETH Zürich as its `MOODLE_URL` DEFAULT** (`README.md:76`), and
its token instructions name **`YOUR_NETHZ_USERNAME`** and **`YOUR_AAI_PASSWORD`** — *nethz*
is ETH's account system and *AAI* is **SWITCHaai**, the Swiss academic federation. 🔵 **Two
independent Swiss-specific signals, one of them the shipped default.** → **EMEA
(Switzerland).**

🟡 **`mcp-canvas-lms` names `canvas.ust.hk` as an `e.g.`** (`README.md:37`) — HKUST, a real
institution, but an illustrative value and not a committed default. 🔵 **Authorial evidence
of the intended deployment, one grade weaker.** → **APAC (Hong Kong).** 🔴 **The probe's
`channel` column cannot express default-vs-example; that distinction is made here by hand
and is a stated limit.**

## 🔴 Three false positives, found before publication

| round | host | where | why it looked real |
|---|---|---|---|
| 1 | `moodle.example.edu` | `data/user-field-schema.example.json` | a real-looking `.edu` |
| 1 | `d2l.myschool.edu` | `config.example.json` | same |
| 2 | `moodle.your-university.edu` | `README.md` | **hyphenated** placeholder label |

🔴 **All three failed in the reassuring direction** — a placement looks like progress on the
axis this shelf calls its weakest. 🟢 **The vocabulary is now token-based and splits on `-`
as well as `.`**, and each of the three is pinned as a test.

## 🆕 `T67` — a bare `.edu` is not a country signal

🔴 **EDUCAUSE restricted `.edu` to US institutions in 2001 and grandfathered the non-US
registrations already held**, so the suffix carries a registration date rather than a
country. 🔴 **This shelf holds the counterexample and placed it the other way**: `P144-V`
placed `ruud0/aula-virtual-mcp` as **EMEA (Spain)** on `aula-virtual.unav.edu` —
Universidad de Navarra, Pamplona.

🟢 **So `.edu` is demoted to a lead**, reported with its own weak `how`, and the known
grandfathered domains are refused outright. 🔴 **That list cannot be complete** — it holds
the ones this shelf has met. 🟢 **A test asserts this probe agrees with `P144-V` rather than
contradicting it.**

🔵 **Generic suffixes are absent by design.** `.io`, `.ai`, `.co`, `.me`, `.dev` are sold
worldwide and place nothing. 🟢 **A row with no national evidence returns `UNPLACED`, which
is an answer; `Global` would be a claim.**
