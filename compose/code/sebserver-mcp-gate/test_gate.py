#!/usr/bin/env python3
"""Executable proof for the SEB Server gate (pase 44, action 1).

The pase-43 version proved the gate over FOUR endpoints. Action 1 of the pase-43
handoff asked for the whole service, so this version runs over all 31
@RestController classes and additionally asserts the four defects that the
re-extraction found, so a regression cannot reintroduce them silently:

  * every endpoint is absolute (the `${...}` admin prefix is resolved);
  * the composed `*_ENDPOINT` constants are present (the OAuth surface above all);
  * the routes ReadonlyEntityController leaves live are never advertised;
  * a controller behind @ConditionalOn* is never advertised.

Runs against a stub upstream: SEB Server is never started, and the stub counts
every call that reaches it, so "withheld" means "never dispatched", not merely
"answered with an error".

    python3 test_gate.py
"""
import re
import sys
from collections import Counter

from gate import (DEAD_SOURCES, DENY_ENDPOINTS, WRITE_VERBS, Gate,
                  build_manifest, default_allowlist, load_operations)

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

    endpoints = {op["endpoint"] for op in ops}
    controllers = {op["controller"] for op in ops}
    print(f"operations read from the tree: {len(ops)}")
    print(f"controllers covered:          {len(controllers)}")
    print(f"distinct endpoints:           {len(endpoints)}")
    print(f"tools in the manifest:        {len(tools)}")
    print(f"tools exposed by tools/list:  {len(gate.exposed())}")
    print(f"by source:                    {dict(Counter(o['source'] for o in ops))}\n")

    # 0. the table covers the service, not a sample
    print("0. the table covers the whole service")
    check(len(controllers) >= 31,
          f"all 31 @RestController classes are present ({len(controllers)})")
    check(len(ops) > 300, f"the surface is the service, not four endpoints ({len(ops)} ops)")

    # 1. every endpoint is an absolute, fully resolved path
    print("\n1. every endpoint is absolute and fully resolved")
    rel = [e for e in endpoints if not e.startswith("/")]
    check(not rel, f"no relative endpoint remains (offenders: {sorted(rel)[:3]})")
    unresolved = [e for e in endpoints if "${" in e or re.search(r"\{[a-z.]+\}", e)]
    check(not unresolved,
          f"no unresolved property placeholder (offenders: {sorted(unresolved)[:3]})")
    check(any(e.startswith("/admin-api/v1/") for e in endpoints),
          "the admin prefix resolved to /admin-api/v1 as the tree's properties say")

    # 2. the composed-constant surface is present
    print("\n2. the surface a literals-only extractor cannot see is present")
    check("/oauth/jwttoken/verify" in endpoints,
          "the OAuth token-verify endpoint is in the table (composed constant)")
    for ep in ("/admin-api/v1/monitoring/proctoring", "/admin-api/v1/exam/seb-settings",
               "/admin-api/v1/orientation/view"):
        check(ep in endpoints, f"{ep} is in the table (composed constant)")

    # 3. every write, on every endpoint, is refused with -32601
    print("\n3. every write on every endpoint is refused with -32601")
    writes = [t for t in tools if t["_verb"] in WRITE_VERBS]
    check(len(writes) > 150, f"the manifest contains the whole write surface ({len(writes)})")
    bad = [t["name"] for t in writes
           if gate.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                           "params": {"name": t["name"]}}
                          ).get("error", {}).get("code") != -32601]
    check(not bad, f"all {len(writes)} write tools answered -32601"
                   + (f" (offenders: {bad[:3]})" if bad else ""))

    # 4. the refusal happened before the upstream
    print("\n4. the refusal is before the upstream, not after it")
    check(reached == [], f"no write reached the stub upstream (reached={len(reached)})")
    check(gate.upstream_calls == 0, "gate's own upstream counter is 0")

    # 5. dead routes are never advertised
    print("\n5. the routes ReadonlyEntityController leaves live are not advertised")
    dead = [t for t in tools if t["_source"] in DEAD_SOURCES]
    check(len(dead) == 20, f"16 denied + 4 guarded rows are in the table ({len(dead)})")
    guarded = [t for t in tools if t["_source"] == "inherited-guarded"]
    check(len(guarded) == 4,
          f"DELETE /{{id}}/force is live on the 4 read-only controllers ({len(guarded)})")
    check(all(t["name"] not in allow for t in dead),
          f"none of the {len(dead)} dead routes is in the allowlist")

    # 6. a conditional controller is never advertised
    print("\n6. a controller behind @ConditionalOn* is not advertised")
    cond = [t for t in tools if t["_conditional"]]
    check(len(cond) > 0, f"the table records the conditional routes ({len(cond)})")
    check(all(t["name"] not in allow for t in cond),
          "LightController is withheld: seb-server ships light.setup=false")

    # 7. named denies are denied outright, reads included
    print("\n7. the named denies are denied outright (reads included)")
    for ep in DENY_ENDPOINTS:
        grp = [t for t in tools if t["_endpoint"] == ep]
        check(len(grp) > 0, f"the manifest contains {ep} tools ({len(grp)})")
        check(all(t["name"] not in allow for t in grp),
              f"all {len(grp)} {ep} tools are outside the allowlist, including reads")

    # 8. withheld tools are not advertised, and no internals leak
    print("\n8. a withheld tool is not advertised by tools/list")
    listed = {t["name"] for t in
              gate.handle({"jsonrpc": "2.0", "id": 2,
                           "method": "tools/list"})["result"]["tools"]}
    check(not (listed & {t["name"] for t in writes}),
          "no write tool appears in tools/list")
    check(listed == set(allow), "tools/list is exactly the allowlist")
    check(all(not k.startswith("_")
              for t in gate.handle({"jsonrpc": "2.0", "id": 3,
                                    "method": "tools/list"})["result"]["tools"]
              for k in t),
          "no internal _-prefixed key leaks into tools/list")

    # 9. the gate is not vacuous: legitimate reads still work
    print("\n9. the gate is not vacuous: legitimate reads still pass")
    reads = [t for t in tools if t["name"] in allow]
    ok = [t for t in reads
          if "result" in gate.handle({"jsonrpc": "2.0", "id": 4,
                                      "method": "tools/call",
                                      "params": {"name": t["name"]}})]
    check(len(ok) == len(reads) and len(reads) > 0,
          f"all {len(reads)} allowed tools dispatched to the upstream")
    check(gate.upstream_calls == len(reads),
          f"upstream saw exactly the {len(reads)} allowed reads and nothing else")
    check(all(not t["_write"] for t in reads), "nothing exposed is a write")

    # 10. an unknown tool name is refused the same way
    print("\n10. an unknown name is refused identically")
    check(gate.handle({"jsonrpc": "2.0", "id": 5, "method": "tools/call",
                       "params": {"name": "seb.exam.post.invented"}}
                      )["error"]["code"] == -32601,
          "an invented tool name also yields -32601")

    # 11. an empty allowlist exposes nothing (P85's floor)
    print("\n11. an empty allowlist exposes nothing")
    g0 = Gate(tools, set(), lambda n, a: {"ok": True})
    check(g0.handle({"jsonrpc": "2.0", "id": 6,
                     "method": "tools/list"})["result"]["tools"] == [],
          "with an empty allowlist tools/list is empty")
    check(g0.handle({"jsonrpc": "2.0", "id": 7, "method": "tools/call",
                     "params": {"name": tools[0]["name"]}}
                    )["error"]["code"] == -32601,
          "and every call is -32601")

    print(f"\n{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"ACTION 1 VERIFIED over the whole service: {len(ops)} operations, "
          f"{len(controllers)} controllers, {len(endpoints)} endpoints.\n"
          f"The entire write surface ({len(writes)}) is withheld with -32601, "
          "no withheld call reached the upstream,\n"
          "and the dead, conditional and named-deny routes are not advertised.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
