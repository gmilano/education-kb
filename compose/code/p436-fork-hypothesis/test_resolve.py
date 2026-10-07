#!/usr/bin/env python3
"""Controls for p436. Offline: every fixture is a real payload captured 2026-10-07.

Rule 2 of P126: a control set made only of pairs that agree never exercises the
detection. Each positive here is matched by the false-positive class that would
make it unreadable if the instrument did not separate them.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resolve_homepage as R

FX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def load(n):
    with open(os.path.join(FX, n), encoding="utf-8") as fh:
        return fh.read()


# (name, raw_path -> body) stubs, keyed exactly as the probe asks for them.
CASES = [
    # 1. fork lineage -- the positive the instrument exists for.
    ("fork lineage: ucfopen/pylti1.3 declares dmitry-viskov/pylti1.3",
     "ucfopen/pylti1.3",
     {"setup.py": load("ucfopen-pylti1.3-setup.py")},
     {"pypi/PyLTI1p3": load("pypi-PyLTI1p3.json")},
     ("pypi", "PyLTI1p3", "UPSTREAM", "dmitry-viskov/pylti1.3")),
    # 2. name collision -- `private: true` must stop the resolution dead.
    ("name collision: a private workspace manifest is NOT resolved",
     "kaorii-ako/Shiori-v1",
     {"package.json": load("kaorii-ako-Shiori-v1-package.json")},
     {},
     ("private", "shiori", "PRIVATE-MANIFEST", "-")),
    # 3. multi-repo publisher -- the SECOND false positive, and the control that shows
    #    ONE rule closes both.  `langfuse/langfuse`'s root manifest is ALSO
    #    `"private": true`: the npm name `langfuse` belongs to the sibling SDK repo
    #    `langfuse/langfuse-js`, so resolving it would have published a "fork
    #    hypothesis" between two repositories of the same owner, neither forked from
    #    the other.  The first build of this test asserted UPSTREAM here and the
    #    `private` rule failed it -- correctly.
    ("multi-repo publisher: langfuse's root manifest is private too",
     "langfuse/langfuse",
     {"package.json": load("langfuse-package.json")},
     {"npm/langfuse": load("npm-langfuse.json")},
     ("private", "langfuse", "PRIVATE-MANIFEST", "-")),
    # 4. SELF -- the negative that forbids an instrument that answers UPSTREAM always.
    #    It also pins the setup.cfg probe: this repo's `pyproject.toml` carries ONLY
    #    tool config, with no `[project]` table, so a probe list of
    #    pyproject/setup.py/package.json reports NO-MANIFEST for a package that is on
    #    PyPI -- "no channel" and "nothing published" collapsing into one string.
    ("self: academic-innovation/django-lti declares itself, via setup.cfg",
     "academic-innovation/django-lti",
     {"pyproject.toml": load("django-lti-pyproject.toml"),
      "setup.cfg": load("django-lti-setup.cfg")},
     {"pypi/django-lti": load("pypi-django-lti.json")},
     ("pypi", "django-lti", "SELF", "academic-innovation/django-lti")),
    # 5. NO-PACKAGE -- a manifest that the registry has never seen.  This is the class
    #    that must NOT be reported as "no upstream": it is "no channel".
    ("no package: ff-ltitoolkit's repo manifest, registry 404",
     "CNIT-Organization/ltitoolkit",
     {"pyproject.toml": load("ltitoolkit-pyproject.toml")},
     {},
     ("pypi", "ff-ltitoolkit", "NO-PACKAGE", "-")),
]


def main():
    ok = n = 0
    for name, slug, raws, regs, want in CASES:
        n += 1

        def fake_get(url, timeout=25, _raws=raws, _regs=regs, _slug=slug):
            pre = f"https://raw.githubusercontent.com/{_slug}/HEAD/"
            if url.startswith(pre):
                p = url[len(pre):]
                return (200, _raws[p]) if p in _raws else (404, "")
            for key, body in _regs.items():
                eco, pkg = key.split("/", 1)
                if eco == "pypi" and url == f"https://pypi.org/pypi/{pkg}/json":
                    return 200, body
                if eco == "npm" and url == f"https://registry.npmjs.org/{pkg}":
                    return 200, body
            return 404, ""

        orig, R.get = R.get, fake_get
        try:
            got = R.one(slug)[1:]
        finally:
            R.get = orig
        if got == want:
            ok += 1
            print(f"PASS {name}")
        else:
            print(f"FAIL {name}: want {want}, got {got}")

    # Negative control, stated as an assertion: an instrument that ignored `private`
    # would resolve case 2 to a DELETED repo for an UNRELATED project.  Assert the
    # collision is real, so the control is not a tautology.
    n += 1
    npm_shiori = json.loads(load("npm-shiori.json"))
    repo = npm_shiori["repository"]["url"]
    desc = npm_shiori["description"]
    local = json.loads(load("kaorii-ako-Shiori-v1-package.json"))["description"]
    if "shiorijs/shiori" in repo and "discord" in desc.lower() and "discord" not in local.lower():
        ok += 1
        print("PASS negative control: the npm name genuinely belongs to another project")
    else:
        print("FAIL negative control: the collision fixture no longer collides")

    print(f"\n{ok}/{n} checks passed")
    return 0 if ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
