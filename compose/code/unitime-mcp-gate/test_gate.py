#!/usr/bin/env python3
"""Verification by EXECUTION of the UniTime MCP gate. stdlib only.

Pass 42 proved the tool partition. Pass 45 (gap 93) re-audits that proof with the
four controls pass 44 had to invent for the SEB Server gate, plus a fifth that
only UniTime needs:

  (a) no route contains an unresolved ${...} placeholder;
  (b) every route is absolute, and the published URL carries the webapp context;
  (c) no row was manufactured -- the table holds the 26 implemented
      do<Verb>(ApiHelper) overrides, not the 60 live routes;
  (d) a route that is conditioned is recorded as conditioned (UniTime has no
      @ConditionalOn*; its analogue is a handler that refuses unless application
      properties are set);
  (e) a verb-crossing handler is refused by a FLOOR, not by policy: GET /api/script
      delegates to doPost, so no read/write allowlist can protect it.

    python3 test_gate.py
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate import (DEFAULT_CONTEXT, Gate, StaleTable, build_manifest,
                  default_allowlist, hard_deny, load_connectors)

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "connectors.tsv")
VERBS = ("Get", "Post", "Put", "Delete")
ok = True
checks = 0
failures = []


def check(label, got, want):
    global ok, checks
    checks += 1
    good = got == want
    ok = ok and good
    if not good:
        failures.append(label)
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")


conns = load_connectors(TSV)
tools = build_manifest(conns)

check("connectors read from tree", len(conns), 15)
check("tools in full manifest (connector x verb)", len(tools), 26)

# ---------------------------------------------------------------- audit controls
print("\n-- the four pass-44 controls, run against UniTime --")

# (a) no unresolved property placeholder, which is the defect that invalidated
#     every route SEB Server published. UniTime's routes are @Service literals.
check("(a) routes containing '${'", [c["route"] for c in conns if "${" in c["route"]], [])

# (b) absolute routes, and a published URL that includes the webapp context.
check("(b) non-absolute routes",
      [c["route"] for c in conns if not c["route"].startswith("/")], [])
check("(b) routes not under the web.xml servlet prefix",
      [c["route"] for c in conns if not c["route"].startswith("/api/")], [])
check("(b) tools whose published URL omits the context",
      [t["name"] for t in tools if not t["_url"].startswith(DEFAULT_CONTEXT + "/api/")], [])
check("(b) the route is DATA, not an f-string: it matches the @Service bean name",
      sorted({t["_url"] for t in tools})[:2],
      ["/UniTime/api/buildings", "/UniTime/api/class-info"])

# (c) nothing manufactured: 26 implemented overrides, not 15 x 4 = 60 routes.
check("(c) live HTTP routes (incl. the 501 fallbacks ApiConnector answers)",
      len(conns) * len(VERBS), 60)
check("(c) the table holds only implemented overrides", len(tools), 26)
check("(c) no verb outside the four servlet verbs",
      sorted({v for c in conns for v in c["verbs"]} - set(VERBS)), [])
check("(c) no row with an empty connector name or no verb",
      [c["cls"] for c in conns if not c["name"] or not c["verbs"]], [])
check("(c) no header or example row leaked into the data",
      [c["cls"] for c in conns if not c["cls"].endswith(("Connector", "Conntector"))], [])

# (d) a conditioned route is recorded as conditioned. UniTime conditions at
#     runtime on application properties, and it conditions a READ too.
guarded = [t["name"] for t in tools if t["_guarded"]]
check("(d) property-guarded tools are recorded", sorted(guarded),
      ["unitime.var-title-crs.get", "unitime.var-title-crs.post"])
check("(d) flagging is not hiding: the guarded read is still exposed",
      "unitime.var-title-crs.get" in default_allowlist(tools), True)

# ------------------------------------------------- (e) the verb-crossing floor
print("\n-- (e) the control only UniTime needs: the verb is not the write boundary --")
floor = hard_deny(tools)
check("(e) the floor is exactly GET /api/script", sorted(floor), ["unitime.script.get"])
check("(e) a crossing verb is a read by its HTTP verb",
      [t["_write"] for t in tools if t["_crossing"]], [False])
check("(e) the floor is outside the default allowlist",
      sorted(floor & default_allowlist(tools)), [])

hits = []


def upstream(name, args):
    hits.append(name)
    return {"content": [{"type": "text", "text": "ok"}]}


# An operator who explicitly names the crossing tool still cannot re-open it.
g_force = Gate(tools, {"unitime.script.get", "unitime.rooms.get"}, upstream)
check("(e) explicit allowlist cannot re-open the floor",
      [t["name"] for t in g_force.exposed()], ["unitime.rooms.get"])
r = g_force.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                    "params": {"name": "unitime.script.get", "arguments": {}}})
check("(e) forced script.get -> -32601", (r.get("error") or {}).get("code"), -32601)
check("(e) the forced call never reached upstream", hits, [])
check("(e) the refusal is logged as a floor decision, not a policy one",
      g_force.log[-1]["decision"], "floor")

# A stale table must fail loudly instead of inferring the route again.
stale = os.path.join(HERE, ".stale.tsv")
with open(stale, "w", encoding="utf-8") as fh:
    fh.write("RoomsConnector\trooms\tGet Post Put Delete \n")
try:
    load_connectors(stale)
    check("(e) a pass-42 3-column table is rejected", "accepted", "StaleTable")
except StaleTable:
    check("(e) a pass-42 3-column table is rejected", "StaleTable", "StaleTable")
finally:
    os.remove(stale)

# ------------------------------------------------------- the pass-42 assertions
print("\n-- the pass-42 partition proof, unchanged --")
allow = default_allowlist(tools)                 # deny 'script', reads only
g = Gate(tools, allow, upstream)

exposed = [t["name"] for t in g.exposed()]
check("tools/list is built from the allowlist", len(exposed), 13)
check("no write verb is exposed", [t for t in g.exposed() if t["_write"]], [])
check("no script tool is exposed", [n for n in exposed if ".script." in n], [])

must_block = ["unitime.script.post", "unitime.script.get",
              "unitime.rooms.post", "unitime.rooms.put", "unitime.rooms.delete",
              "unitime.buildings.post", "unitime.buildings.delete",
              "unitime.events.post", "unitime.events.delete"]
for i, name in enumerate(must_block):
    r = g.handle({"jsonrpc": "2.0", "id": i, "method": "tools/call",
                  "params": {"name": name, "arguments": {}}})
    code = (r.get("error") or {}).get("code")
    check(f"withheld {name} -> -32601", code, -32601)

check("NONE of the withheld calls reached upstream", hits, [])

r = g.handle({"jsonrpc": "2.0", "id": 99, "method": "tools/call",
              "params": {"name": "unitime.rooms.get", "arguments": {}}})
check("allowed rooms.get returns a result", "result" in r, True)
check("exactly one call reached upstream", hits, ["unitime.rooms.get"])

g0 = Gate(tools, set(), upstream)
check("empty allowlist -> 0 tools", len(g0.exposed()), 0)
r0 = g0.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                "params": {"name": "unitime.rooms.get", "arguments": {}}})
check("empty allowlist withholds even a read", (r0.get("error") or {}).get("code"), -32601)
check("upstream still untouched by empty-allowlist calls", hits, ["unitime.rooms.get"])

# ------------------------------------------------------- end-to-end over stdio
print("\n-- end-to-end over a real stdio subprocess --")
env = dict(os.environ, UNITIME_CONNECTORS=TSV,
           UNITIME_ALLOW="unitime.rooms.get,unitime.curricula.get,unitime.script.get")
reqs = [{"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
         "params": {"name": "unitime.script.post", "arguments": {}}},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
         "params": {"name": "unitime.script.get", "arguments": {}}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
         "params": {"name": "unitime.rooms.get", "arguments": {}}}]
p = subprocess.run([sys.executable, os.path.join(HERE, "gate.py")],
                   input="\n".join(json.dumps(r) for r in reqs),
                   capture_output=True, text=True, env=env, timeout=60)
out = [json.loads(l) for l in p.stdout.strip().splitlines()]
check("stdio: tools/list honours the allowlist MINUS the floor",
      len(out[0]["result"]["tools"]), 2)
check("stdio: script.post refused -32601", out[1]["error"]["code"], -32601)
check("stdio: script.get refused -32601 THOUGH it was in UNITIME_ALLOW",
      out[2]["error"]["code"], -32601)
check("stdio: rooms.get served", "result" in out[3], True)
check("stdio: the published URL carries the context",
      out[0]["result"]["tools"][0]["description"].split()[1].startswith("/UniTime/api/"), True)
check("stdio: no private key leaked into tools/list",
      [k for t in out[0]["result"]["tools"] for k in t if k.startswith("_")], [])

print()
print(f"{checks - len(failures)}/{checks} checks passed")
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
