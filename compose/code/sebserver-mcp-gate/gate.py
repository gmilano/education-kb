#!/usr/bin/env python3
"""SEB Server MCP allowlist gate — stdlib only.

Second instance of the P85 allowlist pattern (the first is ../unitime-mcp-gate).
Wraps SEB Server's REST surface (SafeExamBrowser/seb-server, Apache-2.0) as MCP
tools and partitions them so that:

  * tools/list is built FROM THE ALLOWLIST, so a withheld tool is not advertised;
  * a withheld tools/call is refused with JSON-RPC -32601 WITHOUT the call ever
    reaching the upstream (the upstream counter proves it).

Everything is read from the tree, not from documentation:

  * endpoints.tsv  — the 42 `*_ENDPOINT` constants of gbl/api/API.java @ master
  * operations.tsv — per-controller operations, `own` (the controller's own
    @RequestMapping) plus `inherited` (the CRUD surface measured on
    EntityController / ActivatableEntityController)

Why the allowlist cannot be derived from route discovery
-------------------------------------------------------
ReadonlyEntityController KEEPS the inherited PUT/POST/DELETE @RequestMapping
annotations and throws AccessDeniedException in the body. The route therefore
still exists and still advertises itself; the refusal happens at runtime, deep
in the controller. A generator that trusts the annotations would emit write
tools that look legitimate. So the gate denies BY NAME, never by discovery.
"""
import json, os, sys

WRITE_VERBS = {"POST", "PUT", "DELETE", "PATCH"}
# Named-deny, the analogue of UniTime's `script` connector in P85: /batch-action
# is a bulk-action executor — one call fans out to many entities.
DENY_ENDPOINTS = ("/batch-action",)


def load_operations(path):
    ops = []
    for line in open(path):
        if line.startswith("#") or not line.strip():
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 6:
            continue
        endpoint, controller, base_class, verb, segment, source = parts[:6]
        ops.append({
            "endpoint": endpoint, "controller": controller,
            "base_class": base_class, "verb": verb,
            "segment": segment, "source": source,
        })
    return ops


def _slug(op):
    seg = op["segment"].replace("(root)", "root")
    for ch in "+ /{}":
        seg = seg.replace(ch, "_")
    return seg.strip("_").lower() or "root"


def build_manifest(ops):
    """One tool per (endpoint, verb, path segment, source). Names are unique."""
    tools, seen = [], {}
    for op in ops:
        stem = f"seb{op['endpoint'].replace('/', '.')}.{op['verb'].lower()}.{_slug(op)}"
        seen[stem] = seen.get(stem, 0) + 1
        name = stem if seen[stem] == 1 else f"{stem}~{seen[stem]}"
        tools.append({
            "name": name,
            "description": f"{op['verb']} {op['endpoint']} "
                           f"({op['controller']}, {op['source']})",
            "_endpoint": op["endpoint"],
            "_verb": op["verb"],
            "_write": op["verb"] in WRITE_VERBS,
            "_source": op["source"],
            "inputSchema": {"type": "object",
                            "properties": {"params": {"type": "object"}}},
        })
    return tools


def default_allowlist(tools, deny_endpoints=DENY_ENDPOINTS, read_only=True):
    """Policy: deny named endpoints outright; otherwise reads only."""
    allow = set()
    for t in tools:
        if t["_endpoint"] in deny_endpoints:
            continue
        if read_only and t["_write"]:
            continue
        allow.add(t["name"])
    return allow


class Gate:
    def __init__(self, tools, allowlist, upstream):
        self.tools = tools
        self.allow = set(allowlist)
        self.upstream = upstream
        self.log = []
        self.upstream_calls = 0

    def exposed(self):
        return [t for t in self.tools if t["name"] in self.allow]

    def handle(self, req):
        m, rid = req.get("method"), req.get("id")
        if m == "initialize":
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"protocolVersion": "2024-11-05",
                               "serverInfo": {"name": "sebserver-gate",
                                              "version": "0.1.0"},
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
            self.upstream_calls += 1
            return {"jsonrpc": "2.0", "id": rid,
                    "result": self.upstream(
                        name, (req.get("params") or {}).get("arguments") or {})}
        return {"jsonrpc": "2.0", "id": rid,
                "error": {"code": -32601, "message": f"Method not found: {m}"}}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ops = load_operations(os.environ.get(
        "SEB_OPERATIONS", os.path.join(here, "operations.tsv")))
    tools = build_manifest(ops)
    env = os.environ.get("SEB_ALLOW")
    allow = set(env.split(",")) if env is not None else default_allowlist(tools)

    def upstream(name, args):  # real deployment: HTTP to the SEB Server webservice
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
