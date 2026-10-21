# Schoology MCP Server
[![MCP Badge](https://lobehub.com/badge/mcp/coimf-schoology-mcp?style=flat)](https://lobehub.com/mcp/coimf-schoology-mcp)

---

Provide LLMs with your courses and upcoming assignments from Schoology.

## Installation

---

> [!NOTE]
> You must be signed in to Schoology in your browser to use Schoology MCP.

Add the following to the configuration file in your MCP client of choice. Replace `<YOUR-SCHOOL-DISTRICT>.schoology.com` with your Schoology page URL and `PATH/TO/schoology-mcp` with where you cloned this repository. For example, the "Dump Truck Union High School District" might have a base url of `dtuhsd.schoology.com`.

```json
{
  "mcpServers": {
    "schoology-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "PATH/TO/schoology-mcp",
        "run",
        "src/server.py"
      ],
      "env": {
        "SCHOOLOGY_BASE_URL": "<YOUR-SCHOOL-DISTRICT>.schoology.com",
      }
    }
  }
}
```

## Tools

---

1. `get_enrolled_courses`
- Fetch a list of courses the user is enrolled in from Schoology.
- Returns a list of dictionaries containing course information.

2. `get_upcoming_assignments`
- Fetch a list of upcoming assignments from Schoology.
- Returns a list of dictionaries containing assignment information.
