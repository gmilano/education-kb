<p align="center">
  <img src="docs/canvas-mcp-header.png" alt="Canvas MCP — AI tools for Canvas LMS" width="800">
</p>

# Canvas MCP Server

<!--mcp-name: io.github.vishalsachdev/canvas-mcp-->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A local MCP server for reading Canvas courses, assignments, submissions and grades,
with separately enabled educator and student actions. This is the SDM fork of
[Vishal Sachdev's Canvas MCP](https://github.com/vishalsachdev/canvas-mcp).
Available tools depend on Canvas permissions, role, operator allowlists and feature
flags. The main MCP server, local gradebook worker and course mirror are separate
interfaces.

## Current goals

The grading direction is **dual intake**—Canvas submissions and teacher-folder or
paper evidence—and **paired score and feedback outputs** from the same saved
evidence/result revision. Local tools inspect, reconcile and stage proposals for
teacher review before the central gradebook's EDIT workflow and separately
authorized Canvas delivery.

The authenticated Unit 1 teacher-decision-to-EDIT route is source-accepted and
has a completed local canary. Ordinary participation drafts are qualified as a
local overlay pending portable source publication; they remain UNAPPROVED and
use score-only delivery with private analysis. Broader rollout, teacher approval
and Canvas delivery retain their own gates and independent readback. Read
[goals and status](docs/goals-and-status.md) for current priorities. LocalGrAss
owns shared review tools; Canvas owns observations, publisher gates and installed
Canvas bindings.

| Task | Start here |
| --- | --- |
| Read Canvas or use enabled MCP tools | [Installation](docs/installation.md), [tool guide](tools/README.md) |
| Refresh/compare gradebook GET and EDIT | [Gradebook workflow](docs/sdm-gradebook-workflow.md), [worker](docs/sdm-gradebook-worker.md) |
| Archive and inspect course content | [GET-only course mirror](docs/course-mirror.md) |
| Author assignments, rubrics and modules | [Authoring workflow](docs/sdm-canvas-authoring-workflow.md) |
| Understand review/publisher ownership | [Workflow integration](docs/grass-workflow-integration.md) |

## Installation

<a id="local-installation"></a>
<a id="quick-start"></a>

Use Python 3.11+ and a Canvas token issued under your institution's policy.
For a source checkout:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
cp env.template .env
```

Set `CANVAS_API_URL` to your institution's HTTPS URL ending in `/api/v1` and
`CANVAS_API_TOKEN` to your token in the private `.env`. Then configure your MCP
client to launch the absolute `.venv/bin/canvas-mcp-server` path from this checkout.
[Installation and client examples](docs/installation.md) cover manual setup,
packaged desktop extensions, authentication and verification. Local gradebook
and authoring connections require their own setup; this command does not install
them.

<a id="verification"></a>

`canvas-mcp-server --test` checks the Canvas connection; `--config` displays
configuration. Do not include tokens or student records in a support report.

## Tools and workflows

<a id="available-tools"></a>
<a id="for-ai-agents"></a>

Students can inspect their own work; educators can inspect course work and use
explicitly enabled grading/content tools. Learning-design tools cover course
structure and accessibility. Use the [tool reference](tools/README.md) for exact
contracts and [AGENTS.md](AGENTS.md) for agent rules. The
[machine manifest](tools/TOOL_MANIFEST.json) describes the main server, excluding
the separate gradebook server.

`search_canvas_tools` discovers registered MCP tools and TypeScript operations.
Its schema version 2 response separates `mcp_tools` from `code_execution_api`.
An absent write tool is an operator boundary; confirmation tokens bind requests
and do not establish human approval.

<a id="-agent-skills"></a>

The eight maintained [agent workflows](skills/) are optional recipes on top of
an installed MCP connection. They do not enable disabled tools or grant action
authority. Upstream distributes them through `npx skills add vishalsachdev/canvas-mcp`.

## Privacy and writes

<a id="security"></a>
<a id="-privacy--data-protection"></a>

Keep credentials, original student evidence, PIN crosswalks, journals and backups
outside Git and the public website root. Optional `ENABLE_DATA_ANONYMIZATION=true`
reduces supported identity fields sent to an AI client; Canvas and the client's
own data policies still apply. Private local student copies use the registry-bound
four-digit text PIN from `Student Info`, preserving leading zeros and holding
unmatched/conflicting identities. See the [PIN policy](docs/STUDENT-PIN-POLICY.md).

`ALLOWED_WRITE_TOOLS` governs the main server's side-effect tools. HTTP is
read-only when it is unset; stdio retains its configured tools. Writes require
explicit human authorization and each tool's preview/readback contract. Scores
and feedback have separate delivery evidence. Never replay an uncertain comment
send.

<a id="code-execution-api"></a>

`execute_typescript` is disabled by default. Enabling it exposes privileged Canvas
credentials and can bypass confirmation and content-fencing guarantees. Each run
requires authorization for its intended effects; a dry run or local sandbox is
not approval. See the [code API guide](src/canvas_mcp/code_api/README.md).

<a id="hosted-server-retired"></a>

The public hosted endpoint is retired. Use local mode or an authenticated
self-hosted deployment; see [HTTP deployment guidance](deploy/azure/).

## Development and history

<a id="documentation"></a>
<a id="sdm-repository-maintenance"></a>
<a id="publishing"></a>

The [documentation map](docs/documentation-map.md) identifies current guides.
The [annotated technical manual](ANNOTATED_TECHNICAL_MANUAL.md) maps key functions,
callers, state, setup and offline verification.
[CLAUDE.md](CLAUDE.md) contains development and validation rules;
[maintenance](docs/repository-maintenance.md) explains branch ownership, recovery
and installed overlays. Reviewed source, installed behavior, teacher acceptance
and verified delivery are distinct states. A documentation/source merge does not
restart a service, deploy the menu, release a package or send classroom grades.
Tags and deployment/paid-review actions require separate authorization.

Release notes remain in [CHANGELOG.md](CHANGELOG.md); dated audits and design
records remain linked from the current guides. The
[pre-trim README](https://github.com/sirdanielm/canvas-mcp/blob/d0794b247df2b865150c4805d816b9075768ae92/README.md)
retains earlier client examples, contributor credits and release narratives.

## License

[MIT](LICENSE). Created by [Vishal Sachdev](https://github.com/vishalsachdev);
maintained SDM changes are tracked in this fork.
