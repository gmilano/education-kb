#!/usr/bin/env python3
"""p455 -- probe the candidate set first-hand. Registry for the back-link,
raw.githubusercontent for the grant, version axis for the grade.

`Gap 451`'s standing rule is enforced by construction: where a candidate was
found by PACKAGE NAME, the address is taken from the registry record's
repository field and NEVER derived from the name. 2 of 9 name-hits in that
pass belonged to third parties.
"""
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import family_version as fv
import fetch

# (label, registry_kind, registry_name, address_or_'' )
# An empty address means: RESOLVE IT FROM THE REGISTRY BACK-LINK.
CANDIDATES = [
    ("pronotepy",            "pypi",      "pronotepy",            ""),
    ("Pawnote",              "npm",       "pawnote",              ""),
    ("Pawdirecte",           "npm",       "pawdirecte",            ""),
    ("ecoledirecte.js",      "",          "",                      "a2br/ecoledirecte.js"),
    ("Linkdirecte",          "",          "",                      "Scolup/Linkdirecte"),
    ("ecole-directe-api",    "packagist", "studoo/ecole-directe-api", ""),
    ("LanisAPI",             "pypi",      "lanisapi",             ""),
    ("lanis-rs",             "crates",    "lanis-rs",             ""),
    ("maria (Lanis TS)",     "",          "",                      "elderguardian/maria"),
    ("WebUntis (SchoolUtils)", "npm",     "webuntis",             ""),
    ("webuntis_headless",    "npm",       "webuntis_headless",    ""),
    ("untis-api-client",     "npm",       "untis-api-client",     ""),
    ("untis-js",             "npm",       "untis-js",             ""),
    ("WebUntisAPI.Client",   "",          "",                      "Suiram1701/WebUntisAPI.Client"),
    ("WebUntisAPI (Java)",   "",          "",                      "Keule0010/WebUntisAPI"),
    ("education-crm",        "",          "",                      "asadbekme/education-crm"),
    ("moodle-mcp-server",    "",          "",                      "peancor/moodle-mcp-server"),
    ("tiny-llm",             "",          "",                      "skyzh/tiny-llm"),
    ("os-taxonomy",          "",          "",                      "withmarbleapp/os-taxonomy"),
]

SLUG = re.compile(r"github\.com[:/]+([^/]+/[^/#?]+?)(?:\.git)?/?$", re.I)


def slug_from(url):
    if not url:
        return ""
    url = url.strip().replace("git+", "").replace("git://", "https://")
    url = re.sub(r"#.*$", "", url)
    m = SLUG.search(url)
    return m.group(1) if m else ""


rows = []
print(f"{'label':24} {'address':46} {'declared':22} {'served':22} fwd")
print("-" * 130)
for label, kind, name, addr in CANDIDATES:
    declared, regver, backlink, regstatus = "", "", "", ""
    if kind:
        r = fetch.registry(kind, name)
        regstatus = r["status"]
        declared = r["declared"]
        regver = r["version"]
        backlink = r["backlink"]
        if not addr:
            addr = slug_from(backlink)
    if not addr:
        rows.append((label, "NO_ADDRESS_RESOLVED", declared, "", "", kind, name,
                     regver, regstatus, backlink, 0, "", ""))
        print(f"{label:24} {'-- NO ADDRESS FROM REGISTRY --':46} {declared[:22]:22}")
        continue
    g = fetch.grant(addr)
    served = fv.family(g["text"]) if g["verdict"] == "READ" else g["verdict"]
    fwd = fv.only_or_later(g["text"]) if g["verdict"] == "READ" else ""
    rows.append((label, addr, declared, served, fwd, kind, name, regver,
                 regstatus, backlink, g.get("bytes", 0), g.get("sha", ""),
                 g.get("path", g.get("live_path", "")) + "@" + (g.get("ref") or "")))
    print(f"{label:24} {addr:46} {declared[:22]:22} {served[:22]:22} {fwd}")

print("\n--- detail ---")
for (label, addr, declared, served, fwd, kind, name, regver, regstatus,
     backlink, nbytes, sha, where) in rows:
    agree = ""
    if declared and served and not served.isupper():
        cd, cs = fv.canon(declared), fv.canon(served)
        agree = "AGREE" if cd == cs else f"DISAGREE({cd} vs {cs})"
    print(f"{label}\n  addr={addr}\n  registry={kind}:{name}@{regver} status={regstatus} "
          f"declared={declared!r} backlink={backlink!r}\n"
          f"  served={served!r} fwd={fwd} at {where} {nbytes}B {sha} {agree}")

import json
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "probe.json"), "w") as fh:
    json.dump(rows, fh, indent=1)
