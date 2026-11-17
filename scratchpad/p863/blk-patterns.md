## 🟢 Sixty-eighth pass (`p863`, 2026-11-17) — **`P100`–`P101`: one recipe built on a mandate with a published date and a corpus that already exists, and one built on the honest finding that its region's corpus does NOT**

**Ninety-nine** concrete recipes — derived recipes: **99** (`97` + `2`).

🟢 **Every component named below was byte-read on `2026-11-17` from a blobless partial clone, and
the grant beside it is what its own licence file says** —
[`byte-read-grants`](../evidence/byte-read-grants.2026-11-17-p863.tsv). 🔴 **Each recipe states
where the copyleft boundary runs, because in both veins the standards bridge is GPL and the
payload is not.**

---

## 🟢 P100 — *Vietnam upper-secondary AI content, delivered on the mandate's own timetable*

🔵 **The engagement this answers**: Vietnam's MoET issued **Decision `2422/QĐ-BGDĐT` on
`18 August 2026`** — a framework for AI education content in upper-secondary schools, **nationwide
from the `2026–27` school year**, core component **`12` periods per grade per year**. 🔴 **Every
`THPT` school in the country now has contact hours to fill, on a published date, and no national
item bank shipped with the decision.** 🟢 **The open Vietnamese assessment corpus is already three
implementations deep and permissively granted** (`T226`, `T228`).

**Components:**

| Component | Grant, byte-read `2026-11-17` | Role in the build |
|---|---|---|
| [`meesudzu/trac-nghiem-online`](https://github.com/meesudzu/trac-nghiem-online) `80★` | 🟢 **MIT** — `1,068 B`, `sha256₁₂ a44234cb37ea` | 🟢 **Fork as the delivery base.** Already built for `THCS`/`THPT` — Vietnamese school structure, Vietnamese item format, Vietnamese UI. 🔵 The localisation is the part that would cost the most and it is done |
| [`Belikhun/thi-trac-nghiem`](https://github.com/Belikhun/thi-trac-nghiem) `6★` | 🟢 **MIT** — `1,064 B`, `sha256₁₂ 93d0402524c0` | 🟢 **Read, do not merge.** An independent implementation of the same national format — 🔵 **use it to separate what is the FORMAT from what is one author's choice** (`T228`). Where the two agree, that is the national spec |
| [`tamht298/final-project`](https://github.com/tamht298/final-project) `12★` | 🟢 **MIT** — `1,066 B`, `sha256₁₂ 89599f2cdf16` | 🟡 **Third reference point only.** `HEAD 2021-01-12`, a university capstone — 🔵 its value is that it is a third independent agreement on the format, not that it is code worth taking |
| [`shevandrin/rqti`](https://github.com/shevandrin/rqti) `9★` | 🔴 **GPL-3.0** — `34,904 B`, `sha256₁₂ 585e25ef8f59` | 🔴 **AUTHORING-TIME ONLY.** Generates **QTI** from R. 🟢 **The boundary is clean because QTI output is DATA, not a derivative work** — run it in the content pipeline, never link it into delivered product code |

**Wiring:**

1. 🟢 **Fork `trac-nghiem-online`.** Diff it against `thi-trac-nghiem` before changing anything;
   treat the intersection as the national format and everything else as a local choice.
2. 🟢 **Author the `12`-periods-per-grade item set in `r-exams`/`rqti`, emit QTI.** 🔵 **One item
   source, many targets** — QTI is ingested by Moodle, Open edX, Canvas, ILIAS and OpenOLAT, all
   already on [`verticals/solutions.md`](../verticals/solutions.md).
3. 🔴 **Keep the GPL boundary at the pipeline edge**: `rqti` runs in authoring and produces QTI
   files; the forked MIT delivery app only ever reads those files.
4. 🟢 **Ship the item bank as the deliverable, the fork as the reference deployment.** 🔵 Schools
   that already run an LMS take the QTI; schools that do not take the fork.

🔴 **What this recipe does NOT claim.** `HEAD 2025-02-09` on the lead component — 🟢 **it is
stable, not maintained**, so the fork is the delivery vehicle and upstream is not a dependency to
plan patches against. 🔴 **And `"hệ thống quản lý học tập"` returns `0` repositories above five
stars**: 🟢 **Vietnam builds assessment in the open and buys its LMS, so do not propose replacing
the LMS.**

---

## 🟢 P101 — *A Hispanic-LATAM item programme that starts by admitting the corpus is two repositories*

🔵 **The engagement this answers**: a LATAM institution or ministry in a region with **`193` IDB-
reviewed AI initiatives**, `59%` of them generative — 🔴 **and a measured open supply of `2`
permissively granted national-examination repositories across `2,142` addresses** (`T226`).
🟢 **This recipe is built so phase one produces value without the corpus, because the corpus does
not exist yet.**

**Components:**

| Component | Grant, byte-read `2026-11-17` | Role in the build |
|---|---|---|
| [`alvaretto/r-exams_matematicas`](https://github.com/alvaretto/r-exams_matematicas) `8★` | 🟢 **MIT** — `1,078 B`, `sha256₁₂ 67a6e5e5a2af` | 🟢 **The seed item set and, more importantly, the AUTHORING CONVENTION.** Colombian SABER ICFES single-answer items written in `r-exams` — 🔵 **re-targetable to PDF, Moodle XML, QTI and Blackboard from one source** |
| [`shevandrin/rqti`](https://github.com/shevandrin/rqti) `9★` | 🔴 **GPL-3.0** — `34,904 B`, `sha256₁₂ 585e25ef8f59` | 🔴 **Authoring-time only**, same boundary as `P100`: emits QTI, never linked into product |
| [`agn3si/ResultadosUNAM---data`](https://github.com/agn3si/ResultadosUNAM---data) `6★` | 🟢 **MIT** — `1,063 B`, `sha256₁₂ 13e4dd489fe9` | 🟢 **Six admission cycles (`2021`–`2026`) of UNAM outcome data** — 🔵 **the only LONGITUDINAL admissions set in this base.** Phase-one deliverable: admissions yield and equity analysis, which needs no item bank at all |
| [`picuino/test`](https://github.com/picuino/test) `7★` | 🔴 **CC-BY-SA-4.0 — CONTENT, share-alike** — `20,127 B`, `sha256₁₂ 0f1985dd14bf` | 🟡 **Optional, and only for a PUBLIC bank.** 🔴 Share-alike binds derived items (`T229`) — 🟢 fine for a ministry item bank, wrong for a proprietary one. 🔴 Its viewer code is effectively ungranted; take the items, not the app |

**Wiring:**

1. 🟢 **Deliver the admissions analysis FIRST**, off `ResultadosUNAM---data` alone. 🔵 **It is
   permissive, longitudinal and needs no items** — a result in weeks while the licence position is
   still being resolved.
2. 🟢 **Stand up `r-exams` + `rqti` as the authoring convention**, seeded with the Colombian
   items. 🔵 **The convention is the asset**: every item authored afterwards is multi-target from
   day one.
3. 🔴 **Run a licence-request campaign as a named work package, and CLASSIFY each target first**
   (`T230`): 🟢 **Brazilian and Hispanic targets are ORIGINAL work — the uploader can grant**, so
   [`gontijogabriel/Quest-API`](https://github.com/gontijogabriel/Quest-API) (`1M+` items),
   [`rodrigoborgesmachado/questoes-aqui`](https://github.com/rodrigoborgesmachado/questoes-aqui),
   [`jmtoral/admisiones_unam`](https://github.com/jmtoral/admisiones_unam) and
   [`alejandroRdzGarza/repaso-ceneval`](https://github.com/alejandroRdzGarza/repaso-ceneval) are
   worth asking. 🔴 **Do NOT spend the campaign on Indian mirrors — the uploader has no rights to
   grant** (`T230`).
4. 🟢 **Author net-new items into the convention** for whatever the campaign does not return.
   🔵 **Price this honestly**: the measured supply is `2` repositories, so item authoring is a
   line in the budget, not a search result.

🔴 **The failure mode this recipe is shaped to avoid.** 🔵 **A LATAM proposal that promises to
"build on the open corpus" will discover in week three that `60%` of the on-topic addresses above
five stars carry no grant at any path** (`3` of `5` this pass, against `p862`'s `46%`). 🟢 **Lead
with the admissions analysis, treat items as authored work, and the engagement does not depend on
a licence answer arriving.**

---

