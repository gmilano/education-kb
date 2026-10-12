"""p144-npm-source-parity -- ACTION DP.

Extracts the SET of tool names surface_bound.py would count, from a bundle tree and
from a shipped-source tree, and compares the sets rather than the counts.

Count identity is not parity: two trees can both read 14 and name different tools.
DP asked whether bundle and source are interchangeable for this measurement, and only
set identity answers that.
"""
import os, re, sys, json

TOOL = r"[a-z][a-z0-9_.-]{2,63}"
PATS = [re.compile(r"(?:registerTool|\.tool)\(\s*[\"'](" + TOOL + r")[\"']"),
        re.compile(r"\bname\s*:\s*[\"'](" + TOOL + r")[\"']"),
        re.compile(r"\bname\s*=\s*[\"'](" + TOOL + r")[\"']")]
# server-constructor names are not tools (surface_bound's SERVER_CTOR exclusion)
CTOR = re.compile(r"new\s+(?:[A-Za-z_$][\w$]*\.)*(?:Mcp)?Server\s*\(\s*\{?\s*name\s*:\s*[\"']([^\"']+)[\"']")
EXT = {".js", ".mjs", ".cjs", ".ts"}

def names(root):
    got, ctors = set(), set()
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
        for f in files:
            if os.path.splitext(f)[1] not in EXT or f.endswith(".d.ts"):
                continue
            try:
                t = open(os.path.join(base, f), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            ctors |= set(CTOR.findall(t))
            for p in PATS:
                got |= set(p.findall(t))
    return got - ctors

if __name__ == "__main__":
    out = {}
    for spec in sys.argv[1:]:
        label, bundle, source = spec.split("=")
        b, s = names(bundle), names(source)
        out[label] = {"bundle_n": len(b), "source_n": len(s),
                      "identical": sorted(b) == sorted(s),
                      "bundle_only": sorted(b - s), "source_only": sorted(s - b)}
    print(json.dumps(out, indent=2))
