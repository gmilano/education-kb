#!/usr/bin/env python3
"""Verification by EXECUTION of the UniTime MCP gate. stdlib only."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate import load_connectors, build_manifest, default_allowlist, Gate

HERE_ = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE_, "connectors.tsv")
HERE = os.path.dirname(os.path.abspath(__file__))
ok = True

def check(label, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")

conns = load_connectors(TSV)
tools = build_manifest(conns)

check("connectors read from tree", len(conns), 15)
check("tools in full manifest (connector x verb)", len(tools), 26)

# --- upstream stub that RECORDS every call it receives
hits = []
def upstream(name, args):
    hits.append(name)
    return {"content": [{"type": "text", "text": "ok"}]}

allow = default_allowlist(tools)                 # deny 'script', reads only
g = Gate(tools, allow, upstream)

exposed = [t["name"] for t in g.exposed()]
check("tools/list is built from the allowlist", len(exposed), 13)
check("no write verb is exposed", [t for t in g.exposed() if t["_write"]], [])
check("no script tool is exposed", [n for n in exposed if ".script." in n], [])

# --- the four calls that MUST be withheld
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

# --- an allowed call DOES reach upstream
r = g.handle({"jsonrpc": "2.0", "id": 99, "method": "tools/call",
              "params": {"name": "unitime.rooms.get", "arguments": {}}})
check("allowed rooms.get returns a result", "result" in r, True)
check("exactly one call reached upstream", hits, ["unitime.rooms.get"])

# --- empty allowlist exposes zero tools
g0 = Gate(tools, set(), upstream)
check("empty allowlist -> 0 tools", len(g0.exposed()), 0)
r0 = g0.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                "params": {"name": "unitime.rooms.get", "arguments": {}}})
check("empty allowlist withholds even a read", (r0.get("error") or {}).get("code"), -32601)
check("upstream still untouched by empty-allowlist calls", hits, ["unitime.rooms.get"])

# --- end-to-end over real stdio subprocess
env = dict(os.environ, UNITIME_CONNECTORS=TSV,
           UNITIME_ALLOW="unitime.rooms.get,unitime.curricula.get")
reqs = [{"jsonrpc":"2.0","id":1,"method":"tools/list"},
        {"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"unitime.script.post","arguments":{}}},
        {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"unitime.rooms.get","arguments":{}}}]
p = subprocess.run([sys.executable, os.path.join(HERE, "gate.py")],
                   input="\n".join(json.dumps(r) for r in reqs),
                   capture_output=True, text=True, env=env, timeout=60)
out = [json.loads(l) for l in p.stdout.strip().splitlines()]
check("stdio: tools/list honours explicit allowlist", len(out[0]["result"]["tools"]), 2)
check("stdio: script.post refused -32601", out[1]["error"]["code"], -32601)
check("stdio: rooms.get served", "result" in out[2], True)

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
