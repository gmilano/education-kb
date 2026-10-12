"""p147-provisional-reverdict -- `ACTION EI`, discharged on a channel p146 found refused.

`P146-B` proved `p141-agent-surface-gate/surface_gate.py` can return
`NOT_AN_MCP_SERVER (0 'mcp' tokens, no SDK import)` from a walk of zero files, and p146
named five published rows carrying exactly that verdict. 🔴 **It could not tell whether any
of the five WAS such an artefact, because every clone was refused in that session.**

This probe answers the question with the payload in hand. For each row it reports, side by
side:

  * `walked_excl`  -- files the published instrument's exclusion set admits;
  * `walked_all`   -- files admitted when `dist`/`build` are re-admitted;
  * `guard`        -- `walk_guard.walked_or_refuse` over the FIRST set, which is the
                      instrument's own input;
  * `artefact`     -- `SOURCE` or `PAYLOAD` by `surface_gate3`'s rule (does every declared
                      entry point resolve inside an excluded tree?);
  * `verdict_now`  -- the re-measured verdict over whichever set the artefact rule selects.

🔵 **The two counts are the whole measurement.** `walked_excl == 0 < walked_all` is a `T42`
artefact: the row was never read. `walked_excl > 0` means the instrument had input and the
published verdict is a finding about the payload, whatever else is wrong with it.

    python3 reverdict.py <payload-root>...        # TSV to stdout, summary to stderr
    python3 test_reverdict.py                     # 10 tests, authored fixtures, offline
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p146-empty-walk-guard"))
from walk_guard import walked_or_refuse, NO_PAYLOAD_WALKED          # noqa: E402

# The exclusion set `surface_gate.py` carries inline inside `walk()`, verbatim.
SKIP_DIRS = {".git", "node_modules", "__pycache__", "dist", "build",
             ".venv", "venv", "vendor"}
# The two names whose exclusion `P145-A`/`T39` showed to be artefact-relative.
PAYLOAD_NAMES = {"dist", "build"}

EXT = {".js": "js", ".jsx": "js", ".mjs": "js", ".cjs": "js", ".ts": "js", ".tsx": "js",
       ".py": "python", ".php": "php", ".go": "go", ".rs": "rust", ".java": "java",
       ".svelte": "js", ".vue": "js"}

SDK_IMPORT = re.compile(
    r"""(from|import|require)\s*\(?\s*['"]?@?modelcontextprotocol"""
    r"""|\bFastMCP\s*\(|new\s+McpServer\s*\(|from\s+mcp\.server""")
MCP_TOKEN = re.compile(r"\bmcp\b", re.IGNORECASE)


def lang_of(path):
    return EXT.get(os.path.splitext(path)[1].lower())


def walk(root, skip):
    """Every source file under `root`, excluding directory names in `skip`."""
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            p = os.path.join(base, f)
            if lang_of(p):
                yield p


def declared_entries(root):
    """`main`/`bin`/`module`/`exports` from `package.json`, as relative path strings."""
    pj = os.path.join(root, "package.json")
    if not os.path.isfile(pj):
        return []
    try:
        data = json.load(open(pj, encoding="utf-8", errors="replace"))
    except (ValueError, OSError):
        return []
    out = []

    def collect(v):
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, dict):
            for x in v.values():
                collect(x)
        elif isinstance(v, list):
            for x in v:
                collect(x)

    for key in ("main", "module", "bin", "exports"):
        if key in data:
            collect(data[key])
    return [e for e in out if isinstance(e, str) and e.strip()]


def artefact_mode(root):
    """`PAYLOAD` when every declared entry point resolves inside an excluded tree.

    `surface_gate3`'s rule, restated for this probe. No `package.json`, or no declared
    entry, is `SOURCE`: there is nothing saying the built tree is the shipped one.
    """
    entries = declared_entries(root)
    if not entries:
        return "SOURCE", "no declared entry point"
    inside = 0
    for e in entries:
        parts = e.lstrip("./").replace("\\", "/").split("/")
        if parts and parts[0] in PAYLOAD_NAMES:
            inside += 1
    if inside and inside == len(entries):
        return "PAYLOAD", "%d/%d entries inside %s" % (
            inside, len(entries), "/".join(sorted(PAYLOAD_NAMES)))
    return "SOURCE", "%d/%d entries inside a built tree" % (inside, len(entries))


def measure(root, skip):
    """(files, sdk, tokens) over `root` with `skip` excluded."""
    n = 0
    sdk = False
    tokens = 0
    for p in walk(root, skip):
        n += 1
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if SDK_IMPORT.search(t) or '"tools/list"' in t or "'tools/list'" in t:
            sdk = True
        tokens += len(MCP_TOKEN.findall(t))
    return n, sdk, tokens


def verdict_of(sdk, tokens):
    if sdk:
        return "IS_AN_MCP_SERVER"
    return "NOT_AN_MCP_SERVER (%d 'mcp' tokens, no SDK import)" % tokens


def classify(root):
    """One row. `t42` is the only verdict that matters for `ACTION EI`."""
    skip_all = SKIP_DIRS - PAYLOAD_NAMES
    n_excl, sdk_excl, tok_excl = measure(root, SKIP_DIRS)
    n_all, sdk_all, tok_all = measure(root, skip_all)
    status, detail = walked_or_refuse(range(n_excl), root, SKIP_DIRS)
    mode, why = artefact_mode(root)

    if mode == "PAYLOAD":
        sdk, tok = sdk_all, tok_all
    else:
        sdk, tok = sdk_excl, tok_excl

    if n_excl == 0 and n_all > 0:
        t42 = "T42_ARTEFACT"
    elif n_excl == 0 and n_all == 0:
        t42 = "NO_SOURCE_AT_ALL"
    else:
        t42 = "INPUT_SEEN"

    return {
        "row": os.path.basename(root.rstrip("/")),
        "walked_excl": n_excl,
        "walked_all": n_all,
        "guard": status,
        "artefact": mode,
        "artefact_why": why,
        "verdict_published_reproduces": verdict_of(sdk_excl, tok_excl),
        "verdict_now": verdict_of(sdk, tok),
        "t42": t42,
        "guard_detail": detail,
    }


COLS = ["row", "walked_excl", "walked_all", "guard", "artefact", "artefact_why",
        "verdict_published_reproduces", "verdict_now", "t42"]


def main(argv):
    roots = argv[1:]
    if not roots:
        print(__doc__)
        return 2
    print("\t".join(COLS))
    rows = []
    for root in roots:
        if not os.path.isdir(root):
            sys.stderr.write("MISSING\t%s\n" % root)
            continue
        r = classify(root)
        rows.append(r)
        print("\t".join(str(r[c]) for c in COLS))
    art = sum(1 for r in rows if r["t42"] == "T42_ARTEFACT")
    seen = sum(1 for r in rows if r["t42"] == "INPUT_SEEN")
    sys.stderr.write("\n%d row(s): %d T42_ARTEFACT, %d INPUT_SEEN, %d no source\n"
                     % (len(rows), art, seen, len(rows) - art - seen))
    for r in rows:
        if r["guard"] == NO_PAYLOAD_WALKED:
            sys.stderr.write("REFUSED\t%s\t%s\n" % (r["row"], r["guard_detail"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
