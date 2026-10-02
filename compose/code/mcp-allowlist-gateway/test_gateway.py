#!/usr/bin/env python3
"""Verification by EXECUTION of the generic P85 gateway. stdlib only.

    python3 test_gateway.py

Four blocks, and the third is the one that justifies the piece:

  (A) P85's published verification table, converted from prose into assertions.
      Seven rows, run against a fake `frappe-mcp-server` over a real stdio
      subprocess, with the upstream counting its OWN executions -- so
      "no llega al upstream" is measured at the upstream, not inferred at the
      gateway.
  (B) The floor of pass 45, which P85's inline code did NOT have: a name in
      MCP_HARD_DENY is refused THOUGH an operator put it in MCP_ALLOWLIST.
  (C) EQUIVALENCE with the two concrete gates. The extraction is only honest if
      the core reproduces their decisions exactly, so this re-derives the
      partition of `unitime-mcp-gate` (46 tools) and `sebserver-mcp-gate`
      (341 operations) through `policy.Policy` and demands the same answer
      tool-for-tool. This is the control that pass 31 asked for: a method that
      declares an extraction must also be run against a case already known.
  (D) The anti-glob and private-key controls.
"""
import importlib.util, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from policy import EXPOSED, FLOOR, WITHHELD, Policy, hard_deny, parse_allowlist

ok = True
count = 0


def check(label, got, want):
    global ok, count
    count += 1
    good = got == want
    if not good:
        ok = False
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")


def check_same(label, got, want):
    """Set equality, reported as a digest: printing 341 tool names hides the
    answer instead of showing it."""
    global ok, count
    count += 1
    g, w = sorted(got), sorted(want)
    good = g == w
    if not good:
        ok = False
        only_g, only_w = set(g) - set(w), set(w) - set(g)
        print(f"FAIL  {label}: {len(g)} vs {len(w)}; "
              f"only-got={sorted(only_g)[:5]} only-want={sorted(only_w)[:5]}")
    else:
        print(f"PASS  {label}: {len(g)} names, identical")
    return good


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_gateway(allow, hard_deny_names="", calls=()):
    """Drive gateway.py over a real subprocess against fake_upstream.py."""
    env = dict(os.environ)
    env["MCP_ALLOWLIST"] = allow
    env["MCP_HARD_DENY"] = hard_deny_names
    fd, counter = tempfile.mkstemp(prefix="upstream-counter-")
    os.close(fd)
    os.unlink(counter)
    env["MCP_UPSTREAM_COUNTER"] = counter
    env["MCP_AUDIT_LOG"] = ""
    reqs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}]
    for i, name in enumerate(calls, start=3):
        reqs.append({"jsonrpc": "2.0", "id": i, "method": "tools/call",
                     "params": {"name": name, "arguments": {}}})
    p = subprocess.run(
        [sys.executable, os.path.join(HERE, "gateway.py"), "--",
         sys.executable, os.path.join(HERE, "fake_upstream.py")],
        input="\n".join(json.dumps(r) for r in reqs),
        capture_output=True, text=True, env=env, timeout=120)
    out = [json.loads(l) for l in p.stdout.strip().splitlines() if l.strip()]
    ran = []
    if os.path.exists(counter):
        ran = [l.strip() for l in open(counter) if l.strip()]
        os.unlink(counter)
    return out, ran


THREE = "get_document,list_documents,get_doctype_schema"

print("-- (A) P85's verification table, as assertions --")
out, ran = run_gateway(THREE, calls=["get_document", "delete_document", "call_method"])
by_id = {m["id"]: m for m in out}

check("tools/list with an allowlist of 3: upstream 7 -> exposed",
      len(by_id[2]["result"]["tools"]), 3)
check("tools/list exposes exactly the three named",
      sorted(t["name"] for t in by_id[2]["result"]["tools"]),
      ["get_doctype_schema", "get_document", "list_documents"])
check("tools/call of an allowed tool reaches the upstream and runs",
      "result" in by_id[3], True)
check("tools/call delete_document refused -32601",
      by_id[4]["error"]["code"], -32601)
check("tools/call call_method refused -32601",
      by_id[5]["error"]["code"], -32601)
check("neither withheld call REACHED the upstream (counted at the upstream)",
      [r for r in ran if r in ("delete_document", "call_method")], [])
check("total executions at the upstream: only the allowed one", ran, ["get_document"])
check("initialize passes through untouched",
      by_id[1]["result"]["serverInfo"]["name"], "fake-frappe")

print("\n-- (A continued) default deny: the empty allowlist --")
out0, ran0 = run_gateway("", calls=["get_document", "delete_document", "call_method"])
by_id0 = {m["id"]: m for m in out0}
check("empty MCP_ALLOWLIST exposes 0 tools", len(by_id0[2]["result"]["tools"]), 0)
check("empty MCP_ALLOWLIST blocks all three calls",
      [by_id0[i]["error"]["code"] for i in (3, 4, 5)], [-32601] * 3)
check("empty MCP_ALLOWLIST: nothing reached the upstream", ran0, [])

print("\n-- (B) the floor of pass 45, which P85's inline code did not have --")
outf, ranf = run_gateway(THREE + ",delete_document",
                         hard_deny_names="delete_document",
                         calls=["delete_document", "get_document"])
by_idf = {m["id"]: m for m in outf}
check("a floored tool is NOT advertised though it is in MCP_ALLOWLIST",
      [t["name"] for t in by_idf[2]["result"]["tools"] if t["name"] == "delete_document"],
      [])
check("a floored tool is REFUSED though it is in MCP_ALLOWLIST",
      by_idf[3]["error"]["code"], -32601)
check("the floored call did not reach the upstream", "delete_document" in ranf, False)
check("the floor does not disturb the rest", "result" in by_idf[4], True)
check("the refusal never advertises the floor in data.allowed",
      "delete_document" in by_idf[3]["error"]["data"]["allowed"], False)

print("\n-- (C) EQUIVALENCE with the two concrete gates --")
uni = load("uni_gate", os.path.join(HERE, "..", "unitime-mcp-gate", "gate.py"))
uni_tools = uni.build_manifest(
    uni.load_connectors(os.path.join(HERE, "..", "unitime-mcp-gate", "connectors.tsv")))
uni_allow = uni.default_allowlist(uni_tools)
uni_gate = uni.Gate(uni_tools, uni_allow, lambda n, a: {})
uni_pol = Policy(uni_tools, uni_allow,
                 floor=hard_deny(uni_tools, predicate=lambda t: t["_crossing"]))
# 26, not 46: the table holds the implemented do<Verb>(ApiHelper) overrides,
# not the 60 live routes. (Pass 47's prose cites "(46)" for this directory; that
# is this suite's CHECK count, not its tool count -- corrected in pass 48.)
check("UniTime: manifest size agrees", len(uni_tools), 26)
check_same("UniTime: policy reproduces the gate's exposed set tool-for-tool",
           [t["name"] for t in uni_pol.exposed()],
           [t["name"] for t in uni_gate.exposed()])
check("UniTime: policy reproduces the gate's floor",
      uni_pol.floor, uni.hard_deny(uni_tools))
check("UniTime: the floor is non-empty, so the agreement is not vacuous",
      len(uni_pol.floor) > 0, True)
uni_disagree = [t["name"] for t in uni_tools
                if (uni_pol.decide(t["name"]) == EXPOSED)
                != (t["name"] in uni_gate.allow)]
check("UniTime: zero per-tool disagreements over all 26", uni_disagree, [])

seb = load("seb_gate", os.path.join(HERE, "..", "sebserver-mcp-gate", "gate.py"))
seb_ops = seb.load_operations(
    os.path.join(HERE, "..", "sebserver-mcp-gate", "operations.tsv"))
seb_tools = seb.build_manifest(seb_ops)
seb_allow = seb.default_allowlist(seb_tools)
seb_gate = seb.Gate(seb_tools, seb_allow, lambda n, a: {})
# seb-server states its floor as route metadata (dead + conditional + named-deny)
# rather than as a crossing flag, so the predicate is the disjunction of those.
seb_pol = Policy(seb_tools, seb_allow, floor=hard_deny(
    seb_tools,
    predicate=lambda t: t["_source"] in seb.DEAD_SOURCES
    or t["_conditional"] or t["_endpoint"] in seb.DENY_ENDPOINTS))
check("seb-server: 341 operations loaded", len(seb_ops), 341)
check_same("seb-server: policy reproduces the gate's exposed set tool-for-tool",
           [t["name"] for t in seb_pol.exposed()],
           [t["name"] for t in seb_gate.exposed()])
seb_disagree = [t["name"] for t in seb_tools
                if (seb_pol.decide(t["name"]) == EXPOSED)
                != (t["name"] in seb_gate.allow)]
check("seb-server: zero per-tool disagreements over all 341", seb_disagree, [])
check("seb-server: the whole write surface stays withheld",
      [t["name"] for t in seb_pol.exposed() if t["_write"]], [])
check("seb-server: the floor is non-empty, so the agreement is not vacuous",
      len(seb_pol.floor) > 0, True)

print("\n-- (D) exact names, and no leak of decision metadata --")
pol = Policy([{"name": "preview_submit_assignment"}, {"name": "submit_assignment"},
              {"name": "delete_document"}],
             parse_allowlist("preview_submit_assignment"))
check("an allowlisted prefix does NOT admit the shorter name",
      pol.decide("submit_assignment"), WITHHELD)
check("the allowlisted exact name is exposed",
      pol.decide("preview_submit_assignment"), EXPOSED)
check("a glob in the allowlist matches nothing literally named otherwise",
      Policy([{"name": "delete_document"}], parse_allowlist("delete_*")).decide(
          "delete_document"), WITHHELD)
check("parse_allowlist: unset and empty are the same empty allowlist",
      (parse_allowlist(None), parse_allowlist("")), (frozenset(), frozenset()))
check("parse_allowlist tolerates padding and blanks",
      parse_allowlist(" a , ,b "), frozenset({"a", "b"}))
check("no private key reaches tools/list",
      [k for t in by_id[2]["result"]["tools"] for k in t if k.startswith("_")], [])
check("public() strips decision metadata",
      [k for t in uni_pol.public() for k in t if k.startswith("_")], [])
check("floor decision is distinguishable from a plain withholding",
      Policy([{"name": "x"}], {"x"}, floor={"x"}).decide("x"), FLOOR)

print()
print(f"{count} checks run")
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
