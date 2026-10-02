#!/usr/bin/env python3
"""Executable proof for the SEB Server gate (pase 43, action 1).

Requirement from the pase-42 handoff: prove BY EXECUTION that the WRITE
operations of /exam, /lms-setup and /useraccount are withheld with -32601,
and likewise those of /batch-action. Runs against a stub upstream: SEB Server
is never started, and the stub counts every call that reaches it so "withheld"
means "never dispatched", not merely "answered with an error".

    python3 test_gate.py
"""
import sys
from gate import (Gate, build_manifest, default_allowlist, load_operations,
                  DENY_ENDPOINTS, WRITE_VERBS)

TARGETS = ("/exam", "/lms-setup", "/useraccount", "/batch-action")
checks, failures = 0, []


def check(cond, label):
    global checks
    checks += 1
    if not cond:
        failures.append(label)
    print(f"  {'ok  ' if cond else 'FAIL'}  {label}")


def main():
    ops = load_operations("operations.tsv")
    tools = build_manifest(ops)
    allow = default_allowlist(tools)

    reached = []
    gate = Gate(tools, allow, lambda n, a: reached.append(n) or {"ok": True})

    print(f"operations read from the tree: {len(ops)}")
    print(f"tools in the manifest:        {len(tools)}")
    print(f"tools exposed by tools/list:  {len(gate.exposed())}\n")

    # 1. every write on the four target endpoints is refused with -32601
    print("1. writes on the target endpoints are refused with -32601")
    writes = [t for t in tools
              if t["_endpoint"] in TARGETS and t["_verb"] in WRITE_VERBS]
    check(len(writes) > 0, f"the manifest actually contains writes to test ({len(writes)})")
    bad_code = [t["name"] for t in writes
                if gate.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                "params": {"name": t["name"]}}
                               ).get("error", {}).get("code") != -32601]
    check(not bad_code, f"all {len(writes)} write tools answered -32601"
                        + (f" (offenders: {bad_code[:3]})" if bad_code else ""))

    # 2. the refusal happened before the upstream
    print("\n2. the refusal is before the upstream, not after it")
    check(reached == [], f"no write reached the stub upstream (reached={len(reached)})")
    check(gate.upstream_calls == 0, "gate's own upstream counter is 0")

    # 3. withheld tools are not advertised either
    print("\n3. a withheld tool is not advertised by tools/list")
    listed = {t["name"] for t in
              gate.handle({"jsonrpc": "2.0", "id": 2,
                           "method": "tools/list"})["result"]["tools"]}
    check(not (listed & {t["name"] for t in writes}),
          "no write tool appears in tools/list")
    check(all(not k.startswith("_")
              for t in gate.handle({"jsonrpc": "2.0", "id": 3,
                                    "method": "tools/list"})["result"]["tools"]
              for k in t),
          "no internal _-prefixed key leaks into tools/list")

    # 4. /batch-action is denied outright, reads included
    print("\n4. /batch-action is denied outright (named deny, not just writes)")
    ba = [t for t in tools if t["_endpoint"] in DENY_ENDPOINTS]
    check(len(ba) > 0, f"the manifest contains /batch-action tools ({len(ba)})")
    check(all(t["name"] not in allow for t in ba),
          f"all {len(ba)} /batch-action tools are outside the allowlist, "
          "including the reads")

    # 5. the gate is not refusing everything — reads still work
    print("\n5. the gate is not vacuous: legitimate reads still pass")
    reads = [t for t in tools
             if t["_endpoint"] in TARGETS and not t["_write"]
             and t["_endpoint"] not in DENY_ENDPOINTS]
    ok = [t for t in reads
          if "result" in gate.handle({"jsonrpc": "2.0", "id": 4,
                                      "method": "tools/call",
                                      "params": {"name": t["name"]}})]
    check(len(ok) == len(reads) and len(reads) > 0,
          f"all {len(reads)} read tools dispatched to the upstream")
    check(gate.upstream_calls == len(reads),
          f"upstream saw exactly the {len(reads)} reads and nothing else")

    # 6. an unknown tool name is refused the same way
    print("\n6. an unknown name is refused identically")
    check(gate.handle({"jsonrpc": "2.0", "id": 5, "method": "tools/call",
                       "params": {"name": "seb.exam.post.invented"}}
                      )["error"]["code"] == -32601,
          "an invented tool name also yields -32601")

    print(f"\n{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES:")
        for f in failures:
            print("  -", f)
        return 1
    print("ACTION 1 VERIFIED: the write surface of /exam, /lms-setup, "
          "/useraccount and all of /batch-action is withheld with -32601,\n"
          "and no withheld call reached the upstream.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
