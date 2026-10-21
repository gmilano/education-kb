# districtapi-mcp

<!-- Links this package to its entry in the official MCP registry -->
mcp-name: dev.districtapi/districtapi-mcp

MCP server for [districtapi.dev](https://districtapi.dev) — US school district and school data for AI agents.

Expose school district lookups as tools to any MCP-compatible AI assistant (Claude, Cursor, Copilot, etc.).

## Installation

```bash
pip install districtapi-mcp
```

Or run directly with `uvx` (no install needed):

```bash
uvx districtapi-mcp
```

## Configuration

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "districtapi": {
      "command": "uvx",
      "args": ["districtapi-mcp"],
      "env": {
        "DISTRICTAPI_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Cursor / other MCP clients

```json
{
  "mcpServers": {
    "districtapi": {
      "command": "uvx",
      "args": ["districtapi-mcp"],
      "env": {
        "DISTRICTAPI_KEY": "your_api_key_here"
      }
    }
  }
}
```

Get a free API key at [districtapi.dev](https://districtapi.dev).

## Available Tools

| Tool | Description |
|------|-------------|
| `lookup_district_by_address` | Find the district serving a US street address |
| `get_district` | Get full district profile by NCES LEA ID |
| `search_districts` | Search districts by name and/or state |
| `get_district_schools` | List all schools in a district |
| `get_school` | Get full school profile by NCES school ID |
| `find_schools_near_address` | Find schools within a radius of an address |

## Example

Once configured, you can ask your AI assistant:

> "What school district serves 1600 Pennsylvania Ave, Austin TX, and how many students are enrolled?"

The assistant will call `lookup_district_by_address` and return the full district profile.

## Links

- **Website:** [districtapi.dev](https://districtapi.dev)
- **PyPI:** [pypi.org/project/districtapi-mcp](https://pypi.org/project/districtapi-mcp)
- **REST API docs:** [districtapi.dev/docs](https://districtapi.dev/docs)

## License

MIT
