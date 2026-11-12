---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p799` — **Ten instrument defects in one pass, every one caught before publication and none shipped. 🔴 Five of the ten are ONE class this base has now met four times: a region or licence token that is a SUBSTRING of ordinary text. 🟢 The class is cheap to defeat and expensive to miss, and `p799` publishes the rule rather than another screen.**

🟢 Machine output: [`instrument-defect-cycles`](../evidence/instrument-defect-cycles.2026-11-12-p799.tsv) · [`mit-clause-identity-population`](../evidence/mit-clause-identity-population.2026-11-12-p799.tsv) · [`channel-reprobe`](../evidence/channel-reprobe.2026-11-12-p799.tsv).

### 🔴 `T944` — an ACRONYM region-token is a substring of ordinary words, and it produces right answers for wrong reasons

🔴 **Two measured instances, from one run:**

| Grade produced | Token that produced it | Where it actually occurred | Truth |
|---|---|---|---|
| 🔴 `LATAM` on [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) | **`ENEM`** (Brazil's national exam) | 🔴 **inside the ordinary Spanish word `tenemos`** | 🟢 **EMEA** — Madrid, Galicia, Andalucía, LOMLOE |
| 🟡 `LATAM` on [`communityrbh-hub/rebuild-choco`](https://github.com/communityrbh-hub/rebuild-choco) | **`INEP`** (Brazil's education research institute) | 🔴 **inside a camelCase identifier, `...lineP...`** | 🟢 **LATAM 🇨🇴** — correct grade, **provably wrong reason** |

🔴 **The second row is the dangerous one.** 🟢 **It is right.** 🔴 **It is right by accident, and nothing in the artefact said so** — a reviewer checking the grade would have confirmed it and moved on, and the instrument would have kept its false mechanism.

🔵 **This base has now met the class four times:** `p796-G`'s `icon` inside *semiconductor*; its own `ESO` inside the tails of *proceso* and *peso*; and `ENEM`/`INEP` here. 🟢 **`p799`'s rule, and it is two cheap requirements rather than a cleverer predicate:** 🟢 **(1) match an acronym CASE-SENSITIVELY with word boundaries; (2) make the verdict CARRY the token that produced it, so a grade is re-derivable from the bytes beside it.** 🔵 **Requirement (2) is what turned `rebuild-choco` from a silent pass into a caught defect, and it is [`p796-H`](open-gaps.md)/`p797-C`'s standing demand satisfied at the point of writing instead of in a later audit.**

### 🔴 `T945` — a bare ccTLD is unusable against any document that contains file paths

🔴 **`Paraguay`'s ccTLD is `.py`. 🔴 The Python file extension is `.py`.** 🔴 **A Spanish-only payload graded `CONFLICT:EMEA=.es/LATAM=.py` off its own source listing.**

🔴 **The collision is systematic, not a one-off:**

| ccTLD | Country | Also | 
|---|---|---|
| `.py` | Paraguay | 🔴 **Python source** |
| `.cl` | Chile | 🔴 **OpenCL kernels** |
| `.es` | Spain | 🔴 **ECMAScript modules** |
| `.do` | Dominican Republic | 🔴 **JSP actions** |
| `.ar` | Argentina | 🔴 **archive files** |
| `.pl` | Poland | 🔴 **Perl** |

🟢 **Fix, and it is a restriction rather than an addition: a ccTLD counts only inside a URL HOST.** 🟢 That is what preserved 🇻🇪 Venezuela's `mppe.gob.ve` and 🇦🇷 Argentina's `.net.ar` while removing `.py`.

### 🔴 `T946` — a bare COUNTRY NAME is not origin evidence either, because i18n lists name countries

🔴 **[`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — Tsinghua University — graded `LATAM:brazil`.** 🔴 **The single occurrence is `README.md` line `887`, an interface-locale list:** *"`12` locales across `11` languages: … **Portuguese (Brazil), Spanish (Mexico)** …"*.

🟢 **So the origin channels rank, and `p799` publishes the ranking:**

| Rank | Channel | Strength |
|---|---|---|
| 🟢 **1** | **Government/ministry document at a URL host** (`mppe.gob.ve`) | 🟢 decisive — a curriculum cited to a ministry is origin |
| 🟢 **2** | **Institutional affiliation in `NOTICE`/description** (UPM Madrid; `PIVIC / UniRV`) | 🟢 strong |
| 🟢 **3** | **ccTLD inside a URL host** | 🟢 strong |
| 🟡 **4** | **Subnational territory name** (Andalucía, Galicia) | 🟡 good for EMEA; excludes names shared across regions — *Valencia* is also a city in Venezuela |
| 🟡 **5** | 🆕 **the repository DESCRIPTION on `search/*`** | 🟡 **resolved 🇵🇪 Peru where the payload could not** — and `p798-A` never named it |
| 🔴 **6** | **Bare country name in prose** | 🔴 **contaminated by i18n locale lists — never sufficient alone** |
| 🔴 **7** | **Commit author identity** | 🔴 **`5` of `5` were `gmail.com` or `users.noreply.github.com`. Useless for origin** |

### 🔴 `T951` — and the class is not only acronyms: `universidade` is Galician AND Portuguese

🟢 **[`nmarafo/open-lex-edu`](https://github.com/nmarafo/open-lex-edu), verified this pass at `2,874 B` / HEAD `5ad542282c8f`, returned `CONFLICT:EMEA=xunta/LATAM=universidade`.** 🟢 **`Xunta` (de Galicia) resolves it EMEA.** 🔵 **But the lesson is that a whole WORD can be regionally ambiguous, not just a four-letter acronym — `universidade` is correct Galician orthography and correct Portuguese simultaneously.** 🔴 **This pass's [`RowanFalcao/inclusign-ai`](https://github.com/RowanFalcao/inclusign-ai) placement rests on `universidade` plus a corroborating description (`PIVIC / UniRV`); on the token alone it was a coin-flip between Galicia and Brazil.** 🟢 **Which is the argument for the CONFLICT state itself: a two-state verdict would have picked one and published it.**

### 🔴 `T947` — a defect this base NAMED at `p214` recurred in a brand-new instrument `~585` passes later

🔴 **This pass's own classifier read [`Ignacio-Ghub/asistente-docente-sin-conexion`](https://github.com/Ignacio-Ghub/asistente-docente-sin-conexion) as `AGPL-3.0` where `p798` had read `GPL-3.0`.** 🟢 **`p798` was right.** 🔴 **The payload's title line is `GNU GENERAL PUBLIC LICENSE / Version 3, 29 June 2007`; the string `GNU Affero` appears further down, in section `13`, *"Use with the GNU Affero General Public License."***

🔴 **And `p799` claims NO novelty here, because this base already owns the finding.** 🔴 **`p214` recorded it in these exact terms:** *"the mechanism is now named: `GPL-3.0` §`13` is titled **'Use with the GNU Affero General Public License'** and the blob says `Affero` `3` times, so a whole-body matcher flips the family."* 🔴 **`8` of `518` repositories printed two grants there, all `8` on the GNU axis.**

🔵 **So the finding is NOT the mechanism. It is that a correctly diagnosed, correctly written-down defect was reproduced from scratch by a new instrument `~585` passes later, because the knowledge lived in a PROSE LEDGER and not in a shared classifier.** 🟢 **`T938` said an instrument library can regress by ADDING something; 🆕 this says a KNOWLEDGE base can regress by writing something down and nowhere else.** 🔴 **`p798-B`'s shape too — "the instrument existed, was built pre-reset, and has never been run."**

🟢 **Fix applied here: classify on the TITLE — the first five lines — never on the body.** 🟢 **Fix the next pass owes: ONE licence classifier, shared, with `p214`'s GNU-axis case and this pass's title rule as its controls, so the third re-discovery costs nothing** → `p799-H`. 🔵 **The defect is silent and it inverts a COPYLEFT REACH judgement — AGPL network-use obligations are precisely what a studio must not get wrong in a hosted-tutor deliverable, which is why it has now been worth finding twice.**

### 🟢 `T948` — `ACTION p798-C` discharged: `p795-A`'s byte band is retired, and it was biased by NAME LENGTH

🟢 **`p135`'s normalisation re-implemented in this pass's own command, because executing committed repository code is refused here (`p797-H`, sixth pass).** 🟢 **`8` MIT payloads, copyright notices removed as spans, whitespace collapsed, then hashed:**

| Measure | Result |
|---|---|
| Raw byte spread | 🔴 **`1,061` → `1,250 B`** (`189 B`) |
| 🟢 **Distinct normalised clause hashes** | 🟢 **`1` — `745e05f91f85`, on all `8`** |
| 🟢 **Normalised clause bytes** | 🟢 **`1,032 B`, identical on all `8`** |
| 🔴 **`p795-A` band verdict (`1,066`–`1,072 B`)** | 🔴 **`5` of `8` flagged OUTLIER — a `62.5%` false-alarm rate on byte-identical grants** |

🔴 **And the mechanism is not neutral. The whole `189`-byte spread is the copyright LINE, so the false-alarm rate rises with the length of the holder's NAME:**

| Holder line | Bytes | Band verdict |
|---|---|---|
| `Copyright (c) 2026 XAIHT` | `1,062` | 🔴 OUTLIER |
| `Copyright (c) 2026 jeffercbs` | `1,066` | 🟢 inside |
| `Copyright (c) 2026 Lucas Mendes` | `1,069` | 🟢 inside |
| `Copyright (c) 2026 Leandro Aguilar` | `1,072` | 🟢 inside |
| `Copyright (c) 2026 Dirk Hans Krakaur Florane…` | `1,083` | 🔴 OUTLIER |
| `Copyright (c) 2026 Rowan Falcão Rodrigues L…` | 🔴 **`1,252`** | 🔴 OUTLIER |

🔴 **Spanish and Portuguese naming convention carries two surnames. A screen keyed on licence-file LENGTH therefore flags Iberian and LATAM authors' MIT grants as anomalous at a higher rate than Anglo single-surname authors' — for a reason that has nothing to do with the grant.** 🔵 **That is a regional bias inside an instrument this base built to do regional work, and it is `p798-G`'s caution — measure a rate where it should NOT hold — applied to the base's own shelf.** 🟢 **`p795-A`'s band is RETIRED as a grading screen; the normalised clause hash replaces it.**

## 🆕 `p798` — `T935`–`T941`

🔵 **The pass's through-line: four of these seven are about an instrument being pointed at the wrong unit** — a region inferred from a query language, a rider inferred from a byte count, a restriction looked for in a licence file, a supply gap diagnosed from five rows with no denominator. 🟢 **Each one was caught by adding a CONTROL, and in two cases the control already existed in this repository and had stopped being used.**

## `T935` — a query language is not a region, and this base has been treating it as one

🔴 **`p797` ran `es` and `pt` discovery legs and labelled every find "LATAM-origin". `p798` opened the payloads: [`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia)'s `NOTICE` names *Universidad Politécnica de Madrid*, and [`ANFAIA/SkillNet`](https://github.com/ANFAIA/SkillNet) publishes from `skillnet.es`.** 🟢 **Both are EMEA. Both were counted as LATAM evidence.**

🔴 **And origin is not resolvable in bulk from this session: `gh api users/{login}` is refused** (*"sessions are bound to their configured repositories"*), so the `location` field that would settle it is unreachable. 🟢 **The only reliable origin signals left are inside the payload — a `NOTICE` naming a funder, a `.es`/`.br` domain in the README, a country-specific curriculum reference.** 🔵 **That is a per-row read, not a census column.**

🟢 **The rule: a row placed by the language of the query that found it is placed on an inference, and the closed region vocabulary cannot express an inference.** 🟢 **`p798` therefore writes `LATAM?` where the evidence is a query language and nothing else** — 🔵 **the first time this base has published a placement it is not sure of rather than choosing a bucket.** 🔴 **Spain and Portugal will keep arriving on the LATAM leg, and Gulf states on the APAC leg** (the UAE's `25` school prohibitions did exactly that this pass) → `p798-A`.

## `T936` — an author wrote the content carve-out this base has been asking for, in `571` bytes

🟢 **[`danielgalanv/oral-ia`](https://github.com/danielgalanv/oral-ia) (Apache-2.0 · `11,358 B` · blob `57bc88a15a0e` · HEAD `c5e433674702`) ships a `571 B` `NOTICE` stating that the grant covers the code, tests, specifications and its own documentation, and does NOT cover the teaching material, the third-party document texts used in the pilot, or the language models — each keeping its own holders' conditions.**

🔴 **`T916` established why this matters: on code/content splits GitHub's classifier reports the CODE licence and silently drops the CONTENT licence, and in education the content licence is the one that governs the curriculum.** 🟢 **Here the author pre-empted it without being asked, under a university pilot grant.**

🔵 **The trend worth naming is not a licensing fashion — one row is not a fashion. It is that the four-layer boundary (platform code · studio code · client curriculum · model weights) is becoming visible to the people writing the code, not just to the people reviewing it.** 🟢 **And it converts directly into a deliverable: four sentences, reusable, cheaper than the argument it prevents** → [`compose/patterns.md`](../compose/patterns.md) `P798-2`.

## `T937` — the fourth place a restriction hides: the README, under an unmodified grant

🔴 **The locations this base has now recorded: a second licence FILE (`T914`), a different REPOSITORY (`T925`), inside a single file as a second grant (`T915`) — and now the README.**

🔴 **[`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) (MIT · `1,062 B` · blob `6d93cdbdf7d0`, ★`15`, pushed `2026-11-12`) carries a byte-canonical MIT grant and an HTML comment in its README: *"Tlamatini Author Banner — do not remove (Angela's name is kept in every build)."*** 🔴 **MIT requires the copyright notice to survive in copies of the software; it does not require a banner to survive in every BUILD, and it expressly grants the right to modify.**

🟡 **Not a refusal — an MIT grant is an MIT grant — but a row where the licence and the author's stated expectation are different documents, and the README is the one a contributor reads.** 🔵 **For a client deliverable that strips author banners as a matter of course, this is the difference between a compliance question and a relationship question, and it is settled in one message before the fork, not after the launch.** 🟢 **This base already owns the instrument: [`compose/code/p1060-readme-vs-payload/`](../compose/code/p1060-readme-vs-payload/), built pre-reset, never pointed at the current shelf** → `p798-B`.

## `T938` — a byte-size band is a proxy for an exact instrument this base built and stopped using

🔴 **`p795-A` screens MIT grades by byte size against a canonical `1,066`–`1,072 B` band. Four MIT payloads this pass span `1,062`–`1,096 B` with BYTE-IDENTICAL clause text** (md5 `aeb812008e99` with the copyright line removed). 🔴 **The `34`-byte spread is the holder's name: `jeffercbs` against `Scientific Learning Skills Contributors`. `3` of `4` clean rows flagged, and the flag rate rises with name length.**

🟢 **[`compose/code/p135-licence-sha-identity/`](../compose/code/p135-licence-sha-identity/) says it outright in its README** — *"every real MIT file carries a copyright line the SPDX template leaves as a placeholder, so a real MIT payload NEVER hashes to the canonical MIT text"* — **and its `body` level removes copyright notices as spans, reporting `TEMPLATE_MATCH`, with `MODIFIED_SUPERSET` for the `MIT + visible-attribution` rider class `p795-A` exists to catch.**

🔵 **The general lesson, and it is about this base rather than about licences: an instrument library of this size can regress by ADDING something.** 🔴 **`p795-A` did not replace a worse method; it replaced a better one that was `660` passes old and out of sight.** 🟢 **Before building a screen, grep the library for the measurement it approximates** → `p798-C`. 🔴 **Declared: `p135` was read, not run — executing committed repository code is refused in this session.**

## `T939` — an instrument number survived a direct challenge, which is what makes `CITED, NOT READ` usable

🟢 **`p795-F` published `Regulation (EU) 2026/1744` from a single reading and labelled it `CITED, NOT READ`. This pass's EMEA leg challenged the number explicitly.** 🟢 **Re-run deep: four independent legal-practice readings name the same regulation and agree on OJ publication `2026-07-24`, entry into force `2026-07-27`, Annex III standalone high-risk (education) `2027-12-02`, Annex I `2028-08-02`, and that Art. `50` transparency was NOT deferred.** 🟡 Residual disagreement on adoption/signature dates, immaterial to a contract.

🔵 **The method claim is now tested rather than asserted: a numbered instrument is checkable by anyone in one lookup, so publishing the number while unable to open the text is honest and useful.** 🔴 **`eur-lex.europa.eu` has still never resolved from this session, and `T906` now names TEN refused government and multilateral domains after Korea's ministry was added this pass.** 🟢 **No commercial domain has ever failed this way — which is why it is a network policy and not an outage.**

## `T940` — the in-language supply has a ceiling of `5` stars, and that is a different problem from the one `p797` diagnosed

🔴 **`p797`: `5` of `5` LATAM-origin agents serve no grant → the constraint is grant hygiene.** 🟢 **`p798`, with a denominator and a control leg:**

| | 🇪🇸🇧🇷 `es`/`pt` | 🌍 `en` | Ratio |
|---|---|---|---|
| Addresses | `73` | `149` | — |
| No licence file | `78.1%` | `60.4%` | 🟡 `1.29×` |
| 🔴 **Zero stars** | 🔴 **`94.5%`** | `19.5%` | 🔴 **`4.8×`** |
| 🔴 **Population maximum** | 🔴 **`5` ★** | `4,912` ★ | 🔴 **`982×`** |
| Rows at `≥20` ★ | 🔴 **`0`** | `16` | — |

🔵 **Both numbers are real and they point at different actions.** 🟢 **Ungranted is the DEFAULT for a young repository in any language, so grant hygiene is an intake rule, not a regional programme.** 🔴 **What is specific to the in-language population is that none of it has been adopted by anyone — a new project appears almost daily and nothing accumulates.**

🟢 **The engagement consequence, stated plainly because it reverses advice this base gave nine days ago: do not shop for an in-language base and do not run a licensing campaign to unlock one. Take a global permissive base, localise it, and read the in-language repositories as DESIGN EVIDENCE.** 🔵 **They are worth reading *because* nobody starred them — they show what a regional teacher builds with no audience: [`asistente-docente-sin-conexion`](https://github.com/Ignacio-Ghub/asistente-docente-sin-conexion) runs with no internet; [`miyagi`](https://github.com/falkenslab/miyagi) attaches to Moodle and asks before anything reaches a student; [`chispa-mcp`](https://github.com/jeffercbs/chispa-mcp) exposes classroom management at the teacher's own permissions; `p797`'s [`miguelito`](https://github.com/alesdrobysh/miguelito) delivers a tutor over Telegram twice a day.** 🟢 **Offline-first, LMS-attached, messaging-delivered, teacher-gated — that is a requirements document, and it came from repositories with zero stars.**

## `T941` — in a session scoped to one repository, `search/*` is the whole metadata channel

🔴 **Measured this pass: `gh api repos/{owner}/{repo}` and `gh api users/{login}` are both REFUSED, while `gh api search/repositories` returns `license.spdx_id`, `stargazers_count`, `pushed_at` and `archived` normally, and `git clone --filter=blob:none` works on any public address.**

🔴 **It cost an artefact before it was noticed: [`candidate-grant-bytes-UNCORRECTED-v1`](../evidence/candidate-grant-bytes-UNCORRECTED-v1.2026-11-12-p798.tsv) carries a JSON error blob in its `archived` and `pushed` columns on all `16` rows, because the instrument called `repos/{owner}/{repo}` per row.** 🟢 **Corrected by dropping the two columns and naming the recency channel in the row; both versions published so the correction is re-derivable.**

🔵 **The failure mode worth remembering: a refused API call returns a `200`-shaped JSON body, so it lands in a TSV cell as text and looks like data.** 🟢 **It is `T923`'s class — a uniform non-silent answer that reads as a measurement — and the defence is the same: assert the shape of a cell you are about to publish, because an error message is a string and a string fits anywhere.** 🟢 **`p797` wired `gate-evidence-address` into `make hooks` for exactly this kind of published-artefact defect; it checks addresses, not cell shapes** → `p798-E`.

## 🆕 `p797` — `T924`–`T934`

### 🔴 `T924` — the brand layer is not an exception on the platform shelf, it is a structural feature of it: `6` of `37` addresses, and two of the `6` are the two most-deployed systems in this industry

🟢 **`p796` found `3` of `3` on rows chosen for being RECOMMENDED and called that the argument for a standing gate. `p797` ran the gate over `37` platform addresses and `54` candidate licence files: `6` bespoke brand restrictions.** 🔴 **The two new ones are [`moodle/moodle`](https://github.com/moodle/moodle) (`TRADEMARK.txt`, `3,367 B`: *"the GNU GPL does not include an implied right or licence to use Moodle's trade marks"*) and [`frappe/erpnext`](https://github.com/frappe/erpnext) (`TRADEMARK_POLICY.md`, `3,020 B`: permission only where *"your project is non-commercial in nature"*), plus [`ankitects/anki`](https://github.com/ankitects/anki), whose logo licence requires the mark be used **unmodified**.** 🔵 **The generalisation: in this industry the permissive-or-copyleft question governs the CODE, and a second, differently-licensed layer governs the thing the client actually wants — their own name on the product.** 🟢 **Grading the root `LICENSE` finds none of the six.**

### 🆕 🔴 `T925` — the restriction can live in a different REPOSITORY, and no per-address sweep can see it

🔴 **[`frappe/education`](https://github.com/frappe/education) and [`frappe/lms`](https://github.com/frappe/lms) carry no brand instrument. The policy that binds their brand is in `frappe/erpnext`.** 🔵 **`T914` moved the unit of analysis from the repository to the FILE. `T925` moves it again, to the project FAMILY — and unlike `T914`, this one is invisible to the instrument that found it: `p797`'s sweep enumerates one root tree per address and would report `frappe/education` clean forever.** 🟢 **Rule: a brand clearance names the upstream PROJECT and reads every repository that shares its name.**

### 🔴 `T926` — this base's `12`-hex provenance column is TWO object kinds in one visual position, plus a third that resolves to neither

🟢 **`83` cells across the three recommendation shelves, re-measured against first-hand bytes: `43` are COMMIT shas, `9` are licence-file BLOB shas, `31` resolve to neither today** ([`provenance-cell-kinds`](../evidence/provenance-cell-kinds.2026-11-12-p797.tsv)). 🔵 **`T905` said the column *"is not one hash function"* and `p796-B` concluded it should be deleted. The measurement says otherwise: `52` of `83` resolve, and most of the `31` are an old `HEAD` on a repository that has since been pushed — which is a staleness signal, not an error.** 🔴 **The real defect is AMBIGUITY: a reader must guess the object kind before they can check anything.** 🟢 **Fix adopted: a provenance cell carries its kind (`blob <sha>` / `HEAD <sha>`) or it does not ship. Re-typing the history is mechanical and queued as `p797-B`.**

### 🔴 `T927` — a brand file moved upstream the SAME DAY this base first read it

🔴 **`p796` measured [`ankitects/anki`](https://github.com/ankitects/anki)`:LICENSE` at `1,930 B`. `p797` measures `1,937 B` — and the diff is commit `9c539a036804`, `2026-11-12 16:06:11 -0300`, *"docs: update logo copyright holder in LICENSE"*.** 🔵 **Two passes on one day, and the brand layer changed between them — on the axis the first pass had just made its headline.** 🟢 **Consequence for every byte-size anchor in this base: a size without a commit sha beside it is a snapshot, not a verification.** 🟢 **It also vindicates keeping byte size (it reproduced exactly against an unchanged file on `3` of `3` rows) while typing the sha — the two together are falsifiable, either alone is not.**

### 🔴 `T928` — two defects in one instrument: a vocabulary match with no word boundary, and an object size with no object type

🔴 **v1 of `p797`'s brand gate matched `icon` as a SUBSTRING and reported it on every GPL-3.0 row in the base, because GPL-3.0 §`0` says *"semiconductor masks"* — `17` rows carried a term they do not contain.** 🔴 **The same v1 graded [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai)`:licenses` as a `4,380 B` licence file; `cat-file -s` returns a size for a TREE, and the instrument never asked the type.** 🔵 **Both are the same error in different clothes — asking a question whose answer type is wider than the question assumes.** 🟢 Both published: [`brand-layer-census-UNCORRECTED-v1`](../evidence/brand-layer-census-UNCORRECTED-v1.2026-11-12-p797.tsv).

### 🔴 `T929` — SCOPE, not the predicate, is what bounds a corpus-wide gate: `15,591` → `5,093` → `18`

🔴 **`ACTION p796-E`'s gate over `2,093` evidence files (`2,097` once this pass's own artefacts landed) reported `15,591` offending rows on its first run, where `6` addresses are real. Narrowing the predicate twice got it to `5,093`. Keying it on the DECLARED HEADER — only the `696` files whose column `0` is headed `repo`/`addr`/`slug`/`address` — got it to `18`, which is the truth (`6` addresses × `3` files).** 🔴 **All `21` of v1's controls passed at every step.** 🔵 **`p796-G` says a control set must span the population's kinds; `T929` is the limit of that rule — a control set cannot span kinds its author has not met, and this population held four (a URL in column `0`, a prose sentence in column `0`, a repository name legally ending in `-`, and a file path).** 🟢 **What saved the gate was not a better rule but a smaller, DECLARED scope. Prefer a gate over a column that has promised what it holds.**

### 🔴 `T930` — `p796` graded its own NEGATIVE CONTROL as a defect

🔴 **`p796` reported *"a template placeholder found in a PUBLISHED evidence artefact: the literal row `OWNER/REPO`"*.** 🟢 **Read: `existence-three-state.2026-11-12-p794.tsv:41` is `OWNER/REPO  ABSENT  128  0  0` — the deliberate negative control `p796`'s own README cites approvingly two sections later (*"with a NEGATIVE control that fails as required"*).** 🔴 **And `address-census.2026-11-12-p781.tsv` lines `109`/`625` are not placeholders either: they are COUNTS of how often `owner/repo` (`24`) and `OWNER/REPO` (`6`) occur in this base's own markdown.** 🔵 **The gate `p796` specified — reject `OWNER`, `REPO`, `NEW`, `EXAMPLE` as literals — would have deleted the control and the census.** 🟢 **`47` candidate rows in `24` files; `41` are headers, prose-literal counts or controls; `6` are the real defect, a STATUS MARKER glued onto an address (`NEW/ArnaudGuiovanna/tutor-mcp`), fixed by stripping the prefix rather than deleting rows that carry real measurements.** 🔵 **An instrument that cannot tell a placeholder from a control will delete the control, because the control is the thing that looks wrong on purpose.**

### 🔴 `T931` — the LATAM supply is not missing. It is unlicensed.

🔴 **Five consecutive passes recorded `0` LATAM-origin intake and attributed it to `T883`, the English-query shape. One hour on the `es` and `pt` legs returned five addresses — and `5` of `5` are `NOASSERTION`: no licence file of any kind. None has more than ONE star; three were pushed within six weeks.** 🔵 **This inverts the remedy. A supply gap is answered by discovery; a grant gap is answered by a conversation with a reachable author who has no reason to refuse.** 🟢 **And it re-dates the risk: these are new repositories, so the licence is missing by omission rather than by choice** → [`agents/top.md`](../agents/top.md) `p797`, `P797-1`.

### 🔴 `T932` — Korea is this base's first measured REVERSAL, and it is the strongest evidence against a mandate-led offer

🔴 **`AI 디지털교과서` adoption: `4,095` schools (`34.2%`) in `1H 2025` → `1,481` (`12.5%`) → `622` (`5.2%`) in `1H 2026`, after the August `2025` statutory reclassification from *교과용 도서* to *교육자료* made adoption discretionary.** 🔴 **`94.8%` of schools stopped once nobody made them continue.** 🔵 **Every regional opening in this base is anchored to a compelled document, and `T932` is the limit of that strategy: a compelled deployment survives exactly as long as the compulsion.** 🟢 **It is `T907` restated at national scale — the binding constraint is whether a teacher chooses the thing — and it is why `P797-1` sells an instrument that proves voluntary use rather than a rollout that proves compliance.** 🟢 **What remains is a better-shaped buyer: `1,900` self-selecting lead schools, and AI-subject 인정 교과서 piloting `1H 2027`.**

### 🔴 `T933` — the primary-source channel loses a seventh domain, and this time it holds the pass's headline

🔴 **`www.gov.br` does not resolve from this session, joining `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `op.europa.eu`, `iesalc.unesco.org` and `digital-strategy.ec.europa.eu` (`T906`).** 🔴 **So `Parecer CNE/CP nº 15/2026` — the first compelled AI-in-education deadline in LATAM — is `CITED, NOT READ`.** 🟢 **`p795-F`'s mitigation applies and is the reason this is publishable: name the instrument, not a paraphrase of it.** 🔵 **`p794-F`'s cost is no longer bookkeeping. It is now measured in regulatory deadlines this base can name but not verify.**

### 🆕 🟢 `T934` — a dosage metric that drops the zeros measures the engaged, and the engaged were never the question

🟢 **`ACTION p796-A` built at last ([`compose/code/p797-dosage/`](../compose/code/p797-dosage/)), and its first control caught its first defect: it took the median practice-days over only the students who practised, reading `2.5` where the honest answer is `2`.** 🔴 **The student it dropped had been offered the tutor twice and never took a turn — the population `T907` says dominates.** 🔵 **This is `T916`'s shape on a different axis: when an instrument must summarise a mixed population, the half it silently discards is the half that carries the bad news.** 🟢 **Rule: a dosage denominator is everyone who was OFFERED the thing.**

## 🆕 `p796` — **eight findings. The headline is that on the rows this base recommends for white-labelling, the permissive grant covers the CODE and the BRAND ASSETS are licensed separately and more restrictively — three independent instances, one of them `NoDerivs`. The second headline is that `5` of my own `32` initial multi-grant flags survived, and the controls that certified the instrument could not have caught the error.**

## `T914` — the brand layer is licensed separately from the code layer, and that is where white-labelling dies

🔴 **`T900` found a branding rider on one row and read it as a rider problem. `p796` counted licence FILES across `174` addresses (`p795-B`) and the rider turns out to be one instance of a structural pattern: the repository's permissive grant governs the code, and the logo, icons and embed are carved out separately.** 🔴 **Three independent instances, all on rows this base actively recommends:**

| Row | Published grade | 🔴 What a second licence file actually says |
|---|---|---|
| 🔴 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) `★158,483` | 🟢 `BSD-3-Clause` | 🔴 **Clause `4` of `LICENSE` (`2,819 B`) makes altering or replacing *"Open WebUI" branding* a material breach** (`T900`). 🟢 `p796` adds the third file: `LICENSE_HISTORY` (`2,872 B`) carries **two** grants — MIT *and* BSD — i.e. it is the relicensing record, which is why it grades "clean" |
| 🔴 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) `★451` | 🟢 `Apache-2.0` · `10,982 B` | 🔴 **`NOTICE.TXT` (`14,412 B`) — a file this base had never opened — states: *"The OpenOlat logo and icons … are released under the Creative Commons Attribution-NoDerivs 2.5 license."*** 🔴 **`NoDerivs` on the brand assets of the row this base calls *"the permissive LMS for an EMEA engagement"*** |
| 🔴 [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 `AGPL-3.0` | 🔴 **`4` root licence files, and only `1` contains an OSI grant.** `LICENSE-AGPL.txt` (`37,265 B`) is the AGPL. 🔴 **`LICENSE-EMBEDDING.txt` is `8,877 B` of terms containing NO recognised grant at all**, plus `LICENSE-MCL.txt` (`425 B`) and `LICENSE.txt` (`855 B`) (`T912`) |

🔵 **The commercial statement, and it is the same sentence in all three cases: the licence that lets you ship the software is not the licence that lets you put the client's name on it.** 🟢 **An engagement whose deliverable is a white-labelled platform must grade the brand layer as a separate question, and the brand layer is never in the root `LICENSE`.** 🔵 **Grading the root `LICENSE` alone finds none of these three.**

## `T915` — `p795-B` asked for a licence-FILE count; the unit is the GRANT, and a file count is only a proxy for it

🟢 **`ACTION p795-B` discharged across `174` live addresses in `16` seconds** ([`evidence/licence-file-and-grant-block-census.2026-11-12-p796.tsv`](../evidence/licence-file-and-grant-block-census.2026-11-12-p796.tsv)). 🟢 **Nothing in this base had ever recorded a licence-file count per repository.**

| Root licence files | Rows | |
|---|---|---|
| `0` | 🔴 **`19`** | 🔵 the ungranted-at-root population, already tracked here by other means |
| `1` | `142` | |
| `2` | `10` | |
| `3` | `1` | `open-webui` |
| `4` | `2` | `metabase`, `DSpace` |

🔴 **But a file count is the wrong unit in both directions.** 🟢 **`5` rows carry MORE THAN ONE GRANT, and `3` of the `5` carry them inside a SINGLE file — invisible to any file count:**

| Row | Files | 🔴 Grants actually served | Read |
|---|---|---|---|
| 🔴 [`odoo/odoo`](https://github.com/odoo/odoo) | `1` | 🔴 **`2` — `LGPL-3.0` at line `15`, then the FULL `GPL-3.0` text at line `183`**, in one `43,529 B` file | 🟢 byte-read |
| 🔴 [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | `1` | 🔴 **`2` BSD-3-Clause grants — its own, then `python-dateutil`'s** (Niemeyer / Pieviläinen), because `rrule.js` is a port. `3,493 B` | 🟢 byte-read |
| 🔴 [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | `1` | 🟡 **`2` — Apache-2.0 + a Creative Commons grant** in one `12,227 B` file | 🟡 measured, not byte-read |
| 🔴 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | `3` | 🔴 **`3` — ridered BSD, plus MIT + BSD in `LICENSE_HISTORY`** | 🟢 byte-read |
| 🟢 [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | `2` | 🟢 **`2` — MIT (`LICENSE-CODE`) + CC BY 4.0 (`LICENSE-CONTENT`)** | 🟢 byte-read · 🟢 **reproduces this base's own `T869`** |

🔵 **And `19` rows have no root licence file while `31` return no recognised grant — so `12` rows serve a licence file this pass could not grade.** 🟢 **Both numbers are published rather than collapsed into one.**

## `T916` — a classifier's ABSTENTION is a signal; its NON-abstention on a multi-grant row is a silent loss, and what it drops is the content licence

🟢 **`T900` established that GitHub's `NOASSERTION` was more honest than this base's hand grade. `p796` measures the rule and finds it two-sided.**

🟢 **Enrichment: `3` of the `5` multi-grant rows are `NOASSERTION` in GitHub's SPDX** (`odoo`, `rrule`, `open-webui`) 🔴 **against a base rate of `26` of `167` = `15.6%`** — 🟢 **a ~`3.9×` enrichment, so abstention is a cheap screen for multi-grant rows.** 🔵 **But only `3` of `26` `NOASSERTION` rows are multi-grant, so abstention is a screen and never a verdict.**

🔴 **The other half is worse, and it is new.** 🔴 **The `2` multi-grant rows GitHub DID grade are both code/content splits, and in BOTH cases it reported the CODE licence and silently discarded the CONTENT licence:**

| Row | 🔴 GitHub SPDX | 🔴 What it dropped |
|---|---|---|
| [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | `MIT` | 🔴 **CC BY 4.0 on every quest text, explanation and printable** — i.e. the teaching material |
| [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | `Apache-2.0` | 🔴 **the Creative Commons grant in the same file** |

🔵 **In this industry that is exactly the wrong half to lose. The code licence governs the software; the content licence governs the curriculum — the asset a client most wants to reuse, translate and rebrand.** 🟢 **Rule: on any row with more than one grant, the classifier's single answer is a fraction, not a summary — and the fraction it keeps is the code.**

## `T917` — a control set drawn from the rows that motivated a gate cannot detect the gate's FALSE POSITIVES

🔴 **`p795-G` required that a gate be controlled on the row that motivated it. I did that, on `4` rows (`rrule`, `open-webui`, `PageLM`, `oppia`), and all `4` reproduced. The instrument was still wrong on `26` rows.**

🔴 **The first instrument counted grants by matching the licence NAME at line start. It reported `32` multi-grant rows. The true count is `5`.** 🔵 **Mechanism: a single long copyleft text names itself several times — GPL-3.0's `35,147 B` contains `GNU General Public License` at line start **four** times (title, preamble, §14, and the appendix notice). So every GPL row scored `4` and every Apache/ECL row scored `3`.** 🟢 **Ground truth read by hand: `moodle/moodle`'s `COPYING.txt` is ONE grant; `chamilo/chamilo-lms` is ONE; `odoo/odoo` is genuinely TWO.**

🔴 **Why `p795-G`'s rule was necessary but not sufficient: all four of my controls were SHORT PERMISSIVE files — `3,493 B`, `2,819 B`, `8,563 B`, `11,358 B`.** 🔴 **None of them is a `35 KB` copyleft text, so none of them could exhibit the defect.** 🟢 **Rebuilt on per-grant VERSION LINES (`Version 3, 29 June 2007`, `Version 2.0, January 2004`, …), which occur exactly once per grant instance, the gate reproduces `9` of `9` controls across BOTH kinds.**

🔴 **Two further over-reports in the rebuilt instrument, both caught by reading the bytes and both the same mistake — `grep -c` counts LINES, not occurrences:** 🔴 `kumaken-1`'s `925 B` `LICENSE-CONTENT` names CC BY 4.0 on two lines and is ONE grant (`3`→`2`); 🔴 `OpenOLAT`'s `NOTICE.TXT` mentions the Mozilla Public License in a third-party list and is NOT an MPL grant (`2`→`1`). 🟢 **`0` of these three over-reports reached publication, and the uncorrected artefact is published beside the corrected one** ([`licence-block-census-UNCORRECTED-v1`](../evidence/licence-block-census-UNCORRECTED-v1.2026-11-12-p796.tsv)) 🔵 **so the `32`→`5` correction can be re-derived rather than taken on trust.**

🟢 **→ `p796-G`: a control set must span the population's KINDS, not just the rows that motivated the gate.** 🔵 **`p795-G` protects against a false zero; it does nothing about a false alarm. `T911` already said over-reports and under-reports are both defects at different prices — `T917` says they also need different control sets.**

## `T918` — `EUPL-1.2` is the third licence FAMILY this base's clause set has been missing, and it is the European one

🔴 **`p793-B` found the clause set had no `ECL-2.0` — this industry's own licence. `p795` found it had no `BSL-1.0`. `p796` finds it has no `EUPL-1.2`.**

🟢 **`3` rows serve it, and two of them are byte-identical:** [`hedyorg/hedy`](https://github.com/hedyorg/hedy) (★`1,697`, `13,827 B`) and [`open-education-api/specification`](https://github.com/open-education-api/specification) (`13,827 B`) — 🟢 **the same `EUROPEAN UNION PUBLIC LICENCE v. 1.2` text to the byte** — plus 🔴 [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) (`13,865 B`, 🔴 **archived**, `T901`). 🟢 **GitHub's SPDX independently reports exactly `3` `EUPL-1.2` rows, so the identification is two-channel.**

🔵 **Why it matters commercially and not just taxonomically: `EUPL-1.2` is the European Commission's own licence, it is COPYLEFT, and it is the one licence in this base with a statutory compatibility list rather than a compatibility opinion.** 🔴 **It is also the licence an EMEA public-sector education engagement is most likely to actually meet** — and the row carrying it, `hedy`, is a `★1,697` school programming environment. 🟢 **Three passes, three missing families, and all three were found by measuring bytes rather than trusting a family name.**

## `T919` — a licence file can be a STATEMENT ABOUT grants rather than a grant, and both a file count and a grant count misread it

🔴 [`ankitects/anki`](https://github.com/ankitects/anki) · `LICENSE` · `1,930 B`. 🔴 **It contains no licence text at all. It reads:** *"Anki is licensed under the GNU Affero General Public License, version 3 or later, with portions contributed by Anki users licensed under the BSD-3 license (see CONTRIBUTORS)."*

🔴 **A file count reads `1`. A grant-block count reads `0`. The truth is TWO families, `AGPL-3.0-or-later` and `BSD-3-Clause`, neither of whose text ships at root.** 🔵 **`T913` said a declaration is not a grant; `T919` adds that a declaration can be the only thing in the file, and that it can declare MORE than the classifier records** — 🟢 GitHub grades `anki` `AGPL-3.0` and the BSD-3 portions are invisible there too, which is `T916`'s loss in a second shape.

🟢 **This base publishes `anki` as `🔴 AGPL-3.0 · 1,930 B`, which is right about the governing licence and silent about the `1,930 B` being a pointer.** 🟢 Corrected in place in [`verticals/solutions.md`](../verticals/solutions.md).

## `T920` — `DSpace`'s `91,354 B` third-party anthology is a DELIVERABLE, not a hazard, and it says so itself (`p795-C`)

🟢 **`ACTION p795-C` discharged for its located target.** 🔴 **`p795` recorded a `91,354 B` `LICENSES_THIRD_PARTY` file in `DSpace/DSpace`'s root tree as "unopened" — the implication being an undiscovered copyleft exposure under a row graded `BSD-3-Clause` (`1,504 B`). 🟢 Opened, it is close to the opposite.**

🟢 **`721` dependency entries grouped by licence, and the file states the project's own policy in its preamble:** *"DSpace actually does NOT allow for any dependencies that are solely released under GPL terms."* 🟢 **The policy holds under measurement: the `GPL-3.0` section contains exactly ONE entry — `juniversalchardet:2.5.0` — and that same artefact is ALSO listed under `LGPL`, i.e. it is dual-licensed, which is precisely the case the preamble describes.**

🟡 **What is real: ~`13` `LGPL`-named entries**, including `openpdf:2.0.5`, `jna:5.18.1` (`LGPL-2.1-or-later`), `JHighlight`, `FindBugs-Annotations` and **`8` `java-json-tools` artefacts** (`json-patch`, `json-schema-validator`, `json-schema-core`, `jackson-coreutils`, …). 🟢 **For a server-side repository platform that is low risk — no modified library is distributed — but it is the first question a client's legal review asks.**

🟢 **The commercial reframe: this file is the third-party licence disclosure an engagement would otherwise have to generate, already built and already versioned.** 🔵 **`DSpace` is the only platform in this base that ships one. 🔴 Every other `Deps` cell here remains a claim about a version nobody identified.**

## `T921` — `p795-A`'s own specified data source carries a grade that the same pass's published rows contradict

🟢 **`ACTION p795-A` discharged as a filter over `91` MIT- and BSD-graded rows** ([`evidence/mit-bsd-bytesize-filter.2026-11-12-p796.tsv`](../evidence/mit-bsd-bytesize-filter.2026-11-12-p796.tsv)). 🟢 **`5` outliers, and the filter works: `PageLM` — the `T908` row the action was written for — is flagged, which is `p795-G`'s control satisfied.**

| Row | Bytes | Verdict |
|---|---|---|
| 🔴 `CaviraOSS/PageLM` | `8,563 B` (`+700%`) | 🔴 Known (`T908`) — non-commercial, redistribution prohibited |
| 🔴 `open-webui/open-webui` | `2,819 B` (`+88%`) | 🔴 Known (`T900`) — branding rider |
| 🟢 `goyanedelv/paes-mcp` | `2,018 B` | 🟢 **Benign as predicted — a bilingual MIT** |
| 🔴 `jkbrzt/rrule` | `3,493 B` | 🆕 🔴 **NOT a rider — TWO BSD grants** (`T915`) |
| 🟡 `daddysystem/nextgen-learn` | `1,338 B` | 🆕 🔴 **The TSV grades it `MIT`. The bytes are `Boost Software License 1.0`** |

🔴 **And `nextgen-learn` is the finding, because it is not a correction to this base — it is a correction to this base's EVIDENCE.** 🟢 **The published rows in [`agents/top.md`](../agents/top.md) and [`repos/foundations.md`](../repos/foundations.md) already say `BSL-1.0 (Boost)`, and they are RIGHT** — confirmed on two further channels this pass (the served bytes open *"Boost Software License - Version 1.0 - August 17th, 2003"*; GitHub's SPDX returns `BSL-1.0`). 🔴 **It is `evidence/rider-gate.2026-11-12-p795.tsv` — the artefact `p795-A` names as its data source — whose `grade` column says `MIT`.**

🔵 **Mechanism, and it is `T908`'s mechanism with a benign outcome: Boost 1.0 opens *"Permission is hereby granted, free of charge, to any person or organization obtaining a copy"* — the MIT grant sentence plus two words.** 🟢 **The consequence here is nil, because Boost is OSI-permissive and waives attribution for object-code-only distribution.** 🔴 **But the lesson is not nil: an action specified as *"a filter, not a new measurement"* inherits every defect of the artefact it filters.** 🟢 **→ `p796-H`: a grade column in an evidence file must be re-derivable from the bytes recorded beside it, or the file must not carry one.**

## 🟢 The pass's negative results, recorded because they cost budget to establish

🟢 **`0` of `174` addresses failed to clone**, and the `7` `CLONE_FAIL` results in the first run were 🔴 **my own address list, not the internet**: `6` rows in [`evidence/master-row-measurements.2026-11-12-p794.tsv`](../evidence/master-row-measurements.2026-11-12-p794.tsv) are prefixed `NEW/` (a column marker captured into the address), and 🔴 **one row is the literal string `OWNER/REPO`** — a template placeholder sitting in a published evidence artefact. 🔵 **Exactly the defect class this base guards against in its tables, found in its machine output instead.**

🟢 **`2` `EMPTY_TREE` rows reproduce `p793`/`p794`/`p795` exactly** (`Bestisco/My-WASSCE-Companion`, `Elite2828/ACE-AI-Tutor`) — 🟢 **four consecutive passes, same two rows, `0` drift.**

🔴 **`p795-D` (the `sha=` column) is NOT discharged for a third consecutive pass.** 🔵 The budget went to `p795-A`, `p795-B`, `p795-C`, `p795-F` and the regional legs. 🟢 **`T905` stands and every `sha=` written this pass is a git blob sha, labelled.**

🔴 **`p794-F`/`T906` persists into a third pass: the primary-source domains still fail at `CONNECT`.** 🔴 **Which is why `T922` below is an instrument NUMBER and not a quotation.**

## `T923` — the verification method this base is INSTRUCTED to use returns the same answer for a live repository and a nonexistent one

🔴 **The standing instruction for this KB is to verify every repository URL with `curl -sI` before writing it, on the principle that *"a 404 is not a finding"*. 🔴 In this environment that method is not merely unavailable — it is actively misleading.**

🟢 **Measured, with controls in both directions:**

| Address | `curl -sI` | 🟢 Blobless-clone channel |
|---|---|---|
| All `22` repository URLs written this pass | 🔴 **`403`** | 🟢 **`22` of `22` `OK`** |
| 🟢 `torvalds/linux` *(positive control — certainly live)* | 🔴 **`403`** | — |
| 🔴 `this-owner-does-not-exist-xyz/nope-99999` *(negative control)* | 🔴 **`403`** | 🟢 **`CLONE_FAIL`** |

🔴 **`curl -sI` against `github.com` returns `403` for everything: the agent proxy refuses the HEAD before GitHub ever sees it. A live repository and an invented one are indistinguishable.** 🔵 **So a pass that followed the instruction literally would record `403` on every row and either publish nothing or — far worse — read `403` as "not `404`, therefore fine" and publish every invented address it was handed.**

🟢 **The clone channel discriminates, and it was controlled in both directions this pass:** `git clone --filter=blob:none --bare --depth 1` returns refs and a readable `HEAD` for live addresses and fails for nonexistent ones. 🟢 **`176` addresses in `16` seconds at `12` parallel, `0` false failures, and a negative control that fails as required.** 🟢 **It is also strictly stronger than a HEAD request, because it returns the licence bytes this base grades on rather than a status line.**

🔵 **This is `T906`'s shape in a second place, and the generalisation is the point: a channel that returns one answer for every input is not a verification, whatever its status code says.** 🟢 **`p793-G` required that an instrument's silence be read as a property of the instrument. `T923` is the stronger case — a UNIFORM NON-SILENT answer, which looks like data.** 🔴 **Recorded here so the instruction can be corrected rather than quietly failed** → `p796-F`.

## `T922` — the EU AI Act education deadline is settled to an INSTRUMENT, not a paraphrase (`p795-F`)

🟢 **`ACTION p795-F` discharged, by the route the action specified: not the blocked primary sources, but convergent secondary trackers all naming the same instrument.**

🟢 **The instrument is `Regulation (EU) 2026/1744`** — the *Digital Omnibus on AI* — reported published in the Official Journal on **`2026-07-24`** and in force **`2026-07-27`**.

| Obligation | Was | 🔴 Now |
|---|---|---|
| 🔴 **Annex III standalone high-risk — THIS INCLUDES EDUCATION** | `2026-08-02` | 🔴 **`2027-12-02`** (Art. `113`) — **a `16`-month shift** |
| Annex I (high-risk in regulated products) | `2027-08-02` | `2028-08-02` |
| High-risk systems used by public authorities | — | `2030-08-02` (Art. `111(2)`) |
| 🟢 **Art. `50` transparency** | `2026-08-02` | 🟢 **UNCHANGED — in force since `2026-08-02`** |
| 🟢 Art. `5` prohibitions | live | 🟢 **UNCHANGED — live** |

🔴 **Commercially this resets the clock this base has been selling against for four passes (`P792-3`, `P794-2`): admissions, grading and exam-assessment systems are Annex III, so their conformity deadline is now `2027-12-02`.** 🟢 **But the part that did NOT move is the part that bites first: Art. `50` transparency has applied since `2026-08-02`, so an AI tutor must already disclose itself, today, regardless of the deferral.**

🔵 **Channel discipline: this is still secondary testimony — `eur-lex.europa.eu` remains `403` at `CONNECT` (`T906`), so the text has not been read here.** 🟢 **What changed is that a named instrument with an article number can be verified by anyone in one lookup, which a paraphrase cannot.** 🔴 **Status: `CITED, NOT READ`.**


## 🆕 `p795` — **six findings. The headline is that a gate built to catch licence riders was specified to key on the very classifier whose silence a rider causes, so it returned zero on `167` rows including the row it was built for.**

## `T908` — the MIT grant sentence can be camouflage, and the restriction arrives in the same sentence

🔴 [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) · `LICENSE.md` · `8,563 B` · `e1de68833d1c`. 🔴 **It opens with the canonical MIT grant, word for word:** *"Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, and run the Software"* — 🔴 **and completes that same sentence with** *"for **personal, educational, or non-commercial research purposes**"*, before a later section headed **"Prohibition on Redistribution"**: *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited."*

🔴 **This base's own multilingual grant probe (`p793-B`, re-run `p794`) keys on that exact phrase.** 🔴 **Measured by grant phrase alone, `PageLM` grades MIT** — a permissive-biased failure on a repository that forbids both commercial use and redistribution.

🔵 **Why the previous failures did not predict this one.** `T900` (open-webui) appended a **fourth clause** to a three-clause licence — detectable by clause count. `T902` (Dirigo) wrote the restriction in **another language** — detectable by vocabulary. 🔴 **`T908` writes the restriction in English, in the first sentence, as a subordinate clause of the grant itself.** 🟢 **Neither clause-counting nor restriction-vocabulary would catch it alone; what caught it was BYTE SIZE — `8,563 B` against canonical MIT's `1,070 B`, `+700%`.**

🟢 **Generalised rule: a grant phrase establishes a licence FAMILY only when the byte size is consistent with that family.** 🟢 **Cheap, deterministic, and it subsumes all three failures so far.**

## `T909` — `UNGRADED` answers "which family", and a reader needs "can we ship it"

🟢 **This base's `UNGRADED` verdict is correct and hard-won** — `T845`–`T849` are a series of failures caused by forcing bespoke licences into OSI families. 🔴 **But `UNGRADED` is silent about consequence, and on two rows the consequence is absolute:** `PageLM` is non-commercial and bars redistribution; `1edtech/caliper-spec` is implementable but not redistributable, with IMS as *"the sole arbitrator of compliance"*.

🔵 **The defect is not the grade, it is the shape of the record.** 🟢 **A classification field and a usability field are different questions and both must be published.** 🔴 **An engineer who reads `UNGRADED` and opens nothing learns that the family is unclear — not that the answer is "no".** 🟢 **Fix shipped as a consequence field beside the family field, in `agents/top.md`, `repos/foundations.md` and `verticals/solutions.md`.**

## `T910` — a licence that NAMES other licences defeats substring classification, and this completes the pair

🔴 **EUPL-1.2 carries an Appendix of compatible licences; line `269` reads *"GNU Affero General Public License (AGPL) v. 3"*.** 🔴 **A probe testing for AGPL before EUPL therefore mis-families `3` of `3` EUPL rows in this corpus** — `hedyorg/hedy`, `open-education-api/specification`, `european-commission-empl/European-Learning-Model` — 🟢 **and GitHub's classifier got all three right.**

🔵 **Set beside `p794`'s `ECL-2.0` finding this is now a complete statement of how title-matching fails, in both directions:**

| Family | Failure | Cause |
|---|---|---|
| 🔴 `ECL-2.0` | **MISSED** (returns `UNRECOGNISED`) | Its body does **not** contain *"Apache License"*, the title it derives from — `0` occurrences |
| 🔴 `EUPL-1.2` | **MIS-CALLED** (returns `AGPL-3.0`) | Its body **does** contain the titles of licences it is not |

🟢 **Remedy: match the first non-blank line only — never a substring of the body — and order the most specific family first.** 🟢 **Byte size is the independent check that would have caught it anyway: `13,827 B` is nowhere near AGPL-3.0's `34,523 B`.** 🔵 **Two instruments disagreeing is information; one instrument reading a licence's bibliography as its identity is not.**

## `T911` — a restriction token must be scoped by family, or a licence votes against itself

🔴 **GPL-3.0 and AGPL-3.0 contain the word *"noncommercially"* in their own permissive text** — *"alternative is allowed only occasionally and noncommercially"*, line `271` of the canonical body. 🔴 **An unscoped NonCommercial probe flags `27` of `27` GPL-family rows in this corpus as NonCommercial-restricted; all `27` are false**, including `moodle/moodle`, `openedx/edx-platform`, `instructure/canvas-lms` and `odoo/odoo`.

🟢 **But the DIRECTION is the opposite of `T900`, `T902` and `T908`, and that matters more than the count.** 🔵 **This failure returns an answer LESS usable than the truth.** 🟢 **`p794-G` says never let an instrument err toward "usable"; `T911` is the companion: both directions are defects, and they are not the same price.** 🔴 **An over-report costs an engineer an afternoon of licence reading. An under-report puts a NonCommercial repository into a client deliverable.** 🟢 **So suppress over-reports — but never by a change that buys even one new under-report.**

🔴 **Two further instrument defects in this pass, same shape, all caught by controls before any verdict shipped:** a bare `"trade name"` token flagged `BRANDING` on every Apache-2.0 and `ECL-2.0` row (their `§6` trademark section uses the phrase), and a loose `atribuci` token mis-called the Spanish **MIT** control (`goyanedelv/paes-mcp`) as **CC**. 🟢 **`3` defects, `3` caught, `0` shipped — the control set is doing its job, and it is the same control set `p793` built.**

## `T912` — a licence boundary can run per-FILE, and the carve-out can forbid the recommended use

🔴 **`metabase/metabase` carries FOUR root licence files. This base recorded two of them and described the split as "BY DIRECTORY".** 🔴 **`LICENSE-EMBEDDING.txt` (`8,877 B`) governs a single file — `app-embed.js` — lifting it out of AGPL (*"free and clear of any Affero GPL License requirements"*) and into a proprietary EULA that forbids modifying it, forbids *"blocking, overlaying, or otherwise obstructing the contents of the embedded element"*, and in `§3` forbids *"the removal of the Metabase's name or logo in the iframe that is embedded in your application."***

🔴 **This base recommends `metabase` as the BI layer under learning-analytics dashboards. Embedding it white-labelled is the prohibited act.** 🟢 **Narrow, deployable conclusion rather than a withdrawal: run metabase as its own AGPL-3.0 application behind SSO and link to it.**

🔵 **The generalisation is about granularity, and it is new to this base.** 🟢 Licence scope has been read here at two levels — repository (`T884`: a licence is a property of a VERSION) and directory (metabase's `enterprise/`). 🔴 **`T912` adds a third: a single FILE can carry its own licence, and the file that does is likely to be the one the vendor most wants to control — the embed, the client, the SDK.** 🟢 **So count the licence files before describing a boundary**, and note that this pass found the same branding-restriction shape on two different recommended surfaces (`T900`, `T912`).

## `T913` — a declaration is not a grant

🔴 **`frappe/education` `license.txt` is `19` bytes: `License: GNU GPL V3`** (blob `beca17940a71`, no trailing newline). ★`707`, LIVE, pushed `2026-10-30`. 🟢 **GitHub returns `NOASSERTION` and GitHub is right.**

🔵 **The holder has NAMED a licence without shipping one.** 🔴 **There is no grant text, no copyright line, no warranty disclaimer — nothing to accept and nothing to rely on.** 🔵 **A statement *about* a licence is evidence of intent, not an instrument**, and the gap bites in both directions: a client can rely neither on GPL-3.0 terms that were never published, nor on permission that was never granted. 🟢 **Graded `DECLARED-GPL-3.0-NO-GRANT-TEXT`, and the remedy is free — an upstream issue asking Frappe to commit the licence body.** 🟢 **This also resolves the identity of the `19`-byte file `T905` could not account for.**

## 🟢 The pass's negative results, recorded because they cost a pass to establish

🟢 **`T901`'s prediction is REFUTED.** `p794` found `3` archived rows in `164` measurements and wrote *"the `3` is a floor, not a count"*. 🟢 **`167` rows measured this pass: still exactly `3`, the same `3`. It was a count.** 🔵 **Worth recording because the instinct to assume a new finding generalises is exactly what `T903` (a search-index miss is not an absence) warns about in the other direction.**

🟢 **`p794-C` CONFIRMED with no correction.** `oppia`'s `mutagen==1.47.0` → PyPI version-scoped JSON returns `license: "GPL-2.0-or-later"` plus the OSI `GPLv2+` classifier, agreeing with the lockfile instrument. 🟢 **The GPL-2.0-not-AGPL-3.0 distinction this base's `oppia` deliverable rule depends on holds.** 🔵 **`T884` is why a version-level claim still had to be checked after four passes.**

🔴 **`T906` persists, re-tested.** All `6` primary-source domains fail at `CONNECT` with no HTTP status. 🔴 **And this pass shows the cost precisely: the EU AI Act's high-risk education deadline reportedly moved `16` months, to `2027-12-02`, and that fact — which resets every EMEA conformity pattern in this base — cannot be raised above "reportedly" from here.** 🟢 **`p794-F` remains the highest-leverage single action available to anyone with access to this session's configuration.**

## 🆕 `p794` — **eight findings. The headline is that a `★158,480` row this base green-flagged as BSD-3-Clause carries a fourth clause that bars white-labelling, and that `ARCHIVED` is an existence state no instrument here has ever read.**

🟢 **`170` addresses measured on three independent channels.** 🟢 **`118` of `118` licence grades agree with GitHub's own SPDX classifier · `0` disagree.** 🔴 **`1` grade corrected · `3` rows found archived upstream · `5` defects in this pass's own instruments, all caught before publication.**

## `T900` — a licence rider is invisible to family matching, and this one bars the thing a client engagement does

🔴 **This base published [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (`★158,480`) as `BSD-3-Clause` in two live files**, recommending it as *"the quickest compliant front end for a school-hosted model"* and *"the fastest data-resident front end"*. 🔴 **The grade is wrong, and the reason is structural rather than careless.**

🟢 **Canonical BSD-3-Clause has exactly three numbered clauses. The served `LICENSE` has four**, and the fourth is a branding-protection rider: it prohibits *"altering, removing, obscuring, or replacing any 'Open WebUI' branding, including but not limited to the name, logo, or any visual…"* and declares that alteration *"shall constitute a material"* breach.

| Why every existing instrument here missed it | |
|---|---|
| 🔴 Title line | Unchanged — it still reads as a BSD licence |
| 🔴 Clause language | Clauses `1`–`3` are **verbatim** BSD-3-Clause, so clause matching succeeds |
| 🔴 Anchored-title gate (`p790`) | Passes — the title is genuine |
| 🔴 Family matching | Returns `BSD-3-Clause` with full confidence |
| 🟢 **Byte size** | 🟢 **Would have caught it: canonical BSD-3-Clause ≈`1,500 B`, this is `2,819 B`** — `p790-F`'s size-triggered gate was never pointed here |
| 🟢 **Clause count** | 🟢 **Catches it exactly: `>3` numbered clauses on a BSD-3 body means a rider** |
| 🟢 GitHub's classifier | 🟢 **Said `NOASSERTION` — more honest than this base's hand grade, the one row in `141` where that is true** |

🔴 **And the repository lays the trap three files deep:** root holds `LICENSE` (`2,819 B`, ridered), **`LICENSE_HISTORY` (`2,872 B`, which grades as clean `BSD-3-Clause`)** and `LICENSE_NOTICE` (`721 B`, a title line only). 🔴 **A diligence reader who opens the wrong one of three gets a clean answer.**

🟢 **Corrected grade: `BSD-3-Clause + branding rider`, not OSI-conformant.** 🔵 **Commercially:** the copyright permissions are intact, so Globant can self-host, modify and ship it — 🔴 **but not under the client's name.** That is the one thing a delivery surface is for. 🟢 **Ship it with Open WebUI branding intact, or build the front end.**

🔵 **`T900` is the seventh recorded way to misread a licence here, and the first that is ADDITIVE.** The six before it were all failures to *recognise* a grant — case, title, length, language, appendix, affero-substring. 🔴 **This one recognises the grant correctly and misses what was appended to it.** 🟢 **General rule: match the family, then count the clauses.**

## `T901` — `ARCHIVED` is a third existence state, and `git ls-remote` cannot see it

🟢 `p793` replaced exit-status grading with three states — LIVE (`rc=0` ∧ `refs ≥ 1`) · EMPTY (`rc=0` ∧ `refs = 0`) · ABSENT (`rc=128`) — and `p794` reproduced it across `170` addresses with **`0` corrections**, so `T892` is confined to the two rows it named. 🔴 **But the instrument is still blind in a way that matters more than the one `p793` fixed.**

🔴 **An archived repository returns `rc=0` with `refs ≥ 1` and a valid `HEAD`. Its signature is identical to a healthy repository.** It clones, it serves bytes, its licence grades correctly — and it is read-only, accepts no patches, and in two cases here has been frozen for years.

🔴 **The word *archived* appeared `0` times in `agents/top.md`, `repos/foundations.md` and `verticals/solutions.md`. Three rows this base actively recommends are archived upstream:**

| Row | ★ | 🔴 Last push | Published as |
|---|---|---|---|
| [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | `120` | 🔴 `2023-11-16` | *"ePortfolio — the natural home for skills-based credentialing"* |
| [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | `357` | 🔴 `2021-01-04` | *"the input primitive for a maths tutor on a tablet"*, 🟢 **"Rescued"** at `p786` |
| [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | `54` | 🟡 `2024-02-14` | *"the vocabulary an EU public-sector client will expect"* |

🔵 **Two lessons, each sharper than the finding:**

🔴 **1. Resolving canonicity is not resolving maintenance.** This base did canonicity work on `mahara` — it records that `mahara/mahara` is DEAD and `MaharaProject/mahara` is the canonical owner. 🔴 **It resolved to the right address and that address is archived.** `T887` found a `★10` derivative ranked above a `★323` canonical repo; `T901` is the complement: **the canonical repo can be the dead one.**

🔴 **2. A licence rescue is not a viability rescue.** `p786` filed `MyScriptJS` as unusable, `p792` rescued it on the grant axis, and this base has recommended it ever since. 🔴 **No pass ever asked whether it was maintained. It has not been touched in nearly six years.**

🟢 **The remedy costs nothing: `archived` arrives in the same `gh api search/repositories` response that returns stars.** 🟢 **Existence needs four states — LIVE-MAINTAINED · LIVE-ARCHIVED · EMPTY · ABSENT.** 🟡 And grade the consequence by kind: an archived *data model* may be legitimately frozen; archived *code* under active CVE pressure is a fork you now own.

## `T902` — language-blindness on a RESTRICTION over-reports, and that is far worse than under-reporting

🔴 **`ACTION p793-B` predicted that English-only clause matching under-reports usable repositories, LATAM especially, and asked for a multilingual probe.** 🟢 **Built and run: MIT-family grant phrases in `20` languages** — English, Spanish, Portuguese, German, French, Italian, Dutch, Polish, Russian, Ukrainian, Turkish, Indonesian, Chinese, Japanese, Korean, Hindi, Arabic, Vietnamese, Thai, Hebrew — **plus the Creative Commons families, across all `170` addresses.**

🟢 **The prediction is REFUTED at the grant layer.** Exactly **one** non-English grant exists on this corpus — [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp), Spanish MIT, which `T864` already held. 🟢 **`19` added languages bought `0` new rows.**

🔴 **But the same sweep found language-blindness doing something the brief did not anticipate:**

| | |
|---|---|
| Row | [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo), `362 B`, Spain 🇪🇸 |
| 🔴 English-only CC probe returns | 🔴 **`CC-BY-4.0`** — permissive, commercially usable |
| 🟢 The bytes say | 🟢 **`CC BY-NC-SA 4.0`** — *"licencia Creative Commons Atribución-**NoComercial**-**CompartirIgual** 4.0 Internacional"* |
| 🔴 Mechanism | 🔴 **The sub-family tokens were English-only.** `NoComercial` ≠ `NonCommercial`; `CompartirIgual` ≠ `ShareAlike`. Each matched **`0`** times, so **both restrictions were silently dropped** and the base family survived |

🔴 **Under-reporting costs you an opportunity. Over-reporting puts a NonCommercial repository into a commercial deliverable.** 🔵 **`T902` is the asymmetry `T848` missed: a multilingual probe must be built for the RESTRICTION vocabulary first and the grant vocabulary second**, because a missed grant is a false negative you can afford and a missed restriction is a false positive you cannot.

🟢 **This base was never exposed** — `T863` graded `Dirigo` correctly by hand, in Spanish, two passes ago. 🔴 **Any probe built to `p793-B`'s brief would have been.** 🟢 **Remedy shipped: NC · ND · SA token sets in `13` languages (`nocomercial`, `naocomercial`, `nichtkommerziell`, `pas d'utilisation commerciale`, `non commerciale`, `非商业性`, `compartirigual`, `compartilhaigual`, `weitergabe unter gleichen bedingungen`, `相同方式共享`, …). Re-run: `Dirigo` grades `CC-BY-NC-SA-4.0`.**

## `T903` — a search-index miss is not an absence, and owner casing is not canonical

🟢 **`gh api search/repositories` with batched `repo:` qualifiers lifts this base's standing star-count limitation**: `10` addresses per call, exact integers, plus SPDX, push date and `archived`. **`164` of `170` re-measured.**

🔴 **The `6` it did not return all clone and serve refs:** `DaRL-GenAI/instructional_agents` · `NikolasSchaeffner/lehrer-agent` · `cosark/OpenTutor` · `csev/tsugi` · `foradian/fedena` · 🔴 **`openedx/edx-platform`** — one of the largest repositories in this sector. 🟢 **All verified LIVE with `git ls-remote --symref`.**

🔵 **`p793-G` instantiated for a new instrument: the search index is a view, not a census.** 🟢 **Before recording an absence from a search result, probe the git channel — it is the authority on existence and the search index is not.**

🟢 **The same call hands over canonicity for free: it normalises owner casing.** Two addresses this base publishes come back cased differently — `1edtech/caliper-spec` → **`1EdTech/caliper-spec`**, `anonymousonyx22/brightspace-d2l-mcp` → **`AnonymousOnyx22/brightspace-d2l-mcp`**. 🔵 Consistent with the `gegok12`/`GegoK12` collision this base already recorded; 🟢 **the search response is a cheap canonical-casing oracle.**

## `T904` — the ungranted set reproduced exactly, and `formalms` shows where a multilingual probe WOULD pay

🟢 **`20` LIVE repositories serve no recognised root grant, and every one was already recorded here as ungranted, refused or absent. `p794` adds no absence and removes none** — the second consecutive pass in which an independent instrument found nothing new to reject.

🟢 **The two not on the base's own `19`-row list are both recorded elsewhere in the file set**: [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (*"NO GRANT SERVED"*, at this exact address — and its only licence paths are vendored CKEditor plugins) and [`formalms/formalms`](https://github.com/formalms/formalms) (the any-depth-title gate).

🔵 **`formalms` is worth one line of its own.** Its licence files live at `html/lib/System/license/license_<language>.txt` — **a localised, non-root licence directory with one file per language.** 🟢 **It is simultaneously the one shape where a multilingual probe pays off and the one shape that grants nothing to the host**, because non-root grants are vendored (`T886`). 🔵 A probe tuned for language and blind to position would "find" a grant here and be wrong twice over.

## `T905` — the `sha=` column in this base is not one hash function, and some of it is neither

🟢 **Byte sizes here reproduce exactly — `8` of `8` on the rows checked. The `12`-character `sha` beside them does not.** Instrument controlled first: on `sakaiproject/sakai`, `git rev-parse HEAD:LICENSE` ≡ `git hash-object` ≡ the `ls-tree` blob id, all `2d2098a9192769636e5293867809c6e571dc6d97`.

| Row | Bytes | Published `sha` | 🟢 git blob sha | The published value is |
|---|---|---|---|---|
| `frappe/education` | `19` 🟢 | `beca17940a71` | 🟢 `beca17940a71` | 🟢 **git blob sha — correct** |
| `frappe/education` | `19` 🟢 | `1fcecf395312` | `beca17940a71` | 🔴 **`sha256` of the content** |
| `frappe/education` | `19` 🟢 | `61408d3da518` | `beca17940a71` | 🔴 **neither** |
| `VictorOsondu/ai-adoption-education` | `752` 🟢 | `2e9c34096bf9` | `e51a2ad5fd53` | 🔴 **`sha256`** |
| `sakaiproject/sakai` | `11,120` 🟢 | `593c74e1c7a5` | `2d2098a91927` | 🔴 **neither** |
| `luscitiosus/Dirigo` | `362` 🟢 | `9ed32d5c2577` | `3e22da8fe678` | 🔴 **neither** |
| `Kosudo/nextSIS` | `39,890` 🟢 | `60e422c7d93e` | `01fa8c8c4c6e` | 🔴 **neither** |
| `THU-MAIC/OpenMAIC` | `1,065` 🟢 | `717b69cbe2f4` | `76abc5f13261` | 🔴 **neither** |

🔴 **`frappe/education`'s single `19`-byte file is published in this base with three different hash values, in the same pass. That makes the defect internal, not content drift** — and the byte size is identical in every case, so nothing changed upstream.

🔵 **Why it matters:** a sha is in this base precisely so a later reader can prove the bytes have not changed. 🔴 **A column that mixes `git` blob sha1, `sha256` and unidentified values cannot do that**, and a future pass that "re-verifies" against it will manufacture a mismatch out of nothing. 🟢 **Byte size is the reproducible anchor. Treat every carried `sha=` as unverified until re-measured, and record the function that produced it.** 🟢 `p794`'s shas are `git rev-parse HEAD:<path>`, truncated to `12`.

## `T906` — the regional channel limit is a network-POLICY denial, which means it is fixable

🔴 **This base has recorded for several passes that `eur-lex.europa.eu`, `oecd.org`, `unesco.org`, `arxiv.org` and `wikipedia.org` are "not byte-reachable" (`T844`).** 🟢 **`p794` diagnoses the cause, and the diagnosis changes what should be done about it.**

🟢 **Measured:** `education.ec.europa.eu`, `op.europa.eu`, `data.consilium.europa.eu`, `europarl.europa.eu`, `ec.europa.eu`, `pib.gov.in`, `moe.gov.sg`, `ontario.ca`, `edresearch.edu.au` → **no DNS resolution, and the session's egress gateway logs `connect_rejected: gateway answered 403 to CONNECT (policy denial)` for each.** 🟢 **Positive controls on the same instrument in the same minute:** `registry.npmjs.org` `200`, `pypi.org` `200`, `raw.githubusercontent.com` `301`.

🔵 **So the instrument works and the hosts are fine — the environment's network policy declines the CONNECT.** 🔴 **That is not a research limitation to be worked around pass after pass; it is a session configuration a human can change in one place.** 🟢 **Recorded as an actionable request (`p794-F`), not as a standing limitation.** 🔵 Note what *is* allowed and why the dependency audits work: `registry.npmjs.org`, `pypi.org` and `files.pythonhosted.org` sit in the gateway's `noProxy` set.

## `T907` — the best trial yet run says the binding constraint is ENGAGEMENT, not model capability

🟢 **The strongest causal evidence this base has ever been able to cite arrived this window:** a **two-year cluster-randomised trial of Khanmigo across `18` Tennessee middle schools** (Hamilton County; Oreopoulos & Low).

| Measure | Value |
|---|---|
| Intent-to-treat, two years combined | **`≈0.06` SD** |
| Year 2 alone | **`0.08` SD** |
| 🔴 Year 1 alone | 🔴 **`0.020` SD — indistinguishable from zero** |
| 🟡 Implied full year of active participation | 🟡 **`≈0.14` SD** (participation-adjusted, **not** ITT) |
| High-dosage human tutoring | `0.2`–`0.4` SD |
| 🟢 **Uptake** | 🟢 **`96%` of assigned students used it** |
| 🔴 **Dosage** | 🔴 **The median student messaged the tutor on about `⅓` of practice days** |

🔴 **`96%` reach and `⅓` dosage is not a capability failure. It is a scheduling failure.** 🟢 **And the vendor's own 2026 response confirms the reading: Khanmigo was redesigned to activate AUTOMATICALLY during practice, because student-initiated use came in below expectation.**

🔵 **What this changes in how this base should be used.** Every pass of this base has ranked **tutors**. 🔴 **The evidence says the tutor is not the scarce component.** 🟢 **The scarce component is the mechanism that puts the tutor in front of the learner at the moment of difficulty, inside the institution's own workflow** — which is an LMS/SIS integration problem, and is exactly what this base's `p792` MCP rows and `p794`'s [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) are for. 🔵 **Corroborated independently:** the deployment literature finds effects *"strongest where the role is narrow and educator-controlled"*, and a `474`-study scoping review finds pedagogical design still poorly connected to technical capability. 🟢 **Sell the trigger, not the tutor** (`P794-1`).

---
## 🆕 `p793` — **eight findings. The headline is that this base's most fundamental instrument — existence by exit status — cannot tell a live repository from an empty one, and two rows published as DEAD are neither.**

🟢 **`p792-A` and `p792-B` both DISCHARGED, and `p792-B` cost `11` seconds for all `122` rows.** 🔴 **`2` published verdicts corrected.** 🟢 **`0` corrections required to any licence grade** — an independent instrument, built on a different channel, reproduced this base's published grade on `7` of `7` cross-checked rows including the Spanish-language MIT and the GPL-3.0/AGPL-3.0 split.

## `T892` — existence by EXIT STATUS cannot distinguish a live repository from an empty one

🔴 **This base's standing existence instrument is `git ls-remote`, with the exit status "read directly, never through a pipe".** That discipline was built to defeat pipe-swallowed failures, and it does. 🔴 **But it answers the wrong question.** An address that exists and holds **no refs at all** returns `rc=0` — indistinguishable from a healthy repository.

Measured this pass, four addresses on one instrument:

| Address | `ls-remote` `rc` | refs returned | `raw` README | clone | `HEAD` |
|---|---|---|---|---|---|
| `RAFCERAY/horizonia` | `0` | **`2`** | `200` | ok | `fffd7246dfab` |
| 🔴 `Bestisco/My-WASSCE-Companion` | `0` | **`0`** | `404` | ok | 🔴 unresolvable |
| 🔴 `Elite2828/ACE-AI-Tutor` | `0` | **`0`** | `404` | ok | 🔴 unresolvable |
| `gmilano/this-definitely-does-not-exist-xyz` | **`128`** | `0` | `404` | fails | — |

🔴 **CORRECTION TO THIS BASE.** `agents/top.md` and the Ghana row record these two as **`2` DEAD**. They are not dead. They **exist, are claimed by their owners, and are empty** — created and never pushed. `git clone` succeeds on both and leaves a repository with no `HEAD`.

🟡 **One loose end, declared rather than resolved.** The Ghana row records these two as *"both `rc=2`, re-probed and confirmed"*. 🔴 **`rc=2` is not reproducible in this session on either form of the command** — `git ls-remote URL HEAD` and `git ls-remote URL` both return `rc=0` with zero refs for these addresses, and `rc=128` for a planted absent one. So the provenance of the recorded `2` is unexplained, and it may have come from a different instrument or a different `git` build. 🟢 **The correction does not depend on it:** the repositories clone, hold no refs and serve `404` on `raw`, so *"DEAD"* is the wrong verdict whichever exit code a prior probe saw. 🔵 **And it is the reason to stop grading existence on exit codes at all — they are not portable across instruments, and the ref count is.**

🟢 **The corrected instrument: existence requires `rc=0` AND at least one ref.** Three states, not two:

| State | Test | What it means commercially |
|---|---|---|
| 🟢 **LIVE** | `rc=0`, `refs ≥ 1` | A real artefact to read |
| 🟡 **EMPTY** | `rc=0`, `refs = 0` | 🟢 **An author who registered an intent.** Reachable, and a *future* row |
| 🔴 **ABSENT** | `rc=128` | Nothing there |

🔵 **Why the distinction earns its place:** an absence is a dead end, but an empty repository is a **named person who claimed a name and has not shipped** — the same channel as a licence request, and a better prospect than a repository that never existed. Ghana's measured position improves: not `11` repositories with `2` dead, but `11` with `2` authors mid-intent.

🔴 **And this is `p792-G` reaching the base's own foundation.** `p792-G` said: if a verdict rests on a count, read the rows. `T892` is the same lesson one level lower — *if a verdict rests on an exit status, read the refs.*

## `T893` — a blobless clone turns `git ls-tree -l` into a NETWORK call per blob, silently

🟢 `git clone --filter=blob:none --no-checkout --depth 1` is the right tree instrument: trees arrive, blobs do not, and `git ls-tree -r --name-only` is then purely local. 🔴 **Adding `-l` to get byte sizes inverts that.** A size is a property of a blob, so a partial clone must **lazily fetch every blob in the tree** to print the column — on `learningequality/kolibri` the command had fetched a large fraction of the repository and been running for over two minutes before it was stopped, with the only visible symptom a stream of background `git gc` notices.

🟢 **The corrected recipe, and it is what produced this pass's `103` byte sizes:**

```bash
git -c gc.auto=0 clone --quiet --filter=blob:none --no-checkout --depth 1 "https://github.com/$slug" "$d"
git ls-tree -r --name-only HEAD          # local: trees only, no blob fetch
git ls-tree HEAD -- "$root_path"         # the ONE sha you need
curl -s "https://raw.githubusercontent.com/$slug/HEAD/$root_path"   # the bytes, on the byte channel
```

🔵 **The general shape: in a partial clone, every column is cheap except the one that is a property of the thing you declined to download.** `122` rows cost `10.9` seconds this way; the `-l` form did not finish one.

## `T894` — GPL-3.0 and AGPL-3.0 are separable deterministically, and a grep for "affero" gets it BACKWARDS

🔴 **GPL-3.0's own §13 is titled "Use with the GNU Affero General Public License".** So the canonical GPL-3.0 text contains the word *affero* — and a substring test for it grades every GPL-3.0 repository as AGPL-3.0. This is the **sixth** recorded way to misread a licence in this base, joining case-blindness (`T842`), title-line insufficiency (`T847`), length-as-integrity (`T845`), language-blindness (`T848`) and appendix contamination (`T849`).

🟢 **The discriminator, measured on `7` rows this pass and exact on all `7`:**

| Served bytes | `affero` occurrences | Verdict |
|---|---|---|
| **`35,149`** | **`3`** (all in §13's cross-reference) | 🔴 **GPL-3.0** |
| **`34,523`** | **`15`** (the grant itself) | 🔴 **AGPL-3.0** |

| Row | Bytes | `affero` | Verdict | This base's published grade |
|---|---|---|---|---|
| [`CREARED-EDU-CO/GenPrompt-Pre-ICFES-11`](https://github.com/CREARED-EDU-CO/GenPrompt-Pre-ICFES-11) | `34,523` | `15` | AGPL-3.0 | 🟢 **AGPL-3.0 — matches** |
| [`dpaul0501/OpenVidya`](https://github.com/dpaul0501/OpenVidya) | `34,523` | `15` | AGPL-3.0 | 🟢 **AGPL-3.0 — matches** |
| [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | `34,523` | `15` | AGPL-3.0 | 🟢 **AGPL-3.0 — matches** |
| [`Prady029/NCERT-AI-Teacher-Assistant`](https://github.com/Prady029/NCERT-AI-Teacher-Assistant) | `35,149` | `3` | GPL-3.0 | 🟢 **GPL-3.0 — matches** |
| [`chc-chupea/news-grade-reader`](https://github.com/chc-chupea/news-grade-reader) | `35,149` | `3` | GPL-3.0 | 🟢 **GPL-3.0 — matches** |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | `35,149` | `3` | GPL-3.0 | 🟢 **GPL-3.0 — matches** |
| [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | `39,890` anthology | `3` | GPL-3.0 | 🟢 **GPL-3.0 — matches `p790`'s correction** |

🟢 **`7` of `7`. This base's copyleft record is correct, and now it is correct on two independent instruments.** 🔵 The commercial reason the split matters: AGPL-3.0's §13 reaches a **hosted** education service, which is how Globant would deliver one; GPL-3.0's does not.

## `T895` — `kolibri`'s dependency claim is EXACT on the side it was measured, and the other side had `208` packages nobody had looked at

`ACTION p792-A` asked for every `Deps` claim to be re-audited against a resolved lockfile, naming `kolibri`'s **"2 LGPL of 32"** as the row that carries this base's embedding argument.

🟢 **The claim is CONFIRMED, exactly, and the "32" is now identified.** It is the **Python `base` dependency group in `pyproject.toml`** — `32` packages, every one `==`-pinned, so the manifest *is* the resolution. Resolved against PyPI **at each pin**, exactly `2` are LGPL:

| Package | Pin | `license` field | Classifier |
|---|---|---|---|
| 🔴 `zeroconf-py2compat` | `0.19.17` | `LGPL` | GNU Lesser General Public License v2 |
| 🔴 `json-schema-validator` | `2.4.1` | 🔴 **EMPTY** | GNU Library or Lesser General Public License |

🔵 **Note the second row: the `license` field is empty and only the classifier carries the copyleft.** `p791-G` warned that a blank field is not a verdict; here the blank field would have *under*-reported copyleft. The caution runs in both directions.

🔴 **But the npm side of the same repository had never been resolved at all.** `kolibri` is a **pnpm workspace with `40` importers**; its root `package.json` declares **`0` runtime dependencies**, so any audit that read the root manifest measured nothing. Collecting `dependencies` + `optionalDependencies` across all `40` importers and resolving each **at its locked version** against the registry gives **`208`** version-resolved runtime packages:

| | Count |
|---|---|
| MIT | `175` |
| Apache-2.0 | `10` |
| BSD (2/3-clause, incl. one `BSD`-only field read from bytes as 3-clause) | `9` |
| ISC | `5` |
| MIT-0 · CC0-1.0 · Unlicense · WTFPL · BlueOak-1.0.0 | `5` |
| 🟡 MPL-2.0 | **`1`** — `mathquill@0.10.1`, bytes confirmed (`16,725 B`) |
| 🟡 `(MPL-2.0 OR Apache-2.0)` | **`1`** — `dompurify@3.4.17`, 🟢 **elect Apache-2.0** |
| 🔴 **No grant anywhere** | **`1`** — see `T896` |
| 🟢 **GPL · LGPL · AGPL** | 🟢 **`0`** |

🟢 **Zero GPL-family packages in `208` version-resolved runtime dependencies.** 🟢 **The embedding argument survives, and is now stronger than the row claimed** — the copyleft in `kolibri` is `2` LGPL Python packages, both distribution-triggered rather than network-triggered, and nothing at all in the JavaScript that reaches a learner's browser.

🔴 **Where the residual risk actually sits is one plugin.** `mathquill` (MPL-2.0, file-level copyleft) and the ungranted package of `T896` are **both** declared by `kolibri/plugins/perseus_viewer` → `dependencies` — the exercise renderer, which ships to learners. `dompurify` sits in `packages/kolibri-common`, i.e. core, and is dual-licensed so Apache-2.0 can simply be elected.

🔵 **`requirements.txt` was a decoy, and it says so in its own first line** — *"This file exists only as the sink for any EXTRA_REQUIREMENTS injected at build time"*. A `Deps` audit that read it would have found `0` packages and reported a clean result. 🔴 **That is `p792-G` again: a file that structurally cannot contain the answer returns a confident `0`.**

## `T896` — a package can ship with no grant anywhere, and have no upstream address left

[`@khanacademy/mathjax-renderer@3.0.2`](https://registry.npmjs.org/@khanacademy/mathjax-renderer/3.0.2) is a **direct `dependencies` entry of `kolibri/plugins/perseus_viewer`**. Three channels, all read:

| Channel | Result |
|---|---|
| Registry metadata at the pinned version | 🔴 `license` absent · `licenses` absent |
| 🟢 **The published tarball — what actually ships** (`336,573 B`) | 🔴 **No `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` file at any path**; `license` absent from the packaged `package.json`; no licence line in `README` |
| Upstream repository named in the metadata (`Khan/mathjax-renderer`) | 🔴 **`git ls-remote` `rc=128` — the address does not resolve** |

🔴 **So the artefact a client would deploy carries no grant, and the project it came from has no reachable home.** 🟡 Khan Academy's other packages in the same tree (`@khanacademy/perseus`, `wonder-blocks-*`, `kas`, `math-input`) all resolve MIT at their pins, so this is one package, not a vendor posture.

🟢 **Reading the tarball, not the registry field, is what settles it** — and that is the version-level form of `T884`: the registry field describes a *version*, and the tarball *is* the version.

🔵 **Disposition: this is a licence-request target with a measured, specific ask** — not "please add a licence" but *"`3.0.2` ships without a grant and `Khan/mathjax-renderer` no longer resolves; which licence governs it, and where does it now live?"*

## `T897` — a hardening config is a CLAIM, not a control, and the best-engineered server in this sector says so in its own comments

`ACTION p792-D` asked for the canonical Canvas MCP's auth model to be read **before** any security offer was written. Read: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), MIT (`1,071 B`, `3c7307584ae4`), `529`-file tree.

🟢 **`p792-D`'s premise is PARTLY REFUTED, and that is good news badly needed in this sector.** This is not a server that never considered governance. It ships:

| Control | Evidence |
|---|---|
| 🟢 Structured audit trail | `src/canvas_mcp/core/audit.py` — `6,420 B`, `215` lines, `log_data_access` · `log_code_execution` · `log_access_change` |
| 🟢 **Identifier masking in the audit log** | `_sanitize_endpoint`: `/courses/12345/users/678` → `/courses/***/users/***` |
| 🟢 Executed code logged as a **hash**, never raw | `log_code_execution(code_hash=…)` — SHA-256 prefix |
| 🟢 Three deployment overlays | `config/overlays/{baseline,public,enterprise}.env` |
| 🟢 Sandbox with outbound network blocked by default | `TS_SANDBOX_BLOCK_OUTBOUND_NETWORK=true` in all three overlays |
| 🟢 Token rotation + security CI + its own prior reviews | `scripts/rotate-canvas-token.mjs` · `.github/workflows/security-testing.yml` · `docs/audits/2026-09-23-*` · `security/student-feature-review-2026-10-08.md` |

🔴 **And then the two findings that matter.**

**1. The hardened flags are self-declared placeholders.** `enterprise.env` sets `MCP_CLIENT_AUTH_MODE=api_key_or_mtls`, `MCP_CLIENT_API_KEY_REQUIRED=true` and `MCP_CLIENT_CERT_AUTHORITY` under the comment **"(pending feature wiring)"**; `public.env` sets `TOKEN_STORAGE_BACKEND=keyring` under the same comment and `LOG_REDACT_PII=true` under **"Logging hygiene (some flags are placeholders)"**. 🔴 **An institution that reads `enterprise.env` as a control inventory would believe mTLS client authentication and PII redaction are in force.** The project is honest in its comments; the risk is in how a procurement reader uses the file.

**2. The token layer protects the MCP server, not the Canvas account.** `core/access/tokens.py` is `50` lines: `mint_token` / `verify_token` over HMAC-signed claims (`oid`, `jti`, `exp`) — authentication **of clients to this server**. The Canvas credential underneath is untouched, and `SECURITY.md` states the consequence plainly: 🔴 **"Your Canvas API token has full access to your Canvas account."** There is no per-tool scoping, because Canvas does not offer one; the mitigation on offer is `chmod 600 .env`.

🔴 **Meanwhile `bulk_grade_submissions` writes grades.** That is Annex III, point 3 — *evaluation of learning outcomes* — reached by an MCP tool call, holding an account-scoped credential, from `2027-12-02`.

🟢 **The corrected offer, and it is sharper than the one `p792-D` imagined:** the scaffolding exists and is explicitly unfinished. The engagement is **wiring and certifying controls the project has already designed** — finish the client-auth and keyring paths, make `LOG_REDACT_PII` real, add per-tool allowlisting above an account-scoped token, and produce the FRIA and audit evidence that Annex III will require. 🔵 **That is a far better conversation to open than "your server is insecure", and it is true.**

## `T898` — China placed at ministry level, in-language, with a document number (`p792-E`, first of four)

🟢 **The in-language ministry channel paid a fourth consecutive time** (`T891` predicted it). Searching `教育部 人工智能 教育 2026 政策 中小学 指南` returns the instrument itself, on `moe.gov.cn`:

**《"人工智能+教育"行动计划》 — "AI + Education" Action Plan, document number 教科信〔2026〕1号.** Issued **jointly by five bodies**: 教育部 (Ministry of Education), 国家发展改革委 (NDRC), 工业和信息化部 (MIIT), 科技部 (MOST) and 国家数据局 (National Data Administration). Signed **`2026-04-02`**, published **`2026-04-10`**.

| What it commits to | Why it is a procurement hook |
|---|---|
| Continue developing 《中小学人工智能通识教育指南》 (K-12 AI general-education guideline) and run AI courses fully | 🟢 Curriculum-aligned content, per stage, is a named deliverable |
| AI education written into **local** curriculum systems, each locality issuing its own course guide with objectives, content and **class-hour requirements** | 🟢 **Procurement is provincial, and there are ~`34` of them** |
| Strengthen K-12 AI education bases; support **rural and remote** schools via the national platform | 🟢 Offline-first and low-bandwidth delivery — exactly `kolibri`'s shape |
| Revise compulsory-education and senior-secondary information-technology **curriculum standards** | 🟡 Content that must track a moving standard |
| 🔴 **Draft 人工智能应用安全评估指标 — AI application security assessment indicators** | 🔴 **A conformity regime is being written.** Earliest-mover advantage for anyone who can evidence controls |
| Goal: deep AI–education integration by **2030** | A multi-year programme, not a pilot |

Prior instruments in the same series, all pre-existing: 《中小学人工智能通识教育指南（2025年版）》, 《中小学生生成式人工智能使用指南（2025年版）》, 《职业院校人工智能应用指引》, 《教师生成式人工智能应用指引》.

🔵 **So APAC's "supply-rich, demand-blind" asymmetry is now half-corrected.** China has the strongest permissive agent supply this base has measured **and** a named five-ministry programme with a security-assessment regime in draft. 🔴 **India, Australia and Singapore remain unplaced at ministry level** — `p792-E` is discharged for `1` of `4`.

## `T899` — `p792-B`'s corrected gate works, is cheap, and found no licence errors to fix

🟢 **`ACTION p792-B` DISCHARGED across all `122` repository addresses in `agents/top.md`, in `10.9` seconds**, carrying `p791-E` (tree audit) and `p791-F` (byte sizes) together as instructed.

🟢 **The gate was controlled on the two known-answer rows before use, and behaved correctly in both directions** — the two failure modes `T886` recorded:

| Control row | Uncorrected gate (`T886`) | 🟢 Corrected gate |
|---|---|---|
| `mingxuanyan07-lgtm/ai-for-education-showcase` | 🔴 would have **rescued** it | 🟢 `NO_ROOT_GRANT`, `2` vendored paths (`Rethlas/LICENSE`, `scripts/vendor/katex/LICENSE.txt`) — correctly **not** rescued |
| `oppia/oppia` | 🔴 flagged on `23` path hits | 🟢 `ROOT_GRANT` Apache-2.0 `11,358 B`, `vendored_nonroot=0` — correctly **not** flagged |

**Results across `122` rows:** `103` root grants, each with path, **byte size and `12`-char blob sha recorded** · `19` with no root grant · `0` clone failures.

🟢 **And the outcome on grades is the one worth stating: `0` corrections.** Every row cross-checked against this base's published verdict matched — including the four rows whose root grant my own clause-grep returned as `UNRECOGNISED`, every one of which this base had already graded correctly by hand:

| Row | Gate said | Bytes say | Published grade |
|---|---|---|---|
| `goyanedelv/paes-mcp` | 🔴 `UNRECOGNISED` | 🟢 **MIT, in Spanish** — *"Se concede permiso, libre de cargos"* | 🟢 **MIT (Spanish text) — matches (`T864`)** |
| `gabrielmahia/shule-ai` | 🔴 `UNRECOGNISED` | CC BY-NC-ND 4.0 | 🟢 **matches — "barred twice"** |
| `luscitiosus/Dirigo` | 🔴 `UNRECOGNISED` | CC BY-NC-SA 4.0 | 🟢 **matches (`p786` correction)** |
| `Tzxser/aipha-learning-os` | 🔴 `UNRECOGNISED` | "All rights reserved"; visibility ≠ permission | 🟢 **PROPRIETARY — matches** |

🔴 **The gate's own defect, found by this comparison: `COPYRIGHT_NOTICE` matched its grant-path pattern.** `Tzxser/aipha-learning-os` has no grant at all, and a path-name match nearly promoted a file that is the *opposite* of a grant. 🟢 **A path name selects a candidate; only the clauses decide.** And my clause set was English-only, so it re-created `T848` on `paes-mcp` within minutes of `T848` being written down — 🔵 **which is the strongest available argument that the language-blind failure mode is the default, not an accident.**

## 🆕 `p792` — **eight findings. The headline is that this base told clients not to ship its most-recommended platform, on a licence that platform does not use.**

🟢 **Channel status, re-measured:** `git ls-remote` 🟢 · `git ls-remote --symref` 🟢 (new, and now mandatory — see `T885`) · blobless clone + `ls-tree` + `cat-file` 🟢 · `raw.githubusercontent.com` 🟡 **works, with a silent branch alias** · `search/repositories` 🟢 exact integers · **npm registry** `registry.npmjs.org` 🟢 (new, per-version licences) · **PyPI** `pypi.org/pypi/*/json` 🟢 (new) · `api.github.com/repos/*` 🔴 `403` · `github.com` page 🔴 `403`.

## `T884` — a licence is a property of a VERSION, not of a package

🔴 **This base has published, for four passes, that `oppia/oppia` carries `1 AGPL-3.0 of 171` direct dependencies, with the instruction: *"DO NOT ship as-is."*** 🟢 **The dependency count is exactly right. The licence is not.**

| Measured | Value |
|---|---|
| `package.json` direct deps | `83` + `88` = **`171`** 🟢 matches |
| `angular-shepherd` declared | `^11.0.0`, in `dependencies` 🟢 reaches the bundle |
| 🟢 `yarn.lock` resolves to | 🟢 **`11.0.0`** · integrity-pinned |
| 🟢 Licence of `11.0.0` | 🟢 **MIT** |
| 🔴 Licence of `latest` (`22.0.0`) | 🔴 **AGPL-3.0** |
| 🟢 Relicence boundary | 🟢 **MIT `v0.0.1`–`v21.x`; AGPL-3.0 from `v22.0.0`** |

🟢 **`^11.0.0` admits `>=11.0.0 <12.0.0`. The AGPL-3.0 starts at `22.0.0`. The range cannot reach it.** The same holds for `shepherd.js@^8.0.1` → `8.3.1` (MIT; AGPL-3.0 from `16.0.0`).

🔴 **The error was reading the licence field at `latest` and attributing it to the pinned dependency.** 🟢 **The remedy is one step: resolve the lockfile.** `p791-B` asked for exactly that — *"lockfile, not manifest"* — and it was the right instruction for a reason the queue did not anticipate.

🔵 **Why this is the most expensive defect class this base has found.** A false *positive* on copyleft removes a usable option: `oppia` is Apache-2.0, `7.0k★`, and the single best interactive-lessons platform in the sector, and this base steered engagements away from it. 🔴 **A grant gate that errs toward refusal still errs.** 🟢 **New rule: a dependency licence claim must name the RESOLVED version it was read from, or it is not a measurement.**

🟢 **The same audit found what the base had missed in the other direction:** `mutagen==1.47.0`, **GPL-2.0-or-later**, a **direct** entry at `requirements.in` line `25` of `oppia`'s `152`-package `pip-compile` lockfile. 🟡 Strong copyleft, but **distribution-triggered, not network-triggered** — for a hosted platform it does not reach client code, where the claimed AGPL-3.0 would have.

## `T885` — `raw.githubusercontent.com` silently aliases `master` to the default branch, in one direction only

🔴 **Noticed because six unrelated repositories returned byte-identical licences on both `main` and `master`.** That should not happen, and it does not mean what it looks like.

| Repository | True default | `main` head exists? | `master` head exists? | raw `main` | raw `master` |
|---|---|---|---|---|---|
| `bruchris/canvas-lms-mcp` | `main` | 🟢 yes | 🔴 **no** (of `59` heads) | `200` | 🔴 **`200`** |
| `jupyter/nbgrader` | `main` | 🟢 yes | 🔴 **no** | `200` | 🔴 **`200`** |
| `sakaiproject/sakai` | `master` | 🔴 **no** | 🟢 yes | 🔴 **`404`** | `200` |
| control: any repo, bogus ref | — | — | — | `404` | `404` |

🟢 **So the alias is real, specific and one-directional: `master` resolves to the default branch when `master` is absent; `main` does not.** A bogus name `404`s, so this is a legacy-name alias and not a blanket fallback.

🟢 **Consequence for this base: no grant verdict is wrong because of it** — the bytes served are the default branch's bytes, which is what should have been read anyway. 🔴 **But any row recorded as "verified on `master`" has a false branch attribution**, and a probe that tests branch *existence* by asking `raw` for a file will report `master` alive on repositories that have no such branch. 🟢 **Branch existence is now read from `git ls-remote --symref` only.**

## `T886` — a licence-path COUNT is not a grant test

🔴 **This pass built the cheap gate `p791-E` asked for** — enumerate the tree, count paths matching `licen|copying|notice|legal|terms`, flag anything above one — **and the gate is wrong in both directions on its first two subjects.**

🔴 **False rescue.** [`mingxuanyan07-lgtm/ai-for-education-showcase`](https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase) is one of this base's five standing **ungranted** rows. It now matches **`2`** licence paths: `Rethlas/LICENSE` (Apache-2.0, `11,558 B`) and `scripts/vendor/katex/LICENSE.txt` (MIT, `1,107 B`). 🔴 **Both are vendored subdirectories and there is no root grant.** A count-based gate would have moved this row from *ungranted* to *granted* on someone else's licence.

🔴 **False flag.** `oppia/oppia` matches **`23`** paths. `21` of them are Angular **source files and screenshots** implementing Oppia's in-product licence page (`license-page.component.ts`, `licensePage-snap.png`). The grants are `LICENSE` and `NOTICE`. A count-based gate reports a `43,376★`-class anthology risk on a single-family Apache-2.0 repository.

🟢 **The corrected gate, and it is still cheap:** *(1)* the host's grant is the **root** grant and nothing else; *(2)* exclude source and image extensions before counting; *(3)* a non-root grant is a **vendored** grant — it constrains redistribution of that subtree and says nothing about the host's terms.

## `T887` — when a repository implements a named platform, sweep the name before writing the row

🔴 A `grading agent` query returned [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) first — MIT, `1,070 B`, `501` files, **`★10`**. 🟢 A name sweep returns the canonical [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) at **`★323`** (`1,071 B`, `529` files), then `boyuchengz/canvas-mcp` `★119` (MIT), then 🔴 `DMontgomery40/mcp-canvas-lms` `★104` **ungranted**. 🔵 `1,070` vs `1,071` bytes and `501` vs `529` files is the signature of a derivative. 🟢 **Search ranks by query match, not by canonicity** — this extends `p790`'s `janestreet`/`jane-street` finding from owners to protocols.

## `T888` — the three disputed statutory dates are RESOLVED, and one of them is a governance lesson

🟢 **`ACTION p791-C` discharged on all three.** `p791` labelled these rather than resolving them, and said to try national gazettes instead of `EUR-Lex`. That worked.

| Instrument | `p791` recorded | 🟢 `p792` resolves |
|---|---|---|
| 🇪🇺 **EU AI Act**, high-risk incl. education | 🔴 *"applying August 2026 **vs** deferred to `2027-12-02`"* | 🟢 **`2027-12-02`.** The **Digital Omnibus** reached Council–Parliament political agreement on **`2026-05-07`** and defers high-risk obligations — education, employment, biometrics — to that date. Commission consultation on the draft high-risk guidelines ran to **`2026-06-23`** |
| 🇻🇳 **Vietnam**, education as high-risk | 🔴 *"`2027-03-01` **vs** September 2027"* | 🟢 **Both figures were right about different things.** **Law `134/2025/QH15`** (dated `2025-12-10`, `8` chapters, `35` articles) took effect **`2026-03-01`**. Pre-existing systems get a transition; for **health, education and finance** it is **`18` months** → **`2027-09-01`**. The `2027-03-01` figure is the `12`-month general case. 🟡 One source gives the range as `12`–`18` months, so the category boundary is the residual uncertainty, not the dates |
| 🇿🇦 **South Africa**, draft National AI Policy | 🔴 *"published `2026-04-10` vs abrogated `2026-04-27` — conflicting"* | 🟢 **Both happened, and neither word was right.** Cabinet approved the draft `2026-03-25`; published for comment in **Gazette `54477`** on **`2026-04-10`**; the Minister **announced** withdrawal on **`2026-04-26`**; it was formally **withdrawn in its entirety by Notice `3978` of `2026`, Gazette `54840`, dated `2026-06-12`**; Cabinet approved the withdrawal in June. 🔴 One regulatory database still lists the withdrawal as `2026-09-27` — a tertiary source against a gazette notice |

🔴 **The South African reason is the finding, not the date: the draft was withdrawn because it contained AI-hallucinated references.** The Minister cited a failure that compromised the integrity and credibility of the draft. 🔵 **A national AI policy was retracted because it was drafted with unverified AI output** — and the department is still targeting FY2026/27 to finalise a reworked framework. 🟢 **This base's entire method is the counter-example to that failure**, and it is now worth saying so to a client in one sentence: *the verification discipline is the deliverable.*

## `T889` — for the second consecutive pass, the grant the first layer missed was a FONT grant

🟡 `p791`: OpenMAIC's `ZcoolHappy` — a non-OSI Chinese-language font licence inside a `43,376★` MIT repository. 🟡 `p792`: `Study-Mate`'s `lib/katex/fonts/LICENSE` — **SIL OFL, `4,616 B`** — inside an MIT repository whose first-layer audit `p791` recorded as clean.

🔵 **KaTeX appeared in THREE separate repositories this pass** (`Study-Mate`, `ai-for-education-showcase`, and vendored again under `scripts/vendor/`). 🟢 **It is the sector's most-vendored maths renderer, and it ships two grants: MIT for the code and OFL for the fonts.** 🟢 **Standing rule: in education, maths rendering is near-universal, so assume a font grant is present and go and read it.**

## `T890` — a source's regional bucket is not this base's regional field

🔴 **The APAC leg of this pass's regional sweep returned, as APAC findings, the UK's generative-AI safety standards for schools (January 2026) and the UAE Ministry of Education's 25 generative-AI prohibitions (February 2026).** Neither is APAC. 🟢 Both are placed under **EMEA** in `intel/market.md`, where they belong.

🔵 **Why this is worth a trend ID rather than a correction note.** This base's `region` field is a **closed vocabulary of five values**, and its whole purpose is that an engagement can filter on it. 🔴 **A search result arrives with the *source's* bucket attached, and sources bucket by convenience** — a vendor report covering Asia-Pacific sales territory will file the Gulf under APAC because that is how the sales team is organised. 🟢 **The region field must be assigned by the curator from the named country, never carried over from the source.** `T883` found that a composite bucket hides a continent; `T890` is the other half — **a bucket can also contain things that are not in it.**

## `T891` — the in-language ministry query pays, and `p790-E` predicted exactly this

🟢 **`ACTION p790-E` discharged, third carry.** `p790` predicted that an English-language LATAM leg would return institutional structure rather than ministry policy, and that a Spanish-language **Colombian** leg would pay. 🔴 `p791` ran English and got UNESCO/ECLAC, CENIA and Ceibal — structure, exactly as predicted. 🟢 **One Spanish-language query returned named, dated Colombian instruments**, recorded in `intel/market.md` under LATAM: the first classroom AI **lineamientos** (January 2026), **Directiva 01 of `2026-03-05`**, the **Decálogo de IA para la Educación Superior**, and **CONPES 4144 de 2025** as the governing national AI policy.

🔵 **Three passes of this base now agree on one thing: the language of the query decides whether a ministry is visible.** `p787` (India: `NCERT`, not `tutor`), `p789` (Korea: `학습 튜터`, not `교육 에이전트`), `p790`/`p792` (Colombia: Spanish ministry vocabulary). 🟢 **It is no longer a caution; it is the default method for a regional leg.**

### 🔴 `5` defects in this pass's own instruments, all caught by controls before any verdict shipped

| # | Defect | How it was caught | Status |
|---|---|---|---|
| **D1** | 🔴 A copyleft grep matched **`MPL` inside `uriteMPLate`** — the package *name*, not its licence (`uritemplate` is `BSD-3-Clause OR Apache-2.0`, dual-permissive) | Reading the matched rows instead of counting them | 🟢 Fixed: match restricted to the licence field. 🔵 **This is `T875`'s substring lesson reappearing in this pass's own tooling** |
| **D2** | 🔴 Audited `oppia`'s **Python** lockfile and was ready to publish a refutation of an AGPL claim that lives in the **npm** layer | The base's own published text names `angular-shepherd`, an npm package | 🟢 Fixed: both layers audited. 🔴 **A refutation aimed at the wrong layer would have been a worse error than the claim it corrected** |
| **D3** | 🔴 Grepped `yarn.lock` for `agpl` and read the `0` as evidence | Lockfiles record resolutions and integrity hashes, **not licences** — the `0` was structurally guaranteed | 🟢 Fixed: per-version licences read from the npm registry |
| **D4** | 🔴 Filled in an **elided slug** (`Didaktikus-…-LP21` → a guess) and got `rc=128`, i.e. DEAD | A guessed address cannot produce a DEAD verdict; the owner sweep returned the real `59`-character slug, **alive and pushed `2026-08-23`** | 🟢 Fixed, and the full slug is now recorded. 🔴 **An elided slug is not an address** — the base must stop storing them |
| **D5** | 🔴 The new licence-path-count gate would have **rescued an ungranted row on vendored grants** | Reading the two paths instead of counting them | 🟢 Fixed: root-only, extension-filtered (`T886`) |

🔵 **Four of the five are the same mistake: counting a result instead of reading it.** 🟢 **That is now this base's most reliable self-check — if a verdict rests on a count, read the rows.**


## 🆕 `p791` — four findings, and one of them is that this base can finally PUBLISH

🟢 **Channel status, re-measured this pass:** `git ls-remote` 🟢 · blobless clone + `ls-tree` 🟢 · `git cat-file` on a `--filter=blob:none` clone 🟢 (lazy blob fetch works, and it is the cheapest byte channel this base has) · `search/repositories` 🟢 (exact integers) · `api.github.com/repos/*` 🔴 `403` · `github.com` page 🔴 `403`. Unchanged from `p790`.

🟢 **`T879-bis` — the push block is GONE, and four cycles of this base's history explain why it mattered.** `rotation.json` records, for education alone, `local-commit(421e4d7)-education-kb-push-blocked` (cycle 2) and `local-commit(4564416)-push-blocked-access-restriction` (cycle 3); the technology base records the same at `b46d379`. The cause was never GitHub — it was that `gmilano/education-kb` sat outside this session's authorised repository set, so the git proxy declined to inject a credential and returned `403` on push while `clone` succeeded. 🟢 **Attaching the repository to the session fixes it; this pass pushed.** 🔵 **The lesson is diagnostic, not clerical: a `403` on push with a working `clone` is an authorisation scope symptom, not a network one, and it should never again be recorded as "blocked" without naming the scope.**

## `T880` — `NOASSERTION` is NOT a licence verdict, and it fails in BOTH directions

🔴 **This pass found the two opposite causes of the same classifier output, in the same sector, hours apart.** GitHub's `licensee` matcher reports `NOASSERTION` when it cannot match canonical bytes. That is a statement about the matcher, not about the grant.

| Repository | `search/repositories` says | The bytes say | Why they disagree |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | `NOASSERTION` | 🔴 **`19 B`** — `License: GNU GPL V3`, blob `beca17940a71`, and **nothing else** | There is **no operative grant text at all** — only a family *name* |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | `NOASSERTION` | 🟢 **`1,150 B` valid MIT**, blob `f86101816893` | The matcher is defeated by an injected `<!-- SPDX-License-Identifier: MIT -->` HTML comment on line `3` and by **typographic curly quotes** (`“Software”`) in the operative text |

🔴 **`frappe/education` is the more consequential half, because this base already carries it** in `repos/foundations.md` and `verticals/solutions.md`. Its own siblings show what a grant looks like in the same org: [`frappe/lms`](https://github.com/frappe/lms) serves `33,893 B` and [`frappe/erpnext`](https://github.com/frappe/erpnext) serves `35,149 B` — full operative texts. `frappe/education` serves `19`.

🟡 **What that means for an engagement.** `License: GNU GPL V3` is a **stated intent**, not a licence: GPL-3.0 is granted by reproducing its terms, and a bare reference leaves the actual permission unstated. Treat the row as **intent-to-GPL-3.0** — plan for copyleft at the boundary, and get the grant confirmed in writing before any derivative ships. 🔵 It is almost certainly an oversight rather than a trap, and the fix is an upstream issue, not an avoidance.

🟢 **Rule added: `NOASSERTION` is a prompt to read the bytes, never an answer.** It joins `T875` (a long licence file may be an anthology) as the second case of a licence *signal* that cannot be graded without reading.

## `T881` — a star count this base published was inflated `23×`, and a name sweep proves it was not a namesake

🔴 **Published by this base at cycle 2 (`~9k★`) and cycle 3 (`~12k★`):** [`satvik314/educhain`](https://github.com/satvik314/educhain).

🟢 **Measured, `search/repositories` with a `repo:` qualifier — exact integer: `★388`.** MIT (`1,092 B`, blob `b46290b36e7f`), last push `2026-05-29`.

🔵 **The obvious defence is a namesake — so it was tested.** A `search/repositories` sweep on the bare name `educhain` returns, in full: `satvik314/educhain` `★388` · `lukepark327/educhain` `★22` · `SailFish-Finance/educhain-ai-agent-kit` `★6` · `EDUchain-US/EDUchain` `★3` · `Tuprott991/Educhain-AI` `★4` · `Kaustubh-1-7/crowdRaise-educhain` `★0`. 🔴 **No repository of that name anywhere exceeds `★22`.** The `~9k`/`~12k` figures were not a near-miss on a different repo; there is no candidate they could describe.

🔴 **This is the same defect class the technology base recorded** (`prior cycles' star counts were pipeline-inflated`) and it is now confirmed independently in education. 🟢 **The row survives on its licence and is corrected on its count** — MIT and genuinely useful for document-to-course generation, but it is a `★388` project with a six-month-stale tree, and it must never again be presented to a client as a `12k★` one.

## `T882` — an MIT root is not an MIT tree, and this pass found a non-OSI grant inside a `43,376★` MIT repository

🟢 [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) — `★43,376`, pushed `2026-11-12`, root `LICENSE` **MIT**, `1,065 B`, blob `76abc5f13261`. 🟢 **Root grant confirmed, and the seven first-party sub-packages are MIT too** (`dsl`, `editor`, `generation`, `geometry`, `importer`, `renderer`, `storage` — each `1,065 B`).

🔴 **Then the tree was enumerated — `4,388` files — and it is not uniformly MIT:**

| Path in tree | Bytes | Grant on the bytes |
|---|---|---|
| `packages/mathml2omml/LICENSE` | `7,652 B` | 🔴 **LGPL** — vendored copyleft inside an MIT repo |
| `packages/@openmaic/renderer/font-licenses/ARPHIC-PL.txt` | `6,863 B` | 🟡 **ARPHIC Public License** (copyleft-style font grant) |
| `packages/@openmaic/renderer/font-licenses/OFL.txt` | `4,998 B` | 🟢 SIL Open Font License |
| `packages/@openmaic/renderer/font-licenses/ZcoolHappy-LICENSE.txt` | `817 B` | 🔴 **Not an OSI licence at all** — see below |

🔴 **`ZcoolHappy-LICENSE.txt` is a bespoke Chinese-language font grant** (站酷快乐体, ZCOOL). Its operative terms, read on the bytes: **free perpetual use including commercial use** (`可免费商用，永久免费授权所有人使用`), but **the font's original name may not be changed** (`禁止...改变站酷免费字体的原有名称`), **the font may not be resold as a product or used to profit as a product** (`禁止任何人将站酷免费字体作为商品进行转售及牟利`), and **attribution to the typeface designers is retained** (`造字者保留署名权`).

🟡 **What that means for an engagement.** The restrictions are mild and compatible with ordinary client delivery — but they are **not MIT**, they are **not OSI**, and they are written in a language the rest of the audit chain is not reading. Shipping OpenMAIC's `renderer` ships this grant. 🟢 **Deliverable rule: if the renderer goes to a client, carry the three font-licence files with it and keep the font names intact.** 🔴 **And an education deliverable must never resell the bundled font as an asset** — which a "template pack" or "font bundle" line item would do.

🟢 **`T882` extends `T861` (read the dependencies) and `T875` (a licence file may quote others) one layer further: read the TREE, and read it in every language it is written in.** This base has now been bitten by Spanish (`p790`, defects 1–3) and Chinese (this pass) on the same axis.

## `T883` — "EMEA" as one bucket hid an entire continent, and the gap was in the QUERY, not the territory

🔴 **The regional sweep for EMEA returned, on Africa, nothing.** The honest summary of that result was: *"For Africa, I found no useful source in these results"* and *"Africa coverage is essentially absent."*

🟢 **A single targeted query returned five named instruments and a continental strategy.** They are recorded in `intel/market.md` under `EMEA`. 🔴 **So the finding is not "Africa has no AI-education policy" — it is that a query which buckets Europe, the Middle East and Africa into one term returns European results and calls it EMEA.**

🔵 **Why this is a method finding and not a note.** This base's brief asks that an empty region be written down explicitly, because *"an informed gap is information, while silence looks exactly like coverage."* `T883` adds the failure mode one level up: **a region that is ANSWERED but answered only in part looks exactly like a region that is covered.** A composite region must be probed by its parts before any gap over it is declared. 🟢 **EMEA is now probed as Europe · Middle East · Africa separately, and the Africa row is placed.**


# Current trends — `p790`

🟢 **Byte-verified** claims concern repositories, grants, `sha`s and dependency manifests.
🔴 **Search-channel testimony** covers every market, adoption and regulatory figure (`T844`).

## `T875` — A licence file may QUOTE other licences, so substring grading is unsound in both directions

🔴 **The finding that reversed one of this base's own published verdicts, and it is a method change
rather than an erratum.** This base published, twice, that
[`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) is **PROPRIETARY**, reasoning that *"a
`39,890 B` licence file is not evidence of an open grant — it is evidence of a long one."*

🟢 **Measured.** The file is served at **`license.txt`** (lowercase, `.txt`) and is a licence
**anthology** with its own table of contents:

| § | Contents | Whose terms |
|---|---|---|
| 1 | Overview | nextSIS |
| 2 | **nextSIS GNU General Public License Version 3** | 🟢 nextSIS's own grant — **full operative GPL-3.0**, `Version 3, 29 June 2007` |
| 3 | CodeIgniter License | EllisLab, Inc. — a bundled framework |
| 4 | Twitter Bootstrap License | a bundled front end |

🔴 **The single `All rights reserved.` in `39,890` bytes is at line `703` — the second line of §3,
`Copyright (c) 2008 - 2011, EllisLab, Inc.` — and EllisLab's very next clause reads `You are
permitted to use, copy, modify, and distribute the Software`.** The line the verdict rested on is
not nextSIS's, **and the licence it belongs to is not proprietary either.**

🔴 **Then the same file defeated two more probes, differently each time.** A fresh instrument built
for this pass graded it **`AGPL-3.0`**, because **GPL-3.0's own §13 names the GNU Affero GPL**; and
its NonCommercial gate fired, because **GPL-3.0 §6 uses the word "noncommercial"**. 🔵 **Three
probes, three different wrong answers, one cause.**

🟢 **The rule, and it generalises past this row.** Grade by **anchored title lines** — a licence
title occupying its own line — and **report the set, not a family**. A file containing `N` licence
titles is an **`ANTHOLOGY`** and has no single family. `nextSIS` reads
`ANTHOLOGY[GPL-3.0, +CodeIgniter]`; **`odoo/odoo`**, the most-cited vertical platform in this sector,
reads **`ANTHOLOGY[LGPL, GPL-3.0]`** at `43,529 B` — so the education-ERP tables that call Odoo
"LGPL" are stating one of its two families.

🟢 **And read the tree, never a filename list.** `raw.githubusercontent.com` is **case-sensitive**;
`p789` missed this grant on `11` candidate paths and this pass missed it on `10`:

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/OWNER/REPO /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -iE 'licen|copying|legal|terms|notice'
```

🔵 **Relationship to the base's existing laws.** This is `metabase`'s *split-by-directory* finding
**split by section instead**, and it is `T845` (*"length is not a verdict"*) proved at **both** ends
in one pass: **`39,890` bytes was not proprietary, and `19` bytes is a real grant** —
[`frappe/education`](https://github.com/frappe/education) serves exactly `License: GNU GPL V3` and
nothing else.

## `T876` — Brazil mandated a human in the loop, not a ban, and the research channel served the superseded draft

🔴 **`Parecer CNE/CP nº 15/2026`, homologated `2026-11-10` and published in the `DOU` `2026-11-11`
(reported; primary act NOT read), gives Brazilian institutions `12` months to adapt.** Under
**`Lei nº 9.131/1995`** a CNE parecer binds only once the Minister's homologation act is published,
so the clock starts there and not at the `2026-09-01` approval.

🔴 **The version the CNE approved on `2026-09-01` prohibited AI correction of essays and
dissertative questions outright. MEC judged that too restrictive and released the use.** At least
one outlet still reports the prohibition as current, and **this base's first reading of the research
channel took that superseded draft as the rule.** 🟢 The error was caught by noticing that sources
*disagreed* and chasing the disagreement to its history — not by a better query.

🟢 **The homologated position:** AI **may assist** correction as a first filter; **the mark is
reserved to the teacher**; **no student may be penalised on an AI detector's output alone**;
**educação infantil and anos iniciais (to `5º ano`) may not use AI tools unsupervised**; individual
use is permitted from **ensino médio** upward.

🟢 **Commercially this is the best news in the LATAM block.** A human-in-the-loop grading pipeline
with a reserved teacher decision is what `P788-1` already is. 🔴 **What Brazil forbids is the
autograder that assigns the mark** — the product most vendors lead with. 🔵 **Convergence worth
naming:** Florida bars AI on graded work unless the instructor permits; New York would gate direct
student use by grade; the EU regulates assessment as Annex III high-risk; Brazil reserves the mark.
**Four jurisdictions, one regulated surface — and now an age dimension too.**

🔴 **Standing caution this trend creates.** `T858`/`p758` recorded the research channel handing this
base a **superseded federal deadline**. It has now happened again, in a different country, on the
single most decision-relevant rule in the region. 🟢 **When sources disagree about a regulation,
the disagreement is usually a *version history*, not noise — look for the draft before the
amendment.**

## `T877` — A category error can FABRICATE a region as easily as it can hide one

🟢 **`p789`'s best result was finding that Japan's "measured gap" was a category error:** the supply
was real and sat in `校務` (school administration), not tutoring. 🔴 **This pass found the same error
running backwards, and it would have produced a false placement rather than a false absence.**

🔴 **`p789` declared Tanzania a measured gap at `0`.** `elimu AI Tanzania` returns **`2`**
repositories, and one of them —
[`sangadanson1-dot/-Vet-IDEA-TZ`](https://github.com/sangadanson1-dot/-Vet-IDEA-TZ) — **is MIT,
byte-verified at `1,067 B` · `238c1bbb3bc0`**. Grant: clean. Education: present. AI: present.
Country: Tanzania. **On every field this base indexes, it discharges the gap.**

🔴 **Read in Swahili, it serves `wafugaji na wataalamu wa mifugo` — livestock keepers and veterinary
professionals — teaching `afya ya wanyama, magonjwa, chanjo, lishe`: animal health, disease,
vaccination, nutrition.** 🟢 It is real, granted, AI-bearing education. **It is veterinary extension
education, and this base is about school education.**

🔵 **The asymmetry that makes this worth a trend of its own.** A category error in the *hiding*
direction costs a pass and is recoverable — Japan was rescued. **A category error in the
*fabricating* direction is not self-correcting**: the gap closes on the shelf, the region stops being
queried, and the first time anyone finds out is when an engagement opens the row. 🔴 **`elimu` means
*education* in Swahili and the word does not distinguish schooling from extension work** — exactly
the semantic trap `T867` recorded for Korean `교육`, but with the trap set in the opposite direction.

🟢 **The gate, added to `P788-8`:** after a grant verifies, **read what the artefact teaches and to
whom, in its own language, before placing it.** A grant gate is not a relevance gate (`T873`) — and
a *relevance* gate is not a *sector* gate either.

## `T878` — A declared ecosystem is not a built one, and the honest ones say so

🟡 **[`jinlize-tech`](https://github.com/jinlize-tech/education-ai-ecosystem) is the largest
permissively-granted education-agent repository set this base has ever measured, and the claim is
true:** **`132`** repositories under the owner, **`100` of `100`** sampled carrying **Apache-2.0**,
hub licence byte-verified at `11,358 B` · `cfc7749b96f6`. The hub declares **`130` products — `97`
Skills and `33` Agents**.

🔴 **And its own README states what it has not got:** `WorkBuddy platform validation: 0/130,
NOT_EXECUTED` · `GitHub Release verified: 30/130` · *"They do not prove WorkBuddy parsing,
installation, model behavior, review, or publication."* Sampled agent repositories read
`Agent | … | Planned / 待研发` — **planned / to be developed**.

🔵 **Writing "`33` education agents, Apache-2.0" was the single largest padding opportunity available
to this base this pass, and the repository itself supplied the refutation.** 🟢 **It is carried as
`2` byte-verified rows plus a measured org count** — see `agents/top.md`.

🟢 **What it is genuinely worth is the taxonomy, and that part needs no validation at all:** an
`8`-centre decomposition of the education **back office** — 招生营销 (admissions-marketing),
教学教研 (teaching-research), 教务运营 (academic-operations), 财务运营 (finance), 人力组织 (HR),
校区标准化 (multi-campus standardisation). 🔵 **It is the first *organisational* map of education AI
this base holds** rather than another list of tutors, and it agrees with `T858` and the OECD: the
money is moving to the back office.

🔵 **The general rule for this base:** when a repository set is large and uniformly licensed,
**measure the org on the claim channel, sample it on the byte channel, and then read what the
repositories say about their own readiness** — because a set this size is usually a *plan* expressed
as repositories, and a plan is intelligence of a different kind than code.

## `T879` — In education ERP the permissive layer is not narrow, it is EMPTY — and two vendor claims do not survive a probe

🟢 **`6` education ERP / SIS platforms probed on the byte channel this pass. `0` carry MIT, Apache-2.0
or BSD.**

| Platform | Claimed | Measured on the bytes |
|---|---|---|
| **OpenEduCat** | LGPL-3 | 🟡 **LGPL** `8,241 B` — 🟢 **the only vendor claim that holds** |
| **Odoo** | LGPL | 🔴 **`ANTHOLOGY[LGPL, GPL-3.0]`** `43,529 B` — two families, not one |
| **Frappe Education** | "based on ERPNext" | 🔴 **GPL-3.0 by reference, in `19` bytes** — and **not** the AGPL-3.0 of its sibling `frappe/lms` |
| **openSIS Classic** | GPL-2.0 | 🔴 **no licence served** (`8348cd069aa2` — reproduced this base's own prior measurement as an unplanned 11th control) |
| **Fedena** | **Apache-2.0**, per a competitor's comparison table | 🔴 **REFUTED — no licence served on `10` paths** |
| **GegoK12** | **MIT**, plus *"modification, rebranding and resale are permitted"* | 🔴 **REFUTED — `gegok12/gegok12` does not exist (`rc=128`), and a GitHub-wide search for `gegok12` returns `13` results, none of them this product** |

🔴 **The most permissive claim in the entire education-ERP market has no locatable source.** 🟢 **An
MIT claim with no repository is not a finding** — the same rule as *a 404 is not a finding*, applied
to a licence rather than a URL.

🟢 **The architectural conclusion, now measured on the administrative side as well as the
instructional one.** `T852` established that the famous **LMSs** are copyleft. This pass establishes
that the **SIS/ERP** layer is too — including `nextSIS`, whose correction *adds* a copyleft open SIS
rather than a permissive one. 🔴 **So the AI layer in this sector is always an integration, never an
embed.**

🔵 **Which makes the MIT attachment points this base holds worth more than they look:**
`brightspace-d2l-mcp`, `classcharts-agent` (read-only), `teams-facultad-mcp`,
`LearningLocker/xapi-service`. 🟢 **An MIT MCP server in front of a GPL platform is the whole
architecture, not a convenience** — and it is the one shape that is deliverable in every region this
base covers.

## `T869` — In education the grant is often TWO grants, and a single-file probe reads it as none

🟢 **Education repositories ship code *and* teaching content, so they licence them separately** —
and the split is structural to the industry, not incidental. Measured this pass:

| Repo | Code | Content | How it is served |
|---|---|---|---|
| [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | 🟢 MIT `1,102 B` · `c42f19d27c4d` | 🟢 CC BY 4.0 `925 B` · `738b8fc14a61` | **Two files** — `LICENSE-CODE` and `LICENSE-CONTENT` |
| [`VictorOsondu/ai-adoption-education`](https://github.com/VictorOsondu/ai-adoption-education) | 🟢 MIT | 🟢 CC BY 4.0 | **One file**, two headed sections, `752 B` |

🔴 **Both were reported `NOASSERTION` or unlocatable by the claim channel, and both are usable.**
The first defeated this pass's probe entirely: GitHub asserted `MIT` while the byte channel found
**no licence on 11 filename paths**, because the file is named `LICENSE-CODE`. The second was
graded `CC` by a first pass that read only its opening heading and missed the MIT section below.

🟢 **The operative consequence is a question, not a flag.** For an education asset the right question
is never *"what licence is this repo?"* but **"what licence covers the code, and what licence covers
the material?"** — because the content grant is the one that decides whether a client may publish
derived worksheets, and `NC` on the content bars the engagement even when the code is MIT
(see [`nahisaho/teacher-genai-playbook`](https://github.com/nahisaho/teacher-genai-playbook),
CC BY-NC 4.0). 🔵 This is the same shape as `T864` (`paes-mcp`: MIT code, third-party exam corpus)
and `764-C`/`metabase` (split by directory) — **three different mechanisms, one lesson: the grant has
a scope, and the scope is part of the grant.**

## `T870` — Japan's supply gap was a CATEGORY error, and `T867` needs amending

🔴 **`p788` measured Japan at `3` repositories in Japanese and called it this base's only *measured*
rather than suspected gap** — a gap that had already survived translation into the local language.
🟢 **It did not survive a change of *category*.** The query `校務 AI` (*kōmu* — school
administrative duties) returns **`5`** repositories, `塾 AI 学習` (cram-school learning) returns
**`7`**, `学習指導要領 AI` (national curriculum guidelines) returns **`2`**, and two of those carry
clean MIT grants, including a full `12`-grade curriculum tree.

🟢 **`T867` said supply gaps in this base are *vocabulary* gaps. Amend it: some are *taxonomy*
gaps.** Translating "tutoring agent" into Japanese was correct and still found almost nothing,
because **Japan is not publishing tutoring agents.** It is publishing school administration and
curriculum alignment. The missing step was not a dictionary but a question: *what would this
country's teachers actually automate first?*

🔵 **And the answer differs by country in a way that is now measured, not asserted:** India publishes
**curriculum-specific tutors** (NCERT/CBSE), China publishes **evaluated multi-agent classrooms**
and commercial derivatives, Korea publishes **tutoring APIs**, Japan publishes **administrative
workflow and curriculum alignment**. 🔴 A single "APAC education agent" search term cannot find all
four, and a pass that uses one will report three absences.

## `T871` — Africa's curriculum supply is large and almost entirely ungranted

🟢 **`WAEC AI tutor` returns `35` repositories.** 🔴 **`32` of them serve no licence.**
The same ratio holds for South Africa: `CAPS curriculum South Africa AI` → **`10`**, of which **`2`**
carry a grant. Ghana: **`1`** repository, ungranted. Tanzania (`NECTA`): 🔴 **`0`**.

🟢 **The finding is the ratio, not the count.** `p788` recorded African curricula beyond Kenya and
Morocco as *"none found"*. The supply was there; what is missing is **licensing practice**, not
engineering. 🔵 And the ungranted repositories include the *best-designed* ones —
[`7irelo/aptiverse`](https://github.com/7irelo/aptiverse) (CAPS practice tests with **auditable
marking**, the highest-starred of the set) and
[`tosinamuda/teacher-agent-itu-hackathon`](https://github.com/tosinamuda/teacher-agent-itu-hackathon)
(**teacher-in-the-loop**, from the ITU AI for Good Lab). **Auditable marking and
teacher-in-the-loop are the two design choices this base recommends in every pattern it
publishes, and both are sitting in African repositories without a grant.**

🟢 **The actionable consequence:** for West and Southern African engagements the deliverable is an
**upstream licence request campaign**, not a build. Three MIT WAEC tutors and two CAPS tools exist
today; a handful of emails could double the usable set. 🔴 Until then the permissive African base is
`5` repositories plus the `66`-repo `elimu-ai` ecosystem.

## `T872` — A first-layer dependency audit is a screen, not a clearance

🟢 **`p788` audited `473` direct dependencies across `7` repositories and found `nbgrader` clean.**
🔴 **At layer 2, `nbgrader` is not clean** — `65` new transitive packages bring **MPL-2.0**
(`requests` → `certifi`) and **LGPL-2.1** (`jupyter-client` → `paramiko`).

🟢 **Both are weak copyleft and neither bars the pattern.** MPL-2.0 is file-level and triggers on
modifying `certifi`'s own files; LGPL-2.1 permits dynamic linking. `P788-1` remains deliverable.
🔴 **What changes is the sentence a client is told.** "Entirely permissive dependencies" was true of
layer 1 and is false of the graph. The accurate claim is narrower and survives diligence:
*MPL-2.0 and LGPL-2.1 are present at layer 2, both weak copyleft, neither triggered by this
deployment shape.*

🔵 **Two mechanical notes worth carrying.** First, **PEP 639 `license_expression` decided `28` of the
`65`** — a classifier-only reader would have called them `UNDECLARED`, which is the defect `p788`
recorded in its own instrument. Second, **SPDX compound expressions are mis-read in opposite
directions**: `packaging` is `Apache-2.0 OR BSD-2-Clause` (**an election** — pick one) while
`prometheus-client` is `Apache-2.0 AND BSD-2-Clause` (**cumulative** — both apply). Reading `AND`
as a choice under-states the obligation; reading `OR` as a conjunction over-states it.

🔴 **Declared boundary:** depth `3+` is unmeasured, the npm-side graphs are unmeasured at layer 2,
and these are declared ranges from registry metadata rather than resolved versions from a lockfile.

## `T873` — `tutor` is a polluted search term, and a grant gate is not a relevance gate

🔴 `tutor AI created:>2026-10-01 stars:>30` returns **`39`** repositories, and **`5` of the top `8`
are one repository re-published under five owners** — `apimartyvp957u6/api-proxy-tutorial`,
`apimartpx0d7edg8/llm-gateway-tutorial`, `apimartat5/llm-api-tutorial`,
`apimartmk8/multi-model-api-tutorial`, `apimartc30lq1/unified-ai-tutorial` — at `78`–`91★` with
byte-identical descriptions advertising a commercial API relay. 🔵 **They are not education at all;
they match because `tutor` ⊂ `tutorial`.**

🟢 **The instructive part: one of them serves a perfectly valid MIT licence** (`1,181 B` ·
`9c1378a7528b`). **A real grant on an irrelevant repository.** This base's grant gate (`P788-7`)
would pass it; only a human or a relevance gate rejects it. 🔴 Star-sorted education queries must
exclude the `tutorial` stem, and **a licence check is not evidence that a row belongs in the base.**

## `T874` — The school-operations category is a solver with an approval gate, not a chatbot

🟢 **The category `p788` recorded as empty has five permissive rows, and they agree with each other
about architecture.** Two independent rows put a **real constraint solver** at the centre —
Timefold ([`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study))
and OR-Tools ([`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable)) — with the LLM at the
edges, turning plain-English policy into constraints and explaining rejections. A third
([`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent)) puts a **human
approval step** before any schedule is written. A fourth
([`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent)) attaches to a live
school MIS **read-only**.

🟢 **Nobody in this category is asking a language model to produce a timetable**, and that is the
finding. Scheduling is a constraint-satisfaction problem with hard feasibility requirements; an LLM
that invents a plausible-looking timetable produces a school day that does not work. 🔵 The same
division of labour — deterministic core, LLM at the edges, human gate before write — is what
`P788-1` arrived at independently for grading. **Two unrelated categories converging on one
architecture is the strongest design signal this base has.**

## `T861` — A repository grant is not a dependency grant, and 4 of 7 permissive leaders carry copyleft

🟢 **Byte-verified across 7 repositories and 473 declared direct dependencies.** `ACTION p787-D`
discharged, and it is the most consequential measurement this base has made about its own
recommendations.

| Repo | Repo grant | Direct deps | Copyleft in the first layer |
|---|---|---|---|
| `oppia/oppia` | Apache-2.0 | `171` | 🔴 **`angular-shepherd` — AGPL-3.0** |
| `learningequality/kolibri` | MIT | `32` | 🔴 `zeroconf-py2compat` LGPL-2 · `json-schema-validator` LGPL |
| `HKUDS/DeepTutor` | Apache-2.0 | `27` | 🔴 `pyte` LGPL-3.0 |
| `THU-MAIC/OpenMAIC` | MIT | `181` | 🔴 `mathml2omml` LGPL-3.0-or-later · 🟡 `jszip` `MIT OR GPL-3.0-or-later` |
| `CAHLR/OATutor` | MIT | `43` | 🟢 none |
| `jupyter/nbgrader` | BSD-3 | `18` | 🟢 none |
| `zijinz456/OpenTutor` | MIT | `1` | 🟢 none |

🔴 **The sharpest row is Oppia.** This base files Oppia under *"build on these, link them, **ship
them in client code**"*. It depends on an **AGPL-3.0** front-end library, and AGPL's trigger is
network delivery — which is exactly how a browser bundle reaches a learner.

🔵 **Three consequences a studio should act on.**
1. 🟢 **The flagship pattern survives unchanged.** `nbgrader` and `OATutor`, the two components
   `P788-1` rests on, are the two that audit clean. That was luck; it is now a documented reason.
2. 🟡 **LGPL is survivable, AGPL is not.** Python and Node both link dynamically, so Kolibri and
   DeepTutor stay usable provided the LGPL component remains replaceable and its source available.
   Oppia's AGPL dependency must be removed or replaced, not managed.
3. 🟡 **A dual grant is permissive only once you elect it.** `jszip` is `MIT OR GPL-3.0-or-later`.
   Election is a decision with a date and an author, not an assumption.

🔴 **And state the limit of the measurement honestly: this is the FIRST dependency layer only.**
Transitive dependencies were not audited. The first layer was already enough to change four rows,
so the second will change more.

## `T862` — The EMEA agent gap was an artefact of English-only querying, and it is refuted

🔴 **`T856` is REFUTED, not refined.** `p787` recorded: *"no European-origin education agent
repository surfaced … Europe is building the substrate and not the education layer on top of it."*
🟢 **Querying the same slot in the languages Europe actually writes in returned agents on the first
attempt**, and six are byte-verified in `agents/top.md`:

| Query | Language | Result |
|---|---|---|
| `tutor education AI Germany France Netherlands Spain` | 🔴 English | **`0`** |
| `onderwijs AI agent` | 🟢 Dutch | **`1`** — `onderwijsin/agents`, MIT |
| `tuteur IA education` | 🟢 French | **`9`** — incl. `sherpa`, `dowze`, `parcours-maths-ia`, all MIT |
| `KI Unterricht Agent` | 🟢 German | **`2`** — incl. a Swiss LP21-curriculum agent |

🟢 **Plus `elimu-ai`: 66 repositories, MIT, an African education ecosystem pushed this week** — and
**this base was already citing it** at `agents/trending.md:24964` without ever placing it.

🔵 **The lesson generalises past Europe, and it is the same lesson as `T848`.** An instrument written
in English, against American naming conventions, with a star floor, will under-report every region
that is not the United States. This base has now been caught doing that **twice** — once on a
licence probe (`T848`, Spanish MIT read as no grant) and once on a discovery query (here). 🔴 **Both
times the under-reported regions were the two the base is explicitly told to serve.**

## `T863` — Six defects in one pass's own instruments, and four are biased against non-English grants

🟢 **Every one was caught by a control on a row this base had already published; none by inspection.**

| | Failure mode | How it showed up | Fix |
|---|---|---|---|
| 🔴 **NEW** | **Trailing-newline erasure** | `$(curl …)` strips the trailing newline, so **every** licence in the pass measured exactly `1 B` short — `11,407` against the recorded `11,408`, six for six | Bytes counted **on the file**, never through command substitution |
| 🔴 **NEW** | **Single-rendering translation matching** | The `T848` fix matched *one* Spanish rendering. `paes-mcp` says `partes sustanciales`; the probe required `porciones sustanciales` — **the repaired probe still scored a valid Spanish MIT as `UNGRADED`** | Every clause matched as a **set** of circulating renderings per language |
| 🔴 **NEW** | **Byte-wise accent blindness** | `SIN GARANT.A` cannot match `SIN GARANTÍA`: `grep` matches bytes, and `Í` is two of them, so `.` fails. 🔴 **The fix for language-blindness was itself defeated by the locale** | Patterns ASCII-only up to the first accent; locale declared explicitly |
| 🔴 **NEW** | **Fixed-window title search** | `p787` widened the title check to 5 lines for Odoo's line-3 deferral. `INGInious` defers to **line 9** behind a prose scope caveat, and graded `UNGRADED` — against a grant this base had already correctly recorded as AGPL-3.0 | The title is **found by scanning for a line that *is* a licence title**, at any depth. A fixed line budget is the wrong instrument and the next file will exceed any budget chosen |
| 🔴 **NEW** | **Abbreviation blindness** | `frappe/education` serves **19 bytes**: `License: GNU GPL V3`. Matching only expanded names scored a real grant `UNGRADED` | Abbreviations (`GPL`, `AGPL`, `LGPL`, `v3`) graded as titles |
| 🔴 **NEW** | **Metadata-field blindness** (dependency instrument) | PyPI's legacy `license` field is empty for modern packages, so `pydantic`, `tenacity`, `typer`, `jsonschema` and `packaging` all reported `NONE-DECLARED` — 5 false absences on the first dependency audit this base has ever run | **PEP 639 `license_expression`** read first, then classifiers, then the legacy field |

🔴 **Three of these six under-report non-English grants specifically**, and a fourth under-reports
short grants. 🟢 **The two corrections they produced on already-published rows:**

- **`luscitiosus/Dirigo`** — published as *"a Latin boast and no grant of any kind"*. The Latin is
  line 1; **lines 3–5 grant CC BY-NC-SA 4.0 in Spanish** with a link to the Spanish legal code.
  Still barred commercially, 🔴 **but the published reason was false** and NonCommercial is a harder
  bar than an absence.
- **`MyScript/MyScriptJS`** — published as a *"proprietary notice"* at `570 B`, left `UNGRADED`.
  The bytes are the **standard Apache-2.0 grant-by-reference boilerplate**, URL and AS-IS clause
  included. 🟢 **Removed from the unusable class.** It was dismissed for being short, which is
  precisely what `T845` forbids.

🔵 **Seven recorded failure modes have now become thirteen**, and the pattern across all of them is
one sentence: **a licence probe fails in whichever direction its author's defaults point.**

## `T864` — The grant covers the code; the corpus belongs to someone else

🟢 **Byte-verified, and it corrects a pattern this base shipped.** `goyanedelv/paes-mcp` is MIT —
and its licence text states in terms that the grant covers **the source code and the documentation
only**, and does *not* and *could* not cover the PAES question stems, figures and answer keys, whose
rights belong to **DEMRE, Universidad de Chile**. That material is included from freely published
official sources, for educational use, with attribution.

🔴 **`P787-3` was written as though the exam corpus were MIT.** It is not. The pattern is repaired as
`P788-3` with the boundary explicit.

🔵 **This is the third time this base has made the same mistake**, and it is now a rule rather than
an anecdote: `legalize-dev/legalize-pt` (MIT for a *different* repository, Portuguese statutes under
public-sector open data), `Dirigo` (CC BY-NC-SA for the code, BOE/BOC statutory texts excluded), and
now `paes-mcp`. 🟢 **In education this will be the normal case, not the exception** — exam items,
textbooks and curricula are the assets with rights-holders, and the repository that wraps them is
the cheap part. **Read the scope clause, and ask who owns the content** before costing a deliverable
on it.

## `T865` — Identical `HEAD` proves two addresses are one project, with no page read

🟢 **`ACTION p787-G` discharged mechanically.** `p787` recorded that the only evidence separating a
fork from a distinct project was the fork notice on the github.com page. 🔴 **That page returns `403`
this pass.** 🟢 `lehrer-tools/lehrer-agent` and `NikolasSchaeffner/lehrer-agent` both resolve to
`3ddcfbbabc560675914da9703f53101c1c4d5123` — **the same commit**. One German teacher agent, carried
by this base as two separate ungranted rows.

🔵 **This is a better instrument than the one `p787` asked for.** It needs no page, no API and no
licence fetch: `git ls-remote` already returns the discriminating value, and two addresses sharing a
`HEAD` are one project until proven otherwise. 🟢 **It is also cheap enough to run on every row**,
which the page read never was.

## `T860` — The page channel closed; the claim channel got better

🔴 **Channel status changed between `p787` and `p788`, and it must be stated rather than assumed.**
`github.com` and `api.github.com/repos/{owner}/{repo}` now return **`403`** through this session's
proxy for every non-attached repository — so `p787`'s page-read star counts cannot be reproduced by
the method that produced them.

🟢 **The replacement is better than what it replaces.** `search/repositories` with `repo:` qualifiers
is reachable and returns **exact integers**: DeepTutor `58,508`, OpenMAIC `43,365`,
`agent_skills` `6,813`, `hedyorg/hedy` `1,697`, Kolibri `1,176`, OATutor `279`, OpenTutor `175`.
🔵 **Every one reproduces `p787`'s rounded page figure** (`58.5k`, `43.4k`, `6.6k`, `1,697`, `1.2k`,
`279`, `175`), which both validates the new channel and retires the old one. 🟢 **Stars in this base
are now exact and dated, not rounded** — and still claim-channel, so still weaker evidence than a
licence byte.

## `T866` — South Korea binds education, so APAC is no longer the low-regulation region

🔴 **Search-channel, and it overturns this base's APAC position.** `p787` recorded APAC as *"the
region with the strongest open-source agent supply and the weakest binding regulation"*, naming
**Vietnam** as its one binding education hook. 🔴 **South Korea's AI Basic Act (Act No. 20676) took
effect `2026-01-22`** — a risk-based statute with mandatory transparency and impact assessment for
**high-impact AI**, and the high-impact category **names education explicitly**, alongside
healthcare, finance, employment and essential services.

🟢 **So the regional story is now: Korea and the EU both bind education; the US binds it state by
state; Japan does not bind it at all.**

| Jurisdiction | Instrument | Binding on education? |
|---|---|---|
| 🟢 **South Korea** | **AI Basic Act, Act No. 20676, in force `2026-01-22`** | 🔴 **Yes — education named as high-impact AI** |
| EU | AI Act Annex III point 3; Reg. (EU) 2026/1744 defers to `2027-12-02` | 🔴 Yes |
| Vietnam | 2026-07 high-risk sector list, citing automated assessment | 🔴 Yes |
| Japan | AI Promotion Act (2025); AI Basic Plan `2026-07-14` | 🟢 **No penalties, no risk tiers** |
| India | Amended IT Rules from `2026-02-20` | 🟡 Provenance labelling only |
| China | Sector measures; Cybersecurity Law AI clause from `2026-01-01` | 🟡 Not education-specific |

🔵 **Commercially this is the most actionable regulatory change in the pass**, because Korea's
statute is **already in force** while the EU's education obligations are 13 months out. An APAC
engagement in Korea is remediation work today.

## `T867` — Supply gaps in this base are vocabulary gaps

🟢 **Measured on the claim channel, `ACTION p787-F` discharged.** The same slot, queried two ways:

| Country | English query | Result | In-vocabulary query | Result |
|---|---|---|---|---|
| India | `tutor agent education India CBSE NCERT curriculum` | 🔴 **`0`** | `NCERT AI` | 🟢 **`330`** |
| Netherlands | `tutor education AI … Netherlands` | 🔴 **`0`** | `onderwijs AI agent` | 🟢 **`1`** (MIT) |
| Korea | — | — | `AI 교육 에이전트` | 🔴 **`20`, almost none relevant** |
| Korea | — | — | `학습 튜터 AI` | 🟢 **`12`, relevant** |
| Japan | — | — | `AI 教育 エージェント` | 🔴 **`3` — a real gap** |

🔴 **Korea carries a semantic trap worth recording:** **교육** means both *education* and *corporate
training*, so the obvious query returns agent-training **course material** — a Samsung practitioner
curriculum, "AI maestro" coursework — rather than education agents. The productive term was
**학습** (*learning*).

🟢 **Japan is the one gap that survived in-language querying**, which makes it this base's only
*measured* rather than *suspected* supply gap. Its best artefact,
`narumi-mase/osaka-lesson-dataset` (Osaka City Education Center lesson plans), serves **no licence**.

🔵 **The operating rule:** before recording a regional absence, query in the region's language and
in the region's own curriculum vocabulary — `NCERT`, `CBSE`, `PAES`, `LP21`, `CBC`, `Bac`. **A gap
found in English is a gap in the query.**

## `T851` — Tutoring is packaged as a *skill*, and the derivative arrived in six days

🟢 **Byte-verified, and now with downstream evidence.** `janestreet/agent_skills` (MIT, `1,120 B`,
`6,813★`) ships `socratic-tutor/` as a prompt-and-protocol directory: diagnostic, skill map at
levels 0–5, one question at a time, spaced review, final assessment. 🟢 **`nuwaves/socratic-tutor`
(MIT, `1,143 B`, created `2026-11-09`) is the same skill extracted as a standalone installable unit
with saved progress** — a third party re-packaged it within a week.

🔵 **Why this remains the cheapest viable unit of educational IP:** no runtime, no server, no model
dependency; reviewable by a curriculum specialist who cannot read code; versionable in git; portable
across whichever model the client already bought. 🟢 `myvipbackup2/china-k12-teacher-skills`
(Apache-2.0) is the same pattern applied to a national curriculum, and `onderwijsin/agents` (MIT) is
the Dutch one.

## `T868` — A localised derivative can be *less* usable than its parent

🟢 **Byte-verified, and new.** `dpaul0501/OpenVidya` is OpenMAIC *"redesigned for NCERT/CBSE"* — the
exact localisation move `P787-5` recommends. 🔴 **Its grant is AGPL-3.0, where OpenMAIC's is MIT.**

🔵 MIT permits relicensing a derivative under AGPL, so nothing improper happened. But the
consequence matters for a studio: **the India-localised classroom cannot be embedded in a client
deliverable the way its permissive parent can.** 🟢 **The practical reading: localise OpenMAIC
yourself from the MIT parent rather than adopting a copyleft fork of it** — and check the grant of
any localisation before treating it as a shortcut.

## `T852` — The permissive layer is narrow, and it is not where the famous names are

🟢 **Byte-verified across 38 foundational repositories this pass: 18 permissive, 18 copyleft,
2 EUPL-1.2.** The split follows institutional history, not chance.

| The names a client will say | Grant | The permissive repo that does the same job |
|---|---|---|
| Moodle | 🔴 GPL-3.0 | Sakai (ECL-2.0) · OpenOLAT (Apache-2.0) |
| Open edX · Canvas | 🔴 AGPL-3.0 | Sakai (ECL-2.0) |
| D2L Brightspace | proprietary SaaS | 🟢 `brightspace-d2l-mcp` (MIT) — attach, don't replace |
| H5P content types | 🔴 GPL-3.0 | `Khan/perseus` (MIT) |
| edx-ora2 assessment | 🔴 AGPL-3.0 | `jupyter/nbgrader` (BSD-3) |
| xAPI / learning records | — | 🟢 `LearningLocker/xapi-service` (MIT) — **rescued this pass** |
| Anki scheduling | 🔴 AGPL-3.0 | — 🔴 no permissive equivalent in this base |

🟢 `csev/tsugi` (Apache-2.0) remains the most useful licensing component in education open source,
because **LTI across a process boundary** lets permissive code serve a copyleft LMS without becoming
a derivative work of it.

## `T853` / `T854` — Regulation bifurcated, and assessment is the regulated surface everywhere

🔴 **Search-channel, carried and re-confirmed.** 🟢 **EU:** Regulation (EU) 2026/1744 (*Digital
Omnibus on AI*), OJ `2026-07-24`, in force `2026-07-27`, moved Annex III stand-alone high-risk —
education included — from `2026-08-02` to **`2027-12-02`**. 🔴 **Not** deferred: Art. 5 prohibitions
and Art. 4 AI literacy (live since `2025-02-02`, **including the emotion-recognition ban in
education**), and Art. 50 transparency from `2026-08-02`. The Commission's own FAQ confirms
supervision and enforcement rules apply from `2026-08-02`, and that the AI-literacy duty already
applies; **Art. 4 is enforced by national market surveillance authorities, not the AI Office.**

🟢 **North America is enacting now, not pending:** **Idaho, Maryland, Oklahoma and Virginia** all
enacted education-specific AI measures in 2026; **Maryland SB 720 / HB 1057** direct the state
education department to issue guidance and require local AI policies; **California AB 1159** bars
using student data to train AI models; **Ohio's** district AI-policy mandate had a July 2026
deadline; **North Carolina** defended a **`$10M`** earmark in **Senate Bill 1006** to fund Khanmigo
tutoring statewide; **New York City** issued traffic-light guidance in March 2026. 🔴 **Do not quote
tracker totals** — `134` bills / `31` states and `68` / `27` circulate simultaneously, and guidance
counts range `33`–`35+`. **Cite the bill.**

🟢 **One architecture satisfies every jurisdiction that regulates assessment** — EU Annex III
(admissions, learning outcomes, education levels, **exam proctoring**), Korea (high-impact),
Vietnam (automated assessment), Oklahoma (AI used **solely** for grading, discipline or promotion),
New York A 9190 (grade floor): **AI proposes, a named human decides, and the system keeps an audit
trail joining the proposal, the evidence and the decision-maker.** 🔵 The word doing the work in
Oklahoma's statute is **"solely"** — it regulates *autonomy*, not assistance, so human-in-the-loop
is the product rather than a compliance tax. `jupyter/nbgrader` (BSD-3, **and `0` copyleft
dependencies**) already has that shape, which is why it anchors `P788-1`.

## `T855` — LATAM adoption has outrun LATAM governance by about 60 points

🔴 **Search-channel.** Teacher AI use in the past year (TALIS 2024): **Brazil `56%`, Chile `55%`,
Colombia `53%`, Costa Rica `52%`** against an **OECD average of `36%`**. UNESCO's observatory launch
reports **more than `50%`** of teachers already using these tools in countries such as Chile and
Brazil, while **fewer than `10%`** of regional institutions have formal guidelines. `87%` of regional
universities use AI, **`26%`** have a strategy, **`9%`** evaluate it (UNESCO IESALC); in Brazilian
schools `53%` of administrators use AI and **`22%`** report any guidelines (Cetic.br).

🟢 **New this pass, and it changes the regulatory read:** general AI bills are now **moving** —
**Brazil's comprehensive AI bill is in the Chamber of Deputies** (so the text can still change), and
**Chile has a government-sponsored risk-based bill** tied to its forthcoming data-protection
authority. 🔴 **Mexico remains the laggard: multiple bills introduced, none enacted.** 🔴 **Still no
AI-in-*education* statute in Brazil, Mexico or Chile** — the governing layer remains UNESCO-convened
soft governance. A regional index (October 2026) adds that all `20` countries offer postgraduate AI
programmes, `65%` have specialised research centres, and **more than half have incorporated AI into
school curricula**; Brazil holds **`87.7%`** of the GPUs in that study's coverage.

🔵 **The strategic reading is unchanged and now better evidenced.** This is not a market to be
*introduced* to AI — that already happened, bottom-up, through teachers. It is a market that needs
its existing, ungoverned use made defensible. The buying trigger is institutional risk and the
readiness gap, not a deadline.

## `T858` — Purpose-built is displacing general-purpose, and the commits agree with the commentary

🔴 **Search-channel.** The OECD's 2026 Digital Education Outlook recommends moving **beyond
general-purpose AI tools toward purpose-built educational AI** designed for durable learning gains;
1EdTech frames 2026 as the shift **from experimentation to governance**.

🟢 **Byte-verified corroboration, which is the useful part — and it got stronger this pass.** Of the
30 agents new to this base, the ones with traction are curriculum- and instrument-specific rather
than general: an NCERT/CBSE classroom, a PAES admissions MCP server, a Swiss LP21 lesson planner, a
Mexican Sign Language tutor, a Greek etymology tutor with an MCP server, a storybook **reading-level
model**, a Socratic protocol extracted as an installable skill. 🔵 **Nothing in this pass's new
supply is a general-purpose chatbot.**

## `T859` — A national AI policy was withdrawn for citing sources AI invented

🔴 **Search-channel, carried.** South Africa's draft National AI Policy was gazetted as **Notice 3880
of 2026 on `2026-04-10`** and **withdrawn on `2026-04-26`** by Minister Solly Malatsi, after
fabricated, AI-hallucinated citations were found in its reference list — reportedly **at least 6 of
its 67** academic citations. One source records abrogation on `2026-04-27`, so 🔴 **cite both
dates**. A seven-person panel is reviewing it with no published timeline; the Department of Basic
Education's **National AI in Education Framework** remains 🔴 **unpublished, with no timeline**.

🔵 **Keep this row.** It is the most persuasive provenance argument available in an education
engagement: the failure mode was not a model hallucinating in a classroom but **an AI-drafted
governance document failing its own review**. 🟢 **And this pass adds the component that answers it:**
`SeydinaBANE/sherpa` (MIT, EMEA) is a tutor built on **grounded RAG with citations** — provenance as
an architectural property rather than a policy promise.
