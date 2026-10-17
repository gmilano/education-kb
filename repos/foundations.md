---
industry: education
region: Global
updated: 2026-10-17
---

# Foundational repos — Education

> The layer below the agents: platforms, standards, assessment engines and learner-model
> libraries that an engagement builds *on* rather than *with*. Licences read first-hand from
> each repository's `LICENSE` payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)

## Permissive foundations (MIT / Apache-2.0 / BSD)

| Repo | Licence | Stars | Why it is a foundation |
|------|---------|-------|------------------------|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | **Interactive learning with automated feedback**, from TUM Applied Education Technologies. Programming, quiz, modelling and text exercises with automatic assessment and an integrated CI runner. The strongest MIT-licensed teaching platform found this pass — production-grade and university-maintained. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | 4.1k | FSRS, the modern spaced-repetition scheduler. The highest-adoption learning-science component in open source. Pair with [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) (BSD-3-Clause) for a Rust core you can embed. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 450 | The reference PyTorch knowledge-tracing benchmark library: standard datasets, standard splits, comparable baselines. If a client asks "can you predict what this student knows", this is the honest starting point. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT | 352 | Source-code plagiarism detection (UGent). In the GenAI era this is no longer a niche: it is the integrity layer every coding course now needs. |
| [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | Apache-2.0 | 313 | Education datasets plus download/preprocess tooling. Removes the first two weeks of any learner-modelling project. |
| [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT | 82 | Knowledge tracing **plus** cognitive diagnosis **plus** exercise recommendation in one library. Broader than pyKT where the deliverable is a recommender, not a predictor. |
| [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) | MIT | 78 | Unified library for student cognitive modelling, with a configuration-driven pipeline. Good for sweeping many models when the client wants a comparison, not a bet. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | Apache-2.0 | — | Maths and science e-assessment: randomised questions, algebraic marking, SCORM-packaged output. Apache-2.0 makes it embeddable in a commercial deliverable. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | — | Framework for building **LTI** tools that plug into any compliant LMS. The sanctioned way to put an AI tool inside Moodle/Canvas/Open edX without forking the LMS. |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | — | The xAPI (Experience API) specification itself. The vocabulary for "what did this learner actually do" across systems. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | — | SQL-backed **Learning Record Store** for xAPI. The missing piece between an agent that observes learning and a model that needs training data. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | — | Modern SCORM 1.2 / 2004 and AICC runtime. Most institutional content is still SCORM; this is how an agentic front end keeps reading it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | MOOC portal CMS (Django + React) from France Université Numérique. MIT means the client's catalogue front end is genuinely theirs. |
| [openfun/marsha](https://github.com/openfun/marsha) | MIT | — | Video management for education, same FUN-MOOC provenance. The companion to Richie when the course is video-first. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | MIT | — | Student information system (Laravel): enrolment, attendance, results. MIT SIS data is the input every dropout-prediction model needs. |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | Apache-2.0 | — | HAX authoring/CMS for web-component-based course content. Content as components survives an LMS migration; content as LMS pages does not. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 *(README-stated — see note)* | — | The component API for Open edX. The entry point for putting an agent inside an Open edX course. |

**17 permissive foundation rows.**

> **Note on XBlock:** the repository's `README.rst` states *"The code in this repository is
> licensed the Apache 2.0 license unless otherwise"* and points at `LICENSE.txt`, but that
> path did not serve a payload on the raw paths tried this pass. The licence is therefore
> **README-stated, not payload-read** — the weakest evidence grade in this file, and marked
> as such rather than quietly promoted.

## Copyleft foundations — real, but priced

| Repo | Licence | Why you still care |
|------|---------|--------------------|
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(in `COPYING.txt`, not `LICENSE`)* | The world's most deployed LMS and the largest plugin ecosystem in education. GPL is survivable because the integration point is a plugin boundary. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | MOOC-grade platform behind edX. **This base previously published Apache-2.0 for this repo — that was wrong, and the error mattered**: AGPL's network clause is exactly the kind of obligation a hosted-deployment engagement must price in from day one. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 *(prior cell said GPL-2.0)* | Lightweight LMS with deep LATAM public-sector deployment. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | The institutional LMS of the German-speaking EMEA market. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | School management / SIS. Attendance and behaviour data — the signal dropout models actually run on. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | K-12 student information system, light footprint, widely self-hosted. |
| [Vacademy-io/vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Modern e-learning platform with assessment management. AGPL network clause applies. |

## What to reach for, by job

- **"Put an AI tutor inside our existing LMS"** → `tsugi` (LTI) or `openedx/XBlock`. Do not fork the LMS.
- **"Automatically assess student work"** → `Artemis` for programming and modelling, `Numbas` for maths.
- **"Tell us which students are at risk"** → `academico` or `GibbonEdu` for the data, `pykt-toolkit` or `pyedmine` for the model, `lrsql` + `xAPI-Spec` for the event stream.
- **"Make retention stick"** → `fsrs4anki` / `fsrs-rs`. Spaced repetition is the one intervention with a scheduler worth reusing instead of inventing.
- **"We must prove academic integrity"** → `dolos`.
- **"Our content is all SCORM"** → `scorm-again`, and keep the content where it is.

## Declared gaps

- **No permissive full-stack LMS in the top tier.** The only Apache-2.0 complete LMS found
  this pass is **OpenOLAT** (see [`verticals/solutions.md`](../verticals/solutions.md));
  everything else at LMS scale is GPL or AGPL. A client requiring a permissive LMS core has
  exactly one candidate, and that is a finding, not an omission.
- **Star counts marked `—`** were not re-verified this pass; the licence was. An unverified
  number is left blank rather than carried forward from a prior pass, because carried-forward
  numbers are how this base previously published "pykt 1.2k" for a 450-star repository.
- **No LATAM-maintained foundational repo identified.** Chamilo has the deepest LATAM
  public-sector footprint of any platform here, but it is European-maintained (Belgium/Spain).
  The region consumes this layer; it does not yet publish it.
