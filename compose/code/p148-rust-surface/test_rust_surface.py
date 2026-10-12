"""Tests for p148-rust-surface. 14 tests, authored fixtures, offline.

Every fixture is written here, so a pass is a statement about the reader and not
about any repository. The negative cases are the point: `T64` says an instrument
must distinguish "I looked and it is not there" from "I could not look", and four
of these tests check that this one refuses instead of returning zero.
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rust_surface as rs

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append("%s\n    got  %r\n    want %r" % (name, got, want))
        print("FAIL %s" % name)
    else:
        print("ok   %s" % name)


def tree(files):
    d = tempfile.mkdtemp()
    for rel, body in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


ROUTER_SRC = """
use rmcp::{tool, tool_router};

#[tool_router]
impl S {
    #[tool(description = "a")]
    fn alpha(&self) -> String { String::new() }

    #[tool(description = "b")]
    fn beta(&self) -> String { String::new() }
}

impl S {
    #[tool(description = "outside the router")]
    fn gamma(&self) -> String { String::new() }
}
"""

MANIFEST = """
server_id = "s"

[[tools]]
name = "alpha"
risk_class = "read_only"

[[tools]]
name = "beta"
risk_class = "internal_write"
"""

# 1 -- the router block bounds the count
check("router_tools reads only inside #[tool_router]",
      rs.router_tools(ROUTER_SRC), ["alpha", "beta"])

# 2 -- a tree with no #[tool_router] refuses rather than returning 0
d = tree({"src/lib.rs": "pub fn nothing() {}\n", "mcp-server.toml": MANIFEST})
r = rs.measure(d)
check("no #[tool_router] -> refusal, not zero",
      (r["router"], r["verdict"].split(" (")[0]), (None, "NO_RUST_SURFACE_READ"))
shutil.rmtree(d)

# 3 -- a tree with no .rs at all refuses
d = tree({"README.md": "# nothing\n"})
r = rs.measure(d)
check("no .rs walked -> refusal, not zero",
      r["verdict"], "NO_RUST_SURFACE_READ (no .rs file walked)")
shutil.rmtree(d)

# 4 -- a router with no manifest refuses on the manifest side
d = tree({"src/server.rs": ROUTER_SRC})
r = rs.measure(d)
check("router but no manifest -> NO_MANIFEST_READ",
      (len(r["router"]), r["verdict"]), (2, "NO_MANIFEST_READ (no mcp-server.toml)"))
shutil.rmtree(d)

# 5 -- the happy path: equal sets
d = tree({"src/server.rs": ROUTER_SRC, "mcp-server.toml": MANIFEST})
r = rs.measure(d)
check("equal sets -> SET_IDENTICAL", r["verdict"], "SET_IDENTICAL")

# 6 -- and counts agree
check("equal sets -> counts agree", r["count_equal"], True)
shutil.rmtree(d)

# 7 -- counts can agree while sets diverge: the exact case ACTION EO cannot catch
skew = MANIFEST.replace('name = "beta"', 'name = "delta"')
d = tree({"src/server.rs": ROUTER_SRC, "mcp-server.toml": skew})
r = rs.measure(d)
check("counts agree, sets diverge -> EO silent, EP fires",
      (r["count_equal"], r["set_equal"], r["router_only"], r["manifest_only"]),
      (True, False, ["beta"], ["delta"]))
shutil.rmtree(d)

# 8 -- an explicit name in the attribute wins over the fn identifier
named = ROUTER_SRC.replace('#[tool(description = "a")]',
                           '#[tool(name = "renamed", description = "a")]')
check("explicit name = wins over fn identifier",
      rs.router_tools(named), ["renamed", "beta"])

# 9 -- a brace inside a string literal does not end the block
braced = """
#[tool_router]
impl S {
    #[tool(description = "a }")]
    fn alpha(&self) -> String { format!("{{}}") }

    #[tool(description = "b")]
    fn beta(&self) -> String { String::new() }
}
"""
check("a } inside a string does not end the router block",
      rs.router_tools(braced), ["alpha", "beta"])

# 10 -- a brace inside a comment does not end the block either
commented = """
#[tool_router]
impl S {
    // closing } in a comment
    #[tool(description = "a")]
    fn alpha(&self) -> String { String::new() }
    /* and } in a block comment */
    #[tool(description = "b")]
    fn beta(&self) -> String { String::new() }
}
"""
check("a } inside a comment does not end the router block",
      rs.router_tools(commented), ["alpha", "beta"])

# 11 -- a commented-out registration is not a registration
dead = ROUTER_SRC.replace('    #[tool(description = "b")]',
                          '    // #[tool(description = "b")]')
check("a commented-out #[tool( is not counted",
      rs.router_tools(dead), ["alpha"])

# 12 -- a lifetime is not a char literal (the apostrophe case that breaks naive strippers)
lifetimes = """
#[tool_router]
impl<'a> S<'a> {
    #[tool(description = "a")]
    fn alpha(&'a self) -> &'a str { "x" }
}
"""
check("a lifetime does not swallow the block", rs.router_tools(lifetimes), ["alpha"])

# 13 -- manifest_tools takes one name per [[tools]] and stops at the next table
multi = MANIFEST + """
[[other]]
name = "not-a-tool"
"""
d = tree({"mcp-server.toml": multi})
check("manifest_tools ignores a different table array",
      rs.manifest_tools(os.path.join(d, "mcp-server.toml")), ["alpha", "beta"])
shutil.rmtree(d)

# 14 -- a duplicate name is reported, because a set comparison would hide it
dupe_src = ROUTER_SRC.replace("fn beta", "fn alpha", 1)
d = tree({"src/server.rs": dupe_src, "mcp-server.toml": MANIFEST})
r = rs.measure(d)
check("a duplicated router name is reported, not absorbed by the set",
      r["router_dupes"], ["alpha"])
shutil.rmtree(d)

print("\n%d/%d passed" % (14 - len(FAILS), 14))
for f in FAILS:
    print("\n" + f)
sys.exit(1 if FAILS else 0)
