"""p143-tier-size -- `ACTION DL`: is the npm tier simply SMALLER?

`T30` rested on npm publication predicting literal tool registration -- 12% / 50% / 50%
-- with no mechanism established. `ACTION DL` pre-registered the obvious candidate: npm
rows are smaller, and small projects register literally because they have few tools.

🔴 **Falsifier as registered: refuted if the npm rows are not systematically smaller**,
which leaves `T30` a correlation with no proposed cause and demotes it to an observation.

🔴 **This probe reports a second thing the pre-registration did not ask for, because
`ACTION DM` found it first and it changes what a size comparison can mean.** 7 of the 8
npm rows ship ONLY compiled output (`dist/`, `build/`); exactly one ships source. So:

  * a byte count over an npm row measures a BUNDLE -- minified, inlined, with its
    dependencies' code folded in;
  * a byte count over a git row measures SOURCE.

🔵 **Those two numbers do not answer the same question**, and a tier comparison built on
them would repeat, one layer down, exactly the error `T30` was written to name. So this
probe prints both and books neither as a like-for-like comparison. The one npm row that
ships source is the only directly comparable member, and n=1 is reported as n=1.

Run: python3 -I tiersize.py tier=subject=path[=tools] ...
"""

import os
import sys

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "vendor"}
COMPILED = {"dist", "build", "out", "lib"}
SRC_EXT = (".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".go", ".rs", ".php", ".java",
           ".kt", ".rb", ".cs", ".svelte", ".vue")


def measure(root):
    """-> (src_bytes, src_files, compiled_bytes, compiled_files, ships_source)"""
    sb = sf = cb = cf = 0
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(base, root).replace(os.sep, "/")
        parts = set(rel.split("/"))
        compiled = bool(parts & COMPILED)
        for f in files:
            if not f.lower().endswith(SRC_EXT):
                continue
            if f.endswith(".d.ts") or f.endswith(".min.js") or f.endswith(".map"):
                continue
            p = os.path.join(base, f)
            q = p.replace(os.sep, "/")
            if "/test" in q or f.startswith("test_"):
                continue
            try:
                n = os.path.getsize(p)
            except OSError:
                continue
            if compiled:
                cb += n
                cf += 1
            else:
                sb += n
                sf += 1
    return sb, sf, cb, cf, sf > 0


COLS = ["tier", "subject", "tools", "src_bytes", "src_files", "compiled_bytes",
        "compiled_files", "ships_source", "bytes_per_tool", "artefact_measured"]


def main(argv):
    rows = []
    for spec in argv:
        p = spec.split("=")
        tier, subject, path = p[0], p[1], p[2]
        tools = int(p[3]) if len(p) > 3 and p[3].isdigit() else 0
        if not os.path.isdir(path):
            continue
        sb, sf, cb, cf, ships = measure(path)
        measured = "SOURCE" if ships else ("COMPILED_BUNDLE" if cf else "NOTHING")
        basis = sb if ships else cb
        bpt = ("%d" % (basis // tools)) if tools else "-"
        rows.append(dict(zip(COLS, [tier, subject, tools, sb, sf, cb, cf,
                                    "YES" if ships else "NO", bpt, measured])))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    print("", file=sys.stderr)
    tiers = {}
    for r in rows:
        tiers.setdefault(r["tier"], []).append(r)

    def med(v):
        v = sorted(v)
        return v[len(v) // 2] if v else 0

    for tier, rs in sorted(tiers.items()):
        tools = [r["tools"] for r in rs if r["tools"]]
        basis = [(r["src_bytes"] if r["ships_source"] == "YES" else r["compiled_bytes"])
                 for r in rs]
        src_rows = [r for r in rs if r["ships_source"] == "YES"]
        print("# tier %-12s n=%-2d  median tools=%-4s median bytes=%-7s  "
              "ships_source=%d/%d"
              % (tier, len(rs), med(tools) or "-", med(basis) or "-",
                 len(src_rows), len(rs)), file=sys.stderr)

    print("\n# --- the comparison ACTION DL asked for ---", file=sys.stderr)
    npm = tiers.get("npm", [])
    non = [r for t, rs in tiers.items() if t != "npm" for r in rs]
    if npm and non:
        nt = med([r["tools"] for r in npm if r["tools"]])
        ot = med([r["tools"] for r in non if r["tools"]])
        print("# median tool count   npm=%s  non-npm=%s" % (nt, ot), file=sys.stderr)
        print("# 🔴 npm rows are %s on tool count"
              % ("SMALLER" if nt < ot else "NOT smaller"), file=sys.stderr)
        src_npm = [r for r in npm if r["ships_source"] == "YES"]
        print("# npm rows shipping SOURCE (directly comparable): %d of %d  %s"
              % (len(src_npm), len(npm),
                 ", ".join(r["subject"] for r in src_npm) or "-"), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
