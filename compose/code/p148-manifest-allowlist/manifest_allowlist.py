"""p148-manifest-allowlist -- `ACTION EV`: can the manifest replace the name list?

`ACTION EC` (p147) found that `krzysztofbury/librus-mcp`'s own `pyproject.toml` carries the
rule p144 had hand-tuned: an `only-include` allowlist of 16 items that excludes
`legacy_reference` entirely and admits exactly one file from `scripts/`. Reading registration
sites inside it gives **exactly 35**, matching the repository's own `MCP_CONTRACT.md`.
🟢 **`T39` vindicated by the repository itself.**

> 🟡 **`ACTION EV`** — generalise that result: read the **package manifest's include
> allowlist** (`pyproject.toml` `only-include`/`packages`, `package.json` `files`) as the
> `NOT_SHIPPED` rule across all 16 surface subjects, replacing the name list entirely.
> 🔴 *Refuted if any subject has no manifest allowlist to read* — which would mean the
> property-based rule is not universally available and the name list has to stay as a
> fallback, with the two rules' disagreements enumerated.

🔵 **The falsifier is a coverage question, not a correctness one.** `ACTION EC` already
proved the rule is *right* where it exists. `EV` asks whether it exists everywhere, and a
single subject without a manifest allowlist refutes it.

## The eleven manifest shapes this module reads

| manifest | key | tool |
|---|---|---|
| `pyproject.toml` | `[tool.hatch.build.targets.wheel] only-include` / `packages` | hatchling |
| `pyproject.toml` | `[tool.setuptools] packages` / `py-modules` | setuptools |
| `pyproject.toml` | `[tool.setuptools.packages.find] include` | setuptools |
| `pyproject.toml` | `[tool.poetry] packages` | poetry |
| `pyproject.toml` | `[tool.poetry] include` | poetry |
| `package.json` | `files` | npm |
| `Cargo.toml` | `include` | cargo |
| `MANIFEST.in` | `graft` / `include` | setuptools (sdist) |
| `go.mod` | — | 🔴 **Go has no include allowlist at all** |
| `composer.json` | — | 🔴 **PHP has no include allowlist in composer.json** |
| *(none)* | — | 🔴 no manifest |

🔵 **Two of these rows are the finding.** A language can have a package manifest and still
have **no concept** of an include allowlist, so "read the manifest" is not a rule that can be
stated language-independently. That is `T39`'s own shape one level up: 🟢 **a property-based
exclusion is sound only where the property exists.**

    python3 manifest_allowlist.py <clone-dir> [subject ...]
    python3 test_manifest_allowlist.py    # 12 tests, authored fixtures, offline
"""

import json
import os
import re
import sys

# A TOML array of strings on one line or spread over several, under a named key.
ARRAY_KEY = r"""^\s*%s\s*=\s*\[(?P<body>[^\]]*)\]"""
STRINGS = re.compile(r"""["']([^"']+)["']""")


def read(path, limit=200000):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def toml_table(text, table):
    """The body of one TOML table, from its header to the next header."""
    m = re.search(r"^\s*\[%s\]\s*$" % re.escape(table), text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^\s*\[", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def toml_array(body, key):
    """A TOML array of strings under `key`, tolerant of multi-line arrays."""
    if body is None:
        return None
    m = re.search(ARRAY_KEY % re.escape(key), body, re.M | re.S)
    if not m:
        # multi-line: take from the key to the matching close bracket
        m2 = re.search(r"^\s*%s\s*=\s*\[" % re.escape(key), body, re.M)
        if not m2:
            return None
        close = body.find("]", m2.end())
        if close < 0:
            return None
        return STRINGS.findall(body[m2.end():close])
    return STRINGS.findall(m.group("body"))


PY_SHAPES = [
    ("tool.hatch.build.targets.wheel", "only-include", "hatchling only-include"),
    ("tool.hatch.build.targets.wheel", "packages", "hatchling packages"),
    ("tool.hatch.build.targets.sdist", "only-include", "hatchling sdist only-include"),
    ("tool.setuptools", "packages", "setuptools packages"),
    ("tool.setuptools", "py-modules", "setuptools py-modules"),
    ("tool.setuptools.packages.find", "include", "setuptools find include"),
    ("tool.poetry", "packages", "poetry packages"),
    ("tool.poetry", "include", "poetry include"),
]


def pyproject_allowlist(root):
    text = read(os.path.join(root, "pyproject.toml"))
    if not text:
        return None, None
    for table, key, how in PY_SHAPES:
        body = toml_table(text, table)
        got = toml_array(body, key)
        if got:
            return got, "pyproject.toml [%s] %s" % (table, key)
        if body is not None and key == "packages":
            # poetry's `packages` is an array of inline tables: [{include = "x"}]
            inc = re.findall(r"""include\s*=\s*["']([^"']+)["']""", body)
            if inc:
                return inc, "pyproject.toml [%s] packages.include" % table
    return None, "pyproject.toml (no allowlist key)"


def package_json_allowlist(root):
    p = os.path.join(root, "package.json")
    if not os.path.isfile(p):
        return None, None
    try:
        meta = json.loads(read(p))
    except ValueError:
        return None, "package.json (unparseable)"
    files = meta.get("files")
    if isinstance(files, list) and files:
        return [str(f) for f in files], "package.json files"
    return None, "package.json (no files key)"


def cargo_allowlist(root):
    text = read(os.path.join(root, "Cargo.toml"))
    if not text:
        return None, None
    got = toml_array(toml_table(text, "package"), "include")
    if got:
        return got, "Cargo.toml [package] include"
    return None, "Cargo.toml (no include key)"


def manifest_in_allowlist(root):
    text = read(os.path.join(root, "MANIFEST.in"))
    if not text:
        return None, None
    got = re.findall(r"^\s*(?:graft|include|recursive-include)\s+(\S+)", text, re.M)
    if got:
        return got, "MANIFEST.in"
    return None, "MANIFEST.in (no include directive)"


# 🔴 Manifests that exist but cannot express an include allowlist at all.
NO_ALLOWLIST_CONCEPT = {
    "go.mod": "Go has no include allowlist; the module is the unit",
    "composer.json": "composer.json has no include allowlist for a library",
}


def measure(root, subject):
    """(allowlist, how, verdict) for one subject. Refuses rather than inventing one."""
    for fn in (pyproject_allowlist, package_json_allowlist, cargo_allowlist,
               manifest_in_allowlist):
        got, how = fn(root)
        if got:
            return dict(subject=subject, n=len(got), how=how,
                        verdict="ALLOWLIST", allowlist=got, note="")
    # No allowlist. Say WHY, because "absent" and "inexpressible" are different.
    present = []
    for name, why in NO_ALLOWLIST_CONCEPT.items():
        if os.path.isfile(os.path.join(root, name)):
            present.append((name, why))
    if present:
        name, why = present[0]
        return dict(subject=subject, n=0, how=name, verdict="NO_ALLOWLIST_CONCEPT",
                    allowlist=[], note=why)
    seen = [f for f in ("pyproject.toml", "package.json", "Cargo.toml", "MANIFEST.in",
                        "setup.py", "setup.cfg")
            if os.path.isfile(os.path.join(root, f))]
    if seen:
        return dict(subject=subject, n=0, how=", ".join(seen),
                    verdict="MANIFEST_NO_ALLOWLIST", allowlist=[],
                    note="manifest present, no include allowlist declared")
    return dict(subject=subject, n=0, how="-", verdict="NO_MANIFEST", allowlist=[],
                note="no package manifest of any kind")


COLS = ["subject", "verdict", "n", "how", "note"]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    clone_dir = argv[1]
    wanted = argv[2:]
    subjects = wanted or sorted(d for d in os.listdir(clone_dir)
                                if os.path.isdir(os.path.join(clone_dir, d)))
    rows = [measure(os.path.join(clone_dir, s), s) for s in subjects]
    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print("# population: %d" % len(rows))
    for k in sorted(counts):
        print("# %-24s %d" % (k, counts[k]))
    missing = len(rows) - counts.get("ALLOWLIST", 0)
    print("#")
    print("# ACTION EV falsifier -- subjects with NO allowlist to read: %d -> %s"
          % (missing, "REFUTED" if missing else "NOT REFUTED"))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join([r["subject"], r["verdict"], str(r["n"]), r["how"], r["note"]]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
