"""p147-scope-parity -- `ACTION EG` refuted, and the action's own premise is the defect.

`P145-J` found `ahmedEid1/lumen` pinning **tools -> scopes** and never **scopes -> tools**:

    for tool_name in all_tool_names():
        assert tool_name in md["scopes_supported"]        # tests/test_mcp_auth.py:338

`ACTION EG` asked for the missing half, *"refuted if the two sets are not equal -- which
would mean lumen's OAuth vocabulary and its tool registry have already drifted, and
`P145-J` has found a pin that does not hold."*

🔴 **The sets are not equal, so the action is refuted. Its consequence clause is wrong.**
`scopes_supported` carries **10** entries; `all_tool_names()` returns **9**. The extra
element is `WILDCARD_SCOPE = "*"` (`app/models/mcp_client.py:88`) -- a designed element,
not drift.

    set(scopes_supported) - {"*"} == set(all_tool_names())        # holds, 9 == 9

🔵 **A bidirectional equality assertion would FAIL on a correct repository**, which makes
the test `ACTION EG` specified the wrong test. 🟢 **The assertion that catches both
directions** names the wildcard instead of counting past it, and this probe is that
assertion, extracted so it can be run against the payload rather than argued about.

## 🔴 The deployment finding, which is independent of the set algebra

`has_scope()` short-circuits on the wildcard (`app/mcp/principal.py:87`), and `"*"` is the
**shipped default** on two of the three paths that mint a client:

| path | default scopes |
|---|---|
| `app/api/v1/admin_mcp_clients.py:66` | 🔴 `Field(default_factory=lambda: [WILDCARD_SCOPE])` |
| `app/cli.py:478` | 🔴 `scope_list = [WILDCARD_SCOPE]` |
| `issue_token` with an explicit list | 🟢 intersected against the grant (`auth.py:102`) |

🔴 **So the per-tool OAuth vocabulary is, by default, not enforced.**

🟢 **The posture gate is a real second gate and it still applies.** The wildcard bypasses
`has_scope` only; `spec.auth == "admin"` still requires `principal.is_admin`
(`app/mcp/server.py:123`), so `ingest_url_to_draft` -- the one `admin` tool -- is not
reachable with a wildcard token held by a non-admin. 🔵 **That is the difference between
"misconfigured" and "open", and it is why this is a warning and not a vulnerability.**

🔴 **The two writes that matter in a school are `auth="user"`.** `grade_review_card` and
`create_course_draft` are reachable by any authenticated principal holding `"*"`, and the
first one changes a student's record.

    python3 scope_parity.py <lumen-checkout>
    python3 test_scope_parity.py        # 9 tests, authored fixtures, offline
"""

import os
import re
import sys

WILDCARD = "*"


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def tool_specs(src):
    """[(name, auth)] from a `TOOL_SPECS` list literal, in file order.

    `auth` defaults to `"user"`, as `ToolSpec` declares, so a spec that omits the field is
    not silently dropped from the posture census.
    """
    i = src.find("TOOL_SPECS")
    if i == -1:
        return []
    j = src.find("[", i)
    if j == -1:
        return []
    out = []
    for part in src[j:].split("ToolSpec(")[1:]:
        n = re.search(r'name\s*=\s*"([a-z_][a-z0-9_]*)"', part)
        if not n:
            continue
        a = re.search(r'auth\s*=\s*"([a-z]+)"', part)
        out.append((n.group(1), a.group(1) if a else "user"))
    return out


def scopes_supported(src):
    """The `scopes_supported` list literal, with the wildcard resolved to its value."""
    m = re.search(r'"scopes_supported"\s*:\s*\[', src)
    if not m:
        return []
    depth = 0
    i = m.end() - 1
    end = i
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                end = i
                break
        i += 1
    body = src[m.end():end]
    out = []
    for tok in body.split(","):
        tok = tok.strip()
        if not tok:
            continue
        q = re.match(r'^"([^"]*)"$', tok)
        if q:
            out.append(q.group(1))
        elif tok == "WILDCARD_SCOPE":
            out.append(WILDCARD)
        else:
            out.append(tok)
    return out


def parity(tools, scopes):
    """The assertion `ACTION EG` should have specified, in both directions."""
    t = {n for n, _ in tools}
    s = set(scopes)
    return {
        "n_tools": len(t),
        "n_scopes": len(s),
        "equal_raw": t == s,
        "equal_modulo_wildcard": (s - {WILDCARD}) == t,
        "scopes_without_tool": sorted(s - {WILDCARD} - t),
        "tools_without_scope": sorted(t - s),
        "wildcard_present": WILDCARD in s,
    }


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    root = argv[1]
    be = os.path.join(root, "apps", "backend")
    base = be if os.path.isdir(be) else root
    tools = tool_specs(read(os.path.join(base, "app", "mcp", "tools.py")))
    scopes = scopes_supported(read(os.path.join(base, "app", "mcp", "auth.py")))
    if not tools or not scopes:
        sys.stderr.write("could not read TOOL_SPECS and/or scopes_supported under %r\n"
                         % base)
        return 1
    p = parity(tools, scopes)
    print("property\tvalue")
    for k in ("n_tools", "n_scopes", "equal_raw", "equal_modulo_wildcard",
              "wildcard_present"):
        print("%s\t%s" % (k, p[k]))
    print("scopes_without_tool\t%s" % (",".join(p["scopes_without_tool"]) or "-"))
    print("tools_without_scope\t%s" % (",".join(p["tools_without_scope"]) or "-"))
    print("\nname\tauth\thas_scope_entry")
    for n, a in tools:
        print("%s\t%s\t%s" % (n, a, "yes" if n in scopes else "NO"))
    reach = [n for n, a in tools if a in ("public", "user")]
    sys.stderr.write("\n# tools=%d scopes=%d  equal_raw=%s  equal_modulo_wildcard=%s\n"
                     % (p["n_tools"], p["n_scopes"], p["equal_raw"],
                        p["equal_modulo_wildcard"]))
    sys.stderr.write("# reachable with a wildcard token and no elevated role: %d of %d\n"
                     % (len(reach), len(tools)))
    sys.stderr.write("# gated by posture regardless of scope: %s\n"
                     % (", ".join("%s(%s)" % (n, a) for n, a in tools
                                  if a not in ("public", "user")) or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
