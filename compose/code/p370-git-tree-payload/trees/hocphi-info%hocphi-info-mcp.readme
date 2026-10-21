# hocphi-info-mcp

Public, **read-only** [MCP](https://modelcontextprotocol.io) server for
[hocphi.info](https://hocphi.info) — Vietnamese university tuition data with sources.
Lets an AI assistant look up and compare tuition by school and major and get the **same
numbers as the website**, with the academic year and source, instead of guessing.

> **Status: the public Cloud Run service is switched off (2026-10-12) to save money.** The
> code is complete: typed API client, generated models, CI, the seven tools and the HTTP server
> (Streamable HTTP, host/origin checks, rate limiting, JSON logs), plus the Docker image and the
> deploy workflow. But `https://hocphi-info-mcp-722605738307.asia-southeast1.run.app/mcp` no
> longer answers.
>
> **Why:** Cloud Run billed about ₫49k (gross, covered by free-trial credit) in the first 11 days
> of October even though nobody was calling the server. The only requests came from one
> developer's AI client holding a `GET /mcp` stream open (about 31 s each, reconnecting), which
> kept an instance alive all day. The free tier does not apply to Tier 2 regions such as
> `asia-southeast1`, so idle-looking traffic still cost money.
>
> **To bring it back:** push a `v*` tag (or run the *Deploy* workflow by hand); it recreates the
> service from the image in Artifact Registry. Before that, consider making `GET /mcp` return
> `405` so clients do not hold streams open. The daily *Smoke* schedule is disabled while the
> service is off; run it manually after redeploying.

## Tools (all read-only)

| Tool | What it does |
|---|---|
| `search_majors` | Find majors by name/alias (`cntt`, `khmt`, diacritics optional); gives school slugs to use next. |
| `search_schools` | Find schools with their standard-track year-1 range. |
| `get_major_tuition` | Every program of one major at one school, with source, academic year, projections. |
| `compare_programs` | Compare 2-4 programs; flags missing data and mixed academic years. |
| `estimate_total_cost` | The backend's estimate for the whole course, with the assumptions stated. |
| `explore_major_taxonomy` | Browse the Ministry classification (field → group → major) with data. |
| `find_related_majors` | Other majors in the same Ministry group, for comparison. |

Every amount is per academic year in VND (also in millions). Only `year1` is published by the
school; later years are projections (`is_projected`). Missing data is reported explicitly.

## How it works

The server is a thin client of the public hocphi API (`hocphi-info-be`). It contains **no
tuition rules of its own**: every figure (year 1, projected years, course total, ranges)
is computed by the backend; this repo only fetches, validates, caches and presents them
with their sources. It never touches the database.

```
AI client ──MCP (Streamable HTTP)──▶ hocphi-mcp (Cloud Run) ──HTTPS──▶ hocphi API (Fly) ──▶ Postgres
```

## Run the server

```bash
make dev        # http://localhost:8080/mcp   (PORT=... to change)
claude mcp add --transport http hocphi-local http://localhost:8080/mcp
```

- **Stateless Streamable HTTP** at `/mcp` (`stateless_http`): no session id, so any instance
  can serve any request (no sticky sessions on Cloud Run). Both the legacy (`initialize`) and
  the sessionless 2026-07-28 protocol work; tested end to end against a real uvicorn.
- `GET /healthz` is a cheap liveness probe; it does not call the backend.
- **Public and unauthenticated by design** (read-only data), so the guards matter:
  - `Host` must be in `ALLOWED_HOSTS` (else `421`) and browser `Origin`s are refused (`403`)
    — DNS-rebinding protection; official AI clients call from servers and need no CORS.
  - Body limited to 64 KB (`413`); `Content-Type` must be JSON (`400`).
  - **Per-client rate limit** (token bucket, default 60/min, burst 20 → `429` + `Retry-After`).
    The client is the IP the trusted proxy appended to `X-Forwarded-For` (the left part is
    client-controlled and ignored). Counters live in each instance's memory, so the real limit
    is `instances × limit`: a best-effort guard. The hard cost/abuse ceiling is Cloud Run's
    `--max-instances`. Cloud Armor / Redis were rejected as too costly for a free service.
- Logs are one JSON line each on stdout (Cloud Logging reads `severity` / `message`): a
  `request` line per request (method, path, status, duration, hashed client, request id),
  a `tool_call` line per tool call (tool, duration, result count, error code) and library
  logs, all sharing `request_id` (and `logging.googleapis.com/trace` when `GCP_PROJECT` is
  set). Raw IPs are never logged.

## Docker

```bash
docker build -t hocphi-mcp .
docker run --rm -p 8080:8080 -e ALLOWED_HOSTS="localhost:*,127.0.0.1:*" hocphi-mcp
uv run python scripts/smoke_mcp.py http://localhost:8080/mcp --call   # lists the 7 tools, calls one
```

Multi-stage image (uv build stage → slim runtime), runs as a non-root user, honors `$PORT`
(Cloud Run) and stops cleanly on `SIGTERM`. In production set `ALLOWED_HOSTS` to the Cloud Run
host and `GCP_PROJECT` for trace-linked logs. See [`docs/design.md`](docs/design.md) for the
architecture, trade-offs and failure modes.

## Develop

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 for you).

```bash
make install     # uv sync
make check       # ruff + mypy + generated-models check + pytest (same as CI)
make gen-models  # regenerate src/hocphi_mcp/api_models.py from the backend OpenAPI
uv run python scripts/smoke_real_api.py   # call the real API through the client
```

- `src/hocphi_mcp/api_models.py` is **generated** from the backend's `openapi.json`
  (`main` of `hocphi-info-be`); never edit it by hand. Set `OPENAPI_SRC=../hocphi-info-be/openapi.json`
  to develop against a local backend spec. CI regenerates it and fails on any diff. There is no
  scheduled run: after a backend contract change, run `make gen-models` here.
- Configuration is via environment variables (see `.env.example`); defaults are production-ready.
- By default the client calls the Fly origin (`https://hocphi-info-api.fly.dev`) rather than
  `api.hocphi.info`: the latter is behind Cloudflare, which blocks some User-Agents, and
  server-to-server traffic does not need that layer.

## License / data

Tuition figures come from public school announcements; each one carries its source URL.
Treat them as reference values and confirm on the school's website.
