---
industry: education
region: Global
updated: 2026-10-13
---

## Pass 178 — 2026-10-13

🆕 🟢 **`ACTION KT` is DISCHARGED, LIMB `1` FIRED, and `gap 134` is CLOSED.**
[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) — the Technical University of Munich's
interactive-learning platform, and the last fully unverified holder-grade row in this KB — was
cloned and read artefact by artefact. 🟢 **Both limbs of the pre-registered falsifier were put to
the same clone, and limb `1` fires on every criterion it names: it reaches exercise, exam and
assessment objects with WRITE access, through its OWN auth, over data it OWNS.**
🆕 🟢 **The number that settles the *"thin front end"* question: `257` `@Entity` classes and `137`
Liquibase changelogs.** 🔵 **`eagles-edu/sis` was refused at p175 because it was a portal over
somebody else's system of record. `Artemis` IS the system of record — it ships its own schema and
migrates it.**
🆕 🟢 **The finding with the most commercial value in this file: `Artemis` is the first row in this
KB that speaks a real interop standard as a TOOL, with grade passback.** `LTI` at word-boundary
precision in `248` files, its own module at `.../artemis/lti` with `47` files, `Lti13Service`,
`Lti13Configurer`, `Lti13DeepLinkingResponse`, `Lti13AgsClaim`, `DeepLinking` `60`×, AGS `305`× —
**and `NightlyLtiMoodleInteropTest.java` with a `moodle-sign-jwt.php` fixture, so the Moodle
interop is TESTED, nightly, in CI.** 🔴 **And it speaks exactly ONE: `SCORM` `0`, `xAPI` `0`,
`QTI` `0`, `OneRoster` `0`, `Ed-Fi` `0`, `Caliper` `0`.**
🆕 🔴 **The `T265` trap fired again and was caught again: `canvas` matches `45` files, and
`canvas-lms`, `instructure` and `Canvas LMS` match `0`.** 🔵 **Same shape as `dolos`: every hit is
the HTML5 element. A narrower grep would have published *"Canvas-integrated"* for the second pass
running.**
🆕 🟡 **`QTI` is a second trap, and it is instructive about scope.** `0` hits in `src` across
`.java`, `.ts` and `.yml`; a repository-wide grep returns `5`, and all `5` are a `.zip`, an emoji
PNG sheet, a `.webm`, a system-design PNG and the project's own LMS-comparison data file.
🔵 **`T276` again: the scope-limited grep is the HONEST one here, and the wide grep is the one that
would have published a standard this platform does not implement.**
🆕 🟢 **A second EMEA institutional row ENTERS, because `Artemis` cannot be routed without it being
named:** [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), the LLM microservice. 🔴 **`12`★,
and that is the risk sentence, not a footnote.**
🟢 **No other rows enter. `gap 134` closed by verification, not by admission.**

### 🟢 The `7` rows — RE-STATED, with `Artemis` verified and `Pyris` admitted

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 130` B *(EXACT, `md5 37cd0f927f3fdf7f68cf09edaebfb010`)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` *(on `master`)* | 🟡 **North America** — subnational grade (`ACTION KK`) | 🟢 **YES — `ACTION KM`, p176** |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 091` B, `md5 021aaec73f7b974dc5edf4ef703f941b` *(🆕 identical on `main` AND `develop`)*, *"© 2026 TUM Applied Education Technologies"* | 🆕 **`develop@8c158741c38e`** 🔴 *(and `main@07f43f8e0b71` is a DIFFERENT commit; `develop` moved to `6aae3ae2655c` during this pass)* | 🟢 **EMEA** — HOLDER-grade, Germany | 🆕 🟢 **YES — `ACTION KT`, in full below. `13 810` files, `5 172` Java, `4 135` TS, `3 963` test files, `v10.3`** |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 084` B, `md5 00ffc342d555c4129ee54e3286818d50`, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` — 🟢 **unmoved since p175** | 🟢 **EMEA** — HOLDER-grade, Belgium | 🟢 **YES — `ACTION KQ`, p177** |
| 🆕 🟡 [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | 🟢 **`MIT`** — `1 089` B, `md5 5cc3b9844f092545a99800eb9edce880` | `d7b2c095204e` | 🟢 **EMEA** — HOLDER-grade by LINEAGE *(same `ls1intum` org as `Artemis`)* | 🔴 **NO — licence, `md5` and `HEAD` only. 🔴 `12`★, `16` open issues, last push `2026-09-17`: the smallest dependency this KB has ever put on a critical path** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B *(EXACT, `md5 99b58b5c4e30de12e69228065a5bd553`)*, *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` *(on `master`)* | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — grant-path probe only** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 083` B, `md5 9633492b4368ec2c3f77f7116694ad23`, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only; the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 073` B, `md5 2a1660298c8c5a8b41d28eed30f7fde2`, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🟢 **`gap 134` is CLOSED: `0` fully unverified holder-grade rows remain.** `cs-field-guide` is still
only partly read and `Pyris` is new and unread, so **`3` of `7` rows are verified past their
licence** — `canvasapi`, `Artemis`, `dolos`. 🔵 **Three passes, three rows read, two new admissions
in total: the debt is being paid down faster than it is taken on, which is the first time that
sentence has been true in this file.**

### 🆕 🟢 `ACTION KT` — `ls1intum/Artemis` read past its licence, artefact by artefact

🟢 **Controlled: cloned `--depth 1 --single-branch`, which lands on the DEFAULT branch `develop`,
at `8c158741c38e1fd684b38dc6eb54993b1731af89`. `13 810` tracked files, `5 172` `.java`, `4 135`
`.ts`, `3 963` test files, `version = "10.3"`, `JavaLanguageVersion.of(25)`, `node >=24.21.0`.**
🔴 **p177 recorded `HEAD` `09266581a02c`. A `--depth 1` clone cannot reach that object, so this pass
can neither confirm nor place it on a branch, and this repository has two live branches whose heads
differ.** 🔵 **Every count below is a reading of `develop@8c158741c38e` and is labelled as such
(`T281`).**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **grant-path exclusivity** | `LICENSE`, `MIT`, byte- and `md5`-identical on `main` and `develop` | 🟢 **one grant, and branch-independent** |
| 🟢 **does it OWN the data?** | `257` classes carrying `@Entity`; `137` Liquibase/changelog paths | 🟢 **SYSTEM OF RECORD. This is limb `1` and limb `2`'s refutation in one measurement** |
| 🟢 **exercise and exam DOMAIN objects** | `74` files under `**/domain/**` matching exercise/exam, among them `Exam`, `StudentExam`, `ExamSession`, `ExamUser`, `ExerciseGroup`, `ExamRoom`, `Exercise`, `BaseExercise`, `Result`, `GradeStep`, `ExampleSubmission` | 🟢 **the objects the falsifier named, by name** |
| 🟢 **WRITE access to them** | repository-wide `@PostMapping` `261`, `@PutMapping` `143`, `@PatchMapping` `21`, `@DeleteMapping` `103` against `@GetMapping` `538`. In the exam/exercise/assessment web layers specifically: exam `21`/`7`/`8`, exercise `8`/`15`/`7`, assessment `14`/`7`/`7` | 🟢 **`528` write endpoints. Not a read-only front end** |
| 🟢 **its OWN auth** | `@PreAuthorize` in `24` files, `SecurityConfiguration` `9`, `jwt` `63`, **`passkey` `136`**, `saml2` `54`, `oauth2` `26` | 🟢 **own auth, and a passkey surface larger than its JWT surface — unusual and worth a slide** |
| 🟢 **interop — `LTI`, word-bounded** | `248` files; own module `.../artemis/lti` with `47` files; `Lti13Configurer` `27`, `Lti13LaunchRequest` `14`, `Lti13Service` `12`, `Lti13PlatformConfiguration` `12`, `Lti13ClientRegistration` `12`, `Lti13DeepLinkingResponse` `12`, `Lti13TokenRetriever` `9`, `Lti13AgsClaim` `9`, `DeepLinking` `60`, `ags` `305` | 🟢 **`LTI 1.3` as a TOOL, with Deep Linking and Assignment-and-Grade-Services — it can receive a launch AND push grades back** |
| 🟢 **LMS integration, TESTED** | `src/test/java/.../lti/nightly/NightlyLtiMoodleInteropTest.java` + `src/test/resources/lti/nightly/moodle-sign-jwt.php`; `moodle` in `10` files | 🟢 **a nightly interop test against a REAL LMS. `dolos` has `0` LMS integration; this row has one in CI** |
| 🔴 **every OTHER standard** | 🔴 **`SCORM` `0`, `xAPI` `0`, `QTI` `0` *(in `src`)*, `OneRoster` `0`, `Ed-Fi` `0`, `Caliper` `0`** | 🔴 **one standard only. Rostering and learning-record plumbing stay integrator work** |
| 🟡 **`canvas` — the trap, caught** | `45` files case-insensitively; `canvas-lms`/`instructure`/`Canvas LMS` **`0`** | 🟡 **`T265` fired as designed, for the second consecutive pass on a different subject** |
| 🟢 **the AI surface** | `Iris` `748` files *(own module, `254` files)*, `Hyperion` `231`, `Athena` `187`, `pyris` `219`, `llm` `193` | 🟢 **this is not an LMS with AI bolted on; the AI surface is `~5`% of a `13 810`-file tree and has its own modules** |
| 🟢 **what `Hyperion` DOES** | its own admin doc: consistency checks on problem statements, rewriting instructions, **verified exercise-variant generation** *(programming variants verified with real template and solution builds; quiz variants by validity-checking generated questions)*, MCQ generation from a topic or from competencies, bulk MCQ refinement | 🟢 **AI AUTHORING with a verification step — the thing most authoring tools skip** |
| 🟢 **deployment dependency, measured not assumed** | the same doc: *"The functionality is provided by Artemis and Spring AI, so no EduTelligence service needs to be deployed"*; `Pyris` is *"used only for semantic lecture search"* and quiz generation *"falls back gracefully"* without it | 🟢 **`Hyperion` needs an LLM endpoint, NOT the microservice. 🔵 This is the single most budget-relevant sentence in the artefact** |
| 🟡 **model providers named** | `openai` `103`, `gpt-5` `27`, `azure` `13`, `ollama` `10`, `gpt-4o` `3`; `spring.ai.openai` `7` config keys against `spring.ai.model` `1` | 🟡 **OpenAI/Azure is the paved road. `ollama` appears in the Iris test stack and in the Weaviate global-search config, so a local path EXISTS and is not the default** |
| 🔴 **adjudication** | `AutomaticAssessment` in `14` files, `automatic` `378`, `score` `581`, `feedback` `720` | 🔴 **IT ADJUDICATES. This is the opposite of `dolos`, and it is the whole regulatory difference — see [`intel/trends.md`](../intel/trends.md)** |
| 🟢 **proctoring and biometrics** | 🟢 **`proctor` `0`, `webcam` `0`, `emotion` `0`, `face` `2`** — what exists instead is `ExamSession` `21` and `SuspiciousExamSessions` `15`, i.e. session-level anomaly detection | 🟢 **NO biometric surveillance. It stays clear of the Article `5` emotion-recognition PROHIBITION entirely, which is a harder bar than Annex III** |
| 🟡 **privacy regimes named** | `GDPR` `42` files, `DSGVO` `5`, 🔴 **`FERPA` `0`** | 🟡 **EMEA-native by construction. A North America engagement writes the FERPA story itself** |
| 🟢 **deployability** | `deployment/docker/docker-compose.yml`, plus an `iris-stack/docker-compose.yml` for the AI path in tests; `10` docker paths | 🟢 **compose-deployable, with a separate compose file for the AI stack** |
| 🟡 **liveness** | `818`★, `396` forks, `256` open issues, and `develop` moved **during this pass** | 🟡 **very much alive — and fast enough that a pinned SHA is mandatory in any engagement, not optional** |

🟢 **Verdict: `Artemis` ROUTES, and it is the strongest row in this KB.** It is institution-held,
`MIT`, a system of record, AI-native with a verification step, `LTI 1.3` with grade passback, and
nightly-tested against Moodle. 🔴 **Four conditions travel with it and none is optional in a deck:**
**(`1`)** it ADJUDICATES, so in the EU it is an Annex III stand-alone high-risk system and the
conformity work is real *(timing in [`intel/trends.md`](../intel/trends.md))*; **(`2`)** it speaks
ONE standard — no rostering, no SCORM, no xAPI; **(`3`)** `FERPA` is named nowhere, so a US
deployment inherits that work; **(`4`)** the AI path's default provider is OpenAI/Azure, and the
self-hosted limb runs through a `12`★ microservice.
🟢 **Full artefact ledger:**
[`evidence/artemis-artefact-read.2026-10-13-p178.tsv`](../evidence/artemis-artefact-read.2026-10-13-p178.tsv).

## Pass 177 — 2026-10-13

🆕 🟢 **`ACTION KQ` is DISCHARGED and the row a client asks about first is now read past its
licence.** [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) — Ghent University's
source-code similarity detector, the only assessment-integrity route this KB holds — was cloned at
its recorded `HEAD` and read artefact by artefact. 🟢 **Both of the things p176 named as UNVERIFIED
are now measured, and both come out better than the row claimed.**
🆕 🟢 **Language coverage: `20` programming languages in the registry and `19` vendored
`tree-sitter` grammars, against a docs page that lists `11` and trails off in an ellipsis.** 🔵 **The
project undersells itself by `9` languages, `Modelica`, `Verilog`, `R`, `Groovy`, `Scala` and
`OCaml` among them — which is the difference between a CS-department tool and one that reaches an
engineering faculty.**
🆕 🟢 **False-positive behaviour: it has none of the machinery a client will ask about and that is
the correct answer.** `falsePositive` **`0`**, `confidence` **`0`** across the whole repository.
🟢 **What ships instead is template exclusion — `-i/--ignore`, plus `-m/--max-fingerprint-count`
and `-M/--max-fingerprint-percentage` to detect shared code automatically — and the docs state the
problem in their own words before offering the controls.**
🔴 **The core engine's `defaultMinSimilarity` is `0`: it filters nothing unless told to.** The only
threshold lives in the report UI and is **GUESSED** (`guessSimilarityThreshold`, a local minimum
floored at the mean of pairwise similarities), and single-linkage clustering drops edges beneath it.
🔵 **So `dolos` reports similarity and clusters; it never returns a verdict. That is decision
support, not adjudication, and it is the single most useful sentence in this file for a `2026`
education engagement — see [`intel/trends.md`](../intel/trends.md) for why the regulation agrees.**
🆕 🔴 **`ACTION KS` invalidates a COLUMN of this table rather than a row: `8` of `12` published
licence byte counts in this KB are short by exactly `1` byte**, including `4` of the `6` rows below.
🟢 **Corrected figures are published inline and marked; the mechanism and the full audit are in
[`agents/top.md`](../agents/top.md) and
[`evidence/licence-byte-audit.2026-10-13-p177.tsv`](../evidence/licence-byte-audit.2026-10-13-p177.tsv).**
🟢 **No new rows ENTER this pass, for the second pass running and for the same stated reason:
`gap 134` is a debt of verification, and admitting rows while it is open makes it bigger.**

### 🟢 The `6` p175 rows — RE-STATED, with byte counts CORRECTED and verification state explicit

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 130` B *(🆕 CONFIRMED exact; `md5 37cd0f927f3fdf7f68cf09edaebfb010` reproduced independently)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | 🟡 **North America** — subnational grade (`ACTION KK`) | 🟢 **YES — `ACTION KM`, p176** |
| 🟡 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — 🆕 **`1 091` B** *(CORRECTED from `1 090`; `md5 021aaec73f7b974dc5edf4ef703f941b`)*, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — licence, holder and `HEAD` only. The LAST fully unverified holder-grade row (`gap 134`)** |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — 🆕 **`1 084` B** *(CORRECTED from `1 083`; `md5 00ffc342d555c4129ee54e3286818d50`)*, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` — 🟢 **unmoved since p175** | 🟢 **EMEA** — HOLDER-grade | 🆕 🟢 **YES — `ACTION KQ`, in full below. `513` files, `57` test files, `103` test declarations** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B *(🆕 CONFIRMED exact — read by a non-stripping channel, which is part of `ACTION KS`'s proof)* , *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — grant-path probe only** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — 🆕 **`1 083` B** *(CORRECTED from `1 082`)*, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only; the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — 🆕 **`1 073` B** *(CORRECTED from `1 072`)*, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🟢 **`gap 134` narrows from `3` unverified holder-grade rows to `2`** — `Artemis` outright, and
`cs-field-guide` partly. 🔵 **Two passes, two rows read past their licence, no new admissions: the
debt is being paid down rather than refinanced.**

### 🆕 🟢 `ACTION KQ` — `dodona-edu/dolos` read past its licence, artefact by artefact

🟢 **Controlled: cloned at `HEAD` `44925b867ce737206c1debce0add731e294025d5`, the sha this KB
recorded at p175, UNMOVED. `513` tracked files, `57` test files, `103` test declarations.**
🔵 **The rule, per `T265`: do not count the standard's NAME. Count the route that would have to
exist — and check what each token is actually matching before reporting it.**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **grant-path exclusivity** | `LICENSE` only. `LICENCE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` all `404` at the `14` B body | 🟢 **one grant, unambiguous** |
| 🟢 **language coverage — registry** | `LanguagePicker.languages` declares `21` entries: `20` programming languages + a `char` tokenizer | 🟢 **MEASURED** |
| 🟢 **which languages** | `bash` `c` `cpp` `c-sharp` `python` `php` `modelica` `ocaml` `java` `javascript` `elm` `go` `groovy` `r` `rust` `scala` `sql` `typescript` `tsx` `verilog` | 🟢 **`20`, and `6` of them are not in the docs** |
| 🟢 **vendored grammars** | `19` `tree-sitter` grammar directories under `parsers/` | 🟢 **ships its own parsers; no install-time fetch** |
| 🔴 **the docs' own claim** | `docs/about/languages.md` lists `11` and ends in *"..."* | 🔴 **UNDERSELLS BY `9`. Quote the registry, never the docs page** |
| 🟡 **prose, not just code** | `CustomTokenizerLanguage("char", [".txt", ".md"])` via `charTokenizer.ts` | 🟡 **NOT code-only — but character-level. 🔴 Do NOT sell this as essay plagiarism detection** |
| 🟢 **the false-positive problem, named** | `docs/docs/running.md:55` — *"Dolos will often detect these code fragments as similar and include them in the similarity score, making it harder to spot actual plagiarism."* | 🟢 **the project names it before it sells the cure** |
| 🟢 **false-positive control `1`** | `-i` / `--ignore <path>` — a template/boilerplate file whose fragments stop counting toward similarity | 🟢 **ships** |
| 🟢 **false-positive controls `2` and `3`** | `-m/--max-fingerprint-count <int>` and `-M/--max-fingerprint-percentage <fraction>` — auto-detect shared code by how many files a fragment occurs in; combinable with `-i` | 🟢 **ships, and automatic** |
| 🔴 **engine default** | `options.ts:54` — `defaultMinSimilarity = 0` | 🔴 **filters NOTHING out of the box. An unconfigured run is the noisy run the docs warn about** |
| 🟡 **the threshold** | report UI only: `guessSimilarityThreshold` in `web/src/api/utils/cutoff.ts` — a local minimum, floored at the mean of pairwise similarities; `SingleLinkageClustering` drops edges below it | 🟡 **GUESSED per dataset, not a policy you set. Say so before a client calls it a standard** |
| 🟢 **adjudication** | `falsePositive` `0`, `confidence` `0`, no pass/fail anywhere in `513` files | 🟢 **DECISION SUPPORT, not an adjudicator — and see `intel/trends.md`: this is what makes it routable under Annex III and the US oversight statutes** |
| 🔴 **STANDARDS interop, word-boundary** | 🔴 **OneRoster `0`, Ed-Fi `0`, SCORM `0`, xAPI `0`, Caliper `0`, LTI `0`, QTI `0`** | 🔴 **none. Same shape as `canvasapi`: it speaks its own platform, not a standard** |
| 🔴 **privacy regimes named** | 🔴 **`FERPA` `0`, `GDPR` `0`** | 🔴 **names neither. The data-protection story is the integrator's to write** |
| 🔴 **LMS integration** | 🔴 **Canvas `0` in the product sense, `Moodle` `0`, `webhook` `0`** | 🔴 **NONE. Wiring it into an LMS is custom work — budget it** |
| 🟡 **`canvas` — the trap, caught** | `29` case-insensitive hits, **`0`** of them Canvas LMS: every one is the HTML5 `<canvas>` element or `D3` rendering, and `Canvas LMS`/`canvas-lms`/`instructure` match `0` | 🟡 **`T265` fired exactly as designed. A narrower grep would have published *"Canvas-integrated"*** |
| 🟡 **home platform** | `Dodona` — `193` hits | 🟡 **built for Ghent's own platform; that is the integration it has** |
| 🟢 **deployability** | `Dockerfile.cli`, `Dockerfile.web`, `docker-compose.yml`, `docker` `114` hits | 🟢 **deployable as CLI or as a web report** |

🟢 **Verdict: `dolos` ROUTES, and it is stronger than the row that admitted it on language coverage
and honest on everything else.** 🔴 **Two conditions travel with it: there is NO LMS integration of
any kind, and it returns NO verdict.** 🔵 **The second condition is a feature. The first is a line
item.**
🔴 **A method note recorded against this pass's own work: the first run of this probe grepped only
`lib/`, `cli/` and `docs/` and was about to publish *"`threshold` `0`"* and *"`cluster` `0`"*. Both
are false — `16` and `178` hits repository-wide. 🔵 **A scope-limited grep reports the scope, not
the repository (`T276`), and it fails in the direction that makes the finding sound sharper.**
🟢 **Full artefact ledger:**
[`evidence/dolos-artefact-read.2026-10-13-p177.tsv`](../evidence/dolos-artefact-read.2026-10-13-p177.tsv).


## Pass 176 — 2026-10-13

🆕 🟢 **One of p175's four holder-grade rows has now been read PAST its licence, and it is better
than the row claimed.** `ACTION KM` applied `T265`'s rule — name the artefact that would have to
exist and look for THAT, not for the standard's name — to
[`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi). 🟢 **It reaches rostering objects with
READ AND WRITE, carries its own auth model, paginates properly and raises typed errors.**
🔴 **`ACTION KM`'s falsifier limb `1` therefore FIRES, and `gap 123` closes for the administrative
layer — conditionally, and the condition is the whole finding: it is a CLIENT, and the system of
record it clients for is Canvas, whose own core is not permissive.**
🆕 🔴 **`ACTION KJ` converted `0` licence verdicts and found a bigger defect than the one it was
sent for.** No repository this KB ever recorded as grant-free carries a grant at a British spelling
— `0` of `16` paths on each of four subjects. 🔴 **But the probe-list census underneath that answer
is the finding: this repository contains `76` independent hardcoded grant-path lists. `48` carry
`LICENCE`. `3` carry `COPYING.md`.** 🔵 **The defect was never a spelling. It is that the list is
copied `76` times and cannot be extended (`T272`).**
🟢 **No new rows ENTER this pass, and that is deliberate.** p175 admitted six on a licence read and
registered `gap 134` against itself for doing so; p176 spends the pass verifying one of them instead
of admitting more. 🔵 **One row read past its licence is worth more than six read up to it.**

### 🟢 The `6` p175 rows — RE-STATED, with the verification state of each made explicit

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — 🆕 **`1 130` B** *(p175 said `1 129`; blob `f105f1b3670d`, `md5 37cd0f92…`)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | 🟢 **North America** — 🆕 🟡 **subnational grade, see `ACTION KK`** | 🆕 🟢 **YES — `ACTION KM`, in full below** |
| 🟡 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 090` B, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — licence, holder and `HEAD` only (`gap 134`)** |
| 🟡 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — and it is the row a client will ask about first, because it is the only assessment-integrity route here** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B, *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — it served as `ACTION KJ`'s known positive and reproduced at `1 128` B on `master`** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 082` B, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only, and `ACTION KK` downgrades it further: the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 072` B, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🔴 **So `gap 134` narrows from `4` unverified holder-grade rows to `3`, and does not close.**

### 🆕 🟢 `ACTION KM` — `ucfopen/canvasapi` read past its licence, artefact by artefact

🟢 **Controlled: `HEAD` `513588f3077f`, `318` tracked files, `158` Python, `76` test files,
`1 112` test methods.**
🔵 **The rule, per `T265`: do not count the standard's NAME. Count the route that would have to
exist.**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **rostering objects as modules** | `enrollment.py`, `enrollment_term.py`, `section.py`, `course.py`, `user.py`, `account.py`, `grading_period.py` — all PRESENT | 🟢 **reaches them** |
| 🟢 **rostering routes, as named request strings** | `courses/{}/enrollments`, `courses/{}/enrollments/{}`, `/accept`, `/reactivate`, `/reject`, `courses/{}/sections`, `sections/{}/enrollments`, `enrollment_terms`, `sections/{}/crosslist` | 🟢 **named, not inferred** |
| 🟢 **WRITE reach** | 🟢 **`322` `GET`, `127` `POST`, `89` `PUT`, `74` `DELETE`** — and `courses/{}/enrollments` is addressed by `POST` at `course.py:748` as well as `GET` at `:1226` | 🟢 **writes. Compare `edfi-oneroster`: `24` `GET`s, `0` writes** |
| 🟢 **pagination** | `paginated_list.py` — `per_page` defaulting to `100`, a `_next_url` the iterator follows, `__getitem__` growing the list on demand | 🟢 **real, not a thin wrapper** |
| 🟢 **auth model** | `requester.py:187` — `Authorization: Bearer {access_token}`, token held on the requester | 🟢 **its own** |
| 🟢 **error semantics** | `CanvasException` + `BadRequest`, `InvalidAccessToken`, `Unauthorized`, `Forbidden`, `RateLimitExceeded`, `ResourceDoesNotExist`, `RequiredFieldMissing`, `Conflict`, `UnprocessableEntity` | 🟢 **typed, including rate limiting** |
| 🟡 **SIS identifier addressing** | `sis_course_id`, `sis_section_id`, `sis_account_id`, `sis_group_id`, `sis_import_id` | 🟡 **addresses objects by the SIS's OWN ids — interop at the identifier layer** |
| 🔴 **STANDARDS interop, word-boundary** | 🔴 **OneRoster `0`, Ed-Fi `0`, SCORM `0`, xAPI `0`, Caliper `0`.** `LTI` `7` | 🔴 **none. It speaks Canvas, not a standard** |
| 🟡 **activity** | last commit **`2026-04-16`** | 🟡 **`180` days — EXACTLY at this KB's liveness bar, which is why it appeared in p175's sweep at all** |

🟢 **Falsifier limb `1` FIRES: rostering objects AND its own auth model.** Limb `2` is SILENT — it is
not a thin generated wrapper by any of the three tests the action named.
🔴 **And the condition that must travel with the row, because without it the row oversells:**
`canvasapi` is a permissive CLIENT for a system of record that is not permissive. Instructure
publishes Canvas's core under `AGPL-3.0` and sells the operated product.
🔵 **So the honest sentence is: the administrative layer finally has an `MIT` client with write
reach and real auth — for institutions that already run Canvas.** It does not give this KB a
permissive SIS, and the row underneath it is still 🔴 **none** (fourteenth pass).

### 🆕 🔴 `ACTION KJ` — `0` verdicts converted, and a defect `19×` wider than the one registered

🟢 **The four subjects, every one of them a published absence claim in this KB, probed at `16` paths
on the default branch — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENCE.md`,
`LICENCE.txt`, `COPYING`, `COPYING.md`, `COPYING.txt`, `License`, `License.md`, `license`,
`license.md`, `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`:**

| subject | paths answering `200` | verdict |
|---|---|---|
| 🟢 [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | 🟢 **`0` of `16`** | 🟢 **verdict STANDS, and strengthens — see the branch enumeration below** |
| 🟢 [`os4ed/openSIS-Classic`](https://github.com/os4ed/openSIS-Classic) | 🟢 **`0` of `16`** | 🟢 **the *"no root grant"* verdict STANDS. Its `GPL-2.0` is still at `docs/License.txt` (`T209`)** |
| 🟢 [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`0` of `16`** | 🟢 **STANDS. `GPL-2.0` at `html/license.txt`, `9` languages, none named as governing (`gap 116`)** |
| 🟢 [`spdx/license-list-data`](https://github.com/spdx/license-list-data) | 🟢 **`0` of `16`** | 🟢 **STANDS. The canonical SPDX token list still publishes no licence of its own** |
| 🟢 **CONTROL — the known positive** [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`1` of `16` — `LICENCE`, `1 128` B** | 🟢 **the instrument is validated by a positive it was required to find, and it reproduced p175's byte count exactly** |

🆕 🟢 **And the word *"exhaustive"* is EARNED for the first time, on the row that was carrying it
without earning it.** p169's `T209` enumerated `Mr.-Ranedeer`'s default branch — `12` files, `0`
grants. 🟢 **p176 enumerated EVERY branch the remote advertises:**

| branch | tracked files | grant-shaped paths *(case-insensitive `licen[cs]e`/`copying`/`notice`)* |
|---|---|---|
| `main` | `12` | 🟢 **`0`** |
| `v2.6.2` | `12` | 🟢 **`0`** |
| `v2.6.3` | `13` | 🟢 **`0`** |
| `dev/v2.7` | `9` | 🟢 **`0`** |
| `Speedrun-Brother` | `9` | 🟢 **`0`** |

🟢 **`55` file-paths across `5` branches, `0` grants.** 🔵 **Before p176 the word meant *"the default
branch"*; now it means *"every branch the remote advertises"*, and the claim is the same claim.**

### 🆕 🔴 The probe-list census — why `gap 133` was the wrong shape

🟢 **`76` grant-path probe lists found in `compose/code/`, counted by the lines that enumerate two
or more grant paths together:**

| property | count | share |
|---|---|---|
| 🟢 carry `LICENSE` | `76` | `100%` |
| 🟡 **carry the British `LICENCE`** | 🟡 **`48`** | 🟡 **`63.2%`** |
| 🔴 **carry `COPYING.md`** | 🔴 **`3`** | 🔴 **`3.9%`** |

🔴 **`28` lists cannot find a British-spelled grant and `73` cannot find `COPYING.md`** — and
`p120-unread-grant-resolution/probe.sh` has carried `LICENCE LICENCE.md` all along, which is how
this KB found `cs-field-guide` in the first place.
🆕 🔵 **`T272` — a probe list copied `76` times is not a list, it is `76` lists, and extending it is
not an edit but a migration.** p175 wrote *"`P50`'s probe list misses `LICENCE`"*, which implies one
list and one fix. 🔵 **The fix is a shared vocabulary in `compose/code/lib/`, imported rather than
retyped, and `gap 135` registers it as the migration it is.** 🟢 **The reassurance that belongs next
to it: `0` published verdicts change, so this is debt, not error.**

## Pass 175 — 2026-10-13

🆕 🔴 **One row LEAVES this file and it is the one p174 admitted with the most confidence.**
`ACTION KE` read [`eagles-edu/sis`](https://github.com/eagles-edu/sis) past its licence, as
registered, by grepping the tree rather than the README — and found that **every interop and auth
signal it appeared to carry is a substring artefact.** 🔴 **Word-boundary count: `0` for OneRoster,
`0` for Ed-Fi, `0` for LTI, `0` for SCORM, `0` for xAPI, `0` for `tenant`, `0` for `tenancy`, and
`0` for OAuth, OIDC, SAML, JWT, LDAP and SSO.**
🆕 🟢 **Six repositories ENTER, and four of them are placed by the institution named in their own
licence body** — the strongest evidence class `P800` admits, and the first time this file has
obtained holder-grade institutional placement in three regions in one pass.

### 🆕 🟢 Entering — institutional, permissive, licence body READ this pass

| repo | licence *(body READ, bytes, holder)* | `HEAD` | ★ | region *(`P800`)* | what it is |
|---|---|---|---|---|---|
| 🆕 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 129` B, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | `682` | 🟢 **North America** — HOLDER-grade | a Python client for **Canvas LMS**: courses, users, gradebooks. The first rostering-ADJACENT permissive row this KB has ever been able to name |
| 🆕 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 090` B, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | `818` | 🟢 **EMEA** — HOLDER-grade | an institutional **interactive-learning platform with automated feedback**: programming, modelling and text exercises, autograding, an exam mode. A university's own teaching system, `MIT` |
| 🆕 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` | `350` | 🟢 **EMEA** — HOLDER-grade | **source-code plagiarism detection**. Directly serves the assessment-integrity layer this KB routes around every pass |
| 🆕 🟢 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — 🔴 at **`LICENCE`**, `1 128` B, *"© 2016-2022 University of Canterbury Computer Science Education Research Group"* | `7e323930cf6f` | `381` | 🟢 **APAC** — HOLDER-grade, New Zealand | an interactive high-school **computer-science textbook**, maintained by a university education-research group |
| 🆕 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 082` B, 🟡 **holder is an INDIVIDUAL** | `894ed020997f` | `381` | 🟡 **North America** — DESCRIPTION-grade, *"From NYU"* | a **distributed LMS** that automates computing-science courses on Kubernetes, with a cloud IDE |
| 🆕 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 072` B, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | `2 123` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | **educational video generation via CODE** rather than pixels — the only peer-reviewed row in this sweep, and a direct alternative shape to the shelf's video-authoring route |

🔴 **What is verified and what is not, stated so the rows cannot be over-read — and this discipline
is the direct lesson of `ACTION KE`:** licence BODY, byte count, copyright HOLDER and `HEAD` sha.
🔴 **NOT verified: interop (`OneRoster`, Ed-Fi, `LTI`, `SCORM`, xAPI), multi-tenancy, auth model,
dependency closure, build, or whether anyone operates them.** 🟡 **They are CANDIDATES, exactly as
`gap 134` records — not routes.** The one thing p175 will not do is repeat p174's mistake of
publishing a capability claim on top of a licence check.

### 🆕 🔴 Leaving — `eagles-edu/sis`, and the grep that over-reported it

🟢 **The clone is controlled: `HEAD` `7e5fbccad5a0`, `2 598` tracked files — both identical to what
p174 recorded, so this is a re-read of the same tree and not a moved target.**

| token | case-insensitive FILE hits | 🔴 **word-boundary LINE hits** | what it was actually matching |
|---|---|---|---|
| `ed-fi` | `55` | 🔴 **`0`** | `red-fill`, `disabled-fill`, `chip-red-fill` — CSS custom properties |
| `edfi` | `176` | 🔴 **`0`** | `normalizedField`, `normalizedFilters`, `mutatedFields` |
| `lti` | `325` | 🔴 **`0`** | `LevelTile`, `LevelTiles`, `ModalTitle`, `DetailTitle` |
| `oidc` | `29` | 🔴 **`0`** | `autoIdCount` |
| `jwt` | `16` | 🔴 **`0`** | base64 noise inside lockfiles |
| `oneroster`, `scorm`, `xapi`, `caliper`, `clever` | `0` | `0` | — nothing, at either precision |
| `tenant`, `tenancy`, `oauth`, `saml`, `ldap`, `sso`, `bcrypt`, `argon2` | `0`–`4` | 🔴 **`0`** | — |

🆕 🔵 **`T265` — a substring grep is not an interop measurement, and its error is one-directional.**
It can only over-report, so it fails in the direction that flatters the candidate. 🔵 **The rule this
file now uses: name the ARTEFACT that would have to exist — an `EdFi` client class, an
`/ims/oneroster/v1p1` route, a `cmi5` or xAPI statement emitter — and look for that, not for the
standard's name.**
🟢 **What the repository genuinely has, so the row is not merely negative:** `48` Prisma models
with a real school-shaped schema — `Student`, `StudentEnrollmentPeriod`, `StudentAttendance`,
`StudentGradeRecord`, `ParentPortalAccount`, `StudentPortalAccount`, `Family` — and hand-rolled
cookie sessions (`ADMIN_SESSION_TTL`) in place of any federated protocol.
🔴 **And the model that settles the routing question is called `SisConfigMirror`** — `id`,
`payloadJson`, `updatedBy`, two timestamps. 🔵 **A system of record does not mirror its own
configuration from somewhere else. This is a parent-and-student PORTAL in front of an SIS.**
🟡 **One hygiene figure a client should hear before quoting the size: `374` of the `2 598` tracked
files sit under `.backup/` and `.codex-backups/`.** The tree is `14.4%` prior drafts.
🟢 **p174's denominator correction STANDS and is independently reproduced** — `"student information
system" license:mit pushed:>=2026-04-16` is a real population, and `topic:education` is `8 197`
exactly. 🔴 **What does not stand is the conclusion drawn from it.** The twelve-pass row
*"no institutional-scale permissive student information system"* is **RESTORED** in
[`verticals/solutions.md`](../verticals/solutions.md), with the denominator correction kept and the
verdict unchanged.

### 🆕 🔴 A licence path this file has never probed, and what it does to five earlier verdicts

🔴 **`uccser/cs-field-guide` carries its `MIT` grant at `LICENCE` — the British spelling — and
returns `404` at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` and `license`.**
🔵 **`P50` taught that a licence-absence claim is a claim about the PATHS probed. `gap 133` is the
same lesson at a spelling this KB's probe list never contained**, and the Commonwealth spelling is
not rare in exactly the institutional population p175 just started sampling.
🔴 **Consequence, stated rather than deferred: every *"NO GRANT FILE — exhaustive"* verdict in this
KB was reached with an incomplete probe list** — including `JushBJJ/Mr.-Ranedeer-AI-Tutor` on the
`12`-row shelf. `ACTION KJ` re-probes them all.

### 🟢 The count, and the channel that makes it cheap

| figure | channel | cost | precision |
|---|---|---|---|
| 🆕 🟢 **`8 197`** | 🟢 **authenticated MCP repository search** | 🟢 **`1` request** | 🟢 **EXACT** |
| 🟡 `8 191` | `github.com/search` via `WebFetch`, `17` disjoint `pushed:` windows | 🔴 `17` requests, paced around a `429` | 🟢 exact, and off by `6` |
| 🔴 *"`8.2k`"* | the same page, unpartitioned | `1` request | 🔴 two significant figures |

🆕 🔵 **`T264` — a channel ledger is only as good as the request forms somebody thought to try.**
p174's ledger was careful, complete about what it tested, and missed the best channel entirely.
🟢 **The partition method is retained as a FALLBACK, not retired as wrong** — it is the only method
that works when the authenticated channel is unavailable, and it agreed to within `0.07%`.
🔴 **One limit of the new channel, measured and worth writing down: it answers SEARCH and refuses
per-repository file reads by session scope.** Licence bodies in the table above came from
`raw.githubusercontent.com`, `HEAD` shas from `git ls-remote`.
[`evidence/sis-interop-probe.2026-10-13-p175.tsv`](../evidence/sis-interop-probe.2026-10-13-p175.tsv)
· [`evidence/regional-sweep.2026-10-13-p175.tsv`](../evidence/regional-sweep.2026-10-13-p175.tsv)

## Pass 174 — 2026-10-13

🆕 🟢 **Three foundational repositories enter this file, and none of them is new software. They were
invisible because this KB was counting the wrong tag.** `ACTION JZ` made `topic:education`
countable (`8 191`, exactly); the sweep p173 recorded as never-run was then run, and
`"student information system" license:mit pushed:>=2026-04-16` returns **`54` results — an exact
integer, not a rounded one**.

| repo | licence *(body READ this pass, bytes)* | `HEAD` | last commit | tree | what it is |
|---|---|---|---|---|---|
| 🆕 🟢 [`eagles-edu/sis`](https://github.com/eagles-edu/sis) | 🟢 **`MIT`** — `LICENSE`, `1 066` B | `7e5fbccad5a0` | `2026-09-26` → `17` d | 🟢 **`2 598` files** | the largest permissive student information system this KB has ever been able to name |
| 🆕 🟢 [`opensacorg/learning-blocks`](https://github.com/opensacorg/learning-blocks) | 🟢 **`MIT`** — `LICENSE`, `1 075` B, *"Copyright (c) 2022 Code for Sacramento"* | `5bc137c972c7` | `2026-09-15` → `28` d | 🟢 **`849` files** | an SIS built by a **Code for America brigade** — a civic-tech institution, which also PLACES it (`P800`) |
| 🆕 🟡 [`Arux-Software/Bright`](https://github.com/Arux-Software/Bright) | 🟢 **`MIT`** — 🔴 at `LICENSE.txt`, `1 075` B *(a `P50` instance: plain `LICENSE` is absent)* | `7d15ccb7c2e9` | — | — | a framework for working WITH student information systems — a client library, not a system of record |

🔴 **What is verified and what is not, stated so the rows cannot be over-read (`ACTION JR`):**
licence BODY, `HEAD` sha, tree size and commit date. 🔴 **Not verified: `OneRoster`, `SCORM`, xAPI,
multi-tenancy, authentication, dependency closure, or whether anyone operates them.** They are
candidates in [`verticals/solutions.md`](../verticals/solutions.md), not routes.
🔴 **And the residue a client should hear: the head of that `54`-repository population is `31`★** —
a browser extension for a Dutch SIS. There is still no institutional-scale permissive SIS. The
twelve-pass sentence *"none exists"* was stronger than the evidence, and it was never re-tested on
a denominator that could have refuted it.

### 🆕 🟢 The `P50` instance, because this file keeps finding them

🔵 `Arux-Software/Bright` carries its grant at **`LICENSE.txt`** and nothing at `LICENSE`. This KB
has now recorded the same shape at `openfun/ralph` (`LICENSE.md`), `moodle/moodle` (`COPYING.txt`),
`formalms/formalms` (`html/license.txt`) and `os4ed/openSIS-Classic` (not at the root at all).
🟢 **The probe ladder in [`compose/code/grant-ladder-v4/`](../compose/code/grant-ladder-v4) exists
for exactly this reason, and a `404` on `LICENSE` is never a finding on its own.**

### 🟢 Carried forward unchanged

🟡 **Every p168–p173 verdict in this file stands; p174 re-read no platform root grant.** The
`Sakai` manifest reading corrected at p173 (`25` `Apache-1.1` + `9` `BSD`, not `34` `BSD`) is
unchanged, and the `Apache-1.1` support added to the shared classifier at p173 is now also
exercised by p174's own gate suite — `12` of `12`, offline.
[`evidence/exact-count-partition.2026-10-13-p174.tsv`](../evidence/exact-count-partition.2026-10-13-p174.tsv)
## Pass 173 — 2026-10-13

🆕 🟢 **`ACTION JU` DISCHARGED. The shared hardened classifier can now see `Apache-1.1`, and
`Sakai`'s manifest re-reads as `25` `Apache-1.1` paths + `9` `BSD` where p170–p172 all read
`34 BSD`. `207` of `207` regression assertions, `8` of them new, `13` of `14` dependent suites
byte-identical.**
🆕 🔴 **But the falsifier's first limb FIRES and it narrows the gap: the corrected classifier
changes `0` verdicts across the `50` licence bodies committed in this repository's own fixtures. On
the evidence available offline `T232` is a property of ONE 2005-era manifest, not a live defect in
a shared control. The error was LATENT, and `gap 120`'s *"every instrument inherits this"* is true
in principle and empty in practice.**
🆕 🟢 **And the re-read was CONTROLLED where p171's was not. `git fetch` refused the pinned sha —
`fatal: couldn't find remote ref 88f8e09c0a38` — and `raw.githubusercontent.com` served all `86`
paths at that exact commit anyway. `86` of `86` bodies byte-identical to p172's recorded hashes
(`T249`).**

### 🆕 🟢 What `Sakai`'s `licenses/` manifest actually contains, corrected

| family *(shared classifier, p173)* | paths | was read as |
|---|---|---|
| 🆕 🟢 **`Apache-1.1`** | 🆕 **`25`** *(`20` distinct blobs)* | 🔴 **`BSD`** at p170, p171 and p172 |
| 🟢 `Apache-2.0` | `24` | unchanged |
| 🔴 `UNCLASSIFIED` | `16` | unchanged — this is where the `8` proprietary Sun agreements live |
| 🟡 `BSD` | 🆕 **`9`** | was `34` |
| 🟡 `LGPL-2.1` | `5` | unchanged — includes the `2` generic-blob mismatches (`T230`) |
| 🟢 `MIT` | `3` | unchanged |
| 🟡 `MPL-1.1` | `1` | unchanged |
| 🔴 `CC-BY-2.5` | `1` | unchanged |
| ⬜ binary PDF, not read | `2` | unchanged |

🟢 **The `25` are the ASF components of a 2005-era Java stack and they are exactly who you would
expect: `log4j-1.2.8`, `lucene`, `struts-1.1`, `struts-legacy`, `velocity`, `poi`, `oro`, `batik`,
`fop`, `james`, `axis`, `xalan-2.5.2`, `xercesImpl-2.5.0`, `xml-apis`, `jasper-compiler`,
`jasper-runtime`, `avalon-framework`, `cornerstone`, `excaliber`, `logkit`, `db-ojb-1.0.rc6`,
`commons-id-0.1-dev`, `stxx-1.3`, `xmlform` — and `apache1.1.license.txt` itself.**

### 🆕 🟡 What changes for a client, and what does not

| | |
|---|---|
| 🟢 **permission** | 🟢 **NOTHING changes. `Apache-1.1` and `BSD-3-Clause` are both permissive and both OSI; `commercial_use_ok()` answered ALLOWED before and after. No verdict this KB published was wrong** |
| 🔴 **attribution** | 🔴 **THIS is what was lost. `Apache-1.1` clause `3` requires the end-user documentation to carry *"This product includes software developed by the Apache Software Foundation (http://www.apache.org/)"*. `BSD-3-Clause` requires no acknowledgment at all. A deliverable that reported `BSD` over these `25` paths dropped an attribution obligation the client has to meet** |
| 🟡 **what it does NOT prove** | 🟡 **These are manifest files for components `Sakai` may no longer ship. p173 read the MANIFEST, not the build — same limit p172 stated and it still applies** |
| 🟢 **the scanner line to use in a deck** | 🟢 ***"A tool reporting `34 BSD` over `Sakai`'s `licenses/` is reporting `25` `Apache-1.1` files as BSD. `Apache-1.1` is BSD-shaped — it carries the same redistribution grant — plus an attribution clause BSD does not have."*** |

### 🆕 🟢 The classifier change itself

🟢 **Three anchors, all on the TITLE BLOCK except the third's confirming signature, and the order is
load-bearing because `Apache-1.1` CONTAINS the BSD grant phrase:**

| anchor | answer |
|---|---|
| title says `Apache Software License` + `Version 1.1` | `Apache-1.1` |
| title says `Apache Software License` + `Version 1.0` | `Apache-1.0` |
| title says `Apache Software License`, no version, body carries the clause-`3` acknowledgment | `Apache-1.x-UNVERSIONED` *(following `GPL-UNVERSIONED`: never invent a version the payload does not state)* |

🔴 **A payload carrying the acknowledgment but NOT the title stays `BSD`, deliberately** — the ASF
acknowledgment appears in BSD notices of projects that merely credit the ASF, and the suite pins
this with a FABRICATED negative control that says so in its filename.
🟢 **The `7` platform rows, `Moodle`'s `88` grant documents and `OpenOLAT`'s root verdict are
CARRIED UNCHANGED from p168–p172. p173 re-read no platform root and says so.**
[`compose/code/p173-apache11-family/`](../compose/code/p173-apache11-family/)
· [`evidence/apache11-reclassification-sakai86.2026-10-13-p173.tsv`](../evidence/apache11-reclassification-sakai86.2026-10-13-p173.tsv)
· [`evidence/apache11-outside-sakai-corpus.2026-10-13-p173.tsv`](../evidence/apache11-outside-sakai-corpus.2026-10-13-p173.tsv)
· [`evidence/lib-test-surface-pristine-vs-patched.2026-10-13-p173.tsv`](../evidence/lib-test-surface-pristine-vs-patched.2026-10-13-p173.tsv)
## Pass 172 — 2026-10-13

🆕 🔴 **`ACTION JO` settled `gap 117` and found something larger beside it. `8` of the `86` paths in
`Sakai`'s `licenses/` manifest are NOT OPEN-SOURCE GRANTS AT ALL — they are Sun Microsystems
click-through agreements and one single-seat proprietary licence. p171 swept this same population
and published `0` hostile.**
🆕 🟢 **On the question the action actually asked — does the manifest MISLABEL components? — the
answer is no: `3` mismatches, the same `3` p171 found, verified this pass against authoritative
upstream metadata. The first falsifier limb FIRES; the manifest is three stale files on the licence
question.**
🆕 🔴 **And `25` of the `86` paths carry the **Apache Software License 1.1**, which this KB's shared
hardened classifier reports as `BSD` — including the file named `apache1.1.license.txt` (`T232`).**

### 🆕 🟡 The `7` platform rows — HEADs at p172

🟢 **`git ls-remote` at `t0 = 2026-10-13T10:5xZ`, `7` of `7` reachable. Root verdicts carry forward
from p168–p171 body reads; no root grant was re-read this pass.**

| repo | HEAD at p172 | root verdict | moved since p171 | what it is |
|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 **`ad60834ff1f8`** | 🟢 `ECL-2.0` | 🔴 **YES** *(from `88f8e09c0a38`)* | institutional LMS, Java |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `f20534726a59` | 🔴 `GPL-3.0` @ `COPYING.txt` | 🟢 no | the world's most deployed LMS, PHP |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | 🟢 **`MIT`** | 🟢 no | **offline-first** learning platform — the low-connectivity row |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | 🔴 `AGPL-3.0` | 🟢 no | MOOC-scale courseware, Python |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | 🔴 `GPL-3.0` | 🟢 no | LMS with strong assessment/exam tooling, PHP; EMEA-rooted |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`46a5d7d40082`** | 🟡 `LGPL-3.0` | 🔴 **YES** *(from `1c95cefebc17`)* | education **ERP** on Odoo — enrolment, fees, timetabling. 🔴 **Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`, p164)** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | 🟢 **`MIT`** | 🟢 no | SCORM 1.2 / 2004 + AICC + xAPI runtime — the packaging layer |

🟢 **Permissive and buildable without a licence conversation: `2` of `7` — `kolibri` (`MIT`) and
`scorm-again` (`MIT`). `Sakai`'s `ECL-2.0` is an Apache-2.0 variant with a teaching-use patent
carve-out and is the third practical route (`p170`).** 🔴 **`Moodle`, `ILIAS` (`GPL-3.0`) and
`edx-platform` (`AGPL-3.0`) are reciprocal; `AGPL` reaches network use, which is the form most
client deployments take.**

### 🆕 🔴 `ACTION JO` — `8` paths in `Sakai`'s manifest are proprietary agreements

🔴 **Control stated honestly: the measurement was taken at `HEAD 88f8e09c0a38`, and `Sakai` has
since moved to `ad60834ff1f8`. The manifest is `licenses/`, which Sakai has not touched in years,
but this reading is pinned to a sha that is no longer HEAD and says so.**

| class *(read on the TITLE BLOCK, per `P237`)* | paths | what it withholds |
|---|---|---|
| 🔴 **Sun Binary Code License Agreement** | `activation`, `jta`, `jdbc2_0-stdext` | 🔴 **redistribution** *(one archival copy)*, modification, decompilation; `jta` adds *"internal use only … for which the corresponding fee has been paid"* |
| 🔴 **Sun Software License Agreement + Entitlement** | `servlet` | 🔴 redistribution |
| 🔴 **Sun Specification click-through** | `jsf-api`, `jsf-impl`, `standard` | 🟡 a specification grant, not an implementation grant |
| 🔴 **proprietary single-seat** | `java2html` | 🔴 **one copy, one person**, no decompile |

🔴 **Why p171 read `0`: `ACTION JK` tested hostility with `commercial_use_ok()`, a NONCOMMERCIAL
**phrase** test. None of these eight uses the word *"noncommercial"*. They withhold redistribution
instead, and a phrase test for the wrong word is silent on the right finding (`T231`).**
🆕 🔴 **The manifest also contradicts ITSELF about one component: `servlet.license.txt` carries
Sun's proprietary Entitlement while `jsp-api.license.txt` — the sibling API, same upstream, same
directory — carries `Apache-2.0`. The servlet API as Tomcat ships it is `Apache-2.0`.**
🟡 **What this does and does not mean for an engagement: these are 2005-era manifest files for
components `Sakai` may no longer ship. The finding is about the MANIFEST a client's reviewer will
read, not a proven claim that proprietary jars are in today's build. State it that way — and then
check the build, which this pass did not.**

### 🆕 🟢 The three mismatches, verified upstream rather than remembered

| file | body | upstream | verified against |
|---|---|---|---|
| 🔴 `aopalliance.license.txt` | `LGPL-2.1` | 🟢 **Public Domain** | mojohaus third-party report; Apache CXF licence listing |
| 🔴 `dnsjava-1.2.3.license.txt` | `LGPL-2.1` | 🟢 **BSD** | Maven Central POM |
| 🟡 `junit-3.8.1.license.txt` | `IPL-1.0` | 🟡 **`CPL-1.0`** | `repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.pom` declares *"Common Public License Version 1.0"* |

🟢 **The JUnit row is a mismatch by IDENTIFIER and barely by EFFECT — `CPL-1.0` is the IBM Public
License re-stewarded, near-identical text. Report it as an identifier error, not a licence risk.**
🆕 🟢 **`T230` — the MECHANISM of both `LGPL` mismatches is generic-blob reuse. Their blob is
byte-identical to the manifest's own generic `LGPL2.1.license.txt`, so neither file carries a
component-specific copyright line. `8` of `86` paths are copies of a family file; `2` of the `8`
are wrong and the other `6` are right by luck, not by evidence.**

### 🆕 🔴 `T232` — the shared classifier cannot see `Apache-1.1`, and it is `25` of `86` paths here

| family as the classifier reports it | paths | corrected |
|---|---|---|
| 🔴 **`BSD` `34`** | 34 | 🔴 **`9` BSD + `25` `Apache-1.1`** |
| 🟢 `Apache-2.0` | 24 | 24 |
| 🟡 `UNCLASSIFIED` | 16 | 🔴 **`8` of them are proprietary, `1` is not a grant** |
| `LGPL-2.1` | 5 | 5 |
| `MIT` | 3 | 🟡 **`2` — `jing` is `BSD-3-Clause`** |

🔴 **A client scanner reporting *"34 BSD"* over this tree is reporting `25` `Apache-1.1` files as
BSD. `Apache-1.1` is BSD-SHAPED — four clauses on the same skeleton — but carries its own
attribution clause (*"This product includes software developed by the Apache Software
Foundation"*), which is how p172 detects it.**
🆕 🔵 **`T224` re-fired, on p172's own instrument. p172's FIRST hostility test searched for
withholding language in bodies and returned `34` raw hits, `26` of them ordinary `Apache-2.0` and
`LGPL` text matched on phrases like *"shall not modify"*. The finding survived only because the
test was moved to the title block — which is `P237`, a rule written in this KB since pass 77 and
broken again here on the first attempt. A rule that has to be remembered is not a control.**
[`evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv`](../evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv)
· [`evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv`](../evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv)
· [`evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv`](../evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv)
· [`compose/code/p172-manifest-attribution/`](../compose/code/p172-manifest-attribution/)
## Pass 171 — 2026-10-13

🆕 🔴 **`ACTION JK` classified the inner grant bodies this page has been COUNTING, and the count
itself was wrong in one direction only: `105` of `Moodle`'s `193` *"grant bodies"* are PHP SOURCE
FILES, not grants. `Sakai`'s contamination is `0` of `129`. The published pair invited a comparison
that cannot be made (`T223`).**
🆕 🟢 **The substantive answer is reassuring and now measured: `217` third-party grant documents
across the two leading institutional LMSes, `12` families, `0` that withhold commercial use or
redistribution. `gap 115`'s anxiety was procedural, as `penecho`'s `32` predicted.**

### 🆕 🟡 The licence column, with the inner audit CLASSIFIED

| repo | HEAD at p171 | root verdict | name matches | `P170-A` bodies | 🆕 **DOCUMENT bodies** | 🆕 **source-file over-read** | 🆕 **hostile** |
|---|---|---|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 **`88f8e09c0a38`** *(MOVED from `10a1d904d379`)* | 🟢 `ECL-2.0` | `165` | `129` | 🟢 **`129`** *(`72` blobs)* | 🟢 **`0`** | 🟢 **`0`** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `f20534726a59` *(UNCHANGED — controlled re-read)* | 🔴 `GPL-3.0` @ `COPYING.txt` | `217` | `193` | 🆕 🔴 **`88`** *(`80` blobs)* | 🔴 **`105`** | 🟢 **`0`** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | 🟢 `MIT` | `11` | 🟡 `6` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | 🔴 `AGPL-3.0` | `27` | 🟡 `15` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | 🔴 `GPL-3.0` | `7` | 🟢 `2` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `1c95cefebc17` | 🟡 `LGPL-3.0` | `15` | 🟢 `1` | 🟡 *not re-swept this pass* | — | — |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | 🟢 `MIT` | 🟢 `1` | 🟢 `1` | 🟢 **`1`** | 🟢 **`0`** | 🟢 **`0`** |

🔴 **Control honestly stated: `Moodle` was re-read at p170's EXACT `HEAD`, so every difference there
is INSTRUMENT. `Sakai` moved (committed `09:46:58Z` this pass) and the server refused the pinned sha
(`fatal: couldn't find remote ref`), so that limb is UNCONTROLLED — though its name-match count
(`165`) and body count (`129`) are identical at both `HEAD`s, which is a result rather than a control.**

### 🆕 🟢 Family tally — what a client's scanner will actually report

| family | `Sakai` *(72 blobs)* | `Moodle` *(80 blobs)* |
|---|---|---|
| 🟢 **`MIT`** | `7` | 🟢 **`47`** |
| 🟢 **`BSD`** | 🟢 **`29`** | `12` |
| 🟢 **`Apache-2.0`** | `21` | `8` |
| 🟢 **`ECL-2.0`** | `10` | — |
| 🟡 **`LGPL`** | `2` | `3` |
| 🔴 **`GPL`** | — | `2` |
| 🟡 **`IPL-1.0`** | `1` | — |
| 🟡 **multi-family blobs** | `2` | `6` |
| 🟢 **withholding commercial use** | 🟢 **`0`** | 🟢 **`0`** |

🟢 **`Sakai`'s `3` reciprocal bodies (`2` `LGPL-2.1`, `1` `IPL-1.0`) all sit in `licenses/` — a
third-party NOTICE manifest. `0` copyleft grant governs `Sakai`'s own code.** 🔴 **Whether a
dependency notice counts as *"copyleft inside an `ECL-2.0` repository"* is a READING, and it is
counsel's, not an instrument's. Recorded as such rather than declared silent.**
🆕 🟡 **`gap 117` — and that manifest MISLABELS: `aopalliance.license.txt` and
`dnsjava-1.2.3.license.txt` both carry `LGPL-2.1` text, where AOP Alliance is public domain
upstream and dnsjava is `BSD`; `junit-3.8.1.license.txt` carries `IPL-1.0` where JUnit `3.8.1`
shipped `CPL-1.0`. Do not read that directory as a per-component attribution map (`ACTION JO`).**

### 🆕 🔴 `T223` — why `Moodle`'s number was `54%` source code, and why `Sakai`'s was not

| | |
|---|---|
| 🔴 **convention one** | 🔴 **`Moodle` puts a GPL notice header in EVERY php file, so any Moodle source file satisfies `P170-A` step `2`'s body test** |
| 🔴 **convention two** | 🔴 **`Moodle` ships an `admin/tool/licensemanager/` subsystem — a licence-manager FEATURE — whose filenames all contain *"license"*, so they all satisfy the name match** |
| 🔴 **the product** | 🔴 **the two multiply: `105` of `193` are source code, including `lang/en/license.php` and `lib/tests/licenselib_test.php`** |
| 🟢 **why `Sakai` is clean** | 🟢 **its grants live in `licenses/*.txt`. `73` of its `129` paths are `.txt`; `0` are source** |

🟢 **`P171-A` is the fix and it is one predicate: a grant body must BE a licence document, not a
source file that mentions one.** 🔴 **`gap 118` is the residue, and it is a REVIEW-COST hazard rather
than a legal one: a client's scanner will still report ~`193`, so an SBOM review of `Moodle` starts
`105` findings in the hole. Now sized before anyone bills for it.**
[`evidence/inner-grant-families.2026-10-13-p171.tsv`](../evidence/inner-grant-families.2026-10-13-p171.tsv)
## Pass 170 — 2026-10-13

🆕 🟢 **`ACTION JH` DISCHARGED with a silent falsifier: `7` of `7` platform root verdicts reproduce
under the folded, TREE-WIDE gate that p168 could only run root-only. The licence column survives a
stricter instrument for the second consecutive pass.**
🆕 🔴 **What the tree-wide reading adds is not a correction but a change of scale. `Sakai` carries
`129` grant BODIES below its root and `Moodle` `193`, where this shelf prints one licence cell each.
`gap 109`'s shape — *"the published licence is the OUTER grant only"* — is confirmed at two orders of
magnitude larger than the repo it was found on.**
🆕 🟢 **And p169's `ACTION JC` verdict on `OpenEduCat` is INDEPENDENTLY VINDICATED. A broad instrument
finds `15` grant-named paths in that tree; `1` carries a body. The other `14` are the same
`notice-board-icon.svg`, copied into `14` Odoo modules.**
🆕 🔴 **A new candidate was tested and REFUTED before it reached the shelf: `Forma LMS`, called
*"Apache 2.0"* by a secondary source, carries the GNU `GPL` version `2` verbatim and has no root grant
file at all.**
[`evidence/platform-tree-grants.2026-10-13-p170.tsv`](../evidence/platform-tree-grants.2026-10-13-p170.tsv)
[`evidence/name-vs-body-divergence.2026-10-13-p170.tsv`](../evidence/name-vs-body-divergence.2026-10-13-p170.tsv)
[`evidence/permissive-lms-candidates.2026-10-13-p170.tsv`](../evidence/permissive-lms-candidates.2026-10-13-p170.tsv)

### 🆕 🟢 `ACTION JH` — the `7` platform rows, folded and tree-wide

🟢 **Falsifier: *"refuted if any p168 licence verdict changes."* SILENT — all `7` reproduce.**
🟢 **Instrument: treeless clone, exhaustive `ls-tree -r`, root body read and family-matched, plus a
content test on every grant-named path.**

| repo | HEAD | HEAD date | root grant | root verdict *(reproduced)* | grant-named paths | 🆕 **actual bodies** |
|---|---|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `10a1d904d379` | `2026-10-09` | `LICENSE` | 🟢 `ECL-2.0` | `165` | 🔴 **`129`** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | `2026-10-12` | `LICENSE` | 🟢 `MIT` | `11` | 🟡 **`6`** |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | `2026-10-12` | `LICENSE` | 🔴 `AGPL-3.0` | `27` | 🟡 **`15`** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | `f20534726a59` | `2026-10-03` | 🟡 **`COPYING.txt`** | 🔴 `GPL-3.0` | `217` | 🔴 **`193`** |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | `2026-10-13` | `LICENSE` | 🔴 `GPL-3.0` | `7` | 🟢 **`2`** |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `1c95cefebc17` | `2026-09-07` | `LICENSE` | 🟡 `LGPL-3.0` | `15` | 🟢 **`1`** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | `2026-10-09` | `LICENSE` | 🟢 `MIT` | 🟢 **`1`** | 🟢 **`1`** |

🟢 **`6` of `7` rows have a HEAD inside `11` days; `ILIAS` is `0` days old at this pass.**
🟡 **`Moodle`'s root grant is at `COPYING.txt`, not `LICENSE` — recorded because a gate that probes
only `LICENSE` reads `Moodle` as unlicensed, which is `P169-A` step `5`'s original failure mode.**
🔵 **The column to read twice is the last one. This shelf has been publishing one licence per platform
for `170` passes. For `scorm-again` that one cell is the whole truth. For `Sakai` it is `1` of `129`
and for `Moodle` `1` of `193`.**

### 🆕 🔴 What `129` and `193` mean, stated so it is not mistaken for alarm

🟢 **None of this overturns a verdict. The outer grant is what governs the project's own code, and all
`7` reproduced.** 🔴 **What it governs is a fraction of what a client ships.**

| the question a client actually asks | what this shelf could answer before p170 | what it can answer now |
|---|---|---|
| 🟢 *"what licence is Moodle?"* | 🟢 **`GPL-3.0`, body read, verbatim** | 🟢 **unchanged** |
| 🔴 *"what licences will my scanner find in Moodle?"* | 🔴 **unknown** | 🟡 **`193` grant bodies exist; their families are NOT yet classified** |
| 🔴 *"how long is the inner audit?"* | 🔴 **unestimable** | 🟢 **countable: `129` for `Sakai`, `193` for `Moodle`, `15` for `Open edX`, `1` for `scorm-again`** |

🟢 **So the deliverable p170 adds is an ESTIMATE, not a verdict — and estimable work is billable
work.** 🟢 **Classifying those bodies is pre-registered as `ACTION JK`, with `P170-A` as the
procedure and `penecho`'s `32`-file classification as the worked precedent.**
🔴 **The caution that comes with it, from `T213`: do not count grant files by filename. On these same
trees the name match over-reads by `36` on `Sakai` and `24` on `Moodle`, and on `OpenEduCat` by `14`
out of `15`.**

### 🆕 🟢 `gap 109` — p169's `OpenEduCat` answer re-measured by a different instrument

🟢 **p169 used a canonical-filename regex and concluded `1` grant file in `1 345` tracked files.
p170 used a deliberately broad name match and found `15` candidates — then content-tested all `15`.**

| probe | result | reading |
|---|---|---|
| 🔴 **grant-named paths, broad match** | 🔴 **`15`** | 🔴 **looks like a `15`-grant tree** |
| 🟢 **of those, carrying a grant body** | 🟢 **`1`** — the root `LICENSE` | 🟢 **p169 was RIGHT** |
| 🟢 **what the other `14` are** | 🟢 **`static/description/notice-board-icon.svg`, once per Odoo module** | 🟢 **an ICON. The string *"notice"* is in a filename, not a grant** |

🔵 **Two passes, two instruments with opposite biases, one answer. That is the strongest form of
confirmation this KB can produce from a single container, and it is worth more than either reading
alone.** 🟢 **`T201` stands untouched: the root body still promises the `GPL-3.0` text *"at the
bottom"* and still contains `0` occurrences of it.**

### 🆕 🔴 `Forma LMS` — refuted at the artifact, and a hazard class this shelf has not held before

| probe | result |
|---|---|
| 🔴 **claimed by a secondary source** | 🔴 **`Apache-2.0`** |
| 🔴 **root grant file** | 🔴 **NONE — no `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` at the root** |
| 🟢 **actual grant** | 🟢 **`html/license.txt`, `18 346` B — `GNU GENERAL PUBLIC LICENSE Version 2, June 1991`, verbatim** |
| 🟢 **occurrences of *"Apache"* in that body** | 🟢 **`0`** *(the only Apache text in the tree is a vendored jsdoc prettify file)* |
| 🟡 **HEAD** | 🟡 **`446a77a9b9cb`, `2026-07-17` — `88` days** |
| 🆕 🔴 **licence shipped in** | 🔴 **NINE languages — english, spanish, portuguese, italian, german, french, croatian, bosnian, tamil — with NOTHING naming which governs** |

🔵 **The multilingual grant is the new hazard. A translated copyleft licence is not a second licence
and not a choice; it is a convenience that leaves the governing text unnamed. For a LATAM or EMEA
engagement that is a question for counsel, and the right move is to name the English text as
controlling in writing before anything is built on it.**
🟢 **Cost of this refutation: two treeless clones. Value: a `GPL-2.0` platform did not enter a shelf
that exists to identify what Globant can build on permissively.**

### 🆕 🟢 The foundations shelf — permissive rows, re-verified this pass

🟢 **Every row below had its root grant body read on the open channel at p170 or p169, and its HEAD
confirmed by `git ls-remote`.**

| repo | licence *(body read)* | HEAD date | role |
|---|---|---|---|
| 🆕 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0` — §`1`–`9` VERBATIM, appendix replaced by `2` attribution statements** | 🟢 **`2026-10-12`** | 🆕 🟢 **institutional LMS — `QTI`, `SCORM`, curriculum, assessment. RESTORED to the permissive route (`T216`)** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | 🟢 `2026-10-12` | 🟢 offline-first learning platform |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🟢 `2026-10-09` | 🟢 **`SCORM` `1.2` / `2004` + `AICC` runtime — the interop layer** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `MIT` | 🟢 `2026-10-10` | 🟢 **LMS, and the only repo on any shelf shipping a dependency-licence GATE (`T208`)** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 `ECL-2.0` | 🟢 `2026-10-09` | 🟡 institutional LMS — patent limb (`T200`), gate conflict (`T208`) |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 `2026-10-12` | 🟡 MOOC platform — RPC carve-out (`gap 107`) |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` *(at `COPYING.txt`)* | 🟢 `2026-10-03` | 🟡 the incumbent LMS |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` | 🟢 `2026-10-12` | 🟡 **the most active SIS this KB holds** |

🟢 **`4` rows permissive (`MIT` / `Apache-2.0`) and all `4` with a HEAD inside `5` days.**
🔴 **`0` permissive SIS, for a NINTH pass — now with `Forma LMS` tested and refuted rather than the
hole merely re-asserted.**

## Pass 169 — 2026-10-13

🆕 🟢 **`ACTION JC` is DISCHARGED and `gap 109` closes in the direction nobody expected: there are no
unnamed bundled grants in `OpenEduCat` to name. `1 345` tracked files, `1` grant file, `0` vendored
anything, and `14` of `14` Odoo manifests declaring the same `LGPL-3`. The *"bundled libraries ... other
GPL-compatible licenses"* clause has NO REFERENT in the tree.**
🆕 🟢 **And the oldest hole on this shelf — no permissive SIS, re-searched for seven passes — is now
SETTLED rather than merely re-confirmed. The web's one `Apache-2.0` answer, `Fedena`, is real as a
grant and abandoned as software: a licensor statement in `NOTICE`, no licence body in either of its two
trees, and a newest commit of `2016-07-20`.**
🆕 🟢 **Two ACTIVE copyleft SIS options are verified and dated for the first time: `RosarioSIS`
(`GPL-2.0`, HEAD `1` day old) and `openSIS-Classic` (`GPL-2.0`, HEAD `8` days old).**
[`evidence/openeducat-bundled-grants.2026-10-13-p169.tsv`](../evidence/openeducat-bundled-grants.2026-10-13-p169.tsv)
[`evidence/sis-permissive-settled.2026-10-13-p169.tsv`](../evidence/sis-permissive-settled.2026-10-13-p169.tsv)
[`evidence/agent-grant-surface.2026-10-13-p169.tsv`](../evidence/agent-grant-surface.2026-10-13-p169.tsv)

### 🆕 🟢 `gap 109` CLOSED — `OpenEduCat` bundles nothing, and the clause is inherited boilerplate

🟢 **`ACTION JC`'s falsifier was *"refuted if vendored third-party code carrying its own grant is
found"*. SILENT.** 🟢 **Instrument: a treeless clone at HEAD `1c95cefebc17`, then an exhaustive
`ls-tree -r` — not a sampled probe.**

| probe | result | reading |
|---|---|---|
| tracked files | `1 345` | — |
| 🟢 **grant files anywhere in the tree** | 🟢 **`1`** — the root `LICENSE` | 🟢 **ONE grant surface in the whole repository** |
| `node_modules/` · `vendor/` · `static/lib/` · `*.min.js` | 🟢 **`0` · `0` · `0` · `0`** | 🟢 **nothing is vendored** |
| `requirements.txt` · `setup.py` · `pyproject.toml` | 🟢 **`0`** | 🟡 **no declared dependency manifest either** |
| 🟢 **Odoo `__manifest__.py` files** | `14` | 🟢 **the real packaging unit** |
| 🟢 **manifests declaring `'license': 'LGPL-3'`** | 🟢 **`14` of `14`** | 🟢 **UNIFORM — every module agrees with the published licence** |

🔵 **So the hazard p168 flagged was mis-shaped, and saying so is the finding. The clause is Odoo's own
licence-notice boilerplate carried into a derived repository, not a description of this tree. A licence
review of `openeducat_erp` has `1` file to read, not an unknown number.**
🔴 **What survives from p168 untouched is the OTHER defect, `T201`: the body still promises the
`GPL-3.0` text *"at the bottom"* and still contains `0` occurrences of it.**
🟡 **Where the real third-party exposure lives, stated so it is not mistaken for a clean bill: the Odoo
runtime these `14` modules require. That is a DEPENDENCY, outside this tree, and no probe of this
repository can speak to it.**

### 🆕 🔴 `T212` — the `Fedena` question is settled, and the hole does not close

🟢 **p169's vertical-platform query named exactly one new candidate, and a secondary source called it
*"Apache 2.0"*. Instead of recording the claim, p169 verified it on the open channel.**

| repo | HEAD | last commit | root grant files | licence BODY | declared licence |
|---|---|---|---|---|---|
| 🔴 [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | `68a84ac445bf` | 🔴 **`2016-07-20`** | 🟡 `NOTICE` only | 🔴 **ABSENT** | 🟢 `Apache-2.0`, by licensor statement |
| 🔴 [`foradian/fedena`](https://github.com/foradian/fedena) | `333477b06f1d` | 🔴 **`2012-10-12`** | 🟡 `NOTICE` only | 🔴 **ABSENT** | 🟢 `Apache-2.0`, by licensor statement |

🟢 **Verbatim from `projectfedena/fedena`'s `NOTICE`:** *"Fedena / Copyright 2011 Foradian Technologies
Private Limited. ... Licensed under the Apache License, Version 2.0 (the `"License"`)"*.
🟢 **So the grant IS real — a licensor statement, the strongest channel this container has.** 🔴 **And
the software is an abandoned `2011` Rails application: over ten years since the newer tree moved,
fourteen since the older one.** 🔴 **Neither tree contains the Apache text it names — the same defect
class as `T201`.**
🔵 **Why this is worth a `T`-number: it CLOSES A SEARCH LOOP. Seven passes have re-run this query and
`Fedena` is the only name it has ever produced. It is now settled with a reason, so p170 should not
spend the query again.**
🟢 **The absence restates more usefully than before: not *"no permissive SIS exists"* but **"no
permissive AND MAINTAINED SIS exists"** — and the permissive one that did exist is datable.**

### 🆕 🟢 Two active SIS routes, verified — new rows on this shelf

| repo | licence | where the grant lives | HEAD | age | note |
|---|---|---|---|---|---|
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** *(`15 214 B`, *"Version 2, June 1991"*)* | 🟢 root `LICENSE` | `232819b4c07e` | 🟢 **`1` d** | 🟢 **the most active SIS this KB has verified** |
| 🟡 [`os4ed/openSIS-Classic`](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** | 🔴 **`docs/License.txt` — NOT the root (`T209`)** | `5d546f20117e` | 🟢 `8` d | 🔴 **vendors `CKEditor` and plugins with their own grants, unread (`gap 112`)** |

🔵 **Routing consequence: a client who can accept `GPL-2.0` now has two live SIS routes with dates
attached, where this shelf previously had only `OpenEduCat`'s `LGPL-3.0`. A client who cannot accept
copyleft still has nothing, and that is now a measured statement rather than an open search.**

### 🆕 🟢 `P169-A` — the licence gate, corrected in two places by its own failures

🟢 **`P168-A`'s six steps stand. p169 adds a step `0` and rewrites step `5`, because this pass's own
first readings were wrong in both places.**

| step | what it does | why |
|---|---|---|
| 🆕 🟢 **`0`. FOLD** | 🟢 **normalise curly quotes, apostrophes, the `©` glyph and `http`→`https` BEFORE any diff** | 🔴 **`T205` — SPDX's canonical texts carry `246` curly quotes and `1` `©`; FSF ASCII bodies carry `0`. Unfolded, a clean `GPL-3.0` reads as `71` deviations** |
| 🟢 `1`–`4` | 🟢 title-line family · canonical word diff · permissive-set membership · body-contains-its-family | 🟢 unchanged |
| 🆕 🔴 **`5`. TREE, not root** | 🔴 **enumerate grant files with `ls-tree -r` across the whole tree** | 🔴 **`T209` — `openSIS-Classic` keeps its `GPL-2.0` in `docs/`, so a root probe calls an active, plainly licensed SIS *"unlicensed"*** |
| 🟢 `6` | 🟢 resolve every pointer | 🟡 **`fsf.org` and `gnu.org` are unresolvable here (`T211`), so those pointers are UNRESOLVED, not broken** |

### 🆕 🟢 `P169-B` — the treeless clone: a `200×` cheaper instrument for every inventory question

🔴 **p168 answered *"which grant files exist?"* by cloning `10` full trees: `623 MB`, `11 684` files.**
🟢 **p169 answered it for `13` repos with `git clone --depth 1 --filter=blob:none --no-checkout`
followed by `ls-tree -r`: `3.1 MB` total.**
🟢 **The answer is strictly LARGER — `17` root plus `63` non-root grant files across `12` rows, plus the
`1 345`-file `OpenEduCat` census and `4` SIS candidates — because a treeless clone carries every path in
the tree while downloading no blob.**
🟢 **Pair it with `raw.githubusercontent.com` pinned at the HEAD sha for the bodies you actually want.
Both channels are confirmed open in a fresh container this pass.**
🔵 **The rule: clone blobs only when you need to read MANY files. For *"does this file exist"*,
*"what is in this tree"*, or *"what is the HEAD date"*, blobs are pure cost.**

### 🟢 The foundation shelf — licence verdicts carried from p168

🟢 **p168 body-read these `9` under the unfolded, root-only instrument. `ACTION JH` re-runs them under
`P169-A`; until then the verdicts stand as published, with the instrument named.**

| repo | licence | p168 verdict | p169 status |
|---|---|---|---|
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried — re-read pending (`ACTION JH`) |
| 🟢 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried |
| 🟢 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 CLEAN | 🟢 **still the SCORM `2004` route (`P168-B`)** |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** | 🔴 SUBSTITUTED LICENCE | 🔴 **and now known to fail a real allow-list (`T208`)** |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` | 🔴 BODY OMISSION | 🟢 **`gap 109` CLOSED this pass — nothing bundled** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` | 🔴 TWO GRANT SURFACES | 🟡 carried |
| 🟢 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 RPC carve-out | 🟡 carried — `gap 107` stands |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 `Apache-2.0` | 🟢 addendum reproduced | 🟡 carried |


## Pass 168 — 2026-10-13

🟢 **`ACTION IX` is DISCHARGED, falsifier SILENT: of the `7` repos this shelf RECOMMENDS but had
never body-read, `3` carry a licence body that is not the licence they are published as.**
🆕 🟢 **And the instrument retired at p167 is now EXPLAINED rather than merely retired: the
`35 147` / `35 149` byte spread that defeated the band test is ONE URL — `philosophy/why-not-lgpl.html`
against `licenses/why-not-lgpl.html` — between two FSF revisions of the same `GPL-3.0`.**
🆕 🔴 **The canonical channel had to change: `gnu.org` is a `403` POLICY DENIAL at this container's
gateway, so the FSF plain text could not be used. SPDX's registry on `raw.githubusercontent.com`
is `200`, and because SPDX reflows its text the diff is WORD-level after whitespace normalisation —
never byte-level.**
[`evidence/licence-canonical-diff.2026-10-13-p168.tsv`](../evidence/licence-canonical-diff.2026-10-13-p168.tsv)
[`evidence/proxy-channel-census.2026-10-13-p168.tsv`](../evidence/proxy-channel-census.2026-10-13-p168.tsv)

### 🆕 🟢 Every recommended licence body, now READ — `10` bodies, `7` repos, `2` controls

| repo | file | bytes | title-line family | verdict | what the diff found |
|---|---|---|---|---|---|
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | `COPYING.txt` | `35 147` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | `±4` words, all `http://fsf.org/` → `https://fsf.org/` |
| 🟢 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `LICENSE` | `35 147` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | the same `4` URL-scheme hunks |
| 🟢 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | `LICENSE` | `35 149` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | `±1` word — the `why-not-lgpl.html` path. **This is the whole `2`-byte spread** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `LICENSE` | `1 072` | 🟢 `MIT` | 🟢 **CLEAN** | `<year> <copyright holders>` → `2020 Jonathan Putney` |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `LICENSE` | `11 120` | 🟡 **`ECL-2.0`** | 🔴 **SUBSTITUTED LICENCE** | `+137`/`−13` words vs `Apache-2.0`, `95.44%` similar — a DIFFERENT licence, not an amended one |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `LICENSE` | `8 241` | 🟡 `LGPL-3.0` | 🔴 **PREAMBLE ADDENDUM + BODY OMISSION** | `3` added paragraphs, and `5 644` canonical words missing |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `LICENSE` + **`license.txt`** | `35 147` + `1 614` | 🔴 `GPL-3.0` | 🔴 **TWO GRANT SURFACES** | `LICENSE` is clean; a SECOND root file declares **`-or-later`** |
| 🟢 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `LICENSE` | `35 136` | 🔴 `AGPL-3.0` | 🟢 **CONTROL — addendum REPRODUCED** | canonical CONTAINED, `+615` chars appended |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | `LICENSE` | `10 982` | 🟢 `Apache-2.0` | 🟢 **CONTROL — addendum REPRODUCED** | inserts an *"Additional license statement"* AND drops the `APPENDIX` |

🟢 **Both controls reproduced, so the instrument is calibrated before its new findings are believed.**
🟢 **`4` of `7` are clean — and *clean* now has a measured meaning: the only deviation is an FSF text
revision or a filled-in copyright holder.**

### 🆕 🔴 `T200` — `Sakai` is not Apache-2.0, and the clause that differs is the one that matters to us

🟢 **This KB has published `Sakai` as `ECL-2.0` since p131 and was RIGHT.** 🔴 **What was never
published is WHAT `ECL-2.0` changes, and it is not cosmetic.**
🟢 **The licence says so itself, in its own preamble — a licensor statement, the strongest channel
available here:** *"The Educational Community License version 2.0 (`"ECL"`) consists of the Apache
2.0 license, modified to change the scope of the patent grant in section 3 to be specific to the
needs of the education communities using this license."*
🔴 **The inserted paragraph, verbatim:** *"Any patent license granted hereby with respect to
contributions by an individual employed by an institution or organization is limited to patent
claims where the individual that is the author of the Work is also the inventor of the patent
claims licensed, and where the organization or institution has the right to grant such license
under applicable grant and research funding agreements. No other express or implied licenses are
granted."*
🔴 **Read for a services firm: a contribution made by someone EMPLOYED by an institution carries a
patent grant narrowed to claims that person personally invented AND that their employer had the
right to license. `Apache-2.0`'s broad grant does not apply.** 🟢 **`+137`/`−13` words and
`95.44%` word similarity measured independently of the preamble's own claim.**
🟡 **Consequence for the routing table: `Sakai` stays the permissive LMS route and stays
recommended. The patent limb is a diligence item for any engagement that contributes code back,
and it is now stated instead of implied by *"Apache-derived"*.**

### 🆕 🔴 `T201` — `OpenEduCat`'s `LICENSE` promises the GPL text and does not contain it

🟢 **p164 published this body as *"`8 241 B`, INCOMPLETE"*. p168 names exactly what is missing and,
more usefully, that the file itself says it should be there.**
🔴 **The file's own words:** *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE,
Version 3 (LGPLv3), as included below. Since the LGPL is a set of additional permissions on top of
the GPL, **the text of the GPL is included at the bottom as well**."*
🔴 **Measured: `0` occurrences of `"GNU GENERAL PUBLIC LICENSE"` in the whole file. The body ends
mid-`LGPL`, and the `~35 KB` of `GPL-3.0` it promises is absent.** 🔵 **This matters because
`LGPL-3.0` is defined AS a set of additional permissions over `GPL-3.0`: without the `GPL` text,
the grant on disk is incomplete by its own construction, not merely short.**
🔴 **And a third added paragraph carries a carve-out no licence gate would catch:** *"Some external
libraries and contributions bundled with OpenEduCat may be published under other GPL-compatible
licenses."* 🟡 **So the row's published `LGPL-3.0` is the OUTER grant only; bundled components are
declared to be something else, unnamed.**
🔵 **Provenance, stated because it bounds the finding: this wording is Odoo's, and `OpenEduCat` is
an Odoo application — the defect is almost certainly inherited, not authored.**

### 🆕 🔴 `T202` — `Chamilo` has TWO root grant files, and they do not say the same thing

| surface | bytes | what it declares |
|---|---|---|
| 🟢 `LICENSE` | `35 147` | 🔴 the bare `GPL-3.0` body — **no version election at all** |
| 🆕 🔴 `license.txt` | `1 614` | 🔴 **`GPL-3.0`-OR-LATER:** *"either version 3 of the License, or (at your option) any later version"* |

🔴 **A gate that reads `LICENSE` sees `GPL-3.0-only`. A gate that reads `license.txt` sees
`GPL-3.0-or-later`, which is MORE permissive for a client.** 🟢 **`license.txt` is also the surface
the code itself points at: it states the in-source header convention
`/* For licensing terms, see /license.txt */`.**
🆕 🔴 **And both of `license.txt`'s own pointers are DEAD at `master` `440496d70ef0`:
`documentation/license.html` → `404`, `documentation/credits.html` → `404`.**
🔵 **So the file that carries the or-later election, and that every source header cites, refers for
its full text and its contributor list to two paths that no longer exist.** 🟡 **The or-later
reading still holds — it is stated in the file itself, not in the dead pointer — but the
contributor attribution it promises is unrecoverable from the repository.**

### 🔴 What `ACTION IX` means for `gap 105`, restated

🟢 **`gap 105` asked about ADDENDA. The answer is that *addendum* is too narrow a word for the class.**

| deviation class | found in | why a licence gate misses it |
|---|---|---|
| 🔴 **appended paragraph** | `edx-platform`, `OpenOLAT` | canonical still matches as a substring — the extra text is invisible to a containment test |
| 🔴 **substituted licence** | `Sakai` | the title line is honest, but `"ECL-2.0"` matches no entry in an `MIT`/`Apache`/`GPL` allow-list |
| 🔴 **body omission** | `OpenEduCat` | the file declares a family it does not fully contain |
| 🔴 **second grant surface** | `Chamilo` | each file is internally consistent; only reading BOTH shows the conflict |
| 🟢 **text revision / template fill** | `moodle`, `ILIAS`, `oneroster`, `scorm-again` | 🟢 **benign, and now measured so it stops being mistaken for a deviation** |

## Pass 167 — 2026-10-13

🟢 **`ACTION IV` is DISCHARGED, falsifier SILENT: `Ed-Fi-Alliance-OSS/edfi-oneroster` serves `12`
OneRoster 1.2 entities, users and enrolments among them, and `gap 102` CLOSES.**
🆕 🔴 **And this page's own published figure is CORRECTED: it is not `14` GET endpoints. It is `24`
rostering GETs over `12` entities, and neither the code nor the upstream README ever said `14`.**
🆕 🟢 **Every licence body on this shelf is now READ rather than banded — `14` bodies, `5` families,
and the size-band test is retired as unsound.**
[`evidence/oneroster-endpoints.2026-10-13-p167.tsv`](../evidence/oneroster-endpoints.2026-10-13-p167.tsv)
[`evidence/licence-bands.2026-10-13-p167.tsv`](../evidence/licence-bands.2026-10-13-p167.tsv)

### 🆕 🟢 `T189` — the OneRoster server, read route by route

🟢 **Pinned tree: `Ed-Fi-Alliance-OSS/edfi-oneroster`, `Apache-2.0` body-read `10 173 B`, `261`
tracked paths, HEAD `2026-10-12`.** 🟢 **Routes read from `src/routes/oneRoster.js`, controllers
sized to rule out stubs.**

| entity | collection | `/:id` | authz scope |
|---|---|---|---|
| 🟢 `users` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `students` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `teachers` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `enrollments` | 🟢 yes | 🟢 yes | `enrollments` |
| 🟢 `classes` | 🟢 yes | 🟢 yes | `classes` |
| 🟢 `courses` | 🟢 yes | 🟢 yes | `courses` |
| 🟢 `orgs` | 🟢 yes | 🟢 yes | `orgs` |
| 🟢 `schools` | 🟢 yes | 🟢 yes | `orgs` |
| 🟢 `academicSessions` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `gradingPeriods` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `terms` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `demographics` | 🟢 yes | 🟢 yes | `demographics` |

🟢 **`12` entities × `2` shapes = `24` rostering GETs, plus a catch-all `404`, a discovery route and
a health route — `34` `router.get` registrations in total.**
🟢 **Not stubs: `oneRosterController.js` `264` LOC and `OneRosterQueryService.js` `594` LOC.**
🟢 **The upstream README's endpoint table lists the SAME `24` rows and the SAME `12` entities, so
the two channels AGREE and the published `14` has no channel behind it at all.**

🟢 **`ACTION IV`'s falsifier required that users and enrolments NOT both be present. Both are.**
🟢 **So `P166-B` is amended into `P167-B` rather than withdrawn.**

### 🆕 🟢 Write-back, measured instead of deferred

🟢 **`router.post`, `router.put`, `router.patch` and `router.delete` all read `0` across the entire
application.** 🔴 **So this is READ rostering — not *"probably read-only"*, but zero write routes in
the tree.** 🔵 **The sentence a client gets: *`12` rostering entities, read-only, per-scope
authorisation, Apache-2.0; any enrolment write-back INTO the SIS is a build.*** 🟡 **Ed-Fi ODS
itself remains a separate, unmeasured decision.**

### 🆕 🔴 `T193` — the licence size band is retired, and `edx-platform` is why it mattered

🟢 **`ACTION IW` read all `14` licence bodies this shelf has on disk.** 🔴 **`P48`'s published bands
(`11 357`–`11 358` for Apache-2.0, `35 121`–`35 147` for GPL-3.0) match NOTHING on disk.**
🔴 **And the band test is not merely stale: `AGPL-3.0`'s measured maximum `35 136 B` and `GPL-3.0`'s
measured minimum `35 149 B` are `13 B` apart, while `Apache-2.0`'s spread within its OWN family is
`1 235 B` — `95×` larger. A discriminator cannot work in that geometry.**

| family | n | min | max | own spread |
|---|---|---|---|---|
| 🟢 `MIT` | `4` | `1 062` | `1 074` | `12 B` |
| 🔴 `PROPRIETARY` | `1` | `8 563` | `8 563` | — |
| 🟢 `Apache-2.0` | `4` | `10 173` | `11 408` | 🔴 **`1 235 B`** |
| 🔴 `AGPL-3.0` | `4` | `34 522` | `35 136` | 🔴 **`614 B`** |
| 🔴 `GPL-3.0` | `1` | `35 149` | `35 149` | — |

🟢 **The four mechanisms behind the spread, each measured: `http://` vs `https://` in the FSF URLs
(`1 B`); line re-wrapping (`~1 B`); the *"APPENDIX: How to apply"* section present or absent
(`~1 200 B`); and a licensor ADDENDUM — the only one that changes TERMS.**
🔴 **`openedx/edx-platform` carries such an addendum, and it is the most consequential sentence this
pass read: EdX Inc. declares that a public, independently available web service communicating with
its code over RPC is NOT a derivative work, and that Corresponding Source excludes that service's
files.** 🟢 **`P167-C` turns that into a composition; `P167-D` replaces the band with a TITLE-LINE
probe.**


## Pass 166 — 2026-10-13

🟢 **`ACTION IP` is DISCHARGED, falsifier SILENT: the false-NEGATIVE guards changed `4` verdicts
across `2` platforms — but only `2` of the `3` guards did any flipping.**
🆕 🔴 **The pass's sharpest result is a verdict that is YES and UNUSABLE at the same time: Moodle
DOES get OneRoster, from a sibling plugin that is `GPL-3.0` and has not been touched in
`2 091` days.**
🆕 🔴 **And a claim this shelf itself published is CORRECTED: `enrol_oneroster` is not *"in-tree"*.**
[`evidence/capability-census.2026-10-13-p166.tsv`](../evidence/capability-census.2026-10-13-p166.tsv)
[`evidence/fn-guard-verdict-changes.2026-10-13-p166.tsv`](../evidence/fn-guard-verdict-changes.2026-10-13-p166.tsv)
[`evidence/sibling-licences.2026-10-13-p166.tsv`](../evidence/sibling-licences.2026-10-13-p166.tsv)

### 🟢 `T179` — the capability census, `2` platforms × `5` standards, every cell measured

🟢 **Trees pinned before probing:** 🟢 **`moodle/moodle` HEAD `f20534726a59`, `2026-10-03`, default
branch `main`, `67 589` tracked paths** 🟢 **· `Selleo/mentingo` HEAD `242a9324fe48`, `2026-10-10`,
`main`, `4 753` paths.**

| platform | standard | naive | guarded | paths | verdict | implementing repo | its licence |
|---|---|---|---|---|---|---|---|
| 🟡 `moodle/moodle` | 🔴 **OneRoster** | `0` | `0` | `0` | 🟡 **IMPLEMENTED-IN-SIBLING** | 🔴 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 **`GPL-3.0`** (`35 149 B`) |
| 🟡 `moodle/moodle` | 🔴 **Ed-Fi** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟡 `moodle/moodle` | 🟢 **LTI 1.3** | `3 472` | `3 415` | **`423`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟡 `moodle/moodle` | 🟢 **SCORM** | `3 158` | `3 149` | **`166`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟡 `moodle/moodle` | 🟢 **xAPI** | `409` | `406` | **`99`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟢 `Selleo/mentingo` | 🔴 **OneRoster** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟢 `Selleo/mentingo` | 🔴 **Ed-Fi** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟢 `Selleo/mentingo` | 🔴 **LTI 1.3** | `1` | `1` | `1` | 🔴 **ABSENT — the hit is an ANTI-CLAIM** | — | — |
| 🟢 `Selleo/mentingo` | 🟢 **SCORM** | `1 660` | `1 660` | **`254`** | 🟢 **IMPLEMENTED-IN-TREE**, player IN-SIBLING | `Selleo/mentingo` + [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **`MIT` + `MIT`** (`1 072 B`) |
| 🟢 `Selleo/mentingo` | 🔴 **xAPI** | `1` | `1` | `1` | 🔴 **ABSENT — the hit is an ANTI-CLAIM** | — | — |

🟢 **Where Moodle's hits actually live, because a count is not a location:**
🟢 **LTI 1.3 — `public/lib/lti1p3` (`43`), `public/enrol/lti` (`19`), `public/mod/lti`** 🟢 **·
SCORM — `public/mod/scorm` (`121`)** 🟢 **· xAPI — `public/lib/xapi` (`56`) plus
`public/mod/h5pactivity` (`14`).** 🟢 **All code. The config-vs-code guard changed nothing on
Moodle, which is itself the result: Moodle's three standards are implementations, not declarations.**

### 🆕 🔴 `T180` — a verdict that is YES and UNUSABLE in the same breath

🔴 **`moodlehq/moodle-enrol_oneroster` is the reason Moodle can claim OneRoster. Measured the moment
it was named, with `P164-D`:**

| field | measured | consequence |
|---|---|---|
| 🟢 existence | 🟢 **EXISTS** — `134` tracked paths | 🟢 the capability is real, and it is out of tree |
| 🔴 **HEAD** | 🔴 **`b91b12857aac`, `2021-01-20`** | 🔴 **`2 091` days — `11.6×` the `180`-day drop threshold** |
| 🔴 **licence** | 🔴 **`GPL-3.0`, body-read `35 149 B`** | 🔴 **`P37`'s stop-ship gate applies; no permissive path** |

🟢 **Report the capability and its maintenance state together, in that order, always.**
🔵 **A verdict of *"yes, via a plugin"* that omits *"last touched January 2021, and it is GPL"* is
worse for a client than a flat *"no"* — because they budget for an integration instead of a build.
`P166-A` STEP 7.**

### 🆕 🔴 `T181` — a correction to this shelf, found by grepping the shelf FIRST

🔴 **`agents/trending.md` has been carrying the phrase *"Moodle's in-tree `enrol_oneroster`"*.**
🔴 **It is not in-tree. `moodle/moodle` returns `0` OneRoster hits across `67 589` paths, on the
name probe AND on the language-independent `imsglobal.org/spec/oneroster` probe.**
🟢 **`enrol_oneroster` is a separate repository under a different org (`moodlehq`, not `moodle`).**
🔵 **This is `T142`'s out-of-repo class, recorded with the direction reversed: the shelf had the
sibling and filed it as core.** 🟢 **Found by `ACTION IS`'s step 0, at a cost of one `grep`.**

### 🆕 🟢 `T182` — the permissive OneRoster path exists, and the shelf already held it

🟢 **`ACTION IP` leaves `3` of `3` recommended platforms with no OneRoster. The substitute was on
the shelf at `89` hits before p166 measured anything:**

| repo | licence | HEAD | age | paths | what it serves |
|---|---|---|---|---|---|
| 🟢 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`**, body-read **`10 173 B`** | `7442047368fa` | 🟢 **`1` d** | `261` | 🟢 **OneRoster 1.2 over `14` GET endpoints** |

🟢 **`P166-B` composes it.** 🟡 **Scoping honesty: `14` GET endpoints is READ rostering. 🔴 **AMENDED p167 (`T189`): `24` GETs over `12` entities; write-back measured at `0` routes.** Write-back
and the Ed-Fi ODS proper are a separate decision this shelf has NOT measured.**

### 🆕 🟢 `T183` — `gap 79` CLOSED, by commit authorship rather than by guesswork

🔵 **Open since p38: which of `Ed-Fi-Alliance-OSS/edfi-oneroster` and `CSR2017/edfi-oneroster` is
upstream.**

| repo | HEAD | date | HEAD commit author | paths | verdict |
|---|---|---|---|---|---|
| 🟢 **`Ed-Fi-Alliance-OSS/edfi-oneroster`** | `7442047368fa` | 🟢 **`2026-10-12`** | 🟢 **`CSR2017`** | **`261`** | 🟢 **UPSTREAM** |
| 🟡 `CSR2017/edfi-oneroster` | `937248be66de` | `2026-09-22` | 🔴 **`dependabot[bot]`** | `252` | 🟡 **FORK** |

🟢 **The mechanism, not just the dates: the Alliance copy is `21` days ahead with `9` more paths,
and its newest commit is authored BY `CSR2017` — the individual commits INTO the Alliance repo.
The personal copy's newest commit is a dependabot bump, which is what a fork on autopilot looks
like.** 🟢 **Both are `Apache-2.0` at `10 173 B`, identical.** 🟢 **Depend on the Alliance repo.**

### 🆕 🔴 `T184` — three published licence SIZE bands are wrong, and the corrections make the test LESS usable

🔴 **`P48` publishes size bands as a family confirmer. p166 body-read a `10 173 B` Apache-2.0 and
went looking:**

| family | published band | measured on this shelf | outside? |
|---|---|---|---|
| 🔴 **Apache-2.0** | `11 357`–`11 358 B` | 🔴 **`10 173`** · `11 342` · `11 408` | 🔴 **all three** |
| 🔴 **GPL-3.0** | `35 121`–`35 147 B` | 🔴 **`35 149`** *(on TWO repos)* | 🔴 **yes, by `2 B`** |
| 🟢 AGPL-3.0 | `34`–`35 KB` | 🟢 `34 522`–`34 523` | 🟢 within |

🟢 **Cause of the Apache outlier, confirmed not guessed: the `10 173 B` body contains `0`
occurrences of `APPENDIX` and ends at *"END OF TERMS AND CONDITIONS"*.** 🟢 **Apache-2.0 is
BIMODAL — with the *"APPENDIX: How to apply"* section it runs ~`11.3`–`11.4 KB`, without it
~`10.2 KB`. Both are Apache-2.0.**
🔵 **And `35 149 B` reproducing on a second, unrelated repository one pass later is the
licence-reproducibility check working.**
🟢 **Net effect: every correction here WIDENS a band, so `P48`'s own thesis — classify by the NAME
LINE, never the size — comes out stronger.** [`evidence/licence-band-correction.2026-10-13-p166.tsv`](../evidence/licence-band-correction.2026-10-13-p166.tsv)

## Pass 165 — 2026-10-13

🟢 **`ACTION IM` is DISCHARGED, falsifier SILENT: `P164-A`'s guards flipped a verdict on BOTH
platforms.** 🆕 🟢 **One genuinely new false-positive class (`T170`), and OpenOLAT's interop
surface is now QUANTIFIED rather than merely located.**
🟢 **`T142`'s plugin finding is corroborated and extended with a per-plugin licence read.**
[`evidence/interop-guarded-grep.2026-10-13-p165.tsv`](../evidence/interop-guarded-grep.2026-10-13-p165.tsv)

### 🆕 🔴 `T170` — the `-ed` + `fi` camelCase collision, a FIFTH false-positive class and the worst one yet

🔴 **Naive `ed-?fi` returned `620` files on OpenOLAT and `159` on edx-platform. Guarded: `0` and
`0`.** 🟢 **A verdict flip on both platforms — precisely what `ACTION IM`'s falsifier asked for,
so it did not fire.**
🟢 **This class is NOT in p164's taxonomy of three, and the shelf has no prior record of it:**

| platform | collision | hits |
|---|---|---|
| 🔴 OpenOLAT | `ableExtendedFilter` | 🔴 **`577`** |
| 🔴 OpenOLAT | `getSelectedFilterTab` · `setSelectedFilterTab` · `extendedFilter` | `204` · `181` · `169` |
| 🔴 OpenOLAT | `uploadedFile` · `scopedFilter` · `reloadedFile` | `114` · `63` · `53` |
| 🔴 edx-platform | `autoCreatedField` · `lastModifiedField` | `111` · `110` |
| 🔴 edx-platform | `SimpleUploadedFile` · `supportedFieldType` · `embeddedFiles` | `94` · `29` · `16` |

🆕 **`T170`:** 🔵 **an English past participle ending `-ed` followed by a noun beginning `fi`
(`field`, `file`, `filter`) is one of the commonest identifier shapes in any codebase. `Ed-Fi`
probed by substring therefore collides SYSTEMATICALLY, not incidentally — `577` hits from a single
identifier.**
🟢 **Rule for every industry shelf, not just this one: never probe `Ed-Fi` as a bare substring.
Require the hyphen with word boundaries, or probe the path plus the vendor namespace.**
🔵 **Distinct from p164's *substring-in-word* class, which was accidental (`facu`*`lti`*`es`): this
one is generated by English morphology and so recurs in every repository of sufficient size.**

### 🆕 🟢 `T171` — OpenOLAT's interop surface, QUANTIFIED

🔵 **The shelf already knew OpenOLAT is `Apache-2.0` and that its `lti13` lives in a directory.**
🟢 **What it did not have is the size of that surface, which is what decides whether a client can
rely on it.** 🟢 **Measured at HEAD `e4be14f0`, branch `master`, `2026-10-12`, `25 823` tracked
paths, full checkout:**

| standard | path hits | guarded content hits | verdict |
|---|---|---|---|
| 🟢 **LTI 1.3** | `361` | `354` | 🟢 **IMPLEMENTED IN-TREE — `org/olat/ims/lti13/`, `145` files, `18 067` Java LOC** |
| 🟢 **SCORM** | `163` | `338` | 🟢 **IMPLEMENTED IN-TREE — `65` Java files** |
| 🔴 OneRoster | `0` | `0` | 🔴 **ABSENT** |
| 🔴 Ed-Fi | `13` *(all false)* | 🔴 **`0`** | 🔴 **ABSENT** *(`T170`)* |
| 🔴 xAPI | `0` | 🔴 **`0`** | 🔴 **ABSENT — the only hits were a vendored `pdf.js` bundle** |

🟢 **Named classes inside the LTI 1.3 package: `LTI13Platform`, `LTI13Dispatcher`, `LTI13Key`
(JWKS), `LTI13DeepLinkingEnum`, `LTI13ContentItem`, `LTI13Context`, `DeploymentConfigurationPermission`.**
🟢 **SCORM: `ScormCourseNode`, `ScormAssessmentHandler`, `ScormAssessmentConfig`, `ScormEditController`.**
🔵 **`18 067` LOC is not a shim. It is a platform-side implementation, which is the side that
matters if the client wants to HOST tools rather than be one.**

🟢 **Corroboration of the shelf's own `T142` while doing this:** 🟢 **`lti_1p3|lti1p3|lti-1p3`
returns `0` files in OpenOLAT, which nonetheless implements the standard completely under the Java
spelling `LTI13`.** 🟢 **The language-independent probe that works on both platforms is the SPEC
URL — `imsglobal.org/spec/lti`: `12` files in OpenOLAT, `2` in edx-platform.**

### 🆕 🟢 `T172` — the Open edX constellation, licensed per repository

🟢 **`T142` established that edx-platform core carries integration points and the implementations
live in sibling packages. p165 read each sibling's licence and release channel, which `T142` did
not do:**

| repository | licence *(body-read)* | paths | HEAD | PyPI |
|---|---|---|---|---|
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** *(`35 136 B`)* | `9 276` | `2026-10-12` | — |
| 🔴 [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **`AGPL-3.0`** | `237` | `2026-10-01` | 🟢 `lti-consumer-xblock v11.4.2`, `2026-10-01` |
| 🔴 [`openedx/event-routing-backends`](https://github.com/openedx/event-routing-backends) | 🔴 **`AGPL-3.0`** | `352` | `2026-10-07` | 🟢 `v10.1.0`, `2026-09-30`, `AGPL-3.0-or-later` |
| 🔴 [`overhangio/openedx-scorm-xblock`](https://github.com/overhangio/openedx-scorm-xblock) | 🔴 **`AGPL-3.0`** | `48` | `2026-10-09` | 🟢 `v19.0.5`, `2026-10-09`, `AGPLv3` |
| 🔴 `openedx/openedx-scorm-xblock` | — | — | — | 🔴 **ABSENT — the SCORM plugin is NOT under the `openedx` org; it is Overhang.IO's** |
| 🔴 `openedx/openedx-oneroster` | — | — | — | 🔴 **ABSENT — no OneRoster repo under the org** |

🆕 **`T172`:** 🔴 **there is no permissive path through Open edX's interop surface at ANY layer —
core, plugin or published package.** 🟢 **PyPI metadata agrees with every `LICENSE` body, which is
a second independent channel on a question where getting it wrong is expensive.**
🔵 **Stated fairly: AGPL-3.0 is a GATE, not a defect, and Open edX remains the most capable OSS
LMS in this field. Whether the gate binds depends on whether the client distributes or offers the
platform as a network service — a question for their counsel.**
🟢 **Set against `T171`, this is a routing decision rather than a preference, and it is filed in
[`verticals/solutions.md`](../verticals/solutions.md).**

### 🆕 🟢 `T176` — the three guards are not equally valuable, and the weighting INVERTS between repositories

🟢 **Measured on `lti` in OpenOLAT, guard by guard:**
`4 987` files → `grep -I` → `4 973` *(binaries: `0.3%`)* → `--exclude='*.po'` → `4 973`
*(i18n: `0`)* → `\b` boundaries → 🟢 **`354`** *(word boundaries: `93%`)*.
🔴 **On OpenEduCat in p164 the weighting was the REVERSE — binaries and Danish `.po` entries did
the damage, and boundaries less.**
🆕 **`T176`:** 🟢 **keep all three guards not because each always fires, but because which one
fires is not predictable from the term or the repository.** 🔵 **A probe that drops the "useless"
guard after one repository will be wrong on the next one.**

🔵 **And one verdict that needed a fourth category rather than a guard:** 🔴 **edx-platform's only
two SCORM hits are both `envs/mock.yml`, and its xAPI hits are `requirements/*.txt`, `uv.lock`, a
migration and an ADR.** 🟢 **Declaring a dependency is not implementing a standard — reported as
CONFIG-ONLY, which is now an explicit verdict in `P165-A`.**

## Pass 164 — 2026-10-13

🟢 **No new platform row this pass.** 🔴 **The row p163 added is DOWNGRADED on measurement, and
p162's cheap-census instrument (`P162-A`) is CORRECTED — it has a failure mode that cost this
pass real time and that the shelf had not recorded.**

### 🆕 🔴 `openeducat/openeducat_erp` — DOWNGRADED from 🟡 to 🔴 on `ACTION IJ`

🟡 **p163 gave it an amber row as *"a REAL, maintained, self-hostable education ERP with
rostering standards — the integration-target class"*.** 🔴 **The rostering standards are not
there.**
[`evidence/openeducat-interop-probe.2026-10-13-p164.tsv`](../evidence/openeducat-interop-probe.2026-10-13-p164.tsv)

| field | p163 | p164 |
|---|---|---|
| 🟢 repo / head | `1c95cef`, branch `19.0` | 🟢 **unchanged, re-confirmed** |
| 🟢 licence | 🔴 LGPL-3.0, body `8 241 B`, INCOMPLETE on its own terms | 🟢 **unchanged** |
| 🟡 **OneRoster / Ed-Fi / LTI 1.3** | 🟡 *vendor-stated, registered as `ACTION IJ`* | 🔴 **ALL THREE ABSENT — `0` implementing code (`T161`)** |
| verdict | 🟡 amber — integration target | 🔴 **red — bespoke integration only** |

🔵 **Why it keeps a row at all:** 🟢 **it is still a real, maintained ERP with `14` in-tree
modules covering admissions, fees, library and timetable, and those are domains the other four
platforms do not touch.** 🔴 **What changed is the cost of using it: with no standards surface,
every integration is bespoke, and that is a different line in an estimate.**

🔵 **The generalisable lesson, which is worth more than the row:** 🟢 **p163 wrote the claim down
as *vendor-stated* and registered it instead of repeating it. One pass later it was measured and
was false.** 🔴 **Had it been written as fact, this shelf would now be recommending a rostering
integration path that does not exist.**

### 🆕 🔴 `P162-A` is CORRECTED — blobless clones have a failure mode, and it is the obvious one

🟢 **p162 and p163 established `--depth=1 --filter=blob:none --no-checkout` as the default
instrument, at `3.1 MB` for Moodle's `67 589` paths.** 🟢 **That measurement is CORRECT and is
re-confirmed this pass.** 🔴 **What was never stated is what happens when you then need the
FILE CONTENTS.**

🔴 **Measured this pass on `openeducat_erp`, `1 345` paths — the smallest tree on this shelf:**

| approach | result |
|---|---|
| 🟢 blobless clone, path census only | 🟢 **`236 KB`, seconds** |
| 🔴 **blobless clone + `git checkout` of the whole tree** | 🔴 **fetches blobs ONE AT A TIME; still running at `35 MB` after several minutes, and was abandoned** |
| 🟢 **plain `--depth=1` clone (one packfile)** | 🟢 **`65 MB`, completed in a single transfer** |

🆕 **`P164-B` — the corrected rule, in three lines:**

1. 🟢 **Path census, licence read, single-file read → blobless `--no-checkout`, then
   `git cat-file`.** 🟢 **Cheapest by a wide margin; `236 KB` beat `65 MB` by `275×` here.**
2. 🔴 **Whole-tree CONTENT sweep → plain `--depth=1`.** 🔴 **Never `checkout` a blobless clone:
   on-demand fetch is per-blob and is slower than downloading everything once.**
3. 🟢 **Subsystem content sweep → blobless + `git sparse-checkout set <dir>`.** 🟢 **Measured
   this pass at `1.4 MB` for OpenOLAT's AI subsystem (`107` Java files) and `3.3 MB` for
   Moodle's (`279` PHP files).**

🔵 **Why this belongs on the foundations page rather than in a footnote: three passes have now
been planned around *"the clone channel is cheap"*, and it is cheap only for the operations it
is cheap for.**

### 🆕 🟢 `P164-A` — the twelve-row recency sweep, and what it costs

🟢 **`T159`'s instrument, stated as a recipe because it is the one this shelf will run every
pass from now on.** 🟢 **Per repository, with no GitHub API and no authentication:**

```sh
git ls-remote --symref https://github.com/$R HEAD     # existence, default branch, HEAD sha
git ls-remote --tags   https://github.com/$R          # full tag list -> release cadence
git clone -q --depth=1 --filter=blob:none --no-checkout https://github.com/$R $D
git -C $D log -1 --format=%cI                         # HEAD commit DATE
git -C $D ls-tree -r --name-only HEAD | wc -l         # tracked paths
```

🟢 **Twelve repositories in parallel: `3 060 KB` total, one pass.** 🟢 **Yields existence
(`P54`), maintenance age, release discipline and project size — four fields, all primary, none
of which the dead `★` column ever provided.**

### 🟢 The foundations shelf — unchanged otherwise

🟡 **No new foundational repository was added this pass.** 🔵 **Deliberate rather than empty: the
three pre-registered actions were all code-channel probes of platforms already on the shelf, and
global discovery returned `0` education-domain candidates for an eighth consecutive pass
(`T110`).** 🟢 **Recorded so the absence is visible as a decision, not an oversight.**

## Pass 163 — 2026-10-13

🟢 **One new platform row, licence read from the body at source, with TWO grant defects measured
rather than inferred.** 🟢 **And p162's cheap-census instrument (`P162-A`) corroborated a second
time on a second repository, at a cost that makes the clone channel the default rather than the
fallback.**
[`evidence/openeducat-grant.2026-10-13-p163.tsv`](../evidence/openeducat-grant.2026-10-13-p163.tsv)

### 🆕 🟡 `openeducat/openeducat_erp` — the Odoo-based education ERP, LGPL-3.0, and its grant is INCOMPLETE BY ITS OWN WORDS

🔵 **Why it was probed:** 🟢 **the vertical-platform query returned a single vendor's marketing
pages and one claim worth testing — that OpenEduCat is an LGPLv3 Python/Odoo alternative to
Moodle with OneRoster, Ed-Fi and LTI 1.3.** 🔴 **A vendor page is not a grant, so the grant was
read from the tree.**

| field | measurement |
|---|---|
| 🟢 repo | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) |
| 🟢 head | `1c95cefebc176a011e3c16269c5a8691fd1ac9cb` |
| 🟡 **default branch** | 🟡 **`19.0`** — *not* `main` or `master`; it tracks the Odoo major version |
| 🟢 last commit | `2026-09-07` |
| 🟢 tracked paths | `1 345` |
| 🟢 licence path | `LICENSE` — 🟢 **the ONLY licence-bearing path in the whole tree** |
| 🟢 licence body | **LGPL-3.0**, `8 241 B`, `178` lines, blob `ef163fea`, sha256 `528f8403…47a9` |
| 🟢 name line | *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* |

🆕 🔴 **Defect 1 — the body promises the GPL and does not contain it.** 🟢 **Its own fourth line
says the LGPL *"is a set of additional permissions on top of the GPL"* and that *"the text of the
GPL is included at the bottom as well"*.** 🔴 **At `8 241 B` it cannot be: GPL-3.0 alone is
~`35 kB`, and the file ends at the LGPL's proxy clause.** 🔵 **LGPL-3.0 is not a standalone
licence by its own construction, so the grant is incomplete on the terms it sets itself.**

🆕 🔴 **Defect 2 — the file it points at is ABSENT.** 🟢 **Line 2 reads *"For copyright
information, please see the COPYRIGHT file"*.** 🔴 **`0` of `1 345` tracked paths match
`/copyright/i`.** 🔵 **This is `P49`'s pattern again — a file named `LICENSE` is not evidence of a
complete grant — now with a dangling reference as well as a short body.**

🟢 **The engagement consequence, stated plainly:** 🔴 **LGPL-3.0 is copyleft, so OpenEduCat is
outside Globant's permissive lane whatever the body says.** 🟢 **It earns a row because it is a
REAL, maintained, self-hostable education ERP with rostering standards — the integration-target
class, not the fork class** — 🔵 **and because the two defects are exactly what a client's licence
review would raise in week one, so finding them now is cheaper than finding them then.**

### 🟢 `P162-A` corroborated a second time — the clone channel is now the DEFAULT instrument

🟢 **p162 measured `--depth=1 --filter=blob:none --no-checkout` at `3.1 MB` for Moodle's
`67 589` paths.** 🟢 **Two independent repeats this pass:**

| repo | `.git` after blobless shallow clone | tracked paths | sparse working tree |
|---|---|---|---|
| 🟢 `openolat/openolat` | **`1.3 MB`** | `25 823` | **`7.0 MB`** for the whole AI subsystem |
| 🟢 `Selleo/mentingo` | **`408 KB`** | `4 753` | **`4.2 MB`** for `apps/api/src/ai` + `packages/prompts` |
| 🟢 `openeducat/openeducat_erp` | *(blobless, no checkout)* | `1 345` | 🟢 **licence read by `cat-file` on a single blob — no checkout at all** |

🔵 **The `cat-file` path is the cheapest grant read this shelf has: resolve the blob id from
`ls-tree`, fetch exactly that object, read the body, hash it.** 🟢 **No working tree, no checkout,
and the sha256 is recorded so the next pass can prove identity without re-reading.**

### 🔴 What this page still cannot do, after p163

- 🔴 **Rank anything. `search/repositories` stays `403` and `ACTION IF` establishes that attaching
  repositories does not reopen it** *(`T149`)*.
- 🟡 **Three passes of OpenOLAT findings and now four rest on ONE tree** (`e4be14f0`, unchanged
  since p160, re-confirmed as HEAD this pass with a `2026-10-12` last commit). 🔵 **Carried
  forward as a concentration risk, not a defect.**
- 🔴 **OpenEduCat's rostering claims (OneRoster, Ed-Fi, LTI 1.3) are VENDOR-STATED and were not
  verified in the tree this pass.** 🟢 **Registered as `ACTION IJ` rather than repeated as fact.**

## Pass 162 — 2026-10-13

🟢 **`ACTION ID` ran on this page's two most load-bearing platform rows and returned the result
this page wanted: `0 of 8` published capabilities fail STEP 7 or STEP 8.**
🔴 **It also found that the audit cannot see what the page never claimed, and that STEP 7 has a
HORIZON on Moodle that it does not have on Django.**
[`evidence/step7-step8-audit.2026-10-13-p162.tsv`](../evidence/step7-step8-audit.2026-10-13-p162.tsv)

### 🟢 `ACTION ID` — DISCHARGED, falsifier SILENT. Every capability this page publishes survives

🔴 **The falsifier was: *"refuted if `≥1` capability currently published for either platform fails
STEP 7 or STEP 8"*.** 🟢 **Eight audited, zero failures.**

| platform | published capability | STEP 7 — deleted by migration? | STEP 8 — out of repo? |
|---|---|---|---|
| 🟡 `moodle/moodle` | Open Badges, `306` paths, OB v2 | 🟡 **NARROWED — `badge.imageauthorname` / `imageauthoremail` / `imageauthorurl` dropped at `2025013100.01`** | 🟢 no |
| 🟡 `moodle/moodle` | xAPI, `78` paths | 🟢 no | 🟢 no |
| 🟡 `moodle/moodle` | LTI 1.3 / `ltiadvantage` | 🟢 no | 🟢 no |
| 🟡 `moodle/moodle` | core AI subsystem, `372` files | 🟢 **no — `ai_provider` CREATED at `2025011700.02`, actively evolving** | 🟢 no |
| 🟢 `Selleo/mentingo` | SCORM, `119` files *(`T135`)* | 🟢 no | 🆕 🟡 **PARTLY — the player is `scorm-again@3.0.4`, an EXTERNAL npm dependency** |
| 🟢 `Selleo/mentingo` | xAPI — published ABSENT *(`T127`)* | n/a | 🟢 **ABSENCE CONFIRMED by a second instrument: `0` `xapi`/`tincan`/`caliper` entries across `7` manifests** |

🟢 **`Open Badges` is narrowed, not deleted — the capability stands and the `306`-path figure is
not retracted.** 🔵 **But a field drop IS the shape `T141` warned about, caught one level down
from where it was expected.**

🆕 🟢 **The SCORM row improves on audit rather than degrading.** 🟢 **`T135` said mentingo ships
SCORM; STEP 8 confirms it from a different channel and names the player:
`@repo/scorm-export-generator` + `@repo/scorm-export-runtime` in-tree, plus
[`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) `3.0.4` at the registry.**
🟢 **Licence closure read from `registry.npmjs.org`: `MIT` over `MIT`. Clean.**

### 🆕 🔴 `T146` — a STEP 7 / STEP 8 audit is structurally blind to a capability nobody published

🔴 **Both steps take the PUBLISHED LIST as their input, so they can only ever confirm or retract
what a previous pass chose to write down.** 🔴 **While auditing mentingo's SCORM row, the
migration directory produced `0162_add_ai_judge_schema.sql` — a complete evaluative AI subsystem
that five passes of this shelf never recorded** *(`T145`, `agents/top.md`)*.

🟢 **`P160-A` gains STEP 9:**

```bash
# STEP 9 (T146) — enumerate the platform's OWN capability vocabulary before auditing the list
#   you already have. The schema and migration names are the platform's self-description.
ls $DIR/**/migrations/*.sql | sed 's/.*[0-9]\{4\}_//;s/\.sql$//' | tr '_' ' ' | sort -u
grep -rhoE 'CREATE TABLE[^"]*"([a-z_]+)"' $DIR --include=*.sql | sort -u
# A capability named in the schema and absent from your published list is a MISS, not a pass.
```

### 🆕 🔴 STEP 7 has a HORIZON on Moodle that it does not have on Django

🟢 **Measured: `public/lib/db/upgrade.php` is `108 269 B` and `90` upgrade steps, covering
`$oldversion < 2022112802` through `< 2026092300`.**
🔴 **Moodle TRUNCATES upgrade history at major releases. Django migrations are RETAINED forever.**
🔵 **So STEP 7 saw every badge deletion in `edx-platform` back to 2023 (`T141`) but can only see
the current window on Moodle — a capability deleted before 2022 is invisible to this instrument,
and the honest form of a Moodle STEP 7 result is *"no deletion in the current upgrade window"*,
not *"never deleted"*.**

🟢 **What STEP 7 did find in the window, in full:** 🔴 **`1` table dropped —
`moodlenet_share_progress` at `2026030600.02`, removing MoodleNet OUTBOUND SHARING along with
`moodlenetprofile` and the MoodleNet OAuth2 config.** 🟢 **No false presence on this shelf:
`moodlenet/moodlenet` was REJECTED on liveness at `2023-07-07` and never published as a
capability.** 🟡 **`8` field drops, of which `3` are the badge attribution fields above and one is
`grade_grades.overriddenmark` at `2025040700.00`.**

### 🟢 STEP 8's verdict on Moodle, which is the useful negative

🟢 **`composer.json` and `package.json` carry `0` matches for `lti`, `xapi`, `caliper`,
`credential` or `badge`.** 🔵 **Moodle vendors its capabilities IN-TREE, so `T142` — the false
absence that a single-repo census publishes on a plugin platform — does NOT apply to Moodle.**
🟢 **Every path count this page publishes for Moodle is therefore safe from the `edx-platform`
defect, and that is now measured rather than assumed.**

### 🆕 🟢 `P162-A` — the path census, PRICED. P161-C's untested prescription is a `240×` saving

🔴 **p160 spent `746 MB` on a Moodle clone. p161 spent `752 MB` trying to avoid it and recorded
that `--filter=blob:none` saves NOTHING with a checkout, correctly prescribing `--no-checkout`
without pricing it.** 🟢 **Priced this pass, same repository, same question:**
[`evidence/clone-instrument-cost.2026-10-13-p162.tsv`](../evidence/clone-instrument-cost.2026-10-13-p162.tsv)

| instrument | disk | wall | what it buys |
|---|---|---|---|
| 🟢 `git ls-remote --symref` | ~`0` | `<1s` | default branch + HEAD |
| 🆕 🟢 **`--depth=1 --filter=blob:none --no-checkout`** | 🟢 **`3.1 MB`** | 🟢 **`1s`** | 🟢 **all `67 589` paths** |
| 🆕 🟢 **`+ cone sparse-checkout` of the directories under test** | 🟢 **`26 MB`** | 🟢 **`2s`** | 🟢 **`677` files of CONTENT, the whole `public/ai` subsystem** |
| 🟢 `raw.githubusercontent.com`, path known | 🟢 **`108 KB`** | `<1s` | 🟢 **`ACTION ID`'s entire Moodle limb** |
| 🔴 `--depth=1` full shallow clone | 🔴 **`746 MB`** | — | the same `67 589` paths |

🟢 **Agreement check, because a cheaper instrument is worthless if it disagrees: `67 589` paths
from the `3.1 MB` clone is byte-identical to p161's `67 589` from the `746 MB` clone.**
🔵 **`240×` cheaper for the census, `28×` cheaper for the subsystem read, same answer.**
🟢 **STEP 1 of `P160-A` splits: STEP 1a paths, STEP 1b sparse content, STEP 1c a full clone only
when the question is genuinely tree-wide.**
## Pass 161 — 2026-10-12

🟢 **Two pre-registered actions discharged on this page: `ACTION HZ` (`OpenOLAT`'s AI surface,
falsifier FIRED) and `ACTION IB` (`P160-A` over `openedx/edx-platform`, falsifier SILENT).**
🔴 **Between them they correct one claim this page has been making and add a fourth contamination
to the path census.**

### 🔴 `ACTION HZ` — REFUTED. OpenOLAT's AI ledger is RICHER than Moodle's, not absent

🔴 **The falsifier was: *"refuted if OpenOLAT ships a per-call AI audit ledger comparable to
`ai_action_register`"*. It ships one, and *comparable* understates it.**
[`evidence/ai-surface-tri-platform.2026-10-12-p161.tsv`](../evidence/ai-surface-tri-platform.2026-10-12-p161.tsv)

| dimension | Moodle `ai_action_register` | OpenOLAT `o_ai_usage_log` |
|---|---|---|
| columns | `15` | 🟢 **`33`** |
| who / where | `userid`, `contextid`, `courseid` | `fk_identity`, `a_usage_context_type`, `a_usage_context_id`, `a_resource_type`, `a_resource_id`, `a_resource_sub_id`, `a_locale` |
| provider / model | `provider`, `model` | `a_model_provider`, `a_req_model`, 🟢 **`a_resp_model`** *(what was ASKED FOR vs what ANSWERED)* |
| request parameters | 🔴 **none** | 🟢 **`a_req_temperature`, `a_req_top_p`, `a_req_max_output_tokens`, `a_req_num_messages`, `a_req_text_length`** |
| tokens | `prompttokens`, `completiontokens` | `a_input_tokens`, `a_output_tokens`, `a_total_tokens`, 🟢 **`a_cached_input_tokens`, `a_reasoning_tokens`, `a_cache_creation_input_tokens`** |
| outcome | `success`, `errorcode`, `errormessage` | `a_status`, `a_error_code`, `a_error_message`, 🟢 **`a_resp_finish_reason`** |
| timing | `timecreated`, `timecompleted` | `creationdate`, 🟢 **`a_duration_millis`** |
| correlation | 🔴 **none** | 🟢 **`a_invocation_id`, `a_resp_id`, `a_service_interface`, `a_service_method`** |
| prompt / response TEXT | 🔴 **yes — in four per-action tables** *(`ACTION IA`, below)* | 🟢 **NO in the log; yes in `o_ai_essay_correction` for the grading feature only** |

🔵 **The honest reading:** 🟢 **OpenOLAT's log is a better COST and RELIABILITY instrument
(parameters, cache tokens, latency, finish reason, call correlation).** 🟢 **Moodle's is a better
EVIDENCE instrument for a regulator, because it keeps what was asked and what came back.**
🔴 **Neither has a retention policy.**

### 🆕 🔴 `ACTION IA` — Moodle's ledger retains BOTH prompt and response, and nothing ever deletes them

🔴 **Falsifier SILENT: the ledger retains prompt AND response text.**
[`evidence/moodle-ai-ledger-schema.2026-10-12-p161.tsv`](../evidence/moodle-ai-ledger-schema.2026-10-12-p161.tsv)

- 🔴 **`ai_action_register` is an INDEX, not the payload.** 🟢 **`actionid` points into one of four
  per-action tables, and three of them —`ai_action_generate_text`, `ai_action_summarise_text`,
  `ai_action_explain_text` — store `prompt text` and `generatedcontent text` verbatim.**
  🔴 **`ai_action_generate_image` stores `prompt`, `revisedprompt` and `sourceurl`.**
- 🟢 **Subject access and erasure are IMPLEMENTED and complete:**
  `core_ai\privacy\provider`, `806` LOC, implements `metadata\provider` +
  `request\subsystem\provider` + `core_userlist_provider`, with `export_user_data`,
  `delete_data_for_user`, `delete_data_for_users`, `delete_data_for_all_users_in_context` and
  `get_users_in_context`. 🟢 **All six AI tables are declared in the privacy metadata.**
- 🔴 **Retention is ABSENT.** 🔴 **`grep -riE 'retention|purge|cleanup|expiry' public/ai/` returns
  nothing but a UI modal's `cleanUp()`; `public/ai` has NO `db/` directory, NO scheduled task and
  NO `settings.php`.** 🟡 **The only task in the subsystem is an adhoc `backfill_action_courseid`.**
- 🟡 **A generic remedy exists and is OFF by default:** `tool_dataprivacy` purposes carry retention
  periods and `tool_dataprivacy\task\delete_expired_contexts` executes them — 🔴 **gated on
  `tool_dataprivacy/automaticdatadeletionapproval`, which ships `0`, and no AI-specific purpose
  ships at all.**
- 🔵 **The client-facing consequence:** 🔴 **a Moodle site that enables AI accumulates every student
  prompt and every model response indefinitely, in a table a GDPR subject-access request will
  correctly export.** 🟢 **`P161-B` is the bounded fix.**

### 🆕 🟢 `ACTION IB` — `edx-platform` HAS tenancy, and the census found a capability that was DELETED

🟢 **Falsifier SILENT.** 🔴 **But a token census says the opposite, and that is the finding.**
[`evidence/edx-tenancy-census.2026-10-12-p161.tsv`](../evidence/edx-tenancy-census.2026-10-12-p161.tsv)

- 🔴 **`ipath '*tenant*'` returns `0`.** 🟢 **Tenancy is PRESENT and is spelled `site`:
  `SiteConfiguration` is a `OneToOneField` on `django.contrib.sites.Site` with a `site_values`
  `JSONField` that overrides settings per tenant; `66` files import `django.contrib.sites`.**
  🔵 **`T136c` — take the vocabulary from the platform — generalises beyond `lti`.**
- 🆕 🔴 **`T141` — a path census cannot see a capability DELETED BY MIGRATION.**
  🔴 **`ipath '*badge*'` returns `38` paths, `23` of them non-test, including a whole
  `lms/djangoapps/badges` app — and `migrations/0005_delete_all_models.py` (2023-10-24) drops
  `BadgeClass`, `BadgeAssertion`, `CourseEventBadgesConfiguration` and
  `CourseCompleteImageConfiguration`. `models.py` is a `25`-line stub.**
  🔵 **The fourth contamination: `T136` over-counts by NAME, this one over-counts by HISTORY.
  The gate is the migration directory, and `P160-A` gains a STEP 7.**
- 🔴 **`T142` — a single-repo clone census UNDER-reads a plugin-architecture platform.**
  🔴 **`lti13` / `lti1p3` / `ltiadvantage` all return `0`; `lti_consumer` returns `3` references —
  the implementation is the separate `lti-consumer-xblock` package, pinned in
  `requirements/edx/base.txt`. `xapi` returns ONE path, a migration adding external-ID types;
  emission lives in `event-routing-backends`.** 🔵 **Read alone, the clone publishes FALSE
  ABSENCES for LTI 1.3 and xAPI. The dependency manifest is the second instrument.**
- 🔴 **`0` AI files, `0` references to any LLM provider — `edx-platform` core has no AI subsystem
  at all**, against Moodle's `372` and OpenOLAT's `149`.
- 🔴 **Licence: AGPL-3.0, body read, `35 136 B`.** 🔴 **It is NOT in the permissive tier and never
  was; this page should say so wherever it recommends Open edX.**
- 🟢 **OB 3.0 / W3C VC: `0` matches.** 🔴 **`0 of 6` platforms on this shelf issue a modern
  verifiable credential** — p159's `0 of 5` extended, and `P159-A` stands as a build.

## Pass 160 — 2026-10-12

🟢 **`ACTION HX` DISCHARGED, falsifier SILENT: Moodle DOES ship Open Badges — `306` paths — so
`T133` is a PATTERN, not one instance, and the *"credentialing has no incumbent"* finding was
wrong on BOTH platforms this shelf recommends.**
🟢 **`ACTION HY` DISCHARGED on both limbs, falsifier SILENT: `0 of 4` permissive platforms issue
an OB 3.0 / W3C Verifiable Credential — and neither does Moodle, so it is `0 of 5`.**
🆕 🟢 **The pass's largest discovery was not registered at all: Moodle ships a provider-pluggable
AI subsystem in CORE, with an audit ledger as database rows.**

### 🆕 🟢 `moodle/moodle` read from the tree — `ACTION HX` in full

🟢 **`746 MB`, `67 589` tracked files, `depth=1` clone of `main`, HEAD `f20534726` identical to
`ls-remote`.** 🟢 **`6.0dev`, build `20261005`, branch `600`, read from `public/version.php`.**
🔴 **Note for every future pass: Moodle's tree moved under `public/` — a probe against
`mod/`, `lib/` or `badges/` at the root returns `0` and means nothing.**
[`evidence/moodle-surface.2026-10-12-p160.tsv`](../evidence/moodle-surface.2026-10-12-p160.tsv)

| dimension | Moodle `6.0dev` | `OpenOLAT` *(p159, re-measured p160)* | who wins for a studio |
|---|---|---|---|
| 🟢 **Licence** | 🟡 **GPL-3.0** — `COPYING.txt`, `35 147 B` | 🟢 **Apache-2.0** — `10 982 B` | 🟢 **OpenOLAT.** 🔵 **No patent grant and no permissive terms in Moodle; `T129`'s original catch, re-confirmed** |
| 🟢 **LTI 1.3 both ways** | 🟢 **YES** — `mod/lti` as platform (`254` files), `enrol/lti` + `auth/lti` as tool (`154`), `lib/lti1p3` | 🟢 **YES** — `lti13.platform.iss` + `LTI13Platform` | 🟢 **Tie** |
| 🟢 **AGS / NRPS / Deep Linking / JWKS** | 🟢 **ALL FOUR** — `gradebookservices/.../lineitem.php`, `nrps_info.php` + `sync_members.php`, `openid-configuration.php` + `contentitem.js`, `ltiopenid/jwks_helper.php` + `enrol/lti/jwks.php` | 🟢 **ALL FOUR** | 🟢 **Tie** |
| 🟢 **Open Badges** | 🟢 **YES — `306` paths**, `assertion.php`, `badgeclass.php`, `criteria/`, backpack export | 🟢 **YES — `182` paths** | 🟢 **Tie** |
| 🔴 **Open Badges version** | 🔴 **`v2` ONLY — `OPEN_BADGES_V2` ×`132`, `V1` ×`2`, `backpack_api2p1_mapping.php`** | 🔴 **`v2` ONLY** | 🔴 **Neither.** 🆕 **`ACTION HY`'s answer** |
| 🔴 **OB 3.0 / W3C VC** | 🔴 **ABSENT — `0` on eight spellings** | 🔴 **ABSENT — `0`** | 🔴 **Neither** |
| 🟢 **xAPI** | 🟢 **PRESENT — `public/lib/xapi`, `78` paths: `api.php`, `iri.php`, `state_store.php`, `handler.php`** | 🔴 **ABSENT — `0`** | 🟢 **MOODLE — and this is the FIRST capability on this shelf where Moodle beats OpenOLAT** |
| 🔴 **cmi5** | 🔴 ABSENT | 🔴 ABSENT | 🔴 Neither |
| 🟢 **SCORM** | 🟢 `226` paths | 🟢 `186` paths | 🟢 Tie |
| 🔴 **QTI** | 🔴 **`8` paths and ALL of them are QTI `v1.2` LEGACY** — IMS Common Cartridge `.xsd` schemas and a Blackboard import format. 🔴 **No QTI 2.x/3.0 engine** | 🟢 **`919` paths — a full QTI 2.1 assessment engine** | 🟢 **OpenOLAT, decisively. 🔵 For an assessment-heavy engagement this one dimension settles the platform choice** |
| 🔴 **Multi-tenancy** | 🔴 **ABSENT in core.** 🔴 **`62` *"tenant"* paths exist and `62 of 62` are inside the VENDORED `public/lib/google2-service`** *(`T136`)* | 🔴 **ABSENT** *(hierarchical organisations, not tenants)* | 🔴 **Neither.** 🟢 **`Selleo/mentingo` is still the only row on this shelf with a real tenancy boundary (PostgreSQL RLS, MIT)** |
| 🆕 🟢 **AI subsystem in CORE** | 🟢 **YES — `public/ai`, `372` files** | 🟡 **not measured this pass** | 🟢 **Moodle** |
| 🔴 **MCP server** | 🔴 ABSENT | 🟡 not measured | 🔴 Neither |

### 🆕 🟢 `T139` — Moodle's core AI subsystem logs every call as DATABASE ROWS, which is the audit artefact `P158-A` assembled by hand

🟢 **`public/lib/db/install.xml` defines seven core AI tables:** 🟢 **`ai_action_register`,
`ai_action_generate_text`, `ai_action_generate_image`, `ai_action_explain_text`,
`ai_action_summarise_text`, `ai_policy_register`, `ai_providers`.**
🟢 **`ai_action_register`'s own fields:** `actionname`, `actionid`, `success`, `userid`,
`contextid`, `courseid`, `provider`, `model`, `prompttokens`, `completiontokens`, `errorcode`,
`errormessage`, `timecreated`, `timecompleted`.

| layer | what ships | why a studio cares |
|---|---|---|
| 🟢 **Providers, pluggable** | 🟢 **`anthropic`, `awsbedrock`, `azureai`, `deepseek`, `gemini`, `ollama`, `openai`** — seven, `209` files | 🟢 **`ollama` in core means the SOVEREIGN deployment is a configuration, not a fork** — 🔵 **directly answers the EMEA data-residency objection** |
| 🟢 **Per-call ledger** | 🟢 **`ai_action_register` rows: who, which course, which provider, which model, tokens, success, error, timings** | 🟢 **This is the artefact an appeal or a regulator asks for.** 🔵 **`P158-A` built it from Langfuse traces; on Moodle it is already there, GPL-3.0** |
| 🟢 **Consent gate** | 🟢 **`ai_policy_register` + `policy_acceptance_report.php` + a `reportbuilder` system report** | 🟢 **Per-user AI-policy acceptance, reportable** — 🔵 **what the EU AI Act's transparency duty and the US state transparency clauses actually ask to evidence** |
| 🟢 **Rate limiting** | 🟢 **`public/ai/classes/rate_limiter.php`** | 🟢 Cost control in core |
| 🔴 **Actions — and this is the finding** | 🔴 **FOUR, and NONE is evaluative: `generate_text`, `generate_image`, `summarise_text`, `explain_text`** | 🔴 **Moodle core AI does NOT grade, score or place a learner.** 🟢 **So core Moodle sits OUTSIDE the EU AI Act's Annex III evaluative tier — and the moment a plugin adds an evaluative action, that plugin carries the high-risk obligations.** 🔵 **`P160-B` is built on exactly that line** |

🆕 **`T139`:** 🔵 **the governed-AI plumbing a client engagement would otherwise build — provider
abstraction, per-call audit, policy acceptance, rate limiting — is already in Moodle core and is
GPL-3.0.** 🟢 **What is NOT there is the evaluative capability, the tenancy boundary, and OB 3.0.**
🟢 **That is a far better starting position than this shelf has been assuming, and it changes
where the billable work sits.**

### 🟢 `ACTION HY`, second limb — `openlxp/openlxp-xia` assessed, and this shelf's description of it was WRONG

[`evidence/openlxp-xia-assessment.2026-10-12-p160.tsv`](../evidence/openlxp-xia-assessment.2026-10-12-p160.tsv)

| dimension | finding |
|---|---|
| 🟢 **Licence** | 🟢 **Apache-2.0, `11 357 B`, body-read — CONFIRMED** |
| 🔴 **What it is** | 🔴 **A `53`-file Django APP installed with `pip install OpenLXP-XIA`, not a platform.** 🟢 **A V-T-V-L pipeline: Validate → Transform → Validate → Load, for learning-experience METADATA** |
| 🔴 **Not learning RECORDS** | 🔴 **`0` matches for `xapi`, `caliper` or `statement`.** 🔴 **This shelf's `verticals/solutions.md` called it *"learning-record PLUMBING"* — it is metadata CATALOGUING plumbing. Corrected this pass** |
| 🔴 **Maintenance** | 🔴 **Last commit `2026-02-26` — `228` days, and it was a README edit.** 🔴 **`Django>=3.2.3,<4.0.0` — Django 3.2 reached END OF LIFE in April 2024; `boto3~=1.16.54`, `coverage<6.0`: a 2021-era pin set** |
| 🔴 **Needs siblings** | 🟢 **`openlxp/openlxp-xis` and `openlxp/openlxp-xss` RESOLVE.** 🔴 **`openlxp/openlxp-xsr-aws` DOES NOT RESOLVE — a credential prompt, so private or absent** *(`P54`)*. 🟡 **AWS S3 is the only schema server** |
| 🔴 **Verdict** | 🔴 **Do not put it in front of a client as a platform.** 🟡 **Permissive, readable and small enough to vendor the V-T-V-L idea from; shipping it as-is imports an EOL framework pin** |
## Pass 159 — 2026-10-12

🔴 **`ACTION HT` DISCHARGED and its falsifier is SILENT — but the pass that verified `OpenOLAT`
also discovered that this shelf's licence gate reports *"no licence"* for MOODLE.**
🟢 **Both findings are below, and the second one is the more important.**

### 🆕 🔴 `T129` — the licence gate's probe list produced FALSE ABSENCES at `4 of 15`, and the blind spots track project MATURITY

🟢 **The gate was run on a KNOWN-ANSWER control: fifteen platform and foundational rows whose
licences are not in doubt.** 🔴 **Four came back `NO_LICENCE_FILE`.**
[`evidence/licence-path-false-absence.2026-10-12-p159.tsv`](../evidence/licence-path-false-absence.2026-10-12-p159.tsv)

| repo | the 9-path list said | the licence is actually at | and it is |
|---|---|---|---|
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`COPYING.txt`** *(35 147 B)* | 🟢 **GPL-3.0** |
| 🔴 [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`license.txt`** *(35 149 B)* | 🟢 **GPL-3.0** |
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`license.txt`** *(33 893 B)* | 🔴 **AGPL-3.0 — STRICTER than ERPNext's GPL** |
| 🔴 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🔴 **`NO_LICENCE_FILE`** | 🟡 **`NOTICE.txt`** *(545 B)* | 🟡 **Apache-2.0 ASSERTED — and no licence TEXT anywhere in the tree** |

🆕 **`T129`, and the mechanism is the point:** 🟢 **GitHub's *"Add license"* button writes
`LICENSE`.** 🔴 **Projects that predate it, or that follow the GNU convention (`COPYING.txt`) or a
framework's house style (`license.txt`), do not.**
🔴 **So the probe list's blind spots are CORRELATED WITH MATURITY** — 🔴 **which means this
shelf's licence-absence claims were safest exactly where it sampled (the hobby tail, which uses
the button) and WRONG where it mattered most: the platform tier it puts in front of clients.**
🟢 **The same extended probe recovered only `2 of 47` in the `1 ★` tail — `4.3%` there against
`26.7%` on the control.** 🔵 **`T106`'s family again: the instrument's error rate is not constant
across the population it is used on.**

🟢 **`P56` is written** *(see `compose/patterns.md`)*: 🟢 **33 paths, SPDX line first, family read
from the TITLE line, and a byte floor that belongs to the family.**

### 🟢 `ACTION HT` — `OpenOLAT` speaks LTI 1.3 in BOTH directions, and the falsifier is SILENT

[`evidence/openolat-surface.2026-10-12-p159.tsv`](../evidence/openolat-surface.2026-10-12-p159.tsv)

🟢 **`org/olat/ims/lti13` — `148` path matches.** 🟢 **p158's expectation is CONFIRMED, which
matters because `ACTION HR` fired on exactly this expectation one pass ago.**

| dimension | finding | how measured |
|---|---|---|
| 🟢 **Licence** | 🟢 **Apache-2.0**, `10 982 B` | body read on `master` — 🔴 **its default branch is `master`, not `main`** |
| 🟢 **LTI 1.3 — as a PLATFORM** | 🟢 **`lti13.platform.iss`** — OpenOLAT issues as a platform and hosts external tools | `LTI13Module.java` read from `raw` |
| 🟢 **LTI 1.3 — as a TOOL** | 🟢 **`LTI13Platform` stores an EXTERNAL platform's `issuer`, `clientId`, `authorizationUri`, `tokenUri`, `jwkSetUri`** — which is exactly what a Tool keeps about its Platform | `LTI13Platform.java` |
| 🟢 **AGS** *(grade passback)* | 🟢 **`model/json/LineItem.java`, `LineItemScore.java`** | code search |
| 🟢 **NRPS** *(names & roles)* | 🟢 **`model/json/Member.java`, `Context.java`** | code search |
| 🟢 **Deep Linking** | 🟢 **`LTI13ContentItem.java`** | code search |
| 🟢 **OIDC / JWKS** | 🟢 **`OIDCApi.java`, `LTI13Key.java`, private/public key handling** | code search + `raw` |
| 🟢 **Named integrations** | 🟢 **`ZOOM`, `JUPYTER_HUB`, `MEDIASITE_GLOBAL`, `MEDIASITE_COURSE`, `EXTERNAL`, `EXT_TEMPLATE`, `SHARED`** | `LTI13ToolType.java` enum |
| 🟢 **QTI 2.1** | 🟢 **`org/olat/ims/qti21` — `660` path matches**, a full assessment engine | code search |
| 🟢 **SCORM** | 🟢 **`org/olat/modules/scorm` + `ScormCourseNode` — `154` paths** | code search |
| 🔴 **xAPI** | 🔴 **ABSENT — `0` matches across FOUR spellings** *(`xapi`, `cmi5`, `"Tin Can"`, `"experience api"`)* | code search |
| 🟢 **Open Badges** | 🟢 **`org/olat/modules/openbadges` — `156` paths**, `v2` package, LinkedIn push | code search — 🆕 **see `T133`** |
| 🔴 **Open Badges 3.0 / W3C VC** | 🔴 **ABSENT — `0` matches for `OpenBadgeCredential`, `VerifiableCredential`, `openbadges/v3`** | code search |
| 🟢 **Tenancy** | 🟢 **HIERARCHICAL organisations — materialized-path tree, `matchOrganisationOrItsParents`, `customerNumber`, `externalId`, per-organisation role grants, `15` `*ToOrganisation` scoping types** | `Organisation.java`, `RolesByOrganisation.java` |
| 🟡 **Tenancy enforcement** | 🟡 **APPLICATION-level. No row-level security.** | 🔵 **The honest contrast with `mentingo` — see below** |

🟢 **Cost of the whole assessment: `8` code searches, `7` `raw` fetches, one `ls-remote`. No clone.**
🟢 **`P55` holds a second time: *"does it integrate with X?"* is settled from the tree, not the
feature table.**

### 🆕 🔴 `T132` — the GitHub topic list is unreliable in BOTH directions

🔴 **p158's `T127` caught `mentingo`'s topic list OVER-claiming: it advertised `scorm` and `xapi`
the schema does not have.**
🔴 **`OpenOLAT` UNDER-claims: its topics are `qti`, `scorm`, `lms`, `curriculum-management`,
`assessment` — and `lti` is NOT among them**, although LTI 1.3 is its deepest integration
surface at `148` paths, in both directions, with AGS, NRPS and Deep Linking.
🆕 **`T132`:** 🔵 **a topic list is marketing, and marketing both exaggerates and forgets.**
🟢 **It can never settle a capability question in either direction — not presence, and not
absence.**

### 🟢 Tenancy, compared honestly — two different guarantees, not one better one

| | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(MIT)* | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) *(Apache-2.0)* |
|---|---|---|
| **shape** | 🟡 **FLAT** — `tenantId` ×154 | 🟢 **HIERARCHICAL** — materialized path, parent matching |
| **enforced where** | 🟢 **DATABASE** — PostgreSQL RLS, least-privilege runtime role | 🟡 **APPLICATION** code |
| **what it buys** | 🟢 ***"a bug in application code cannot read another tenant's rows"*** | 🟢 **faculty → department → programme, with roles granted per node** |
| **where it fits** | 🟢 **Many unrelated customers on one deployment** | 🟢 **ONE institution with real internal structure** |

🔵 **Neither dominates.** 🔴 **A studio that wants a DB-level guarantee and a hierarchy has
neither off the shelf** — 🟢 **and that is a build, not a search.**

### 🟢 The foundational shelf, every licence re-read with the corrected gate

[`evidence/foundations-licences.2026-10-12-p159.tsv`](../evidence/foundations-licences.2026-10-12-p159.tsv)

| repo | default branch | licence *(body-read)* | tier |
|---|---|---|---|
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** *(10 982 B)* | 🟢 **Permissive + patent grant** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `main` | 🟢 **MIT** *(1 062 B)* | 🟢 **Permissive** — 🟢 **fourth consecutive confirming pass** |
| 🟢 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | `main` | 🟢 **Apache-2.0** *(11 357 B)* | 🟢 **Permissive** — 🆕 **NEW to this shelf: a learning-experience data pipeline** |
| 🟢 [`openfun/richie`](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** *(1 079 B)* | 🟢 **Permissive** |
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | `main` | 🟢 **MIT** *(1 066 B)* | 🟢 **Permissive** |
| 🟡 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🔴 `master` | 🟡 **Apache-2.0 asserted in `NOTICE.txt`** *(545 B)*, no licence text in tree | 🟡 **Usable, but the grant is a NOTICE not a LICENSE** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** *(`COPYING.txt`, 35 147 B)* | 🟡 **Copyleft — cross at a protocol boundary** *(`P156-A`)* |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `master` | 🟡 **AGPL-3.0** *(35 136 B)* | 🔴 **Hosting is distribution** |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** *(35 147 B)* | 🟡 **Copyleft** — 🆕 **a THIRD default-branch convention** |
| 🟡 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** *(35 147 B)* | 🟡 **Copyleft** |
| 🟡 [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **`20.0`** | 🟡 **LGPL-3.0** *(43 529 B; its `LICENSE` defers to a `COPYRIGHT` file)* | 🟡 **Copyleft, library-scoped** |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** *(8 241 B)* | 🟡 **Copyleft** — 🟢 **confirmed on a FIFTH ref** |
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`develop`** | 🔴 **AGPL-3.0** *(`license.txt`)* | 🔴 **Hosting it for a client is distribution** |
| 🔴 [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **`develop`** | 🟡 **GPL-3.0** *(`license.txt`)* | 🟡 **Copyleft** |
| 🔴 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🔴 `master` | 🔴 **LGPL-3.0** *(`LICENSE.txt`, 7 650 B)* | 🔴 **CORRECTION — p157 offered this as a BUILD BASE without naming its copyleft** |

🔴 **`9` of `15` are copyleft; `5` are permissive; `1` carries only a NOTICE.**
🔴 **`8` of `15` do NOT default to `main`** — `master` ×5, plus `release_11`, `20.0`, `19.0` and
`develop` ×2. 🟢 **`P53` is not an edge case on this shelf; it is the majority case.**
🟢 **And the search channel's `default_branch` agreed with `ls-remote` on `100 of 100` tail rows**,
🔵 **so resolving the ref is now cheap — but `ls-remote` is still what proves the repository
EXISTS** *(`P54`)*.
## Pass 158 — 2026-10-12

🔴 **`ACTION HR` DISCHARGED and its falsifier FIRED. `Selleo/mentingo` does NOT speak LTI 1.3,
and this shelf has been recommending it inside `P156-A` on the assumption that it does.**
🟢 **Four passes of carrying it unassessed is over: data model, multi-tenancy, SCORM surface and
LTI support are all now measured from the repository itself.**
[`evidence/mentingo-surface.2026-10-12-p158.tsv`](../evidence/mentingo-surface.2026-10-12-p158.tsv)

### 🔴 `ACTION HR` — LTI 1.3 is ABSENT, and the claim this shelf repeated came from a topic list

🔴 **`lti` appears 4 times in the `100 244 B` schema module. All four are substrings of other
words** — `multirange` ×3, `totalTime` ×1. 🔴 **There is no LTI table, no LTI column, no LTI
dependency in `apps/api/package.json`.**
🔴 **`xapi` appears `0` times.**

🔴 **The only place `LTI` and `xAPI` appear in the whole repository front matter is inside an
HTML comment in the README, in Polish, which translates as:**

> *"STAGE 3 — to be confirmed by the team, DO NOT PUBLISH WITHOUT VERIFICATION: ISO 27001
> (Selleo certificate or only process conformity?), WCAG 2.1 AA (accessibility audit), DPA/GDPR
> template, pentest, **xAPI/LTI**, mapping to NIS-2 / art. 8e KSC, retention and data deletion."*

🟢 **So the maintainers know these are unverified, and deliberately commented them OUT of the
rendered README.** 🔴 **This shelf nevertheless published *"SCORM + xAPI"* on this row for four
passes** — 🔴 **read, on p157's own account, from the repository's GitHub TOPIC LIST.**

🆕 **`T127`:** 🔴 **a FEATURE claim fails across instruments exactly the way `T117` showed a
LICENCE claim fails, and the ranking of instruments is the same** — 🟢 **the data model is
authoritative, the rendered README is cautious, and the topic list is marketing.**
🔵 **`T110`, `T117`, `T120`, `T121` and now `T127`: on this shelf, every instrument that is cheap
to read is the one that is wrong.**

### 🟢 What `mentingo` actually is, measured

| dimension | finding | how measured |
|---|---|---|
| 🟢 **Licence** | 🟢 **MIT**, `1 062 B`, *"Copyright (c) 2024 Selleo"* | body re-read on `main` — **CONFIRMED, third pass running** |
| 🔴 **LTI 1.3** | 🔴 **ABSENT** | `0` real hits in schema; unverified HTML comment only |
| 🔴 **xAPI** | 🔴 **ABSENT** | `0` hits in schema |
| 🟡 **SCORM** | 🟡 **README says *"SCORM 1.2 export"*. The SCHEMA carries `scorm_packages`, `scorm_scos`, `scorm_attempts` and `scorm_runtime_state`, plus 5 SCORM enums including `scormStandardEnum`** | 🟢 **Runtime + attempt state is what a PLAYER needs, not an exporter** — 🟡 **so the README understates it. The enum's members live in `@repo/shared` and were NOT read this pass** |
| 🟢 **Multi-tenancy** | 🟢 **PostgreSQL Row-Level Security with a least-privilege runtime role (`LMS_DATABASE_URL`) and per-tenant domains.** `tenants` table; `tenantId` ×154 and `withTenantId` ×98 in the schema | 🟢 **`docs/architecture.md`: *"A bug in application code cannot read another tenant's rows through that connection."*** 🔵 **DB-enforced, not app-enforced — the strongest tenancy claim on this shelf** |
| 🟢 **Data model** | 🟢 **`104` tables, `12` enums, `3 103` lines, `100 244 B`, Drizzle ORM** | `apps/api/src/storage/schema/index.ts` |
| 🆕 🟢 **AI mentor** | 🟢 **7 tables** — `aiMentorLessons`, `aiMentorConfigurations`, `aiMentorTeacherConfigurations`, `aiMentorRoleplayConfigurations`, `aiMentorThreads`, `aiMentorPracticeSessions`, `aiMentorThreadMessages` | schema |
| 🆕 🟢 **LLM-as-judge assessment engine** | 🟢 **7 tables** — `aiJudgeConfigurations`, `aiJudgeCriteria`, `aiJudgeScoreGuidance`, `aiJudgeBlockingErrors`, `aiMentorJudgements`, `aiMentorJudgementCriteria`, `aiMentorJudgementBlockingErrors` | 🟢 **Rubric criteria, score guidance AND hard-fail *blocking errors*, modelled in the database.** 🔵 **NOTHING ELSE ON THIS SHELF HAS THIS** |
| 🟢 **RAG** | 🟢 `documents`, `docChunks`, `documentToAiMentorLesson`, `searchDocuments` over **PostgreSQL 16 + pgvector** | schema + architecture doc |
| 🟢 **Also in the model** | 🟢 **Learning paths (7 tables, incl. path certificates), RBAC policy engine (5 tables: roles, rule sets, rule-set permissions), live training + attendance (7 tables), calendar sync inbound/outbound, `outboxEvents` transactional outbox, `courseAuthoring*` agent surface (4 tables), `integrationApiKeys`, `certificates`, `forms`** | schema |
| 🟢 **Stack** | 🟢 **NestJS 10 + CQRS · Drizzle · PG 16 + pgvector · Redis + BullMQ · Socket.IO · Remix/React · LiveKit voice · Langfuse tracing · Vercel AI SDK + OpenAI · LangChain** | README *At a glance* + `apps/api/package.json` |
| 🟢 **Distribution** | 🟢 **AWS Marketplace one-click CloudFormation**, self-host, or Selleo-managed | README |
| 🟡 **UI languages** | 🟢 **English, Polish, German, Spanish, French, Czech** | 🟢 **Spanish present.** 🔴 **No Portuguese — a real gap for Brazil** |
| 🟢 **Refs** | `39` heads on origin | `git ls-remote --heads` |

### 🔴 The consequence for this shelf's own advice, stated plainly

🔴 **`P156-A` layer 5 is LTI 1.3. Its closing paragraph offers `mentingo` as a drop-in swap for
layer 1. Those two sentences are incompatible, and p158 is the pass that found it.**

🟢 **The corrected reading:**

| engagement | does `mentingo` fit? |
|---|---|
| 🔴 **University / K-12, existing LMS estate, tools federated over LTI** | 🔴 **NO.** 🟢 **Moodle, Open edX, OpenOLAT, Sakai, ILIAS and Chamilo all speak LTI 1.3; `mentingo` does not. `P156-A` keeps layer 1 copyleft-but-unmodified for exactly this reason** |
| 🟢 **Corporate L&D / HRTech, greenfield, white-label, resold** | 🟢 **YES, and it is the best row on this shelf for it** — MIT, DB-level tenancy, AI mentor and judge in the core, AWS Marketplace deployment |

🟢 **`mentingo`'s own README says this before this shelf did** — *"Mentingo is a TypeScript
platform designed for corporate L&D… If you need a large academic plugin ecosystem, choose
Moodle."* 🔴 **The shelf filed it as *"the only MIT LMS"* and inherited an academic framing the
project never claimed.** 🟢 **It is not a Moodle replacement; it is a Docebo/TalentLMS
replacement, under MIT.**

### 🆕 🟢 `P55` — settle an interoperability question from the DATA MODEL, not the feature table

🟢 **Cost of this assessment: `6` `raw` fetches and one `ls-remote`. No clone.**
🟢 **The decisive artefact was `apps/api/src/storage/schema/index.ts` — a single `100 KB` module
that answered LTI, xAPI, SCORM, tenancy and subsystem inventory at once.**
🆕 **`P55`: for any *"does it integrate with X?"* question, grep the schema and the dependency
manifest. A feature table states intent; a table definition states what ships.**
🔵 **`P52`'s channel map made this free: metadata from search, bodies from `raw`, refs from
`ls-remote` — and a schema file is just another body.**

### 🔴 Open on this page after p158

- 🔴 **`scormStandardEnum`'s members are unread** — they live in `@repo/shared`. 🟡 **Whether `mentingo` supports SCORM 2004 as well as 1.2 is therefore still unknown, and the README's own TODO asks the same question about IMPORT.**
- 🟢 **`mentingo` is no longer an open gap.** 🔵 **Four passes of *"unassessed beyond licence"* are closed.**
- 🔴 **No foundational row other than `mentingo` has had its data model read.** 🟡 **`OpenOLAT` (Apache-2.0, the other fork-safe platform) is the one that matters next, and it is the one that DOES speak LTI and QTI.**

## Pass 157 — 2026-10-12

🟢 **`ACTION HM` DISCHARGED after three unreached passes. The foundational tier finally has an
attention measurement beside its licences** — 🔴 **and the number is the most important thing
this shelf has measured about the market it sells into.**
🟡 **Discharged on a SUBSTITUTED instrument, and this pass says so rather than claiming the
registered one worked.**

### 🔴 `T118` — attention has DECOUPLED from deployment, and the gap is 1.7×

🔴 **One tutoring repository has more GitHub stars than the ENTIRE institutional platform tier
put together.**
[`evidence/platform-attention.2026-10-12-p157.tsv`](../evidence/platform-attention.2026-10-12-p157.tsv)

| | ★ |
|---|---|
| 🟢 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor), one repository | **41 210** |
| 🔴 **All 13 platform + foundational rows below, summed** | **23 945** |
| 🔴 **Ratio** | 🔴 **1.72 ×** |

🔴 **And `moodle/moodle` — the most-deployed open-source LMS on earth, vendor-reported at 400M+
users and 150k+ sites — has `7 475 ★`.** 🔴 **`DeepTutor` has `5.5 ×` that.**
🔴 **`bigbluebutton` (`9 241`) outranks Moodle too**, so 🔵 **inside the tier the ordering is not
deployment either — the videoconferencing layer beats the system of record.**

🟢 **What a studio should take from this, stated plainly:**
- 🔴 **Stars measure developer attention, NOT installed base.** 🟢 **On this shelf the two are
  not merely different, they are nearly inverted, and the inversion is 1.7× at the top.**
- 🔵 **So a shortlist built by sorting stars will recommend the tutoring layer and miss the
  system of record the client actually runs** — 🟢 **which is `P156-A`'s whole premise, now with
  a number behind it instead of an assumption.**
- 🟢 **And the converse: a client's installed platform will never look exciting on GitHub.**
  🔵 **Do not let a star count argue you into forking it.**

### 🟢 The foundational and platform tier — ★, activity and licence, all measured

🟢 **13 of 14 rows served ★ and `pushed_at`.** 🟢 **Every row is ACTIVE** — 🔵 **twelve of
fourteen pushed within four days of this pass, which is itself the answer to *"is this
maintained?"***

| repo | ★ | last push | licence *(body-read, path recorded)* | what it is, and the licence consequence |
|---|---|---|---|---|
| 🔴 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **9 241** | `2026-10-11` | 🔴 **LGPL-3.0** (`LICENSE`, 7 652 B) | 🟢 **The virtual-classroom layer: WebRTC, whiteboard, breakouts, recording.** 🟡 **LGPL — link freely, modifying the library is not free.** 🔵 **Top of the tier by attention** |
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | **7 475** | `2026-10-12` | 🔴 **GPL** (🆕 `COPYING.txt`, 35 147 B — `P50`) | 🟢 **The most-deployed open-source LMS.** 🔴 **GPL: a distributed derivative ships source.** 🟢 **Plugin-boundary work is the commercial route** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **1 237** | `2026-10-10` | 🟡 **ECL-2.0** (`LICENSE`, 11 120 B) | 🟢 **Apache-2.0 derivative, permissive, built for university consortia.** 🔵 **Permissive route #2** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **1 143** | `2026-10-12` | 🟢 **MIT** (`LICENSE`, 1 097 B) | 🟢 **Offline-first, built for low/no-connectivity deployment.** 🔵 **The LATAM and Africa infrastructure row, and MIT** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | **1 011** | `2026-10-12` | 🔴 **GPL** (`LICENSE`, 35 147 B) | 🟢 **Lightweight LMS with real deployment in francophone and LATAM public education** |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **887** | `2026-10-12` | 🔴 **LGPL-3.0** (🆕 `19.0/LICENSE`, 8 241 B) | 🟢 **Education ERP on Odoo: admissions, fees, timetable, library.** 🆕 🟡 **Default branch is `19.0`, not `master`** — see the correction below |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | **664** | `2026-10-12` | 🔴 **19 B stub, no licence field in `pyproject.toml`** | 🟢 **School management on Frappe/ERPNext.** 🔴 **The grant has NO readable surface. Do not build a deliverable on it without asking the maintainer** |
| 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **646** | `2026-10-12` | 🔴 **GPL-2.0** | 🟢 **Student Information System — enrolment, attendance, gradebook.** 🔵 **The SIS lane, and the only row here that is a SIS rather than an LMS** |
| 🔴 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **505** | `2026-10-12` | 🔴 **GPL** | 🟢 **Institutional LMS, strong DACH public-sector deployment.** 🟡 **Default branch `release_11`** |
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **447** | `2026-10-12` | 🟢 **Apache-2.0** (`LICENSE`, 10 982 B) | 🟢 **A full institutional LMS under a PERMISSIVE licence WITH a patent grant.** 🔵 **The fork-safe platform route, and the most under-rated row on this shelf at 447 ★** |
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **446** | `2026-10-11` | 🟢 **MIT** (`LICENSE`, 1 066 B) | 🟢 **DKT, AKT, SAKT knowledge tracing on standard datasets.** 🔵 **The one row that answers *"does the student know it?"* with a model.** 🟢 **MIT, so it ships inside a client product** |
| 🔴 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | **150** | `2026-09-08` | 🔴 **GPL** (`LICENSE.txt`, 35 146 B) | 🟢 **Interactive content types that drop into Moodle, Open edX and Canvas.** 🔵 **Content layer, not a platform** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **93** | `2026-10-12` | 🟢 **MIT** (`LICENSE`, 1 062 B) | 🟢 **The only MIT LMS. AI-native, SCORM + xAPI, white-label.** 🟡 **EMEA — Poland.** 🔴 **Still unassessed beyond licence, ★ and region, FOURTH pass** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **NOT SERVED** | — | 🔴 **AGPL-3.0** (🆕 re-read `master/LICENSE`, 35 136 B) | 🔴 **AGPL reaches a HOSTED derivative, not just a shipped one.** 🔵 **The most common MOOC platform and the most restrictive licence in this table** |

🟢 **Permissive routes through this tier, and there are exactly four:** 🟢 **`OpenOLAT`
(Apache-2.0)** · 🟡 **`sakai` (ECL-2.0)** · 🟢 **`mentingo` (MIT)** · 🟢 **`kolibri` (MIT)**.
🔴 **Everything else is GPL, LGPL or AGPL.**

### 🆕 🔴 `T120` — a `repo:` search miss is NOT evidence of absence

🔴 **`openedx/edx-platform` was absent from TWO independent `repo:`-qualified searches**, which
would read as a deleted or renamed repository. 🟢 **It is neither:**

| probe | result |
|---|---|
| 🔴 `repo:openedx/edx-platform` in two separate queries | 🔴 **absent both times** — 6 of 7, then 7 of 8 |
| 🟢 `raw.../openedx/edx-platform/master/LICENSE` | 🟢 **`200`, `35 136 B`, GNU AFFERO GENERAL PUBLIC LICENSE** |
| 🔴 `raw.../openedx/edx-platform/main/LICENSE` | 🔴 **`404` — there is no `main`; the ref is `master`** |

🔴 **A second row behaves the same way:** `LAION-AI/Desktop_BUD-E` is absent from `repo:` search
and 🟢 **answered `ls-remote` with two refs and served a `4 970 B` README on `raw`.**
🆕 **`T120`:** 🟢 **an index miss and a dead repository are indistinguishable from inside the
search channel**, 🔴 **so *"not found"* from a search endpoint is never publishable as
*"gone"* — 🟢 **it costs one `ls-remote` to tell them apart, and this shelf now pays it.**

### 🟢 `P52` — the channel map, measured rather than assumed

🟢 **p156 recorded *"`api.github.com` refuses this session, `403` on all 17 owners"* as a
categorical gap.** 🟢 **It is narrower than that, and the shelf has been leaving metadata on
the table.**
[`evidence/channel-map.2026-10-12-p157.tsv`](../evidence/channel-map.2026-10-12-p157.tsv)

| channel | status | what it answers |
|---|---|---|
| 🔴 `curl api.github.com` | 🔴 **`403`, 2nd pass** | 🔴 nothing |
| 🔴 `curl github.com` *(rendered)* | 🔴 **`403` this session** | 🔴 nothing — 🟡 **so p156's rendered channel is not reproducible by curl here** |
| 🟢 **GitHub MCP `search_repositories`** | 🟢 **`200` for ANY public repo** | 🟢 **population counts, ★, forks, open issues, SPDX licence, `default_branch`, `pushed_at`, `archived`, topics** |
| 🔴 GitHub MCP `list_branches` / `get_file_contents` | 🔴 **refused outside this session's own repos** | 🔴 nothing third-party |
| 🟢 `raw.githubusercontent.com` | 🟢 **`200`** | 🟢 **file BODIES, any public repo, any ref** |
| 🟢 `git ls-remote --heads` | 🟢 **15 of 15** | 🟢 **the complete ref list for any public repo** |

🆕 **`P52`** — 🟢 **the GitHub channel is SPLIT, not closed: GLOBAL SEARCH endpoints answer for
any repository, PER-REPOSITORY endpoints are scoped to this session.** 🟢 **So the working
triple is: metadata from search, bodies from `raw`, refs from `ls-remote`** — 🔵 **and together
they cover everything this shelf had been treating as unreachable for three passes.**

### 🆕 🟢 CORRECTION, and it strengthens p156 rather than weakening it

🔴 **p156 probed `openeducat_erp`'s `COPYRIGHT` pointer on `master`, `18.0` and `17.0` and found
`404` on all three. None of those is the default branch** — 🟢 **the default is `19.0`.**
🟢 **Probed this pass: `19.0/LICENSE` = `200`, `8 241 B`, LGPLv3 — identical. `19.0/COPYRIGHT` =
`404`.**
🟢 **So `ACTION HB`'s conclusion HOLDS on the branch it had not examined, and the dangling
pointer is now confirmed on FOUR refs.** 🔵 **Stated because the gap was real even though the
answer did not change** — 🟢 **and because it is the same defect `P53` was written for, found in
this shelf's own prior work rather than in someone else's repository.**

## Pass 156 — 2026-10-12

🟢 **Every licence on this page is now read from a BODY on `raw.githubusercontent.com`, this
pass, with the PATH that answered recorded next to it.**
🔴 **And the pass found the reason a licence sweep lies: the most-deployed LMS in the world does
not keep its licence in a file called `LICENSE`.**
[`evidence/foundations-licences.2026-10-12-p156.tsv`](../evidence/foundations-licences.2026-10-12-p156.tsv)

### 🆕 🔴 `P50` — probe `COPYING*` before concluding a repository has no licence

🔴 **`moodle/moodle` returned `404` on `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`,
`COPYING` and `license`, across both `main` and `master`.** 🟢 **Its licence is at
`COPYING.txt` — `35 147 B`, the full GNU GPL text.**
🔴 **A sweep that stopped at `LICENSE*` would have published *"Moodle: no licence file"***, which
is 🔴 **both false and the single most damaging error this shelf could make**, since Moodle is
the row most engagements start from.
🆕 **`T109`** — 🟢 **a licence-absence claim is a claim about the PATHS PROBED, and it is only as
strong as that list.** 🟢 **`P50` therefore requires the probe list to be published with the
verdict**, which this page now does.

### 🟢 The foundational layer, licence read from the body this pass

| repo | licence *(body-read)* | path that answered | bytes | what it is, and the licence consequence |
|---|---|---|---|---|
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | `LICENSE` | 1 066 | 🟢 **Knowledge tracing: DKT, AKT, SAKT and more on standard datasets.** 🟢 **MIT, so the learner model can ship inside a client product.** 🔵 **The one row on this shelf that answers *"how do you know the student knows it?"*** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | `LICENSE` | 1 097 | 🟢 **Offline-first learning platform built for low/no-connectivity deployment.** 🟢 **MIT.** 🔵 **The LATAM and Africa infrastructure row — and the UNESCO IESALC finding below is exactly its market** |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | `LICENSE` | 10 982 | 🟢 **A full institutional LMS under a PERMISSIVE licence with a patent grant.** 🔵 **The copyleft-free LMS route — confirmed again this pass** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | `LICENSE` | 1 062 | 🟢 **The only MIT-licensed LMS on this shelf.** 🟡 **EMEA — Poland** *(`P36`, verified owner profile, this pass)*. 🔴 **Still unassessed beyond licence, ★ and region** |
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL** | 🆕 **`COPYING.txt`** | **35 147** | 🟢 **The most-deployed open-source LMS; vendor reports 400M+ users, 150k+ sites** *(self-reported)*. 🔴 **GPL: a distributed derivative must ship source.** 🟢 **Plugin-boundary work is the normal commercial route** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | `LICENSE` | 35 136 | 🔴 **AGPL — network use counts, so a hosted derivative triggers disclosure.** 🟡 **The most common MOOC platform and the most restrictive licence in this table** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** | `LICENSE` | 11 120 | 🟢 **Educational Community License 2.0 — an Apache-2.0 derivative, permissive, built for university consortia.** 🔵 **Permissive route #2** |
| 🔴 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | `LICENSE` | 7 652 | 🟢 **The virtual-classroom layer: WebRTC, whiteboard, breakouts, recording.** 🟡 **LGPL — linking is fine, modifying the library is not free** |
| 🔴 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL** | `LICENSE.txt` | 35 146 | 🟢 **Interactive content types that drop into Moodle, Open edX and Canvas.** 🔵 **The content layer, not a platform** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL** | `LICENSE` | 35 147 | 🟢 **Lightweight LMS with real deployment in francophone and LATAM public education** |
| 🔴 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL** | `LICENSE` | 35 147 | 🟢 **Institutional LMS, strong in German-speaking EMEA** |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0**, 🔴 **from a 19 B stub** | `license.txt` | **19** | 🔴 **The whole grant is the string `License: GNU GPL V3`.** 🔴 **`pyproject.toml` carries NO licence field**, so 🔴 **the `-only` / `-or-later` question has no surface at all** *(carried from p155, unchanged)* |

🟢 **Twelve rows, twelve bodies read, twelve paths recorded.**
🟢 **Permissive and safe to build on: `pykt-toolkit` (MIT), `kolibri` (MIT), `OpenOLAT`
(Apache-2.0), `mentingo` (MIT), `sakai` (ECL-2.0) — five of twelve.**
🔴 **Seven of twelve are copyleft**, and 🔴 **the two platforms a client is most likely to already
run — Moodle and Open edX — are the GPL and AGPL rows.**

### 🔵 What this means for a studio, stated once

🟢 **The engagement shape that survives this licence table is the SAME in every region:**
🟢 **leave the LMS alone and compose beside it.** 🔴 **Moodle's GPL and Open edX's AGPL make a
forked, resold platform a disclosure event**; 🟢 **an MIT/Apache agent that talks to the LMS over
LTI, MCP or REST carries none of it. See `compose/patterns.md` `P156-A`.**

### 🔴 Open on this page

- 🔴 **No star count for ANY row above — a THIRD unreached pass.** 🟢 **The rendered topic page
  can serve it; nothing else is blocking.**
- 🔴 **`mentingo` still unassessed on data model and multi-tenancy** — the only MIT LMS.
- 🔴 **No credentialing or skills-pathway repository, in 156 passes**, against a 2026 trend
  source that names digital credentials as a live buyer demand.
- 🔴 **No evaluation harness.** 🟢 **`pykt-toolkit` is the nearest thing and it models learners,
  it does not evaluate a tutor.**


## Pass 155 — 2026-10-12

🟢 **`ACTION GQ` DISCHARGED — and it REFUTES a warning this shelf has published for two
passes.** 🔴 **`openeducat_erp`'s licence was readable the whole time**: `LICENSE` on `master`
returns **`200`, 8 241 B**, and its first sentence names **LGPL-3.0**.
🔴 **And the pass's main finding is a defect in this shelf's own gate: `P44`'s size check
cannot tell the licence families apart.** 🔴 **Three measured collisions, the worst 11 bytes
wide, all on fresh reads taken this pass.**

### 🟢 `ACTION GQ` — the two ERP rows, answered from bodies

[`evidence/licence-name-channel.2026-10-12-p155.tsv`](../evidence/licence-name-channel.2026-10-12-p155.tsv)

p153's falsifier: *"refuted if the tree says something OTHER than the one-liner and the README
say."* 🟢 **SILENT on both rows — the trees AGREE with the declarations.** 🔴 **But the reach
claim was wrong, and that is the finding.**

| row | what the shelf published | what the body says | verdict |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 *"LGPL-3.0 — README-declared, **NOT file-read**"*, with a *"do not quote"* warning | 🟢 **`LICENSE` = `200`, 8 241 B, 178 lines: *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below."*** Identical body on `master`, `18.0` and `17.0` | 🟢 **LGPL-3.0 CONFIRMED from the body.** 🔴 **The *"not file-read"* warning is WITHDRAWN** |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 *"GPL-3.0 — a ONE-LINE declaration, ~20 B"* | 🟢 **`license.txt` on `develop` = exactly `19 B`: `License: GNU GPL V3`.** 🔴 **`pyproject.toml` exists (1 622 B) and carries NO licence field at all.** `main` 404s — the default branch is `develop` | 🟡 **CONFIRMED, and SHARPENED below** |

🔴 **Why the `openeducat` error happened, said rather than smoothed.** 🟢 **`P45` and `T92` —
this shelf's own channel for reading a licence without a clone — were created in p153.**
🔴 **Nobody aimed them at the two rows the shelf was warning about.** `ACTION GQ` was written
as *"CLONE `frappe/education` and `openeducat_erp`"*, so it inherited a clone budget it never
needed and went unreached for two passes. 🆕 **`T100`: an action phrased around an expensive
instrument outlives the cheap instrument that replaced it.**

### 🆕 🔴 `openeducat_erp` carries a carve-out in its preamble — `T92`'s SECOND instance

🔴 **Before the LGPL text begins, the body says:**

> *"Some external libraries and contributions bundled with OpenEduCat may be published under
> other GPL-compatible licenses. For these, please refer to the relevant source files and/or
> license files, in the source code tree."*

🔵 **So the root grant is LGPL-3.0 and the tree is not uniformly LGPL-3.0 — by the root file's
own admission.** 🟢 **This is exactly `scibly-dev/scibly`'s shape from p154** (AGPL-3.0 at the
root, proprietary inside `ee/`), 🟢 **so `T92` — *a licence can be a property of the PATH, not
the repository* — now has TWO instances, and the second is a row a studio bills against.**
🔴 **It is no longer an anecdote.** 🟢 **`P47`'s path-licence gate is therefore mandatory on
this row**, and the carve-out is *declared*, which makes it cheap to honour and inexcusable to
miss.

### 🆕 🔴 `frappe/education`: a 19-byte grant whose VERSION DIRECTION is unanswerable

🟢 **Exact, not approximate: 19 bytes.** `License: GNU GPL V3` — and 🔴 **`pyproject.toml`, the
one other surface that could speak, is silent.** 🔴 **One declaration surface, 19 bytes, no
`-or-later`, no `-only`.**

🔵 **Why that is worse than a long copyleft licence.** `P43` turns on exactly this word:
Moodle's **GPL-3.0-or-later** gives a relicensing route, Canvas's **AGPL-3.0-only** does not.
🔴 **`frappe/education` does not say**, so 🔴 **`P43` cannot be run on it at all** — the
question has no surface to read. 🟢 **Previously published as *"GPL if the one-liner binds"*;
🟢 the correct statement is *"GPL version 3, with the or-later/only question UNANSWERABLE from
any surface in the repository."*** 🔵 **For an engagement: that is a question for Frappe
Technologies in writing, not a question for an auditor.**

### 🆕 🔴 `T97` / `P48` — `P44`'s size check is REFUTED as a family discriminator

[`evidence/band-collision.2026-10-12-p155.tsv`](../evidence/band-collision.2026-10-12-p155.tsv)

`P44` step 4 reads: *"MIT ≈ 1 062–1 105 B, Apache-2.0 ≈ 11 357–11 358 B, GPL-3.0 ≈ 35 121–35 147 B,
AGPL-3.0 ≈ 34–35 KB."* 🔴 **Three collisions, measured this pass:**

| # | the pair | bytes | gap | if you trusted size |
|---|---|---|---|---|
| 🔴 **1** | **MIT** cluster *(ten bodies, 1 062–1 102 B)* vs 🔴 **AGPL-3.0 short form** — [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 1 102 vs **1 134** | 🔴 **32 B** | 🔴 **You read the STRONGEST COPYLEFT as the MOST PERMISSIVE licence.** The worst direction that exists |
| 🔴 **2** | **Apache-2.0** — [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) vs **ECL-2.0** — [`sakai`](https://github.com/sakaiproject/sakai) | 10 982 vs **11 120** | 🔴 **138 B** | 🔴 ECL-2.0's **narrowed patent grant** collapses into Apache-2.0's standard one |
| 🔴 **2b** | **Apache-2.0's own RANGE** — `feifei-companion` 10 227 → `DeepTutor` 11 408 | 1 181 B wide | — | 🔴 **The Apache range BRACKETS ECL-2.0 entirely.** The two are not separable by size in principle, not just in practice |
| 🔴 **3** | **GPL-3.0** — `moodle/moodle` `COPYING.txt`, 🟢 **re-read fresh this pass** vs **AGPL-3.0** — `openedx/edx-platform` `LICENSE` | 35 147 vs **35 136** | 🔴 **11 B** | 🔴 **You lose *network use counts as distribution*** — the single most consequential distinction for a hosted LMS |

🟢 **Both figures in collision 3 are fresh reads taken this pass**, not a carried band against
a new measurement: `moodle/moodle/main/COPYING.txt` = **35 147 B, `GNU GENERAL PUBLIC LICENSE`**;
`openedx/edx-platform/master/LICENSE` = **35 136 B, `GNU AFFERO GENERAL PUBLIC LICENSE`**.
🔴 **The AGPL body sits INSIDE the band this shelf uses to confirm GPL-3.0.**

🟢 **What survives.** Size still catches the `P411` shape — 🟢 **a body that CLASSIFIES as one
family but is the wrong SIZE for it is a flag** (`PageLM`'s 8 563 B "MIT"). 🟢 **And a 19-byte
or 1 134-byte body is a flag by itself: a grant too short to be a licence text.**
🔴 **What dies is size as a CONFIRMER of family.** 🆕 **`P48` replaces it: read the NAME LINE.**
🟢 **This pass classified 19 of 19 bodies by name line with zero ambiguity**, including both
AGPL short-form and full-text bodies in the same sweep.

### 🆕 🟢 New foundational rows, licences read from bodies

| repo | licence *(body-read)* | bytes | `HEAD` | why it is here |
|---|---|---|---|---|
| 🆕 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | **10 982** | `e4be14f` | 🟢 **A full Java institutional LMS under a STANDARD permissive licence.** 🔵 **This shelf has said for several passes that `sakai` (ECL-2.0) is *"the"* copyleft-free LMS — 🔴 that is now WRONG: there are TWO, and the newcomer carries the better-understood grant** |
| 🆕 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** — 🔴 **version 2, not 3** | **15 214** | `22ec5ba` | 🟢 **A K-12 Student Information System** — attendance, grades, scheduling, the inputs a dropout-prediction agent needs. 🔴 **The secondary source that surfaced it said only *"GPL"*; the body says **Version 2**, and `P43`'s whole question lives in that number** |
| 🆕 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **1 062** | `242a932` | 🟢 **The only MIT-licensed LMS this shelf has found.** 92 ★, young — 🔵 **but it is the only row where the platform licence imposes nothing at all** |

### 🆕 🔴 `T96` — third-party comparison sites misreport platform licences, and the error UNDERSTATES copyleft

🔵 **The layer a studio's first-pass shortlist is actually built from is the comparison
article, not the repository.** 🔴 **Three of three platform licences cross-checked against the
secondary sources that surfaced them this pass are wrong or imprecise:**

| platform | what secondary sources said | what the BODY says | the error |
|---|---|---|---|
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 one source: *"Apache License 2.0: Used by Open edX"* *(another said AGPLv3)* | 🔴 **AGPL-3.0**, 35 136 B, name line `GNU AFFERO GENERAL PUBLIC LICENSE` | 🔴 **AGPL → Apache. Understates copyleft — the dangerous direction, same as `T89`'s badge** |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 *"Apache 2.0"* *(another said ECL v2)* | 🟢 **ECL-2.0**, 11 120 B, name line `Educational Community License, Version 2.0 (ECL-2.0)` | 🟡 **Apache-DERIVED is not Apache.** ECL-2.0 narrows the patent grant — material for a studio |
| 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 bare *"GPL"* | 🔴 **GPL-2.0**, 15 214 B | 🔴 **Version dropped**, which is where `P43` lives |

🟢 **So `T89` generalises off the repository.** p153 found a repo whose own badge contradicted
its own `LICENSE`; 🔴 **p155 finds the same error direction one layer out, in the sources a
shortlist is built from, and the sources CONTRADICT EACH OTHER on the same platform in the
same search.** 🔵 **Operationally: a licence column in a comparison article is a hypothesis.
`P48` costs one `curl`.**

##### 🔴 What this page still cannot do, after p155

- 🔴 **`openeducat_erp`'s per-directory carve-out is DECLARED but UNMEASURED** — nobody has
  enumerated which bundled paths are not LGPL. 🔵 **`ACTION HB`.**
- 🔴 **`frappe/education`'s version direction is unanswerable from the repo.** 🔵 **Ask the vendor.**
- 🔴 **No star count for ANY foundational row** — `ACTION GN`, unreached a second pass.
- 🔴 **`P44` step 4 is now known-wrong in the published text below**; 🟢 **`P48` supersedes it
  in `compose/patterns.md`**, and the older text is left standing as history rather than
  silently edited.


## Pass 154 — 2026-10-12

🟢 **Two foundational layers this shelf has been reasoning ABOUT without ever enumerating are
now enumerated with licences attached: ASSESSMENT/GRADING and KNOWLEDGE TRACING.**
🔴 **And the second one — the layer every adaptive-learning claim rests on — is HALF
UNGRANTED.**

### 🔴 The knowledge-tracing layer: permissive or ungranted, never copyleft

🔵 **Why this layer decides an engagement.** Every "adaptive", "personalised" or "mastery"
claim a studio makes needs a learner model underneath it. `topic:knowledge-tracing` is **86
repositories**; here are the top 20 by stars, licence read from the API's detector.

| repo | licence | ★ | last push | what it is |
|---|---|---|---|---|
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **446** | 2026-10-11 | 🟢 **The field's benchmark library** — already this shelf's KT reference, now with a star figure |
| [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) | 🟢 **MIT** | **194** | 2022-06-16 | A collection of KT implementations. 🔴 **Four years cold** |
| [`jhljx/GKT`](https://github.com/jhljx/GKT) | 🟢 **MIT** | **141** | 2021-03-19 | Graph-based KT (IJCAI). 🔴 **Five years cold** |
| [`jilljenn/ktm`](https://github.com/jilljenn/ktm) | 🟢 **MIT** | **140** | 2025-08-12 | 🟡 **EMEA (inferred)** — Knowledge Tracing Machines: factorization machines for KT |
| 🔴 [`ckyeungac/deep-knowledge-tracing-plus`](https://github.com/ckyeungac/deep-knowledge-tracing-plus) | 🔴 **NO GRANT** | **124** | 2019-01-08 | DKT+ |
| [`lccasagrande/Deep-Knowledge-Tracing`](https://github.com/lccasagrande/Deep-Knowledge-Tracing) | 🟢 **MIT** | **107** | 2020-12-04 | DKT in TF2 |
| 🔴 [`arshadshk/SAINT-pytorch`](https://github.com/arshadshk/SAINT-pytorch) | 🔴 **NO GRANT** | **94** | 2022-04-26 | 🔴 **SAINT — one of the transformer KT baselines everybody cites** |
| 🔴 [`seewoo5/KT`](https://github.com/seewoo5/KT) | 🔴 **NO GRANT** | **90** | 2024-08-11 | KT models in PyTorch |
| 🔴 [`ApexEDM/GIKT`](https://github.com/ApexEDM/GIKT) | 🔴 **NO GRANT** | **83** | 2021-07-17 | Graph interaction KT |
| [`tswsxk/EduData`](https://github.com/tswsxk/EduData) | 🟢 **Apache-2.0** | **83** | 2023-05-03 | 🟢 **Education datasets + a download/preprocess interface** — the data side of the layer |
| [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | 🟢 **MIT** | **82** | 2026-09-17 | 🟢 **Active.** KT + cognitive diagnosis + exercise recommendation in one library |
| [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) | 🟢 **MIT** | **78** | 2026-01-06 | 🔵 **APAC** — unified student-modelling library (FCS 2025) |
| 🔴 [`yxonic/DTransformer`](https://github.com/yxonic/DTransformer) | 🔴 **NO GRANT** | **46** | 2025-03-24 | 🔴 **Diagnostic-transformer KT — a current-generation model with no grant** |
| 🔴 [`arshadshk/Last_Query_Transformer_RNN-PyTorch`](https://github.com/arshadshk/Last_Query_Transformer_RNN-PyTorch) | 🔴 **NO GRANT** | **45** | 2021-04-08 | Kaggle-winning architecture |
| 🔴 [`TianHongZXY/pytorch-SAKT`](https://github.com/TianHongZXY/pytorch-SAKT) | 🔴 **NO GRANT** | **38** | 2023-07-23 | SAKT |
| 🔴 [`xiaopengguo/ATKT`](https://github.com/xiaopengguo/ATKT) | 🔴 **NO GRANT** | **34** | 2021-11-01 | Adversarial-training KT (ACM MM, oral) |
| [`THUwangcy/HawkesKT`](https://github.com/THUwangcy/HawkesKT) | 🟢 **MIT** | **31** | 2023-09-14 | 🔵 **APAC** — temporal cross-effects (WSDM'21) |
| [`jdxyw/deepKT`](https://github.com/jdxyw/deepKT) | 🟢 **MIT** | **28** | 2021-11-05 | KT in PyTorch |
| 🔴 [`ZhijieXiong/dlkt`](https://github.com/ZhijieXiong/dlkt) | 🔴 **NO GRANT** | **17** | 2025-09-04 | 🟢 **Migrated to `pyedmine`** — follow the successor |
| 🔴 [`HFUT-LEC/awesome-student-cognitive-modeling`](https://github.com/HFUT-LEC/awesome-student-cognitive-modeling) | 🔴 **NO GRANT** | **14** | 2024-08-01 | Resource list |

🔴 **The count: 10 of 20 carry NO GRANT. 9 are MIT, 1 is Apache-2.0. ZERO are copyleft.**

🟢 **That distribution is the commercially useful fact on this page.** A studio reaching for
the layer finds no GPL trap — 🔴 **it finds an EMPTY GRANT, which is strictly worse, because
copyleft at least tells you the price.** 🔴 **And the ungranted rows are not the fringe**:
SAINT, SAKT, DTransformer and ATKT are the transformer baselines a client's data-science
reviewer will ask for by name.
🟢 **The buildable path is therefore `pykt-toolkit` (MIT) or `pyedmine` (MIT, active) as the
substrate, with `EduData` (Apache-2.0) for datasets** — and any paper implementation treated
as a SPEC to reimplement, never as a dependency.

### 🟢 The assessment / grading layer — enumerated for the first time

🔵 **`topic:grading` is 259 repositories.** The rows that matter for an education engagement,
licence from the API's detector:

| repo | licence | ★ | last push | region | what it is |
|---|---|---|---|---|---|
| 🟢 [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** | **1 374** | 2026-10-01 | Global | 🟢 **The most-starred permissive grading system in open source.** Assign, release, collect and autograde notebooks. 🟢 **`HEAD` `f9915da`** |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟡 **NOASSERTION** | **437** | 2026-10-07 | 🟡 North America | Full course environment with assessment. 🔴 **Read the body before adopting** (`P47`) |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🟡 **NOASSERTION** | **243** | 2026-10-12 | 🟡 **EMEA** | 🟢 **Secure, automated exercise assessment running the instructor's own tests** — the grading substrate for programming courses |
| 🔴 [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | 🔴 **GPL-3.0** | **85** | 2026-10-06 | 🟡 North America | Checks writers' and programmers' work |
| 🆕 🔴 [`five-plus-one/AI-Marker-Suite`](https://github.com/five-plus-one/AI-Marker-Suite) | 🔴 **GPL-3.0**, body-read **35 154 B** | **79** | 2026-10-12 | 🔵 **APAC** | 🟢 **AI marking over 24 named incumbent platforms** — the retrofit pattern |
| 🔴 [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) | 🔴 **NO GRANT** (8 paths probed) | **74** | 2026-10-06 | 🟡 North America | Offline React app for digital math homework |
| 🔴 [`zmievsa/autograder`](https://github.com/zmievsa/autograder) | 🔴 **GPL-3.0** | **48** | 2024-07-15 | — | Assignment grading for programming courses |
| 🔴 [`ai-lingnan/econai-agent-platform`](https://github.com/ai-lingnan/econai-agent-platform) | 🔴 **AGPL-3.0** | **38** | 2026-07-17 | 🔵 **APAC** | 🟢 **Dual-agent parallel grading** |
| 🔴 [`federicazoe/gradetools`](https://github.com/federicazoe/gradetools) | 🔴 **GPL-3.0** | **35** | 2025-07-24 | 🟡 North America | R package for a grading workflow |
| 🔴 [`sourcegrade/jagr`](https://github.com/sourcegrade/jagr) | 🔴 **AGPL-3.0** | **33** | 2026-10-07 | 🟡 **EMEA** | Java autograder in Kotlin |
| 🟢 [`pedal-edu/pedal`](https://github.com/pedal-edu/pedal) | 🟢 **MIT** | **32** | 2026-08-24 | 🟡 North America | 🟢 **Static + dynamic analysis of student Python with feedback generation** — permissive, and the right shape to put an agent behind |

🔴 **The grading layer is COPYLEFT-HEAVY, and the inverse of the modelling layer.** Of those
11 rows: **2 permissive (`nbgrader` BSD-3, `pedal` MIT)**, **6 copyleft**, **2 NOASSERTION**,
**1 ungranted**.
🟢 **So the composable grading stack has exactly two entry points** — and both are real:
`nbgrader` for notebook-based courses, `pedal` for Python feedback. 🔵 **Everything else is a
licence conversation before it is an engineering one.**

### 🟢 Spaced repetition, added as a foundational row

| repo | licence | ★ | last push | why it is foundational |
|---|---|---|---|---|
| 🟢 [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4 101** | 2026-08-14 | 🟢 **The FSRS scheduler — the most-starred permissive row in the whole retention layer.** `HEAD` `ff7c85c` |
| 🟢 [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** | **515** | 2026-10-11 | 🟢 **The MCP boundary onto Anki** — an agent can read and write a learner's real review queue. `HEAD` `e0e347f` |

🔵 **Why these belong next to the KT rows and not in a curiosities drawer.** `pykt` tells you
what a learner knows; **FSRS tells you when to ask again**. 🟢 **A retention claim with no
scheduler underneath it is a chatbot with a syllabus.**

🟢 **All 23 rows probed this pass verified by `git ls-remote`, 23 of 23, negative control
returned nothing**
([`evidence/ls-remote-verification.2026-10-12-p154.tsv`](../evidence/ls-remote-verification.2026-10-12-p154.tsv)).

##### 🔴 What this page still cannot do, after p154

- 🔴 **Every licence above except two is from the API's DETECTOR, not from the body.** The
  two body-reads are `AI-Marker-Suite` (35 154 B, GPL-3.0) and the three absences confirmed
  by probe. 🔵 **`ACTION GU`**: body-read the 11 grading rows before any of them is quoted.
- 🔴 **`inducer/relate` and `INGInious` are `NOASSERTION`** — the `scibly` class. Unread.
- 🔴 **The 10 ungranted KT rows were not contacted and no issue was filed.** An ungranted
  repo can be granted on request; nobody has asked.

## Pass 153 — 2026-10-12

🟢 **18 of 18 rows verified for EXISTENCE and `HEAD` by `git ls-remote`, with a negative
control that fires** — and 🟢 **every licence below read from the LICENCE FILE BODY**, not
from a sidebar, a badge or this shelf's memory.
🆕 **A new channel does it for one round trip per repo and no clone.**

### 🟢 The foundational layer, with the licence read from the file and the file's size as its tell

🔵 **Why the byte size is published next to the licence.** This shelf learned at `P411`
that a proprietary licence can open with the MIT grant verbatim; **the tell was the size**
— 8 563 B against ~1 070 B for a real MIT. 🟢 **So every row carries the body size, and the
sizes cluster exactly as a clean corpus should**: MIT **1 062–1 105 B**, Apache-2.0
**11 357–11 358 B**, GPL-3.0 **35 121–35 147 B**.

| repo | licence (read from the body) | body | `HEAD` | why it is foundational |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **GPL-3.0-or-later** | 35 147 B | `f205347` | The world's most-deployed LMS. 🟢 **p152 measured the election: 13 859 of 14 024 notices say `-or-later`** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | — | `b3f862e` | MOOC-grade LMS behind edX. 🟡 **Root-only notice surface (p152)** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0-only** | — | `1c9f0bb` | 🔴 **`-only` elected BY OMISSION in 16 896 files** (`T85`, p152) — the strictest row here, and it reads as silent to a naive matcher |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **LGPL-3.0-or-later** | — | `1524a63` | Virtual classroom with an LMS-native integration path. 255 of 263 notices `-or-later` (p152) |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | — | `10a1d90` | Apache-derived, university-governed LMS. 🟢 **The most permissive copyleft-free LMS of the big four** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | — | `d3de265` | 🟢 **Offline-first learning platform, MIT.** The row for low-connectivity deployments — LATAM rural, Africa, APAC islands |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | — | `948a378` | *"Framework for building custom learning components that run in the Open edX LMS"* — 🟢 **the permissive entry point into an AGPL platform** |
| [`netless-io/flat`](https://github.com/netless-io/flat) | 🟢 **MIT** | **1 062 B** | `d194d5b` | 🟢 **The largest permissive synchronous-classroom codebase this shelf has measured** |
| [`OpenVidu/openvidu`](https://github.com/OpenVidu/openvidu) | 🟢 **Apache-2.0** | **11 357 B** | `ba72e6b` | Self-hosted real-time video over LiveKit/mediasoup. 🟢 **Permissive substrate for live tutoring** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** | **1 094 B** | `d0cd78c` | 🟢 **A PERMISSIVE SIS** — the layer where this shelf had only copyleft and non-OSI |
| [`Ilyas-Codes/eCourse`](https://github.com/Ilyas-Codes/eCourse) | 🟢 **MIT** | **1 062 B** | `3ee89f6` | 🟢 **Lightweight LMS without Moodle's copyleft** |
| [`geli-lms/geli`](https://github.com/geli-lms/geli) | 🟢 **Apache-2.0** | **11 358 B** | `02ae520` | E-learning platform, permissive, patent grant included |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | **1 105 B** | `a40eff7` | Intelligent tutoring with Bayesian Knowledge Tracing, UC Berkeley. 🟢 **The ITS reference for STEM** |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **1 066 B** | `eec087e` | PyTorch knowledge tracing — the field's standard toolkit. 🟢 **The modelling core under any adaptive-learning claim** |
| [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** | **1 079 B** | `8b14aec` | Django+React CMS for education portals. 🟢 **The permissive front end for an AGPL LMS** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0 — README-declared** | 🔴 **not file-read** | `1c95cef` | Education ERP on the Odoo framework, 73+ modules. 🔴 **See the warning below** |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 **GPL-3.0 — a ONE-LINE declaration** | 🔴 **~20 B** | `444cc8e` | School management on Frappe/ERPNext. 🔴 **See the warning below** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** | 35 121 B | `1d83c2b` | School-management/SIS platform. Attendance, grades, scheduling — 🟢 **the input data for a dropout-prediction agent** |

🟢 **8 of 18 are MIT or Apache-2.0.** 🔴 **7 are copyleft** (2 AGPL, 3 GPL/LGPL-family, plus
Moodle and BigBlueButton's `-or-later` elections). 🟢 **1 is ECL-2.0.**
🟡 **2 cannot be read from a file body at all** — and those two are the finding.

### 🔴 Two rows whose licence CANNOT be read the way the other sixteen were

🔵 **Both are ERP-class platforms, which is where a studio's margin usually is, and both
fail the test this shelf applies to everything else.**

🔴 **`frappe/education`** — its licence lives at `license.txt` on branch `develop` and its
entire content is the string **`License: GNU GPL V3`**. 🟢 **About 20 bytes against the
35 147 B of a real GPL-3.0 body.** 🔴 **So GitHub's own detector cannot classify it — the
sidebar shows a bare "License" link with no type** — and neither can any body-marker
matcher, including this shelf's. 🟢 **The intent is unambiguous and the instrument is
useless on it**, which is `T85`'s shape (an election by omission) in a new place: 🆕 **a
GRANT BY REFERENCE.**

🔴 **`openeducat/openeducat_erp`** — the sidebar likewise shows an unclassified "License"
link; the **README** states LGPL-3.0. 🔴 **That is a README surface, which is exactly the
surface `lumen` proved can lie** (`T89`, this pass). 🟡 **Recorded as README-declared, NOT
file-read, and the distinction is kept** rather than flattened into the table.

🟢 **The consequence for a studio, stated plainly:** both rows are usable, 🔴 **and neither
licence should be quoted to a client's legal team from this page.** 🔵 **For those two,
clone and read, or ask the maintainer.** 🔵 **`ACTION GQ`.**

### 🆕 🟢 The channel that made this page cheap, and the control that makes it trustworthy

| channel | what it does | cost | result |
|---|---|---|---|
| 🟢 `git ls-remote <url>` | existence + `HEAD` SHA | 1 round trip, **no tree** | 🟢 **18 of 18** |
| 🟢 `raw.githubusercontent.com/<o>/<r>/<branch>/LICENSE` | 🟢 **the licence BODY and its byte size** | 1 round trip, **no clone** | 🟢 **16 of 18 read directly** |
| 🔴 `curl github.com/<o>/<r>` | — | — | 🔴 **`403` on 17 of 17** |
| 🔴 `api.github.com/repos/…` | — | — | 🔴 refused — the session's repository-scope policy, defined as **`P150-A`** at [`repos/trending.md:242`](trending.md), an APPEND-ONLY page |

🟢 **NEGATIVE CONTROLS, both fired.** A slug that cannot exist returns **no SHA** from
`ls-remote`; a wrong licence path returns **`404`** from `raw`. 🔵 **Without them this page
would be eighteen rows of a channel that might say yes to anything** — `P42`'s rule applied
to a liveness check.

🔵 **And a channel difference INSIDE one host, for the third time this pass.**
`raw.githubusercontent.com` answers `curl`; `github.com` repo HTML refuses it; `WebFetch`
renders it. 🟢 **`ACTION GE2`'s rule earns its keep again: name the URL refused and the URL
that answered, never "the channel".** 🆕 **`T92` — a licence body is readable without a clone, so a 58-row census does not
need 2.4 GB.** 🔵 **Stated with an em-dash deliberately**: an earlier draft of this line
used a colon, and 🔴 **this pass's own citation check could not see it as a statement** —
🟢 `T91`'s lesson landing on the pass that wrote it.

### 🟢 How to choose from this page — the licence decides, then the attachment point

1. 🟢 **Permissive and complete, pick first:** `kolibri` (MIT, offline-first), `flat`
   (MIT, synchronous classroom), `academico` (MIT, SIS), `eCourse` (MIT, LMS),
   `geli` (Apache-2.0), `OpenVidu` (Apache-2.0, real-time).
2. 🟢 **Permissive LAYERS onto a copyleft host:** `XBlock` (Apache-2.0) into Open edX,
   `richie` (MIT) in front of it. 🔵 **This is the route that keeps your code yours**
   when the client already runs an AGPL LMS.
3. 🔴 **Copyleft hosts — the plugin inherits.** Moodle (GPL-3.0-or-later), Open edX and
   Canvas (AGPL), BigBlueButton (LGPL-3.0-or-later), Gibbon (GPL-3.0).
   🔴 **Canvas is the strictest: `AGPL-3.0-only`, elected by omission** — 🟢 **so an
   `-or-later` relicensing route that works for Moodle does NOT exist for Canvas** (`P43`).
4. 🟢 **Copyleft-free institutional LMS:** `sakai` (ECL-2.0), the Apache-derived option.
5. 🔴 **Do not quote the licence of `frappe/education` or `openeducat_erp` from here.**

##### 🔴 What this page still cannot do, after p153

- 🔴 **No star count for any of the 18.** The star budget went to the agent tier
  (`ACTION GI`); 🔵 **`ACTION GN`** carries it.
- 🔴 **Two of eighteen licences are not file-read** (`frappe/education`,
  `openeducat_erp`) — named above rather than smoothed into the table.
- 🔴 **`ls-remote` proves existence and freshness, nothing else** — not activity, not
  maintenance, not fitness. No row here is recommended on the strength of a `HEAD` SHA.
- 🔴 **The `-only`/`-or-later` election was re-measured for NONE of these rows this pass**;
  the elections quoted are p152's, on p152's clones, and 🔴 **those clones are gone** — the
  container is ephemeral.
- 🔴 **`raw` was tried on three branches and six filenames.** A repo that keeps its licence
  elsewhere would read as `NO_LICENCE_FILE_FOUND`, which is a limit of the probe and not a
  property of the repo. 🟢 **None of the 18 hit it.**

## Pass 152 — 2026-10-12

🔴 **Every per-file licence figure on this shelf counts files that belong to somebody else,
and this pass can finally say so with a number.** 🟢 **`T86`.** 🔴 **And the licence TERM —
the `-only` / `-or-later` election — turns out to be readable on three of the six largest
subjects, which means `T81`'s null was a property of SMALL repositories and not of
education copyleft.**

| measurement | value |
|---|---|
| foundational subjects walked this pass | 🟢 **6** vertical platforms, `git clone --depth 1`, **6 of 6 OK**, **2.4 GB** |
| source files scanned | 🟢 **105 727** (licence files excluded at any depth) |
| 🆕 files carrying a GNU per-file notice | 🟢 **31 205** |
| …of those, electing `-or-later` | **14 115** |
| …electing `-only` with the WORD "only" | 🟢 **0** |
| 🆕 …electing `-only` **by OMISSION** | 🔴 **16 896** |
| notices that never reach a VERSION | **194** |
| 🔴 subjects whose verdict is attributable to a VENDORED file | 🔴 **2 of 6** (`sakai`, `edx-platform`) |
| 🟢 the reproduction control — p151's 7 rows re-measured | 🟢 **1 513 files, 7 SILENT, control 7 of 7 — EXACT** |

🟢 **Artefacts:**
[verticals](../compose/code/p152-vertical-election/result.verticals.2026-10-12-p152.tsv) ·
[omission forms](../compose/code/p152-vertical-election/result.omission.2026-10-12-p152.tsv) ·
[the reproduction of p151's seven](../compose/code/p152-vertical-election/result.repro-p151-seven.2026-10-12-p152.tsv).

### 🆕 🟢 `P42` — the NOTICE DENOMINATOR, and why this shelf needed it

🔴 **p151 published *"0 elections over 1 513 files"* with no denominator**, and a figure of
that shape cannot be read. 🔴 **A tree with zero GNU notices and a tree with 16 905 notices
that each decline to elect both report "0 elections" — and they are opposite facts.**

🟢 **With the denominator, `SILENT` splits into four classes that were one:**

| class | subject | notices | what the silence MEANS |
|---|---|---|---|
| **NO_NOTICE** | `kolibri` | **0 of 4 350** | 🟢 permissive — there is no copyleft notice to elect in |
| **ROOT_ONLY** | `edx-platform` | 🟡 **0 first-party** (1 vendored) | 🟡 the licence lives in the root file alone |
| 🔴 **DECLINING** | `canvas-lms` | 🔴 **16 905 of 19 286 — 87.7%** | 🔴 **not silent at all: an election, by omission** |
| **NOTICE_NO_VERSION** | p151's seven rows | **17 of 1 513** | 🟢 a GNU licence named, no version to elect from |

🟢 **And the fourth class re-reads p151's own result.** All **17** notice-bearing files
across the seven small rows name a GNU licence and never reach a version, 🔴 **while
`Agso-o/sigaa-calendar` and `ahmedEid1/lumen` have ZERO notices across 1 020 source files.**
🟢 **So `T81` HOLDS for the small rows — for a cause p151 did not measure.**

🔵 **Same defect class as `T84`'s `LINK LAYER`/`PROMPT LAYER` split**: two populations that
read zero on one instrument for different reasons, and an instrument that reports them
identically is hiding the difference. 🟢 **`P42` is that rule generalised: never publish a
zero without the denominator that makes it a measurement.**

### 🔴 The vendored-file problem, which touches every licence figure this shelf has published

🔴 **Two of six subjects' verdicts come from code the subject did not write:**

- 🔴 **`sakaiproject/sakai`** — **1** hit in **11 620** files:
  `library/src/webapp/js/trimpath-template-latest.js`, *"TrimPath Template … Copyright (C)
  2004, 2005 Metaha"*, dual GPL-2.0-or-later / Apache-2.0. 🟢 **Sakai is ECL-2.0 and elects
  nothing.**
- 🔴 **`openedx/edx-platform`** — its only notice-bearing file is
  `common/test/data/uploads/jschannel.js`. 🟢 **First-party notice surface: ZERO.**

🔴 **`SKIP_DIRS` cannot fix either**: it excludes `vendor/`, and neither bundled copy is
under `vendor/`. 🔵 **A path-name exclusion is the wrong instrument for a provenance
question** — 🟢 **the right signal is the notice's own copyright holder**, which sits in the
same eight kilobytes the walk already reads. 🔵 **`ACTION GF`.**

🔴 **The consequence for this page is not confined to these two rows.** Every per-file
licence sweep in this shelf's history — `p199-perfile-license`, `p441-tree-licence-enumeration`,
`p969-root-only-licence-reach` — walked trees without separating first-party from bundled
files. 🟢 **None of their published verdicts is withdrawn on this evidence**, because none
of them was measured for this defect; 🔴 **but none can be said to be free of it either.**
🟢 **Stated once, at page level, rather than as a correction this pass has not earned.**

### 🟢 The six foundational platforms, with the stars this page never had

| repo | licence | ★ | forks | 🆕 election | notice rate |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **LGPL-3.0** | **9.2k** | 6.0k | 🟢 `-or-later` | 8.5% |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | **8.2k** | 4.4k | 🟡 unstated | 🟡 0% first-party |
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | **7.5k** | — | 🟢 `-or-later` | 23.3% |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | **6.9k** | 3.0k | 🔴 **`-only`** | 🔴 **87.7%** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | **1.2k** | 1.0k | 🟢 none (vendored hit) | 0.1% |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | **1.1k** | 1.0k | 🟢 n/a | 0% |

🟢 **6 of 6 sidebar licences agree with this shelf's hand-read values** — a free second
licence channel, in the same nine fetches that refuted `T78`.

🔵 **The permissive foundation story is unchanged and now has a number beside it**:
🟢 **`kolibri` (MIT) is still the only one of the six a studio can build on without a
copyleft conversation** — and at **1.1k ★** it is also the second-least-starred. 🔴 **The
popularity and the permissiveness point in opposite directions on this shelf**, which is
the sentence this page has implied for 152 passes and could not previously support.

### 🔴 What this page still cannot do

- 🔴 **The election is unmeasured on every foundational subject that is not one of these
  six.** 🟢 Six were cloned; no larger population was sampled and none is implied.
- 🔴 **No notice-to-holder attribution** (`ACTION GF`), so `sakai`'s row is published with a
  verdict this page knows is wrong rather than quietly dropped.
- 🔴 **The positive control degrades on big trees**: it fires on **10 of 161** licence
  bodies here against 7 of 7 on the small rows, because these six trees bundle 161 licence
  files that are mostly vendored MIT/Apache. 🟢 **The figure is given rather than hidden.**
  🔵 **`ACTION GG`.**
- 🔴 **p151's `election.py` was NOT the instrument used.** One invocation was refused
  `[Code from External]`; 🟢 **the re-implementation reproduces p151's three published
  figures exactly**, which licenses it as a reproduction and 🔴 **not as an independent
  second surface.**

## Pass 151 — 2026-10-12

🟢 **The 58-row licence census is RE-PUBLISHED**, the body matcher is retired in both
modules that owned a copy, and 🟢 **the GNU-family population is confirmed at SEVEN over all
58 subjects** rather than the 28 trees p150 could reach.

| measurement | value |
|---|---|
| subjects walked | **58** — 🟢 **50 of 50 `git clone`**, 🟢 **8 of 8 `npm pack`** |
| subjects shipping a licence FILE | **39** |
| of those, carrying a readable TITLE line | 🟢 **39 — all of them** |
| GNU-family population, by the title surface | **7** |
| …by the retired body matcher, as a population | **7** |
| rows where the two surfaces DISAGREE | 🔴 **5** — exactly the five `T77` named |
| rows changing licence id against the published census | 🔴 **4 of 52** |
| …of those, outside the GNU family | 🟢 **0** — `ACTION FN`'s falsifier is SILENT |
| rows with more than one licence file | **0** |

🟢 **The re-published artefact:**
[`evidence/licence-census.2026-10-12-p151.tsv`](../evidence/licence-census.2026-10-12-p151.tsv).

### 🟢 The five corrections, now in the census and not only beside it

| row | published | corrected |
|---|---|---|
| `Agso-o/sigaa-calendar` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `despedite/siu-guarani` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `mhlavac/edupage-mcp` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `ahmedEid1/lumen` *(agent tier, not in the 52)* | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `qxbao/qldt-hanu-mcp` | 🔴 `LGPL` | 🟢 **GPL-2.0** — wrong family **and** no version |

🔵 **`mhlavac/edupage-mcp` is the row that makes the title WINDOW load-bearing**: its
`LICENSE` opens with *"Copyright (c) 2026 Martin Hlavac"* and names the GNU licence on the
next non-blank line. 🔴 **A one-line window would read it as having no licence at all** — so
the window's width is now asserted against this row's shape in the suite.

### 🟢 The coverage result, which the action did not ask for and matters more

🔴 **A narrower surface that answers less often is a trade, not a fix.** 🟢 **39 of 39
licence files on this shelf carry a readable title line**, so retiring the body matcher
costs **zero coverage**. 🔵 That is why the replacement can be shipped rather than offered
as an option.

### 🔴 The eighth GNU-family row, and why `T77` cannot touch it

🔴 **`moodle-mcp-server-aql-0.1.7` declares `AGPL-3.0` in `package.json` and ships no
licence file.** It is GNU-family at the **declaration** layer, where there is no body to
mis-read. 🟢 **8 GNU-family ids across 58 rows; 7 of them read from a body.** 🔵 Stated now
so it is not later found as a correction.

### 🔴 A figure on the re-published census that is NOT this shelf's figure

🔴 **Strict-unlicensed reads 10 on the new artefact and 8 on `p149-common-title-licence`'s
58-row result.** The two rows are **`eugeborzone/Auto_Grade_Guarani`** and
**`frjunioalves/suap-mcp`**, both Portuguese-language. 🔵 **`p145`'s README surface is the
English-only `licen[cs]e` pattern that `T63` proved cannot match `Licença`/`Licencia`**;
p147's extended matcher can, and reads both as `README_ONLY`. 🟢 **8 is the correct figure.**
The full reconciliation, with every difference attributed:

| class | p149 (58) | after p150's `ACTION FE` | this artefact | 🟢 reconciled |
|---|---|---|---|---|
| `FILE` | 39 | 39 | 39 | **39** |
| `PKG_ONLY` | 4 | 7 | 7 | **7** |
| `README_ONLY` | 7 | 4 | 🔴 **2** | **4** |
| `NONE` | 8 | 8 | 🔴 **10** | **8** |

🟢 **Nothing is unexplained**: the `PKG`/`README` split is the inverted grant ladder p150
fixed, and the `NONE` difference is the English-only README surface. 🔵 **`ACTION FW`** moves
the README-heading question into `lib/` for the same reason the licence-identity question
now lives there (`P40`), and 🔵 **it is deliberately NOT fixed in the pass that measured it**
(`ACTION EU`'s rule).

### 🟢 Where the licence question now lives

🟢 **[`compose/code/lib/licence_identity.py`](../compose/code/lib/licence_identity.py)** —
imported by `p145-licence-census` and `p147-licence-language`. 🔵 **p149's `identify_ext()`
DELEGATES to p147's `identify()`**, so p150's *"three published copies"* were two copies and
one delegation, and two edits fixed all three. 🔴 **`retired_identify()` is kept, and kept
wrong**, so the defect can be reproduced rather than asserted. **47 tests.**

## Pass 150 — 2026-10-12 — this shelf cannot see a GPL row, and has published none in 150 passes

🔴 **`T77`. Five of seven GNU-family rows on this shelf carry the wrong licence
identifier**, and the cause is one published line applied the wrong way.

### 🔴 The defect, and why it is structural rather than a typo

`p145-licence-census.identify()` — copied verbatim into `p147-licence-language` and
`p149-common-title-licence` — tests the licence **body** for a phrase:

    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),

🔴 **GPL-3.0's own section 13 is TITLED *"Use with the GNU Affero General Public License"***
and its body names the Affero licence twice more. 🔴 **So every verbatim GPL-3.0 file matches
the AGPL rung before the GPL rung is reached.**

🔴 **And the whole family behaves this way.** GPL-2.0's preamble reads *"you may want to use
the GNU Lesser General Public License instead"* — so a GPL-2.0 file matches the **LGPL** rung.
🔵 **Each GNU licence names its siblings in its own text, which is exactly what a
body-substring test cannot survive.** 🔵 **`T39`'s class again: the phrase is right and the
test is wrong, because the phrase lives inside the licence it is meant to exclude.**

### 🔴 The published distribution was the clue, and nobody read it

| licence | rows in `p145`'s published census |
|---|---|
| MIT | 33 |
| *(none)* | 9 |
| 🔴 **AGPL-3.0** | 🔴 **6** |
| Apache-2.0 | 2 |
| 🔴 **LGPL** | 🔴 **1** |
| ISC | 1 |
| 🔴 **GPL** | 🔴 **ZERO** |

🔵 **A shelf of 58 education repositories, a third of them LATAM university scrapers and
Moodle plugins, publishes not one GPL row** — while its own `agents/top.md` describes several
rows as GPL-3.0 by hand. 🔴 **The contradiction was on two pages at once and went nine passes
without being read as a signal.**

### 🟢 Measured, row by row

| row | published | measured from the title line | direction |
|---|---|---|---|
| `Agso-o/sigaa-calendar` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `despedite/siu-guarani` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `mhlavac/edupage-mcp` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `ahmedEid1/lumen` *(agent tier)* | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `qxbao/qldt-hanu-mcp` | 🔴 `LGPL` | 🟢 **GPL-2.0** | 🔴 **WRONG FAMILY, and no version** |
| `edwyj/ddl-killer` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 **right** |
| `fabrica-de-inovacao/expeditto` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 **right** |

🟢 **Two rows are genuinely AGPL-3.0, which is why the defect survived**: the matcher is not
always wrong, so every spot-check that happened to land on `ddl-killer` or `expeditto`
confirmed it.

### 🔵 What the error costs a studio, in both directions

🔴 **Four rows OVERSTATED.** AGPL-3.0 obliges source disclosure to anyone interacting with the
software **over a network**; GPL-3.0 obliges it on **distribution** only. 🔵 **A hosted tutor
or a SaaS SIS connector trips AGPL §13 and does not trip GPL-3.0** — so this shelf has been
telling a studio that three LATAM/EMEA connectors and one tutoring agent are unusable behind a
hosted product when they are ordinary copyleft. 🟢 **The safe direction, and still wrong: it
disqualifies usable work.**

🔴 **One row runs the other way, and that is the dangerous one.** `qxbao/qldt-hanu-mcp` was
filed as `LGPL` — the most permissive member of the family, routinely treated as
link-and-go. 🔴 **It is GPL-2.0**: full copyleft, **no patent grant**, and incompatible with
GPL-3.0-licensed code it might be combined with. 🔵 **An understatement of obligation on a row
nobody flagged.**

### 🟢 The fix: a licence is identified by its TITLE, confirmed by its operative clause

[`p150-gpl-affero-discrimination`](../compose/code/p150-gpl-affero-discrimination/README.md),
**35 tests**, authored fixtures, offline.

| surface | what it reads | why it is independent of the body |
|---|---|---|
| **title** | the licence name as a **whole line** in the first 5 non-blank lines, plus the version | 🟢 **a sentence is never just a licence's name** |
| **clause** | AGPL-3.0's §13 *"Remote Network Interaction"*, anchored to line start | 🟢 **this is the clause that MAKES AGPL different; a plain GPL file cannot contain it** |

🟢 **A verdict is returned only when both surfaces agree**; a hand-edited or genuinely
dual-licensed file comes back `DISAGREE` and is named rather than guessed at. 🟢 **The version
is carried** — `GPL-2.0` and `GPL-3.0` are different instruments and this shelf published
neither.

🔵 **The window must stay narrow, and the tests enforce it.** An earlier draft used a 20-line
title window; the GPL-2.0 fixture caught it reading "Lesser" out of the preamble and returning
`LGPL-2.0` — 🟢 **the defect being fixed, reproduced inside the fix.** The matcher now requires
the licence name to **be** the line.

### 🟢 `ACTION FE` — the grant ladder is corrected, and it moves exactly three rows

[`p150-grant-ladder-order`](../compose/code/p150-grant-ladder-order/README.md), **17 tests**.
🔴 *Refuted if any row other than the three npm rows p149 named changes class.* 🟢 **Falsifier
silent.**

| subject | p147 (inverted) | corrected | direction |
|---|---|---|---|
| `eth-moodle-mcp-1.3.3` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |
| `moodle-mcp-server-aql-0.1.7` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |
| `owen-x-tech-canvas-mcp-1.1.0` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |

🟢 **No connector row, no agent row, and no licence IDENTIFICATION changes** — only the rung
recording where the grant was found. 🔵 **p147's inversion had been quietly WEAKENING three
rows**, reporting prose where a declared `package.json` licence exists; the correction restores
the stronger reading, which is why it moves no figure in the dangerous direction.

🟢 **FILE-grant rows are invariant by construction** — `census()` returns on the licence-file
branch before either reordered branch — so the test set is the 18 non-FILE rows plus the 6
agent rows, **24 subjects measured**, and the invariance is asserted rather than assumed.

### 🔴 What this pass did NOT fix, deliberately and otherwise

- 🔴 **The three published copies of `identify()` are UNCHANGED.** `p145`, `p147` and `p149`
  all still carry the body matcher. 🔵 **Correcting them in the pass that measures them is the
  mistake `ACTION EU` exists to avoid** — and the mistake `ACTION FE` was registered to undo.
  🔵 **`ACTION FN`.**
- 🔴 **The 44-row census is NOT re-published.** Five rows are known wrong and the TSV that
  carries them is p145's. 🟢 **The corrected values are in
  [`result.2026-10-12-p150.tsv`](../compose/code/p150-gpl-affero-discrimination/result.2026-10-12-p150.tsv)**
  and the row-by-row table above.
- 🔴 **`GPL-3.0-only` versus `GPL-3.0-or-later` is NOT distinguished.** That election lives in
  per-file headers, not the licence body, and it changes what a derivative may relicense to.
  🔵 **`ACTION FO`.**
- 🔴 **Only 28 trees were measured, not 58.** The GNU-family population was identified from
  `p145`'s published census — which is the artefact under suspicion. 🔵 **A row whose body
  contains no sibling mention cannot be mis-sorted by this defect**, so the published `MIT`,
  `Apache-2.0` and `ISC` rows are not at risk from `T77`; 🔴 **that is an argument, not a
  measurement.** 🔵 **`ACTION FU`.**
- 🔴 **`moodle-mcp-server-aql`'s `AGPL-3.0` is untouched** and stands: it is `PKG_ONLY`, read
  from a declared manifest string, not from a body match.

## Pass 149 — 2026-10-12 — the licence census reproduces over 58, the denominator moves, and two of this KB's instruments disagree about evidence strength

🟢 **Every channel this page needs was open**: 🟢 **`git clone` 50 of 50**, 🟢 **`npm pack` 8 of
8**, 🆕 🟢 **`cargo fetch` + `cargo test` for the Rust row.**

### 🟢 The licence census, reproduced and extended to 58

🟢 **`ACTION FC` re-ran the grant census over the whole population** rather than the 44 this
page usually quotes. 🟢 **Strict-unlicensed reproduces at 8**, and 🔵 **the eight are now named
on one line** so no later pass has to re-derive them:

`MatheusMach/QuantoFalta` · `P1ckle3/blackboard-mcp` · `Piyushtanwani/DAU-buddy` ·
`SIU-Toba/docker-guarani` · `karkarkins/BlackboardAssistantMCP` · `ruud0/aula-virtual-mcp` ·
`hesham0-0nasser/tutor-lms-mcp` · `@n35da/brightspace-mcp@0.4.0`

🔴 **The denominator is 58, not the 57 p148 quoted** — 44 connectors + 8 npm + **6**
agent-tier, every one reached. 🟢 **The figure 8 is unaffected**, because every agent-tier row
but `tutor-lms-mcp` carries a `FILE` grant (`AGPL-3.0`, `MIT`, `MIT`, `Apache-2.0`, `MIT`).
🔴 **Recorded as a one-row discrepancy to reconcile, not as an error in p148**: the agent tier
has **no committed subject list**, so the two counts cannot be compared directly.
🟢 **`ACTION FL` registers the list.**

🔴 **`ACTION FC` itself is REFUTED**: adding eighteen common-title licence forms (`Apache
License 2.0`, `GPLv2`, `GPL v3`, `BSD 3-Clause`, `MPL 2.0`, …) changes **0 of 58** rows.
🟢 **So `T72` is confirmed a Fedena-specific artefact outside this shelf's population.**
🔵 **Exactly one row is `UNIDENTIFIED` under both rules** — `eugeborzone/Auto_Grade_Guarani`,
a Spanish licence **heading with no licence named under it**, which is not a title-form case.
🟢 **The matcher is kept anyway**: it is tested, it costs nothing, and the next shelf this KB
censuses will not be this one.

### 🆕 🔴 `T74` — two of this KB's own instruments disagree about what counts as stronger evidence

🔴 **The page's real finding, and it came out of a reproduction control.**

| module | grant ladder |
|---|---|
| `p145-licence-census` | `FILE` → 🟢 **`PKG_ONLY`** → `README_ONLY` → `NONE` |
| `p147-licence-language` | `FILE` → 🔴 **`README_ONLY`** → `PKG_ONLY` → `NONE` |

🔵 **p145's own docstring states the intent** — *"`README_ONLY` the only mention is prose in a
README. **Weaker still**"* — weaker, that is, than a licence declared in a package manifest.
🔴 **p147 silently inverted the two rungs.**

🟢 **It was invisible on the population p147 ran.** Over the 44 connectors the two modules
agree row for row, because 🔵 **no connector carries both a manifest licence field and a README
licence heading**, and p147's base tally on the 44 reproduces p145's exactly. 🔴 **p147 never
ran the npm tier** — where rows carry both — and there it moves **3 of 8**:
`@owen-x-tech/canvas-mcp@1.1.0` and `eth-moodle-mcp@1.3.3` (**MIT** either way) and
`moodle-mcp-server-aql@0.1.7` (**AGPL-3.0** either way), each from `PKG_ONLY` to `README_ONLY`.

🟢 **No licence identification changes.** 🔴 **What changes is the evidence class, in the
weakening direction**: a declared manifest field demoted to a prose mention. 🔵 **p145's order
is the defensible one.** 🔴 **Deliberately not fixed this pass** — changing the ladder in the
pass that measures it would mean comparing a modified instrument against published figures,
the mistake `ACTION EU` was built to avoid. 🟢 **`ACTION FE`.**

### 🟢 `zavora-ai/mcp-student-records` — the strongest pin on the shelf gains a third surface

🟢 **A third declaration surface, set-identical to the manifest**: the **23** tools flagged
`requires_approval = true` are exactly the **23** names passed to `mcp_2026_server!` as
`approval_tools`. 🟢 **And the crate now builds and tests here** — 24 of its own tests passing,
7 added. 🔴 **Its approval gate, though fail-closed at the MCP boundary, is bypassable
in-process via a `pub` store.** 🔵 **Full detail in `agents/top.md` and `p149-approval-enforcement`.**

### 🟡 `ACTION FB` — the build target behind every `NOT_SHIPPED` figure on this page

🟢 **Named, for all five rows that have an allowlist**: `librus-mcp` **wheel (35)** ·
`soongpt-plugin` **wheel (20)** · `global-education-mcp` **wheel (10)** ·
`vtop-bhopal-mcp` **npm tarball (0)** · `ai-tutor-mcp` **npm tarball (1)**. 🟢 **librus
reproduces p148's 35 / 39 exactly.** 🔴 **`yourssu/soongpt-plugin` declares TWO targets**, which
p148's key list could not see — 🟢 **but they agree at 20**, so `T68`'s *disagreement* stays a
single instance while its *structure* generalises to 2 of 5. 🔵 **The two npm rows are
structurally immune**: one tarball, one `files` key, no second target to disagree with.

## Pass 148 — 2026-10-12 — the foundational Rust row gets a bidirectional pin, and the `NOT_SHIPPED` rule fails as a general rule

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's figures are
re-measured from the payload rather than carried.

### 🟢 `zavora-ai/mcp-student-records` — promoted to the strongest pin on the shelf

🟢 **`ACTION EO` and `ACTION EP` both discharge with silent falsifiers.** This row is the
first on this shelf whose declared tool manifest and whose actual router are proved **equal
as sets**, by an instrument that reads its language.

| property | value | how it is known |
|---|---|---|
| repo | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | clone, this pass |
| licence | 🟢 **Apache-2.0** | full body at `LICENSE`; `Cargo.toml` declares it |
| language | Rust, edition 2024, `rust-version = 1.94.1` | `Cargo.toml` |
| SDK | `rmcp` **3.1.2** + `adk-mcp-sdk` **0.2.0** | `Cargo.toml` |
| 🟢 **router surface** | 🟢 **46** | `#[tool(` sites inside `#[tool_router] impl StudentServer`, `src/server.rs`, brace-tracked |
| 🟢 **declared surface** | 🟢 **46** | `mcp-server.toml`, 46 `[[tools]]` |
| 🟢 **set identity** | 🟢 **PROVED** | symmetric difference empty both ways; **0** duplicates either side; order identical |
| approval-gated writes | **23 of 46** | `requires_approval = true` |
| risk classes | `read_only` / `internal_write` / `ExternalWrite` | typed per tool in the manifest |
| compliance posture | 🟢 **FERPA-gated communications + a FERPA access log** | `get_access_log` tool; package description |
| 🔴 **what the repo itself asserts** | 🔴 **the COUNT only** | `tests/manifest_test.rs`: `len() == 46`, `domain`, `requires_approval` on 11 named writes. 🔴 **No set comparison** |

🔵 **`P144-G` closes at 4 of 4.** The three earlier bidirectional pins were a SHA-256
lockfile (`malkreide/global-education-mcp`, 10), a classification manifest
(`oliverhruby/edupage-mcp`, 31) and a golden name array
(`divyarthjain/vtop-bhopal-mcp`, 17). 🆕 **The fourth is a typed TOML manifest with a risk
class per tool, and it is the only one of the four where the pin is a governance artefact
rather than a test fixture.** 🔴 **It is also the only one of the four the repository does
not verify itself.**

🟢 **For a studio, this is the row to start a records layer on**, and the caveat is one
sentence: the manifest is a contract the code happens to satisfy today, and nothing in CI
stops it drifting. [`p148-rust-surface`](../compose/code/p148-rust-surface/README.md) is the
check to vendor into a build — **14 tests**, offline, no network.

### 🔴 `ACTION EV` — the manifest allowlist cannot replace the name list, and the reason is worse than coverage

`ACTION EC` (p147) found the `NOT_SHIPPED` rule already written in `librus-mcp`'s own
`pyproject.toml`, and `T39` was vindicated. 🔴 **`ACTION EV` asked whether that generalises.
It does not.**

| verdict | n of 16 | meaning |
|---|---|---|
| 🟢 `ALLOWLIST` | **5** | a manifest include allowlist exists and was read |
| 🔴 `MANIFEST_NO_ALLOWLIST` | **7** | a manifest exists and declares no allowlist |
| 🔴 `NO_MANIFEST` | **3** | no package manifest of any kind |
| 🔴 `NO_ALLOWLIST_CONCEPT` | **1** | 🔴 **the manifest CANNOT express one** — `go.mod`; the module is the unit |

🔴 **5 of 16. The falsifier fires by eleven rows.** 🔵 **And `NO_ALLOWLIST_CONCEPT` is the
row that makes this structural rather than incidental**: `Agso-o/sigaa-calendar` is Go, and
no amount of author diligence would give it an include allowlist, because the format has no
such key. 🟢 **That is `T39` one level up — a property-based exclusion is sound only where
the property exists** — and it means the name list stays as a fallback, as the action's
consequence clause specified.

| row | allowlist | items | source |
|---|---|---|---|
| `krzysztofbury/librus-mcp` | 🟢 yes | **1** | `pyproject.toml [tool.hatch.build.targets.wheel] packages` |
| `malkreide/global-education-mcp` | 🟢 yes | **1** | same key |
| `yourssu/soongpt-plugin` | 🟢 yes | **1** | same key |
| `divyarthjain/vtop-bhopal-mcp` | 🟢 yes | **4** | `package.json files` |
| `nirholas/ai-tutor-mcp` | 🟢 yes | **4** | `package.json files` |

### 🆕 🔴 `T68` — and one manifest declares TWO allowlists that disagree

🔴 **This is the sharpest thing `ACTION EV` found, and it corrects p147's prose.**
`librus-mcp`'s `pyproject.toml` carries **two** hatchling include allowlists, for two
different build targets, and they do not admit the same directories:

| target | key | items | 🔴 `.tool(` sites inside it |
|---|---|---|---|
| **wheel** | `packages` | **1** — `src/librus_mcp` | 🟢 **35** |
| **sdist** | `only-include` | **16** — incl. `tests_native`, `scripts/qualify_native.py` | 🔴 **39** |

🔴 **p147 named the 16-item `only-include` as the rule and published 35, which is the wheel
figure.** 🟢 **The number 35 is correct** — it is what the installable package contains, it
matches `MCP_CONTRACT.md`'s prose to the token, and it is the figure a studio consuming the
package would observe. 🔴 **The rule cited for it yields 39**, because the sdist allowlist
admits `scripts/qualify_native.py` (**2** sites) and `tests_native` (**2** sites).

🔵 **So "read the manifest's include allowlist" is underdetermined.** A pass has to say
*which build target*, and the right answer depends on which artefact the question is about.
🟢 **For a tool surface, the wheel is the right target**, and this page states that
explicitly from now on.

🟢 **p147's other librus figures reproduce exactly.** Whole tree **60**, and the
decomposition is **35** (`src/librus_mcp`) + **21** (`legacy_reference`) + **2** (`scripts`)
+ **2** (`tests_native`) = **60**. 🔵 p147 reported *"23 in `legacy_reference` + 2 in
`scripts`"*, attributing `tests_native`'s two to `legacy_reference`; the total is identical
and no published figure changes.

Instrument [`p148-manifest-allowlist`](../compose/code/p148-manifest-allowlist/README.md),
**12 tests** — one of which is the two-allowlist shape itself.

### 🔵 The npm tier, re-measured — unchanged

🟢 **8 of 8 tarballs fetched.** `ACTION EQ` ran the language-extended licence matcher over
all eight: **0 rows change class**. The tier's licence picture stands as p145 published it —
**4 `README_ONLY`, 3 `PKG_ONLY`, 1 `NONE`** (`@n35da/brightspace-mcp`, still the only npm
row on this shelf with no grant on any channel, and still the only one of the eight that
ships source).
## Pass 147 — 2026-10-12 — the npm tier gains two regions, and a foundational row was never read

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's npm block is
re-measured from the payload rather than carried.

### 🆕 🟢 Two npm rows are region-placeable after all — `T59` NARROWED

🔴 **`T59` called this shelf's 8 npm rows "structurally unplaceable on the region axis."**
🟢 **That is a property of the INSTRUMENT lane, not of the evidence.**

| row | region | host | where | strength |
|---|---|---|---|---|
| 🟢 `eth-moodle-mcp@1.3.3` | 🟢 **EMEA** | `moodle-app2.let.ethz.ch` — ETH Zürich | `README.md:76`, the `MOODLE_URL` **default** | 🟢 **strong** |
| 🟡 `mcp-canvas-lms@1.0.5` | 🟡 **APAC** | `canvas.ust.hk` — HKUST | `README.md:37`, an **`e.g.`** | 🟡 **a lead** |
| `@imazhar101/mcp-canvas-server` | 🔴 `UNPLACED` | — | — | — |
| `@ink-waffle/moodle-mcp` | 🔴 `UNPLACED` | — | — | — |
| `@n35da/brightspace-mcp` | 🔴 `UNPLACED` | — | 🔴 only `d2l.myschool.edu`, a placeholder | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `UNPLACED` | — | — | — |
| `canvas-mcp-server` | 🔴 `UNPLACED` | — | — | — |
| `moodle-mcp-server-aql` | 🔴 `UNPLACED` | — | 🔴 only `moodle.example.edu`, a placeholder | — |

🟢 **`eth-moodle-mcp` is strong because two independent Swiss-specific signals agree**: the
shipped `MOODLE_URL` default is ETH Zürich's production Moodle, and the token-minting
instruction names **nethz** (ETH's account system) and **AAI** (SWITCHaai, the Swiss
academic federation). Instrument [`p147-npm-region`](../compose/code/p147-npm-region/README.md), **15 tests**.

### 🟢 `@imazhar101/mcp-canvas-server` — 227 confirmed by a third method

🔴 **This page has carried a disagreement: 227 descriptors on one instrument, 18 dynamic
sites on another.** 🟢 **Resolving the 18 one level gives exactly 227.**

**18 tool modules, 18 spread sites in the `tools/list` handler, 1:1** at
`dist/servers/canvas/src/index.js:263-280`. Largest: `user-tools` **39**, `page-tools`
**21**, `file-tools` **20**, `submission-tools` **20**, `module-tools` **18**. Smallest:
`lti-launch-definition-tools` **1**, `grading-standard-tools` **3**, `admin-tools` **4**.

🟢 **So `T42` is confirmed by a third method**: `surface_bound` counts descriptors,
`surface_gate*` counts registration sites, and the two are the same surface at two levels.
🔵 **The largest tool surface this KB quotes is correct.** Instrument
[`p147-tooldef-sum`](../compose/code/p147-tooldef-sum/README.md), **11 tests**.

### 🆕 🟢 A foundational row this page should have had — Apache-2.0, Rust, 46 tools

| [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | v1.2.0 |
|---|---|
| licence | 🟢 **Apache-2.0** — buildable on, no copyleft |
| surface | 🟢 **46 tools**, declared in `mcp-server.toml` and pinned by test |
| write governance | 🟢 **23 of 46 `requires_approval = true`**; typed `risk_class` per tool |
| compliance | 🟢 **FERPA-gated communications + FERPA access log** |
| domain | 🟢 self-declared `domain = "education"` in the manifest |

🔴 **Both `os.walk` surface gates on this shelf read it as zero files**, because it is Rust
and `lang_of` has no `.rs` (`T64`). 🔵 **It is a complete SIS surface — students, courses,
enrollments, grades, rubrics, attendance, guardians, transcripts, analytics — under a
permissive licence, and the shelf could not see it.**

### 🔴 `moodle-mcp-server-aql`'s AGPL-3.0 — a packaging defect, not a missing grant

🔴 **`ACTION EF` REFUTED exactly as its falsifier specified.** The declared repository
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) is alive
and carries the **complete 661-line AGPL-3.0 body** at its monorepo root.

🔴 **The tarball carries no licence file at all.** Cause, named precisely:
`packages/server/package.json` ships an explicit **`files` allowlist of 16 globs**, none of
them `LICENSE`, and there is **no `LICENSE` inside `packages/server/`**. 🔵 **npm's
automatic licence inclusion looks in the package directory and does not reach up a
monorepo.** 🟢 **The grant exists and it is AGPL-3.0** — the obligation is real, the file
just never shipped. 🔵 **Restate as a packaging warning, not a licence gap.**

## Pass 146 — 2026-10-12 — the platform layer's licence map, and a shelf-wide instrument defect

🔴 **No foundational repo was cloned this pass** (`P146-A`). 🟢 **But the licence axis of the
major platform layer was read for the first time, on a channel no previous pass had
tried** — and it changes which platform a studio should reach for.

### 🆕 🟢 The platform layer, read on the licence axis — one permissive row out of seven

| repo | licence | ★ | what it is | build bar |
|---|---|---|---|---|
| 🟢 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 1.2k | Learning, teaching, research and collaboration platform. 🟢 **ECL-2.0 is Apache-2.0 with a narrowed §3 patent grant — OSI-approved, copyleft: no** | 🟢 **PASSES** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | 8.2k | The Open edX LMS and Studio. MOOC-grade, Python/Django | 🔴 **network copyleft** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | 6.9k | Instructure's open LMS, alongside its commercial SaaS | 🔴 **network copyleft** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 6.2k | The most-deployed LMS worldwide; deepest plugin ecosystem | 🔴 copyleft |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility | 🔴 copyleft |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 886 | 🟢 **LMS + SIS + fees + parent app on ONE database**, on the Odoo framework | 🔴 weak copyleft |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 505 | Official ILIAS release and development branches | 🔴 copyleft |

🔵 **Why this is a foundations finding and not a verticals one.** A foundational repo is
one you build **on**. 🔴 **Six of these seven cannot be built on in the fork-and-modify
sense without a reciprocal obligation**, and the two largest carry AGPL's network clause,
which triggers on precisely the hosted multi-tenant shape these platforms are deployed in.
🟢 **Sakai is the only row where fork-and-modify is also on the table** — and it is the
fourth-largest, which is why no previous pass noticed.

🟢 **The API-boundary pattern remains the default on every copyleft row** and is unaffected:
a separate agent service speaking REST/LTI to the platform incurs no obligation on the
agent's own code. 🔵 **The licence map changes which platform you pick when the client
needs core changes, not whether the shelf's patterns work.**

### 🆕 🔴 The instrument layer under this page has a shelf-wide defect

🔴 **`T42` is a property of this shelf, not an incident.** `p146-exclusion-reach` reads every
traversing instrument in `compose/code/`:

| | count |
|---|---|
| instruments that traverse a tree | **35** |
| …carrying an **empty-walk guard** | 🔴 **0** |
| …excluding `dist`/`build` with no re-admission while emitting a verdict | 🔴 **5** |
| …that **cannot read anything but a git clone** | 🔴 **16** |

🆕 🔴 **`T59`**: 16 of 35 instruments traverse by `git ls-tree`/`ls-files`, so a clone is a
**precondition**, not a convenience — and 🔴 **the entire region-placement lane is in that
set** (`americas`, `cctld_urlctx`, `origin_scale`, `repo_origin`, `tenancy`). 🔵 **A
published npm package is not a git tree, so the 8 npm rows on this shelf are structurally
unplaceable on the region axis this KB exists to serve.** 🔴 **No pass had said so.**
`ACTION EK` asks whether a non-git channel can place any of them.

🟢 **`p146-empty-walk-guard` is the four-line fix**, with the distinction it exists to
preserve pinned by test: *zero files walked* withholds a verdict; *files walked, none
matched* is a finding and keeps its verdict.

### 🔴 What this page did NOT do this pass

- 🔴 **No star count, commit count, HEAD date or licence file was read for any existing
  shelf row** — all of those need a clone.
- 🔴 **The seven platform licences above are page readings, not `LICENSE`-file reads.** A
  licence badge is a declaration; `T21`/`P145-I` is this KB's own evidence that a
  declaration and a shipped grant diverge. 🔵 **They are published as declarations.**
- 🔴 **OpenEduCat's Odoo dependency chain was not read** — upstream is LGPL-3.0 with a
  proprietary Enterprise edition, and the obligation interaction is unknown.

# Education — foundational repos

**Pass 145, 2026-10-12.** 🔴 **The npm rows on this page were never read.** The instrument
this KB measures tool surfaces with excludes `dist` and `build` unconditionally, and **7 of
the 8 npm packages cited here ship their entire payload under exactly those two names**.
🟢 **All eight are now measured**, and 🔴 **none of the eight ships a licence file.**

### 🔴 `ACTION DZ` / `P145-A` — seven rows on this page returned a verdict over zero files

🔵 **p144 discharged `ACTION DP` by cloning three npm packages and comparing bundle against
source.** That comparison was sound. 🔴 **What nobody checked is whether the instrument
could read the bundle at all** — and on seven of eight rows it could not, because
`SKIP_DIRS` removed the only tree the package ships.

| package | all code under | files | p143 read | p145 reads |
|---|---|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 `dist/` | 69 | 🔴 `NOT_AN_MCP_SERVER` | **18 dynamic sites** (227 descriptors) |
| `moodle-mcp-server-aql` | 🔴 `dist/` | 68 | 🔴 `NOT_AN_MCP_SERVER` | 🔴 **`MUTATED` — plugin-extensible** |
| `@ink-waffle/moodle-mcp` | 🔴 `dist/` | 18 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **16 literal** |
| `mcp-canvas-lms` | 🔴 `dist/` | 16 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **3 literal** |
| `eth-moodle-mcp` | 🔴 `build/` | 13 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **18 literal** |
| `canvas-mcp-server` | 🔴 `build/` | 6 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **54 literal** |
| `@owen-x-tech/canvas-mcp` | 🔴 `build/` | 4 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **62 literal** |
| 🟢 `@n35da/brightspace-mcp` | 🟢 `lib/` + `server.mjs` | 17 | 🟢 **17 dynamic** | 🟢 **17 dynamic** (unchanged) |

🟢 **Four of the new readings reproduce counts this page already held by other means** — 16,
3, 18 and 54 match `p143-tier-size`'s hand counts exactly, and **62** matches the live
surface `p139` established for `@owen-x-tech/canvas-mcp`. 🔵 **Agreement across two
unrelated instruments on five rows is what makes the seven corrections trustworthy.**

### 🔴 The rule this page should have been applying, and now is

> **A tree is excluded only when it does not bear the property being measured.**

`dist/` is a regenerated artefact in a git checkout and **the shipped source itself** in a
published tarball. 🔵 **Same name, opposite correctness** — so the test is the package's own
declared entry point (`main`, `bin`, `module`, `exports`), not the name. Instrument:
[`p145-surface-payload-repair`](../compose/code/p145-surface-payload-repair/README.md),
**14 tests**.

🟢 **This also forecloses `T37` by construction**: a committed `dist/` beside its own source
stays excluded, so the double count that defeated `P144-A`'s first draft cannot recur.

### 🔴 `ACTION DX` — not one npm row on this page ships a licence file

| package | grant | licence |
|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 README only | MIT |
| `@ink-waffle/moodle-mcp` | 🔴 `package.json` only | MIT |
| `@n35da/brightspace-mcp` | 🔴 **NONE** | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `package.json` only | MIT |
| `canvas-mcp-server` | 🔴 `package.json` only | MIT |
| `eth-moodle-mcp` | 🔴 `package.json` only | MIT |
| `mcp-canvas-lms` | 🔴 `package.json` only | MIT |
| `moodle-mcp-server-aql` | 🔴 `package.json` only | 🔴 **AGPL-3.0** |

🔴 **0 of 8.** 🔵 **Consistent with `T21`'s 33% npm licence-payload rate rather than in
conflict with it**: `npm pack` includes a `LICENSE` only if one exists in the tree, so a
0% file rate at HEAD and a 33% historical payload rate describe the same population at two
times. 🟢 **`P138`'s distinction holds and is the operative one here — a licence identifier
is not a licence**, and seven of these rows offer only an identifier.

🔴 **`@n35da/brightspace-mcp` is the sharpest row on the page**: the only npm package that
ships readable source, and the only one with no licence of any kind. 🔵 **The row a
developer can most easily learn from is the row they have least right to copy.**

### 🔴 The foundational row that is unbounded by design

`moodle-mcp-server-aql` builds `toolDefinitions = buildCoreToolDefinitions()` and then
**`.push()`es one descriptor per discovered plugin** (`dist/server/factory.js:131`, inside
the plugin loop). 🔴 **Its tool surface is a property of the deployment's plugin set**, not
of the published package — the first row on these shelves that is unbounded for an
architectural reason rather than an instrumental one.

🔴 **It is also the AGPL-3.0 declaration.** 🔵 **A plugin-extensible connector under
copyleft is a specific delivery hazard**: the extension points invite exactly the
modification the licence attaches obligations to. `ACTION EF` tests whether any licence
text exists behind the declaration.

### 🟢 What this page can now say about its own instruments

🔴 **`ACTION DV` asked for all four tiers under one instrument and that is not achievable
here.** `surface_bound.py` reads **JS and TS only**; of the 20 MCP servers across the four
tiers, **7 are Python and 1 is PHP**. 🔵 **Recorded as a structural property of the
population**, not as an environment blocker and not as a probe to re-register.

🔴 **And the two instruments measure different things.** `surface_bound` counts
**descriptors**; the gate instruments count **registration sites**. On
`@imazhar101/mcp-canvas-server` that is **227** against **18**, and 🟢 **neither number is
wrong** — which is why `T30`, built across both, is withdrawn outright rather than
reinstated.


**Pass 144, 2026-10-12.** 🔴 **The correction this page owed about its npm instruments is
discharged, and it resolves in the opposite direction.** p143 recorded that 7 of 8 npm packages
could not be read at all because they ship only compiled output, and withdrew the npm figures on
that basis. 🟢 **Three of them were cloned this pass and the compiled output turns out to be a
faithful measurement**: bundle and shipped source return **identical tool-name sets** on 3 of 3.
🔴 **But 5 of 8 have no reachable source at all**, and one of those *declares* a repository that
is dead.

### 🟢 `ACTION DP` — the npm foundation rows measure the same on bundle and on source

[`p144-npm-source-parity`](../compose/code/p144-npm-source-parity/README.md).

| package | repo | licence | bundle | shipped source | name sets |
|---|---|---|---|---|---|
| `canvas-mcp-server@2.2.3` | 🟢 [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🟢 MIT | **54** | 🟢 **54** | 🟢 identical |
| `moodle-mcp-server-aql@0.1.7` | 🟢 [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** | **14** | 🟢 **14** | 🟢 identical |
| `mcp-canvas-lms@1.0.5` | 🟢 [`MisterCommand/mcp-canvas-lms`](https://github.com/MisterCommand/mcp-canvas-lms) | 🟢 MIT | **3** | 🟢 **3** | 🟢 identical |

🔵 **Set identity is the claim, not count identity** — `namesets.py` reports `bundle_only` and
`source_only`, both empty on all three rows. 🟢 **So `T30`'s npm figure is reinstated**, which is
what `ACTION DP` specified on this outcome.

🔴 **`moodle-mcp-server-aql` is AGPL-3.0 and that is a stop-ship for a studio build**, declared
in the npm metadata and confirmed in the repository. It is the only copyleft row on the npm tier.

### 🔴 The 5 rows this page cannot verify, stated per row rather than as a share

| package | source route | outcome |
|---|---|---|
| `@owen-x-tech/canvas-mcp@1.1.0` | `repository: owentaylor/canvas-mcp` | 🔴 **DECLARED AND DEAD** — `git ls-remote` prompts for credentials |
| `@imazhar101/mcp-canvas-server@2.1.3` | none | 🔴 no `repository`, `homepage` or `bugs`; **227 declared tools unverifiable** |
| `@ink-waffle/moodle-mcp@0.2.0` | none | 🔴 **18 `.map` files, zero `sourcesContent`** |
| `@n35da/brightspace-mcp@0.4.0` | none | 🔴 no pointer |
| `eth-moodle-mcp@1.3.3` | none | 🔴 no pointer |

🟢 **One correction to `P138-H` in the other direction**: `mcp-canvas-lms` was recorded as having
no `repository` field, which is true, and it is placeable anyway from `homepage`/`bugs`. 🔵 **A
missing `repository` field is not the same as an unsourceable package**, and three fields have to
be read before a row is declared dark.

🔴 **The sourcemap route is now closed and recorded as closed.** Three packages ship `.map`
files and not one carries `sourcesContent`, so a map yields original *path names* and no original
*bytes*. 🔵 **A future pass should not re-attempt it.**

### 🟢 `global-education-mcp` is no longer the only self-verifying row on this page

[`p144-surface-pin-census`](../compose/code/p144-surface-pin-census/README.md). `ACTION DQ` asked
for a second row carrying a committed tool-surface pin and found **two**, by two mechanisms
neither of which is a hash lockfile.

| row | licence | mechanism | pinned |
|---|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 MIT | `tools.lock.json`, SHA-256 per tool | **10** |
| 🆕 🟢 [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | 🟢 MIT | classification manifest over live `list_tools()` | **31** |
| 🆕 🟢 [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) | 🟢 Apache-2.0 | `EXPECTED_TOOLS` golden name array | **17** |

🔴 **Three instances and three incompatible formats.** 🔵 **So a consumer cannot ask "does it
ship the lockfile?"** — the question is whether *any* committed artefact pins the surface, and
the answer has to be looked for in three places.

### 🆕 🔴 Two rows cited by this KB carry no licence at all

Found while verifying something else, which is why `ACTION DX` now counts all 44 connector rows
and all 8 packages rather than trusting an incidental pair.

| row | size | licence at HEAD |
|---|---|---|
| 🔴 [`Piyushtanwani/DAU-buddy`](https://github.com/Piyushtanwani/DAU-buddy) | **40 literal tools, 176 commits** | 🔴 **NONE** |
| 🔴 [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | 4 commits | 🔴 **NONE** |

🔴 **`DAU-buddy` is the largest tool surface on the github-only tier and it is unusable** — no
licence means no grant, and no grant means a studio cannot copy a line of it. 🔵 **It remains
worth reading as a design reference**, which is a different permission from building on it.

### 🔵 Channel note — `curl -sI` cannot verify a GitHub URL in this environment

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` for every repository, live or
dead**, so it cannot distinguish them and must not be used as a URL check here. 🟢 **`git
ls-remote` and `git clone` both work**, and are what showed `owentaylor/canvas-mcp` to be dead
rather than merely unreachable. 🔵 **Every repository figure on this page was produced by
`git clone` over full history**; see
[`evidence/verified-repos.2026-10-12-p144.tsv`](../evidence/verified-repos.2026-10-12-p144.tsv).

**Pass 143, 2026-10-12.** 🟢 **`ACTION DO` discharged: the education-statistics row added last
pass is now VERIFIED rather than declared**, and it is the only row on this page whose tool
surface a consumer can check without running it. 🔴 **And a correction this page owes: the
licence-and-payload instruments it cites for npm rows cannot read 7 of the 8 npm packages at
all**, because they ship only compiled output.

### 🟢 `ACTION DO` — `global-education-mcp`'s lockfile verifies, independently recomputed

[`p143-lockfile-audit`](../compose/code/p143-lockfile-audit/README.md). p142 added this row on
the strength of a *declared* `tools.lock.json`. 🟢 **It is now a checked claim.**

| row | licence | verification |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **10 of 10 hashes recompute**, independently of the repository's own generator. 🟢 **10 of 10 agree with `server.py`** on `name`, `annotations` and `description`. 🟢 **10 of 10 `readOnlyHint: true`, zero write tools.** HEAD `26f7cd2`, **2026-10-04**, EMEA (`+0200` ×70) |

🔴 **One of the four hashed fields is NOT verified and the honest statement names it.**
`inputSchema` is generated by pydantic at import; checking it requires executing the
repository, which this audit does not do. 🔵 **So a consumer who cannot run the server has
verified three fields of four** — and that is still the strongest tool-surface guarantee
anywhere on these shelves.

**What a studio does with it.** 🟢 **`scripts/tool_signatures.py ci` is one CI step that
replaces four of this KB's own instruments** (`p139-tool-count-drift`,
`description-drift-audit`, `p141-agent-surface-gate`, `p142-github-only-tier`) for any
repository that adopts the pattern. 🔵 **It is the cheapest control on these shelves and it is
MIT**, so it can be lifted.

### 🔴 A correction this page owes about its own npm instruments

[`p143-tier-size`](../compose/code/p143-tier-size/README.md) measured what the 8 npm connector
packages actually ship:

| | |
|---|---|
| 🔴 npm packages shipping **only** compiled output (`dist/` or `build/`) | **7 of 8** |
| 🟢 npm packages shipping **source** | **1 of 8** — `@n35da/brightspace-mcp` (`.mjs`, `lib/`) |

🔴 **So a source-reading instrument sees nothing in 7 of 8 npm rows**, and any figure this KB
has published comparing npm rows to repository rows was comparing a **bundle** to a **source
tree**. 🔵 **`T21`'s licence-payload gradient is unaffected** — it reads published packages in
all three ecosystems, one artefact kind throughout, which is exactly why it has survived four
falsifiers. 🔴 **`T30`'s registration gradient is withdrawn**, and `T36` is the general rule.

**The practical consequence for a studio evaluating an npm education connector.** 🔴 **You
cannot audit what you cannot read.** 7 of 8 of these packages require fetching the repository
separately to review the code you are installing, and `@owen-x-tech/canvas-mcp` — whose README
claims 150+ tools against 62 measured — 🔴 **is the row whose repository is gone.** 🟢 **Prefer
the row that ships source or pins its surface**; on this page that is `@n35da/brightspace-mcp`
and `malkreide/global-education-mcp` respectively.

### 🔵 Channel note — the clone channel opened, and it changes what this page can verify

🟢 **`git clone` of public repositories now works from this environment**, with full history.
🔵 **Every verification on this page previously rested on single-file fetches**; licence files,
POM chains and payload measurements can now be read in tree. 🔴 **`api.github.com` repository
endpoints remain refused — on SCOPE, not a block** (`rate_limit` answers `200`), so star counts
are still unavailable and commit counts remain the size proxy. 🔴 **`codeload.github.com`
tarballs are `403` while `git clone` succeeds**, which is worth recording as a channel
asymmetry rather than rediscovering.

**Pass 142, 2026-10-12.** 🔴 **`ACTION DF` refuted: the licence a consumer gets from veraPDF
depends on which MODULE it resolves, not on the project.** 🟢 **And a foundational row is added
that this page has never had a category for — a permissively licensed, read-only connector over
UNESCO and OECD education statistics, which is a primary source for the figures `intel/market.md`
has had to take from vendor blogs.**

### 🔴 `ACTION DF` — veraPDF's grant is per-module, and 3 of 3 jars say nothing

[`p142-verapdf-module-grant`](../compose/code/p142-verapdf-module-grant/README.md). p140's
parent-chain walker, **executed unchanged**; only the coordinates are new.

| coordinate | own POM | effective licence | depth | jar licence text |
|---|---|---|---|---|
| `org.verapdf:core:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** *(from `verapdf-parent`)* | **4** | 🔴 `SILENT` — 460 entries |
| 🔴 **`org.verapdf:verapdf-xmp-core:1.30.3`** | 🟢 **BSD-3-Clause** | 🟢 **BSD-3-Clause** | 4 | 🔴 `SILENT` — 78 entries |
| `org.verapdf:validation-model:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** | 4 | 🔴 `SILENT` — 369 entries |
| 🔴 `org.verapdf:xmp-core:1.30.3` | — | — | — | 🔴 **404 — never published** |

**What a studio has to do differently.** veraPDF is the PDF/UA validator — the component you
reach for when course material has to meet an accessibility obligation. 🔴 **The election between
GPL-3.0 and MPL-2.0 applies to `core` and `validation-model` and does NOT arise for
`verapdf-xmp-core`, which is BSD-3-Clause.** A scanner reading the named umbrella coordinate
reports nothing and the umbrella has no jar at all.

🔵 **`org.verapdf:xmp-core` was never a coordinate.** p141 read it out of
`<modules><module>xmp-core</module></modules>`, and **a `<module>` entry is a source-tree path,
not an artifactId** — the directory `xmp-core/` builds `verapdf-xmp-core`. Any probe deriving
coordinates from a `<modules>` block inherits this error; it is pinned as a test.

### 🆕 🟢 The education-statistics layer — a foundational tier this page did not have

| repo | licence | what it is |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **UNESCO UIS (4 000+ indicators) and OECD *Education at a Glance*, over SDMX, with no API key.** 151 commits, HEAD **2026-10-04**, EMEA (`+0200` ×70). **10 tools, every name a literal, every one `readOnlyHint: true` — zero write tools.** Full MCP `ToolAnnotations` on 10 of 10, and 🟢 **a `tools.lock.json` that SHA-256-hashes each tool's annotations, description and schema** |
| 🟢 [`alcastaro/opendata-latam-mcp`](https://github.com/alcastaro/opendata-latam-mcp) | 🟢 **MIT** | 7 national CKAN open-data portals (AR, CL, DO, EC, MX, PA, UY), 15 628 datasets, cross-country parallel search. 🟢 **LATAM-placed on government hosts in 8 countries.** Not education-specific; the regional-evidence layer for engagements that need one |

🔵 **Why these belong on a *foundations* page rather than only on the agents shelf.** Every
regional figure this KB carries — market size, adoption rate, CAGR by region — currently comes
from market-research marketing pages, and `intel/market.md` says so each pass. 🟢 **UNESCO UIS and
OECD EAG are the primary sources those pages are re-quoting**, and there is now an MIT-licensed,
read-only, annotation-complete client for both.

🔴 **And it cannot run here.** `api.uis.unesco.org` and `sdmx.oecd.org` both answer `000` through
this environment's proxy. 🔵 **This is the most actionable entry the blocked-source ledger has
ever carried: two hostnames, one MIT dependency, and the figure channel this KB has been missing
for twenty passes.**

### 🟢 The practice worth copying off this page's newest row

`tools.lock.json` is a **tool-surface lockfile**: one SHA-256 per tool over its signature
(annotations + description + input schema), committed. 🔵 **This KB has built four instruments to
detect what that file prevents** — `p139-tool-count-drift`, `description-drift-audit`,
`p141-agent-surface-gate`, `p142-github-only-tier`. 🟢 **A row that pins its own surface by hash
makes all four unnecessary against it**, and the repository's own comment states the intent: the
logging wrapper preserves `__doc__` *"damit der `tools.lock.json`-Hash stabil bleibt"*. Adopted
as pattern `P21`.

**Pass 141, 2026-10-12.** 🔴 **`ACTION DC` applied p140's parent-chain walk to every Maven
coordinate this KB cites, and three further rows change verdict — so `T26` is not a property of
two artefacts but of Maven's inheritance model.** 🔴 **`ACTION DA` found the opposite failure
one layer below `openedx-core`'s distribution: not a disagreement between layers, but silence
in all of them below the wheel.**

### 🔴 `ACTION DC` — 5 of 9 coordinates on this shelf do not declare their own licence

[`p141-pom-chain-sweep`](../compose/code/p141-pom-chain-sweep/README.md). The walker is p140's,
re-used **unchanged** so that a changed verdict cannot be mistaken for a changed method; only
the population is new.

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util:1.2.0` | Apache-2.0 | — | — | 1 |
| 🆕 🔴 **`org.verapdf:verapdf-library:1.30.3`** | 🔴 **NONE** | `org.verapdf:verapdf-parent:1.30.1` | 🔴 **GPL-3.0 *or* MPL-2.0** | **3** |
| 🆕 🔴 `org.jasig.ssp:ssp:2.8.0` | 🔴 **NONE** | `org.jasig.parent:jasig-parent:39` | Apache-2.0 | **3** |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |
| 🆕 🟢 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` | Apache-2.0 | — | — | 1 |

Cumulative, p140 + p141: 🔴 **`INHERITS_FROM_PARENT` 5** (`net.oauth.core:oauth`,
`sakai-kernel-impl`, `verapdf-library`, `jasig.ssp:ssp`, `sakaiproject:kernel`) against 🟢
**`DECLARES_OWN` 4** (`sakai-kernel-api`, `lti-launch`, `basiclti-util`,
`spring-security-lti13`). 🔵 **56% inherit. An audit that reads one POM per coordinate is wrong
more often than right on this shelf.**

🟢 **`org.imsglobal:basiclti-util:1.2.0` is also now walked rather than carried.** p140's prose
table listed it as *"Apache-2.0 (own)"* on an earlier pass's authority while its committed TSV
held only four rows. 🟢 **The walk confirms it — `DECLARES_OWN`, depth 1** — so the cell is
now evidenced by the same instrument as its neighbours rather than inherited from prose.

### 🔴 The row that should change a delivery decision: veraPDF

`org.verapdf:verapdf-library` is the **PDF/UA accessibility validator** — in an education
engagement, the component reached for to prove course material meets an accessibility duty.

🔴 **Its own POM carries no `<licenses>` block at all. The grant is two levels up, and it is a
dual GPL-3.0 / MPL-2.0 offer** — at once the strongest reciprocal licence anywhere on these
shelves and, through MPL-2.0, the route out of it. 🟢 **MPL-2.0 is the obvious election for a
studio, and it cannot be elected by a team that does not know it is offered.** 🔴 A scanner
reading the named coordinate reports *"no licence"*, which invites the *"permissive by default"*
error p140 corrected on `net.oauth.core:oauth` — this time on a component whose licence
genuinely constrains redistribution.

🔵 **And there is no payload to inspect for a second opinion.** `verapdf-library` is
`<packaging>pom` with modules `core` and `xmp-core`; 🔴 **`verapdf-library-1.30.3.jar` is 404 on
Central**, because no jar is published under that name — consumers resolve `org.verapdf:core`.
`org.jasig.ssp:ssp:2.8.0` is the same class, `<packaging>war`. 🔵 **The coordinate a dependency
declaration names has no own grant and no bytes: the licence lives in a parent and the code
lives in siblings.** `org.sonatype.oss:oss-parent:7` is the shared grandparent of both chains
and declares nothing, so the walk must continue *past* a silent ancestor rather than stop there.

### 🟢 The cleanest Maven row on this shelf, and it places itself in EMEA

🆕 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` — **Apache-2.0, declared in its own POM, depth 1**,
LTI 1.3 for Spring Security. 🔵 **Its `groupId` is the origin evidence**: `uk.ac.ox` is the
University of Oxford's reverse-DNS namespace and `.ac.uk` maps to 🟢 **EMEA** with no inference
required. A Maven `groupId` is a stronger origin signal than an npm author field — it is a
namespace the organisation had to control in order to publish — and this is the first row this
KB has placed that way.

🔴 **It still ships no licence text** — no `LICENSE` or `NOTICE` among the jar's 72 entries. So
`T21`'s gradient firms up on a sixth Maven row rather than softening:

| ecosystem | declares a licence, ships no text |
|---|---|
| PyPI | 🟢 **0%** — 0 of 10 *(after p140's `openedx-learning` correction)* |
| npm | 33% |
| 🔴 **Maven** | 🔴 **83% — 5 of 6** *(p140: 80%, 4 of 5)* |

🔴 **`edu.ksu.ome.lti:lti-launch` 1.4.7 remains the worst row on the shelf** — LGPL-3.0 declared
in its own POM, no text in the jar, and pattern `P13` still depends on it.

### 🔴 `ACTION DA` — `openedx-core` is clean at the distribution layer and SILENT below it

[`p141-package-grant-layer`](../compose/code/p141-package-grant-layer/README.md). p140 called
`openedx-core` **1.9.1** the cleanest licence payload this KB has measured. 🟢 **That stands.**
🔴 **One layer down there is nothing.**

| package | `.py` files | licence files | SPDX headers | copyright lines |
|---|---|---|---|---|
| `openedx_catalog` | 12 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_content` | **132** | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_core` | 1 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_django_lib` | 7 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_learning` | 29 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_tagging` | 56 | 🔴 0 | 🔴 0 | 🔴 0 |
| **total** | **237** | 🔴 **0** | 🔴 **0** | 🔴 **0** |

🟢 Distribution layer, for contrast: `License-Expression: AGPL-3.0-only` (PEP 639) plus
`dist-info/licenses/LICENSE.txt`, **35 139 bytes**, Metadata-Version 2.4.

🔵 **p140's falsifier expected DISAGREEMENT between layers. The measured answer is SILENCE — and
for a studio that is the worse one.** Nobody vendors a wheel; they lift `openedx_tagging/` or
`openedx_content/` into their own tree. 🔴 **The moment a subtree leaves `dist-info/`'s company
it carries no grant, no holder and no notice** — while **AGPL-3.0-only** is the most reciprocal
obligation anywhere on these shelves. 🔵 **The licence is correct, current and complete in
exactly the one place the copy does not come from.** A `T21`-clean artefact can be `T18`-silent;
this is the clearest instance of it, and both findings are true of different layers.

🟢 **One thing this confirms rather than discovers:** `openedx_learning` survives as a **package
inside** the distribution even though the *distribution* `openedx-learning` was retired to a
shim. 🔵 **The name was demoted, not killed** — the 29 files under it are live code at 1.9.1,
not the 1 479-byte husk `openedx-learning` 0.33.1 publishes. A row keyed on the string alone
cannot distinguish those, which is exactly why `T27` reads the `Development Status` classifier.

### 🟡 One citation on this page, re-checked and confirmed

`uk.ac.ox.ctl:spring-lti13` is **404 on Maven Central**, as the row below already records. 🟢
The real artefact is `spring-security-lti13`; the shorter coordinate has never existed. 🔵
Recorded as a confirmation, not republished as a finding — and the kind of re-check `T24` exists
to force.

### 🔴 A method note: a `429` from Central is not a `404`

Maven Central answered **429** on two of six metadata fetches and on the `basiclti-util` jar,
clearing after 8–24 s of backoff. 🔴 **An earlier draft of this sweep recorded
`uk.ac.ox.ctl:spring-security-lti13` as "not on Central" off a single un-retried `429`** — which
would have deleted the cleanest row in the table above. Every fetch retries with backoff and a
failure is reported as a failure, never as an absence.


**Pass 140, 2026-10-12.** 🔴 **Two of p139's findings on this page are refuted, and both
refutations make the underlying defect worse rather than milder.** `ACTION CR` resolved the Maven
parent chains p139 recorded as "no signal"; `ACTION CS` established that the one PyPI hit was
never a defect at all — it is a **package rename this KB has been failing to follow for two
passes.**

### 🔴 `ACTION CR` — both "declares nothing" rows DO declare, two and three levels up

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🔴 `net.oauth.core:oauth` 20100527 | **NONE** | 🆕 `net.oauth:oauth-parent:20090531` | 🆕 **Apache-2.0** | 3 |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | **NONE** | 🆕 `org.sakaiproject:oss-parent:1` | 🆕 **ECL-2.0** | 4 |

Both p139 controls return unchanged — `sakai-kernel-api` 25.2 `DECLARES_OWN` (ECL-2.0),
`edu.ksu.ome.lti:lti-launch` 1.4.7 `DECLARES_OWN` (LGPL-3.0) — so the changed verdicts belong to
the rows, not to the method.
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🔴 Two sentences on this page are now wrong, and here is the correction

p139 wrote, of `net.oauth.core:oauth`:

> *"carries no licence signal at all … No grant and no file is not 'permissive by default' — it
> is **unlicensed**, and sixteen years of use does not change that."*

🔴 **There is a grant: Apache-2.0, inherited from `net.oauth:oauth-parent`.** 🔵 **And the reason
nobody found it is the finding** — the parent sits under a **different `groupId`**, `net.oauth`
rather than `net.oauth.core`. The artefact is not unlicensed. Its grant is two files and one
namespace hop from where any reader would look.

p139 also described the two Sakai kernel artefacts as *"same release line, opposite licence
posture"*. 🔴 **Both are ECL-2.0.** `api` declares it directly; `impl` inherits it from
`org.sakaiproject:oss-parent:1`. 🔵 **The posture is identical — only the declaration DEPTH
differs**, and depth is precisely what a scanner reading one POM does not traverse.

### 🔴 The declared-but-absent rate on this shelf's Maven rows rises to 80%

| coordinate | declares | ships licence text in the jar |
|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` 1.2.0 | Apache-2.0 (own) | 🟢 `META-INF/LICENSE` + `NOTICE` |
| 🔴 `edu.ksu.ome.lti:lti-launch` 1.4.7 | LGPL-3.0 (own) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 (own) | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` 20100527 | 🆕 Apache-2.0 (**inherited**) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🆕 ECL-2.0 (**inherited**) | 🔴 **NONE** |

🔴 **5 of 5 declare; 4 of 5 (80%) ship no text** — against p139's 40–67% and npm's 33%. 🔵 **So
`T21`'s gradient steepens rather than collapsing: PyPI 9%, npm 33%, Maven 80%.** The falsifier
fired and the trend it threatened got stronger, which is the only outcome that makes writing one
worthwhile. 🔴 **`edu.ksu.ome.lti:lti-launch` — the LGPL-3.0 Kansas State library pattern `P13`
depends on — remains the worst row**: the strongest obligation of the five and no text to satisfy
it.

## 🆕 🔴 `openedx-learning` is RETIRED. The row this page should carry is `openedx-core`

### `ACTION CS` — the empty 0.33.x wheels were never a packaging bug

p139 found `openedx-learning` **0.33.0** and **0.33.1** shipping **1 479-byte** wheels and
pre-registered `ACTION CS` to ask whether the breakage was known upstream. 🔴 **It is not
breakage.** The 0.33.1 `setup.py` says so in its own docstring:

> *"Builds a final shell release of openedx-learning which simply 'redirects' to openedx-core"*

with `packages=[]`, `install_requires=["openedx-core==0.34.1"]`,
`Development Status :: 7 - Inactive`, and a `long_description` reading
**"This package has been renamed to `openedx-core`!"**

🟢 **So `pip install openedx-learning` WORKS** — it resolves the shim and installs `openedx-core`.
p139's *"`pip install` resolves to the empty one"* is true of the bytes and wrong about the
outcome. 🆕 **This pass also measured the sdist, which p139 did not**: 11 paths, carrying
`setup.py` and `setup.cfg` and **zero package source**, with `top_level.txt` a single newline.
🔵 **A build recipe with nothing to build — which is exactly what a rename shim looks like.**

### 🆕 The row to carry forward

| field | value |
|---|---|
| package | 🆕 [`openedx-core`](https://pypi.org/project/openedx-core/) — [`openedx/openedx-core`](https://github.com/openedx/openedx-core) |
| latest | **1.9.1**, uploaded **2026-10-09** *(three days before this pass)* |
| version continuity | first release **0.34.1** — exactly what the shim pins |
| licence | 🔴 **AGPL-3.0-only**, as a **PEP 639 `License-Expression`** |
| 🟢 licence payload | `dist-info/licenses/LICENSE.txt`, **35 139 B**, `License-File: LICENSE.txt`, Metadata-Version **2.4** |
| wheel | 261 paths, 358 188 B |
| consolidates | `openedx_core`, `openedx_learning`, `openedx_tagging`, `openedx_catalog`, `openedx_content`, `openedx_django_lib` |
| steward | `David Ormsbee <dave@axim.org>` — **Axim Collaborative** |

🟢 **It is the cleanest licence payload this KB has measured.** Declared by SPDX expression,
shipped automatically under PEP 639 — 🔵 **which vindicates `T21`'s mechanism on the newest
artefact on the shelf: the grant is shipped by the build system, not by the maintainer's
diligence.** 🟢 **And it removes p139's only PyPI hit**: that row was a shim with no code, so this
shelf's PyPI declared-but-absent rate is **0 of 10**, not 1 of 11.

🔴 **The lesson is a freshness check, not a licence check.** Both signals — the `Inactive`
classifier and the rename in `long_description` — were sitting in the artefact p139 downloaded.
🔵 **New rule: before carrying a package row forward, read its latest release's
`Development Status` classifier and its `long_description`.** Entered as `T27`.

### 🔴 `ACTION CQ` — three `ROOT_ONLY` rows record ownership NOWHERE in source

`ACTION CQ` asked whether p139's foreign-source-header class extends beyond its three largest
rows. 🟡 **It does, weakly — 1 of 5, against p139's 2 of 3** (`Tim Branyen, contributors`, an
MIT-licensed vendored grunt task inside GPL-3.0 `adaptlearning/adapt_framework`). Across all eight
`ROOT_ONLY` rows: **3 of 8.**

🔴 **The stronger result is one the action did not ask for.** `overhangio/tutor` (157 source files
read), `openedx/XBlock` (99) and `openedx/codejail` (31) carry **no copyright header in any
source file** — 287 files, zero headers. So each row is scored for *where a holder is findable at
all*:

| row | does `LICENSE` name a holder? | where ownership actually lives |
|---|---|---|
| `Crosstalk-Solutions/project-nomad` | 🟢 yes — appendix **filled**: `Copyright 2024-2026 Crosstalk Solutions LLC` | + `package.json` |
| `adaptlearning/adapt_framework` | 🟡 only inside the GPL's **interactive-mode example** | — |
| `openedx/XBlock` | 🔴 no — left as `Copyright [yyyy] [name of copyright owner]` | `NOTICE.txt`, `pyproject.toml` |
| `openedx/codejail` | 🔴 no — **no copyright line at all** in the appendix | `NOTICE.txt`, `pyproject.toml` |
| `overhangio/tutor` | 🔴 no — left as `Copyright (C) <year>  <name of author>` | `pyproject.toml` **only** |

🔵 **For a delivery team asking "who holds this code?", the answer is increasingly not in the file
named `LICENSE`.** `adapt_framework` is a third form this KB has not recorded: its holder appears
in the licence file *only* as part of the GPL's illustrative `show c` snippet — a real
attribution in a place no scanner treats as one.
[`p140-rootonly-header-reach`](../compose/code/p140-rootonly-header-reach/README.md).

### 🔴 Open edX names its holder three ways across three layers

| layer | artefact | holder | contact |
|---|---|---|---|
| repo | `openedx/XBlock` | `edX` | 🔴 `oscm@edx.org` |
| repo | `openedx/codejail` | `edX` / 🆕 `Open edX Project` | 🆕 `oscm@openedx.org` |
| registry | `openedx-core` 1.9.1 | 🆕 `David Ormsbee` | 🆕 **`dave@axim.org`** |

🟢 **The holder NAME is defensible.** edX Inc. was *renamed* Axim Collaborative — same trustees,
same mission, same tax ID — after Harvard and MIT sold the edX brand to 2U, so `Copyright 2014,
edX` names the pre-rename identity of the current steward rather than a third party.

🔴 **The CONTACT domain is not.** `edx.org` is operated by **2U**, a different company from the
steward, and `openedx/XBlock`'s `pyproject.toml` still routes there while its sibling
`openedx/codejail` routes to `openedx.org`. 🔵 **Two repositories in one GitHub organisation, same
licence, different holder string and different contact domain — and a third domain on the live
PyPI artefact.** A client asked to send a notice gets three answers to one question.

🟡 **And one row inverts the expected reading.** `overhangio/tutor` declares
`authors = [{name = "Edly"}, {email = "hello@edly.io"}]`, which is **correct and current**: Edly,
the edtech arm of Pakistan-based Arbisoft, acquired Overhang.IO on **2023-03-27**, and Tutor's
founder Régis Behmo leads its technical direction there. 🔵 **Here the metadata is fresher than
the GitHub organisation name** — so a row's org name is not evidence of anything.

**Pass 139, 2026-10-12.** 🔴 **p138 measured the npm payload layer and found a third of the
connector shelf declaring a licence it does not ship. This pass asked the obvious next question —
is that open source, or is it npm? — and the answer is neither: it is the TOOLCHAIN.**
`ACTION CM` ran the same method against **PyPI** and **Maven Central**. Probe, tests and committed
TSVs: [`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

| registry | artefacts measured | 🔴 declare a licence, ship no licence file | rate | vs the 10% threshold |
|---|---|---|---|---|
| 🟢 **PyPI** | **11** (+1 absent from the registry) | 🟡 **1** — and it ships **nothing at all** | **9%** | 🟢 **REFUTED** |
| 🔴 **Maven Central** | **5** (+1 absent) | 🔴 **2 of the 3 that declare** | **40–67%** | 🔴 **NOT REFUTED** |
| *(npm, p138)* | *21* | *7* | *33%* | *not refuted* |

🔵 **The defect tracks each ecosystem's DEFAULT BUILD BEHAVIOUR, not its culture.**

- 🟢 **Python's backends ship the licence for you.** Under **PEP 639**, setuptools and hatch copy
  declared licence files into `<dist>.dist-info/licenses/`. **10 of 11** packages carried one in
  *both* wheel and sdist — every Open edX row included. A maintainer gets this right by doing nothing.
- 🔴 **Maven's jar plugin ships nothing for you.** A POM's `<licenses>` block lives in a *sibling
  file*; the jar on the classpath is untouched. `META-INF/LICENSE` requires deliberate
  configuration, and **2 of 3 declaring artefacts had not done it**.
- 🔴 **npm's `files` array names what to pack and silently omits what is absent** — p138's
  `canvas-mcp-server` *listed* `LICENSE` and shipped 8 paths containing none.

### 🔴 `P139-D1` — the Maven rows, and the library this KB tells clients to build on is in the defect class

| coordinate | version | POM declares | jar paths | licence in jar |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` | 1.2.0 | Apache-2.0 | 70 | 🟢 `META-INF/LICENSE`, `META-INF/NOTICE` |
| 🔴 **`edu.ksu.ome.lti:lti-launch`** | **1.4.7** | 🔴 **LGPL-3.0** | 43 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | 25.2 | 🔴 **ECL-2.0** | **578** | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` | 20100527 | 🔴 **nothing declared** | 32 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing declared** | **524** | 🔴 **NONE** |
| — `uk.ac.ox.ctl:spring-lti13` | — | — | — | not on Central (**404**) |

All five resolvable jars were **sha1-verified against the repository's own `.sha1`**; no mismatches.

🔴 **`edu.ksu.ome.lti:lti-launch` is the artefact built from
[`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) — the LGPL-3.0 Kansas State
library p137 identified (`P137-A`) as the LTI→OAuth-subject mapping that pattern `P13` depends on.**
It declares the strongest obligation of the five and ships no text to satisfy it. 🔵 **The one
interoperability library this KB recommends building on reproduces p138's worst npm row, in Java.**

🔴 **`sakai-kernel-api` declares ECL-2.0 while `sakai-kernel-impl` declares nothing** — two
artefacts of one kernel, same release line, opposite licence posture, and the one with **578
paths** is the one making the claim with no text. ECL-2.0 is **education's own licence** (an
Apache-2.0 derivative with a university-oriented patent clause), and it is exactly the identifier a
client's scanner will not recognise.

🔴 **`net.oauth.core:oauth` (2010) carries no licence signal at all** and is still a transitive
dependency of LTI 1.1 integrations. No grant and no file is not "permissive by default" — it is
**unlicensed**, and sixteen years of use does not change that.

### 🔴 `P139-D2` — the PyPI hit is not a licence defect: `openedx-learning` ships NO CODE

The one PyPI row declaring a licence and shipping no licence file is **`openedx-learning` 0.33.1**
— *"Open edX Learning Core (and Tagging)"*. It declares `AGPL 3.0` by legacy field **and**
classifier. Its wheel holds **4 paths, all metadata**; `top_level.txt` is **1 byte**; `RECORD`
lists only the four `dist-info` entries.

| version | wheel | sdist |
|---|---|---|
| 0.31.0 | 268 554 B | 192 313 B |
| 0.32.0 | 257 553 B | 189 430 B |
| 🔴 **0.33.0** | 🔴 **1 479 B** | 🔴 **1 748 B** |
| 🔴 **0.33.1** *(latest)* | 🔴 **1 479 B** | 🔴 **1 742 B** |

🔴 **`pip install openedx-learning` resolves to 0.33.1 and installs no modules.** Across **79
releases**, the two most recent are the empty ones — this is the *current* state of a core library
of the dominant open-source higher-education platform, not an old artefact. The collapse from 257 KB
to 1.4 KB is the signature of a packaging regression, shipped twice.

🔵 **A licence probe found a release defect.** It is counted honestly in both places: as a licence
row it is the hit that makes PyPI 9% rather than 0%; as a *finding* it belongs to a different class.

🟡 **Two smaller carries.** `xblock-sdk` 0.15.2 ships **two vendored Jasmine 1.3.1 `MIT.LICENSE`
files** under `sample_xblocks/*/static/js/lib/` beside its own AGPL-3.0 grant — `ACTION CJ`'s
foreign-holder class, in a payload. And `moodle-dl` declares `GPL-3.0` with `license_files`
**absent** from its metadata yet **ships** `LICENSE` in both distributions: 🔵 **a missing
`License-File` field does not imply a missing file**, the mirror image of npm's `files` naming one
it does not ship.

## 🔴 `ACTION CJ` — on the rows where the root licence file was "the whole story", it names nobody

p137 cleared **8** of the 20 largest rows as `ROOT_ONLY`: one licence file, nothing else
licence-shaped in the tree. `ACTION CJ` read the **source-file headers** of the three largest.
🔴 **Two of the three carry a holder their licence file does not name**, so p137's 50% is a **floor,
not an estimate**. Probe, 20 tests and TSV:
[`p139-source-header-holder`](../compose/code/p139-source-header-holder/README.md).

| row | tree paths | source files read | own holders | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 1 411 | 2 | 🔴 **1 — `FOSS United`, 78 header lines** | `FOREIGN_HEADER_IN_SOURCE` |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 450 | 1 | 🟢 0 | `OWN_HEADERS_ONLY` — 🔴 *but its pointer dangles* |
| 🔴 [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 660 | 🔴 **0** | 🔴 **3** | `FOREIGN_HEADER_IN_SOURCE` |

🔴 **`frappe/lms`'s `license.txt` names no holder of `frappe/lms`.** All **three** of its
`Copyright` lines are the AGPL's own apparatus: the FSF's copyright on the licence text (line 4),
the §0 definitions (line 65), and 🔴 **the "how to apply" template with the placeholder never
filled in** — `Copyright (C) <year>  <name of author>` (line 633). Ownership exists **only** in the
source headers, and there it is **two distinct legal entities**: `Frappe` / `Frappe Technologies
Pvt. Ltd.` (165 lines) and 🔴 **`FOSS United`** (78 lines), a separate Indian non-profit. 🔵 **A
verdict read from the root — "AGPL-3.0, Frappe" — is wrong in both halves on 78 files.**

🔴 **`openeducat/openeducat_erp`'s root `LICENSE` delegates copyright twice, and both pointers
dangle.** It opens *"For copyright information, please see the COPYRIGHT file."* — and
`git ls-tree -r HEAD` over all **1 345** paths finds **no `COPYRIGHT` file anywhere**. It then
delegates again, to "the relevant source files", which carry only `OpenEduCat Inc` (190 lines).
🔵 **The grant is sound and legible (LGPL-3.0, stated in its first lines); the chain that would say
whom you owe terminates nowhere.** It is the only one of the three honest enough to say it is not
trying.

🔴 **`academico-sis/academico` has zero headers of its own** and three foreign ones, all in built
Filament bundles under `public/` — `Pusher` (`echo.js`), `Chen Fengyuan` (`cropperjs`), `Chen,
Yi-Cyuan` (`js-sha256`) — 🔵 **the paths a client redistributes, and where no licence file would
ever be looked for.**

### 🟢 A channel p138 recorded as closed is open, and HEAD dates are measurable again

🟢 **`git clone --depth 1` against `github.com` works here.** p138 published **UNMEASURED** for
star counts *and* HEAD dates on the strength of `api.github.com`, `codeload` and `github.com` HEAD
all answering **403**. 🔵 **Git smart-HTTP is a different lane from the REST API, and it answers** —
which is how every row on this page was verified this pass, and how the `ACTION CN` lineage work was
done at all.

| row | HEAD commit | HEAD date |
|---|---|---|
| `frappe/lms` | `0f760e6` | **2026-10-11** |
| `openeducat/openeducat_erp` | `1c95cef` | **2026-09-07** |
| `academico-sis/academico` | `d0cd78c` | **2026-10-07** |

🔴 **Star counts stay `UNMEASURED`** — git carries no star count, so that half of p138's gap stands.


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟢 **p138 measured a fifth layer — the published package — and found a
third of the connector tier shipping an SPDX identifier with no licence text. It then registered a
falsifier against itself, and this pass fires it: `ACTION CH` read every shipped text file in all
21 payloads, and 0 of the 9 licence-file-less packages carry their own grant in a source header.**
🔴 **p138's count stands.** 🔴 **A sixth layer is now measured, and it is the one a partial copy
depends on: per-file notice, practised by 1 of 21 rows.** On the other 20, a single file lifted out
of the tree names no holder and no grant. 🔵 **And the repository layer was measured in the same
pass as the payload layer for the first time** — through this KB's already-documented raw-file lane,
not a new one — re-verifying two of this KB's published licence figures byte-exact. Instrument and 24 tests:
[`p139-source-header-grant`](../compose/code/p139-source-header-grant/README.md).

**Pass 138, 2026-10-12.** 🔴 **p137 measured that a licence cell describes a repository root rather
than a whole tree. This pass measured a fifth layer, and it is the only one a client actually
receives: the published package.** `ACTION CD` downloaded **21** education-LMS connector tarballs
(Canvas, Moodle, Brightspace, EduBase), **sha1-verified every one against the registry's own
`shasum`** — 21 of 21 matched — and enumerated every shipped path.

| the layer | what it tells you | measured |
|---|---|---|
| root licence file | what you may do | 🟢 right about the **family** 92% of the time (`p444`) |
| tree enumeration | 🔴 **whom you owe** | 🔴 incomplete for **50%** of the largest rows (`p137`) |
| 🆕 **published payload** | 🔴 **what the client is actually handed** | 🔴 **9 of 21 packages ship NO licence file; 7 of those declare an SPDX id** |

🔵 **`npm install` unpacks a tarball; it does not clone a repository.** A grant that lives only at
HEAD is never conveyed to the person who installs the package — so a licence cell sourced from a
repository can be correct about the repository and wrong about the delivery.

🔴 **The row that matters most is the copyleft one.** `moodle-mcp-server-aql` **0.1.7**
(2026-10-01) declares **AGPL-3.0** across **141 shipped paths** and ships no licence text, while
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) carries a
canonical **34 523-byte** `LICENSE`. 🔵 The strongest obligation on this shelf, conveyed without the
document that states it.

🔴 **And the mechanism is now known rather than guessed**: `canvas-mcp-server` **2.2.3**'s packed
manifest reads `files: ["build/**/*", "README.md", "LICENSE", "package.json"]` — it **names**
`LICENSE` — and its 8 shipped paths contain none. npm omits a `files` entry that does not exist in
the tree, silently. 🔵 **New rule for this page: a manifest that lists a licence is not evidence
that one shipped.**

🟢 **Direction of the error, which decides the remedy.** All nine defective rows are the repository
being *better* than the distribution — **not one package shipped a licence its repository lacked**.
The ask to an upstream is a one-line `files` change, not a relicensing conversation.

Instrument, method, committed 21-row TSV and 7 passing tests:
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🔴 **This probe reads licence FILES only**, so the `pipwerks` case — a grant in a source-file header
— stays invisible to it. **7 of 21 is a floor, not a count.** `ACTION CH` was registered to close
that hole at the repository layer and **did not run this pass**; it is re-registered.

🔴 **Scope, stated:** npm only, four platform families, one registry search each. PyPI, Maven and
crates were not probed, and `moodler-mcp` — a Python connector on this KB's shelf — **is not on PyPI
at all (404)**, so for part of the shelf there is no payload layer to measure and no registry to
arbitrate a disputed address.

**Pass 137, 2026-10-11.** 🔴 **Every licence cell on this page describes a repository ROOT, and for
half of the largest rows the root is not the whole obligation.** `ACTION BY` enumerated the file
trees of the **20 largest rows on this page** — **224 591 paths** — and found **316** licence-shaped
files outside the root, **242** of them real grants. 🔴 **Ten of the twenty (50%) carry at least one
grant whose copyright holder is not the repository's own.** The refutation threshold was **5%**.
Instrument, tests and per-row results: `compose/code/p137-foreign-holder-tree`.

🔵 **Read this next to [`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md),
which measured the other half of the same question and looks like it says the opposite.** p444: the
licence **family** read from the root file is the tree's family **92%** of the time. p137: the
**ownership** is incomplete in **50%** of the largest rows. 🟢 **Both are true, and together they
are the rule: a root licence cell predicts what you may DO; it does not predict whom you OWE.**

### 🆕 `ACTION BY` — what the trees carry, per row

| row | tree paths | non-root licence files | real grants | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **67 589** | 96 | 87 | 🔴 **66** | `FOREIGN_HOLDER_IN_TREE` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 18 127 | 76 | 58 | 🔴 **13** | `FOREIGN_HOLDER_IN_TREE` |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 13 231 | 28 | 22 | 🔴 **17** | `FOREIGN_HOLDER_IN_TREE` |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 25 823 | 17 | 13 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 5 137 | 14 | 10 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 9 273 | 18 | 11 | 🔴 **9** | `FOREIGN_HOLDER_IN_TREE` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 22 662 | 23 | 22 | 🔴 **4** | `FOREIGN_HOLDER_IN_TREE` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 4 826 | 2 | 2 | 2 | `FOREIGN_HOLDER_IN_TREE` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 17 073 | 6 | 1 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 5 749 | 8 | 8 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 7 405 | 13 | 8 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 489 | 1 | 1 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 14 | 🟡 **0 readable** | 0 | 🟡 unreadable class |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 664 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 249 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 118 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/codejail`](https://github.com/openedx/codejail) | 43 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 193 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |

### 🔴 The two findings inside the 50% that change a delivery decision

🔴 **`instructure/canvas-lms` is AGPL-3.0 at the root and ships an MIT LTI Advantage implementation
four levels down.** `gems/lti-advantage/LICENSE.txt` is **MIT, held by a named individual (Nathan
Mills)**. 🟢 **The LTI Advantage code inside the dominant North-American LMS is the permissive part
of it** — which is a different sentence from anything this page has published about Canvas, and the
one a studio needs before it decides to reimplement rather than extract. (The same tree also carries
`rick olson`'s `attachment_fu` and `Coolite Inc.`'s date library.)

🆕 **`classroomio/classroomio` (AGPL-3.0) vendors ten MIT-licensed agent-skills packs** —
`skills/*/LICENSE`, held by three outside individuals. 🔵 **This is a 2026-shaped obligation**: the
skills are exactly the part a client redistributes, and their grants are not the platform's.

🔵 **The rest of the 50% is front-end vendoring and the FSF's own text**: Fonticons, Twitter's
Bootstrap, Tiny Technologies' editor, Michael Bostock's d3, Ivan Sagalaev's highlight.js, Adobe's
cmaps, the PDFium Authors, Google's Liberation data, Mozilla; plus **The Trustees of Columbia
University** and the Apache Software Foundation inside Sakai, and a Debian maintainer's packaging
copyright inside Kolibri. The FSF appears as a holder **21 times** — a vendored licence body, not a
third-party grant, and counted because a notice obligation attaches to it too.

### 🔴 Three defects this probe produced before it produced a finding — stated, because the first two were wrong in the direction of a finding

1. 🔴 **An empty path list counted as one path**, so seven of twenty rows were first reported as
   carrying a non-root licence file they do not have. `printf '%s\n' "$empty" | grep -c ''` is 1.
2. 🔴 **Sakai's `content-copyright` i18n bundles matched on the WORD "copyright"** and produced seven
   false grants out of translated UI strings.
3. 🔴 **A four-filename licence sweep over 16 candidate rows called `kstateome/lti-launch`
   unlicensed. Tree enumeration found `License.txt` — LGPL-3.0, 7 651 B.** One of this pass's two
   absence verdicts was false, which is `p288-agpl-casefold` biting this KB a second time, and is
   why the committed instrument matches case-insensitively and ships a regression test for it.

🟡 **And one limit that keeps 50% a floor rather than an estimate:** this instrument reads licence
**files**. A grant inside a source header — the `pipwerks` case p136 corrected — is invisible to it.
🔴 **`Crosstalk-Solutions/project-nomad` defeats the method entirely**: `ROOT_ONLY` over 664 paths,
while composing Kiwix, Kolibri and Ollama **as container images**, so its real third-party
obligations are nowhere in its tree.

### 🆕 One row added to the interoperability layer, and it is university-owned

| repo | licence *(payload-read)* | ★ | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **LGPL-3.0** (`License.txt`, 7 651 B; `pom.xml` `<licenses>` agrees) | **UNMEASURED** | **2026-09-30** | 🟢 **US public university** (Kansas State University, Office of Mediated Education) | 🔴 **The only repository in this KB that maps a verified LTI launch onto a per-user OAuth grant** — `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → Canvas as that user. LTI **1.1** (OAuth 1.0a consumer model), Spring/Java, 34 paths. 🟢 **The first university-owned row in this page's standards tier**, and the pattern `P13` now copies. 🔴 LGPL + Java: port the pattern, not the file |

---

**Pass 135, 2026-10-11.** 🟢 **The assessment and course-content layer is added — the part of the
standards stack p134's interoperability section pointed at and did not reach.** p134 finished with
LTI, OneRoster, Ed-Fi and xAPI. Finishing the register (`ACTION BN`) found that **SCORM carries an
order of magnitude more code than any of them**, and that two of the six remaining standards have
almost no supply at all. Rows are below under *The assessment and content layer*.

🔴 **Every licence cell added this pass was established by hash, and the method matters more than
any single row.** `compose/code/p135-licence-sha-identity` discharges `ACTION BP` and **refutes its
premise**: not one payload in a 26-repo corpus is a whitespace variant of its canonical text. They
differ by **line wrap width** (SPDX wraps at ~105 columns, real `LICENSE` files at ~72), by
**typographic punctuation** (SPDX's GPL-3.0 uses curly quotes; shipped `COPYING` files use ASCII),
and by **the licence steward editing its own text** — two such edits are now known for GNU, the
`http`→`https` change and 🔴 **the FSF's move of `why-not-lgpl.html` from `/licenses/` to
`/philosophy/`, which was the entire remaining difference on five GPL-3.0 payloads.**
🟢 **Result: 21 of 26 resolved to a named SPDX identifier; the 5 that did not each have a named
cause, and 2 of them are correctly unmatched** because the text genuinely is not canonical.

🔴 **Two rows added this pass carry the defect this page exists to catch.**
[`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) — **391★, 130 forks,
pushed 2026-09-18 — has no licence file under any of eight probed filenames**, and
[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is published
**unlicensed and archived by the US Department of Defense body that authored both SCORM and xAPI.**
Neither can be used in a client deliverable. Both are measured absent, not inferred.
<!--corrected by p136: see "The pipwerks correction" below. The `pipwerks` half of this paragraph is
wrong about rights and right about files -- a grant IS declared, in `package.json` and the source
header. The `adlnet` half is not re-measured this pass and stands as written.-->

## 🔴 The `pipwerks` correction — `ACTION BR`, and the sentence this page got wrong

**Pass 136, 2026-10-11.** `ACTION BR` asked for the **dependency closure** of the unlicensed
`pipwerks/scorm-api-wrapper` across this KB's own rows, predicting refutation *"if no published row
depends on it."* 🔴 **The action was discharged and it answered a bigger question than it asked: the
premise of five pages of this KB is wrong.**

| what p135 published | what p136 measured |
|---|---|
| *"no licence file exists under 8 probed filenames"* | 🟢 **TRUE.** Re-confirmed; the repository's whole tree is `package.json`, `readme.md` and three source files |
| *"there is no grant, so there is no right to use it"* | 🔴 **FALSE.** `package.json` carries `"license": "MIT-style license: http://pipwerks.mit-license.org/"`, and `src/JavaScript/SCORM_API_wrapper.js` lines 11–12 carry *"Copyright (c) Philip Hutchison / MIT-style license: …"* |
| *"391★, 130 forks, pushed 2026-09-18"* — a live dependency | 🔴 **HEAD commit is 2018-09-06.** The manifest version is `1.1.20160322`. `pushed_at` moved in 2026; the code did not |
| *"the blast radius is unmeasured"* | 🟢 **Measured. One** published row on this KB's pages depends on it |

🟢 **The one dependant, and how it hides.** Seven manifest types were probed across the 324 repo
rows on this KB's non-log pages; **150 rows exposed at least one manifest**, and the only
`pipwerks` hit in any of them is **pipwerks' own `package.json`**. 🔴 **A manifest probe is the
wrong instrument**: [`numbas/Numbas`](https://github.com/numbas/Numbas) (Apache-2.0, Newcastle
University) **vendors the file** at `runtime/scripts/SCORM_API_wrapper.js` — version
**`v1.1.20121005`**, four years behind upstream's own manifest — with the copyright and MIT-style
header **intact**. GitHub code search finds **293 files** named `SCORM_API_wrapper.js` carrying that
header, including [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) and
[`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper), both in the H5P family this
KB tables on `verticals/solutions.md`.

🔵 **So the rule this page should carry is about the grant's LOCATION, not its existence.** A
filename probe measures files. A grant can live in a package manifest, a source header, or a URL —
and when it travels inside a **vendored file**, the header travels with it while the version does
not. 🔴 **The residual risk is real but different from the one this page published**: the terms are
declared, *unread* (the host is refused in this channel — DNS failure on `http`, 403 CONNECT on
`https`) and **not an SPDX identifier**, since *"MIT-style"* names no standard text.

**Pass 134, 2026-10-11.** 🟢 **This page gains the layer it was missing: the interoperability
standards an institution procures against.** `instructure/ims-lti` has sat at the bottom of this
page for many passes, described correctly as *"the integration path that avoids touching platform
source"* — and this KB never followed that sentence anywhere. Followed, it leads to **`Cvmcosta/ltijs`
(Apache-2.0, 373★, pushed 2026-10-06)**, which is larger and far more active than the row that
pointed at it, and to the first **vendor- and government-owned** repositories this KB has ever
tabled. See the new section *The interoperability layer* below, and `agents/top.md` → *Standards-native
agents*.

🟢 **`ACTION BG` is also discharged on this page** — the mirror detector p133 asked for was built and
run, one of its three proposed signals works, and `P133-A`'s inference about Canvas is narrowed. See
*The mirror rule, measured* below.

**Pass 132, 2026-10-11.** p131's rows carried forward unchanged (they were verified hours earlier
in the same date window); 🔴 **one new row changes this page's headline recommendation and refutes
this page's own flagship gap** — see `README.md` → Pass 132, `P132-C`. These are the systems a
client already runs, or would sensibly adopt, and that AI work gets attached to. Licence is the
first column that matters: it decides whether Globant can ship a derivative at all.

🔴 **Read this before trusting a licence cell.** GitHub's `license.spdx_id` reports **`NOASSERTION`
("Other")** whenever its matcher does not recognise a `LICENSE` file as a known template. That is
*not* a finding of "no grant", and p130 published it as one. Where this KB has **read the payload**,
the payload wins and the cell below says so.

## The platforms

| repo | licence | stars | last push | origin | why it is foundational |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | **9 241** | 2026-10-10 | North America (Blindside Networks, Canada) | The open virtual-classroom stack: WebRTC audio/video, whiteboard, breakouts, recordings. LGPL means linking is fine; modifying the library itself carries reciprocity. The place live-session AI (transcription, attention, summarisation) attaches. |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **8 195** | 2026-10-10 | North America (Open edX / Axim) | The LMS + Studio behind MOOC-scale deployments. **Renamed:** this repo was `openedx/edx-platform`; the old URL still resolves and the README says "formerly known as edx-platform". Write the new name — earlier passes of this KB cite the old one. |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | **7 473** | 2026-10-09 | APAC (Moodle HQ, Perth, Australia) | The most deployed LMS in the world, ~2 000 plugins. **Important for delivery:** this GitHub repo is a *public mirror* of `git.moodle.org` — pull requests do not go here, and it publishes no GitHub releases. Contribution goes through Moodle's own tracker and git server. 🟢 **Its mirror is live (pushed 2026-10-09), which is exactly why Canvas's frozen one was mistaken for a quiet project rather than a stopped job.** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | **6 863** | 2026-04-30 **(mirror frozen — not inactivity)** | North America (Instructure, US) | The dominant LMS in North American higher ed and the one with the richest third-party API surface — which is why every MCP connector on the agent shelf targets Canvas first. 🔴 **Corrected by p133: this KB called it "the quietest of the major platforms" for four passes and that was a measurement error.** The repo's own topics include **`gerrit-mirror`**, and `instructure/analytics` carries the identical `pushed_at` **one second later** (14:52:10 / 14:52:11 on 2026-04-30) — a batch export, not a human push. 🟡 **The correct statement: the public GitHub mirror has been frozen since 2026-04-30, so GitHub is not a usable activity signal for Canvas, and anyone diffing this tree to track upstream has been reading a stale copy for five months.** Development is in Instructure's Gerrit; `updated_at` still moves daily. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | **6 845** | 2026-10-11 | Global (Oppia Foundation) | An online learning platform built around structured, explorable lessons with built-in misconception handling. **The only major education platform under a permissive licence** — so the one a client can fork into a closed product without reciprocity. Underrated for exactly that reason. Android client: [`oppia/oppia-android`](https://github.com/oppia/oppia-android) (Apache-2.0, 418). |
| [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | **3 299** | 2026-10-11 | APAC (Frappe, India) | Modern, actively developed LMS on the Frappe framework — so it sits next to Frappe/ERPNext finance and HR data without integration work. The strongest APAC-origin platform here. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2 336 | 2026-10-11 | unplaced | Next-generation learning platform, Python/Next.js, AI features first-class rather than bolted on. Young, fast-moving. |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | AGPL-3.0 | 1 717 | 2026-10-11 | unplaced | Education platform aimed at companies running cohort training. Relevant to corporate-L&D engagements rather than academic ones. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1 237 | 2026-10-09 | North America (Apereo Foundation) | Long-lived Java academic LMS. ECL-2.0 is Apache-2.0 with an educational-community patent tweak — **permissive**, and the licence most people misread as restrictive. Strong fit where a client already runs Java/Oracle estate. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | 1 127 | 2026-10-08 | EMEA (Overhang.IO, France) | The Docker-based Open edX distribution — in practice *the* supported way to stand up and upgrade Open edX. A large first-party plugin ecosystem, all AGPL-3.0: `tutor-mfe` (micro-frontends), `tutor-cairn` (real-time analytics), `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. If the engagement is Open edX, it is a Tutor engagement. |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 141 | 2026-10-10 | Global (Learning Equality) | Offline-first learning platform for low- and no-connectivity classrooms; content syncs by LAN or USB. **MIT-licensed**, which with its offline design makes it the single best base for rural LATAM, African and South Asian deployments. Content tooling: [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192). |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1 009 | 2026-10-10 | EMEA (Chamilo Association, Belgium) | LMS built around ease of use and accessibility, with real institutional adoption in Francophone Europe and Spanish-speaking LATAM. The most LATAM-relevant of the EMEA-origin platforms. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The natural target for the administrative automation nobody else serves. 🔴 **Licence corrected by p131.** GitHub's API reports `NOASSERTION` and p130 published that as "review terms before use". This KB had already **read `master/LICENSE` in full — 8 241 bytes, genuinely LGPL-3.0** — and used that read to *retract* an even earlier "no grant" row. p130 reinstated the retracted claim by trusting the API field over its own evidence. **LGPL on an LGPL Odoo base: linking is fine, modifying the module itself carries reciprocity.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## The offline / low-connectivity stack (added by p132 — and it refutes this page's own gap)

🔴 **This page has carried, for several passes, that "the offline slot is the cleanest unclaimed
opportunity in this KB". It is not unclaimed.** It is occupied by the second-largest repository
anywhere in this KB.

| repo | licence | stars | origin | why it is foundational |
|---|---|---|---|---|
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 **Apache-2.0** | **39 444** | unplaced | **Offline-first knowledge and education server**: Wikipedia, thousands of books, courses, maps and optional local AI, all on hardware the client owns with no internet required. Architecturally a **Docker orchestration layer over containerised tools** — **Kiwix** powers the Information Library, **Kolibri** powers the Education Platform, **Ollama** powers the AI Assistant (the installer provisions Ollama on the host; an external OpenAI-compatible endpoint is also supported). 🟢 **Permissive, so a client can ship a derivative.** 850 commits, updated the day of this pass. |
| [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 **UNREAD** | 20 | unplaced | macOS / Apple Silicon port, bundling Ollama, Open WebUI, Kiwix, Kolibri and FlatNotes. Useful as a single-machine pilot before committing to the Docker stack. Licence not measured this pass. |
| [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) | 🟡 **UNREAD** | 2 | **APAC (India)** | Offline LMS for Class 10 Maths and Science on the Indian curriculum: FastAPI + React + RAG over structured chapter data with a local Ollama model, gamified quizzes, LAN-only operation, and a claimed Kolibri integration. 🔴 **Duplicate pair** with [`Tushar-cy/Ai-edge-learning-hub`](https://github.com/Tushar-cy/Ai-edge-learning-hub) (same owner, byte-identical description). Small, but the only row that targets a *named national curriculum* offline. |

🔵 **Why eleven passes missed it, and why the probe was not at fault.** p131 ran `kolibri stars:>2`,
got 86 repos, correctly resolved 3 to the Learning Equality family and 0 with AI. **The probe was
valid; the conclusion was false.** NOMAD *composes* Kolibri as a container and never names it in
its description — the dependency appears only in the README architecture. **A dependency is not
always visible in the metadata of the thing that depends on it.**

🟢 **What this changes for an engagement.** The low-connectivity offer stops being *"build an
offline tutor"* and becomes *"deploy and extend an Apache-2.0 stack that already composes content,
library and local inference"* — faster, cheaper and far more defensible in a procurement
conversation. Kolibri (MIT) remains the right content layer; what changed is that the integration
around it already exists. See `compose/patterns.md` → P2.

## Administrative automation — the first optimiser (added by p132)

| repo | licence | stars | origin | what it gives you |
|---|---|---|---|---|
| [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | Conflict-free academic timetable generation under **India's NEP 2020**: electives, faculty availability, courses, rooms, balanced workloads, scenario simulation, manual overrides, exports, and a natural-language interface over MCP. 🟢 **The "most-cited driver, least-served tier" finally has a repo, and it is an optimiser rather than an LLM wrapper.** 🔴 One star — a reference design, not a dependency. |

## 🟢 The interoperability layer — how AI attaches without touching platform source *(new, p134)*

🔴 **Read this section before proposing a fork of anything above it.** Every platform in *The
platforms* is AGPL-3.0, GPL-3.0, LGPL-3.0 or ECL-2.0, and this KB spends a lot of words on which
reciprocity obligation bites when. 🟢 **The standards below make most of that moot:** a tool
launched over **LTI 1.3** runs as a separate application with its own licence, talking to the LMS
over HTTP. It never links platform code, so it inherits **no** copyleft obligation from Moodle,
Canvas or Open edX — and it is *invited in* by a client ID the institution issues and can revoke,
rather than holding a user's password.

| repo | licence | stars | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (payload-read) | **373** | **2026-10-06** | named individual | 🟢 **The reference LTI 1.3 Advantage tool provider, and the headline addition to this page.** OIDC launch, Deep Linking, AGS grade passback, NRPS rosters. **1.8× the stars of `ims-lti` and pushed five days before this pass** — where `ims-lti` is Instructure's library for *their* platform, this is the platform-independent one. If an engagement puts AI inside an existing LMS, this is the integration dependency. |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (payload-read) | 138 | 2024-08-18 | named individual | The Python LTI 1.3 Advantage library (Django/Flask). 🔴 **Dormant ~2 years**, and that is the most consequential staleness on this page: Python is where the agent frameworks live, so the LTI binding for an agent build is the least-maintained link in the chain. |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (payload-read) | 6 | **2026-10-09** | 🟢 **standards body** | Serves a **OneRoster 1.2 API from an Ed-Fi ODS**. The bridge between the two US K-12 data standards, written by the body that owns one of them. 🟢 **Stars are the wrong measure here: this is the row that makes a US K-12 rostering story procurement-safe.** |
| [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** (payload-read) | 7 | 2026-07-30 | 🟢 **platform vendor (Google)** | Conformance tests for a OneRoster integration. 🟢 **The only test suite in this KB that proves an integration correct rather than asserting it.** |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (payload-read, 711 B) | 10 | 2026-05-11 | named individual (noreply addr) | TypeScript OneRoster SDK. 🟢 **0BSD — the most permissive licence in this KB; it drops even attribution**, so a derivative carries no notice obligation at all. |
| [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) | 🟢 **MIT** (payload-read; holder **"UNIwise ApS"**) | 3 | 2026-06-11 | 🟢 **platform vendor (EMEA, Denmark)** | Integration packages for the **WISEflow** assessment platform — user creation, flow setup, assessor allocation, **grade passback**. 🟢 **A European assessment vendor publishing its own MIT integration path**: the cleanest EMEA counterparty in this KB, and the opposite of the unsanctioned-connector problem. |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | 17 | **2026-10-11** | 🟢 **national public operator (EMEA, France)** | Learning-analytics visualisation over **xAPI**. Same owner as [`openfun/richie`](https://github.com/openfun/richie) below — 🟢 **France Université Numérique now gives this KB two MIT rows, and this one was pushed on the day of this pass.** The dashboard layer over an LRS. |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 15 | 2025-08-29 | named individual | 🟢 **The only repo found that bridges an AI agent to a sanctioned standard**: an MCP server that records and retrieves learning activity through an xAPI Learning Record Store. 🔴 **15 stars, last push ~14 months ago** — load-bearing and unmaintained, which is precisely why it is a build item rather than a dependency. Full tier in `agents/top.md`. |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | **Apache-2.0** | 12 | 2025-07-03 | 🟢 **government (US DoD ADL Initiative)** | xAPI profile for lifetime learner tracking, from the body that authored xAPI. The modelling reference for an LRS schema. |
| [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) | 🔴 **no licence field** | 0 | 2026-04-14 | 🟢 **government (Minnesota Dept of Education)** | C# SDK for a US state's Ed-Fi ODS API. 🔴 **The best-owned row on this page and unusable, because it carries no grant** — the recurring shape of this KB in one line. |

🔵 **The licence asymmetry is worth stating plainly, because it inverts this page's usual advice.**
*The platforms* are copyleft almost without exception and the one permissive major platform
(`oppia/oppia`, Apache-2.0) is the one nobody asks for. 🟢 **The interoperability layer is
permissive almost without exception** — Apache-2.0, MIT and 0BSD, with named vendor and government
holders. **So the licence-safest way to build on a copyleft platform is to not build on it at all,
and to attach over a standard instead.**

🔴 **And the honest limit of this section:** these are libraries, conformance tests and profiles.
They are the plumbing a security review passes. **None of them contains any AI**, and the one row
that joins them to an agent has 15 stars and has not been pushed in over a year.

## 🟢 The mirror rule, measured — `ACTION BG` discharged *(p134)*

p133 corrected a four-pass claim that `instructure/canvas-lms` was *"the quietest of the major
platforms"*, having found the topic `gerrit-mirror` and a sibling repo sharing its `pushed_at` one
second later. 🟢 **`ACTION BG` asked for that to become a detector before any further freshness
claim published. It was built and run over the 40 most-recently-updated `instructure` repositories,
and the result is mixed in a useful way.**

| proposed signal | verdict | measurement |
|---|---|---|
| **a topic containing *mirror*** | 🟢 **WORKS — and the defect is a lane, not a row** | **5 of 40** repos carry `gerrit-mirror`: `canvas-lms`, `dockerfiles`, `switchman`, `screencap`, `outrigger`. `ACTION BG`'s refutation condition (*"refuted if `canvas-lms` is the only mirror"*) is **not met** |
| **two repos in an org sharing `pushed_at` to the second** | 🔴 **DOES NOT GENERALISE — retire it** | across 40 repos, **no timestamp is shared by more than one repo.** p133's own evidence was two *adjacent* seconds (`:10` and `:11`), not a shared one; generalised into a detector it finds nothing |
| **a README naming an upstream elsewhere** | 🟡 **NOT TESTED** this pass | would need a payload read per repo; the topic field is cheaper and sufficient |

🔴 **And the measurement narrows `P133-A`'s inference.** p133 concluded 2026-04-30 was *"the date
their export to GitHub stopped running"*. 🟢 **It was not: sibling mirrors in the same org received
exports on 2026-09-30 (`switchman`) and 2026-10-08 (`dockerfiles`)** — three days before this pass.
**The Gerrit export job is running; `canvas-lms` specifically stopped receiving it.** Whether that
is a disabled export, a renamed upstream branch or a deliberate halt is not visible from here, and
this KB should not guess. 🟢 **p133's operative conclusion survives intact and is the one to quote:
`pushed_at` on `canvas-lms` is not an activity signal.** Its stronger causal story does not.

🟢 **The control that makes the rule usable:** [`instructure/ims-lti`](https://github.com/instructure/ims-lti)
carries **no** mirror topic and was pushed **2026-10-02**. **So within one org, some repos are
mirrors and some are GitHub-native, and the topic tells you which.** `pushed_at` is a valid
freshness signal for `ims-lti` and an invalid one for `canvas-lms` — which means freshness must be
checked per repo, never per organisation.

### 🔴 p136 runs the rule over the whole corpus — and 44% of its hits are not mirrors at all

`ACTION BU` asked for p135's successor signal (README **byte-identity**, which p135 called *"a
verdict"* against licence grouping's *"lead"*) to be applied corpus-wide. **1 389 READMEs fetched
over 1 528 published rows → 71 byte-identical clusters, 25 of them cross-owner** — twelve times
`ACTION BU`'s refutation threshold, so **not refuted**. 🔴 **But the word "verdict" does not
survive:**

| lineage verdict | clusters | what it means here |
|---|---|---|
| `ALIAS` — **identical ref set** | 🔴 **11** | **One repository under two slugs.** GitHub keeps answering a renamed owner or repo name, so the "two owners" are one |
| `DIVERGED_FORK` — shared commit shas | 5 | A real fork; count the connector once |
| `FORK_AT_TIP` — same HEAD, different ref sets | 4 | A fork that has not diverged yet |
| `ATTRIBUTION_STRIPPED_COPY` — identical root tree, **zero** shared commits | 1 | the ENEM cluster (`ACTION BW`, below) |
| `SQUASHED_COPY` — one side a single commit | 1 | `0awei0/kt`, and it **dropped the upstream MIT file** |
| `UNRESOLVED` — measurement not taken | 🔵 3 | **said, not guessed** |

🔴 **One of the eleven aliases lands on a conclusion this KB published.** `agents/trending.md`
reasoned about `theopenem/OneRoster.NET` versus `jdolny/OneRoster.NET` — *"both licences name
`theopenem` as copyright … so pin `theopenem`"* — when the two slugs have an **identical ref set**
(`3f4540f9706d9099`) and are **one repository**. The pin is harmless; the reasoning was about a
distinction that does not exist. 🟡 `KI-Campus/LRS` and `openHPI/openLRS` are the same case across
*both* a rename and a transfer.

🔴 **And 37 further clusters are this KB citing one repository under two spellings** — `Elgg/Elgg`
and `elgg/elgg`, `Schroedinger-Hat/certo` under **three**, eight `Opetushallitus/*` pairs. That is
`p443`'s case-collision class measured across the whole corpus for the first time.

🟢 **The rule, generalised for this page.** Freshness must be checked per repo (p134).
**Identity must be checked before freshness**: resolve the slug to a repository by **ref set**, then
ask about forks, then ask about dates. Instrument, six verdicts and 10 tests:
`compose/code/p136-lineage-verdict/`.

## 🟢 The assessment and content layer — added by p135

The standards an institution procures against do not stop at rostering and grade passback. Two more
carry real code: **SCORM**, which packages and tracks course content, and **QTI**, which carries
assessment items. This is where an AI engagement touching *content* or *assessment* attaches.

| system | repo | licence *(hash-verified)* | ★ | pushed | owner | why it is foundational |
|---|---|---|---|---|---|---|
| **Adapt Framework** | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** 🆕 *(p136: `UNMATCHED` → `RESOLVED` at ratio `0.997431`, holder **"2013 ADAPT LEARNING"**, 11 opcodes and not one an added clause)* | **630** | **2026-10-10** | Adapt community | The largest repo in the whole standards stack. Authoring toolkit producing responsive, accessible, multi-language courses that emit **both SCORM and xAPI**. 🔵 Copyleft: run it as a tool, do not link it |
| **OpenOlat** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0 + attribution** | **447** | 2026-10-09 | frentix GmbH / Univ. of Zurich | 🟢 **A full Java LMS this KB had never tabled**, with QTI, SCORM, curriculum management, assessment and lecture management built in. The permissive full-featured LMS this page's flagship gap says does not exist — see the verdict below |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **354** | 2026-10-09 | individual | The modern SCORM 1.2 / 2004 runtime. **Offline-first**, TypeScript, actively maintained. 🟢 **The permissive replacement for the unlicensed `pipwerks` wrapper** |
| **Numbas** | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | 215 | 2026-10-09 | 🟢 **Newcastle University (UK)** | Browser-based e-assessment, strongest in mathematics, SCORM-packageable. **Institution-owned and permissive** — the cleanest base for assessment work before the 2027 clocks. 🆕 **p136: it vendors `pipwerks`' SCORM wrapper** (`runtime/scripts/SCORM_API_wrapper.js`, `v1.1.20121005`, header intact) — the only `pipwerks` dependant on this KB's pages, and a reminder that Apache-2.0 at the root says nothing about a vendored subtree |
| **QTI 3 item player** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** | 30 | 2026-04-07 | amp-up.io | The reference renderer for QTI 3 assessment items, with a four-component sibling family from the same vendor |
| **Mentingo** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 92 | **2026-10-10** | Selleo (PL) | 🟢 **An AI-native LMS under a permissive licence** — AI mentor, role-play, SCORM and xAPI, white-label, self-hosted. Small, but the only row where the AI is the platform's architecture rather than a bolt-on |
| **1EdTech validator** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** | 17 | 2026-09-23 | 🟢 **1EdTech (the standards body)** | Conformance validation for **Open Badges and Comprehensive Learner Record**. The second conformance suite this KB has found, and the steward's own |

🔴 **Do not reach for these two, and the reason is the licence, not the code**

| repo | ★ | problem |
|---|---|---|
| [`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) | **391** | 🆕 **p136: the reason changed.** The grant is **declared by reference** (`package.json` + source header, *"MIT-style license"* at a host refused in this channel) — so *"confers no rights whatsoever"* is withdrawn. Reach instead for `scorm-again` because **HEAD here is 2018-09-06** and *"MIT-style"* is not an SPDX id, not because there is no grant |
| [`cybercussion/SCOBot`](https://github.com/cybercussion/SCOBot) | 164 | **CC-BY-SA-4.0, and the file is only the 837-byte human-readable deed.** ShareAlike copyleft, no patent grant, and a content licence applied to code |

### 🔴 What this layer does NOT have

| standard | supply measured this pass |
|---|---|
| **Caliper Analytics** | 🔴 **One repository, 0★, no licence, last touched 2023.** The standard for carrying learning events to an analytics layer has no usable open-source client in any language |
| **Comprehensive Learner Record** | 🔴 **One real repository** — the 1EdTech validator above. The other two hits are an empty 2018 repo and a student project |
| **LTI Deep Linking**, probed alone | 🔴 **One repository, which declares in its own description that Deep Linking is not supported.** In practice it exists only inside `ltijs` |

## Supporting infrastructure

| repo | licence | stars | what it gives you |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 470 | The component framework for custom learning activities inside Open edX. Permissively licensed even though the platform around it is AGPL — so a custom XBlock is the lowest-friction way to put an AI activity inside Open edX. |
| [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | 476 | Sandboxed execution of untrusted code. Directly reusable wherever an agent runs learner-submitted or model-generated code — an auto-grader for programming courses, for instance. |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 354 | Modern SCORM/AICC/xAPI runtime in TypeScript. The bridge between legacy courseware a client already owns and anything new. |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 316 | Django/React CMS for building course catalogues and education portals in front of Open edX. From France Université Numérique, so it is proven at national scale in EMEA. |
| [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | 263 | The H5P interactive-content family (Norway); the Moodle binding is [`h5p/moodle-mod_hvp`](https://github.com/h5p/moodle-mod_hvp) (GPL-3.0, 157). The standard way to ship interactive activities into an existing LMS. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 404 | Laravel/Filament school-management platform for small and mid-size institutions. MIT, so the most forkable administrative base here. |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | 203 | LTI tool-provider/consumer library. LTI is how an external AI tool gets launched from inside any compliant LMS — the integration path that avoids touching platform source, and therefore avoids AGPL reciprocity entirely. |

## The system-of-record tier (restored by p131)

p130's declared gaps said *"`openeducat_erp` (licence unclear) and `academico` (small) are the whole
field."* 🔴 **They are not.** This KB read a system-of-record tier in an earlier pass and p130's
rewrite dropped it. Restored here, because "there is no open-source SIS" and "every open-source SIS
is copyleft" are completely different briefings for a client.

| repo | licence | why it matters | the catch |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | **NOASSERTION** (API) — read terms | **662★**, pushed 2026-10-05, 454 forks. Full school management on Frappe: students, programmes, fees, assessment. Sits beside ERPNext finance/HR with no integration work. | Licence does not resolve to an OSI identifier via the API; GPL-3.0 in the Frappe family's own documentation. **Read `LICENSE` before committing** — this is exactly the row class p130 got wrong. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886★. The Odoo-based ERP; the broadest functional coverage of the tier. | Odoo module, so you inherit the Odoo ecosystem *and* its constraints. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | **404★**, pushed 2026-10-07. Laravel/Filament. **The only permissive SIS**, so the only forkable base for a closed client product. Carries the topic `student-information-system`. | Small, and aimed at small-to-mid institutions rather than a university of record. |
| **RosarioSIS** | GPL-2.0 | A genuine student information system with real deployments. | GPL-2.0 — the most restrictive option here. |
| **Gibbon** | GPL-3.0 | School platform with a long institutional track record. | GPL-3.0 reciprocity. |
| **openSIS** / **Fedena** | copyleft / mixed | Named in this KB's earlier reads of the tier; both long-lived. | Neither is permissive; verify the current edition's terms, since both have had commercial forks. |

🔵 **Provenance of the four rows without links.** RosarioSIS, Gibbon, openSIS and Fedena are
carried from **this KB's own earlier read of the tier** (`agents/trending.md:5160`, which recorded
`RosarioSIS mobile@899f6da` GPL-2.0, `Gibbon v31.0.00@683d2c4` GPL-3.0 and `OpenEduCat 19.0@1c95cef`
LGPL-3.0 at specific commits). 🔴 **They were NOT re-verified this pass and are deliberately listed
without links** — a row this pass did not measure does not get presented as one it did. Re-verify
before quoting them to a client; the three linked rows above were verified this pass and are in
`evidence/verified-repos.2026-10-11-p131.tsv`.

**The honest summary for a client:** there are **at least six** open-source systems of record. Exactly
**one** (`academico`, MIT) can become a closed derivative; one more (`openeducat_erp`, LGPL-3.0)
permits linking without reciprocity. The rest are GPL-family. 🔴 **So the gap is not supply — it is
that the system-of-record tier is almost entirely copyleft**, which is a licensing conversation at
the start of an engagement, not a missing-software conversation.

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release. 🟢 **And if the constraint
is connectivity rather than licensing, start from `Crosstalk-Solutions/project-nomad`
(Apache-2.0, 39 444★) instead of assembling the stack yourself** — it already composes Kolibri,
Kiwix and a local model, and it is permissive enough to fork.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia
  (Apache-2.0) and Sakai (ECL-2.0) are the permissive options and neither is a drop-in replacement
  for either. 🟢 **SURVIVES.**
- ~~**No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.~~ 🔴 **REFUTED by p131** — see the system-of-record tier
  above: at least six systems, read by an earlier pass and dropped by p130's rewrite. 🟢 **The
  surviving gap is that the tier is almost entirely copyleft, with `academico` (MIT) the lone
  permissive base — and that no AI *agent* targets any of them** (`agents/top.md`).
- **Canvas is the quietest major platform** (last push 2026-04-30, ~5 months) 🔴 **and it is now
  ~5.5 months quiet, unchanged on re-check this pass.** Worth raising explicitly before
  recommending it as an actively developed base — it is still the richest API surface in the
  sector, which is why every connector targets it.
- ~~**Three Kolibri-family repos, zero AI on any of them.** A valid re-probe this pass
  (`kolibri stars:>2` → 86 repos) resolves the family to three Learning Equality repos; the other
  83 are name collisions. **The offline slot is still the cleanest unclaimed opportunity in this
  KB** (`intel/trends.md` → T8).~~ 🔴 **REFUTED BY p132.** The family resolution was right —
  [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, 1 141★),
  [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192★),
  [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
  (52★) — **and the conclusion drawn from it was wrong.**
  [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
  (**Apache-2.0, 39 444★**) runs Kolibri as its education container beside Kiwix and Ollama, and
  does not contain the string `kolibri` in its description. 🟢 **The surviving gaps are narrower and
  real: (a) no AI project builds *inside* Kolibri itself** — NOMAD orchestrates it from outside and
  the Learning Equality repos carry no AI; **(b) nothing offline targets LATAM.** The one
  curriculum-specific offline row found is Indian (`Tushar-cy/Offline-AI`), and LATAM — where this
  KB argues offline is a first-class requirement rather than an edge case — has none.
  🟡 **Also note a new collision source: Aleph Alpha ships a 78B model called "Kolibri".**

### 🟡 p135's verdict on this page's flagship gap

- **"No permissively licensed, full-featured LMS at the scale of Moodle or Canvas."**
  🟡 **NARROWED, and honestly it is weaker than it was.**
  [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is **447★**, pushed 2026-10-09, under
  **Apache-2.0** (with two attribution statements replacing the appendix — permissive in effect),
  and it ships QTI, SCORM, curriculum management, assessment and lecture management in one Java
  codebase. It is a real, maintained, permissive, full-featured LMS, and **this KB had never listed
  it.** 🔴 **The gap survives only in its "at the scale of Moodle or Canvas" clause** — OpenOlat is
  447★ against Moodle's order of magnitude more, and its deployment base is concentrated in
  German-speaking Europe. 🔵 **For an EMEA engagement that clause may not matter**, and this is now
  the first permissive answer this page can give to *"we want off Moodle's GPL."*
- 🆕 **The offline gap gains a permissive component it did not have.**
  [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT, 354★) lists `offline-first`
  among its own topics and implements the SCORM runtime client-side. 🟢 **That is the missing piece
  between `T8`'s offline requirement and standards-tracked course delivery** — a learner can
  complete tracked content with no connectivity and reconcile later. It still does not close *"no
  AI project builds inside Kolibri itself"*, and it still is not LATAM-originated.

### 🆕 Gaps this page opens after p135

- ~~**The sector's most-used SCORM library is unlicensed, and the blast radius is unmeasured.**~~
  🟢 **CLOSED AND CORRECTED by p136 (`ACTION BR`).** A grant is declared (manifest + source header);
  the blast radius on this KB's own pages is **one row**, `numbas/Numbas`, by **vendoring** rather
  than by manifest; and the sector-level reach is **293 files** carrying the header. 🔴 **What
  replaces it is narrower**: the declared body is unreadable in this channel and *"MIT-style"* is
  not an SPDX identifier, so the row's terms are *declared and unread* — and `pipwerks`' HEAD commit
  is **2018-09-06**, which makes it a stale dependency regardless of its licence.
- 🔴 **No permissive Python library exists for Open Badges.** Both Python rows are copyleft
  (LGPL-2.1 and LGPL-3.0). The permissive credential work is in **Rust** (`impierce`, Apache-2.0)
  and **Java** (`1EdTech`, Apache-2.0), which is a language mismatch for most AI engagements.

### 🆕 Gaps this page opens after p136

- 🔴 **This page's dependency picture is manifest-shaped, and the sector's is not.** `ACTION BR`
  measured 150 of 324 rows exposing at least one of seven manifest types; the one dependency that
  mattered was **vendored**, invisible to all seven. Until a tree-level probe runs (the instruments
  exist — `compose/code/p275-tree-enumeration`, `p441-tree-licence-enumeration`), **every "no
  dependants" statement on this page is a statement about manifests**.
- 🔴 **A root licence says nothing about a vendored subtree, and this page tables root licences.**
  `numbas/Numbas` is Apache-2.0 at the root and carries an MIT-style third-party header four levels
  down. Of the 24 rows in this page's platform and standards tables, **the number whose vendored
  subtrees have been read is zero.** 🔵 **This is `p969-root-only-licence-reach` one level deeper.**
  p93 measured that the grant ladder cannot see a **per-directory** licence (`bncc-dados`: code at
  the root, data one directory down). p136 measures that it cannot see a **third-party header inside
  a vendored file** either — same blind spot, and the vendored case is the common one in a sector
  whose code moves by copying.
- 🟡 **Three `UNRESOLVED` lineage clusters remain** (`education-ai-suite`, `OpenPronounce`,
  `agents-radar`). Each needs one clone per side; none is an education-supply row, which is why they
  were left — recorded so the 25-cluster figure is not read as 25 resolved.
