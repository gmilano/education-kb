# OB3 MCP Server

A local Model Context Protocol server that exposes the [Open Badges 3.0](https://www.imsglobal.org/spec/ob/v3p0/) specification as queryable tools for coding agents.

Built on [sql.js](https://github.com/sql-js/sql.js) (pure-WASM SQLite) for zero-native-dependency portability — no platform-specific binaries, works everywhere Node runs. The OB3 spec corpus is small enough that the WASM overhead is negligible.

## Quick Start

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "ob3": {
      "command": "npx",
      "args": ["-y", "mcp-ob-ts"]
    }
  }
}
```

### Cursor

Add to your Cursor MCP configuration:

```json
{
  "mcpServers": {
    "ob3": {
      "command": "npx",
      "args": ["-y", "mcp-ob-ts"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add ob3 -- npx -y mcp-ob-ts
```

### Kiro

Add to `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "ob3": {
      "command": "npx",
      "args": ["-y", "mcp-ob-ts"]
    }
  }
}
```

## Tools

The server exposes tools for querying the OB3 specification:

| Tool                            | Description                                    |
| ------------------------------- | ---------------------------------------------- |
| `ping`                          | Health check                                   |
| `list_classes`                  | List all OB3 classes                           |
| `get_class`                     | Get full details for a class                   |
| `list_properties`               | List properties (optionally filtered by class) |
| `get_property`                  | Get full details for a property                |
| `get_section`                   | Retrieve a spec section by heading             |
| `list_sections`                 | List all spec sections                         |
| `search_spec`                   | Full-text search across the spec               |
| `get_examples`                  | Get JSON-LD examples for a class               |
| `get_context`                   | Retrieve the OB3 JSON-LD context               |
| `resolve_term`                  | Resolve a JSON-LD term to its IRI              |
| `cross_reference`               | Find relationships between classes             |
| `find_conformance_requirements` | List conformance/validation rules              |
| `validate_credential`           | Validate a credential against the OB3 schema, JSON-LD structure, and/or cryptographic signature |
| `generate_credential`           | Generate a representative credential by walking the type graph |
| `create_achievement_credential` | Build an unsigned credential from substantive content |

## Development

```bash
pnpm install
pnpm build
pnpm test
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full development guide, release process, and CI details.

### Architecture

```
src/
├── cli.ts          # CLI entry point (bin)
├── server.ts       # MCP server setup
├── config.ts       # Configuration / paths
├── tools/          # One file per MCP tool
├── spec/           # SQLite-backed spec index (sql.js)
├── context/        # JSON-LD context loader
├── vocab/          # RDF vocabulary (N3)
├── validate/       # JSON Schema + JSON-LD validation
├── create/         # Credential builder (rich-tier authoring)
├── generator/      # Type-graph credential generation
├── crypto/         # Canonicalization + signature verification
└── util/           # Shared helpers (output bounding)
```

Spec data lives in `data/snapshots/<version>/` as versioned snapshots. The SQLite index (`data/index.db`) is rebuilt from snapshots via `pnpm data:ingest`.

## Why sql.js?

This server uses sql.js (SQLite compiled to WASM) instead of native bindings like better-sqlite3. The OB3 spec corpus is small (~hundreds of rows with FTS), so the WASM overhead is imperceptible. The trade-off buys universal portability: no `node-gyp`, no platform-specific prebuild downloads, no broken installs on CI or in containers.

## License

[MIT](./LICENSE)
