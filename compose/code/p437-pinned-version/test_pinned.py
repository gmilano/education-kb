#!/usr/bin/env python3
"""Controls for p437. Offline; no network.

Rule 2 of P126: the set must contain the case where the instrument FAILS, not
only cases where it agrees with itself. Here that means, for every specifier
class, a version that must be REJECTED as well as one that must be accepted --
otherwise an evaluator that returns True always would pass.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pinned import (satisfies_py, satisfies_npm, spec_class, vkey,
                    parse_pyproject, parse_requirements, parse_package_json)

PY = [
    # (spec, version, want)
    ("==1.4.2", "1.4.2", True),
    ("==1.4.2", "1.4.3", False),          # the exact pin must EXCLUDE the newer release
    (">=2.31", "2.32.0", True),
    (">=2.31", "2.30.0", False),
    ("~=1.4.2", "1.4.9", True),
    ("~=1.4.2", "1.5.0", False),          # ~= caps the last segment
    ("~=1.4.2", "1.4.1", False),
    (">=2.8,<3", "2.10.1", True),
    (">=2.8,<3", "3.0.0", False),         # the upper bound is the whole point of CAPPED
    ("==1.4.*", "1.4.7", True),
    ("==1.4.*", "1.5.0", False),
    ("!=1.4.2", "1.4.2", False),
    # A pre-release EXACT pin must resolve.  Both rows that this instrument first
    # reported NO-SATISFYING-RELEASE for -- `opentelemetry-semantic-conventions
    # ==0.65b0` and `webapp2==3.0.0b1`, both real lines of oppia's hash-pinned
    # requirements.txt -- ARE served by PyPI; the trailing line-continuation
    # backslash was being carried into the comparison.
    ("==0.65b0", "0.65b0", True),
    ("==0.65b0", "0.66b1", False),
    ("==3.0.0b1", "3.0.0b1", True),
    ("", "9.9.9", True),                  # no specifier accepts anything
]

NPM = [
    ("^1.2.3", "1.9.0", True),
    ("^1.2.3", "2.0.0", False),           # caret does not cross a major
    ("^1.2.3", "1.2.2", False),
    ("^0.2.3", "0.2.9", True),
    ("^0.2.3", "0.3.0", False),           # caret on 0.x does not cross a MINOR
    ("~1.2.3", "1.2.9", True),
    ("~1.2.3", "1.3.0", False),
    (">=18", "20.1.0", True),
    (">=18", "17.0.2", False),
    ("1.2.3", "1.2.3", True),
    ("1.2.3", "1.2.4", False),
    ("*", "0.0.1", True),
    ("^1.0.0 || ^2.0.0", "2.5.0", True),
    ("^1.0.0 || ^2.0.0", "3.0.0", False),
]

CLASSES = [
    ("==1.2.3", "pypi", "EXACT"),
    (">=2.31", "pypi", "FLOOR"),
    (">=2.8,<3", "pypi", "CAPPED"),
    ("~=1.4", "pypi", "CAPPED"),
    ("", "pypi", "ANY"),
    ("^1.2.3", "npm", "CAPPED"),
    ("~1.2.3", "npm", "CAPPED"),
    ("1.2.3", "npm", "EXACT"),
    (">=18", "npm", "FLOOR"),
    ("*", "npm", "ANY"),
    ("workspace:*", "npm", "NON-REGISTRY"),
    ("file:./common", "npm", "NON-REGISTRY"),   # the OATutor row pass 24 resolved by hand
]

PYPROJECT = '''
[project]
name = "x"
dependencies = [
  "pyjwt[crypto]>=2.8,<3",
  "requests>=2.31",
  "typing_extensions>=4.9",
  "defusedxml==0.7.1",
  "foo>=1.0; python_version < '3.11'",
  "faiss-cpu>=1.8.0,<2.0.0; python_version < '3.14'",
]
'''

REQS = """
# a comment
Django>=4.2,<5
pytz==2024.1
-r other.txt
semver
webencodings==0.5.1 \\
    --hash=sha256:a0af1213f3c2226497a97e2b3aa469f2c78f7977  \\
    --hash=sha256:b36a1c245f2d304965eb4e0a82848379241dc04b
"""

PKG = '{"dependencies": {"axios": "^1.6.0", "zod": "3.23.8", "@axe-core/puppeteer": "~4.9.0"}}'


def main():
    ok = n = 0
    for spec, v, want in PY:
        n += 1
        got = satisfies_py(v, spec)
        ok += got == want
        print(f"{'PASS' if got == want else 'FAIL'} pypi {spec!r} vs {v} -> {got} (want {want})")
    for spec, v, want in NPM:
        n += 1
        got = satisfies_npm(v, spec)
        ok += got == want
        print(f"{'PASS' if got == want else 'FAIL'} npm  {spec!r} vs {v} -> {got} (want {want})")
    for spec, eco, want in CLASSES:
        n += 1
        got = spec_class(spec, eco)
        ok += got == want
        print(f"{'PASS' if got == want else 'FAIL'} class {eco} {spec!r} -> {got} (want {want})")

    n += 1
    got = dict(parse_pyproject(PYPROJECT))
    # `3.14` must NOT appear: it is the right-hand side of an environment marker
    # quoted INSIDE a double-quoted TOML string, not a package.
    want = {"pyjwt": ">=2.8,<3", "requests": ">=2.31", "typing_extensions": ">=4.9",
            "defusedxml": "==0.7.1", "foo": ">=1.0", "faiss-cpu": ">=1.8.0,<2.0.0"}
    ok += got == want
    print(f"{'PASS' if got == want else 'FAIL'} parse pyproject: extras and env markers stripped, SPEC KEPT -> {got}")

    n += 1
    got = dict(parse_requirements(REQS))
    want = {"django": ">=4.2,<5", "pytz": "==2024.1", "semver": "",
            "webencodings": "==0.5.1"}   # the trailing line-continuation is NOT part of the spec
    ok += got == want
    print(f"{'PASS' if got == want else 'FAIL'} parse requirements -> {got}")

    n += 1
    got = dict(parse_package_json(PKG))
    want = {"axios": "^1.6.0", "zod": "3.23.8", "@axe-core/puppeteer": "~4.9.0"}
    ok += got == want
    print(f"{'PASS' if got == want else 'FAIL'} parse package.json -> {got}")

    # Pre-release demotion: the whole point is that `max()` over candidates must not
    # pick 2.0.0rc1 over 1.9.9 when both satisfy. Asserted on the key, not on a run.
    n += 1
    got = vkey("1.9.9") > vkey("2.0.0rc1")
    ok += (got is False)
    print(f"{'PASS' if got is False else 'FAIL'} vkey: 2.0.0rc1 ranks above 1.9.9 numerically "
          f"(the candidate filter, not the key, excludes pre-releases)")

    n += 1
    got = vkey("1.10.0") > vkey("1.9.0")
    ok += (got is True)
    print(f"{'PASS' if got is True else 'FAIL'} vkey: 1.10.0 > 1.9.0 (numeric, not lexicographic)")

    print(f"\n{ok}/{n} checks passed")
    return 0 if ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
