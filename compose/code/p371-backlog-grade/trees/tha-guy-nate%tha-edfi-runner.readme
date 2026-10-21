# tha-edfi-runner

[![CI](https://github.com/tha-guy-nate/tha-edfi-runner/actions/workflows/ci.yml/badge.svg)](https://github.com/tha-guy-nate/tha-edfi-runner/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/tha-guy-nate/tha-edfi-runner/graph/badge.svg)](https://codecov.io/gh/tha-guy-nate/tha-edfi-runner)
[![PyPI](https://img.shields.io/pypi/v/tha-edfi-runner)](https://pypi.org/project/tha-edfi-runner/)
[![Python](https://img.shields.io/pypi/pyversions/tha-edfi-runner)](https://pypi.org/project/tha-edfi-runner/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![wheel size](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Ftha-edfi-runner%2Fjson&label=wheel%20size&query=%24.urls%5B0%5D.size&suffix=%20B)](https://pypi.org/project/tha-edfi-runner/#files)

A Tabular Helper API library that wraps the Ed-Fi ODS REST API with a typed, pipeline-friendly interface.

## Install

```bash
pip install tha-edfi-runner
pip install "tha-edfi-runner[httpx2]"   # optional httpx2 HTTP backend
```

## Quick start

```python
from tha_edfi_runner import ThaEdfiBase, ThaStudentAssessment

# Fetch tokens for each district
base = ThaEdfiBase()
token_rows = base.batch_fetch_tokens(
    district_rows,
    oauth_endpoint="oauth/token",
    account_col="District BK",
)

# POST student assessment payloads
runner = ThaStudentAssessment(api_version="v3")
results = runner.batch_post_payload(
    rows,
    payload_col="payload",
    key_col="Student Assessment BK",
    workers=4,
    commit=True,
)
```

## Auth

Three auth modes are supported — pass exactly one set of credentials:

```python
# OAuth2 client credentials (fetches a token automatically)
ThaEdfiBase(base_url="...", client_id="key", client_secret="secret")

# Pre-fetched bearer token
ThaEdfiBase(base_url="...", bearer_token="eyJ...")

# No auth (valid for ThaEdfiBase construction; _session() will raise)
ThaEdfiBase(base_url="...")
```

By default, `token_url` is derived as `{base_url}/oauth/token`. Override with `token_url=`.

## URL structure

Ed-Fi ODS data endpoints follow the pattern:

```
{base_url}/data/{api_version}/ed-fi/{resource}
```

Pass `api_version` once and the library handles the rest:

```python
runner = ThaStudentAssessment(base_url="https://ods.example.com/api", api_version="v3")
# data calls hit: https://ods.example.com/api/data/v3/ed-fi/studentAssessments
# OAuth token:    https://ods.example.com/api/oauth/token
```

## Multi-district deployments

When each row carries its own URL and token, pass `base_url` and `api_version` at the runner level as defaults, then override per-row via column names:

```python
runner = ThaStudentAssessment(api_version="v3")   # default version
results = runner.batch_get_all(
    rows,
    key_col="District BK",
    url_col="targetUrl",          # per-row ODS base URL
    token_col="EdFi Token",       # per-row bearer token
    api_version_col="apiVersion", # per-row override (takes precedence over "v3")
)
```

## Typical workflow

```python
from tha_edfi_runner import ThaEdfiBase, ThaStudentAssessment
from tha_map_runner import ThaMap

# 1. Fetch tokens for each district
base = ThaEdfiBase()
token_rows = base.batch_fetch_tokens(
    district_rows,
    oauth_endpoint="oauth/token",
    account_col="District BK",
    workers=4,
)

# 2. Enrich district rows with tokens
mapper = ThaMap()
enriched = mapper.enrich_rows(
    district_rows,
    source=token_rows,
    mapping={"EdFi Token": "EdFi Token", "token_expires_at": "token_expires_at"},
    row_key="District BK",
    source_key="District BK",
)

# 3. Fetch all assessments across districts
runner = ThaStudentAssessment(api_version="v3")
flat_assessments = runner.batch_get_all(
    enriched,
    key_col="District BK",
    workers=4,
    show_progress=True,
)

# 4. Join back to original rows
enriched = mapper.expand_rows(
    district_rows,
    source=flat_assessments,
    mapping={"Assessment ID": "id", "Score": "scoreResults.result"},
    row_key="District BK",
    source_key="District BK",
)
```

## API

### `ThaEdfiBase`

```python
ThaEdfiBase(
    *,
    base_url="",
    api_version="",
    client_id=None,
    client_secret=None,
    token_url=None,
    bearer_token=None,
    backend=None,         # "requests" (default) or "httpx2"
    req=None,             # share an existing ThaReq (and its per-thread sessions)
)
```

`backend` picks the HTTP client used for every Ed-Fi and OAuth call, including the
per-row instances the batch methods create. `"requests"` is the default. `"httpx2"`
needs the `[httpx2]` extra and raises `ImportError` with the install command if it
is missing. With `req=`, `backend` can be left out (the req's backend is used);
passing a `backend` that differs from the req's raises `EdfiError`. Only the `requests` backend retries 5xx responses at the transport
level, and only for GET/DELETE (never POST); the `httpx2` backend retries connection
failures only.

#### `base.fetch_token()`

Fetch a token using this instance's OAuth2 credentials. Returns:

```python
{"token": "eyJ...", "status": None, "message": None}           # success
{"token": None, "status": "error", "message": "auth error: HTTP 401"}  # failure
```

#### `base.batch_fetch_tokens()`

```python
base.batch_fetch_tokens(
    rows,
    *,
    oauth_endpoint,                    # e.g. "oauth/token"
    account_col,                       # deduplication key
    workers=1,
    show_progress=False,
    progress_desc=None,        # step prefix, e.g. "[4/7]" -> "[4/7]: <text>"
    label=None,                # replaces the default progress text
    skip_statuses=["error", "warning"],
    status_col="row status",
    url_col="targetUrl",
    key_col="oAuthKey",
    secret_col="oAuthSecret",
    token_col="EdFi Token",
    expires_col="token_expires_at",
) -> list[dict]
```

Returns one record per unique `account_col` value with `token_col` and `expires_col` set. Results stored in `base.rows`.

---

### `ThaStudentAssessment`

Inherits `ThaEdfiBase`. Default endpoint: `ed-fi/studentAssessments`.

#### Single methods

```python
runner.post_payload(payload, *, key, endpoint=..., commit=False,
                    retry_statuses=None, retry_messages=None, max_retries=2,
                    retry_backoff=1.0,
                    allow_statuses=None) -> dict
# {"key": ..., "status": None | "error" | "dry_run" | <allowed>, "message": ...,
#  "http_status": int | None, "correlation_id": str | None}

runner.get_by_id(resource_id, *, endpoint=...) -> dict
# {"id": ..., "status": None | "error", "message": ..., "data": dict | None,
#  "http_status": int | None, "correlation_id": str | None}

runner.get_all(*, key, endpoint=..., params=None, limit=500, show_progress=False) -> dict
# {"key": ..., "status": None | "error", "message": ..., "data": [dict, ...],
#  "correlation_id": str | None}

runner.delete_by_id(resource_id, *, key, endpoint=..., commit=False) -> dict
# {"id": ..., "key": ..., "status": "deleted" | "error" | "dry_run", "message": ...,
#  "http_status": int | None, "correlation_id": str | None}

# http_status is the HTTP status code of the Ed-Fi response (e.g. 201, 409, 401),
# or None for client-side failures (dry run, invalid JSON, missing column).
# correlation_id is the Ed-Fi correlation id of an error response (the body's
# "correlationId", else a correlation-id header) and None otherwise. Quote it to
# the ODS host to find the request in their logs.
```

#### Retrying and allowing error statuses (opt-in)

`post_payload` and `batch_post_payload` treat every non-2xx response as `"error"`
and never retry it unless you opt in:

```python
runner.batch_post_payload(
    rows,
    payload_col="payload",
    key_col="District BK",
    commit=True,
    retry_statuses={400},                      # re-POST on these codes...
    retry_messages=["unable to resolve"],      # ...only when the message matches
    max_retries=2,                             # ...up to 2 more times
    retry_backoff=1.0,                         # sleeping 1s, 2s, 4s, ...
    allow_statuses={400: "warning", 409: None},  # non-retried code -> row status
)
```

- `retry_messages`: optional case-insensitive substrings. When set, a listed code
  is retried only if the Ed-Fi message contains one of them, so a payload error
  like `"... is required"` fails right away instead of being retried.
- `retry_statuses`: HTTP codes to re-POST on. `401` isn't allowed here; use
  re-auth (below) instead. After `max_retries` the result
  is final. Success gives `status=None, message=None`; anything else gives
  `"error"`, with the correlation id and retries attempted in the message, e.g.
  `"HTTP 400 Bad Request: <Ed-Fi detail> (correlation id: <id>; retries attempted: 2)"`.
- `allow_statuses`: maps an HTTP code to the row status it gets in place of
  `"error"`. It applies only to errors that weren't retried; a retry that never
  succeeds always ends as `"error"`. The Ed-Fi detail and `correlation_id` stay
  on the result. Codes not in the map stay `"error"`, and so do client-side
  failures such as invalid JSON.

All write methods require `commit=True` to execute — otherwise return `status="dry_run"`.

#### Batch methods

All batch methods share these common parameters:

```python
rows,
*,
endpoint=...,
workers=1,
show_progress=False,
progress_desc=None,        # step prefix, e.g. "[4/7]" -> "[4/7]: <text>"
label=None,                # replaces the default progress text
skip_statuses=["error", "warning"],
status_col="row status",
url_col="targetUrl",
token_col="EdFi Token",
api_version_col=None,           # column holding per-row ODS version (overrides runner api_version)
auth_key_col=None,              # enable reactive re-auth on 401
auth_secret_col=None,
oauth_endpoint=None,
expires_col=None,               # enable proactive re-auth before token expiry
refresh_cooldown=30.0,          # seconds refreshes pause after 3 failures; 0 = never pause
row_id_col=None,                # column echoed onto each result as `row_id`
```

Method-specific required params:

```python
runner.batch_post_payload(rows, *, payload_col, key_col, ..., commit=False) -> list[dict]
runner.batch_get_by_id(rows, *, id_col, ...) -> list[dict]
runner.batch_get_all(rows, *, key_col, ...) -> list[dict]   # flat list; inject key_col into each record
runner.batch_delete_by_id(rows, *, id_col, key_col, ..., commit=False) -> list[dict]
```

Results stored in `runner.rows`.

`batch_post_payload`, `batch_get_by_id`, and `batch_delete_by_id` add these fields to
each result dict:

- `row_index` — the row's position in the `rows` you passed in, unchanged by rows
  dropped via `skip_statuses`. A position-based correlation key for
  `ThaMap.enrich_rows` when the business key repeats across a batch.
- `row_id` — the value of `row_id_col` for that row, copied through verbatim (a
  caller-owned identity assigned upstream, e.g. at CSV read). `None` on every
  result unless you pass `row_id_col`. Prefer this over `row_index` when you have a
  stable id; `row_index` is the fallback.
- `http_status`, `correlation_id`: see the single-method note above.

### Re-auth

Provide `auth_key_col`, `auth_secret_col`, and `oauth_endpoint` to enable automatic token refresh:

- **Proactive**: if `expires_col` is set and the token has expired, a fresh token is
  fetched before the call. The expiry can be a number or a numeric string (e.g. after a
  CSV round trip).
- **Reactive**: if a call returns 401, the token is refreshed once and the call retried.

A refreshed token is shared by every row and worker in the batch call, keyed by
`(base_url, client id)`. One refresh serves the whole batch instead of one per row,
and when several workers hit an expired token at once, only one token request is made.
Rows after a refresh use the new token directly.

Refresh failures show up in the row message:

- `"auth refresh failed: <reason>"`: the row's token had expired or already got a 401
  in this batch, and the refresh failed, so the call was not sent with that token.
  These rows have `http_status=None`, like other failures that never reach Ed-Fi.
- `"auth error: HTTP 401; auth refresh failed: <reason>"`: a 401 and the refresh after
  it both failed.
- `"auth error: HTTP 401 (re-auth not possible: empty 'oAuthKey')"`: re-auth is
  configured, but this row is missing what it needs (or a setting like
  `oauth_endpoint` isn't set).

Failed refreshes for a client back off (1s, then 2s). After 3 failures in a row,
refreshes for that client pause for `refresh_cooldown` seconds (30 by default):

- **First pause:** rows wait it out instead of failing, then one refresh is tried. If it
  works, the batch carries on with the new token, so a short throttle delays the batch
  without losing rows.
- **If that refresh fails too**, the problem isn't a short throttle. From then on, rows
  for that client fail fast during each pause with
  `(refresh paused <n>s after <n> failed refreshes)`, and one refresh is tried after
  each pause. Rerun those rows once the token endpoint or credentials are fixed.
- **`refresh_cooldown=0`** never pauses: every row after the third failure tries its own
  refresh, so the batch keeps going without waiting but can hit the token endpoint once
  per row while it's failing. A longer value waits longer before the next attempt.

A refreshed token that Ed-Fi rejects with a 401 counts as a failed refresh, so
credentials that get unusable tokens hit the same limit. The count resets once Ed-Fi
accepts a refreshed token. A 401 that isn't about expiry (Ed-Fi refusing the client's
tokens) therefore costs one token request per pause before rows fail fast. Ed-Fi
normally answers a missing permission with 403, which doesn't trigger re-auth.

The refreshed token lives only inside that batch call. The `token_col` values in your
rows aren't updated, so if you keep tokens elsewhere, fetch a new one for the next run
(e.g. with `batch_fetch_tokens`).

Each batch call uses one HTTP session per worker thread, shared across rows, and closes
them when the call returns.

## Alternatives

- [**requests**](https://docs.python-requests.org) — HTTP client underlying this library; use directly for full control
- [**edfi-client**](https://pypi.org/project/edfi-client/) — Ed-Fi-specific client with broader resource coverage

Choose this library when you're already working in the `tha-*` row-dict pipeline and want Ed-Fi batch operations to follow the same conventions (skip_statuses, commit flag, self.rows, per-row credentials).

## License

MIT
