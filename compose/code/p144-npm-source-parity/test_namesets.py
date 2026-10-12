"""Tests for `namesets.py` -- the properties `ACTION DP` rests on.

🔵 The probe's claim is SET identity, so the tests that matter are the ones that would
distinguish a real parity from a count coincidence.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import namesets  # noqa: E402


def _tree(**files):
    d = tempfile.mkdtemp()
    for name, body in files.items():
        p = os.path.join(d, name)
        os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
        open(p, "w", encoding="utf-8").write(body)
    return d


def test_three_registration_shapes_all_found():
    d = _tree(**{"a.ts": 'server.registerTool("alpha", {})',
                 "b.ts": 'const t = { name: "beta", inputSchema: {} }',
                 "c.ts": 'export const name = "gamma"'})
    assert namesets.names(d) == {"alpha", "beta", "gamma"}


def test_server_constructor_name_is_not_a_tool():
    """The `new Server({name: "x"})` name is the SERVER, and counting it inflates by one."""
    d = _tree(**{"s.ts": 'const s = new Server({ name: "my-server", version: "1" });\n'
                         'const t = { name: "real_tool" };'})
    assert namesets.names(d) == {"real_tool"}


def test_count_coincidence_is_not_parity():
    """🔴 The case a count comparison passes and a set comparison fails."""
    a = _tree(**{"x.ts": 'const t = { name: "tool_one" }'})
    b = _tree(**{"x.ts": 'const t = { name: "tool_two" }'})
    assert len(namesets.names(a)) == len(namesets.names(b)) == 1
    assert namesets.names(a) != namesets.names(b)


def test_declaration_files_are_skipped():
    d = _tree(**{"i.d.ts": 'const t = { name: "ghost" }', "i.ts": 'const t = { name: "kept" }'})
    assert namesets.names(d) == {"kept"}


def test_node_modules_excluded():
    d = _tree(**{"i.ts": 'const t = { name: "kept" }'})
    os.makedirs(os.path.join(d, "node_modules"))
    open(os.path.join(d, "node_modules", "dep.ts"), "w").write('const t={name:"vendored"}')
    assert namesets.names(d) == {"kept"}


if __name__ == "__main__":
    fails = 0
    for fn in sorted(k for k in dict(globals()) if k.startswith("test_")):
        try:
            globals()[fn]()
            print("PASS %s" % fn)
        except AssertionError:
            fails += 1
            print("FAIL %s" % fn)
    sys.exit(1 if fails else 0)
