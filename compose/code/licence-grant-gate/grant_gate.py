#!/usr/bin/env python3
"""licence-grant-gate - the instrument of P453..P458 (pass 32, 2026-10-07).

Reads a GRANT, not a file's existence. Pure functions over payload text so the
suite runs offline; `probe_repo` is the only network entry point.

Environment facts measured on 2026-10-07 (re-measured, not inherited):
  curl -sI https://github.com/<repo>      -> 403
  curl     https://github.com/<repo>      -> 403   (GET, not just HEAD)
  https://api.github.com/repos/<repo>     -> 403
  raw.githubusercontent.com               -> 200/404, and CASE-SENSITIVE
So raw is the only channel, and no star count is readable.
"""
import re

# ---------------------------------------------------------------- P453
# raw.githubusercontent.com paths are case-sensitive. Proven by control:
#   pykt-team/pykt-toolkit/main/LICENSE   200
#   pykt-team/pykt-toolkit/main/license   404
#   pykt-team/pykt-toolkit/main/LiCeNsE   404
# openedx/XBlock keeps its grant in LICENSE.TXT - a caps extension. A probe
# list without it returns ABSENT for a real Apache-2.0 repo already shelved.
LICENCE_PATHS = (
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.TXT",
    "LICENCE", "LICENCE.md", "LICENCE.txt",
    "LICENSE.rst", "COPYING", "COPYING.txt", "COPYING.md",
    "LICENSE-MIT", "LICENSE-APACHE", "License.md", "License.txt", "license",
)

# ---------------------------------------------------------------- P454
# The existence fallback must not assume Markdown. openedx/XBlock ships
# README.rst (200) and has no README.md (404): probing only README.md
# reports a live repository as non-existent.
EXISTENCE_PATHS = ("README.md", "README.rst", "README.txt",
                   "pyproject.toml", "package.json", "setup.py")

FAMILIES = (
    # (family, ordered title-region probes)  GNU resolved title-first per P452.
    ("AGPL-3.0", ("GNU AFFERO GENERAL PUBLIC LICENSE",)),
    ("LGPL", ("GNU LESSER GENERAL PUBLIC LICENSE",)),
    ("GPL", ("GNU GENERAL PUBLIC LICENSE",)),
    ("Apache-2.0", ("Apache License",)),
    ("ECL-2.0", ("Educational Community License",)),
    ("MPL-2.0", ("Mozilla Public License",)),
    ("BSD", ("BSD ", "Redistribution and use in source and binary forms")),
    ("ISC", ("ISC License",)),
    ("MIT", ("MIT License", "Permission is hereby granted, free of charge")),
    ("CC", ("Creative Commons", "Attribution-NonCommercial", "CC BY")),
)

# ---------------------------------------------------------------- P455
# A 200 on a LICENSE path is NOT a grant. murderszn/open-tutor serves 869
# bytes at main/LICENSE whose text refuses one. Existence was never the test.
NON_GRANT_MARKERS = (
    "has not declared a project-wide reuse license",
    "does not grant additional rights",
    "is not itself a declaration of an open-source",
    "all rights reserved",
    "no licence has been chosen",
    "no license has been chosen",
    "a future project-wide license must be chosen",
)


def family_of(text):
    """Licence family from the payload's TITLE region (P452), or None."""
    if not text:
        return None
    head = text[:1200]
    for family, probes in FAMILIES:
        for p in probes:
            if p.lower() in head.lower():
                return family
    return None


def is_non_grant(text):
    """True when a licence-shaped payload explicitly withholds a grant (P455)."""
    if not text:
        return False
    low = " ".join(text.lower().split())
    return any(m in low for m in NON_GRANT_MARKERS)


def reads_as_grant(text):
    """(family, granted, reason). `granted` is the only commercial answer.

    A payload can be present, correctly named, served 200 and still grant
    nothing - that is P455, and it inverts the answer rather than shading it.
    """
    if not text or not text.strip():
        return (None, False, "empty payload")
    if is_non_grant(text):
        return (family_of(text), False, "explicit non-grant in payload (P455)")
    fam = family_of(text)
    if fam is None:
        return (None, False, "payload present but no known licence family in title region")
    return (fam, True, "grant read from payload")


# ---------------------------------------------------------------- P456
# A licence family inside a README's requirements/install/stack section is not
# a licence claim. formalms/formalms publishes no grant; the only "Apache" in
# its README is "- Apache (recommended) with mod_rewrite enabled" - a web
# server. A secondary source turned that into "Apache 2.0, no copyleft
# obligations", which is the exact conclusion the error manufactures.
REQUIREMENT_CUES = (
    "mod_rewrite", "web server", "webserver", "nginx", "php", "mysql",
    "mariadb", "recommended", "requirement", "prerequisite", "install",
    "apt-get", "yum ", "docker", "httpd", "server with",
)
AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")


def readme_licence_role(line):
    """'licence-claim' | 'requirement' | None for one README line (P456).

    Apache, nginx, MIT and BSD are each simultaneously the name of a licence
    and the name of something that is not one. Role, not presence.
    """
    if not line:
        return None
    low = line.lower()
    if not any(w in low for w in AMBIGUOUS_WORDS):
        return None
    if re.search(r"apache[\s-]*(licen[sc]e)?[\s-]*2(\.0)?", low) and "mod_rewrite" not in low:
        if not any(c in low for c in REQUIREMENT_CUES):
            return "licence-claim"
    if any(c in low for c in REQUIREMENT_CUES):
        return "requirement"
    if "licen" in low:
        return "licence-claim"
    return "requirement"


# ---------------------------------------------------------------- P457
# De-duplicate on the licence COPYRIGHT HOLDER, not the README hash. A renamed
# fork with an edited README defeats hash comparison (algenlab/adaptive-tutor
# vs zijinz456/OpenTutor: different README md5, same holder) but almost never
# rewrites the LICENSE copyright line - that is the one edit that looks like
# theft. Extends P160 (fork-lineage-audit), which keyed on inherited metadata.
HOLDER_RE = re.compile(
    r"copyright\s*(?:\(c\)|©)?\s*(?:[0-9]{4}(?:\s*[-–]\s*[0-9]{4})?)?[,\s]*(.+)",
    re.I)


# P459 - found by running this instrument live, not by reading it. The long-form
# licences (Apache-2.0, AGPL/GPL/LGPL, ECL-2.0, MPL) contain the WORD
# "copyright" inside their own BODY - Apache's definition of "Legal Entity",
# AGPL's section 2 - so a holder scraped from anywhere in the payload returns
# boilerplate: "owner or entity authorized by", "on the software, and (2)
# offer". Two unrelated Apache-2.0 repos then share a "holder" and
# same_project() merges them as forks. A false POSITIVE fork is worse than the
# miss P457 fixed, because it deletes a real project as a duplicate.
#
# Fix, in two parts: only a notice in the payload's HEAD region counts, and the
# captured string must look like a party rather than a clause.
HOLDER_HEAD_LINES = 12
BODY_BOILERPLATE = (
    "entity authorized by", "legal entity", "please see", "and (2)",
    "and (1)", "the software, and", "other entities that control",
    "direct or indirect", "no charge", "subject to the terms",
    "work shall mean", "means the", "shall mean",
)


def _looks_like_a_party(who):
    """Reject a clause fragment masquerading as a copyright holder (P459)."""
    if not who or len(who) < 2 or len(who) > 80:
        return False
    low = who.lower()
    if any(b in low for b in BODY_BOILERPLATE):
        return False
    if low.startswith(("or ", "and ", "on ", "the software", "that ", "which ")):
        return False
    first = who.lstrip("<([\"'")[:1]
    if not first:
        return False
    # a party starts with a capital, a digit or a non-latin script - not with a
    # lowercase english word, which is how a mid-sentence fragment begins.
    return first.isupper() or first.isdigit() or not first.isascii()


def holder_of(text):
    """Normalised copyright holder from a licence payload's HEAD, or None.

    Returns None for the long-form licences, which carry no party in their
    grant text - that is correct, not a miss (P459).
    """
    if not text:
        return None
    for line in text.splitlines()[:HOLDER_HEAD_LINES]:
        line = line.strip()
        if "copyright" not in line.lower():
            continue
        if "free software foundation" in line.lower():
            continue          # the GNU texts carry the FSF's own notice
        m = HOLDER_RE.search(line)
        if not m:
            continue
        who = m.group(1).strip(" .,\t")
        who = re.sub(r"\s+", " ", who)
        who = re.sub(r"^(the\s+)?", "", who, flags=re.I)
        if who.lower() in ("holder", "owner", "<year>", "author", "holders"):
            continue
        if _looks_like_a_party(who):
            return who
    return None


def same_project(payload_a, payload_b):
    """True when two repos share a licence copyright holder -> fork or rename."""
    a, b = holder_of(payload_a), holder_of(payload_b)
    if not a or not b:
        return False
    return a.lower() == b.lower()


def verdict(licence_text, readme_text=None):
    """One repo -> the row this KB is allowed to publish."""
    if licence_text is None:
        if readme_text:
            return {"state": "EXISTS-NOLICENCE", "family": None, "granted": False,
                    "holder": None,
                    "note": "real repo, no grant under %d probed names "
                            "(all rights reserved until shown otherwise)" % len(LICENCE_PATHS)}
        return {"state": "ABSENT", "family": None, "granted": False, "holder": None,
                "note": "no licence and no README/manifest"}
    fam, granted, why = reads_as_grant(licence_text)
    return {"state": "LICENSED" if granted else "NON-GRANT",
            "family": fam, "granted": granted, "holder": holder_of(licence_text),
            "note": why}


# ---------------------------------------------------------------- network
def probe_repo(repo, branches=("main", "master", "develop"), get=None):
    """Only network entry point. `get(url) -> (status, text)`; injectable."""
    if get is None:                                   # pragma: no cover
        import urllib.request

        def get(url):
            try:
                with urllib.request.urlopen(url, timeout=20) as r:
                    return r.status, r.read().decode("utf-8", "replace")
            except Exception as exc:
                return getattr(exc, "code", 0), ""
    base = "https://raw.githubusercontent.com/%s/%s/%s"
    for b in branches:
        for name in LICENCE_PATHS:
            st, body = get(base % (repo, b, name))
            if st == 200 and body.strip():
                v = verdict(body)
                v["path"] = "%s/%s" % (b, name)
                v["bytes"] = len(body.encode("utf-8"))
                return v
    for b in branches:
        for name in EXISTENCE_PATHS:
            st, body = get(base % (repo, b, name))
            if st == 200:
                v = verdict(None, readme_text=body or " ")
                v["path"] = "%s/%s" % (b, name)
                return v
    return verdict(None)
