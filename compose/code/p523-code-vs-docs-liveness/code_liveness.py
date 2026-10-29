#!/usr/bin/env python3
"""p523 / code-vs-docs liveness.

The base's verification table (agents/top.md) records
`git clone --depth 1`, committer date as the AUTHORITATIVE liveness channel.
microsoft/autogen falsifies that: its HEAD commit is one day old and its
subject is "docs: add archive caution to landing page".

This instrument separates the last commit from the last commit THAT CHANGED
CODE, and reports the gap between them in days. A large gap is a project
that is publishing notices about itself, not shipping.

Offline-safe: every function takes a commit list, so the suite runs with no
network. Only `measure()` clones.
"""
import datetime as _dt
import os
import re
import subprocess
import sys

# Paths whose change does not constitute shipping. Deliberately conservative:
# a file is DOCS only if it is unambiguously prose or project metadata.
DOCS_RE = re.compile(
    r"""(?xi)
    ^(docs?|documentation|website|site|\.github|examples?|notebook|blog)/
  | (^|/)(README|CHANGELOG|CONTRIBUTING|CODE_OF_CONDUCT|SECURITY
         |SUPPORT|MAINTAINERS|AUTHORS|NOTICE|CITATION|ROADMAP|GOVERNANCE)
        (\.[A-Za-z0-9]+)?$
  | \.(md|rst|txt|adoc)$
  | ^LICENSE
    """
)

# A commit subject that announces the project's own retirement. These are the
# commits a liveness reader must not count as activity.
# `archive` is the trap: "use archive link of the tutorial" is a URL, not a
# retirement. So the archive arm must be followed by a word about THE PROJECT,
# and any archive-as-a-location phrasing is excluded outright.
# Negative controls for this live in the suite and are permanent.
_ARCHIVE_LOCATION = re.compile(
    r"(?i)\barchiv(e|ed)\s+(link|url|copy|version|page|snapshot)\b"
    r"|\barchive\.(org|is|ph)\b|\bweb\s*archive\b"
)
RETIRE_RE = re.compile(
    r"""(?xi)
    \b(unmaintained|no\ longer\ maintained|maintenance\ mode|sunset(ting)?
       |end\ of\ life|read[-\ ]only\ (mode|repo|repository))\b
  | \barchiv(e|ed|ing)\s+(caution|notice|banner|warning|status|disclaimer)\b
  | \barchiv(e|ed|ing)\b (?=.*\b(project|repo|repository|package|library
       |framework|this)\b)
  | \b(project|repo|repository|package|library|framework)\b (?=.*\barchiv(e|ed|ing)\b)
  | \bdeprecat(e|ed|ing)\s+(this|the)\s+(project|repo|repository|package
       |library|framework)\b
    """
)


def is_docs_only(paths):
    """True iff every path in the commit is prose/metadata. Empty -> not docs."""
    paths = [p for p in paths if p]
    if not paths:
        return False
    return all(DOCS_RE.search(p) for p in paths)


def announces_retirement(subject):
    """True only when the subject retires THE PROJECT.

    🔴 The first draft of this matched any `archiv*` and graded
    `open-spaced-repetition/fsrs4anki` NOTICES-ONLY on two 2024 commits that
    read "use archive link of Chinese version of the tutorial2". That is a
    4,119-star MIT row, and the false verdict would have kept it off the shelf.
    Both commits are permanent negative controls in the suite.
    """
    s = subject or ""
    if _ARCHIVE_LOCATION.search(s):
        return False
    return bool(RETIRE_RE.search(s))


def classify(commits):
    """commits: [{date: 'YYYY-MM-DD', sha, subject, paths: [...]}] newest first.

    Returns a verdict dict. `code_date` is the newest commit that touched a
    non-docs path; None if the window holds none.
    """
    head = commits[0] if commits else None
    code = next((c for c in commits if not is_docs_only(c["paths"])), None)
    retire = [c for c in commits if announces_retirement(c["subject"])]
    v = {
        "head_date": head["date"] if head else None,
        "head_sha": head["sha"] if head else None,
        "head_subject": head["subject"] if head else None,
        "head_is_docs_only": is_docs_only(head["paths"]) if head else None,
        "code_date": code["date"] if code else None,
        "code_sha": code["sha"] if code else None,
        "code_subject": code["subject"] if code else None,
        "retirement_commits": [(c["date"], c["sha"], c["subject"]) for c in retire],
        "window": len(commits),
    }
    v["gap_days"] = _days(v["code_date"], v["head_date"])
    # SHIPPING: code landed and nothing announces retirement.
    # NOTICES-ONLY: HEAD is docs and the window names its own retirement.
    if v["retirement_commits"] and v["head_is_docs_only"]:
        v["verdict"] = "NOTICES-ONLY"
    elif v["code_date"] is None:
        v["verdict"] = "NO-CODE-IN-WINDOW"
    elif v["gap_days"] is not None and v["gap_days"] >= 90:
        v["verdict"] = "STALE-CODE"
    else:
        v["verdict"] = "SHIPPING"
    return v


def _days(a, b):
    if not a or not b:
        return None
    f = "%Y-%m-%d"
    return (_dt.datetime.strptime(b, f) - _dt.datetime.strptime(a, f)).days


def measure(slug, window=60, workdir="/tmp/p523/clones"):
    """Clone shallow and read `window` commits with their changed paths."""
    os.makedirs(workdir, exist_ok=True)
    d = os.path.join(workdir, slug.replace("/", "%"))
    if not os.path.isdir(d):
        subprocess.run(
            ["git", "clone", "--filter=blob:none", "--no-checkout", "--quiet",
             f"https://github.com/{slug}", d],
            check=True, timeout=600,
        )
        subprocess.run(["git", "-C", d, "fetch", "--deepen", str(window), "--quiet"],
                       timeout=600)
    out = subprocess.run(
        ["git", "-C", d, "log", f"-{window}", "--name-only",
         "--format=%x00%cs%x1f%h%x1f%s"],
        capture_output=True, text=True, timeout=300,
    ).stdout
    commits = []
    for blk in out.split("\x00"):
        blk = blk.strip("\n")
        if not blk:
            continue
        head, _, rest = blk.partition("\n")
        parts = head.split("\x1f")
        if len(parts) < 3:
            continue
        commits.append({
            "date": parts[0], "sha": parts[1], "subject": parts[2],
            "paths": [p for p in rest.split("\n") if p.strip()],
        })
    return commits


if __name__ == "__main__":
    for slug in sys.argv[1:]:
        try:
            v = classify(measure(slug))
        except Exception as e:  # network/clone failure is a result, not a crash
            print(f"{slug}\tERROR\t{type(e).__name__}: {e}")
            continue
        print(f"{slug}\t{v['verdict']}\thead={v['head_date']}({v['head_sha']})"
              f"\tcode={v['code_date']}({v['code_sha']})\tgap={v['gap_days']}d"
              f"\tretire_notices={len(v['retirement_commits'])}")
        if v["verdict"] != "SHIPPING":
            print(f"    head_subject: {v['head_subject']}")
            print(f"    code_subject: {v['code_subject']}")
            for d, s, sub in v["retirement_commits"][:3]:
                print(f"    retires: {d} {s} {sub}")
