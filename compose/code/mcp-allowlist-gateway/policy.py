#!/usr/bin/env python3
"""The P85 decision core, transport-free. stdlib only.

This is the GENERIC piece gap 103 says P85 promises and does not ship. It is
deliberately NOT a copy of either concrete gate, because neither could be
copied: see README.md. What the two gates share is not their transport and not
their manifest -- it is the DECISION, and that is what lives here.

Three rules, and they are the whole contract:

  1. DEFAULT DENY.  An empty allowlist exposes zero tools. A gateway that fails
     open is not a gateway.
  2. EXACT NAMES.   No globs, no prefixes. `preview_submit_assignment` in the
     allowlist does not admit `submit_assignment`, and `delete_*` cannot enter
     by accident.
  3. THE FLOOR WINS. A name in the floor is refused even when an operator put
     it in the allowlist. Pass 45 found the case that forces this: UniTime's
     `GET /api/script` delegates to `doPost`, so a verb-based read/write policy
     cannot protect it. A floor is not policy -- it is the thing policy may not
     re-open.

Enforcement is at TWO points, and only the second one is a control:
trimming `tools/list` hides a tool; refusing `tools/call` by name, before the
call reaches the upstream, is what makes the pattern a compliance control
rather than a cosmetic one.
"""

# -32601 (Method not found), not -32602 (Invalid params): to the client the
# withheld tool DOES NOT EXIST on this server, which is exactly the assertion
# the gateway wants to make.
REFUSAL_CODE = -32601

EXPOSED = "exposed"
WITHHELD = "withheld"
FLOOR = "floor"


def parse_allowlist(raw):
    """Parse MCP_ALLOWLIST. Comma-separated exact names; blanks dropped.

    An UNSET variable and an empty one are both the empty allowlist, because
    rule 1 leaves no room for a difference: there is no value of this variable
    that means "expose everything".
    """
    return frozenset(t.strip() for t in (raw or "").split(",") if t.strip())


def hard_deny(tools, predicate=None, names=()):
    """Build the floor: the names no allowlist may re-open.

    Two sources, unioned, because the two concrete gates disagree on how the
    floor is known and both ways are legitimate:

      * `predicate(tool) -> bool` -- derived from measured tool metadata. This
        is UniTime's `_crossing` flag (a handler whose GET delegates to doPost).
      * `names` -- stated outright, for a floor known from documentation or
        policy rather than from the tree.
    """
    floor = {n for n in names if n}
    if predicate is not None:
        floor |= {t["name"] for t in tools if predicate(t)}
    return floor


class Policy:
    """Partitions a measured tool manifest into exposed / withheld / floor."""

    def __init__(self, tools, allowlist, floor=()):
        self.tools = list(tools)
        self.floor = set(floor)
        # Rule 3 applied once, here, rather than at every call site: the floor
        # is subtracted from the allowlist at construction, so no later code
        # path can forget it.
        self.allow = set(allowlist) - self.floor

    def decide(self, name):
        if name in self.floor:
            return FLOOR
        return EXPOSED if name in self.allow else WITHHELD

    def exposed(self):
        """The tools to advertise. Built FROM the allowlist, so a withheld tool
        is never advertised in the first place."""
        return [t for t in self.tools if t["name"] in self.allow]

    def withheld(self):
        return [t for t in self.tools if t["name"] not in self.allow]

    def public(self, tools=None):
        """Strip private keys. Metadata used to make the decision (`_write`,
        `_crossing`, `_source`, ...) describes the upstream's attack surface and
        is not the client's business."""
        src = self.exposed() if tools is None else tools
        return [{k: v for k, v in t.items() if not k.startswith("_")} for t in src]

    def refusal(self, req_id, name):
        """The JSON-RPC error for a refused tools/call.

        `data.allowed` is deliberate: the client is told what it MAY call, so a
        well-behaved one can recover without guessing. It never lists the floor.
        """
        return {"jsonrpc": "2.0", "id": req_id,
                "error": {"code": REFUSAL_CODE,
                          "message": f"Tool '{name}' no expuesta por este gateway",
                          "data": {"allowed": sorted(self.allow)}}}
