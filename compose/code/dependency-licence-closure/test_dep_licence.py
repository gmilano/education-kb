#!/usr/bin/env python3
"""Offline control for dep_licence.py. No network: every fixture is inline.

Run: python3 test_dep_licence.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dep_licence import (classify_licence, pypi_licence, npm_licence,
                         parse_requirements, parse_pyproject,
                         parse_package_json, parse_dependency_group, verdict)

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


# --- classification, and the substring trap that makes it necessary ---------
check("MIT", classify_licence("MIT"), "PERMISSIVE")
check("Apache", classify_licence("Apache-2.0"), "PERMISSIVE")
check("BSD-3", classify_licence("BSD-3-Clause"), "PERMISSIVE")
check("ISC", classify_licence("ISC"), "PERMISSIVE")

# The ordering control. All three contain the substring "GPL"; a naive sweep
# collapses them into one class and the whole instrument becomes noise.
check("AGPL is strong", classify_licence("AGPL-3.0"), "STRONG-COPYLEFT")
check("GPL is strong", classify_licence("GPL-3.0-only"), "STRONG-COPYLEFT")
check("LGPL is WEAK not strong", classify_licence("LGPL-2.1"), "WEAK-COPYLEFT")
check("MPL is weak", classify_licence("MPL-2.0"), "WEAK-COPYLEFT")
check("Mozilla prose", classify_licence("Mozilla Public License 2.0"), "WEAK-COPYLEFT")

# Non-commercial outranks everything: it blocks the engagement outright.
check("CC-BY-NC", classify_licence("CC-BY-NC-4.0"), "NONCOMMERCIAL")
check("NC prose", classify_licence("Creative Commons Non-Commercial"), "NONCOMMERCIAL")

check("None is UNKNOWN", classify_licence(None), "UNKNOWN")
check("empty is UNKNOWN", classify_licence("   "), "UNKNOWN")
check("junk is UNKNOWN", classify_licence("see LICENSE file"), "UNKNOWN")

# Defect found by running this instrument against the real shelf and reading the
# output: defusedxml publishes the string "PSFL", the Python Software Foundation
# Licence, which is permissive -- and the first version of this classifier only
# knew the bare token "PSF", so it reported a false UNKNOWN on a clean package.
# A false UNKNOWN is not harmless here: UNKNOWN is what this KB escalates on.
check("PSFL is permissive", classify_licence("PSFL"), "PERMISSIVE")
check("PSF bare still works", classify_licence("PSF"), "PERMISSIVE")
check("PSF prose", classify_licence("Python Software Foundation License"),
      "PERMISSIVE")
check("HPND", classify_licence("Historical Permission Notice and Disclaimer"),
      "PERMISSIVE")
# The live control for the headline of this pass: PyMuPDF's own published field.
# The free half of the dual grant is AGPL, so the dual string must classify
# STRONG-COPYLEFT, not PERMISSIVE and not UNKNOWN.
check("PyMuPDF dual string",
      classify_licence("Dual Licensed - GNU AFFERO GPL 3.0 or Artifex Commercial License"),
      "STRONG-COPYLEFT")
# "Dual License" naming neither half is genuinely unreadable from the field --
# python-dateutil publishes exactly this. UNKNOWN is the correct verdict, and
# the README says it must be resolved at the repository layer, not guessed.
check("Dual License names nothing", classify_licence("Dual License"), "UNKNOWN")

# npm legacy shapes
check("npm dict", classify_licence({"type": "MIT", "url": "x"}), "PERMISSIVE")
check("npm list picks worst", classify_licence([{"type": "MIT"}, {"type": "GPL-3.0"}]),
      "STRONG-COPYLEFT")

# --- PyPI field migration: the live defect this instrument was built around --
# pypdf really does serve license=null with license_expression=BSD-3-Clause.
# A reader that knows only the old field calls it UNKNOWN and reports a false
# finding.
check("PEP639 expression wins",
      pypi_licence({"info": {"license": None, "license_expression": "BSD-3-Clause"}}),
      ("BSD-3-Clause", "license_expression"))
check("legacy license field",
      pypi_licence({"info": {"license": "MIT", "classifiers": []}}),
      ("MIT", "license"))
check("classifier fallback",
      pypi_licence({"info": {"license": "", "classifiers":
                             ["Programming Language :: Python",
                              "License :: OSI Approved :: Apache Software License"]}}),
      ("Apache Software License", "classifier"))
check("absent everywhere",
      pypi_licence({"info": {"license": None, "classifiers": []}}),
      (None, "absent"))
# A project that pastes its whole licence text into the field must not blow up.
long_text = "Copyright (c) 2026 Somebody\n" + ("Permission is hereby granted " * 40)
got_val, got_src = pypi_licence({"info": {"license": long_text}})
check("long text truncated", len(got_val) <= 120, True)
check("long text still classifies", classify_licence(got_val), "UNKNOWN")

# --- npm packument ---------------------------------------------------------
check("npm latest version licence",
      npm_licence({"dist-tags": {"latest": "4.14.0"},
                   "versions": {"4.14.0": {"license": "MPL-2.0"},
                                "1.0.0": {"license": "MIT"}}}),
      ("MPL-2.0", "version.license"))
check("npm root fallback",
      npm_licence({"dist-tags": {"latest": "9.9.9"}, "versions": {}, "license": "ISC"}),
      ("ISC", "root.license"))
check("npm absent", npm_licence({"dist-tags": {}, "versions": {}}), (None, "absent"))

# --- manifest parsing ------------------------------------------------------
check("requirements basic",
      parse_requirements("requests>=2.0\nnumpy==1.26.0\n# a comment\n\n"),
      ["numpy", "requests"])
check("requirements drops flags and extras",
      parse_requirements("-r base.txt\n--index-url https://x\nuvicorn[standard]>=0.2\n"
                         "pkg ; python_version<'3.9'\n-e .\n"),
      ["pkg", "uvicorn"])

check("pep621 inline array",
      parse_pyproject('[project]\ndependencies = ["fastapi>=0.1", "pydantic"]\n'),
      ["fastapi", "pydantic"])
check("pep621 multiline array",
      parse_pyproject('[project]\nname = "x"\ndependencies = [\n  "httpx>=0.27",\n'
                      '  "rich",\n]\n[project.optional-dependencies]\n'
                      'dev = ["pytest"]\n'),
      ["httpx", "rich"])
check("poetry table, python excluded",
      parse_pyproject('[tool.poetry.dependencies]\npython = "^3.11"\n'
                      'langchain = "^0.2"\n[tool.poetry.group.dev.dependencies]\n'
                      'black = "*"\n'),
      ["langchain"])

check("package.json runtime only",
      parse_package_json('{"dependencies":{"axe-core":"^4.6.0","Zod":"^3"},'
                         '"devDependencies":{"typescript":"^5"}}'),
      ["axe-core", "zod"])
check("package.json malformed", parse_package_json("{not json"), [])
check("package.json empty", parse_package_json("{}"), [])

# --- the Kolibri shape: canonical field empty, truth in a PEP 735 group -------
# Reproduced from the live manifest. [project].dependencies is "[]" and the
# runtime set is [dependency-groups] base. Both halves are asserted, because the
# dangerous half is the FIRST one: a reader of the canonical field alone gets a
# confident zero rather than a visible failure.
_KOLIBRI = """[project]
name = "kolibri"
dependencies = []
[dependency-groups]
base = [
  "django>=4.2,<5.0",
  "django-filter",
]
dev = ["pytest"]
"""
check("kolibri canonical field is empty", parse_pyproject(_KOLIBRI), [])
check("kolibri runtime set is in the group",
      parse_dependency_group(_KOLIBRI, "base"), ["django", "django-filter"])
check("group is named, not guessed",
      parse_dependency_group(_KOLIBRI, "dev"), ["pytest"])
check("absent group yields nothing",
      parse_dependency_group(_KOLIBRI, "nosuchgroup"), [])
check("inline group array",
      parse_dependency_group('[dependency-groups]\nbase = ["httpx", "rich"]\n', "base"),
      ["httpx", "rich"])

# --- depth-2 closure findings, 2026-10-07 (p438) ---------------------------
# Each positive is paired with the negative that forbids a lazy fix.
check("BlueOak-1.0.0 is permissive, not UNKNOWN",
      classify_licence("BlueOak-1.0.0"), "PERMISSIVE")
check("Blue Oak Model License 1.0.0, spelled out",
      classify_licence("Blue Oak Model License 1.0.0"), "PERMISSIVE")
check("the new rule does not swallow a copyleft that merely mentions oak",
      classify_licence("GPL-3.0-only (Oakland fork)"), "STRONG-COPYLEFT")
check("a licence FIELD that is TEXT defers to the classifier",
      pypi_licence({"info": {
          "license": "Copyright (c) 2015 Project Jupyter Contributors\nAll rights "
                     "reserved.\n\nRedistribution and use in source and binary forms, "
                     "with or without modification, are permitted provided that the "
                     "following conditions are met:",
          "classifiers": ["License :: OSI Approved :: BSD License"]}}),
      ("BSD License", "classifier (license field is text)"))
check("a SHORT licence field is still the licence, classifier or not",
      pypi_licence({"info": {"license": "MPL-2.0",
                             "classifiers": ["License :: OSI Approved :: MIT License"]}}),
      ("MPL-2.0", "license"))
check("licence TEXT with NO classifier is still reported, not dropped",
      pypi_licence({"info": {"license": "x" * 200, "classifiers": []}})[1], "license")
check("no field and no classifier is absent, which is a finding not a default",
      pypi_licence({"info": {"license": None, "classifiers": []}}), (None, "absent"))

# --- verdict ordering ------------------------------------------------------
check("clean", verdict("PERMISSIVE", ["PERMISSIVE", "PERMISSIVE"]), "CLEAN")
check("weak", verdict("PERMISSIVE", ["PERMISSIVE", "WEAK-COPYLEFT"]), "REVIEW-WEAK")
check("strong beats weak",
      verdict("PERMISSIVE", ["WEAK-COPYLEFT", "STRONG-COPYLEFT"]), "REVIEW-STRONG")
check("nc beats strong",
      verdict("PERMISSIVE", ["STRONG-COPYLEFT", "NONCOMMERCIAL"]), "BLOCKER")
check("unknown is reported, not swallowed",
      verdict("PERMISSIVE", ["PERMISSIVE", "UNKNOWN"]), "REVIEW-UNKNOWN")

TOTAL = 55
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
