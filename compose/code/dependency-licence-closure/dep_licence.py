#!/usr/bin/env python3
"""Classify the licences of a project's DECLARED DIRECT dependencies.

This KB verifies the licence of each shelf repository from its own LICENSE
payload. That answers "what is this project?". It does not answer "what does
this project install?", which is the question that decides whether Globant can
redistribute a build of it to a client.

Pure functions only; no network. The fetching half lives in resolve.sh so the
classifier can be tested offline.
"""
import json
import re

# Order matters. "AGPL-3.0" contains "GPL", "LGPL-2.1" contains "GPL", and a
# naive substring sweep therefore reports every copyleft licence as STRONG.
# Non-commercial is probed first because "CC-BY-NC" names no GPL at all yet is
# the hardest blocker of the four for a commercial engagement.
_RULES = [
    ("NONCOMMERCIAL", [r"\bNC\b", r"non-?commercial", r"CC-BY-NC", r"CC\s*BY\s*NC"]),
    ("STRONG-COPYLEFT", [r"\bAGPL", r"AFFERO"]),
    ("WEAK-COPYLEFT", [r"\bLGPL", r"\bMPL", r"MOZILLA PUBLIC", r"\bEPL",
                       r"ECLIPSE PUBLIC", r"\bCDDL"]),
    ("STRONG-COPYLEFT", [r"\bGPL", r"GENERAL PUBLIC LICENSE"]),
    ("PERMISSIVE", [r"\bMIT\b", r"APACHE", r"\bBSD\b", r"BSD-\d", r"\bISC\b",
                    r"\bZLIB\b", r"UNLICENSE", r"\b0BSD\b", r"PYTHON-2",
                    r"\bPSFL?\b", r"PYTHON SOFTWARE FOUNDATION",
                    r"HISTORICAL PERMISSION", r"\bHPND\b",
                    r"PUBLIC DOMAIN", r"\bCC0\b", r"BOOST",
                    # Blue Oak Model License 1.0.0 -- OSI-approved, permissive, and
                    # not recognised by any rule above.  Found by the depth-2 closure
                    # of 2026-10-07: `glob` and `sax`, two of the most widely installed
                    # packages on npm, both declare `BlueOak-1.0.0` and both came back
                    # UNKNOWN.  An UNKNOWN on a package at that install count is not a
                    # neutral gap -- it is the classifier failing on a licence that is
                    # safer than several it already passes.
                    r"BLUE\s*OAK", r"BLUEOAK"]),
]


def classify_licence(raw):
    """Map a licence string to one of five classes.

    Returns UNKNOWN for None, empty, or anything no rule recognises. UNKNOWN is
    a finding, not a default: it means the dependency ships without a readable
    grant, which is the condition this KB has already catalogued three ways at
    the repository layer.
    """
    if raw is None:
        return "UNKNOWN"
    if isinstance(raw, dict):            # legacy npm {"type": "...", "url": ...}
        raw = raw.get("type") or ""
    if isinstance(raw, list):            # npm "licenses": [{...}, {...}]
        parts = [classify_licence(x) for x in raw]
        for cls in ("NONCOMMERCIAL", "STRONG-COPYLEFT", "WEAK-COPYLEFT", "PERMISSIVE"):
            if cls in parts:
                return cls
        return "UNKNOWN"
    text = str(raw).strip()
    if not text:
        return "UNKNOWN"
    upper = text.upper()
    for cls, pats in _RULES:
        for p in pats:
            if re.search(p, upper, re.IGNORECASE):
                return cls
    return "UNKNOWN"


def pypi_licence(payload):
    """Read a licence out of a pypi.org/pypi/<name>/json payload.

    PEP 639 moved the value: modern packages leave ``info.license`` empty and
    carry ``info.license_expression`` instead, and a reader that only knows the
    old field classifies them UNKNOWN. pypdf is the live control for this --
    ``license`` is null, ``license_expression`` is BSD-3-Clause. Classifiers are
    the third place to look, because some packages populate only those.
    """
    info = (payload or {}).get("info") or {}
    expr = info.get("license_expression")
    if expr and str(expr).strip():
        return str(expr).strip(), "license_expression"
    lic = info.get("license")
    classifier = None
    for c in info.get("classifiers") or []:
        if c.startswith("License ::"):
            classifier = c.split("::")[-1].strip()
            break
    if lic and str(lic).strip():
        text = str(lic).strip()
        # Some projects dump their entire licence TEXT into this field.  Truncating
        # it to 120 characters and classifying the truncation is how
        # `jupyterlab-pygments` -- a plain BSD-3-Clause package -- came back UNKNOWN
        # in the depth-2 closure of 2026-10-07: its `license` field opens
        # "Copyright (c) 2015 Project Jupyter Contributors\nAll rights reserved."
        # and names no licence in its first 120 characters.  When the field is TEXT
        # rather than a NAME and a classifier exists, the classifier is the better
        # datum; the field is still reported when there is no classifier.
        if len(text) > 80 and classifier:
            return classifier, "classifier (license field is text)"
        return text[:120], "license"
    if classifier:
        return classifier, "classifier"
    return None, "absent"


def npm_licence(payload):
    """Read a licence out of a registry.npmjs.org/<name> packument."""
    d = payload or {}
    latest = ((d.get("dist-tags") or {}).get("latest"))
    ver = ((d.get("versions") or {}).get(latest)) or {}
    for field, src in (("license", "version.license"), ("licenses", "version.licenses")):
        if ver.get(field):
            return ver[field], src
    for field, src in (("license", "root.license"), ("licenses", "root.licenses")):
        if d.get(field):
            return d[field], src
    return None, "absent"


_PY_NAME = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)")


def _clean_py_req(spec):
    """Strip version pins, extras and environment markers off a requirement."""
    spec = spec.split(";")[0].strip()          # drop env marker
    spec = spec.split("#")[0].strip()          # drop comment
    if not spec or spec.startswith("-"):       # -r other.txt, -e ., --flags
        return None
    spec = spec.split("[")[0]                  # drop extras
    m = _PY_NAME.match(spec)
    return m.group(1).lower() if m else None


def parse_requirements(text):
    """Direct dependency names from a requirements.txt."""
    out = []
    for line in (text or "").splitlines():
        name = _clean_py_req(line)
        if name:
            out.append(name)
    return sorted(set(out))


def parse_pyproject(text):
    """Direct runtime dependency names from a pyproject.toml.

    Deliberately a line scanner rather than a TOML parse: this has to read
    Poetry's ``[tool.poetry.dependencies]`` table and PEP 621's ``dependencies``
    array, and the environment cannot be assumed to have tomllib for every
    Python it runs under. Only the runtime tables are read -- dev and test
    extras do not ship to a client, so a copyleft test dependency is not the
    same finding as a copyleft runtime one.
    """
    out, section, in_pep621 = [], None, False
    for line in (text or "").splitlines():
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            section, in_pep621 = s, False
            continue
        if re.match(r"^dependencies\s*=\s*\[", s):
            in_pep621 = (section in ("[project]", None)) or section == "[project]"
            rest = s.split("[", 1)[1]
            for chunk in re.findall(r'"([^"]+)"|\'([^\']+)\'', rest):
                nm = _clean_py_req(chunk[0] or chunk[1])
                if nm:
                    out.append(nm)
            if "]" in rest:
                in_pep621 = False
            continue
        if in_pep621:
            for chunk in re.findall(r'"([^"]+)"|\'([^\']+)\'', s):
                nm = _clean_py_req(chunk[0] or chunk[1])
                if nm:
                    out.append(nm)
            if "]" in s:
                in_pep621 = False
            continue
        if section and re.search(r"poetry\.dependencies\]$", section):
            if "=" in s and not s.startswith("#"):
                nm = _clean_py_req(s.split("=")[0])
                if nm and nm != "python":
                    out.append(nm)
    return sorted(set(out))


def parse_dependency_group(text, group="base"):
    """Names from a PEP 735 ``[dependency-groups]`` table entry.

    Needed because of a live case this instrument hit on its first run:
    Kolibri's ``[project]`` table declares ``dependencies = []`` -- literally
    empty -- and its real runtime set lives in ``[dependency-groups] base``,
    resolved at build time by ``make staticdeps``. Its ``requirements.txt`` is a
    deliberate empty sink. A sweep that reads only the canonical PEP 621 field,
    or that trusts a 200 on ``requirements.txt``, reports Kolibri as a
    zero-dependency project. That is not a missing measurement, it is a
    confident wrong one, which is worse.

    The group is named by the caller rather than guessed, because PEP 735 groups
    are usually dev tooling and only this project uses one for runtime.
    """
    out, in_group = [], False
    section = None
    for line in (text or "").splitlines():
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            section, in_group = s, False
            continue
        if section == "[dependency-groups]" and re.match(
                r"^%s\s*=\s*\[" % re.escape(group), s):
            in_group = True
            rest = s.split("[", 1)[1]
            for chunk in re.findall(r'"([^"]+)"|\'([^\']+)\'', rest):
                nm = _clean_py_req(chunk[0] or chunk[1])
                if nm:
                    out.append(nm)
            if "]" in rest:
                in_group = False
            continue
        if in_group:
            for chunk in re.findall(r'"([^"]+)"|\'([^\']+)\'', s):
                nm = _clean_py_req(chunk[0] or chunk[1])
                if nm:
                    out.append(nm)
            if "]" in s:
                in_group = False
    return sorted(set(out))


def parse_package_json(text):
    """Runtime ``dependencies`` from a package.json -- not devDependencies."""
    try:
        d = json.loads(text or "{}")
    except (ValueError, TypeError):
        return []
    return sorted({k.lower() for k in (d.get("dependencies") or {})})


def verdict(project_class, dep_classes):
    """Does the dependency closure contradict the project's own licence?

    A permissive project whose declared runtime closure pulls in copyleft or
    non-commercial code cannot be handed to a client as "MIT, build on it
    freely" without a linkage review. This returns where to look; it is not a
    legal conclusion, and the README says so.
    """
    if "NONCOMMERCIAL" in dep_classes:
        return "BLOCKER"
    if "STRONG-COPYLEFT" in dep_classes:
        return "REVIEW-STRONG"
    if "WEAK-COPYLEFT" in dep_classes:
        return "REVIEW-WEAK"
    if "UNKNOWN" in dep_classes:
        return "REVIEW-UNKNOWN"
    return "CLEAN"
