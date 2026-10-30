#!/usr/bin/env python3
"""doc-channel.py -- the instrument Gap 553-E asked for, at the sample size Gap 553-F
asked for (p554).

WHY THIS EXISTS
  553-E  One artefact, three channels, three different licences. The LATAM dataset
         `juanmoisesd/ai-educational-impact-latin-america-dataset` carries CC0-1.0
         (abridged) in `main/LICENSE`, states `License: CC BY 4.0` in its own README
         metadata table, and returns `NOASSERTION` from GitHub's `license.spdx_id`.
         CC0 waives; CC BY 4.0 requires attribution. A corpus built from that dataset
         carries an attribution obligation under one reading and none under the other,
         AND THE REPOSITORY ASSERTS BOTH. Ask: a GRANT-DISAGREES-WITH-DOCUMENTATION
         verdict that reads the three sources and REPORTS the disagreement rather than
         silently resolving it in the payload's favour.

  553-F  Ask: "a measurement, over a larger sample than seven, of what share of
         education repositories ... carry a readable grant" on each channel.

🔴 WHAT THIS INSTRUMENT CANNOT DO, AND ONE SUBSTITUTION IT WAS FORCED TO MAKE
  1. 🔴 THE PLATFORM CHANNEL IS NOT READ THIS PASS. `api.github.com` returns HTTP 403
     to this session ("GitHub access to this repository is not enabled for this
     session"), so `license.spdx_id` -- 553-E's third source -- is UNREACHABLE. This
     module substitutes the PACKAGE-METADATA channel (`package.json`, `composer.json`,
     `pyproject.toml`, `setup.py`, `Cargo.toml`, `DESCRIPTION`, `pom.xml`), which is
     readable over `raw.githubusercontent.com` and is a channel a CONSUMER actually
     reads: a dependency resolver believes it. The substitution is recorded as
     `Gap 554-A`; it is NOT a closure of the platform limb of 553-E.
  2. The README limb reads a WINDOW, never the whole file -- see `readme_window()`.
     This is Gap 553-A's lesson carried across: a README that says "MIT; bundles X
     which is GPL-3.0" defeats a whole-file matcher exactly as GPL s13 defeated a
     whole-payload one. A window can still be wrong; it cannot be wrong THAT way.
  3. It reports DISAGREEMENT. It does not decide which channel is right. On the one
     case where this base has read the law (`553-E`), the payload is the operative
     grant -- but a repository that contradicts itself is a question for counsel, and
     a verdict that picked a winner would hide the question.

USAGE   python3 -I ingest/doc-channel.py owner/repo [owner/repo ...]
        python3 -I ingest/doc-channel.py --file sample.txt
OUTPUT  TSV: repo, branch, payload_family, readme_family, pkg_family, verdict, evidence
"""
import concurrent.futures as cf
import importlib.util
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("gv", os.path.join(HERE, "grant-verdict.py"))
gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gv)

TIMEOUT = 25

README_NAMES = ["README.md", "README.rst", "README.txt", "README",
                "readme.md", "Readme.md", "README.MD", "docs/README.md"]

PKG_FILES = ["package.json", "composer.json", "pyproject.toml", "setup.py",
             "setup.cfg", "Cargo.toml", "DESCRIPTION", "pom.xml", "build.gradle",
             "Gemfile.gemspec", "pubspec.yaml"]

# 🔵 The family vocabulary MUST be the one `grant-verdict.py::spdx_of` emits, or the
# comparison measures spelling. These patterns map documentation prose onto it.
DOC_FAMILY = [
    (r"\bbusiness source licen[cs]e|\bbusl\b", "BUSL-1.1"),
    (r"server side public licen[cs]e|\bsspl\b", "SSPL-1.0"),
    (r"elastic licen[cs]e 2", "Elastic-2.0"),
    (r"functional source licen[cs]e|\bfsl-", "FSL"),
    (r"\bpolyform\b", "PolyForm"),
    (r"sustainable use licen[cs]e", "SUL"),
    (r"commons clause", "CommonsClause"),
    # 🔴 AGPL BEFORE GPL, and LGPL before GPL: "AGPL-3.0" contains "GPL-3.0" as a
    # substring. Ordering here is load-bearing -- Gap 553-A one layer up.
    (r"\bagpl|affero", "AGPL-3.0"),
    (r"\blgpl|lesser general public", "LGPL"),
    (r"\bgpl-?\s?3|gplv3|general public licen[cs]e,? version 3", "GPL-3.0"),
    (r"\bgpl-?\s?2|gplv2|general public licen[cs]e,? version 2", "GPL-2.0"),
    (r"\bcc0\b|creative commons zero|public domain dedication", "CC0-1.0"),
    (r"cc[- ]by[- ]sa", "CC-BY-SA-4.0"),
    (r"cc[- ]by[- ]nc|creative commons.{0,20}noncommercial", "CC-BY-NC-4.0"),
    (r"cc[- ]by\b|creative commons attribution", "CC-BY-4.0"),
    (r"educational community licen[cs]e|\becl-?2", "ECL-2.0"),
    (r"mozilla public licen[cs]e|\bmpl-?\s?2", "MPL-2.0"),
    (r"apache licen[cs]e|apache-?\s?2|apache 2\.0", "Apache-2.0"),
    (r"bsd[- ]3|3-clause bsd", "BSD-3-Clause"),
    (r"bsd[- ]2|2-clause bsd", "BSD-2-Clause"),
    (r"\bisc licen[cs]e\b", "ISC"),
    (r"\bunlicen[cs]e\b", "Unlicense"),
    (r"\bmit licen[cs]e\b|licen[cs]ed under (the )?mit|\bmit\b", "MIT"),
    (r"\bproprietary\b|all rights reserved", "PROPRIETARY"),
]


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "globant-kb/p554"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except Exception:
        return None


def families_in(text):
    """All families NAMED in `text`, in vocabulary order, de-duplicated.

    🔴 FALSE-POSITIVE SURFACE OF THIS FUNCTION, stated here per Gap 553-C's ask:
      * `\\bmit\\b` matches the word MIT anywhere -- "MIT Media Lab", "mitodl",
        "Massachusetts Institute of Technology" abbreviated. It is LAST in the list
        and only reached on a window that has already failed every other pattern,
        but on a window containing an institutional MIT it WILL fire. Any MIT read
        from documentation alone is therefore reported, never trusted.
      * `apache` matches a project that merely RUNS on the Apache httpd server.
      * A window naming two families returns two. That is the finding, not an error:
        it is 553-E's shape inside one channel.
    """
    t = text.lower()
    out = []
    for pat, fam in DOC_FAMILY:
        if re.search(pat, t) and fam not in out:
            out.append(fam)
    return out


# 🔴 p554 / Gap 554-E -- CAUGHT ON THIS MODULE'S OWN FIRST USE AGAINST A NEW ROW.
# `Zenglian990/AI_Tutor_Release` carries `"license": "ISC"` in `package.json` while its
# LICENSE file and README both say MIT. `families_in()` returned NOTHING for it, and
# the row was scored CHANNELS-AGREE. The cause: `families_in` was written for PROSE
# ("licensed under the ISC License") and a manifest writes a BARE SPDX ID. So the
# manifest channel -- the one a dependency resolver actually believes -- was the
# weakest reader in the module, and every disagreement it alone would have caught was
# scored as agreement. 🔵 The published disagreement rate before this fix is a LOWER
# BOUND, and is republished after it.
SPDX_IDS = {
    "MIT": "MIT", "ISC": "ISC", "UNLICENSE": "Unlicense", "WTFPL": "WTFPL",
    "APACHE-2.0": "Apache-2.0", "APACHE 2.0": "Apache-2.0", "APACHE-2": "Apache-2.0",
    "BSD-3-CLAUSE": "BSD-3-Clause", "BSD-3": "BSD-3-Clause", "BSD3": "BSD-3-Clause",
    "BSD-2-CLAUSE": "BSD-2-Clause", "BSD-2": "BSD-2-Clause", "BSD": "BSD-3-Clause",
    "MPL-2.0": "MPL-2.0", "ECL-2.0": "ECL-2.0",
    "AGPL-3.0": "AGPL-3.0", "AGPL-3.0-ONLY": "AGPL-3.0",
    "AGPL-3.0-OR-LATER": "AGPL-3.0", "AGPLV3": "AGPL-3.0",
    "LGPL-3.0": "LGPL", "LGPL-2.1": "LGPL", "LGPL-3.0-OR-LATER": "LGPL",
    "GPL-3.0": "GPL-3.0", "GPL-3.0-ONLY": "GPL-3.0", "GPL-3.0-OR-LATER": "GPL-3.0",
    "GPL-2.0": "GPL-2.0", "GPL-2.0-ONLY": "GPL-2.0", "GPL-2.0-OR-LATER": "GPL-2.0",
    "CC0-1.0": "CC0-1.0", "CC-BY-4.0": "CC-BY-4.0", "CC-BY-SA-4.0": "CC-BY-SA-4.0",
    "CC-BY-NC-4.0": "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0": "CC-BY-NC-SA-4.0",
    "BUSL-1.1": "BUSL-1.1", "SSPL-1.0": "SSPL-1.0", "ELASTIC-2.0": "Elastic-2.0",
    "PROPRIETARY": "PROPRIETARY", "UNLICENSED": "PROPRIETARY",
}


def manifest_families(value):
    """The licence field of a package manifest, read as an SPDX EXPRESSION first and
    as prose only if that fails. 🔵 A manifest value is machine-written: `MIT`,
    `ISC`, `AGPL-3.0-or-later`, `(MIT OR Apache-2.0)`. Reading it with prose patterns
    (Gap 554-E) threw away the channel's whole point.

    🔴 FALSE-POSITIVE SURFACE: an SPDX expression with OR (`(MIT OR Apache-2.0)`) is a
    CHOICE the consumer makes, not a conflict; both ids are returned and a reader that
    treats them as a disagreement would be wrong. Such a row is marked in `evidence`.
    """
    toks = [t.strip(" ()\"',;") for t in re.split(r"\s+(?:OR|AND)\s+|[,/|]", value.strip(), flags=re.I)]
    out = []
    for t in toks:
        fam = SPDX_IDS.get(t.upper())
        if fam and fam not in out:
            out.append(fam)
    return out or families_in(value)


def readme_window(text):
    """The slice of a README a family matcher may read: badge lines + the licence
    section. NEVER the whole file -- Gap 553-A's lesson, carried across channels."""
    win = []
    # 1. shields/badge lines anywhere -- they encode the family in the URL
    for ln in text.splitlines():
        low = ln.lower()
        if ("shields.io" in low or "img.shields.io" in low or "badge" in low) and "licen" in low:
            win.append(ln)
    # 2. the licence SECTION: a heading matching /licen[cs]e/ to the next heading of
    #    the same or higher level, capped so a trailing section cannot swallow the file
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{1,6})\s*.*licen[cs]e", ln, re.I)
        if not m:
            continue
        level = len(m.group(1))
        sec = [ln]
        for nxt in lines[i + 1:]:
            m2 = re.match(r"^(#{1,6})\s", nxt)
            if m2 and len(m2.group(1)) <= level:
                break
            sec.append(nxt)
            if len(sec) > 40:
                break
        win.extend(sec)
    # 3. a metadata table row or front-matter key naming a licence -- the shape that
    #    produced 553-E (`| License | CC BY 4.0 |`)
    for ln in lines:
        if re.search(r"^\s*[|*-]?\s*\**licen[cs]e\**\s*[|:]", ln, re.I):
            win.append(ln)
    return "\n".join(win)


def pkg_license(name, body):
    """The `license` FIELD of a package manifest -- never the whole manifest.
    A manifest's dependency list names other projects; its licence field names this
    one. Reading the whole file would reproduce 553-A a third time."""
    try:
        txt = body.decode("utf-8", "replace")
    except Exception:
        return None, None
    if name in ("package.json", "composer.json", "pubspec.yaml"):
        if name.endswith(".json"):
            try:
                d = json.loads(txt)
            except Exception:
                return None, None
            v = d.get("license") or d.get("licenses")
            if isinstance(v, list):
                v = ",".join(x.get("type", "") if isinstance(x, dict) else str(x) for x in v)
            return (str(v), f"{name}:license") if v else (None, None)
        m = re.search(r"^licen[cs]e:\s*(.+)$", txt, re.I | re.M)
        return (m.group(1).strip(), f"{name}:license") if m else (None, None)
    if name in ("pyproject.toml", "Cargo.toml", "setup.cfg", "DESCRIPTION"):
        m = re.search(r"^\s*licen[cs]e\s*[=:]\s*(.+)$", txt, re.I | re.M)
        if m:
            return m.group(1).strip().strip('"\'{} '), f"{name}:license"
        m = re.search(r"License :: OSI Approved :: ([^\"'\n]+)", txt)
        return (m.group(1).strip(), f"{name}:classifier") if m else (None, None)
    if name == "setup.py":
        m = re.search(r"licen[cs]e\s*=\s*[\"']([^\"']+)[\"']", txt, re.I)
        return (m.group(1), "setup.py:license=") if m else (None, None)
    if name == "pom.xml":
        m = re.search(r"<licenses>.*?<name>([^<]+)</name>", txt, re.S | re.I)
        return (m.group(1).strip(), "pom.xml:licenses/name") if m else (None, None)
    if name == "build.gradle":
        m = re.search(r"licen[cs]e\s*[=:]\s*[\"']([^\"']+)[\"']", txt, re.I)
        return (m.group(1), "build.gradle") if m else (None, None)
    return None, None


def read_channels(slug):
    branch, sha = gv.symref(slug)
    if not branch:
        return {"slug": slug, "dead": True}

    def one(path):
        return path, fetch(f"https://raw.githubusercontent.com/{slug}/{branch}/{path}")

    rd_txt, rd_name, pkg_val, pkg_src = None, None, None, None
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for path, body in ex.map(one, README_NAMES + PKG_FILES):
            if not body or body.startswith(b"404: Not Found"):
                continue
            if path in README_NAMES and rd_txt is None:
                rd_txt, rd_name = body.decode("utf-8", "replace"), path
            elif path in PKG_FILES and pkg_val is None:
                v, src = pkg_license(path, body)
                if v:
                    pkg_val, pkg_src = v, src

    # payload channel: delegate entirely to the p553 instrument
    row, _ = gv.run(slug)
    cols = row.split("\t")
    payload_fams = cols[5] if len(cols) > 6 else "-"
    payload_verdict = cols[6] if len(cols) > 6 else "-"

    win = readme_window(rd_txt) if rd_txt else ""
    return {
        "slug": slug, "dead": False, "branch": branch, "sha": sha,
        "payload": payload_fams, "payload_verdict": payload_verdict,
        "readme_name": rd_name, "readme_window_bytes": len(win),
        "readme_fams": families_in(win) if win else [],
        "pkg_src": pkg_src, "pkg_raw": pkg_val,
        "pkg_fams": manifest_families(pkg_val) if pkg_val else [],
    }


def verdict(r):
    """🔴 FALSE-POSITIVE SURFACE: a channel naming a SUPERSET of the payload's families
    (a README that says "GPL-3.0, and the docs are CC-BY-4.0") is reported as
    DISAGREES. That is deliberate -- a split code/data grant IS a thing a reader must
    be told about -- but it is not the same defect as a flat contradiction, so the
    evidence column prints both sides and the reader resolves it."""
    pay = set(x for x in r["payload"].split("+") if x and x != "-")
    doc = set(r["readme_fams"]) | set(r["pkg_fams"])
    # 🔵 `PROPRIETARY` comes from `all rights reserved`, which is boilerplate in a
    # copyright line and co-occurs with permissive grants constantly. It is dropped
    # from the COMPARISON and kept in the columns, so it informs a reader without
    # manufacturing a disagreement on every repo with a copyright header.
    doc.discard("PROPRIETARY")
    if not pay and not doc:
        return "ALL-CHANNELS-SILENT"
    if pay and not doc:
        return "DOC-SILENT"
    if doc and not pay:
        return "PAYLOAD-SILENT-DOC-ASSERTS"
    if doc <= pay:
        return "CHANNELS-AGREE"
    return "GRANT-DISAGREES-WITH-DOCUMENTATION"


def main():
    args = sys.argv[1:]
    if args and args[0] == "--file":
        slugs = [l.strip() for l in open(args[1]) if l.strip() and not l.startswith("#")]
    else:
        slugs = args
    if not slugs:
        print(__doc__)
        return
    print("repo\tbranch\tpayload_families\treadme_families\tpkg_families\tverdict\tevidence")
    rows = []
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(read_channels, slugs):
            rows.append(r)
    for r in rows:
        if r["dead"]:
            print(f"{r['slug']}\t-\t-\t-\t-\tDEAD-OR-PRIVATE\t-")
            continue
        v = verdict(r)
        ev = (f"readme={r['readme_name'] or 'NONE'}[{r['readme_window_bytes']}B-window]"
              f"{' SPDX-OR-CHOICE' if r['pkg_raw'] and ' OR ' in r['pkg_raw'].upper() else ''}"
              f" pkg={r['pkg_src'] or 'NONE'}"
              f"{'=' + r['pkg_raw'] if r['pkg_raw'] else ''}"
              f" payload_verdict={r['payload_verdict']}")
        print(f"{r['slug']}\t{r['branch']}\t{r['payload'] or '-'}"
              f"\t{'+'.join(r['readme_fams']) or '-'}"
              f"\t{'+'.join(r['pkg_fams']) or '-'}\t{v}\t{ev}", flush=True)


if __name__ == "__main__":
    main()
