## `2026-11-19` (p927) — **The topic index's floor moved from 601 to 2,298, and fifteen legs reported more than the page cap can return. This file has been recording a backlog it has never once measured to the bottom.**

### 🟢 What changed since `p926`

`p926` opened thirteen unasked topic words, returned **601 unheld** repositories and wrote
`926-R1`: *a discovery channel is exhausted only against the vocabulary it was asked with.* `p927`
asked **35 more words neither `p925` nor `p926` used** — `student-management`, `ai-tutor`,
`study-tools`, `scorm`, `lti`, `xapi`, `open-badges`, `proctoring`, `plagiarism-detection`,
`gradebook`, `autograding`, `learning-analytics`, `serious-games`, `pedagogy`, `lesson-plan`,
`question-generation`, `literacy`, `math-education`, `stem-education`, `virtual-classroom`,
`canvas-lms`, `openedx`, `moodle`, and twelve more.

**Result: 3,000 unique repositories, 2,298 of them unheld** against the **8,432** slugs this base
has ever named. Full yields in `evidence/topic-vocabulary-yield.2026-11-19-p927.tsv`; the backlog
itself in `evidence/unheld-backlog.2026-11-19-p927.tsv`. The leg table is in `agents/trending.md`
`927-F1`.

### 🔴 The number this file most needs: 2,298 unheld is a **floor**, not a measurement

Fifteen of the 35 legs report a `total_count` larger than the 100-row page this base fetches:

| Leg | `total_count` | Rows this base actually saw |
|---|---|---|
| `topic:student-management` | **1,651** | 100 |
| `topic:ai-tutor` | **986** | 100 |
| `topic:study-tools` | **817** | 100 |
| `topic:canvas-lms` | **505** | 100 |
| `topic:tutoring` | **499** | 100 |
| `topic:learning-analytics` | **424** | 100 |
| `topic:plagiarism-detection` | **407** | 100 |
| `topic:grading` | **305** | 100 |
| `topic:xapi` | **284** | 100 |
| `topic:stem-education` | **275** | 100 |
| `topic:pedagogy` | **272** | 100 |
| `topic:scorm` | **247** | 100 |
| `topic:question-generation` | **241** | 100 |
| `topic:lti` / `topic:moodle` | **190** each | 100 each |
| `topic:proctoring` | **176** | 100 |

🔵 **`927-R1`.** Every sentence this file has written about what the topic channel contains has been
a sentence about a 100-row page. **Until a pass shards these legs by star band or paginates them,
no number in this file is a supply measurement** — including 2,298. That is the honest reading and
it is the single most important line in this section.

### 🔴 The usable fraction reproduces at 5.9%

| Filter | Rows remaining |
|---|---|
| unheld, from 35 topic legs | **2,298** |
| permissive grant (MIT / Apache-2.0 / BSD / ISC / MPL-2.0 / Unlicense / 0BSD) | 924 |
| **and** pushed since 2026-05-01, not archived | 409 |
| **and** AI / agent / LLM / tutor / grading signal | 182 |
| **and** not a reading list, solution dump, cheat sheet or course-notes repo | 🟢 **136** |

`p926` measured **8.8%** on a different vocabulary; `p927` measures **5.9%**. 🔵 Two independent leg
lists landing within a few points of each other is the first evidence this file has that the
*filter*, not the leg list, is the stable instrument.

**And the star-sorted head is again not education software** — `TheAlgorithms/C-Plus-Plus`
(34,894 ★), `goplus/xgo` (9,493 ★, a programming language), `online-ml/river` (6,151 ★, online ML),
`raiyanyahya/how-to-train-your-gpt` (4,183 ★), `bkerler/exploit_me` (1,118 ★, an **ARM exploitation
CTF**), `ShreyamMaity/student-offers` (774 ★, a list of student discounts). `926-F2`'s rule
reproduces exactly: **filter before sorting.**

### 🟢 Repositories promoted out of this file's backlog this pass

Eleven went to `repos/foundations.md`, three to `verticals/solutions.md`, twenty to `agents/top.md`.
All grants byte-read 2026-11-19, **36 probed / 36 resolved / 0 404s**
(`evidence/grant-byte-read.2026-11-19-p927.tsv`). The ones that change what this base can build:

| Repo | Grant (byte-read) | ★ | Why it moved off the shelf |
|---|---|---|---|
| https://github.com/parthdhanani/scorm-kit | **MIT** `1,070 B` | 2 | SCORM 1.2 packaging, validation and runtime — the one delivery form indifferent to which LMS the client runs |
| https://github.com/parthdhanani/storycraft | **MIT** `1,070 B` | 1 | Markdown storyboard → SCORM 1.2 compiler; identical grant hash to `scorm-kit` |
| https://github.com/wonmortech/sanad | **Apache-2.0** `11,337 B` | 0 | Verifiable certificates and badges under **W3C Verifiable Credentials 2.0** |
| https://github.com/parler-haut-interagir-librement/open-badges-bundle | **MIT** `1,155 B` | 0 | Open Badges issuance with published issuer profile, keys and revocation (Symfony) |
| https://github.com/openpatch/bitflow | **MIT** `1,069 B` | 44 | Dynamic flow-based assessment library, maintained since 2021 |
| https://github.com/mrlvsb/kelvin | **MIT** `1,063 B` | 35 | VŠB–TU Ostrava's production code examinator, maintained since 2020 |
| https://github.com/artevelde-uas/canvas-lms-app | 🟢 **ISC** `771 B` | 12 | A university's permissive branding layer on an **AGPL** LMS — `T17` in production |
| https://github.com/jonsorr/D2L_Brightspace_APIs | **MIT** `1,074 B` | 2 | **First Brightspace row in this base.** The fourth major LMS had no row anywhere |
| https://github.com/missing-elements/h5p-toolkit | **MIT** `1,073 B` | 10 | Plays `.h5p` offline with **no H5P server** — H5P without the platform dependency |
| https://github.com/10kH/MisconceptDialogue | **MIT** `1,129 B` | 1 | **AACL-IJCNLP 2026** artefact: *Evaluation Criteria Shape Measured Success in LLM Math Tutoring* |
| https://github.com/uemanet/harpia | **MIT** `1,063 B` | 28 | A **Brazilian state university's** academic system, open since 2017 — see `927-F5` |

### 🔴 One correction this file owes `p926`

`926-G2` measured eleven Spanish- and Portuguese-language rows in its backlog and found **none
permissively licensed**. This pass's backlog contains **MIT-licensed LATAM rows, byte-read** —
`uemanet/harpia`, `DerickxP/Learn-Quest-Serious-Game`, `alberto2005-coder/detector-ia`,
`Gehiner/KodlandFaster`. 🔵 The finding was true of eleven rows from one leg list and was published
as a fact about a region. **It is the same failure `926-R1` names, one level up**, and it is
recorded in full as `927-F5` in `agents/trending.md`.

---

