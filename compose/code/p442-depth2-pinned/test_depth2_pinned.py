#!/usr/bin/env python3
"""Offline controls for p442. No network: `runtime_edges` and `is_extra_only` are pure.

What this instrument can get wrong is its EDGE SET, not its arithmetic -- resolution and
dating are `p437`'s, already controlled by 47 assertions there. So every control below is
a scope or parse control, and each is paired with the case that must still be KEPT
(rule 2 of P126): a reader that returns everything, and a reader that returns nothing,
must both fail.

Run: python3 test_depth2_pinned.py
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import depth2_pinned as d  # noqa: E402

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


def pypi(reqs):
    return d.runtime_edges({"info": {"requires_dist": reqs}}, "pypi")


# --- the specifier must SURVIVE, which is the whole reason this file exists ---
# `p438` matched only the name and discarded the rest, so there was no pin to resolve.
check("the specifier is carried, not discarded",
      pypi(["requests>=2.31.0"]), [("requests", ">=2.31.0")])
check("an exact pin survives", pypi(["certifi==2024.2.2"]), [("certifi", "==2024.2.2")])
check("a compound specifier survives whole",
      pypi(["urllib3>=1.21.1,<3"]), [("urllib3", ">=1.21.1,<3")])
check("a bare name yields an empty specifier, not a dropped row",
      pypi(["six"]), [("six", "")])

# --- extras: the marker decides, and it is the OPTIONAL half that goes --------
check("an extra-gated requirement is optional and excluded",
      pypi(['PySocks>=1.5.6; extra == "socks"']), [])
check("but a python_version marker still INSTALLS and is kept",
      pypi(['tomli>=1.1.0; python_version < "3.11"']), [("tomli", ">=1.1.0")])
check("and a sys_platform marker is kept -- an obligation that binds only on Windows "
      "is still an obligation",
      pypi(['pywin32>=1.0; sys_platform == "win32"']), [("pywin32", ">=1.0")])
check("a marker combining extra with another term is still optional",
      pypi(['x>=1; python_version < "3.11" and extra == "test"']), [])

# --- the marker must be STRIPPED before the specifier is read ----------------
# `p437` published `3.14` as a dependency once, because a quote-splitting pattern read
# the environment marker's own version number as a constraint.  Here the failure mode is
# the mirror image: carrying the marker INTO the specifier makes it unresolvable.
check("the marker is not carried into the specifier",
      pypi(['faiss-cpu>=1.8.0; python_version < "3.14"']),
      [("faiss-cpu", ">=1.8.0")])
check("and the name is still lowercased for the depth-1 subtraction",
      pypi(["Jinja2>=3.0"]), [("jinja2", ">=3.0")])

# --- extras in BRACKETS on the dependency, not in the marker -----------------
# `p437`'s control: a scan to the first `]` closes on the extra's bracket and returns
# nothing for the whole manifest.
check("a bracketed extra is stripped and the specifier after it is read",
      pypi(["pyjwt[crypto]>=2.8,<3"]), [("pyjwt", ">=2.8,<3")])
check("several extras in one bracket do not break the read",
      pypi(["celery[redis,auth]==5.3.6"]), [("celery", "==5.3.6")])

# --- npm scope: three dependency maps are NOT installed by `npm install <pkg>` --
NPM = {"dist-tags": {"latest": "2.0.0"},
       "versions": {"2.0.0": {"dependencies": {"lodash": "^4.17.21"},
                              "devDependencies": {"jest": "^29"},
                              "peerDependencies": {"react": ">=18"},
                              "optionalDependencies": {"fsevents": "^2"}},
                    "1.0.0": {"dependencies": {"left-pad": "1.0.0"}}}}
check("npm runtime dependencies are read", d.runtime_edges(NPM, "npm"),
      [("lodash", "^4.17.21")])
check("and only from the LATEST version, never an older one",
      [n for n, _ in d.runtime_edges(NPM, "npm")], ["lodash"])
check("a packument whose dist-tag dangles expands to nothing and does not raise",
      d.runtime_edges({"dist-tags": {"latest": "9.9.9"}, "versions": {}}, "npm"), [])
check("requires_dist null expands to nothing and does not raise",
      d.runtime_edges({"info": {"requires_dist": None}}, "pypi"), [])

# --- is_extra_only, directly, with the pair that makes it non-trivial ---------
check("extra == is optional", d.is_extra_only('x; extra == "y"'), True)
check("a requirement with NO marker is never optional", d.is_extra_only("x>=1"), False)
check("the word extra inside a NAME is not a marker",
      d.is_extra_only("extras-require>=1.0"), False)

# --- scope: a zero denominator is a path fault, not a clean sweep (P355) ------
with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as f:
    empty = f.name
r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "depth2_pinned.py"),
                    empty, "2026-10-07"], capture_output=True, cwd=HERE)
os.unlink(empty)
check("exits 2 on an empty denominator", r.returncode, 2)

TOTAL = 21
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
