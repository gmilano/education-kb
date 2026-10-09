---
industry: education
region: Global
updated: 2026-10-09
---

# Education — current trends

**Pass 90, 2026-10-09.** Six trends, each tied to something measured or dated this pass.

## T1 — The unit of delivery is becoming the *agent skill*, not the application

🟢 **The clearest new signal in the supply this pass.** A large and fast-growing share of `topics/ai-tutor`
(664 repos) is no longer web applications but **skills for agent harnesses** — markdown-plus-scripts packages
that run inside Claude Code and comparable hosts. Measured on the first two pages (40 rows), roughly a quarter
are explicitly skills: `universal-examprep-skill` (303★), `universal-diagnostic-tutor-skill` (242★),
`education-skills` (107★), `kaogong-skill` (166★), `study-assistant-skills`, `sijiao-skill`, `feynman-tutor`,
`learn-anything`, `Tov-learn`.

🟢 **They are near-uniformly MIT** — every skill row verified this pass read MIT from the payload.
🔵 **Why it matters commercially:** a skill has no UI, no hosting, no database and no migration. Pedagogy ships
as a versioned text artefact that runs inside whatever harness the client already licenses. For a studio this
is the cheapest delivery vehicle that has ever existed in this industry, and the licence tier means it can be
built on without a copyleft conversation.
🔴 **The counter-risk:** a skill inherits the host's model, limits and data policy. In a jurisdiction that
regulates automated assessment (Korea, Vietnam) or student-data training (California AB 1159), "it is just a
skill" is not a compliance position.

## T2 — The permissive platform tier was real all along, and the licence *classifier* was part of why it looked empty

🔴 **This KB asserted for six passes that the education platform tier was `8 of 8 copyleft`, corrected it in
pass 89 to `2 of 10`, and this pass measures at least 9 permissive platforms.** Two failures stacked:

1. **No membership criterion.** Each census reported the licence mix of whatever sample the prior pass left
   behind. 🟢 Fix: state the criterion before counting (`verticals/solutions.md` now does).
2. 🟢 **A licence family the tooling did not recognise.** `Sakai` and `Opencast` are **ECL-2.0** — the
   Educational Community License, OSI-approved, Apache-2.0-derived, permissive. A classifier keyed on the
   familiar families returns *"unclassified"*, and unclassified reads as risk and gets dropped.

🔵 **The generalisable trend, and the one worth carrying to other industries: a vertical with its own licence
family will be systematically undercounted as copyleft by generic tooling.** Education has ECL. The failure was
not carelessness; it was an instrument that did not know a name.

## T3 — Adoption is near-universal; governance is the market

Consistent across every region measured, with the gap widest in LATAM:

| region | adoption | governance |
|---|---|---|
| North America | 86 % of orgs use genAI; 60 % of K-12 teachers | 🔴 134 bills / 31 states, highly divergent district policy |
| LATAM | 🟢 87 % of institutions (UNESCO IESALC, 200 institutions / 19 countries, **Sep 2026**); 92 % of students | 🔴 **no sectoral regulation; non-binding guidance only** |
| APAC | fastest growth, 28.1 % CAGR | 🟡 the world's most advanced *and* most fragmented law |
| EMEA | 🔴 not measured this pass | 🟢 the most defined calendar: AI Act, high-risk, **2 Dec 2027** |

🟢 **The number to carry into a pitch is LATAM's 92 % student use against 30 % who consider their institution's
integration effective.** Adoption is not the problem anywhere. 🔵 **The purchasable artefact is governance:
policy, disclosure, assessment redesign, staff capability, and an audit trail.**

## T4 — The EU AI Act deadline moved, and most published guidance is now wrong

🟡 **High-risk obligations — education among them — moved to 2 December 2027** (Digital/AI Omnibus, Council
approval 29 Jun 2026); embedded high-risk systems to 2 Aug 2028. Enforcement *powers* still begin 2 Aug 2026.
🔴 **A large share of vendor and consultancy guidance still states August 2026 for high-risk duties.** The
practical effect is a ~14-month build window that institutions believe they have either already missed or
already survived. Both beliefs are wrong and both are a reason to buy.

## T5 — Generators are saturated; checkers barely exist

🟢 **Measured, not impressionistic.** The agent shelf is dense with tools that *produce* instructional content
(`DeepTutor`, `educhain`, `mentingo`, `Hyperion`, half of `topics/ai-tutor`) and nearly empty of tools that
*audit* it for alignment, accuracy or accessibility. 🔴 **A targeted search for AI accessibility/alignment
checkers in education returned nothing usable this pass**; the only LMS accessibility checker found,
`ucfopen/UDOIT`, is **GPL-3.0 and not AI-driven**.

🔵 **A checker is also the easier enterprise sale** — it does not displace the educator, it evidences compliance
with accessibility and alignment standards. Against North America's WCAG/508 exposure and its mandated district
AI policies, this is the most clearly unserved build on the shelf.

## T6 — Licence metadata in this industry is unreliable, and blogs are the worst source

🔴 **Measured on 92 slugs resolved this pass:**

| finding | count |
|---|---|
| no licence payload in **17** candidate filenames | **6** (~1 in 15) |
| licence materially mis-stated by a widely-cited source | ≥2 — 🔴 **`frappe/lms` published as MIT, actually AGPL-3.0**; 🔴 **`tutor-gpt` listed as permissive, actually GPL-3.0** |
| **split grant** (docs ≠ code) | 🟡 **`microsoft/autogen`**: `LICENSE` CC-BY-4.0, `LICENSE-CODE` **MIT** |
| slug circulating in roundups that does not exist | **3** — `apereo/opencast`, `tutor-dev/tutor`, `h5p/h5p-standalone` |

🟢 **Operational rule: read the payload, pin the SHA, cite the filename.** An AGPL platform sold to a client as
MIT is a commercial incident, and this pass found that exact error in a top-ranked comparison article.

🔵 **Instrument caveat worth keeping.** Under this session's egress proxy, `curl -sI https://github.com/<slug>`
returns **403 for a real slug and an invented one alike**, and with `-sI` prints only the proxy's
`200 Connection Established` — which earlier passes mistook for a live page. `api.github.com` is 403 for both.
🟢 **`git ls-remote --symref` and `raw.githubusercontent.com` both discriminate cleanly and are what this KB should use.**

*Prior pass content is preserved in git history at commit `457eaba` and earlier.*
