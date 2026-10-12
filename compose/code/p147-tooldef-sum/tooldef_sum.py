"""p147-tooldef-sum -- `ACTION ED`: follow the 18 spreads one level and sum.

`@imazhar101/mcp-canvas-server` reads **227 `BOUNDED_STATIC` descriptors** on
`surface_bound` and **18 dynamic registration sites** on `surface_gate*`. `T42` says both
are correct about different properties; `ACTION ED` tests that by resolving the 18 into the
descriptors they actually return.

> 🟡 **`ACTION ED`** -- resolve the **227 vs 18** disagreement by following the 18
> `getToolDefinitions()` calls one level and summing what they return.
> 🔴 *Refuted if the sum is not 227* -- which would mean `surface_bound`'s descriptor count
> includes descriptors the handler never publishes, and the largest tool surface this KB
> quotes is wrong.

## Method -- count objects at array depth 1, not occurrences of `name:`

🔴 **A `grep -c 'name:'` is wrong here and reads 13 on `course-tools.js`, which publishes 11.** Canvas
tools take a parameter called `name`, so the token occurs inside `inputSchema.properties`
as often as it occurs as a descriptor key. This probe tracks bracket depth from the `[` that
opens the returned array and counts only the `{` that sit at depth 1 of that array, which is
what a spread of the array contributes to the handler's `tools` list.

🟢 **Strings and comments are consumed by the scanner**, so a `{` inside a description does
not open a level. 🔴 **No module is imported or executed** -- the payload is third-party and
this measurement does not need it to run.

    python3 tooldef_sum.py <package-root>          # per-module TSV + sum
    python3 test_tooldef_sum.py                    # 11 tests, authored fixtures, offline
"""

import os
import re
import sys

CALL = re.compile(r"\.\.\.\s*[\w.$]*\.getToolDefinitions\s*\(\s*\)")
DEFN = re.compile(r"\bgetToolDefinitions\s*\(\s*\)\s*\{")


def _scan_array(src, i):
    """Count objects at depth 1 of the array opening at `src[i] == '['`.

    Returns (count, index just past the matching ']'). Depth is tracked over all three
    bracket kinds so a nested array of enums cannot be mistaken for the descriptor list.
    """
    assert src[i] == "["
    depth = 0
    count = 0
    n = len(src)
    while i < n:
        c = src[i]
        if c in "\"'`":
            quote = c
            i += 1
            while i < n:
                if src[i] == "\\":
                    i += 2
                    continue
                if src[i] == quote:
                    break
                i += 1
            i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            while i < n and src[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            end = src.find("*/", i + 2)
            i = n if end == -1 else end + 2
            continue
        if c in "[{(":
            depth += 1
            if c == "{" and depth == 2:
                count += 1
            i += 1
            continue
        if c in "]})":
            depth -= 1
            i += 1
            if depth == 0:
                return count, i
            continue
        i += 1
    return count, i


def module_count(path):
    """Descriptors returned by `getToolDefinitions()` in one module, or None."""
    src = open(path, encoding="utf-8", errors="replace").read()
    m = DEFN.search(src)
    if not m:
        return None
    j = src.find("[", m.end())
    if j == -1:
        return None
    count, _ = _scan_array(src, j)
    return count


def handler_sites(path):
    """The spread calls in the `tools/list` handler, in file order."""
    src = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for m in CALL.finditer(src):
        line = src.count("\n", 0, m.start()) + 1
        out.append((line, m.group(0).strip()))
    return out


def resolve(root):
    index = None
    for base, _dirs, files in os.walk(root):
        for f in files:
            if f == "index.js" and os.sep + "canvas" + os.sep in base + os.sep:
                index = os.path.join(base, f)
                break
        if index:
            break
    if index is None:
        return None, [], []
    sites = handler_sites(index)
    tools_dir = os.path.join(os.path.dirname(index), "tools")
    mods = []
    if os.path.isdir(tools_dir):
        for f in sorted(os.listdir(tools_dir)):
            if f.endswith(".js"):
                p = os.path.join(tools_dir, f)
                mods.append((f, module_count(p)))
    return index, sites, mods


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    root = argv[1]
    index, sites, mods = resolve(root)
    if index is None:
        sys.stderr.write("no canvas index.js under %r\n" % root)
        return 1
    # The handler spreads at the top of `tools/list`; the duplicate calls further down
    # are the dispatch table mapping names to handlers, not additional surface.
    first_block = [s for s in sites if s[0] <= (sites[0][0] + len(mods) + 2)] if sites else []
    print("module\tdescriptors")
    total = 0
    for name, c in mods:
        print("%s\t%s" % (name, "PARSE_FAIL" if c is None else c))
        total += c or 0
    print("TOTAL\t%d" % total)
    sys.stderr.write("modules=%d  spread_sites_in_handler=%d  total_spread_calls=%d\n"
                     % (len(mods), len(first_block), len(sites)))
    sys.stderr.write("sum_of_descriptors=%d\n" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
