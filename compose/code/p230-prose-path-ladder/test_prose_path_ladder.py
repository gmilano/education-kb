#!/usr/bin/env python3
"""p230 controls. Run from THIS directory (p229's `-I` finding: `python3 -I` strips the
script's directory from sys.path, so an import-bearing suite only passes from inside its
own folder). `make hooks` cd's in."""
import re
import sys
from pathlib import Path

# p229 measured why the licence gate stayed a one-off for eleven passes: `python3 -I`
# strips the script's directory from sys.path, so an import-bearing suite dies from the
# repo root and passes from inside its folder. p230 makes the suite say so itself rather
# than relying on the caller to cd — it runs under `-I`, from anywhere.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from harvest import SLUG_RE, slugs_on, paths_on
from lazy_lint import expand, first_class_after, scan as lint_scan

FAIL = []


def check(name, got, want):
    if got != want:
        FAIL.append(f"{name}: got {got!r}, want {want!r}")


# ---------------------------------------------------------------- ACTION TD
# The defect, stated as a test. Each of these is a REAL repository on these shelves
# that p228's lazy regex truncated at its first dot.
for url, want in [
    ("https://github.com/processing/p5.js",                 ["processing/p5.js"]),
    ("https://github.com/dmitry-viskov/pylti1.3",           ["dmitry-viskov/pylti1.3"]),
    ("https://github.com/jdolny/OneRoster.NET",             ["jdolny/OneRoster.NET"]),
    ("https://github.com/nakafaai/nakafa.com",              ["nakafaai/nakafa.com"]),
    ("https://github.com/JuliaPluto/Pluto.jl",              ["JuliaPluto/Pluto.jl"]),
    ("https://github.com/eclipse/paho.mqtt.java",           ["eclipse/paho.mqtt.java"]),
    ("https://github.com/ramsrigouthamg/Questgen.ai",       ["ramsrigouthamg/Questgen.ai"]),
    ("https://github.com/gener8v/gener8v.tools.pii-scanner", ["gener8v/gener8v.tools.pii-scanner"]),
]:
    check(f"TD dotted {want[0]}", slugs_on(url), want)

# A sentence-final period is STRIPPED, not stopped at — the distinction the fix rests on.
check("TD sentence-final period", slugs_on("see https://github.com/moodle/moodle."), ["moodle/moodle"])
check("TD period then space",     slugs_on("https://github.com/a/b.js, and more"),   ["a/b.js"])
check("TD markdown link",         slugs_on("[x](https://github.com/processing/p5.js)"), ["processing/p5.js"])
check("TD backticked",            slugs_on("`https://github.com/a/b.c`"),            ["a/b.c"])

# T230-1: a clone URL's `.git` suffix is not part of the repository name. The lazy regex
# hid this by truncating before it ever reached the suffix.
check("T230-1 .git suffix", slugs_on("https://github.com/bruchris/canvas-lms-mcp.git"),
      ["bruchris/canvas-lms-mcp"])

# T224-2 preserved: a dotted OWNER is a hostname, never a slug.
check("T224-2 dotted owner", slugs_on("https://github.com.evil/a/b"), [])

# Non-regression: the undotted majority behaves exactly as p228's regex did.
check("undotted unchanged", slugs_on("https://github.com/moodle/moodle)"), ["moodle/moodle"])
check("two on one line",
      slugs_on("https://github.com/a/b and https://github.com/c/d.e"), ["a/b", "c/d.e"])

# ---------------------------------------------------------------- ACTION TA
# The probe list is harvested by SHAPE, so a name no pass has invented is found.
check("TA recorded path",  paths_on("read at `main/COPYING.txt`"),        ["COPYING.txt"])
check("TA subdir path",    paths_on("`AmazonBedrock/LICENSE`"),           ["AmazonBedrock/LICENSE"])
check("TA HEAD ref strip", paths_on("`HEAD/LICENSE`"),                    ["LICENSE"])
# T230-2: the shape that finds a licence FILE also finds instruments, predicates and
# status tokens. A probe-list entry must be a path whose basename NAMES THE GRANT.
check("T230-2 instrument",  paths_on("`lib/license_family.sh`"), [])
check("T230-2 predicate",   paths_on("`is_licence_path`"),       [])
check("T230-2 status token", paths_on("`NO_LICENCE_FILE`"),      [])
check("T230-2 pass dir",    paths_on("`p147-licence-language`"), [])
# T230-3: a hostname-first token is a URL, not a repository path.
check("T230-3 hostname", paths_on("`apache.org/licenses/LICENSE-2.0.txt`"), [])
# T230-4: a probe path that is also a slug on these shelves is a REPOSITORY.
check("T230-4 slug not path",
      paths_on("`spdx/license-list-data`", known_slugs={"spdx/license-list-data"}), [])

# ---------------------------------------------------------------- ACTION TB
# The lint's own arithmetic: expand both classes, intersect.
check("TB expand range",  "".join(sorted(expand("a-c"))), "abc")
check("TB expand escape", " " in expand(r"\s"), True)
# POSITIVE CONTROL — p228's SLUG_RE must be flagged, with `.` as the overlap.
P228 = r"""SLUG_RE = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*?)(?=[)\s`,.;:'\"\]]|$)")"""  # lazy-lint: fixture
m = re.search(r"\[([^\]\\]*(?:\\.[^\]\\]*)*)\]\s*[*+]\?", P228)
term = first_class_after(P228, m.end())
check("TB positive control flagged", bool(expand(m.group(1)) & expand(term)), True)
check("TB overlap is the dot", "".join(sorted(expand(m.group(1)) & expand(term))), ".")
# T230-6: the terminator class of that very defect BEGINS with `)`, so a `([^)]*)` capture
# of the lookahead body reads nothing. The first draft of this lint scored 0 findings —
# including on its own positive control — for exactly that reason.
check("T230-6 terminator starts with )", term.startswith(")"), True)
# NEGATIVE CONTROL — p230's own greedy SLUG_RE must NOT be flagged.
GREEDY = r"""github\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)(?=[)\s`,;:'\"\]]|$)"""
check("TB negative control clean", bool(re.search(r"\[[^\]]*\]\s*[*+]\?", GREEDY)), False)
# A lazy quantifier with a DISJOINT terminator is safe and must not be reported.
check("TB disjoint terminator safe", bool(expand("A-Za-z0-9_.-") & expand(r")\s\]#,")), False)

# ---------------------------------------------------------------- summary
if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  " + f)
    sys.exit(1)
# T230-8: the lint must not report this file's own positive-control fixture.
own = lint_scan(Path(__file__))
check("T230-8 fixture not self-reported", own, [])
if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  " + f)
    sys.exit(1)
print("p230-prose-path-ladder: 33/33 controls pass")
