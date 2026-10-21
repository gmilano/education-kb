# Quizlar MCP Server

Voice-led, FSRS-scheduled flashcards from YouTube, PDFs, web, or text. Auto-graded quizzes.

Quizlar's MCP server lets Claude, Cursor, Cline, Windsurf, or any MCP-compatible client:

- Create flashcard decks from YouTube videos, PDFs, web pages, or pasted text
- Run auto-graded quizzes with the same tier-1-exact-match → phonetic → LLM grading pipeline that powers the [voice product](https://quizlar.app)
- Track memory with FSRS spaced repetition — Quizlar is the scheduler of record, every answer updates real memory state

This repo is the public discovery surface (`server.json` for the Official MCP Registry + a stdio bundle for clients that need it). The hosted MCP server itself is closed-source and runs at `https://mcp.quizlar.app` — `/mcp/` for OAuth-capable clients, `/mcp-apikey/` for apiKey Bearer auth (used by every snippet in this README).

## Listings

- **Official MCP Registry** — `io.github.quizlar/mcp-server` v1.0.0
- **Smithery** — <https://smithery.ai/servers/quizlar/quizlar>

## Setup

1. **Mint an API key** at <https://quizlar.app/settings/api-keys> (format: `sk-qz-<32 chars>`).
2. **Pick your client below** and paste the snippet.

### Cursor

`~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "quizlar": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.quizlar.app/mcp-apikey/",
        "--header",
        "Authorization:Bearer ${QUIZLAR_API_KEY}"
      ],
      "env": { "QUIZLAR_API_KEY": "sk-qz-..." }
    }
  }
}
```

### Windsurf

`~/.codeium/windsurf/mcp_config.json` — Windsurf supports Streamable HTTP natively, no wrapper needed:

```json
{
  "mcpServers": {
    "quizlar": {
      "serverUrl": "https://mcp.quizlar.app/mcp-apikey/",
      "headers": { "Authorization": "Bearer ${QUIZLAR_API_KEY}" }
    }
  }
}
```

Then `export QUIZLAR_API_KEY=sk-qz-...` in your shell.

### Claude Desktop

Open Settings → Connectors → "Add custom connector":

- **Name:** Quizlar
- **URL:** `https://mcp.quizlar.app/mcp-apikey/`
- Add header → **Name:** `Authorization`, **Value:** `Bearer sk-qz-...`

Or edit `claude_desktop_config.json` directly using `mcp-remote`:

```json
{
  "mcpServers": {
    "quizlar": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.quizlar.app/mcp-apikey/",
        "--header",
        "Authorization:Bearer ${QUIZLAR_API_KEY}"
      ],
      "env": { "QUIZLAR_API_KEY": "sk-qz-..." }
    }
  }
}
```

### Cline

Edit `cline_mcp_settings.json` (Cline → Settings → MCP Servers → "Edit JSON"):

```json
{
  "mcpServers": {
    "quizlar": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.quizlar.app/mcp-apikey/",
        "--header",
        "Authorization:Bearer ${QUIZLAR_API_KEY}"
      ],
      "env": { "QUIZLAR_API_KEY": "sk-qz-..." }
    }
  }
}
```

Detailed steps in [`llms-install.md`](./llms-install.md).

### Smithery

```sh
npx -y @smithery/cli@latest install @quizlar/quizlar --client claude
```

Replace `claude` with `cursor`, `windsurf`, etc. Smithery walks you through pasting your API key.

## Tools

22 tools mapped 1:1 to learner verbs:

- **Build decks:** `create_deck`, `create_deck_from_text`, `create_deck_from_youtube`, `create_cards_batch`, `get_job_status`
- **Quiz:** `quiz_me` (composite: build + start in one call), `start_quiz`, `submit_answer`, `skip_question`, `end_quiz`
- **Browse:** `list_decks`, `get_deck`, `list_cards`, `search_decks`, `search_cards`, `list_sessions`
- **Analytics:** `get_progress`, `get_study_recommendations`, `get_learning_velocity`, `get_knowledge_gaps`, `get_retention_curves`, `get_card_difficulty_stats`

## Auth

Bearer API key (`sk-qz-<32 chars>`) is the simplest path; the `/mcp-apikey/` mount used in every snippet above accepts the Bearer header directly and skips the OAuth handshake that some stdio bridges can't drive. Quizlar also exposes full OAuth 2.1 with Dynamic Client Registration + PKCE on `https://mcp.quizlar.app/mcp/` (discovery card at `/.well-known/oauth-authorization-server`) for clients that prefer a browser flow.

## Troubleshooting

- **`401 Unauthorized` on every tool call** — API key is missing, mistyped, or revoked. Re-mint at <https://quizlar.app/settings/api-keys> and paste the full `sk-qz-…` value, including the prefix, into the `Authorization: Bearer …` header.
- **Client doesn't see Quizlar tools after editing config** — fully restart the client (most don't hot-reload MCP config). For Claude Desktop, quit from the menu bar; for Cursor / Windsurf / Cline, close all windows.
- **`mcp-remote` fails to launch** — usually a Node.js / `npx` path issue. Run `npx -y mcp-remote --help` in a terminal to verify it resolves; if behind a corporate proxy, set `HTTPS_PROXY` in the client's `env` block or install `mcp-remote` globally with `npm i -g mcp-remote`.
- **`429` / quota errors mid-quiz** — free-tier daily limits reached. Quotas reset at midnight UTC; or upgrade at <https://quizlar.app/settings/billing>.
- **OAuth callback never returns to the client** — your loopback port may be blocked. Fall back to the API-key flow above; it bypasses OAuth entirely.

For anything not covered here, file an issue at <https://github.com/quizlar/mcp-server/issues> or email <support@quizlar.app>.

## Links

- **App:** <https://quizlar.app>
- **Issues:** <https://github.com/quizlar/mcp-server/issues>
- **Stdio bundle source:** [`bundle/`](./bundle/) (used to publish to Smithery + any other stdio-only client)

## License

MIT for this configuration repo. The hosted MCP server itself is proprietary.
