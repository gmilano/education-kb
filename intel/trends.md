---
industry: education
region: Global
updated: 2026-10-07
---

## 🔴 Forty-sixth pass, 2026-10-07 — five trends: a correction that did not travel one line, a consumer asking for a string that could not exist, plurality that resolves to one vendor, a free tier priced to zero, and a rationale its own suite refuted

⏱️ **Thirteenth pass of this date.** 🔵 **All market and regulatory figures are secondary and carry
their series (`P477`, `P515`); `eur-lex.europa.eu` stays proxy-blocked (`Gap 56`), so the EU
education dates are NOT cited as primary (`Gap 241`, and `P555`'s contradiction is unresolved).**
Existence by `git ls-remote --heads` against a negative control in the same run (`P510`); licences
from payload via the shared classifier (`P237`).

### T1 🔴 `P561` — a correction that is **one line away** from the defect it fixes still does not travel

🟢 **Pass 45 measured `P551`: the CC branch of the shared classifier STAMPED `-4.0` instead of
READING the version**, published a CC-BY-SA-3.0 treebank as 4.0, fixed it, and shipped a suite.
🔴 **The MPL branch — the line immediately above — was doing the identical thing, and still was at
the end of that pass.** Measured first-hand this pass on the canonical MPL-1.1 text (SPDX,
**23 668 B**, title *"Mozilla Public License Version 1.1"*): 🔴 **`MPL-2.0`**.

🔵 **The trend is not "a second instance of a known bug". It is that proximity is not transmission.**
This base's standing explanation for non-travelling corrections has been *distance* — five hardened
instruments knew `P171`, a sixth written from scratch did not (`P237`), so the fix was moved into a
shared file. 🔴 **`P561` falsifies the distance theory: the fix and the defect are in the same
function, ten lines apart, written by the same pass.** 🟢 **What transmits a correction is not
proximity and not a shared file — it is a SUITE THAT ASKS THE QUESTION OF EVERY BRANCH.** The CC
branch got four new assertions at pass 45; the MPL and EPL branches got none, so they kept their
defects under a green `141/141`.

### T2 🔴 `P562` — a consumer can spend a base's whole history asking for a value its producer cannot emit, and every suite stays green

🟢 **The pass's sharpest finding, and nothing in the library could reveal it.**
`p429-cession-claim-audit` classifies **delivery risk** — the question *"can we ship this?"* — by
testing the family string against sets. Its `COPYLEFT` set named **`EPL-2.0`**. 🔴 **The classifier
emitted the unversioned `EPL` and could never emit `EPL-2.0`**, so every EPL component that ever
passed through landed in `NO_CLASIFICADA` — the string this base reserves for *no verdict*.

| Side of the contract | What it held |
|---|---|
| 🔴 Producer's output | `EPL` |
| 🔴 Consumer's expectation | `EPL-2.0` |
| 🔴 Result | **`NO_CLASIFICADA`** on a licence family whose regime is entirely settled |
| 🟢 Suites | **green throughout** — both sides were internally consistent and tested |

🔵 **The lesson generalises past licences, and it is the one worth carrying:** a contract between two
components can be violated by **neither** of them. The producer's values were right, the consumer's
set was right, and the **intersection was empty** — a defect that lives in the join and is therefore
invisible to any suite that tests one side. 🟢 **The instrument class that catches it is a suite that
asserts the producer's actual OUTPUT SET against the consumer's EXPECTED SET**, which is what
`p429`'s six new cases now do. 🔴 **Of this base's instruments, that remains the only pair so
checked; the rest are still one-sided.**

### T3 🔴 `P564` — a shelf can look plural and have **one supplier**, and only the payload says so

🔵 **The mandated vertical query presented two independent MIT options for the ERP/CRM layer:**
`krayin/laravel-crm` (*"the only one you can fork, modify and ship inside a commercial product with
essentially no strings attached"*) and `aureuserp/aureuserp`. 🟢 **Both are MIT, confirmed on two
channels each.** 🔴 **Their `LICENSE` files are byte-identical — 1 077 B, `cmp` clean — and both are
held by `Webkul Software`.**

🔵 **So the licence-diversity a studio thinks it is buying by picking one of each does not exist**,
and the secondary channel could not have told them: it stated in as many words that it *"did not
find a source describing Webkul's broader role"*. 🟢 **The payload answered in one `cmp`.**
🔵 **The trend is the method, not the repo pair:** a licence LIST tells you what each row claims; a
licence PAYLOAD tells you who actually holds the grant, and holder-concentration is invisible to
every row-by-row reading — including this base's own, for 45 passes.

### T4 🔴 The entry tier of education AI is being priced to **zero** by four firms at once, and the incumbent is buying the AI layer

🔵 **Measured in the North America channel this pass** (secondary, `P515`): OpenAI *ChatGPT for
Teachers* (Nov 2025), Anthropic *Claude for Teachers* (Jul 2026), plus Google and Amazon giving AI
tools to students and teachers — 🔴 **four free offerings aimed at the same buyer** — while
**McGraw Hill completed its acquisition of TeachFX**, an AI-native teacher-coaching platform, and the
**AFT** runs a **USD 23 M** teacher-AI academy with **three AI companies** as partners.

🔴 **The implication for a studio is a repricing, not a new market.** The generic classroom assistant
is no longer a billable deliverable. 🟢 **What stays billable is what the free tier structurally
cannot supply:** the institution's data boundary, the **academic domain model**, conformity evidence
against a named instrument (Vietnam now, EU Annex III later), and integration with the SIS.
🔵 **And T5 of pass 45 still holds underneath this** — governance is the barrier, which is the same
sentence read from the buyer's side.

### T5 🟢 A rationale a suite can **refute** is worth more than one it cannot — measured on this pass's own fix

🔵 **This pass wrote a fix, justified it in a comment, and its own mutant suite refuted the
justification twice.**

| Claim written | Mutant built | Result |
|---|---|---|
| 🔴 *"the load-bearing control is the probe ORDER (2.0 first)"* | invert the order | 🟢 paho still `EPL-2.0` — **refuted** |
| 🔴 *"then it is the ANCHOR on the licence phrase"* | unanchor the 1.0 probe, leave it second | 🟢 paho still `EPL-2.0` — **refuted** |
| 🟢 *"the two protections are REDUNDANT"* | unanchored **and** first | 🔴 `EPL-1.0` — **confirmed: both must break** |

🔵 **The comment in `lib/license_family.sh` now asserts the redundancy and prints the 2×2**, because
that is what was measured. 🟢 **The general point, and it is `P541`'s in a new direction:** a control
whose rationale was never tested is a control whose rationale is a guess. 🔴 **Forty-five passes of
this base's prose carry rationales in exactly that state** — the difference here is only that a
mutant was cheap enough to build, and it cost two wrong sentences to find out.

### 🟡 What did not move, said plainly

🔴 **Zero new education-native AI agents, sixth consecutive pass, fourteenth saturation
declaration** — the mandated query returns the horizontal shelf plus catalogues, in every region.
🔴 **Zero new education-native foundational repos** — the mandated platform query returned the
generalist ERP axis for the twenty-seventh time. 🔴 **LATAM produced nothing new** (reproduction of
pass 45's IESALC/TALIS/PISA figures, which is confirmation). 🔴 **UK, Gulf and Africa still empty,
fifth consecutive pass.** 🟡 **`Gap 249` opened and left open**: dual licensing (`h2database`,
MPL-2.0 **or** EPL-1.0) collapses to one arm, and fixing it changes `family_of`'s return contract
from a string to a set. 🟡 **`p411-cession-identity-gate` still inlines a licence classifier and
still carries `P561`** — declared, not fixed.

## 🔴 Forty-fifth pass, 2026-10-07 — five trends: a fix that was appended instead of substituted, a version that was stamped instead of read, a ShareAlike floor under an entire language, the code/content licence line, and regulation turning binding in the region that had nothing

⏱️ **Twelfth pass of this date.** 🔵 **All market and regulatory figures are secondary and carry
their series (`P477`, `P515`); `eur-lex.europa.eu` stays proxy-blocked (`Gap 56`), so the Annex III
deferral is NOT cited as primary (`Gap 241`).** Existence by `git ls-remote --heads` against a
negative control in the same run (`P510`); licences from payload via the shared classifier (`P237`).

### T1 🔴 `P550` — a fix that is **appended** rather than **substituted** leaves two answers in one file, and no suite can see it

🟢 **`lib/license_family.sh` — the shared control every licence verdict on this KB passes through —
defined `commercial_use_ok()` twice**, and the comment block explaining why the first version was
wrong sat **between the two**. Bash keeps the last, so the hardened body ran and **no published
verdict was wrong**; 🔴 **but correctness rested on source order.**

🔵 **The trend is not the duplicate — it is why forty-five passes of green suites could not see it.**
A suite calls a **name**; the name resolves to **one** body; `132/132` says nothing whatsoever about
the body that did not resolve. 🔴 **`P541` was about a gate that measures nothing while reporting
success. This is its sibling: an instrument that measures CORRECTLY while carrying a second,
contradictory implementation of the same question.** 🟢 **Measured cost if the order ever flipped:
7 of 27 of this KB's real payloads invert** — Moodle's GPL-3.0 and the **Unlicense** among them —
**all** in the over-restrictive direction (`P308`'s, not `P312`'s), which bounds the damage to lost
shelf rather than an unsafe deliverable.

🔵 **The general lesson, and it is cheap to apply:** when a pass fixes an instrument, the old
implementation must be **deleted**, not left above the new one with an explanation in between. 🟢 **Now
mechanically enforced** — `p550-duplicate-definition-sweep/` over 302 files, suite 26/26.

### T2 🔴 `P551` — the **version** is part of a licence's identity, and it was being stamped rather than read

The same control read a CC payload's *attributes* (NC/SA/ND) from the text and then concatenated
**`-4.0` literal**. 🟢 **Caught on `UD_Portuguese-PUD`**, whose 19 556-byte title block says
**ShareAlike 3.0** and contains no "4.0" at all.

🔴 **The direction is the dangerous one.** CC **4.0** explicitly covers *sui generis* **database
rights** (Art. 4) and adds a 30-day cure period; **3.0** does neither — and **a treebank is a
database**. 🔵 **So the defect did not lose shelf, it INVENTED a grant**, which is `P312`'s direction
and the one that costs a deliverable. 🟢 **Fixed, with "no version declared" answering
`CC-BY-SA-UNVERSIONED` instead of defaulting to 4.0** — because *"declares 4.0"* and *"declares
nothing"* are different facts and `P502` says they must not share a string.

🔵 **Both T1 and T2 were found by RUNNING the control on new input, not by reading it** — the same
way `P546` surfaced last pass. 🟢 **That is now three consecutive passes where the productive audit
move was to hand a hardened instrument a corpus it had never seen.**

### T3 🔴 `Gap 246` measured: there is **no permissive Portuguese treebank**, so the ShareAlike floor under PT NLP is **structural**

🟢 **The unmeasured half of `Gap 246` is closed with data.** spaCy's *code* is MIT; its Portuguese
**model artefacts** are not:

| Asset | Licence (measured this pass) | Commercial (`P250`) |
|---|---|---|
| `pt_core_news_sm` / `md` / `lg` **3.8.0** | 🟡 **CC-BY-SA-4.0** | 🟢 ALLOWED |
| `UD_Portuguese-Bosque` v2.8 (the training corpus) | 🟡 **CC-BY-SA-4.0** | 🟢 ALLOWED |
| `UD_Portuguese-GSD` | 🟡 **CC-BY-SA-4.0** | 🟢 ALLOWED |
| `UD_Portuguese-PUD` | 🟡 **CC-BY-SA-3.0** | 🟢 ALLOWED |
| `UD_Portuguese-Petrogold` | 🟡 **CC-BY-SA-4.0** | 🟢 ALLOWED |
| `UD_Portuguese-CINTIL` | 🔴 **CC-BY-NC-ND-4.0** | 🔴 **PROHIBITED** |
| WikiNER (NER source) | 🟢 CC-BY-4.0 | 🟢 ALLOWED |
| Explosion fastText vectors (`md`/`lg`) | 🟢 **CC0** | 🟢 ALLOWED |

🔴 **Every Universal Dependencies Portuguese treebank is ShareAlike or worse.** 🔵 **So this is not a
bad choice of model that a better choice fixes** — the obligation is inherited from the only training
data that exists, and swapping Bosque for GSD or Petrogold changes nothing. 🟢 **The practical rule
this yields:** inference against an **unmodified** `pt_core_news_*` and shipping your own code beside
it is clean; **fine-tuning produces a CC-BY-SA-4.0 derivative**, so the tuned artefact is the thing
that obliges. 🔵 **And CINTIL must be kept out of any pipeline** — NonCommercial *and* NoDerivatives.

### T4 🟡 `P553` — the permissive/copyleft line in education AI runs between **code and content**, not between agents and platforms

🔵 **Two unrelated tiers measured in the same pass returned the same licence**, which is what makes
this a trend rather than a coincidence:

| Tier | Example measured this pass | Licence |
|---|---|---|
| Code | `explosion/spaCy`, `essay-br`, `wwrwbs/AI_AWE` | 🟢 MIT / Apache-2.0 |
| Agent-skill corpus | `GarethManning/education-agent-skills` (165 skills) | 🟡 **CC-BY-SA-4.0** |
| Model artefact | `pt_core_news_*` 3.8.0 | 🟡 **CC-BY-SA-4.0** |
| Training corpus | `UD_Portuguese-Bosque` | 🟡 **CC-BY-SA-4.0** |

🔴 **A procurement review built for code licences reads the repo-root `LICENSE`, finds MIT, and
stops** — and in education the obligation is in the *pedagogical content*, the *model* and the
*corpus*. 🟢 **This is the most transferable finding of the pass** and it generalises past Portuguese:
education's valuable assets are curricula, item banks, rubrics and treebanks, and the academic and
public bodies that produce them default to Creative Commons, not to MIT.

### T5 🟢 Regulation turned **binding** in the region that had nothing, while the EU's own education date got *less* certain

🔵 **For eight passes APAC returned no education-policy instrument.** 🟢 **This pass it returned the
most education-specific binding one in any region:** **Vietnam**'s AI law, in force **2026-03-01**,
names **education** among six high-risk sectors — *automated assessment* and *behavioural
monitoring* explicitly — and attaches the classification **only where the output is the sole basis
for a decision without meaningful human review**. 🔵 **That qualifier is a design brief, not a
caveat**: preserve a human decision point and the obligation does not attach. 🟢 **Also binding:**
Korea's AI Framework Act from **2026-01-22** (foreign providers over thresholds must appoint a
domestic representative and report to MSIT); Taiwan's AI Basic Act from **December 2025**; China's
existing algorithm, deep-synthesis and generative-AI rules. 🟡 **Japan and Singapore stay
voluntary.**

🔴 **Meanwhile the EU — the region this KB treats as its regulatory anchor — produced a
contradiction** (`P555`, `intel/market.md`): the Commission's page enforces from **2026-08-02**
while a sector guide reports revised high-risk dates of **2027-12-02** and **2028-08-02**. 🔵 **The
trend across both: binding beats guidance in 2026, and the places to read the rule are shifting away
from the jurisdiction everyone benchmarks.** 🟢 **In North America the mandate arrived at the state
level** — Ohio requiring every K-12 district to hold an AI policy by **2026-07-01**.

### 🔵 Gap ledger for this pass

| | |
|---|---|
| 🟢 **Closed** | `Gap 246`'s measurement half — spaCy PT **model artefact** licences measured (**CC-BY-SA-4.0**) and the corpus tier swept: **no permissive PT treebank exists** |
| 🟡 **Narrowed, NOT closed** | `Gap 244` — `p550`'s oracle reaches both shell and payload channels, but the 31+9 rows `P542` left unjudged are **still unjudged**; nothing in this pass adjudicated them |
| 🔴 **Still open** | `Gap 245` — the 23 `P541`-class defects named at pass 44 are **still named and unfixed**; this pass fixed two defects in the *classifier*, not those 23 |
| 🔴 **Widened** | `Gap 241` — six passes of secondary sources have produced a **contradiction** on the EU education date, not a convergence (`P555`) |
| 🔴 **Opened** | `Gap 247` — the ShareAlike reach of a **fine-tuned** `pt_core_news_*` artefact is reasoned from the licence text, **not** tested against a published CC-BY-SA interpretation or counsel; the host-vs-ship rule in `compose/patterns.md` rests on it |
| 🔴 **Opened** | `Gap 248` — **UK, Gulf and African** education-AI regulation returned nothing in this pass's EMEA channel; "EMEA" on this KB currently means **EU** |

## 🔴 Forty-fourth pass, 2026-10-07 — four trends: a gate that passed while blind hid a real backlog, "port" turns out to mean "reimplement", the acronym defect is asymmetric, and a sweep's own accusations needed auditing

⏱️ **Eleventh pass of this date.** 🔵 **All market and regulatory figures are secondary and carry
their series (`P477`, `P515`); `eur-lex.europa.eu` stays proxy-blocked (`Gap 56`), so the Annex III
deferral is NOT cited as primary (`Gap 241`).** Existence by `git ls-remote --heads` against a
negative control in the same run (`P510`); licences from payload via the shared classifier (`P237`).

### T1 🔴 `P542` / `P546` — a blind gate does not merely fail to catch things, it **manufactures a clean record**, and this KB has been reading one

🟢 **`Gap 243` is closed with code** (`compose/code/p542-empty-input-sweep/`, `repos/foundations.md`
`P542`): **23 of 187** invocation points in `compose/code/` exit `0` having judged nothing. 🔴 **Two
of the 23 are this KB's own gap gates** (`p370`, `p471`).

🔵 **The trend is not the count — it is what the count was hiding.** `p383-region-heading-gate`, run
against `intel/market.md` for the first time this pass, returns **14 findings** and exits `1`: the
file had accumulated **8** canonical `## Opportunities by region` blocks where the contract allows
**one**, and **every one of them omitted `Global`**. 🔴 **That backlog is seven passes old.** It was
invisible because the gate was being invoked with no arguments, printing `total 0` — the exact defect
`P541` named at pass 43.

🔴 **The general lesson, and it is the most expensive one on this KB:** a gate that cannot distinguish
*"I checked and found nothing"* from *"I checked nothing"* does not produce a gap in the record — it
produces a **positive claim of cleanliness**. 🔵 **Silence is detectable; a false `0` is not.**
🟢 **Acted on**: the backlog is cleared, the live block carries all five values, `p383` exits `0`.

### T2 🔴 `P544` — in the Portuguese feature tier the code exists and **none of it may be sold**, so the remedy's verb changes from *port* to *reimplement*

`Gap 239` named the remedy as *"port the extractor"* once a Portuguese equivalent was found. 🟢 **A
far more complete one was found than the gap assumed** — but its licence topology voids the verb:

| Asset | Licence (payload) | What blocks it |
|---|---|---|
| `nilc-nlp/nilcmetrix` (23 metric modules, Go+Python service) | **AGPL-3.0** | 🔴 **network copyleft** — and it ships as an HTTP service (`EXPOSE 8080`), which is the precise trigger |
| `nilc-nlp/coh-metrix-port` | **GPL-3.0** | 🟡 copyleft deliverable |
| `kristopherkyle/TAALED` — the tool `Gap 239` names as the feature source | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **NonCommercial — `commercial_use_ok()` refuses it** |
| `explosion/spaCy` | 🟢 **MIT** | 🟢 nothing |

🔵 **This is `P516`'s shape for the third time** — *"the licence is permissive and the intelligence is
not"* — now inverted once more: here the **intelligence is freely published** (the index definitions
are statistics in papers) and the **implementations** are what is encumbered. 🟢 **So the path is
real and the cost is honest**: reimplement the index set over spaCy's `pt_core_news_*` pipeline from
published definitions. 🔴 **Nothing is copied, so nothing needs licensing — and nothing is inherited
either**, including the validation those tools accumulated. → **`Gap 246`**.

🔴 **A correction that must travel:** pass 43 wrote module 2's features as *"31 TAALED/QuanSyn
features"*. 🔵 **A later pass must not read that as "TAALED is available to build on."**

### T3 🟢 `P546`'s sibling — the region-acronym defect is **asymmetric**, which makes it cheap to route around

`P513` said the acronym is the defect. 🟢 **This pass measures that the defect is not uniform**, and
that is the actionable part: **LATAM** returns education-native research (UNESCO IESALC, UNU-IAS,
SciELO, IDB), **North America** returns a usable if vendor-heavy channel, and **EMEA** and **APAC**
return enterprise IT with the channel stating outright that it found no education-specific data.

🔵 **Why: Spanish- and Portuguese-language academic and multilateral literature genuinely writes about
*América Latina* as a unit, while no education ministry on earth describes itself as "EMEA".** 🟢
**Operational rule left written:** run the probe as prescribed for LATAM and NA; for EMEA and APAC
substitute the **national instrument** (ministry, Council of Europe, MOE) before concluding anything.
🔴 **Four identical regional queries is the wrong shape for a global KB** — it reads as coverage and
delivers two nil results.

### T4 🔴 `P543` — a sweep that audits other instruments needs its own accusations audited, and hand-checking **one** row changed the headline by a third

🔵 **The sequence is the trend.** `Gap 243`'s remedy — *"assert a non-zero exit"* — produced **49**
accusations on first run. Two shapes exit `0` on empty input **correctly** and the loop could not see
either:

1. 🔴 **library modules** (no `__main__`; the suite *imports* them) — **24 of the 49**, found by the run;
2. 🔴 **stdin filters** (`sys.stdin`, `while read`; EOF ⇒ correctly do nothing) — **11 of the
   remaining 34**, found by **reading one accusation by hand** before publishing.

🟢 **49 → 25 → 23.** 🔵 **The first number was wrong by more than a factor of two, and the prescribed
remedy produced it.** 🟢 **Both defects are now mutants in the suite** (`ignora_invocable`,
`ignora_filtro`) — the `P480` lesson: a correction that is not a regression test does not survive the
next instrument. 🔴 **The general form, and this KB has now paid for it twice (`P502`, and here): an
instrument that collapses two different causes into one verdict will report the wrong one with full
confidence.**

🟢 **The counter-evidence this pass also produced, and it belongs in the same trend** (`P545`): the
sweep accidentally re-ran a dated result artefact from pass 39 and it reproduced with **exactly one
byte** of difference — `pom_bytes` for OpenOLAT, an **upstream** property. 🔵 **So the correct reading
of 23/187 is "a third of this tree's gates cannot tell empty from clean", NOT "this KB's evidence is
fabricated."** 🟢 **The instruments that measure, reproduce.**

### 🔵 Trend table — what moved, what did not

| | This pass |
|---|---|
| 🟢 **Closed** | `Gap 243` with code (`P542`), 42/42 suite, 7 mutants killed; `p383`'s 14-finding backlog on `intel/market.md` |
| 🟡 **Narrowed** | `Gap 239` (feature layer found, licence blocks the verb); `Gap 242` (a better instrument named: UNESCO IESALC / UNU-IAS, 200 HEIs, 19 countries) |
| 🔴 **Opened** | `Gap 244` (oracle A does not reach shell: 31+9 rows unjudged); `Gap 245` (the 23 defects are **named and unfixed**); `Gap 246` (PT index set must be reimplemented; spaCy PT **model** licences unmeasured) |
| 🔴 **Unmoved** | `Gap 56` (eur-lex proxy-blocked); `Gap 240` (upstream contribution untaken); `Gap 237` (Spanish, structural); the **agent** shelf — twelfth consecutive saturated pass, fourth with zero new rows |

## 🟢 Forty-third pass, 2026-10-07 — three trends: a value asserted from itself is not measured (found in this pass's **own** oracle), `Gap 237`'s premise is **refuted**, and the EU clock this KB reads was moved sixteen months

⏱️ **Tenth pass of this date.** 🔵 **All market and regulatory figures are secondary and carry their
series (`P477`, `P515`); `eur-lex.europa.eu` remains blocked by the proxy (`Gap 56`), so the Omnibus
date below is NOT cited as primary.** Existence by `git ls-remote --heads` against a negative control
in the same run (`P510`).

### T1 🔴 `P534` — mutation testing found two defects in **this pass's own oracle**, and neither was findable by reading it

🟢 **`P533`'s suite passed `38/38` before it was mutation-tested.** It was then run against **11
deliberate mutations of the emitter**, and 🔴 **two survived** — the oracle was passing while not
judging:

| Mutation | 🔴 Why it survived | 🟢 Fix |
|---|---|---|
| **M8** — default `step` becomes `2` instead of `1` | `O3.grid` and `O3.cover` both compare the executed draw against `grid()`, and **both sides derive from `effective_step`**. A wrong default is **self-consistent and therefore invisible**. The round-trip oracles miss it too, because a defaulted `step` is never emitted at all | `O3b` asserts the default against the **external source** (`operator-attribute.ts:24`, `step ?? "1"`), not against another expression of itself |
| **M9** — drop `"` → `&quot;` in attribute escaping | 🔴 **Every attribute value in the suite happened to be quote-free.** The surface was never exercised | `O7b` round-trips a `title` carrying `"`, `<` and `&` |

🔵 **This is `P469`'s rule in miniature, and it deserves restating in its strongest form: a value
asserted from itself is not measured.** `P469` recorded it about a *gap status*; `M8` is the same error
one level down, inside a test — the assertion and the thing asserted shared a derivation, so the test
could only ever agree with the code.

🟢 **And `P471`'s rule held exactly as written**: a gate can pass every assertion while judging
nothing. Reading the suite would not have found either defect; **mutating the thing under test did.**

🔴 **A third defect, same provenance.** Mutation **M4** (drop text escaping) *was* detected — unescaped
output is not well-formed, so the assertion's own parse raised — but it surfaced as an **uncaught
traceback rather than a reported failure**. 🔵 **On a board a crash is indistinguishable from a broken
runner**, so a real detection reads as infrastructure noise. `check_call` now reports an assertion's
own exception as a failure.

🟢 **Final matrix: 11 of 11 mutations detected, baseline back to `43/0`.** 🔵 **The last row matters —
a matrix that cannot return to zero failures is measuring its own damage, not the code's.**

> 🟢 **Rule for every later pass that ships an instrument:** mutate it before publishing the number.
> This KB has twelve passes' worth of gates whose pass-counts were never adversarially tested, and
> `P534` is the first evidence of what that is worth: **2 of 11 defects slipped a suite that read as
> complete.**

### T2 🟢 `P537` — `Gap 237`'s premise is **refuted for Chile**: there is no rubric to automate, because the exam has no essay

🔵 **`Gap 237` prescribed the cheaper probe: *"query per country (`prueba de egreso`, `PAES`, `examen
de admisión`) rather than pan-Spanish, since `P521` is this KB's own evidence that the query's shape
hides tiers."* 🟢 **It was run verbatim. It paid twice, and neither payment was the one expected.**

🔴 **The first payment is a refutation.** The query surfaces practice platforms for Chile's **PAES** —
[`Rodrigo0876/PAESnet`](https://github.com/Rodrigo0876/PAESnet) (web practice, auto-marking,
simulated items explicitly *not* DEMRE originals) and
[`AngelitUX/EstudiaUni`](https://github.com/AngelitUX/EstudiaUni) (timed official DEMRE mock papers,
Gemini-backed tutor) — 🔴 **and none of them grades written work, because the PAES has no essay
component.** 🔵 **So the thing `Gap 237` was looking for in Chile cannot exist**: there is no official
essay rubric to standardise on, because there is no official essay.

🟢 **This sharpens `Gap 237` from "unmeasured" to "structurally mis-specified per country", and it
changes the remedy's unit.** Pass 42 wrote the gap as *"Spanish-speaking LATAM has no single
equivalent instrument"* and priced the remedy as *"a rubric and a human-graded corpus, per target
country"*. 🔴 **The per-country probe shows the first question is prior to that: does the country's
exam contain graded writing at all?** Chile's does not. 🔵 **A rubric programme for a country with no
essay exam is not expensive — it is void.** The probe must therefore be *"which Spanish-speaking
systems examine writing against a published rubric"*, and only those are candidates.

🔵 **The second payment is `P535`** — the same result set returned `wwrwbs/AI_AWE`, the Apache-2.0
assembled scorer `Gap 236` said did not exist. 🟢 **Recorded here because of where it came from: a
Spanish-language query about Chile surfaced an English-language asset that ten passes of
English-language sweeps had missed.** 🔴 **That is a second instance of `P521`'s lesson and it points
the opposite way** — `P521` found that changing the query's *language* reveals tiers in that language;
`P537` finds that changing the language reveals assets in the *original* language too, because the
corpus a query reaches is not the corpus its language suggests.

### T3 🔴 `P538` — the EU high-risk education deadline this KB has carried was **deferred sixteen months**, and this KB has recorded the superseded date more than once

🔴 **The standing figure in this KB's lineage is `2026-08-02` as full enforcement for education AI.**
Pass 40's own note already flagged that *"the EMEA channel reproduced a superseded date"*. 🟢 **This
pass can now say what the correct position is, and it splits by article:**

| Obligation | Date | Status |
|---|---|---|
| **Annex III high-risk** education systems — admissions, learning-outcome evaluation, level placement, exam/behaviour monitoring | 🔴 **Deferred to December 2027** | 🔴 **Moved by the "Digital Omnibus" amendment — ~16 additional months.** Compliance obligations themselves reported unchanged, only the date |
| **Article 50** transparency / AI-disclosure | 🟢 **Still 2026-08-02** | 🟢 **Did not move** |
| **Article 4** AI-literacy duty | 🟢 **In effect** | 🟡 Reported with *"relaxed scope"* |

🔴 **Stated limit, and it is why this is a trend and not yet a corrected fact in `intel/market.md`'s
primary column:** `eur-lex.europa.eu` and `data.europa.eu` are **blocked by this environment's proxy**
(`Gap 56`, open since pass ~24). 🔵 **Every source for the deferral is secondary** — sector press and
compliance vendors — and they name the instrument inconsistently. 🟢 **What is consistent across them
is the split above**: the high-risk clock moved, the transparency clock did not. 🔴 **A later pass with
eur-lex reachable must pin the amending regulation's identifier and date before this is quoted as
settled.** → **`Gap 241`**.

🔵 **Why it matters commercially rather than only legally.** The deferral moves the *compliance*
deadline and not the *procurement* one: an institution buying an admissions or assessment system in
2026 is buying a system that must be conformant by December 2027, and conformity assessment is a
property of the system, not of the purchase date. 🟢 **So the sales conversation does not get sixteen
months of relief; the documentation does.**

### T4 🔴 `P541` — a gate in this KB's own `compose/code/` reported **success while measuring zero files**, and this pass paid for it in real time

🔵 **Found by accident, which is the only reason it is reportable.** Pass 43 ran
`compose/code/p383-region-heading-gate/check_headings.py` with no arguments to verify its own new
`## Opportunities by region` block, and read the output:

```
archivo	hallazgo	linea	detalle
#	total	0
```

🔴 **`total 0`, exit code `0` — and it had measured zero files.** The gate takes paths **as
arguments**, received none, iterated an empty list, and reported a clean tree. 🔴 **This pass believed
its region headings were gated for several minutes on the strength of a number that judged nothing.**

🟢 **Proof it was not judging, run before the fix**: a deliberate `### Latam` — the exact
open-vocabulary defect the mandate warns about, *"not 'Latam', not 'Brazil'… each variant becomes its
own bucket and the filter stops working"* — was planted in a copy of `intel/market.md` and the gate
still reported `total 0`. 🟢 **Invoked correctly it catches it immediately** (`P383-OUT-OF-VOCAB`).

🔵 **The three gates in this tree have three different no-argument contracts, and nobody wrote that
down:**

| Gate | No-argument behaviour | Verdict |
|---|---|---|
| `p243-frontmatter-coverage` | 🟢 **Discovers its own files** — reported `146 de 146` | 🟢 Correct by design |
| `p239-table-integrity` | 🟡 **Crashes** (`FileNotFoundError` on its `"-"` default) | 🟡 Ugly, but **impossible to mistake for a pass** |
| `p383-region-heading-gate` | 🔴 **`total 0`, exit `0`** | 🔴 **The defect** |

🟢 **Fixed, with the control and the control's own control.** `main([])` now returns `2` with
`P541-NO-INPUT` on stderr, and three assertions were added to `test_check_headings.py`: empty input
**refuses**, a clean file **approves** (`0`), a dirty file **fails** (`1`). 🔵 **The last two matter as
much as the first — a gate that refuses *always* also judges nothing.** Suite: **8/8 → 11/11**.

🔴 **Why this is a trend and not a bug report.** `P534` (this same pass) found two defects in a
*freshly written* oracle by mutating it. `P541` found one in a gate that has been **in the tree since
pass 117** and has been cited as authority since. 🟢 **Together they say something this KB can act on:
a pass-count is not evidence until somebody has tried to make it lie.** 🔵 **And `P237`'s rule
generalises one step further than it was written:** a shared *instrument* stops the defect from being
re-implemented, but it does not stop the instrument from being **mis-invoked**. 🟢 **A usage contract
that has to be remembered is not a control either** — so the gate now enforces its own.

> 🔴 **Prescription for later passes, cheap and specific:** every instrument in `compose/code/` that
> takes paths by argument should refuse empty input. 🔵 **This pass fixed the one it tripped over and
> did not sweep the other ~120 directories** — that sweep is **`Gap 243`**.

## 🟢 Forty-second pass, 2026-10-07 — four trends: the sweep language was the missing axis, a 0-ref result refutes a **slug** not an **artefact**, open weights reach the proprietary baseline, and a keyword sweep inside a monorepo needs a package column

⏱️ **Ninth pass of this date.** 🔵 **All market figures are secondary and carry their series (`P477`,
`P515`).** Existence by `git ls-remote --heads` against a negative control in the same run (`P510`).

### T1 🟢 `P521` — the missing axis was the **language of the query**, and `P503`'s lesson now has three instances

🔵 **`Gap 235` prescribed exactly one next step: *"query the Portuguese-language corpus directly
(`corretor automático de redação código aberto`)"*. 🟢 **It was run verbatim, and it worked on the first
attempt** — six distinct Portuguese essay-scoring trees, swept in full in `agents/top.md` (`P522`).

🔴 **None of them had ever appeared in this KB**: `CorrecaoRedacao`, `Corretor-de-redacao`, `UTFPR`,
`essay-br`, `lplnufpi`, `LanguageTool` and `QWK` each returned **0 live files** before this pass.

🟢 **This is the third time a sweep's blind spot has turned out to be an axis nobody had written down,
and the three make a progression worth stating as a rule:**

| Pass | The axis that was missing | What the sweep was varying instead |
|---|---|---|
| `P503` | the **topic vocabulary** | synonyms within one vocabulary |
| `P508` | the **distribution channel** — `KernEqWPS` is on neither CRAN nor PyPI | language and licence |
| 🆕 `P521` | the **language of the query itself** | English terms, more of them |

> **`P521`.** 🟢 **A tier can be invisible to every English-language query and busy in its own language,
> and for a company whose engagements are regional that is a structural blind spot rather than an
> accident.** 🔵 **The rule to carry: when a regional tier reads as empty, the next instrument is not
> another English synonym — it is the same question in the language the practitioners publish in.** 🔴
> **And the corollary that costs the most if ignored: eight passes recorded a LATAM essay-scoring gap
> that was an artefact of the query language, not a fact about the region.**

### T2 🔴 `P523` — `P517`'s slug was wrong, and a `0`-ref result refutes a **slug**, never an **artefact**

🔴 **Reported against this KB's own prior finding, which is what `P502` requires.** `P517` and `Gap 235`
recorded `AIRGOLAB-CEFET-RJ/textgrader` as *"0 refs — does not resolve"* and concluded **"nothing
retrievable"**. 🟢 **The existence verdict was right. The inference drawn from it was not, and the
organisation name was simply wrong.**

| Slug | `git ls-remote --heads` | 🟢 What it establishes |
|---|---|---|
| `AILAB-CEFET-RJ/gcc1734` | 🟢 **1 ref, `main`** | 🟢 **The organisation is `AILAB-CEFET-RJ` and it exists** — the control that makes the rest of this table mean something |
| 🔴 `AILAB-CEFET-RJ/textgrader` | 🔴 **0 refs** | 🔴 Does not resolve **under the correct org** |
| 🔴 `AIRGOLAB-CEFET-RJ/textgrader` (`P517`'s slug) | 🔴 **0 refs** | 🔴 **The org in `P517` was a misreading** — *AirGoLab* is how the lab is named on Brazil's MCTI research-infrastructure registry, `AILAB-CEFET-RJ` is how it publishes on GitHub |
| 🔴 `AIRGOLAB-CEFET-RJ/DRL-ALM` | 🔴 **0 refs** | 🔴 Corroborates: **no repo resolves under `AIRGOLAB-CEFET-RJ` at all** |
| 🔴 `TextGrader`, `Textgrader`, `text-grader`, `textgrader-api`, `ailab-cefet-rj/textgrader` | 🔴 **0 refs each** | 🔴 Five further name and case variants, all negative |
| `totally-fake-org-zzz9/nope-repo-abc` — 🔵 control | 🔴 **0 refs** | 🔴 Does not exist |

🔵 **And the artefact is independently attested while the repository is unreachable.** The project's own
declared site, `aquarii.eic.cefet-rj.br/textgrader`, returns 🔴 **`403` over HTTP and fails TLS over
HTTPS** — unreachable, not absent. It is also catalogued on **eduCAPES**, Brazil's federal higher-education
repository, as *"Plataforma de Avaliação Automatizada de Textos Dissertativos com Base nas Competências
do ENEM"*, pointing at that same URL. 🔵 **A search result still hyperlinks the GitHub repository and
quotes its README, so it was public at crawl time.**

> **`P523`.** 🔴 **`0` refs means *this slug serves no refs*. It does not mean the project does not
> exist, was never published, or has nothing to offer** — and `P517` quietly made all three of those
> inferences from one measurement. 🟢 **The discriminating control is a **sibling repo under the same
> org**: if a sibling serves refs, the org is real and the verdict is about the repo; if nothing under
> the org serves refs, the org name itself is the suspect.** 🔵 **Neither `P510` nor `P517` specified
> that second control, and without it a typo and a deletion are the same string.** 🟢 **`textgrader`'s
> correct status: published, peer-catalogued, and **not anonymously retrievable today** — private,
> renamed or removed, and this pass cannot tell which.**

### T3 🟢 `P526` — measured counter-evidence to `P516`: open weights reach the proprietary baseline, and **compute** is the binding constraint

🔵 **`P516` found the essay-scoring tier inverted — the fully-open option archived, the live option an
MIT harness around a proprietary model — and asked the right question: *where does the judgement live,
and can the client keep it?* 🟢 **The UTFPR project (`P522`) is the first artefact this KB has read that
actually measures that trade-off, on Portuguese, against a human-graded reference.** 🔴 **Its code is
ungranted, so what follows is **read as evidence, not adopted as a component**.**

🔵 **Reported in the project's own metric, Quadratic Weighted Kappa against ENEM human scores, 300-essay
fixed stratified sample, cross-prompt evaluation:**

| Configuration | QWK raw | QWK calibrated | 🔵 What it isolates |
|---|---|---|---|
| Holistic, one call per essay | 0.47 | 0.54 | the naive baseline |
| One call **per competency** (C1–C5, rubric in prompt) | 0.53 | 🟢 **0.60** | 🟢 **Decomposing by rubric criterion is worth ~0.06** |
| **+ anchor essays** (one per score band) and a C5 checklist | 0.59 | 0.61 | 🟢 C1 rises 0.29 → 0.35 |
| **+ LanguageTool on C1** and a Reflect-and-Revise C5 rubric | 🟢 **0.63** | 0.61 | 🟢 **Best raw figure; `P525`'s open component is doing work** |

🟢 **The two results that matter more than any single number:**

| | |
|---|---|
| 🟢 **Open weights are not the weak link** | **`gpt-oss-120B`, open-weight, reaches ~0.52 holistic — the same band as the hosted proprietary model it was compared against.** 🔵 **So the project's own evidence is that the *proprietary* model carried no decisive quality advantage at the holistic level** |
| 🔴 **Most of the apparent weakness was **scale**, not judgement** | 🟢 **A bias calibration learned on theme-separated folds moves the best 7B model from QWK 0.25 to 0.42.** 🔵 **That is the single largest effect in the table and it is pure post-processing — no better model, no more compute** |

🔴 **And the constraint that actually bit, which is the part a studio must price.** The project
**abandoned** local fine-tuning of 70B/72B models mid-run: *"interrompida no meio da execução por falta
de crédito computacional"*. 🔵 **It then moved to free hosted endpoints.** 🟢 **So the reason the
judgement ended up off-premises was **GPU budget**, not model capability** — a cost question, which a
studio can answer, rather than a capability question, which it cannot.

> **`P526`.** 🟢 **`P516`'s diagnosis stands and its pessimism does not.** 🔵 **`P516` said a client
> cannot keep the judgement in this tier. The measured position is better: with `essay-br` (MIT,
> `P524`) as the graded reference, an open-weight model at the proprietary baseline, calibration worth
> more than model size, and LanguageTool as an ownable C1 feature source, **the judgement can be
> owned** — the price is GPU time for fine-tuning, and it is a known, bounded, one-off price.** 🔴
> **The honest caveat the source itself states: at 300 essays, differences of ~0.04 sit inside the noise
> (paired bootstrap), and the published essay-br band is 0.60–0.73 — so 0.63 is mid-band, not
> state-of-the-art.** 🟢 **The procurement consequence: the per-score marginal cost and the
> frozen-scoring problem `P516` identified are both **solvable here**, and solving them is a sizing
> exercise rather than a research project.** See the chain in `compose/patterns.md` (`P532`).

### T4 🔴 `P528` — inside a monorepo, a keyword sweep without a **package** column produces a false positive

🔵 **Reported against this pass's own instrument, before `P527` was written.** The first sweep for QTI
template support searched the whole `qti3` tree for *"template"* and found **40+ files**, which reads as
strong support. 🔴 **Re-run per package, the `writer` had `0` — and its one *"template"* hit,
`item-body-template.ts`, is a **layout** placeholder validator with no relation to template variables.**

| Sweep | Result | Truth |
|---|---|---|
| 🔴 `grep -r template` over the repo | 🔴 **40+ files → "supported"** | 🔴 **Wrong for the package that matters** |
| 🟢 Same term, **per package** | 🟢 `core` 45, **`writer` 0** | 🟢 **Correct, and it is the whole of `P527`** |

> **`P528`.** 🔴 **In a monorepo a repository-level keyword count measures the *project*, and a
> capability question is almost always about **one package**.** 🟢 **The fix is a column, not a better
> query: sweep per package and print the package name.** 🔵 **The aggravating factor here is a genuine
> homonym — QTI's *template variables* (parametrisation) and an HTML *body template* (layout) share a
> word — so the false positive was not noise, it was the adjacent concept.** 🟢 **General rule:
> confirm a capability on the **exported surface** of the specific package that would provide it
> (`P500`'s lesson), never on a tree-wide string count.**

### 🔴 The informed gap this pass declares rather than leaves silent — Spanish

🟢 **`Gap 235` covered Portuguese **and Spanish**. The Portuguese half is answered. The Spanish half was
searched this pass and is **negative**, which is recorded here so that silence is not read as coverage.**

Query run: `corrector automático ensayos español código abierto licencia MIT github`. 🔴 **No
open-source essay *scorer* for Spanish.** What the channel returns instead is the **orthography and
grammar** tier — `BrayanZambranoDev/AI-Text-Corrector` (README declares MIT; 🔴 **payload not read this
pass, so unverified here**), `gmiguelgosuna/Corrector-espanol` (hosted third-party API),
`ZethAlvarez01/TT-R-20-1-006` (Flask prototype) — 🔵 **all of which correct text and none of which
*grades* an essay against a rubric.**

🔵 **Why the asymmetry with Portuguese is real and not a query artefact:** Brazil has **one national
essay-graded exam with a published five-competency rubric (ENEM)**, which creates both a corpus and a
community. 🔴 **Spanish-speaking LATAM has no single equivalent instrument**, so there is no one rubric
to standardise on. 🟢 **That makes the Spanish gap structural, and it changes the remedy: for Spanish the
first artefact is a **rubric and a graded corpus**, not a model.** See `Gap 237`.

## 🟢 Forty-first pass, 2026-10-07 — three trends: permissive code over non-permissive intelligence, a registry channel that confirms packages that do not exist, and the agent shelf declared **saturated** rather than unmeasured

⏱️ **Eighth pass of this date.** 🔵 **All market figures below are secondary and carry their series
(`P477`, and now `P515`'s stricter rule: base year, scope definition and publisher, or do not quote).**

### T1 🔴 `P516` — in the essay-scoring tier the licence is permissive and the **intelligence** is not, and the one dead end is the only thing that was ever fully open

🔵 **This KB had no row in the automated-essay-scoring tier. This pass measured it, and the result is a
shape worth naming because it will recur across every LLM-era education tier.**

| Asset | Licence (payload · bytes · title block) | Existence (`P510`) | 🔴 What it actually gives you |
|---|---|---|---|
| [`edx/ease`](https://github.com/edx/ease) — the historical reference implementation | 🔴 **AGPL-3.0** · `master/LICENSE.txt` **35,136 B** · `GNU AFFERO GENERAL PUBLIC LICENSE Version 3` | 🟢 refs served | 🟢 **A complete, self-contained scoring model** — classical ML, trains on your own graded corpus, no external call. 🔴 **AGPL-3.0 and archived 2024-02-28.** 🔵 **Fully open, fully yours, and dead** |
| 🆕 [`markm-io/ai-essay-evaluator`](https://github.com/markm-io/ai-essay-evaluator) **1.3.7** (2026-06) | 🟢 **MIT** · `main/LICENSE` **1,069 B** · `MIT License` | 🟢 `main` served | 🔴 **A harness.** Multiple scoring formats, batch processing, custom training — 🔴 **around a fine-tuned OpenAI `GPT-4o-mini`.** 🟢 **The MIT grant is real and covers everything that was written; none of what *scores* is in it** |
| `AIRGOLAB-CEFET-RJ/textgrader` (LATAM-origin) | 🔴 **no licence payload on `main`, `master` or `develop`** | 🔴 **0 refs — does not resolve** | 🔴 **Nothing retrievable.** See `P517` |

> **`P516`.** 🔴 **The tier inverted between 2024 and 2026: the fully-open option is archived, and the
> live option is permissively-licensed scaffolding over a proprietary model.** 🔵 **"MIT" has stopped
> answering the question a studio actually needs answered**, which is not *may I modify this?* but
> **where does the judgement live, and can the client keep it?** 🟢 **Three consequences, and they are
> procurement consequences rather than engineering ones:**
>
> | | |
> |---|---|
> | 🔴 **Per-score marginal cost** | A classical model has none after training; an API harness has one per essay, forever, priced by a third party |
> | 🔴 **Scoring cannot be frozen** | 🔵 **An exam board must defend *this year's* marks against *last year's*. A provider that silently updates a model breaks comparability** — and the MIT harness gives no mechanism to pin it |
> | 🔴 **Annex III lands on the judgement, not the wrapper** | 🟢 **2027-12-02 covers *exam scoring* (`P514`). The evidence obligations attach to whatever decides the score** — which, here, the client does not possess |
>
> 🟢 **The honest recommendation: use `ai-essay-evaluator` as a *rubric and harness* reference and treat
> the scoring model as replaceable from day one.** 🔵 **`edx/ease`, AGPL and archived, remains the only
> implementation in this tier that a client could fully own — so it is worth reading as a specification
> even though it cannot be shipped.** ⚠️ **AGPL-3.0: reading and reimplementing is not copying, and no
> pass of this KB has had counsel read any of this.**

### T2 🔴 `P517` — `pypi.org/project/<name>/` returns **200 for packages that do not exist**, so "URL verified" on that channel is not evidence of anything

🔴 **Reported against this pass's own verification step, before anything was written.** The instruction
this KB runs under says *verify every URL; a 404 is not a finding*. 🔴 **This pass's verification pass
returned `200` for two fictional packages:**

| URL | HTML channel | 🟢 JSON API `pypi.org/pypi/<name>/json` | Truth |
|---|---|---|---|
| `pypi.org/project/EqUMP/` | 🟢 200 | 🟢 **200**, 26,427 B | 🟢 **Exists** — `info.license = 'MIT'`, v0.3.6 |
| `pypi.org/project/pronounce-assess/` | 🟢 200 | 🟢 **200**, 6,611 B | 🟢 **Exists** — v0.1.0 |
| 🔴 `pypi.org/project/NOTAREALPKG-zzz9/` (control) | 🔴 **200** | 🟢 **404**, 24 B | 🔴 **Does not exist** |
| 🔴 `pypi.org/project/definitely-not-a-package-xyz987/` (control) | 🔴 **200** | 🟢 **404**, 24 B | 🔴 **Does not exist** |

> **`P517`.** 🔴 **An HTTP `200` from `pypi.org/project/…` is worthless as an existence check here — it is
> returned for arbitrary names.** 🟢 **The JSON API discriminates perfectly against two independent
> negative controls and additionally returns the licence, so it is strictly better: one request, sound
> existence, machine-readable licence.** 🔵 **This completes a set with `P510` (use `git ls-remote`, not
> `github.com` HTML) — **in both cases the human-facing HTML surface is unreliable in this environment
> and the machine-facing channel is sound.** 🟢 **The general rule for later passes: verify against the
> channel that is *built* to answer the question, and prove it on a negative control in the same run.**

🟢 **A second, smaller licence-channel finding from the same probe, worth recording because it will cause
a false negative otherwise:**

| Package | `info.license` | `info.license_expression` | Verdict |
|---|---|---|---|
| `EqUMP` 0.3.6 | 🟢 `'MIT'` | `None` | 🟢 MIT |
| `pronounce-assess` 0.1.0 | 🔴 **`None`** | 🟢 **`MIT`** | 🟢 **MIT** |

🔵 **The legacy `license` field is empty on a package that is plainly MIT; the **PEP 639**
`license_expression` field carries it.** 🔴 **A probe reading only `license` would have recorded
`pronounce-assess` as unlicensed — the same false-negative class as `P494`, in a new field.** 🟢 **Read
`license`, `license_expression` **and** the `License ::` classifiers, and treat absence across all three
as "undetermined", never as "unlicensed".**

### T3 🟢 The education **agent** shelf is saturated at the permissive end — a conclusion, not a shrug

🔵 **Three passes reported "zero new agents" and `P497` attributed it to the search string.** 🟢 **`P512`
(`agents/trending.md`) shows a job-shaped query returns four real tutoring agents on the first attempt —
`OATutor`, `OpenTutor`, `DeepTutor`, `TutorGPT` — of which three were already shelved and the fourth is
**GPL-3.0**.**

| | Permissive | Copyleft |
|---|---|---|
| **Mastery-model tutoring** | 🟢 `OATutor` (MIT) — Bayesian Knowledge Tracing | — |
| **Agentic / lifelong tutoring** | 🟢 `DeepTutor` (Apache-2.0) · `OpenTutor` (MIT) | — |
| 🆕 **Theory-of-Mind tutoring** | 🔴 **none** | 🔴 **`tutor-gpt` (GPL-3.0)** |
| **Learner modelling** | 🟢 `pyKT` · `pyBKT` (MIT) | — |
| **Pronunciation / speech** | 🟢 `OpenPronounce` (MIT) · `pronounce-assess` (MIT) | — |
| **Essay scoring** | ⚠️ `ai-essay-evaluator` (MIT harness, proprietary model — `P516`) | 🔴 `edx/ease` (AGPL-3.0, archived) |

🟢 **What follows from saturation is a change of activity, and it is the actionable trend of this pass:**

| 🔴 Stop | 🟢 Start |
|---|---|
| Sweeping for undiscovered permissive education agents | **Composing the four that exist** (`compose/patterns.md`) |
| Treating absence as "not yet found" | 🟢 **Treating the two *named* holes as a build list**: a permissive Theory-of-Mind layer (`tutor-gpt` is the spec), and a permissive observed-score/kernel equating port (`KernEqWPS` is the spec and the oracle — `P508`, Gap 234) |
| Quoting market totals | 🔵 **Quoting the regulatory calendar** — it is dated, checkable, and `P514` shows the market is getting it wrong |

### 🔴 `P517`'s sibling gap — the LATAM-origin asset that could not be shelved

> 🔴 **Gap 235 (new).** 🔴 **`AIRGOLAB-CEFET-RJ/textgrader` — a Portuguese-language essay-and-short-answer
> grader from CEFET-RJ, and the only LATAM-origin asset the essay-scoring sweep surfaced — has an
> **unresolvable repo path**: `0` refs from `git ls-remote`, matching the negative control, and no licence
> payload on `main`, `master` or `develop`, although a search result hyperlinks it as a repository.** 🟢
> **Recorded as a declared gap rather than a finding, and deliberately not hyperlinked (`P501`).** 🔵 **Why
> it matters out of proportion to one repo: every permissive asset in the tier above scores **English**.
> A Portuguese or Spanish essay scorer is the single most region-specific gap in this KB's LATAM
> coverage, and this pass could not confirm that one exists at all.** 🟢 **Next pass: query the
> Portuguese-language corpus directly (`corretor automático de redação código aberto`), and check whether
> CEFET-RJ publishes under a different organisation name — a renamed org is the most likely explanation
> for a live search result pointing at a dead path.**

## 🟢 Fortieth pass, 2026-10-07 — three trends: the comparability tier starts migrating to permissive Python, query *shape* beats query *topic*, and a stale regulation date proves reproducible

⏱️ **Seventh pass of this date.** 🔵 **All market figures below are secondary and carry their series
(`P477`).**

### T1 🟢 The comparability tier is **migrating from GPL R to MIT Python**, and that changes what Globant can sell rather than merely what it can read

🔵 **Pass 39 established the tier's licence topology and explained it:** calibration grew up in Python/ML
so it is permissive; comparability grew up in R/CRAN so it is GPL (`P493`). 🟢 **This pass measured eight R
packages and found 8 / 8 GPL — the mechanism is confirmed, not weakened.** 🔴 **What pass 39 could not see
is that the tier is being re-implemented:**

| | Calibration tier | Comparability tier, pass 39 | 🆕 Comparability tier, pass 40 |
|---|---|---|---|
| Permissive **Python** | 🟢 `py-irt` · `irtorch` · `girth` — MIT | 🔴 **none** | 🟢 **`EqUMP` — MIT** |
| Permissive **Java** | — | 🟢 `psychometrics` — Apache-2.0 | 🟢 unchanged |
| Copyleft **R** | — | `equate` GPL-3 | 🔴 **8 / 8 GPL, measured** |

🟢 **The consequence is commercial, not academic.** 🔵 **An **R/GPL** comparability layer can only be a
side-car: a separate process, invoked over a boundary, with its own distribution obligations.** 🟢 **A
**Python/MIT** layer is an **in-product component** — it imports into the same service as the calibration
tier that is already MIT.** 🔴 **The caveat that keeps this honest: `EqUMP` implements **linking** and
**true-score equating** only. `equating/kernel/`, `equating/obs/` and `scoring/` are declared and empty
(`P500`), so **observed-score and kernel equating remain R-only and GPL-only**.**

### T2 🟢 `P503` — on a saturated shelf, the productive variable is query **shape**, not query **topic**

🔴 **The evidence is this KB's own two measurements of the same subject, one pass apart:**

| Query | Shape | Returned |
|---|---|---|
| `equating` · `test equating` · `equiparación` | **topic alone** | 🔴 **0** — recorded at `repos/foundations.md` by pass 39 |
| `top open source AI agents education 2026 github MIT` | **topic + year + licence**, but topic is a *homonym* | 🔴 **0 education agents**, three passes running (`P497`) |
| 🆕 `Python test equating library MIT Apache permissive item response theory linking` | 🟢 **topic + language + licence + method** | 🟢 **`EqUMP`** — the one permissive implementation in the tier |

> **`P503`.** 🔵 **`P497` showed a topic word can fail by returning a *homonym class*. This pass shows the
> complementary case: a topic word can fail by being **too short to discriminate**, and the fix is to add
> the axes the KB actually cares about — **language** and **licence** — to the query itself.** 🟢 **Those
> are the two columns every row of this KB carries, so putting them in the query aligns the search with the
> shelf.** 🔴 **Stated with its limit: this is one success against one prior failure on one subject.** 🔵 **It
> is a hypothesis with a cheap test — any later pass can run the bare topic and the shaped topic
> side by side and record both, which is what this pass did.**

🔴 **The mandated sweeps are not thereby excused.** They are run every pass and recorded in full in
`agents/trending.md`; `P503` is an argument for running **additional** shaped queries, never for
substituting them.

### T3 🔴 `P505` — a regulation date can be **reproducibly** wrong in a channel, and this KB has regressed on this exact date once already

🟢 **The only Annex III education date this KB may write is `2027-12-02`.** 🔴 **The mandated EMEA sweep
returned `2026-08-02` again this pass** — the pre-**Digital Omnibus** date, superseded by a **16-month**
deferral whose stated rationale was that **harmonised standards were not ready**.

| Obligation | Date | Moved? |
|---|---|---|
| **Annex III stand-alone high-risk** — education and assessment named explicitly | 🟢 **2027-12-02** | 🔴 **Yes, from 2026-08-02** |
| **Annex I embedded** high-risk | **2028-08-02** | 🔴 Yes, from 2027-08-02 |
| 🟢 **Article 50 transparency** | 🟢 **2026-08-02** | 🟢 **No** |

🔵 **Why the error is attractive rather than obvious: `2026-08-02` is still a real, live AI Act date — it
is Article 50's.** 🔴 **So a stale source is not quoting a dead date; it is attaching a live date to the
wrong obligation**, which no date-plausibility check catches. 🟢 **The underlying obligations did not
change — only the date non-compliance bites.** ⚠️ **Attribution limit, stated: the page carrying the stale
claim (`planbe.eco`) is `EGRESS_BLOCKED` here, so the stale assertion is attributed to the **search-summary
layer** and not quoted from a page this pass could open. `eur-lex.europa.eu` has been unreachable since
pass 32, so the primary text is still unread.**

### 🔵 Trend table — what moved, what did not

| | Pass 39 | 🆕 Pass 40 |
|---|---|---|
| Permissive equating implementations | **1** (Java) | 🟢 **2** (Java + Python) |
| Permissive **observed-score** equating | 🔴 0 | 🔴 **0 — unchanged (`P500`)** |
| R comparability packages measured | 1 | 🟢 **8, all GPL** |
| New education **agents** | 0 | 🔴 **0 — third consecutive** |
| `P480` fixture gate | blocked (3rd) | 🔴 **blocked (4th), same cause** |

---

## 🟢 Thirty-ninth pass, 2026-10-07 — five trends: comparability overtakes calibration as the defensible claim, and a KB learns that writing a control down is not running it

⏱️ **Sixth pass of this date.** 🔵 **All market figures below are secondary and carry their series
(`P477`); the 2026 global range across five published series is now **$8.98 B – $12.3 B** — see
`intel/market.md`.**

### T1 🟢 The defensible unit moves one step further: from the **score**, past the **measurement claim**, to the **comparability claim**

🔵 **Pass 38 called this shift correctly and stopped one step short.** It said the defensible unit is a
*measurement claim* — difficulty, discrimination, standard error — rather than a score. 🔴 **A measurement
claim about a single form is not yet defensible, because the regulator's question is comparative.**

| Question asked | Answered by | Held by this KB since |
|---|---|---|
| *"What did the student score?"* | the grader | pass 1 |
| *"On what basis is the score a measurement?"* | item parameters — IRT calibration | 🟢 **pass 38** |
| 🔴 *"On what basis is **this** score comparable to **that** one?"* | 🆕 **linking / equating** | 🟢 **pass 39** |
| 🔴 *"Comparable **for whom**?"* | 🆕 **differential item functioning** | 🟢 **pass 39** |

🔴 **The technical correction that drives the whole pass:** two forms calibrated independently carry
parameters on **two different scales**, because IRT fixes the metric only up to a linear transformation.
🔵 **So pass 38's recipe `P491`, which promised to *"prove two exam variants are equivalent"*, compared
numbers in mismatched units.** 🟢 **`P496` installs the missing link — anchor items plus a Stocking-Lord
transformation — and restates the claim to what the evidence supports.**

🟢 **And the claim, stated properly, is unusually strong for a sales conversation:** *"the two variants are
on a common scale, their difficulty difference is X logits ± SE, and no item shows DIF above ETS class B
for any reported subgroup."* 🔴 **No LLM-centric pitch can produce that sentence**, which is precisely why
it is defensible.

### T2 🔴 `P498` — a knowledge base can **write down a control and not run it**, and the written rule reads exactly like a solved problem

🔴 **Pass 38's headline finding was `P483`: a reset had dropped the open-gap register into `archive/`, so
twelve passes could not see a gap that pass 25 had already identified and priced.** 🟢 **The rule it wrote
is correct:** *"A reset or re-scope must carry forward the open-gap register as live content."* 🔴 **Pass
38 did not carry it forward.** Measured this pass: the live tree contained **no** gap register, and the
only reachable copy was still the archive path pass 38 had quoted.

🔵 **So the gap `P483` described remained open for one more pass — while the KB's own text asserted the
remedy.** 🟢 **This pass created `intel/open-gaps.md`**: 40 bold-declared gaps recovered from the eight
archived files, each with its archive `file:line`, bucketed **12 open / 5 status-undeterminable / 23
closed** by a mechanical read of the declaring line — 🔵 **explicitly a reachability index, not a
re-adjudication.**

🔴 **And the cost of the un-run control was immediate and measurable, not hypothetical.** `Gap 39`'s
declaring line has **two halves**; pass 38 quoted the **last sentence** and closed the gap on it:

| | `P483` (pass 38) | 🆕 `P498` (this pass) |
|---|---|---|
| The failure | a gap that was true went **uncollectable** | the **remedy was recorded as done** when it was only specified |
| How it reads | *"no pass could see it"* | 🔴 *"the rule is in the file"* — 🔵 which is worse, because it **stops the next pass from checking** |
| What it cost | 12 passes of unrealised work | 🔴 **`Gap 39` closed at half** — `P492` |
| The control | carry the register forward | 🆕 **execute the control in the same pass that prescribes it, or label it a TODO with an owner** |

> 🔵 **Generalised, because Globant ships this shape constantly.** 🔴 **A documented control is not a
> control.** An audit finding, a runbook step, a governance policy — each is a *specification* until
> something executes it, and the document is indistinguishable from a solved problem on every later read.
> 🟢 **The practical rule: a finding that prescribes an action must either perform it or carry an explicit
> `NOT DONE` marker with an owner.** 🔵 **`P480`'s fixture debt on this very shelf is the same shape, now
> three passes old** — and `agents/top.md` records this pass's decision not to let silence stand in for a
> third denial.

### T3 🔴 Comparability tooling is jurisdiction-neutral, so the regional story is **who is obliged**, and it inverts the usual ranking

🟢 **A linking transformation and a Mantel-Haenszel statistic are mathematics: no locale, no curriculum, no
jurisdiction.** 🔴 **`P474` fired again this pass and had to be enforced twice** — `difair` and `aequitas`
have North-America-affiliated authors, `difR` is maintained from Belgium and `difNLR` from Czechia, and
**none of them is recorded as a regional row.** 🔵 **All four regional searches returned zero
region-specific open-source assessment-fairness tooling; the gap is declared, per region, in
`repos/foundations.md`.**

🔵 **The useful regional question is therefore which regulator makes auditable comparability mandatory, and
the answer inverts the market ranking:**

| Region | What makes comparability evidence required | Clock | 🔵 Commercial shape |
|---|---|---|---|
| **EMEA** | 🔴 **Strongest.** Annex III high-risk + Annex IV accuracy/robustness + bias examination | 🔴 **Disputed** — "full effect August 2026" vs the Omnibus deferral to **2027-12-02**; `eur-lex` unreachable, so build to the **earlier** date | 🟢 **Compliance sale** |
| **North America** | 🟡 **No statute — but decades of professional practice.** DIF is already standard in US large-scale testing; 134 bills / 31 states | 🟡 Now, by procurement language rather than law | 🟢 **Easiest sale**: the requirement is pre-agreed, only the permissive on-premise *how* is new |
| **APAC** | 🔴 **Weakest obligation, largest volume.** Compulsory curricula (China age 6, India Class 3) but no regime names item-level fairness evidence | 🔴 Not scheduled | 🟢 **Ministry-scale build**, not compliance |
| **LATAM** | 🔴 **Obligation absent; capacity is the binding constraint.** <10% of institutions have guidelines | 🟡 Brazil PL 2.338/2023 still in the Chamber | 🟢 **Instrument + policy**, anchored to UNESCO's LAC observatory and the new IADB framework |

🔴 **The asymmetry worth saying out loud: the region with the heaviest obligation (EMEA) has the least
assessment volume, and the region with the volume (APAC) has the lightest obligation.** 🟢 **`P496` needs
~500 responses per item, so the technically easiest deployments and the commercially most urgent ones are
in different hemispheres.**

### T4 🔴 Licence topology is a property of the **tier**, and this is the trend-level reading of `P493`

🟢 **Pass 38 concluded of the assessment chain: *"all four permissive, no copyleft anywhere."*** 🔴 **One
tier down, the ratio reverses: of the eight comparability implementations this pass measured, **six are
GPL or LGPL**, one is unlicensed, and the permissive options number **exactly one per capability**.**

🔵 **The cause is ecosystem lineage, not education.** Item *estimation* grew up in Python/ML, where
MIT/Apache are the defaults; item *comparability* grew up in **R/CRAN**, where GPL is the default. 🟢 **So
the licence profile of a capability is predictable from the community that built it**, and that is a
reusable heuristic rather than an education fact:

| If the capability's reference implementations are… | Expect | 🔵 Plan for |
|---|---|---|
| Python / ML-lineage | 🟢 MIT · Apache-2.0 | in-product |
| 🔴 **R / CRAN / academic-statistics lineage** | 🔴 **GPL · LGPL** | 🟡 **side-car, or a single permissive outlier carrying the whole tier** |
| Java / enterprise-2010s lineage | 🟡 Apache-2.0 — 🔴 **often with no `LICENSE` file at all** (`P494`) | read **source headers** |

🔴 **The deliverable risk this creates is concentration, not copyleft.** 🟢 **There is one permissive DIF
library and one permissive equating library in existence as far as this pass can measure**, and one of
them is **v0.7.0 and not on PyPI**. 🔵 **That is a single-point-of-failure sentence a client should hear in
the first conversation**, with the mitigation attached: pin the SHA, vendor it, keep the GPL reference
implementation as an offline validation oracle.

### T5 🔴 On a saturated vertical shelf, the topic-word query is the bottleneck — and it fails by returning a **homonym class**

🔴 **Two consecutive passes have added zero agents, and this pass measured why rather than calling it
saturation.** 🔵 **`P497`:** both mandated sweeps — `top open source AI agents education 2026 github MIT`
and `github trending education AI 2026` — returned **AI pedagogy**: horizontal agent frameworks
(`openclaw`, `CrewAI`, `LangGraph`, `dify`) and material that **teaches AI to humans**
(`ai-engineering-from-scratch`, Karpathy's *Zero to Hero*, an AI/ML jobs list).

| The query asks for | The corpus optimises for |
|---|---|
| 🟢 software **for** schools — tutors, graders, LMS connectors, item banks | 🔴 material **about** AI, for learners |

🟢 **Every finding of substance this pass produced came from a query containing neither the word
*education* nor the word *AI***: *"what makes two calibrated tests comparable?"* 🔵 **That is the
generalisable move for any mature vertical KB — stop naming the industry and start naming the **layer of
the delivery chain** whose absence you can measure first.** 🔴 **A pass that runs only the topic sweeps
will correctly report saturation and find nothing, indefinitely.**

---

## 🟢 Thirty-eighth pass, 2026-10-07 — five trends: scoring becomes a measurement claim, and a KB can lose a gap it already paid for

⏱️ **Fifth pass of this date.** 🔵 **All market figures below are secondary and carry their series
(`P477`): never divide a figure from one series by a figure from another.**

### T1 🟢 The defensible unit of AI assessment is shifting from the *score* to the *measurement claim*

🔵 **Thirty-seven passes of this shelf have tracked agents that produce and grade items.** 🔴 **None of
them can answer the question a regulator actually asks: *on what basis is this score comparable?***

The EU AI Act classes **student evaluation and exam scoring** as high-risk, and the obligation that
bites is not "a human reviewed it" but **accuracy, robustness and documented performance**. 🟢 **Those
are psychometric properties, not LLM properties.** An item's **difficulty**, **discrimination** and the
**standard error** of an ability estimate are the evidence; a rubric and a transcript are not.

🔴 **The practical consequence, and it inverts a common pitch.** "Our AI generates infinite practice
variants" is a **liability** under a high-risk regime unless variant **equivalence** is measured —
without it, two students sitting different variants received different tests, and the grades are not
comparable. 🟢 **With a calibration layer it becomes the strongest possible answer**: the variants are
equivalent *to a stated tolerance*, and here is the item-parameter table.

🟢 **And this is now buildable entirely permissively** — `py-irt` (MIT) or `irtorch` (MIT) for
calibration, `catsim` (BSD-3) for adaptive selection, on top of the MIT QTI chain this KB already held.
🔵 **See `P491` in `compose/patterns.md`, and the tier in `repos/foundations.md`.**

### T2 🔴 A knowledge base can lose a gap it has already paid to identify — and losing it is worse than never having it

🔴 **This pass's largest finding is about this repository.** `Gap 39`, opened at **pass 25**, named the
missing item-calibration layer, priced it (*"acotado y construible"*) and prescribed the remedy
(*"calibrar con una librería IRT de Python"*). 🔴 **The `2026-10-06` reset left it in `archive/` and it
appears nowhere in the live tree.** Twelve passes ran without being able to see it.

🔵 **The asymmetry is what makes this a trend and not a bookkeeping note.** A **fact** that falls out of
a KB gets rediscovered by the next sweep that touches the topic — facts are in the world. 🔴 **A *gap*
is not in the world. It is an inference the KB made about its own coverage**, so when the record goes,
the inference is not recoverable by searching harder: nothing out there contradicts it, and no sweep
returns it.

🔴 **`P469` and `P483` are the two ways this fails, and they are opposites:**

| | `P469` (pass 35) | 🆕 `P483` (this pass) |
|---|---|---|
| The claim | a gap that was **false** | a gap that was **true** |
| The failure | asserted for 3 passes, disproved by the KB's own shelves | **archived**, so no pass could act on it |
| What it cost | credibility — a deliverable would have said "nothing exists" | **12 passes of unrealised work**, already identified and priced |
| The control | probe the shelf before declaring | 🆕 **carry the open-gap register forward through any reset** |

> 🔵 **Generalised beyond this KB, because Globant ships this shape to clients.** Any knowledge asset
> with a **lifecycle** — a re-scope, a migration, a reset — must treat its **open questions** as
> first-class content with the same migration guarantee as its answers. 🔴 **Deliverables migrate the
> conclusions and drop the register of what was known to be missing**, which is precisely the part the
> next engagement needs.

### T3 🔴 Measurement libraries are jurisdiction-neutral, so the regional story is regulatory, not geographic

🟢 **An IRT estimator is mathematics: it has no locale, no curriculum and no jurisdiction in its domain
model.** 🔴 **Which means the usual regional-placement move does not apply, and `P474` fired on this pass
to stop it** — `catsim`'s author publishes from a `.com.br` domain and the pass nearly recorded a
**LATAM** placement on the strength of a hostname.

🔵 **The right question is not where the library was written but which regulator makes auditable
measurement mandatory, and the answer differs sharply:**

| Region | What makes calibration a requirement | Clock |
|---|---|---|
| **EMEA** | 🔴 **EU AI Act high-risk**: assessment, admissions, proctoring. Accuracy + robustness documentation | 🟡 **deferred to 2027-12-02** (July 2026 AI Omnibus) — but **Art. 4 AI-literacy has applied since 2025-02-02** |
| **APAC** | 🔴 **Already binding in places.** Korea's Basic AI Act provisions from **H2 2026**; China's GenAI Measures operationally enforced since 2023 | 🔴 **now** |
| **North America** | 🟡 **State-level and specific**: human-oversight and no-high-stakes-AI-decisions rules (Oklahoma, Maryland) make the *measurement* the defensible artefact | 🟡 **live, fragmented** |
| **LATAM** | 🟡 **Brazil PL 2.338/2023** risk-based, in the Chamber of Deputies — text can still change | 🟡 **pending** |

🔵 **So the same MIT library is a compliance asset on four different timetables.** 🟢 **EMEA's deferral
is the window, not the reprieve**: a system calibrated now is evidence-ready in 2027 at no extra cost,
whereas retrofitting calibration onto a deployed grader means re-running every item.

### T4 🟢 Open source licence risk has moved from the *licence* to the *dependency named in prose*

🔵 **Passes 33–37 hardened this KB against licence misreads — payload over prose, title block over body,
two channels over one.** 🔴 **This pass's trap defeated all of it and was perfectly visible in a README.**

`hicsail/opencat-pro` serves a **1,106-byte MIT** payload, classifies cleanly, and says in its own
`README`: *"The UI framework is based on Accessible+. **A valid license is required to use this in
production.**"* 🔴 **Every licence control this KB owns returns `OK`, and the platform is not shippable.**

| Generation of risk | Example | What catches it |
|---|---|---|
| Wrong licence claimed in prose | `formalms` Apache claim (`P470`) | 🟢 read the payload |
| Wrong family from body tokens | Sakai ECL→Apache (`P476`), GPL §6 (`P250`) | 🟢 title-block classification |
| Registry name held by the ungranted twin | `moodle-mcp` (`P482`) | 🟢 back-resolution |
| 🆕 **Permissive repo, non-free vendored asset** | `opencat-pro` (`P486`) | 🔴 **nothing automated. Read the README's licence section** |

🔵 **The pattern across generations: as licence *metadata* gets more reliable, the residual risk moves
into the parts that were never metadata.** 🔴 **For a platform, "what licence is this repo?" has become a
less useful question than "what does this repo not contain?"**

### T5 🔴 On a saturated shelf, discovery stops paying and *chain completion* starts

🟢 **Measured this pass: 1,087 distinct slugs on the roster; four broad discovery searches; zero new
usable agents.** Every candidate the general channels produced was already held.

🔵 **Meanwhile two narrow searches aimed at a *missing link* rather than a trend produced eight
permissive rows and a complete delivery chain.** 🔴 **The difference was not effort or luck — it was the
question.** "What is trending in education AI" samples the same popular surface every pass. "What does
the assessment chain still lack" interrogates the KB's own structure.

🔵 **The market data agrees with the method.** Capital in the sector fell while structural adoption rose
(pass 34, `T5`), and the agentic shift is described by every 2026 series as moving **from experiment to
deployment**. 🟢 **In a deployment market the scarce input is not another agent — it is the one component
that makes an existing agent defensible.** 🔴 **A studio that keeps cataloguing tutors is cataloguing the
abundant half.**

> 🔵 **Operational form of this trend for Globant.** Audit a client's intended chain link by link and
> find the link with **no permissive option**. That link is the engagement: it is where the client
> cannot self-serve from GitHub, and on this shelf it has twice been **measurement** rather than
> generation.

## 🟢 Thirty-seventh pass, 2026-10-07 — five trends: the tutor becomes a classroom, and local inference stops being the fallback

⚠️ **T1, T2 and T4 rest on payload-verified repositories measured this pass. T3 and T5 mix payload
evidence with secondary sources, and every market/regulatory domain cited is blocked from this
environment (`000`), `eur-lex.europa.eu` included.** The distinction is load-bearing and belongs in any
deck built from this file.

### T1 🔵 The binding axis has three values, not two — and the third one changes who owns the asset

Pass 36 established that the tutor is becoming **jurisdiction-shaped**: `bandup` marks Singapore PSLE
and A-Level GP against *those papers'* band descriptors; `MathTutor` targets India's JEE;
`lesson-plan-parse-mbsse` encodes Sierra Leone's national lesson plans. 🟢 **This pass adds the
counter-example that forces a second axis**, and it is not a weaker case — it is a different
architecture:

| Asset | Binding | Where the rubric lives |
|---|---|---|
| `bandup` (MIT) · `MathTutor` (MIT) | 🟢 **Jurisdiction** — PSLE /40, A-Level GP /50, JEE | 🔴 **Encoded in the repo** |
| 🆕 `SaadRahman01/moodle-mcp` (MIT) | 🟢 **Platform** — Moodle's Hooks API, capabilities, XMLDB, WS surface | n/a — the *platform contract* is the binding |
| 🆕 `laurauguc/grading_assistant` (MIT) | 🟢 **Nothing** — rubric-agnostic | 🟢 **Uploaded by the teacher at runtime** |

🔵 **The three shapes sell completely differently, and conflating them is how an engagement gets
mispriced.**

- **Jurisdiction-bound** → the differentiator is the **rubric encoding**, the client owns it, and it
  cannot be handed to a vendor's cloud. The scaffolding is commodity.
- **Platform-bound** → the differentiator is **surviving the platform's upgrade cycle**. `moodle-mcp`
  is explicit about this: *"hardened to survive site redesigns"*, version-filtered docs, Jira tracker
  search. 🔵 **This is a maintenance product, not a model product.**
- **Rubric-agnostic** → 🔴 **there is no moat, and that is the point.** `GradeMate` takes any rubric as
  an upload, which makes it the right **pilot** vehicle — fastest path to a teacher using it — and the
  wrong **platform** bet.

🟢 **The sequencing this implies: pilot rubric-agnostic, productise jurisdiction-bound, price
platform-bound as a retainer.**

### T2 🟢 The unit is shifting from the tutor to the classroom, and the new artefact is the peer

🆕 **`THU-MAIC/OpenMAIC` (MIT, Tsinghua MAIC) is not a better tutor — it is a different unit.** AI
**teachers and AI classmates** that speak, draw on a shared whiteboard, and hold real-time discussion;
one click turns a document into slides, quizzes, interactive simulations and project-based activities.

🔵 **The AI *classmate* is the genuinely new object here, and it is pedagogically load-bearing rather
than decorative.** A 1:1 tutor can only model expert→novice transfer. A simulated cohort can carry
peer explanation, disagreement and group work — the mechanisms that 1:1 tutoring structurally cannot
reproduce, and that the **0.3–0.5 SD** tutoring effect size is measured *against* rather than on top of.

🔴 **The honest caveat: no evaluation of the classmate mechanism is verifiable from here.** The
`JCST'26` paper (`10.1007/s11390-025-6000-0`) is real as a citation and **unreadable in this
environment** — `arxiv.org` and `aclanthology.org` are `000`. 🔵 **So shelve `OpenMAIC` on its
**architecture and licence**, which are payload-verified, and treat the learning-outcome claim as
unverified until a reachable channel exists.**

### T3 🟢 Local inference has stopped being the degraded fallback and become the compliance feature

Three independent assets, three regions, same architectural choice:

| Asset | Local path | Posture |
|---|---|---|
| 🆕 `OpenMAIC` (APAC) | **Lemonade** local inference + **FunASR** local ASR | 🟢 **the whole classroom runs on-premise** |
| `bandup` (APAC, pass 36) | **Ollama**, no telemetry | 🔴 **persistent warning when a non-local model is selected** |
| `Kolibri` (MIT) | offline-first by design | 🟢 **assumes intermittent connectivity as the normal case** |

🔵 **What changed is that regulation now pays for this, in all four regions at once** — and it is the
rare case where the compliant architecture is also the cheaper one at scale:

- 🔴 **California AB 1159** forecloses training on student data outright — the "we improve the model
  on your data" clause is simply unavailable.
- 🔴 **Korea's AI Basic Act** (in force January 2026) names **education** high-impact; **Japan and
  Korea** mandate student-data encryption with penalties.
- 🔴 **EU AI Act** high-risk duties — data governance and human oversight — applicable since **2 Aug
  2026**.
- 🔵 **LATAM**: <10% of institutions hold formal guidelines, so **"the data never leaves" is the
  policy**, delivered as architecture instead of paperwork.

🟢 **The consequence for a proposal: "runs on your infrastructure" moved from a concession you make on
price to the clause that wins the deal.**

### T4 🔴 Education's open source frontier is copyleft — and the most AI-native entrants carry the strictest terms

Measured from payload this pass, by tier: 🟢 **exactly one permissive option each** — `OpenOLAT`
(Apache-2.0) for LMS, `OSSS` (Apache-2.0, immature) for SIS, `Kolibri` (MIT) for offline — against
**Moodle GPL-3.0, RosarioSIS GPL-2.0, OpenEduCat LGPL, Sakai and Opencast ECL-2.0, and Canvas, Open
edX and 🆕 ClassroomIO all AGPL-3.0**.

🔴 **The direction of travel is the problem.** `ClassroomIO` is the newest, most explicitly AI-native
LMS on these shelves — it ships its own MCP server — and it is **AGPL-3.0**, the one licence whose
obligation fires on **operating** the software rather than shipping it. 🔵 **So the entrants most
attractive to an AI engagement are arriving under the terms least compatible with hosting one.**

🟢 **And `ClassroomIO` shows the shape the market is settling into: an MIT integration layer
(`@classroomio/mcp`, verified on npm) bolted to an AGPL core.** 🔵 **Two licences, two conversations —
and a deck that names only the permissive half is describing the adapter, not the platform.**

### T5 🔴 In agentic education, capability without a grant is the normal state — and the grant is the scarce input

**4 of 10 repositories probed this pass serve no licence payload at all**, every one of them real and
actively committed: `StudyMate` (LangGraph + Gemini + RAG + SQLite, diagnostic assessment and
replanning), `mcp-canvas-lms`, and **both** agentic curriculum-and-rubric generators
(`AI-Powered-Adaptive-Curriculum…`, `EduAgent`).

🔵 **The clustering is the signal, not the count: the niche closest to what clients ask for —
"generate the curriculum, the assignments and the rubric, then grade against it" — is precisely the
niche where nothing carries a licence.** 🔴 **For this KB that is a sourcing dead end, not a
shortlist.** A README cannot be built on.

🟢 **Which is why the regulatory convergence matters more than it looks.** OECD and EDUCAUSE 2026 both
find **AI-assisted grading outperforms fully autonomous grading**; NA states bar machine-emitted
high-stakes decisions outright (**NYC's Red list: grading, discipline, promotion, surveillance**); the
EU classifies exam scoring as high-risk. 🔵 **So the unlicensed cluster is chasing full autonomy — the
capability that is simultaneously unbuildable from these repos and unsellable under the regulation.**
🟢 **The buildable product is the assistive one, and it is the one the permissive shelf already
supports:** `GradeMate` (MIT) for rubric intake, `OpenMAIC` (MIT) for delivery, `moodle-mcp` (MIT) for
the platform surface, `lm-evaluation-harness-pt` (MIT) for evaluation.

## 🟢 Thirty-sixth pass, 2026-10-07 — five trends: the tutor stops being general, and a market series stops being one series

⚠️ **T1 and T2 rest on payload-verified repositories. T3–T5 rest on secondary sources and every cited
market/regulatory domain is blocked from this environment (000).** The distinction is load-bearing.

### T1 🟢 The tutor is becoming jurisdiction-shaped, and that inverts what the differentiator is

Three of the five permissive agents verified this pass are **bound to a named jurisdiction's assessment
instrument**, not to a subject:

| Asset | Bound to | Not |
|---|---|---|
| `BaijayantaRoy/bandup` (MIT) | **Singapore PSLE composition /40 and A-Level GP /50**, each marked against *that paper's own* band descriptors | "an essay marker" |
| `dikshant182004/MathTutor` (MIT) | **India's JEE** | "a maths tutor" |
| `AI-for-Education/lesson-plan-parse-mbsse` (MIT) | **Sierra Leone's MBSSE national lesson plans**, Primary + JSS + SSS | "a curriculum parser" |

🔴 **None is a general tutor with a locale setting.** Earlier passes shelved breadth-first tutors whose
selling point was subject coverage — `DeepTutor`, `Educhain`, `OATutor`. 🔵 **This is the orthogonal axis,
and it is the one engagements are actually sold on: a client does not buy "maths tutoring", they buy
"passes *our* exam, marked against *our* rubric."**

🔵 **The consequence for build-vs-extend is the reverse of how these projects are pitched.** The agent
scaffolding — LangGraph graph, retrieval, memory — is **commodity and now available MIT-licensed in
working form**. The **rubric encoding, the band descriptors, the curriculum structure** are the
differentiator, the thing no upstream repo can supply, and the thing a client already owns and cannot
hand to a vendor's cloud. 🟢 **So the engagement shape is: take the scaffold, build the rubric layer,
keep it on the client's infrastructure.**

### T2 🔴 A licence string from a search summary will overwrite a verified shelf, and it did — three times in one pass

Three independent instances, all caught, all inside the same pass:

1. **`CC-BY-NC-4.0` read as a grant.** A fresh discovery probe reported
   `CRSS-AI/agentic-se-course-early-2026` as **`GRANTED`** because a `LICENSE` file existed. The payload
   forbids commercial use outright. 🟢 **This KB's shared classifier returns `CC-BY-NC-4.0` / `PROHIBIDO`
   on the first call — it simply was not run, because the probe was new code (`P473`).**
2. **`ECL-2.0` reported as `Apache-2.0`.** A search summary called Sakai *"Apache 2.0"*; that phrase was
   written into this pass's own trending row **before anything checked it**. Payload: **`ECL-2.0`**. 🔴 **And
   `repos/foundations.md` already said so.** Corrected in the same pass that introduced it (`P476`).

3. **An unlicensed repo cited as `MIT` inside a compose recipe.** `kaushal0494/AITutor-EvalKit` was
   written into this pass's `P47` as 🟢 MIT on a search summary's authority. **Payload: no licence at
   all**, and 🔴 **this KB's `agents/top.md` had already recorded three prior reproductions of exactly
   that false claim.** The fifth reproduction came from the pass that wrote the precedence rule, and it
   would have shipped **a recipe whose CI gate was an unlicensed dependency** (`P478`).

🔵 **The three share one mechanism and it is not carelessness: each is a case where a *plausible* licence
string was available more cheaply than the true one.** `CC BY-NC` *looks* like a grant because it sits at
`LICENSE`; `ECL-2.0` *is* Apache-2.0 in all but one section, so calling it Apache is 95% true — and the
5% is the patent grant, which is the clause a legal review argues about.

🔴 **The deeper pattern, and the reason this is a trend rather than three mistakes: every one was
already paid for and the controls already existed.** `P237` (never rewrite the classifier), `P250`
(family and commercial use are two columns), and a prior pass's record that **Sakai was missing for ten
passes over a misread licence line**. 🔵 **A control that exists but is not *in the path* of new code is
documentation, not a control** — which is the same shape as `P471`, where a passing gate judged nothing.

> **Order of precedence, now explicit: payload > this KB's verified shelf > secondary prose.** Never the
> other way, however confident the prose.

### T3 🟢 Local-first inference is becoming a compliance feature rather than a cost decision

`bandup` ships **local by default via Ollama** — no account, no telemetry, no essay leaving the machine —
and shows a **persistent on-screen warning the moment a non-local model is selected**. It states the
reason plainly: pasting children's writing into a cloud chatbot is a line many schools and parents will
not cross.

🔵 **Read that as architecture meeting regulation, because three jurisdictions now demand it
independently:** California **AB 1159** (prohibits using student data to train AI models), Vietnam's Law
on AI (**behavioural monitoring** named high-risk, in force 1 Mar 2026), and EMEA districts with
data-residency rules already self-hosting open-weight models. 🟢 **The "degrade gracefully to a local
model, and tell the user when you don't" pattern satisfies all three without a compliance review per
jurisdiction** — and `bandup` additionally separates the **OCR model choice from the marking model
choice**, so the most sensitive step (raw handwriting) can stay local while reasoning goes remote. 🔵 **That
per-step data-boundary granularity is the transferable idea.**

### T4 🔴 Education AI obligations are enforceable in APAC now, and deferred in the EU — the ordering is the roadmap

Unchanged from pass 35 and worth restating because it keeps being read backwards: the EU moved education
high-risk from **2 Aug 2026 to 2 Dec 2027** (Digital Omnibus), while **South Korea's AI Basic Act (22 Jan
2026)** treats education as high-impact and **Vietnam's Law on AI (1 Mar 2026)** names education among six
high-risk sectors, **explicitly including automated assessment and behavioural monitoring**.

🔴 **The common error is reading the EU deferral as sixteen months of global breathing room. It is sixteen
months of *European* breathing room during which two APAC statutes are already live**, and Article 50
transparency applies in Europe from Aug 2026 regardless.

🆕 **What this pass adds is the sub-national layer in North America, where the binding instrument is state
statute.** **Ohio HB 96** required **every** K-12 district to adopt an AI-use policy by **1 July 2026 — a
deadline that has passed.** 🟢 **So the engagement opening inverts: not "help us form a position" but "our
policy is in force and our tooling does not comply."** 🔴 **And because the statute does not prescribe
content, the policies differ district by district** — a product shipping into Ohio must read each
district's policy, not the state model.

### T5 🔴 A market figure without its series attached is not a number

This file's companion, `intel/market.md`, obtained a **complete five-region 2026 split** for the first
time and found it **sums to exactly the published global total** ($10.40B, 0.0% error), with the
CAGR-implied 2030 sum landing **0.3%** from that series' published 2030. 🟢 **That closure identifies the
series.** It also showed this KB has been dividing a figure from that series by a global total from a
**different** series (41.5% CAGR vs 31.2%), producing a plausible and wrong conclusion: North America's
share *"falling to ~25% by 2030"* when within its own series it is **35.4% → 33.6%**, roughly flat.

🔵 **Why this is a trend and not an accounting note: the secondary tier republishes figures without their
provenance, and figures from incompatible series circulate side by side as though comparable.** A share,
a ratio or a CAGR computed across two of them looks exactly like a finding. 🔴 **The error is undetectable
by inspection and detectable by addition** — which is the cheap test nobody runs (`P477`).

🟢 **What survived the correction is worth noting, because not everything did:** the inference that mature
markets grow below the global rate holds within the coherent series — NA (31.1%) and Europe (31.9%) below
the implied 32.8%, while APAC (35.3%), MEA (34.3%) and LATAM (33.5%) are above it. **The conclusion was
right; the arithmetic under it was borrowed from the wrong series.**

## 🔴 Thirty-fifth pass, 2026-10-07 — five trends, and the first is a gap that existed only on the shelf that declared it

### T1 🔴 A gap claim is the most dangerous kind of claim a knowledge base can hold, because nothing contradicts it

Pass 33 wrote a census that contradicted itself (`P465`). This pass found something worse:
`repos/foundations.md` declared for **three consecutive passes** that there is **no EMEA-origin
permissive education foundation** — while this same KB recorded `OpenOLAT/OpenOLAT` (**Apache-2.0**,
University of Zurich → frentix GmbH, Switzerland) and `OpenOLAT/qtiworks` (**BSD-3-Clause**,
University of Edinburgh, **already tagged `🟢 EMEA`**). One of those rows calls OpenOLAT *"the most
permissive full LMS in this KB."*

🔵 **Why a gap claim decays differently from a fact.** A wrong licence gets caught: the next pass
re-reads the payload and the channels disagree. **A wrong absence has no payload to re-read.** It is
re-asserted by passes that "confirm" it the only way an absence can be confirmed — by searching
outward and finding nothing — and **searching outward never looks inward**. `P467` is the pure case:
it probed **nine** European forges, measured them correctly, and hardened a conclusion that a
one-second `grep -ri openolat` would have destroyed.

🔵 **The transferable rule, `P469`: an absence is a claim about the whole corpus, so it must be tested
against the corpus, and it must name the scope it was measured on.** *"Not on this shelf"* and *"not
findable in this industry"* are different sentences and only one of them was true.

🔴 **And here is the part that makes this a trend rather than a mistake: the mechanical guard already
existed.** `compose/code/p370-gap-gate/` was built to falsify declared gaps against this KB's own
index, passes **27/27**, and previously caught this exact error class. Swept against the live tree
this pass it returns **5 gap sentences → 0 CONTRADICHOS, all `NO-CLAIM`** — because the KB's prose
shifted from Spanish to English and **two independent filters in the gate are Spanish-only**. On the
verbatim `P467` sentence the sweep extractor matches **nothing**, the scope classifier returns
`SIN-ALCANCE`, and yet the region resolves correctly to **`EMEA`** with **94 EMEA rows** on the shelf.

🔵 **So this is pass 34's T1 — *"a knowledge base loses capability the same way it loses facts"* —
recurring in its worst form: not a capability forgotten, but a capability still running, still
green, and silently covering nothing.** `27/27` and `0 CONTRADICHOS` were each true, and together
they were misleading. **A passing suite measures the cases you wrote, never the class you stopped
writing**; the only symptom was a denominator falling from 29 to 5, and nothing reported denominators.

🔵 **The design rule, `P471`, and it generalises past this KB: `NO-CLAIM` must not be the same
verdict as "unparseable."** Give every classifier a third outcome — pass, fail, and *I could not read
this* — and make sweeps print their denominator. Instrument shipped this pass:
`compose/code/p471-gap-gate-language/` (**16/16**), which found **8 language-blind claims among 50**,
including a second false English one: *"no LATAM-origin permissive education project."* Recipe: `P45`.

🔴 **Second-order cost, and it is the real one:** `P467` reasoned *from* the false gap to a client
instruction — *"never quote this KB's thin EMEA shelf as market evidence."* The instruction happens to
be good advice. **It was derived from a premise that was false.** A conclusion that survives its
premise being wrong is luck, not method.

### T2 🔴 For the first time, the EU is not the binding constraint on an education AI roadmap

The **Digital Omnibus** (final Council approval **29 June 2026**) moved stand-alone Annex III
high-risk obligations — which cover **education access and assessment: admissions, student
evaluation, exam scoring** — from **2 Aug 2026** to **2 Dec 2027**. In the same window, **South
Korea's AI Basic Act** came into force (**22 Jan 2026**, education = *high-impact*) and **Vietnam's
Law on AI** came into force (**1 Mar 2026**, education among six high-risk sectors, naming
**automated assessment** and **behavioural monitoring**). **Taiwan** passed its AI Basic Act in
**Dec 2025**.

🔵 **Every AI-in-education compliance narrative written before mid-2026 assumed Brussels set the
clock.** It no longer does. A grading or proctoring product shipping into Seoul or Hanoi is in scope
**today**; the same product in Frankfurt has until **Dec 2027**.

🔴 **The failure mode this creates is specific and predictable: reading the EU deferral as global
relief.** It is regional relief, and it arrived in the same months two APAC statutes became
enforceable. ⚠️ **Also note what did *not* move: Article 50 transparency applies from Aug 2026
regardless**, and the substance of the high-risk obligations is unchanged — only the date moved.
⚠️ **All of this is secondary-sourced: `eur-lex.europa.eu` is 000 from here.**

### T3 🟢 LATAM's gap is governance, not adoption — and that inverts the usual sell

**87%** of Latin American institutions use AI in at least one area; **only 26%** have a formal AI
strategy. **79%** of faculty use AI in teaching (**+18 points** on the global 2025 figure), yet
**88%** report only minimal-to-moderate engagement. UNESCO's finding is the same in prose:
institutions are using generative AI for teaching, learning and research **without policies to govern
it**.

🔵 **The usual regional pitch — "adoption is low, here is a pilot" — is simply wrong for LATAM.**
Adoption already happened, informally, faculty by faculty. The unmet need is **policy, academic
integrity, and faculty enablement**, and those are the precondition for the deeper uses (assessment,
feedback, analytics) that the 88%-shallow figure says have not started. 🔵 **Governance first is the
revenue path here, not the compliance tax.**

### T4 🔴 A published licence claim is now a *more* dangerous input than a missing one

**Forma LMS** is recommended by articles this pass **because** it is Apache-2.0 — permissive
licensing is the stated reason to pick it. From this environment: **19 licence filenames × `main` and
`master` → nothing**, **Packagist → 404**, **no parseable `composer.json`**. Recorded `licence
unverified` (`P470`).

🔵 **Pass 32 retired *"it has a LICENSE file"*. This retires something stronger: *"a source I trust
says it is Apache-2.0."*** The missing-licence case is safe because it is visibly missing — nobody
ships it by accident. **The confidently-asserted-but-unverifiable case ships**, because it reads like
a finished answer. 🔴 **And it lands on the platform tier**, where a licence error decides in-tree
versus side-car — the most expensive architectural commitment in an engagement.

🟢 **The complementary finding in the same week:** the permissive platform tier is **larger** than
this KB said — OpenOLAT **Apache-2.0** and Eloom **MIT**, both payload-verified. 🔵 **So the lesson
is not "distrust permissive claims." It is: verify them, in both directions.** This pass found one
false permissive claim and two true ones this KB was not using.

### T5 🟡 "Purpose-built beats general-purpose" is now the industry's own stated thesis — which raises the bar on composition

Sources converge on 2026's defining movement being **away from generic AI tools toward platforms
purpose-built for education**, with pedagogical structure — learning objectives, grade-level
expectations, assessment logic, instructional flow — **embedded in the system rather than supplied by
a prompt**. The adoption metric that predicts retention is **5–10 hours saved per teacher per week**,
and the deployments that work start **with teachers, not students**.

🔵 **Read against this KB's own shelves, that thesis is a warning about composition.** The generalist
agent tier (CrewAI, LangGraph, OpenHands) supplies orchestration and **no pedagogy**; the education
tier supplies the standards and structure (QTI, LTI, xAPI, Open Badges, curriculum ontologies).
🔴 **A recipe that wires a generalist orchestrator to an LLM and calls it an education product is
exactly the generic tool the industry is reported to be moving away from.** The structure has to come
from the standards tier — which is precisely why `qtiworks` (**BSD-3-Clause**, programmatic QTI 2.1)
arriving on the foundations shelf this pass matters more than another agent framework would.

⚠️ **One honest note on T5's evidence:** the "5–10 hours" threshold and the purpose-built thesis come
from **vendor and trade press**, not from controlled study. 🔵 **Usable as a product-design heuristic
and as language a client will recognise; not as an efficacy claim in a deliverable.**

## 🟢 Thirty-fourth pass, 2026-10-07 — five trends, and the first is that this KB forgot an instrument it had already built

### T1 🔴 A knowledge base loses capability the same way it loses facts — in the freshest layer

Pass 33 wrote a six-channel census whose `raw.githubusercontent.com` row says, verbatim,
*"**the only licence channel**"* — and whose `pypi.org` row, four lines later in the same table, says
*"still open, as pass 41 used it for `edx-proctoring`"*. 🔴 **Both cannot be true, and the narrower
one was the one that propagated**, into the pass-33 headers of four separate shelves.

🔵 **Nothing was lost that was never had.** Earlier passes used PyPI, npm, Packagist and Maven
Central, and verified that each discriminates. **What decayed was not a fact but the record of a
capability** — and a capability nobody remembers having is indistinguishable from one that does not
exist. The downstream cost is real: four shelves spent a pass telling readers that licence
verification had one source when this KB's own history proves it has five.

🔵 **The transferable rule: a census is a cumulative instrument record, not a re-derivation from
whatever this pass happened to probe.** A pass that measures three channels must inherit the other
seventeen, not quietly redefine the census as three. Pass 33 named this exact failure in its own T2
— *"the freshest layer is where stale claims live"* — and then committed it. Recorded as `P465`.

### T2 🟢 Payload proves a document exists; a classifier proves a claim — and the gap between them is where the traps live

Pass 32 established that *"it has a LICENSE file"* is no longer a usable test. The complement, worth
stating as its own trend: **a registry classifier is the publisher's own machine-readable assertion
about what the licence is**, and it fails differently from a text-matched blob. The worked example
found this pass:

> **`open-webui`** serves a file named `LICENSE` at 200. Its PyPI metadata declares
> **`License :: Other/Proprietary License`**, and the text is a bespoke *"Open WebUI License"* with
> branding restrictions. 🔴 **One channel sees a licence file; the other says "proprietary".**

🟢 **Run both and the agreement rate becomes a measurable property of the shelf.** Ten existing rows
were re-read through their registries this pass and **ten agreed** — including an independent
reproduction of this KB's Open edX asymmetry (`xblock` Apache-2.0 against `openedx-learning` and
`edx-proctoring` AGPL-3.0, plus the newly recorded `edx-opaque-keys` **AGPL-3.0-only**). ⚠️ **But
`P468`: the channel is silent more often than it is wrong.** `crewai` publishes no licence metadata,
`chamilo/chamilo-lms` 404s on Packagist, and 8 of 20 PyPI rows carried only free text. **A silence is
not a finding, and a row answered by one channel must say so.**

### T3 🔴 Licence-resolvable and install-resolvable are different properties, and only one is ever checked

[`soumics/adaptive-ai-tutor`](https://github.com/soumics/adaptive-ai-tutor) is MIT. Its RAG core
[`soumics/llm-rag-assistant`](https://github.com/soumics/llm-rag-assistant) is **also MIT**. The
dependency closure is clean and this KB's own closure tooling would pass it without comment. And it
**cannot be installed from this environment**, because `requirements.txt` pins that core as a
**GitHub archive zip at an exact commit**, and `github.com/.../archive/<sha>.zip` is **403** here
(`codeload.github.com` likewise).

🔵 **A manifest scan answers "what am I allowed to use?" and never "will this resolve?"** The two
diverge whenever a project distributes outside a package registry — direct VCS pins, archive URLs,
submodules, vendored wheels. 🔵 **The engagement consequence is sharper than the KB consequence:** a
client's build environment is usually *more* restricted than this one, and a pinned GitHub archive is
a supply-chain dependency on a single immutable URL with **no registry mirror behind it**. Recorded
as `P466`.

### T4 🔴 A declared gap needs three parts, and this KB has been writing two

This shelf has declared for three passes that it can find no EMEA-origin permissive education
foundation. True and honest about the result; silent about the reach. This pass measured the reach
and found **nine European and public-sector forges unreachable** — `code.europa.eu`,
`gitlab.opencode.de`, Codeberg, Framagit, FSFE (all previously recorded), plus three measured here
for the first time: **`forge.apps.education.fr` (the French Ministry of Education's forge)**,
`invent.kde.org` and `salsa.debian.org`. All **000**.

🔴 **The EUPL tier is by construction the tier most likely to live where this instrument cannot
look** — EUPL is the European Commission's licence and the Commission publishes to `code.europa.eu`.

🔵 **The gap is still a gap; it did not become coverage.** What changed is that it can no longer be
quoted as evidence *about the market*. 🔵 **A declared gap needs three parts: what was searched, what
was found, and what could not be reached.** This KB had been writing the first two, which is how an
instrument limit comes to read as an industry fact. Recorded as `P467`.

### T5 🔴 Capital fell 44% while structural adoption hit 47% — this is a services market, not a product market

On a like-for-like window, **January–July 2026 raised ~$435M across 24 deals against ~$774M across 37
deals in January–July 2025: −43.8% in capital, −35.1% in deals.** Pass 32 recorded this decline at
26%; the like-for-like figure is worse. Meanwhile **47% of higher-education institutions now use AI
structurally** in teaching and administration, and **more than 50% of teachers in Chile and Brazil
use AI tools** inside institutions of which **fewer than 10%** have written guidelines.

🔵 **Capital down with usage up is not a contradiction, it is a market-shape signal.** Deal count fell
further than deal size, so fewer companies are clearing the bar at all rather than rounds being
repriced downward. Nobody is funding a new education AI product — and institutions are deploying
anyway, from operational budget, into stacks they already own.

🟢 **That is a systems-integration market**, which is the business Globant is in: the buyer is the
institution, the money is operational rather than venture, and the deliverable is governance and
integration into the Moodle, Canvas, Open edX and SIS estate the client already runs. 🔵 **The
corollary is a positioning warning: pitching a *platform* into this market pitches against the one
thing the funding data says is not being bought.**

### 🔵 What this pass did NOT establish

- 🔴 **No star counts.** `api.github.com` **403**. The **GitHub MCP** route an earlier pass used is
  **outside this session's repository scope** (restricted to `globant-kb` and `education-kb`), so
  "not obtainable this pass" means exactly that. Every popularity figure on these shelves is
  inherited or absent.
- 🔴 **No model-weights licence.** `huggingface.co` **000**. Sarvam AI, ILMU, Sahabat AI, SEA-LION,
  HyperCLOVA X Think, NTT Sarashina and Latam-GPT appear in `intel/market.md` as **client-supplied
  inputs**, and **not one of their weights licences is verified here.** Oldest standing limit; it did
  not move.
- 🔴 **No primary legal text.** `eur-lex.europa.eu` **000**. Every AI Act date is secondary-sourced
  and must be re-verified against the Official Journal before client use.
- 🟡 **Maven Central is reachable and still unused.** `repo1.maven.org` 200; **no JVM row read**.
  Sakai, OpenOLAT and Opencast remain payload-verified only. This is the cheapest open task for the
  next pass.
- 🟡 **Bitbucket is reachable and unused.** 200, and **never named in this KB before** — capability,
  not coverage. No row on any shelf points at it.

## 🔴 Thirty-third pass, 2026-10-07 — five trends, and the first is that this KB re-acquired an error it had already fixed

### T1 🔴 A declared gap decays faster than a row, and nobody re-measures gaps

This KB declared *"there is no permissive open-source exam proctoring agent"* and ranked building one
as its **second-best build opportunity**. The gap rested on a single repository's licence verdict.
Re-probed this pass, that repository is **MIT** (`master/LICENSE`, 1068 B, © 2026 Prem Biswal), and a
**second** permissive proctoring agent — MIT, copyright **2020** — surfaced in the same run.

🔵 **The asymmetry is the trend, and it generalises past this KB.** A *row* is wrong only if the repo
it names changes. A *gap* is wrong the moment **any repository anywhere** acquires a licence, is
renamed, or is published — so a gap's error rate scales with the whole ecosystem while a row's
scales with one project. **Yet rows get re-verified every pass and gaps get restated.** Twenty-six
passes quoted this one without re-running the measurement beneath it.

🟢 **The discipline: a declared gap must carry the probe scope that produced it, and must be
re-measured — not restated — before it is quoted.** In the very table where this failed, the row
*beside* the mis-probed one recorded its scope (*"2 branches × 6 filenames"*); the one that mattered
recorded none. Because of that omission, the correction **cannot distinguish** *"the licence was
added after the probe"* from *"the probe was too narrow"*. **A negative verdict without its scope is
not a measurement — it is an opinion with a timestamp.**

### T2 🔴 The freshest layer of a knowledge base is where stale claims live

Pass 32's new top sections in three files asserted that EU AI Act Annex III enforcement for education
began in **August 2026**. This KB had **already corrected that** — Regulation (EU) 2026/1744 moved
Annex III stand-alone high-risk to **2027-12-02** — and the correct dates were sitting **deeper in the
same files**, recorded as `P284`.

🔵 **The mechanism is worth naming because it is structural, not careless.** A new pass drafts its top
section from what the search channel returned this hour. The open web still overwhelmingly repeats
*"the AI Act takes full effect in August 2026"*. So each pass that writes top-down from fresh
summaries **re-imports the ecosystem's consensus error**, and it lands precisely where a reader looks
first, while the correction sits a thousand lines below. 🟢 **The rule: draft the new section against
the tree, not against the search results.** Grep your own corrections before writing the date.

### T3 🟢 "Open source" for a sovereign model splits by layer and by holder

**Latam-GPT** — Chile's CENIA with 60+ institutions across 15 countries, ~$550k — is reported
everywhere as *"the open source model for Latin America"*. Measured:

| Layer | What it actually is |
|---|---|
| Tooling code | 🟢 **MIT** / **MIT-0**, verified from payload — but held by **Tim Duffy**, **EleutherAI** and an **individual contributor**, and **two of three repos are upstream projects re-hosted** |
| Model weights | 🔴 Reported **Llama 3.1 Community Licence** — **not OSI-approved**, with acceptable-use and naming conditions. ⚠️ **Unverifiable from this environment** (`huggingface.co` → **000**) |

🔵 **Neither half matches the headline.** The code is genuinely permissive but is substantially other
people's code; the model is not open source in the sense this KB uses the term. **Not one of the
three grants is held by the project or any partner institution.** 🟢 **The generalisation, which now
has instances in three industries' worth of sovereign-model announcements: read a sovereign-AI
"open source" claim by layer (code / weights / data) and by holder (who actually grants it).** A
national or regional AI programme is a consortium, and consortia publish grants held by whoever
happened to write the file.

### T4 🔴 The model layer of this industry cannot be verified, and that is a standing limit

`huggingface.co` returns **000** from this environment, and `eur-lex.europa.eu` does too. So the two
sources that would settle this industry's two hardest questions — **what licence do these weights
carry** and **what does the regulation actually say** — are both closed.

🔵 **This is not a small operational note; it bounds what this KB can assert.** Education AI is
converging on open-weights models run on institution-owned hardware (the local-first trend this KB
has tracked for passes), which means **the licence that matters most is increasingly the one on the
weights** — and that is exactly the one unreachable here. 🟢 **The honest posture, and the one this
pass adopts: say "reported as" for every weights licence, and prefer compositions where the
permissive code is yours and the weights are a swappable, client-chosen dependency.** A pattern that
hard-codes one open-weights model is one terms change away from a re-read nobody here can perform.

### T5 🟢 LATAM is the most AI-positive region measured and the least governed — a 61-point gap

| Signal | LATAM | Global |
|---|---|---|
| Faculty positive about AI in education | **72%** | 57% |
| Faculty using AI in teaching | **79%** | — |
| Faculty at only *minimal-to-moderate* engagement | 🔴 **88%** | — |
| Institutions using AI in ≥1 area | **87%** | — |
| Institutions with a formal AI strategy | 🔴 **26%** | — |

🔵 **Enthusiasm 15 points above global, usage high, depth shallow, governance almost absent.** That
combination is the exact inverse of EMEA, where regulation forces governance and appetite lags. 🟢 **So
the same studio capability sells on opposite arguments in the two regions**: in EMEA, *"the law
requires this by December"*; in LATAM, *"you already deployed it and nobody owns it"*. ⚠️ **And the
regional-governance anchor now exists** — UNESCO's **Observatory on AI in Education for Latin America
and the Caribbean**, launched **2026-04-14** — alongside **Uruguay** becoming the first LATAM
signatory of the Council of Europe's **Framework Convention on AI**. A LATAM governance engagement no
longer has to import a European framework to have something to point at.

## 🟢 Thirty-second pass, 2026-10-07 — six trends, and the first one is a correction to how this KB reads a licence

### T1 🔴 "It has a LICENSE file" stopped being a usable test

[`murderszn/open-tutor`](https://github.com/murderszn/open-tutor) serves a 869-byte file at
`main/LICENSE` whose text is: *"This repository has not declared a project-wide reuse license… A
public GitHub repository is not itself a declaration of an open-source or open-content license."*
**The file exists, is correctly named, returns 200, and refuses the grant.**

🔵 **This is a new shape of licence signal and it will spread.** Maintainers are learning that
silence gets misread as permission, so some now publish an explicit *refusal* in the place a licence
would go — which is good practice that **breaks every existence-based scanner**, including the one
this KB was using. Every prior licence defect recorded here moved a row between two real licences,
where the error is a wrong *degree* of freedom; this one files an all-rights-reserved repo as
licensed. 🟢 **The rule, generalised: existence is not the test — the grant is the test.** Paired with
`P456` (a README's `- Apache (recommended) with mod_rewrite enabled` became "Apache-2.0, no copyleft
obligations" in a secondary source), the discipline is now: **read the payload, identify the subject,
and check the role the word is playing in the sentence.**

### T2 🟢 The integration surface schools want is the gradebook, not the chat window

Six MCP servers for **LMS gradebooks** — five Canvas, one Moodle — all MIT, each with a **different
copyright holder**, all surfacing in the same window. Not a fork tree; six independent decisions.

🔵 **Read it as a shift in where the value is believed to be.** A tutoring chatbot sits beside the
institution's systems of record; a gradebook agent sits **inside** one. Grades are the institution's
hardest data: they are contested, audited, appealed and legally consequential. Six people wiring
agents to that API means the market's belief has moved from *"AI talks to students"* to **"AI
operates the administrative machinery teachers actually lose time to."** ⚠️ **And nothing certifies
the write path.** Tool counts span 3× (51 / 102 / 165), there is no shared schema, no conformance
suite, and no agreement on whether a grade write is idempotent. **The absence of a standard here is
itself the trend** — and the opening: whoever publishes a conformance suite for LMS gradebook agents
defines the category. 🔴 Two repos circulated as part of this "all MIT" set have **no licence at
all** (`CreveXTech/canvas-lms-mcp`, `DMontgomery40/mcp-canvas-lms`) — the blanket claim was wrong
for 2 of 8.

### T3 🟢 Local-first became a compliance strategy, not a privacy preference

Three of four notable new learning workspaces this pass run inference on hardware the user owns:
`zijinz456/OpenTutor` (10+ providers, **no API key required**), `LEARNableLabs/opentutor` (history
stays on the machine), `open-edge-platform/education-ai-suite` (OpenVINO on Intel CPU/iGPU/NPU).

🔵 **The driver is regulatory arithmetic, and it points the same way in two regions at once.** EU AI
Act Annex III makes educational assessment **high-risk** with conformity duties due **2027-12-02**
(⏸️ **pass 33, 2026-10-07: this line read *"full enforcement from August 2026"* — superseded by Reg.
(EU) 2026/1744. The duty live since 2026-08-02 is **Article 50 transparency**, which was not
deferred. See `P284`**);
California **A.B. 1159** would bar training on student data unless the school benefits; Idaho
**S.B. 1227** mandates data-privacy requirements for AI tools in K-12. A stack where student work
**never leaves the building** does not need a cross-border transfer argument, a sub-processor
addendum, or a promise about model training — the questions do not arise. 🟢 **As of this pass the
permissive version of that stack is complete and verified:** `education-ai-suite` (Apache-2.0,
including **hardware benchmarking** — the question that decides affordability), `prometheus-eval`
(Apache-2.0, **open evaluator weights**), `rubric` (MIT, rubrics as data). ⚠️ The constraint is
capital expenditure and ops capability, and edtech funding is **down 26% YoY** — so the pitch is
*run-rate reduction plus audit readiness*, not *transformation*.

### T4 🔴 Adoption has saturated while capital retreated — the scissor defines the engagement

**86%** of educational organisations have adopted generative AI, the **highest of any industry**;
**86%** of students across 16 countries use AI in their studies; **60%** of US K-12 teachers used AI
tools in 2024–25. Meanwhile edtech venture funding in H1 2026 was **$1B, down 26% YoY**, in smaller
and more selective cheques.

🔵 **There is no greenfield left to sell, and no budget for a speculative platform.** When adoption
is near-universal, the remaining work is **consolidation, governance and proving value on what is
already installed** — inventory, data-flow mapping, control sets, evidence trails, retiring
redundant tools. ⚠️ **The honest reading of 86%:** it counts *any* generative-AI use, including a
teacher using a consumer chatbot nobody sanctioned. It measures **diffusion, not governed
institutional capability**, and the distance between those two is exactly the billable work. Do not
let the number be quoted as 86% of institutions having an AI programme.

### T5 🔴 A national mandate failed at under 30%, and the cause was teachers, not technology

South Korea mandated AI textbooks from 2025. Adoption sat **below 30%** by March, and in **August the
National Assembly stripped them of official textbook status** after unions argued the pace had
outrun teacher preparation — this in the **second jurisdiction after the EU** to pass comprehensive
AI legislation.

🔵 **This is the most useful negative result available in this industry right now.** A wealthy,
technically capable country with legislative will, a national curriculum and funding still failed —
and failed *upward*, by legislative reversal, which is the expensive kind. The binding constraint
was **teacher capability and trust**. 🟢 **The contrast case is India's DIKSHA**, which frames AI as
**accessibility** (read-aloud for visually impaired students, keyword search inside video) rather
than as substitution: politically durable, technically modest, and already running at national
scale on `project-sunbird/sunbird-lms-service` (MIT, shelved pass 31). ⚠️ **Idaho S.B. 1227
independently legislates the same lesson** — it explicitly prohibits AI from replacing human
teachers. Two jurisdictions, two routes, one conclusion: **lead with augmentation and teacher
preparation, or repeat Korea.**

### T6 🔴 LATAM's constraint is licences, not output — 1 of 4 repos carries a grant

Four LATAM education-AI repositories were found this pass. **One has a licence.**
🟢 [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) — MIT, Universidad Tecnológica de
Pereira, Colombia, Open-edX-native, rural-first, closes pass 31's declared LATAM gap. 🔴 The other
three publish **no grant**: `a-bobadilla/Asistente-Pedagogico-IA` (Canvas, competency-based lesson
planning), `henriquebotelhogomes/educacao` (Brazil, LangChain + Llama 3/Groq + Docling + Qdrant),
`virginiandujar/educa-ia`.

🔵 **This reframes the regional story this KB has been telling.** Earlier passes recorded LATAM as
thin on supply; measured repo by repo, **the work exists and is relevant — it is simply unusable.**
That is a different problem with a much cheaper fix: a grant is one file. ⚠️ It compounds with the
governance vacuum on the demand side (Mexico: **73%** of university students using AI for coursework
against **over 80%** of institutions having no normative framework) — unusable local supply *and*
absent local policy, while usage is already near-universal. 🟢 **The lowest-cost high-visibility
regional contribution available: get licences onto LATAM education repos.** It converts existing
regional work into reusable assets and is the kind of upstream act that is remembered.

### 🔵 What this pass did NOT establish

- ⚠️ **No star counts, no momentum measurement.** Three channels measured, three **403**: `curl -sI`
  on github.com, `curl` **GET** on github.com, `api.github.com`. Every trend above is read from
  licence payloads, repository documents and secondary sources — **not** from growth data. Any claim
  here about something "gaining traction" rests on *independent appearance in the same window*, not
  on measured stars.
- 🔴 **EMEA supply gap unresolved, second consecutive pass.** No EMEA-origin permissively licensed
  education repo found. EMEA has the strictest regime (Annex III, August 2026) and the thinnest
  local open-source supply on this shelf.
- ⚠️ **APAC growth rate is genuinely disputed** — **35.3%** vs **28.1%** CAGR from two houses with
  different base years and scopes. Recorded as a range, deliberately not averaged.
- 🔵 **Two tutoring systems are paper-only**, no code located: `LEA` (arXiv:2607.13370) and the
  multi-agent tutoring latency/cost study (arXiv:2604.24110).
- 🔴 **`formalms/formalms` effective licence is still unknown.** Established only that **no grant is
  published in the repository** (16 filenames × 3 branches, all 404) and that the "Apache 2.0" claim
  in a secondary source traces to a **web-server requirement line**. Its Docebo lineage is **GPL**,
  the opposite of the claim — but this pass did not confirm Forma's own terms, only that the
  repository publishes none.

# Trends — Education, October 2026

## 1. Purpose-built beats general-purpose

The most defining trend of 2026 is the move away from generic AI assistants
toward platforms built specifically for education. Buyers who piloted a general
chatbot in 2024–25 are now replacing it with something that understands
curriculum, mastery and assessment. Consequence for Globant: a thin wrapper over
a frontier API is no longer a differentiated offer; the pedagogy layer is.

## 2. From experimentation to governance

AI in education has shifted from "can we" to "under what policy." Clear policies,
data boundaries and oversight are now preconditions of adoption, not follow-ups.
Ohio required every district to have a written AI policy by July 2026; 134
state-level bills were introduced in the US in 2026; the EU AI Act classifies
educational assessment as high-risk. **The compliance artefact is now part of the
deliverable.** Ship the policy mapping, the audit trail and the oversight gate
with the software.

## 3. Agent-native tutoring architecture is settling

DeepTutor (Apache-2.0, 40.8k★, v1.6.13 on 2026-10-04) shows the shape the
category is converging on:

- a **two-layer plugin model** — single-shot *Tools* the model calls, and
  multi-stage *Capabilities* that take over a whole turn;
- **three entry points** — CLI, WebSocket API and Python SDK, so the same engine
  serves a terminal, a web client and an embedded integration;
- **per-learner workspaces with persistent memory**, personality and an evolving
  skill set, rather than one stateless assistant for everyone.

Copy this decomposition even if you do not use DeepTutor. Memory-per-learner and
the Tool/Capability split are the two decisions that matter.

## 4. MCP has become the LMS integration layer

This is the most practically important shift of the last few months.
`vishalsachdev/canvas-mcp` (MIT) now exposes **up to 102 Canvas tools and 8 agent
skills** — including a 20-check WCAG accessibility scanner and bulk grading —
and works with 40+ MCP clients. `peancor/moodle-mcp-server` (MIT) does the
equivalent for Moodle.

Why it matters beyond convenience: **MCP side-cars keep their permissive
license** while in-tree LMS plugins inherit copyleft. Every in-tree Moodle AI
plugin probed this pass is GPL-3.0; both canonical MCP servers are MIT. The
integration style now determines the IP outcome.

**Refinement from the second pass of 2026-10-06 — and it is a correction of
emphasis.** A side-car is permissive *by the author's choice*, not by
construction. Sweeping every Canvas and Moodle MCP server that surfaces in
search, the shelf is in worse shape than the canonical two suggest:
`DMontgomery40/mcp-canvas-lms` (103★, 54 tools, v2.3.0) and `loyaniu/moodle-mcp`
(38★) carry **no license at all** on any branch or in their READMEs, and
`csmediapro/moodle-mcp-server` is **AGPL-3.0 with a paid premium tier**. Only
four of the seven servers probed are usable, and the most-starred non-canonical
one is not. An unlicensed repo is worse than a copyleft one: AGPL is a constraint
you architect around, no license is all-rights-reserved. **A license probe is now
week-one engagement work, not diligence you defer.** Full table in
`agents/top.md`.

## 5. Framework consolidation — AutoGen is out

`microsoft/autogen` (61.3k★) is in **maintenance mode**: no new features,
community-managed, with the README directing new users to **Microsoft Agent
Framework** (MIT, 14.0k★, Python + .NET). Its `LICENSE` at HEAD is now CC-BY-4.0
rather than plain MIT. Any education proposal still specifying AutoGen should be
re-specified on MAF, smolagents or LangGraph. Earlier cycles of this KB
recommended AutoGen; that recommendation is withdrawn.

## 6. Sovereign and on-prem inference is a requirement, not a preference

EMEA districts with data-residency rules self-host open-weight models (Llama,
Mistral) rather than call commercial APIs. Every major APAC economy has built its
own base model — Sarvam AI, ILMU, Sahabat AI, SEA-LION, HyperCLOVA X Think, NTT
Sarashina. California AB 1159 makes "student data is not used for training" a
legal commitment that must be demonstrable. Ollama (MIT) and vLLM are therefore
infrastructure, not an optimisation.

Note the APAC gap: these are **base models with no education agent layer**.

## 7. Assessment is the regulated frontier — and the tooling gap

AI-driven assessment is named in nearly every forecast as a growth area, and in
nearly every regulation as high-risk. Meanwhile **no permissive open source
auto-grader exists** — searched again this pass, nothing credible found. OATutor
(MIT) supplies something more useful than a grader: Bayesian Knowledge Tracing,
which yields a *defensible, inspectable* mastery estimate, published at CHI '23
with follow-up in PLOS ONE.

The honest position with a client: automate item generation and feedback, keep
scoring human-gated, and use an explainable mastery model where a number has to
be justified.

**Amended in the third pass of 2026-10-06 — the tooling half of this trend is no
longer true as stated.** [Selleo/mentingo](https://github.com/Selleo/mentingo)
(**MIT**, read from payload, 91★) grades open-ended behavioural and
problem-solving answers automatically and returns actionable feedback, and traces
every model call through Langfuse. So a permissive auto-grader exists — for
**corporate L&D**, not for academic assessment, and with no rubric or curriculum
alignment. Three things follow:

1. **The build-vs-adopt answer changed for L&D work.** You no longer start an
   enterprise training grader from scratch.
2. **The compliance answer did not change at all.** Annex III, the Oklahoma and
   Maryland statutes and Korea's high-impact classification are indifferent to
   licence. The human gate on consequential scores stays.
3. **Say both sentences to the client in that order.** A client who hears only
   "an open source auto-grader exists" will hear "we can drop the review step",
   and that is the one misreading of this KB that creates real liability.

## 8. Skills economy and verifiable competency

Real-time skills visibility, adaptive training and competency frameworks gained
ground in 2026, with career-navigation tools spreading across K-12,
post-secondary and workforce contexts. Open Badges tooling
(`1EdTech/openbadges-validator-core`, Apache-2.0) is the permissive
infrastructure for competency claims a third party can verify. Expect corporate
L&D and public workforce programmes to converge on this.

## 9. Offline-first is an equity requirement, not a legacy concern

Kolibri (MIT) — offline-first teaching and learning with no internet — is the
only fully permissive end-to-end platform on the education shelf. Given CEPAL's
findings on LATAM structural gaps and a widening talent gap since 2022, plus
sub-10% institutional readiness in a region where over half of Chilean and
Brazilian teachers already use AI personally, offline-capable and low-cost is
where the volume is.

## 10. Human connection is becoming the measured outcome

As AI becomes commonplace, human-driven indicators — engagement, well-being,
sustained participation — are becoming *more* important, not less. Practical
effect: instrument for retention and participation, not just for correctness and
completion. A tutoring deployment that improves completion while reducing
sustained participation is a failure that only shows up if you measure it.

## 11. Agent-specific governance has arrived, and a regulator wrote it first

Until 2026, education AI governance was general AI rules applied to education by
analogy. That changed: **Singapore's IMDA published the world's first Model AI
Governance Framework for Agentic AI** at Davos in January 2026, updated in June
2026 — a framework that governs autonomous planning, reasoning and action
directly. Its four dimensions read as a build checklist:

1. **bound the agent upfront** — pick appropriate agentic use cases and place
   explicit limits on the agent's powers;
2. **make humans meaningfully accountable** — define which checkpoints require
   human approval (note *meaningfully*: a rubber-stamp approval does not count);
3. **technical controls across the whole agent lifecycle**, not just at launch;
4. **enable end-user responsibility** through transparency and **training** — the
   framework explicitly expects users of workflow-assisting agents to be taught
   capabilities, common failure points and risks.

Two consequences. First, dimension 4 makes teacher and student enablement a
*compliance artefact*, which means it is fundable rather than discretionary.
Second, a system designed to this framework largely satisfies EU Annex III, the
Oklahoma/Maryland human-oversight statutes and Korea's high-impact
classification at the same time — so use it as the cross-region checklist even on
engagements nowhere near Singapore.

The binding-regulation wave is also wider than this KB recorded: **Korea's AI
Framework Act took effect 22 January 2026** and **Vietnam's dedicated AI law
(No. 134/2025/QH15) on 1 March 2026**.

## 12. Agent Skills are becoming the distribution format for pedagogy

The interesting packaging unit is shifting from "a tutoring app" to "a skill an
agent can load." `vishalsachdev/canvas-mcp` (MIT) ships **8 agent skills**
alongside its 103 tools. `JuneYaooo/lineage-skill` (Apache-2.0, 448★ — the
highest-starred project on the `education-ai` topic) exists only to produce them:
it distils videos, PDFs, transcripts and notes into **source-backed teacher Agent
Skills**, preserving source attribution, extracting the instructor's methodology
and ordering practice tasks progressively.

**Measured in the third pass of 2026-10-06, and it is now the majority shape.**
The `ai-tutor` topic sweep returned a skills cluster that no earlier pass had seen,
all MIT, all read from payload: **universal-examprep-skill (300★)** with
cross-session memory and citation-sourced answers; **algo-sensei (285★)** for
DSA mentoring; **universal-diagnostic-tutor-skill (238★)**, diagnosis-first for
STEM and CS; **kaogong-skill (156★)** with authority citations for Chinese
civil-service exams; **flysheep-ai/education-skills (106★)**, the first skill
**pack** rather than a single skill; plus feynman-tutor, anything-to-course and
Scientific-learning-skills. Of the 17 permissive projects added this pass, **eight
are skills and only nine are applications.**

Three signals worth separating out:

- **A pack is emerging as the distribution unit above the skill.** `education-skills`
  bundles teaching-and-learning skills as a collection — the shape an institution
  would actually publish, and the shape a studio would actually sell.
- **Citations and cross-session memory are the differentiators, not the prompt.**
  The two highest-starred skills both carry provenance (citation-sourced,
  authority citations) and one carries memory across sessions. That is exactly what
  the high-risk regimes ask for, arrived at by the market rather than by the
  regulator.
- **Diagnosis-first is the pedagogically strongest pattern on the shelf.**
  `universal-diagnostic-tutor-skill` and `Scientific-learning-skills` both establish
  the misconception before explaining, and `feynman-tutor` inverts the roles so the
  learner teaches the AI. These reach for what OATutor's Bayesian Knowledge Tracing
  does, without the statistical machinery — cheaper to build, weaker to defend.
  Use the skill shape for formative work and the BKT shape where a number must be
  justified.

Why this matters commercially: a skill is portable across the 40+ clients that
speak MCP, which makes an institution's *pedagogy* — its methodology, its
sequencing, its worked examples — the reusable asset rather than the application
wrapped around it. Source-backed matters just as much: a skill that carries
provenance back to the instructor's own materials is defensible in a way a
fine-tune is not, and provenance is what the high-risk regimes ask for. Expect
"turn our course into agent skills" to become a recognisable engagement shape.

## 13. Curriculum mandates have become the demand driver — and they specify the architecture

New in the third pass of 2026-10-06, and the most actionable trend added today.
Two jurisdictions have moved past guidance to **compulsory AI instruction with
published specifics**:

- **UAE** — Cabinet decision **May 2025**, mandatory AI from **Kindergarten (age 4)
  to Grade 12**, from the **2025–26 academic year**, delivered **inside an existing
  subject** (Computing, Creative Design and Innovation) **without extending school
  hours**, by **specially trained teachers**, across **seven areas**: foundational
  concepts, data and algorithms, software use, ethical awareness, real-world
  applications, innovation and project design, and policies and community
  engagement.
- **China, at provincial level** — **Beijing**: at least **8 hours of AI lessons a
  year** in every primary and secondary school from **1 September 2025**, compulsory
  from age six. **Guangdong**: **6 hours a year** in lower grades rising to **one
  hour a fortnight in grades 10 and 11**. The sequence runs from voice-recognition
  basics through machine learning and **misinformation detection** to applied
  projects.

**Why this is a different kind of trend from trend 2 (governance).** Governance
constrains how you deploy. A mandate **creates a budgeted obligation to deliver
content and train teachers** — it is a procurement trigger, not a compliance cost.
The UAE design makes that explicit: the material goes inside an existing subject
with no extra hours, so what is being bought is **integrated curriculum content and
teacher enablement**, which is services work, not a licence sale.

**And the mandates hand you the two hardest design requirements as inputs.** Beijing
**bars primary-school pupils from independent generative-AI use** and **prohibits
teachers from substituting AI for their core instructional duties.** Those are not
policy footnotes; they are system requirements:

- **age-gated capability** — younger cohorts get teacher-mediated AI only, enforced
  by the system and not by guidance;
- **enforced teacher-in-the-loop** — the teacher's role is structurally protected,
  not advisory.

This is the strictest formulation of human oversight anywhere in this KB, and it is
therefore the most useful one to build to: **a design that satisfies Beijing
satisfies EU Annex III, the Oklahoma and Maryland statutes, Korea's high-impact
classification and Singapore's agentic framework.** Note also that two of the UAE's
seven areas — ethical awareness, and policies and community engagement — are
governance and civics rather than technique, so a curriculum pipeline must produce
**age-appropriate ethics and policy material**, not only exercises. Pattern P9 in
`compose/patterns.md` builds to all of it.

## 14. The permissive shelf stopped being thin, so the differentiator moved

Three passes on 2026-10-06 took the permissive education open source layer from
"DeepTutor plus fragments" to roughly **30 verified projects**, including a full
**MIT** AI-native LMS (Mentingo), a 506★ MCP server, a local-first adaptive
workspace with FSRS and a knowledge graph (OpenTutor), and a skills cluster at
100–300★. Earlier passes of this KB described the AI layer as thin and the platform
layer as copyleft, and concluded that the defensible position was the permissive
side-car. **The side-car conclusion survives; the "thin layer" premise does not.**

What changes in the pitch: the scarce thing is no longer *knowing which repos
exist* — a client can read a listicle. The scarce things are now

1. **composition** — wiring a specific set of these parts into something that
   serves one institution's pedagogy;
2. **licence diligence** — this pass alone rejected six projects totalling 963★ for
   AGPL, GPL or no licence at all, including two whose only licence statement was
   unenforceable prose;
3. **governance** — the audit trail, the oversight gate, the age gating, the
   provenance.

None of the three is available off a shelf, and all three are services.

## 15. Permissive is a bigger set than "MIT, Apache, BSD" — and open core hides inside directories

A practical trend with a direct commercial cost, measured this pass.

**The allowlist is wrong if it has three names on it.** The education shelf depends
on at least six permissive licences: MIT, Apache-2.0, BSD, **ECL-2.0** (the
Apache-2.0 text with the patent grant narrowed to education — Sakai, Opencast and
Kuali Rice all use it), **the PostgreSQL License** (pgvector), and ISC. A filter
that string-matches `MIT|Apache|BSD` rejects **four genuinely permissive
higher-education components**. Fix the filter, not the finding.

**And a repo-level licence is no longer a sufficient reading.**
`langfuse/langfuse` is MIT *except* its `ee/`, `web/src/ee/` and `worker/src/ee/`
directories, which carry a separate enterprise licence — a **by-directory**
carve-out that no badge can express. Its copyright line now reads **ClickHouse,
Inc.**, so the holder changed between passes while the licence string did not. Two
additions to the probe discipline: read the carve-out **paths**, and record the
**copyright holder** alongside the licence so a change of ownership is visible next
pass.

**The flip side, and the harder lesson, is about withdrawals.** Everything above
guards against a false positive. The second pass of 2026-10-06 produced the
opposite error: it withdrew this KB's OpenTutor entry after probing
`tutornew/OpenTutor` (8★, unlicensed) when the real project was
`zijinz456/OpenTutor` (**MIT, 130★, FSRS 4.5, 12 blocks, LOOM knowledge graph**).
A 404 or an unlicensed verdict is evidence about **one owner's repository**, never
about a project. **A withdrawal needs a stronger probe than an addition**, because
a wrong addition wastes a probe and a wrong withdrawal destroys knowledge and is
believed.

## 16. US state law has converged on one testable rule: human judgment is final

Fifteen trends in, the single most useful thing about the 134 AI-in-education bills
across 31 US states is **how little they disagree on the core requirement.** Read
by mechanism rather than by state, the 2026 statutes converge on a sentence you can
build against:

| State | Instrument | The operative requirement |
|---|---|---|
| Idaho | **SB 1227**, Generative AI in Education Act | statutory test: **"human judgment remains the final authority"**; AI may not replace human teachers |
| Oklahoma | **SB 1734** | AI only **under educator supervision with human review**; barred from high-stakes decisions; **annual parent disclosure** |
| Maryland | **AI Ready Schools Act** | human oversight; all **24** districts adopt aligned policies within **120 days** of MSDE guidance |
| Ohio | **HB 96** (2025–27 budget) | first state to **mandate** a written district AI policy — deadline **1 July 2026, now passed** |
| California | **AB 1159** (CALPIPA, signed 10 Sep 2026) | **identifiable student data may not train generative AI**; higher-ed provisions from **1 July 2027** |

**Why this is a trend and not a list.** Four different legislatures, drafting
independently, landed on **teacher-in-the-loop plus no-high-stakes-automation** —
the *same* requirement the EU AI Act imposes on Annex III education systems, the
*same* one Beijing enforces by barring primary pupils from independent generative-AI
use, and the *same* one trend 7 identifies as the regulated frontier. **A single
oversight architecture now satisfies the EU, five-plus US states and China.** That
is the strongest reuse argument in this KB: build the gate once, sell it in every
region.

**And the statutes are buying more than compliance.** Idaho mandates **AI literacy
standards and educator training**; Oklahoma requires **annual parent disclosure**;
Ohio's districts are **past** their policy deadline and therefore in the
implement-and-audit phase. These are **enablement and recurring-reporting lines**,
not one-off policy documents — the same shape as the UAE's teacher-training mandate
in trend 13.

**What to build, concretely.** The gate is the product:
`WAITING_REVIEW`-style approval before any graded or published artefact, an
immutable evidence trail per decision, cohort-based capability tiering, and a
disclosure report generator. [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
(MIT) is the **only permissive reference implementation** of that shape this KB has
found — 0★ and unproven, so read it and re-implement rather than pin it. Pattern
P11 assembles the production version.

## 17. The EU compliance clock moved, and the near-term deliverable is labelling

**Added in the fifth pass of 2026-10-06. This supersedes the August 2026 dates
used in trend 2 and pattern P4.**

**Regulation (EU) 2026/1744** — the *Digital Omnibus on AI* — amends the AI Act.
Parliament approval **16 June 2026**, Council adoption **29 June 2026**, signature
**8 July 2026**, Official Journal **24 July 2026**, in force **27 July 2026**.
CELEX **32026R1744**.

| Obligation | Was | Now |
|---|---|---|
| Annex III stand-alone high-risk — **education**: admission and access, evaluation of learning outcomes, student level placement, exam or behaviour monitoring | 2 Aug 2026 | **2 Dec 2027** |
| Annex I embedded high-risk | 2 Aug 2027 | **2 Aug 2028** |
| **Article 50 transparency**, incl. **watermarking / synthetic-content marking** | 2 Dec 2026 | **unchanged** |

The industry read this as a reprieve. It is not, quite. The **heavy** work moved
— technical documentation, conformity assessment, CE marking, EU-database
registration. The **transparency** work did not, and its deadline is **2 December
2026**: disclose that a learner is talking to an AI system, and mark
AI-generated content. For an education deployment that means labelling every
generated lesson, item and piece of feedback.

**So the trend is a sequencing inversion.** Through 2026 the assumption was:
conformity first, transparency as a detail inside it. From now to December 2027
it is the reverse — **labelling and classification are the live obligations, and
conformity is the planned programme.** The deferral is also explicitly not a
holiday: classifying systems against Annex III and Annex I, and beginning
compliance planning, is immediate.

The clients in the worst position are the ones who heard "delayed" and stopped:
unlabelled, unclassified, and 14 months from a conformity deadline they have not
started scoping.

**Sourcing caveat.** EUR-Lex and the Commission's own notice are unreachable from
this environment (egress denied). Every date above is corroborated across several
independent legal and compliance-vendor analyses, and the CELEX id is given for
one-step verification. **Verify against EUR-Lex before this goes into a client
deliverable.**

## 18. Pedagogy evaluation is published as research and licensed as content

**Added in the fifth pass of 2026-10-06.** The fourth pass found one instrument
claiming MIT in a peer-reviewed paper with no `LICENSE` payload and called it a
licence failure mode. Searching for an alternative revealed that **this is how the
entire subfield licenses**:

| Instrument | Venue | Claimed | `LICENSE` payload |
|---|---|---|---|
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) (ETH Zurich LRE, 43★, 14 forks) | EMNLP 2025 oral | README badge **CC BY 4.0**; README body **CC BY-SA 4.0** — *same file* | **none** (10 filenames probed) |
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | EACL 2026 | MIT, stated in the paper | **none** |
| [kaushal0494/UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | NAACL 2025 | not stated | **none** |
| Open TutorAI (arXiv 2602.07176) | arXiv | "open source" | **CC BY-NC-SA 4.0** |

Four instruments for measuring whether a tutor *teaches well* — the one
capability an education client actually buys — and **not one permissive software
licence among them.**

**Why this is structural rather than accidental.** These come from education and
NLP research groups, where the publishing norm is Creative Commons for artefacts
and papers. CC licences govern *content*; they were never designed to grant the
rights a delivery team needs over *code*. The subfield is behaving normally for
research and anomalously for software, and the mismatch lands on whoever tries to
ship.

**A fifth failure mode, and the nastiest: the licence that contradicts itself
inside one file.** MathTutorBench's badge says CC BY 4.0 and its footer says
CC BY-SA 4.0, with no payload behind either. A reviewer who checks the badge
clears it; a reviewer who reads to the bottom flags ShareAlike; a reviewer who
probes the payload finds nothing. All three are reading the same commit.

**What to do.** MathTutorBench is also the best of the four — 7 tasks across 3
skills (problem solving, Socratic questioning, solution correctness, mistake
location, mistake correction, scaffolding generation, pedagogy following), a
**1.5B pedagogical reward model** scoring generated teacher utterances against
ground truth, and a 20+ model leaderboard. **Read the task design, re-implement
the harness, vendor none of them, and file a `LICENSE` issue on all three
unlicensed repositories.** For model *selection* — a different question —
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
is MIT and usable today.

## 19. The compliance toolchain commoditised; the education profile did not

**Added in the fifth pass of 2026-10-06.** This KB recorded "no open source EU AI
Act compliance toolkit" four times and implied each time that the work was a
build from scratch. It is not, any longer:

| Repo | Licence (payload) | What it already carries |
|---|---|---|
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** | Six-tier risk classifier over the Act's decision tree; **61 conformity checklist items** across risk management, data governance, documentation and human oversight; **8 document templates**; CLI, zero-dependency TypeScript SDK, client-only web UI |
| [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) | **Apache-2.0** | ETH Zurich: a technical interpretation of the Act plus a generative-model benchmarking suite — the measurement half |

**Neither mentions education, or Annex III point 3.** So the generic layer
commoditised while the vertical layer stayed empty, which is the same shape
trend 14 identified on the agent shelf: *the permissive base is no longer the
scarce thing, and the differentiator moved up the stack.*

**The missing artefact is small and specific:** Annex III point 3's four education
categories — admission and access, evaluation of learning outcomes, student level
placement, exam or behaviour monitoring — mapped onto the 61 checklist items a
school, university or edtech vendor actually has to evidence. That is a
**profile on an MIT base**, contributable upstream, and it is days of work.
Pattern **P13**.

## 20. Voice became a permissive capability — while its two best-known assets relicensed away

Added sixth pass, 2026-10-06.

Spoken interaction has been the one education capability that forced a
proprietary dependency. Oral practice, pronunciation feedback, role-play,
accessibility for pre-literate and low-literacy learners — all of it routed to a
paid speech API, which in turn meant per-token cost, a connectivity requirement
and student audio leaving the institution. **That is no longer true, and the
reason is one component.**

[k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) — **Apache-2.0,
15.1k★, 2,092 commits** — provides speech-to-text, text-to-speech, speaker
diarization and voice-activity detection **in a single permissive tree that runs
with no Internet connection** on Android, iOS, HarmonyOS, Raspberry Pi, RISC-V and
x86. Four capabilities, one licence, embedded-class hardware.

**The same trend has a trap inside it, and it caught the obvious choice.** The
best-known offline TTS in education and accessibility is Piper — adopted by Home
Assistant and NVDA, fast on a Pi 4. [rhasspy/piper](https://github.com/rhasspy/piper)
is **MIT** and has been **archived read-only since 2025-10-06**; development moved
to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl), which is
**GPL-3.0**. **The permissive version is frozen and the maintained version is
copyleft.** Separately, Coqui TTS — 46.1k★, MPL-2.0 — is **unmaintained upstream**
after the company wound down, while the [Idiap fork](https://github.com/idiap/coqui-ai-TTS)
at 2.3k★ carries **5,309 commits against the original's 4,668**. And
**SeamlessM4T**, the first result for "open source multilingual speech", is
**CC BY-NC-4.0** — unusable in billable work.

**What this means for how the shelf is read.** On an immature shelf, stars find
the live projects. On this one they point at a frozen repository, an abandoned
one, and a non-commercial licence. **The fields that carry the signal are archive
status, the successor notice and the commit count on the fork** — and the fork
with 5% of the stars is the one to depend on.

**The commercial consequence** is that voice moves from a line item with a
recurring per-token cost to a one-off build on hardware the client already owns.
That reprices every spoken-practice and oral-assessment proposal, and it is the
component that completes the offline-first pattern (**P18**).

## 21. Mother-tongue AI is a three-region capability — and the two-region version of this trend was wrong

Added sixth pass, 2026-10-06. **Revised in the seventh pass of 2026-10-06: the
headline claim was "two regions" and it is false.** ASEAN has a permissive,
self-hostable language layer in **five languages across four countries**, found
by searching in Bahasa, Thai and Vietnamese rather than in English:

| Repo | Licence (payload) | ★ / commits | Country |
|---|---|---|---|
| [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** | **1.8k** / 1,276 | Vietnam |
| [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** | **1.2k** / **6,649** | Thailand |
| [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** | 530 / 961 | Malaysia |
| [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** | 292 / 992 | Indonesia |
| [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** | 291 / 755 | Malaysia |

**Why the sixth pass got it wrong, because the error is reusable.** It asked
which languages have a permissive layer and went looking for **sovereign
models** — found SEA-LION, correctly established it has no repository-level
grant, and recorded the region as empty. But what makes a Thai tutor possible is
not a sovereign LLM, it is a **tokenizer**: Thai has no spaces between words.
**The gap was an artefact of the noun, not of the region.** Three regional gaps
in this KB have now been refuted by changing the channel, the layer and the noun
— and none by searching the original channel harder.

**Two qualifications that keep this honest.** None of the ASEAN shelf is
education-specific — like AI4Bharat, these are general toolkits that make a
mother-tongue tutor possible without making one. And only **one** of them covers
speech (`malaya-speech`), so spoken practice in Thai, Vietnamese and Indonesian
routes through the general shelf (`sherpa-onnx`, Whisper) and must be
accuracy-tested per language rather than assumed.

**What survives of the original trend, and it is still the commercially useful
part:** most of the world's teaching languages still have no permissive
self-hostable layer, the gap is a differentiator rather than a disqualifier, and
corpus-building is fundable first-phase work that ministries and development
funders pay for directly. The count moved from two regions to three. The argument
did not change.

**Original sixth-pass text follows, retained so the correction is legible.**

"Multilingual" in education AI usually means the handful of languages a frontier
model happens to serve well. Asked instead **which teaching languages have a
permissive, self-hostable layer**, the honest answer is narrow and uneven.

**Where it exists:**

- **India — broad, MIT, one institution.** AI4Bharat (IIT Madras) ships
  translation across **all 22 scheduled Indian languages**
  ([IndicTrans2](https://github.com/AI4Bharat/IndicTrans2)), TTS in **13**
  ([Indic-TTS](https://github.com/AI4Bharat/Indic-TTS)), ASR pretrained on **40**
  ([IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec)), and the annotation
  platform to curate it all ([Shoonya](https://github.com/AI4Bharat/Shoonya)) —
  **every one MIT**. Paired with Sunbird (MIT), a full national stack is
  permissive end to end (**P16**).
- **Uganda and Africa — small, Apache-2.0/MIT, and better than it looks.**
  [SunbirdAI/salt](https://github.com/SunbirdAI/salt) (**Apache-2.0**) ships
  translation, ASR and **studio-recorded TTS by professional voice actors** across
  Luganda, Swahili, Ateso, Lugbara, Acholi and Runyankole;
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**) carries
  continental MT from a 1,000-participant, 30-country community.
- **Portuguese — permissive, but it moved.** Tucano (Apache-2.0, peer-reviewed in
  *Patterns*) was Brazil-origin and is **archived since 2026-02-24**; **Tucano 2**
  continues under the **University of Bonn** [Polygl0t](https://github.com/Polygl0t/Polygl0t)
  initiative (Apache-2.0).

**Where it does not exist:** essentially everywhere else. Most of the world's
teaching languages have **no permissive, self-hostable speech or translation
layer** — and in ASEAN the nearest thing,
[SEA-LION](https://github.com/aisingapore/sea-lion), **has no repository-level
licence at all**: its grant is deferred to each HuggingFace model card because
terms vary with the base model, so "SEA-LION is MIT" is not a sentence anyone can
truthfully say.

**Three consequences for how engagements are scoped.**

1. **Check the language before promising the capability.** Mother-tongue delivery
   is deliverable from the shelf in two regions. Elsewhere the honest scope begins
   with **data collection**, and SALT is the worked example of doing that
   properly — six languages, studio recordings, two peer-reviewed papers,
   Apache-2.0.
2. **The gap is the differentiator, not the disqualifier.** A client whose
   language has no permissive layer has no off-the-shelf competitor either.
   Building the corpus is a defensible, fundable first phase — and it is the kind
   of work ministries and development funders pay for directly.
3. **Licence review in APAC is per checkpoint and recurring.** Where the grant
   lives on the model card, it must be re-read every time the checkpoint changes.
   Budget it as a standing task, not a one-time gate.

**And the sharpest instance of the gap is an application, not a language.** Oral
reading fluency — the highest-volume literacy measurement in primary education —
has **no permissive implementation anywhere**: FLORA, Literably, Amplify Text
Reading Online and SoapBox Labs are all closed, with no public repository. The
components are all now permissive and shelved, and a **public dataset with a
published accuracy baseline** exists (Ghana ORF Dataset; Whisper V2 at 10.3% WER,
*IJAIED* [10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)).
That is an open category with no open competitor — wired up as **P17**.

## 22. Regulation has started pricing the *corpus*, not just the decision

Added seventh pass, 2026-10-06.

Every education-AI compliance regime this KB has tracked regulates by the
**decision an AI makes about a learner**. EU AI Act **Annex III point 3**:
admission and access, evaluation of learning outcomes, level placement, exam or
behaviour monitoring. The Oklahoma and Maryland statutes: human judgment must be
final on consequential decisions. Korea's AI Framework Act: high-impact systems
need oversight and documentation. All decision-shaped.

**Vietnam has added a second axis, and it regulates the tutor by where its
content came from.**

**Decree 33**, signed **2026-06-30**, in force **2026-08-15**, implements Law No.
134/2025/QH15 and lists **46 high-risk AI systems** across six sectors. Three are
in education:

1. AI providing **self-learning content from uncontrolled data sources**
2. AI that **automatically evaluates results and ranks learners**
3. AI that **monitors and analyses learner behaviour using biometric data**

Categories 2 and 3 are Annex III in different words. **Category 1 has no
European equivalent, and it is the one that reaches the default architecture in
this KB.** An AI that generates self-study material from an uncurated corpus is
high-risk *even when it makes no decision about any learner at all*. A RAG tutor
that only ever explains things — no grading, no ranking, no monitoring — is in
scope in Vietnam on **corpus provenance alone**.

Obligations: report the risk level to the **Ministry of Science and Technology
before use**; **conformity assessment** before deployment and maintained
throughout; designated systems assessed by a **registered or recognised body**,
others **self-assessed** by the provider. Transition: education systems already
operating — grouped with healthcare and banking — have until **2027-09-01**;
everything else high-risk until **2027-03-01**.

**Three consequences.**

- **The ingestion pipeline becomes a compliance artefact.** Pattern **P2**
  (curriculum ingestion → item bank) and every RAG tutor on the shelf need a
  **source manifest** — what was ingested, from where, under what rights, reviewed
  by whom — not as good practice but as the evidence a conformity assessment
  consumes. This is the same gate `microsoft/shiksha-copilot` built as a human
  curator step and `CurriculumCraft-AI` argued for with synthetic generation; both
  now have a regulator asking for it. Wired up as **P20**.
- **One trigger is narrower than the EU's, and that is worth money.** Vietnam
  qualifies behaviour monitoring to **biometric** data. Non-biometric engagement
  analytics — time on task, attempt counts, mastery curves — sit **outside**
  category 3, where the EU's "behaviour monitoring" arguably captures them.
  Analytics-heavy products can be scoped more aggressively in Vietnam than in the
  EU, which is the first instance in this KB of an APAC regime being *looser* than
  Annex III on a specific axis.
- **"Curated corpus" stops being a quality claim and becomes a licence to
  operate.** The commercial read: in Vietnam the defensible tutor is the one that
  can name its sources. That favours exactly the curriculum-aligned, ministry-
  reviewed ingestion shape this KB already recommends, and it disfavours the
  general-purpose "upload anything" assistant.

**Provenance caveat, and it matters here more than anywhere else in this file.**
Every legal-publisher domain carrying Decree 33 is **EGRESS_BLOCKED** in this
environment — `allenandgledhill.com`, `vietnam-briefing.com`, `vietnamnews.vn`,
`thuvienphapluat.vn`, `vietanlaw.com` and `ed.events`, **6/6 refused** — so **the
primary text was not read.** The three education categories come from **two
independently-phrased searches whose summaries agreed on all three**, across five
secondary outlets; the **biometric** qualifier on category 3 appeared in only one
of the two. **Verify against the decree before this reaches a client
deliverable**, and treat the biometric narrowing as the least-confirmed element.

## 23. The licence label and the licence grant have come apart — and reading the payload is no longer enough

**Added in the eighth pass of 2026-10-06. This is a correction to how every
other trend in this file was verified.**

Eight passes of this KB established one verification rule: never trust a badge,
a sidebar or a blog post — **read the `LICENSE` payload from
`raw.githubusercontent.com`.** That rule bought real accuracy, and this pass
found its ceiling. **Four live cases, and the payload is wrong or silent in
every one:**

| Case | Payload says | Grant actually is | Direction |
|---|---|---|---|
| `Llamacha/IWSLT2023_Quechua_data` | **Apache-2.0**, complete and unambiguous | README: audio is **CC BY-NC-ND 3.0**, owned by Siminchikkunarayku + Llamacha | Payload **too permissive** |
| **Latam-GPT** (CENIA) | *(no repository located)* | **Llama 3.1 Community License** © Meta — **not OSI-approved**, AUP + 700M-MAU clause | Label **too permissive** |
| `caiuc/equipo-*` × 20 | **MIT**, complete | Holder is **CAi UC**, the event organiser, not the authoring teams — **template-inherited** | Grant **not issued by the author** |
| `AmericasNLP/americasnlp{2021,2022,2023,2024}` | **Nothing** | No grant at all, across four editions of a flagship venue — including a 2024 shared task on *creating educational materials* | **Silent** |

**The three shapes of failure, named so they can be checked for:**

1. **Wrong scope.** A correct, complete licence file that governs the
   repository's *scripts* while the *data* — the only reason to clone it — is
   governed elsewhere and more restrictively. New in this pass.
2. **Wrong holder.** A valid licence whose copyright line names someone other
   than the author, so the grant was inherited rather than issued. This KB's
   `p184` rule, now observed at a scale of 20 repositories at once.
3. **Wrong label.** Open *weights* under a bespoke corporate licence,
   described as open *source* by the press, by Brookings, and by **the European
   Commission's own Open Source Observatory**.

**Why it is a trend and not a methodology footnote.** All three shapes are
produced by the same market condition: **"open" has become a positioning claim
before it is a legal one.** Model-weight releases normalised bespoke licences
with acceptable-use policies and user-count thresholds; academic and
public-sector projects publish under grant-funded obligations to be "open"
without anyone on the project owning the licence question; and template-driven
repository creation propagates a copyright line nobody re-reads.

**Consequence for Globant, and it is a billable one.** The licence question in
an education engagement is no longer a checkbox a developer can clear in an
afternoon by looking at a repository page. **Three points, every time: the
payload, the asset-scope statement, and the holder.** For anything whose value
is data, audio, a corpus or weights, the asset-scope statement is
**controlling**. Budget it, and say so in the proposal — because the failure
mode is not "we could not find a licence", it is **"we found one, it was clean,
and it was the wrong one."**

**And the inverse is an opportunity.** The same condition means genuinely
permissive regional assets are **undersold**: BERTimbau sat at 886★ and MIT,
unmentioned anywhere in this KB for seven passes, while Latam-GPT's non-open
licence was being reported as open source by the EC. The asset that is quietly
correctly licensed is the one with no marketing behind it.

## 24. Licensing hygiene is now the measured constraint in two regions — and one event's rules fixed it in eight hours

**Added in the eighth pass of 2026-10-06.**

The seventh pass concluded of MEA: *"the binding constraint is not interest,
funding or capability — it is licensing hygiene. Three `LICENSE` files would
change the regional answer."* The eighth pass found the **same shape in LATAM's
indigenous-language layer**, which makes it a pattern rather than a regional
quirk:

- **AmericasNLP**, the flagship academic venue for the indigenous languages of
  the Americas: **four probed editions (2021, 2022, 2023, 2024), no `LICENSE`
  payload in any** — and the **2024 edition's Shared Task 2 is "Creation of
  Educational Materials for Indigenous Languages"**, which is precisely the
  asset this KB would want, shipped with data, baselines and no grant. Corpora for **Aymara** (6,531 pairs), **Nahuatl** (16,145)
  and **Quechua** (125,008).
- ASR for **Quechua, Guaraní, Bribri, Kotiria and Wai'khana**; MT for Peru; a
  T5 for **10** indigenous languages — **all ungranted.**
- **Ten of twelve** probed repositories carry no grant. The same organisation
  licensed its 2023 release and not its 2025 one; the same author licensed
  neither of two.
- Five LATAM education-AI applications found the same pass
  (Colombia ×3, Chile, Peru): **none has a `LICENSE` payload.**

**The capability is funded, published and benchmarked. The redistribution right
is absent.** So a Quechua or Guaraní tutor is blocked on **data rights, not on
modelling** — and that is a procurement and legal problem, which is cheap to fix
and expensive to discover late.

**The remedy, demonstrated rather than proposed.** **CAi UC** (*Centro de
Alumnos de Ingeniería*, Pontificia Universidad Católica de Chile) ran
**HaCAIthon 2026** with one clause in its rules: projects must ship an **OSI
licence** and a **root `LICENSE` file** to be *eligible for evaluation*.
**Result: 20 team repositories, 19 MIT and one AGPL-3.0, in a single eight-hour
event**, four of them education-track — including **EduFlow**, the first
LATAM-origin MIT education repository in this KB with running code.

**Why this is the most leveraged intervention this KB has identified.** The
sixth and seventh passes' recommendation was *file an issue asking for a
`LICENSE` file* — correct, but **retrospective**, one repository at a time, and
dependent on a maintainer who has already moved on. A submission rule is
**prospective**: it licenses work that does not exist yet, at the moment of
creation, when the authors are present and the question is trivial.

**The concrete action, with its caveat.** Sponsoring or co-writing the licence
clause in a university hackathon's rules — São Paulo, Lima, Bogotá, and on the
identical argument in Nairobi — costs a sponsorship line and addresses the one
constraint blocking **both** LATAM and MEA. **Caveat:** CAi UC's own template
put the **organiser** in the copyright line rather than the authoring team,
which is the wrong holder and triggers this KB's `p184` flag on all 20 repos. A
sponsored clause should name the **authors** as holders — a one-line difference
between a channel that produces usable assets and one that produces flagged
ones.

## 25. Permissive licensing has become a funding condition, and philanthropy is now the supply mechanism

For nine passes this KB has treated the permissive shelf as something that either
*exists* or *does not* — an organic output of universities, hackathons,
ministries and individuals, to be swept and graded. A different mechanism is now
operating: **a funder is buying the shelf into existence, and making the licence
a condition of the money.**

**The instrument.** The **K-12 AI Infrastructure Program** — **$26M**,
multi-year, led by **Digital Promise** with **Learning Data Insights**,
**DrivenData**, the **Massive Data Institute at Georgetown University** and
**Catalyst @ Penn GSE**, funded by the **Gates Foundation**, which also runs
proposal review and award monitoring. Launched 3 Nov 2025; first cycle open
4 Feb 2026.

**The condition.** All funded developments must be released under a licence **at
least as permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)** — with
**Apache-2.0** recommended for software and code *including evaluations, models
and applications*, and **CC-BY** for datasets and knowledge products.

**The volume already committed:** **twelve named projects** — four in cohort 1
(29 Jun 2026: Learning Equality on science misconceptions; Princeton on
simulated student models; National Tutoring Observatory / Cornell on ASR
leaderboards for education; Stanford's KB-TutorBench for formative assessment)
and **eight** in cohort 2 (21 Sept 2026, formative assessment plus math,
literacy and writing, outputs stated to be openly licensed) — plus the separate
**EDU AI** award of **up to $8M** for open-source K-12 math tutoring model(s),
closed 31 Jul 2026, work from Nov 2026 over 30–36 months.

**Why this is a trend and not a news item.** Three structural consequences:

1. **The arrival of permissive assets becomes predictable.** Organic open source
   gives you a shelf you discover; a funded programme gives you a **pipeline with
   owners and dates.** For the first time this KB can tell a client *when* a
   missing capability is expected rather than only that it is missing.
2. **Apache-2.0 becomes the default licence of the education AI commons,
   displacing MIT.** This KB's shelves are MIT-dominant because individuals and
   universities default to MIT. A funder specifying Apache-2.0 for *models,
   evaluations and applications* pushes the new layer toward Apache-2.0 — which
   brings an explicit patent grant, a material improvement for client work, and
   a licence-compatibility question nobody has to solve because both are
   permissive.
3. **It inverts where the gaps are.** The capabilities being funded are precisely
   the ones organic open source failed to produce: **evaluation, benchmarks,
   datasets, formative assessment, ASR for education.** These are expensive,
   unglamorous, require real data access, and have no individual-contributor
   path — which is exactly why this KB kept finding them absent for nine passes.

**The honest counterweight, measured:** **nothing has shipped.** `KB-TutorBench`
→ **0 repositories**; `learningequality` filtered on `benchmark` → **0
repositories**; the National Tutoring Observatory's org holds a website at 0★
with no licence payload. **Funded is not shipped**, and the correct posture is
architectural readiness (**P23**), not waiting.

⚠️ **Tier 2.** `k12-ai-infrastructure.org` and `digitalpromise.org` are
**EGRESS_BLOCKED** here; **no RFP or announcement was read.** Figures are
corroborated across independent search summaries. Confirm before client use.

## 26. In the US the procurement rubric, not the regulator, is now the specification

Trend 16 recorded that US state law had converged on one testable rule: **human
judgment is final.** That is a *constraint*. What a vendor actually has to
satisfy is a **scored rubric**, and 2026 is the year those rubrics became
mandatory, standardised and dated.

**The mechanism:**

- **Maryland SB 720** (effective **1 Jun 2026**): the state department publishes
  guidance **and an AI-tool evaluation rubric**; every local school system must
  adopt an aligned policy **within 120 days** and designate an **AI
  coordinator**. Reported as **24 districts** on the clock for **Fall 2026**.
- **Vermont** (**23 Jan 2026**): a rubric scoring **educational value, data
  privacy, usability and accessibility, cost, scalability, vendor reputation and
  age restrictions.**
- **Idaho, Maryland, Alabama**: statutory **capability assessments**,
  **pre-training verification**, and a **prohibition on vendors training models
  on student records** — now standard contract language.
- **CoSN, *U.S. State of EdTech 2026*: 39% of districts score interoperability in
  their RFP rubrics.**

**Three reasons this changes delivery, not just sales:**

1. **Interoperability is now a scored criterion, which retro-justifies trend 4.**
   This KB argued MCP/LTI side-cars on engineering grounds. In two of five
   district procurements, that architecture **wins points**. An LTI + MCP
   side-car (**P1**) is not merely clean — it is the shape the rubric rewards.
2. **"Prohibit training on student records" is an architecture constraint, and a
   familiar one.** It forces either a no-training contractual guarantee or
   inference you control. That is the **sovereign/on-prem** stack of trend 6 and
   pattern **P4** — arriving in North America through procurement law rather than
   through data-protection law as it did in the EU.
3. **The rubrics' own gap is the differentiator.** Most reportedly do **not**
   require **auditable interaction records**, **disclosure of how outputs are
   generated**, or **evidence of bias/accuracy/reliability evaluation.** Ship
   those three and you exceed every published rubric — and they are, nearly
   exactly, the artefacts the **EU AI Act education profile** already compels
   (**P13**). **One evidence pack, two regions.** That is the first genuine
   cross-region reuse this KB has identified on the compliance axis, and it runs
   from EMEA into North America rather than the other way round.

**The demand signal underneath it** is concrete: **NJSBA RFP 2026-02** (virtual
tutoring, with optional **outcomes-based contracting**) and **New Mexico PED RFP
27-92400-00002** (statewide high-impact tutoring for reading and math under
**House Bill 2**, SY2026-27 the first implementation year). Districts and states
are buying tutoring at scale, on rubrics, with outcome clauses.

⚠️ **Tier 2.** `cosn.org`, `marylandpublicschools.org`, `njsba.org`,
`web.ped.nm.gov`, `excelined.org` and `marketbrief.edweek.org` are all
**EGRESS_BLOCKED** here; **no rubric or RFP document was read.** Confirm each
statutory citation before client use.

## 27. The evaluation void is being closed by two instruments in two regions — a cheque and a rule

For five passes this KB recorded one absence: **no shippable permissive evaluator
of tutoring quality.** The ninth pass found North America buying it. This pass
found EMEA regulating it. **The same void, addressed by two different kinds of
instrument, on overlapping timelines.**

| Region | Instrument | Mechanism | Status |
|---|---|---|---|
| **North America** | **$26M K-12 AI Infrastructure Program** (Digital Promise + Gates Foundation) | **Funding**, with a mandatory licence floor at least as permissive as CC-BY-4.0 (content) / Apache-2.0 (code and models) | 12 projects funded; named grantees include Harvard's **OpenLiteracy**, Maryland's classroom datasets, Stanford's **KB-TutorBench**, Cornell's ASR leaderboards. **0 repositories shipped.** |
| **EMEA** | **Council of Europe Compass for AI and Education** + **Committee of Experts (EDU IA)** | **Rule-making** — a **European Reference Framework for the Evaluation of Educational Technologies**, plus a proposed **legal instrument to regulate AI systems in education** | 2026–27 work programme; Committee of Ministers text adopted in **Munich** under **Article 20** of the Framework Convention on AI |
| **APAC** | **none found** | — | Searched this pass and the ninth. No regional instrument and no regional funder addressing evaluation of educational AI. The region's most on-target asset, `AI-EDU-LAB/E-EVAL` (Chinese K12 LLM education evaluation benchmark, 33★), exists and is **ungranted** — re-probed across 20 URLs this pass, still no licence payload. **APAC built the benchmark and did not license it.** |
| **LATAM** | **none found** | — | Searched this pass and the ninth. No regional instrument, no regional funder. What exists is the measured demand: **9.0% of 200 higher education institutions across 19 countries have formal evaluation mechanisms** (UNESCO IESALC / UNU-IAS). **The need is quantified and the instrument is absent**, which makes this the region where an evaluation harness is sold as capability rather than as compliance. |

Both facts are **Tier 2** (search-summary corroborated; no primary document is
reachable from this environment).

**Why the pairing matters more than either half.** A benchmark you can adopt late;
a conformance framework you cannot. Evaluation evidence — interaction audit trails,
output provenance, measured accuracy and bias — has to be **generated while the
system runs**, which means a deployment that did not instrument for it has nothing
to submit when the framework lands. The North American artefacts are a *swap-in*;
the European framework is a *precondition*.

**What to do with it.** Build the harness now and leave the benchmark slot empty
(**P23**). It is the same harness in both regions: the US side fills it with
Apache-2.0 benchmarks as the twelve projects deliver through 2027; the EMEA side
turns its output into a conformance file. This also gives the EU AI Act work
(**P13**) a named successor instrument to track rather than horizontal regulation
alone.

**The honest counterweight:** `tutoring quality evaluation benchmark
license:apache-2.0` still returns **0 repositories**, measured 6 Oct 2026. Neither
instrument has produced a usable artefact yet. The trend is real; the shelf is
still empty.

## 28. Interoperability became a scored line item — and the permissive Python LTI hole closed on 2026-10-07

The ninth pass found the demand signal: **39% of districts score interoperability
in their RFP rubrics** (CoSN, Tier 2). That is not a technical preference, it is
**points in a bid**. This pass measured the supply side, payload-verified:

| Standard | Permissive implementations found |
|---|---|
| **LTI 1.3** | **4** — `Cvmcosta/ltijs` (Apache-2.0, 373★, Node), `1EdTech/lti-1-3-php-library` (Apache-2.0, 124★, PHP, **from the standards body**), `Unicon/tool13demo` (Apache-2.0, 27★, Spring Boot), `oxctl/spring-security-lti13` (Apache-2.0, 25★, Spring Security) |
| **OneRoster 1.1 / 1.2** | **1** — `theopenem/OneRoster.NET` (MIT, 6★, .NET), **rostering only, gradebook not implemented** |
| **Caliper Analytics** | **0 found on a permissive licence** |
| **QTI** | not swept |

🔵 **CORRECTED, twenty-fourth pass of 2026-10-07. The structural finding below is withdrawn.**

> ~~**The structural finding: there is no Python LTI 1.3 library on the permissive shelf.** Node,
> PHP, Java and .NET are served. Python — where essentially all of the AI tutoring and agent code in
> this KB is written — is not.~~

**Python is served.** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — **MIT**
(payload 1,098 B, © The Regents of the University of Michigan), head commit **2026-10-05 (2 d)**,
PyPI [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1, 2026-08-07 (61 d)**, 17
releases. [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (BSD-3,
98 d) serves the JupyterHub case and implements LTI 1.3 **and** 1.1.

🔴 **What was actually true, and is the version to carry into a bid:** the **well-maintained**
Python LTI 1.3 shelf was **copyleft**, not absent. The most actively developed implementation in any
language is [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) —
committed and released **6 days** ago — and it is **AGPL-3.0** (payload 34,520 B). This KB swept for
*permissive* and read the result as *nonexistent*, which is trend 29 turned on a licence filter
instead of a topic filter.

⚠️ **The narrow claim that survives:** there is no **live framework-agnostic** permissive Python
LTI 1.3 library. `dmitry-viskov/pylti1.3` is the only framework-neutral one and it is **1,416 days
cold on the commit channel, 1,417 on the release channel** — both channels agreeing, which is the
signature of abandonment rather than of a finished library. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`.

🟢 **So the two-runtime architecture is now conditional, not structural.** If the AI tier is Django
or JupyterHub, LTI launch happens **in-process** and there is no adapter to budget. Only a
non-Django, non-JupyterHub Python tier still needs the second runtime.

Three consequences for how work is scoped:

1. **The LMS choice now implies the integration runtime.** Moodle → the 1EdTech
   PHP library; a Spring estate → `oxctl`/`Unicon`; a Node AI service → `ltijs`.
   Week-one decision, alongside the platform.
2. **Grade passback and analytics streams are builds, not selections.**
   OneRoster.NET does rostering only, and Caliper has no permissive
   implementation here. If the rubric scores either, say "build" in the bid.
3. 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07.** This read *"a Python LTI 1.3 library is the
   clearest open-source contribution opening this KB has identified"*. **A Python LTI 1.3 library
   now exists** ([`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti), MIT, 2 d). The
   contribution opening that survives is narrower and still has the same buyer: a **framework-neutral**
   permissive Python LTI 1.3 library, or a **permissive-licensed equivalent of
   `openedx/xblock-lti-consumer`**, which is AGPL-3.0. 🔴 **Caliper Analytics, at zero permissive
   implementations, is now the clearest opening in this layer.**

**And a vocabulary warning that is part of the trend.** `OneRoster OR Caliper OR
"LTI 1.3" license:apache-2.0` returns **184 repositories**, led by
`google/caliper` (deprecated Java micro-benchmarking, 818★) and
`hyperledger-caliper/caliper` (blockchain benchmarking, 708★). **Education
standards share names with unrelated ecosystems**, and the result count reads as
ecosystem health when it is mostly a different ecosystem.

### 🔵 Correction, eighteenth pass of 2026-10-06 — the hole is **LTI-shaped**, not Python-shaped

Two things in this trend were measured and one was inferred. The measurement stands; the inference
does not.

**Stands:** ~~there is **no permissive Python LTI 1.3 library**. That is what the sweep tested and it
is still true.~~ 🔵 **Withdrawn at pass 23 and now *replaced* at pass 24 — see the block below, which
pass 24 corrects in turn: the library pass 23 named as the MIT answer was a 406-day fork.**

> 🔴 **WITHDRAWN at the twenty-third pass of 2026-10-07. The sentence immediately above is false and
> is retained only so this correction has something to point at.** It was already false when a later
> pass of 2026-10-06 reinstated [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3)
> (MIT, 1,069 B payload) in `agents/top.md` — a correction that never left its pass-scoped section,
> which is **trend 50** committed inside trend 28. The twenty-third pass closes it twice over:
> 🟢 [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) — **BSD-3-Clause**
> (1,527 B payload), head commit **2026-07-01**, README states it implements **LTI 1.3 and LTI 1.1**
> and is tested against **Open edX, Canvas and Moodle**; and 🟢
> [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti)
> — **MIT** (1,097 B), head commit 2025-08-27. ⚠️ `pylti1.3` itself is **1,415 days cold**, so the
> correction that first closed the gap closed it with an abandoned library. 🔴 **`ltiauthenticator`
> was cited three times in this KB before anyone counted it**, because it is filed as a JupyterHub
> authenticator and the gap was swept for as an *LTI library* — trend 29 turned on this KB's own
> index. See **trend 53** and `repos/foundations.md`, twenty-third pass.

**Withdrawn:** the broader reading — *"Python, where essentially all of the AI tutoring and agent
code in this KB is written, is not served"*. Two **MIT Python libraries for education standards**
were payload-verified this pass, both from the Dutch national education-ICT agency:
[`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) (IMS-LOM metadata records) and
[`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) (the Eduterm
curriculum-vocabulary service). **Python is served for metadata and curriculum alignment.** It is
unserved for **LTI 1.3 launch**.

🟢 **This makes the contribution opening cheaper, not smaller.** The gap is **one protocol**, not a
language's worth of missing ecosystem — and it keeps its procurement-scored buyer.

**And the QTI row of the table above is no longer blank.** It was the only standard left unswept,
and it turns out to be the **best**-served: **five MIT implementations**, three first published in
2026, one of them (`amp-up-io/qti3-item-player`, MIT, 30★) **1EdTech Certified for QTI 3 Basic and
Advanced "Delivery" conformance** — the first externally certified permissive asset in this KB.
Set against LTI 1.3's four uncertified implementations, OneRoster's one (rostering only) and
Caliper's zero. See `repos/foundations.md`, eighteenth pass, and §44 below.

⚠️ **The method note, because it is the transferable part:** QTI went unswept for ten passes
because the sweeps were organised **by topic** and QTI is a **standard**. The row was not empty
because the world was empty. It was empty because nothing had asked.

## 29. Gap claims built on licence-filtered search are claims about an index, not about the world

This is a methodological trend, and it belongs here because this KB — and every
consultancy doing the same work — **prices engagements on declared absences.**

Measured this pass: [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody)
is listed in GitHub's repository search as **"License: Not specified."** Its
payload at `main/LICENSE` is a **complete, unmodified MIT licence.**

**GitHub's licence field reported unlicensed about a repository carrying an MIT
grant.** The consequence is mechanical: a `license:mit` or `license:apache-2.0`
filter **cannot return** a repository the index believes is unlicensed. So every
zero-result, licence-filtered measurement — the instrument this KB uses to declare
that something does not exist — has a **false-negative floor it cannot see.**

Three of those zero-result measurements were run in this very pass, and are quoted
in `intel/market.md` as evidence that funded projects have not shipped. They stay,
because they remain the best available measurement. **Their meaning changes:**
they are evidence of **absence as the licence index sees it.**

The same pass produced the other half of the lesson. Re-probing the 41
repositories this KB had recorded as ungranted — 10 filenames × 2 branches each,
controls validated 6 of 6 — flipped exactly **one**, and the cause was neither of
the things the previous pass blamed: not the British spelling `LICENCE` (which
flipped **zero** of 41), but the **branch name**, which no pass had ever varied.

**The operational rule, for this KB and for client diligence:** a licence claim
is only as good as the payload read from the repository, under **every** spelling
and **every** branch; and an *absence* claim must state the instrument that
produced it. "There is no permissive X" is not a finding. **"A GitHub repository
search filtered on `license:apache-2.0` returned zero results on this date"** is,
and it is a materially weaker claim — which is the point.

## 30. The ministry tier is being bought by one proprietary vendor across three regions, ahead of the governance capacity

**Tier 2.** OpenAI's **Education for Countries**, launched at Davos 2026, works
directly with ministries of education, public universities and research partners.
Named participants place into three of this KB's four regions:

| Region | Named |
|---|---|
| **EMEA** | Estonia, Greece, Italy (**CRUI**, the rectors' conference), Slovakia, UAE, Jordan |
| **APAC** | Kazakhstan, **Singapore** (Ministry of Education + **GovTech**, added 20 May 2026 at the Education World Forum, London) |
| **LATAM** | **Trinidad & Tobago** |
| **North America** | **none named.** The programme is US-headquartered and contracts with *other* countries' ministries; **no US state or federal education agency is named as a participant.** North America's national-tier analogue is the $26M philanthropic programme with an Apache-2.0 floor (trend 25), which is the opposite acquisition model: it buys open artefacts rather than onboarding ministries. |

**Nine national or sector-wide bodies, one vendor, the ministry tier.** This is the
competitive context for every engagement in this KB, and it changes the pitch in
two specific ways.

**First, the sequencing is the risk.** LATAM is measured at **9% of institutions
with formal evaluation mechanisms** and **8% with a dedicated AI budget** (UNESCO
IESALC, 200 institutions, 19 countries). Trinidad & Tobago is acquiring a national
AI education programme into that. **The vendor is arriving before the capacity to
evaluate the vendor** — which is simultaneously the strongest argument for buying
governance work now and the mechanism by which a closed stack becomes permanent.

**Second, the opening is in the buyers' own language.** Singapore's MOE is
described as *"exploring various AI tools from different partners."* A ministry
that states a multi-partner posture while onboarding one vendor will evaluate
alternatives — and with **GovTech** in the room, the counterparty is an engineering
organisation capable of assessing an open, auditable, data-resident stack on its
merits. The named Singapore use case is **mother tongue language learning**, which
is precisely where this KB's permissive language-substrate shelves are strong and a
single global vendor is weakest.

**And EMEA is the region where this argument is being written into law.** Six EMEA
bodies are in the programme while the Council of Europe drafts a legal instrument
on AI systems in education and a framework for evaluating educational technology
(trend 27). **Sovereignty, auditability and data residency are not positioning in
this region; they are the subject matter of the instrument being drafted.**

## Regional notes where the trend diverges

- **North America:** adoption is broad (60% of K-12 teachers) and the binding
  constraint is policy and procurement, not willingness.
- **EMEA:** the AI Act's general application is **already live (2 August 2026)**;
  what is deferred is the high-risk set (Annex III stand-alone to 2 December 2027,
  embedded to 2 August 2028). The trend is pre-emptive compliance architecture, and
  the sequencing institutions actually use is admin and teacher support first,
  assessment last. The region is $2.64B in 2026 and the K-12 integration leaders
  are Finland, Estonia and the Netherlands — small digitally mature states, not the
  large economies. Africa is in this bucket and is greenfield.
- **EMEA, third pass:** Europe is **$2.64B (2026) → $8.0B (2030) at 31.9% CAGR** —
  *slower* than the 41.5% global rate, so it is the compliance-depth market rather
  than the growth market. **Middle East & Africa is sized at last: $0.56B (2026) →
  $1.6B (2030), 34.3% CAGR**, though a second source puts the UAE alone at $7.4M
  (2024) → $21M (2029), so quote MEA as a range. MEA runs on **strategies, not
  statutes** — Saudi Arabia, the UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco and
  South Africa all have national AI strategies and none has a binding AI law — and
  the **UAE's compulsory KG→Grade 12 AI curriculum** is the region's clearest
  procurement trigger.
- **APAC, third pass:** the regional shelf is the **strongest** permissive shelf in
  this KB, not the weakest — StudyMate (MIT, 624★), kaogong-skill (MIT, 156★),
  feifei-companion (Apache-2.0, 105★) and AI_Tutor_Release (MIT, 57★, aligned to
  the Chinese grade 1–9 curriculum) are all China-origin, and DeepTutor is Hong
  Kong. What is genuinely absent is an education layer on a **sovereign** model, and
  any India-, Japan-, Korea- or ASEAN-origin permissive education project at all.
  Scale: **~530M K-12 students in Asia**; adoption 65–75% (2025) → 80–90% (2026).
  Law per country: Korea 22 Jan 2026, **Vietnam 1 Mar 2026 (SEA's first)**, Japan
  deliberately voluntary, **India and Australia with no national framework in
  force**.
- **LATAM, third pass:** **87% of institutions use AI, 26% have a formal AI
  strategy**; **72% of faculty are positive about AI against 57% globally.** An
  enthusiasm-rich, governance-poor market — the easiest region in this KB to sell
  governance into and the hardest to sell adoption into. **Uruguay is the first
  LATAM signatory of the Council of Europe's AI Framework Convention (2025)**,
  which makes it the cheapest bridgehead for reusing EMEA compliance artefacts in
  the region.
- **APAC:** sovereign models everywhere; an education agent layer nowhere — and
  now sovereign *inferencing platforms* too, so the hosting gap is closing while
  the pedagogy gap stays open. Singapore leads on agentic governance, Korea
  (22 Jan 2026) and Vietnam (1 Mar 2026) on binding law. ANZ
  diverges from the rest of the region — higher public support for banning AI in
  schools, where Asian markets surveyed show lower support for bans.
- **LATAM:** the trend is teacher-led, bottom-up adoption outrunning institutional
  governance by a wide margin — now quantified for higher education: **92% of
  students and 79% of faculty** actively using AI, **94% of faculty** expecting to,
  while **88% of faculty report only minimal-to-moderate engagement**. Adoption is
  done; depth is not. UNESCO's LAC Observatory (14 April 2026) is the top-down
  counterweight now forming, and Colombia's funded CONPES 4144 programme shows the
  regulatory map fragmenting country by country rather than converging.

## Declared gaps this pass

**Updated in the fifth pass of 2026-10-06. Read this block first — it supersedes
the fourth-pass block that follows it.**

Channel new to this KB this pass: **institution-first search** (funding body,
ministry, university and research-group names, English and Spanish, not ordered by
stars). **Six gaps changed state, three of them refuted outright.**

- **REFUTED: "no India-origin permissive education project."**
  [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) —
  **MIT, 9★, 12 forks, 149 commits** — Microsoft Research India's VELLM
  initiative, validated in classrooms with the **Sikshana Foundation**.
  Teacher-side: curriculum → lesson plans, examples, analogies, activities and
  assessments → DOCX/PPT/handouts, plus multi-chapter question banks against
  blueprint formats, with a **human-curator gate** on textbook ingestion. Plus
  [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI)
  (MIT, 0★, **CBSE/NCERT grades 9–12 on open-weight Gemma only**).
- **REFUTED and reframed: "no ASEAN-origin permissive education project."**
  [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) —
  **MIT, 158★, 78 forks, 15,802 commits**, NUS-origin, "currently supported by the
  AI Centre for Educational Technologies." **What is actually missing is ASEAN's
  agent layer:** AICET's Codaveri (30,000+ feedback items), Softmark (70,000+
  scripts in 2025) and ScholAIstic run at Singapore Ministry-of-Education scale
  and are **all closed source**. The substrate is permissive; the products are
  not.
- **REFUTED on existence, confirmed on substance: "no LATAM-origin permissive
  education project — the firmest finding in this KB."**
  [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) — **MIT**, Universidad
  Tecnológica de Pereira, Sirius research group, Colombia, funded under
  **SNCTI** — specifies an Open edX side-car tutor for rural higher education in
  Risaralda, with a named pedagogical director. It has **4 commits and every code
  path in its own documented tree returns 404.** **The LATAM gap is a delivery-capacity
  gap, not an interest gap**, and a Colombian public university has
  independently specified **this KB's pattern P1**. Partnership lead; never a fork
  point.
- **RE-SIZED, much smaller: "no open source EU AI Act compliance toolkit specific
  to education."** The generic toolkit exists and is **MIT** —
  [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
  (six risk tiers, **61 conformity checklist items**, 8 document templates, CLI +
  SDK + client-only UI) — alongside Apache-2.0
  [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) from ETH Zurich.
  Neither mentions education or **Annex III point 3**. The gap is now an
  **education profile on an MIT base**: days of work, upstream-contributable.
  Trend 19, pattern **P13**.
- **STILL OPEN, and now structural rather than accidental: no shippable permissive
  evaluator of tutoring quality.** All four published instruments are licensed as
  *content*, not software: MathTutorBench (**CC BY 4.0 badge vs CC BY-SA 4.0 body,
  same file, no payload**), AITutor-EvalKit (MIT in the paper, no payload),
  UnifyingAITutorEvaluation (no payload), Open TutorAI (CC BY-NC-SA). See trend
  18. Re-implement; vendor none.
- **STILL OPEN, with a licence reason attached: no education layer on an APAC
  sovereign model.** [aisingapore/sealion](https://github.com/aisingapore/sealion)
  (424★) has **no repository-level `LICENSE` payload**; its README states terms
  vary by base model — Llama3 variants restrict commercial use, Gemma variants
  differ — and points to each **Hugging Face model card**. **Rights clear per
  model and per release, never per repository.** Landscape additions: **MaLLaM**
  (Malaysia, with NVIDIA, 3M+ users via YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL**
  (March 2026).
- **NEW: no permissive way for a non-technical educator to author and publish
  their own agent.** AICET's **ScholAIstic** does exactly this — educators design
  and deliver specialised chatbots, deployed across Social Work, Law and Nursing
  at NUS since June 2024 — and it is closed. Pattern **P8** is the nearest thing
  in this KB and it stops short: it produces Agent Skills *for* educators, not an
  authoring surface *used by* them. Precisely sized, uncontested, and validated at
  faculty scale by somebody else.
- **NEW: the education vertical does not appear in general AI trend tracking.** A
  daily AI open-source trend feed read on 2026-10-06
  ([duanyytop/agents-radar#3628](https://github.com/duanyytop/agents-radar/issues/3628))
  listed 23 repositories by star movement and **not one was an education-vertical
  project** — the only education-adjacent entry was `rasbt/LLMs-from-scratch`, which
  is AI literacy. *(That feed's star counts are demonstrably inflated and were not
  used for any number in this KB; it was read as a presence/absence check only.)*
  **An education shelf must be built by vertical search and never by watching what
  trends.**
- **Still no Brazil-origin permissive project.**
  [vitorr2101/Projeto-Agente-IA-Educacional](https://github.com/vitorr2101/Projeto-Agente-IA-Educacional)
  surfaced on a Portuguese-language search and has **no `LICENSE` payload** on
  either branch across five filenames. The one LATAM-origin project that exists is
  **Colombian**.
- **Unverifiable, therefore not recorded: "K.A.L.I."**, described in search results
  as a sovereign AI learning engine with 3D logic visualisation. A targeted search
  returned ten unrelated `sovereign`-named repositories and no such project. Named
  here so a later pass does not re-surface it as new.

---

### Fourth-pass gap block, retained

**Updated in the fourth pass of 2026-10-06.** Channels new to this KB this pass:
paper-to-repository tracing, a GitHub-organisation sweep, and a
Spanish/Portuguese-language search. Four of the gaps below changed state.

- **RESOLVED-IN-PART: lesson generation is no longer a gap at all.**
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT, 40.0k★,
  Tsinghua**) generates complete lessons — slides, quizzes, HTML simulations, PBL
  scenes — with server-side PostgreSQL-backed persistence. This KB spent three
  passes recording the 404 of a `-Brasil`-suffixed fork of this project as evidence
  of absence. **Check the upstream of a name before recording a gap.**
- **NARROWED: Africa has a code shelf.** `AI-for-Education` (5 of 6 repos MIT) is
  built for **Sierra Leone's MBSSE** and **Uganda**. At 1–12★ it is research-grade,
  so the gap becomes *small and specific* rather than *empty*. Teacher capability
  is still the binding constraint.
- **NARROWED: the gated-grading architecture has a permissive reference
  implementation.** `littlecookie0722/AI-Teaching-Agent` (MIT) implements the
  `WAITING_REVIEW` gate, sandboxed grading with evidence, and answer-stripped
  candidate views. **0★, no releases** — so the gap moves from "unbuilt" to
  "**not built at production maturity**". Re-implement, do not pin.
- **STILL OPEN, and now the firmest finding in this KB: no LATAM-origin permissive
  education project.** The gap **lost its strongest piece of evidence** this pass
  (`OpenMAIC-Brasil` was never Brazilian) and **survived anyway** on a
  Spanish/Portuguese-language search that returned zero LATAM-origin projects.
  Four independent channels agree.
- **STILL OPEN: no India-, Japan-, Korea- or ASEAN-origin permissive education
  project**, searched by jurisdiction name this pass. OpenMAIC **widens** the China
  lead rather than closing this. And still **no education layer on any APAC
  sovereign model** (Sarvam, SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think,
  BharatGen, Fugaku-LLM, NTT Sarashina).
- **NEW, precisely sized: no shippable permissive evaluator of tutoring quality.**
  `AITutor-EvalKit` (EACL 2026) is the only published instrument for scoring
  *tutoring* rather than answers — **MI** (Mistake Identification), **ML** (Mistake
  Location), **PG** (Providing Guidance), **AC** (Actionability) — and it has **no
  `LICENSE` payload**. `AI-for-Education/pedagogy-benchmark` (MIT, 12★) closes only
  the adjacent half: it scores **models against exam questions, not live tutor
  dialogue**. The evaluation gap is now split, and only the model-selection half is
  closed.
- **Still no open source EU AI Act compliance toolkit specific to education** —
  re-searched this pass, nothing found.

- **NARROWED (third pass, 2026-10-06): a permissive automated grader exists, for
  corporate L&D only.** `Selleo/mentingo` (MIT) grades open-ended behavioural and
  problem-solving answers automatically with Langfuse tracing over it. Still
  missing: a standalone permissive grader for **academic** assessment, and anything
  rubric- or curriculum-aligned for K-12 or higher-ed exams. The oversight
  requirement is unchanged — see trend 7.
- No open source EU AI Act compliance toolkit specific to education.
- No LATAM-origin open source education agent project — **now confirmed across
  three independent channels.** The third pass of 2026-10-06 added the `ai-tutor`
  topic page and a stars-sorted education search: 30 repositories read, 17 net new,
  **zero LATAM-origin.** This is the most firmly established gap in this KB.
  Earlier evidence, retained: `planejaia/OpenMAIC-Brasil`, surfaced by search as a
  Brazil-origin multi-agent classroom with a v1.0.0 release, returns **HTTP 404**;
  every file 404s across four branches. The `education-ai` GitHub topic contains
  no LATAM-origin project at all (its long tail is Chinese, Indian and German, and
  nothing on it exceeds 448★). Latam-GPT is regional foundation infrastructure,
  not a pedagogy layer.
- **Africa: almost entirely uncovered, and that is now stated rather than
  implied.** South Africa's draft national AI policy (2026) is forming and
  GenAITEd Ghana is a published first-of-its-kind curriculum-aligned teacher-education
  agent, but there is no deployed open source African education AI shelf to
  recommend from. Greenfield, with teacher capability as the binding constraint.
- **No permissive open source auto-grader — and now a measured reason to distrust
  the shelf generally.** Of seven education MCP servers probed, three are
  unusable (two unlicensed, one AGPL + paid tier). The education open source
  shelf is thinner than its star counts imply.
- **PARTLY REFUTED (third pass, 2026-10-06): APAC-origin education agents exist in
  volume.** The earlier claim that `panaversity/learn-agentic-ai` was the only
  APAC-origin asset was an artefact of sweeping one topic page. StudyMate (MIT,
  **624★**), kaogong-skill (MIT, 156★), feifei-companion (Apache-2.0, 105★) and
  AI_Tutor_Release (MIT, 57★, Chinese grade 1–9 curriculum-aligned) are all
  China-origin and permissive; DeepTutor is Hong Kong. **What survives:** no
  education layer on an APAC **sovereign** model (Sarvam, SEA-LION, Sahabat AI,
  ILMU, HyperCLOVA X Think, BharatGen, Fugaku-LLM, NTT Sarashina), and **no India-,
  Japan-, Korea- or ASEAN-origin permissive education project found in any channel.**
  The APAC shelf is China-plus-Hong-Kong.
- **No curriculum-aligned permissive content pipeline for the UAE's seven-area
  mandate** — searched this pass, nothing found. `Zenglian990/AI_Tutor_Release`
  (MIT) is aligned to the Chinese grade 1–9 curriculum and is the only
  curriculum-aligned permissive tutor on the shelf; there is **no equivalent for
  the UAE framework**, and two of its seven areas are ethics and policy rather than
  technique. That is a specific, sized, uncontested build opportunity.
- **No open source age-gating or capability-tiering component for education.**
  Beijing bars primary pupils from independent generative-AI use and China
  prohibits teachers from substituting AI for core instruction; nothing on the
  permissive shelf implements cohort-based capability tiering. Pattern P9 assembles
  it from general-purpose parts, as pattern P4 does for Annex III.

## Declared gaps — eighth pass, 2026-10-06

- **Trend 21 needs splitting, not another increment.** It currently reads
  *"mother-tongue AI is a three-region capability"*. After this pass the honest
  form is **two claims**: *capability* is at least **four** regions (India,
  Africa, ASEAN, LATAM), while **redistributable** capability is still **two**.
  LATAM has the corpora, the ASR and the MT and cannot license them. Left as a
  declared gap rather than silently renumbered, because the distinction between
  *existing* and *usable* is the whole content of trends 23 and 24.
- **No automated evaluator of tutoring quality — open since the fourth pass,
  unchanged.** TutorIA's **RNF-09** (pedagogical review by **≥2 subject-expert
  teachers per subject before launch**, MIT) is a **human protocol**, and it is
  the first citable one in this KB. It does not close the gap and is not
  presented as closing it.
- **No permissive open-source exam proctoring agent — not re-probed this pass.**
  The seventh pass's sweep stands; recorded so the next pass knows it was
  skipped rather than re-confirmed.
- **North America's general-language channel is saturated.** Four consecutive
  passes, identical facts. The next North America trend must come from district
  RFP language, state education-agency procurement portals, or vendor filings —
  **none of which this KB has ever swept.** Recorded as an exhausted channel, not
  as regional stability.
- **Latam-GPT's licence is single-source.** `huggingface.co`, `latamgpt.org`,
  `interoperable-europe.ec.europa.eu` and `opensourceforu.com` are all
  **EGRESS_BLOCKED** in this environment (4/4), so the model card was **not
  read**. The Llama 3.1 Community License's *properties* are independently
  confirmed from the OSI's published position; the **link** between Latam-GPT
  and that licence is not. Confirm before any client deliverable.
- **The `p184` holder question on the 20 CAi UC repositories is unresolved and
  is not a probe question.** Whether a student federation's template copyright
  validly covers code written by independent teams during an event is a matter
  for counsel. Recorded as a legal open item, not as a licence finding.

## Declared gaps — ninth pass, 2026-10-06

- **Trend 7's tooling gap is funded, not filled.** Assessment remains the
  regulated frontier with no permissive tooling *today* — measured this pass as
  **0 repositories** for `tutoring quality evaluation benchmark
  license:apache-2.0`. What changed is that **three or more of the twelve funded
  projects under trend 25 target exactly this**, through 2027. Recorded as a dated
  gap rather than renumbering trend 7.
- **The proctoring claim in this KB was wrong, and trend 7 should not be read as
  supporting it.** The seventh pass declared *"no permissive open-source exam
  proctoring agent"*; the eighth carried it unchanged. **204 MIT-licensed
  repositories match**, four payload-verified at 18–47★. The surviving claim is
  **maturity**, not existence — and the one framework-grade implementation
  (`lebmatter/exampro`, 72★) is **ungranted**. See `agents/top.md`, ninth pass.
- **Trend 21 still needs splitting, and the eighth pass's note stands
  unactioned.** *Capability* is at least four regions; **redistributable**
  capability is still two. This pass adds a fourth datapoint in the same shape
  from a new region — `AI-EDU-LAB/E-EVAL` (33★, Chinese K12 LLM education
  evaluation benchmark, **no licence payload**) — so the pattern is now recorded
  in **MEA, LATAM and APAC**. Left as a declared gap for a second consecutive
  pass rather than silently renumbered.
- **No primary funder or procurement document was read.** Fourteen hosts are
  **EGRESS_BLOCKED**: `k12-ai-infrastructure.org`, `digitalpromise.org`,
  `unu.edu`, `arxiv.org`, `cosn.org`, `marylandpublicschools.org`, `njsba.org`,
  `web.ped.nm.gov`, `excelined.org`, `marketbrief.edweek.org`,
  `edtechinnovationhub.com`, `www2.fundsforngos.org`, `en.wikipedia.org`,
  `rachel.worldpossible.org` (and `rachel.core2learn.org`). **Trends 25 and 26
  rest entirely on corroborated search summaries.** This is the largest block of
  Tier 2 material this KB has admitted to its durable files; it is labelled as
  such in every table, and it should be the first thing the next pass tries to
  upgrade if egress changes.
- **Seven of cohort 2's eight grantees are unnamed.** Announced 21 Sept 2026;
  only **MMSA & TERC** surfaced. Each unnamed award is an Apache-2.0-or-better
  artefact with a named owner landing inside twelve months — **the single
  highest-value lookup available to the next pass.**
- **Vendor filings remain unswept.** The eighth pass named three North America
  sub-channels: district RFPs ✅, state procurement portals ✅, **vendor filings
  ❌**. Earnings calls, S-1s and 10-Ks of listed edtech vendors are a distinct
  channel and would speak to consolidation and pricing, which no channel in this
  KB currently covers.
- **EMEA and APAC general queries have now failed twice consecutively.** Both
  returned enterprise AI-governance material, not education. The
  **ministry-engineering-org** channel that produced the UK DfE estate this pass
  is the obvious replacement for both and has not been run outside the UK.
  Recorded as exhausted channels, not as regional stability.
- **SciEval and EduEVAL-DB are leads, not findings.** `arxiv.org/pdf/2604.25472`
  and `arxiv.org/pdf/2602.15531` are EGRESS_BLOCKED and a GitHub name sweep
  returned **no repository** for either. Both are directly on the evaluation gap
  and should be re-probed when arXiv is reachable.
- **This KB's licence probe had a spelling bug for nine passes — and the fix was
  already written down.** Pattern **P22**'s gate lists `LICENCE`; **no recorded
  sweep ever ran it**, and **three of six UK ministry MIT grants use it.** Every
  negative result in this pass was re-run against the British spellings and
  survived, but **earlier passes' "ungranted" verdicts on Commonwealth, MEA and
  ministry-adjacent repositories were produced by a query that could not have
  found a British-spelled grant** and are unconfirmed until re-probed. This is
  the seventh instance of the probe-vocabulary failure mode and the first that
  invalidates prior conclusions rather than merely missing new ones.

## Declared gaps — tenth pass, 2026-10-06

- **No permissive Caliper Analytics implementation.** Searched with the licence
  filter; the result set is dominated by two unrelated projects sharing the name.
  If an RFP scores learning-analytics event streams, it is a build.
- 🔵 ~~**No Python LTI 1.3 library.**~~ **CLOSED, twenty-fourth pass of 2026-10-07.**
  [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — MIT, head commit **2 d**, PyPI
  `django-lti` **v0.10.1 (61 d)**. Django-coupled; `jupyterhub/ltiauthenticator` (BSD-3, 98 d)
  covers JupyterHub. ⚠️ Still open in the narrow form, but **narrowed again** in the
  twenty-fifth pass: the framework-agnostic slot holds exactly one candidate,
  [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0 (103 d)**, a 0★ alpha that
  **vendors** the abandoned `PyLTI1p3` rather than replacing it and whose `LICENSE` names
  `Dmitry Viskov` rather than its own authors.
- **No gradebook in the permissive OneRoster shelf.** `theopenem/OneRoster.NET`
  states it: rostering calls only, grade book not implemented.
- **`OpenLiteracy` returns 0 GitHub repositories**, as do `tutoring quality
  evaluation benchmark license:apache-2.0` and `formative assessment dataset
  classroom`. Three funded, named, dated projects; three measured zeros. **Read
  these three zeros against trend 29** — they are measurements of GitHub's licence
  index, not of the world.
- **Five of the eight Cohort 2 grantees of the $26M programme remain unnamed.**
  Harvard (Ying Xu), Maryland (Jing Liu) and MMSA & TERC are known.
- **The oral reading fluency shelf is two repositories**, one MIT with a single
  commit (`prosody`), one with no licence payload (`ReaDirect-V2`), neither with a
  star. The sixth pass's *"does not exist"* wording is **retired** in favour of
  this denominator.
- **The vendor-filings channel is unreachable, not unswept.** `www.sec.gov` is
  `EGRESS_BLOCKED`. McGraw Hill's and Workday's FY2026 open-source and
  copyleft-risk disclosures are Tier 2 only. The next pass needs a different host,
  not a better query.
- **No primary document was read, and 23 distinct hosts have now been attempted
  across two passes with zero reachable** — including three syndicated mirrors
  tried specifically to bypass a blocked primary host. Every market, funder,
  regulatory and procurement figure in these files is **Tier 2**.
- **Two Learning Equality repositories are ungranted** —
  `kolibri-design-system` and `kolibri-server`, no payload under 20 probed URLs —
  inside an organisation whose other five probed repositories are MIT. **Licence
  posture is not inherited; probe each repository.**
- **The fork direction between `theopenem/OneRoster.NET` and
  `jdolny/OneRoster.NET` is not established.** Byte-identical README and licence,
  both naming `theopenem` as holder; `github.com` returns 403 to `curl` here and
  the rendered page carries no fork banner. Pin the holder-matching copy.
- **APAC's `E-EVAL` and nine LATAM-placed language/hackathon repositories remain
  ungranted after a full 20-URL re-probe.** These negatives now hold under a
  stricter method than the one that produced them, which makes them usable: the
  blocker is licensing, not capability, and not this KB's reach.

## 31. The pedagogy benchmark is no longer missing — it is licensed shut

For three passes this KB recorded the evaluation void as an *absence*: nothing to
measure a tutor against, a $26M philanthropic programme funding the artefact, and an
engagement line that said *build the harness and wait*. Measured properly on
2026-10-06, the absence was a search artefact. **The benchmarks exist. The grants
do not.**

| Benchmark | Institution | ★ | Grant, read from the payload | Usable in client work? |
|---|---|---|---|---|
| `Khan/tutoring-accuracy-dataset` | **Khan Academy, Inc.** | 57 | Custom **"Evaluation Dataset License"** — internal, **non-commercial evaluation only**; **no redistribution, no model training, no production use**; viral over combined datasets. Carve-out: evaluating products *intended for commercial use*, and commercial use of the **insights**, are permitted. | ⚠️ **Borrow, never ship** |
| `eth-lre/mathtutorbench` | **ETH Zurich** (EMNLP 2025 Oral) | 43 | **No payload.** README asserts **CC BY 4.0** in a badge and **CC BY-SA 4.0** in the body. | 🔴 **Ungranted** |
| `Yunfeng-Wan/CSTutorBench` | — | 2 | **CC BY-NC-4.0** | 🔴 **NonCommercial** |
| `shivanireddyk/tutoreval` | one author | 0 | **MIT** | ✅ — and it is a weekend project |

**This is a different trend from "there is no benchmark," and it changes the
deliverable.** A void is filled by building. A wall is navigated by **separating the
instrument from the artefact**: the harness and the rubric are yours and permissive;
the datasets are called at measurement time under their own terms and never vendored,
never trained on, never handed over. The number you deliver is the finding — and
Khan's licence explicitly permits you to bill for it.

The second-order effect is a market one. **An industry whose only credible quality
benchmarks are non-redistributable cannot standardise on them.** Every vendor
measures privately against instruments it cannot publish results from in a
comparative form. That is precisely the condition that makes the EMEA route — a
*reference framework* for evaluation, written as a rule (trend 27) — more durable
than the North American route of funding open artefacts, and it is why a
**permissively licensed pedagogical benchmark is the highest-value open-source
contribution available in this industry right now.** It is a licensing contribution,
not a code one.

## 32. The evaluation tooling for education is being written by governments, and it is permissive

The three most capable evaluation instruments on these shelves are not vendor
products and not academic one-offs:

| Instrument | Who maintains it | Licence | Scale |
|---|---|---|---|
| **Inspect** (`UKGovernmentBEIS/inspect_ai`) | **UK AI Security Institute** | **MIT** | **2,945★**, 779 forks, pushed 2026-10-06 |
| **Moonshot** (`aiverify-foundation/moonshot`) | **AI Verify Foundation** (Singapore **IMDA**) | **Apache-2.0** | 355★, 72 forks, pushed 2026-10-06 |
| **Sunbird** (`project-sunbird/*`) | India's national platform programme | **MIT** | deployed at national tier; 🔴 dormant since 2024 |

**A pattern worth naming: the public sector is now the most reliable source of
permissively licensed AI infrastructure in this industry.** Private open-source
education platforms in this KB trend AGPL-3.0 (LearnHouse 2,320★, CourseLit 1,269★,
Obojobo, Materia) or GPL (Moodle, i-educar, OpenEMIS). The MIT and Apache-2.0 assets
at comparable scale are governmental or government-adjacent: UK AISI, Singapore IMDA,
India's Sunbird, France Université Numérique's Richie (MIT), Switzerland's OpenOLAT
(Apache-2.0), the Ed-Fi Alliance (Apache-2.0).

Three consequences for how an engagement is built and sold:

1. **The permissive layer and the copyleft layer have swapped places.** The
   conventional assumption is permissive infrastructure underneath and copyleft
   applications above. In education it is now **copyleft platforms underneath and
   permissive, government-built evaluation and interoperability tooling around
   them.** Put the client-visible AI in the permissive layer — portal tier (Richie,
   MIT), evaluation tier (Inspect, MIT), protocol tier (pylti1.3, MIT) — and the
   copyleft stays behind an interface.
2. **A government licence is a procurement argument.** "The evaluation harness is
   the UK AI Security Institute's, MIT-licensed" answers a ministry's question about
   independence in one sentence, in a way no vendor claim does.
3. **But a government repository is not a maintained dependency by default.**
   Sunbird is MIT, at national scale, and has not been pushed to since August 2024,
   with one component archived. Inspect and Moonshot were both pushed on the day of
   this pass. **Check `pushed_at`, not provenance.**

## Declared gaps — eleventh pass, 2026-10-06

- **No permissively licensed tutoring-evaluation benchmark exists.** Trend 31. Four
  instruments, one MIT and at 0★. **The gap worth a Globant contribution**, and the
  contribution is a licence, not an algorithm.
- **No oral reading fluency product exists.** Re-measured with the API: **4
  repositories, 6 including forks.** One MIT (`prosody`, 0★, 1 commit), one
  BSD-2-Clause-plus-contribution-clause Android app from 2017 (`labaaoom`, 1★), one
  ungranted even on its real default branch (`ReaDirect-V2`, branch
  `deployment/playstore`), one 0★ calculator. The capability gap stands; the count is
  now exact rather than approximate.
- **`OpenLiteracy` → `total_count` 0.** The Harvard/Ying Xu early-reading project
  funded to close exactly that gap still has no public repository.
- **The Caliper reference implementation is not obtainable.** 1EdTech moved it to
  private repositories on **2023-06-17**; `imsglobal/caliper-python` and
  `concentricsky/badgr-server` both 404, and surviving public forks are 0★. The
  learning-analytics half of the interoperability tier is behind a membership while
  the LTI half stayed open. **Do not promise Caliper emission without pricing a
  membership or a clean-room build.**
- **Five of the eight Cohort 2 grantees of the $26M K-12 AI Infrastructure Program
  remain unnamed, and this gap is not closeable from this environment.** Naming them
  needs a primary document; 23 distinct hosts carrying one were attempted across the
  ninth and tenth passes and **all 23 returned EGRESS_BLOCKED**. Recorded as closed
  to this instrument so no further pass rediscovers it.
- **The LATAM-origin repository shelf does not exist.** `educación IA aprendizaje` →
  10 repositories, **all 0–1★**, one of them a satirical art project. Fifth
  consecutive pass at 0–9★, first measured with a count.
- **~155 of the 172 addresses dropped by this repository's reset are still
  unrecovered**, including the Ed-Fi stack, LibreTexts, OpenStax, the Nextcloud AI
  apps, the xAPI/LRS tier, ~16 Moodle AI plugins and ~20 education MCP servers. They
  are listed in `archive/2026-10-06-pre-reset/`. **A pass spent there will out-yield
  a pass spent on the open internet.**

## 33. The permissive set includes two more licences the standard filter rejects — and one of them is education's own

Trend 15 established that "permissive" is a bigger set than MIT, Apache and BSD. This
pass found the two entries that matter most for this industry, and the first one is not a
curiosity:

**ECL-2.0 — the Educational Community License 2.0.** OSI-approved. It is **Apache-2.0
with exactly one modification**: the patent grant is narrowed so that a contributing
university licenses patents only for the work it contributed, rather than across its
whole portfolio. That clause exists because technology-transfer offices would otherwise
veto university participation in open source. For redistribution and commercial use, it
behaves as Apache-2.0.

It covers the **Apereo** estate — the consortium behind **Sakai** and a large share of
higher education's shared infrastructure. A `license:mit OR license:apache-2.0` filter
rejects all of it. This KB's own filters have been doing so for eleven passes.

**ISC.** OSI-approved, functionally MIT, shorter. It carries
[pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) — a **QTI 2.1/2.2/3.0
player** with bidirectional QTI ↔ PIE transforms, copyright **© 2026 Renaissance
Learning**, a commercial assessment vendor.

**The permissive allow-list for this KB is therefore: MIT, Apache-2.0, BSD (2- and
3-clause), ISC, ECL-2.0.** MPL-2.0 sits just outside it as **file-level weak copyleft** —
usable in a mixed deliverable with per-file discipline, which is a different and much
cheaper constraint than AGPL's network-use clause.

⚠️ **A licence being usable does not make the code usable.** All three ECL-2.0
repositories found this pass have been **archived and read-only since 2019-01-31**. The
right conclusion is "add ECL-2.0 to the filter", not "adopt Apereo's analytics stack" —
for which the live permissive answer is the ADL/Yet Analytics xAPI chain.

## 34. Education's reusable IP lives at the plugin seam of copyleft platforms, not beside them

The most-deployed platforms in this industry are copyleft: **Moodle** (GPL-3.0),
**Open edX** (AGPL-3.0), **OpenEMIS** (GPL-2.0), **i-educar** (GPL-2.0). Eleven passes of
this KB priced that as a constraint on reusable studio IP. **It is more precisely a
constraint on where the IP sits.**

[openedx/XBlock](https://github.com/openedx/XBlock) — the **plugin SDK** that every Open
edX course component is written against — is **Apache-2.0** at **470★**, while the
platform core it plugs into is AGPL-3.0. A component written against the XBlock API is
**yours**, under whatever licence you choose, provided it stays a plugin consumed through
the published API rather than being linked into the platform tree.

Moodle shows the same architecture with the opposite default: its **in-tree** AI plugins
are GPL-3.0 (correctly — 8 of 8 verified this pass), while
[peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server), which reaches
Moodle data **from outside the tree**, is MIT. This KB has recorded that licence-boundary
note for several passes; XBlock generalises it.

**The pattern, stated as a rule for engagement design:**

| Where your code sits | Licence you inherit | Reusable as studio IP |
|---|---|---|
| Inside the platform tree | The platform's (GPL/AGPL) | No |
| Against a **published plugin API** | **Your choice** | **Yes** |
| Outside the platform, over MCP / REST / LTI | **Your choice** | **Yes** |

**So the architectural decision that determines IP ownership is made before any code is
written**, and it is not a licence decision — it is a packaging decision. The LATAM
`TutorIA` specification on this KB's agent shelf already chose correctly
(*"delivered as an Open edX XBlock/plugin"*) without, as far as its documents show,
knowing that the SDK was Apache-2.0.

⚠️ **Get the packaging reviewed by counsel, not by a licence-file read.** The AGPL reaches
derivative works, and whether a plugin is one is a question about linkage and distribution,
not about which repository the licence file lives in.

## 35. Ungranted code clusters by the type of body that published it, not by region

Across the 66 repository addresses resolved this pass, **11 carried no licence grant at
all** — measured against 30+ filename variants on each repository's real default branch,
so these are absences of a grant rather than failures of a probe. They are not scattered:

| Publisher type | Ungranted found | Examples |
|---|---|---|
| **Public-sector bodies and standards groups** | 5 | DG EMPL (`european-digital-credentials`), **FWU** Germany (2 school ontologies), **DINI-AG-KIM**, **IMDA**'s `LLM-Evals-Catalogue` |
| **Individual-maintainer LMS plugins** | 3 | `moodle-tool_aiconnect`, `moodle-local_aihub`, **`moodle-ai-graded-assignment`** |
| **Academic content repositories** | 1 | **`CAHLR/OATutor-Content`** — the content of an **MIT** engine |
| **LATAM individual projects** | 2 | `tutor-adaptativo-ia`, `API-EduAdapt` |

**The inversion is the finding.** The bodies whose output is *most* reusable in principle —
ministries and standards groups publishing curriculum vocabularies and credential models,
whose entire purpose is shared infrastructure — are the **least likely** to attach a grant.
Meanwhile the individual developers publishing tutoring apps mostly do attach one.

**Three operational consequences:**

1. **Organisation-level licence inference is unsafe, even inside a regulator.** The
   `aiverify-foundation` organisation has two Apache-2.0 repositories and one ungranted
   one. Read every payload.
2. **The engine and its content are separately licensed, and the content is the pedagogy.**
   `CAHLR/OATutor` is MIT; `CAHLR/OATutor-Content` — the problem bank and hint trees — is
   ungranted. Anyone scoping an OATutor deployment on the strength of the engine's licence
   has mispriced the asset.
3. 🟢 **Asking is the cheapest unblock in this industry.** A ministry can attach a licence
   in one commit, and the usual reason there is none is that nobody asked. This belongs in
   the first fortnight of a public-sector engagement, in **every** region — it is not an
   EMEA peculiarity, it is a property of public-sector publishing.

## 36. The compliance instrument differs in *kind* by region, and that determines the deliverable

Trend 27 recorded two instruments closing the evaluation void — a cheque and a rule. With
APAC's harness verified this pass, the full picture is that **each region specifies AI-in-
education compliance through a different *kind* of artefact**, and a proposal written for
one region's instrument does not transfer:

| Region | The instrument | Its nature | What you actually deliver |
|---|---|---|---|
| **North America** | State statutes + **district procurement rubrics** (134 bills / 31 states; Ohio's July 2026 written-policy deadline) | A **scoring sheet** and a set of prohibitions | Evidence that scores: Ed-Fi/OneRoster/xAPI conformance, a policy and inventory pack, human-oversight procedures |
| **EMEA** | **EU AI Act**, enforcement from **2 Aug 2026** | A **statute** with a conformity-assessment duty | A conformity file for a high-risk system, before deployment |
| **APAC** | **AI Verify** (IMDA Singapore, **Apache-2.0**) plus binding national laws (Korea 22 Jan 2026, Vietnam 1 Mar 2026, Australia's TEQSA plans) | An **open-source test harness**, extensible by plugin | A **test plugin inside the regulator's own harness** — plus the national readiness documents |
| **LATAM** | 🔴 **Nothing regional.** Brazil's bill, Chile's framework, Colombia's CONPES, Mexico's sectoral rules, all at different speeds; **UNESCO** warns institutions use GenAI without policies | An **institutional vacuum** | The institution's own governance layer — there is no external artefact to conform to |

🆕 **APAC's shape is the strongest of the four and it exists in no other region.** When the
regulator publishes its conformance harness under Apache-2.0 **and** ships a plugin kit
(`aiverify-developer-tools`), compliance evidence can be produced **by the regulator's own
instrument** rather than asserted by the vendor — and an education-specific test profile can
be contributed upstream, where it becomes a reference other implementers must meet.

🔴 **LATAM's shape is the weakest, and it is why the governance engagement is the regional
engagement.** With 92% student and 79% faculty adoption and no instrument at any level, the
deliverable is not conformance — it is the institution's first policy.

## 37. Measured by language rather than by region, the LATAM supply gap is absence, not thinness

Five passes of this KB measured "the LATAM shelf" and found repositories at 0–9★, and
described the result as **thin**. All five measured in **Spanish**.

Measured this pass with `total_count`:

| Query | Result |
|---|---|
| `tutor IA educación aprendizaje` (**Spanish**) | **3** — all 0–1★, one of which no longer resolves. **Live shelf: 2.** |
| `tutor inteligência artificial educação aprendizagem` (**Portuguese**) | 🔴 **0** |

**Brazil is the largest education system in Latin America, and the Portuguese-language
permissive AI-tutoring shelf is empty.** Not immature, not low-star: zero. "Thin" was the
wrong word for a condition that is, in half the region, absence — and the word was wrong
because the measurement was monolingual.

**The generalisable lesson is about measurement, not about Brazil.** A region is not a
language, and a supply claim about a region measured in one of its languages is a claim
about that language. This KB's regional vocabulary is correctly closed to five values
(trend hygiene the compiler depends on), but **the probe underneath a regional claim has to
enumerate the region's languages.** APAC is the obvious next case: every APAC measurement in
this KB to date has been in English or Chinese, which leaves Hindi, Bahasa, Japanese, Korean
and Vietnamese unmeasured — and trend 21's mother-tongue finding says that is where the
demand is.

**What Brazil does have** is copyleft and consequential: `yunger7/enem-api` (**GPL-2.0**, an
API over the national university-entrance exam), `portabilis/i-educar` (GPL-2.0, the largest
free school-management platform), `moodle-mod_maici` (GPL-3.0). And exactly one permissive
Portuguese asset: `thiagoluzin/pemara-edu-mira` (**MIT**, 0★) — whose architecture, **school
LAN, offline-capable, optional AI**, is the regionally correct one.

🟢 **For a LATAM-rooted firm this is the cheapest durable position in this entire KB**: at
`total_count: 0` there is no incumbent to displace, and the publishing cost is one competent
MIT component.

## 38. The permissive AI-native frontier is state-funded and non-Western — and its legal holder is harder to identify than its licence

Trend 14 recorded that the permissive shelf stopped being thin, so the differentiator moved.
Trend 15 recorded that *permissive* is a bigger set than three licence names, and that open
core hides inside directories. This pass puts a third fact beside them, and it changes who
a Globant engagement cites as a reference.

**The most capable permissive AI-native education platform available today is Moroccan and
government-funded.** [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
— **BSD-3-Clause**, 108★ / **192 forks** — ships multi-model tutoring, **local RAG**,
voice/video/**3D-avatar** modes and **RBAC**, and serves **Ollama** in the same
configuration surface as hosted APIs. It comes from the **IRF-SIC Laboratory at Ibn Zohr
University, Agadir**, with the **CRMEF Souss-Massa**, funded by Morocco's **Ministry of
Higher Education**, the **Digital Development Agency** and the **CNRST**.

Set that against the rest of the AI-native permissive field as this KB has measured it:
Mentingo (MIT, a Polish consultancy), Coursemology (MIT, NUS Singapore), Sunbird (MIT, an
Indian foundation at national scale), Oppia (Apache-2.0, a US-origin non-profit). 🟢 **Not
one of the leading permissive AI-native education platforms is a Western commercial
product.** They are **universities, foundations, ministries and small consultancies** —
publishing bodies, in the sense of trend 35. The commercial AI-education market is
proprietary; the permissive shelf that market sits on is **public-sector and academic**,
and increasingly **Global South**.

### The consequence for delivery

🟢 **The sovereign deployment stopped being a build and became a configuration.** Every
pattern in this KB from **P4** onward specifies the data-residency stack component by
component — on-prem serving, local retrieval, typed outputs, checkpointed audit trails —
because no platform shipped it. One now does, under a permissive licence, with a
government as its sponsor. **P33** is the shape that follows.

🟢 **And the reference changes.** A public-sector education buyer in EMEA or LATAM asking
whether sovereign AI tutoring is real can be pointed at a **ministry-funded production
project**, not a vendor pilot. That is a materially different procurement conversation.

### The warning that travels with the trend, and it is the new part

🔴 **On a state-funded academic project, the licence is clean and the holder is not.** The
payload reads:

```
Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev
All rights reserved.
```

**`R2D-dev` appears in no public artefact of the project** — not the README, not the
documentation, not the search index. The grant is an unambiguous BSD-3-Clause; the entity
holding it cannot be identified. On a redistribution engagement, the holder is the party a
warranty or indemnity question routes to.

This is trend 15's Langfuse lesson generalised. There, the finding was that *the copyright
holder on a dependency can change under you between passes, and no licence probe will flag
it*. Here it is sharper: **the holder can be unidentifiable from the outset**, and a
licence probe reports the component as fully clear. ⚠️ **A licence check is not a
provenance check.** Record **who grants** alongside **what is granted** — for an academic
or ministry-funded project the two are routinely answered by different documents, and
sometimes the first is not answered at all.

🔵 **Three shapes to probe for, now that the pattern is named:** `All rights reserved.`
sitting above a permissive grant (vestigial, but it stops procurement reviewers); a
copyright range that ends before the current year on an actively developed repository; and
a holder named as an organisation that has no web presence. **None of the three invalidates
a grant. All three are questions a client's counsel will ask**, so answer them in the
diligence pack rather than at the meeting.

## Declared gaps — twelfth pass, 2026-10-06

- 🔴 **No public Caliper reference implementation survives in any language.** The eleventh
  pass established that `IMSGlobal/caliper-python` went private on 2023-06-17. This pass
  confirmed it with a second instrument **and found `1EdTech/caliper-php` is gone too**.
  There is no second language to fall back on. **Do not promise Caliper emission without
  pricing a 1EdTech membership or a clean-room build.** The xAPI alternative *is*
  permissive end to end (profile → pipe → store → conformance suite, all MIT/Apache-2.0),
  so this is a standards choice to make at proposal time, not a capability gap.
- 🔴 **No permissive Open Badges server.** `concentricsky/badgr-server` is gone, confirmed
  twice. Trend 8's verifiable-credential half still has no permissive server implementation.
- 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07.** This read *"the Python LTI 1.3 tier is
  `total_count: 4` and one library deep… budget a fork from day one"*. 🔴 **`total_count: 4` was a
  property of the search index, not of the world** — trend 29's own thesis, applied here late. The
  measured tier is **six implementations**: [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
  (MIT, **2 d**, PyPI `django-lti` v0.10.1), `jupyterhub/ltiauthenticator` (BSD-3, 98 d),
  `openedx/xblock-lti-consumer` (🔴 **AGPL-3.0**, 6 d), `eduNEXT/openedx-lti-tool-plugin`
  (Apache-2.0, ⚠️ 443 d, not on PyPI), `Harvard-University-iCommons/django-lti` (MIT, 🔴 406 d fork)
  and `dmitry-viskov/pylti1.3` (MIT, 🔴 1,416 d). 🟢 **Do not budget a fork** — take `django-lti`.
  ⚠️ The Java side is healthier only on paper: `UOC/java-lti-1.3-provider-example` is **1,418 days
  cold**, measured pass 23.
- 🔴 **No permissive Apache-2.0 AI grading tool.** `automated grading rubric LLM education
  license:apache-2.0` → **`total_count: 0`**. The only permissive answer in this KB remains
  `Selleo/mentingo` (MIT). ⚠️ And a Moodle plugin for the function exists and is
  **ungranted** (`alvarogregori/moodle-ai-graded-assignment`) — the supply is there and the
  grant is not.
- 🔴 **`CAHLR/OATutor-Content` is ungranted.** The MIT engine on this KB's core shelf has an
  **unlicensed content repository**. Its problem bank and hint trees — the pedagogy, i.e.
  the asset — cannot be redistributed. **New this pass, and it changes how OATutor should
  be scoped.**
- 🔴 **The Portuguese-language permissive shelf is `total_count: 0`.** Trend 37. **The
  single clearest contribution opportunity in this KB**, and the contribution is a
  published component, not a licence.
- 🔴 **No oral reading fluency product exists.** Re-measured independently: `total_count: 4`,
  the same four repositories as the eleventh pass (`prosody` MIT 0★; `labaaoom` 2017,
  `NOASSERTION`; `ReaDirect-V2` ungranted on branch `deployment/playstore`; `ORF_Calculator_6th`
  0★). **Holds, now reproduced by two passes with the same count.**
- 🔴 **`OpenLiteracy` → `total_count: 0`.** Still no public repository for the Harvard/Ying Xu
  early-reading project funded to close that gap.
- 🔴 **No education test profile exists for AI Verify.** `aiverify-developer-tools` is
  Apache-2.0 and built for exactly this, and nothing education-specific has been contributed.
  **New this pass. The highest-leverage upstream contribution available in APAC**, because it
  lands inside the regulator's own instrument.
- 🔴 **~89 archive addresses remain unrecovered**, down from ~155. The largest untouched
  block is the **~20-server education MCP cluster** — and **2 of the 4 dead addresses found
  this pass were MCP servers**, so expect decay there and record it as supply data rather
  than re-declaring it as absence.
- ⚠️ **Every "ungranted" verdict in this KB older than the twelfth pass is suspect.** The
  13th failure mode — **case-sensitive licence filenames** — turned a **470★ Apache-2.0**
  repository (`openedx/XBlock`, at `LICENSE.TXT`) into a false absence in this pass's own
  first sweep, and earlier passes used lowercase-only probe sets. **A retroactive re-probe
  with case variants is owed**, and it is cheap.
- ⚠️ **A `total_count` is an upper bound, not a census.**
  `junjie1005/Plataforma-IA-Educativa-Rutas-Personalizadas` is listed by the search index
  and unreachable via `git ls-remote`. Counts from the index should be stated as "indexed",
  and existence confirmed separately, before a count is quoted as a measurement.
- ⚠️ **APAC has never been measured in its own languages.** Hindi, Bahasa Indonesia,
  Japanese, Korean and Vietnamese queries have not been run by any pass of this KB, while
  trend 21 says mother-tongue capability is where the demand sits. **Declared as an
  unmeasured region-language pair, not as an absence** — the LATAM lesson of trend 37 is
  precisely that those are different claims.

## Declared gaps — thirteenth pass, 2026-10-06

**The twelfth pass's gaps all stand.** Nothing above was closed by this pass, and the
Caliper, Open Badges, LTI-Python, AI-grading, OATutor-Content, OpenLiteracy, AI-Verify-profile
and oral-reading-fluency gaps should be read forward unchanged. What follows is what this
pass changed, closed or newly measured.

- 🟢 **Partly closed: "APAC has never been measured in its own languages."** This pass ran
  the mandatory queries in **Japanese** and **Korean** — the first pass of this KB to search
  in either. ⚠️ **The result is a negative, and it is a real measurement.** Japanese
  returned **no education-specific asset at all** (the generalist agent layer, same as
  English). Korean returned **5 candidates, 1 licensed** — and the licensed one
  (`HKUDS/ClawTeam`, MIT, 5.5k★) is **software-engineering infrastructure, not education**.
  🔴 **Still unmeasured: Hindi, Bahasa Indonesia, Vietnamese.** The gap narrows to three
  languages and should not be re-declared as five.
- 🟢 **Confirmed on harder evidence: the Portuguese-language permissive shelf.** Trend 37
  was derived from a two-language instrument. This pass searched **in Portuguese** and found
  **4 candidates, 2 licensed (MIT), at 2★ and 0★**
  (`bonafe/inteligencia-aberta`, `armandokeller/SAEP2026-Agentes-IA-e-Ferramentas`). ⚠️ The
  gap is therefore **no longer `total_count: 0`** — it is *"two MIT assets, neither adopted,
  one not education software"*. **The contribution opportunity of P32 stands and is better
  evidenced**: the absence is of *adopted, reusable* components, not of activity.
- 🔴 **NEW — three forges are unreachable, so the non-GitHub supply picture is unmeasured,
  not empty.** `codeberg.org` (the EU sovereignty forge), `gitee.com` (the China-domestic
  forge) and the European Commission's **Joinup / OSOR** catalogue all return **403 at the
  egress proxy**; `arxiv.org` and `alphaxiv.org` are blocked for the third consecutive pass.
  Every licence fact in this KB rests on `raw.githubusercontent.com` because **it is the
  only code-hosting payload this environment can read**. Two named Codeberg education
  projects — **`lerntools`** (German, privacy-focused digital education) and
  **`lmemsm/delightful-educational-games`** — were surfaced and **deliberately left off every
  shelf**, because an unverifiable row is not a finding. ⚠️ **Read this KB as the permissive
  education shelf *on GitHub*.** The EMEA and APAC pictures are understated by an unknown
  amount, and the EU-hosted forge is precisely the blind spot for the sovereignty story this
  KB sells.
- 🔴 **NEW — avatar-based pedagogy has no obtainable permissive implementation.** The
  **VTutor** cluster has three arXiv papers (`2502.04103`, `2505.06676`, `2505.07736`), a
  live demo and a claimed **CC BY 4.0** licence. Reality: the SDK repository
  (`anonymousStars/vtutor-sdk`) has **no licence payload** across 13 filenames and sits under
  a peer-review anonymisation handle, and the organisation the papers name as its home —
  **`VTutorTools`** — **exists with zero public repositories**. ⚠️ **A new failure mode: the
  named home exists and is empty** — distinct from a dead address and from a mislabelled
  licence. And **CC BY 4.0 is a content licence being applied to an SDK**, which is trend 18
  one step further along. 🟢 The capability is reachable today only by composing
  `livekit/livekit` (Apache-2.0) with the avatar mode `open-tutor-ai-CE` already ships under
  BSD-3-Clause — **pattern P33**. VTutor is a **watch item, not a component**.
- 🔴 **Unmoved for the eighth pass: the Arabic ask.** `781991937/TOFAN-AI-2026` was
  re-probed independently this pass on its real default branch across 13 filenames —
  **still no grant**. The Arabic channel went **0 for 3**. ⚠️ Restating this gap in this file
  has not moved it in eight passes. **The action is an issue opened on the repository**, and
  that is what the next pass should carry rather than another re-probe.
- ⚠️ **NEW — the 14th failure mode: a permissive body with no title line.** A licence
  classifier that matches the payload's **heading** reports a bare **BSD-3-Clause** body as
  *unclassified*, and an automated allowlist gate rejects a genuinely permissive component.
  `open-tutor-ai-CE` is the live example; `crewAIInc/crewAI` is the same shape recorded
  earlier as a parenthetical rather than as a property of the instrument. 🟢 **Classify on
  the operative clauses, not the heading.** Together with the 13th failure mode
  (case-sensitive filenames), **the retroactive re-probe already owed should also drop the
  title-line assumption.**
- ⚠️ **NEW — a trending-log entry is not a shelved asset.** The twelfth pass verified
  `open-tutor-ai-CE` correctly and left it only in `repos/trending.md`; for a day, the best
  permissive AI-native platform available to this practice was absent from `agents/top.md`
  and `verticals/solutions.md`. 🟢 **Rule: a payload-verified asset is shelved in the same
  pass that verifies it.** The ~89 unrecovered archive addresses and the **~20-server
  education MCP cluster** should be worked under that rule — **probe, then shelve what the
  probe grants, before moving on.**
- ⚠️ **NEW — the demand side is saturated at this channel's resolution.** All four regions'
  market figures and regulatory instruments were re-run this pass and came back
  **unchanged**. Future passes should spend their budget on **supply** and re-run the demand
  queries only to catch a regime change — the same discipline already applied to the
  generalist GitHub query, which has now returned **zero new rows for nine consecutive
  passes** (fourteen for the infrastructure query).

## 39. Integration coverage follows the higher-education install base, and K-12 administration is an empty tier

Measured this pass for the first time: the number of open-source integration repositories per
education platform, one platform name per query, licences read from payloads.

| Platform | Integration repos | Best permissive, payload-backed server |
|---|---|---|
| Canvas LMS | **117** | MIT, 278★ |
| Moodle | **86** | MIT, 43★ (+ MIT 18★ new) |
| Brightspace / D2L | **23** | MIT, 57★, on npm |
| Google Classroom | **17** | MIT, **6★** |
| Blackboard Learn | **5** | MIT, 2★ |
| Open edX | **1** | AGPL-3.0 |
| 🔴 PowerSchool (US K-12 SIS) | **0** | none |

**Canvas and Moodle hold 203 of the 249 repositories.** Blackboard, with a large global
university estate, has five. Google Classroom — the widest K-12 reach on the table — has
seventeen, and its best *dedicated* server has six stars. PowerSchool measures zero.

🔵 **The trend is not "K-12 is underserved"; it is that supply tracks who can get
credentials.** An individual developer can obtain a Canvas or Moodle token for their own
course in minutes. Nobody can obtain a district student information system token for a
weekend project. So the open-source tier maps almost perfectly onto *self-serve
authentication*, and stops exactly where institutional authorisation begins.

**Three consequences that decide how an engagement is priced.**

1. **In higher education the connector is not differentiating.** It exists, it is MIT, and it
   is duplicated. Sell configuration, governance, pedagogy and the audit trail.
2. **In K-12 administration there is nothing to adopt and nothing to compete with**, and the
   barrier that emptied the tier — institutional credentials — is one an enterprise
   integrator clears as a matter of course. This is the clearest build-versus-adopt signal
   this KB has produced.
3. **The empty tier and the regulated tier are the same tier.** Student records, guardians,
   enrolment, accommodations. The absence of hobbyist code is not an absence of demand; it is
   the regulated surface declining to be built by hobbyists.

⚠️ **The counter-reading to keep in view:** a tier at `total_count: 0` may also be a tier
served entirely by the platform vendor's own paid integrations. Zero open repositories is a
statement about the open-source shelf, not about whether a client currently has an
integration.

## 40. The MCP server has become a product shape, and the catalogue it is listed in is mostly closed

The official MCP Registry was censused first-hand this pass: **11,505 unique servers** across
31,300 version rows. Filtered on education vocabulary with word boundaries: **102 servers, of
which 71 (70%) carry no source repository at all.**

🔵 **The education tier of the registry is a directory of hosted commercial endpoints with
open-source entries mixed in.** Among the 71: **`com.moodlemcp/moodle`** — *"Connect your
Moodle to AI assistants: courses, content, grading"* — a **closed, hosted connector competing
directly with the 86 open repositories** in that platform's tier; `io.cubite/lms` (hosted LMS
with SCORM/xAPI); `com.skillsail/mcp` (SCORM authoring and export); and a dense US
school-data cluster (`ai.edusignal/districts`, `co.schoolscope/mcp`, `ai.sacs/sacs-mcp`,
`com.olyport/nces-education`, `com.olyport/college-scorecard`).

**What changed, stated as a change:** for two years the open-source education stack competed
with proprietary *platforms*. It now also competes with **proprietary connectors to open
platforms** — a thin, high-margin layer sold in front of software the client already hosts
themselves. That is the same layer a Globant deliverable occupies.

**So the differentiator moves to the three things an endpoint cannot offer**, and they are
the three a client cannot get from a service they do not host: **the code**, **deployment
inside their own boundary**, and **the audit trail**. Keep an observability layer in the stack
(Langfuse, MIT outside `ee/`) so the third is a by-product of running rather than a separate
compliance project.

⚠️ **And a vocabulary warning for proposals.** "It's in the MCP registry" now sounds like a
provenance claim and is not one: the registry says nothing about a licence, **one of six
sampled entries points at a repository that no longer exists**, and its `?q=` search
parameter returns HTTP 200 with the unfiltered page. Being listed is marketing; the payload
is provenance.

## 41. What places an asset is the institution, not the language — and the institution's name is searchable in English

Trend 37 concluded that measured by language rather than region, the LATAM supply gap is
absence rather than thinness. The thirteenth pass then tested language directly — Japanese,
Korean, Arabic, Portuguese — and got **3 licensed finds from 12 candidates (25%), only one of
them education software**, concluding that language was the wrong variable.

This pass replaced the variable with the **name of the platform the asset integrates with**,
run one name at a time: **16 licensed from 20 candidates (80%), and all 16 are education
software.**

🟢 **Two properties make this channel structurally better, not just luckier.**

- **It cannot drift.** Topic queries, star-sorted queries and language queries all collapse
  into the generalist agent layer — this KB has recorded that collapse 45 times, and ten
  consecutive passes of the mandatory generalist query have yielded zero repositories. A
  platform name cannot collapse: `brightspace` returns 23 repositories and every one is about
  Brightspace.
- **It places the finding by region for free**, because a platform is an institution in a
  country. Skolverket places to Sweden, Smartschool to Belgium, KUPID to Korea, NTU COOL to
  Taiwan, SLIIT to Sri Lanka, VGU to Vietnam. No inference step, so no inferred-data error.

**The sharp version of the correction:** the Korean asset `SonAIengine/ku-portal-mcp` (MIT,
13★) already existed when the Korean-language query was run, and that query did not find it.
The platform name **KUPID** did. So the finding is not that non-English search is useless —
it is that **the institution is the unit of placement, and institutions are usually
searchable in English even when their README is not.**

⚠️ **The method caveat that cost this pass a region.** The channel works only with one
platform name per query. `sigaa OR suap OR siga mcp server` — three Brazilian
university-system names — returned **`total_count: 160,659`** and the generalist layer,
because Boolean `OR` lets the highest-volume terms (`mcp`, `server`) dominate. **LATAM's
platform tier therefore remains unmeasured**, and that is recorded as a gap rather than as a
result.

## 42. The national curriculum is becoming a callable API — and the wrapper's licence is not the data's licence

New this pass, and it is a shape rather than a single asset: a **state education authority's
own API estate, wrapped thinly under a permissive licence and published as an agent-callable
server.**

| Authority | Wrapper | Licence (payload read) |
|---|---|---|
| **Skolverket** (Sweden) — Läroplan/syllabus API, Skolenhetsregistret school-unit register, Planned Educations | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP), 12★ | 🟢 **MIT**, 1,093 B |
| **Udir** (Norway) — school (NSR) and kindergarten (NBR) registries | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none**, 0 of 20 filenames |

🔵 **Why this matters more than its star counts suggest.** In every regime this KB tracks,
*"aligned to the national curriculum"* is a procurement requirement, and it has been a
**consulting deliverable** — a human reads the syllabus and writes a mapping that is stale on
the day it ships. Where the authority publishes an API and a permissive wrapper exists, the
alignment becomes **a tool call inside the product**, re-evaluated on every run. It is the
input trend 13 implied and pattern P15 lacked.

⚠️ **And it comes with a licensing distinction this KB has not had to make before.**
Skolverket-MCP's copyright line reads **"Skolverket Syllabus MCP Contributors"**, *not the
agency*. So:

- the **MIT grant covers the wrapper** — safe to fork, modify, ship, rebrand;
- the **agency's own terms govern the data** the wrapper returns, and the MIT licence says
  nothing whatsoever about them;
- a proposal that cites "MIT" for a national-curriculum capability is **citing the connector
  and implying the corpus**. Trend 22 priced the corpus; this is the same error arriving
  through a cleaner-looking door.

🟢 **The generalisable move, and nothing about it is Nordic.** Check whether the target
country's education authority publishes an open API; check whether a permissive wrapper
exists; expect to write one. Writing a thin wrapper over a public national API is small,
well-bounded and highly reusable — and **Udir is the proof that the gap is normal**: same
region, same quality of public data, no grant at all.

## Declared gaps — fourteenth pass, 2026-10-06

**Measured and genuinely missing, after first-hand probing this pass.**

1. 🔴 **LATAM's platform-integration tier is unmeasured, by this pass's own error.** SIGAA
   and SUAP were OR'd into one query, which collapsed into the generalist layer
   (`total_count: 160,659`). The only LATAM asset found, `vnschneider/suap-mcp`, has **no
   licence payload** and declares **AGPL-3.0-or-later** in `pyproject.toml` — no grant today,
   and a copyleft constraint if one ever lands. **Next pass: SIGAA and SUAP, one name per
   query.**
2. 🔴 **Zero of the MCP Registry's 102 education servers are LATAM-placed.** Fourth
   independent instrument to return absence rather than thinness for the region. Consistent
   with trend 37.
3. 🔴 **PowerSchool integration tier: `total_count: 0`.** No open-source asset of any licence
   for the dominant US K-12 student information system. This is a build, and the gap is
   structural (credentials), not temporal.
4. ⚠️ **The registry census is incomplete and is reported as a floor.** The page loop ended
   on an empty body at page 313 (31,300 records → 11,505 unique servers). The true index size
   is unknown; resume from the cursor before quoting any denominator from it.
5. ⚠️ **Seven assets are declared-and-ungranted, one of them at 103★.**
   `DMontgomery40/mcp-canvas-lms` — second-highest-starred Canvas MCP server on GitHub —
   ships a `package.json` MIT field and no licence file. Six others the same (five MIT, one
   ISC); one declares AGPL-3.0. **One commit each would unblock them**, and asking is cheaper
   than rebuilding.
6. ⚠️ **No permissive asset found this pass addresses accommodations as a first-class
   surface.** `GarphenGate/moltline-mcp` (MIT) is the only one that even names it among its
   eight skills. Accommodations are a legal requirement in both US and EU school systems, and
   the tier is effectively empty.
7. 🔵 **Negative method result, recorded so the next twelve passes do not re-buy it:** the
   licence-filename **case-variant ladder** (19 extra requests per repository) paid out
   **zero times across 98 repositories** — all 76 payloads sat at plain `LICENSE`. Keep it
   for a single high-value asset whose absence would change a recommendation; do not pay it
   across a census.

## 33. The licence has stopped being the last gate — the access grant is

Every licensing trend in this file (23, 24, 25, 29) answers one question: **may we copy and
redistribute this code?** This pass found the first component in this KB's history where the
answer is an unqualified **yes** and the component still cannot be shipped.

[`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) is MIT,
payload read, 20 tools over the Infinite Campus student information system. Its own README
quotes the vendor's Terms of Use:

> Users may not access, use, or search the Services by any means other than our publicly
> supported interfaces (for example, scraping or using the content to train artificial
> intelligence software).

…then states that the server calls non-public mobile endpoints and that **"IC may treat this
as a ToS violation"**, restricts itself to personal parent/student use, forbids bulk
extraction and model training, and invokes **FERPA and COPPA** on its output.

**Two grants are needed to ship an integration, and only one of them is in the repository:**

| Grant | Who gives it | Where it lives | What a licence audit sees |
|---|---|---|---|
| **Copyright** — may we copy the code? | the maintainer | `LICENSE` | 🟢 everything |
| **Access** — may we call the system? | the **platform vendor** | the vendor's ToU, and the institution's contract | 🔴 **nothing** |

🔴 **This is why the trend matters beyond one repository.** The whole SIS integration tier —
24 permissive assets across seven countries, found this pass — is built on unofficial access
and says so in its own words: *"web scraping"* (`GeovaneSchmitz/sigaa-api`), *"unofficial…
at your own risk"* (`kc0506/ntucool`), repository topic `reverse-engineering`
(`elisaado/somtoday-api-docs`). The licences are clean. The access is not granted by anyone.

⚠️ **The clause to watch is the AI-specific one.** Infinite Campus's ToU does not merely
forbid scraping; it names **"using the content to train artificial intelligence
software"** as a prohibited means of access. This KB has **one** verified instance of that
clause, so it is recorded as a data point and **not** yet asserted as an industry-wide
pattern — but it is the clause that would, if it spreads, make the distinction between
"integrate with" and "train on" a contractual line rather than an ethical one. **Next pass
should read the ToU of PowerSchool, Canvas/Instructure, Moodle-hosting and Google Classroom
and establish whether this is one vendor or the sector.**

🟢 **What to do about it, commercially.** The constraint is not a dead end, it is a scoping
rule: a client engagement that touches a proprietary SIS must budget for the **vendor's
official API entitlement** before any agent work is scoped. Both US K-12 vendors publish
OneRoster endpoints, and this KB's interoperability tier already carries permissive
OneRoster and Ed-Fi implementations. **Prototype on the community client, ship on the
official API.** Operationalised as **P25** and gated by **P26**.

## 34. Permissive supply collects at the edges of platforms it is not allowed to fork

This pass measured both halves of the student information system space and the result is a
structural law, not a coincidence:

| Layer | Assets found | Licence set |
|---|---|---|
| **SIS platforms** (deployable products) | 5, with 1,600+ ★ and 1,000+ forks between them | 🔴 **{GPL-2.0, GPL-3.0}** + one ungranted. **Zero MIT. Zero Apache. Zero BSD.** |
| **SIS clients, wrappers, MCP servers, extensions** | 36 addresses, 24 permissive | 🟢 **22 MIT · 1 Apache-2.0 · 1 BSD-2 · 1 WTFPL** |

🔵 **You cannot fork an open SIS permissively, so all the permissive work happens around it.**
The MIT supply is clients, timetable decoders, MCP servers and browser extensions —
everything that *talks to* a student information system without *being* one. The same shape
holds for learning platforms, where Moodle (GPL-3.0) and Open edX (AGPL-3.0) are surrounded
by an MIT MCP cluster this KB has censused at 98 addresses.

**Three consequences for how an engagement is shaped:**

1. 🟢 **The permissive shelf is reliably an *integration* shelf.** When this KB reports a
   deep permissive tier, expect side-cars and clients, not a product you can brand and
   resell. The exceptions are rare enough to be named individually (Mentingo, OpenMAIC,
   Coursemology, Sunbird).
2. ⚠️ **"Is there an open-source X?" and "is there a permissive open-source X?" have
   different answers at the platform layer in every category this KB has measured.** Ask the
   second question.
3. 🔵 **The copyleft platform is often still the right answer** — it is simply a different
   engagement: deploy-and-extend under GPL obligations, or take the LGPL-3.0 middle path
   (OpenEduCat on Odoo) where a module can stay proprietary. What it is not is a white-label
   product.

## Declared gaps — fifteenth pass, 2026-10-06

Searched this pass; stated so they can be falsified rather than left as silence.

1. 🔴 **No permissive SIS *platform* exists.** Five measured, all GPL-2.0/GPL-3.0 or
   ungranted. If a client needs a brandable, resellable student information system, **there
   is nothing to start from** and this KB has now looked properly.
2. 🔴 **The UK has no permissive MIS integration layer.** `bromcom` 36 repositories (nothing
   above 2★), `"arbor mis"` 7 (nothing above 0★), `"capita sims" school` **0**. Against the
   strongest government MIT estate in this KB. **A clean build opportunity, stated as a gap
   rather than as an absence of evidence.**
3. ⚠️ **Restated mid-pass, because this pass falsified its own first version.** The gap
   was first written as *"no Japan-, Korea-, Australia- or India-placed SIS integration asset
   was found"*. The **Australia half was wrong**: the MCP Registry channel, run later in the
   same pass, returned
   [`EquateItAu/classquill-mcp`](https://github.com/EquateItAu/classquill-mcp) — **MIT,
   payload-verified, Australian** (ClassQuill tutoring-business data, read-only by design).
   🔵 **The first version was true of the platform-name channel and false of the world**,
   which is precisely the error this pass corrected in the fourteenth pass's work — reproduced
   here within hours, and caught only because a second channel was run.
   **Corrected gap: no Japan-, Korea- or India-placed asset was found.** India's `diksha` is
   a name collision returning 2,864 irrelevant repositories and `samarth ugc` returned 0;
   `sentral compass school australia api` was OR'd and is not evidence of anything.
   🟢 **The standing rule this produces: never write a gap from one channel.** Name the
   channel in the gap, or run a second one before publishing it.
4. ⚠️ **The ministry tier is still unmeasured.** Skolverket (SE) is shelved from the
   fourteenth pass, but Udir (NO), Eduscol (FR), INEP/Censo Escolar (BR), MEXT (JP) and the
   Gulf ministries were not queried by name. **This is the fourteenth pass's instruction 2
   only half-executed — the SIS half is done, the ministry half is not.**
5. ⚠️ **Whether the anti-AI-training ToU clause is one vendor or the sector is unknown.**
   One verified instance (Infinite Campus). Trend 33 names the four ToUs to read next.
6. ⚠️ **The MCP Registry's true index size remains unestablished**, but for a better-understood
   reason than before: the empty page that stopped the fourteenth pass at 31,300 records is a
   **transient fault, not an end-of-index marker** — re-requesting the same cursor returned
   100 servers on 3 of 3 attempts. Any denominator quoted from a walk without retries is a
   floor, not a size. See `repos/trending.md`, fifteenth pass.
7. 🔵 **Negative method result, priced so it is not re-bought:** `curl -sI` against
   `github.com` returns **HTTP 403 for every repository** through this environment's egress
   proxy — 36 of 36, including repositories whose payloads were then read successfully. A
   uniform response across all inputs carries no information. **Use `git ls-remote --symref`
   for existence and `raw.githubusercontent.com` for payloads.**
8. 🟢 **Positive method result worth adopting ahead of the filename ladder:** read the
   **README's own licence link**. `OS4ED/openSIS-Classic` keeps its GPL-2.0 text at
   `docs/License.txt` — mixed case, in a subdirectory, with a byte-order mark — which no
   filename ladder in this KB would have found. The README said where it was, in one request.

## Addendum to the fifteenth pass — the registry channel, and what it does to two claims

🟢 **The MCP Registry is low-density and high-precision, and it fails differently from the
platform-name channel.** ~160 education-matching servers in a 17,000+-name index (under 1%),
most of them false positives on words like *exam*, *canvas* and *education* used outside
education — and then **13 of 16 hand-filtered addresses carried a licence payload, 12 of them
MIT**. Rows in `agents/top.md`.

🔵 **It reached three regions the platform channel missed in the same pass**: Australia
(`EquateItAu/classquill-mcp`, MIT), Norway (`MartinSA04/ntnu-mcp`, MIT) and EU-regulated
tutoring (`Cogniledger/cogniledger-mcp-makuri`, MIT — *"EU-compliant AI tutoring platform for
immigrant children"*, the most regulated user group in this KB). **Run both channels. The
platform channel finds institutions; the registry finds products.**

⚠️ **And it qualifies the fourteenth pass's "the hole is K-12 administration".**
[`Eason0in/classdojo-mcp`](https://github.com/Eason0in/classdojo-mcp) (MIT) imports and
verifies ClassDojo rosters, and ClassDojo's K-12 install base is very large. It is unofficial
and roster-scoped, so the *administration* claim survives in substance — **but the tier was
not empty when it was called empty**, and that is now the second claim of that pass this one
has had to qualify.

🟢 **Two addresses the fourteenth pass left as "not read" are now read**, and both are
ungranted: `3121n/nor-data-udir-mcp` (Udir, Norway) and `DistrictAPI/districtapi-mcp` (US
school districts by address). A fourth registry entry, `lockinplanner/lock-in`, **does not
resolve at all** — the registry indexes addresses it does not verify.

---

## 34. National open-data licences are the permissive tier for curriculum — and they grant commercial use

The permissive allow-list in this KB has been a **software** list: MIT, Apache-2.0, BSD, plus
ECL-2.0 and ISC added in the twelfth pass. The sixteenth pass found the tier below it, and the
licence that governs it is not a software licence at all.

[`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL)
publishes Norway's national curriculum (**LK20**) as **queryable RDF over a SPARQL endpoint, in
production since 7 December 2020**, under **NLOD** — *Norsk lisens for offentlige data* /
Norwegian Licence for Open Government Data. The payload states the grant in English:

> *"You are allowed to copy and make available, change and/or merge data sets described here
> with other data sets, and **to use them for commercial purposes**."*

Conditions: attribution in a prescribed string, **no use of the ministry's logo** without
separate agreement, no misleading or distorted presentation, and no liability for data errors.
**No share-alike. No non-commercial clause.**

🔵 **Why this is a trend and not a single row.** Every pattern in this KB that aligns content to
a curriculum (`P9`, `P15`, `P16`, `P19`) has had to *assume* a lawful, authoritative,
machine-readable source of curriculum truth. In Norway that assumption is now a citation. The
same shape — a national open-data licence over a government education dataset — exists wherever
a state publishes under NLOD, the UK OGL, France's Licence Ouverte, or a CC-BY equivalent.

⚠️ **And the trend has a hard edge: the licence covers the *data*, not the code.** `Grep_SPARQL`
is documentation of an endpoint; there is no platform to vendor. Teams must read "NLOD" as *you
may build and bill on this data*, never as *here is a system*.

🔴 **The counter-measurement, which is why this is a trend with a narrow footprint.** Of five
education ministries queried by name this pass, **one** has a code estate at all. France
publishes teachers' personal class material and no ministry repositories; Japan publishes
documents plus a CC0 kanji table; the Gulf query returned 7,228 results and **zero** ministry
repositories. **The permissive curriculum tier is real, verifiable and commercially
unencumbered — in a minority of countries.**

## 35. The grant has left the licence file — and three ecosystems moved it somewhere different

Trend 23 recorded that *the licence label and the licence grant have come apart*: GitHub's
label disagreed with the payload, so the rule became **read the payload**. The sixteenth pass
found the next step, and it breaks that rule's assumption that there *is* a payload to read.

**Three repositories in one pass, three different places the grant actually lives:**

| Ecosystem | Repository | `LICENSE` contains | The grant is in | Real licence |
|---|---|---|---|---|
| **R / CRAN** | `SidneyBissoli/educabR` | **61 bytes**: `YEAR:` and `COPYRIGHT HOLDER:` — a template fill-in, no grant text | **`DESCRIPTION`** → `License: MIT + file LICENSE` | 🟢 **MIT** |
| **REUSE / FSFE** | `espoon-voltti/evaka` | a pointer stating *"never the original license texts"* | **`LICENSES/LGPL-2.1-or-later.txt`** + per-file SPDX headers | **LGPL-2.1-or-later** |
| **Odoo** | `JayVora-SerpentCS/OdooEduERP` | **nothing** — NO-PAYLOAD on its real default branch `19.0` | **`school/__manifest__.py`** → `"license": "AGPL-3"` | 🔴 **AGPL-3.0** |

🔴 **The consequence is that NO-PAYLOAD has stopped meaning "unlicensed."** In this KB's
conventions NO-PAYLOAD means *ask upstream*, and an upstream ask is a reason to proceed while
waiting. For an Odoo module that reading is **backwards**: the quiet root conceals
**network copyleft** that reaches any hosted deliverable. `OdooEduERP` is 157★ and was active
last week, so the misread is likely rather than hypothetical.

🔵 **The rule this replaces trend 23's with:** *read the payload* becomes **read the payload,
then read the ecosystem's manifest.** Concretely — `DESCRIPTION` for R, `LICENSES/` plus SPDX
headers for REUSE, `__manifest__.py` for Odoo, and by extension `package.json`, `pyproject.toml`
and `pom.xml`, which this KB already probes in `p289`/`p294`.

⚠️ **REUSE deserves separate attention because of *where* it is spreading.** It is an FSFE
standard adopted by European public-sector and publicly funded projects — **precisely the
population this KB's EMEA sections are built on.** Expect the pointer-file shape again, and
expect a naive probe to return either NO-GRANT or a family guessed from prose. Both are wrong,
and the second is worse because it looks like an answer.

## 36. A control that cannot be executed is documentation — and this is now measured, not argued

This KB has built real controls for licence classification: `lib/license_family.sh` (41/41
regression tests) and `lib/probe_payload.sh`. `lib/README.md` states the rule — **source them,
do not rewrite them** — and records its own violations: pass 77 rewrote the classifier and
re-imported P171; pass 15 rewrote the probe loop and re-imported the GPL-§6 defect. Pass 15
concluded: *"A third recurrence should be treated as evidence that documentation cannot carry
this and only tooling can."*

**The sixteenth pass is the third recurrence, and it re-imported four documented defects in a
single instrument:** CC0 nested unreachably inside a CC-BY gate; a substring match in which
**`IMPLIED` contains `mpl`**, so a plain MIT payload classified as MPL-2.0; a 40-line "title
block" wide enough to include GPL-2.0's preamble, which *mentions* the Lesser GPL; and no size
floor, so a 1,001-byte pointer was accepted as a 27,030-byte licence.

🔵 **But the cause is new, and it is the finding.** The earlier diagnosis was laziness — writing
six `grep` lines is easier than finding the library. That is not what happened here. **The
library was located, read, and deliberately copied; the environment refused to execute it**
("code from external"). An architecture can be copied from prose. **Branch order cannot** — and
all four defects are branch-order or anchoring bugs.

🔴 **So the generalisable claim is about control design, not diligence: a control implemented as
executable code in one language, validated by a test suite in that same language, is only a
control in environments that will run it.** Elsewhere it degrades silently into prose — and
prose is what pass 15 said must not be relied upon.

🟢 **What survives environment loss is a fixture: an input, an expected output, and a stated
reason the case is required.** Four real repositories caught all four defects in four requests,
with no interpreter and no trust. Shipped as
`compose/code/p432-fromscratch-fixture-gate/`.

⚠️ **The coverage lesson is pass 15's, restated and now sharper.** An instrument validated only
on the family you care about scores 100% while broken. The required fixture here is
**`openfun/richie`, a plain MIT repository** — because MIT is the family everyone tests, and the
defect corrupted exactly that family. Worse, this KB *builds an architecture recommendation* on
richie being MIT (*"MIT at the portal tier is the cleanest place to put client-visible AI"*),
so the defect would have **inverted a published recommendation** rather than merely mislabelling
a row.

🔵 **And the fourth fixture's pass condition is refusing to answer.** `evaka` must return
UNCLASSIFIED. An instrument that names `LGPL-2.1` there is wrong *even though that is the right
licence*, because it read prose instead of a grant. **A control must distinguish knowing from
guessing right.**

## 37. Where a state publishes education software, it ships the substrate and leaves the agent to the market

Two ministry estates are now shelved in this KB — the **UK Department for Education** (MIT,
ninth pass) and **Norway's Utdanningsdirektoratet** (sixteenth pass) — and independently they
produced the same shape.

Udir's 18 repositories: a curriculum SPARQL service (**NLOD**), the open portion of the national
**exam administration** system (**Apache-2.0**), a **design system** (**MIT**), a person-data
**rostering** spec (ungranted), test tooling and shared CI (**MIT**/ungranted), and **two
maintained Moodle plugins** (GPL-3.0 — one of them an abandoned plugin the directorate picked
up, on default branch `MOODLE_405_STABLE`).

🔴 **No tutor. No assessment model. No agent of any kind.** Across both estates, in two
countries.

🟢 **Read commercially, that is a better finding than a gap.** The state has already paid for
and permissively licensed the parts no vendor can differentiate on — authoritative curriculum
data, exam administration, accessible components, rostering semantics — and **the layer a studio
sells is the layer the state does not build.**

⚠️ **With a caveat that is itself a pattern.** In both estates **the highest-value assets are the
ungranted ones**: Udir's `KL06-LK20-public` (the curriculum interface) and `pifu` (the
rostering spec) are **NO-PAYLOAD against 30+ filename variants on their real default branches**.
🔵 **A ministry's publishing instinct outruns its licensing process** — which makes the upstream
licence ask (a one-commit change) the single highest-leverage, lowest-cost action available
against a public-sector estate.

---

## Declared gaps — sixteenth pass, 2026-10-06

Searched this pass, not found, stated so the absence is informative rather than silent.

1. 🔴 **No education ministry publishes an AI agent.** Searched: `org:Utdanningsdirektoratet`
   (18 repos, all 18 probed), `eduscol` (107), `mext`/`monbukagakusho` (1,701),
   `inep`/`censo escolar` (3,572), `"ministry of education"` + Gulf (7,228). **Zero
   ministry-published tutoring, grading or assessment agents.** Substrate yes; agents no.
2. 🔴 **France has no ministry code estate.** `eduscol` returns individual teachers' class
   material. The one real asset, `VictorNain26/tomai-curriculum` (**a RAG index over the French
   national curriculum**), is **ungranted**. ⚠️ **Falsifiable by**: an `org:` query against
   `education.gouv.fr`-affiliated organisations, which this pass did not run.
3. 🔴 **No Gulf ministry repository was found, and the count that suggests otherwise is void.**
   7,228 results match README **funding acknowledgements** ("supported by the Ministry of
   Education"), not owners. ⚠️ **This gap is about a channel, not the world** — a lesson this KB
   has now had to learn twice. **Only `org:` can settle it.**
4. 🔴 **The four-vendor anti-AI-training question is still open after two passes.** PowerSchool,
   Instructure/Canvas, Google Classroom and Moodle hosting Terms of Use are **all four
   egress-blocked** in this environment. ⚠️ **It remains unestablished whether the clause the
   fifteenth pass read in Infinite Campus's ToU is one vendor's or the sector's**, and this KB
   must not say "the sector" until four payloads are read.
5. 🔴 **No public-sector xAPI profile is usable yet.** `KS-AVT/avt` — Norwegian municipal-sector
   (**KS**) xAPI statements for *"Aktivitetsdata for vurdering og tilpassing"* — is
   **NO-PAYLOAD** on its default branch `AVT2`. The xAPI/LRS tier (twelfth pass) still has
   **no government reference implementation**. ⚠️ Worth one more probe on other branches before
   being treated as settled.
6. 🔴 **`mcp-brasil` identity is unresolved.** Two live addresses, same name, both MIT,
   **246★ vs 1,805★**, neither reported as a fork of the other. ⚠️ **Nothing should be quoted
   from either in a deliverable until first-commit SHAs are compared** — pin a commit, not a
   name.
7. ⚠️ **Carried over unclosed from the fifteenth pass, and not closeable by an unattended run:**
   the licence ask on [`IFRN/suapi`](https://github.com/IFRN/suapi). It requires opening an
   issue on a third party's repository — an outward-facing write with no mandate here.
   **It needs a human, or an explicit instruction that upstream asks are in scope.**

---

## 38. The licence question has moved from *permission* to *delivery model* — and the EUPL is where education meets it

Through sixteen passes this KB's licence axis has been **permissive vs copyleft vs ungranted**:
may we use it at all? **The seventeenth pass found a tier where that question is settled "yes"
and the answer still constrains the architecture** — and it is not a marginal tier. It is
**188 live repositories, the entire published code estate of a national education agency.**

Every Finnish payload read is **EUPL** (v1.1 or v1.2), ten of ten. The EUPL is OSI-approved, and:

| The EUPL property | Why education hits it harder than other industries |
|---|---|
| **Art. 1 counts *"communication to the public"* as Distribution** — making functionality available over a network | 🔴 Education delivery is **almost always** network delivery: an LMS, a tutor, a portal. The copyleft triggers on the normal shape of the engagement, AGPL-style. |
| **Art. 5 carries a compatibility list** (GPL-2.0/3.0, AGPL-3.0, LGPL, MPL-2.0, EPL, CeCILL, OSL) | 🟡 A genuine relicensing route for combined works — the only copyleft licence with one. ⚠️ And because the compatible licence prevails on conflict, the EC's own discussion notes the SaaS duty **can be circumvented** via GPL-3.0. **Documented, contested, not a sales route.** |
| Valid in 23 EU languages, written for public bodies | 🔵 It is *why* European state estates pick it: it is the licence that survives a procurement lawyer in any member state. **Expect more of it, not less.** |

🔵 **The structural trend, stated for the next pass: as European public bodies publish more
education software, the dominant licence in this industry's supply will be a network-reaching
copyleft, not MIT.** The KB's instinct — *permissive good, copyleft bad* — gives the wrong answer
here. **The right question is no longer "may we use it?" but "may we use it *the way we intend to
ship it*?"** Calling these services is free of obligation; forking them into a hosted product is
not. That is a two-cell answer, and the KB now needs both cells in every platform row.

## 39. The regulation stopped being forthcoming and started being in force — in three regions at once

Every prior pass wrote about education-AI regulation in the future tense. **As of this pass it is
present tense in three regions simultaneously**, and the dates are specific:

| Instrument | Status read this pass | What it binds |
|---|---|---|
| **EU AI Act**, high-risk obligations | ⚠️ **CORRECTED in the nineteenth pass of 2026-10-06. This row read "Apply from August 2026 — in force now" and that is wrong.** Regulation (EU) 2026/1744 (*Digital Omnibus on AI*, CELEX 32026R1744, OJ 24 July 2026, in force 27 July 2026) deferred **Annex III stand-alone high-risk from 2026-08-02 to 2027-12-02**, and Annex I embedded to 2028-08-02. What *is* in force since **2026-08-02** is the AI Act's general application including **Article 50 transparency**, which the Omnibus did **not** defer. See trend 17, which held the correct dates before this row was written. | Education **access and assessment** — admissions, student evaluation, exam scoring, and monitoring for prohibited behaviour during tests (Annex III, point 3) — are high-risk: risk management, data governance, human oversight, transparency, conformity assessment **before** deployment. **The duty is unchanged; only its start date moved.** |
| **Vietnam, Law on Artificial Intelligence** | 🔴 **In force 2026-03-01** | Six high-risk sectors **including education**, naming **automated assessment and behavioural monitoring** |
| **South Korea, AI Basic Act** | 🔴 **In force 2026-01-22** | Comprehensive statute with enforcement teeth |
| **Taiwan, AI Basic Act** | Passed December 2025 | Comprehensive statute |
| **US states** | 🔴 **134 bills, 31 states**, this session | **CA AB 1159** (no student data in training), **Idaho SB 1227**, **OK / MD** human-oversight and no-high-stakes-decisions rules |

Against which: 🔴 **10% of 450+ surveyed institutions have formal AI guidelines**, while **92% of
students use AI.**

🔵 **The trend is a reversal of who carries the risk.** While the rules were forthcoming, the
buyer's question was *"what can AI do for us?"* Now that assessment is a high-risk classification
in force, the buyer's question is *"can you prove this deployment is conformant?"* — and that is a
question a studio answers with artefacts (data-flow attestations, human-oversight design, a
per-jurisdiction obligation matrix), not with a model. ⚠️ **Note the divergence trap in APAC:**
the same assessment feature is high-risk in Vietnam, statutory in Korea and voluntary-guidance in
Singapore and Japan, so **a regional posture is not a compliance position** — the matrix has to be
per country, and it belongs in the product's configuration rather than in a slide.

## 40. A number that is plausible in two columns will eventually be read from the wrong one

This pass withdrew a figure this KB had carried for seven weeks: `dasgltd/mcp-brasil` at
**"246★"**. The repository has **0★**. **246 is its commit count** — and this KB carries exactly
that number, correctly labelled, in a **commits / tags** column of `repos/trending.md`.

🔵 **The failure was not carelessness about stars; it was a column with no type.** Both numbers
sit on the same rendered page, both are small integers, and **246 is a completely reasonable star
count** — so nothing downstream could flag it. The two numeric gates this KB already ships
(`p349-star-resolution-band`, `p351-star-digit-sweep`) check the *shape* of a star figure, and
246 is shaped correctly.

🟢 **The control that would have caught it is one comparison: a star count equal to that repo's
own commit count is a flag.** It is cheap, it is first-hand under the clone instrument, and it
generalises — **the defect class is "two plausible numbers on one page", and licence bytes vs
file counts is the next instance waiting to happen.**

## Declared gaps — seventeenth pass, 2026-10-06

Searched this pass, not found, stated so the absence is informative rather than silent.

1. 🟢 **CLOSED from the sixteenth pass: `mcp-brasil` identity.** Item 6 of the sixteenth-pass
   gaps is resolved and its figures are withdrawn. All three addresses share root commit
   `8b786bf` (2026-03-22); **`Mcp-Brasil/mcp-brasil` is upstream** (1.8k★, no fork banner),
   `dasgltd/mcp-brasil` is a **0★ fork** of it in exact sync, `marcellodesales/mcp-brasil` a fork
   8 commits behind. **There was never a 7.3× star gap between two projects.**
2. 🔴 **Four national education ministries remain unmeasured — and the names were the wrong
   instrument.** `Mineduc` (Chile, Colombia) and `onderwijsinspectie` (Netherlands) are **org
   names claimed with zero public repositories**; `SEP` (Mexico) resolves to **an unrelated
   software consultancy**; `stil` and `DUO` are **404**. ⚠️ **None of these is evidence that the
   body publishes nothing.** Falsifiable by: the bodies' own language and national code-hosting
   habits (`gob.mx`, `datos.gob.cl`, `developer.overheid.nl`) — the channel that found
   `Utdanningsdirektoratet` and `Opetushallitus`.
3. 🔴 **No APAC ministry education estate has been found by any pass.** The region now has three
   binding AI statutes and this KB has **one** APAC-origin permissive education asset
   (`panaversity/learn-agentic-ai`, MIT, Pakistan). ⚠️ **Unmeasured, not empty** — no `org:` query
   has yet been run against an APAC education authority.
4. 🔴 **179 of Opetushallitus's 188 repositories are unread.** Nine were probed, chosen by stars
   and domain relevance. The estate's full licence picture is **sampled, not established**.
5. 🔴 **`Skolverket/dnp-usermanagement` (7★) and `dnp-provplattform` are NO-PAYLOAD.** Sweden's
   national digital-assessment platform and user-management API specifications are **ungranted**,
   which is the second consecutive pass where the most interesting *document* in a state estate
   is the one with no licence.
6. 🔴 **This KB's own licence classifier cannot read the EUPL** (`grep -c -i eupl` → **0**), and
   **this pass could not execute it to confirm the consequence** — the behaviour is traced by
   reading the code. ⚠️ **Second consecutive pass unable to run `compose/code/lib/*.sh`.** A
   control that cannot be executed is documentation (§36), and that is now true two passes
   running.
7. 🔴 **A new payload class has no instrument: `GRANT-BY-REFERENCE` with a dead pointer.** The six
   EUPL-1.1 notices name their terms at `http://www.osor.eu/eupl/`, which returns **403**. The
   repository contains neither the terms nor a working address for them. ⚠️ **Not equivalent to
   NO-PAYLOAD** — the grant is real and the named licence is public — but it means **the terms
   must be pinned from the EC's dated text**, because the repo pins nothing.
8. ⚠️ **Carried over unclosed, and still not closeable by an unattended run:** the four-vendor
   anti-AI-training ToU question (sixteenth-pass gap 4, egress-blocked) and the licence ask on
   [`IFRN/suapi`](https://github.com/IFRN/suapi) (an outward-facing write on a third party's
   repository, with no mandate here). **Both need a human or an explicit instruction.**


## 43. The grant and the *offer* have come apart — a copyleft payload can carry an advertised willingness to relicense

§23 established that the licence **label** and the licence **grant** had come apart, and that
reading the payload is no longer enough. The eighteenth pass found the next layer down, and it runs
the other way: a payload that reads **GPL-3.0** can sit under a README that **offers to change it**.

[`Citolab/qti-components`](https://github.com/Citolab/qti-components) — 19★, 10 forks,
**2,456 commits**, the most mature QTI item renderer measured — ships `main/LICENSE.md` as
unambiguous **GPL-3.0**, and states in its README:

> *"This project is licensed under the GPLv3 License. Please note that the licensing is GPLv3 —
> if you want to use it in another way, feel free to ask!"*

Citolab is the software lab attached to **Cito**, the Netherlands' national assessment institute,
so the holder is **identifiable, institutional and reachable** — which is what makes the offer worth
anything.

**Three consequences, and the third is the one that changes behaviour:**

1. **A payload-reading classifier cannot see this.** `license_family.sh` reads the payload and will
   return GPL-3.0, correctly. The offer lives in prose, in a different file, and **no licence
   instrument this KB owns will ever surface it**. It is found by reading the README — the step
   that automation was supposed to remove.
2. **"Copyleft" stops being a routing decision and becomes an opening position.** This KB's
   standing rule is that copyleft decides whether the AI work is a plugin (and inherits) or a
   side-car (and does not). That rule holds *by default*. Where the holder advertises
   negotiability, there is a **third branch**: ask.
3. 🔴 **The cost of not asking is paid silently.** A team that routes around a GPL-3.0 renderer and
   rebuilds it has spent the budget **before discovering the licence was negotiable** — and nothing
   in the pipeline flags it, because the payload was read correctly and the verdict was right.

🟢 **The operational rule: when a copyleft component is on the critical path and its holder is an
identifiable institution, read the README for a relicensing offer before designing around the
licence.** It is one read, and the alternative is a rebuild.

⚠️ **And the warning that travels with it.** An offer in a README is **not a grant**. It is an
invitation to a negotiation whose outcome is unknown, cannot be assumed in a bid, and must be
settled in writing with the named holder before any architecture depends on it. Record it as
**"GPL-3.0, holder has advertised willingness to relicense"** — never as a permissive row.

## 44. Who publishes the state's education code is a regional property — and it decides who you contract with

Four passes have now probed state education estates across three regions. The pattern is not *how
much* each region publishes. It is **which body does the publishing**, and the answer differs by
region in a way that changes the counterparty, the artefact and the engagement shape.

| Region | Who publishes | Measured evidence |
|---|---|---|
| **EMEA** | 🟢 **The agency itself** | Norway's **Utdanningsdirektoratet** and Finland's **Opetushallitus** (188 repos, EUPL) — passes 16–17. The Netherlands' **Stichting Kennisnet**, 29 repos, 6 MIT libraries payload-verified — this pass |
| **APAC** | 🟡 **An arm's-length foundation or vendor, never the ministry** | India: the **EkStep Foundation** publishes `Sunbird-Ed` (MIT, 38,046 commits, the DIKSHA national platform) while **SamagraX** carries 124 repos with its most-starred and its education repo both **ungranted**. Singapore: `opengovsg`, **98 repos, zero education products**; the assessment work reaches the market through **Coursemology / Codaveri** (MIT). Indonesia: `kemdikbud` exists with **1 empty repository** |
| **LATAM** | 🔴 **The state publishes *data*; a private third party publishes the *code*** | **Mineduc Chile's Centro de Estudios**: **21 datasets** via `datos.gob.cl`, **no code estate**. **SEP Mexico**: no education repositories under `mxabierto` (61 repos). The only clients that reach the data are **third-party MIT** — `pipeworx-io/mcp-datos-cl` (© 2026 Mojibake Inc.) and `gerardbourguett/mcp-chilegob-dataset` (© 2025, an individual) |
| **North America** | 🟡 **A non-profit standards alliance, with state agencies as adopters** | ⚠️ **Partial read, flagged as one in the twentieth pass.** This KB's measured evidence is the **Ed-Fi Alliance** estate (**Apache-2.0**, the US K-12 data standard — see `repos/foundations.md`) plus vendor-side integration repos; state education agencies in this KB's sample **adopt and certify against** that standard rather than publishing code of their own. 🔴 **No dedicated North American state-estate sweep has been run**, so this row is weaker evidence than the other three and must not be cited as if it were equal to them |

**Why this is a trend and not a table of four anecdotes:** the instrument that works in one region
returns nothing in another, and *returning nothing is not the same as there being nothing*. Pass 17
ran `org:` against ministry names and recorded four dead ends with the correct caveat that they were
**unmeasured, not empty**. They were unmeasured because `org:`-against-a-ministry is an **EMEA-shaped
instrument**. In APAC the ministry is not the publisher. In LATAM the artefact is not a repository.

**Three delivery consequences:**

1. **EMEA — the estate is the integration target, and the licence is the whole question.** You will
   meet real code with a real grant (EUPL, MIT, GPL-3.0), and §38's delivery-model analysis applies
   directly.
2. **APAC — find the foundation, not the ministry, and expect the grant to be missing.** The two
   largest APAC estates measured have their **most valuable repositories ungranted**. The
   first question is not "what licence?" but **"is there a licence at all?"**
3. 🔴 **LATAM — the counterparty question inverts.** There is nothing to fork from the state, so
   *"what may we fork?"* is the wrong question. The right ones are **"what are the open-data
   portal's terms of use?"** and **"who owns the only existing client, and is it maintained?"** A
   single individual's MIT repository standing between a client and a national dataset is a
   **supply-chain risk**, not a solution — and building a maintained, permissive replacement is a
   **small, well-defined, fundable piece of work** this KB can point a LATAM engagement at.

🔵 **This confirms §42 in a second region** — *"the national curriculum is becoming a callable API,
and the wrapper's licence is not the data's licence"* — and sharpens it: in **both** regions where
it has now been observed, **the wrapper's holder is a private party and the data's holder is the
state.**

## Declared gaps — eighteenth pass, 2026-10-06

Searched or probed this pass, not resolved, stated so the absence is informative rather than silent.

1. 🟢 **CLOSED from the seventeenth pass (gap 3, partially): the APAC ministry tier is now
   MEASURED.** Three orgs probed — `kemdikbud` (**1 empty repo**), `opengovsg` (**98 repos, zero
   education**), `Samagra-Development` (**124 repos, top assets ungranted**). ⚠️ **Measured, not
   closed:** three orgs is not a region, and **no Japanese or Korean body has been probed at all**.
   The next instrument is the **foundation tier**, not the ministry tier — see §44.
2. 🟢 **CLOSED from the seventeenth pass (gap 2, for two of four): Chile and Mexico.** `Mineduc` and
   `SEP` are not thin publishers. **They publish a different artefact class** — Mineduc ships **21
   datasets** through `datos.gob.cl`; SEP has no repositories under `mxabierto`. 🔴 **Still open:
   `onderwijsinspectie` resolved to the wrong body** (the inspectorate, not the publisher —
   **Kennisnet** is), and **`stil` and `DUO` were not re-probed this pass.**
3. 🔴 **Instruction 1 (the EUPL grant-notice anchor) is NOT shipped, for the third consecutive
   pass, and the cause is now diagnosed rather than reported.** `bash` 5.2.21, `python3`, `git` and
   `curl` are all present and the library is readable; what the environment refuses is **executing
   code that arrives inside the repository** (policy reason `[Code from External]`). It is a sandbox
   property, not a missing tool, and it will not vary between passes. ⚠️ **The anchor was
   deliberately not written**, because pass 17's instruction *is* the validation — fixture gate, ten
   payloads, negative control — and an unvalidated classifier change in the one file every licence
   row depends on is **§36's failure committed in the worst possible place**. An unvalidated control
   is worse than a declared gap, because it looks like a control.
4. 🔴 **Instruction 2 (the commit-count / star-count equality flag) is likewise unshipped**, same
   cause. ⚠️ Note that this pass **would have been caught by it in reverse**: `Kennisnet/qti-components`
   has **2,377 commits and 1 star**, and the two columns were never at risk of being confused
   because the fork-lineage clone reported both in the same breath. **The manual instrument covered
   the gap the automated one would have.**
5. 🔴 **20 of Kennisnet's 29 repositories are unread.** Nine were probed, chosen by stars and domain
   relevance; **two of those nine are NO-PAYLOAD**. The estate's ungranted rate is **sampled, not
   established** — the identical shortfall declared for Opetushallitus's 188, now in a second
   estate. ⚠️ A 2-of-9 ungranted rate must not be reported as 22% of the estate.
6. 🔴 **The 1EdTech certification claim was read from the vendor's own README, not from the
   issuer's register.** `amp-up-io/qti3-item-player` states QTI 3 Basic and Advanced "Delivery"
   certification, and this KB has recorded it as the first externally certified permissive asset.
   ⚠️ **By §23's own rule that is a claim to check against its issuer**, and 1EdTech's certified-products
   register was not read this pass. **Scope and date of the certificate are unestablished.**
7. 🔴 **Structural defect, newly measured and NOT silently repaired: the numbering has collided.**
   `compose/patterns.md` reuses **P1, P25, P26, P27, P28, P29 and P30** across two and three
   distinct patterns each; `intel/trends.md` reuses **33–40**, with `## 34.` used **three** times.
   Cross-references of the form "see P25" are therefore **ambiguous by construction**. Declared
   rather than renumbered, per this KB's standing policy of declaring over silently renumbering —
   but ⚠️ **this one has a cost the policy did not anticipate**, because unlike a trend whose
   *content* needs splitting, these are **identical labels on unrelated content**, and every future
   cross-reference inherits the ambiguity. **It needs a deliberate renumbering pass with a
   redirect table, not another declaration.**
8. 🔴 **`intel/market.md` still carries TWO `## Opportunities by region` blocks** where the brief
   specifies one. 🟢 The `###` damage `p383-region-heading-gate` measured at pass 117 is **fully
   repaired** — both blocks now contain **exactly four `###` headings, all in the closed vocabulary,
   zero out-of-vocabulary siblings** (it was 24). The remaining defect is the **block count: 2, not
   1.** This pass added its regional opportunities **inside the existing final block** rather than
   opening a third.
9. 🔴 **`datos.gob.cl` was never reached first-hand — the LATAM figures in this pass are Tier 2.**
   The portal is **EGRESS_BLOCKED** from this environment, so the **21 datasets** count and the dataset
   inventory behind §44 and P35 come from search results. 🟢 The claim that **the state publishes data
   and a third party publishes the code** does **not** rest on that number — it rests on the first-hand
   finding that `mxabierto` has **no education repositories** and that both Chilean clients are
   **third-party MIT**, all payload- and `ls-remote`-verified. ⚠️ But the **21** itself is unconfirmed.
10. ⚠️ **Carried over unclosed for a third consecutive pass, and still not closeable by an unattended
   run:** the four-vendor anti-AI-training ToU reads (egress-blocked) and the licence ask on
   [`IFRN/suapi`](https://github.com/IFRN/suapi) (an outward-facing write on a third party's
   repository, with no mandate here). **Both need a human or an explicit instruction.**

## 45. The deadline moved and the duty did not — and in 2026 that happened in three regions at once

**Added in the nineteenth pass of 2026-10-06. This is the counterpart to trend 39, whose headline
row this pass had to correct.**

Trend 39 recorded that education-AI regulation had stopped being forthcoming and started being in
force. 🔵 **The 2026 update is narrower and more useful: the dates slipped, the obligations did
not.** Three of four regions had a 2026 compliance cliff in education; three of those cliffs moved
during 2026, and no technical standard behind any of them changed.

| Region | Instrument | 2026 movement | Standard |
|---|---|---|---|
| **North America** | DOJ rule under **ADA Title II** (2024-04-24) | 🔴 **Interim Final Rule 2026-04-20**: **2026-04-24 → 2027-04-26** (entities ≥50,000) and **2028-04-26** (<50,000, special districts). DOJ had *"overestimated the capabilities (whether staffing or technology) of covered entities"* | **WCAG 2.1 AA — unchanged** |
| **EMEA** | **EU AI Act**, Annex III §3 (education) | 🔴 **2026-08-02 → 2027-12-02** (Reg. (EU) 2026/1744, CELEX 32026R1744, in force 2026-07-27). Annex I embedded → 2028-08-02 | Conformity duties unchanged |
| **EMEA** | **European Accessibility Act**, in force 2025-06-28 | ⚠️ **No movement, and no safe harbour either**: as of 2026-07-20 **no EN 301 549 version had been cited in the Official Journal under the EAA**; v4.1.0 (Nov 2025) still in Public Enquiry and Vote to Aug 2026 | **EN 301 549** — cited nowhere, so **no presumption of conformity** |
| **APAC** | Standing mandates | 🟢 **Nothing moved because nothing was pending** — India RPwD 2016 + **GIGW 3.0**; Japan **JIS X 8341-3:2016**, mandatory for government; Australia **AHRC April 2025** affirming WCAG 2.2 AA under the 1992 DDA + DTA Digital Experience Policy | **Three countries, three WCAG versions** |
| **LATAM** | 🔴 **No accessibility deadline in any market** | Demand is programme-driven: UNICEF **Accessible Digital Textbooks** | Universal Design for Learning |

### 🔵 Why this is a trend and not a news item

**Because it changes what the buyer is buying.** While a deadline is approaching, the product is a
*sprint*: scope it, hit the date, leave. Once the regulator has moved the date — and in North
America stated in writing that it did so because covered entities **could not staff the work** —
the sprint pitch collapses and what remains is **capacity**: an estate inventory, a per-criterion
manual queue sized in hours, a CI gate the client owns, and a regression baseline. 🟢 **The backlog
is identical; only the urgency narrative is gone.** And the extension is the strongest available
evidence that the buyer cannot do it alone, so the capacity sale is *better* evidenced than the
sprint ever was.

⚠️ **The failure mode to avoid is now the obvious one:** a proposal whose urgency rests on a date
the regulator has already moved once tells the buyer the author has not read the rule since 2024.

### 🔴 The second-order trend: an extension does not relieve a duty, and two regions prove it differently

- **North America:** the obligation to provide equal digital access *remains fully in force* under
  the ADA. Only the technical-standard compliance date moved. A district sued today is not defended
  by the 2027 date.
- **EMEA:** the EAA has bound suppliers since **2025-06-28** with **no harmonised standard cited**,
  which is the mirror image — the duty is live and the *safe harbour* is the thing that is missing.
  🟢 **So conformance has to be evidenced rather than asserted:** per criterion, with engine and
  version named, and with **undetermined** as a legitimate third verdict (WCAG-EM's own vocabulary).

🔵 **Both regions therefore reward the same artefact — a per-criterion evidence ledger — and they
reward it for opposite reasons.** That convergence is why **P36** is written once and ported, rather
than built twice.

### 🟢 The supply fact that makes the trend actionable

The toolchain for this work is permissive and nineteen passes of this KB never recorded it:
`IBMa/equal-access` (**Apache-2.0**, 780★), `GoogleChrome/lighthouse` (**Apache-2.0**, 30.9k★),
`microsoft/accessibility-insights-web` (**MIT**, 955★), `tesseract-ocr/tesseract` (**Apache-2.0**,
76.8k★), with `dequelabs/axe-core` and `ocrmypdf/OCRmyPDF` (**MPL-2.0**) usable unmodified, and an
agent tier at `Community-Access/accessibility-agents` (**MIT**, 421★, 39 MCP tools over PDF/ePub
and Office), `ronantakizawa/a11ymcp` (**MIT**) and `tomaszboloz/WCAG-Accessibility-Skills` (**MIT**,
10★ — the per-criterion ledger).

⚠️ **With one hard limit that decides the commercial shape: no permissive engine produces tagged
PDF/UA.** veraPDF validates (dual GPL/MPL, licence files named `LICENSE.GPL` / `LICENSE.MPL`, outside every shortlist filename); OCRmyPDF
makes PDFs *searchable*, which is a different thing. **Courseware is PDFs, both Title II and the
EAA cover documents, so the document estate is the largest line item and the least automatable.**
🔵 **That is the trend's sharpest commercial consequence: the regulation is automatable on the web
tier and human on the document tier, and a single blended rate for both is a mispriced contract.**

### 🔵 And the inversion worth remembering

In every other tier this KB has measured, permissive supply sits at the edges of platforms nobody
may fork. **Here it is the measuring layer that is permissive and the end-user application layer
that is copyleft** — Cboard **GPL-3.0**, AsTeRICS Grid **AGPL-3.0**, NVDA **GPL-2.0+**, pa11y
**LGPL-3.0**. 🟢 **Since the billable work is remediating the client's estate rather than shipping
an assistive application, the half a studio needs is the permissive half.** ⚠️ **And the proposal
rule that follows: never offer to fork the assistive application — integrate at the file-format
boundary and test against it.**

---

## 46. The date that governs a client's system is in the transition article, not the headline — and modernising the system is what forfeits it

**Twentieth pass of 2026-10-06.** ⚠️ **Cite this trend by its title.** This file contains
**eight duplicated trend numbers** — see the trend below — so "trend 46" is unambiguous today
only because 46 was free when it was written.

🔴 **Every pass of this KB until now recorded when a rule *starts*. None recorded when it
*binds a system that already exists*.** Verified by grep before this was written: `Article 111`,
`grandfather`, `legacy system`, `transition period`, `placed on the market before` and
`31 December 2030` returned **zero occurrences** across all eight files. That is the expensive
kind of gap, because a client's estate is made almost entirely of systems that already exist.

| Region | Market / instrument | Headline date | What the transitional article says | Governs an existing system from |
|---|---|---|---|---|
| **EMEA** | EU AI Act, **Art. 111** | Annex III §3 applies **2027-12-02** | A high-risk system lawfully placed on the market before the high-risk rules apply continues **without retrofit or additional certification, provided its design remains unchanged**; providers and deployers of high-risk AI **intended to be used by public authorities** must comply **by 2 August 2030**; AI inside **Annex X** large-scale IT systems placed before **2027-08-02** → **2030-12-31** | 🟢 **2030-08-02** for a public-authority deployment — in education, most ministries and state universities |
| **APAC** | Vietnam, law 134/2025/QH15 | in force **2026-03-01** | existing systems comply by **2027-03-01**; **health, education and finance by 2027-09-01** | 🟢 **2027-09-01** — eighteen months after the date this KB's summary tables carried |
| **APAC** | South Korea, Framework Act | in force **2026-01-22** | enforcement decree effective **2026-07-21** made high-impact duties real; investigations and fines **deferred ≥1 year** (→ ~**2027-07-21**); 🔴 **generated-content labelling has no grace** | ⚠️ split — labelling now, the rest ~2027-07-21 |
| **LATAM** | Peru, *reglamento* DS 115-2025-PCM | in force **2026-01-22** | sector obligations for **health, education**, justice, security, economy and finance **activated 2026-09-10**; staged compliance **1–4 years from September 2025** by sector and size | 🔴 **2026-09-10 — already passed** |
| **North America** | no federal high-risk statute; DOJ ADA Title II IFR | — | ⚠️ **no transition article exists, because no binding federal high-risk statute does**; state duties attach at enactment | **2027-04-26** (DOJ ADA Title II IFR, ≥50,000 population) |

### 🔴 The second-order effect, and it is the one that changes a proposal

🔵 **The EU extension is conditional on the design remaining unchanged. Vietnam's is conditional on a
filed transition plan, and a reclassification restarts a 12-month clock.** Grandfathering is
therefore not a property of a system — it is a property of a system **being left alone**.

⚠️ **An AI Studio engagement is definitionally the thing that does not leave it alone.** Adding a
tutor to a legacy LMS, wiring an agent into an SIS, replacing a rules-based placement engine with a
model: each is a change in design, and each converts a system that had until **2030-08-02** into one
that must satisfy Annex III **the day it ships**.

🟢 **So the conformity work is in scope of the modernisation phase, not of a later phase the
extension pays for — because the modernisation is what ends the extension.** ⚠️ **The sales failure
mode is the reassuring sentence** — "you have until 2030" — true until the client signs the statement
of work that makes it false.

🟢 **And the inversion is a sellable engagement this KB had no language for: the non-modifying
mandate.** Observability, evidence, inventory and an accessibility remediation queue built *around* a
frozen high-risk core — which **banks** the extension instead of spending it, and is exactly what the
evidence tier in `repos/foundations.md` and pattern **`P-TRANSITION-EVIDENCE`** deliver.

### 🔵 Why this is a trend and not a news item

Because the shape repeats across four jurisdictions written independently of each other: **a duty, a
later date for what already exists, and a condition that the existing thing not be touched.** The EU
wrote it as design stability, Vietnam as a filed plan plus a sector-specific extension, Korea as
deferred enforcement with one carve-out that bites immediately, Peru as a staged activation by sector
and organisation size. ⚠️ **Four regimes, four mechanisms, one commercial consequence** — the
regulated moment is the *change*, not the calendar.

### ⚠️ The qualification this trend carries, stated plainly

🔴 **The primary texts could not be read.** `eur-lex.europa.eu`, `artificialintelligenceact.eu`,
`ai-act-law.eu`, the Commission's AI Act Service Desk, `loc.gov` and the law-firm notes all returned
**`EGRESS_BLOCKED`** from this environment's proxy. The dates above are **triangulated across
independent search summaries naming the same instrument, article and date** — a weaker standard than
this KB's payload rule for licences, and recorded as such. ⚠️ **Re-read the instrument before any of
these dates enters a client proposal.**

---

## 47. A knowledge base that corrects itself needs unambiguous pointers, and this one has eight duplicated trend numbers

**Twentieth pass of 2026-10-06.** This is a trend about this KB's own machinery, recorded here
because the nineteenth pass's headline finding was a correction that failed to propagate — and its
own pointer is ambiguous.

| Measurement of `intel/trends.md` | Value |
|---|---|
| Numbered trend headings | **54** |
| Highest number used | **45** |
| 🔴 Duplicated numbers | **8** — `33`, `34` (**three times**), `35`, `36`, `37`, `38`, `39`, `40` |
| Skipped by the later series | `41`, `42` — used once each earlier, then 40 → 43 |
| 🔴 Cross-references in this KB pointing at an ambiguous number | **27** — `agents/trending.md` 9, `compose/patterns.md` 8, `intel/market.md` 4, `intel/trends.md` 4, `repos/trending.md` 2 |
| 🔴 References to **`trend 39`** alone | **13** |

🔵 **The nineteenth pass found a correction that could not reach an assertion written after it, and
fixed the assertion. But that finding is addressed to "trend 39" — and this file has two.** A reader
following the pointer lands on *"Integration coverage follows the higher-education install base"* as
readily as on *"The regulation stopped being forthcoming and started being in force"*. ⚠️ **A
correction whose dependents are named by an ambiguous key is not propagated — it is only filed.**

🟢 **The prescription is deliberately the cheap one: cite trends by title, and do not renumber.**
Renumbering would silently invalidate **27 live cross-references** across five files, trading an
ambiguous pointer for a confidently wrong one. The numbers remain historical labels; **the title is
the key.** ⚠️ **And the rule for later passes: before writing `trend N`, grep `^## N\.` and count
the hits.**

### 🔴 And the same defect is worse in `compose/patterns.md`, where it was found by writing into it

This pass went to add a pattern, chose the next free number by reading the highest one in the file,
and **collided with three existing definitions.**

| Measurement of `compose/patterns.md` | Value |
|---|---|
| Numbered `## Pn` headings | **46** |
| Distinct numbers | **36** |
| 🔴 Duplicated numbers | **7** — `P1` ×2, `P25` ×3, `P26` ×3, `P27` ×2, **`P28` ×3**, `P29` ×2, `P30` ×2 |
| 🔴 Cross-references in this KB pointing at one of those seven | **137**, across ten files — `compose/patterns.md` 64, `intel/market.md` 17, `agents/trending.md` 15, `agents/top.md` 9, `repos/foundations.md` 6, `intel/trends.md` 6, `repos/trending.md` 5, `verticals/solutions.md` 4 |

🟢 **This KB already owns an instrument for the adjacent defect, and it is a good one.**
`compose/code/pattern-citation-audit/` detects **dangling** citations — numbers cited but never
defined — and its 8 assertions pass. Run against the current tree it reports **36 patterns defined**
and dangling citations running up into the **P60s**, inherited from the pre-reset era and still
present in the live append-only files.

🔴 **But it cannot see this defect, because it asks the opposite question.** A number defined **three
times** is defined, so it never dangles; the audit passes it. ⚠️ **Dangling and duplicated are two
different failures of the same namespace, and an instrument for one is not an instrument for the
other.** The one-line addition that would close it: assert that each number resolves to **exactly
one** definition, not **at least one**.

🟢 **What this pass did about it, rather than only recording it.** The new pattern is named
**`P-TRANSITION-EVIDENCE`**, not given a number. A content key cannot collide, cannot dangle, and
tells a reader what it points at without a lookup. ⚠️ **It is not a migration** — the 137 existing
references stay as they are, for the same reason the trend numbers do: renumbering would trade an
ambiguous pointer for a confidently wrong one. 🔵 **It is the convention for new entries only**, and
the cheapest possible fix is simply to stop minting numbers into a damaged space.

🔵 **Why this generalises beyond this KB.** Any append-only corpus maintained by automated passes
accumulates identifiers faster than it accumulates a way to allocate them. The failure is silent:
nothing breaks, the number is simply reused, and every pointer written before the collision keeps
resolving — to the wrong target half the time. 🟢 **The durable fix is to key corrections to content,
not to position** — which is also why this KB's correction blocks quote the sentence they are
correcting rather than citing its line number.

---

## 48. The licence you can redistribute and the licence you install are two different facts, and the industry publishes only the first

🔴 **Measured, not argued: 13 education projects, 352 declared direct dependencies, and the two
layers disagree for 4 of the 13.** The shelf licence is a public, prominent, well-governed fact —
every project puts it in the sidebar, and this KB spent twenty passes reading it from the payload
rather than the badge. 🔵 **The dependency layer is equally public and nobody reads it**, because
nothing in the ecosystem's presentation puts it next to the first.

| Project | Published licence | What `pip install` / `npm install` adds |
|---|---|---|
| DeepTutor (40.8k★) | Apache-2.0 | **AGPL-3.0** or a paid Artifex licence, via `PyMuPDF` |
| Oppia | Apache-2.0 | **GPL-2.0-or-later**, via `mutagen` |
| Kolibri | MIT | **LGPL** ×2 |
| A11y MCP | MIT | **MPL-2.0** ×2, via `axe-core` |

🟢 **The base rate is the other half of the trend and it is good news: 337 of 352 dependencies
(95.7%) are permissive.** This is not a story about an unsafe ecosystem. It is a story about **where
the remaining 4.3% hides** — never in the project you evaluated, always one declaration down.

⚠️ **The commercial consequence is asymmetric, which is why it is worth a trend.** Discovering an
AGPL dependency during due diligence costs an afternoon. Discovering it after a fixed-price delivery
has shipped a hosted tutor costs either a source-disclosure obligation over the whole service or a
commercial licence bought under time pressure. 🔵 **The cost of the check is one command; the cost of
skipping it is a renegotiation.**

🟢 **The engagement rule this yields:** quote the dependency closure, not the repository licence, in
any document a client signs. **"MIT" describes the code the maintainer wrote. It does not describe
the build you are about to hand over.**

## 49. A manifest returning HTTP 200 is evidence the file exists, not evidence it declares anything

🔴 **Five of 17 targets this pass declared zero dependencies, and all five files fetched fine.** Not
one was a parser bug. Four distinct shapes, each of which turns a filename-keyed sweep into a
confident wrong answer:

| Shape | Live case | The wrong answer it produces |
|---|---|---|
| **empty sink file** | Kolibri: `requirements.txt` is a build-time `EXTRA_REQUIREMENTS` sink **and** `[project].dependencies = []`; the real set is in `[dependency-groups] base` | 🔴 "zero dependencies" |
| **workspace root** | `mentingo`, `OpenTutor`: root manifest is `devDependencies` + pnpm; runtime lives in `apps/*` | 🔴 "no runtime dependencies" |
| **meta-package** | `agent-framework`: one dep, `agent-framework-core[all]` | ⚠️ "1 dependency" — true and useless |
| 🟢 **genuine zero** | `WCAG-Accessibility-Skills` | 🟢 correct, and it **confirms the project's own documented claim** |

🔵 **The epistemics matter more than the parsing.** A missing measurement announces itself; a
**confident wrong one does not**, and "this project has no dependencies" reads like a clean bill of
health. ⚠️ **The only defence is a positive control** — an instrument that cannot distinguish "zero
because nothing is declared" from "zero because I looked in the wrong file" is not measuring
anything. This pass had exactly one genuine zero out of five, and it is the row that proves the other
four are findings rather than silence.

🟢 **This is the same lesson as this KB's licence-filename case sweep (pass 12) and its
`LICENSE`-outside-root catalogue, arriving a layer down: the anchor recognises a SPELLING, and the
object is a DECLARATION.** The family now has four members at the repository layer and four at the
manifest layer.

## 50. A correction that lands only in a pass-scoped section has been filed, not applied

🔴 **Third reproduction of one failure mode, on a third unrelated fact.** The pattern is now stable
enough to be a trend rather than three incidents:

| Pass | The fact | Where the correction landed | Where it failed to reach |
|---|---|---|---|
| 19 → 20 | AI Act Annex III deferred to **2027-12-02**, not in force 2026-08-02 | trend 39, seventeenth-pass EMEA paragraph | a **third** location in `intel/market.md`, found by a structural gate a pass later |
| 17 → 21 | a **third** market series, $8.3B → **$11.4B (2026)** → $57.2B by 2033 at **25.9%** | the seventeenth pass's own section, ~3,600 lines down, correctly named and prescribed | 🔴 **the `## Global market size` table at the TOP of the same file**, which kept presenting 40.9% as settled |

🔵 **The second row is the embarrassing one and it is recorded on purpose.** The twenty-first pass ran
the mandatory trends query, got the third series back, and **began writing it up as a new finding** —
a rival series this KB had supposedly never seen. It had seen it, four passes earlier, and had written
a better prescription for it than the one being drafted. ⚠️ **The re-discovery was caught only because
the pass went to edit the duplicate `## Opportunities by region` heading and read the surrounding
section on the way.**

**Measured spread of the un-propagated figure across non-archive files:**

| Token | Occurrences |
|---|---|
| `40.9%` | **19** |
| `42.48` | **12** |
| `11.4B` | **10** |
| `25.9%` | **6** |

⚠️ **Nineteen against six is not a disagreement between sources, it is a disagreement between this
KB's own files**, and a reader who quotes the top of `intel/market.md` gets the 19 without ever
meeting the 6.

🟢 **The rule, and it is cheap: a pass that corrects a published figure must edit the table that
publishes it, in the same pass.** Describing the correction in a dated section is necessary — the
append-only history is how this KB stays auditable — but it is **not sufficient**, because nobody
quotes the history, they quote the summary table. 🔵 **A correction has two halves: the record and the
edit. This KB has been reliably doing the first and intermittently doing the second**, and the three
rows above are what that looks like after twenty-one passes.

🟢 **Corrected this pass:** all three market series now sit side by side in the
`## Global market size` table, each with its base year, terminal year and CAGR attached. The
commercial rule stands as the seventeenth pass wrote it — **quote 2026 as a range ($10.6–11.4B) and
attribute every horizon figure to its publisher by name.** ⚠️ **Never quote a bare CAGR**: between
these three series it ranges from 25.9% to 41%, and the choice silently moves a 2033 number by
roughly 3×.

## Declared gaps — twenty-first pass, 2026-10-06

🔴 **Named here because an unreported gap looks exactly like coverage.**

| Gap | Status, and why it is open |
|---|---|
| **The shelf's vulnerability history is entirely unmeasured** | 🔴 **NEW and now explicit.** `api.osv.dev` returns **403** at the egress proxy, and `api.github.com` has been 403 since pass 37, so no advisory, GHSA or CVE channel exists from this environment. ⚠️ **Twenty-one passes have recommended Moodle, Open edX, Canvas, Oppia and Kolibri without once checking a published vulnerability against them.** A pass with a reachable advisory source should treat this as its channel |
| **Real adoption still cannot be separated from stars** | 🔴 **Probed and closed again this pass:** `pypistats.org` and `api.npmjs.org` both **403**. Download counts are the one signal that would distinguish an asset in production from an asset being starred, and they are not reachable |
| **Transitive dependency licences** | 🔴 **OPEN, by design.** This pass measured depth 1 only. Hypothesis pre-registered in the instrument's README: depth 2 **raises** the copyleft count, because `certifi`'s MPL-2.0 is transitive almost everywhere. Falsifiable — if depth 2 adds no new copyleft *class*, depth 1 was sufficient |
| **Three shelf rows have no closure measurement at all** | 🔴 `Selleo/mentingo` and `zijinz456/OpenTutor` (pnpm workspace roots — read `apps/*`), `Miaotofu01/Study-Mate` (vestigial `package.json`). ⚠️ **Listed as unmeasured, never as clean** |
| **No SBOM layer anywhere on the shelf** | 🔴 **NEW.** No `syft`, `cyclonedx`, `pip-licenses` or `license-checker` row exists. The twentieth pass found the same absence one layer up (`mlflow`, `dvc`, `evidently`, `croissant`, `fairlearn`: zero occurrences). Not shelved this pass because none of them was verified against an education deployment |
| **Six dependency rows are unreadable at the registry layer** | ⚠️ Resolvable at the **repository** layer, where this KB already has a working channel. Prediction recorded before measurement: `python-dateutil` resolves permissive, `azure-cognitiveservices-speech` stays proprietary |
| **The education-agent and GitHub-trending queries** | ⚠️ **Thin for the third consecutive pass**, which makes it a stable property of the channel rather than a bad day. "Education" in a trending feed means *learning to build AI*, not *AI for schools* |

## 51. Every forge's licence field is a classifier, and a second one is now measured wrong — while its search cannot filter by licence at all

**Added in the twenty-second pass of 2026-10-06. This extends trends 23 and 29 to a second forge,
and the direction of the error is the same.**

Trend 23 established that the licence *label* and the licence *grant* have come apart, and that
reading the payload is the floor. Trend 29 established that GitHub's licence **index** can report
"not specified" about a repository carrying a complete MIT grant, so every licence-filtered
zero-result has an invisible false-negative floor.

**Measured this pass on GitLab, 22 payloads read first-hand against the forge's own
`license.key`:**

| What the forge said | What the file said | Class |
|---|---|---|
| `agpl-1.0` | **GNU GPL v2**, 15,214 B — byte-identical to this KB's reading of the same project on GitHub | 🔴 wrong by two families |
| `ecl-2.0` | **Apache-2.0**, verbatim, zero occurrences of "Educational Community" | 🔴 wrong |
| `other` | **LGPL-3.0**, named in the file's own first three lines | ⚠️ silent about a knowable answer |
| `gpl-2.0+` | plain **GPL-2.0**; the "or later" is nowhere in the payload — but the project's `composer.json` declares **`GPL-2.0-or-later`** | 🔵 **agreement, and the one case where the payload *under*-reads the grant** |
| `other` ×2 | **REUSE pointers**; the real answer is a *set* of 4 and of 6 identifiers, two of them `LicenseRef-` | 🔵 not a grant at all |
| agreed | — | 🟢 16 |

**Seventeen agree, two wrong, one silent, two REUSE pointers of 22.** The ECL-2.0 case is the instructive one:
**ECL-2.0 is a modified Apache-2.0**, differing in its patent grant, so a similarity classifier will
confuse them — and in education that is the *worst* pair to confuse, because ECL is the licence the
higher-education consortia actually use.

🔴 **And the half with no workaround: `license=true` on GitLab's project-**search** endpoint is
silently ignored. 0 of 534 projects came back with a licence**, while the same parameter on the
single-project endpoint resolves correctly. On GitHub a licence filter is *lossy*; on GitLab there is
**no licence filter at all**. A candidate costs two requests: one to find it, one to learn whether it
carries a grant.

**What this means for how absence is priced.** This KB declares gaps, and clients buy against them.
Trend 29 already said a licence-filtered zero-result is a claim about an index. This pass adds the
stronger form: **on at least one major forge, a licence-filtered sweep is not weak evidence, it is
not possible** — so any "no permissive X exists" claim that leaned on a licence filter was measuring
GitHub's index and calling it the world.

**The rule, stated so it can be applied:** a forge's licence field is a hint for *triage ordering*
and is never written into a row. ⚠️ **Including when it agrees** — 16 of 22 agreed here, and the
agreement is unverifiable without the read that makes it redundant.

## 52. This KB cannot measure whether its own shelf is alive, and the reason is one HTTP status

> 🔴 **FALSIFIED at the twenty-third pass of 2026-10-07.** `git ls-remote` plus a blob-filtered
> depth-1 fetch dated **884 of 904** references without touching `api.github.com`. The title
> over-claimed what this trend's own closing paragraph already knew. See *"Trend 52 is falsified"*
> at the end of this file; what survives of it is recorded there too.

**Added in the twenty-second pass of 2026-10-06.**

`api.github.com` has returned **403** to this environment since pass 37. Forty-plus passes have
therefore recorded, for every GitHub row: licence (read from payload), ★ (read from the rendered
page), description, release tags — and **never once a commit-recency measurement**, because the
endpoint that serves `pushed_at` is the one that is blocked. The nineteenth pass audited 475
references for *liveness* and found "nothing newly dead" — but the probe it used was **licence-payload
reachability**, which a repository abandoned in 2021 passes just as cleanly as one committed to this
morning.

**GitLab's API serves `last_activity_at` for free, to an unauthenticated caller.** Measured on the
534 education projects this pass swept:

| | Count | Share |
|---|---|---|
| touched in 2026 | 254 | **47.6%** |
| touched in the last 30 days | 100 | **18.7%** |
| untouched since before 2024 | **179** | **33.5%** |

**One project in three is more than two years cold** — and three of this pass's own candidates were
rejected on exactly that basis (`particify/.../arsnova-lms-connector`, MIT, last commit **2022-09-12**;
`moodlenet/moodlenet`, AGPL-3.0, **2023-07-07**).

**The trend is the asymmetry, not the number.** Maintenance status is the second question any client
asks after licensing, this KB answers it for GitLab rows and cannot answer it for the ~470 GitHub
references that are its substance. 🔵 **It is also not hopeless:** a shallow `git ls-remote` returns
ref SHAs without the API, and a `--depth=1` clone returns the head commit's date — both channels this
KB has already proven open. ⚠️ **Pre-registered as the action for the next pass: measure head-commit
recency for the twenty highest-value GitHub rows via `git`, not via an API, and publish the
distribution next to this one.** If it comes back similar to 33.5%, roughly a third of this KB's
shelf is cold and several patterns need their components re-picked.

---

## 53. The licence tells you if you may use it; only the date tells you if anyone else still does

**Added in the twenty-third pass of 2026-10-07.** Measurement window 2026-10-06 ~21:00 UTC →
2026-10-07 00:00 UTC; ages computed against the reference date 2026-10-06.

For twenty-two passes this KB described every repository on two axes — **licence** (read from
payload, rigorously) and **★** (read from a rendered page, and pass 22 showed ★ measures a host's
audience rather than adoption). Both are properties of a repository **at rest**. Neither says
whether anyone is still working on it.

Adding a time axis did not change which repositories exist. It changed **which ones to pick**, and in
one case it inverted the choice completely:

| | `packbackbooks/lti-1-3-php-library` | `1EdTech/lti-1-3-php-library` |
|---|---|---|
| licence payload | Apache-2.0, 11,343 B, `sha256 78b49eea…` | Apache-2.0, 11,343 B, `sha256 78b49eea…` |
| head commit | 🟢 **2026-09-23** | 🔴 **2020-06-03** |

**Identical grant, identical bytes, same library, 2,303 days apart — and this KB cited the cold
one.** No licence audit, dependency audit or star count could have caught it.

🟢 **The generalisable claim:** licence answers *may we*, ★ answers *who noticed*, **date answers
*will anyone fix it*** — and for a component going into a client deliverable with a support
expectation, the third question is the one the client is actually buying. A licence-and-★ shelf is a
**catalogue**; a licence-★-and-date shelf is a **recommendation**.

⚠️ **A date is not a verdict.** A 472-day-old 1EdTech-certified QTI player may still be the right
pick, because certification does not lapse when maintenance pauses; a 0-day-old repository may be a
week old in total. The rule is **disclose, then argue** — never **sort and prune**.

---

## 54. Liveness is tier-structured, and in this KB it is inversely correlated with how regulated the tier is

**Added in the twenty-third pass of 2026-10-07.**

The aggregate was the least informative number produced by dating 884 repositories. **The spread
between tiers was 9×, measured inside one KB in one sitting:**

| Tier | n | in 2026 | 🔴 cold >1 y | 🔴 pre-2024 |
|---|---|---|---|---|
| MCP side-cars | 121 | **90.9%** | 🟢 **5.0%** | 🟢 **0.0%** |
| whole KB | 873 | 73.3% | 23.1% | 11.2% |
| eval tier | 17 | 52.9% | 35.3% | 5.9% |
| voice / speech | 13 | 53.8% | 46.2% | 0.0% |
| **interoperability (LTI/QTI/OneRoster/Caliper/xAPI)** | **73** | 🔴 **50.7%** | 🔴 **46.6%** | 🔴 **34.2%** |
| Kennisnet (NL national metadata) | 9 | 33.3% | 66.7% | 44.4% |
| Sunbird estate | 8 | 12.5% | 75.0% | 62.5% |
| India substrate (AI4Bharat et al.) | 8 | 12.5% | 87.5% | 0.0% |
| LATAM indigenous NLP | 10 | 🔴 **0.0%** | 🔴 **100%** | 🔴 70.0% |
| Kuali estate | 4 | 🔴 **0.0%** | 🔴 **100%** | 🔴 **100%** |

🔴 **The ordering is close to the inverse of how much this KB argues each tier matters
commercially.** Trend 28 records that **39% of district RFPs score interoperability**; the
interoperability tier is the coldest thing here that is not an abandoned consortium. Trends 21 and
25 build equity and mother-tongue arguments on language substrates; **LATAM indigenous NLP is 100%
cold and the India substrate has nothing touched in 30 days.** The newest tier — MCP side-cars, which
no regulator scores and no RFP names — is the liveliest by a wide margin.

🔵 **The most plausible reading is maturity, not neglect.** A standards implementation that passes
conformance can be correct and finished; a protocol that changed in 2026 cannot. But the commercial
consequence does not depend on which reading is right: **the tier a buyer scores hardest is the tier
whose components you will be maintaining yourself**, and that belongs in the price.

🟢 **One genuinely reassuring result.** `compose/patterns.md` — the components actually wired into
engagements — is **warmer than the foundation shelf it draws from** (18.8% vs 33.0% cold).
Twenty-two passes of composition, without once reading a date, still selected disproportionately
from the live subset.

⚠️ **Do not compare these figures to pass 22's GitLab 33.5%.** That was an undifferentiated search
population; this is a curated shelf. The valid comparison is tier against tier, inside one corpus,
measured the same minute — which is what the table above is.

---

## 55. A `LICENSE` file is a filename, not a grant — and the strongest counter-example is a refusal

**Added in the twenty-third pass of 2026-10-07.**

This KB's licence-reliability work has moved through three failure classes. The third is new, and it
breaks the assumption the first two still shared:

| Class | Recorded | Shape | What it breaks |
|---|---|---|---|
| detector names the wrong OSI licence | trend 23; pass 22 (2 wrong of 20 payloads) | label ≠ grant, **between** parties | reading the sidebar |
| the project contradicts itself | pass 22 (`sam-lms`: ISC badge, MIT payload) | disagreement **inside** one project | reading any single source |
| 🆕 **the file is an anti-grant** | **this pass** | the payload **withholds every right a licence confers** | reading the *filename* as evidence at all |

[`Wahid7852/Verbix-Flutter`](https://gitlab.com/Wahid7852/Verbix-Flutter) carries `LICENSE.md`,
**208 bytes**, and GitLab classifies it `license_key: "other"`:

> *Copyright (c) 2024 Swati Sharma · This code is provided for viewing purposes only as part of a
> Google Solution Challenge. No permissions are granted for reuse, distribution, or modification.*

🔴 **Every pipeline that counts "repositories with a licence file" counts this as covered.** So does
every dependency scanner that treats `other` as "needs review" and then reviews nothing. The rule
this KB now operates under: **payload first, manifest second, detector never alone** — and, added
here, **presence never at all.**

🔵 **The same shape, inverted, is the larger supply story.** Four education projects measured across
the last two passes are real, active, and carry **no grant of any kind**: three LATAM
(`ccsl-ufpa/educacaovigiada-org-br`, `angeelrdz-group/nova-aula`,
`evertonwilliam/plataforma-de-educacao`) and — new this pass, and the reason the framing had to
widen — one **North American**, [`cderda/cargogetgraded`](https://gitlab.com/cderda/cargogetgraded),
a step-level algebra autograder piloting in Fall 2026 whose root tree was enumerated to establish
that no licence file exists anywhere in it.

🟢 **Ungranted-but-real is therefore a global condition with a LATAM concentration, not a LATAM
condition** — and unlike an absence, it is fixable in a week by someone who knows which file to add.
That is `P-GRANT-CLINIC` in `compose/patterns.md`.

---

## 🔴 Trend 52 is falsified — by a channel it named itself

**Twenty-third pass of 2026-10-07.** Trend 52, written one pass earlier, is titled *"This KB cannot
measure whether its own shelf is alive, and the reason is one HTTP status."* **It can, and the status
was never the obstacle.**

`api.github.com/repos/*` does return **403** — and so do `/search/*`, `/orgs/*` and `/licenses/*`,
re-probed this pass, while `api.github.com/` and `/rate_limit` return **200**, so it is the resource
paths that are denied rather than the host. But `pushed_at` was never the only way to date a
repository:

```
git ls-remote https://github.com/<slug> HEAD            # existence  → ref SHA
git fetch --depth 1 --filter=blob:none origin HEAD      # head commit
git log -1 --format=%cI FETCH_HEAD                      # its date
```

**884 of 904 references dated, in under two minutes, with no API.** 🔵 Trend 52's own closing
paragraph names both commands as *"channels this KB has already proven open"* and then pre-registers
the measurement for a later pass — so the trend's **title** over-claimed what its **body** already
knew. That is the transferable lesson, and it is not about GitHub: **an impossibility claim written
from one blocked endpoint will usually survive only until someone tries the second endpoint in the
same paragraph.**

🟢 **What survives of trend 52:** the observation that forty-plus passes recorded licence, ★ and
description while never recording recency, and that pass 20's liveness audit used **licence-payload
reachability** — a probe an abandoned repository passes as cleanly as a live one. Both true, both
the reason this pass was worth running. 🟢 **And pass 20's conclusion itself survives the stronger
probe: zero newly dead across 904 references.**

⚠️ **One thing trend 52 got right that this pass could not fix:** `huggingface.co` (000) and
`codeberg.org` (000) remain unreachable, and the 15 LATAM self-hosted forges probed under pass 22's
pre-registered action B returned **000 on all 45 requests — as did a deliberately bogus control
host.** That probe does **not** discriminate, so it yields no finding about LATAM self-hosted supply
in either direction, and none is recorded.

---

## 56. The fork is the default search result, and the licence holder is the cheapest way to detect it

**Added in the twenty-fourth pass of 2026-10-07.** Two of this KB's three Learning Tools
Interoperability picks turned out to be **cold forks of live upstreams**, found one pass apart, and
in both cases **the field that identified the upstream was already written down in this KB**.

| Language | What was cited | Age when caught | Live upstream | Age | The field that gave it away |
|---|---|---|---|---|---|
| PHP | `1EdTech/lti-1-3-php-library` | 🔴 2,317 d | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 14 d | the **composer package name** |
| Python | `Harvard-University-iCommons/django-lti` | 🔴 406 d | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 2 d | the **licence payload's copyright holder** |

🔴 **Pass 23 wrote the second clue down and marked it with a warning symbol.** Its table recorded the
Harvard repository's MIT payload as *"⚠️ The Regents of the **University of Michigan**, 2022"* — and
moved on. A payload holder that is not the publishing institution is **not primarily an attribution
defect; it is a lineage signal.**

**Why the fork outranks the upstream.** A standards body, a famous university or a well-known
organisation publishing a fork gives that copy the institutional name, the inbound links and the
search rank. The upstream — a vendor (`packbackbooks`) or a university *unit*
(`academic-innovation`) — has none of those. **Searching by reputation returns the fork; searching
by provenance returns the library.**

### The operational rule

> 1. **Holder ≠ publishing account ⇒ treat it as a fork hypothesis**, not a footnote.
> 2. **Resolve it against the package registry's declared homepage** — PyPI `project_urls`,
>    npm `repository`, the composer name. This works where `api.github.com` is 403, as it is here.
> 3. **Enumerate the remote's tags** (`git ls-remote`). A copy whose tags stop six minor versions
>    below the registry's current release is a fork, whatever its README says. `django-lti`:
>    Harvard tops out at `v0.3.2`, PyPI serves `v0.10.1`.
> 4. **An organisation's *old name* is a staleness signal by construction.** `IMSGlobal` became
>    1EdTech in 2022; a repository still under `IMSGlobal/` has not been touched since. P1's
>    component had not been touched for **3,600 days**.

🔵 **This KB already owned both halves of the instrument and had never connected them:**
`compose/code/p184-holder-mismatch/` sweeps holders, `compose/code/fork-lineage-audit/` resolves
lineage. Wiring them is pre-registered as the next pass's action A.

⚠️ **The commercial consequence is not pedantry.** The forked copy is not merely older — it can be a
**different protocol generation**. P1's component implements **LTI 1.1 and LTI 1.0 extensions and
not LTI 1.3 at all**, which is the version every procurement rubric in `intel/market.md` scores. A
component audit that checks licences and stars but not **provenance and protocol version** will pass
a library that cannot win the bid it was selected for.

---

## 57. A repository's commit date and its build's release dates are different facts, and only one of them is what a client installs

**Added in the twenty-fourth pass of 2026-10-07.** Pass 23 dated 884 repositories by head commit.
This pass dated the **293 depth-1 dependencies** those repositories declare, by latest release.
Against identical cut dates:

| | Installed tier (292 deps) | Citing tier (884 repos) |
|---|---|---|
| median age | **65 d** | 42 d |
| 🔴 cold > 1 year | **30.1%** | 23.0% |
| 🔴 pre-2024 | **13.0%** | 11.1% |

🟢 **The installed tier is older — by 1.31× on the cold bucket.** ⚠️ **And the aggregate is the
least useful number produced.** The actionable finding is that **the two dates can diverge inside a
single project**, in both directions:

| Project | Commit channel | Release channel | What the divergence means |
|---|---|---|---|
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **7 d** | 🔴 **median dependency 604 d**; 21/35 cold | maintained **project**, 2020-era **build** (Material-UI v4, superseded 2021) |
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 2 d | 🟢 61 d | healthy on both — the shape to look for |
| `Harvard-University-iCommons/django-lti` | 🔴 406 d | 🔴 not published | a fork, and both channels say so |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🟢 6 d | 🟢 6 d | commit and release in lockstep — a release-driven project |
| `dmitry-viskov/pylti1.3` | 🔴 1,416 d | 🔴 1,417 d | **both channels agreeing is the signature of abandonment**, as distinct from a finished library |

### What to do with it in an engagement

1. **Quote the median, disclose the maximum.** `oppia/oppia` has the oldest dependency in this KB
   (`crcmod`, **5,923 d**) and a median of **60 d**. The maximum describes a legacy tail; the median
   describes the build you inherit.
2. **A green head commit does not price an adoption.** Adopting OATutor means adopting its front
   end. The first sprint is a dependency uplift, not a feature. **Put it in the estimate.**
3. **One cold channel is a question; two are an answer.** Cold commits with fresh releases means
   vendored or branch-based development — look harder. Cold on both means abandoned.
4. **Ages from this channel are lower bounds.** It dates the *latest* release, not the *pinned* one.
   A pinned manifest is older than reported, never newer.

🔵 **And a `LICENSE`-class correction falls out of the same sweep.** The pass-21 dependency closure
left **6 rows** at `UNKNOWN` licence class. All six are resolved from the registry classifiers:
four were **permissive all along** (`python-dateutil` ×3, whose `license` field reads literally
*"Dual License"* while its classifiers say Apache-2.0 **and** BSD; `semver`, whose field contains
the raw BSD notice text), one was **not a registry package** (`@common/global-config`, spec
`file:./common`), and one is **genuinely proprietary**:
[`azure-cognitiveservices-speech`](https://pypi.org/project/azure-cognitiveservices-speech/),
declared by `oppia/oppia`, carrying *"License :: Other/Proprietary License"* and an empty licence
field.

> 🔴 **`UNKNOWN` was never a licence finding — it was a *parse* finding, and reporting it as risk
> overstated four rows and understated one.** Resolve it against the classifiers before it reaches
> a client. And note the real exposure it was hiding: **an engagement that forks Oppia and ships it
> inherits a Microsoft Speech SDK licence obligation.** Oppia's own Apache-2.0 grant is unaffected —
> a permissive project may depend on proprietary software — but the deliverable is not. The
> permissive substitute is already on this KB's shelf: `k2-fsa/sherpa-onnx`, Apache-2.0.

## 58. The head SHA, not the name, is what tells you whether two slugs are two repositories

*Added in the twenty-fifth pass, 2026-10-07. Instrument:
`compose/code/p436-fork-hypothesis/sha_discriminator.py`.*

Trend 56 established that a licence holder which does not match the publishing account is a fork
signal, and that the package registry's declared homepage resolves the upstream. Run over the
whole 503-slug shelf, that resolution returns **21 rows whose registry names a different
repository** — and **six of them are not forks at all.** They are GitHub **renames and transfers**,
where the old path keeps working as a redirect and nothing visible changes:

| Cited | Declared | Head |
|---|---|---|
| `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` | both `9f05599` |
| `NVIDIA/NeMo` | `NVIDIA-NeMo/NeMo` | both `50c71db` |
| `iterative/dvc` | `treeverse/dvc` | both `56e5982` |
| `adlnet/lrs-conformance-test-suite` | `TryxAPI/lrs-conformance-tests` | both `5bc232d` |
| `stanfordnlp/edu-convokit` | `rosewang2008/edu-convokit` | both `d845ffd` |
| `1EdTech/openbadges-validator-core` | `IMSGlobal/openbadges-validator-core` | both `0a66b52` |

> 🟢 **The rule: a declared-elsewhere row is not lineage until the heads differ.**
> `git ls-remote <a> HEAD == git ls-remote <b> HEAD` is one call, needs no API, and separates a
> rename from a fork exactly. Only after it differs is "which is upstream" a question.

🔵 **And the direction is not fixed.** Five of the six are the KB citing a former name; the sixth
is the **registry** carrying a name the project abandoned in 2022. Neither source is authoritative
alone, which is why the discriminator has to be the ref itself.

⚠️ **Consequence for an engagement, not just for a KB.** A dependency manifest, a vendor
questionnaire or an SBOM that names `iterative/dvc` is naming a repository that now belongs to a
different company. The code is identical today. The *governance* is not, and that is the question
a procurement review is actually asking when it asks who maintains a component.

## 59. Half of what a build installs is pinned, so the registry's latest release is the wrong number by a factor of four

*Added in the twenty-fifth pass, 2026-10-07. Instrument: `compose/code/p437-pinned-version/`.
Supersedes the figures in trend 57, which are left as published and should not be re-quoted.*

Trend 57 separated what a repository **commits** from what its build **installs**, and dated the
installed tier from each dependency's **latest** release. It published the limit honestly: a
manifest pinning `foo==1.0` installs 1.0 regardless. Resolving the specifiers measures the size of
that limit:

| | Latest release | **Pinned release** | Ratio |
|---|---|---|---|
| median age | 57 d | 🔴 **220 d** | **3.9×** |
| cold > 1 yr | 27.2% | 🔴 **42.5%** | 1.6× |
| cold > 2 yr | 15.0% | 23.2% | 1.5× |

🔵 **The reason the gap is this large is a property of the corpus, and it must be quoted with the
ratio or the ratio does not transfer: 52% of these 327 dependency rows are pinned EXACTLY**
(`==1.2.3`), and another 30% are capped (`^`, `~`, `<`). Only the remaining 18% — `>=` and
unpinned — resolve to the latest release, and those are the rows where the two numbers agree.

🔴 **The row this reverses is the one trend 57 called cleanest.** `ronantakizawa/a11ymcp` was filed
as *"0 of 5 cold, oldest dependency 57 d"*. It pins `puppeteer` and `puppeteer-core` at **13.5.0,
released 2022-03-05 — 1,675 days, twelve major versions behind** a current 25.12.0 from a fortnight
ago. Its median moves from **14 d to 686 d, a factor of 49.** `CAHLR/OATutor`'s median triples,
604 d → **1,839 d**.

> **What to put in a bid:** adopting a component means adopting its *pinned* dependency set, not
> the latest versions of its dependency names. Price the uplift from the pin. The two numbers
> differ by 4× at the median of this corpus and by 49× on its worst row, and the *latest*-release
> figure is the one that flatters.

⚠️ **This is still a lower bound.** The manifest is resolved, not the lock file, and a real solver
can only move a capped version **down**.

## 60. `UNKNOWN` is a parse class before it is a risk class — and depth 2 proves depth 1 was enough

*Added in the twenty-fifth pass, 2026-10-07. Instrument: `compose/code/p438-depth2-closure/`.
Closes the depth-2 question the closure's README has carried open since pass 21.*

Extending the dependency closure one level down — what the 268 depth-1 packages themselves
require, runtime only, `extra`-gated and dev dependencies excluded — **doubles it: 276 further
distinct packages.** The licence result does not move:

| | Depth 2 |
|---|---|
| `PERMISSIVE` | **273** |
| `WEAK-COPYLEFT` (MPL-2.0: `tqdm`, `mathquill`) | 2 |
| `STRONG-COPYLEFT` · non-commercial · proprietary | 🟢 **0 · 0 · 0** |
| `UNKNOWN` | 1 |

> 🟢 **No new licence class appears at depth 2. For the licence-class question, depth 1 was
> sufficient, and this gap is closed.**

🔴 **The prediction's conclusion held and its mechanism did not.** Pass 24 expected the copyleft
count to rise via `certifi` (MPL-2.0). **`certifi` is a *depth-1* dependency of this corpus** and
could not have been the route; the rise came from `tqdm` and `mathquill`. 🔵 **A prediction can be
right about the outcome and wrong about every step to it, and recording only the outcome would
have left a false mechanism in the file.**

**And the `UNKNOWN` bucket repeated trend 57's lesson one level down: 4 rows, 3 of them parse
failures.** `glob` and `sax` — two of the most-installed packages on npm — declare
**`BlueOak-1.0.0`**, an OSI-approved permissive licence no rule in the classifier recognised.
`jupyterlab-pygments` puts the licence **text** in the `license` field, and its first 120
characters name no licence. All three are permissive; all three read as risk. The classifier now
knows Blue Oak and prefers the PyPI classifier when the field is prose, with seven new controls.

🔴 **The one that survives is `azure-core`: empty `license`, no `license_expression`, and no
`License ::` classifier at all** — reached only through `azure-cognitiveservices-speech`, the
single proprietary depth-1 row trend 57 found in `oppia/oppia`. A second reason to take that
trend's advice and substitute `k2-fsa/sherpa-onnx`.

🔵 **Dated, the closure has a gradient, and it runs one way:** what this KB **cites** has a median
head-commit age of **48 d**; depth 1 installs at **57 d** (latest) and **220 d** (pinned); depth 2
installs at **177 d** (latest). ⚠️ **Depth 2's pinned tier is not measured and would be older
still** — every level down is older than the one above it, and the number a client is shown is
always the one from the top.

## 61. Where this KB's prose and its instruments disagree about a licence, it has been the instrument — four times out of four

This is a trend about **method**, and it is the finding of the twenty-sixth pass. Pass 25's action A
was sent to resolve the **87 repositories this shelf cites that ship no licence file**. Every licence
fact the action surfaced was **already written in this KB's prose**. What was wrong was the
machinery:

| Defect | Instrument | What the prose already said, and where | Scale |
|---|---|---|---|
| five **MPL-2.0** payloads filed **GPL** | `p436/sweep_payload.family_of` | all five correct as MPL-2.0 in `repos/foundations.md` and `agents/top.md` | 5 of 412 |
| `LICENSE.TXT` read as **no licence** | `p436`'s 14-name rooted probe | `repos/foundations.md`: *"Found at `LICENSE.TXT` — uppercase extension. A nine-name lowercase probe reports this [as ungranted]… two characters away from a name the probe already tried"* | ≥3 of 87 |
| **EUPL-1.2** → `UNKNOWN` | `family_of` **and** `dep_licence.classify_licence` | nine files discuss EUPL; `repos/foundations.md` lists **eight** Finnish national services carrying it | the whole EMEA public-sector tier |
| npm `UNLICENSED` → `PERMISSIVE` | `dep_licence.classify_licence` | — latent; no prose, and no published row | would have fired on this sweep |

🔴 **The detectable symptom was available without a single new fetch: the published family
distribution over 412 licensed payloads contained ZERO MPL-2.0 rows.** A zero, for one of the most
common licences on GitHub, in a 412-row table. Nobody read the distribution as a measurement of the
classifier.

🔵 **The structural cause is that `p342` deliberately chose the other direction.** Its README says,
in so many words: *"the assertions run against the TSVs, not against the prose of the `.md` files."*
That was the right call for catching prose that drifts from measurement. It leaves the **inverse**
uncovered — and the inverse is what happened. **Where a human wrote the licence into the prose and an
instrument later measured it wrong, nothing in this repository compares the two.**

⚠️ **What this trend does NOT say:** that prose beats measurement. Prose is why `p342` exists. It says
that a corpus which versions both must **reconcile** them, and that an instrument marked
`authoritative` whose output contradicts a sentence a human wrote after reading the file is a defect
until one of the two is retracted.

**Consequence for Globant.** On a client engagement the same asymmetry appears as an SBOM that
disagrees with the repository's own README. 🟢 **Reconcile the two before shipping either**, and when
they disagree, read the licence file — the four rows above all resolve that way.

## 62. A filename list can only find a licence; to sustain its absence you must enumerate the tree

`P441`, and it closes a hole this KB had already named three times without closing.

Run over the 87 repositories published as shipping no licence:

| Instrument | Grants found |
|---|---|
| `p436`'s **14 filenames**, rooted | **0** |
| `p440`'s **41 filenames**, rooted | 1 |
| 🟢 `p441`'s **complete tree enumeration** | 🟢 **9** |

A `--filter=blob:none --no-checkout --depth 1` clone plus `git ls-tree -r` lists the whole tree with
no API, no pagination and no truncation, in **13 seconds for all 87**. The nine it finds fail the
filename list on four distinct axes, and **no amount of widening reaches any of them reliably**:

- **extension case** — `openedx/XBlock` ships `LICENSE.TXT`, **Apache-2.0**;
- **a third capitalisation** — `SchoolUtils/WebUntis` ships `License`, **MIT**;
- **family suffix** — `veraPDF/veraPDF-library` ships `LICENSE.GPL` *and* `LICENSE.MPL`, because two
  grants cannot both live in a file called `LICENSE`;
- **depth** — `Opetushallitus/aoe`'s **EUPL-1.2** is in `aoe-web-backend/` and `aoe-web-frontend/`;
  `learningequality/kolibri-server`'s is `debian/copyright`; and
  [`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) carries **three** —
  `LICENSE/LICENSE.code` (**NCSA**, corrected in the twenty-seventh pass — *not* MIT), `LICENSE.original` and `LICENSE.output` (CC-BY-4.0).

🔵 **`cs341-illinois/coursebook` is the row that makes the case.** Separate grants for the code, the
original content and the output is the *correct* structure for a course repository and the one a
single `LICENSE` file cannot express — so a rooted filename probe reports a teaching repository with
exemplary licensing hygiene as having none at all.

🔴 **And enumeration overshoots exactly as symmetrically as the list undershoots.** The first build
published 14 hits; six were an **icon component** named `copyright`, an **XSLT transform**, a vendored
**package manager**, a vendored **ontology tool**, a vendored **editor**, and — the cleanest `P342`
instance this KB has measured — the European Commission's `licence-EUPL 1.2-brightgreen.svg`, a
**README badge image**. So the pattern channel is a *finding* channel whose positives are a reading
list, and stage 2 **reads each candidate blob** and keeps only payloads that classify as a licence
text. 🟢 **Separating the project's own grant from a bundled dependency's needed DEPTH, not a
vendor-name list**: a project states its licence at the root or one directory down, and nothing
states its own licence four levels into a static-assets tree.

**Consequence for Globant.** 🟢 **"No `LICENSE` file" is not a finding; it is a probe result.** Before
discarding a candidate, enumerate the tree and read the registry (`p440`). On this shelf that moves
**15 of 87** repositories out of the unusable column — 9 by the tree, 6 more by the registry alone.

## 63. ⚠️ CORRECTED — every level of a dependency graph is older than the one above it **only when the parent is taken at its latest release**

`p442` closes the gradient `p438` left open with the words *"a pinned depth-2 tier is not measured
here and would be older"*. It is, and it is:

| Tier | basis | median age | cold > 1 yr |
|---|---|---|---|
| what this KB **cites** | head commit | **48 d** | 24.8% |
| installed **depth 1** | latest release | 57 d | 27.2% |
| installed **depth 1** | 🔴 **pinned** | **220 d** | 42.5% |
| installed **depth 2** | latest release | 177 d | 37.0% |
| installed **depth 2** | 🔴 **pinned** | 🔴 **334.5 d** | 🔴 **48.6%** |

🔴 **CORRECTED in the twenty-seventh pass of 2026-10-07 — the monotone claim holds for ONE of the
two possible chains, and `p442` did not state which one it walked.**

`p442` built its depth-2 edge set from each depth-1 package's **latest** release
(`info.requires_dist`, `versions[dist-tags.latest]`), then resolved those specifiers to a pin.
`compose/code/p446-pinned-parent-chain/` walks the chain **pinned the whole way** — the dependency
list of the depth-1 version this shelf actually pins, which `p437` had already resolved — and gets
🟢 **97 d, not 334.5 d.** Depth 2 is then **younger** than depth 1's 220 d, and the ladder is not
monotone.

| | `p442` — latest parent | `p446` — pinned parent |
|---|---|---|
| median pinned depth-2 age | **334.5 d** | 🟢 **97 d** |
| `EXACT` share / median | 21% / 49 d | 11% / 🔴 **1,553 d** |
| `CAPPED` share / median | 56% / 🔴 **694 d** | 58% / 62 d |

🔵 **Both are right about their own corpus, and they disagree about which class carries the
staleness.** With *latest* parents the `CAPPED` rows are current libraries' wide ranges resolving
under a cap that may itself be years old; with *pinned* parents those caps are satisfied by today's
release (62 d) while the `EXACT` rows go to **4.3 years**, because an old pinned parent exact-pins
whatever was current when it shipped. `puppeteer-core` pinned at **13.5.0** (2022) alone contributes
24 of the 100 `EXACT` rows.

⚠️ **The transferable rule is `P446`: when a measurement walks a chain, every leg's version is a
parameter, and a chain with one leg unstated is not reproducible.** Here the unstated leg is worth
**3.4×**. A build installs the *pinned* parent, so for *"how old is what a build installs two levels
down"* the pinned chain is the faithful one; `p442`'s number answers *"how old would the current
releases install"*, which is also a real question and a different one.

🟢 **What survives, and is now better supported than before:** depth 1 is the tier to quote. Under
`p442`'s chain it is the younger tier and under `p446`'s the older, so it is **the only tier both
chains agree is worth measuring** — and it is the one a client's own manifest controls.

🔵 **The original claim is kept verbatim below, because deleting it would hide the correction —
read it as "true of the latest-parent chain", not of the ladder in general:**

> 🟢 **Monotone on both axes, and roughly additive: one level down costs about what resolving the pin
> costs, and doing both costs the sum.** The figure a client is shown is always the one from the top
> of that table; the figure their build installs is the one from the bottom. **Nearly half of what
> lands on disk two levels down is more than a year old.**

🔴 **But the MECHANISM inverts between the tiers, and that is the transferable part.** At depth 1,
**49%** of specifiers are `EXACT` and they carry the whole effect. At depth 2, `EXACT` is **21%** and
its median delta is **zero** — the effect lives entirely in `CAPPED`, at **694 d** pinned against
257 d latest. The reason is structural: a depth-1 manifest is an **application's** and applications
pin exactly; a depth-2 specifier is a **library's** constraint on its own dependency, and libraries
publish ranges so they can be co-installed.

🔵 **This is trend 59's own warning coming true on the next tier.** It wrote: *"quote the class
distribution with the ratio or the ratio does not transfer."* Here is the corpus where it does not —
same shelf, one level down, direction preserved and mechanism replaced.

**The concentration is narrow and therefore actionable.** `react-scripts` contributes **38** cold pins
— the CRA layer under `CAHLR/OATutor`'s 2020-era front end, which `p438` reached from the licence
direction. 🔴 **`aws-sdk` v2 exact-pins nine packages more than two years old**, including
`querystring==0.2.0` at **4,964 d** and `sax==1.2.1` at **3,854 d against a current release 75 days
old** — a **51×** gap on an XML parser. 🟢 **Move to the modular `@aws-sdk/client-*` v3 packages**;
that one substitution removes the worst column in the table.

🟢 **And the exception reproduces.** Trend 59 found exactly one row of 327 where the pin is *newer*
than the latest stable — `oppia/oppia` pinning the pre-release `webapp2==3.0.0b1`. One row of 344 does
the same here: `@material-ui/core` pins `popper.js@1.16.1-lts`, **2,375 d**, against a latest stable
`1.16.1` at **2,450 d**. **Two corpora, two ecosystems, one mechanism — a suffix-tagged release that
postdates the last plain one.** So *"every published age is a lower bound on staleness"* holds in
343 of 344 rows here and 326 of 327 there, and the exception is structural rather than anecdotal.

## 64. Trend 61, measured at corpus scale: the prose wins 18 times out of 19, and the nineteenth is prose a defective instrument overwrote

Trend 61 recorded that where this KB's prose and its instruments disagreed about a licence, the
instrument was wrong — **four times out of four**. Pass 28 built the gate that measures it over the
whole corpus instead of over one pass's findings (`p449`, 6 published files, 431 slugs with a bound
licence claim, 510 co-occurrences where the binding rules refused and said so).

| Verdict | n |
|---|---|
| `AGREE` | **299** |
| `PROSE-ONLY` | 83 |
| `PROSE-MIXED-INCLUDES-TODAY` — the gate **abstains** | 29 |
| 🟡 `STALE-DATA` — prose right, data behind | **14** |
| `DATA-ABSTAINS` — classifier gap, not a prose error | 5 |
| 🔴 `CONTRADICT` — prose wrong | **1** |

**Prose and data disagree on 15 of 431, and the prose is right in 14.** With pass 26's four, the
record is **18 of 19**.

🔴 **And the nineteenth is not a counterexample, it is the mechanism.** The single `CONTRADICT`,
`oat-sa/lib-lti1p3-core`, is published LGPL-2.1 and is GPL-2.0 — but the pre-reset archive carries
GPL-2.0 for it in **nine** places, once as a deliberate finding (*"the exception that breaks the
symmetry — a protocol library and still GPL-2.0"*). The prose **regressed**: a correct human
reading was overwritten by the classifier's wrong answer, and `intel/market.md` then published
EMEA architecture advice concluding *"neither is a blocker."*

**Consequence for Globant:** in a corpus that versions prose and data, the prose is the layer where
somebody read the actual document and the data is the layer a compiler consumes. Neither can be the
sole authority — the prose goes stale and the data is wrong — so the reconciliation has to run in
**both directions** and must **abstain** where the corpus contradicts itself. Asserting
*"against the TSVs, not against the prose"*, as `p342` chose to, was backwards.

## 65. A truncation window is a sampling decision, and carrying one from a picker into a counter silently caps the count

`p441` read `text[:4000]` to pick ONE licence family, where reading further cannot change the
answer because the granting licence names itself at the top. Two functions later the same constant
was governing a function whose entire purpose was to **count** families, and three separate defects
followed from it:

| Defect | Mechanism | Cost |
|---|---|---|
| **`P452`** | the GNU licences name each other; GPL-2.0's Preamble recommends the LGPL at char **784**, GPL-3.0's closing notes at **34,143** | 🔴 **every GPL-2.0 payload filed LGPL**, 7 rows, commercial verdict inverted |
| **`P448`** | the EUPL-1.2 Appendix, which names five other families, begins at char **5964** of a 13,699-char payload | the count of multi-family payloads reads **38** at window 6000 and **73** on full text |
| **`P447`** | patterns written with literal spaces; licence prose wraps at ~72 columns, so a family name straddling a break does not match | LGPL and AGPL invisible in `axe-core`'s real MPL payload |

**Consequence for Globant:** when a client's licence-scanning tooling reports a clean result, ask
what window it read and whether that window was chosen for a different question. A constant that is
provably safe for "which licence is this?" is provably unsafe for "which licences are mentioned?"
and for "is this GPL or LGPL?" — and all three questions get asked of the same payload.

## 66. `CC-BY` is not a licence, it is four licences with opposite commercial answers, and the label hides the only one that matters

One label on this shelf covered plain Attribution, Attribution-NonCommercial,
Attribution-NonCommercial-ShareAlike, and one document that is not Creative Commons at all. Read
line by line, **5 of the 7 rows published `CC-BY` are commercially unusable or mislabelled** — four
are **NonCommercial** and one is a **paid dual-tier** licence.

🔴 **The one to remember:** `sign/translate`'s `LICENSE.md` grants a free tier under CC BY-NC-SA 4.0
to *"individuals, non-profit organizations, and educational institutions"* and states that *"a
separate license is required for for-profit commercial organizations."* The classifier matched
`"creative commons"` at character 848 — inside the free tier's heading — and filed the whole
repository as attribution-only.

🔵 **The structural point: a licence family is not the unit of a commercial decision.** `MIT` and
`Apache-2.0` are safe as families; `CC-BY` and `GPL` are not, because the qualifier (`NC`, `SA`,
`v2` vs `v3`, linking exception or none) carries the answer. A vocabulary coarse enough to be
comparable across a shelf is too coarse to clear a deliverable, and this KB had been using one
vocabulary for both jobs.

**Consequence for Globant:** for any Creative Commons or GNU row, the **qualifier is the finding**
and the family is filing. Publish `CC BY-NC-SA 4.0`, never `CC`; publish `GPL-2.0`, never `GPL`.

## 67. A grant below the root is usually the documentation, and it is usually *more* permissive — but a rooted probe reads it as the code's licence

Full-tree enumeration of all 412 licensed rows (blobless clone + `git ls-tree -r`, every candidate
path read and classified rather than name-matched): **323 `ROOT-ONLY` (78.4%)**, 47
`DIVERGENT-BUNDLED`, 33 `CONCORDANT`, **9 `DIVERGENT-OWN` (2.2%)**.

🔴 **The 9 are not dual-licensed projects — the expected tier produced zero.** Four are an explicit
code/documentation split: `microsoft/autogen` (CC-BY root, `LICENSE-CODE` = MIT), `ankitects/anki`
(AGPL-3.0, `docs-site/` = CC BY-SA), `learnhouse/learnhouse` (AGPL-3.0, `docs/` = MIT),
`yongsoojoo/esd2026-agent-workflow` (MIT, `LICENSE-docs` = CC BY).

🟢 **And the direction is the opposite of the feared one: 0 of 412 pair a permissive root with a
reciprocal grant deeper.** Every divergence runs copyleft-or-CC root → permissive component, or
permissive → permissive.

**Consequence for Globant:** the practical instruction inverts the usual caution. On a repository
whose root grant is Creative Commons or AGPL, **look for `LICENSE-CODE` or `docs/LICENSE` before
writing it off** — on this shelf the code is more permissive than the root in three cases out of
three. The trap is the reverse: a rooted probe on `microsoft/autogen` reports **CC-BY**, which is
the *documentation* licence, for a repository whose code is MIT.

## Declared gaps — twenty-sixth pass, 2026-10-07

- 🔴 **No case oracle exists on this host.** `p443` measured five channels — `raw.githubusercontent`,
  `git ls-remote`, the git smart-HTTP `info/refs` endpoint, rendered `github.com` and
  `codeload.github.com` — and the first three serve **200 for any capitalisation with no redirect**
  while the last two are **403**. So the canonical spelling of a slug is **unknowable from here**, and
  `p439`'s canonicalisation for registry-decided rows is a preference rather than evidence. Its
  collision *detection* is unaffected.
- 🔴 **186 of 496 cited repositories (37.5%) have no spelling oracle at all** — neither a published
  package nor a self-link that names them. Their spelling in this KB is an unverified assertion.
- 🔴 **Maven Central's POM layer is not reliably reachable.** `maven-metadata.xml` answers 200 and
  carries **no licence element**; the POM that does carry it answered **429 for the same URL that
  answered 200 ten seconds earlier**, three times in a row under calibration. A single-shot probe
  cannot distinguish a POM with no licence from a POM that was rate-limited.
- 🔴 **RTF licence payloads are not read.** `docs/LICENSE.rtf` on both `OS4ED/openSIS-*` rows
  classifies `UNKNOWN`, which is a limit of the classifier and not an absence.
- 🔴 **A payload that NAMES other licences cannot be classified by substring order.** Reordering fixed
  MPL-2.0 and EUPL-1.2, where the granting licence is identifiable from the head. It cannot fix
  `nvaccess/nvda`'s *"GPL version 2 or later, with two special exceptions"* whose exception names the
  LGPL. Deciding which named licence is granted and which is referenced is a reading task; the
  instrument now counts the marks and hands over a reading list instead of guessing.
- 🔴 **`NO-CHANNEL` at 57 of 87 bounds the registry approach.** Two thirds of the repositories that
  ship no licence file also publish no package, so there is no second channel to ask.
- 🔴 **Sixteenth consecutive pass in which the mandatory query set produced no new repository**, and
  the tenth with no new instrument. One new named datum in sixteen passes: OpenAI appointed a policy
  lead for Australia and New Zealand — a personnel fact, not a repository. Every repository added this
  pass came from a **package registry** or from `git ls-tree`.

## 64. A guarantee proved in one module protects nothing in another — this KB has two licence classifiers and the hardened one is not the one its instruments call

This KB contains **two** licence classifiers. Measured on the same **19,329 bytes** of
[`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication)'s
root `LICENSE`:

| Classifier | Family | Commercial use |
|---|---|---|
| `lib/license_family.sh` → `osi_family_of` | 🟢 **`CC-BY-NC-4.0`** | 🔴 **NO** |
| `p436/sweep_payload.py` → `family_of` | 🔴 **`CC-BY`** | *(no such axis exists)* |

The shell classifier is the hardened one: **106/106** on its own suite, and **`P312`**, written in
pass 101, exists *specifically* to assert that a NonCommercial payload answers `PROHIBITED` on the
commercial axis **and keeps the `NC` attribute in its family**. **21/21**, offline, for twenty-six
passes.

🔴 **The Python `family_of` has no NonCommercial concept at all — and `family_of` is what `p436`
(the 503-slug payload sweep), `p441` (the tree enumeration) and `p444` (the root-vs-tree
comparison) all call.** Every family verdict those three instruments published passed through a
classifier that cannot express the one attribute that decides whether the work is billable.

**Five rows are the price, and all five report as plain `CC-BY`, a licence that permits commercial
use:** `facebookresearch/seamless_communication`, `openstax/osbooks-biology-bundle`,
`sign/translate`, `Yunfeng-Wan/CSTutorBench`, `Jona-Zwetsloot/Somtoday-Mod`. ⚠️ **Three more bar
commercial use with no `NC` token at all** — `canyongbs/advisingapp` and `sodadata/soda-core`
(**Elastic**), `digillab-lmu/smart-rag` (**PolyForm**), all source-available and not OSI, all
reported `UNKNOWN`. **11 of 412 root payloads restrict commercial use; the Python classifier flags
none.**

🔵 **And the blindness is symmetric, which is what makes this a structural finding rather than a
bug report.** Neither classifier is a superset:

| Case | Python | Shell | Right |
|---|---|---|---|
| NonCommercial (5) | 🔴 erased to `CC-BY` | 🟢 named | **shell** |
| Elastic / PolyForm (3) | 🔴 `UNKNOWN` | 🟢 named | **shell** |
| **EUPL (9)** | 🟢 `EUPL` | 🔴 `UNCLASSIFIED` | **Python** |
| MPL read as GPL (4) | 🟢 `MPL-2.0` | 🔴 `GPL-3.0` | **Python** |
| GPLv2 read as LGPL (4) | 🔴 `LGPL` | 🟢 `GPL-2.0` | **shell** |

🔵 **Each was hardened against the defect the other still has.** Pass 26 reordered the Python
classifier for *"the families that name other families"* — MPL §1.12 naming GPL-2.0/LGPL-2.1/
AGPL-3.0, EUPL-1.2's appendix naming five — and the shell classifier never received that fix. The
shell classifier gained the NC axis and the source-available families in passes 82 and 101, and the
Python one never received those. **No instrument in this KB consults both.**

🔴 **43 of 412 root families (10.4%) are wrong in one of the two, and which one is wrong depends on
the licence family.** There is no single classifier in this repository that gets this shelf right.

⚠️ **The transferable rule, and it is not about licences.** A control suite proves a property of
**the module it imports**. `P312` proved that *the shell classifier* preserves NonCommercial; it
proved nothing about any other code path, and three instruments built afterwards took a different
one. **A guarantee does not propagate by being true — it propagates by being imported.** Rule 1 of
`P126` says do not re-derive what the repository already versions; this is its contrapositive:
**when you do re-derive it, you inherit none of its hardening.**

🟢 **The cheapest channel this KB has used.** Finding this needed no new endpoint, no API and no
clone — only running two functions it already had over the same bytes and reading the difference.

## 65. Every leg of a measured chain is a parameter, and an unstated one here is worth 3.4×

`p442` dated the pinned depth-2 dependency tier at **334.5 d** and concluded the ladder was
*"monotone on both axes"* — trend 63. Walking the same chain with **one leg changed** gives
**97 d**, which makes depth 2 *younger* than depth 1's 220 d and the ladder not monotone at all.

Both chains resolve the depth-2 **specifier** identically — both import `p437`'s resolver, so the
second leg is literally the same code. They differ on **whose dependency list the specifier is read
from**:

| | first leg | endpoint |
|---|---|---|
| `p442` | the depth-1 package's **latest** release | `info.requires_dist` · `versions[dist-tags.latest]` |
| `p446` | the depth-1 package's **pinned** version | `/pypi/<name>/<PINNED>/json` · `versions[<PINNED>]` |

| | `p442` latest-parent | **`p446` pinned-parent** |
|---|---|---|
| median pinned age | **334.5 d** | 🟢 **97 d** |
| `EXACT` share / median | 21% / 49 d | 11% / 🔴 **1,553 d** |
| `CAPPED` share / median | 56% / 🔴 **694 d** | 58% / 62 d |

🔵 **Both are right about their own corpus, and they disagree about which specifier class carries
the staleness.** With *latest* parents the `CAPPED` rows are current libraries' wide ranges, which
resolve to the newest release under a cap that may itself be years old. With *pinned* parents those
caps are satisfied by today's version (62 d) while the `EXACT` rows go to **4.3 years**, because
**an old pinned parent exact-pins whatever was current when it shipped**. `puppeteer-core` pinned
at **13.5.0** (2022) alone contributes 24 of the 100 `EXACT` rows and drags in `rimraf 3.0.2`
(**+2,199 d** behind its own latest) and `https-proxy-agent 5.0.0` (**+2,313 d**); the same package
at latest contributes none of it.

🔴 **Neither number is wrong. Quoting either without naming the parent version is.** A build
installs the *pinned* parent, so for *"how old is what a build installs two levels down"* the
pinned chain is the faithful one; `p442`'s figure answers *"how old would the current releases
install"*, which is a different and also real question.

🟢 **What survives is stronger than what it replaces.** Depth 1 is the tier to quote — under one
chain it is the younger tier and under the other the older, so it is **the only tier both chains
agree is worth measuring**, and the only one a client's own manifest controls. An uplift priced
from the depth-1 pin understates nothing.

⚠️ **The rule generalises past dependencies.** Any measurement that walks a chain — a fork to its
upstream, a slug to its registry entry to its declared repository, a pin to a release to a date —
has a version or a revision at **every** leg. `p437` learned this for the last leg (*the pinned
release, not the latest*). **`P446` is the same lesson for every other leg**, and the test for it
is one question: *could a reader reproduce this number without asking me which version I read?*
## Declared gaps — twenty-eighth pass, 2026-10-07

Stated as gaps rather than left as silence, because an unstated gap is indistinguishable from
coverage.

- 🔴 **No case oracle exists on this host, and a fourth channel confirmed the gap is structural.**
  Pass 26 measured five channels (`raw`, `git ls-remote`, `info/refs`, rendered `github.com`,
  `codeload`) at `200 / resolves / 200 / 403 / 403`. This pass added the shelf itself as a fifth:
  **173 of the 186** unverifiable slugs are cited by **no other repository** on the shelf, and of
  the 13 that are cited, 5 are the same owner and 3 are known fork pairs. **5 genuinely independent
  citations out of 186.** A repository nobody else names has no external spelling, so this gap will
  not close by adding channels.
- 🔴 **The gate abstains on 29 rows where this corpus contradicts itself** (`PROSE-MIXED-INCLUDES-TODAY`),
  and at least one of them carries a live error: `Citolab/qti-components` is described as both GPL
  and LGPL across nine mentions, and it is GPL-3.0. The abstention is honest and it is not a
  verdict. **Pre-registered as pass 29's action A**, resolved by binding each mention to its pass
  date.
- 🟡 **`api.github.com` has been 403 since pass 37** and rendered `github.com` is 403. Every
  structural fact in this pass came from `git` over HTTPS, `raw.githubusercontent.com`, or
  re-reading a file already in this repository. Star counts and fork counts therefore remain
  **uncalibratable on this host** and are carried as published values, not measurements.
- 🔴 **13 of the 412 licensed payloads still classify `UNKNOWN`** after three classifier fixes.
  That is a refusal, not a verdict (`P160`), and it is why the gate has a `DATA-ABSTAINS` class
  rather than counting these as prose errors. The known sub-classes are RTF payloads
  (`docs/LICENSE.rtf`, `OS4ED/openSIS-*`), markdown pointers to another project's terms, and
  bespoke dual-tier documents.
- 🔴 **APAC produced no new repository and no new regulatory instrument this pass**, for the
  seventeenth consecutive pass on repositories. The regional query returns adoption statistics and
  vendor expansion only. **APAC supply on this shelf is the thinnest of the four regions**, and no
  APAC repository appears among the 21 corrected licence rows. An APAC engagement starts from a
  Global or EMEA repository localised, not a regional one.
- ⚠️ **Pass 27's `p445-classifier-divergence` measured `43 of 412` disagreements against the
  **pre-`P452`** Python classifier.** Its published distribution (35 `GPL`, 11 `LGPL`, 9 `EUPL`,
  13 `UNKNOWN`) is this pass's stage-0 intermediate exactly, before the 7 `LGPL → GPL` rows moved,
  so **7 of its rows change on the Python side alone** and the `43` is **stale rather than wrong**.
  Re-running it is pre-registered as pass 29's action C, together with pass 27's own action B.
- ⚠️ **The corrected `family_of` has not yet been propagated to the downstream censuses that
  consumed it** (`holder.tsv`, `homepage.tsv`, the `p250` commercial sweep, the `p419` copyleft
  census). Those still carry the pre-`P452` families. **Pre-registered as pass 29's action B**, and
  named here so the debt is not invisible — which is the exact failure mode pass 26 had, publishing
  a correction in prose and not in the data.

## 68. The two-classifier problem is the industry's, not just this KB's — and two concurrent passes measured it

🔵 **The finding generalises past this knowledge base, which is why it is a trend and not a
method note.** This KB held two licence classifiers over the same 412 education repositories.
Each was independently hardened, each had a passing regression suite, and **they disagreed on
43 of 412 payloads (10.4%)**. Two concurrent passes then repaired them — one each — and the
disagreement fell to **10 (2.4%)**. Every row that moved was a *defect*, not a vocabulary
preference.

🔴 **The direction of the errors is what a buyer should care about**, because they run both
ways commercially:

| Error direction | Example | Cost |
|---|---|---|
| **Over-permissive** — a restricted payload read as usable | 5 payloads reading `CC-BY` where the text says `CC-BY-NC` | 🔴 a non-commercial asset quoted into a billable deliverable |
| **Over-restrictive** — a usable payload read as restricted | `untis4j` LGPL-3.0 read as GPL-3.0; `pupilfirst` MIT read as CC-BY-SA; five MPL-2.0 layers read as GPL | 🔴 a permissive component rejected, and a competitor who read it correctly bids lower |

🔴 **And the sharpest part: the over-permissive class survived both repairs.** Each pass fixed
the classifier it was looking at, and the five rows that can put a non-commercial asset into
an invoice sit in the one neither closed. **A defect that two independent reviewers each
assume the other owns is the most durable kind.**

⚠️ **Every education buyer running an automated licence scan is running one classifier,
once.** The 2026 compliance toolchain commoditised (trend 19) and the scanners it ships are
single-implementation: one regex set, one vocabulary, one set of blind spots, and no second
reader with the right to disagree. **The measured disagreement rate between two independently
hardened classifiers over the same corpus was 10.4%.** A single scanner does not have a lower
error rate than that — it has an **unmeasurable** one.

🟢 **The practical consequence.** Licence verdicts on an open-source education stack should be
produced by **two independent readers with the right to disagree**, and the disagreements
**published rather than resolved by precedence**. That is cheap — the second reader can be a
different open-source classifier — and it converts an unknown error rate into a list of named
rows. In a procurement conversation, *"these ten rows are contested and here is why"* is a
defensible position; a single green dashboard is not.

## 69. The licence name and the licence grant come apart in one nameable place: the title block

Trend 23 recorded that *the licence label and the licence grant have come apart, and reading
the payload is no longer enough*. This pass located **where**, across five independent defect
classes that all reduce to one mechanism.

🔴 **A licence body contains the vocabulary of other licences, by construction:**

| Payload | Names, in its own body | Consequence if read as a body |
|---|---|---|
| GPL-2.0 and GPL-3.0 | *"use the **GNU Lesser General Public License** instead of this License"* (closing recommendation) | 8 GPL repositories read as LGPL |
| MPL-2.0 | §1.12 defines *"Secondary License"* by naming **GPL-2.0, LGPL-2.1, AGPL-3.0** | 5 MPL repositories read as GPL |
| GPL-3.0 | §13 is titled *"Use with the **GNU Affero** General Public License"* | GPL-3.0 read as AGPL-3.0 |
| EUPL-1.2 | its Appendix lists **GPL, AGPL, MPL, EPL, CeCILL, CDDL** as compatible | an EUPL payload claimable by five other families |
| a mixed `LICENSE` | *"`docs/` is CC BY-SA … content outside is MIT"* | a permissive repository read as ShareAlike |

🟢 **So the rule that survives all five is about evidence class, not vocabulary: a licence
NAME identifies only where it is a TITLE; a GRANT PHRASE identifies wherever it appears.**

⚠️ **And "title" cannot be implemented as a window.** Three attempts this pass used a
character window (200) or a line window (6); all three failed, one by making a GPL-3.0 fixture
answer `AGPL-3.0`. The concurrent pass hit the same wall independently and wrote the same
conclusion. **A window is a bet on the file's layout. A title is the first one or two
non-blank lines.**

🔴 **The container case is the trap, and it is new.** A licence shipped as **RTF, PDF or any
markup** puts markup in the title block. Every family probe then declines, the payload falls
to `UNCLASSIFIED`, and — critically — **an unclassified family is exactly the state in which
most tools fall back to token-matching the body.** Measured consequence: GPL-2.0 §3(c)'s
*"this alternative is allowed only for noncommercial distribution"* — a condition on one
distribution option — turned a real SIS platform into a *commercial-use prohibited* row.
**The guarantee was in place and the container walked around it.**

🟢 **Two concrete rules for an engagement.** First, **a licence delivered only as RTF or PDF
is a due-diligence finding in itself** — ask for plain text, because every scanner on both
sides of the table is guessing at it. Second, **check whether the grant is at the root at
all**: two platforms on this shelf have no root licence and are findable only at
`docs/License.txt`, so a client's root-only procurement scan reports a correctly-licensed
GPL-2.0 platform as unlicensed.

## 70. An AI-curriculum repository is not an AI-education product, and the market's biggest numbers are the former

🔴 **The mandatory query set for *"open source AI agents education"* produced three
repositories this pass after seventeen empty passes — and all three teach *about* AI rather
than doing anything in a school:**
[`awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) (Apache-2.0,
**140,891★**), [`Made-With-ML`](https://github.com/GokuMohandas/Made-With-ML) (MIT, 49,696★),
[`Hands-On-Large-Language-Models`](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
(Apache-2.0, 29,517★).

🔵 **The star counts are the point.** The largest of them has **140,891 stars** — more than
every education-sector agent on this shelf combined, by a wide margin. The most-starred
*tutoring* asset this KB has ever recorded is in the tens of thousands, and most of the
shelf sits at 0–600. **A naive popularity ranking of "AI + education" open source returns
developer curricula, not education software**, which is why this KB shelves them on the
enablement tier and says so in the row.

⚠️ **For a studio this is a scoping hazard with a specific shape.** A client who has done
their own GitHub research arrives having seen these repositories and reasonably concludes the
open-source education space is enormous and mature. It is not: the *enablement* space is
enormous and mature, and the *product* space is thin, young and mostly copyleft. **Setting
that expectation in week one is cheaper than discovering it in week six.**

🟢 **And they are genuinely valuable, for exactly one thing.** All three are Apache-2.0 or
MIT, so the training materials can be forked, rebranded and **left with the client** — the
difference between enablement and a course licence. ⚠️ Two of the three have not been pushed
in five to seven months, which for a book's companion repository is correct behaviour and
still the difference between *"fork it"* and *"follow it"*.

## 71. A licence claim has a SUBJECT, and an instrument that reads cells without one counts the corpus's corrections as the corpus's contradictions

**Measured, thirtieth pass of 2026-10-07.** Pass 28's `p449` reconciler abstained on **29 rows**
it described as *"the corpus says two things."* 🔴 **Adjudicated first-hand: 14 of 29, and 0 are
contradictions.** The corpus says **one thing about two subjects**, and nine distinct shapes do it:
a named successor (`rhasspy/piper` → `OHF-Voice/piper1-gpl`), a dependency (`kolibri`'s two LGPL
deps), an either/or alternative (Fairlearn **or** AIF360), an ancestor licence (ECL-2.0 *is*
Apache-2.0), a documentation layer (`LICENSE-docs` = CC BY 4.0), an in-tree/side-car boundary
(`moodle-mcp-server` is MIT *because* Moodle's tree is GPL-3.0), the **`Was` column of a correction
table**, a family inside a **refutation marker** (*"AGPL-3.0, **not MIT**"*), and a family inside a
**`license:` search filter**.

🔴 **The two that invert the instrument are the transferable part.** `CORRECTION-TRAIL` and
`QUOTED-REFUTATION` mean the gate reads a correction as a claim and a refutation as an assertion. A
corpus whose method is publishing corrections therefore **manufactures a fresh contradiction with
every correction it makes** — pass 28's five correct `GPL → MPL-2.0` fixes created four abstentions
in the act of landing. ⚠️ **An instrument that degrades as the corpus improves will read as a
worsening corpus**, and nothing in the figure itself distinguishes the two.

🔴 **And a tenth shape that is not a subject error, which is why it is the expensive one.**
`Llamacha/IWSLT2023_Quechua_data` is filed `CC-BY`; this KB's prose says **CC BY-NC-ND 3.0**, in five
places, each with a scope-conflict warning. **The qualifier was normalised away, and that inverts the
commercial answer** — `CC-BY` permits commercial use and derivatives, `CC BY-NC-ND` forbids both. 🔵
**A subject error files a true statement against the wrong repository; a stripped qualifier files a
false statement against the right one.** The second is the one that reaches a client deliverable,
which is why `compose/patterns.md` gains **`P22` check 4** this pass rather than waiting for pass 28's
action-D sweep to become runnable.

🔵 **The cheap rule:** before an instrument binds an attribute to an entity, it must answer *is this
entity what the sentence is about?* and *did the label keep its qualifier?* Three exclusions get most
of the first — the `Was` column of a correction table, any value inside a refutation marker, and any
value inside a query expression — and the second needs only that the **full licence string** be
carried instead of a normalised family. **Consequence for this KB:** the standing prose-vs-data record
moves to **32 of 33** in favour of the sentence a human wrote, and the reason is now explicit — prose
carries the *scope* (`deps`, `docs`, `in-tree`, `README`) and the *qualifier* (`NC`, `ND`) that the
TSV has no column for.

⚠️ **Scope:** 14 of 29 adjudicated first-hand; 3 presumed `CORRECTION-TRAIL` by signature
(`edrys`, `coqui-ai-tts`, `ocrmypdf`); 12 unexamined. Execution of this tree's suites was **denied**
this pass, so this is a reading and not a re-measurement (`P107`).

## 72. 🔴 Two runs of one hourly schedule collide on sequence numbers, and this file already carries the collision in its own headings

**Found while numbering this trend, twenty-ninth pass of 2026-10-07.** This file has **two `## 64.`
and two `## 65.`** — passes 27 and 28 ran concurrently on 2026-10-07, neither could see the other,
and both claimed the next two numbers:

| Number | One claimant | The other |
|---|---|---|
| **64** | *"the prose wins 18 times out of 19"* (pass 28) | *"this KB has two licence classifiers and the hardened one is not the one its instruments call"* (pass 27) |
| **65** | *"a truncation window is a sampling decision"* (pass 28) | *"every leg of a measured chain is a parameter, and an unstated one here is worth 3.4×"* (pass 27) |

🔴 **Why it is a defect and not an untidiness: `trend-backlink-audit` resolves a citation by its
number.** Every citation of "trend 64" or "trend 65" in this KB is now **ambiguous between two
unrelated findings**, and the audit cannot detect it, because each number does have a section — it has
two. The gate checks existence, not uniqueness.

🔴 **And the census, measured on `HEAD` after the merge rather than assumed, is far worse than the
pair that prompted this trend: 83 numbered headings carry only 72 distinct numbers — 11 excess.**

| Number | Claimants |
|---|---|
| **34** | 🔴 **three** |
| 33, 35, 36, 37, 38, 39, 40 | two each |
| 64, 65 | two each — the pair this trend was opened for |

⚠️ **So the 64/65 collision was not the first instance, it was the ninth and tenth**, and the 33–40
block means **eight consecutive numbers** were duplicated at some earlier point without anything
flagging it. 🔵 **A citation of "trend 34" in this corpus is ambiguous three ways**, and no
instrument in this tree can currently say so, because the only question asked of a trend number is
whether a section exists for it. **The invocation that produced this table is
`grep -o "^## [0-9]\+\." intel/trends.md | sort -n | uniq -c`** — the whole defect was one `uniq -c`
away from visible for however many passes it has been live.

🔵 **The structural point, which generalises past this repository:** a monotonic counter is **not** a
safe identifier under concurrency, and an append-only file makes the collision invisible, because both
writers appended successfully and neither diff conflicted. The pre-reset lineage hit the same class
from the other side — pass 27 was *renumbered to 28* at merge time, which preserved the sequence by
rewriting an identifier other sections may already have cited.

⚠️ **The 64/65 pair is left in place deliberately, not silently renumbered.** Renumbering them now
would break whichever citations already point at the current headings, and this pass cannot run
`trend-backlink-audit` to find out which (execution denied). 🔵 **Pre-registered for pass 31:** give
that audit a **uniqueness** assertion alongside its existence assertion, enumerate the citations of
64 and 65, and only then renumber — lowest-risk direction first.

🔴 **And this trend caught itself in the act, which is the strongest evidence it could have had.**
It was drafted as **69**, with its companion as **68**, by a run that had read the file and found 67
to be the highest number. **While it was being written, the concurrently-running pass 29 published
68, 69 and 70.** Both runs read the same file, both computed the same next number, and neither was
wrong at the time it looked. The collision was caught **only because the merge forced a human-style
re-read** — and it was then resolved by renumbering this pair to **71** and **72**, after pass 29's
block rather than on top of it. 🔵 **So the count for this file is now: ten numbers surviving as duplicates (33–40, 64, 65), one
collision avoided (68, 69) — and the one avoided was avoided by luck of merge order, not by any
control.** A uniqueness assertion would have caught all eleven; `git` caught none of them, because
appending to different offsets of the same file is not a textual conflict.

⚠️ **The same class is live in `compose/patterns.md` and is not fixed here either. Measured:
48 pattern headings, 37 distinct numbers.** 🔵 **Two of the repeats are the intentional convention
and must not be counted as defects** — `P1` and `P22` each appear twice because a later pass
published a dated *`… update`* section under the original number, which is this KB's way of amending
a pattern in place. 🔴 **The remaining six are genuine collisions, where unrelated patterns share one
identifier:** `P25` ×3, `P26` ×3, `P28` ×3, `P27` ×2, `P29` ×2, `P30` ×2. Pattern numbers are cited
across this KB exactly as trend numbers are, so **that file needs the same uniqueness assertion —
with an exemption for the `update` form**, or the gate will condemn the one convention that is
working.
🔵 **Pre-registered for pass 31 alongside the audit change:** publish the duplicate census for both
files before renumbering anything, because the census is what tells you which direction is safe.

## Trends — thirty-first pass, 2026-10-07

### T-31.1 — The market has stopped buying "personalisation" and started buying workflows

2026's clearest shift is **away from generic AI tools toward platforms purpose-built for education**,
and within those, toward **workflow-first** applications: course-design support, teacher
productivity, instructional and administrative workflow automation, structured student-support tasks.
Broad personalisation promises are being displaced by *proven instructional benefit*.
**Consequence for engagements:** scope the admin and teacher-facing workflow first. It is where the
evidence is, and — per UNESCO's confidence tiers — where regulatory risk is lowest.

### T-31.2 — Governance has become the product, not the paperwork

Across all four regions, AI in education is moving **from experimentation to governance**: clear
policies, data boundaries, oversight. This is now a deliverable line item rather than a compliance
afterthought — explicitly so in EMEA (EU AI Act enforcement from **2 Aug 2026**, education as a
high-risk domain), in North America (**134 bills / 31 states**; **CA AB 1159** barring student data
from model training; **OK/MD** human-oversight and no-high-stakes-decision rules), and in APAC
(**Korea Framework Act** 22 Jan 2026, **Vietnam** 1 Mar 2026, **Taiwan AI Basic Act** Dec 2025, with
automated assessment and behavioural monitoring named high-risk).

### T-31.3 — "Human must dispose" is now a design constraint with statutory force

Oklahoma and Maryland **ban AI from making high-stakes decisions about students** and require human
oversight; the EU AI Act attaches human-oversight obligations to the same class of systems; Korea and
Japan add education-specific data-protection duties. **An autograder that writes a final grade is
non-compliant in a growing number of jurisdictions.** The compliant shape is *propose-and-review*:
model output as a reviewable suggestion, with the human action logged. Notably,
`pawtograder/platform` already separates CI autograding from **rubric-based handgrading**, which is
this shape arrived at for pedagogical reasons before the statutes required it.

### T-31.4 — Memory and persistent learner state are the live technical frontier

The broader agent ecosystem's recognition that **stateless agents are unsuitable for production** has
landed in education as *durable learner state*: review scheduling, session memory, misconception
tracking, metacognition, auditable pedagogical decisions. `ArnaudGuiovanna/tutor-mcp` (MIT, canonical
— see the fork note in `agents/trending.md`) is the clearest MCP-shaped expression of it, and
`pawtograder/platform` is the clearest production expression of **course state exposed to staff-side
LLMs over MCP**. ⚠️ Persistent learner state is also precisely what **CA AB 1159** and the Korean
EdTech privacy rules constrain — *store it, do not train on it.*

### T-31.5 — The open-source growth this window is in curriculum, not classroom runtimes

Four of the five highest-signal repos this window are **books and courses**
(`rasbt/LLMs-from-scratch`, `rohitg00/ai-engineering-from-scratch`, `bojieli/ai-agent-book`,
`datawhalechina/hello-agents`). Deployable, permissively-licensed classroom *runtimes* grew far more
slowly. **Read:** for a 2026 engagement, expect to **compose and build** the runtime on an existing
LMS core; do not expect to adopt a finished open-source AI classroom.

### T-31.6 — Licence shape, not capability, is the gating factor in education open source

Of six repos verified this pass, **two are buildable** (MIT, Apache-2.0), two are **GPL-3.0-or-later**,
one is **CC BY-NC-SA 4.0**, one has **no licence file at all**. The sector's institutional and
public-sector origins mean copyleft and NonCommercial grants are over-represented relative to general
AI tooling. **The strategic implication is concrete:** prefer **MIT Sunbird/DIKSHA** as an LMS base
over **GPL-3.0 Moodle** where a proprietary AI layer must be redistributed, and keep the MCP
side-car boundary (already pattern `P-moodle-mcp` on this shelf) when working against a GPL tree.

### 🔵 Declared gaps for this pass

- **LATAM-origin and EMEA-origin open-source education repos: none new found**, searched in Spanish
  and Portuguese and against region-specific queries. See `agents/trending.md` 2026-10-07 for probed
  slugs and their 404s.
- **Latam-GPT has no located repository** — licence and composability unverified; press coverage is
  not a licence.
- **No star counts read this pass** (`api.github.com` 403, session-scoped). The single star figure
  carried in `repos/trending.md` is explicitly marked second-hand.
