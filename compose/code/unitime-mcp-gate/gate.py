#!/usr/bin/env python3
"""UniTime MCP allowlist gate — stdlib only.

Wraps UniTime's 15 named API connectors (JavaSource/org/unitime/timetable/api/connectors/,
Apache-2.0) as MCP tools, and partitions them with the P85 allowlist pattern:
tools/list is built FROM THE ALLOWLIST, and a withheld tool is refused with
JSON-RPC -32601 WITHOUT the call ever reaching the upstream.

Connector name + verbs are read from the tree, not from documentation.
"""
import json, sys, os

VERB_HTTP = {"Get": "GET", "Post": "POST", "Put": "PUT", "Delete": "DELETE"}
READ_VERBS = {"Get"}


def load_connectors(path):
    out = []
    for line in open(path):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3 or not parts[1]:
            continue
        cls, name, verbs = parts[0], parts[1], parts[2].split()
        out.append((cls, name, verbs))
    return out


def build_manifest(connectors):
    """One tool per (connector, verb). 26 for UniTime's 15 connectors."""
    tools = []
    for cls, name, verbs in connectors:
        for v in verbs:
            tools.append({
                "name": f"unitime.{name}.{v.lower()}",
                "description": f"{VERB_HTTP[v]} /api/{name} (UniTime {cls})",
                "_connector": name,
                "_verb": v,
                "_write": v not in READ_VERBS,
                "inputSchema": {
                    "type": "object",
                    "properties": {"params": {"type": "object"}},
                },
            })
    return tools


def default_allowlist(tools, deny_connectors=("script",), read_only=True):
    """Policy: deny named connectors outright; otherwise reads only."""
    allow = []
    for t in tools:
        if t["_connector"] in deny_connectors:
            continue
        if read_only and t["_write"]:
            continue
        allow.append(t["name"])
    return set(allow)


class Gate:
    def __init__(self, tools, allowlist, upstream):
        self.tools = tools
        self.allow = set(allowlist)
        self.upstream = upstream
        self.log = []

    def exposed(self):
        return [t for t in self.tools if t["name"] in self.allow]

    def handle(self, req):
        m, rid = req.get("method"), req.get("id")
        if m == "initialize":
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"protocolVersion": "2024-11-05",
                               "serverInfo": {"name": "unitime-gate", "version": "0.1.0"},
                               "capabilities": {"tools": {}}}}
        if m == "tools/list":
            pub = [{k: v for k, v in t.items() if not k.startswith("_")}
                   for t in self.exposed()]
            return {"jsonrpc": "2.0", "id": rid, "result": {"tools": pub}}
        if m == "tools/call":
            name = (req.get("params") or {}).get("name")
            if name not in self.allow:
                self.log.append({"tool": name, "decision": "withheld"})
                return {"jsonrpc": "2.0", "id": rid,
                        "error": {"code": -32601,
                                  "message": f"Method not found: {name}"}}
            self.log.append({"tool": name, "decision": "exposed"})
            return {"jsonrpc": "2.0", "id": rid,
                    "result": self.upstream(name, (req.get("params") or {}).get("arguments") or {})}
        return {"jsonrpc": "2.0", "id": rid,
                "error": {"code": -32601, "message": f"Method not found: {m}"}}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    tsv = os.environ.get("UNITIME_CONNECTORS",
                         os.path.join(here, "connectors.tsv"))
    tools = build_manifest(load_connectors(tsv))
    env = os.environ.get("UNITIME_ALLOW")
    allow = set(env.split(",")) if env is not None else default_allowlist(tools)

    def upstream(name, args):  # real deployment: HTTP to /api/<connector>?token=...
        return {"content": [{"type": "text", "text": f"upstream {name}"}]}

    g = Gate(tools, allow, upstream)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        sys.stdout.write(json.dumps(g.handle(json.loads(line))) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
