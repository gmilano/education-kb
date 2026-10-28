"""Offline controls for p511-absence-channel. No network: fixtures only."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from absence_channel import (
    LIVE, UNREADABLE, UNKNOWN, LS_REF_OK, LS_AUTH_PROMPT, MCP_ROW, MCP_NO_ROW,
    classify, liveness_from_raw, run_controls, sweep, ControlFailure, UnsoundProbe,
)

FAILS = []


def check(name, cond):
    print(("  ok   " if cond else "  FAIL ") + name)
    if not cond:
        FAILS.append(name)


print("p511-absence-channel offline controls")

check("known-good public grades LIVE", classify(LS_REF_OK, MCP_ROW) == LIVE)
check("never-existed grades UNREADABLE not ABSENT", classify(LS_AUTH_PROMPT, MCP_NO_ROW) == UNREADABLE)
check("private-in-scope grades LIVE (proxy injects credentials)", classify(LS_REF_OK, None) == LIVE)
check("live-but-silently-excluded still grades LIVE", classify(LS_REF_OK, MCP_NO_ROW) == LIVE)
check("MCP row alone is enough for LIVE", classify(None, MCP_ROW) == LIVE)
check("no observation grades UNKNOWN", classify(None, None) == UNKNOWN)
check("no code path returns the string ABSENT",
      "ABSENT" not in {classify(a, b) for a in (LS_REF_OK, LS_AUTH_PROMPT, None)
                       for b in (MCP_ROW, MCP_NO_ROW, None)})

try:
    liveness_from_raw(404)
    check("raw 404 refuses a liveness verdict", False)
except UnsoundProbe:
    check("raw 404 refuses a liveness verdict", True)

check("raw 200 implies LIVE", liveness_from_raw(200) == LIVE)

try:
    liveness_from_raw(403)
    check("raw 403 refuses a liveness verdict", False)
except UnsoundProbe:
    check("raw 403 refuses a liveness verdict", True)

check("run_controls() returns the control count", run_controls() == 8)
check("sweep runs controls then classifies",
      sweep({"a/b": (LS_REF_OK, MCP_ROW), "c/d": (LS_AUTH_PROMPT, MCP_NO_ROW)})
      == {"a/b": LIVE, "c/d": UNREADABLE})

print("%d/%d green" % (12 - len(FAILS), 12))
sys.exit(1 if FAILS else 0)
