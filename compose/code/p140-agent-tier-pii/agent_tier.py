"""p140-agent-tier-pii — `ACTION CT`: what a learner-facing MCP agent tier actually
persists, and whether it is a write surface of the `P18` class.

`ACTION CT` as p139 pre-registered it:

> Read **`ArnaudGuiovanna/tutor-mcp`** in source: what its "durable learner state" and
> "auditable pedagogical decisions" actually persist, and whether any of it is a write
> surface of the `P18` class. 🔴 *Refuted if the agent tier turns out to hold no learner PII
> at all, which would put it outside the Annex III/Decision 33 frame this KB has been
> applying.*

This probe measures four things over a git clone, reading text only:

1.  **The tool surface**, excluding `*_test.go`. An earlier count of 60 included `bench`,
    `client`, `test`, `tool_that_does_not_exist` and the server's own name `tutor_mcp` --
    test fixtures, not tools. The non-test denominator is 56.
2.  **The write surface**, by verb. `P18` exists because an undocumented write to an LMS is
    an ungoverned capability; the same question is asked of this row.
3.  **Documentation drift** against `docs/mcp-tools.md`, the same README-versus-build axis
    `p139-tool-count-drift` applied to the npm shelf.
4.  **Persisted learner identifiers and psychological state**, by reading the schema rather
    than the prose -- which is what decides whether the row is inside the Annex III /
    Decision 33 frame at all.

🔵 **Go, not JavaScript, so none of p139's JS idioms apply.** Registration here is the
official `modelcontextprotocol/go-sdk` form, `mcp.AddTool(server, &mcp.Tool{Name: "..."}, h)`,
and tool names are `Name:` fields on struct literals.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

TOOL_NAME = re.compile(r'Name:\s*"([a-z][a-z0-9_]{2,60})"')
DOC_TOOL = re.compile(r"`([a-z][a-z0-9_]{2,60})`")

WRITE_VERBS = (
    "add", "set", "update", "record", "submit", "publish", "delete", "archive",
    "unarchive", "init", "draft", "cancel", "prepare", "start", "mark", "queue",
    "join", "create", "remove", "revoke",
)
WRITE = re.compile(r"^(?:%s)_" % "|".join(WRITE_VERBS))

# Columns that identify a natural person directly.
DIRECT_PII = re.compile(
    r"^\s*(email|full_name|display_name|first_name|last_name|given_name|family_name|"
    r"phone|phone_number|address|date_of_birth|birth_date|dob|national_id|ip_address)\b",
    re.IGNORECASE | re.MULTILINE,
)
# Columns recording inferred affective or psychological state. Vietnam's Decision
# 33/2026/QĐ-TTg names psychological assessment in its education high-risk list (p138),
# so these are the columns that decide the regime question.
AFFECT_HINT = re.compile(
    r"^\s*(energy|mood|affect|confidence|subject_confidence|satisfaction|"
    r"perceived_difficulty|frustration|engagement|motivation|autonomy_score|"
    r"next_session_intent|calibration|self_efficacy)\b",
    re.IGNORECASE | re.MULTILINE,
)
# A gate that makes a decision reviewable by a human rather than by the model.
OVERSIGHT = re.compile(r"high_stakes|human_review|human_reviewed|adjudicat", re.IGNORECASE)

CREATE_TABLE = re.compile(
    r"CREATE TABLE(?:\s+IF NOT EXISTS)?\s+([A-Za-z_][\w]*)\s*\((.*?)\n\);",
    re.DOTALL | re.IGNORECASE,
)


def git(repo, *args):
    out = subprocess.run(("git", "-C", str(repo)) + args, capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def tracked(repo):
    return [p for p in git(repo, "ls-tree", "-r", "HEAD", "--name-only").splitlines() if p]


def read(repo, path):
    return git(repo, "show", "HEAD:" + path)


def tool_surface(repo, tool_dir="tools", server_name=None):
    """Registered tool names from non-test sources."""
    paths = [p for p in tracked(repo)
             if p.startswith(tool_dir + "/") and p.endswith(".go")
             and not p.endswith("_test.go")]
    names = set()
    for p in paths:
        names.update(TOOL_NAME.findall(read(repo, p)))
    if server_name:
        names.discard(server_name)
    return sorted(names), len(paths)


def documented(repo, doc_path):
    text = read(repo, doc_path)
    return set(DOC_TOOL.findall(text)) if text else set()


def schema_scan(repo, schema_paths):
    """Tables carrying direct identifiers or affective state."""
    pii, affect, tables = {}, {}, 0
    for sp in schema_paths:
        text = read(repo, sp)
        if not text:
            continue
        for name, body in CREATE_TABLE.findall(text):
            tables += 1
            cols = [m.group(1).lower() for m in DIRECT_PII.finditer(body)]
            if cols:
                pii.setdefault(name, set()).update(cols)
            acols = [m.group(1).lower() for m in AFFECT_HINT.finditer(body)]
            if acols:
                affect.setdefault(name, set()).update(acols)
    return pii, affect, tables


def oversight_tools(names, repo, tool_dir="tools"):
    hits = [n for n in names if OVERSIGHT.search(n)]
    # A one-way gate is proven by the ABSENCE of an inverse tool, so record both.
    inverse = [n for n in names if re.match(r"^(unmark|clear|unset|reset)_", n)]
    return hits, inverse


def measure(repo, server_name="tutor_mcp", doc_path="docs/mcp-tools.md",
            schema_paths=("db/schema.sql", "db/schema_pg.sql")):
    names, src_files = tool_surface(repo, server_name=server_name)
    doc = documented(repo, doc_path)
    writes = [n for n in names if WRITE.match(n)]
    undoc = [n for n in names if n not in doc]
    undoc_writes = [n for n in undoc if WRITE.match(n)]
    pii, affect, tables = schema_scan(repo, schema_paths)
    oversight, inverse = oversight_tools(names, repo)

    all_paths = tracked(repo)
    return {
        "repo": Path(str(repo)).name,
        "tree_paths": len(all_paths),
        "go_test_files": sum(1 for p in all_paths if p.endswith("_test.go")),
        "go_src_files": sum(1 for p in all_paths
                            if p.endswith(".go") and not p.endswith("_test.go")),
        "tool_source_files": src_files,
        "tools": len(names),
        "writes": len(writes),
        "documented": len(doc & set(names)),
        "undocumented": len(undoc),
        "undocumented_writes": len(undoc_writes),
        "schema_tables": tables,
        "direct_pii_tables": len(pii),
        "affect_tables": len(affect),
        "oversight_tools": ",".join(oversight) or "-",
        "inverse_tools": ",".join(inverse) or "NONE",
        "verdict": (
            "PII_AND_AFFECT" if pii and affect else
            "PII_ONLY" if pii else
            "AFFECT_ONLY" if affect else
            "NO_LEARNER_PII"
        ),
        "_undocumented": undoc,
        "_undocumented_writes": undoc_writes,
        "_pii": {k: sorted(v) for k, v in pii.items()},
        "_affect": {k: sorted(v) for k, v in affect.items()},
        "_writes": writes,
    }


COLS = ["repo", "tree_paths", "go_src_files", "go_test_files", "tools", "writes",
        "documented", "undocumented", "undocumented_writes", "schema_tables",
        "direct_pii_tables", "affect_tables", "oversight_tools", "inverse_tools",
        "verdict"]


def main(argv):
    if not argv:
        print(__doc__, file=sys.stderr)
        print("usage: agent_tier.py <clone> [...]", file=sys.stderr)
        return 2
    rows = [measure(d) for d in argv]
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    print("\n# detail", file=sys.stderr)
    for r in rows:
        print(r["repo"], json.dumps({
            "undocumented": r["_undocumented"],
            "undocumented_writes": r["_undocumented_writes"],
            "direct_pii": r["_pii"],
            "affect": r["_affect"],
            "writes": r["_writes"],
        }, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
