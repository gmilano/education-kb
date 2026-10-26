#!/usr/bin/env python3
"""First-hand grant + liveness verification for p454's APAC/Global candidates,
using THIS pass's family reader (p453's mis-grades GPLv2 as LGPL and reports a
closed grant as UNREAD). Every read gates on curl's own %{http_code}."""
import hashlib, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

def load(n, p):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s)
    sv = sys.argv; sys.argv = [sv[0]]; s.loader.exec_module(m); sys.argv = sv; return m

v453 = load("v", os.path.join(ROOT, "compose/code/p453-vocabulary-ledger/verify.py"))
f454 = load("f", os.path.join(ROOT, "compose/code/p454-carried-cell-value/family_title.py"))

PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING", "license",
         "LICENSE-MIT", "MIT-LICENSE", "LICENSE.rst"]
READMES = ["README.md", "README.rst", "README.markdown", "readme.md", "README",
           "README.txt"]

CAND = [
    ("github.com/ardianryan/dapodik-sdk",         "npm @smansage/dapodik-sdk",        "MIT"),
    ("github.com/smantriplw/vervalpd-node",       "npm vervalpd-node",               ""),
    ("github.com/adereksisusanto/dapodik-api-php","packagist adereksisusanto/...",    ""),
    ("github.com/bantenprov/dapodik-data-guru",   "packagist bantenprov/...-guru",    ""),
    ("github.com/pipeworx-io/mcp-estat-japan",    "npm @pipeworx/mcp-estat-japan",    "MIT"),
    ("github.com/edu-sharing/Edu-Sharing",        "npm ngx-edu-sharing-api",          "GNU GPL v2"),
    # Fabricated negative control -- must be unreachable on every probe.
    ("github.com/nope-p454-dapodik/nope-p454",    "(fabricated control)",             ""),
]

print(f"{'address':46s} {'README':16s} {'grant path':14s} {'family (p454)':34s} {'bytes':>8s}  sha256_12")
for addr, origin, declared in CAND:
    slug = "/".join(addr.split("/")[1:])
    rd, rdcode = "--", "000"
    for r in READMES:
        b, c, s = v453.fetch(f"https://raw.githubusercontent.com/{slug}/HEAD/{r}")
        if c == "200" and b:
            rd, rdcode, rdbytes = r, c, s
            break
    gp, fam, size, sha = "--", "NO_PAYLOAD", 0, ""
    for p in PATHS:
        b, c, s = v453.fetch(f"https://raw.githubusercontent.com/{slug}/HEAD/{p}")
        if c == "200" and b:
            gp, fam, size = p, f454.family(b), s
            sha = hashlib.sha256(b.encode()).hexdigest()[:12]
            old = v453.family(b)
            if old != fam:
                fam = f"{fam}   [p453 reader: {old}]"
            break
    print(f"{addr:46s} {rd:16s} {gp:14s} {fam:34s} {size:8d}  {sha}")
    print(f"{'':46s} origin={origin}  registry_declared={declared!r}")
