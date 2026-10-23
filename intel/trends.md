---
industry: education
region: Global
updated: 2026-10-23
---

## 🆕 `p408` · 2026-10-23 — a fork that FROZE an abandoned grant, India's **MIT** DPI going stale, and eight legs that returned nothing unshelved

🔵 **Dating note.** Every probe, clone, licence read and search leg below was run on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fourteenth pass dated today**, after `p395`–`p407`.

🟢 **This is a RESEARCH pass, not an instrument pass.** `p405`–`p407` were all repairs to this base's own measurement layer. This one runs the prescribed brief — four global legs and one leg per region — and reports what the supply and the regional instruments actually returned, including where they returned nothing.

### 🔴 Trend: a grant is a property of a **ref**, not of a project — and this pass has the first specimen where BOTH answers are right

🔴 **Every licence trap this base carries is a variant of "the grant was read in the wrong place."**
A grant one directory down (`openSIS-Classic`, `docs/License.txt`). A grant at `LICENSE.txt` rather
than `LICENSE` (`ai-shifu`, `tutor`). An AGPL text sitting inside a file labelled GPL
(`moodle-local_copilot`, §13). A grant at the submodule pin rather than the superproject
(`gate-pin-grant`). In every one of them there is a single correct answer and a reader who missed it.

🟢 **`p408` adds a class where there is no such answer.** `project-sunbird/project-sunbird.github.io`
is **MIT** today and was **AGPL-3.0** until `006b8246` on **2018-06-21**; a fork whose HEAD is
**2018-03-27** carries the AGPL text with a **byte-identical blob sha**. Both repositories report
their licence correctly. Both badge-reads are right. **The project has two grants and the ref
decides which one you got.**

🔵 **Why this is a trend and not an anecdote.** Three forces now push education repositories through
relicensing: public-money DPI programmes that need permissive terms to be adopted across
jurisdictions (Sunbird's own 2018 MIT switch is this), the AI-extension wave rebasing education
plugins onto platform grants they did not originally carry, and the single-maintainer tutor supply
this base has been cataloguing since `p385`, where a licence is changed as casually as a README.
🔴 **The operational consequence is a dating requirement on the licence column itself:** every
licence cell on these shelves is *"the grant at the ref we read, on the date we read it"*, and a
fork — even a dormant one — is a **separate licence fact**, never an inherited one.

🟡 **The second trend this pass measures: the grant is no longer the scarce thing — maintenance is.**
Sunbird ED is MIT at national-platform scale, which is the licence outcome
[`repos/foundations.md`](../repos/foundations.md) opens by saying education does not get; and its
portal is **311 days** without a commit, its mobile app **399**, and one of its named repositories
no longer resolves. 🔵 The classic education trade was *current code, hostile grant* (Moodle, Open
edX, Canvas). This is the **inverse**, and it prices differently: a permissive-but-stale base is a
fork-and-maintain engagement, and the cost lands in the staffing plan rather than in legal review.

## 🆕 `p407` · 2026-10-23 — the instruments are now the thing most likely to be wrong

🔴 **Trend: this base's measurement layer has overtaken its subject as the source of error.**
Three of this pass's four findings are defects in **instruments**, not in the market — a frozen
population, a spelling-bound date pattern, and a possessive apostrophe — and each one had a
committed instrument that already knew the right answer. 🔵 **The lesson generalises past this
KB:** an agentic pipeline that grades its own corpus accumulates *checks that cannot fail*, and
nothing in a green run distinguishes those from checks that pass. 🟢 **The cheap counter-measure
is mutation**: five of six mutations against `p407`'s own suite reddened a named control, and the
sixth revealed that the suite's imported classifier was not load-bearing on any published figure.

🔵 **For an engagement this is a sellable practice, not an internal note.** A client running
LLM evaluation or compliance checks has exactly this failure mode, and *"show me a mutation that
makes your green test red"* is a one-day audit that finds it.

## 🆕 `p407` · 2026-10-23 — EMEA's education clock has 14 months on it, not zero

🔴 **The market's majority reading is wrong, and this base was repeating it on its own
opportunity row.** Annex III education obligations apply from **2027-12-02** — the Digital Omnibus
(in force **2026-07-27**) deferred them — while **2026-08-02** is the **Article 50** transparency
date only. 🔵 **A sixth independent sighting of the wrong date arrived this pass**, in an
otherwise current source, which is what a majority misreading looks like: the client's installed
adviser has probably given them the wrong deadline.

🟢 **So the EMEA pitch inverts.** It is **not** "you are already non-compliant"; it is
"you have ~14 months, and conformity work ports to Vietnam's Decision 33 and Brazil's PL 2338/2023
because all three are risk-tiered." 🔴 **And `2026-08-02` still binds for transparency**, so a
chatbot-facing deployment has a live obligation today even though the high-risk tier does not.

## 🆕 `p407` · 2026-10-23 — the agent surface is moving OUT of the LMS

🟢 **New direction, first specimen read this pass.**
[`microsoft/moodle-local_copilot`](https://github.com/microsoft/moodle-local_copilot) (**GPL-3.0**,
release **5.1.0**) does not put a model behind Moodle; it puts **Moodle behind Copilot**, as two
declarative agents a teacher drives from Word, PowerPoint and BizChat. 🔵 Every other Moodle AI
row this base carries runs the other way (the `aiprovider_*` family). 🔴 **The strategic read:
the LMS is becoming a tool-provider to someone else's assistant**, and whoever owns the assistant
surface owns the teacher's attention. 🔴 **It is also the anti-sovereign option** — M365 Copilot
licensing, Entra registration, no local-model path — so it sits directly opposite the Ollama-provider
route for EMEA sovereignty and LATAM cost. **Both can be true on one estate; a proposal must say
which surface it is buying.**


## 🆕 `p406` — what changed on this shelf

🟢 **One trend is newly measurable on this base rather than asserted from a source, and it is about
the base itself.**

### 🆕 `T83` — open-source education supply DECAYS at ~2.2 % of carried addresses, and the decay is not uniform across tiers

🟢 **Measured, not estimated: 59 of 2 681 carried addresses do not resolve.** 🔴 **And the per-tier
split is the finding, not the rate:**

| tier | addresses | 🔴 unresolvable | rate |
|---|---:|---:|---:|
| **institutional platforms** *(`verticals/solutions.md`)* | 104 | **0** | **0 %** |
| market intelligence *(`intel/market.md`)* | 74 | **0** | **0 %** |
| foundation repos | 152 | 5 | 3.3 % |
| 🔴 **agent tier** *(`agents/top.md`)* | 238 | **12** | **5.0 %** |

🔵 **The mechanism, and it is a procurement argument rather than an observation.** Platforms carry a
foundation, consortium or company behind the namespace — Moodle, Open edX, Canvas, Sakai, Kolibri,
OpenOlat, BigBlueButton, H5P, Opencast. The agent tier is **single-maintainer MCP servers and
npm-published demos**. 🟢 **So the layer a client's system of record sits on is the layer least likely
to vanish, and the layer Globant composes on top is the volatile one** — which is an argument for
putting the integration contract, not the agent, at the centre of a design.

🟡 **A caveat that cuts against reading this as a maintenance signal.** `EXISTS-PUBLIC` says the
address **answers today**, not that anything is maintained: `StudentTraineeCenter/edu-agent` resolves
and has **511 tracked files** and has not been committed to since **2025-12-30**. 🔵 Dormancy is
`p173-dormancy-bands`'s question and it is a different axis from existence. Two addresses go further
and answer `EXISTS-NO-REFS` — **empty repositories, which EXIST** — so a row keyed on either survives
a 404 check and still ships no code.

### 🟡 `T84` — ECL-2.0 is a THIRD licence class on the platform tier, and a MIT/Apache shortlist mis-sorts it

🟢 **Opencast's licence title line, read first-hand this pass** at `153d1b1`:
**`Educational Community License, Version 2.0 (ECL-2.0)`**. Sakai carries the same grant. 🟡 ECL-2.0
is an **Apache-2.0 derivative whose patent grant is narrowed to the licensor's own contributions** —
neither MIT/Apache nor copyleft. 🔴 **A `"MIT / Apache 2.0 / BSD only"` filter drops both Apereo
platforms, and the error runs toward OVER-caution:** both are permissive and redistributable. 🔵
Named as a trend because this is the second Apereo platform to land on the tier, so the class is not
a one-off row any more.

### 🔵 Regional: the leg saturation is real, and one exception repaired a live row

🔴 **Fourth consecutive pass in which the four prescribed regional legs returned no unshelved fact.**
🟢 **The exception did something better than add one:** the APAC leg resolved this base's own
three-way contradiction about Vietnam's education deadline, and in doing so **refuted a published
opportunity row** that priced an education engagement against **2027-03-01** when education's
deadline is **2027-09-01**. 🔵 Full derivation and the no-primary-read bound on
[`intel/market.md`](market.md).

🟢 **The generalisable lesson for a saturated channel:** a leg that returns only carried facts is not
a wasted leg if it is read against what the base already says. The value here came from the
**collision** between a returned fact and a shelved one, not from novelty.

---

## 🆕 `p405` — what changed on this shelf

🟢 **One new trend, `p405-T1`, opened because it is a *measurement defect* this base has been
publishing as an ecosystem reading** — not because a pass needed a finding. 🟡 **One amendment** to the
licence ladder: a cell `p401` and `p382` between them do not have. 🔴 **No trend is retired.**

### 🔴 `p405-T1` — an address count is not a project count, and the error is NOT uniform across groups

🔵 **The shape.** This base counts **addresses**. Its census, its crowding findings and its
*"real supply, not census noise"* conclusion are all address-denominated. 🔴 **Measured over the four
name-collision groups `intel/open-gaps.md` item 3 names: 42 resolved addresses are 27 projects.**

| group | addresses | 🟢 projects | absorbed | inflation |
|---|---|---|---|---|
| `canvas-mcp` | 20 | 9 | **11** | 🔴 **2.22×** |
| `brightspace-mcp-server` | 4 | 2 | 2 | 🔴 **2.00×** |
| `blackboard-mcp` | 8 | 6 | 2 | 1.33× |
| `moodle-mcp` | 10 | **10** | 🟢 **0** | 🟢 **1.00×** |
| **total** | **42** | **27** | **15** | **1.56×** |

🔴 **The non-uniformity is the trend, and it is what makes a single correction factor useless.** A base
that applied **1.56×** everywhere would be wrong about three of the four groups, and most wrong about
the one where the count is already correct. 🟢 **So the prediction, in a form a successor can refute:**
inflation tracks **how easy the platform is to get credentials for**, not how popular it is. Canvas and
Brightspace have free instructor sandboxes, so a working server attracts forks that are *tutorials*;
Moodle must be self-hosted, so each of its ten implementations was written by someone who already had a
server. 🔵 **Refutable:** measure a group whose platform needs no credentials at all and the inflation
should be higher than `canvas-mcp`'s 2.22×.

🔴 **Why the existing channels could not see it, stated as absence rather than weakness.** `p402`'s
ref-set test answers *"one repository or two"* and `p404`'s pair test answers *"which of these two."*
🟢 **Neither can answer *"how many projects are in this group of twenty"*, because that is a property of
the whole pair graph** — and it needs **`C(N,2)` verdicts**, which is why it stayed open at a clone per
pair. 🟢 **The cost is now `O(N)` clones for `C(N,2)` verdicts** — 20 clones for 190 pairs
([`compose/code/p405-group-lineage/`](../compose/code/p405-group-lineage/README.md), 12 controls) — so
the question is affordable at group grain for the first time.

🟡 **Two second-order consequences worth writing down.**

| | |
|---|---|
| 🟡 **A platform-coverage claim is address-denominated and therefore wrong** | *"Twenty open-source Canvas MCP servers"* is true about addresses and **false** about what a client buys. By projects, Canvas has **fewer** than Moodle. Placed on [`verticals/solutions.md`](../verticals/solutions.md) |
| 🔴 **Transitivity is claimed and did NOT bind here** | Lineage is transitive, so the citable unit is the connected **component**. 🟢 **In all four groups measured, every within-family pair was directly related**, so components equal naive pair-clusters. 🔵 Named rather than left as an untested strength of the instrument |

### 🟡 Amendment to the licence ladder — a plugin's grant can live ABOVE it in the tree

🔴 **`p401` read 51 Moodle plugin grants through two channels and found every one
`GPL-3.0-or-later` — *"Not one MIT, Apache-2.0 or BSD in 51 reads."*** 🟢 **Here is a 52nd, and it is
neither.** `local_italiciamcp`, shipped inside
[`marcosnahuel/moodle-mcp`](https://github.com/marcosnahuel/moodle-mcp), is a real Moodle local plugin —
`$plugin->component = 'local_italiciamcp'`, `db/services.php`, `db/access.php`, 13
`classes/external/` web-service functions, `$plugin->supported = [400, 501]`:

| channel | `p401`'s question | 🟢 **measured here** |
|---|---|---|
| **P** — the grant in the plugin's own PHP headers | reads 51 of 60 | 🔴 **0 of 18 PHP files carry any GPL mention** — not the *"version 3 … or any later version"* paragraph, not the word `GPL` anywhere |
| **L** — a licence-shaped file inside the plugin | reads 24 of 60 | 🔴 **0** — no `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` or `LICENCE` at any path inside the plugin directory |
| 🆕 **A** — the nearest licence file in an **ANCESTOR** directory | 🔴 **no cell** | 🟢 **MIT**, 1,065 B, two directories up at the repository root; README reads *"MIT © 2026 Italicia"* |

🟢 **`p382-subtree-grant` does not cover this, and the direction is why.** That instrument asks
*"which subtrees does this grant **narrow itself** to?"* — a property the payload declares.
🔴 **This asks the inverse: what grant reaches a subtree that declares NOTHING?** 🔵 Both are needed,
and only one existed.

🔴 **The commercial read, which is the opposite of what *"an MIT Moodle plugin"* sounds like.** A plugin
calling Moodle's GPL APIs is normally held to GPL distribution terms, so the likeliest explanation is a
**licensing defect on the author's side** — and a studio that treated the MIT file as permission to
build closed derivative work on it would be relying on the author's mistake. 🟢 **`p401`'s boundary rule
is UNCHANGED:** a studio's permissive code belongs **outside** the plugin boundary. 🔵 **What changes is
the ladder**, which must now ask for the nearest ancestor grant before recording a plugin as
*"no grant / unknown"* — and `p401` already named the direction of that error: an ungranted plugin reads
as *unencumbered*, which is the opposite of the truth. Rows:
[`plugin-inherited-grant.2026-10-23-p405.tsv`](../evidence/plugin-inherited-grant.2026-10-23-p405.tsv).

### 🔵 A null worth recording, because it is the THIRD pass to spend it

🔴 **The four English regional legs returned zero new facts for a third consecutive pass — and two of
the four no longer reach education at all.** EMEA and APAC returned *enterprise* AI material
(a 2023 Workday study, a Pearson–TCS alliance, a Sydney office). 🟢 **That is a change in kind, not
degree:** the legs are not reporting stale education facts, they are reporting non-education facts.
🔵 `T82` governs — that licenses *"these legs do not reach education in these regions"*, never
*"there is no EMEA education AI news."* 🔴 A fourth English regional leg is a **predictable** null, so
the successor move is a channel change. See [`market.md`](market.md).

---


## 🆕 `p404` — what changed on this shelf

🟢 **One new trend is opened, `p404-T1`, and it is opened because it is a *class* this base has been
grading one-at-a-time with the wrong instrument** — not because a pass needed a finding. 🟡 **One
amendment** to the licence/alias reasoning: a cell that did not exist. 🔴 **No trend is retired.**

### 🟢 `p404-T1` — "same name, different HEADs" is THREE mechanisms, and only full history separates them

🔵 **The shape.** This base keeps meeting pairs of addresses that share a plugin or module name and
differ at HEAD. It has graded them with ref sets (`p402`) and with HEAD equality (`p370`, `p349`), and
both channels answer only *"one repository or two"*. 🔴 **Neither can say which mechanism produced the
pair** — and the three mechanisms have **different consequences for a build**:

| mechanism | measurement | consequence |
|---|---|---|
| **Content copy / squash-republish** | 🔴 **0 shared commits** · 🟢 **>0 shared trees**, and the shared tree is one side's **root** tree | 🟢 **Direction is knowable.** One address is the product and the other is provenance — and the live one may be the *younger* address, which currency alone reads backwards |
| **Continuation / hand-off** *(a true fork)* | 🟢 **Shared commits**, and one HEAD is an **ancestor** of the other | 🟢 One address is a **strict superset**; citing the other is citing a prefix. 🔴 Its warnings travel into the superset unless a commit removed them |
| **Independent reimplementation** | 🔴 **0 shared commits AND 0 shared trees** | 🔴 **Two different products.** Language, grant and release discipline may all differ, so the bare name cannot carry a recommendation |

🔴 **Why the old channel could not see it.** A **squash-republish shares ZERO commit SHAs with its
origin.** So on a ref-set or HEAD test a *copy* and two *unrelated namesakes* are indistinguishable —
the signal is **absent** from the channel, not faint in it. 🔵 This is why `p402` was right to refuse a
direction and wrong to record the question as unestablishable: the refusal was about the instrument.

🟢 **Three instances, measured in one pass, one of each mechanism** —
`moodle-aiprovider_openaicompatible` (copy, `lmscloud-io` → `ADORSYS-GIS`), `lti` (continuation,
`macewan-cs` → `astiusa`), `moodle-mcp-server` (independent). 🟢 **Tree SHAs are the load-bearing
addition**: git content-addresses directory state, so a byte-identical tree is **one SHA** however the
history around it was rewritten, and *where* that tree sits in history is the direction.
🔵 `p401` had already found the `classes/provider.php` **blob** identical at 3,963 B and correctly
declined to call it a direction — the **tree** carries the same bytes **plus their position**.

🔴 **What the trend predicts, in a form a successor can refute.** Of `p397`'s **551** candidate pairs,
the ones a ref-set test labels `DISTINCT` are **not** mostly name collisions: this pass's 3-for-3 says
the label hides copies and continuations. 🟡 `p397`'s own arm already found **8 of 15 "forks" are
renames** — same defect, the other direction. 🔵 **The cheap test is now wired**
([`compose/code/p404-fork-direction/`](../compose/code/p404-fork-direction/README.md), 9 controls),
and 🔴 it costs a **full clone per address**, so it is run on **named pairs in bounded batches**. `T82`
governs the sweep; `p402`'s refusal is not re-tested.

### 🟡 Amendment to the licence frontier — identical grant bytes do NOT make a substitutable dependency

🔴 **This base's licence reasoning has had no cell for *package identity*.** It records the grant, its
bytes, its channel and its scope — and a reader takes "same licence, same code, superset history" to
mean "swap the import". 🟢 [`astiusa/lti`](https://github.com/astiusa/lti) refutes that: the MIT file
is **byte-identical** to [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (1,108 B,
`sha256`₁₆ `6e58273960b0`, still **© 2021 MacEwan University**), the history is a **strict superset**
— and the 2023-05-22 commit **changed the Go module path**. 🔴 **So moving costs an import edit in
every consumer**, which is a migration, not a version bump.

🔵 **What to add to a licence cell from now on:** when two addresses share a grant and a lineage, say
whether the **package identity** (Go module path, npm name, PyPI distribution, Moodle `$plugin->component`)
is the same. 🟢 For the `aiprovider_openaicompatible` pair it **is** — both declare
`$plugin->component = 'aiprovider_openaicompatible'`, so there a studio really can swap addresses. 🔴 For
the `lti` pair it is not. 🟡 **Same question, opposite answers, in one pass** — which is why this is an
amendment and not a note.

### 🔵 A null worth recording, because it was predicted and is cheap to re-test wrongly

🔴 **The non-GitHub-forge leg returned nothing.** A leg aimed explicitly at **GitLab and Codeberg**
returned five education-AI addresses and **all five are hosted on GitHub**. 🟢 This base already holds
`gitlab.com` and `codeberg.org` references, so the forges are not unknown here — what is measured is
that **an English-language, forge-named web leg does not reach them**. 🔵 `T82` governs: that licenses
*"this leg does not reach those forges"*, never *"there is no education AI on GitLab"*. 🟢 The cheaper
successor is a **host API probe** with this base's existing
[`gitlab-api-channel`](../compose/code/gitlab-api-channel/README.md), not another web leg.

---

## 🆕 `p403` — what changed on this shelf

🟢 **`p401-T1` gets a THIRD independent instance, and this one was PREDICTED before it was found.**
🟡 **`T36` gets a fourth instance, and its first commercially-usable one** — which changes what the
trend costs a client. 🔴 **No new trend number is opened**: both findings are instances of trends this
base already carries, and recording them as new would be re-selling.

### 🟢 `p401-T1`, third instance — and the first *predictive* one (India)

🔵 **The trend, as this base already states it:** national-language supply appears roughly a year
behind national mandates, and an English-language leg reports the pre-lag state indefinitely.
Evidenced on the **Gulf** (`p401`), and proved from the other direction on **LATAM** (`p387`).

🟢 **`p403` used it as a prediction rather than a description.**
[`intel/market.md`](market.md) already carried India's mandate — **AI and computational thinking
compulsory from Class 3 from the 2026–27 academic year**, with the IndiaAI Mission behind it. A trend
that holds implies **Indic-language education supply appearing around now**. 🟢 **A Hindi-language leg
returned three previously unshelved addresses on its first page**, where the English legs have returned
zero granted education-native addresses for six-plus consecutive passes:
[`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) (MIT code, 14 Indic languages,
HEAD 2026-09-16), [`AI4Bharat/Anudesh-Backend`](https://github.com/AI4Bharat/Anudesh-Backend) (MIT,
HEAD 2026-09-01) and
[`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi)
(🔴 ungranted, HEAD **2026-10-19 — 4 d**).

🔴 **And the control that stops this becoming "run more languages".** A **Japanese**-language leg was
run in the same pass and returned **nothing education-native** — only general-purpose agent frameworks
and licence-comparison blogspam. 🟢 **Japan is the APAC jurisdiction this base records as having a
promotion-first framework with no penalties and no mandate.** So the dividend tracks **the mandate, not
the language** — which is `p401-T1`'s actual claim, and it now has a negative control supporting it
rather than three positives alone.

🔵 **The predictive form, for a successor:** the next legs worth spending are the languages of
jurisdictions whose mandates have **just** commenced. 🔴 **Not** Japanese.

### 🟡 `T36`, fourth instance — and the first where both grants are commercially usable

🔴 [`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) carries **MIT** in its root
`LICENSE` (1,074 B, payload-read) and **`CC-BY-4.0`** over the dataset, in its own §License section.
🟢 The three earlier instances (`inno-agent`'s ungranted skill hub, `os-taxonomy`'s
`ODbL-1.0 AND CC-BY-SA-4.0` data, `h5p`'s GPL content) all had one half a studio **could not use**.
🟢 **Here both halves are usable** — so the consequence is not exclusion but **attribution obligations
attaching to the data**, which is a documentation task rather than an architectural one.

🔵 **What that adds to `T36`:** the trend's cost is not constant. Reading it as *"the curriculum half is
unusable"* would have mis-priced this repository. The licence column must name **which artefact** is
granted **and under what** — not merely flag that two grants exist.

## 🆕 `p402` — what changed on this shelf

🔵 **No trend is added or retired this pass.** The pass was an **instrument and backlog** pass, and
saying so keeps the trend list from drifting on passes that did not measure a trend.

🟡 **One amendment, to `Trend 6` (the permissive-licence frontier).** The frontier is not only *which
licence* a component carries but **which address carries it**. `p402` closed `ACTION ZZ-al` and found
that `ease`'s canonical address is **neither** of the two the register tracked, but a third owner —
[`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease), **archived read-only since
2024-02-28**. 🔵 The grant (**AGPL-3.0**) never changed, so the *frontier* does not move; what moves is
the confidence a reader should place in an address that a search result hands them.

🟢 **The durable rule, now wired into `Pattern AF`:** warrant the **canonical** address, and treat an
owner named `*-unsupported` or an archive banner as a **stewardship finding in its own right** — the
thing to establish *before* promising a client a maintained dependency.

🔴 **And a measured regional gap, repeated rather than new:** the EMEA leg returned **no
education-specific instrument** for the **third consecutive pass**, and the APAC leg surfaced **no
ministry-level instrument** at all. 🔵 Both are written down as informed gaps on
[`intel/market.md`](market.md), because silence looks exactly like coverage.



**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🟢 **Three trends this pass can evidence
rather than quote, and one it can date.**

### 🆕 `p401-T1` — national-language supply is appearing roughly one year behind national mandates

🟢 **Evidenced, not asserted.** The Gulf school mandates took effect in the **2025/26** academic
year (Saudi Arabia, UAE). The **first permissive Arabic-first education repositories on these
shelves were created 2026-09-14, 2026-10-12 and 2026-10-13** — three unrelated projects inside six
weeks, after a year of nothing. 🔵 The same shape is already on this base from the other
direction: `p387` broke a four-pass LATAM supply null with Spanish and Portuguese legs, after
LATAM policy had been typed for passes.

🔴 **The actionable form of the trend is a warning about measurement, not about markets.** An
English-language search reports the pre-lag state indefinitely, because the supply that appears is
named and documented in the local language. 🟢 **A regional supply claim is only as good as the
language of the leg that produced it** — and this base asserted *"not one address"* for the Gulf
across five passes on English legs alone.

### 🆕 `p401-T2` — the AI integration surface in education is consolidating into platform plugin APIs, and that surface is copyleft

🟢 **Measured this pass.** Moodle's `core_ai` subsystem now has a **provider-plugin** interface,
and the shelf holds **60** Moodle plugin addresses with **51 readable grants — every one
`GPL-3.0-or-later`, not one permissive**. Two independent vendors ship the *same*
OpenAI-compatible provider shim with a **byte-identical `classes/provider.php`**. 🔵 Integration is
standardising on the platform's own extension point rather than on bespoke forks, which is good
engineering and a **licence ceiling**: the standard seam is GPL by construction.

🔴 **The consequence contradicts the usual read of "open source is consolidating".** Consolidation
here *reduces* what a studio can own: the more the ecosystem converges on plugin APIs, the more of
the integration lives inside the copyleft boundary. 🟢 The counter-move is architectural and is
written up on [`verticals/solutions.md`](../verticals/solutions.md) — keep the plugin a thin GPL
adapter and put the IP behind a network boundary.

### 🆕 `p401-T3` — the gap between institutional USE and institutional GOVERNANCE is the measurable market

🟢 **The cleanest number any leg returned this pass.** UNESCO IESALC with UNU-IAS, **200
institutions across 19 countries** in Latin America and the Caribbean: **87% use AI in at least one
area; 26% have a formal AI strategy.** Adoption is driven by **individual academics and students**,
not institutions. 🔵 Independent sources describe the same gap elsewhere in different words — a
2026 survey across 450+ institutions reporting roughly **10%** with formal AI-use guidelines, and
the broad 2026 framing of a shift *"from experimentation to governance."*

🟡 **Why this is a trend and not a statistic.** Where use precedes policy by that margin, the first
paid work is **not** building a tutor — it is inventory, data-boundary definition, an acceptable-use
policy and an audit trail for AI already in use. 🔵 That is also the work the EU AI Act's Art. 4
literacy duty and Annex III high-risk classification will require evidence of, so it is **billable
twice**.

### 🟡 `p401-T4` — "purpose-built for education" is now the stated direction of travel, and it is still mostly a claim

🟡 **Convergent across 2026 commentary**, including the OECD's Digital Education Outlook framing and
1EdTech's watch-list: a move away from general-purpose assistants toward systems **built for
learning**, with evidence of durable gains, plus teacher-first deployment and digital credentials
as a skills-verification mechanism. 🔴 **Band: `reported`, and deliberately not promoted.** The
specific adoption figures circulating with this framing — an *"83% AI teaching assistant
deployment"*, a *"42% outcome gain"*, *"92% of university students using AI"* — are **secondary and
untraceable to a primary instrument from this session**, and this base does not put a number in a
deck it cannot source. 🟢 **What IS evidenced here:** the one new PISA-aligned permissive agent
([`braiinz94/braiinz-education`](https://github.com/braiinz94/braiinz-education), Apache-2.0, 0 ★)
is the first address on these shelves aligned to an **international assessment** rather than a
national curriculum — one data point in the predicted direction, and a thin one.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🟢 **Two new
trends, both measured, and the first one is about this base's own repair habit rather than about
the industry.**

### 🆕 `T81` — a defect is fixed where it was FOUND, not where it LIVES

🔵 **`T29` → `T80` → `T81` is one line of descent.** `T29`: a statement about a file disagreed
with the file. `T80`: two shelves disagreed and only one was machine-readable. 🔴 **`T81`: a
defect found in one member of a closed vocabulary is repaired in that member and left standing
in the others.**

🟢 **Evidence, and it is this base's own last pass.** `p399` found that the typed policy layer
answered *"no LATAM teaching mandate"* across 11 rows while the README held the refuting
statute, and fixed it properly — LATAM **0 → 6** rows. 🔴 **It did not re-ask the question of
EMEA, North America or APAC.** Re-asked this pass: **EMEA 7 · LATAM 6 · North America 3 ·
APAC 1** — and APAC's single row was `regional | NOT_ESTABLISHED`, in the region holding the
largest mandated AI-education deployment on earth. 🟢 Now **7**. See `400-G` on
[`market.md`](market.md).

🔵 **Why this is a trend and not one pass's slip:** `region` is a **closed five-value
vocabulary** in this KB by brief. A closed vocabulary makes the generalisation step *cheap and
mechanical* — four greps — which is exactly why skipping it is easy to miss in review. 🟢 **The
operational rule it yields:** when a finding is of the form *"this axis is blank for X"*, the
pass closes only after the same query has been run for every other value of X, and the result
published even when it is "no change". 🔴 The failure mode is not laziness; it is that a
correct, well-evidenced, properly-fixed finding *feels finished* at the moment the instance is
repaired.

### 🆕 `T82` — a refusal names the command it refused, and the OUTER command is not the capability

🔴 **Three passes have now mis-scoped a refusal, each one layer further out.** `395-C`/`396-C`
concluded *"executing repository code is refused"* and told successors to stop ranking
instrument work — refuted by `p397`, which found the refusal was a **clause** of a compound
command, and one clause was a genuine HTTP 403. 🔴 **`p399` then published *"`make hooks` was
refused on this session (`Code from External`), so no gate score is restated here"* — and
`p400` reproduces the `make` refusal exactly, then runs **31 of the 32 gate control suites** at `HEAD` (and 32 of 33 in this commit)
directly with `python3 -I`.**

🟢 **So the gate suite was never unreachable; the *build tool* was.** The measured cost of the
mis-scoping is on the record: two currency gates sat **red and unseen** at `HEAD` (`400-B`),
which is the same price `397-B` paid for the same class of error one generation earlier.
🔵 **The rule:** a refusal licenses exactly one conclusion — *this invocation was refused*. Any
claim about a **capability** needs a second, differently-shaped attempt before it may be
written down, and *"I could not run it"* may never be published as *"it cannot be run."*

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No industry
trend was added: the brief's eight legs returned nothing this base did not hold, for the second
consecutive pass.** 🟢 **One new trend about this base's own structure is added, and it is
measured rather than observed.**

### 🆕 `T80` — the defect has moved from the sentence to the LAYER BOUNDARY

🔵 **`T29` was "a statement about the file disagreed with the file." `397-A` was "a superlative
derived over the rows in view rather than over the shelf." 🔴 `T80` is the same family one level
out: two shelves that are both correct, that disagree with each other, and only one of which an
instrument can read.**

Evidence this pass: `README.md` has carried **Colombia's `Ley 2626 de 2026`** — a binding
education-AI statute — since the `p277` regional battery, while
[`policy-matrix.tsv`](policy-matrix.tsv), the layer built **because** *"prose is not readable by an
instrument"*, carried **11 teaching-mandate rows and not one LATAM**. 🔴 **Neither shelf was lying;
the fact simply never crossed between them**, and the typed side is the side that answers queries.

🟢 **Why this is a trend and not an incident:** the same crossing failed for **six** jurisdictions
at once (CO, AR, CL, MX, BR, PE) plus two the base had lost entirely (PY, UY) — so the mechanism is
structural, not a slip on one row. 🟢 **The cheap standing check it implies:** for any claim of the
form *"no jurisdiction in region R does X"*, grep the prose shelves for R before publishing the
blank. That check, run once this pass, is what produced the finding.

### 🔵 `T42`, held still rather than advanced — and the gate score deliberately NOT restated

🔴 **`make hooks` was REFUSED on this session's classifier** (`Code from External`), where `p398`
ran it twice in full. 🟢 **So `p399` does not restate the gate score** — `398-B`'s whole lesson is
that a score is a derived quantity that goes stale exactly like a census sentence, and a pass that
could not re-derive it must say so rather than carry `p398`'s **46/47** forward as if re-measured.
🔵 **What this adds to `T42`:** the refusal is **not stable across sessions**. Same repository, same
command, same month — `p397` and `p398` ran it, `p399` cannot. 🔴 **Any gate claim in this base is
therefore conditional on the session that made it**, which is a property no shelf here had recorded.
`Gap 399-B`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No industry trend
was added: the four regional legs returned nothing this base did not hold** (`Gap 398-C`). 🟢 **Two
trends about this base's own instruments are refined instead, and both are measured.**

🔵 **`T42` narrowed one notch further.** `396-C` recorded *"executing repository code is refused"*;
`p397` refuted that by running the repo's own suites and localised the refusal to a **compound**
command. 🟢 **`p398` adds the discriminating axis: the classifier gates the AUTHORSHIP of the code,
not the host, the tool or the command shape.** `make hooks` ran **twice** this pass, in full; a
**hand-written** script that merely *imported* the same repository module was refused
(`Code from External`), and so was a `make` target on one invocation and not another. 🔵 So a pass
should reach for **the repository's own committed targets** and treat an ad-hoc probe as unavailable —
which is the opposite of the usual instinct to write a quick script.

🔴 **And a trend this base should name because it has now fired four passes running:** a new channel's
first yield is overwhelmingly **content the base already owns**. `p393` warned of it; `p395`, `p396`
and `p397` each caught themselves about to re-sell an owned fact; 🔴 **`p398` measured it at the
channel level — nine of ten rows on `topic:autograder`'s first page, and 100% of eight search legs.**
🟢 **The operational consequence: grep the tree BEFORE writing, not after**, and rank a channel by
*what it adds* rather than by *what it returns*. 🆕 **`T43`.**

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** Three trends, each
tied to a measurement in [`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv),
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p397.tsv).

### 🆕 `T40` — The permissive LTI 1.3 supply in Python is not thin, it is ABANDONED — on both sides of its own fork

🔴 **`p393` corrected the count of permissive Python LTI libraries from three to five and noted they
were *"largely unmaintained."* `p397` dates the two halves of the one that looked institutional, and
both are dead:**

| address | HEAD | days | note |
|---|---|---|---|
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | `d8fa43e` | 🔴 **1 432** | the upstream |
| [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) | `6a47f0f` | 🔴 **1 379** | 🟢 a **genuine divergent fork** (shared root `676b78fec64c`, different HEAD) by **UCF Open**, University of Central Florida |

🔵 **Why this is a trend and not a row.** The hopeful reading of an abandoned library is *"an
institution forked it and carries it now."* 🟢 **Here that institution exists, the fork is real and
measured — and it stopped 1 379 days ago, 53 days after the upstream did.** 🔴 **So "someone forked
it" is not evidence of maintenance, and a provenance test that only proves lineage will tell you the
fork exists while saying nothing about whether anyone is home.** Lineage and liveness are two
measurements and a recommendation needs both. 🟢 The best-maintained Python LTI option on these
shelves remains the **AGPL** one — which is a licence conversation, not an availability one.

### 🆕 `T41` — A rename is indistinguishable from a fork until you compare HEADs, and this industry renames constantly

🟢 **Education software is unusually prone to this**, because its infrastructure is run by
**standards bodies and foundations that re-badge**: `IMSGlobal` → `1EdTech`, `edx` → `openedx`
(Axim), `digitalcredentials` → **OpenWallet Foundation Labs**, `pytorch` → `meta-pytorch`,
`kantord` → `LibreLingo`. 🔴 **Eight of 15 shared-root pairs on these shelves were renames, not
forks — 53%.** GitHub answers on the old path indefinitely, so **both addresses look alive, carry the
same licence payload and the same stars**, and nothing in a licence read or a star read can separate
them.

🔵 **The consequence for a studio is concrete:** a dependency audit that lists `IMSGlobal/...` and a
conformance clause that cites `1EdTech/...` are the **same dependency**, and a client reading both
will reasonably ask which one you actually tested. 🟢 **Fold on HEAD, cite the current path, and keep
the old one as an alias rather than a row.**

### 🆕 `T42` — A refused channel is a claim with a shelf life, and this base just paid for forgetting that twice in three passes

🔴 **`396-A` named this exactly one pass ago:** *"an absence recorded against ONE channel hardens
into a fact about the world within two or three passes, and then stops being retested."* 🔴 **It
happened again immediately, to `396-C`** — *"executing repository code is refused by the environment
classifier… three ranked items are permanently blocked."* 🟢 **`p397` ran the repository's own Python
suite on its first attempt: 59 checks, 0 failures.** What `p396` actually hit was a **compound shell
command** in which one clause was refused, and the refusal was attributed to the whole.

🔴 **The cost was not hypothetical.** `make hooks` went unrun for two passes, and three gates drifted
red unseen — `gate-region-headings`, `gate-census-currency`, `gate-union-currency` — taking the
standing score from **44/46 to 41/46** with nobody watching. 🔵 **The gates were working the entire
time; nothing was reading them.**

🟢 **The generalisation, which is a cheap writing rule:** *carry the channel AND the granularity in
the claim.* `396-B` already said a 403 is ambiguous between host, proxy and tool. 🟢 **`p397` adds the
third axis: ambiguous between the command and a clause of it.** Re-measure one clause at a time
before recording a capability as absent — `p397`'s own channel table does, and that is how both
findings above were found.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Four trends, each tied to a measurement in
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p396.tsv).

### 🆕 `T37` — Agents have memory; institutions have records; nothing joins them

🔴 Every tutoring agent on these shelves keeps **its own** memory — `DeepTutor`'s lifelong memory,
`inno-agent`'s L1/L2/L3 layers, `OATutor`'s Bayesian knowledge tracing. 🔴 **None of them writes to
the institution's Learning Record Store**, which is where a registrar, an accreditor, a regulator or
a credential actually looks. The entire open-source supply joining the two is
[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi): **MIT, 15 ★, 419 days
without a commit.**
🔵 **Why this is a trend and not a gap note.** Agent memory is designed for *continuity of
conversation*; an LRS is designed for *evidence that survives the vendor*. They are different
artefacts with different owners, and the market has built the first and not the second. 🟢 Every
regulatory pressure in `intel/market.md` — Oklahoma's teacher-review requirement, the EU's Article 26
logging duty, LATAM's missing governance — lands on the **second**. 🟢 This is the clearest unserved
build in this base.

### 🆕 `T38` — The standard moved and the implementations did not: xAPI 2.0 has zero adoption

🟢 xAPI 2.0 is **IEEE 9274.1.1-2023**, reportedly also an ISO/IEC/IEEE edition in 2025 *(secondary;
unconfirmed — `arxiv.org` and the standards hosts are refused)*. 🔴 **The two best-adopted permissive
LRSs do not implement it**: `lrsql` (144 ★) is 1.0.3-era and Ralph's docs say 2.0 *"is not currently
supported."* 🔴 **The three that claim it hold 1 star between them** — `pelotech/xapi-lrs` (0 ★),
`codetakt/kiva` (0 ★), `nurullahturkoglu/xapi-dotnet` (1 ★).
🔵 **The asymmetry to notice:** all three were written in the last 75 days, while the referee —
[`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite), MIT,
78 ★ — is **413 days old**. 🟢 A standard whose conformance suite ages faster than its implementations
is a standard where **claims cannot be checked from the outside**, which is precisely why the
pattern for this layer is *run the suite yourself*, not *read the badge*.

### 🆕 `T39` — "Open source" is splitting from "permissively licensed" in education, in a new way

🔴 `395-D` recorded the split *inside* a project: MIT kernel, ungranted skills. This pass found it
*across a language community*. The most active new education agent found by a non-English leg —
`Aula y Comunidad Educativa Aumentada`, 1 day old — publishes under a **bespoke "Licencia
Comunitaria de Uso Profesional."** Public repository, visible source, 🔴 **no open-source grant.**
🔵 Combined with `h5p/h5p-php-library` (GPL content reported as MIT) and `withmarbleapp/os-taxonomy`
(ODbL + CC-BY-SA over the data), this base has now seen three distinct shapes of the same thing:
ungranted companions, mislabelled grants, and bespoke licences. 🟢 **The operative habit is unchanged
and keeps paying: read the payload, never the badge.** Four of this pass's reads contradicted what
the search channel said about the same repository.

### 🆕 `T40` — A measured absence is only as good as the channel that measured it

🔴 `394-C` concluded this environment *"cannot ENUMERATE GitHub at all,"* and five passes of thin
supply were explained by it. 🟢 **This pass enumerated GitHub twice** — `github.com/trending` at 200
after fourteen passes recorded as 403, and `github.com/search` returning 150 results — and one query
on the reopened channel produced **eight unseen addresses, six of them live and permissive.**
🔴 The refusal was real but narrower than recorded: it is on `api.github.com` and on `curl`, not on
the HTML endpoints through WebFetch.
🔵 **The generalisable lesson, and it is uncomfortable for a base built on declared absences:** an
absence recorded against *one* channel hardens into a fact about *the world* within two or three
passes, and then stops being retested. 🟢 The fix is cheap — **carry the channel in the claim**
("not found via WebSearch" ≠ "does not exist") — and this base should now re-measure a refused
channel on a fixed cadence rather than inheriting it. `396-A`, `396-G`.


# Education industry trends

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Four trends, each tied to a measurement in
[`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv),
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv) or
[`channel-state`](../evidence/channel-state.2026-10-23-p395.tsv).

### 🆕 `T33` — Regulation has started FORBIDDING feature classes, not just risk-rating them

🔴 The EU AI Act bans **emotion-inference systems in educational settings** outright — unacceptable
risk, in the same tier as social scoring and predictive policing. 🔵 Every other regulatory fact on
these shelves is an *obligation* (assess it, document it, keep a human in the loop); this one is a
**prohibition**, and it is the first thing in this base that makes a feature unshippable rather than
expensive. 🟢 **Read it as a design-review input, not a legal-review input.** "Engagement detection"
and "attention scoring" are the two product names this most often hides behind, and both are
routinely proposed in edtech pitches. 🟡 Note the asymmetry with `Annex III ¶3`, which makes grading,
admission, level-assignment and exam monitoring *high-risk but permitted* — so the same product can
hold one feature that needs conformity assessment and another that cannot exist.

### 🆕 `T34` — The integration standard is LANGUAGE-PARTITIONED, and the partition is maintenance

🟢 LTI 1.3 is the surface every agent must cross to live inside Moodle, Canvas, Blackboard or D2L, and
all 13 known addresses were dated this pass in one sitting. 🔴 **The permissive supply is live in
PHP, Node and Python (1–9 days) and dead in Go and Java (679, 1,193, 1,918 days).** 🔵 The standard is
not thinly supported — it is supported *in some runtimes only*, which no amount of spec-reading
reveals and only dating shows. 🟢 Consequence: the language of the client's platform team now decides
an architecture, not a preference — a JVM or Go shop gets an **HTTP edge**, not a library.

### 🆕 `T35` — Supply arrives through the leg you choose, and the prescribed English legs are spent

🔴 **Sixth consecutive pass** in which the four prescribed English global legs returned **zero granted
education-native addresses** — only general-purpose agent frameworks, learning-resource lists and
market-research blogspam (`Gap 387-D`). 🟢 **The same pass found four granted addresses on two legs
nobody had prescribed:** one in **Spanish** (`agente educativo código abierto … tutor IA`), which
surfaced the 1.3k ★ agent, and one naming a **standard** rather than a category (`"LTI 1.3" OR "Open
Badges" … MIT Apache`), which surfaced the Go and Java tier. 🔵 **The dry spell was a property of the
query, not of the ecosystem** — and this base spent five passes attributing it to the ecosystem.

### 🆕 `T36` — The grant on the code and the grant on the curriculum keep coming apart

🔴 Third instance on these shelves, and this time on the pass's best address.
[`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) is **MIT**; its companion skill-library and
workspace-preset hub is **ungranted on every arm**. The pattern already appears in
`withmarbleapp/os-taxonomy` (permissive code absent, `ODbL-1.0 AND CC-BY-SA-4.0` over the data) and in
`h5p/h5p-php-library` (GPL content routinely mistaken for MIT). 🔵 **In an agent-era project the
reusable asset is increasingly the skills, prompts and presets — exactly the half that carries no
grant.** 🟢 So the licence column on these shelves needs to stop describing "the repository" and start
naming *which artefact* is granted; `Gap 549` said this about one repo, and it is now a trend.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/intel-trends.md`](../archive/2026-10-22-p383-pre-rewrite/intel-trends.md).

> The previous version's headline trends were about **what this knowledge base could see** —
> channel yield, address supply, star thresholds. Those are facts about a scraper, not about
> education. They are preserved in the archive and in
> [`agents/trending.md`](../agents/trending.md); this shelf is now about the industry.


## 🆕 `p392` — what changed on this shelf

🔴 **`Trend 19`'s closing claim is withdrawn** (*"Node and PHP have maintained LTI 1.3; Python does
not"*) — three Python implementations read first-hand, and withdrawing it turns a language constraint
into a **licence** constraint, which is the more useful statement. 🟢 **Two new trends**: `Trend 20`,
the granted proctoring supply covers the lockdown and not the inference — the inverse of where the
regulatory exposure sits; and `Trend 21`, LATAM's public buyers are procuring AI education platforms
as **subscriptions**, with no tender asking for open source.

## 🆕 `p390` — note on what was removed from this shelf

Two `p387` sections that stood here (*"Date the artefact, not the repository"* and *"The LATAM
supply gap was a reading gap too"*) were **measurement-apparatus notes, not industry trends** —
exactly what `p383`'s rewrite note above says this shelf is not for. They are preserved verbatim in
[`archive/2026-10-22-p390-pre-trim/intel-trends.md`](../archive/2026-10-22-p390-pre-trim/intel-trends.md)
and their durable content lives where it belongs: the dating method in
[`agents/top.md`](../agents/top.md) under *How these rows were verified*, and the LATAM supply in
`Tier 4` of that same shelf. Nothing was lost; it was filed.

## 🆕 `p386` — The LMS-integration gap is not a licence gap any more. It is a **tenancy** gap.

For four passes this base recorded Blackboard and D2L as the two platforms where
*"a permissively-licensed MCP server would be a genuine contribution."* `p386` probed all fifteen
addresses first-hand: **6 MIT grants on Blackboard, 6 on D2L, 1 ungranted, 2 dead.** The licences
were there the whole time; nobody had read them.

🔵 **What replaced the gap is a sharper and more useful trend.** Eleven of the twelve granted
servers authenticate **as the signed-in student** — the learner's own browser SSO/MFA session or
session cookies, no admin API key, read-only because nothing else is possible from that position.
They are built by students, for themselves, at their own university, and several hard-code it.

That makes the 2026 community LMS-MCP supply a **personal-tooling** supply, and it does not become
an institutional one by being licensed well:

| what an institution needs | what a session-scraping server has |
|---|---|
| tenant identity, per-role scope | the rights of whoever signed in |
| an audit trail of every agent action | nothing, or stdout |
| a stable contract against the vendor's API | a login page that changes without notice |
| a data-protection answer for a DPO | the student's session cookie in a config file |

🟢 **Exactly one address read as institution-grade** — [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
(MIT): official REST API, OAuth2, role gate, FERPA handling, PII scrub, JSON audit log, Prometheus
metrics, grade write-back (maintainer self-claims, read not executed). **One in twelve.**

🔵 **The consequence for a studio, and it is a sellable one.** The scarce artefact in LMS
integration is no longer a permissive server — it is a **hardened** one. The work is: take a granted
community server, put tenant auth, role scoping, rate limiting and an audit trail around it, and
pin it to the vendor's documented API rather than its login page. That is a small, well-bounded
engagement with a deliverable the client can show their data-protection officer, and it is
available on **every** major LMS as of this pass. 🔴 On D2L it is still partly greenfield: all six
granted Brightspace servers are student-side.

🔴 **And the methodological trend underneath it, because it will recur in every industry in this
rotation:** a census that counts **addresses** and a census that counts **grants** are different
measurements, and the first one silently masquerades as the second. *"Nine servers and not one
verified grant"* described this base's own reading, not the world — the honest word for a count of
zero reads is **unread**, never **ungranted**.

## Trend 1 — Adoption is finished. Governance is the market.

**88–95% of students and faculty already use AI; 26–54% can name a governing policy.**
That gap, not the adoption curve, is what 2026–27 budget buys.

- Coursera (n=4,200, 5 countries): **95%** using AI academically, **26%** of educators report a
  formal institutional policy.
- EDUCAUSE 2026: only **54%** are aware of *any* policy or guideline.
- Ellucian (n=779): institutional adoption **49% → 66%** year on year, with **data privacy the top
  barrier**.
- Digital Education Council (n=45,398, 35 countries): **88%** of students, **77%** of faculty.

- 🆕 `p384` **UNESCO IESALC** (n=**200 institutions, 19 countries**, Sept 2026): **87%** of LAC
  higher-ed institutions use AI in at least one area — **74%** in teaching and learning, **57%** in
  research — against **26%** with a formal AI strategy. 🟢 **An independent, institutional source
  landing on the same 26%** as Coursera's educator-reported figure, in a different region with a
  different method. The governance gap is no longer an inference from one survey; it replicates.
- 🆕 **OECD TALIS 2024** puts teacher AI use at **~50%+** in Brazil, Chile, Colombia and Costa Rica
  against an **OECD average of 36%**; Uruguay's **Ceibal** reports **75%** of public-school
  teachers. 🔵 Practitioner uptake is running ahead of the OECD mean in LATAM — the governance gap
  is widest exactly where adoption is fastest, which is the opposite of the usual assumption.

**So:** stop selling introduction. Sell policy-to-configuration, audit trails and a governed
gateway. The shadow-AI estate already exists on every campus. 🟢 And sell it **hardest in LATAM**,
not last — the 87%/26% split there is the widest measured in this file.

## Trend 2 — The ROI reckoning arrived, and procurement is being rewired around evidence

- **~80%** of institutions are investing in AI; **29%** of CTOs say it met or exceeded ROI
  expectations (Inside Higher Ed / Hanover).
- **~7 in 10 provosts** use AI weekly themselves; **1 in 10** report a centralised institutional
  strategy. Personal adoption has outrun institutional capability.
- The **US Department of Education's "Dear Colleague" letter** tells states to evaluate ed-tech by
  **measurable learning outcomes rather than screen time**, and to put **evidence requirements into
  procurement**.
- **US/Canada faculty intent to keep using AI fell 76% → 67%** in one year.

**So:** a before/after measurement on the client's own subject mix is becoming a procurement
precondition, not a nice-to-have. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
MMLU and GSM8K are all MIT; there is no licence reason not to ship this with every engagement.

## Trend 3 — Regulatory divergence hardened in 2026. One global configuration is no longer viable.

Four regimes moved in four different directions in a single year:

| region | 2026 direction |
|---|---|
| **EU** | **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) pushed high-risk education systems from 2 Aug 2026 to **2 Dec 2027** — while **Art. 50 transparency still starts 2 Aug 2026** and **Art. 4 AI literacy has bound every school since 2 Feb 2025**. Emotion recognition in education: prohibited. 🆕 `p385` **The nearest date is neither of those: machine-readable marking of AI-generated content on systems ALREADY on the market is due 2 Dec 2026.** Annex I (AI embedded in regulated products) moves to **2 Aug 2028**. |
| **US** | No federal rule; **134+ bills across 31 states**, **33–35 states** with guidance, and binding district-policy mandates (Idaho SB 1227 effective 1 Jul 2026; Oklahoma SB 1734 by 2027-28). |
| **India / China** | **Content labelling and provenance**: India's amended IT Rules from **20 Feb 2026**; China's labelling measures from **1 Sep 2025** (988 services filed by 30 Jun 2026). |
| **Vietnam / Brazil / Mexico** | **Sectoral high-risk designation**: Vietnam names education among six high-risk sectors; Brazil's PL 2.338/2023 reportedly covers student selection; Mexico replicates the EU risk model. |

**So:** regional configuration is now a product requirement. The same tutor needs provenance
watermarking for India, a transparency notice for the EU, a prohibited-uses lockout for DC, and a
teacher-facing-only mode for ANZ and Brazil.

🆕 `p385` **Two corrections to how this trend gets sold.** First, **the EU deferral is widely
misread as breathing room.** It defers the *high-risk* regime; it defers nothing for a system already
deployed, which owes machine-readable marking on **2 Dec 2026**. A client told "the EU moved to 2027"
and nothing else has been misinformed about the only date within the current budget year. Second,
**employment-adjacent AI is separating from student-facing AI as its own regulated surface**:
**Illinois SB 2909** restricts AI in *teacher* evaluation from **1 Jan 2027**, where DC had only a
non-mandatory ban. A product that evaluates staff is a different compliance object from one that
teaches learners, and the two are still being scoped as one in most pitches.

## Trend 4 — Restriction is a real countertrend, not noise

For two years the only direction was adoption. In 2026 the brake appeared:

- **District of Columbia** 2026-27 policy bans AI from **grading, discipline, IEP decisions and
  teacher evaluations** — four of the highest-value automation targets.
- **Ipsos Education Monitor 2026:** **Australia and New Zealand show the highest support for
  banning AI in schools**, while Asian markets show the lowest. One company, two opposite mandates.
- **European Schools:** **no** generative AI tool approved for system-wide use.
- 🔴 **UNCONFIRMED:** a reported **New York City moratorium** on student-facing generative AI
  (EdWeek; date metadata inconsistent). If it holds, the largest US district has gone the other way.

**So:** "student-facing optional" should be an architectural switch from day one, not a retrofit.
A product that cannot run teacher-facing-only is unsellable in a growing share of the market.

## Trend 5 — Teacher-facing is beating student-facing where growth is fastest

HolonIQ's **2026 LATAM EdTech 100** finds regional AI positioning concentrated in **teacher-facing
instructional tools rather than consumer tutoring** — Teachy (Brazil) in lesson preparation, Ginia
(Mexico) in employability. The regulation points the same way: Brazil's draft law targets
**student selection**, DC bans AI in grading and discipline, ANZ sentiment is restrictive.

**So:** the market and the regulator agree for once. Lesson preparation, assessment drafting,
feedback generation and administrative load carry the growth and avoid the hot zone.

## Trend 6 — The permissive-licence frontier runs *across* the stack, not along it

Measured first-hand this pass over 58 live repositories:

- **Platform tier is copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, Chamilo
  GPL-3.0, ILIAS GPL-3.0, Tutor AGPL-3.0, Frappe LMS AGPL-3.0, Sakai ECL-2.0, Opencast ECL-2.0,
  OpenEduCat LGPL-3.0, H5P GPL-3.0.
- **Exactly one permissive major LMS**: **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT),
  Apache-2.0** — and no roundup we read mentions it.
- **Agent tier is permissive almost throughout**: MIT / Apache-2.0 / BSD-3.

**So:** the architecture follows from the licences. Compose permissive agents **over** a copyleft
platform across **LTI 1.3**, **MCP** or web services — never fork the platform. The interop boundary
is a legal artefact as much as a technical one.

## Trend 7 — MCP reached the LMS, and that is genuinely new

As of 2026 the LMS is addressable by agents without a fork:

- **Moodle's own plugin directory** carries **`webservice_mcp`**, exposing Moodle's external
  functions as **MCP tools over JSON-RPC 2.0** — **Moodle 4.5–5.2**, latest release
  **23 Jul 2026**, gated on the `webservice/mcp:use` capability.
- **Canvas** is served by community MIT servers ([r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp),
  fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp)).
- 🔴 **No official server from Instructure or Moodle HQ**, and two of the most-advertised community
  Canvas/Moodle servers are **unlicensed** — see [`agents/top.md`](../agents/top.md).
- 🆕 `p387` **27 distinct education MCP server slugs are shelved** on
  [`agents/top.md`](../agents/top.md) — re-derived by this base's own `recount` instrument, which
  was runnable this pass for the first time in several (the figure stood at **12** here while the
  shelf had grown to 27). Across both agent shelves **MCP reaches **6 distinct LMS platforms**** —
  Canvas, Moodle, Google Classroom, Blackboard, Brightspace/D2L and Open edX. The cumulative
  harvest behind that is lopsided: **35 Canvas servers and 20 Moodle**, against **2 for Open edX**.
- 🔴 🆕 `p387` **A correction this shelf owed since `p386`, and did not carry.** The bullet above
  used to end *"Blackboard has 9 with not one verified grant and D2L has 6 with the only one
  checked ungranted"* — and concluded that a permissive server on either platform *"would be a real
  contribution."* `p386` probed all fifteen addresses and found **6 MIT grants on Blackboard and 6
  on D2L**; it corrected [`agents/top.md`](../agents/top.md) and **left this sentence standing**.
  🔵 The live claim is: on Canvas and Moodle the work is *selection*; on Blackboard and D2L the
  grants exist and the missing thing is **tenancy** — every granted server there authenticates as
  the signed-in student (see `compose/patterns.md` **Pattern N**, and `Gap 387-A`).

**So:** the integration cost of an LMS-aware agent dropped by an order of magnitude this year, and
the remaining risk moved from engineering to licensing.

## Trend 8 — Measurement gap in this pass, stated rather than papered over

**No popularity metric is published this pass.** Every star channel was closed in this sandbox:
`api.github.com` 403, `github.com` HTML 403, `img.shields.io` blocked, `api.star-history.com`
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated across several industries**; carrying unverifiable numbers forward would
repeat that error. Licence, default ref and liveness **were** verified first-hand for all 58 live
addresses — see [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

**So:** rank by licence permissiveness, maintenance signal and fit. Popularity was never the
decision criterion for a studio engagement anyway.

🟢 🆕 `p387` **Partially closed — and by a channel, not by a workaround.** "Maintenance signal" was
the one criterion in that sentence this base could not actually measure. It can now: **package
registries publish dates**, and 26 education packages are dated in
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv). 🔴 **Still open:** repository
commit activity, contributor counts and issue latency (all behind `api.github.com`, 403), and the
many shelf entries that are **not published packages at all** — for those, publication is absent
rather than old, which is itself worth telling a client.

## Trend 9 — 🆕 `p384` The curriculum-data layer arrived, and its licence is a *database* licence

**Every adaptive-learning pitch rests on knowing what a learner must master before the next topic.
Until this pass, no shelf here held that artefact. Now one does — and it is not licensed like code.**

[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) `v1` publishes **1,930
micro-topics** and **4,102 prerequisite edges** as a DAG — each edge tagged `hard`/`soft` with a
one-line reason — over **9 subjects**, aligned to **NGSS, Common Core, the UK National Curriculum**
and the Australian curriculum. Its grant, read first-hand at `main/LICENSE` (25,289 B), is the
**Open Data Commons Open Database License (ODbL)**. There is **no separate code grant**.

**Why this is a trend and not just a row.** Every licence question these shelves have answered so
far was a **copyright** question about code: can we link to it, can we ship closed extensions. ODbL
is a **share-alike database right**, and it draws its line in a different place:

- **§4.3 — a *Produced Work*** (the tutor's output: a lesson plan, a next-topic choice, an
  explanation) needs **an attribution notice and nothing else**. 🟢 This is the permissive path.
- **§4.4 — a *Derivative Database*** (the client's topics merged in, standards remapped, the graph
  re-cut) must be publicly used **only** under ODbL, a later ODbL, or a compatible licence. §4.4(b)
  is explicit that extracting *"the whole or a Substantial part of the Contents into a new
  database"* **is** a Derivative Database. 🔴 This is the trap, and it is the thing a studio would
  naturally do next.

🔴 **A licence scanner pointed at code will not see this at all.** Neither will a licence badge:
ODbL is not in the permissive/copyleft taxonomy these shelves have been using, so the row cannot be
classified green or red — it is **green on one axis and red on the other, depending on what you
ship**. `Pattern L` was built for the case where a badge misreports a code grant; this is the case
where the *category* is wrong.

**So:** three concrete consequences.
1. **Ground on it, do not fork it.** Keep client curriculum data in a separate store joined at
   query time, so the taxonomy stays an **input** rather than a component of the deliverable. That
   is **Pattern H** in [`compose/patterns.md`](../compose/patterns.md).
2. **Add a data-rights question to intake.** Alongside "what licence is the code", ask "what rights
   govern the **data** we ground on". Education runs on standards, item banks and curriculum maps —
   this will not be the last ODbL/CC-BY-SA artefact on these shelves.
3. **Check coverage before promising it.** The maintainers state their own gap: teaching research
   covers **1,049** topics (Science and Mathematics) and **881 topics have none**. A
   research-backed-guidance claim is true for roughly half the graph.

## Trend 10 — 🆕 `p388` The parent is the unserved persona in education AI, and the statutes are pushing toward them

Every market map this base has built, and every roundup it has read, segments education AI into
**student-facing** and **teacher-facing** — `Trend 5` is about which of the two is growing faster.
Both categories are about people *inside* the institution. **The parent is outside it, and is the
person who actually logs into the portal.**

**The supply arrived this pass and it is not a prototype tier.**
[chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) (**MIT**, 20 tools
over **Infinite Campus / Campus Parent**, **47 published releases**) and
[chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) (**MIT**, 18 tools,
**43 releases**) are maintained, deliberately scoped to the observer surface, and built by one
maintainer working the same problem across two platforms — which is what a real need looks like
rather than a weekend demo.

**Three reasons this is a trend and not a curiosity:**

1. **The statutes are already there.** Every North American instrument this base tracks puts
   **family transparency** in the text — Oklahoma SB 1734 names it outright; Maryland's Chapter 634
   is built around guidance districts must hand down to families. Regulators keep asking
   institutions to *explain AI to parents*; nobody is building the surface that would.
2. **There is no incumbent to displace.** The parent portal is a **feature of the SIS**, not a
   market. No vendor defends it, and the SIS vendors have no incentive to open it. That is the rarest
   condition in education software, where every other surface has a 20-year incumbent.
3. **It inverts the tenancy problem instead of solving it.** `p386`'s finding — every granted LMS
   server authenticates as the signed-in user, so a studio cannot hand one to an institution — reads
   as a *defect* for student and teacher tools. For the parent it is **the correct architecture**:
   the parent's own credential, the parent's own child, no institutional tenancy required at all.

🔴 **And the boundary that defines the engagement, because it is not a licence boundary.** Hosted by a
family, these tools are a person exercising their own access. **Hosted by a studio for a district, the
identical API call becomes a FERPA-governed disclosure of an education record.** The code does not
change; the obligation does. 🔵 So the honest market shape is **two different products**: a
parent-side tool (no tenancy, no FERPA exposure, no institutional sale) and a district-side one (full
tenancy, full FERPA, a real procurement cycle). Conflating them is how this gets sold wrong.
`Pattern P` in [`compose/patterns.md`](../compose/patterns.md) is built on that split.

## Trend 11 — 🆕 `p388` Jurisdictional curriculum content is becoming the defensible layer, and it is arriving region by region

`Trend 9` recorded that a curriculum-data layer had arrived and that its licence was a **database**
licence. `p388` shows the *shape* that layer is taking, and it is not one global graph:

| region | asset | licence | what makes it local |
|---|---|---|---|
| **North America** | 🆕 [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 🟢 MIT | The **BC Ministry** K–12 curriculum in its real three-column **KDU** structure — and the **First Peoples Principles of Learning**, a provincial requirement no imported product carries |
| **LATAM** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) (`p387`) | 🟢 MIT | **BNCC** skill codes, Brazil's national curriculum, with invented codes discarded before a teacher sees them |
| **Global** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (`p384`) | 🟡 **ODbL** (database licence) | 1,590 topics / 3,221 prerequisite edges mapped to NGSS and Common Core |

**The pattern across the three:** the model is interchangeable, the *curriculum authority* is not.
A tutor that cites a BNCC code, a BC Big Idea or an NGSS standard is doing something a
general-purpose tutor **cannot** — not because its reasoning is better, but because it is anchored to
the instrument the jurisdiction grades against.

**Three consequences for an engagement:**

1. **Curriculum grounding is now demonstrable in three regions, not described in one.** `Pattern H`
   stops being a proposal and becomes a reference build with a local example in hand.
2. 🟡 **The risk on these assets is currency, not licence.** The BC server is 🟢 MIT — clean — but it
   is a **crawl** of `curriculum.gov.bc.ca`, last published **2026-03-27**. Curricula are revised on
   political timetables. **Quote the re-crawl as a maintenance line item**, and never let a client
   believe a crawl is a feed.
3. **Keep asking the data-rights question from `Trend 9`.** Two of the three assets above are code
   (MIT); one is a **database** under ODbL. "What licence is the code?" and "what rights govern the
   data we ground on?" remain two different intake questions with two different answers.

## Trend 12 — 🆕 `p388` An exhausted channel is not an exhausted supply — and "published but unreadable" is now a real category

This is a trend about **how this industry's open-source supply is actually distributed**, and it has
a direct procurement consequence.

**The discovery finding.** `p382` recorded that this industry's address supply was **exhausted**.
What was exhausted were four search-engine legs. **`registry.npmjs.org/-/v1/search` is open**, and 29
education queries returned **383 GitHub addresses absent from this entire base**, of which **22 are
granted and education-specific** — the largest single intake in this base's recorded history. 🔵 The
general lesson, and it is the third of its kind here: `p386` learned *a count of addresses is not a
count of grants*; `p387` learned *a null leg is not a null supply*; `p388` adds *an exhausted channel
is not an exhausted supply*. All three are one error — **a property of the instrument reported as a
property of the industry.**

🔵 **Why a package registry is structurally the better instrument for this industry.** A trending page
ranks by attention over days. Education tooling is **institutional, unglamorous and
low-star** — a 47-release parent-portal server for a US K-12 SIS will never trend anywhere. The
registry indexes it anyway, and returns its **entire publish history in the same call**, which
answers "is it maintained?" at the moment of discovery rather than two steps later.

🔴 **The new supply category, and it is the uncomfortable half.** Of 32 addresses probed, **6 publish
to npm from a repository that is not publicly readable** — `git ls-remote` prompts for credentials,
so the repository is **closed, not missing**. The package installs; the provenance cannot be audited.
The costliest instance is **103 published versions** of an AI-generation quiz library **with SCORM
support** ([thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)); the
most instructive is [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest
declares **`"SEE LICENSE IN LICENSE"` — pointing at a file inside a repository nobody can read.**

**So the licence-reading discipline this base built needs one more rule.** `Pattern L` clears a
repository by reading its **subtree**; for these there *is* no subtree. The rule that replaces it:
**for an npm-only dependency, the manifest is a claim and the tarball is the evidence** —
`registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves the published artefact even when the repository is
closed, and **it is the licence that actually ships**. 🔴 That is how this pass established that a
major publisher's tutoring SDK (**115 published versions**) carries **no licence at all**: not from
the repo, which is private, but from the artefact, which is not. 🔵 And the corollary a studio should
internalise: **commercial education vendors are starting to distribute as closed SaaS with an npm
veneer.** The npm scope looks like open source, installs like open source, and grants nothing.

🔵 🆕 `p391` **The channel now has a decay curve, not just a verdict.** Re-run with 32 queries of
*fresh* vocabulary (tenancy, SEN/IEP, proctoring, QTI, xAPI, OneRoster, FERPA, standards, personas):
**321** addresses absent from this base → 37 past a domain filter → 11 probed → **3 shelvable**.
That is **0.9%**, against `p388`'s **5.7%** (22 of 383). 🟢 The channel is **depleting, not
exhausted** — it still produced three rows, one of which opened a category (`Pattern W`). 🔴 But the
seam `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary.
🔴 **And the instrument nearly lied:** the first draft of the domain filter matched the query column
of its own output and "confirmed" 37 education rows that were Vercel, AWS and Storybook packages.
Caught before a shelf. *A filter that scores its own prompt is not a filter.*

## Trend 13 — 🆕 `p389` The supply has a currency problem, and it is now a number

This base has built a careful discipline about *licences* and almost none about *time*. `p387` and
`p388` both recorded that no maintenance signal was available. It was: **`git` read access is open to
every public repository**, and a blobless shallow clone returns the last commit date at the real
default ref in about a second. Sixty addresses were dated this pass.

**The distribution, which is the trend.** 58 live, 2 dead. **48 of 58 moved within 30 days**, and 17
of those were committed **on the day of the pass**. That is a healthier supply than this industry's
reputation suggests — education tooling is unglamorous, not abandoned. But **7 of 58 are past 120
days, and four of those seven carried a recommendation on these shelves**:

| stale address | days | what it was being recommended for |
|---|---|---|
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 343 | a Tier-1 tutor |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 242 | Moodle integration |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 209 | North American curriculum grounding |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 144 | Canvas integration — **and it is ungranted** |

🔵 **The general shape, and it is this base's fourth instance of one error.** `p386`: a count of
addresses is not a count of grants. `p387`: a null leg is not a null supply. `p388`: an exhausted
channel is not an exhausted supply. **`p389`: a closed popularity channel is not a closed maintenance
channel.** Four passes, one mistake — *a property of the instrument reported as a property of the
industry* — and each time the fix was to ask which channel was actually being measured.

🔴 **The procurement consequence, which outlives the instrument.** A licence tells you whether you
*may* build on something. A date tells you whether you will be **alone** on it. Those are different
risks and they price differently: an MIT repository that has not moved in eight months is a
**vendoring decision with a maintenance line in the estimate**, not an integration. Both numbers
belong in the same row of a proposal, and until this pass only one of them was here.

🟡 **And the limit, stated so the number is not over-read.** A commit date says someone pushed — not
to the branch a release is cut from, and not that the project is healthy.
[instructure/canvas-lms](https://github.com/instructure/canvas-lms) is the case in point: `master` is
175 days behind while its `stable/*` branches move, because that is how Instructure ships. A
specification or a dataset that is *finished* is not decaying either. Read the date against what the
artefact is.

## Trend 14 — 🆕 `p389` APAC has become the net exporter of open-source education AI, and the Gulf the net importer

**The supply side.** The largest education-native repository in open source is
[**OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, ~41.3k ★, from **Tsinghua
University**, committed the day of this pass, published in **JCST 2026** and validated inside the
university on **700+ students**. It is not an outlier in its region: the Tier-1 tutor shelf on
[`agents/top.md`](../agents/top.md) is now **majority APAC by origin** — DeepTutor (HKU, Apache-2.0),
ai-shifu (China, Apache-2.0), educhain (India, MIT), OpenTutor (China, MIT), Aha Tutor (China, MIT),
learn-shell (China), ChatTutor (APAC) — against one EMEA entry (mentingo, Poland) and, at Tier 1, one
North American (tutor-gpt, now 343 days stale). 🔵 **The pattern is not "China ships a lot of AI."**
It is that **the pedagogy is being designed in the repository** — mastery estimates that record
*confidence* separately from correctness, FSRS review built in, cognitive-load detection,
misconception-aware branching — in projects whose authors are university teaching groups rather than
startups. That is a supply a studio can build a practice on, and its licences are permissive.

**The demand side, created by statute rather than by procurement.** The **UAE** approved an AI
curriculum across **all public and private schools** by Cabinet decision in September 2026, with
**22,000 teachers and education professionals** to be trained, and for 2026-27 merged Design,
Innovation and Computer Science into a single subject, *Artificial Intelligence and Technology*,
KG–Grade 12. **Saudi Arabia** began a comprehensive AI curriculum across all levels of public
education in the 2025-26 academic year, led by the **National Curriculum Center** with **SDAIA**.
These are the most aggressive AI-in-education mandates anywhere: not permission to pilot, a
**compulsory subject with a teacher-training number attached**.

🔴 **And the mismatch is the opportunity.** This pass found **no Gulf-origin and no Arabic-first
open-source education agent or platform** — not one address. The region with the world's strongest
statutory demand for AI teaching material has, as far as this base can see, **no local open-source
supply at all**, while the permissive supply that does exist is EN + zh-CN. The gap is not a model
gap; it is **curriculum-grounding and language**: Arabic-first content, alignment to the UAE MoE's
seven curriculum areas, and the teacher-training surface those 22,000 professionals will be trained
on. 🟡 Recorded as an informed gap, not a finding: the searches run were English-language, and an
Arabic-language search is the obvious next leg.

## Trend 15 — 🆕 `p389` The parent surface now has a cautionary case, and it is in LATAM

`p388` added the parent/guardian persona and named **FERPA** as the line that splits a family-run
assistant from a district-hosted one. The LATAM equivalent of that line is **LGPD Article 14**, and
unlike FERPA it already has a public failure attached to it.

- **Brazil has no AI statute in force.** As of October 2026 **PL 2338/2023** — passed by the Senate
  in December 2024 — is still in the Câmara dos Deputados, with reports that the vote resumes after
  the October 2026 elections. So the binding instrument for an education engagement today is the
  **LGPD**, not an AI law.
- **Children's data has its own consent basis.** For core teaching a school generally relies on
  contract and legal obligation, but uses **beyond** that — images, communications, extracurricular
  activity — require **specific, explicit, recorded and revocable consent from a parent or guardian**
  under Art. 14. An AI parent portal is squarely in the "beyond" category.
- **The cautionary case.** In 2023 the São Paulo state education department (**SEDUC**) had its
  *Minha Escola* app installed on parents' phones without notice or consent; Data Privacy Brasil
  assessed it as a probable LGPD violation. 🔵 **This is the precise failure mode of the persona
  `p388` added** — a district-hosted parent surface deployed *to* families rather than *for* them —
  and it is the reference a LATAM client will have in mind, so bring it up first.

🟢 **What this makes defensible rather than risky.** The pattern that survives Art. 14 is the one
`Pattern P-1` already describes: the **family runs the agent and exercises its own access right**, so
no new disclosure is created. For the district-hosted variant (`P-2`), the deliverable a Brazilian
client should be sold is the **consent and revocation mechanism itself** — per-guardian, recorded,
revocable, auditable — as a first-class feature, not a checkbox. 🟡 **Mexico: informed gap.** No
education-specific AI guidance or student-data rule was found for Mexico in this pass; the general
position is a data-protection regime and no AI statute. Stated, not inferred.

## Trend 16 — 🆕 `p390` The copyleft firewall moved inside the platform, and it is a packaging decision rather than a licensing one

For several passes this shelf framed "permissive agent + copyleft platform" as a problem solved at
the **boundary**: hold the agent outside the LMS and talk to it over LTI or MCP, so no copyleft
reaches your code. That is still a valid pattern, but `p390` found the cleaner answer was in the
platforms' own packaging the whole time, and **nobody had read it per-package**:

| package | role | licence |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | the platform you deploy | 🔴 **AGPL-3.0** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | the component API your plugin imports | 🟢 **Apache-2.0** |
| [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | what you develop against | 🟢 **Apache-2.0** |
| [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) | newer core data layer | 🔴 **AGPL-3.0** |

All four read from the payload at their real default ref on **2026-10-22**; the two Apache grants are
at `LICENSE.TXT`, which is also why a badge-level or root-`LICENSE` read misses them.

**Why this is a trend and not a trivium.** It means the in-platform plugin — the deepest, most
useful integration, with full access to course state and no network hop — is **also** the one that
can stay MIT or proprietary. The industry had been treating depth of integration and licence freedom
as a trade-off, and for Open edX specifically they are not. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(MIT, Universidad Tecnológica de Pereira) has been shipping on exactly this basis.

🔴 **The trend has a sharp edge: the boundary is per-package, and it is moving.** `openedx-learning`
is the newer core data layer and it is **AGPL-3.0**. As more platform functionality migrates there,
the set of imports that keeps a plugin permissive **shrinks**. Audit the dependency list in CI, not
once at kick-off. The general rule this generalises to: **licence is a property of the package you
import, not of the organisation that publishes it** — and in education, where every major platform is
copyleft, that distinction is worth real money.

## Trend 17 — 🆕 `p390` Voice is the next interface gap, and the open-source supply has not arrived

Across seven passes these shelves accumulated tutors, graders, LMS connectors, parent portals and a
generated classroom. **Every one of them is text-first.** `p390` found exactly **one** granted
voice-first education agent in the open-source supply — [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
(MIT, Brazil, pt-BR, 15 days old, self-described as *"in development"* with no public deployment).

**Why the gap matters commercially.** Voice is not a convenience feature in this industry; it is an
access feature, and it maps onto precisely the markets with the fastest growth and the least supply:

- **Early grades**, where reading and typing fluency is the thing being taught, not assumed.
- **Shared-device and phone-only households** — the LATAM and APAC reality `Trend 10` documents.
- **Language learning**, where pronunciation *is* the assessed skill and text cannot carry it.
- **Accessibility**, which in EMEA public procurement is frequently a scored requirement rather
  than a nice-to-have.

**Why the gap is narrow rather than deep, which is the opportunity.** The hard parts are already
permissive and maintained: [`livekit/agents`](https://github.com/livekit/agents) (Apache-2.0) solves
turn detection, interruption and barge-in — the things that actually make a spoken tutor usable — and
[`mozilla/common-voice`](https://github.com/mozilla/common-voice) supplies **CC0-1.0** speech corpora
across ~130 language variants for ASR evaluation and fine-tuning. What is missing is not
infrastructure; it is **an education-grade assembly of it** — mastery model in the loop, symbolic
checking behind the arithmetic, and the biometric/disclosure posture a school can sign.
🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md) is that assembly.

🔴 **`Gap 390-A` — the informed gap, stated rather than left as silence.** The searches this pass ran
for an open-source voice or multilingual tutor in an **African or South Asian language** returned
**nothing granted and maintained**. What came back instead: one India-first multilingual *toolkit*
(not a tutor), an arXiv framework for low-cost home language learning with **no public code located**,
and a repository that teaches *Spanish to non-speakers* inside an agent CLI — which is the inverse of
a Spanish-language tutor for Spanish-speaking learners, a category error this base recorded in `p388`
and which keeps recurring in search results. 🔵 **Read this as a null result in the open-source
supply, not a null in demand** — Africa is among the fastest-growing online-education markets. For a
client engagement in those languages the honest position is: **the substrate is permissive and ready,
the localised tutor does not exist and would be built, and Common Voice is where its evaluation set
comes from.**


## Trend 18 — 🆕 `p391` Education AI is shipping as **harness extensions**, not standalone applications

Three of this base's education rows are now plugins to the *same* agent harness, by **three
unrelated maintainers**, all MIT, all published inside about ten days:

| row | what it is | published |
|---|---|---|
| [`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (`p388`, Tier 1) | narrated-blackboard adaptive tutor | npm v1.7.0, 2026-10-22 |
| [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🆕 `p391`, Tier 1) | diagnosis-first learning runtime | npm v0.1.1, 2026-10-17 |
| [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (🆕 `p391`) | K8s + OIDC multi-tenant hosting for the same harness | npm v0.10.0-rc.1, 2026-10-12 |

They are extensions to **DeepSeek Harness**, and the pattern is not harness-specific — this pass also
read [`mackt/pi-language-tutor`](https://github.com/mackt/pi-language-tutor) (MIT) as an extension to
the Pi agent. 🟢 **Why it is a trend and not a coincidence:** a harness extension inherits model
plumbing, tool calling, auth, UI shell and a distribution channel for free, so a single maintainer can
ship a credible tutor in weeks. The economics now favour the plugin over the application.

🔵 **The operational consequence, and it explains a channel result this base has hit repeatedly.** The
distribution channel for education AI is becoming **the agent harness's package registry** — which is
why `registry.npmjs.org` keeps yielding education supply while `moodle.org` has never once been
reachable *or* necessary. Looking for education AI in LMS plugin directories is looking where it was
built in 2019.

🔴 **The cost a studio inherits, stated plainly.** A harness extension is **not deployable without its
harness**. `dsh-diagnostic-tutor` requires DeepSeek Harness; adopting it means adopting that runtime,
its update cadence and its governance. For a client who cannot, the move is to copy the *structure*
(see `Pattern X`) rather than the package — which is exactly why `Pattern X` separates the pedagogy
from the runtime instead of recommending the repository wholesale.

## Trend 19 — 🆕 `p391` The standards body's reference implementation goes stale; the **vendor fork** carries the maintenance

`p390` dated [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) at 2,332
days and concluded the LTI 1.3 integration path had no installable implementation. The grant and the
dating were both right; the conclusion was wrong, because the maintained line is not at the
authoritative-looking address:

| address | last commit | registry | verdict |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **2026-10-16** | packagist `lti-1p3-tool` **v6.4.4**, 68 versions, 2026-09-23 | 🟢 **install this** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Node) | **2026-10-13** | npm `ltijs` **v7.0.7**, 207 versions, 2026-10-06 | 🟢 **install this** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 2020-06-03 | — | 🔴 spec citation only |
| [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) | 2020-06-03, **identical sha `3a192de`** | — | 🔴 the same project, renamed org |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) | 2022-11-21 | PyPI `PyLTI1p3` 2.0.0, **2022-11-20** | 🔴 genuinely dead |

🟢 **The generalisable rule:** in standards-driven education interop, the consortium publishes the
spec and a demonstration; a **vendor with production traffic** maintains the library. So when a
reference implementation dates badly, the next question is *who ships this in production* — not
*should we vendor the spec*. Check the fork network and the package registry before concluding a path
is closed.

🔴 🆕 `p392` **The "language asymmetry" half of this trend is WITHDRAWN, and withdrawing it sharpens
the rule above rather than weakening it.** `p391` closed this trend with: *"Node and PHP have
maintained LTI 1.3; Python does not… the interop edge is therefore a separate Node or PHP service in
front of the agent."* Read first-hand this pass, **Python has three**:

| address | grant | last commit | registry | role |
|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | **2026-10-20 — 2 d** | PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07 | 🟢 **in-process**, Django app + middleware |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 — 113 d | PyPI **v1.6.3**, 15 releases | 🟢 LTI 1.1 **and** 1.3 into JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | **2026-10-22 — 0 d** | PyPI `lti-consumer-xblock` **v11.4.2** | 🔴 best-maintained of the three, **copyleft** |

🟢 **And the maintainer pattern holds in Python too, which is the trend's real content.** The three
Python implementations are maintained by a **university innovation centre** (Michigan), an
**ecosystem project** (Jupyter) and a **platform vendor** (Open edX) — not by the standards body. The
rule is unchanged and now has six instances instead of four: *in standards-driven education interop,
ask who ships this in production.*

🔴 **What survives as a constraint is licence-shaped, not language-shaped**, and that is a more useful
thing to tell a client: the best-maintained Python LTI implementation is **AGPL-3.0**, the
best-maintained Node one is Apache-2.0, and the permissive Python options are smaller (26 ★ and 73 ★)
and framework-bound. The question is never *"does this language have LTI"* but *"does the maintained
implementation in my language carry a grant I can ship?"* `Gap 391-A` **CLOSED**.

## Trend 20 — 🆕 `p392` The granted proctoring supply covers the **lockdown**, not the **inference** — which is the opposite of the regulatory exposure

For four passes this base recorded proctoring as having *"no credible permissive open-source option"*
and treated that as a liability boundary to name rather than fill. Probed first-hand, the supply
exists — and its **shape** is the trend:

| component | grant | last commit | what it actually does | the AI part |
|---|---|---|---|---|
| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) | 🟢 **MIT** (1,069 B, manifest agrees) | **2026-09-28** | tab-switch, right-click, DevTools shortcuts, clipboard events, camera state, **faces**, audio loudness, **virtual-camera / loopback / screen-share detection** | 🟢 **real** — face-api on TF.js, **in the browser** |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 🔴 **CONFLICT** — Apache-2.0 payload, `ISC` manifest **and** npm | **2026-10-13**, 398 commits | blocks copy/paste/cut, right-click, selection, shortcuts; detects `tabSwitch`, `browserBlur`, `exitTab`, `fullScreen`; periodic page and webcam snapshots POSTed to an endpoint you build | 🔴 **absent** — object detection, multi-face and eye tracking are marked *"(To be Done)"* |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🔴 **AGPL-3.0** | 🆕 re-read `p392`: `master` HEAD **2026-10-22 — 0 d** (this base's harvest row said 2026-05-30; the live read is today), 253 releases | the exam **workflow** — attempts, review states, integration points | 🔴 none; it brokers a vendor |

🔵 **The asymmetry, stated as a rule:** open-source proctoring is **deterministic browser lockdown and
event telemetry**, while the **inference** — identity, gaze, multiple faces, behavioural scoring — is
either absent, roadmapped, or the proprietary service the AGPL workflow brokers. 🟢 **And the
regulatory exposure runs the other way.** Lockdown and event logs do no biometric inference: they
are not what the EU AI Act's Annex III is reaching for, and they are explainable to a student
(*"you left fullscreen at 14:03"*). The inference layer is where high-risk obligations, biometric
rules and the whole evidentiary argument live — and that is exactly the layer the permissive supply
does not have.

🟢 **So the honest advice to a client flips, and it is now sellable in both directions:** *we can
build the integrity layer you can defend — lockdown, event trail, human review — permissively and
today; the part that would flag a student automatically is the part that makes you a deployer of a
high-risk system, and neither of us should want it in v1.* 🔴 The obligation attaches to the
**deployment**, not the dependency, so an open-source grant transfers no compliance relief whatsoever.

## Trend 21 — 🆕 `p392` LATAM's public buyers are procuring AI education platforms as **subscriptions**, and no tender asks for open source

A replacement regional leg shaped like a **buyer** rather than a supplier — public-procurement
vocabulary in Spanish and Portuguese — returned five live 2026 instruments where three passes of
English, stars-sorted supply legs returned nothing: Santa Fe province (Argentina, Tender 01/26,
*subscriptions* to AI-enhanced educational cloud platforms), **OEI-Chile `OEI-LIC-1-25`** (design and
build of an AI platform for **administrative management in Chilean schools** over regulatory,
financial and operational data), UNOPS Argentina `ITB/2026/62779` (educational platform **licences**,
2+2 years), the **CIEDEPAR** consortium in Paraná (multi-municipality SaaS education management) and
Francisco Morato, SP (**R$1,924,665.00**).

🔴 **Not one of the five specifies free or open-source software.** The spend is real, the AI framing
is explicit, and the procurement shape is **product subscription**.

🔵 **Why this is a trend and not five anecdotes:** it is the demand-side mirror of *Trend 6*. This
base's whole thesis is permissive assembly, and the buyers writing the cheques are specifying
subscriptions — so the binding constraint on an open-source education engagement in LATAM is **the
specification, not the licence frontier**. 🟢 The opening is a total-cost bid against subscription
pricing, with the OEI-Chile scope (administrative management, compliance recommendations) matching the
`i-educar` + agent shape these shelves already hold; the work is to get *"or equivalent open-source
implementation"* into a specification written for a product. 🟡 Graded **`ATTRIBUTED-UNVERIFIED`** —
aggregators and news items; no official portal (COMPR.AR, ChileCompra, PNCP) is reachable here.


## Trend 22 — 🆕 `p393` The education **interoperability layer is Python** while the agent layer is TypeScript, and a one-registry sweep answers half the question

**What was measured.** `p393` opened the channel `Gap 392-C` said did not exist: `pypi.org/simple/`
under PEP 691 returns **920,784 project names in 45,189,043 B in 1.4 seconds**, unauthenticated. A
sweep of 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, 13 live and
verified first-hand.

**What came back was a layer, not a list.** Not more tutors or more agents — **plumbing**:

| standard / surface | granted Python supply found | grant |
|---|---|---|
| **LTI 1.3 / Advantage** | `openfun/django-lti-toolbox` (France Université Numérique), `Harvard-University-iCommons/django-lti-dynamic-registration` | 🟢 MIT, 🟢 MIT |
| **QTI** (assessment exchange) | `vosslab/qti_package_maker`, `Citolab/qti-convert-python` (Cito, NL) | 🟡 LGPL-3.0, 🔴 GPL-3.0 |
| **OneRoster / Caliper** | the `timeback-*` family — 🔴 **source unresolvable** | 🔴 unauditable |
| **Ed-Fi** (US K-12 data) | `edanalytics/edfi_api_client`; `Ed-Fi-Exchange-OSS/LMS-Toolkit` 🔴 archived | 🟢 Apache-2.0 ×2 |
| **LMS → agent bridge** | `Dathis/swiss-moodle-mcp`, `Snaw80/moodle-mcp` | 🟢 MIT ×2 |
| **Autograding** | `edulinq/autograder-py`; `otter-grader` already carried, now measured at **161 ★** | 🟢 MIT, 🟢 BSD-3 |

🔵 **Why this is a trend and not a haul.** The split is systematic. The **agent** layer — MCP servers
for Canvas, tutors, parent agents — is overwhelmingly **npm/TypeScript**, which is why eleven passes of
npm sweeps built a rich agent shelf. The **standards and institutional-data** layer is
**PyPI/Python**, because it lives next to the Django and Flask applications that universities and
ministries actually run (Open edX, `now-lms`, campus SIS integrations) and next to the
notebook-and-grading stack. 🔴 **A supply claim is therefore only as wide as its registry.** This base
published *"there is no maintained Python LTI 1.3 library"* (`Gap 391-A`) from a channel that
**cannot index PyPI** — and then found five.

🟢 **The rule for a studio:** one discovery channel per ecosystem, named before any absence is
published. This base's set is now npm + PyPI + Packagist (measured, 0 yield) + `git ls-remote` and
`raw.githubusercontent.com` for verification. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** —
and CRAN matters here, because `otter-grader` grades **R** and the statistics-teaching stack is
R-shaped.

🔴 **The cost of the channel, stated with it:** the dump carries **names only**, so it discovers by
token and a token is not a capability. Two of fifteen candidates were pure collisions — `proctor-ai`
is a **prompt-engineering** library, `xapi-python` is the **xStation5 broker API** — and whole keys are
unusable (`canvas` returns 146 names dominated by HTML-canvas and AWS Nova Canvas; `d2l` is
Dive-into-Deep-Learning). Discovery is cheap; **adjudication is the work**.

## Trend 23 — 🆕 `p393` A new supply class: **live releases, dead source** — and the licence claim is unauditable in principle

**The instances, found the same hour.** [`superbuilders/timeback-dev-python`](https://github.com/superbuilders/timeback-dev-python)
is the declared `Repository` of **three** actively-released PyPI packages — `timeback-qti`,
`timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last
**2026-07-18**, each declaring **MIT**, together the most complete 1EdTech client family in Python on
paper. 🔴 **The repository does not resolve for an unauthenticated clone.** Second instance:
`moodle-mcp-bridge` v1.7.0, advertising *"a Moodle site as 88 typed AI tools"* → `NmaaAlhawary/MCP-Moodle`,
also unresolvable.

🔵 **Why this is a distinct class and not a variant of an existing one.** This base already grades
three failure modes, and none of them covers this:

| class | the payload | the verdict |
|---|---|---|
| `UNGRANTED` (no licence file) | exists, is empty of a grant | read, and found wanting |
| `README-ONLY` / `MANIFEST-ONLY` | a grant **asserted** somewhere other than a payload | downgraded, because the assertion is checkable against the absence |
| 🆕 **`LIVE-RELEASES-DEAD-SOURCE`** | 🔴 **cannot be fetched at all** | **not assessable** — there is nothing to read, and no amount of care fixes it |

🔴 **The procurement consequence is sharper than it looks.** `p388`'s *"published but unreadable"* was
about a payload that says nothing; this is about a payload that **cannot be obtained**. A studio can
install these packages — pip will resolve them happily — but it **cannot warrant the licence to a
client**, because warranting a grant means having read it. And an MIT declaration in registry metadata
is a claim by the uploader, not a grant in a distributable artefact.

🟢 **What to do with it.** Evaluate in a sandbox if the capability is needed; **never ship it into a
client deliverable**; ask the publisher to open the repository, which is a cheap request and a fair
one. 🔵 And record the class, because the economics favour its growth: publishing to a registry is
free and keeping a public repository is a maintenance commitment, so **more supply will arrive this
shape**, not less.

## Trend 24 — 🆕 `p394` In the teaching stack the **delivery** layer is permissive and the **measurement** layer is copyleft, and a language boundary rides along with it

🟢 **The observation.** `p394` opened the R half of the CS-teaching stack and the licence column split
cleanly down the middle of the pedagogy:

| what it does | components | licence |
|---|---|---|
| **Deliver** the teaching loop — present, accept, grade, respond | `rstudio/gradethis` (**MIT**, 164 ★), `rstudio/learnr` (**Apache-2.0**, 738 ★), `ucbds-infra/ottr` (**BSD-3-Clause**) | 🟢 **permissive, all three** |
| **Measure** the learner — item response theory, adaptive item selection, exam generation, item analysis | `cran/exams` (**GPL-2 \| GPL-3**), `philchalmers/mirt` (**GPL >= 3**), `cran/catR` (**GPL >= 3**), `cran/TAM` (**GPL >= 2**), `ShinyItemAnalysis` (**GPL-3**) | 🔴 **copyleft, all five** |

🔵 **Why it is not a coincidence.** The delivery components are **vendor-authored** — Posit, a company
selling an R platform, and a university programme that needed its autograder to be adoptable. The
measurement components are **academic instruments**, written by psychometricians inside a GPL research
culture and in some cases decades old. **The licence tracks who paid for the code and why**, and it has
produced a split running exactly along the boundary between *product* and *science*.

🟢 **Why that is good news rather than a blocker.** The boundary falls where a studio's product
boundary has to fall anyway: own the teaching loop, reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. 🔴 **The
trap is reading it as a licence problem and swapping in a permissive psychometrics library instead.**
There is no credible permissive equivalent of `mirt` or `catR`; building one is a multi-year research
project and approximating one is how a studio ends up shipping an adaptive engine whose claims it
cannot defend. 🔵 This base already carries the symptom: `adaptive-knowledge-graph` (~350 ★) and
`OATutor` implement IRT and BKT from scratch, and `mirt` — **235 ★, committed daily** — is the thing
they are approximating.

🔵 **And the language boundary rides along with it.** `Trend 22` recorded that the agent layer is
npm/TypeScript while the standards layer is PyPI/Python. `p394` adds that the **measurement** layer is
**CRAN/R**. Three layers, three registries — and a supply claim is still only as wide as the registry
it was swept from. 🔴 **R is the worst case of the three**, because its registry is unreachable here on
**both** tools and its grants are invisible to GitHub's licence sidebar (`Gap 394-B`): five granted GPL
packages in this tier show **no licence** in the GitHub UI, because the grant lives only in
`DESCRIPTION`. **So a GitHub-UI-driven sweep does not merely under-count R supply — it reports it as
unlicensed.**

## Trend 25 — 🆕 `p394` A string matched as though it were a meaning is this base's most productive error class, and it runs in three directions

🟢 **The observation, as a count rather than an impression.** Three independently-found defects, three
different instruments, one mechanism:

| gap | instrument | direction | what the string was |
|---|---|---|---|
| `Gap 392-A` | capability-absence gate | 🔴 **over-refutes** — denies a real absence | a runtime key read as a capability |
| `Gap 393-A` | PyPI index channel | 🔴 **over-discovers** — invents supply | a package *name* read as a capability (`proctor-ai`, `xapi-python`, `canvas`, `d2l`) |
| **`P459`** 🆕 | `licence-grant-gate` | 🔴 **strips a grant** — denies a real permission | **"all rights reserved"**, line 2 of the canonical BSD template, read as a refusal |

🔵 **`P459` is the most expensive of the three and it was the last to be found**, because the other two
produce *visible* nonsense — a claim you can check, a candidate you can reject — whereas this one
produces a **false absence of a grant**, which looks exactly like diligence. A usable component is
quietly marked unshippable and nobody re-opens the question. 🟢 On these shelves its realised damage
was **nil** — no published row was graded from an untitled BSD payload, checked rather than assumed —
and its exposure was **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells.

🔴 **And the fourth instance is on this base's own shelf rather than in an instrument.**
`anastasasenov/bbmcps` sat in the Blackboard census for eight passes because its URL scheme reads
`blackboard://`. It is a shared-memory MCP server; the word is an **architectural metaphor**. So the
class does not only mis-discover and mis-refute — **it mis-files what the base already owns**, and a
census cell inherited as a count is exactly where it hides.

🟢 **The transferable rule, and it is cheap.** Before a token decides a verdict, ask what else that
token means. The gate that got this wrong already holds the right idea one screen away:
`AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`, with a comment noting each is simultaneously a
licence name and something else. 🔵 **The insight was applied to licence names and never to licence
clause text, nor to package names, nor to URL schemes.** One lexicon separating a **string** from a
**capability** would close `Gap 392-A`, `Gap 393-A` and the `bbmcps` class together — which is why
`p393` ranked that unification fifth and why `p394` ranks it **first**.
