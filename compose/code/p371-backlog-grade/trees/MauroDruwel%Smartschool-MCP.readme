# Smartschool MCP Server

<!-- mcp-name: io.github.MauroDruwel/smartschool-mcp -->

[![CI](https://github.com/MauroDruwel/Smartschool-MCP/actions/workflows/ci.yml/badge.svg)](https://github.com/MauroDruwel/Smartschool-MCP/actions/workflows/ci.yml)
[![Mauro Quality Gate](https://img.shields.io/badge/Mauro%20Quality%20Gate-Passed-2ea44f?style=flat&logo=github)](https://github.com/MauroDruwel/quality-gate)
[![codecov](https://codecov.io/gh/MauroDruwel/Smartschool-MCP/branch/main/graph/badge.svg)](https://codecov.io/gh/MauroDruwel/Smartschool-MCP)
[![PyPI version](https://img.shields.io/pypi/v/smartschool-mcp)](https://pypi.org/project/smartschool-mcp/)
[![License: MIT](https://img.shields.io/github/license/MauroDruwel/Smartschool-MCP)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

Connect Claude (and other MCP clients) to your Smartschool account — ask about grades, assignments, messages, and your schedule in plain language.

## Tools

| Tool | What it does |
|------|-------------|
| `get_courses` | List enrolled courses with teacher info |
| `get_results` | Grades with optional filtering, pagination, and statistics |
| `get_future_tasks` | Upcoming assignments organised by date |
| `get_messages` | Inbox/sent/trash with search, sender filter, and body retrieval |
| `get_schedule` | Day schedule by offset (0 = today, 1 = tomorrow, …) |
| `get_periods` | Academic terms for the current school year |
| `get_reports` | Available report cards |
| `get_planned_elements` | Planner items for the next N days |
| `get_student_support_links` | School support resources and links |
| `get_student_notes` | Student file notes (Leerlingvolgsysteem), without confidential notes; details on request (`text`, `fields`, `date`, `choice`, `attachments` as name + mime) |
| `get_student_absences` | Absences recorded in the Leerlingvolgsysteem (date, code, description, part of day) |
| `get_attachments` | List attachments for a specific message |
| `download_attachment` | Download a specific attachment by message and file ID |
| `get_homepage_blocks` | "In de kijker" blocks pinned to the homepage (e.g. monthly menu, calendar) |
| `download_homepage_image` | Download an image embedded in a homepage block |

## Quick start — Claude Desktop

```bash
uvx mcp install smartschool-mcp \
  -e SMARTSCHOOL_USERNAME="you" \
  -e SMARTSCHOOL_PASSWORD="secret" \
  -e SMARTSCHOOL_MAIN_URL="school.smartschool.be" \
  -e SMARTSCHOOL_MFA="YYYY-MM-DD"
```

Or add it manually to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "smartschool": {
      "command": "uvx",
      "args": ["smartschool-mcp"],
      "env": {
        "SMARTSCHOOL_USERNAME": "you",
        "SMARTSCHOOL_PASSWORD": "secret",
        "SMARTSCHOOL_MAIN_URL": "school.smartschool.be",
        "SMARTSCHOOL_MFA": "YYYY-MM-DD"
      }
    }
  }
}
```

Config file locations: `%APPDATA%\Claude\claude_desktop_config.json` (Windows) · `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) · `~/.config/Claude/claude_desktop_config.json` (Linux)

## Remote / claude.ai

The server supports **Streamable HTTP** transport for use as a remote integration on claude.ai.

### Comparing modes

| Mode | Best for | Setup | Credentials | Auth method |
|------|----------|-------|-------------|-------------|
| **Single-user** | Personal use or one household | Simple, local | In env vars | Optional static Bearer token |
| **Universal** | Hosting for multiple users | Requires public URL + HTTPS | Via login form | OAuth 2.1 with login form |

### Single-user mode

One server instance, your credentials in environment variables:

```bash
export SMARTSCHOOL_USERNAME="..."
export SMARTSCHOOL_PASSWORD="..."
export SMARTSCHOOL_MAIN_URL="school.smartschool.be"
export SMARTSCHOOL_MFA="YYYY-MM-DD"
export MCP_API_KEY="a-long-random-secret"   # optional but recommended

smartschool-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Add to claude.ai → Settings → Integrations:
- **URL:** `https://your-domain.example.com/mcp`
- **Authorization header:** `Bearer <your MCP_API_KEY>` (if set)

### Universal mode — OAuth 2.1 login flow

One hosted server instance serves **any** Smartschool user via OAuth 2.1. Users authenticate through a browser-based login form during the authorization flow.

```bash
export MCP_ISSUER_URL="https://your-domain.example.com"  # public server URL

smartschool-mcp --transport streamable-http --universal \
  --issuer-url "$MCP_ISSUER_URL" \
  --host 0.0.0.0 --port 8000
```

In claude.ai → Settings → Integrations → Add custom integration:
- **URL:** `https://your-domain.example.com/mcp`

**How it works:**

1. Claude.ai discovers OAuth endpoints at `https://your-domain.example.com/.well-known/oauth-authorization-server`
2. Claude.ai registers a client dynamically via `/register`
3. Claude.ai directs the user to `/authorize?...` (OAuth authorization endpoint)
4. User is redirected to a login form at `/smartschool-login`
5. User enters: **School URL**, **Username**, **Password**, and optional **MFA** (date of birth)
6. On successful login, the server generates an authorization code
7. Claude.ai exchanges the code for an access token (via `/token` with PKCE)
8. Claude.ai uses the Bearer token on all subsequent `/mcp` requests

> **Security:** Credentials are never stored in URLs or environment variables. They're collected via HTTPS form submission and validated against Smartschool. Only access tokens are sent with API requests.

### Making the server publicly accessible

**Required for universal mode.** Claude.ai requires HTTPS and must be able to reach your server to redirect users to the login form and receive authorization callbacks.

Some options:

| Option | Command |
|--------|---------|
| Cloudflare Tunnel | `cloudflared tunnel --url http://localhost:8000` |
| ngrok | `ngrok http 8000` |
| VPS | nginx / Caddy with a Let's Encrypt cert |

After setting up the tunnel/proxy, your server will be reachable at `https://your-domain.example.com`. Use this as `MCP_ISSUER_URL`.

## Environment variables

| Variable | CLI flag | Default | Description |
|----------|----------|---------|-------------|
| `MCP_TRANSPORT` | `--transport` | `stdio` | `stdio` or `streamable-http` |
| `MCP_HOST` | `--host` | `0.0.0.0` | Bind address (HTTP only) |
| `MCP_PORT` | `--port` | `8000` | Port (HTTP only) |
| `MCP_API_KEY` | — | — | Static Bearer token (single-user mode only) |
| `MCP_UNIVERSAL` | `--universal` | off | Enable universal mode (set to `1`, `true`, or `yes`) |
| `MCP_ISSUER_URL` | `--issuer-url` | — | **Required in universal mode.** Public URL of the server, e.g. `https://mcp.example.com` |
| `SESSION_TTL_SECONDS` | — | `3600` | How long to cache Smartschool sessions (universal mode) |
| `SMARTSCHOOL_USERNAME` | — | — | Your Smartschool username (single-user mode only) |
| `SMARTSCHOOL_PASSWORD` | — | — | Your Smartschool password (single-user mode only) |
| `SMARTSCHOOL_MAIN_URL` | — | — | School hostname, e.g. `school.smartschool.be` (single-user mode only) |
| `SMARTSCHOOL_MFA` | — | — | Date of birth `YYYY-MM-DD` if required (single-user mode only) |

## Contributing

PRs are welcome. Run `uv sync --extra dev` to install dev dependencies, then `uv run pytest` / `uv run ruff check .` / `uv run mypy smartschool_mcp/` before submitting.

## Disclaimer

Unofficial tool, not affiliated with Smartschool. Use in accordance with your school's terms of service.
