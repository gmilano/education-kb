"""p144-not-shipped-breadth -- ACTION DS.

`surface_gate2.NOT_SHIPPED` excludes 11 directory names. It was built for ONE defect
(`librus-mcp`'s `legacy_reference/`). DS asks whether it is doing more work than that.

Method: re-admit each excluded directory NAME one at a time -- i.e. run the shipped-tree
scan with NOT_SHIPPED minus {d} -- and record every row whose VERDICT changes against
the all-exclusions baseline. A name that changes no verdict is inert; a name that changes
a verdict on a row other than librus-mcp means the list is load-bearing beyond its cause.
"""
import json, os, sys

# python3 -I does not prepend the script directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import surface_gate2 as sg

BASE = sorted(sg.NOT_SHIPPED)


def verdicts(subjects):
    out = {}
    for name, path in subjects:
        if not os.path.isdir(path):
            out[name] = "NO_CLONE"
            continue
        sdk, _ = sg.is_mcp_server(path)
        if not sdk:
            out[name] = "NOT_AN_MCP_SERVER"
            continue
        lit, dyn, gated, _l, _s, _si = sg.scan(path, shipped_only=True)
        out[name] = "%s|lit=%d|dyn=%d|gated=%d" % (sg._verdict(lit, dyn, gated), lit, dyn, gated)
    return out


if __name__ == "__main__":
    subjects = []
    for spec in sys.argv[1:]:
        n, p = spec.split("=", 1)
        subjects.append((n, p))
    full = set(BASE)
    sg.NOT_SHIPPED = set(full)
    baseline = verdicts(subjects)
    report = {"baseline": baseline, "readmit": {}}
    for d in BASE:
        sg.NOT_SHIPPED = full - {d}
        v = verdicts(subjects)
        changed = {k: {"baseline": baseline[k], "readmitted": v[k]}
                   for k in v if v[k] != baseline[k]}
        report["readmit"][d] = changed
    print(json.dumps(report, indent=2))
