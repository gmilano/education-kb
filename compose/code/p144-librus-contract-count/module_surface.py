"""p144-librus-contract-count -- `ACTION DR`.

Re-counts `krzysztofbury/librus-mcp`'s shipped tool surface by a method that shares no code
with the AST instrument that produced p143's **35**, because `P143-C` means that instrument
got this repository wrong twice.

The independent method is the repository's OWN partition of its surface:

  1. count `server.tool(` sites per shipped MODULE under `src/librus_mcp/`;
  2. read which modules are registered unconditionally in `server.py` and which are behind
     a `config.features.*` test;
  3. read the DECLARED DEFAULTS of those flags out of `config.py`;
  4. compose the three surfaces the repository's `MCP_CONTRACT.md` claims in prose.

🔵 **This is a cross-check against documentation, not a second run of the same idea.** The
contract states three figures -- 27, 31 and 35 -- and a count that reproduces all three from
source is far stronger evidence than one that reproduces the single number under test.

🔴 **And it exposes something the AST instrument cannot see.** The feature gates are
`if config.features.send_message: register_send_tools(server)` in `server.py`, while the
registration sites live in `send_tools.py`. 🔴 **The gate and the sites it gates are in
different files**, so a lexical `GATED` detector that looks for an enclosing `if` finds
nothing and reports `gated=0` on a server with three real feature gates.

Run: python3 -I module_surface.py <librus-mcp-checkout>
"""
import os
import re
import sys

SITE = re.compile(r"server\.tool\s*\(")
GATED_CALL = re.compile(r"if\s+config\.features\.(\w+)\s*:\s*\n\s*register_(\w+?)_tools\s*\(",
                        re.MULTILINE)
DEFAULT = re.compile(r"^\s*(\w+)\s*:\s*bool\s*=\s*(True|False)", re.MULTILINE)


def main(argv):
    root = argv[0]
    src = os.path.join(root, "src", "librus_mcp")
    per = {}
    for f in sorted(os.listdir(src)):
        if not f.endswith(".py"):
            continue
        n = len(SITE.findall(open(os.path.join(src, f), encoding="utf-8",
                                  errors="replace").read()))
        if n:
            per[f[:-3]] = n
    server = open(os.path.join(src, "server.py"), encoding="utf-8",
                  errors="replace").read()
    gates = {m.group(2) + "_tools": m.group(1) for m in GATED_CALL.finditer(server)}
    cfg = open(os.path.join(src, "config.py"), encoding="utf-8",
               errors="replace").read()
    defaults = {m.group(1): m.group(2) == "True" for m in DEFAULT.finditer(cfg)}

    total = sum(per.values())
    gated_counts = {mod: per.get(mod, 0) for mod in gates}
    default_on = sum(c for mod, c in gated_counts.items()
                     if defaults.get(gates[mod], False))
    default_off = sum(c for mod, c in gated_counts.items()
                      if not defaults.get(gates[mod], False))
    ungated = total - sum(gated_counts.values())

    print("\t".join(["module", "sites", "gated_by", "default"]))
    for mod, n in sorted(per.items(), key=lambda kv: -kv[1]):
        flag = gates.get(mod, "-")
        print("\t".join([mod, str(n), flag,
                         "-" if flag == "-" else str(defaults.get(flag, "?"))]))
    print("")
    print("\t".join(["surface", "tools", "composition"]))
    print("\t".join(["all_features", str(total), "every module registered"]))
    print("\t".join(["default", str(ungated + default_on),
                     "ungated %d + default-on gated %d" % (ungated, default_on)]))
    print("\t".join(["minimal", str(ungated),
                     "ungated only; -%d default-on, -%d default-off"
                     % (default_on, default_off)]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
