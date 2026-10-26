#!/usr/bin/env python3
"""p457 — full payload re-read census over every address carried on the primary shelves.

Closes Gap 456-A: p456 resolved refs for all 455 carried addresses but only re-read the
PAYLOAD for the 15 whose default branch fell outside the guessed list. The other 424 were
resolved and not read. This reads every one.

Channels (both established on this host, neither is curl -sI, which returns 403 on every
real repository here -- Gap 449-A):
  1. git ls-remote --symref <url> HEAD  -> existence + resolved default ref, authoritative
  2. curl on raw.githubusercontent.com/<slug>/HEAD/<path> -> the payload itself

Byte counts INCLUDE the trailing newline (the convention p450 fixed after shell command
substitution stripped it and manufactured a one-byte drift against three published cells).
Family is classified from the payload TITLE, never from a whole-body grep: GPL-3.0's closing
section recommends the LGPL (p450's defect) and a 40-line window mis-grades GPL-2.0 as LGPL
(p454's defect). Both defects are kept reproducible as negative controls in controls.py.
"""
import concurrent.futures as cf
import hashlib, json, os, re, subprocess, sys, tempfile

LICENCE_PATHS = ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
                 "COPYING", "COPYING.txt", "LICENSE.rst", "license", "LICENSE-MIT",
                 "COPYING.LESSER", "LICENSE.APACHE2"]

def sh(cmd, timeout=60):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"

def resolve(slug):
    """Channel 1. Returns (state, ref). state in {LIVE, DEAD}."""
    rc, out, err = sh(["git", "ls-remote", "--symref",
                       f"https://github.com/{slug}", "HEAD"], timeout=90)
    if rc != 0:
        return ("DEAD", None)
    m = re.search(r"^ref:\s+refs/heads/(\S+)\s+HEAD", out, re.M)
    if m:
        return ("LIVE", m.group(1))
    # resolved but no symref line: a repo that answers refs without a symbolic HEAD
    return ("LIVE", None) if out.strip() else ("DEAD", None)

def fetch(slug, path):
    """Channel 2. Returns (http_code, nbytes, sha256_12) -- bytes include trailing newline."""
    fd, tmp = tempfile.mkstemp(prefix="p457-")
    os.close(fd)
    try:
        rc, out, _ = sh(["curl", "-sL", "-o", tmp, "-w", "%{http_code}",
                         f"https://raw.githubusercontent.com/{slug}/HEAD/{path}"], timeout=60)
        code = out.strip() or "000"
        if rc != 0 or code != "200":
            return (code, 0, None)
        blob = open(tmp, "rb").read()
        return (code, len(blob), hashlib.sha256(blob).hexdigest()[:12])
    finally:
        try: os.unlink(tmp)
        except OSError: pass

TITLE_RULES = [
    # ordered; first match wins; applied to the title window only
    (r"GNU AFFERO GENERAL PUBLIC LICENSE", "AGPL-3.0"),
    (r"GNU LESSER GENERAL PUBLIC LICENSE.*Version 3", "LGPL-3.0"),
    (r"GNU LESSER GENERAL PUBLIC LICENSE.*Version 2\.1", "LGPL-2.1"),
    (r"GNU GENERAL PUBLIC LICENSE.*Version 3", "GPL-3.0"),
    (r"GNU GENERAL PUBLIC LICENSE.*Version 2", "GPL-2.0"),
    (r"Apache License\s*,?\s*Version 2\.0", "Apache-2.0"),
    (r"Mozilla Public License Version 2\.0", "MPL-2.0"),
    (r"Educational Community License.*Version 2\.0", "ECL-2.0"),
    (r"MIT License|Permission is hereby granted, free of charge", "MIT"),
    (r"Creative Commons", "CC"),
    (r"The Unlicense|This is free and unencumbered software", "Unlicense"),
    (r"ISC License", "ISC"),
    (r"BSD", "BSD"),
]

def classify(slug, path, nbytes):
    """Family from the TITLE WINDOW of the payload, re-fetched once. Never a body grep."""
    fd, tmp = tempfile.mkstemp(prefix="p457c-")
    os.close(fd)
    try:
        sh(["curl", "-sL", "-o", tmp,
            f"https://raw.githubusercontent.com/{slug}/HEAD/{path}"], timeout=60)
        text = open(tmp, "rb").read().decode("utf-8", "replace")
    finally:
        try: os.unlink(tmp)
        except OSError: pass
    head = "\n".join(text.splitlines()[:14])
    flat = re.sub(r"\s+", " ", head)
    for rx, fam in TITLE_RULES:
        if re.search(rx, flat, re.I):
            if fam == "BSD":  # count clauses, and only from the clause list
                n = len(re.findall(r"^\s*\d+\.\s|Redistributions", text[:2000], re.M))
                if "Neither the name" in text[:4000]:
                    return "BSD-3-Clause"
                return "BSD-2-Clause" if n else "BSD"
            return fam
    return "UNCLASSIFIED"

def one(slug):
    rec = {"slug": slug}
    state, ref = resolve(slug)
    rec["state"], rec["ref"] = state, ref
    if state == "DEAD":
        rec["verdict"] = "ADDRESS_DEAD"
        return rec
    for path in LICENCE_PATHS:
        code, nb, dig = fetch(slug, path)
        if code == "200" and nb > 0:
            rec.update(path=path, bytes=nb, sha256_12=dig,
                       family=classify(slug, path, nb), verdict="PAYLOAD_READ")
            return rec
    rec["verdict"] = "REPO_LIVE_NO_GRANT"
    return rec

def main():
    addresses = sorted(json.load(open(sys.argv[1])).keys())
    # Controls, both directions, run inside the sweep -- a fabricated slug MUST come back dead.
    controls = ["gmilano/this-repository-does-not-exist-p457",
                "HKUDS/DeepTutor", "moodle/moodle"]
    todo = addresses + [c for c in controls if c not in addresses]
    out = {}
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for rec in ex.map(one, todo):
            out[rec["slug"]] = rec
            print(rec["verdict"], rec["slug"], rec.get("family", ""),
                  rec.get("bytes", ""), rec.get("ref", ""), flush=True)
    json.dump(out, open(sys.argv[2], "w"), indent=0, sort_keys=True)

if __name__ == "__main__":
    main()
