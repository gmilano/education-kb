---
industry: education
region: Global
updated: 2026-10-20
---

## Pass 349 · 2026-10-20 — two recipes built out of this pass's eleven new components, and both are the thing a studio must do before it is allowed to build: keep student data out of the model, and train on the cohort without holding the cohort

**Evidence:** [`compliance-vocabulary-grants`](../evidence/compliance-vocabulary-grants.2026-10-20-p349.tsv) · [`keyed-authors`](../evidence/keyed-authors.2026-10-20-p349.tsv) · [`alias-register`](../evidence/alias-register.2026-10-20-p349.tsv) · [`payload-digest`](../evidence/payload-digest.2026-10-20-p349.tsv)

### P49 — "Nothing identifiable reaches the model" — the student-data boundary for any LMS engagement (EMEA first by regulation, LATAM first by gap)

🔵 **The problem it solves, stated the way a client states it:** *"we want an AI tutor in Moodle and our DPO says no."* The answer is not a policy document; it is a process between the LMS and the model.

| stage | component | grant, read at the pin | what it does here |
|---|---|---|---|
| 1 · detect | [`data-privacy-stack/presidio`](https://github.com/data-privacy-stack/presidio) | 🟢 **MIT**, 1 084 B | named-entity + pattern recognition over the prompt and the attached material, with a per-country recogniser set |
| 2 · redact in-process | [`Rizzo-AI-Academy/rizzo-pii`](https://github.com/Rizzo-AI-Academy/rizzo-pii) (Python) or [`thoughtbot/top_secret`](https://github.com/thoughtbot/top_secret) (Ruby) | 🟢 **MIT**, 1 090 B / 1 095 B | a local-first filter in the request path, so the un-redacted text never leaves the estate |
| 3 · hold the consent | [`securitybunker/databunker`](https://github.com/securitybunker/databunker) | 🟢 **MIT**, 1 078 B | the subject record, the consent, and the data-subject request, as an API the LMS calls rather than a spreadsheet |
| 4 · decide | the LMS's own web services (Moodle **GPL-3.0**, Canvas **AGPL-3.0**) | 🟡 copyleft, and it does not reach stages 1–3 | the tutor call itself, made on redacted text |
| 5 · evidence | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) | 🟢 **MIT**, 1 168 B | the disparity report a regulator asks for once the model is making decisions |

🟢 **Wiring, concretely.** Run `presidio-analyzer` and `presidio-anonymizer` as two services beside the LMS; put stage 2's filter in the LMS plugin that makes the model call, not in the model gateway, so the raw string has no hop where it exists un-redacted; call `databunker` from the enrolment flow rather than the tutor flow, because consent is captured once and read often. 🔵 **Estimate: 6–8 weeks** for one LMS and one tutor surface, most of it in stage 1's recogniser tuning.

🔴 **The LATAM variant is a contribution rather than a configuration, and this pass measured why.** `presidio`'s `country_specific` recogniser sets cover **18 countries and no Latin American one** — no CPF, no CNPJ, no CURP, no RUT, no DNI. 🟢 **So stage 1 for a Brazilian or Mexican client starts with writing a recogniser class into an MIT codebase**, which is two files and a test fixture, and lands the studio as a named contributor to the layer every regional competitor will also need. `ACTION ZZ-ak` checks for an existing fork first.

### P50 — "Train on the cohort without holding the cohort" — the privacy-budget build for retention, placement and early-warning models

🔵 **The problem:** the useful model needs five years of student records, and the institution cannot hand them over.

| stage | component | grant, read at the pin | what it does here |
|---|---|---|---|
| 1 · get a dump you may keep | [`GreenmaskIO/greenmask`](https://github.com/GreenmaskIO/greenmask) | 🟢 **Apache-2.0**, 11 357 B | anonymised, consistent Postgres dumps from the live SIS into the staging environment |
| 2 · measure what the dump still leaks | [`arx-deidentifier/arx`](https://github.com/arx-deidentifier/arx) | 🟢 **Apache-2.0**, 10 351 B | k-anonymity / l-diversity / t-closeness and a re-identification risk figure the DPO can sign |
| 3 · substitute what you still cannot have | [`hitsz-ids/synthetic-data-generator`](https://github.com/hitsz-ids/synthetic-data-generator) | 🟢 **Apache-2.0**, 11 339 B | structured-tabular synthesis for the columns that stay too sparse to anonymise |
| 4 · train with a budget, not a promise | [`meta-pytorch/opacus`](https://github.com/meta-pytorch/opacus) (deep) or [`IBM/differential-privacy-library`](https://github.com/IBM/differential-privacy-library) (scikit-learn) | 🟢 **Apache-2.0**, 10 241 B / 🟢 **MIT**, 1 078 B | DP-SGD or DP drop-ins, so ε is an artefact of the build |
| 5 · report the cohort, not the student | [`google/differential-privacy`](https://github.com/google/differential-privacy) or [`OpenMined/PyDP`](https://github.com/OpenMined/PyDP) | 🟢 **Apache-2.0**, 13 333 B / 11 357 B | DP aggregations for the dashboard the institution publishes |
| 6 · show it is not discriminating | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) | 🟢 **MIT**, 1 168 B | group-fairness metrics and mitigation over the trained model |

🟢 **The deliverable that makes this sellable is not the model — it is ε plus the risk figure plus the disparity report, in one pack, with the payload digests of every component recorded.** 🔵 **Estimate: 8–12 weeks**, and stage 2 is where it either passes or stops.

🔴 **Two maintenance facts to price into the quote, both measured this pass:** `arx` has not moved since **2025-10-01** (4 306 commits, 40 author addresses (`%ae`)) and `hitsz-ids/synthetic-data-generator` has not moved since **2025-03-06** (281 commits, 25 author addresses (`%ae`)). 🟢 Neither has a maintained open alternative at the same scope, so the honest line to a client is *"we will carry patches for this component"* rather than *"it is actively maintained"*.

### 🟡 An amendment to p348's dedupe recipe, from this pass's own run

🔴 p348's recipe told a studio to dedupe its supply list by case fold and by HEAD. 🟢 **Add the register step, because this pass proved both of those pass a stale address**: resolve every address through the search index's `full_name` before quoting an option count, and keep the result as dated evidence — the channel can be shut, as the HTML `301` channel was (`403` on all 43 addresses here). 🔵 The artefact is [`alias-register`](../evidence/alias-register.2026-10-20-p349.tsv): group, address, state, pin, and the channel that decided it.

## Pass 348 · 2026-10-20 — two recipes, and both are things a studio does BEFORE it builds: produce the fairness evidence Annex III will ask for, and dedupe your own supply list so the option count you quote is true

**Evidence:** [`p348-placement-and-metadata`](../evidence/p348-placement-and-metadata.2026-10-20-p348.tsv) · [`p348-payload-identity-cross-repo`](../evidence/p348-payload-identity-cross-repo.2026-10-20-p348.tsv) · [`p348-shelf-fold-identity`](../evidence/p348-shelf-fold-identity.2026-10-20-p348.tsv) · [`p348-institutional-orphan-probe`](../evidence/p348-institutional-orphan-probe.2026-10-20-p348.tsv)

### P37 — "Prove it isn't discriminating" — the Annex III evidence pack for an assessment, admissions or proctoring model (EMEA first, and anywhere a regulator asks the question second)

🔵 **The client problem.** The client has or wants a model that touches admissions, assessment, placement or proctoring. From **2027-12-02** that is EU Annex III high-risk (search-channel convergence — no EU host resolves from this environment, so the date travels as a claim), and the duty that bites is not accuracy, it is **demonstrated non-discrimination across protected groups, in a technical file that exists before the audit does.** 🔴 **This base has written that sentence for six passes and never named a component that produces the evidence.** Here it is.

| Layer | Component | Grant, read at the pin this pass | What it does here |
|---|---|---|---|
| **Fairness metrics + mitigation** | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) | 🟢 **MIT** at ROOT, holder line absent · 2 300 ★ · 1 117 c · **139 author names** · pushed 2026-10-20 | The measurement itself: group-fairness metrics (selection rate, TPR/FPR parity, equalised odds) and mitigation, on any sklearn-shaped model. 🟢 **139 authors over seven years is the denominator a conformity argument leans on** |
| **Test cohorts without touching student records** | [`sdv-dev/SDV`](https://github.com/sdv-dev/SDV) | 🟢 Already shelved here | Synthetic cohorts with controlled group composition, so the fairness suite runs on data the client may legally share with an auditor |
| **The human decision the law wants** | [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) | 🟢 **MIT**, shelved p344 | Gates grade and announcement writes behind explicit human confirmation. 🔵 **The same component answers New York's prohibition, Korea's Act and Oklahoma SB 1734** — the control is identical in three regions |
| **Integrity input, so "the student didn't write it" is not a model guess** | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** at ROOT + three own-holder subtree grants · Ghent University · 3 859 c | Source-code similarity as a *reported signal to a human*, never an automatic verdict. 🔴 Wiring `dolos` straight to a sanction is the Annex III failure in one line |
| **Did the intervention help, and for whom** | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 **Apache-2.0** at ROOT · 2 815 c · 14 author names | Randomised assignment inside live courses. 🟢 **Subgroup efficacy is the other half of the fairness file**: a model can be metric-fair and still only help one group |
| **Service-standard reference** | [`DFE-Digital/education-benchmarking-and-insights`](https://github.com/DFE-Digital/education-benchmarking-and-insights) | 🟢 **MIT**, holder `Department for Education - Digital` · **5 266 c** · 30 authors · pushed 2026-10-20 | What a public education service's data boundary, notification architecture and pipeline look like when a ministry has to defend them |

🟢 **How to wire it.** (1) Define the protected attributes with the client's counsel, **in writing, before any code** — in education they are usually SEN/disability status, free-school-meal or low-income flags, migration or language background, and sex; (2) generate synthetic cohorts with `SDV` that span those groups at controlled rates, and keep the real data out of the audit artefact; (3) run `fairlearn`'s metric frame per group on the client's model, store the output as a dated artefact in the repo, **not as a notebook cell**; (4) put `che-ntucool-mcp`'s confirmation gate on every write that reaches a student record, so the human decision is in the log rather than in the policy document; (5) if an integrity signal is in scope, `dolos` produces it as a *finding a human adjudicates*, with an appeal path; (6) run the intervention as a `terracotta` experiment and report the fairness metrics **per arm**.

🔴 **What this recipe refuses to do.** It does not claim the model is compliant. 🟢 **It produces the artefacts a regulator asks for and leaves the verdict to the client's counsel** — which is the only honest shape for a compliance deliverable, and `P250` is why: an undetermined verdict and a prohibited one are indistinguishable, so a studio that asserts compliance has taken the client's risk onto its own balance sheet.

🟡 **Why nobody had assembled this before, and it is a lesson rather than an excuse.** Not one of `fairlearn`, `SDV` or the privacy tier carries an education token, so **every education-token discovery filter this base has run is structurally blind to the compliance half of its own market.** `ACTION ZZ-ae`.

### P38 — "How many open options are there, actually?" — the supply-dedup check to run before you quote an option count (any region; 30 minutes)

🔵 **The client problem.** A studio says *"there are five open-source options for this layer"* in a deck. 🔴 **This base just measured how wrong that sentence can be on its own shelves**: 65 folded-collision groups, a fourth alias pair whose two owners share no characters, and two repositories shipping byte-identical payloads. 🟡 **Every one of those inflates an option count, and the inflation is invisible to reading the list.**

| Check | Command | What it catches | Measured here |
|---|---|---|---|
| **1 · fold the slug** | `make fold-census` (offline) | the same address published under different casings | **65** collision groups; **63** invisible to the case-sensitive `gate-identity` |
| **2 · pin the HEAD** | `git ls-remote --symref https://github.com/<slug> HEAD` | two addresses, one repository — a rename, an org transfer, a vanity fork | **4** on-shelf alias pairs. 🔴 The newest, [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) ≡ [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) at `1c46a82ba384`, is **invisible to step 1** |
| **3 · digest the payload** | `curl -s raw.githubusercontent.com/<slug>/HEAD/<file> \| sha256sum` | two repositories, one body of work | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) and [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) ship `SKILL.md` at **sha256 `152e3272fbd108fe…`** — identical, and **invisible to steps 1 and 2** |
| **4 · read the holder line** | `make gate-grant-scope`'s channel | the org is regional, the CODE is upstream | [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) holder reads **`EleutherAI`**; [`AI-for-Education/edu-qurating`](https://github.com/AI-for-Education/edu-qurating) is a QuRating fork |
| **5 · enumerate the tree at the pin** | `git ls-tree -r --name-only HEAD` + read each hit | "no licence" that is really "a licence you did not look for"; and a vendored grant published as the project's | [`DaviPac/Classroom-mcp`](https://github.com/DaviPac/Classroom-mcp) is a genuine **ABSENCE-ENUMERATED**; `safytech/ulearn`'s TinyMCE **LGPL** and `AcademicsToday/academicstoday-django`'s **Twitter** Bootstrap grant both grade **FOREIGN** beside correct own-holder roots |
| **6 · date the stream** | `git log -1 --date=short` + `rev-list --count` + the `%z` histogram | a finished pilot sold as a platform; an unplaceable row | [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) dormant **30 months**; [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) is **5 commits**; [`EduNLP/EduCoder`](https://github.com/EduNLP/EduCoder) has a Chinese-lab name and a **US Pacific** commit stream on all 49 |

🟢 **The deliverable is one table per layer**: address, pin, grant at the pin with its scope and holder, commits, author NAMES (say the key), first and last commit, timezone majority, and **which of the other rows it is the same thing as.** 🔵 **An option count after this check is usually smaller and always defensible** — and the honest version of the deck line is *"there are three distinct options and two of them are the same project under different stewardship."*

🔴 **Do not skip step 3 because steps 1 and 2 passed.** The three checks catch three disjoint classes; this base owned instruments for two of them and had run the cheaper one over **17.4 %** of its own addresses.

---

## Pass 347 · 2026-10-20 — two recipes built on rows this pass read at a pin, and both answer a question this base could not answer yesterday: who contains the student's code, and what a national education service actually looks like underneath

🟢 **Both recipes below are built only from components whose grants were read first-hand at a pinned HEAD sha — this pass or a named earlier one — and every address is on these shelves.** 🔵 Where a grant is **package-scoped** rather than repository-scoped, the step says so, because that is the difference between a dependency a studio may ship and one it may not.

### P35 — "The agent may write the tests; it may not be the sandbox" — AI-assisted autograding a university can defend to an examination board (EMEA — Germany, and anywhere with an appeals process)

🔵 **The client problem.** A faculty wants AI to cut marking load on programming coursework. 🔴 **Two things kill these pilots, and neither is model quality.** First, *appeals*: a student challenges a mark, and "the model said so" is not a defensible answer in front of an examination board. Second, *execution*: grading coursework means **running code a student wrote**, on faculty infrastructure, at submission volume — and an LLM-generated test harness executing untrusted code with ambient filesystem and network access is an incident waiting for a deadline. 🟢 **This base has shelved five autograders and, until this pass, no sandbox.**

| Layer | Component | Grant, read at the pin | What it does here |
|---|---|---|---|
| **Containment** | [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) | 🟡 **MIT, 1 345 B** — stock body, five copyright lines (TUM + four individuals); read at pin `b5c2595`. 🔴 GitHub's classifier says `NOASSERTION`; the template test says MIT | **The policy boundary.** ArchUnit/WALA static policy plus AspectJ/Byte Buddy runtime instrumentation over file, network, command, thread and JVM access, with deadline-aware hidden tests. **Nothing the student's code does escapes a declared policy** |
| **Rule-named findings** | [`kit-sdq/autograder`](https://github.com/kit-sdq/autograder) | 🟢 **MIT, 1 068 B** at **`LICENSE.md`**, read at pin `42263e5` | PMD + SpotBugs + Spoon behind one grading contract. 🟢 **This is the appeals layer:** every deduction has a rule name, a line and a rationale a human can re-check |
| **Course + submission plumbing** | [`autolab/Autolab`](https://github.com/autolab/Autolab) | 🟢 Apache-2.0, 11 323 B at `master/LICENSE` (read p296) | Assignment lifecycle, submission intake, gradebook. 🔴 **Its grant resolves on `master`, not `main`** |
| **Notebook courses (alternative intake)** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause (shelved, p341 census) | Use instead of Autolab when the course is notebook-shaped. 🟡 Trips conservative scanner rules on its own boilerplate — permissive, see `p341-bsd-boilerplate-cost` |
| **Human oversight gate** | [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) | 🟢 MIT (shelved p344) | Gates **grade writes** behind explicit human confirmation — the Article-14-shaped control, reused here verbatim |
| **Model access** | [`AI-for-Education/fabdata-llm`](https://github.com/AI-for-Education/fabdata-llm) | 🟢 **MIT, 1 065 B**, read at pin `a0f85c3` | The provider abstraction the pedagogy benchmark itself runs on 🟡 **dormant four months, nine authors — vendor it rather than depend on it** |
| **Model selection, defended** | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT, 1 064 B (read p345) | Answers *"why this model"* with teacher-qualification-exam scores instead of vibes |

🟢 **The wiring, concretely.** The agent's job is bounded to **two** artefacts: (1) candidate test cases for a rubric item, and (2) prose feedback on findings it did not produce. 🔴 **It never executes anything and it never writes a mark.** Submission intake lands in Autolab; Autolab invokes `kit-sdq/autograder`, which runs **inside** an `Ares2` policy declaring exactly the files, sockets, threads and subprocesses this assignment may touch; findings come back rule-named; the agent turns findings into student-readable prose and proposes a mark; `che-ntucool-mcp`'s confirmation gate holds the grade write until a human presses the button. 🟢 **Appeals then have a record with three separable layers** — what the code did (sandbox log), which rule fired (autograder finding), what was said about it (agent output) — and only the third was generated.

🔴 **The licence posture, stated because it decides the commercial shape.** Ares2 and `kit-sdq/autograder` are **MIT**; Autolab is **Apache-2.0**; nbgrader is **BSD-3-Clause**. 🟢 **Every component is permissive, so the integration and the rubric packs stay the studio's IP.** 🟡 Two cautions: **GitHub's licence API reports `NOASSERTION` for Ares2** and a client's scanner may echo it — the answer is the licence file itself, 1 345 B of verbatim MIT whose extra bytes are five copyright lines; and `fabdata-llm` is a four-month-dormant nine-author project, so vendor it at a pin.

🔵 **Regional trigger.** Germany, Austria and Switzerland first — both grading components are TUM's and KIT's, and naming the chairs is half the credibility in that market — then any jurisdiction where assessment decisions are appealable, which under the EU AI Act is all of EMEA: **Annex III education duties at 2027-12-02, Article 50 transparency live since 2026-08-02, Article 4 literacy already binding.** 🟢 This recipe is conformity-by-construction rather than conformity-by-documentation: the human-confirmation gate and the rule-named findings *are* the Article 14 and Article 13 story.

### P36 — "Show me a national education service that works" — the public-sector reference build (EMEA — United Kingdom, and any ministry engagement)

🔵 **The client problem.** A ministry, national agency or state education department wants to put a service online — a vacancies board, a course catalogue, a scholarship register, a qualifications finder — and the procurement conversation stalls on unquantifiable risk: *how long, how many people, what does accessibility and service-standard compliance actually cost, and can we see one that runs?* 🔴 **Every answer on the market is a vendor case study.** 🟢 **There are now two complete, MIT-licensed, production national services on these shelves, both pushed on the day of this pass.**

| Layer | Component | Grant, read at the pin | What it does here |
|---|---|---|---|
| **Reference service A — demand side** | [`DFE-Digital/teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) | 🟢 **MIT, 1 092 B**, `main/LICENSE`, read at pin `0a49905` | The UK DfE's live national teaching-vacancies service. **19 717 commits · 122 authors · 2017 → today.** Read it for notification architecture, school/trust account models, search, and nine years of production maintenance |
| **Reference service B — publish-then-find** | [`DFE-Digital/publish-teacher-training`](https://github.com/DFE-Digital/publish-teacher-training) | 🟢 **MIT, 1 091 B**, `main/LICENSE`, read at pin `d55fba5` | Provider-facing editing plus candidate-facing search in one codebase. **17 549 commits · 142 authors.** The shape of almost every national catalogue |
| **Identity + LTI seam (Python)** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT, 1 098 B**, read at pin `1ac0b56` | LTI 1.3 / Advantage launches when the service must appear inside an institution's LMS. 🔴 **Use Michigan's, not the Harvard-named fork of it** |
| **Offline / low-connectivity leg** | [`learningequality/morango`](https://github.com/learningequality/morango) + [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT, 1 074 B** (morango, read at pin `c8679ab`; default ref **`release-v0.9.x`**) | **morango is the sync protocol, Kolibri is the product.** Add this leg when the service must work in buildings that lose their link |
| **Shared content vocabulary** | [`learningequality/le-utils`](https://github.com/learningequality/le-utils) | 🟢 **MIT, 1 084 B** at **`LICENSE.txt`**, read at pin `14c5493` | Content kinds, formats, language codes — the model to align to if anything will ever hand files to Kolibri |
| **Open curriculum content** | [`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) | 🟡 **Split, read at pin `0d5ee4e`:** code **NCSA**, content **CC-BY-3.0**, builds **CC-BY-4.0** | Real content for the demo, and 🟢 **the worked example of how to license a curriculum asset by artefact type** |
| **Transparency / credential layer (optional)** | [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 MIT, 1 091 B, pin `1c46a82` (read p346) | Verifiable credentials where the service certifies something |

🟢 **The wiring, concretely.** This recipe is read-first, build-second, and the first deliverable is a document rather than code: a **gap analysis against a running service.** Clone both DfE repositories at the pins above; extract four things the client's own team will recognise — (1) the service-standard and accessibility patterns as implemented, not as policy; (2) the data model for providers/courses/locations/vacancies; (3) the notification and alert architecture; (4) the test and deployment pipeline — and put each beside what the client has. 🟢 **Then the estimate stops being a guess:** 142 authors over seven years is a real denominator for *"what does a national service cost"*, and the delta between their model and yours is the actual scope. 🔵 Build phase: fork the publish-then-find skeleton, keep the GOV.UK-style design-system discipline, bolt on `django-lti` only if the service has to live inside an LMS, and add the morango/Kolibri leg only where connectivity genuinely fails.

🔴 **The licence posture.** **Everything above is MIT except the content**, which is why the content licence has to be read rather than assumed: `coursebook`'s **CC-BY-3.0 / CC-BY-4.0** split means the *book* carries attribution obligations the *code* does not. 🟢 **A studio can own the whole integration and still owe attribution on a PDF it ships** — and that distinction, not copyleft, is where education engagements actually get licence surprises.

🔵 **Regional trigger.** The UK first, where the artefacts are the client's own government's. 🟢 Then **LATAM**, where UNESCO IESALC's survey puts institutional AI use at 87 % against 26 % with a formal strategy: a reference build from a working national service is the fastest way to turn that 61-point governance gap into a scoped programme. 🟡 And **APAC**, where Vietnam and South Korea have named education in statute and a ministry asking *"what does compliant look like"* can now be shown 19 717 commits of it.


## Pass 346 · 2026-10-20 — two recipes built only from rows whose grants were read at a pin this pass or a previous one, each with the compliance clock it answers and the data boundary it must not cross

**Evidence:** [`p346-institutional-orphan-probe`](../evidence/p346-institutional-orphan-probe.2026-10-20-p346.tsv) · [`p346-coursemology-pin-grant-boundary`](../evidence/p346-coursemology-pin-grant-boundary.2026-10-20-p346.tsv) · [`p346-curriculum-data-carveout`](../evidence/p346-curriculum-data-carveout.2026-10-20-p346.tsv).

🔴 **`make hooks` did not run this pass**, so p345's `gate-absence` and `gate-pin-grant` findings are unjudged rather than cleared ([`agents/top.md`](../agents/top.md)). 🟢 Every component below is an address already on these shelves, and each new one is cited with the pin its grant was read at — `gate-evidence-store`'s rule that no recipe may depend on a component it cannot locate.

### P33 — "A lesson-planning agent that is aligned to the national curriculum and cannot invent it" (EMEA — United Kingdom)

🔵 **The client problem.** A trust, academy chain or ministry wants AI lesson planning. The thing that kills these pilots is not model quality: it is that the output cannot be shown to match the statutory curriculum, and that teachers catch the model inventing objectives. 🟢 **The fix is to make the curriculum a retrieved spine rather than model memory**, and the UK now has that spine permissively.

| Layer | Component | Grant, read at the pin | What it does here |
|---|---|---|---|
| Curriculum spine | [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT, 1 084 B** at **`LICENCE`**, pin `386f3f8` | API + SDK + **MCP app** over the Oak Open Curriculum data. Because it ships an MCP surface, the agent **retrieves** units and objectives instead of recalling them |
| Pedagogical grading | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT, 1 064 B (read p345) | Scores candidate lesson output on pedagogical quality rather than fluency. 🔴 **5-commit bench** — adopt and maintain it, do not depend on upstream |
| Skills mapping | [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟡 **MIT, untitled payload**, 1 068 B, pin `cf2877d` | Maps lesson outcomes onto **ESCO** skills and **ISCO** occupations — the vocabulary EU-facing clients already report against |
| Human oversight gate | [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) | 🟢 MIT (shelved p344) | Gates grade and announcement **writes** behind explicit human confirmation — the Article-14-shaped control, reusable verbatim |
| Delivery | [`moodle/moodle`](https://github.com/moodle/moodle) + [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | 🟡 Moodle is **GPL-3.0** | Writes the approved plan into the LMS the school already runs. 🔵 Keep your code a separate MCP client; do not patch Moodle core |
| Credentialling (optional) | [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT, 1 091 B**, pin `1c46a82` | Issues a verifiable credential when a unit completes |

🟢 **The wiring, concretely.** Stand the Oak MCP app up as the agent's **only** curriculum tool, and put it behind this base's own [`mcp-allowlist-gateway`](code/mcp-allowlist-gateway) so the agent cannot reach an unapproved tool. The planning loop is then: *retrieve* the statutory unit and its objectives over MCP → *draft* the lesson → *grade* the draft with `pedagogy-benchmark` and reject below threshold → *tag* outcomes with `esco-skill-extractor` → *present* to the teacher through `che-ntucool-mcp`'s confirmation gate → *write* to Moodle only after the teacher confirms. 🔵 **Every curriculum claim in the output carries the Oak unit identifier it was retrieved with**, which is what makes the result auditable to a head of department rather than merely plausible.

🔴 **The compliance clock this answers, and the feature it forbids.** **Article 50 transparency duties apply from 2026-08-02** and were not deferred, so the teacher-facing surface must disclose AI generation. **Annex III education high-risk moved to 2027-12-02** (Regulation (EU) 2026/1744 — secondary-source convergence; every EU primary host returns HTTP 000 from this environment, so take the date from counsel), which means the conformity documentation can be *scheduled* rather than crashed. 🔴 **Emotion recognition in education has been prohibited since 2025-02-02: no attention scoring, no engagement detection, no affect-aware tutoring in this build, deferral or not.** 🟡 **And the human gate is not decoration** — a UK deployer is the one carrying the oversight duty, which is precisely why the confirmation step sits between the model and the LMS write.

### P34 — "A sovereignty-safe coursework and assessment stack with a readable data boundary" (APAC — Singapore, South Korea, Vietnam)

🔵 **The client problem.** An APAC university or ministry will not put student work in a foreign SaaS tutor, and now has a statute to point at. 🟢 **This region's supply is strong enough to answer that entirely on-premises** — and p346 found the deepest permissive coursework bench on these shelves.

| Layer | Component | Grant, read at the pin | What it does here |
|---|---|---|---|
| Coursework platform | [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 🟢 **MIT, 1 118 B**, pin `6310c97` 🔴 **plus the submodule boundary below** | Assessments, autograded programming questions, submission and grading workflow. 15 821 commits, 86 authors, twelve years, live |
| CS autograding at scale | [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT, 1 082 B**, pin `894ed02` | Per-student containerised cloud IDEs + autograder, if the engagement is a computing faculty |
| High-stakes exam delivery | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🟡 **MPL-2.0**, 16 725 B, pin `eff84b2` | Lockdown exam client. 🔴 **File-level reciprocity: publish changes to ITS files; your surrounding product stays yours** |
| Curriculum alignment (KR) | [`DECK6/korean-elementary-learning-map`](https://github.com/DECK6/korean-elementary-learning-map) | 🟡 **MIT + data carve-out**, 1 543 B, pin `67539e3` | Ontology over the **2022 revised Korean elementary curriculum** for alignment and prerequisite ordering |
| Analytics | [`openedx/tutor-contrib-aspects`](https://github.com/openedx/tutor-contrib-aspects) | 🟢 **Apache-2.0**, 11 356 B, pin `c1dcc29` | Use instead of the above pair where the client's estate is already Open edX + [`overhangio/tutor`](https://github.com/overhangio/tutor) |
| Human oversight gate | [`psychquant/che-ntucool-mcp`](https://github.com/psychquant/che-ntucool-mcp) | 🟢 MIT (shelved p344) | The same confirmation gate; answers Korea's disclosure duty and Vietnam's high-risk classification with one component |

🔴 **The pre-flight that this recipe will not run without, and it is specific to Coursemology.** `.gitmodules` is present at the superproject pin, so `git clone --recurse-submodules` pulls two components the MIT cell does not cover: `authentication/singular-keycloak-database-federation` at pin `734e8ed` (**Apache-2.0**, 11 356 B) and `client/vendor/recorderjs` at pin `08e7abd` (**MIT — but with no licence file at all**; ten root filenames probed at the pin all return HTTP 404 and the grant exists only under `## License (MIT)` in `README.md`, © 2013 Matt Diamond). 🟢 **So the vendoring review here must read a README, because a licence scanner over this tree reports a component with no grant.** 🟡 If the audio-recording feature is not needed, the cheapest answer is to not initialise that submodule and record why.

🔴 **The compliance clocks this answers.** **Korea:** the **AI Basic Act has been in force since 2026-01-22**, covering high-impact AI with generative-AI disclosure duties. **Vietnam:** the AI law is **in force from 2026-03-01 and names education among high-risk sectors**, compliance due **2027-03-01**, with a **six-month grace period for education systems already operating before 2026-08-15** — so a system stood up now is in a materially better position than one started later. **India:** **DPDP** obligations phase in to **May 2027** and bear directly on student data. 🟡 **China** regulates by service type rather than sector, so the labelling and generative-AI rules apply to the feature, not the school. 🔵 **The commercial point for a sovereignty-led procurement: every component above is self-hostable and permissive except the exam client, whose reciprocity is per-file** — there is no AGPL §13 hosting trap anywhere in this stack, which is the thing that disqualifies an Open edX fork.

🟢 **What NOT to build into either recipe, learned the expensive way on these shelves.** Do not staff or source a LATAM leg off a Portuguese- or Spanish-language repository name (`ACTION ZZ-g`, `ACTION ZZ-h`: two instances, two passes). Do not rely on an address a repository search omits until a HEAD comparison says which way it is non-canonical (`ACTION ZZ-n`). And do not let a licence scanner be the last word on an education data row — in both carve-out instances this base has read, the binding restriction sat outside the SPDX-readable channel.

## Pass 345 · 2026-10-20 — two recipes, each wiring a row this pass verified first-hand to rows already on these shelves

**Evidence:** [`p345-orphan-promotion-probe`](../evidence/p345-orphan-promotion-probe.2026-10-20-p345.tsv) · [`p345-mcp-brasil-grant-scope`](../evidence/p345-mcp-brasil-grant-scope.2026-10-20-p345.tsv).

### P31 — "Does our AI tutor actually work?" — a randomised trial inside the client's own LMS, with the ethics layer in code

🔴 **The question that kills AI-tutoring pilots** is not whether the tutor is good; it is that nobody can show it worked, because the pilot had no control arm and no consent story, so the result cannot be published or defended to a board.

**Components, every grant read first-hand:**

| Role | Component | Grant | Note |
|---|---|---|---|
| Randomisation, treatment arms, consent, export filtering | [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0, 11 323 B, read at **`development/LICENSE`** | ⚠️ ships a binding **`NOTICE`** (239 B) under §4(d) — carry it forward |
| The tutoring arm | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | already on the build tier; **Bayesian Knowledge Tracing**, so mastery is an inspectable model rather than a prompt, and it ships LTI middleware |
| The control arm | the client's existing coursework | — | no build |
| Content for both arms | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 MIT | generates the item bank so both arms draw from one pool |
| Integration seam | **LTI 1.3** | — | Terracotta and OATutor both speak it; one integration serves both arms |

**Wiring.** Stand Terracotta up as the LMS plug-in and define two treatment conditions on a single assignment sequence. Arm A renders the OATutor activity (its LTI middleware is the hand-off); arm B renders the existing coursework. Generate the item bank once with Educhain and feed both arms so content is held constant and only the *tutoring* varies. Let Terracotta collect consent **in the form the instructor cannot see**, randomise assignment, and filter non-consenting students out of the export. OATutor's BKT traces per-skill mastery inside arm A, which gives a process measure to put beside the outcome measure.

🟢 **What this buys:** a result with a control arm, a consent record, and de-identified exports — i.e. one a university ethics board will accept and a client can publish. 🟡 **Cost and limits:** Terracotta is Java and presumes an LMS (Canvas is its reference target); budget the LTI 1.3 registration dance, which is the real schedule risk. **6–9 weeks** for a single-course trial. 🔴 **Do not** substitute a star-count judgement here: Terracotta carries 21 ★ and a 2 815-commit, 18-author, seven-year log — per `ACTION ZZ-c` the log is the bench.

### P32 — A Brazilian education-data agent that is defensible under LGPD on day one

🔴 **The LATAM engagement shape this base could not serve until this pass.** A ministry, state secretariat or edtech client asks for an agent over national assessment data. The data is real, public and radioactive: INEP pulled ENEM microdata from public access in 2022 under LGPD pressure and resumed in anonymised form in 2024.

**Components, every grant read first-hand:**

| Role | Component | Grant | Note |
|---|---|---|---|
| Systems-of-record access | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 **MIT (1 072 B) for the CODE only** | `SOURCES.md` §4 `Educação — RISCO ALTO`: `inep`, `inep_enem`, `inep_censo_escolar`, plus `FNDE` at §4.2 |
| The compliance boundary | the same repo's `NOTICE` (3 135 B), `ACCEPTABLE_USE.md` (8 109 B), `SOURCES.md` (19 286 B) | 🟡 asserted conditions | **read all three before writing a line** |
| Agent orchestration | any MCP-speaking client on these shelves | — | it is an MCP server; no adapter to write |
| Curriculum/outcome framing | [`satvik314/educhain`](https://github.com/satvik314/educhain) · [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | 🟢 MIT | turn a measured gap into material rather than a dashboard |

**Wiring.** Point an MCP client at `mcp-brasil` and keep the server's **default PII masking on**. Work only through the whitelisted aggregate columns — `COLUNAS_DISTINCT_PERMITIDAS` in `datasets/inep_enem/constants.py` permits state, sex, age band, race and school and withholds `NU_INSCRICAO`, name and CPF. Use the Censo Escolar for the denominator and ENEM for the outcome, then hand the identified gap to Educhain or `instructional_agents` to produce targeted material.

🔴 **The four hard rules, taken from the project's own documents rather than invented here.** (1) **Never** set `MCP_BRASIL_LGPD_ALLOW_PII` without a documented legal basis under LGPD art. 7 or 11 — the project's own text states that enabling it **transfers controller responsibility to you**. (2) Re-identification by cross-referencing other bases is **VEDADO** under LGPD art. 12. (3) Formal research on non-anonymised microdata belongs in INEP's **SEDAP** protected-access service, **not** in this server. (4) Attribute **INEP** per `SOURCES.md`, and carry the `NOTICE` forward.

🟡 **The residual risk, which the project publishes as an open item and so should you:** validating one sample of the 2023 archive and enumerating every column to confirm no direct re-identification key survives. 🟢 **Close it in week one** — it is a day of work and it converts the project's open item into your evidence. **6–8 weeks** to a defensible pilot. 🔵 Note for the client conversation: the server is explicitly **not** an official government service, and its own `NOTICE` says so.

## Pass 344 · 2026-10-20 — two recipes this pass can state concretely because it read the grants first-hand, and one pre-flight check that belongs in front of every recipe on this shelf

**Evidence:** [`p344-payload-absence-enumerated`](../evidence/p344-payload-absence-enumerated.2026-10-20-p344.tsv) · [`p344-address-resolution`](../evidence/p344-address-resolution.2026-10-20-p344.tsv) · [`p344-region-placement`](../evidence/p344-region-placement.2026-10-20-p344.tsv) · [`p344-agent-runtime-region`](../evidence/p344-agent-runtime-region.2026-10-20-p344.tsv).

🔴 **`make hooks` could not be run (tool policy, `Code from External`) — second consecutive pass.** `ACTION ZZ-a` satisfied; **no recipe below cites an instrument verdict.** Every licence named was read from its payload with `curl` at the repository's **actual default ref**.

### 🔴 Pattern 0 — the pre-flight that goes in front of every other recipe on this shelf

🟢 **Three of the four addresses this pass touched would have broken a recipe written from a search result.** This is four commands, it needs no instrument, and `ACTION ZZ-e` is the reason it exists:

```bash
# 1. Does the address exist, and what is its REAL default branch?
#    A credential prompt is a MEASUREMENT (ACTION p293): the address is not a repository.
git ls-remote --symref https://github.com/OWNER/REPO HEAD

# 2. Enumerate the tree at THAT ref — never assume main/master, never assume root.
git clone --bare --filter=blob:none https://github.com/OWNER/REPO r.git
git -C r.git ls-tree -r --name-only HEAD \
  | grep -iE '(^|/)(licen[cs]e|copying|notice)([.-][a-z]+)?$' \
  | grep -vE '(^|/)(vendor|node_modules|third_party|addons)/'   # drop dependency decoys

# 3. Read the payload. A manifest declaration is NOT a grant (ACTION p280).
git -C r.git show HEAD:PATH/TO/LICENSE | head -5

# 4. Who wrote it? (ACTION ZZ-c / ZZ-f) — at a high agent share the region channel is void.
git -C r.git log --format='%ae%x09%s' | grep -i anthropic
```

🔴 **What each step caught this pass.** Step 1: `openeducat/openeducat` and `forma-lms/formalms` **do not exist**, and the real OpenEduCat default branch is **`19.0`**, not `main`. Step 2: Forma LMS's grant is at **`html/license.txt`**, with **four dependency decoys above it** — a first-match ladder answers Symfony's MIT on a GPL-2.0 project. Step 3: two MCP connectors declare `"license": "MIT"` and **ship no licence text at all**. Step 4: `davipac/classroom-mcp` is **2 of 2 commits agent-authored**, so its `+0000` offset describes a datacenter.

### 🟢 Pattern A — education ERP with an agent layer that the LGPL cannot reach (APAC-first, portable)

🔵 **Why it is stateable now:** OpenEduCat was carried as an unresolved address for five passes. 🟢 **Resolved and read first-hand this pass: `openeducat/openeducat_erp`, default ref `19.0`, `LICENSE` 8 241 B, `LGPL-3.0`** — 1 711 commits · 97 authors, **live 2026-10-13**, placed **APAC — India** (`techreceptives.com` 637 + `openeducat.com` 263, `+0530` 1 493/1 711).

**Wiring, and the licence boundary is the architecture:**

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| system of record | **`openeducat/openeducat_erp`** `@19.0` | 🟡 LGPL-3.0 | the vertical's **only live full education ERP** — SIS, LMS, admissions, finance, library |
| integration seam | its **Odoo XML-RPC / JSON-RPC API** — *not* a custom addon | — | 🔴 **the whole point: see below** |
| agent orchestration | **`langgraph`** (MIT) or **`crewai`** (MIT), running **outside** the ERP process | 🟢 MIT | permissive, so Globant's agent logic stays Globant's |
| human-confirmation gate | the pattern from **`psychquant/che-ntucool-mcp`** (MIT) | 🟢 MIT | gates grade/announcement writes behind explicit confirmation |
| model serving | **`ollama`** (MIT) or **`vllm`** (Apache-2.0), self-hosted | 🟢 MIT / Apache-2.0 | keeps student data inside the institution |

🔴 **The boundary, stated precisely, because the vendor's marketing does not.** The LGPL's weak-copyleft unit is the **module**. Globant may *link* proprietary services against OpenEduCat and keep them separate — **but a modification to an OpenEduCat module carries back, and an Odoo-style addon that subclasses a core model is a modification, not a link.** 🟢 **So the agents live in a separate process and speak over the API. Nothing proprietary is ever an addon.** 🔵 **This is the same seam this shelf prescribes for Moodle and Open edX, which is why the recipe survives the licence difference and ports to any of the three.**

🟢 **Where it lands first:** **Vietnam** — education is named high-risk (automated assessment, behavioural monitoring), compliance **2027-03-01** with grace for systems live before **2026-08-15**, so the human-confirmation gate is a *requirement* rather than a nicety; and **Korea**, in force since **2026-01-22**, 🔴 **where the local-representative requirement must reach the proposal before the architecture does.**

### 🟡 Pattern B — the LATAM governance engagement, which is NOT a build

🔵 **This pass gave the region its first hard denominator and it changes what the recipe is.** **UNESCO IESALC/UNU-IAS: 200 institutions, 19 countries — 87% use AI, 26% have a formal AI strategy.** 🔴 **A 61-point gap, with adoption driven by individual faculty and students rather than institutional policy.**

🔴 **So the deliverable is not a tutor.** The buyer is a rector or provost who **has already lost control of the surface**, and the first engagement is to map it:

1. 🟢 **Inventory** — enumerate AI already in use across teaching, assessment, admissions and administration. There is no model in this step; it is interviews plus log analysis, and it is the step that produces the client's first honest number.
2. 🟢 **Policy and acceptable-use** — modelled on the governance shape the binding regimes already specify, so the institution is not re-deciding from scratch: **a human decision between model and record** (NYC's prohibition, EU Article 14), and **transparency disclosure** (EU Article 50, live since 2026-08-02).
3. 🟢 **Oversight instrumentation** — the audit trail, built on permissive parts: **`langgraph`** (MIT) for the decision path, **`grafana`**-style dashboards for the record. 🔴 **Not on the platform tier, which is copyleft.**
4. 🟡 **Only then** a build, and `Cvmcosta/ltijs` (**LTI 1.3**, the one instrument-placed LATAM row on these shelves, Brazil) is the integration route into whatever LMS the institution already runs.

🟢 **Align, do not compete:** **UNESCO's Observatory on AI in Education for LAC** (launched **2026-04-14**) with **CAF, CENIA, ECLAC, Santillana, Tec de Monterrey, ProFuturo, Fundación Ceibal**, and the Mexico pilot with **CONALEP and DGETI**. 🔴 **And the pitch is the inverse of EMEA's and APAC's: there is no education-specific compliance deadline in the region, so this is sold on the adoption gap and institutional risk. Do not copy a deadline-driven deck into LATAM.**

### 🔴 What NOT to wire, measured this pass

- 🔴 **`loyaniu/moodle-mcp` — do not use.** **No licence payload anywhere in its tree and no `license` key in `pyproject.toml`** ⇒ all rights reserved by default. 🟡 **It is the best-benched of the three connectors probed** (institutional `calvin.edu`, plus a genuine `rwth-aachen.de` EMEA co-contribution), **which is exactly the trap.** 🟢 **Use `pablopc05/mcp-usc` (MIT, Universidade de Santiago de Compostela) instead** — the Moodle connector this shelf recommends and the fork candidate for a Spanish-language tenancy.
- 🟡 **`adriasantacreu/google-classroom-mcp` and `davipac/classroom-mcp` — do not wire yet.** Both declare `"license": "MIT"` in `package.json` with **no licence text**. 🟢 **Intent is unambiguous and it is a one-email fix** — ask for a `LICENSE` file before building. 🔴 Also: `google-classroom-mcp` is **11 commits over 3 days, dormant 7 months**, and `classroom-mcp`'s default branch is **an unmerged agent working branch**.
- 🔴 **`formalms/formalms` — not a permissive foundation, whatever a secondary source says.** Claimed Apache-2.0 by a 2026 LMS comparison; **the payload is GPL-2.0.** 🟡 Real Italian vendor bench, 7 494 commits, **three months stale** — usable only where copyleft is already accepted.
- 🔴 **`withmarbleapp/os-taxonomy` — read the grant before planning on it.** A 1 590-topic / 3 221-edge curriculum graph, but **`ODbL-1.0` (database) + `CC-BY-SA-4.0` (text) and no code licence**: reusable **as share-alike data**, not as a component.
- 🔴 **`Noor-ul-Eman28/AI-Tutor-MCP-Toolkit` — the one new slug the supply legs returned, and it has no grant** at any standard root name. Not promoted, not wired.

## Pass 343 · 2026-10-20 — two new recipes and one correction that had been sitting in three of them: every `tutor-mcp` step on this shelf pointed at the FORK

**Evidence:** [`p343-action-zc-placement`](../evidence/p343-action-zc-placement.2026-10-20-p343.tsv).

🔴 **`make hooks` was not run this pass** — the session's tool policy refuses to execute this repository's own `compose/code/` instruments. Every component grant below was read first-hand with `curl`; every activity figure with `git`.

### 🔴 Correction applied to P1, P6 and P7 — three recipes shipped a fork's URL while this base's own instrument had already proved it was one

🟢 **`compose/code/p139-duplicate-lineage/` established at p139 that `kvnloo/tutor-mcp` is a fork of `ArnaudGuiovanna/tutor-mcp`, seven commits behind, with a byte-identical description and a `LICENSE` reading `Copyright (c) 2026 Arnaud Guiovanna`.** `agents/top.md` flags it as *"🟡 A fork."* 🔴 **And three recipes on this shelf — plus the canonical agent-table row — still named the fork as the component to build on.**

🟢 **Re-measured this pass, and the gap has widened:** upstream `ArnaudGuiovanna/tutor-mcp` is at **467 commits · 5 authors · head 2026-10-16**; the fork was last measured at **452 c · 2026-10-02**. **Fifteen commits and two weeks behind, and drifting.** 🟢 **All four citations now point upstream**, with the fork retained only where this base discusses lineage.

🔵 **The class, because it is the fourth sighting in two days and the cheapest one yet:** *capability present, instrument already built and already run, verdict never propagated to the shelf that spends it.* **p139 produced the right answer and nobody edited the recipe.** 🟢 **`ACTION ZZ-f`: when a lineage, licence or placement verdict lands in `evidence/` or `compose/code/`, grep the four decision shelves AND `compose/patterns.md` for the slug in the same pass. A verdict that does not reach a recipe has a 0% delivery rate, which is `p327`'s rule applied to this file.**

---

### P9 — A Brazilian national-curriculum agent, where the standards layer is already hosted and the budget goes to the platform half — NEW at p343

**Trigger:** 🟢 **LATAM — Brazil.** Any engagement that must answer *"does this student's work meet the BNCC, and which habilidade does it hit?"* — public-sector delivery, a Brazilian edtech, or a global platform localising for Brazil. 🔵 **The trigger that makes it urgent:** Brazil's **PL 2338/2023** (Senate-passed 2024, awaiting the Chamber of Deputies) would classify student selection as high-risk with fines to **BRL 50M or 2% of turnover** — so the curriculum-alignment audit trail is cheapest to build now, before the bill lands.

**Why this recipe exists, stated honestly:** 🔴 **Five passes of this base recorded that the LATAM supply side returned nothing placeable.** 🟢 **It was wrong, and the asset is nine stars deep:** every discovery leg here is star- or trending-ranked, and the Brazilian curriculum stack is invisible to all of them (`intel/trends.md` **T37**, `ACTION ZZ-d`).

**Wiring:**
1. 🟢 **`bncc-dev/bncc-pacotes`** (**MIT** code + **CC BY 4.0** data, `main/LICENSE` is a Portuguese `# Licenças` splitter) — **the standards layer, and it is already a product.** Three ways in, pick by stack: `@bncc/dados` (npm **v0.7.0**, typed TS API — `porCodigo`, `habilidadesEF`, `buscar`, `decodificar`), `bncc` (PyPI **v0.5.0**, the same API in snake_case), or **`@bncc/mcp` (npm v0.6.0)**. 🟢 **Fastest path: the hosted MCP at `mcp.bncc.dev` — streamable HTTP, NO API KEY, seven tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`). **A day-one agent demo needs no infrastructure at all.** 🟡 Pin `@bncc/dados` for production rather than depending on the hosted endpoint, and note the packages are **0.x** — the README ties `1.0.0` to the `dados-v1.0.0` release of `bncc-dados`.
2. 🟢 **`bncc-dev/bncc-dados`** (**CC BY 4.0**) — the dataset itself, **1 721 learning objectives of Brazilian basic education**, which the README states are *"verificadas contra os documentos oficiais do MEC/CNE"*. Vendor this, pinned by commit, if the engagement cannot call out.
3. 🟢 **`bncc-dev/bncc-benchmark`** (**MIT** harness + **CC BY 4.0** items/results) — **the evaluation half, in the same licence shape.** 🔵 **This is the step that makes the deliverable defensible rather than demo-able:** an item bank and a published methodology for scoring a model against the national curriculum. Use it as the acceptance gate, not as a marketing number.
4. 🟢 **`ArnaudGuiovanna/tutor-mcp`** (**MIT**, 1 073 B, 467 c · 5 a · head 2026-10-16) — the **deterministic pedagogy** engine: BKT for mastery, FSRS for review timing, prerequisite rules, mastery routing at 0.85, narrative memory for session context. 🔵 **Feed its skill graph from the BNCC codes** so progression is expressed in the national framework's own vocabulary rather than a bespoke taxonomy. SQLite for a pilot, PostgreSQL for the institution profile.
5. 🟡 **`portabilis/i-diario`** (**AGPL-3.0**, 35 326 B — read first-hand at p341/p342) if the engagement must touch a Brazilian SIS. 🔴 **It has no agent seam of its own**, so this is a build, and the AGPL stays on the far side of it.
6. 🟢 **`Cvmcosta/ltijs`** (Apache-2.0, placed **LATAM — Brazil** at p342) as the LMS seam — Brazilian-maintained, which matters in a public-sector bid.

**Licence posture:** 🟢 **The cleanest LATAM recipe on this shelf.** Steps 1–4 and 6 are MIT/Apache-2.0 code with CC BY 4.0 data — **no copyleft anywhere in the client's own layer**, and attribution is the only obligation on the data. 🔴 **Two things to get right:** the **`bncc.dev` name and visual identity are explicitly NOT licensed** (*"o código é livre; a marca não"*), so a derivative must not present itself as bncc.dev; and if step 5 is in scope, the AGPL-3.0 SIS must sit behind a service boundary. **Timeline:** 6–8 weeks for the alignment agent (steps 1–4), 12–14 with the SIS integration.

---

### P10 — Deterministic pedagogy behind a generative tutor, for a buyer who has to defend the progression decision — NEW at p343

**Trigger:** 🟢 **EMEA first, then North America.** The EU AI Act classifies admissions, student evaluation and exam scoring as **high-risk** — risk management, data governance, human oversight and conformity assessment *before* deployment. 🟢 **Also North America, where the obligation now has the same shape from a different direction:** **New York City** places **grading and discipline** in a *prohibited* tier, and **Oklahoma SB 1734** bars AI as the primary basis for grading or discipline. 🔵 **Both regimes ask the same question — *what decided this?* — and a prompt cannot answer it.**

**Why this recipe exists:** 🔴 **Every tutor on these shelves whose progression logic lives in a prompt fails this question by construction.** There is no artefact to audit, no threshold to show, and no way to replay the decision. 🟢 **The 2026 answer is a split architecture, and it now exists as off-the-shelf MIT parts:** the model generates and explains; a deterministic engine decides what comes next.

**Wiring:**
1. 🟢 **`ArnaudGuiovanna/tutor-mcp`** (**MIT**, 1 073 B) — **the decision engine, and the reason this recipe is buildable rather than aspirational.** Its own framing is *"Generative teaching. Deterministic pedagogy"*: **BKT** knowledge estimates, **FSRS** review scheduling, prerequisite rules, assessment evidence, a mastery routing threshold of **0.85**, and two MCP tools that carry the contract — `get_next_activity` (the client asks what to do) and `record_interaction` (the client reports what happened). 🟢 **Because progression is a function of stored state and a published threshold, the answer to *"why was this learner advanced?"* is a query, not a narrative.** Transports: local stdio, or remote HTTPS with **OAuth** — the Institution profile on PostgreSQL. 🟡 **Alpha, v0.6.1** — pin it, and budget for reading its migrations.
2. 🟢 **`CAHLR/OATutor`** (**MIT**, UC Berkeley CAHLR) — the **second, independent** BKT implementation on these shelves, and the one with academic provenance. 🔵 **Use it as the cross-check, not as a duplicate:** two mastery estimates that disagree on a cohort is exactly the finding a conformity assessment wants documented, and it costs one evaluation run.
3. 🟢 **`ankimcp/anki-mcp-server`** (**MIT**, 521 ★, placed **EMEA**) — the retention layer over real Anki decks, so spaced repetition runs in a tool the learner already owns and the review schedule is inspectable outside the vendor's database. 🔵 **A client-owned review store is a data-residency answer as much as a pedagogical one.**
4. 🟢 **`Selleo/mentingo`** (**MIT**, 1 062 B, **1 348 c · 48 a**, placed **EMEA — Poland**) — **the delivery surface, and the step that changes this recipe's economics.** It is the first AI-native LMS on these shelves an engagement can **fork** rather than integrate; every other platform here (Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0) costs an adapter and imposes copyleft on the hosting question. 🟢 **MIT means the client's own layer stays closed.**
5. 🟡 **`withmarbleapp/os-taxonomy`** (ODbL-1.0 + CC BY-SA-4.0, 6.6k ★, placed **EMEA**) for the prerequisite graph — **1 591 micro-topics, 3 225 prerequisite edges.** 🔴 **Read `intel/trends.md` T37 before this step.** Use the **graph and the standard CODES**, keep the client's enrichment in a **separate** database so no Derivative Database is created, and do not ship Common Core or NGSS **prose**: CCSS is purpose-limited and NGSS is codes-only pending WestEd approval. 🟢 **For a UK engagement this step is clean** (OGL v3.0, full text, no share-alike); **for Australia it is clean with ACARA's notice**; **for Brazil, swap in P9's step 1–2.**
6. 🟢 **`falkenslab/moodle-mcp`** (**MIT**) if the client will not leave Moodle — ~230 tools under the teacher's own login, students anonymised to the model. 🔵 **The anonymisation is not a nicety here; it is the data-minimisation argument the AI Act asks for, already implemented.**

**Licence posture:** 🟢 **Steps 1–4 and 6 are MIT end to end — the first recipe on this shelf with no copyleft and no purpose-limited content in its core path.** 🔴 **Step 5 is the only licence decision, and it is a CONTENT decision, not a code one.** **Timeline:** 8–10 weeks for steps 1–4; add 3–4 for the conformity technical file, which is the deliverable the EMEA buyer is actually purchasing.

🔵 **What P10 deliberately does not contain:** a claim that BKT or FSRS is pedagogically better than a well-prompted model. 🟢 **The argument is narrower and it is the one the regulation makes: the decision must be inspectable.** An auditable threshold that is slightly worse on a benchmark beats an excellent prompt that cannot be examined, in both of the jurisdictions above.

## Pass 342 · 2026-10-20 — eight recipes, unchanged in structure; P8's step 5 is no longer a manual step, and P8 gains the check that stops the opposite error

**Evidence:** [`p342-nonenglish-title-falsifier`](../evidence/p342-nonenglish-title-falsifier.2026-10-20-p342.tsv) · [`p342-channel-disagreement`](../evidence/p342-channel-disagreement.2026-10-20-p342.tsv).

🟢 **P1–P7 are unchanged.** 🟢 **P8, the grant-legibility pass, is the only recipe this pass touches, and the change is that one of its steps became tooling.**

### P8 — amended at `p342`

🔴 **What `p341` wrote when it created P8:** *"No instrument exists for step 5 of `P8`; it is manual and said to be manual."* Step 5 was: *when the family classifiers return nothing, read the payload by hand and determine whether the licence is simply stated in a language the tooling does not read.*

🟢 **Step 5 is now instrumented for the detection half.** `pass257.scan()` returns a **distinct verdict** for exactly that case — `UNREADABLE-TITLE:no-family-vocabulary-for-this-language` — so *"a language the tooling does not read"* is now a value the pipeline emits rather than a hypothesis a human forms. **Wire step 5 as: route every `UNREADABLE-TITLE` row to a human, and nothing else.** Portuguese AGPL titles resolve without a human at all.

🔴 **Step 5b, NEW, and it is the error that step 5 as written would have made.** A row returning no family is **not** necessarily a language problem. Measured this pass: of three payloads with no family, **one** was a translated grant and **two** were **dual-licence index documents** where the correct answer is *two* families and no single-family classifier can be right. **Before concluding "unreadable language", check whether the payload is an index pointing at sibling files.** The tell is cheap: a short payload (< 2 KB) whose text names two or more families and contains no operative grant clause.

🔴 **Step 5c, NEW — the opposite failure, and the more dangerous one.** A payload can resolve **confidently and wrongly**. `lib/license_family.sh::family_of` answers `MIT` on `haolpku/k12-kgraph`, whose operative grant is **CC BY-NC-SA 4.0**, by reading the payload's cross-reference to a sibling `LICENSE-CODE` file as its own grant. **So P8 must never promote a row on `family_of` alone:** require `pass257.scan()` (which returns `RESTRICTED:added-restriction` on that payload) and, for any dataset or content row, `pass258.content_verdict()` (which returns not-usable with `noncommercial` and `sharealike` both named). 🔵 **Two channels, always, and `p262`'s rule as the reason: a row's state is not what it QUOTES.**

**Licence posture of P8, restated:** the recipe produces a **decision record**, not a running system, and every component it names is already on these shelves. **Regional trigger:** any engagement whose supply includes Brazilian municipal or curriculum repositories — where this pass measured 3 of 6 Portuguese payloads returning no family on the first channel.

## Pass 341 · 2026-10-20 — eight recipes, each named down to the slug, each with its licence posture stated and its regional trigger

🟢 **New at p341: P8, the grant-legibility pass** — the recipe the 208-payload census turned into a deliverable, and the first on this shelf whose output is a decision record rather than a running system. 🔵 It exists because this pass found that a row can sit on a shelf for 22 passes reading *"licence not shown"* when the licence is plainly stated in a language the tooling does not read (`intel/trends.md` **T31**).

🟢 **P7, the institutional LMS seam** — the first recipe whose components are *regionally placed*, built on p340's completed connector census. P1–P6 are p339's and are unchanged.

Every repository named below was existence- and grant-verified first-hand this pass (`git ls-remote` + `raw.githubusercontent.com`; see `agents/top.md` for the channel table). **The licence posture line is not decoration** — six of eight Tier-1 platforms are GPL/AGPL, so each recipe states explicitly where the client's proprietary logic lives.

---

### P1 — The copyleft-safe AI tutor inside an existing LMS

**Trigger:** client already runs Moodle, Canvas or Open edX and wants an AI tutor without forking it. The most common engagement in this KB.

**Wiring:**
1. **`Cvmcosta/ltijs`** (Apache-2.0) — stand up the tutor as a certified **LTI 1.3 / LTI Advantage** tool. This is the seam: it installs into Moodle, Canvas, Open edX, Sakai, Blackboard and D2L unchanged.
2. **`CAHLR/OATutor`** (MIT) — take its **Bayesian Knowledge Tracing** mastery model as the learner-state engine. BKT gives you a defensible, inspectable mastery estimate; an LLM alone does not.
3. **`ArnaudGuiovanna/tutor-mcp`** (MIT — 🔴 **upstream; `kvnloo/tutor-mcp` is a fork 15 commits behind, corrected at p343**) — skill-graph construction with prerequisites, plus review scheduling, exposed over MCP so any model can drive it.
4. **`satvik314/educhain`** (MIT) — generate the MCQs and lesson scaffolds the tutor serves, across its 8 pedagogical approaches.
5. Grades and roster flow back through LTI Advantage **AGS/NRPS**, so the LMS stays the system of record.

**Licence posture:** 🟢 **Entirely permissive.** Nothing touches the AGPL/GPL platform tree; client logic stays closed. **Timeline:** 6–8 weeks to a piloted tool in one course.

---

### P2 — Auditable assessment AI built for the EU conformity runway

**Trigger:** EMEA client with grading or admissions AI. **Why now:** Regulation (EU) 2026/1744 moved Annex III education duties to **2 Dec 2027** — a 16-month design window before remediation pricing applies.

**Wiring:**
1. **`jupyter/nbgrader`** (BSD-3-Clause) on **`jupyterhub/jupyterhub`** (BSD-3-Clause) — the **deterministic autograder runs first and owns the grade**. Non-negotiable: it makes the scoring reproducible, which is what a conformity file needs.
2. **`anthropics/k12-teacher-skills`** (Apache-2.0) — its grading-support and differentiation skills as the **second-pass reviewer** over the autograder's output: narrative feedback, not score authority.
3. **`Cvmcosta/ltijs`** (Apache-2.0) — deliver into the LMS and return grades via AGS, so every write is attributable.
4. Human-oversight gate: no AI-only grade is ever released. Log the model version, prompt, inputs and the reviewing human per decision — this *is* the Article 14 evidence.
5. **`opencast/opencast`** (ECL-2.0) only if lecture-capture evidence is in scope.

**Licence posture:** 🟢 Permissive + ECL-2.0; no copyleft exposure.
🔴 **Hard constraint:** ship **no** emotion, attention or engagement inference. **Article 5(1)(f) prohibits emotion inference in educational institutions outright** — it is not a high-risk category you can document your way into. **Timeline:** 10–12 weeks for the conformity-ready pipeline.

---

### P3 — Teacher-workload reduction over Moodle, no platform changes at all

**Trigger:** teacher enablement is the named bottleneck in **every** region measured this pass. Fastest visible win in the KB.

**Wiring:**
1. **`falkenslab/moodle-mcp`** (MIT) — ~230 Moodle tools under the **teacher's own login**, with students anonymised to the model. Ships Spanish and English docs.
2. **`anthropics/k12-teacher-skills`** (Apache-2.0) — lesson-plan creation, tiered differentiation (below / at / above proficiency), lesson prep.
3. **`DaRL-GenAI/instructional_agents`** (MIT) — ADDIE-model multi-agent course design for whole-unit builds rather than single lessons.
4. **`littlecookie0722/AI-Teaching-Agent`** (MIT) — Markdown source → reviewable Lab + Exam package. 🟡 Use the **CLI** path; its README states MCP/agent expansion is frozen.
5. **`h5p/h5p-php-library`** (GPL-3.0) — emit interactive content types into Moodle. 🟡 Consume H5P as a **packaging target**, don't link client code into the library.

**Licence posture:** 🟢 Permissive agents against an unmodified GPL platform — the MCP server is a separate program, so no copyleft reaches the client's code. **Timeline:** 3–4 weeks to a pilot cohort; the shortest path to a demonstrable result.

---

### P4 — Offline-first deployment for the LATAM and low-connectivity curriculum gap

**Trigger:** CENIA found **13 of 19** LATAM countries do not teach early AI; Google.org's USD 4.6 M targets 1.25 M students across 9 countries by 2028. Much of that footprint has no reliable connectivity, where a cloud tutor cannot run at all.

**Wiring:**
1. **`learningequality/kolibri`** (MIT) — offline-first platform and content channels. The only MIT Tier-1 platform; it is the whole reason this pattern is viable.
2. **`chamilo/chamilo-lms`** (GPL-3.0) — where an institutional LMS is required, Chamilo's LATAM and Francophone-Africa installed base beats importing a US default.
3. Local inference on a school server for the tutor loop, with **`satvik314/educhain`** (MIT) used **ahead of time** to batch-generate quizzes and lesson plans into Kolibri channels — content is pre-built, not generated per request.
4. **`withmarbleapp/os-taxonomy`** (ODbL) for curriculum alignment of the generated content. 🔴 **ODbL has share-alike reach over derived databases** — counsel must clear it before a derived alignment database ships.
5. **`ankimcp/anki-mcp-server`** (MIT) / **`ankitects/anki`** (AGPL-3.0) for offline spaced-repetition retention. 🟡 Anki core is AGPL — drive it through its API, never patch its tree.
6. Spanish/Portuguese first, English second. **`moodle-mcp`**'s Spanish docs make it the teacher-facing default if the client is on Moodle.

**Licence posture:** 🟡 Mixed. MIT core; GPL and AGPL components consumed as **unmodified deployed systems**; ODbL needs a counsel sign-off. **Timeline:** 8–10 weeks including offline content pre-generation.

---

### P5 — National-curriculum delivery at mandate scale

**Trigger:** China's compulsory AI from age six (Sept 2025); India's mandatory AI and computational thinking from **Class 3 in 2026-27** behind the ₹10,372 crore India AI Mission; US state CS/AI graduation credits. State-procured, national volume.

**Wiring:**
1. **`openedx/edx-platform`** (AGPL-3.0) deployed via **`overhangio/tutor`** (AGPL-3.0) — the MOOC-scale backbone. 🔵 Do not attempt Open edX without Tutor.
2. **`openedx/frontend-app-learning`** (AGPL-3.0) for the bespoke learner UI the ministry will demand.
3. **`THU-MAIC/OpenMAIC`** (MIT, v1.2.1 2026-10-18) — multi-agent classroom with AI teacher plus AI classmates; generates slides, quizzes, simulations and project work. Server-first generation survives closed tabs, which matters on shared school hardware. 🔵 APAC-native: its default search providers are Kimi and DeepSeek — an asset here, a residency question in EMEA.
4. **`HKUDS/DeepTutor`** (Apache-2.0, v1.6.15 2026-10-19) — bounded tutoring memory and learning-path review for the personalised layer across a multi-year cohort.
5. **`Cvmcosta/ltijs`** (Apache-2.0) — keep every proprietary extension outside the AGPL tree.

**Licence posture:** 🔴 **AGPL-3.0 at the core — decide this at architecture time.** Hosting a *modified* Open edX as a service owes modified source to its users. Keep differentiating logic in LTI/MCP services; deploy Tutor's plugin framework rather than patching the platform.
🔴 **Compliance gate is pre-launch in China** (security assessment + algorithm filing before public launch, content labelling since Sept 2025) and **platform-layer in India** (amended IT Rules effective 20 Feb 2026: labelling and due diligence on AI-generated content). Scope it into the delivery timeline, not after UAT. **Timeline:** 14–18 weeks for a national pilot.

---

### P6 — Employability-linked skilling, the LATAM commercial pattern

**Trigger:** HolonIQ's 2026 LATAM EdTech 100 shows the market shifting from course delivery to **job-outcome-linked** training — Ginia (MX), Vetto (BR), Teachy (BR), Mattilda (MX). This is where regional money actually is.

**Wiring:**
1. **`GeminiLight/gen-mentor`** (CC0-1.0) — the goal-oriented ITS from the WWW 2025 paper: refine the target role, measure the gap against the learner's background, schedule sessions, generate each session's reading and quiz, rebuild the learner profile from behaviour. **Goal-to-gap-to-path is precisely the employability loop.** 🟡 CC0 is a public-domain dedication, not a software licence — no patent grant, no warranty disclaimer; have counsel look before it enters a deliverable.
2. **`ArnaudGuiovanna/tutor-mcp`** (MIT — 🔴 **upstream, corrected at p343; the fork was cited here for six passes**) — hold the role's skill graph with prerequisites, and version it as the target role changes.
3. **`frappe/education`** (GPL-3.0) for enrolment and administration, or **`frappe/lms`** (AGPL-3.0) for delivery. 🟡 **The two halves of the Frappe stack sit on different rungs** — Education is GPL, LMS is AGPL. Choose deliberately; the AGPL half is the network-facing one.
4. **`GibbonEdu/core`** (GPL-3.0) if a school-management/SIS layer is needed; **`OS4ED/openSIS-Classic`** (**GPL-2.0**, `master/docs/License.txt`) is the other real option. 🔴 **Declared gap: no permissively licensed SIS of scale exists** — all three candidates (Gibbon GPL-3.0, Frappe Education GPL-3.0, openSIS GPL-2.0) are copyleft. If the client needs closed SIS extensions, build a bespoke SIS service over LTI 1.3 instead of forking a GPL one. 🔵 Credentialing note: Open Badges is implementable, but `1EdTech/openbadges-specification` carries the **IMS Global Specification Document License**, not an OSI grant — implement the spec, do not vendor the document.
5. **`Cvmcosta/ltijs`** (Apache-2.0) as the seam, again.
6. 🟡 Brazil's **Bill 2.338/2023** would make student selection high-risk with fines to **BRL 50 M or 2 % of turnover**; it has passed the Senate and sits in the Chamber. Build the audit trail now — and re-check the bill's status against Chamber records before quoting it.

**Licence posture:** 🟡 Mixed; CC0 and the GPL/AGPL Frappe split are the two items needing a decision before build. **Timeline:** 8–10 weeks.

---

### What these recipes deliberately do not contain

- 🔴 **No emotion, attention or engagement inference anywhere.** Prohibited outright in EU educational settings under Article 5(1)(f). Excluded from all six patterns by design, including the APAC and LATAM ones, so that a pattern is never region-locked by a feature that cannot cross into EMEA.
- 🔴 **No AI-only grade release in any pattern.** Demand is highest in assessment and so is scrutiny (EU Annex III; Vietnam's high-risk classification). Every grading path runs a deterministic autograder first and a human gate last.
- 🔴 **`eth-lre/mathtutorbench` is not wired into P1 or P2** despite being the natural tutoring benchmark. It **serves no licence file on a 10-path ladder** — unlicensed, therefore not usable in a client deliverable. Named rather than silently omitted, so a future pass re-probes it instead of re-discovering it.
- 🟡 **No star-count-based ranking.** Both channels that serve stars are 403 here. Ordering above reflects **licence safety and dated evidence**, not popularity.

---

### P7 — The institutional LMS seam, forked rather than built (EMEA, APAC, North America — and the LATAM build) — NEW at p340

**Trigger:** a client is one institution (a university, a ministry pilot, a school network) running a *tenancy* of Canvas, Moodle, Brightspace or Blackboard, and wants an agent over it in weeks rather than quarters. 🔵 **This is the pattern p340's census made possible: a connector to a specific institution's tenancy already exists, under MIT, for four institutions on three continents, and forking one is strictly cheaper than writing the API client again.**

**Wiring:**
1. **Pick the regional precedent, not the generic lane.** **`pablopc05/mcp-usc`** (MIT, `main/LICENSE`) for a **European Moodle** tenancy — Spanish-language, CI, acts under the student's own permissions. **`psychquant/che-ntucool-mcp`** (MIT) for an **APAC Canvas** tenancy. **`skhdemo/uoft-quercus-mcp`** (MIT) for a **North American Canvas** tenancy with a personal-access-token model. **`sonaiengine/ku-portal-mcp`** (MIT, on PyPI) where the seam is a **student portal** rather than an LMS.
2. **Lift the write gate before writing any feature.** `che-ntucool-mcp` gates **grade and announcement writes behind an explicit human confirmation** and leaves reads unguarded. 🟢 **Port that boundary first** — it is the EU AI Act Article 14 human-oversight control, and it satisfies Korea's high-impact and Vietnam's high-risk education provisions at the same time.
3. **Swap the platform client, keep the tool surface.** All four are thin API clients around a documented LMS API behind an MCP tool surface. Re-pointing the base URL and auth strategy to the client's tenancy is the actual work; the tool definitions, the pagination and the error handling carry over.
4. **Add the mastery model, not just the chat.** **`CAHLR/OATutor`** (MIT) for inspectable **Bayesian Knowledge Tracing**, or **`ArnaudGuiovanna/tutor-mcp` (upstream, corrected at p343)** (MIT) for the skill graph and review scheduling, so learner state is defensible rather than a prompt.
5. **Generate into the platform, not beside it.** **`satvik314/educhain`** (MIT) for MCQs and lesson scaffolds; write them back through the connector so the LMS stays the system of record.
6. **If the platform is Open edX, stop and use LTI 1.3 instead.** Both Open edX MCP lanes are **AGPL-3.0** and one is a Tutor plugin. 🔴 **MCP is the wrong seam on that one platform.**

**Licence posture:** 🟢 **Entirely permissive — every component above is MIT, each grant read from the file at p340.** Nothing touches the platform's GPL/AGPL tree, so client logic stays closed. 🔴 **Two traps the census named, and both are in repositories a roundup will recommend:** verify the connector's grant **from its tree, not its badge** — **23 of 93 (25%) have no licence at all**, and on **Blackboard that is 4 of 7** — and never adopt **`AStheTECH/mewcp-google-classroom`**, whose `LICENSE.md` is a proprietary licence forbidding commercial use and SaaS hosting (`intel/trends.md` T29).

**Timeline:** **2–4 weeks** to a working agent over the client's own tenancy when a regional precedent exists and is forked; **6–8 weeks** where one does not and the API client is written from scratch.

🔴 **Regional note, stated as a gap rather than a claim:** **there is no LATAM precedent to fork.** p340 probed the two candidates these shelves carried — `idavi/usp-mcp` (Universidade de São Paulo by its name) **does not exist**, and `DaviPac/Classroom-mcp` (Portuguese, referencing **SIGAA**) has **no licence and two AI-authored commits**. 🟢 **So in LATAM this pattern inverts into a build — and the cheapest build is a fork of `mcp-usc`, which is already Spanish-language and already Moodle.** Fifth consecutive pass at which the LATAM supply side returned nothing adoptable.

---

## ⏷ Carried history — everything below this line predates Pass 340 and was NOT rewritten

🟢 **Pass 339 prepends; it does not replace.** An earlier draft of this pass replaced these shelves outright and `gate-permissive-arm` caught the cost: the corpus lost ~1.2 MB of first-hand-verified rows and the `MIT`+`Apache-2.0` cell count fell from 7 000+ to 6 597. 🔵 **Deleting verified rows is not curation** — the live section above carries this pass's findings, and every prior pass's verified shelf stands underneath it.

## Pass 338 · 2026-10-20 — three recipes, every component's grant re-read first-hand this pass, and the first one sells the gap this pass measured in four regions

🔵 Every component below carries a grant measured on `raw.githubusercontent.com` **this pass**, at a branch resolved by `git ls-remote --symref`. Byte counts are from where the file landed. 🔴 **New in these recipes: each component records the AXIS of its grant** (root or nested), because `agents/top.md` FINDING 1 shows a root-only scan silently mis-grades the platform tier.

---

### 🟢 R-338.1 — The AI-governance boundary: sell the 56-point gap, not a model

**The problem it solves.** The measurement this pass made in two hemispheres: **66%** of North American students use ChatGPT while **10%** of institutions have formal AI guidelines; **92%** of LATAM students and **79%** of faculty engage with AI while **~30%** of universities have published a policy. 🔴 **No model ships a fix for that, and a tutor deployment makes it worse** — more usage inside an institution that still has not decided what is allowed.

| role | component | grant, re-read this pass | axis | why this one |
|---|---|---|---|---|
| delivery platform | https://github.com/OpenOLAT/OpenOLAT | 🟢 **Apache-2.0**, `master/LICENSE`, **10 982 B** | 🟢 root | 🟢 the only permissive platform in the LMS tier — the governance layer you build stays yours |
| mastery model | https://github.com/CAHLR/OATutor | 🟢 **MIT**, `main/LICENSE`, **1 105 B** | 🟢 root | 🟢 **BKT is explainable.** A school board can be shown *why* a learner was advanced; a transformer's logits cannot be |
| teaching-lab runtime | https://github.com/jupyterhub/jupyterhub | 🟢 **BSD**, `main/LICENSE`, **1 475 B** | 🟢 root | 🟢 attribution only; authenticators and spawners may be closed. Per-user isolation is the audit unit |
| authoring | https://github.com/openpatch/hyperbook | 🟢 **MIT**, `main/LICENSE.md`, **1 069 B** | 🟢 root | static, reviewable courseware output — a diff is the audit trail |

**How to wire it.**
1. **OpenOLAT as the system of record**, unmodified, deployed on client infrastructure (this is also the APAC sovereignty answer).
2. **Your governance service sits outside it** and is the deliverable: an acceptable-use policy engine, a disclosure register (which learner interaction used which model, when), and a human-in-the-loop checkpoint on anything touching grades or progression.
3. **Integrate over LTI 1.3 / web services only.** 🔴 Never as an in-tree plugin — see the licence note below.
4. **OATutor supplies the mastery estimate**, and because BKT is auditable, the disclosure register can state the reason for every advancement decision.
5. **Hyperbook authors the content** so that every change to what a learner is told is a reviewable commit.

🟢 **Why the boundary is also the licence answer.** OpenOLAT is Apache-2.0, so in principle in-tree work is safe — **but build the LTI boundary anyway**, because it is what makes the same governance service sellable on Moodle (GPL-3.0), Chamilo (GPL-3.0) and Open edX (AGPL-3.0) without relicensing a line. 🔵 **One service, four platforms, zero copyleft reach into the deliverable.**

🟡 **The honest bound:** the percentages above are search-channel and attributed, and the LATAM primary source was unreachable from this environment (`ENOTFOUND`). **Use them to size an offer, not to price a contract.**

---

### 🟢 R-338.2 — A licence-verification step that does not mis-grade the platform tier

**The problem it solves.** 🔴 **A root-only SPDX scan gets the grant wrong on 8 of the 11 foundation rows measured this pass**, and it fails in both directions: it reports GPL-2.0 platforms as *unlicensed*, and secondary comparison pages report one of them as *Apache-2.0* when it is GPL-2.0. **Either error mis-prices a bid.**

| role | component | grant, re-read this pass | axis | the trap it demonstrates |
|---|---|---|---|---|
| nested-grant specimen | https://github.com/formalms/formalms | 🟡 **GPL-2.0**, `master/`**`html/license.txt`**, **18 346 B** | 🔴 **NESTED** | 🔴 grant at depth **and** a 6 198 B README that never says *licence* — both standard channels miss it |
| nested-grant specimen | https://github.com/OS4ED/openSIS-Classic | 🟡 **GPL-2.0**, `master/`**`docs/License.txt`**, **17 286 B** | 🔴 **NESTED** | 🟡 grant at depth, but the README names it — a README-link fallback does fire here |
| off-branch specimen | https://github.com/overhangio/tutor | 🔴 **AGPL-3.0**, `release/`**`LICENSE.txt`**, **34 523 B** | 🟢 root | 🔴 default branch is **`release`** — a `main`-pinned probe calls it ungranted |
| off-branch specimen | https://github.com/francoisjacquet/rosariosis | 🟡 **GPL-2.0**, `mobile/LICENSE`, **15 214 B** | 🟢 root | 🔴 default branch is **`mobile`** |
| off-name specimen | https://github.com/moodle/moodle | 🟡 **GPL-3.0**, `main/`**`COPYING.txt`**, **35 147 B** | 🟢 root | 🟡 the grant is not named `LICENSE` at all |

**How to wire it — four steps, in this order, and the order is the point.**
1. **Resolve the branch first:** `git ls-remote --symref https://github.com/<slug> HEAD`. 🔴 **Never assume `main`** — 7 of 11 foundation rows are not on it.
2. **Walk a case-varied root ladder** on *that* branch: both spellings (`licen[sc]e`), three casings, the extension set `{∅, .md, .txt, .MD, .TXT}`, plus `COPYING`/`UNLICENSE`/`MIT-LICENSE`. That is `ACTION ZL`'s 42 rungs.
3. **Before writing down an absence, exclude DEPTH** (`ACTION ZN`). Cheap version: prefixes `{docs, html, licenses, LICENSES, legal, src, lib, app, web, .github}` × stems `{LICENSE, LICENSE.txt, LICENSE.md, License.txt, license.txt, licence.txt, COPYING, COPYING.txt}`. Authoritative version: **enumerate the tree** (`make enumerate`).
4. **Read the TITLE LINE of the payload, not a badge.** 🔴 Byte bands are not identities — but they are a useful cross-check: a canonical AGPL-3.0 is **34 523 B** here on two unrelated repositories, GPL-3.0 is **35 147 B** on two more.

🔴 **The negative control is part of the recipe, not an optional extra.** Run the same probe against an invented slug (`<org>/definitely-not-a-real-repo`): it must come back `UNRESOLVED`. 🔵 **A `github.com` HTML `HEAD` returns 403 for everything in this environment, including repositories that do not exist** — it carries zero bits and must never be used as existence evidence (`ACTION ZM`). **Existence is `ls-remote`; grant is `raw`.**

---

### 🟢 R-338.3 — LATAM back-office automation, aimed at the one number that is not saturated

**The problem it solves.** UNESCO IESALC, 200 institutions across 19 countries: teaching and learning **73.5%**, research **57.0%**, 🟢 **administration 34.1%**, community engagement **20.0%**. 🔵 **The classroom is saturated and the back office is barely touched** — that is the widest whitespace on this shelf, and it is the half of a university that owns enrolment, retention and financial aid.

| role | component | grant, re-read this pass | axis | why this one |
|---|---|---|---|---|
| student information system | https://github.com/francoisjacquet/rosariosis | 🟡 **GPL-2.0**, `mobile/LICENSE`, **15 214 B** | 🟢 root | a real SIS, not an LMS: enrolment, scheduling, grades, the records the back office actually runs on |
| student information system | https://github.com/OS4ED/openSIS-Classic | 🟡 **GPL-2.0**, `master/`**`docs/License.txt`**, **17 286 B** | 🔴 **NESTED** | the alternative SIS, long public-sector install base |
| education statistics over MCP | https://github.com/SidneyBissoli/uis-mcp-server | 🟢 **MIT**, `main/LICENSE.md`, **1 088 B** | 🟢 root | 🟢 **UNESCO Institute for Statistics data as an agent tool**, and a **LATAM-placed** maintainer — regional benchmarking without building an ingest |
| LMS integration | https://github.com/Cvmcosta/ltijs | 🟢 **Apache-2.0**, `master/LICENSE`, **11 361 B** — re-read this pass, matching the p331 cell | 🟢 root | the LTI 1.3 boundary itself; 🟢 **LATAM-placed at p335** — root commit 2019-05-30, `-0300` on 513 of 575 commits |
| mastery model | https://github.com/CAHLR/OATutor | 🟢 **MIT**, `main/LICENSE`, **1 105 B** | 🟢 root | explainable retention signals — a bursar will not act on an unexplained score |

**How to wire it.**
1. **SIS stays unmodified** (`rosariosis` or `openSIS-Classic`). 🔴 Both are **GPL-2.0**, so in-tree modules are derivative: your logic lives in an external service that reads the SIS over its web API.
2. **Retention and financial-aid prioritisation in that external service**, with OATutor's BKT supplying an explainable mastery signal rather than an opaque risk score.
3. **`uis-mcp-server` supplies national benchmarks** so a single institution's numbers can be placed against its country's, which is the comparison a rector asks for first.
4. **`ltijs` carries the learning-side integration** when the SIS work expands into the LMS.
5. 🔴 **Honour `rosariosis`'s default branch (`mobile`) and `openSIS-Classic`'s nested grant (`docs/License.txt`) in your own dependency audit**, or your compliance report will declare two GPL-2.0 platforms unlicensed.

🟡 **The bound to state in the deck:** administration at **34.1%** is from the UNESCO IESALC survey of 200 institutions; the 92%/79% usage figures are from the Digital Education Council's LATAM 2026 survey (>30 000 responses, 29 institutions). 🔴 **Both are attributed, neither was read from a primary PDF this pass** — `digitaleducationcouncil.com` is `ENOTFOUND` from this environment.

## Pass 337 · 2026-10-20 — three recipes, every component's grant re-read first-hand this pass, and the first one is the ODbL boundary with a named family behind it

🔵 Every component below carries a grant measured on `raw.githubusercontent.com` **this pass**, at a branch resolved by `git ls-remote --symref` — not restated from a badge. Byte counts are from the repaired 42-rung ladder. Where a component is 🟡 or 🔴, the recipe says what the obligation is and what to do instead.

---

### 🟢 R-337.1 — Curriculum-graph tutoring that never creates a Derivative Database

**The problem it solves.** A client wants AI tutoring aligned to a real curriculum with prerequisites, and wants to keep its own IP. The curriculum data is **ODbL share-alike**; vendoring it creates a Derivative Database and drags the share-alike obligation onto the client's dataset.

| role | component | grant, re-read this pass | why this one |
|---|---|---|---|
| curriculum graph | `withmarbleapp/os-taxonomy` | 🔴 **ODbL-UNVERSIONED**, `main/LICENSE`, **25 289 B** (`ODbL 1.0 + CC BY-SA 4.0` per `PROVENANCE.md`) | 1 590 topics, 3 221 prerequisite edges — the only open prerequisite graph on these shelves |
| mastery model | `CAHLR/OATutor` | 🟢 **MIT**, `main/LICENSE`, **1 105 B**, © Z. A. Pardos / CAHL | 🟢 **BKT is explainable** — auditable to a school board, which the US oversight statutes require |
| delivery platform | `OpenOLAT/OpenOLAT` | 🟢 **Apache-2.0**, `master/LICENSE`, **10 982 B** | 🟢 the only permissive platform in the LMS tier — your layer may stay closed |
| agent orchestration | `huggingface/smolagents` | 🟢 **Apache-2.0**, `main/LICENSE`, **11 357 B** | small, auditable loop; no framework lock-in |

**Wiring, and the one rule that carries the licence.** 🟢 **Fetch `os-taxonomy` at runtime from its own distribution; never vendor it into the repo and never write its records into your database.** Hold topic IDs and prerequisite edges in memory per session, key your own progress records by **topic ID only**, and persist nothing of the graph itself. `OATutor`'s BKT consumes the topic ID and the learner's response history — **both yours** — and emits a mastery probability. `smolagents` wraps the tutoring loop; `OpenOLAT` carries delivery, identity and gradebook over LTI.

🔴 **What breaks it:** an ETL job that materialises the graph into a client table. That is a Derivative Database and ODbL §4.4 then requires it be offered under ODbL. 🟡 **And `data/curriculum-standards.json` is a separate question entirely** — UK National Curriculum records are **OGL v3.0** (ship the required notice verbatim), Common Core records are **purpose-limited CCSS Public License** with no clear derivative grant. 🔴 **Do not treat the repository as one licence; it is three.**

---

### 🟢 R-337.2 — An LMS-native teacher-workflow agent for a copyleft platform, with the client's logic staying proprietary

**The problem it solves.** The LATAM and EMEA public-sector install base runs **Moodle (GPL-3.0)** and **Chamilo (GPL-3.0)**. Teacher-facing AI is the demand (OECD TALIS: Brazil 56%, Chile 55% teacher AI use; Uruguay 75%), but in-tree plugin code is derivative and would have to ship GPL-3.0.

| role | component | grant, re-read this pass | boundary role |
|---|---|---|---|
| LMS core | `moodle/moodle` | 🟡 **GPL-3.0**, `main/`**`COPYING.txt`**, **35 147 B** | 🟢 **run UNMODIFIED** — no obligation attaches |
| LMS core, LATAM public sector | `chamilo/chamilo-lms` | 🟡 **GPL-3.0**, `master/LICENSE`, **35 147 B** | 🟢 same: unmodified core |
| LMS bridge | `csmediapro/moodle-mcp-server` (carried) | 🟢 MIT | 🟢 speaks Moodle **Web Services** — **no plugin installed on the LMS** |
| agent runtime | `huggingface/smolagents` | 🟢 **Apache-2.0**, **11 357 B** | your prompts, policy and tools — 🟢 **stays closed** |

**Wiring.** The agent runs **outside** the LMS as a service. It reaches Moodle over **Web Services** via the MCP bridge; it never links Moodle code, so the GPL boundary is never crossed. 🔴 **The compliance envelope is not optional here: the agent DRAFTS and a teacher DISPOSES.** DC bars AI from grading, discipline, IEP decisions and teacher evaluation; Oklahoma and Maryland bar high-stakes student decisions; the EU puts assessment in Annex III high-risk from **2027-12-02**. 🟢 So the deliverable is a **draft queue with an explicit human approval step and an audit record of who approved what** — which is also the artefact that sells.

🟡 **If the client insists on in-LMS UI**, the plugin must be GPL-3.0 — so keep the plugin a **thin view** (render, submit, approve) and leave every model call, prompt and policy in the external service. **Thin plugin, fat service.**

---

### 🟢 R-337.3 — A licence-and-branch preflight for any education component, before it reaches a client deck

**The problem it solves.** This pass measured three ways a component gets written down wrongly, each on real rows. The recipe is the base's own instruments, run in order, and it is cheap.

| step | instrument, in this repo | what it catches — each measured on a real row this pass |
|---|---|---|
| 1. does it exist? | `git ls-remote` | 🔴 **`curl -sI https://github.com/…` returns 403 for an INVENTED slug too** — the HTML channel carries **zero bits** here. `ls-remote` returns `RESOLVES` / `NO-REFS`. |
| 2. which branch? | `ls-remote --symref` | 🔴 **5 of 15** foundation repos do not default to `main` — `master` ×4 and **`release`** (`overhangio/tutor`); `rosariosis` defaults to **`mobile`** |
| 3. where is the grant? | `lib/probe_payload.sh`, 42 case-varied rungs | 🔴 **2 of 15** do not keep it at `LICENSE` (Moodle → `COPYING.txt`, tutor → `LICENSE.txt`); and a **lowercase `license.txt`** is a real shape (`kitschpatrol/yanki`, MIT, 1 071 B) that an uppercase ladder refuses |
| 4. is it a grant or a pointer? | `p307.classify_payload` | 🔴 a **682 B** Apache *appendix* is a `POINTER`, not a grant (p336's specimen) — size alone decides nothing, but 682 B cannot hold §2 and §3 |
| 5. which family, really? | `lib/license_family.sh` | 🔴 a **25 289 B** ODbL grant typed `UNCLASSIFIED` until this pass; **GPL-3.0 vs LGPL-3.0** is a linkability question (p336's five rows) |
| 6. is it alive? | bare-clone channel | 🔴 both new slugs this pass refused on it: **10 commits, last 2026-07-07**; **2 commits, one day old** |
| 7. where is it from? | `p115-region-evidence` | 🟢 timezone offsets + author domains place a row — `-0700` ⇒ North America, `+0100` ⇒ EMEA |

🔵 **Run it in this order because each step can invalidate the next.** A 403 read as a 404 refuses a real repository (step 1); a `main`-pinned probe invents an absence on `tutor` (step 2); an uppercase-only ladder invents one on `yanki` (step 3); and a named family that is not also named in the permission gate turns a correct ALLOWED into a wrong BLOCKED (step 5, caught on itself this pass). 🟢 **Steps 1-3 are one `ls-remote` and a handful of `raw` requests — the cheapest part of any engagement, and the part that decides whether the rest of the table is true.**

## Pass 336 · 2026-10-20 — four recipes, each wired only from rows this base has read first-hand

🔵 Every component below carries a grant read on `raw.githubusercontent.com` **and** an activity figure from the bare-clone channel. Where a component is 🟡, the recipe says what the risk is and what to do instead.

### 🟢 P336-A — The virtual classroom an institution already has a licence to extend

**Unblocked by this pass**: BigBlueButton is **LGPL-3.0**, not `GPL-3.0`. It is linkable, so a proprietary layer may drive it.

```
BigBlueButton  (LGPL-3.0, 7 652 B — virtual classroom, recording, breakouts)
  └── its own API / webhooks           ← link from OUTSIDE; do not patch internals
       ├── celtic-project/LTI-PHP      (LGPL-3.0, 7 651 B)  → PHP-side LMS launch
       │   └── or lti-tool/lti-tool    (MIT, 1 077 B)       → Node-side launch
       │   └── or Cvmcosta/ltijs       (Apache-2.0)         → Node, 🟢 LATAM-maintained
       ├── session recording  ──►  transcript  ──►  tutor-side learner model
       └── OATutor (MIT) BKT state     ← pedagogy, already on these shelves
```
🟢 **Why it holds:** the LMS integration is an LTI launch, not a fork; BigBlueButton stays unmodified behind its API, which keeps the LGPL boundary clean. **6–8 weeks** to a working lecture-capture-to-learner-model loop.
🔴 **The one rule:** no patches to BigBlueButton's source. A change to its own files must ship LGPL. Everything above goes in your layer.

### 🟢 P336-B — Custom interactive content, authored by subject experts, graded by an agent

```
openpatch/hyperbook      (MIT, 1 069 B · 2 087 c · 10 a · 456 c in 2026)
  └── Markdown → interactive courseware          ← subject experts author in Markdown
h5p/h5p-cli              (MIT, 1 066 B · 730 c · 39 a · 13 years)
  └── build + test CUSTOM H5P content types      ← the client's own interaction types
       └── drops into Moodle · Canvas · Open edX · Drupal unchanged
missing-elements/h5p-offline-player (MIT, 1 073 B)   🟡 288 c, 5 a, all 2026
  └── H5P playback with NO H5P server             ← rural / low-connectivity delivery
intellectif/learning-kit (MIT, 1 072 B · 275 c · 5 a)  🟡 region unresolved (L1)
  └── framework-free scoring, rubric + deferred grading, weighted assessment
```
🟢 **Why this is the strongest new recipe:** it replaces the assessment engine this shelf's patterns keep hand-rolling, and `h5p-cli` means the client's *own* interaction types — a lab simulation, a music-notation drill — become first-class LMS content instead of an iframe. **8–10 weeks.**
🟡 **Two stated risks:** the offline player is young (288 commits, one author-cluster) — treat as the low-connectivity *option*, not the default path; and `learning-kit`'s region is unresolved, which matters for data-residency, not for code.

### 🟢 P336-C — Moodle without web services, which is how Moodle actually arrives

🔴 **The recurring blocker:** institutional Moodle has web services **off**, and the sysadmin will not enable them for a pilot.

```
falkenslab/moodle-driver (MIT, 1 067 B)   🟡 320 c in NINE days, ONE author
  └── drives Moodle as any user, from code/CLI, with that user's own login
       └── no web-service enablement, no admin ticket, no procurement cycle
falkenslab/moodle-mcp    (MIT, 1 067 B)   🟡 169 c / 12 d / 1 a  (same maintainer)
  └── the same surface over MCP, for an agent
       ├── OATutor (MIT) BKT              → learner model from gradebook history
       └── uis-mcp-server (MIT, 🟢 LATAM) → UNESCO baselines for the cohort
```
🟢 **Use it to kill the procurement cycle on a pilot:** a two-week demonstrator against the real Moodle, on a real account, with no change to the institution's configuration.
🔴 **Do not stake a delivery date on it.** One author, nine days, 🟡 on this base's bar. The moment the pilot is approved, migrate to the web-services path or to `moodle-mcp` with a maintained fork you control. 🔵 Both halves share one maintainer — a single-point dependency on both legs of the same stack.

### 🟢 P336-D — The ministry conversation, which opens before any system exists

```
uis-mcp-server (MIT, 1 088 B · 100 c · 🟢 LATAM — Brazil · official MCP Registry)
  └── UNESCO Institute for Statistics indicators over MCP
       enrolment · completion · out-of-school rate · spend per student, by country
  └── agent reads the country's own baseline BEFORE the first workshop
Principled-Evolution/gopal (Apache-2.0, 11 357 B canonical — on these shelves)
  └── Rego policy packs: EU AI Act · GDPR · NIST AI RMF · FERPA
       └── per-jurisdiction gate:  what may be processed · logged · automated
            ├── 🔴 California AB 1159   → student data may NOT train models
            ├── 🔴 Oklahoma / Maryland  → human oversight; no high-stakes autonomy
            ├── 🟢 Vietnam              → human review exits the high-risk class
            └── 🟢 EMEA                 → transparency NOW; high-risk 2027-12-02
```
🟢 **Why it wins the room:** every other recipe needs the client to already own a system. This one answers *"how is our country actually doing"* from UNESCO's own numbers in the first meeting, then shows the governance layer that 74 % of LATAM institutions lack and 31 US states are legislating. **4–6 weeks** to a defensible baseline-plus-policy deliverable.
🔵 **This is the 87/26 engagement**: take the AI an institution already runs informally and give it a strategy, a data boundary and an audit trail.

## Pass 335 · 2026-10-20 — P30: the Brightspace front end a deliverable can own outright, and the two-channel licence gate that keeps it ownable

🔵 **T26 (this pass) says the proprietary vendor is the permissive one. P30 is what that buys.** On **D2L Brightspace** the whole UI layer — components, i18n, test reporting — is **Apache-2.0 from the vendor**, so a studio can build a client-facing front end with **no copyleft in the build chain and a patent grant on the way in**. 🔴 **On Open edX the same build is AGPL-3.0 and this pattern does not apply; use P28's LTI seam instead.**

### 🟢 P30 — A Brightspace-native assistant front end, all-permissive, vendor-benched

| Role | Component | Grant, read first-hand | Activity, bare clone | Placed |
|---|---|---|---|---|
| UI component system | [`BrightspaceUI/core`](https://github.com/BrightspaceUI/core) | 🟢 **Apache-2.0**, 10,421 B | 🟢 **9,598 c · 180 a · 1,020 c in 2026 · head 2026-10-19** | 🟢 NA, `d2l.com(2,748)` |
| i18n / formatting | [`BrightspaceUI/intl`](https://github.com/BrightspaceUI/intl) | 🟢 **Apache-2.0**, 10,421 B | 115 npm versions · head 2026-09-23 | 🟢 NA |
| Experimental components | [`BrightspaceUI/labs`](https://github.com/BrightspaceUI/labs) | 🟢 **Apache-2.0**, 10,421 B | published through 2026-10-19 | 🟢 NA |
| Test evidence for the UI | [`Brightspace/test-reporting-node`](https://github.com/Brightspace/test-reporting-node) | 🟢 **Apache-2.0**, 10,421 B | 🟢 **1,129 c · 13 a · 358 c in 2026** | 🟢 NA |
| MCP seam into the LMS | [`rohanmuppa/brightspace-mcp-server`](https://github.com/rohanmuppa/brightspace-mcp-server) | 🟢 **MIT**, 1,068 B | 414 c · 17 a · head 2026-10-20 (p334) | 🟢 NA |
| Standards seam, if the client is multi-LMS | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0**, 11,361 B | 575 c · 17 a · 51 c in 2026 | 🟢 **LATAM — Brazil** |
| Grade write-back with the approval hop | P26 | — | — | — |
| Licence gate in CI | [`google/licenseclassifier`](https://github.com/google/licenseclassifier) | 🟢 **Apache-2.0**, 11,358 B | 249 c · 30 a (p333) | — |

### 🟢 The wiring, concretely

1. **Build the front end on `@brightspace-ui/core`, not on a generic design system.** The client's users already know these components, and **accessibility is the vendor's problem, already solved** — that is the single largest hidden cost in an education UI engagement.
2. **Pin `@brightspace-ui/core` to an exact version.** 🔴 **2,121 published versions and 1,020 commits in 2026**: this moves fast enough that a floating range will break a demo. Renovate it on a schedule, not on `^`.
3. **The assistant talks to the LMS only through `brightspace-mcp-server`** — the same protocol boundary as P29, for the same reason: it is MIT, so the adapter is a deliverable the client owns.
4. **If the client runs more than one LMS, put `ltijs` in front instead** and keep the Brightspace components as the UI layer only. 🔵 The seam and the skin are separable, and **only the seam is portable**.
5. **Grade write-back goes through P26's approval hop** — unchanged, and it is what keeps the build outside the EU's Annex III high-risk class and inside Vietnam's entry-2 carve-out.
6. **Run the two-channel licence gate below in CI from day one.**

### 🔴 The two-channel licence gate — new this pass, and it is what T27 costs if you skip it

**A single-channel check passes this stack and still ships copyleft.** The gate has to read **both**:

1. 🟢 **Read the repository licence PAYLOAD, not the registry field.** `@groton/canvas-api` declares **no licence on npm** and its tree is **GPL-3.0, 35,149 B**. A registry-only gate sees an empty field and most implementations treat that as "unknown, continue".
2. 🟢 **Treat a registry grant with no payload as WEAK, not as absent and not as equal.** **8 of 27 packages measured this pass are declared-only** (7 MIT, 1 ISC). They are usually fine; they are not the same claim as a payload, and the row must say which channel it came from.
3. 🔴 **Never infer the holder from a long-form payload.** Apache-2.0 returns `owner or entity authorized by` and GPL/AGPL returns `Free Software Foundation, Inc.` — **boilerplate that reads like an institutional holder.** Read `NOTICE` for Apache, and otherwise fall through to the commit channel.
4. 🟢 **Fail the build on payload-copyleft, warn on declared-only, and record the channel in the SBOM row.** `licenseclassifier` does step 1 correctly; steps 2–4 are the wrapper this base now specifies.

🟡 **Honest limit on P30: it is a FRONT-END pattern.** It gets a studio an ownable, accessible, vendor-native UI with a clean licence story. **It does not make the LMS replaceable**, and on Open edX none of it transfers — the vendor's own tooling is AGPL-3.0 there, which is T26.

---


## Pass 334 · 2026-10-20 — P29: the MCP seam into a proprietary LMS, with a citing tutor behind it

🔵 **P28 (p333) wired the LTI 1.3 seam. P29 is the other seam, and it exists because of what p334 measured:** on a **proprietary** LMS the MCP connector is MIT, so the studio owns the whole integration outright. **Every row below was read first-hand at p334** — grant on `raw.githubusercontent.com`, activity from a bare `--filter=blob:none` clone.

### 🟢 P29 — Teacher-facing tutoring and course assistance over MCP, on an all-permissive stack

| Role | Component | Grant, first-hand | Activity, first-hand | Placed |
|---|---|---|---|---|
| MCP seam into the client's LMS — **Canvas** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT**, 1,071 B | **1,041 c · 30 a · 927 c in 2026 · head 2026-10-19** | 🟢 North America |
| …or **Brightspace / D2L** | [`rohanmuppa/brightspace-mcp-server`](https://github.com/rohanmuppa/brightspace-mcp-server) | 🟢 **MIT**, 1,068 B | **414 c · 17 a · head 2026-10-20** | 🟢 North America |
| …or **Blackboard** | [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) | 🟢 **MIT**, 1,084 B | 🟡 21 c · 3 a · head 2026-10-14 | 🟢 EMEA |
| …or **Google Classroom** | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | 🟢 **MIT**, 1,071 B (`master`) | 🟡 28 c · 3 a · head 2026-10-13 | 🟢 EMEA |
| The tutor, and it **cites the curriculum** | [`CogitoNTNU/TutorAI`](https://github.com/CogitoNTNU/TutorAI) | 🟢 **MIT**, 1,140 B | **1,140 c · 19 a · 111 c in 2026 · head 2026-10-07** | 🟢 EMEA — Norway |
| Pedagogy / mastery state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, 1,073 B | 467 c · 5 a · 2026-10-16 (p330) | — |
| Mastery model (BKT) | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | **1,045 c · head 2026-10-16** — re-confirmed first-hand p334 | North America |
| Teacher skills over MCP | [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) | 🟢 **Apache-2.0**, 10,173 B | 42 c (p327) | — |
| Licence gate in CI | [`google/licenseclassifier`](https://github.com/google/licenseclassifier) | 🟢 **Apache-2.0**, 11,358 B | 249 c · 30 a (p333) | — |
| Curriculum + eval corpus | [`Haozhe-Xing/agent_learning`](https://github.com/Haozhe-Xing/agent_learning) | 🟢 **MIT**, 1,068 B | **175 c · 11 a in 2026 · head 2026-10-17** | 🟢 APAC — China |

### 🟢 The wiring, concretely

1. **Stand up the platform's MCP server as its own process**, pinned to a commit, configured with a **service account scoped to the courses in the engagement** — not an instructor's token. On Canvas this is `vishalsachdev/canvas-mcp`; the lane is chosen by which LMS the client runs, and nothing else in the stack changes.
2. **The agent never calls the LMS API.** It calls MCP tools. 🔵 That is the whole point of this pattern: the seam is a protocol boundary you can log, replay and refuse at, and it is MIT, so the adapter is a client deliverable.
3. **`tutor-mcp` holds pedagogy state** — skill graph, BKT, FSRS review scheduling — and knows nothing about the LMS. **`OATutor`'s BKT** is the mastery model when the engagement needs a published, citable one (UC Berkeley, 1,045 commits).
4. **`TutorAI` is the retrieval half**: ingest the course's own textbook and **require the answer to cite it**. Its `backend/flashcards/knowledge_base/{embeddings,db_interface,llm,factory}.py` is a swappable retrieval layer and a swappable model factory, which is what lets the same deployment run a hosted model in North America and a self-hosted one in the EU.
5. **Write-back stays teacher-facing in v1.** Read rosters, read submissions, draft feedback — **and stop.** A grade is written by the instructor approving a draft, which is P26's step 5 and the reason this pattern passes the same four jurisdictions.
6. **`licenseclassifier` runs in CI over the whole dependency tree** — and p333's defect is why: a grant classifier that greps for a family name grades a repository by its maintainer's first name.

### 🔴 What will go wrong, named in advance

- 🔴 **`sandraschi/classroom-mcp` and `felipedias-ie/blackboard-mcp` are 21–28 commits and 3 authors each.** **Fork and pin.** Do not take an upstream bump mid-engagement on a connector this young.
- 🔴 **`falkenslab/moodle-mcp` is 169 commits by ONE author in 12 days.** Live, fast, and a single point of failure. 🟢 **On Moodle, prefer the LTI seam** (`lti-tool`, `tsugi`) and treat MCP as an accelerator you own a fork of.
- 🔴 **On Open edX there is no permissive MCP lane at all** — `blend-ed/openedx-mcp` is **AGPL-3.0**. **Use LTI 1.3 and P28 instead**; do not reach for MCP and then discover the grant.
- 🔴 **`TutorAI` has 19 authors historically and 2 in 2026.** A student organisation's bench rotates. **Fork, pin, and budget for maintaining the retrieval layer yourself** — do not sell it as vendor-backed.
- 🟡 **`anthropic.com` appears on 171 of `canvas-mcp`'s commits.** That is tool-written authorship, not a vendor relationship, and it is not a support channel. **Read the bench as 30 authors with heavy agent assistance.**
- 🔴 **The service account is the security boundary and clients will push back on it.** An MCP server with an instructor's own token inherits everything that instructor can see across every course they teach. **Scope it per engagement or the first incident is a FERPA conversation.**

### 🟢 Where it sells, by region

- 🟢 **North America** — both widest-bench connectors are NA-placed and point at Canvas and Brightspace. **Oklahoma / Maryland / Idaho SB 1227** all ask for human oversight; step 5 *is* the oversight, with an audit record. **California AB 1159**: nothing in this stack trains on student data.
- 🟢 **EMEA** — ship inside the window to **2027-12-02** so Art. 14 oversight is the architecture rather than a retrofit; **Art. 50 transparency applies today**, so the tutor announces itself. 🔴 **Do not add affect detection to this pattern in Europe: Art. 5(1)(f) prohibits emotion inference in education outright.** Cite Council conclusions **9003/26** for the sovereignty half and run inference on an EU-located model via `TutorAI`'s factory.
- 🟢 **APAC** — **India's CT & AI mandate (Classes 3–8, from 2026-27)** makes this a **teacher-enablement** sale: `agent-skills` plus `agent_learning`'s eval harness, measured against the CBSE framework. **Japan and Korea** both ask for human responsibility in writing; step 5 answers both.
- 🟡 **LATAM** — the fit is the **UNESCO observatory** and **IDB** pilot estate (59% already using generative AI) and **teacher-facing** delivery, which is what HolonIQ measures the region's edtech actually building. **Design to LGPD Art. 20** (review of solely-automated decisions) from the start — which step 5 satisfies by construction.

---

## Pass 333 · 2026-10-20 — P28: the permissive LTI 1.3 seam, end to end, beside an LMS you never fork

### 🟢 P28 — District/university LMS integration on an all-permissive stack

🔵 **The problem this solves, and why it is worth a pattern:** every LMS engagement in this sector runs into the same wall — **the platform tier is copyleft (Moodle GPL-3.0, Chamilo GPL-2.0, Gibbon GPL-3.0, ILIAS GPL-3.0, OpenEduCat LGPL-3.0)** and a client's legal review stops the work. 🟢 **The answer is that you do not need the platform's licence at all: LTI 1.3 is a standards boundary, and everything on YOUR side of it can be permissive.** **p333 is the first pass where this KB can name every component of that seam from a first-hand verified row.**

**Components — every grant read first-hand at `raw.githubusercontent.com`, bytes recorded:**

| Role | Component | Grant | Activity, first-hand |
|---|---|---|---|
| LTI 1.3 Advantage surface (launch, AGS, NRPS, Deep Linking, Dynamic Registration) | [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) | 🟢 **MIT**, 1,077 B | 346 c · 6 a · head 2026-10-19 (p331) |
| OIDC relying party, server | [`yetanalytics/pedestal-oidc`](https://github.com/yetanalytics/pedestal-oidc) | 🟢 **Apache-2.0**, 11,357 B | 123 c · 5 a · head 2026-10-16 (p333) |
| OIDC, browser | [`yetanalytics/re-oidc`](https://github.com/yetanalytics/re-oidc) | 🟢 **Apache-2.0**, 11,357 B | 70 c · 4 a · head 2026-10-16 (p333) |
| xAPI learning record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0**, 11,357 B | verified p333 |
| Tutoring agent behind the launch | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | head 2026-10-19 (p330) |
| ITS state + review scheduling over MCP | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, 1,073 B | 467 c · 5 a (p330) |
| 🔴 **Licence gate in CI** | [`google/licenseclassifier`](https://github.com/google/licenseclassifier) | 🟢 **Apache-2.0**, 11,358 B | 249 c · 30 a (p333) |

**Wiring:**

```
Moodle / Canvas / Open edX          ← NEVER FORKED. Reached only across the LTI 1.3 boundary.
        │  LTI 1.3 launch (an OIDC auth flow)
        ▼
  lti-tool (MIT) ──────── pedestal-oidc (Apache-2.0)   server-side RP
        │                 re-oidc (Apache-2.0)         browser-side
        ▼
  tutor-mcp (MIT) ──► DeepTutor (Apache-2.0)           the pedagogy
        │
        ▼  xAPI statements
  lrsql (Apache-2.0)                                   the record store
        │
        ▼
  AGS score write-back ──► back across the LTI boundary into the LMS gradebook
```

🟢 **Why the whole thing holds together commercially:** `lti-tool`'s dependency surface is **two packages (`zod`, `jose`)** and its storage is pluggable (`postgresql`, `mysql`, `dynamodb`, `d1`+`hono`) — so the same pattern serves a conventional district deployment and an edge one. **Three of the seven components come from two houses that ship (Yet Analytics; Longsight commits to `lti-tool`), not from lone authors.**

🔴 **The step that is NOT optional, and it is new this pass.** Put **`licenseclassifier` in CI as a gate over the dependency tree**, not as a one-off review. 🔵 **The reason is measured, in this repository, this pass: the substring licence check that every cheap pipeline uses graded 610 rows wrong here, and 7 of the corrections were GPL/AGPL projects sitting in the corpus marked permissive — `tooljet/tooljet` among them.** **A pattern that recommends permissive components and does not gate the transitive closure is recommending a snapshot, not a property.**

**Estimate:** 6–8 weeks to a working LTI 1.3 launch with score write-back and an LRS behind it, on this stack, for one LMS. 🔴 **Add a week if the client's legal review has not seen an LTI-boundary argument before** — that conversation, not the code, is the long pole.

---

**Pass 332 · 2026-10-20.** **One new recipe, `P27`, and it is the first pattern in this file that puts a studio's own code INSIDE the content layer rather than beside it.** 🟢 **It exists because p332 measured something the H5P row on these shelves had been understating: the content types are MIT while the renderer is GPL-3.0, so the fork boundary is a tier lower than this file has been drawing it.**

### P8 — The grant-legibility pass: read the payload yourself before you scope the attachment point (LATAM public sector first, then any non-English estate) — NEW at p341

**Trigger:** an engagement over an estate whose repositories are **not** US/UK-origin — a Brazilian or Spanish-speaking municipal or ministry stack, a Japanese or Korean university platform — or any estate where a licence scanner has returned `unknown`, `no license found`, or a family that disagrees with the repository's own sidebar. 🔴 **Measured basis: of 208 payloads on these shelves, 3 are non-English and ALL THREE return no family from the shared scanner; one of them is `AGPL-3.0` and read as `no-family-no-restriction`.**

**Why it is a pattern and not a checklist item.** A scanner's silence on a licence is indistinguishable from a permissive grant *in the direction that costs money*, and the two findings that justify this recipe are both silent failures: a **Portuguese AGPL-3.0** read as unclassified, and a **"Community License"** whose body recites MIT verbatim read as MIT.

**Wiring:**
1. **Enumerate the tree, not a path ladder.** `git clone --depth 1 --filter=blob:none --no-checkout` then `git ls-tree -r HEAD`. 🔴 One grant in 208 on these shelves lives at **`docs/License.txt`**, and a root-only ladder publishes that repository as ungranted — it has been wrongly refused twice in this base's history.
2. **Resolve the default branch; never assume `main`.** `git ls-remote --symref`. 🔴 Measured here: `frappe/education`'s payload is on **`develop`**, `portabilis/i-diario`'s on **`1.6`**, `portabilis/i-educar`'s on **`2.12`**. A `curl` of `main/LICENSE` returns 404 on all three.
3. **Vary the path by case.** 6 of 208 grants sit at `license.txt`, `license.md`, `LICENCE.md` or `docs/License.txt`. Reuse `lib/probe_payload.sh` — it generates the ladder; do not retype it.
4. **Read the TITLE LINE as its own channel, separately from the body.** This is the step that catches the expensive class. `caviraoss/pagelm` → title **"PageLM Community License"**, body **MIT word for word**, plus commercial-use and SaaS restrictions. 🟢 `make bespoke-census PAYLOADS="..."` types each payload `SPDX-TITLED` / `BESPOKE-TITLED` / `UNTITLED` and flags the rows a human must read.
5. **Do not treat a non-English payload as unlicensed.** Match the licence's own title in the local language — `LICENÇA PÚBLICA GERAL AFFERO GNU` is AGPL-3.0; `LICENCIA PÚBLICA GENERAL` is GPL. 🔴 This step has no instrument in this KB yet and is the open half of T31; do it by hand and record the reading.
6. **Record the CHANNEL of the grant, not only its value** (`ACTION ZD`, p335). A family read from a 19-byte `License: GNU GPL V3` declaration is a *pointer*, not a grant text — right answer, weaker evidence — and a client's legal review will ask which it was.
7. **Price the halves of a stack separately.** 🔴 The worked instance: `portabilis/i-educar` (SIS core) is **GPL-2.0** and `portabilis/i-diario` (teacher-facing portal) is **AGPL-3.0**. **§13's network reach attaches to the teacher-facing half — the half an agent attaches to.** Pick the attachment point *after* this step, not before.

**Components (all read first-hand at p341):**
- `lib/probe_payload.sh` + `lib/fetch_payload_to_file.sh` — the located-payload loop, byte-exact sizing, symref branch resolution
- `compose/code/p341-bespoke-instrument-census` — the title-form classifier and `gate-bespoke-title` (34 offline controls)
- `compose/code/pass257-restriction-scan` — the unscoped restriction vocabulary, 11 languages on the restriction axis
- `compose/code/lib/license_family.sh` — the family classifier that **does** know `ECL-2.0` and `CC-BY-4.0`

**Deliverable:** a per-repository row carrying *family · path · branch · bytes · title form · grant channel*, plus a named list of the rows a human read and what they concluded. 🟢 **On this corpus that list was 16 of 208 (7.7 %) — small enough to be read by a person in an afternoon, and that is the point of measuring it rather than escalating everything.**

**Honest limits.** A payload answers the **copyright** question only; whether a system may be *called* lives in its Terms of Use and is invisible to every step above (`P26`). 🟡 And step 5 is manual: this KB has no multilingual family vocabulary, which is exactly the gap T31 names.

## P27 — A custom interactive content type, forked under MIT, generated by an agent, delivered through the client's existing copyleft LMS

🟢 **The problem it solves.** A client on Moodle or Open edX wants an interaction their LMS does not have — a domain-specific simulation, a branching clinical scenario, a code-tracing exercise with real evaluation. 🔴 **The standing advice on these shelves has been to generate H5P content JSON and leave the renderer alone, which keeps GPL contained and limits the studio to the interactions H5P already ships.** 🟢 **p332's census shows that limit was a measurement artefact, not a licence constraint.**

### 🟢 The grant boundary, measured first-hand p332 — this is what makes the pattern legal

**Every cell from [`evidence/p332-h5p-grant-channels.2026-10-20-p332.tsv`](../evidence/p332-h5p-grant-channels.2026-10-20-p332.tsv). 🔴 Note the channel column: 8 of 10 H5P repositories have NO licence file, so a file-first audit will tell you this pattern is impossible.**

| piece | repo | grant, and the channel that answered | what you do with it |
|---|---|---|---|
| renderer | `h5p/h5p-php-library` | 🔴 **GPL-3.0** — `LICENSE.txt` **and** `composer.json` agree | 🔴 **Deploy unmodified.** Containment is the whole strategy |
| editor core | `h5p/h5p-editor-php-library` | 🔴 **GPL-3.0** — `composer.json` | 🔴 Deploy unmodified |
| 🟢 **the fork base** | `h5p/h5p-interactive-video` | 🟢 **MIT** — *no licence file*; `package.json` **and** the full MIT text in the README | 🟢 **FORK AND MODIFY.** 2,447 c · 115 a · head 2026-10-02 — the most active, most broadly authored repo in the org |
| alternative fork bases | `h5p/h5p-course-presentation`, `h5p/h5p-drag-question` | 🟢 **MIT** — `package.json` | 🟢 Fork. Pick by interaction shape |
| `h5p/h5p-accordion` | | 🟢 **MIT** — real `LICENSE.txt`, 1,073 B, *© 2015 Joubel* | 🟢 Fork. **The one content type whose grant a file-first audit will find** |
| 🟡 read the README first | `h5p-question-set`, `h5p-multi-choice`, `h5p-blanks` | 🟡 **MIT, in the README body and nowhere else** | 🟡 Fork, and **copy that README text into the engagement's own licence file** |
| 🔴 do not touch | `h5p/h5p-core` | 🔴 **No grant on any of the three channels** (README is 14 bytes) | 🔴 Out of scope until the holder answers |

🔵 **Why `h5p-accordion` is worth naming even though it is the least capable base: it proves the MIT tier is the holder's intent rather than manifest drift.** One content type carries a real MIT file under *Joubel*'s copyright — the house behind H5P. **The other MIT content types are the same grant, published less carefully.**

### 🟢 The wiring, piece by piece

```
  [ authoring agent ]                         DeepTutor (Apache-2.0) or a direct LLM call
         |  emits H5P content JSON conforming to YOUR forked semantics
         v
  [ your forked content type ]  <--- MIT, your code, your client's branding, your interaction
         |  h5p-interactive-video fork + a new semantics.json + your JS
         v
  [ H5P renderer, UNTOUCHED ]   <--- GPL-3.0, deployed as a dependency, never patched
         |
         v
  [ LTI 1.3 tool ]              <--- lti-tool / @lti-tool/core (MIT), or Cvmcosta/ltijs (Apache-2.0)
         |  Launch + Deep Linking to place the activity, AGS to write the grade back
         v
  [ client LMS ]                <--- Moodle (GPL-3.0) / Open edX (AGPL-3.0), deployed as-is
         ^
         |  human-approval hop before any grade is final
  [ P26's approval gate ]       <--- required wherever Annex III pt 3 / Art. 14 or a US state rule applies
```

🟢 **The licence argument in one sentence a client's counsel can check:** *your* code is the forked content type, **MIT**; the **GPL-3.0** renderer and the **GPL/AGPL** LMS are deployed unmodified as dependencies, so no copyleft obligation reaches the studio's work product; the LTI layer that joins them is **MIT or Apache-2.0**.

### 🟢 The pieces, with their measured provenance

| layer | choice | grant | measured |
|---|---|---|---|
| LMS integration | `lti-tool/lti-tool` (`@lti-tool/core`) | 🟢 MIT, 1,077 B | 346 c · 6 a · head 2026-10-19, release 2026-10-20 (p331) |
| LMS integration, mature | `Cvmcosta/ltijs` | 🟢 Apache-2.0, 11,361 B | 575 c · 17 a (p331) — 🟡 only 2 distinct authors in 2026 |
| content fork base | `h5p/h5p-interactive-video` | 🟢 MIT (manifest + README) | 2,447 c · 115 a · head 2026-10-02 (p332) |
| renderer | `h5p/h5p-php-library` | 🔴 GPL-3.0 | unmodified dependency |
| authoring agent | `HKUDS/DeepTutor` | 🟢 Apache-2.0 | head 2026-10-19 (p330) |
| pedagogy / mastery | `CAHLR/OATutor` | 🟢 MIT | 1,045 c · 27 a (p330) — BKT, UC Berkeley |
| curriculum spine | `withmarbleapp/os-taxonomy` | 🟡 **ODbL-1.0 + CC BY-SA 4.0** | 23 c · 3 a (p331) — 🔴 **data, not code: the share-alike reaches your derived taxonomy** |
| approval gate | `P26`, this file | — | four jurisdictions |

### 🔴 What will go wrong, named in advance

1. 🔴 **A procurement audit will report your fork as unlicensed.** Seven of the eight H5P grants are invisible to a `LICENSE`-file scanner. 🟢 **Mitigation, and do it on day one: commit a `LICENSE` file into your fork carrying the MIT text your base published in its README or manifest, and cite the upstream channel in the commit message.** You are not changing the grant; you are publishing it where an auditor looks.
2. 🔴 **H5P's grant is per repository and the org is not uniform.** 🟢 Read the specific content type. Never write "H5P is MIT" in a client document.
3. 🔴 **`h5p-core` has no grant on any channel.** If your fork's dependency graph reaches it, stop.
4. 🟡 **The GPL renderer must stay a dependency, not a patch.** The moment someone fixes a renderer bug in-tree, the containment argument is gone. **Pin it, upstream the fix, and keep the fork boundary in CI.**
5. 🟡 **`os-taxonomy` is ODbL + CC BY-SA.** Share-alike on data is not share-alike on code, and it reaches a derived taxonomy. Keep it at arm's length or accept the obligation knowingly.

### 🟢 Shape of the engagement

**6–8 weeks.** Weeks 1–2: fork base selection and the licence-provenance commit (item 1 above is the first deliverable, not the last); the LTI 1.3 launch + Deep Linking seam against the client's real LMS. Weeks 3–5: the content type itself — `semantics.json`, the interaction, and the agent's JSON contract against it. Weeks 6–7: AGS grade write-back with `P26`'s approval hop. Week 8: the procurement pack — grant per dependency, **with the channel that answered beside each one.**

🔵 **One honest limit on this pattern, because it is not the LMS-replacement story a client may want to hear.** It puts studio-owned MIT code inside the content layer of a platform the client already runs. 🔴 **It does not make the platform permissive** — tenth consecutive pass with no permissive education LMS or SIS (`verticals/solutions.md` p332). **The permissive surface in this sector is the layers, never the base, and `P27` is the deepest layer this KB can currently show a studio how to own.**

---

**Pass 331 · 2026-10-20.** **One new recipe, P26, and two amendments to standing patterns.** 🟢 **P26 is the first pattern in this file whose compliance argument is the same in four jurisdictions on three continents** — it is the architectural form of Trend 20 — **and every component in it was measured alive on two channels on 2026-10-20.** 🔴 **The amendments correct a dependency this file has named since p319 and that is dead on both channels.**

## P26 — Graded assessment that writes to the client's gradebook, with the human-approval hop in the protocol

🟢 **The problem it solves is regulatory and architectural at once.** Four jurisdictions — **Vietnam (Decision 33/2026/QĐ-TTg, effective 2026-08-15), Oklahoma and Maryland, the EU (Annex III pt 3 + Art. 14, 2027-12-02) and Korea (AI Basic Act, in force 2026-01-22)** — all draw their high-risk line at **automated assessment whose output stands alone without meaningful human review.** 🟢 **So build the review hop into the protocol rather than into a policy document, and the same deployment is compliant in all four.**

### The stack — every row MIT, Apache-2.0 or BSD-3, every row measured alive p331

| layer | repo / package | grant, first-hand | liveness, first-hand p331 |
|---|---|---|---|
| **LMS integration** | [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) · `@lti-tool/core` | 🟢 **MIT**, 1,077 B | 346 c · 6 a · 2026-10-19 · 🟢 **release 1.3.1, 2026-10-20** |
| **autograder (notebooks)** | `nbgrader` | 🟢 **BSD-3-Clause** | 🟢 **0.9.6 — 2026-09-30** |
| **autograder (alt.)** | `otter-grader` | 🟢 **BSD-3-Clause** | 🟢 **7.0.0 — 2026-07-27** |
| **integrity / plagiarism** | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) · `@dodona/dolos` | 🟢 **MIT** | 🟢 **2.10.0 — 2026-10-19** |
| **tutor / hint state** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, 1,073 B | 467 c · 5 a · 2026-10-16 |
| **pedagogy evaluation** | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | 🟡 **MIT code**; corpora **CC BY-NC-SA 4.0** | 289 c (p327) |

### The wiring, concretely

1. **Launch.** The tool is an `@lti-tool/core` LTI 1.3 tool. Register it against the client's Moodle / Canvas / Open edX with **Dynamic Registration** (`services/dynamicRegistration.service.ts`) rather than by hand — it is the difference between a one-click install and a ticket to the LMS admin. Pick the storage adapter from `packages/`: **`postgresql`** or **`mysql`** on-premise, **`dynamodb`** or **`d1` + `hono`** if the client wants it at the edge.
2. **Roster.** Read the cohort from **NRPS** (`services/nrps.service.ts`, `schemas/lti13/nrps/contextMembership.schema.ts`). 🟢 **Never ask the institution to export a CSV of students** — NRPS is the answer to the data-protection question before it is asked, and under **California AB 1159** it matters that the roster is read, used and not retained for training.
3. **Collect and grade.** Submissions run through **`nbgrader`** or **`otter-grader`** in a sandbox. 🔴 **This is the step that is high-risk in all four jurisdictions, and it stays out of the high-risk class only because of step 5.**
4. **Integrity.** **`@dodona/dolos`** runs similarity over the submission set. 🟢 **Report it as evidence to a human, never as a verdict** — an automated plagiarism finding that stands alone is the clearest example of the thing every one of the four instruments prohibits.
5. 🟢 **The human hop — this is the pattern.** The machine score and the Dolos signal land in a **review queue**, not in the gradebook. An instructor approves, overrides or returns each one. **Only on approval does the tool call AGS** (`schemas/lti13/ags/scoreSubmission.schema.ts`) to write the score. 🟢 **The approval identity and timestamp are logged beside the submission.**
6. **Feedback.** Hints and next-step guidance come from **`tutor-mcp`**, which holds learner state and review scheduling. Grade the *feedback* with **`learning-commons-org/evaluators`** — its Feedback family scores revision actionability, student-response specificity and 🟢 **withholding answers**, which is the property a tutor must have and an LLM does not have by default.

### Why the compliance argument is one argument and not four

| jurisdiction | what it asks | where P26 answers it |
|---|---|---|
| 🟢 **Vietnam** — Decision 33 entry 2 | Is the AI output the **sole basis** for the official outcome? | **No — step 5.** The official outcome is the instructor's approval |
| 🟢 **Oklahoma / Maryland** | Human oversight; no AI decision on high-stakes outcomes | **Step 5**, with an audit record |
| 🟢 **EU** — Annex III pt 3, Art. 14 | Effective human oversight of a high-risk system | **Step 5**; the AGS call is the documented control point |
| 🟡 **Korea** — AI Basic Act | Human-oversight duties on high-impact education AI | **Step 5** |
| 🟢 **California AB 1159** | Student data must not train models | **Step 2 + 3.** Roster read via NRPS, nothing retained for training |
| 🟢 **NYC** — K-8 student-facing moratorium | No student-facing AI through grade 8 | 🟢 **Deploy teacher-facing only: steps 1–5 need no student surface** |

🔵 **The reusable insight: the oversight hop is not a compliance tax, it is a protocol feature that already exists.** **LTI AGS was designed so that a tool writes a score deliberately. Putting a human in front of that call costs one queue and turns four regulatory regimes into one architecture.**

🔴 **Cost honestly stated: the review queue is the whole build.** Steps 1–4 and 6 are integration of maintained libraries; step 5 is UI, state and an audit log, and it is where the estimate goes. 🔴 **And `Gap 316(i)` — the real wiring cost of the agent-to-LTI hop — remains the highest-value unmeasured number on this shelf.** **P26 does not close it. It names the place it should be measured once.**

## Amendments to standing patterns (p331)

🔴 **Every pattern in this file that reaches an LMS through `pylti1.3` must be re-cut.** `pylti1.3` is **dead on both channels — last commit 2022-11-21, last PyPI release `PyLTI1p3` 2.0.0 on 2022-11-20.** 🟢 **Substitute `@lti-tool/core` (MIT) for new builds, or `ltijs` (Apache-2.0, `ltijs` 7.0.7 of 2026-10-06) where a longer track record is required.** 🟡 **If the client's stack is Python and must stay Python, that is now an open problem this KB cannot solve with a maintained permissive library — say so in the bid rather than pinning a 2022 commit.**

🟡 **P4 (EU) — the date metadata, not the conclusion.** The Annex III education deadline stands at **2027-12-02**. 🟡 **But this pass's sources give Reg. (EU) 2026/1744 an OJ publication of 2026-07-24 and entry into force of 2026-07-27, against the 2026-07-08 recorded in `intel/policy-matrix.tsv`.** 🔴 **Two new Art. 5 prohibitions phase in 2026-12-02 — six weeks out — and emotion inference in educational settings is the limb this sector touches.** **P4 should lead with that date, not with 2027.**

---


# Compose patterns — education

**Pass 327 · 2026-10-19.** **Eleven recipes. P14 is new and it is the first pattern in this file
whose three layers all come from one vendor** — the pre-wired K-12 stack (standards data over MCP +
Apache-2.0 teacher skills + MIT evaluators), with the Gated/Open boundary drawn as an architecture
decision rather than a licence footnote. **Every repo it names had its licence read first-hand at
p327.**

**P11 gains `dodona-edu/dolos`** (MIT, Ghent University, 3,838 commits) as the integrity engine
with a maintaining university behind it — previously this pattern named only `JPlag` and `jieplag`.
**P10 Variant A gains a model-selection gate**: `AI-for-Education/pedagogy-benchmark` (MIT, 1,143
questions from Chile's teacher-qualification exams, 920 CDPK + 223 SEND) answers "which model, in
Spanish, for teachers" with a number. **P5 gains `open-edge-platform/education-ai-suite`**
(Apache-2.0, Intel, OpenVINO, CPU/iGPU/NPU) as the on-device inference layer beside Kolibri.
**P3 and P6 gain `autolab/Autolab`** (Apache-2.0, CMU, 2,179 commits) and
`datakind/student-success-tool` (MIT, John Jay College CUSP, Google.org, 3,015 commits) as the two
US-institution-deployed artefacts for autograding and retention evidence.

**Pass 319 · 2026-10-19.** Ten recipes. Every repo named below is in `agents/top.md`,
`repos/foundations.md` or `verticals/solutions.md`, with the pass in which it was read first-hand
recorded there. Timings are engagement estimates, not measurements.

**Changes this pass. P10 is new and it is the most defensible pattern in this file**: the verified
curriculum spine, built on Brazil's `bncc-dev` stack, with a published number behind it — curriculum
hallucination **31.9% ungrounded, 2.3% when the model queries the verified dataset over MCP**. It
comes with a port variant for India, where the same artefact does not exist and a 2026-27 mandate
is arriving without it.

**P1 gains a "prove it teaches" stage**, because the evaluation layer this KB declared missing for
four passes now exists and its finding is that **LLM-judged helpfulness is not a pedagogy signal**
(`agents/top.md`). **P7 gains a per-pupil opt-out, an approval queue and a decision log**, which US
statute has turned from nice-to-have into bid-qualifying. **P5 gains two more permissive offline
components.** And the cross-cutting LTI risk now has a real alternative rather than an index —
`tsugiproject/tsugi`, Apache-2.0, 4,011 commits.

Carried from pass 317: **P8** — the permissive-LMS build on OpenOLAT (Apache-2.0), the first
pattern in this KB that does *not* require an LTI boundary. **P1 gains a FERPA-filtered retrieval
step.** **P4 gains the 2026-12-02 watermarking date and ports to South Korea**, whose Framework Act
on AI has been in force since 2026-01-22. **Every pattern now carries the `pylti1.3` concentration
risk explicitly** — one 138-star, single-maintainer MIT library is the seam in seven of eight
recipes, and that belongs in the SOW.

---

## P25 — The LTI boundary as its own service: shipping a Python agent into a Canvas or Moodle tenancy now that the Python LTI library is dead — NEW in p330

**The problem this solves, and it was invisible until this pass measured it.** Every tutor, grader and classroom agent in this KB is Python or TypeScript, and every North American district engagement ends at the same sentence: *"it has to launch from Canvas and write to the gradebook."* 🔴 **This KB has answered that for eleven passes by pointing at `dmitry-viskov/pylti1.3`.** 🔴 **Measured first-hand at p330 across every ref: 178 commits, 16 authors, and no commit on any branch or tag since `2022-11-21`. Its last substantive commit is *"Support Python 3.11"*. The other permissive Python option, `openfun/django-lti-toolbox`, died `2024-11-14`.** 🟢 **The fix is not to find a third Python library — there isn't one. It is to stop putting the LTI boundary in the agent's language.**

### The stack, with grants read first-hand and activity measured first-hand (p330)

| layer | repo | grant | activity (p330) | role, and why this one |
|---|---|---|---|---|
| **LTI boundary — PHP route** | `tsugiproject/tsugi` | 🟢 **Apache-2.0** | 🟢 **4,012 commits · 47 authors · last 2026-10-19 · 486 commits in 2026** | The launch, the AGS writeback, the NRPS roster and Deep Linking. 🟢 **Verified from the tree, not the README** (`lib/src/Util/LTI13.php`, `ims/ags/route.php`, `lib/src/Controllers/Ims/Nrps.php`, `DeepLinkRequest.php`) **with unit tests** (`lib/tests/Util/LTI13Test.php`). Handles **LTI 1.1 as well** — its own commit of 2026-10-18. 🟡 Three authors in 2026 |
| **LTI boundary — TS route** | `Liberate-Labs/ltikit-sdk` | 🟢 **MIT**, `main/LICENSE` 1,063 B | 🟡 **38 commits · 1 author · last 2026-07-10** | Same surface, serverless/edge: `packages/core/src/{ags,nrps,deep-linking}.ts`, **each with its own `.test.ts`**; Dynamic Registration; **cookieless launches (Platform Storage)**; adapters for memory, Prisma, Redis, Supabase. 🔴 **Fork and pin** — last three `main` commits are an ownership handover, seven dependabot branches unmerged |
| **The agent** | `ArnaudGuiovanna/tutor-mcp` | 🟢 **MIT** | 🟢 **467 commits · 5 authors · last 2026-10-16** | The deterministic pedagogy engine: skill graph, BKT, FSRS, prerequisite rules. Speaks **MCP**, knows nothing about LTI |
| **or the chassis** | `eai6/ai-tutor` | 🟢 **MIT**, 1,090 B | **787 commits · 4 authors · 2026-08-20** | When the engagement needs the whole Django tutor — 5E phases, mastery gating, `apps/safety/` consent and audit |
| **Autograding (optional)** | `Gchism94/jupyterquest` | 🟢 **MIT**, 1,070 B | 🟡 **249 commits · 3 authors · 2026-05-07** | `.ipynb` autograding where the mark must be defensible: CI, Codecov, **Zenodo DOI `10.5281/zenodo.10784348`**. **North America** (`gchism@arizona.edu`) |
| **Legacy courseware (optional)** | `jcputney/scorm-again` | 🟢 **MIT** | 🟢 **1,243 commits · 14 authors · last 2026-10-20** | The SCORM 1.2 / 2004 route into installed courseware that LTI does not reach |

### The wiring, concretely

```
Canvas / Moodle tenancy
        │  LTI 1.3 launch (OIDC, platform JWKS, state+nonce)
        ▼
┌─────────────────────────────────────────────┐
│  BOUNDARY SERVICE  — tsugi (PHP) or ltikit (TS)  │
│   · validates the launch, resolves the user      │
│   · NRPS → roster                                │
│   · Deep Linking → placement                     │
│   · AGS → writes the score back                  │
│   · mints a short-lived internal token           │
└───────────────┬─────────────────────────────┘
                │  internal HTTP + MCP — NO LTI beyond this line
                ▼
        tutor-mcp  /  eai6-ai-tutor  /  jupyterquest
        (Python, knows only: user id, course id, role, callback)
```

**Four rules make this work, and each one is the answer to a mistake this KB has seen in a real repository:**

1. 🟢 **The boundary speaks LTI and nothing else speaks LTI.** The agent receives a resolved identity (user, course, role, grade callback) over internal HTTP. **This is what makes the dead-library problem survivable: when the boundary library rots, you replace one service, not the product.**
2. 🔴 **Write the grade over AGS, from the boundary.** `ictinnovations/moodle-mod_ictexam` (🔴 GPL-3.0, read first-hand p330) is the cautionary case: its README *requires* AGS and NRPS to be enabled on the LTI preset, and then returns the mark through **`classes/external/set_grade.php`, a vendor-specific Moodle web service**. 🔵 **That works and it is not portable** — it binds the product to Moodle at the one point LTI exists to keep portable. **Use the standard path you already enabled.**
3. 🟡 **Pin the boundary by commit, and budget maintenance for it.** Neither option is a dependency you can forget: Tsugi is 486 commits a year from **three** people; LTIkit is **one** author and is between owners. **Price six to ten days a year against the boundary service in the bid; it is still an order of magnitude cheaper than owning an LTI implementation.**
4. 🔴 **Do not put copyleft inside the boundary.** `adamzammit/LTIPlugin` (GPL-3.0) and `artcc/freelingo` (AGPL-3.0, §13 reaching hosted users) are readable references, **not components of a hosted deliverable.**

### What this is worth, and where it sells

🟢 **North America, highest value.** This is the region where the LMS *is* the integration point and where **cooperative purchasing** (p329) makes the integration the reusable asset — win one district, become buyable by every member, and the boundary service is what carries across. 🔵 **A proposal that names the library, shows the 2022 commit date, and prices the boundary explicitly is doing diligence the incumbent vendor has not.**

🟡 **EMEA, second.** Universities buying through **GÉANT OCRE** (p329) ask the sustainability question directly, and a boundary service with 47 contributors behind it answers it better than a library with none. 🔴 **Declare the accessibility gap in the same breath** — nothing in this KB remediates *course content* for WCAG 2.2 AA inside an LMS, and the European Accessibility Act makes that the buyer's liability, not the vendor's.

🔴 **APAC, usually not.** The region's strongest artefacts — OpenMAIC, DeepTutor, Rumi, Shiksha Copilot — deploy *beside* institutional systems or as national programmes, not inside a Canvas tenancy. **Reach for P15 or P14 there and skip this boundary entirely; the integration debt is the thing APAC engagements do not have.**

### 🔴 What was not verified, stated plainly

**Neither boundary option was run against a live LMS by this pass.** Tsugi's LTI 1.3 surface is established **from the shipped tree and its unit tests**; LTIkit's is established from its tree plus **its author's claim** of live verification against Canvas and MoodleCloud, which this environment cannot corroborate — `github.com`, `api.github.com` and every non-allowlisted host are unreachable. 🟢 **Both grants are byte-verified and both activity triples are first-hand.** 🔴 **Budget a spike against the client's actual tenancy before committing to either route in a fixed-price scope: platform quirks in Canvas and Moodle are the part no repository can tell you about.**


## P23 — The enforceable help-level contract: instructor-set policy, tutor-side enforcement, and an evaluator that proves it held — NEW in p329

**The problem this solves, and it is the one that actually blocks faculty sign-off.** Every academic-integrity conversation ends at the
same question: *"how do I know it gave a hint and not the answer?"* 🔴 **Every tutor in this KB answers that with a promise in a
README.** `eai6/ai-tutor` hardcodes a **three-level hint ladder** and states the tutor never gives direct answers; the claim is
credible and **unverifiable**. 🟢 **p329 found the two missing halves — a way to make the help level *configurable by the instructor*,
and a way to *measure* whether it was respected — and all three layers are permissive.**

### The stack, with grants read first-hand and activity measured first-hand (p329)

| layer | repo | grant | activity (p329) | role, and why this one |
|---|---|---|---|---|
| **Chassis** | `eai6/ai-tutor` | 🟢 **MIT**, 1,090 B | **787 commits · 4 authors · last 2026-08-20** | The production-shaped Django tutor: **5E phase tag on every `LessonStep`**, five step types, skill-graph with **prerequisite mastery gating**, 35-MCQ bank (10 sampled, 8/10 to pass), and `apps/safety/` shipping **`ConsentRecord` (incl. `parental`, `withdrawn_at`)** + **`SafetyAuditLog`** with pseudonymised `user_hash`. 🔴 **Two months stale — fork it, own it** |
| **Policy surface** | `DanielG0798/CourseGuide-AI` | 🟢 **MIT**, 1,068 B | **9 commits · 2 authors · 2026-09-16→21** | 🟡 **A 9-commit course prototype — VENDOR THE DESIGN, NOT THE DEPENDENCY.** What to take: an **instructor-defined policy** (*allowed help levels, approved sources, style constraints*), an **assistance-kind classifier** (*concept · hint · setup check · next step · analogy*), a **progressively limited** response, an MCP server over stdio, and `tests/m2/test_cases.yaml` as the shape of the fixture set |
| **Proof** | `learning-commons-org/evaluators` | 🟡 **Code MIT** · prompts CC BY 4.0 · 🔴 **CLEAR + PERSUADE 2.0 corpora CC BY-NC-SA 4.0** | **289 commits · 13 authors · last 2026-10-19** | 🟢 **The closing piece, and it is almost too neat: one of its seven Feedback evaluators is literally *"withholding answers"*.** Also *revision actionability*, *student-response specificity*, *tone appropriateness*, plus 8 Text Complexity evaluators for grade-level fit. `pip install learning-commons-evaluators` / `npm install @learning-commons/evaluators` |
| **Authoring** | `anthropics/k12-teacher-skills` **or** `learning-commons-org/agent-skills` | 🟢 **Apache-2.0**, 10,173 B | **4 commits · 3 authors · last 2026-10-13** / **42 · 6 · 2026-10-06** | Teacher-facing authoring of the policy. 🔵 **Take `agent-skills` when the policy must be tied to a curriculum spine over MCP; take `k12-teacher-skills` when it rides a prompt** |
| **Integrity evidence** | `dodona-edu/dolos` | 🟢 **MIT**, 1,083 B | 🟢 **3,859 commits · 25 authors · last 2026-10-19** | Similarity evidence for a human reviewer, per **P11** — never a verdict. **The most alive foundation in this KB** |

### The wiring, concretely

1. **Declare the contract as data, not as a prompt.** One policy document per course or assignment: `allowed_help_levels`,
   `approved_sources`, `style_constraints`. **Store it beside `ai-tutor`'s `LessonStep`, keyed to the same `course`/`assignment`
   identifier**, so the policy is versioned with the curriculum rather than living in a system prompt.
2. **Enforce it where the hint ladder already is.** `ai-tutor`'s three-level ladder becomes the *mechanism*; the policy becomes its
   *bound*. Classify the incoming request by assistance kind (CourseGuide-AI's five categories), then **clamp the ladder to the level
   the policy permits** and let mastery gating stay as it is.
3. 🟢 **Score every response that ships, with the evaluator the contract names.** Run `evaluators`' **withholding answers** over
   sampled tutor turns in CI, with **Text Complexity** for grade-level fit. **This converts "it gives hints, we promise" into a
   per-release number**, and the number is the artefact a faculty senate signs off on.
4. **Keep the corpora out of the deliverable.** 🔴 **Ship the evaluators and their prompts; do NOT ship *CLEAR* or
   *PERSUADE 2.0* (CC BY-NC-SA 4.0) and do not use them to validate a commercial release.** Re-annotate against client data, or
   validate in-house and keep the corpus out of what you hand over.
5. **Attach the consent and audit layer that already exists.** `ai-tutor`'s `ConsentRecord` / `SafetyAuditLog` satisfy the P4 and P9
   procurement questions; **consent withdrawal is already modelled as a first-class timestamped event with `parental` as its own type.**

### What this is worth, and where it sells

🟢 **The deliverable is not a tutor — it is a *tutor plus a measured guarantee about what it refuses to do*, and the guarantee is the
thing nobody else bids.** **EMEA:** the measurement is directly reusable as Annex III evidence of human-oversight design ahead of
**2027-12-02**, and it is procurable through **GÉANT OCRE** by direct award (p329). **North America:** *human oversight* and *no
high-stakes AI decisions* are already statute in Oklahoma, Maryland, Idaho and Virginia — a per-release withholding score is
compliance evidence, and cooperative purchasing (**Sourcewell / OMNIA / NASPO ValuePoint**) makes one win orderable by every member
district. **LATAM:** pair with `AI-for-Education/pedagogy-benchmark` (MIT, 1,143 questions from Chile's teacher-qualification exams)
and scope the bid to **ChileCompra Directive No. 44/2026**.

🔴 **Build estimate and the honest risks.** **8–10 weeks.** Two of the five layers are prototypes or stale: **CourseGuide-AI is 9
commits — reimplement its design rather than importing it**, and **`ai-tutor` has not moved since 2026-08-20, so forking means
owning it**. 🟡 **The classifier is the technical risk** — CourseGuide-AI's own README says its classification *"uses a simple keyword
tool; nuanced prompts may be mislabeled"* — **so the assistance-kind classifier is the component to rebuild properly and the one to
put the fixture suite around.**

## P24 — Vehicle-first engagement shaping: find the contract route before designing the solution — NEW in p329

🔴 **The failure this prevents is the most expensive one in public-sector education work: a technically excellent proposal with no
contractual route to being bought.** 🟢 **p329 established that the unit of market access is the procurement vehicle, not the vendor
landscape** (`intel/trends.md` trend 13). **This pattern is the operational form of that finding: establish the vehicle in week one,
and let it constrain the architecture — not the reverse.**

| region | the route | what it constrains in the build |
|---|---|---|
| **EMEA** | 🟢 **GÉANT OCRE 2024** — **2025-02-03 → 2030-02**, 39 countries, IaaS/PaaS/SaaS, **direct award** available | **Package the work as a SERVICE an eligible institution can direct-award**, not as a product needing its own tender. Favours hosted/managed shapes over licence sales |
| **EMEA (UK)** | **DfE "AI Tutoring Tools for Education"** — ~£1.5M ex VAT, contract **2026-06 → 2028-05**, Find a Tender **014992-2026** / **013464-2026**; plus **Crescent Purchasing Consortium** (2026-02, SEND lot naming AI adaptive testing) | **Pre-tender market engagement is the window to influence the spec.** Build the **curriculum-alignment** and **safeguarding** evidence early — those are what a DfE-reviewed framework screens on |
| **North America** | **Cooperative purchasing** — `Sourcewell`, `OMNIA Partners`, `NASPO ValuePoint`; also **791 Purchasing Cooperative RFP `791202603005`**; **California Ed Tech JPA RFP 25/26-01** (pre-vetted **portfolio**, not winner-take-all) | 🟢 **Design for ONE solicitation and many orderers:** per-district configuration without per-district engineering. **Multi-tenancy is a procurement requirement here, not an architecture preference** |
| **LATAM** | **ChileCompra Directive No. 44/2026** via **Mercado Público**; **Brazil PBIA** buyers = **MCTI, MEC, federal universities, SENAI/SENAC**; portals **PNCP** / **Mercado Público** / 🔴 **CompraNet frozen at 2022, only Nuevo León live** | **Score against the Directive's own criteria.** 🔴 **Do not promise federal Mexican tender monitoring — the data does not exist.** Mexico is state-level or it is fiction |
| **APAC** | 🔴 **No vehicle found.** China's *AI Plus Education* buying is expected at **provincial / municipal bureau** level, 2026–2027 | **Target a province, not a ministry.** 🟡 **Go per-country next (`MOE Singapore`, `MEXT`, `AusTender`, `GeM India`) — "APAC" is not a procurement jurisdiction** |

### The procedure, and the one rule that matters

1. **Week one: name the vehicle, its dates and its eligibility rule.** If you cannot name it, the engagement has no route and that is
   the first finding to deliver, not a detail to resolve later.
2. **Confirm it at source before it enters a bid.** 🔴 **Every vehicle above is SEARCH-CHANNEL-ONLY in this KB — all sixteen
   procurement hosts tested in p329 answered `403` at CONNECT or `000`.** **Each row carries a notice ID precisely so confirmation is
   one lookup on the buyer's own portal.**
3. **Let the vehicle pick the shape.** Direct-award framework → sell a service. Cooperative → sell configurable multi-tenancy.
   Directive-governed tender → sell against the published scoring criteria.
4. **Then pick the stack**, from **P23** for tutoring with an enforceable help contract, **P11** for integrity evidence, **P4** for the
   EU AI Act provider package.
5. 🔵 **Check the policy gate separately, and do not confuse the two.** Trend 2 (*procurement is policy-gated*) and trend 13 (*the
   vehicle*) **fail differently: clear the policy gate with no vehicle and you are compliant and unbuyable; find the vehicle and miss
   the gate and you are disqualified on review.**

## P15 — The ministry tutor you fork instead of build: MIT reference implementation + standards spine + pedagogy benchmark — NEW in p328

🟢 **What changed at p328, and it is the reason this pattern replaces most of P1's build phase.** `eai6/ai-tutor` is **MIT** (`main/LICENSE` and `master/LICENSE`, both 1,090 B, *"Copyright (c) 2026 World Bank Group and contributors"*) and it already ships, **in code read first-hand this pass**, the four things every tutor engagement in this KB has quoted as build work: **5E-structured lesson steps, prerequisite mastery gating over an auto-built skill graph, a specified exit-ticket assessment, and a GDPR consent + audit layer.** 🔵 **This pattern is therefore a *fork, localise and prove* engagement, not a greenfield one — which is a materially different proposal to put in front of a ministry.**

**Fits:** a national or sub-national ministry, a district consortium, or a development-finance-funded programme. **Region:** written for **EMEA** (the reference deployment is Seychelles) with **LATAM** and **APAC** variants below. **Shape:** 10–14 weeks to a provable pilot.

### The components, each with its grant read first-hand at p328

| layer | component | grant | why this one |
|---|---|---|---|
| **tutor core** | `eai6/ai-tutor` | 🟢 **MIT**, 1,090 B | Django 6.0.2, seven apps. **The fork base.** `apps/{accounts,curriculum,tutoring,dashboard,llm,media_library,safety}` all verified as real files |
| **curriculum spine** | `withmarbleapp/os-taxonomy` | **ODbL-1.0** + CC BY-SA 4.0 | **1,591 topics, 3,225 prerequisite edges, 3,261 standards from seven national curricula.** 🟢 ODbL: a *produced work* stays yours — see P13 for the boundary |
| **spine, national variant** | `bncc-dev` (Brazil, CC BY 4.0) · `cn-math-taxonomy` (🔴 **CC BY-NC — cannot ship**) | per-row | Use when the client's mandate names a national framework |
| **curriculum validator** | `devissaputra/curriculum_knowledge_graph` | 🟢 **MIT**, 1,076 B | 8 entity types, 7 relation types, **invalid edges rejected**, cycle and coverage-gap detection, 36 passing tests. 🔴 **Take the validator, not its synthetic data** |
| **teacher workflow** | `learning-commons-org/agent-skills` (preferred) or `anthropics/k12-teacher-skills` | 🟢 **Apache-2.0**, 10,173 B | Four K-12 skills; the Learning Commons build is **grounded in the Knowledge Graph over MCP**, so it ties to the spine rather than to a prompt |
| **pedagogy evaluation** | `learning-commons-org/evaluators` | 🟡 code **MIT**; corpora **CC BY-NC-SA 4.0** | **19 evaluators in five families.** 🔴 **Ship the evaluators; never ship the CLEAR / PERSUADE 2.0 corpora** |
| **outcome benchmark** | `AI-for-Education/pedagogy-benchmark` | 🟢 **MIT**, 1,063 B | **1,143 real teacher-qualification-exam questions** (920 CDPK + 223 SEND). Chilean source exams → **the LATAM variant's native instrument** |
| **sovereign inference** | local **Ollama** (first-class in the fork) + `open-edge-platform/education-ai-suite` | 🟢 **Apache-2.0**, 11,350 B | Intel CPU/iGPU/NPU via OpenVINO. **"No student data leaves the building" is a config change, not a port** |
| **integrity, if assessed work counts** | `dodona-edu/dolos` | 🟢 **MIT**, 1,083 B | Ghent University. Wire per **P11** — sell the audit trail, never the verdict |

### How to wire it

**1. Fork and stand up the reference, unmodified (week 1).** `seed_seychelles` ships 7 geography + 8 mathematics units; **run it first and demo it before touching anything.** The README carries a *fork & deploy to your own Azure* walkthrough and a CI/CD workflow; the Docker path is there if the client is not on Azure. 🔵 **A working tutor in week 1 is what buys the other thirteen weeks.**

**2. Repoint the spine from the seed to the client's curriculum (weeks 2–4).** The ingest path is already the one a ministry has: **upload a curriculum PDF/DOCX → generated lesson steps, media, exit tickets and a skill map.** Then:
- Run the generated skill graph through **`curriculum_knowledge_graph`'s validator** before anyone teaches from it — it **rejects invalid relation semantics** (`LearningOutcome ──TEACHES→ Course` is refused) and detects **cycles, bottlenecks, disconnected entities and assessment-coverage gaps**. 🔴 **An auto-extracted prerequisite graph with a cycle in it will lock students out of lessons, and `ai-tutor` gates on exactly that graph.**
- Map topics to the client's standards via **`os-taxonomy`** where the national framework is one of its seven, or **`bncc-dev`** for Brazil.
- 🔴 **Before quoting standard text in anything, read `os-taxonomy`'s `PROVENANCE.md`:** four frameworks ship **codes-only** (`ngss-k5`, `ngss-ms`, `c3-social-studies`, `ib-pyp-pspe`), UK NC ships in full under **OGL v3**, Common Core ships in full under the **purpose-limited CCSS Public License**. **Topic→standard links survive everywhere; NGSS and IB prose cannot be redistributed.**

**3. Keep the pedagogy structural — do not let it collapse into a prompt (weeks 2–6).** The fork's value is that **5E is a phase tag on every `LessonStep`** and step types are a closed set (`teach`, `worked_example`, `practice`, `quiz`, `summary`). 🔵 **Localise the content inside that structure; resist the request to "just let the model freestyle in the client's language."** Keep the three-level hint ladder, the Socratic no-direct-answers constraint, the interleaved retrieval practice, and **remediation routed before an exit-ticket retake**. Tune the exit-ticket parameters (shipped: **35-MCQ bank, 10 sampled, 8/10 to pass**) with the client's assessment people, in writing.

**4. Wire the consent and audit layer to the client's actual legal basis (weeks 3–6). This is the stage that wins the procurement.** `apps/safety/models.py` already ships:
- `ConsentRecord` — `ConsentType` includes **`parental`**; `withdrawn_at` timestamp; `unique_together = ['user', 'consent_type']`, so consent state is unambiguous per user per purpose.
- `SafetyAuditLog` — **pseudonymised 16-char `user_hash`** (not the user id), `consent_given` / `consent_withdrawn` / content-flagging / rate-limiting / age-verification event types, a `severity` field, three composite indexes.
- Management commands **`export_user_data`**, **`delete_user_data`**, **`safety_cleanup`**.

🟢 **Map these to the instrument by region, and the mapping is the deliverable, not the code:** **EMEA** → GDPR Art. 6 lawful basis per `ConsentType`, Art. 15 access via `export_user_data`, Art. 17 erasure via `delete_user_data`; **plus EU AI Act Art. 4 (literacy) and Art. 50 (transparency)**, which 🔴 **are the obligations still on the near calendar — the Annex III high-risk regime is reported moved to 2027-12-02, so do not sell this as beating an August 2026 deadline** (see `intel/market.md`). **LATAM** → **Chile Ley 21.719, in force 2026-12-01**, roughly six weeks out. **North America** → Oklahoma **S.B. 1734** parent opt-out maps to `ConsentType.PARENTAL`; California **A.B. 1159**'s bar on training against student data is a model-config and DPA question, not a code one; Ohio's district policy mandate (deadline **2026-07-01, already past**) means the client's own adopted policy is your specification. **APAC** → **Korea's AI Basic Act**, in force 2026-01-22, education named high-impact, **grace period ≈12 months** — the remediation window.

**5. Prove it teaches, with two instruments, before scale (weeks 6–12). Non-negotiable.**
- **`evaluators`** on the tutor's output: the **Text Complexity** family for grade-level appropriateness, and the **Feedback** family — including the **withholding-answers** evaluator, which **directly measures the fork's own Socratic constraint.** 🟢 **That alignment is the strongest reason to pick this evaluator set over an LLM-as-judge rubric.**
- **`pedagogy-benchmark`** on the model stack: **1,143 real teacher-qualification-exam questions.** Report CDPK and **SEND** separately — **a tutor that scores well overall and badly on special educational needs is a tutor a ministry cannot deploy**, and this is the only instrument in the KB that separates them.
- 🔴 **Keep the CC BY-NC-SA corpora out of the deliverable.** Validate in-house, or re-annotate against client data. **The report may cite the scores; the package may not contain the annotated CLEAR or PERSUADE 2.0 corpora.**

**6. Sovereignty variant, if data cannot leave (any time).** Switch the `llm` app's per-purpose model config to **local Ollama** — already a first-class provider — and add **`education-ai-suite`** for Intel CPU/iGPU/NPU inference via OpenVINO. 🔵 **This is the only step in the pattern that is a configuration change rather than engineering work, and it is usually the step the client assumes is the hardest.**

### What to sell, in order

1. **Weeks 1–2 — the working demo on the client's own curriculum sample.** Flat fee. It is a fork, so this is real and cheap, and it reframes every later conversation.
2. **Weeks 2–6 — curriculum spine + validated skill graph.** The validator output (cycles, bottlenecks, assessment-coverage gaps) **is itself a finding the client has never had about their own curriculum** and is sellable even if the tutor is never deployed.
3. **Weeks 3–6 — the compliance package**, mapped to the client's named instrument. 🟢 **Highest margin, lowest build.**
4. **Weeks 6–12 — the measurement report** from `evaluators` + `pedagogy-benchmark`. **This is the renewal.**
5. **Then, and only then — scale and localisation.**

### 🔴 What was not verified, stated plainly

- **The World Bank affiliation is self-declared.** The copyright line and contributors list name the World Bank Group and its Education Team; **the repository sits in a personal namespace**, and `github.com`, `api.github.com` and `worldbank.org` were all unreachable this pass. **In a bid, say "MIT, with the World Bank Group on the copyright line." Do not say "a World Bank project."**
- **Stars, forks and commit counts are unobtainable** — the metadata channel answered 403 throughout. **Maturity here is argued from the shipped code and the README, both read first-hand, not from attention.**
- **The README's staging URL does not answer** (`000`). Evidence of intent to deploy, not of a live service.
- 🟡 **The announced Seychelles national programme appears to be a different stack** — a World Bank 2026 Annual Meetings transcript describes a **proprietary Grok** tutor. 🔵 **Treat that as the opening, not the objection: an MIT stack the ministry can audit, host and keep is the argument against a single-vendor proprietary tutor, and it is the argument this pattern exists to make.** 🔴 **The transcript's "5,000 schools / one million students" figure is not carried — Seychelles' population is under 150,000, so it belongs to another country in the same session.**
- **The EU AI Act postponement (Reg. (EU) 2026/1744) is from secondary legal commentary and is NOT first-hand.** **Verify on EUR-Lex before step 4's EMEA mapping goes into a client document.**

## P14 — The pre-wired K-12 stack: one vendor, three layers, and the Gated boundary as an architecture decision — NEW in p327

**Region: North America** (the data tier is US state standards). **Ports to any region for the
agent and evaluation tiers only — see *Portability* below.**

🔵 **Why this pattern exists.** Every pattern in this file from P1 onward assembles three layers by
hand: a curriculum spine, an agent that acts on it, and something that judges the output. **P14 is
the first time all three ship from one vendor with permissive code**, which changes the engagement
from *build the stack* to *integrate it and own the boundary*. 🔴 **That makes the licence boundary
the deliverable, because it is the only part the vendor has not already solved.**

### The three layers, each licence read first-hand at p327

| layer | artefact | licence | what it contributes |
|---|---|---|---|
| **Data** | `learning-commons-org/knowledge-graph` (161 ★, v1.15.0 of 2026-10-14) | 🟡 **MIT code; data per dataset *and per download*** — Open (CC BY 4.0 / CC0), Open + Gated, Gated | US academic standards by state · **state↔CCSS crosswalks with a `jaccard` score** · Math + ELA learning components · Math Coherence Map · **Eedi Misconceptions Graph** · WIDA ELD · XQ Competencies · Carnegie Skills Progressions |
| **Agent** | `learning-commons-org/agent-skills` (40 ★) and `anthropics/k12-teacher-skills` (575 ★) | 🟢 **Apache-2.0** both; `NOTICE` names **Anthropic, PBC** and **Learning Commons** | Four teacher workflows: lesson-plan creation · lesson differentiation (below / at / above proficiency) · lesson prep · **check for understanding, with distractors drawn from documented misconceptions** |
| **Evaluation** | `learning-commons-org/evaluators` (86 ★, 289 commits) | 🟡 **Code MIT · prompts + settings CC BY 4.0 · annotated corpora CC BY-NC-SA 4.0** | **19 evaluators**: text complexity (8), feedback (7, incl. **withholding answers**), graphics (2, early access), math standards alignment, critical thinking. Python + TypeScript SDKs |

### How to wire it

**1 — Stand up the data tier, pinned.** Take the **Open** datasets only. Two access routes, and
pick deliberately:

```shell
# MCP, for an agent runtime
claude mcp add --transport http learning-commons-kg \
  https://kg.mcp.learningcommons.org/mcp \
  --header "Authorization: Bearer $LC_API_KEY"
```

🔴 **Pin the version.** The repo tags releases and ships `.release-please-manifest.json`
(`{".": "1.15.0"}` at the time of this pass). **The vendor publishes its own regressions and they
are the silent kind:** v1.10.1 restored Texas↔CCSS math crosswalks *"incorrectly removed in
v1.9.0"* and told consumers to re-download; v1.13.1 restored a `jaccard` property *"unintentionally
removed in v1.12.0"*; v1.14.0 fixed four states' standards whose `inLanguage` claimed Spanish for
English text. 🟢 **Build against a pinned tag, diff the `CHANGELOG.md` before bumping, and treat a
spine bump as a release gate — not a dependency update.**

🔴 **And the trap that is documented but easy to miss:** v1.12.0 states that newly added standards
frameworks are **not yet aligned to learning components**, so *every* learning-component→standard
alignment still points at the superseded framework. **If your tutor resolves a standard to its
components, assert `isCurrent` on the framework and fail loudly rather than silently serving a
deprecated alignment.**

**2 — Install the skills, then fork them.** `npx skills add learning-commons-org/agent-skills`, or
the plugin route for the Anthropic companion:

```shell
git clone https://github.com/anthropics/k12-teacher-skills
claude plugin marketplace add ./k12-teacher-skills
claude plugin install k12-education@k12-teacher-skills
```

🟢 **Apache-2.0 on both, so forking is clean and patent-granted.** 🔵 **Fork rather than consume:
the four skills are written against the vendor's connector, and a client engagement almost always
needs a fifth skill and a different curriculum binding.** Keep the `NOTICE` attribution — Apache-2.0
requires it and the co-development credit is the part a client's counsel will check.

**3 — Make the evaluators the acceptance gate, not a report.** Install
`pip install learning-commons-evaluators` (or the npm package) and run the relevant family on every
generated artefact **before a teacher sees it**. 🟢 **The pairing that makes this defensible: the
skills ship their own `evals/` rubrics for pedagogy, rigor, formatting and model scaffolding, and
`evaluators` supplies the learning-science dimensions. Run both — the vendor's rubric for
"did the skill do its job" and the evaluator for "is this fit for a child of this grade."**

🔴 **The hard stop, and it is the whole reason this stage needs engineering.** The **expert-annotated
CLEAR and PERSUADE 2.0 corpora are CC BY-NC-SA 4.0.** You may ship the evaluators and their
prompts in a paid product; you may **not** ship those corpora, and you may not use them to validate
a commercial model release. 🟢 **So the billable, defensible work is re-annotating against the
client's own materials** — which also produces a better gate, because the thresholds end up
calibrated to the district's actual reading levels rather than to a research corpus.

**4 — Draw the Gated line before scoping, not during delivery.** Classify every content
requirement in the statement of work:

| requirement | tier | what it costs |
|---|---|---|
| Standards, crosswalks, learning components, misconceptions, progressions | 🟢 **Open** (CC BY 4.0 / CC0) | Attribution only — **to each original source, not to the distributor** |
| IM® v.360 **scope and sequence** | 🟢 **Open** | Attribution |
| IM® v.360 **instructional** or **assessment materials** | 🔴 **Gated** | **Publisher approval + separate agreement.** A line item and a lead time |
| **OpenSciEd** curriculum | 🔴 **Gated** | Same |
| **Learner Variability Navigator** (math / literacy models) | 🔴 **Gated** | Same |

🔴 **The clause to put in front of counsel, quoted from `LICENSE.md`:** compiling datasets into your
own build means you *"take on the licensing and attribution obligations of every dataset and
download you include,"* and the distributor's role *"doesn't consolidate those into a single license
for your build."* 🟢 **Never export the whole graph and label the result CC BY 4.0. Carry per-source
attribution, and keep an Open-only build target in CI so a Gated dataset cannot leak into a
deliverable by accident.**

**5 — Add the layers the vendor does not ship.** 🔴 **None of the three repositories touches
compliance, and in North America K-12 that is the bid-qualifying part.** Bring in, unchanged:
**P7** (grade-band gating, teacher-only mode, parent consent as state with an approval queue and a
decision log), **P9** (the COPPA disclosure boundary), **P3** (the policy-gated deployment layer).
🔵 **Add `autolab/Autolab`** (Apache-2.0, CMU) **where the engagement needs assessment *execution***
— so the agent advises and a deterministic grader adjudicates, which is the only arrangement that
survives a "did AI grade my child" question.

### What to sell, in order

1. **The Open/Gated classification of the client's content requirements** — a two-week audit that
   de-risks the whole programme and is sellable on its own.
2. **The pinned-spine release gate** — version pinning, `CHANGELOG` diffing, `isCurrent` assertion
   and a loud failure on deprecated alignments. 🟢 **Sold as correctness engineering, which it is.**
3. **Re-annotation of the evaluation corpus against client materials** — the lawful route to a
   commercial-grade acceptance gate.
4. **The fifth skill** — whatever workflow the client has that the four shipped skills do not.
5. **The compliance layer** (P7 + P9 + P3), which the vendor stack leaves entirely open.

### Portability

🟢 **The architecture ports everywhere. The data tier does not.** `agent-skills`, the Anthropic
companion and `evaluators` are jurisdiction-neutral — Apache-2.0 and MIT code, rebindable to any
spine. 🔴 **The Knowledge Graph data tier is US state standards and CCSS crosswalks: it does not
port to EMEA, APAC or LATAM.** Substitute the regional spine and keep the other two layers:

- **LATAM** → `bncc-dev` for Brazil (**P10 Variant A**), with
  `AI-for-Education/pedagogy-benchmark` as the model-selection gate. 🔴 **Re-annotate the
  evaluators for Spanish/Portuguese — the shipped rubrics are English and ELA-centric.**
- **EMEA** → 🔴 **no commercially usable national-curriculum graph exists in this KB for any
  European state.** Use `withmarbleapp/os-taxonomy` (ODbL + CC BY-SA, UK NC 2013 in full under OGL
  v3) via **P13**, and pair with OpenOLAT (Apache-2.0) for a **fully permissive** stack with no
  copyleft seam. Add `dodona-edu/dolos` (MIT, Ghent) for integrity per **P11**.
- **APAC** → `THU-MAIC/OpenMAIC` (MIT, 41.1k ★) for the multi-agent classroom shell, or
  `microsoft/Shiksha-Copilot` (MIT, MSR India + Sikshana) and `Orenda-Project/rumi-platform`
  (Apache-2.0, Taleemabad, Pakistan) where a named national deployment is the requirement.
  Add `open-edge-platform/education-ai-suite` (Apache-2.0, Intel/OpenVINO) for on-device per **P5**.

### 🔴 What was not verified, stated plainly

**The per-dataset licence labels and access tiers above are read from the repository's own
`README.md` and `LICENSE.md` at p327.** The authoritative download-level terms live on
`docs.learningcommons.org` and `platform.learningcommons.org`, and **the network policy answered
403 to CONNECT for both**, so **no dataset record count is asserted here and no download was
fetched.** 🔵 **Before this pattern enters a signed scope, pin the download-level terms from the
catalog pages — the Open/Gated split is the commercial hinge of the whole pattern and it deserves a
first-hand read.**

## P13 — The share-alike data boundary: shipping a proprietary product on an ODbL dataset — NEW in p326

**For:** every engagement in which the most valuable asset is **someone else's data under a
share-alike licence** — ODbL, CC BY-SA, ODC-BY — and the client intends to keep their product
proprietary. In this industry that is now the default case, not the exception: the sector's
largest open curriculum graph is **ODbL-1.0 + CC BY-SA 4.0**, and the usual reflex — *"share-alike,
so we can't use it"* — **is wrong and costs the client the best asset on the shelf.**

**The legal fact the whole pattern rests on.** ODbL binds a **derivative database**, not a
**produced work**. Modify the dataset → your modified dataset must be published under ODbL. Use
the dataset inside a product, a model or an application → **the product is yours.** CC BY-SA
covers the authored *text* in the same release on the same logic. **So the obligation is not
"open-source your tutor." It is "if you improve the graph, publish the improved graph."**

**Which turns a legal question into an architecture question — and it has a reference
implementation.** `tbh-23/Homestead` (**MIT**, 15 ★, 41 commits) ships this boundary:

**Wiring**
1. **Never vendor the dataset.** No copy in the repository, no copy in the container image, no
   copy in the deployment artefact. Homestead's README says so explicitly and its server enforces
   it. **A dataset committed into your tree is the single fact that makes the boundary arguable.**
2. **Fetch it at runtime from upstream, into a cache outside the repository**, pinned to a commit.
   Homestead caches under a private path and serves it to the browser from there.
3. **Verify on fetch.** Check the published SHA-256 per file; if the dataset ships no checksums,
   compute and store your own at pin time. A silent curriculum change is a correctness incident.
4. **Diff on refresh and surface the delta.** Homestead **notifies the user when topics are added
   or removed upstream** rather than absorbing the change invisibly. Do the same: an operator must
   see a curriculum move.
5. **Keep client-specific work in an overlay, keyed by the upstream ID — never as an edit to the
   graph.** Extra topics, re-banded ages, jurisdiction mappings, proprietary difficulty estimates
   all live in your own table joined on `topicId`. 🔵 **This is the commercial hinge of the whole
   pattern:** an overlay is a produced work and stays the client's; an in-place edit produces a
   derivative database and must be published.
6. **Carry the attribution, exactly as specified.** ODbL and CC BY-SA both require it and the
   upstream release gives the string to use. Put it in the product's about screen and in the data
   documentation — not only in a source file nobody renders.
7. **Audit the third-party layer separately.** A share-alike dataset can legitimately contain
   material the publisher could not relicense. In `os-taxonomy` four of seven curricula ship
   **codes only** and Common Core stays under its own purpose-limited licence. **Your product's
   rights posture is the union of the licences inside the dataset, not the licence on the
   dataset.**

**What to tell the client, in one sentence each.**
- **Private edtech:** *"We can build on it, you keep your product, and the only thing you owe back
  is changes to the public graph — which is why we are putting your changes in an overlay."*
- **Public sector or ministry:** *"Your jurisdiction extension becomes a public asset published
  under your name."* 🟢 **Lead with this; it is usually the thing they wanted anyway and could not
  justify paying for.**
- **Either:** *"The dataset ships checksums and we pin them. Your curriculum cannot change under
  your tutor without someone being told."*

**What this pattern does not do.** It does not clear **trademark** (NGSS is a WestEd mark with a
sample-approval requirement for commercial use), it does not clear **purpose-limited** upstream
licences (the CCSS Public License), and it does not make an **NC** dataset usable — `cn-math-
taxonomy` (CC BY-NC) and K12-KGraph's data (CC BY-NC-SA) stay out of client work no matter how
the code is arranged. **Share-alike is an architecture problem. NonCommercial is a wall.**

**Estimate:** 3–5 days of engineering inside any pattern that consumes external data, and it has
to be designed in at the start — **retrofitting a vendored dataset out of a shipped product is a
much worse week.**

---
## P12 — The measured-outcome public-school pilot: buy the evidence design, not the code — NEW in p325

**The problem this solves.** Every education bid ends at the same question — *does it actually
teach?* — and p323 established that the sector's usual answer (an LLM judge scoring helpfulness) is
the wrong instrument, while p319's own favourite example published judged scores about itself.
**This KB now holds exactly one artefact with a real classroom answer, and it cannot be used:**
`JustinoLM/STI-matematicas` (Universidad Tecnológica de Panamá) — **74 students, three sixth-grade
sections of a Panamanian public school, 710 practice sessions, pre→post 1.83 → 2.56 of 8,
Wilcoxon p = 0.0012, r = 0.41, SUS 70.1** — and **no licence file at all** (seven filenames probed
across five branch names), project finished, infrastructure decommissioned.

🟢 **So take its *design* and run it on components that are licensed.** This pattern is the
measurement protocol plus the permissive stack that can carry it. **It is the only pattern here
whose deliverable is a number rather than a system** — the system is a means to the number.

### What to wire, and why each piece

| role | component | licence | why this one |
|---|---|---|---|
| **pedagogy decision layer** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | Skill graph + **BKT** + **FSRS** + prerequisite rules behind MCP, SQLite local / PostgreSQL hosted. The mastery decision is **deterministic and inspectable** — the model never decides whether the learner has mastered anything |
| **hint ladder** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT | Read its hint sequencing, and mirror Panama's three rungs: *general strategy → step-by-step → a model-generated hint that points at the committed error without revealing the answer*. **The third rung is the only generative one** |
| **event capture** | [`openfun/ralph`](https://github.com/openfun/ralph) | MIT | xAPI **LRS** to the ADL standard, from a national public operator. **Install it before the tutor, not after** — a pre/post claim needs an event history that predates the intervention, or there is nothing to measure against |
| **teacher dashboard** | [`openfun/potsie`](https://github.com/openfun/potsie) | MIT | Grafana **dashboards-as-code** (Jsonnet/grafonnet) over the LRS. Reviewable in a pull request, on infrastructure a ministry already runs |
| **retention scheduling** | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | If you need FSRS outside `tutor-mcp`'s implementation |
| **enrolment / certificates** *(optional)* | [`openfun/joanie`](https://github.com/openfun/joanie) | MIT | Headless education ERP, when the pilot has to issue anything a learner keeps |
| **leakage check** | [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | MIT | Pre-registered audit of whether a helpfulness judge rewards handing over the answer. **Run it against your own prompt before the pilot**, not after |
| **pedagogical capability of the model** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🟡 CC BY / CC BY-SA (contradictory — see `agents/top.md`) | The one peer-reviewed benchmark that scores pedagogy **with a trained reward model against real teacher utterances rather than an LLM judge** |
| **calibration** *(optional)* | [`yjo2lee/knowsim`](https://github.com/yjo2lee/knowsim) | MIT | A learner simulator with a **known** knowledge state, for checking the tutor's confidence against what the learner actually knows |

🔴 **Not in the stack, deliberately:** `JustinoLM/STI-matematicas` itself (no grant),
`braivo/braivo` and `avps82/mentar` (**AGPL-3.0** — fine to run, fatal to link into client code),
and any artefact whose only quality evidence is a self-reported judged score.

### The privacy boundary — copy this verbatim, it is the first ministry question

Panama's design is the cheapest defensible answer this KB has read, and **four of its five controls
cost nothing**:

1. **No student data in the repository, ever** — the validation data was never published.
2. **Argon2** password hashing only.
3. **Server-verified admin token** for administrative functions; **teachers scoped to their own
   groups within their own school.**
4. 🟢 **Prompts leave with anonymous placeholders substituted server-side — never student names.**
   This is the control to put on the slide: it decouples *which model you call* from *what the model
   learns about a child*. Panama's system calls **DeepSeek** from a public primary school on that
   basis.
5. **Grade-band gating and teacher-only modes** where the jurisdiction requires them (**P7**, **P9**).

🔵 **Why this matters commercially: it converts the sovereignty objection into an engineering
line item.** A buyer who believes they must have a sovereign model has an expensive problem; a buyer
who needs *no identifiers to cross the boundary* has a middleware problem. Offer the sovereign path
too (`compose` **P4**, **P21** — GWDG / AcademicCloud in the EU), but price the placeholder boundary
first.

### The measurement protocol — the actual deliverable

**Stage 1 — instrument and baseline (2–3 weeks, before any AI is deployed).**
Build an **8-item pre-test** per target skill, administered on paper or in the LMS, and stand up
`ralph` so that baseline behaviour is already being recorded. Register the analysis **before data
collection**: the primary outcome, the test, the effect-size measure and the exclusion rule. The two
pre-registered audits in this KB (`conv-vs-ped-tutor`, `ability-levels-audit`) are the template, and
p323's finding is why it matters — **difference-in-differences on a bounded rating scale can
manufacture an effect from nothing.**

**Stage 2 — the pilot (6–10 weeks).** Panama's scale is the realistic floor and it was enough for
significance: **three class sections, ~74 learners, ~700 sessions.** Keep per-session events in the
LRS, not in application logs.

**Stage 3 — analysis, exactly this.**
- Pre→post on the 8-item instrument, **paired**, reported as a mean change with n stated.
- **Wilcoxon signed-rank** (not a t-test — these are bounded small-integer scores), with the
  **effect size r** alongside the p-value. Panama: *p = 0.0012, r = 0.41 (medium)*.
- **SUS** for perceived usability, n stated separately (learners who finished the survey ≠ learners
  who practised). Panama: *70.1 / 100*.
- Engagement as a **denominator-honest** figure: *65 of 74 completed at least one practice*, not
  "74 students used it".

**Stage 4 — the disclosure that makes the rest credible.** 🟢 **State the limit in the deliverable,
in one sentence, before anyone asks:** *without a control group the improvement cannot be attributed
to the system alone.* **Panama's README says exactly that, and it is why its numbers are worth
quoting at all.** Then offer the fix as the next phase: **a waitlist or stepped-wedge control** —
sections receive the system in sequence, so every class gets it and attribution becomes possible.
**That is the second engagement, and it is an easier sell after an honest first one.**

### What to sell, in order

1. **Stage 1 alone is billable** — instrument design, pre-registration and an LRS that works is a
   complete piece of work, and the client owns it whatever the pilot shows.
2. **The pilot.** Deterministic mastery, three-rung hints, placeholder boundary, dashboards-as-code.
3. **The attributable study.** Stepped-wedge, the number a ministry can act on.

🔴 **The risk to name in the proposal, because it is real: the pilot may show nothing.** A medium
effect from one school is the *good* case here. **Price Stages 1 and 2 so that a null result is
still a delivered engagement** — an instrumented school, a reviewable dashboard, a pre-registered
protocol and a permissive stack are assets regardless — and **never contract on an uplift target.**
Every vendor in this sector promises one; p323's evidence is that most of those promises are
measured with the wrong instrument.

### Portability

**LATAM first** — the Panama precedent, Spanish-language, public-school, and `repos/foundations.md`
now carries a pt-BR enablement track (`LucasSpinola/assistentes-educacionais-com-ia`) for the
knowledge-transfer line item. **EMEA next**, where the same stack is the public operator's own
software (**P21**, **P22**) and the EU AI Act's high-risk duties for assessment make a
pre-registered evidence file an asset rather than an overhead. **APAC as a build**, where
`muhammedalakbarli/imparo`'s 154-skill graph and `wwlwgo/cn-primary-math-knowledge-graph` show what
expressing a national curriculum costs.

## P11 — The academic-integrity evidence chain: sell the audit trail, never the verdict — NEW in p324

**Why this pattern exists now.** For seven passes this KB told studio leads there was no credible
open source in this category and to sell process evidence instead. **The first half of that was a
query artefact** (`intel/trends.md` trend 9, retracted in p324) — the components exist, three of
them measured first-hand this pass, and two are permissive. **The second half was right**, and it
is the design constraint of this pattern: every component here produces **evidence for a human
reviewer**, and nothing in it emits an authorship verdict.

**The stack, named repo by repo, with the licence posture each one forces.**

| # | stage | repo | licence | how it wires in |
|---|---|---|---|---|
| 1 | **Process evidence** (the foundation, already in this KB) | `jupyter/nbgrader`, `ucbds-infra/otter-grader`, `jupyterhub/jupyterhub` | BSD-3-Clause / BSD-3-Clause / BSD-3-Clause | **Deploy first and unchanged.** Submission history, execution provenance and per-cell autograding are the only artefacts in the chain that evidence *how* the work was produced. If a client will fund one stage, fund this one |
| 2 | **Prose, citation and stylometric signals** | `sunilgentyala/aegis-integrity` | **MIT** | `pip install "aegis-integrity[ml]"`, then run it **as an MCP server** — seven tools, of which `aegis_check_citations` and `aegis_analyze_paper` are the two to expose first. Pass `offline=true` by default; enable Crossref only with the client's written sign-off, and note in the DPIA that **reference metadata leaves the machine and the document never does** |
| 3 | **Text similarity against the institution's own corpus** | `NoplagLabs/noplag-engine` | **Apache-2.0** | `docker compose up` with PostgreSQL; load the institution's prior submissions through `POST /v1/corpus/documents`; call `POST /v1/checks` and read character-range matches from `/v1/checks/{id}/report`. 🔴 **Put an auth proxy in front of it on day one** — *"the API ships with no authentication"* |
| 4 | **Code similarity and collusion** (any CS, data or bootcamp engagement) | `jplag/JPlag` | 🟡 **GPL-3.0** | **Service boundary, never linked.** Run it as its own container exposing one HTTP endpoint; call it from the orchestrator. Twenty-odd languages, Java API or CLI, and its report viewer is local — *"No data will leave your computer!"* Substitute `thu-cs-lab/jieplag` (**MIT**, Rust) when the client's constraint is GPL avoidance rather than language coverage |
| 5 | **Orchestration and the review UI** | your code, plus the review-UI shape from `openeduhub/metadata-agent-canvas` | — | The canvas pattern this KB recorded in p322 is **exactly** the right interaction here: each signal shown with a **confidence badge**, inline annotation by the reviewer, and an **explicit confirm step** before anything is recorded. Reuse the interaction design; the repository's own grant is unverified, so do not depend on its code |
| 6 | **Calibration test before go-live** | `yjo2lee/knowsim` (MIT) for assistant-side calibration; the two pre-registered audits (`bydeng01/*`, MIT) for the measurement discipline | MIT | Run the "prove it teaches" discipline from p323 against *this* product too: pre-register what a positive finding means, freeze the evaluation set, log decisions |

**The wiring, in one sentence:** stage 1 runs continuously in the LMS; stages 2–4 run per
submission behind one orchestrator that **fans out and merges signals into a single reviewer
packet**; stage 5 is the only place a human decision is recorded; stage 6 gates the launch.

🔴 **The four rules that keep this sellable.**

1. **No verdict, ever.** Mirror `aegis-integrity`'s own language in the product copy: *"Results
   are a supporting signal for human review, not a determination of misconduct."* A client asking
   for an AI-authorship score is asking for the one thing the literature does not support.
2. **Do not ship the AI-text score as a finding.** Use it, if at all, as an internal triage
   ordering that the reviewer never sees as a number. `aegis-integrity`'s own README warns
   *"Do not treat AEGIS as having solved ESL false positives"*, and its changelog records an ESL
   multiplier that was **inverted** in an earlier release. **In any engagement with a
   second-language cohort — most of LATAM and much of EMEA and APAC — this stage is the fairness
   exposure, and the mitigation is not shipping its output.**
3. **Two licence boundaries, both structural.** JPlag is GPL-3.0 → separate process, HTTP only.
   `noplag-engine` is the **open core of a hosted product** → pin the version, read the diff on
   upgrade, and expect the roadmap to favour the hosted side.
4. **State the corpus limit in the proposal.** Both similarity engines match **only against what
   you load**. *"Plagiarism detection is corpus-based, not a live web/database crawl"* — a client
   expecting web-wide coverage is expecting the commercial product, and that expectation has to
   die in the sales conversation rather than in the pilot.

**Effort, measured against what is being assembled rather than guessed:** stages 1 and 3 are
deployment and data loading; stage 4 is a container and one endpoint; stage 2 is configuration plus
the DPIA conversation; stage 5 is the only real build. **The honest shape is 6–8 weeks for stages
1–4 plus a reviewer UI, and the long pole is the client's data-protection sign-off on stage 2, not
the code.**

**Where it sells, by region:** see `intel/market.md` under *Opportunities by region* — North
America on the human-oversight statutes, EMEA on the AI Act's high-risk assessment duties, APAC on
Vietnam's *"sole basis … without meaningful human review"* carve-out, LATAM on the 87%-use /
26%-strategy gap and the research-integrity remit of its university sector.

## P21 — The EU public-sector OER tutor: integrate the copyleft platform, own the permissive edges

**When to propose it.** A European public-sector or publicly funded education buyer — ministry,
federal state, national OER portal, university consortium — that already runs a content repository
and wants an AI tutor over it, under AI Act scrutiny and, increasingly, with a stated preference
for inference that stays in national or academic infrastructure.

**Why this recipe and not a fork.** Everything in the reference stack was read first-hand at p321,
and the licences do not permit the obvious move. The two layers with real engineering are
**`edu-sharing` (GPL-3.0, 16,110 commits)** and **`oeh-search-etl` (no licence file, 1,397
commits)**. The three permissive artefacts are a **dataset** and two **prototypes**. So the
architecture is forced, and that is a feature: it keeps Globant's deliverable on the permissive side
of the line.

**The wiring, named repo by named repo.**

1. **Leave the repository platform alone and talk to it over HTTP.**
   `edu-sharing/edu-sharing-community-repository` (**GPL-3.0**) stays a deployed service — either the
   client's existing instance or a stock install. **Do not link its code.** `openeduhub/tutor-chatbot`
   demonstrates the integration surface: the edu-sharing / WLO REST API, in its case
   `https://www.wirlernenonline.de/api/v1`. This is the same posture this KB takes on Moodle and
   OpenOLAT, so the copyleft question never reaches the deliverable.

2. **Take the competency model as data, from `openeduhub/oeh-metadata-vocabs` (CC0-1.0, 938
   commits).** SKOS/Turtle at `w3id.org/openeduhub/vocabs`: educational context, level, discipline,
   school type, rights and cost, machine-readable quality criteria, and **DigCompEdu, ESCO skills
   and EQF/DQR**. CC0 means no attribution condition — load it and move on. **This replaces the
   bespoke skill-taxonomy work that otherwise opens every one of these engagements**, and because
   the vocabularies are the ones the platform already annotates against, your tutor's skill graph
   and the client's content metadata share a vocabulary by construction rather than by mapping.

3. **Put the deterministic pedagogy in `tutor-mcp` (MIT), not in the prompt.** Skill graph, BKT,
   FSRS, prerequisite rules and narrative memory behind MCP, keyed to the vocabulary URIs from
   step 2. The vocabulary supplies the node identities; `tutor-mcp` supplies the mastery state and
   the decision about what to teach next. `agents/top.md` carries the row.

4. **Ground answers in the client's own content, not the open web.** `HKUDS/LightRAG` (MIT) over the
   material the platform returns for the learner's current objective. `tutor-chatbot`'s pattern is
   worth copying exactly here: **extract the learning metadata from the learner's question first,
   query the repository API with it, then attach the retrieved materials to the answer as direct
   links filtered by subject, content type and source** — so every claim carries a provenance link
   back into the client's repository. That is what makes the output defensible to an inspector.

5. **Make the inference provider pluggable from day one.** `tutor-chatbot` offers **OpenAI or GWDG**;
   `ki-prompt-benchmark` adds **AcademicCloud**. Build the same seam. For a publicly funded EU buyer
   this is no longer a nice-to-have — see the p321 trend in `intel/trends.md`.

6. **Ship the evaluation harness as part of the deliverable, modelled on
   `openeduhub/ki-prompt-benchmark` (Apache-2.0).** Judge-scored comparison of the current prompt
   against a candidate on **five criteria, 1–10, with a named winner and a written rationale**, plus
   generation time and token cost per provider, feedback accumulated across runs into a regenerated
   prompt per field. **It is three commits — take the design and build it properly.** Pair it with
   `AITutor-EvalKit` (MIT) if the buyer wants a teaching-quality measure rather than a
   metadata-quality one.

7. **Add `pylti1.3` (MIT) only if the tutor must appear inside an LMS**, and keep the AI Act posture
   from `intel/market.md`: Article 50 transparency has applied since `2026-08-02`, so the tutor
   discloses that it is an AI in the learner-facing surface, and anything touching admissions,
   assessment or learning-path steering is Annex III high-risk from `2027-12-02`.

**What the client ends up owning.** A permissively licensed tutor, a permissively licensed
evaluation harness, a CC0 competency model, and an HTTP integration against a GPL-3.0 platform they
already run. **Nothing in the deliverable is copyleft and nothing depends on an unlicensed
repository** — which is the whole reason the recipe is shaped this way.

**The honest caveat.** Steps 1, 2 and 7 rest on artefacts with 16,110, 938 and 178 commits. Steps 5
and 6 rest on prototypes of 10 and 3 commits, and step 6's reference exports to a schema
(`mds.xml` v10.0) that is specific to edu-sharing. **Budget real engineering for the pluggable
provider and the evaluation harness** — this recipe tells you the shape and the licence position,
not that the code exists.

## P22 — The OER catalogue enrichment pipeline: the first AI product a public education buyer will actually sign — NEW in p322

**When to propose it.** Any buyer that owns a large, badly catalogued body of learning content —
national or regional OER portal, ministry repository, university consortium, publisher backlist,
corporate academy after three acquisitions — and has been told to "do something with AI". It is the
pattern to lead with **instead of** a tutor (P1, P21) when the content layer is not yet trustworthy,
and p322's trend reading is the argument: Germany's public OER operator archived its chatbot in 2023
and spent the following three years building exactly this pipeline.

**Why it closes.** Every step is measurable against a before/after count, none of it touches a
child, none of it makes a pedagogical claim that has to be defended, and the output is the
prerequisite for every later AI phase. Under the EU AI Act this workload sits far away from the
Annex III education triggers that make P4 expensive — **it processes content, not learners.**

**The reference implementation exists, service by service, and was read first-hand at p322.** It is
`openeduhub` / WirLernenOnline. Use it as the architecture and **not** as the dependency set,
because the licences divide by layer:

| Step | Reference service (read p322) | Licence | Take it or rebuild it |
|---|---|---|---|
| 1. Harvest | `openeduhub/oeh-search-etl` (1,397 commits, Scrapy→Postgres→Elasticsearch) | 🔴 none | **Rebuild.** Use Scrapy directly; copy the spider layout only |
| 2. Clean text from a URL | `openeduhub/text-extraction` (77 commits) | 🔴 none | **Rebuild** on `trafilatura` + `markitdown` with a Playwright fallback — and copy its per-domain multibucket rate limiting, which is the part homegrown harvesters omit and publishers block over |
| 3. Deduplicate | `openeduhub/duplicate-detection` (25 commits, **MinHash over shingles**, URL + title normalisation) | **Apache-2.0** (`LICENSE` read first-hand; its README wrongly says MIT) | **Take it.** Hash-based, not embeddings: a MinHash threshold is defensible to a client, a cosine distance is not |
| 4. Extract metadata with an LLM | `openeduhub/metadata-agent-api` (24 commits, 11 schemas, **per-field origin tags**, `/generate` `/extract-field` `/validate` `/upload`) | 🔴 README says MIT, **no licence file** | **Rebuild to its endpoint shape.** Copy the schema set and the origin-tag idea; the origin tags are the provenance feature a public buyer now asks for by name |
| 5. Human review before anything is written | `openeduhub/metadata-agent-canvas` (60 commits, Angular 19 + LangChain, **confidence badge → inline edit → explicit confirm**) | 🔴 README claims Apache-2.0, **no licence file** | **Rebuild the interaction, which is the valuable part.** This is what a human-oversight requirement looks like as a UI instead of a policy sentence |
| 6. Capture from the teacher's browser | `openeduhub/metadata-browser-plugin-fuerAPI` (11 commits, **Manifest V3**, guest upload, lesson-plan cart) | **Apache-2.0** | **Take it** as the starting point for the contribution surface |
| 7. Readability / reading level | `openeduhub/text-statistics` (94 commits, Flesch Reading Ease + **Wiener Sachtextformel**, 200 WPM baseline, **no ML**) | 🟡 GPL-3.0 | **Deploy as a service behind HTTP, never link.** Confirm the Wiener formula before applying it outside German |
| 8. Accessibility + licence screen | `openeduhub/metalookup` (623 commits, Playwright + **Lighthouse**, `POST /extract`) | 🟡 GPL-3.0 | **Deploy as a service.** This is the compliance screen public procurement asks for and it already exists |
| 9. Predict missing metadata without labels | `openeduhub/its-jointprobability` (200 commits, **Pyro ProdLDA**, predicts discipline, resource type, audience, educational context, topic) | 🔴 none | **Rebuild** — and this is the row that justifies the engagement when the client has no labelling budget |
| 10. Subject classification | `openeduhub/discipline-classification` (73 commits, Keras/TF, **ships pretrained `wirlernenonline.oeh.h5`**, top-3 with scores) | 🟡 GPL-3.0 | **Service boundary**, and check the training-data provenance before shipping the weights |
| 11. Bulk-run one prompt over the catalogue | `openeduhub/z-api-runner` (37 commits, Swagger, model unstated) | 🔴 none | **Rebuild.** Trivial to write, universally needed, never budgeted |
| 12. Judge the output | `openeduhub/llm-judge` (1 commit, 6 criteria in `config.yaml`, gpt-4o-mini) + `openeduhub/ki-prompt-benchmark` (Apache-2.0, LLM-as-judge prompt bench, p321) | **Apache-2.0** | **Take the configuration shape, not the scores** — `llm-judge` publishes neither scale nor prompts nor aggregation, and it judges **factual accuracy, not pedagogy** |
| Everything above, to the platform | `openeduhub/edu-sharing-python-client` (519 commits, **389 operations generated from `openapi.json`**, verified against **edu-sharing 11.0**) | **Apache-2.0** | **Take it, and start here.** A permissive generated client is how you touch a GPL-3.0 edu-sharing instance with no linking question |
| Vocabularies for every field above | `openeduhub/oeh-metadata-vocabs` (938 commits, SKOS/Turtle, DigCompEdu/ESCO/EQF-DQR) | **CC0-1.0** | **Take it.** No attribution condition at all |

**The correction overlay, which is the non-obvious step.** `openeduhub/wlo-quellenliste`
(Apache-2.0, 6 commits) does the thing every one of these projects eventually needs and nobody
designs for: it merges the harvest with an **editorial correction CSV at serve time** rather than
mutating the harvested records. Build this in from day one — the harvest will be wrong, the
editorial team will be right, and overwriting the source destroys the ability to re-harvest.

**Inference placement, for an EMEA public buyer.** `metadata-agent-api` and `metadata-agent-canvas`
both ship a **B-API→AcademicCloud (`deepseek-r1`)** provider alongside OpenAI. A buyer that must
keep inference in national or academic compute therefore has a working reference for *this*
workload, not just for a tutor demo — quote it in the pitch, and see `intel/trends.md`.

**Sequencing and estimate.** Steps 1–3 and the client (the trustworthy-catalogue milestone) is where
the measurable win is: **6–8 weeks**. Steps 4–6 with human review in the loop: **a further 6–8
weeks**, and this is the phase that needs the client's editorial team committed, not just their IT.
Steps 7–12 are individually small and should be sold as a menu, not a block. **Timings are
engagement estimates, not measurements.**

**The three risks to put in the proposal yourself.**
1. **Six of the twelve reference services carry no licence** — 1,852 commits of it. The estimate
   above assumes rebuilding steps 1, 2, 4, 9 and 11, so do not let a reviewer price it as reuse.
2. **The GPL-3.0 analysers (7, 8, 10) must stay behind a process boundary.** Containerise and call
   over HTTP; if a client's security policy forbids that topology, those three steps become
   rebuilds too.
3. **Four of the reference repositories state a licence the repository does not carry.** Verify
   from the `LICENSE` file, not the README, on every one of them and on anything else you add — the
   full instance list is in `repos/foundations.md`.

## P1 — Curriculum-grounded lifelong tutor

**For:** any institution that wants a tutor answering from *its* material, with a learner model that
survives across sessions. The default education engagement.

**Stack**
- `HKUDS/DeepTutor` (Apache-2.0, 41.8k ★, **v1.6.15 released 2026-10-19**) — tutoring agent and lifelong learner state
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — the auditable agent loop for custom tools
- `dmitry-viskov/pylti1.3` (MIT, 138 ★) — LTI 1.3 tool so the tutor launches from the client's LMS
- Client LMS — `moodle/moodle` (GPL-3.0), `openedx/openedx-platform` (AGPL-3.0) or
  `instructure/canvas-lms` (AGPL-3.0), **unmodified**

**Wiring**
1. Ingest course material (syllabi, slides, past assignments) into LightRAG; one index per course,
   one namespace per institution. **Where a verified curriculum standard exists for the
   jurisdiction, ground against it rather than against the slides alone — see P10.** For Brazilian
   basic education that is `bncc-dev`; the measured difference is 31.9% → 2.3% curriculum
   hallucination.
1b. **Filter retrieved documents by student identity, institution and authorised category *before*
   prompt construction, and emit a disclosure record per retrieval.** New this pass. Copy the shape
   from `ashutoshrana/haystack-ferpa-filter` (Apache-2.0, 41 commits) — **read it, do not import it
   at 0 stars** — which returns filtered documents plus a `disclosure_record` for the caller to
   persist. This is cheap to build at design time, effectively impossible to retrofit after a
   FERPA/GDPR review, and it is the artefact that answers "prove this student could lawfully see
   that document". It also feeds P3's audit log for free.
2. Run DeepTutor as a service; pin the version — it released v1.6.15 on 2026-10-19 and moves weekly.
3. Expose the service as an LTI 1.3 Advantage tool via `pylti1.3`. The LMS launches it; the LMS is
   never patched. **This is what keeps Globant's code off the GPL/AGPL side of the line.**
4. Return grades/progress through LTI AGS so the gradebook stays authoritative.
   **Worked reference, new in pass 320.** This step has been asserted in every pattern in this file
   without a readable example of the passback itself. There is one now:
   **`adamzammit/LTIPlugin`** (**GPL-3.0**, 14 ★, 97 commits) makes LimeSurvey an LTI provider and
   **returns a 0.0–1.0 score to the gradebook, with README setup against Canvas, Moodle, openEdX
   and Blackboard.** **Read it; do not link it.** Three constraints: it is **not AI**, the page
   **never states an LTI version** and the bundled `LTI-Tool-Provider-Library-PHP` points at the
   **legacy 1.x Basic Outcomes path rather than 1.3 Advantage AGS** (verify the submodule before
   citing it as Advantage), and **GPL-3.0 is copyleft** — run it behind a process boundary, keep it
   out of the deliverable. **Use it to shorten the "how does the score actually land in four
   different gradebooks" question from four specifications to one repository.** For the permissive
   Advantage implementation you will actually ship against, `dmitry-viskov/pylti1.3` remains the
   dependency, with `tsugiproject/tsugi` as the heavier alternative.
5. Persist learner state in Globant-owned storage, keyed by the LTI `sub` claim — never by email.
6. **Prove it teaches, and do not use an LLM judge to do it. New this pass.** Before the pilot
   closes, run an evaluation the client's academics can defend:
   - Score tutoring behaviour with **`eth-lre/mathtutorbench`**'s task shapes — problem solving,
     socratic questioning, solution correctness, mistake location, mistake correction, scaffolding —
     which grade against **ground-truth teacher utterances via a reward model**, not a judge's
     opinion (licence caveat: CC BY badge vs CC BY-SA footer; resolve before extending it).
   - Borrow the discipline from **`bydeng01/conv-vs-ped-tutor`** and
     **`bydeng01/ability-levels-audit`** (both MIT): **pre-register the comparison, freeze and hash
     the data, keep a decisions log, separate registered analysis from post-hoc.**
   - **Measure answer leakage explicitly** — whether the tutor's "helpfulness" came at the cost of
     the student's later independent work. That is the failure mode an LLM helpfulness judge
     rewards.
   - **Never present a difference-in-differences on a bounded satisfaction scale as evidence of
     learning.** The audit above shows that design can manufacture an effect from nothing, and a
     client's statistician will eventually notice.
   **Cost:** 2–3 weeks inside the pilot. **Value:** it is the one claim in this market that
   competitors cannot make, in a sector where every deck asserts an uplift.

**Licence note:** every component Globant writes or links sits on the far side of the LTI boundary,
so the GPL-3.0/AGPL-3.0 platform never reaches it. Say this explicitly in the SOW.

**Competitive note, new this pass:** on Canvas, **Instructure's Project Athena (announced
2026-07-22) does this natively.** Do not sell P1 alone into a Canvas account. Sell P1 + P2 (the
pedagogy Athena does not do) or P1 + P3 (the audit trail the district must buy anyway).

**Estimate:** 8–10 weeks to a pilot with one faculty.

---

## P2 — Mastery-and-retention engine (the "actually pedagogical" tutor)

**For:** clients who will be asked by an accreditor or a ministry *why* the tutor showed what it
showed. P1 answers content; this one answers pedagogy. **This is the pattern that survives contact
with Canvas's native AI.**

**Stack**
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★, 467 commits) — **the engine.** Skill graph, Bayesian
  Knowledge Tracing, FSRS scheduling, prerequisite gating, cross-session narrative memory, as an
  MCP server. SQLite over stdio locally; PostgreSQL over HTTPS + OAuth in the institutional profile
- `CAHLR/OATutor` (MIT, 268 ★) — reference BKT implementation and hint sequencing; use to validate
  tutor-mcp's mastery estimates against a published academic implementation
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — standalone FSRS where you need
  scheduling outside the MCP server (offline clients, batch jobs)
- `satvik314/educhain` (MIT, 387 ★) — generate the item bank the engine consumes
- `HKUDS/DeepTutor` (Apache-2.0) — conversational surface
- `GeminiLight/gen-mentor` (CC0-1.0, 135 ★, WWW '25 oral) — **read, don't depend.** The
  peer-reviewed multi-agent ITS architecture to cite when a ministry asks for provenance
- `xiaoyang111222/cn-math-taxonomy` (**CC BY-NC 4.0**, 780 ★) — **new this pass; read, never
  ship.** The shape of the artefact step 1 asks the client's SMEs to produce, already built for
  Chinese K-9 mathematics: **531 knowledge points, 909 prerequisite edges distinguished as 788
  hard and 121 soft**, 2,271 items and 230 curriculum-standard entries, with a diagnostic engine
  and validation scripts. **NonCommercial rules it out of a deliverable, and its author states it
  is an AI-generated draft not reviewed by teachers** — so take two things from it: the
  **hard/soft prerequisite distinction** (a soft edge degrades the recommendation, a hard edge
  blocks progression) and the warning that a generated skill graph is a draft until a teacher signs
  each edge
- `brownplt/LTLTutor` (**GPL-3.0**, 12 ★, 320 commits, CAV 2025 Distinguished Paper) — **read,
  don't link.** Misconception-driven adaptation: it models the specific wrong beliefs learners hold
  and targets practice at them, which is a sharper decision rule than mastery probability alone

**Wiring**
1. Stand up tutor-mcp in the institutional profile (PostgreSQL, HTTPS, OAuth). Define the subject's
   skill graph — concepts and prerequisites — with the client's SMEs. **This is the engagement's
   real intellectual work and it is not LLM work.**
2. Educhain generates candidate items from the curriculum; a human SME approves into the bank.
   The approval step is not optional — Educhain is 387 ★ and slow-moving; treat output as a draft.
3. Let the engine decide: BKT tracks per-skill mastery, prerequisite rules gate progression, FSRS
   schedules review. **The LLM explains; the engine decides what comes next.** That separation is
   the entire defensibility argument and tutor-mcp enforces it architecturally.
4. Put DeepTutor (or any MCP-capable client) on the front as the conversational surface.
5. Validate against OATutor on a sample cohort before go-live — two independent BKT implementations
   agreeing is an evidence artefact an accreditor will accept.
6. **Have a teacher sign every prerequisite edge, and record who signed it. New this pass.** The
   skill graph is the engine's entire authority; a generated graph is a hypothesis. Borrow the
   hard/soft edge distinction from `cn-math-taxonomy` and treat an unsigned edge as soft.
7. **Run P1's stage 6 evaluation here too, and it matters more in this pattern than in P1** —
   because a mastery engine makes progression decisions. Pre-register the comparison, freeze the
   data, measure answer leakage, and **do not report an LLM-judged helpfulness score to an
   accreditor** (`agents/top.md`).

**The integration caveat that decides scope:** tutor-mcp's README names **no LTI, SCORM or xAPI
support.** It is MCP-only. For an institutional deployment you write the LTI 1.3 wrapper yourself
with `pylti1.3` and bridge it to the MCP server. Budget that bridge explicitly — it is the single
most-repeated unbudgeted item in this sector (see trend 6 in `intel/trends.md`).

**Estimate:** 6–8 weeks on top of P1; 10–12 weeks standalone. Add 2–3 weeks for the LTI bridge.

---

## P3 — Policy-gated deployment layer (North America, dated demand)

**For:** US districts and systems facing Ohio's 2026-07-01 framework requirement, Idaho SB 1227,
Oklahoma/Maryland human-oversight rules, or any of the 134 bills across 31 states in 2026.
**Sell this before selling a tutor.**

**Stack**
- Any tutor from P1/P2 as the governed subject
- `jupyterhub/jupyterhub` (BSD-3-Clause, 8.4k ★) — provenance-capturing compute for student work
- `jupyter/nbgrader` (BSD-3-Clause, 1.4k ★) + `ucbds-infra/otter-grader` (BSD-3-Clause, 161 ★) —
  autograding with a recorded execution trail
- `dmitry-viskov/pylti1.3` (MIT) — identity and grade passback from the LMS of record
- P7's gating layer (below) — grade-band enforcement is now part of the same deliverable

**Wiring**
1. Put every agent call behind a gateway that logs: prompt, retrieved sources, response, learner id,
   timestamp, model version. This log *is* the deliverable — it satisfies "educator supervision" and
   "no high-stakes automated decisions" in one artefact.
2. Hard-gate high-stakes actions (final grades, placement, discipline) behind human approval.
   Idaho's "AI cannot replace human teachers", and Oklahoma's and Maryland's reported bars on
   high-stakes AI decisions, are code-level constraints, not policy sentences.
3. Run assessment in JupyterHub; grade with nbgrader/otter-grader so the submission's execution
   history is evidence. This is the **process-evidence** answer to integrity — there is no credible
   open source AI-detector to buy instead, and there should not be (trend 9).
4. Generate the parent-disclosure and retention report from the same log. FERPA/COPPA retention
   windows are configuration, not a rewrite.

**Estimate:** 4–6 weeks; deployable before the tutor it governs.

---

## P4 — EU AI Act provider package (EMEA)

**For:** EMEA engagements where Globant builds the tool and therefore becomes the **provider** under
the AI Act, while the school is only the deployer. Annex III lists education as high-risk —
admissions, learning-outcome evaluation, student level placement, exam/behaviour monitoring.

**Stack**
- P1 tutor, plus:
- `openfun/richie` (MIT, 316 ★) — MIT portal/catalogue in front of an AGPL Open edX back end
- `overhangio/tutor` (AGPL-3.0, 1.1k ★) — reproducible Open edX deployment, in-region
- `learningequality/kolibri` (MIT, 1.2k ★) — where on-device/offline delivery is required
- Self-hosted models for data residency

**Wiring**
1. **Ship Article 50 transparency now.** It applied from 2026-08-02 and was *not* deferred: AI
   interaction disclosure in the UI and machine-readable marking of generated content. The smallest
   immediate billable item in EMEA. **The watermarking grace period for AI-generated content runs to
   2026-12-02** — six weeks from this pass — so machine-readable marking is a dated deliverable, not
   a backlog item.
2. **Check the 2026-12-02 prohibitions before that date** — new bans (non-consensual intimate
   imagery, CSAM) take effect six weeks from this pass. For an education product this is a
   content-safety and image-generation audit, and it is not deferred.
3. **Article 4 is now an obligation to take AI-literacy measures for staff** (relaxed, not removed).
   A documented staff-training programme discharges it, and the client needs one anyway (trend 1).
4. Build the high-risk conformity file *during* development: technical documentation, risk
   management, data governance, logging, human oversight, post-market monitoring. The deadline moved
   to **2027-12-02** under Regulation (EU) 2026/1744 — against 12–18 month public procurement
   cycles, conformity-ready is what wins 2026–27 bids. The deferral moved the date, not the
   substance.
5. **No emotion recognition anywhere in the stack.** Banned in schools since Feb 2025 — no
   engagement-detection from webcam, no affect scoring. Check this in code review.
6. Keep Open edX or Canvas unmodified behind Richie; AGPL's network clause reaches modified
   platforms, and not modifying it is the cheapest compliance decision available.

**Reuse note — the conformity file is the most portable artefact in this KB.** It travels to:
- **Brazil.** PL 2338/2023 is risk-based and passed the Senate in December 2024.
- **South Korea, and this one is already in force.** The **Framework Act on AI (Law No. 20676) has
  applied since 2026-01-22**, its **high-impact AI** category explicitly covers **student evaluation
  in early childhood, elementary and secondary education**, and high-impact operators owe
  **user-protection measures and records of safety and trust measures (Art. 34(1))** — the same
  documentation set as the Annex III file. The **fundamental-rights impact assessment is voluntary
  (Art. 35)**, so lead with it as a differentiator rather than a cost. **A foreign vendor without a
  Korean presence must appoint a domestic agent** — a commercial arrangement to settle before
  bidding, not an engineering task. Grace period on fines is reported as one year from entry into
  force. Read the Enforcement Decree and MSIT guidance before quoting thresholds.
- **Uruguay**, as the LATAM pilot: first in Latin America to sign the Council of Europe AI Framework
  Convention, so European-shaped evidence is the evidence it already expects.

**Estimate:** 10–12 weeks including the conformity file. Porting it to a second jurisdiction:
2–3 weeks, almost entirely mapping and review rather than build.

---

## P5 — Offline-first national curriculum delivery (APAC, Africa, and the India mandate)

**For:** India's compulsory AI + Computational Thinking rollout for Classes 3–8 from 2026-27 across
32,900 CBSE schools — 50 h/yr for Classes III–V, 100 h/yr for VI–VIII — where **64.7% of schools
have computers and 63.5% have internet.** A cloud tutor does not serve this brief. **Also the right
pattern for Sub-Saharan Africa**, where the strongest evidence base for low-resource AI tutoring
exists (World Bank Edo State, Nigeria; EIDU in Kenya, ~400k children) and Kenya's DigiSchool has
put over 1 million tablets into primary schools.

**Stack**
- `learningequality/kolibri` (MIT, 1.2k ★) — offline-first delivery; MIT, so AI can embed directly
- `Sunbird-Ed/SunbirdEd-portal` (MIT, 41 ★) — India's national stack; the integration target
- `zijinz456/OpenTutor` (MIT, 145 ★) — **new this pass.** Local-first adaptive workspace, 10+ LLM
  providers, runs on-device; the tutor shell when nothing may leave the building
- `satvik314/educhain` (MIT, 387 ★) — bulk generation of curriculum-aligned items, SME-reviewed
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — scheduling that works with no network
- `microsoft/ai-agents-for-beginners` (MIT, 77.5k ★) — white-labelled teacher-training base
- `elimu-ai/webapp` (MIT, 41 ★, **8,075 commits**) — **new this pass.** Per-language content hosting
  that pushes to Android devices for out-of-school children, with production deployments in Hindi,
  Tagalog, Thai, Vietnamese and English; the same org publishes MIT ML components for reading-level
  prediction and storybook/video recommendation
- `ipti/br.tag` — **new this pass**, and read for one design decision rather than adopted: school
  management built for rural schools with **data sync for schools without internet**. Its licence is
  unresolved (README says BSD-3-Clause, sidebar links GPL-2.0), so **copy the sync model, not the
  code**

**Wiring**
1. Generate and SME-approve the item bank **centrally and online**; the only step needing
   connectivity at scale.
2. Package approved content into Kolibri channels; distribute by sync server, USB or sneakernet.
   Kolibri is MIT, so an embedded on-device scheduler or small local model is licence-clean.
3. Use OpenTutor as the on-device adaptive surface where a local LLM is available; fall back to
   pre-generated Kolibri content where it is not. **Design for both — device capability varies
   school to school in exactly these markets.**
4. Run FSRS scheduling fully on-device; sync learner state opportunistically, not continuously.
5. Integrate with Sunbird for national reporting — verify the wider `Sunbird-Ed` org's component
   repos before scoping; the portal is one piece of a larger stack.
6. Deliver teacher training from the `ai-agents-for-beginners` curriculum. **Training is the
   engagement, not an add-on** — and per trend 1, delivering training that *lands* is the hard part.
7. **Stage the adoption and say so in the bid. New this pass, and it is the lesson of the most
   expensive failure in this sector.** South Korea mandated AI digital textbooks nationally, met
   teacher and parent resistance, retreated to voluntary adoption, and on **2025-08-04** the
   National Assembly removed them from the legal definition of a textbook, taking the funding with
   them; usage had already fallen from ~37% of eligible classes in the first semester of 2025 to
   19% in the second, and schools from ~4,190 to 2,095. **Every education ministry in APAC watched
   that.** So: opt-in pilot schools, published outcome measures (P1 stage 6), teacher capability
   before coverage, and a documented exit path. **Price change management as the main line item,
   not the technology.**

**Estimate:** 12–14 weeks for a state-level pilot.

---

## P6 — The roster and SIS data spine (North America)

**For:** any US district or state engagement, under any of the patterns above. An agent that does
not know who the student is, what they are enrolled in and which teacher owns them is a demo.
Earlier passes of this KB called this bespoke integration work; **it is not, and that was a
search error — see `repos/foundations.md`.**

**Stack**
- `Ed-Fi-Alliance-OSS/Data-Management-Service` (Apache-2.0, 12 ★, 1,105 commits) — the Ed-Fi API
  platform, successor to the ODS/API platform
- `Ed-Fi-Alliance-OSS/edfi-oneroster` (Apache-2.0, 6 ★, 151 commits) — serves a **OneRoster 1.2**
  API from data in an Ed-Fi ODS
- `dmitry-viskov/pylti1.3` (MIT) — LTI identity at launch, reconciled against the roster
- Whichever tutor and governance layer from P1/P2/P3

**Wiring**
1. Stand up the Data-Management-Service against the district's Ed-Fi ODS. **Pin to a commit —
   neither repo publishes GitHub releases.**
2. Expose OneRoster 1.2 through `edfi-oneroster` as the single read interface your agents use for
   enrolment, section and teacher-of-record data. One contract, not one per SIS vendor.
3. At LTI launch, resolve the `sub` claim to the roster identity; everything downstream — learner
   state, mastery estimates, audit log entries — keys off that resolved id, never off an email.
4. Feed the teacher-of-record relationship into P3's human-approval gates. "Educator supervision"
   has to name an actual educator, and this is where that name comes from.
5. Keep the roster read-only from the agent side. Writes go back through the LMS gradebook over
   LTI AGS, not into the SIS.

**The standards argument to put in the proposal:** 1EdTech's 2026 position is that interoperability
is the precondition for AI, naming CASE, Edu-API and OneRoster as the standards that give an AI
system trustworthy institutional context. This pattern is that position implemented on Apache-2.0
code.

**Scope limit, stated plainly:** Ed-Fi is a North American standard in practice. It is not a route
into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions. Everywhere
else, SIS sync is still bespoke.

**Estimate:** 3–5 weeks alongside P1 or P3; longer if the district's ODS is not already populated,
which is a data-quality project and should be priced as one.

---

## P7 — Grade-band gating and teacher-only mode (North America K-12)

**Pass 320 upgrade — model parent consent as state, not as a flag.** Pass 319 scoped the parent
opt-out from **a single tracker** reporting Oklahoma's statute and flagged it as unverified.
**There are now two independent instances by two different mechanisms:** Oklahoma's reported
opt-**out**, and **South Carolina H.B. 5253**, reported to require **written parental opt-in
consent**. Opt-in and opt-out are **not the same data model** — opt-in defaults a pupil to
*excluded* and blocks the product until a positive record exists; opt-out defaults to *included*
and must honour a withdrawal at any time, including retroactively for data already processed.
**Build the stricter one and configure down:** store a per-pupil consent record with a mode
(`opt-in` / `opt-out`), a timestamp, the granting party and the jurisdiction, and make the tutor
check it on every launch rather than at enrolment. **A product that cannot express both modes is
unbiddable in at least two states**, and the duty to provide **alternative access to core
instruction** for a non-consenting pupil is a curriculum-delivery requirement, not a feature flag —
it is what makes `learningequality/kolibri` (MIT, offline) useful in this pattern rather than
decorative. *(Both statutes are snippet-sourced; `www.future-ed.org` and `www.multistate.us` are
unreachable from this session. Verify before a bid — and scope for it regardless, because the cost
of building it is small and the cost of retrofitting it is not.)*

**For:** districts that restrict rather than adopt. **New York City runs a one-year moratorium on
student-facing AI through eighth grade; Katy ISD (Texas) is banning generative AI chatbots for
K-6.** A product that cannot be switched off for a grade band cannot be bid into these districts —
and they are not outliers.

**Stack**
- P6's roster spine — grade level is a roster attribute, and it is the only trustworthy source
- P3's logging gateway — the gate is enforced and evidenced at the same chokepoint
- Any P1/P2 tutor as the gated subject

**Wiring**
1. Resolve grade level from the roster at launch (P6), not from a profile field a student can edit.
2. Enforce three modes at the gateway, per grade band, as policy configuration rather than code:
   **student-facing**, **teacher-facing only** (the teacher may use the agent *about* the student's
   work; the student never sees it), and **off**.
3. Default to the most restrictive mode for any learner whose grade level does not resolve. Fail
   closed.
4. Emit the mode into every audit-log entry. "Prove no eighth-grader interacted with the AI" then
   becomes a query, which is exactly the question a district under a moratorium will ask.
5. Expose the configuration to district administrators. The policy will change mid-contract; make
   that a settings change, not a release.
6. **Add a per-pupil opt-out that degrades gracefully. New this pass.** Four states enacted
   education-AI statutes in 2026 — **Idaho, Maryland, Oklahoma, Virginia** — and per one tracker
   Oklahoma's gives **parents an opt-out from student-facing AI tools together with a duty to
   provide alternative access to core instruction** *(single-tracker claim; verify against the
   statute, build for it regardless)*. The flag belongs on the roster record (P6), is enforced at
   the same gateway as the grade band, and **must leave the pupil with the instruction minus the AI
   path** — an opt-out that removes the lesson is a civil-rights problem, not a feature.
7. **Add an approval queue.** Oklahoma permits AI only under educator supervision with human review
   and **bars it from high-stakes student decisions**. So nothing AI-written reaches a student, a
   parent or a record until a named educator signs it, and the signature is logged with the draft
   it approved. `JaimeArriagadaRosas/Plugin-Feedback-Canvas` implements exactly this shape against
   Canvas over LTI 1.3 and **has no licence** (`agents/top.md`) — read it, rebuild it.
8. **Add a decision log that can answer "was any high-stakes determination AI-made?" with a
   query.** Placement, discipline, promotion, eligibility. The answer a district needs is "no, and
   here is the record", not a policy document.

**Why this is worth building once:** it is small, every K-12 district in a restricting state needs
it, and teacher-facing-only mode **keeps the engagement alive in a district that has banned
student-facing AI.** That is the difference between a lost account and a smaller one. **With the
opt-out, approval queue and decision log added, this pattern is no longer defensive — in Oklahoma,
Idaho, Maryland and Virginia it is the compliance surface the statute asks for**, and
`SirhanMacx/Claw-ED` (MIT, 778 commits) is a working reference for the teacher-facing-only product
shape.

**Estimate:** 2–3 weeks on top of P3 and P6 for gating; **+2 weeks for the opt-out, approval queue
and decision log.**

---

## P8 — The permissive-LMS build: no LTI boundary (greenfield, and EMEA sovereignty) — NEW

**For:** two specific situations, and no others. (1) A **greenfield** build — a corporate academy,
a bootcamp, a new programme, a ministry standing up something new — where no incumbent LMS exists.
(2) An **EMEA sovereignty** engagement where the buyer needs the data, the platform and ideally the
vendor inside Europe.

**Why it is new:** every other pattern in this KB pays the same architectural tax — Globant's agent
code must sit on the far side of a network boundary because the LMS is GPL/AGPL. **`OpenOLAT` is
Apache-2.0 with 31,877 commits**, so for the first time that tax is optional.

**Stack**
- `OpenOLAT/OpenOLAT` (**Apache-2.0**, 448 ★, 31,877 commits) — the LMS. Teaching, learning,
  assessment, communication, modular course authoring. frentix GmbH (Switzerland), built on the
  University of Zurich's OLAT 7.1
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★) — the P2 pedagogy engine; BKT, FSRS, prerequisite gating
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `HKUDS/DeepTutor` (Apache-2.0, 41.7k ★) — conversational surface
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — agent loop for custom tools
- Self-hosted models (in-region) for the sovereignty case
- **Not** `pylti1.3`. That is the point of this pattern

**Wiring**
1. Confirm the licence from the **file, not the page.** OpenOLAT's GitHub sidebar names no licence;
   `LICENSE` is the full Apache-2.0 text followed by two provenance notices crediting the OLAT
   Zentrum at the University of Zurich and the OpenOLAT community/frentix GmbH. **Those are
   attribution notices in the NOTICE tradition, not additional licence terms** — the grant is
   Apache-2.0. Record it that way in the licence inventory and attach the file to the SOW. Pin to a
   commit and keep the NOTICE attribution intact in any distribution.
2. Deploy OpenOLAT in-region. For the sovereignty case this is the whole proposition: European
   platform, European maintainer, client-controlled infrastructure, no US hyperscaler dependency.
3. **Integrate the agent in-process.** Apache-2.0 permits linking Globant's code to the platform, so
   ship one deployable instead of a tool plus a bridge. Keep the agent in its own module behind a
   clean interface anyway — not for licence reasons now, but so the work ports to a Moodle or Canvas
   client later across an LTI boundary (P1).
4. Run tutor-mcp as the pedagogy engine and LightRAG as the retrieval layer, exactly as in P1/P2.
   Add P1's **step 1b FERPA/GDPR retrieval filter** — in EMEA this is GDPR and Annex III evidence,
   not optional.
5. If the client is EMEA, **run P4 on top.** Apache-2.0 removes the licence boundary; it removes
   nothing about the AI Act. Globant is still the provider and still owes the conformity file.

**What this pattern does NOT do.** It does not apply to a client already running Moodle, Canvas,
Open edX or Sakai — which is nearly every client. There, the incumbent platform is a given and the
LTI boundary is mandatory; use P1. **Do not propose a migration to OpenOLAT.** 448 stars against
Moodle's 7.5k and Canvas's 6.9k is not a competitive position, the documentation's centre of gravity
is Swiss-German, and no institution is leaving Canvas for it. This pattern is for the cases where
there is nothing to migrate from.

**The honest risk:** a smaller community than Moodle or Open edX, which means fewer integrators,
less third-party plugin supply and a thinner hiring pool. Price support accordingly, and do not
present it as a like-for-like Moodle substitute.

**Estimate:** 8–10 weeks to pilot (greenfield), 12–14 weeks with P4's conformity file for an EMEA
public-sector buyer. Roughly 2–3 weeks less than the equivalent P1 build, because the LTI bridge
and its testing disappear.

---

## P9 — The COPPA disclosure boundary (North America K-12) — NEW

**Time**: 3–5 weeks for the audit, 6–10 weeks for remediation | **Licences**: all permissive
**Trigger**: the amended COPPA Rule, full compliance required since **2026-04-22**

**Why this is the shortest-cycle pattern in this file.** It does not ask the district to buy a new
capability. It tells them something they already own is out of compliance with a federal rule that
took effect six months ago, and then fixes it. The budget line exists before the conversation does.

**The legal mechanic, stated precisely because the whole pattern turns on it.** Amended
§312.5(a)(2) requires **separate verifiable parental consent before a child's personal information
is disclosed to a third party**, and the exception covers disclosures *integral* to the service,
not merely useful or convenient. A parent may consent to the product and refuse the disclosure.
The Rule also adds **retention limits**, a **written, published retention policy**, and
**biometric identifiers** to the definition of personal information.

**In a typical 2025-vintage K-12 tutor, the pupil's prompt goes to OpenAI, Anthropic or Google.
That is a disclosure to a third party.** If it was covered by a single blanket consent at
sign-up — which is the normal implementation — the deployment is non-compliant.

### Stage 1 — the posture audit (3–5 weeks, sellable on its own)

Inventory, for every AI feature the district runs:

1. **Egress**: which fields leave the district boundary, to which processor, under what contract.
   Prompts are the obvious one; transcript history, assignment text, IEP-adjacent notes and voice
   audio are the ones that get missed. Voice adds biometrics, which are now PII by definition.
2. **Consent structure**: is there one consent or two? If the parent cannot accept the product and
   decline third-party model disclosure *independently*, there is a finding.
3. **Retention**: is there a written, published retention policy, and does the system actually
   enforce it — including on the processor's side, where the contract usually says 30 days and
   nobody has checked.
4. **Integrality argument**: for each disclosure you intend to keep, write the sentence explaining
   why it is integral to the service the parent asked for. If that sentence is hard to write, the
   disclosure fails the exception.

Deliverable: a findings register mapped clause-by-clause, with each finding marked
*remediate-in-place* or *remove-the-disclosure*.

### Stage 2 — remediation, and there are only two real answers

**Answer A — separate the consent and keep the disclosure.** Split the consent flow in two, gate
model calls on the second grant, and degrade gracefully for pupils whose parents granted only the
first: the product must still work, teacher-facing or with local-only features. Add retention
enforcement as a scheduled job with an audit record per deletion, reusing the hash-chained audit
shape the governance layer in **P3** already builds. This is the cheaper path and it leaves the
district's existing vendor relationships intact.

**Answer B — remove the disclosure entirely.** If the model call never leaves the district
boundary, §312.5(a)(2) is not engaged for that call. Two routes, both already in this KB:

- **On-premise inference behind the LMS the district already runs.** Moodle's core AI subsystem
  takes an **Ollama** provider directly, and its **OpenAI-compatible** provider accepts a
  self-hosted **LiteLLM** or **LocalAI** gateway (`verticals/solutions.md`). The pupil's prompt
  reaches a model the district operates. No third party, no second consent, no retention exposure
  at a processor.
- **Offline-first delivery** where connectivity or policy makes even on-premise inference
  impractical — **Kolibri** (MIT) plus the local tutor shell in **P5**, with
  `zijinz456/OpenTutor` (MIT, 10+ providers incl. local) as the agent shell.

**Pair B with the deterministic pedagogy engine and the compliance story gets better, not worse.**
`tutor-mcp` (MIT) runs BKT, FSRS and prerequisite gating **locally against SQLite** — the mastery
model, which is the most sensitive longitudinal record in the system, never needs to leave the
building at all. The LLM is then only a language surface over a local decision engine, and the
smallest possible share of pupil data crosses any boundary. **This is the strongest commercial
argument in this KB for the architecture it has advocated for four passes, and it now has a
federal rule behind it rather than an aesthetic preference.**

### What not to build

**Do not build a COPPA compliance engine.** `repos/foundations.md` records about a dozen
FERPA/COPPA governance repos, every one at 8 stars or fewer and nearly all started in the two
months after the April deadline. The market is forming; none has won; and a client's compliance
posture should not sit behind a 1-star dependency. Build the audit as a method and the remediation
as architecture, reuse **P3**'s audit-logging layer, and keep the legal determination with the
district's counsel — the engagement is the disclosure-boundary redesign, not a legal opinion.

**Scope boundary to state in the SOW:** Globant determines where data flows and makes it match what
the district's counsel says the Rule requires. Globant does not certify COPPA compliance.

---

## P10 — The verified curriculum spine (LATAM now; APAC as a build; **cross-national and licensed, from p326**) — NEW

**For:** any engagement where the client is accountable to a **national or state curriculum
standard** — a ministry, a public school network, a board, a national edtech, a university serving
a regulated programme. This is the pattern that answers "how does your tutor know what my
jurisdiction requires it to teach?" with data instead of a prompt.

**Why it is new, and why it is the most defensible recipe in this file:** pass 319 found the first
artefact in this sector that turns a national curriculum into verified, permissively licensed,
machine-readable infrastructure **and publishes what it is worth.**

### Variant A — Brazil, today, with components that already exist

**Stack**
- `bncc-dev/bncc-dados` (**MIT code / CC BY 4.0 data**, 22 ★, 40 commits) — the BNCC as **1,721
  verified learnings** (1,580 basic-education skills across three stages plus the 141-item Computing
  complement), JSON canonical with SQLite/SQL/CSV builds, JSON Schema draft 2020-12, content version
  `dados-2026.08`
- `bncc-dev/bncc-pacotes` (**MIT code / CC BY 4.0 data**, 9 ★, 103 commits) — npm `@bncc/dados`,
  **npm `@bncc/mcp` (seven MCP tools)**, PyPI `bncc`, and a **hosted keyless MCP endpoint** at
  `mcp.bncc.dev`
- `bncc-dev/bncc-benchmark` (**MIT code / CC BY 4.0 items and results**, 9 ★, 82 commits) — the
  acceptance test
- `HKUDS/LightRAG` (MIT) + `HKUDS/DeepTutor` (Apache-2.0) — retrieval and tutoring, as in P1
- `portabilis/i-educar` (GPL-2.0, **34,948 commits**) and `portabilis/i-diario` (**AGPL-3.0**,
  read first-hand at p341) — the records layer a Brazilian public client is already running.
  🔴 **The two halves differ and it matters here:** `i-diario` is network copyleft and is the
  teacher-FACING half, so §13 attaches to the surface this pattern attaches to
- `dmitry-viskov/pylti1.3` (MIT) or `tsugiproject/tsugi` (Apache-2.0) — the boundary

**Wiring**
1. **Pin the curriculum dataset to a release, not a branch** (`dados-2026.08`, schema v1.1.0), and
   record the checksum. The packages already do this internally; your deployment must too, because
   a curriculum that changes silently under a tutor is a correctness incident.
2. **Resolve every learning objective through the MCP server or the typed package — never through
   the model's memory.** This is the whole point: a well-formed code that does not exist returns an
   explanatory error rather than `null`, which is what stops a tutor inventing a standard.
3. **Index the client's own material with LightRAG and link each chunk to one or more curriculum
   codes.** The codes are the join key between what the client teaches and what the state requires.
4. **Expose two retrieval paths to the tutor**: curriculum (authoritative, from the dataset) and
   course material (client-owned, from LightRAG). Keep them separate in the prompt and label them,
   so a citation can always be traced to one or the other.
5. **Run the benchmark as the acceptance test before go-live**, on the client's own model and
   configuration: direct lookup, existence (including plausible fake codes — this is the one that
   catches a confident tutor), open generation, reverse lookup. **Publish the result to the client.**
6. Keep Globant's agent on the far side of the LMS/SIS boundary as always: i-Educar is GPL-2.0, and
   i-Diário's licence is unresolved.

**What to promise, with the number behind it:** on this curriculum, an ungrounded model invents a
standard **31.9%** of the time; with the verified dataset queried over MCP, **2.3%**; with the data
pasted directly into the prompt, **0.2%**. Across the models the benchmark tested, faithful-text
rates ran from **88% down to 3%** — so **no model choice closes a 30-point grounding gap.**

**Estimate:** 5–7 weeks on top of P1, most of it in step 3 (mapping client material to codes).

### Variant B — India, where the artefact barely exists and the mandate is dated

> **🟡 UPDATE, pass 323.** This variant's premise was *"the artefact does not exist."* **It now
> partly does, and it has no licence.** `razi-03/NCERT-CKG` (`repos/foundations.md`) covers **Class X
> NCERT Mathematics from 18 PDFs**: **10,417 CKG nodes, 1,682 semantic nodes with provenance at
> 1,682 / 1,682, 13,757 provenance-aware edges** — and it **separates prerequisite reasoning from
> textbook ordering**, explicitly refusing to treat chapter order as prerequisite evidence. **That is
> step 1 of the build below, done correctly, by someone else, on one grade of one subject.**
>
> **What this changes about the engagement, concretely:**
>
> - **Step 0 is now "talk to `razi-03`."** 0 stars, 0 forks, **two commits, no LICENSE file**. A
>   permissive licence on that repository would hand this build a verified Class X Mathematics seed
>   and a method already aligned with Brazil's. **That is the cheapest possible acceleration of a
>   10–14 week build, and it costs one email.** If the answer is no, nothing is lost — the method
>   below is unchanged.
> - **Two unknowns to resolve before using any of it:** the README says **nothing about textbook
>   copyright or whether the 18 NCERT PDFs are bundled** (this KB has already recorded one NCERT
>   project that bundles textbook PDFs, and that is a live copyright question), and it **never
>   mentions an LLM**, so whether the edges are model-derived is **unknown rather than disclosed.**
>   Neither can be assumed benign; both are answerable by reading the tree.
> - **The deadline is unchanged and close:** AI + Computational Thinking compulsory for **Classes
>   3–8 from 2026-27 across 32,900 CBSE schools.** Class X Mathematics is not in that band, so the
>   seed does not cover the mandated grades — **it de-risks the method, not the scope.**
> - **The window is narrower than p319 priced it.** See Variant C: the uncontested-opportunity
>   framing no longer holds region-wide.

**The gap, as measured in p322 and now qualified:** GitHub's `ncert` and `cbse` topics hold 180
repositories and **nothing above 15 stars that is curriculum infrastructure** — and that sweep
**missed** the artefact above, which a query on the *artefact type* rather than the country topic
found in one search. The one MCP server
(`jinanshm/ncert-mcp`, 1 ★, 2 commits) is **unlicensed** and ingests by downloading the NCERT PDFs
and **tagging chunks with an LLM via OpenRouter with no human verification described** — which is a
hallucination source with a schema. `praj2408/RAG-Enhanced-NCERT-Tutor` (MIT, 3 commits) **bundles
textbook PDFs**, a copyright question of its own. The best data asset is a **2018** scrape of
~20,000 schools. Meanwhile **AI + Computational Thinking is compulsory for Classes 3–8 from
2026-27 across 32,900 CBSE schools.**

**The build, copying Brazil's method rather than its data**
1. **Extract against the official source and verify it.** Character-level checking against the
   published curriculum document, not LLM tagging. A code sweep for missing and extra codes.
2. **Publish a schema** and 25–30 contract and completeness checks that run in CI, so a divergence
   fails the build rather than reaching a classroom.
3. **Keep a decisions log** for every inconsistency found in the source. This is what makes the
   dataset citable by a ministry.
4. **Split the licence deliberately**: permissive for the pipeline, attribution-only for the data,
   with the normative texts identified as official acts. That is what makes it adoptable by
   competitors — which is the point of a moat built on a standard.
5. **Ship an MCP server and typed packages** over it, plus a hosted endpoint.
6. **Build the benchmark alongside it**, including the fake-code existence task, and publish the
   numbers.

**Why do this rather than a tutor:** whoever holds the verified curriculum layer for a jurisdiction
is in every bid in that jurisdiction, because the alternative is each vendor re-deriving it badly.
~~At 22 stars in Brazil, **nobody is competing for this yet.**~~ **Corrected in p323: pick the
jurisdiction deliberately, because one is now contested.** Brazil's `bncc-dev` is still at
low-double-digit stars and uncontested; **China's equivalent has 420 stars, 67 forks and a NeurIPS
2026 acceptance** (Variant C). India is contested by one unlicensed two-commit repository. **The
opportunity is per-jurisdiction, and it is no longer uniformly open.** It is fundable as a standalone asset
(a board, a ministry, a national edtech, or a foundation), it is reusable across every subsequent
engagement in the market, and it is the rare deliverable whose quality is **objectively
demonstrable** — the benchmark is the proof.

**Estimate:** 10–14 weeks for one subject across the mandated grades, including verification;
longer for a full curriculum. **Verification is the majority of the work and the entire value.**

**Where else this applies:** anywhere with a published national curriculum and no data layer —
which, on the topics swept this pass, is everywhere except Brazil. Germany's attempt was archived
in 2021; the Dutch and Spanish-language topics produced course material; the English `oer` topic
produced textbooks and no competency metadata. Ed-Fi (`repos/foundations.md`) is the North American
**rostering** standard and does not cover curriculum.

### Variant C — China and the method-reuse play, where the artefact exists and its data is NonCommercial — NEW in p323

**The situation that makes this a distinct variant:** `haolpku/K12-KGraph` (`repos/foundations.md`)
has already built what Variants A and B describe, for China's PEP K-12 curriculum, to a standard a
Globant build would be measured against:

| | What it holds |
|---|---|
| Scope | **48 PEP textbooks** — Mathematics 23, Physics 9, Chemistry 7, Biology 9 |
| Graph | **10,685 nodes**, **23,278 edges across 9 edge types**, **every edge carrying an `evidence` field** linking to textbook source text |
| Verification | **12 subject-qualified expert annotators, Fleiss' κ = 0.84**; DAG validation of `is_a` and `prerequisites_for`; 3-expert spot-check at **98.4% fully correct** |
| Proof | **K12-Bench, 23,640 multi-select questions**; K12-Train, 2,267 pairs; three fine-tuned checkpoints on Hugging Face |
| Standing | **NeurIPS 2026 Evaluations & Datasets Track**, 420 ★, 67 forks |
| Licence | **MIT (code) / CC BY-NC-SA 4.0 (graph, benchmark, training data)** |

**The licence is the whole design constraint, so state it to the client on day one:** the
**pipeline is MIT and reusable**; the **curriculum graph, benchmark and training data are
NonCommercial and ShareAlike and cannot enter a commercial deliverable — in China or anywhere
else.** ShareAlike would additionally attach to any derivative graph. **There is no version of this
engagement in which K12-KGraph's data ships.**

**What to actually sell, in order:**

1. **The method transfer, not the data.** Fork the **MIT pipeline** and run it against the client's
   own corpus — their textbooks, their syllabus, their licensed content. **The expensive, risky part
   of P10 has a working reference implementation** with a published quality bar; that converts a
   10–14 week verification project from a research bet into an execution task. **Price the saving,
   and be explicit that the saving is in the method.**
2. **Adopt its verification protocol as the acceptance criterion.** Per-edge source evidence,
   automatic DAG validation of the prerequisite subgraph, multi-annotator agreement with a reported
   κ, and a stratified expert spot-check. **This is the first externally published, peer-reviewed
   quality bar for a curriculum graph, and a client can hold a vendor to it.** Brazil's `bncc-dev`
   supplies the complementary half — character-level verification against the homologated source,
   contract checks in CI, a decisions log. **Together they are the specification Globant should be
   writing into its own P10 statements of work.**
3. **Use K12-Bench as an off-the-shelf evaluation instrument where the licence permits
   non-commercial use** — internal benchmarking, a research collaboration, a public-sector pilot
   with a university partner. **Not in a paid deliverable.** Check the specific use against
   CC BY-NC-SA 4.0 with counsel; "internal" and "non-commercial" are not synonyms.
4. **Where the client wants the graph itself and the licence forbids it, the answer is Variant A or
   B's build.** Rebuilt from the client's corpus with the client's grant. **The existence of a
   NonCommercial artefact is a reason the build is well understood, not a reason to skip it.**

**The competitive read, which is the real reason this variant exists.** p319 priced the verified
curriculum layer as an **uncontested** build-once opportunity at 22 stars. **In APAC it is
contested, by an academic group, with a peer-reviewed quality bar and 420 stars.** Two consequences:
**expect a Chinese or regional client to know this artefact already**, and **expect the quality bar
in any APAC curriculum-data bid to be K12-KGraph's, not this KB's.** The jurisdictions still open —
India (barely, see Variant B), most of LATAM beyond Brazil, most of EMEA, and everywhere on
`repos/foundations.md`'s unswept-language list — are where the uncontested framing still holds, and
**that framing now has a shelf life.**

**Estimate:** 4–6 weeks for a method-transfer engagement (fork, re-target the pipeline to the
client's corpus, stand up the verification protocol and acceptance criteria) before any curriculum
volume is processed; the per-subject build then prices as Variant B. **The first deliverable is the
acceptance criteria, and it is sellable on its own.**

### Variant D — the cross-national spine, available today, for a client with no jurisdiction mandate — NEW in p326

**For:** the engagement Variants A and B do not cover — an international school network, a
consumer or B2C learning product, a corporate foundation's K-6 programme, a pilot that has to run
before a ministry conversation exists, or **any client in a jurisdiction this KB has no curriculum
artefact for.** Variants A and B both start from a national mandate. **This one starts from the
absence of one.**

**Stack**
- `withmarbleapp/os-taxonomy` (**ODbL-1.0 database / CC BY-SA 4.0 text**, 6.1 ★k) — **1,591
  micro-topics, 3,225 prerequisite edges, ages 4–15, eight subjects, 2,189 links into 3,261
  standards across UK NC 2013, CCSS ELA, CCSS Math, NGSS K-5, NGSS MS, C3 and IB PYP PSPE.**
  Ships `assessmentPrompt` on **all 1,591** topics and `evidence` descriptors on 1,556
- `tbh-23/Homestead` (**MIT**, 15 ★) — **read it before you write anything**: the runtime-fetch
  boundary, the 90% mastery gate and the independently re-solved mastery tests are already built
- `ArnaudGuiovanna/tutor-mcp` (MIT) — BKT mastery state and prerequisite rules over MCP, keyed to
  the taxonomy's topic IDs
- `open-spaced-repetition/fsrs4anki` (MIT) — retention scheduling once a topic is mastered
- `openfun/ralph` (MIT) — xAPI learning records, **one statement per topic ID**
- `HKUDS/LightRAG` (MIT) — retrieval over the client's own material, chunks linked to topic IDs

**Wiring**
1. **Pin a commit and record the SHA-256s from `data/manifest.json`.** The dataset moves: every
   secondary description in circulation says 1,590 topics / 3,221 edges, and the file shipped on
   2026-10-19 is **1,591 / 3,225**. Verify the hash on every refresh and diff the topic set —
   Homestead does exactly this and surfaces added and removed topics to the user.
2. **Do not vendor the data. Fetch it at runtime into a cache outside your repository.** This is
   P13 and it is what keeps the ODbL database out of your product.
3. **Load `dependencies.json` as the ordering authority, and respect `strength`.** 2,030 edges are
   `hard` — gate on these. 1,195 are `soft` — surface them as *"this will be easier if…"*, never
   as a block. **Every edge carries a prose `reason`; show it to the learner or the parent.** It
   is the cheapest explainability win in the whole pattern and it was authored, not generated at
   request time.
4. **Use `assessmentPrompt` as the mastery check, not a model-generated question.** One per topic,
   all 1,591, with a `{{name}}` placeholder to substitute or strip. **Substitute server-side, as
   P12's Panama design does** — the prompt sent to the model should not carry the learner's name.
5. **Use `evidence` as the rubric.** Three observable can-do statements per topic on 1,556 of
   them; they are what a teacher or parent signs off against, and what an LLM judge should be
   scored on reproducing — not helpfulness. See the *"prove it teaches"* stage.
6. **Join the client's own material to topic IDs with LightRAG**, exactly as in Variant A. The
   topic ID is the join key between the spine and everything the client already owns.
7. **Write client-jurisdiction extensions into an overlay table keyed by topic ID — never into the
   graph.** This is the commercial decision in the whole pattern; see P13.

**What to promise, and what not to.** Promise **sequencing, age banding, standards alignment and
assessment coverage on day one** — those are shipped data, verifiable against published checksums,
and they are normally six weeks of authoring. 🔴 **Do not promise instructional effect.** The
dataset's own teaching-research layer is **agent-authored, unverified for this release, covers
1,051 of 1,591 topics** and describes itself as *"research-informed proposals, not empirically
validated interventions."* **English, History, Computing, Life Skills, PSD and Learning to Learn
have zero research records**, and the file says so per subject. Quote the coverage table; it is a
better slide than a claim.

🟢 **The one-slide pitch this variant unlocks, for North America and EMEA literacy mandates.**
The entire **`Computing` subject is AI literacy — 21 topics, ages 5–11**, sequenced, age-banded
and assessment-ready: *Smart Versus Not-Smart Devices*, *Voice Assistants and How They Work*, *AI
Mistakes and Limitations*, *Recommendation Systems and Filter Bubbles*, *Bias in AI Systems*, *AI
Data Collection and Privacy*, *Deepfakes and AI-Generated Content*, *Designing Fair AI Rules*,
*AI and the Future of Work*, *AI and the Environment*. **Against California AB 2876, Utah H.B.
273, Illinois HB 316 and the EU AI Act Article 4 staff-literacy duty**, that is a curriculum a
district can adopt rather than commission. 🔴 **It stops at age 11 and HB 316 is grades 6–12 —
scope and price the upper-secondary extension explicitly rather than letting it be assumed.**

🔴 **The licence check to run before the proposal goes out.** Four curricula ship **codes only**
(NGSS K-5, NGSS MS, C3 Social Studies, IB PYP PSPE) and **Common Core ships in full but under the
purpose-limited CCSS Public License, not ODbL.** **NGSS is a WestEd trademark with a
sample-approval requirement for commercial use.** The topic→standard *links* are unaffected, so
*"this lesson aligns to NGSS 1-ESS1-1"* is fine everywhere; **rendering the text of 1-ESS1-1 is
not.** Read `PROVENANCE.md`, and if the client needs verbatim text, clear it upstream — the
dataset's export tool takes a per-source switch for exactly that case.

**Estimate:** 3–4 weeks to a working mastery tutor on top of P1 or P2 — the shortest curriculum
path in this file, because **the spine is the part that is already built.** Most of the time goes
into step 6.

---

---

## The cross-cutting risk, re-stated in pass 319 — and now with a real alternative

**Eight of these ten patterns cross the LMS boundary through `dmitry-viskov/pylti1.3`: one MIT
library, re-verified in pass 319 at 138 stars, 84 forks, 178 commits, a single maintainer, 39 open
issues and still no published release.** It is the most load-bearing and least redundant component in this KB's architecture, and
pass 317 is the first pass to say so out loud.

It is good software — it covers the whole LTI Advantage surface (Deep Linking, AGS, Names and Roles,
Course Groups, Submission Review, Data Privacy Launch), which is why every pattern leans on it. The
risk is not quality, it is concentration. **Name it in the risk section of any SOW that depends on
it**, and know the fallbacks — which pass 318 made specific. `1EdTech/ltibootcamp` indexes LTI 1.3
implementations across seven languages: **`ltijs` and Atomic LTI Worker (Node)**, **OAT's core /
Deep Linking / Names & Roles libraries and a Symfony bundle (PHP)**, **UOC's library and Spring
Boot library (Java)**, **`LtiAdvantagePlatform` (.NET)**, **Atomic Jolt's starter app (Ruby)**,
**Atomic Forge (Rust)**, and `django-lti` alongside `pylti1.3` itself (Python). `ltijs` is the
route `blamb/lti-tutor` took to working deep linking and AGS passback against Moodle.
**Caveat before you scope on any of them:** that index carries no LICENSE file, its newest content
folder is `europe_tech_2020`, and its own README says the entries "have not been vetted" — verify
each against its repository. And **P8 avoids the dependency entirely.**

**Pass 319 found the alternative itself, not another index: `tsugiproject/tsugi` — Apache-2.0,
376 ★, 266 forks, 4,011 commits, Apereo Incubating**, maintained around the co-author of the LTI
specification, with an IMS ContentItem app store and low-level IMS libraries shared with Sakai.
Against 178 commits and one maintainer that is a different class of dependency. **Two caveats
before it goes in a SOW:** it is **PHP**, and **its GitHub page does not state which LTI versions or
Advantage services it implements** — verify the Advantage surface against the repository and the
Tsugi documentation first. Also recorded for breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229
commits)** covers **SCORM 1.2 and 2004** for the large installed base of courseware LTI does not
reach — **AICC was removed in v3.0.0 and cmi5/xAPI are roadmap "potential" only**, so promise
neither.

---

## The "prove it teaches" stage, specified — what to actually test, pass 323

p322 added a *prove it teaches* stage to P1 and pointed at MathTutorBench. **Pass 323 read four
2026 education benchmarks and the stage can now be specified as test cases rather than a gesture.**
Three of the four have **no public code** and the fourth has **no licence** (`intel/trends.md`), so
**this stage is something an engagement builds** — but the findings tell you exactly what to build.

**Run these four checks, in this order, on any tutor deliverable:**

1. **Pedagogy, scored without an LLM judge.** MathTutorBench's task shapes — problem solving,
   socratic questioning, solution correctness, mistake location, mistake correction, plus the
   pedagogy win-rate tasks — scored against ground-truth teacher utterances. **Never report an
   LLM-judged helpfulness score as evidence of learning**; the leakage audit
   (`bydeng01/conv-vs-ped-tutor`) exists because a judge will reward a tutor for handing over the
   answer.
2. **Demographic fairness, on the cues that actually move** — **language and immigration background
   first, then first-language, then SES, then gender.** EduFair-Bench's finding is that **language
   and immigration cues produce larger gaps than gender and SES**, which is the reverse of most
   fairness test plans. **And because capability and fairness are largely orthogonal, do not accept
   a model upgrade as a fairness remediation** — re-test after every model change.
3. **Adversarial safety with teacher personas, not generic jailbreaks.** EduGuardBench's shape:
   persona-based prompts targeting **academic misconduct** specifically, scored by attack success
   rate **and** a three-tier refusal-quality assessment. **Grade refusals, do not just count
   them** — its *Educational Transformation Effect* shows the best outcome is a refusal that becomes
   a teachable moment, and that capacity is **strongly negatively correlated with attack success
   rate.** A tutor that refuses bluntly and a tutor that redirects into learning score the same on a
   binary refusal metric and are not the same product.
4. **Model selection, tested rather than assumed.** Two results overturn common assumptions:
   **safety is not monotonic in model size** (mid-sized models were most vulnerable), and
   **education-specialised models led neither education module** of ELBench's nine-model comparison.
   **So: no "we used a bigger model" safety argument, and no domain-tuned-model premium without a
   head-to-head on the client's own tasks.**

**Discipline, borrowed from the two pre-registered audits and non-negotiable if the number will
appear in a bid:** pre-register the comparison, **freeze the dataset and hash it** before analysis
runs, separate registered diagnostics from post-hoc analysis, and keep a decisions log. The
`ability-levels-audit` headline is the warning — **difference-in-differences on a censored rating
scale can manufacture an effect that is not there**, and that is the shape of most tutoring-uplift
claims a client will be shown.

**Sellable on its own:** 3–4 weeks as an evaluation engagement over a client's existing tutor,
whoever built it. **It is the cheapest credible entry point in this KB**, and after this pass it is
the one with the clearest external references.

## Pattern selection by region

| Region | Lead with | Why |
|---|---|---|
| Greenfield / no incumbent LMS (any region) | **P8** | Apache-2.0 OpenOLAT removes the LTI boundary; one deployable, 2–3 weeks less build |
| North America | **P9 first**, then **P3 + P6**, then P7 where restricted, then P1/P2 | **P9 leads because the amended COPPA Rule has been in force since 2026-04-22 and most deployed K-12 AI is likely non-compliant** — it sells into the installed base rather than competing with a frontier-model seat licence. Then the dated policy requirements (Ohio 2026-07-01, NC model policy 2026-12-31, Idaho SB 1227, 134 bills/31 states); governance is the budgeted line and the roster spine is now open source |
| EMEA | **P4**, with **P8** where sovereignty decides the deal | Provider-side conformity under Annex III; Article 50 live, watermarking and new prohibitions both land 2026-12-02, 2027-12-02 the real deadline. OpenOLAT is the only permissive, EMEA-authored, EMEA-maintained LMS in this KB |
| EMEA — Gulf | **P1/P2 with Arabic-first localisation** | UAE ~28% of GCC edtech, National AI Strategy 2031; incumbents (Alef, Classera, Abwaab) are proprietary and buying integration, not platforms |
| EMEA — Africa | **P5** | Strongest low-resource evidence base in the world (Edo State, EIDU); DigiSchool tablets are installed hardware needing content |
| APAC | **P10 Variant B + P5** (India), P1 + labelling (China), P1 (Japan), **P4 ported** (South Korea) | Curriculum mandate plus infrastructure gap — **and pass 319 found the curriculum *data* gap under it: 180 NCERT/CBSE repositories and no verified dataset**, so the spine is a build, not a dependency. China needs labelling/registration at the generation step; Japan has the fewest blockers; **Korea's Framework Act on AI is in force since 2026-01-22 and names student evaluation as high-impact**, so the EMEA conformity file sells there now — and the 2025 AI-textbook reversal means every Korean and regional buyer is bidding on deployment risk, not capability |
| APAC — Australia / NZ | **P7**, then P1 | Ipsos 2026 finds ANZ public support for banning AI in schools *higher* than in Asian markets — closer to the US restriction posture than to the rest of APAC |
| LATAM — Brazil | **P10 Variant A**, then P2, with P4's artefacts ported | **The only jurisdiction with a verified open curriculum dataset, an MCP server over it and a published grounding measurement (31.9% → 2.3%)**, plus a 34,948-commit municipally originated SIS with no AI in it. Brazil's June 2026 AI/tech agreement with the EU means the conformity file transfers, and PL 2338 is risk-based |
| LATAM — Spanish-speaking | **P2**, with P4's artefacts ported, and P10 as a build | No equivalent curriculum data layer was found in the Spanish-language topic sweep, so P10 here is Variant B work. The 92%-usage / 30%-satisfaction gap and the 50/19 feedback gap are delivery problems, which P2 answers |
| Any region, no jurisdiction mandate — international schools, B2C, corporate foundations, pre-ministry pilots | **P10 Variant D + P13** | **New in p326.** The cross-national spine (`os-taxonomy`: 1,591 topics, 3,225 edges, seven curricula, ODbL + CC BY-SA) ships sequencing, age banding and 1,591 assessment prompts on day one, so the curriculum build that gates Variants A–C disappears. **P13 is not optional beside it** — it is what keeps the share-alike database outside a proprietary product. Strongest where a *literacy* mandate is the buying motion (Illinois HB 316, California AB 2876, Utah H.B. 273, EU AI Act Art. 4): the entire Computing subject is 21 AI-literacy topics, ages 5–11. **Age band stops at 11 — price the upper-secondary extension.** |

**P13, new in p326, is the second pattern selected by a *requirement* rather than a region, and the requirement is a licence.** It applies wherever the asset the client most wants is published under share-alike terms — which, since the sector's largest open curriculum graph is ODbL-1.0, is now the common case rather than the awkward one. 🔵 **Read it before quoting any engagement that consumes external data: it is three to five days designed in at the start and a bad week retrofitted.**

**P11, new in p324, is the first pattern in this file that is selected by a *requirement* rather
than by a region or a starting position** — it applies wherever assessment integrity is a stated
obligation, which on this pass's evidence is all four regions with a different statute behind it in
each: human-oversight mandates in North America (Oklahoma, Maryland, California AB 1159), high-risk
assessment duties under the EU AI Act in EMEA, Vietnam's *"sole basis … without meaningful human
review"* carve-out in APAC, and the 87%-use / 26%-strategy institutional gap in LATAM. **Lead with
it wherever the buyer has already written an integrity policy and has nothing to implement it
with**, and pair it with **P3** in North America, where it is the same governance sale.

**No pattern here is LATAM-only or North-America-only.** P1 and P2 are the portable core; P3, P4,
P5, P6, P7 and P9 are the regional wrappers that make them biddable. **P10 is portable in method and
regional in data** — Variant A is a Brazilian assembly job, Variant B is the same recipe anywhere a
curriculum is published and not yet machine-readable, which on this pass's evidence is everywhere
else. **P8, new this pass, is the only
one selected by the client's starting position rather than by region** — it applies wherever there
is no incumbent LMS, and it is strongest in EMEA because sovereignty and a permissive European
platform happen to answer the same objection.

**For LATAM specifically, pass 317 sharpened the pitch without needing a new pattern.** UNESCO
IESALC (2026-09-09; 200 institutions, 19 countries) found **87% of LAC higher-education institutions
using AI and only 26% with a formal AI strategy** — a 61-point gap, with adoption driven by
individuals rather than institutions. That is P3's governance deliverable with the compliance driver
swapped for an institutional-risk driver, and it is the same work this KB already sells in North
America.
