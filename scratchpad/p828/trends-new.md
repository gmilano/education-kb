## T99 — The LMS agent tier is not Canvas and Moodle. It is Brightspace, D2L and Blackboard, at `147` repositories against `5` shelved

🟢 **The measurement.** `p828` ran the brand axis (`T86`'s rule) against the LMS vendors this base
had NOT enumerated, on the `gh api search/repositories` channel, `2026-11-15`:

| Brand token (`… mcp in:name,description`) | Repositories | Times this base names the brand in prose |
|---|---|---|
| `moodle mcp` | `248` | `5,286` |
| `canvas lms mcp` | `140` | `3,074` |
| 🔴 `blackboard mcp` | **`78`** | `433` |
| 🔴 `brightspace mcp` | **`41`** | `431` |
| 🔴 `d2l mcp` | **`28`** | `236` |
| `google classroom mcp` | `46` | — |

🔴 **Before this pass these shelves held about `5` rows across Brightspace, D2L and Blackboard
combined, while naming those three brands `1,100` times in their own prose.** 🟢 **`p828` filed
`20` of them after byte-read.**

🔵 **Why it matters commercially, and it is not "more rows".** Moodle and Canvas are the brands a
studio reaches for because they are the brands an *open-source* conversation reaches for. D2L
Brightspace and Blackboard are where a large share of North American and European
**institutional, paid** LMS estate actually sits — and that estate had almost no mapped open agent
surface in this base. 🟢 **The supply exists and is permissive; it simply was not indexed under
the words a pedagogy-shaped search uses.** This is `T86`/`T82` confirmed on a third axis: **the
vendor brand**.

🔴 **Honest limit.** The `total_count` figures are search-channel population counts, not quality
counts. Of the `~50` D2L/Blackboard repositories inspected, most are `0–2★` single-maintainer
student builds; `20` carried a byte-read permissive grant and are what was filed. **Population is
not adoption, and this trend claims only population.**

## T100 — The dominant form of an education agent is INSTITUTION-BOUND, and it names its institution in the repository name

🟢 **`30` of the `61` rows filed this pass are bound to ONE named institution** — UFC, UNEMAT,
IFSC, UFAL, CEFET-MG, UnB, UFPE, Cruzeiro do Sul, DTU, EDHEC, TUM, Glasgow, SRCE/Merlin, Burch,
UAEU, SLIIT, Tokyo University of Technology, USTC, Monash, MUN, Waterloo, Purdue, RIT, UH Mānoa,
among others — and in nearly every case **the institution's name or its system's name is the
repository name**.

🟢 **This is the operational form of `T82`/`T86`, and it is now strong enough to state as a
discovery protocol rather than an observation:** to find the education agent supply for a
territory, enumerate **the names of the institutions and the systems they run** — SIGAA, SUAP,
Q-Acadêmico, USOS, Aurion, Merlin, DTU Learn, Lamakū, myCourses — **not** the names of educational
activities. A search for *"tutor"*, *"grading"* or *"adaptive learning"* does not reach any of the
`30`.

🔵 **The consequence for an engagement.** An institution-bound agent is not a product, but it is
something better for a studio: **a working, legally reusable specification of exactly how that
institution's system authenticates, paginates and names its data.** 🟢 **The expensive part of an
LMS/SIS integration is that knowledge, and `30` universities' worth of it is sitting under a
permissive licence.** 🔴 **It is also fragile: single-maintainer, `0–2★`, and tied to a portal
that can change without notice.** Adopt the KNOWLEDGE, vendor the CODE, and expect to own it.

## T101 — The write path is already common in this tier, and the controls on it are the exception rather than the norm

🔴 **The finding.** Among the rows filed this pass, several act **on the student's behalf rather
than merely reading**: [`sahildayal/mycourses-mcp`](https://github.com/sahildayal/mycourses-mcp)
submits assignments and posts to discussions, [`MattFor/moodle-mcp`](https://github.com/MattFor/moodle-mcp)
submits homework, [`quantai1314/ustc-bb-mcp`](https://github.com/quantai1314/ustc-bb-mcp) submits
coursework, [`JesseTho/lamaku-mcp`](https://github.com/JesseTho/lamaku-mcp) **authors into**
courses (pages, media, discussions, assignments), and
[`Teci-AI/moodle-mcp-connector`](https://github.com/Teci-AI/moodle-mcp-connector) authors course
content. 🔴 **None of these declares a human-confirmation step in its own description.**

🟢 **Against that, three independent implementations in the same cohort ship a REAL control, and
each is a different kind:**

- 🟢 [`simonseifert/merlin-mcp`](https://github.com/simonseifert/merlin-mcp) — **phone-approved
  sends**: a human confirmation on the outbound action, out of band from the model.
- 🟢 [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) — **RBAC middleware**: the authorisation
  decision sits in the server, not in the prompt, which is the only form that survives an
  institution-wide (rather than student-owned) deployment.
- 🟢 [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp) — **the server
  never handles the password or the CAPTCHA**; the human logs in and the server inherits the
  session cookie. Credential non-possession as a design choice.

🔵 **Why this is the trend and not a note.** This base has repeatedly found that education agents
read. 🔴 **They have started writing, at exactly the moment the EMEA calendar makes the write path
the regulated one** — grading, steering learning and admissions are the Annex III uses, and a
system that *submits* or *authors* is far closer to that line than one that lists deadlines.
🟢 **The three controls above are cheap, already implemented and independently invented, which is
the strongest available evidence that they are the right ones to require.** Any engagement that
adopts a row from this tier should treat the write path as requiring one of them, by default.
