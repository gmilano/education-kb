# marimo-grader

**Documentation:** https://marimograder.org/ — including a
[live demo assignment](https://marimograder.org/demo/try-an-assignment/) that runs in the browser.

The documentation and the [DartBrains](https://dartbrains.org) course book are built with
[marimo-book](https://marimobook.org) ([source](https://github.com/ljchang/marimo-book)), which
publishes student notebooks as course pages that link back to the grader.

A multi-tenant, FERPA-appropriate grading service for [marimo](https://marimo.io) assignments.
Students open a notebook (MoLab, WASM, or a local kernel), sign in with Dartmouth SSO from
inside the notebook, and click **Submit**. Instructors and TAs grade in a web app. Grades export
to Canvas.

The design document is in [`docs/design.html`](docs/design.html); the API contract is in
[`docs/api.md`](docs/api.md). Deployment lives on the site:
[Overview](https://marimograder.org/operators/overview/) and
[Deploy](https://marimograder.org/operators/deploy/).

```
backend/   FastAPI service + worker  (Python, PostgreSQL, SQLAlchemy 2, Alembic, python3-saml)
frontend/  Instructor, TA and student UI  (Svelte 5 runes, TypeScript, Vite)
client/    marimo-grader-client: the anywidget students see in the notebook  (Python, anywidget)
deploy/    Caddy image, droplet bootstrap/deploy scripts, DigitalOcean runbook
docs/      design document and API contract
```

## How it fits together

* **Identity.** Browsers sign in through Dartmouth SAML (Shibboleth + Duo) and get an HttpOnly
  session cookie. Notebooks never see credentials: the widget starts a device-style handshake,
  the student approves it in a browser tab, and the notebook receives an 8-hour token bound to
  their NetID.
* **Submissions are immutable.** Every Submit stores the whole notebook as a content-addressed
  artifact and records an attempt for one question. The worker autogrades with
  [MoGrader](https://github.com/jameskermode/mograder)'s engine (used as a library, not as a
  server) and renders the notebook to HTML for the grading view.
* **Authorization is per offering.** Roles (student, TA, instructor) live on enrollments. Every
  route resolves the caller's enrollment first. Platform admins manage courses but cannot read
  student work.
* **Audit.** Grade, roster, settings, and export actions append to `grade_audit`.

## Local development

Requirements: `uv`, `pnpm`, Docker (for PostgreSQL only; the test suite runs on SQLite).

```bash
cp .env.example .env                      # dev defaults: GRADER_AUTH_MODE=dev
docker compose up -d postgres

cd backend
uv sync --all-extras
uv run alembic upgrade head
uv run grader seed                        # course + offering, instructor "prof", two students
uv run grader-api                         # http://localhost:8000  (docs at /api/docs)

cd ../frontend
pnpm install && pnpm dev                  # http://localhost:5173, proxies /api to :8000
```

Sign in during development at `http://localhost:8000/api/v1/auth/dev-login?netid=prof`
(any NetID works; `prof` is the seeded instructor and platform admin).

Run the worker in a second terminal (needs the `worker` extra, which installs mograder and marimo):

```bash
cd backend && uv run grader-worker
```

### Tests

```bash
cd backend && uv run pytest && uv run ruff check src tests
cd frontend && pnpm check && pnpm build
cd client && uv run pytest
```

## Publishing an assignment

Write one marimo notebook with MoGrader markers (`### BEGIN SOLUTION`, `### BEGIN HIDDEN TESTS`,
a `_marks = {...}` cell, and `check("glm-q01: Load the data", [...])` calls). Then:

```bash
cd backend
uv run grader publish path/to/glm.py --server http://localhost:8000 \
    --offering <offering-id> --slug glm --title "GLM" --manual glm-q05
```

The command signs you in through the device handshake, generates the student version, uploads
both, and writes `glm_student.py` with the server, offering, assignment, and version ids embedded
in its PEP 723 block. That file is what dartbrains.org links to. Inside it, the assignment cells
use `marimo-grader-client`:

```python
from marimo_grader_client import Grader
g = Grader()                 # reads server/ids from the notebook's PEP 723 block
g.signin_button()
g.check("glm-q01: Load the data", [(bold.shape[0] == 128, "Expected 128 volumes")])
g.submit_button("glm-q01")
```

## Production

Production runs on one DigitalOcean droplet (Docker Compose: API, worker, Caddy) plus
DigitalOcean Managed PostgreSQL. Images are built by GitHub Actions and pulled from GHCR;
nothing is built on the server. The step-by-step runbook, including secret generation, SAML
registration, backups, and staging vs. production settings, is in
[`deploy/README.md`](deploy/README.md).

### Deploying to DigitalOcean

```bash
# once, on a fresh Ubuntu 24.04 droplet
ssh root@<droplet-ip> 'bash -s' < deploy/bootstrap.sh

# each release, as the deploy user in /srv/grader (holds docker-compose.prod.yml + .env)
./deploy.sh            # or ./deploy.sh sha-<short> / ./deploy.sh v0.2.0
curl -fsS https://grader.dartbrains.org/api/health
```

Before the first deploy: set every secret in `.env` (`GRADER_ENV=prod` refuses to start
otherwise), register the SP with Dartmouth IT (metadata at `/api/v1/auth/saml/metadata`), and
submit the deployment for Dartmouth's security and privacy review (design §13).

`docker compose up -d --build` still brings up the same shape locally (with a local PostgreSQL)
for testing the containers before pushing.

## Status

Phase 1 skeleton (see design §16). Done: schema and migrations, SAML SP and dev login, device
handshake and notebook tokens, immutable submissions, worker with MoGrader integration, triage
and grid endpoints, manual scoring with audit, roster import from Canvas CSV and Banner files,
Canvas gradebook export, the Svelte UI, and the notebook widget. Open spikes from the design
document (§15) still apply, most importantly a live test against the Dartmouth IdP and the
device handshake from a MoLab notebook.

## Acknowledgements

The grading engine is [MoGrader](https://github.com/jameskermode/mograder) by James Kermode
(University of Warwick, MIT license): its authoring markers, `check()` runtime, cell-hash
integrity check, hidden-test reinjection, and sandboxed runner do the actual autograding here.
marimo-grader uses it as a library and contributes fixes upstream rather than forking it.
See [The grading engine](https://marimograder.org/how-it-works/grading-engine/) for what is used
and the behaviours worth knowing. The documentation and the DartBrains course book are built with
[marimo-book](https://marimobook.org), and the whole system exists because of
[marimo](https://marimo.io).

MIT.
