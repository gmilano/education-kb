#!/usr/bin/env python3
"""p853-slug-presence — the presence check `852-G3` / `T174` prescribed.

The defect it closes, measured at p852 in BOTH directions:

  (i)  UNDER-REPORTING.  A presence index keyed on `github.com/<owner>/<repo>`
       URLs reported `weizhenFrank/AutoGrader` ABSENT while the slug sat in
       `agents/trending.md` written as a bare `owner/repo` with no URL.
       A false NEW is a duplicate row.

  (ii) OVER-REPORTING.  A substring check reported `UOC/java-lti-1.3` PRESENT
       because `UOC/java-lti-1.3-provider` — a different, dead repository —
       contains it as a prefix.  A false PRESENT suppresses a live permissive row.

The contract, in one sentence: an address is PRESENT when this corpus names
THAT repository, in URL form or bare-slug form, at a word boundary that no
longer repository name can satisfy.

Offline.  No network.  `python3 -I` safe: no imports outside the stdlib and
no reliance on the script's own directory being on `sys.path`.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

# Hosts whose path begins with `<owner>/<repo>`.  `raw.githubusercontent.com`
# is here because this base's byte-reads are recorded as raw URLs, and a
# presence check that cannot see its own evidence channel is half blind.
URL_HOSTS = (
    r"github\.com",
    r"raw\.githubusercontent\.com",
    r"api\.github\.com/repos",
    r"codeload\.github\.com",
)

# A repository name may be extended by any of these characters, so none of
# them may sit immediately after a match: `java-lti-1.3` != `java-lti-1.3-provider`.
NAME_CHAR = r"A-Za-z0-9_.\-"


def _slug_parts(slug: str) -> tuple[str, str]:
    s = slug.strip().strip("/")
    for prefix in ("https://", "http://"):
        if s.startswith(prefix):
            s = s[len(prefix):]
    for host in ("github.com/", "raw.githubusercontent.com/", "www.github.com/"):
        if s.lower().startswith(host):
            s = s[len(host):]
    if s.endswith(".git"):
        s = s[: -len(".git")]
    parts = [p for p in s.split("/") if p]
    if len(parts) < 2:
        raise ValueError(f"not an owner/repo slug: {slug!r}")
    return parts[0], parts[1]


def patterns(slug: str) -> tuple[re.Pattern, re.Pattern]:
    """Return (url_form, bare_form) patterns for one `owner/repo`.

    Both reject a trailing name character, so a LONGER repository name can
    never satisfy a shorter one.  `.git` is accepted as a terminator because
    `owner/repo.git` IS that repository, while `owner/repo.js` is not.
    """
    owner, repo = (re.escape(p) for p in _slug_parts(slug))
    tail = r"(?:\.git)?(?![" + NAME_CHAR + r"])"
    url = re.compile(r"(?:" + "|".join(URL_HOSTS) + r")/" + owner + r"/" + repo + tail, re.I)
    # The bare form must NOT fire inside a longer path (`foo/owner/repo`),
    # which is why `/` is in the look-behind class; the URL form above is what
    # covers the legitimate `host/owner/repo` case.
    bare = re.compile(r"(?<![" + NAME_CHAR + r"/])" + owner + r"/" + repo + tail, re.I)
    return url, bare


def classify(slug: str, text: str) -> str:
    """`url`, `bare`, `both` or `absent` — the FORM matters, not just the bit.

    p852's under-reporting failure was invisible precisely because the index
    collapsed the form away.  Keeping it is what makes the failure reportable.
    """
    url, bare = patterns(slug)
    hit_url = bool(url.search(text))
    hit_bare = bool(bare.search(text))
    if hit_url and hit_bare:
        return "both"
    if hit_url:
        return "url"
    if hit_bare:
        return "bare"
    return "absent"


# The three shelves the count gate reads.  A slug on one of these is GRADED;
# a slug anywhere else in the corpus is written down but ungraded — p852's
# taxonomy, made mechanical.
SHELVES = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md")

# 🔴 Self-pollution, found while first running this instrument over the live
# corpus: this very file and its test suite NAME candidate slugs as fixtures,
# so a scan that reads `compose/code/` reports a never-before-seen candidate as
# already PRESENT — a false PRESENT, which is the `852-G3` over-reporting
# direction re-created by the repair itself.  Instrument directories are
# therefore reported in their own tier and never as corpus presence.
INSTRUMENT_PREFIX = "compose/code/"


def tier_of(rel_path: str) -> str:
    rel = rel_path.replace(os.sep, "/")
    if rel in SHELVES:
        return "shelf"
    if rel.startswith(INSTRUMENT_PREFIX):
        return "instrument"
    return "history"


def verdict(tiers) -> str:
    """SHELVED / UNGRADED / FIXTURE-ONLY / NEW — what a pass should DO with the address."""
    if "shelf" in tiers:
        return "SHELVED"
    if "history" in tiers:
        return "UNGRADED"
    if "instrument" in tiers:
        return "FIXTURE-ONLY"
    return "NEW"


def md_files(root: str, include_archive: bool = False):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in {".git", "__pycache__"} and (include_archive or d != "archive")
        )
        for name in sorted(filenames):
            if name.endswith((".md", ".tsv", ".txt", ".py", ".sh")):
                yield os.path.join(dirpath, name)


def scan(root: str, slugs, include_archive: bool = False):
    """{slug: {"state": ..., "hits": [(path, lineno, form, line)]}} — evidence, not a bit."""
    compiled = {s: patterns(s) for s in slugs}
    out = {s: {"state": "absent", "hits": []} for s in slugs}
    for path in md_files(root, include_archive):
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                for lineno, line in enumerate(fh, 1):
                    for slug, (url, bare) in compiled.items():
                        form = ""
                        if url.search(line):
                            form = "url"
                        if bare.search(line):
                            form = "both" if form else "bare"
                        if form:
                            rel = os.path.relpath(path, root)
                            out[slug]["hits"].append((rel, lineno, form, line.strip()[:160]))
        except OSError:
            continue
    for slug, rec in out.items():
        tiers = {tier_of(h[0]) for h in rec["hits"]}
        rec["tiers"] = tiers
        rec["verdict"] = verdict(tiers)
        forms = {h[2] for h in rec["hits"]}
        if not forms:
            rec["state"] = "absent"
        elif forms == {"url"}:
            rec["state"] = "url-only"
        elif forms == {"bare"}:
            rec["state"] = "bare-only"
        else:
            rec["state"] = "both"
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="word-boundary presence check for owner/repo addresses")
    ap.add_argument("slugs", nargs="+", help="owner/repo addresses (URLs accepted)")
    ap.add_argument("--root", default=".", help="corpus root (default: cwd)")
    ap.add_argument("--include-archive", action="store_true", help="also scan archive/")
    ap.add_argument("--evidence", action="store_true", help="print the matching lines")
    args = ap.parse_args(argv)

    result = scan(args.root, args.slugs, args.include_archive)
    width = max(len(s) for s in args.slugs)
    print(f"{'address':<{width}}  {'verdict':<13} {'form':<10} hits  where")
    for slug in args.slugs:
        rec = result[slug]
        form = {"absent": "—", "url-only": "url", "bare-only": "bare-only", "both": "both"}[rec["state"]]
        files = sorted({h[0] for h in rec["hits"] if tier_of(h[0]) != "instrument"})
        inst = sorted({h[0] for h in rec["hits"] if tier_of(h[0]) == "instrument"})
        where = ", ".join(files[:3]) or ("fixtures only: " + ", ".join(inst[:2]) if inst else "—")
        print(f"{slug:<{width}}  {rec['verdict']:<13} {form:<10} {len(rec['hits']):>4}  {where}")
        if args.evidence:
            for path, lineno, form, line in rec["hits"][:6]:
                print(f"    {path}:{lineno} [{form}] {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
