"""Tests for p148-manifest-allowlist. 12 tests, authored fixtures, offline.

Test 11 is the one that matters: a single `pyproject.toml` can declare **two**
include allowlists, for the wheel and for the sdist, and they can disagree about
the same directory. 🔴 **`librus-mcp` does exactly that**, and the two rules give
**35** and **39** registration sites for the same repository.
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import manifest_allowlist as ma

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


# 1 -- hatchling only-include
d = tree({"pyproject.toml": '[tool.hatch.build.targets.wheel]\nonly-include = ["src/a", "src/b"]\n'})
r = ma.measure(d, "s")
check("hatchling only-include", (r["verdict"], r["n"]), ("ALLOWLIST", 2))
shutil.rmtree(d)

# 2 -- npm files
d = tree({"package.json": '{"name":"x","files":["dist","README.md"]}'})
r = ma.measure(d, "s")
check("package.json files", (r["verdict"], r["n"], r["how"]),
      ("ALLOWLIST", 2, "package.json files"))
shutil.rmtree(d)

# 3 -- cargo include
d = tree({"Cargo.toml": '[package]\nname = "x"\ninclude = ["src/**", "LICENSE"]\n'})
r = ma.measure(d, "s")
check("Cargo.toml include", (r["verdict"], r["n"]), ("ALLOWLIST", 2))
shutil.rmtree(d)

# 4 -- MANIFEST.in
d = tree({"MANIFEST.in": "graft src\ninclude README.md\n"})
r = ma.measure(d, "s")
check("MANIFEST.in directives", (r["verdict"], r["n"]), ("ALLOWLIST", 2))
shutil.rmtree(d)

# 5 -- a manifest with no allowlist key is NOT the same as no manifest
d = tree({"package.json": '{"name":"x","version":"1.0.0"}'})
r = ma.measure(d, "s")
check("manifest, no allowlist key -> MANIFEST_NO_ALLOWLIST",
      r["verdict"], "MANIFEST_NO_ALLOWLIST")
shutil.rmtree(d)

# 6 -- no manifest at all is its own verdict
d = tree({"README.md": "# x\n"})
r = ma.measure(d, "s")
check("no manifest -> NO_MANIFEST", r["verdict"], "NO_MANIFEST")
shutil.rmtree(d)

# 7 -- Go cannot express an allowlist, which is different from not declaring one
d = tree({"go.mod": "module example.com/x\n\ngo 1.24\n"})
r = ma.measure(d, "s")
check("go.mod -> NO_ALLOWLIST_CONCEPT", r["verdict"], "NO_ALLOWLIST_CONCEPT")
shutil.rmtree(d)

# 8 -- an empty files array is not an allowlist
d = tree({"package.json": '{"name":"x","files":[]}'})
r = ma.measure(d, "s")
check("empty files array is not an allowlist",
      r["verdict"], "MANIFEST_NO_ALLOWLIST")
shutil.rmtree(d)

# 9 -- a multi-line TOML array is read whole
d = tree({"pyproject.toml": '[tool.hatch.build.targets.wheel]\nonly-include = [\n  "src/a",\n  "src/b",\n  "src/c",\n]\n'})
r = ma.measure(d, "s")
check("multi-line TOML array", r["n"], 3)
shutil.rmtree(d)

# 10 -- poetry's array-of-inline-tables form
d = tree({"pyproject.toml": '[tool.poetry]\nname = "x"\npackages = [{include = "a"}, {include = "b"}]\n'})
r = ma.measure(d, "s")
check("poetry packages.include", (r["verdict"], r["n"]), ("ALLOWLIST", 2))
shutil.rmtree(d)

# 11 -- 🔴 TWO allowlists in one manifest, disagreeing: the librus-mcp shape
both = ('[tool.hatch.build.targets.wheel]\npackages = ["src/pkg"]\n\n'
        '[tool.hatch.build.targets.sdist]\n'
        'only-include = ["src/pkg", "tests_native", "scripts/q.py"]\n')
d = tree({"pyproject.toml": both})
wheel = ma.toml_array(ma.toml_table(both, "tool.hatch.build.targets.wheel"), "packages")
sdist = ma.toml_array(ma.toml_table(both, "tool.hatch.build.targets.sdist"),
                      "only-include")
check("two targets, two different allowlists, both readable",
      (wheel, len(sdist)), (["src/pkg"], 3))

# 12 -- …and `measure` reports only the FIRST it finds, which is a stated limit
r = ma.measure(d, "s")
check("measure reports the wheel target, not the sdist one",
      (r["n"], "wheel" in r["how"]), (1, True))
shutil.rmtree(d)

print("\n%d/%d passed" % (12 - len(FAILS), 12))
for f in FAILS:
    print("\n" + f)
sys.exit(1 if FAILS else 0)
