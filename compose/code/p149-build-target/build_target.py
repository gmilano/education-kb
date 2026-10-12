"""p149-build-target -- `ACTION FB`: which build target is every `NOT_SHIPPED` figure against?

`T68` found that `librus-mcp`'s one `pyproject.toml` declares **two** include allowlists --
a wheel `packages` and an sdist `only-include` -- that they disagree (**35** tool sites
against **39**), and that p147 had named one while publishing the other's number.

> 🟢 **`ACTION FB`** -- state which build target every `NOT_SHIPPED` figure was measured
> against. Audit the **5** `ALLOWLIST` rows for a second target.
> 🔴 *Refuted if no other subject declares two* -- which would make `librus-mcp` the single
> instance and `T68` a caution rather than a census correction.

## 🔴 Not refuted -- and the reason it looked refuted is an instrument gap

🔴 **`yourssu/soongpt-plugin` declares two targets as well**, and `p148-manifest-allowlist`
could not see the second one. Its shape table reads:

    ("tool.hatch.build.targets.sdist", "only-include", ...)

🔴 **and `soongpt-plugin`'s sdist uses `include`, not `only-include`.** 🔵 **So p148's "one
instance" was a property of its own key list**, not of the shelf -- the same defect class as
`T39` and `P148-C`: an instrument that answers only the question it was spelled to ask.
🟢 **This module enumerates ALL targets** rather than returning the first match, and adds the
four hatch keys p148's table omits.

## What it measures

For every target a manifest declares: the allowlist items, the files in scope, and the
tool-definition sites inside that scope. 🟢 **Two targets on one subject are reported as two
rows**, so a divergence is visible rather than averaged.

    python3 build_target.py <clone-dir> [subject ...]
    python3 test_build_target.py       # 22 tests, authored fixtures, offline
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir, "p148-manifest-allowlist"))

import manifest_allowlist as ma  # noqa: E402  the TOML/array readers, reused as published

# 🟢 Every hatch target/key pair, not the first that matches. 🔴 p148's table held
# (wheel, only-include), (wheel, packages) and (sdist, only-include) -- it omitted
# (sdist, include), which is the one `soongpt-plugin` uses, and (wheel, include).
HATCH_TARGETS = [
    ("tool.hatch.build.targets.wheel", "packages", "wheel"),
    ("tool.hatch.build.targets.wheel", "only-include", "wheel"),
    ("tool.hatch.build.targets.wheel", "include", "wheel"),
    ("tool.hatch.build.targets.sdist", "only-include", "sdist"),
    ("tool.hatch.build.targets.sdist", "include", "sdist"),
    ("tool.hatch.build.targets.sdist", "packages", "sdist"),
]
OTHER_PY_TARGETS = [
    ("tool.setuptools", "packages", "wheel+sdist"),
    ("tool.setuptools", "py-modules", "wheel+sdist"),
    ("tool.setuptools.packages.find", "include", "wheel+sdist"),
    ("tool.poetry", "packages", "wheel+sdist"),
    ("tool.poetry", "include", "wheel+sdist"),
]

# 🔴 Per-language tool-definition sites. The Python form is the one `p144-librus-contract-count`
# published 35 and 39 with (`server.tool(`), widened to the decorator and `mcp.tool(` forms
# that the same libraries accept. 🟢 `librus-mcp` reproducing 35/39 is the control.
SITE_PATTERNS = {
    ".py": [re.compile(r"(?:^|[^\w.])(?:\w+\.)?tool\s*\(", re.M),
            re.compile(r"@\s*(?:\w+\.)*tool\s*\(", re.M)],
    ".js": [re.compile(r"\.(?:tool|registerTool)\s*\(", re.M)],
    ".mjs": [re.compile(r"\.(?:tool|registerTool)\s*\(", re.M)],
    ".cjs": [re.compile(r"\.(?:tool|registerTool)\s*\(", re.M)],
    ".ts": [re.compile(r"\.(?:tool|registerTool)\s*\(", re.M)],
}


def declared_targets(root):
    """[(target, key, kind, items)] -- every build target the manifest declares."""
    out = []
    text = ma.read(os.path.join(root, "pyproject.toml"))
    if text:
        for table, key, kind in HATCH_TARGETS + OTHER_PY_TARGETS:
            body = ma.toml_table(text, table)
            items = ma.toml_array(body, key)
            if items:
                out.append((table, key, kind, items))
            elif body is not None and key == "packages":
                inc = re.findall(r"""include\s*=\s*["']([^"']+)["']""", body)
                if inc:
                    out.append((table, "packages.include", kind, inc))
    pj = os.path.join(root, "package.json")
    if os.path.exists(pj):
        try:
            with open(pj, encoding="utf-8", errors="replace") as fh:
                meta = json.load(fh)
        except (OSError, ValueError):
            meta = {}
        files = meta.get("files")
        if isinstance(files, list) and files:
            # 🔵 npm publishes ONE tarball. `files` is the only allowlist a package can
            # declare, so an npm row structurally cannot have a second target to disagree
            # with -- which is a finding about the format, not about the author.
            out.append(("package.json", "files", "npm-tarball(single)", files))
    return out


def files_in_scope(root, items):
    """Files under the allowlist items, as paths relative to `root`."""
    scope = []
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            for base, dirs, names in os.walk(path):
                dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", "node_modules"}]
                for n in names:
                    scope.append(os.path.relpath(os.path.join(base, n), root))
        elif os.path.isfile(path):
            scope.append(os.path.relpath(path, root))
    return sorted(set(scope))


def count_sites(root, rel_paths):
    """Tool-definition sites, deduplicated by position within each file.

    🔴 The first run of this module counted 43 sites in `librus-mcp`'s sdist scope against
    p148's **39**, while reproducing its wheel figure of **35** exactly. The cause was this
    function: `@mcp.tool(` matches BOTH patterns, so every decorator site was counted twice,
    and the wheel scope hid it because `librus-mcp` registers with `server.tool(` and uses no
    decorators. 🟢 **Positions are now deduplicated**, and the sdist reproduces 39.
    """
    total = 0
    for rel in rel_paths:
        pats = SITE_PATTERNS.get(os.path.splitext(rel)[1].lower())
        if not pats:
            continue
        text = ma.read(os.path.join(root, rel), limit=400000)
        ends = set()
        for pat in pats:
            for m in pat.finditer(text):
                # The open paren is the one position every form shares.
                ends.add(m.end())
        total += len(ends)
    return total


COLS = ["subject", "target", "key", "kind", "items", "files_in_scope", "tool_sites"]


def measure(root, subject):
    rows = []
    for table, key, kind, items in declared_targets(root):
        scope = files_in_scope(root, items)
        rows.append(dict(subject=subject, target=table, key=key, kind=kind,
                         items=len(items), files_in_scope=len(scope),
                         tool_sites=count_sites(root, scope)))
    if not rows:
        rows.append(dict(subject=subject, target="-", key="-", kind="NO_TARGET",
                         items=0, files_in_scope=0, tool_sites=0))
    return rows


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    clone_dir, subjects = argv[1], argv[2:]
    if not subjects:
        subjects = sorted(d for d in os.listdir(clone_dir)
                          if os.path.isdir(os.path.join(clone_dir, d)))
    all_rows, multi = [], []
    for s in subjects:
        rows = measure(os.path.join(clone_dir, s), s)
        all_rows.extend(rows)
        real = [r for r in rows if r["kind"] != "NO_TARGET"]
        if len(real) > 1:
            multi.append((s, real))
    print("# subjects: %d   target rows: %d" % (len(subjects), len(all_rows)))
    print("# subjects declaring MORE THAN ONE target: %d" % len(multi))
    for s, real in multi:
        counts = {r["tool_sites"] for r in real}
        print("#   %-46s %d targets, tool_sites %s -> %s"
              % (s, len(real), sorted(counts),
                 "AGREE" if len(counts) == 1 else "DIVERGE"))
    print("#")
    print("# ACTION FB falsifier -- another subject with two targets? %s -> %s"
          % ("YES" if len(multi) > 1 else "NO",
             "NOT REFUTED" if len(multi) > 1 else "REFUTED"))
    print("\t".join(COLS))
    for r in all_rows:
        print("\t".join(str(r[c]) for c in COLS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
