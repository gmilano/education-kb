#!/usr/bin/env python3
"""mcp-allowlist-gateway -- proxy MCP stdio que reexporta SOLO las tools de una
allowlist y registra cada llamada bloqueada. stdlib only.

This is the piece P85 documents and gap 103 found missing from the tree. Unlike
`sebserver-mcp-gate/` and `unitime-mcp-gate/`, which ARE the upstream (they
synthesize a manifest from a surface measured out of a checkout), this wraps a
THIRD-PARTY upstream it does not control and cannot re-measure. That is the
shape P85's wiring describes, and the reason the generic piece had to be
written rather than extracted -- see README.md.

Usage:
    MCP_ALLOWLIST=get_document,list_documents,get_doctype_schema \
    MCP_AUDIT_LOG=./mcp-blocked.jsonl \
    python3 gateway.py -- npx -y frappe-mcp-server

Environment:
    MCP_ALLOWLIST   comma-separated EXACT tool names. Unset or empty => deny all.
    MCP_HARD_DENY   comma-separated names no allowlist may re-open (the floor).
    MCP_AUDIT_LOG   append JSON lines here; falls back to stderr on OSError.
"""
import json, os, subprocess, sys, threading, time

from policy import FLOOR, Policy, hard_deny, parse_allowlist

ALLOW = parse_allowlist(os.environ.get("MCP_ALLOWLIST"))
DENY = parse_allowlist(os.environ.get("MCP_HARD_DENY"))
AUDIT_LOG = os.environ.get("MCP_AUDIT_LOG", "").strip()
_lock = threading.Lock()


def audit(event, **fields):
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event, **fields}
    line = json.dumps(rec, ensure_ascii=False)
    with _lock:
        if AUDIT_LOG:
            try:
                with open(AUDIT_LOG, "a", encoding="utf-8") as fh:
                    fh.write(line + "\n")
                return
            except OSError:
                pass        # si el log falla, el evento no se pierde: cae a stderr
        print(line, file=sys.stderr, flush=True)


def main():
    argv = sys.argv[1:]
    if argv and argv[0] == "--":
        argv = argv[1:]
    if not argv:
        print("uso: gateway.py -- <comando del servidor upstream>", file=sys.stderr)
        return 2

    # The upstream manifest is unknown until tools/list answers, so the policy
    # starts with no tools and is re-seeded when the listing arrives. The
    # DECISION never depends on that manifest -- only the advertisement does --
    # so a tools/call arriving before any tools/list is still judged correctly.
    pol = Policy([], ALLOW, floor=hard_deny([], names=DENY))
    audit("gateway_start", upstream=argv,
          allowlist=sorted(pol.allow), floor=sorted(pol.floor))
    up = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=None, text=True, bufsize=1)
    pending, plock = set(), threading.Lock()

    def c2u():                                   # cliente -> upstream
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                up.stdin.write(line + "\n"); up.stdin.flush(); continue
            m = msg.get("method")
            if m == "tools/list":
                with plock:
                    pending.add(json.dumps(msg.get("id")))
            elif m == "tools/call":
                name = (msg.get("params") or {}).get("name", "")
                decision = pol.decide(name)
                if decision != "exposed":        # PUNTO 2: el control real
                    audit("tool_call_blocked", tool=name,
                          request_id=msg.get("id"),
                          reason="floor" if decision == FLOOR else "not_allowlisted")
                    sys.stdout.write(json.dumps(pol.refusal(msg.get("id"), name)) + "\n")
                    sys.stdout.flush(); continue
                audit("tool_call_allowed", tool=name, request_id=msg.get("id"))
            up.stdin.write(json.dumps(msg) + "\n"); up.stdin.flush()
        try:
            up.stdin.close()
        except OSError:
            pass

    def u2c():                                   # upstream -> cliente
        for line in up.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                sys.stdout.write(line + "\n"); sys.stdout.flush(); continue
            key = json.dumps(msg.get("id"))
            with plock:
                is_list = key in pending
                if is_list:
                    pending.discard(key)
            if is_list and isinstance(msg.get("result"), dict):
                tools = msg["result"].get("tools")
                if isinstance(tools, list):      # PUNTO 1: recorte del listado
                    pol.tools = tools
                    kept, dropped = pol.exposed(), pol.withheld()
                    msg["result"]["tools"] = kept
                    audit("tools_list_filtered",
                          exposed=[t.get("name") for t in kept],
                          withheld=[t.get("name") for t in dropped],
                          upstream_total=len(tools))
            sys.stdout.write(json.dumps(msg) + "\n"); sys.stdout.flush()

    threading.Thread(target=c2u, daemon=True).start()
    t2 = threading.Thread(target=u2c, daemon=True); t2.start()
    rc = up.wait(); t2.join(timeout=2)
    audit("gateway_stop", upstream_returncode=rc)
    return rc


if __name__ == "__main__":
    sys.exit(main())
