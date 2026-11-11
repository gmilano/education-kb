# UIS SDG4 MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that gives AI assistants
direct, grounded access to UNESCO Institute for Statistics (UIS) published SDG 4 education indicator
data via the UIS public API.

The server handles all indicator ID resolution, API calls, and validity filtering.
The AI receives only clean, observed data and generates narrative from it —
it never produces or estimates data values.

---

## What it solves

Previous attempts at AI-driven UIS data tools failed because:

| Problem | Fix in this server |
|---|---|
| Wrong indicator IDs (hallucinated) | All IDs resolved from a validated codebook, never inferred |
| API connection failures | Per-indicator error isolation + retry logic |
| Modelled estimates presented as reported data | Validity filter applied server-side before returning to AI |
| No indicator hierarchy | Full SDG number → IG group → indicator ID chain in codebook |

**Core principle:** the AI writes the narrative; the server owns the numbers.

---

## Prerequisites

- Python 3.10 or later
- An MCP-compatible client (Claude Desktop, Cursor, or any client implementing the [MCP spec](https://modelcontextprotocol.io))
- Internet access to reach `api.uis.unesco.org`

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/uis-sdg4-mcp.git
cd uis-sdg4-mcp

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the self-test (no API connection needed)
python server.py --test

# 5. Run the full offline test suite
pip install pytest
pytest tests/ -v -m "not api"

# 6. Optionally run API tests (requires internet)
pytest tests/ -v -m api
```

---

## Connecting to Claude Desktop

Edit your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "uis-sdg4": {
      "command": "python",
      "args": ["/absolute/path/to/uis-sdg4-mcp/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/uis-sdg4-mcp/server.py` with the actual full path on your machine.
Restart Claude Desktop. The tools will appear automatically.

### Using a virtual environment (recommended)

```json
{
  "mcpServers": {
    "uis-sdg4": {
      "command": "/absolute/path/to/uis-sdg4-mcp/venv/bin/python",
      "args": ["/absolute/path/to/uis-sdg4-mcp/server.py"]
    }
  }
}
```

---

## Connecting to other MCP-compatible clients

The server communicates over stdio and follows the open MCP specification.
Any client implementing the spec can connect using the same `command` / `args` pattern above.

---

## Available tools

### `resolve_sdg_indicators`
Maps an SDG 4 indicator number to validated UIS indicator IDs from the authoritative codebook.
Always call this before fetching data when you know the SDG number but not the indicator IDs.

**Example prompt:** *"What are the indicator IDs for SDG 4.6.1?"*

---

### `get_indicator_data`
Fetches published UIS data for one or more indicator IDs and a country.
Returns only observed/reported data — modelled estimates excluded by default.
Applies UIS validity rules (excludes MAGNITUDE: SUPP, NA, INCLUDED).

**Example prompt:** *"Get literacy rate data for Uzbekistan from 2014 to 2024."*

---

### `compute_coverage`
Computes post-threshold data availability statistics for a list of indicator IDs.
For a single country: returns years with data, latest year, and post-threshold status.

**Example prompt:** *"Does Uzbekistan have out-of-school rate data after 2020?"*

---

### `compute_sdg_coverage`
Convenience tool: resolves an SDG number to indicator IDs, then computes coverage in one call.

**Example prompt:** *"What is the data availability situation for SDG 4.1.4 for Tanzania?"*

---

### `format_country_briefing`
Formats raw API results into a structured briefing dict with gap years, year-over-year
changes, and post-threshold availability — ready for the AI to narrate.
Also returns the UIS writing style guide.

**Example prompt:** *"Generate a data availability briefing for Morocco on SDG 4.6.1."*

---

### `list_sdg4_indicators`
Lists all validated SDG 4 indicator numbers with labels and component UIS indicator IDs.
Optionally filter by `global` or `thematic` scope.

**Example prompt:** *"List all global SDG 4 indicators."*

---

### `validate_indicator_ids`
Checks whether given indicator IDs exist in the live UIS API.
Use after a data release update to verify codebook IDs are still current.

---

### `get_writing_style_guide`
Returns the UIS writing style rules for generating briefings.
Neutral, factual language. No evaluative adjectives. No attribution of data gaps
to country behaviour or capacity.

---

## Example workflow

A user can type natural language — the AI calls the tools in sequence:

```
User: "Generate a data briefing for Uzbekistan covering SDG 4.6.1 literacy indicators."

AI calls:
  1. resolve_sdg_indicators("4.6.1")
     → ["LR.AG15T24", "LR.AG15T99", "LR.AG25T64", "LR.AG65T99"]

  2. get_indicator_data(["LR.AG15T24","LR.AG15T99"], "UZB", 2014, 2025)
     → observed records per indicator, years with data, validity-filtered

  3. format_country_briefing("Uzbekistan", "UZB", <results from step 2>)
     → structured briefing dict with gap years, latest values, writing style guide

  4. AI generates narrative from the structured data
```

---

## Codebook structure

The `codebooks/` directory contains the authoritative mappings:

| File | Contents |
|---|---|
| `indicator_framework.json` | All 45 SDG 4 indicators: SDG number → IG group codes → validated indicator IDs |
| `region_order.json` | UIS sub-region canonical order and naming |
| `validity_rules.json` | MAGNITUDE exclusions, modelled prefix list, API configuration |

### Updating the codebook

When UIS publishes a new indicator framework version:

1. Open `codebooks/indicator_framework.json`
2. Add, remove, or update indicator ID lists for the affected SDG numbers
3. Run `pytest tests/ -v -m "not api"` to verify consistency
4. Run `python server.py --test` for a quick end-to-end check
5. Optionally run `pytest tests/ -v -m api` to validate against the live API

---

## Data validity rules

A data record is counted as observed/reported if:
- `MAGNITUDE` is **not** in `{SUPP, NA, INCLUDED}`
- `VALUE` is non-null
- `INDICATOR_ID` does **not** start with `CR.MOD.` or `LR.GALP.` (modelled estimates)

Coverage threshold: a country is considered to have data for an indicator if it has
at least one valid record with `YEAR > 2020` (configurable per request).

---

## Writing style

All generated text follows UIS conventions:
- Neutral, factual language
- No evaluative adjectives (poor, weak, alarming, impressive, strong)
- No attribution of data gaps to country behaviour or capacity
- Passive constructions when describing gaps
- Describes what the data show, not what they imply

---

## Repository structure

```
uis-sdg4-mcp/
├── README.md
├── requirements.txt
├── pyproject.toml
├── server.py                        # MCP server entry point
├── codebooks/
│   ├── indicator_framework.json     # Validated SDG4 indicator ID mappings
│   ├── region_order.json            # UIS regional classification
│   └── validity_rules.json          # Data validity rules and API config
├── tools/
│   ├── __init__.py
│   ├── map_indicators.py            # SDG number → indicator ID resolution
│   ├── fetch_data.py                # UIS API calls with validity filtering
│   ├── coverage.py                  # Coverage statistics computation
│   └── briefing.py                  # Output formatting helpers
└── tests/
    ├── __init__.py
    └── test_tools.py                # Offline + API test suite
```

---

## Data source

All data is retrieved live from the **UIS public API**:
`https://api.uis.unesco.org/api/public`

No data is stored locally. The codebooks contain only structural metadata
(indicator IDs, regional groupings, validity rules) — not data values.

Source: UNESCO Institute for Statistics — UIS Bulk Data Download / UIS API,
SDG4 Monitoring Framework, January 2026.

---

## License

MIT License. See `LICENSE` for details.

Data accessed via this tool is subject to [UIS data terms of use](https://uis.unesco.org/en/uis-data-licence).
