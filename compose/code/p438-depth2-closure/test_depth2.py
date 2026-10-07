#!/usr/bin/env python3
"""Controls for p438. Offline; no network.

The thing this instrument can get wrong is its SCOPE, not its arithmetic: an
expansion that counts optional dependencies describes an install nobody
performs, and one that drops platform-conditional dependencies misses licence
obligations that bind on some machines. Every control below is a scope control,
and each is paired with the case that must still be KEPT.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from depth2 import is_extra_only, runtime_deps

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append(f"{label}: got {got!r}, want {want!r}")
        print(f"FAIL {label}: got {got!r}, want {want!r}")
    else:
        print(f"PASS {label}")


# --- the `extra` marker: optional, therefore out of scope -------------------
check("extra-gated requirement is optional",
      is_extra_only('PySocks!=1.5.7,>=1.5.6; extra == "socks"'), True)
check("extra-gated with single quotes",
      is_extra_only("urllib3[socks]; extra == 'socks'"), True)
check("a plain requirement is NOT optional",
      is_extra_only("certifi>=2017.4.17"), False)
# The pair that matters: a marker is not an extra just because it is a marker.
check("python_version marker is KEPT -- it installs on some interpreters",
      is_extra_only('tomli>=1.1.0; python_version < "3.11"'), False)
check("sys_platform marker is KEPT -- a Windows-only licence still binds",
      is_extra_only('pywin32>=223; sys_platform == "win32"'), False)
check("a combined marker with extra IS optional",
      is_extra_only('x>=1; python_version < "3.11" and extra == "test"'), True)

# --- PyPI expansion ---------------------------------------------------------
PYPI_DOC = {"info": {"requires_dist": [
    "charset-normalizer<4,>=2",
    "idna<4,>=2.5",
    "certifi>=2017.4.17",
    'PySocks!=1.5.7,>=1.5.6; extra == "socks"',
    'chardet<6,>=3.0.2; extra == "use-chardet-on-py3"',
    'tomli>=1.1.0; python_version < "3.11"',
]}}
check("pypi runtime deps: extras dropped, markers kept, names normalised",
      runtime_deps("requests", "pypi", PYPI_DOC),
      ["certifi", "charset-normalizer", "idna", "tomli"])
check("pypi package with requires_dist null expands to nothing",
      runtime_deps("x", "pypi", {"info": {"requires_dist": None}}), [])

# --- npm expansion ----------------------------------------------------------
NPM_DOC = {
    "dist-tags": {"latest": "2.0.0"},
    "versions": {
        "1.0.0": {"dependencies": {"old-dep": "^1"}},
        "2.0.0": {
            "dependencies": {"axios": "^1.6.0", "zod": "3.23.8"},
            "devDependencies": {"jest": "^29"},
            "peerDependencies": {"react": ">=18"},
            "optionalDependencies": {"fsevents": "^2"},
        },
    },
}
check("npm runtime deps: only `dependencies`, and only of the LATEST version",
      runtime_deps("p", "npm", NPM_DOC), ["axios", "zod"])
check("npm package with no dependencies key expands to nothing",
      runtime_deps("p", "npm", {"dist-tags": {"latest": "1.0.0"},
                                "versions": {"1.0.0": {}}}), [])
check("npm doc with a dangling dist-tag does not raise",
      runtime_deps("p", "npm", {"dist-tags": {"latest": "9.9.9"}, "versions": {}}), [])

TOTAL = 13
if FAIL:
    print(f"\nFAIL ({len(FAIL)} of {TOTAL})")
    sys.exit(1)
print(f"\n{TOTAL}/{TOTAL} assertions pass, no network")
