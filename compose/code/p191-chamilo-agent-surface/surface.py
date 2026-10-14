#!/usr/bin/env python3
"""p191 / `P1060` — the agent surface of a SECOND platform, counted from definitions.

Why this exists
---------------
p190 counted `openedx-mcp`'s surface from its decorators and found `33` tool definitions
against `0` tool names in its README *(`ACTION NF`)*. 🔴 **One platform is an anecdote.**
This module asks the same question of [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms),
which ships a **native** MCP server *(`config/packages/mcp.yaml`, `app: Chamilo`,
`version: 2.1.0`)* — not a third-party facade — so the comparison is between two real
platform agent layers rather than between a platform and a plugin.

What it reads, and what it refuses to infer
-------------------------------------------
🟢 **Definitions, not prose.** A tool exists when a `#[McpTool(name: '…')]` attribute exists
in the source. The server's `instructions:` string in `mcp.yaml` is **not** evidence of a
tool and is **not** a control: it is a prompt. 🔴 p190's lesson, paid for in full — *"a
README's security sentence is a claim; a decorator is a fact"* — applies to a YAML
`instructions:` block with the same force, and this is the pass that had to say so, because
Chamilo's own block contains the sentence *"Every capability must respect the permissions of
the authenticated Chamilo user"*, which is a **statement of intent addressed to a model**.

🟢 **Guards are counted where they are ENFORCED**: `isGranted(...)`, an explicit
`AccessDeniedException`, a role constant. A guard named in a `description:` is counted
separately *(`in_prose`)* and never as enforcement.

read / write is from the tool's own VERB, which is the one thing a name does carry
-----------------------------------------------------------------------------------
🔴 Deliberately coarse, and a declared limit: `generate_student_success_feedback` is counted
a WRITE because it persists feedback about a learner, while `review_course_quality` is
counted a READ. A verb list cannot settle every case; it settles `62` of `68` without
reading a body, and the six it cannot are listed in `AMBIGUOUS_VERBS` rather than guessed.
"""
from __future__ import annotations

import re

TOOL_RE = re.compile(r"#\[McpTool\((.*?)\)\]", re.S)
NAME_RE = re.compile(r"name:\s*'([^']+)'")
DESC_RE = re.compile(r"description:\s*'((?:[^'\\]|\\.)*)'", re.S)

READ_VERBS = ("get", "list", "read", "find", "review")
WRITE_VERBS = ("create", "update", "edit", "upsert", "add", "set", "close", "move",
               "remove", "delete", "generate", "illustrate", "manage", "import")
# Verbs whose blast radius a NAME cannot settle. Listed, never guessed.
AMBIGUOUS_VERBS = ("review", "generate", "illustrate", "manage")

ENFORCED_RE = re.compile(
    r"isGranted\s*\(|throw new AccessDeniedException|AccessDeniedException\s*\(")
ROLE_RE = re.compile(r"'(ROLE_[A-Z_]+)'")


def tools_in(source: str) -> list[dict]:
    """Every `#[McpTool]` definition in one PHP source, with its name and description."""
    out: list[dict] = []
    for m in TOOL_RE.finditer(source):
        blk = m.group(1)
        name = NAME_RE.search(blk)
        desc = DESC_RE.search(blk)
        out.append({
            "name": name.group(1) if name else "(unnamed)",
            "description": (desc.group(1) if desc else ""),
        })
    return out


def classify(name: str) -> str:
    verb = name.split("_", 1)[0]
    if verb in READ_VERBS:
        return "read"
    if verb in WRITE_VERBS:
        return "write"
    return "unclassified"


def guard_report(source: str) -> dict:
    """Enforcement found in CODE, and guard words found only in PROSE, kept apart."""
    descriptions = " ".join(d["description"] for d in tools_in(source))
    code = TOOL_RE.sub("", source)  # attributes out: what is left is executable
    return {
        "enforced": len(ENFORCED_RE.findall(code)),
        "roles": sorted(set(ROLE_RE.findall(code))),
        "in_prose": sorted({w for w in ("confirm", "destructive", "audit", "permission")
                            if w in descriptions.lower()}),
    }


def summarise(sources: dict[str, str]) -> dict:
    """path -> source  ⇒  the surface, as counts plus the lists behind them."""
    tools: list[tuple[str, str, str]] = []
    enforced = 0
    roles: set[str] = set()
    prose: set[str] = set()
    for path, src in sorted(sources.items()):
        for t in tools_in(src):
            tools.append((path, t["name"], classify(t["name"])))
        g = guard_report(src)
        enforced += g["enforced"]
        roles.update(g["roles"])
        prose.update(g["in_prose"])
    return {
        "n_tools": len(tools),
        "reads": sum(1 for _, _, k in tools if k == "read"),
        "writes": sum(1 for _, _, k in tools if k == "write"),
        "unclassified": sorted(n for _, n, k in tools if k == "unclassified"),
        "ambiguous": sorted(n for _, n, _ in tools
                            if n.split("_", 1)[0] in AMBIGUOUS_VERBS),
        "files_with_enforcement": sum(
            1 for src in sources.values() if guard_report(src)["enforced"]),
        "enforcement_sites": enforced,
        "roles": sorted(roles),
        "guard_words_in_prose_only": sorted(prose),
        "tools": tools,
    }


if __name__ == "__main__":
    import os
    import sys

    if len(sys.argv) < 2:
        sys.stderr.write("usage: surface.py <dir-of-php-sources>\n")
        sys.exit(2)
    root = sys.argv[1]
    srcs = {}
    for fn in sorted(os.listdir(root)):
        if fn.endswith(".php"):
            with open(os.path.join(root, fn), encoding="utf-8", errors="replace") as fh:
                srcs[fn] = fh.read()
    if not srcs:
        sys.stderr.write("p191: 0 sources — a path fault, not an empty surface (P355)\n")
        sys.exit(2)
    s = summarise(srcs)
    print("measure\tvalue")
    for k in ("n_tools", "reads", "writes", "files_with_enforcement",
              "enforcement_sites"):
        print(f"{k}\t{s[k]}")
    print("roles\t" + ";".join(s["roles"]))
    print("guard_words_in_prose_only\t" + ";".join(s["guard_words_in_prose_only"]))
    print("verb-ambiguous tools\t" + ";".join(s["ambiguous"]))
    print("unclassified\t" + (";".join(s["unclassified"]) or "0"))
    print("\nfile\ttool\tkind")
    for path, name, kind in sorted(s["tools"], key=lambda t: t[1]):
        print(f"{path}\t{name}\t{kind}")
