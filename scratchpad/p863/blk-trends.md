## 🟢 `2026-11-17` — sixty-eighth pass (`p863`) — **`6` trends (`T226`–`T231`): a thin yield that turned out to be a property of ONE language and not of the method, a third defect class in query vocabulary, two incompatible kinds of licence refusal, and the first measured RETREAT from a national AI-education deployment**

**Two hundred and twenty-three** trends — derived trends: **223** (`217` + `6`).

## 🟢 `T226` — a yield rate is not a finding until it is measured where it should NOT hold

🔴 **For three passes this base has been narrowing toward a conclusion: the open supply around
national examinations is thin outside English.** `p862` measured the Portuguese tier; `p863` ran
the nine Hispanic terms `862-G2` named and got **`2,142` addresses → `2` usable**. 🔴 **That is
`0.09%`, and it would have shipped as "non-English examination corpora are thin".**

🟢 **`p798-G` says: when a finding is a RATE, measure it somewhere it should not hold.** 🟢 **The
same instrument, same hour, pointed at Vietnamese:**

| Leg | Terms | Addresses | `stars:>5` | On topic | 🟢 Permissive |
|---|---|---|---|---|---|
| 🔴 Hispanic LATAM | `9` | `2,142` | `11` | `5` | 🔴 **`2`** |
| 🟢 **Vietnamese** (`"trắc nghiệm"`) | **`1`** | `1,170` | `7` | 🟢 **`7` of `7`** | 🟢 **`3`** |
| 🔴 Indian (`NCERT`, `CBSE`) | `2` | `2,257` | `18` | `18` | 🔴 **`0`** |

🔵 **One Vietnamese term out-yielded nine Hispanic terms on permissive supply, and did it with
`0` false friends.** 🟢 **So the thin yield is not a property of non-English querying, not of the
examination vein, and not of the method — it is a property of Spanish-language GitHub
specifically.** 🔴 **Three passes of narrative were one control away from being wrong, and the
control cost two minutes.**

## 🔴 `T227` — the national-examination ACRONYM is a third defect class, and no exclusion repairs it

🟢 This base has now catalogued three distinct ways a query term fails:

| Class | Example | Why it fails | Repair |
|---|---|---|---|
| **Stem collision** (`p861`) | `grading` → `grade` | shares a ROOT with a common adjective | 🟢 `NOT` on the root, or a precise synonym (`autograding`) |
| **Cross-language homograph** (`T219`) | `rúbrica`, `banca` | shares SPELLING across two languages | 🔴 no term to exclude — abandon the word, query the phrase |
| 🆕 **Acronym namespace collision** (`T227`) | `EXANI`, `"Saber Pro"`, `PAES` | the acronym is also a HARDWARE, GAME or LIBRARY name | 🔴 **no repair at all** |

🔴 **The evidence is total, not partial.** `EXANI` (`217`) → Cisco **ExaNIC** network cards
(`206★`), an *Exanima* game map, an *Exanite* action-RPG. `"Saber Pro"` (`431`) → a **Beat
Saber** mod, a Chinese *Saber* UI frontend, `ecomfe/saber-promise`. 🔴 **`0` of those `6`
top-band addresses is an examination artefact.**

🟢 **The two Hispanic terms that DID work are an institution name (`Ceneval` → `2` of `2` on
topic) and a natural-language phrase (`"examen de admisión"` → `1` of `1`).** 🔵 **Rule: never
query a national examination by its acronym. Query the ISSUING BODY or the phrase a candidate
would type.** 🔴 **This is strictly worse than the other two classes: a stem collision loses
precision, a homograph loses a word, but an acronym collision returns a FULL top band of confident
wrong answers — the failure mode that looks most like success.**

## 🔴 `T228` — two independent implementations of one national format make the FORMAT the asset

🟢 Vietnam's `"trắc nghiệm"` tier has three permissive members built by unrelated authors —
[`meesudzu/trac-nghiem-online`](https://github.com/meesudzu/trac-nghiem-online) (`80★`),
[`Belikhun/thi-trac-nghiem`](https://github.com/Belikhun/thi-trac-nghiem) (`6★`),
[`tamht298/final-project`](https://github.com/tamht298/final-project) (`12★`) — 🔵 **all
implementing the same national multiple-choice examination shape, none depending on another.**

🟢 **Convergence by unrelated authors is evidence about the SPECIFICATION, not about any
repository.** 🔵 **This base saw the same signal in Brazil**, where *"a dozen projects have
converged on the same five published ENEM competencies"* made the specification free while no code
was adoptable (`T188`). 🔴 **The difference is that Vietnam's convergence is ALSO granted** — 🟢
so here the format and an implementation of it are both takeable, which is the first time both
halves have been available in the same vein.

## 🔴 `T229` — a CONTENT licence and a CODE licence answer different questions, and a row needs both

🟢 [`picuino/test`](https://github.com/picuino/test) byte-reads as **`CC-BY-SA-4.0`**
(`20,127 B`, `sha256₁₂ 0f1985dd14bf`) and ships **a question bank AND a web page to view it**.
🔴 **`CC-BY-SA-4.0` is a content licence: it governs the questions and says nothing coherent about
the viewer's source.**

🔵 **The practical consequence is asymmetric and easy to get backwards.** 🟢 **Share-alike binds
DERIVED ITEMS** — an item bank built from these must be redistributed on the same terms, which is
fine for a public bank and wrong for a proprietary item library. 🔴 **Meanwhile the viewer code
is effectively ungranted**, because a content licence is not a patent or software grant.
🟢 **Rule: when a row's payload is CONTENT, record the content grant and the code grant
separately — this base's shelf format has one licence column and that column is not enough for
this row class.** 🔵 Logged as an instrument limitation, not only as a trend → `863-G4`.

## 🔴 `T230` — ORIGINAL-work refusals and REDISTRIBUTION refusals need opposite remedies

🔴 **Two licence refusals that look identical in a `NONE` field are not the same problem.**

| | Brazil / Hispanic LATAM | 🆕 India |
|---|---|---|
| What is ungranted | artefacts the uploader **wrote** | ministry textbooks the uploader **mirrors** |
| Examples | `Quest-API` (`1M+` items), `questoes-aqui`, `repaso-ceneval` | `utsingh/upsc` (`69★`), `nit-in/download_ncert_books`, `ncert-downloader` |
| Scale this pass | `3` of `5` on-topic Hispanic rows | 🔴 **`0` of `18` permissive across `2,257` addresses** |
| 🟢 **Remedy** | 🟢 **a licence request to the uploader can fix it** — the rights are theirs | 🔴 **a licence request is worthless** — the uploader has no rights to grant |

🔵 **India's estate is the largest education corpus this base has ever indexed and the least
usable, and the reason is upstream copyright, not uploader neglect.** 🟢 **The only path is
NCERT's own terms.** 🔴 **This base's [`licence-requests`](licence-requests/) workflow must
therefore record WHICH class a refusal is in, or it will generate requests that cannot
succeed** → `863-G4`.

## 🔴 `T231` — the first measured RETREAT from a national AI-education deployment

🟢 **South Korea's AI digital-textbook adoption fell `37%` → `19%` in a single semester, and the
software was legally reclassified from *textbook* to *educational material*.** 🟢 The ministry has
moved to `16` teacher-authored AI subjects instead.

🔵 **Every national datum this base holds has, until now, pointed one way: more mandate, more
scope, earlier dates.** 🔴 **Korea is the first reversal, and it reversed at the point of
CLASSROOM adoption rather than at the policy level — the policy survived, the deployment did
not.** 🟢 **The replacement is instructive: teacher-authored subjects rather than vendor-supplied
software.**

🔵 **Read against Singapore's stated fear of *"cognitive offloading"*, Japan's deliberate slowness
(official digital textbooks as late as `2030`), and the global `38%` → `68%` jump in
AI-DETECTION use, a consistent picture appears** — 🟢 **institutions are buying CONTROL over AI
faster than they are buying INSTRUCTION from it.** 🔴 **A pitch built on instructional upside is
selling against the measured direction of the market.**

---

