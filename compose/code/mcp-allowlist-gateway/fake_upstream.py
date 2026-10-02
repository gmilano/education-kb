#!/usr/bin/env python3
"""A stand-in for `frappe-mcp-server`'s surface. stdlib only.

Seven tools, the same seven P85's verification table uses. Two of them are the
reason P85 exists: `call_method` executes arbitrary whitelisted server methods
and `delete_document` deletes, both over an academic ERP, with no partition by
role.

It counts its own executions in `MCP_UPSTREAM_COUNTER`, because "the call was
refused" and "the call never reached the upstream" are DIFFERENT claims and only
the second one matters. A gateway that refuses the client after forwarding the
call has already done the damage.
"""
import json, os, sys

TOOLS = [
    {"name": "get_document", "description": "Read one document",
     "inputSchema": {"type": "object", "properties": {"doctype": {"type": "string"}}}},
    {"name": "list_documents", "description": "List documents",
     "inputSchema": {"type": "object", "properties": {"doctype": {"type": "string"}}}},
    {"name": "get_doctype_schema", "description": "Read a doctype schema",
     "inputSchema": {"type": "object", "properties": {"doctype": {"type": "string"}}}},
    {"name": "update_document", "description": "Update a document",
     "inputSchema": {"type": "object", "properties": {"name": {"type": "string"}}}},
    {"name": "delete_document", "description": "Delete a document",
     "inputSchema": {"type": "object", "properties": {"name": {"type": "string"}}}},
    {"name": "call_method", "description": "Call an arbitrary whitelisted method",
     "inputSchema": {"type": "object", "properties": {"method": {"type": "string"}}}},
    {"name": "create_document", "description": "Create a document",
     "inputSchema": {"type": "object", "properties": {"doctype": {"type": "string"}}}},
]

COUNTER = os.environ.get("MCP_UPSTREAM_COUNTER", "").strip()


def bump(name):
    if not COUNTER:
        return
    with open(COUNTER, "a", encoding="utf-8") as fh:
        fh.write(name + "\n")


def handle(req):
    m, rid = req.get("method"), req.get("id")
    if m == "initialize":
        return {"jsonrpc": "2.0", "id": rid,
                "result": {"protocolVersion": "2024-11-05",
                           "serverInfo": {"name": "fake-frappe", "version": "0.1.0"},
                           "capabilities": {"tools": {}}}}
    if m == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    if m == "tools/call":
        name = (req.get("params") or {}).get("name", "")
        bump(name)
        return {"jsonrpc": "2.0", "id": rid,
                "result": {"content": [{"type": "text", "text": f"upstream ran {name}"}]}}
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": f"Method not found: {m}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        sys.stdout.write(json.dumps(handle(json.loads(line))) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
