#!/usr/bin/env python3
"""two_channel.py - grade a repo's liveness on BOTH channels, never one.

Pass 24 (registry-recency-channel) established the rule in prose:
  citing tier   -> git head commit  -> ANY commit, including a README typo
  installed tier-> registry release -> a DELIBERATE publication
Pass 329/330 then re-graded the whole shelf on the citing channel alone, and
mis-graded Cvmcosta/ltijs by 2.4 years (newest git tag v5.9.5 2024-05-01;
npm ltijs 7.0.7 2026-10-06).

This module makes the rule executable. verdict() refuses to return a liveness
grade when a package-bearing row has only one channel.
"""
import json
import subprocess
import urllib.request

STALE_DAYS = 365


def git_head_date(slug, host="https://github.com"):
    """Citing channel: ISO date of the head commit, or None if the slug does not resolve."""
    try:
        out = subprocess.run(
            ["git", "ls-remote", "%s/%s" % (host, slug), "HEAD"],
            capture_output=True, text=True, timeout=60)
    except (subprocess.SubprocessError, OSError):
        return None
    if out.returncode != 0 or not out.stdout.strip():
        return None
    return "RESOLVES"


def registry_release(pkg, registry):
    """Installed channel: (version, upload_date) of the latest release, or None."""
    if registry == "npm":
        url = "https://registry.npmjs.org/" + pkg
    elif registry == "pypi":
        url = "https://pypi.org/pypi/%s/json" % pkg
    else:
        raise ValueError("unknown registry: %s" % registry)
    try:
        with urllib.request.urlopen(url, timeout=35) as fh:
            d = json.load(fh)
    except Exception:
        return None
    if registry == "npm":
        latest = d.get("dist-tags", {}).get("latest")
        if not latest:
            return None
        return (latest, d.get("time", {}).get(latest, "")[:10])
    dated = sorted((f[0]["upload_time"][:10], v)
                   for v, f in d["releases"].items() if f)
    if not dated:
        return None
    return (d["info"]["version"], dated[-1][0])


def verdict(slug, pkg=None, registry=None, git_ok=None, release=None):
    """Return a liveness verdict, or UNGRADED when a packaged row has one channel.

    git_ok / release may be injected so the gate is testable offline.
    """
    if git_ok is None:
        git_ok = git_head_date(slug) is not None
    if pkg and release is None:
        release = registry_release(pkg, registry)

    if not git_ok and not pkg:
        return "NO-REF"
    if pkg and release is None:
        # resolves on git, absent from the registry it claims to ship to
        return "UNPUBLISHED" if git_ok else "NO-REF"
    if pkg is None:
        # not a packaged artefact: the citing channel is the whole story, and
        # that is a legitimate single-channel grade
        return "ALIVE-CITING-ONLY" if git_ok else "NO-REF"
    return "GRADED:%s@%s" % release


def gate(rows):
    """Refuse a shelf write when any packaged row carries only one channel.

    rows: iterable of dicts with keys slug, pkg, registry, release.
    Returns the list of offending slugs; empty means the write may proceed.
    """
    bad = []
    for r in rows:
        if r.get("pkg") and r.get("release") in (None, "", "-"):
            bad.append(r["slug"])
    return bad


if __name__ == "__main__":
    import sys
    for slug in sys.argv[1:]:
        print(slug, verdict(slug))
