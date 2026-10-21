# NCCU Moodle MCP

An MCP server that accesses **NCCU Moodle** (`moodle.nccu.edu.tw`) on behalf of a
student. It logs in through the NCCU single-sign-on portal (`i.nccu.edu.tw`) and
exposes Moodle data as MCP tools.

It runs as a **hosted HTTP server**: you (the operator) run one instance, and
everyone else just adds its URL to their MCP client config — no install on their
side.

- **Multi-tenant & stateless** — each call authenticates with the credentials
  passed to it, uses that session for the one call, and discards it. Nothing is
  cached to disk or shared between calls, so concurrent users never interfere.

### Tools
| Tool | Description | WS function |
|------|-------------|-------------|
| `list_courses` | Enrolled courses by semester, each with the user's **role** (student/teacher/…). No `sem` → latest; `sem="1142"` → that term; `sem="all"` → every course. | `core_enrol_get_users_courses` + `core_enrol_get_enrolled_users` (role, ≤5 parallel) |
| `search_courses` | Filter enrolled courses by a keyword (the app's "filter my courses" box) — case-insensitive substring of the name (code / 中文 / English). Searches every term by default; `sem` scopes it. | `core_enrol_get_users_courses` + `core_enrol_get_enrolled_users` (role on matches) |
| `get_course_role` | The user's role in one course (`course_id`): student / teacher / editingteacher / teachingassistant / manager. | `core_enrol_get_enrolled_users` |
| `list_assignments` | Assignments with due dates, **submission status**, and your **role** per course. Only your *student* courses by default (`include_all_role` to add TA/teacher ones). Scope by `sem`, `course_ids`, and/or **due** (`due_from`/`due_to`) or **open** (`opens_from`/`opens_to`) date ranges. | `mod_assign_get_assignments` + `mod_assign_get_submission_status` + `core_enrol_get_enrolled_users` (≤5 parallel) |
| `upcoming_deadlines` | Upcoming due dates/quiz closings within `days` (default 14), each with your **role**; student courses only unless `include_all_role`. | `core_calendar_get_action_events_by_timesort` + `core_enrol_get_enrolled_users` |
| `get_grades` | Your grade items for one course (`course_id`). | `gradereport_user_get_grade_items` |
| `get_course_contents` | Everything the teacher posted in a course (`course_id`), grouped by week/section; empty weeks hidden unless `include_empty`. | `core_course_get_contents` |
| `get_module` | Open one posted item by `cmid` (the id in a `mod/.../view.php?id=` link; `course_id` optional — resolved from the cmid). Returns content by type — file links (browser-openable), page html, label/forum intro, forum discussions, **rich assignment detail** (instructions, attachments, submission, grade & feedback), quiz attempts. | `core_course_get_course_module` + `core_course_get_contents` (+ `mod_assign`/`mod_page`/`mod_forum`/`mod_quiz` by type) |
| `submit_assignment` | Submit (繳交) an assignment's online-text answer by `cmid` or `instance`. **Saves only** — never the irreversible submit-for-grading; usually a save already counts as submitted, else returns `needs_finalize` + the Moodle link for the user to finalize themselves. | `mod_assign_save_submission` (+ `core_course_get_course_module` to resolve cmid) |
| `list_announcements` | Announcement tiles (headers only) for one course or all current-semester courses; paginated. | `mod_forum_get_forums_by_courses` + `mod_forum_get_forum_discussions` |
| `get_announcement` | Read one announcement's thread (posts + replies) by `discussion_id`; paginated. | `mod_forum_get_discussion_posts` |
| `get_notifications` | The notification bell (due reminders, grading, forum posts); reports unread count. | `message_popup_get_popup_notifications` |

Course data comes from Moodle's **mobile Web Services API**, not HTML scraping:
after SSO login, the server obtains a Web Services token the way the Moodle app
does (`admin/tool/mobile/launch.php` → `moodlemobile://token=…`) and calls the
REST API. Semester is the NCCU term code encoded in each course's short name
(e.g. `1151`).

**Nothing about the Moodle instance is hardcoded.** On startup the server fetches
Moodle's login page (via the stable entry `moodle.nccu.edu.tw`) and discovers both
the current backend host (e.g. `moodle45.nccu.edu.tw`) and the NCCU SSO login URL
(which encodes the `MoodleSSOxx.aspx` path) — so if the school moves to a different
instance number, it keeps working. The discovered values are cached in memory for
the process (site-wide config, not per-user state).

---

## Part A — For users (setup guide)

You do **not** clone or install anything. You just add one block to your MCP
client's config: the central server's address plus **your own** NCCU credentials
as headers. The server reads those headers on each request, so every user
connects as themselves.

**Before you start, get these three things:**

1. The **server address** from the operator — e.g. `http://140.119.x.x:3033/mcp`
   or `https://moodle-mcp.example.com/mcp`.
2. Your **NCCU student ID** (e.g. `112703016`).
3. Your **NCCU portal password** (the one you use at <https://i.nccu.edu.tw>).

In every snippet below, replace `SERVER_ADDRESS`, `YOUR_STUDENT_ID`, and
`YOUR_PASSWORD`.

---

### Claude Code

**Option 1 — CLI (easiest).** Run this once; the flag `-s user` makes it
available in every project:

```bash
claude mcp add -s user --transport http nccu-moodle SERVER_ADDRESS \
  -H "X-Moodle-Username: YOUR_STUDENT_ID" \
  -H "X-Moodle-Password: YOUR_PASSWORD"
```

**Option 2 — edit the config file** directly. Create/edit `.mcp.json` in your
project folder (or add this `mcpServers` block to your existing config):

```json
{
  "mcpServers": {
    "nccu-moodle": {
      "type": "http",
      "url": "SERVER_ADDRESS",
      "headers": {
        "X-Moodle-Username": "YOUR_STUDENT_ID",
        "X-Moodle-Password": "YOUR_PASSWORD"
      }
    }
  }
}
```

**Verify:**

```bash
claude mcp list                 # nccu-moodle should be listed
```

Then start Claude Code and run `/mcp` — you should see `nccu-moodle` connected
with the `list_courses` tool.

---

### opencode

opencode is configured by a JSON file (there's no add command for MCP). Edit
one of:

- **Global** (recommended, works everywhere): `~/.config/opencode/opencode.json`
- **Per project**: `opencode.json` in the project root

Add the `mcp` block (merge into the file if it already exists):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "nccu-moodle": {
      "type": "remote",
      "url": "SERVER_ADDRESS",
      "enabled": true,
      "headers": {
        "X-Moodle-Username": "YOUR_STUDENT_ID",
        "X-Moodle-Password": "YOUR_PASSWORD"
      }
    }
  }
}
```

**Verify:** restart opencode; the `list_courses` tool from `nccu-moodle` should
be available to the assistant.

---

### Try it

Ask the assistant, for example:

> *List my Moodle courses this semester.*  ·  *List all my Moodle courses.*
> *What's due this week — and have I submitted it?*  ·  *What was due last week?*
> *Which assignments haven't I submitted yet?*  ·  *Any assignments in 1142?*
> *What are the latest announcements?*  ·  *Open that announcement and read it.*
> *What are my grades in course 18284?*  ·  *Do I have any notifications?*

The assistant picks the right tool and reads your credentials from the headers
you set — so you never type your password into the chat, and **the assistant
never sees or
handles your password** (the tool has no username/password parameters).

---

### Notes & safety

> ⚠️ **Lockout:** NCCU suspends an account for **15 minutes after 5 failed login
> attempts**. Make sure the password in your config is correct.
>
> 🔒 Your password is stored in a local config file and sent to the server on
> each call. Keep that file private, and don't commit a personal `.mcp.json` /
> `opencode.json` containing your password to a shared repository. The operator
> should serve the endpoint over **HTTPS** (see Part B).

**Troubleshooting:**

| Symptom | Fix |
|---------|-----|
| Tool errors with *"Missing credentials…"* | The `headers` block is missing or misspelled. Header names must be exactly `X-Moodle-Username` and `X-Moodle-Password`. |
| *"Moodle login failed…"* | Wrong student ID or password. Fix it in the config (mind the 5-attempt lockout). |
| `list_courses` not showing up | Config not loaded — re-check the file location, valid JSON, and restart the client. For Claude Code, confirm with `claude mcp list`. |
| Connection/timeout errors | Server address wrong or server not reachable. Confirm `SERVER_ADDRESS` with the operator. |

---

## Part B — For the operator (run the server)

This project uses **[uv](https://docs.astral.sh/uv/)** to manage Python and
dependencies.

### 1. Install

```bash
cd /path/to/moodle_mcp
uv sync          # creates .venv and installs from uv.lock
```

(Install uv first if needed: `curl -LsSf https://astral.sh/uv/install.sh | sh`.)

### 2. Run as an HTTP server

```bash
MCP_HOST=0.0.0.0 uv run nccu-moodle-mcp http
```

Endpoint: `http://<host>:3033/mcp` (Streamable HTTP, stateless, JSON responses).
On startup it discovers + caches the Moodle backend and SSO URL, then serves.

Environment variables:

| Var | Default | Purpose |
|-----|---------|---------|
| `MCP_HOST` | `127.0.0.1` | Bind address. Set `0.0.0.0` to accept remote connections. |
| `MCP_PORT` | `3033` | Port. |
| `MCP_ALLOWED_HOSTS` | `*` (any host) | Hostnames allowed in the `Host` header (DNS-rebinding guard). Default `*` accepts any host. To lock down, set specific hostnames (comma-separated) — include the port if clients send one (e.g. `1.2.3.4:3033`). |
| `MOODLE_SSO_URL` | *(auto-discovered)* | The NCCU SSO login URL (`i.nccu.edu.tw/Login.aspx?...`). Normally found automatically from Moodle's login page; set this to skip discovery or pin it. |

> The host check defaults to allowing **any** host. If you set
> `MCP_ALLOWED_HOSTS` to specific names, a request whose `Host` isn't listed is
> rejected with **HTTP 421** — the value must match the `Host` header exactly,
> **including the port** when one is present.

### 3. Put it behind HTTPS (recommended)

Terminate TLS with a reverse proxy and forward to the app on localhost. Example
Caddy config:

```
moodle-mcp.example.com {
    reverse_proxy 127.0.0.1:3033
}
```

Run the app bound to localhost, optionally locking the host to your domain:

```bash
MCP_ALLOWED_HOSTS="moodle-mcp.example.com" uv run nccu-moodle-mcp http
```

(You can also leave `MCP_ALLOWED_HOSTS` at its default `*` when the app port is
only reachable through the proxy.)

### 4. Keep it running

**Docker Compose (recommended).** The repo ships a `Dockerfile` (multi-stage,
uv-based) and `docker-compose.yml` (service `nccucourse`, bind `0.0.0.0:3033`,
`MCP_ALLOWED_HOSTS=*`, restart policy, healthcheck):

```bash
docker compose up -d --build     # build and start
docker compose logs -f           # watch
docker compose down              # stop
```

Override settings via a local `.env` or the shell, e.g. to lock the host down:

```bash
MCP_ALLOWED_HOSTS=moodle-mcp.example.com docker compose up -d
```

**systemd (bare-metal alternative):**

```ini
[Unit]
Description=NCCU Moodle MCP
After=network.target

[Service]
WorkingDirectory=/path/to/moodle_mcp
Environment=MCP_HOST=0.0.0.0
Environment=MCP_PORT=3033
ExecStart=/usr/local/bin/uv run nccu-moodle-mcp http
Restart=always

[Install]
WantedBy=multi-user.target
```

### Smoke test

```bash
curl -s https://moodle-mcp.example.com/mcp -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

---

## Layout

```
src/nccu_moodle_mcp/        the package
├── __init__.py
├── __main__.py             `python -m nccu_moodle_mcp [http]`
├── app.py                  the MCPServer instance, credential handling, tool runner, param types
├── server.py               entry point: imports tools (registers them) and runs the transport
├── moodle_client.py        MoodleClient: SSO login, site discovery, ws() core
├── helpers.py              shared helpers (time / HTML / term-code / semester filter)
└── tools/                  one module per tool — logic + its own @mcp.tool (+ tool-specific helpers)
    ├── courses.py          list_courses, search_courses, get_course_role
    ├── assignments.py      list_assignments
    ├── deadlines.py        upcoming_deadlines
    ├── grades.py           get_grades
    ├── contents.py         get_course_contents
    ├── module.py           get_module (open one item, dispatch by type)
    ├── submissions.py      submit_assignment (save online-text; no finalize)
    ├── announcements.py    list_announcements, get_announcement
    └── notifications.py    get_notifications
scripts/
└── http_client.py          minimal plain-requests client for testing
pyproject.toml              metadata, deps, `nccu-moodle-mcp` entry point
uv.lock                     pinned lockfile (committed)
Dockerfile                  multi-stage uv build; `prod` target runs the server
docker-compose.yml          service `nccucourse` — build + run on port 3033
.dockerignore               keeps .venv, secrets, caches out of the build context
```
