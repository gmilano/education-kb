#!/usr/bin/env python3
"""UniTime MCP allowlist gate — stdlib only.

Wraps UniTime's 15 named API connectors (JavaSource/org/unitime/timetable/api/connectors/,
Apache-2.0) as MCP tools, and partitions them with the P85 allowlist pattern:
tools/list is built FROM THE ALLOWLIST, and a withheld tool is refused with
JSON-RPC -32601 WITHOUT the call ever reaching the upstream.

Pass 45 (audit of gap 93) changed three things, all of them because the pass-42
version inferred what it should have read:

  1. The route is DATA, read from connectors.tsv, which carries the @Service bean
     name. ApiServlet.getConnector() does getBean(servletPath + pathInfo), so the
     bean name IS the route. getName() only feeds getCacheMode(). The old gate
     pasted "/api/" + getName() into an f-string; it was right by coincidence in
     15 of 15 connectors and unverified in all 15.
  2. The deployed URL needs the webapp context (pom.xml ships <warName>UniTime</warName>),
     so the gate carries UNITIME_CONTEXT and publishes <context>+route.
  3. HARD_DENY is a floor, not a policy: a verb whose handler crosses into another
     verb is refused even when an operator names it in UNITIME_ALLOW. GET /api/script
     with ?script= delegates to doPost and with ?delete= removes a queue item, so for
     that connector the HTTP verb is not the write boundary and a read/write
     allowlist cannot protect it.
"""
import json
import os
import sys

VERB_HTTP = {"Get": "GET", "Post": "POST", "Put": "PUT", "Delete": "DELETE"}
READ_VERBS = {"Get"}
DEFAULT_CONTEXT = "/UniTime"   # pom.xml <warName>; override with UNITIME_CONTEXT


class StaleTable(Exception):
    """connectors.tsv predates the route column. Fail loudly, never infer."""


def load_connectors(path):
    """Parse the 6-column TSV: class, route, name, verbs, crossing, guarded."""
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 6:
            raise StaleTable(
                f"{path}: {len(parts)} columns, expected 6 "
                "(class, route, name, verbs, crossing, guarded). "
                "Regenerate it with extract_surface.py -- do not infer the route."
            )
        cls, route, name, verbs, crossing, guarded = parts[:6]
        if not route.startswith("/") or "${" in route:
            raise StaleTable(f"{path}: {cls} route {route!r} is not an absolute literal")
        out.append({
            "cls": cls,
            "route": route,
            "name": name,
            "verbs": verbs.split(),
            "crossing": [] if crossing == "-" else crossing.split(),
            "guarded": [] if guarded == "-" else guarded.split(),
        })
    return out


def build_manifest(connectors, context=None):
    """One tool per implemented (connector, verb). 26 for UniTime's 15 connectors.

    A verb a connector does not override is NOT in here: the route is live and
    answers 501 from ApiConnector, but there is nothing to expose.
    """
    ctx = DEFAULT_CONTEXT if context is None else context
    tools = []
    for c in connectors:
        for v in c["verbs"]:
            tools.append({
                "name": f"unitime.{c['name']}.{v.lower()}",
                "description": f"{VERB_HTTP[v]} {ctx}{c['route']} (UniTime {c['cls']})",
                "_connector": c["name"],
                "_route": c["route"],
                "_url": ctx + c["route"],
                "_verb": v,
                "_write": v not in READ_VERBS,
                "_crossing": v in c["crossing"],
                "_guarded": v in c["guarded"],
                "inputSchema": {
                    "type": "object",
                    "properties": {"params": {"type": "object"}},
                },
            })
    return tools


def hard_deny(tools):
    """The floor: tools no allowlist may re-open. Verb-crossing handlers."""
    return {t["name"] for t in tools if t["_crossing"]}


def default_allowlist(tools, deny_connectors=("script",), read_only=True):
    """Policy: deny named connectors outright; otherwise reads only."""
    floor = hard_deny(tools)
    allow = []
    for t in tools:
        if t["name"] in floor:
            continue
        if t["_connector"] in deny_connectors:
            continue
        if read_only and t["_write"]:
            continue
        allow.append(t["name"])
    return set(allow)


class Gate:
    def __init__(self, tools, allowlist, upstream):
        self.tools = tools
        self.floor = hard_deny(tools)
        self.allow = set(allowlist) - self.floor
        self.upstream = upstream
        self.log = []

    def exposed(self):
        return [t for t in self.tools if t["name"] in self.allow]

    def handle(self, req):
        m, rid = req.get("method"), req.get("id")
        if m == "initialize":
            return {"jsonrpc": "2.0", "id": rid,
                    "result": {"protocolVersion": "2024-11-05",
                               "serverInfo": {"name": "unitime-gate", "version": "0.2.0"},
                               "capabilities": {"tools": {}}}}
        if m == "tools/list":
            pub = [{k: v for k, v in t.items() if not k.startswith("_")}
                   for t in self.exposed()]
            return {"jsonrpc": "2.0", "id": rid, "result": {"tools": pub}}
        if m == "tools/call":
            name = (req.get("params") or {}).get("name")
            if name not in self.allow:
                self.log.append({"tool": name,
                                 "decision": "floor" if name in self.floor else "withheld"})
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
    tsv = os.environ.get("UNITIME_CONNECTORS", os.path.join(here, "connectors.tsv"))
    ctx = os.environ.get("UNITIME_CONTEXT", DEFAULT_CONTEXT)
    tools = build_manifest(load_connectors(tsv), context=ctx)
    env = os.environ.get("UNITIME_ALLOW")
    allow = set(env.split(",")) if env is not None else default_allowlist(tools)

    def upstream(name, args):  # real deployment: HTTP to <context>/api/<connector>?token=...
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
