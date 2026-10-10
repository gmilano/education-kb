---
industry: education
region: Global
updated: 2026-10-10
---

# Education — current trends

**Pass 91, 2026-10-10.** Seven trends, each tied to something measured or dated this pass.

## T1 — The unit of delivery is the *agent skill*, not the application

🟢 **Holds on a second measurement.** `topics/ai-tutor` holds **664 repos** — unchanged from pass 90, so the
denominator is stable rather than inflating. Roughly a quarter of the first two pages are **skills for agent
harnesses** rather than web applications: markdown-plus-scripts packages with no UI, no hosting, no database
and no migration. `universal-examprep-skill` (303★), `universal-diagnostic-tutor-skill` (242★), `Bloom` (285★,
explicitly *"self-hostable AI tutor **and** Claude Code skill"*), `kaogong-skill` (166★), `education-skills`
(107★).

🟢 **Near-uniformly MIT** — every skill row verified this pass read MIT from the payload.
🟢 🆕 **And the shape has now crossed into a second tier.** `tomaszboloz/WCAG-Accessibility-Skills` (MIT) is
**both** an agent skill **and** an accessibility checker, and `Community-Access/accessibility-agents` (MIT)
ships eleven review agents for coding hosts. **The skill is becoming the delivery vehicle for compliance
tooling, not just for tutoring** — which is a more defensible sale, because it attaches to a standard.
🔴 **The counter-risk is unchanged:** a skill inherits the host's model, limits and data policy. Where
automated assessment is regulated (Korea, Vietnam) or student-data training restricted (California AB 1159),
"it is just a skill" is not a compliance position.

## T2 — A vertical with its own licence family gets undercounted as copyleft by generic tooling

🟢 **Pass 90's finding, now fixed in code rather than only described.** `Sakai` and `Opencast` are
**ECL-2.0** — the Educational Community License, OSI-approved, Apache-2.0-derived, **permissive**. v2's
classifier returned `OTHER/unclassified`; unclassified reads as risk and gets dropped, which is part of how
*"8 of 8 copyleft"* survived six passes. 🟢 **`grant-ladder-v3` tests ECL *before* Apache** (ECL is
Apache-derived, so an Apache test swallows it) and both rows now classify. `OTHER/unclassified` across the
92-slug shelf went **2 → 0**.

🟢 🆕 **The same reasoning extended, pre-emptively, to the licences this industry will meet next:**
**EUPL-1.2** (the European Union Public Licence — the grant EU public bodies are steered toward, so it will
appear in EMEA public-sector education tenders) and three **source-available, non-OSI** families now named
rather than dropped: **BSL-1.1**, **Fair Code** and the **Sustainable Use License**. 🔴 That last group
matters because `leemonade/leemons` (292★, listed on `topics/lms`) is **Fair Code License v1.0 — not open
source**, and v2 would have shown it as merely "unclassified".

🔵 **The transferable rule: name the family, including the families that are not open.** Silence and a
refusal are both "unclassified" to a reader, and only one of them is a warning.

## T3 — Adoption is near-universal; governance is the market

Consistent across every region measured. 🆕 The LATAM governance figure is now a *measured* one rather than a
paraphrase.

| region | adoption | governance |
|---|---|---|
| North America | 86 % of orgs; 60 % of K-12 teachers | 🔴 134 bills / 31 states; 🆕 **only ~10 % of institutions have formal guidelines, and 71 % of teachers report no AI training** |
| LATAM | 🟢 87 % of institutions (UNESCO IESALC, 200 institutions / 19 countries, fieldwork **Aug–Oct 2025**); 92 % of students, 🆕 **79 % of faculty** | 🔴 🆕 **26 % have any formal framework** (UNESCO's own figure); no sectoral regulation anywhere in the region |
| APAC | fastest growth, 28.1 % CAGR | 🟡 the world's most advanced *and* most fragmented law — **plus three curriculum mandates** (see `T7`) |
| EMEA | 🟡 🆕 **first numbers ever recorded here** — UK: 36 % feel encouraged by their institution, 38 % are provided AI tools (HEPI, n=1 054) | 🟢 the most defined calendar: AI Act high-risk **2 Dec 2027**, 🆕 **Art. 4 literacy duty in force now** |

🟢 **The number to carry into a pitch has changed, and it is stronger than pass 90's.** Not "92 % use against
30 % effective" — which rested on a figure this pass found mis-stated — but **92 % of LATAM students using AI
against 26 % of institutions having any framework at all**, both from named instruments with stated sample
sizes. 🔵 **The purchasable artefact is governance plus capability: policy, disclosure, assessment redesign,
staff training, and an audit trail.** North America's 71 %-untrained figure says the capability half is the
bigger one.

## T4 — The EU AI Act has **two** deadlines, and the one that binds now is the one nobody cites

🟡 High-risk obligations — education among them — moved to **2 December 2027** (Digital/AI Omnibus, Council
approval 29 Jun 2026); embedded high-risk systems to 2 Aug 2028. Enforcement *powers* still begin 2 Aug 2026.
🔴 **A large share of vendor and consultancy guidance still states August 2026 for high-risk duties, and this
pass found that exact error again in a current source.**

🟢 🆕 **The addition that changes the pitch: Article 4's staff AI-literacy duty is already in force and was
not deferred.** So the EMEA conversation is not "prepare for a 2027 deadline" — which invites delay — but
"there is a duty you are already subject to, and a 14-month window on the larger one". 🔵 **Two deadlines, two
sales: literacy now, high-risk conformity by Dec 2027.** The first funds the second.

## T5 — Generators are saturated; the checker gap is now **half closed**, and the remaining half is sharper

🔴 **What this KB published for five passes:** *"a targeted search for AI accessibility/alignment checkers in
education returned nothing usable"* and *"the only accessibility checker found is `UDOIT` — GPL-3.0, and not
AI-driven."* 🟢 **The accessibility half is FALSE and was falsified on the first targeted query this pass.**
Three permissive, AI-driven WCAG checkers verified from the payload: `tomaszboloz/WCAG-Accessibility-Skills`
(MIT), `Community-Access/accessibility-agents` (MIT), `9mtm/WCAG-Checker` (MIT, covers **PDF** as well as web).

🔵 **Why the shelf missed them, and this is the transferable part: the query named the industry.** Searching
*"accessibility checker **education**"* returns LMS plugins, and the LMS plugin in this space is GPL. Dropping
the industry term and searching the **standard** — WCAG — returns permissive, AI-driven tools immediately.
🟢 **A compliance tool is named after the standard it enforces, not the sector that buys it.** This is `P870`
(re-point the vocabulary) in a new guise, and it is the second time this pass that changing the query word
rather than the query target discharged a long-standing gap — the other being **CBSE** for India.

🔴 **What still does not exist: an instructional-alignment checker under a permissive grant with usable
evidence.** The narrowed specification, which is more useful than the old blanket claim:

| candidate | why it does not close the gap |
|---|---|
| `nsip/curriculum-mapper` (Apache-2.0, Australia) | 🔴 **archived, read-only**, keyword-based not semantic |
| `learning-commons-org/evaluators` | 🔴 **the corpora that make it evidence-backed are CC-BY-NC-SA** — see `T6` |
| `Zion-support/curriculum-alignment-checker` | 🔴 no licence payload in 24 filenames; self-describes as batch-generated |
| `lovejzzz/CourseMapper` | 🔴 no licence payload in 24 filenames; own README logs attribution failures |

🔵 **A checker remains the easier enterprise sale** — it does not displace the educator, it evidences
compliance. With North America at ~10 % guideline coverage and WCAG/508 exposure, **the accessibility half can
now be composed rather than built, and the alignment half is a clean, specified build.**

## T6 — 🆕 In the checker and dataset tier, the grant splits along code / prompt / corpus lines — and the permissive part is not the valuable part

🟢 **The most commercially consequential finding of this pass.**
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) ships **one**
`LICENSE.md` granting **four different things**:

| layer | grant | usable in a paid deliverable? |
|---|---|---|
| evaluator **code** | **MIT** | 🟢 yes |
| **prompts and settings** | **CC-BY-4.0** | 🟢 yes, with attribution |
| **Annotated CLEAR Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |
| **Annotated PERSUADE 2.0 Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |

🔴 **The non-commercial clause sits precisely on the annotated corpora — which are what make it an
evidence-backed rubric evaluator rather than a prompt template.** 🔵 **So the question in this tier is not
"is it permissive" but "is the permissive part the valuable part". Here it is not.**

🟢 **A second shape, same lesson:** `learning-commons-org/knowledge-graph` licenses **per dataset and per
download** — `Open` / `Open + Gated` / `Gated` — through a platform catalogue, and states in terms that its
gated content is **not** covered by the CC licences the same file references. **A repo-root licence read
cannot resolve a data-layer grant.**

🔵 **Generalisation worth carrying to every other industry KB: as AI work moves from code to
code-plus-evaluation-data, licence risk migrates from the repository to the corpus, and corpora are where
non-commercial clauses live.** Pass 90 found a 2-way split (`microsoft/autogen`: docs CC-BY, code MIT) and it
was benign. This is a 4-way split and it is binding.

## T7 — 🆕 The regulatory frontier has moved from *regulating AI systems* to *mandating AI instruction* — and that is a services market, not a compliance cost

🟢 **Four jurisdictions now compel AI *teaching*, three of them in APAC, all dated:**

| jurisdiction | instrument | from | reach |
|---|---|---|---|
| 🇨🇳 China | Ministry of Education — compulsory from **age six**, tiered primary→secondary | **Sep 2025** | **≥ 8 hours per year, nationwide** |
| 🇸🇬 Singapore | Ministry of Education — AI literacy across curriculum, co-curriculum and self-directed learning, with developmental milestones | announced **Mar 2026** | **all schools by 2027**, via Student Learning Space + IMDA modules |
| 🇮🇳 India | CBSE — *Computational Thinking and AI*, **Classes 3–8**, notification **9 Apr 2026** | session **2026-27** | CBSE-affiliated schools; aligned to NEP 2020 / NCFSE 2023 |
| 🇪🇺 EU | **AI Act Article 4** — staff AI-literacy duty | 🟢 **in force now** | every institution deploying an AI system |

🔵 **Why this is a different business from everything else in this file.** A risk-classification regime
creates work that is defensive, legal-led and priced as compliance. A **curriculum mandate creates work that
is constructive, educator-led and priced as delivery**: someone must write the material, localise it to each
jurisdiction's scope and hours, train the teachers who have never taught it, and assess it.
🔴 **And the supply is thin where it matters.** The permissive AI-literacy curricula that exist
(`microsoft/ai-agents-for-beginners`, `rohitg00/ai-engineering-from-scratch`,
`pguso/agents-from-scratch`, `huggingface/agents-course` — all MIT or Apache-2.0) are written for **adult
developers**, not for **eight-year-olds in Class 3**. 🟢 **Nothing on this shelf addresses the primary-school
mandate that China has already implemented and India starts this session.**
🔴 **And curriculum is content, so it is where NC clauses cluster** — `cccareers/open-source-curriculum` is
**CC-BY-NC-SA**, unusable in a paid deliverable.

🔵 **This also corrects a sentence this KB carried for several passes.** The shelf said *"Singapore and Japan
stay deliberately voluntary"*. 🟢 **True of Singapore's position on regulating AI systems; false of its
position on AI in schools.** Voluntary regulation and mandated curriculum are different axes, and conflating
them understated the region's most purchasable commitment.

## Instrument note carried forward

🟢 **`git ls-remote --symref` and `raw.githubusercontent.com` discriminate; `curl` on `github.com` and
`api.github.com` return 403 for real and invented slugs alike and must not be used.**
🆕 **Newly recorded: `WebFetch` on `https://github.com/topics/<t>` renders the page, its star counts and the
topic total, while `curl` on the identical URL is 403.** That is where star counts and topic denominators come
from.
🔴 **Re-confirmed (`P944`/`P950`): the policy-source block is an EGRESS ALLOWLIST, not DNS.** Four primary
hosts needed this pass — `cbse.gov.in`, `digitaleducationcouncil.com`, `hepi.ac.uk`, `unu.edu` — returned
`000`/0 B under `curl` and `ENOTFOUND` under `WebFetch`. Not retried per host. Figures from them are labelled
*search-summary* in `intel/market.md`.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
