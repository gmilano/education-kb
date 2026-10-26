#!/usr/bin/env python3
"""p455 -- the read channel, in one place, with its gates stated.

Two rules this base learned the hard way and this file enforces:

1. `Gap 449-A`: `curl -sI https://github.com/...` returns 403 on EVERY real
   repo on this host, so a HEAD probe is a false-negative machine. The grant
   channel is `raw.githubusercontent.com`, gated on `%{http_code}`.

2. `Gap 453-E` (d) / `Gap 454-E`: an ungated byte-reader records
   `404: Not Found` -- 14 bytes -- as a licence. Every read here returns the
   HTTP status alongside the body and NO caller may look at the body without
   it.

Refs are resolved, never assumed: `Gap 454`'s shelf note records 13 of 58 live
addresses not on `main` (`master`, `develop`, `dev`, `release`, `development`,
`release_11`, `19.0`, `tcd`, `trunk`, `2.2`). `HEAD` on raw.githubusercontent
follows the repository's own default branch, which is why it is tried first.
"""
import hashlib
import json
import subprocess

UA = "globant-kb-education-research/p455"
REFS = ["HEAD", "main", "master", "develop", "dev", "development", "trunk"]
GRANT_PATHS = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
    "COPYING", "COPYING.txt", "COPYING.LESSER", "LICENSE-MIT",
    "license", "License", "LICENSE.rst", "docs/License.txt",
]
# `Gap 454-H`: a 404 on every grant path cannot distinguish "repository exists
# without a licence file" from "repository is gone". These paths answer that,
# and they must be NON-licence paths.
LIVE_PATHS = ["README.md", "readme.md", "README.rst", "README",
              "package.json", "pyproject.toml", "setup.py", "Cargo.toml",
              "composer.json", ".gitignore"]


def raw(owner_repo, ref, path, timeout=25):
    """(status, body_bytes). Status is read before the body, always."""
    url = f"https://raw.githubusercontent.com/{owner_repo}/{ref}/{path}"
    try:
        p = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A", UA,
             "-w", "\n%{http_code}", url],
            capture_output=True, timeout=timeout + 10)
    except subprocess.TimeoutExpired:
        return (0, b"")
    out = p.stdout
    i = out.rfind(b"\n")
    if i < 0:
        return (0, b"")
    try:
        status = int(out[i + 1:].strip() or 0)
    except ValueError:
        status = 0
    return (status, out[:i])


def digest(body):
    return hashlib.sha256(body).hexdigest()[:12]


def grant(owner_repo):
    """First readable grant payload across refs x paths, or a typed miss.

    Returns a dict. `verdict` is one of:
      READ              -- a payload was served; ref/path/bytes/sha recorded
      REPO_LIVE_NO_GRANT-- a non-licence path serves 200, no grant path does
      ADDRESS_DEAD      -- nothing serves 200 anywhere (`Gap 454-H`'s split)
    """
    for ref in REFS:
        for path in GRANT_PATHS:
            st, body = raw(owner_repo, ref, path)
            if st == 200 and body.strip():
                return {"verdict": "READ", "ref": ref, "path": path,
                        "bytes": len(body), "sha": digest(body),
                        "text": body.decode("utf-8", "replace")}
        # Only the first ref that resolves at all is worth a full path sweep;
        # if the whole ref 404s on README too, move on.
        st, _ = raw(owner_repo, ref, "README.md")
        if st != 200 and ref != REFS[-1]:
            continue
    for ref in REFS:
        for path in LIVE_PATHS:
            st, body = raw(owner_repo, ref, path)
            if st == 200 and body.strip():
                return {"verdict": "REPO_LIVE_NO_GRANT", "ref": ref,
                        "live_path": path, "bytes": 0, "sha": "", "text": ""}
    return {"verdict": "ADDRESS_DEAD", "ref": "", "bytes": 0, "sha": "", "text": ""}


def _curl_json(url, timeout=30):
    try:
        p = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A", UA,
             "-H", "Accept: application/json", "-w", "\n%{http_code}", url],
            capture_output=True, timeout=timeout + 10)
    except subprocess.TimeoutExpired:
        return (0, None)
    out = p.stdout
    i = out.rfind(b"\n")
    if i < 0:
        return (0, None)
    try:
        status = int(out[i + 1:].strip() or 0)
    except ValueError:
        return (0, None)
    if status != 200:
        return (status, None)
    try:
        return (status, json.loads(out[:i].decode("utf-8", "replace")))
    except json.JSONDecodeError:
        return (status, None)


# `Gap 455-C`: a 200 is NOT evidence of a well-formed record. This pass read
# `registry.npmjs.org/pawnote` twenty times; nineteen returned
# `1.6.2 / GPL-3.0-or-later / LiterateInk/Pawnote.js` and ONE returned HTTP 200
# with a body that parsed as JSON and carried no `dist-tags` at all. An
# unguarded parser records that as "the package declares no licence" -- a
# silent false negative on the exact channel every registry-sourced cell on
# these shelves rests on. The shape of the record is asserted, not assumed.
REQUIRED_SHAPE = {
    "pypi": ("info",),
    "npm": ("dist-tags", "versions"),
    "crates": ("crate",),
    "packagist": ("package",),
}


def _shape_ok(kind, d):
    return bool(d) and all(k in d for k in REQUIRED_SHAPE.get(kind, ()))


def registry(kind, name):
    """Declared licence + repository BACK-LINK from a package registry.

    `Gap 451`'s standing rule: the back-link is the evidence, NEVER the name.
    2 of 9 registry name-hits in that pass belonged to third parties, so a
    record is only usable here when it carries a repository URL of its own.

    `malformed` is True when the host served 200 and the body was not a record
    of the expected shape. A caller must treat that as NO READ, never as an
    absent declaration.
    """
    out = {"kind": kind, "name": name, "status": 0, "declared": "",
           "backlink": "", "version": "", "malformed": False}
    if kind == "pypi":
        st, d = _curl_json(f"https://pypi.org/pypi/{name}/json")
        out["status"] = st
        if not _shape_ok(kind, d):
            out["malformed"] = (st == 200)
            return out
        info = d.get("info", {})
        out["version"] = info.get("version", "")
        out["declared"] = (info.get("license") or "")[:120]
        exp = info.get("license_expression")
        if exp:
            out["declared"] = exp
        urls = info.get("project_urls") or {}
        for v in list(urls.values()) + [info.get("home_page") or ""]:
            if v and "github.com/" in v:
                out["backlink"] = v
                break
    elif kind == "npm":
        st, d = _curl_json(f"https://registry.npmjs.org/{name}")
        out["status"] = st
        if not _shape_ok(kind, d):
            out["malformed"] = (st == 200)
            return out
        latest = (d.get("dist-tags") or {}).get("latest", "")
        out["version"] = latest
        v = (d.get("versions") or {}).get(latest, {}) or {}
        lic = v.get("license") or d.get("license") or ""
        out["declared"] = lic if isinstance(lic, str) else json.dumps(lic)[:120]
        repo = v.get("repository") or d.get("repository") or {}
        url = repo.get("url", "") if isinstance(repo, dict) else str(repo)
        out["backlink"] = url
    elif kind == "crates":
        st, d = _curl_json(f"https://crates.io/api/v1/crates/{name}")
        out["status"] = st
        if not _shape_ok(kind, d):
            out["malformed"] = (st == 200)
            return out
        c = d.get("crate", {})
        out["version"] = c.get("max_version", "")
        out["backlink"] = c.get("repository") or ""
        vers = d.get("versions") or []
        if vers:
            out["declared"] = vers[0].get("license") or ""
    elif kind == "packagist":
        st, d = _curl_json(f"https://packagist.org/packages/{name}.json")
        out["status"] = st
        if not _shape_ok(kind, d):
            out["malformed"] = (st == 200)
            return out
        pkg = d.get("package", {})
        out["backlink"] = pkg.get("repository") or ""
        versions = pkg.get("versions") or {}
        for vname, v in versions.items():
            if "dev" in vname:
                continue
            lic = v.get("license") or []
            out["version"] = vname
            out["declared"] = ", ".join(lic) if isinstance(lic, list) else str(lic)
            break
    return out
