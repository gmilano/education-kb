# uniAI-MCP

uniAI-MCP is a Model Context Protocol (MCP) server that provides AI agents with direct, deterministic access to university academic materials, including syllabi, unit-wise notes, and previous year questions (PYQs). It relies on a clean SQLite database to map academic subjects to their specific local markdown files without requiring fuzzy text matching, vector databases, or complex embeddings.

---

## Features & MCP Tools

uniAI-MCP implements the MCP protocol (over streamable HTTP) and exposes the following tools:

1. **`get_availability()`**
   - Discovers all supported academic years, subjects, codes, and available resource types (`syllabus`, `notes`, `pyq`).
   - Call this first before accessing any university material.
2. **`get_syllabus(code: str)`**
   - Returns the complete markdown syllabus for the specified subject code (e.g. `BCS501H`).
3. **`get_notes(code: str, unit: int)`**
   - Returns the unit notes for the specified subject code and unit (units 1–5).
4. **`get_pyq(code: str)`**
   - Returns all previous year questions for the subject, indexed and formatted with year labels (e.g. `2026-0`, `2025-1`).
5. **`uniAI_instructions` (MCP Prompt)**
   - Guided prompt instructing AI clients on proper workflow: checking availability first, verifying subject code validity, and serving materials directly.

---

## Unified Resource Organization

All academic materials are stored in a predictable, unified hierarchy relative to `RESOURCES_ROOT`:

```
resources/
└── {university}/                   # e.g., AKTU
    └── {year}/                     # e.g., 3
        └── {subject_code}/         # e.g., BCS501H
            ├── syllabus/           # e.g., aktu.md
            ├── notes/              # Unit-wise notes (units 1-5)
            │   ├── unit1/
            │   │   └── {source}.md # e.g., gateway-classes.md
            │   ├── unit2/
            │   ├── unit3/
            │   ├── unit4/
            │   └── unit5/
            └── pyq/                # Previous year question papers
                ├── 2026-0.md
                ├── 2025-0.md
                └── ...
```

---

## Database Architecture

A lightweight SQLite database (`database.db`) guarantees deterministic resource lookups:

- **`subjects`**: `id`, `year`, `name`, `code` (unique code per subject)
- **`sources`**: `id`, `name` (e.g., `'AKTU'`, `'Gateway Classes'`)
- **`resources`**: `id`, `subject_id`, `resource_type` (`'syllabus'`, `'notes'`, `'pyq'`), `source_id`, `label`, `file_path`

---

## Getting Started

### Prerequisites

- [Python 3.12+](https://www.python.org/)
- [`uv`](https://docs.astral.sh/uv/) package manager

### Environment Configuration

Create a `.env` file in the project root (see `.env.example`):

```bash
BASE_DIR=/home/anon/PROJECTS/uniAI-MCP
DB_PATH=/home/anon/PROJECTS/uniAI-MCP/database.db
RESOURCES_ROOT=/home/anon/PROJECTS/uniAI-MCP/resources
```

### Installation

Install dependencies using `uv`:

```bash
uv sync
```

---

## Running the Server

Start the streamable HTTP MCP server:

```bash
# Direct module execution
uv run -m src.uniai_mcp.main

# Or via installed console script
uv run uniai-mcp
```

The server binds to port `3001` with transport security configured.

### MCP Inspector

To test and inspect the server using the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector@latest
```
Connect via streamable HTTP to `http://localhost:3001`.

### Tunneling (Optional)

To expose the server securely using Cloudflare Tunnel:

```bash
cloudflared tunnel run projects
```

---

## Testing

The project has a comprehensive pytest suite covering availability, syllabi, notes, and PYQs:

```bash
# Run all tests
uv run pytest

# Run individual test modules
uv run pytest test/test_availability.py
uv run pytest test/test_syllabus.py
uv run pytest test/test_notes.py
uv run pytest test/test_pyq.py
```

---

## Ingestion & Extraction Scripts

### Ingestion

Scripts to populate and migrate data into the unified resource hierarchy and database:

- `ingest/migrate_all_resources.py`: Ingests BCS501H syllabus, 5 units of notes, and 34 PYQ markdown files.
  ```bash
  uv run python ingest/migrate_all_resources.py
  ```
- `ingest/add_missing_syllabi.py`: Sets up unified syllabus paths for remaining Year 3 AKTU subjects.
  ```bash
  uv run python ingest/add_missing_syllabi.py
  ```

### OCR Extraction

Scripts for processing raw PDFs:

- `extract/extract_ollama.py`: Submits PDF pages to OCR service.
  ```bash
  uv run python extract/extract_ollama.py
  ```
- `extract/poll_results.py`: Polls OCR results and compiles markdown outputs.
  ```bash
  uv run python extract/poll_results.py
  uv run python extract/poll_results.py --once
  ```
