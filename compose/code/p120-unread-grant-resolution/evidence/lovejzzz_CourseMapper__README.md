# EduTool

[EduTool.dev](https://edutool.dev) is an editable course-material workspace for educators. The current release is **v0.20.09** (see [`release.json`](https://edutool.dev/release.json) for the deployed commit). It preserves the **0.18.7 interface**, local Scion, all ten material categories, the existing editors and applicable exports.

**v0.20.09** checks English quiz answers for who said what, reasoning errors and repeats, and computes more answers exactly (see [docs/v0.20.09-english-question-checks.md](docs/v0.20.09-english-question-checks.md)). **v0.20.08** builds quizzes from the teacher's own material: poems, dialogues, data and dated facts in the description are kept verbatim and shown in each material, Scion writes one checked question at a time from them, calculation answers are computed in code, and Chinese descriptions set lessons, minutes and quiz size correctly. See [docs/v0.20.08-material-quality.md](docs/v0.20.08-material-quality.md) for the live twelve-course result. **v0.20.07** simplifies the interface: one description box on the homepage, one setup page with editable lessons, minutes and quiz size, a full-width workspace with Assistant and Export drawers, and material views that show each objective, source and note once. **v0.20.06** applied the fixes from the September 22, 2026 site audit: correct lesson and quiz counts from course descriptions, materials pre-selected from the description, labeled retrieval instead of silent cross-lesson repeats, distinct lesson-plan prompts, whole artifact names, Wikisource and zh.wikipedia research routing, a visible model-download notice, accessibility fixes and a strict classroom benchmark in `npm run check`. See [docs/v0.20.06-audit-fixes.md](docs/v0.20.06-audit-fixes.md) for what changed, how it was verified and what remains. Earlier notes below describe the v0.19.x releases and are kept as history.

Reviewed shared tasks connect source records, reference answers, scoring and material revisions. A direct material regeneration refreshes related reviewed-task materials atomically, protects teacher edits, and rejects stale changes. Source-review drafts, selections from large source packets, project recovery, student-copy exports, full lesson objectives and worked explanations have been improved.

**Scope decision (September 8, 2026):** release the implemented improvements as v0.19.99 and reserve the ground-up architecture and unfinished ambitious features for a separate rebuild. This is not completion of the original v0.20.0 roadmap. Natural local generation still has demonstrated source-attribution and answer-quality failures; shared tasks may require explicit teacher review. No new model-weight, universal classroom-readiness or learning-outcome claim is made. Broad fresh-model acceptance, three newly accepted six-lesson courses and live Google conversion are not certified by this stabilization release.

See the [v0.19.99 release verification](docs/v0.19.99-release.md), [historical implementation evidence](docs/v0.20.0-implementation.zh-CN.md), and the separate [ground-up design and coding handoff](docs/edutool-ground-up-design.en.md). The [original roadmap](docs/v0.20.0-roadmap.zh-CN.md) retains its unfinished gates for reference; its dates and development reports are historical evidence, not current release claims.

Quality improvements continue within this interface. The experimental Course Studio replacement is preserved for research; it is not the production application.

v0.19.2 extends the shared-task compiler with eight bounded evidence operations: dated stages, effective amendments, cropped charts, testimony attribution, coupled interventions, cache/order, label/order and initial-condition/duration comparisons. Independent cases, answers, feedback and four-level rubrics stay connected across all ten materials. Full experimental designs and short error-diagnosis questions now have different scoring requirements. Chinese course actions and compiler directions are supported; assignment teacher references always start on a new page. Supported source tasks also regenerate directly without a redundant model refresh. Accepted source edits update matching resource packets in the saved course map and material grounding as well as visible answers, while preserving unrelated resources and teacher annotations. See the [output and export review](docs/v0.19.2-output-review.zh-CN.md).

At the v0.19.2 release, all 30 existing source packets passed the then-current automatic checker. These cases were exposed during development; that was regression evidence, not a new blind evaluation. The current pooling contract additionally requires explicit distinct-group membership: the original depot packet lacks that premise and does not automatically produce a shared task; the v0.19.99 export regression uses an explicitly adapted fixture while retaining the original refusal check. The original failures remain published. Four complete fictional workshop packages accompany the [v0.19.2 release](https://github.com/lovejzzz/CourseMapper/releases/tag/v0.19.2), including Chinese source analysis and experimental design. They use the actual application exporters with zero new model calls. Parsing remains bounded, institutional syllabus details need confirmation, and exported guides retain some repeated explanations. No model-weight or learning-outcome improvement is claimed.

v0.19.1 introduced source-quantity reasoning: combine counts across groups, bound unknown overlaps, and distinguish count shares from measured amounts. Its [historical review](docs/v0.19.1-output-review.zh-CN.md) retains the eight then-unsupported cases and earlier results.

v0.19.0 adds precise source-driven updates, teacher-edit conflict review, transaction undo/redo, independent practice and stronger export checks. Three complete workshop samples and their [educational export review](docs/v0.19.0-output-review.zh-CN.md) accompany the release. Its [acceptance record](docs/v0.19.0-acceptance.zh-CN.md), [30-case benchmark](benchmarks/classroom/v2/README.md) and [actual local-model investigation](research/scion/evaluation/v0.19.0/README.md) distinguish completed software verification from unresolved source-understanding and educational-quality work. The first held-out failures remain published; passing development cases is not a claim of general classroom readiness.

The [v0.19.0 release](https://github.com/lovejzzz/CourseMapper/releases/tag/v0.19.0) includes three editable Office course packages, 27 PDF handouts, verification records and SHA-256 checksums. The examples cover proportions and rounding, conflicting historical records, and fair experimental comparisons. They are single-session workshops drawn from the development set.

## Materials and workflow

Start with a course description or existing files, choose materials, configure the course, then review and edit the resulting package. The original material categories are:

- Course Map
- Syllabus
- Lesson Plans
- Slide Decks
- Assignment Briefs
- Rubrics
- Discussion Prompts
- Quiz & Exam Bank
- Study Guides
- Course FAQ

Custom deliverables, `.coursemapper` project files, local session recovery, version history and the original material-specific editors remain available. Linked changes use the existing course model and sync/review workflow. Check affected materials after changing an objective, assessment or source; a synchronized field is not proof that every dependent answer is correct.

Exports retain the original material-dependent choices, including Word, PDF, CSV, PowerPoint, Google Docs/Sheets/Slides and course ZIP packages. PDF handouts share the Word content builder, preserve mathematical symbols and Chinese text, and keep quiz answers on a separate page. PDF rendering runs locally; the renderer and any needed Chinese fonts load on demand from the site. Downloaded and Google Drive files are snapshots; edits to those copies do not automatically return to EduTool.

## Scion research and the fast compiler

Scion inference remains local. Optional **Scion web research** uses browser-readable public catalogs (Wikipedia, DOAJ, Europe PMC, and W3C/WAI for accessibility). It does not call the paused hosted model or require a rented inference server. Queries can include the course title, lesson topics and concepts; private research-off mode sends no such queries.

The research transport now serializes requests, deduplicates successful and failed reads, shares one time/request budget across discovery and repair, and moves on after a provider rate limit. A single-lesson transaction has at most 14 requests and 20 seconds of network budget; larger courses are capped at 96 requests and 60 seconds. An approved teaching plan already covered by instructor facts, or a single-lesson route that copies only the frozen instructor ledger, skips redundant research unless current evidence is requested.

Publication, content-revision, indexing and retrieval dates remain distinct. A new index entry or download does not make an old paper current. Time-sensitive scholarly queries include publication filters; undated or old evidence alone cannot pass the current-evidence gate. These are bounded catalog searches, **not unrestricted browsing of every website**. Recent source dates also do not prove present legal, clinical or scientific applicability. Misses, conflicts and incomplete evidence remain visible for review. API behavior follows [Europe PMC documentation](https://europepmc.org/RestfulWebService), [DOAJ publication metadata](https://doaj.github.io/doaj-docs/master/data_models/IncomingAPIArticle.html), and [MediaWiki request guidance](https://www.mediawiki.org/wiki/API:Etiquette).

The compiler creates reusable guided-practice units that keep a question, reference answer and scoring conditions together. Admitted examples and definitions feed student review and teacher checks. Explicit proportion equations additionally support exact conversion, complementary-count and error-analysis exercises without another model call. Study guides show editable worked examples and expandable answers; Word exports include a practice answer key. This improves teaching content without presenting the compiler as a trained model or claiming independently validated learning outcomes.

The compiler now selects a shared teaching task before material-specific source rotation. For admitted exact proportions, dated-record comparisons and explicitly sourced confounded experiments, the same inputs, reasoning, answer, errors and four-level scoring criteria drive the existing materials. Task identities remain stable across input edits while content revisions change. Authored tasks and machine-scored quiz configurations are preserved. This is a bounded source-operation compiler, not a trained specialist model. The [third output review](benchmarks/classroom/v1/TASK-PROGRESSION.zh-CN.md) records lesson-specific source routing, linked diagnosis/repair tasks, syllabus consistency and a fix that preserves source facts during single-lesson regeneration. The same five inputs now pass all 295 probes. Manual review also found defects those probes missed; targeted regression tests cover them. The earlier [shared-task review](benchmarks/classroom/v1/SHARED-TASKS.zh-CN.md) remains as the historical baseline.

## Run locally

The [classroom output benchmark](benchmarks/classroom/v1/README.md) evaluates all ten materials independently of the product grader. It replays five frozen inputs without model calls and includes source-derived reference answers, contrasting learner responses, corruption tests, and a [completed educational review](benchmarks/classroom/v1/REVIEW.zh-CN.md). Run `npm run benchmark:outputs` for saved artifacts and defect reports; `npm run benchmark:outputs:test` checks that the evaluator detects deliberate defects. `--strict` currently passes the five-case corpus; educational weaknesses and untested domains remain. Passing software checks does not certify classroom readiness.

The frozen v3 corpus has 36 development and 24 reserved inputs. Run `npm run benchmark:v3:probe -- --out NEW_DIRECTORY` to capture the development inputs serially through the production compiler. This diagnostic supplies original requests and source records without Scion or reviewed bindings; it is not the complete natural-language acceptance path. It preserves each output and hashes, reports missing shared tasks, and leaves educational and export judgments pending. The first run formed no shared task in any of the 36 inputs, despite material text being present. Reserved cases remain unused for product diagnosis.

Use Node.js 22 or later:

```sh
npm ci
npm run dev
```

```sh
npm run check
npm run test:e2e
npm run test:production # Uses dist from npm run check/build; verifies the deployed CSP and download recovery.
npm run format:check
```

The compatibility suite exercises the restored material views, editing/sync contracts and exports. Browser tests run with **one Chromium worker** to keep machine load bounded. Synthetic test courses verify software behavior, not educational effectiveness. `npm run test:scion` separately covers the production runtime, cancellation queue, contract validation, evidence preservation and local-only policy and dormant hosted transport contracts.

## Scion and current limits

**Scion currently runs locally. The shared free online API is temporarily paused because its allowance cannot reliably serve visitors.** The online option is removed, saved online selections migrate to local Scion, and the Cloudflare relay rejects new health/completion requests before touching quota storage or Google. No paid fallback is enabled.

Local Scion uses pinned Gemma 4 E2B weights on compatible devices. First use downloads approximately 3.35 GB. Model downloads and optional source research still need a network connection. Some source-ledger operations use the deterministic evidence compiler with zero model calls; receipts distinguish those operations from inference. No new adapter has been trained or promoted. Reviewed pooled-proportion proposals use bounded reasoning for group identification and short constrained extraction for other fields. A recorded English development case improves, at increased latency; broader model acceptance remains pending.

The ten materials, editors, sync and exports retain the 0.18.7 interface. An automatic review after a single material regeneration performs deterministic checks without starting unrelated model retries. Explicit generation and Finish package actions retain their bounded repair paths.

Explicit `Source facts:` are preserved, including decimals and later limitations. For a source that explicitly supplies a fraction = decimal = percentage equation, the compiler checks both equalities exactly before producing a worked calculation shared by study guides, teacher plans and other compatible teaching surfaces. This verifies that arithmetic only, not the underlying observations or the effectiveness of the lesson. Unsupported or rounded equalities are not promoted by this check.

The dormant transport remains in `server/scion/` for a future explicit relaunch. `HOSTED_ENABLED` defaults closed and the deployed setting is `false`; the browser's `SCION_HOSTED_ENABLED` policy is also false. Existing limits, encrypted credentials and stored projects are retained.

The [September 5 production-pipeline audit](docs/scion-quality-2026-09-05.zh-CN.md) records live model calls, exported samples, fixes and remaining limits. Recent real-course audits found substantive weaknesses including unsupported source inferences, repeated practice and solved examples that reveal later answers. Generated material requires instructor review. Do not treat automatic checks or a model's self-review as independent expert validation.

## Development and deployment

- `src/screens/`, `src/components/`, `src/hooks/`, `src/model/`, `src/lib/`: restored application and its existing course pipeline.
- `src/studio/`: isolated experimental authoring and export research.
- `server/scion/`: paused shared free inference gateway and its tests.
- `research/scion/`: adapter training/conversion experiments, outside the website runtime.
- `tests/workspace-mobile.spec.js`, `tests/export-smoke.spec.js`: original browser regression coverage.
- `docs/interface-restoration.zh-CN.md`: restoration scope, source baseline and verification notes.

GitHub Actions tests the commit before GitHub Pages deploys it. The public [`release.json`](https://edutool.dev/release.json) reports the actual deployed commit and interface baseline. See [CHANGELOG.md](CHANGELOG.md) for the experimental candidate and subsequent restoration.

The restoration source is commit `27513a835c5fc9a6bd4a2d98813a04a8afbc55d4`. The experimental Studio checkpoint is `f64f6c62`; its deployed candidate was `d79ebe6f`. The previous implementation and research remain recoverable in Git history. Model weights and local audit outputs are not included in website commits.
