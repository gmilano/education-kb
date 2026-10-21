# MathTrail Canvas

[![CI](https://github.com/MathTrail/canvas-api/actions/workflows/ci.yml/badge.svg)](https://github.com/MathTrail/canvas-api/actions/workflows/ci.yml)
[![CodeQL](https://github.com/MathTrail/canvas-api/actions/workflows/codeql.yml/badge.svg)](https://github.com/MathTrail/canvas-api/actions/workflows/codeql.yml)
[![Release and deploy](https://github.com/MathTrail/canvas-api/actions/workflows/release.yml/badge.svg)](https://github.com/MathTrail/canvas-api/actions/workflows/release.yml)
[![Release](https://img.shields.io/github/v/release/MathTrail/canvas-api)](https://github.com/MathTrail/canvas-api/releases/latest)
[![Go Version](https://img.shields.io/github/go-mod/go-version/MathTrail/canvas-api)](https://github.com/MathTrail/canvas-api/blob/main/go.mod)
[![codecov](https://codecov.io/gh/MathTrail/canvas-api/branch/main/graph/badge.svg)](https://codecov.io/gh/MathTrail/canvas-api)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/15460/badge)](https://www.bestpractices.dev/projects/15460)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/MathTrail/canvas-api/badge)](https://scorecard.dev/viewer/?uri=github.com/MathTrail/canvas-api)
[![License: MIT](https://img.shields.io/github/license/MathTrail/canvas-api)](LICENSE)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=MathTrail_canvas-api&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=MathTrail_canvas-api)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=MathTrail_canvas-api&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=MathTrail_canvas-api)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=MathTrail_canvas-api&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MathTrail_canvas-api)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MathTrail_canvas-api&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MathTrail_canvas-api)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=MathTrail_canvas-api&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=MathTrail_canvas-api)

MathTrail Canvas is a math tutor for children in grades 1–6. A child solves a task by hand, with a stylus or a finger, anywhere on a squared sheet and writes the final answer on the same sheet — there is no separate answer box. On **Send Answer**, one AI call reads the whole sheet: it finds the final answer, follows the reasoning and finds the first mistake. A program, not the AI, compares the answer with the task's key. When the answer is wrong, the tutor frames the place where the reasoning went wrong and asks one short guiding question. It never gives the answer.

![The task screen on a tablet, as the design draws it](docs/design/app.png)

The picture is a concept from the design: it shows where the product is heading, further than the MVP goes.

## Design

Where the design differs from the documents, the documents win.

- [The olympiad coach](https://mathtrail.app/en/coach/) — live on mathtrail.app.

## The MathTrail core

[mathtrail-standalone](https://github.com/MathTrail/mathtrail-standalone) is the core of MathTrail: a free, open-source app for Claude and ChatGPT that turns an adult's own chat into an olympiad maths trainer for grades 1–6, with checked tasks in any language, a diagnosis of the child's mistake and a memory of how they are progressing. Canvas takes its service skeleton, development environment, CI/CD and Terraform, but runs on its own: it shares neither tasks nor data with the core.

## Documents

The documents are in Russian.

- [docs/product.md](docs/product.md) — what we build and why: the scope of the MVP, scenarios, unit economics, metrics and acceptance criteria.
- [docs/spec.md](docs/spec.md) — how it is built: architecture, the sheet and the check images, the answer check, the draft analysis, the AI tutor, the API, data, security and deployment.
- [docs/privacy.md](docs/privacy.md) — children's data: what is collected and kept, what the external AI service receives, parental consent, deletion and retention.
- [docs/decisions.md](docs/decisions.md) — the decision log: what was decided, why, and what was rejected.
- [docs/self-hosting.md](docs/self-hosting.md) — how it is deployed: the one-time bootstrap, the delivery of every release, rollback and return.
- [docs/stack.html](docs/stack.html) — the technology stack, layer by layer, with versions and what is still to be chosen. Open the file from a checkout in a browser: GitHub shows only its source.
- [RUN.md](RUN.md) — the implementation plan, in epics: the current epic broken into small tasks, run and reviewed one at a time, and the later epics. The done epics, with their tasks, are archived in [docs/plan/](docs/plan/).
