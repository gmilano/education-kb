#!/usr/bin/env python3
"""The GitLab API channel — discovery, metadata, licence payload, licence set.

Pass 22 of the education KB (2026-10-06). Live instrument: every number this KB
publishes from this channel comes out of these four calls and nothing else.

    discovery      GET /api/v4/projects?search=TERM&order_by=star_count&...
    metadata       GET /api/v4/projects/:idEnc?license=true
    payload        GET /api/v4/projects/:idEnc/repository/files/:pathEnc/raw?ref=REF
    licence set    GET /api/v4/projects/:idEnc/repository/tree?path=LICENSES

Usage
    python3 gitlab_channel.py search "ai tutor" ["adaptive learning" ...]
    python3 gitlab_channel.py resolve owner/project [owner/project ...]
    python3 gitlab_channel.py payload owner/project
    python3 gitlab_channel.py control        # the negative controls, printed

Why `classify_payload` is anchored and not a substring match: see P-GL-3 in
README.md. A classifier that looks for licence names anywhere in a licence text
finds GPL inside MPL-2.0 and LGPL inside GPL-2.0, and both errors were made by
this pass's first draft.
"""
import json, sys, urllib.error, urllib.parse, urllib.request

API = "https://gitlab.com/api/v4"
UA = {"User-Agent": "globant-education-kb/pass22"}
HEAD_LINES = 6          # how far into a payload an anchored classifier may look

# (family, needle) in precedence order: the longer names must be tried first,
# because "GNU GENERAL PUBLIC LICENSE" is a substring of neither but
# "GENERAL PUBLIC LICENSE" is a substring of the Affero and Lesser titles.
ANCHORS = [
    ("AGPL",   "GNU AFFERO GENERAL PUBLIC LICENSE"),
    ("LGPL",   "GNU LESSER GENERAL PUBLIC LICENSE"),
    ("GPL",    "GNU GENERAL PUBLIC LICENSE"),
    ("Apache", "APACHE LICENSE"),
    ("MPL",    "MOZILLA PUBLIC LICENSE"),
    ("ECL",    "EDUCATIONAL COMMUNITY LICENSE"),
    ("MIT",    "MIT LICENSE"),
]


def _get(url, raw=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        body = r.read()
    return body if raw else json.loads(body)


def enc(slug):
    return urllib.parse.quote(slug, safe="")


def search(term, per_page=30):
    """Discovery. NOTE: `license=true` is accepted and SILENTLY IGNORED here."""
    q = urllib.parse.urlencode({"search": term, "order_by": "star_count", "sort": "desc",
                                "per_page": str(per_page), "license": "true", "archived": "false"})
    return _get(f"{API}/projects?{q}")


def resolve(slug):
    """Metadata + licence key + last_activity_at. Unknown slug -> HTTPError 404."""
    return _get(f"{API}/projects/{enc(slug)}?license=true")


def payload(slug, path, ref):
    return _get(f"{API}/projects/{enc(slug)}/repository/files/{enc(path)}/raw?ref={enc(ref)}", raw=True)


def licence_set(slug, path="LICENSES"):
    """The REUSE case: the root LICENSE is a pointer, the answer is this listing."""
    return [e["name"] for e in _get(f"{API}/projects/{enc(slug)}/repository/tree?path={enc(path)}&per_page=100")]


def classify_payload(text, head_lines=HEAD_LINES):
    """Anchored licence classifier: a licence name counts only when it is a TITLE.

    A title line is one whose stripped text *begins* with the licence name. That
    is the whole fix: GPL-2.0's body says "use the GNU Lesser General Public
    License instead" and MPL-2.0's body says "the GNU General Public License",
    but neither sentence begins a line with the name, so neither can be mistaken
    for a title. Scanning the first N lines was NOT enough -- the suite's
    negative control proved it.

    Returns (family, version|None). ('REUSE', None) for a pointer file,
    (None, None) when no title block names a licence.
    """
    if "reuse.software" in text.lower() or "REUSE best practices" in text:
        return ("REUSE", None)
    lines = [l.strip().upper() for l in text.splitlines() if l.strip()][:head_lines]
    for fam, needle in ANCHORS:
        for i, line in enumerate(lines):
            if line.startswith(needle):
                window = " ".join(lines[i:i + 2])
                ver = next((v for v in ("3", "2", "1") if f"VERSION {v}" in window), None)
                return (fam, ver)
    body = text.upper()[:1200]
    if "PERMISSION IS HEREBY GRANTED, FREE OF CHARGE" in body:
        return ("MIT", None)
    if "REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS" in body:
        return ("BSD", None)
    return (None, None)


def agrees(detector_key, family):
    """Does the forge's licence key name the same family the payload does?"""
    if not detector_key or not family:
        return False
    k = detector_key.lower()
    if family == "AGPL":
        return k.startswith("agpl")
    if family == "LGPL":
        return k.startswith("lgpl")
    if family == "GPL":
        return k.startswith("gpl")
    # REUSE (a pointer file) and any unknown family are never agreement.
    return {"Apache": "apache", "MIT": "mit", "BSD": "bsd",
            "MPL": "mpl", "ECL": "ecl"}.get(family, "\0no-such-key") in k


def controls():
    """The three controls this channel's claims rest on."""
    out = {}
    try:
        resolve("definitely-not-a-project-zzz9/nope")
        out["api_unknown_slug"] = "200 — DOES NOT DISCRIMINATE"
    except urllib.error.HTTPError as e:
        out["api_unknown_slug"] = f"{e.code} — DISCRIMINATES" if e.code == 404 else str(e.code)
    try:
        d = resolve("gitlab-org/gitlab-runner")
        out["single_project_license"] = (d.get("license") or {}).get("key")
    except Exception as e:
        out["single_project_license"] = f"ERR {e}"
    hits = search("ai tutor")
    out["search_license_served"] = sum(1 for p in hits if p.get("license"))
    out["search_hits"] = len(hits)
    return out


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "control"
    if cmd == "control":
        for k, v in controls().items():
            print(f"{k:28} {v}")
    elif cmd == "search":
        for term in sys.argv[2:]:
            hits = search(term)
            print(f"\n## {term}: {len(hits)} hits, {sum(1 for p in hits if p.get('license'))} with licence")
            for p in hits[:10]:
                print(f"  {p.get('star_count'):>5} {(p.get('last_activity_at') or '')[:10]} "
                      f"{p['path_with_namespace']}")
    elif cmd == "resolve":
        for slug in sys.argv[2:]:
            try:
                d = resolve(slug)
            except urllib.error.HTTPError as e:
                print(f"{e.code} {slug}")
                continue
            lic = d.get("license") or {}
            print(f"200 {slug} ★{d.get('star_count')} act={(d.get('last_activity_at') or '')[:10]} "
                  f"detector={lic.get('key')} license_url={d.get('license_url')}")
    elif cmd == "payload":
        slug = sys.argv[2]
        d = resolve(slug)
        lu = d.get("license_url") or ""
        if not lu:
            print(f"{slug}: NO licence payload declared")
            sys.exit(1)
        _, _, rest = lu.partition("/-/blob/")
        ref, _, path = rest.partition("/")
        body = payload(slug, path, ref).decode("utf-8", "replace")
        fam, ver = classify_payload(body)
        key = (d.get("license") or {}).get("key")
        print(f"{slug}\n  path={path}@{ref} bytes={len(body)}\n  detector={key}\n  payload={fam} {ver or ''}"
              f"\n  verdict={'AGREE' if agrees(key, fam) else 'CHECK'}")
        if fam == "REUSE":
            print("  licence set:", licence_set(slug))
    else:
        print(__doc__)
        sys.exit(2)
