#!/usr/bin/env python3
"""Measure an npm-published MCP server's LICENSE and TOOL SURFACE from the
registry tarball -- no install, no running server, no GitHub API.

Why this exists (pase 49). Two channels this KB had written off:

  * `tools` counts: declared NOT reproducible since the figure inventory began
    ("tools/list over stdio against the server -- needs the package
    installed"). **326 such figures across the eight files.**
  * licenses: declared NOT reproducible since pase 37, because github.com
    answers 403 to curl here and api.github.com answers 200 with a body that
    denies access.

Both are reachable without either channel. `registry.npmjs.org` serves the
metadata AND the published tarball, and the tarball carries the shipped
`package.json` plus the compiled server. So the tool surface can be counted
statically, and the license can be read from two independent artifacts (the
registry document and the manifest inside the tarball).

    python3 probe.py @ink-waffle/sisu-mcp
    python3 probe.py @ink-waffle/sisu-mcp --json

⚠ What this does NOT establish: a `license` FIELD is an assertion by the
publisher, not license TEXT. The probe reports the field and, separately,
whether a LICENSE file is actually shipped. For `@ink-waffle/sisu-mcp` the
field says MIT in both artifacts and **no license file exists in any channel**,
which is a different -- and worse -- fact than "unverified".
"""
from __future__ import annotations

import io
import json
import re
import sys
import tarfile
import urllib.parse
import urllib.request

REGISTRY = "https://registry.npmjs.org/"
TIMEOUT = 60

#: How an MCP server registers a tool, across the SDK versions in the wild.
TOOL_CALL = re.compile(r"registerTool\s*\(|\.\s*tool\s*\(|setRequestHandler\s*\(")
#: A tool NAME literal: the first argument of registerTool("...").
TOOL_NAME = re.compile(r"registerTool\s*\(\s*[\"']([A-Za-z0-9_.:-]+)[\"']")
#: The OLDER SDK shape, and the third pattern pase 49 met in the wild:
#: `getToolDefinitions()` returns `[{name: 'x', description, inputSchema}, ...]`.
#: Keyed on `name` AND `inputSchema` together -- `name:` alone appears on every
#: schema property in the file, so matching it alone over-counts by an order of
#: magnitude. @imazhar101/mcp-canvas-server is this shape.
TOOL_DEF = re.compile(
    r"[\"']?name[\"']?\s*:\s*[\"']([A-Za-z0-9_.:-]+)[\"']"
    r"(?=(?:[^{}]|\{[^{}]*\}){0,400}?inputSchema)",
    re.S)
LICENSE_FILE = re.compile(r"(^|/)(LICEN[CS]E|COPYING)(\.[A-Za-z]+)?$", re.I)


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": "kb-probe"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        data = r.read()
    return data if binary else json.loads(data)


def probe(pkg: str) -> dict:
    doc = fetch(REGISTRY + urllib.parse.quote(pkg, safe="@"))
    latest = doc.get("dist-tags", {}).get("latest")
    ver = doc.get("versions", {}).get(latest, {})
    out = {
        "package": pkg,
        "latest": latest,
        "license_registry": ver.get("license") or doc.get("license"),
        "repository": (ver.get("repository") or {}).get("url")
        if isinstance(ver.get("repository"), dict) else ver.get("repository"),
        "homepage": ver.get("homepage"),
        "tarball": ver.get("dist", {}).get("tarball"),
    }

    blob = fetch(out["tarball"], binary=True)
    out["tarball_bytes"] = len(blob)
    names, calls, tools, manifest_license, license_files = set(), 0, 0, None, []
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            rel = m.name.split("package/", 1)[-1]
            if LICENSE_FILE.search(rel):
                license_files.append(rel)
            if rel == "package.json":
                manifest_license = json.load(tf.extractfile(m)).get("license")
                continue
            if not rel.endswith((".js", ".mjs", ".cjs", ".ts")):
                continue
            if rel.endswith(".d.ts") or rel.endswith(".map"):
                continue
            try:
                src = tf.extractfile(m).read().decode("utf-8", "replace")
            except Exception:
                continue
            calls += len(TOOL_CALL.findall(src))
            found = set(TOOL_NAME.findall(src)) | set(TOOL_DEF.findall(src))
            names |= found
            tools += len(found)
    out["license_manifest"] = manifest_license
    out["license_files_shipped"] = license_files
    out["tool_names"] = sorted(names)
    out["tool_name_count"] = len(names)
    out["register_call_count"] = calls
    # Two independent counts. They agreeing is the verification; this probe
    # reports the disagreement rather than picking a favourite.
    # The SURFACE is the distinct-name count. `register_call_count` counts
    # occurrences, and a package that ships two builds (ESM + CJS) registers
    # every tool twice: @signdocs-brasil/mcp-server gives 37 occurrences for 26
    # distinct tools. Reporting the occurrence count as the tool count would
    # inflate the surface by 42 %.
    out["counts_agree"] = (len(names) == calls) if names else None
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    pkg = argv[1]
    r = probe(pkg)
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    print("package            : %s@%s" % (r["package"], r["latest"]))
    print("license (registry) : %s" % r["license_registry"])
    print("license (manifest) : %s" % r["license_manifest"])
    agree = r["license_registry"] == r["license_manifest"]
    print("  two artifacts agree: %s" % ("yes" if agree else "NO"))
    print("license FILE shipped: %s"
          % (", ".join(r["license_files_shipped"]) or
             "NONE -- the field is an assertion, there is no license text"))
    print("repository         : %s" % (r["repository"] or "NONE PUBLISHED"))
    print("tarball            : %d bytes" % r["tarball_bytes"])
    print("TOOL SURFACE       : %d distinct tool names" % r["tool_name_count"])
    print("  registration occurrences: %d%s" % (
        r["register_call_count"],
        "  (more than the surface: duplicate builds register twice)"
        if r["tool_name_count"] and r["register_call_count"] > r["tool_name_count"]
        else ""))
    for t in r["tool_names"]:
        print("    %s" % t)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
